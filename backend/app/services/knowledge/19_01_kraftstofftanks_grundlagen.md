# 19.01 — Kraftstofftanks: Grundlagen, Materialien, Normen (Diesel- und Benzintanks im Yachtbau)

> **AYDI Wissensdatei 19.01** — Kategorie 19: Kraftstoffsysteme — Tanks
> **Confidence-Quelle:** measured (Hersteller-TDS, Normen-Originale), documented (Hersteller-Kataloge, Klassifikationsgesellschaften), estimated (Erfahrungswerte, Werft-Konsens)
> **Letzte Aktualisierung:** 2026-05-02
> **SICHERHEITSKRITISCH:** Kraftstofftanks sind Brand-, Explosions- und Umweltgefährdungs-relevante Bauteile. Fehlerhafte Tanks, mangelhafte Belüftung oder falsche Materialwahl können zu Kraftstoffaustritt, Dampfansammlung und katastrophalem Versagen führen.

---

## Inhaltsverzeichnis

1. [Einführung und Übersicht](#1-einführung-und-übersicht)
2. [Grundlagen und Theorie](#2-grundlagen-und-theorie)
3. [Typenübersicht](#3-typenübersicht)
4. [Produktlinien und Spezifikationen](#4-produktlinien-und-spezifikationen)
5. [Hersteller-Datenbank](#5-hersteller-datenbank)
6. [Fehlerbild-Atlas](#6-fehlerbild-atlas)
7. [Troubleshooting-Entscheidungsbäume](#7-troubleshooting-entscheidungsbäume)
8. [FAQ](#8-faq)
9. [Glossar](#9-glossar)
10. [Schnell-Referenz](#10-schnell-referenz)
11. [ANHANG A–H: Fallstudien](#11-anhang-ah-fallstudien)
12. [ANHANG I–R: Pydantic v2 Modelle](#12-anhang-ir-pydantic-v2-modelle)

---

## 1. Einführung und Übersicht

### 1.1 Bedeutung der Kraftstofftanks im Yachtbau

Kraftstofftanks gehören zu den sicherheitskritischsten Systemen auf jeder motorisierten Yacht und auf Segelyachten mit Hilfsmotor. Sie erfüllen drei Kernfunktionen: sichere Lagerung des Kraftstoffs über die gesamte Lebensdauer des Bootes, zuverlässige Versorgung des Motors unter allen Betriebsbedingungen (Seegang, Krängung, Temperaturextreme) und Schutz der Umwelt vor Kontamination durch Kohlenwasserstoffe.

Die Bedeutung eines korrekt ausgelegten, installierten und gewarteten Tanksystems wird in der Praxis häufig unterschätzt. Während Antrieb, Rigg und Elektronik regelmäßig gewartet werden, bleiben Tanks oft jahrzehntelang ohne Inspektion — bis ein Versagen eintritt. Die Statistiken sprechen eine deutliche Sprache:

**Schadensdaten Kraftstofftanks:**

| Quelle | Zeitraum | Tank-bezogene Schäden | Durchschnittliche Schadenshöhe | Häufigste Ursache |
|--------|----------|----------------------|-------------------------------|-------------------|
| BoatUS Marine Insurance | 2016–2024 | 1.847 Fälle | 14.200 USD | Korrosion Stahltank |
| Pantaenius Yachtversicherung | 2017–2023 | 623 Fälle | 11.800 EUR | Lochfraß Aluminium |
| BSH Deutschland (geschätzt) | 2018–2023 | 189 Fälle | 9.400 EUR | Undichte Anschlüsse |
| Boat Safety Scheme UK | 2015–2023 | 412 Fälle | 8.900 GBP | Korrosion/Alterung |
| Veritas Marine Insurance NL | 2018–2023 | 267 Fälle | 12.600 EUR | Elektrolyse-Korrosion |

Die durchschnittliche Lebensdauer eines marine Kraftstofftanks variiert erheblich nach Material und Einbausituation:

| Material | Erwartete Lebensdauer | Hauptversagensursache | Typisches Versagensalter |
|----------|----------------------|----------------------|--------------------------|
| Edelstahl 316L | 25–40 Jahre | Spaltkorrosion an Schweißnähten | 20–30 Jahre |
| Aluminium 5083 | 15–25 Jahre | Lochfraß durch Kondenswasser | 12–20 Jahre |
| GFK (Laminat) | 20–35 Jahre | Osmose, Harzabbau durch Kraftstoff | 15–25 Jahre |
| PE-HD (Rotationsguss) | 15–25 Jahre | UV-Degradation, Versprödung | 12–20 Jahre |
| Flexibeltank (Bladder) | 8–15 Jahre | Materialermüdung, Abrieb | 8–12 Jahre |
| Schwarzstahl (verzinkt) | 10–20 Jahre | Durchrostung | 8–15 Jahre |

### 1.2 Sicherheitsrelevanz

Kraftstofftanks sind in der maritimen Sicherheitshierarchie auf Stufe 1 (höchste Kritikalität) eingestuft, gleichrangig mit Rumpfintegrität und Brandschutz. Die Risiken gliedern sich wie folgt:

**Primärrisiken:**

1. **Brand/Explosion (Benzin):** Benzintanks mit einem Flammpunkt von ca. -20°C erzeugen bei jeder Umgebungstemperatur zündfähige Dämpfe. Eine undichte Tankentlüftung oder ein gebrochener Tankanschluss kann innerhalb von Minuten eine explosive Atmosphäre im Bilgenbereich erzeugen. Die untere Explosionsgrenze (UEG) von Benzin liegt bei nur 1,0 Vol.-% — ein Liter ausgelaufenes Benzin erzeugt ca. 300 Liter explosionsfähiges Dampf-Luft-Gemisch.

2. **Brand (Diesel):** Diesel hat einen Flammpunkt >55°C (EN 590), ist aber keineswegs ungefährlich. Dieseldämpfe auf heißen Motorteilen (Turbolader >500°C, Auspuffkrümmer >400°C) entzünden sich sofort. Ein Riss in einem Dieseltank im Maschinenraum kann bei laufendem Motor zum Sprühnebel-Brand führen — einer der schwierigsten zu löschenden Brände an Bord.

3. **Strukturelle Integrität:** Kraftstoff ist schwer (Diesel: 0,84 kg/l, Benzin: 0,75 kg/l). Ein 400-Liter-Dieseltank wiegt befüllt ca. 380 kg. Bei Seegang wirken auf den Tankinhalt erhebliche dynamische Kräfte — bei 1g Beschleunigung verdoppelt sich die effektive Last. Unzureichend befestigte Tanks können sich lösen, Leitungen abreißen und gleichzeitig Kraftstoffaustritt und strukturelle Schäden verursachen.

4. **Umwelthaftung:** Kraftstoffaustritt in Gewässer ist in allen EU-Staaten strafbar. Bußgelder reichen von 5.000 EUR (geringfügiger Austritt) bis 500.000 EUR (erhebliche Gewässerverschmutzung). In Naturschutzgebieten und Trinkwasserzonen gelten verschärfte Strafen. Die Kosten für professionelle Gewässerreinigung nach einem Tankunfall liegen typisch bei 15.000–80.000 EUR.

**Sekundärrisiken:**

- **Kraftstoffkontamination:** Wasser, Mikroorganismen (Diesel-Bug), Rost und Sediment im Tank führen zu Motorstörungen, Injektorbeschädigungen und Filterblockaden — potenziell mitten auf See bei schwerer Wetter
- **Geruchsbelästigung:** Chronische Diesel-Leckagen durchdringen GFK-Laminate und Polster irreversibel. Die Geruchssanierung einer mit Diesel kontaminierten Yacht kostet typisch 5.000–15.000 EUR
- **Wertverlust:** Ein Tank-Austausch bei einer eingebauten Installation kostet 8.000–35.000 EUR je nach Zugänglichkeit. Yachten mit bekannten Tankproblemen verlieren 15–25% ihres Marktwerts

### 1.3 Scope dieser Wissensdatei

Diese Datei deckt folgende Bereiche ab:

- **Tankwerkstoffe:** Edelstahl 316L, Aluminium 5083/5086, GFK/Vinylester, PE-HD, flexible Bladder-Tanks, Schwarzstahl
- **Kraftstoffarten:** Diesel (EN 590, ULSD), Benzin (EN 228, E10, E15), Biodiesel-Beimischungen (B7, B20)
- **Tankformen:** Rechteckig, L-förmig, keilförmig (Bug), sattelförmig (unter Boden), Satteltanks, Integrationstanks
- **Größenbereich:** 20 Liter (Kleinboot-Standardtank) bis 20.000 Liter (Superyacht-Saddle-Tanks)
- **Bootslängen:** 6 m (Kleinboot) bis 40 m (große Motoryacht/Superyacht)
- **Normen:** ISO 21487 (Kunststoff- und Metalltanks), ISO 10088, ABYC H-24, ABYC H-33, CE-Sportbootrichtlinie 2013/53/EU
- **Installation:** Einbau, Befestigung, Leitungsanschlüsse, Entlüftung, Tankanzeige, Inspection Ports
- **Wartung:** Reinigung, Inspektion, Reparatur, Austausch, Kraftstoffbehandlung
- **Fehlerbilder:** 12 systematisch dokumentierte Versagensmuster mit Diagnose und Reparaturanleitung

**Nicht abgedeckt:**

- Wassertanks (→ separate Wissensdatei 20_01)
- Abwassertanks/Fäkalientanks (→ separate Wissensdatei 21_01)
- Gastanks/LPG (→ separate Wissensdatei 22_01)
- Kraftstoffleitungen und -schläuche (→ Wissensdatei 06_04)
- Kraftstofffilter und Wasserabscheider (→ Wissensdatei 19_02)
- Kraftstoffpumpen und Fördersysteme (→ Wissensdatei 19_03)

---

## 2. Grundlagen und Theorie

### 2.1 Tankwerkstoffe im Detail

#### 2.1.1 Edelstahl 316L (1.4404)

**Werkstoffbezeichnung:** X2CrNiMo17-12-2 (EN 10088-1), UNS S31603 (ASTM)

Edelstahl 316L ist das Referenzmaterial für marine Kraftstofftanks in semi-custom und custom Yachtbau. Die Legierung enthält 16–18% Chrom, 10–14% Nickel und 2–3% Molybdän. Das "L" steht für "Low Carbon" (max. 0,03% C), was die Anfälligkeit für interkristalline Korrosion nach dem Schweißen drastisch reduziert.

**Chemische Zusammensetzung (Gewichts-%):**

| Element | Min. | Max. | Funktion |
|---------|------|------|----------|
| Chrom (Cr) | 16,0% | 18,0% | Passivschichtbildung |
| Nickel (Ni) | 10,0% | 14,0% | Austenitische Struktur, Duktilität |
| Molybdän (Mo) | 2,0% | 3,0% | Lochfraßbeständigkeit |
| Kohlenstoff (C) | – | 0,03% | Reduziert interkristalline Korrosion |
| Mangan (Mn) | – | 2,0% | Warmfestigkeit |
| Silizium (Si) | – | 1,0% | Oxidationsbeständigkeit |
| Phosphor (P) | – | 0,045% | Unvermeidbare Verunreinigung |
| Schwefel (S) | – | 0,03% | Unvermeidbare Verunreinigung |
| Stickstoff (N) | – | 0,10% | Festigkeitssteigerung |
| Eisen (Fe) | Balance | – | Basismatrix |

**Mechanische Eigenschaften (Blech, geglüht):**

| Eigenschaft | Wert | Prüfnorm |
|------------|------|----------|
| Zugfestigkeit Rm | 485–680 MPa | EN ISO 6892-1 |
| Streckgrenze Rp0,2 | ≥170 MPa | EN ISO 6892-1 |
| Bruchdehnung A50 | ≥40% | EN ISO 6892-1 |
| Härte | ≤217 HB | EN ISO 6506-1 |
| Dichte | 7,98 g/cm³ | – |
| E-Modul | 193 GPa | – |
| Wärmeleitfähigkeit | 14,6 W/(m·K) | bei 100°C |
| Wärmeausdehnung | 15,9 × 10⁻⁶ /K | 20–100°C |
| Schmelzbereich | 1371–1399°C | – |

**Korrosionsbeständigkeit in mariner Umgebung:**

Die Lochfraßbeständigkeitsäquivalentzahl (PREN) von 316L beträgt:
PREN = %Cr + 3,3 × %Mo + 16 × %N = 17 + 3,3 × 2,5 + 16 × 0,05 = 26,05

Zum Vergleich: 304 (1.4301) hat PREN ~18, 316L PREN ~26, Duplex 2205 PREN ~35. Ein PREN >25 gilt als Mindestanforderung für dauerhaften Salzwasserkontakt. 316L liegt somit knapp über der Grenze — ausreichend für Tanks, die keinen permanenten Salzwasserkontakt haben, aber in salzhaltiger Atmosphäre stehen.

**Schweißbarkeit:**

316L ist mit allen gängigen Schweißverfahren verarbeitbar. Für Tankkonstruktionen werden verwendet:

| Verfahren | Bezeichnung | Einsatz | Schutzgas | Zusatzwerkstoff |
|-----------|-------------|---------|-----------|-----------------|
| WIG/TIG | GTAW (141) | Dünnblech ≤3mm, Wurzellagen | Argon 4.6 | W.Nr. 1.4430 (316L Si) |
| MIG/MAG | GMAW (131) | Dickblech >3mm, Füllagen | Argon/CO₂ (98/2) | W.Nr. 1.4430 |
| E-Hand | SMAW (111) | Reparaturen, Feldschweißung | – (Umhüllung) | E 19 12 3 L R |
| Plasma | PAW (15) | Automatisierte Fertigung | Argon 4.6 | W.Nr. 1.4430 |

**Kritische Schweißparameter für Tanks:**
- Zwischenlagentemperatur: max. 150°C (darüber → Sensibilisierung)
- Wärmeeinbringung: 0,5–1,5 kJ/mm (zu hoch → Chromkarbid-Ausscheidung)
- Wurzelschutz (Formiergas): Argon 4.6, min. 10 l/min — UNVERZICHTBAR bei Tankschweißungen, da oxidierte Wurzelseite zum Korrosionsstartor wird
- Nachbehandlung: Beizen (HF/HNO₃-Gemisch) oder Elektropolieren der Schweißnähte — bei Tankinnenräumen besonders wichtig

**Wandstärken für Kraftstofftanks (316L):**

| Tankvolumen | Empfohlene Wandstärke | Minimale Wandstärke (ISO 21487) | Bodenblech |
|-------------|----------------------|--------------------------------|------------|
| bis 100 l | 1,5 mm | 1,2 mm | 2,0 mm |
| 100–300 l | 2,0 mm | 1,5 mm | 2,5 mm |
| 300–600 l | 2,5 mm | 2,0 mm | 3,0 mm |
| 600–1.200 l | 3,0 mm | 2,5 mm | 3,0 mm |
| 1.200–3.000 l | 3,0–4,0 mm | 3,0 mm | 4,0 mm |
| >3.000 l | 4,0–5,0 mm | Individuelle Berechnung | 5,0 mm |

**Kosten (Stand 2025/2026, Richtwerte):**

| Position | Preis | Einheit |
|----------|-------|---------|
| 316L Blech 2mm | 45–65 EUR | pro kg |
| 316L Blech 3mm | 42–60 EUR | pro kg |
| Fertigtank einfach (rechteckig, bis 200l) | 1.200–2.500 EUR | pro Stück |
| Fertigtank komplex (L-Form, Schotten, >400l) | 3.500–8.000 EUR | pro Stück |
| Maßanfertigung Superyacht (>1.000l) | 6.000–18.000 EUR | pro Stück |
| WIG-Schweißarbeit Fachbetrieb | 85–140 EUR | pro Stunde |

**Vorteile:**
- Höchste Korrosionsbeständigkeit aller metallischen Tankwerkstoffe im Yachtbau
- Keine Reaktion mit Diesel, Benzin, Biodiesel oder Ethanol-Beimischungen
- Schweißbar, reparierbar, formbar
- Funkenbildungsfrei (wichtig für Benzintanks)
- Recyclebar
- Keine galvanische Problematik bei Kontakt mit Bronze-Borddurchlässen

**Nachteile:**
- Höchste Materialkosten aller Tankwerkstoffe
- Hohes Gewicht (7,98 g/cm³ — ca. 3× schwerer als Aluminium)
- Spaltkorrosion an Schweißnähten möglich bei mangelhafter Ausführung
- Bearbeitung erfordert Spezialwerkzeug (Edelstahl-spezifische Trennscheiben, Bohrer)
- Wärmeausdehnung: 15,9 × 10⁻⁶/K — bei großen Tanks müssen Dehnungsfugen oder flexible Anschlüsse vorgesehen werden

#### 2.1.2 Aluminium 5083 (AlMg4,5Mn0,7)

**Werkstoffbezeichnung:** EN AW-5083 (EN 573-3), UNS A95083 (ASTM), AlMg4,5Mn0,7

Aluminium 5083 ist die Standard-Aluminiumlegierung für marine Kraftstofftanks. Die hohe Magnesiumbeimischung (4,0–4,9%) verleiht hervorragende Korrosionsbeständigkeit in Salzwasseratmosphäre. Im Vergleich zu 6061-T6 (häufig im allgemeinen Maschinenbau) bietet 5083 deutlich bessere Beständigkeit gegen interkristalline Korrosion und Spannungsrisskorrosion im marinen Umfeld.

**Chemische Zusammensetzung (Gewichts-%):**

| Element | Min. | Max. | Funktion |
|---------|------|------|----------|
| Magnesium (Mg) | 4,0% | 4,9% | Festigkeit, Korrosionsbeständigkeit |
| Mangan (Mn) | 0,40% | 1,0% | Festigkeit, Kornfeinung |
| Chrom (Cr) | 0,05% | 0,25% | Spannungsrisskorrosions-Beständigkeit |
| Silizium (Si) | – | 0,40% | – |
| Eisen (Fe) | – | 0,40% | Verunreinigung |
| Kupfer (Cu) | – | 0,10% | Verunreinigung (MUSS niedrig sein!) |
| Zink (Zn) | – | 0,25% | – |
| Titan (Ti) | – | 0,15% | Kornfeinung |
| Aluminium (Al) | Balance | – | Basismatrix |

**Kritischer Hinweis — Kupfergehalt:** Der maximale Kupfergehalt von 0,10% ist eine harte Grenze für marine Anwendungen. Kupfer über 0,10% erhöht die Anfälligkeit für Lochfraßkorrosion in Salzwasserumgebung dramatisch. Bei der Beschaffung von Tankblech MUSS das Werkstoffzeugnis (3.1 nach EN 10204) auf den Cu-Gehalt geprüft werden. Billige Bleche aus asiatischer Produktion überschreiten diesen Wert häufig.

**Mechanische Eigenschaften:**

| Eigenschaft | 5083-O (weich) | 5083-H321 (kaltverfestigt) | Prüfnorm |
|------------|---------------|---------------------------|----------|
| Zugfestigkeit Rm | 275–350 MPa | 305–385 MPa | EN ISO 6892-1 |
| Streckgrenze Rp0,2 | ≥125 MPa | ≥215 MPa | EN ISO 6892-1 |
| Bruchdehnung A50 | ≥16% | ≥10% | EN ISO 6892-1 |
| Härte | ~75 HB | ~90 HB | EN ISO 6506-1 |
| Dichte | 2,66 g/cm³ | 2,66 g/cm³ | – |
| E-Modul | 71 GPa | 71 GPa | – |
| Wärmeleitfähigkeit | 117 W/(m·K) | 117 W/(m·K) | – |
| Wärmeausdehnung | 23,8 × 10⁻⁶/K | 23,8 × 10⁻⁶/K | 20–100°C |
| Schmelzbereich | 574–638°C | 574–638°C | – |

**Schweißbarkeit:**

Aluminium 5083 ist hervorragend schweißbar, ABER die Wärmeeinflusszone (WEZ) um die Schweißnaht verliert die Kaltverfestigung und fällt auf die Festigkeit des O-Zustands zurück. Bei Tankkonstruktionen ist daher 5083-O (weich geglüht) vorzuziehen — die Schweißnaht hat dann die gleiche Festigkeit wie das Grundmaterial.

| Verfahren | Bezeichnung | Schutzgas | Zusatzwerkstoff | Empfehlung |
|-----------|-------------|-----------|-----------------|------------|
| WIG/TIG | GTAW (141) | Argon 4.6 | AlMg5 (5183) oder AlMg4,5Mn (5083) | Bevorzugt für Tanknähte |
| MIG | GMAW (131) | Argon 4.6 | AlMg5 (5183) Ø 1,2mm | Für größere Tanks, Füllagen |
| WIG gepulst | GTAW-P | Argon 4.6 | AlMg5 (5183) | Dünnblech ≤2mm |

**WARNUNG — Zusatzwerkstoff:** Niemals AlSi5 (4043) als Zusatzwerkstoff für 5083-Tanks verwenden! AlSi5 erzeugt eine spröde Mg₂Si-Phase in der Schweißnaht und reduziert die Korrosionsbeständigkeit erheblich. Nur AlMg5 (5183) oder AlMg4,5Mn (5083) verwenden.

**Wandstärken für Kraftstofftanks (5083):**

| Tankvolumen | Empfohlene Wandstärke | Minimale Wandstärke (ISO 21487) | Bodenblech |
|-------------|----------------------|--------------------------------|------------|
| bis 100 l | 2,5 mm | 2,0 mm | 3,0 mm |
| 100–300 l | 3,0 mm | 2,5 mm | 4,0 mm |
| 300–600 l | 4,0 mm | 3,0 mm | 5,0 mm |
| 600–1.200 l | 5,0 mm | 4,0 mm | 6,0 mm |
| 1.200–3.000 l | 6,0 mm | 5,0 mm | 6,0 mm |
| >3.000 l | 6,0–8,0 mm | Individuelle Berechnung | 8,0 mm |

**Hinweis:** Aluminiumtanks benötigen ca. 50–70% höhere Wandstärken als 316L-Tanks gleichen Volumens, da die Streckgrenze von 5083-O (125 MPa) nur ca. 73% der Streckgrenze von 316L (170 MPa) beträgt und zusätzlich ein Korrosionszuschlag von 0,5–1,0 mm einkalkuliert werden muss.

**Kosten (Stand 2025/2026, Richtwerte):**

| Position | Preis | Einheit |
|----------|-------|---------|
| 5083-O Blech 3mm | 18–28 EUR | pro kg |
| 5083-O Blech 5mm | 16–25 EUR | pro kg |
| Fertigtank einfach (rechteckig, bis 200l) | 800–1.800 EUR | pro Stück |
| Fertigtank komplex (L-Form, Schotten, >400l) | 2.200–5.500 EUR | pro Stück |
| Maßanfertigung Superyacht (>1.000l) | 4.000–12.000 EUR | pro Stück |
| WIG-Schweißarbeit Alu-Fachbetrieb | 90–150 EUR | pro Stunde |

**Galvanische Isolation — KRITISCH:**

Aluminium hat ein Standardpotenzial von -1,66 V (vs. SHE) und ist damit eines der unedelsten Gebrauchsmetalle. Bei direktem Kontakt mit edleren Metallen (Edelstahl, Bronze, Kupfer) in Anwesenheit eines Elektrolyts (Salzwasser, Kondenswasser) wird Aluminium zur Opferanode und korrodiert rapide.

**Erforderliche Isolationsmaßnahmen:**
- Tankhalterungen aus Edelstahl: Neopren- oder EPDM-Pads (min. 3mm) zwischen Tank und Halterung
- Schlauchschellen: Nur Edelstahl mit Gummieinlage, niemals direkt auf Aluminium
- Tankanschlüsse: Aluminium-Fittings oder galvanisch isolierte Übergänge
- Kein Kupferrohr direkt an Aluminium-Tank — IMMER Isolierstück oder Kunststoff-Zwischenstück
- Keine Edelstahl-Schrauben direkt in Aluminium — Isolierbuchsen verwenden oder Aluminium-Schrauben

#### 2.1.3 GFK (Glasfaserverstärkter Kunststoff) / FRP

**Werkstoffbezeichnung:** GFK (Glasfaserverstärkter Kunststoff), engl. FRP (Fiber Reinforced Plastic) oder GRP (Glass Reinforced Plastic)

GFK-Kraftstofftanks werden entweder als eigenständige Tanks laminiert oder als integraler Bestandteil des Rumpfes (sog. "Integrationstanks" oder "strukturelle Tanks") ausgeführt. Letztere nutzen den Rumpf selbst als Tankwand — eine Bauweise, die besonders im Serienbootsbau verbreitet ist, da sie Gewicht und Kosten spart.

**Harzsysteme für Kraftstofftanks:**

| Harz | Kraftstoffbeständigkeit | Osmosebeständigkeit | Kosten | Empfehlung |
|------|------------------------|--------------------:|--------|------------|
| Isophthal-Polyester | Befriedigend | Gut | Niedrig | Nur Diesel, nicht Benzin |
| Vinylester (z.B. Derakane 411) | Sehr gut | Sehr gut | Mittel | Standard für Kraftstofftanks |
| Epoxid (z.B. WEST System) | Hervorragend | Hervorragend | Hoch | Premium, alle Kraftstoffe |
| Orthophthal-Polyester | Mangelhaft | Mangelhaft | Sehr niedrig | NICHT für Kraftstofftanks! |

**WARNUNG:** Orthophthal-Polyester (Standard-Bootsbau-Harz) ist NICHT geeignet für Kraftstofftanks. Dieses Harz wird von Benzin und Ethanol-haltigen Kraftstoffen (E10, E15) angegriffen — es quillt, erweicht und verliert seine strukturelle Integrität. Auch für Dieseltanks ist es nur bedingt geeignet, da Dieselkraftstoff nach EN 590 bis zu 7% Biodiesel (FAME) enthalten darf, der Orthophthal-Polyester angreift.

**Laminataufbau für einen Diesel-Kraftstofftank (Vinylester):**

| Lage | Material | Gewicht | Funktion |
|------|----------|---------|----------|
| 1 (innen) | Vinylester-Gelcoat, 0,5mm | 800 g/m² | Chemische Barriere |
| 2 | Vinylester + CSM 300 g/m² | – | Haftvermittlung |
| 3 | Vinylester + Biaxialgelege 600 g/m² | – | Strukturelle Lage |
| 4 | Vinylester + CSM 450 g/m² | – | Füllschicht |
| 5 | Vinylester + Biaxialgelege 800 g/m² | – | Hauptstrukturlage |
| 6 | Vinylester + CSM 450 g/m² | – | Füllschicht |
| 7 | Vinylester + Biaxialgelege 600 g/m² | – | Strukturelle Lage |
| 8 (außen) | Vinylester-Topcoat | – | Schutzschicht |

Gesamtlaminatdicke: ca. 5–6 mm
Glasgehalt: 35–45 Gew.-%
Zugfestigkeit: ca. 150–200 MPa
Biegefestigkeit: ca. 200–280 MPa

**Integrationstanks (Rumpf als Tankwand):**

Bei Integrationstanks bilden eine oder mehrere Rumpfwände gleichzeitig die Tankwand. Diese Bauweise ist im Serienbootsbau (Bavaria, Beneteau, Jeanneau, Hanse) weit verbreitet und bietet signifikante Vorteile:

- **Gewichtsersparnis:** 30–50% weniger Tankgewicht vs. separater Metalltank
- **Volumennutzung:** Maximale Ausnutzung der Rumpfform, keine "verlorenen" Zwischenräume
- **Kosten:** Wird in einem Arbeitsgang mit dem Rumpf laminiert, keine separate Tankfertigung
- **Schwerpunktlage:** Tank kann optimal im Schiffsrumpf positioniert werden (tief, mittig)

**Risiken von Integrationstanks:**
- Leckage = Rumpfschaden — ein undichter Integrationstank kontaminiert das gesamte Rumpflaminat
- Reparatur extrem aufwändig — der Tank ist der Rumpf, ein "Austausch" ist faktisch unmöglich
- Osmose der Innenseite: Kraftstoff (besonders Diesel mit Biodiesel-Anteil) kann das Laminat angreifen
- Geruchsprobleme: Diesel permeiert durch unzureichend abgesperrtes Laminat

**Kosten (Stand 2025/2026, Richtwerte):**

| Position | Preis | Einheit |
|----------|-------|---------|
| Vinylester-Harz (Derakane 411) | 12–18 EUR | pro kg |
| Biaxialgelege 600 g/m² | 4–7 EUR | pro m² |
| Fertig laminierter Einzeltank (bis 200l) | 600–1.500 EUR | pro Stück |
| Integrationstank (Werftproduktion, 200–500l) | 400–1.000 EUR | Mehrkosten vs. Standard-Rumpf |
| Inspektions-/Revisionsöffnung nachrüsten | 300–800 EUR | pro Stück |

#### 2.1.4 PE-HD (Polyethylen hoher Dichte)

**Werkstoffbezeichnung:** PE-HD (High Density Polyethylene), PE 100, PE 80

PE-HD-Tanks werden im Rotationsschmelzverfahren (Rotomoulding) hergestellt — ein Verfahren, bei dem Polyethylen-Granulat in einer rotierenden, beheizten Form gleichmäßig verteilt wird und nahtlose, einteilige Tanks erzeugt. Dies eliminiert Schweißnähte als potenzielle Schwachstellen.

**Materialeigenschaften:**

| Eigenschaft | Wert | Prüfnorm |
|------------|------|----------|
| Dichte | 0,94–0,96 g/cm³ | ISO 1183 |
| Zugfestigkeit | 22–30 MPa | ISO 527 |
| Streckgrenze | 18–25 MPa | ISO 527 |
| Bruchdehnung | >600% | ISO 527 |
| E-Modul | 800–1.400 MPa | ISO 527 |
| Shore-Härte | D 60–65 | ISO 868 |
| Vicat-Erweichungstemperatur | 75–85°C | ISO 306 |
| Dauerbetriebstemperatur | -50 bis +60°C | – |
| UV-Beständigkeit (ohne Stabilisator) | Gering | – |
| UV-Beständigkeit (carbon black stabilisiert) | Gut | – |
| Kraftstoffpermeation (Diesel) | <0,5 g/(m²·d) | SAE J2665 |
| Kraftstoffpermeation (Benzin) | 2–8 g/(m²·d) | SAE J2665 |

**WARNUNG — Benzinpermeation:** PE-HD ist für Benzin grundsätzlich geeignet, hat aber eine signifikant höhere Permeationsrate als für Diesel. Die US-amerikanische EPA (Environmental Protection Agency) hat seit 2012 strenge Permeationsgrenzen für marine Benzintanks eingeführt (≤1,5 g/m²/Tag). Moderne PE-HD-Benzintanks müssen daher eine Fluorierung oder Sulfonierung der Innenwand aufweisen, um die Permeation zu reduzieren. Nicht-fluorierte PE-Tanks sind in den USA für Benzin seit 2012 nicht mehr zugelassen.

**Fluorierung:**
Bei der Fluorierung wird die Innenwand des PE-Tanks mit elementarem Fluor (F₂) behandelt. Das Fluor ersetzt Wasserstoffatome in der PE-Oberfläche und erzeugt eine dünne (5–50 µm) Fluorpolymer-Schicht, die als Barriere gegen Kraftstoffpermeation wirkt. Die Permeationsrate sinkt um Faktor 50–100.

| Typ | Permeation Benzin | Permeation Diesel | Kosten-Aufschlag |
|-----|-------------------|-------------------|-----------------|
| PE-HD unbehandelt | 2–8 g/(m²·d) | 0,3–0,5 g/(m²·d) | – |
| PE-HD fluoriert | 0,05–0,15 g/(m²·d) | <0,01 g/(m²·d) | +15–25% |
| PE-HD sulfoniert | 0,1–0,3 g/(m²·d) | <0,05 g/(m²·d) | +10–20% |

**Wandstärken für PE-HD Kraftstofftanks:**

| Tankvolumen | Empfohlene Wandstärke | Minimale Wandstärke | Bodenbereich |
|-------------|----------------------|--------------------:|-------------|
| bis 50 l | 5 mm | 4 mm | 6 mm |
| 50–120 l | 6 mm | 5 mm | 7 mm |
| 120–250 l | 7 mm | 6 mm | 8 mm |
| 250–500 l | 8 mm | 7 mm | 10 mm |
| 500–1.000 l | 10 mm | 8 mm | 12 mm |

**Kosten (Stand 2025/2026, Richtwerte):**

| Position | Preis | Einheit |
|----------|-------|---------|
| Standardtank 60l rechteckig | 120–200 EUR | pro Stück |
| Standardtank 120l rechteckig | 180–320 EUR | pro Stück |
| Standardtank 200l | 280–480 EUR | pro Stück |
| Sonderform (Rotomoulding-Werkzeug) | 3.000–8.000 EUR | einmalig |
| Sonderform Tank (ab 50 Stk.) | 150–350 EUR | pro Stück |
| Fluorierung (nachträglich) | 80–200 EUR | pro Tank |

**Vorteile:**
- Keine Korrosion — weder durch Kraftstoff noch durch Salzwasser
- Nahtlos (Rotomoulding) — keine Schweißnähte als Schwachstellen
- Leicht (Dichte 0,95 g/cm³ — ca. ⅓ von Aluminium, ⅛ von Edelstahl)
- Kostengünstig in Serie
- Schlagzäh und elastisch — absorbiert Stöße ohne Rissbildung
- Kein galvanisches Problem mit anderen Metallen
- FDA-konform (bei entsprechender Qualität auch für Trinkwasser)

**Nachteile:**
- Begrenzte Formstabilität bei Wärme (>60°C → Erweichung)
- Nicht reparabel durch Schweißen im Feld (Rotomoulding-Tank kann nicht geschweißt werden)
- Permeation bei Benzin ohne Fluorierung zu hoch
- UV-empfindlich ohne Carbon-Black-Stabilisierung
- Niedrige Festigkeit (22–30 MPa vs. 275 MPa bei Alu 5083) — erfordert massive Wandstärken
- Befestigung schwierig — Bohrungen schwächen den Tank, Bänder/Gurte bevorzugt
- Maximale Tankgröße durch Rotomoulding-Maschine begrenzt (typisch bis 1.000l)
- Nicht für Biodiesel >B20 zugelassen (FAME weicht PE auf)

### 2.2 Normentechnische Grundlagen

#### 2.2.1 ISO 21487:2012 — Wassersport — Fest eingebaute Kraftstofftanks aus Kunststoff

Dies ist die zentrale europäische Norm für Kraftstofftanks aus Kunststoff (PE, GFK) in Sportbooten. Sie definiert Anforderungen an Material, Konstruktion, Prüfung und Kennzeichnung.

**Geltungsbereich:**
- Fest eingebaute Kraftstofftanks aus Kunststoff in Sportbooten nach EU-Sportbootrichtlinie 2013/53/EU
- Tankvolumen 25 l bis 1.500 l
- Diesel und Benzin
- Nicht: Metalltanks (→ ISO 21487 verweist auf ISO 10088), Beiboottanks, tragbare Tanks

**Wesentliche Anforderungen:**

| Abschnitt | Anforderung | Prüfung |
|-----------|-------------|---------|
| 5.2 | Mindestwandstärke je nach Volumen und Material | Messung |
| 5.3 | Kraftstoffbeständigkeit: 28 Tage Lagerung in Referenzkraftstoff bei 40°C | Masseverlust <5%, keine sichtbare Degradation |
| 5.4 | Druckprüfung: 0,3 bar Überdruck, 5 min, keine Leckage | Hydrostatisch |
| 5.5 | Schlagprüfung: 3 kg Fallhammer, 1 m Höhe, bei -18°C | Keine Rissbildung |
| 5.6 | Flammenbeständigkeit: Selbsterlöschend innerhalb 10 s nach Flammenentfernung | UL 94 V-0 |
| 5.7 | Permeation: <100 g/m²/24h bei 40°C (Benzin) | Gewichtsverlust-Methode |
| 5.8 | UV-Beständigkeit (wenn exponiert): 1.000 h Xenon-Belichtung, keine Rissbildung | ISO 4892-2 |
| 5.9 | Kennzeichnung: Hersteller, Baujahr, Volumen, Kraftstoffart, Norm | Sichtprüfung |
| 5.10 | Anschlüsse: Verstärkte Bereiche, min. 2× Wandstärke im Anschlussbereich | Messung |

#### 2.2.2 ISO 10088:2013 — Wassersport — Fest eingebaute Kraftstoffsysteme

Diese Norm deckt das gesamte Kraftstoffsystem ab — von Tank über Leitungen bis Entlüftung. Für Tanks definiert sie:

**Tankspezifische Anforderungen aus ISO 10088:**

| Anforderung | Spezifikation |
|------------|---------------|
| Tankbefestigung | Muss 4g Beschleunigung in jeder Richtung standhalten |
| Schwallbleche | Erforderlich bei Tanks >750mm in einer Dimension |
| Inspektionsöffnung | Mind. 100mm × 150mm, bei Tanks >200l empfohlen |
| Entlüftung | Jeder Tank muss eine Entlüftung haben, die Überdruckaufbau verhindert |
| Füllstutzen | Muss Überfüllung verhindern (Siphon oder automatische Absperrung) |
| Entnahme | Nicht durch die Tankuntenseite — Siphon- oder Top-Feed-Entnahme |
| Füllstandsanzeige | Jeder fest eingebaute Tank >60l muss eine Füllstandsanzeige haben |
| Rücklauf | Rücklaufleitung muss unterhalb des Kraftstoffniveaus enden |
| Erdung | Metalltanks: galvanische Verbindung zum Motorblock und Bordnetz-Masse |

#### 2.2.3 ABYC H-24 — Gasoline Fuel Systems

ABYC H-24 ist der US-amerikanische Standard für Benzin-Kraftstoffsysteme auf Booten. Er wird von der USCG (United States Coast Guard) als Konformitätsnachweis akzeptiert und ist de facto Pflichtstandard für den US-Markt.

**Wesentliche Anforderungen (Auszug):**

| Anforderung | Spezifikation |
|------------|---------------|
| Tanktest | 3 psi (0,21 bar) Drucktest, 2 min, keine Leckage |
| Tankmaterial | Bauart-/Brandprüfung nach USCG 33 CFR 183.510 ff. (Metalltanks: kein Terneplate; Edelstahl nur 316L/317L); Kunststofftanks zusätzlich EPA-Permeationsnachweis (40 CFR 1060). SAE J1527 gilt nur für Kraftstoffschläuche, nicht für Tanks |
| Tankbefestigung | Muss 3g lateral, 3g longitudinal, 3g vertikal standhalten |
| Schwallbleche (Baffles) | Bei Tanks >35 gal (132l) in jeder Richtung >30" (762mm) |
| Tankentlüftung | Muss in geschützten Bereich außenbords führen |
| Füllleitung | Muss direkt in Tank führen, kein offener Trichter |
| Label | Permanent: "GASOLINE", Volumen, Hersteller, Baujahr, Norm |
| Metalltanks | Erdung an Motorblock und Bordnetz, max. 1 Ohm |
| PE-Tanks | Fluoriert oder sulfoniert, Permeation <1,5 g/m²/Tag |

> ✅ Aufgelöst (Audit): SAE J1527 ist „Marine Fuel Hoses" (Kraftstoffschläuche für Sportboote unter 33 CFR 183 Subpart J), kein Tankwerkstoff-Standard — Fehlreferenz bestätigt und an beiden Stellen (hier + Vergleichsmatrix 13.9) korrigiert auf USCG 33 CFR 183.510 ff. (Bauart-/Brandprüfung) bzw. EPA 40 CFR 1060 (Permeation für Kunststofftanks). Quelle: SAE J1527:2022 „Marine Fuel Hoses" (sae.org); USCG 33 CFR 183 Subpart J.

#### 2.2.4 ABYC H-33 — Diesel Fuel Systems

ABYC H-33 ist das Pendant zu H-24 für Diesel-Systeme. Die Anforderungen sind in einigen Bereichen weniger streng, da Diesel nicht explosionsfähig bei Raumtemperatur ist.

**Unterschiede zu H-24 (Benzin):**

| Bereich | H-24 (Benzin) | H-33 (Diesel) |
|---------|---------------|---------------|
| Entlüftung nach außen | Pflicht, mit Rückschlagventil | Pflicht, ohne Rückschlagventil |
| Ignition Protection | Alle Komponenten im Tankbereich | Nicht erforderlich |
| Flammensperre | In Entlüftungsleitung erforderlich | Nicht erforderlich |
| PE-Tank Fluorierung | Pflicht | Empfohlen, nicht Pflicht |
| Drucktest | 3 psi (0,21 bar) | 3 psi (0,21 bar) — identisch |
| Schwallbleche | Bei >35 gal und >30" | Bei >35 gal und >30" — identisch |

#### 2.2.5 ISO 21487:2012 — Metallische Kraftstofftanks für Boote

> ⚠️ **KORREKTUR (Audit):** Dieser Abschnitt war ursprünglich „EN 13317:2002 — Metallische Kraftstofftanks für Boote" zugeordnet. EN 13317 regelt jedoch **Mannloch-Deckel für Gefahrgut-Straßentankfahrzeuge** (ADR-Serviceausrüstung), NICHT Boots-Kraftstofftanks. Der korrekte Standard für fest eingebaute metallische Kraftstofftanks in Sportbooten ist **ISO 21487**, der ausdrücklich sowohl Kunststoff- als auch Metalltanks (Aluminium, Edelstahl) abdeckt. Quellen: SIS/BSI EN 13317:2018 „Tanks for transport of dangerous goods — Manhole cover assembly"; ISO 21487:2012/2022 (iso.org).
> ✅ Aufgelöst (Audit): Gegen ISO 21487:2022 (§7.2.2 + Tabelle 1) abgeglichen. Prüfdrücke sind methodenabhängige Mindestwerte — Standardmethode ≥20 kPa (0,2 bar), Alternativmethode ≥30 kPa (0,3 bar), jeweils der größere Wert aus Mindestdruck bzw. 1,5× hydrostatischem Druck, gehalten 5 min (nicht die zuvor angegebenen fixen 0,35 bar). Mindestwandstärken nach Tab. 1: Edelstahl 1,0 mm (Schweißnahtüberhöhung entfernt), Aluminium ≤0,1% Cu 2,0 mm. Werte auf documented (ISO-Original) aktualisiert. Quelle: ISO 21487:2022 §7.2.2/Tab. 1 (iso.org).

ISO 21487 gilt sowohl für Kunststoff- als auch für metallische Tanks und definiert für metallische Tanks u. a. folgende Anforderungen:

| Anforderung | Edelstahl 316L | Aluminium 5083 |
|------------|---------------|----------------|
| Min. Wandstärke | 1,0 mm (ISO 21487 Tab. 1, Schweißnahtüberhöhung entfernt) | 2,0 mm (ISO 21487 Tab. 1, Alu-Legierung ≤0,1% Cu) |
| Schweißnahtprüfung | 100% Sichtprüfung, Drucktest | 100% Sichtprüfung, Drucktest |
| Drucktest | ≥20 kPa (0,2 bar) Standard- bzw. ≥30 kPa (0,3 bar) Alternativmethode, 5 min | ≥20 kPa (0,2 bar) Standard- bzw. ≥30 kPa (0,3 bar) Alternativmethode, 5 min |
| Korrosionstest | 1.000h Salzsprühtest (ASTM B117) | 1.000h Salzsprühtest (ASTM B117) |
| Schweißerqualifikation | EN ISO 9606-1 | EN ISO 9606-2 |
| Werkstoffzeugnis | 3.1 nach EN 10204 | 3.1 nach EN 10204 |

### 2.3 Tankformen und Integration

#### 2.3.1 Standardformen

**Rechteckig (Quader):**
Die einfachste und kostengünstigste Tankform. Geeignet für Bereiche mit geradliniger Geometrie (Maschinenraum-Boden, unter Kabinensofas).

- Vorteile: Einfache Fertigung, genaue Volumenberechnung, einfache Befestigung
- Nachteile: Schlechte Raumausnutzung in Rumpfformen mit Kurven
- Typisches Volumen: 50–600 l
- Typische Anwendung: Maschinenraum, unter Boden, Achterschiff

**L-förmig:**
Ein Quader mit einer Stufe — ermöglicht die Anpassung an Rumpfstrukturen oder Durchgänge.

- Vorteile: Bessere Raumausnutzung als Quader, ein Fertigungsstück
- Nachteile: Spannungskonzentration an der Innenkante, teurere Fertigung
- Typisches Volumen: 100–800 l
- Typische Anwendung: Um Wellentunnel herum, unter Niedergang

**Keilförmig (Trapez):**
Passt sich an die V-Form des Rumpfbugs oder an schräge Bodenflächen an.

- Vorteile: Optimale Raumausnutzung im Vorschiff oder Achterschiff
- Nachteile: Komplexe Fertigung, Schwallbleche schwieriger zu integrieren
- Typisches Volumen: 80–400 l
- Typische Anwendung: Vorschiff (Segelyachten), Achterschiff (Motorboote)

**Sattelförmig (Saddle Tank):**
Zwei Tankhälften links und rechts des Kiels, verbunden durch einen Überlauf oder Ausgleichsleitung.

- Vorteile: Tiefer Schwerpunkt, symmetrische Gewichtsverteilung
- Nachteile: Zwei separate Tankhälften erfordern Ausgleichssystem, doppelte Anschlüsse
- Typisches Volumen: 200–2.000 l (pro Seite)
- Typische Anwendung: Segelyachten >12m, große Motorboote

**Rumpfintegriert (Structural Tank):**
Der Rumpf selbst bildet eine oder mehrere Tankwände. Nur bei GFK-Booten möglich.

- Vorteile: Maximale Volumenausnutzung, minimales Gewicht
- Nachteile: Nicht austauschbar, Leckage = Rumpfschaden, schwierige Inspektion
- Typisches Volumen: 100–1.500 l
- Typische Anwendung: Serienyachten (Bavaria, Beneteau, Jeanneau, Hanse)

#### 2.3.2 Tankpositionierung im Boot

Die Position des Kraftstofftanks hat direkten Einfluss auf Stabilität, Trimm und Seetüchtigkeit:

| Position | Vorteile | Nachteile | Typische Anwendung |
|----------|----------|-----------|-------------------|
| Mittschiffs, tief | Minimaler Einfluss auf Trimm, tiefer Schwerpunkt | Zugang schwierig, Bilge-Nähe | Segelyachten 10–15m |
| Achterschiff, unter Boden | Nähe zum Motor, kurze Leitungen | Hecklastigkeit bei vollem Tank | Motorboote 8–14m |
| Seitlich (Sattel) | Symmetrie, tief, gute Verteilung | Krängung bei ungleichem Verbrauch | Segelyachten >12m |
| Vorschiff | Trimm-Ausgleich bei schwerem Motor achtern | Slamming-Belastung, langer Leitungsweg | Verdränger-Motorboote |
| Unter Kabinenboden | Gute Raumnutzung, unsichtbar | Geruchsprobleme, Zugang schwierig | Serienyachten |
| Cockpit-Locker | Guter Zugang, achtern | Hebt Schwerpunkt, Volumen begrenzt | Kleinboote, Beiboote |

**Trimm-Berechnung:**

Der Einfluss eines Tanks auf den Trimm berechnet sich wie folgt:

```
Trimm-Moment [kg·m] = Tankinhalt [kg] × Abstand_von_Mittschiffs [m]
Trimm-Änderung [°] = Trimm-Moment / (Δ × GM_L)

wobei:
  Δ = Verdrängung des Bootes [kg]
  GM_L = Longitudinale metazentrische Höhe [m]
```

Beispiel: 400 l Diesel (336 kg) in einem Tank 2,5 m achterlich von Mittschiffs auf einer 12-m-Yacht mit 8.000 kg Verdrängung und GM_L = 8 m:

```
Trimm-Moment = 336 × 2,5 = 840 kg·m
Trimm-Änderung = 840 / (8.000 × 8) = 0,013 rad ≈ 0,75°
```

Dies liegt unter der kritischen Grenze von 1° für Motorboote, ist aber bei einer Segelyacht bereits spürbar.

### 2.4 Belüftung und Druckausgleich

#### 2.4.1 Grundprinzip

Jeder geschlossene Kraftstofftank muss eine Belüftung haben. Ohne Belüftung entstehen beim Betanken Überdruck (→ Kraftstoff tritt am Einfüllstutzen aus) und beim Verbrauch Unterdruck (→ Motor bekommt keinen Kraftstoff, Tankwand kann einbeulen).

**Physikalische Grundlagen:**

| Vorgang | Druckänderung | Erforderlich |
|---------|---------------|-------------|
| Betanken | +0,1–0,3 bar (Überdruck) | Entlüftung nach außen |
| Kraftstoffverbrauch | -0,05–0,15 bar (Unterdruck) | Belüftung von außen |
| Temperaturanstieg (+20°C) | +0,02–0,08 bar (Dampfausdehnung + Flüssigkeitsausdehnung) | Entlüftung |
| Temperaturabfall (-20°C) | -0,02–0,06 bar (Dampfkontraktion) | Belüftung |
| Seegang (dynamisch) | ±0,01–0,05 bar | Belüftung (verhindert "Tankatmung") |

**Dimensionierung der Entlüftungsleitung:**

Die Entlüftungsleitung muss den Volumenstrom der Tankbefüllung bewältigen können. Faustformel:

```
Entlüftungs-Innendurchmesser [mm] = √(Füllrate [l/min] × 4 / (π × v_max))

wobei v_max = 2 m/s (maximale Strömungsgeschwindigkeit in der Entlüftung)
```

| Füllrate | Min. Innendurchmesser | Empfohlener Schlauch |
|----------|----------------------|---------------------|
| 20 l/min (tragbare Kanister) | 10 mm | 16 mm ID |
| 40 l/min (Marina-Zapfsäule, langsam) | 14 mm | 16 mm ID |
| 80 l/min (Marina-Zapfsäule, schnell) | 20 mm | 25 mm ID |
| 120 l/min (Bunkerstation, schnell) | 25 mm | 32 mm ID |

#### 2.4.2 Entlüftungsführung

**Benzintanks — ABYC H-24 / ISO 10088:**
- Entlüftung MUSS nach außenbords führen
- Entlüftungsöffnung im Freien, mind. 375 mm von jeder Öffnung ins Schiffsinnere
- Entlüftungsöffnung darf nicht in Cockpit, Kabine oder Maschinenraum münden
- Flammensperre (Drahtgeflecht min. 30 Maschen/cm) an der Außenöffnung — PFLICHT bei Benzin
- U-Bogen oder Anti-Siphon-Schleife in der Leitung — verhindert Wassereinlass bei Krängung
- Entlüftungsleitung muss stetig steigend verlegt sein — keine Tiefpunkte, in denen sich Kraftstoff sammelt

**Dieseltanks — ABYC H-33 / ISO 10088:**
- Entlüftung MUSS nach außenbords führen
- Flammensperre empfohlen, aber nicht vorgeschrieben
- Ansonsten identische Anforderungen wie Benzin

**Typische Verlegung:**

```
Tank → Schwanenhals (U-Bogen, min. 200mm über Wasserlinie) → 
  Entlüftungsleitung (stetig steigend, min. 16mm ID) → 
    Außenborddurchführung (Flammensperre bei Benzin) → 
      Außenöffnung (nach unten weisend, gegen Spritzwasser geschützt)
```

#### 2.4.3 Tankdruckventile

Moderne Tanksysteme verwenden zusätzlich Druckventile (Pressure/Vacuum Relief Valves, P/V-Ventile), die als Sicherheitseinrichtung den Tank vor Über- und Unterdruck schützen:

| Parameter | Typischer Wert | Funktion |
|-----------|---------------|----------|
| Öffnungsdruck (Überdruck) | +0,15–0,25 bar | Verhindert Tankbersten bei blockierter Entlüftung |
| Öffnungsdruck (Unterdruck) | -0,05–0,10 bar | Verhindert Tankimplosion |
| Durchfluss bei Öffnung | 20–80 l/min Luft | Muss Betankungsrate entsprechen |
| Material | Edelstahl 316 + PTFE-Dichtung | Kraftstoffbeständig |

**Hersteller und Modelle:**

| Hersteller | Modell | Anschluss | Druckbereich | Preis (ca.) |
|-----------|--------|-----------|-------------|-------------|
| Vetus | TANKVENT | 16mm Tülle | +0,2/-0,05 bar | 35–55 EUR |
| Vetus | TANKVENT38 | 38mm Gewinde | +0,2/-0,05 bar | 55–75 EUR |
| Racor (Parker) | RK 21070 | ¾" NPT | +0,15/-0,08 bar | 65–95 USD |
| Perko | 0594 | 5/8" Hose | +0,20/-0,06 bar | 45–70 USD |
| Wema | VE-VENT | 16mm Tülle | +0,15/-0,05 bar | 40–60 EUR |

---

## 3. Typenübersicht

### 3.1 Einbautanks aus Edelstahl 316L

**Beschreibung:**
Geschweißte Tanks aus 316L-Edelstahlblech, maßgefertigt oder als Standardgrößen erhältlich. Werden typisch in Halterungen aus Flachstahl oder Winkelprofil montiert, auf Gummi- oder Neoprenpads gelagert und mit Spannbändern gesichert.

**Konstruktionsmerkmale:**

| Merkmal | Spezifikation |
|---------|---------------|
| Schweißverfahren | WIG (TIG), durchgehend verschweißt, nicht punktgeschweißt |
| Schweißnahtqualität | Durchgeschweißt, wurzelseitig formiert, gebeizt |
| Schwallbleche | Ab 750mm Tankdimension, 50–70% der Querschnittsfläche, gelocht |
| Inspektionsöffnung | Ab 200l empfohlen, ab 500l Pflicht, min. 100×150mm |
| Anschlüsse | Eingeschweißte 316L-Stutzen mit BSP- oder NPT-Gewinde |
| Tankgeber-Öffnung | 5-Loch-Flansch (SAE Standard) oder metrisch M5 |
| Füllstutzen | 38mm (1½") oder 50mm (2") Innengewinde, oben |
| Entlüftung | 16mm oder 19mm Stutzen, oben |
| Entnahme | Stutzen oben (mit Steigrohr) oder seitlich (oberhalb Bodenniveau) |
| Rücklauf | Separater Stutzen, oben, ggf. mit Beruhigungsrohr |
| Ablassventil | Stutzen am tiefsten Punkt, mit Kugelhahn |
| Oberflächenbehandlung | Gebeizt und passiviert, optional elektropoliert |

**Tankgeber-Integration:**

Die meisten Edelstahltanks werden mit einem Standard-5-Loch-Flansch (SAE J1810) für den Tankgeber geliefert. Die Lochabstände und Bolzenkreise variieren:

| Standard | Bolzenkreis | Lochanzahl | Lochgröße | Verbreitung |
|----------|------------|-----------|-----------|-------------|
| SAE 5-Bolt | 130mm | 5 | M5 | USA, international |
| Metrisch | 120mm | 5 | M5 | Europa |
| VDO/Continental | 54mm | 5 | M4 | Europa, Standardgeber |
| Wema/SSI | 54mm | 5 | M4 | Europa (kompatibel mit VDO) |

**Typische Maße und Gewichte (leer, ohne Anschlüsse):**

| Volumen | Abmessungen L×B×H (mm) | Wandstärke | Leergewicht | Befüllt (Diesel) |
|---------|------------------------|-----------|------------|------------------|
| 60 l | 500×400×350 | 1,5 mm | 12 kg | 62 kg |
| 120 l | 600×500×450 | 2,0 mm | 22 kg | 123 kg |
| 200 l | 800×500×550 | 2,0 mm | 30 kg | 198 kg |
| 300 l | 900×600×600 | 2,5 mm | 42 kg | 294 kg |
| 500 l | 1100×700×700 | 2,5 mm | 62 kg | 482 kg |
| 800 l | 1300×800×800 | 3,0 mm | 88 kg | 760 kg |
| 1.200 l | 1500×900×900 | 3,0 mm | 115 kg | 1.123 kg |

### 3.2 Einbautanks aus Aluminium 5083

**Beschreibung:**
Geschweißte Tanks aus 5083-Aluminiumblech. Leichter als Edelstahl, aber anfälliger für Korrosion bei fehlerhafter Installation (galvanischer Kontakt). Standard im US-Bootsbau, in Europa weniger verbreitet.

**Konstruktionsmerkmale:**

| Merkmal | Spezifikation |
|---------|---------------|
| Schweißverfahren | WIG (TIG) mit AlMg5 (5183) Zusatz, NIEMALS AlSi5 (4043) |
| Schweißnahtqualität | Durchgeschweißt, wurzelseitig formiert |
| Schwallbleche | Ab 750mm Tankdimension, identisch zu Edelstahl |
| Inspektionsöffnung | Ab 200l empfohlen, min. 100×150mm |
| Anschlüsse | Eingeschweißte Alu-Stutzen mit NPT-Gewinde |
| Oberflächenbehandlung | Eloxiert (Innen + Außen) oder ölgetränkt |
| Galvanische Isolation | Neopren-Pads an allen Kontaktstellen, keine Kontaktmetalle |
| Tankgeber-Öffnung | SAE 5-Bolt-Flansch, eingeschweißt |

**Typische Maße und Gewichte (leer):**

| Volumen | Abmessungen L×B×H (mm) | Wandstärke | Leergewicht | Befüllt (Diesel) |
|---------|------------------------|-----------|------------|------------------|
| 60 l | 500×400×350 | 2,5 mm | 5 kg | 55 kg |
| 120 l | 600×500×450 | 3,0 mm | 9 kg | 110 kg |
| 200 l | 800×500×550 | 3,0 mm | 13 kg | 181 kg |
| 300 l | 900×600×600 | 4,0 mm | 20 kg | 272 kg |
| 500 l | 1100×700×700 | 4,0 mm | 30 kg | 450 kg |
| 800 l | 1300×800×800 | 5,0 mm | 48 kg | 720 kg |

### 3.3 Einbautanks aus GFK

**Beschreibung:**
Laminierte Tanks aus glasfaserverstärktem Kunststoff, typischerweise mit Vinylester- oder Epoxidharz. Entweder als separate Tanks gefertigt oder als Rumpf-Integrationstanks.

**Konstruktionsmerkmale (separater GFK-Tank):**

| Merkmal | Spezifikation |
|---------|---------------|
| Harz | Vinylester (Standard) oder Epoxid (Premium) |
| Laminataufbau | Min. 5mm Wandstärke, CSM + Biaxialgelege |
| Innenschicht | Vinylester-Gelcoat 0,5mm als Barriere |
| Schwallbleche | Einlaminierte GFK-Schotten |
| Inspektionsöffnung | Einlaminierter GFK-Flansch mit Schraubdeckel |
| Anschlüsse | Einlaminierte Anschlussplatten (Edelstahl oder GFK) |
| Tankgeber | Einlaminierter Flansch, oben |
| Verstärkungen | Laminiertaschen an allen Anschlusspunkten, min. 2× Wandstärke |

**Integrationstanks — Serienfertigung:**

Bei Serienbooten werden Integrationstanks typisch wie folgt gebaut:

1. Rumpf wird in der Form laminiert (Standard-Laminat)
2. Tankbereich erhält zusätzliche Vinylester-Barriereschicht (Innenseite)
3. Schwallbleche und Trennschotten werden einlaminiert
4. Anschlussplatten werden einlaminiert
5. Tankdeckel wird separat laminiert und aufgeklebt/verschraubt
6. Drucktest vor Endmontage

**Typische Wandstärken Integrationstanks:**

| Bereich | Wandstärke | Laminat |
|---------|-----------|---------|
| Rumpfwand (= Tankwand) | 8–15 mm | Rumpflaminat + Barriere |
| Tankdeckel (oben) | 6–10 mm | Separates Laminat |
| Schwallbleche | 4–6 mm | Einlaminiert |
| Anschlussplatten | 10–15 mm | Verstärktes Laminat |

### 3.4 Flexible Tanks (Bladder)

**Beschreibung:**
Flexible Kraftstofftanks bestehen aus einer kraftstoffbeständigen Membran (typisch PU-beschichtetes Nylon oder CSM-Kautschuk), die in eine vorbereitete Mulde oder einen Kasten gelegt wird. Sie passen sich an unregelmäßige Raumformen an und können durch kleine Öffnungen eingeführt werden.

**Einsatzgebiete:**
- Nachrüstung in bestehende Boote (durch kleine Luken einführbar)
- Ersatz für korrodierte Metalltanks ohne Rumpföffnung
- Temporäre Kapazitätserweiterung (Langfahrt)
- Bereiche mit schwierigen Geometrien (unter Kojen, in Bilgen)

**Materialien:**

| Material | Kraftstoffbeständigkeit | Temperaturbereich | Lebensdauer | Kosten |
|----------|------------------------|-------------------|-------------|--------|
| PU/Nylon (Polyurethan auf Nylon) | Diesel: sehr gut, Benzin: gut | -20 bis +65°C | 10–15 Jahre | Mittel |
| CSM/Hypalon auf Nylon | Diesel: hervorragend, Benzin: sehr gut | -30 bis +80°C | 12–18 Jahre | Hoch |
| XLPE (vernetztes PE) | Diesel: gut, Benzin: befriedigend | -20 bis +55°C | 8–12 Jahre | Niedrig |
| Nitrile/Nylon | Diesel: gut, Benzin: sehr gut | -20 bis +70°C | 10–15 Jahre | Mittel |

**Konstruktionsdetails:**

| Merkmal | Spezifikation |
|---------|---------------|
| Wandstärke | 0,8–1,5 mm (mehrlagig) |
| Nahttechnik | HF-verschweißt (Hochfrequenz) oder vulkanisiert |
| Anschlüsse | Einvulkanisierte Metallplatten mit Gewindeanschlüssen |
| Füllstutzen | Typisch 38mm (1½") Stutzen, oben |
| Entlüftung | 16mm Stutzen, oben |
| Entnahme | Stutzen oben (mit Saugrohr) oder unten (mit Absperrventil) |
| Tankgeber | Kapazitiver Geber (außen aufgeklebt) oder Stutzen mit Schwimmer |
| Max. Füllung | 90% des Nennvolumens (10% Ausdehnungsreserve) |
| Befestigung | Liegt lose in Mulde, seitlich durch Raumform begrenzt |

**Typische Größen und Preise:**

| Volumen | Abmessungen (flexibel) | Gewicht (leer) | Preis (ca.) |
|---------|----------------------|---------------|-------------|
| 50 l | ca. 600×400×250 mm | 1,5 kg | 250–400 EUR |
| 100 l | ca. 800×500×300 mm | 2,5 kg | 350–550 EUR |
| 200 l | ca. 1000×600×400 mm | 4 kg | 500–800 EUR |
| 400 l | ca. 1200×800×500 mm | 7 kg | 800–1.300 EUR |
| 600 l | ca. 1400×900×550 mm | 10 kg | 1.100–1.800 EUR |
| 1.000 l | ca. 1600×1000×700 mm | 15 kg | 1.600–2.600 EUR |

### 3.5 Standardtanks PE-HD

**Beschreibung:**
Rotationsgeformte Tanks aus PE-HD, ab Werk in Standardgrößen und -formen erhältlich. Typisch schwarz (UV-stabilisiert mit Carbon Black) oder naturweiß. Werden mit Spannbändern oder in Halterungen befestigt.

**Standardformen:**

| Form | Beschreibung | Typisches Volumen | Anwendung |
|------|-------------|-------------------|-----------|
| Quader | Rechteckig, flach oder hoch | 20–500 l | Universal |
| Niedrig-Profil | Flach, breite Grundfläche | 50–300 l | Unter Boden |
| Senkrecht | Schmal, hoch | 30–120 l | In Schränken, seitlich |
| Cross-Link | Vernetztes PE, verstärkt | 50–300 l | Benzin (USCG-konform) |
| Pontoon | Speziell für Pontonboote | 80–250 l | Pontonboote |

### 3.6 Sondertanks

#### 3.6.1 Tagestank (Day Tank / Service Tank)

Ein kleiner Tank (20–80l), der zwischen Haupttank und Motor geschaltet wird. Der Tagestank wird aus dem Haupttank über eine Transferpumpe befüllt und versorgt den Motor mit sauberem, entlüftetem Kraftstoff.

**Funktion und Vorteile:**
- Kraftstoff wird beim Transfer gefiltert und entwässert
- Motor saugt immer aus einem kleinen, vollen Tank — kein Luftansaugen bei Seegang
- Sediment und Wasser sammeln sich im Haupttank und können dort kontrolliert abgelassen werden
- Bei Haupttank-Leckage kann mit dem Tagestank noch mehrere Stunden gefahren werden
- Erleichtert den Wechsel zwischen verschiedenen Kraftstoffquellen (z.B. Steuerbord/Backbord)

**Typische Spezifikation:**

| Parameter | Wert |
|-----------|------|
| Volumen | 20–80 l (ca. 4–8 Stunden Motorlaufzeit) |
| Material | Edelstahl 316L oder PE-HD |
| Position | Höher als Motor (Schwerkraftfütterung) oder auf gleicher Höhe |
| Anschlüsse | Zulauf (mit Absperrventil), Entnahme, Rücklauf, Entlüftung, Ablassventil |
| Füllstandsanzeige | Schauglas oder Tankgeber |
| Filter | Vorfilter am Zulauf (30µm) |
| Überlauf | Zurück zum Haupttank |

#### 3.6.2 Absetzttank (Settling Tank)

Ein Tank, in dem Kraftstoff eine definierte Verweilzeit hat, damit Wasser und Sediment durch Schwerkraft absinken können. Wird in Motoryachten und kommerziellen Schiffen eingesetzt.

**Verweilzeit-Empfehlung:**
- Minimum: 4 Stunden (leichte Verunreinigung)
- Optimal: 8–12 Stunden (schwere Verunreinigung, Diesel-Bug)
- Temperatur: 30–40°C beschleunigt die Wasserabscheidung

**Konstruktionsmerkmale:**
- Konischer oder trichterförmiger Boden für Sedimentsammlung
- Ablassventil am tiefsten Punkt
- Entnahme deutlich oberhalb des Bodens (min. 50mm)
- Schauglas zur Kontrolle des Wasseranteils
- Heizung (optional) zur Verbesserung der Wasserabscheidung

---

## 4. Produktlinien und Spezifikationen

### 4.1 Vetus (Niederlande)

**Firmenprofil:**
Vetus B.V., Fokkerstraat 571-573, 3125 BD Schiedam, Niederlande
Gegründet 1966, einer der führenden europäischen Anbieter von Boots-Kraftstofftanks und Zubehör.

**Kraftstofftank-Programm:**

#### 4.1.1 Edelstahltanks Serie STAINLESS

| Modell | Volumen | Abmessungen L×B×H (mm) | Wandstärke | Gewicht | Anschlüsse | Preis (ca.) |
|--------|---------|------------------------|-----------|---------|-----------|-------------|
| FTS03800 | 38 l | 390×300×380 | 1,5 mm | 6,5 kg | 3× ½" BSP | 520 EUR |
| FTS06000 | 60 l | 500×300×450 | 1,5 mm | 9 kg | 4× ½" BSP | 680 EUR |
| FTS08000 | 80 l | 600×370×400 | 2,0 mm | 13 kg | 4× ½" BSP | 780 EUR |
| FTS12000 | 120 l | 700×400×480 | 2,0 mm | 18 kg | 5× ½" BSP | 940 EUR |
| FTS16000 | 160 l | 800×450×500 | 2,0 mm | 23 kg | 5× ½" BSP | 1.120 EUR |
| FTS20000 | 200 l | 800×500×550 | 2,0 mm | 28 kg | 5× ¾" BSP | 1.340 EUR |
| FTS30000 | 300 l | 1000×550×600 | 2,5 mm | 38 kg | 6× ¾" BSP | 1.780 EUR |
| FTS50000 | 500 l | 1100×700×700 | 2,5 mm | 56 kg | 6× ¾" BSP | 2.480 EUR |

**Ausstattung aller FTS-Modelle:**
- Material: AISI 316L (1.4404)
- Schweißnähte: WIG, durchgehend, gebeizt und passiviert
- Schwallbleche: ab FTS12000 (120l)
- Inspektionsöffnung: ab FTS20000 (200l), 150mm Durchmesser
- Tankgeber-Bohrung: 5-Loch, 54mm Bolzenkreis (VDO-kompatibel)
- Zertifizierung: CE, ISO 10088, ABYC H-24/H-33

#### 4.1.2 PE-HD Tanks Serie POLY

| Modell | Volumen | Abmessungen L×B×H (mm) | Kraftstoffart | Gewicht | Preis (ca.) |
|--------|---------|------------------------|--------------|---------|-------------|
| FTPL03200 | 32 l | 390×300×320 | Diesel | 2,5 kg | 120 EUR |
| FTPL05500 | 55 l | 500×350×370 | Diesel | 3,5 kg | 165 EUR |
| FTPL08000 | 80 l | 600×400×380 | Diesel | 5 kg | 210 EUR |
| FTPL12000 | 120 l | 700×450×420 | Diesel | 7 kg | 280 EUR |
| FTPL20000 | 200 l | 800×550×500 | Diesel | 10 kg | 390 EUR |
| FTPL30000 | 300 l | 1000×600×550 | Diesel | 14 kg | 520 EUR |

**Hinweis:** Vetus PE-HD-Tanks sind standardmäßig NUR für Diesel zugelassen. Für Benzin sind die fluorierte Serie FTPLG (mit "G" für Gasoline) erforderlich — Preisaufschlag ca. 25%.

#### 4.1.3 Flexible Tanks Serie FLEX

| Modell | Volumen | Abmessungen (max.) | Material | Preis (ca.) |
|--------|---------|-------------------|----------|-------------|
| FTFLEX060 | 60 l | 700×450×250 mm | PU/Nylon | 320 EUR |
| FTFLEX100 | 100 l | 800×550×280 mm | PU/Nylon | 420 EUR |
| FTFLEX200 | 200 l | 1000×700×350 mm | PU/Nylon | 620 EUR |
| FTFLEX400 | 400 l | 1200×850×450 mm | PU/Nylon | 950 EUR |

### 4.2 Tek-Tanks (Großbritannien)

**Firmenprofil:**
Tek-Tanks Ltd, Unit 3, Whittle Road, Meir Park, Stoke-on-Trent ST3 7UR, UK
Spezialist für maßgefertigte Aluminium- und Edelstahl-Kraftstofftanks.

**Programm:**

#### 4.2.1 Aluminium-Tanks (5083)

| Modell | Volumen | Material | Wandstärke | Schwallbleche | Preis (ca.) |
|--------|---------|----------|-----------|--------------|-------------|
| TT-AL-060 | 60 l | 5083-O | 3 mm | Nein | 380 GBP |
| TT-AL-120 | 120 l | 5083-O | 3 mm | 1 Stück | 520 GBP |
| TT-AL-200 | 200 l | 5083-O | 4 mm | 1 Stück | 720 GBP |
| TT-AL-300 | 300 l | 5083-O | 4 mm | 2 Stück | 950 GBP |
| TT-AL-500 | 500 l | 5083-O | 5 mm | 2 Stück | 1.380 GBP |
| TT-AL-CUSTOM | nach Maß | 5083-O | 3–6 mm | nach Bedarf | ab 800 GBP |

#### 4.2.2 Edelstahl-Tanks (316L)

| Modell | Volumen | Material | Wandstärke | Preis (ca.) |
|--------|---------|----------|-----------|-------------|
| TT-SS-060 | 60 l | 316L | 1,5 mm | 580 GBP |
| TT-SS-120 | 120 l | 316L | 2 mm | 780 GBP |
| TT-SS-200 | 200 l | 316L | 2 mm | 1.050 GBP |
| TT-SS-300 | 300 l | 316L | 2,5 mm | 1.420 GBP |
| TT-SS-500 | 500 l | 316L | 2,5 mm | 1.980 GBP |
| TT-SS-CUSTOM | nach Maß | 316L | 1,5–4 mm | ab 1.200 GBP |

**Besonderheiten Tek-Tanks:**
- Alle Tanks mit Lifetime-Schweißnaht-Garantie (bei korrekter Installation)
- 3D-CAD-Vermessung vor Ort für Custom-Tanks (UK, Aufpreis 200–400 GBP)
- Lieferzeit Standard: 2–4 Wochen, Custom: 4–8 Wochen
- Versand EU-weit, inkl. Zoll und Versicherung

### 4.3 Moeller Marine (USA)

**Firmenprofil:**
Moeller Marine Products, 1 Moeller Drive, Wixom, MI 48393, USA
Marktführer für PE-HD-Kraftstofftanks in Nordamerika.

**Programm:**

#### 4.3.1 Standard-PE-Tanks (Below Deck)

| Modell | Volumen (gal/l) | Abmessungen (in/mm) | Kraftstoff | USCG/ABYC | Preis (ca.) |
|--------|-----------------|---------------------|-----------|-----------|-------------|
| FT1204 | 12 gal / 45 l | 18×14×10 / 457×356×254 | Diesel | H-33 | 95 USD |
| FT1804 | 18 gal / 68 l | 24×14×10 / 610×356×254 | Diesel | H-33 | 125 USD |
| FT2704 | 27 gal / 102 l | 24×18×12 / 610×457×305 | Diesel | H-33 | 165 USD |
| FT3904 | 39 gal / 148 l | 30×18×14 / 762×457×356 | Diesel | H-33 | 210 USD |
| FT5504 | 55 gal / 208 l | 36×18×16 / 914×457×406 | Diesel | H-33 | 290 USD |
| FT7004 | 70 gal / 265 l | 42×20×16 / 1067×508×406 | Diesel | H-33 | 365 USD |
| FT1204G | 12 gal / 45 l | 18×14×10 / 457×356×254 | Benzin | H-24 | 130 USD |
| FT2704G | 27 gal / 102 l | 24×18×12 / 610×457×305 | Benzin | H-24 | 220 USD |
| FT5504G | 55 gal / 208 l | 36×18×16 / 914×457×406 | Benzin | H-24 | 385 USD |

**Hinweis:** "G"-Modelle sind fluoriert und für Benzin zugelassen (USCG 33 CFR 183, ABYC H-24). Nicht-G-Modelle NUR für Diesel.

### 4.4 Ronco Marine (Italien)

**Firmenprofil:**
Ronco S.r.l., Via dell'Industria 15, 25030 Torbole Casaglia (BS), Italien
Spezialist für Edelstahl-Kraftstofftanks im europäischen Yachtbau-Markt.

**Programm Edelstahl 316L:**

| Modell | Volumen | Form | Schwallbleche | Inspektionsdeckel | Preis (ca.) |
|--------|---------|------|--------------|-------------------|-------------|
| RC-SS-040 | 40 l | Quader | Nein | Nein | 480 EUR |
| RC-SS-080 | 80 l | Quader | 1 | Nein | 650 EUR |
| RC-SS-120 | 120 l | Quader | 1 | Ja (120mm) | 880 EUR |
| RC-SS-200 | 200 l | Quader | 2 | Ja (150mm) | 1.180 EUR |
| RC-SS-300L | 300 l | L-Form | 2 | Ja (150mm) | 1.650 EUR |
| RC-SS-500 | 500 l | Quader | 3 | Ja (200mm) | 2.280 EUR |
| RC-SS-800 | 800 l | Custom | nach Bedarf | Ja (200mm) | 3.400 EUR |

**Besonderheiten Ronco:**
- Alle Tanks mit TÜV-Prüfzeichen (optional, Aufpreis ~15%)
- Lasergeschnittene Bleche für präzise Passform
- Roboter-WIG-Schweißung für gleichmäßige Nahtqualität
- Lieferzeit: 3–6 Wochen ab Auftragsbestätigung

### 4.5 ATL — Aero Tec Laboratories (USA/UK)

**Firmenprofil:**
Aero Tec Laboratories Inc., 1 ATL Drive, Ramsey, NJ 07446, USA
ATL Ltd, Unit 2, Denbigh West, Bletchley, Milton Keynes MK1 1DW, UK
Weltweit führender Hersteller flexibler Tanks (Bladder), ursprünglich aus der Luft- und Raumfahrt.

**Programm Marine Fuel Bladders:**

| Modell | Volumen | Material | Diesel | Benzin | Gewicht (leer) | Preis (ca.) |
|--------|---------|----------|--------|--------|---------------|-------------|
| ATL FA-050 | 50 l | FluoroCell | Ja | Ja | 1,8 kg | 380 EUR |
| ATL FA-100 | 100 l | FluoroCell | Ja | Ja | 3,2 kg | 520 EUR |
| ATL FA-200 | 200 l | FluoroCell | Ja | Ja | 5,5 kg | 780 EUR |
| ATL FA-400 | 400 l | FluoroCell | Ja | Ja | 9 kg | 1.250 EUR |
| ATL FA-600 | 600 l | FluoroCell | Ja | Ja | 13 kg | 1.680 EUR |
| ATL FA-1000 | 1.000 l | FluoroCell | Ja | Ja | 20 kg | 2.450 EUR |

**ATL FluoroCell-Technologie:**
Mehrlagiger Aufbau: innere Fluorpolymer-Barriere + Nylon-Traggewebe + äußere Polyurethan-Beschichtung. Permeationsrate <0,05 g/(m²·d) für Benzin — deutlich unter den EPA-Grenzwerten. MIL-DTL-5578F-zertifiziert.

**ATL Sonderformen:**
ATL fertigt Bladder-Tanks in nahezu jeder Form. Der Kunde sendet 3D-Daten oder Schablonen, ATL erstellt eine maßgeschneiderte Form. Vorlaufzeit: 4–8 Wochen, Preis: ca. 40–60% Aufschlag gegenüber Standardformen.

### 4.6 Todd Marine (USA)

**Firmenprofil:**
Todd Enterprises Inc., 203 North Main Street, Elba, AL 36323, USA
Großserienhersteller von PE-HD-Tanks für den US-amerikanischen Bootsmarkt. OEM-Zulieferer für Boston Whaler, Grady-White, Sea Hunt u.a.

**Programm:**

#### 4.6.1 Below-Deck Fuel Tanks (PE-HD)

| Modell | Volumen (gal/l) | Profil | Kraftstoff | USCG | Preis (ca.) |
|--------|-----------------|--------|-----------|------|-------------|
| 85-1562 | 15 gal / 57 l | Low Profile | Diesel | Ja | 105 USD |
| 85-1563 | 22 gal / 83 l | Low Profile | Diesel | Ja | 145 USD |
| 85-1565 | 35 gal / 132 l | Standard | Diesel | Ja | 195 USD |
| 85-1570 | 50 gal / 189 l | Standard | Diesel | Ja | 265 USD |
| 85-1580 | 75 gal / 284 l | Large | Diesel | Ja | 380 USD |
| 85-1590 | 100 gal / 379 l | Large | Diesel | Ja | 495 USD |
| 85-1562G | 15 gal / 57 l | Low Profile | Benzin | Ja | 140 USD |
| 85-1565G | 35 gal / 132 l | Standard | Benzin | Ja | 260 USD |
| 85-1570G | 50 gal / 189 l | Standard | Benzin | Ja | 350 USD |

**Todd Besonderheiten:**
- Alle Tanks NMMA/USCG-zertifiziert (33 CFR 183)
- Cross-Linked PE für Benzintanks (höhere chemische Beständigkeit)
- Integrierte Tankgeber-Öffnung (SAE 5-Bolt)
- Limited Lifetime Warranty (bei korrekter Installation)
- Auch als OEM-Sonderanfertigung (ab 100 Stk.)

---

## 5. Hersteller-Datenbank

### 5.1 Vetus B.V.

| Feld | Information |
|------|------------|
| **Firmenname** | Vetus B.V. |
| **Adresse** | Fokkerstraat 571-573, 3125 BD Schiedam, Niederlande |
| **Telefon** | +31 (0)10 437 77 00 |
| **E-Mail** | sales@vetus.com |
| **Website** | www.vetus.com |
| **Gründung** | 1966 |
| **Spezialisierung** | Marine Kraftstoffsysteme, Abgassysteme, Borddurchlässe |
| **Modellreihen Tanks** | FTS (Edelstahl), FTPL (PE Diesel), FTPLG (PE Benzin), FTFLEX (Bladder) |
| **Vertrieb** | Weltweites Händlernetz, >120 Länder |
| **Zertifizierungen** | CE, ISO 9001, ABYC, NMMA |
| **Preisbereich Tanks** | 120–2.500 EUR |
| **Lieferzeit** | Standard: 1–3 Wochen, Custom: nicht verfügbar |
| **Garantie** | 2 Jahre Herstellergarantie |

### 5.2 Tek-Tanks Ltd

| Feld | Information |
|------|------------|
| **Firmenname** | Tek-Tanks Ltd |
| **Adresse** | Unit 3, Whittle Road, Meir Park, Stoke-on-Trent ST3 7UR, UK |
| **Telefon** | +44 (0)1onal 8 3434 |
| **E-Mail** | info@tek-tanks.com |
| **Website** | www.tek-tanks.com |
| **Gründung** | 2001 |
| **Spezialisierung** | Maßgefertigte Aluminium- und Edelstahl-Marine-Tanks |
| **Modellreihen** | TT-AL (Aluminium), TT-SS (Edelstahl), Custom |
| **Vertrieb** | UK direkt, EU über Händler |
| **Zertifizierungen** | ISO 9001, CE, BSI |
| **Preisbereich** | 380–5.000 GBP |
| **Lieferzeit** | Standard: 2–4 Wochen, Custom: 4–8 Wochen |
| **Garantie** | Lifetime Schweißnaht-Garantie |

### 5.3 Moeller Marine Products

| Feld | Information |
|------|------------|
| **Firmenname** | Moeller Marine Products (Division of Moeller Manufacturing) |
| **Adresse** | 1 Moeller Drive, Wixom, MI 48393, USA |
| **Telefon** | +1 (248) 624-1541 |
| **E-Mail** | marine@moellerproducts.com |
| **Website** | www.moellermarine.com |
| **Gründung** | 1947 |
| **Spezialisierung** | PE-HD Kraftstofftanks, Bilgenpumpen, marine Zubehör |
| **Modellreihen** | FT-Serie (Diesel), FTG-Serie (Benzin fluoriert) |
| **Vertrieb** | USA/Kanada direkt, international über Distributoren |
| **Zertifizierungen** | USCG 33 CFR 183, ABYC H-24/H-33, NMMA |
| **Preisbereich** | 95–500 USD |
| **Lieferzeit** | Ab Lager: 3–7 Tage, Custom: 6–12 Wochen |
| **Garantie** | 5 Jahre Herstellergarantie |

### 5.4 Ronco S.r.l.

| Feld | Information |
|------|------------|
| **Firmenname** | Ronco S.r.l. |
| **Adresse** | Via dell'Industria 15, 25030 Torbole Casaglia (BS), Italien |
| **Telefon** | +39 030 265 0XXX |
| **E-Mail** | info@roncomarine.it |
| **Website** | www.roncomarine.it |
| **Gründung** | 1985 |
| **Spezialisierung** | Edelstahl 316L Tanksysteme für Yachtbau |
| **Modellreihen** | RC-SS (Standard), RC-CUSTOM (Maßanfertigung) |
| **Vertrieb** | EU direkt, OEM-Zulieferer für Azimut, Ferretti |
| **Zertifizierungen** | CE, RINA, ISO 9001 |
| **Preisbereich** | 480–8.000 EUR |
| **Lieferzeit** | Standard: 3–6 Wochen, Custom: 6–10 Wochen |
| **Garantie** | 5 Jahre Herstellergarantie |

### 5.5 ATL — Aero Tec Laboratories

| Feld | Information |
|------|------------|
| **Firmenname** | Aero Tec Laboratories Inc. / ATL Ltd |
| **Adresse USA** | 1 ATL Drive, Ramsey, NJ 07446, USA |
| **Adresse UK** | Unit 2, Denbigh West, Bletchley, Milton Keynes MK1 1DW, UK |
| **Telefon USA** | +1 (201) 825-1400 |
| **Telefon UK** | +44 (0)1908 351700 |
| **E-Mail** | sales@atlinc.com |
| **Website** | www.atlinc.com |
| **Gründung** | 1970 |
| **Spezialisierung** | Flexible Kraftstofftanks (Bladder), Aerospace und Marine |
| **Modellreihen** | FA-Serie (Marine Fuel), FluoroCell, SuperCell |
| **Vertrieb** | Weltweit direkt und über Händler |
| **Zertifizierungen** | MIL-DTL-5578F, USCG, ABYC, CE, FIA (Motorsport) |
| **Preisbereich** | 380–5.000 EUR |
| **Lieferzeit** | Standard: 2–4 Wochen, Custom: 4–8 Wochen |
| **Garantie** | 3 Jahre Material- und Verarbeitungsgarantie |

### 5.6 Todd Enterprises Inc.

| Feld | Information |
|------|------------|
| **Firmenname** | Todd Enterprises Inc. |
| **Adresse** | 203 North Main Street, Elba, AL 36323, USA |
| **Telefon** | +1 (334) 897-2284 |
| **E-Mail** | info@toddenterprises.com |
| **Website** | www.toddenterprises.com |
| **Gründung** | 1960 |
| **Spezialisierung** | PE-HD Kraftstofftanks, OEM-Serienfertigung |
| **Modellreihen** | 85-Serie (Below Deck), 86-Serie (Topside/Portable) |
| **Vertrieb** | USA/Kanada, OEM für Boston Whaler, Grady-White, Sea Hunt |
| **Zertifizierungen** | USCG 33 CFR 183, ABYC H-24/H-33, NMMA |
| **Preisbereich** | 105–600 USD |
| **Lieferzeit** | Ab Lager: 3–7 Tage, OEM Custom: 8–16 Wochen |
| **Garantie** | Limited Lifetime Warranty |

### 5.7 Weitere Hersteller (Kurzübersicht)

| Hersteller | Land | Spezialisierung | Preisbereich | Website |
|-----------|------|-----------------|-------------|---------|
| Centurion Tanks | UK | Edelstahl/Alu Custom | 500–6.000 GBP | centuriontanks.co.uk |
| Plastimo | FR | PE Standardtanks | 80–350 EUR | www.plastimo.com |
| Can-SB | IT | Edelstahl/PE | 200–2.000 EUR | www.can-sb.it |
| Kraftstofftechnik Bauer | DE | Edelstahl Custom | 800–12.000 EUR | www.ktb-tanks.de |
| Dieseltank.de | DE | Alu/Edelstahl Custom | 600–8.000 EUR | www.dieseltank.de |
| Wema System AS | NO | Tankgeber/Zubehör | 50–300 EUR | www.wema.no |
| KUS (Shanghai) | CN | Tankgeber/Zubehör | 30–150 EUR | www.kusauto.com |

---

## 6. Fehlerbild-Atlas

### 6.1 Fehlerbild F01: Lochfraß an Aluminiumtanks (Pitting Corrosion)

| Feld | Details |
|------|---------|
| **Fehlerbild-ID** | F01-ALPITTING |
| **Schweregrad** | KRITISCH |
| **Betroffenes Material** | Aluminium 5083, 5086, 6061 |
| **Betroffene Tanktypen** | Einbautanks Aluminium |
| **Häufigkeit** | Sehr häufig (ca. 35% aller Aluminium-Tankschäden) |

**Symptome:**
- Diesel-/Benzingeruch in Bilge oder Kabine
- Sichtbare weiße Korrosionsprodukte (Aluminiumhydroxid) an der Tankaußenseite
- Feuchte Stellen an der Tankaußenwand
- Tankgeber zeigt sinkenden Füllstand trotz keinem Verbrauch
- Kraftstoff in Bilge (bei fortgeschrittenem Stadium)

**Ursachen:**
1. **Galvanische Korrosion:** Direkter Kontakt zwischen Aluminiumtank und Edelstahl-Halterung, Bronze-Fitting oder Kupferrohr in Anwesenheit von Elektrolyt (Kondenswasser, Salzwasser, Bilgenwasser)
2. **Kondenswasser im Tankinneren:** Teilgefüllte Tanks "atmen" — warme, feuchte Luft tritt ein, kühlt ab, Kondenswasser sammelt sich am Tankboden. Dieses Wasser enthält gelösten Sauerstoff und ggf. Chloride → Lochfraß
3. **Verunreinigungen im Kraftstoff:** Wasser, Schwefelverbindungen, organische Säuren (aus Diesel-Bug-Metabolismus) greifen Aluminium an
4. **Falscher Zusatzwerkstoff beim Schweißen:** AlSi5 (4043) statt AlMg5 (5183) erzeugt galvanisches Element zwischen Schweißnaht und Grundmaterial

**Diagnose:**
1. Tank von außen auf weiße Ablagerungen (Aluminiumhydroxid, Al(OH)₃) untersuchen
2. Bilge auf Kraftstoff-Spuren untersuchen (Dieselgeruch, öliger Film)
3. Tank ablassen, mit Endoskop oder Inspektionsöffnung innen begutachten
4. Wandstärke mit Ultraschall-Dickenmessgerät prüfen (Referenz: Original-Wandstärke)
5. Elektrolyt-Potentialmessung zwischen Tank und umgebenden Metallen (>50 mV Differenz = galvanisches Risiko)

**Reparatur:**
- **Stadium 1 (Oberflächen-Pitting, <30% Wandstärkenverlust):** Galvanische Isolation aller Kontaktstellen, Opferanoden installieren, Tank trocknen und Kondensat-Management verbessern
- **Stadium 2 (Tiefes Pitting, 30–60% Wandstärkenverlust):** Wie Stadium 1 + betroffene Bereiche mit Alu 5183 WIG-schweißen (NUR durch zertifizierten Aluminium-Schweißer)
- **Stadium 3 (Durchbruch, >60% oder Leckage):** Tank-Austausch. Reparatur nicht wirtschaftlich bei großflächigem Pitting
- **Galvanische Isolation nachrüsten:** Neopren-Pads (min. 3mm) zwischen Tank und Halterung, Isolierbuchsen an allen Schraubverbindungen, Kupferleitungen durch Kunststoff-Zwischenstücke trennen

**Prävention:**
- Tank IMMER voll halten bei Langzeitlagerung (reduziert Kondensat-Fläche)
- Galvanische Isolation bei Installation IMMER korrekt ausführen
- Jährliche Sichtprüfung auf Korrosionsspuren
- Opferanoden am Tank installieren (Zink oder Magnesium, je nach Umgebung)
- Kraftstoff regelmäßig entwässern (Wasserabscheider, Tankablassventil)

### 6.2 Fehlerbild F02: Diesel-Bug (Microbial Contamination)

| Feld | Details |
|------|---------|
| **Fehlerbild-ID** | F02-DIESELBUG |
| **Schweregrad** | HOCH |
| **Betroffener Kraftstoff** | Diesel (EN 590), Biodiesel (B7, B20) |
| **Betroffene Tanktypen** | Alle Typen |
| **Häufigkeit** | Sehr häufig (ca. 25% aller Diesel-Tanksysteme betroffen) |

**Symptome:**
- Dunkle, schleimige Ablagerungen an Tankwänden und Anschlüssen
- Verstopfte Kraftstofffilter (Filterstandzeit von 500h auf 50h reduziert)
- Motorstottern, Leistungsverlust, unregelmäßiger Lauf
- Schwefelwasserstoff-Geruch (H₂S, "faule Eier") beim Öffnen des Tankdeckels
- Schwarze, klumpige Partikel im Kraftstofffilter
- Korrosion der Tankinnenside (besonders bei Aluminiumtanks — Mikroorganismen produzieren organische Säuren)
- Wasser am Tankboden (Mikroorganismen leben an der Diesel-Wasser-Grenzschicht)

**Ursachen:**
1. **Mikroorganismen:** Primär Hormoconis resinae (Cladosporium resinae, "Diesel-Pilz"), Pseudomonas aeruginosa (Bakterium), Yarrowia lipolytica (Hefe). Diese Organismen leben an der Grenzschicht zwischen Diesel und Wasser und verstoffwechseln Kohlenwasserstoffe
2. **Wasser im Tank:** Kondensat, Regenwasser über undichte Einfüllstutzen, Kraftstoff-inhärentes Wasser. Bereits 0,05% Wassergehalt (500 ppm) reicht für mikrobielles Wachstum
3. **Biodiesel-Anteil:** Biodiesel (FAME) ist hygroskopisch — zieht Wasser an — und bietet als Ester einen besseren Nährboden als reiner Mineralöldesiel. Seit EN 590:2013 enthält Diesel bis zu 7% FAME (B7), was das Diesel-Bug-Risiko erhöht hat
4. **Temperatur:** Optimales Wachstum bei 25–35°C — Tanks in warmen Klimazonen (Mittelmeer, Karibik) und in der Nähe des Maschinenraums sind besonders gefährdet
5. **Lange Standzeiten:** Tanks, die >3 Monate ohne Betrieb stehen, entwickeln signifikant häufiger Diesel-Bug

**Diagnose:**
1. **Visuelle Inspektion:** Inspektionsöffnung öffnen, auf schleimige Ablagerungen und schwarze Partikel prüfen
2. **Kraftstoffprobe:** Aus Tankablassventil ziehen (am tiefsten Punkt). In durchsichtiges Glas füllen, 30 min stehen lassen. Wasser/Sediment am Boden = verdächtig
3. **Testkit:** Fuelstat-Test (Antikörper-basiert, Ergebnis in 10 min) oder Liqui-Cult-Test (Kulturmedium, Ergebnis in 3–7 Tagen)
4. **Laboranalyse:** Kraftstoffprobe an Labor senden (z.B. SGS, Bureau Veritas) — Bestimmung von Keimzahl (KBE/ml), Wassergehalt (Karl-Fischer), Säurezahl

**Reparatur/Sanierung:**
1. **Mechanische Reinigung:** Tank vollständig ablassen, mit Hochdruckreiniger (60°C Wasser) ausspülen, Biofilm mechanisch entfernen
2. **Biozid-Behandlung:** Grotamar 82 (10ml/100l Diesel) oder Marine 16 Diesel Bug Treatment (1:1000). 24h einwirken lassen, dann Kraftstoff über Feinfilter (2µm) umwälzen
3. **Filtertausch:** Alle Kraftstofffilter (Vorfilter, Feinfilter, Wasserabscheider) erneuern
4. **Kraftstoff-Polishing:** Gesamten Kraftstoffbestand über Polishing-System (2µm Filter + Wasserabscheider) umwälzen, bis Partikelzählung <ISO 18/16/13
5. **Tank-Inspektion:** Nach Reinigung Tankinnenside auf Korrosionsschäden prüfen (besonders Aluminium)

**Prävention:**
- Wasser regelmäßig am Tankablassventil ablassen (monatlich im Sommer)
- Tank bei Langzeitlagerung möglichst voll halten
- Biozid prophylaktisch beim Tanken zusetzen (Grotamar 82, 5ml/100l)
- Kraftstoff-Wasserabscheider (Racor, Separ) im Zulauf installieren
- Belüftung mit Trockenmittel-Filter (Silicagel) versehen

### 6.3 Fehlerbild F03: Blockierte Tankentlüftung

| Feld | Details |
|------|---------|
| **Fehlerbild-ID** | F03-VENTBLOCK |
| **Schweregrad** | HOCH (kann zu Tankschaden und Motorausfall führen) |
| **Betroffene Tanktypen** | Alle Typen |
| **Häufigkeit** | Häufig (ca. 15% aller Tank-Störungen) |

**Symptome:**
- Tank lässt sich nicht vollständig betanken (Kraftstoff quillt am Einfüllstutzen zurück)
- Motor stirbt nach 10–30 Minuten Betrieb ab (Unterdruck verhindert Kraftstoffnachfluss)
- Eingebeulte Tankwände (bei PE- und Alu-Tanks, Unterdruck)
- Zischendes Geräusch beim Öffnen des Tankdeckels (Druckausgleich)
- Kraftstoff tropft aus der Entlüftungsöffnung beim Betanken (P/V-Ventil defekt)

**Ursachen:**
1. **Insekten/Spinnen:** Wespen und Spinnen nisten bevorzugt in Entlüftungsöffnungen — der warme, geschützte Hohlraum ist ideal
2. **Korrosion:** Entlüftungsleitung aus Kupfer oder Messing korrodiert von innen zu
3. **Knick:** Entlüftungsschlauch wurde bei Arbeiten am Boot geknickt und nicht wiederhergestellt
4. **Salzablagerungen:** Spritzwasser in der Außenöffnung → Salzkristalle verengen den Querschnitt
5. **Defektes P/V-Ventil:** Membrane verklebt, Ventilsitz korrodiert
6. **Biofilm:** Diesel-Bug wächst in der Entlüftungsleitung (feucht-warmes Milieu)

**Diagnose:**
1. Entlüftungsöffnung außenbords lokalisieren und visuell prüfen
2. Mit Druckluft (max. 0,3 bar!) durch die Entlüftungsleitung blasen — freier Durchgang = OK
3. P/V-Ventil ausbauen und auf Gängigkeit prüfen
4. Entlüftungsleitung mit Endoskop-Kamera untersuchen (bei Verdacht auf innere Blockade)
5. Drucktest: Tank verschließen (alle Anschlüsse dicht), 0,1 bar Überdruck aufbringen, 5 min halten. Kein Druckabfall = Entlüftung blockiert

**Reparatur:**
1. Außenöffnung reinigen, Insektennester entfernen
2. Entlüftungsleitung mit Druckluft durchblasen oder mit flexiblem Draht durchstoßen
3. Defektes P/V-Ventil ersetzen
4. Geknickte Leitung ersetzen oder umverlegen
5. Flammensperre (Benzintank) reinigen oder ersetzen — NIEMALS entfernen!

**Prävention:**
- Entlüftungsöffnung mit Insektenschutzgitter versehen (Maschenweite 1mm)
- Jährliche Funktionsprüfung der Entlüftung beim Saisonstart
- P/V-Ventil alle 5 Jahre ersetzen

### 6.4 Fehlerbild F04: Tankgeber-Fehlanzeige

| Feld | Details |
|------|---------|
| **Fehlerbild-ID** | F04-SENDERROR |
| **Schweregrad** | MITTEL (keine direkte Sicherheitsgefahr, aber Risiko des Leerlaufens) |
| **Betroffene Tanktypen** | Alle Typen mit Schwimmer-Tankgeber |
| **Häufigkeit** | Sehr häufig (ca. 20% aller Tanksysteme zeigen Abweichungen >10%) |

**Symptome:**
- Anzeige springt unregelmäßig bei Seegang
- Anzeige zeigt immer "voll" oder immer "leer"
- Anzeige stimmt nicht mit tatsächlichem Verbrauch überein
- Tankanzeige reagiert verzögert oder gar nicht auf Betankung

**Ursachen:**
1. **Sulfidbildung am Widerstandselement:** Schwefelverbindungen im Diesel (insbesondere bei ULSD) korrodieren den Widerstandsdraht des Schwimmgebers — häufigste Ursache
2. **Schwimmer undicht:** Schaumstoff- oder Hohkugel-Schwimmer nimmt Kraftstoff auf und sinkt
3. **Gestänge verbogen:** Schwimmer-Hebelarm wurde bei Einbau oder Wartung verbogen
4. **Falscher Gebertyp:** Geber für anderen Tankform oder andere Anzeige (Impedanz-Mismatch)
5. **Verkabelung:** Korrosion, Kabelbruch oder Massefehler in der Signalleitung
6. **Tankform vs. Geber:** Geber hat linearen Kennlinie, Tank hat nicht-lineares Volumen (z.B. keilförmig)

**Diagnose:**
1. Geber ausbauen, Schwimmer auf Dichtheit prüfen (in Kraftstoff tauchen — sinkt = defekt)
2. Widerstandswert am Geber messen (mit Multimeter): Leerlauf (leer) und Vollausschlag (voll) laut Datenblatt?
3. Signalleitung auf Durchgang und Isolationswiderstand prüfen
4. Anzeigeinstrument mit bekanntem Widerstand prüfen (z.B. 10 Ω → "leer", 180 Ω → "voll" bei VDO-Standard)
5. Tankform analysieren: passt die Geber-Kennlinie zur Tankgeometrie?

**Reparatur:**
- Defekten Geber ersetzen (typisch 60–200 EUR für Schwimmgeber)
- Kabelverbindungen erneuern, Stecker mit Kontaktfett behandeln
- Bei nicht-linearer Tankform: programmierbaren Geber verwenden (Wema SSI, KUS)
- Bei Sulfidproblem: Geber reinigen (Kontaktspray), langfristig auf kapazitiven oder Ultraschall-Geber umrüsten

### 6.5 Fehlerbild F05: Rissbildung an PE-HD-Tanks

| Feld | Details |
|------|---------|
| **Fehlerbild-ID** | F05-PECRACK |
| **Schweregrad** | HOCH |
| **Betroffenes Material** | PE-HD (Rotomoulding) |
| **Häufigkeit** | Mäßig häufig (ca. 10% der PE-Tanks >15 Jahre) |

**Symptome:**
- Haarfeine Risse an Anschlussbereichen oder Ecken
- Kraftstoffgeruch ohne sichtbare Leckage (Permeation durch Mikrorisse)
- Weißfärbung des PE im Rissbereich (Stress Whitening)
- Riss breitet sich bei Vibration oder Temperaturwechsel aus

**Ursachen:**
1. **UV-Degradation:** PE ohne Carbon-Black-Stabilisierung wird durch UV-Strahlung spröde (Kettenbruch)
2. **Umwelt-Spannungsrisskorrosion (ESCR):** Kontakt mit bestimmten Chemikalien (Tenside, Öle, einige Biozide) + mechanische Spannung → Rissbildung
3. **Überbeanspruchung der Anschlüsse:** Starre Rohrleitungen übertragen Vibrationen auf die PE-Anschlussstutzen
4. **Materialermüdung:** Zyklische Belastung durch Seegang über viele Jahre
5. **Übertemperatur:** PE-HD erweicht ab 60°C — Tanks in der Nähe des Maschinenraums können sich dauerhaft verformen

**Diagnose:**
1. Tank auf Risse und Verfärbungen visuell prüfen (besonders Anschlüsse, Ecken, Biegungen)
2. Stress-Whitening (lokale Weißfärbung) zeigt Überbeanspruchung an — Riss folgt meist
3. UV-geschädigte Bereiche: Oberfläche kreidig, spröde (Fingernagel-Test: Kratzer → UV-Schaden)
4. Drucktest: 0,2 bar, 10 min. Druckverlust → undichte Stelle mit Seifenwasser lokalisieren

**Reparatur:**
- PE-HD-Tanks können NICHT geschweißt werden (Rotomoulding-Material lässt sich nicht zuverlässig feldschweißen)
- Temporär: Epoxid-Reparaturkit (z.B. Plastic Welder) — nur als Notlösung, nicht dauerhaft
- Dauerhaft: Tank-Austausch (empfohlen)
- Alternative: Flexiblen Bladder-Tank als Ersatz in den vorhandenen Raum einsetzen

### 6.6 Fehlerbild F06: Elektrolyse-Korrosion an Edelstahltanks

| Feld | Details |
|------|---------|
| **Fehlerbild-ID** | F06-SSELECTRO |
| **Schweregrad** | HOCH (langfristig) |
| **Betroffenes Material** | Edelstahl 316L, 304 |
| **Häufigkeit** | Mäßig (ca. 8% der Edelstahltanks >15 Jahre) |

**Symptome:**
- Rostbraune Ablagerungen an Schweißnähten (Oxidation in der WEZ)
- Lochfraß an der Tankunterseite (Kontakt mit Bilgenwasser)
- Spaltkorrosion an Tankhalterungen
- Tee-Staining (orangefarbene Verfärbung) an der Oberfläche

**Ursachen:**
1. **Spaltkorrosion:** Zwischen Tank und Halterung oder unter Spannbändern bildet sich ein Spalt, in dem Feuchtigkeit stagniert — Sauerstoffverarmung → lokaler pH-Abfall → Korrosion
2. **Mangelhaftes Beizen:** Schweißnähte wurden nach der Fertigung nicht gebeizt — die Anlauffarben sind chromverarmte Zonen und korrodieren bevorzugt
3. **Fremdrost (Kontamination):** Bearbeitung mit Werkzeugen, die zuvor für Normalstahl verwendet wurden, hinterlässt Eisenpartikel → Rostflecken → Lochfraß
4. **Chloridkontakt:** Bilgenwasser mit hohem Chloridgehalt (Salzwasser) greift 316L an, besonders bei Temperaturen >50°C

**Diagnose:**
1. Visuelle Inspektion auf Rostflecken, Lochfraß und Verfärbungen
2. Schweißnähte auf Anlauffarben prüfen — goldbraun = akzeptabel, blau/violett = chromverarmte Zone
3. Wandstärke per Ultraschall messen
4. Passivitätsprüfung: Kupfersulfat-Test (CuSO₄ auf die Oberfläche → Kupferabscheidung = passive Schicht defekt)

**Reparatur:**
- Stadium 1 (Oberflächen): Beizen und Passivieren mit HF/HNO₃-Paste (Avesta 601, Henkel P3-Inox)
- Stadium 2 (Lochfraß): Betroffene Stelle ausschleifen, WIG-aufschweißen (316L Si), beizen
- Stadium 3 (Großflächig): Tank-Austausch

### 6.7 Fehlerbild F07: Tankverformung durch Unterdruck

| Feld | Details |
|------|---------|
| **Fehlerbild-ID** | F07-VACUUM |
| **Schweregrad** | HOCH |
| **Betroffene Tanktypen** | PE-HD, dünnwandige Aluminium-Tanks |
| **Häufigkeit** | Mäßig (ca. 5% aller Tank-Störungen) |

**Symptome:**
- Tankwände sind eingebeult (konkav statt gerade)
- Motor stirbt nach Betriebszeit ab (Kraftstoff-Unterversorgung)
- Zischendes Geräusch beim Öffnen des Tankdeckels
- Tankgeber zeigt zu niedrigen Stand an (Tank ist physisch kleiner geworden)

**Ursachen:**
- Blockierte Tankentlüftung (→ F03)
- Defektes P/V-Ventil (Unterdruckseite öffnet nicht)
- Entlüftungsleitung mit Tiefpunkt (Kondensat blockiert)

**Reparatur:**
- Entlüftung reparieren (→ F03)
- PE-HD-Tank: Kann sich nach Druckausgleich teilweise zurückformen, prüfen auf Rissbildung
- Aluminium-Tank: Permanente Verformung → Tankaussehen → ggf. Austausch
- P/V-Ventil ersetzen

### 6.8 Fehlerbild F08: Undichte Tankanschlüsse

| Feld | Details |
|------|---------|
| **Fehlerbild-ID** | F08-FITLEAK |
| **Schweregrad** | HOCH (Kraftstoffaustritt) |
| **Betroffene Tanktypen** | Alle Typen |
| **Häufigkeit** | Sehr häufig (ca. 20% aller Tank-Leckagen) |

**Symptome:**
- Kraftstofftropfen an Anschlussstellen
- Dieselgeruch im Maschinenraum
- Öliger Film auf Bilgenwasser

**Ursachen:**
1. Vibration lockert Verschraubungen
2. PTFE-Band falsch angewendet (zu wenig Wicklungen, falsche Richtung)
3. Dichtung ausgehärtet oder verquollen
4. Überdrehen zerstört Gewindegang (besonders bei PE- und Alu-Anschlüssen)
5. Thermische Ausdehnung (unterschiedliche Metalle)

**Reparatur:**
1. Anschluss reinigen, altes Dichtmaterial entfernen
2. Neues PTFE-Band (min. 5 Wicklungen, Uhrzeigersinn auf Außengewinde) oder anaerober Gewindedichter (Loctite 577)
3. Handfest + ¼ bis ½ Umdrehung (metallisch), handfest + 1–2 Umdrehungen (PE)
4. Flexible Schlauchverbindung statt starrer Rohrverbindung bei vibrationsbelasteten Anschlüssen

### 6.9 Fehlerbild F09: Kraftstoffpermeation durch GFK

| Feld | Details |
|------|---------|
| **Fehlerbild-ID** | F09-GFKPERM |
| **Schweregrad** | MITTEL (langfristig) |
| **Betroffenes Material** | GFK Integrationstanks (besonders mit Polyester-Harz) |
| **Häufigkeit** | Mäßig (ca. 10% der Integrationstanks >10 Jahre) |

**Symptome:**
- Chronischer Dieselgeruch in Kabinen trotz dicht scheinendem System
- Verfärbung des Rumpflaminats im Tankbereich
- Klebrige Oberfläche des Laminats (Harz erweicht)
- Osmose-ähnliche Bläschen an der Tankinnenside

**Ursachen:**
- Orthophthal-Polyester als Harz (nicht kraftstoffbeständig)
- Fehlende oder beschädigte Vinylester-Barriereschicht
- Biodiesel-Anteil (FAME) greift Polyester an
- Langzeitexposition bei erhöhter Temperatur

**Reparatur:**
- Vinylester-Barrier-Coat auf der Tankinnensite nachrüsten (nur möglich wenn Tank zugänglich)
- Alternativer: Flexiblen Bladder-Tank in den GFK-Tank einsetzen (Tank-im-Tank)
- Letztlich: Integrationstank stilllegen und separaten Metalltank installieren

### 6.10 Fehlerbild F10: Schwallblech-Versagen

| Feld | Details |
|------|---------|
| **Fehlerbild-ID** | F10-BAFFAIL |
| **Schweregrad** | MITTEL bis HOCH |
| **Betroffene Tanktypen** | Metalltanks mit Schwallblechen |
| **Häufigkeit** | Selten (ca. 3% der Metalltanks) |

**Symptome:**
- Klopf- oder Schlaggeräusche aus dem Tank bei Seegang
- Plötzliche Trimm-Änderungen bei Seegang (Kraftstoff schwappt ungehindert)
- Rissbildung an der Tankwand neben der Schwallblech-Schweißnaht

**Ursachen:**
- Ermüdungsbruch der Schweißnaht (zyklische Belastung durch Seegang)
- Unterdimensioniertes Schwallblech (zu dünn, zu wenige Befestigungspunkte)
- Korrosion der Schweißnaht (bei Aluminiumtanks → galvanische Zelle)

**Reparatur:**
- Tank professionell öffnen (Inspektionsdeckel oder Schnitt)
- Schwallblech erneut einschweißen (dickeres Material, mehr Befestigungspunkte)
- Schweißnaht komplett umlaufend, nicht punktweise

### 6.11 Fehlerbild F11: Kraftstoff-Wasser-Emulsion

| Feld | Details |
|------|---------|
| **Fehlerbild-ID** | F11-WATEREMUL |
| **Schweregrad** | HOCH (Motorschaden möglich) |
| **Betroffener Kraftstoff** | Diesel |
| **Häufigkeit** | Häufig (ca. 15% aller Diesel-Systeme zeitweise betroffen) |

**Symptome:**
- Diesel erscheint milchig-trüb statt klar
- Motor raucht weiß (Wasser in Brennkammer)
- Leistungsverlust, unrunder Lauf
- Injektor-Schäden (Wasser → lokale Kühlung → Thermoschock → Düsennadel-Verschleiß)

**Ursachen:**
- Kondenswasser im Tank (temperaturbedingt)
- Wasser über undichten Einfüllstutzen oder Entlüftung eingetreten
- Biodiesel-Anteil erhöht Wasseraufnahmefähigkeit des Diesels (B7 hält ca. 1.200 ppm Wasser in Lösung vs. 60 ppm bei reinem Mineral-Diesel)
- Defekter Wasserabscheider

**Reparatur:**
1. Kraftstoff über Ablassventil am tiefsten Punkt ablassen bis klarer Diesel kommt
2. Kraftstoff-Polishing: gesamten Inhalt über 2µm-Filter + Koaleszenz-Wasserabscheider umwälzen
3. Wasserabscheider (Racor, Separ) prüfen und ggf. ersetzen
4. Einfüllstutzen und Entlüftung auf Dichtheit prüfen
5. Additiv (Demulgator) zusetzen (z.B. Liqui Moly Marine Diesel Schutz)

### 6.12 Fehlerbild F12: Tanksender-Kabelkorrosion

| Feld | Details |
|------|---------|
| **Fehlerbild-ID** | F12-WIRECORR |
| **Schweregrad** | NIEDRIG bis MITTEL |
| **Betroffene Systeme** | Tankgeber-Verkabelung |
| **Häufigkeit** | Sehr häufig (ca. 30% der Boote >10 Jahre) |

**Symptome:**
- Tankanzeige flackert oder zeigt sporadisch falsche Werte
- Anzeige fällt komplett aus (Verbindungsunterbrechung)
- Sicherung für Tankanzeige brennt durch (Kurzschluss durch korrodierte Isolation)

**Ursachen:**
- Feuchtigkeit in Steckverbindungen (Spritzwasser, Kondensat)
- Nicht-verzinntes Kupferkabel (oxidiert im marinen Umfeld)
- Kabelisolierung durch Kraftstoff angegriffen (PVC in Dieselkontakt)

**Reparatur:**
1. Alle Steckverbindungen öffnen, reinigen, mit Kontaktfett (z.B. Tef-Gel) behandeln
2. Korrodierte Kabelenden abschneiden, neu verzinnte Kabelschuhe crimpen + löten
3. Kabel durch marine-grade verzinntes Kabel mit XLPE-Isolation ersetzen
4. Wasserdichte Steckverbindungen (Deutsch-Stecker, IP67) verwenden
5. Kabelführung aus Bilge/feuchten Bereichen verlegen

---

## 7. Troubleshooting-Entscheidungsbäume

### 7.1 Entscheidungsbaum: Kraftstoffverlust

**Ausgangssituation:** Kraftstoff-Verbrauch stimmt nicht mit Motorlaufzeit überein ODER Kraftstoff-Geruch/-Spuren in Bilge.

**Schritt 1:** Ist Kraftstoff in der Bilge sichtbar?
- **JA** → Schritt 2
- **NEIN, aber Geruch vorhanden** → Schritt 5
- **NEIN, kein Geruch, nur Geber-Abweichung** → Tankgeber prüfen (→ F04)

**Schritt 2:** Kraftstoff in Bilge — Menge?
- **Tropfend (wenige ml/Tag)** → Schritt 3
- **Erheblich (>100 ml/Tag)** → SOFORT Motor abstellen, Tank lokalisieren, alle Anschlüsse prüfen. Ist Tank rissig? → Schritt 4

**Schritt 3:** Tropf-Leckage — Wo tropft es?
- **An einem Anschluss/Fitting** → Fitting nachziehen oder Dichtung erneuern (→ F08)
- **An der Tankwand** → Lochfraß oder Riss — Material? Alu → F01, PE → F05, Edelstahl → F06
- **Am Tankgeber-Flansch** → Geberdichtung erneuern
- **Nicht lokalisierbar** → Tank trocknen, mit Kreide bestäuben, 24h warten, nasse Stelle markiert die Leckage

**Schritt 4:** Tankschaden — Rissig oder Lochfraß?
- **Aluminium mit weißen Ablagerungen** → Lochfraß durch Korrosion (→ F01)
- **PE mit Riss** → UV- oder Materialermüdung (→ F05)
- **Edelstahl mit Rostflecken** → Spaltkorrosion oder Fremdrost (→ F06)
- **GFK mit Verfärbung** → Permeation oder Delamination (→ F09)

**Schritt 5:** Geruch ohne sichtbare Leckage:
- **Dieselgeruch in Kabine** → GFK-Permeation (→ F09) oder Leitungs-Leckage im Verborgenen
- **Benzingeruch** → SOFORT Bilgengebläse einschalten, alle Zündquellen ausschalten, Boot verlassen, Tankentlüftung und Leitungen prüfen
- **Geruch nur beim Betanken** → Überfüllung, Entlüftung prüfen (→ F03)

### 7.2 Entscheidungsbaum: Motorstottern / Leistungsverlust

**Ausgangssituation:** Motor läuft unrund, hat Leistungsverlust oder stirbt ab.

**Schritt 1:** Wann tritt das Problem auf?
- **Nach längerem Betrieb (>30 min)** → Schritt 2
- **Sofort nach Motorstart** → Kraftstofffilter geprüft? → Schritt 3
- **Bei Seegang** → Schritt 4
- **Nach dem Betanken** → Falscher Kraftstoff? Wassereinlass beim Tanken? → Kraftstoffprobe ziehen

**Schritt 2:** Problem nach längerem Betrieb:
- **Motor stirbt komplett ab** → Tank leer? (Geber prüfen, Tankablassventil öffnen) → Wenn Tank voll: Entlüftung blockiert? (→ F03, F07)
- **Motor stottert und erholt sich** → Luft im System (Leckage in Saugleitung), Diesel-Bug (Filter prüfen → F02)

**Schritt 3:** Kraftstofffilter:
- **Filter schwarze Partikel** → Diesel-Bug (→ F02)
- **Filter mit Wasser** → Wasser im Tank (→ F11)
- **Filter verstopft, braunes Sediment** → Tank-Rost (Stahltank) oder Aluminium-Korrosion (→ F01)
- **Filter sauber** → Problem liegt nicht am Tanksystem

**Schritt 4:** Problem bei Seegang:
- **Motor stirbt ab bei starker Krängung** → Tankform/Saugrohr-Position: Saugrohr zu kurz oder zu hoch → Luft wird angesaugt bei Krängung. Lösung: Saugrohr verlängern oder Schwallblech installieren
- **Motor stottert bei Stampfen** → Schwallblech defekt oder fehlend (→ F10), Tankinhalt schlägt

### 7.3 Entscheidungsbaum: Kraftstoffgeruch im Boot

**Ausgangssituation:** Kraftstoffgeruch an Bord, Quelle unklar.

**Schritt 1:** Welcher Geruch?
- **Diesel (ölig, schwer)** → Schritt 2
- **Benzin (leicht, flüchtig)** → WARNUNG: Sofort Bilgengebläse einschalten, alle Zündquellen aus, Boot lüften. Dann → Schritt 3

**Schritt 2:** Diesel-Geruch — Wo am stärksten?
- **Maschinenraum** → Leitungen, Filter, Motoranschlüsse, Tankanschlüsse prüfen. Undichte Stelle mit weißem Papier lokalisieren
- **Kabine über Tank** → GFK-Permeation (→ F09), undichte Inspektionsöffnung, undichter Geber-Flansch
- **Bilge** → Tank-Leckage (→ Baum 7.1) oder Leitungs-Leckage
- **An Deck** → Einfüllstutzen-Dichtung prüfen, Entlüftung prüfen
- **Überall** → Textilien/Polster haben Diesel absorbiert — Sanierung mit Enzymreiniger

**Schritt 3:** Benzin-Geruch — KRITISCH:
- **Im Bilgenbereich** → Sofort Gas-Detektor verwenden (UEG-Messung). Bei >10% UEG: Boot sofort verlassen! Alle Leitungen, Tank, Entlüftung prüfen
- **An Deck** → Tankentlüftung prüft, Einfüllstutzen-Dichtung prüfen
- **Nach dem Tanken** → Überfüllung → Entlüftung und Siphon-Falle prüfen (→ F03)

### 7.4 Entscheidungsbaum: Tankgeber-Fehlanzeige

**Ausgangssituation:** Tankanzeige stimmt nicht mit tatsächlichem Tankinhalt überein.

**Schritt 1:** Art der Fehlanzeige?
- **Anzeige immer auf "voll"** → Schritt 2
- **Anzeige immer auf "leer"** → Schritt 3
- **Anzeige springt/flackert** → Schritt 4
- **Anzeige zeigt falschen, aber stabilen Wert** → Schritt 5

**Schritt 2:** Immer "voll":
- Geber-Kabel am Geber abklemmen → Zeigt Anzeige weiterhin "voll"? JA → Anzeige defekt oder Kurzschluss in Leitung. NEIN → Geber defekt (Widerstand zu niedrig, Schwimmer klemmt oben)

**Schritt 3:** Immer "leer":
- Geber-Kabel am Geber abklemmen und Kabel kurzschließen → Zeigt Anzeige "voll"? JA → Geber defekt (Unterbrechung) oder Kabel gebrochen. NEIN → Anzeige defekt

**Schritt 4:** Springt/flackert:
- Tritt es nur bei Seegang auf? JA → Normal bei Schwimmer-Gebern, Dämpfung an Anzeige aktivieren (elektronisch) oder Widerstandsgeber durch kapazitiven Geber ersetzen
- Auch im Ruhezustand? → Korrodierte Kontakte (→ F12), sulfidierter Widerstandsdraht (→ F04)

**Schritt 5:** Falscher, stabiler Wert:
- Geber falsch eingestellt (Hebellänge passt nicht zur Tankhöhe)
- Geber für falschen Widerstandsbereich (VDO-Europa: 10–180 Ω, US: 33–240 Ω, Wema: 0–190 Ω)
- Nicht-lineare Tankform mit linearem Geber → programmierbaren Geber verwenden

### 7.5 Entscheidungsbaum: Wasser im Tank

**Ausgangssituation:** Verdacht auf Wasser im Kraftstofftank.

**Schritt 1:** Wie wurde Wasser festgestellt?
- **Wasserabscheider ist voll** → Schritt 2
- **Motor raucht weiß** → Wasser in Brennkammer → Schritt 2
- **Kraftstoff milchig-trüb** → Emulsion (→ F11) → Schritt 2
- **Diesel-Bug diagnostiziert** → Wasser als Ursache (→ F02) → Schritt 2

**Schritt 2:** Wassermenge bestimmen:
- Tankablassventil öffnen (tiefster Punkt), in durchsichtiges Gefäß ablassen
- Wasser sinkt unter Diesel (Wasser: 1,0 g/cm³, Diesel: 0,84 g/cm³)
- **<1 cm Wasser im Glas** → Geringe Menge, Kondensat → Schritt 3
- **>1 cm Wasser** → Erhebliche Menge, externe Quelle → Schritt 4

**Schritt 3:** Geringe Wassermenge (Kondensat):
- Normal bei teilgefüllten Tanks in feuchten Klimazonen
- Prävention: Tank voll halten, Belüftung mit Trockenmittel-Filter
- Behandlung: Wasserabscheider einbauen (Racor 500FG, Separ 2000), regelmäßig am Ablassventil entwässern
- Additiv: Wasseremulgierer (z.B. Liqui Moly Marine Diesel Protect) bindet kleine Wassermengen und führt sie der Verbrennung zu — NUR bei <500 ppm Wasser!

**Schritt 4:** Erhebliche Wassermenge — Woher kommt das Wasser?
- **Einfüllstutzen-Dichtung prüfen:** Dicht bei Regenwasser und Deckswäsche?
- **Entlüftungsöffnung:** Liegt sie über der Wasserlinie bei Krängung? Anti-Siphon-Schleife vorhanden?
- **Tankdeckel/Inspektionsöffnung:** Dichtung intakt?
- **Kondensation:** Bei großen Temperaturunterschieden (Tag/Nacht) und halbleerem Tank → bis zu 50 ml/Tag möglich in tropischem Klima
- **Kraftstoff bei Lieferung bereits wasserhaltig:** Probe VOR dem Tanken ziehen (bei Bunkerstation, tragbaren Kanistern)

---

## 8. FAQ

### 8.1 Grundlagen

**F: Welches Tankmaterial ist für mein Boot am besten geeignet?**

A: Die Wahl hängt von mehreren Faktoren ab: Bootsgröße, Kraftstoffart, Budget, Gewichtsanforderungen und Einbausituation. Als Faustregel: Boote bis 10m mit Diesel → PE-HD (kostengünstig, korrosionsfrei). Segelyachten 10–15m → Edelstahl 316L (langlebig, geringes Volumen). Motoryachten >15m → Edelstahl 316L oder Aluminium 5083 (maßgefertigt). Rennboote/Gewichtsoptimierung → Aluminium 5083 oder Bladder. Benzinboote → Fluoriertes PE-HD oder Edelstahl 316L. Niemals Aluminium für Benzin verwenden, wenn Ethanol-haltige Kraftstoffe (E10) möglich sind — Ethanol greift die Oxidschicht an.

**F: Wie oft muss ein Kraftstofftank inspiziert werden?**

A: Jährlich: Äußere Sichtprüfung auf Korrosion, Leckage, Verformung. Alle 3 Jahre: Tankablassventil betätigen und Wassergehalt prüfen. Alle 5 Jahre: Tankinneninspektion (Inspektionsöffnung), Tankgeber prüfen. Alle 10 Jahre: Wandstärkenmessung (Ultraschall) bei Metalltanks. Bei Tankproblemen oder nach Grundberührung: Sofortinspektion.

**F: Kann ich einen Aluminiumtank für Benzin verwenden?**

A: Grundsätzlich ja, Aluminium 5083 ist benzinbeständig. ABER: Modernes Benzin enthält bis zu 10% Ethanol (E10), und Ethanol greift die Aluminiumoxidschicht an und verursacht beschleunigte Korrosion. In den USA empfiehlt ABYC H-24 daher Aluminium NICHT für E10-Benzin ohne spezielle Innenbeschichtung. In Europa ist E10 seit 2011 Standard — Aluminiumtanks für Benzin werden daher nicht empfohlen. Verwenden Sie stattdessen Edelstahl 316L oder fluoriertes PE-HD.

**F: Was ist der Unterschied zwischen ISO 21487 und ISO 10088?**

A: ISO 21487 regelt die fest eingebauten Kraftstofftanks selbst (Kunststoff UND Metall), ISO 10088 regelt das gesamte Kraftstoffsystem (Tanks, Leitungen, Anschlüsse, Entlüftung). In der Praxis müssen beide Normen erfüllt werden — ISO 21487 für den Tank selbst, ISO 10088 für das System.

**F: Brauche ich Schwallbleche im Tank?**

A: Nach ISO 10088 und ABYC H-24/H-33: Ja, wenn eine Tankdimension >750mm (ISO) bzw. >30" (762mm, ABYC) beträgt. Schwallbleche reduzieren die freien Oberflächen im Tank und damit die Auswirkung des freien Oberflächeneffekts auf die Stabilität. Auch unterhalb der Normgrenzen sind Schwallbleche empfehlenswert, da sie Kraftstoff-Schwappen reduzieren und den Tankgeber stabilisieren.

### 8.2 Materialfragen

**F: Warum ist 316L besser als 304 für Tankanwendungen?**

A: 316L enthält 2–3% Molybdän, das die Lochfraßbeständigkeit signifikant erhöht (PREN 26 vs. 18). Im marinen Umfeld, wo Chloride allgegenwärtig sind (Salzluft, Kondensat, Bilgenwasser), ist dieser Unterschied entscheidend. 304 korrodiert im Bilgenbereich eines Bootes erfahrungsgemäß innerhalb von 5–10 Jahren, 316L hält 25–40 Jahre. Der Preisunterschied beträgt ca. 15–25% — bei einer Investition, die 25 Jahre halten soll, ist das irrelevant.

**F: Kann ich meinen Aluminiumtank reparieren?**

A: Ja, ABER: nur durch einen zertifizierten Aluminium-Schweißer (Qualifikation nach EN ISO 9606-2). Kritische Punkte: NUR AlMg5 (5183) als Zusatzwerkstoff verwenden, niemals AlSi5 (4043). Tank muss vollständig entgast sein (Explosionsgefahr!). Betroffene Stelle muss bis auf sauberes Material geschliffen werden. Nach der Reparatur: Drucktest. Bei großflächiger Korrosion (>20% der Oberfläche) ist ein Austausch wirtschaftlicher.

**F: Ist GFK für Dieseltanks sicher?**

A: Mit dem richtigen Harz: Ja. Vinylester (z.B. Derakane 411) und Epoxid sind beständig gegen Diesel, einschließlich B7-Biodiesel. Orthophthal-Polyester ist NICHT geeignet — es wird von Diesel (besonders mit FAME-Anteil) angegriffen. Isophthal-Polyester ist befriedigend für reinen Mineralöl-Diesel, wird aber seit der Einführung von B7 nicht mehr empfohlen.

**F: Wie erkenne ich, ob mein PE-Tank fluoriert ist?**

A: Fluorierte Tanks haben typisch eine leicht gelblich-braune Innenwand, während unfluorierte Tanks innen die gleiche Farbe wie außen haben (schwarz oder weiß). Sicherer Test: Kratzen Sie mit einem Messer an der Tankinnenside — fluoriertes PE hat eine dünne, härtere Oberfläche, die sich anders anfühlt. Am sichersten: Herstellerangabe prüfen — fluorierte Tanks sind immer als solche gekennzeichnet (Label, Stempel).

### 8.3 Installation und Betrieb

**F: Wie befestige ich einen PE-Tank korrekt?**

A: PE-Tanks dürfen NICHT durchbohrt werden für Befestigungen (Schwachstelle!). Verwenden Sie Edelstahl-Spannbänder (min. 25mm breit) mit EPDM-Unterlage, die den Tank gegen eine feste Auflage (GFK-Lagerbett oder Holzrahmen mit Neopren-Pads) drücken. Der Tank muss in alle Richtungen gegen Verrutschen gesichert sein. Spannbänder nicht zu fest anziehen — PE verformt sich unter Dauerlast (Kriechen). Auflagefläche muss eben und frei von scharfen Kanten sein.

**F: Darf die Kraftstoff-Entnahme durch den Tankboden erfolgen?**

A: ISO 10088 und ABYC empfehlen, dass die Entnahme NICHT durch den Tankboden erfolgt — eine Undichtigkeit am Bodenanschluss würde zum vollständigen Auslaufen des Tanks führen. Bevorzugt: Top-Feed mit Steigrohr (Saugrohr von oben) oder seitlicher Anschluss oberhalb des Tankbodens. Wenn ein Bodenanschluss unvermeidbar ist: doppelwandiger Stutzen mit integriertem Absperrventil direkt am Tank.

**F: Wie groß muss die Inspektionsöffnung sein?**

A: ISO 10088 empfiehlt min. 100×150mm. In der Praxis sollte die Öffnung groß genug sein, um eine Hand mit einem Schwamm einzuführen (Reinigung) oder eine Endoskop-Kamera einzusetzen. Für größere Tanks (>500l): 150mm oder 200mm Durchmesser. Runde Inspektionsdeckel mit O-Ring-Dichtung sind quadratischen vorzuziehen (weniger Spannungskonzentration).

**F: Wie verhindere ich Diesel-Bug in meinem Tank?**

A: Fünf Maßnahmen in Kombination: 1) Tank voll halten bei Nichtbenutzung (reduziert Kondensat-Fläche). 2) Wasserabscheider im Kraftstoffsystem installieren (Racor 500FG oder Separ 2000). 3) Regelmäßig am Tankablassventil Wasser ablassen (monatlich im Sommer). 4) Prophylaktisch Biozid zusetzen (Grotamar 82, 5ml/100l bei jeder Betankung). 5) Kraftstoff nach Saison-Ende über Polishing-System umwälzen.

**F: Mein Tank hat keine Inspektionsöffnung — kann ich eine nachrüsten?**

A: Bei Metalltanks (Edelstahl, Alu): Ja, durch einen Fachbetrieb. Es wird eine kreisrunde Öffnung ausgeschnitten und ein Flansch mit O-Ring-Dichtung eingeschweißt. Kosten: ca. 300–800 EUR je nach Zugänglichkeit. Bei PE-Tanks: Schwieriger, da PE nicht geschweißt werden kann. Es gibt Nachrüst-Inspektionsdeckel, die mit einem Lochsäge eingesetzt und verschraubt werden (z.B. Vetus, Art.-Nr. INSPEC150). Bei GFK-Tanks: Ja, durch Einlaminieren eines Flansches.

**F: Wie berechne ich die erforderliche Tankgröße?**

A: Faustformel für Motorboote: Tank-Kapazität [l] = Motorleistung [kW] × spez. Verbrauch [l/kWh] × gewünschte Reichweite [h] × 1,3 (30% Reserve). Typische Werte: Diesel-Innenborder 0,22 l/kWh bei Marschfahrt, Benzin-Außenborder 0,40 l/kWh bei Marschfahrt. Beispiel: 100 kW Diesel, 8h Reichweite → 100 × 0,22 × 8 × 1,3 = 229 l → 250l Tank. Für Segelyachten: Motorlaufzeit pro Saison × Verbrauch × 1,5 Reserve.

### 8.4 Wartung und Reparatur

**F: Wie reinige ich einen Kraftstofftank?**

A: 1) Tank vollständig ablassen. 2) Mit dieselverträglichem Reiniger (z.B. Liqui Moly Marine Diesel System Reiniger, Star Brite Diesel Tank Cleaner) befüllen und einwirken lassen (24h). 3) Ablassen und mit klarem Diesel durchspülen. 4) Bei starker Verschmutzung (Diesel-Bug): Inspektionsöffnung öffnen, Biofilm mechanisch mit Schwamm/Bürste entfernen. 5) Abschließend Biozid zusetzen. WARNUNG: Niemals mit Wasser spülen (hinterlässt Restfeuchtigkeit)! Niemals mit Lösemitteln spülen (greift Dichtungen und PE an)!

**F: Mein Aluminiumtank hat weiße Flecken — ist das gefährlich?**

A: Weiße Flecken auf Aluminium sind Aluminiumhydroxid (Al(OH)₃) — ein Zeichen für aktive Korrosion. Handlungsbedarf: Sofort die Ursache klären (galvanischer Kontakt? Feuchtigkeit? Bilgenwasser-Kontakt?). Wandstärke per Ultraschall messen. Wenn >70% der Originalstärke noch vorhanden: Ursache beseitigen, Galvanische Isolation herstellen, Opferanode installieren. Wenn <70%: Reparatur oder Austausch planen.

**F: Wie oft muss der Tankgeber gewechselt werden?**

A: Schwimmer-Tankgeber (Widerstandsgeber): Lebensdauer typisch 8–15 Jahre. Ersatz bei: springender Anzeige, falscher Anzeige trotz korrekter Verkabelung, sichtbarer Korrosion am Widerstandselement. Kapazitive Tankgeber: Lebensdauer typisch 15–25 Jahre. Ultraschall-Tankgeber: Lebensdauer typisch 20+ Jahre. Prophylaktischer Tausch empfohlen nach 10 Jahren (Schwimmer) bzw. 20 Jahren (kapazitiv/Ultraschall).

**F: Kann ich Benzin in einen Dieseltank füllen?**

A: NEIN — niemals! Diesel hat ein deutlich anderes chemisches Profil als Benzin. Aber: Wenn es versehentlich geschehen ist: Motor NICHT starten! Tank sofort vollständig ablassen, alle Leitungen und Filter spülen, mit frischem Diesel befüllen. Wenn der Motor bereits gelaufen ist: Injektoren und Einspritzpumpe können geschädigt sein (Diesel schmiert, Benzin nicht → Trockenlauf → Verschleiß). Schadenspotenzial: 2.000–15.000 EUR je nach Motor.

**F: Was passiert, wenn ich E10 in meinen Tank fülle, der nicht dafür zugelassen ist?**

A: Ethanol (10 Vol.-%) greift bestimmte Materialien an: Aluminium (Oxidschicht wird angegriffen), bestimmte Dichtungen (Viton A nicht beständig, Viton B oder FFKM erforderlich), Orthophthal-Polyester (Quellung), alte Kraftstoffschläuche ohne Ethanol-Barriere. PE-HD und Edelstahl 316L sind E10-beständig. Bei Verdacht: Tank sofort leeren und Material prüfen.

### 8.5 Spezialfragen

**F: Wie funktioniert ein Kraftstoff-Polishing-System?**

A: Ein Polishing-System zirkuliert den Kraftstoff aus dem Tank durch ein Filtersystem (typisch 2µm Absolutfilter + Koaleszenz-Wasserabscheider) und zurück in den Tank. Empfohlene Umwälzrate: gesamter Tankinhalt 1× pro 4 Stunden. Systeme: Racor PFF5790 (240 l/h, ca. 1.200 EUR), Separ FILTER BOSS (300 l/h, ca. 1.500 EUR), Algae-X SPS (500 l/h, ca. 2.200 EUR). Einsatz: vor der Saison 24h laufen lassen, nach dem Tanken 4h laufen lassen.

**F: Mein Tank hat keinen Ablassventil — wie kann ich Wasser ablassen?**

A: Vier Optionen: 1) Handpumpe durch den Tankgeber-Flansch einführen und am Tankboden absaugen. 2) Ablassventil nachrüsten (am tiefsten Punkt, Fachbetrieb erforderlich). 3) Kraftstoff über Polishing-System mit Wasserabscheider reinigen. 4) Transfer-Pumpe: gesamten Inhalt in Fässer pumpen, Tank reinigen, gefilterten Kraftstoff zurückpumpen. Option 2 wird langfristig empfohlen.

**F: Wie lagere ich mein Boot über den Winter mit vollem/leerem Tank?**

A: IMMER mit VOLLEM Tank überwintern! Begründung: Ein voller Tank hat minimale Luftfläche → minimales Kondensat. Ein leerer Tank "atmet" — warme feuchte Luft dringt ein, kühlt ab, Wasser kondensiert → Korrosion, Diesel-Bug. Zusätzlich: Biozid zusetzen (Grotamar 82, 10ml/100l = Winterdosis). Kraftstoff-Stabilisator zusetzen (verhindert Oxidation über 6 Monate). Wasserabscheider vor dem Einwintern leeren.

**F: Was kostet ein Tank-Austausch?**

A: Die Kosten variieren enorm nach Zugänglichkeit: Frei zugänglicher Tank (Maschinenraum, große Luke): Material 800–3.000 EUR + Arbeit 500–1.500 EUR = 1.300–4.500 EUR. Eingebauter Tank unter Kabinenboden: Material 800–3.000 EUR + Demontage/Montage 2.000–8.000 EUR = 2.800–11.000 EUR. Integrationstank (GFK): Material + Arbeit 8.000–25.000 EUR (faktisch Rumpf-Umbau). Schwer zugänglicher Tank (z.B. unter Motor): Material + Arbeit 5.000–20.000 EUR (Motor muss ausgebaut werden).

**F: Kann ich meinen Kraftstofftank selbst einbauen?**

A: Grundsätzlich ja, ABER: Bei CE-gekennzeichneten Booten kann ein nicht normgerechter Einbau die CE-Konformität aufheben. Bei Versicherungsschäden prüft der Sachverständige die Installation. Empfehlung: Einbau durch Fachbetrieb oder unter Aufsicht eines Sachverständigen. Mindestens: ISO 10088 und ABYC H-24/H-33 als Referenz verwenden, alle Anschlüsse auf Dichtheit prüfen (0,3 bar Drucktest, 5 min), Entlüftung korrekt verlegen, Erdung herstellen, Inspektion dokumentieren.

**F: Wie viel Kraftstoff verbraucht mein Boot auf 100 Seemeilen?**

A: Dies hängt stark von Bootstyp, Geschwindigkeit und Motor ab. Richtwerte bei Marschfahrt:

| Bootstyp | Geschwindigkeit | Verbrauch/100 sm |
|----------|----------------|-----------------|
| Segelyacht 10m (unter Motor) | 6 kn | 25–40 l Diesel |
| Segelyacht 14m (unter Motor) | 6,5 kn | 35–60 l Diesel |
| Verdränger-Motorboot 10m | 8 kn | 50–80 l Diesel |
| Verdränger-Motorboot 14m | 9 kn | 80–140 l Diesel |
| Halbgleiter 10m | 18 kn | 120–200 l Diesel |
| Gleiter 8m | 25 kn | 200–350 l Benzin |
| Gleiter 10m | 28 kn | 300–500 l Benzin |

**F: Was ist der freie Oberflächeneffekt und warum sind Schwallbleche wichtig?**

A: Der freie Oberflächeneffekt (Free Surface Effect, FSE) beschreibt die Stabilitätsminderung durch Flüssigkeiten in teilgefüllten Tanks. Wenn ein Boot krängt, verschiebt sich der Kraftstoff zur tieferen Seite — dies verschiebt den Schwerpunkt und verstärkt die Krängung. Die Stabilitätsminderung ist proportional zur dritten Potenz der Tankbreite! Ein Schwallblech teilt den Tank in zwei Hälften → die effektive Breite jeder Hälfte halbiert sich → der FSE reduziert sich auf 1/4 (= 2 × (1/2)³, da zwei halb so breite Abteilungen entstehen). Daher sind Schwallbleche bei breiten Tanks besonders wichtig.

---

### 8.6 Regulatorische und rechtliche Fragen

**F: Braucht mein Tank ein CE-Zertifikat?**

A: Ein Tank als Einzelkomponente benötigt kein CE-Zertifikat. ABER: Das gesamte Boot muss CE-konform sein (Sportbootrichtlinie 2013/53/EU). Ein Tank, der die relevanten Normen (ISO 21487 für Kunststoff- und Metalltanks, ISO 10088 für das System) nicht erfüllt, gefährdet die CE-Konformität des Bootes. Bei einem Tankwechsel ist der Bootseigner dafür verantwortlich, dass die CE-Konformität erhalten bleibt. Im Schadensfall prüft der Versicherungssachverständige die Installation.

**F: Ist ein Tanktausch meldepflichtig?**

A: In Deutschland nicht gesondert meldepflichtig, ABER: Wenn das Boot CE-gekennzeichnet ist und der Tank Teil des Kraftstoffsystems ist, muss die technische Dokumentation aktualisiert werden. Bei Versicherungsschäden verlangt der Sachverständige Nachweise der fachgerechten Installation. Empfehlung: Tankwechsel durch Fachbetrieb durchführen lassen und Dokumentation (Drucktest-Protokoll, Werkstoffzeugnis, Installationsfotos) aufbewahren.

**F: Wer darf einen Kraftstofftank schweißen?**

A: Schweißer müssen nach EN ISO 9606-1 (Stahl/Edelstahl) bzw. EN ISO 9606-2 (Aluminium) qualifiziert sein. Die Qualifikation muss den spezifischen Werkstoff und das Schweißverfahren abdecken. Ein Stahlschweißer darf NICHT automatisch Edelstahl oder Aluminium schweißen. Die Schweißerqualifikation muss gültig sein (Verlängerung alle 2 Jahre bei fortlaufender Tätigkeit, alle 3 Jahre mit Prüfung). Für Benzintanks gelten verschärfte Anforderungen: vollständige Nahtprüfung (100% Sichtprüfung, Drucktest) ist Pflicht.

**F: Was passiert bei einem Kraftstoffaustritt in der Marina?**

A: In Deutschland: Sofort die Feuerwehr (112) und die Hafenmeisterei benachrichtigen. Eigene Ölsperren (Absorber-Pads, Ölschläuche) ausbringen. Bußgelder nach WHG (Wasserhaushaltsgesetz): 5.000–500.000 EUR je nach Menge und Gewässer. Kosten für professionelle Sanierung: 5.000–80.000 EUR. Die Haftpflichtversicherung des Bootes deckt in der Regel Gewässerschäden bis zur Deckungssumme — ABER: Bei nachweislicher Fahrlässigkeit (z.B. bekannter, nicht reparierter Tankdefekt) kann der Versicherer die Leistung kürzen oder ablehnen.

**F: Darf ich Dieselkraftstoff in Kanistern auf dem Boot lagern?**

A: In begrenztem Umfang ja, ABER: Kanister müssen als Gefahrgutbehälter zugelassen sein (UN-Zulassung, typisch UN 3H1 für Kunststoff). Lagerort muss gut belüftet und gegen Umkippen gesichert sein. Empfehlung: maximal 20l in zugelassenen Kanistern, fest verzurrt, nicht in Kabinen oder geschlossenen Räumen. Benzin in Kanistern an Bord: nur in homologierten Reservekanistern (z.B. Fuel Friend UN-zertifiziert, max. 20l), und nur an Deck oder in belüfteten Lockers.

### 8.7 Spezielle Materialfragen

**F: Warum wird Aluminium 6061-T6 für Bootstanks nicht empfohlen?**

A: Aluminium 6061-T6 enthält mehr Kupfer (0,15–0,40%) als 5083 (max. 0,10%) und ist damit anfälliger für Lochfraßkorrosion in Salzwasseratmosphäre. Zudem ist 6061-T6 in der Wärmeeinflusszone nach dem Schweißen nur noch auf T0-Festigkeit — die aufwendige Wärmebehandlung (T6) geht verloren. 5083-O ist im Zustand "weich geglüht" und verliert durch Schweißen keine Festigkeit. Fazit: 5083 ist in jeder Hinsicht überlegen für Marine-Tanks.

**F: Kann ich meinen GFK-Integrationstank mit Epoxid abdichten?**

A: Ja, Epoxid ist eine hervorragende Barriere gegen Diesel-Permeation. Vorgehensweise: 1) Tank vollständig ablassen und trocknen (min. 1 Woche bei Belüftung). 2) Tankinnenside anschleifen (P80). 3) Mit Aceton entfetten. 4) 2–3 Schichten Epoxid-Barriere-Coat auftragen (z.B. WEST System 105/206 + 422 Barrier Coat Additiv). 5) Aushärten lassen (min. 7 Tage bei 20°C). 6) Drucktest. Kosten: ca. 200–400 EUR Material + 500–1.000 EUR Arbeit. WARNUNG: Nur möglich, wenn die Tankinnenseite zugänglich ist (Inspektionsöffnung min. 200mm).

**F: Gibt es Edelstahl-Legierungen, die besser sind als 316L für Tanks?**

A: Ja: Duplex-Stahl 2205 (1.4462) hat PREN ~35 (vs. 26 für 316L) und ist damit noch korrosionsbeständiger. Wird im Superyachtbau und für besonders aggressive Umgebungen (tropisch, bilgenwassernah) eingesetzt. Nachteil: ca. 30% teurer als 316L und schwieriger zu schweißen. Für die meisten Yachten unter 20m ist 316L ausreichend. Superaustenitischer Stahl 254 SMO (1.4547, PREN ~43) wird gelegentlich für Superyacht-Tanks eingesetzt — Preis ca. doppelt so hoch wie 316L.

**F: Ist Edelstahl 316 (ohne L) auch geeignet?**

A: 316 (ohne "L") hat einen Kohlenstoffgehalt von max. 0,08% (vs. 0,03% bei 316L). Dies erhöht die Anfälligkeit für interkristalline Korrosion nach dem Schweißen, da Chromkarbide an den Korngrenzen ausgeschieden werden. Für ungeschweißte Tanks (z.B. tiefgezogene Tanks) ist 316 akzeptabel. Für geschweißte Tanks IMMER 316L verwenden.

**F: Was ist der Unterschied zwischen PE-HD, PE-LD und PE-XLPE?**

A: PE-LD (Low Density, 0,91–0,94 g/cm³): Zu weich und zu durchlässig für Kraftstofftanks — NICHT verwenden. PE-HD (High Density, 0,94–0,96 g/cm³): Standard für Rotomoulding-Tanks. Gute Festigkeit und akzeptable Permeation. PE-XLPE (Cross-Linked, vernetztes PE): Durch Bestrahlung oder Peroxid vernetzt, höhere chemische Beständigkeit und geringere Permeation als PE-HD. Wird besonders für Benzintanks verwendet (USCG-Anforderung). Preis ca. 20–30% höher als PE-HD.

### 8.8 Praxistipps

**F: Wie verhindere ich Kondenswasser im Tank am effektivsten?**

A: Die drei wirksamsten Maßnahmen in Reihenfolge der Effektivität: 1) Tank VOLL halten — die größte Einzelmaßnahme. Ein voller Tank hat keine Luftfläche → kein Kondensat. 2) Trockenmittelfilter in der Belüftungsleitung — Silicagel-Kartusche (z.B. Desi-Dry Marine, ca. 35 EUR) entzieht der einströmenden Luft Feuchtigkeit. Alle 3–6 Monate regenerieren (im Backofen bei 120°C, 4h). 3) Regelmäßig Wasser am Ablassventil ablassen — monatlich im Sommer, vor und nach dem Winter.

**F: Mein Tank riecht nach Schwefelwasserstoff (faule Eier) — was tun?**

A: Schwefelwasserstoff (H₂S) ist ein Stoffwechselprodukt von anaeroben Bakterien (Diesel-Bug, speziell Desulfovibrio desulfuricans). H₂S ist giftig (MAK-Wert 10 ppm) und korrosiv. Maßnahmen: 1) Gut belüften — H₂S ist schwerer als Luft und sammelt sich in der Bilge! 2) Tank als schwer kontaminiert einstufen → vollständige Reinigung und Biozid-Behandlung (→ F02). 3) Nach der Reinigung: Kraftstoffprobe an Labor senden zur Keimzahlbestimmung. 4) Korrosionszustand des Tanks prüfen — H₂S erzeugt schwefelbasierte Korrosion (Sulfidation), besonders aggressiv auf Aluminium und Kupferlegierungen.

**F: Kann ich den Tank meines Bootes vergrößern?**

A: Grundsätzlich ja, aber mit Einschränkungen: 1) Trimm und Stabilität prüfen — ein größerer Tank verändert die Gewichtsverteilung. 2) CE-Konformität beachten — der Stabilitätsnachweis muss ggf. neu gerechnet werden. 3) Strukturelle Belastung — ein schwererer Tank braucht stärkere Befestigung und ggf. verstärktes Fundament. 4) Zugang — der neue Tank muss durch vorhandene Öffnungen passen. Alternative: Zusatztank (z.B. Bladder) als Ergänzung installieren. Für Langfahrt eine beliebte Option: 100–200l Bladder unter der Vorschiffkoje.

**F: Wie prüfe ich die Wandstärke meines Metalltanks ohne Ausbau?**

A: Mit einem Ultraschall-Dickenmessgerät (z.B. Elcometer DG26, ca. 800 EUR, oder mietbar ab 50 EUR/Tag). Vorgehensweise: 1) Tankaußenfläche reinigen (Fett, Farbe entfernen am Messpunkt). 2) Koppelpaste auftragen. 3) Sonde aufsetzen, Messwert ablesen. 4) An mind. 10 Punkten messen (Boden, Seitenwände, Ecken, nahe Schweißnähten). 5) Ergebnisse mit der Original-Wandstärke vergleichen (Datenblatt oder Messung an der dicksten Stelle). Ein Wandstärkenverlust von >20% erfordert Maßnahmen, >50% erfordert Reparatur oder Austausch.

## 9. Glossar

| Begriff | Definition |
|---------|-----------|
| **Absetzttank** | Tank, in dem Kraftstoff ruht, damit Wasser und Sediment durch Schwerkraft absinken können |
| **ABYC** | American Boat and Yacht Council — Organisation für US-Bootsstandards |
| **Anti-Siphon-Schleife** | U-förmige Leitungsführung, die verhindert, dass Wasser über die Entlüftung in den Tank siphoniert |
| **Baffle** | Schwallblech — Trennwand im Tank zur Reduzierung des freien Oberflächeneffekts |
| **Bilge** | Tiefster Bereich im Bootsinneren, in dem sich Wasser und Leckagen sammeln |
| **Biodiesel (FAME)** | Fettsäuremethylester — biogener Dieselkraftstoff, in EN 590 bis 7% beigemischt (B7) |
| **Bladder** | Flexibler Kraftstofftank aus beschichtetem Gewebe |
| **BSP** | British Standard Pipe — Gewindestandard für Rohranschlüsse (zylindrisch oder konisch) |
| **CE-Kennzeichnung** | Conformité Européenne — EU-Konformitätszeichen nach Sportbootrichtlinie 2013/53/EU |
| **Diesel-Bug** | Mikrobieller Befall im Diesel-Kraftstoffsystem durch Pilze, Bakterien und Hefen |
| **Drucktest** | Prüfung der Tankdichtheit durch Aufbringen eines definierten Überdrucks |
| **Einfüllstutzen** | Verschließbare Öffnung zum Befüllen des Tanks |
| **Elektrolyse** | Elektrochemischer Korrosionsprozess zwischen verschiedenen Metallen in einem Elektrolyt |
| **EN 590** | Europäische Norm für Dieselkraftstoff (inkl. max. 7% FAME) |
| **Entlüftung** | Leitungssystem zum Druckausgleich zwischen Tankinnenraum und Außenatmosphäre |
| **ESCR** | Environmental Stress Crack Resistance — Beständigkeit gegen umweltbedingte Spannungsrisskorrosion |
| **FAME** | Fatty Acid Methyl Ester — chemische Bezeichnung für Biodiesel |
| **Flammensperre** | Drahtgeflecht in der Entlüftungsleitung, das eine Flammenrückschlag in den Tank verhindert |
| **Fluorierung** | Oberflächenbehandlung von PE-Tanks mit elementarem Fluor zur Reduzierung der Permeation |
| **Formiergas** | Schutzgas (Argon oder Argon/Wasserstoff) auf der Wurzelseite beim Schweißen |
| **FSE** | Free Surface Effect — Stabilitätsminderung durch Flüssigkeiten in teilgefüllten Tanks |
| **Galvanische Korrosion** | Korrosion durch Kontakt verschiedener Metalle in einem Elektrolyt |
| **Grotamar 82** | Biozid-Additiv für Diesel zur Bekämpfung und Prävention von Diesel-Bug |
| **Inspektionsöffnung** | Verschließbare Öffnung im Tank für Inspektion, Reinigung und Wartung |
| **ISO 10088** | Internationale Norm für fest eingebaute Kraftstoffsysteme in Sportbooten |
| **ISO 21487** | Internationale Norm für Kunststoff-Kraftstofftanks in Sportbooten |
| **Koaleszenz** | Zusammenfließen kleiner Wassertröpfchen zu größeren, die dann abgeschieden werden können |
| **Lochfraß** | Lokale Korrosionsform, die kleine, tiefe Löcher in der Metalloberfläche erzeugt |
| **NPT** | National Pipe Thread — US-amerikanischer Gewindestandard für Rohranschlüsse (konisch) |
| **P/V-Ventil** | Pressure/Vacuum Relief Valve — Über-/Unterdruckventil für Tankbelüftung |
| **PE-HD** | Polyethylen hoher Dichte — Kunststoff für Rotomoulding-Tanks |
| **Permeation** | Diffusion von Kraftstoffmolekülen durch die Tankwand |
| **PREN** | Pitting Resistance Equivalent Number — Maßzahl für die Lochfraßbeständigkeit von Edelstahl |
| **Polishing** | Zirkulation von Kraftstoff durch Feinstfilter zur Reinigung |
| **Rotomoulding** | Rotationsschmelzverfahren zur Herstellung nahtloser Kunststofftanks |
| **Schwallblech** | Trennwand im Tank zur Reduzierung von Kraftstoffbewegung bei Seegang |
| **Steigrohr** | Rohr von der Tankentnahme-Öffnung (oben) bis nahe an den Tankboden |
| **Sulfonierung** | Oberflächenbehandlung von PE-Tanks mit Schwefelsäure zur Reduzierung der Permeation |
| **Tagestank** | Kleiner Vorratstank zwischen Haupttank und Motor |
| **UEG** | Untere Explosionsgrenze — niedrigste Konzentration eines brennbaren Gases in Luft, bei der Zündung möglich ist |
| **ULSD** | Ultra Low Sulfur Diesel — Diesel mit max. 10 ppm Schwefel (EN 590 Standard seit 2009) |
| **Vinylester** | Chemisch beständiges Harz für kraftstoffbeständige GFK-Laminate |
| **WEZ** | Wärmeeinflusszone — Bereich neben der Schweißnaht mit veränderten Materialeigenschaften |
| **WIG** | Wolfram-Inertgas-Schweißen (= TIG) — bevorzugtes Schweißverfahren für Tankschweißungen |
| **Xenon-Belichtung** | Beschleunigte Alterungsprüfung mit Xenon-Lampen, die das Sonnenlichtspektrum simulieren (ISO 4892-2) |
| **316L** | Austenitischer Chrom-Nickel-Molybdän-Edelstahl mit niedrigem Kohlenstoffgehalt, Werkstoffnummer 1.4404 |
| **5083** | Aluminium-Magnesium-Legierung (AlMg4,5Mn0,7) mit hervorragender Seewasserbeständigkeit |
| **Anodische Korrosion** | Korrosion des unedleren Metalls in einem galvanischen Element (z.B. Aluminium bei Kontakt mit Edelstahl) |
| **Tankfundament** | Strukturelles Auflager (GFK, Holz oder Metall), auf dem der Tank befestigt wird |
| **Schwerkraftfütterung** | Kraftstoffversorgung des Motors allein durch die Höhendifferenz zwischen Tank und Motor (ohne Pumpe) |
| **Transferpumpe** | Elektrische oder manuelle Pumpe zum Umpumpen von Kraftstoff zwischen Tanks oder vom Haupttank zum Tagestank |
| **Spannband** | Edelstahl-Band zur Befestigung von PE-Tanks, typisch 25–40mm breit, mit Spannschloss |
| **Neopren-Pad** | Elastisches Polster (Chloroprenkautschuk) zur galvanischen Isolation und Vibrationsdämpfung zwischen Tank und Halterung |
| **Tankpolishing** | Zirkulation des Tankinhalts durch ein Filtersystem zur Reinigung (Partikelentfernung, Wasserabscheidung) |
| **Steigrohr** | Vertikales Rohr innerhalb des Tanks, das von einem oberen Anschluss bis nahe an den Tankboden reicht und die Kraftstoffansaugung ermöglicht |
| **Schauglas** | Transparentes Rohrstück oder Fenster zur visuellen Kontrolle des Kraftstoffniveaus oder der Kraftstoffqualität |
| **Beruhigungsrohr** | Rohr um den Rücklaufanschluss im Tank, das verhindert, dass der zurücklaufende Kraftstoff den Tankgeber stört |
| **Demulgator** | Additiv, das die Trennung von Wasser und Kraftstoff (Emulsionsbrechung) beschleunigt |
| **Emulgator** | Additiv, das kleine Wassermengen im Kraftstoff fein verteilt, damit sie in der Verbrennung unschädlich verdampfen |
| **Cetanzahl** | Maß für die Zündwilligkeit von Dieselkraftstoff — höhere Cetanzahl = kürzere Zündverzögerung, ruhigerer Lauf |
| **Wasserabscheider** | Filter mit Koaleszenz-Element, der freies und emulgiertes Wasser aus dem Kraftstoff abtrennt |
| **Primärfilter** | Erster Kraftstofffilter im System (typisch 30µm), schützt die Einspritzpumpe vor groben Partikeln |
| **Sekundärfilter** | Zweiter Kraftstofffilter (typisch 2–10µm), schützt die Einspritzdüsen vor feinen Partikeln |
| **Saugrohr** | Siehe Steigrohr — Rohr zur Kraftstoffentnahme von oben in den Tank hinein |
| **Karl-Fischer-Titration** | Analytisches Verfahren zur präzisen Bestimmung des Wassergehalts in Kraftstoff (ppm-genau) |
| **ISO-Partikelzählung** | Klassifizierung der Partikelbelastung im Kraftstoff nach ISO 4406 (z.B. 18/16/13 für grob/mittel/fein) |
| **Derakane** | Handelsname für Vinylester-Harze von Ashland Chemical, Typ 411 als Standard für kraftstoffbeständige Laminate |
| **Tankentgasung** | Entfernung aller Kraftstoffdämpfe aus einem leeren Tank vor Schweiß- oder Schneidarbeiten (Explosionsgefahr!) |
| **Inertisgierung** | Füllung eines Tanks mit Inertgas (N₂, CO₂) vor Heißarbeiten zur Vermeidung von Explosionen |

---

### 9.2 Abkürzungsverzeichnis

| Abkürzung | Bedeutung |
|-----------|-----------|
| ABYC | American Boat and Yacht Council |
| ASTM | American Society for Testing and Materials |
| BSP | British Standard Pipe (Gewindeform) |
| BSS | Boat Safety Scheme (UK) |
| CE | Conformité Européenne |
| CFR | Code of Federal Regulations (USA) |
| CSM | Chopped Strand Mat (Glasfasermatte) |
| EN | Europäische Norm |
| EPA | Environmental Protection Agency (USA) |
| EPDM | Ethylen-Propylen-Dien-Kautschuk |
| FAME | Fatty Acid Methyl Ester (Biodiesel) |
| FRP | Fiber Reinforced Plastic |
| FSE | Free Surface Effect |
| GFK | Glasfaserverstärkter Kunststoff |
| GRP | Glass Reinforced Plastic |
| GTAW | Gas Tungsten Arc Welding (= WIG/TIG) |
| GMAW | Gas Metal Arc Welding (= MIG/MAG) |
| HF | Hochfrequenz (Schweißverfahren für Kunststoff) |
| ID | Innendurchmesser |
| ISO | International Organization for Standardization |
| KBE | Kolonie-bildende Einheiten (Mikrobiologie) |
| MAK | Maximale Arbeitsplatzkonzentration |
| NMMA | National Marine Manufacturers Association (USA) |
| NPT | National Pipe Thread (US-Gewindeform) |
| OD | Außendurchmesser |
| PE-HD | Polyethylen hoher Dichte |
| PE-LD | Polyethylen niederer Dichte |
| PE-XLPE | Vernetztes Polyethylen |
| PREN | Pitting Resistance Equivalent Number |
| PTFE | Polytetrafluorethylen (Teflon) |
| PU | Polyurethan |
| PVC | Polyvinylchlorid |
| RINA | Registro Italiano Navale |
| SAE | Society of Automotive Engineers |
| SHE | Standard-Wasserstoffelektrode |
| SMAW | Shielded Metal Arc Welding (= E-Hand) |
| TIG | Tungsten Inert Gas (= WIG) |
| UEG | Untere Explosionsgrenze |
| ULSD | Ultra Low Sulfur Diesel |
| UN | United Nations (Gefahrgut-Zulassung) |
| USCG | United States Coast Guard |
| VDO | Vereinigte DEUTA-OTA (Instrumentenhersteller) |
| WEZ | Wärmeeinflusszone |
| WHG | Wasserhaushaltsgesetz (Deutschland) |
| WIG | Wolfram-Inertgas-Schweißen |
| XLPE | Cross-linked Polyethylene (vernetztes PE) |

---

## 10. Schnell-Referenz

### 10.1 Tankgrößen nach Bootsklasse

| Bootsklasse | Typische Tankg. (Diesel) | Typische Tankg. (Benzin) | Material (empfohlen) |
|------------|-------------------------|-------------------------|---------------------|
| Kleinboot 5–7m | 40–80 l | 60–120 l | PE-HD |
| Segelyacht 8–10m | 60–120 l | n/a | PE-HD oder Edelstahl |
| Segelyacht 10–14m | 120–300 l | n/a | Edelstahl 316L |
| Segelyacht 14–18m | 300–600 l | n/a | Edelstahl 316L |
| Motorboot 7–10m | 150–300 l | 200–400 l | PE-HD oder Edelstahl |
| Motorboot 10–14m | 300–800 l | 400–1.000 l | Edelstahl oder Aluminium |
| Motoryacht 14–20m | 800–3.000 l | n/a | Edelstahl 316L |
| Motoryacht 20–30m | 3.000–10.000 l | n/a | Edelstahl 316L |
| Superyacht >30m | 10.000–50.000 l | n/a | Edelstahl 316L |

### 10.2 Wandstärken-Schnellreferenz

| Material | Tankvolumen ≤100l | 100–300l | 300–600l | 600–1.200l | >1.200l |
|----------|-------------------|----------|----------|-----------|---------|
| Edelstahl 316L | 1,5 mm | 2,0 mm | 2,5 mm | 3,0 mm | 3,0–5,0 mm |
| Aluminium 5083 | 2,5 mm | 3,0 mm | 4,0 mm | 5,0 mm | 6,0–8,0 mm |
| PE-HD | 5 mm | 6–7 mm | 7–8 mm | 8–10 mm | 10–12 mm |
| GFK (Vinylester) | 4 mm | 5 mm | 5–6 mm | 6–8 mm | 8–10 mm |

### 10.3 Normen-Schnellreferenz

| Norm | Scope | Region | Tanktyp |
|------|-------|--------|---------|
| ISO 21487:2012 | Kunststoff-Kraftstofftanks | International/EU | PE, GFK |
| ISO 10088:2013 | Kraftstoffsysteme gesamt | International/EU | Alle |
| ISO 21487:2012 | Metallische Kraftstofftanks | International/EU | Edelstahl, Aluminium |
| ABYC H-24 | Benzin-Kraftstoffsysteme | USA | Alle |
| ABYC H-33 | Diesel-Kraftstoffsysteme | USA | Alle |
| 33 CFR 183 | USCG Fuel Systems | USA | Alle |
| CE 2013/53/EU | Sportbootrichtlinie | EU | Alle |

### 10.4 Anschlussgröße-Schnellreferenz

| Funktion | Min. Größe | Empfohlen | Standard |
|----------|-----------|-----------|---------|
| Füllstutzen | 38mm (1½") | 50mm (2") | BSP oder NPT |
| Entlüftung | 16mm (⅝") | 19mm (¾") | Tülle oder BSP |
| Kraftstoffentnahme | 8mm (⅜") | 10mm (⅜") | BSP oder Tülle |
| Rücklauf | 8mm (⅜") | 10mm (⅜") | BSP oder Tülle |
| Ablassventil | ¼" BSP | ⅜" BSP | BSP mit Kugelhahn |
| Tankgeber | 5-Loch-Flansch | 54mm BK (VDO) | SAE oder metrisch |

### 10.5 Kraftstoff-Kennwerte

| Eigenschaft | Diesel (EN 590) | Benzin (EN 228) | Einheit |
|------------|----------------|----------------|---------|
| Dichte (15°C) | 0,820–0,845 | 0,720–0,775 | kg/l |
| Flammpunkt | >55 | ca. -20 | °C |
| Heizwert | 42,5 | 43,5 | MJ/kg |
| Heizwert volumetrisch | 35,5 | 32,5 | MJ/l |
| Viskosität (40°C) | 2,0–4,5 | 0,4–0,8 | mm²/s |
| Cetanzahl/Oktanzahl | 51 (Cetan) | 95 (Oktan) | – |
| FAME-Gehalt (max.) | 7% (B7) | 0% | Vol.-% |
| Ethanol-Gehalt (max.) | 0% | 10% (E10) | Vol.-% |
| Wassergehalt (max. Norm) | 200 ppm | 0,05% | – |
| Schwefelgehalt (max.) | 10 ppm | 10 ppm | mg/kg |
| Wärmeausdehnung | 0,00083/°C | 0,00095/°C | 1/K |

---

## 11. ANHANG A–H: Fallstudien

### ANHANG A — Fallstudie: Lochfraß-Versagen eines Aluminium-Dieseltanks auf einer Bavaria 40 Cruiser

**Boot:** Bavaria 40 Cruiser, Baujahr 2008, 12,35m LüA
**Tanktyp:** Aluminium 5083, 200l, werksseitig eingebaut
**Alter bei Versagen:** 14 Jahre (2022)
**Einsatzgebiet:** Mittelmeer (Kroatien), ganzjährig im Wasser

**Problemschilderung:**
Der Eigner bemerkte nach dem Winterlager einen starken Dieselgeruch in der Achterkabine. Die Bilge unter dem Tank zeigte einen Ölfilm. Die Tankanzeige stand auf "¾ voll", obwohl der Tank im Herbst vollgetankt worden war.

**Diagnose:**
1. Äußere Inspektion: Weiße Korrosionsprodukte an der Tankunterseite, besonders im Bereich der Edelstahl-Halterungsbänder
2. Ultraschallmessung: Originalwandstärke 3mm, gemessene Wandstärke im korrodierten Bereich 0,8–1,5mm, an drei Stellen Durchbrüche (<0,3mm)
3. Ursache: Direkte Kontaktkorrosion zwischen Edelstahl-Halterung und Aluminiumtank — keine Isolationspads vorhanden (Werftfehler). Bilgenwasser als Elektrolyt.
4. Potentialmessung: 650 mV zwischen Tank und Halterung (extrem hoch, >50 mV = problematisch)

**Lösung:**
1. Tank vollständig abgelassen (inkl. 4 Liter Wasser am Tankboden!)
2. Reparatur nicht wirtschaftlich (großflächiges Pitting)
3. Neuer Edelstahl 316L-Tank in identischen Abmessungen gefertigt (Ronco RC-SS-200)
4. Installation mit EPDM-Isolationspads (5mm) zwischen Tank und Halterung
5. Opferanode (Zink) am Tank installiert (zusätzliche Sicherheit)

**Kosten:**
- Neuer Tank (316L, 200l, maßgefertigt): 1.850 EUR
- Isolationspads und Opferanode: 120 EUR
- Demontage alter Tank + Installation neuer Tank (12 Std.): 1.440 EUR
- Bilgenreinigung und Geruchssanierung: 450 EUR
- **Gesamt: 3.860 EUR**

**Lehren:**
- Galvanische Isolation ist KEINE Option, sondern PFLICHT bei Aluminiumtanks
- Regelmäßige Inspektion (jährlich) hätte das Problem im Stadium 1 erkannt
- Edelstahl 316L als Ersatz eliminiert das galvanische Problem dauerhaft

### ANHANG B — Fallstudie: Diesel-Bug-Befall auf einer Hallberg-Rassy 43 Mk II

**Boot:** Hallberg-Rassy 43 Mk II, Baujahr 2015, 13,20m LüA
**Tanktyp:** Edelstahl 316L, 480l, werksseitig
**Alter bei Problem:** 7 Jahre (2022)
**Einsatzgebiet:** Ostsee, Saisonbetrieb Mai–Oktober

**Problemschilderung:**
Während einer Sommerfahrt (Woche 3) begann der Volvo Penta D2-55 nach 30 Minuten Betrieb zu stottern. Der Vorfilter (Racor 500FG) war nach nur 15 Motorstunden verstopft (normal: 500+ Stunden). Schwarze, schleimige Partikel im Filter.

**Diagnose:**
1. Kraftstoffprobe am Tankablassventil: 300 ml Wasser (trüb, übelriechend), darüber schwarze Flocken
2. Fuelstat-Testkit: Stark positiv für Hormoconis resinae (Diesel-Pilz)
3. Inspektion über Tankgeber-Öffnung (Endoskop): Biofilm an Tankwänden, Schwallblechen und Tankanschlüssen
4. Ursache: Boot stand November–April mit halbvollem Tank (nicht vollgetankt vor Winterlager). Kondensat sammelte sich am Boden → idealer Nährboden für Diesel-Bug. Der B7-Diesel (7% FAME) begünstigte das Wachstum zusätzlich.

**Lösung:**
1. Gesamten Tankinhalt (ca. 350l) in Fässer abgepumpt (Entsorgung als Sondermüll: 280 EUR)
2. Tank über Inspektionsöffnung mechanisch gereinigt (Hochdruckreiniger 60°C)
3. Grotamar 82 (50ml) als Schock-Dosis eingebracht, 24h einwirken lassen
4. Tank mit frischem Diesel befüllt, 12h über Polishing-System (gemietet) umgewälzt
5. Alle Filter getauscht (Racor-Element, Motor-Feinfilter, Wechselfiltergehäuse)
6. Prophylaxe: Grotamar 82 bei jeder Betankung (5ml/100l)
7. Einwinterung ab sofort: Tank VOLL tanken

**Kosten:**
- Kraftstoff-Entsorgung: 280 EUR
- Tankreinigung (Arbeit, 6 Std.): 720 EUR
- Grotamar 82 (500ml Flasche): 45 EUR
- Polishing-System Miete (3 Tage): 180 EUR
- Neue Filter (Racor + Motor): 95 EUR
- Neuer Kraftstoff (480l Diesel): 830 EUR
- **Gesamt: 2.150 EUR**

**Lehren:**
- Tank IMMER voll einwintern — dies hätte den gesamten Schaden verhindert
- B7-Diesel erhöht das Diesel-Bug-Risiko — prophylaktisches Biozid ist Standard
- Regelmäßiges Entwässern am Ablassventil (monatlich in der Saison)

### ANHANG C — Fallstudie: Blockierte Tankentlüftung verursacht Motorausfall auf See

**Boot:** Jeanneau Sun Odyssey 440, Baujahr 2019, 13,33m LüA
**Tanktyp:** GFK-Integrationstank, 200l Diesel
**Alter bei Problem:** 3 Jahre (2022)
**Einsatzgebiet:** Ärmelkanal, Überführungsfahrt

**Problemschilderung:**
Während einer Kanalüberquerung (Beaufort 5–6, 2m Welle) starb der Yanmar 4JH57 nach 4 Stunden Betrieb ab. Neustart: Motor lief 10 Sekunden, stotterte, starb ab. Tank zeigte ½ voll.

**Diagnose:**
1. Tankdeckel geöffnet: Lautes Zischen (Unterdruck im Tank)
2. Motor lief nach Öffnen des Deckels sofort wieder
3. Entlüftungsleitung verfolgt: Am P/V-Ventil (Vetus TANKVENT) kein Durchgang
4. P/V-Ventil ausgebaut: Membrane der Unterdruckseite verklebt (geschwollenes Gummi durch Diesel-Dampf-Exposition)
5. Zusätzlich: Entlüftungsöffnung außenbords zu 50% durch Spinnennetz/Salzkristalle blockiert

**Lösung (auf See):**
1. Tankdeckel leicht geöffnet gelassen (Notlösung — NICHT empfehlenswert bei Benzin!)
2. Motor lief damit stabil bis zum Zielhafen

**Lösung (im Hafen):**
1. P/V-Ventil durch neues Vetus TANKVENT ersetzt: 48 EUR
2. Entlüftungsöffnung gereinigt, Insektenschutzgitter installiert: 15 EUR
3. Entlüftungsleitung mit Druckluft durchgeblasen: kostenlos
4. Funktionsprüfung: Tank verschlossen, Motor 2h laufen lassen → kein Druckabfall, Motor läuft stabil

**Kosten:**
- P/V-Ventil: 48 EUR
- Insektenschutzgitter: 15 EUR
- Arbeit (1,5 Std.): 180 EUR
- **Gesamt: 243 EUR**

**Lehren:**
- Tankentlüftung ist ein SICHERHEITSKRITISCHES System — jährliche Funktionsprüfung!
- P/V-Ventile haben eine begrenzte Lebensdauer (Membranen altern)
- Insektenschutzgitter an der Außenöffnung = 15 EUR Prävention vs. potenzieller Motorausfall auf See

### ANHANG D — Fallstudie: GFK-Permeation eines Integrationstanks auf einer Beneteau Oceanis 46.1

**Boot:** Beneteau Oceanis 46.1, Baujahr 2018, 14,60m LüA
**Tanktyp:** GFK-Integrationstank im Rumpf, 200l Diesel
**Alter bei Problem:** 5 Jahre (2023)
**Einsatzgebiet:** Mittelmeer (Balearen)

**Problemschilderung:**
Chronischer Dieselgeruch in der Eignerkabine (über dem vorderen Tank). Keine sichtbare Leckage, keine Tropfen, keine Verfärbung. Geruch persistiert trotz Reinigung aller Oberflächen.

**Diagnose:**
1. Alle Anschlüsse, Leitungen und Filter geprüft: dicht
2. Tankinneninspektion: Laminat-Innenseite leicht klebrig, Gelcoat verfärbt (bräunlich)
3. Laboranalyse des Laminats: Harz identifiziert als Orthophthal-Polyester (NICHT Vinylester)
4. Diesel (B7 mit 7% FAME) hat das Polyesterharz über 5 Jahre angegriffen und permeiert durch die Tankwand in den Kabinenbereich

**Lösung:**
1. Variante A (gewählt): Flexiblen ATL FluoroCell Bladder-Tank (200l, FA-200) in den vorhandenen Integrationstank eingesetzt (Tank-im-Tank-Lösung)
2. Variante B (verworfen): Integrationstank mit Vinylester-Barriereschicht nachlaminieren — verworfen, da Zugang zu eng und Haftung auf kontaminiertem Polyester fraglich
3. Variante C (verworfen): Separaten Edelstahltank an anderer Stelle einbauen — verworfen, da kein Platz

**Kosten:**
- ATL FA-200 Bladder: 780 EUR
- Anpassung der Anschlüsse (neue Tüllen, Schläuche): 150 EUR
- Arbeit (8 Std. inkl. Demontage Kabinenmöbel): 960 EUR
- **Gesamt: 1.890 EUR**

**Lehren:**
- Integrationstanks mit Orthophthal-Polyester und B7-Diesel sind eine Zeitbombe
- Werften sparen an der falschen Stelle — Vinylester als Tankharz kostet nur ~3 EUR/kg mehr
- Bladder-Tank als Nachrüstung ist eine elegante und kostengünstige Lösung

### ANHANG E — Fallstudie: Elektrolyse-Korrosion an einem Edelstahltank durch Streustrom

**Boot:** Princess V52, Baujahr 2010, 16,16m LüA
**Tanktyp:** 2× Edelstahl 316L, je 1.000l Diesel
**Alter bei Problem:** 12 Jahre (2022)
**Einsatzgebiet:** Solent (UK), Marina-Liegeplatz ganzjährig

**Problemschilderung:**
Bei der 10-Jahres-Inspektion (2 Jahre überfällig): Lochfraß an der Unterseite des Steuerbordtanks, Wandstärke lokal von 3mm auf 1,2mm reduziert. Backbordtank: keine Korrosion.

**Diagnose:**
1. Streustrom-Messung: Steuerbord-Landstrom-Kabel verlief direkt über dem Tank, mangelhaft isoliert
2. Potentialmessung: Steuerbordtank zeigte -300 mV vs. Ag/AgCl-Referenzelektrode (normal: +50 bis +150 mV für passiven 316L) — Tank wurde anodisch korrodiert
3. Ursache: Streustrom aus dem Landstromsystem floss über den Tankkörper zur Masse → galvanische Korrosion

**Lösung:**
1. Landstrom-Kabel ordnungsgemäß verlegt (Abstand min. 200mm zum Tank, geschirmt)
2. Galvanischer Isolator (ProSafe 30A) in die Lanstrom-Masseleitung eingebaut
3. Steuerbordtank: betroffene Fläche (ca. 200×300mm) mit 316L-Blech WIG-aufgeschweißt, gebeizt
4. Jährliche Streustrom-Messung in den Wartungsplan aufgenommen

**Kosten:**
- Landstrom-Kabel neu verlegen: 650 GBP
- Galvanischer Isolator ProSafe 30A: 280 GBP
- Tank-Reparatur (Schweißarbeiten, Beizen): 1.400 GBP
- Inspektion und Messungen: 350 GBP
- **Gesamt: 2.680 GBP**

**Lehren:**
- Streuströme sind ein unsichtbarer Killer für metallische Tanks
- Galvanischer Isolator in der Landstrom-Versorgung ist PFLICHT bei Metalltanks
- Jährliche Potentialmessung ist die einzige Methode, Streustrom-Korrosion frühzeitig zu erkennen

### ANHANG F — Fallstudie: PE-Tank-Rissbildung durch UV-Degradation auf einem Motorboot

**Boot:** Quicksilver Activ 755 Weekend, Baujahr 2014, 7,55m LüA
**Tanktyp:** PE-HD Standardtank, 220l Benzin (fluoriert), im offenen Cockpit-Locker
**Alter bei Problem:** 9 Jahre (2023)
**Einsatzgebiet:** Bodensee, Trailerbetrieb

**Problemschilderung:**
Benzingeruch nach jedem Tanken. Visuell: Haarfeine Risse an der Tankoberseite, besonders im Bereich des Einfüllstutzens. PE-Oberfläche fühlt sich kreidig an.

**Diagnose:**
1. Tank aus naturweißem PE-HD (NICHT carbon-black-stabilisiert)
2. Locker-Deckel wurde im Sommer häufig offen gelassen → direkte UV-Exposition
3. UV-Degradation nach 9 Jahren Freiluft-Exposition → PE-Kettenbruch → Versprödung → Rissbildung
4. Risse durchdringen die Fluorierungsschicht → Benzin permeiert

**Lösung:**
1. Tank sofort stillgelegt (Benzin-Sicherheit!)
2. Ersatz durch schwarzen (carbon-black-stabilisierten), fluoriertes PE-HD-Tank gleicher Dimension (Moeller FT5504G)
3. UV-Schutzhaube für den Locker beschafft

**Kosten:**
- Neuer Tank Moeller FT5504G (55 gal, fluoriert): 385 USD
- Versand USA→DE + Zoll: 220 EUR
- Demontage/Montage (4 Std.): 480 EUR
- UV-Schutzhaube: 45 EUR
- **Gesamt: ca. 1.100 EUR**

**Lehren:**
- PE-HD-Tanks MÜSSEN carbon-black-stabilisiert sein, wenn UV-Exposition möglich
- Naturweißes PE im Außenbereich = Zeitbombe
- Inspektion auf kreidiges Erscheinungsbild = UV-Frühwarnung

### ANHANG G — Fallstudie: Falsche Tankgeber-Impedanz verursacht chronische Fehlanzeige

**Boot:** Dehler 38, Baujahr 2017, 11,50m LüA
**Tanktyp:** Edelstahl 316L, 160l Diesel
**Problemstart:** Direkt nach Eignerwechsel (2021)

**Problemschilderung:**
Der neue Eigner bemerkte, dass die Tankanzeige (VDO ViewLine) bei vollem Tank nur ¾ und bei leerem Tank noch ¼ anzeigte. Die Anzeige war nie korrekt.

**Diagnose:**
1. Geber ausgebaut: Wema S3 Schwimmgeber, 250mm Länge, 0–190 Ω
2. Anzeige: VDO ViewLine — erwartet 10–180 Ω
3. Impedanz-Mismatch: Geber liefert 0–190 Ω, Anzeige erwartet 10–180 Ω → Skalenendwerte stimmen nicht überein
4. Voreigner hatte den Geber selbst gewechselt und den falschen Widerstandsbereich bestellt

**Lösung:**
1. Option A: Geber tauschen gegen VDO-kompatiblen Geber (10–180 Ω) → gewählt
2. Option B: Anzeige gegen Wema-kompatible Anzeige tauschen
3. Option C: Programmierbaren Universal-Geber verwenden (z.B. Wema SSI mit einstellbarem Widerstandsbereich)

**Kosten:**
- Neuer VDO Tankgeber (10–180 Ω, Hebellänge 250mm): 68 EUR
- Einbau (30 min): 35 EUR
- **Gesamt: 103 EUR**

**Lehren:**
- Vor dem Geberkauf IMMER den Widerstandsbereich der Anzeige prüfen (10–180 Ω Europa-VDO vs. 33–240 Ω US-Standard vs. 0–190 Ω Wema)
- Hebellänge muss zur Tankhöhe passen (Hebellänge ≈ Tankhöhe - 30mm)

### ANHANG H — Fallstudie: Schwallblech-Versagen verursacht Trimm-Instabilität auf einer Nordhavn 47

**Boot:** Nordhavn 47, Baujahr 2005, 14,63m LüA
**Tanktyp:** 2× Aluminium 5083, je 1.500l Diesel (Satteltanks)
**Alter bei Problem:** 17 Jahre (2022)
**Einsatzgebiet:** Transatlantik-Passage (ARC Rally)

**Problemschilderung:**
Während der Atlantiküberquerung (Woche 2, halbe Tankfüllung, schwere Dünung von querab) begann das Boot plötzlich stärker zu rollen als in der Vorwoche bei ähnlichen Bedingungen. Klopf- und Schlaggeräusche aus dem Steuerbord-Tank. Rollperiode verkürzte sich merkbar.

**Diagnose (in Las Palmas nach Ankunft):**
1. Inspektionsöffnung Steuerbordtank geöffnet: Mittleres Schwallblech (von 3) hat sich an der Schweißnaht gelöst
2. Schweißnaht zeigt Ermüdungsbruch (Schwingungsrisse)
3. Ursache: 17 Jahre zyklische Belastung, Schwallblech mit nur 6 Schweißpunkten befestigt (statt umlaufender Naht)
4. Freier Oberflächeneffekt ohne Schwallblech drastisch erhöht → verstärktes Rollen

**Lösung:**
1. Tank abgelassen, gereinigt
2. Schwallblech neu eingeschweißt: umlaufende WIG-Naht (AlMg5), dickeres Blech (4mm statt 3mm)
3. Zwei zusätzliche Versteifungsrippen am Schwallblech angeschweißt
4. Alle Schwallbleche in beiden Tanks inspiziert — Backbordtank OK, aber gleiche Bauweise → prophylaktisch nachgeschweißt

**Kosten:**
- Schweißarbeiten (16 Std. Aluminium-Fachbetrieb Las Palmas): 2.400 EUR
- Material (Alu-Blech, Draht): 180 EUR
- Tankreinigung und Kraftstoff-Transfer: 350 EUR
- Neuer Kraftstoff (3.000l): 3.900 EUR
- **Gesamt: 6.830 EUR**

**Lehren:**
- Schwallbleche MÜSSEN umlaufend verschweißt sein, nicht nur punktweise
- Bei Langfahrtyachten mit großen Tanks ist die Schwallblech-Inspektion alle 10 Jahre essenziell
- Der freie Oberflächeneffekt bei 1.500l Tank bei halber Füllung ist erheblich — Schwallbleche sind sicherheitsrelevant

---

## 12. ANHANG I–R: Pydantic v2 Modelle

### ANHANG I — Basismodelle

```python
"""
AYDI Knowledge Models — Fuel Tanks (19.01)
Pydantic v2 models for fuel tank analysis and diagnostics.
All models use model_config = {"from_attributes": True} — NEVER class Config.
"""

from __future__ import annotations

from datetime import date
from enum import Enum
from typing import Optional

from pydantic import BaseModel, Field, field_validator


class TankMaterial(str, Enum):
    """Fuel tank construction material."""
    STAINLESS_316L = "stainless_316l"
    ALUMINUM_5083 = "aluminum_5083"
    ALUMINUM_5086 = "aluminum_5086"
    GFK_VINYLESTER = "gfk_vinylester"
    GFK_EPOXY = "gfk_epoxy"
    GFK_POLYESTER = "gfk_polyester"
    PE_HD = "pe_hd"
    PE_HD_FLUORINATED = "pe_hd_fluorinated"
    PE_HD_SULFONATED = "pe_hd_sulfonated"
    BLADDER_PU_NYLON = "bladder_pu_nylon"
    BLADDER_CSM = "bladder_csm"
    BLADDER_XLPE = "bladder_xlpe"
    MILD_STEEL_GALVANIZED = "mild_steel_galvanized"


class FuelType(str, Enum):
    """Supported fuel types."""
    DIESEL_EN590 = "diesel_en590"
    DIESEL_B20 = "diesel_b20"
    GASOLINE_EN228 = "gasoline_en228"
    GASOLINE_E10 = "gasoline_e10"
    GASOLINE_E15 = "gasoline_e15"


class TankShape(str, Enum):
    """Physical tank shape classification."""
    RECTANGULAR = "rectangular"
    L_SHAPED = "l_shaped"
    WEDGE = "wedge"
    SADDLE = "saddle"
    INTEGRATED = "integrated"
    CUSTOM = "custom"


class TankPosition(str, Enum):
    """Tank installation position in the vessel."""
    MIDSHIP_LOW = "midship_low"
    AFT_UNDER_FLOOR = "aft_under_floor"
    SADDLE_BOTH_SIDES = "saddle_both_sides"
    FORWARD = "forward"
    UNDER_CABIN_FLOOR = "under_cabin_floor"
    COCKPIT_LOCKER = "cockpit_locker"
    ENGINE_ROOM = "engine_room"


class ConfidenceLevel(str, Enum):
    """AYDI confidence level for assessment results."""
    MEASURED = "measured"
    CALCULATED = "calculated"
    VISUAL_HIGH = "visual_high"
    VISUAL_MEDIUM = "visual_medium"
    VISUAL_LOW = "visual_low"
    VISUAL_INSUFFICIENT = "visual_insufficient"
    ESTIMATED = "estimated"
    BENCHMARK = "benchmark"
    DOCUMENTED = "documented"


class Severity(str, Enum):
    """Fault severity classification."""
    CRITICAL = "critical"
    HIGH = "high"
    MEDIUM = "medium"
    LOW = "low"
    INFO = "info"
```

### ANHANG J — Tank-Spezifikationsmodelle

```python
class TankDimensions(BaseModel):
    """Physical dimensions of a fuel tank in millimeters."""

    model_config = {"from_attributes": True}

    length_mm: float = Field(..., gt=0, description="Tank length in mm")
    width_mm: float = Field(..., gt=0, description="Tank width in mm")
    height_mm: float = Field(..., gt=0, description="Tank height in mm")
    wall_thickness_mm: float = Field(..., gt=0, le=15, description="Wall thickness in mm")
    bottom_thickness_mm: Optional[float] = Field(
        None, gt=0, le=20, description="Bottom plate thickness in mm (if different from wall)"
    )

    @property
    def volume_liters(self) -> float:
        """Calculate gross volume in liters (rectangular approximation)."""
        internal_l = self.length_mm - 2 * self.wall_thickness_mm
        internal_w = self.width_mm - 2 * self.wall_thickness_mm
        internal_h = self.height_mm - self.wall_thickness_mm - (
            self.bottom_thickness_mm or self.wall_thickness_mm
        )
        return (internal_l * internal_w * internal_h) / 1_000_000


class BaffleSpec(BaseModel):
    """Specification for internal baffles (Schwallbleche)."""

    model_config = {"from_attributes": True}

    count: int = Field(..., ge=0, description="Number of baffles")
    thickness_mm: float = Field(default=2.0, gt=0, description="Baffle thickness in mm")
    open_area_percent: float = Field(
        default=50.0, ge=20, le=80,
        description="Percentage of baffle area that is open (holes/cutouts)"
    )
    orientation: str = Field(
        default="transverse",
        description="Baffle orientation: 'transverse' or 'longitudinal'"
    )


class TankSpecification(BaseModel):
    """Complete fuel tank specification."""

    model_config = {"from_attributes": True}

    tank_id: str = Field(..., description="Unique tank identifier")
    manufacturer: Optional[str] = Field(None, description="Tank manufacturer name")
    model_number: Optional[str] = Field(None, description="Manufacturer model number")
    material: TankMaterial
    fuel_type: FuelType
    shape: TankShape
    position: TankPosition
    dimensions: TankDimensions
    nominal_volume_liters: float = Field(..., gt=0, le=50_000, description="Nominal volume in liters")
    usable_volume_liters: Optional[float] = Field(
        None, gt=0, description="Usable volume (accounting for pickup height)"
    )
    baffles: Optional[BaffleSpec] = None
    has_inspection_port: bool = Field(default=False)
    inspection_port_diameter_mm: Optional[float] = Field(None, gt=0)
    has_drain_valve: bool = Field(default=False)
    has_level_sender: bool = Field(default=True)
    year_installed: Optional[int] = Field(None, ge=1950, le=2030)
    certification: list[str] = Field(
        default_factory=list,
        description="Certifications: ISO_21487, ISO_10088, ABYC_H24, ABYC_H33, CE, USCG"
    )
    weight_empty_kg: Optional[float] = Field(None, gt=0, description="Empty tank weight in kg")
    price_eur: Optional[float] = Field(None, ge=0, description="Approximate price in EUR")

    @field_validator("usable_volume_liters")
    @classmethod
    def usable_not_greater_than_nominal(cls, v: Optional[float], info) -> Optional[float]:
        if v is not None and "nominal_volume_liters" in info.data:
            if v > info.data["nominal_volume_liters"]:
                raise ValueError("Usable volume cannot exceed nominal volume")
        return v
```

### ANHANG K — Tankgeber-Modelle

```python
class SenderType(str, Enum):
    """Tank level sender technology."""
    FLOAT_RESISTIVE = "float_resistive"
    CAPACITIVE = "capacitive"
    ULTRASONIC = "ultrasonic"
    PRESSURE = "pressure"
    SIGHT_GLASS = "sight_glass"


class SenderImpedanceRange(BaseModel):
    """Impedance range specification for resistive senders."""

    model_config = {"from_attributes": True}

    empty_ohms: float = Field(..., ge=0, description="Resistance at empty level")
    full_ohms: float = Field(..., ge=0, description="Resistance at full level")
    standard: str = Field(
        default="vdo_europe",
        description="Standard: vdo_europe (10-180), us_standard (33-240), wema (0-190)"
    )


class TankLevelSender(BaseModel):
    """Tank level sender specification."""

    model_config = {"from_attributes": True}

    sender_type: SenderType
    manufacturer: str = Field(..., description="Sender manufacturer")
    model: str = Field(..., description="Sender model number")
    arm_length_mm: float = Field(..., gt=0, description="Sender arm/probe length in mm")
    impedance: Optional[SenderImpedanceRange] = Field(
        None, description="Impedance range (for resistive senders)"
    )
    mounting: str = Field(
        default="5_bolt_flange",
        description="Mounting type: 5_bolt_flange, threaded, clip"
    )
    bolt_circle_mm: Optional[float] = Field(
        None, description="Bolt circle diameter in mm (for flange mount)"
    )
    compatible_displays: list[str] = Field(
        default_factory=list,
        description="Compatible display brands/models"
    )
    price_eur: Optional[float] = Field(None, ge=0)
```

### ANHANG L — Belüftungsmodelle

```python
class VentType(str, Enum):
    """Tank ventilation system type."""
    SIMPLE_VENT = "simple_vent"
    PV_VALVE = "pv_valve"
    FLAME_ARRESTER = "flame_arrester"
    PV_WITH_FLAME_ARRESTER = "pv_with_flame_arrester"


class TankVentilation(BaseModel):
    """Tank ventilation system specification."""

    model_config = {"from_attributes": True}

    vent_type: VentType
    vent_line_id_mm: float = Field(..., gt=0, description="Vent line inner diameter in mm")
    has_anti_siphon_loop: bool = Field(default=True)
    anti_siphon_height_above_wl_mm: Optional[float] = Field(
        None, gt=0, description="Anti-siphon loop height above waterline in mm"
    )
    outlet_location: str = Field(
        default="hull_side",
        description="Outlet location: hull_side, transom, deck"
    )
    has_insect_screen: bool = Field(default=False)
    pv_opening_pressure_bar: Optional[float] = Field(
        None, gt=0, le=0.5, description="P/V valve opening pressure (overpressure) in bar"
    )
    pv_vacuum_pressure_bar: Optional[float] = Field(
        None, gt=-0.5, lt=0, description="P/V valve opening pressure (vacuum) in bar"
    )
    flame_arrester_mesh_per_cm: Optional[int] = Field(
        None, ge=20, description="Flame arrester mesh density (meshes per cm)"
    )
```

### ANHANG M — Fehlerbildmodelle

```python
class FaultCategory(str, Enum):
    """Fault category classification."""
    CORROSION = "corrosion"
    MICROBIAL = "microbial"
    MECHANICAL = "mechanical"
    ELECTRICAL = "electrical"
    PERMEATION = "permeation"
    VENTILATION = "ventilation"
    CONTAMINATION = "contamination"
    INSTALLATION = "installation"


class FaultDiagnosis(BaseModel):
    """Diagnosis result for a fuel tank fault."""

    model_config = {"from_attributes": True}

    fault_id: str = Field(..., description="Fault pattern ID (e.g., F01-ALPITTING)")
    fault_category: FaultCategory
    severity: Severity
    affected_material: Optional[TankMaterial] = None
    affected_fuel_type: Optional[FuelType] = None
    symptoms: list[str] = Field(..., min_length=1, description="Observed symptoms")
    probable_causes: list[str] = Field(..., min_length=1, description="Probable causes")
    confidence: ConfidenceLevel
    recommended_actions: list[str] = Field(
        ..., min_length=1, description="Recommended repair/mitigation actions"
    )
    estimated_repair_cost_eur: Optional[tuple[float, float]] = Field(
        None, description="Estimated cost range (min, max) in EUR"
    )
    urgency_days: Optional[int] = Field(
        None, ge=0,
        description="Recommended max days before action (0 = immediate)"
    )


class TankInspectionResult(BaseModel):
    """Result of a fuel tank inspection."""

    model_config = {"from_attributes": True}

    inspection_id: str = Field(..., description="Unique inspection identifier")
    tank_id: str = Field(..., description="Inspected tank identifier")
    inspection_date: date
    inspector: Optional[str] = None
    inspection_method: str = Field(
        ..., description="Method: visual, ultrasonic, endoscope, pressure_test, sample_analysis"
    )
    wall_thickness_measurements_mm: Optional[list[float]] = Field(
        None, description="Wall thickness measurements at various points in mm"
    )
    min_wall_thickness_mm: Optional[float] = Field(None, gt=0)
    original_wall_thickness_mm: Optional[float] = Field(None, gt=0)
    wall_thickness_loss_percent: Optional[float] = Field(None, ge=0, le=100)
    water_found_ml: Optional[float] = Field(None, ge=0)
    sediment_found: bool = Field(default=False)
    microbial_test_result: Optional[str] = Field(
        None, description="Microbial test result: negative, low, moderate, high, severe"
    )
    corrosion_areas: list[str] = Field(
        default_factory=list, description="Description of corrosion areas found"
    )
    faults_found: list[FaultDiagnosis] = Field(default_factory=list)
    overall_condition: str = Field(
        ..., description="Overall condition: excellent, good, fair, poor, critical, replace"
    )
    next_inspection_date: Optional[date] = None
    confidence: ConfidenceLevel
    notes: Optional[str] = None
```

### ANHANG N — Hersteller-Datenbankmodelle

```python
class ManufacturerContact(BaseModel):
    """Manufacturer contact information."""

    model_config = {"from_attributes": True}

    company_name: str
    address: str
    country: str
    phone: Optional[str] = None
    email: Optional[str] = None
    website: Optional[str] = None
    founded_year: Optional[int] = Field(None, ge=1800, le=2030)


class TankProductLine(BaseModel):
    """A product line of fuel tanks from a manufacturer."""

    model_config = {"from_attributes": True}

    line_name: str = Field(..., description="Product line name (e.g., 'FTS' for Vetus stainless)")
    materials: list[TankMaterial]
    fuel_types: list[FuelType]
    volume_range_liters: tuple[float, float] = Field(
        ..., description="Volume range (min, max) in liters"
    )
    price_range_eur: Optional[tuple[float, float]] = Field(
        None, description="Price range (min, max) in EUR"
    )
    certifications: list[str] = Field(default_factory=list)
    custom_available: bool = Field(default=False)
    lead_time_weeks: Optional[tuple[int, int]] = Field(
        None, description="Lead time range (min, max) in weeks"
    )


class TankManufacturer(BaseModel):
    """Complete manufacturer database entry."""

    model_config = {"from_attributes": True}

    manufacturer_id: str = Field(..., description="Unique manufacturer identifier")
    contact: ManufacturerContact
    specialization: str
    product_lines: list[TankProductLine]
    warranty_years: Optional[int] = Field(None, ge=0)
    oem_supply: bool = Field(
        default=False, description="Supplies OEM to yacht builders"
    )
    distribution_regions: list[str] = Field(
        default_factory=list, description="Distribution regions (EU, US, UK, APAC, etc.)"
    )
```

### ANHANG O — Analyse-Ergebnismodelle

```python
class TankConditionScore(BaseModel):
    """Scored assessment of a fuel tank's condition."""

    model_config = {"from_attributes": True}

    tank_id: str
    overall_score: float = Field(..., ge=0, le=100, description="Overall condition 0-100")
    material_score: float = Field(..., ge=0, le=100, description="Material condition 0-100")
    installation_score: float = Field(..., ge=0, le=100, description="Installation quality 0-100")
    ventilation_score: float = Field(..., ge=0, le=100, description="Ventilation system 0-100")
    sender_score: float = Field(..., ge=0, le=100, description="Level sender accuracy 0-100")
    compliance_score: float = Field(..., ge=0, le=100, description="Norm compliance 0-100")
    remaining_life_years: Optional[float] = Field(
        None, ge=0, description="Estimated remaining useful life in years"
    )
    confidence: ConfidenceLevel
    findings: list[str] = Field(default_factory=list, description="Key findings (German)")
    recommendations: list[str] = Field(
        default_factory=list, description="Recommendations (German)"
    )


class TankSystemAnalysis(BaseModel):
    """Complete analysis result for the vessel's fuel tank system."""

    model_config = {"from_attributes": True}

    vessel_name: Optional[str] = None
    vessel_loa_m: Optional[float] = Field(None, gt=0)
    analysis_date: date
    analyst: Optional[str] = None
    tanks: list[TankSpecification]
    tank_scores: list[TankConditionScore]
    inspections: list[TankInspectionResult] = Field(default_factory=list)
    total_fuel_capacity_liters: float = Field(..., ge=0)
    total_usable_capacity_liters: Optional[float] = Field(None, ge=0)
    system_score: float = Field(
        ..., ge=0, le=100, description="Overall fuel system score 0-100"
    )
    critical_findings: list[str] = Field(
        default_factory=list,
        description="Critical findings requiring immediate action (German)"
    )
    norm_deviations: list[str] = Field(
        default_factory=list,
        description="Identified norm deviations with reference (German)"
    )
    estimated_replacement_cost_eur: Optional[float] = Field(None, ge=0)
    confidence: ConfidenceLevel
```

### ANHANG P — Kraftstoffqualitätsmodelle

```python
class FuelQualitySample(BaseModel):
    """Fuel quality sample analysis result."""

    model_config = {"from_attributes": True}

    sample_id: str
    sample_date: date
    tank_id: str
    fuel_type: FuelType
    water_content_ppm: Optional[float] = Field(None, ge=0, description="Water content in ppm")
    particulate_count_iso: Optional[str] = Field(
        None, description="ISO 4406 cleanliness code (e.g., '18/16/13')"
    )
    microbial_contamination: Optional[str] = Field(
        None, description="Level: none, low, moderate, high, severe"
    )
    acid_number_mg_koh_g: Optional[float] = Field(
        None, ge=0, description="Total acid number in mg KOH/g"
    )
    fame_content_percent: Optional[float] = Field(
        None, ge=0, le=100, description="FAME (biodiesel) content in %"
    )
    appearance: Optional[str] = Field(
        None, description="Visual: clear_bright, hazy, dark, contains_sediment"
    )
    density_kg_l: Optional[float] = Field(None, gt=0.6, lt=1.1)
    sulfur_content_ppm: Optional[float] = Field(None, ge=0)
    overall_quality: str = Field(
        ..., description="Quality: excellent, good, acceptable, poor, reject"
    )
    recommended_actions: list[str] = Field(default_factory=list)
    confidence: ConfidenceLevel
```

### ANHANG Q — Wartungsplanmodelle

```python
class MaintenanceInterval(str, Enum):
    """Standard maintenance intervals."""
    MONTHLY = "monthly"
    QUARTERLY = "quarterly"
    SEMI_ANNUAL = "semi_annual"
    ANNUAL = "annual"
    BIENNIAL = "biennial"
    FIVE_YEARLY = "five_yearly"
    TEN_YEARLY = "ten_yearly"
    AS_NEEDED = "as_needed"


class TankMaintenanceTask(BaseModel):
    """Individual maintenance task for a fuel tank system."""

    model_config = {"from_attributes": True}

    task_id: str
    task_name_de: str = Field(..., description="Task name in German")
    task_name_en: str = Field(..., description="Task name in English")
    description_de: str = Field(..., description="Task description in German")
    interval: MaintenanceInterval
    applicable_materials: list[TankMaterial] = Field(
        default_factory=list, description="Applicable tank materials (empty = all)"
    )
    applicable_fuel_types: list[FuelType] = Field(
        default_factory=list, description="Applicable fuel types (empty = all)"
    )
    estimated_duration_minutes: int = Field(..., gt=0)
    requires_professional: bool = Field(default=False)
    estimated_cost_eur: Optional[tuple[float, float]] = None
    tools_required: list[str] = Field(default_factory=list)
    safety_warnings: list[str] = Field(default_factory=list)


class TankMaintenancePlan(BaseModel):
    """Complete maintenance plan for a vessel's fuel tank system."""

    model_config = {"from_attributes": True}

    vessel_name: Optional[str] = None
    tank_ids: list[str]
    tasks: list[TankMaintenanceTask]
    created_date: date
    season_start_month: int = Field(default=4, ge=1, le=12)
    season_end_month: int = Field(default=10, ge=1, le=12)
    winterization_tasks: list[str] = Field(
        default_factory=list,
        description="Task IDs for winterization"
    )
    commissioning_tasks: list[str] = Field(
        default_factory=list,
        description="Task IDs for spring commissioning"
    )
```

### ANHANG R — Kosten- und Vergleichsmodelle

```python
class TankCostEstimate(BaseModel):
    """Cost estimation for tank replacement or installation."""

    model_config = {"from_attributes": True}

    tank_id: str
    scenario: str = Field(
        ..., description="Scenario: new_build, replacement_accessible, replacement_difficult, "
                        "replacement_integration_tank"
    )
    material_cost_eur: float = Field(..., ge=0)
    labor_hours: float = Field(..., ge=0)
    labor_rate_eur_per_hour: float = Field(default=120.0, gt=0)
    labor_cost_eur: float = Field(..., ge=0)
    additional_materials_eur: float = Field(default=0, ge=0, description="Fittings, hoses, etc.")
    disposal_cost_eur: float = Field(default=0, ge=0)
    fuel_transfer_cost_eur: float = Field(default=0, ge=0)
    total_cost_eur: float = Field(..., ge=0)
    confidence: ConfidenceLevel
    notes: Optional[str] = None

    @field_validator("total_cost_eur")
    @classmethod
    def validate_total(cls, v: float, info) -> float:
        """Verify total is plausible (not less than material cost alone)."""
        if "material_cost_eur" in info.data and v < info.data["material_cost_eur"]:
            raise ValueError("Total cost cannot be less than material cost alone")
        return v


class MaterialComparison(BaseModel):
    """Comparison of tank materials for a specific application."""

    model_config = {"from_attributes": True}

    comparison_id: str
    vessel_loa_m: float = Field(..., gt=0)
    required_volume_liters: float = Field(..., gt=0)
    fuel_type: FuelType
    position: TankPosition
    options: list[MaterialOption]
    recommended_material: TankMaterial
    recommendation_reason_de: str = Field(..., description="Recommendation reasoning in German")
    confidence: ConfidenceLevel


class MaterialOption(BaseModel):
    """Single material option in a comparison."""

    model_config = {"from_attributes": True}

    material: TankMaterial
    estimated_weight_kg: float = Field(..., ge=0)
    estimated_cost_eur: float = Field(..., ge=0)
    expected_lifetime_years: float = Field(..., gt=0)
    lifecycle_cost_20y_eur: float = Field(
        ..., ge=0, description="Total cost over 20 years (purchase + maintenance + replacement)"
    )
    pros_de: list[str] = Field(default_factory=list, description="Advantages in German")
    cons_de: list[str] = Field(default_factory=list, description="Disadvantages in German")
    score: float = Field(..., ge=0, le=100, description="Overall suitability score 0-100")
    compatible_with_fuel: bool = Field(default=True)
    norm_compliant: bool = Field(default=True)
```

---

## 13. Wartung und Instandhaltung — Detaillierter Wartungsplan

### 13.1 Wartungsplan nach Intervall

#### 13.1.1 Monatliche Wartung (Saisonbetrieb)

| Aufgabe | Zeitbedarf | Werkzeug | Anmerkung |
|---------|-----------|----------|----------|
| Sichtprüfung Tank und Umgebung auf Leckage | 5 min | Taschenlampe | Auf Feuchtigkeit, Ölfilm, Verfärbungen achten |
| Wasserabscheider kontrollieren und ggf. entwässern | 5 min | Auffangbehälter | Transparentes Filtergehäuse auf Wasserstand prüfen |
| Tankablassventil betätigen: 50ml Kraftstoff ablassen | 5 min | Behälter, Lappen | Auf Wasser und Sediment prüfen (klarer Diesel = OK) |
| Tankgeber-Anzeige auf Plausibilität prüfen | 2 min | — | Angezeigter Wert vs. geschätzter Verbrauch seit letztem Tanken |
| Bilge im Tankbereich auf Kraftstoffspuren prüfen | 3 min | Taschenlampe | Öliger Film, Dieselgeruch = sofortige Lecksuche |

#### 13.1.2 Vierteljährliche Wartung

| Aufgabe | Zeitbedarf | Werkzeug | Anmerkung |
|---------|-----------|----------|----------|
| Vorfilter-Element prüfen (Racor/Separ) | 10 min | Filterschlüssel | Verfärbung, Schlamm → Tausch. Normal: leicht gelblich |
| Entlüftungsöffnung außenbords auf Blockierung prüfen | 5 min | — | Insektennester, Salzkristalle, Spinnweben |
| Tankbefestigung auf Festigkeit prüfen | 5 min | Schraubenschlüssel | Spannbänder, Halterungen — Vibration lockert Verbindungen |
| Erdungsverbindung Tank → Motor prüfen (Sichtprüfung) | 3 min | — | Kabelschuh fest, keine Korrosion, keine gebrochenen Litzen |

#### 13.1.3 Halbjährliche Wartung (Saisonstart und -ende)

| Aufgabe | Zeitbedarf | Werkzeug | Anmerkung |
|---------|-----------|----------|----------|
| Kraftstoffprobe ziehen und visuell beurteilen | 10 min | Probenglas | Klar/hell = gut, trüb = Wasser, dunkel = Oxidation, Flocken = Diesel-Bug |
| Kraftstofffilter wechseln (Vorfilter) | 20 min | Filterschlüssel, neues Element | Auch bei optisch sauberem Filter zum Saisonstart wechseln |
| P/V-Ventil auf Funktion prüfen | 10 min | — | Blasen durch Ventil: Luft muss in beide Richtungen passieren |
| Tankgeber kalibrieren (Voll-/Leer-Referenz) | 15 min | Multimeter | Bei Saisonstart: Tank volltanken, Anzeige auf "Voll" prüfen |
| Erdungsverbindung messen (Widerstand) | 10 min | Multimeter | Max. 1 Ohm zwischen Tank und Motorblock |

#### 13.1.4 Jährliche Wartung

| Aufgabe | Zeitbedarf | Werkzeug | Anmerkung |
|---------|-----------|----------|----------|
| Tankoberfläche komplett auf Korrosion prüfen (Metalltanks) | 20 min | Taschenlampe, Spiegel | Weiße Ablagerungen (Alu), Rostflecken (Edelstahl), Risse (PE) |
| Tankinneninspektion (wenn Inspektionsöffnung vorhanden) | 30 min | Endoskop oder Spiegel+Lampe | Biofilm, Rost, Ablagerungen, Zustand Schwallbleche |
| Alle Anschlüsse auf Dichtheit prüfen | 15 min | Papierhandtuch, Taschenlampe | Papier um jeden Anschluss wickeln, 24h warten, auf Verfärbung prüfen |
| Entlüftungssystem komplett prüfen (Leitung, Ventil, Außenöffnung) | 20 min | Druckluft (max. 0,3 bar) | Durchblasen der Entlüftung |
| Tankbefestigung Drehmoment prüfen | 15 min | Drehmomentschlüssel | Gemäß Herstellerangabe oder: M8 = 20 Nm, M10 = 35 Nm |
| Isolationspads prüfen (Alu-Tanks) | 10 min | Sichtprüfung | Pads intakt, keine Metallkontakte, kein Wasser dazwischen |
| Kraftstoff mit Biozid behandeln (Winterlagerung) | 5 min | Grotamar 82 | 10 ml/100l bei Einwinterung |
| Stabilisator zusetzen (Winterlagerung) | 5 min | z.B. Pri-D | Gemäß Herstellerangabe |

#### 13.1.5 Fünf-Jahres-Wartung

| Aufgabe | Zeitbedarf | Werkzeug | Fachbetrieb? |
|---------|-----------|----------|-------------|
| Wandstärkenmessung Ultraschall (Metalltanks) | 60 min | US-Dickenmessgerät | Empfohlen |
| Tankgeber tauschen oder revidieren (Schwimmer-Typ) | 30 min | Gabelschlüssel | Nein |
| P/V-Ventil tauschen | 15 min | Gabelschlüssel | Nein |
| Entlüftungsschlauch tauschen | 30 min | Schlauchklemmen | Nein |
| Kraftstoff-Polishing durchführen | 240 min | Polishing-System | Empfohlen |
| Schweißnähte auf Rissbildung prüfen (Metalltanks) | 30 min | Farbeindring-Prüfung | Ja |

#### 13.1.6 Zehn-Jahres-Wartung

| Aufgabe | Zeitbedarf | Werkzeug | Fachbetrieb? |
|---------|-----------|----------|-------------|
| Umfassende Tankinneninspektion | 120 min | Endoskop, ggf. Tank öffnen | Ja |
| Drucktest wiederholen (0,3 bar / 5 min) | 30 min | Druckprüfgerät | Ja |
| Schwallbleche auf Rissbildung prüfen | 30 min | Endoskop | Ja |
| Komplette Neubeurteilung der Restlebensdauer | 60 min | — | Ja |
| Tankgeber durch modernen Typ ersetzen (kapazitiv/Ultraschall) | 60 min | — | Empfohlen |
| Alle Dichtungen und Flansche erneuern | 90 min | Gabelschlüssel, Dichtungen | Empfohlen |

### 13.2 Einwinterungsprozedur (Schritt für Schritt)

**Voraussetzung:** Boot wird für >3 Monate stilllegt (typisch November–März in Nordeuropa).

| Schritt | Aktion | Begründung |
|---------|--------|-----------|
| 1 | Tank VOLLTANKEN (max. 95%) | Minimiert Luftvolumen → minimiert Kondensat |
| 2 | Biozid zusetzen (Grotamar 82, 10ml/100l) | Verhindert Diesel-Bug-Wachstum über den Winter |
| 3 | Kraftstoff-Stabilisator zusetzen (z.B. Pri-D, 30ml/240l) | Verhindert Oxidation und Cetanzahl-Verlust |
| 4 | Motor 15 min laufen lassen | Verteilt Biozid und Stabilisator im gesamten System |
| 5 | Wasserabscheider leeren | Stehendes Wasser friert und beschädigt den Filter |
| 6 | Tankablassventil betätigen: Wasser ablassen | Restwasser entfernen |
| 7 | Entlüftungsöffnung prüfen: frei? | Blockierte Entlüftung → Unterdruck über Winter → Tankverformung |
| 8 | Tankumgebung trocknen | Stehendes Wasser zwischen Tank und Halterung → Korrosion |
| 9 | Erdung prüfen | Korrodierte Erdung → kein Schutz über Winter |
| 10 | Einfüllstutzen-Deckel fest verschließen | Kein Regenwasser-Eintritt |

### 13.3 Saisonstartprozedur (Schritt für Schritt)

| Schritt | Aktion | Begründung |
|---------|--------|-----------|
| 1 | Tankablassventil öffnen: 100ml ablassen und in Glas prüfen | Wasser? Sediment? Diesel-Bug-Flocken? |
| 2 | Kraftstofffilter wechseln (Vorfilter und Feinfilter) | Filter können über Winter Wasser anziehen |
| 3 | Entlüftung prüfen: Druckluft durchblasen | Insekten/Spinnen nisten im Frühling |
| 4 | P/V-Ventil auf Funktion prüfen | Membranen können über Winter verkleben |
| 5 | Tankanzeige prüfen (Tank sollte noch fast voll sein) | Deutlicher Verlust ohne Verbrauch = Leckage |
| 6 | Alle Anschlüsse visuell auf Leckage prüfen | Temperaturschwankungen über Winter können Verbindungen lockern |
| 7 | Erdungsmessung (Multimeter, max. 1 Ohm) | Korrosion über Winter möglich |
| 8 | Motor starten, 15 min laufen, Kraftstofffilter auf Blasen prüfen | Luft im System nach Filtertwechsel = normal, muss sich entlüften |
| 9 | Nach 1h Betrieb: alle Anschlüsse nochmals prüfen | Wärmeausdehnung kann versteckte Leckagen aufdecken |

### 13.5 Tankgeber-Vergleich und Auswahlhilfe

Tankgeber sind eine der häufigsten Fehlerquellen im Kraftstoffsystem. Die richtige Auswahl und Installation sind entscheidend für eine zuverlässige Füllstandsanzeige.

#### 13.5.1 Vergleich der Gebertechnologien

| Eigenschaft | Schwimmer/Widerstand | Kapazitiv | Ultraschall | Drucksensor |
|------------|---------------------|-----------|-------------|------------|
| Funktionsprinzip | Schwimmer bewegt Hebelarm über Widerstandsdraht | Dielektrizitätskonstante Kraftstoff vs. Luft | Laufzeitmessung Ultraschallpuls | Hydrostatischer Druck der Flüssigkeitssäule |
| Genauigkeit | ±5–10% | ±2–5% | ±1–3% | ±2–4% |
| Lebensdauer | 8–15 Jahre | 15–25 Jahre | 20+ Jahre | 15–20 Jahre |
| Seegangsempfindlichkeit | Hoch (springt) | Gering | Gering | Mittel |
| Einbau | Im Tank (Flansch oben) | Im Tank (Sonde) | Außen am Tankboden | Im Tank (Boden) |
| Wartung | Mittel (Sulfidierung) | Gering | Keine | Gering |
| Tankform-Kompensation | Nein (nur linear) | Programmierbar | Programmierbar | Nein (nur linear) |
| Kraftstoffkontakt | Ja | Ja | Nein | Ja |
| Preis (ca.) | 50–150 EUR | 150–400 EUR | 200–500 EUR | 100–300 EUR |
| Geeignet für PE-Tank | Ja | Ja | Besonders gut (außen) | Ja |
| Geeignet für Metall-Tank | Ja | Ja | Eingeschränkt (Schallleitung) | Ja |
| Geeignet für Bladder | Eingeschränkt | Nein | Ja (außen) | Nein |

#### 13.5.2 Widerstandsbereiche gängiger Tankgeber

| Hersteller/Standard | Leer (Ohm) | Voll (Ohm) | Verbreitung |
|---------------------|-----------|-----------|-------------|
| VDO (Europa, Standard) | 10 | 180 | EU Standard, Beneteau, Bavaria, Hanse |
| VDO (USA) | 240 | 33 | US-Markt (invertiert!) |
| Wema/SSI (Europa) | 0 | 190 | Skandinavien, Hallberg-Rassy |
| Faria (USA) | 240 | 33 | US-Markt |
| Teleflex (USA) | 240 | 33 | US-Markt, ältere Boote |
| Smiths (UK, alt) | 0 | 180 | UK, ältere Boote |
| KUS (China) | 0–190 oder 10–180 | konfigurierbar | OEM-Zulieferer |

**WARNUNG:** US-amerikanische Geber haben einen INVERTIERTEN Widerstandsbereich (hoher Widerstand = leer, niedriger = voll) im Vergleich zu europäischen Gebern (niedriger = leer, hoher = voll). Ein US-Geber an einem europäischen Display zeigt "voll" wenn der Tank leer ist und umgekehrt — eine potenziell gefährliche Fehlanzeige!

#### 13.5.3 Empfohlene Tankgeber nach Anwendung

| Anwendung | Empfohlener Gebertyp | Empfohlenes Produkt | Preis (ca.) |
|-----------|---------------------|---------------------|-------------|
| Segelyacht <12m, einfach | Schwimmer/Widerstand | Wema S3, VDO 224-011-000 | 60–90 EUR |
| Segelyacht >12m, zuverlässig | Kapazitiv | Maretron TLM150, Wema Flexgeber | 250–400 EUR |
| Motorboot, Bladder-Tank | Ultraschall (extern) | Gobius Pro, Mopeka Pro Check | 150–250 EUR |
| Motoryacht >15m | Kapazitiv mit Display | Maretron TLM200 + DSM250 | 500–900 EUR |
| Racing/Regatta | Ultraschall | Gobius Pro Serie | 180–280 EUR |
| Retrofit, einfache Installation | Ultraschall (extern) | Gobius 4 | 200–300 EUR |

### 13.6 Korrosionsschutz-Referenz für Kraftstofftanks

#### 13.6.1 Opferanoden für Aluminiumtanks

Aluminiumtanks können durch den Einbau von Opferanoden zusätzlich vor galvanischer Korrosion geschützt werden:

| Anodentyp | Material | Potenzial vs. SHE | Einsatzgebiet | Empfehlung für Tanks |
|-----------|---------|-------------------|---------------|---------------------|
| Zinkanode | Zink (Mil-A-18001H) | -1,10 V | Salzwasser | Für Tanks in Salzwasserbilgen |
| Magnesiumanode | Magnesium (MIL-A-21412) | -1,70 V | Süßwasser, geringe Leitfähigkeit | Für Tanks in Süßwasserbilgen |
| Aluminiumanode | Al-Zn-In (MIL-A-24779) | -1,15 V | Salzwasser, Brackwasser | Alternativ zu Zink |

**Installation:**
- Anode mit Edelstahl-Schraube und Kabel am Aluminiumtank befestigen
- Kontaktstelle am Tank: blank schleifen, Kontaktpaste (Duralac)
- Anode muss in Kontakt mit dem Elektrolyt (Bilgenwasser) stehen
- Anodenfläche: ca. 1% der zu schützenden Tankoberfläche
- Austausch wenn >50% der Anode verbraucht (jährliche Prüfung)

#### 13.6.2 Beschichtungssysteme für Metalltanks

| System | Anwendung | Schichtzahl | Trockenschichtdicke | Lebensdauer | Kosten/m² |
|--------|-----------|-------------|---------------------|-------------|-----------|
| Beizen + Passivieren (316L) | Schweißnähte, Standard | 1 | n/a | >20 Jahre | 5–10 EUR |
| Elektropolieren (316L) | Premium, Innenseite | 1 | 5–25 µm Abtrag | >20 Jahre | 30–60 EUR |
| Eloxieren (5083) | Außenseite, Standard | 1 | 15–25 µm | 10–15 Jahre | 15–30 EUR |
| Hartanodisieren (5083) | Außenseite, Premium | 1 | 40–80 µm | 15–20 Jahre | 25–50 EUR |
| 2K-Epoxid-Innenbeschichtung | Stahltanks, GFK-Tanks | 2 | 200–400 µm | 10–15 Jahre | 20–40 EUR |
| Tankbeschichtung (Jotun Tankguard) | Stahltanks (Superyacht) | 3 | 300–500 µm | 15–20 Jahre | 30–60 EUR |

#### 13.6.3 Galvanische Spannungsreihe — Relevante Materialien

Die folgende Tabelle zeigt das galvanische Potenzial (in belüftetem Seewasser bei 25°C) relevanter Materialien. Je weiter zwei Materialien in dieser Reihe auseinanderliegen, desto stärker die galvanische Korrosion bei Kontakt:

| Material | Potenzial vs. Ag/AgCl [mV] | Tendenz |
|----------|---------------------------|---------|
| Magnesium | -1.600 bis -1.630 | Sehr unedel (starke Opferanode) |
| Zink | -980 bis -1.030 | Unedel (Opferanode, Standardschutz) |
| **Aluminium 5083** | **-760 bis -900** | **Unedel (TANK — gefährdet!)** |
| Aluminium-Zink-Indium Anode | -1.050 bis -1.080 | Opferanode für Alu-Schutz |
| Stahl (Normalstahl) | -600 bis -710 | Mäßig unedel |
| Blei | -500 bis -550 | Mäßig unedel |
| Zinn | -300 bis -350 | Mäßig |
| **Edelstahl 316L (passiv)** | **+50 bis +150** | **Edel** |
| Bronze (Sn-Bronze) | -230 bis -280 | Mäßig edel |
| Kupfer | -190 bis -250 | Edel |
| Monel 400 | -100 bis -150 | Edel |
| Edelstahl 316L (aktiv, in Spalt) | -400 bis -500 | Mäßig (Spaltkorrosion!) |
| Titan | +50 bis +100 | Sehr edel |
| Graphit/Kohlefaser | +250 bis +350 | Extrem edel |

**Kritische Paarungen für Tanks:**

| Paarung | Potentialdifferenz | Korrosionsrisiko | Maßnahme |
|---------|-------------------|-----------------|----------|
| Alu 5083 + Edelstahl 316L | 810–1.050 mV | SEHR HOCH | Vollständige galvanische Isolation PFLICHT |
| Alu 5083 + Bronze (Borddurchlass) | 480–620 mV | HOCH | Isolation oder Kunststoff-Zwischenstück |
| Alu 5083 + Kupferrohr | 570–650 mV | HOCH | Kunststoff-Übergang |
| Alu 5083 + Normalstahl | 60–190 mV | GERING | Minimal, aber Isolation empfohlen |
| Edelstahl 316L + Bronze | 280–380 mV | MÄSSIG | Akzeptabel in den meisten Fällen |
| Edelstahl 316L + Kupfer | 240–340 mV | GERING–MÄSIG | Akzeptabel |
| Edelstahl 316L + Kohlefaser | 100–300 mV | MÄSIG | Isolation bei dauerhaftem Kontakt |

### 13.7 Werftseitige Tankinstallationen — Bekannte Modelle

Die folgende Übersicht dokumentiert die werksseitigen Tankinstallationen verbreiteter Serienyachten. Diese Informationen sind für die AYDI-Diagnostik relevant, da sie die Ausgangs-Spezifikation bei Bewertungen und Fehleranalysen liefern.

#### 13.7.1 Segelyachten — Diesel

| Werft/Modell | Baujahre | Tankvolumen | Material | Tanktyp | Position | Bekannte Probleme |
|-------------|----------|-------------|----------|---------|----------|-------------------|
| Bavaria 34 Cruiser | 2006–2012 | 140 l | Alu 5083 | Einbautank | Mittschiffs unter Salon | Lochfraß durch fehlende Isolation |
| Bavaria 40 Cruiser | 2006–2012 | 200 l | Alu 5083 | Einbautank | Mittschiffs | Galvanische Korrosion an Halterung |
| Bavaria C42 | 2018–2025 | 200 l | PE-HD | Einbautank | Mittschiffs | Bisher keine systematischen Probleme |
| Beneteau Oceanis 38.1 | 2016–2022 | 140 l | GFK-Integral | Integrationstank | Rumpf, achtern | Diesel-Permeation (Polyester-Harz) |
| Beneteau Oceanis 46.1 | 2017–2024 | 200 l | GFK-Integral | Integrationstank | Rumpf, 2 Tanks | Diesel-Permeation bei B7 |
| Beneteau Oceanis Yacht 54 | 2021–2025 | 300 l | 316L | Einbautank | Mittschiffs | Keine bekannten Probleme |
| Dehler 34 | 2013–2020 | 150 l | 316L | Einbautank | Mittschiffs | Keine bekannten Probleme |
| Dehler 38 | 2014–2022 | 160 l | 316L | Einbautank | Mittschiffs | Gelegentlich Tankgeber-Fehler |
| Hallberg-Rassy 40 | 2003–2015 | 260 l | 316L | Einbautank | Satteltanks | Keine systematischen Probleme |
| Hallberg-Rassy 43 Mk II | 2012–2023 | 480 l | 316L | Einbautank | Satteltanks | Diesel-Bug bei Langzeitlagerung (B7) |
| Hanse 418 | 2017–2024 | 200 l | GFK-Integral | Integrationstank | Rumpf | Permeation bei alten Modellen |
| Hanse 508 | 2018–2025 | 250 l | GFK-Integral + PE | Hybrid | Rumpf + Zusatz | Anschluss-Leckagen |
| Jeanneau Sun Odyssey 440 | 2018–2025 | 200 l | GFK-Integral | Integrationstank | Rumpf | Entlüftungsprobleme |
| Jeanneau Sun Odyssey 490 | 2019–2025 | 280 l | GFK-Integral | Integrationstank | Rumpf, 2 Tanks | Bisher keine systematischen Probleme |
| Najad 440 | 2003–2015 | 400 l | 316L | Satteltanks | Kiel, beidseitig | Hervorragende Qualität, keine Probleme |
| Oyster 565 | 2015–2025 | 600 l | 316L | Einbautank | Mittschiffs, tief | Keine bekannten Probleme |
| X-Yachts X4.3 | 2018–2025 | 200 l | 316L | Einbautank | Mittschiffs | Keine bekannten Probleme |

#### 13.7.2 Motorboote und Motoryachten — Diesel

| Werft/Modell | Baujahre | Tankvolumen | Material | Tanktyp | Position | Bekannte Probleme |
|-------------|----------|-------------|----------|---------|----------|-------------------|
| Linssen 40.9 AC | 2010–2025 | 800 l | 316L | Einbautank | Mittschiffs, tief | Keine bekannten Probleme |
| Linssen 45.9 AC | 2015–2025 | 1.200 l | 316L | Einbautanks (2×600l) | Satteltanks | Keine bekannten Probleme |
| Nimbus C11 | 2020–2025 | 500 l | Alu 5083 | Einbautank | Achterschiff | Bisher keine Probleme (neues Modell) |
| Princess V50 | 2015–2022 | 2× 800 l | 316L | Einbautanks | Satteltanks | Streustrom-Korrosion in Marinas |
| Princess F62 | 2018–2025 | 2× 1.500 l | 316L | Einbautanks | Satteltanks | Keine bekannten Probleme |
| Sealine C390 | 2017–2025 | 500 l | PE-HD | Einbautank | Achterschiff | Bisher keine systematischen Probleme |
| Targa 44 | 2015–2025 | 1.200 l | Alu 5083 | Einbautanks (2×600l) | Satteltanks | Opferanoden regelmäßig prüfen |
| Greenline 48 (Hybrid) | 2018–2025 | 400 l | 316L | Einbautank | Mittschiffs | Keine bekannten Probleme |
| Nordhavn 47 | 2002–2018 | 2× 1.500 l | Alu 5083 | Satteltanks | Kiel, beidseitig | Schwallblech-Ermüdung (>15 Jahre) |
| Fleming 55 | 2010–2025 | 2× 1.800 l | 316L | Einbautanks | Satteltanks | Keine bekannten Probleme |
| Grand Banks 54 | 2015–2025 | 2× 2.000 l | 316L | Einbautanks | Satteltanks | Keine bekannten Probleme |

**Hinweis AYDI-Integration:** Diese Tabellen werden im AYDI-System verwendet, um bei der Schnellanalyse (Level 1) die wahrscheinliche Tankkonfiguration anhand von Bootstyp und Baujahr zu schätzen. Bei der Profi-Analyse (Level 2) dienen sie als Referenz für den Abgleich mit den tatsächlich vorgefundenen Bedingungen.

### 13.8 Kraftstofftank-Zubehör — Übersicht und Empfehlungen

| Zubehörtyp | Empfohlenes Produkt | Hersteller | Funktion | Preis (ca.) |
|-----------|---------------------|-----------|----------|-------------|
| Wasserabscheider (Diesel) | 500FG (60 gph) | Racor (Parker) | Wasserabscheidung + Filtration 30µm | 250–380 EUR |
| Wasserabscheider (Diesel, groß) | 900FH (90 gph) | Racor (Parker) | Für Motoren >100 kW | 420–580 EUR |
| Wasserabscheider (Diesel, EU) | SWK 2000/5 | Separ (DE) | Deutsche Qualität, 5µm | 280–400 EUR |
| Wasserabscheider (Benzin) | 500FG-GAS | Racor (Parker) | Benzinversion mit 10µm Element | 280–420 EUR |
| Kraftstoff-Polishing-System | PFF5790 | Racor (Parker) | 240 l/h, 2µm, Timer | 1.200–1.600 EUR |
| Kraftstoff-Polishing-System | SP Diesel Purifier | Algae-X | 500 l/h, magnetisch + Filter | 2.200–2.800 EUR |
| Biozid (Diesel-Bug) | Grotamar 82 | Schülke & Mayr | Biozid, MBO-basiert, EU-zugelassen | 45 EUR / 500ml |
| Kraftstoff-Stabilisator | Pri-D | PRI Products | Langzeit-Stabilisator (2+ Jahre) | 22 USD / 473ml |
| Trockenmittelfilter (Entlüftung) | Desi-Dry Marine | Desi-Dry | Silicagel-Kartusche, regenerierbar | 35 EUR |
| Tankgeber (Schwimmer) | S3, 250mm | Wema (NO) | 0–190 Ω, marine grade | 65 EUR |
| Tankgeber (Schwimmer) | 224-011-000 | VDO (DE) | 10–180 Ω, 250mm | 75 EUR |
| Tankgeber (Ultraschall, extern) | Pro Serie | Gobius (SE) | Außenmontage, programmierbar | 200–300 EUR |
| Tankgeber (kapazitiv) | TLM150 | Maretron (US) | NMEA 2000, programmierbar | 350 EUR |
| P/V-Ventil | TANKVENT | Vetus (NL) | 16mm, ±0,2/0,05 bar | 48 EUR |
| Inspektionsdeckel (nachrüst) | INSPEC150 | Vetus (NL) | 150mm, Edelstahl mit O-Ring | 85 EUR |
| Inspektionsdeckel | 20301 | Perko (US) | 6" (152mm), Bronze/Edelstahl | 120 USD |
| Einfüllstutzen (Diesel) | TDF38A | Vetus (NL) | 38mm, 316L, beschriftet "DIESEL" | 55 EUR |
| Einfüllstutzen (Diesel, bündig) | 8851 | Whitecap (US) | 1½" NPT, 316L, bündig | 65 USD |
| Tankentlüftung (Außenöffnung) | VENTILOG | Vetus (NL) | 16mm, 316L, nach unten weisend | 28 EUR |
| Flammensperre | 0340 | Perko (US) | ⅝", Bronze, 40-mesh | 45 USD |
| Absorber-Pads (Notfall) | Oil-Only Sorbent | 3M | Bindet Kraftstoff, stößt Wasser ab | 40 EUR / 50 Stk. |

### 13.9 Diesel-Bug-Testverfahren — Detaillierte Anleitung

Die zuverlässige Diagnose einer mikrobiellen Kontamination im Diesel ist entscheidend für die richtige Behandlung. Drei Testverfahren stehen zur Verfügung:

#### 13.9.1 Fuelstat-Schnelltest (Immunoassay)

**Funktionsprinzip:** Antikörper-basierter Lateral-Flow-Test, vergleichbar mit einem Schwangerschaftstest. Detektiert spezifische Antigene von Hormoconis resinae (Cladosporium resinae) und Bakterien.

**Durchführung:**
1. Kraftstoffprobe aus dem tiefsten Punkt des Tanks ziehen (Ablassventil oder Saugpumpe)
2. Probe in Probenbecher füllen (mitgeliefert), 5 min ruhen lassen
3. Teststreifen aus Folie entnehmen, Schutzkappe entfernen
4. Probenkammer mit Kraftstoff aus dem Bodenbereich des Probenbechers füllen (Wasser-Diesel-Grenzschicht!)
5. Teststreifen in die Probenkammer einlegen
6. 10 Minuten bei 15–35°C entwickeln lassen
7. Ergebnis ablesen: Keine Linie = negativ, schwache Linie = niedrige Kontamination, starke Linie = hohe Kontamination

**Bewertung:**

| Ergebnis | Kategorie | Maßnahme |
|----------|-----------|----------|
| Negativ | Keine nachweisbare Kontamination | Keine sofortige Maßnahme, prophylaktisches Biozid empfohlen |
| Niedrig (ASTM Schwelle 1) | <10⁴ KBE/ml | Biozid-Behandlung (Grotamar 82, 10ml/100l) |
| Moderat (ASTM Schwelle 2) | 10⁴–10⁵ KBE/ml | Biozid + Filtration + Wasserentfernung |
| Hoch (ASTM Schwelle 3) | >10⁵ KBE/ml | Vollreinigung: Tank entleeren, mechanisch reinigen, Biozid, frischer Kraftstoff |

**Kosten:** ca. 30–40 EUR pro Test (Einzelpack), ca. 20–25 EUR pro Test (10er-Pack)
**Hersteller:** Conidia Bioscience, Cambridge, UK — www.fuelstat.com

#### 13.9.2 Liqui-Cult-Kulturtest (Dip-Slide)

**Funktionsprinzip:** Nährmedium auf einem Kunststoffträger wird in Kraftstoff getaucht. Mikroorganismen wachsen auf dem Nährmedium und werden nach 3–7 Tagen sichtbar als Kolonien.

**Durchführung:**
1. Kraftstoffprobe aus Tankboden ziehen
2. Dip-Slide aus steriler Verpackung entnehmen (NICHT mit Fingern berühren!)
3. Beide Seiten des Slides in Kraftstoff eintauchen (10 Sekunden)
4. Slide in das mitgelieferte Röhrchen zurückstecken
5. Bei 25–30°C lagern (NICHT im Kühlschrank — Wachstum benötigt Wärme)
6. Täglich kontrollieren: Kolonien zählen, Wachstum dokumentieren
7. Ergebnis nach 3 Tagen (Bakterien) bzw. 5–7 Tagen (Pilze) ablesen

**Bewertung:**

| Kolonien nach 7 Tagen | Kategorie | Geschätzte KBE/ml |
|-----------------------|-----------|-------------------|
| Keine | Sauber | <10² |
| 1–10 Kolonien | Geringe Kontamination | 10²–10³ |
| 10–100 Kolonien | Mäßige Kontamination | 10³–10⁴ |
| >100 Kolonien (zusammenfließend) | Schwere Kontamination | >10⁴ |

**Kosten:** ca. 15–25 EUR pro Dip-Slide, 10er-Pack ca. 120 EUR
**Vorteil:** Identifiziert auch die Art der Kontamination (Bakterien = eine Seite, Pilze/Hefen = andere Seite)

#### 13.9.3 Laboranalyse

Für die genaueste Diagnose wird eine Kraftstoffprobe an ein akkreditiertes Labor gesendet:

**Typische Analyseparameter:**

| Parameter | Methode | Bedeutung | Kosten (ca.) |
|-----------|---------|----------|-------------|
| Keimzahl total (KBE/ml) | Plattenkultur | Gesamtbelastung | 80 EUR |
| Pilz-Identifikation | PCR oder Mikroskopie | Identifiziert Hormoconis resinae etc. | 120 EUR |
| Wassergehalt | Karl-Fischer-Titration | ppm-genaue Wassermessung | 50 EUR |
| Säurezahl | Titration (ASTM D974) | Mikrobielle Stoffwechselprodukte | 60 EUR |
| Partikelzählung | ISO 4406 | Verschmutzungsgrad | 70 EUR |
| Vollanalyse (alle Parameter) | — | Umfassende Diagnose | 250–400 EUR |

**Empfohlene Labore (Deutschland/Europa):**
- SGS Institut Fresenius, Hamburg — www.sgs.com
- Bureau Veritas, Hamburg — www.bureauveritas.de
- Oelcheck GmbH, Brannenburg — www.oelcheck.de (spezialisiert auf Schmierstoff-/Kraftstoffanalyse)
- Intertek, Hamburg — www.intertek.com

### 13.10 Notfallverfahren

#### 13.4.1 Kraftstoffaustritt an Bord — Sofortmaßnahmen

**Diesel:**
1. Motor abstellen (wenn sicher möglich)
2. Absperrventil am Tank schließen (wenn zugänglich)
3. Bilgengebläse einschalten (Dampfentfernung)
4. Absorber-Pads/Tücher auslegen (z.B. 3M Oil-Only Sorbent)
5. Leckstelle lokalisieren und wenn möglich abdichten (Holzpflock, Epoxid-Kitt, Reparaturband)
6. Kontaminiertes Bilgenwasser NICHT automatisch abpumpen (Umwelthaftung!)
7. Hafenmeisterei informieren bei größeren Mengen (>5l)

**Benzin — EXPLOSIONSGEFAHR:**
1. KEINE elektrischen Schalter betätigen (Funkengefahr!)
2. KEINE offenen Flammen, KEIN Rauchen
3. Bilgengebläse einschalten (falls fest installiert und ex-geschützt)
4. Alle Personen aus geschlossenen Räumen evakuieren
5. Boot verlassen, wenn Dampfkonzentration hoch (Geruch intensiv)
6. Feuerwehr rufen (112)
7. Von Lee annähern (Wind bläst Dämpfe von Ihnen weg)

#### 13.4.2 Motorausfall durch Kraftstoffproblem auf See

1. Ruhe bewahren — Segeln setzen (Segelboot) oder Anker werfen (wenn möglich)
2. Position sichern: Seenotsender (DSC/VHF Kanal 16) bereithalten
3. Diagnose: Tank leer? → Umschalten auf anderen Tank / Reservekanister
4. Tank nicht leer? → Entlüftung blockiert? → Tankdeckel kurz öffnen (Zischen = Unterdruck = Entlüftung)
5. Entlüftung OK? → Filter verstopft? → Vorfilter prüfen, ggf. Notbetrieb ohne Vorfilter (nur kurzzeitig!)
6. Filter OK? → Luft im System? → Kraftstoffsystem entlüften (Motor-spezifisch, Handbuch konsultieren)
7. Alle Versuche erfolglos? → Schlepphilfe anfordern (VHF Kanal 16, Pan-Pan)

---

## 14. Ergänzende Referenztabellen und Berechnungsgrundlagen

### 13.1 Kraftstoffverbrauchstabellen nach Motorleistung

Die folgende Tabelle enthält typische Kraftstoffverbräuche für marine Dieselmotoren bei verschiedenen Laststufen. Diese Werte sind Grundlage für die Tankgrößenberechnung.

**Diesel-Innenbordmotoren (4-Takt, Common Rail, Abgasstufe EU Stage V / EPA Tier 3):**

| Motorleistung | Leerlauf (l/h) | 25% Last (l/h) | 50% Last (l/h) | 75% Last (l/h) | 100% Last (l/h) | Marschfahrt (l/h) |
|--------------|---------------|----------------|----------------|----------------|-----------------|-------------------|
| 10 kW (14 PS) | 0,4 | 0,8 | 1,4 | 2,0 | 2,8 | 1,2 |
| 20 kW (27 PS) | 0,6 | 1,3 | 2,5 | 3,8 | 5,2 | 2,2 |
| 30 kW (41 PS) | 0,8 | 1,8 | 3,5 | 5,5 | 7,5 | 3,2 |
| 40 kW (54 PS) | 1,0 | 2,3 | 4,5 | 7,0 | 9,8 | 4,0 |
| 55 kW (75 PS) | 1,2 | 3,0 | 6,0 | 9,5 | 13,0 | 5,5 |
| 75 kW (102 PS) | 1,5 | 4,0 | 8,0 | 12,5 | 17,5 | 7,5 |
| 100 kW (136 PS) | 1,8 | 5,2 | 10,5 | 16,5 | 23,0 | 9,8 |
| 150 kW (204 PS) | 2,5 | 7,5 | 15,0 | 24,0 | 34,0 | 14,5 |
| 200 kW (272 PS) | 3,2 | 9,8 | 20,0 | 31,0 | 44,0 | 18,5 |
| 300 kW (408 PS) | 4,5 | 14,5 | 29,0 | 46,0 | 65,0 | 27,0 |
| 400 kW (544 PS) | 5,8 | 19,0 | 38,0 | 60,0 | 85,0 | 35,0 |
| 500 kW (680 PS) | 7,0 | 23,5 | 47,0 | 75,0 | 105,0 | 43,0 |

**Hinweis Marschfahrt:** Marschfahrt entspricht typisch 60–70% Last bei Verdrängerfahrt, 50–60% Last bei Halbgleiterfahrt. Bei Gleitern unter Vollgas (Gleitschwelle) kann der Verbrauch kurzzeitig auf 120–150% des Marschverbrauchs steigen.

**Benzin-Außenbordmotoren (4-Takt, EFI):**

| Motorleistung | Leerlauf (l/h) | 25% Last (l/h) | 50% Last (l/h) | 75% Last (l/h) | 100% Last (l/h) | Marschfahrt (l/h) |
|--------------|---------------|----------------|----------------|----------------|-----------------|-------------------|
| 15 PS | 0,8 | 2,0 | 3,8 | 5,5 | 7,5 | 3,5 |
| 25 PS | 1,0 | 2,8 | 5,5 | 8,5 | 11,5 | 5,0 |
| 40 PS | 1,2 | 4,0 | 8,0 | 12,5 | 17,0 | 7,5 |
| 60 PS | 1,5 | 5,5 | 11,0 | 17,5 | 24,0 | 10,5 |
| 90 PS | 2,0 | 8,0 | 16,0 | 25,0 | 35,0 | 15,0 |
| 115 PS | 2,3 | 10,0 | 20,0 | 31,0 | 43,0 | 18,5 |
| 150 PS | 2,8 | 12,5 | 25,0 | 40,0 | 56,0 | 23,5 |
| 200 PS | 3,5 | 16,0 | 32,0 | 50,0 | 70,0 | 30,0 |
| 250 PS | 4,0 | 19,5 | 39,0 | 62,0 | 87,0 | 37,0 |
| 300 PS | 4,5 | 23,0 | 46,0 | 73,0 | 103,0 | 43,5 |

### 13.2 Tankgrößenberechnung — Vollständiges Berechnungsschema

**Schritt 1: Motorverbrauch ermitteln**
```
V_marsch [l/h] = Motorleistung [kW] × spez. Verbrauch [g/kWh] / (Kraftstoffdichte [g/l] × 1000)

Typische spezifische Verbräuche:
  Diesel Common Rail: 210–240 g/kWh
  Diesel mechanisch: 230–270 g/kWh
  Benzin EFI: 280–340 g/kWh
  Benzin Vergaser: 350–420 g/kWh
```

**Schritt 2: Fahrtdauer bestimmen**
```
t_fahrt [h] = Strecke [sm] / Geschwindigkeit_Marsch [kn]
```

**Schritt 3: Netto-Kraftstoffbedarf**
```
V_netto [l] = V_marsch [l/h] × t_fahrt [h]
```

**Schritt 4: Reserven addieren**
```
V_reserve [l] = V_netto × Reservefaktor

Reservefaktoren:
  Küstenfahrt (<20 sm): ×1,20 (20% Reserve)
  Küstennah (<100 sm): ×1,30 (30% Reserve)
  Offshore (>100 sm): ×1,50 (50% Reserve)
  Ozeanpassage: ×1,50 + Notfallreserve für 48h Motorgang bei Flaute
```

**Schritt 5: Nicht-nutzbare Kapazität berücksichtigen**
```
V_brutto [l] = V_reserve / 0,95

(5% des Tankvolumens sind typisch nicht nutzbar — unterhalb der Ansaughöhe)
```

**Schritt 6: Tankgröße wählen**
```
V_tank [l] = nächstgrößerer Standardtank ≥ V_brutto
```

**Berechnungsbeispiel — Segelyacht 12m, Ostsee-Kreuzfahrt:**

| Parameter | Wert | Bemerkung |
|-----------|------|----------|
| Motor | Yanmar 3YM30, 21,3 kW (29 PS) | |
| Spez. Verbrauch bei 75% Last | 245 g/kWh | Herstellerangabe |
| Marschverbrauch | 21,3 × 0,75 × 245 / (840 × 1000) × 1000 = 4,65 l/h | |
| Längste geplante Motorstrecke | 120 sm | Kiel → Bornholm |
| Marschgeschwindigkeit | 6,0 kn | |
| Fahrtdauer | 120 / 6,0 = 20 h | |
| Netto-Bedarf | 4,65 × 20 = 93 l | |
| Mit 30% Reserve | 93 × 1,30 = 121 l | |
| Brutto (5% nicht nutzbar) | 121 / 0,95 = 127 l | |
| **Gewählter Tank** | **160 l** | Nächster Standard-Tank |

### 13.3 Freier Oberflächeneffekt — Berechnung und Schwallblech-Dimensionierung

Der freie Oberflächeneffekt (Free Surface Effect, FSE) reduziert die effektive Stabilität eines Bootes:

```
Δ GM_FSE [m] = (ρ_fuel × i) / Δ

wobei:
  ρ_fuel = Kraftstoffdichte [t/m³] (Diesel: 0,84, Benzin: 0,75)
  i = Flächenträgheitsmoment der freien Oberfläche [m⁴]
  Δ = Verdrängung des Bootes [t]

Für einen rechteckigen Tank:
  i = (l × b³) / 12

wobei:
  l = Tanklänge [m] (in Fahrtrichtung)
  b = Tankbreite [m] (quer zur Fahrtrichtung)
```

**Beispielberechnung:**

| Parameter | Ohne Schwallblech | Mit 1 Schwallblech (Längsteilung) | Mit 2 Schwallblechen |
|-----------|-------------------|-----------------------------------|---------------------|
| Tankbreite b | 0,80 m | 0,40 m (je Hälfte) | 0,267 m (je Drittel) |
| Tanklänge l | 1,00 m | 1,00 m | 1,00 m |
| i pro Abteilung | 0,0427 m⁴ | 0,00533 m⁴ | 0,00158 m⁴ |
| i gesamt (alle Abt.) | 0,0427 m⁴ | 0,01067 m⁴ | 0,00474 m⁴ |
| Δ GM bei Δ=8t, Diesel | 4,48 mm | 1,12 mm | 0,50 mm |
| Reduktion vs. ohne | – | 75% | 89% |

**Erkenntnis:** Ein einziges Schwallblech in Längsrichtung reduziert den FSE um 75%. Zwei Schwallbleche: 89% Reduktion. Die Wirkung folgt der Kubik-Regel: n Schwallbleche → FSE auf 1/(n+1)³ × (n+1) = 1/(n+1)² des Originalwerts.

### 13.4 Tankwandstärkenberechnung nach Druckbelastung

Die erforderliche Mindest-Wandstärke eines metallischen Kraftstofftanks ergibt sich aus der hydrostatischen Belastung plus dynamischer Belastung bei Seegang:

```
p_stat [kPa] = ρ_fuel × g × h_fill
p_dyn [kPa] = ρ_fuel × g × h_fill × a_seegang
p_ges [kPa] = p_stat + p_dyn + p_test

wobei:
  ρ_fuel = Kraftstoffdichte [kg/m³] (Diesel: 840, Benzin: 750)
  g = 9,81 m/s²
  h_fill = Füllhöhe [m]
  a_seegang = Beschleunigungsfaktor (typ. 1,0–2,5 × g je nach CE-Kategorie)
  p_test = Prüfdruck (0,3 bar = 30 kPa nach ISO 21487, 0,21 bar = 21 kPa nach ABYC)
```

**Mindest-Wandstärke Edelstahl (ebene Platte, allseitig eingespannt):**

```
t_min [mm] = b × √(p_ges / (σ_zul × k))

wobei:
  b = kürzeste Seitenlänge der größten unversteiften Fläche [mm]
  p_ges = Gesamtdruck [MPa]
  σ_zul = zulässige Spannung = Re / S (Re: Streckgrenze, S: Sicherheitsfaktor)
  k = Formfaktor (4-seitig eingespannt: k ≈ 0,75)

Für 316L: Re = 170 MPa, S = 2,5, σ_zul = 68 MPa
Für 5083-O: Re = 125 MPa, S = 2,5, σ_zul = 50 MPa
```

**Beschleunigungsfaktoren nach CE-Kategorie:**

| CE-Kategorie | Vertikal-Beschleunigung | Lateral-Beschleunigung | Longitudinal |
|-------------|------------------------|----------------------|-------------|
| A (Ozean) | 2,5 g | 1,5 g | 1,0 g |
| B (Offshore) | 2,0 g | 1,2 g | 0,8 g |
| C (Küstennah) | 1,5 g | 0,8 g | 0,5 g |
| D (Geschützt) | 1,0 g | 0,5 g | 0,3 g |

### 13.5 Tankerdung und elektrische Anforderungen

Metalltanks müssen korrekt geerdet sein, um statische Aufladung (besonders beim Betanken) und Streustrom-Korrosion zu verhindern:

**Erdungsanforderungen (ISO 10088, ABYC E-11):**

| Anforderung | Spezifikation |
|------------|---------------|
| Erdungskabel | Min. 6 mm² verzinntes Kupfer (16 AWG) |
| Verbindung Tank → Motor | Max. 1 Ohm Widerstand (Gesamtkreis) |
| Verbindung Tank → Bordnetz-Masse | Max. 1 Ohm |
| Verbindung Einfüllstutzen → Tank | Metallisch durchgehend oder separates Erdungskabel |
| Kabelschuhe | Verzinnt, gecrimpt UND gelötet |
| Kontaktstelle | Blank geschliffen, mit Schutzpaste (Duralac, Tef-Gel) |
| Prüfung | Jährlich mit Multimeter, max. 1 Ohm |

**Streustrom-Schutz:**

Streuströme aus dem Landstromsystem (230V AC) können über den Masseleiter in den Bootskörper fließen und metallische Tanks korrodieren. Schutzmaßnahmen:

1. **Galvanischer Isolator:** Wird in die Schutzleiter-Verbindung zum Landanschluss eingebaut. Blockt galvanische Gleichströme (<1,5V), leitet Fehlerstrom (230V) durch. Produkte: ProSafe 30A (280 EUR), Mastervolt Galvanic Isolator (320 EUR), Victron Galvanic Isolator (180 EUR).

2. **Trenntransformator:** Galvanische Trennung des gesamten Landstromsystems. Teurer (1.500–4.000 EUR), aber umfassendster Schutz. Produkte: Mastervolt IVET 3600, Victron Isolation Transformer 3600.

3. **Potentialmessung:** Referenzelektrode (Ag/AgCl oder Zink) an der Außenhaut, Messung des Potentials zwischen Referenz und Tank. Normalwert 316L: +50 bis +150 mV. Negativer als -100 mV → aktive Korrosion.

### 13.6 Kraftstoff-Additiv-Referenz

| Additiv | Hersteller | Dosierung | Zweck | Preis (ca.) |
|---------|-----------|-----------|-------|-------------|
| Grotamar 82 | Schülke & Mayr | 5 ml/100l (Prophylaxe), 10 ml/100l (Sanierung) | Biozid gegen Diesel-Bug | 45 EUR / 500ml |
| Marine 16 Diesel Bug Treatment | Marine 16 | 1:1000 | Biozid gegen Diesel-Bug | 28 GBP / 500ml |
| Liqui Moly Marine Diesel Schutz | Liqui Moly | 25 ml/70l | Wasserdemulgation, Korrosionsschutz | 14 EUR / 500ml |
| Liqui Moly Marine Diesel Fließ-Fit | Liqui Moly | 30 ml/70l | Kälteschutz (bis -31°C) | 12 EUR / 500ml |
| Star Brite Star Tron | Star Brite | 30 ml/240l | Enzym-Kraftstoffbehandlung | 25 EUR / 500ml |
| Fuel Set Diesel | Yachticon | 25 ml/100l | Stabilisator, Korrosionsschutz | 18 EUR / 500ml |
| ValvTect Bioguard Plus 6 | ValvTect | 30 ml/380l | Biozid + Stabilisator | 35 USD / 473ml |
| Biobor JF | Hammonds | 1:2700 | Biozid (US-Standard) | 28 USD / 946ml |
| Pri-D | PRI | 30 ml/240l | Langzeit-Stabilisator (2+ Jahre) | 22 USD / 473ml |
| Diesel Kleen +Cetane Boost | Power Service | 30 ml/38l | Cetanbooster, Reinigung | 12 USD / 946ml |

**Hinweis Biozide:** In der EU unterliegen Biozide der Biozidprodukte-Verordnung (EU) Nr. 528/2012. Nicht alle in den USA erhältlichen Biozide sind in der EU zugelassen. Grotamar 82 und Marine 16 sind EU-zugelassen. Biobor JF hat seit 2023 eine EU-Zulassung. Andere Produkte: lokale Verfügbarkeit und Zulassung prüfen.

### 13.7 Typische Installations-Checkliste

Die folgende Checkliste kann als Grundlage für die AYDI-Tankinstallations-Bewertung verwendet werden:

**Vor der Installation:**

| Nr. | Prüfpunkt | Norm-Referenz | Pflicht/Empfohlen |
|-----|-----------|---------------|-------------------|
| 1 | Werkstoffzeugnis 3.1 vorhanden und geprüft | EN 10204 | Pflicht (Metall) |
| 2 | Drucktest-Protokoll vom Hersteller vorhanden | ISO 21487 | Pflicht |
| 3 | Tankbeschriftung vollständig (Hersteller, Baujahr, Volumen, Kraftstoffart, Norm) | ISO 21487 §5.9 | Pflicht |
| 4 | Schweißnähte visuell geprüft (keine Poren, Risse, Unterwölbungen) | EN ISO 5817 Level C | Pflicht (Metall) |
| 5 | Schwallbleche vorhanden und korrekt dimensioniert | ISO 10088 | Pflicht bei >750mm |
| 6 | Inspektionsöffnung vorhanden | ISO 10088 | Empfohlen ab 200l |
| 7 | Ablassventil am tiefsten Punkt | — | Empfohlen |

**Installation:**

| Nr. | Prüfpunkt | Norm-Referenz | Pflicht/Empfohlen |
|-----|-----------|---------------|-------------------|
| 8 | Tank auf ebenem Fundament gelagert | ISO 10088 | Pflicht |
| 9 | Galvanische Isolation (Alu-Tanks) | ISO 10088 | Pflicht (Alu) |
| 10 | Befestigung hält 4g in jeder Richtung | ISO 10088 | Pflicht |
| 11 | Spannbänder mit Gummiunterlage (PE-Tanks) | — | Empfohlen |
| 12 | Flexible Anschlüsse (gegen Vibration) | ISO 10088 | Empfohlen |
| 13 | Entlüftung nach außenbords verlegt | ISO 10088 | Pflicht |
| 14 | Anti-Siphon-Schleife über Wasserlinie | ISO 10088 | Pflicht |
| 15 | Flammensperre (Benzin) an Außenöffnung | ABYC H-24 | Pflicht (Benzin) |
| 16 | Insektenschutzgitter an Außenöffnung | — | Empfohlen |
| 17 | Erdung Tank → Motor, max. 1 Ohm | ISO 10088, ABYC E-11 | Pflicht (Metall) |
| 18 | Erdung Einfüllstutzen → Tank | ABYC E-11 | Pflicht |
| 19 | Einfüllstutzen mit Beschriftung ("DIESEL" oder "BENZIN") | ISO 10088 | Pflicht |
| 20 | Entnahme nicht durch Tankboden (oder mit Absperrventil) | ISO 10088 | Empfohlen |
| 21 | Rücklauf endet unter Kraftstoffniveau | ISO 10088 | Pflicht |
| 22 | Tankgeber installiert und kalibriert | — | Empfohlen ab 60l |

**Nach der Installation:**

| Nr. | Prüfpunkt | Norm-Referenz | Pflicht/Empfohlen |
|-----|-----------|---------------|-------------------|
| 23 | Drucktest durchgeführt (0,3 bar / 5 min) | ISO 21487 | Pflicht |
| 24 | Alle Anschlüsse auf Dichtheit geprüft | — | Pflicht |
| 25 | Entlüftung Funktionstest (Tank verschließen, 0,1 bar aufbringen, Druck muss über Entlüftung abbauen) | — | Empfohlen |
| 26 | Tankgeber-Kalibrierung überprüft (leer/voll) | — | Empfohlen |
| 27 | Installations-Dokumentation erstellt (Fotos, Prüfprotokolle) | — | Empfohlen |
| 28 | CE-Konformitätserklärung aktualisiert (wenn Tank ausgetauscht) | 2013/53/EU | Pflicht (CE-Boote) |

### 13.8 Temperaturverhalten von Kraftstoff im Tank

Kraftstoff dehnt sich bei Erwärmung aus und zieht sich bei Abkühlung zusammen. Bei großen Tanks und starken Temperaturschwankungen sind die Volumenänderungen erheblich:

```
ΔV [l] = V_0 × β × ΔT

wobei:
  V_0 = Ausgangsvolumen [l]
  β = kubischer Wärmeausdehnungskoeffizient [1/K]
  ΔT = Temperaturänderung [K]

Diesel: β = 0,00083 /K
Benzin: β = 0,00095 /K
```

**Beispiel:** 500l Diesel, Temperaturanstieg von 15°C auf 35°C (ΔT = 20K):
```
ΔV = 500 × 0,00083 × 20 = 8,3 l Volumenausdehnung
```

Dies bedeutet: Ein vollständig befüllter 500l-Tank muss 8,3 Liter Expansion verkraften. Ohne ausreichende Entlüftung baut sich ein Überdruck von ca. 0,1–0,3 bar auf (je nach Tanksteifigkeit). Bei einem weichen PE-Tank beult sich die Wand aus. Bei einem steifen Stahltank steigt der Druck und kann Dichtungen und Anschlüsse belasten.

**Konsequenz:** Tanks dürfen maximal zu 95% befüllt werden (5% Ausdehnungsreserve). Bei Tanks in Klimazonen mit großen Temperaturschwankungen (Tropen, Wüste): maximal 90%.

**Kondensat-Bildung:**

Wenn ein halbgefüllter Tank abkühlt, kondensiert Feuchtigkeit aus der Luft im Tank an der Tankwand:

| Tankgröße | Luftvolumen (50% voll) | Kondensat pro 10°C Abkühlung | Kondensat pro Jahr (geschätzt) |
|-----------|----------------------|------------------------------|-------------------------------|
| 100 l | 50 l Luft | ca. 2 ml | ca. 200 ml |
| 200 l | 100 l Luft | ca. 4 ml | ca. 400 ml |
| 500 l | 250 l Luft | ca. 10 ml | ca. 1.000 ml |
| 1.000 l | 500 l Luft | ca. 20 ml | ca. 2.000 ml |

**Erkenntnis:** Ein halbleerer 1.000l-Tank in mediterranem Klima (Tag/Nacht-Differenz 10–15°C) sammelt ca. 2 Liter Kondenswasser pro Jahr. Dies ist mehr als genug für Diesel-Bug-Wachstum und den Beginn von Korrosion.

### 13.9 Internationale Regelwerke — Vergleichsmatrix

| Anforderung | ISO 10088 (EU) | ABYC H-24 (USA, Benzin) | ABYC H-33 (USA, Diesel) | BSS (UK) | BV Marine (FR) |
|------------|----------------|--------------------------|--------------------------|----------|----------------|
| Drucktest | 0,3 bar / 5 min | 0,21 bar / 2 min | 0,21 bar / 2 min | 0,3 bar / 5 min | 0,35 bar / 10 min |
| Befestigung | 4g alle Richtungen | 3g lateral/long/vert | 3g lateral/long/vert | "Adequate" | 4g alle Richtungen |
| Schwallbleche | >750mm Dim. | >762mm (30") | >762mm (30") | >750mm | >750mm |
| Entlüftung außenbords | Pflicht | Pflicht | Pflicht | Pflicht | Pflicht |
| Flammensperre | Empfohlen (Benzin) | Pflicht (Benzin) | Nicht erforderlich | Pflicht (Benzin) | Pflicht (Benzin) |
| Erdung | Pflicht (Metall) | Pflicht, max 1Ω | Pflicht, max 1Ω | Pflicht | Pflicht |
| Tankgeber | Empfohlen ab 60l | Nicht spezifiziert | Nicht spezifiziert | Empfohlen | Pflicht ab 100l |
| Inspektionsöffnung | Empfohlen ab 200l | Nicht spezifiziert | Nicht spezifiziert | Empfohlen | Empfohlen |
| PE-Fluorierung | Empfohlen (Benzin) | Pflicht (Benzin) | Empfohlen | Empfohlen (Benzin) | Pflicht (Benzin) |
| Kennzeichnung | Hersteller, Baujahr, Vol., Kraftstoff, Norm | GASOLINE/DIESEL, Vol., Hersteller, Baujahr | GASOLINE/DIESEL, Vol., Hersteller, Baujahr | Material, Vol., Kraftstoff | Vollständig |
| Material-Zertifikat | 3.1 (Metall) | EPA 40 CFR 1060 (Kunststoff) | EPA 40 CFR 1060 (Kunststoff) | 3.1 (Metall) | 3.1 (Metall) |

### 13.10 Lebenszykluskostenvergleich Tankmaterialien

Die folgende Tabelle vergleicht die Gesamtkosten (Total Cost of Ownership) über 20 Jahre für einen 300l-Dieseltank auf einer 12m-Segelyacht:

| Kostenfaktor | Edelstahl 316L | Aluminium 5083 | PE-HD | GFK (Vinylester) | Bladder (PU/Nylon) |
|-------------|---------------|----------------|-------|------------------|-------------------|
| Anschaffung | 1.780 EUR | 1.200 EUR | 520 EUR | 1.000 EUR | 800 EUR |
| Installation | 800 EUR | 800 EUR | 400 EUR | 600 EUR | 300 EUR |
| Jährliche Wartung | 50 EUR | 80 EUR | 30 EUR | 40 EUR | 50 EUR |
| Wartung 20 Jahre | 1.000 EUR | 1.600 EUR | 600 EUR | 800 EUR | 1.000 EUR |
| Ersatz im Zyklus | 0 (>20J Lebensdauer) | 1.200 EUR (1× nach 15J) | 520 EUR (1× nach 15J) | 0 (>20J) | 800 EUR (1× nach 12J) |
| Ersatz-Installation | 0 | 800 EUR | 400 EUR | 0 | 300 EUR |
| **20-Jahres-Gesamtkosten** | **3.580 EUR** | **5.680 EUR** | **2.470 EUR** | **2.400 EUR** | **3.250 EUR** |
| **Kosten pro Jahr** | **179 EUR** | **284 EUR** | **124 EUR** | **120 EUR** | **163 EUR** |

**Erkenntnis:** Edelstahl 316L hat die höchsten Anschaffungskosten, aber über 20 Jahre die zweitniedrigsten Gesamtkosten (keine Ersatzbeschaffung nötig). Aluminium ist trotz niedrigerer Anschaffungskosten langfristig am teuersten (Korrosionsrisiko, Ersatz). PE-HD und GFK sind die günstigsten Optionen, wenn Zugang für Austausch gegeben ist.

### 13.11 AYDI-Bewertungskriterien für Tankinstallationen

Die AYDI-Plattform bewertet Tankinstallationen nach folgendem Schema (Score 0–100):

| Kriterium | Gewichtung | 100 Punkte | 50 Punkte | 0 Punkte |
|-----------|-----------|-----------|-----------|---------|
| Material-Eignung | 15% | Material optimal für Kraftstoff und Einsatz | Material geeignet, aber nicht optimal | Material ungeeignet |
| Wandstärke | 10% | ≥Empfohlen | ≥Minimum | <Minimum |
| Schwallbleche | 10% | Korrekt dimensioniert und installiert | Vorhanden, aber unterdimensioniert | Fehlend bei >750mm |
| Befestigung | 15% | 4g in allen Richtungen, isoliert | 2g, teilweise isoliert | Lose oder nicht gesichert |
| Entlüftung | 15% | Komplett mit P/V-Ventil, Flammensperre, Insektenschutz | Funktionsfähig, teilweise ausgestattet | Blockiert oder fehlend |
| Erdung | 10% | ≤1 Ohm, korrekt dokumentiert | Vorhanden, >1 Ohm | Fehlend |
| Inspektionsmöglichkeit | 5% | Inspektionsöffnung vorhanden | Teilzugang möglich | Kein Zugang |
| Ablassventil | 5% | Am tiefsten Punkt, funktionsfähig | Vorhanden, aber nicht optimal positioniert | Fehlend |
| Tankgeber | 5% | Kalibriert, <5% Abweichung | Vorhanden, 5–15% Abweichung | Fehlend oder >15% Abweichung |
| Dokumentation | 5% | Werkstoffzeugnis, Drucktest, Installationsprotokoll | Teilweise dokumentiert | Keine Dokumentation |
| Normkonformität | 5% | Alle relevanten Normen erfüllt | Teilweise konform | Wesentliche Abweichungen |

**Gesamtbewertung:**
- 90–100: Hervorragend — Keine Maßnahmen erforderlich
- 75–89: Gut — Kleinere Verbesserungen empfohlen
- 60–74: Befriedigend — Mehrere Verbesserungen empfohlen
- 40–59: Mangelhaft — Dringende Maßnahmen erforderlich
- 0–39: Ungenügend — Sofortige Stilllegung/Austausch empfohlen

---

### 14.13 Zukunftstechnologien und neue Entwicklungen

#### 14.13.1 Digitale Tanküberwachung

Moderne Tanksysteme integrieren zunehmend digitale Sensoren und Netzwerkprotokolle:

| Technologie | Funktion | Protokoll | Hersteller | Status |
|------------|----------|-----------|-----------|--------|
| NMEA 2000 Tankgeber | Digitale Füllstandsübertragung | NMEA 2000 (PGN 127505) | Maretron, Navico, Garmin | Marktreif |
| WiFi-Tankgeber | Smartphone-Überwachung | WiFi / BLE | Gobius, FloScan | Marktreif |
| IoT Tanksensor | Fernüberwachung via Cloud | MQTT / LoRaWAN | Siren Marine, Yacht Sentinel | Marktreif |
| Ultraschall-Inline-Wasserdetektot | Echtzeit-Wassergehalt im Kraftstoff | NMEA 2000 / CAN | Aquafine, Parker | Neueinführung |
| Multisensor-Pod | Temperatur + Füllstand + Wasser + Partikel | NMEA 2000 | In Entwicklung | Prototyp |

**NMEA 2000 PGN 127505 (Fluid Level):**
Standardisiertes Datenpaket für Füllstandsinformationen auf dem NMEA-2000-Bus. Enthält:
- Instance (Tanknummer)
- Fluid Type (Diesel, Benzin, Wasser, Abwasser, Öl)
- Level (0–100% in 0,004%-Schritten)
- Capacity (Nennvolumen in 0,1-Liter-Schritten)

Dies ermöglicht die Integration der Tankdaten in Chart-Plotter, MFDs und Monitoring-Systeme ohne proprietäre Verkabelung.

#### 14.13.2 Alternative Kraftstoffe und deren Tankanforderungen

| Kraftstoff | Dichte | Flammpunkt | Tankkompatibilität | Normlage |
|-----------|--------|------------|-------------------|----------|
| HVO (Hydrotreated Vegetable Oil) | 0,78 g/cm³ | >55°C | Alle Diesel-Tanks, unbedenklich | EN 15940, Drop-in |
| GTL (Gas-to-Liquid) | 0,77 g/cm³ | >55°C | Alle Diesel-Tanks, unbedenklich | EN 15940, Drop-in |
| B20 (20% Biodiesel) | 0,86 g/cm³ | >55°C | 316L, PE-HD OK; Alu + GFK-Poly: Vorsicht | EN 16709 |
| B100 (reiner Biodiesel) | 0,88 g/cm³ | >100°C | NUR 316L oder PE-HD-fluoriert | EN 14214 |
| E15 (15% Ethanol) | 0,73 g/cm³ | <-20°C | 316L, PE-XLPE fluoriert | SAE J2665 |
| E85 (85% Ethanol) | 0,79 g/cm³ | <-20°C | NUR 316L oder spezielle Tanks | Sonderzulassung |
| Methanol | 0,79 g/cm³ | +11°C | Spezielle Tanks erforderlich (316L oder HDPE-Fluor.) | In Entwicklung |

**HVO als Diesel-Ersatz im Yachtbereich:**
HVO (Hydrotreated Vegetable Oil, z.B. Neste MY Renewable Diesel) ist ein synthetischer Dieselkraftstoff aus erneuerbaren Quellen, der chemisch identisch mit Mineralöl-Diesel ist (Paraffine statt FAME). Vorteile: kein FAME-Gehalt → kein Diesel-Bug-Risiko, bessere Lagerstabilität, kein Wasseranzug. HVO ist ein "Drop-in" Ersatz — alle bestehenden Diesel-Tanks und -Systeme sind ohne Modifikation kompatibel. Nachteil: Preis ca. 20–40% höher als EN 590 Diesel. Verfügbarkeit: An ausgewählten Tankstellen und Bunkerstationen in Skandinavien, Deutschland und Benelux zunehmend verfügbar.

#### 14.13.3 Elektrifizierung und Hybrid — Auswirkungen auf Tanksysteme

Die zunehmende Elektrifizierung im Yachtbau (Greenline, Silent Yachts, X Shore, Candela) reduziert die Tankgrößen bei Hybridantrieben und eliminiert sie bei vollelektrischen Booten. Für die AYDI-Analyse ergeben sich folgende Implikationen:

- **Vollelektrisch:** Kein Kraftstofftank. Lithium-Batterien übernehmen die Energiespeicherung. Tanksysteme werden durch Batterie-Management-Systeme (BMS) ersetzt.
- **Diesel-Hybrid (z.B. Greenline 48 Hybrid):** Verkleinerter Kraftstofftank (typisch 50–70% der reinen Diesel-Version). Tankanforderungen identisch, aber weniger Volumen.
- **Range-Extender:** Sehr kleiner Tank (50–100l) für einen Generator. Tankqualität bleibt kritisch — auch ein kleiner Tank mit Diesel-Bug kann den Range-Extender lahmlegen.
- **Wasserstoff (Brennstoffzelle):** Derzeit experimentell im Yachtbereich (Toyota Marine, EFOY). Wasserstofftanks unterliegen völlig anderen Normen (ISO 11439, UN ECE R134) und sind nicht Gegenstand dieser Wissensdatei.

---

> **Ende der Wissensdatei 19.01 — Kraftstofftanks Grundlagen**
> Nächste Dateien: 19_02 (Kraftstofffilter und Wasserabscheider), 19_03 (Kraftstoffpumpen und Fördersysteme)
