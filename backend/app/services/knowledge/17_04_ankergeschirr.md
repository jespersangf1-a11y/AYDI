---
titel: "Ankergeschirr und Zubehör"
kategorie: "Anker und Kette"
unterkategorie: "Ankergeschirr und Zubehör"
version: "2.0"
letzte_aktualisierung: "2026-04"
autor: "AYDI Maritime Knowledge Base"
---

# 17_04 — Ankergeschirr und Zubehör

---

## Inhaltsverzeichnis

1. [Einführung](#1-einführung)
2. [Ankerwirbel (Swivels)](#2-ankerwirbel-swivels)
3. [Ankerschäkel (Bow Shackles)](#3-ankerschäkel-bow-shackles)
4. [Kettenvorläufer](#4-kettenvorläufer)
5. [Ankerbojen und Ankerbälle](#5-ankerbojen-und-ankerbälle)
6. [Triplinen](#6-triplinen)
7. [Ankerrollen (Bow Rollers)](#7-ankerrollen-bow-rollers)
8. [Bugbeschläge und Klüsen](#8-bugbeschläge-und-klüsen)
9. [Ankerkästen und -taschen](#9-ankerkästen-und--taschen)
10. [Ankerlicht und Signale](#10-ankerlicht-und-signale)
11. [Kettenstopper (Chain Stoppers / Devil's Claw)](#11-kettenstopper-chain-stoppers--devils-claw)
12. [Ankermarkierung](#12-ankermarkierung)
13. [Fehlerbild-Atlas](#13-fehlerbild-atlas)
14. [Troubleshooting](#14-troubleshooting)
15. [FAQ](#15-faq)
16. [Glossar](#16-glossar)
17. [Schnell-Referenz](#17-schnell-referenz)
18. [ANHANG A–H: Fallstudien](#18-anhang-a-h-fallstudien)
19. [ANHANG I–R: Pydantic v2 Datenmodelle](#19-anhang-i-r-pydantic-v2-datenmodelle)

---

## 1. Einführung

### 1.1 Zweck dieses Dokuments

Dieses Dokument bildet die zentrale Wissensbasis für alle Komponenten des
Ankergeschirrs und des zugehörigen Zubehörs im Yachtdesign. Es dient als
Referenz für die AYDI-Analyse-Engine zur Bewertung, Dimensionierung und
Fehlerdiagnose sämtlicher Bauteile, die den Anker mit dem Boot verbinden
und das sichere Ankern ermöglichen.

Unter „Ankergeschirr" fasst man alle Beschlag- und Verbindungsteile zusammen,
die zwischen Anker und Ankerwindenanlage bzw. Klampe stehen. Diese Komponenten
sind sicherheitskritisch: Ein einziges versagendes Glied — sei es ein
korrodierter Wirbel, ein unterdimensionierter Schäkel oder eine gebrochene
Ankerrolle — kann zum Verlust des Ankers und im schlimmsten Fall zum Verlust
des Bootes führen.

### 1.2 Relevanz für die Yachtkonstruktion

Das Ankergeschirr beeinflusst zahlreiche Aspekte des Yachtdesigns:

- **Strukturell**: Lasteinleitung am Bug, Verstärkung der Bugrolle, Klüsen-Integration
- **Sicherheit**: Bruchlast-Kette aller Verbindungen, Redundanz bei schwerem Wetter
- **Ergonomie**: Handhabbarkeit beim An- und Ablegen, Zugänglichkeit der Komponenten
- **Gewichtsverteilung**: Vorschiffslast durch Anker, Kette und Beschläge
- **Ästhetik**: Saubere Bugrolle-Integration, verdeckte Ankerkästen
- **Wartung**: Korrosionsschutz, Austauschbarkeit einzelner Komponenten
- **Kosten**: Beschaffung, Installation, Lebensdauerkosten

### 1.3 Systematik der Ankergeschirr-Kette

Die Belastungskette beim Ankern verläuft wie folgt:

```
Ankergrund → Anker → Ankerwirbel → Schäkel → Kette/Leine →
→ Ankerrolle / Klüse → Kettenstopper → Klampe / Winde
```

**Fundamentalregel**: Die Bruchlast jedes einzelnen Gliedes muss mindestens
der Bruchlast der Kette entsprechen. Ein System ist nur so stark wie sein
schwächstes Glied.

### 1.4 Historische Entwicklung

| Zeitraum | Entwicklung | Merkmale |
|----------|------------|----------|
| Vor 1900 | Schmiedeeiserne Beschläge | Handgeschmiedete Schäkel, Holzrollen |
| 1900–1950 | Stahlguss-Komponenten | Erste standardisierte Schäkelgrößen |
| 1950–1980 | Edelstahl-Einführung | 304er Stahl, erste Drehwirbel |
| 1980–2000 | 316L-Standard | Höhere Korrosionsbeständigkeit, Leichtbau |
| 2000–2015 | High-Performance-Wirbel | Kugellager-Wirbel, geschmiedete Schäkel |
| 2015–heute | Integrierte Systeme | Ultra-Wirbel, selbstausrichtende Rollen, smarte Markierung |

### 1.5 Normative Grundlagen

Relevante Normen für Ankergeschirr:

| Norm | Titel | Relevanz |
|------|-------|----------|
| ISO 15084:2003 | Ankern, Vertäuen und Schleppen — Starke Punkte | Belastungsanforderungen für Beschläge |
| ISO 15085:2003 | Mann-über-Bord-Verhütung | Sicherheit am Bug |
| DIN 82101 | Schäkel — Bügel- und Gabelschäkel | Schäkelmaße und -toleranzen |
| DIN 82016 | Ladeschäkel (Cargo Shackles) | Lade-/Vertäugeschirr, Schäkelmaße und -toleranzen |
| CE 2013/53/EU | Sportboot-Richtlinie | Gesamtsicherheit |
| ISO 4565 | Ankerausrüstung für Yachten | Dimensionierungsgrundlage |
| ABYC H-40 | Anchoring, Mooring and Strong Points | US-Standard für Ankerausrüstung |
| EN 13411-3 | Pressklemmen für Drahtseile (Ferrules and ferrule-securing) | Relevant für Kettenvorläufer |

> ✅ Aufgeloest (Audit): DIN 82016 = „Ladeschäkel" (Cargo Shackles / Lade- und Vertäugeschirr), NICHT „Drehwirbel für Ketten" — Zuordnung im Text korrigiert. Norm-Confidence: documented. Quelle: DIN 82016 „Cargo lifting gear — Accessories and fittings for lifting and mooring — Cargo shackles" (ANSI Webstore / AFNOR / GlobalSpec).

### 1.6 Bootklassen-Kalibrierung

Die Dimensionierung des Ankergeschirrs richtet sich nach der Bootsgröße:

| Bootsklasse | LOA | Displacement | Typische Kette | WLL Wirbel/Schäkel |
|-------------|-----|-------------|----------------|---------------------|
| Kleinkreuzer | 6–8 m | 1–3 t | 6 mm | ≥ 800 kg |
| Fahrtenyacht | 8–12 m | 3–8 t | 8 mm | ≥ 1.500 kg |
| Blauwasser-Yacht | 10–15 m | 8–18 t | 10 mm | ≥ 2.500 kg |
| Performance-Cruiser | 12–18 m | 8–20 t | 10–12 mm | ≥ 3.000 kg |
| Ketch/Ketsch | 15–22 m | 15–35 t | 12–13 mm | ≥ 4.000 kg |
| Superyacht | 20–40 m | 30–200 t | 13–16 mm | ≥ 6.000 kg |

### 1.7 Einordnung im AYDI-Analysesystem

Innerhalb der AYDI-Analyse wird das Ankergeschirr in folgenden Modulen bewertet:

- **Strukturanalyse**: Lasteinleitung, Verstärkungsbereiche, Materialstärken
- **Compliance**: CE-Konformität, Bruchlastketten-Nachweis
- **Ergonomie**: Handhabbarkeit, Zugänglichkeit, Bedienkräfte
- **Materialanalyse**: Korrosionsbeständigkeit, Materialpaarung, galvanische Korrosion
- **Kostenanalyse**: Anschaffung, Austauschkosten, Lifecycle
- **Visuelle Analyse**: Zustandserkennung via Fotos, Korrosionserkennung

### 1.8 Confidence-Level-Zuordnung

| Datenquelle | Confidence-Level | Beispiel |
|-------------|-----------------|----------|
| CAD-Modell mit Beschlagspezifikation | `measured` | Exakte Schäkelgröße, Wirbel-WLL |
| Foto der Bug-/Ankerinstallation | `visual_high` bis `visual_low` | Wirbeltyp erkennbar, Korrosion sichtbar |
| Herstellerdatenblatt | `documented` | WLL, Bruchlast, Gewicht |
| Bootsklasse-Schätzung | `estimated` | Typische Schäkelgröße für 12m Yacht |
| Servicebericht | `documented` | Zustandsbeschreibung, Austauschhistorie |
| Rechnerische Ableitung | `calculated` | WLL aus Kettengröße abgeleitet |

---

## 2. Ankerwirbel (Swivels)

### 2.1 Funktion und Bedeutung

Der Ankerwirbel (engl. swivel) verbindet Ankerkette und Anker. Seine
Hauptfunktion ist die freie Drehung der Kette relativ zum Anker, um
Torque (Verdrehen) der Kette zu verhindern. Ohne Wirbel dreht sich
die gesamte Kette beim Schwojen und verknäult sich im Kettenkasten.

**Kritische Anforderungen:**
- Freie 360°-Rotation unter Last
- WLL mindestens gleich der Ketten-WLL
- Korrosionsbeständigkeit in Salzwasser (316L Minimum)
- Passgenauigkeit zur Kettengröße (ISO-kalibriert)
- Kompakte Bauform für sauberen Einzug über die Bugrolle

### 2.2 Bauformen

#### 2.2.1 Gabel-Gabel-Wirbel (Jaw-Jaw)

- **Beschreibung**: Beide Enden als offene Gabel mit Bolzen
- **Vorteile**: Einfache Montage, beidseitig demontierbar
- **Nachteile**: Bolzen können sich lösen, breitere Bauform
- **Einsatz**: Seltener bei modernen Ankerwirbeln, eher bei Vertäuung

#### 2.2.2 Gabel-Auge-Wirbel (Jaw-Eye)

- **Beschreibung**: Ein Ende Gabel, anderes Ende geschlossenes Auge
- **Vorteile**: Augenseite dauerhaft mit Kette verbunden
- **Nachteile**: Nur einseitig demontierbar
- **Einsatz**: Standard für viele Ankerwirbel

#### 2.2.3 Auge-Auge-Wirbel (Eye-Eye)

- **Beschreibung**: Beide Enden als geschlossene Augen
- **Vorteile**: Keine lösbaren Bolzen, kompakt
- **Nachteile**: Montage nur mit Schäkeln möglich
- **Einsatz**: Häufig bei Ketten-Ketten-Verbindungen

#### 2.2.4 Bügelwirbel (Shackle-Type)

- **Beschreibung**: Integrierter Schäkel an einem oder beiden Enden
- **Vorteile**: Direkte Kettenmontage ohne zusätzlichen Schäkel
- **Nachteile**: Nicht universell kompatibel
- **Einsatz**: Herstellerspezifische Lösungen (z.B. Ultra Swivel)

#### 2.2.5 Kugellager-Wirbel (Ball-Bearing)

- **Beschreibung**: Integriertes Kugellager für reibungsarme Drehung
- **Vorteile**: Leichtgängig auch unter Last, geringerer Verschleiß
- **Nachteile**: Höherer Preis, Lager wartbar
- **Einsatz**: Premium-Segment, Blauwasser-Yachten

### 2.3 Hersteller-Datenbank

#### 2.3.1 Mantus Marine Swivels

Mantus Marine aus Austin, Texas, ist einer der führenden Anbieter von
hochfesten Ankerwirbeln. Die Wirbel zeichnen sich durch geschmiedeten
316L-Edelstahl und hohe Bruchlasten aus.

| Modell | Kette (mm) | WLL (kg) | Bruchlast (kg) | Gewicht (g) | Preis (EUR) |
|--------|-----------|----------|----------------|-------------|-------------|
| Mantus Swivel M1 | 6 | 1.360 | 4.082 | 280 | 89 |
| Mantus Swivel M1 | 8 | 2.270 | 6.800 | 480 | 109 |
| Mantus Swivel M1 | 10 | 3.630 | 10.886 | 780 | 139 |
| Mantus Swivel M1 | 12 | 4.540 | 13.600 | 1.120 | 179 |
| Mantus Swivel M1 | 13 | 5.440 | 16.300 | 1.380 | 209 |
| Mantus Swivel M1 | 16 | 7.260 | 21.772 | 2.100 | 289 |

**Technische Merkmale:**
- Material: Geschmiedeter 316L-Edelstahl
- Drehung: 360° frei unter Last
- Oberfläche: Poliert
- Befestigung: Gabel-Gabel mit verschraubtem Bolzen
- Besonderheit: Patentierte Bolzenverriegelung gegen Lösen

#### 2.3.2 Kong Marine Swivels

Kong, italienischer Hersteller aus Lecco, produziert hochwertige marine
Drehwirbel mit langer Tradition in der Seil- und Hebetechnik.

| Modell | Kette (mm) | WLL (kg) | Bruchlast (kg) | Gewicht (g) | Preis (EUR) |
|--------|-----------|----------|----------------|-------------|-------------|
| Kong Anchor Swivel | 6–7 | 1.000 | 4.000 | 260 | 79 |
| Kong Anchor Swivel | 8 | 1.500 | 6.000 | 420 | 99 |
| Kong Anchor Swivel | 10 | 2.500 | 10.000 | 700 | 129 |
| Kong Anchor Swivel | 12 | 3.500 | 14.000 | 1.050 | 169 |
| Kong Anchor Swivel | 13–14 | 5.000 | 20.000 | 1.400 | 219 |
| Kong Anchor Swivel | 16 | 6.500 | 26.000 | 2.200 | 299 |

**Technische Merkmale:**
- Material: AISI 316 Edelstahl, warmgeschmiedet
- Drehung: Kugellager-unterstützt (ab 10mm-Variante)
- Oberfläche: Elektropoliert
- Befestigung: Gabel-Auge
- Besonderheit: CE-zertifiziert nach Maschinenrichtlinie
- Herkunft: Made in Italy

#### 2.3.3 Ultra Marine Swivels

Ultra Marine aus Neuseeland stellt den bekannten Ultra Swivel her, der
sich durch eine besonders flache Bauform auszeichnet und dadurch
optimal über die Bugrolle einzieht.

| Modell | Kette (mm) | WLL (kg) | Bruchlast (kg) | Gewicht (g) | Preis (EUR) |
|--------|-----------|----------|----------------|-------------|-------------|
| Ultra Swivel | 6–8 | 1.500 | 5.400 | 350 | 99 |
| Ultra Swivel | 8–10 | 2.500 | 9.000 | 580 | 139 |
| Ultra Swivel | 10–12 | 4.000 | 14.400 | 950 | 189 |
| Ultra Swivel | 12–13 | 5.500 | 19.800 | 1.350 | 239 |
| Ultra Swivel | 14–16 | 7.500 | 27.000 | 2.050 | 329 |
| Ultra Flip Swivel | 6–8 | 1.500 | 5.400 | 400 | 119 |
| Ultra Flip Swivel | 8–10 | 2.500 | 9.000 | 650 | 159 |
| Ultra Flip Swivel | 10–12 | 4.000 | 14.400 | 1.050 | 209 |
| Ultra Flip Swivel | 12–13 | 5.500 | 19.800 | 1.500 | 269 |

**Technische Merkmale:**
- Material: 316 Edelstahl, Feinguss + CNC-bearbeitet
- Drehung: Frei 360°, Low-Profile-Design
- Oberfläche: Poliert, passiviert
- Befestigung: Integrierter Schäkelkopf
- Besonderheit: Flush-fit über Bugrolle, patentiertes Profil
- Ultra Flip Swivel: Zusätzliche Schwenkfunktion für Ankerausrichtung

#### 2.3.4 Wichard Marine Swivels

Wichard, französischer Premiumhersteller aus Thiers, ist bekannt für
höchste Qualitätsstandards und Langlebigkeit.

| Modell | Kette (mm) | WLL (kg) | Bruchlast (kg) | Gewicht (g) | Preis (EUR) |
|--------|-----------|----------|----------------|-------------|-------------|
| Wichard HR Swivel | 6 | 1.200 | 4.800 | 290 | 119 |
| Wichard HR Swivel | 8 | 2.000 | 8.000 | 490 | 149 |
| Wichard HR Swivel | 10 | 3.200 | 12.800 | 820 | 189 |
| Wichard HR Swivel | 12 | 4.500 | 18.000 | 1.200 | 239 |
| Wichard HR Swivel | 13 | 5.800 | 23.200 | 1.500 | 289 |
| Wichard HR Swivel | 16 | 7.500 | 30.000 | 2.300 | 379 |
| Wichard Bolt Swivel | 6 | 1.000 | 4.000 | 250 | 89 |
| Wichard Bolt Swivel | 8 | 1.800 | 7.200 | 430 | 119 |
| Wichard Bolt Swivel | 10 | 2.800 | 11.200 | 720 | 149 |
| Wichard Bolt Swivel | 12 | 4.000 | 16.000 | 1.050 | 189 |

**Technische Merkmale:**
- Material: HR (Haute Résistance) geschmiedeter 316L-Edelstahl
- Drehung: Kugellager bei HR-Serie, Gleitlager bei Bolt-Serie
- Oberfläche: Poliert, säurepassiviert
- Befestigung: Gabel-Gabel (HR), Bolzen-Auge (Bolt)
- Besonderheit: 25 Jahre Herstellergarantie, Made in France
- Zertifizierung: BV (Bureau Veritas) geprüft

### 2.4 Dimensionierungsregeln für Wirbel

#### 2.4.1 Grundregel

```
WLL_Wirbel ≥ WLL_Kette
Bruchlast_Wirbel ≥ Bruchlast_Kette
```

#### 2.4.2 Sicherheitsfaktoren

| Einsatzbereich | Sicherheitsfaktor | Empfehlung |
|----------------|-------------------|------------|
| Küstenfahrt | 4:1 | WLL = Bootsgewicht × 1,0 |
| Offshore | 5:1 | WLL = Bootsgewicht × 1,5 |
| Blauwasser | 6:1 | WLL = Bootsgewicht × 2,0 |
| Sturmankern | 8:1 | WLL = Bootsgewicht × 3,0 |

#### 2.4.3 Kompatibilitätsprüfung

Der Wirbel muss zur Kettengröße passen. Folgende Parameter sind zu prüfen:

- **Innendurchmesser Gabel/Auge**: Muss Kettenglied aufnehmen
- **Bolzendurchmesser**: Muss in Kettenglied passen
- **Gesamtbreite**: Muss über Bugrolle passen (inkl. seitlicher Führung)
- **Gesamtlänge**: Beeinflusst Einzugverhalten über Bugrolle
- **Gewicht**: Trägt zur Vorschiffslast bei

### 2.5 Vergleichsmatrix Ankerwirbel

| Kriterium | Mantus M1 | Kong Anchor | Ultra Swivel | Wichard HR | Wichard Bolt |
|-----------|----------|-------------|-------------|-----------|-------------|
| Material | 316L geschmiedet | 316 warmgeschmiedet | 316 Feinguss+CNC | 316L geschmiedet | 316L geschmiedet |
| Bauform | Gabel-Gabel | Gabel-Auge | Integriert | Gabel-Gabel | Bolzen-Auge |
| Kugellager | Nein | Ab 10 mm | Nein | Ja (HR-Serie) | Nein |
| Flush-fit Bugrolle | Mäßig | Mäßig | Hervorragend | Gut | Gut |
| Bruchlast (10mm) | 10.886 kg | 10.000 kg | 14.400 kg | 12.800 kg | 11.200 kg |
| Preis (10mm) | 139 € | 129 € | 189 € | 189 € | 149 € |
| Garantie | 2 Jahre | 2 Jahre | 5 Jahre | 25 Jahre | 25 Jahre |
| Herkunft | USA | Italien | Neuseeland | Frankreich | Frankreich |
| Preis/Leistung | ★★★★★ | ★★★★☆ | ★★★★☆ | ★★★☆☆ | ★★★★☆ |
| Blauwasser-Eignung | ★★★★☆ | ★★★★☆ | ★★★★★ | ★★★★★ | ★★★☆☆ |

**AYDI-Empfehlung nach Einsatzbereich:**
- **Küstenfahrt, Budget**: Mantus M1 (bestes Preis-Leistungs-Verhältnis)
- **Küstenfahrt, Standard**: Kong Anchor Swivel (gute Qualität, CE-zertifiziert)
- **Blauwasser, Standard**: Ultra Swivel (Flush-fit, hohe Bruchlast)
- **Blauwasser, Premium**: Wichard HR (Kugellager, 25 Jahre Garantie, BV-geprüft)
- **Regatta/Gewicht**: Ultra Swivel (leichteste Bauform bei hoher Bruchlast)

### 2.6 Galvanische Kompatibilität von Wirbeln

| Wirbel-Material | Kette verzinkt | Kette 316L | Kette G40 | Kette G70 |
|----------------|---------------|-----------|----------|----------|
| 316L | ⚠ Zink opfert sich | ✓ Ideal | ⚠ Potenziell | ⚠ Potenziell |
| 316 | ⚠ Zink opfert sich | ✓ Gut | ⚠ Potenziell | ⚠ Potenziell |
| Verzinkt | ✓ Kein Risiko | ✗ Stahl korrodiert | ✓ Kein Risiko | ✓ Kein Risiko |
| Titan | ✗ Alles andere korrodiert | ✓ Gut | ✗ Stahl korrodiert | ✗ Stahl korrodiert |

**Wichtig**: Bei verzinkter Kette und 316L-Wirbel opfert sich die Zinkschicht
der Kette im Bereich des Wirbels schneller auf. Dies ist akzeptabel, muss
aber beobachtet werden. Bei 316L-Kette und 316L-Wirbel besteht kein
galvanisches Risiko.

### 2.7 Einbautipps und häufige Fehler

#### 2.7.1 Korrekte Einbaurichtung

- Gabel-Seite zum Anker, Auge-Seite zur Kette (bei Gabel-Auge-Wirbeln)
- Bolzen so orientieren, dass er nicht am Grund scheuert
- Wirbel muss sich VOR dem Einbau frei drehen lassen

#### 2.7.2 Typische Einbaufehler

| Fehler | Folge | Vermeidung |
|--------|-------|-----------|
| Wirbel zu groß für Bugrolle | Klemmt beim Einzug | Rollenbreite vor Kauf messen |
| Wirbel zu klein für Kette | Kettenglied passt nicht | Gabelweite prüfen |
| Bolzen nicht gesichert | Löst sich, Wirbel öffnet sich | Sicherungsdraht montieren |
| Falsches Material | Galvanische Korrosion | 316L verwenden |
| Kein Süßwasser-Spülung | Salzverkrustung, Blockierung | Nach jedem Einsatz spülen |
| Wirbel direkt am Ankerauge ohne Schäkel | Verschleiß an beiden Teilen | Immer Schäkel dazwischen |

### 2.8 Wartung und Inspektion

#### 2.5.1 Wartungsintervalle

| Maßnahme | Intervall | Beschreibung |
|----------|-----------|-------------|
| Sichtkontrolle | Vor jeder Ankermanöver | Bolzensitz, Drehgängigkeit, sichtbare Korrosion |
| Drehtest | Monatlich | Wirbel muss sich leicht drehen lassen |
| Reinigung | Nach jedem Salzwasser-Einsatz | Süßwasser-Spülung, trocknen |
| Bolzenkontrolle | Saisonweise | Bolzenspiel prüfen, Sicherungsdraht kontrollieren |
| Verschleißmessung | Jährlich | Bolzendurchmesser messen (max. 10% Verschleiß) |
| Kugellager-Wartung | Alle 2 Jahre | Reinigung, Fettung (bei Kugellager-Wirbeln) |
| Austausch | Bei Verschleiß >10% | Gesamten Wirbel ersetzen |

#### 2.5.2 Lebensdauer-Erwartung

| Material/Qualität | Erwartete Lebensdauer | Bemerkung |
|--------------------|-----------------------|-----------|
| 316L geschmiedet, Premium | 15–20 Jahre | Bei korrekter Wartung |
| 316 Feinguss, Standard | 8–12 Jahre | Spaltkorrosion beachten |
| 304 Edelstahl | 3–5 Jahre | Nicht empfohlen für Salzwasser |
| Verzinkter Stahl | 2–4 Jahre | Nur Notlösung |

---

## 3. Ankerschäkel (Bow Shackles)

### 3.1 Funktion und Bedeutung

Ankerschäkel (engl. bow shackles, anchor shackles) dienen als Verbindungselemente
zwischen den verschiedenen Komponenten des Ankergeschirrs. Sie verbinden:
- Anker mit Wirbel
- Wirbel mit Kette
- Kette mit Kettenvorläufer
- Kettenvorläufer mit Leine

### 3.2 Bauformen

#### 3.2.1 Bügelschäkel (Bow Shackle / Omega Shackle)

- **Form**: Omega-förmig (bauchig), auch „Harfenschäkel" genannt
- **Vorteil**: Breiterer Bügel erlaubt mehr Bewegungsfreiheit des eingehängten Gliedes
- **Einsatz**: Standard für Ankerverbindungen
- **WLL**: Höher als D-Schäkel gleicher Bolzengröße

#### 3.2.2 D-Schäkel (Dee Shackle)

- **Form**: D-förmig (schmaler)
- **Vorteil**: Kompakter, gerichtete Belastung
- **Einsatz**: Weniger geeignet für Ankerverbindungen (eingeschränkte Bewegung)
- **WLL**: Geringer als Bügelschäkel gleicher Bolzengröße

#### 3.2.3 Langglied-Schäkel (Long Shackle)

- **Form**: Gestreckter Bügelschäkel
- **Vorteil**: Passt durch Kettennuss der Ankerwinch
- **Einsatz**: Verbindung Kette-Kette, wenn durch Winde laufen muss

#### 3.2.4 Schnellschäkel (Snap Shackle)

- **Form**: Mit Federverschluss
- **Vorteil**: Schnelle Montage/Demontage
- **Nachteil**: Geringere Bruchlast, Versagensrisiko durch Federmechanismus
- **Einsatz**: NICHT für Ankerverbindungen empfohlen (nur für Tripleine)

### 3.3 Dimensionierung von Ankerschäkeln

#### 3.3.1 Größentabelle nach Kettendurchmesser

| Kette (mm) | Schäkelgröße | Bolzen (mm) | Innenweite (mm) | WLL 316L (kg) | Bruchlast (kg) |
|-----------|-------------|------------|-----------------|---------------|----------------|
| 6 | 6 mm | 8 | 12 | 500 | 2.000 |
| 8 | 8 mm | 10 | 16 | 750 | 3.000 |
| 8 | 10 mm | 12 | 20 | 1.000 | 4.000 |
| 10 | 10 mm | 12 | 20 | 1.000 | 4.000 |
| 10 | 12 mm | 14 | 24 | 1.500 | 6.000 |
| 12 | 12 mm | 14 | 24 | 1.500 | 6.000 |
| 12 | 14 mm | 16 | 28 | 2.000 | 8.000 |
| 13 | 14 mm | 16 | 28 | 2.000 | 8.000 |
| 13 | 16 mm | 19 | 32 | 2.500 | 10.000 |
| 16 | 16 mm | 19 | 32 | 2.500 | 10.000 |
| 16 | 19 mm | 22 | 38 | 3.350 | 13.400 |

#### 3.3.2 Auswahlregel

```
Schäkelgröße ≥ Kettendurchmesser + 2 mm (Minimum)
Schäkelgröße ≥ Kettendurchmesser + 4 mm (Empfohlen)

Innenweite ≥ 2 × Kettendurchmesser (für Bügelschäkel)
```

#### 3.3.3 Materialanforderungen

| Material | Kennzeichnung | Salzwasser-Eignung | Empfehlung |
|----------|--------------|-------------------|------------|
| AISI 316L | Gravur „316L" oder „A4" | Hervorragend | Standard für Yachten |
| AISI 316 | Gravur „316" oder „A4" | Sehr gut | Akzeptabel |
| AISI 304 | Gravur „304" oder „A2" | Mäßig | Nicht empfohlen |
| Verzinkter Stahl | Keine Gravur / „Galv" | Befristet | Nur Notlösung |
| Titan Gr. 5 | „Ti" oder „Gr5" | Hervorragend | Premium-Segment |

### 3.4 Hersteller und Preise

| Hersteller | Modell | Material | 8mm | 10mm | 12mm | 14mm |
|-----------|--------|----------|-----|------|------|------|
| Wichard | HR Bow Shackle | 316L geschmiedet | 29 € | 39 € | 49 € | 69 € |
| Wichard | Self-Locking | 316L geschmiedet | 39 € | 49 € | 65 € | 89 € |
| Kong | Anchor Shackle | 316 warmgeschmiedet | 22 € | 29 € | 39 € | 55 € |
| Seldén | Bow Shackle | 316L | 19 € | 25 € | 35 € | 49 € |
| Plastimo | Standard | 316 Feinguss | 12 € | 16 € | 22 € | 32 € |
| Blue Wave | Precision | 316L geschmiedet | 25 € | 32 € | 42 € | 59 € |
| Lalizas | Budget | 316 Feinguss | 8 € | 11 € | 15 € | 22 € |

### 3.5 Schäkelbolzen-Sicherung

#### 3.5.1 Methoden

1. **Sicherungsdraht (Seizing Wire)**
   - 316L-Draht 0,8–1,2 mm durch Bolzenloch führen
   - 3–4 Windungen, Enden verdrillen und umbiegen
   - Einfachste und zuverlässigste Methode
   - Austausch bei jeder Demontage

2. **Splint (Cotter Pin)**
   - Nur bei Schäkeln mit Splintloch im Bolzen
   - Sicherer als Draht, aber umständlicher
   - 316L-Splinte verwenden

3. **Schraubensicherungslack (Thread Locker)**
   - Loctite 243 (mittelfest) auf Gewinde
   - Zusätzlich zu Draht, nicht als alleinige Sicherung
   - Nicht bei regelmäßiger Demontage

4. **Selbstsichernde Bolzen (Self-Locking)**
   - Wichard Self-Locking-System
   - Keine zusätzliche Sicherung nötig
   - Höherer Preis, aber zuverlässig

#### 3.5.2 Häufige Fehler

- Bolzen ohne jede Sicherung eingeschraubt → Löst sich nach wenigen Ankermanövern
- Kabelbinder statt Sicherungsdraht → UV-Zerfall, nicht seewasserfest
- Falsches Material (Kupferdraht in Edelstahlschäkel) → Galvanische Korrosion
- Zu wenig Drahtwindungen → Draht bricht unter Vibration

### 3.6 Inspektion und Prüfung von Schäkeln

#### 3.6.1 Visuelle Inspektion

| Prüfpunkt | Methode | Akzeptabel | Nicht akzeptabel |
|-----------|---------|-----------|-----------------|
| Bügel-Form | Sichtprüfung | Gleichmäßig gerundet | Verformt, ovalisiert |
| Bolzengewinde | Finger-Test | Sauber einschraubbar | Schwergängig, beschädigt |
| Gravur | Lupe | Lesbar (316L, A4) | Unleserlich, keine Gravur |
| Oberfläche | Sichtprüfung | Glatt, metallisch | Lochfraß, Risse, Rost |
| Bolzenloch | Stift-Test | Sicherungsdraht passt | Ausgefranst, zu groß |
| Bolzensitz | Spiel-Test | Kein spürbares Spiel | Bolzen wackelt |

#### 3.6.2 Maß-Prüfung

| Messung | Werkzeug | Grenzwert für Austausch |
|---------|----------|----------------------|
| Bolzendurchmesser | Messschieber | < 90% Nennmaß |
| Bügelöffnung (Innenweite) | Messschieber | > 110% Nennmaß (aufgebogen) |
| Bügeldurchmesser | Messschieber | < 90% Nennmaß (Materialabtrag) |
| Gesamtlänge | Messschieber | > 105% Nennmaß (gelängt) |

#### 3.6.3 Austauschintervalle

| Einsatz | Empfohlener Austausch | Begründung |
|---------|----------------------|-----------|
| Küstenfahrt, Gelegenheit | Alle 5–8 Jahre | Geringe Beanspruchung |
| Regelmäßige Fahrt | Alle 3–5 Jahre | Normaler Verschleiß |
| Blauwasser, Dauersegler | Alle 2–3 Jahre | Hohe Beanspruchung, Sicherheit |
| Charterboot | Jährlich | Unbekannte Vorbelastung |

---

## 4. Kettenvorläufer

### 4.1 Funktion und Zweck

Der Kettenvorläufer (engl. chain leader, chain-rode connection, chain-to-rope
splice) bezeichnet das Verbindungsstück zwischen Ankerkette und Ankerleine bei
gemischten Ankergeschirren (Kette + Leine). Er kann auch als kurzes Kettenstück
am Anfang eines reinen Leinengeschirrs eingesetzt werden.

### 4.2 Aufbau eines gemischten Ankergeschirrs

```
Anker → Wirbel → Kette (10–30 m) → Kettenvorläufer-Verbindung → Leine (30–80 m)
```

### 4.3 Verbindungsmethoden

#### 4.3.1 Kettenschäkel-Spleiss-Verbindung

- Leine wird direkt in das letzte Kettenglied gespleißt
- **Vorteil**: Keine zusätzlichen Beschläge, kompakt, läuft durch Bugrolle
- **Nachteil**: Spleiss muss fachmännisch ausgeführt werden
- **Festigkeit**: 80–90% der Leinenbruchlast (bei korrektem Spleiss)
- **Material Leine**: 3-schäftiges Nylon oder Polyester-Kern mit Nylon-Mantel

#### 4.3.2 Ketten-Leine-Schäkel

- Schäkel verbindet letztes Kettenglied mit gespleißtem Auge der Leine
- **Vorteil**: Einfach demontierbar
- **Nachteil**: Schäkel als potentielle Schwachstelle, läuft schlechter über Rolle
- **Festigkeit**: Begrenzt durch Schäkel-WLL

#### 4.3.3 Kettenverbinder (Chain-Rope Connector)

- Spezielle Beschläge wie Mantus Chain Hook oder Kong Chain Connector
- **Vorteil**: Schnelle Montage, hohe WLL
- **Nachteil**: Teurer als einfacher Schäkel
- **Festigkeit**: Herstellerangaben beachten

### 4.4 Dimensionierung

#### 4.4.1 Kettenlänge im gemischten Geschirr

| Bootsklasse | Empfohlene Kettenlänge | Leinenlänge | Gesamtlänge |
|-------------|----------------------|-------------|-------------|
| Kleinkreuzer 6–8 m | 10–15 m × 6 mm | 30–50 m | 40–65 m |
| Fahrtenyacht 8–12 m | 15–25 m × 8 mm | 40–60 m | 55–85 m |
| Blauwasser 10–15 m | 20–40 m × 10 mm | 50–80 m | 70–120 m |
| Performance 12–18 m | 30–50 m × 10 mm | 50–80 m | 80–130 m |

#### 4.4.2 Leinen-Dimensionierung

| Kette (mm) | Leinendurchmesser (mm) | Material | Bruchlast (kg) |
|-----------|----------------------|----------|----------------|
| 6 | 12–14 | Nylon 3-schäftig | 2.400–3.200 |
| 8 | 14–16 | Nylon 3-schäftig | 3.200–4.400 |
| 10 | 16–18 | Nylon 3-schäftig | 4.400–5.800 |
| 12 | 18–20 | Nylon 3-schäftig | 5.800–7.200 |
| 13 | 20–22 | Nylon 3-schäftig | 7.200–9.000 |

### 4.5 Preise für Kettenvorläufer-Komponenten

| Komponente | Hersteller | Größe | Preis (EUR) |
|-----------|-----------|-------|-------------|
| Mantus Chain Hook | Mantus Marine | 6–8 mm | 59 |
| Mantus Chain Hook | Mantus Marine | 10–12 mm | 79 |
| Mantus Chain Hook | Mantus Marine | 13–16 mm | 99 |
| Kong Chain Connector | Kong | 8–10 mm | 45 |
| Kong Chain Connector | Kong | 12–14 mm | 65 |
| Nylon 3-schäftig (per m) | Liros | 14 mm | 3,20 |
| Nylon 3-schäftig (per m) | Liros | 16 mm | 4,50 |
| Nylon 3-schäftig (per m) | Liros | 18 mm | 5,80 |
| Nylon 3-schäftig (per m) | Liros | 20 mm | 7,50 |
| Nylon 3-schäftig (per m) | Gleistein | 14 mm | 3,80 |
| Nylon 3-schäftig (per m) | Gleistein | 16 mm | 5,20 |
| Nylon 3-schäftig (per m) | Gleistein | 18 mm | 6,50 |

### 4.6 Pflege des Kette-Leine-Übergangs

| Maßnahme | Intervall | Beschreibung |
|----------|-----------|-------------|
| Spleiss-Kontrolle | Vor jeder Saison | Spleiss auf Aufgehen, Scheuerstellen prüfen |
| Schäkel-Kontrolle | Monatlich | Bolzensitz, Sicherungsdraht am Übergangsschäkel |
| Leine waschen | Nach Salzwasser | Nylon-Leine in Süßwasser spülen, trocknen |
| UV-Schutz | Dauerhaft | Leine bei Nichtgebrauch abdecken (UV-Zerfall) |
| Austausch Spleiss | Alle 3–5 Jahre | Spleiss verliert mit der Zeit Festigkeit |
| Leine erneuern | Alle 5–8 Jahre | Nylon-Alterung (Festigkeitsverlust 10–15% nach 5 Jahren) |

### 4.7 Vergleich: Nur Kette vs. gemischtes Geschirr

| Kriterium | Nur Kette | Kette + Leine |
|-----------|----------|---------------|
| Gewicht Vorschiff | Hoch (50–120 kg) | Geringer (30–60 kg) |
| Ankerhaltekraft | Höher (Kettenbogen) | Geringer (weniger Gewicht am Grund) |
| Ruckdämpfung | Keine (starr) | Gut (Nylon-Dehnung) |
| UV-Beständigkeit | Hervorragend | Leine UV-empfindlich |
| Scheuerbeständigkeit | Hervorragend | Leine scheuergefährdet |
| Preis | Höher (Kette teuer) | Geringer (Leine günstig) |
| Stauraum | Viel (schwere Kette) | Weniger (Leine komprimierbar) |
| Tiefwasser-Eignung | Schwer (Gewicht) | Besser (leichter zu handhaben) |
| Korallen-/Fels-Eignung | Gut (Kette widerstandsfähig) | Schlecht (Leine schneidet sich durch) |
| Windenkompatibilität | Direkt über Kettennuss | Leine über Spillkopf |

**AYDI-Empfehlung:**
- **Küstenfahrt, flache Gewässer**: Nur Kette (30–50 m)
- **Blauwasser, moderate Tiefen**: Kette (30–50 m) + Leine (50–80 m)
- **Tiefwasser-Ankern**: Kette (15–20 m) + Leine (80–120 m)
- **Performance/Regatta**: Minimale Kette (5–10 m) + Leine

---

## 5. Ankerbojen und Ankerbälle

### 5.1 Funktion

Ankerbojen und Ankerbälle erfüllen zwei wesentliche Funktionen:

1. **Markierung der Ankerposition**: Die Ankerboje zeigt anderen Booten an,
   wo der Anker liegt, und verhindert so, dass Nachbarlieger über die eigene
   Kette fahren oder ihren Anker in die eigene Kette schlagen.

2. **Bergungshilfe**: Bei verklemmtem Anker ermöglicht die Tripleine (an der
   Ankerboje befestigt) das Freiziehen des Ankers von der Gegenrichtung.

### 5.2 Typen

#### 5.2.1 Aufblasbare Ankerbojen

- **Beschreibung**: PVC- oder Hypalon-Schwimmkörper, aufblasbar
- **Volumen**: 10–50 Liter
- **Vorteile**: Platzsparende Lagerung, günstig
- **Nachteile**: Pannengefahr (scharfe Muscheln, UV), Ventilversagen
- **Hersteller**: Plastimo (ab 12 €), Osculati (ab 9 €), Lalizas (ab 8 €)

#### 5.2.2 Feste Schwimmkörper (Hartschaum)

- **Beschreibung**: Geschlossenporiger Schaum, unlöschbar
- **Volumen**: 5–30 Liter
- **Vorteile**: Unzerstörbar, kein Aufblasen nötig
- **Nachteile**: Sperriger bei Lagerung
- **Hersteller**: Polyform (ab 22 €), Dan-Fender (ab 18 €)

#### 5.2.3 Ankerbälle (Day Shapes)

- **Beschreibung**: Schwarze Kugel (∅ ≥ 300 mm) als Tagessignal für Ankerlieger
- **Pflicht**: Gemäß KVR (Kollisionsverhütungsregeln) Regel 30
- **Material**: Kunststoff (faltbar oder starr)
- **Hersteller**: Plastimo (faltbar, ab 8 €), Lalizas (starr, ab 15 €)

### 5.3 Rechtliche Anforderungen

| Regelwerk | Anforderung | Geltungsbereich |
|-----------|------------|----------------|
| KVR Regel 30 | Ankerball ∅ ≥ 300 mm bei Tag | International |
| KVR Regel 30 | Ankerlicht (weiß, Rundumlicht) bei Nacht | International |
| SeeSchStrO § 3 | Ankerball bei Tag | Deutsche Seeschifffahrtsstraßen |
| BinSchStrO | Ankerball bei Tag auf Binnenwasserstraßen | Deutsche Binnenwasserstraßen |
| ColRegs | Black ball shape forward | International |

### 5.4 Preisübersicht Ankerbojen

| Hersteller | Modell | Typ | Volumen (l) | Preis (EUR) |
|-----------|--------|-----|-------------|-------------|
| Plastimo | Anchor Buoy | Aufblasbar | 15 | 12 |
| Plastimo | Anchor Buoy Deluxe | Aufblasbar | 30 | 22 |
| Plastimo | Rigid Buoy | Hart | 10 | 28 |
| Polyform | A-0 | Hart | 7,5 | 22 |
| Polyform | A-1 | Hart | 13 | 32 |
| Polyform | A-2 | Hart | 19 | 42 |
| Polyform | A-3 | Hart | 28 | 55 |
| Osculati | Anchor Buoy | Aufblasbar | 20 | 14 |
| Dan-Fender | Anchor Marker | Hart | 12 | 25 |
| Lalizas | Anchor Ball | Aufblasbar | 15 | 9 |

---

## 6. Triplinen

### 6.1 Funktion und Zweck

Die Tripleine (engl. trip line) ist eine Hilfsleine, die am Ankerkopf
(an der Flunkenkrone oder am Trip-Ring) befestigt ist und zur Wasseroberfläche
(an eine Ankerboje) oder zurück an Bord geführt wird. Sie dient zum:

1. **Freitrippen eines verklemmten Ankers**: Zug an der Tripleine dreht den
   Anker um und löst ihn aus dem Grund
2. **Markierung der Ankerposition**: Mit Ankerboje an der Oberfläche
3. **Kontrolle der Ankerlage**: Tripleine zeigt, wo genau der Anker liegt

### 6.2 Systeme

#### 6.2.1 Boje-System (Surface Trip Line)

```
Anker (Trip-Ring) → Tripleine → Ankerboje (an der Oberfläche)
```

- **Vorteil**: Markierung + Bergungshilfe
- **Nachteil**: Boje kann sich in Nachbarlieger-Geschirr verfangen
- **Leinenlänge**: Wassertiefe × 1,2 + Reserve

#### 6.2.2 Deck-System (On-Deck Trip Line)

```
Anker (Trip-Ring) → Tripleine → Klampe/Kette an Deck
```

- **Vorteil**: Keine Boje im Wasser, keine Verwechslung
- **Nachteil**: Keine Markierung für andere, Tripleine kann sich um Kette wickeln
- **Leinenlänge**: Gleich der Ankerkettenlänge + Reserve

#### 6.2.3 Reitgewicht-System (Kellet Trip)

- Tripleine am Anker, Reitgewicht auf Hauptkette
- Doppelfunktion: Reitgewicht flacht Kettenbogen ab, Tripleine als Bergungshilfe

### 6.3 Dimensionierung

| Bootsklasse | Tripleine Ø (mm) | Material | Bruchlast (kg) | Preis/m (EUR) |
|-------------|-----------------|----------|----------------|---------------|
| Kleinkreuzer | 6–8 | Polypropylen (schwimmfähig) | 500–900 | 0,60–1,00 |
| Fahrtenyacht | 8–10 | Polypropylen (schwimmfähig) | 900–1.500 | 1,00–1,50 |
| Blauwasser | 10–12 | Polypropylen (schwimmfähig) | 1.500–2.200 | 1,50–2,20 |
| Performance | 10–14 | Dyneema/Polyester | 2.200–4.000 | 2,50–5,00 |

**Wichtig**: Schwimmfähige Leine (Polypropylen) verwenden, damit die Tripleine
nicht auf dem Grund liegt und sich nicht in Steinen/Korallen verhakt.

### 6.4 Befestigung am Anker

| Ankertyp | Trip-Ring vorhanden? | Befestigungsmethode |
|----------|---------------------|---------------------|
| Bügelanker (Rocna, Mantus) | Ja (Slot am Schaft) | Durch Slot fädeln, Palstek |
| Pflugscharanker (Delta, CQR) | Meist nein | Am Schaftkopf befestigen |
| Plattenanker (Spade, Sword) | Ja (am Flunkenrücken) | Am Ring befestigen |
| Danforth/Fortress | Ja (Flunkenkrone) | Am Trip-Ring, Palstek |
| Bruce/Claw | Nein | Am Schaftkopf befestigen |

### 6.5 Vor- und Nachteile der Triplein-Systeme

| System | Vorteil | Nachteil | Empfehlung |
|--------|---------|----------|-----------|
| Boje-System | Markierung + Bergung | Boje kann sich verfangen | Standard für unbekannte Gründe |
| Deck-System | Keine Boje im Wasser | Keine Markierung, wickelt sich | Erfahrene Segler, bekannte Gründe |
| Reitgewicht-System | Doppelfunktion | Komplex im Handling | Blauwasser, enge Buchten |

### 6.6 Tripleine richtig ausbringen

**Schritt-für-Schritt-Anleitung (Boje-System):**

1. **Vorbereitung**: Tripleine am Anker-Trip-Ring befestigen (Palstek)
2. **Länge berechnen**: Wassertiefe × 1,2 + 2 m Reserve (bei Hochwasser)
3. **Boje befestigen**: Am Ende der Tripleine, Boje aufblasen oder festen Schwimmer verwenden
4. **Anker ausbringen**: Normal ankern, Tripleine mit auslegen
5. **Kontrolle**: Boje muss frei schwimmen, Tripleine darf nicht um Kette gewickelt sein
6. **Markierung**: Bei Nacht Reflektorband an der Boje anbringen

**Häufige Fehler:**
- Tripleine zu kurz → Boje wird bei Hochwasser untergezogen
- Tripleine zu lang → Boje treibt weit ab, verfängt sich in Nachbarbooten
- PP-Leine nicht schwimmfähig gewählt → Leine liegt auf dem Grund, verfängt sich
- Trip-Ring am falschen Ende des Ankers → Tripleine hilft nicht beim Freitrippen

---

## 7. Ankerrollen (Bow Rollers)

### 7.1 Funktion und Bedeutung

Die Ankerrolle (engl. bow roller, anchor roller) ist ein am Bug montierter
Beschlag, der folgende Funktionen erfüllt:

1. **Führung der Ankerkette/Leine** beim Ein- und Ausfahren
2. **Lagerung des Ankers** in Seefahrtposition (auf der Rolle festgezurrt)
3. **Reibungsreduktion** beim Ankermanöver
4. **Lastverteilung** auf die Bugstruktur
5. **Schutz des Bugs** vor Scheuerschäden durch Kette und Anker

### 7.2 Bauformen

#### 7.2.1 Einfache Bugrolle (Simple Bow Roller)

- **Beschreibung**: Einzelne Rolle auf Wangen montiert
- **Einsatz**: Kleinere Boote, Segelboote bis 10 m
- **Vorteil**: Kompakt, günstig
- **Nachteil**: Nur eine Kettengröße, kein Ankerlager

#### 7.2.2 Doppel-Bugrolle (Twin Bow Roller)

- **Beschreibung**: Zwei parallele Rollen für zwei Ankerketten
- **Einsatz**: Katamarane, Boote mit Zweitanker am Bug
- **Vorteil**: Zwei Anker gleichzeitig fahrbereit
- **Nachteil**: Breiterer Bugbeschlag nötig

#### 7.2.3 Selbstausrichtende Bugrolle (Self-Aligning)

- **Beschreibung**: Rolle schwenkt horizontal, richtet sich nach Kettenrichtung aus
- **Einsatz**: Boote, die häufig Ankerplatz wechseln
- **Vorteil**: Kein Verkanten der Kette bei seitlichem Zug
- **Nachteil**: Komplexer, teurer

#### 7.2.4 Anker-Wiege (Anchor Cradle)

- **Beschreibung**: Geformte Aufnahme, in die der Anker exakt einrastet
- **Einsatz**: Festmontierter Hauptanker auf dem Bug
- **Vorteil**: Sicherer Ankersitz, saubere Optik
- **Nachteil**: Nur für einen bestimmten Ankertyp passend

#### 7.2.5 Eingebaute Bugrolle (Recessed / Flush-Mount)

- **Beschreibung**: In den Bug eingelassene Rolle, bündig mit Decksoberfläche
- **Einsatz**: Performance-Yachten, Superyachten
- **Vorteil**: Saubere Optik, kein Überstehen am Bug
- **Nachteil**: Aufwändiger Einbau, strukturelle Verstärkung nötig

### 7.3 Hersteller-Datenbank

#### 7.3.1 Lewmar Bow Rollers

Lewmar (UK) ist einer der größten Hersteller von Ankerbeschlägen weltweit.

| Modell | Typ | Für Kette | Material | Rollenlänge (mm) | Max. Ankergewicht (kg) | Preis (EUR) |
|--------|-----|----------|----------|-----------------|----------------------|-------------|
| Lewmar Concept 1 | Einfach | 6–8 mm | 316L + Nylon-Rolle | 200 | 15 | 149 |
| Lewmar Concept 2 | Einfach | 8–10 mm | 316L + Nylon-Rolle | 280 | 25 | 219 |
| Lewmar Concept 3 | Einfach | 10–12 mm | 316L + Nylon-Rolle | 350 | 35 | 289 |
| Lewmar Concept 4 | Einfach | 12–14 mm | 316L + Nylon-Rolle | 420 | 50 | 389 |
| Lewmar V-Bow Roller | V-Form | 8–12 mm | 316L | 300 | 30 | 259 |
| Lewmar Claw Anchor Roller | Wiege | 10–13 mm | 316L + HDPE | 380 | 45 | 449 |
| Lewmar Pro-Fish | Doppel | 8–10 mm | 316L | 320×2 | 25 | 379 |
| Lewmar Horizon | Flush | 10–14 mm | 316L | 450 | 60 | 849 |

**Technische Merkmale (Lewmar):**
- Material Wangen: 316L Edelstahl, 4–6 mm Materialstärke
- Rollen: Glasfaserverstärktes Nylon oder HDPE
- Achsen: 316L Edelstahl, Ø 12–20 mm je nach Modell
- Befestigung: 4–8 × M8–M12 Bolzen mit Unterdeck-Gegenplatten
- Oberflächenbehandlung: Poliert und passiviert

#### 7.3.2 Maxwell Bow Rollers

Maxwell Marine (Neuseeland) ist spezialisiert auf Ankerwinden und -beschläge.

| Modell | Typ | Für Kette | Material | Max. Ankergewicht (kg) | Preis (EUR) |
|--------|-----|----------|----------|----------------------|-------------|
| Maxwell P104153 | Einfach | 6–8 mm | 316L | 15 | 129 |
| Maxwell P104154 | Einfach | 8–10 mm | 316L | 25 | 189 |
| Maxwell P104155 | Einfach | 10–13 mm | 316L | 40 | 269 |
| Maxwell P104156 | Einfach | 13–16 mm | 316L | 60 | 369 |
| Maxwell Deluxe Roller | Wiege | 8–10 mm | 316L + Teak | 30 | 349 |
| Maxwell Deluxe Roller | Wiege | 10–13 mm | 316L + Teak | 50 | 469 |
| Maxwell Twin Roller | Doppel | 8–10 mm | 316L | 25 | 399 |
| Maxwell Twin Roller | Doppel | 10–13 mm | 316L | 40 | 529 |

**Technische Merkmale (Maxwell):**
- Material: 316L Edelstahl, Investment-Cast oder CNC-gefräst
- Deluxe-Reihe: Teak-Einlagen als Ankerschutz
- Achsen: Durchgehende 316L-Achse mit Sicherungsmutter
- Passend zu Maxwell-Winden (abgestimmte Geometrie)

#### 7.3.3 Custom-Bugrollen

Für Superyachten und individuelle Anforderungen werden Bugrollen
maßgefertigt:

| Anbieter | Material | Lieferzeit | Preisbereich (EUR) |
|----------|----------|------------|-------------------|
| Batsystem (SE) | 316L CNC | 4–6 Wochen | 500–2.000 |
| Antal (IT) | 316L + Bronze | 6–8 Wochen | 800–3.000 |
| Amar (IT) | 316L geschmiedet | 8–12 Wochen | 1.200–5.000 |
| Custom-Schmiede (DE) | 316L / Duplex | 6–10 Wochen | 1.500–8.000 |

### 7.4 Dimensionierung

#### 7.4.1 Rollenbreite

Die Rollennut muss zur Kettengröße passen:

| Kette (mm) | Rollennut-Breite (mm) | Rollendurchmesser min. (mm) |
|-----------|---------------------|-----------------------------|
| 6 | 8–10 | 40 |
| 8 | 10–13 | 50 |
| 10 | 13–16 | 60 |
| 12 | 16–19 | 70 |
| 13 | 17–20 | 75 |
| 14 | 19–22 | 80 |
| 16 | 22–25 | 90 |

#### 7.4.2 Wangenhöhe

Die Wangen (seitliche Führungen) müssen hoch genug sein, um den Ankerschaft
sicher zu halten:

```
Wangenhöhe ≥ Ankerschaft-Durchmesser + 10 mm
Wangenhöhe ≥ Kettendurchmesser × 3
```

#### 7.4.3 Befestigung und strukturelle Anforderungen

| Parameter | Anforderung | Berechnung |
|-----------|------------|------------|
| Bolzengröße | M8 min. (bis 12m Boot) | M10 ab 12m, M12 ab 18m |
| Bolzenanzahl | 4 min., 6 empfohlen | 8 ab 18m |
| Gegenplatte | Edelstahl 3–6 mm | Unterdeck, Lastverteilung |
| Decksverstärkung | GFK-Auflamierung oder Holzkern | Mindestens 200×200 mm |
| Max. Belastung | 3× Ankergewicht dynamisch | Sicherheitsfaktor 3 |

### 7.5 Material-Anforderungen

| Komponente | Material | Anforderung |
|-----------|----------|------------|
| Wangen | 316L Edelstahl | Min. 4 mm, poliert |
| Rolle | Nylon/HDPE/Bronze | UV-beständig, Salzwasser-resistent |
| Achse | 316L Edelstahl | Min. Ø 12 mm, passgenaue Bohrung |
| Bolzen | 316L Edelstahl | Mit Nyloc-Mutter oder Sicherungsblech |
| Sicherungsstift | 316L Edelstahl | Federstecker oder R-Clip |

### 7.6 Installation

#### 7.6.1 Einbauschritte

1. **Positionierung**: Bugrolle mittig auf Bugspitze ausrichten
2. **Anzeichnen**: Bohrlöcher durch Bugrolle auf Deck übertragen
3. **Decksverstärkung**: Unterdeck-Gegenplatte anfertigen
4. **Bohren**: Löcher bohren (Durchmesser = Bolzen + 1 mm)
5. **Abdichten**: Sikaflex 291i oder 3M 5200 auf Auflagefläche
6. **Montage**: Bolzen von oben, Gegenplatte von unten
7. **Anzug**: Vorgeschriebenes Drehmoment (M8: 18–22 Nm, M10: 35–42 Nm)
8. **Dichtigkeitsprüfung**: Wasser auf Beschlag, unten auf Durchfeuchtung prüfen

#### 7.6.2 Typische Fehler bei der Installation

- Keine Gegenplatte → Deck bricht unter Last aus
- Falsches Dichtmittel (Silikon statt PU) → Deck-Undichtigkeit
- Bugrolle nicht mittig → Kette scheuert einseitig
- Rolle zu klein für Ankertyp → Anker hängt unsicher
- Zu wenig Bolzen → Einzelbolzen-Überlastung

---

## 8. Bugbeschläge und Klüsen

### 8.1 Begriffsklärung

- **Klüse** (engl. fairlead, chock): Führungsöffnung in der Bordwand oder am Bug
  für Leinen und Ketten
- **Bugbeschlag**: Oberbegriff für alle Beschläge im Bugbereich (Klampen, Klüsen,
  Rollen, Poller)
- **Ankerklüse**: Speziell für die Ankerkette dimensionierte Durchführung

### 8.2 Klüsentypen

#### 8.2.1 Offene Klüse (Open Fairlead)

- Halboffene U-Form, Leine wird von oben eingelegt
- Vorteil: Schnelle Bedienung
- Nachteil: Leine kann herausspringen bei Lose
- Preis: 25–80 EUR (316L)

#### 8.2.2 Geschlossene Klüse (Closed Fairlead / Pipe Hawse)

- Geschlossene Rohrform, Leine/Kette muss eingefädelt werden
- Vorteil: Sicherer Halt, Leine kann nicht herausspringen
- Nachteil: Umständliches Einlegen
- Preis: 35–120 EUR (316L)

#### 8.2.3 Ankerklüse (Anchor Hawse Pipe)

- Große Durchführung für Ankerkette, oft mit Deckel
- Vorteil: Kette läuft in den Kettenkasten, sauberes Deck
- Nachteil: Wasser dringt ein (Deckel nötig)
- Preis: 45–180 EUR (316L mit Deckel)

#### 8.2.4 Fluchtklüse (Flush Fairlead)

- Bündig ins Deck eingelassen
- Vorteil: Kein Stolpern, saubere Optik
- Nachteil: Höhere Reibung, Einbauhöhe nötig
- Preis: 60–200 EUR (316L)

### 8.3 Hersteller und Preise

| Hersteller | Typ | Material | Größe | Preis (EUR) |
|-----------|-----|----------|-------|-------------|
| Lewmar | Open Fairlead 5" | 316L | 127 mm | 42 |
| Lewmar | Open Fairlead 7" | 316L | 178 mm | 58 |
| Lewmar | Closed Fairlead | 316L | 150 mm | 75 |
| Osculati | Ankerklüse Ø80 | 316L + Deckel | 80 mm | 48 |
| Osculati | Ankerklüse Ø100 | 316L + Deckel | 100 mm | 62 |
| Osculati | Ankerklüse Ø120 | 316L + Deckel | 120 mm | 78 |
| Wichard | Flush Fairlead | 316L geschmiedet | 100 mm | 89 |
| Wichard | Flush Fairlead | 316L geschmiedet | 130 mm | 119 |
| Plastimo | Open Fairlead | 316L | 120 mm | 32 |
| Plastimo | Open Fairlead | 316L | 160 mm | 45 |
| Viadana | Flush Fairlead | 316L | 100 mm | 72 |
| Viadana | Flush Fairlead | 316L | 140 mm | 98 |

### 8.4 Dimensionierung

#### 8.4.1 Klüsengröße

```
Klüsen-Innendurchmesser ≥ 3 × Kettendurchmesser + 10 mm
Klüsen-Innendurchmesser ≥ 2 × Leinendurchmesser + 5 mm
```

#### 8.4.2 Material und Wandstärke

| Bootsklasse | Wandstärke Klüse (mm) | Material | Befestigung |
|-------------|----------------------|----------|-------------|
| Kleinkreuzer 6–8 m | 3–4 | 316L | 4× M6 |
| Fahrtenyacht 8–12 m | 4–5 | 316L | 4× M8 |
| Blauwasser 10–15 m | 5–6 | 316L | 6× M8 |
| Performance 12–18 m | 6–8 | 316L / Duplex | 6× M10 |
| Superyacht 20 m+ | 8–12 | Duplex 2205 | 8× M10 |

### 8.5 Scheuerschutz

Leinen müssen in Klüsen vor Durchscheuern geschützt werden:

| Methode | Material | Lebensdauer | Preis (EUR) |
|---------|----------|-------------|-------------|
| Scheuerschutz-Schlauch | PVC/Nylon | 1–3 Saisons | 5–15 |
| Lederwicklung | Rindsleder, genäht | 2–5 Saisons | 15–40 |
| Dyneema-Chafe-Guard | UHMWPE-Geflecht | 3–8 Saisons | 25–60 |
| Teflon-Buchse in Klüse | PTFE | 5–10 Jahre | 30–80 |
| Keramik-Einlage | Al₂O₃ Keramik | 10–20 Jahre | 80–200 |

### 8.6 Bugklampen

Bugklampen sind die Festmachepunkte für Ankerleinen und Reiterleinen am Bug.
Sie müssen für die Ankerlast dimensioniert sein.

#### 8.6.1 Dimensionierung

| Bootsklasse | Klampenlänge (mm) | Bolzengröße | WLL (kg) |
|-------------|------------------|-------------|----------|
| 6–8 m | 150–200 | M8 | 1.000 |
| 8–12 m | 200–250 | M10 | 2.000 |
| 10–15 m | 250–300 | M10 | 3.000 |
| 12–18 m | 300–350 | M12 | 4.500 |
| 15–22 m | 350–400 | M12 | 6.000 |
| 20–40 m | 400–500 | M16 | 10.000 |

#### 8.6.2 Hersteller und Preise

| Hersteller | Modell | Länge (mm) | Material | Preis (EUR) |
|-----------|--------|-----------|----------|-------------|
| Lewmar | Open Base Cleat | 150 | 316L | 35 |
| Lewmar | Open Base Cleat | 200 | 316L | 48 |
| Lewmar | Open Base Cleat | 250 | 316L | 65 |
| Lewmar | Open Base Cleat | 300 | 316L | 89 |
| Osculati | Heavy Duty Cleat | 200 | 316L | 32 |
| Osculati | Heavy Duty Cleat | 250 | 316L | 45 |
| Osculati | Heavy Duty Cleat | 300 | 316L | 62 |
| Wichard | Forged Cleat | 200 | 316L geschmiedet | 55 |
| Wichard | Forged Cleat | 250 | 316L geschmiedet | 72 |
| Wichard | Forged Cleat | 300 | 316L geschmiedet | 95 |

#### 8.6.3 Befestigung

- **Durchgehende Bolzen**: Mindestens 4× M8 (Kleinboot) bis 6× M12 (große Yacht)
- **Gegenplatte**: 316L Edelstahl, Mindestfläche 150×80 mm
- **Dichtmittel**: Sikaflex 291i, keine Silikone
- **Decksverstärkung**: Bei GFK-Deck Holzkern oder GFK-Aufdopplung im Klampenbereich

### 8.7 Poller am Bug

Bei größeren Yachten (ab 15 m) werden anstelle oder zusätzlich zu Klampen
Poller am Bug montiert:

| Typ | Höhe (mm) | Durchmesser (mm) | Material | Preis (EUR) |
|-----|----------|-----------------|----------|-------------|
| Einfachpoller | 120–200 | 60–100 | 316L / Bronze | 80–250 |
| Doppelpoller | 150–250 | 60–80 × 2 | 316L / Bronze | 150–400 |
| Kreuzpoller | 120–200 | 50–80 | 316L | 120–350 |

**Vorteil gegenüber Klampen**: Höhere Belastbarkeit, einfacheres Belegen,
keine Verletzungsgefahr durch scharfe Kanten.

---

## 9. Ankerkästen und -taschen

### 9.1 Ankerkästen (Anchor Lockers)

#### 9.1.1 Typen

**Integrierter Ankerkasten (Built-in Locker):**
- In den Vorschiffsrumpf integriert
- Zugang über Decksluke
- Standard bei Serienbooten ab 8 m
- Volumen: 50–500 Liter je nach Bootsgröße

**Aufgesetzter Ankerkasten (Deck Locker):**
- Auf dem Vordeck montierter Kasten
- Häufig bei Retrofits oder Fischerbooten
- Material: GFK, Aluminium oder 316L
- Volumen: 30–200 Liter

**Bugsprit-Ankerkasten:**
- In den Bugsprit integriert
- Saubere Lösung für Katamarane und Trawler
- Aufwändiger Einbau

#### 9.1.2 Dimensionierung

| Bootsklasse | Kettenmenge | Kettenvolumen (l) | Empf. Kastenvolumen (l) |
|-------------|-----------|-------------------|------------------------|
| Kleinkreuzer 6–8 m | 30 m × 6 mm | 15 | 30–50 |
| Fahrtenyacht 8–12 m | 50 m × 8 mm | 45 | 80–120 |
| Blauwasser 10–15 m | 80 m × 10 mm | 110 | 180–250 |
| Performance 12–18 m | 80 m × 10 mm | 110 | 180–250 |
| Ketch 15–22 m | 100 m × 12 mm | 200 | 300–400 |
| Superyacht 20–40 m | 120 m × 14 mm | 350 | 500–700 |

**Berechnungsformel:**

```
Kettenvolumen (Liter) = Kettenlänge_m × (Kettendurchmesser_mm / 10)² × 0,55
Kastenvolumen (Liter) = Kettenvolumen × 1,8 (für lose fallende Kette)
```

#### 9.1.3 Entwässerung

- **Pflicht**: Jeder Ankerkasten muss selbstlenzend sein
- **Minimum**: 2 Ablauföffnungen (Steuerbord/Backbord) mit ∅ ≥ 25 mm
- **Empfohlen**: Ablaufrinne zum tiefsten Punkt, Schlauch nach außenbords
- **Rückschlagventil**: Bei Ankerkasten unter der Wasserlinie zwingend

#### 9.1.4 Belüftung

Ankerkästen müssen belüftet sein, um:
- Korrosion der Kette zu reduzieren (Feuchtigkeit abführen)
- Geruchsbildung zu verhindern (Schlick, Algen)
- Kondensation zu minimieren

**Empfehlung**: Mindestens 2 Lüftungsöffnungen (je 25 cm² Querschnitt)
mit Edelstahl-Lüfterrosten.

### 9.2 Ankertaschen

#### 9.2.1 Typen und Einsatz

Ankertaschen werden verwendet, wenn kein integrierter Ankerkasten vorhanden ist
oder für die Lagerung von Reserveankern.

| Typ | Material | Einsatz | Preis (EUR) |
|-----|----------|---------|-------------|
| Flache Ankertasche | 600D Polyester, PVC-beschichtet | Zweitanker, Steganker | 25–60 |
| Tiefe Ankertasche | 1000D Cordura | Hauptanker Kleinboot | 40–90 |
| Ankerkorb | Edelstahl-Draht | Heckanker, offen | 35–80 |
| Anker-Rollentasche | Nylon + Schaumstoff | Danforth/Fortress Transport | 30–65 |

#### 9.2.2 Hersteller

| Hersteller | Modell | Für Anker bis | Material | Preis (EUR) |
|-----------|--------|-------------|----------|-------------|
| Plastimo | Anchor Stow Bag S | 8 kg | PVC 600D | 28 |
| Plastimo | Anchor Stow Bag M | 15 kg | PVC 600D | 38 |
| Plastimo | Anchor Stow Bag L | 25 kg | PVC 600D | 52 |
| Burke Marine | Anchor Bag Deluxe | 20 kg | 1000D Cordura | 65 |
| Musto | Anchor Bag | 12 kg | PVC 600D | 45 |
| Navyline | Ankertasche | 10 kg | Polyester | 22 |
| Navyline | Ankertasche XL | 20 kg | Polyester | 35 |

### 9.3 Ankerkastendeckel und -luken

#### 9.3.1 Typen

| Typ | Beschreibung | Dichtung | Preis (EUR) |
|-----|-------------|---------|-------------|
| Klappdeckel mit Scharnier | Standard, nach oben klappend | EPDM oder Neoprene | 45–180 |
| Schiebedeckel | Seitlich verschiebbar | Filzdichtung | 60–200 |
| Flush-Deckel | Bündig mit Deck, versenkte Griffe | EPDM | 120–350 |
| Gasdruckfeder-Deckel | Klappbar mit Gasdruckfeder-Unterstützung | EPDM | 180–450 |

#### 9.3.2 Dichtungstypen

| Material | Temperaturbereich | UV-Beständigkeit | Lebensdauer | Preis/m (EUR) |
|----------|------------------|-----------------|-------------|---------------|
| EPDM | -40° bis +120°C | Gut | 8–12 Jahre | 3–8 |
| Neoprene (CR) | -30° bis +100°C | Mäßig | 5–8 Jahre | 4–10 |
| Silikon | -60° bis +200°C | Hervorragend | 10–15 Jahre | 6–15 |
| PVC weich | -20° bis +60°C | Schlecht | 3–5 Jahre | 2–5 |

**AYDI-Empfehlung**: EPDM-Dichtung als bester Kompromiss aus Preis, Haltbarkeit
und UV-Beständigkeit. Alle 5–8 Jahre austauschen.

### 9.4 Kettenführung im Ankerkasten

Damit die Kette sich nicht im Kasten verknotet, sind Kettenführungen sinnvoll:

| Methode | Beschreibung | Kosten (EUR) | Wirksamkeit |
|---------|-------------|-------------|-------------|
| PVC-Fallrohr | Vertikales Rohr vom Decksdurchlass zum Kastenboden | 20–50 | Gut |
| Edelstahl-Leitschiene | Führungsschiene vom Durchlass zum Boden | 80–200 | Sehr gut |
| Kettensammelkorb | Edelstahlkorb im Kasten, Kette fällt geordnet | 100–300 | Hervorragend |
| Ketten-Separator | Trennwand im Kasten für Haupt-/Zweitkette | 50–150 | Gut (2 Ketten) |

**Prinzip**: Die Kette soll vom Decksdurchlass gerade nach unten in den tiefsten
Punkt des Kastens fallen. Horizontale Umlenkungen verursachen Verknäulung.

---

## 10. Ankerlicht und Signale

### 10.1 Rechtliche Grundlage

Gemäß den Kollisionsverhütungsregeln (KVR / ColRegs) muss ein ankerndes
Fahrzeug folgende Signale führen:

#### 10.1.1 Nachtsignal

- **Weißes Rundumlicht** (360°) im vorderen Teil des Schiffes
- Bei Schiffen >50 m: Zusätzliches weißes Rundumlicht achtern, tiefer als vorne
- Sichtweite: Mindestens 2 sm (Boote <50 m), 3 sm (Boote ≥50 m)
- Position: Möglichst hoch (Mast oder Ankerlichtstange)

#### 10.1.2 Tagsignal

- **Schwarzer Ball** (Ankerball) ∅ ≥ 300 mm im Vorschiff
- Position: Möglichst gut sichtbar, am Vorstag oder separater Stange
- Pflicht auch bei kleinen Sportbooten (oft ignoriert)

### 10.2 Ankerlichter — Typen und Hersteller

| Hersteller | Modell | Typ | Leuchtmittel | Sichtweite (sm) | Leistung (W) | Preis (EUR) |
|-----------|--------|-----|-------------|-----------------|-------------|-------------|
| Hella Marine | NaviLED 360 | Aufsteck | LED | 2 | 0,5 | 65 |
| Hella Marine | NaviLED 360 Pro | Aufsteck | LED | 2 | 0,7 | 89 |
| Aqua Signal | Serie 34 | Aufsteck | LED | 2 | 0,5 | 55 |
| Aqua Signal | Serie 43 | Masttop | LED | 3 | 1,2 | 149 |
| Lalizas | FOS LED 360 | Aufsteck | LED | 2 | 0,3 | 29 |
| Lalizas | Classic 20 | Aufsteck | Glühbirne | 2 | 10 | 19 |
| Perko | 1134 | Aufsteck | LED | 2 | 0,5 | 45 |
| Perko | 1311 | Masttop | LED | 3 | 1,5 | 129 |
| Osculati | Orion | Aufsteck | LED | 2 | 0,4 | 35 |

### 10.3 Stromverbrauch und Autonomie

| Typ | Leistung (W) | Strom bei 12V (mA) | 10h Nacht (Ah) | 100Ah-Batterie (Nächte) |
|-----|-------------|--------------------|-----------------|-----------------------|
| LED Modern | 0,3–0,7 | 25–58 | 0,25–0,58 | >170 |
| LED Premium | 0,5–1,5 | 42–125 | 0,42–1,25 | 80–240 |
| Glühbirne | 10–25 | 830–2.080 | 8,3–20,8 | 5–12 |

**Empfehlung**: LED-Ankerlichter haben sich vollständig durchgesetzt. Die
Stromersparnis gegenüber Glühbirnen beträgt Faktor 20–40.

### 10.4 Installation

#### 10.4.1 Montageoptionen

| Montage | Beschreibung | Vorteil | Nachteil |
|---------|-------------|---------|----------|
| Masttop fest | Am Mast montiert, geschaltet | Höchste Sichtbarkeit | Dauerhaft montiert |
| Aufsteckbar Mast | Auf Mastfuß-Halter | Abnehmbar | Wind-empfindlich |
| Ankerlichtstange | Separate Stange am Bug | Flexibel, gute Sicht | Zusätzliche Stange |
| Solarlaterne | Autonome LED mit Solarzelle | Kein Kabel nötig | Begrenzte Helligkeit |

#### 10.4.2 Kabelanforderungen

| Mastlänge (m) | Kabelquerschnitt (mm²) | Sicherung (A) |
|--------------|----------------------|---------------|
| Bis 12 | 1,0 | 1 (LED) / 3 (Glühbirne) |
| 12–16 | 1,5 | 1 (LED) / 3 (Glühbirne) |
| 16–22 | 2,5 | 2 (LED) / 5 (Glühbirne) |

### 10.5 Ankerlichtalarm und Ankerüberwachung

Moderne Systeme kombinieren Ankerlicht mit GPS-Überwachung:

| Hersteller | Modell | Funktion | Preis (EUR) |
|-----------|--------|----------|-------------|
| Garmin | Anchor Alarm (integriert) | GPS-Ankeralarm im Plotter | In Plotter enthalten |
| Simrad | Anchor Watch | GPS-Alarm + Logbuch | In Plotter enthalten |
| DragAlarm | Standalone | GPS + SMS-Benachrichtigung | 89 |
| Yacht Devices | YDAB-01 | NMEA2000 Ankeralarm | 129 |
| SailTimer | Anchor Watch App | Smartphone-App (iOS/Android) | 0–5 (App) |

**Funktionsweise:**
1. GPS-Position beim Ankern speichern
2. Alarmradius definieren (z.B. Schwoikreis + 20%)
3. Bei Überschreitung: Akustischer Alarm und/oder SMS/Push-Benachrichtigung
4. Besonders wichtig bei Nachtankern und bei ablandigem Wind

### 10.6 Sonderregelungen nach Revier

| Revier | Besonderheit | Ankerverbot/Einschränkung |
|--------|-------------|-------------------------|
| Naturschutzgebiete (DE) | Ankern oft verboten | Bojen-Festmachung statt Ankern |
| Seegraswiesen (Balearen) | Ankern über Posidonia verboten | Bojen oder Sandgrund nutzen |
| Korallenriffe (Karibik) | Ankern auf Korallen verboten | Mooring-Bojen verwenden |
| Fahrwasser | Ankern im Fahrwasser verboten | Seitlich versetzen |
| Häfen | Ankern nur in Ankerzonen | Hafenordnung beachten |
| Militärsperrgebiete | Ankern verboten | Seekarte prüfen |

---

## 11. Kettenstopper (Chain Stoppers / Devil's Claw)

### 11.1 Funktion und Bedeutung

Der Kettenstopper ist eines der wichtigsten und am häufigsten
unterschätzten Elemente des Ankergeschirrs. Er übernimmt die Ankerlast
von der Winde und leitet sie in die Bugstruktur ein.

**Warum ein Kettenstopper unverzichtbar ist:**
- Die Ankerwinch ist NICHT dafür gebaut, die Ankerlast dauerhaft zu halten
- Ohne Kettenstopper ruht die gesamte Zugkraft auf der Windentrommel/Kettennuss
- Dies führt zu vorzeitigem Verschleiß des Windengetriebes
- Bei Windenausfall hält nur der Kettenstopper den Anker

### 11.2 Bauformen

#### 11.2.1 Hebelkettenstopper (Lever Chain Stopper)

- **Beschreibung**: Hebelklappe, die in ein Kettenglied greift
- **Bedienung**: Hebel umlegen, Kette wird geklemmt
- **Vorteil**: Schnelle Bedienung, hohe Haltekraft
- **Nachteil**: Muss zur Kettengröße passen
- **Preis**: 89–350 EUR je nach Größe

#### 11.2.2 Fallkettenstopper (Guillotine Chain Stopper)

- **Beschreibung**: Vertikaler Keil, der durch Schwerkraft in die Kette fällt
- **Bedienung**: Keil anheben = Kette frei, Keil fallen lassen = gesichert
- **Vorteil**: Automatische Sicherung bei Lose
- **Nachteil**: Schwerer, muss vertikal montiert werden
- **Preis**: 120–450 EUR

#### 11.2.3 Schraubkettenstopper (Screw Chain Stopper)

- **Beschreibung**: Schraubklemme, die die Kette gegen eine Fläche presst
- **Bedienung**: Schraube anziehen
- **Vorteil**: Universell, passt für verschiedene Kettengrößen
- **Nachteil**: Langsame Bedienung
- **Preis**: 60–180 EUR

#### 11.2.4 Devil's Claw (Kettenkralle)

- **Beschreibung**: Hakengabel, die in ein Kettenglied greift, mit Sicherungsstift
- **Bedienung**: Kralle in Kettenglied einhängen, sichern
- **Vorteil**: Sehr hohe Haltekraft, einfache Konstruktion
- **Nachteil**: Umständliches Ein-/Aushängen unter Last
- **Preis**: 45–180 EUR

#### 11.2.5 Ankerkettenbremse (Chain Brake)

- **Beschreibung**: Fußpedal-betätigte Bremse in der Kettenführung
- **Bedienung**: Pedal treten = Kette gebremst, loslassen = frei
- **Vorteil**: Stufenlos regelbar, fußbetätigt (Hände frei)
- **Nachteil**: Nicht als Dauerstopper geeignet, nur Manövrierhilfe
- **Preis**: 150–400 EUR

### 11.3 Hersteller und Preise

| Hersteller | Modell | Typ | Kette (mm) | WLL (kg) | Material | Preis (EUR) |
|-----------|--------|-----|-----------|----------|----------|-------------|
| Lewmar | Chain Stopper | Hebel | 6–8 | 1.500 | 316L | 95 |
| Lewmar | Chain Stopper | Hebel | 8–10 | 2.500 | 316L | 129 |
| Lewmar | Chain Stopper | Hebel | 10–12 | 3.500 | 316L | 169 |
| Lewmar | Chain Stopper | Hebel | 12–14 | 5.000 | 316L | 229 |
| Lewmar | Chain Stopper | Hebel | 14–16 | 7.000 | 316L | 329 |
| Maxwell | Chain Stopper | Hebel | 6–8 | 1.200 | 316L | 89 |
| Maxwell | Chain Stopper | Hebel | 8–10 | 2.200 | 316L | 119 |
| Maxwell | Chain Stopper | Hebel | 10–13 | 3.500 | 316L | 159 |
| Maxwell | Chain Stopper | Hebel | 13–16 | 5.500 | 316L | 249 |
| Kong | Devil's Claw | Kralle | 8–10 | 2.000 | 316L | 65 |
| Kong | Devil's Claw | Kralle | 10–12 | 3.000 | 316L | 85 |
| Kong | Devil's Claw | Kralle | 12–14 | 4.500 | 316L | 119 |
| Mantus | Chain Hook | Kralle | 6–8 | 1.800 | 316L | 59 |
| Mantus | Chain Hook | Kralle | 8–10 | 2.800 | 316L | 79 |
| Mantus | Chain Hook | Kralle | 10–13 | 4.000 | 316L | 99 |
| Mantus | Chain Hook | Kralle | 13–16 | 6.000 | 316L | 139 |
| Osculati | Chain Stopper | Schraube | 6–10 | 1.500 | 316L | 68 |
| Osculati | Chain Stopper | Schraube | 10–14 | 3.000 | 316L | 98 |
| Plastimo | Guillotine | Guillotine | 8–10 | 2.000 | 316L + Nylon | 135 |
| Plastimo | Guillotine | Guillotine | 10–12 | 3.000 | 316L + Nylon | 185 |
| Plastimo | Guillotine | Guillotine | 12–14 | 4.500 | 316L + Nylon | 245 |

### 11.4 Dimensionierung

#### 11.4.1 Grundregel

```
WLL_Kettenstopper ≥ WLL_Kette
WLL_Kettenstopper ≥ Bootsgewicht × 1,5 (Küste)
WLL_Kettenstopper ≥ Bootsgewicht × 2,5 (Blauwasser)
```

#### 11.4.2 Montageposition

| Position | Abstand Winde–Stopper | Vorteil |
|----------|----------------------|---------|
| Direkt vor Winde | 200–500 mm | Kurze Kettenstrecke ohne Sicherung |
| Am Klüsenaustritt | 0–200 mm | Kette direkt an Austritt gesichert |
| Zwischen Winde und Bugrolle | 500–1.500 mm | Kompromiss, flexible Platzierung |

#### 11.4.3 Befestigung

- Mindestens 4 Bolzen M8 (bis 12 m Boot), M10 (ab 12 m)
- Unterdeck-Gegenplatte aus 316L, Mindestfläche 100×100 mm
- Decksverstärkung erforderlich (GFK-Aufdopplung oder Holzkern)
- Dichtmittel: Sikaflex 291i oder 3M 5200

### 11.5 Ankerkette sichern — Best Practices

#### 11.5.1 Reiterleine (Snubber / Bridle)

Zusätzlich zum Kettenstopper wird eine Reiterleine empfohlen:

```
Kette → Kettenstopper → Reiterleine (Nylon) → Klampe
```

**Dimensionierung Reiterleine:**

| Bootsklasse | Leinendurchmesser (mm) | Länge (m) | Material |
|-------------|----------------------|-----------|----------|
| Kleinkreuzer 6–8 m | 12–14 | 5–8 | Nylon 3-schäftig |
| Fahrtenyacht 8–12 m | 14–16 | 8–12 | Nylon 3-schäftig |
| Blauwasser 10–15 m | 16–18 | 10–15 | Nylon 3-schäftig |
| Performance 12–18 m | 18–20 | 12–18 | Nylon 3-schäftig |

**Funktion der Reiterleine:**
- Nimmt Rucklasten beim Schwojen auf (Nylon-Dehnung = Stoßdämpfer)
- Entlastet Ankerwinde und Kettenstopper
- Reduziert Kettengeräusche in der Ankerklüse
- Verhindert Ruck-Belastungen auf die Bugstruktur

### 11.6 Reiterleine — Detaillierte Anleitung

#### 11.6.1 Reiterleine ausbringen (Schritt für Schritt)

1. Kette auf gewünschte Länge ausfahren
2. Kettenstopper schließen → Kette ist arretiert
3. Winde entlasten (etwas Kette fieren bis Stopper Last übernimmt)
4. Mantus Chain Hook (oder ähnlich) in ein Kettenglied einhängen
5. Reiterleine am Chain Hook befestigen (Palstek oder gespleißtes Auge)
6. Reiterleine über Klüse/Bugrolle zur Bugklampe führen
7. An der Klampe belegen (ausreichend Törns)
8. Kette von der Winde etwas fieren, bis Reiterleine Last übernimmt
9. Kette hängt jetzt lose zwischen Kettenstopper und Klüse
10. Reiterleine trägt die Ankerlast über die Klampe

#### 11.6.2 Scheuerschutz für die Reiterleine

| Methode | Material | Haltbarkeit | Preis (EUR) |
|---------|----------|-------------|-------------|
| Chafe Guard (Schlauch) | PVC/Nylon | 1–3 Saisons | 8–20 |
| Lederwicklung | Rindsleder | 3–6 Saisons | 15–30 |
| Dyneema-Hülse | UHMWPE | 5–10 Saisons | 20–45 |
| Teflon-Schlauch | PTFE | 5+ Saisons | 15–35 |
| Doppelte Reiterleine | Nylon (Backup) | — | 30–60 |

**AYDI-Empfehlung**: Immer Scheuerschutz an der Klüse montieren.
Bei Blauwasser: Dyneema-Hülse für maximale Haltbarkeit. Bei Sturm:
Zweite Reiterleine als Backup ausbringen.

#### 11.6.3 Bridle-System für Katamarane

Katamarane verwenden statt einer einzelnen Reiterleine ein Bridle-System
(V-förmige Doppelleine):

```
                Kette
                  |
            [Chain Hook]
               /    \
     Reiterleine    Reiterleine
     (BB-Klampe)    (StB-Klampe)
```

**Dimensionierung Bridle:**
- Jeder Schenkel: Gleicher Durchmesser wie Mono-Reiterleine
- Schenkellänge: Rumpfbreite × 1,5
- Y-Stück: Edelstahl-Ring oder Mantus Bridle Plate

| Katamaran-Breite (m) | Schenkellänge (m) | Leinendurchmesser (mm) |
|----------------------|-------------------|----------------------|
| 6–7 (kleiner Kat) | 9–10 | 14 |
| 7–8 (Standard) | 10–12 | 16 |
| 8–10 (groß) | 12–15 | 18 |
| 10–12 (Superyacht) | 15–18 | 20 |

---

## 12. Ankermarkierung

### 12.1 Zweck

Die Ankermarkierung dient dazu:
- Die ausgebrachte Kettenlänge schnell abzulesen
- Die korrekte Schwoikreis-Berechnung zu ermöglichen
- Das Ankermanöver sicherer und effizienter zu gestalten

### 12.2 Markierungssysteme

#### 12.2.1 Farbmarkierung

| Kettenlänge (m) | Farbe | Markierungsmethode |
|----------------|-------|-------------------|
| 10 | Rot | Farbstreifen oder Kabelbinder |
| 15 | Blau | Farbstreifen oder Kabelbinder |
| 20 | Gelb | Farbstreifen oder Kabelbinder |
| 25 | Grün | Farbstreifen oder Kabelbinder |
| 30 | Weiß | Farbstreifen oder Kabelbinder |
| 35 | Rot (2×) | Doppelmarkierung |
| 40 | Blau (2×) | Doppelmarkierung |
| 45 | Gelb (2×) | Doppelmarkierung |
| 50 | Grün (2×) | Doppelmarkierung |

#### 12.2.2 Kabelbinder-System

- Farbige Kabelbinder an definierten Positionen durch Kettenglieder
- **Vorteil**: Günstig, einfach nachzurüsten, am Kettenzähler und an Markierung erkennbar
- **Nachteil**: Kabelbinder verschleißen (UV, Reibung), regelmäßig erneuern
- **Material**: UV-beständige Kabelbinder, Breite 4,8 mm

#### 12.2.3 Sprühfarben-Markierung

- Kettenabschnitte mit mariner Sprühfarbe markieren
- **Vorteil**: Gut sichtbar, auch nachts mit Taschenlampe
- **Nachteil**: Farbe scheuert ab, muss alle 1–2 Saisons erneuert werden
- **Empfehlung**: Markierungsfarbe auf Epoxidbasis (haltbarer als Acryl)

#### 12.2.4 Elektronische Kettenzähler

- Sensor an der Winde zählt Kettenglieder
- **Vorteil**: Exakte Messung, Display am Steuerstand
- **Nachteil**: Kalibrierung nötig, Sensorausfall möglich
- Hersteller: Lewmar (ab 189 EUR), Maxwell (ab 169 EUR), Quick (ab 210 EUR)

#### 12.2.5 Professionelle Markierungsmethoden

Für gewerbliche Yachten und Charterbetrieb werden haltbarere Methoden verwendet:

| Methode | Beschreibung | Haltbarkeit | Kosten (EUR) |
|---------|-------------|-------------|-------------|
| Eingeschlagene Marken | Punzen-Markierung auf Kettenglied | Dauerhaft | 2–5 pro Markierung |
| Aufgeschweißte Wulste | Kleine Schweißpunkte als taktile Markierung | Dauerhaft | Werft-Arbeit |
| Farbtauchen | Kette in Farbwanne tauchen (Epoxid) | 3–5 Jahre | 30–50 gesamt |
| Kunststoff-Kabelschuhe | Crimphülsen in Farben auf Kettenglieder | 2–4 Jahre | 15–25 gesamt |
| Markierungsfahnen | Nylon-Fähnchen durch Kettenglied | 1–2 Jahre | 10–20 gesamt |

**Für AYDI-Analyse:**
Bei der visuellen Analyse kann das Vorhandensein und der Zustand der
Kettenmarkierung automatisch erkannt werden. Fehlende oder unleserliche
Markierung wird als F-17_04-12 erfasst.

### 12.3 Endmarkierung

**Pflicht**: Das Kettenende muss markiert und gesichert sein!

- Kettenende NICHT fest mit dem Boot verbinden (Soll-Bruchstelle oder
  Schnellauslösung, damit die Kette im Notfall losgelassen werden kann)
- Markierung des letzten Meters: Rote Markierung, deutlich sichtbar
- Empfehlung: 3 m vor dem Ende → rote Sprühfarbe, letztes Glied → Kabelbinder rot

### 12.4 Soll-Bruchstelle am Kettenende

| Methode | Beschreibung | Bruchlast |
|---------|-------------|-----------|
| Kabelbinder | 3× Kabelbinder 7,6 mm durch letztes Glied | ~200 kg |
| Dyneema-Lashing | 3 mm Dyneema, 3 Windungen | ~500 kg |
| Sollbruch-Schäkel | Schwacher Schäkel mit definierter Bruchlast | 300–800 kg |
| Schnellauslösung | Bolzen mit Ring, manuell ziehbar | ∞ (manuell) |

**Wichtig**: Die Soll-Bruchstelle muss stark genug sein, um normales
Ankern auszuhalten, aber schwach genug, um bei Notfall (Kette verhakt,
Sturm, Kollision) die Kette loszulassen, bevor das Boot beschädigt wird.

### 12.5 AYDI-Bewertungskriterien für Ankermarkierung

| Kriterium | Gewicht | 100 Punkte | 50 Punkte | 0 Punkte |
|-----------|---------|-----------|-----------|----------|
| Markierung vorhanden | 30% | Vollständig, alle 5–10 m | Teilweise, >50% lesbar | Keine/unleserlich |
| Markierungsmethode | 20% | Epoxid-Farbe + Kabelbinder | Nur Kabelbinder | Nur Edding/Klebeband |
| Endmarkierung | 20% | Rote Markierung + Soll-Bruchstelle | Nur Soll-Bruchstelle | Weder noch |
| Kettenzähler | 15% | Kalibrierter elektronischer Zähler | Unkalibriert | Nicht vorhanden |
| Lesbarkeit | 15% | Auf 1 m Entfernung eindeutig | Nur bei genauem Hinsehen | Nicht erkennbar |

---

## 13. Fehlerbild-Atlas

### Fehlerbild F-17_04-01: Korrodierter Ankerwirbel

**Beschreibung**: Ankerwirbel zeigt sichtbare Korrosion (Lochfraß,
Spaltkorrosion, Verfärbung, Rostflecken).

**Ursache**:
- Falsches Material (304 statt 316L)
- Galvanische Korrosion durch Materialpaarung (z.B. verzinkter Schäkel an 316L-Wirbel)
- Mangelhafte Wartung (keine Süßwasser-Spülung)
- Dauerhafte Salzwasser-Exposition ohne Trocknung
- Chlorid-Konzentration in stehendem Wasser (Ankerkasten)

**Bewertung**: KRITISCH — Korrodierte Wirbel können ohne Vorwarnung brechen.

**Maßnahme**:
- Sofortiger Austausch bei sichtbarem Lochfraß (Materialquerschnitt reduziert)
- Materialprüfung mit Magnet (316L = nicht magnetisch, 304 = leicht magnetisch)
- Bei oberflächlicher Verfärbung: Reinigung mit Oxalsäure, Beobachtung
- Präventiv: Regelmäßige Süßwasser-Spülung, Trocknung im Ankerkasten sicherstellen

**Confidence**: `visual_high` (Korrosion am Wirbel gut erkennbar auf Fotos)

---

### Fehlerbild F-17_04-02: Blockierter Ankerwirbel

**Beschreibung**: Ankerwirbel dreht sich nicht mehr frei, ist steif oder
vollständig blockiert.

**Ursache**:
- Salzablagerungen im Drehgelenk
- Kugellager-Verschleiß (bei Kugellager-Wirbeln)
- Korrosion im Lagersitz
- Verformung durch Überlastung
- Sand/Schlamm im Mechanismus

**Bewertung**: HOCH — Blockierter Wirbel verursacht Torque in der Kette,
kann zu Kettenverknäulung und Ankerversagen führen.

**Maßnahme**:
- Reinigung mit Süßwasser und Bürste
- WD-40 oder Ballistol als Kriechöl zum Lösen
- Kugellager fetten (marine Fett, z.B. Lewmar Winch Grease)
- Bei Verformung: Sofortiger Austausch

**Confidence**: `visual_medium` (Blockierung auf Foto nur indirekt erkennbar —
Anzeichen: verdrehte Kette oberhalb des Wirbels)

---

### Fehlerbild F-17_04-03: Gebrochene Ankerrolle

**Beschreibung**: Bugrolle oder deren Achse ist gebrochen, gerissen oder
verbogen.

**Ursache**:
- Überlastung (zu schwerer Anker für die Rolle)
- Materialermüdung (Dauerschwingbelastung durch Seegang)
- Korrosion (insb. Spaltkorrosion an den Achsbohrungen)
- Kollision (Ankerhandling, Anlegen)
- Unterdimensionierte Wangen oder Achse

**Bewertung**: KRITISCH — Anker kann sich vom Bug lösen und Schäden am Rumpf
verursachen. Ankermanöver nicht mehr sicher durchführbar.

**Maßnahme**:
- Sofortiger Austausch der gesamten Bugrolle
- Prüfung der Decksverstärkung (Gegenplatten)
- Ursachenanalyse: War die Rolle richtig dimensioniert?
- Ggf. Upgrade auf nächstgrößere Rolle

**Confidence**: `visual_high` (Bruch/Riss an der Bugrolle gut erkennbar)

---

### Fehlerbild F-17_04-04: Undichter Ankerkasten

**Beschreibung**: Wasser dringt aus dem Ankerkasten in angrenzende Bereiche
ein (Vorschiffskabine, Segellast, Stauraum).

**Ursache**:
- Defekte Dichtung der Ankerkastenluke
- Riss im Ankerkasten-Laminat
- Verstopfte oder fehlende Entwässerung
- Durchbruch für Kettendurchführung undicht
- Ankerklüse ohne Deckel oder mit defektem Deckel

**Bewertung**: MITTEL bis HOCH — Wassereinbruch schädigt Innenausbau,
fördert Osmose/Fäulnis, kann bei schwerem Wetter gefährlich werden.

**Maßnahme**:
- Dichtung der Luke erneuern
- Entwässerung prüfen und reinigen
- Klüsendeckel montieren oder ersetzen
- Laminat-Risse mit Epoxid reparieren
- Kettendurchführung mit Sikaflex abdichten

**Confidence**: `visual_medium` (Wasserflecken oft sichtbar, Ursache
erfordert detaillierte Inspektion)

---

### Fehlerbild F-17_04-05: Schäkelbolzen gelöst

**Beschreibung**: Der Bolzen eines Ankerschäkels hat sich gelöst oder ist
verloren gegangen. Schäkel hängt nur noch am Bügel.

**Ursache**:
- Keine Bolzensicherung (Draht/Splint) montiert
- Kabelbinder als Ersatz verwendet (UV-zerfall)
- Vibrationen haben Bolzen gelockert
- Falsches Gewinde (Bolzen passt nicht exakt)

**Bewertung**: KRITISCH — Schäkel kann sich öffnen, Anker geht verloren.
Sofortige Gefahr bei Ankerlast.

**Maßnahme**:
- Neuen Bolzen einschrauben und mit 316L-Sicherungsdraht sichern
- Alle Schäkel des Ankergeschirrs auf Bolzensitz prüfen
- Sicherungsdraht bei jeder Saison erneuern
- Alternative: Wichard Self-Locking-Schäkel verwenden

**Confidence**: `visual_high` (Fehlender Bolzen eindeutig erkennbar)

---

### Fehlerbild F-17_04-06: Kettenstopper-Versagen

**Beschreibung**: Kettenstopper hält die Kette nicht mehr, Kette rutscht durch
oder Stopper bricht.

**Ursache**:
- Hebelmechanismus verschlissen
- Korrosion am Klemmbereich
- Falsche Kettengröße (Kette zu klein für Stopper)
- Befestigungsbolzen gelockert oder gebrochen
- Überlastung (Rucklast bei Sturmböe ohne Reiterleine)

**Bewertung**: KRITISCH — Gesamte Ankerlast fällt auf die Winde, die dafür
nicht ausgelegt ist. Windengetriebe-Schaden wahrscheinlich.

**Maßnahme**:
- Stopper sofort reparieren oder austauschen
- Ersatzweise: Kette mit Kettenkralle (Devil's Claw) sichern
- Reiterleine (Snubber) als zusätzliche Sicherung einrichten
- Befestigungsbolzen mit vorgeschriebenem Drehmoment nachziehen

**Confidence**: `visual_medium` (Verschleiß am Stopper erkennbar, Versagen
erst unter Last feststellbar)

---

### Fehlerbild F-17_04-07: Verklemmter Anker ohne Tripleine

**Beschreibung**: Anker sitzt im Grund fest und kann nicht gelichtet werden.
Keine Tripleine vorhanden.

**Ursache**:
- Anker unter Felsen/Korallen/Kabel verklemmt
- Keine Tripleine montiert
- Kette in Wrackteilen verfangen
- Zu starker Eingrabeeffekt bei langem Liegen

**Bewertung**: HOCH — Ankerverlust droht. Bergungsversuch kann Winde
oder Bugbeschläge beschädigen.

**Maßnahme**:
- Motorisch über den Anker fahren und aus verschiedenen Richtungen ziehen
- Kette auf Slip mit Klampe führen, Boot rückwärts gegen fahren
- Taucher beauftragen (ab 150 EUR)
- Im Notfall: Kette an Boje legen und später bergen
- Prävention: Immer Tripleine verwenden bei unbekanntem Grund

**Confidence**: `visual_low` (Situation nur indirekt erkennbar — gespannte
Kette, Boot liegt nicht frei)

---

### Fehlerbild F-17_04-08: Ankerball fehlt

**Beschreibung**: Boot liegt vor Anker, führt aber keinen Ankerball (Tag)
oder kein Ankerlicht (Nacht).

**Ursache**:
- Ankerball nicht an Bord
- Crew kennt die Pflicht nicht
- Bequemlichkeit/Nachlässigkeit
- Ankerlicht-Glühbirne defekt
- Kabelbruch zum Masttop-Ankerlicht

**Bewertung**: MITTEL — Ordnungswidrigkeit, Bußgeld möglich.
Wichtiger: Andere Schiffe erkennen den Ankerlieger nicht → Kollisionsgefahr.

**Maßnahme**:
- Ankerball und LED-Ankerlicht beschaffen (Investition: ab 30 EUR)
- Crew einweisen (KVR Regel 30)
- LED-Ankerlicht auf Funktion prüfen vor Saisonstart
- Reservelampe oder autonomes Solar-Ankerlicht mitführen

**Confidence**: `visual_high` (Fehlen des Ankerballs/Ankerlichts auf Fotos
eindeutig erkennbar)

---

### Fehlerbild F-17_04-09: Galvanische Korrosion an Beschlägen

**Beschreibung**: An der Verbindungsstelle verschiedener Metalle zeigt sich
verstärkte Korrosion (weißer/grüner Belag, Metallabbau).

**Ursache**:
- Unverträgliche Materialpaarung (z.B. Aluminium-Bugrolle mit 316L-Bolzen)
- Verzinkter Schäkel an Edelstahlkette
- Bronze-Klüse neben Aluminium-Beschlag
- Fehlende galvanische Isolation

**Bewertung**: HOCH — Galvanische Korrosion beschleunigt Materialabbau
exponentiell. Bruchgefahr an tragenden Teilen.

**Maßnahme**:
- Alle Materialpaarungen im Bugbereich prüfen
- Galvanische Reihe beachten: Nur gleiche oder benachbarte Metalle paaren
- Bei unvermeidlicher Materialpaarung: Nylon-Buchsen als Isolation einsetzen
- Opferanoden im Bugbereich prüfen

**Confidence**: `visual_medium` (Korrosion sichtbar, Materialpaarung auf
Foto nicht immer eindeutig bestimmbar)

---

### Fehlerbild F-17_04-10: Kette scheuert am Bug

**Beschreibung**: Ankerkette scheuert an der Bugkante, am Rumpf oder an
der Ankerklüse und verursacht Schäden am Gelcoat/Laminat.

**Ursache**:
- Bugrolle nicht richtig ausgerichtet (Kette läuft seitlich)
- Klüsenkante zu scharfkantig (kein Radius)
- Kette zu lang für Bugrolle (hängt seitlich durch)
- Schwojen bei Wind verursacht seitlichen Kettenzug
- Fehlende Kettenführung zwischen Winde und Bugrolle

**Bewertung**: MITTEL — Ästhetischer Schaden zunächst, bei Dauer
strukturelle Schäden am Laminat möglich.

**Maßnahme**:
- Bugrolle nachjustieren oder größere Rolle montieren
- Klüsenkante verrunden (Schleifen, Edelstahl-Einfassung)
- Kettenführung nachrüsten (Edelstahl-Leitschienen)
- Scheuerschutz am Rumpf anbringen (Edelstahl-Leiste oder GFK-Aufdopplung)

**Confidence**: `visual_high` (Scheuerspuren am Bug gut erkennbar)

---

### Fehlerbild F-17_04-11: Verstopfte Ankerkastenentwässerung

**Beschreibung**: Ankerkasten steht unter Wasser, weil die Entwässerung
verstopft ist.

**Ursache**:
- Ablauflöcher durch Schlick, Sand, Algen verstopft
- Ablaufschlauch geknickt oder durch Algen zugewachsen
- Rückschlagventil verklemmt
- Keine Entwässerung vorgesehen (Konstruktionsfehler)

**Bewertung**: MITTEL — Stehendes Wasser fördert Kettenkorrosion,
Geruchsbildung, bei viel Wasser Trimmprobleme.

**Maßnahme**:
- Ablauflöcher reinigen (Draht, Bürste)
- Ablaufschlauch durchspülen
- Rückschlagventil prüfen und ggf. tauschen
- Bei fehlendem Ablauf: Nachrüsten (Bohren + Borddurchlass)
- Regelmäßig: Bei jedem Ankerlichten den Kasten inspizieren

**Confidence**: `visual_medium` (Wasser im Kasten erkennbar, Ursache
erfordert Inspektion)

---

### Fehlerbild F-17_04-12: Ankerkettenmarkierung unleserlich

**Beschreibung**: Kettenmarkierung (Farbe, Kabelbinder) ist abgescheuert,
verblasst oder verloren gegangen. Kettenlänge kann nicht mehr abgelesen werden.

**Ursache**:
- Normale Abnutzung (Reibung über Bugrolle, Kettennuss)
- UV-Zerfall (bei Kabelbindern)
- Falsche Farbe verwendet (nicht Epoxid-basiert)
- Kabelbinder nicht UV-stabilisiert

**Bewertung**: NIEDRIG — Keine unmittelbare Gefahr, aber erschwertes
Ankermanöver (Schwoikreis-Berechnung ungenau).

**Maßnahme**:
- Kettenmarkierung erneuern (alle 1–2 Saisons)
- Epoxid-basierte Markierungsfarbe verwenden
- UV-stabilisierte Kabelbinder Breite 4,8 mm
- Elektronischen Kettenzähler als Backup verwenden
- Kette einmal vollständig ausfahren und komplett neu markieren

**Confidence**: `visual_high` (Vorhandene/fehlende Markierung auf Fotos
erkennbar)

---

## 14. Troubleshooting

### 14.1 Entscheidungsbaum: Ankerwirbel-Probleme

```
PROBLEM: Ankerwirbel funktioniert nicht korrekt
│
├── Dreht sich nicht?
│   ├── Salzverkrustung? → Süßwasser einweichen, WD-40, manuell lockern
│   ├── Korrosion im Lager? → Oxalsäure-Behandlung, wenn schwer → Austausch
│   ├── Sand/Schlick im Mechanismus? → Zerlegen, reinigen, fetten
│   └── Mechanische Verformung? → Sofortiger Austausch
│
├── Dreht sich, aber rau/schwergängig?
│   ├── Kugellager-Wirbel? → Lager reinigen und neu fetten
│   ├── Gleitlager-Wirbel? → Lagerflächen reinigen, ggf. polieren
│   └── Verformung? → Spiel messen, bei >0,5 mm Schlag: Austausch
│
├── Bolzen locker?
│   ├── Sicherungsdraht vorhanden? → Draht erneuern, Bolzen nachziehen
│   ├── Gewinde verschlissen? → Neuen Bolzen beschaffen
│   └── Kein Sicherungsdraht? → Sicherungsdraht montieren!
│
└── Sichtbare Korrosion?
    ├── Oberflächlich (Verfärbung)? → Reinigen, beobachten
    ├── Lochfraß? → Sofortiger Austausch
    └── Rissbildung? → Sofortiger Austausch, Bruchgefahr!
```

### 14.2 Entscheidungsbaum: Bugrolle quietscht oder klemmt

```
PROBLEM: Bugrolle dreht sich nicht frei
│
├── Kette verklemmt?
│   ├── Kettenglied verkantet? → Manuell ausrichten
│   ├── Kette zu groß für Rolle? → Rollengröße prüfen
│   └── Wirbel/Schäkel zu breit? → Anderen Wirbel wählen
│
├── Rolle dreht nicht?
│   ├── Achse festgerostet? → Achse lösen, reinigen, fetten
│   ├── Rolle gebrochen? → Rolle ersetzen (Nylon/HDPE)
│   ├── Salzverkrustung? → Süßwasser, WD-40
│   └── Buchse verschlissen? → Buchse ersetzen
│
├── Quietschen?
│   ├── Trockene Achse? → Mit marine Fett schmieren
│   ├── Korrosion? → Achse polieren, Ursache beheben
│   └── Nylon-Rolle deformiert? → Rolle ersetzen
│
└── Kette springt aus Rolle?
    ├── Wangen zu niedrig? → Größere Bugrolle oder Wangenerhöhung
    ├── Seitlicher Kettenzug? → Kettenführung nachrüsten
    └── Falsche Rollengröße? → Passende Rolle für Kette wählen
```

### 14.3 Entscheidungsbaum: Kettenstopper-Probleme

```
PROBLEM: Kettenstopper funktioniert nicht
│
├── Kette rutscht durch?
│   ├── Falsche Kettengröße? → Stopper für richtige Kette beschaffen
│   ├── Hebel verschlissen? → Hebel/Klemmbacke erneuern
│   ├── Korrosion an Klemmfläche? → Reinigen, bei starker Korrosion tauschen
│   └── Kette verkantet eingelegt? → Kette korrekt in Stopper führen
│
├── Hebel lässt sich nicht umlegen?
│   ├── Korrosion? → WD-40, Reinigung, Schmierung
│   ├── Verformung? → Austausch des Hebels
│   └── Kette im Weg? → Kette etwas fieren, dann Hebel betätigen
│
├── Stopper bricht?
│   ├── Unterdimensioniert? → Größeren Stopper montieren
│   ├── Korrosionsschaden? → Material prüfen (muss 316L sein)
│   ├── Keine Reiterleine verwendet? → Reiterleine nachrüsten
│   └── Befestigung gerissen? → Gegenplatte und Befestigung prüfen
│
└── Befestigung locker?
    ├── Bolzen gelockert? → Nachziehen mit korrektem Drehmoment
    ├── Gegenplatte fehlt? → Gegenplatte nachrüsten
    └── Deck ausgefranst? → Deck reparieren, neu unterfüttern
```

### 14.4 Entscheidungsbaum: Ankerkasten-Probleme

```
PROBLEM: Probleme mit dem Ankerkasten
│
├── Wasser im Kasten?
│   ├── Ablauf verstopft? → Reinigen, durchspülen
│   ├── Kein Ablauf vorhanden? → Nachrüsten
│   ├── Klüsendeckel undicht? → Dichtung erneuern oder Deckel tauschen
│   └── Riss im Laminat? → Epoxid-Reparatur
│
├── Geruch aus dem Kasten?
│   ├── Schlick/Algen in Kette? → Kette vor Einziehen spülen
│   ├── Stehendes Wasser? → Ablauf prüfen
│   └── Keine Belüftung? → Lüftungsöffnungen nachrüsten
│
├── Kette verhakt im Kasten?
│   ├── Kastenform ungünstig? → Kettenleitung (PVC-Rohr) einbauen
│   ├── Kette fällt falsch? → Kettenfall-Position optimieren
│   └── Kette zu lang für Kasten? → Kettenvolumen berechnen
│
└── Luke undicht?
    ├── Dichtung verschlissen? → Neue Dichtung (Neoprene, EPDM)
    ├── Luke verformt? → Luke richten oder ersetzen
    └── Scharniere defekt? → Scharniere tauschen
```

### 14.5 Entscheidungsbaum: Ankerbergung bei verklemmtem Anker

```
PROBLEM: Anker sitzt fest und lässt sich nicht lichten
│
├── Tripleine vorhanden?
│   ├── Ja → An Tripleine ziehen (Anker wird umgedreht)
│   │   ├── Anker löst sich? → Erfolg. Tripleine war richtig dimensioniert
│   │   └── Auch über Tripleine fest? → Taucher beauftragen
│   │
│   └── Nein (keine Tripleine)
│       ├── Motor vorwärts über Ankerposition fahren
│       │   ├── Kette straff von vorne → Fieren + Motor rückwärts
│       │   └── Verschiedene Richtungen versuchen (360°)
│       │
│       ├── Kette auf Klampe belegen, mit Motorkraft ziehen?
│       │   ├── Achtung: Max. Klampenlast beachten!
│       │   └── Rucklast vermeiden (Wellenhub nutzen)
│       │
│       └── Anker aufgeben?
│           ├── Kette an Boje befestigen → Später bergen
│           └── Kette slipppen (Soll-Bruchstelle → Kette geht verloren)
```

---

## 15. FAQ

### 15.1 Ankerwirbel

**F-01: Brauche ich unbedingt einen Ankerwirbel?**
Ja, bei Kettenbetrieb ist ein Wirbel dringend empfohlen. Ohne Wirbel dreht
sich die gesamte Kette beim Schwojen, was zu Verknäulung im Kettenkasten
und erschwertem Ankerlichten führt. Einzige Ausnahme: Reine Leinengeschirre
(dort ist der Wirbel in der Leinen-Drehung integriert).

**F-02: Welcher Wirbel passt zu meinem Anker?**
Der Wirbel muss zur Kettengröße passen, nicht zum Ankertyp. Wählen Sie einen
Wirbel mit gleicher oder höherer WLL als Ihre Kette. Die Gabelweite muss das
Kettenglied aufnehmen können.

**F-03: Mantus oder Wichard — welcher Wirbel ist besser?**
Beide Hersteller produzieren hochwertige Wirbel aus 316L-Edelstahl. Mantus
bietet ein gutes Preis-Leistungs-Verhältnis, Wichard hat die höheren
Bruchlasten und die längere Garantie (25 Jahre). Für Blauwasser-Yachten
empfehlen wir Wichard HR oder Ultra Swivel.

**F-04: Wie oft muss ich den Wirbel warten?**
Sichtprüfung vor jeder Ankermanöver. Drehtest monatlich. Gründliche
Reinigung und Prüfung jährlich. Kugellager-Wirbel alle 2 Jahre fetten.

**F-05: Kann ich einen verzinkten Wirbel verwenden?**
Nicht empfohlen. Verzinkung hält im Salzwasser nur 2–4 Jahre, danach
korrodiert der Stahl rapide. Außerdem verursacht Zink an Edelstahlkette
galvanische Korrosion. Investieren Sie in 316L.

### 15.2 Ankerschäkel

**F-06: Wie sichere ich den Schäkelbolzen richtig?**
Mit 316L-Sicherungsdraht (0,8–1,2 mm), 3–4 Windungen durch das Bolzenloch,
Enden verdrillen und umbiegen. Alternativ: Wichard Self-Locking-Schäkel
verwenden. NICHT: Kabelbinder, Klebeband, Kupferdraht.

**F-07: D-Schäkel oder Bügelschäkel für den Anker?**
Immer Bügelschäkel (Bow Shackle) für Ankerverbindungen. Die breitere Form
erlaubt dem Ankerschaft mehr Bewegungsfreiheit und verteilt die Last besser.

**F-08: Welche Schäkelgröße brauche ich?**
Mindestens Kettendurchmesser + 2 mm, empfohlen + 4 mm. Beispiel: Bei 10 mm
Kette → 12 mm Schäkel (Minimum) oder 14 mm (empfohlen). Die Innenweite
muss das Kettenglied aufnehmen.

**F-09: Wie erkenne ich 316L vs. 304 Edelstahl?**
316L ist weniger magnetisch als 304. Halten Sie einen starken Magneten an
den Schäkel. Wenn er deutlich angezogen wird → wahrscheinlich 304 oder
sogar gewöhnlicher Stahl. 316L zeigt keine oder minimale Magnetanziehung.
Zusätzlich: Gravur prüfen (316L, A4, AISI 316L).

**F-10: Muss der Schäkel die gleiche Bruchlast wie die Kette haben?**
Ja, mindestens. Jedes Glied der Ankergeschirr-Kette (im übertragenen Sinne)
muss mindestens die Bruchlast der Ankerkette haben. Ein unterdimensionierter
Schäkel ist die häufigste Schwachstelle.

### 15.3 Kettenvorläufer und gemischtes Geschirr

**F-11: Kette oder Leine — was ist besser?**
Beide haben Vor- und Nachteile. Kette: Höheres Gewicht (besserer Kettenbogen,
geringerer Zug am Anker), scheuer- und UV-beständig. Leine: Leichter (weniger
Vorschiffslast), elastisch (Stoßdämpfer-Effekt), günstiger. Die Kombination
(Kette + Leine) vereint die Vorteile beider Systeme.

**F-12: Wie lang muss der Kettenvorläufer sein?**
Für ein gemischtes Geschirr: Mindestens 10 m Kette. Empfohlen: 15–25 m für
Fahrtenyachten, 20–40 m für Blauwasser. Die Kette muss lang genug sein,
damit sie bei normaler Schwoikreis-Berechnung auf dem Grund liegt (Gewicht!).

**F-13: Kann ich die Kette direkt an die Leine spleißen?**
Ja, das ist sogar die beste Verbindungsmethode. Ein fachmännisch ausgeführter
Spleiss direkt in das letzte Kettenglied hält 80–90% der Leinenbruchlast
und läuft sauber über die Bugrolle. Lassen Sie den Spleiss von einem
Tauwerk-Fachmann anfertigen (Kosten: ca. 30–50 EUR).

### 15.4 Ankerbojen und Triplinen

**F-14: Wann brauche ich eine Tripleine?**
Immer bei unbekanntem Ankergrund, bei Verdacht auf Felsen, Korallen, Kabel
oder Wrackteile. In gut bekannten Sandgründen kann darauf verzichtet werden,
empfohlen ist sie jedoch immer.

**F-15: Welches Material für die Tripleine?**
Schwimmfähiges Polypropylen (PP) ist ideal, da die Leine nicht auf den Grund
sinkt und sich nicht verhaken kann. Durchmesser: 6–10 mm für Fahrtenyachten,
10–14 mm für Blauwasser-Yachten.

**F-16: Muss ich einen Ankerball führen?**
Ja, gemäß KVR Regel 30 ist ein schwarzer Ball (∅ ≥ 300 mm) bei Tag und ein
weißes Rundumlicht bei Nacht Pflicht für ankernde Fahrzeuge. Verstöße können
mit Bußgeld geahndet werden. Wichtiger als das Bußgeld: Ihre Sicherheit,
wenn andere Schiffe Sie als Ankerlieger erkennen.

### 15.5 Ankerrollen und Bugbeschläge

**F-17: Meine Bugrolle ist zu klein für meinen neuen Anker. Was tun?**
Eine unterdimensionierte Bugrolle ist ein Sicherheitsrisiko. Tauschen Sie
die Bugrolle gegen eine passende Größe aus. Die Wangenhöhe muss den
Ankerschaft sicher halten, die Rollenbreite muss zur Kette passen.
Vergessen Sie nicht die Decksverstärkung für die neue Bugrolle.

**F-18: Kann ich eine Aluminium-Bugrolle verwenden?**
Aluminium ist leichter, aber anfälliger für galvanische Korrosion in
Kontakt mit Edelstahlkette. Nur mit galvanischer Isolation (Nylon-Buchsen)
verwenden. Für Salzwasser ist 316L vorzuziehen.

**F-19: Wie befestige ich eine Bugrolle auf einem GFK-Deck?**
Durchgehende Bolzen (M8 bis M12 je nach Bootsgröße) mit Unterdeck-Gegenplatte
aus 316L-Edelstahl (3–6 mm). Decksverstärkung durch Aufdopplung oder Holzkern.
Abdichtung mit Sikaflex 291i. Niemals nur Schrauben ins GFK drehen!

### 15.6 Kettenstopper

**F-20: Brauche ich einen Kettenstopper, wenn ich eine elektrische Winde habe?**
Unbedingt ja! Die Ankerwinch ist NICHT als Dauerhaltung der Ankerlast
ausgelegt. Ohne Kettenstopper ruht die gesamte Last auf dem Windengetriebe,
was zu vorzeitigem Verschleiß führt. Im schlimmsten Fall versagt das
Getriebe und die Kette rauscht unkontrolliert aus.

**F-21: Kettenstopper oder Devil's Claw — was ist besser?**
Der Hebelkettenstopper ist komfortabler (ein Handgriff). Die Devil's Claw
ist robuster und günstiger, aber umständlicher zu bedienen, besonders unter
Last. Für Blauwasser-Yachten: Beides an Bord haben (Redundanz!).

**F-22: Muss ich zusätzlich zum Kettenstopper eine Reiterleine verwenden?**
Dringend empfohlen. Die Reiterleine (Nylon-Snubber) übernimmt die Rucklasten
beim Schwojen und entlastet den Kettenstopper. Außerdem reduziert sie
Kettengeräusche an der Klüse erheblich — nachts in einer ruhigen Bucht
ein bedeutender Komfortgewinn.

### 15.7 Ankermarkierung

**F-23: Muss ich meine Ankerkette markieren?**
Keine gesetzliche Pflicht, aber dringend empfohlen. Ohne Markierung wissen
Sie nicht, wie viel Kette ausgebracht ist. Der Schwoikreis lässt sich nicht
berechnen, das Ankermanöver wird unsicher. Markierung kostet 20 Minuten
und ein paar Kabelbinder oder Sprühfarbe.

**F-24: Farb- oder Kabelbinder-Markierung?**
Beide Methoden haben Vor- und Nachteile. Kabelbinder: Einfacher anzubringen,
schnell erneuert, aber UV-empfindlich. Sprühfarbe: Haltbarer (mit Epoxid-
Basis), besser sichtbar, aber aufwändiger aufzutragen. Ideal: Kombination
aus beidem (Kabelbinder UND Farbmarkierung).

**F-25: Soll ich das Kettenende fest im Boot sichern?**
NEIN! Das Kettenende muss über eine Soll-Bruchstelle oder Schnellauslösung
verfügen. Im Notfall (Sturmankern, Schiff in Gefahr) müssen Sie die Kette
slipppen können. Eine fest montierte Kette kann das Boot nach unten ziehen.
Empfehlung: 3× Kabelbinder 7,6 mm oder Dyneema-Lashing als Soll-Bruchstelle.

**F-26: Was ist ein Reitgewicht (Kellet)?**
Ein Gewicht (5–15 kg), das an der Ankerkette herabgelassen wird (ca. 1/3
der Kettenlänge vom Bug). Es flacht den Kettenbogen ab und erhöht die
Haltekraft des Ankers bei wenig Kette. Nützlich bei begrenztem Schwoikreis
(enger Hafen, Mangrovenbucht).

**F-27: Wie berechne ich den Schwoikreis?**
Schwoikreis-Radius = Kettenlänge + Bootslänge. Bei Kette/Leine-Kombination:
Der effektive Radius ist geringer, da die Leine weniger auf dem Grund liegt.
Faustformel: Radius ≈ 0,8 × Gesamtlänge Kette+Leine + Bootslänge.

**F-28: Wie viel Kette muss ich ausbringen?**
Faustformel für Kette: 5× Wassertiefe bei ruhigem Wetter, 7× bei
mäßigem Wind, 10× bei Starkwind. Bei gemischtem Geschirr: Gesamtlänge
(Kette+Leine) × gleiche Faktoren. Bei Sturmankern: So viel wie möglich.

### 15.8 Allgemeine Fragen

**F-29: Was kostet ein komplettes Ankergeschirr?**
Abhängig von Bootsgröße und Qualitätsanspruch:

| Bootsklasse | Budget (EUR) | Standard (EUR) | Premium (EUR) |
|-------------|-------------|---------------|---------------|
| Kleinkreuzer 6–8 m | 200–400 | 400–800 | 800–1.500 |
| Fahrtenyacht 8–12 m | 400–800 | 800–1.500 | 1.500–3.000 |
| Blauwasser 10–15 m | 800–1.500 | 1.500–3.000 | 3.000–6.000 |
| Performance 12–18 m | 1.000–2.000 | 2.000–4.000 | 4.000–8.000 |

(Ohne Anker, Kette und Winde — nur Beschläge und Zubehör.)

**F-30: Wie überprüfe ich mein Ankergeschirr vor der Saison?**
Checkliste Saison-Check Ankergeschirr:
1. Wirbel: Drehgängigkeit prüfen, Bolzen kontrollieren, Korrosion?
2. Schäkel: Bolzensitz prüfen, Sicherungsdraht intakt?
3. Bugrolle: Drehgängigkeit, Achse, Wangen, Befestigung
4. Kettenstopper: Funktion, Hebelmechanismus, Befestigung
5. Kette: Markierung vorhanden? Korrosion? Glieder intakt?
6. Ankerlicht: Funktion testen
7. Ankerball: Vorhanden und griffbereit?
8. Ankerkasten: Entwässerung, Belüftung, Dichtung der Luke
9. Reiterleine: Zustand, Scheuerstellen, Schäkel
10. Tripleine: Vorhanden, Zustand, Boje aufblasbar?

### 15.9 Wartung und Pflege

**F-31: Wie reinige ich Edelstahl-Beschläge richtig?**
Süßwasser-Spülung nach jedem Salzwasser-Einsatz. Für hartnäckige Flecken:
Oxalsäure-Reiniger (z.B. BarKeepers Friend). Für Politur: Marine-Edelstahl-
Politur (z.B. Flitz, Star brite). NICHT: Stahlwolle (hinterlässt Partikel
die rosten), chlorhaltige Reiniger (greifen Passivschicht an).

**F-32: Kann ich rostende Edelstahlbeschläge retten?**
Oberflächlicher „Flugrost" (von Stahlpartikeln in der Umgebung) lässt sich
mit Oxalsäure oder Zitronensäure entfernen. Echter Lochfraß im 316L
deutet auf Materialfehler oder extremen Chlorid-Kontakt hin. Bei
Lochfraß an tragenden Teilen: Sofort austauschen, nicht reparierbar.

**F-33: Wie lagere ich Ankergeschirr-Teile über den Winter?**
Alle Beschläge gründlich mit Süßwasser reinigen und trocknen. Wirbel
und Schäkel mit dünnem Ölfilm (Ballistol oder WD-40 Long-Term) konservieren.
Nylon-Leinen trocken und dunkel lagern (UV!). Kette im Ankerkasten
belassen, Kasten gut belüften. Ankerlicht-Batterien entnehmen.

**F-34: Welches Fett/Öl für Ankerwirbel-Kugellager?**
Marine-Fett auf Lithium-Basis oder synthetisches Marine-Fett.
Empfehlungen: Lewmar Winch Grease, Harken Pawl Oil + Winch Grease,
Tef-Gel (PTFE-basiert für Anti-Seize). NICHT: Haushaltsfett, WD-40
allein (verdampft), Kupferpaste (galvanische Probleme).

**F-35: Wie oft muss ich Sicherungsdraht erneuern?**
Bei jeder Demontage des Schäkels neuen Draht verwenden. Zusätzlich:
Jährliche Sichtkontrolle. Draht erneuern, wenn er knickt, bricht oder
Korrosionsspuren zeigt. Ein Satz Sicherungsdraht (316L, 1 mm × 10 m)
kostet etwa 5 EUR — am Material sollte hier nicht gespart werden.

### 15.10 Spezialfragen

**F-36: Wie ankere ich auf Felsgrund?**
Bügelanker (Rocna, Mantus, Ultra) eignen sich schlecht für Fels. Fortress
(Aluminium, flache Fluken) kann in Felsspalten greifen. Empfehlung:
Immer Tripleine verwenden! Alternativ: Anker mit Kette über Felskante
legen (Kette verhakt am Felsen). Reiterleine unbedingt verwenden.

**F-37: Was ist eine Ankerkette mit Wirbeln in der Kette?**
Manche Hersteller bieten Ketten mit integrierten Wirbelgliedern alle
15–25 m an. Dies reduziert Torque-Aufbau in langen Ketten. Nachteil:
Wirbelglieder sind potentielle Schwachstellen und laufen nicht durch
die Kettennuss der Winde. Empfehlung: Nur am Anker einen Wirbel verwenden.

**F-38: Wie erkenne ich eine kalibrierte Kette?**
Kalibrierte Ketten (DIN 766, ISO 4565) haben exakte Gliedmaße, die in
die Kettennuss der Ankerwinch passen. Erkennbar an: Gleichmäßige Gliedform,
keine sichtbaren Gussnähte, Stempel „DIN 766" oder Herstellerprägung.
Unkalibrierte Ketten (DIN 763, DIN 764) haben andere Gliedmaße und passen
NICHT in die Kettennuss.

**F-39: Kann ich Kette und Beschläge unterschiedlicher Hersteller kombinieren?**
Ja, solange alle Teile zur gleichen Norm passen (DIN 766 für Kette, ISO für
Schäkelmaße). Die Materialkompatibilität beachten (alle 316L oder alle
verzinkt, nicht mischen). Probleme treten auf bei: Exotischen Kettenmaßen
(z.B. US-Standard 3/8" ≠ 10 mm ISO), Wirbeln die nicht über die Bugrolle
passen, Schäkeln deren Innenweite nicht zum Kettenglied passt.

**F-40: Was kostet eine professionelle Ankergeschirr-Inspektion?**
Eine Fachinspektion durch einen Bootsbau-Sachverständigen oder eine
AYDI-Analyse kostet je nach Umfang:
- Sichtprüfung Ankergeschirr: 80–150 EUR
- Detailprüfung inkl. Maßaufnahme: 150–300 EUR
- Vollinspektion inkl. Unterwasser und Protokoll: 300–600 EUR
- AYDI-Analyse (visuell + strukturell): abhängig vom Paket

**F-41: Brauche ich einen Zweitanker?**
Für Küstenfahrt: Empfohlen, aber nicht zwingend. Für Blauwasser: Ja,
unbedingt. Der Zweitanker (oft ein leichter Fortress) dient als:
- Backup bei Hauptanker-Versagen
- Heckanker (Bahamian Moor, enge Buchten)
- Ergänzung bei Sturmankern (zwei Anker in V)
Montage: Am Heck, am Bugbeschlag (Doppelrolle), oder unter Deck (Fortress faltbar)

**F-42: Wie entsorge ich alte Ankerkette und Beschläge?**
Edelstahl-Beschläge und -ketten sind wertvoller Rohstoff. Beim Schrotthändler
erhalten Sie für 316L-Edelstahl 1,50–3,00 EUR/kg. Verzinkte Kette bringt
etwa 0,30–0,50 EUR/kg. Nylon-Leinen gehören in den Restmüll, nicht in
die gelbe Tonne (kein Verpackungsmaterial).

---

## 16. Glossar

| Nr. | Begriff (DE) | Begriff (EN) | Definition |
|-----|-------------|-------------|-----------|
| G-01 | Ankerball | Anchor ball / Day shape | Schwarzer Ball ∅ ≥ 300 mm als Tagsignal für ankernde Schiffe (KVR Regel 30) |
| G-02 | Ankerboje | Anchor buoy | Schwimmkörper, der die Position des Ankers markiert |
| G-03 | Ankergeschirr | Anchor tackle / Ground tackle | Gesamtheit aller Bauteile zwischen Anker und Boot |
| G-04 | Ankerkasten | Anchor locker / Chain locker | Stauraum für Ankerkette und Anker im Vorschiff |
| G-05 | Ankerklüse | Anchor hawse pipe | Durchführung für die Ankerkette durch Deck oder Bordwand |
| G-06 | Ankerlicht | Anchor light | Weißes Rundumlicht als Nachtsignal für ankernde Schiffe |
| G-07 | Ankermarkierung | Chain marking | Farbliche oder materielle Markierung der Ankerkette in definierten Abständen |
| G-08 | Ankerrolle | Bow roller / Anchor roller | Am Bug montierte Rolle zur Führung der Ankerkette |
| G-09 | Ankerschäkel | Anchor shackle | Bügelförmiges Verbindungselement für Kette, Wirbel, Anker |
| G-10 | Ankerwirbel | Anchor swivel | Drehgelenk zwischen Kette und Anker zur Verhinderung von Torque |
| G-11 | Bruchlast | Breaking load / MBL | Maximale Kraft bis zum Versagen des Bauteils |
| G-12 | Bugbeschlag | Bow fitting | Oberbegriff für alle Beschläge im Bugbereich |
| G-13 | Bugsprit | Bowsprit | Über den Bug hinausragendes Strukturelement |
| G-14 | Bügelschäkel | Bow shackle / Omega shackle | Schäkel mit bauchiger Omega-Form für höhere WLL |
| G-15 | D-Schäkel | Dee shackle | Schäkel mit schmaler D-Form |
| G-16 | Devil's Claw | Kettenkralle | Hakengabel, die in ein Kettenglied greift zur Kettensicherung |
| G-17 | Galvanische Korrosion | Galvanic corrosion | Korrosion durch elektrochemische Reaktion bei Kontakt verschiedener Metalle |
| G-18 | Kellet | Reitgewicht | Gewicht, das an der Ankerkette herabgelassen wird zur Verflachung des Kettenbogens |
| G-19 | Kettenbogen | Chain catenary | Durchhang der Ankerkette zwischen Bug und Grund |
| G-20 | Kettenführung | Chain guide | Leitschiene zur Führung der Kette zwischen Winde und Bugrolle |
| G-21 | Kettenkralle | Chain claw / Devil's claw | Haken zum Eingreifen in ein Kettenglied zur Sicherung |
| G-22 | Kettenkasten | Chain locker | Stauraum für die Ankerkette (Synonym für Ankerkasten) |
| G-23 | Kettennuss | Gypsy / Wildcat | Zahnrad der Ankerwinch, das in die kalibrierte Kette greift |
| G-24 | Kettenstopper | Chain stopper | Mechanischer Stopper, der die Kette arretiert und die Ankerlast von der Winde nimmt |
| G-25 | Kettenvorläufer | Chain leader | Kettenstück am Anfang eines Leinengeschirrs oder Kette-Leine-Verbindung |
| G-26 | Klampe | Cleat | Befestigungspunkt für Leinen auf dem Deck |
| G-27 | Klüse | Fairlead / Chock | Leinenführung durch Bordwand oder Schanzkleid |
| G-28 | Kugellager-Wirbel | Ball-bearing swivel | Ankerwirbel mit integriertem Kugellager für leichtgängige Drehung |
| G-29 | KVR | ColRegs | Kollisionsverhütungsregeln — internationales Regelwerk zur Verhütung von Zusammenstößen auf See |
| G-30 | Lochfraß | Pitting corrosion | Lokale Korrosionsform mit kleinen, tiefen Löchern im Material |
| G-31 | Reiterleine | Snubber / Bridle | Nylon-Leine als Stoßdämpfer zwischen Kette und Klampe |
| G-32 | Schwoikreis | Swinging circle | Kreisfläche, die ein ankerndes Boot beim Drehen um den Anker überstreicht |
| G-33 | Sicherungsdraht | Seizing wire | Dünner Edelstahldraht zur Sicherung von Schäkelbolzen |
| G-34 | Soll-Bruchstelle | Weak link | Definierte Schwachstelle am Kettenende, die bei Überlast bricht |
| G-35 | Spaltkorrosion | Crevice corrosion | Korrosion in engen Spalten (z.B. zwischen Bolzen und Schäkel) |
| G-36 | Torque | Torque / Verdrehung | Verdrehung der Ankerkette durch Strömung und Schwojen |
| G-37 | Tripleine | Trip line | Hilfsleine am Ankerkopf zum Freitrippen des Ankers |
| G-38 | WLL | Working Load Limit | Maximal zulässige Arbeitslast eines Bauteils (Bruchlast / Sicherheitsfaktor) |
| G-39 | 316L | AISI 316L / A4 | Molybdän-haltiger Edelstahl, Standard für marine Beschläge |
| G-40 | Duplex 2205 | Duplex 2205 | Hochfester Duplex-Edelstahl für anspruchsvolle marine Anwendungen |
| G-41 | Schwojen | Swinging at anchor | Drehen des Bootes um den Ankerpunkt durch Wind- und Strömungswechsel |
| G-42 | Ankertasche | Anchor bag | Transporttasche für Anker und Zubehör |
| G-43 | Passivierung | Passivation | Chemische Oberflächenbehandlung von Edelstahl zur Verbesserung der Korrosionsbeständigkeit |
| G-44 | Ankerkettenbremse | Chain brake | Fußpedal-betätigte Bremse zum kontrollierten Fieren der Ankerkette |

| G-45 | Kettenzähler | Chain counter | Elektronisches Gerät zur Messung der ausgebrachten Kettenlänge |
| G-46 | Bridle | Bridle | V-förmige Doppel-Reiterleine für Katamarane |
| G-47 | Ankerwiege | Anchor cradle | Geformte Aufnahme für den Anker am Bug |
| G-48 | Fluchtklüse | Flush fairlead | Bündig ins Deck eingelassene Klüse |
| G-49 | Bugsprit-Ankerkasten | Bowsprit locker | In den Bugsprit integrierter Ankerkasten |
| G-50 | Reitgewicht | Kellet / Sentinel | Gewicht auf der Ankerkette zur Verflachung des Kettenbogens |

---

## 17. Schnell-Referenz

### 17.1 Checkliste: Ankergeschirr zusammenstellen

```
□ Wirbel: WLL ≥ Ketten-WLL, Material 316L, passend zur Kettengröße
□ Schäkel: Bügelschäkel, Größe = Kette + 4 mm, 316L, Bolzen gesichert
□ Bugrolle: Passend zu Kette UND Anker, 316L Wangen, Unterdeck-Gegenplatte
□ Kettenstopper: WLL ≥ Ketten-WLL, passend zur Kettengröße
□ Reiterleine: Nylon 3-schäftig, Ø = Kette × 1,5, Länge = 3× Wassertiefe
□ Kettenmarkierung: Alle 5 oder 10 m, Farbsystem festlegen
□ Soll-Bruchstelle: Am Kettenende, 3× Kabelbinder 7,6 mm
□ Ankerlicht: LED, 2 sm Sichtweite, Funktion geprüft
□ Ankerball: ∅ ≥ 300 mm, griffbereit an Deck
□ Tripleine: PP schwimmfähig, passende Länge, mit Boje
□ Ankertasche/Ankerkasten: Entwässerung, Belüftung, ausreichendes Volumen
```

### 17.2 Dimensionierungstabelle nach Bootsklasse

| Parameter | 6–8 m | 8–12 m | 10–15 m | 12–18 m | 15–22 m | 20–40 m |
|-----------|-------|--------|---------|---------|---------|---------|
| Kette | 6 mm | 8 mm | 10 mm | 10–12 mm | 12–13 mm | 13–16 mm |
| Wirbel WLL (kg) | ≥800 | ≥1.500 | ≥2.500 | ≥3.000 | ≥4.000 | ≥6.000 |
| Schäkel | 8–10 mm | 10–12 mm | 12–14 mm | 14–16 mm | 16–19 mm | 19–22 mm |
| Reiterleine | 12 mm | 14 mm | 16 mm | 18 mm | 20 mm | 22 mm |
| Kettenstopper WLL (kg) | ≥1.200 | ≥2.000 | ≥3.000 | ≥4.000 | ≥5.500 | ≥8.000 |
| Bugrolle Achse (mm) | 12 | 14 | 16 | 18 | 20 | 22+ |
| Klüse Ø (mm) | ≥40 | ≥50 | ≥60 | ≥70 | ≥80 | ≥100 |
| Ankerlicht | LED 2 sm | LED 2 sm | LED 2 sm | LED 3 sm | LED 3 sm | LED 3 sm |

### 17.3 Preisübersicht Ankergeschirr komplett (Standard-Qualität)

| Komponente | 8–12 m Yacht | 10–15 m Yacht | 12–18 m Yacht |
|-----------|-------------|---------------|---------------|
| Wirbel (316L) | 109–149 € | 139–189 € | 179–289 € |
| Schäkel 2× (316L) | 50–80 € | 70–100 € | 100–140 € |
| Bugrolle (316L) | 189–289 € | 269–389 € | 389–849 € |
| Kettenstopper | 119–169 € | 159–229 € | 229–329 € |
| Reiterleine (Nylon) | 30–50 € | 40–70 € | 60–100 € |
| Kettenmarkierung | 10–20 € | 10–20 € | 10–20 € |
| Ankerlicht (LED) | 55–89 € | 55–89 € | 89–149 € |
| Ankerball | 8–15 € | 8–15 € | 15–25 € |
| Tripleine + Boje | 25–50 € | 35–65 € | 50–90 € |
| **Gesamt** | **595–911 €** | **785–1.166 €** | **1.121–1.991 €** |

### 17.4 Material-Verträglichkeitstabelle

| Material A | Material B | Kompatibel? | Risiko |
|-----------|-----------|------------|--------|
| 316L | 316L | ✓ Ja | Kein Risiko |
| 316L | 316 | ✓ Ja | Minimales Risiko |
| 316L | 304 | ⚠ Bedingt | Leichtes galvanisches Risiko |
| 316L | Verzinkt | ✗ Nein | Starke galvanische Korrosion am Zink |
| 316L | Aluminium | ✗ Nein | Aluminium korrodiert stark |
| 316L | Bronze/Messing | ⚠ Bedingt | Geringes Risiko, aber vermeidbar |
| 316L | Titan | ✓ Ja | Kein Risiko |
| Verzinkt | Verzinkt | ✓ Ja | Kein galv. Risiko (aber generell korrosionsanfällig) |
| Aluminium | Aluminium | ✓ Ja | Kein galv. Risiko (Marine-Alu verwenden) |
| Bronze | Bronze | ✓ Ja | Kein Risiko |

### 17.5 Wartungsplan Ankergeschirr

| Komponente | Vor jeder Fahrt | Monatlich | Saisonweise | Jährlich | Alle 3–5 Jahre |
|-----------|----------------|-----------|------------|----------|----------------|
| Wirbel | Sichtprüfung | Drehtest | Bolzenkontrolle | Verschleißmessung | Austausch prüfen |
| Schäkel | Bolzensitz prüfen | — | Sicherungsdraht | Maßprüfung | Austausch |
| Bugrolle | Sichtprüfung | — | Achse schmieren | Rolle prüfen | Achse prüfen |
| Kettenstopper | Funktion prüfen | — | Schmierung | Befestigung prüfen | Austausch prüfen |
| Kette | Sichtprüfung | — | Markierung prüfen | Verschleiß messen | Kette erneuern |
| Reiterleine | Sichtprüfung | — | Scheuerstellen | Austausch prüfen | Austausch |
| Ankerlicht | Funktion prüfen | — | Dichtung prüfen | Birne/LED prüfen | — |
| Ankerkasten | — | — | Entwässerung | Dichtung Luke | Laminat prüfen |
| Tripleine | Sichtprüfung | — | Zustand | Austausch prüfen | Austausch |
| Ankerball | Verfügbarkeit | — | Zustand | — | — |

### 17.6 Notfall-Checkliste: Anker hält nicht

```
1. □ Kette prüfen: Genug ausgebracht? (Faustformel: 5-7× Wassertiefe)
2. □ Mehr Kette fieren (bis 10× Wassertiefe)
3. □ Motor langsam achteraus: Anker einfahren lassen
4. □ Reiterleine ausbringen: Rucklasten dämpfen
5. □ Wenn weiter Drift: Motor gegen die Drift, Anker lichten
6. □ Neuen Ankerplatz suchen (beserer Grund, weniger Wind)
7. □ Anker prüfen: Kraut/Schlick an den Fluken? Reinigen!
8. □ Bei Dauer-Drift: Zweitanker ausbringen (V-Formation oder Tandem)
9. □ Wenn alles scheitert: Motor laufen lassen, Ankerwache verstärken
10. □ Notfall: Hafen anlaufen, wenn sicher erreichbar
```

### 17.7 Empfohlene Ersatzteile an Bord

| Komponente | Menge | Begründung |
|-----------|-------|-----------|
| Schäkel (passend) | 3 Stück | Universelles Verbindungselement |
| Sicherungsdraht 316L 1mm | 10 m | Für Bolzensicherung |
| Nylon-Leine (Ersatz-Reiterleine) | 15 m | Backup bei Scheuer-Bruch |
| Kabelbinder UV-beständig | 50 Stück | Markierung, Notfixierung |
| Sprühfarbe marine | 1 Dose | Kettenmarkierung erneuern |
| Federstecker 316L | 5 Stück | Für Achsen und Bolzen |
| WD-40 | 1 Dose | Lösung festsitzender Teile |
| Marine-Fett | 1 Tube | Kugellager, Achsen schmieren |
| Dyneema 3mm | 5 m | Notlashing, Soll-Bruchstelle |
| Ankerboje (aufblasbar) | 1 Stück | Tripleine/Markierung |

---

## 18. ANHANG A–H: Fallstudien

### ANHANG A: Fallstudie — Bavaria 40 Cruiser, Ankergeschirr-Upgrade

**Ausgangssituation:**
- Boot: Bavaria 40 Cruiser (12,35 m), Baujahr 2018
- Bestehendes Ankergeschirr: 50 m × 8 mm DIN 766, einfacher verzinkter Schäkel,
  kein Wirbel, kleine Bugrolle, kein Kettenstopper
- Problem: Kette verdreht sich regelmäßig, Schäkel korrodiert, Kette scheuert am Bug

**Analyse (AYDI):**
- Kette 8 mm für 8,5 t Displacement: Grenzwertig, besser 10 mm
- Verzinkter Schäkel: Inkompatibel mit Edelstahlkette → galvanische Korrosion
- Kein Wirbel: Torque-Problem, erklärt Kettenverknäulung
- Bugrolle unterdimensioniert: Wangen zu niedrig für Delta-Anker
- Kein Kettenstopper: Gesamte Last auf Lewmar V1 Winde → Getriebeverschleiß

**Upgrade-Empfehlung:**
1. Kette: 60 m × 10 mm DIN 766 (316L oder verzinkt G40) → 420 EUR
2. Wirbel: Mantus Swivel M1, 10 mm → 139 EUR
3. Schäkel: 2× Wichard HR Bow Shackle 12 mm → 98 EUR
4. Bugrolle: Lewmar Concept 3 → 289 EUR
5. Kettenstopper: Lewmar Chain Stopper 10–12 mm → 169 EUR
6. Reiterleine: Liros Nylon 16 mm × 12 m → 54 EUR
7. Kettenmarkierung: Kabelbinder-Set → 12 EUR

**Gesamtkosten Upgrade**: 1.181 EUR (Material) + ca. 300 EUR (Einbau wenn Werft)

**Ergebnis nach Upgrade:**
- Keine Kettenverknäulung mehr (Wirbel funktioniert)
- Kein Scheuern am Bug (passende Bugrolle)
- Winde entlastet (Kettenstopper übernimmt Dauerlast)
- Kettenlänge zuverlässig ablesbar (Markierung)
- AYDI-Score: 42/100 → 87/100

---

### ANHANG B: Fallstudie — Hallberg-Rassy 43, Blauwassertauglich machen

**Ausgangssituation:**
- Boot: Hallberg-Rassy 43 MkII (13,28 m), Baujahr 2020
- Geplant: Atlantik-Überquerung und Karibik-Saison
- Bestehendes Geschirr: 80 m × 10 mm, Rocna 25 kg, Ultra Swivel, Lewmar V3 Winde

**Analyse (AYDI):**
- Grundausstattung gut (HR-Standard)
- Kein Kettenstopper montiert (Werftauslieferung ohne!)
- Keine Reiterleine → Rucklast auf Winde bei Karibik-Squalls
- Ankerball fehlt in der Ausstattung
- Tripleine nicht vorhanden (in Korallengebieten essenziell!)
- Kettenende fest mit Kettenkastenbolzen verschraubt → keine Soll-Bruchstelle

**Blauwasser-Ergänzung:**
1. Kettenstopper: Maxwell Chain Stopper 10–13 mm → 159 EUR
2. Reiterleine: Gleistein Nylon 18 mm × 15 m + Mantus Chain Hook → 176 EUR
3. Tripleine: PP 10 mm × 40 m + Plastimo Anchor Buoy 30l → 62 EUR
4. Ankerball: Plastimo faltbar → 8 EUR
5. Ankerlicht: Hella Marine NaviLED 360 Pro (Backup) → 89 EUR
6. Soll-Bruchstelle: Dyneema-Lashing 3 mm → 5 EUR
7. Zweitanker: Fortress FX-37 (Heckmontage) + Ankertasche → 580 EUR
8. Kettenmarkierung erneuern: Epoxid-Farbe → 25 EUR

**Gesamtkosten**: 1.104 EUR

**Ergebnis:**
- Vollständig blauwassertaugliches Ankergeschirr
- Redundanz durch Zweitanker
- Rucklasten gedämpft (Reiterleine)
- Tripleine für Korallengebiete vorhanden
- AYDI-Score: 71/100 → 95/100

---

### ANHANG C: Fallstudie — Jeanneau Sun Odyssey 349, Charterboot-Probleme

**Ausgangssituation:**
- Boot: Jeanneau SO 349 (10,34 m), Baujahr 2019, Charterbetrieb
- Meldung: „Anker hält nicht", „Kette ist immer verdreht", „Bugrolle quietscht"
- Letzte Wartung des Ankergeschirrs: Nie (4 Jahre Charterbetrieb!)

**Inspektion (AYDI visuell + Servicebericht):**
- Wirbel: Blockiert (Salzverkrustung, kein Fett seit 4 Jahren)
- Schäkel: Bolzen locker, kein Sicherungsdraht, Gewinde verschlissen
- Bugrolle: Nylon-Rolle verschlissen, Achse korrodiert → quietscht
- Kette: 40 m × 8 mm, keine Markierung, Endglied direkt am Boot verschraubt
- Delta-Anker: 10 kg — unterdimensioniert für das Boot
- Kein Kettenstopper, keine Reiterleine

**Befunde:**
- F-17_04-02 (Blockierter Wirbel): Confidence `visual_high`
- F-17_04-05 (Schäkelbolzen gelöst): Confidence `visual_high`
- F-17_04-10 (Kette scheuert am Bug): Confidence `visual_high`
- F-17_04-12 (Markierung unleserlich): Confidence `visual_high`

**Instandsetzung:**
1. Neuer Wirbel: Kong Anchor Swivel 8 mm → 99 EUR
2. Neue Schäkel: 2× Kong 10 mm + Sicherungsdraht → 63 EUR
3. Neue Bugrolle-Rolle + Achse: Lewmar Ersatzteil → 45 EUR
4. Kettenmarkierung: Kabelbinder-Set → 12 EUR
5. Soll-Bruchstelle: 3× Kabelbinder 7,6 mm → 2 EUR
6. Anker-Upgrade: Rocna 15 kg (besser für Charterbetrieb) → 350 EUR

**Gesamtkosten**: 571 EUR

**Empfehlung an Charterbasis:**
- Ankergeschirr in den jährlichen Wartungsplan aufnehmen
- Crew-Briefing: Wirbel nach Salzwasser spülen
- AYDI-Score: 28/100 → 72/100

---

### ANHANG D: Fallstudie — Catana 47, Katamaran-Doppelbugrolle

**Ausgangssituation:**
- Boot: Catana 47 (14,02 m), Baujahr 2016
- Problem: Zwei Buganker gewünscht (Bahamas-Revision), aber nur eine Bugrolle
- Breiteres Vorschiff als Monohull → Mehr Platz, andere Anforderungen

**Analyse:**
- Katamarane haben zwei Bugoptionen: Einzelrolle mittig (Standard) oder
  Doppelrolle an beiden Rümpfen
- Bei Einzelrolle: Zweitanker über separate Bugrolle an zweitem Rumpf
- Lasteinleitung: Katamaran-Bugstruktur oft leichter gebaut als Monohull

**Lösung:**
1. Bestehende Mittel-Bugrolle beibehalten (Hauptanker Rocna 25 kg)
2. Zweite Bugrolle an BB-Rumpf: Maxwell Twin Roller 10–13 mm → 529 EUR
3. Decksverstärkung BB-Rumpf: GFK-Aufdopplung + Gegenplatte → 150 EUR
4. Zweitanker: Mantus M1 16 kg → 420 EUR
5. Zweite Kette: 30 m × 10 mm → 180 EUR
6. Zweiter Wirbel: Ultra Swivel 10–12 mm → 189 EUR
7. Zweiter Kettenstopper: Kong Devil's Claw 10–12 mm → 85 EUR

**Gesamtkosten**: 1.553 EUR + 400 EUR Werft-Einbau

**Ergebnis:**
- Bahamian Moor möglich (zwei Anker in V-Form)
- Redundanz bei Einzelanker-Versagen
- AYDI-Score: 65/100 → 91/100

---

### ANHANG E: Fallstudie — Contest 42CS, Sturmankern Mittelmeer

**Ausgangssituation:**
- Boot: Contest 42CS (12,80 m), Baujahr 2014
- Szenario: Unvorhergesehener Meltemi (7–8 Bft) auf Ankerplatz in Griechenland
- Besatzung: 2 Personen
- Ankergeschirr: 80 m × 10 mm, Spade 20 kg, Wichard HR Swivel, Lewmar V3

**Chronologie:**
1. 14:00 — Ankern in Lee einer Insel, 6 m Wassertiefe, 50 m Kette, Wind 3 Bft
2. 18:00 — Wind dreht auf NW, zunimmt auf 5 Bft
3. 22:00 — Meltemi setzt ein, 7 Bft in Böen 8, Boot schwoijt stark
4. 22:15 — Kettengeräusche werden extrem laut (keine Reiterleine!)
5. 22:30 — Kette auf 70 m verlängert, Reiterleine improvisiert (Festmacherleine)
6. 01:00 — Böen bis 45 kn, Boot hält, Reiterleine scheuert an Klüse
7. 05:00 — Wind lässt nach auf 5 Bft, Reiterleine 50% durchgescheuert

**Lehren:**
- Reiterleine aus Nylon (nicht Polyester-Festmacher) verwenden → Elastizität!
- Scheuerschutz an der Klüse ist Pflicht
- Kettenstopper war korrekt eingesetzt → Winde blieb unbeschädigt
- 70 m bei 6 m Tiefe = Verhältnis 11,7:1 → Ausreichend für 7–8 Bft
- Wichard HR Swivel: Keine Probleme trotz extremer Belastung

**AYDI-Bewertung:**
- Ankergeschirr grundsätzlich gut dimensioniert
- Defizit: Keine dedizierte Reiterleine mit Scheuerschutz → F-17_04-06 (potentiell)
- Empfehlung: Dedizierte Nylon-Reiterleine 18 mm × 15 m mit Chafe Guard beschaffen

---

### ANHANG F: Fallstudie — Beneteau First 36.7, Regatta + Fahrtensegler

**Ausgangssituation:**
- Boot: Beneteau First 36.7 (10,90 m), Baujahr 2008
- Doppelnutzung: Regatta (Gewicht minimieren) und Sommerferien-Fahrt
- Problem: Schweres Ankergeschirr reduziert Regatta-Performance

**Analyse:**
- Standard-Ausrüstung: 50 m × 8 mm Kette (35 kg) + Delta 14 kg = 49 kg am Bug
- Für Regatta: Vorschiffslast verschlechtert Pitching und Amwind-Performance
- Für Fahrt: Vollständiges Ankergeschirr nötig

**Lösung: Modulares System:**
1. Regatta: Fortress FX-16 (3,2 kg) + 5 m × 6 mm Kette + 50 m Nylon 14 mm
   → Gesamtgewicht Vorschiff: 11 kg → Ersparnis 38 kg
2. Fahrt: Rocna 10 kg + 40 m × 8 mm + Kong Wirbel + Mantus Chain Hook
   → Gesamtgewicht Vorschiff: 45 kg
3. Schnellwechsel-System: Bugrolle bleibt, Kette/Anker tauschbar

**Kosten:**
- Fortress FX-16: 390 EUR
- Leichtkette 5 m × 6 mm: 25 EUR
- Nylon 14 mm × 50 m: 160 EUR
- Mantus Chain Hook für Schnellwechsel: 59 EUR
- Ankertasche für Fortress: 30 EUR

**Gesamtkosten**: 664 EUR

**AYDI-Score:**
- Regatta-Konfiguration: 55/100 (absichtlich minimiert)
- Fahrt-Konfiguration: 78/100 (gut, nicht Blauwasser)

---

### ANHANG G: Fallstudie — Superyacht Oyster 885, Premium-Ankergeschirr

**Ausgangssituation:**
- Boot: Oyster 885 (27,00 m), Baujahr 2022
- Anforderung: Vollständig blauwassertaugliches Premium-Ankergeschirr
- Budget: „Was nötig ist" (Eigneraussage)

**Spezifikation:**
- Hauptanker: Ultra Anchor 75 kg → 3.200 EUR
- Kette: 120 m × 14 mm DIN 766 (316L) → 4.800 EUR
- Wirbel: Wichard HR Swivel 16 mm → 379 EUR
- Schäkel: 3× Wichard Self-Locking 16 mm → 267 EUR
- Bugrolle: Custom-Anfertigung Antal, 316L + Bronze, Ankerwiege → 4.500 EUR
- Kettenstopper: 2× Lewmar Chain Stopper 14–16 mm → 658 EUR
- Reiterleine: Gleistein Nylon 22 mm × 20 m × 2 (Bridle) → 340 EUR
- Kettenzähler: Lewmar Premium → 289 EUR
- Ankerlicht: Aqua Signal Serie 43 LED → 149 EUR
- Ankerball: Rigides Modell → 25 EUR
- Zweitanker: Fortress FX-125 (30 kg, faltbar, Heckmontage) → 1.450 EUR
- Tripleine: Dyneema 12 mm × 50 m → 250 EUR
- Ankertasche für Fortress: Custom → 180 EUR

**Gesamtkosten**: 16.487 EUR (nur Geschirr-Zubehör, ohne Winde)

**AYDI-Score**: 97/100 (Premium, redundant, blauwassertauglich)

**Analyse-Details:**
- Hauptanker Ultra 75 kg: Überdimensioniert für Displacement (Sicherheit)
- 120 m × 14 mm Kette: Ermöglicht Ankern bis 20 m Wassertiefe mit 6:1 Verhältnis
- 316L-Kette statt verzinkt: Höhere Kosten, aber keine Korrosion über 20+ Jahre
- Wichard HR mit BV-Zertifizierung: Versicherungsrelevant bei Superyachten
- Zwei Kettenstopper: Redundanz bei Versagen eines Stoppers
- Fortress FX-125: Leichtester Zweitanker für diese Größenklasse, faltbar → verstaubar
- Bridle-Reiterleine (2× 22 mm): Für Katamarane und breite Superyachten
- Custom-Bugrolle Antal: Perfekt angepasst an Rumpfform und Ankertyp

**Wartungskosten (jährlich geschätzt):**
- Inspektion und Pflege: 200–400 EUR
- Verbrauchsmaterial (Draht, Fett): 50 EUR
- Anteilige Erneuerung (Reiterleine, Markierung): 100–200 EUR
- **Jährliche Gesamtkosten**: 350–650 EUR

---

### ANHANG H: Fallstudie — Hanse 315, Budget-Ankergeschirr

**Ausgangssituation:**
- Boot: Hanse 315 (9,45 m), Baujahr 2021, Küstenfahrt Ostsee/Nordsee
- Budget: Maximal 500 EUR für komplettes Ankergeschirr-Zubehör
- Vorhandene Ausrüstung: Bruce-Anker 7,5 kg (Werftausstattung), 30 m × 8 mm Kette

**Budget-Lösung:**
1. Wirbel: Kong Anchor Swivel 8 mm → 99 EUR
2. Schäkel: 2× Plastimo Standard 10 mm → 32 EUR
3. Kettenstopper: Osculati Schraube 6–10 mm → 68 EUR
4. Reiterleine: Liros Nylon 14 mm × 8 m → 26 EUR
5. Kettenmarkierung: Kabelbinder → 8 EUR
6. Ankerlicht: Lalizas FOS LED 360 → 29 EUR
7. Ankerball: Lalizas faltbar → 8 EUR
8. Sicherungsdraht: 316L 1 mm × 10 m → 5 EUR
9. Scheuerschutz: PVC-Schlauch 2 m → 6 EUR

**Gesamtkosten**: 281 EUR — unter Budget!

**Reservebudget-Empfehlung:**
- Anker-Upgrade: Bruce → Mantus M1 8 kg → 189 EUR (von verbleibendem Budget)

**AYDI-Score**: 61/100 (solide Basisausstattung für Küstenfahrt)

**Detailbewertung Budget-Lösung:**
| Komponente | Score | Kommentar |
|-----------|-------|----------|
| Wirbel (Kong 8mm) | 78/100 | Gute Qualität, passende Größe |
| Schäkel (Plastimo 10mm) | 62/100 | Feinguss statt geschmiedet, akzeptabel |
| Kettenstopper (Osculati) | 65/100 | Schraubtyp = langsamer, aber funktional |
| Reiterleine (Liros 14mm) | 70/100 | Ausreichend für Küstenfahrt |
| Markierung (Kabelbinder) | 55/100 | Grundfunktion, UV-empfindlich |
| Ankerlicht (Lalizas LED) | 72/100 | KVR-konform, geringe Sichtweite |
| Ankerball (Lalizas) | 80/100 | Erfüllt KVR-Anforderung |
| Bugrolle (vorhanden) | 60/100 | Werft-Standard, nicht geprüft |
| Gesamt | 61/100 | Solide Basis, Upgrade empfohlen |

**Verbesserungsvorschläge mit Budget-Priorität:**
1. Anker-Upgrade (Bruce → Mantus): +11 Score-Punkte → 72/100 (189 EUR)
2. Kettenstopper-Upgrade (Schraube → Hebel): +5 Score-Punkte (60 EUR Aufpreis)
3. Epoxid-Kettenmarkierung statt Kabelbinder: +3 Score-Punkte (15 EUR)
4. Tripleine nachrüsten: +4 Score-Punkte (25 EUR)

**Anmerkung**: Der Bruce-Anker ist nicht mehr zeitgemäß (geringe Haltekraft
pro kg im Vergleich zu modernen Bügelankern). Das Upgrade auf einen
Mantus M1 oder Rocna würde den Gesamt-Score auf 72/100 heben.

### ANHANG H.1: Lifecycle-Kostenvergleich über 10 Jahre

| Komponente | Budget (Hanse 315) | Standard (Bavaria 40) | Premium (Oyster 885) |
|-----------|-------------------|----------------------|---------------------|
| Erstinvestition | 281 € | 1.181 € | 16.487 € |
| Jährliche Wartung | 50 € | 120 € | 500 € |
| Austauschkosten (10 J.) | 200 € | 500 € | 2.000 € |
| **10-Jahres-Kosten** | **981 €** | **2.881 €** | **23.487 €** |
| Pro Jahr | 98 € | 288 € | 2.349 € |
| Pro Jahr / m LOA | 10,40 € | 23,30 € | 86,90 € |

**Erkenntnis**: Die Ankergeschirr-Kosten pro Meter LOA steigen überproportional
mit der Bootsgröße und dem Qualitätsanspruch. Ein Budget-Setup für einen
Kleinkreuzer kostet etwa 10 EUR pro Meter pro Jahr — im Vergleich zu
Liegegebühren, Versicherung und allgemeiner Wartung ein marginaler Betrag.

### ANHANG H.2: Gewichtsvergleich Ankergeschirr am Bug

Die Vorschiffslast beeinflusst Trimm und Segelverhalten:

| Boot | Anker (kg) | Kette (kg) | Beschläge (kg) | Gesamt (kg) | % Displacement |
|------|-----------|-----------|---------------|------------|----------------|
| Hanse 315 | 7,5 | 18 | 3 | 28,5 | 0,6% |
| Bavaria 40 | 15 | 42 | 5 | 62 | 0,7% |
| HR 43 | 25 | 55 | 8 | 88 | 0,7% |
| Catana 47 | 25+16 | 55+21 | 12 | 129 | 0,9% |
| Contest 42CS | 20 | 55 | 7 | 82 | 0,7% |
| Oyster 885 | 75+30 | 140 | 18 | 263 | 0,4% |

**AYDI-Grenzwerte für Vorschiffslast:**
- Segelyacht ≤ 12 m: Max. 1,0% des Displacements
- Segelyacht 12–18 m: Max. 0,8% des Displacements
- Motoryacht: Max. 1,5% des Displacements
- Regattayacht: Max. 0,5% des Displacements

Überschreitung führt zu:
- Erhöhtem Pitching im Seegang
- Verschlechtertem Amwind-Kurs (Segelyachten)
- Höherem Kraftstoffverbrauch (Motoryachten)
- Trimmveränderung (Bug-lastiger)

---

## 19. ANHANG I–R: Pydantic v2 Datenmodelle

### ANHANG I: Basismodelle

```python
"""
Pydantic v2 Datenmodelle für Ankergeschirr und Zubehör.
Alle Modelle verwenden model_config = {"from_attributes": True} (Pydantic v2).
NIEMALS class Config verwenden.
"""

from __future__ import annotations

from datetime import date
from enum import Enum
from typing import Optional

from pydantic import BaseModel, Field, field_validator


# --- Enums ---

class MaterialType(str, Enum):
    """Materialtypen für Ankergeschirr-Komponenten."""
    STAINLESS_316L = "316L"
    STAINLESS_316 = "316"
    STAINLESS_304 = "304"
    GALVANIZED = "galvanized"
    BRONZE = "bronze"
    ALUMINUM = "aluminum"
    TITANIUM = "titanium"
    NYLON = "nylon"
    HDPE = "hdpe"
    DUPLEX_2205 = "duplex_2205"


class ConfidenceLevel(str, Enum):
    """Confidence-Level gemäß AYDI-Standard."""
    MEASURED = "measured"
    CALCULATED = "calculated"
    VISUAL_HIGH = "visual_high"
    VISUAL_MEDIUM = "visual_medium"
    VISUAL_LOW = "visual_low"
    VISUAL_INSUFFICIENT = "visual_insufficient"
    ESTIMATED = "estimated"
    BENCHMARK = "benchmark"
    DOCUMENTED = "documented"


class ComponentCondition(str, Enum):
    """Zustandsbewertung einer Komponente."""
    NEW = "new"
    GOOD = "good"
    ACCEPTABLE = "acceptable"
    WORN = "worn"
    CRITICAL = "critical"
    FAILED = "failed"


class SeverityLevel(str, Enum):
    """Schweregrad eines Fehlerbildes."""
    CRITICAL = "critical"
    HIGH = "high"
    MEDIUM = "medium"
    LOW = "low"
    INFO = "info"


class BoatClass(str, Enum):
    """Bootsklasse für Dimensionierung."""
    SMALL_CRUISER = "small_cruiser"          # 6-8 m
    CRUISING_YACHT = "cruising_yacht"        # 8-12 m
    BLUEWATER_YACHT = "bluewater_yacht"      # 10-15 m
    PERFORMANCE_CRUISER = "performance_cruiser"  # 12-18 m
    KETCH = "ketch"                          # 15-22 m
    SUPERYACHT = "superyacht"                # 20-40 m
```

### ANHANG J: Ankerwirbel-Modelle

```python
class SwivelType(str, Enum):
    """Bauformen von Ankerwirbeln."""
    JAW_JAW = "jaw_jaw"
    JAW_EYE = "jaw_eye"
    EYE_EYE = "eye_eye"
    SHACKLE_TYPE = "shackle_type"
    BALL_BEARING = "ball_bearing"


class AnchorSwivel(BaseModel):
    """Ankerwirbel (Anchor Swivel) — Datenmodell."""

    model_config = {"from_attributes": True}

    manufacturer: str = Field(..., description="Hersteller des Wirbels")
    model: str = Field(..., description="Modellbezeichnung")
    swivel_type: SwivelType = Field(..., description="Bauform des Wirbels")
    chain_size_mm: float = Field(..., ge=4, le=22, description="Kettengröße in mm")
    wll_kg: float = Field(..., ge=100, description="Working Load Limit in kg")
    breaking_load_kg: float = Field(..., ge=200, description="Bruchlast in kg")
    weight_g: float = Field(..., ge=50, description="Gewicht in Gramm")
    material: MaterialType = Field(..., description="Werkstoff")
    has_ball_bearing: bool = Field(False, description="Kugellager vorhanden")
    price_eur: Optional[float] = Field(None, ge=0, description="Preis in EUR")
    certification: Optional[str] = Field(None, description="Zertifizierung (z.B. BV, CE)")
    warranty_years: Optional[int] = Field(None, ge=0, description="Garantie in Jahren")

    @field_validator("breaking_load_kg")
    @classmethod
    def breaking_load_must_exceed_wll(cls, v: float, info) -> float:
        """Bruchlast muss mindestens 2,5× WLL betragen."""
        wll = info.data.get("wll_kg")
        if wll and v < wll * 2.5:
            raise ValueError(
                f"Bruchlast ({v} kg) muss mindestens 2,5× WLL ({wll} kg) betragen"
            )
        return v


class SwivelAssessment(BaseModel):
    """Bewertung eines Ankerwirbels durch AYDI."""

    model_config = {"from_attributes": True}

    swivel: AnchorSwivel
    condition: ComponentCondition
    confidence: ConfidenceLevel
    is_compatible_with_chain: bool = Field(
        ..., description="Passt der Wirbel zur Kettengröße?"
    )
    wll_sufficient: bool = Field(
        ..., description="Ist die WLL ausreichend für die Bootsklasse?"
    )
    rotation_free: Optional[bool] = Field(
        None, description="Dreht sich der Wirbel frei?"
    )
    corrosion_detected: Optional[bool] = Field(
        None, description="Korrosion erkannt?"
    )
    bolt_secured: Optional[bool] = Field(
        None, description="Ist der Bolzen gesichert?"
    )
    remaining_life_years: Optional[float] = Field(
        None, ge=0, description="Geschätzte Restlebensdauer in Jahren"
    )
    findings: list[str] = Field(default_factory=list, description="Befunde")
    recommendations: list[str] = Field(
        default_factory=list, description="Empfehlungen"
    )
    score: float = Field(..., ge=0, le=100, description="Bewertung 0-100")
```

### ANHANG K: Ankerschäkel-Modelle

```python
class ShackleType(str, Enum):
    """Bauformen von Ankerschäkeln."""
    BOW_SHACKLE = "bow_shackle"
    DEE_SHACKLE = "dee_shackle"
    LONG_SHACKLE = "long_shackle"
    SNAP_SHACKLE = "snap_shackle"


class BoltSecuringMethod(str, Enum):
    """Methoden zur Bolzensicherung."""
    SEIZING_WIRE = "seizing_wire"
    COTTER_PIN = "cotter_pin"
    THREAD_LOCKER = "thread_locker"
    SELF_LOCKING = "self_locking"
    NONE = "none"


class AnchorShackle(BaseModel):
    """Ankerschäkel (Anchor Shackle) — Datenmodell."""

    model_config = {"from_attributes": True}

    manufacturer: str = Field(..., description="Hersteller")
    model: str = Field(..., description="Modellbezeichnung")
    shackle_type: ShackleType = Field(..., description="Schäkeltyp")
    size_mm: float = Field(..., ge=4, le=30, description="Schäkelgröße in mm")
    bolt_diameter_mm: float = Field(..., ge=6, le=30, description="Bolzendurchmesser in mm")
    inner_width_mm: float = Field(..., ge=8, le=50, description="Innenweite in mm")
    wll_kg: float = Field(..., ge=100, description="Working Load Limit in kg")
    breaking_load_kg: float = Field(..., ge=200, description="Bruchlast in kg")
    material: MaterialType = Field(..., description="Werkstoff")
    bolt_securing: BoltSecuringMethod = Field(
        BoltSecuringMethod.SEIZING_WIRE, description="Bolzensicherungsmethode"
    )
    price_eur: Optional[float] = Field(None, ge=0, description="Preis in EUR")

    @field_validator("inner_width_mm")
    @classmethod
    def inner_width_must_fit_chain(cls, v: float, info) -> float:
        """Innenweite muss mindestens 2× Bolzendurchmesser betragen."""
        bolt = info.data.get("bolt_diameter_mm")
        if bolt and v < bolt * 1.2:
            raise ValueError(
                f"Innenweite ({v} mm) zu gering für Bolzen ({bolt} mm)"
            )
        return v


class ShackleAssessment(BaseModel):
    """Bewertung eines Ankerschäkels durch AYDI."""

    model_config = {"from_attributes": True}

    shackle: AnchorShackle
    condition: ComponentCondition
    confidence: ConfidenceLevel
    is_compatible_with_chain: bool
    wll_sufficient: bool
    bolt_present: Optional[bool] = None
    bolt_secured: Optional[bool] = None
    securing_method: Optional[BoltSecuringMethod] = None
    corrosion_detected: Optional[bool] = None
    findings: list[str] = Field(default_factory=list)
    recommendations: list[str] = Field(default_factory=list)
    score: float = Field(..., ge=0, le=100)
```

### ANHANG L: Bugrollen-Modelle

```python
class BowRollerType(str, Enum):
    """Bauformen von Bugrollen."""
    SIMPLE = "simple"
    TWIN = "twin"
    SELF_ALIGNING = "self_aligning"
    ANCHOR_CRADLE = "anchor_cradle"
    FLUSH_MOUNT = "flush_mount"


class BowRoller(BaseModel):
    """Bugrolle (Bow Roller) — Datenmodell."""

    model_config = {"from_attributes": True}

    manufacturer: str = Field(..., description="Hersteller")
    model: str = Field(..., description="Modellbezeichnung")
    roller_type: BowRollerType = Field(..., description="Bauform")
    chain_size_min_mm: float = Field(..., ge=4, le=20, description="Min. Kettengröße mm")
    chain_size_max_mm: float = Field(..., ge=4, le=22, description="Max. Kettengröße mm")
    max_anchor_weight_kg: float = Field(..., ge=1, description="Max. Ankergewicht kg")
    roller_length_mm: Optional[float] = Field(None, ge=50, description="Rollenlänge mm")
    cheek_height_mm: Optional[float] = Field(None, ge=10, description="Wangenhöhe mm")
    axle_diameter_mm: Optional[float] = Field(None, ge=8, description="Achsdurchmesser mm")
    material_cheeks: MaterialType = Field(..., description="Material Wangen")
    material_roller: MaterialType = Field(..., description="Material Rolle")
    bolt_count: int = Field(..., ge=2, le=12, description="Anzahl Befestigungsbolzen")
    bolt_size: str = Field(..., description="Bolzengröße (z.B. M8, M10)")
    price_eur: Optional[float] = Field(None, ge=0, description="Preis in EUR")

    @field_validator("chain_size_max_mm")
    @classmethod
    def max_must_exceed_min(cls, v: float, info) -> float:
        """Max. Kettengröße muss ≥ Min. sein."""
        min_val = info.data.get("chain_size_min_mm")
        if min_val and v < min_val:
            raise ValueError("Max. Kettengröße muss ≥ Min. Kettengröße sein")
        return v


class BowRollerAssessment(BaseModel):
    """Bewertung einer Bugrolle durch AYDI."""

    model_config = {"from_attributes": True}

    bow_roller: BowRoller
    condition: ComponentCondition
    confidence: ConfidenceLevel
    is_compatible_with_chain: bool
    is_compatible_with_anchor: bool
    cheeks_sufficient_height: Optional[bool] = None
    roller_turns_freely: Optional[bool] = None
    mounting_secure: Optional[bool] = None
    backing_plate_present: Optional[bool] = None
    corrosion_detected: Optional[bool] = None
    chafe_marks_on_hull: Optional[bool] = None
    findings: list[str] = Field(default_factory=list)
    recommendations: list[str] = Field(default_factory=list)
    score: float = Field(..., ge=0, le=100)
```

### ANHANG M: Kettenstopper-Modelle

```python
class ChainStopperType(str, Enum):
    """Bauformen von Kettenstoppern."""
    LEVER = "lever"
    GUILLOTINE = "guillotine"
    SCREW = "screw"
    DEVILS_CLAW = "devils_claw"
    CHAIN_BRAKE = "chain_brake"


class ChainStopper(BaseModel):
    """Kettenstopper (Chain Stopper) — Datenmodell."""

    model_config = {"from_attributes": True}

    manufacturer: str = Field(..., description="Hersteller")
    model: str = Field(..., description="Modellbezeichnung")
    stopper_type: ChainStopperType = Field(..., description="Bauform")
    chain_size_min_mm: float = Field(..., ge=4, le=20)
    chain_size_max_mm: float = Field(..., ge=4, le=22)
    wll_kg: float = Field(..., ge=500, description="Working Load Limit in kg")
    material: MaterialType = Field(..., description="Werkstoff")
    bolt_count: int = Field(..., ge=2, le=8)
    bolt_size: str = Field(..., description="Bolzengröße")
    price_eur: Optional[float] = Field(None, ge=0)

    @field_validator("chain_size_max_mm")
    @classmethod
    def max_must_exceed_min(cls, v: float, info) -> float:
        min_val = info.data.get("chain_size_min_mm")
        if min_val and v < min_val:
            raise ValueError("Max. Kettengröße muss ≥ Min. Kettengröße sein")
        return v


class ChainStopperAssessment(BaseModel):
    """Bewertung eines Kettenstoppers durch AYDI."""

    model_config = {"from_attributes": True}

    chain_stopper: ChainStopper
    condition: ComponentCondition
    confidence: ConfidenceLevel
    is_compatible_with_chain: bool
    wll_sufficient: bool
    mechanism_functional: Optional[bool] = None
    mounting_secure: Optional[bool] = None
    backing_plate_present: Optional[bool] = None
    corrosion_detected: Optional[bool] = None
    snubber_present: Optional[bool] = None
    findings: list[str] = Field(default_factory=list)
    recommendations: list[str] = Field(default_factory=list)
    score: float = Field(..., ge=0, le=100)
```

### ANHANG N: Ankerkasten-Modelle

```python
class AnchorLockerType(str, Enum):
    """Bauformen von Ankerkästen."""
    BUILT_IN = "built_in"
    DECK_MOUNTED = "deck_mounted"
    BOWSPRIT = "bowsprit"


class AnchorLocker(BaseModel):
    """Ankerkasten (Anchor Locker) — Datenmodell."""

    model_config = {"from_attributes": True}

    locker_type: AnchorLockerType = Field(..., description="Bauform")
    volume_liters: float = Field(..., ge=10, description="Volumen in Litern")
    chain_capacity_m: float = Field(..., ge=5, description="Kettenkapazität in Metern")
    chain_size_mm: float = Field(..., ge=4, le=22, description="Kettengröße in mm")
    has_drainage: bool = Field(..., description="Entwässerung vorhanden")
    drainage_count: int = Field(0, ge=0, description="Anzahl Ablauföffnungen")
    drainage_diameter_mm: Optional[float] = Field(None, description="Ablauf-Ø mm")
    has_ventilation: bool = Field(False, description="Belüftung vorhanden")
    has_hatch_seal: bool = Field(True, description="Lukendichtung vorhanden")
    material: Optional[str] = Field(None, description="Material (GFK, Alu, etc.)")

    @field_validator("volume_liters")
    @classmethod
    def volume_must_fit_chain(cls, v: float, info) -> float:
        """Kastenvolumen muss für die Kettenmenge ausreichen."""
        chain_m = info.data.get("chain_capacity_m")
        chain_mm = info.data.get("chain_size_mm")
        if chain_m and chain_mm:
            required = chain_m * (chain_mm / 10) ** 2 * 0.55 * 1.8
            if v < required * 0.8:
                raise ValueError(
                    f"Kastenvolumen ({v}l) möglicherweise zu klein "
                    f"für {chain_m}m × {chain_mm}mm Kette (benötigt ~{required:.0f}l)"
                )
        return v


class AnchorLockerAssessment(BaseModel):
    """Bewertung eines Ankerkastens durch AYDI."""

    model_config = {"from_attributes": True}

    locker: AnchorLocker
    condition: ComponentCondition
    confidence: ConfidenceLevel
    volume_sufficient: bool
    drainage_functional: Optional[bool] = None
    ventilation_adequate: Optional[bool] = None
    hatch_seal_intact: Optional[bool] = None
    water_present: Optional[bool] = None
    odor_detected: Optional[bool] = None
    chain_tangling: Optional[bool] = None
    findings: list[str] = Field(default_factory=list)
    recommendations: list[str] = Field(default_factory=list)
    score: float = Field(..., ge=0, le=100)
```

### ANHANG O: Ankermarkierung-Modelle

```python
class MarkingMethod(str, Enum):
    """Methoden der Ankerkettenmarkierung."""
    CABLE_TIES = "cable_ties"
    SPRAY_PAINT = "spray_paint"
    EPOXY_PAINT = "epoxy_paint"
    ELECTRONIC_COUNTER = "electronic_counter"
    NONE = "none"


class ChainMarking(BaseModel):
    """Ankerkettenmarkierung — Datenmodell."""

    model_config = {"from_attributes": True}

    method: MarkingMethod = Field(..., description="Markierungsmethode")
    interval_m: float = Field(5.0, ge=1, le=25, description="Markierungsintervall in Metern")
    total_chain_length_m: float = Field(..., ge=5, description="Gesamtkettenlänge in Metern")
    color_scheme: Optional[dict[float, str]] = Field(
        None, description="Farbschema: {Meter: Farbe}"
    )
    end_marking_present: bool = Field(
        False, description="Endmarkierung vorhanden"
    )
    weak_link_present: bool = Field(
        False, description="Soll-Bruchstelle am Kettenende vorhanden"
    )
    weak_link_type: Optional[str] = Field(
        None, description="Art der Soll-Bruchstelle"
    )
    electronic_counter_installed: bool = Field(
        False, description="Elektronischer Kettenzähler installiert"
    )
    electronic_counter_manufacturer: Optional[str] = Field(
        None, description="Hersteller Kettenzähler"
    )
    last_renewed: Optional[date] = Field(
        None, description="Letzte Erneuerung der Markierung"
    )


class ChainMarkingAssessment(BaseModel):
    """Bewertung der Ankerkettenmarkierung durch AYDI."""

    model_config = {"from_attributes": True}

    marking: ChainMarking
    confidence: ConfidenceLevel
    is_readable: Optional[bool] = None
    end_marking_visible: Optional[bool] = None
    weak_link_adequate: Optional[bool] = None
    renewal_recommended: bool = False
    findings: list[str] = Field(default_factory=list)
    recommendations: list[str] = Field(default_factory=list)
    score: float = Field(..., ge=0, le=100)
```

### ANHANG P: Beleuchtung und Signale

```python
class AnchorLightType(str, Enum):
    """Typen von Ankerlichtern."""
    MASTHEAD_FIXED = "masthead_fixed"
    CLIP_ON = "clip_on"
    POLE_MOUNT = "pole_mount"
    SOLAR_LANTERN = "solar_lantern"


class LightSource(str, Enum):
    """Leuchtmitteltyp."""
    LED = "led"
    INCANDESCENT = "incandescent"
    SOLAR_LED = "solar_led"


class AnchorLight(BaseModel):
    """Ankerlicht — Datenmodell."""

    model_config = {"from_attributes": True}

    manufacturer: str = Field(..., description="Hersteller")
    model: str = Field(..., description="Modellbezeichnung")
    light_type: AnchorLightType = Field(..., description="Montagetyp")
    light_source: LightSource = Field(..., description="Leuchtmitteltyp")
    visibility_nm: float = Field(..., ge=1, le=5, description="Sichtweite in Seemeilen")
    power_watts: float = Field(..., ge=0.1, le=30, description="Leistungsaufnahme in Watt")
    voltage: float = Field(12.0, description="Betriebsspannung in Volt")
    current_ma: Optional[float] = Field(None, description="Stromaufnahme in mA")
    is_colreg_compliant: bool = Field(True, description="KVR-konform")
    price_eur: Optional[float] = Field(None, ge=0)


class AnchorBall(BaseModel):
    """Ankerball (Day Shape) — Datenmodell."""

    model_config = {"from_attributes": True}

    manufacturer: Optional[str] = None
    diameter_mm: float = Field(..., ge=200, description="Durchmesser in mm")
    is_collapsible: bool = Field(False, description="Faltbar")
    is_colreg_compliant: bool = Field(True, description="KVR-konform (∅ ≥ 300 mm)")
    price_eur: Optional[float] = Field(None, ge=0)

    @field_validator("is_colreg_compliant")
    @classmethod
    def check_compliance(cls, v: bool, info) -> bool:
        diameter = info.data.get("diameter_mm")
        if diameter and diameter < 300:
            return False
        return v


class NavigationSignalsAssessment(BaseModel):
    """Bewertung der Ankersignale durch AYDI."""

    model_config = {"from_attributes": True}

    anchor_light: Optional[AnchorLight] = None
    anchor_ball: Optional[AnchorBall] = None
    confidence: ConfidenceLevel
    light_functional: Optional[bool] = None
    light_colreg_compliant: Optional[bool] = None
    ball_present: Optional[bool] = None
    ball_colreg_compliant: Optional[bool] = None
    findings: list[str] = Field(default_factory=list)
    recommendations: list[str] = Field(default_factory=list)
    score: float = Field(..., ge=0, le=100)
```

### ANHANG Q: Gesamt-Ankergeschirr-Bewertung

```python
class SnubberLine(BaseModel):
    """Reiterleine (Snubber/Bridle) — Datenmodell."""

    model_config = {"from_attributes": True}

    diameter_mm: float = Field(..., ge=8, le=28, description="Durchmesser in mm")
    length_m: float = Field(..., ge=3, le=30, description="Länge in Metern")
    material: str = Field("nylon_3strand", description="Material")
    has_chafe_guard: bool = Field(False, description="Scheuerschutz vorhanden")
    chain_hook_type: Optional[str] = Field(None, description="Kettenhaken-Typ")
    condition: ComponentCondition = Field(
        ComponentCondition.GOOD, description="Zustand"
    )


class TripLine(BaseModel):
    """Tripleine (Trip Line) — Datenmodell."""

    model_config = {"from_attributes": True}

    diameter_mm: float = Field(..., ge=4, le=16, description="Durchmesser in mm")
    length_m: float = Field(..., ge=5, le=80, description="Länge in Metern")
    material: str = Field("polypropylene", description="Material (sollte schwimmfähig sein)")
    is_buoyant: bool = Field(True, description="Schwimmfähig")
    has_buoy: bool = Field(False, description="Ankerboje befestigt")
    buoy_volume_l: Optional[float] = Field(None, ge=1, description="Bojenvolumen in Litern")


class AnchorTackleFullAssessment(BaseModel):
    """Vollständige Bewertung des Ankergeschirrs durch AYDI."""

    model_config = {"from_attributes": True}

    # Identifikation
    boat_name: Optional[str] = None
    boat_class: BoatClass = Field(..., description="Bootsklasse")
    loa_m: float = Field(..., ge=4, le=60, description="Länge über alles in Metern")
    displacement_t: float = Field(..., ge=0.5, le=500, description="Verdrängung in Tonnen")
    assessment_date: date = Field(..., description="Bewertungsdatum")

    # Einzelbewertungen
    swivel_assessment: Optional[SwivelAssessment] = None
    shackle_assessments: list[ShackleAssessment] = Field(default_factory=list)
    bow_roller_assessment: Optional[BowRollerAssessment] = None
    chain_stopper_assessment: Optional[ChainStopperAssessment] = None
    locker_assessment: Optional[AnchorLockerAssessment] = None
    marking_assessment: Optional[ChainMarkingAssessment] = None
    signals_assessment: Optional[NavigationSignalsAssessment] = None

    # Zusatzkomponenten
    snubber: Optional[SnubberLine] = None
    trip_line: Optional[TripLine] = None

    # Gesamtbewertung
    overall_score: float = Field(..., ge=0, le=100, description="Gesamtbewertung 0-100")
    overall_confidence: ConfidenceLevel = Field(..., description="Gesamt-Confidence")
    is_bluewater_ready: bool = Field(False, description="Blauwassertauglich")
    is_coastal_adequate: bool = Field(False, description="Küstenfahrt-tauglich")

    # Befunde und Empfehlungen
    critical_findings: list[str] = Field(
        default_factory=list, description="Kritische Befunde"
    )
    findings: list[str] = Field(
        default_factory=list, description="Alle Befunde"
    )
    recommendations: list[str] = Field(
        default_factory=list, description="Empfehlungen"
    )

    # Kosten
    estimated_upgrade_cost_eur: Optional[float] = Field(
        None, ge=0, description="Geschätzte Kosten für empfohlenes Upgrade"
    )

    # Metadaten
    aydi_version: str = Field("2.0", description="AYDI-Version")
    analysis_modules_used: list[str] = Field(
        default_factory=list, description="Verwendete Analysemodule"
    )
```

### ANHANG R: Fehlerbild-Modelle

```python
class FaultPattern(BaseModel):
    """Fehlerbild im Ankergeschirr — Datenmodell."""

    model_config = {"from_attributes": True}

    fault_id: str = Field(
        ...,
        pattern=r"^F-17_04-\d{2}$",
        description="Fehlerbild-ID (z.B. F-17_04-01)"
    )
    title: str = Field(..., description="Kurztitel des Fehlerbildes")
    description: str = Field(..., description="Ausführliche Beschreibung")
    severity: SeverityLevel = Field(..., description="Schweregrad")
    affected_component: str = Field(
        ..., description="Betroffene Komponente (z.B. 'swivel', 'shackle')"
    )
    causes: list[str] = Field(default_factory=list, description="Mögliche Ursachen")
    visual_indicators: list[str] = Field(
        default_factory=list, description="Visuelle Indikatoren für Fotoerkennung"
    )
    recommended_actions: list[str] = Field(
        default_factory=list, description="Empfohlene Maßnahmen"
    )
    typical_confidence: ConfidenceLevel = Field(
        ..., description="Typischer Confidence-Level bei visueller Erkennung"
    )
    estimated_repair_cost_eur: Optional[tuple[float, float]] = Field(
        None, description="Geschätzte Reparaturkosten (min, max) in EUR"
    )


class FaultPatternMatch(BaseModel):
    """Ergebnis einer Fehlerbild-Erkennung durch AYDI."""

    model_config = {"from_attributes": True}

    fault_pattern: FaultPattern
    confidence: ConfidenceLevel
    match_score: float = Field(..., ge=0, le=1, description="Übereinstimmung 0.0-1.0")
    location_description: Optional[str] = Field(
        None, description="Lokalisierung des Fehlers"
    )
    evidence: list[str] = Field(
        default_factory=list, description="Erkennungsmerkmale"
    )
    recommended_action: str = Field(
        ..., description="Primäre empfohlene Maßnahme"
    )
    urgency: str = Field(
        ..., description="Dringlichkeit: 'sofort', 'zeitnah', 'nächste_saison'"
    )


# --- Zusammenfassung aller Fehlermuster ---

ANCHOR_TACKLE_FAULT_PATTERNS: list[dict] = [
    {
        "fault_id": "F-17_04-01",
        "title": "Korrodierter Ankerwirbel",
        "severity": "critical",
        "affected_component": "swivel",
        "typical_confidence": "visual_high",
    },
    {
        "fault_id": "F-17_04-02",
        "title": "Blockierter Ankerwirbel",
        "severity": "high",
        "affected_component": "swivel",
        "typical_confidence": "visual_medium",
    },
    {
        "fault_id": "F-17_04-03",
        "title": "Gebrochene Ankerrolle",
        "severity": "critical",
        "affected_component": "bow_roller",
        "typical_confidence": "visual_high",
    },
    {
        "fault_id": "F-17_04-04",
        "title": "Undichter Ankerkasten",
        "severity": "high",
        "affected_component": "anchor_locker",
        "typical_confidence": "visual_medium",
    },
    {
        "fault_id": "F-17_04-05",
        "title": "Schäkelbolzen gelöst",
        "severity": "critical",
        "affected_component": "shackle",
        "typical_confidence": "visual_high",
    },
    {
        "fault_id": "F-17_04-06",
        "title": "Kettenstopper-Versagen",
        "severity": "critical",
        "affected_component": "chain_stopper",
        "typical_confidence": "visual_medium",
    },
    {
        "fault_id": "F-17_04-07",
        "title": "Verklemmter Anker ohne Tripleine",
        "severity": "high",
        "affected_component": "trip_line",
        "typical_confidence": "visual_low",
    },
    {
        "fault_id": "F-17_04-08",
        "title": "Ankerball fehlt",
        "severity": "medium",
        "affected_component": "navigation_signals",
        "typical_confidence": "visual_high",
    },
    {
        "fault_id": "F-17_04-09",
        "title": "Galvanische Korrosion an Beschlägen",
        "severity": "high",
        "affected_component": "fittings",
        "typical_confidence": "visual_medium",
    },
    {
        "fault_id": "F-17_04-10",
        "title": "Kette scheuert am Bug",
        "severity": "medium",
        "affected_component": "bow_roller",
        "typical_confidence": "visual_high",
    },
    {
        "fault_id": "F-17_04-11",
        "title": "Verstopfte Ankerkastenentwässerung",
        "severity": "medium",
        "affected_component": "anchor_locker",
        "typical_confidence": "visual_medium",
    },
    {
        "fault_id": "F-17_04-12",
        "title": "Ankerkettenmarkierung unleserlich",
        "severity": "low",
        "affected_component": "chain_marking",
        "typical_confidence": "visual_high",
    },
]
```

---

### ANHANG R.1: Konfigurations-Konstanten

```python
# --- Konfiguration für Ankergeschirr-Analyse ---

ANCHOR_TACKLE_SCORING_WEIGHTS: dict[str, float] = {
    "swivel": 0.15,
    "shackle": 0.10,
    "bow_roller": 0.15,
    "chain_stopper": 0.15,
    "locker": 0.10,
    "marking": 0.05,
    "signals": 0.10,
    "snubber": 0.10,
    "trip_line": 0.05,
    "compatibility": 0.05,
}

CHAIN_SIZE_TO_MIN_SHACKLE: dict[int, int] = {
    6: 8, 8: 10, 10: 12, 12: 14, 13: 14, 14: 16, 16: 19,
}

CHAIN_SIZE_TO_ROLLER_NUT_WIDTH: dict[int, tuple[int, int]] = {
    6: (8, 10), 8: (10, 13), 10: (13, 16),
    12: (16, 19), 13: (17, 20), 14: (19, 22), 16: (22, 25),
}

BOAT_CLASS_MIN_WLL: dict[str, int] = {
    "small_cruiser": 800,
    "cruising_yacht": 1500,
    "bluewater_yacht": 2500,
    "performance_cruiser": 3000,
    "ketch": 4000,
    "superyacht": 6000,
}

BLUEWATER_MINIMUM_SCORE: float = 80.0
COASTAL_MINIMUM_SCORE: float = 50.0

MARKING_COLORS: dict[int, str] = {
    10: "rot", 15: "blau", 20: "gelb", 25: "grün", 30: "weiß",
    35: "rot_doppelt", 40: "blau_doppelt", 45: "gelb_doppelt", 50: "grün_doppelt",
}
```

### ANHANG R.2: Scoring-Funktionen

```python
def calculate_anchor_tackle_score(
    assessment: AnchorTackleFullAssessment,
) -> float:
    """
    Berechnet den Gesamtscore des Ankergeschirrs.

    Gewichtung der Einzelkomponenten:
    - Wirbel: 15%
    - Schäkel: 10%
    - Bugrolle: 15%
    - Kettenstopper: 15%
    - Ankerkasten: 10%
    - Markierung: 5%
    - Signale (Licht + Ball): 10%
    - Reiterleine: 10%
    - Tripleine: 5%
    - Allgemeine Kompatibilität: 5%
    """
    weights = {
        "swivel": 0.15,
        "shackle": 0.10,
        "bow_roller": 0.15,
        "chain_stopper": 0.15,
        "locker": 0.10,
        "marking": 0.05,
        "signals": 0.10,
        "snubber": 0.10,
        "trip_line": 0.05,
        "compatibility": 0.05,
    }

    scores: dict[str, float] = {}

    if assessment.swivel_assessment:
        scores["swivel"] = assessment.swivel_assessment.score
    else:
        scores["swivel"] = 0.0  # Kein Wirbel = 0 Punkte

    if assessment.shackle_assessments:
        scores["shackle"] = sum(
            s.score for s in assessment.shackle_assessments
        ) / len(assessment.shackle_assessments)
    else:
        scores["shackle"] = 30.0  # Keine Schäkel bewertet = niedrig

    if assessment.bow_roller_assessment:
        scores["bow_roller"] = assessment.bow_roller_assessment.score
    else:
        scores["bow_roller"] = 20.0

    if assessment.chain_stopper_assessment:
        scores["chain_stopper"] = assessment.chain_stopper_assessment.score
    else:
        scores["chain_stopper"] = 0.0  # Kein Stopper = kritisch

    if assessment.locker_assessment:
        scores["locker"] = assessment.locker_assessment.score
    else:
        scores["locker"] = 50.0  # Neutral wenn nicht bewertet

    if assessment.marking_assessment:
        scores["marking"] = assessment.marking_assessment.score
    else:
        scores["marking"] = 20.0  # Keine Markierung = schlecht

    if assessment.signals_assessment:
        scores["signals"] = assessment.signals_assessment.score
    else:
        scores["signals"] = 30.0  # Keine Signale bewertet = schlecht

    if assessment.snubber:
        scores["snubber"] = 80.0 if assessment.snubber.condition in (
            ComponentCondition.NEW, ComponentCondition.GOOD
        ) else 50.0
    else:
        scores["snubber"] = 0.0  # Keine Reiterleine = 0

    if assessment.trip_line:
        scores["trip_line"] = 80.0
    else:
        scores["trip_line"] = 30.0  # Keine Tripleine = niedrig

    # Kompatibilitätsprüfung
    compatibility_score = 100.0
    if assessment.swivel_assessment and not assessment.swivel_assessment.is_compatible_with_chain:
        compatibility_score -= 50.0
    if assessment.bow_roller_assessment and not assessment.bow_roller_assessment.is_compatible_with_chain:
        compatibility_score -= 30.0
    if assessment.chain_stopper_assessment and not assessment.chain_stopper_assessment.is_compatible_with_chain:
        compatibility_score -= 20.0
    scores["compatibility"] = max(0.0, compatibility_score)

    # Gewichtete Summe
    total = sum(scores[k] * weights[k] for k in weights)
    return round(min(100.0, max(0.0, total)), 1)


def is_bluewater_ready(assessment: AnchorTackleFullAssessment) -> bool:
    """Prüft ob das Ankergeschirr blauwassertauglich ist."""
    checks = [
        assessment.overall_score >= 80,
        assessment.swivel_assessment is not None,
        assessment.chain_stopper_assessment is not None,
        assessment.snubber is not None,
        assessment.signals_assessment is not None,
    ]
    if assessment.swivel_assessment:
        checks.append(assessment.swivel_assessment.wll_sufficient)
    if assessment.chain_stopper_assessment:
        checks.append(assessment.chain_stopper_assessment.wll_sufficient)
    return all(checks)


def is_coastal_adequate(assessment: AnchorTackleFullAssessment) -> bool:
    """Prüft ob das Ankergeschirr für Küstenfahrt ausreichend ist."""
    checks = [
        assessment.overall_score >= 50,
        assessment.swivel_assessment is not None or True,  # Wirbel empfohlen, nicht Pflicht
    ]
    if assessment.swivel_assessment:
        checks.append(assessment.swivel_assessment.wll_sufficient)
    return all(checks)
```

---

*Ende des Dokuments — AYDI Maritime Knowledge Base v2.0, April 2026*
*Dieses Dokument wird regelmäßig aktualisiert. Preise sind Richtwerte und können abweichen.*
*Alle Angaben ohne Gewähr. Für sicherheitsrelevante Entscheidungen stets Fachpersonal konsultieren.*
