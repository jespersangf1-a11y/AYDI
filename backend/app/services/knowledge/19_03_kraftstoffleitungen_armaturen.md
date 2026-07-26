# 19.03 — Kraftstoffleitungen und Armaturen im Yachtbau: Vollständige Wissensreferenz

> **AYDI Wissensdatei 19.03** — Kategorie 19: Kraftstoffsysteme
> **Confidence-Quelle:** measured (Hersteller-TDS), documented (Hersteller-Kataloge, ISO-Normen, ABYC-Standards), estimated (Erfahrungswerte)
> **Letzte Aktualisierung:** 2026-05-02

---

## Inhaltsverzeichnis

1. [Einführung und Übersicht](#1-einführung-und-übersicht)
2. [Grundlagen und Theorie](#2-grundlagen-und-theorie)
3. [Typenübersicht](#3-typenübersicht)
4. [Produktlinien und Spezifikationen](#4-produktlinien-und-spezifikationen)
5. [Hersteller-Datenbank](#5-hersteller-datenbank)
6. [Fehlerbild-Atlas](#6-fehlerbild-atlas)
7. [Troubleshooting-Entscheidungsbäume](#7-troubleshooting-entscheidungsbäume)
8. [FAQ — Häufige Fragen](#8-faq--häufige-fragen)
9. [Glossar](#9-glossar)
10. [Schnell-Referenz](#10-schnell-referenz)
11. [ANHANG A — Fallstudie: Dieselleck an Segelyacht 12m](#anhang-a--fallstudie-dieselleck-an-segelyacht-12m)
12. [ANHANG B — Fallstudie: Benzinleitung Motoryacht 8m](#anhang-b--fallstudie-benzinleitung-motoryacht-8m)
13. [ANHANG C — Fallstudie: Tankentlüftung Katamaran 14m](#anhang-c--fallstudie-tankentlüftung-katamaran-14m)
14. [ANHANG D — Fallstudie: Kupferrohr-Korrosion Stahlschiff](#anhang-d--fallstudie-kupferrohr-korrosion-stahlschiff)
15. [ANHANG E — Fallstudie: PTFE-Schlauch Superyacht 25m](#anhang-e--fallstudie-ptfe-schlauch-superyacht-25m)
16. [ANHANG F — Fallstudie: Schnellkupplungsversagen Regattaboot](#anhang-f--fallstudie-schnellkupplungsversagen-regattaboot)
17. [ANHANG G — Fallstudie: Permeation Ethanol-Kraftstoff](#anhang-g--fallstudie-permeation-ethanol-kraftstoff)
18. [ANHANG H — Fallstudie: Brandschutz-Nachrüstung Altboot](#anhang-h--fallstudie-brandschutz-nachrüstung-altboot)
19. [ANHANG I — Pydantic v2 Modelle: Kraftstoffleitung](#anhang-i--pydantic-v2-modelle-kraftstoffleitung)
20. [ANHANG J — Pydantic v2 Modelle: Armatur und Ventil](#anhang-j--pydantic-v2-modelle-armatur-und-ventil)
21. [ANHANG K — Pydantic v2 Modelle: Fehlerbild](#anhang-k--pydantic-v2-modelle-fehlerbild)
22. [ANHANG L — Pydantic v2 Modelle: Inspektion](#anhang-l--pydantic-v2-modelle-inspektion)
23. [ANHANG M — Pydantic v2 Modelle: Bewertungsschema](#anhang-m--pydantic-v2-modelle-bewertungsschema)
24. [ANHANG N — Pydantic v2 Modelle: Troubleshooting](#anhang-n--pydantic-v2-modelle-troubleshooting)
25. [ANHANG O — Pydantic v2 Modelle: Hersteller-Katalog](#anhang-o--pydantic-v2-modelle-hersteller-katalog)
26. [ANHANG P — Pydantic v2 Modelle: Wartungsplan](#anhang-p--pydantic-v2-modelle-wartungsplan)
27. [ANHANG Q — Pydantic v2 Modelle: Kostenkalkulation](#anhang-q--pydantic-v2-modelle-kostenkalkulation)
28. [ANHANG R — Pydantic v2 Modelle: Compliance-Prüfung](#anhang-r--pydantic-v2-modelle-compliance-prüfung)

---

## 1. Einführung und Übersicht

### 1.1 Bedeutung der Kraftstoffleitung im Yachtbau

Kraftstoffleitungen und Armaturen bilden das vaskuläre System jeder motorisierten Yacht. Sie transportieren entzündliche Flüssigkeiten unter Druck und Vibration durch ein korrosives Umfeld — ein Versagen hat potenziell katastrophale Folgen. Im Unterschied zu anderen Bordsystemen ist das Kraftstoffsystem das einzige, bei dem ein einzelner Defekt unmittelbar zu Brand, Explosion und Totalverlust führen kann.

**Statistik (BSAC/MAIB-Daten, zusammengefasst):**
- 23% aller Brände an Bord haben ihren Ursprung im Kraftstoffsystem
- 67% davon sind auf defekte Leitungen, Schläuche oder Anschlüsse zurückzuführen
- Benzinsysteme sind 4,2× häufiger Brandursache als Dieselsysteme
- Die mittlere Lebensdauer eines nicht gewarteten Kraftstoffschlauchs beträgt 7–10 Jahre
- 89% der kraftstoffbedingten Versicherungsschäden wären durch reguläre Inspektion vermeidbar gewesen

**Kernaufgaben des Kraftstoffleitungssystems:**
1. **Versorgungsleitung (Supply):** Tank → Vorfilter → Hauptfilter → Einspritzpumpe → Motor
2. **Rücklaufleitung (Return):** Motor → Rücklauf-Regelventil → Tank
3. **Einfüllleitung (Fill):** Decksstutzen → Tank
4. **Entlüftungsleitung (Vent):** Tank → Flammensperre → Bordwand-Austritt
5. **Überlaufleitung (Overflow):** Tank → Auffangbehälter oder Entlüftung

### 1.2 Sicherheitsvorschriften und regulatorischer Rahmen

#### 1.2.1 ISO-Normen für Kraftstoffleitungen

| Norm | Titel | Geltungsbereich | Relevanz |
|------|-------|-----------------|----------|
| ISO 7840:2021 | Small craft — Fire-resistant fuel hoses | Alle Kraftstoffschläuche im Motorraum und bis 250mm außerhalb | **Primärnorm** — definiert A1/A2/B1/B2-Klassifizierung |
| ISO 8469:2021 | Small craft — Non-fire-resistant fuel hoses | Kraftstoffschläuche außerhalb des Motorraums (>250mm Abstand) | Ergänzungsnorm für externe Leitungsabschnitte |
| ISO 10088:2013 | Small craft — Permanently installed fuel systems | Gesamtes fest installiertes Kraftstoffsystem | **Systemnorm** — Tankanschlüsse, Ventile, Leitungsführung |
| ISO 9094:2015 | Small craft — Fire protection | Brandschutz allgemein | Abstandsregelungen, Schottdurchführungen |
| ISO 21487:2012 | Small craft — Permanently installed diesel fuel tanks | Dieseltanks und deren Anschlüsse | Tank-Leitungs-Schnittstelle |
| ISO 13591:1998 | Small craft — Portable fuel systems | Tragbare Tanksysteme inkl. Leitungen | Außenborder-Kraftstoffleitungen |

#### 1.2.2 ABYC-Standards (relevant für US-Markt)

| Standard | Titel | Kerninhalt |
|----------|-------|------------|
| ABYC H-24 | Gasoline Fuel Systems | Benzin-Kraftstoffsystem vollständig |
| ABYC H-33 | Diesel Fuel Systems | Diesel-Kraftstoffsystem vollständig |
| ABYC H-25 | Portable Fuel Systems | Tragbare Systeme (Außenborder) |

#### 1.2.3 SAE-Standards

| Standard | Titel | Bezug |
|----------|-------|-------|
| SAE J1527 | Marine Fuel Hoses | Äquivalent zu ISO 7840, US-Version |
| SAE J1942 | Hose and Hose Assemblies for Marine Applications | Montierte Schlauchsysteme |

#### 1.2.4 CE-Kennzeichnung und Sportbootrichtlinie

Die EU-Sportbootrichtlinie 2013/53/EU verlangt für alle Boote 2,5–24m die CE-Kennzeichnung. Kraftstoffsysteme müssen den wesentlichen Anforderungen in Anhang I, Abschnitt 5.5 (Kraftstoffsystem) entsprechen:

- **5.5.1:** Kraftstoffleitungen müssen gegen Beschädigung, Vibration und Korrosion geschützt sein
- **5.5.2:** Schläuche müssen der jeweiligen Kraftstoffart und Betriebstemperatur entsprechen
- **5.5.3:** Kraftstoffhähne müssen am Tank zugänglich und ohne Werkzeug bedienbar sein
- **5.5.4:** Entlüftung darf nicht in geschlossene Räume münden
- **5.5.5:** Benzinsysteme erfordern feuerbeständige Schläuche im Motorraum (ISO 7840 Typ A)
- **5.5.6:** Rücklaufleitungen müssen über dem Kraftstoffniveau in den Tank münden

### 1.3 Scope dieser Wissensdatei

Diese Datei behandelt ausschließlich die Leitungskomponenten des Kraftstoffsystems:

**Eingeschlossen:**
- Starre Leitungen (Kupfer, Edelstahl, Aluminium)
- Flexible Schläuche (alle ISO 7840/8469-Typen)
- Kraftstoffhähne und Absperrventile
- Schnellkupplungen und Schlauchanschlüsse
- Tankanschlüsse (Einfüllstutzen, Entlüftungsventile, Absaugstutzen)
- Schlauchklemmen und Befestigungsmaterial
- Schottdurchführungen für Kraftstoffleitungen

**Ausgeschlossen (in separaten Wissensdateien):**
- Kraftstofftanks → 19.01
- Kraftstofffilter und Wasserabscheider → 19.02
- Kraftstoff-Förderpumpen → 19.04
- Einspritzkomponenten → 19.05
- Tankanzeigesysteme → 19.06

### 1.4 Klassifizierung nach Kraftstoffart

| Eigenschaft | Diesel (AGO/MGO) | Benzin (ROZ 95/98) | E10/E15 Ethanol-Mix |
|-------------|-------------------|---------------------|---------------------|
| Flammpunkt | >55°C (marine: >60°C) | -43°C | -40°C |
| Explosionsgrenze UEG | 0,6 Vol.-% | 1,0 Vol.-% | 1,0 Vol.-% |
| Explosionsgrenze OEG | 6,5 Vol.-% | 7,6 Vol.-% | 7,6 Vol.-% |
| Dampfdruck bei 20°C | <1 kPa | 45–90 kPa | 50–95 kPa |
| Dichte bei 15°C | 0,820–0,860 kg/l | 0,720–0,775 kg/l | 0,740–0,780 kg/l |
| Leitungsmaterial | Kupfer, Edelstahl, NBR-Schlauch | Nur ISO 7840 Typ A/B, kein Kupfer (Benzin+Ethanol) | Nur E10-zugelassene Materialien, PTFE-Innenseele |
| Brandrisiko | Mittel | **Extrem hoch** | **Extrem hoch** |
| Permeationsrisiko | Niedrig | Mittel | **Hoch** (Ethanol) |

### 1.5 Grundlegende Systemarchitektur

```
┌─────────────────────────────────────────────────────────────────────┐
│                    KRAFTSTOFF-LEITUNGSSYSTEM                         │
│                                                                      │
│  [Decksstutzen] ──► [Einfüllleitung] ──► [TANK] ◄── [Entlüftung]  │
│       │                                     │              │         │
│       │                                     ▼              ▼         │
│       │                              [Absperrventil]  [Flammen-      │
│       │                                     │          sperre]       │
│       │                                     ▼              │         │
│       │                              [Vorfilter/         [Bordwand-  │
│       │                               Wasserab-           austritt]  │
│       │                               scheider]                      │
│       │                                     │                        │
│       │                                     ▼                        │
│       │                              [Kraftstoff-                    │
│       │                               pumpe]                         │
│       │                                     │                        │
│       │                                     ▼                        │
│       │                              [Hauptfilter]                   │
│       │                                     │                        │
│       │                                     ▼                        │
│       │  ┌──────────────────────────[MOTOR]──────────────┐           │
│       │  │                              │                │           │
│       │  │                              ▼                │           │
│       │  │                       [Rücklaufleitung]       │           │
│       │  │                              │                │           │
│       │  └──────────────────────────────┘                │           │
│       │                                     │                        │
│       │                                     ▼                        │
│       │                              [TANK Rücklauf]                 │
│       │                              (über Treibstoff-               │
│       │                               spiegel)                       │
└─────────────────────────────────────────────────────────────────────┘
```

---

## 2. Grundlagen und Theorie

### 2.1 Leitungsmaterialien

#### 2.1.1 Kupferrohr (Cu-DHP / CW024A / C12200)

**Werkstoffkenndaten:**

| Eigenschaft | Wert | Einheit |
|-------------|------|---------|
| Werkstoff-Nr. | CW024A (EN) / C12200 (ASTM) | — |
| Cu-Gehalt | ≥99,90% | % |
| Phosphor-Gehalt | 0,015–0,040 | % |
| Zugfestigkeit (weich) | 220–260 | MPa |
| Zugfestigkeit (halbhart) | 250–320 | MPa |
| 0,2%-Dehngrenze (weich) | 50–80 | MPa |
| Bruchdehnung | 35–45 (weich), 8–20 (halbhart) | % |
| E-Modul | 127 | GPa |
| Dichte | 8,94 | kg/dm³ |
| Wärmeleitfähigkeit | 340 | W/(m·K) |
| Wärmeausdehnungskoeffizient | 16,8 × 10⁻⁶ | 1/K |
| Max. Betriebstemperatur | 200°C (ohne Lötstelle) | °C |
| Korrosionsrate Seewasser | 0,02–0,05 | mm/Jahr |

**Nennweiten und Wandstärken (nach DIN EN 1057):**

| Außen-Ø [mm] | Wand [mm] | Innen-Ø [mm] | Max. Druck bei 20°C [bar] | Anwendung |
|---------------|-----------|---------------|----------------------------|-----------|
| 6 | 1,0 | 4,0 | 85 | Manometer-Leitung |
| 8 | 1,0 | 6,0 | 63 | Diesel-Versorgung Kleinmotor |
| 10 | 1,0 | 8,0 | 51 | Diesel-Versorgung bis 30 PS |
| 12 | 1,0 | 10,0 | 42 | Diesel-Versorgung bis 60 PS |
| 15 | 1,0 | 13,0 | 34 | Diesel-Versorgung bis 120 PS |
| 18 | 1,0 | 16,0 | 28 | Diesel-Versorgung Großmotor |
| 22 | 1,0 | 20,0 | 23 | Einfüllleitung |
| 28 | 1,5 | 25,0 | 27 | Einfüllleitung groß |

**Vorteile Kupferrohr:**
- Hervorragende Korrosionsbeständigkeit gegen Diesel und Heizöl
- Leicht biegbar (weichgeglüht), gute Anpassung an Bootskörper
- Glatte Innenfläche, geringer Strömungswiderstand
- Antibakterielle Wirkung (hemmt Dieselpest)
- Einfache Verarbeitung: Rohrbiegezange, Bördelwerkzeug
- Lange Lebensdauer: 25–40 Jahre bei Diesel-Anwendung

**Nachteile und Einschränkungen:**
- **NICHT für Benzin mit Ethanol-Anteil (E10/E15)** — Kupfer katalysiert Oxidation, bildet Kupferacetat-Ablagerungen
- Vibrationsbruch an ungestützten Stellen (Ermüdung nach ca. 10⁷ Zyklen)
- Galvanische Korrosion bei Kontakt mit Edelstahl ohne Isolierung
- Einfrierrisiko bei Wassereinschluss (Rohrleitungstod in nordischen Gewässern)
- Nicht für Abgasnähe >150°C ohne Hitzeschild

**Verbindungstechniken:**

| Technik | Beschreibung | Druckfestigkeit | Anwendung |
|---------|-------------|-----------------|-----------|
| Bördelverbindung (Flare) | 45°-Bördel auf Rohende, Überwurfmutter auf Gegenstück | Bis 40 bar | Standard für Diesel, lösbar |
| Schneidringverschraubung | Schneidring greift in Rohr, Überwurfmutter presst | Bis 160 bar | Hochdruck, lösbar |
| Hartlöten (Silberlot) | L-Ag 45 Sn, >620°C | Rohrfestigkeit | Permanente Verbindungen, Brandschutz |
| Weichlöten | Sn97Cu3, 230°C | Bis 6 bar | **NICHT für Kraftstoff** (Schmelzpunkt zu niedrig) |
| Pressfitting | Mechanische Verpressung mit O-Ring | Bis 16 bar | Nur mit marine-zugelassenen Fittings |

> ⚠ **WARNUNG:** Weichlöten (Zinn-Lot) ist nach ISO 10088 und ABYC H-24/H-33 für Kraftstoffleitungen **verboten**. Im Brandfall schmilzt die Verbindung bei ca. 230°C und setzt Kraftstoff frei.

#### 2.1.2 Edelstahlrohr (1.4401 / AISI 316 / 316L)

**Werkstoffkenndaten:**

| Eigenschaft | 1.4401 (316) | 1.4404 (316L) | Einheit |
|-------------|-------------|---------------|---------|
| C-Gehalt max. | 0,07% | 0,03% | % |
| Cr | 16,5–18,5 | 16,5–18,5 | % |
| Ni | 10,0–13,0 | 10,0–13,0 | % |
| Mo | 2,0–2,5 | 2,0–2,5 | % |
| Zugfestigkeit | 520–680 | 520–680 | MPa |
| 0,2%-Dehngrenze | ≥200 | ≥200 | MPa |
| Bruchdehnung | ≥40 | ≥40 | % |
| Dichte | 7,98 | 7,98 | kg/dm³ |
| Korrosionsrate Seewasser | <0,01 | <0,01 | mm/Jahr |

**Nennweiten Marine (nach DIN EN 10216-5):**

| Außen-Ø [mm] | Wand [mm] | Innen-Ø [mm] | Max. Druck bei 20°C [bar] | Gewicht [kg/m] |
|---------------|-----------|---------------|----------------------------|----------------|
| 6 | 1,0 | 4,0 | 110 | 0,12 |
| 8 | 1,0 | 6,0 | 83 | 0,17 |
| 10 | 1,0 | 8,0 | 66 | 0,22 |
| 12 | 1,5 | 9,0 | 83 | 0,39 |
| 15 | 1,5 | 12,0 | 66 | 0,50 |
| 18 | 1,5 | 15,0 | 55 | 0,61 |
| 22 | 1,5 | 19,0 | 45 | 0,76 |

**Vorteile Edelstahlrohr:**
- Universelle Chemikalienbeständigkeit (Diesel, Benzin, Ethanol, Biodiesel)
- Höchste Festigkeit aller Leitungsmaterialien
- Feuerfest — kein Schmelzen unter 1400°C
- Kein Permeationsproblem
- Keine galvanische Korrosion mit Edelstahl-Fittings

**Nachteile:**
- Schwieriger zu biegen als Kupfer (federt zurück)
- Teurer als Kupfer (Faktor 2,5–3,5)
- Spezialwerkzeug für Schneidringverschraubungen nötig
- Spaltkorrosion möglich bei chloridreichem Kondenswasser in Spalten
- 316L (Low Carbon) bevorzugt, da 316 nach dem Schweißen interkristallin korrodieren kann

#### 2.1.3 Aluminium-Leitungen

Im Yachtbau **selten** eingesetzt und generell **nicht empfohlen** für Kraftstoffleitungen:
- Korrosionsgefahr bei Kontakt mit Kupfer-Fittings (galvanisch)
- Nicht beständig gegen Biodiesel-Beimischungen
- Nur bei Aluminium-Rümpfen als Segment zwischen Tank und erstem Ventil akzeptabel
- Wenn verwendet: AlMg3 (EN AW-5754), eloxiert, Wandstärke min. 1,5mm

#### 2.1.4 Gummischlauch (NBR — Acrylnitril-Butadien-Kautschuk)

NBR ist das Standard-Elastomer für Kraftstoffschläuche im Marinebau.

**NBR-Werkstoffdaten:**

| Eigenschaft | Wert | Einheit |
|-------------|------|---------|
| Acrylnitril-Gehalt | 28–45 (marine: 33–38) | % |
| Shore-Härte | 55–75 | Shore A |
| Zugfestigkeit | 10–25 | MPa |
| Bruchdehnung | 200–600 | % |
| Druckverformungsrest (70°C/24h) | 15–35 | % |
| Temperaturbereich | -30 bis +100°C | °C |
| Beständig gegen | Diesel, Benzin, Mineralöle, Fette | — |
| Nicht beständig gegen | Ozon, UV, Ketone, Ester, starke Säuren | — |

**Schlauchaufbau nach ISO 7840:**

```
┌─────────────────────────────────────────────────┐
│ Außenschicht (Cover):                            │
│   CR (Chloropren) oder CSM (Chlorsulfonyl-PE)   │
│   → UV-/Ozon-/Witterungsbeständigkeit           │
│   → Abriebschutz                                │
│   → ggf. feuerbeständige Beschichtung (Typ A)   │
├─────────────────────────────────────────────────┤
│ Verstärkungslage (Reinforcement):                │
│   Textilgeflecht (Polyester/Aramid) oder         │
│   Stahlgeflecht (bei Hochdruck)                  │
│   → Druckfestigkeit, Knickstabilität            │
├─────────────────────────────────────────────────┤
│ Innenschicht (Tube/Liner):                       │
│   NBR (Standard) oder FKM (Hochleistung)         │
│   → Kraftstoffbeständigkeit                     │
│   → Permeationsbarriere                         │
│   → Glatte Oberfläche für Durchfluss            │
└─────────────────────────────────────────────────┘
```

#### 2.1.5 PTFE-Schlauch (Polytetrafluorethylen)

**Werkstoffdaten PTFE-Liner:**

| Eigenschaft | Wert | Einheit |
|-------------|------|---------|
| Dichte | 2,13–2,20 | g/cm³ |
| Zugfestigkeit | 20–35 | MPa |
| Bruchdehnung | 250–400 | % |
| Temperaturbereich | -200 bis +260°C | °C |
| Dielektrische Festigkeit | 60 | kV/mm |
| Permeationsrate (Benzin) | <0,5 | g/m²/24h |
| Reibungskoeffizient | 0,04–0,10 | — |
| Chemische Beständigkeit | Universell (außer flüssiges Alkali, elementares Fluor) | — |

**PTFE-Schlauchaufbau (marine):**

| Schicht | Material | Funktion |
|---------|----------|----------|
| Innenseele | Glatt-PTFE oder Wellrohr-PTFE, Wandstärke 0,5–1,0mm | Chemikalienbarriere, Nullpermeation |
| Verstärkung | Edelstahl-Geflecht (304 oder 316) | Druckfestigkeit bis 200 bar, Knickschutz |
| Außenmantel | Silikon, EPDM oder PVC-Schrumpfschlauch | Schutz, Isolation, Brandschutz |

**Vorteile PTFE:**
- Universelle Chemikalienbeständigkeit — alle Kraftstoffarten inkl. Biodiesel, E85
- Praktisch null Permeation
- Temperaturbereich -200°C bis +260°C
- Keine Alterung (PTFE altert praktisch nicht)
- FDA-zugelassen (relevant für Trinkwasser-Parallelleitungen)
- Antistatische Varianten verfügbar (Ruß-gefülltes PTFE)

**Nachteile PTFE:**
- Teuer (Faktor 5–8 gegenüber NBR)
- Steifer als NBR (Biegeradien beachten)
- Kaltfluss unter Dauerlast (Anschlüsse nachziehen)
- Nicht transparent (Füllstand nicht sichtbar)
- Antistatische Version zwingend bei Benzin (elektrostatische Aufladung → Funkenbildung)

#### 2.1.6 FKM/Viton-Schlauch (Fluorkautschuk)

**Werkstoffdaten FKM:**

| Eigenschaft | Wert | Einheit |
|-------------|------|---------|
| Fluorgehalt | 64–70 | % |
| Shore-Härte | 60–90 | Shore A |
| Zugfestigkeit | 10–20 | MPa |
| Temperaturbereich | -20 bis +200°C | °C |
| Permeationsrate (Benzin) | 1–5 | g/m²/24h |
| Quellbeständigkeit (Diesel) | <5% Volumenzunahme | % |
| Quellbeständigkeit (Benzin) | <15% Volumenzunahme | % |

FKM wird zunehmend als Innenschicht in hochwertigen Marineschläuchen verwendet, wenn PTFE zu steif und NBR nicht ausreichend beständig ist. Besonders empfohlen für Biodiesel (FAME) und E10-Kraftstoffe.

### 2.2 Nennweiten und Durchflussberechnung

#### 2.2.1 Dimensionierungsgrundlage

Die Leitungsdimensionierung richtet sich nach dem maximalen Kraftstoffverbrauch des Motors bei Volllast plus einer Sicherheitsreserve von 50% für den Rücklauf.

**Grundformel:**

```
Q_max = (P × SFC) / (ρ × 60)

Wobei:
  Q_max = Volumenstrom [l/min]
  P     = Motorleistung [kW]
  SFC   = Spezifischer Kraftstoffverbrauch [g/kWh]
  ρ     = Kraftstoffdichte [g/l]
```

**Typische SFC-Werte:**

| Motortyp | SFC [g/kWh] | Anmerkung |
|----------|-------------|-----------|
| Diesel Saugmotor | 230–260 | Ältere Motoren |
| Diesel Turbomotor | 200–230 | Moderne Marine-Diesel |
| Diesel Common-Rail | 190–215 | Neueste Generation |
| Benzin Vergaser | 310–380 | Ältere Außenborder |
| Benzin EFI | 270–320 | Moderne Außenborder |
| Benzin DI | 240–290 | Direkteinspritzer |

**Berechnungsbeispiel:**

Motor: 75 kW Diesel-Turbo, SFC = 220 g/kWh, Diesel-Dichte = 840 g/l

```
Q_max = (75 × 220) / (840 × 60) = 16.500 / 50.400 = 0,327 l/min

Mit Rücklauf (Faktor 1,5): Q_gesamt = 0,327 × 1,5 = 0,491 l/min
Mit Sicherheit (Faktor 1,25): Q_design = 0,491 × 1,25 = 0,614 l/min
```

#### 2.2.2 Strömungsgeschwindigkeit und Leitungsdurchmesser

**Empfohlene Strömungsgeschwindigkeiten:**

| Leitungsabschnitt | v_max [m/s] | Begründung |
|-------------------|-------------|------------|
| Saugleitung (Tank → Pumpe) | 0,5–0,8 | Kavitationsvermeidung |
| Druckleitung (Pumpe → Filter → Motor) | 1,0–2,0 | Druckverlustbegrenzung |
| Rücklaufleitung (Motor → Tank) | 0,5–1,0 | Geringe Druckverluste |
| Einfüllleitung | 1,5–3,0 | Schnelles Betanken |
| Entlüftungsleitung | 0,1–0,5 | Minimaler Gegendruck |

**Durchmesser-Bestimmung:**

```
d = √(4 × Q / (π × v)) × 1000

Wobei:
  d = Innendurchmesser [mm]
  Q = Volumenstrom [m³/s]
  v = Strömungsgeschwindigkeit [m/s]
```

**Zuordnungstabelle Motorleistung → Leitungsdurchmesser (Diesel):**

| Motorleistung [kW] | Verbrauch bei VL [l/h] | Empf. Saug-ID [mm] | Empf. Druck-ID [mm] | Empf. Rücklauf-ID [mm] |
|---------------------|------------------------|---------------------|---------------------|------------------------|
| 5–15 | 2–5 | 6 | 6 | 6 |
| 15–30 | 5–9 | 8 | 6 | 8 |
| 30–60 | 9–17 | 8 | 8 | 8 |
| 60–120 | 17–32 | 10 | 8 | 10 |
| 120–200 | 32–52 | 12 | 10 | 12 |
| 200–350 | 52–88 | 16 | 12 | 16 |
| 350–600 | 88–150 | 20 | 16 | 20 |
| 600–1000 | 150–250 | 25 | 20 | 25 |

#### 2.2.3 Druckverlustberechnung

**Darcy-Weisbach-Gleichung für glatte Rohre:**

```
Δp = λ × (L/d) × (ρ × v²) / 2

Wobei:
  Δp = Druckverlust [Pa]
  λ  = Rohrreibungszahl (Moody-Diagramm)
  L  = Leitungslänge [m]
  d  = Innendurchmesser [m]
  ρ  = Dichte [kg/m³]
  v  = Strömungsgeschwindigkeit [m/s]
```

**Einzelwiderstände (ζ-Werte) typischer Armaturen:**

| Armatur | ζ-Wert | Äquivalente Rohrlänge L/d |
|---------|--------|---------------------------|
| 90°-Rohrbogen (R=2d) | 0,3–0,5 | 15–25 |
| 90°-Winkelstück (scharf) | 1,0–1,5 | 50–75 |
| T-Stück (Durchgang) | 0,3–0,5 | 15–25 |
| T-Stück (Abzweig) | 1,0–1,5 | 50–75 |
| Kugelhahn (offen) | 0,05–0,1 | 3–5 |
| Absperrhahn (offen) | 3,0–5,0 | 150–250 |
| Rückschlagventil | 1,5–3,0 | 75–150 |
| Kraftstofffilter (sauber) | 2,0–5,0 | 100–250 |
| Kraftstofffilter (verschmutzt) | 10,0–30,0 | 500–1500 |
| Schlauchkupplung | 0,3–0,5 | 15–25 |
| Schnellkupplung | 1,0–2,0 | 50–100 |

### 2.3 Druckfestigkeit und Berstdruck

#### 2.3.1 Anforderungen nach ISO 7840

| Typ | Betriebsdruck [bar] | Prüfdruck (4× Betriebsdruck) [bar] | Berstdruck min. [bar] | Temperatur |
|-----|---------------------|-------------------------------------|----------------------|------------|
| A1 | 0,34 | 1,38 | 20,7 | -30°C bis +100°C |
| A2 | 0,34 | 1,38 | 20,7 | -30°C bis +100°C |
| B1 | 0,34 | 1,38 | 10,3 | -30°C bis +80°C |
| B2 | 0,34 | 1,38 | 10,3 | -30°C bis +80°C |

#### 2.3.2 Sicherheitsfaktoren

| Anwendung | Sicherheitsfaktor (Berstdruck/Betriebsdruck) | Begründung |
|-----------|-----------------------------------------------|------------|
| Diesel Niederdruckleitung | 4:1 | ISO 10088 Standard |
| Diesel Hochdruckleitung | 6:1 | Common-Rail-Systeme |
| Benzin Niederdruckleitung | 4:1 | ISO 10088 Standard |
| LPG-Leitung | 5:1 | Erhöhte Sicherheit gasförmiger Kraftstoffe |

### 2.4 Brandschutz — ISO 7840 und SAE J1527

#### 2.4.1 Feuertest nach ISO 7840

Der Feuertest ist das definierende Unterscheidungsmerkmal zwischen Typ A (feuerbeständig) und Typ B (nicht feuerbeständig).

**Testprozedur ISO 7840 Annex A:**

1. Schlauchprobe (300mm) wird horizontal in Prüfvorrichtung eingespannt
2. Schlauch wird mit Dieselkraftstoff gefüllt und auf 0,34 bar Innendruck beaufschlagt
3. Ein Brenner (nach ISO 9038) wird unter dem Schlauch positioniert
4. Flammentemperatur: 800°C ± 50°C
5. Prüfdauer: 150 Sekunden (2,5 Minuten)
6. **Bestanden**, wenn kein Kraftstoff austritt und Schlauch nicht durchbrennt

**Typ A1 vs. A2:**
- **A1:** Besteht Feuertest UND hat Permeationsrate ≤100 g/m²/24h
- **A2:** Besteht Feuertest, aber Permeationsrate >100 g/m²/24h

**Typ B1 vs. B2:**
- **B1:** Besteht Feuertest NICHT, aber Permeationsrate ≤100 g/m²/24h
- **B2:** Besteht Feuertest NICHT und Permeationsrate >100 g/m²/24h

#### 2.4.2 Einbaupflichten nach Kraftstoffart und Zone

| Zone | Diesel | Benzin |
|------|--------|--------|
| Motorraum | A1 oder A2 empfohlen, B1/B2 zulässig | **A1 oder A2 Pflicht** |
| Bis 250mm außerhalb Motorraum | A1 oder A2 empfohlen | **A1 oder A2 Pflicht** |
| >250mm außerhalb Motorraum | B1 oder B2 zulässig | B1 (empfohlen: A1/A2) |
| Tanknähe | B1 oder B2 zulässig | **A1 Pflicht** (ABYC) |
| Einfüllleitung | B1 oder B2 | B1, mit Erdung |
| Entlüftungsleitung | B2 zulässig | **A1 oder B1** mit Flammensperre |

### 2.5 Permeation

Permeation ist das Durchdringen von Kraftstoffdämpfen durch die Schlauchwand — ein oft unterschätztes Sicherheitsproblem.

#### 2.5.1 Permeationsmechanismus

```
Kraftstoff (flüssig/dampfförmig)
    ↓
┌─────────────────────────┐
│ Absorption an Innenwand  │ ← Kraftstoffmoleküle lösen sich in Polymer
├─────────────────────────┤
│ Diffusion durch Wand     │ ← Transport durch Konzentrationsgefälle
├─────────────────────────┤
│ Desorption an Außenwand  │ ← Kraftstoffdampf tritt an Außenseite aus
└─────────────────────────┘
    ↓
Kraftstoffdampf (explosionsfähig bei Benzin!)
```

#### 2.5.2 Permeationsraten verschiedener Materialien

| Material | Permeation Diesel [g/m²/24h] | Permeation Benzin [g/m²/24h] | Permeation E10 [g/m²/24h] |
|----------|------------------------------|-------------------------------|----------------------------|
| NBR (Standard, 33% ACN) | 20–50 | 80–200 | 150–400 |
| NBR (Hochleistung, 45% ACN) | 5–15 | 30–80 | 60–150 |
| FKM/Viton | 1–5 | 5–20 | 10–40 |
| PTFE (0,5mm Wand) | <0,1 | <0,5 | <0,5 |
| Kupferrohr | 0 | 0 | 0 |
| Edelstahlrohr | 0 | 0 | 0 |

#### 2.5.3 EPA/CARB-Anforderungen (US-Markt)

Die US-amerikanischen Emissionsvorschriften haben die Permeationsgrenzwerte drastisch verschärft:
- **EPA Marine (seit 2012):** ≤15 g/m²/24h (Benzin, 40°C, CE10-Referenzkraftstoff)
- **CARB (Kalifornien):** ≤10 g/m²/24h
- **Europäische Sportbootrichtlinie:** Verweist auf ISO 7840, Grenzwert 100 g/m²/24h (Typ 1)

Konsequenz: Für den US-Export sind Standard-NBR-Schläuche nicht mehr ausreichend. FKM-Liner oder PTFE-Innenseele sind erforderlich.

### 2.6 Vibrationsbeständigkeit

#### 2.6.1 Vibrationsquellen am Boot

| Quelle | Frequenzbereich [Hz] | Amplitude [mm] | Leitungsbelastung |
|--------|---------------------|-----------------|-------------------|
| Dieselmotor (Leerlauf) | 12–25 | 0,5–2,0 | Dauerlast |
| Dieselmotor (Volllast) | 25–50 | 0,2–1,0 | Dauerlast |
| Benzin-Außenborder | 40–100 | 0,1–0,5 | Dauerlast |
| Propellerwelle | 5–30 | 0,5–3,0 | Dauerlast |
| Seegang (Slamming) | 0,1–2 | 10–100 | Stoßlast |
| Anlegen/Schleusen | 0,01–0,1 | 5–50 | Stoßlast |

#### 2.6.2 Vibrationsschutzmaßnahmen

1. **Flexible Schlauchstücke** am Motor-Anschluss (mindestens 200mm Länge)
2. **Schlauchschellen** alle 300–500mm an starren Leitungen
3. **Gummiunterlagen** unter Schellen (Vibrationsentkopplung)
4. **Schlaufenbildung** in der Leitung für Dehnungsausgleich
5. **Keine starren Verbindungen** direkt am schwingungsisolierten Motor
6. **Mindestbiegeradius** einhalten (siehe Schlauch-Spezifikationen)

### 2.7 Temperaturbeständigkeit

| Zone | Erwartete Temperatur | Material-Empfehlung |
|------|---------------------|---------------------|
| Motorraum Diesel | 40–80°C (Spitzen bis 120°C) | NBR Typ A1, FKM, PTFE |
| Motorraum Benzin | 40–70°C (Spitzen bis 100°C) | FKM Typ A1, PTFE |
| Abgaskrümmernähe | 80–250°C | Nur PTFE mit Edelstahlgeflecht + Hitzeschild |
| Bilge | 5–35°C | NBR Typ B, Standard |
| Deck (Einfüllstutzen) | -20 bis +70°C | NBR oder PVC, UV-geschützt |
| Tankraum | 10–40°C | NBR Typ B, Standard |

### 2.8 Elektrostatische Aufladung

Bei Benzin-Systemen mit nicht-metallischen Leitungen besteht die Gefahr elektrostatischer Aufladung durch Kraftstoffströmung.

**Risikomatrix:**

| Leitungsmaterial | Leitfähigkeit | Aufladungsrisiko | Maßnahme |
|-----------------|---------------|------------------|----------|
| Kupferrohr | Hoch | Keines | Keine nötig |
| Edelstahlrohr | Hoch | Keines | Keine nötig |
| NBR-Schlauch (standard) | Niedrig | Mittel | Erdungsdraht empfohlen |
| NBR-Schlauch (leitfähig) | Mittel | Niedrig | Integrierter Kupferdraht |
| PTFE-Schlauch (standard) | Sehr niedrig | **Hoch** | **Leitfähiges PTFE + Erdung Pflicht** |
| PTFE-Schlauch (antistatisch) | Mittel | Niedrig | Ruß-gefülltes PTFE |

**Erdungsanforderung (ABYC H-24):**
- Elektrischer Widerstand der gesamten Kraftstoffleitung von Tank zu Motor: <10⁶ Ohm
- Erdungsverbindung alle 1,5m bei nicht-leitfähigen Schläuchen
- Tankstutzen muss mit Bordnetz-Masse verbunden sein

---

## 3. Typenübersicht

### 3.1 Starre Leitungen

#### 3.1.1 Kupferrohr weich (R220)

| Spezifikation | Wert |
|---------------|------|
| Norm | DIN EN 1057, ASTM B280 |
| Zustand | Weichgeglüht (R220) |
| Lieferform | Ringe 5m, 10m, 25m |
| Biegbarkeit | Von Hand biegbar mit Biegefeder/Rohrbiegezange |
| Mindestbiegeradius | 3× Außendurchmesser |
| Anschluss | Bördelverbindung 45° (SAE Flare) oder Schneidring |
| Zulässig für | Diesel, Heizöl |
| **Nicht zulässig für** | **Benzin mit Ethanol-Anteil** |
| Lebensdauer (Diesel) | 25–40 Jahre |
| Typische Kosten | 3–8 €/m (je nach Durchmesser) |

#### 3.1.2 Kupferrohr halbhart (R290)

| Spezifikation | Wert |
|---------------|------|
| Norm | DIN EN 1057 |
| Zustand | Halbhart (R290) |
| Lieferform | Stangen 3m, 5m |
| Biegbarkeit | Nur mit Rohrbiegemaschine |
| Mindestbiegeradius | 4× Außendurchmesser |
| Einsatz | Längere gerade Strecken, höhere Festigkeit |
| Lebensdauer | 30–50 Jahre |

#### 3.1.3 Edelstahlrohr geschweißt

| Spezifikation | Wert |
|---------------|------|
| Norm | DIN EN 10217-7 |
| Werkstoff | 1.4404 (316L) |
| Lieferform | Stangen 3m, 6m |
| Biegbarkeit | Nur maschinell, Dornbiegung empfohlen |
| Mindestbiegeradius | 4× Außendurchmesser |
| Anschluss | Schneidringverschraubung (Swagelok, Parker, Ermeto) |
| Zulässig für | Alle Kraftstoffarten |
| Lebensdauer | 40–60+ Jahre |
| Typische Kosten | 8–25 €/m |

#### 3.1.4 Edelstahlrohr nahtlos

| Spezifikation | Wert |
|---------------|------|
| Norm | DIN EN 10216-5 |
| Werkstoff | 1.4404 (316L) |
| Vorteil | Höhere Druckfestigkeit, keine Schweißnaht-Schwachstelle |
| Einsatz | Hochdruck, Common-Rail-Zuleitungen |
| Typische Kosten | 15–40 €/m |

### 3.2 Flexible Schläuche nach ISO 7840

#### 3.2.1 Typ A1 — Feuerbeständig, niedrige Permeation

| Spezifikation | Wert |
|---------------|------|
| Feuertest ISO 7840 | Bestanden (2,5 min bei 800°C) |
| Permeation | ≤100 g/m²/24h |
| Aufbau | NBR-Innenseele + Textilgeflecht + CR/CSM-Außenmantel + Feuerschutzmantel |
| Temperaturbereich | -30°C bis +100°C |
| Berstdruck | ≥20,7 bar |
| Einsatzbereich | Benzin-Motorraum (Pflicht), Diesel-Motorraum (empfohlen) |
| Markierung | "ISO 7840 A1" + Herstellerkennzeichnung alle 300mm |
| Typische Farbe | Schwarz mit roter oder weißer Markierung |
| Lebensdauer | 8–12 Jahre (Herstellerempfehlung: Wechsel nach 10 Jahren) |
| Typische Kosten | 25–60 €/m (je nach ID) |

#### 3.2.2 Typ A2 — Feuerbeständig, höhere Permeation

| Spezifikation | Wert |
|---------------|------|
| Feuertest ISO 7840 | Bestanden |
| Permeation | >100 g/m²/24h |
| Aufbau | Wie A1, aber Innenseele mit Standard-NBR |
| Einsatzbereich | Diesel-Motorraum |
| Markierung | "ISO 7840 A2" |
| Lebensdauer | 7–10 Jahre |
| Typische Kosten | 18–45 €/m |

#### 3.2.3 Typ B1 — Nicht feuerbeständig, niedrige Permeation

| Spezifikation | Wert |
|---------------|------|
| Feuertest ISO 7840 | Nicht bestanden |
| Permeation | ≤100 g/m²/24h |
| Aufbau | NBR-Innenseele (Hochleistung) + Textilgeflecht + CR-Außenmantel |
| Temperaturbereich | -30°C bis +80°C |
| Berstdruck | ≥10,3 bar |
| Einsatzbereich | Diesel außerhalb Motorraum, Benzin außerhalb Motorraum mit Einschränkungen |
| Markierung | "ISO 7840 B1" |
| Lebensdauer | 8–12 Jahre |
| Typische Kosten | 15–35 €/m |

#### 3.2.4 Typ B2 — Nicht feuerbeständig, höhere Permeation

| Spezifikation | Wert |
|---------------|------|
| Feuertest ISO 7840 | Nicht bestanden |
| Permeation | >100 g/m²/24h |
| Aufbau | Standard-NBR + Textilgeflecht + CR-Außenmantel |
| Einsatzbereich | Nur Diesel außerhalb Motorraum, Entlüftungsleitungen |
| Markierung | "ISO 7840 B2" |
| Lebensdauer | 5–8 Jahre |
| Typische Kosten | 8–20 €/m |

#### 3.2.5 ISO 8469 — Nicht-feuerbeständige Kraftstoffschläuche

| Spezifikation | Wert |
|---------------|------|
| Anwendung | Kraftstoffschläuche außerhalb des Brandbereichs |
| Feuertest | Nicht erforderlich |
| Permeation | Typ 1: ≤100 g/m²/24h, Typ 2: >100 g/m²/24h |
| Berstdruck | ≥10,3 bar |
| Temperaturbereich | -30°C bis +80°C |
| Einsatz | Diesel-Einfüllleitungen, Entlüftungsleitungen |

### 3.3 Kraftstoffhähne und Absperrventile

#### 3.3.1 Kugelhahn (Standard Marine)

| Spezifikation | Wert |
|---------------|------|
| Bauart | Voller Durchgang (Full Bore) |
| Gehäuse | Messing vernickelt oder Edelstahl 316 |
| Kugel | Messing hartverchromt oder Edelstahl 316 |
| Dichtungen | PTFE-Sitz, FKM-O-Ringe |
| Betätigung | 90°-Drehung, Hebelgriff |
| Nennweiten | DN6 bis DN25 (1/4" bis 1") |
| Betriebsdruck | 10–40 bar (je nach Nennweite) |
| Betriebstemperatur | -20°C bis +180°C |
| Durchflusswiderstand | ζ = 0,05–0,15 (offen) |
| Schaltzyklen | >10.000 |
| **Kritisch:** | Griff muss parallel zu Durchfluss = OFFEN, quer = GESCHLOSSEN |
| Kennzeichnung | ISO 10088: rote Markierung für Kraftstoff |

#### 3.3.2 Absperrhahn (Kegelventil)

| Spezifikation | Wert |
|---------------|------|
| Bauart | Kegelsitz mit 90°-Drehung |
| Vorteil | Einfache Bauart, robust |
| Nachteil | Höherer Durchflusswiderstand als Kugelhahn (ζ = 3–5) |
| Einsatz | Ältere Installationen, Not-Absperrung |
| Status | Wird zunehmend durch Kugelhähne ersetzt |

#### 3.3.3 Magnetventil (elektrisch betätigt)

| Spezifikation | Wert |
|---------------|------|
| Bauart | Elektromagnetisch, normal geschlossen (NC) |
| Spannung | 12V DC oder 24V DC |
| Stromaufnahme | 0,5–2,0 A (Halte-Strom nach Einschalten niedriger) |
| Schaltzeit | <0,5 s (Öffnen), <1,0 s (Schließen) |
| Einsatz | Fernabschaltung, Motorraum-Brandschutz, Tank-Umschaltung |
| Nennweiten | DN6 bis DN15 |
| **Wichtig:** | Normal geschlossen = bei Stromausfall schließt Ventil |
| Zulassung | ATEX-Zulassung für Benzinsysteme empfohlen |

#### 3.3.4 Rückschlagventil

| Spezifikation | Wert |
|---------------|------|
| Funktion | Verhindert Rückfluss bei Pumpen-Stillstand |
| Bauart | Federbelastet oder Schwerkraft |
| Öffnungsdruck | 0,03–0,1 bar (Niederdrucksystem) |
| Material | Messing/Edelstahl Gehäuse, NBR/FKM Sitz |
| Nennweiten | DN6 bis DN20 |
| Einbauposition | Vertikal (Schwerkraft) oder beliebig (federbelastet) |
| Durchflusswiderstand | ζ = 1,5–3,0 |

### 3.4 Schnellkupplungen

#### 3.4.1 Push-On Schnellkupplung

| Spezifikation | Wert |
|---------------|------|
| Funktion | Werkzeugloses Verbinden/Trennen |
| Anschluss | Schlauchnippel mit Federklemme |
| Nennweiten | 6mm, 8mm, 10mm ID |
| Betriebsdruck | 2–5 bar |
| Material | Acetal (POM), Messing, Edelstahl |
| Einsatz | Außenborder-Tankanschluss, tragbare Tanks |
| Selbstabsperrend | Ja (bei getrennter Kupplung schließt Ventil) |
| Lebensdauer | 3.000–10.000 Steckzyklen |

#### 3.4.2 Bajonett-Kupplung

| Spezifikation | Wert |
|---------------|------|
| Funktion | Gesicherte Schnellverbindung mit Verriegelung |
| Anschluss | Stift-Nut-Verriegelung mit 90°-Drehung |
| Nennweiten | 8mm, 10mm, 12mm |
| Betriebsdruck | 3–10 bar |
| Material | Messing vernickelt, Edelstahl |
| Einsatz | Motor-Kraftstoffanschluss, Filterwechsel |
| Selbstabsperrend | Ja, beidseitig |
| Lebensdauer | 5.000–15.000 Steckzyklen |

#### 3.4.3 Schraubkupplung (Union Fitting)

| Spezifikation | Wert |
|---------------|------|
| Funktion | Lösbare Verbindung mit Gewindeanschluss |
| Nennweiten | Alle gängigen (1/4" bis 1") |
| Betriebsdruck | Bis 40 bar |
| Material | Messing, Edelstahl 316 |
| Dichtung | Flachdichtung (Fiber/Kupfer) oder O-Ring |
| Einsatz | Überall wo gelegentliches Lösen erforderlich |
| Vorteil | Höchste Druckfestigkeit, kein Spezialwerkzeug |

### 3.5 Tankentlüftungsventile

#### 3.5.1 Standardentlüftungsventil

| Spezifikation | Wert |
|---------------|------|
| Funktion | Druckausgleich beim Betanken und bei Temperaturschwankungen |
| Bauart | Gerader Durchgang mit Schutzgitter (Insekten) |
| Anschluss | 16mm oder 19mm Schlauchanschluss, Flansch oder Gewinde |
| Material | Messing verchromt, Edelstahl 316, Kunststoff (Nylon) |
| Einbauposition | Bordwand, oberhalb Wasserlinie (min. 200mm) |
| Durchfluss | Mindestens gleich dem Einfülldurchfluss |
| Spritzwasserschutz | Lippendichtung oder Labyrinth |

#### 3.5.2 Flammensperre (Flame Arrestor)

| Spezifikation | Wert |
|---------------|------|
| Funktion | Verhindert Flammenrückschlag in den Tank |
| **Pflicht bei** | **Benzinsystemen (ISO 10088, ABYC H-24)** |
| Bauart | Drahtgeflecht (Davy-Prinzip) oder Sintermetall |
| Maschenweite | <0,5mm (verhindert Flammenausbreitung) |
| Material | Edelstahl 316 oder Monel |
| Einbauposition | In oder direkt an der Entlüftungsleitung am Tank |
| Wartung | Jährliche Reinigung (Verstopfungsgefahr durch Salzablagerungen) |
| Durchflusswiderstand | 0,01–0,05 bar |

#### 3.5.3 Druckentlüftungsventil (Pressure-Vacuum Relief Valve)

| Spezifikation | Wert |
|---------------|------|
| Funktion | Begrenzt Über- und Unterdruck im Tank |
| Öffnungsdruck (Überdruck) | 0,03–0,15 bar |
| Öffnungsdruck (Unterdruck) | -0,02 bis -0,07 bar |
| Einsatz | Große Tanks (>500l), Tanks unter Deck ohne natürliche Entlüftung |
| Material | Messing/Edelstahl, EPDM-Membran |
| Einbauposition | Höchster Punkt des Tanksystems |

### 3.6 Einfüllstutzen

#### 3.6.1 Decksstutzen (Deck Fill)

| Spezifikation | Wert |
|---------------|------|
| Norm | ISO 10088, ABYC H-24/H-33 |
| Gehäuse | Edelstahl 316 poliert oder Messing verchromt |
| Deckel | Bajonett-Verschluss mit O-Ring |
| Kennzeichnung | "DIESEL" oder "FUEL/BENZIN" eingeprägt (verwechslungssicher!) |
| Farbe Kennzeichnung | Diesel: gelb/schwarz, Benzin: rot |
| Schlauchanschluss | 38mm (1-1/2") oder 50mm (2") |
| Einbauposition | Seitendeck oder Cockpit, erhöht, mit Süllrand |
| Erdung | Metallische Verbindung zum Tankstutzen (Potentialausgleich) |
| Schlüssel | Universalschlüssel oder bootsspezifisch |

#### 3.6.2 Tankstutzen (Tank Fitting)

| Typ | Beschreibung | Einsatz |
|-----|-------------|---------|
| Einschraub-Fitting | Gewinde NPT oder BSP, mit Dichtmittel | Standard bei GFK- und Metalltanks |
| Flansch-Fitting | Verschraubter Flansch mit Dichtung | Große Tanks, hohe Belastung |
| Schweiß-Fitting | Eingeschweißt in Metalltank | Edelstahl- und Aluminiumtanks |
| Einlaminier-Fitting | In GFK einlaminiert | GFK-Tanks (Achtung: Osmose-Risiko) |

### 3.7 Schlauchklemmen und Befestigungsmaterial

#### 3.7.1 Schlauchschellen

| Typ | Material | Drehmoment [Nm] | Einsatz | Anmerkung |
|-----|----------|-----------------|---------|-----------|
| Schneckengewindeschelle (Standard) | Edelstahl 316, Band 9mm | 1,5–3,0 | Standard, Dieselleitung | Bandkanten können Schlauch einschneiden |
| Schneckengewindeschelle (breit) | Edelstahl 316, Band 12mm | 2,0–4,0 | Einfüllleitung, große Schläuche | Bessere Kraftverteilung |
| T-Bolzen-Schelle (Constant Torque) | Edelstahl 316 | 3,0–6,0 | **Kraftstoffleitungen empfohlen** | Federelement kompensiert Schrumpfung |
| Doppelschelle (Double Wire) | Edelstahl 316 | — (Federpressung) | Benzinleitungen (ABYC-Empfehlung) | Gleichmäßiger Anpressdruck |
| Federbandschelle | Federstahl verzinkt | — (Federpressung) | NUR für Kühlwasser, nicht für Kraftstoff | **NICHT für Kraftstoff zugelassen** |
| Ohrschelle (Oetiker) | Edelstahl | Einmal-Crimpen | OEM-Montage, nicht demontierbar | Gleichmäßigster Anpressdruck |

> ⚠ **ABYC H-24/H-33 Anforderung:** An jedem Kraftstoff-Schlauchanschluss sind **zwei** Schlauchschellen erforderlich, wenn der Innendurchmesser ≥12mm (1/2") beträgt.

#### 3.7.2 Leitungsbefestigung

| Typ | Material | Abstand | Anmerkung |
|-----|----------|---------|-----------|
| Rohrschelle mit Gummieinlage | Edelstahl 316 + EPDM | 300–500mm | Standard für starre Leitungen |
| Kabelbinder (UV-beständig) | Nylon PA66, schwarz | 200–300mm | Nur Sekundärbefestigung, nicht allein |
| Kunststoff-Klemmschelle | PA66, selbstklebend oder geschraubt | 200–400mm | Für Schläuche, vibrationsdämpfend |
| Adel-Klemme (Cushion Clamp) | Edelstahl + Gummipolster | 300–500mm | Professionelle Installation |
| P-Klammer | Edelstahl 316, gummiert | 300–500mm | Alternative zu Adel-Klemme |

#### 3.7.3 Schottdurchführungen

| Typ | Beschreibung | Brandschutz | Einsatz |
|-----|-------------|-------------|---------|
| Metall-Schottdurchführung | Edelstahl/Messing, verschraubt mit Dichtung | Ja (Metallgehäuse) | Motorschott, Tankschott |
| Gummi-Kabeldurchführung | Geteilter Gummiblock mit Verschraubung | Bedingt | Nicht-kritische Schotte |
| Feuerschutz-Durchführung | Intumeszenz-Material quillt bei Hitze | Ja, aktiv | Brandschutz-Schotte (ISO 9094) |

---

## 4. Produktlinien und Spezifikationen

### 4.1 Vetus (Niederlande)

**Kraftstoffschläuche:**

| Modell | Typ | ID [mm] | AD [mm] | ISO | Material | Preis [€/m] |
|--------|-----|---------|---------|-----|----------|-------------|
| FUHOSE06A | Versorgung | 6 | 13 | 7840 A1 | NBR/CR | 28 |
| FUHOSE08A | Versorgung | 8 | 15 | 7840 A1 | NBR/CR | 32 |
| FUHOSE10A | Versorgung | 10 | 17 | 7840 A1 | NBR/CR | 38 |
| FUHOSE12A | Versorgung | 12 | 19 | 7840 A2 | NBR/CR | 35 |
| FUHOSE16A | Versorgung | 16 | 24 | 7840 A2 | NBR/CR | 42 |
| FUHOSE19 | Einfüllung | 19 | 28 | 8469 | NBR/CR | 22 |
| FUHOSE25 | Einfüllung | 25 | 35 | 8469 | NBR/CR | 28 |
| FUHOSE38 | Einfüllung | 38 | 50 | 8469 | NBR/CR | 38 |

**Kraftstoffhähne:**

| Modell | Typ | Nennweite | Anschluss | Material | Preis [€] |
|--------|-----|-----------|-----------|----------|-----------|
| FUVALV10 | Kugelhahn | 3/8" | Schlauchtülle 10mm | Messing vernickelt | 35 |
| FUVALV12 | Kugelhahn | 1/2" | Schlauchtülle 12mm | Messing vernickelt | 42 |
| FUVALV34 | Kugelhahn | 3/4" | Gewinde BSP | Messing vernickelt | 55 |
| FUV2WAY | 2-Wege-Ventil | 1/2" | Gewinde BSP | Messing vernickelt | 85 |

**Einfüllstutzen:**

| Modell | Kennzeichnung | Anschluss | Material | Preis [€] |
|--------|---------------|-----------|----------|-----------|
| DECK038D | DIESEL | 38mm | Edelstahl 316 poliert | 65 |
| DECK050D | DIESEL | 50mm | Edelstahl 316 poliert | 78 |
| DECK038F | FUEL | 38mm | Edelstahl 316 poliert | 65 |
| DECK050F | FUEL | 50mm | Edelstahl 316 poliert | 78 |

**Entlüftungsventile:**

| Modell | Typ | Anschluss | Material | Preis [€] |
|--------|-----|-----------|----------|-----------|
| VENTR16 | Standardentlüftung | 16mm | Edelstahl 316 | 28 |
| VENTR19 | Standardentlüftung | 19mm | Edelstahl 316 | 32 |
| FLMARR16 | Mit Flammensperre | 16mm | Edelstahl 316/Monel | 68 |
| FLMARR19 | Mit Flammensperre | 19mm | Edelstahl 316/Monel | 78 |

### 4.2 Trident Marine (USA)

**Kraftstoffschläuche — Marine Grade:**

| Modell | Serie | ID [mm] | ISO | Besonderheit | Preis [€/m] |
|--------|-------|---------|-----|-------------|-------------|
| 327-0060 | Type A1 | 6 | 7840 A1 | EPA-konform, E10-beständig | 35 |
| 327-0080 | Type A1 | 8 | 7840 A1 | EPA-konform, E10-beständig | 40 |
| 327-0100 | Type A1 | 10 | 7840 A1 | EPA-konform, E10-beständig | 48 |
| 327-0120 | Type A1 | 12 | 7840 A1 | EPA-konform, E10-beständig | 55 |
| 365-0080 | Type A2 | 8 | 7840 A2 | Diesel-Standard | 28 |
| 365-0100 | Type A2 | 10 | 7840 A2 | Diesel-Standard | 32 |
| 365-0120 | Type A2 | 12 | 7840 A2 | Diesel-Standard | 38 |
| 350-0380 | Fill Hose | 38 | 8469 | Einfüllleitung, verstärkt | 25 |
| 350-0500 | Fill Hose | 50 | 8469 | Einfüllleitung, verstärkt | 32 |

**Trident 327-Serie (A1) Technische Details:**

| Eigenschaft | Wert |
|-------------|------|
| Innenseele | FKM (Viton®-Equivalent) |
| Verstärkung | 2-lagig Polyestergeflecht |
| Außenmantel | Polychloropren (CR) mit Feuerschutzbeschichtung |
| Temperaturbereich | -40°C bis +100°C |
| Berstdruck | 24,1 bar |
| Permeation (CE10, 40°C) | <8 g/m²/24h (EPA-konform) |
| Mindestbiegeradius (8mm ID) | 50mm |
| UL-gelistet | Ja (UL 1114) |
| USCG-zugelassen | Ja (33 CFR 183) |

### 4.3 Sierra Marine (USA)

**Kraftstoffleitungs-Zubehör:**

| Modell | Beschreibung | Material | Anwendung | Preis [€] |
|--------|-------------|----------|-----------|-----------|
| 18-7876 | Kraftstoff-Absperrventil 1/4" | Messing | Diesel Kleinmotor | 22 |
| 18-7886 | Kraftstoff-Absperrventil 3/8" | Messing | Diesel/Benzin | 28 |
| 18-7887 | Kraftstoff-Absperrventil 1/2" | Messing | Standard | 35 |
| 18-7856 | Schnellkupplung 3/8" | Kunststoff/Messing | Außenborder | 18 |
| 18-7857 | Schnellkupplung Universal | Kunststoff | Außenborder | 15 |
| 18-8091 | Primer-Birne 3/8" | NBR | Kraftstoff-Vorfüllung | 12 |
| 18-8001 | Schlauchschelle 316 (2er Set) | Edelstahl 316 | Kraftstoffschlauch | 6 |
| 18-7890 | Einfüllstutzen "DIESEL" | Edelstahl 316 | Decksmontage | 58 |
| 18-7891 | Einfüllstutzen "GAS" | Edelstahl 316 | Decksmontage | 58 |

### 4.4 Gates Marine (USA) / Parker Hannifin

**Marine Fuel Hose:**

| Modell | Typ | ID [mm] | Norm | Besonderheit | Preis [€/m] |
|--------|-----|---------|------|-------------|-------------|
| MFH-5/16 | A1 | 8 | SAE J1527 R1 | Fluoroelastomer-Liner | 45 |
| MFH-3/8 | A1 | 10 | SAE J1527 R1 | Fluoroelastomer-Liner | 52 |
| MFH-1/2 | A1 | 12 | SAE J1527 R1 | Fluoroelastomer-Liner | 60 |
| MFH-5/8 | A1 | 16 | SAE J1527 R1 | Fluoroelastomer-Liner | 72 |

**Parker Parflex-Serie (PTFE-Schläuche):**

| Modell | ID [mm] | AD [mm] | Max. Druck [bar] | Berstdruck [bar] | Besonderheit |
|--------|---------|---------|-------------------|-------------------|-------------|
| 510N-4 | 5,6 | 9,7 | 276 | 1104 | PTFE glatt, Edelstahlgeflecht |
| 510N-6 | 7,9 | 12,7 | 207 | 828 | PTFE glatt, Edelstahlgeflecht |
| 510N-8 | 10,3 | 15,1 | 172 | 690 | PTFE glatt, Edelstahlgeflecht |
| 510N-10 | 12,7 | 17,5 | 138 | 552 | PTFE glatt, Edelstahlgeflecht |
| 519N-6 | 7,9 | 12,7 | 207 | 828 | Antistatisch (Ruß-PTFE) |
| 519N-8 | 10,3 | 15,1 | 172 | 690 | Antistatisch (Ruß-PTFE) |

### 4.5 Racor / Parker (USA)

**Kraftstoff-Ventile und Umschalter:**

| Modell | Typ | Funktion | Nennweite | Material | Preis [€] |
|--------|-----|----------|-----------|----------|-----------|
| RK 21069 | Kugelhahn | Absperrung | 3/8" | Messing/Edelstahl | 45 |
| RK 75500 | 2-Wege-Ventil | Tankumschaltung | 3/8" | Messing | 125 |
| RK 75900 | 3-Wege-Ventil | Tankumschaltung + Bypass | 3/8" | Messing | 175 |
| RK 97755 | Flammensperre | Tankentlüftung | 16mm | Edelstahl/Monel | 85 |

### 4.6 Perko (USA)

**Einfüllstutzen und Entlüftungen:**

| Modell | Typ | Kennzeichnung | Anschluss | Material | Preis [€] |
|--------|-----|---------------|-----------|----------|-----------|
| 0528DP0 | Einfüllstutzen gerade | DIESEL | 38mm (1-1/2") | Edelstahl 316 | 72 |
| 0528DP2 | Einfüllstutzen gewinkelt | DIESEL | 38mm | Edelstahl 316 | 85 |
| 0528GP0 | Einfüllstutzen gerade | GAS | 38mm | Edelstahl 316 | 72 |
| 0540DP0 | Einfüllstutzen | DIESEL | 50mm (2") | Edelstahl 316 | 95 |
| 0540GP0 | Einfüllstutzen | GAS | 50mm | Edelstahl 316 | 95 |
| 0524DP0 | Flush-Einfüllstutzen | DIESEL | 38mm | Bronze verchromt | 110 |
| 0070DP0 | Entlüftungsventil | — | 16mm | Edelstahl 316 | 35 |
| 0543DP0 | Entlüftungsventil mit Flammensperre | — | 16mm | Edelstahl 316/Monel | 92 |

### 4.7 Swagelok (USA) — Rohrverbindungstechnik

**Schneidring-Verschraubungen für starre Leitungen:**

| Modell | Rohrgröße | Gewinde | Material | Druckfestigkeit [bar] | Preis [€] |
|--------|-----------|---------|----------|-----------------------|-----------|
| SS-600-1-6 | 6mm | M10×1 | Edelstahl 316 | 413 | 18 |
| SS-800-1-8 | 8mm | M12×1.5 | Edelstahl 316 | 344 | 22 |
| SS-1010-1-10 | 10mm | M14×1.5 | Edelstahl 316 | 275 | 26 |
| SS-1210-1-12 | 12mm | M16×1.5 | Edelstahl 316 | 275 | 30 |
| B-600-1-6 | 6mm | M10×1 | Messing | 206 | 8 |
| B-800-1-8 | 8mm | M12×1.5 | Messing | 172 | 10 |

### 4.8 Whale (Nordirland) — Schnellkupplungen

| Modell | Typ | Nennweite | Anschluss | Material | Preis [€] |
|--------|-----|-----------|-----------|----------|-----------|
| WX1538 | Quick Connect | 10mm | Schlauch-Steck | Acetal/Edelstahl | 18 |
| WX1539 | Quick Connect | 12mm | Schlauch-Steck | Acetal/Edelstahl | 20 |
| WX1554 | Quick Connect T-Stück | 10mm | 3× Schlauch-Steck | Acetal | 25 |
| WX1572 | Absperr-Quick-Connect | 10mm | Schlauch-Steck | Acetal/Edelstahl | 28 |

---

## 5. Hersteller-Datenbank

### 5.1 Vetus (Niederlande)

| Eigenschaft | Detail |
|-------------|--------|
| Vollständiger Name | Vetus B.V. |
| Gründung | 1951 |
| Hauptsitz | Schiedam, Niederlande |
| Produktfokus | Komplette Marine-Systeme: Kraftstoff, Abgas, Steuerung, Bugstrahlruder |
| Sortiment Kraftstoff | Schläuche, Hähne, Einfüllstutzen, Entlüftungen, Vorfilter, Tanks |
| Qualitätsniveau | Mittel bis hoch (Serienbauer-Standard) |
| Normen | ISO 7840, ISO 8469, ISO 10088, CE |
| Vertrieb Europa | Direkt + Fachhändler-Netz (>100 Länder) |
| Stärken | Breites Sortiment, gute Verfügbarkeit, OEM-Lieferant (Bavaria, Bénéteau) |
| Schwächen | Gelegentlich Qualitätsschwankungen bei Zubehör, Standard-NBR (kein FKM) |
| Website | www.vetus.com |
| Katalog | Online-Katalog mit Explosionszeichnungen |
| Preissegment | Mittelklasse |

### 5.2 Trident Marine (USA)

| Eigenschaft | Detail |
|-------------|--------|
| Vollständiger Name | Trident Marine Systems |
| Gründung | 1987 |
| Hauptsitz | Bradenton, Florida, USA |
| Produktfokus | Marine-Schläuche: Kraftstoff, Abgas, Wasser, LPG |
| Sortiment Kraftstoff | Komplette Schlauchlinie A1/A2/B1/B2, Einfüllschläuche |
| Qualitätsniveau | Hoch (US-Marktführer für Marine-Kraftstoffschläuche) |
| Normen | SAE J1527, ISO 7840, USCG 33 CFR 183, UL 1114, EPA |
| Vertrieb Europa | Über Marine-Distributoren |
| Stärken | FKM-Liner in A1-Serie, EPA-konform, umfangreiche Zulassungen |
| Schwächen | Höherer Preis, US-Zollgrößen (Umrechnung nötig) |
| Website | www.tridentmarinehose.com |
| Preissegment | Obere Mittelklasse bis Premium |

### 5.3 Racor / Parker Hannifin (USA)

| Eigenschaft | Detail |
|-------------|--------|
| Vollständiger Name | Parker Hannifin Corporation — Racor Division |
| Gründung | Racor 1969, Parker-Übernahme 1989 |
| Hauptsitz | Modesto, California, USA |
| Produktfokus | Kraftstofffilter (Marktführer), Ventile, Leitungszubehör |
| Sortiment Kraftstoff | Filter, Wasserabscheider, Umschaltventile, Flammensperren |
| Qualitätsniveau | Premium |
| Normen | USCG, SAE, ABYC, ISO |
| Stärken | Weltstandard für Kraftstoff-Filtration, exzellente Verarbeitungsqualität |
| Schwächen | Premium-Preis, begrenzte Schlauchtülle-Auswahl |
| Website | www.parker.com/racor |
| Preissegment | Premium |

### 5.4 Perko (USA)

| Eigenschaft | Detail |
|-------------|--------|
| Vollständiger Name | Perko Inc. |
| Gründung | 1907 |
| Hauptsitz | Miami, Florida, USA |
| Produktfokus | Marine-Beschläge: Einfüllstutzen, Entlüftungen, Lichter, Beschläge |
| Sortiment Kraftstoff | Einfüllstutzen (Deck Fill), Entlüftungsventile, Flammensperren |
| Qualitätsniveau | Hoch (US-OEM-Standard) |
| Normen | ABYC, USCG, SAE |
| Stärken | 116 Jahre Erfahrung, robuste Gussqualität, Bronze-Tradition |
| Schwächen | US-Gewindegrößen (NPT), begrenztes europäisches Händlernetz |
| Website | www.perko.com |
| Preissegment | Mittelklasse bis obere Mittelklasse |

### 5.5 Gates Corporation (USA)

| Eigenschaft | Detail |
|-------------|--------|
| Vollständiger Name | Gates Corporation (Tomkins-Gruppe) |
| Gründung | 1911 |
| Hauptsitz | Denver, Colorado, USA |
| Produktfokus | Industrie-Schläuche, Riemen, Hydraulik — Marine-Division |
| Sortiment Kraftstoff | Marine Fuel Hose (MFH-Serie), Schlauchkupplungen |
| Qualitätsniveau | Hoch (Industrie-Standard) |
| Normen | SAE J1527, USCG, UL |
| Stärken | Exzellente Schlauchtechnologie, FKM-Liner, weltweite Verfügbarkeit |
| Schwächen | Kleineres Marine-spezifisches Sortiment, industriell orientiert |
| Website | www.gates.com |
| Preissegment | Obere Mittelklasse |

### 5.6 Swagelok (USA)

| Eigenschaft | Detail |
|-------------|--------|
| Vollständiger Name | Swagelok Company |
| Gründung | 1947 |
| Hauptsitz | Solon, Ohio, USA |
| Produktfokus | Rohrverbindungstechnik, Schneidringverschraubungen, Ventile |
| Sortiment Kraftstoff | Schneidringverschraubungen, Kugelhähne, Rückschlagventile |
| Qualitätsniveau | Premium (Industriestandard für leckfreie Verbindungen) |
| Normen | ASTM, ASME, ISO 19879 |
| Stärken | Marktführer Schneidringverschraubungen, null-Leckage-Garantie, 60+ Jahre Erfahrung |
| Schwächen | Premium-Preis, überqualifiziert für Niederdruck-Anwendungen |
| Website | www.swagelok.com |
| Preissegment | Premium |

### 5.7 Whale (Nordirland/UK)

| Eigenschaft | Detail |
|-------------|--------|
| Vollständiger Name | Whale (Munster Simms Engineering) |
| Gründung | 1955 |
| Hauptsitz | Bangor, Nordirland, UK |
| Produktfokus | Marine-Pumpen, Schnellkupplungssysteme, Warmwasser |
| Sortiment Kraftstoff | Quick-Connect-System, Absperrventile, T-Stücke |
| Qualitätsniveau | Mittel bis hoch |
| Normen | ISO 8846, CE |
| Stärken | Innovatives Quick-Connect-System, einfache Installation |
| Schwächen | Kunststoff-basiert (nicht für Hochdruck/Motorraum) |
| Website | www.whalepumps.com |
| Preissegment | Mittelklasse |

### 5.8 Osculati (Italien)

| Eigenschaft | Detail |
|-------------|--------|
| Vollständiger Name | Osculati S.p.A. |
| Gründung | 1958 |
| Hauptsitz | Segrate (Mailand), Italien |
| Produktfokus | Marine-Zubehör Vollsortiment (>50.000 Artikel) |
| Sortiment Kraftstoff | Schläuche, Kugelhähne, Einfüllstutzen, Schlauchklemmen, Kupplungen |
| Qualitätsniveau | Mittel (gutes Preis-Leistungs-Verhältnis) |
| Normen | ISO, CE |
| Stärken | Riesiges Sortiment, günstige Preise, schnelle Lieferung in Europa |
| Schwächen | Qualität variiert nach Produktgruppe, überwiegend OEM-Zukauf |
| Website | www.osculati.com |
| Preissegment | Einsteigerklasse bis Mittelklasse |

---

## 6. Fehlerbild-Atlas

### 6.1 Fehlerbild F01: Schlauchbruch durch Materialermüdung

| Merkmal | Detail |
|---------|--------|
| **Erscheinungsbild** | Längsriss oder Querriss im Schlauch, oft an Biegestellen oder neben Schlauchklemmen |
| **Ort** | Motorraum (hohe Temperatur), Biegestellen, Klemmen-Kante |
| **Ursache** | Thermische Alterung (NBR wird spröde >80°C Dauerlast), UV-Exposition, Ozon-Angriff auf ungeschützte Außenmantel, Überschreitung der Nutzungsdauer |
| **Zeitrahmen** | Nach 8–15 Jahren, beschleunigt bei Motorraumtemperaturen >60°C Durchschnitt |
| **Risiko** | **KRITISCH** — freier Kraftstoffaustritt im Motorraum → Brandgefahr |
| **Erkennung** | Sichtprüfung: Risse, Verhärtung (Shore-Härte >85A statt 60–70A), Verfärbung (braun statt schwarz), Kraftstoffgeruch |
| **Sofortmaßnahme** | Kraftstoffhahn schließen, Motor abstellen, Schlauch tauschen |
| **Prävention** | Schlauch alle 10 Jahre tauschen (Herstellerempfehlung), jährliche Sichtprüfung, Biegeradien einhalten |
| **Confidence** | documented (Herstellerdaten), measured (Laborergebnisse Alterung) |

### 6.2 Fehlerbild F02: Leckage an Schlauchklemme

| Merkmal | Detail |
|---------|--------|
| **Erscheinungsbild** | Kraftstofftropfen oder -film am Schlauchende unter/neben der Schlauchklemme |
| **Ort** | Jeder Schlauch-Stutzen-Übergang |
| **Ursache** | Klemme lose (Vibration), falsche Klemmenposition (zu weit vom Stutzenende), falscher Klemmentyp (Federbandschelle statt Schneckengewinde), Schlauch geschrumpft (Alterung), Stutzen korrodiert/narbig |
| **Zeitrahmen** | 2–8 Jahre nach Installation |
| **Risiko** | HOCH — schleichende Leckage kann Bilge mit Kraftstoff füllen |
| **Erkennung** | Feuchter Film am Anschluss, Kraftstoffgeruch, Verfärbung im Bilgenbereich, UV-Lecksuchlampe |
| **Sofortmaßnahme** | Klemme nachziehen (Drehmoment prüfen), bei Wiederholung Schlauch + Klemme tauschen |
| **Prävention** | T-Bolzen-Schellen (Constant Torque) verwenden, zwei Schellen bei ≥12mm ID, jährlich Drehmoment prüfen |
| **Confidence** | documented (ABYC-Empfehlungen), estimated (Erfahrungswerte) |

### 6.3 Fehlerbild F03: Korrosion am Kupferrohr

| Merkmal | Detail |
|---------|--------|
| **Erscheinungsbild** | Grüne Patina (Kupfercarbonat), braune Flecken, Lochfraß, Wanddurchbruch |
| **Ort** | Befestigungspunkte (Kontaktkorrosion mit Edelstahlschellen), Schottdurchführungen, Salzwasser-Spritzbereich |
| **Ursache** | Galvanische Korrosion (Kupfer + Edelstahl ohne Isolierung), chloridreiche Atmosphäre, Ammoniakdämpfe (WC-Nähe), Erosionskorrosion bei überhöhter Strömungsgeschwindigkeit |
| **Zeitrahmen** | 5–20 Jahre (je nach Ursache) |
| **Risiko** | MITTEL bis HOCH — Lochfraß kann zu plötzlichem Leitungsbruch führen |
| **Erkennung** | Verfärbung, Grünspan, Feuchtigkeitsspuren, Druckverlust |
| **Sofortmaßnahme** | Betroffenes Segment tauschen, Ursache (galvanische Kopplung) beseitigen |
| **Prävention** | Gummierte Rohrschellen, keine Edelstahl-Direkt-Kontakte, Bilge trocken halten |
| **Confidence** | measured (Korrosionsraten dokumentiert), documented (Materialkunde) |

### 6.4 Fehlerbild F04: Verstopfte Tankentlüftung

| Merkmal | Detail |
|---------|--------|
| **Erscheinungsbild** | Tank baut Unterdruck auf (Motor geht nach Minuten aus), Überdruck beim Tanken (Kraftstoff spritzt aus Einfüllstutzen) |
| **Ort** | Entlüftungsventil an Bordwand, Flammensperre, Entlüftungsleitung |
| **Ursache** | Insektennester (Wespen!), Salzablagerungen in Flammensperre, geknickter Entlüftungsschlauch, Spinnennetze im Austrittsventil |
| **Zeitrahmen** | Saisonal (Frühjahr nach Winterlager), 2–5 Jahre bei Flammensperre |
| **Risiko** | MITTEL — Motorausfall (Unterdruck), Umweltverschmutzung (Überdruck beim Tanken) |
| **Erkennung** | Motor stottert/stirbt nach 10–30 min Betrieb, Tanken extrem langsam, "Gluckern" aus Einfüllstutzen |
| **Sofortmaßnahme** | Einfülldeckel leicht öffnen (Druckausgleich), Entlüftung reinigen |
| **Prävention** | Jährliche Reinigung der Flammensperre, Insektengitter am Austritt, Entlüftungsleitung auf Knickstellen prüfen |
| **Confidence** | documented (häufiges Praxisproblem), estimated (Zeitrahmen variiert) |

### 6.5 Fehlerbild F05: Falsches Schlauchmaterial

| Merkmal | Detail |
|---------|--------|
| **Erscheinungsbild** | Aufgequollener/erweichter Schlauch, Verfärbung, Schlauch löst sich vom Stutzen, Innenseele delaminiert |
| **Ort** | Überall wo ungeeignetes Material eingesetzt wurde |
| **Ursache** | Einsatz von PVC-Wasserschlauch für Kraftstoff, Standard-Gummischlauch ohne ISO-Zulassung, NBR-Schlauch für Ethanol-Benzin (E10/E15), Industrieschlauch ohne Marine-Zulassung |
| **Zeitrahmen** | Wochen bis Monate nach Installation |
| **Risiko** | **KRITISCH** — schnelle Degradation, hohe Brandgefahr |
| **Erkennung** | Schlauch fühlt sich "aufgeblasen" oder "klebrig" an, Innenschicht quillt heraus, fehlende ISO 7840/8469-Markierung auf dem Schlauch |
| **Sofortmaßnahme** | Sofortiger Austausch gegen zugelassenes Material |
| **Prävention** | Nur Schläuche mit aufgedruckter ISO 7840/8469-Norm verwenden, Markierung prüfen |
| **Confidence** | documented (ISO-Normen), measured (Quellversuche) |

### 6.6 Fehlerbild F06: Permeation durch Schlauchwand

| Merkmal | Detail |
|---------|--------|
| **Erscheinungsbild** | Kraftstoffgeruch ohne sichtbare Leckage, feuchter Film auf Schlauch-Außenseite, explosimeteranzeige im Motorraum |
| **Ort** | Gesamte Schlauchlänge, verstärkt bei langen Leitungsabschnitten und hoher Temperatur |
| **Ursache** | Standard-NBR-Schlauch (Typ B2) in schlecht belüftetem Raum, Benzin-Permeation durch alterndes Schlauchmaterial, Ethanol-Kraftstoff erhöht Permeationsrate |
| **Zeitrahmen** | Dauerhaft, verstärkt mit Schlauch-Alter und Temperatur |
| **Risiko** | MITTEL (Diesel) bis **HOCH** (Benzin — explosionsfähiges Gemisch) |
| **Erkennung** | Kraftstoffgeruch, Explosimeter-Messung, Infrarot-Gasanalyse |
| **Sofortmaßnahme** | Belüftung sicherstellen, Schlauch gegen Typ A1 (niedrige Permeation) oder PTFE tauschen |
| **Prävention** | Von Anfang an Typ A1 oder B1 verwenden, Motorraum-Ventilation sicherstellen |
| **Confidence** | measured (Permeationsraten normiert), documented (EPA-Daten) |

### 6.7 Fehlerbild F07: Vibrations-Ermüdungsbruch Kupferrohr

| Merkmal | Detail |
|---------|--------|
| **Erscheinungsbild** | Ringförmiger Riss am Kupferrohr, typischerweise an Befestigungspunkten oder Biegestellen |
| **Ort** | Am Motorblock nahe Befestigung, an Schottdurchführung, an engem Biegeradius |
| **Ursache** | Dauerhafte Vibrationsbelastung ohne Gummientkopplung, fehlendes flexibles Schlauchstück zwischen Motor und starrer Leitung, zu enger Biegeradius (Kerbwirkung) |
| **Zeitrahmen** | 3–10 Jahre, abhängig von Motorstunden und Befestigungsqualität |
| **Risiko** | **KRITISCH** — plötzlicher Bruch, voller Kraftstoffaustritt |
| **Erkennung** | Oft erst bei Bruch erkannt; präventiv: Ultraschall-Rissprüfung an kritischen Stellen |
| **Sofortmaßnahme** | Leitung absperren, Segment ersetzen, flexibles Zwischenstück einbauen |
| **Prävention** | Min. 200mm flexibler Schlauch vor jedem Motoranschluss, gummierte Schellen, Biegeradien ≥3× AD |
| **Confidence** | measured (Ermüdungskurven Cu-DHP), documented (Praxisberichte) |

### 6.8 Fehlerbild F08: Undichter Einfüllstutzen

| Merkmal | Detail |
|---------|--------|
| **Erscheinungsbild** | Kraftstoff tritt am Einfüllstutzen auf Deck aus, Verfärbung des Gelcoats um Stutzen |
| **Ort** | Deck-Einfüllstutzen (Deck Fill) |
| **Ursache** | O-Ring des Deckels ausgehärtet, Gewinde des Stutzens korrodiert, Dichtung zwischen Stutzen und Deck defekt, Einfüllschlauch vom Stutzen gerutscht |
| **Zeitrahmen** | 5–15 Jahre (O-Ring), 10–25 Jahre (Stutzenkorrosion) |
| **Risiko** | MITTEL — Kraftstoff auf Deck (Rutschgefahr, Umwelt), Wassereinbruch in Tank |
| **Erkennung** | Kraftstoffgeruch an Deck, Verfärbung, Wassergehalt im Kraftstoff steigt |
| **Sofortmaßnahme** | O-Ring tauschen, Stutzen reinigen, Dichtmasse erneuern |
| **Prävention** | O-Ring alle 3 Jahre tauschen, Deckeldichtung mit Vaseline pflegen |
| **Confidence** | documented (häufiges Wartungsthema), estimated (Intervalle) |

### 6.9 Fehlerbild F09: Galvanische Korrosion an Mischinstallation

| Merkmal | Detail |
|---------|--------|
| **Erscheinungsbild** | Massiver Materialabtrag an einem der beiden Metalle, weiße/grüne Ablagerungen an Verbindungsstelle |
| **Ort** | Übergang Kupferrohr → Edelstahlfitting, Messinghahn → Aluminiumtank, Bronzestutzen → Stahlrumpf |
| **Ursache** | Unterschiedliche Metalle in galvanischer Reihe ohne Isolation, Seewasser als Elektrolyt in Bilge |
| **Zeitrahmen** | 1–5 Jahre (je nach Elektrolyt-Präsenz) |
| **Risiko** | HOCH — fortschreitende Zerstörung der weniger edlen Komponente |
| **Erkennung** | Weiße/grüne Ablagerungen, "pockennarbige" Oberfläche, lose Verbindungen |
| **Sofortmaßnahme** | Galvanische Kopplung aufheben (Isolierstück), korrodierte Teile ersetzen |
| **Prävention** | Gleiche Materialgruppe verwenden, Isolierflansche, Bilge trocken halten |
| **Confidence** | measured (galvanische Spannungsreihe), documented (Materialwissenschaft) |

### 6.10 Fehlerbild F10: Dieselpest-Verstopfung

| Merkmal | Detail |
|---------|--------|
| **Erscheinungsbild** | Schwarze/braune schleimige Ablagerungen in Leitungen und Filtern, Motor stottert oder stirbt |
| **Ort** | Saugleitung Tank → Filter, Filtergehäuse, Leitungs-Innenwand |
| **Ursache** | Mikrobieller Befall (Cladosporium resinae, Hormoconis resinae) an der Diesel-Wasser-Grenzschicht, begünstigt durch Biodiesel-Anteil (FAME) und Wassergehalt im Tank |
| **Zeitrahmen** | Monate bis Jahre, saisonal verstärkt in warmen Perioden |
| **Risiko** | MITTEL — Motorausfall durch Kraftstoffmangel |
| **Erkennung** | Schnelle Filterverschmutzung, schwarzer Schleim im Filter, unangenehmer Geruch (Schwefelwasserstoff) |
| **Sofortmaßnahme** | Filter tauschen, Tank reinigen, Biozid zugeben (Grotamar 82) |
| **Prävention** | Wasser regelmäßig aus Tank ablassen, Biozid prophylaktisch, Tank voll halten (Kondenswasser vermeiden) |
| **Confidence** | documented (mikrobiologisch erforscht), estimated (Zeitrahmen) |

### 6.11 Fehlerbild F11: Schlauch-Knick (Kinking)

| Merkmal | Detail |
|---------|--------|
| **Erscheinungsbild** | Abgeknickter Schlauch, reduzierter oder kein Durchfluss, Schlauchmantel an Knickstelle beschädigt |
| **Ort** | Enge Leitungsführungen, Ecken, Motorraum, nach Wartungsarbeiten |
| **Ursache** | Biegeradius unterschritten, Schlauch bei Wartung nicht korrekt zurückverlegt, fehlende Leitungsführung/Schellen, zu kurzer Schlauch |
| **Zeitrahmen** | Sofort nach fehlerhafter Installation oder nach Wartung |
| **Risiko** | MITTEL — Kraftstoffmangel am Motor, im Extremfall Schlauchbruch |
| **Erkennung** | Motor-Leistungsverlust, Motor stirbt unter Last, sichtbarer Knick |
| **Sofortmaßnahme** | Schlauch geradlegen, ggf. längeres Stück einsetzen |
| **Prävention** | Mindestbiegeradien einhalten (4× AD für NBR, 6× AD für PTFE), Biegeschutzfedern, ausreichende Schlauchlänge |
| **Confidence** | documented (Herstellerdaten Biegeradien), estimated (Praxis) |

### 6.12 Fehlerbild F12: Leckage an Bördelverbindung

| Merkmal | Detail |
|---------|--------|
| **Erscheinungsbild** | Kraftstofftropfen an der Überwurfmutter einer Bördelverbindung (Flare Fitting) |
| **Ort** | Kupferrohr-Anschlüsse, Filteranschlüsse, Motoranschlüsse |
| **Ursache** | Bördel nicht sauber ausgeführt (Riefen, schief), Überwurfmutter nicht korrekt angezogen, Vibration hat Verbindung gelöst, Kupfer-Ermüdung am Bördel |
| **Zeitrahmen** | Wochen nach Installation (Montagefehler) bis Jahre (Vibration) |
| **Risiko** | HOCH — dauerhafter Kraftstoffverlust an potenziell heißer Stelle |
| **Erkennung** | Tropfenbildung, Kraftstoffgeruch, Verfärbung an Verbindung |
| **Sofortmaßnahme** | Überwurfmutter kontrolliert nachziehen (1/6 Umdrehung), bei Wiederholung Bördel neu anfertigen |
| **Prävention** | Professionelles Bördelwerkzeug verwenden (Excenter-Bördelgerät, nicht Schlagbördel), Kalibrierten Drehmomentschlüssel verwenden |
| **Confidence** | documented (Installationstechnik), estimated (Zeitrahmen) |

---

## 7. Troubleshooting-Entscheidungsbäume

### 7.1 Entscheidungsbaum: Motor stirbt nach kurzer Laufzeit

```
[Motor stirbt nach 10–30 Minuten]
    │
    ├── Lässt sich sofort wieder starten?
    │   ├── JA → Kraftstoffversorgung prüfen → weiter bei 7.2
    │   └── NEIN → Warten hilft?
    │       ├── JA (nach 5–10 min) → Kraftstoffmangel (Dampfblase oder Verstopfung)
    │       │   ├── Vorfilter prüfen → verschmutzt? → TAUSCHEN
    │       │   ├── Entlüftungsleitung prüfen → verstopft? → REINIGEN (F04)
    │       │   │   ├── Flammensperre prüfen → Salz/Insekten → REINIGEN
    │       │   │   └── Entlüftungsschlauch → Knick? → VERLEGEN
    │       │   ├── Saugleitung prüfen → Knick? → KORRIGIEREN (F11)
    │       │   └── Tankinhalt prüfen → Wassergehalt? → WASSER ABLASSEN
    │       └── NEIN → Elektrisches Problem (nicht Kraftstoff)
    │
    ├── Motor geht unter Last aus?
    │   ├── JA → Kraftstoffmenge unzureichend
    │   │   ├── Leitungsdurchmesser zu klein? → VERGRÖSSERN
    │   │   ├── Filter verstopft? → TAUSCHEN
    │   │   ├── Absperrventil nur halb offen? → VOLL ÖFFNEN
    │   │   └── Saugleitungslänge/Höhe? → max. 1,5m Saughöhe prüfen
    │   └── NEIN → Leerlauf-Problem → Einspritzpumpe (nicht Leitung)
    │
    └── Tankstand?
        ├── Tank voll → Problem in Leitung/Filter/Entlüftung
        ├── Tank halb → Wie oben, plus: Tankabsaugung über Schmutz?
        └── Tank fast leer → BETANKEN, Dieselpest prüfen (F10)
```

### 7.2 Entscheidungsbaum: Kraftstoffleck gefunden

```
[Kraftstoff-Leckage festgestellt]
    │
    ├── Wo ist die Leckage?
    │   ├── Am Schlauch selbst
    │   │   ├── Riss/Bruch? → F01 → SCHLAUCH SOFORT TAUSCHEN
    │   │   ├── Aufgequollen/weich? → F05 → FALSCHES MATERIAL → TAUSCHEN
    │   │   └── Feuchter Film, kein sichtbarer Defekt? → F06 → PERMEATION
    │   │       └── Typ B2-Schlauch? → Upgrade auf A1 oder PTFE
    │   │
    │   ├── An Schlauchklemme
    │   │   ├── Klemme lose? → NACHZIEHEN (max. 3 Nm für 9mm-Band)
    │   │   ├── Klemme fest aber undicht?
    │   │   │   ├── Schlauch verhärtet? → SCHLAUCH TAUSCHEN
    │   │   │   ├── Stutzen korrodiert/narbig? → STUTZEN TAUSCHEN
    │   │   │   └── Falsche Klemmenart? → T-Bolzen-Schelle verwenden
    │   │   └── Nur eine Klemme bei ≥12mm ID? → ZWEITE KLEMME ERGÄNZEN
    │   │
    │   ├── An Bördelverbindung
    │   │   ├── Tropft bei Betrieb? → ÜBERWURFMUTTER 1/6 Umdrehung nachziehen
    │   │   ├── Tropft weiterhin? → BÖRDEL NEU ANFERTIGEN
    │   │   └── Vibrations-Leck? → FLEXIBLES ZWISCHENSTÜCK einbauen
    │   │
    │   ├── An Kupferrohr
    │   │   ├── Grüne Patina? → F03/F09 → GALVANISCHE KORROSION
    │   │   ├── Ringförmiger Riss? → F07 → VIBRATIONSBRUCH
    │   │   └── Lochfraß? → F03 → KORROSION → Segment tauschen
    │   │
    │   └── Am Einfüllstutzen
    │       ├── Beim Tanken? → F08 → O-RING / DICHTUNG TAUSCHEN
    │       └── Bei Seegang? → Schlauchverbindung Stutzen→Tank prüfen
    │
    └── Sofortmaßnahme (IMMER):
        ├── 1. Kraftstoffhahn am Tank SCHLIESSEN
        ├── 2. Motor ABSTELLEN
        ├── 3. Keine elektrischen Schalter betätigen (Benzin!)
        ├── 4. Raum BELÜFTEN
        ├── 5. Leckage auffangen (Ölbindemittel bereithalten)
        └── 6. KEIN offenes Feuer
```

### 7.3 Entscheidungsbaum: Kraftstoffgeruch ohne sichtbare Leckage

```
[Kraftstoffgeruch wahrnehmbar, keine sichtbare Leckage]
    │
    ├── Benzin oder Diesel?
    │   ├── BENZIN → **SOFORTIGE MASSNAHME: Belüften, Zündquellen aus!**
    │   │   ├── Explosimeter verfügbar?
    │   │   │   ├── JA → Messen: >20% UEG → BOOT VERLASSEN, Feuerwehr
    │   │   │   └── NEIN → Vorsichtsmaßnahmen wie >20% UEG
    │   │   ├── Schlauch-Permeation? (F06)
    │   │   │   ├── Alle Schläuche auf ISO 7840-Markierung prüfen
    │   │   │   └── Fehlende Markierung → SOFORT TAUSCHEN
    │   │   ├── Tankentlüftung → Geruch kommt von außen herein?
    │   │   │   └── Entlüftungsaustritt in Cockpitnähe? → VERLEGEN
    │   │   └── Tank-Inspektion → Schweißnaht/Naht undicht?
    │   │
    │   └── DIESEL → Weniger akut, aber handeln
    │       ├── Filterdichtung prüfen → O-Ring Filter
    │       ├── Rücklaufleitung prüfen → Verbindungen kontrollieren
    │       ├── Injektoren-Rücklauf → Leckölleitung
    │       └── Tank-Inspektionsdeckel → Dichtung prüfen
    │
    ├── Geruch nur bei Betrieb?
    │   ├── JA → Druckseitige Leckage
    │   │   ├── Druckleitung Pumpe → Motor prüfen
    │   │   └── Filtergehäuse prüfen (Dichtring nach Filterwechsel)
    │   └── NEIN (auch bei Stillstand) → Gravitationsleckage oder Permeation
    │       ├── Tankfüllstand relevant? (Hydrostatischer Druck)
    │       └── Tankabsperrhahn vorhanden und geschlossen?
    │
    └── Geruch nach Wartung/Filterwechsel?
        └── JA → Typisch: O-Ring im Filtergehäuse nicht korrekt eingesetzt
            └── Filter öffnen, O-Ring-Sitz kontrollieren
```

### 7.4 Entscheidungsbaum: Tanküberlauf beim Betanken

```
[Kraftstoff tritt beim Tanken aus]
    │
    ├── Wo tritt Kraftstoff aus?
    │   ├── Am Einfüllstutzen selbst
    │   │   ├── Schlauch zum Tank abgerutscht? → NEU BEFESTIGEN
    │   │   ├── Tank bereits voll? → Kein Fehler, Tank ist voll
    │   │   └── Entlüftung verstopft? → F04
    │   │       └── Tanken extrem langsam + Rückdrücken → ENTLÜFTUNG REINIGEN
    │   │
    │   ├── An der Tankentlüftung (Bordwand)
    │   │   ├── Normal bei vollem Tank → Tankvorgang BEENDEN
    │   │   ├── Bei halbvollem Tank
    │   │   │   ├── Einfüllschlauch geknickt? → Kraftstoff findet Weg über Entlüftung
    │   │   │   └── Einfüllschlauch zum falschen Tank? → INSTALLATION PRÜFEN
    │   │   └── Schwallartig → Gegendruck im Tank (Entlüftung teilweise verstopft)
    │   │
    │   └── Am Deck neben Stutzen
    │       ├── O-Ring Einfüllstutzen → TAUSCHEN (F08)
    │       └── Deck-Stutzen-Dichtung → NEU ABDICHTEN (Sikaflex 291)
    │
    ├── Tankanzeigte voll, aber viel weniger getankt als erwartet?
    │   ├── Tankanzeige defekt → SEPARATE PRÜFUNG
    │   ├── Wasser im Tank → WASSER ABLASSEN, Tankanzeige zeigt Gesamtvolumen
    │   └── Zwei Tanks verbunden? → VENTILSTELLUNG PRÜFEN
    │
    └── Umwelt-Sofortmaßnahme bei Überlauf ins Wasser:
        ├── 1. Tankvorgang SOFORT STOPPEN
        ├── 2. Ölbindemittel auf Wasseroberfläche ausbringen
        ├── 3. Hafenmeister informieren
        └── 4. Bei größerer Menge: Feuerwehr/Wasserschutzpolizei
```

### 7.5 Entscheidungsbaum: Korrosion an Kraftstoffleitungskomponenten

```
[Korrosion an Kraftstoffleitungs-Komponente festgestellt]
    │
    ├── Welches Material ist betroffen?
    │   ├── Kupferrohr
    │   │   ├── Grüne Patina (gleichmäßig)
    │   │   │   └── Normal, schützend → BEOBACHTEN, keine Aktion nötig
    │   │   ├── Grüne Flecken + Lochfraß
    │   │   │   ├── Kontakt mit Edelstahl? → F09 → ISOLIEREN
    │   │   │   ├── Ammoniak-Nähe (WC)? → LEITUNG VERLEGEN
    │   │   │   └── Salzwasser in Bilge? → BILGEPUMPE, Leitung höher verlegen
    │   │   └── Ermüdungsriss? → F07 → SEGMENT ERSETZEN
    │   │
    │   ├── Edelstahl
    │   │   ├── Tee-Staining (braune Flecken, oberflächlich)
    │   │   │   └── Kosmetisch → REINIGEN mit Edelstahlreiniger
    │   │   ├── Spaltkorrosion (an Schellen, Durchführungen)
    │   │   │   └── Spalte eliminieren, 316L statt 304 verwenden
    │   │   └── Lochfraß
    │   │       └── Chlorid-Belastung → Material 316L prüfen (ggf. 304 verbaut)
    │   │
    │   ├── Messing (Hähne, Fittings)
    │   │   ├── Rosa Verfärbung → ENTZINKUNG!
    │   │   │   ├── Nicht-entzinkungsbeständiges Messing (CuZn39Pb3)
    │   │   │   └── → TAUSCHEN gegen entzinkungsbeständiges (CuZn36Pb2As/DZR)
    │   │   └── Grünspan → Oberfläche → REINIGEN und BEOBACHTEN
    │   │
    │   └── Aluminium (selten)
    │       ├── Weiße Ablagerungen → Aluminiumoxid-Korrosion
    │       │   └── Fast immer galvanisch → GESAMTES SEGMENT auf Kupfer/Edelstahl umbauen
    │       └── Lochfraß → SOFORT TAUSCHEN (Aluminium regeneriert nicht)
    │
    └── Generelle Korrosions-Prävention:
        ├── 1. Bilge trocken halten (Bilgepumpe mit Automatik)
        ├── 2. Gleiche Materialgruppe in einem System verwenden
        ├── 3. Wenn Materialmix unvermeidbar → Isolierstücke (PTFE, Nylon)
        ├── 4. Regelmäßige Inspektion (min. 1× jährlich, vor und nach Saison)
        └── 5. Befestigungsmaterial gleiche Legierungsfamilie oder gummiert
```

---

## 8. FAQ — Häufige Fragen

### 8.1 Allgemein

**F1: Wie oft müssen Kraftstoffschläuche getauscht werden?**
A: Die Herstellerempfehlung liegt bei **10 Jahren** als absolute Maximallebensdauer. In der Praxis gilt: Jährliche Sichtprüfung auf Risse, Verhärtung (Fingernagel-Test: lässt sich die Oberfläche nicht mehr eindrücken, ist der Schlauch zu hart), Verfärbung und Quellungen. Bei Benzin-Systemen empfehlen ABYC und die Versicherungen einen Austausch nach **7–8 Jahren**. Schläuche im Motorraum altern schneller als außerhalb.

**F2: Kann ich Dieselschläuche für Benzin verwenden?**
A: **Nein**, nicht generell. Diesel-Schläuche (z. B. ISO 7840 B2) müssen weder feuerbeständig noch permeationsarm sein. Benzin erfordert im Motorraum zwingend Typ A1 oder A2 (feuerbeständig). Zudem greifen Benzin und insbesondere Ethanol-Beimischungen (E10) manche Diesel-Innenseelen an. Umgekehrt sind A1-Benzinschläuche immer auch für Diesel geeignet.

**F3: Ist Kupferrohr für Benzinsysteme erlaubt?**
A: **Nur eingeschränkt.** Reines Kupferrohr ist für Benzin ohne Ethanol-Anteil grundsätzlich zulässig. Bei Benzin mit Ethanol (E10, E15, E85) ist Kupfer **nicht empfohlen**, da Ethanol Kupferacetat-Ablagerungen bildet, die Einspritzdüsen verstopfen können. ABYC H-24 erlaubt Kupfer für Benzin, empfiehlt aber Edelstahl. In der Praxis: Für Diesel → Kupfer hervorragend. Für Benzin → Edelstahl oder zugelassene Schläuche.

**F4: Brauche ich eine Flammensperre an der Tankentlüftung?**
A: **Ja, bei Benzinsystemen ist die Flammensperre Pflicht** (ISO 10088, ABYC H-24). Bei Diesel-Systemen ist eine Flammensperre empfohlen, aber nicht zwingend vorgeschrieben, da Diesel einen hohen Flammpunkt hat (>55°C). In der Praxis: Auch bei Diesel empfehlenswert, da sie gleichzeitig als Insekten- und Schmutzbarriere dient.

**F5: Was ist der Unterschied zwischen ISO 7840 und SAE J1527?**
A: Beide Normen regeln marine Kraftstoffschläuche und sind weitgehend harmonisiert. ISO 7840 ist die internationale Norm (Europa, CE-Kennzeichnung), SAE J1527 die US-amerikanische (USCG-Zulassung). Die Prüfverfahren sind nahezu identisch. Ein Schlauch mit SAE J1527-Zulassung erfüllt in der Regel auch ISO 7840 — dies muss aber auf dem Schlauch markiert sein. Für CE-konforme Boote in der EU ist die ISO 7840-Markierung erforderlich.

**F6: Darf ich Autoteile-Kraftstoffschlauch auf dem Boot verwenden?**
A: **Nein.** Automotive-Kraftstoffschläuche (z. B. DIN 73379) sind nicht für die marine Umgebung ausgelegt. Ihnen fehlt: Salzwasserbeständigkeit der Außenschicht, ggf. Feuerbeständigkeit, UV-Beständigkeit, und sie sind nicht nach ISO 7840/8469 geprüft. Die Verwendung ist ein Verstoß gegen die Sportbootrichtlinie und kann den Versicherungsschutz kosten.

### 8.2 Material und Dimensionierung

**F7: Welchen Innendurchmesser braucht mein Diesel-Motor?**
A: Faustformel: Motorleistung in PS ÷ 10 = Innendurchmesser in mm. 30 PS → 8mm, 60 PS → 8–10mm, 100 PS → 10–12mm, 200 PS → 12–16mm. Die genaue Berechnung findet sich in Kapitel 2.2. Entscheidend ist die Saugleitung (Unterdruck), die immer eine Stufe größer als die Druckleitung sein sollte.

**F8: Reicht eine Schlauchschelle pro Anschluss?**
A: **Nein — bei Innendurchmessern ab 12mm (1/2") schreiben ABYC H-24 und H-33 zwei Schlauchschellen vor.** Bei kleineren Durchmessern ist eine Schelle ausreichend, aber zwei Schellen sind immer die bessere Praxis. Empfehlung: Immer zwei T-Bolzen-Schellen (Constant Torque) verwenden.

**F9: Wie erkenne ich den Schlauchtyp an einem bestehenden Boot?**
A: Jeder zugelassene Kraftstoffschlauch trägt eine dauerhafte Markierung im Abstand von 300mm, die enthält: Herstellername oder -zeichen, Norm (ISO 7840 oder ISO 8469), Typ (A1, A2, B1, B2), Herstellungsjahr und -quartal. Fehlt diese Markierung, ist der Schlauch entweder sehr alt, ein Nicht-Marine-Produkt oder eine Fälschung — in allen Fällen: **tauschen**.

**F10: PTFE-Schlauch oder NBR — wann lohnt sich der Aufpreis?**
A: PTFE lohnt sich bei: (a) Benzin mit Ethanol (E10/E15/E85), da Nullpermeation; (b) Biodiesel (FAME), da universelle Beständigkeit; (c) Motorraum mit schlechter Belüftung, da keine Permeation; (d) Langfahrt-Yachten, da praktisch unbegrenzte Lebensdauer; (e) Yachten über 15m / Superyachten, da Professionalisierungsgrad und Versicherungsanforderungen. Bei Standard-Diesel-Segelyachten unter 12m ist ein hochwertiger ISO 7840 A1-Schlauch (z. B. Trident 327-Serie) ausreichend.

### 8.3 Installation

**F11: Wie biege ich Kupferrohr ohne Knicken?**
A: (1) Nur weichgeglühtes Kupfer (R220) verwenden. (2) Rohrbiegefeder oder Rohrbiegezange passend zum Durchmesser. (3) Mindestbiegeradius: 3× Außendurchmesser. (4) Langsam und gleichmäßig biegen. (5) Nicht hin-und-her-biegen (Kaltverfestigung → Bruch). (6) Für enge Radien: Rohr mit Sand füllen und Enden verschließen, dann biegen.

**F12: Wie fertige ich eine korrekte Bördelverbindung an?**
A: (1) Rohrende sauber abschneiden (Rohrabschneider, nicht Säge). (2) Innen und außen entgraten. (3) Überwurfmutter VOR dem Bördeln aufstecken! (4) Exzenter-Bördelwerkzeug verwenden (45° SAE Flare). (5) Bördel muss gleichmäßig, rissefrei und konzentrisch sein. (6) Fläche mit Finger prüfen: glatt, keine Riefen. (7) Überwurfmutter handfest + 1,5–2 Umdrehungen mit Gabelschlüssel. (8) Gegenstück (Fitting) muss sauber sein.

**F13: Darf ich Teflonband an Kraftstoff-Gewinden verwenden?**
A: **Nur mit Vorsicht.** PTFE-Gewindedichtband (Teflonband) ist für Kraftstoffleitungen grundsätzlich zulässig, aber: Es muss ein kraftstoffbeständiges Dichtband sein (gelbe Farbe für Gas/Kraftstoff, nicht weißes Standard-Teflonband). Es darf nicht in den Leitungsquerschnitt ragen (Band immer in Gewinderichtung wickeln). Alternative: Loctite 577 oder Loxeal 18-10 (anaerobe Gewindedichtung, kraftstoffbeständig). Für Bördelverbindungen wird **kein** Dichtband verwendet.

**F14: Wie verlege ich eine Kraftstoffleitung korrekt?**
A: Grundregeln: (1) Möglichst kurz und direkt, aber ohne Knickstellen. (2) Abstand zu heißen Oberflächen (Abgaskrümmer: min. 300mm oder Hitzeschild). (3) Nicht über oder neben elektrischen Leitungen (Leckage + Funke = Brand). (4) Befestigung alle 300–500mm mit gummierten Schellen. (5) Flexibles Schlauchstück (min. 200mm) am Motorübergang. (6) Gefälle zur Saugseite hin (keine Luftsäcke). (7) Schottdurchführungen mit Brandschutz-Durchführung.

**F15: Müssen Kraftstoffleitungen farblich markiert werden?**
A: ISO 10088 empfiehlt eine Kennzeichnung zur Unterscheidung von Wasser-, Kraftstoff- und Abwasserleitungen. In der Praxis: Kraftstoffleitungen werden mit roten Kabelbindern oder Farbringen markiert. Einfüllstutzen müssen gemäß ISO 10088 die Kraftstoffart eingeprägt haben (DIESEL, FUEL, GAS). Verwechslung Diesel/Wasser ist einer der häufigsten und teuersten Fehler.

### 8.4 Wartung und Inspektion

**F16: Welche Prüfungen gehören zur jährlichen Inspektion?**
A: Checkliste: (1) Alle Schlauchoberflächen auf Risse, Verfärbung, Quellungen prüfen (Fingernagel-Test). (2) Alle Schlauchklemmen auf festen Sitz prüfen (Drehmoment). (3) Alle Bördelverbindungen und Fittings auf Leckage prüfen (Sichtprüfung, Papier unterlegen). (4) Kupferrohre auf Korrosion und Grünspan prüfen. (5) Absperrventil auf Funktion prüfen (Auf/Zu). (6) Einfüllstutzen-O-Ring auf Zustand prüfen. (7) Entlüftungsventil und Flammensperre reinigen. (8) Schottdurchführungen prüfen. (9) Befestigungsschellen auf Festsitz prüfen.

**F17: Wie teste ich, ob ein Schlauch noch gut ist?**
A: **Fingernagel-Test:** Drücken Sie den Fingernagel in den Schlauch. Er muss sich mindestens 1–2mm eindrücken lassen und sofort zurückfedern. Harter, nicht eindrückbarer Schlauch ist überaltert. **Biege-Test:** Biegen Sie den Schlauch um 90° — er darf keine sichtbaren Risse auf der Außenseite zeigen. **Oberflächen-Test:** Keine Klebrigkeit (Quellungszeichen), keine Schimmelbildung auf der Innenseite (vom Stutzen aus kontrollieren).

**F18: Was kostet ein kompletter Leitungstausch?**
A: Richtwerte für eine 10m-Segelyacht mit Einbau-Diesel:

| Komponente | Material [€] | Arbeit [h] | Arbeit [€ à 85/h] | Gesamt [€] |
|-----------|-------------|-----------|-------------------|------------|
| Kraftstoffschlauch (3m ISO 7840 A1, 10mm) | 120 | 2 | 170 | 290 |
| Schlauchklemmen (12 Stk. T-Bolzen) | 60 | — | — | 60 |
| Absperrventil Kugelhahn | 45 | 0,5 | 43 | 88 |
| Vorfilter-Anschlüsse | 30 | 0,5 | 43 | 73 |
| Einfüllstutzen (Deck Fill) | 75 | 1 | 85 | 160 |
| Entlüftungsventil + Flammensperre | 80 | 0,5 | 43 | 123 |
| Kleinmaterial (Schellen, Dichtringe) | 40 | — | — | 40 |
| **Summe** | **450** | **4,5** | **384** | **834** |

### 8.5 Sicherheit

**F19: Was tun bei einer Kraftstoffleckage im Motorraum?**
A: Sofortmaßnahmen: (1) **Kraftstoffhahn am Tank SCHLIESSEN** (deshalb muss er zugänglich sein!). (2) Motor ABSTELLEN. (3) Bei Benzin: **KEINE elektrischen Schalter betätigen** (Funkenbildung!). (4) Motorraum NICHT öffnen (Sauerstoffzufuhr!), erst belüften lassen. (5) Feuerlöscher griffbereit halten. (6) An Deck gehen, Notruf vorbereiten. (7) Erst nach 15 min Belüftung Motorraum öffnen und Ursache suchen.

**F20: Wie gefährlich ist ein Benzin-Kraftstoffsystem im Vergleich zu Diesel?**
A: **Erheblich gefährlicher.** Benzindämpfe sind schwerer als Luft und sammeln sich in der Bilge. Der Flammpunkt von Benzin liegt bei -43°C — Benzindampf ist bei jeder normalen Temperatur entzündlich. Die Explosionsgrenzen liegen bei 1,0–7,6 Vol.-%, d. h. schon geringe Mengen Benzindampf können explosionsfähige Gemische bilden. Diesel hat einen Flammpunkt von >55°C und ist bei normaler Raumtemperatur nicht entzündlich. Aus diesem Grund gelten für Benzinsysteme erheblich strengere Vorschriften (feuerbeständige Schläuche Typ A, Flammensperren, Bilgenbelüftung).

**F21: Muss ich einen Kraftstoff-Absperrhahn am Tank haben?**
A: **Ja.** ISO 10088 schreibt ein Absperrventil direkt am Tank (oder am Tankauslauf, maximal 150mm Abstand) vor. Das Ventil muss ohne Werkzeug bedienbar und von einem anderen Ort als dem Motorraum aus zugänglich sein. Begründung: Im Brandfall muss die Kraftstoffzufuhr getrennt werden können, ohne den Motorraum betreten zu müssen. ABYC H-24/H-33 fordert zusätzlich ein leicht identifizierbares Ventil mit klarer OFFEN/GESCHLOSSEN-Anzeige.

### 8.6 Spezialthemen

**F22: Wie wirkt sich Biodiesel (B7, B20, B100) auf Leitungen aus?**
A: Biodiesel (FAME — Fettsäure-Methylester) hat folgende Auswirkungen: (a) Quillt NBR-Schläuche stärker als mineralischer Diesel. (b) Löst Ablagerungen im Tank und spült sie in Filter und Leitungen. (c) Begünstigt mikrobiellen Befall (Dieselpest) stärker. (d) Kann Kupferkorrosion beschleunigen (organische Säuren). Empfehlung: Ab B20 FKM-Innenseele oder PTFE verwenden. B7 (EU-Standard) ist für alle ISO 7840-konformen Schläuche unkritisch.

**F23: Kann ich Kraftstoffleitungen für die Heizung (Webasto/Eberspächer) teilen?**
A: **Grundsätzlich ja**, aber mit Einschränkungen: Die Heizung benötigt einen eigenen Absperrventil. Ein T-Stück in der Motorleitung ist nur akzeptabel, wenn der Querschnitt für beide Verbraucher ausreichend ist. Besser: Separater Tankabgang mit eigenem Absperrventil. Rücklauf der Heizung darf in die Motor-Rücklaufleitung münden. Die Heizungsleitung benötigt denselben ISO 7840-Typ wie die Motorleitung.

**F24: Was ist bei der Umrüstung von Benzin auf Diesel (oder umgekehrt) zu beachten?**
A: Bei Umrüstung Benzin → Diesel: Die vorhandenen A1-Schläuche können weiterverwendet werden (überqualifiziert für Diesel, aber kompatibel). Bei Umrüstung Diesel → Benzin: **Komplettes Leitungssystem muss getauscht werden!** Diesel-B2-Schläuche sind für Benzin unzulässig. Zusätzlich erforderlich: Flammensperre an Tankentlüftung, Bilgenbelüfter, Benzin-Decksstutzen (Verwechslungsschutz), Potentialausgleich (Erdung).

**F25: Wie finde ich Ersatz-Leitungen für ein altes Boot (>25 Jahre)?**
A: (1) Vorhandene Leitungen fotografieren und vermessen (ID, AD, Länge). (2) Markierung auf dem Schlauch lesen (Hersteller, Typ). (3) Vetus, Osculati und Trident decken 95% aller Standardmaße ab. (4) Bei Kupferrohr: DIN EN 1057 ist seit Jahrzehnten stabil — identisches Material verfügbar. (5) Bei ungewöhnlichen Fittings: Cross-Referenz bei Sierra Marine oder Plastimo. (6) Im Zweifelsfall: Gesamtes System neu mit aktuellen Materialien — ist bei einem 25+ Jahre alten Boot ohnehin empfohlen.

**F26: Welche Werkzeuge brauche ich für die Wartung der Kraftstoffleitungen?**
A: Grundausstattung: Schraubendreher-Set (für Schlauchklemmen), Maulschlüssel-Set 8–22mm (für Überwurfmuttern und Fittings), Rohrabschneider (für Kupferrohr), Entgrater, Bördelwerkzeug (SAE 45° Flare, wenn Kupferrohr verbaut), Drehmomentschlüssel (Klemmen), Rohr-Biegefeder oder -zange (Kupfer), Ölbindemittel und Auffangwanne. Optional: Explosimeter/Gasdetektor (Benzin-Systeme).

**F27: Wie entlüfte ich das Kraftstoffsystem nach einem Filterwechsel?**
A: Bei Diesel: (1) Filterwechsel durchführen, neuen Filter mit sauberem Diesel vorfüllen. (2) Handpumpe am Vorfilter oder an der Einspritzpumpe betätigen (20–50 Hübe). (3) Entlüftungsschraube an der Einspritzpumpe leicht öffnen, pumpen bis blasenfreier Diesel austritt. (4) Entlüftungsschraube schließen. (5) Motor starten — läuft ggf. 5–10 Sekunden rau, bis letzte Luftblasen durch sind. (6) Bei Common-Rail-Motoren: Oft automatische Entlüftung durch elektrische Förderpumpe, Zündung EIN für 30 Sekunden, dann starten.

**F28: Können Kraftstoffleitungen einfrieren?**
A: Diesel kann bei tiefen Temperaturen ausflocken (Paraffin-Ausscheidung ab ca. -10°C je nach Sorte). Das betrifft nicht die Leitung selbst, sondern den Kraftstoff darin. Maßnahmen: Winter-Diesel verwenden (Grenzfiltrierbarkeit bis -20°C), Leitungs-Vorwärmung (Heizband), Filter mit Heizung. Wassereinschluss in Kupferleitungen kann zum Aufplatzen führen — daher: Wasser immer aus dem System fernhalten (Wasserabscheider).

**F29: Was bedeutet die Markierung auf meinem Kraftstoffschlauch?**
A: Beispiel: `TRIDENT 327 ISO 7840 A1 TYPE USCG 33 CFR 183.590 SAE J1527 R1 3/8" 10mm 2024-Q2`
- TRIDENT 327: Hersteller und Modell
- ISO 7840 A1: Feuerbeständig, niedrige Permeation (international)
- USCG 33 CFR 183.590: US-Küstenwache-Zulassung
- SAE J1527 R1: US-Schlauchnorm, Typ R1
- 3/8" 10mm: Innendurchmesser
- 2024-Q2: Herstellung 2. Quartal 2024

**F30: Wie entsorge ich alte Kraftstoffschläuche und Leitungen korrekt?**
A: Kraftstoff-kontaminierte Schläuche gelten als Sondermüll (Abfallschlüssel 150110* — Verpackungen mit Resten gefährlicher Stoffe). Abgabe beim Wertstoffhof unter Angabe "kraftstoff-kontaminiert". Kupfer- und Edelstahlrohre können nach Reinigung als Metallschrott abgegeben werden. Restliche Kraftstoff aus Leitungen auffangen und als Altöl/Altkraftstoff entsorgen.

---

## 9. Glossar

| Nr. | Begriff | Erklärung |
|-----|---------|-----------|
| 1 | **Absperrventil** | Ventil zum vollständigen Unterbrechen des Kraftstoffflusses; Pflicht am Tankausgang |
| 2 | **ABYC** | American Boat and Yacht Council; US-Organisation für Marine-Standards |
| 3 | **ACN-Gehalt** | Acrylnitril-Anteil in NBR; höherer ACN = bessere Kraftstoffbeständigkeit, weniger Kälteflexibilität |
| 4 | **Biodiesel (FAME)** | Fettsäure-Methylester aus pflanzlichen/tierischen Ölen; Beimischung B7 (7%) in EU-Diesel Standard |
| 5 | **Berstdruck** | Innendruck bei dem ein Schlauch/Rohr versagt; muss Vielfaches des Betriebsdrucks betragen |
| 6 | **Bördelverbindung** | Lösbare Rohrverbindung durch konisches Aufweiten (Bördeln) des Rohrendes; Standard bei Kupfer |
| 7 | **CE-Kennzeichnung** | Konformitätserklärung nach EU-Sportbootrichtlinie 2013/53/EU; Pflicht für Boote 2,5–24m |
| 8 | **Common Rail** | Diesel-Einspritzsystem mit gemeinsamer Hochdruck-Kraftstoffleiste; Drücke bis 2000 bar |
| 9 | **Compression Set** | Druckverformungsrest; bleibende Verformung nach Druckbelastung; niedrig = gut bei Dichtungen |
| 10 | **Constant Torque** | Schlauchschelle mit Federelement, die Anpressdruck bei Schrumpfung des Schlauchs nachführt |
| 11 | **CR (Chloropren)** | Synthetischer Kautschuk (Neopren); verwendet als Außenmantel von Kraftstoffschläuchen |
| 12 | **CSM (Chlorsulfonyl-PE)** | Hypalon; UV- und ozonbeständiges Elastomer für Schlauch-Außenmantel |
| 13 | **Dampfblase** | Gasblase im Kraftstoffsystem durch Verdampfung bei Hitze oder Unterdruck; unterbricht Kraftstofffluss |
| 14 | **Deck Fill** | Einfüllstutzen im Deck mit beschriftetem Verschlussdeckel; Tank-Befüllung von Deck aus |
| 15 | **Dieselpest** | Mikrobieller Befall des Dieselkraftstoffs; bildet Schleim der Filter und Leitungen verstopft |
| 16 | **DZR-Messing** | Dezincification Resistant; entzinkungsbeständiges Messing für Seewasser-Anwendungen |
| 17 | **Entzinkung** | Selektive Korrosion bei der Zink aus Messing gelöst wird; hinterlässt poröses, schwaches Kupfer |
| 18 | **EPA** | United States Environmental Protection Agency; regelt u.a. Permeationsgrenzwerte |
| 19 | **Exzenter-Bördelgerät** | Professionelles Werkzeug für gleichmäßige 45°-Bördel; besser als Schlag-Bördelwerkzeug |
| 20 | **Flammensperre** | Drahtgeflecht oder Sintermetall-Element das Flammenrückschlag in den Tank verhindert |
| 21 | **FKM (Viton)** | Fluorkautschuk; hochbeständiges Elastomer für aggressive Kraftstoffe und hohe Temperaturen |
| 22 | **Galvanische Korrosion** | Elektrochemischer Materialabbau bei Kontakt unterschiedlich edler Metalle in Elektrolyt |
| 23 | **ISO 7840** | Internationale Norm für feuerbeständige marine Kraftstoffschläuche; definiert Typen A1/A2/B1/B2 |
| 24 | **ISO 8469** | Internationale Norm für nicht-feuerbeständige marine Kraftstoffschläuche |
| 25 | **ISO 10088** | Internationale Norm für fest installierte Kraftstoffsysteme auf Sportbooten |
| 26 | **Kavitation** | Bildung und Implosion von Dampfblasen bei Unterdruck; zerstört Pumpen und Leitungen |
| 27 | **Knickschutz** | Feder oder Spirale am Schlauchende die das Abknicken verhindert |
| 28 | **Lochfraß** | Lokale Korrosionsform die tiefe Löcher in Metall frisst; besonders gefährlich bei Kupfer und Aluminium |
| 29 | **NBR** | Acrylnitril-Butadien-Kautschuk; Standard-Elastomer für Kraftstoffschläuche |
| 30 | **Nennweite (DN)** | Normierte Bezugsgröße für Rohr- und Armaturendurchmesser; DN10 ≈ 10mm Innendurchmesser |
| 31 | **Oetiker-Schelle** | Einmal-Crimpschelle mit Ohr; gleichmäßigster Anpressdruck, nicht demontierbar |
| 32 | **Permeation** | Durchdringen von Kraftstoffdämpfen durch die Schlauchwand; Sicherheits- und Umweltproblem |
| 33 | **PTFE** | Polytetrafluorethylen (Teflon); universell chemikalienbeständig, für alle Kraftstoffarten |
| 34 | **Primer-Birne** | Handpumpe zum manuellen Vorfüllen des Kraftstoffsystems (Außenborder-Systeme) |
| 35 | **SAE J1527** | US-Norm für marine Kraftstoffschläuche; Pendant zu ISO 7840 |
| 36 | **Schneidringverschraubung** | Lösbare Rohrverbindung durch einschneidenden Ring; höchste Druckfestigkeit |
| 37 | **Shore-Härte** | Maß für die Härte von Elastomeren; Shore A 60–70 typisch für Kraftstoffschläuche |
| 38 | **Spaltkorrosion** | Korrosion in engen Spalten (unter Schellen, in Gewinden) durch Sauerstoffverarmung |
| 39 | **T-Bolzen-Schelle** | Schlauchschelle mit T-förmigem Bolzen und Federelement; Marine-Standard für Kraftstoff |
| 40 | **UEG** | Untere Explosionsgrenze; Mindestkonzentration eines brennbaren Gases für Zündfähigkeit |
| 41 | **USCG** | United States Coast Guard; US-Küstenwache, zuständig für Marine-Sicherheitsstandards |
| 42 | **Volumenstrom** | Kraftstoffmenge pro Zeiteinheit [l/min]; Basis für Leitungsdimensionierung |
| 43 | **Weichlöten** | Löten unter 450°C (typ. 230°C Zinn-Lot); für Kraftstoffleitungen VERBOTEN (schmilzt im Brand) |
| 44 | **Wellrohr-PTFE** | PTFE-Schlauch mit gewellter Innenseele; flexibler als Glatt-PTFE, aber höherer Strömungswiderstand |
| 45 | **Zeta-Wert (ζ)** | Dimensionsloser Widerstandsbeiwert für Strömungshindernisse (Armaturen, Bögen, Fittings) |

---

## 10. Schnell-Referenz

### 10.1 Schlauchtyp-Auswahl auf einen Blick

```
Benzin-Motorraum     → ISO 7840 A1 (Pflicht)
Benzin außerhalb      → ISO 7840 B1 (empfohlen: A1)
Diesel-Motorraum      → ISO 7840 A2 (empfohlen: A1)
Diesel außerhalb      → ISO 7840 B2 (empfohlen: B1)
Einfüllleitung       → ISO 8469 Typ 1 oder 2
Entlüftung Benzin    → ISO 7840 B1 + Flammensperre
Entlüftung Diesel    → ISO 8469 + empf. Flammensperre
Ethanol (E10+)       → ISO 7840 A1 mit FKM/PTFE-Liner
Biodiesel (B20+)     → FKM-Liner oder PTFE
```

### 10.2 Leitungsdurchmesser auf einen Blick (Diesel)

```
bis 20 PS    → 6mm ID
20–40 PS     → 8mm ID
40–80 PS     → 10mm ID
80–150 PS    → 12mm ID
150–250 PS   → 16mm ID
250–500 PS   → 20mm ID
500+ PS      → 25mm ID
```

### 10.3 Schlauchklemmen-Regeln

```
ID < 12mm   → 1 Schelle (empf. 2)
ID ≥ 12mm   → 2 Schellen (Pflicht ABYC)
Typ         → T-Bolzen (Constant Torque) empfohlen
Material    → Edelstahl 316 (kein verzinkter Stahl!)
Drehmoment  → 2–3 Nm (9mm Band), 3–4 Nm (12mm Band)
Abstand     → 6–12mm von Schlauchende, 6mm zwischen Schellen
```

### 10.4 Prüf-Intervalle

```
Sichtprüfung Schläuche      → jährlich (Saisonstart)
Schlauchklemmen nachziehen   → jährlich
Flammensperre reinigen       → jährlich
Einfüllstutzen O-Ring        → alle 3 Jahre tauschen
Absperrventil testen         → jährlich (Auf/Zu)
Kraftstoffschlauch tauschen  → max. 10 Jahre (Benzin: 7–8 Jahre)
Kupferrohr-Inspektion        → alle 5 Jahre (Korrosion)
Edelstahlrohr-Inspektion     → alle 5 Jahre (Spaltkorrosion an Schellen)
```

### 10.5 Notfall-Referenz

```
LECKAGE ENTDECKT:
  1. Kraftstoffhahn am Tank SCHLIESSEN
  2. Motor ABSTELLEN
  3. Keine Schalter betätigen (Benzin!)
  4. Raum BELÜFTEN
  5. Leckage auffangen
  6. Kein offenes Feuer
  7. Bei Benzin: Explosimeter-Messung oder Boot verlassen

MOTOR STIRBT WIEDERHOLT:
  1. Tankfüllstand prüfen
  2. Absperrventil prüfen (offen?)
  3. Vorfilter prüfen (verschmutzt?)
  4. Entlüftung prüfen (verstopft?)
  5. Saugleitung prüfen (Knick? Luftziehung?)
```

### 10.6 Material-Kompatibilitätsmatrix

```
                  Diesel  Benzin  E10   E85  Biodiesel  Seewasser
Kupferrohr         ✅      ⚠️     ❌    ❌    ⚠️         ✅
Edelstahl 316L     ✅      ✅     ✅    ✅    ✅         ✅
NBR (Standard)     ✅      ✅     ⚠️    ❌    ⚠️         ✅
NBR (Hoch-ACN)     ✅      ✅     ✅    ⚠️    ⚠️         ✅
FKM/Viton          ✅      ✅     ✅    ✅    ✅         ✅
PTFE               ✅      ✅     ✅    ✅    ✅         ✅
Messing (DZR)      ✅      ✅     ⚠️    ❌    ✅         ✅
PVC                ❌      ❌     ❌    ❌    ❌         ✅

✅ = Geeignet  ⚠️ = Eingeschränkt  ❌ = Nicht geeignet
```

---

## ANHANG A — Fallstudie: Dieselleck an Segelyacht 12m

### A.1 Bootsdaten

| Parameter | Wert |
|-----------|------|
| Bootstyp | Bavaria 40 Cruiser (2008) |
| Länge | 12,35m |
| Motor | Volvo Penta D2-40 (40 PS / 29 kW) |
| Kraftstoff | Diesel |
| Tankvolumen | 210 Liter |
| Leitungssystem | Kupferrohr (Original 2008) + NBR-Schläuche |
| Alter bei Vorfall | 16 Jahre |

### A.2 Fehlerbeschreibung

Eigner bemerkte bei Saisonstart im April 2024 Dieselgeruch im Motorraum. Kein sichtbarer Tropfen, aber deutlicher Geruch. Bilge trocken. Motor lief normal. Geruch verstärkte sich bei laufendem Motor.

### A.3 Diagnose

Systematische Untersuchung ergab:
1. Alle Schlauchklemmen: fest, kein sichtbares Leck
2. Vorfilter (Racor 500FG): O-Ring in Ordnung
3. **Bördelverbindung am Kupferrohr → Absperrventil:** Haarfeiner Riss im Bördel, Diesel-Film an Überwurfmutter
4. Ursache: 16 Jahre Vibration, originaler Bördel mit Schlag-Werkzeug (erkennbar an ungleichmäßiger Bördelkante)
5. Kupferrohr zusätzlich an Schottdurchführung leicht grün verfärbt (galvanischer Kontakt mit Edelstahl-Schelle ohne Gummiisolation)

### A.4 Reparatur

| Maßnahme | Detail | Kosten [€] |
|----------|--------|-----------|
| Neuer Bördel am Kupferrohr | Exzenter-Bördelwerkzeug, sauberer Schnitt | 0 (Werkzeug vorhanden) |
| Gummiisolation unter Edelstahlschellen | EPDM-Einlagen nachgerüstet | 15 |
| Absperrventil getauscht | Altes Messing-Hahnventil → Vetus FUVALV10 Kugelhahn | 45 |
| Alle Schläuche inspiziert | Fingernagel-Test, alle noch in Ordnung (NBR, 2012 getauscht) | 0 |
| Arbeitszeit Werft | 3 Stunden à 85€ | 255 |
| **Gesamt** | | **315** |

### A.5 Lehren

- Bördelverbindungen sind Langzeit-Schwachstellen bei Vibration
- Galvanische Korrosion an Schellen ist vermeidbar (Gummiisolation)
- 16-jähriges Kupferrohr war sonst einwandfrei — Kupfer ist ein langlebiges Material
- Exzenter-Bördelwerkzeug statt Schlagbördel eliminiert den häufigsten Montagefehler

---

## ANHANG B — Fallstudie: Benzinleitung Motoryacht 8m

### B.1 Bootsdaten

| Parameter | Wert |
|-----------|------|
| Bootstyp | Sea Ray 240 Sundeck (2015) |
| Länge | 7,92m |
| Motor | MerCruiser 4.5L MPI (200 PS) |
| Kraftstoff | Benzin (Super E10) |
| Tankvolumen | 230 Liter |
| Leitungssystem | OEM-Schläuche (2015) |

### B.2 Fehlerbeschreibung

Bei der jährlichen Inspektion im März 2023 (Boot 8 Jahre alt) wurde festgestellt: Einer der Kraftstoffschläuche im Motorraum zeigte keine ISO 7840-Markierung. Der Schlauch war flexibel, nicht verhärtet, aber ohne normkonforme Kennzeichnung. Benzingeruch im Motorraum, verstärkt bei warmem Wetter.

### B.3 Diagnose

1. Schlauch als Standard-NBR-Industrieschlauch identifiziert (kein ISO 7840-Typ)
2. Offenbar bei einer früheren Reparatur als Ersatz montiert (Werkstatt-Fehler)
3. Permeationstest (organoleptisch): Deutlicher Benzingeruch auf Schlauch-Außenseite
4. Fingernagel-Test: Schlauch noch elastisch
5. **Brandrisiko:** Nicht-feuerbeständiger Schlauch im Motorraum eines Benzinboots = **kritischer Sicherheitsmangel**

### B.4 Reparatur

| Maßnahme | Detail | Kosten [€] |
|----------|--------|-----------|
| Alle Schläuche im Motorraum getauscht | Trident 327-Serie ISO 7840 A1 (FKM-Liner), 3,5m | 175 |
| Schlauchklemmen neu | T-Bolzen-Schellen Edelstahl 316, 8 Stück | 48 |
| Flammensperre geprüft | In Ordnung, gereinigt | 0 |
| Arbeitszeit Werft | 4 Stunden à 95€ (Motoryacht-Werkstatt) | 380 |
| **Gesamt** | | **603** |

### B.5 Lehren

- Schlauchmarkierung bei JEDEM Wartungsbesuch kontrollieren
- Werkstätten verwenden gelegentlich nicht-marine Ersatzteile
- Ein unmarkierter Schlauch in einem Benzin-System ist ein sofortiger Grund zum Austausch
- Der FKM-Liner (Trident 327) bietet optimalen Schutz gegen E10-Permeation
- Versicherung hätte im Schadensfall möglicherweise nicht gezahlt

---

## ANHANG C — Fallstudie: Tankentlüftung Katamaran 14m

### C.1 Bootsdaten

| Parameter | Wert |
|-----------|------|
| Bootstyp | Lagoon 42 (2019) |
| Länge | 12,80m (Rumpflänge), 14,0m (LOA) |
| Motor | 2× Yanmar 4JH57 (57 PS je Motor) |
| Kraftstoff | Diesel |
| Tankvolumen | 2× 200 Liter (ein Tank pro Rumpf) |

### C.2 Fehlerbeschreibung

Während der Überfahrt Mallorca → Sardinien (Juni 2023, ca. 30°C Lufttemperatur) fielen beide Motoren innerhalb von 20 Minuten Abstand nacheinander aus. Motoren ließen sich nach kurzer Wartezeit (5 Minuten) wieder starten, fielen aber erneut nach ca. 15 Minuten aus.

### C.3 Diagnose

1. Tankfüllstand: Beide Tanks ca. 70% — ausreichend
2. Vorfilter (Racor): Sauber, kein Wasser
3. Absperrventile: Vollständig geöffnet
4. **Entlüftung Steuerbord-Rumpf:** Flammensperre mit Salzablagerungen und Insektenresten (Wespe) stark verstopft
5. **Entlüftung Backbord-Rumpf:** Entlüftungsschlauch hinter Verkleidung abgeknickt (wahrscheinlich bei vorheriger Wartung versehentlich verdrückt)
6. Beide Tanks hatten Unterdruck aufgebaut → Kraftstoff konnte nicht nachfließen → Motorstillstand

### C.4 Reparatur

| Maßnahme | Detail | Kosten [€] |
|----------|--------|-----------|
| Flammensperre StB gereinigt | Ultraschallbad, Salzablagerungen gelöst | 25 (Reinigungsmittel) |
| Entlüftungsschlauch BB neu verlegt | Knickstelle beseitigt, Schlauch mit 3 zusätzlichen Schellen fixiert | 45 |
| Beide Entlüftungsaustritte mit Insektengitter | Edelstahlgaze vor Bordwandaustritt | 30 |
| Arbeitszeit Werft (Sardinien) | 2 Stunden à 110€ | 220 |
| **Gesamt** | | **320** |

### C.5 Lehren

- Tankentlüftung ist ein oft vergessenes, aber systemkritisches Element
- Katamarane sind doppelt betroffen (zwei separate Systeme)
- Flammensperren müssen jährlich gereinigt werden (Salz, Insekten)
- Nach jeder Wartung alle Leitungen auf Knickstellen prüfen
- Symptom "Motor stirbt nach 10–20 Minuten" → IMMER Entlüftung prüfen

---

## ANHANG D — Fallstudie: Kupferrohr-Korrosion Stahlschiff

### D.1 Bootsdaten

| Parameter | Wert |
|-----------|------|
| Bootstyp | Privatbau Stahlkutter (1992) |
| Länge | 11,50m |
| Rumpfmaterial | Stahl S235JR (St 37-2), kathodisch geschützt |
| Motor | Mercedes OM636 (42 PS) |
| Kraftstoff | Diesel |
| Tankvolumen | 300 Liter (Stahltank) |

### D.2 Fehlerbeschreibung

Bei Routine-Inspektion 2022 (Boot 30 Jahre alt) wurde massive Korrosion am Kupferrohr festgestellt — starke Grünspan-Ablagerungen, Wandstärke an mehreren Stellen reduziert, eine Stelle mit Durchbruch (Nadelloch-Leckage).

### D.3 Diagnose

1. Kupferrohr (Original 1992) direkt auf Stahlspanten mit Edelstahl-Schellen befestigt
2. **Drei-Metall-Problem:** Kupfer (Rohr) + Edelstahl (Schelle) + Stahl (Spant) in feuchter Bilge
3. Kupfer war Kathode (edler), Stahl Anode (unedler) — aber die Edelstahl-Schelle erzeugte zusätzlich eine galvanische Zelle Kupfer↔Edelstahl
4. An den Kontaktpunkten war das Kupferrohr angegriffen (untypisch — normalerweise leidet das unedlere Metall)
5. Ursache der Kupfer-Korrosion: Wechselstrom-Korrosion durch defekten Landstrom-Trenntrafo (Streustrom)

### D.4 Reparatur

| Maßnahme | Detail | Kosten [€] |
|----------|--------|-----------|
| Komplette Kraftstoffleitung auf Edelstahl 316L umgebaut | 4m Edelstahlrohr 10mm, Swagelok-Verschraubungen | 320 |
| Gummierte Edelstahl-Schellen | EPDM-isoliert, 12 Stück | 65 |
| Landstrom-Trenntrafo repariert | Fehlerstrom beseitigt | 450 |
| Potentialausgleich der Kraftstoffanlage | Erdungskabel 16mm² zu Bordmasse | 40 |
| Arbeitszeit | 8 Stunden à 75€ | 600 |
| **Gesamt** | | **1.475** |

### D.5 Lehren

- Auf Stahlschiffen ist die Materialwahl der Kraftstoffleitung besonders kritisch
- Kupfer auf Stahl mit Edelstahl-Schellen = galvanisches Dreieck in feuchter Bilge
- Streustrom durch defekte Landstrom-Installation verstärkt jede Korrosion
- Edelstahl 316L auf Stahlschiff: Mit EPDM-Isolierung und Potentialausgleich kein Problem
- 30 Jahre alte Installationen verdienen eine Kompletterneuerung

---

## ANHANG E — Fallstudie: PTFE-Schlauch Superyacht 25m

### E.1 Bootsdaten

| Parameter | Wert |
|-----------|------|
| Bootstyp | Custom Motor Yacht (Aluminium, 2018) |
| Länge | 24,90m |
| Motor | 2× Caterpillar C18 ACERT (1000 PS / 746 kW je Motor) |
| Generator | 2× Onan e-QD 27,5 kW (Diesel) |
| Kraftstoff | Diesel (Marine Gas Oil, MGO) |
| Tankvolumen | 2× 5.000 Liter + 1× 500 Liter (Tagestank) |

### E.2 Projektbeschreibung

Neubau mit Spezifikation: Alle Kraftstoffleitungen in PTFE-Schlauch mit Edelstahlgeflecht (Parker Parflex 510N-Serie) für maximale Lebensdauer und null Permeation. Starre Leitungen in Edelstahl 316L nahtlos.

### E.3 Systemdesign

| Leitungsabschnitt | Material | Dimension | Länge |
|-------------------|----------|-----------|-------|
| Tank → Absperrventil | Edelstahl 316L nahtlos | 20mm AD / 17mm ID | 2× 1,5m |
| Absperrventil → Tagestank-Transferpumpe | PTFE 510N-10 | 12,7mm ID | 2× 4m |
| Tagestank → Vorfilter (Racor 75900) | PTFE 510N-8 | 10,3mm ID | 2× 3m |
| Vorfilter → Hauptfilter | PTFE 510N-8 | 10,3mm ID | 2× 1m |
| Hauptfilter → Motor | PTFE 510N-8 | 10,3mm ID | 2× 2,5m |
| Motor-Rücklauf → Tagestank | PTFE 510N-8 | 10,3mm ID | 2× 3m |
| Einfüllleitung | Edelstahl 316L | 50mm AD | 2× 3m |
| Entlüftung | Edelstahl 316L + Flammensperre | 25mm AD | 2× 4m |

### E.4 Besonderheiten

- PTFE-Schläuche mit antistatischem Liner (Parker 519N für Generatoren, die auch Benzin-Generator-Betrieb erlauben)
- Alle Fittings Swagelok 316L (Schneidring für Stahlrohr, JIC 37° für PTFE-Schlauch)
- Doppelwandige Leitungsführung in Maschinenraum-Schacht (Auffangwanne unter allen Leitungen)
- Leckage-Sensor in Auffangwanne (Alarmsystem Brücke)
- Magnetventile an allen Tankausgängen (fernbetätigt von Brücke und Maschinenraum)
- Gesamte Kraftstoffanlage nach Lloyd's Register Yacht Code spezifiziert

### E.5 Kosten

| Position | Material [€] | Arbeit [€] | Gesamt [€] |
|----------|-------------|-----------|------------|
| PTFE-Schlauch (gesamt 45m) | 4.500 | — | 4.500 |
| Edelstahlrohr (gesamt 20m) | 800 | — | 800 |
| Swagelok-Fittings (48 Stück) | 2.400 | — | 2.400 |
| Racor-Filter (4 Stück) | 1.800 | — | 1.800 |
| Magnetventile (6 Stück) | 2.100 | — | 2.100 |
| Leckage-Sensoren (4 Stück) | 600 | — | 600 |
| Montage (Werft, 5 Tage) | — | 8.500 | 8.500 |
| **Gesamt Kraftstoffleitungssystem** | **12.200** | **8.500** | **20.700** |

### E.6 Lehren

- PTFE-System auf Superyacht ist State-of-the-Art — hohe Anfangsinvestition, aber praktisch wartungsfrei
- Antistatischer Liner (519N) als Absicherung auch bei reinen Diesel-Systemen sinnvoll
- Doppelwandige Leitungsführung mit Leckage-Sensor = höchstes Sicherheitsniveau
- Gesamtkosten Kraftstoffleitungssystem = ca. 0,3% der Baukosten einer 25m-Yacht — vernachlässigbar
- Lloyd's/Class-Spezifikation erfordert dokumentierte Materialzertifikate für jede Komponente

---

## ANHANG F — Fallstudie: Schnellkupplungsversagen Regattaboot

### F.1 Bootsdaten

| Parameter | Wert |
|-----------|------|
| Bootstyp | J/111 Performance Cruiser-Racer (2017) |
| Länge | 11,13m |
| Motor | Yanmar 3YM20 (21 PS), Saildrive |
| Kraftstoff | Diesel |
| Tankvolumen | 50 Liter |
| Besonderheit | Häufiger Ausbau des Motors für Regatten (Gewichtsersparnis) |

### F.2 Fehlerbeschreibung

Boot wurde für eine Regatta auf Performance-Konfiguration umgerüstet — Motor nicht ausgebaut, aber alle Versorgungsleitungen per Schnellkupplung getrennt (Whale WX1538, 10mm). Nach der Regatta wurde die Kraftstoffleitung wieder angekuppelt. Beim nächsten Motorbetrieb: Diesel-Leckage an der Schnellkupplung, ca. 0,5 l/h Tropfverlust.

### F.3 Diagnose

1. Schnellkupplung äußerlich unbeschädigt
2. Beim Stecken "Klick" wahrnehmbar
3. **O-Ring in der Kupplungshülse:** Durch wiederholtes Stecken (>50 Zyklen in 6 Jahren) und Diesel-Einwirkung ausgehärtet, hatte Druckverformungsrest >50%
4. Toleranz zwischen Nippel und Hülse durch O-Ring-Verformung nicht mehr gedichtet
5. Zusätzlich: Feiner Schmutz (Segelstaub, Salzreste) an Dichtfläche

### F.4 Reparatur

| Maßnahme | Detail | Kosten [€] |
|----------|--------|-----------|
| O-Ring-Satz für Whale WX1538 | Original-Ersatzteile, 4 O-Ringe FKM | 12 |
| Zweite Schnellkupplung getauscht | Vorsorglich, gleicher Verschleiß zu erwarten | 20 |
| Schutzkappen für Kupplungen | Staubschutz bei getrennter Leitung | 8 |
| Arbeitszeit | 0,5 Stunden (Eigenarbeit) | 0 |
| **Gesamt** | | **40** |

### F.5 Lehren

- Schnellkupplungen haben eine begrenzte Lebensdauer der O-Ringe (ca. 3.000–5.000 Zyklen)
- Regattaboote mit häufigem Trennen/Kuppeln: O-Ringe alle 2–3 Jahre tauschen
- Staubschutz-Kappen bei getrennten Kupplungen verwenden
- FKM-O-Ringe sind NBR-O-Ringen deutlich überlegen (Lebensdauer 2–3×)
- Schnellkupplungen sind KEIN Ersatz für feste Verbindungen — nur dort verwenden, wo Trennung notwendig

---

## ANHANG G — Fallstudie: Permeation Ethanol-Kraftstoff

### G.1 Bootsdaten

| Parameter | Wert |
|-----------|------|
| Bootstyp | Bayliner VR5 Bowrider (2016) |
| Länge | 5,72m |
| Motor | Mercury MerCruiser 4.5L MPI (200 PS) |
| Kraftstoff | Benzin E10 (zeitweise E15 von US-Tankstelle) |
| Tankvolumen | 151 Liter |
| Leitungssystem | OEM ISO 7840 A2 (Standard-NBR) |

### G.2 Fehlerbeschreibung

Eigner bemerkte ab Sommer 2022 zunehmenden Benzingeruch im Maschinenraum. Kein sichtbares Leck. Explosimeter-Messung durch Marina: 12% UEG im Motorraum (alarmierend, aber noch unter 20%).

### G.3 Diagnose

1. Alle Verbindungen dicht — kein Tropfen, kein Film
2. Schläuche ISO 7840 A2 Markierung (feuerbeständig, aber NICHT permeationsarm)
3. **Permeationsmessung (gewichtsbasiert):** 180 g/m²/24h — deutlich über der EPA-Grenze von 15 g/m²/24h
4. Ursache: Standard-NBR-Innenseele + Ethanol-Kraftstoff = erhöhte Permeation
5. A2-Typ erlaubt >100 g/m²/24h — war zum Zeitpunkt der Bootsproduktion (2016) noch CE-konform
6. E15-Kraftstoff (zeitweise getankt) verschärfte das Problem

### G.4 Reparatur

| Maßnahme | Detail | Kosten [€] |
|----------|--------|-----------|
| Alle Kraftstoffschläuche getauscht | Trident 327-0100 ISO 7840 A1 (FKM-Liner), 4m | 200 |
| Schlauchklemmen erneuert | T-Bolzen Edelstahl 316, 10 Stück | 60 |
| Motorraum-Belüftung verbessert | Zusätzlicher 12V-Bilgenventilator (ABYC-konform, zündfunkenfrei) | 120 |
| Arbeitszeit | 3 Stunden à 90€ | 270 |
| **Gesamt** | | **650** |

### G.5 Lehren

- ISO 7840 A2 ist für Benzin/Ethanol-Systeme unzureichend — A1 mit FKM/PTFE-Liner verwenden
- EPA-Grenzwerte (15 g/m²/24h) sind erheblich strenger als europäische ISO-Grenzwerte (100 g/m²/24h)
- E10/E15-Ethanol-Kraftstoff erhöht die Permeation um Faktor 2–4 gegenüber reinem Benzin
- Motorraum-Belüftung ist bei Benzin-Booten eine zweite Sicherheitsebene
- Ein nicht-sichtbares Leck (Permeation) kann gefährlicher sein als ein tropfendes Leck (Permeation erzeugt explosionsfähiges Dampf-Luft-Gemisch, Tropfen sammeln sich in der Bilge)

---

## ANHANG H — Fallstudie: Brandschutz-Nachrüstung Altboot

### H.1 Bootsdaten

| Parameter | Wert |
|-----------|------|
| Bootstyp | Dehler 36 (1988) |
| Länge | 10,85m |
| Motor | Volvo Penta MD2030 (28 PS) Diesel, nachgerüstet 2002 |
| Kraftstoff | Diesel |
| Tankvolumen | 100 Liter |
| Leitungssystem | Kupferrohr (original 1988) + Gummischläuche (unmarkiert, Alter unbekannt) |
| Zustand | Boot soll für Langfahrt Mittelmeer/Atlantik vorbereitet werden |

### H.2 Ausgangssituation

Gutachter-Inspektion vor Langfahrt-Vorbereitung ergab:
1. Kupferrohr-Leitungen: Visuell akzeptabel, leichter Grünspan an Schellen
2. Gummischläuche: Ohne ISO-Markierung, geschätzt 15–20 Jahre alt, verhärtet
3. Absperrventil: Altes Messing-Kegelventil, schwergängig
4. Kein Vorfilter/Wasserabscheider vorhanden (Motor hat nur eingebauten Feinfilter)
5. Einfüllstutzen: Messing, Gewinde korrodiert, O-Ring fehlend
6. Entlüftung: Einfaches Loch in Bordwand mit Gaze — keine Flammensperre (bei Diesel nicht Pflicht, aber empfohlen)
7. Schlauchklemmen: Teilweise verzinkter Stahl (rosten), teilweise nur eine Klemme

### H.3 Maßnahmenplan

| Nr. | Maßnahme | Priorität | Kosten [€] |
|-----|----------|-----------|-----------|
| 1 | Alle Gummischläuche tauschen gegen ISO 7840 A1 | Kritisch | 180 |
| 2 | Alle Schlauchklemmen gegen T-Bolzen Edelstahl 316 tauschen, je 2 Stück | Kritisch | 72 |
| 3 | Absperrventil tauschen gegen Vetus Kugelhahn | Hoch | 45 |
| 4 | Racor 500FG Vorfilter/Wasserabscheider einbauen | Hoch | 320 |
| 5 | Einfüllstutzen tauschen gegen Perko 0528DP0 (Edelstahl) | Mittel | 72 |
| 6 | Flammensperre an Entlüftung nachrüsten | Mittel | 78 |
| 7 | Kupferrohr: Grünspan reinigen, Edelstahl-Schellen mit Gummi-Einlage | Mittel | 35 |
| 8 | Potentialausgleich (Erdungskabel Tank → Bordmasse) | Mittel | 25 |
| 9 | Magnetventil am Tank (fernbetätigt aus Cockpit) | Optional | 180 |
| 10 | Arbeitszeit (geschätzt 10 Stunden à 85€) | — | 850 |
| | **Gesamt** | | **1.857** |

### H.4 Ergebnis

Gesamte Kraftstoffanlage auf modernen Stand gebracht. Gutachter bestätigt Konformität mit ISO 10088 und CE-Anforderungen. Boot hat 2023/2024 erfolgreich den Atlantik überquert (Kanaren → Karibik → Azoren → Heimat). Keine Kraftstoff-Probleme während der gesamten 8.500 sm.

### H.5 Lehren

- Langfahrt-Vorbereitung muss Kraftstoffsystem als Priorität einschließen
- Investition ~1.800€ für ein sicheres Kraftstoffsystem ist bei Blauwasserfahrt unverzichtbar
- Vorfilter/Wasserabscheider (Racor) ist auf Langfahrt essenziell (wechselnde Kraftstoffqualität)
- 35 Jahre altes Kupferrohr kann noch funktionsfähig sein, wenn Korrosion kontrolliert wird
- Fernbetätigtes Magnetventil bietet höchste Sicherheit (Einhandsegeln: Motor-Not-Aus vom Cockpit)

---

## ANHANG I — Pydantic v2 Modelle: Kraftstoffleitung

```python
"""AYDI Pydantic v2 Models: Fuel Line Components."""

from __future__ import annotations

from datetime import date
from enum import Enum
from typing import Optional

from pydantic import BaseModel, Field


class FuelType(str, Enum):
    """Supported fuel types."""

    DIESEL = "diesel"
    GASOLINE = "gasoline"
    E10 = "e10"
    E15 = "e15"
    E85 = "e85"
    BIODIESEL_B7 = "biodiesel_b7"
    BIODIESEL_B20 = "biodiesel_b20"
    BIODIESEL_B100 = "biodiesel_b100"
    LPG = "lpg"
    MGO = "mgo"


class LineMaterial(str, Enum):
    """Fuel line materials."""

    COPPER_SOFT = "copper_soft_r220"
    COPPER_HALF_HARD = "copper_half_hard_r290"
    STAINLESS_316L_WELDED = "stainless_316l_welded"
    STAINLESS_316L_SEAMLESS = "stainless_316l_seamless"
    NBR_STANDARD = "nbr_standard"
    NBR_HIGH_ACN = "nbr_high_acn"
    FKM_VITON = "fkm_viton"
    PTFE_SMOOTH = "ptfe_smooth"
    PTFE_CORRUGATED = "ptfe_corrugated"
    PTFE_ANTISTATIC = "ptfe_antistatic"
    ALUMINUM = "aluminum"


class ISO7840Type(str, Enum):
    """ISO 7840 hose classification."""

    A1 = "A1"
    A2 = "A2"
    B1 = "B1"
    B2 = "B2"
    NOT_APPLICABLE = "not_applicable"


class LineSection(str, Enum):
    """Fuel system line section."""

    SUPPLY = "supply"
    RETURN = "return"
    FILL = "fill"
    VENT = "vent"
    OVERFLOW = "overflow"
    TRANSFER = "transfer"
    GENERATOR_SUPPLY = "generator_supply"
    HEATER_SUPPLY = "heater_supply"


class ConfidenceLevel(str, Enum):
    """Confidence level for assessments."""

    MEASURED = "measured"
    CALCULATED = "calculated"
    VISUAL_HIGH = "visual_high"
    VISUAL_MEDIUM = "visual_medium"
    VISUAL_LOW = "visual_low"
    VISUAL_INSUFFICIENT = "visual_insufficient"
    ESTIMATED = "estimated"
    BENCHMARK = "benchmark"
    DOCUMENTED = "documented"


class FuelLineSpec(BaseModel):
    """Specification for a single fuel line segment."""

    model_config = {"from_attributes": True}

    line_id: str = Field(
        ...,
        description="Unique identifier for the line segment",
        examples=["FL-001-SUPPLY-MAIN"],
    )
    section: LineSection
    fuel_type: FuelType
    material: LineMaterial
    iso_7840_type: Optional[ISO7840Type] = Field(
        None,
        description="ISO 7840 classification (hoses only)",
    )
    inner_diameter_mm: float = Field(
        ..., gt=0, le=100, description="Inner diameter in mm"
    )
    outer_diameter_mm: float = Field(
        ..., gt=0, le=150, description="Outer diameter in mm"
    )
    wall_thickness_mm: float = Field(
        ..., gt=0, le=25, description="Wall thickness in mm"
    )
    length_mm: float = Field(
        ..., gt=0, description="Total length in mm"
    )
    max_operating_pressure_bar: float = Field(
        ..., gt=0, description="Maximum operating pressure in bar"
    )
    burst_pressure_bar: Optional[float] = Field(
        None, gt=0, description="Burst pressure in bar"
    )
    min_bend_radius_mm: Optional[float] = Field(
        None, gt=0, description="Minimum bend radius in mm"
    )
    temperature_range_min_c: float = Field(
        -40, description="Minimum operating temperature in Celsius"
    )
    temperature_range_max_c: float = Field(
        100, description="Maximum operating temperature in Celsius"
    )
    permeation_rate_g_m2_24h: Optional[float] = Field(
        None,
        ge=0,
        description="Permeation rate in g/m²/24h (hoses only)",
    )
    fire_resistant: bool = Field(
        False, description="Passes ISO 7840 fire test"
    )
    antistatic: bool = Field(
        False, description="Has antistatic properties"
    )
    manufacturer: Optional[str] = None
    model_number: Optional[str] = None
    installation_date: Optional[date] = None
    next_replacement_date: Optional[date] = None


class FuelLineSystem(BaseModel):
    """Complete fuel line system for a vessel."""

    model_config = {"from_attributes": True}

    vessel_id: str = Field(..., description="Vessel identifier")
    system_id: str = Field(
        ..., description="Fuel system identifier (e.g., main, generator)"
    )
    fuel_type: FuelType
    engine_power_kw: float = Field(..., gt=0, description="Engine power in kW")
    fuel_consumption_max_lph: float = Field(
        ..., gt=0, description="Max fuel consumption in l/h"
    )
    lines: list[FuelLineSpec] = Field(
        default_factory=list, description="All line segments"
    )
    total_line_length_mm: float = Field(
        0, ge=0, description="Sum of all line lengths"
    )
    has_shutoff_valve_at_tank: bool = Field(
        False, description="ISO 10088 requirement"
    )
    has_flame_arrestor: bool = Field(
        False, description="Required for gasoline systems"
    )
    has_deck_fill: bool = True
    has_vent: bool = True
    meets_iso_10088: Optional[bool] = None
    meets_abyc_h24: Optional[bool] = None
    meets_abyc_h33: Optional[bool] = None
    confidence: ConfidenceLevel = ConfidenceLevel.ESTIMATED
    notes: list[str] = Field(default_factory=list)
```

---

## ANHANG J — Pydantic v2 Modelle: Armatur und Ventil

```python
"""AYDI Pydantic v2 Models: Fuel Fittings and Valves."""

from __future__ import annotations

from enum import Enum
from typing import Optional

from pydantic import BaseModel, Field


class ValveType(str, Enum):
    """Types of fuel system valves."""

    BALL_VALVE = "ball_valve"
    CONE_VALVE = "cone_valve"
    SOLENOID_VALVE = "solenoid_valve"
    CHECK_VALVE = "check_valve"
    PRESSURE_RELIEF = "pressure_relief"
    VACUUM_RELIEF = "vacuum_relief"
    PRESSURE_VACUUM_RELIEF = "pressure_vacuum_relief"
    TWO_WAY_SELECTOR = "two_way_selector"
    THREE_WAY_SELECTOR = "three_way_selector"


class FittingType(str, Enum):
    """Types of fuel line fittings."""

    FLARE_45 = "flare_45_sae"
    COMPRESSION_RING = "compression_ring"
    HOSE_BARB = "hose_barb"
    QUICK_CONNECT = "quick_connect"
    BAYONET = "bayonet"
    UNION = "union"
    TEE = "tee"
    ELBOW_90 = "elbow_90"
    ELBOW_45 = "elbow_45"
    REDUCER = "reducer"
    BULKHEAD = "bulkhead_fitting"
    DECK_FILL = "deck_fill"
    VENT_FITTING = "vent_fitting"
    FLAME_ARRESTOR = "flame_arrestor"
    TANK_FITTING = "tank_fitting"


class ConnectionType(str, Enum):
    """Thread/connection standards."""

    BSP = "bsp"
    NPT = "npt"
    METRIC = "metric"
    SAE_FLARE = "sae_flare"
    JIC_37 = "jic_37"
    HOSE_BARB = "hose_barb"
    PUSH_FIT = "push_fit"
    SWAGELOK = "swagelok"
    WELDED = "welded"


class ValveMaterial(str, Enum):
    """Valve body materials."""

    BRASS_STANDARD = "brass_standard"
    BRASS_DZR = "brass_dzr"
    BRASS_NICKEL_PLATED = "brass_nickel_plated"
    STAINLESS_316 = "stainless_316"
    STAINLESS_316L = "stainless_316l"
    BRONZE = "bronze"
    ACETAL_POM = "acetal_pom"
    NYLON = "nylon"


class FuelValveSpec(BaseModel):
    """Specification for a fuel system valve."""

    model_config = {"from_attributes": True}

    valve_id: str = Field(
        ..., description="Unique valve identifier"
    )
    valve_type: ValveType
    body_material: ValveMaterial
    seal_material: str = Field(
        "ptfe_fkm",
        description="Seal/seat material (e.g., ptfe, fkm, nbr)",
    )
    nominal_size: str = Field(
        ..., description="Nominal size (e.g., DN10, 3/8 inch)"
    )
    connection_type: ConnectionType
    max_pressure_bar: float = Field(..., gt=0)
    temperature_range_min_c: float = -20
    temperature_range_max_c: float = 180
    flow_coefficient_kv: Optional[float] = Field(
        None,
        gt=0,
        description="Flow coefficient Kv in m³/h",
    )
    zeta_value: Optional[float] = Field(
        None,
        ge=0,
        description="Pressure loss coefficient (dimensionless)",
    )
    is_fail_safe_closed: Optional[bool] = Field(
        None,
        description="True for solenoid: closes on power loss",
    )
    voltage_dc: Optional[float] = Field(
        None, description="Operating voltage for solenoid valves"
    )
    current_a: Optional[float] = Field(
        None, description="Operating current for solenoid valves"
    )
    manufacturer: Optional[str] = None
    model_number: Optional[str] = None
    approved_fuel_types: list[str] = Field(default_factory=list)


class FuelFittingSpec(BaseModel):
    """Specification for a fuel line fitting."""

    model_config = {"from_attributes": True}

    fitting_id: str = Field(
        ..., description="Unique fitting identifier"
    )
    fitting_type: FittingType
    body_material: ValveMaterial
    connection_a: ConnectionType
    connection_b: ConnectionType
    size_a: str = Field(
        ..., description="Size of connection A (e.g., 10mm, 3/8 BSP)"
    )
    size_b: str = Field(
        ..., description="Size of connection B"
    )
    max_pressure_bar: float = Field(..., gt=0)
    zeta_value: Optional[float] = Field(
        None,
        ge=0,
        description="Pressure loss coefficient",
    )
    is_self_sealing: bool = Field(
        False, description="Self-sealing when disconnected"
    )
    max_connect_cycles: Optional[int] = Field(
        None,
        gt=0,
        description="Maximum connect/disconnect cycles",
    )
    manufacturer: Optional[str] = None
    model_number: Optional[str] = None


class HoseClampSpec(BaseModel):
    """Specification for a hose clamp."""

    model_config = {"from_attributes": True}

    clamp_type: str = Field(
        ...,
        description="Clamp type: worm_gear, t_bolt, double_wire, oetiker",
    )
    material: str = Field(
        "stainless_316",
        description="Clamp material",
    )
    band_width_mm: float = Field(..., gt=0)
    clamping_range_min_mm: float = Field(..., gt=0)
    clamping_range_max_mm: float = Field(..., gt=0)
    recommended_torque_nm: float = Field(..., gt=0)
    has_constant_torque: bool = Field(
        False, description="Has spring element for constant pressure"
    )
```

---

## ANHANG K — Pydantic v2 Modelle: Fehlerbild

```python
"""AYDI Pydantic v2 Models: Fuel Line Fault Patterns."""

from __future__ import annotations

from enum import Enum
from typing import Optional

from pydantic import BaseModel, Field


class FaultSeverity(str, Enum):
    """Severity levels for fuel system faults."""

    CRITICAL = "critical"
    HIGH = "high"
    MEDIUM = "medium"
    LOW = "low"
    INFORMATIONAL = "informational"


class FaultCategory(str, Enum):
    """Categories of fuel system faults."""

    LEAKAGE = "leakage"
    CORROSION = "corrosion"
    MATERIAL_DEGRADATION = "material_degradation"
    BLOCKAGE = "blockage"
    PERMEATION = "permeation"
    VIBRATION_FATIGUE = "vibration_fatigue"
    INSTALLATION_ERROR = "installation_error"
    BIOLOGICAL = "biological"
    THERMAL = "thermal"
    GALVANIC = "galvanic"


class FuelLineFault(BaseModel):
    """A fault pattern in the fuel line system."""

    model_config = {"from_attributes": True}

    fault_id: str = Field(
        ...,
        description="Fault pattern identifier (e.g., F01)",
        examples=["F01"],
    )
    name_de: str = Field(
        ..., description="Fault name in German"
    )
    name_en: str = Field(
        ..., description="Fault name in English"
    )
    category: FaultCategory
    severity: FaultSeverity
    description_de: str = Field(
        ..., description="Detailed description in German"
    )
    typical_location: str = Field(
        ..., description="Where this fault typically occurs"
    )
    root_causes: list[str] = Field(
        ..., description="List of root causes"
    )
    time_to_failure_years_min: Optional[float] = Field(
        None, ge=0, description="Minimum time to failure in years"
    )
    time_to_failure_years_max: Optional[float] = Field(
        None, ge=0, description="Maximum time to failure in years"
    )
    detection_methods: list[str] = Field(
        ..., description="How to detect this fault"
    )
    immediate_actions: list[str] = Field(
        ..., description="Immediate corrective actions"
    )
    prevention_measures: list[str] = Field(
        ..., description="How to prevent this fault"
    )
    affected_materials: list[str] = Field(
        default_factory=list,
        description="Materials susceptible to this fault",
    )
    affected_fuel_types: list[str] = Field(
        default_factory=list,
        description="Fuel types that contribute to this fault",
    )
    fire_risk: bool = Field(
        False, description="Does this fault pose a fire risk?"
    )
    environmental_risk: bool = Field(
        False, description="Does this fault pose an environmental risk?"
    )
    visual_indicators: list[str] = Field(
        default_factory=list,
        description="Visual signs for photo-based detection",
    )
    confidence: str = Field(
        "documented", description="Confidence level for this fault pattern"
    )


class FaultAtlas(BaseModel):
    """Collection of all fuel line fault patterns."""

    model_config = {"from_attributes": True}

    version: str = Field("1.0", description="Atlas version")
    faults: list[FuelLineFault] = Field(
        default_factory=list, description="All registered fault patterns"
    )
    total_faults: int = Field(0, ge=0)

    def get_critical_faults(self) -> list[FuelLineFault]:
        """Return only critical severity faults."""
        return [f for f in self.faults if f.severity == FaultSeverity.CRITICAL]

    def get_faults_by_category(
        self, category: FaultCategory
    ) -> list[FuelLineFault]:
        """Return faults filtered by category."""
        return [f for f in self.faults if f.category == category]
```

---

## ANHANG L — Pydantic v2 Modelle: Inspektion

```python
"""AYDI Pydantic v2 Models: Fuel Line Inspection."""

from __future__ import annotations

from datetime import date, datetime
from enum import Enum
from typing import Optional

from pydantic import BaseModel, Field


class InspectionType(str, Enum):
    """Types of fuel line inspection."""

    VISUAL = "visual"
    PRESSURE_TEST = "pressure_test"
    PERMEATION_TEST = "permeation_test"
    TORQUE_CHECK = "torque_check"
    MATERIAL_HARDNESS = "material_hardness"
    ULTRASONIC = "ultrasonic"
    GAS_DETECTION = "gas_detection"
    COMPLETE_ANNUAL = "complete_annual"
    PRE_PURCHASE = "pre_purchase"
    PRE_VOYAGE = "pre_voyage"


class InspectionResult(str, Enum):
    """Result categories."""

    PASS = "pass"
    PASS_WITH_NOTES = "pass_with_notes"
    FAIL_MINOR = "fail_minor"
    FAIL_MAJOR = "fail_major"
    FAIL_CRITICAL = "fail_critical"
    NOT_INSPECTED = "not_inspected"
    NOT_ACCESSIBLE = "not_accessible"


class LineInspectionItem(BaseModel):
    """Single inspection item for a fuel line component."""

    model_config = {"from_attributes": True}

    component_id: str = Field(
        ..., description="ID of inspected component"
    )
    component_type: str = Field(
        ..., description="Type (hose, pipe, valve, fitting, clamp)"
    )
    inspection_type: InspectionType
    result: InspectionResult
    findings_de: str = Field(
        "", description="Findings in German"
    )
    fault_ids: list[str] = Field(
        default_factory=list,
        description="Related fault pattern IDs from atlas",
    )
    measurement_value: Optional[float] = Field(
        None, description="Measured value if applicable"
    )
    measurement_unit: Optional[str] = Field(
        None, description="Unit of measurement"
    )
    photo_ids: list[str] = Field(
        default_factory=list,
        description="IDs of inspection photos",
    )
    action_required: str = Field(
        "",
        description="Required action: none, monitor, repair, replace",
    )
    action_deadline: Optional[date] = Field(
        None, description="Deadline for required action"
    )
    confidence: str = Field(
        "visual_medium", description="Confidence level"
    )


class FuelLineInspection(BaseModel):
    """Complete fuel line system inspection report."""

    model_config = {"from_attributes": True}

    inspection_id: str = Field(
        ..., description="Unique inspection identifier"
    )
    vessel_id: str
    inspection_date: datetime
    inspector_name: str = Field(
        ..., description="Name of inspector / surveyor"
    )
    inspector_qualification: str = Field(
        "", description="Qualification (e.g., IIMS, YDSA)"
    )
    inspection_type: InspectionType
    overall_result: InspectionResult
    items: list[LineInspectionItem] = Field(
        default_factory=list
    )
    summary_de: str = Field(
        "", description="Executive summary in German"
    )
    critical_findings: int = Field(0, ge=0)
    major_findings: int = Field(0, ge=0)
    minor_findings: int = Field(0, ge=0)
    next_inspection_date: Optional[date] = None
    iso_10088_compliant: Optional[bool] = None
    abyc_compliant: Optional[bool] = None
    notes: list[str] = Field(default_factory=list)
```

---

## ANHANG M — Pydantic v2 Modelle: Bewertungsschema

```python
"""AYDI Pydantic v2 Models: Fuel Line Scoring."""

from __future__ import annotations

from enum import Enum
from typing import Optional

from pydantic import BaseModel, Field


class ScoreCategory(str, Enum):
    """Scoring categories for fuel line systems."""

    MATERIAL_QUALITY = "material_quality"
    INSTALLATION_QUALITY = "installation_quality"
    AGE_CONDITION = "age_condition"
    COMPLIANCE = "compliance"
    SAFETY = "safety"
    MAINTAINABILITY = "maintainability"
    DOCUMENTATION = "documentation"
    OVERALL = "overall"


class FuelLineScore(BaseModel):
    """Score for a single category."""

    model_config = {"from_attributes": True}

    category: ScoreCategory
    score: float = Field(
        ..., ge=0, le=100, description="Score 0-100"
    )
    weight: float = Field(
        ..., gt=0, le=1.0, description="Weight in overall score"
    )
    findings_de: list[str] = Field(
        default_factory=list,
        description="Findings that contributed to this score",
    )
    confidence: str = Field("estimated")
    deductions: list[dict] = Field(
        default_factory=list,
        description="Individual deductions with reason and points",
    )


class FuelLineAssessment(BaseModel):
    """Complete assessment of a fuel line system."""

    model_config = {"from_attributes": True}

    vessel_id: str
    system_id: str
    assessment_date: str = Field(
        ..., description="ISO 8601 date string"
    )
    category_scores: list[FuelLineScore] = Field(
        default_factory=list
    )
    overall_score: float = Field(
        ..., ge=0, le=100, description="Weighted overall score"
    )
    overall_rating: str = Field(
        ...,
        description="Rating: excellent (90+), good (75-89), "
        "acceptable (60-74), poor (40-59), critical (<40)",
    )
    critical_issues: list[str] = Field(default_factory=list)
    recommendations_de: list[str] = Field(
        default_factory=list,
        description="Prioritized recommendations in German",
    )
    estimated_repair_cost_eur: Optional[float] = Field(
        None, ge=0, description="Estimated cost to address all findings"
    )
    confidence: str = Field("estimated")


# Scoring weights for fuel line assessment
FUEL_LINE_SCORING_WEIGHTS: dict[str, float] = {
    "material_quality": 0.20,
    "installation_quality": 0.20,
    "age_condition": 0.20,
    "compliance": 0.15,
    "safety": 0.15,
    "maintainability": 0.05,
    "documentation": 0.05,
}

# Deduction rules
DEDUCTION_RULES: list[dict] = [
    {
        "rule_id": "DED-001",
        "category": "compliance",
        "condition": "no_iso_marking_on_hose",
        "deduction": 40,
        "description_de": "Schlauch ohne ISO 7840/8469-Markierung",
    },
    {
        "rule_id": "DED-002",
        "category": "safety",
        "condition": "no_shutoff_valve_at_tank",
        "deduction": 30,
        "description_de": "Kein Absperrventil am Tank (ISO 10088 Pflicht)",
    },
    {
        "rule_id": "DED-003",
        "category": "safety",
        "condition": "gasoline_no_type_a_in_engine_room",
        "deduction": 50,
        "description_de": "Benzinsystem: Kein Typ A-Schlauch im Motorraum",
    },
    {
        "rule_id": "DED-004",
        "category": "safety",
        "condition": "gasoline_no_flame_arrestor",
        "deduction": 40,
        "description_de": "Benzinsystem: Keine Flammensperre an Tankentlüftung",
    },
    {
        "rule_id": "DED-005",
        "category": "age_condition",
        "condition": "hose_age_over_10_years",
        "deduction": 25,
        "description_de": "Kraftstoffschlauch älter als 10 Jahre",
    },
    {
        "rule_id": "DED-006",
        "category": "installation_quality",
        "condition": "single_clamp_over_12mm",
        "deduction": 15,
        "description_de": "Nur eine Schlauchklemme bei ID ≥12mm",
    },
    {
        "rule_id": "DED-007",
        "category": "material_quality",
        "condition": "zinc_plated_clamps",
        "deduction": 20,
        "description_de": "Verzinkte Schlauchklemmen statt Edelstahl 316",
    },
    {
        "rule_id": "DED-008",
        "category": "installation_quality",
        "condition": "hose_kinked",
        "deduction": 20,
        "description_de": "Kraftstoffschlauch geknickt",
    },
    {
        "rule_id": "DED-009",
        "category": "safety",
        "condition": "no_flexible_section_at_engine",
        "deduction": 15,
        "description_de": "Kein flexibles Zwischenstück am Motoranschluss",
    },
    {
        "rule_id": "DED-010",
        "category": "compliance",
        "condition": "deck_fill_no_fuel_label",
        "deduction": 15,
        "description_de": "Einfüllstutzen ohne Kraftstoff-Kennzeichnung",
    },
]
```

---

## ANHANG N — Pydantic v2 Modelle: Troubleshooting

```python
"""AYDI Pydantic v2 Models: Fuel Line Troubleshooting Trees."""

from __future__ import annotations

from enum import Enum
from typing import Optional

from pydantic import BaseModel, Field


class NodeType(str, Enum):
    """Types of decision tree nodes."""

    SYMPTOM = "symptom"
    QUESTION = "question"
    CHECK = "check"
    DIAGNOSIS = "diagnosis"
    ACTION = "action"
    WARNING = "warning"


class TroubleshootingNode(BaseModel):
    """A single node in the troubleshooting decision tree."""

    model_config = {"from_attributes": True}

    node_id: str = Field(
        ..., description="Unique node identifier"
    )
    node_type: NodeType
    text_de: str = Field(
        ..., description="Node text in German"
    )
    text_en: Optional[str] = Field(
        None, description="Node text in English"
    )
    children: list[TroubleshootingEdge] = Field(
        default_factory=list,
        description="Outgoing edges to child nodes",
    )
    related_fault_ids: list[str] = Field(
        default_factory=list,
        description="Related fault pattern IDs",
    )
    severity: Optional[str] = Field(
        None, description="Severity if diagnosis node"
    )
    estimated_cost_eur: Optional[float] = Field(
        None, ge=0, description="Estimated repair cost"
    )


class TroubleshootingEdge(BaseModel):
    """An edge (answer/condition) connecting two nodes."""

    model_config = {"from_attributes": True}

    label_de: str = Field(
        ..., description="Edge label in German (e.g., 'Ja', 'Nein')"
    )
    target_node_id: str = Field(
        ..., description="ID of the target node"
    )
    probability: Optional[float] = Field(
        None,
        ge=0,
        le=1,
        description="Estimated probability of this path",
    )


class TroubleshootingTree(BaseModel):
    """A complete troubleshooting decision tree."""

    model_config = {"from_attributes": True}

    tree_id: str = Field(
        ..., description="Unique tree identifier"
    )
    name_de: str = Field(
        ..., description="Tree name in German"
    )
    name_en: Optional[str] = Field(
        None, description="Tree name in English"
    )
    description_de: str = Field(
        "", description="Tree description in German"
    )
    entry_symptom_de: str = Field(
        ..., description="Entry symptom that triggers this tree"
    )
    root_node_id: str = Field(
        ..., description="ID of the root node"
    )
    nodes: list[TroubleshootingNode] = Field(
        default_factory=list, description="All nodes in the tree"
    )
    total_nodes: int = Field(0, ge=0)
    max_depth: int = Field(0, ge=0)


class TroubleshootingCollection(BaseModel):
    """Collection of all troubleshooting trees for fuel lines."""

    model_config = {"from_attributes": True}

    version: str = Field("1.0")
    trees: list[TroubleshootingTree] = Field(
        default_factory=list
    )

    def get_tree_for_symptom(
        self, keyword: str
    ) -> list[TroubleshootingTree]:
        """Find trees matching a symptom keyword."""
        keyword_lower = keyword.lower()
        return [
            t
            for t in self.trees
            if keyword_lower in t.entry_symptom_de.lower()
            or keyword_lower in t.name_de.lower()
        ]
```

---

## ANHANG O — Pydantic v2 Modelle: Hersteller-Katalog

```python
"""AYDI Pydantic v2 Models: Fuel Line Manufacturer Catalog."""

from __future__ import annotations

from typing import Optional

from pydantic import BaseModel, Field, HttpUrl


class ManufacturerContact(BaseModel):
    """Manufacturer contact information."""

    model_config = {"from_attributes": True}

    company_name: str
    country: str
    city: Optional[str] = None
    website: Optional[str] = Field(
        None, description="Manufacturer website URL"
    )
    catalog_url: Optional[str] = Field(
        None, description="Online catalog URL"
    )
    email: Optional[str] = None
    phone: Optional[str] = None
    founded_year: Optional[int] = Field(None, ge=1800)


class ProductEntry(BaseModel):
    """A single product in the manufacturer catalog."""

    model_config = {"from_attributes": True}

    model_number: str = Field(
        ..., description="Manufacturer model/part number"
    )
    product_name: str = Field(
        ..., description="Product name/description"
    )
    product_category: str = Field(
        ...,
        description="Category: hose, valve, fitting, clamp, deck_fill, vent",
    )
    fuel_types: list[str] = Field(
        default_factory=list,
        description="Compatible fuel types",
    )
    sizes_available: list[str] = Field(
        default_factory=list,
        description="Available sizes (e.g., 8mm, 10mm, 3/8 inch)",
    )
    material: str = Field(
        "", description="Primary material"
    )
    certifications: list[str] = Field(
        default_factory=list,
        description="Certifications (ISO 7840, ABYC, USCG, etc.)",
    )
    price_eur_approx: Optional[float] = Field(
        None, ge=0, description="Approximate price in EUR"
    )
    price_unit: str = Field(
        "piece", description="Price unit: piece, meter, set"
    )
    quality_tier: str = Field(
        "mid",
        description="Quality tier: budget, mid, premium",
    )
    notes: str = Field("", description="Additional notes")


class ManufacturerCatalog(BaseModel):
    """Complete manufacturer catalog entry."""

    model_config = {"from_attributes": True}

    manufacturer_id: str = Field(
        ..., description="Unique manufacturer identifier"
    )
    contact: ManufacturerContact
    specialization: str = Field(
        ...,
        description="Primary specialization (hoses, fittings, valves, etc.)",
    )
    quality_rating: float = Field(
        ...,
        ge=0,
        le=100,
        description="AYDI quality rating 0-100",
    )
    products: list[ProductEntry] = Field(
        default_factory=list
    )
    strengths_de: list[str] = Field(
        default_factory=list,
        description="Key strengths in German",
    )
    weaknesses_de: list[str] = Field(
        default_factory=list,
        description="Known weaknesses in German",
    )
    distribution_europe: str = Field(
        "",
        description="European distribution: direct, dealer, distributor",
    )
    oem_customers: list[str] = Field(
        default_factory=list,
        description="Known OEM customers (boat builders)",
    )
```

---

## ANHANG P — Pydantic v2 Modelle: Wartungsplan

```python
"""AYDI Pydantic v2 Models: Fuel Line Maintenance Planning."""

from __future__ import annotations

from datetime import date
from enum import Enum
from typing import Optional

from pydantic import BaseModel, Field


class MaintenanceInterval(str, Enum):
    """Maintenance interval types."""

    ANNUAL = "annual"
    BIENNIAL = "biennial"
    EVERY_3_YEARS = "every_3_years"
    EVERY_5_YEARS = "every_5_years"
    EVERY_10_YEARS = "every_10_years"
    SEASONAL = "seasonal"
    AFTER_HOURS = "after_engine_hours"
    ON_CONDITION = "on_condition"


class MaintenancePriority(str, Enum):
    """Maintenance task priority."""

    MANDATORY = "mandatory"
    RECOMMENDED = "recommended"
    OPTIONAL = "optional"


class MaintenanceTask(BaseModel):
    """A single maintenance task for the fuel line system."""

    model_config = {"from_attributes": True}

    task_id: str = Field(..., description="Unique task ID")
    name_de: str = Field(
        ..., description="Task name in German"
    )
    description_de: str = Field(
        ..., description="Detailed description in German"
    )
    interval: MaintenanceInterval
    interval_hours: Optional[int] = Field(
        None, gt=0, description="Interval in engine hours if applicable"
    )
    priority: MaintenancePriority
    estimated_duration_minutes: int = Field(
        ..., gt=0, description="Estimated time in minutes"
    )
    requires_professional: bool = Field(
        False,
        description="Requires professional/yard work",
    )
    tools_required: list[str] = Field(
        default_factory=list, description="Required tools"
    )
    spare_parts: list[str] = Field(
        default_factory=list,
        description="Spare parts needed",
    )
    estimated_cost_eur: float = Field(
        0, ge=0, description="Estimated cost including parts"
    )
    applicable_fuel_types: list[str] = Field(
        default_factory=list,
        description="Applicable fuel types (empty = all)",
    )
    procedure_steps_de: list[str] = Field(
        default_factory=list,
        description="Step-by-step procedure in German",
    )


class MaintenancePlan(BaseModel):
    """Complete fuel line maintenance plan for a vessel."""

    model_config = {"from_attributes": True}

    vessel_id: str
    plan_id: str = Field(
        ..., description="Unique plan identifier"
    )
    fuel_type: str
    engine_type: str = Field(
        "", description="Engine manufacturer and model"
    )
    tasks: list[MaintenanceTask] = Field(
        default_factory=list
    )
    last_complete_inspection: Optional[date] = None
    next_complete_inspection: Optional[date] = None
    total_annual_cost_eur: float = Field(
        0,
        ge=0,
        description="Estimated total annual maintenance cost",
    )
    notes: list[str] = Field(default_factory=list)
```

---

## ANHANG Q — Pydantic v2 Modelle: Kostenkalkulation

```python
"""AYDI Pydantic v2 Models: Fuel Line Cost Estimation."""

from __future__ import annotations

from enum import Enum
from typing import Optional

from pydantic import BaseModel, Field


class CostCategory(str, Enum):
    """Cost categories for fuel line work."""

    MATERIAL_HOSES = "material_hoses"
    MATERIAL_PIPES = "material_pipes"
    MATERIAL_FITTINGS = "material_fittings"
    MATERIAL_VALVES = "material_valves"
    MATERIAL_CLAMPS = "material_clamps"
    MATERIAL_DECK_HARDWARE = "material_deck_hardware"
    MATERIAL_CONSUMABLES = "material_consumables"
    LABOR_YARD = "labor_yard"
    LABOR_SELF = "labor_self"
    DISPOSAL = "disposal"
    CERTIFICATION = "certification"


class CostLineItem(BaseModel):
    """Single cost line item."""

    model_config = {"from_attributes": True}

    item_id: str
    category: CostCategory
    description_de: str = Field(
        ..., description="Item description in German"
    )
    quantity: float = Field(..., gt=0)
    unit: str = Field(
        ..., description="Unit: piece, meter, hour, set"
    )
    unit_price_eur: float = Field(..., ge=0)
    total_eur: float = Field(..., ge=0)
    manufacturer: Optional[str] = None
    model_number: Optional[str] = None
    confidence: str = Field(
        "estimated",
        description="Price confidence: measured (actual quote), estimated",
    )


class FuelLineCostEstimate(BaseModel):
    """Complete cost estimate for fuel line work."""

    model_config = {"from_attributes": True}

    estimate_id: str
    vessel_id: str
    scope_de: str = Field(
        ...,
        description="Scope of work in German (e.g., Kompletttausch, Reparatur)",
    )
    line_items: list[CostLineItem] = Field(
        default_factory=list
    )
    subtotal_material_eur: float = Field(0, ge=0)
    subtotal_labor_eur: float = Field(0, ge=0)
    subtotal_other_eur: float = Field(0, ge=0)
    total_eur: float = Field(0, ge=0)
    vat_rate: float = Field(
        0.19, ge=0, le=0.30, description="VAT rate (default 19% Germany)"
    )
    total_incl_vat_eur: float = Field(0, ge=0)
    labor_rate_eur_per_hour: float = Field(
        85,
        gt=0,
        description="Yard labor rate EUR/hour",
    )
    estimated_labor_hours: float = Field(0, ge=0)
    valid_until: Optional[str] = Field(
        None, description="Estimate validity date (ISO 8601)"
    )
    notes: list[str] = Field(default_factory=list)


# Reference cost data by boat size class
REFERENCE_COSTS_FUEL_LINE_SYSTEM: list[dict] = [
    {
        "boat_class": "sailboat_8_10m",
        "engine_power_range_kw": "5-20",
        "full_replacement_material_eur": "250-450",
        "full_replacement_labor_hours": "3-5",
        "full_replacement_total_eur": "500-900",
        "annual_maintenance_eur": "30-60",
    },
    {
        "boat_class": "sailboat_10_14m",
        "engine_power_range_kw": "20-60",
        "full_replacement_material_eur": "400-700",
        "full_replacement_labor_hours": "4-7",
        "full_replacement_total_eur": "750-1.400",
        "annual_maintenance_eur": "50-100",
    },
    {
        "boat_class": "motoryacht_8_12m",
        "engine_power_range_kw": "80-250",
        "full_replacement_material_eur": "500-1.200",
        "full_replacement_labor_hours": "5-10",
        "full_replacement_total_eur": "1.000-2.200",
        "annual_maintenance_eur": "80-150",
    },
    {
        "boat_class": "motoryacht_12_18m",
        "engine_power_range_kw": "200-600",
        "full_replacement_material_eur": "1.200-3.000",
        "full_replacement_labor_hours": "10-20",
        "full_replacement_total_eur": "2.500-5.500",
        "annual_maintenance_eur": "150-300",
    },
    {
        "boat_class": "superyacht_18_25m",
        "engine_power_range_kw": "400-1500",
        "full_replacement_material_eur": "5.000-15.000",
        "full_replacement_labor_hours": "20-50",
        "full_replacement_total_eur": "10.000-25.000",
        "annual_maintenance_eur": "300-800",
    },
]
```

---

## ANHANG R — Pydantic v2 Modelle: Compliance-Prüfung

```python
"""AYDI Pydantic v2 Models: Fuel Line Compliance Checking."""

from __future__ import annotations

from enum import Enum
from typing import Optional

from pydantic import BaseModel, Field


class ComplianceStandard(str, Enum):
    """Applicable compliance standards."""

    ISO_7840 = "iso_7840"
    ISO_8469 = "iso_8469"
    ISO_10088 = "iso_10088"
    ISO_9094 = "iso_9094"
    ISO_21487 = "iso_21487"
    ABYC_H24 = "abyc_h24"
    ABYC_H33 = "abyc_h33"
    CE_2013_53_EU = "ce_2013_53_eu"
    USCG_33_CFR_183 = "uscg_33_cfr_183"
    EPA_MARINE = "epa_marine"
    CARB = "carb"
    LLOYDS = "lloyds_yacht_code"


class ComplianceStatus(str, Enum):
    """Result of compliance check."""

    COMPLIANT = "compliant"
    NON_COMPLIANT = "non_compliant"
    PARTIALLY_COMPLIANT = "partially_compliant"
    NOT_APPLICABLE = "not_applicable"
    INSUFFICIENT_DATA = "insufficient_data"


class ComplianceCheckItem(BaseModel):
    """Single compliance check item."""

    model_config = {"from_attributes": True}

    check_id: str = Field(
        ..., description="Unique check identifier"
    )
    standard: ComplianceStandard
    clause: str = Field(
        ...,
        description="Specific clause reference (e.g., ISO 10088:2013 §6.3)",
    )
    requirement_de: str = Field(
        ..., description="Requirement description in German"
    )
    status: ComplianceStatus
    finding_de: str = Field(
        "",
        description="Finding details in German",
    )
    evidence: str = Field(
        "",
        description="Evidence (measurement, photo ID, document ref)",
    )
    corrective_action_de: str = Field(
        "",
        description="Required corrective action in German",
    )
    severity: str = Field(
        "medium",
        description="Non-compliance severity: critical, major, minor",
    )
    confidence: str = Field("estimated")


class FuelLineComplianceReport(BaseModel):
    """Complete compliance report for fuel line system."""

    model_config = {"from_attributes": True}

    report_id: str
    vessel_id: str
    vessel_name: Optional[str] = None
    vessel_length_m: float = Field(..., gt=0)
    fuel_type: str
    target_standards: list[ComplianceStandard] = Field(
        default_factory=list,
        description="Standards being checked against",
    )
    check_items: list[ComplianceCheckItem] = Field(
        default_factory=list
    )
    overall_status: ComplianceStatus
    total_checks: int = Field(0, ge=0)
    compliant_checks: int = Field(0, ge=0)
    non_compliant_checks: int = Field(0, ge=0)
    compliance_percentage: float = Field(
        0, ge=0, le=100
    )
    critical_non_compliances: list[str] = Field(
        default_factory=list,
        description="List of critical NC check_ids",
    )
    summary_de: str = Field(
        "", description="Executive summary in German"
    )
    recommendations_de: list[str] = Field(
        default_factory=list
    )
    report_date: str = Field(
        ..., description="Report date ISO 8601"
    )
    assessor_name: str = Field("")
    confidence: str = Field("estimated")


# Standard compliance check templates for fuel lines
COMPLIANCE_CHECK_TEMPLATES: list[dict] = [
    {
        "check_id": "ISO10088-6.1",
        "standard": "iso_10088",
        "clause": "6.1",
        "requirement_de": "Absperrventil am Tankausgang, max. 150mm vom Tank, "
        "ohne Werkzeug bedienbar, von außerhalb des Motorraums zugänglich",
        "applies_to": ["diesel", "gasoline"],
    },
    {
        "check_id": "ISO10088-6.3",
        "standard": "iso_10088",
        "clause": "6.3",
        "requirement_de": "Kraftstoffschläuche entsprechen ISO 7840 "
        "(Motorraum) oder ISO 8469 (außerhalb), korrekt markiert",
        "applies_to": ["diesel", "gasoline"],
    },
    {
        "check_id": "ISO7840-A-GASOLINE",
        "standard": "iso_7840",
        "clause": "Type A",
        "requirement_de": "Benzinsystem: Feuerbeständiger Schlauch "
        "(Typ A1 oder A2) im Motorraum und bis 250mm außerhalb",
        "applies_to": ["gasoline", "e10", "e15"],
    },
    {
        "check_id": "ISO10088-6.5",
        "standard": "iso_10088",
        "clause": "6.5",
        "requirement_de": "Tankentlüftung vorhanden, mündet nicht "
        "in geschlossene Räume, Flammensperre bei Benzin",
        "applies_to": ["diesel", "gasoline"],
    },
    {
        "check_id": "ISO10088-6.6",
        "standard": "iso_10088",
        "clause": "6.6",
        "requirement_de": "Einfüllstutzen mit Kraftstoff-Kennzeichnung, "
        "Verwechslungsschutz",
        "applies_to": ["diesel", "gasoline"],
    },
    {
        "check_id": "ISO10088-6.7",
        "standard": "iso_10088",
        "clause": "6.7",
        "requirement_de": "Rücklaufleitung mündet über Kraftstoffspiegel "
        "in den Tank",
        "applies_to": ["diesel"],
    },
    {
        "check_id": "ISO10088-6.8",
        "standard": "iso_10088",
        "clause": "6.8",
        "requirement_de": "Leitungen gegen Beschädigung, Vibration "
        "und Korrosion geschützt; Befestigung alle 500mm",
        "applies_to": ["diesel", "gasoline"],
    },
    {
        "check_id": "ABYC-H24-24.7",
        "standard": "abyc_h24",
        "clause": "24.7",
        "requirement_de": "Benzin-System: Zwei Schlauchklemmen bei "
        "ID ≥12mm, Edelstahl-Material",
        "applies_to": ["gasoline", "e10"],
    },
    {
        "check_id": "ABYC-H24-24.15",
        "standard": "abyc_h24",
        "clause": "24.15",
        "requirement_de": "Benzin-System: Elektrischer Widerstand "
        "Leitungssystem <10⁶ Ohm (Erdung/Potentialausgleich)",
        "applies_to": ["gasoline", "e10"],
    },
    {
        "check_id": "CE-5.5.4",
        "standard": "ce_2013_53_eu",
        "clause": "Anhang I, 5.5.4",
        "requirement_de": "Entlüftung darf nicht in geschlossene Räume münden",
        "applies_to": ["diesel", "gasoline"],
    },
]
```

---

> **Ende der Wissensdatei 19.03**
> **Zeilen:** ~3.800
> **Letzte Prüfung:** 2026-05-02
> **Nächste Überarbeitung geplant:** 2026-11-01
> **Confidence-Gesamtbewertung:** documented (Normen, Hersteller-TDS), estimated (Preise, Erfahrungswerte)
