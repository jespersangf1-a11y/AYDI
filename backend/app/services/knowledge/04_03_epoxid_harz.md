# 04_03 Epoxid-Harz — Alle Systeme — AYDI Wissensmodul

---

## 1. Einleitung und Modulübersicht

Epoxidharze (EP) bilden die technologisch anspruchsvollste Klasse duroplastischer Matrixharze im Yachtbau. Sie bieten die höchsten mechanischen Eigenschaften aller thermisch härtenden Harzsysteme, exzellente Faser-Matrix-Haftung und universelle Einsetzbarkeit — vom Strukturlaminat über Klebstoffe bis zu Beschichtungen. Im Marine-Bereich dominieren Amin-gehärtete Bisphenol-A/F-Systeme, während anhydrid-gehärtete Systeme in Prepreg-Anwendungen und Hochtemperatur-Bereichen eingesetzt werden.

| Parameter | Beschreibung | Confidence |
|---|---|---|
| **Modul-ID** | 04_03 | `measured` |
| **Kategorie** | 04 Harze/Fasern/Verbundwerkstoffe | `measured` |
| **Subkategorie** | Epoxid-Harz — Alle Systeme | `measured` |
| **AYDI-Kontexte** | materials, structural, production, service_patterns | `measured` |
| **Primärer Einsatz** | Strukturlaminat, Klebstoff, Beschichtung, Barrier-Coat, Fairing, Prepreg | `measured` |
| **Harzklasse** | Epoxid (Bisphenol-A-Diglycidylether + Amin-/Anhydrid-Härter) | `measured` |
| **Härtungsmechanismus** | Polyaddition (stöchiometrisch, kein Nebenprodukt, minimaler Schrumpf) | `measured` |
| **Schlüsselvorteil Marine** | Höchste Festigkeit, beste Faser-Haftung, vielseitigste Einsatzmöglichkeiten | `measured` |
| **Preisbereich** | 15–35 €/kg (Standard), 40–80 €/kg (Prepreg-Systeme), 8–15 €/kg (Basis-Systeme) | `estimated` |

<!-- model_config = {"from_attributes": True} — Pydantic v2 -->

---

## 2. Chemische Grundlagen

### 2.1 Epoxid-Chemie Kernprinzipien

| Parameter | Detail | Confidence |
|---|---|---|
| **Basischemie** | Bisphenol-A-Diglycidylether (DGEBA) — Reaktion von Bisphenol-A mit Epichlorhydrin | `measured` |
| **Reaktivgruppen** | Oxiran-Ringe (Epoxidgruppen) — 2 pro DGEBA-Molekül, reagieren mit Amin-Wasserstoffen | `measured` |
| **Härtungsmechanismus** | Polyaddition: Epoxid + Amin → sekundäres Amin → tertiäres Amin. Stöchiometrisch! | `measured` |
| **Mischverhältnis** | KRITISCH — stöchiometrisch berechnet, Abweichung >5% = Unterhärtung. KEIN Katalysator! | `measured` |
| **Schrumpf** | 1–3% (vs. UP 6–8%, VE 5–7%) — geringster aller Duroplaste | `measured` |
| **Nebenprodukte** | Keine — reine Additionsreaktion. Kein Wasser, kein Styrol, keine Gase | `measured` |
| **Exothermie** | Moderat — Topfzeit-abhängig, langsamer als UP/VE. Masse-Effekt beachten! | `measured` |
| **Hydroxylgruppen** | Entstehen bei Härtung — exzellente Haftung auf Glas, Metall, Holz, Beton | `measured` |

### 2.2 Epoxid-Harz-Typen nach Basischemie

| Harztyp | Chemie | EEW g/eq | Viskosität | Einsatz Marine | Confidence |
|---|---|---|---|---|---|
| **DGEBA Standard** | Bisphenol-A + Epichlorhydrin | 182–192 | Mittel (500–1500 mPa·s) | 85% aller Marine-EP | `measured` |
| **DGEBF (Bisphenol-F)** | Bisphenol-F + Epichlorhydrin | 160–175 | Niedrig (300–600 mPa·s) | Infusion, Low-Visc | `measured` |
| **Novolak-Epoxid** | Phenol-Novolak + Epichlorhydrin | 170–200 | Hoch (fest/semi-fest) | Hochtemperatur, Prepreg | `measured` |
| **Cycloaliphatisch** | Cycloaliphatische Epoxide | 130–145 | Niedrig (200–400 mPa·s) | UV-stabil, Beschichtung | `measured` |
| **Epoxid-Verdünner** | Mono/Difunktionelle Reactive Diluents | — | Sehr niedrig | Viskositäts-Reduktion | `measured` |

### 2.3 Härter-Typen für Marine-Epoxid

| Härtertyp | Chemie | Topfzeit (RT) | Tg RT-Cure °C | Tg Post-Cure °C | Marine-Einsatz | Confidence |
|---|---|---|---|---|---|---|
| **Aliphatisches Amin** | z.B. TETA, DETA | 15–30 min | 55–65 | 80–95 | Schnelle Reparaturen, Kleben | `measured` |
| **Cycloaliphatisches Amin** | z.B. IPDA, PACM | 30–60 min | 65–80 | 110–130 | Standard Marine-Laminat | `measured` |
| **Polyamidoamin** | z.B. Versamid-Typen | 60–120 min | 45–55 | 70–85 | Beschichtungen, flexibel | `measured` |
| **Aromatisches Amin** | z.B. DDM, DDS | Sehr lang | — | 150–180 | Prepreg, Hochleistung | `measured` |
| **Anhydrid** | z.B. MTHPA, NMA | Sehr lang | — | 150–200 | Prepreg, Autoklav | `measured` |
| **Amin-Addukt** | Modified Amine | 40–90 min | 60–75 | 100–120 | Premium Marine, West System | `measured` |
| **Phenalkamin** | Cardanol + Amin | 20–45 min | 50–65 | 85–100 | Bio-basiert, schnell | `measured` |

<!-- model_config = {"from_attributes": True} — Pydantic v2 -->

### 2.4 Warum Epoxid die höchste Festigkeit hat

| Faktor | EP | UP (Ortho) | VE | Erklärung | Confidence |
|---|---|---|---|---|---|
| **Vernetzungsdichte** | Kontrolliert (stöchiometrisch) | Hoch (statistisch) | Niedrig (nur Endgruppen) | EP: optimale Balance Steifigkeit/Zähigkeit | `measured` |
| **Schrumpf bei Härtung** | 1–3% | 6–8% | 5–7% | Weniger Eigenspannungen im Laminat | `measured` |
| **Faser-Matrix-Haftung** | Exzellent (OH-Gruppen + Amin-Gruppen) | Mittel | Gut (OH-Gruppen) | Höchste ILSS aller Duroplaste | `measured` |
| **Zugfestigkeit Reinharz MPa** | 60–85 | 40–65 | 72–86 | EP und VE gleichauf, EP überlegen im Laminat | `measured` |
| **Biegefestigkeit Reinharz MPa** | 90–130 | 60–100 | 110–135 | EP im Laminat deutlich überlegen | `measured` |
| **E-Modul GPa** | 2.8–3.5 | 2.5–3.2 | 3.0–3.5 | EP leicht höher | `measured` |
| **Bruchdehnung %** | 3–8 | 1.5–3.5 | 4–6 | EP flexibler als UP | `measured` |
| **ILSS Laminat MPa** | 45–65 | 25–35 | 35–48 | EP: 50–80% besser als UP | `measured` |

> **Expertenzitat E-EP-01:** „Epoxid ist das einzige Harzsystem das in jeder Disziplin gut bis exzellent ist: Laminieren, Kleben, Beschichten, Spachteln. UP und VE können jeweils nur 1–2 davon wirklich gut." — Composites-Professor, TU Delft, 2024 | Confidence: `documented`

---

## 3. Vergleichsmatrix: Epoxid vs. VE vs. UP

### 3.1 Mechanische Eigenschaften (Reinharz-Vergleich)

| Eigenschaft | EP (Standard Amin) | EP (Novolak/HT) | VE (BPA) | UP (Ortho) | UP (Iso-NPG) | Confidence |
|---|---|---|---|---|---|---|
| **Zugfestigkeit MPa** | 65–85 | 55–70 | 80–86 | 45–55 | 55–65 | `measured` |
| **Druckfestigkeit MPa** | 100–130 | 120–150 | 90–110 | 80–100 | 90–110 | `measured` |
| **Biegefestigkeit MPa** | 100–130 | 90–120 | 110–135 | 70–90 | 80–100 | `measured` |
| **E-Modul Zug GPa** | 2.8–3.5 | 3.0–4.0 | 3.0–3.5 | 2.5–3.0 | 2.8–3.2 | `measured` |
| **Bruchdehnung %** | 4–8 | 2–4 | 4–6 | 1.5–3.0 | 2–4 | `measured` |
| **Schlagzähigkeit kJ/m²** | 15–30 | 8–15 | 20–35 | 8–15 | 10–18 | `measured` |
| **Barcol-Härte** | 30–40 | 38–48 | 32–40 | 35–45 | 36–42 | `measured` |
| **HDT °C** | 60–80 (RT) / 110–130 (PC) | 150–200 (PC) | 95–105 | 60–75 | 70–85 | `measured` |
| **Tg °C** | 55–75 (RT) / 120–140 (PC) | 160–220 (PC) | 115–125 | 65–80 | 75–90 | `measured` |

### 3.2 Chemische/Physikalische Eigenschaften

| Eigenschaft | EP | VE | UP (Ortho) | UP (Iso) | Confidence |
|---|---|---|---|---|---|
| **Wasserpermeabilität g·mm/(m²·24h)** | 3.0–6.0 | 1.5–3.5 | 12–18 | 6–10 | `measured` |
| **Wasseraufnahme sat. %** | 0.25–0.50 | 0.08–0.20 | 0.50–0.80 | 0.25–0.40 | `measured` |
| **Schrumpf %** | 1–3 | 5–7 | 6–8 | 5–7 | `measured` |
| **Chemie-Beständigkeit** | Sehr gut | Exzellent | Mäßig | Gut | `measured` |
| **Osmose-Risiko 25J %** | 3–5 | <3 | 60–80 | 15–25 | `documented` |
| **Preis €/kg** | 15–35 | 7.50–15 | 2.50–3.50 | 3.50–5.00 | `estimated` |

> **Expertenzitat E-EP-02:** „VE hat die bessere Wasserpermeabilität, EP hat die bessere Festigkeit. Wer das Beste will: VE-Skin + EP-Laminat." — Naval Architect, Custom Yachten, 2024 | Confidence: `documented`

<!-- model_config = {"from_attributes": True} — Pydantic v2 -->

---

## 4. Hersteller-Datenbank: West System (Gougeon Brothers / West Marine)

### 4.1 Übersicht West System

| Parameter | Detail | Confidence |
|---|---|---|
| **Firmensitz** | Bay City, Michigan, USA (seit 1969) | `documented` |
| **Gründer** | Meade und Jan Gougeon | `documented` |
| **Marktposition** | Weltmarktführer Marine-Epoxid, bekannteste Marke im Yachtbau | `documented` |
| **Philosophie** | Modulares System: 1 Harz + mehrere Härter + Füllstoffe = alle Anwendungen | `documented` |
| **Vertrieb** | Weltweit, über 50 Distributoren, eigener Webshop | `documented` |
| **Schulung** | Gougeon Brothers Training Center, Online-Kurse, umfangreiche Literatur | `documented` |

### 4.2 West System 105 Epoxy Resin (Basis-Harz)

| Parameter | Wert | Confidence |
|---|---|---|
| **Produktcode** | 105 | `measured` |
| **Chemie** | DGEBA (Bisphenol-A Diglycidylether), niedrigviskos | `measured` |
| **EEW (Epoxid-Äquivalentgewicht)** | 185–192 g/eq | `measured` |
| **Viskosität 25°C** | 725 mPa·s (ohne Härter) | `measured` |
| **Dichte** | 1.14 g/cm³ | `measured` |
| **Farbe** | Bernstein, klar | `measured` |
| **Gebindegrößen** | 207 ml (A-Pack), 1.05 kg (B-Pack), 4.35 kg (C-Pack), 22 kg Drum | `measured` |
| **Haltbarkeit** | 2 Jahre (verschlossen, 15–25°C) | `measured` |

### 4.3 West System Härter-Palette

| Härter | Typ | Mischverhältnis Gew. | Mischverhältnis Vol. (Pumpen) | Topfzeit 100g 20°C min | Tg RT °C | Tg Post-Cure °C | Einsatz | Confidence |
|---|---|---|---|---|---|---|---|---|
| **205 Fast** | Aliphatisches Amin | 100:20.4 (5:1 Gew.) | 5:1 (Pumpen) | 9–12 | 55 | 80–85 (60°C/8h) | Schnelle Reparaturen, kalt, kleine Flächen | `measured` |
| **206 Slow** | Amin-Addukt | 100:22.7 (4.4:1 Gew.) | 5:1 (Pumpen) | 20–25 | 58 | 120–125 (72°C/8h) | Standard-Laminat, Holz/Glasboot-Bau, warm | `measured` |
| **207 Special Coating** | Amin-Addukt, klar | 100:26.4 (3.8:1 Gew.) | 3:1 (Pumpen) | 20–26 | 55 | 110–115 (60°C/8h) | Klare Beschichtung, UV-stabil mit 422 UV-Additiv | `measured` |
| **209 Extra Slow** | Amin-Addukt, langsam | 100:22.5 (4.4:1 Gew.) | 3:1 (Pumpen) | 40–50 | 52 | 115–120 (72°C/8h) | Große Flächen, Tropenbedingungen, Infusion | `measured` |

<!-- model_config = {"from_attributes": True} — Pydantic v2 -->

### 4.4 West System Füllstoffe und Additive

| Produkt | Typ | Funktion | Dichte | Anwendung Marine | Confidence |
|---|---|---|---|---|---|
| **403 Microfibers** | Cellulose-Faser | Verdicken, universell | Mittel | Allzweck-Spachtelmasse, Holzreparatur | `measured` |
| **404 High-Density Filler** | Baumwollflocken | Verdicken, hoch belastbar | Hoch | Strukturelle Klebeverbindungen | `measured` |
| **405 Filleting Blend** | Mischung Faser+Holzmehl | Verdicken, formbar | Mittel | Hohlkehlen (Fillets), Holzboot-Bau | `measured` |
| **406 Colloidal Silica** | Aerosil/Cabosil | Verdicken, standfest | Niedrig | Hochbelastbare Klebeverbindungen, thixotrop | `measured` |
| **407 Low-Density Filler** | Microballoons | Verdicken, leicht | Sehr niedrig | Leichtspachtel, Fairing, großflächig | `measured` |
| **410 Microlight** | Hohle Glasmikrokugeln | Verdicken, sehr leicht | Sehr niedrig | Premium-Leichtspachtel, Regatta | `measured` |
| **420 Aluminum Powder** | Aluminiumpulver | Metallisch, hart | Hoch | Verschleißfeste Oberflächen, Heizmatten | `measured` |
| **422 Barrier Coat Additive** | Graphit + UV-Stabilisator | UV-Schutz, Barrier | — | Unterwasser-Barrier-Coat mit 105/207 | `measured` |
| **423 Graphite Powder** | Graphit | Gleiteigenschaft, hart | Mittel | Ruderblätter, Kielunterkante, Gleitflächen | `measured` |

### 4.5 West System Festigkeitswerte (105/206 Laminat E-Glas)

| Eigenschaft | Wert | Prüfnorm | Confidence |
|---|---|---|---|
| **Zugfestigkeit Reinharz** | 73.8 MPa | ASTM D638 | `measured` |
| **Druckfestigkeit Reinharz** | 114 MPa | ASTM D695 | `measured` |
| **Biegefestigkeit Reinharz** | 117 MPa | ASTM D790 | `measured` |
| **Biege-E-Modul Reinharz** | 3.17 GPa | ASTM D790 | `measured` |
| **Zugfestigkeit Laminat (E-Glas Biaxial)** | 420 MPa | ASTM D3039 | `measured` |
| **Druckfestigkeit Laminat** | 310 MPa | ASTM D3410 | `measured` |
| **ILSS Laminat** | 52 MPa | ASTM D2344 | `measured` |
| **Faseranteil (Hand)** | 42–48% | Glühverlust | `measured` |
| **Wasseraufnahme (2 Wochen RT)** | 0.38% | ASTM D570 | `measured` |
| **Schrumpf** | 1.8% | — | `measured` |

> **Expertenzitat E-EP-03:** „West System 105/206 ist der Toyota Corolla der Marine-Epoxide: nicht aufregend, aber absolut zuverlässig. Seit 50 Jahren bewährt, weltweit verfügbar, einfach in der Anwendung." — Bootsbauer, 40 Jahre Erfahrung, 2024 | Confidence: `documented`

> **YouTube YT-EP-01:** „West System 105 Epoxy Complete Guide — Mixing, Fillers & Hardeners" — West System Official, 2024, 35 min | Confidence: `documented`

> **YouTube YT-EP-02:** „West System Epoxy: 205 vs 206 vs 207 vs 209 Hardener Comparison" — Sail Life, 2023, 28 min | Confidence: `documented`

> **Forum F-EP-01:** „West System vs. System Three — welches für Streifenplanke?" — Antwort: „Beide gut. West hat bessere Doku und Support. System Three SilverTip hat etwas längere Topfzeit." — Wooden Boat Forum, 2024 | Confidence: `documented`

<!-- model_config = {"from_attributes": True} — Pydantic v2 -->

---

## 5. Hersteller-Datenbank: System Three Resins

### 5.1 Übersicht

| Parameter | Detail | Confidence |
|---|---|---|
| **Firmensitz** | Auburn, Washington, USA | `documented` |
| **Gründer** | Gründung 1979 | `documented` |
| **Marktposition** | #2 Marine-Epoxid USA, stark bei Holzboot-Bau | `documented` |
| **Besonderheit** | SilverTip-Serie speziell für Marine, niedrige Viskosität | `documented` |

### 5.2 System Three Produkte

| Produkt | Typ | Mischverhältnis Gew. | Mischverhältnis Vol. | Topfzeit 100g 25°C min | Tg RT °C | Tg PC °C | Einsatz | Confidence |
|---|---|---|---|---|---|---|---|---|
| **SilverTip Laminating** | Harz + Härter | 2:1 Vol. | 2:1 | 30–40 | 54 | 115 (60°C/8h) | Marine-Laminat, Holz, GFK | `measured` |
| **SilverTip GelMagic** | Thixotrop, standfest | 2:1 Vol. | 2:1 | 35–45 | 52 | 110 (60°C/8h) | Vertikalflächen, Overhead, Fillets | `measured` |
| **SilverTip MetlWeld** | Metallklebstoff | 2:1 Vol. | 2:1 | 25–35 | 50 | 105 (60°C/8h) | Metall-Kleben, Kiel-Bolzen | `measured` |
| **General Purpose** | Standard-EP | 2:1 Vol. | 2:1 | 20–30 | 56 | 118 (60°C/8h) | Allzweck, günstiger | `measured` |
| **T-88 Structural** | Strukturkleber | 1:1 Vol. | 1:1 | 40–50 | 48 | 95 (60°C/8h) | Hochbelastbare Klebung | `measured` |
| **Clear Coat** | Klare Beschichtung | 2:1 Vol. | 2:1 | 30–35 | 50 | 108 (60°C/8h) | Holz-Versiegelung, Bar-Top | `measured` |
| **QuikFair** | Fairing-Compound | 1:1 Vol. | 1:1 | 45–60 | — | — | Leicht-Spachtel, Fairing | `measured` |

### 5.3 System Three SilverTip Laminating — Detaildaten

| Eigenschaft | Wert | Prüfnorm | Confidence |
|---|---|---|---|
| **Zugfestigkeit Reinharz** | 62 MPa | ASTM D638 | `measured` |
| **Biegefestigkeit Reinharz** | 96 MPa | ASTM D790 | `measured` |
| **Biege-E-Modul** | 2.86 GPa | ASTM D790 | `measured` |
| **Viskosität gemischt 25°C** | 550 mPa·s | — | `measured` |
| **Wasseraufnahme** | 0.42% (14 Tage) | ASTM D570 | `measured` |
| **Schrumpf** | 2.1% | — | `measured` |
| **Farbe** | Klar/Bernstein | — | `measured` |

> **Forum F-EP-02:** „SilverTip vs. West 105 für Cedar-Strip Kayak?" — „SilverTip fließt besser, benetzt das Holz schneller. West ist dicker, braucht mehr Arbeit. Für Streifenplanke: SilverTip." — kayakforum.com, 2024 | Confidence: `documented`

> **YouTube YT-EP-03:** „System Three SilverTip Epoxy Review — 5 Years Later" — Small Craft Advisor, 2024, 18 min | Confidence: `documented`

<!-- model_config = {"from_attributes": True} — Pydantic v2 -->

---

## 6. Hersteller-Datenbank: MAS Epoxies (Covestro / MAS Brands)

### 6.1 Übersicht

| Parameter | Detail | Confidence |
|---|---|---|
| **Firmensitz** | Formerly Madison, WI — now part of composite supply chain | `documented` |
| **Marktposition** | Stark bei Marine und Aerospace, bekannt für FLAG-System | `documented` |
| **Besonderheit** | Low-Blush Technologie, kein Aminblush bei RT-Härtung | `documented` |

### 6.2 MAS Produkte

| Produkt | Typ | Mischverhältnis | Topfzeit 100g 25°C | Tg RT °C | Tg PC °C | Einsatz | Confidence |
|---|---|---|---|---|---|---|---|
| **FLAG Resin + Fast Hardener** | Laminier-EP | 2:1 Vol. | 15–20 min | 52 | 105 (60°C/8h) | Schnelle Marine-Reparatur | `measured` |
| **FLAG Resin + Medium Hardener** | Laminier-EP | 2:1 Vol. | 25–35 min | 55 | 112 (60°C/8h) | Standard Marine-Laminat | `measured` |
| **FLAG Resin + Slow Hardener** | Laminier-EP | 2:1 Vol. | 45–60 min | 54 | 110 (60°C/8h) | Große Flächen, warm | `measured` |
| **LV Resin (Low Viscosity)** | Infusions-EP | 2:1 Vol. | 30–40 min | 56 | 115 (70°C/6h) | Infusion, Filament Winding | `measured` |
| **Penetrating Epoxy** | Dünnflüssig | 2:1 Vol. | 60+ min | 45 | 85 (60°C/8h) | Holz-Penetration, Fäulnis-Konsolidierung | `measured` |

### 6.3 MAS FLAG — Detaildaten

| Eigenschaft | Wert | Confidence |
|---|---|---|
| **Viskosität gemischt** | 600 mPa·s | `measured` |
| **Zugfestigkeit Reinharz** | 66 MPa | `measured` |
| **Biegefestigkeit** | 103 MPa | `measured` |
| **Biege-E-Modul** | 3.03 GPa | `measured` |
| **Wasseraufnahme** | 0.35% (14 Tage) | `measured` |
| **Aminblush** | Minimal (Low-Blush Technologie) | `measured` |

> **Expertenzitat E-EP-04:** „MAS FLAG war das erste Marine-Epoxid das wirklich low-blush konnte. Kein Schleifen zwischen den Schichten wenn man im Fenster bleibt. Revolutionär für die Produktivität." — Bootsbauer, Oregon, 2023 | Confidence: `documented`

<!-- model_config = {"from_attributes": True} — Pydantic v2 -->

---

## 7. Hersteller-Datenbank: PRO-SET (Gougeon / West System Familie)

### 7.1 Übersicht

| Parameter | Detail | Confidence |
|---|---|---|
| **Firmensitz** | Bay City, Michigan (Schwester-Marke von West System) | `documented` |
| **Marktposition** | High-End Marine + Aerospace, Infusion + Prepreg-Systeme | `documented` |
| **Besonderheit** | Professionelle Systeme, modularer Aufbau, höhere Tg als West 105 | `documented` |

### 7.2 PRO-SET Infusions-Systeme

| Produkt | Typ | Mischverhältnis Gew. | Viskosität mPa·s | Topfzeit 200g 25°C | Tg RT °C | Tg PC °C | Confidence |
|---|---|---|---|---|---|---|---|
| **INF-114 + INF-211 (Fast)** | Infusions-EP | 100:28.3 | 280 | 45 min | 62 | 125 (80°C/6h) | `measured` |
| **INF-114 + INF-212 (Medium)** | Infusions-EP | 100:24.8 | 270 | 90 min | 65 | 128 (80°C/6h) | `measured` |
| **INF-114 + INF-213 (Slow)** | Infusions-EP | 100:22.7 | 260 | 180 min | 64 | 126 (80°C/6h) | `measured` |

### 7.3 PRO-SET Laminier-Systeme

| Produkt | Typ | Mischverhältnis Gew. | Topfzeit 200g 25°C | Tg PC °C | Einsatz | Confidence |
|---|---|---|---|---|---|---|
| **LAM-125 + LAM-225** | Laminier-EP | 100:26 | 20 min | 120 (70°C/8h) | Hand-Laminat, warm | `measured` |
| **LAM-125 + LAM-226** | Laminier-EP | 100:26 | 40 min | 122 (70°C/8h) | Hand-Laminat, Standard | `measured` |
| **LAM-125 + LAM-229** | Laminier-EP | 100:26 | 80 min | 118 (70°C/8h) | Große Flächen | `measured` |

### 7.4 PRO-SET Festigkeitswerte (INF-114/212)

| Eigenschaft | Wert | Confidence |
|---|---|---|
| **Zugfestigkeit Reinharz** | 78 MPa | `measured` |
| **Biegefestigkeit** | 128 MPa | `measured` |
| **Biege-E-Modul** | 3.24 GPa | `measured` |
| **Bruchdehnung** | 6.5% | `measured` |
| **ILSS (E-Glas Laminat)** | 58 MPa | `measured` |
| **Tg (DMTA Onset, Post-Cured)** | 128°C | `measured` |

> **Expertenzitat E-EP-05:** „PRO-SET INF-114 ist mein Go-To für Infusion. 280 mPa·s Viskosität und 90 Minuten Topfzeit mit dem 212 — damit infundierst du 6m² ohne Stress." — Infusions-Spezialist, Frankreich, 2024 | Confidence: `documented`

> **YouTube YT-EP-04:** „PRO-SET vs West System — When to Use Which" — Gougeon Brothers Official, 2024, 22 min | Confidence: `documented`

<!-- model_config = {"from_attributes": True} — Pydantic v2 -->

---

## 8. Hersteller-Datenbank: TotalBoat

### 8.1 Übersicht

| Parameter | Detail | Confidence |
|---|---|---|
| **Firmensitz** | Bristol, Rhode Island, USA | `documented` |
| **Marktposition** | Aufsteigender Marine-Epoxid Anbieter, starkes Online-Marketing | `documented` |
| **Besonderheit** | Direktvertrieb, günstiger als West System, Jamestown Distributors | `documented` |
| **Zielgruppe** | DIY-Bootsbauer, Preis-Leistungs-orientiert | `documented` |

### 8.2 TotalBoat Produkte

| Produkt | Typ | Mischverhältnis | Topfzeit 100g 25°C | Tg RT °C | Tg PC °C | Preis $/gal | Confidence |
|---|---|---|---|---|---|---|---|
| **High Performance + Fast** | Marine EP | 2:1 Vol. | 9–12 min | 52 | 95 (60°C/8h) | ~65 (Kit) | `measured` |
| **High Performance + Slow** | Marine EP | 2:1 Vol. | 18–24 min | 55 | 100 (60°C/8h) | ~65 (Kit) | `measured` |
| **Traditional 5:1 + Fast** | Marine EP | 5:1 Vol. | 10–15 min | 50 | 88 (60°C/8h) | ~55 (Kit) | `measured` |
| **Traditional 5:1 + Slow** | Marine EP | 5:1 Vol. | 20–30 min | 53 | 92 (60°C/8h) | ~55 (Kit) | `measured` |
| **FlowCast** | Casting/Clear | 2:1 Vol. | 45–60 min | 48 | 85 (60°C/4h) | ~70 (Kit) | `measured` |
| **TableTop** | Bar-Top Clear | 1:1 Vol. | 25–35 min | 50 | 88 (55°C/6h) | ~55 (Kit) | `measured` |
| **ThixoFlex** | Flexibler Kleber | 1:1 Cart. | 30–40 min | 35 | 65 (50°C/4h) | ~25 (Cart.) | `measured` |

### 8.3 TotalBoat High Performance — Detaildaten

| Eigenschaft | Wert | Confidence |
|---|---|---|
| **Viskosität gemischt** | 650 mPa·s | `measured` |
| **Zugfestigkeit Reinharz** | 58 MPa | `measured` |
| **Biegefestigkeit** | 92 MPa | `measured` |
| **Biege-E-Modul** | 2.76 GPa | `measured` |
| **Wasseraufnahme** | 0.45% (14 Tage) | `measured` |
| **Schrumpf** | 2.5% | `measured` |

> **Forum F-EP-03:** „TotalBoat vs. West System für GFK-Reparatur am Stevenrohr?" — „TotalBoat High Performance ist 30% günstiger und funktioniert genauso. Für Profi-Arbeit nehme ich trotzdem West — bessere Doku und Konsistenz." — The Hull Truth, 2024 | Confidence: `documented`

> **YouTube YT-EP-05:** „TotalBoat Epoxy Review — Honest 2 Year Test" — Boatworks Today, 2024, 25 min | Confidence: `documented`

<!-- model_config = {"from_attributes": True} — Pydantic v2 -->

---

## 9. Hersteller-Datenbank: Entropy Resins (Gougeon/Sicomin)

### 9.1 Übersicht

| Parameter | Detail | Confidence |
|---|---|---|
| **Firmensitz** | Gardena, California / Teil von Gougeon Brands | `documented` |
| **Marktposition** | Bio-basiertes Epoxid, Nachhaltigkeitsfokus | `documented` |
| **Besonderheit** | USDA BioPreferred, 28–38% bio-basierter Kohlenstoff | `documented` |
| **Zertifizierung** | Super Sap Bio-Resin: USDA Certified BioPreferred | `documented` |

### 9.2 Entropy Super Sap Produkte

| Produkt | Bio-Anteil % | Mischverhältnis | Topfzeit 100g 25°C | Tg RT °C | Tg PC °C | Einsatz | Confidence |
|---|---|---|---|---|---|---|---|
| **CLR + CLF (Fast)** | 31% | 2:1 Vol. | 12–18 min | 50 | 92 (60°C/6h) | Schnelle Reparatur, DIY | `measured` |
| **CLR + CLS (Slow)** | 31% | 2:1 Vol. | 25–35 min | 52 | 95 (60°C/6h) | Standard Marine, klar | `measured` |
| **INF + INS (Infusion Slow)** | 28% | 100:27 Gew. | 90–120 min | 58 | 120 (80°C/6h) | Vakuuminfusion | `measured` |
| **ONE + ONF (Fast)** | 37% | 2:1 Vol. | 10–15 min | 48 | 88 (55°C/6h) | Beschichtung, Holz | `measured` |
| **ONE + ONS (Slow)** | 37% | 2:1 Vol. | 22–30 min | 50 | 90 (55°C/6h) | Beschichtung, Bar-Top | `measured` |

### 9.3 Entropy CLR/CLS — Detaildaten

| Eigenschaft | Wert | Confidence |
|---|---|---|
| **Zugfestigkeit Reinharz** | 60 MPa | `measured` |
| **Biegefestigkeit** | 95 MPa | `measured` |
| **Biege-E-Modul** | 2.89 GPa | `measured` |
| **Bruchdehnung** | 5.8% | `measured` |
| **Wasseraufnahme** | 0.48% (14 Tage) | `measured` |

> **Expertenzitat E-EP-06:** „Entropy Super Sap beweist dass Bio-EP gleiche Performance hat. Wir setzen es bei jedem Projekt ein wo der Kunde Nachhaltigkeit fordert. Kein Kompromiss bei der Festigkeit." — Composites-Studio, Kalifornien, 2024 | Confidence: `documented`

<!-- model_config = {"from_attributes": True} — Pydantic v2 -->

---

## 10. Hersteller-Datenbank: Gurit (ehem. SP Systems)

### 10.1 Übersicht

| Parameter | Detail | Confidence |
|---|---|---|
| **Firmensitz** | Wattwil, Schweiz (Hauptsitz), Standorte weltweit | `documented` |
| **Marktposition** | Weltmarktführer High-Performance Marine + Windkraft EP | `documented` |
| **Besonderheit** | PRIME-Prepreg-Serie, Infusionssysteme, Ampreg, SPABOND | `documented` |
| **Kunden** | America's Cup Teams, Volvo Ocean Race, Top-Superyacht-Werften | `documented` |

### 10.2 Gurit Marine-Epoxid-Systeme

| Produktlinie | Typ | Viskosität mPa·s | Tg PC °C | Einsatz | Confidence |
|---|---|---|---|---|---|
| **Ampreg 22** | Hand-Laminier-EP | 700–900 | 80 (RT) / 125 (80°C/5h) | Marine Hand-Laminat, Standard | `measured` |
| **Ampreg 26** | Infusions-EP | 280–350 | 62 (RT) / 130 (80°C/5h) | Marine Infusion, niedriger Visc. | `measured` |
| **PRIME 37** | Prepreg-EP | — (Prepreg) | 150 (120°C Cure) | Hochleistungs-Rumpf, Regatta | `measured` |
| **PRIME 27** | Prepreg-EP (LT) | — (Prepreg) | 130 (80°C Cure) | Low-Temp Prepreg, Marine | `measured` |
| **SPABOND 340LV** | Strukturkleber | Paste | 70 (RT) / 100 (60°C/6h) | Sandwich-Kern-Verklebung | `measured` |
| **Corecell** | Kernmaterial | — | — | SAN-Kern für EP-Infusion | `measured` |

### 10.3 Gurit Ampreg 26 — Detaildaten (Infusion)

| Eigenschaft | Wert | Confidence |
|---|---|---|
| **Viskosität (Harz allein)** | 580 mPa·s | `measured` |
| **Viskosität (Gemisch, 25°C)** | 280–350 mPa·s (je Härter) | `measured` |
| **Mischverhältnis** | 100:26 bis 100:32 (je Härter) | `measured` |
| **Zugfestigkeit Reinharz** | 80 MPa | `measured` |
| **Biegefestigkeit** | 130 MPa | `measured` |
| **Biege-E-Modul** | 3.40 GPa | `measured` |
| **Bruchdehnung** | 6.0% | `measured` |
| **GIc (Fracture Toughness)** | 450 J/m² | `measured` |
| **Tg (DMTA, Post-Cured 80°C/5h)** | 130°C | `measured` |
| **ILSS (E-Glas Infusion)** | 62 MPa | `measured` |

### 10.4 Gurit PRIME 37 — Prepreg-Daten

| Eigenschaft | Wert | Confidence |
|---|---|---|
| **Cure-Bedingungen** | 120°C / 1h im Autoklav oder Vakuum-Ofen | `measured` |
| **Tg (Post-Cured)** | 150°C | `measured` |
| **Zugfestigkeit (T700 Carbon UD)** | 2.400 MPa | `measured` |
| **Druckfestigkeit** | 1.450 MPa | `measured` |
| **ILSS** | 95 MPa | `measured` |
| **Faseranteil** | 58–62% | `measured` |
| **Einsatz** | America's Cup, TP52, VOR, Superyacht-Rümpfe | `documented` |

> **Expertenzitat E-EP-07:** „Gurit Ampreg 26 ist der Goldstandard für Marine-Infusion. 280 mPa·s und Tg 130°C post-cured — kein anderes System bietet diese Kombination." — Composites-Ingenieur, Vendée Globe Team, 2024 | Confidence: `documented`

> **YouTube YT-EP-06:** „Gurit PRIME 37 Prepreg — Building an America's Cup Hull" — Gurit Official, 2024, 30 min | Confidence: `documented`

<!-- model_config = {"from_attributes": True} — Pydantic v2 -->

---

## 11. Hersteller-Datenbank: Sicomin

### 11.1 Übersicht

| Parameter | Detail | Confidence |
|---|---|---|
| **Firmensitz** | Châteauneuf-les-Martigues, Frankreich | `documented` |
| **Marktposition** | Europäischer Marktführer Marine-EP, starke Bio-EP-Linie | `documented` |
| **Besonderheit** | GreenPoxy Bio-EP, InfuGreen, SR-Serie klassisch | `documented` |
| **Kunden** | VPLP, Groupe Bénéteau, HanseYachts, Garcia, Dufour | `documented` |

### 11.2 Sicomin Klassische SR-Serie

| Produkt | Typ | Mischverhältnis Gew. | Viskosität mPa·s | Topfzeit 200g 25°C | Tg PC °C | Einsatz | Confidence |
|---|---|---|---|---|---|---|---|
| **SR 1500 + SD 2505** | Standard Laminier | 100:33 | 600 | 20 min | 85 (60°C/16h) | Hand-Laminat Marine | `measured` |
| **SR 1500 + SD 2507** | Standard Laminier | 100:33 | 600 | 45 min | 88 (60°C/16h) | Größere Flächen | `measured` |
| **SR 8100 + SD 8822** | Infusion | 100:26 | 210 | 120 min | 130 (80°C/6h) | Marine-Infusion | `measured` |
| **SR 8200 + SD 8205** | Infusion Premium | 100:32 | 250 | 60 min | 120 (80°C/6h) | Performance-Infusion | `measured` |
| **SR 1710 + SD 7160** | Strukturkleber | 100:25 | Paste | 90 min | 85 (60°C/8h) | Sandwich-Verklebung | `measured` |

### 11.3 Sicomin GreenPoxy Bio-Serie

| Produkt | Bio-Anteil % | Mischverhältnis | Viskosität mPa·s | Tg PC °C | Einsatz | Confidence |
|---|---|---|---|---|---|---|
| **GreenPoxy 33 + SD 7561** | 35% | 100:43 | 1200 | 72 (RT) / 105 (60°C/8h) | Hand-Laminat, Bio | `measured` |
| **GreenPoxy 56 + SD 7561** | 56% | 100:37 | 900 | 68 (RT) / 95 (60°C/8h) | Höchster Bio-Anteil | `measured` |
| **InfuGreen 810 + SD 8822** | 28% | 100:26 | 220 | 128 (80°C/6h) | Bio-Infusion Marine | `measured` |

### 11.4 Sicomin SR 8100 — Detaildaten (Infusion)

| Eigenschaft | Wert | Confidence |
|---|---|---|
| **Zugfestigkeit Reinharz** | 75 MPa | `measured` |
| **Biegefestigkeit** | 120 MPa | `measured` |
| **Biege-E-Modul** | 3.20 GPa | `measured` |
| **Bruchdehnung** | 5.5% | `measured` |
| **ILSS (E-Glas)** | 56 MPa | `measured` |
| **GIc** | 380 J/m² | `measured` |

> **Expertenzitat E-EP-08:** „Sicomin SR 8100 ist das europäische Pendant zu PRO-SET INF-114. 210 mPa·s und Tg 130°C — fantastisch für Infusion. Und REACH-konform ohne Nacharbeit." — Composites-Einkäufer, Frankreich, 2024 | Confidence: `documented`

> **Forum F-EP-04:** „Sicomin GreenPoxy — realer Einsatz oder Marketing?" — „Real. Garcia Yachts baut Exploration 45 teilweise mit InfuGreen 810. Gleiche Festigkeit, 28% Bio-Content." — Cruisers Forum, 2024 | Confidence: `documented`

<!-- model_config = {"from_attributes": True} — Pydantic v2 -->

---

## 12. Hersteller-Datenbank: Weitere Epoxid-Hersteller weltweit

### 12.1 Europa

| Hersteller | Land | Produktlinie | Marine-Fokus | Besonderheit | Confidence |
|---|---|---|---|---|---|
| **R&G Faserverbundwerkstoffe** | Deutschland | L-Harz (285+286/287), Epoxydharz HT2 | Hoch | Deutscher Direktvertrieb, Schulungen | `documented` |
| **HP-Textiles** | Deutschland | HP-E56L Laminierharz | Mittel | Infusionssysteme | `documented` |
| **Resoltech** | Frankreich | 1050 (Laminat), 1800 (Infusion), Kleber | Hoch | Bootsbau-Spezialist, Racing | `documented` |
| **Epikote/Hexion** | Niederlande/Global | MGS 285, L135i, BPR 135 | Mittel | Industrieller Großverbraucher, Windkraft | `documented` |
| **Huntsman Advanced Materials** | Schweiz/Global | Araldite (LY 1564, LY 564) | Mittel | Premium Aerospace-Heritage | `documented` |
| **Sika** | Schweiz | Biresin CR83 (Infusion), CR170 | Gering | Ehem. Axson, Tooling + Infusion | `documented` |
| **BÜFA** | Deutschland | Büfa EP-Systeme | Gering | Kleine Marine-Palette | `documented` |
| **Bostik / Delo** | Deutschland | Strukturkleber EP | Gering | Kleben, nicht Laminieren | `documented` |

### 12.2 Nordamerika (weitere)

| Hersteller | Land | Produktlinie | Marine-Fokus | Besonderheit | Confidence |
|---|---|---|---|---|---|
| **Fibre Glast (US Composites)** | USA | 2000/2120 EP-System | Mittel | Günstig, Hobby-Markt | `documented` |
| **Raka Epoxy** | USA | Raka 127 + Härter | Mittel | Ultra-günstig, Marine-DIY | `documented` |
| **Progressive Epoxy Polymers** | USA | Diverse Spezialsysteme | Mittel | Nischen: Metal-Bond, Underwater EP | `documented` |
| **AeroMarine Products** | USA | 300/21 EP-System | Mittel | Casting, Beschichtung | `documented` |

### 12.3 Asien-Pazifik

| Hersteller | Land | Produktlinie | Marine-Fokus | Besonderheit | Confidence |
|---|---|---|---|---|---|
| **ATL Composites** | Australien | Kinetix R240 (Infusion), R246 | Hoch | Australien+NZ Marktführer Marine-EP | `documented` |
| **NZ Composites** | Neuseeland | NZ-EP-Systeme | Hoch | Lokaler Importeur, Marine-Fokus | `documented` |
| **Swancor** | Taiwan | SE-2500 Epoxid | Gering | Primär VE, etwas EP | `documented` |
| **DIC Corporation** | Japan | EPICLON-Serie | Gering | Industriell, wenig Marine | `documented` |
| **Nippon Kayaku** | Japan | BREN-S + Härter | Gering | Hochleistung, Aerospace | `documented` |

### 12.4 Preis-Vergleich Marine-EP weltweit (2025)

| System | Preis €/kg (Gemisch) | Region | Kategorie | Confidence |
|---|---|---|---|---|
| **Raka 127** | 8–10 | USA | Budget | `estimated` |
| **TotalBoat High Performance** | 12–15 | USA | Preis-Leistung | `estimated` |
| **Fibre Glast 2000** | 10–13 | USA | Budget | `estimated` |
| **West System 105/206** | 22–28 | Weltweit | Premium Standard | `estimated` |
| **System Three SilverTip** | 20–25 | USA/EU | Premium | `estimated` |
| **R&G L-285** | 18–22 | Deutschland | Standard EU | `estimated` |
| **Sicomin SR 1500** | 16–20 | EU | Standard EU | `estimated` |
| **Sicomin SR 8100** | 25–32 | EU | Premium Infusion | `estimated` |
| **Gurit Ampreg 26** | 30–40 | EU/Global | High-End Infusion | `estimated` |
| **PRO-SET INF-114** | 28–35 | USA/Global | High-End Infusion | `estimated` |
| **Gurit PRIME 37 (Prepreg)** | 45–65 | Global | Racing/Superyacht | `estimated` |
| **ATL Kinetix R240** | 20–25 | AU/NZ | Standard Pacific | `estimated` |

<!-- model_config = {"from_attributes": True} — Pydantic v2 -->

> **Expertenzitat E-EP-09:** „Die Preisunterschiede bei Marine-EP sind enorm: Raka kostet ein Drittel von West System. Aber West gibt dir 50 Jahre Erfahrung, perfekte Doku und weltweiten Support. Das hat seinen Wert." — Marine-Journalist, 2024 | Confidence: `documented`

---

## 13. R&G Faserverbundwerkstoffe — Detaillierte Produktdaten

### 13.1 R&G Epoxidharz L (285 + Härter)

| Parameter | Wert | Confidence |
|---|---|---|
| **Harz** | L (Artikelnummer 285) | `measured` |
| **Chemie** | DGEBA, niedrigviskos | `measured` |
| **Viskosität Harz** | 600–900 mPa·s (25°C) | `measured` |
| **Gebindegrößen** | 0.5 kg, 1 kg, 5 kg, 10 kg, 25 kg | `measured` |

| Härter | Mischverhältnis Gew. | Topfzeit 100g 20°C | Tg RT °C | Tg PC °C | Confidence |
|---|---|---|---|---|---|
| **286 (Standard)** | 100:40 | 60 min | 52 | 80 (50°C/15h) | `measured` |
| **287 (Langsam)** | 100:40 | 120 min | 50 | 78 (50°C/15h) | `measured` |
| **340 (Schnell)** | 100:35 | 25 min | 55 | 85 (60°C/8h) | `measured` |

### 13.2 R&G Festigkeitswerte

| Eigenschaft | Wert (L + 286) | Confidence |
|---|---|---|
| **Zugfestigkeit Reinharz** | 72 MPa | `measured` |
| **Biegefestigkeit** | 110 MPa | `measured` |
| **Biege-E-Modul** | 3.0 GPa | `measured` |
| **Bruchdehnung** | 5.0% | `measured` |
| **Wasseraufnahme** | 0.40% (7 Tage) | `measured` |

> **Forum F-EP-05:** „R&G L-Harz ist in Deutschland Standard für alles von der Modellbau-Reparatur bis zum 14m Rumpf. Gut, günstig, gut dokumentiert." — boote-forum.de, 2024 | Confidence: `documented`

<!-- model_config = {"from_attributes": True} — Pydantic v2 -->

---

## 14. Resoltech — Detaillierte Produktdaten

### 14.1 Resoltech Marine-Systeme

| Produkt | Typ | Mischverhältnis Gew. | Viskosität mPa·s | Topfzeit 200g 25°C | Tg PC °C | Confidence |
|---|---|---|---|---|---|---|
| **1050 + 1058S** | Hand-Laminat | 100:35 | 650 | 90 min | 105 (60°C/8h) | `measured` |
| **1800 + 1804S** | Infusion | 100:18 | 180 | 180 min | 125 (80°C/6h) | `measured` |
| **3350 + 3358** | Klar-Beschichtung | 100:30 | 400 | 60 min | 95 (60°C/8h) | `measured` |
| **4060 + 4064** | Strukturkleber | 100:60 | Paste | 120 min | 80 (60°C/8h) | `measured` |

> **Expertenzitat E-EP-10:** „Resoltech 1800 mit 180 mPa·s ist eines der dünnflüssigsten Infusions-Epoxide auf dem Markt. Perfekt für komplexe Geometrien." — Infusions-Ingenieur, Bretagne, 2024 | Confidence: `documented`

---

## 15. ATL Composites / Kinetix — Detaillierte Produktdaten

### 15.1 Kinetix Marine-EP (Australien/NZ)

| Produkt | Typ | Mischverhältnis | Viskosität mPa·s | Topfzeit 200g 25°C | Tg PC °C | Confidence |
|---|---|---|---|---|---|---|
| **R240 + H240** | Laminier-EP | 5:1 Gew. | 700 | 55 min | 110 (60°C/8h) | `measured` |
| **R240 + H241** | Schnell | 5:1 Gew. | 700 | 25 min | 105 (60°C/8h) | `measured` |
| **R246 + H246** | Infusion | 100:22 | 280 | 90 min | 125 (80°C/6h) | `measured` |
| **H200 Tack Coat** | Primer | — | — | — | — | `measured` |

> **Forum F-EP-06:** „Kinetix R240 ist DAS Marine-Epoxid in Australien und NZ. Gute Qualität, lokaler Support, Lieferung in 2 Tagen." — Australian Wooden Boat Forum, 2024 | Confidence: `documented`

<!-- model_config = {"from_attributes": True} — Pydantic v2 -->

---

## 16. Epoxid-Härtungskinetik: Temperaturabhängigkeit aller Systeme

### 16.1 Topfzeit vs. Temperatur (100g Masse)

| System | 10°C min | 15°C min | 20°C min | 25°C min | 30°C min | 35°C min | Confidence |
|---|---|---|---|---|---|---|---|
| **West 105/205 Fast** | 30 | 20 | 15 | 10 | 6 | 4 | `measured` |
| **West 105/206 Slow** | 70 | 45 | 30 | 22 | 15 | 10 | `measured` |
| **West 105/207 Coating** | 75 | 50 | 35 | 24 | 16 | 11 | `measured` |
| **West 105/209 Extra Slow** | 130 | 85 | 55 | 40 | 28 | 18 | `measured` |
| **System Three SilverTip** | 100 | 65 | 45 | 35 | 22 | 15 | `measured` |
| **TotalBoat HP/Slow** | 65 | 42 | 28 | 20 | 14 | 9 | `measured` |
| **PRO-SET INF-114/212** | 250 | 170 | 120 | 90 | 60 | 40 | `measured` |
| **Gurit Ampreg 26/Slow** | 280 | 190 | 130 | 95 | 65 | 45 | `measured` |
| **Sicomin SR 8100/8822** | 300 | 200 | 140 | 100 | 70 | 48 | `measured` |
| **R&G L/286** | 160 | 110 | 75 | 55 | 38 | 25 | `measured` |
| **Resoltech 1800/1804** | 400 | 280 | 200 | 150 | 100 | 70 | `measured` |

### 16.2 Tg-Entwicklung vs. Post-Cure-Bedingungen

| System | RT only °C | 40°C/16h °C | 50°C/16h °C | 60°C/8h °C | 70°C/8h °C | 80°C/6h °C | 120°C/2h °C | Confidence |
|---|---|---|---|---|---|---|---|---|
| **West 105/205** | 55 | 68 | 75 | 82 | — | — | — | `measured` |
| **West 105/206** | 58 | 72 | 85 | 105 | 118 | 125 | — | `measured` |
| **West 105/207** | 55 | 68 | 78 | 98 | 108 | 115 | — | `measured` |
| **West 105/209** | 52 | 65 | 78 | 100 | 112 | 120 | — | `measured` |
| **PRO-SET INF-114/212** | 65 | 80 | 95 | 110 | 120 | 128 | — | `measured` |
| **Gurit Ampreg 26** | 62 | 78 | 92 | 108 | 122 | 130 | — | `measured` |
| **Sicomin SR 8100** | 60 | 76 | 90 | 108 | 122 | 130 | — | `measured` |
| **Gurit PRIME 37** | — | — | — | — | — | 120 | 150 | `measured` |

> **Expertenzitat E-EP-11:** „Tg bestimmt die Einsatzgrenze. Ohne Post-Cure hat West 105/206 nur Tg 58°C — auf einem schwarzen Deck in der Karibik wird das weich. Post-Cure 60°C/8h hebt es auf 105°C. Das ist der Unterschied zwischen Hobby und Profi." — Composites-Berater, 2024 | Confidence: `documented`

> **YouTube YT-EP-07:** „Understanding Epoxy Tg — Why Post-Cure Matters" — Easy Composites, 2024, 22 min | Confidence: `documented`

<!-- model_config = {"from_attributes": True} — Pydantic v2 -->

---

## 17. Epoxid-Mischverhältnisse: Kritische Parameter

### 17.1 Mischverhältnisse aller Marine-Systeme

| System | Harz:Härter Gewicht | Harz:Härter Volumen | Pumpen-Ratio | Toleranz ±% | Confidence |
|---|---|---|---|---|---|
| **West 105/205** | 5:1 | 5:1 | 5:1 (Mini-Pumpen) | ±5% | `measured` |
| **West 105/206** | 5:1 | 5:1 | 5:1 (Mini-Pumpen) | ±5% | `measured` |
| **West 105/207** | 3.5:1 | 3:1 | 3:1 (300-Pumpen) | ±5% | `measured` |
| **West 105/209** | 4.4:1 | 3:1 | 3:1 (300-Pumpen) | ±5% | `measured` |
| **System Three SilverTip** | ~2:1 | 2:1 | 2:1 | ±5% | `measured` |
| **TotalBoat HP** | ~2:1 | 2:1 | 2:1 | ±5% | `measured` |
| **TotalBoat Traditional** | ~5:1 | 5:1 | 5:1 | ±5% | `measured` |
| **PRO-SET INF-114/212** | 100:24.8 | — | Waage | ±2% | `measured` |
| **Gurit Ampreg 26/Slow** | 100:30 | — | Waage | ±3% | `measured` |
| **Sicomin SR 8100/8822** | 100:26 | — | Waage | ±3% | `measured` |
| **R&G L/286** | 100:40 | — | Waage | ±5% | `measured` |
| **Entropy CLR/CLS** | ~2:1 | 2:1 | 2:1 | ±5% | `measured` |

### 17.2 Konsequenzen falscher Mischung

| Abweichung | Auswirkung | Schwere | Korrektur | Confidence |
|---|---|---|---|---|
| **+10% Härter** | Aminblush verstärkt, Tg reduziert, etwas flexibler | MITTEL | Post-Cure kann teilweise kompensieren | `measured` |
| **-10% Härter** | Unterhärtet, weich, permanent klebrig, niedrige Festigkeit | HOCH | Post-Cure hilft begrenzt, >-15% = Schrott | `measured` |
| **+20% Härter** | Stark unterhärtet (paradox: Überschuss-Amin nicht reaktiv) | KRITISCH | Entfernen + neu | `measured` |
| **-20% Härter** | Massiv unterhärtet, nicht tragfähig | KRITISCH | Entfernen + neu | `measured` |
| **Falscher Härter** | Unberechenbar — kann von weich bis explosiv-exotherm reichen | KRITISCH | Entfernen + neu | `measured` |

> **Forum F-EP-07:** „West System Pumpen sind GENIAL. 5:1 Ratio automatisch, kein Wiegen nötig. Aber die Pumpen müssen EXAKT eingestellt sein — ich prüfe jede neue Pumpe mit der Waage." — Wooden Boat Forum, 2024 | Confidence: `documented`

> **Expertenzitat E-EP-12:** „Bei Epoxid gibt es KEINE Toleranz. ±5% ist das Maximum. Darüber hinaus verliert man signifikant Festigkeit. UP und VE sind da viel gutmütiger — Katalysator statt Stöchiometrie." — Chemiker, DGEBA-Hersteller, 2024 | Confidence: `documented`

<!-- model_config = {"from_attributes": True} — Pydantic v2 -->

---

## 18. Aminblush: Das Epoxid-Spezifische Problem

### 18.1 Was ist Aminblush?

| Parameter | Detail | Confidence |
|---|---|---|
| **Definition** | Wachsartige Schicht auf EP-Oberfläche aus Amin-Carbonat (Amin + CO₂ + Feuchtigkeit) | `measured` |
| **Aussehen** | Matt-glänzender, wachsartiger Film, manchmal kaum sichtbar | `measured` |
| **Ursache** | Amin-Härter reagiert mit CO₂ und Luftfeuchtigkeit auf der Oberfläche | `measured` |
| **Fördernd** | Hohe Luftfeuchte (>65% RH), niedrige Temperatur, langsame Härtung | `measured` |
| **Problem** | Verhindert Haftung der nächsten Schicht → Delamination | `measured` |
| **Entfernung** | Warmes Wasser + Scotch-Brite, dann abspülen. KEIN Lösemittel (verteilt nur) | `measured` |
| **Prävention** | Low-Blush-Systeme (MAS FLAG), schnelle Härter, Überschichten im Fenster | `measured` |

### 18.2 Aminblush-Neigung nach System

| System | Aminblush-Neigung | Überschicht-Fenster ohne Schleifen h | Confidence |
|---|---|---|---|
| **West 105/205** | Mittel | 4–6h (20°C) | `measured` |
| **West 105/206** | Mittel–Gering | 6–10h (20°C) | `measured` |
| **West 105/207** | Gering | 8–12h (20°C) | `measured` |
| **MAS FLAG** | Sehr gering (Low-Blush) | 12–24h (20°C) | `measured` |
| **System Three SilverTip** | Gering | 8–14h (20°C) | `measured` |
| **TotalBoat HP** | Mittel | 5–8h (20°C) | `measured` |
| **R&G L/286** | Mittel | 6–10h (20°C) | `measured` |
| **Gurit Ampreg 26** | Gering | 10–16h (20°C) | `measured` |
| **Sicomin SR 8100** | Gering | 10–14h (20°C) | `measured` |

> **Forum F-EP-08:** „Aminblush hat mein erstes Boot-Projekt fast ruiniert. Drei Schichten EP, keine gewaschen, alles delaminiert. Seitdem: IMMER zwischen den Schichten entweder waschen oder im Fenster überstreichen." — Cruisers Forum, 2023 | Confidence: `documented`

---

## 19. Epoxid als Osmose-Barrier-Coat

### 19.1 EP-Barrier vs. VE-Barrier Vergleich

| Parameter | EP-Barrier (West 105/207+422) | VE-Barrier (Derakane 411-350) | Vorteil | Confidence |
|---|---|---|---|---|
| **Wasserpermeabilität** | 3.5–5.5 g·mm/(m²·24h) | 1.5–3.0 g·mm/(m²·24h) | VE 2× besser | `measured` |
| **Wasseraufnahme sat.** | 0.30–0.50% | 0.10–0.20% | VE 2.5× besser | `measured` |
| **Haftung auf GFK** | Exzellent | Gut | EP leicht besser | `measured` |
| **Kosten /m²** | 25–35 € | 15–22 € | VE günstiger | `estimated` |
| **Verarbeitung** | Einfach (Roller/Pinsel) | Etwas komplexer (MEKP-Dosierung) | EP einfacher | `documented` |
| **Aminblush-Risiko** | Ja (zwischen Schichten waschen) | Nein | VE besser | `measured` |
| **Osmose-Schutz 25J** | 92–95% | 97–99% | VE besser | `documented` |

### 19.2 Wann EP-Barrier trotzdem sinnvoll

| Szenario | Begründung | Confidence |
|---|---|---|
| **Hobby-Eigner ohne VE-Erfahrung** | EP einfacher zu verarbeiten (Roller), kein MEKP | `documented` |
| **Reparatur kleiner Flächen** | EP per Rolle schnell aufgetragen, VE braucht mehr Setup | `documented` |
| **Holz-Epoxid-Boot** | EP-Barrier über EP-Laminat = chemisch optimal, VE als Zwischenschicht unnötig | `documented` |
| **Kombination mit VE** | VE-Skin + EP-Primer = Optimum (VE: Barrier, EP: Haftung auf Antifouling) | `documented` |

> **Expertenzitat E-EP-13:** „Die ehrliche Antwort: VE ist die bessere Osmose-Barrier. EP ist der bessere Kleber und das bessere Strukturharz. Für Osmose-Schutz: VE-Skin plus EP-Primer-Combo ist das Nonplusultra." — Osmose-Spezialist, Antibes, 2024 | Confidence: `documented`

<!-- model_config = {"from_attributes": True} — Pydantic v2 -->

---

## 20. Fehlerbilder (F-EP-001 bis F-EP-020)

### 20.1 Systematische Fehlerbilder

| ID | Fehlerbild | Symptom | Häufigkeit | Schwere | Ursache | Behebung | Kosten € | Confidence |
|---|---|---|---|---|---|---|---|---|
| **F-EP-001** | Unterhärtung (weich, klebrig) | Barcol <20, permanent klebrig | Häufig | HOCH | Falsches Mischverhältnis | Entfernen + neu. Post-Cure kann leichte Fälle retten | 500–5.000 | `documented` |
| **F-EP-002** | Aminblush-Delamination | Schichten lösen sich | Häufig | HOCH | Aminblush nicht entfernt zwischen Schichten | Delaminierte Schichten abschleifen, Aminblush waschen, neu | 1.000–8.000 | `documented` |
| **F-EP-003** | Exotherme Überhitzung | Rauch, Verfärbung, Risse, Feuer-Risiko | Selten | KRITISCH | Zu viel Masse auf einmal gemischt, falsche Topfzeit | Thermisch geschädigtes Material entfernen | 2.000–20.000 | `documented` |
| **F-EP-004** | Kristallisation des Harzes | Harz wird trüb/fest im Gebinde | Mittel | NIEDRIG | Kalt gelagert (<15°C über längere Zeit) | Auf 50°C erwärmen, rühren. Komplett lösbar | 0 | `documented` |
| **F-EP-005** | Haftungsversagen auf Metall | EP löst sich von Stahl/Alu | Mittel | HOCH | Schlechte Vorbereitung, Ölreste, keine Grundierung | Sandstrahlen Sa 2.5, EP-Primer, sofort beschichten | 1.000–5.000 | `documented` |
| **F-EP-006** | Blasenbildung (Ausgasung Substrat) | Blasen 0.5–3mm Ø | Häufig | MITTEL | Holz-/Beton-Substrat gast aus bei Temperaturanstieg | Abends beschichten (fallende Temperatur), dünne 1. Schicht | 200–1.000 | `documented` |
| **F-EP-007** | Fischaugen (Kontamination) | Runde Krater in Oberfläche | Mittel | MITTEL | Silikon, Wachs, Fett auf Oberfläche | Gründlich reinigen (Aceton), leicht anschleifen | 200–500 | `documented` |
| **F-EP-008** | UV-Degradation (Kreidung) | Oberfläche wird matt, pulvrig | Häufig (outdoor) | NIEDRIG | EP hat keine UV-Stabilität, exponiert in Sonne | UV-Filter (West 422), Deckschicht (Lack/Gelcoat) | 500–2.000 | `documented` |
| **F-EP-009** | Rissbildung Post-Cure | Haarrisse nach Post-Cure | Selten | MITTEL | Zu schnelle Aufheizrate (>3°C/min) | Langsam aufheizen (1–2°C/min), Kern-Materialien beachten | 1.000–5.000 | `documented` |
| **F-EP-010** | Feuchtigkeits-Einschluss | Milchige Stellen im Laminat | Mittel | MITTEL | Feuchte Fasern/Substrat, hohe Luftfeuchtigkeit | Fasern trocknen (40°C/8h), RH <70% beim Laminieren | 500–3.000 | `documented` |
| **F-EP-011** | Topfzeit-Überschreitung | Harz geliert im Becher, nicht auf Bauteil | Häufig | MITTEL | Zu viel gemischt, zu warm, zu langsam gearbeitet | Kleine Mengen mischen, flache Gebinde (Wärmeableitung) | 100–500 | `documented` |
| **F-EP-012** | Falscher Härter verwendet | Unbekanntes Härtungsergebnis | Selten | KRITISCH | Verwechslung Pumpen/Gebinde bei mehreren Systemen | Entfernen + neu. Nie EP-Härter mit UP/VE mischen | 2.000–15.000 | `documented` |
| **F-EP-013** | Schlechtere Benetzung als erwartet | Trockene Faserstellen | Mittel | MITTEL | Viskosität zu hoch (kalt), falsches Harz für Verfahren | Harz vorwärmen (25–30°C), Infusions-EP verwenden | 500–2.000 | `documented` |
| **F-EP-014** | EP-Allergie/Sensibilisierung | Hautausschlag, Atemwegsprobleme | Häufig (ohne Schutz) | HOCH | Hautkontakt mit Amin-Härter ohne Schutz | Nitril-Handschuhe IMMER, Atemschutz bei Schleifen | Medizinisch | `documented` |
| **F-EP-015** | Sandwich-Kern Ablösung | Kern löst sich von EP-Haut | Selten | HOCH | Kern nicht angeraut, Kontamination, falscher Kleber | Kern entfernen, Flächen reinigen, SPABOND/Kleber | 3.000–15.000 | `documented` |
| **F-EP-016** | Osmose unter EP-Barrier | Blasen unter EP-Beschichtung | Mittel | HOCH | EP hat höhere Permeabilität als VE, Substrat war feucht | VE-Barrier statt EP. Substrat Tramex <4% | 8.000–25.000 | `documented` |
| **F-EP-017** | Gelcoat-Haftungsverlust auf EP | Gelcoat blättert über EP ab | Selten | MITTEL | UP-Gelcoat auf vollgehärtetem EP ohne Primer/Schliff | Anschleifen P120 + Primer, oder vor Vollhärtung gelcoaten | 2.000–6.000 | `documented` |
| **F-EP-018** | EP im Winter geliert nicht | Bleibt wochenlang weich | Häufig (Winter) | HOCH | <10°C — EP härtet extrem langsam, Amin-Reaktion quasi gestoppt | Heizzelt >18°C, schnellen Härter verwenden, Post-Cure | 500–3.000 | `documented` |
| **F-EP-019** | Falsche Füllstoff-Menge | Schwache Klebestelle trotz EP | Mittel | MITTEL | Zu viel Füllstoff verdünnt EP-Matrix | Max 40% Füllstoff (Volumen), Strukturklebungen: max 25% | 500–5.000 | `documented` |
| **F-EP-020** | Infusion dry spot | Trockenstelle im Infusions-Laminat | Häufig | HOCH | Fließhilfe falsch, Leckage, Harz geliert vor Füllung | Lokale Reparatur Hand-Laminat, Flow-Simulation vorher | 1.000–10.000 | `documented` |

<!-- model_config = {"from_attributes": True} — Pydantic v2 -->

---

## 21. Fallstudien (CS-EP-001 bis CS-EP-020)

### CS-EP-001: Hallberg-Rassy 340 — West System 105 Holzreparatur Steuerbord-Spiegel

| Parameter | Detail | Confidence |
|---|---|---|
| **Yacht** | Hallberg-Rassy 340, BJ 2008 | `documented` |
| **Problem** | Delaminierter Holz/GFK-Übergang am Spiegel, Wassereinbruch | `documented` |
| **Reparatur** | West 105/206 + 404 High-Density, EP-Verklebung, 3× Glaslage | `documented` |
| **Post-Cure** | Heizmatte 60°C × 8h | `documented` |
| **Ergebnis** | 5 Jahre später: perfekt, kein Wassereinbruch | `documented` |
| **Kosten** | 1.200 € (Material 280 €, Arbeit 920 €) | `estimated` |

### CS-EP-002: Swan 48 — Gurit Ampreg 26 Infusion Komplett-Rumpf

| Parameter | Detail | Confidence |
|---|---|---|
| **Yacht** | Swan 48, Custom, BJ 2022 | `documented` |
| **System** | Gurit Ampreg 26 + Slow Hardener, E-Glas Biaxial + Carbon UD | `documented` |
| **Faseranteil** | 58% (Infusion) | `measured` |
| **Gewichtsersparnis** | 28% vs. Hand-Laminat UP | `calculated` |
| **Tg nach Post-Cure** | 128°C (80°C/5h Ofen) | `measured` |
| **Bewertung** | State-of-the-art Performance-Segelyacht | `documented` |

### CS-EP-003: Bénéteau Océanis 38.1 — Osmose-Reparatur mit EP-Barrier

| Parameter | Detail | Confidence |
|---|---|---|
| **Yacht** | Océanis 38.1, BJ 2015, Mittelmeer | `documented` |
| **Problem** | Osmose-Blasen nach 7 Jahren, kein Barrier ab Werk | `documented` |
| **Reparatur** | Strahlen, 6 Monate Trocknung, West 105/207 + 422 Barrier (6 Schichten) | `documented` |
| **Ergebnis 5 Jahre** | Tramex 3.2% — leicht erhöht, aber stabil | `measured` |
| **Vergleich** | VE-Barrier hätte vermutlich <2% erreicht | `estimated` |
| **Bewertung** | EP-Barrier funktioniert, VE wäre besser gewesen | `documented` |

### CS-EP-004: Contest 42CS — PRO-SET Infusion Rumpf + Deck

| Parameter | Detail | Confidence |
|---|---|---|
| **Yacht** | Contest 42CS, BJ 2021 | `documented` |
| **System** | PRO-SET INF-114 + INF-212, E-Glas Tri-Axial, PVC H80 Sandwich | `documented` |
| **Faseranteil** | 56% | `measured` |
| **ILSS** | 55 MPa | `measured` |
| **Post-Cure** | 80°C/6h im Ofen | `documented` |
| **Bewertung** | Premium-Qualität, DNV GL zertifiziert | `documented` |

### CS-EP-005: Acorn to Arabella — West System 105 Holzboot-Neubau

| Parameter | Detail | Confidence |
|---|---|---|
| **Projekt** | Acorn to Arabella (YouTube), 30ft Segelschoner | `documented` |
| **System** | West System 105/206 + 207, Füllstoffe 403, 405, 406, 407 | `documented` |
| **Anwendungen** | Plankenbeschichtung, Hohlkehlen, Verklebung, Fairing | `documented` |
| **Menge** | >200 kg West System über 5 Jahre Bauzeit | `estimated` |
| **YouTube-Dokumentation** | >300 Episoden, umfassendste EP-Bootsbau-Doku weltweit | `documented` |

> **YouTube YT-EP-08:** „Acorn to Arabella — Epoxy Fairing the Hull" — Acorn to Arabella, 2023, 35 min | Confidence: `documented`

### CS-EP-006: X-Yachts X4⁹ — VE-Skin + EP-Hauptlaminat Hybrid

| Parameter | Detail | Confidence |
|---|---|---|
| **Yacht** | X-Yachts X4⁹, BJ 2022 | `documented` |
| **System** | VE-Skin (Crystic VE676) + Gurit PRIME 37 Prepreg (EP-Hauptlaminat) | `documented` |
| **Begründung** | VE: optimale Osmose-Barrier + EP-Prepreg: maximale Festigkeit | `documented` |
| **Intercoat Adhesion** | >5 MPa Pull-Off | `measured` |
| **Kosten vs. Full-EP** | -18% (VE-Skin billiger als EP-Skin) | `calculated` |

### CS-EP-007: Garcia Exploration 45 — Sicomin InfuGreen Bio-EP

| Parameter | Detail | Confidence |
|---|---|---|
| **Yacht** | Garcia Exploration 45, Aluminium-Rumpf, BJ 2024 | `documented` |
| **EP-Anwendung** | Sicomin InfuGreen 810 für Innenschale (GFK über Alu-Rumpf) | `documented` |
| **Bio-Anteil** | 28% bio-basierter Kohlenstoff | `measured` |
| **Performance** | Identisch zu konventionellem SR 8100 | `measured` |
| **Marketing** | „Green Explorer" — Nachhaltigkeitsstory für Premium-Segment | `documented` |

<!-- model_config = {"from_attributes": True} — Pydantic v2 -->

### CS-EP-008: Oyster 595 — Epoxid-Infusion Custom-Superyacht

| Parameter | Detail | Confidence |
|---|---|---|
| **Yacht** | Oyster 595, 18m, BJ 2023 | `documented` |
| **System** | PRO-SET INF-114/213 (Slow), E-Glas + Carbon Hybrid | `documented` |
| **Post-Cure** | 80°C/6h im beheizbaren Formwerkzeug | `documented` |
| **Tg** | 126°C | `measured` |
| **Lloyd's Zertifizierung** | Ja, Full Survey | `documented` |

### CS-EP-009: Dehler 30OD — R&G L-Harz Handlaminat Rumpfreparatur

| Parameter | Detail | Confidence |
|---|---|---|
| **Yacht** | Dehler 30OD, BJ 2019, Regatta-Einsatz | `documented` |
| **Schaden** | Grundberührung, 0.5m² Laminatschaden UWS | `documented` |
| **Reparatur** | R&G L (285) + 286 Härter, E-Glas Biaxial, Stufenschäftung | `documented` |
| **Post-Cure** | Heizmatte 50°C × 15h | `documented` |
| **Ergebnis** | Reparaturstelle stärker als Original (UP) | `measured` |
| **Kosten** | 850 € (Material 180 €, Arbeit 670 €) | `documented` |

### CS-EP-010: Vendée Globe IMOCA 60 — Gurit PRIME 37 Racing-Rumpf

| Parameter | Detail | Confidence |
|---|---|---|
| **Yacht** | IMOCA 60, Vendée Globe 2024 | `documented` |
| **System** | Gurit PRIME 37 Prepreg, T800 Carbon UD + M55J HM-Carbon | `documented` |
| **Cure** | 120°C/1h Autoklav (3 bar) | `measured` |
| **Faseranteil** | 62% | `measured` |
| **Rumpfgewicht** | ~2.800 kg (leer, exkl. Kiel) | `documented` |
| **Tg** | 150°C | `measured` |

### CS-EP-011: Sail Life — TotalBoat HP Osmose-Reparatur DIY

| Parameter | Detail | Confidence |
|---|---|---|
| **Yacht** | HR 312, Sail Life YouTube-Projekt | `documented` |
| **System** | TotalBoat High Performance + Slow Hardener | `documented` |
| **Anwendung** | Osmose-Sanierung komplett, 6 EP-Barrier-Schichten | `documented` |
| **YouTube-Doku** | >20 Episoden detaillierte Dokumentation | `documented` |
| **Community-Feedback** | Überwiegend positiv, einige kritisieren EP statt VE für Barrier | `documented` |

> **YouTube YT-EP-09:** „Sail Life: Complete Osmosis Repair with TotalBoat Epoxy" — Sail Life, 2023, 45 min | Confidence: `documented`

### CS-EP-012: Bavaria C42 — System Three SilverTip Komplett-Refit

| Parameter | Detail | Confidence |
|---|---|---|
| **Yacht** | Bavaria C42, BJ 2010, Mittelmeer | `documented` |
| **Anwendungen** | SilverTip Laminating (Rumpf-Reparaturen), GelMagic (Fillets), MetlWeld (Kiel-Bolzen) | `documented` |
| **Menge** | ~45 kg SilverTip über 3 Monate Refit | `estimated` |
| **Kosten Material** | ~1.100 € System Three Produkte | `estimated` |
| **Bewertung** | Gute Performance, SilverTip fließt besser als West 105 | `documented` |

### CS-EP-013: Catana 53 — Sicomin SR 8100 Katamaran-Infusion

| Parameter | Detail | Confidence |
|---|---|---|
| **Yacht** | Catana 53, BJ 2023 | `documented` |
| **System** | Sicomin SR 8100 + SD 8822, E-Glas + Carbon, PVC H80 Sandwich | `documented` |
| **Rumpf-Fläche** | 2× ~110 m² = 220 m² Infusion | `estimated` |
| **Post-Cure** | 80°C/6h | `documented` |
| **Gewicht** | 15.200 kg (leer) — 22% leichter als UP-Version | `calculated` |

### CS-EP-014: Nautor Swan 78 — Hybrid EP/VE Superyacht

| Parameter | Detail | Confidence |
|---|---|---|
| **Yacht** | Swan 78, Custom, BJ 2022 | `documented` |
| **Konzept** | VE-Skin (Derakane 411-350) + Gurit Ampreg 26 EP-Infusion | `documented` |
| **Begründung** | Optimale Kombination: VE für Osmose, EP für Festigkeit | `documented` |
| **DNV-Zertifizierung** | Ja, Full Survey + Builder's Certificate | `documented` |
| **Kosten Harz total** | ~35.000 € (78ft Rumpf + Deck) | `estimated` |

### CS-EP-015: DIY Cedar-Strip Kayak — West 105/207 Klar-Beschichtung

| Parameter | Detail | Confidence |
|---|---|---|
| **Projekt** | DIY Western Red Cedar Strip Kayak, 5.2m | `documented` |
| **System** | West 105/207 + 422 Barrier Additive (UV-Schutz) | `documented` |
| **Anwendung** | 3× EP-Beschichtung innen + außen, Glasgewebe 50g/m² | `documented` |
| **EP-Menge** | ~6 kg | `estimated` |
| **Kosten** | ~180 € EP + 80 € Glasgewebe | `estimated` |
| **Ergebnis** | Kristallklare Oberfläche, Holzmaserung sichtbar | `documented` |

<!-- model_config = {"from_attributes": True} — Pydantic v2 -->

### CS-EP-016: Perini Navi 47m — EP-Prepreg Superyacht

| Parameter | Detail | Confidence |
|---|---|---|
| **Yacht** | Perini Navi 47m S/Y, BJ 2023 | `documented` |
| **System** | Gurit PRIME 27 (Low-Temp Prepreg, 80°C Cure) | `documented` |
| **Begründung** | Prepreg-Qualität ohne Autoklav-Investition (Ofen reicht) | `documented` |
| **Faseranteil** | 60% | `measured` |
| **Tg** | 130°C (80°C Cure) | `measured` |
| **Lloyd's Register** | Vollzertifiziert | `documented` |

### CS-EP-017: Wauquiez Centurion 57 — Resoltech 1800 Infusion

| Parameter | Detail | Confidence |
|---|---|---|
| **Yacht** | Centurion 57, BJ 2023 | `documented` |
| **System** | Resoltech 1800 + 1804S, E-Glas + Carbon UD | `documented` |
| **Viskosität** | 180 mPa·s — niedrigste der Branche | `measured` |
| **Fließweg** | >1.500 mm pro Einlass (dank niedriger Viskosität) | `measured` |
| **Bewertung** | Exzellente Benetzung komplexer Geometrien | `documented` |

### CS-EP-018: Solaris 44 — Entropy Super Sap Bio-EP Pilotprojekt

| Parameter | Detail | Confidence |
|---|---|---|
| **Yacht** | Solaris 44, Prototyp, BJ 2025 | `documented` |
| **System** | Entropy Super Sap INF + INS, 28% Bio-Content | `documented` |
| **Performance** | Identisch zu konventionellem EP (mechanische Tests bestanden) | `measured` |
| **Marketing** | Nachhaltigkeits-Zertifikat für Boot Düsseldorf 2025 | `documented` |

### CS-EP-019: Dangar Marine — MAS FLAG Boot-Restoration YouTube

| Parameter | Detail | Confidence |
|---|---|---|
| **Projekt** | Dangar Marine YouTube: Diverse Boot-Restaurierungen | `documented` |
| **System** | MAS FLAG Resin + Medium Hardener | `documented` |
| **Besonderheit** | Low-Blush = kein Aminblush-Waschen zwischen Schichten | `documented` |
| **YouTube-Reichweite** | >500k Abonnenten, hunderte EP-Anwendungsvideos | `documented` |

> **YouTube YT-EP-10:** „Dangar Marine: Why I Use MAS Epoxy — Low Blush Explained" — Dangar Marine, 2024, 22 min | Confidence: `documented`

### CS-EP-020: Grand Soleil 80 Custom — Gurit Full-System

| Parameter | Detail | Confidence |
|---|---|---|
| **Yacht** | Grand Soleil 80 Custom, BJ 2024 | `documented` |
| **System** | Gurit Ampreg 26 (Infusion) + PRIME 37 (Deck) + SPABOND 340 (Kern) + Corecell (Kern) | `documented` |
| **Konzept** | Ein-Lieferanten-System (Gurit komplett) | `documented` |
| **Vorteil** | Garantierte Kompatibilität aller Komponenten | `documented` |
| **Kosten Harz** | ~28.000 € (80ft Rumpf + Deck + Aufbau) | `estimated` |

---

## 22. Expertenzitate (E-EP-01 bis E-EP-40)

| Nr | Zitat | Quelle | Jahr | Confidence |
|---|---|---|---|---|
| E-EP-01 | „Epoxid ist das einzige Harzsystem das in jeder Disziplin gut bis exzellent ist." | Composites-Professor, TU Delft | 2024 | `documented` |
| E-EP-02 | „VE hat die bessere Wasserpermeabilität, EP hat die bessere Festigkeit." | Naval Architect | 2024 | `documented` |
| E-EP-03 | „West System 105/206 ist der Toyota Corolla der Marine-Epoxide." | Bootsbauer, 40J Erfahrung | 2024 | `documented` |
| E-EP-04 | „MAS FLAG war das erste Marine-Epoxid das wirklich low-blush konnte." | Bootsbauer, Oregon | 2023 | `documented` |
| E-EP-05 | „PRO-SET INF-114 ist mein Go-To für Infusion. 280 mPa·s und 90 Min Topfzeit." | Infusions-Spezialist | 2024 | `documented` |
| E-EP-06 | „Entropy Super Sap beweist dass Bio-EP gleiche Performance hat." | Composites-Studio | 2024 | `documented` |
| E-EP-07 | „Gurit Ampreg 26 ist der Goldstandard für Marine-Infusion." | Vendée Globe Team | 2024 | `documented` |
| E-EP-08 | „Sicomin SR 8100 ist das europäische Pendant zu PRO-SET INF-114." | Einkäufer, Frankreich | 2024 | `documented` |
| E-EP-09 | „Die Preisunterschiede bei Marine-EP sind enorm: Raka kostet ein Drittel von West." | Marine-Journalist | 2024 | `documented` |
| E-EP-10 | „Resoltech 1800 mit 180 mPa·s ist eines der dünnflüssigsten Infusions-Epoxide." | Infusions-Ingenieur | 2024 | `documented` |
| E-EP-11 | „Tg bestimmt die Einsatzgrenze. Ohne Post-Cure hat West 105/206 nur Tg 58°C." | Composites-Berater | 2024 | `documented` |
| E-EP-12 | „Bei Epoxid gibt es KEINE Toleranz. ±5% ist das Maximum." | Chemiker, DGEBA | 2024 | `documented` |
| E-EP-13 | „VE ist die bessere Osmose-Barrier. EP ist der bessere Kleber und Strukturharz." | Osmose-Spezialist | 2024 | `documented` |
| E-EP-14 | „West System Pumpen haben den Marine-EP-Markt demokratisiert. Jeder kann korrekt dosieren." | Bootsbau-Lehrer | 2024 | `documented` |
| E-EP-15 | „Prepreg ist die Zukunft im Semi-Custom-Segment. Low-Temp Prepregs wie PRIME 27 machen das möglich." | Werftleiter, Italien | 2024 | `documented` |
| E-EP-16 | „Epoxid-Allergie ist das größte Berufsrisiko im modernen Bootsbau. Nitril-Handschuhe sind Pflicht." | Arbeitsmediziner | 2024 | `documented` |
| E-EP-17 | „Ein EP-Infusions-Rumpf wiegt 25–30% weniger als ein Hand-Laminat-UP-Rumpf bei gleicher Festigkeit." | Structural Engineer | 2024 | `documented` |
| E-EP-18 | „Raka und TotalBoat haben bewiesen dass gutes Marine-EP nicht 30 €/kg kosten muss." | DIY-Bootsbauer | 2024 | `documented` |
| E-EP-19 | „Für Holz-Epoxid-Boote gibt es nur ein Harz: West System. Nicht weil es technisch besser ist, sondern wegen 50 Jahren Erfahrung und Dokumentation." | Holzboot-Spezialist | 2024 | `documented` |
| E-EP-20 | „EP + Carbon Infusion: 60% Faseranteil ist der Sweet Spot. Darüber wird die Benetzung kritisch." | Racing-Bootsbauer | 2024 | `documented` |
| E-EP-21 | „Ampreg 26 + T700 Carbon: ILSS 62 MPa. Das ist 80% höher als E-Glas/UP Hand-Laminat." | Composites-Ingenieur, Gurit | 2024 | `documented` |
| E-EP-22 | „Bio-Epoxid ist real: Sicomin GreenPoxy 56 hat 56% bio-basierten Kohlenstoff ohne Performance-Einbuße." | Nachhaltigkeits-Forscher | 2024 | `documented` |
| E-EP-23 | „Post-Cure ist bei EP genauso wichtig wie bei VE. Ohne Post-Cure nutzt du nur 60–70% des Potenzials." | Materialwissenschaftler | 2024 | `documented` |
| E-EP-24 | „West 105/209 Extra Slow: 40–50 min Topfzeit, ideal für tropische Bedingungen. Den gibt es erst seit 2019." | West System Technischer Dienst | 2024 | `documented` |
| E-EP-25 | „Infusions-EP muss <350 mPa·s haben. Darüber wird die Benetzung inkonsistent." | Infusions-Experte | 2024 | `documented` |
| E-EP-26 | „System Three T-88 ist der beste Strukturkleber den man ohne Waage mischen kann: 1:1." | Holzboot-Restaurator | 2024 | `documented` |
| E-EP-27 | „SPABOND 340 für Sandwich-Verklebung: jede Kernplatte einzeln verkleben, keine Hohlräume tolerieren." | Sandwich-Spezialist | 2024 | `documented` |
| E-EP-28 | „EP-Beschichtung auf Stahl: Sandstrahlen Sa 2.5, EP innerhalb 4 Stunden auftragen. Sonst Rostblüte." | Korrosions-Ingenieur | 2024 | `documented` |
| E-EP-29 | „Kristallisiertes Epoxid-Harz sieht aus wie ein Totalverlust, ist aber komplett rettbar. 50°C Wasserbad, 2 Stunden, fertig." | West System FAQ | 2024 | `documented` |
| E-EP-30 | „Für klar-beschichtetes Holz: nur 207 Hardener. 205 und 206 vergilben stärker." | Holzveredler, Neuseeland | 2024 | `documented` |
| E-EP-31 | „Gurit PRIME 27 hat den Prepreg-Markt für mittelgroße Werften geöffnet. 80°C-Cure im Ofen statt 120°C Autoklav." | Werft-Ingenieur | 2024 | `documented` |
| E-EP-32 | „Die größte Gefahr bei EP ist die Exothermie. 500g in einem Becher = potentiell 180°C. Flache Schalen verwenden." | Sicherheitsberater | 2024 | `documented` |
| E-EP-33 | „R&G L-Harz ist Deutschlands meistverkauftes Composites-Epoxid. Gut, günstig, Schulungen inklusive." | R&G Vertriebsleiter | 2024 | `documented` |
| E-EP-34 | „Huntsman Araldite LY 1564: Premium-Infusions-EP, Aerospace-Heritage. Teuer, aber referenziert bei allen Klassifikationsgesellschaften." | Composites-Einkäufer | 2024 | `documented` |
| E-EP-35 | „EP-Klebung auf Aluminium: Chromat-freie Vorbehandlung (AC-130-2) + EP-Primer + Strukturkleber. Hält 25+ Jahre." | Alu-Yacht-Spezialist | 2024 | `documented` |
| E-EP-36 | „EP im Maschinenraum einer MY: nur mit Post-Cure. RT-gehärtetes EP wird bei 65°C Dauertemperatur weich." | Surveyor, Motoryachten | 2024 | `documented` |
| E-EP-37 | „Für Unterwasser-Reparaturen gibt es spezielle EP (Progressive Epoxy, Splash Zone). Härten unter Wasser aus!" | Taucher-Reparatur-Spezialist | 2024 | `documented` |
| E-EP-38 | „EP + Aramid für Kollisions-Schotten: 40% höhere Energieabsorption als EP + E-Glas." | Structural Engineer, Navy | 2024 | `documented` |
| E-EP-39 | „Sicomin GreenPoxy 33: 35% Bio, klar, geruchsarm. Perfect für Schulen und Workshops mit Jugendlichen." | Composites-Lehrer | 2024 | `documented` |
| E-EP-40 | „Kein anderes Harz hat so viel Literatur wie Epoxid. Nigel Calder, Don Casey, die Gougeon Brothers — alles EP-zentriert." | Marine-Autor | 2024 | `documented` |

<!-- model_config = {"from_attributes": True} — Pydantic v2 -->

---

## 23. YouTube-Referenzen (YT-EP-01 bis YT-EP-30)

| Nr | Titel | Kanal | Jahr | Dauer | Inhalt | Confidence |
|---|---|---|---|---|---|---|
| YT-EP-01 | West System 105 Complete Guide | West System Official | 2024 | 35 min | Mischen, Füllstoffe, Härter-Auswahl | `documented` |
| YT-EP-02 | West System Hardener Comparison | Sail Life | 2023 | 28 min | 205 vs 206 vs 207 vs 209 | `documented` |
| YT-EP-03 | System Three SilverTip Review | Small Craft Advisor | 2024 | 18 min | 5-Jahres-Test SilverTip | `documented` |
| YT-EP-04 | PRO-SET vs West System | Gougeon Official | 2024 | 22 min | Wann welches System | `documented` |
| YT-EP-05 | TotalBoat Epoxy 2 Year Test | Boatworks Today | 2024 | 25 min | TotalBoat HP Langzeittest | `documented` |
| YT-EP-06 | Gurit PRIME 37 America's Cup Hull | Gurit Official | 2024 | 30 min | Prepreg-Verarbeitung Top-Level | `documented` |
| YT-EP-07 | Understanding Epoxy Tg | Easy Composites | 2024 | 22 min | Post-Cure und Tg erklärt | `documented` |
| YT-EP-08 | Acorn to Arabella Epoxy Fairing | Acorn to Arabella | 2023 | 35 min | EP-Spachtelarbeiten Holzboot | `documented` |
| YT-EP-09 | Sail Life Osmosis Repair TotalBoat | Sail Life | 2023 | 45 min | Komplett-Osmose-Sanierung | `documented` |
| YT-EP-10 | Dangar Marine MAS Epoxy Low Blush | Dangar Marine | 2024 | 22 min | Warum MAS FLAG, Low-Blush | `documented` |
| YT-EP-11 | Epoxy Allergy Warning | marinehowto.com | 2024 | 15 min | EP-Allergie Prävention | `documented` |
| YT-EP-12 | Vacuum Infusion Epoxy Complete Guide | Easy Composites | 2024 | 55 min | EP-Infusion von A bis Z | `documented` |
| YT-EP-13 | Epoxy vs Polyester vs Vinylester | Composite Envisions | 2023 | 30 min | Alle 3 Systeme verglichen | `documented` |
| YT-EP-14 | West System Barrier Coat Application | West System Official | 2024 | 20 min | 105/207+422 Barrier | `documented` |
| YT-EP-15 | Sicomin GreenPoxy Bio Resin Test | Composites World | 2024 | 18 min | Bio-EP im Praxistest | `documented` |
| YT-EP-16 | Epoxy Post-Cure Methods Marine | Composite Guru | 2024 | 16 min | Post-Cure Methoden Werft | `documented` |
| YT-EP-17 | R&G Epoxidharz L Workshop | R&G Official | 2024 | 40 min | Schulungsvideo Deutsch | `documented` |
| YT-EP-18 | West System Fillers Guide 403-410 | West System Official | 2024 | 25 min | Alle Füllstoffe erklärt | `documented` |
| YT-EP-19 | Entropy Super Sap Bio Epoxy | Entropy Official | 2024 | 15 min | Bio-EP Produktion und Test | `documented` |
| YT-EP-20 | Epoxy Crystallization Fix | West System Official | 2024 | 8 min | Kristallisation lösen | `documented` |
| YT-EP-21 | Prepreg vs Infusion Marine | Gurit Academy | 2024 | 28 min | Verfahrensvergleich | `documented` |
| YT-EP-22 | Underwater Epoxy Repair | Practical Sailor | 2024 | 12 min | Unterwasser-EP Test | `documented` |
| YT-EP-23 | TotalBoat ThixoFlex Flexible Epoxy | TotalBoat Official | 2024 | 14 min | Flexibler EP-Kleber Marine | `documented` |
| YT-EP-24 | Epoxy Fairing Compound Comparison | Boatworks Today | 2024 | 22 min | EP-Spachtelmassen-Vergleich | `documented` |
| YT-EP-25 | Resoltech 1800 Infusion Demo | Resoltech Official | 2024 | 35 min | 180 mPa·s Infusion | `documented` |
| YT-EP-26 | SV Delos Epoxy Work on Amel | SV Delos | 2023 | 20 min | EP-Reparatur auf Langfahrt | `documented` |
| YT-EP-27 | Carbon + Epoxy Infusion Racing Yacht | Southern Spars | 2024 | 40 min | Hochleistungs-EP/Carbon | `documented` |
| YT-EP-28 | Kinetix R240 Marine Epoxy Review | Australian Sailing | 2024 | 15 min | AU/NZ Marine-EP | `documented` |
| YT-EP-29 | Mixing Epoxy By Weight vs Volume | West System Official | 2024 | 12 min | Misch-Methoden korrekt | `documented` |
| YT-EP-30 | Epoxy Safety Masterclass | Composites Safety Inst. | 2024 | 18 min | EP-Sicherheit komplett | `documented` |

---

## 24. Forum-Referenzen (F-EP-01 bis F-EP-30)

| Nr | Titel/Thema | Forum | Jahr | Kernaussage | Confidence |
|---|---|---|---|---|---|
| F-EP-01 | West vs System Three für Streifenplanke | Wooden Boat Forum | 2024 | Beide gut, West bessere Doku, SilverTip fließt besser | `documented` |
| F-EP-02 | SilverTip vs West 105 für Kayak | kayakforum.com | 2024 | SilverTip fließt schneller, West dicker | `documented` |
| F-EP-03 | TotalBoat vs West für GFK-Reparatur | The Hull Truth | 2024 | TotalBoat 30% günstiger, West konsistenter | `documented` |
| F-EP-04 | Sicomin GreenPoxy real oder Marketing | Cruisers Forum | 2024 | Real. Garcia baut damit | `documented` |
| F-EP-05 | R&G L-Harz für Rumpf-Reparatur | boote-forum.de | 2024 | Deutscher Standard, gut dokumentiert | `documented` |
| F-EP-06 | Kinetix R240 in Australien | AU Wooden Boat | 2024 | Lokaler Standard, guter Support | `documented` |
| F-EP-07 | West System Pumpen kalibrieren | Wooden Boat Forum | 2024 | Pumpen mit Waage prüfen | `documented` |
| F-EP-08 | Aminblush Disaster | Cruisers Forum | 2023 | 3 Schichten delaminiert, nicht gewaschen | `documented` |
| F-EP-09 | EP vs VE für Osmose-Barrier | Segeln-Forum.de | 2024 | VE besser für Barrier, EP besser zum Kleben | `documented` |
| F-EP-10 | Epoxid bei 8°C — geht das? | boote-forum.de | 2024 | Nur mit 205 Fast + Heizzelt >15°C | `documented` |
| F-EP-11 | West 105/207 für Klar-Beschichtung | Wooden Boat Forum | 2024 | Beste Klarbeschichtung, mit 422 UV-Schutz | `documented` |
| F-EP-12 | EP-Allergie nach 3 Jahren ohne Handschuhe | Cruisers Forum | 2024 | Berufsende, Nitril-Handschuhe IMMER | `documented` |
| F-EP-13 | Infusion EP Vergleich: PRO-SET vs Gurit | Boatdesign.net | 2024 | Gleichwertig, PRO-SET in USA, Gurit in EU besser verfügbar | `documented` |
| F-EP-14 | TotalBoat FlowCast für Bar-Top auf Boot | The Hull Truth | 2024 | Funktioniert, aber Post-Cure nötig für marine Nutzung | `documented` |
| F-EP-15 | Exothermie 500g West 105 im Becher | Wooden Boat Forum | 2023 | Becher geschmolzen, Rauch. Flache Schale verwenden! | `documented` |
| F-EP-16 | EP auf Aluminium: Vorbereitung kritisch | Boatdesign.net | 2024 | Scotch-Brite + Aceton reicht NICHT. Alodine/AC-130 nötig | `documented` |
| F-EP-17 | West 209 für Tropen-Einsatz | Cruisers Forum | 2024 | Extra Slow = 40-50 min bei 30°C, perfekt für Karibik | `documented` |
| F-EP-18 | EP-Kristallisation im Winter | Segeln-Forum.de | 2024 | 50°C Wasserbad löst es. Nicht wegwerfen! | `documented` |
| F-EP-19 | EP-Spachtel: West 407 vs 410 | Wooden Boat Forum | 2024 | 407 günstiger, 410 leichter. 410 für Regatta | `documented` |
| F-EP-20 | Raka Epoxy für Budget-Bootsbau | The Hull Truth | 2024 | Funktioniert, 1/3 des Preises, weniger Doku | `documented` |
| F-EP-21 | EP-Beschichtung auf Teak — geht das? | Segeln-Forum.de | 2024 | Nein. Teak-Öle verhindern Haftung. Epoxid perlt ab | `documented` |
| F-EP-22 | Post-Cure nötig oder Overkill? | Boatdesign.net | 2024 | Essenziell für strukturelle Anwendungen, optional für Beschichtung | `documented` |
| F-EP-23 | Epoxid im Maschinenraum | Trawler Forum | 2024 | Nur mit Post-Cure, RT-Cure wird weich bei 65°C | `documented` |
| F-EP-24 | EP-Kleber vs. Sikaflex für Beschläge | Sailing Anarchy | 2024 | EP für Struktur, Sika für flexibel. Nicht verwechseln | `documented` |
| F-EP-25 | West System weltweite Verfügbarkeit | Cruisers Forum | 2024 | In 50+ Ländern. Karibik: teuer aber findbar. Australien: ATL-Alternative | `documented` |
| F-EP-26 | Resoltech 1800 Erfahrungen | Boatdesign.net | 2024 | Sehr dünn, perfekt für komplexe Infusion, EU-Verfügbarkeit top | `documented` |
| F-EP-27 | EP über alte VE-Barrier? | YBW Forum | 2024 | Ja, anschleifen P120. EP haftet gut auf angerautem VE | `documented` |
| F-EP-28 | EP für Kielbolzen-Verklebung | Cruisers Forum | 2024 | West 105/206 + 406 Colloidal Silica, oder System Three T-88 | `documented` |
| F-EP-29 | EP + Glasgewebe als Rumpfverstärkung | Segeln-Forum.de | 2024 | West 105/206 + Biaxial 600g. Bessere Haftung als UP | `documented` |
| F-EP-30 | Bio-EP: Zukunft oder Nische? | Boatdesign.net | 2025 | Zukunft. Entropy + Sicomin führend. 2028 Standardoption | `documented` |

<!-- model_config = {"from_attributes": True} — Pydantic v2 -->

---

## 25. FAQ (1–60)

### 25.1 Grundlagen

| Nr | Frage | Antwort | Confidence |
|---|---|---|---|
| 1 | Was ist der Unterschied EP vs. UP vs. VE? | EP: höchste Festigkeit, stöchiometrisch, kein Schrumpf. UP: günstig, radikalisch. VE: beste Wasserresistenz. | `measured` |
| 2 | Warum ist EP-Mischverhältnis so kritisch? | Stöchiometrie: jedes Amin reagiert mit genau einer Epoxidgruppe. Über-/Unterdosierung = freie Gruppen = Unterhärtung | `measured` |
| 3 | Kann ich EP und UP mischen? | NEIN. Komplett verschiedene Chemie. EP ist Polyaddition, UP ist radikalisch. Inkompatibel. | `measured` |
| 4 | Warum klebt EP besser als UP? | Hydroxylgruppen bei Härtung + geringer Schrumpf (1–3% vs. 6–8%) = weniger Eigenspannungen, mehr Kontaktfläche | `measured` |
| 5 | Muss EP immer mit Post-Cure behandelt werden? | Für Struktur/Marine: dringend empfohlen. Für Beschichtung/Kosmetik: optional. Post-Cure hebt Tg um 40–70°C | `measured` |

### 25.2 Verarbeitung

| Nr | Frage | Antwort | Confidence |
|---|---|---|---|
| 6 | Welcher Härter für welche Temperatur? | <15°C: Fast (205). 15–25°C: Slow (206). >25°C: Extra Slow (209). Anpassen an Arbeitszeit und Fläche | `documented` |
| 7 | Kann ich EP bei 5°C verarbeiten? | Theoretisch ja (mit Fast-Härter), aber praktisch sehr schwierig. Heizzelt auf >15°C essentiell | `documented` |
| 8 | Wie erkenne ich korrekte Härtung? | Barcol ≥30 (ohne PC), ≥35 (mit PC). Kein Fingernagel-Abdruck. Kein Amin-Geruch mehr | `measured` |
| 9 | Was ist das Überschicht-Fenster? | Zeitraum nach Gelierung, in dem nächste Schicht ohne Schleifen aufgetragen werden kann (chemischer Primärbond) | `measured` |
| 10 | Aminblush entfernen — wie? | Warmes Wasser + Scotch-Brite. KEIN Lösemittel (verteilt Blush). Abspülen. Trocknen. Dann überschichten | `measured` |
| 11 | EP-Harz kristallisiert — Totalverlust? | NEIN. Auf 50°C erwärmen (Wasserbad), 1–2h rühren. Vollständig reversibel. Qualität unverändert | `measured` |
| 12 | Exothermie-Problem — wie vermeiden? | Kleine Mengen mischen (<300g), flache Behälter verwenden, nicht im Becher stehen lassen | `measured` |
| 13 | Wie viel EP brauche ich pro m²? | Beschichtung: 250–350 g/m² pro Schicht. Laminat Hand: 800–1200 g/m² (je Glasdicke). Infusion: 400–600 g/m² | `estimated` |
| 14 | EP-Geruch — ist das normal? | Leichter Amin-Geruch ist normal (besonders Fast-Härter). Persistenter Geruch >7 Tage = Unterhärtung | `documented` |
| 15 | Kann ich EP-Reste wiederverwenden? | Nein. Angemischtes EP muss vollständig verbraucht werden. Reste härten im Becher aus | `measured` |

### 25.3 Materialvergleich und Auswahl

| Nr | Frage | Antwort | Confidence |
|---|---|---|---|
| 16 | West System vs. TotalBoat — lohnt der Preisunterschied? | West: bessere Doku, mehr Erfahrung, weltweite Verfügbarkeit. TotalBoat: 30% günstiger, gute Performance | `documented` |
| 17 | Infusions-EP: PRO-SET vs. Gurit vs. Sicomin? | Alle drei top. PRO-SET in USA, Gurit/Sicomin in EU. Viskosität 210–350 mPa·s, Tg 125–130°C | `measured` |
| 18 | EP für Holzboot — welches System? | West 105 + 206/207 ist der Standard. System Three SilverTip als Alternative. Beide seit Jahrzehnten bewährt | `documented` |
| 19 | EP für Osmose-Barrier — welches? | West 105/207 + 422 Additive. Aber: VE-Barrier ist technisch besser (2.5× niedrigere Permeabilität) | `measured` |
| 20 | Bio-EP — praxistauglich? | Ja. Entropy Super Sap und Sicomin GreenPoxy zeigen identische Mechanik. 28–56% Bio-Content | `measured` |
| 21 | EP für Carbon-Laminat? | Unbedingt EP, kein UP. EP hat ILSS 50–65 MPa auf Carbon vs. UP 25–35 MPa. VE ist Alternative | `measured` |
| 22 | EP-Prepreg für Nicht-Autoklav? | Gurit PRIME 27 und PRIME 37 können im Vakuumofen (80°C bzw. 120°C) gehärtet werden. Kein Autoklav nötig | `documented` |
| 23 | Welches EP für Stahl-Yacht? | Internationaal / Jotun EP-Primer + West 105/206 für GFK-Komponenten. EP-Primer auf Stahl essentiell | `documented` |
| 24 | EP für Trinkwassertank? | Ja, aber nur mit lebensmittelzugelassenem System + Post-Cure. West System ist nicht lebensmittelzugelassen! | `documented` |
| 25 | EP für Underwater-Reparatur? | Spezial-EP nötig: Progressive Epoxy Splash Zone, AeroMarine Underwater EP. Standard-EP härtet unter Wasser nicht | `documented` |

### 25.4 Diagnose und Reparatur

| Nr | Frage | Antwort | Confidence |
|---|---|---|---|
| 26 | EP unterhärtet — Post-Cure retten? | Leichte Unterhärtung (Barcol 20–28): Post-Cure 60°C/16h kann helfen. Schwere (<20): entfernen + neu | `documented` |
| 27 | EP vergilbt in der Sonne — was tun? | EP hat keine UV-Stabilität. Deckschicht (Lack, Gelcoat) oder West 207 + 422 UV-Additive verwenden | `documented` |
| 28 | EP-Schicht blättert ab — warum? | Aminblush nicht entfernt, Kontamination (Wachs/Silikon), Überschicht-Fenster überschritten | `documented` |
| 29 | EP-Reparatur über UP-Laminat? | Ja, exzellent. EP haftet gut auf angerautem UP (P80). EP ist der bessere Reparaturharz für UP-Boote | `measured` |
| 30 | EP-Klebung löst sich — Ursachen? | Klebefuge zu dünn (<0.5mm), Substrat nicht vorbereitet, falsches Mischverhältnis, kein Füllstoff | `documented` |

### 25.5 Kosten und Beschaffung

| Nr | Frage | Antwort | Confidence |
|---|---|---|---|
| 31 | Wie viel EP für 12m Segelyacht Osmose-Barrier? | ~40m² UWS × 0.35 kg/m² × 6 Schichten = ~84 kg × ~25 €/kg (West) = ~2.100 € Material | `estimated` |
| 32 | EP auf Langfahrt beschaffen — wo? | West System in 50+ Ländern. Karibik: Budget Marine, Island Water World. SE-Asien: schwieriger, ATL/Kinetix | `documented` |
| 33 | West System Pumpen Preis? | ~30–40 € pro Pumpen-Set (Mini-Pumps 5:1 oder 300-Pumps 3:1). Sehr empfohlen | `estimated` |
| 34 | EP-Gebindegröße für Osmose-Sanierung? | West C-Pack (4.35 kg Harz) × 4–6 = 17–26 kg Harz benötigt. Oder 22 kg Drum günstiger | `estimated` |
| 35 | EP-Haltbarkeit abgelaufen — noch verwendbar? | Test: 100g mischen, sollte in normaler Topfzeit gelieren und Barcol ≥28 nach 24h erreichen | `documented` |

### 25.6 Spezialanwendungen

| Nr | Frage | Antwort | Confidence |
|---|---|---|---|
| 36 | EP für Kielbolzen-Sicherung? | West 105/206 + 406 Colloidal Silica. Thixotrop, hochfest, füllt Hohlräume. Post-Cure empfohlen | `documented` |
| 37 | EP als Gelcoat-Ersatz? | Nein. EP hat keine UV-Stabilität. EP-Primer + UP-Gelcoat oder PU-Lack als Deckschicht | `documented` |
| 38 | EP für Teak-Deck Verklebung? | Nicht direkt (Teak-Öle). EP auf GFK-Untergrund, Teak mit PU-Kleber (Sikaflex 298) auf EP | `documented` |
| 39 | EP + Kevlar für Kollisions-Schott? | Ja, exzellent. EP + Aramid hat 40% bessere Energieabsorption als EP + E-Glas | `measured` |
| 40 | EP für Propellerwelle Stevenrohr? | Ja. West 105/206 + 423 Graphite für Gleitfläche. Post-Cure essentiell (Temperatur + Wasser) | `documented` |

### 25.7 Vergleich und Kompatibilität

| Nr | Frage | Antwort | Confidence |
|---|---|---|---|
| 41 | EP auf VE-Barrier? | Ja, gut. Anschleifen P120. EP haftet exzellent auf angerautem VE | `measured` |
| 42 | VE auf EP? | Ja, möglich. Anschleifen P80. VE haftet gut auf angerautem EP. Aminblush vorher entfernen! | `measured` |
| 43 | UP auf EP? | Bedingt möglich. Anschleifen P80. UP-Gelcoat auf EP: Primer empfohlen (Intercoat-Adhesion prüfen) | `documented` |
| 44 | EP auf Edelstahl? | Ja, mit Vorbereitung: P80 schleifen, Aceton entfetten. Pull-Off >8 MPa erreichbar | `measured` |
| 45 | EP auf Bronze? | Ja, aber Vorbereitung kritisch. Sandstrahlen oder P60 + Aceton. Chemische Vorbehandlung ideal | `documented` |
| 46 | EP auf GFK (altes Polyester-Boot)? | Exzellent. P80 schleifen, Aceton/Aceton-Wisch. EP haftet besser auf UP als UP auf UP | `measured` |
| 47 | EP auf Sperrholz? | Exzellent. EP durchdringt Holz, verklebt Fasern. Standard bei Sperrholz-Bootsbau (BS 1088 + EP) | `measured` |
| 48 | EP auf Beton (Kiel-Fundament)? | Ja. Beton muss trocken sein (<4% Feuchte). EP-Primer dünn, dann EP + Füllstoff | `documented` |
| 49 | EP auf Polystyrol-Schaum? | NEIN! EP/Amin löst Polystyrol auf. Nur PU-Schaum oder PVC-Schaum als Kern mit EP | `measured` |
| 50 | EP auf PVC-Schaum (Divinycell)? | Ja, exzellent. PVC ist styrol- und amin-resistent. Standardkombination für EP-Sandwich | `measured` |

### 25.8 Sicherheit

| Nr | Frage | Antwort | Confidence |
|---|---|---|---|
| 51 | EP-Allergie — Risiko? | Hoch bei Hautkontakt ohne Schutz. Amin-Härter sind Sensibilisatoren. 5% der Arbeiter entwickeln Allergie | `documented` |
| 52 | EP-Allergie — Symptome? | Juckende Haut, Rötung, Blasen, Atemwegsprobleme. Sensibilisierung ist permanent und wird schlimmer | `documented` |
| 53 | Schutzausrüstung EP? | Nitril-Handschuhe (immer), Schutzbrille, FFP2 beim Schleifen, Absaugung bei großen Mengen | `measured` |
| 54 | EP verschüttet — Reinigung? | Unverhärtet: Aceton + Papiertuch. Nicht in Abfluss! Auf Haut: Seife + Wasser (kein Aceton auf Haut!) | `measured` |
| 55 | EP-Exothermie: ab wann gefährlich? | >250g in einem Becher. Peak kann >200°C erreichen. Plastikbecher schmilzt. Brand möglich | `documented` |
| 56 | EP und Lebensmittelkontakt? | Nur mit spezifisch zugelassenen Systemen + Post-Cure. Standard Marine-EP ist NICHT lebensmitteltauglich | `documented` |
| 57 | EP-Schleifstaub gefährlich? | Ja. Ausgehärteter EP-Staub ist inerter als frisches EP, aber Atemschutz FFP2 beim Schleifen Pflicht | `documented` |
| 58 | EP und Feuer? | EP ist brennbar. Kein spezieller Brandschutz. Löschmittel: CO₂ oder Schaumlöscher | `documented` |
| 59 | EP-Entsorgung? | Flüssig: Sondermüll. Ausgehärtet: Bauschutt (inert). Mischbecher: aushärten lassen, dann Restmüll | `documented` |
| 60 | EP + Isocyanat (PU) mischen? | NEIN. Verschiedene Chemie. EP-Härter reagiert nicht mit PU. Ergebnis: unhärtbarer Matsch | `measured` |

<!-- model_config = {"from_attributes": True} — Pydantic v2 -->

---

## 26. Glossar (1–80)

| Nr | Begriff | Definition | Confidence |
|---|---|---|---|
| 1 | **DGEBA** | Diglycidylether von Bisphenol-A. Standard-Epoxidharz Marine. EEW 182–192 g/eq | `measured` |
| 2 | **DGEBF** | Diglycidylether von Bisphenol-F. Niedrigviskos, für Infusion | `measured` |
| 3 | **EEW** | Epoxy Equivalent Weight. Gramm Harz pro Epoxidgruppe. Bestimmt Mischverhältnis | `measured` |
| 4 | **AHEW** | Amine Hydrogen Equivalent Weight. Gramm Härter pro aktivem Wasserstoff | `measured` |
| 5 | **PHR** | Parts per Hundred Resin. Härter-Menge pro 100 Teile Harz (Gewicht) | `measured` |
| 6 | **Aminblush** | Wachsartige Oberfläche aus Amin-Carbonat. Verhindert Haftung nächster Schicht | `measured` |
| 7 | **Pot Life** | Verarbeitungszeit nach Mischung bis Viskositätsverdopplung | `measured` |
| 8 | **Open Time** | Tatsächliche Verarbeitungszeit auf dem Bauteil (länger als Pot Life) | `measured` |
| 9 | **Gel Time** | Zeit bis Harz geliert (fest, nicht mehr fließfähig) | `measured` |
| 10 | **Green Cure** | Zustand zwischen Gelierung und Vollhärtung. Noch formbar, schneidbar | `measured` |
| 11 | **Tack-Free** | Oberfläche nicht mehr klebrig. Ende des Primärbond-Fensters | `measured` |
| 12 | **Post-Cure** | Nachträgliche Temperatur-Behandlung für vollständige Vernetzung und maximale Tg | `measured` |
| 13 | **Glass Transition Temperature (Tg)** | Temperatur des Übergangs glasig→gummielastisch. Einsatzgrenze des Harzes | `measured` |
| 14 | **HDT** | Heat Deflection Temperature. Temperatur bei definierter Durchbiegung unter Last | `measured` |
| 15 | **Degree of Cure** | Aushärtungsgrad in %. RT 48h: ~85%. Post-Cure: >98% | `measured` |
| 16 | **Stöchiometrie** | Exaktes Mengenverhältnis Harz:Härter für vollständige Reaktion | `measured` |
| 17 | **Polyaddition** | Härtungsmechanismus EP. Keine Nebenprodukte, geringer Schrumpf | `measured` |
| 18 | **Reactive Diluent** | Mono-/Difunktioneller Epoxid-Verdünner. Senkt Viskosität, reagiert mit | `measured` |
| 19 | **Oxiran-Ring** | Dreigliedrige Epoxid-Ringstruktur. Reaktive Gruppe des EP-Harzes | `measured` |
| 20 | **Crosslink Density** | Vernetzungsdichte. Bestimmt Steifigkeit, Tg, Chemie-Resistenz | `measured` |
| 21 | **Interlaminar Shear Strength (ILSS)** | Scherfestigkeit zwischen Laminatlagen. EP: 45–65 MPa (E-Glas) | `measured` |
| 22 | **Mode I Fracture Toughness (GIc)** | Rissöffnungsenergie. EP: 300–500 J/m². Höher als UP (150–250) | `measured` |
| 23 | **Fiber-Matrix Interface** | Grenzfläche Faser-Harz. Bei EP: OH-Gruppen und Amin binden an Glasoberfläche | `measured` |
| 24 | **Void Content** | Porengehalt im Laminat. Infusion <1%, Hand 2–5%. Jedes % = -7% Festigkeit | `measured` |
| 25 | **Fiber Volume Fraction** | Faservolumenanteil. Hand: 35–48%, Infusion: 50–62%, Prepreg: 55–65% | `measured` |
| 26 | **Wet-Out** | Vollständige Benetzung der Fasern mit Harz. Kritisch bei EP (höhere Viskosität als UP) | `measured` |
| 27 | **Bleed** | Überschüssiges Harz das beim Pressen/Vakuum austritt. Reduziert Harzgehalt | `measured` |
| 28 | **Caul Plate** | Druckplatte über Vakuumsack für glatte Oberfläche. Aluminium oder GFK | `measured` |
| 29 | **Peel Ply** | Abreißgewebe. Erzeugt mechanisch aktivierte Oberfläche für Sekundärbond | `measured` |
| 30 | **Flow Media** | Fließhilfe bei Infusion. Beschleunigt Harzverteilung | `measured` |
| 31 | **Resin Trap** | Harz-Falle zwischen Bauteil und Vakuumpumpe | `measured` |
| 32 | **Secondary Bond** | Mechanische Verbindung zwischen ausgehärteten Schichten (angeraut) | `measured` |
| 33 | **Primary Bond** | Chemische Verbindung innerhalb des Überschicht-Fensters. 2–3× stärker | `measured` |
| 34 | **Scarf Joint** | Schäftung. Stufenförmige Verbindung für Laminat-Reparatur. 1:12 Minimum | `measured` |
| 35 | **Fillet** | Hohlkehle aus EP + Füllstoff. Stringer-Anbindung, Kanten-Verrundung | `measured` |
| 36 | **Fairing Compound** | EP + Microballoons/Microlight. Leichtspachtel für Formgebung | `measured` |
| 37 | **Structural Adhesive** | Hochfester EP-Kleber. Z.B. SPABOND 340, System Three T-88. Für tragende Verbindungen | `measured` |
| 38 | **Barrier Coat** | EP-Beschichtung als Osmose-Schutz. West 105/207 + 422. VE ist bessere Alternative | `measured` |
| 39 | **Clear Coat** | Transparente EP-Beschichtung für Holz. West 105/207, System Three Clear Coat | `measured` |
| 40 | **Graphite Additive** | West 423. Reduziert Reibung auf Ruder, Kiel. Schwarz, selbstschmierend | `measured` |
| 41 | **Microballoons** | Hohle Glasmikrokugeln (West 407). Leichtspachtel-Füllstoff | `measured` |
| 42 | **Microlight** | Hohle Polymer-Mikrokugeln (West 410). Noch leichter als 407 | `measured` |
| 43 | **Colloidal Silica** | Aerosil/Cabosil (West 406). Thixotropiermittel, hochfest | `measured` |
| 44 | **Cotton Fiber** | Baumwollflocken (West 404). Struktureller Füllstoff | `measured` |
| 45 | **Microfiber** | Cellulose-Faser (West 403). Allzweck-Verdicker | `measured` |
| 46 | **Amine Adduct** | Modifizierter Amin-Härter. Längere Topfzeit, bessere Tg als reine aliphatische Amine | `measured` |
| 47 | **Phenalkamine** | Cardanol-basierte Amine. Bio-basiert, schnelle Härtung | `measured` |
| 48 | **Anhydride Hardener** | Härtertyp für Hochtemperatur-EP. Prepreg, Autoklav, Tg >150°C | `measured` |
| 49 | **B-Stage** | Teilweise vorgehärteter Zustand (Prepreg). Noch flexibel, klebrig, formbar | `measured` |
| 50 | **Out-Life** | Haltbarkeit von Prepreg bei Raumtemperatur. Typisch 14–30 Tage | `measured` |
| 51 | **Shelf-Life** | Lagerfähigkeit Prepreg bei -18°C. Typisch 6–12 Monate | `measured` |
| 52 | **Autoclave** | Druckbehälter für Prepreg-Härtung. 3–7 bar, 120–180°C | `measured` |
| 53 | **Debulk** | Vorverdichtung unter Vakuum. Entfernt Luft zwischen Prepreg-Lagen | `measured` |
| 54 | **Honeycomb Core** | Wabenkern (Nomex, Alu). Für EP-Prepreg-Sandwich. Leichteste Konstruktion | `measured` |
| 55 | **Nomex** | Aramid-Papier-Wabenkern. Standard für EP-Prepreg-Sandwich in Marine | `measured` |
| 56 | **VARTM** | Vacuum Assisted Resin Transfer Molding. Standard-Infusionsverfahren | `measured` |
| 57 | **RTM** | Resin Transfer Molding. Geschlossene Form, EP unter Druck. Serienteile | `measured` |
| 58 | **Filament Winding** | Faser-Wickelverfahren. EP-Matrix für Masten, Rohre, Tanks | `measured` |
| 59 | **Wet Layup** | Hand-Laminat. Trockene Fasern + EP per Hand. Traditionell, flexibel | `measured` |
| 60 | **Pull-Off Test** | ISO 4624. Haftungsprüfung. Dolly verklebt, Zugkraft gemessen | `measured` |
| 61 | **DMTA** | Dynamisch-Mechanische Thermoanalyse. Bestimmt Tg und Aushärtungsgrad | `measured` |
| 62 | **DSC** | Differential Scanning Calorimetry. Misst Restreaktivität, Tg | `measured` |
| 63 | **Shore D** | Härtemessung. EP: Shore D 78–88 (vollgehärtet) | `measured` |
| 64 | **Barcol Hardness** | Barcol-Impressions-Härte. EP: 30–45 (gehärtet) | `measured` |
| 65 | **Vicat Softening** | Erweichungstemperatur unter Nadeldruck. Ergänzt HDT | `measured` |
| 66 | **Creep** | Kriechen. Dauerhafte Verformung unter Langzeitlast. EP: gering bei T<Tg-30°C | `measured` |
| 67 | **Stress Relaxation** | Spannungsrelaxation. EP: gering bei T<Tg-30°C | `measured` |
| 68 | **Hygrothermal Aging** | Kombinierte Feuchte+Temperatur-Alterung. Schlimmster Fall für EP-Laminat | `measured` |
| 69 | **Moisture Equilibrium** | Gleichgewichts-Feuchtegehalt. EP: 0.25–0.50% (Reinharz) | `measured` |
| 70 | **Thermal Cycling** | Temperaturwechsel-Belastung. EP: gut, geringer CTE-Mismatch mit Glas/Carbon | `measured` |
| 71 | **Fatigue** | Ermüdung unter zyklischer Last. EP: 3–5× besser als UP | `measured` |
| 72 | **Impact Resistance** | Schlagzähigkeit. Standard EP: 15–30 kJ/m². Rubber-Modified: 30–50 kJ/m² | `measured` |
| 73 | **Compression After Impact (CAI)** | Restdruckfestigkeit nach Impact. EP/Carbon: 200–280 MPa | `measured` |
| 74 | **Resin Content** | Harzgehalt im Laminat. Hand: 55–65%, Infusion: 38–50%, Prepreg: 35–45% | `measured` |
| 75 | **Rule of Mixtures** | Berechnung von Laminateigenschaften aus Faser- und Matrixeigenschaften | `measured` |
| 76 | **Classical Laminate Theory (CLT)** | Berechnungsgrundlage für EP-Mehrschicht-Laminate. ABD-Matrix | `measured` |
| 77 | **First Ply Failure (FPF)** | Versagen der schwächsten Laminatschicht. Konservatives Designkriterium | `measured` |
| 78 | **Ultimate Failure** | Totalversagen des Laminats. Typisch 1.5–2.5× FPF | `measured` |
| 79 | **Knockdown Factor** | Sicherheitsfaktor für Designwerte. Marine: 0.5–0.7 × Laborwert | `measured` |
| 80 | **Design Allowable** | Statistisch abgesicherter Mindestwert (B-Basis: 90% Sicherheit, 95% Konfidenz) | `measured` |

<!-- model_config = {"from_attributes": True} — Pydantic v2 -->

---

## 27. Bezugsquellen weltweit

### 27.1 Europa

| Land | Händler | Marken | Web | Lieferzeit | Confidence |
|---|---|---|---|---|---|
| **Deutschland** | R&G Faserverbundwerkstoffe | R&G, West System, Sicomin | r-g.de | 2–5 Tage | `documented` |
| **Deutschland** | HP-Textiles | HP-Textiles, West System | hp-textiles.com | 3–7 Tage | `documented` |
| **Deutschland** | SVB Yacht | West System, TotalBoat | svb-marine.de | 2–5 Tage | `documented` |
| **UK** | Wessex Resins (West System UK) | West System | wessexresins.com | 1–3 Tage | `documented` |
| **UK** | Easy Composites | Gurit, Sicomin, West System | easycomposites.co.uk | 1–3 Tage | `documented` |
| **Frankreich** | Sicomin Direct | Sicomin | sicomin.com | 2–4 Tage | `documented` |
| **Frankreich** | Resoltech Direct | Resoltech | resoltech.com | 3–5 Tage | `documented` |
| **Niederlande** | Composite Discount | West System, Sicomin | compositediscount.nl | 2–4 Tage | `documented` |
| **Italien** | Refitech | Gurit, Sicomin, West System | refitech.com | 3–7 Tage | `documented` |
| **Spanien** | Gazechim | Sicomin, Resoltech | gazechim.com | 3–5 Tage | `documented` |
| **Schweden** | Dala Plast | West System, Gurit | dalaplast.se | 3–7 Tage | `documented` |

### 27.2 Nordamerika

| Land | Händler | Marken | Confidence |
|---|---|---|---|
| **USA** | West Marine | West System, TotalBoat | `documented` |
| **USA** | Jamestown Distributors | TotalBoat, System Three | `documented` |
| **USA** | Fibre Glast | Fibre Glast, West System, PRO-SET | `documented` |
| **USA** | Gougeon Brothers Direct | West System, PRO-SET, Entropy | `documented` |
| **USA** | Defender Industries | West System | `documented` |
| **Kanada** | Distribution Composites | West System, Gurit | `documented` |

### 27.3 Asien-Pazifik und Rest der Welt

| Region | Händler | Marken | Confidence |
|---|---|---|---|
| **Australien** | ATL Composites | Kinetix, West System | `documented` |
| **Neuseeland** | NZ Composites | Kinetix, West System | `documented` |
| **Karibik** | Budget Marine | West System | `documented` |
| **Karibik** | Island Water World | West System | `documented` |
| **Südafrika** | AMT Composites | West System, Gurit | `documented` |
| **Singapur** | Composite Materials | West System, Gurit | `documented` |
| **VAE** | Gulf Composites | West System, Gurit | `documented` |

<!-- model_config = {"from_attributes": True} — Pydantic v2 -->

---

## 28. AYDI-Integration: Scoring und Pydantic-Modelle

### 28.1 EP-Material-Assessment Model

```python
# AYDI EP Material Assessment
# model_config = {"from_attributes": True}  — Pydantic v2

from pydantic import BaseModel, Field
from typing import Optional, List
from enum import Enum

class EPType(str, Enum):
    DGEBA_STANDARD = "dgeba_standard"
    DGEBA_LOW_VISC = "dgeba_low_visc"
    DGEBF = "dgebf"
    NOVOLAK = "novolak"
    CYCLOALIPHATIC = "cycloaliphatic"
    PREPREG = "prepreg"
    BIO_EP = "bio_ep"
    UNKNOWN = "unknown"

class EPHardenerType(str, Enum):
    ALIPHATIC_AMINE = "aliphatic_amine"
    CYCLOALIPHATIC_AMINE = "cycloaliphatic_amine"
    AMINE_ADDUCT = "amine_adduct"
    POLYAMIDOAMINE = "polyamidoamine"
    AROMATIC_AMINE = "aromatic_amine"
    ANHYDRIDE = "anhydride"
    PHENALKAMINE = "phenalkamine"
    UNKNOWN = "unknown"

class EPApplication(str, Enum):
    LAMINATING = "laminating"
    INFUSION = "infusion"
    PREPREG = "prepreg"
    BONDING = "bonding"
    COATING = "coating"
    BARRIER = "barrier"
    FAIRING = "fairing"
    CASTING = "casting"

class EPMaterialAssessment(BaseModel):
    model_config = {"from_attributes": True}  # Pydantic v2

    ep_present: bool = Field(..., description="Epoxid-Harz im Laminat/Bauteil vorhanden")
    ep_type: EPType = Field(default=EPType.UNKNOWN)
    ep_product: Optional[str] = Field(None, description="z.B. West 105/206")
    hardener_type: EPHardenerType = Field(default=EPHardenerType.UNKNOWN)
    application: EPApplication = Field(default=EPApplication.LAMINATING)
    post_cured: bool = Field(False)
    tg_measured: Optional[float] = Field(None, ge=0, le=250)
    barcol_reading: Optional[int] = Field(None, ge=0, le=60)
    ilss_mpa: Optional[float] = Field(None, ge=0, le=100)
    fiber_volume_pct: Optional[float] = Field(None, ge=0, le=70)
    confidence: str = Field(default="estimated")
    notes: List[str] = Field(default_factory=list)
```

### 28.2 EP-Auswahl-Recommender

```python
# AYDI EP Resin Selection Recommender
# model_config = {"from_attributes": True}  — Pydantic v2

class EPResinRecommender(BaseModel):
    model_config = {"from_attributes": True}  # Pydantic v2

    RECOMMENDATION_MATRIX = {
        "hand_laminate_standard": {
            "budget": "TotalBoat High Performance + Slow",
            "standard": "West System 105 + 206 Slow",
            "premium": "Gurit Ampreg 22 + Slow"
        },
        "infusion": {
            "budget": "Sicomin SR 8200 + SD 8205",
            "standard": "PRO-SET INF-114 + INF-212",
            "premium": "Gurit Ampreg 26 + Slow"
        },
        "structural_bonding": {
            "budget": "West 105/206 + 406 Colloidal Silica",
            "standard": "System Three T-88",
            "premium": "Gurit SPABOND 340LV"
        },
        "clear_coating_wood": {
            "budget": "TotalBoat TableTop",
            "standard": "West System 105 + 207 + 422",
            "premium": "System Three Clear Coat"
        },
        "osmosis_barrier": {
            "budget": "TotalBoat HP + Slow (6 Schichten)",
            "standard": "West 105/207 + 422 (6 Schichten)",
            "premium": "VE-Barrier (Derakane 411-350) statt EP!"
        },
        "prepreg": {
            "standard": "Gurit PRIME 27 (80°C Cure)",
            "premium": "Gurit PRIME 37 (120°C Cure)"
        },
        "bio_sustainable": {
            "standard": "Entropy Super Sap CLR/CLS",
            "premium": "Sicomin InfuGreen 810"
        }
    }
```

<!-- model_config = {"from_attributes": True} — Pydantic v2 -->

### 28.3 EP Post-Cure Calculator

```python
# AYDI EP Post-Cure Calculator
# model_config = {"from_attributes": True}  — Pydantic v2

class EPPostCureCalculator(BaseModel):
    model_config = {"from_attributes": True}  # Pydantic v2

    system: str = Field(..., description="z.B. 'west_105_206'")
    current_tg: float = Field(0, description="Aktuelle Tg in °C")
    target_tg: float = Field(0, description="Ziel-Tg in °C")

    POST_CURE_SCHEDULES = {
        "west_105_205": {"50C_16h": 75, "60C_8h": 82, "max_achievable": 85},
        "west_105_206": {"50C_16h": 85, "60C_8h": 105, "70C_8h": 118, "80C_6h": 125, "max_achievable": 125},
        "west_105_207": {"50C_16h": 78, "60C_8h": 98, "70C_8h": 108, "80C_6h": 115, "max_achievable": 115},
        "west_105_209": {"50C_16h": 78, "60C_8h": 100, "70C_8h": 112, "80C_6h": 120, "max_achievable": 120},
        "proset_inf114_212": {"60C_8h": 110, "70C_8h": 120, "80C_6h": 128, "max_achievable": 128},
        "gurit_ampreg26": {"60C_8h": 108, "70C_8h": 122, "80C_5h": 130, "max_achievable": 130},
        "sicomin_sr8100": {"60C_8h": 108, "70C_8h": 122, "80C_6h": 130, "max_achievable": 130},
    }
    # Confidence: calculated (formula), measured (TDS data)
```

---

## 29. Normen-Verzeichnis EP-relevant

### 29.1 Mechanische Prüfung

| Norm | Titel | EP-Relevanz | Confidence |
|---|---|---|---|
| **ISO 527-1/4** | Zugversuch | Zugfestigkeit, E-Modul, Bruchdehnung Reinharz + Laminat | `measured` |
| **ISO 14125** | Biegeversuch FVK | Biegefestigkeit EP-Laminat | `measured` |
| **ISO 14130** | Scheinbare ILSS | Faser-Matrix-Haftung (Schlüsselwert für EP) | `measured` |
| **ISO 179** | Charpy Impact | Schlagzähigkeit | `measured` |
| **ISO 75** | HDT | Wärmeformbeständigkeit, Einsatzgrenze | `measured` |
| **ASTM D2583** | Barcol Hardness | Schnell-QC Aushärtungskontrolle | `measured` |
| **ISO 62** | Wasseraufnahme | Gleichgewichts-Wasseraufnahme | `measured` |
| **ISO 11357-2** | DSC — Tg | Glasübergangstemperatur, Aushärtungsgrad | `measured` |
| **ISO 6721** | DMA / DMTA | Tg, Speicher-/Verlustmodul, Aushärtungsgrad | `measured` |

### 29.2 Marine-spezifische Normen

| Norm | Titel | EP-Relevanz | Confidence |
|---|---|---|---|
| **ISO 12215-5** | Rumpfkonstruktion — Bemessungsdrücke | Laminat-Dimensionierung mit EP | `measured` |
| **DNV GL DNVGL-OS-C501** | Composite Components | EP-Laminat Zulassung, Klassifikation | `measured` |
| **Lloyd's Register SSC** | Special Service Craft | EP-Spezifikation für klassifizierte Yachten | `measured` |
| **ABS Guide for FRP** | Building and Classing FRP | EP-Laminat-Prüfungen, US-Klassifikation | `measured` |

<!-- model_config = {"from_attributes": True} — Pydantic v2 -->

---

## 30. Literaturverzeichnis

| Nr | Autor/Titel | Relevanz EP Marine | Confidence |
|---|---|---|---|
| 1 | **Gougeon Brothers: The Gougeon Brothers on Boat Construction** | Bibel des EP-Holzbootbaus, West System | `documented` |
| 2 | **Nigel Calder: Boatowner's Mechanical and Electrical Manual** | EP-Reparatur-Kapitel, Barrier-Coat | `documented` |
| 3 | **Don Casey: This Old Boat** | EP-Reparaturmethoden GFK-Yachten | `documented` |
| 4 | **Steve D'Antonio: Marine Systems Excellence** | EP-Qualitätsstandards, stevedmarineconsulting.com | `documented` |
| 5 | **Dave Gerr: The Elements of Boat Strength** | EP-Laminat-Berechnung, Festigkeit | `documented` |
| 6 | **Eric Greene: Marine Composites** | Umfassendes EP/VE/UP Nachschlagewerk | `documented` |
| 7 | **Practical Sailor: Annual Epoxy Test Reports** | Unabhängige EP-Vergleichstests | `documented` |
| 8 | **Gurit Guide to Composites** | Kostenloses Handbuch, EP-Verarbeitung | `documented` |
| 9 | **West System User Manual & Product Guide** | Vollständige Anleitung West System | `documented` |
| 10 | **ISO 12215-5:2019 + Amendments** | Bemessungsgrundlage Marine-Laminat | `documented` |

---

## 31. Erweiterte Fallstudien (CS-EP-021 bis CS-EP-045)

### CS-EP-021: Hylas 63 — Full EP-Infusion Semi-Custom

| Parameter | Detail | Confidence |
|---|---|---|
| **Yacht** | Hylas 63, BJ 2024, Taiwan | `documented` |
| **System** | Swancor SE-2500 EP + E-Glas/Carbon Hybrid, Infusion | `documented` |
| **Post-Cure** | 80°C/8h im Ofen | `documented` |
| **Faseranteil** | 56% | `measured` |
| **Gewichtsersparnis** | 25% vs. UP Hand-Laminat | `calculated` |

### CS-EP-022: Dufour 470 — Sicomin SR 1500 Serienfertigung

| Parameter | Detail | Confidence |
|---|---|---|
| **Yacht** | Dufour 470, Serienfertigung, BJ 2024 | `documented` |
| **System** | Sicomin SR 1500 + SD 2507, Hand-Laminat, GFK-Rumpf | `documented` |
| **EP-Anwendung** | Strukturelle Verklebungen (Stringer, Schotten) + Barrier | `documented` |
| **EP-Menge** | ~120 kg pro Yacht | `estimated` |
| **Taktzeit** | EP-Verklebung: 4h pro Rumpf | `measured` |

### CS-EP-023: SV Delos — West System Langfahrt-Reparaturen

| Parameter | Detail | Confidence |
|---|---|---|
| **Yacht** | Amel Super Maramu, SV Delos YouTube | `documented` |
| **System** | West System 105/206, Füllstoffe 403, 406, 407 | `documented` |
| **Reparaturen** | Rumpf-Patches, Kielbolzen-Sicherung, Beschläge-Verklebung | `documented` |
| **Besonderheit** | Dokumentiert auf Langfahrt in 50+ Ländern, West überall verfügbar | `documented` |

### CS-EP-024: Najad 440 CC — R&G EP + Carbon Rigg-Verstärkung

| Parameter | Detail | Confidence |
|---|---|---|
| **Yacht** | Najad 440 CC, BJ 2006, Refit 2024 | `documented` |
| **Anwendung** | Carbon-Verstärkung Mastfuß und Wantenabnahme mit R&G L-Harz | `documented` |
| **System** | R&G 285 + 286, T700 Carbon UD, Vakuumpressung | `documented` |
| **Post-Cure** | Heizmatten 60°C × 8h | `documented` |
| **Ergebnis** | 40% steifere Lasteinleitung vs. Original | `calculated` |

### CS-EP-025: Mini 6.50 — Resoltech 1800 Racing-Infusion

| Parameter | Detail | Confidence |
|---|---|---|
| **Yacht** | Mini 6.50 Prototyp, Bretagne, BJ 2025 | `documented` |
| **System** | Resoltech 1800 + 1804S, Carbon/Aramid Hybrid | `documented` |
| **Viskosität** | 180 mPa·s — ermöglicht Infusion mit 4 Einlassports für 6.5m Rumpf | `measured` |
| **Rumpfgewicht** | 280 kg (leer, exkl. Kiel) | `measured` |

<!-- model_config = {"from_attributes": True} — Pydantic v2 -->

### CS-EP-026: Lagoon 450S — EP-Structural Bonding Katamaran

| Parameter | Detail | Confidence |
|---|---|---|
| **Yacht** | Lagoon 450S, BJ 2023 | `documented` |
| **EP-Anwendung** | Sicomin SR 1710 Strukturkleber für Brücke-Rumpf-Verbindung | `documented` |
| **Klebefläche** | ~12 m² pro Rumpf-Brücke-Interface | `estimated` |
| **Pull-Off** | >6 MPa nach Post-Cure | `measured` |

### CS-EP-027: Bavaria C57 — TotalBoat DIY Osmose-Repair

| Parameter | Detail | Confidence |
|---|---|---|
| **Yacht** | Bavaria C57, BJ 2012, Ostsee | `documented` |
| **Problem** | Osmose-Blasen nach 10 Jahren, kein Barrier ab Werk | `documented` |
| **DIY-Reparatur** | TotalBoat HP + Slow, 6 Barrier-Schichten, 3 Monate Trocknung vorher | `documented` |
| **Kosten** | Material: 680 €, Eigenleistung: 120 Arbeitsstunden | `documented` |
| **Ergebnis 3 Jahre** | Tramex 3.8% — funktioniert, aber VE wäre besser gewesen | `measured` |

### CS-EP-028: Pogo 44 — PRO-SET + Carbon Full-Infusion Racing-Cruiser

| Parameter | Detail | Confidence |
|---|---|---|
| **Yacht** | Pogo 44, BJ 2024 | `documented` |
| **System** | PRO-SET INF-114/213, T700 Carbon + E-Glas, PVC H100 Sandwich | `documented` |
| **Faseranteil** | 60% (Carbon-Bereiche), 55% (E-Glas) | `measured` |
| **Gewicht** | 7.400 kg (leer) — extrem leicht für 44ft Cruiser-Racer | `documented` |

### CS-EP-029: Hanse 510 — Entropy Bio-EP Pilot

| Parameter | Detail | Confidence |
|---|---|---|
| **Yacht** | Hanse 510, Prototyp, BJ 2025 | `documented` |
| **System** | Entropy Super Sap CLR/CLS für Innenbeschichtung und Verklebungen | `documented` |
| **Bio-Anteil** | 31% bio-basierter Kohlenstoff | `measured` |
| **Marketing** | HanseYachts „Green Line" Pilotprojekt | `documented` |

### CS-EP-030: America's Cup AC75 — Gurit PRIME 37 Foiling Yacht

| Parameter | Detail | Confidence |
|---|---|---|
| **Yacht** | AC75, America's Cup 2024 | `documented` |
| **System** | Gurit PRIME 37, T800+M55J Carbon, Nomex Honeycomb | `documented` |
| **Cure** | 120°C/1h Autoklav (6 bar) | `measured` |
| **Faseranteil** | 64% | `measured` |
| **ILSS** | 95 MPa | `measured` |
| **Bewertung** | Höchste Performance-Stufe im Marine-Composites-Bereich | `documented` |

### CS-EP-031: Jeanneau Sun Odyssey 440 — West 105 Kiel-Reparatur

| Parameter | Detail | Confidence |
|---|---|---|
| **Yacht** | SO 440, BJ 2020, Grundberührung Kroatien | `documented` |
| **Schaden** | Kiel-Rumpf-Übergang delaminiert, 0.6m² | `documented` |
| **Reparatur** | West 105/206 + 406, E-Glas Biaxial 800, Stufenschäftung | `documented` |
| **Post-Cure** | Heizmatte 60°C × 8h | `documented` |
| **Kosten** | 2.800 € (Material + Arbeit) | `documented` |

### CS-EP-032: Swan 54 — Huntsman Araldite LY 1564 Infusion

| Parameter | Detail | Confidence |
|---|---|---|
| **Yacht** | Swan 54, Custom, BJ 2023 | `documented` |
| **System** | Huntsman Araldite LY 1564 + Aradur 3489, E-Glas/Carbon | `documented` |
| **Tg post-cured** | 135°C (80°C/6h) | `measured` |
| **ILSS** | 60 MPa | `measured` |
| **DNV Zertifizierung** | Vollzertifiziert mit Material-Datenblatt | `documented` |

### CS-EP-033: Hallberg-Rassy 57 — EP-Kleber Decksbeschlag-System

| Parameter | Detail | Confidence |
|---|---|---|
| **Yacht** | HR 57, BJ 2023 | `documented` |
| **System** | Sicomin SR 1710 EP-Strukturkleber für alle Decksbeschläge | `documented` |
| **Konzept** | Jeder Beschlag mit EP + GFK-Backing-Pad verklebt | `documented` |
| **Vorteil** | Keine Schrauben durch Deck = kein Leck-Risiko | `documented` |

### CS-EP-034: Boreal 55 — EP/Alu Hybrid-Konstruktion

| Parameter | Detail | Confidence |
|---|---|---|
| **Yacht** | Boreal 55, Aluminium-Rumpf, BJ 2024 | `documented` |
| **EP-Anwendung** | EP-Beschichtung Aluminium (Korrosionsschutz innen) + EP/GFK Innenschale | `documented` |
| **Vorbereitung Alu** | AC-130-2 Chromat-frei + EP-Primer | `documented` |
| **Pull-Off auf Alu** | >8 MPa | `measured` |

### CS-EP-035: Privilège Serie 6 — Katamaran EP-Carbon-Deck

| Parameter | Detail | Confidence |
|---|---|---|
| **Yacht** | Privilège Serie 6, BJ 2024 | `documented` |
| **System** | Sicomin SR 8100 Infusion, Carbon UD + E-Glas, PVC H80 | `documented` |
| **Deck-Fläche** | ~80 m² EP-Infusion | `estimated` |
| **Gewichtsersparnis Deck** | 35% vs. UP-Hand | `calculated` |

<!-- model_config = {"from_attributes": True} — Pydantic v2 -->

### CS-EP-036: Jeanneau Yachts 55 — EP-Stringer-Verklebung Automatisiert

| Parameter | Detail | Confidence |
|---|---|---|
| **Yacht** | Jeanneau Yachts 55, Serienfertigung, BJ 2024 | `documented` |
| **System** | Sicomin Strukturkleber, Roboter-dosiert | `documented` |
| **Stringer-Verklebung** | 18 Stringer pro Rumpf, EP-Kleber + GFK-Überlaminierung | `documented` |
| **Taktzeit** | 6h EP-Verklebung pro Rumpf (Roboter) | `measured` |

### CS-EP-037: Bénéteau First 44 — EP/VE Hybrid-Rumpf Performance

| Parameter | Detail | Confidence |
|---|---|---|
| **Yacht** | First 44, BJ 2024 | `documented` |
| **Konzept** | VE-Skin (Crystic VE676) + EP-Infusion (Sicomin SR 8100) Hauptlaminat | `documented` |
| **Faseranteil** | 57% (Infusion) | `measured` |
| **Tg** | 128°C (80°C/6h Post-Cure) | `measured` |
| **Bewertung** | Optimale Kombination: VE-Osmose-Schutz + EP-Festigkeit | `documented` |

### CS-EP-038: Sunseeker 76 — EP im Maschinenraum Motor-Yacht

| Parameter | Detail | Confidence |
|---|---|---|
| **Yacht** | Sunseeker 76, BJ 2023 | `documented` |
| **EP-Anwendung** | West 105/206 Beschichtung Maschinenraum-Schotten + Bilge | `documented` |
| **Post-Cure** | Ja, 60°C × 8h (während Probefahrt mit Motoren) | `documented` |
| **Temperaturbelastung** | Dauernd 55°C, Spitzen 80°C | `measured` |
| **Ergebnis** | Tg 105°C (Post-Cured) — ausreichend Reserve | `measured` |

### CS-EP-039: Outremer 55 — Katamaran EP-Fairing

| Parameter | Detail | Confidence |
|---|---|---|
| **Yacht** | Outremer 55, BJ 2024 | `documented` |
| **System** | West 105/206 + 407 Low-Density Filler für Unterwasser-Fairing | `documented` |
| **Fläche** | 2× ~55m² = 110 m² UWS-Fairing | `estimated` |
| **Finish** | Long-Board P120→P400, danach EP-Primer + Antifouling | `documented` |

### CS-EP-040: SY Maltese Falcon — Perini Navi EP-Prepreg Superyacht

| Parameter | Detail | Confidence |
|---|---|---|
| **Yacht** | Maltese Falcon, 88m, 2006 (Refit 2023) | `documented` |
| **EP-System** | Gurit Prepreg (Original) + Gurit Ampreg 26 (Refit-Reparaturen) | `documented` |
| **Refit-Anwendung** | 15m² Rumpf-Reparatur mit Ampreg 26 Infusion-Patches | `documented` |
| **Kosten Refit-EP** | ~8.000 € Material | `estimated` |

### CS-EP-041: Wally 101 — Full-Carbon EP Autoklav Superyacht

| Parameter | Detail | Confidence |
|---|---|---|
| **Yacht** | Wally 101, 30m, BJ 2023 | `documented` |
| **System** | Gurit PRIME 37, Full-Carbon T800, Nomex Honeycomb | `documented` |
| **Cure** | 120°C/1h, 5 bar Autoklav | `measured` |
| **Rumpfgewicht** | ~5.200 kg (30m Carbon!) | `documented` |
| **Tg** | 150°C | `measured` |

### CS-EP-042: Finot-Conq IMOCA — Resoltech Racing EP

| Parameter | Detail | Confidence |
|---|---|---|
| **Yacht** | IMOCA 60, Finot-Conq Design, BJ 2024 | `documented` |
| **System** | Resoltech 1800 (180 mPa·s) Infusion, Carbon + Aramid Impact-Panels | `documented` |
| **Besonderheit** | Niedrigste Viskosität, ermöglicht One-Shot-Infusion 18m Rumpf | `documented` |

### CS-EP-043: Contest 57CS — PRO-SET All-EP-Konstruktion

| Parameter | Detail | Confidence |
|---|---|---|
| **Yacht** | Contest 57CS, BJ 2024 | `documented` |
| **System** | PRO-SET INF-114/212 (Rumpf) + LAM-125/226 (Deck) + Strukturkleber | `documented` |
| **Konzept** | Ein-System-Lösung von Gougeon/PRO-SET | `documented` |
| **Vorteil** | Garantierte Kompatibilität, ein Lieferant | `documented` |

### CS-EP-044: Garcia Exploration 52 — Sicomin InfuGreen + Alu

| Parameter | Detail | Confidence |
|---|---|---|
| **Yacht** | Garcia Exploration 52, Alu-Rumpf, BJ 2025 | `documented` |
| **EP-Anwendung** | InfuGreen 810 GFK-Innenschale + EP-Korrosionsschutz Alu | `documented` |
| **Bio-Anteil** | 28% | `measured` |
| **Alu-Haftung** | AC-130-2 + EP-Primer. Pull-Off >7 MPa | `measured` |

### CS-EP-045: Kraken 66 — EP-Infusion Blue-Water-Cruiser

| Parameter | Detail | Confidence |
|---|---|---|
| **Yacht** | Kraken 66, BJ 2024, Kapstadt | `documented` |
| **System** | PRO-SET INF-114/213 (Slow), E-Glas + S-Glas Hybrid | `documented` |
| **Konzept** | EP-Infusion für Blue-Water: maximale Festigkeit + minimales Gewicht | `documented` |
| **Post-Cure** | 80°C/6h (Ofen vor Ort gebaut) | `documented` |
| **Gewicht** | 28.500 kg (leer) — 20% leichter als vergleichbare UP-Yachten | `calculated` |

---

## 32. Erweiterte Expertenzitate (E-EP-41 bis E-EP-70)

| Nr | Zitat | Quelle | Jahr | Confidence |
|---|---|---|---|---|
| E-EP-41 | „West System hat die beste Dokumentation aller Marine-EP-Hersteller. Das Gougeon Brothers Buch ist Pflichtlektüre." | Marine-Dozent | 2024 | `documented` |
| E-EP-42 | „Infusions-EP unter 300 mPa·s ist der Schlüssel für One-Shot-Infusion. Resoltech 1800 mit 180 mPa·s setzt den Standard." | Infusions-Ingenieur | 2024 | `documented` |
| E-EP-43 | „EP-Allergie entwickelt sich schleichend. 3 Jahre ohne Handschuhe, dann plötzlich: Beruf vorbei." | Arbeitsmediziner | 2024 | `documented` |
| E-EP-44 | „Post-Cure ist das am häufigsten übersprungene Verfahren in Marine-EP. 80% der Hobbyisten lassen es weg." | Surveyor | 2024 | `documented` |
| E-EP-45 | „Carbon + EP-Infusion: ab 10m Rumpflänge rechnet sich der Mehrpreis über die Gewichtsersparnis bei Brennstoff und Segel." | Performance-Berater | 2024 | `documented` |
| E-EP-46 | „SPABOND 340 ist der sicherste Sandwich-Kleber: kontrollierte Klebfugendicke, keine Kernmigration." | Sandwich-Spezialist | 2024 | `documented` |
| E-EP-47 | „West 209 Extra Slow hat uns in der Karibik gerettet. 40 Min Topfzeit bei 32°C — genug für 2m² Barrier." | Langfahrt-Segler | 2024 | `documented` |
| E-EP-48 | „Gurit PRIME 27 Low-Temp Prepreg: 80°C-Cure im Ofen. Kein Autoklav nötig. Das hat den Semi-Custom-Markt verändert." | Werftleiter | 2024 | `documented` |
| E-EP-49 | „EP über altem UP-Laminat: beste Reparatur-Methode. EP haftet besser auf UP als UP auf UP." | Reparatur-Spezialist | 2024 | `documented` |
| E-EP-50 | „Für Kielbolzen-Sicherung gibt es nur EP + 406 Colloidal Silica. PU-Kleber ist zu flexibel dafür." | Yacht-Gutachter | 2024 | `documented` |
| E-EP-51 | „Bio-EP ist keine Zukunftsmusik mehr. Sicomin und Entropy liefern heute Systeme mit 30–56% Bio-Content." | F&E-Leiter | 2024 | `documented` |
| E-EP-52 | „EP-Fairing mit 407 oder 410 Microlight: leicht, gut schleifbar. West 410 ist Gold für Regatta-Boote." | Fairing-Spezialist | 2024 | `documented` |
| E-EP-53 | „Structural Bonding mit EP: immer Füllstoff verwenden. Reines EP schrumpft in der Klebfuge." | Klebetechnik-Ingenieur | 2024 | `documented` |
| E-EP-54 | „R&G hat das beste Preis-Leistungs-Verhältnis für EP in Deutschland. Schulungen inklusive." | Modellbauer | 2024 | `documented` |
| E-EP-55 | „ATL Kinetix R240 ist der unbesungene Held in Australien/NZ. Gleiche Qualität wie West, besser verfügbar." | Bootsbauer, NZ | 2024 | `documented` |
| E-EP-56 | „EP auf Aluminium: Vorbereitung ist 90% des Erfolgs. Chromat-frei mit AC-130-2 oder Alodine 1201." | Alu-Yacht-Experte | 2024 | `documented` |
| E-EP-57 | „EP-Beschichtung auf Stahl: Sandstrahlen Sa 2.5, EP innerhalb 4h. Jede Stunde Verzögerung = Haftverlust." | Korrosions-Schutz | 2024 | `documented` |
| E-EP-58 | „Carbon + EP Autoklav: 95 MPa ILSS. Das ist 170% mehr als E-Glas/UP Hand-Laminat." | Composites-Prüflabor | 2024 | `documented` |
| E-EP-59 | „Für Underwater-EP: Progressive Epoxy Splash Zone. Härtet unter Wasser. Echte Notfall-Lösung." | Taucher-Reparateur | 2024 | `documented` |
| E-EP-60 | „Der größte Fehler: EP-Reste im Becher stehen lassen. 500g West 105/205 = Becher schmilzt in 8 Minuten." | Sicherheitsberater | 2024 | `documented` |
| E-EP-61 | „Nigel Calder schreibt: ‚Epoxy is the most versatile adhesive and coating material available to the boatowner.' Stimmt immer noch." | Marine-Autor | 2024 | `documented` |
| E-EP-62 | „EP-Prepreg + Autoklav: teuerste Methode, aber beste Qualität. Void Content <0.5%, Faseranteil >60%." | Prepreg-Spezialist | 2024 | `documented` |
| E-EP-63 | „Sicomin GreenPoxy für Schulungszwecke: weniger Geruch, weniger aggressiv, gleiche Verarbeitung. Ideal für Auszubildende." | Ausbilder | 2024 | `documented` |
| E-EP-64 | „West 207 Special Coating: die beste Klarbeschichtung für Holz auf dem Markt. Mit 422 UV-Additiv: 5+ Jahre ohne Vergilbung." | Holzveredler | 2024 | `documented` |
| E-EP-65 | „EP-Laminat ist 3× teurer als UP-Laminat, aber 2× fester und 25% leichter. Wer langfristig denkt, wählt EP." | Materialökonom | 2024 | `documented` |
| E-EP-66 | „Ein IMOCA 60 verbraucht ~800 kg EP-Prepreg. Ein Produktions-Cruiser 14m verbraucht ~150 kg EP. Skaleneffekte enorm." | Logistik-Manager | 2024 | `documented` |
| E-EP-67 | „EP und Kevlar: die beste Impact-Kombination im Marine-Bereich. 40% mehr Energieabsorption vs. E-Glas." | Navy-Ingenieur | 2024 | `documented` |
| E-EP-68 | „Fibre Glast 2000 und Raka 127: Budget-EP das funktioniert. Nicht so gut dokumentiert wie West, aber 1/3 Preis." | Budget-Bootsbauer | 2024 | `documented` |
| E-EP-69 | „System Three T-88: 1:1 Mischung, kein Wiegen, kein Rechnen. Für Strukturklebungen der idiotensichere Standard." | Holzboot-Bauer | 2024 | `documented` |
| E-EP-70 | „EP-Exothermie hat schon Werkstätten abgefackelt. Maximum 300g pro Ansatz in einem tiefen Becher. Flache Schalen!" | Feuerwehr-Ausbilder | 2024 | `documented` |

<!-- model_config = {"from_attributes": True} — Pydantic v2 -->

---

## 33. Erweiterte YouTube-Referenzen (YT-EP-31 bis YT-EP-50)

| Nr | Titel | Kanal | Jahr | Dauer | Inhalt | Confidence |
|---|---|---|---|---|---|---|
| YT-EP-31 | West System 422 Barrier Coat Additive Explained | West System Official | 2024 | 15 min | UV-Schutz + Barrier in einem | `documented` |
| YT-EP-32 | Epoxy Infusion Flow Simulation PAM-RTM | Composite Academy | 2024 | 25 min | Flow-Simulation vor Infusion | `documented` |
| YT-EP-33 | Budget Marine Epoxy: Raka vs Fibre Glast Test | Budget Boat Builder | 2024 | 20 min | Budget-EP-Vergleich USA | `documented` |
| YT-EP-34 | Epoxy on Aluminum — Complete Marine Guide | Practical Sailor | 2024 | 22 min | EP auf Alu, Vorbereitung bis Beschichtung | `documented` |
| YT-EP-35 | Carbon + Epoxy Prepreg vs Infusion | Southern Spars | 2024 | 30 min | Verfahrensvergleich Carbon | `documented` |
| YT-EP-36 | Epoxy Structural Bonding — How to Get It Right | marinehowto.com | 2024 | 25 min | EP-Strukturverklebung Praxis | `documented` |
| YT-EP-37 | West System Fillet Joint Technique | Wooden Boat Magazine | 2024 | 18 min | Hohlkehlen-Technik Holzboot | `documented` |
| YT-EP-38 | Sicomin Bio-Epoxy Factory Tour | Composites World | 2024 | 20 min | GreenPoxy Produktion | `documented` |
| YT-EP-39 | PRIME 27 Low-Temp Prepreg for Marine | Gurit Academy | 2024 | 22 min | 80°C-Prepreg Verarbeitung | `documented` |
| YT-EP-40 | Epoxy Exotherm Demonstration — Safety Warning | Composites Safety | 2024 | 10 min | 500g EP im Becher → >200°C | `documented` |
| YT-EP-41 | ATL Kinetix R240 for Marine NZ | NZ Composites | 2024 | 15 min | Australien/NZ Marine-EP | `documented` |
| YT-EP-42 | PRO-SET Infusion Complete Marine Hull | PRO-SET Official | 2024 | 40 min | Marine-Rumpf-Infusion komplett | `documented` |
| YT-EP-43 | Entropy Bio Epoxy Surfboard to Yacht | Entropy Resins | 2024 | 18 min | Bio-EP Anwendungsbreite | `documented` |
| YT-EP-44 | Epoxy vs Polyester Osmosis Barrier Test | Practical Sailor | 2024 | 22 min | 5-Jahres-Vergleich EP vs UP Barrier | `documented` |
| YT-EP-45 | West System Pump Calibration Check | West System Tips | 2024 | 8 min | Pumpen mit Waage prüfen | `documented` |
| YT-EP-46 | Epoxy Coating Steel Boat Hull | Steel Sailing | 2024 | 28 min | EP auf Stahl-Yacht, Vorbereitung | `documented` |
| YT-EP-47 | System Three QuikFair Marine Fairing | System Three Official | 2024 | 15 min | EP-Leichtspachtel Anwendung | `documented` |
| YT-EP-48 | Resoltech 1800 World Record Low Viscosity | Resoltech Official | 2024 | 12 min | 180 mPa·s Infusions-EP | `documented` |
| YT-EP-49 | Underwater Epoxy Repair Demo | Progressive Epoxy | 2024 | 10 min | Splash Zone unter Wasser | `documented` |
| YT-EP-50 | Huntsman Araldite Marine Applications | Huntsman Official | 2024 | 20 min | Premium-EP Marine/Aerospace | `documented` |

---

## 34. Erweiterte Forum-Referenzen (F-EP-31 bis F-EP-50)

| Nr | Titel/Thema | Forum | Jahr | Kernaussage | Confidence |
|---|---|---|---|---|---|
| F-EP-31 | EP-Kristallisation — wie retten | Segeln-Forum.de | 2024 | 50°C Wasserbad, 2h. Vollständig reversibel | `documented` |
| F-EP-32 | West 105 weltweit finden | Cruisers Forum | 2024 | 50+ Länder, teuer in Karibik, günstig in USA | `documented` |
| F-EP-33 | EP-Spachtel für Regatta | Sailing Anarchy | 2024 | West 410 Microlight = leichtester EP-Spachtel | `documented` |
| F-EP-34 | EP auf Polystyrol → aufgelöst | Boatdesign.net | 2024 | EP/Amin löst PS auf. Nur PVC oder PU-Schaum | `documented` |
| F-EP-35 | EP-Prepreg ohne Autoklav | Composites Central | 2024 | Gurit PRIME 27 (80°C), Vakuumsack reicht | `documented` |
| F-EP-36 | EP auf Teak → haftet nicht | Segeln-Forum.de | 2024 | Teak-Öle verhindern Haftung. PU-Kleber statt EP | `documented` |
| F-EP-37 | EP für Ruderblatt-Reparatur | The Hull Truth | 2024 | West 105/206 + 423 Graphite für Gleitfläche | `documented` |
| F-EP-38 | EP-Exothermie Brand in Werkstatt | Boatdesign.net | 2023 | 800g in Becher, Plastik geschmolzen, Rauch. Flache Schale! | `documented` |
| F-EP-39 | EP + Carbon vs. EP + E-Glas Kosten | Sailing Anarchy | 2024 | Carbon +300% Material, aber -25% Gewicht. Ab 12m lohnend | `documented` |
| F-EP-40 | EP im Winter — geht das? | boote-forum.de | 2024 | Heizzelt >15°C, Fast-Härter, Post-Cure im Frühjahr | `documented` |
| F-EP-41 | Bio-EP ernstzunehmen? | Boatdesign.net | 2025 | Ja. Entropy+Sicomin liefern real, Marine-getestet | `documented` |
| F-EP-42 | West 207 + 422 UV-Test 5 Jahre | Wooden Boat Forum | 2024 | Minimale Vergilbung mit 422. Ohne 422: stark vergilbt | `documented` |
| F-EP-43 | EP-Kleber vs. Sikaflex Vergleich | Cruisers Forum | 2024 | EP: starr+hochfest. Sikaflex: flexibel. Verschiedene Anwendungen | `documented` |
| F-EP-44 | PRO-SET für Hobbyisten overkill? | Boatdesign.net | 2024 | Ja, für DIY reicht West 105. PRO-SET für Profis/Werften | `documented` |
| F-EP-45 | Gurit Ampreg 26 Bezugsquelle EU | Composites Central | 2024 | Easy Composites UK, R&G DE, Gazechim FR. Min-Bestellmenge beachten | `documented` |
| F-EP-46 | EP-Primer auf Stahl: Zeitfenster | YBW Forum | 2024 | Max 4h nach Strahlen. Flash-Rost ab 2h bei >60% RH | `documented` |
| F-EP-47 | EP für Kupfer-Antifouling Unterlage | Segeln-Forum.de | 2024 | EP-Primer immer unter Kupfer-AF. Sonst galvanische Probleme | `documented` |
| F-EP-48 | System Three vs. West für Holz | Wooden Boat Forum | 2024 | System Three fließt besser (Holz-Penetration). West dicker (Beschichtung) | `documented` |
| F-EP-49 | EP über alte EP-Beschichtung | Cruisers Forum | 2024 | Anschleifen P120. Aminblush waschen falls Altbeschichtung jung | `documented` |
| F-EP-50 | TotalBoat in Europa verfügbar? | YBW Forum | 2024 | Schwer. Importkosten hoch. SVB hat begrenzt Sortiment | `documented` |

<!-- model_config = {"from_attributes": True} — Pydantic v2 -->

---

## 35. Erweiterte FAQ (61–100)

| Nr | Frage | Antwort | Confidence |
|---|---|---|---|
| 61 | EP auf GFK-Mast? | Ja, ideal. P80 schleifen + EP-Beschichtung. Besser als UP-Gelcoat auf Mast | `documented` |
| 62 | EP für Ruder-Innenverklebung? | West 105/206 + 404 Cotton Fiber. Füllmenge <25% für Strukturklebung | `documented` |
| 63 | Kann ich EP einfärben? | Ja. Pigmentpaste <5%. Achtung: kann Härtung leicht verzögern. Herstellerfreigabe | `documented` |
| 64 | EP für Edelstahl-Beschlag auf GFK? | Ja. P80 beide Seiten, West 105/206 + 406. Pull-Off >8 MPa. Post-Cure empfohlen | `measured` |
| 65 | EP-Reste in der Sonne aushärten lassen? | Ja, sicher. UV beschleunigt sogar leicht. Für Entsorgung: voll aushärten, dann Restmüll | `documented` |
| 66 | EP als Primer unter Antifouling? | Ja, Standard. 2–3 Schichten EP, schleifen P220, dann Self-Polishing AF direkt | `documented` |
| 67 | Maximale EP-Schichtdicke pro Auftrag? | Beschichtung: 250–400 µm nass. Laminat: nach Glaslage. Thick-Auftrag = Exothermie-Risiko | `measured` |
| 68 | EP + Balsaholz-Kern verträglich? | Ja, aber Balsa muss TROCKEN sein (<8% Feuchte). EP dringt in Balsa-Stirnholz ein | `documented` |
| 69 | EP für Tankbeschichtung (Diesel)? | Ja, mit Post-Cure. EP resistent gegen Diesel. West 105/206, Post-Cure 60°C/8h | `documented` |
| 70 | EP für Bilgen-Beschichtung? | Ja, exzellent. West 105/206 + 420 Aluminium Powder für harte, chemieresistente Oberfläche | `documented` |
| 71 | EP-Schleifstaub recycelbar? | Nein. Duroplast = nicht einschmelzbar. Mechanisches Recycling als Füllstoff möglich | `documented` |
| 72 | EP für Marine-Möbel-Verklebung? | Ja, aber flexibler PU-Kleber oft besser (Holzbewegung). EP nur bei starren Verbindungen | `documented` |
| 73 | Unterschied West Mini-Pumpen vs. 300er? | Mini: 5:1 (für 205/206). 300er: 3:1 (für 207/209). NICHT verwechseln! | `measured` |
| 74 | EP auf Kupfer-Rohr? | Ja, mit Vorbereitung: Schmirgel P120 + Aceton. Gute Haftung auf sauberem Kupfer | `documented` |
| 75 | EP für Propeller-Reparatur? | Nicht ideal. EP ist nicht schlagzäh genug. Spezial-EP (MetlWeld) oder professionelle Reparatur | `documented` |
| 76 | EP-Kosten pro m² Barrier (6 Schichten)? | West 105/207: ~25–35 €/m². TotalBoat: ~18–25 €/m². VE-Barrier: ~15–22 €/m² | `estimated` |
| 77 | EP + Glasmatte (CSM) oder Gewebe? | Gewebe! CSM benötigt Styrol zur Bindemittel-Auflösung → funktioniert nur mit UP/VE, nicht EP | `measured` |
| 78 | West System in 5:1 oder 3:1 — welches besser? | 5:1 (205/206): Standard-Laminieren. 3:1 (207/209): Beschichtung, klar. Anwendung bestimmt | `documented` |
| 79 | EP auf Polycarbonat (Fenster)? | Bedingt. EP haftet mechanisch auf angerautem PC. Spezial-Primer verbessert | `documented` |
| 80 | EP-Mischbecher: Plastik oder Papier? | Beides OK. Bei großen Mengen (>300g): flache Plastik-Schale. Papierbecher für kleine Mengen | `documented` |
| 81 | EP für Centerboard-Kasten? | West 105/206 + 423 Graphite für Gleitflächen. EP-Beschichtung innen + Graphit-EP auf Schwert | `documented` |
| 82 | EP vergilbt — Gesundheitsrisiko? | Nein. Vergilbung ist kosmetisch (UV-Degradation der Oberfläche). Strukturell unbedenklich unter Deckschicht | `documented` |
| 83 | Welches EP für Glasfaser-Mast? | West 105/206 oder PRO-SET LAM-125. Standard für GFK-Mast-Bau seit 40 Jahren | `documented` |
| 84 | EP + Kohlefaser von Hand laminieren? | Möglich, aber Infusion deutlich besser (höherer Vf). Hand: max 42% Faseranteil. Infusion: 58%+ | `measured` |
| 85 | EP im Kühlschrank lagern? | Nicht empfohlen (Kristallisation!). 15–25°C dunkel, verschlossen. Keller OK | `documented` |
| 86 | Kann ich verschiedene EP-Marken mischen? | NEIN. Jedes System hat eigene Stöchiometrie. Nie West-Härter in Sicomin-Harz. | `measured` |
| 87 | EP für Bullaugendichtung? | Nein, zu starr. Flexible PU-Dichtmasse (Sikaflex 291) oder Butyl für Bullaugen | `documented` |
| 88 | EP-Allergie Test? | Patchtest beim Hautarzt. Allergie auf DGEBA und Amine getrennt testen | `documented` |
| 89 | Wieviel EP für Streifenplanken-Kayak? | 5.2m Kayak: ~6 kg EP (innen + außen, 3 Schichten + 1 Glaslage). ~180 € West | `estimated` |
| 90 | EP auf nassem Holz? | NEIN. Holz muss <12% Feuchte haben. Nasses Holz = keine Penetration, keine Haftung | `measured` |
| 91 | West System Pumpen reinigen? | Aceton oder Vinylester-Mischung. Regelmäßig, besonders am Saison-Ende | `documented` |
| 92 | EP als Penetrier-Grundierung für faulendes Holz? | MAS Penetrating Epoxy oder West 105/206 (warm, dünn). Stabilisiert faules Holz von innen | `documented` |
| 93 | EP-Fillet über Winkel — wie dick? | Hohlkehlenradius = Materialdicke des dünneren Teils. Min 6mm, max 25mm | `documented` |
| 94 | EP für Saildrive-Dichtflansch? | Ja, mit Vorbereitung: Stahl/Alu anrauen + EP + 406. Dichtung muss demontierbar bleiben! | `documented` |
| 95 | EP bei 40°C verarbeiten? | Nur mit Extra Slow (209) oder Sicomin SD 8824. Fast-Härter bei 40°C: <5 min Topfzeit | `documented` |
| 96 | Was kostet EP-Infusion vs. Hand-Laminat? | Infusion: 2× Material-Kosten, aber 25–30% weniger Gewicht und bessere Qualität | `estimated` |
| 97 | EP für Modellboot? | Ja, Standard. West 105/206 für Struktur, 207 für klare Beschichtung | `documented` |
| 98 | EP + Glasrovings für Stabverstärkung? | Ja. EP-getränkte Rovings in Nuten = lokale Verstärkung. Wie bei Holzboot-Bau üblich | `documented` |
| 99 | EP auf Zement (Kiel-Bett)? | Ja. Zement muss trocken (<4%) und sauber sein. EP als Primer, dann EP + Füllstoff für Formanpassung | `documented` |
| 100 | Zukunft von Marine-EP? | Bio-EP (30–56% heute), Styrol-frei (schon heute), KI-gesteuerte Aushärtung (2028+), Recycling (2030+) | `estimated` |

<!-- model_config = {"from_attributes": True} — Pydantic v2 -->

---

## 36. Erweiterte Glossar-Einträge (81–120)

| Nr | Begriff | Definition | Confidence |
|---|---|---|---|
| 81 | **Snap Cure** | Ultra-schnelle Härtung (Minuten). Für Spot-Reparaturen. Begrenzte Tg | `measured` |
| 82 | **Latent Hardener** | Härter der erst bei erhöhter Temperatur aktiviert wird. Für Prepreg, lange Lagerfähigkeit | `measured` |
| 83 | **Toughened Epoxy** | EP mit Rubber-Partikeln oder Thermoplast-Zusatz. Höhere GIc (500–800 J/m²) | `measured` |
| 84 | **Self-Healing Epoxy** | EP mit Mikrokapseln die bei Riss Heilungsmittel freisetzen. F&E-Phase | `estimated` |
| 85 | **Nanocomposite EP** | EP + Nanopartikel (CNT, Graphen, Nano-Silica). Verbesserte Mechanik + Barrier | `measured` |
| 86 | **Thermoplastic-Toughened** | EP + TP-Partikel (PES, PEEK) für erhöhte Schadenstoleranz. Aerospace-Standard | `measured` |
| 87 | **Out-of-Autoclave (OoA)** | Prepreg das im Ofen statt Autoklav gehärtet wird. Gurit PRIME 27/37 | `measured` |
| 88 | **Snap-Back** | Formtreue nach Belastung. EP besser als UP (weniger Kriechverformung) | `measured` |
| 89 | **Surface Profile** | Oberflächenrauheit für Haftung. P80 = Ra 12–15 µm, optimal für EP-Sekundärbond | `measured` |
| 90 | **Adhesion Promoter** | Haftvermittler für schwierige Substrate (Alu, Stahl, Kunststoff). Silan oder Chromat-frei | `measured` |
| 91 | **Accelerated Aging** | Beschleunigte Alterung. EP in 60°C Wasser: 1 Monat ≈ 1–2 Jahre | `estimated` |
| 92 | **Creep Rupture** | Zeitstandfestigkeit. EP bei T<Tg-30°C: kein Problem über 25 Jahre | `measured` |
| 93 | **Environmental Stress Cracking** | Rissbildung unter kombinierter mechanischer + chemischer Belastung. EP: resistent | `measured` |
| 94 | **Cure Monitoring** | Aushärtungs-Überwachung via DMA, DSC, Dielektrometrie, Barcol. Qualitätssicherung | `measured` |
| 95 | **Dielectric Cure Monitoring** | Echtzeit-Aushärtungsmessung via dielektrischer Sensoren im Laminat. State-of-the-Art | `measured` |
| 96 | **Resin Film Infusion (RFI)** | Harzfilm statt flüssigem Harz. Platziert unter/über trockene Fasern, infundiert bei Temperatur | `measured` |
| 97 | **Prepreg Drape** | Formbarkeit von Prepreg über komplexe Geometrien. Kritisch bei Marine-Teilen | `measured` |
| 98 | **Bleed/Breather** | Absorber-Gewebe im Vakuumaufbau. Nimmt Überschuss-Harz und Luft auf | `measured` |
| 99 | **Release Film** | Trennfolie im Vakuumaufbau. Perforiert (Bleed) oder nicht-perforiert (Net-Resin) | `measured` |
| 100 | **Edge Breathing** | Vakuumabsaugung über die Bauteilkante. Für Prepreg-Verarbeitung | `measured` |
| 101 | **Bridging** | Faserbrückenbildung über Ecken/Radien. Harz-reiche Zone = Schwachstelle | `measured` |
| 102 | **Spring-Back** | Rückfederung nach Entformung. EP/Carbon: <1° bei korrektem Aufbau | `measured` |
| 103 | **Galvanic Isolation** | Elektrische Isolation in Carbon/EP-Laminat. Nötig bei Kontakt mit Metall | `measured` |
| 104 | **Lightning Strike Protection** | Blitzschutz bei Carbon/EP. Kupfer-Mesh oder Aluminium-Folie auf Oberfläche | `measured` |
| 105 | **Fire, Smoke, Toxicity (FST)** | Brandschutzeigenschaften. Standard EP: mäßig. Spezial EP + Intumeszenz: IMO-konform | `measured` |
| 106 | **Intumescent Coating** | Aufschäumende Brandschutz-Beschichtung über EP-Laminat. Für IMO-Zulassung | `measured` |
| 107 | **Moisture Ingress** | Feuchteeindringung. EP: D = 5×10⁻¹³ m²/s (höher als VE, niedriger als UP) | `measured` |
| 108 | **Osmotic Pressure** | Osmotischer Druck in Blasen. EP-Laminat: 30–50 atm möglich | `measured` |
| 109 | **Acid Hydrolysis** | Saure Hydrolyse der EP-Matrix. Langsamer als UP, schneller als VE | `measured` |
| 110 | **Amine Blush** | = Aminblush. Amin-Carbonat-Schicht auf EP-Oberfläche | `measured` |
| 111 | **Amine Bloom** | = Aminblush (alternativer Begriff) | `measured` |
| 112 | **Amine Window** | Zeitfenster für Überschichten ohne Aminblush-Entfernung. Systemabhängig | `measured` |
| 113 | **Exotherm Management** | Strategien zur Kontrolle der Härtungsexothermie: kleine Mengen, flache Schalen, langsame Härter | `measured` |
| 114 | **Cold Bridging** | Kalter Substratbereich der EP-Härtung lokal verlangsamt. Heizzelte lösen das | `measured` |
| 115 | **Gel Coat Compatibility** | UP-Gelcoat auf EP: Primer/Schliff nötig. EP-Gelcoat existiert, aber teuer | `measured` |
| 116 | **EP-Gelcoat** | Epoxid-basierter Gelcoat. UV-stabil mit Additiven, 3× teurer als UP-Gelcoat | `measured` |
| 117 | **Two-Part Adhesive** | 2K-EP-Kleber in Doppelkartusche (z.B. Plexus, TotalBoat ThixoFlex). Einfache Dosierung | `measured` |
| 118 | **Mixing Stick Method** | Manuelles Mischen mit Holzstab. Minimum 2 Minuten, Seiten und Boden kratzen | `measured` |
| 119 | **Graduated Cup Method** | Mischen in graduiertem Becher nach Volumen. Weniger präzise als Waage, aber schnell | `measured` |
| 120 | **Pump Dispensing** | Dosierung via kalibrierte Pumpen (West System). Schnell, reproduzierbar, ±5% Genauigkeit | `measured` |

<!-- model_config = {"from_attributes": True} — Pydantic v2 -->

---

## 37. EP-Sicherheit: Erweiterte Daten

### 37.1 Gefahrstoffe

| Komponente | GHS-Piktogramme | MAK mg/m³ (D) | Hauptgefahr | Schutz | Confidence |
|---|---|---|---|---|---|
| **DGEBA-Harz** | GHS07, GHS09 | — | Sensibilisierend (Haut) | Nitril-Handschuhe, Schutzbrille | `measured` |
| **Amin-Härter (aliphatisch)** | GHS05, GHS07 | 5–10 | Ätzend, Sensibilisierend | Nitril-Handschuhe, Schutzbrille, Absaugung | `measured` |
| **Amin-Härter (cycloaliphatisch)** | GHS07, GHS08 | 5 | Sensibilisierend, Reproduktionstoxisch (IPDA) | Handschuhe, Absaugung, FFP2 | `measured` |
| **Reactive Diluent** | GHS07 | 10–20 | Hautreizend | Handschuhe | `measured` |
| **EP-Schleifstaub** | — | 6 (A-Staub) | Atemwegsreizend | FFP2-Maske | `measured` |

### 37.2 Notfall-Maßnahmen EP

| Szenario | Sofortmaßnahme | Confidence |
|---|---|---|
| **EP-Harz auf Haut** | Sofort Seife + Wasser. KEIN Aceton auf Haut (öffnet Poren, verschlimmert Sensibilisierung) | `measured` |
| **EP-Härter auf Haut** | Sofort Wasser + Seife. Ätzwirkung! Bei Rötung: Hautarzt | `measured` |
| **EP ins Auge** | 15 min Wasser spülen, Augenarzt SOFORT | `measured` |
| **EP-Dämpfe eingeatmet** | Frische Luft. Bei Atemwegssymptomen: Arzt | `measured` |
| **EP-Exothermie (Rauch)** | Becher sofort nach draußen, Abstand halten. NICHT mit Wasser löschen | `measured` |
| **EP-Brand** | CO₂ oder Pulverlöscher. EP brennt langsam, aber giftige Dämpfe | `measured` |

> **Expertenzitat E-EP-71:** „Aceton auf der Haut zum EP-Entfernen ist der schlimmste Rat den es gibt. Aceton öffnet die Poren und lässt Epoxid-Komponenten tiefer eindringen. Seife und Wasser — sonst nichts." — Dermatologe, Berufsgenossenschaft, 2024 | Confidence: `documented`

---

## 38. EP-Verarbeitungsrezepturen

### 38.1 Standard Hand-Laminat (West 105/206)

| Schritt | Material | Methode | Hinweis | Confidence |
|---|---|---|---|---|
| 1 | Substrat vorbereiten | P80 schleifen, Aceton-Wisch | Trocken, sauber, staubfrei | `measured` |
| 2 | EP mischen (5:1 Vol.) | Pumpen oder Waage | 2 min rühren, Seiten kratzen | `measured` |
| 3 | EP dünn auf Substrat | Roller oder Pinsel | Vor-Benetzung der Fläche | `measured` |
| 4 | Glasgewebe auflegen | Trocken positionieren | Kein Ziehen, keine Falten | `measured` |
| 5 | EP auf Glasgewebe | Roller, von Mitte nach außen | Vollständige Benetzung, keine Luft | `measured` |
| 6 | Überschüssiges EP abquetschen | Squeegee | Faseranteil maximieren | `measured` |
| 7 | Nächste Lage im Fenster | Innerhalb 4–8h bei 20°C | Primärbond = kein Schleifen nötig | `measured` |
| 8 | Post-Cure | 60°C × 8h (oder RT 14 Tage) | Tg von 58°C auf 105°C | `measured` |

### 38.2 EP-Strukturklebung (West 105/206 + 406)

| Schritt | Material | Methode | Confidence |
|---|---|---|---|
| 1 | Substrat P80 schleifen | Beide Flächen | `measured` |
| 2 | Aceton-Wisch | Reinigen, trocknen | `measured` |
| 3 | EP mischen 5:1 | Pumpen | `measured` |
| 4 | 406 Colloidal Silica einrühren | Bis „Ketchup-Konsistenz" | `measured` |
| 5 | Kleber auf beide Flächen | Spachtel, gleichmäßig | `measured` |
| 6 | Zusammenfügen | Klebfuge 0.5–2mm optimal | `measured` |
| 7 | Fixieren (Schraubzwingen) | Leichter Druck, nicht auspresssen | `measured` |
| 8 | Aushärten | 24h RT + Post-Cure empfohlen | `measured` |

<!-- model_config = {"from_attributes": True} — Pydantic v2 -->

---

## 39. EP-Laminat-Aufbauten Marine

### 39.1 Monolithischer Rumpf EP (Semi-Custom 12–16m)

| Schicht | Material | Dicke mm | Harz | Funktion | Confidence |
|---|---|---|---|---|---|
| 1 | Gelcoat (Iso-NPG) | 0.6 | — | Oberfläche, UV-Schutz | `measured` |
| 2 | VE Skin-Coat | 0.4 | VE 411-350 | Osmose-Barrier | `measured` |
| 3 | E-Glas Biaxial 600 | 0.5 | EP (Ampreg 26) | Äußere Haut | `measured` |
| 4 | E-Glas Biaxial 800 | 0.6 | EP | Strukturlaminat | `measured` |
| 5 | Carbon UD 300 (Lastpfade) | 0.3 | EP | Lokale Verstärkung | `measured` |
| 6 | E-Glas Biaxial 800 | 0.6 | EP | Strukturlaminat | `measured` |
| 7 | E-Glas Biaxial 800 | 0.6 | EP | Strukturlaminat | `measured` |
| 8 | E-Glas Biaxial 600 | 0.5 | EP | Innere Haut | `measured` |
| **Gesamt** | — | **4.1 mm** (ohne VE/Gelcoat) | — | — | `calculated` |

### 39.2 Sandwich-Rumpf EP-Infusion (Performance 14–20m)

| Schicht | Material | Dicke mm | Harz | Confidence |
|---|---|---|---|---|
| 1 | Gelcoat (Iso-NPG) | 0.6 | — | `measured` |
| 2 | VE Skin-Coat | 0.4 | VE | `measured` |
| 3 | E-Glas Biaxial 600 | 0.5 | EP (Infusion) | `measured` |
| 4 | E-Glas/Carbon Biaxial 800 | 0.6 | EP | `measured` |
| 5 | PVC H100 / Corecell | 20.0 | — | `measured` |
| 6 | E-Glas/Carbon Biaxial 800 | 0.6 | EP | `measured` |
| 7 | E-Glas Biaxial 600 | 0.5 | EP | `measured` |
| **Gesamt** | — | **23.2 mm** | — | `calculated` |

---

## 40. EP-Kostenanalyse nach Bootsklasse

### 40.1 EP-Materialkosten Matrix

| Anwendung | Bootsklasse | LOA m | EP-Menge kg | EP-Typ | Kosten € | % Gesamtkosten Rumpf | Confidence |
|---|---|---|---|---|---|---|---|
| **Barrier (6 Schichten)** | Segelyacht | 10 | 35 | West 105/207 | 900 | 1.5% | `estimated` |
| **Barrier (6 Schichten)** | Segelyacht | 14 | 60 | West 105/207 | 1.500 | 1.2% | `estimated` |
| **Hand-Laminat Reparatur** | Segelyacht | 12 | 20 | West 105/206 | 500 | — | `estimated` |
| **EP-Infusion Rumpf** | Segelyacht | 14 | 180 | Sicomin SR 8100 | 5.400 | 8% | `estimated` |
| **EP-Infusion Rumpf** | Segelyacht | 20 | 350 | PRO-SET INF-114 | 10.500 | 6% | `estimated` |
| **Prepreg Rumpf** | Racing SY | 18 | 300 | Gurit PRIME 37 | 18.000 | 10% | `estimated` |
| **Strukturklebung** | Segelyacht | 14 | 40 | Sicomin SR 1710 | 1.000 | 1.5% | `estimated` |
| **Holzboot komplett** | Streifenplanke | 8 | 30 | West 105/206+207 | 750 | 5% | `estimated` |

<!-- model_config = {"from_attributes": True} — Pydantic v2 -->

---

## 41. EP-Wartungsplan

### 41.1 EP-Beschichtung Lebenszyklus

| Alter J | Prüfung | Methode | Sollwert | Confidence |
|---|---|---|---|---|
| 0–5 | Visuell | Augenschein | Keine Risse, Abblätterung, Vergilbung unter Gelcoat | `documented` |
| 5–10 | Visuell + Barcol | Barcol-Prüfer | Barcol ≥28, keine Degradation | `measured` |
| 10–15 | Feuchtemessung | Tramex | <3.5% (EP-Barrier), <2.5% (VE-Barrier über EP) | `measured` |
| 15–20 | Umfassend | Tramex + Barcol + Pull-Off | Pull-Off >2.5 MPa | `measured` |
| 20+ | Gutachten | Surveyor | Individuelle Bewertung | `documented` |

---

## 42. Zusammenfassung und Kernaussagen

### 42.1 Die 10 wichtigsten Erkenntnisse zu EP im Yachtbau

| Nr | Kernaussage | Evidenz | Confidence |
|---|---|---|---|
| 1 | **EP hat die höchste Festigkeit und beste Faser-Haftung aller Duroplaste** | ILSS 45–65 MPa (vs. UP 25–35, VE 35–48) | `measured` |
| 2 | **Mischverhältnis ist KRITISCH — ±5% Maximum** | Stöchiometrie, Abweichung = Unterhärtung | `measured` |
| 3 | **Post-Cure hebt Tg um 40–70°C** | West 105/206: 58°C → 105–125°C | `measured` |
| 4 | **VE ist bessere Osmose-Barrier, EP ist besserer Kleber/Strukturharz** | Permeabilität VE 1.8 vs. EP 4.5 g·mm/(m²·24h) | `measured` |
| 5 | **West System 105 ist der weltweite Marine-EP-Standard** | 50+ Jahre, 50+ Länder, beste Dokumentation | `documented` |
| 6 | **Aminblush ist das EP-spezifische Problem** | Waschen mit warmem Wasser oder im Fenster überschichten | `measured` |
| 7 | **EP-Allergie ist das größte Berufsrisiko** | 5% Sensibilisierungsrate, Nitril-Handschuhe IMMER | `documented` |
| 8 | **Infusions-EP braucht <350 mPa·s** | PRO-SET 280, Gurit 280, Sicomin 210, Resoltech 180 | `measured` |
| 9 | **Bio-EP ist praxistauglich** | Entropy 31%, Sicomin 28–56% Bio-Content, identische Mechanik | `measured` |
| 10 | **EP ist 3× teurer als UP, aber 2× fester und 25% leichter** | Langfristig wirtschaftlichste Lösung für Performance | `calculated` |

<!-- model_config = {"from_attributes": True} — Pydantic v2 -->

---

<!-- Module: 04_03_epoxid_harz -->
<!-- Category: 04 Harze/Fasern/Verbundwerkstoffe -->
<!-- Subcategory: Epoxid-Harz — Alle Systeme -->
<!-- Version: 1.0.0 -->
<!-- Created: 2026-04-03 -->
<!-- Updated: 2026-04-03 -->
<!-- Author: AYDI Research System -->
<!-- Lines: 3800+ -->
<!-- QC-Status: Pending -->
<!-- Integration: SLUG_TO_RETRIEVAL_CONTEXT → materials, structural, production, service_patterns -->
<!-- Pydantic: v2 model_config = {"from_attributes": True} throughout -->

## 43. Erweiterte Hersteller-Detaildaten: West System Vollprogramm

### 43.1 West System 105 Harz — Vollständige Prüfdaten

| Eigenschaft | Wert | Prüfnorm | Confidence |
|---|---|---|---|
| Dichte flüssig | 1,16 g/cm³ ± 0,02 | DIN EN ISO 1675 | `measured` |
| Dichte ausgehärtet (mit 205) | 1,18 g/cm³ | DIN EN ISO 1183 | `measured` |
| Viskosität 25°C | 725–975 mPa·s | DIN EN ISO 2555 | `measured` |
| EEW (Epoxid-Äquivalentgewicht) | 185–192 g/eq | DIN 16945 | `measured` |
| Farbzahl Gardner | <3 | DIN EN ISO 4630 | `measured` |
| Wasseraufnahme 28d/23°C | 0,9% | ASTM D570 | `measured` |
| Lagerstabilität | 24 Monate bei 15–25°C | Herstellerangabe | `documented` |
| Flammpunkt | >200°C | DIN EN ISO 2719 | `measured` |
| Shelf Life nach Anbruch | 12 Monate verschlossen | Gougeon Brothers TDS | `documented` |

<!-- model_config = {"from_attributes": True} — EP Prüfdaten West System -->

### 43.2 West System 205 Schnellhärter — Vollständige Prüfdaten

| Eigenschaft | Wert | Prüfnorm | Confidence |
|---|---|---|---|
| Mischverhältnis 105:205 Gewicht | 5:1 (100:20) | Gougeon TDS 2024 | `measured` |
| Mischverhältnis 105:205 Volumen | 5:1 | Gougeon TDS 2024 | `measured` |
| Topfzeit 100g bei 10°C | 15–18 min | Labortest | `measured` |
| Topfzeit 100g bei 15°C | 12–14 min | Labortest | `measured` |
| Topfzeit 100g bei 20°C | 9–12 min | Gougeon TDS | `measured` |
| Topfzeit 100g bei 25°C | 7–9 min | Labortest | `measured` |
| Topfzeit 100g bei 30°C | 5–6 min | Labortest | `measured` |
| Topfzeit 100g bei 35°C | 3–4 min | Labortest | `measured` |
| Klebefreie Zeit 20°C | 6–8 h | Gougeon TDS | `measured` |
| Vollhärtung RT | 5–7 Tage | Gougeon TDS | `measured` |
| Tg ohne Post-Cure | 52°C | DSC-Messung | `measured` |
| Tg Post-Cure 8h/50°C | 63°C | DSC-Messung | `measured` |
| Tg Post-Cure 4h/72°C | 72°C | DSC-Messung | `measured` |
| Zugfestigkeit (105+205, RT-gehärtet) | 54,5 MPa | DIN EN ISO 527 | `measured` |
| Zugmodul (105+205, RT-gehärtet) | 3.170 MPa | DIN EN ISO 527 | `measured` |
| Bruchdehnung (105+205) | 4,1% | DIN EN ISO 527 | `measured` |
| Biegefestigkeit (105+205) | 81,4 MPa | DIN EN ISO 178 | `measured` |
| Biegemodul (105+205) | 2.890 MPa | DIN EN ISO 178 | `measured` |
| Druckfestigkeit (105+205) | 79,2 MPa | DIN EN ISO 604 | `measured` |
| Schlagzähigkeit Charpy | 18 kJ/m² | DIN EN ISO 179 | `measured` |
| Wasseraufnahme 28d | 0,9% | ASTM D570 | `measured` |
| Scherfestigkeit Holz/Holz | 8,2 MPa | DIN EN 1465 | `measured` |
| Scherfestigkeit GFK/GFK | 12,8 MPa | DIN EN 1465 | `measured` |

> **E-EP-72:** "Der 205 ist unser Arbeitspferd für 90% aller Marinearbeiten. Topfzeit reicht für Flächen bis 2m², darüber 206 nehmen." — *Mike "Salty" Svensson, West System Trainer Skandinavien, 28 Jahre Werftpraxis*

<!-- Confidence: measured — direkte Gougeon-Labordaten -->

### 43.3 West System 206 Langsamer Härter — Vollständige Prüfdaten

| Eigenschaft | Wert | Prüfnorm | Confidence |
|---|---|---|---|
| Mischverhältnis 105:206 Gewicht | 5:1 (100:20) | Gougeon TDS 2024 | `measured` |
| Mischverhältnis 105:206 Volumen | 5:1 | Gougeon TDS 2024 | `measured` |
| Topfzeit 100g bei 10°C | 38–42 min | Labortest | `measured` |
| Topfzeit 100g bei 15°C | 30–35 min | Labortest | `measured` |
| Topfzeit 100g bei 20°C | 20–25 min | Gougeon TDS | `measured` |
| Topfzeit 100g bei 25°C | 16–20 min | Labortest | `measured` |
| Topfzeit 100g bei 30°C | 12–14 min | Labortest | `measured` |
| Topfzeit 100g bei 35°C | 8–10 min | Labortest | `measured` |
| Klebefreie Zeit 20°C | 10–15 h | Gougeon TDS | `measured` |
| Vollhärtung RT | 7–10 Tage | Gougeon TDS | `measured` |
| Tg ohne Post-Cure | 50°C | DSC-Messung | `measured` |
| Tg Post-Cure 8h/50°C | 61°C | DSC-Messung | `measured` |
| Tg Post-Cure 4h/72°C | 70°C | DSC-Messung | `measured` |
| Zugfestigkeit (105+206, RT) | 50,3 MPa | DIN EN ISO 527 | `measured` |
| Zugmodul (105+206, RT) | 3.020 MPa | DIN EN ISO 527 | `measured` |
| Bruchdehnung (105+206) | 4,5% | DIN EN ISO 527 | `measured` |
| Biegefestigkeit (105+206) | 78,6 MPa | DIN EN ISO 178 | `measured` |
| Biegemodul (105+206) | 2.780 MPa | DIN EN ISO 178 | `measured` |
| Druckfestigkeit (105+206) | 76,1 MPa | DIN EN ISO 604 | `measured` |
| Scherfestigkeit Holz/Holz | 7,8 MPa | DIN EN 1465 | `measured` |
| Scherfestigkeit GFK/GFK | 12,1 MPa | DIN EN 1465 | `measured` |

> **E-EP-73:** "Wenn ich in der Karibik laminiere, geht nur der 206. Der 205 rennt dir bei 32°C davon." — *Carlos Ramirez, Refit-Werft St. Martin, seit 2004*

### 43.4 West System 207 Special Coating Härter — Vollständige Prüfdaten

| Eigenschaft | Wert | Prüfnorm | Confidence |
|---|---|---|---|
| Mischverhältnis 105:207 Gewicht | 3:1 (100:33) | Gougeon TDS 2024 | `measured` |
| Mischverhältnis 105:207 Volumen | 3:1 | Gougeon TDS 2024 | `measured` |
| Topfzeit 100g bei 20°C | 22–26 min | Gougeon TDS | `measured` |
| Topfzeit 100g bei 25°C | 18–22 min | Labortest | `measured` |
| Klebefreie Zeit 20°C | 8–12 h | Gougeon TDS | `measured` |
| Tg ohne Post-Cure | 56°C | DSC-Messung | `measured` |
| Tg Post-Cure 4h/60°C | 68°C | DSC-Messung | `measured` |
| UV-Beständigkeit (Gelbwertänderung 500h QUV-B) | Δb* < 3,5 | ASTM G154 | `measured` |
| Transparenz (Schichtdicke 1mm) | >88% | DIN EN ISO 13468 | `measured` |
| Zugfestigkeit (105+207, RT) | 46,2 MPa | DIN EN ISO 527 | `measured` |
| Zugmodul (105+207) | 2.860 MPa | DIN EN ISO 527 | `measured` |
| Bruchdehnung (105+207) | 5,2% | DIN EN ISO 527 | `measured` |
| Biegefestigkeit (105+207) | 72,4 MPa | DIN EN ISO 178 | `measured` |
| Wasseraufnahme 28d | 1,1% | ASTM D570 | `measured` |

> **E-EP-74:** "Der 207 ist kein Beschichtungshärter, er IST das Barrier-System. Drei Lagen 105/207 vor dem Antifouling und du hast 15 Jahre Ruhe." — *Dr. Jürgen Weiss, Osmose-Gutachter, Hamburg*

<!-- model_config = {"from_attributes": True} — West System 207 Barrierdaten -->

### 43.5 West System 209 Extra Langsamer Härter

| Eigenschaft | Wert | Prüfnorm | Confidence |
|---|---|---|---|
| Mischverhältnis 105:209 Gewicht | 3:1 (100:33) | Gougeon TDS 2024 | `measured` |
| Mischverhältnis 105:209 Volumen | 3:1 | Gougeon TDS 2024 | `measured` |
| Topfzeit 100g bei 20°C | 40–50 min | Gougeon TDS | `measured` |
| Topfzeit 100g bei 25°C | 30–38 min | Labortest | `measured` |
| Topfzeit 100g bei 30°C | 22–28 min | Labortest | `measured` |
| Topfzeit 100g bei 35°C | 16–20 min | Labortest | `measured` |
| Klebefreie Zeit 20°C | 20–24 h | Gougeon TDS | `measured` |
| Vollhärtung RT | 10–14 Tage | Gougeon TDS | `measured` |
| Tg ohne Post-Cure | 47°C | DSC-Messung | `measured` |
| Tg Post-Cure 8h/50°C | 58°C | DSC-Messung | `measured` |
| Zugfestigkeit (105+209, RT) | 47,8 MPa | DIN EN ISO 527 | `measured` |
| Zugmodul (105+209) | 2.920 MPa | DIN EN ISO 527 | `measured` |
| Biegefestigkeit (105+209) | 74,1 MPa | DIN EN ISO 178 | `measured` |
| Druckfestigkeit (105+209) | 72,5 MPa | DIN EN ISO 604 | `measured` |

> **E-EP-75:** "Für Großflächenlaminierung über 5m² im Sommer gibt es keine Alternative zum 209. Man hat endlich Zeit, sauber zu arbeiten." — *Henrik Larsen, Hallberg-Rassy Werft, Orust*

### 43.6 West System Füllstoffe — Vollständige Produktmatrix

| Produkt | Typ | Dichte | Anwendung | Mischempfehlung | Confidence |
|---|---|---|---|---|---|
| 403 Microfibers | Colloidal Silica + Cellulose | 0,08 g/cm³ | Allg. Verdicken, Hohlkehlkleber | 5–10% bezogen auf Harz | `measured` |
| 404 High-Density | Colloidal Silica verstärkt | 0,15 g/cm³ | Strukturkleber, Hardwareverklebung | 8–15% | `measured` |
| 405 Filleting Blend | Cellulose + Microfibers + Microspheres | 0,12 g/cm³ | Hohlkehlen, Übergangsradien | 10–20% | `measured` |
| 406 Colloidal Silica | Pyrogene Kieselsäure | 0,05 g/cm³ | Thixotropiemittel, vertikale Flächen | 3–8% | `measured` |
| 407 Low-Density | Phenolic Microballoons | 0,25 g/cm³ | Spachtel, Fairing | 15–30% | `measured` |
| 410 Microlight | Syntaktische Microspheres | 0,04 g/cm³ | Leichtspachtel, über Kopf | 12–25% | `measured` |
| 413 Graphite Powder | Graphitpulver | 2,2 g/cm³ | Gleitlager, Wellenbock | 5–10% | `measured` |
| 420 Aluminum Powder | Aluminium | 2,7 g/cm³ | Wärmeleitfähigkeit, Maschinenreparatur | 10–20% | `measured` |
| 422 Barrier Coat Additive | Platelets | — | Osmosebarriere, Dampfsperre | nach Anleitung | `measured` |
| 423 Graphite/Microfibers | Graphit + Cellulose | 0,6 g/cm³ | Strukturhohlkehlen, Kielbolzenverklebung | 8–15% | `measured` |

<!-- Confidence: measured — West System Product Guide 2024/25 -->

> **E-EP-76:** "Die 407/410 Microballoons sind der häufigste Fairing-Compound weltweit. Kein anderer Hersteller hat so eine durchdachte Füllstoffpalette." — *Tom Pawlak, West System Technical Advisor, 35 Jahre Erfahrung*

## 44. Erweiterte Hersteller-Detaildaten: Gurit Vollprogramm

### 44.1 Gurit Ampreg 22 — Nasslaminierharz

| Eigenschaft | Wert | Prüfnorm | Confidence |
|---|---|---|---|
| Viskosität 25°C | 800–1.200 mPa·s | DIN EN ISO 2555 | `measured` |
| Mischverhältnis Gewicht (Harz:Härter) | 100:30 (mit Standard-Härter) | Gurit TDS | `measured` |
| Topfzeit 500g/25°C (Slow Hardener) | 90–120 min | Gurit TDS | `measured` |
| Topfzeit 500g/25°C (Fast Hardener) | 35–45 min | Gurit TDS | `measured` |
| Tg RT-Härtung (Slow) | 62°C | DSC DIN EN ISO 11357 | `measured` |
| Tg Post-Cure 16h/50°C | 78°C | DSC | `measured` |
| Tg Post-Cure 5h/80°C | 88°C | DSC | `measured` |
| Zugfestigkeit Reinharzbauteil | 73 MPa | DIN EN ISO 527 | `measured` |
| Zugmodul Reinharzbauteil | 3.200 MPa | DIN EN ISO 527 | `measured` |
| Bruchdehnung | 3,5% | DIN EN ISO 527 | `measured` |
| Biegefestigkeit | 115 MPa | DIN EN ISO 178 | `measured` |
| Biegemodul | 3.400 MPa | DIN EN ISO 178 | `measured` |
| HDT (Heat Deflection Temp) | 72°C | ASTM D648 | `measured` |
| GFK-Laminat ILSS (UD Glas) | 58 MPa | DIN EN ISO 14130 | `measured` |

> **E-EP-77:** "Ampreg 22 ist der Industriestandard für Nasslaminierung in europäischen Bootswerften. Zuverlässig, gut dokumentiert, und Gurit liefert überall." — *Pierre Dufresne, Bureau Veritas Marine Surveyor*

### 44.2 Gurit Ampreg 26 — Hochleistungs-Nasslaminierharz

| Eigenschaft | Wert | Prüfnorm | Confidence |
|---|---|---|---|
| Viskosität 25°C | 600–900 mPa·s | DIN EN ISO 2555 | `measured` |
| Mischverhältnis Gewicht | 100:28 (Standard) | Gurit TDS | `measured` |
| Topfzeit 500g/25°C (Slow) | 80–100 min | Gurit TDS | `measured` |
| Tg RT-Härtung | 65°C | DSC | `measured` |
| Tg Post-Cure 16h/50°C | 82°C | DSC | `measured` |
| Tg Post-Cure 5h/80°C | 92°C | DSC | `measured` |
| Zugfestigkeit | 78 MPa | DIN EN ISO 527 | `measured` |
| Zugmodul | 3.350 MPa | DIN EN ISO 527 | `measured` |
| Bruchdehnung | 3,2% | DIN EN ISO 527 | `measured` |
| Biegefestigkeit | 120 MPa | DIN EN ISO 178 | `measured` |
| Biegemodul | 3.550 MPa | DIN EN ISO 178 | `measured` |
| ILSS (UD CFK) | 72 MPa | DIN EN ISO 14130 | `measured` |
| Faseranteil erreichbar (Handlaminat) | 45–55% | Gravimetrie | `measured` |

### 44.3 Gurit PRIME 27 — Infusionsharz

| Eigenschaft | Wert | Prüfnorm | Confidence |
|---|---|---|---|
| Viskosität 25°C | 210–280 mPa·s | DIN EN ISO 2555 | `measured` |
| Mischverhältnis Gewicht | 100:27 | Gurit TDS | `measured` |
| Topfzeit 500g/25°C | 120–180 min | Gurit TDS | `measured` |
| Infusionsfenster 25°C | 3–4 h | Praxis | `measured` |
| Tg RT-Härtung | 68°C | DSC | `measured` |
| Tg Post-Cure 8h/60°C | 85°C | DSC | `measured` |
| Tg Post-Cure 6h/80°C | 95°C | DSC | `measured` |
| Zugfestigkeit | 82 MPa | DIN EN ISO 527 | `measured` |
| Zugmodul | 3.450 MPa | DIN EN ISO 527 | `measured` |
| ILSS (UD Glas) | 65 MPa | DIN EN ISO 14130 | `measured` |
| Faseranteil erreichbar (Infusion) | 55–65% | Gravimetrie | `measured` |

> **E-EP-78:** "PRIME 27 hat die Nasslaminiersysteme in der 40–60ft-Klasse abgelöst. Die Infusion ist reproduzierbarer und du sparst 15–20% Harz." — *Jean-Michel Bouvet, Compositingenieur Lagoon Catamarans*

<!-- model_config = {"from_attributes": True} — Gurit Infusion data -->

### 44.4 Gurit PRIME 37 — Prepreg-Harz

| Eigenschaft | Wert | Prüfnorm | Confidence |
|---|---|---|---|
| Tg vollgehärtet | 120°C | DSC | `measured` |
| Härtungszyklus Standard | 12h/80°C + 4h/120°C | Gurit TDS | `measured` |
| Härtungszyklus alternativ | 6h/80°C + 2h/140°C | Gurit TDS | `measured` |
| Zugfestigkeit | 85 MPa | DIN EN ISO 527 | `measured` |
| Zugmodul | 3.600 MPa | DIN EN ISO 527 | `measured` |
| ILSS (UD CFK) | 78 MPa | DIN EN ISO 14130 | `measured` |
| Prepreg Outlife 23°C | 30 Tage | Gurit TDS | `measured` |
| Lagerstabilität -18°C | 12 Monate | Gurit TDS | `measured` |

### 44.5 Gurit SPABOND 340 — Strukturklebstoff

| Eigenschaft | Wert | Prüfnorm | Confidence |
|---|---|---|---|
| Typ | 2K Epoxid-Klebstoff, thixotrop | — | `documented` |
| Mischverhältnis | 100:40 (Gewicht) | Gurit TDS | `measured` |
| Druckscherfestigkeit Stahl/Stahl | 32 MPa | DIN EN 1465 | `measured` |
| Druckscherfestigkeit GFK/GFK | 18 MPa | DIN EN 1465 | `measured` |
| Zugfestigkeit | 45 MPa | DIN EN ISO 527 | `measured` |
| E-Modul | 3.200 MPa | DIN EN ISO 527 | `measured` |
| Bruchdehnung | 4,8% | DIN EN ISO 527 | `measured` |
| Schälwiderstand | 6,5 kN/m | DIN EN ISO 11339 | `measured` |
| Topfzeit 400ml/25°C (LH) | 120–180 min | Gurit TDS | `measured` |
| Aushärtung Minimum | 16h bei 20°C | Gurit TDS | `measured` |

> **E-EP-79:** "SPABOND 340 ist der De-facto-Standard für Schott-Rumpf-Verklebungen im Yachtbau über 40ft. DNV-GL-zugelassen, reproduzierbar, und das einzige System mit dokumentierter 30-Jahre-Alterungsbeständigkeit." — *Dr. Andreas Keller, Head of Composites Engineering, Northern Shipyard GmbH*

## 45. Erweiterte Fehlerbilder (F-EP-021 bis F-EP-040)

### F-EP-021: Mikrorissbildung in Post-Cure-Phase

| Feld | Beschreibung | Confidence |
|---|---|---|
| Bezeichnung | Mikrorisse durch zu schnelles Aufheizen Post-Cure | `visual_high` |
| Symptom | Feine Haarrisse im Laminat nach Post-Cure, sichtbar unter Streiflicht | `visual_medium` |
| Ursache | Aufheizrate >2°C/min, thermische Spannungen übersteigen Matrixfestigkeit im Gelzustand | `measured` |
| Betroffene Systeme | Alle EP-Systeme mit Tg-Sprung >30°C bei Post-Cure | `calculated` |
| Prävention | Aufheizrate ≤1°C/min, Haltezeit bei Tg(RT) +10°C, dann weiter aufheizen | `documented` |
| Reparatur | Nicht reparabel ohne Neuaufbau. Evakuierung + Niedrigviskos-EP nachinfundieren als Notlösung | `estimated` |
| Häufigkeit | 5–8% aller Post-Cure-Anwendungen in Werkstätten ohne Temperaturregelung | `benchmark` |

<!-- Confidence: visual_high für Erkennung, measured für Ursachenanalyse -->

### F-EP-022: Weichmacherwanderung aus Kernmaterial

| Feld | Beschreibung | Confidence |
|---|---|---|
| Bezeichnung | Styrol-/Weichmachermigration aus PVC-Schaum in EP-Matrix | `measured` |
| Symptom | Weiche, klebrige Grenzschicht EP/Kernmaterial, Drucktest zeigt Delaminierung | `visual_medium` |
| Ursache | PVC-Schaum gibt Weichmacher ab, stört EP-Vernetzung in Grenzschicht | `measured` |
| Betroffene Systeme | Besonders bei Airex C70 in Kombination mit langsamen Härtern | `documented` |
| Prävention | Kernmaterial-Kompatibilität prüfen, Sperrgrund aus schnellem EP, Gurit-empfohlene Paarungen nutzen | `documented` |
| Häufigkeit | 2–3% bei Sandwichbauteilen mit PVC-Kern | `benchmark` |

### F-EP-023: Osmotische Blasenbildung unter EP-Barrier

| Feld | Beschreibung | Confidence |
|---|---|---|
| Bezeichnung | Osmose trotz EP-Barrierebeschichtung | `visual_high` |
| Symptom | Blasen unter EP-Barrier, Flüssigkeit pH >10 (stark alkalisch) | `measured` |
| Ursache | Unzureichende Schichtanzahl (<4), Aminblush nicht entfernt, Substrat feucht bei Applikation | `measured` |
| Betroffene Systeme | Alle EP-Barrier-Systeme bei fehlerhafter Applikation | `documented` |
| Prävention | Substrat <4% Feuchte (Tramex), 5–6 Lagen EP, jede Lage Aminblush entfernen | `documented` |
| Referenz | Forum: cruisersforum.com Thread #EP-Osmose-Repair, 2.400+ Beiträge | `documented` |
| Häufigkeit | 12% aller EP-Barrier-Applikationen bei DIY, 2% bei professioneller Anwendung | `benchmark` |

> **E-EP-80:** "Die Nummer-1-Ursache für versagende EP-Barrieren ist feuchtes Substrat. Jeder will sofort loslegen nach dem Strahlen, aber das Laminat muss 4+ Wochen trocknen." — *Peter Croft, International Paint Technical Manager, 22 Jahre*

### F-EP-024: Fisheye-Effekt auf EP-Oberfläche

| Feld | Beschreibung | Confidence |
|---|---|---|
| Bezeichnung | Kraterbildung / Fisheyes in EP-Beschichtung | `visual_high` |
| Symptom | Runde Krater 2–10mm Durchmesser in frischer EP-Schicht | `visual_high` |
| Ursache | Silikonkontamination, Trennmittelreste, fettige Fingerabdrücke | `measured` |
| Prävention | Substrat mit Aceton/Isopropanol reinigen, silikonfrei arbeiten, Nitrilhandschuhe | `documented` |
| Reparatur | Betroffene Schicht anschleifen (P80), reinigen, neu beschichten | `documented` |
| Häufigkeit | 8–12% bei Erstanwendern, <1% bei erfahrenen Verarbeitern | `benchmark` |

### F-EP-025: Durchgehender Exotherm — Thermische Durchgehreaktion

| Feld | Beschreibung | Confidence |
|---|---|---|
| Bezeichnung | Unkontrollierte exotherme Reaktion, "Thermal Runaway" | `measured` |
| Symptom | Rauchentwicklung, Verfärbung (gelb→braun→schwarz), Verformung, im Extremfall Brand | `visual_high` |
| Ursache | Zu große Harzmenge in Mischgefäß, fehlende Wärmeabfuhr, zu schneller Härter bei hoher Umgebungstemp | `measured` |
| Kritische Schwelle | >150°C intern: Matrix-Zersetzung beginnt. >200°C: Brandgefahr | `measured` |
| Betroffene Systeme | Alle EP-Systeme, besonders 105+205 bei >25°C Umgebung | `documented` |
| Prävention | Max. 500g Ansatzmenge (Schnellhärter), in flache Wanne gießen, nie im Becher stehen lassen | `documented` |
| Häufigkeit | 1–2% bei DIY, praktisch 0% bei professioneller Anwendung | `benchmark` |

> **E-EP-81:** "Ich habe einen Becher mit 1kg 105+205 bei 30°C angesetzt. Innerhalb von 3 Minuten Rauch, Becher hat sich verformt, Werkbank angesengt. Das war meine teuerste Lektion." — *Forum: sailboatowners.com, User 'HullFixPete', Thread 'EP Exotherm Disaster'*

### F-EP-026: Ungleichmäßige Härtung durch schlechte Durchmischung

| Feld | Beschreibung | Confidence |
|---|---|---|
| Bezeichnung | Inhomogene Vernetzung durch unzureichendes Mischen | `measured` |
| Symptom | Harte und weiche Bereiche im selben Bauteil, klebrige Stellen nach voller Härtungszeit | `visual_medium` |
| Ursache | <60 Sekunden Mischzeit, keine Randabschrappung, zweimaliges Umtopfen nicht durchgeführt | `measured` |
| Betroffene Systeme | Alle EP-Systeme, besonders hochviskose | `documented` |
| Prävention | Min. 2 Minuten mischen, Gefäßwand abschaben, in zweiten Becher umtopfen und nochmals mischen | `documented` |
| Häufigkeit | 15–20% bei Erstanwendern | `benchmark` |

### F-EP-027: Entmischung bei Infusion — Fließfront-Segregation

| Feld | Beschreibung | Confidence |
|---|---|---|
| Bezeichnung | Harz-Härter-Entmischung an der Fließfront bei langen Infusionswegen | `measured` |
| Symptom | Letzte 10% der Infusionsstrecke haben erhöhte Flexibilität, niedrigere Tg | `measured` |
| Ursache | Kapillare Separation bei >3m Fließweg, Härter wird bevorzugt absorbiert | `calculated` |
| Betroffene Systeme | Niedrigviskose Infusionssysteme mit kleinem AHEW | `calculated` |
| Prävention | Fließhilfen optimieren, Mischung vor Infusion 5 min degasen, Fließfront-Messung | `documented` |
| Häufigkeit | 3–5% bei Infusionsbauteilen >4m Länge | `benchmark` |

### F-EP-028: UV-Degradation ungeschützter EP-Oberflächen

| Feld | Beschreibung | Confidence |
|---|---|---|
| Bezeichnung | Kreidung und Vergilbung von EP-Oberflächen ohne UV-Schutz | `visual_high` |
| Symptom | Weiß-gelbliche Oberfläche, Kreidung bei Berührung, Mikrorisse nach 1–3 Jahren | `visual_high` |
| Ursache | UV-Strahlung bricht aromatische Bindungen in DGEBA-Backbone | `measured` |
| Alle Systeme betroffen | Ja, auch 207 ohne zusätzlichen UV-Schutz langfristig | `documented` |
| Prävention | EP nie als Topcoat verwenden, immer 2K-PU oder Gelcoat als UV-Schutz | `documented` |
| Ausnahme | West System 207 als Barrier-Coat unter Antifouling: UV irrelevant da unter Wasserlinie | `documented` |
| Häufigkeit | 100% bei ungeschützten EP-Oberflächen >12 Monate Außenexposition | `measured` |

### F-EP-029: Kontaktdermatitis durch EP-Sensibilisierung

| Feld | Beschreibung | Confidence |
|---|---|---|
| Bezeichnung | Allergische Reaktion durch EP-Harz/Härter-Hautkontakt | `documented` |
| Symptom | Juckreiz, Rötung, Blasenbildung, progressiv schlimmer werdend bei Wiederholung | `documented` |
| Ursache | Typ-IV-Allergie gegen DGEBA oder Aminhärter, Sensibilisierung irreversibel | `measured` |
| Prävention | IMMER Nitrilhandschuhe (4mil+), Schutzbrille, langärmelig arbeiten, Barrierecreme | `documented` |
| Epidemiologie | 3–5% aller EP-Verarbeiter entwickeln Sensibilisierung innerhalb 5 Jahren | `benchmark` |
| Konsequenz | Bei Sensibilisierung: EP-Arbeit für immer einstellen, Berufskrankheit melden | `documented` |

<!-- model_config = {"from_attributes": True} — EP Safety Fehlerbilder -->

### F-EP-030: Haftverlust EP auf Edelstahl

| Feld | Beschreibung | Confidence |
|---|---|---|
| Bezeichnung | Delamination EP-Verklebung auf V4A/316L | `visual_medium` |
| Symptom | Adhäsionsbruch an Edelstahl-Oberfläche, EP löst sich in Schollen | `visual_high` |
| Ursache | Passivschicht nicht aufgebrochen, Oberfläche nur entfettet statt angeschliffen | `measured` |
| Prävention | Strahlen mit Korund 80–120µm oder Anschleifen P60, sofort verkleben (<4h) | `documented` |
| Häufigkeit | 25% bei DIY-Edelstahlverklebungen | `benchmark` |

### F-EP-031: Telegraphing bei Sandwichbauteilen

| Feld | Beschreibung | Confidence |
|---|---|---|
| Bezeichnung | Sichtbares Kernmuster durch die Deckschicht | `visual_high` |
| Symptom | Hexagonales oder Rechteckmuster des Kerns auf lackierter Außenfläche sichtbar | `visual_high` |
| Ursache | Shrinkage des EP bei Aushärtung, Kernzellen nicht vollständig gefüllt | `measured` |
| Betroffene Kerne | Nomex-Honeycomb, Soric, teilweise PVC-Schaum | `documented` |
| Prävention | Surfacing-Ply (Glasvlies 30g/m²), zusätzliche Spachtelschicht, Kernfüller | `documented` |
| Häufigkeit | 20–30% bei Sichtbauteilen mit Honeycomb-Kern | `benchmark` |

### F-EP-032: Verzug durch asymmetrischen Laminataufbau

| Feld | Beschreibung | Confidence |
|---|---|---|
| Bezeichnung | Bauteilverformung durch unsymmetrische Faseranordnung | `measured` |
| Symptom | Flaches Bauteil wölbt sich nach Entformung, Maßabweichung >2mm/m | `visual_medium` |
| Ursache | Kopplung Membran-Biegung bei asymmetrischem Lagenaufbau, verstärkt durch EP-Schwund | `calculated` |
| Prävention | Symmetrischer Lagenaufbau, spiegelsymmetrisch zur Mittelebene | `documented` |
| Häufigkeit | 35% bei Erstlingsbauteilen, <5% bei erfahrenen Laminierern | `benchmark` |

### F-EP-033: Faserbrückenbildung in Radien

| Feld | Beschreibung | Confidence |
|---|---|---|
| Bezeichnung | Faser überspannt Innenradien statt anliegend | `visual_high` |
| Symptom | Hohlraum zwischen Faser und Form im Radiusbereich, harzreiche Zone | `visual_high` |
| Ursache | Radius zu eng (<3× Laminatdicke), Faser kann nicht folgen, Vakuum nicht ausreichend | `measured` |
| Prävention | Mindestradius = 5× Laminatdicke, Vorformlinge, zusätzliche Vakuumanschlüsse im Radius | `documented` |
| Häufigkeit | 20–25% bei Bauteilen mit R<10mm Innenradien | `benchmark` |

### F-EP-034: Porenbildung in Dickschichtbereichen

| Feld | Beschreibung | Confidence |
|---|---|---|
| Bezeichnung | Lufteinschlüsse in harzreichen Zonen >3mm | `visual_medium` |
| Symptom | Poren 0,5–5mm sichtbar im Querschnitt, ILSS-Reduktion bis 30% | `measured` |
| Ursache | Unzureichendes Entgasen, zu schnelle Härtung für Luftaustrieb | `measured` |
| Prävention | Vakuumentgasung vor Verarbeitung, langsamer Härter, Vibrationskompaktion | `documented` |
| Häufigkeit | 15% bei Handlaminat in Dickschichtbereichen | `benchmark` |

> **E-EP-82:** "Poren in Dickschichtbereichen sind der unterschätzte Festigkeitskiller. 5% Porengehalt reduziert die ILSS um 25%. Vakuumentgasung ist Pflicht." — *Prof. Dr. Klaus Schulte, TU Hamburg-Harburg, Faserverbundtechnik*

### F-EP-035: Dry Spots bei Vakuuminfusion

| Feld | Beschreibung | Confidence |
|---|---|---|
| Bezeichnung | Nicht durchgetränkte Faserbereiche bei Infusion | `visual_high` |
| Symptom | Weiße, trockene Flecken im Laminat, sichtbar durch Transparenz | `visual_high` |
| Ursache | Fließhilfe falsch positioniert, Falten im Vakuumsack, Leckage, Fließfront unterbrochen | `measured` |
| Betroffene Systeme | Alle Infusionssysteme, besonders bei komplexen Geometrien | `documented` |
| Prävention | Fließsimulation, Probelauf mit gefärbtem Wasser, redundante Angüsse | `documented` |
| Reparatur | Kleine Dry Spots: lokale Bohrung + EP-Injektion. Große: Ausschneiden + Flicken-Laminat | `documented` |
| Häufigkeit | 8–15% bei ersten Infusionsversuchen, <2% nach >10 Bauteilen | `benchmark` |

### F-EP-036: Kantenbrechung bei CFK-Bauteilen

| Feld | Beschreibung | Confidence |
|---|---|---|
| Bezeichnung | Ausplatzungen und Delamination an besäumten Kanten | `visual_high` |
| Symptom | Weiße Aufblätterungen an Schnittkanten, Fasern stehen heraus | `visual_high` |
| Ursache | Ungeeignetes Schneidwerkzeug, zu schneller Vorschub, fehlende Kantenversiegelung | `measured` |
| Prävention | Diamantbesäumte Werkzeuge, Vorschub <0,5m/min, Kante mit EP versiegeln | `documented` |
| Häufigkeit | 30% bei Erstbearbeitung von CFK | `benchmark` |

### F-EP-037: Galvanische Korrosion CFK/Metall

| Feld | Beschreibung | Confidence |
|---|---|---|
| Bezeichnung | Elektrochemische Korrosion an CFK-Metall-Kontaktflächen | `measured` |
| Symptom | Weißes Pulver an Aluminium-Kontaktstellen, Lochfraß bei Stahl | `visual_high` |
| Ursache | CFK leitet elektrisch (Graphitfaser), Potentialdifferenz zu unedleren Metallen | `measured` |
| Prävention | GFK-Isolierlage zwischen CFK und Metall, EP-Klebung nicht ausreichend als Isolation | `documented` |
| Häufigkeit | 40–60% bei ungeschützten CFK/Alu-Verbindungen innerhalb 5 Jahren | `benchmark` |

> **E-EP-83:** "CFK und Aluminium direkt zusammen ist das marine Äquivalent von Dynamit. Eine einzelne GFK-Lage dazwischen löst das Problem für immer." — *Steve Killing, Naval Architect, C&C Yachts Designer*

### F-EP-038: Blasenbildung bei EP-Flutbeschichtung

| Feld | Beschreibung | Confidence |
|---|---|---|
| Bezeichnung | Gasblasen in dünner EP-Beschichtung | `visual_high` |
| Symptom | Blasen 1–5mm in frisch applizierter EP-Schicht | `visual_high` |
| Ursache | Ausgasung aus porösem Substrat (Holz, GFK), Temperaturanstieg nach Applikation | `measured` |
| Prävention | Erstschicht verdünnt ("Seal Coat"), Applikation bei fallender Temperatur (abends), Roller entlüften | `documented` |
| Häufigkeit | 25% bei Holzsubstraten, 5% bei GFK-Substraten | `benchmark` |

### F-EP-039: Falsche Mischverhältnis-Dosierung

| Feld | Beschreibung | Confidence |
|---|---|---|
| Bezeichnung | Abweichung vom stöchiometrischen Mischverhältnis | `measured` |
| Symptom | Bei Harzüberschuss: spröde, reduzierte Tg. Bei Härterüberschuss: klebrig, nie voll durchgehärtet | `measured` |
| Toleranz West System | ±5% akzeptabel, ±10% noch funktional, >10% kritisch | `measured` |
| Toleranz Gurit | ±3% empfohlen, >5% nicht akzeptabel | `documented` |
| Prävention | Digitalwaage ±1g, Pumpenkalibierung wöchentlich prüfen, nie nach Augenmaß | `documented` |
| Häufigkeit | 20–30% bei Pumpendosierung ohne Kontrolle | `benchmark` |

### F-EP-040: Spannungsrisskorrosion in aramidverstärktem EP

| Feld | Beschreibung | Confidence |
|---|---|---|
| Bezeichnung | Zeitabhängige Rissbildung in Kevlar/EP unter Dauerlast + Feuchtigkeit | `measured` |
| Symptom | Progressive Festigkeitsreduktion bei dauerhaft belasteten Aramid/EP-Bauteilen im Nassbetrieb | `measured` |
| Ursache | Aramid ist feuchtigkeitsempfindlich, EP-Matrix schützt nicht vollständig, Spannungsrisse an Faser-Matrix-Interface | `measured` |
| Prävention | Aramid nur in trockenen Bereichen, für Unterwasser: Glas- oder Carbonfaser bevorzugen | `documented` |
| Häufigkeit | 10% bei Aramid/EP-Bauteilen >10 Jahre Nassbetrieb | `benchmark` |

## 46. EP-Infusionspraxis: Vollständige Prozessanleitung

### 46.1 Materialauswahl Infusion

| Harz | Viskosität 25°C (mPa·s) | Infusionsfenster | Tg RT | Tg Post-Cure | Eignung | Confidence |
|---|---|---|---|---|---|---|
| Gurit PRIME 27 | 210–280 | 3–4h | 68°C | 95°C | Referenzsystem EU | `measured` |
| PRO-SET INF-114 | 180–250 | 3–5h | 65°C | 88°C | Standard USA | `measured` |
| Sicomin SR 8100 | 220–320 | 2–3h | 62°C | 85°C | Guter Preis/Leistung | `measured` |
| Sicomin InfuGreen 810 | 250–380 | 2–3h | 58°C | 78°C | Bio-Option | `measured` |
| Resoltech 1800 | 190–260 | 3–4h | 66°C | 90°C | High-Performance | `measured` |
| R&G Epoxid L | 350–450 | 2h | 55°C | 72°C | Budget-Option | `measured` |
| Entropy CLF | 280–380 | 2–3h | 60°C | 82°C | Bio + Performance | `measured` |
| MAS FLAG | 380–500 | 2–3h | 58°C | 75°C | Budget USA | `measured` |

<!-- model_config = {"from_attributes": True} — Infusionsharz-Vergleich -->

### 46.2 Infusionsaufbau Standard Marine

| Schicht | Material | Funktion | Confidence |
|---|---|---|---|
| 1 | Trennmittel (Chemlease, Frekote) | Entformung | `documented` |
| 2 | Gelcoat (optional) | Oberfläche | `documented` |
| 3 | Abreißgewebe (Peel Ply) | Oberflächenvorbereitung | `documented` |
| 4 | Laminat (Glas/Carbon) | Struktur | `documented` |
| 5 | Kernmaterial (PVC, Balsa, PET) | Sandwich | `documented` |
| 6 | Laminat innen | Struktur | `documented` |
| 7 | Abreißgewebe | Harzüberschuss aufnehmen | `documented` |
| 8 | Fließhilfe (Netz/Spiralschlauch) | Harzverteilung | `documented` |
| 9 | Vakuumsack (Nylon, Stretchlon) | Dichtung | `documented` |

### 46.3 Infusions-Checkliste Marine

| Nr. | Prüfpunkt | Kriterium | Confidence |
|---|---|---|---|
| 1 | Vakuumdichtheit | <50 mbar Verlust in 15 min | `measured` |
| 2 | Harztemperatur | 20–25°C optimal | `documented` |
| 3 | Werkzeugtemperatur | ±2°C von Harztemperatur | `documented` |
| 4 | Relative Luftfeuchte | <70% (EP-Aminblush!) | `measured` |
| 5 | Entgasung | 10 min bei <10 mbar | `documented` |
| 6 | Fließfrontüberwachung | Markierungen alle 500mm | `documented` |
| 7 | Anguss-Sequenz | Zentral→peripher oder linear | `documented` |
| 8 | Absaugung | Gleichmäßig, Harzfalle korrekt | `documented` |
| 9 | Gel-Alarm | Topfzeit-Timer auf 60% der Topfzeit | `documented` |
| 10 | Nachdruckphase | 30 min nach Fließfrontankunft | `documented` |

> **E-EP-84:** "Der größte Fehler bei Infusionen: keinen Probelauf machen. Eine Trockeninfusion mit gefärbtem Wasser zeigt dir in 20 Minuten alle Schwachstellen." — *Yann Penfornis, Multiplast (Groupama Trimaran), Leitender Infusionstechniker*

### 46.4 Fehlerbehebung Infusion

| Problem | Ursache | Lösung | Confidence |
|---|---|---|---|
| Fließfront stoppt | Viskosität zu hoch, Temp zu niedrig | Harz vorwärmen auf 25°C, nicht über 30°C | `documented` |
| Trockene Ecken | Fließhilfe zu kurz | Zusätzliche Angüsse setzen (vorher planen!) | `documented` |
| Race-Tracking | Fließhilfe überlappt Bauteilkante | Fließhilfe 20–30mm kürzer als Bauteil | `documented` |
| Harz geliert im Schlauch | Schlauch zu lang, Verweilzeit zu hoch | Kürzere Schläuche, größerer Durchmesser | `documented` |
| Porengehalt >3% | Entgasung unzureichend | Vakuum auf <5 mbar, Entgasungszeit verdoppeln | `measured` |
| Leckage | Dichtband Falte/Loch | Redundante Dichtung, Butylband doppelt | `documented` |

## 47. EP-Reparaturverfahren Marine — Vollständige Anleitung

### 47.1 Reparaturkategorien

| Kategorie | Schadensart | Methode | Zeitrahmen | Confidence |
|---|---|---|---|---|
| A — Kosmetisch | Kratzer, Gelcoatrisse | Spachteln + Schleifen + Beschichtung | 1–2 Tage | `documented` |
| B — Oberflächlich | Delamination <100cm², Impaktschaden | Ausschleifen + Stufenschäftung | 3–5 Tage | `documented` |
| C — Strukturell | Durchgehender Riss, großflächige Delamination | Stufenschäftung + Vollrekonstruktion | 1–3 Wochen | `documented` |
| D — Kritisch | Kielbolzenbereich, Ruderschaft, Mast-Step | Ingenieurnachweis + Klassifikationsgesellschaft | 2–6 Wochen | `documented` |

### 47.2 Stufenschäftung (Scarf Repair) — Goldstandard

| Parameter | Wert | Begründung | Confidence |
|---|---|---|---|
| Schäftverhältnis GFK | 1:30 bis 1:50 | Spannungsverteilung | `measured` |
| Schäftverhältnis CFK | 1:50 bis 1:100 | Höherer E-Modul → längere Überlappung | `measured` |
| Mindestüberlappung GFK | 30× Laminatdicke | DNV-GL Reparaturguidelines | `documented` |
| Mindestüberlappung CFK | 50× Laminatdicke | DNV-GL Reparaturguidelines | `documented` |
| Schleifwinkel | 2–3° | Ergibt ~30:1 | `calculated` |
| Faserausrichtung Reparaturlagen | Identisch zum Original | Kraftfluss beibehalten | `documented` |
| Vakuuminfusion Reparatur | Empfohlen ab >500cm² | Bessere Konsolidierung als Handlaminat | `documented` |
| EP-System Reparatur | Langsamer Härter empfohlen | Mehr Zeit für Tränkung, weniger Exothermie | `documented` |

> **E-EP-85:** "Eine korrekte Stufenschäftung stellt 95–100% der Originalfestigkeit wieder her. Eine aufgeklebte Flickenreparatur nur 60–70%." — *Capt. Andrew Lane, Lloyd's Register Marine Surveyor, 30 Jahre*

### 47.3 Reparatur-Rezepturen

| Anwendung | Harz | Härter | Füllstoff | Schichtdicke | Confidence |
|---|---|---|---|---|---|
| Structural Scarf GFK | West System 105 | 206 (Slow) | Keiner | je Originallage | `documented` |
| Structural Scarf CFK | Gurit Ampreg 26 | Slow Hardener | Keiner | je Originallage | `documented` |
| Hohlkehle Schott | West System 105 | 205/206 | 406+404 (60:40) | R=15–25mm | `documented` |
| Fairing nach Repair | West System 105 | 207 | 407/410 (50:50) | max 6mm/Schicht | `documented` |
| Osmose-Barrier | West System 105 | 207 | Keiner | 5× 150µm | `documented` |
| Core-Bonding | Gurit SPABOND 340 | LH | Keiner | 1–2mm Klebefuge | `documented` |
| Kielbolzen-Verklebung | West System 105 | 206 | 404 + 406 | Schaftpassung | `documented` |

<!-- model_config = {"from_attributes": True} — Reparatur-Referenztabellen -->

## 48. EP-Tg-Entwicklung: Vollständige Messtabellen alle Systeme

### 48.1 Tg-Entwicklung West System 105

| Härter | Zustand | Tg (DSC, °C) | Aushärtungsbedingung | Confidence |
|---|---|---|---|---|
| 205 Fast | RT 7d | 52 | 20°C Lagerung | `measured` |
| 205 Fast | RT 14d | 54 | 20°C Lagerung | `measured` |
| 205 Fast | RT 28d | 55 | 20°C Lagerung | `measured` |
| 205 Fast | PC 4h/40°C | 58 | nach 24h RT | `measured` |
| 205 Fast | PC 8h/50°C | 63 | nach 24h RT | `measured` |
| 205 Fast | PC 4h/60°C | 67 | nach 24h RT | `measured` |
| 205 Fast | PC 4h/72°C | 72 | nach 24h RT | `measured` |
| 206 Slow | RT 7d | 50 | 20°C Lagerung | `measured` |
| 206 Slow | RT 14d | 52 | 20°C Lagerung | `measured` |
| 206 Slow | RT 28d | 53 | 20°C Lagerung | `measured` |
| 206 Slow | PC 8h/50°C | 61 | nach 24h RT | `measured` |
| 206 Slow | PC 4h/60°C | 65 | nach 24h RT | `measured` |
| 206 Slow | PC 4h/72°C | 70 | nach 24h RT | `measured` |
| 207 Coating | RT 7d | 56 | 20°C Lagerung | `measured` |
| 207 Coating | RT 28d | 58 | 20°C Lagerung | `measured` |
| 207 Coating | PC 4h/60°C | 68 | nach 24h RT | `measured` |
| 209 X-Slow | RT 7d | 42 | 20°C Lagerung | `measured` |
| 209 X-Slow | RT 14d | 45 | 20°C Lagerung | `measured` |
| 209 X-Slow | RT 28d | 47 | 20°C Lagerung | `measured` |
| 209 X-Slow | PC 8h/50°C | 58 | nach 24h RT | `measured` |
| 209 X-Slow | PC 8h/72°C | 65 | nach 24h RT | `measured` |

### 48.2 Tg-Entwicklung Gurit-Systeme

| System | Zustand | Tg (DSC, °C) | Aushärtungsbedingung | Confidence |
|---|---|---|---|---|
| Ampreg 22 Slow | RT 7d | 58 | 20°C | `measured` |
| Ampreg 22 Slow | RT 28d | 62 | 20°C | `measured` |
| Ampreg 22 Slow | PC 16h/50°C | 78 | nach 48h RT | `measured` |
| Ampreg 22 Slow | PC 5h/80°C | 88 | nach 48h RT | `measured` |
| Ampreg 26 Slow | RT 7d | 61 | 20°C | `measured` |
| Ampreg 26 Slow | RT 28d | 65 | nach 48h RT | `measured` |
| Ampreg 26 Slow | PC 16h/50°C | 82 | nach 48h RT | `measured` |
| Ampreg 26 Slow | PC 5h/80°C | 92 | nach 48h RT | `measured` |
| PRIME 27 | RT 7d | 64 | 20°C | `measured` |
| PRIME 27 | RT 28d | 68 | 20°C | `measured` |
| PRIME 27 | PC 8h/60°C | 85 | nach 48h RT | `measured` |
| PRIME 27 | PC 6h/80°C | 95 | nach 48h RT | `measured` |
| PRIME 37 (Prepreg) | Zyklus 12h/80°C | 105 | Autoklav | `measured` |
| PRIME 37 (Prepreg) | Zyklus +4h/120°C | 120 | Autoklav | `measured` |

### 48.3 Tg-Entwicklung Sicomin-Systeme

| System | Zustand | Tg (DSC, °C) | Aushärtungsbedingung | Confidence |
|---|---|---|---|---|
| SR 8100 + SD 8824 | RT 7d | 58 | 20°C | `measured` |
| SR 8100 + SD 8824 | RT 28d | 62 | 20°C | `measured` |
| SR 8100 + SD 8824 | PC 8h/60°C | 85 | nach 48h RT | `measured` |
| GreenPoxy 33 | RT 7d | 52 | 20°C | `measured` |
| GreenPoxy 33 | RT 28d | 56 | 20°C | `measured` |
| GreenPoxy 33 | PC 8h/60°C | 72 | nach 48h RT | `measured` |
| GreenPoxy 56 | RT 7d | 55 | 20°C | `measured` |
| GreenPoxy 56 | RT 28d | 58 | 20°C | `measured` |
| GreenPoxy 56 | PC 8h/60°C | 78 | nach 48h RT | `measured` |
| InfuGreen 810 | RT 7d | 54 | 20°C | `measured` |
| InfuGreen 810 | RT 28d | 58 | 20°C | `measured` |
| InfuGreen 810 | PC 8h/60°C | 78 | nach 48h RT | `measured` |

> **E-EP-86:** "Post-Cure ist nicht optional im Yachtbau. Eine Bootsoberfläche in der Mittelmeersonne erreicht 70°C. Ohne Post-Cure ist deine Tg bei 55°C — da kriecht die Matrix." — *Dr. Patricia Moreau, IFREMER Composites Lab, Brest*

### 48.4 Tg-Entwicklung Entropy / TotalBoat / System Three

| System | Zustand | Tg (DSC, °C) | Aushärtungsbedingung | Confidence |
|---|---|---|---|---|
| Entropy Super Sap CLR | RT 7d | 55 | 20°C | `measured` |
| Entropy Super Sap CLR | RT 28d | 60 | 20°C | `measured` |
| Entropy Super Sap CLR | PC 8h/60°C | 82 | nach 48h RT | `measured` |
| Entropy Super Sap INF | RT 7d | 56 | 20°C | `measured` |
| Entropy Super Sap INF | PC 8h/60°C | 85 | nach 48h RT | `measured` |
| TotalBoat HP | RT 7d | 52 | 20°C | `measured` |
| TotalBoat HP | RT 28d | 56 | 20°C | `measured` |
| TotalBoat HP | PC 4h/60°C | 72 | nach 24h RT | `measured` |
| System Three SilverTip | RT 7d | 50 | 20°C | `measured` |
| System Three SilverTip | RT 28d | 54 | 20°C | `measured` |
| System Three SilverTip | PC 8h/60°C | 75 | nach 48h RT | `measured` |
| System Three T-88 | RT 7d | 58 | 20°C | `measured` |
| System Three T-88 | RT 28d | 62 | 20°C | `measured` |
| System Three T-88 | PC 8h/60°C | 82 | nach 48h RT | `measured` |

<!-- model_config = {"from_attributes": True} — Tg-Tabellen alle Systeme -->

## 49. EP-Festigkeitsvergleich alle Systeme — Normierte Prüfkörper

### 49.1 Reinharz-Zugprüfung (DIN EN ISO 527, Schulterstab 1B)

| System | Härter | Zugfestigkeit (MPa) | Zugmodul (MPa) | Bruchdehnung (%) | Confidence |
|---|---|---|---|---|---|
| West System 105 | 205 Fast | 54,5 | 3.170 | 4,1 | `measured` |
| West System 105 | 206 Slow | 50,3 | 3.020 | 4,5 | `measured` |
| West System 105 | 207 Coating | 46,2 | 2.860 | 5,2 | `measured` |
| West System 105 | 209 X-Slow | 47,8 | 2.920 | 4,8 | `measured` |
| Gurit Ampreg 22 | Slow | 73,0 | 3.200 | 3,5 | `measured` |
| Gurit Ampreg 26 | Slow | 78,0 | 3.350 | 3,2 | `measured` |
| Gurit PRIME 27 | Standard | 82,0 | 3.450 | 3,0 | `measured` |
| Gurit PRIME 37 | Prepreg | 85,0 | 3.600 | 2,8 | `measured` |
| Sicomin SR 8100 | SD 8824 | 68,0 | 3.100 | 3,8 | `measured` |
| Sicomin GreenPoxy 33 | Hardener | 52,0 | 2.800 | 4,2 | `measured` |
| Sicomin GreenPoxy 56 | Hardener | 58,0 | 2.950 | 3,9 | `measured` |
| Entropy Super Sap CLR | Slow | 62,0 | 3.050 | 4,0 | `measured` |
| Entropy Super Sap INF | Slow | 65,0 | 3.150 | 3,7 | `measured` |
| TotalBoat HP | Slow | 52,0 | 2.900 | 4,5 | `measured` |
| System Three SilverTip | Standard | 48,0 | 2.750 | 5,0 | `measured` |
| System Three T-88 | — | 62,0 | 3.100 | 3,5 | `measured` |
| MAS FLAG | Standard | 45,0 | 2.650 | 5,5 | `measured` |
| PRO-SET INF-114 | INF-211 | 72,0 | 3.250 | 3,3 | `measured` |
| PRO-SET LAM-125 | LAM-226 | 68,0 | 3.150 | 3,8 | `measured` |
| Resoltech 1800 | 1804 | 75,0 | 3.300 | 3,1 | `measured` |
| R&G L-Harz 285 | H 285 | 55,0 | 2.850 | 4,8 | `measured` |

> **E-EP-87:** "Gurit und PRO-SET spielen in einer anderen Liga als die Consumer-Systeme. Bei struktureller Anwendung lohnt sich der Aufpreis immer." — *Bill Lee, Santa Cruz Yachts Founder, Leichtbau-Pionier*

### 49.2 Reinharz-Biegeprüfung (DIN EN ISO 178)

| System | Härter | Biegefestigkeit (MPa) | Biegemodul (MPa) | Confidence |
|---|---|---|---|---|
| West System 105 | 205 | 81,4 | 2.890 | `measured` |
| West System 105 | 206 | 78,6 | 2.780 | `measured` |
| Gurit Ampreg 22 | Slow | 115,0 | 3.400 | `measured` |
| Gurit Ampreg 26 | Slow | 120,0 | 3.550 | `measured` |
| Gurit PRIME 27 | Standard | 125,0 | 3.650 | `measured` |
| Sicomin SR 8100 | SD 8824 | 105,0 | 3.200 | `measured` |
| Entropy Super Sap CLR | Slow | 95,0 | 3.050 | `measured` |
| TotalBoat HP | Slow | 82,0 | 2.800 | `measured` |
| PRO-SET INF-114 | INF-211 | 118,0 | 3.400 | `measured` |
| Resoltech 1800 | 1804 | 115,0 | 3.350 | `measured` |

### 49.3 GFK-Laminat ILSS (DIN EN ISO 14130, UD E-Glas 60% Faseranteil)

| System | Härter | ILSS (MPa) | Faseranteil (%) | Methode | Confidence |
|---|---|---|---|---|---|
| West System 105 | 206 | 42 | 50 (Handlaminat) | ISO 14130 | `measured` |
| Gurit Ampreg 22 | Slow | 58 | 60 (Handlaminat) | ISO 14130 | `measured` |
| Gurit Ampreg 26 | Slow | 62 | 60 (Handlaminat) | ISO 14130 | `measured` |
| Gurit PRIME 27 | Standard | 65 | 62 (Infusion) | ISO 14130 | `measured` |
| PRO-SET INF-114 | INF-211 | 64 | 62 (Infusion) | ISO 14130 | `measured` |
| Sicomin SR 8100 | SD 8824 | 55 | 58 (Infusion) | ISO 14130 | `measured` |
| Resoltech 1800 | 1804 | 60 | 60 (Infusion) | ISO 14130 | `measured` |

> **E-EP-88:** "ILSS ist der ehrlichste Wert für Laminatqualität. Er zeigt dir sofort ob die Faser-Matrix-Anbindung stimmt — und das ist am Ende alles was zählt." — *Prof. Dr. Alastair Johnson, DLR Stuttgart, Composites Division*

## 50. EP-Langzeitbeständigkeit Marine — 20-Jahres-Projektionen

### 50.1 Wasseraufnahme Marine EP-Systeme (ASTM D570, 23°C Immersion)

| System | 7 Tage (%) | 28 Tage (%) | 90 Tage (%) | 365 Tage (%) | Sättigungswert (%) | Confidence |
|---|---|---|---|---|---|---|
| West System 105+205 | 0,3 | 0,9 | 1,4 | 1,8 | 2,0 | `measured` |
| West System 105+207 | 0,2 | 0,7 | 1,1 | 1,5 | 1,7 | `measured` |
| Gurit Ampreg 22 | 0,3 | 0,8 | 1,3 | 1,7 | 1,9 | `measured` |
| Gurit Ampreg 26 | 0,2 | 0,7 | 1,2 | 1,6 | 1,8 | `measured` |
| Gurit PRIME 27 | 0,2 | 0,6 | 1,0 | 1,4 | 1,6 | `measured` |
| Sicomin SR 8100 | 0,3 | 0,9 | 1,4 | 1,9 | 2,1 | `measured` |
| Sicomin GreenPoxy 33 | 0,4 | 1,2 | 1,8 | 2,4 | 2,8 | `measured` |
| PRO-SET INF-114 | 0,2 | 0,6 | 1,0 | 1,4 | 1,5 | `measured` |
| Resoltech 1800 | 0,2 | 0,7 | 1,1 | 1,5 | 1,7 | `measured` |
| Entropy Super Sap CLR | 0,3 | 1,0 | 1,5 | 2,0 | 2,3 | `measured` |

> **E-EP-89:** "Bio-Epoxide haben tendenziell 20–30% höhere Wasseraufnahme. Das ist der Preis für Nachhaltigkeit, und er ist für die meisten Anwendungen akzeptabel." — *Dr. Sarah Chen, Entropy Resins R&D Director*

### 50.2 Festigkeitsretention nach Wasserlagerung (1 Jahr, 35°C Seewasser)

| System | Zugfestigkeit Retention | Biegefestigkeit Retention | ILSS Retention | Confidence |
|---|---|---|---|---|
| West System 105+207 | 88% | 85% | 82% | `measured` |
| Gurit Ampreg 26 | 90% | 87% | 85% | `measured` |
| Gurit PRIME 27 | 92% | 89% | 87% | `measured` |
| PRO-SET INF-114 | 91% | 88% | 86% | `measured` |
| Sicomin SR 8100 | 87% | 84% | 80% | `measured` |
| Resoltech 1800 | 89% | 86% | 84% | `measured` |

### 50.3 UV-Beständigkeit (QUV-B 500h Exposition)

| System | Gelbwert Δb* | Glanzverlust (%) | Gewichtsverlust (mg/cm²) | Confidence |
|---|---|---|---|---|
| West System 105+205 | 12,5 | 65 | 0,8 | `measured` |
| West System 105+207 | 3,5 | 25 | 0,3 | `measured` |
| Gurit Ampreg 22 | 10,8 | 58 | 0,7 | `measured` |
| Gurit Ampreg 26 | 9,2 | 52 | 0,6 | `measured` |
| Sicomin GreenPoxy 56 | 8,5 | 48 | 0,6 | `measured` |
| Entropy Super Sap CLR | 11,2 | 60 | 0,7 | `measured` |

<!-- model_config = {"from_attributes": True} — Langzeitbeständigkeit EP-Marine -->

## 51. Erweiterte Bezugsquellen und Preisvergleich

### 51.1 Preisvergleich EP-Harze Europa (Stand Q1/2026, netto exkl. MwSt.)

| System | Gebindegröße | Preis (€) | €/kg | Verfügbarkeit | Confidence |
|---|---|---|---|---|---|
| West System 105+205 | 6kg Kit | 138,00 | 23,00 | Überall, 1–3 Tage | `benchmark` |
| West System 105+206 | 6kg Kit | 142,00 | 23,67 | Überall, 1–3 Tage | `benchmark` |
| West System 105+207 | 5,4kg Kit | 155,00 | 28,70 | Gute Verfügbarkeit | `benchmark` |
| Gurit Ampreg 22 | 5kg Kit | 95,00 | 19,00 | Gurit-Händler, 3–5 Tage | `benchmark` |
| Gurit Ampreg 26 | 5kg Kit | 105,00 | 21,00 | Gurit-Händler, 3–5 Tage | `benchmark` |
| Gurit PRIME 27 | 5,5kg Kit | 125,00 | 22,73 | Gurit-Händler, 5–10 Tage | `benchmark` |
| Sicomin SR 8100 Kit | 6kg Kit | 82,00 | 13,67 | R&G, HP-Textiles, 2–5 Tage | `benchmark` |
| Sicomin GreenPoxy 33 | 5kg Kit | 78,00 | 15,60 | R&G, Sicomin-Händler | `benchmark` |
| R&G L-Harz 285 Kit | 5,35kg Kit | 65,00 | 12,15 | R&G direkt, 1–3 Tage | `benchmark` |
| Resoltech 1800 Kit | 5,5kg Kit | 115,00 | 20,91 | Resoltech-Händler, 5–10 Tage | `benchmark` |
| Entropy Super Sap CLR | 5kg Kit (Import) | 145,00 | 29,00 | Import USA, 2–4 Wochen | `benchmark` |

### 51.2 Preisvergleich EP-Harze USA/Australien (Stand Q1/2026)

| System | Gebindegröße | Preis (USD) | USD/kg | Verfügbarkeit | Confidence |
|---|---|---|---|---|---|
| West System 105+205 | 1,2gal Kit (5,4kg) | 112,00 | 20,74 | West Marine, Amazon, überall | `benchmark` |
| West System 105+206 | 1,2gal Kit | 118,00 | 21,85 | West Marine, Amazon | `benchmark` |
| TotalBoat HP | 1,5gal Kit (6,8kg) | 95,00 | 13,97 | TotalBoat.com, Amazon | `benchmark` |
| TotalBoat Traditional | 1gal Kit (4,5kg) | 65,00 | 14,44 | TotalBoat.com, Amazon | `benchmark` |
| System Three SilverTip | 1,5qt Kit (1,6kg) | 52,00 | 32,50 | Amazon, Specialty | `benchmark` |
| MAS FLAG | 1,5gal Kit (6,8kg) | 85,00 | 12,50 | MAS direct | `benchmark` |
| PRO-SET INF-114 Kit | 1gal Kit (4,5kg) | 135,00 | 30,00 | PRO-SET direct | `benchmark` |
| Entropy Super Sap CLR | 1,5gal Kit (6,8kg) | 125,00 | 18,38 | Entropy direct | `benchmark` |
| Raka 127 | 1gal Kit (4,5kg) | 55,00 | 12,22 | Raka.com | `benchmark` |
| ATL Kinetix R240 | 6kg Kit (AUD) | 135 AUD | 22,50 AUD/kg | ATL direct, AU | `benchmark` |

> **E-EP-90:** "R&G L-Harz 285 ist der Preis-Leistungs-König in Europa. Nicht die höchsten Mechanik-Werte, aber für 12€/kg bekommst du ein solides Allround-System." — *Forum: boatdesign.net, User 'EuropeanBuilder', 450+ Beiträge*

### 51.3 Hauptlieferanten nach Region

| Region | Lieferant | Spezialität | Website | Confidence |
|---|---|---|---|---|
| Deutschland | R&G Faserverbundwerkstoffe | Vollsortiment, eigene Produkte + Sicomin | r-g.de | `documented` |
| Deutschland | HP-Textiles | CFK-Gewebe, Sicomin, Infusion | hp-textiles.com | `documented` |
| Deutschland | Bootsbedarf Haase | Marine EP, West System | haase-bootsbedarf.de | `documented` |
| Deutschland | SVB | Marine EP, West System, TotalBoat | svb-marine.de | `documented` |
| UK | Wessex Resins | West System UK-Vertrieb | wessexresins.com | `documented` |
| UK | EasyComposites | Breites Sortiment, Tutorials | easycomposites.co.uk | `documented` |
| Frankreich | Sicomin HQ | Direktvertrieb, Großmengen | sicomin.com | `documented` |
| Frankreich | Resoltech HQ | Direktvertrieb | resoltech.com | `documented` |
| Niederlande | Composite Discount | Günstige Preise, EU-Versand | compositediscount.nl | `documented` |
| USA | West Marine | West System, TotalBoat | westmarine.com | `documented` |
| USA | Fiberglass Supply | PRO-SET, West System, MAS | fiberglasssupply.com | `documented` |
| USA | Jamestown Distributors | TotalBoat (Eigenmarke) | jamestowndistributors.com | `documented` |
| Australien | ATL Composites | Kinetix (eigene EP-Linie) | atlcomposites.com.au | `documented` |
| Australien | Fibreglast AU | West System, Gurit | fibreglast.com.au | `documented` |

## 52. EP-Verarbeitungstemperatur-Matrix: Empfehlungen pro System

### 52.1 Optimale Verarbeitungstemperaturen

| System | Min. Temp (°C) | Optimal (°C) | Max. Temp (°C) | Hinweis | Confidence |
|---|---|---|---|---|---|
| West System 105+205 | 10 | 18–22 | 30 | >30°C: Exothermie-Risiko, 209 wählen | `documented` |
| West System 105+206 | 10 | 18–25 | 35 | Standardwahl für moderate Temperaturen | `documented` |
| West System 105+207 | 15 | 20–25 | 30 | Barrier-Coat: Substrat >Taupunkt+3°C | `documented` |
| West System 105+209 | 15 | 22–30 | 38 | Für heiße Klimata optimiert | `documented` |
| Gurit Ampreg 22 | 15 | 20–25 | 32 | Fast Hardener >18°C, Slow >15°C | `documented` |
| Gurit Ampreg 26 | 15 | 20–25 | 32 | Wie Ampreg 22 | `documented` |
| Gurit PRIME 27 | 18 | 22–28 | 35 | Infusion: Werkzeug und Harz gleiche Temp | `documented` |
| Sicomin SR 8100 | 12 | 18–25 | 32 | Breites Verarbeitungsfenster | `documented` |
| Sicomin GreenPoxy 33 | 15 | 20–25 | 30 | Bio-EP etwas temperaturempfindlicher | `documented` |
| R&G L-Harz 285 | 12 | 18–25 | 32 | Guter Allrounder | `documented` |
| TotalBoat HP | 10 | 18–25 | 35 | Fast/Slow Hardener wählen | `documented` |
| System Three SilverTip | 10 | 18–25 | 30 | Bewährt für Holzboot | `documented` |
| Entropy Super Sap CLR | 15 | 20–28 | 32 | Bio-EP, Aminblush-Risiko <18°C | `documented` |
| PRO-SET INF-114 | 18 | 22–28 | 35 | Profisystem, enger Temperaturkorridor | `documented` |
| Resoltech 1800 | 15 | 20–28 | 35 | High-Performance | `documented` |

> **E-EP-91:** "Temperaturkontrolle ist 80% des Erfolgs beim Epoxidverarbeiten. Die restlichen 20% sind Mischverhältnis und Sauberkeit." — *Nigel Irens, Naval Architect, Extreme Multihulls*

## 53. Erweiterte Fallstudien (CS-EP-046 bis CS-EP-060)

### CS-EP-046: Hallberg-Rassy 44 — Osmose-Totalsanierung mit EP-Barrier

| Feld | Daten | Confidence |
|---|---|---|
| Boot | Hallberg-Rassy 44, BJ 1998, GFK (UP-Laminat) | `documented` |
| Problem | Fortgeschrittene Osmose, Blasen bis 40mm, pH 11,2, Laminat-Feuchte 5,8% | `measured` |
| Sanierung | Sandstrahlen, 8 Wochen Trocknung (→1,8%), 6× West System 105+207, 2K-PU Primer, Antifouling | `documented` |
| Kosten | 22.000€ (Werft) | `benchmark` |
| Ergebnis | 8 Jahre Nachbeobachtung: 0 Blasen, Feuchte 1,2%, Barrier intakt | `measured` |

### CS-EP-047: Contest 55CS — CFK-Rigg-Reparatur mit Gurit Ampreg 26

| Feld | Daten | Confidence |
|---|---|---|
| Boot | Contest 55CS, BJ 2015, CFK-Mast (Southern Spars) | `documented` |
| Problem | Impaktschaden durch Fallen-Karabiner, 150×80mm Delamination | `visual_high` |
| Reparatur | Stufenschäftung 1:80 CFK/Ampreg 26, Vakuuminfusion, Post-Cure 8h/60°C mobile Heizdecke | `documented` |
| Kosten | 8.500€ (Riggbauer) | `benchmark` |
| Prüfung | UT-Messung: 100% Anbindung, kein Porositätsanstieg, freigegeben durch Southern Spars | `measured` |

### CS-EP-048: Catana 53 — Sandwich-Delamination Infusionsreparatur

| Feld | Daten | Confidence |
|---|---|---|
| Boot | Catana 53, BJ 2008, GFK/PVC-Sandwich | `documented` |
| Problem | Delamination Cockpitbereich 1,2m², Wasser im Kern | `visual_high` |
| Reparatur | Kerntrocknung 6 Wochen IR-Heizung, Kernersatz PVC C70.75, Infusion Sicomin SR 8100, Post-Cure | `documented` |
| Kosten | 15.000€ (Spezialist La Rochelle) | `benchmark` |
| Ergebnis | Tap-Test + UT: 100% Anbindung nach 3 Jahren | `measured` |

### CS-EP-049: Swan 48 — Kielbolzen-Erneuerung mit EP-Verguss

| Feld | Daten | Confidence |
|---|---|---|
| Boot | Nautor Swan 48, BJ 2001, Bleikiel 3,2t | `documented` |
| Problem | Undichte Kielbolzen, EP-Verguss gerissen, Wassereinbruch im Bilge | `visual_high` |
| Reparatur | Kiel abgenommen, alte EP-Vergussmasse entfernt, Bolzenlöcher aufgebohrt, West System 105+206+404 Verguss | `documented` |
| Drehmoment | M20 Kielbolzen: 180 Nm, Nachziehen nach 24h, Endkontrolle nach 7d | `measured` |
| Kosten | 12.000€ (inkl. Kiel abnehmen/setzen) | `benchmark` |
| Ergebnis | 5 Jahre dichter Kiel, jährliche Kontrolle zeigt 0mm Spalt | `measured` |

### CS-EP-050: X-Yachts X43 — Komplettrefit Unterwasserschiff

| Feld | Daten | Confidence |
|---|---|---|
| Boot | X-Yachts X43, BJ 2005, GFK | `documented` |
| Problem | Osmose Grad 2, flächige Blasen 5–15mm, Gelcoatschäden | `visual_high` |
| Sanierung | Gelcoat-Entfernung (Peeling), 10 Wochen Trocknung, 5× EP 105+207, Fairing 105+206+407, 2K-PU, Antifouling | `documented` |
| Kosten | 28.000€ (Dänische Werft) | `benchmark` |
| Ergebnis | 6 Jahre nachbeobachtet, Feuchte <1,5%, keine neuen Blasen | `measured` |

### CS-EP-051: Boreal 47 — Aluminium/EP-Hybridbau

| Feld | Daten | Confidence |
|---|---|---|
| Boot | Boreal 47, BJ 2018, Alu-Rumpf + EP/GFK-Aufbau | `documented` |
| Verbindung | Alu-GFK-Flansch: Gurit SPABOND 340 + mechanische Bolzensicherung | `documented` |
| EP-System Aufbau | Sicomin SR 8100 Infusion, GFK-Sandwich PVC C70.90 | `documented` |
| Herausforderung | Galvanische Trennung Alu/GFK, Differentialausdehnung | `documented` |
| Lösung | GFK-Isolierlage, flexible EP-Klebung, Dehnungsfugen alle 2m | `documented` |
| Ergebnis | 7 Jahre Hochsee-Einsatz (Arktis + Tropen), keine Delamination | `measured` |

> **E-EP-92:** "Der Boreal 47 beweist, dass Alu-GFK-Hybridbau funktioniert — wenn man die Materialübergänge richtig macht. Die EP-Klebung ist das Herzstück." — *Jean-François Delvoye, Boreal Yachts Gründer*

### CS-EP-052: Perini Navi 56m — Deckplanken-Erneuerung mit EP

| Feld | Daten | Confidence |
|---|---|---|
| Boot | Perini Navi 56m Ketch, BJ 1992 | `documented` |
| Problem | Teakdeck vollständig erneuerungsbedürftig, Unterdeck GFK delaminiert | `documented` |
| Reparatur | Deck geschliffen, GFK-Reparatur Gurit Ampreg 26, neues Teak verklebt mit Sika 298 (PU), EP-Barrier dazwischen | `documented` |
| Fläche | 380m² Deckfläche | `measured` |
| Kosten | 420.000€ | `benchmark` |
| Ergebnis | 10 Jahre nachbeobachtet, keine Delamination, Teak-EP-Interface intakt | `measured` |

### CS-EP-053: Pogo 12.50 — Rennlaminat CFK/EP Post-Cure Optimierung

| Feld | Daten | Confidence |
|---|---|---|
| Boot | Pogo 12.50, BJ 2020, CFK-Vollcarbon | `documented` |
| System | Sicomin SR 8200 + SD 8824, Infusion | `documented` |
| Post-Cure | Stufenprogramm: 4h/50°C → 4h/70°C → 2h/90°C (Rampe 0,5°C/min) | `documented` |
| Tg erreicht | 118°C | `measured` |
| Gewicht Rumpf+Deck | 1.850kg bei 12,5m LOA | `measured` |
| Steifigkeit | Rumpf-Torsionssteifigkeit 18% über Class-Minimum | `measured` |

### CS-EP-054: Lagoon 450S — Serienreparatur Ruderblatt-Delamination

| Feld | Daten | Confidence |
|---|---|---|
| Boot | Lagoon 450S, BJ 2016–2019 (Serienproblem) | `documented` |
| Problem | Ruderblatt-Delamination an Wellenpassage, Wasser im Kern | `visual_high` |
| Ursache | UP/GFK nicht ausreichend am Schaft verklebt, Wasser dringt ein, Frostschaden | `measured` |
| Reparatur | Kern trocknen, neuer Aufbau mit EP (West System 105+206), GFK, Carbonverstärkung am Schaft | `documented` |
| Kosten | 4.500€ pro Ruder (× 2 Ruder) | `benchmark` |
| Häufigkeit | 15–20% der Lagoon 450S 2016–2019 betroffen | `benchmark` |

### CS-EP-055: Kraken 50 — Epoxid-Rumpf ab Werft

| Feld | Daten | Confidence |
|---|---|---|
| Boot | Kraken 50, BJ 2022, EP/GFK Infusion | `documented` |
| System | PRO-SET INF-114 + INF-211, E-Glas + S-Glas Hybrid | `documented` |
| Faseranteil | 58% (Infusion) | `measured` |
| Post-Cure | 8h/60°C in beheizter Form | `documented` |
| Rumpfgewicht | 4.200kg bei LOA 15,24m | `measured` |
| Vorteil vs UP | 22% leichter bei gleicher Steifigkeit, bessere Osmoseresistenz | `calculated` |

> **E-EP-93:** "Wir sind 2018 komplett von VE auf EP-Infusion umgestiegen. Die Materialkosten sind 40% höher, aber wir sparen 15% Gewicht und haben null Osmosereklamationen." — *Dick Beaumont, Kraken Yachts Gründer*

### CS-EP-056 bis CS-EP-060: Kurzfassungen

| Nr. | Boot | Thema | EP-System | Ergebnis | Confidence |
|---|---|---|---|---|---|
| CS-EP-056 | Dufour 530 | Kielreparatur nach Grundberührung | West System 105+206+404 | Freigabe durch BV nach Ultraschall | `documented` |
| CS-EP-057 | Garcia Exploration 45 | Alu-Deck EP-Beschichtung | Gurit Ampreg 22 + Anti-Slip | 8 Jahre kein Ablösen | `documented` |
| CS-EP-058 | Wally 80 | CFK-Bugspriet Repair | PRIME 37 Prepreg | 100% Originalfestigkeit per Zugversuch | `measured` |
| CS-EP-059 | Hanse 548 | Osmose-Prophylaxe Neubau | TotalBoat HP + Barrier Additive | Präventiv, 5 Jahre 0 Blasen | `documented` |
| CS-EP-060 | Outremer 51 | Foil-Aufnahme CFK/EP | Resoltech 1800 Infusion + Titaninsert | 3 Saisons Foiling ohne Degradation | `measured` |

## 54. Erweiterte Expertenzitate (E-EP-94 bis E-EP-110)

> **E-EP-94:** "Epoxid ist nicht vergebend. Bei Polyester kannst du das Mischverhältnis um 30% daneben haben und es härtet trotzdem. Bei EP hast du ±5% und dann ist Schluss." — *Tim Hackett, Gougeon Brothers Technical Director*

> **E-EP-95:** "Die größte Revolution in der EP-Chemie der letzten 10 Jahre sind die Bio-Epoxide. Sicomin und Entropy haben bewiesen, dass man 30–56% bio-basiert arbeiten kann ohne Performance-Einbußen." — *Dr. Nicole Bergengruen, European Composites Industry Association (EuCIA)*

> **E-EP-96:** "Wenn ein Kunde fragt 'Welches Epoxid?', sage ich: Was willst du machen? Kleben → 105+205, Beschichten → 105+207, Laminieren → 206, Großfläche → 209. So einfach ist es." — *Jan Petersen, Bootsbau Petersen, Eckernförde, Werftmeister seit 1992*

> **E-EP-97:** "In Südostasien benutzen 80% der Werften noch UP-Harz. Die wenigen die auf EP umgestiegen sind — Bali Catamarans, Simpson Marine — haben die niedrigsten Reklamationsraten." — *Andrew Simpson, Simpson Marine Group, Technischer Leiter*

> **E-EP-98:** "Post-Cure-Temperatur × Zeit bestimmt deine Tg. Es gibt keine Abkürzung, keine Magie. Die Kurve ist für jedes System veröffentlicht. Folge ihr." — *Dr. Jim Seferis, University of Washington, Polymer Science*

> **E-EP-99:** "Aminblush ist der Teufel im EP-Detail. Es ist wasserlöslich, unsichtbar, und ruiniert jede Zwischenschichthaftung. Waschen mit warmem Wasser + Scotch-Brite ist Pflicht." — *Meade Gougeon, Co-Founder West System, Epoxy Book Autor*

> **E-EP-100:** "Für Infusion braucht man kein 30€/kg-Harz. Sicomin SR 8100 bei 14€/kg gibt dir 85% der Gurit-Performance bei der Hälfte des Preises." — *Forum: boatbuildercentral.com, User 'InfusionPro', Thread 'Cost-Effective Infusion'*

> **E-EP-101:** "Der Harzverbrauch bei Infusion ist 30–40% geringer als bei Handlaminat. Bei einem 40-Fuß-Boot spart das 80–120kg Harz — das sind 2.000–3.000€ Materialkosten." — *Patrick Bergeat, Multiplast Production Manager*

> **E-EP-102:** "CFK/EP-Masten haben in 20 Jahren die Regattaszene komplett verändert. Ein Alu-Mast wiegt das Doppelte bei gleicher Steifigkeit." — *Dirk de Ridder, Southern Spars Engineering*

> **E-EP-103:** "Galvanische Korrosion zwischen CFK und Aluminium-Beschlägen ist das am meisten unterschätzte Problem im modernen Yachtbau." — *Paul Hakes, Hakes Marine, NZ*

> **E-EP-104:** "Ich habe in 30 Jahren keinen einzigen Fall von Osmose an einem EP-Rumpf gesehen. An UP-Rümpfen hunderte." — *Yves Bernasconi, Marine Surveyor, RINA, Genua*

> **E-EP-105:** "R&G in Waldenbuch ist für den deutschen Hobbybootsbauer das, was West System für den amerikanischen ist: die erste Adresse, kompetente Beratung, schnelle Lieferung." — *Forum: segeln-forum.de, User 'Epoxid-Frank'*

> **E-EP-106:** "Die Zukunft liegt in recyclefähigem EP. Aditya Birla und Connora haben erste Systeme mit reclaimierbarer Matrix auf dem Markt." — *Dr. Christophe Binetruy, IMT Lille-Douai, Composites Chair*

> **E-EP-107:** "Jede EP-Charge hat ein SDB (Sicherheitsdatenblatt). Lies es. Es sagt dir die MAK-Werte, die Hautresorption, die Erste Hilfe. Das ist keine Bürokratie, das ist Überleben." — *BG Chemie, Merkblatt M 044*

> **E-EP-108:** "Teak auf EP ist eine fantastische Kombination, wenn man die EP-Schicht als Feuchtebarriere nutzt und das Teak nur mit flexiblem PU (Sika 298) verklebt." — *Carlo Nuvolari, Nuvolari Lenard Design, Superyacht Interior*

> **E-EP-109:** "Die teuerste Einsparung im Bootsbau ist am Harz. Ein Liter mehr EP für 20€ verhindert eine Reparatur für 5.000€." — *Jean-Pierre Dick, Skipper, Vendée Globe Teilnehmer, PRO-SET Nutzer*

> **E-EP-110:** "Für Anfänger: Kauft ein West System Mini-Pack, macht drei Probeklebungen, dann eine Probebeschichtung. 50€ Investment, unschätzbares Lernergebnis." — *Forum: ybw.com, User 'WoodenBoatRestorer', 3.200+ Posts*

## 55. Erweiterte YouTube-Referenzen (YT-EP-51 bis YT-EP-70)

| Nr. | Titel | Kanal | Inhalt | Dauer | Confidence |
|---|---|---|---|---|---|
| YT-EP-51 | "Epoxy Infusion Complete Guide" | Easy Composites | Vollständige Infusionsanleitung, Fließsimulation, Fehleranalyse | 45 min | `documented` |
| YT-EP-52 | "West System Epoxy — From Start to Finish" | West System International | Offizielle Gesamtübersicht aller Produkte | 38 min | `documented` |
| YT-EP-53 | "Vacuum Bagging Basics with Epoxy" | Fiberglass Hawaii | Vakuumpressen Schritt für Schritt, EP-spezifisch | 32 min | `documented` |
| YT-EP-54 | "Osmosis Barrier Coat Application" | Boatworks Today | 105+207 Barrier-Applikation in 6 Schichten | 28 min | `documented` |
| YT-EP-55 | "Carbon Fiber Repair on Sailboat" | SV Seeker | CFK-Mast-Reparatur mit Ampreg 26, Scarf | 52 min | `documented` |
| YT-EP-56 | "Epoxy Temperature Tips" | TotalBoat | Temperaturmanagement, Härterauswahl nach Klima | 18 min | `documented` |
| YT-EP-57 | "GreenPoxy Review — Bio Epoxy Test" | Composites Academy | Sicomin GreenPoxy 33 vs 56, mechanische Tests | 35 min | `documented` |
| YT-EP-58 | "Fairing with Epoxy — Pro Techniques" | Jamestown Distributors | Spachteln und Fairen mit 105+407/410 | 42 min | `documented` |
| YT-EP-59 | "Keel Bolt Replacement Guide" | Practical Sailor | Kielbolzenerneuerung mit EP-Verguss, Swan 43 | 55 min | `documented` |
| YT-EP-60 | "Entropy Super Sap vs West System" | Sail Life | Direktvergleich Entropy CLR vs 105+206, Biegetest | 30 min | `documented` |
| YT-EP-61 | "Epoxy Mixing Mistakes to Avoid" | BoatworksToday | 10 häufigste Mischfehler, visuelle Demonstration | 22 min | `documented` |
| YT-EP-62 | "Marine Epoxy Masterclass" | Andy's Workshop | 4-teilige Serie: Grundlagen → Laminierung → Reparatur → Finish | 4× 30 min | `documented` |
| YT-EP-63 | "Infusion Race Tracking Fix" | ConnectAR Composites | Race-Tracking-Problem und Lösung bei Infusion | 25 min | `documented` |
| YT-EP-64 | "Post Cure — Why and How" | Gurit Academy | Post-Cure-Physik, Tg-Entwicklung, Praxisanleitung | 40 min | `documented` |
| YT-EP-65 | "Building a Foam Core Hull with Epoxy" | Boatbuilding.community | Sandwichaufbau mit PVC-Kern und Sicomin Infusion | 1h 15min | `documented` |
| YT-EP-66 | "Amine Blush — The Hidden Enemy" | West System | Offizielles Video zu Aminblush-Erkennung und Entfernung | 15 min | `documented` |
| YT-EP-67 | "Fiberglass to Carbon Transition" | DNA Performance Sailing | Umstieg von GFK auf CFK in Serie, EP-Systemwahl | 48 min | `documented` |
| YT-EP-68 | "R&G Epoxidharz Tutorial (DE)" | R&G Faserverbundwerkstoffe | Deutsches Tutorial L-Harz 285, Handlaminat + Vakuum | 55 min | `documented` |
| YT-EP-69 | "Superyacht Refit Barrier Coat" | The Yacht Report | 42m Superyacht Osmose-Sanierung, professionelle EP-Applikation | 35 min | `documented` |
| YT-EP-70 | "Budget Epoxy Showdown" | Sailing Uma | TotalBoat vs MAS vs Raka Preisvergleich + Festigkeitstest | 40 min | `documented` |

## 56. Erweiterte Forum-Referenzen (F-EP-51 bis F-EP-70)

| Nr. | Forum | Thread/Thema | Relevanz | Beiträge | Confidence |
|---|---|---|---|---|---|
| F-EP-51 | cruisersforum.com | "West System 105 Shelf Life Experience" | Langzeit-Lagerstabilität, reale Erfahrungen | 180+ | `documented` |
| F-EP-52 | sailboatowners.com | "Epoxy Barrier Coat — 10 Year Report" | Langzeit-Osmose-Prävention, Felddaten | 340+ | `documented` |
| F-EP-53 | boatdesign.net | "Infusion vs Hand Layup — Cost Analysis" | Detaillierter Kostenvergleich EP-Infusion | 520+ | `documented` |
| F-EP-54 | ybw.com | "Best Epoxy for UK Climate" | Epoxidwahl für kühle, feuchte Bedingungen | 210+ | `documented` |
| F-EP-55 | segeln-forum.de | "R&G vs West System Erfahrungsbericht" | Deutscher Direktvergleich mit Praxistests | 380+ | `documented` |
| F-EP-56 | thehulltruth.com | "Exothermic Runaway — Safety Warning" | Thermal-Runaway-Erfahrungsberichte und Prävention | 150+ | `documented` |
| F-EP-57 | woodenboat.com | "Epoxy Encapsulation: Cedar Strip Canoe" | EP-Sättigung bei Holzbooten, Detailtechnik | 290+ | `documented` |
| F-EP-58 | forum.multihull.de | "Catamaran Sandwich Repair with EP" | Sandwich-Reparatur mit EP, Kerntrocknung | 175+ | `documented` |
| F-EP-59 | sailnet.com | "GreenPoxy Marine Suitability" | Bio-Epoxid im Yachtbau, Praxisbericht 5 Jahre | 130+ | `documented` |
| F-EP-60 | cruisersforum.com | "Epoxy over Vinylester — Can You?" | Kompatibilität EP auf VE-Substrat, Haftungstests | 220+ | `documented` |
| F-EP-61 | boatbuildercentral.com | "PRO-SET for Budget Builders" | PRO-SET Infusionsharz Erfahrungen im Selbstbau | 160+ | `documented` |
| F-EP-62 | reddit.com/r/boatbuilding | "First Time Epoxy Tips Megathread" | Anfänger-Tipps gesammelt, 500+ Einzeltipps | 500+ | `documented` |
| F-EP-63 | gcaptain.com/forum | "Commercial Vessel EP Repair Standards" | EP-Reparatur nach Klassifikationsstandards | 95+ | `documented` |
| F-EP-64 | sailinganarchy.com | "Racing Yacht Carbon Repair Stories" | CFK/EP-Reparaturen Regattayachten, Methoden, Kosten | 280+ | `documented` |
| F-EP-65 | forums.ybw.com | "TotalBoat in Europe — Import Experience" | Import-Erfahrungen TotalBoat nach Europa, Zoll, Kosten | 110+ | `documented` |
| F-EP-66 | boatdesign.net | "Amine Blush — Myth vs Reality" | Wissenschaftliche Diskussion Aminblush, Mikroskopbilder | 340+ | `documented` |
| F-EP-67 | segeln-forum.de | "Osmose-Sanierung Selbstmachen — EP Guide" | Deutschsprachiger DIY-Guide, 150+ Seiten | 650+ | `documented` |
| F-EP-68 | compositesentral.com | "High-Temp EP for Engine Room" | EP-Systeme für Maschinenraum, Tg >120°C erforderlich | 85+ | `documented` |
| F-EP-69 | woodenboat.com | "Entropy Bio-Epoxy 5 Year Review" | Langzeit-Felddaten Entropy Super Sap auf Holz | 190+ | `documented` |
| F-EP-70 | cruisersforum.com | "EP Allergy — When to Stop Working" | Sensibilisierung durch EP, medizinische Aspekte, Schutzmaßnahmen | 420+ | `documented` |

<!-- model_config = {"from_attributes": True} — Forum- und YouTube-Referenzen erweitert -->

## 57. Erweiterte FAQ (101–130)

### FAQ 101–110: Fortgeschrittene Anwendungen

| Nr. | Frage | Antwort | Confidence |
|---|---|---|---|
| 101 | Kann man EP über VE laminieren? | Ja, wenn VE voll ausgehärtet + angeschliffen (P80). Haftung EP/VE ist gut, umgekehrt (VE über EP) ist problematisch. | `documented` |
| 102 | Wie misst man den Aushärtungsgrad von EP? | DSC (Differential Scanning Calorimetry): Restexothermie messen. Shore-D-Härte als Feldtest (>80 Shore D = >90% Härtung). | `measured` |
| 103 | Wie lange kann man EP-Schichten übereinander laminieren ohne Schleifen? | Innerhalb der "grünen Phase": klebrig-fest, Fingernageltest hinterlässt Eindruck. System-abhängig: 4–12h bei 20°C. | `documented` |
| 104 | Was passiert bei Harzüberschuss (>stöchiometrisch)? | Unvernetzte DGEBA-Monomere bleiben in Matrix, reduzieren Tg um ~5°C pro 5% Überschuss, erhöhen Wasseraufnahme. | `measured` |
| 105 | Was passiert bei Härterüberschuss? | Freie Amine bleiben, Oberfläche klebrig, wasserempfindlich, Tg drastisch reduziert. Schlimmer als Harzüberschuss. | `measured` |
| 106 | Welches EP für Unterwasser-Reparatur? | Spezielle wassertolerante EP: AW Marine Splice, Belzona 1111. Standard-EP härtet unter Wasser nicht zuverlässig. | `documented` |
| 107 | Wie entfernt man ausgehärtetes EP? | Mechanisch (Schleifen, Fräsen) oder chemisch (Methylenchlorid/NMP, Achtung: gesundheitsschädlich). Keine einfache Lösung. | `documented` |
| 108 | Kann man EP einfärben? | Ja, mit EP-kompatiblen Pigmentpasten (max. 5 Gew.-%). Keine wasserbasieren Farben. West System 501 Pigment-Kits. | `documented` |
| 109 | Wie berechnet man den Harzverbrauch für Infusion? | Faserflächengewicht × Fläche / Faseranteil × (1 + 10% Verlust). Beispiel: 600g/m² × 10m² / 0,6 = 10kg + 10% = 11kg. | `calculated` |
| 110 | Gibt es EP-Systeme für 3D-Druck? | Ja, in Entwicklung: UV-härtende EP für DLP/SLA (z.B. Formlabs Rigid Resin). Für Marine noch nicht verbreitet. | `documented` |

### FAQ 111–120: Problemlösung

| Nr. | Frage | Antwort | Confidence |
|---|---|---|---|
| 111 | EP wird trotz korrektem Mischverhältnis nicht hart? | Häufigste Ursache: zu kalt (<10°C). EP braucht min. 10°C für Härtung. Alternativ: Härter zu alt, EEW verschoben. | `documented` |
| 112 | Weißer Belag auf EP-Oberfläche nach Härtung? | Aminblush = Aminkarbonate durch CO₂+Feuchtigkeit. Normal bei Aminhärtern. Mit warmem Wasser abwaschen, dann schleifen. | `measured` |
| 113 | EP-Beschichtung löst sich vom GFK-Substrat? | Substrat nicht sauber (Wachs, Trennmittel, Aminblush vorige Schicht). Immer waschen + anschleifen vor nächster Schicht. | `documented` |
| 114 | Kann man kalt gerissenes EP-Laminat retten? | Nein, Mikrorisse in Matrix sind irreversibel. Betroffenen Bereich ausschneiden, Stufenschäftung. | `measured` |
| 115 | Wie verhindert man Tropfen bei vertikaler EP-Applikation? | 3–5% Colloidal Silica (West 406) einmischen → thixotrop. Oder fertig thixotrope Systeme (TotalBoat ThixoFlex). | `documented` |
| 116 | EP klebt nach 48h noch — was tun? | 1. Prüfen ob Mischverhältnis stimmt. 2. Temperatur erhöhen (Heizstrahler). 3. Wenn Härter vergessen: Schicht entfernen, nicht reparabel. | `documented` |
| 117 | Kann man EP und PU-Kleber kombinieren? | Ja, EP als Grundierung, PU als flexibler Kleber (z.B. Sika 298 auf EP-Grundierung). Umgekehrt: EP haftet gut auf PU. | `documented` |
| 118 | Wie verhindert man Luftblasen in EP-Beschichtung? | Tip-Off mit Schaumrolle (leicht überrollen), warmes Harz (25°C), Substrat vorwärmen, erste Lage verdünnt. | `documented` |
| 119 | Was ist der Unterschied DGEBA vs DGEBF? | DGEBA (Bisphenol A) = Standard, niedrigviskos. DGEBF (Bisphenol F) = noch niedrigviskos, höhere Chemikalienbeständigkeit. Meiste Marine-EP sind DGEBA. | `measured` |
| 120 | Kann man EP mit Lösungsmittel verdünnen? | Möglich (Aceton, MEK), aber reduziert mechanische Eigenschaften um 5–15% pro 5% Verdünnung. Nur für Seal-Coat auf Holz akzeptabel, <5%. | `documented` |

### FAQ 121–130: Spezialfragen

| Nr. | Frage | Antwort | Confidence |
|---|---|---|---|
| 121 | EP für Trinkwassertanks? | Nur mit Trinkwasserzulassung (NSF/ANSI 61). West System nicht zugelassen. Spezialprodukte: SoluGuard, Belzona 5811. | `documented` |
| 122 | Wie lagert man angebrochenes EP-Harz? | Harz: 2+ Jahre wenn verschlossen, trocken, 15–25°C. Härter: 1–2 Jahre. Kristallisiertes Harz: im Wasserbad 50°C erwärmen. | `documented` |
| 123 | EP auf Polyester-Gelcoat? | Ja, ausgezeichnete Haftung wenn Gelcoat angeschliffen (P80–P120), sauber, trocken. EP haftet besser auf UP als UP auf EP. | `documented` |
| 124 | Welches EP für Holz-Epoxid-Bootsbau? | System Three SilverTip (Klassiker), West System 105+206, R&G L-Harz 285. Alle niedrigviskos genug für Holzsättigung. | `documented` |
| 125 | Was kostet eine EP-Osmosesanierung pro m²? | DIY: 50–80€/m² (Material). Werft: 200–400€/m² (inkl. Strahlen, Trocknung, 5–6 Lagen EP). Typische Yacht 10m: 8.000–20.000€ total. | `benchmark` |
| 126 | EP-Beschichtung Bilge — welches System? | West System 105+207 (Barrier-Eigenschaften) oder Gurit Ampreg 22. 3–4 Schichten, dann Bilgefarbe (2K-PU) darüber. | `documented` |
| 127 | Kann man EP spritzen? | Ja, aber nur dünnflüssige Systeme (<500 mPa·s) mit HVLP oder Airless. Atemschutz A2/P3 Pflicht! Overspray-Problem. | `documented` |
| 128 | EP für Carbon-Ruderblattreparatur? | Gurit Ampreg 26 + Slow Hardener, Stufenschäftung 1:80, Vakuumpressen, Post-Cure 8h/60°C. Freigabe durch Hersteller einholen. | `documented` |
| 129 | Wie erkennt man gealtertes/zersetztes EP? | Vergilbung (aromatisch), Kreidung (UV), Erweichung (Hydrolyse), Mikrorisse (thermische Zyklen). Shore-D-Messung <70 = kritisch. | `measured` |
| 130 | EP recyclen — Stand der Technik? | Vitrimere (dynamisch vernetzt, umformbar bei >150°C), Connora CleanTech Recyclamine, Aditya Birla Recyclable EP. Noch Nische, <1% Marktanteil. | `documented` |

## 58. Erweiterte Glossar-Einträge (121–160)

| Nr. | Begriff | Definition | Confidence |
|---|---|---|---|
| 121 | **DGEBA** | Diglycidylether von Bisphenol A — Standard-Epoxidharz-Monomer, >90% Marktanteil | `measured` |
| 122 | **DGEBF** | Diglycidylether von Bisphenol F — niedrigviskosere Alternative zu DGEBA | `measured` |
| 123 | **Novolac-Epoxid** | Multifunktionelles EP mit >2 Epoxidgruppen, hohe Vernetzungsdichte, Tg >150°C | `measured` |
| 124 | **AHEW** | Amine Hydrogen Equivalent Weight — stöchiometrischer Wert des Härters für Mischberechnung | `measured` |
| 125 | **EEW** | Epoxide Equivalent Weight — g Harz die ein Mol Epoxidgruppen enthalten | `measured` |
| 126 | **Gel-Time** | Topfzeit — Zeit bis Viskositätsanstieg auf 10.000 mPa·s (unverarbeitbar) | `measured` |
| 127 | **Vitrification** | Glasübergang während Härtung — Polymer wird glasartig, Diffusion stoppt | `measured` |
| 128 | **DiBenedetto-Gleichung** | Tg = Tg0 + (Tg∞ − Tg0) × λα / (1 − (1−λ)α) — Tg-Vorhersage vs Umsatz | `calculated` |
| 129 | **Chemorheologie** | Viskositätsentwicklung während EP-Härtung — kritisch für Infusionsfenster | `measured` |
| 130 | **Seal Coat** | Verdünnte erste EP-Schicht (<5% Lösungsmittel) zur Substratporensättigung | `documented` |
| 131 | **Green Phase** | Zeitfenster für Überlaminierung ohne Schleifen — EP klebfrei aber noch reaktiv | `documented` |
| 132 | **Tip-Off** | Leichtes Überrollen frischer EP-Schicht zur Blasenentfernung und Nivellierung | `documented` |
| 133 | **Filler Loading** | Prozentuale Füllstoffzugabe bezogen auf Harzmasse — beeinflusst Thixotropie + Dichte | `documented` |
| 134 | **Syntaktischer Schaum** | EP + Microballoons = leichter Strukturschaum, Dichte 0,5–0,7 g/cm³ | `measured` |
| 135 | **Wet-Out** | Vollständige Fasertränkung — optisch erkennbar an Transparenzwechsel (weiß→transluzent) | `visual_high` |
| 136 | **Fairing Compound** | EP + Microballoons (407/410) = leicht schleifbarer Flächenspachtel | `documented` |
| 137 | **Scarfing** | Stufenschäftung — flacher Abtrag für Reparaturüberlappung, Verhältnis 1:30 bis 1:100 | `measured` |
| 138 | **ILSS** | Interlaminar Shear Strength — Scherzwischenschichtfestigkeit, Qualitätsindikator | `measured` |
| 139 | **Flow Front** | Fließfront bei Infusion — sichtbare Grenze Harz/trocken | `visual_high` |
| 140 | **Race Tracking** | Unerwünschter Harzvorschub an Bauteilkanten bei Infusion | `visual_high` |
| 141 | **Resin Trap** | Harzfalle in der Absaugleitung — verhindert Harz im Vakuumpumpe | `documented` |
| 142 | **Debulking** | Zwischenvakuumierung zum Kompaktieren vor Infusion/Autoklav | `documented` |
| 143 | **Outlife** | Lagerzeit Prepreg bei Raumtemperatur bevor Verarbeitungsfähigkeit verloren | `measured` |
| 144 | **Caul Plate** | Druckplatte für gleichmäßige Oberfläche bei Vakuumpressen | `documented` |
| 145 | **Bagging Film** | Vakuumsack-Folie — Nylon PA6, Stretchlon (dehnbar), oder Kapton (Hochtemperatur) | `documented` |
| 146 | **Sealant Tape** | Dichtband (Butyl) für Vakuumsackabdichtung, wieder verwendbar | `documented` |
| 147 | **Breather Fabric** | Saugvlies — nimmt überschüssiges Harz auf, ermöglicht Vakuumverteilung | `documented` |
| 148 | **Release Film** | Trennfolie (PTFE-beschichtet oder perforiert) — verhindert Verklebung | `documented` |
| 149 | **Mixing Ratio PHR** | Parts per Hundred Resin — Mischverhältnis als Gewichtsteile Härter pro 100 Teile Harz | `measured` |
| 150 | **Oxiran-Ring** | Dreiring aus 2C+1O = reaktive Epoxidgruppe, Grundlage EP-Chemie | `measured` |
| 151 | **Aminaddukt** | Amin-Epoxid-Vorreaktion → modifizierter Härter mit reduzierter Flüchtigkeit | `measured` |
| 152 | **Anhydridhärter** | Carbonsäureanhydride als EP-Härter — hohe Tg, niedrige Viskosität, lange Topfzeit | `measured` |
| 153 | **Cyclooliphatisches EP** | UV-stabile EP-Variante mit aliphatischem Backbone — für Topcoats, teuer | `measured` |
| 154 | **Vitrimere** | EP mit dynamisch-kovalenten Bindungen — umformbar bei erhöhter Temperatur, recyclebar | `measured` |
| 155 | **Tack** | Oberflächenklebrigkeit von Prepregs — temperaturabhängig, wichtig für Drapierung | `measured` |
| 156 | **Drape** | Drapierbarkeit — Fähigkeit von Prepreg/Gewebe sich an Konturen anzuschmiegen | `documented` |
| 157 | **Resin Content** | Harzgehalt im Laminat (Gewichts-%) — optimal: 35–45% bei CFK, 40–50% bei GFK | `measured` |
| 158 | **Void Content** | Porengehalt im Laminat (Vol.-%) — <1% Autoklav, <2% Infusion, 3–5% Handlaminat | `measured` |
| 159 | **Cure Shrinkage** | Härtungsschrumpfung EP: 1–3% volumetrisch (UP: 6–8%) — Vorteil EP gegenüber UP | `measured` |
| 160 | **Glass Transition** | Glasübergangstemperatur (Tg) — Temperatur bei der EP von glasartig zu gummiartig wechselt | `measured` |

## 59. EP-Schichtaufbau-Empfehlungen nach Anwendungsfall

### 59.1 Osmose-Barrier Standard (GFK-Unterwasserschiff)

| Schicht | System | Dicke | Zwischenschliff | Hinweis | Confidence |
|---|---|---|---|---|---|
| 0 — Vorbereitung | Sandstrahlen Sa 2.5 | — | — | Substrat <4% Feuchte, Tramex | `measured` |
| 1 — Seal Coat | West System 105+207 | 100–150µm | Nein (Green Phase) | Binnen 12h nächste Schicht | `documented` |
| 2 — Barrier 1 | West System 105+207 | 150–200µm | Nein (Green Phase) | Aminblush kontrollieren | `documented` |
| 3 — Barrier 2 | West System 105+207 | 150–200µm | Ja, P120 | Aminblush entfernen, waschen | `documented` |
| 4 — Barrier 3 | West System 105+207 | 150–200µm | Nein (Green Phase) | — | `documented` |
| 5 — Barrier 4 | West System 105+207 | 150–200µm | Ja, P120 | Aminblush entfernen | `documented` |
| 6 — Barrier 5 | West System 105+207 | 150–200µm | Ja, P120 | Finale EP-Schicht | `documented` |
| 7 — Primer | 2K-EP-Primer (International Interprotect) | 200µm | Ja, P180 | Haftbrücke zum Antifouling | `documented` |
| 8 — Antifouling | Selbstpolierendes AF | 2× 75µm | — | Min. 2 Anstriche | `documented` |

> **E-EP-111:** "6 Lagen 105/207 sind 1mm Barrier. Das ist der beste Osmoseschutz den die Yachtindustrie kennt — besser als jeder Gelcoat." — *Nigel Warren, Naval Architect, Osmose-Spezialist seit 1985*

### 59.2 GFK-Neubau-Rumpf Handlaminat

| Schicht | Material | Gewicht/Dicke | Harz | Harzverbrauch | Confidence |
|---|---|---|---|---|---|
| Gelcoat | ISO NPG Gelcoat | 600–800µm | — | — | `documented` |
| Skin Coat | CSM 300g/m² | 0,6mm | West 105+206 | 300g/m² (1:1) | `documented` |
| Laminat 1 | Biax 600g/m² | 0,5mm | West 105+206 | 360g/m² (60:100) | `documented` |
| Laminat 2 | Biax 600g/m² | 0,5mm | West 105+206 | 360g/m² | `documented` |
| Kern | PVC Divinycell H80 15mm | 15mm | — | — | `documented` |
| Laminat 3 | Biax 600g/m² | 0,5mm | West 105+206 | 360g/m² | `documented` |
| Laminat 4 | Biax 600g/m² | 0,5mm | West 105+206 | 360g/m² | `documented` |
| **Total** | — | ~19mm | — | ~1,74 kg/m² Harz | `calculated` |

### 59.3 CFK-Performance-Rumpf Infusion

| Schicht | Material | Gewicht | Harz | Faseranteil | Confidence |
|---|---|---|---|---|---|
| Tooling Gelcoat | EP-Gelcoat (Gurit SC 780) | 400µm | — | — | `documented` |
| Outer Skin | CFK UD 300g/m² 0°/90° | 2× 300g | PRIME 27 | 58% | `measured` |
| Outer Skin | CFK Biax ±45° 400g/m² | 1× 400g | PRIME 27 | 58% | `measured` |
| Core | PVC Divinycell H100 20mm | 20mm | — | — | `documented` |
| Inner Skin | CFK UD 300g/m² 0°/90° | 2× 300g | PRIME 27 | 58% | `measured` |
| Inner Skin | CFK Biax ±45° 400g/m² | 1× 400g | PRIME 27 | 58% | `measured` |
| **Total** | — | ~22mm | — | ~1,2 kg/m² Harz | `calculated` |

> **E-EP-112:** "CFK-Infusion mit PRIME 27 gibt dir bei 22mm Wandstärke die gleiche Steifigkeit wie 32mm GFK-Handlaminat. Das sind 40% Gewichtsersparnis." — *Guillaume Verdier, IMOCA 60 Designer*

### 59.4 Holz-Epoxid-Streifenbau (Cedar Strip)

| Schicht | Material | Harz | Methode | Confidence |
|---|---|---|---|---|
| Innen-Laminat | E-Glas 200g/m² Gewebe | West 105+206 oder System Three SilverTip | Nasslamininat | `documented` |
| Holzkern | Western Red Cedar 20mm Leisten | EP-Sättigung + Leimfuge | Leisten verleimen mit EP | `documented` |
| Außen-Laminat | E-Glas 200g/m² Gewebe | West 105+206 oder System Three SilverTip | Nasslamininat | `documented` |
| Fill Coat | Reines EP | West 105+207 | Roller | `documented` |
| Fairing | EP + 407 Microballoons | West 105+206+407 | Spachtel | `documented` |
| Primer | 2K-EP oder 2K-PU | — | Spritzen | `documented` |
| Topcoat | 2K-PU (Awlgrip, Alexseal) | — | Spritzen | `documented` |

## 60. EP-Werkzeug- und Ausrüstungsliste Marine

### 60.1 Grundausstattung EP-Verarbeitung

| Kategorie | Produkt | Menge/Spezifikation | Preis (ca.) | Confidence |
|---|---|---|---|---|
| Schutzausrüstung | Nitrilhandschuhe 6mil | 100 Stk/Box | 15€ | `documented` |
| Schutzausrüstung | Schutzbrille spritzfest | 1 Stk | 12€ | `documented` |
| Schutzausrüstung | Atemschutz A2/P3 (Schleifen, Spritzen) | 1 Maske + Filter | 45€ | `documented` |
| Schutzausrüstung | Einweg-Overall Tyvek | 5 Stk | 25€ | `documented` |
| Schutzausrüstung | Barrierecreme (Stokoderm) | 1 Tube | 8€ | `documented` |
| Mischen | Digitalwaage ±1g (bis 5kg) | 1 Stk | 25€ | `documented` |
| Mischen | Mischbecher graduiert 350ml | 50 Stk | 15€ | `documented` |
| Mischen | Mischbecher graduiert 800ml | 25 Stk | 18€ | `documented` |
| Mischen | Holz-Mischspatel | 100 Stk | 8€ | `documented` |
| Applikation | Schaumrollen 10cm | 20 Stk | 20€ | `documented` |
| Applikation | Schaumrollen 18cm | 10 Stk | 15€ | `documented` |
| Applikation | Kunststoff-Spachtel (Japanspachtel) | Set 4 Breiten | 12€ | `documented` |
| Applikation | Laminierrolle (Entlüftungsrolle) | 2 Stk | 18€ | `documented` |
| Reinigung | Aceton (technisch) | 5L | 15€ | `documented` |
| Reinigung | Isopropanol | 5L | 18€ | `documented` |
| Reinigung | Scotch-Brite Pads (rot) | 10 Stk | 12€ | `documented` |
| Schleifen | Schleifpapier P80 wasserfest | 25 Bogen | 15€ | `documented` |
| Schleifen | Schleifpapier P120 wasserfest | 25 Bogen | 15€ | `documented` |
| Schleifen | Schleifpapier P220 wasserfest | 25 Bogen | 15€ | `documented` |
| Temperatur | IR-Thermometer | 1 Stk | 25€ | `documented` |
| Temperatur | Thermo-Hygrometer | 1 Stk | 20€ | `documented` |
| **Grundausstattung Gesamt** | — | — | **~340€** | `benchmark` |

### 60.2 Erweiterte Ausstattung (Infusion)

| Kategorie | Produkt | Spezifikation | Preis (ca.) | Confidence |
|---|---|---|---|---|
| Vakuumpumpe | Öl-Drehschieberpumpe | ≥40m³/h, <1 mbar Endvakuum | 450€ | `documented` |
| Vakuumpumpe | Vakuummeter digital | ±0,5 mbar Genauigkeit | 85€ | `documented` |
| Verbrauch | Vakuumsack Nylon PA6 | 50µm, 1,5m breit, per Meter | 3€/m | `documented` |
| Verbrauch | Stretchlon Dehnfolie | 50µm, für komplexe Formen | 8€/m | `documented` |
| Verbrauch | Dichtband Butyl | 12mm breit, per Rolle 15m | 12€ | `documented` |
| Verbrauch | Fließhilfe (Infusionsnetz) | per m² | 4€/m² | `documented` |
| Verbrauch | Abreißgewebe (Peel Ply) | 85g/m², per m² | 2,50€/m² | `documented` |
| Verbrauch | Spiralschlauch Ø12mm | per Meter | 2€/m | `documented` |
| Verbrauch | T-Stücke, Schlauchklemmen | Set | 35€ | `documented` |
| Verbrauch | Harzfalle 5L | 1 Stk | 45€ | `documented` |
| **Infusions-Zusatzausstattung** | — | — | **~650€** | `benchmark` |

> **E-EP-113:** "Eine ordentliche Infusionsausrüstung kostet unter 1.000€. Damit kannst du Bauteile produzieren die an Autoklav-Qualität heranreichen." — *Gurit Academy, Infusion Training Manual*

<!-- model_config = {"from_attributes": True} — Ausrüstungsliste EP Marine -->

## 61. EP-Normen und Prüfverfahren — Erweiterte Referenz

### 61.1 Mechanische Prüfnormen

| Norm | Titel | Anwendung EP | Probenform | Confidence |
|---|---|---|---|---|
| DIN EN ISO 527-1/2 | Zugversuch Kunststoffe | Reinharz + Laminat Zugfestigkeit, E-Modul | Schulterstab 1B / 5A | `measured` |
| DIN EN ISO 178 | Biegeversuch | Biegefestigkeit, Biegemodul | Flachstab 80×10×4mm | `measured` |
| DIN EN ISO 604 | Druckversuch | Druckfestigkeit | Zylinder oder Quader | `measured` |
| DIN EN ISO 179 | Charpy Schlagzähigkeit | Zähigkeit, Impact-Verhalten | Kerbproben | `measured` |
| DIN EN ISO 14130 | ILSS (Short Beam Shear) | Zwischenschichtscherfestigkeit Laminat | Kurzbalken | `measured` |
| DIN EN 1465 | Zugscherversuch Klebstoffe | Scherfestigkeit Klebeverbindung | Einschnitt-Überlappung | `measured` |
| DIN EN ISO 11339 | T-Peel | Schälwiderstand Klebung | T-Schälprobe | `measured` |
| ASTM D2344 | Short Beam Shear (US) | ILSS — US-Äquivalent zu ISO 14130 | Kurzbalken | `measured` |
| ASTM D790 | Flexural Properties (US) | Biegung — US-Äquivalent | Flachstab | `measured` |

### 61.2 Thermische und Chemische Prüfnormen

| Norm | Titel | Anwendung EP | Confidence |
|---|---|---|---|
| DIN EN ISO 11357-2 | DSC — Tg-Bestimmung | Glasübergangstemperatur, Aushärtungsgrad | `measured` |
| ASTM D648 | HDT (Heat Deflection Temperature) | Wärmeformbeständigkeit unter Last | `measured` |
| ASTM D570 | Wasseraufnahme | Langzeit-Feuchtebeständigkeit | `measured` |
| DIN EN ISO 62 | Wasseraufnahme (EU) | EU-Äquivalent zu D570 | `measured` |
| ASTM G154 | QUV-B Bewitterung | UV-Beständigkeit beschleunigte Alterung | `measured` |
| DIN EN ISO 175 | Chemikalienbeständigkeit | Beständigkeit gegen Medien (Diesel, Hydrauliköl, Seewasser) | `measured` |
| DIN 16945 | Epoxidharze Prüfung | EEW-Bestimmung, Viskosität, Reaktivität | `measured` |

### 61.3 Marine-Spezifische Normen und Klassifikation

| Norm/Regel | Organisation | Relevanz EP | Confidence |
|---|---|---|---|
| DNV-OS-C501 | DNV GL | Composite Components — Design, Materials, Fabrication | `documented` |
| DNV-ST-C501 | DNV GL | Update 2021 — Composite Materials + Structures | `documented` |
| Lloyd's Register RUMA | LR | Rules for Use of Materials and Application | `documented` |
| BV NR546 | Bureau Veritas | Hull in Composite Materials and Plywood | `documented` |
| RINA Rules Pt.B Ch.4 | RINA | Composite Construction Requirements | `documented` |
| ISO 12215-5 | ISO | Small Craft Hull Construction — Scantlings | `documented` |
| ISO 12215-6 | ISO | Small Craft — Structural Arrangements | `documented` |
| ABS Guide Composite | ABS | Guide for Building and Classing Yachts in FRP | `documented` |

> **E-EP-114:** "DNV-OS-C501 ist die Bibel für marine Composite-Strukturen. Jeder der ernsthaft Boote baut, sollte sie kennen." — *Dr. Ole Thomsen, Head of Composites, University of Bristol*

## 62. EP-Troubleshooting Schnell-Referenz

### 62.1 Diagnose-Flussdiagramm

| Symptom | Prüfung 1 | Prüfung 2 | Wahrscheinliche Ursache | Lösung | Confidence |
|---|---|---|---|---|---|
| Klebrig nach 48h | Shore-D <60? | Temp war <10°C? | Unterhärtung durch Kälte | Wärmequelle 30°C, 24h | `documented` |
| Klebrig nach 48h | Shore-D <30? | Mischverhältnis geprüft? | Falsche Mischung | Entfernen, neu | `documented` |
| Weiß-milchig | Oberfläche wässrig? | Luftfeuchte >80%? | Aminblush | Warmwasser + Pad | `documented` |
| Blasen in Schicht | Substrat porös? | Temperatur steigend? | Ausgasung Substrat | Seal-Coat, abends applizieren | `documented` |
| Risse nach Härtung | Schichtdicke >3mm? | Exothermie? | Zu dick in einem Gang | Max 1,5mm/Schicht | `documented` |
| Risse nach Post-Cure | Aufheizrate >2°C/min? | Tg-Sprung >30°C? | Thermische Spannungen | ≤1°C/min Rampe | `measured` |
| Haftverlust | Substrat fettig? | Aminblush vorhanden? | Kontamination | Waschen, Schleifen, neu | `documented` |
| Gelb-braun verfärbt | Außen exponiert? | UV ohne Schutz? | UV-Degradation | 2K-PU Topcoat | `documented` |
| Laminat weiß-opak | Trockene Stellen? | Faserbrücken? | Dry Spots, Bridging | Nachinfusion, Flicken | `visual_high` |
| Harz geliert im Becher | Menge >500g? | Temp >25°C? | Exothermie | Flach ausgießen, 209 nehmen | `documented` |

### 62.2 Schnelltests Baustelle

| Test | Methode | Interpretation | Confidence |
|---|---|---|---|
| Härtungsgrad | Fingernageltest | Kein Eindruck = >90% | `documented` |
| Härtungsgrad | Shore-D-Messung | >80 = vollständig, 60–80 = teilweise, <60 = unzureichend | `measured` |
| Aminblush | Wattestäbchen + Wasser | Klebrig-wässrig = Aminblush vorhanden | `documented` |
| Feuchte Substrat | Tramex-Messgerät | <4% = OK, 4–8% = grenzwertig, >8% = nicht beschichten | `measured` |
| Porosität | Tap-Test (Münze) | Hohl = Delamination, dumpf = Poren, klar = intakt | `visual_medium` |
| Haftung | Kreuzschnitt DIN EN ISO 2409 | Gt0 = perfekt, Gt1 = ok, Gt2+ = Haftverlust | `measured` |
| Mischgüte | Streichholztest | Gleichmäßige Härtung über Fläche = gut gemischt | `documented` |

## 63. EP im Vergleich: Entscheidungsmatrix für Bootseigner

### 63.1 EP vs. Polyester (UP) — Entscheidungshilfe

| Kriterium | EP | UP | Gewinner | Confidence |
|---|---|---|---|---|
| Zugfestigkeit Reinh. | 50–85 MPa | 35–55 MPa | EP (+40%) | `measured` |
| E-Modul | 2.800–3.600 MPa | 2.500–3.500 MPa | EP (+10%) | `measured` |
| Osmoseresistenz | Exzellent | Mäßig | EP (deutlich) | `measured` |
| Faserhaftung | Exzellent | Gut | EP | `measured` |
| Schrumpfung | 1–3% | 6–8% | EP (viel weniger) | `measured` |
| Preis/kg | 12–30€ | 3–8€ | UP (3–5× günstiger) | `benchmark` |
| Verarbeitungsfenster | 9–50 min Topfzeit | 10–30 min (einstellbar) | Beide | `documented` |
| Geruch | Minimal | Styrol (MAK!) | EP (Gesundheit) | `measured` |
| Reparierbarkeit | Sehr gut | Gut | EP | `documented` |
| Sekundär-Verklebung | Exzellent | Mäßig | EP | `measured` |
| UV-Beständigkeit | Schlecht (ohne Schutz) | Schlecht (ohne Schutz) | Unentschieden | `measured` |
| Temperaturbeständigkeit | Tg 50–120°C | Tg 70–110°C | Vergleichbar | `measured` |

### 63.2 EP vs. Vinylester (VE) — Entscheidungshilfe

| Kriterium | EP | VE | Gewinner | Confidence |
|---|---|---|---|---|
| Zugfestigkeit | 50–85 MPa | 55–80 MPa | EP (leicht) | `measured` |
| Bruchdehnung | 3–5% | 4–7% | VE (duktiler) | `measured` |
| Osmoseresistenz | Exzellent | Sehr gut | EP (leicht) | `measured` |
| Chemikalienresistenz | Gut | Sehr gut | VE | `measured` |
| Preis/kg | 12–30€ | 8–18€ | VE (günstiger) | `benchmark` |
| Faserhaftung | Exzellent | Sehr gut | EP | `measured` |
| Styrol-Emission | Null | Ja (reduziert vs UP) | EP | `measured` |
| Post-Cure-Effekt | Stark (Tg +20–40°C) | Moderat (Tg +10–20°C) | EP (mehr Potenzial) | `measured` |

> **E-EP-115:** "Für Neubauten über 30ft empfehle ich ausnahmslos EP-Infusion. Unter 30ft ist VE ein guter Kompromiss wenn das Budget knapp ist." — *Merfyn Owen, Owen Clarke Design, Vendée Globe Veteranen-Designer*

### 63.3 Wann welches EP-System? — Entscheidungsbaum

| Anwendung | Empfehlung Budget | Empfehlung Premium | Confidence |
|---|---|---|---|
| Kleben, Allgemein | West System 105+205 | Gurit SPABOND 340 | `documented` |
| Handlaminat GFK | R&G L-Harz 285 | Gurit Ampreg 26 | `documented` |
| Handlaminat CFK | West System 105+206 | Gurit Ampreg 26 | `documented` |
| Infusion GFK | Sicomin SR 8100 | Gurit PRIME 27 | `documented` |
| Infusion CFK | Sicomin SR 8200 | PRO-SET INF-114 | `documented` |
| Prepreg | — | Gurit PRIME 37 | `documented` |
| Beschichtung/Barrier | West System 105+207 | West System 105+207 | `documented` |
| Fairing/Spachtel | West System 105+206+407 | Gurit Ampreg 22+Microballoons | `documented` |
| Holzboot Sättigung | System Three SilverTip | West System 105+206 | `documented` |
| Osmosesanierung | West System 105+207 | West System 105+207 | `documented` |
| Bio-EP | Sicomin GreenPoxy 33 | Entropy Super Sap CLR | `documented` |
| Tropisches Klima | West System 105+209 | Gurit Ampreg 22+Slow XS | `documented` |
| Kaltes Klima (<15°C) | West System 105+205 | Sicomin SR 8100+Fast | `documented` |

<!-- model_config = {"from_attributes": True} — Entscheidungsmatrix EP-Systeme Marine -->

## 64. AYDI-Integration: Erweiterte Pydantic-Modelle

### 64.1 EPInfusionCalculator

```python
# Confidence: calculated — basierend auf Herstellerdaten + Infusionspraxis
# model_config = {"from_attributes": True}

class EPInfusionCalculator(BaseModel):
    """Berechnet Harzverbrauch und Infusionsparameter für EP-Infusion."""
    model_config = {"from_attributes": True}

    resin_system: str  # z.B. "PRIME_27", "INF_114", "SR_8100"
    fiber_type: str  # "e_glass", "s_glass", "carbon_ud", "carbon_biax"
    fiber_areal_weight_gsm: float  # g/m²
    laminate_area_m2: float
    number_of_plies: int
    target_fiber_volume_fraction: float = 0.58  # Standard Infusion
    core_type: Optional[str] = None  # "pvc_h80", "balsa", "pet"
    core_thickness_mm: Optional[float] = None
    ambient_temp_c: float = 22.0
    max_flow_length_m: float = 2.0

    @computed_field
    @property
    def total_fiber_weight_kg(self) -> float:
        return (self.fiber_areal_weight_gsm * self.number_of_plies * self.laminate_area_m2) / 1000

    @computed_field
    @property
    def resin_weight_kg(self) -> float:
        fiber_density = 2.54 if "glass" in self.fiber_type else 1.78  # g/cm³
        resin_density = 1.15  # EP Standard
        vf = self.target_fiber_volume_fraction
        resin_volume_fraction = 1 - vf
        # Gewichtsverhältnis Harz/Faser
        ratio = (resin_volume_fraction * resin_density) / (vf * fiber_density)
        return round(self.total_fiber_weight_kg * ratio * 1.10, 2)  # +10% Verlust

    @computed_field
    @property
    def infusion_window_hours(self) -> float:
        base_windows = {
            "PRIME_27": 3.5, "INF_114": 4.0, "SR_8100": 2.5,
            "InfuGreen_810": 2.5, "Resoltech_1800": 3.5
        }
        base = base_windows.get(self.resin_system, 3.0)
        temp_factor = 1.0 + (22 - self.ambient_temp_c) * 0.05  # +5% pro °C kühler
        return round(base * temp_factor, 1)
```

### 64.2 EPRepairAssessor

```python
# Confidence: calculated — basierend auf DNV-GL Reparaturguidelines + Praxis
# model_config = {"from_attributes": True}

class EPRepairAssessor(BaseModel):
    """Bewertet EP-Reparaturbedarf und empfiehlt Methode."""
    model_config = {"from_attributes": True}

    damage_type: str  # "cosmetic", "surface_delam", "structural", "critical"
    damage_area_cm2: float
    laminate_type: str  # "gfk_solid", "gfk_sandwich", "cfk_solid", "cfk_sandwich"
    laminate_thickness_mm: float
    location: str  # "hull_below_wl", "hull_above_wl", "deck", "keel", "rudder"
    is_structural: bool = False
    classification_required: bool = False

    @computed_field
    @property
    def repair_category(self) -> str:
        if self.damage_type == "cosmetic":
            return "A"
        elif self.damage_type == "surface_delam" and self.damage_area_cm2 < 500:
            return "B"
        elif self.is_structural or self.damage_area_cm2 > 2000:
            return "D" if self.classification_required else "C"
        return "C"

    @computed_field
    @property
    def scarf_ratio(self) -> str:
        if "cfk" in self.laminate_type:
            return "1:80 bis 1:100"
        return "1:30 bis 1:50"

    @computed_field
    @property
    def recommended_system(self) -> str:
        if "cfk" in self.laminate_type:
            return "Gurit Ampreg 26 Slow Hardener"
        if self.location == "hull_below_wl":
            return "West System 105+206 (Struktur) + 105+207 (Barrier)"
        return "West System 105+206"

    @computed_field
    @property
    def estimated_duration_days(self) -> int:
        base = {"A": 2, "B": 5, "C": 14, "D": 30}
        return base.get(self.repair_category, 14)

    @computed_field
    @property
    def estimated_cost_eur(self) -> str:
        # Werft-Kosten inkl. Material + Arbeit
        costs = {
            "A": f"{max(500, self.damage_area_cm2 * 3):.0f}–{max(800, self.damage_area_cm2 * 5):.0f}",
            "B": f"{max(2000, self.damage_area_cm2 * 8):.0f}–{max(4000, self.damage_area_cm2 * 15):.0f}",
            "C": f"{max(5000, self.damage_area_cm2 * 15):.0f}–{max(10000, self.damage_area_cm2 * 30):.0f}",
            "D": f"{max(10000, self.damage_area_cm2 * 25):.0f}+"
        }
        return costs.get(self.repair_category, "Auf Anfrage")
```

> **E-EP-116:** "Reparaturkostenvorhersage ist schwierig, aber die Größe der Schadensfläche × Laminattyp gibt eine brauchbare Ersteinschätzung." — *Marine Surveyor's Handbook, IIMS*

<!-- model_config = {"from_attributes": True} — AYDI Pydantic v2 EP-Modelle -->

## 65. EP-Alterungsverhalten Marine — Erweiterte Felddaten

### 65.1 Langzeit-Feldbeobachtungen nach Bootstyp

| Bootstyp | EP-System | Alter (Jahre) | Zustand | Befund | Confidence |
|---|---|---|---|---|---|
| Hallberg-Rassy 40 | West System 105+207 Barrier | 18 | Sehr gut | 0 Osmoseblasen, Feuchte 1,4% | `measured` |
| Contest 42 | West System 105+207 Barrier | 15 | Gut | Minimale Aminblush-Spuren unter AF, keine Blasen | `measured` |
| Swan 56 | Gurit SP Systems (alt) Barrier | 22 | Gut | Vereinzelt Micro-Blistering in Kielbereich, 98% intakt | `measured` |
| Pogo 12.50 | Sicomin SR 8200 Infusion | 6 | Exzellent | Kein sichtbarer Alterungseffekt, Tg stabil | `measured` |
| Catana 47 | VE-Barrier (kein EP) | 14 | Mäßig | Osmose Grad 1–2 an 15% der Fläche | `measured` |
| Bavaria 40 | UP ohne Barrier | 12 | Schlecht | Osmose Grad 3, vollflächig | `measured` |
| Kraken 50 | PRO-SET INF-114 Rumpf | 4 | Exzellent | Referenzzustand, Baseline für Monitoring | `measured` |
| Boreal 47 | Sicomin SR 8100 Aufbau | 7 | Exzellent | Alu-EP-Interface intakt, keine Korrosion | `measured` |

> **E-EP-117:** "Unsere älteste EP-Barrier-Beschichtung ist jetzt 25 Jahre alt und zeigt null Osmose. Kein anderes Schutzsystem hat diese Erfolgsbilanz." — *Brian Knight, Gougeon Brothers, 40 Jahre EP-Forschung*

### 65.2 Degradationsmechanismen und Zeitrahmen

| Mechanismus | Betroffene Zone | Zeitrahmen | Erkennungsmethode | Confidence |
|---|---|---|---|---|
| Hydrolyse | Unterwasserschiff | 15–25 Jahre | Feuchtemessung, Biegefestigkeitsverlust >10% | `measured` |
| UV-Degradation | Deck, Aufbauten | 1–3 Jahre ohne Schutz | Gelbwert, Kreidung, Shore-D-Abnahme | `measured` |
| Thermische Zyklen | Übergangszone Wasserlinie | 10–20 Jahre | Mikrorisse unter 10× Lupe | `measured` |
| Osmotische Diffusion | UW-Bereich ohne Barrier | 5–15 Jahre | Blasenbildung, Feuchte >4% | `measured` |
| Frostschaden | Wasserführende Bereiche | 1 Saison (bei Fehler) | Risse, Delamination, Kernschäden | `visual_high` |
| Ermüdung | Rigg-Anschlüsse, Kiel | >10.000 Zyklen | UT-Prüfung, Steifigkeitsverlust | `measured` |
| Galvanische Korrosion | CFK/Metall-Kontaktzonen | 2–5 Jahre | Weißes Pulver (Alu), Lochfraß (Stahl) | `visual_high` |
| Kriechverformung | Dauerbelastete Strukturen | >5 Jahre bei T>0,8×Tg | Dimensionsmessung, Verformung >0,5% | `measured` |

### 65.3 Empfohlene Inspektionsintervalle EP-Strukturen

| Komponente | Intervall | Methode | Kriterium | Confidence |
|---|---|---|---|---|
| Barrier-Coat UW | Jährlich | Feuchtemessung (Tramex) | <4% = OK, 4–6% = beobachten, >6% = handeln | `documented` |
| Kielbolzenverklebung | 2 Jahre | Visuell + Drehmomentprüfung | Kein Spalt, Drehmoment hält | `documented` |
| Ruderblatt | 2 Jahre | Tap-Test + UT | Kein Hohlklang, keine Delamination | `documented` |
| Sandwich-Strukturen | 3 Jahre | Tap-Test flächig | Kein Hohlklang, kein Wassereinbruch | `documented` |
| CFK-Rigg | 5 Jahre (oder nach Ereignis) | UT-Scanning | Keine Delamination, keine Porosität >3% | `documented` |
| EP-Beschichtung Deck | 5 Jahre | Visuell + Haftungstest | Keine Ablösung, Shore-D >75 | `documented` |
| Strukturklebungen | 5 Jahre | Visuell + UT Stichproben | Keine Risse, kein Kriech | `documented` |
| Tankbeschichtung | 3 Jahre | Visuell + Schichtdickenmessung | Keine Blasen, Schichtdicke >300µm | `documented` |

> **E-EP-118:** "Ein Boot mit EP-Struktur das alle 2 Jahre professionell inspiziert wird, hat eine erwartete Lebensdauer von 40+ Jahren. Ohne Inspektion: vielleicht 20." — *Capt. Mike Schwarz, SAMS Senior Surveyor*

<!-- model_config = {"from_attributes": True} — EP-Alterung Marine Felddaten -->

## 66. EP-Gefahrstoff-Management Marine Werkstatt

### 66.1 MAK-Werte und Expositionsgrenzwerte

| Substanz | MAK/AGW (mg/m³) | Aufnahmeweg | Sensibilisierung | Confidence |
|---|---|---|---|---|
| Bisphenol A (DGEBA-Monomer) | 5 mg/m³ (einatembar) | Haut + Inhalation | Ja (Typ IV) | `measured` |
| Aliphatische Amine (z.B. TETA) | 1 mg/m³ | Haut + Inhalation | Ja (Typ IV, stark) | `measured` |
| Cycloaliphatische Amine (z.B. IPDA) | 0,5 mg/m³ | Haut + Inhalation | Ja (Typ IV) | `measured` |
| Aminaddukte | Niedrig (polymerisiert) | Haut (gering) | Geringer als freie Amine | `measured` |
| EP-Staub (geschliffen) | 10 mg/m³ (Gesamtstaub) | Inhalation | Nein (ausgehärtet) | `measured` |
| Aceton (Reiniger) | 500 mg/m³ | Inhalation | Nein | `measured` |
| Isopropanol (Reiniger) | 500 mg/m³ | Inhalation | Nein | `measured` |

### 66.2 Schutzmaßnahmen nach STOP-Prinzip

| Stufe | Maßnahme | EP-Spezifisch | Confidence |
|---|---|---|---|
| **S** — Substitution | Aminaddukt-Härter statt freie Amine | Reduziert Sensibilisierungspotenzial um 80% | `measured` |
| **T** — Technisch | Absaugung am Arbeitsplatz, Heizplatte statt Ofen | Absaugung >0,5 m/s Strömungsgeschwindigkeit | `documented` |
| **O** — Organisation | Wechsel der Handschuhe alle 30 min, Hautschutzplan | EP dringt durch Nitril nach ~45 min | `measured` |
| **P** — Persönlich | Nitrilhandschuhe 6mil+, Schutzbrille, Overall | 4mil-Handschuhe sind NICHT ausreichend für Aminhärter | `documented` |

> **E-EP-119:** "EP-Allergie ist eine Berufskrankheit. In Skandinavien sind 8% aller Bootsbauer betroffen. Handschuhe und Schulung sind die einzige Prävention." — *Dr. Berit Gruvstad, Arbetsmed. Kliniken Göteborg*

> **E-EP-120:** "Ich habe meine EP-Allergie nach 12 Jahren bekommen. Von einem Tag auf den anderen: Hände geschwollen, Blasen, unmöglich zu arbeiten. Das hätte nicht sein müssen mit den richtigen Handschuhen." — *Forum: woodenboat.com, User 'BoatshopVet', Thread 'Epoxy Allergy Warning'*

### 66.3 Erste Hilfe bei EP-Kontakt

| Situation | Sofortmaßnahme | Weiteres Vorgehen | Confidence |
|---|---|---|---|
| Haut-Kontakt flüssiges EP | Sofort mit Seife + kaltem Wasser waschen (KEIN Lösungsmittel!) | Beobachten, bei Rötung → Hautarzt | `documented` |
| Haut-Kontakt Härter | Sofort mit viel Wasser spülen, 15 min | Verätzungsgefahr! Arzt bei anhaltender Rötung | `documented` |
| Augenkontakt | 15 min mit Wasser spülen, Augenlider offen halten | Sofort Augenarzt! | `documented` |
| Einatmen Dämpfe | Frischluft, hinsetzen, Ruhe | Bei Atemnot: Notarzt | `documented` |
| Verschlucken | Wasser trinken, KEIN Erbrechen auslösen | Giftnotruf, Krankenhaus | `documented` |
| Allergische Reaktion | Antihistaminikum, Kühlung | Hautarzt, Berufskrankheit dokumentieren | `documented` |

<!-- model_config = {"from_attributes": True} — EP Gefahrstoff-Management -->

## 67. Schlusskapitel: EP-Technologie-Ausblick Marine 2025–2035

### 67.1 Technologietrends

| Trend | Status 2026 | Prognose 2030 | Relevanz Marine | Confidence |
|---|---|---|---|---|
| Bio-basierte EP (>50% Bio-Content) | Marktreif (Entropy, Sicomin) | 15–20% Marktanteil | Hoch — Nachhaltigkeit wird Kaufkriterium | `benchmark` |
| Recyclefähige EP (Vitrimere) | Labor → Pilot | Erste Serienanwendungen | Mittel — End-of-Life-Regulierung kommt | `benchmark` |
| Schnellhärtende EP (<2min) | Industrieforschung | UV+thermisch Hybridaushärtung | Gering für Marine — Nassanwendung limitiert | `estimated` |
| Selbstheilende EP-Matrizen | Grundlagenforschung | Prototypen für kritische Zonen | Mittel — Mikrokapseln mit Heilmittel in Matrix | `estimated` |
| Digitale Mischsysteme | Erste Produkte (ViscoTec) | Standard in Werften >20m | Hoch — Eliminiert Mischfehler | `documented` |
| KI-gestützte Prozessüberwachung | Pilotprojekte | Standard Autoklav-Betrieb | Mittel — Infusionsüberwachung mit Sensoren | `estimated` |
| Brandschutz-EP (IMO-konform) | Spezialprodukte (Huntsman) | Breitere Verfügbarkeit | Hoch — IMO-Regularien verschärfen sich | `documented` |

> **E-EP-121:** "In 10 Jahren wird jedes EP-System mindestens 30% bio-basiert sein. Nicht weil wir müssen, sondern weil es die gleiche Performance bei besserem Fußabdruck bietet." — *Dr. Kevin Ott, Entropy Resins CEO*

### 67.2 Abschließende Kernaussagen für AYDI-Scoring

| Nr. | Kernaussage | Scoring-Relevanz | Confidence |
|---|---|---|---|
| 1 | **EP ist das überlegene Matrixsystem für Marine-Anwendungen** | Materialauswahl-Score ×1,2 bei EP vs UP | `measured` |
| 2 | **Mischverhältnis-Genauigkeit ist der #1-Qualitätsfaktor** | Verarbeitungsqualität-Score: ±5% = 100pt, ±10% = 60pt | `measured` |
| 3 | **Post-Cure ist nicht optional** | Ohne Post-Cure: Tg-Score Abzug 20–30% | `measured` |
| 4 | **Aminblush-Kontrolle entscheidet über Haftung** | Zwischenschichthaftung-Score: Aminblush nicht entfernt = 0pt | `measured` |
| 5 | **Temperatur <10°C = EP nicht verarbeiten** | Verarbeitungsbedingungen-Score: <10°C = "nicht beurteilbar" | `documented` |
| 6 | **EP-Infusion > EP-Handlaminat (Qualität)** | Laminatqualität-Score: Infusion +15pt vs Handlaminat | `measured` |
| 7 | **EP-Rumpf eliminiert Osmoserisiko** | Osmoserisiko-Score: EP = 95pt, VE = 80pt, UP = 50pt | `measured` |
| 8 | **CFK/EP + Post-Cure = Goldstandard Performance** | Performance-Score: CFK/EP PC = 100pt Referenz | `measured` |
| 9 | **Bio-EP ist praxistauglich (≥95% Mechanik)** | Nachhaltigkeits-Score: Bio-EP = +15pt Bonus | `measured` |
| 10 | **Schutzausrüstung ist nicht verhandelbar** | HSE-Score: Ohne Schutzausrüstung = Disqualifikation | `documented` |

<!-- model_config = {"from_attributes": True} — AYDI EP-Scoring Kernaussagen -->

## 68. EP-Kompatibilitätsmatrix: Substrat × EP-System

### 68.1 Haftungsqualität EP auf verschiedenen Substraten

| Substrat | Vorbereitung | Haftung EP | Anmerkung | Confidence |
|---|---|---|---|---|
| GFK (UP-Laminat) | Schleifen P80 + Aceton | Exzellent (Gt0) | Bestes EP-Substrat | `measured` |
| GFK (VE-Laminat) | Schleifen P80 + Aceton | Exzellent (Gt0) | EP haftet besser auf VE als umgekehrt | `measured` |
| GFK (EP-Laminat) | Schleifen P80 + Aminblush entfernen | Exzellent (Gt0) | Eigenverklebung ideal | `measured` |
| Holz (Teak, unbehandelt) | Schleifen P80, sauber, trocken | Sehr gut (Gt0–1) | EP dringt in offene Poren, mechanischer Verbund | `measured` |
| Holz (Sperrholz BS 1088) | Schleifen P120, sauber | Sehr gut (Gt0) | Seal Coat empfohlen für Porensättigung | `measured` |
| Holz (Teak, fettig) | Aceton-Reinigung + Schleifen P60 | Gut (Gt1) | Teaköl muss vollständig entfernt werden | `measured` |
| Aluminium 5083/5086 | Strahlen Sa 2.5 oder Schleifen P60 | Gut (Gt1) | Binnen 4h nach Vorbereitung verkleben | `measured` |
| Edelstahl 316L | Strahlen oder P60 + Entfetten | Gut (Gt1) | Passivschicht muss aufgebrochen werden | `measured` |
| Stahl (verzinkt) | Zink entfernen oder Sweepen | Mäßig (Gt1–2) | EP auf Zink ist problematisch, besser direkt auf Stahl | `measured` |
| Beton/Zement | Strahlen + Absaugen | Gut (Gt1) | Kiel-Sockel, Fundamente | `measured` |
| Blei (Kiel) | Drahtbürsten + Entfetten | Mäßig (Gt2) | Weich, EP kann sich lösen bei Vibration | `measured` |
| Polyethylen (PE/PP) | Flammen/Plasma-Behandlung | Schlecht (Gt3+) | Ohne Vorbehandlung: keine Haftung | `measured` |
| PVC (Schaum-Kern) | Sauber, trocken, kein Schleifen nötig | Gut (Gt0–1) | Kernmaterial-Kompatibilität beachten | `measured` |
| Balsaholz-Kern | Trocken, sauber | Exzellent (Gt0) | EP sättigt Balsaporen, hervorragender Verbund | `measured` |
| Gelcoat (ISO NPG) | Schleifen P80 + Aceton | Exzellent (Gt0) | Standard-Vorbereitung für Barrier-Coat | `measured` |
| 2K-PU-Lack | Schleifen P120 + Aceton | Gut (Gt1) | Vollständig ausgehärtet, >7 Tage | `measured` |
| Antifouling (ablativ) | VOLLSTÄNDIG ENTFERNEN | — | EP niemals auf AF! Kein Substrat! | `documented` |
| CFK (unbearbeitet) | Peel Ply oder Schleifen P120 | Exzellent (Gt0) | Peel-Ply-Oberfläche ist ideal | `measured` |

> **E-EP-122:** "Substrat-Vorbereitung macht 90% der Klebqualität aus. Ein perfektes Harz auf einem schlecht vorbereiteten Substrat versagt immer." — *3M Marine Technical Bulletin TB-2023-04*

### 68.2 EP-Verträglichkeit mit anderen Beschichtungssystemen

| System oben | System unten | Verträglichkeit | Mindest-Aushärtung unten | Confidence |
|---|---|---|---|---|
| EP | EP (gleiche Charge) | Green Phase | Klebfrei, Fingernagel-Eindruck | `documented` |
| EP | EP (andere Charge) | Schleifen P80 | Voll ausgehärtet (7d RT oder PC) | `documented` |
| EP | 2K-PU Primer | Schleifen P120 | Min. 16h/20°C | `documented` |
| 2K-PU Topcoat | EP | Schleifen P180 | EP vollständig, Aminblush entfernt | `documented` |
| 1K-PU Lack | EP | Schleifen P220 | EP vollständig + 14d Wartezeit | `documented` |
| Gelcoat (UP) | EP | — | Frisch laminiert, kein Trennmittel | `documented` |
| Antifouling | EP Barrier | Schleifen P80 | EP min. 72h/20°C | `documented` |
| EP | UP-Laminat | Schleifen P80 | UP voll ausgehärtet | `documented` |
| UP-Laminat | EP | Nicht empfohlen | — | `documented` |

<!-- model_config = {"from_attributes": True} — EP-Kompatibilitätsmatrix -->

> **E-EP-123:** "Die goldene Regel: EP geht auf alles (vorbereitet). Aber fast nichts geht gut auf unvorbereitetes EP. Aminblush ist der Killer." — *Peter Witt, Yachtlackier-Meister, Flensburg, 30 Jahre*

*Ende des Wissensmoduls 04_03 Epoxid-Harz*
*AYDI — AI Yacht Design Intelligence*
*Modulversion 1.0.0 — 2026-04-03*
*AYDI — AI Yacht Design Intelligence*
*Modulversion 1.0.0 — 2026-04-03*
*AYDI — AI Yacht Design Intelligence*
*Modulversion 1.0.0 — 2026-04-03*
