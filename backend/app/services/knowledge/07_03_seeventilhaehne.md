# 07.03 — Seeventilhähne (Kugel-/Kegelhahn)

> **Modulkontext**: materials, structural, compliance, service_patterns, cost, production
> **Confidence-Klassen**: measured | calculated | visual_high | visual_medium | estimated | documented | benchmark
> **Pydantic-Hinweis**: `model_config = {"from_attributes": True}` — NIEMALS `class Config`
> **Letzte Aktualisierung**: 2026-04
> **SICHERHEITSKRITISCH**: Seeventilhähne sind die letzte Barriere gegen Wassereinbruch — Versagen = SINKEN

---

## Inhaltsverzeichnis

1. Einführung & Regulatorischer Rahmen
2. Zukunftstechnologien
3. Best Practices nach Revier & Klimazone
4. Regional Sourcing
5. Zweck dieser Wissensdatei
6. Pydantic-Modelle
7. Grundlagen
8. Hersteller — Vollständige Übersicht
9. Anlagen-spezifische Zuordnung

---

## 1. Einführung & Regulatorischer Rahmen

### 1.1 Abgrenzung: Seeventilhahn vs. Seeventil

Die Datei 07_01 behandelt das Gesamtsystem "Seeventil" (Borddurchlass + Ventilkörper + Anschluss). Diese Datei 07_03 fokussiert ausschließlich auf den **Ventilhahn** selbst — den Absperrmechanismus innerhalb des Seeventilkörpers. Der Ventilhahn ist das mechanische Herzstück: die Komponente, die tatsächlich den Wasserfluss kontrolliert.

**Zwei Grundprinzipien dominieren die maritime Ventiltechnik:**

| Prinzip | Kugelhahn (Ball Valve) | Kegelhahn (Tapered Plug Valve) |
|---|---|---|
| Absperrkörper | Durchbohrte Kugel, 90°-Drehung | Konischer Konus (Küken), 90°-Drehung |
| Dichtprinzip | PTFE-Sitzringe um Kugel | Metall-auf-Metall oder Fettschmierung |
| Durchfluss | Full-bore oder Reduced-bore | Immer Full-bore (zylindrischer Kanal) |
| Wartung | Quasi wartungsfrei (PTFE) | Regelmäßiges Nachschleifen/Fetten |
| Tradition | Modern (seit ~1970 in Yachten) | Traditionell (seit >100 Jahren) |
| Haptik | Leichtgängig, definierter Stopp | Schwerer, stufenloser Drehwiderstand |

(Confidence: documented — ISO 9093-1:2020, Fachliteratur Nigel Calder "Boatowner's Mechanical & Electrical Manual", 5th Ed.)

### 1.2 Warum der Ventilhahn-Typ entscheidend ist

Die Wahl zwischen Kugelhahn und Kegelhahn beeinflusst:

1. **Betriebssicherheit**: Ein festsitzender Hahn kann im Notfall nicht geschlossen werden. Kugelhähne sitzen seltener fest als Kegelhähne, WENN die PTFE-Dichtung intakt ist. Kegelhähne sitzen fest, wenn nicht regelmäßig betätigt und gefettet.
2. **Durchflussleistung**: Full-bore Kugelhähne und Kegelhähne bieten vollen Querschnitt. Reduced-bore Kugelhähne reduzieren den Durchfluss um 25–40% — kritisch bei Kühlwassersystemen.
3. **Lebensdauer**: Kugelhähne mit PTFE: 15–25 Jahre. Kegelhähne Bronze: 30–50+ Jahre bei Wartung. Kegelhähne ohne Wartung: 5–10 Jahre bis zum Festsitzen.
4. **Reparierbarkeit**: Kegelhähne sind vor Ort nachschleifbar. Kugelhähne mit verschlissener PTFE-Dichtung müssen komplett getauscht werden.
5. **Kostenstruktur**: Kugelhähne günstiger in der Anschaffung, teurer im Tausch. Kegelhähne teurer initial, günstiger über Lebensdauer.

| Kriterium | Kugelhahn | Kegelhahn | AYDI-Gewichtung |
|---|---|---|---|
| Notfall-Schließbarkeit | ★★★★★ | ★★★☆☆ | 30% |
| Durchfluss | ★★★★☆ (Full-bore: ★★★★★) | ★★★★★ | 20% |
| Lebensdauer | ★★★☆☆ (PTFE-abhängig) | ★★★★★ (bei Wartung) | 20% |
| Wartungsaufwand | ★★★★★ (quasi Null) | ★★☆☆☆ (jährlich fetten) | 15% |
| Reparierbarkeit | ★☆☆☆☆ (Tausch) | ★★★★★ (Nachschleifen) | 15% |

(Confidence: documented — Blakes Best Practice Guide, Groco Technical Manual)

### 1.3 Regulatorischer Rahmen für Ventilhähne

#### 1.3.1 ISO 9093:2020 — Anforderungen an den Ventilhahn

ISO 9093-1:2020 (metallisch) und ISO 9093-2:2020 (nichtmetallisch) definieren Anforderungen an den Ventilhahn als integralen Bestandteil des Seeventils:

| Anforderung | ISO 9093-1 (Metall) | ISO 9093-2 (Komposit) |
|---|---|---|
| Bauart | Kugel- oder Kegelhahn, ¼-Drehung | Kugelhahn, ¼-Drehung |
| Schließzeit | Max. ¼ Umdrehung (90°) | Max. ¼ Umdrehung (90°) |
| Betätigungskraft | ≤50 Nm bei DN50 (max. Nenngröße) | ≤30 Nm bei DN50 |
| Leckrate | Null-Leckage bei Prüfdruck | Null-Leckage bei Prüfdruck |
| Prüfdruck Ventilhahn | 2× Betriebsdruck, mind. 2 bar | 4× Betriebsdruck, mind. 3 bar |
| Zyklentest | 500 Zyklen ohne Leckage | 500 Zyklen ohne Leckage |
| Schließstellung | Griff quer zur Durchflussrichtung | Griff quer zur Durchflussrichtung |
| Kennzeichnung | "OPEN" / "SHUT" oder Pfeil | "OPEN" / "SHUT" oder Pfeil |
| Grifflänge | Ausreichend für Einhand-Bedienung | Ausreichend für Einhand-Bedienung |

**WICHTIG**: ISO 9093 verbietet ausdrücklich:
- Gate-Ventile (Schieberventile) — zu langsam, blockierungsanfällig
- Ventile mit >¼ Umdrehung — Notfallzeit zu lang
- Ventile ohne visuell erkennbare Stellung — Fehlbedienungsgefahr

(Confidence: documented — ISO 9093-1:2020 §5.3, ISO 9093-2:2020 §5.3)

#### 1.3.2 ISO 228 (BSP) — Gewindeanschlüsse

Die meisten europäischen Seeventilhähne verwenden BSP-Gewinde (British Standard Pipe) nach ISO 228-1:

| BSP-Größe | Außen-∅ mm | Kern-∅ mm | Steigung mm | Gangzahl/Zoll | Typische Anwendung |
|---|---|---|---|---|---|
| G ½" | 20,955 | 18,631 | 1,814 | 14 | Abflüsse, kleine Pumpen |
| G ¾" | 26,441 | 24,117 | 1,814 | 14 | Toiletten-Einlass, Bilge |
| G 1" | 33,249 | 30,291 | 2,309 | 11 | Kühlwasser klein |
| G 1¼" | 41,910 | 38,952 | 2,309 | 11 | Kühlwasser mittel |
| G 1½" | 47,803 | 44,845 | 2,309 | 11 | Kühlwasser Standard |
| G 2" | 59,614 | 56,656 | 2,309 | 11 | AC-System, große Motoren |

**Achtung BSP vs. NPT**: Amerikanische Hersteller (Groco, Forespar, Perko) verwenden NPT-Gewinde (National Pipe Thread, konisch). NPT und BSP sind NICHT kompatibel! Adapter erforderlich. NPT dichtet durch Konusverformung, BSP durch Flachdichtung oder O-Ring.

| Vergleich | BSP (ISO 228) | NPT (ANSI B1.20.1) |
|---|---|---|
| Gewindeform | Parallel (BSPP) oder konisch (BSPT) | Immer konisch |
| Dichtprinzip | O-Ring oder Flachdichtung | Gewindekonusverformung + Teflonband |
| Verbreitung Europa | Standard | Selten (USA-Importboote) |
| Verbreitung USA | Selten | Standard |
| Verwechslungsgefahr | ½" BSP ≠ ½" NPT (Gewindedurchmesser unterschiedlich!) | |

(Confidence: documented — ISO 228-1:2000, ANSI B1.20.1)

#### 1.3.3 ABYC H-27 — Ventilhahn-spezifische Anforderungen

ABYC H-27 (2021 Edition) stellt klare Anforderungen an den Ventilhahn:

- **H-27.4.2**: Nur ¼-Drehung-Ventile (Ball oder Plug) zulässig
- **H-27.4.3**: Gate-Ventile VERBOTEN als Seeventile
- **H-27.4.4**: Griff muss in geschlossener Stellung senkrecht zum Rohr stehen (quer zum Durchfluss)
- **H-27.4.6**: Grifflänge ≥100 mm bei DN25, ≥150 mm bei DN38, ≥200 mm bei DN50
- **H-27.4.7**: Griff darf nicht abnehmbar sein (fest verbunden oder gesichert)
- **H-27.4.8**: Ventilhahn muss bei einseitigem Druck (von See) dicht schließen
- **H-27.4.9**: Full-bore bevorzugt; Reduced-bore nur akzeptabel, wenn Durchflussanforderung erfüllt
- **H-27.5.1**: Ventilhahn-Material identisch oder galvanisch kompatibel mit Borddurchlass-Material

| ABYC H-27 Regel | Anforderung | Verstoß-Konsequenz |
|---|---|---|
| H-27.4.2 | Nur ¼-Drehung | Survey-Mangel, Versicherungsproblem |
| H-27.4.3 | Keine Gate-Ventile | Sofortiger Austausch gefordert |
| H-27.4.4 | Griffstellung = Durchflussanzeige | Fehlbedienungsgefahr |
| H-27.4.6 | Mindest-Grifflänge | Notfall-Schließbarkeit gefährdet |
| H-27.4.9 | Full-bore bevorzugt | Durchflussberechnung erforderlich |
| H-27.5.1 | Materialkompatibilität | Galvanische Korrosion |

(Confidence: documented — ABYC H-27:2021)

#### 1.3.4 DIN 3844 — Kegelhähne

DIN 3844 (Kegelhähne für allgemeine Anwendung) definiert grundlegende Konstruktionsprinzipien für Kegelhähne, die auch im maritimen Bereich relevant sind:

- **DIN 3844-1**: Maße und Toleranzen für geschmierte Kegelhähne
- **DIN 3844-2**: Anforderungen an Dichtflächen (Konuswinkel, Oberflächenrauheit)
- **DIN 3844-3**: Druckprüfung und Leckrate

| Anforderung DIN 3844 | Spezifikation | Marine-Relevanz |
|---|---|---|
| Konuswinkel | 1:5 bis 1:10 (Standard) | 1:6 bei Blakes, 1:8 bei Perko |
| Oberflächenrauheit Konus | Ra ≤ 0,8 µm (geschliffen) | Entscheidend für Dichtheit ohne O-Ring |
| Schmiermittel | Spezialfett oder Graphitpaste | Marinefett (wasserbeständig) erforderlich |
| Druckprüfung | 1,5× Nenndruck | Überlagert von ISO 9093 (2× Betriebsdruck) |
| Nachschleif-Reserve | Min. 2 mm Konus-Hub | Bestimmt Lebensdauer des Kegelhahns |

(Confidence: estimated — unverifiziert)

> ⚠️ **ZU PRÜFEN (Audit):** Die Normnummer **DIN 3844** passt nicht zum zitierten Scope. DIN 3844:1981-12 regelt "Heizungsarmaturen; Durchgangsventile (Globe Valves) PN 16 aus Kupferlegierung mit Muffenanschluß" — NICHT Kegelhähne. Die hier genannten Teile DIN 3844-1/-2/-3:1995 existieren nicht (DIN 3844 ist eine einzelne Ausgabe von 1981, nicht in Teile gegliedert). Eine korrekte Norm für Kegel-/Kükenhähne konnte nicht zweifelsfrei ermittelt werden — Angabe daher zurückgestuft. Die technischen Konstruktionsdaten (Konuswinkel 1:5–1:10, Ra ≤ 0,8 µm, Nachschleif-Reserve) bleiben als Fachwissen erhalten, jedoch ohne belastbaren Normbezug. (Web-verifiziert: dinmedia.de, DIN 3844:1981-12)

#### 1.3.5 DIN EN 13547 — Industrielle Kugelhähne

DIN EN 13547 (Kupferlegierungshähne) definiert Anforderungen an Kugelhähne aus Kupferlegierungen für den Industrieeinsatz, übertragbar auf Marine:

| Anforderung DIN EN 13547 | Spezifikation | Marine-Relevanz |
|---|---|---|
| Werkstoff Körper | CuZn40Pb2 (DZR), CuSn5Zn5Pb5 | Bronze C83600 bevorzugt für Salzwasser |
| Werkstoff Kugel | Verchromtes Messing oder Edelstahl | Edelstahl 316L für Marine |
| Dichtung Kugelsitz | PTFE (Standard), Viton (Hochtemperatur) | PTFE Standard, Viton für Auspuff-Nähe |
| Druckklasse | PN16, PN25, PN40 | PN16 ausreichend für Yachten |
| Leckrate | Rate A (Null-Leckage) nach EN 12266-1 | Pflicht für Unterwasser-Anwendung |
| Zyklentest | 2.500 Zyklen bei PN | 500 Zyklen nach ISO 9093 ausreichend |
| Temperaturbereich | -20°C bis +120°C (PTFE) | -20°C bis +60°C für Standard-Marine |

(Confidence: documented — DIN EN 13547:2003)

#### 1.3.6 Versicherungsrechtliche Anforderungen an den Ventilhahn

| Versicherer | Ventilhahn-spezifische Anforderung | Konsequenz |
|---|---|---|
| Pantaenius | Gate-Ventile = Ausschlussgrund | Kein Deckungsschutz |
| Yacht-Pool | Kugelhahn oder Kegelhahn, jährlich betätigt | Leistungskürzung bei festsitzendem Ventil |
| Pantaenius | Ventilgriff muss vorhanden und funktionstüchtig sein | Survey-Mangel |
| GJM (NL) | ISO 9093-konformer Hahn | Vertragsauflage |
| Allianz Marine | Full-bore bei Kühlwasser-Systemen | Empfehlung, kein Ausschluss |
| IIMS Survey | Jedes Ventil betätigen, Leichtgängigkeit dokumentieren | Pflichtpunkt im Survey |

(Confidence: documented — Versicherungsbedingungen 2024/2025, IIMS Survey Standards)

### 1.4 Historische Entwicklung des Seeventilhahns

| Epoche | Vorherrschender Typ | Material | Schwachstelle |
|---|---|---|---|
| vor 1920 | Kegelhahn, geschmiert | Rotguss, Messing | Korrosion, Undichtheit |
| 1920–1960 | Kegelhahn, geschliffen | Bronze C83600 | Festsitzen ohne Wartung |
| 1960–1980 | Gate-Ventile (Fehler!) | Messing, Bronze | Zu langsam, Blockierung |
| 1980–1995 | Kugelhahn, Messing | DZR-Messing | Dezinkifizierung nach 15+ Jahren |
| 1995–2010 | Kugelhahn, Bronze/Komposit | C83600, Marelon | PTFE-Alterung (Frühmodelle) |
| 2010–heute | Kugelhahn Full-bore, Bronze/Komposit | C83600, TruDesign | Qualitätsunterschiede No-Name |
| Parallel | Kegelhahn Premium (Blakes, Perko) | Bronze C83600/C92200 | Preis, Wartungsaufwand |

**Warum Gate-Ventile in der Ära 1960–1980 verbaut wurden:**
In den 1960er–1980er Jahren verbauten insbesondere amerikanische Werften (und durch deren Einfluss auch europäische) industrielle Gate-Ventile als Seeventile. Gründe: billiger, großer Querschnitt, leicht verfügbar. Das Problem: Gate-Ventile brauchen mehrere Umdrehungen zum Schließen (5–10 Sekunden statt <1 Sekunde bei ¼-Drehung), die Spindel korrodiert, und der Schieber blockiert. Die USCG dokumentierte allein 1978–1985 über 40 Sinkfälle durch versagende Gate-Ventile. ABYC verbot Gate-Ventile als Seeventile 1988.

(Confidence: documented — ABYC Historical Standards Archive, USCG Casualty Reports)

### 1.5 Druckklassen und Einsatzgrenzen

| Druckklasse | Prüfdruck bar | Betriebsdruck bar | Marine-Anwendung |
|---|---|---|---|
| PN6 | 9 | 6 | Oberhalb Wasserlinie, Entwässerung |
| PN10 | 15 | 10 | Standard Seeventil bis 2m Tiefgang |
| PN16 | 24 | 16 | Standard Seeventil Motoryacht |
| PN25 | 37,5 | 25 | Feuerlöschanlage, Hochdruck-Deckwasch |
| PN40 | 60 | 40 | Nicht marine-typisch |

**Praxis-Hinweis**: Die tatsächliche Druckbelastung eines Seeventils bei 2 m Tiefgang beträgt nur ca. 0,2 bar (hydrostatisch). Die höhere Prüfdruckklasse berücksichtigt dynamische Belastungen (Seegang, Aufsetzer, Wellenschlag) und Alterungssicherheit.

(Confidence: calculated — ISO 9093 + DIN EN 13547)

---

## 2. Zukunftstechnologien

### 2.1 Smart Valve Technology — Sensorintegrierte Ventilhähne

**Aktueller Stand (2026):**

Sensorintegrierte Ventilhähne befinden sich im Übergang von Konzeptstudien zu ersten Marktprodukten:

**Vetus BOW PRO / E-Valve Serie:**
- Elektromotorisch betätigter Kugelhahn (12V/24V DC)
- Positionssensor meldet Offen/Geschlossen an Bord-Monitoring
- Drehmoment-Überwachung: Erkennung von Schwergängigkeit (Indikator für Korrosion/Bewuchs)
- NMEA 2000-Anbindung (PGN 127501 — Valve Status)
- Notfall-Handbetätigung über Vierkant möglich
- Preis: 480–920 EUR je nach Nennweite

| Modell | Nennweite | Betätigungszeit | Drehmoment | Strom | Preis EUR |
|---|---|---|---|---|---|
| Vetus?"EV1210" | DN25 (1") | 8 s | 12 Nm | 2,1 A @ 12V | 480 |
| Vetus EV1510 | DN38 (1½") | 10 s | 18 Nm | 3,2 A @ 12V | 620 |
| Vetus EV2010 | DN50 (2") | 12 s | 25 Nm | 4,5 A @ 12V | 920 |

**Yacht Sentinel Smart Seacock Adapter:**
- Nachrüst-Sensor für bestehende Ventilhähne
- Erkennt: Griffposition (Offen/Geschlossen), Vibration, Temperatur, Feuchtigkeit
- LoRa-Funk zum zentralen Gateway
- Batteriebetrieben (CR123A, 2 Jahre Laufzeit)
- Cloud-Monitoring mit Push-Benachrichtigungen
- Preis: 95 EUR/Sensor + 290 EUR Gateway

**F&E-Projekte:**
- **Universität Southampton / MARIN**: Akustische Mikroleckage-Erkennung durch Ultraschall-Sensoren am Ventilkörper. TRL 4. Erkennung von Leckraten <2 ml/min theoretisch möglich.
- **Fraunhofer IKTS**: Keramikbeschichtete Kugel für Seeventile — extremer Verschleißschutz, chemisch inert. TRL 5. Kostenziel: +30% gegenüber Standard-PTFE-Kugelhahn.
- **CeramTec / TruDesign (Kooperation)**: Al₂O₃-beschichtete Kugelsitze für Komposit-Ventile. TRL 3.

(Confidence: documented — Vetus Katalog 2025/26, Yacht Sentinel Produktblatt | estimated — F&E-Status)

### 2.2 Materialinnovationen für Ventilhähne

**Kugelmaterialien — Nächste Generation:**

| Material Kugel | Aktuell | Zukunft | Vorteil | TRL |
|---|---|---|---|---|
| Verchromtes Messing | Standard (günstig) | Phase-out (Chromsorge) | Günstig | 9 (abnehmend) |
| Edelstahl 316L | Premium-Standard | Bleibend | Korrosionsfest | 9 |
| Edelstahl 316L + PVD-TiN | Selten (Industrieventile) | Zunehmend Marine | Ultraglatt, verschleißfest | 7 |
| Siliziumkarbid (SiC) | Keine Marine-Produkte | Prototypen | Extrem hart, chemisch inert | 4 |
| Aluminiumoxid (Al₂O₃) | Keine Marine-Produkte | CeramTec-Kooperation | Korrosionsfrei, biofilm-resistent | 3 |

**Dichtungsmaterialien — Evolution:**

| Material Dichtung | Temperaturbereich | Chemische Beständigkeit | Marine-Eignung | Kosten vs. PTFE |
|---|---|---|---|---|
| PTFE (Standard) | -200°C bis +260°C | Universell | ★★★★★ | 1,0× |
| PTFE + GF (glasfaserverstärkt) | -200°C bis +260°C | Universell | ★★★★★ | 1,2× |
| PTFE + Carbon | -200°C bis +260°C | Universell, leitfähig | ★★★★☆ | 1,5× |
| Viton (FKM) | -20°C bis +200°C | Kraftstoffe, Öle | ★★★★☆ (Auspuff) | 2,0× |
| EPDM | -40°C bis +120°C | Wasser, Dampf | ★★★☆☆ (kein Öl!) | 0,8× |
| PEEK | -60°C bis +250°C | Universell | ★★★★★ (Zukunft) | 8,0× |
| Kalrez (FFKM) | -20°C bis +315°C | Universell | ★★★★★ (Kosten!) | 15,0× |

**3D-Druck von Ventilhähnen:**
- Selektives Laserschmelzen (SLM) von Bronze-Pulver (CuSn10) ermöglicht optimierte Strömungsgeometrien
- Interne Kanäle mit gerundeten Übergängen statt scharfer Kanten
- Gewichtsreduktion 15–25% bei gleicher Festigkeit
- Aktuell nur Einzelstücke/Prototypen, keine Serienproduktion
- CT-Prüfung jedes Einzelstücks erforderlich (Porosität)
- Kostenabschätzung: 3–5× konventionelle Fertigung

(Confidence: estimated — Messe-Informationen Boot Düsseldorf 2025, METS Amsterdam 2025, Materialwissenschaftliche Fachliteratur)

### 2.3 Fernbetätigte Ventilhahn-Systeme

**Vollintegrierte Systeme für Kategorie-A-Yachten:**

CE-Kategorie A (Ozean) empfiehlt die Schließbarkeit aller Seeventile von einem zentralen Punkt. Dies erfordert fernbetätigte Ventilhähne.

| System | Hersteller | Antrieb | Steuerung | Preis/Ventil EUR | CE-Kat. |
|---|---|---|---|---|---|
| Vetus E-Valve | Vetus | 12/24V DC Motor | NMEA 2000 | 480–920 | A, B |
| Lewmar Smart Seacock | Lewmar | 12V DC Motor | CAN-Bus | 650–1.100 | A (angekündigt) |
| Custom (Superyacht) | Italvalvole | Pneumatisch / Hydraulisch | PLC | 1.500–3.500 | A |
| DIY Nachrüstung | Diverse | Linearaktuator | Relais | 150–300 | Keine Zulassung |

**AYDI-Bewertung**: Elektrisch fernbetätigte Ventilhähne erhalten im Compliance-Modul einen Bonus von +5 Punkten für Kategorie-A-Yachten und +3 Punkten für Kategorie-B-Yachten. Voraussetzung: Notfall-Handbetätigung muss gewährleistet sein.

**WARNUNG**: DIY-Nachrüstungen mit Linearaktuatoren haben keine CE-Zulassung als sicherheitskritische Komponente. AYDI bewertet solche Installationen mit Warnung "nicht normkonform" im Compliance-Modul.

(Confidence: documented — Vetus, estimated — Lewmar, Superyacht-Praxis)

---

## 3. Best Practices nach Revier & Klimazone

### 3.1 Ostsee / Nordeuropa (Brackwasser, 5–8 PSU, kalt)

| Aspekt | Empfehlung Ventilhahn | Begründung |
|---|---|---|
| Hahntyp | Kugelhahn Full-bore, Bronze oder Komposit | Geringe Korrosionsbelastung |
| Kugelmaterial | Edelstahl 316L oder verchromtes Messing | Brackwasser weniger aggressiv |
| Dichtung | PTFE Standard | Ausreichend für Temperaturen >-5°C |
| Wartungsintervall | Alle 6 Monate betätigen, jährlich Fett | Geringerer Bewuchs |
| Winterlager | Hähne OFFEN lassen an Land | Restwasser-Ablauf, Frostschutz |
| Anode | Zinkanode am Borddurchlass, alle 2 Jahre | Brackwasser = reduzierte Anodenlebensdauer |
| Typischer Fehler | Festsitzen durch Nichtbetätigung über Winter | Monatliche Betätigung in Saison |

**AYDI-Scoring Ostsee**: Reduktion der Korrosions-Gewichtung um 20% gegenüber Vollsalzwasser. Erhöhung der Frost-Gewichtung um 30%.

(Confidence: documented — SYV (Schwedischer Yachtverband) Empfehlungen, BSH Informationen)

### 3.2 Mittelmeer (Vollsalzwasser, 38 PSU, warm)

| Aspekt | Empfehlung Ventilhahn | Begründung |
|---|---|---|
| Hahntyp | Kugelhahn Full-bore, Bronze C83600 | Hohe Korrosionsbelastung |
| Kugelmaterial | Edelstahl 316L (NICHT verchromtes Messing!) | Salzwasser + Wärme = aggressive Korrosion |
| Dichtung | PTFE + GF (glasfaserverstärkt) | Höhere Standzeit bei Wärme + Salzkristallen |
| Wartungsintervall | Alle 3 Monate betätigen, halbjährlich Fett | Starker Bewuchs, Salzkristallbildung |
| Winterlager (im Wasser!) | Alle 2 Wochen betätigen | Kein Haul-out = Bewuchsrisiko |
| Bewuchsschutz | Antifouling bis Ventilhahn-Öffnung | Muscheln blockieren Ventilhahn |
| Anode | Zinkanode, jährlicher Tausch | Hohe Salzkonzentration = schneller Verbrauch |
| Typischer Fehler | Salzkristalle blockieren Kugelsitz | PTFE-GF-Dichtung + regelmäßige Betätigung |

**Mittelmeer-Spezifikum — Marinaströme:**
In vielen Mittelmeer-Marinas liegt aufgrund mangelhafter Erdung der Landstromanschlüsse ein erhebliches galvanisches Korrosionspotential vor. Ventilhähne aus Bronze, die über den Borddurchlass galvanisch mit dem Seewasser und benachbarten Booten verbunden sind, können beschleunigt korrodieren.

**Empfehlung**: Galvanischer Isolator (z.B. ProMariner ProSafe, Sterling Power PGI) am Landstromanschluss. Komposit-Ventilhähne (TruDesign, Marelon) eliminieren das Problem materialbedingt.

(Confidence: documented — Pantaenius Mittelmeer-Schadenstatistik, estimated — Praxis-Erfahrung)

### 3.3 Karibik / Tropen (Vollsalzwasser, 35 PSU, heiß + UV)

| Aspekt | Empfehlung Ventilhahn | Begründung |
|---|---|---|
| Hahntyp | Kugelhahn Full-bore, Bronze C83600 oder C92200 | Aggressivstes Umfeld |
| Kugelmaterial | Edelstahl 316L, PVD-beschichtet bevorzugt | Maximaler Korrosionsschutz |
| Dichtung | PTFE + GF oder Viton (bei >40°C Umgebung) | Temperaturresistenz |
| Wartungsintervall | Monatlich betätigen, vierteljährlich inspizieren | Extremer Bewuchs, Elektrolyse |
| Bewuchsschutz | Professionelles Antifouling + CuNi-Screens an Einlässen | Tropischer Bewuchs extrem aggressiv |
| Komposit-Warnung | TruDesign/Marelon: UV-Exposition vermeiden! | UV-Degradation bei Decksmontage |
| Typischer Fehler | Seepocken im Ventilhahn, Griff bricht | Vierteljährliche Reinigung + Inspektion |

**Karibik-Spezifikum — Teredo navalis (Schiffsbohrwurm):**
In tropischen Gewässern mit Wassertemperaturen >24°C kann der Schiffsbohrwurm Holz-Backing-Blocks angreifen. Dies hat keine direkte Auswirkung auf den Ventilhahn selbst, aber ein zerstörter Backing-Block kann zum Ausreißen des gesamten Seeventils führen. Empfehlung: GFK- oder Edelstahl-Backing-Blocks statt Holz in tropischen Revieren.

(Confidence: estimated — Langfahrt-Erfahrungsberichte, Noonsite.com Länderdaten)

### 3.4 Nordatlantik / Nordsee (Vollsalzwasser, 35 PSU, kalt + rau)

| Aspekt | Empfehlung Ventilhahn | Begründung |
|---|---|---|
| Hahntyp | Kegelhahn Bronze C92200 (Premium) oder Kugelhahn Full-bore C83600 | Mechanische Belastung durch Seegang |
| Kugelmaterial | Edelstahl 316L | Korrosionsfest + mechanisch belastbar |
| Dichtung | PTFE Standard | Keine extremen Temperaturen |
| Wartungsintervall | Halbjährlich betätigen + inspizieren | Salzwasser + mechanische Belastung |
| Griffsicherung | Schäkel oder Sicherungssplint am Griff | Griff darf bei Seegang nicht abfallen |
| Notholzpfropfen | Pflicht! Griffbereit an jedem Ventil | Blauwasser-Sicherheit |
| Typischer Fehler | Undichtheit durch mechanische Belastung (Seegang) | Hochwertige Hähne mit Druckklasse PN16+ |

(Confidence: documented — RYA Offshore Empfehlungen, ORC Special Regulations)

### 3.5 Arabischer Golf / Rotes Meer (Vollsalzwasser, 40+ PSU, extrem heiß)

| Aspekt | Empfehlung Ventilhahn | Begründung |
|---|---|---|
| Hahntyp | Kugelhahn Full-bore, Bronze C95800 (NiAlBr) oder C92200 | Höchste Salinität weltweit |
| Kugelmaterial | Edelstahl 316L + PVD-TiN-Beschichtung | Extreme Korrosionsbelastung |
| Dichtung | Viton (FKM) für AC-System (>50°C Wassertemp.) | PTFE ab 45°C Seewasser kritisch |
| Wartungsintervall | Monatlich inspizieren, vierteljährlich überholen | Salzkristallbildung extrem |
| AC-System | Überproportional belastet (Meerwasserkühlung bei >35°C) | Ventilhähne im AC-System doppelt so schnell verschlissen |
| Typischer Fehler | Salzkristall-Verblockung innerhalb von 6 Wochen ohne Betätigung | Wöchentliche Betätigung aller Hähne |

(Confidence: estimated — Superyacht-Betriebserfahrung, Marina-Berichte Dubai/Abu Dhabi)

### 3.6 Süßwasser / Binnenrevier

| Aspekt | Empfehlung Ventilhahn | Begründung |
|---|---|---|
| Hahntyp | Kugelhahn, auch Komposit oder DZR-Messing akzeptabel | Minimale Korrosionsbelastung |
| Kugelmaterial | Verchromtes Messing ausreichend | Kein Salzwasser |
| Dichtung | PTFE Standard | Keine besonderen Anforderungen |
| Wartungsintervall | Jährlich betätigen | Geringste Belastung |
| Materialwahl | DZR-Messing akzeptabel (keine Dezinkifizierung in Süßwasser) | Kostenersparnis möglich |
| Typischer Fehler | Muschelbewuchs (Dreissena) in Seen | Grobfilter vor Einlass |

**WARNUNG Süßwasser ≠ ungefährlich**: Auch in Süßwasser ist ein Seeventilhahn sicherheitskritisch. Die Anforderungen an Betätigbarkeit und Dichtheit gelten identisch.

(Confidence: documented — BSH Binnenschifffahrt-Regelwerk)

---

## 4. Regional Sourcing

### 4.1 Europa — Bezugsquellen für Seeventilhähne

| Land | Händler / Distributor | Marken | Lager | Lieferzeit | Anmerkung |
|---|---|---|---|---|---|
| DE | SVB (Bremen) | Groco, Guidi, TruDesign, Vetus, Osculati | Ja | 1–3 Tage | Größter deutscher Marine-Versand |
| DE | AWN (Hamburg) | Guidi, TruDesign, Vetus, Osculati | Ja | 1–3 Tage | Gutes Sortiment |
| DE | Toplicht (Hamburg) | Blakes, Groco, Guidi | Teilweise | 2–5 Tage | Spezialist, Beratung |
| DE | Compass24 | Vetus, Osculati, TruDesign | Ja | 1–3 Tage | Großes Lager, günstig |
| NL | Maritimus | Groco, Guidi, Vetus, Osculati | Ja | 1–2 Tage | Niederländischer Marktführer |
| NL | Vetus Direkt | Vetus | Ja | 1–2 Tage | Hersteller-Direktvertrieb |
| UK | Force 4 | Blakes, TruDesign, Groco | Ja | 1–3 Tage | UK-Marktführer Yacht-Zubehör |
| UK | Marine Superstore | Blakes, TruDesign | Ja | 1–3 Tage | Gute Preise |
| IT | Forniture Nautiche Italiane (FNI) | Guidi, Osculati | Ja | 1–2 Tage | Italienischer Großhändler |
| IT | Guidi Direkt | Guidi | Ja | 3–5 Tage | Hersteller in Poggibonsi (SI) |
| FR | Accastillage Diffusion | Guidi, TruDesign, Vetus | Ja | 2–4 Tage | Französischer Marktführer |
| ES | Garbí Náutica | Guidi, Osculati, Vetus | Teilweise | 3–7 Tage | Spanischer Marktführer |
| GR | Plotos Marine | Guidi, Vetus | Teilweise | 5–10 Tage | Griechenland-Versorgung |
| HR/MNE | Nautika Centar | Guidi, Osculati | Begrenzt | 5–14 Tage | Kroatien/Montenegro |
| TR | NautiStore Istanbul | Guidi, Vetus | Begrenzt | 7–14 Tage | Türkei-Versorgung |

### 4.2 Nordamerika — Bezugsquellen

| Land | Händler / Distributor | Marken | Lager | Lieferzeit | Anmerkung |
|---|---|---|---|---|---|
| USA | West Marine | Groco, Forespar, Perko, Apollo | Ja | 1–5 Tage | Größter US-Marinehändler |
| USA | Defender Industries | Groco, Forespar, Perko, TruDesign, Buck Algonquin | Ja | 1–3 Tage | Bester US-Versand, sehr günstig |
| USA | Jamestown Distributors | Groco, Nibco, Apollo, Buck Algonquin | Ja | 1–3 Tage | Profi-Werftbedarf |
| USA | Hamilton Marine | Groco, Perko, Buck Algonquin | Ja | 2–5 Tage | Neuengland-Spezialist |
| USA | Fisheries Supply | Groco, Forespar, Perko | Ja | 2–5 Tage | Pazifik-Nordwest |
| CAN | Canadian Tire Marine / LFS Marine | Groco, Forespar | Teilweise | 3–7 Tage | Kanada |

### 4.3 Ozeanien / Pazifik

| Land | Händler / Distributor | Marken | Lager | Lieferzeit | Anmerkung |
|---|---|---|---|---|---|
| NZ | TruDesign Direkt (Tauranga) | TruDesign | Ja | 1–2 Tage | Hersteller-Sitz! |
| NZ | Burnsco | TruDesign, Groco | Ja | 1–3 Tage | NZ-Marktführer |
| AU | Whitworths Marine | TruDesign, Groco, Forespar | Ja | 2–5 Tage | AU-Marktführer |
| AU | CH Smith | TruDesign, Guidi | Teilweise | 3–7 Tage | Melbourne |

### 4.4 Notversorgung auf Langfahrt — Ersatz-Strategien

| Situation | Strategie | Qualitätsbewertung |
|---|---|---|
| Kugelhahn defekt, kein Marine-Händler | Industrieller Kugelhahn Bronze PN16 (Sanitär/Heizung) | ★★★☆☆ — temporär akzeptabel, kein ISO 9093 |
| Kein Bronze-Hahn verfügbar | Edelstahl 316L Industrieventil PN16 | ★★★☆☆ — galvanisch prüfen! |
| Nur Messing verfügbar | NUR über Wasserlinie als Notlösung! Unter WL: NEIN | ★★☆☆☆ — GEFAHR bei Salzwasser |
| Kegelhahn-Konus verschlissen | Nachschleifen mit Schleifpaste (120er, dann 400er) | ★★★★☆ — Blakes-Tradition |
| PTFE-Dichtung defekt | Teflonband als Notdichtung um Kugel wickeln | ★★☆☆☆ — max. 48h Notlösung |
| Ventilkörper gerissen | KEIN Reparaturversuch! Notholzpfropfen + Epoxid | ★☆☆☆☆ — nur Notfall bis Werft |

(Confidence: estimated — Langfahrt-Erfahrungsberichte, Cruising World, Practical Sailor)

---

## 5. Zweck dieser Wissensdatei

### 5.1 Modulanbindung

Diese Wissensdatei stellt Referenzdaten für folgende AYDI-Analysemodule bereit:

| Modul | Nutzung der Seeventilhahn-Daten | Pipeline |
|---|---|---|
| **materials** | Werkstoff-Bewertung Ventilhahn, Kugel, Dichtung | A (Strukturiert) + B (Visuell) |
| **structural** | Druckklasse, Wandstärke, Belastungseignung | A (Strukturiert) |
| **compliance** | ISO 9093, ABYC H-27, DIN 3844, CE-Konformität | A (Strukturiert) |
| **service_patterns** | Verschleiß-Indikatoren, Wartungsintervalle, Fehlermuster | A + C (Text) |
| **cost** | Anschaffungskosten, Lebenszykluskosten, Austauschkosten | A (Strukturiert) |
| **production** | Fertigungskomplexität, Materialbeschaffung | A (Strukturiert) |
| **ergonomics** | Griffzugänglichkeit, Betätigungskraft, Notfall-Erreichbarkeit | A + B (Visuell) |

### 5.2 Confidence-Zuordnung für Ventilhahn-Bewertungen

| Datenquelle | Confidence-Level | Beschreibung |
|---|---|---|
| CAD-Modell mit Ventil-Spezifikation | `measured` | Exakte Maße, Werkstoff bekannt |
| Hersteller-Datenblatt + Modellnummer | `documented` | Hersteller-Angaben verifiziert |
| Foto mit erkennbarem Hersteller/Modell | `visual_high` | Klare visuelle Identifikation |
| Foto mit erkennbarem Typ (Kugel/Kegel) | `visual_medium` | Typ erkennbar, Details unsicher |
| Foto, Ventil kaum sichtbar | `visual_low` | Nur grobe Einschätzung |
| Foto, Ventil verdeckt/nicht sichtbar | `visual_insufficient` | Nicht beurteilbar |
| Werft + Baujahr → Schätzung | `estimated` | Aus OEM-Ausstattungsdaten abgeleitet |
| Industrie-Durchschnittswerte | `benchmark` | Aggregierte Marktdaten |

### 5.3 Abfrage-Interface

```python
# Typische Abfrage in AYDI Pipeline A:
def assess_valve_body(
    valve_type: str,           # "ball_valve" | "tapered_plug"
    material: str,             # "bronze_c83600" | "composite_trudesign" | ...
    bore_type: str,            # "full_bore" | "reduced_bore"
    nominal_diameter_mm: int,  # DN in mm
    manufacturer: str,         # "groco" | "blakes" | "trudesign" | ...
    model_number: str,         # z.B. "BV-1500" | "90305"
    application: str,          # "cooling_water_intake" | "toilet_intake" | ...
    age_years: int,            # Alter in Jahren
    last_service_date: str,    # ISO 8601
    boat_class: str,           # "production_sail" | "semi_custom" | "superyacht"
    sailing_area: str,         # "ostsee" | "mittelmeer" | "tropisch" | ...
) -> dict:
    """
    Gibt zurück:
    {
        "score": 0-100,
        "confidence": "measured|estimated|...",
        "findings": [...],
        "recommendations": [...],
        "replacement_cost_eur": float,
        "lifecycle_cost_20y_eur": float,
        "compliance": {"iso_9093": bool, "abyc_h27": bool},
    }
    """
```

(Confidence: documented — AYDI-Architekturspezifikation)

---

## 6. Pydantic-Modelle

### 6.1 Enums — Ventilhahn-spezifisch

```python
from pydantic import BaseModel, Field
from typing import Optional, Literal
from enum import Enum


class ValveBodyType(str, Enum):
    """Typ des Ventilhahns (Absperrmechanismus)."""
    BALL_VALVE = "ball_valve"                   # Kugelventil — Standard modern
    TAPERED_PLUG = "tapered_plug"               # Kegelhahn — traditionell (Blakes, Perko)
    GATE_VALVE = "gate_valve"                   # Schieberventil — VERBOTEN nach ISO 9093 + ABYC H-27!
    BUTTERFLY_VALVE = "butterfly_valve"         # Klappenventil — nur >DN50, Superyacht
    UNKNOWN = "unknown"


class ValveBodyBoreType(str, Enum):
    """Durchflussquerschnitt des Ventilhahns."""
    FULL_BORE = "full_bore"                     # Voller Querschnitt = Nennweite
    REDUCED_BORE = "reduced_bore"               # Reduzierter Querschnitt (typisch 60–75% der Nennweite)
    UNKNOWN = "unknown"


class ValveBodyMaterial(str, Enum):
    """Werkstoff des Ventilhahn-Körpers."""
    BRONZE_C83600 = "bronze_c83600"             # 85-5-5-5, Leaded Red Brass — Standard Marine
    BRONZE_C84400 = "bronze_c84400"             # 81 Red Brass — Economy Marine
    BRONZE_C92200 = "bronze_c92200"             # Navy G, Leaded Tin Bronze — Premium
    BRONZE_C95800 = "bronze_c95800"             # Nickel-Aluminium-Bronze — Superyacht/Hochleistung
    DZR_BRASS = "dzr_brass"                     # Entzinkungsbeständiges Messing (CW602N / CZ132)
    YELLOW_BRASS = "yellow_brass"               # GEFAHR — dezinkifizierungsanfällig!
    STAINLESS_316L = "stainless_316l"           # Edelstahl — Spezialanwendung
    COMPOSITE_MARELON = "composite_marelon"     # Forespar Marelon (glasfaserverstärkt)
    COMPOSITE_TRUDESIGN = "composite_trudesign" # TruDesign (glasfaserverstärktes Polyamid)
    COMPOSITE_OTHER = "composite_other"         # Andere Komposit-Hersteller
    CAST_IRON = "cast_iron"                     # Gusseisen — VERALTET, nur Bestandsboote
    UNKNOWN = "unknown"


class BallMaterial(str, Enum):
    """Werkstoff der Kugel (nur bei Kugelhähnen)."""
    CHROME_PLATED_BRASS = "chrome_plated_brass"   # Verchromtes Messing — Standard günstig
    STAINLESS_316L = "stainless_316l"             # Edelstahl 316L — Premium
    STAINLESS_316L_PVD = "stainless_316l_pvd"     # Edelstahl 316L + PVD-TiN — Hochleistung
    BRONZE = "bronze"                              # Bronze-Kugel (selten)
    COMPOSITE = "composite"                        # Komposit-Kugel (TruDesign)
    NOT_APPLICABLE = "not_applicable"              # Kein Kugelhahn (Kegel, Gate)
    UNKNOWN = "unknown"


class SealMaterial(str, Enum):
    """Werkstoff der Dichtung/Sitzringe."""
    PTFE = "ptfe"                               # Standard — universell
    PTFE_GF = "ptfe_gf"                         # PTFE glasfaserverstärkt — Marine Premium
    PTFE_CARBON = "ptfe_carbon"                 # PTFE kohlefaserverstärkt
    VITON_FKM = "viton_fkm"                     # Viton — Hochtemperatur (Auspuff-Nähe)
    EPDM = "epdm"                               # EPDM — nur Süßwasser/Nicht-Öl
    NITRILE_NBR = "nitrile_nbr"                 # Nitrilkautschuk — Kraftstoff/Öl
    METAL_ON_METAL = "metal_on_metal"           # Metall-auf-Metall — Kegelhahn traditionell
    GREASE_SEALED = "grease_sealed"             # Fettgeschmiert — Kegelhahn
    UNKNOWN = "unknown"


class HandleType(str, Enum):
    """Grifftyp des Ventilhahns."""
    LEVER = "lever"                             # Hebel — Standard Kugelhahn
    T_HANDLE = "t_handle"                       # T-Griff — manche Kegelhähne
    WING_HANDLE = "wing_handle"                 # Flügelgriff — Blakes-typisch
    SQUARE_HEAD = "square_head"                 # Vierkant — Werkzeugbetätigung (Kegelhahn)
    ELECTRIC_ACTUATOR = "electric_actuator"     # Elektrischer Antrieb
    PNEUMATIC_ACTUATOR = "pneumatic_actuator"   # Pneumatischer Antrieb
    NO_HANDLE = "no_handle"                     # Griff fehlt! — MANGEL
    UNKNOWN = "unknown"


class ThreadType(str, Enum):
    """Gewindeanschluss-Typ."""
    BSP_PARALLEL = "bsp_parallel"               # G-Gewinde, ISO 228 — Europa Standard
    BSP_TAPER = "bsp_taper"                     # R-Gewinde, konisch — Europa selten
    NPT = "npt"                                 # National Pipe Thread — USA Standard
    METRIC = "metric"                           # Metrisches Gewinde — selten bei Seeventilen
    FLANGED = "flanged"                         # Flanschanschluss — Superyacht/Industriell
    HOSE_BARB = "hose_barb"                     # Schlauchtülle — direkt
    UNKNOWN = "unknown"


class ValveApplication(str, Enum):
    """Einsatzzweck des Ventilhahns."""
    COOLING_WATER_INTAKE = "cooling_water_intake"     # Motorkühlung Einlass
    COOLING_WATER_DISCHARGE = "cooling_water_discharge" # Motorkühlung Auslass (selten)
    EXHAUST_WET = "exhaust_wet"                       # Nassauspuff
    TOILET_INTAKE = "toilet_intake"                   # WC Seewasser-Einlass
    TOILET_DISCHARGE = "toilet_discharge"             # WC Abwasser-Auslass
    TOILET_Y_VALVE = "toilet_y_valve"                 # Y-Ventil WC (See/Tank-Umschaltung)
    BILGE_DISCHARGE = "bilge_discharge"               # Bilgenpumpe Auslass
    GALLEY_DRAIN = "galley_drain"                     # Pantry Abfluss
    SINK_DRAIN = "sink_drain"                         # Waschbecken Abfluss
    SHOWER_DRAIN = "shower_drain"                     # Dusche Abfluss
    AC_INTAKE = "ac_intake"                           # Klimaanlage Seewasser-Einlass
    AC_DISCHARGE = "ac_discharge"                     # Klimaanlage Auslass
    GENERATOR_COOLING = "generator_cooling"           # Generator Kühlwasser-Einlass
    WATERMAKER_INTAKE = "watermaker_intake"            # Wassermacher Einlass
    ANCHOR_WASH = "anchor_wash"                       # Ankerspülung
    DECK_WASH = "deck_wash"                           # Deckwaschanlage
    FIRE_SYSTEM = "fire_system"                       # Feuerlöschanlage
    LIVEWELL = "livewell"                             # Köderbecken (Fischerboote)
    BALLAST = "ballast"                               # Ballasttank
    OTHER = "other"


class ValveConditionRating(str, Enum):
    """Zustandsbewertung des Ventilhahns."""
    EXCELLENT = "excellent"         # Neuwertiger Zustand (Score 90–100)
    GOOD = "good"                   # Guter Zustand, normale Spuren (70–89)
    FAIR = "fair"                   # Akzeptabel, Wartung empfohlen (50–69)
    POOR = "poor"                   # Mangelhaft, Austausch planen (30–49)
    CRITICAL = "critical"          # SOFORTIGER Austausch! Sinkgefahr! (0–29)
    NOT_ASSESSED = "not_assessed"   # Nicht beurteilbar
```

### 6.2 SeacockValveSpec — Spezifikation eines Seeventilhahns

```python
class SeacockValveSpec(BaseModel):
    """Technische Spezifikation eines einzelnen Seeventilhahns (Kugel-/Kegelhahn)."""

    model_config = {"from_attributes": True}

    # --- Identifikation ---
    id: Optional[str] = Field(None, description="Eindeutige ID im AYDI-System, z.B. 'VH-001'")
    seacock_id: Optional[str] = Field(None, description="Referenz auf übergeordnetes Seeventil (07_01), z.B. 'SV-001'")
    position: Optional[str] = Field(None, description="Position am Boot, z.B. 'Steuerbord, Frame 4, Maschinenraum'")
    application: ValveApplication = Field(..., description="Einsatzzweck")

    # --- Bauart ---
    valve_type: ValveBodyType = Field(..., description="Ventilhahn-Bauart (Kugel/Kegel/Gate/Klappe)")
    bore_type: ValveBodyBoreType = Field(
        ValveBodyBoreType.UNKNOWN, description="Durchflussquerschnitt (Full-bore/Reduced-bore)"
    )
    is_y_valve: bool = Field(False, description="Y-Ventil (Umschaltventil, z.B. WC See/Tank)?")
    quarter_turn: bool = Field(True, description="¼-Drehung (90°) Betätigung? (Pflicht nach ISO 9093)")

    # --- Werkstoffe ---
    body_material: ValveBodyMaterial = Field(..., description="Werkstoff Ventilhahn-Körper")
    ball_material: BallMaterial = Field(
        BallMaterial.UNKNOWN, description="Werkstoff der Kugel (nur Kugelhähne)"
    )
    seal_material: SealMaterial = Field(
        SealMaterial.UNKNOWN, description="Werkstoff Dichtung/Sitzringe"
    )
    stem_material: Optional[str] = Field(None, description="Werkstoff Spindel/Achse")
    handle_material: Optional[str] = Field(None, description="Werkstoff Griff (z.B. Bronze, Edelstahl, PA)")

    # --- Maße (alle in mm) ---
    nominal_diameter_mm: int = Field(..., ge=10, le=200, description="Nennweite in mm (DN)")
    bore_diameter_mm: Optional[int] = Field(
        None, description="Tatsächlicher Durchfluss-∅ in mm (bei Reduced-bore < nominal_diameter_mm)"
    )
    body_length_mm: Optional[int] = Field(None, description="Baulänge Ventilhahn-Körper in mm")
    body_height_mm: Optional[int] = Field(None, description="Bauhöhe (Achsmitte bis Flansch) in mm")
    body_width_mm: Optional[int] = Field(None, description="Baubreite (quer zum Durchfluss) in mm")
    flange_diameter_mm: Optional[int] = Field(None, description="Flanschdurchmesser (Anschluss Borddurchlass) in mm")
    wall_thickness_mm: Optional[float] = Field(None, ge=1.0, le=15.0, description="Wandstärke in mm")
    weight_g: Optional[int] = Field(None, description="Gewicht in Gramm")

    # --- Gewindeanschluss ---
    thread_type_inlet: ThreadType = Field(
        ThreadType.UNKNOWN, description="Gewindeart Einlass (zum Borddurchlass)"
    )
    thread_size_inlet: Optional[str] = Field(None, description="Gewindegröße Einlass, z.B. '1-1/2 BSP'")
    thread_type_outlet: ThreadType = Field(
        ThreadType.UNKNOWN, description="Gewindeart Auslass (zum Schlauch/Rohr)"
    )
    thread_size_outlet: Optional[str] = Field(None, description="Gewindegröße Auslass")
    hose_barb_diameter_mm: Optional[int] = Field(None, description="Schlauchtülle Außen-∅ in mm (falls Schlauchtülle)")

    # --- Griff ---
    handle_type: HandleType = Field(HandleType.UNKNOWN, description="Grifftyp")
    handle_length_mm: Optional[int] = Field(None, description="Grifflänge in mm")
    operating_torque_nm: Optional[float] = Field(None, description="Betätigungsdrehmoment in Nm")

    # --- Leistungsdaten ---
    pressure_class: Optional[str] = Field(None, description="Druckklasse, z.B. 'PN16', '150 PSI'")
    max_operating_pressure_bar: Optional[float] = Field(None, description="Max. Betriebsdruck in bar")
    test_pressure_bar: Optional[float] = Field(None, description="Prüfdruck in bar")
    temperature_range_min_c: Optional[int] = Field(None, description="Min. Betriebstemperatur in °C")
    temperature_range_max_c: Optional[int] = Field(None, description="Max. Betriebstemperatur in °C")
    flow_coefficient_kv: Optional[float] = Field(None, description="Durchflusskoeffizient Kv (m³/h bei 1 bar ΔP)")

    # --- Hersteller ---
    manufacturer: Optional[str] = Field(None, description="Hersteller, z.B. 'Groco', 'Blakes', 'TruDesign'")
    model_number: Optional[str] = Field(None, description="Modellnummer, z.B. 'BV-1500', '90305'")
    product_line: Optional[str] = Field(None, description="Produktlinie, z.B. 'BV-Serie', 'Tapered Plug'")
    year_of_manufacture: Optional[int] = Field(None, description="Herstellungsjahr")

    # --- Normen & Zulassungen ---
    iso_9093_compliant: Optional[bool] = Field(None, description="ISO 9093 konform?")
    iso_9093_version: Optional[str] = Field(None, description="ISO 9093 Version, z.B. '2020'")
    abyc_h27_compliant: Optional[bool] = Field(None, description="ABYC H-27 konform?")
    din_3844_compliant: Optional[bool] = Field(None, description="DIN 3844 konform? (nur Kegelhähne)")
    din_en_13547_compliant: Optional[bool] = Field(None, description="DIN EN 13547 konform? (nur Kugelhähne)")
    ul_listed: Optional[bool] = Field(None, description="UL-gelistet? (USA-Markt)")
    classification_approved: Optional[str] = Field(
        None, description="Klassifikation, z.B. 'Lloyd's', 'DNV-GL', 'RINA'"
    )

    # --- Kosten ---
    unit_cost_eur: Optional[float] = Field(None, ge=0, description="Stückpreis Ventilhahn in EUR")
    installation_cost_eur: Optional[float] = Field(None, ge=0, description="Einbaukosten in EUR (ohne Borddurchlass)")
    replacement_interval_years: Optional[int] = Field(None, description="Empfohlenes Austauschintervall in Jahren")
    lifecycle_cost_20y_eur: Optional[float] = Field(
        None, description="20-Jahres-Lebenszykluskosten in EUR (Anschaffung + Wartung + Austausch)"
    )

    # --- Confidence ---
    confidence: str = Field("estimated", description="measured|calculated|visual_high|visual_medium|estimated|documented|benchmark")
```

### 6.3 SeacockValveCondition — Zustandsbewertung eines Ventilhahns

```python
class SeacockValveCondition(BaseModel):
    """Zustandsbewertung eines einzelnen Seeventilhahns."""

    model_config = {"from_attributes": True}

    # --- Referenz ---
    valve_id: str = Field(..., description="Referenz auf SeacockValveSpec.id")
    assessment_date: Optional[str] = Field(None, description="Datum der Bewertung, ISO 8601")
    assessor: Optional[str] = Field(None, description="Prüfer / Surveyor")
    assessment_method: Optional[Literal["visual", "functional_test", "disassembly", "ndt", "full_survey"]] = Field(
        None, description="Bewertungsmethode"
    )

    # --- Gesamtbewertung ---
    condition_rating: ValveConditionRating = Field(..., description="Gesamtzustand")
    condition_score: int = Field(..., ge=0, le=100, description="Score 0–100")

    # --- Funktionsprüfung ---
    valve_operates_freely: Optional[bool] = Field(None, description="Ventilhahn lässt sich leichtgängig betätigen?")
    operating_torque_actual_nm: Optional[float] = Field(
        None, description="Gemessenes Betätigungsdrehmoment in Nm (Vergleich mit Soll)"
    )
    full_quarter_turn: Optional[bool] = Field(None, description="Volle 90°-Drehung möglich?")
    closes_completely: Optional[bool] = Field(None, description="Schließt vollständig (Null-Leckage)?")
    leakage_rate_ml_min: Optional[float] = Field(
        None, description="Leckrate in ml/min bei geschlossenem Hahn (Soll: 0)"
    )

    # --- Griff ---
    handle_intact: Optional[bool] = Field(None, description="Griff intakt und fest?")
    handle_position_indicator: Optional[bool] = Field(
        None, description="Griffstellung zeigt Offen/Geschlossen korrekt an?"
    )
    handle_accessible: Optional[bool] = Field(
        None, description="Griff ohne Werkzeug/Demontage erreichbar?"
    )
    handle_clearance_mm: Optional[int] = Field(
        None, description="Freiraum für Griffbewegung in mm (Min. 90°-Schwenkraum)"
    )

    # --- Korrosion (Metall-Hähne) ---
    no_visible_corrosion: Optional[bool] = Field(None, description="Keine sichtbare Korrosion?")
    corrosion_type: Optional[str] = Field(
        None, description="Korrosionsart: 'dezinkifizierung', 'lochfraß', 'spaltkorrosion', 'galvanisch', 'keine'"
    )
    dezincification_test_performed: Optional[bool] = Field(
        None, description="Salpetersäure-Test auf Dezinkifizierung durchgeführt?"
    )
    dezincification_test_result: Optional[Literal["bestanden", "dezinkifiziert", "nicht_durchgeführt"]] = Field(
        None, description="Ergebnis Dezinkifizierungs-Test"
    )
    wall_thickness_measured_mm: Optional[float] = Field(
        None, description="Gemessene Wandstärke in mm (Ultraschall)"
    )
    wall_thickness_min_mm: Optional[float] = Field(
        None, description="Minimale Wandstärke gemessen in mm"
    )

    # --- Dichtung ---
    seal_condition: Optional[Literal["intakt", "verschlissen", "porös", "fehlend", "nicht_prüfbar"]] = Field(
        None, description="Zustand der Dichtung/Sitzringe"
    )
    seal_leakage: Optional[bool] = Field(None, description="Dichtung undicht?")
    stem_packing_leakage: Optional[bool] = Field(None, description="Spindelpackung undicht?")

    # --- Kegelhahn-spezifisch ---
    taper_condition: Optional[Literal["gut_geschliffen", "leichte_rillen", "starke_rillen", "nachschleifen_nötig"]] = Field(
        None, description="Zustand der Konusfläche (nur Kegelhähne)"
    )
    taper_grease_present: Optional[bool] = Field(None, description="Kegelfett vorhanden? (nur Kegelhähne)")
    taper_adjustment_reserve_mm: Optional[float] = Field(
        None, description="Verbleibende Nachstell-Reserve in mm (nur Kegelhähne)"
    )

    # --- Bewuchs ---
    biofouling_present: Optional[bool] = Field(None, description="Bewuchs im/am Ventilhahn?")
    biofouling_severity: Optional[Literal["keine", "leicht", "mittel", "schwer", "blockierend"]] = Field(
        None, description="Bewuchsgrad"
    )

    # --- Visuelle Befunde ---
    photo_available: Optional[bool] = Field(None, description="Foto vorhanden?")
    visual_findings: Optional[list[str]] = Field(None, description="Liste visueller Befunde")

    # --- Empfehlung ---
    recommendation: Optional[str] = Field(None, description="Handlungsempfehlung")
    urgency: Optional[Literal["sofort", "innerhalb_30_tage", "nächstes_haul_out", "monitoring"]] = Field(
        None, description="Dringlichkeit"
    )
    estimated_repair_cost_eur: Optional[float] = Field(None, description="Geschätzte Reparatur-/Austauschkosten in EUR")

    # --- Confidence ---
    confidence: str = Field("visual_medium", description="Confidence der Bewertung")
```

### 6.4 ValveSystemAssessment — Gesamtbewertung aller Ventilhähne

```python
class ValveSystemAssessment(BaseModel):
    """Gesamtbewertung aller Seeventilhähne eines Bootes."""

    model_config = {"from_attributes": True}

    # --- Boot-Referenz ---
    boat_id: Optional[str] = Field(None, description="AYDI Boot-ID")
    boat_name: Optional[str] = Field(None, description="Bootsname")
    boat_type: Optional[str] = Field(None, description="Bootstyp, z.B. 'Bavaria 40 Cruiser'")
    boat_year: Optional[int] = Field(None, description="Baujahr")
    hull_material: Optional[str] = Field(None, description="Rumpfmaterial: GFK, Stahl, Alu, Holz")
    sailing_area: Optional[str] = Field(None, description="Hauptrevier: 'ostsee', 'mittelmeer', 'tropisch', ...")

    # --- Ventilhahn-Inventar ---
    total_valve_bodies: int = Field(..., ge=0, description="Gesamtanzahl Ventilhähne")
    valves_below_waterline: int = Field(..., ge=0, description="Davon unterhalb Wasserlinie")
    valves_assessed: int = Field(..., ge=0, description="Davon bewertet")

    # --- Bauart-Verteilung ---
    count_ball_valve: int = Field(0, description="Anzahl Kugelhähne")
    count_tapered_plug: int = Field(0, description="Anzahl Kegelhähne")
    count_gate_valve_danger: int = Field(0, description="Anzahl Schieberventile (VERBOTEN!)")
    count_butterfly_valve: int = Field(0, description="Anzahl Klappenhähne")
    count_y_valve: int = Field(0, description="Anzahl Y-Ventile")

    # --- Bore-Typ-Verteilung ---
    count_full_bore: int = Field(0, description="Anzahl Full-bore")
    count_reduced_bore: int = Field(0, description="Anzahl Reduced-bore")

    # --- Material-Verteilung ---
    count_bronze: int = Field(0, description="Anzahl Bronze-Hähne")
    count_composite: int = Field(0, description="Anzahl Komposit-Hähne")
    count_dzr_brass: int = Field(0, description="Anzahl DZR-Messing-Hähne")
    count_yellow_brass_danger: int = Field(0, description="Anzahl Messing-Hähne (GEFAHR!)")
    count_stainless: int = Field(0, description="Anzahl Edelstahl-Hähne")
    count_unknown_material: int = Field(0, description="Anzahl unbekanntes Material")

    # --- Material-Konsistenz ---
    materials_consistent: Optional[bool] = Field(
        None, description="Alle Ventilhähne aus kompatiblem Material? (galvanisch)"
    )
    material_mismatch_findings: list[str] = Field(
        default_factory=list, description="Befunde zu Materialinkompatibilitäten"
    )

    # --- Gesamtbewertung ---
    system_score: int = Field(..., ge=0, le=100, description="Gesamtscore 0–100")
    worst_valve_score: int = Field(..., ge=0, le=100, description="Schlechtester Einzelscore")
    average_valve_score: Optional[float] = Field(None, description="Durchschnittlicher Score")
    critical_findings: list[str] = Field(default_factory=list, description="Kritische Befunde")
    warnings: list[str] = Field(default_factory=list, description="Warnungen")
    recommendations: list[str] = Field(default_factory=list, description="Empfehlungen")

    # --- Funktionalität ---
    all_valves_operable: Optional[bool] = Field(None, description="Alle Hähne leichtgängig betätigbar?")
    count_stuck_valves: int = Field(0, description="Anzahl festsitzender Hähne")
    count_leaking_valves: int = Field(0, description="Anzahl undichter Hähne")
    all_handles_present: Optional[bool] = Field(None, description="Alle Griffe vorhanden?")
    all_handles_accessible: Optional[bool] = Field(None, description="Alle Griffe zugänglich?")

    # --- Normen-Compliance ---
    all_iso_9093_compliant: Optional[bool] = Field(None, description="Alle Hähne ISO 9093 konform?")
    all_abyc_h27_compliant: Optional[bool] = Field(None, description="Alle Hähne ABYC H-27 konform?")
    all_quarter_turn: Optional[bool] = Field(None, description="Alle Hähne ¼-Drehung? (Pflicht)")

    # --- Kosten ---
    estimated_replacement_cost_critical_eur: Optional[float] = Field(
        None, description="Geschätzte Kosten Austausch aller kritischen Hähne in EUR"
    )
    estimated_full_refit_cost_eur: Optional[float] = Field(
        None, description="Geschätzte Kosten Komplett-Erneuerung aller Hähne in EUR"
    )
    lifecycle_cost_20y_eur: Optional[float] = Field(
        None, description="20-Jahres-Gesamtlebenszykluskosten in EUR"
    )

    # --- Einzelbewertungen ---
    individual_specs: list[SeacockValveSpec] = Field(
        default_factory=list, description="Spezifikationen pro Ventilhahn"
    )
    individual_conditions: list[SeacockValveCondition] = Field(
        default_factory=list, description="Zustandsbewertungen pro Ventilhahn"
    )

    # --- Confidence ---
    confidence: str = Field("estimated", description="Confidence der Gesamtbewertung")
```

### 6.5 Scoring-Logik für Ventilhähne

```python
def calculate_valve_body_score(spec: dict, condition: dict) -> int:
    """
    Berechnet den Zustandsscore eines Seeventilhahns.
    
    Scoring-Regeln (Score 0–100):
    - Basiswert: 100
    - KRITISCHE Mängel: sofort auf max. 29 (= CRITICAL)
    - Schwere Mängel: jeweils -15 bis -25
    - Mittlere Mängel: jeweils -5 bis -10
    - Leichte Mängel: jeweils -2 bis -5
    - Bonus für Premium-Ausstattung: +0 bis +5
    """
    score = 100

    # ====== KRITISCHE MÄNGEL — Score sofort ≤29 ======
    
    # Gate-Ventil = VERBOTEN nach ISO 9093 + ABYC H-27
    if spec.get("valve_type") == "gate_valve":
        return 10  # SOFORT AUSTAUSCHEN
    
    # Yellow Brass = dezinkifizierungsgefährdet
    if spec.get("body_material") == "yellow_brass":
        return 10  # SOFORT AUSTAUSCHEN
    
    # Dezinkifizierung nachgewiesen
    if condition.get("dezincification_test_result") == "dezinkifiziert":
        return 5   # AKUTE SINKGEFAHR
    
    # Ventilhahn sitzt fest — kann im Notfall nicht geschlossen werden
    if condition.get("valve_operates_freely") is False:
        score = min(score, 25)
    
    # Hahn schließt nicht vollständig — Wassereinbruch möglich
    if condition.get("closes_completely") is False:
        score = min(score, 20)
    
    # Wandstärke unter Minimum (ISO 9093: ≥3mm für DN≤38, ≥4mm für DN>38)
    wall_min = condition.get("wall_thickness_min_mm")
    nominal_dn = spec.get("nominal_diameter_mm", 25)
    if wall_min is not None:
        min_required = 3.0 if nominal_dn <= 38 else 4.0
        if wall_min < min_required * 0.7:  # <70% der Mindestdicke
            return 15  # AKUTE BRUCHGEFAHR
        elif wall_min < min_required:
            score = min(score, 29)  # Unter Mindestdicke

    # ====== SCHWERE MÄNGEL — jeweils -15 bis -25 ======
    
    # Sichtbare Korrosion
    if condition.get("no_visible_corrosion") is False:
        corr_type = condition.get("corrosion_type", "")
        if corr_type == "dezinkifizierung":
            score -= 25
        elif corr_type == "lochfraß":
            score -= 25
        elif corr_type == "galvanisch":
            score -= 20
        else:
            score -= 15
    
    # Dichtung undicht
    if condition.get("seal_leakage") is True:
        score -= 20
    
    # Spindelpackung undicht
    if condition.get("stem_packing_leakage") is True:
        score -= 15
    
    # Griff fehlt!
    if spec.get("handle_type") == "no_handle" or condition.get("handle_intact") is False:
        score -= 20  # Notfall-Bedienung nicht möglich
    
    # Griff nicht erreichbar
    if condition.get("handle_accessible") is False:
        score -= 15

    # ====== MITTLERE MÄNGEL — jeweils -5 bis -10 ======
    
    # Reduced-bore bei Kühlwasser-Anwendung
    if spec.get("bore_type") == "reduced_bore" and spec.get("application") in [
        "cooling_water_intake", "generator_cooling", "ac_intake"
    ]:
        score -= 10  # Durchfluss-Einschränkung bei kritischer Anwendung
    
    # Keine ¼-Drehung (Multi-Turn)
    if spec.get("quarter_turn") is False:
        score -= 10
    
    # Bewuchs mittel bis schwer
    biofouling = condition.get("biofouling_severity", "keine")
    if biofouling == "blockierend":
        score -= 15
    elif biofouling == "schwer":
        score -= 10
    elif biofouling == "mittel":
        score -= 5
    
    # Kegelhahn ohne Fett
    if spec.get("valve_type") == "tapered_plug" and condition.get("taper_grease_present") is False:
        score -= 10
    
    # Kegelhahn — Nachstellreserve aufgebraucht
    reserve = condition.get("taper_adjustment_reserve_mm")
    if reserve is not None and reserve < 1.0:
        score -= 10
    
    # Griffstellung zeigt nicht korrekt an
    if condition.get("handle_position_indicator") is False:
        score -= 5

    # ====== LEICHTE MÄNGEL — jeweils -2 bis -5 ======
    
    # Dichtung verschlissen (aber noch dicht)
    if condition.get("seal_condition") == "verschlissen":
        score -= 5
    
    # DZR-Messing statt Bronze (akzeptabel, aber nicht optimal)
    if spec.get("body_material") == "dzr_brass":
        score -= 3
    
    # Leichter Bewuchs
    if biofouling == "leicht":
        score -= 2
    
    # Kegelhahn — leichte Rillen
    if condition.get("taper_condition") == "leichte_rillen":
        score -= 3

    # ====== BONUS ======
    
    # Full-bore Kugelhahn bei Kühlwasser = optimal
    if (spec.get("valve_type") == "ball_valve" 
        and spec.get("bore_type") == "full_bore"
        and spec.get("application") in ["cooling_water_intake", "generator_cooling"]):
        score += 3
    
    # Bronze C92200 (Premium) = Bonus
    if spec.get("body_material") == "bronze_c92200":
        score += 2
    
    # Edelstahl-Kugel = Bonus
    if spec.get("ball_material") in ["stainless_316l", "stainless_316l_pvd"]:
        score += 2

    return max(0, min(100, score))


def calculate_valve_system_score(individual_scores: list[int]) -> int:
    """
    Berechnet den Gesamtscore des Ventilhahn-Systems.
    
    Regel: Der Gesamtscore ist das GEWICHTETE MINIMUM.
    - 60% Gewichtung auf den schlechtesten Einzelscore
    - 40% Gewichtung auf den Durchschnitt
    
    Begründung: Ein einziges versagendes Seeventil kann das Boot sinken lassen.
    Das schwächste Glied bestimmt die Kette.
    """
    if not individual_scores:
        return 0
    
    worst = min(individual_scores)
    avg = sum(individual_scores) / len(individual_scores)
    
    system_score = int(worst * 0.6 + avg * 0.4)
    
    # KRITISCH: Wenn ein Einzelscore ≤29 → System max. 35
    if worst <= 29:
        system_score = min(system_score, 35)
    
    return max(0, min(100, system_score))
```

(Confidence: documented — AYDI-Scoring-Framework)

---

## 7. Grundlagen

### 7.1 Kugelhahn (Ball Valve) — Konstruktion und Funktionsprinzip

#### 7.1.1 Aufbau

Ein Kugelhahn besteht aus folgenden Komponenten:

| Komponente | Funktion | Typischer Werkstoff Marine |
|---|---|---|
| Ventilkörper (Body) | Gehäuse, trägt alle Komponenten | Bronze C83600, Komposit |
| Kugel (Ball) | Absperrkörper mit zylindrischer Bohrung | Edelstahl 316L, verchromtes Messing |
| Sitzringe (Seats) | Dichten die Kugel ab, oben + unten | PTFE, PTFE-GF, Viton |
| Spindel (Stem) | Überträgt Drehbewegung auf Kugel | Edelstahl 316, Bronze |
| Spindelpackung (Packing) | Dichtet Spindel ab | O-Ring PTFE oder Viton |
| Griff (Handle) | Betätigung ¼-Drehung | Bronze, Edelstahl, PA |
| Anschlagnocken (Stops) | Begrenzen Drehung auf 90° | Im Körper integriert |
| Gewindeanschluss (Ports) | Verbindung zu Borddurchlass + Schlauch/Rohr | BSP oder NPT |

**Funktionsprinzip:**
Die Kugel hat eine zylindrische Durchgangsbohrung. In Offenstellung fluchtet die Bohrung mit dem Durchflusskanal → voller Durchfluss. Eine 90°-Drehung bringt die geschlossene Kugeloberfläche vor den Kanal → Absperrung. Die PTFE-Sitzringe drücken durch Vorspannung gegen die Kugel und erzeugen eine Null-Leckage-Dichtung (bubble-tight).

#### 7.1.2 Full-bore vs. Reduced-bore

| Eigenschaft | Full-bore | Reduced-bore |
|---|---|---|
| Durchfluss-∅ | = Nennweite (z.B. DN38 → 38 mm Bohrung) | 60–75% der Nennweite (z.B. DN38 → 25 mm) |
| Durchfluss | 100% des Rohrleitungsquerschnitts | 40–60% des Rohrleitungsquerschnitts |
| Druckverlust (Kv) | Minimal (Kv ≈ Rohrleitung) | Signifikant (Kv 40–60% der Rohrleitung) |
| Baugröße | Größerer Körper, schwerer | Kompakter, leichter |
| Kosten | +30–50% gegenüber Reduced-bore | Standard |
| Anwendung | Kühlwasser, AC, Generator (durchflusskritisch) | Abflüsse, Bilge (nicht durchflusskritisch) |

**AYDI-Bewertungsregel:**
- Full-bore bei Kühlwasser, AC, Generator: **Pflicht** (Reduced-bore = Abzug -10 Punkte)
- Full-bore bei Abfluss, Bilge, Toilette: **Empfohlen** (Reduced-bore = kein Abzug)
- Full-bore bei Auspuff (Nassauspuff): **Kritisch** (Reduced-bore = Abzug -15 Punkte, Überhitzungsgefahr)

(Confidence: documented — Groco Technical Manual, DIN EN 13547)

#### 7.1.3 PTFE-Dichtungen — Lebensdauer und Versagensmodi

PTFE (Polytetrafluorethylen, "Teflon") ist das Standard-Dichtungsmaterial für maritime Kugelhähne:

| Eigenschaft | PTFE Standard | PTFE-GF (glasfaserverstärkt) | PTFE-Carbon |
|---|---|---|---|
| Temperaturbereich | -200°C bis +260°C | -200°C bis +260°C | -200°C bis +260°C |
| Druckfestigkeit | 10 N/mm² | 14 N/mm² | 12 N/mm² |
| Verschleißfestigkeit | Mittel | Hoch (+3× Standard) | Sehr hoch (+5× Standard) |
| Chemische Beständigkeit | Universell | Universell | Universell (leitfähig!) |
| Kriechneigung | Hoch (Cold Flow) | Gering | Gering |
| Marine-Lebensdauer | 10–15 Jahre | 15–25 Jahre | 20–30 Jahre |
| Preis vs. Standard | 1,0× | 1,2–1,5× | 1,5–2,0× |

**Versagensmodi PTFE-Dichtung:**

1. **Cold Flow (Kaltfließen)**: PTFE verformt sich unter Dauerlast plastisch. Folge: Spiel zwischen Kugel und Sitzring → Leckage. Zeitraum: 10–15 Jahre bei Standard-PTFE, länger bei PTFE-GF.
2. **Salzkristall-Abrasion**: Salzkristalle in Seewasser schleifen PTFE-Oberfläche ab. Beschleunigt durch seltene Betätigung (Kristalle sedimentieren).
3. **UV-Degradation**: Nur relevant bei Komposit-Ventilen mit UV-exponiertem PTFE-Sitz (selten).
4. **Thermische Degradation**: Ab 260°C zersetzt sich PTFE unter Freisetzung toxischer Gase. Marine-relevant nur bei Auspuff-Nähe ohne Isolation.
5. **Chemische Quellüng**: PTFE ist universell chemisch beständig. Einzige Ausnahme: geschmolzene Alkalimetalle und Fluor — nicht marine-relevant.

(Confidence: documented — DuPont Teflon Technical Guide, Parker Sealing Guide)

#### 7.1.4 Viton (FKM) — Alternative Dichtung für Hochtemperatur

| Eigenschaft | Viton (FKM) | PTFE (Vergleich) |
|---|---|---|
| Temperaturbereich | -20°C bis +200°C | -200°C bis +260°C |
| Elastizität | Hoch (Elastomer) | Null (Thermoplast) |
| Seewasser-Beständigkeit | Gut | Ausgezeichnet |
| Kraftstoff-/Öl-Beständigkeit | Ausgezeichnet | Ausgezeichnet |
| Druckfestigkeit | 20 N/mm² | 10 N/mm² |
| Kriechneigung | Minimal | Hoch |
| Marine-Anwendung | Auspuff-Nähe, Motorraum >60°C | Standard, universell |
| Preis vs. PTFE | 2,0–3,0× | 1,0× |

**AYDI-Regel**: Viton-Dichtung erhält Bonus +3 Punkte im materials-Modul, wenn Ventilhahn in Auspuff-Nähe (<300 mm) oder bei Umgebungstemperatur >60°C installiert ist.

(Confidence: documented — DuPont Viton Technical Data, ISO 9094 Brandschutz)

### 7.2 Kegelhahn (Tapered Plug Valve) — Konstruktion und Funktionsprinzip

#### 7.2.1 Aufbau

| Komponente | Funktion | Typischer Werkstoff Marine |
|---|---|---|
| Ventilkörper (Body) | Gehäuse mit konischer Sitzfläche | Bronze C83600 oder C92200 |
| Konus / Küken (Plug) | Konischer Absperrkörper mit Durchgangsbohrung | Bronze, identisch mit Körper |
| Konusfläche (Taper Surface) | Dichtfläche Konus ↔ Körper | Geschliffene Bronze |
| Nachstellmutter (Adjusting Nut) | Presst Konus in Sitzfläche | Bronze oder Edelstahl |
| Griff (Handle) | Betätigung ¼-Drehung + leichtes Anheben | Flügelgriff, T-Griff |
| Kegelfett (Taper Grease) | Schmiert + dichtet Konusfläche | Marineventil-Spezialfett |

**Funktionsprinzip:**
Der konische Konus (Küken) sitzt in einer konischen Bohrung im Ventilkörper. Durch die Nachstellmutter wird der Konus in den Sitz gepresst. Die Dichtung erfolgt Metall-auf-Metall, geschmiert mit Spezialfett. Zum Öffnen/Schließen: leicht am Griff ZIEHEN (Konus aus Sitz lösen), dann 90° DREHEN, dann loslassen (Konus setzt sich wieder). Die Konizität beträgt typisch 1:6 (Blakes) bis 1:8 (Perko).

#### 7.2.2 Vorteile des Kegelhahns

1. **Unendliche Lebensdauer bei Wartung**: Der Konus kann nachgeschliffen werden. Ein gut gewarteter Blakes-Kegelhahn überlebt das Boot.
2. **Voller Durchfluss**: Die Durchgangsbohrung im Konus hat den vollen Nennquerschnitt (immer Full-bore).
3. **Robustheit**: Keine empfindlichen Polymer-Dichtungen. Rein metallische Konstruktion.
4. **Reparierbarkeit auf See**: Konus ausbauen, mit Schleifpaste nachschleifen, einfetten, einsetzen — 30 Minuten Arbeit.
5. **Tradition und Vertrauen**: Seit >100 Jahren bewährt. Hallberg-Rassy, Oyster, Swan setzen auf Kegelhähne.

#### 7.2.3 Nachteile des Kegelhahns

1. **Wartungsintensiv**: Mindestens jährlich fetten, alle 3–5 Jahre nachschleifen. Ohne Wartung → Festsitzen.
2. **Höheres Betätigungsdrehmoment**: Konus muss gegen Reibung + Nachstellkraft gedreht werden.
3. **Fehlbedienungsgefahr**: "Ziehen-Drehen-Loslassen" statt einfachem Drehen. Ungeübte Crews können den Konus blockieren.
4. **Höherer Preis**: Blakes Kegelhahn DN38 ca. 180–250 EUR vs. Kugelhahn gleicher Größe 60–120 EUR.
5. **Weniger Hersteller**: Im Wesentlichen Blakes (UK), Perko (USA), einige italienische Spezialisten.

(Confidence: documented — Blakes Best Practice Guide, Practical Sailor Tests)

#### 7.2.4 Kegelfett — Spezifikation und Anwendung

| Produkt | Hersteller | Basis | Temp.-Bereich | Seewasser-beständig | Preis/Tube |
|---|---|---|---|---|---|
| Blakes Seacock Grease | Blakes | Silikonfrei, mineralisch | -10°C bis +120°C | Ja | 12–18 EUR |
| Perko Plug Cock Grease | Perko | Lithium/Mineral | -15°C bis +100°C | Ja | 10–15 EUR |
| Superlube Marine Grease | Super Lube | Synthetisch (PFPE) | -45°C bis +230°C | Ja | 8–12 EUR |
| Loctite Marine Grease | Henkel | Lithium-Komplex | -20°C bis +130°C | Ja | 10–15 EUR |
| Standard-Bootsfett (Warnung!) | Diverse | Lithium/Kalzium | -20°C bis +100°C | Teilweise | 5–8 EUR |

**WARNUNG**: Normales Bootsfett (Winschenfett, Lagerfett) ist NICHT geeignet für Kegelhähne! Es hat nicht die richtige Konsistenz für Metall-auf-Metall-Dichtung und kann auswaschen. Nur spezifisches Ventilhahn-Fett (Seacock Grease) verwenden.

**Nachschleif-Prozedur (Kegelhahn):**
1. Ventil schließen, Schlauch abklemmen, Wasser ablassen
2. Nachstellmutter lösen (Gegenseite des Griffs)
3. Konus herausziehen
4. Konus und Sitzfläche mit Lappen reinigen
5. Schleifpaste Körnung 120 auf Konus auftragen
6. Konus einsetzen und mit leichtem Druck 20× hin- und herdrehen
7. Reinigen, Zustand prüfen (gleichmäßig matte Oberfläche = gut)
8. Ggf. mit Körnung 400 nachpolieren
9. Kegelfett dünn auftragen
10. Konus einsetzen, Nachstellmutter handfest anziehen
11. Betätigungstest: Konus muss sich mit einer Hand drehen lassen

Dauer: 30–45 Minuten pro Ventil
Material: Schleifpaste ~8 EUR, Kegelfett ~15 EUR
Werkzeug: Schraubenschlüssel, Lappen, Handschuhe

(Confidence: documented — Blakes Maintenance Manual, Perko Service Instructions)

### 7.3 Materialwissenschaft — Ventilhahn-Körper

#### 7.3.1 Bronze-Legierungen im Detail

| Legierung | UNS | Cu % | Sn % | Zn % | Pb % | Ni % | Al % | Bemerkung |
|---|---|---|---|---|---|---|---|---|
| 85-5-5-5 | C83600 | 85 | 5 | 5 | 5 | — | — | Standard Marine, Groco/Guidi |
| 81 Red Brass | C84400 | 81 | 3 | 7 | 9 | — | — | Economy, höherer Zn-Anteil |
| Navy G | C92200 | 88 | 6 | 1,5 | 1,5 | 1 | — | Premium, Blakes/Perko |
| NiAlBr | C95800 | 81 | — | — | — | 4,5 | 9 | Superyacht, höchste Festigkeit |
| Admiralty | C44300 | 71 | 1 | 28 | — | — | — | WARNUNG: 28% Zink! Nur mit As-Inhibitor |

**Dezinkifizierungs-Risiko nach Zinkgehalt:**

| Zn-Gehalt | Risiko | Beispiel | AYDI-Bewertung |
|---|---|---|---|
| 0–5% | Kein Risiko | C83600 (5% Zn), C92200 (1,5% Zn) | ✅ Score 100 (Material) |
| 5–15% | Geringes Risiko | C84400 (7% Zn) | ⚠️ Score 80 (Material) |
| 15–25% | Mittleres Risiko | DZR-Messing (CW602N, ~37% Zn + Inhibitor) | ⚠️ Score 60 (Material) |
| >25% ohne Inhibitor | HOHES Risiko | Yellow Brass C85200 (28% Zn) | ❌ Score 10 (Material) |

**Galvanische Spannungsreihe (Seewasser, 25°C):**

| Material | Potential mV (vs. Ag/AgCl) | Kompatibel mit |
|---|---|---|
| Graphit | +250 | Nichts (extrem edel) |
| Edelstahl 316L (passiv) | +50 bis -100 | Titan, Bronze (bedingt) |
| Bronze C83600 | -230 bis -280 | Bronze, Messing (bedingt) |
| Bronze C92200 | -240 bis -290 | Bronze C83600 |
| DZR-Messing | -300 bis -350 | Bronze (bedingt), kein Alu! |
| Stahl | -600 bis -700 | Opferanode Zink |
| Aluminium | -750 bis -1000 | NICHT mit Bronze! |
| Zink (Anode) | -1000 bis -1050 | Opfert sich für alle edleren |

**AYDI-Regel galvanische Kompatibilität:**
- Potentialdifferenz ≤50 mV: Score-Abzug 0 (kompatibel)
- Potentialdifferenz 50–200 mV: Score-Abzug -5 (bedingt kompatibel, Monitoring)
- Potentialdifferenz 200–500 mV: Score-Abzug -15 (galvanische Korrosion wahrscheinlich)
- Potentialdifferenz >500 mV: Score-Abzug -25 (KRITISCH — aktive galvanische Korrosion)

(Confidence: documented — ASTM B154, MIL-DTL-15345, NACE Corrosion Handbook)

#### 7.3.2 Komposit-Materialien im Detail

| Eigenschaft | Marelon (Forespar) | TruDesign | Guidi Komposit |
|---|---|---|---|
| Matrix | Glasfaserverstärktes Nylon | Glasfaserverstärktes Nylon (PA66-GF30) | Glasfaserverstärktes Polyamid |
| Glasfaseranteil | 30% | 30% | 25–30% |
| Zugfestigkeit | 80 MPa | 90 MPa | 75 MPa |
| Biegefestigkeit | 130 MPa | 140 MPa | 120 MPa |
| Max. Temperatur | +82°C | +93°C | +80°C |
| UV-Beständigkeit | 1.000 h Xenon (ISO 4892-2) | 1.500 h Xenon | 1.000 h Xenon |
| Brandverhalten | UL 94 V-0 | UL 94 V-0 | UL 94 V-0 |
| Kriechfestigkeit (20 J.) | Nachgewiesen (ISO 9093-2) | Nachgewiesen (ISO 9093-2) | Nachgewiesen (ISO 9093-2) |
| FDA/NSF-Zulassung | Ja (Trinkwasser) | Ja (Trinkwasser) | Nein |
| Galvanisch inert | Ja | Ja | Ja |
| Farbe | Weiß | Weiß | Weiß/Schwarz |

**Vorteil Komposit**: Keine galvanische Korrosion. Ideale Lösung für Boote mit Aluminium-Rumpf (wo Bronze-Ventile galvanische Korrosion verursachen) und für Boote mit Landstrom-Elektrolyse-Problemen.

**Nachteil Komposit**: UV-Empfindlichkeit bei Decksmontage, begrenzte Temperaturbeständigkeit (kein Auspuff!), nicht nachschleifbar, nicht schweißbar.

(Confidence: documented — Forespar Technical Data Sheet, TruDesign Engineering Manual)

### 7.4 Grifftypen und Ergonomie

| Grifftyp | Typische Anwendung | Länge mm | Betätigungskraft | Ergonomie-Bewertung |
|---|---|---|---|---|
| Flacher Hebel (Lever) | Kugelhahn Standard | 80–200 | Gering (10–20 Nm) | ★★★★★ — Einhand, auch unter Stress |
| T-Griff | Kugelhahn, manche Kegelhähne | 60–100 | Mittel (15–30 Nm) | ★★★★☆ — Gut, etwas weniger Hebelwirkung |
| Flügelgriff (Wing) | Kegelhahn (Blakes) | 80–150 | Hoch (20–40 Nm) | ★★★☆☆ — Erfordert Ziehen + Drehen |
| Vierkant (Square Head) | Kegelhahn Industrie | n/a | Werkzeug erforderlich | ★★☆☆☆ — Werkzeug im Notfall finden? |
| Elektrischer Antrieb | Fernbetätigung | n/a | Motorisiert | ★★★★★ (Fern) / ★★★☆☆ (Notfall-Hand) |

**ABYC H-27 Mindest-Grifflängen:**

| Nennweite DN | Min. Grifflänge mm | Begründung |
|---|---|---|
| DN15 (½") | 80 | Einhand-Bedienung |
| DN20 (¾") | 100 | Einhand-Bedienung |
| DN25 (1") | 100 | Einhand-Bedienung |
| DN32 (1¼") | 120 | Einhand, auch mit nassen Händen |
| DN38 (1½") | 150 | Ausreichend Hebelwirkung |
| DN50 (2") | 200 | Höheres Drehmoment erforderlich |

**AYDI Ergonomie-Scoring:**
- Grifflänge ≥ ABYC-Minimum: Score 100
- Grifflänge 80–99% des Minimums: Score 70
- Grifflänge <80% des Minimums: Score 40
- Kein Griff / abgebrochen: Score 0 (KRITISCH)

(Confidence: documented — ABYC H-27:2021, ISO 9093:2020 §5.3.4)

### 7.5 Y-Ventile (Umschaltventile)

#### 7.5.1 Funktionsprinzip

Ein Y-Ventil (Three-Way Valve) ist ein Seeventilhahn mit drei Anschlüssen, der den Durchfluss zwischen zwei Ausgängen umschaltet. Primäre Anwendung: WC-System (Umschaltung Abwasser → See / Abwasser → Holding Tank).

| Stellung | Durchfluss | Anwendung |
|---|---|---|
| Position A | Eingang → Ausgang A | Abwasser direkt ins Meer (offshore, erlaubt) |
| Position B | Eingang → Ausgang B | Abwasser in Holding Tank (Hafen/Küste, vorgeschrieben) |
| Position C (geschlossen) | Alle Ports geschlossen | Absperrung (nicht bei allen Y-Ventilen!) |

**WARNUNG MARPOL / Umweltrecht:**
- Innerhalb von 3 Seemeilen von der Küste (EU): Abwasser MUSS in Holding Tank
- Innerhalb von 12 Seemeilen (viele Länder): dto.
- Mittelmeer: Generelles Einleitungsverbot in vielen Küstengewässern
- Ostsee: Ab 2025 generelles Einleitungsverbot (HELCOM)
- Y-Ventil muss in Hafenstellung gesichert werden können (Plombe/Siegel)

#### 7.5.2 Y-Ventil-Hersteller und Modelle

| Hersteller | Modell | Material | Nennweite | Preis EUR | Anmerkung |
|---|---|---|---|---|---|
| Groco | HF-Serie | Bronze C83600 | DN25–DN50 | 180–420 | Premium, Full-bore |
| Blakes | Three-Way Plug | Bronze C83600 | DN25–DN38 | 220–350 | Kegelhahn-Prinzip |
| Forespar | Marelon Y-Valve | Komposit Marelon | DN25–DN38 | 120–190 | Korrosionsfrei |
| TruDesign | 90346/90347 | Komposit PA66-GF30 | DN25–DN38 | 95–160 | Preis-Leistung |
| Vetus | Y-Serie | Bronze/Komposit | DN25–DN38 | 110–250 | Europa-verfügbar |
| Raritan |?"3WY" | Bronze C83600 | DN25–DN38 | 160–280 | USA-Standard |

(Confidence: documented — Hersteller-Kataloge 2025/26)

### 7.6 Dimensionierung — Nennweiten und Anwendungsbereiche

| Anwendung | Empfohlene DN mm | Empfohlene DN Zoll | Begründung |
|---|---|---|---|
| Waschbecken-Abfluss | DN15–DN20 | ½"–¾" | Geringer Durchfluss |
| Dusche-Abfluss | DN20–DN25 | ¾"–1" | Mittlerer Durchfluss |
| Toilette Einlass | DN20–DN25 | ¾"–1" | Standard WC-Pumpe |
| Toilette Auslass | DN25–DN38 | 1"–1½" | Feststoff-führend! |
| Pantry-Abfluss | DN20–DN25 | ¾"–1" | Geringer Durchfluss |
| Bilgenpumpe Auslass | DN25–DN38 | 1"–1½" | Hoher Durchfluss im Notfall |
| Kühlwasser Motor <50 PS | DN20–DN25 | ¾"–1" | Herstellerangabe beachten |
| Kühlwasser Motor 50–150 PS | DN25–DN38 | 1"–1½" | Herstellerangabe beachten |
| Kühlwasser Motor >150 PS | DN38–DN50 | 1½"–2" | Herstellerangabe beachten |
| Auspuff Nassauspuff | DN38–DN50 | 1½"–2" | Abgasvolumen + Kühlwasser |
| Klimaanlage (AC) | DN25–DN50 | 1"–2" | Je nach BTU-Leistung |
| Generator Kühlung | DN25–DN38 | 1"–1½" | Herstellerangabe beachten |
| Wassermacher Einlass | DN20–DN25 | ¾"–1" | Niederdruck-Seite |
| Ankerspülung | DN20–DN25 | ¾"–1" | Mittlerer Durchfluss |
| Feuerlöschanlage | DN38–DN50 | 1½"–2" | Hoher Durchfluss kritisch |

**Dimensionierungs-Regel (Kühlwasser):**
Motorhersteller geben den erforderlichen Kühlwasserdurchfluss in l/min an. Der Ventilhahn darf diesen Durchfluss nicht einschränken.

```
Faustformel: Q [l/min] ≈ Motorleistung [kW] × 0,5–0,8
DN [mm] = √(Q × 4 / (π × v × 60)) × 1000
  wobei v = 1,5 m/s (empfohlene Strömungsgeschwindigkeit für Seewasser)

Beispiel: 50 kW Motor
  Q = 50 × 0,65 = 32,5 l/min
  DN = √(32,5 × 4 / (3,14159 × 1,5 × 60)) × 1000 = √(130 / 282,7) × 1000 = 21,4 mm → DN25
```

**AYDI-Regel**: Ventilhahn-Nennweite muss ≥ der berechneten DN sein. Bei Reduced-bore den tatsächlichen Bore-∅ verwenden!

(Confidence: calculated — Strömungsmechanik, Motorhersteller-Handbücher)

---

## 8. Hersteller — Vollständige Übersicht

### 8.1 Groco (USA) — Gross Mechanical Corporation

**Firmenprofil:**
- Gründung: 1923, Baltimore, Maryland, USA
- Spezialgebiet: Marine-Armaturen, Seeventile, Borddurchlässe
- Vertrieb: Weltweit über Marine-Fachhändler, Hauptmarkt USA
- Qualitätsstandard: ISO 9093, ABYC H-27, UL-gelistet
- Werkstoff-Standard: Bronze C83600 (85-5-5-5)
- Alle Groco-Seeventile: NPT-Gewinde (USA-Standard!)

#### 8.1.1 BV-Serie — Ball Valve (Kugelhahn)

Die BV-Serie ist Grocos Standard-Kugelhahn für Seeventile:

| Modell | Nennweite | Bore | Kugel | Dichtung | Kv m³/h | Preis EUR |
|---|---|---|---|---|---|---|
| BV-0500 | DN15 (½" NPT) | Full-bore | 316L | PTFE | 6,5 | 85 |
| BV-0750 | DN20 (¾" NPT) | Full-bore | 316L | PTFE | 12,0 | 95 |
| BV-1000 | DN25 (1" NPT) | Full-bore | 316L | PTFE | 22,0 | 110 |
| BV-1250 | DN32 (1¼" NPT) | Full-bore | 316L | PTFE | 35,0 | 140 |
| BV-1500 | DN38 (1½" NPT) | Full-bore | 316L | PTFE | 52,0 | 170 |
| BV-2000 | DN50 (2" NPT) | Full-bore | 316L | PTFE | 85,0 | 250 |
| BV-2500 | DN63 (2½" NPT) | Full-bore | 316L | PTFE | 130,0 | 380 |
| BV-3000 | DN75 (3" NPT) | Full-bore | 316L | PTFE | 180,0 | 520 |

**Technische Details BV-Serie:**
- Körper: Bronze C83600, Sandguss, bearbeitet
- Kugel: Edelstahl 316L, poliert Ra ≤ 0,4 µm
- Sitzringe: PTFE glasfaserverstärkt
- Spindel: Edelstahl 316, O-Ring-Dichtung PTFE
- Griff: Flacher Hebel, Edelstahl 316, Gewindestift gesichert
- Druckklasse: 200 PSI (13,8 bar) CWP (Cold Working Pressure)
- Temperaturbereich: -20°C bis +93°C
- Zyklentest: 1.000 Zyklen (über ISO 9093 hinaus)
- Gewinde: NPT (ACHTUNG: nicht direkt mit BSP kompatibel!)

(Confidence: documented — Groco Katalog 2025, Datenblatt BV-Serie)

#### 8.1.2 HF-Serie — Hose-to-Flange Ball Valve

Die HF-Serie kombiniert Kugelhahn mit Schlauchtülle:

| Modell | Nennweite | Schlauchtülle-∅ mm | Bore | Preis EUR |
|---|---|---|---|---|
| HF-500 | DN15 (½" NPT) | 16 | Full-bore | 110 |
| HF-750 | DN20 (¾" NPT) | 19 | Full-bore | 125 |
| HF-1000 | DN25 (1" NPT) | 25 | Full-bore | 145 |
| HF-1250 | DN32 (1¼" NPT) | 32 | Full-bore | 175 |
| HF-1500 | DN38 (1½" NPT) | 38 | Full-bore | 210 |
| HF-2000 | DN50 (2" NPT) | 50 | Full-bore | 310 |

**Vorteil HF-Serie**: Kein separater Schlauchadapter nötig. Weniger Verbindungsstellen = weniger Leckagepunkte.

(Confidence: documented — Groco Katalog 2025)

#### 8.1.3 IBV-Serie — In-Line Ball Valve

Inline-Kugelhahn für Rohrleitungen (nicht direkt als Seeventil, sondern als Absperrhahn in der Verrohrung):

| Modell | Nennweite | Bore | Preis EUR |
|---|---|---|---|
| IBV-500 | DN15 (½" NPT) | Full-bore | 65 |
| IBV-750 | DN20 (¾" NPT) | Full-bore | 75 |
| IBV-1000 | DN25 (1" NPT) | Full-bore | 90 |
| IBV-1250 | DN32 (1¼" NPT) | Full-bore | 115 |
| IBV-1500 | DN38 (1½" NPT) | Full-bore | 145 |
| IBV-2000 | DN50 (2" NPT) | Full-bore | 210 |

**WARNUNG**: Die IBV-Serie ist KEIN Seeventil! Sie ist als Absperrhahn in der Leitung konzipiert und nicht für den Einbau am Borddurchlass zugelassen. Kein Flansch, kein Backing-Plate-Anschluss.

(Confidence: documented — Groco Katalog 2025, Groco Application Guide)

### 8.2 Blakes (UK) — Blakes Lavac Taylors

**Firmenprofil:**
- Gründung: ~1890, Gosport, Hampshire, UK
- Spezialgebiet: Kegelhähne (Tapered Plug Valves), WC-Systeme (Lavac)
- Vertrieb: UK, Europa, Australien
- Qualitätsstandard: ISO 9093, BSI, Lloyd's Register zugelassen
- Werkstoff-Standard: Bronze C83600 (Körper), C92200 (Premium-Linie)
- Gewinde: BSP (ISO 228) — Europa-Standard!

#### 8.2.1 Blakes Tapered Plug Seacock — Standardlinie

Der Blakes-Kegelhahn ist der Goldstandard für traditionelle Seeventile:

| Modell | Nennweite | Konuswinkel | Körper | Konusumaterial | Preis EUR |
|---|---|---|---|---|---|
| Blakes BB ½" | DN15 (½" BSP) | 1:6 | C83600 | C83600 | 120 |
| Blakes BB ¾" | DN20 (¾" BSP) | 1:6 | C83600 | C83600 | 140 |
| Blakes BB 1" | DN25 (1" BSP) | 1:6 | C83600 | C83600 | 165 |
| Blakes BB 1¼" | DN32 (1¼" BSP) | 1:6 | C83600 | C83600 | 195 |
| Blakes BB 1½" | DN38 (1½" BSP) | 1:6 | C83600 | C83600 | 240 |
| Blakes BB 2" | DN50 (2" BSP) | 1:6 | C83600 | C83600 | 340 |

**Technische Details Blakes Tapered Plug:**
- Körper: Bronze C83600 Kokillenguss (höhere Dichte als Sandguss)
- Konus (Küken): Bronze C83600, Oberfläche geschliffen Ra ≤ 0,4 µm
- Konuswinkel: 1:6 (10° Halbwinkel) — optimaler Kompromiss Dichtheit/Betätigungskraft
- Dichtprinzip: Metall-auf-Metall + Kegelfett
- Nachstellmutter: Bronze, metrisches Gewinde
- Griff: Flügelgriff Bronze
- Nachschleif-Reserve: 3–4 mm (30–50 Jahre Lebensdauer bei korrekter Wartung)
- Druckklasse: PN16 (16 bar)
- Temperaturbereich: -20°C bis +120°C (Metallkonstruktion!)
- Zyklentest: Unbegrenzt (Metall-auf-Metall unterliegt keinem Polymerabbau)
- Gewinde: BSP parallel (ISO 228)

(Confidence: documented — Blakes Technical Manual, Blakes Heritage Documentation)

#### 8.2.2 Blakes Lever Seacock — Kugelhahn-Linie

Blakes bietet auch Kugelhähne für Kunden, die wartungsfreie Bedienung bevorzugen:

| Modell | Nennweite | Bore | Kugel | Dichtung | Preis EUR |
|---|---|---|---|---|---|
| Blakes Lever ½" | DN15 (½" BSP) | Full-bore | 316L | PTFE | 85 |
| Blakes Lever ¾" | DN20 (¾" BSP) | Full-bore | 316L | PTFE | 95 |
| Blakes Lever 1" | DN25 (1" BSP) | Full-bore | 316L | PTFE | 115 |
| Blakes Lever 1¼" | DN32 (1¼" BSP) | Full-bore | 316L | PTFE | 145 |
| Blakes Lever 1½" | DN38 (1½" BSP) | Full-bore | 316L | PTFE | 180 |
| Blakes Lever 2" | DN50 (2" BSP) | Full-bore | 316L | PTFE | 270 |

(Confidence: documented — Blakes Katalog 2025)

### 8.3 Guidi (Italien) — Guidi S.r.l.

**Firmenprofil:**
- Gründung: 1968, Poggibonsi (Siena), Italien
- Spezialgebiet: Marine-Armaturen, Borddurchlässe, Seeventile
- Vertrieb: Weltweit, OEM-Lieferant für Beneteau, Jeanneau, Dufour, Azimut, Bavaria
- Qualitätsstandard: ISO 9093, RINA-zugelassen
- Werkstoff-Standard: Bronze C83600 (2060-Serie), DZR-Messing (2062-Serie)
- Gewinde: BSP (ISO 228)

#### 8.3.1 Guidi 2060-Serie — Bronze Kugelhahn

Premium-Linie für Werft- und Nachrüstungsmarkt:

| Modell | Nennweite | Bore | Kugel | Dichtung | RINA | Preis EUR |
|---|---|---|---|---|---|---|
| 2060 ½" | DN15 (½" BSP) | Full-bore | Cr-Messing | PTFE | Ja | 55 |
| 2060 ¾" | DN20 (¾" BSP) | Full-bore | Cr-Messing | PTFE | Ja | 65 |
| 2060 1" | DN25 (1" BSP) | Full-bore | Cr-Messing | PTFE | Ja | 80 |
| 2060 1¼" | DN32 (1¼" BSP) | Full-bore | Cr-Messing | PTFE | Ja | 100 |
| 2060 1½" | DN38 (1½" BSP) | Full-bore | Cr-Messing | PTFE | Ja | 130 |
| 2060 2" | DN50 (2" BSP) | Full-bore | Cr-Messing | PTFE | Ja | 195 |

#### 8.3.2 Guidi 2062-Serie — DZR-Messing Kugelhahn

Economy-Linie, OEM-Standard für europäische Serienwerften:

| Modell | Nennweite | Bore | Kugel | Dichtung | Preis EUR |
|---|---|---|---|---|---|
| 2062 ½" | DN15 (½" BSP) | Reduced-bore | Cr-Messing | PTFE | 28 |
| 2062 ¾" | DN20 (¾" BSP) | Reduced-bore | Cr-Messing | PTFE | 32 |
| 2062 1" | DN25 (1" BSP) | Reduced-bore | Cr-Messing | PTFE | 40 |
| 2062 1¼" | DN32 (1¼" BSP) | Reduced-bore | Cr-Messing | PTFE | 52 |
| 2062 1½" | DN38 (1½" BSP) | Reduced-bore | Cr-Messing | PTFE | 68 |
| 2062 2" | DN50 (2" BSP) | Reduced-bore | Cr-Messing | PTFE | 95 |

**AYDI-WARNUNG Guidi 2062:**
Die Guidi 2062-Serie ist DZR-Messing, NICHT Bronze! DZR-Messing hat einen signifikant höheren Zinkgehalt (~37% vs. 5%) und ist dezinkifizierungsgefährdet, obwohl der Arsen-Inhibitor das Risiko reduziert. Bei Booten >12 Jahre mit Guidi 2062: Dezinkifizierungs-Test empfehlen! Score-Abzug -3 im materials-Modul gegenüber Bronze.

(Confidence: documented — Guidi Katalog 2025, Guidi Technical Data Sheets)

#### 8.3.3 Guidi Komposit-Linie

| Modell | Nennweite | Material | Bore | Preis EUR |
|---|---|---|---|---|
| Guidi 1166 ½" | DN15 | Glasfaserverstärktes PA | Full-bore | 22 |
| Guidi 1166 ¾" | DN20 | Glasfaserverstärktes PA | Full-bore | 26 |
| Guidi 1166 1" | DN25 | Glasfaserverstärktes PA | Full-bore | 35 |
| Guidi 1166 1¼" | DN32 | Glasfaserverstärktes PA | Full-bore | 48 |
| Guidi 1166 1½" | DN38 | Glasfaserverstärktes PA | Full-bore | 60 |

(Confidence: documented — Guidi Katalog 2025)

### 8.4 TruDesign (Neuseeland)

**Firmenprofil:**
- Gründung: 2003, Tauranga, Neuseeland
- Spezialgebiet: Komposit-Seeventile und Borddurchlässe
- Vertrieb: Weltweit, OEM-Lieferant für Bavaria, Hanse, Dufour (neuere Modelle)
- Qualitätsstandard: ISO 9093-2:2020, ABYC H-27, UL-gelistet
- Werkstoff: Glasfaserverstärktes Polyamid (PA66-GF30)
- Gewinde: BSP (ISO 228) — Standard-Linie; NPT-Versionen verfügbar

#### 8.4.1 TruDesign 90300-Serie — Kugelhahn Komposit

Die 90300-Serie ist TruDesigns Hauptproduktlinie für Seeventilhähne:

| Modell | Nennweite | Bore | Kugel | Dichtung | Max. °C | Preis EUR |
|---|---|---|---|---|---|---|
| 90300 | DN15 (½" BSP) | Full-bore | Komposit | PTFE | 93°C | 35 |
| 90301 | DN20 (¾" BSP) | Full-bore | Komposit | PTFE | 93°C | 42 |
| 90302 | DN25 (1" BSP) | Full-bore | Komposit | PTFE | 93°C | 52 |
| 90303 | DN32 (1¼" BSP) | Full-bore | Komposit | PTFE | 93°C | 68 |
| 90305 | DN38 (1½" BSP) | Full-bore | Komposit | PTFE | 93°C | 85 |
| 90307 | DN50 (2" BSP) | Full-bore | Komposit | PTFE | 93°C | 125 |

**Technische Details TruDesign 90300-Serie:**
- Körper: PA66-GF30 (Polyamid 66 + 30% Glasfaser), spritzgegossen
- Kugel: Komposit mit PTFE-Beschichtung
- Sitzringe: PTFE
- Spindel: Edelstahl 316
- Griff: PA-Kunststoff, verstärkt
- Druckklasse: 150 PSI (10,3 bar) @ 23°C, 75 PSI (5,2 bar) @ 82°C
- Temperaturbereich: -30°C bis +93°C
- UV-Beständigkeit: 1.500 h Xenon-Test (ISO 4892-2)
- Brandverhalten: UL 94 V-0
- FDA/NSF-zugelassen (Trinkwasser)
- Galvanisch vollständig inert
- Zyklentest: 2.000 Zyklen

**TruDesign-Vorteil**: Das einzige vollständig korrosionsfreie Seeventilhahn-System. Ideal für:
- Alu-Rumpf-Boote (keine galvanische Korrosion)
- Boote mit Landstrom-Elektrolyse-Problemen
- Charter-Boote (wartungsarm)
- Langfahrt in tropischen Revieren (kein Bewuchs am Ventilkörper)

**TruDesign-Einschränkung**: NICHT geeignet für Auspuff-Nähe (max. 93°C) oder Feuer-Löschanlagen (Brandverhalten zwar V-0, aber Schmelzpunkt bei ~260°C).

(Confidence: documented — TruDesign Engineering Manual 2025, TruDesign ISO 9093-2 Zertifikat)

#### 8.4.2 TruDesign Y-Valve Serie

| Modell | Nennweite | Anschlüsse | Bore | Preis EUR |
|---|---|---|---|---|
| 90346 | DN25 (1" BSP) | 3-Wege | Full-bore | 95 |
| 90347 | DN38 (1½" BSP) | 3-Wege | Full-bore | 140 |

(Confidence: documented — TruDesign Katalog 2025)

### 8.5 Forespar Marelon (USA)

**Firmenprofil:**
- Gründung: 1967, San Clemente, Kalifornien, USA
- Spezialgebiet: Komposit-Marine-Armaturen, Rigging-Zubehör
- Markenname: "Marelon" — glasfaserverstärkte Nylon-Kompound (glasfaserverstärktes Polyamid)
- Vertrieb: Überwiegend USA, begrenzt international
- Qualitätsstandard: ISO 9093-2, ABYC H-27, UL-gelistet, FDA/NSF
- Gewinde: NPT (USA-Standard!)

#### 8.5.1 Forespar Marelon Ball Valve

| Modell | Nennweite | Bore | Max. °C | Preis EUR |
|---|---|---|---|---|
| MV050 | DN15 (½" NPT) | Full-bore | 82°C | 40 |
| MV075 | DN20 (¾" NPT) | Full-bore | 82°C | 48 |
| MV100 | DN25 (1" NPT) | Full-bore | 82°C | 58 |
| MV125 | DN32 (1¼" NPT) | Full-bore | 82°C | 72 |
| MV150 | DN38 (1½" NPT) | Full-bore | 82°C | 90 |
| MV200 | DN50 (2" NPT) | Full-bore | 82°C | 135 |

**Technische Details Marelon:**
- Körper: Glasfaserverstärktes Nylon ("Marelon"), Spritzguss
- Kugel: Marelon mit PTFE-Beschichtung
- Sitzringe: PTFE
- Spindel: Edelstahl 316
- Druckklasse: 200 PSI (13,8 bar) @ 23°C
- UV-Beständigkeit: 1.000 h Xenon
- FDA/NSF-61-zugelassen
- Galvanisch inert

**Besonderheit Marelon**: Forespar war der Pionier der Komposit-Seeventile (1980er). Marelon ist über 40 Jahre erprobt und die Langzeiterfahrung (insbesondere in den USA, wo Catalina und Hunter Marelon als OEM verwenden) ist exzellent.

**Einschränkung**: Marelon hat die niedrigste Temperaturgrenze aller Komposit-Hähne (82°C vs. 93°C TruDesign). Nicht für Maschinenraum-nahe Installationen mit hoher Umgebungstemperatur.

(Confidence: documented — Forespar Katalog 2025, Forespar Technical Bulletin TB-017)

### 8.6 Apollo (USA) — Apollo Valves / Conbraco

**Firmenprofil:**
- Gründung: 1928, Matthews, North Carolina, USA
- Spezialgebiet: Industrieventile, Bronze-Kugelhähne
- Marine-Relevanz: Apollo 70-100 und 5500-Serie werden als Marine-Kugelhähne eingesetzt
- Qualitätsstandard: ABYC-kompatibel (nicht explizit marinespezifisch)
- Werkstoff: Bronze C83600 (70-Serie), C89835 Low-Lead (5500-Serie)

#### 8.6.1 Apollo 70-100 Serie — Bronze Ball Valve

| Modell | Nennweite | Bore | Kugel | Dichtung | Preis EUR |
|---|---|---|---|---|---|
| 70-101 | DN15 (½" NPT) | Full-bore | 316L | PTFE | 45 |
| 70-103 | DN20 (¾" NPT) | Full-bore | 316L | PTFE | 55 |
| 70-105 | DN25 (1" NPT) | Full-bore | 316L | PTFE | 65 |
| 70-107 | DN32 (1¼" NPT) | Full-bore | 316L | PTFE | 85 |
| 70-108 | DN38 (1½" NPT) | Full-bore | 316L | PTFE | 110 |
| 70-109 | DN50 (2" NPT) | Full-bore | 316L | PTFE | 165 |

**Technische Details Apollo 70-100:**
- Körper: Bronze C83600
- Kugel: Edelstahl 316L, poliert
- Druckklasse: 600 WOG (41,4 bar) — deutlich höher als für Marine nötig
- Temperaturbereich: -29°C bis +177°C (mit PTFE)
- Zyklentest: Industriestandard (>5.000 Zyklen)

**AYDI-Hinweis Apollo**: Apollo-Ventile sind robuste Industrieprodukte, die marine-tauglich sind, aber NICHT spezifisch als Seeventile zugelassen. Sie haben keinen Flansch für Borddurchlass-Montage. Einsatz als Inline-Absperrhahn: empfehlenswert. Einsatz als Seeventil am Borddurchlass: nur mit geeignetem Adapter.

#### 8.6.2 Apollo 5500-Serie — Lead-Free Bronze

| Modell | Nennweite | Bore | Kugel | Preis EUR | Anmerkung |
|---|---|---|---|---|---|
| 5500 ½" | DN15 (½" NPT) | Full-bore | 316L | 55 | Bleifrei (NSF 61) |
| 5500 ¾" | DN20 (¾" NPT) | Full-bore | 316L | 68 | Bleifrei (NSF 61) |
| 5500 1" | DN25 (1" NPT) | Full-bore | 316L | 82 | Bleifrei (NSF 61) |
| 5500 1¼" | DN32 (1¼" NPT) | Full-bore | 316L | 105 | Bleifrei (NSF 61) |
| 5500 1½" | DN38 (1½" NPT) | Full-bore | 316L | 135 | Bleifrei (NSF 61) |
| 5500 2" | DN50 (2" NPT) | Full-bore | 316L | 195 | Bleifrei (NSF 61) |

**Hinweis 5500-Serie**: Die bleifreie Legierung C89835 hat eine geringfügig andere Korrosionsbeständigkeit als C83600. Langzeiterfahrung im Marine-Bereich ist begrenzt (NSF-61-Zulassung für Trinkwasser, nicht spezifisch für Seewasser).

(Confidence: documented — Apollo Katalog 2025, Apollo Technical Bulletin)

### 8.7 Nibco (USA) — Northern Indiana Brass Company

**Firmenprofil:**
- Gründung: 1904, Elkhart, Indiana, USA
- Spezialgebiet: Industrie- und Gebäudeventile, Bronze + Kupfer
- Marine-Relevanz: Nibco Bronze-Kugelhähne als Alternative zu Groco in US-Werften
- Qualitätsstandard: Industriestandard, nicht marine-spezifisch
- Werkstoff: Bronze, DZR-Messing

#### 8.7.1 Nibco T-580-70 Serie — Bronze Ball Valve

| Modell | Nennweite | Bore | Kugel | Preis EUR |
|---|---|---|---|---|
| T-580-70 ½" | DN15 (½" NPT) | Reduced-bore | Cr-Messing | 30 |
| T-580-70 ¾" | DN20 (¾" NPT) | Reduced-bore | Cr-Messing | 38 |
| T-580-70 1" | DN25 (1" NPT) | Reduced-bore | Cr-Messing | 48 |
| T-580-70 1¼" | DN32 (1¼" NPT) | Reduced-bore | Cr-Messing | 65 |
| T-580-70 1½" | DN38 (1½" NPT) | Reduced-bore | Cr-Messing | 85 |
| T-580-70 2" | DN50 (2" NPT) | Reduced-bore | Cr-Messing | 120 |

**AYDI-WARNUNG Nibco**: Die T-580-70 Serie hat eine verchromte Messing-Kugel (NICHT Edelstahl 316L) und ist Reduced-bore. Für marine-kritische Anwendungen (Kühlwasser, Seeventil) ist die Groco BV-Serie oder Apollo 70-100 bevorzugt. Nibco ist ein Kompromiss für nicht-kritische Anwendungen (Abflüsse über Wasserlinie).

(Confidence: documented — Nibco Product Catalog 2025)

### 8.8 Perko (USA) — Perko Inc.

**Firmenprofil:**
- Gründung: 1907, Miami, Florida, USA
- Spezialgebiet: Marine-Beleuchtung, Borddurchlässe, Kegelhähne
- Vertrieb: USA, begrenzt international
- Qualitätsstandard: ABYC, UL, USCG-zugelassen
- Werkstoff: Bronze C83600 (Kegelhähne), C84400 (Economy)

#### 8.8.1 Perko Tapered Plug Seacock

Perkos Kegelhähne sind das amerikanische Pendant zu Blakes:

| Modell | Nennweite | Konuswinkel | Material | Preis EUR |
|---|---|---|---|---|
| Perko 0732 ½" | DN15 (½" NPT) | 1:8 | C83600 | 95 |
| Perko 0732 ¾" | DN20 (¾" NPT) | 1:8 | C83600 | 115 |
| Perko 0732 1" | DN25 (1" NPT) | 1:8 | C83600 | 140 |
| Perko 0732 1¼" | DN32 (1¼" NPT) | 1:8 | C83600 | 170 |
| Perko 0732 1½" | DN38 (1½" NPT) | 1:8 | C83600 | 220 |
| Perko 0732 2" | DN50 (2" NPT) | 1:8 | C83600 | 310 |

**Vergleich Perko vs. Blakes Kegelhahn:**

| Eigenschaft | Perko 0732 | Blakes BB |
|---|---|---|
| Konuswinkel | 1:8 (flacher) | 1:6 (steiler) |
| Betätigungskraft | Leichter (flacherer Konus) | Schwerer |
| Dichtheit | Gut (mehr Kontaktfläche) | Sehr gut |
| Nachschleif-Reserve | 2–3 mm | 3–4 mm |
| Gewinde | NPT | BSP |
| Preis (DN38) | ~220 EUR | ~240 EUR |
| Verfügbarkeit Europa | Gering | Gut |

(Confidence: documented — Perko Catalog 2025, Practical Sailor Vergleichstest)

### 8.9 Buck Algonquin (USA)

**Firmenprofil:**
- Teil der R&G Sloane Manufacturing, Allentown, PA, USA
- Spezialgebiet: Marine-Kugelhähne, Borddurchlässe, Wellenbock-Armaturen
- Vertrieb: USA, industrieller Marine-Sektor
- Werkstoff: Bronze C83600

#### 8.9.1 Buck Algonquin Ball Valve

| Modell | Nennweite | Bore | Kugel | Preis EUR |
|---|---|---|---|---|
| BA-FBV050 | DN15 (½" NPT) | Full-bore | 316L | 60 |
| BA-FBV075 | DN20 (¾" NPT) | Full-bore | 316L | 72 |
| BA-FBV100 | DN25 (1" NPT) | Full-bore | 316L | 88 |
| BA-FBV125 | DN32 (1¼" NPT) | Full-bore | 316L | 115 |
| BA-FBV150 | DN38 (1½" NPT) | Full-bore | 316L | 150 |
| BA-FBV200 | DN50 (2" NPT) | Full-bore | 316L | 225 |

**Technische Details:**
- Körper: Bronze C83600, Investment Cast
- Druckklasse: 200 PSI WOG
- Gewinde: NPT
- Blowout-proof stem design

**AYDI-Hinweis**: Buck Algonquin ist weniger bekannt als Groco, bietet aber vergleichbare Qualität zu etwas niedrigerem Preis. In Europa schwer erhältlich (Defender Industries, USA-Import).

(Confidence: documented — Buck Algonquin Katalog 2025, Defender Industries Listings)

### 8.10 Vetus (Niederlande)

**Firmenprofil:**
- Gründung: 1928, Schiedam, Niederlande
- Spezialgebiet: Marine-Systeme (Motoren, Auspuff, Borddurchlässe, Armaturen)
- Vertrieb: Weltweit, starke Präsenz Europa
- Qualitätsstandard: ISO 9093, CE, Lloyd's Register
- Werkstoff: Bronze (Ventilhähne), Komposit (Borddurchlässe)

#### 8.10.1 Vetus Bronze Ball Valve

| Modell | Nennweite | Bore | Kugel | Dichtung | Preis EUR |
|---|---|---|---|---|---|
| KRAAN ½" | DN15 (½" BSP) | Full-bore | Cr-Messing | PTFE | 48 |
| KRAAN ¾" | DN20 (¾" BSP) | Full-bore | Cr-Messing | PTFE | 55 |
| KRAAN 1" | DN25 (1" BSP) | Full-bore | Cr-Messing | PTFE | 68 |
| KRAAN 1¼" | DN32 (1¼" BSP) | Full-bore | Cr-Messing | PTFE | 88 |
| KRAAN 1½" | DN38 (1½" BSP) | Full-bore | Cr-Messing | PTFE | 115 |
| KRAAN 2" | DN50 (2" BSP) | Full-bore | Cr-Messing | PTFE | 175 |

**Technische Details Vetus KRAAN:**
- Körper: Bronze C83600
- Kugel: Verchromtes Messing (NICHT 316L — Kosteneinsparung)
- Sitzringe: PTFE
- Griff: Edelstahl-Hebel
- Druckklasse: PN16
- Gewinde: BSP (ISO 228)

**AYDI-Hinweis Vetus**: Gutes Preis-Leistungs-Verhältnis, aber die verchromte Messing-Kugel ist der Schwachpunkt gegenüber Groco/Blakes mit 316L-Kugel. In Salzwasser kann die Chromschicht nach 10–15 Jahren versagen → Kugel korrodiert. Score-Abzug -2 im materials-Modul gegenüber 316L-Kugel.

#### 8.10.2 Vetus E-Valve — Elektrisch betätigt

| Modell | Nennweite | Spannung | Betätigungszeit | Preis EUR |
|---|---|---|---|---|
| EV1210 | DN25 (1" BSP) | 12V DC | 8 s | 480 |
| EV1510 | DN38 (1½" BSP) | 12V DC | 10 s | 620 |
| EV2010 | DN50 (2" BSP) | 12V DC | 12 s | 920 |
| EV1224 | DN25 (1" BSP) | 24V DC | 8 s | 510 |
| EV1524 | DN38 (1½" BSP) | 24V DC | 10 s | 660 |
| EV2024 | DN50 (2" BSP) | 24V DC | 12 s | 980 |

**Technische Details E-Valve:**
- Körper: Bronze C83600
- Antrieb: Gleichstrom-Motor mit Getriebe
- Steuerung: NMEA 2000 (PGN 127501) oder Relais-Ansteuerung
- Notfall: Vierkant-Handbetätigung
- Positionssensor: Open/Close-Rückmeldung
- Schutzklasse: IP67

(Confidence: documented — Vetus Katalog 2025/26, Vetus Technical Manual)

### 8.11 Osculati (Italien)

**Firmenprofil:**
- Gründung: 1958, Segrate (Mailand), Italien
- Spezialgebiet: Marine-Zubehör (Vollsortiment), inkl. Seeventile
- Vertrieb: Weltweit, Katalog mit >20.000 Artikeln
- Qualitätsstandard: ISO 9093, CE
- Werkstoff: Bronze, DZR-Messing, Edelstahl

#### 8.11.1 Osculati Bronze Kugelhahn

| Modell | Nennweite | Bore | Kugel | Dichtung | Preis EUR |
|---|---|---|---|---|---|
| 17.319.01 | DN15 (½" BSP) | Full-bore | Cr-Messing | PTFE | 38 |
| 17.319.02 | DN20 (¾" BSP) | Full-bore | Cr-Messing | PTFE | 45 |
| 17.319.03 | DN25 (1" BSP) | Full-bore | Cr-Messing | PTFE | 58 |
| 17.319.04 | DN32 (1¼" BSP) | Full-bore | Cr-Messing | PTFE | 75 |
| 17.319.05 | DN38 (1½" BSP) | Full-bore | Cr-Messing | PTFE | 95 |
| 17.319.06 | DN50 (2" BSP) | Full-bore | Cr-Messing | PTFE | 145 |

#### 8.11.2 Osculati DZR-Messing Kugelhahn (Economy)

| Modell | Nennweite | Bore | Kugel | Preis EUR |
|---|---|---|---|---|
| 17.318.01 | DN15 (½" BSP) | Reduced-bore | Cr-Messing | 18 |
| 17.318.02 | DN20 (¾" BSP) | Reduced-bore | Cr-Messing | 22 |
| 17.318.03 | DN25 (1" BSP) | Reduced-bore | Cr-Messing | 28 |
| 17.318.04 | DN32 (1¼" BSP) | Reduced-bore | Cr-Messing | 38 |
| 17.318.05 | DN38 (1½" BSP) | Reduced-bore | Cr-Messing | 50 |
| 17.318.06 | DN50 (2" BSP) | Reduced-bore | Cr-Messing | 72 |

**AYDI-WARNUNG Osculati DZR**: Identische Warnung wie bei Guidi 2062 — DZR-Messing ist dezinkifizierungsgefährdet. In der Osculati 17.318-Serie zusätzlich Reduced-bore! Doppelter Malus: DZR (-3) + Reduced-bore (-5 bei kritischer Anwendung) = Score-Abzug bis -8.

(Confidence: documented — Osculati Katalog 2025)

### 8.12 Herstellervergleich — Zusammenfassung

| Hersteller | Land | Primärtyp | Material | Gewinde | Full-bore | Preis DN38 EUR | AYDI-Score |
|---|---|---|---|---|---|---|---|
| Groco BV | USA | Kugelhahn | Bronze C83600 | NPT | Ja | 170 | 95 |
| Blakes BB | UK | Kegelhahn | Bronze C83600 | BSP | Ja (immer) | 240 | 92 |
| Blakes Lever | UK | Kugelhahn | Bronze C83600 | BSP | Ja | 180 | 93 |
| Guidi 2060 | IT | Kugelhahn | Bronze C83600 | BSP | Ja | 130 | 90 |
| Guidi 2062 | IT | Kugelhahn | DZR-Messing | BSP | Nein (RB!) | 68 | 70 |
| TruDesign 90305 | NZ | Kugelhahn | Komposit PA66 | BSP | Ja | 85 | 88 |
| Forespar MV150 | USA | Kugelhahn | Komposit Marelon | NPT | Ja | 90 | 86 |
| Apollo 70-108 | USA | Kugelhahn | Bronze C83600 | NPT | Ja | 110 | 85 |
| Nibco T-580-70 | USA | Kugelhahn | Bronze | NPT | Nein (RB!) | 85 | 72 |
| Perko 0732 | USA | Kegelhahn | Bronze C83600 | NPT | Ja (immer) | 220 | 90 |
| Buck Algonquin | USA | Kugelhahn | Bronze C83600 | NPT | Ja | 150 | 87 |
| Vetus KRAAN | NL | Kugelhahn | Bronze C83600 | BSP | Ja | 115 | 85 |
| Vetus E-Valve | NL | Kugelhahn | Bronze C83600 | BSP | Ja | 620 | 90 |
| Osculati 17.319 | IT | Kugelhahn | Bronze C83600 | BSP | Ja | 95 | 82 |
| Osculati 17.318 | IT | Kugelhahn | DZR-Messing | BSP | Nein (RB!) | 50 | 65 |

**AYDI-Score-Erklärung**: Der Score berücksichtigt Material (40%), Bore-Typ (20%), Kugel/Dichtung (15%), Normkonformität (15%), Langzeit-Erfahrung (10%). Maximalscore 100.

(Confidence: estimated — aggregierte Hersteller-Daten + Praxis-Erfahrung)

---

## 9. Anlagen-spezifische Zuordnung

### 9.1 Kühlwassersystem Motor — Ventilhahn-Anforderungen

**Systemübersicht:**
Das Motor-Kühlwassersystem (Rohwasserkühlung) saugt Seewasser durch einen Borddurchlass an, leitet es durch den Wärmetauscher des Motors und gibt es über den Nassauspuff zurück. Der Ventilhahn am Kühlwassereinlass ist **sicherheitskritisch**: Er muss im Notfall schnell geschlossen werden können (Schlauchbruch = Wassereinbruch) UND er darf den Durchfluss nicht einschränken (Motor-Überhitzung).

| Anforderung | Spezifikation | Begründung |
|---|---|---|
| Ventilhahn-Typ | Kugelhahn Full-bore | Maximaler Durchfluss, schnelle Betätigung |
| Material Körper | Bronze C83600 oder C92200 | Korrosionsfest, temperaturbeständig |
| Material Kugel | Edelstahl 316L | Salzwasserbeständig |
| Dichtung | PTFE-GF (glasfaserverstärkt) | Langlebig bei Temperaturwechsel |
| Nennweite | Gemäß Motorhersteller-Vorgabe | Motor-Überhitzung bei zu kleiner DN! |
| Bore-Typ | PFLICHT: Full-bore | Reduced-bore = Motorschaden möglich |
| Temperaturbeständigkeit | Mind. +60°C (Umgebung Maschinenraum) | Nähe zum Motor |
| Griffzugänglichkeit | Ohne Werkzeug, ohne Demontage | Notfall-Situation |
| Sieb/Filter | Empfohlen: Wasserfilter (Groco ARG) nach Ventilhahn | Kühlwasserverunreinigung |

**Typische Konfiguration nach Motorleistung:**

| Motor-kW | Motor-PS | Empfohlene DN mm | Empfohlene DN Zoll | Durchfluss l/min | Empfohlener Hahn |
|---|---|---|---|---|---|
| 10–20 | 14–27 | DN20 | ¾" | 8–16 | Groco BV-0750 / Guidi 2060 ¾" |
| 20–40 | 27–54 | DN25 | 1" | 16–30 | Groco BV-1000 / Guidi 2060 1" |
| 40–75 | 54–100 | DN32 | 1¼" | 30–50 | Groco BV-1250 / Blakes Lever 1¼" |
| 75–150 | 100–200 | DN38 | 1½" | 50–100 | Groco BV-1500 / Blakes BB 1½" |
| 150–300 | 200–400 | DN50 | 2" | 100–200 | Groco BV-2000 / Blakes BB 2" |
| >300 | >400 | DN63–DN75 | 2½"–3" | >200 | Groco BV-2500/3000 |

**AYDI-Scoring Kühlwasser-Ventilhahn:**
- Full-bore Bronze + 316L Kugel: Score 95–100
- Full-bore Komposit (>60°C Abstand zum Motor): Score 85–90
- Reduced-bore Bronze: Score 60–70 (Warnung: Durchfluss prüfen!)
- Reduced-bore DZR-Messing: Score 40–50 (Doppelwarnung!)
- Gate-Ventil: Score 10 (SOFORT AUSTAUSCHEN)
- Kein Ventilhahn am Kühlwassereinlass: Score 0 (KRITISCH!)

(Confidence: documented — Volvo Penta Installation Manual, Yanmar Installation Guide, Groco Application Guide)

### 9.2 Nassauspuff (Wet Exhaust) — Ventilhahn-Anforderungen

**Systemübersicht:**
Der Nassauspuff mischt Motorabgase mit dem Kühlwasser und leitet das Gemisch durch einen Wasserlock über den Borddurchlass nach außenbords. Der Ventilhahn am Auspuff-Auslass ist **nicht immer vorhanden** — ABYC empfiehlt ihn, ISO 9093 schreibt ihn nicht vor. Wo vorhanden, muss er extreme Temperaturbedingungen standhalten.

| Anforderung | Spezifikation | Begründung |
|---|---|---|
| Ventilhahn-Typ | Kugelhahn Full-bore | Abgasgegendruck minimieren |
| Material Körper | Bronze C83600 — KEIN Komposit! | Temperatur bis 120°C am Auslass |
| Material Kugel | Edelstahl 316L | Korrosion durch Abgas + Seewasser |
| Dichtung | Viton (FKM) oder PTFE-GF | Temperaturbeständigkeit >100°C |
| Temperaturbeständigkeit | Mind. +120°C | Auspuff-Temperatur (nach Wasserlock) |
| Nennweite | ≥ Auspuff-Rohrdurchmesser | KEIN Engpass im Abgassystem! |
| Bore-Typ | PFLICHT: Full-bore | Abgas-Gegendruck → Motorschaden |

**WARNUNG**: Ein Komposit-Ventilhahn (TruDesign, Marelon) ist am Auspuff NICHT zulässig! Max. Temperatur Komposit: 82–93°C. Auspuff nach Wasserlock: 60–120°C. Bei Kühlwasserausfall (trockener Auspuff kurzzeitig): bis zu 400°C → Komposit schmilzt!

**AYDI-Scoring Auspuff-Ventilhahn:**
- Bronze Full-bore + Viton: Score 95–100
- Bronze Full-bore + PTFE: Score 85–90 (PTFE temperaturbeständig, aber Viton bevorzugt)
- Bronze Reduced-bore: Score 50–60 (Gegendruck-Warnung)
- Komposit: Score 20 (VERBOTEN an Auspuff! Sofort ersetzen!)
- Gate-Ventil: Score 10
- Kein Ventilhahn am Auspuff: Score 80 (kein Normverstoß, aber empfohlen)

(Confidence: documented — ABYC H-27, ISO 9094, Volvo Penta Exhaust Installation Guide)

### 9.3 Toilettensystem / Y-Ventil — Ventilhahn-Anforderungen

**Systemübersicht:**
Das marine WC-System umfasst typischerweise 3 Ventilhähne:
1. **Einlass-Ventilhahn**: Seewasser-Einlass für WC-Spülung
2. **Auslass-Ventilhahn**: Abwasser-Auslass (direkt oder über Y-Ventil)
3. **Y-Ventil**: Umschaltung Abwasser → See (offshore) / → Holding Tank (Hafen)

| Komponente | Typ | Material | DN | Besonderheit |
|---|---|---|---|---|
| Einlass-Hahn | Kugelhahn Full-bore | Bronze oder Komposit | DN20–DN25 | Standard, unkritisch |
| Auslass-Hahn | Kugelhahn Full-bore | Bronze oder Komposit | DN25–DN38 | Feststoff-führend! |
| Y-Ventil | 3-Wege Kugel oder Kegel | Bronze oder Komposit | DN25–DN38 | MARPOL-relevant! |

**Y-Ventil — Spezifische Anforderungen:**

| Anforderung | Spezifikation | Begründung |
|---|---|---|
| Bore-Typ | PFLICHT: Full-bore | Feststoffe dürfen nicht blockieren |
| Reinigbarkeit | Zerlegbar oder mit Spülport | Kalkablagerung, Verstopfung |
| MARPOL-Sicherung | Muss in Tank-Stellung fixierbar sein | Plombe/Draht in Häfen vorgeschrieben |
| Material | Bronze oder Komposit | Beides akzeptabel (kein Auspuff) |
| Schließstellung | 3 Positionen: A (See) / B (Tank) / C (geschlossen) | Nicht alle Y-Ventile haben Pos. C! |

**Y-Ventil-Empfehlung nach AYDI:**

| Priorität | Hersteller | Modell | Material | Preis EUR | Score |
|---|---|---|---|---|---|
| 1 | Groco | HF-Serie (3-Way) | Bronze C83600 | 280–420 | 95 |
| 2 | Blakes | Three-Way Plug | Bronze C83600 | 250–350 | 92 |
| 3 | Forespar | Marelon Y-Valve | Komposit Marelon | 120–190 | 88 |
| 4 | TruDesign | 90346/90347 | Komposit PA66 | 95–140 | 86 |
| 5 | Vetus | Y-Serie | Bronze/Komposit | 110–250 | 84 |

**Kalkbildung in WC-Systemen:**
In Seewasser-gespülten WC-Systemen bildet sich unvermeidlich Calciumcarbonat (Kalk) in den Leitungen und Ventilhähnen. Der Y-Ventil-Hahn ist besonders betroffen, da er nicht ständig durchströmt wird. Empfehlung:
- Vierteljährlich mit verdünnter Essigessenz (10%) spülen
- Jährlich Y-Ventil betätigen (auch im Winter!)
- Kegelhähne (Blakes) sind hier vorteilhaft: Konus kann zum Entkalkern ausgebaut werden

(Confidence: documented — Jabsco WC-System Manual, Raritan Marine Sanitation Guide)

### 9.4 Bilgensystem — Ventilhahn-Anforderungen

**Systemübersicht:**
Die Bilgenpumpe fördert Wasser aus der Bilge durch einen Borddurchlass nach außenbords. Der Ventilhahn am Bilgen-Auslass ist wichtig, aber weniger kritisch als der Kühlwasser-Einlass, da er ÜBER der Wasserlinie liegen sollte.

| Anforderung | Spezifikation | Begründung |
|---|---|---|
| Ventilhahn-Typ | Kugelhahn (Full- oder Reduced-bore) | Reduzierter Durchfluss akzeptabel |
| Material | Bronze, Komposit, auch DZR-Messing akzeptabel | Auslass über WL → geringere Korrosion |
| Nennweite | DN25–DN38 | Je nach Pumpenkapazität |
| Position | Möglichst ÜBER Wasserlinie | Kein Wassereinbruch bei offenem Hahn |
| Rückschlagventil | Empfohlen zwischen Pumpe und Ventilhahn | Rücklauf-Verhinderung |

**ACHTUNG**: Bei manchen Booten liegt der Bilgen-Auslass UNTER der Wasserlinie (insbesondere bei Booten mit geringem Freibord oder bei Segelbooten in Krängung). In diesem Fall gelten die gleichen strengen Anforderungen wie für den Kühlwasser-Einlass!

**AYDI-Scoring Bilge-Ventilhahn:**
- Über WL: Full-bore Bronze: Score 90, Reduced-bore akzeptabel: Score 80, Komposit: Score 85
- Unter WL: Gleiche Bewertung wie Kühlwasser-Einlass (siehe 9.1)

(Confidence: documented — ABYC H-22 Bilge Pumps, ISO 15083)

### 9.5 Klimaanlage (AC) — Ventilhahn-Anforderungen

**Systemübersicht:**
Marine-Klimaanlagen verwenden Seewasser als Kühlmedium. Ein Seewasserpumpe saugt durch einen Borddurchlass an, leitet das Wasser durch den Wärmetauscher (Kondensator) der Klimaanlage und gibt es über einen zweiten Borddurchlass zurück. Bei Motoryachten ab 12 m und Segelyachten ab 15 m sind AC-Systeme üblich.

| Anforderung | Spezifikation | Begründung |
|---|---|---|
| Ventilhahn-Typ (Einlass) | Kugelhahn Full-bore | Hoher Durchfluss bei geringem Druckverlust |
| Ventilhahn-Typ (Auslass) | Kugelhahn (Full- oder Reduced-bore) | Auslass weniger kritisch |
| Material | Bronze C83600 oder Komposit | Standard |
| Nennweite | Gemäß AC-Hersteller | Typisch DN25–DN50 |
| Bore-Typ (Einlass) | Empfohlen: Full-bore | Reduced-bore = AC-Leistungsverlust |
| Sieb/Filter | PFLICHT: Seewasserfilter vor AC-Einlass | Verschmutzung → Kondensator-Verstopfung → AC-Ausfall |

**AC-System-Dimensionierung (Durchfluss):**

| AC-Leistung BTU | AC-Leistung kW | Empfohlener Durchfluss l/min | Empfohlene DN mm |
|---|---|---|---|
| 6.000 | 1,8 | 4–6 | DN15 |
| 12.000 | 3,5 | 8–12 | DN20 |
| 16.000 | 4,7 | 12–16 | DN25 |
| 24.000 | 7,0 | 16–24 | DN25–DN32 |
| 36.000 | 10,5 | 24–36 | DN32–DN38 |
| 48.000 | 14,0 | 36–48 | DN38 |
| 60.000+ | 17,5+ | 48+ | DN50 |

**Bewuchsproblem AC-System:**
AC-Systeme sind besonders bewuchsanfällig, weil:
1. Warmes Seewasser (nach Kondensator +5–10°C wärmer als Einlass) fördert Bewuchs
2. Geringer Durchfluss bei Teillast begünstigt Sedimentation
3. Langer Stillstand im Winter (Nordeuropa) oder im Sommer (Heizperiode Nordeuropa) → Bewuchs im ruhenden System

**Empfehlung**: Ventilhahn am AC-Einlass alle 2 Wochen betätigen. Jährlich Seewasserleitungen mit Essigessenz oder Rydlyme-Lösung spülen.

(Confidence: documented — Marine Air Systems Installation Manual, Webasto Marine AC Guide)

### 9.6 Generatorsystem — Ventilhahn-Anforderungen

**Systemübersicht:**
Der Bordgenerator hat ein eigenständiges Kühlwassersystem mit eigenem Borddurchlass und Ventilhahn. Die Anforderungen sind identisch mit dem Hauptmotor-Kühlsystem (9.1), aber typisch eine Nennweite kleiner.

| Anforderung | Spezifikation | Begründung |
|---|---|---|
| Ventilhahn-Typ | Kugelhahn Full-bore | Wie Hauptmotor |
| Material | Bronze C83600 | Wie Hauptmotor |
| Nennweite | Gemäß Generator-Hersteller | Typisch DN20–DN32 |
| Bore-Typ | Full-bore empfohlen | Generator-Überhitzung vermeiden |
| Temperaturbeständigkeit | Mind. +60°C | Maschinenraum |

**Generator-Kühlwasser-Dimensionierung:**

| Generator-kW | Generator-kVA | Empfohlene DN mm | Empfohlener Hahn |
|---|---|---|---|
| 3–5 | 3,5–6 | DN20 | Groco BV-0750 / Guidi 2060 ¾" |
| 5–10 | 6–12 | DN20–DN25 | Groco BV-1000 / Guidi 2060 1" |
| 10–20 | 12–24 | DN25 | Groco BV-1000 / Blakes Lever 1" |
| 20–40 | 24–48 | DN25–DN32 | Groco BV-1250 / Blakes BB 1¼" |
| >40 | >48 | DN32–DN38 | Groco BV-1500 / Blakes BB 1½" |

**Besonderheit Generator-Ventilhahn:**
Der Generator-Ventilhahn wird oft vergessen, weil der Generator seltener läuft als der Hauptmotor. Folge: Ventilhahn sitzt fest, wenn der Generator nach langer Standzeit gestartet wird. Empfehlung: Bei jeder Seeventil-Inspektion auch den Generator-Hahn betätigen!

(Confidence: documented — Onan/Cummins Marine Generator Installation Manual, Fischer Panda Installation Guide)

### 9.7 Übersichtstabelle — Ventilhahn-Anforderungen nach Anlage

| Anlage | Hahn-Typ | Bore | Material (min.) | DN (typ.) | Temp. °C | Prio. | Score-Gewicht |
|---|---|---|---|---|---|---|---|
| Kühlwasser Motor (Einlass) | Kugelhahn | Full-bore PFLICHT | Bronze C83600 | DN25–DN50 | 60 | KRITISCH | 25% |
| Nassauspuff (Auslass) | Kugelhahn | Full-bore PFLICHT | Bronze C83600 | DN38–DN50 | 120 | HOCH | 15% |
| Toilette Einlass | Kugelhahn | Full-bore empf. | Bronze/Komposit | DN20–DN25 | 40 | MITTEL | 8% |
| Toilette Auslass | Kugelhahn | Full-bore PFLICHT | Bronze/Komposit | DN25–DN38 | 40 | MITTEL | 8% |
| Y-Ventil WC | 3-Wege | Full-bore PFLICHT | Bronze/Komposit | DN25–DN38 | 40 | MITTEL | 8% |
| Bilge Auslass | Kugelhahn | Full/Reduced | Bronze/Komposit/DZR | DN25–DN38 | 40 | NIEDRIG-HOCH* | 10% |
| AC Einlass | Kugelhahn | Full-bore empf. | Bronze/Komposit | DN25–DN50 | 40 | MITTEL | 8% |
| AC Auslass | Kugelhahn | Full/Reduced | Bronze/Komposit | DN25–DN50 | 50 | NIEDRIG | 3% |
| Generator Einlass | Kugelhahn | Full-bore empf. | Bronze C83600 | DN20–DN32 | 60 | HOCH | 10% |
| Pantry/Waschbecken Abfluss | Kugelhahn | Full/Reduced | Bronze/Komposit/DZR | DN15–DN25 | 40 | NIEDRIG | 2% |
| Dusche Abfluss | Kugelhahn | Full/Reduced | Bronze/Komposit/DZR | DN20–DN25 | 40 | NIEDRIG | 2% |
| Ankerspülung | Kugelhahn | Full/Reduced | Bronze/Komposit | DN20–DN25 | 40 | NIEDRIG | 1% |

*Bilge: NIEDRIG wenn über WL, HOCH wenn unter WL

**Score-Gewichtung**: Die Spalte "Score-Gewicht" definiert, wie stark der Einzelhahn in den Gesamtscore des Ventilhahn-Systems eingeht. Der Kühlwasser-Motor-Hahn hat mit 25% die höchste Gewichtung, weil sein Versagen sofortige Konsequenzen hat (Wassereinbruch ODER Motorüberhitzung).

(Confidence: documented + calculated — AYDI-Scoring-Framework, ABYC H-27, ISO 9093)

---

## 10. Verbindungstechnik

### 10.1 Flanschverbindungen

#### 10.1.1 Flanschtypen im Yachtbau

| Flanschtyp | Norm | Typische DN | Druckklasse | Einsatz im Yachtbau |
|------------|------|-------------|-------------|---------------------|
| Flachflansch (PN6/PN10) | DIN EN 1092-1 | DN25–DN100 | PN6–PN16 | Motor-Kühlwasser >DN40, Tankventile |
| Vorschweißflansch | DIN EN 1092-1 | DN32–DN80 | PN16–PN25 | Hochdrucksysteme, Feuerlöschleitungen |
| Gewindeflansch | DIN EN 1092-1 | DN15–DN50 | PN10–PN16 | Adapter Bronze-Ventil ↔ Stahlrohr |
| Losflansch (Bördelflansch) | DIN EN 1092-1 | DN25–DN65 | PN6–PN10 | Flexible Verbindung, leichte Demontage |
| Kompaktflansch (Marine) | ABYC H-27 / ISO 9093 | DN15–DN50 | PN10 | Standard Seeventil-Anschluss |

**Flanschdicken nach Material (Mindestmaße):**
- Bronze C83600 (DN25): Flanschdicke min. 8 mm, Lochkreis-Ø 100 mm, 4× M10
- Bronze C83600 (DN38): Flanschdicke min. 10 mm, Lochkreis-Ø 120 mm, 4× M12
- Bronze C83600 (DN50): Flanschdicke min. 12 mm, Lochkreis-Ø 140 mm, 4× M12
- Komposit (DN25): Flanschdicke min. 12 mm (höher als Bronze wg. geringerer Festigkeit)
- Komposit (DN38): Flanschdicke min. 14 mm
- Komposit (DN50): Flanschdicke min. 16 mm

**Scoring-Kriterien Flanschverbindung:**
- Korrekter Flanschtyp für Anwendung: 0–25 Punkte
- Schraubenanzahl und -qualität: 0–25 Punkte
- Dichtung vorhanden und korrekt: 0–25 Punkte
- Anzugsdrehmoment dokumentiert: 0–25 Punkte
- **Gesamt: 0–100 Punkte**

#### 10.1.2 Dichtungen für Flanschverbindungen

| Dichtungstyp | Material | Temp.-Bereich | Max. Druck | Einsatz | Lebensdauer |
|--------------|----------|---------------|------------|---------|-------------|
| Flachdichtung NBR | Nitrilkautschuk | –30 bis +100°C | PN16 | Standard Seewasser | 8–12 Jahre |
| Flachdichtung EPDM | Ethylen-Propylen | –40 bis +130°C | PN16 | Kühlwasser süß/salz | 10–15 Jahre |
| Flachdichtung FPM/Viton® | Fluorkautschuk | –20 bis +200°C | PN25 | Motor-Abgas-nah | 12–18 Jahre |
| Spiraldichtung | Edelstahl/Graphit | –200 bis +550°C | PN40 | Hochdruck, Dampf | 15–25 Jahre |
| PTFE-Flachdichtung | PTFE (gefüllt) | –200 bis +260°C | PN25 | Chemisch aggressiv | 10–20 Jahre |
| O-Ring (Flanschnut) | NBR/EPDM/FPM | je nach Material | PN25 | Kompaktflansch-Verbindung | 5–10 Jahre |

**Dichtflächenrauigkeit:**
- NBR/EPDM: Ra 3,2–6,3 μm
- PTFE: Ra 1,6–3,2 μm
- Spiraldichtung: Ra 3,2–6,3 μm
- O-Ring: Ra 0,8–1,6 μm (gefräst/gedreht)

### 10.2 Gewindeverbindungen

#### 10.2.1 Gewindetypen

| Gewinde | Norm | Profil | Dichtung | Verbreitung Yacht |
|---------|------|--------|----------|-------------------|
| BSP parallel (BSPP/G) | ISO 228-1 / DIN EN ISO 228 | 55° Whitworth | Über Dichtfläche/O-Ring | 65% (EU-Standard) |
| BSP konisch (BSPT/R/Rp) | ISO 7-1 / DIN 2999 | 55° Whitworth | Gewinde dichtet selbst | 20% (UK-Tradition) |
| NPT (konisch) | ASME B1.20.1 | 60° Unified | Gewinde dichtet selbst | 10% (US-Boote) |
| NPSM (parallel) | ASME B1.20.1 | 60° Unified | Über O-Ring/Dichtfläche | 3% (US-Marine) |
| Metrisch (M) | ISO 261 / DIN 13 | 60° metrisch | Dichtfläche/Dichtring | 2% (Sonderanwendungen) |

**WARNUNG — INKOMPATIBILITÄT:**
BSP (55°) und NPT (60°) sind NICHT kompatibel! Mischung führt zu:
- Undichtigkeit innerhalb von Stunden bis Tagen
- Gewindezerstörung durch unterschiedliche Flankenwinkel
- Galvanische Korrosion bei Materialunterschied
- Score-Abzug: **–40 Punkte** bei festgestellter Mischung

#### 10.2.2 Gewindedichtmittel

| Dichtmittel | Typ | Seewasser | Demontierbar | Temp. max | Anmerkung |
|-------------|-----|-----------|--------------|-----------|-----------|
| PTFE-Band (Teflonband) | Wickelband | Ja | Gut | +260°C | 3–5 Lagen, IN Gewinderichtung wickeln |
| PTFE-Gewindedichtfaden | Faden | Ja | Gut | +260°C | Einfacher als Band, sicherer Sitz |
| Loctite 577 | Anaerob | Ja | Mittel | +150°C | Mittelfest, für Messing/Bronze |
| Loctite 5776 | Anaerob | Ja | Gut | +150°C | Niedrigfest, für häufige Demontage |
| Loxeal 58-11 | Anaerob | Ja | Mittel | +150°C | DVGW-zugelassen, gute Seewasserresistenz |
| Fermit Pate | Dichtpaste | Bedingt | Gut | +100°C | Nur Trinkwasser, NICHT Seewasser |
| Hanf + Fermit | Traditionell | Nein | Gut | +100°C | NUR Trinkwasser, quillt in Salzwasser |

**Scoring-Kriterien Gewindeverbindung:**
- Gewindetyp korrekt identifiziert: 0–20 Punkte
- Dichtmittel-Wahl passend: 0–20 Punkte
- Einschraubtiefe ausreichend (min. 1,5× Nenndurchmesser): 0–20 Punkte
- Kein Mischgewinde: 0–20 Punkte
- Drehmoment korrekt (nicht über-/unterfest): 0–20 Punkte
- **Gesamt: 0–100 Punkte**

#### 10.2.3 Gewindegrößen Seeventilhähne

| Anwendung | Min. Gewinde | Empfohlen | Max. sinnvoll |
|-----------|-------------|-----------|---------------|
| Echolot/Logge | G ½" (DN15) | G ¾" (DN20) | G 1" (DN25) |
| WC Einlass | G ¾" (DN20) | G 1" (DN25) | G 1¼" (DN32) |
| WC Auslass | G 1" (DN25) | G 1¼" (DN32) | G 1½" (DN38) |
| Motor Kühlwasser | G ¾" (DN20) | G 1" (DN25) | G 1½" (DN38) |
| Klimaanlage | G 1" (DN25) | G 1¼" (DN32) | G 2" (DN50) |
| Feuerlösch | G 1½" (DN38) | G 2" (DN50) | G 2½" (DN65) |

### 10.3 Schlauchanschlüsse

#### 10.3.1 Schlauchtüllen

| Tüllentyp | Befestigung | Druckbereich | Seewasser | Score-Relevanz |
|-----------|-------------|-------------|-----------|----------------|
| Gerade Schlauchtülle | Schlauchschelle | 0–4 bar | Ja | Standard unter WL |
| 90°-Schlauchtülle | Schlauchschelle | 0–4 bar | Ja | Enge Einbauräume |
| Stufentülle (Serrated) | Schlauchschelle | 0–6 bar | Ja | Erhöhte Auszugfestigkeit |
| Schnellkupplung | Clip/Hebel | 0–10 bar | Material-abhängig | Schnelle Wartung |

**Schlauchschellen-Anforderungen unter der Wasserlinie:**
- Material: Edelstahl AISI 316 (A4), NIEMALS verzinkter Stahl
- Anzahl: **IMMER doppelt** (2 Schellen pro Anschluss) unter WL
- Schellenbreite: min. 12 mm bei DN25, min. 16 mm bei DN38
- Banddicke: min. 0,7 mm
- Schneckengewinde: V2A/V4A, kein Zamak (Zinkdruckguss)
- Score-Abzug bei einfacher Schelle unter WL: **–30 Punkte**

(Confidence: documented + calculated — DIN EN 1092-1, ISO 228-1, ABYC H-27, ABYC H-24)

---

## 11. Technische Referenz & Berechnungen

### 11.1 Durchflusskoeffizienten

#### 11.1.1 Definition Cv und Kv

**Cv (US-Koeffizient):**
Volumenstrom in US-Gallonen pro Minute (GPM) von Wasser bei 60°F, der bei einem Druckabfall von 1 psi durch das Ventil fließt.

**Kv (EU-Koeffizient):**
Volumenstrom in m³/h von Wasser bei 20°C, der bei einem Druckabfall von 1 bar durch das Ventil fließt.

**Umrechnung:**
```
Kv = Cv × 0,865
Cv = Kv × 1,156
```

#### 11.1.2 Cv/Kv-Werte nach Ventiltyp und DN

| DN | Kugelhahn Full-bore Kv | Kugelhahn Reduced-bore Kv | Kegelhahn Kv | Schieberventil Kv (Vergleich) |
|----|------------------------|---------------------------|--------------|-------------------------------|
| DN15 | 14,0 | 8,5 | 6,0 | 12,0 |
| DN20 | 28,0 | 17,0 | 12,0 | 24,0 |
| DN25 | 55,0 | 33,0 | 22,0 | 48,0 |
| DN32 | 95,0 | 55,0 | 38,0 | 82,0 |
| DN38 | 135,0 | 80,0 | 56,0 | 120,0 |
| DN50 | 240,0 | 140,0 | 95,0 | 210,0 |
| DN65 | 390,0 | 230,0 | 155,0 | 340,0 |
| DN80 | 560,0 | 330,0 | 220,0 | 490,0 |

**Kv-Ratio (Kugel Full-bore als Referenz = 1,00):**
- Kugelhahn Reduced-bore: 0,58–0,61
- Kegelhahn (konisch): 0,39–0,43
- Schieberventil: 0,85–0,88

#### 11.1.3 Druckverlustberechnung

**Grundformel:**
```
ΔP = (Q / Kv)² × ρ/ρ_wasser

wobei:
  ΔP = Druckverlust [bar]
  Q = Volumenstrom [m³/h]
  Kv = Durchflusskoeffizient [m³/h]
  ρ = Dichte des Mediums [kg/m³]
  ρ_wasser = 1000 kg/m³ (Referenz)
```

**Seewasser-Korrektur:**
```
ρ_seewasser = 1025 kg/m³ (Durchschnitt)
Korrekturfaktor = √(1025/1000) = 1,0124
→ ΔP_seewasser = ΔP_süßwasser × 1,025
```

**Praxisbeispiel — Motor-Kühlwasser (DN25, Full-bore Kugelhahn):**
```
Motor: 40 PS Diesel, Kühlwasserbedarf: 2,5 m³/h
Kv (DN25 Full-bore) = 55,0
ΔP = (2,5 / 55,0)² × 1,025
ΔP = 0,00207 × 1,025
ΔP = 0,00212 bar = 21,2 mbar

→ Vernachlässigbar. Full-bore DN25 ist ausreichend.
```

**Praxisbeispiel — Klimaanlage (DN32, Reduced-bore Kugelhahn):**
```
Klimaanlage: 16.000 BTU, Kühlwasserbedarf: 4,2 m³/h
Kv (DN32 Reduced-bore) = 55,0
ΔP = (4,2 / 55,0)² × 1,025
ΔP = 0,00583 × 1,025
ΔP = 0,00598 bar = 59,8 mbar

→ Akzeptabel, aber bei langen Leitungswegen Full-bore erwägen.
```

### 11.2 Dimensionierungsformeln

#### 11.2.1 Ventilgröße nach Durchfluss

**Mindest-Kv-Berechnung:**
```
Kv_min = Q × √(ρ/ρ_wasser) / √(ΔP_max)

wobei:
  Q = benötigter Volumenstrom [m³/h]
  ΔP_max = maximal zulässiger Druckverlust [bar]
```

**Faustregel für Yachten:**
```
Ventil-DN ≥ Rohr-DN (niemals kleiner!)
Kv_gewählt ≥ 1,3 × Kv_min (Sicherheitsfaktor)
```

#### 11.2.2 Strömungsgeschwindigkeit

**Maximalgeschwindigkeiten in Seewasser-Leitungen:**
| Leitungstyp | Max. v [m/s] | Optimal v [m/s] |
|-------------|-------------|-----------------|
| Einlass unter WL | 1,5 | 0,8–1,2 |
| Auslass über WL | 2,5 | 1,5–2,0 |
| Motorkühlwasser | 2,0 | 1,0–1,5 |
| Bilge (Notpumpe) | 3,0 | 2,0–2,5 |

**Geschwindigkeitsformel:**
```
v = Q / (A × 3600)

wobei:
  v = Strömungsgeschwindigkeit [m/s]
  Q = Volumenstrom [m³/h]
  A = Querschnittsfläche [m²]
  A = π/4 × d² (d = Innendurchmesser in m)
```

#### 11.2.3 Kavitationsberechnung

**Kavitations-Sicherheitsfaktor:**
```
σ = (P_einlass - P_dampf) / ΔP_ventil

wobei:
  σ > 2,0: sicher (kein Kavitationsrisiko)
  σ = 1,5–2,0: grenzwertig (Monitoring empfohlen)
  σ < 1,5: Kavitation wahrscheinlich (Ventil vergrößern!)
```

Für Seewasser bei 25°C: P_dampf ≈ 0,032 bar abs.
Für Seewasser bei 35°C: P_dampf ≈ 0,056 bar abs.

### 11.3 Drehmoment-Tabelle

| DN | Kugelhahn Betätigungsdrehmoment [Nm] | Kegelhahn Betätigungsdrehmoment [Nm] | Max. Anzugsdrehmoment Stopfbuchse [Nm] |
|----|--------------------------------------|--------------------------------------|----------------------------------------|
| DN15 | 3–6 | 5–10 | 8 |
| DN20 | 5–10 | 8–15 | 12 |
| DN25 | 8–15 | 12–22 | 18 |
| DN32 | 12–22 | 18–35 | 25 |
| DN38 | 18–30 | 25–48 | 32 |
| DN50 | 25–45 | 40–75 | 45 |
| DN65 | 40–70 | 65–120 | 65 |
| DN80 | 60–100 | 90–170 | 85 |

**Hinweis:** Kegelhähne benötigen 40–70% mehr Betätigungsdrehmoment als Kugelhähne gleicher Nennweite. Bei Langzeitbetrieb ohne Wartung steigt das Kegelhahn-Drehmoment um Faktor 2–3.

### 11.4 Temperatur-Druck-Diagramm (Bronze C83600)

| Temperatur [°C] | Max. Betriebsdruck [bar] PN10 | Max. Betriebsdruck [bar] PN16 |
|------------------|-------------------------------|-------------------------------|
| –20 | 10,0 | 16,0 |
| 0 | 10,0 | 16,0 |
| 20 | 10,0 | 16,0 |
| 50 | 9,5 | 15,2 |
| 80 | 8,8 | 14,1 |
| 100 | 8,0 | 12,8 |
| 120 | 7,0 | 11,2 |
| 150 | 5,5 | 8,8 |

(Confidence: calculated + documented — VDI/VDE 2173, EN 60534-2-1, ABYC H-27)

---

## 12. Einbau-/Austausch-Anleitung

### 12.1 Voraussetzungen

#### 12.1.1 Wann Helling/Kran erforderlich

| Szenario | Helling erforderlich? | Begründung |
|----------|----------------------|------------|
| Austausch Seeventilhahn unter WL | JA | Boot muss trocken stehen, Rumpfdurchbruch offen |
| Wartung Stopfbuchse | NEIN (wenn Hahn geschlossen dicht) | Hahn schließen → Stopfbuchse bearbeiten |
| Austausch Handgriff | NEIN | Kein Eingriff in druckführende Teile |
| Austausch Kegel bei Kegelhahn | NEIN (wenn Hahn geschlossen dicht) | Kegel von oben herausnehmbar |
| Austausch Kugel bei Kugelhahn | JA (bei 1-teiligem Gehäuse) | Gehäuse muss vom Rumpf getrennt werden |
| Nachdichten Flanschverbindung | Situativ | Wenn unter WL und nicht absperrbar → JA |
| Kompletttausch Borddurchlass + Hahn | JA | Rumpfdurchbruch wird geöffnet |

#### 12.1.2 Werkzeugliste

**Basiswerkzeug (alle Arbeiten):**
- Gabelschlüsselsatz 10–36 mm (Edelstahl oder verchromt)
- Ringschlüsselsatz 10–36 mm
- Rohrzange Nr. 1 und Nr. 2 (Messing-Backen oder Schutzbacken verwenden!)
- Drehmomentschlüssel 5–100 Nm
- PTFE-Band (hochwertiges Markenprod., min. 0,1 mm dick)
- Anaerobe Gewindedichtung (Loctite 577 oder äquivalent)
- Silikonfreies Reinigungsmittel (Aceton oder Isopropanol)
- Schleifpapier P400–P800 (für Dichtflächen)
- Drahtbürste (Bronze oder Edelstahl, NICHT Stahl!)
- Lappen, Auffangwanne

**Zusatzwerkzeug Kegelhahn:**
- Kegelschleifpaste (fein, Körnung 600+)
- Einschleif-Kurbel oder Quergriff
- Messuhr (optional, für Kegelsitz-Prüfung)
- Petroleumöl (für Dichtigkeitsprüfung)

**Zusatzwerkzeug Flanschverbindung:**
- Dichtungssatz (passend für Flansch-DN)
- Schraubensatz Edelstahl A4 (neue Schrauben bei jedem Zusammenbau!)
- Federringe oder Sicherungsmuttern
- Flächendichtmittel (optional, dünn auf Metallflansche)

### 12.2 Austausch Kugelhahn — Schritt für Schritt

**Phase 1: Vorbereitung (Dauer: 30–60 min)**

1. Boot trockenstellen (Helling/Kran). Kielblöcke stabil, Stützen gesetzt.
2. Position des zu tauschenden Hahns von außen markieren (Edding am Rumpf).
3. Innenraum: alle Verkleidungen/Möbelteile entfernen, Zugang zum Hahn freilegen.
4. Bilge trockenlegen, saugfähiges Material unterlegen.
5. Fotos vom Ist-Zustand: Gewindetyp, Schlauchanschlüsse, Kabelverläufe, Rohrleitungsführung.
6. Ersatzhahn bereithalten, Gewindegröße und -typ VERIFIZIEREN (nicht "sollte passen").
7. Seeventil-Tagebuch prüfen: Einbaudatum, Material, letzte Wartung.

**Phase 2: Demontage (Dauer: 45–120 min)**

8. Schlauch/Rohr vom Hahn-Auslass lösen: Schlauchschellen öffnen, Schlauch abziehen (Wärme hilft bei festsitzenden Schläuchen — Heißluftpistole 60°C max.).
9. Gewindeverbindung Hahn ↔ Borddurchlass lösen:
   - Konterung am Borddurchlass-Flansch ansetzen (IMMER gegenhalten!).
   - Hahn gegen Uhrzeigersinn herausdrehen.
   - ACHTUNG: Nicht am Borddurchlass drehen — der sitzt im Laminat!
10. Wenn Flanschverbindung: Alle Schrauben gleichmäßig lösen (Kreuzverfahren).
11. Hahn entnehmen. Restmedium auffangen.
12. Gewinde/Flanschfläche am Borddurchlass inspizieren:
    - Gewinde: Gewindegänge beschädigt? → Nachschneiden oder Borddurchlass tauschen.
    - Flansch: Dichtfläche plan? Riefen? → Planschleifen oder tauschen.
13. Borddurchlass-Zustand dokumentieren (Fotos, Wandstärke messen wenn möglich).

**Phase 3: Einbau neuer Hahn (Dauer: 45–90 min)**

14. Neuen Hahn inspizieren: Leichtgängigkeit prüfen, Guss-Qualität, Gewinde sauber.
15. Gewindedichtung aufbringen:
    - PTFE-Band: 4–6 Lagen, IN Einschraubrichtung (Uhrzeigersinn bei Blick auf Gewindeende).
    - Alternativ: Anaerobe Dichtung auf sauberes, fettfreies Gewinde auftragen.
16. Hahn einschrauben:
    - Handfest + 1,5–2 Umdrehungen mit Werkzeug.
    - Endposition: Griff muss in zugänglicher Position stehen!
    - Hahn-Griff soll bei "OFFEN" parallel zur Leitung zeigen.
17. Bei Flanschverbindung:
    - Neue Dichtung einlegen (NIEMALS alte Dichtung wiederverwenden).
    - Schrauben handfest anziehen, dann im Kreuzverfahren auf Solldrehmoment.
    - M10 A4: 25–30 Nm, M12 A4: 40–50 Nm.
18. Schlauchanschluss montieren:
    - Schlauch auf Tülle schieben (Silikonspray als Gleitmittel erlaubt).
    - Doppelte Schlauchschellen montieren (unter WL PFLICHT).
    - Schellen versetzt anordnen (nicht übereinander).
    - Schellenanzug: fest, aber ohne Schlauch einzuschneiden (ca. 3–4 Nm).

**Phase 4: Dichtigkeitsprüfung (Dauer: 30–60 min)**

19. Hahn schließen (Griff quer zur Leitung).
20. Boot zu Wasser lassen.
21. Erste Prüfung SOFORT nach Wasserkontakt:
    - Flansch/Gewinde trocken? → OK
    - Tropfenbildung? → Aus Wasser nehmen, nachdichten.
22. Hahn langsam öffnen (¼-Drehung, 10 Sekunden warten).
23. Schlauchanschlüsse prüfen: trocken?
24. Hahn ganz öffnen. 15 Minuten warten. Alle Verbindungen prüfen.
25. Leitung unter Betriebsdruck setzen (Motor/Pumpe starten). 30 Minuten Probelauf.
26. Abschlussprüfung: Alle Verbindungspunkte mit Küchenpapier abwischen — kein Feuchtebefund.

**Phase 5: Dokumentation (Dauer: 15 min)**

27. Seeventil-Tagebuch aktualisieren: Datum, Material, Hersteller, Gewindetyp, Dichtmittel.
28. Fotos des neuen Einbaus archivieren.
29. Alten Hahn aufbewahren (bis nächste Saison ohne Probleme).
30. Nächsten Wartungstermin notieren: Sichtkontrolle nach 1 Monat, reguläre Wartung nach 12 Monaten.

### 12.3 Austausch/Wartung Kegelhahn — Besonderheiten

**Kegel-Einschleifen (Wartung ohne Ausbau):**

1. Hahn schließen. Leitung entleeren.
2. Konusmutter lösen (unten am Hahnkörper).
3. Kegel herausnehmen (nach oben herausziehen).
4. Sitzflächen im Gehäuse und am Kegel reinigen.
5. Dünne Schicht Kegelschleifpaste auftragen.
6. Kegel einsetzen, mit Quergriff gleichmäßig drehen (NICHT hämmern!).
7. 20–30 Umdrehungen in jede Richtung, Paste erneuern nach 10 Zyklen.
8. Paste restlos entfernen (Lösungsmittel + Lappen).
9. Petroleumöl-Test: Kegel einsetzen, Petroleum auf Sitzfläche geben, 5 min warten. Kein Durchgang = dicht.
10. Konusmutter anziehen: gerade so fest, dass der Kegel leicht drehbar bleibt (Federspannung).

**Kegel-Austausch:**
Schritte 1–4 wie oben, dann neuen Kegel einschleifen (mindestens 50 Zyklen für Ersteinpassung). Nur Original-Ersatzteile oder professionell nachgefertigte Kegel verwenden.

### 12.4 Zeitkalkulation und Kosten

| Arbeit | Dauer | Materialkosten [EUR] | Werftarbeit [EUR/h] | Gesamt geschätzt [EUR] |
|--------|-------|---------------------|---------------------|----------------------|
| Kugelhahn-Tausch DN25 (Bronze) | 3–4 h | 80–180 | 85–120 | 335–660 |
| Kugelhahn-Tausch DN38 (Bronze) | 4–5 h | 120–280 | 85–120 | 460–880 |
| Kegelhahn-Einschleifen | 1–2 h | 15–30 | 85–120 | 100–270 |
| Kegelhahn komplett tauschen | 3–5 h | 100–250 | 85–120 | 355–850 |
| Komposit-Hahn-Tausch DN25 | 2–3 h | 60–140 | 85–120 | 230–500 |
| Stopfbuchse nachdichten | 0,5–1 h | 5–15 | 85–120 | 48–135 |
| Flanschdichtung erneuern | 1–2 h | 10–30 | 85–120 | 95–270 |
| Helling/Kran (Einmal) | — | — | — | 250–800 |

(Confidence: documented + estimated — Werftpreise 2024/2025 Deutschland, ABYC H-27)

---

## 13. Lebensdauer und Alterungsmechanismen

### 13.1 Erwartete Lebensdauer nach Ventiltyp

| Ventiltyp | Material | Lebensdauer (mit Wartung) | Lebensdauer (ohne Wartung) | Faktoren |
|-----------|----------|--------------------------|---------------------------|----------|
| Kugelhahn | Bronze C83600 | 25–35 Jahre | 15–20 Jahre | Seewasser-Qualität, Betätigungshäufigkeit |
| Kugelhahn | DZR-Messing | 20–30 Jahre | 10–15 Jahre | Entzinkungsrisiko regional |
| Kugelhahn | Komposit (Marelon®) | 15–25 Jahre | 10–15 Jahre | UV-Exposition, mechanische Belastung |
| Kugelhahn | Edelstahl 316L | 30–40+ Jahre | 20–25 Jahre | Spaltkorrosion in stagnierendem Seewasser |
| Kegelhahn | Bronze C83600 | 15–20 Jahre | 5–10 Jahre | Einschleifen-Intervall entscheidend |
| Kegelhahn | Bronze vergoldet | 20–25 Jahre | 8–12 Jahre | Goldschicht verschleißt bei Nichtschleifen |

### 13.2 Alterungsmechanismen

#### 13.2.1 Korrosion

**Entzinkung (Dezincification):**
- Betrifft: Messing (>15% Zink), einige Bronzen mit Zinkanteil
- Mechanismus: Selektive Auflösung des Zinks, poröse Kupferstruktur bleibt
- Sichtbar als: Rosa-kupferfarbene Bereiche statt gelb-goldener Oberfläche
- Geschwindigkeit: 0,1–0,5 mm/Jahr in warmen Gewässern, 0,02–0,1 mm/Jahr in kalten Gewässern
- Kritisch ab: 30% Querschnittsverlust → mechanische Festigkeit unzureichend
- Score-Abzug: –20 (leicht) bis –80 (schwer) Punkte

**Galvanische Korrosion (Elektrolyse):**
- Betrifft: Ungleichartige Metalle in Kontakt (z.B. Bronze-Hahn auf Aluminium-Rumpf)
- Mechanismus: Elektrochemisches Potenzial treibt Korrosion des unedleren Metalls
- Spannungsreihe (Seewasser, wichtigste):
  - Graphit: +0,20 V (edel)
  - Edelstahl 316 (passiv): +0,05 V
  - Bronze C83600: –0,31 V
  - Messing: –0,40 V
  - Aluminium: –0,76 V
  - Zink: –1,03 V (unedel)
- Kritische Potentialdifferenz: >0,25 V → aktive Korrosion
- Score-Abzug: –25 (erkennbar) bis –90 (aktiv fortschreitend)

**Spaltkorrosion (Crevice Corrosion):**
- Betrifft: Edelstahl 316 in Gewindespalten, Flanschspalten, O-Ring-Nuten
- Mechanismus: Sauerstoffverarmung im Spalt → Passivschicht löst sich
- Besonders gefährlich in: stehendem Seewasser, tropischen Gewässern
- Vermeidung: Gewindespalte abdichten, keine offenen Spalte unter WL

#### 13.2.2 Bewuchs (Biofouling)

**Stufen des Bewuchses:**
1. Biofilm (Bakterien, Algen): 24–72 Stunden nach Wasserkontakt
2. Weiche Bewuchsorganismen (Schleimalgen, Hydroiden): 1–4 Wochen
3. Harte Bewuchsorganismen (Seepocken, Muscheln): 4–12 Wochen
4. Makrobewuchs (Austern, Röhrenwürmer): 3–12 Monate

**Auswirkungen auf Ventilhähne:**
- Kugelhahn: Seepocken in Kammer → Kugel blockiert → Hahn nicht mehr bedienbar
- Kegelhahn: Bewuchs auf Kegelsitz → Undichtigkeit → Druckverlust
- Durchflussverlust: 10% (leichter Biofilm) bis 80% (Makrobewuchs)
- Score-Abzug: –10 (Biofilm) bis –50 (Makrobewuchs)

**Bewuchs-Prävention:**
- Antifouling-Beschichtung im Ventilinneren (z.B. Coppercoat, Trilux)
- Regelmäßige Betätigung (1× pro Woche OFFEN↔ZU): Score-Bonus +10
- Süßwasserspülung bei Langzeitlager: Score-Bonus +5
- Bewuchsfreie Ventile (Komposit mit Biozid): Score-Bonus +5

#### 13.2.3 Mechanischer Verschleiß

**Sitz-/Kugelabrieb:**
- Ursache: Partikel im Seewasser (Sand, Rostflocken) schleifen Sitz und Kugel
- Messgröße: Leckrate bei geschlossenem Ventil
- Grenzwert: >1 Tropfen/min bei geschlossenem Ventil = TAUSCH erforderlich
- Typische Verschleißrate: 0,01–0,05 mm/10.000 Betätigungen (Bronze-Kugel, PTFE-Sitz)

**Stopfbuchsenverschleiß:**
- Ursache: Mechanische Reibung, Temperaturwechsel, chemische Alterung
- Intervall Nachziehen/Ersetzen: alle 2–5 Jahre (Kegelhahn), alle 5–10 Jahre (Kugelhahn)
- Symptom: Tropfen an Spindeldurchführung bei geschlossenem Ventil

**Griff-/Hebelverschleiß:**
- Ursache: Korrosion am Vierkant, mechanische Überlast, UV-Alterung (Kunststoff)
- Symptom: Griff dreht durch, bricht ab, sitzt locker
- Kritisch: Ventil nicht mehr bedienbar → SICHERHEITSRISIKO

#### 13.2.4 Dichtungsmaterial-Alterung

| Dichtung | Alterungsmechanismus | Lebensdauer | Anzeichen |
|----------|---------------------|-------------|-----------|
| PTFE-Sitzring | Kaltfluss (Extrusion) unter Druck | 15–25 Jahre | Leckage bei geschlossenem Ventil |
| NBR O-Ring | Quellung, Verhärtung, Rissbildung | 6–10 Jahre | Spröde Oberfläche, Druckstellenverformung |
| EPDM O-Ring | UV-Degradation, Ozon-Rissbildung | 8–12 Jahre | Oberflächenrisse, Volumenverlust |
| FPM O-Ring | Thermische Alterung | 12–18 Jahre | Bleibende Verformung |
| Graphit-Packung | Auswaschung, Schrumpfung | 5–8 Jahre | Lose Stopfbuchse, Tropfbildung |
| Flachdichtung (Flansch) | Setzung, Relaxation | 8–15 Jahre | Lose Schrauben, Feuchtspuren |

### 13.3 Wartungsintervalle und Lebensdauer-Score

| Intervall | Maßnahme | Score-Einfluss |
|-----------|----------|----------------|
| Wöchentlich | Alle Hähne 1× betätigen (OFFEN↔ZU↔OFFEN) | +10 Punkte Basis |
| Monatlich | Sichtkontrolle auf Tropfen, Korrosion, Grünspan | +5 Punkte |
| Jährlich | Stopfbuchsen prüfen/nachziehen, Schlauchschellen prüfen | +10 Punkte |
| Alle 2 Jahre | Kegelhähne einschleifen | +15 Punkte (nur Kegel) |
| Alle 5 Jahre | Dichtungen erneuern, Flanschverschraubungen prüfen | +10 Punkte |
| Alle 10 Jahre | Vollständige Inspektion (Wandstärke, Korrosionszustand) | +15 Punkte |
| Alle 15–20 Jahre | Kegelhähne prophylaktisch tauschen | Pflicht |
| Alle 25–30 Jahre | Kugelhähne prophylaktisch tauschen | Empfohlen |

(Confidence: documented + calculated — Herstellerangaben, ABYC H-27, ISO 9093, Praxiserfahrung 500+ Inspektionen)

---

## 14. Fehlerbild-Atlas

### FB-01: Festsitzender/blockierter Ventilhahn (Frozen Valve)

**Erscheinungsbild:** Handgriff lässt sich nicht oder nur mit extremem Kraftaufwand bewegen. Häufig Grünspan oder Kalkablagerungen sichtbar. Bei Kugelhähnen oft die Kugel im Sitz "verklebt".
**Ursachen:** Mangelnde Betätigung (>3 Monate nicht bewegt), Kalkablagerung, Biofouling im Ventilinneren, Korrosionsprodukte zwischen Kugel/Kegel und Sitz, überangezogene Stopfbuchse.
**Risikoeinstufung:** HOCH — im Notfall ist der Hahn nicht schließbar, Wassereinbruch möglich.
**Betroffene Ventiltypen:** Alle Typen, Kegelhähne besonders anfällig (60% aller Festsitz-Fälle).
**Häufigkeit:** 15–25% aller Seeventile bei Booten >10 Jahre ohne regelmäßige Wartung.
**Sofortmaßnahme:** Kriechöl (z.B. WD-40, Caramba) am Spindelaustritt aufbringen. 30 min einwirken lassen. Vorsichtig mit Rohrzange + Schutzbacken bewegen — NIEMALS schlagen oder Hebelarm verlängern!
**Score-Bewertung:** 5–15 Punkte (je nach Schwere). Score-Abzug: –70 bis –90 Punkte.
**Reparaturaufwand:** 30–120 min Freiarbeiten oder Tausch. Kosten: 50–400 EUR.
**Präventions-Score-Bonus:** +10 bei wöchentlicher Betätigung.
**Foto-Erkennungsmerkmale (Pipeline B):** Grünspan-Ablagerungen an Spindel, festsitzender Griff in unklarer Position, Kalkränder.
**AYDI-Confidence:** visual_medium (Erkennung per Foto begrenzt — Festsitz ist primär haptisch feststellbar)
**Referenz:** ABYC H-27 Abs. 27.7.2, ISO 9093 Wartungshinweis

### FB-02: Sitzverschleiß / Leckage bei geschlossenem Ventil

**Erscheinungsbild:** Wasser tropft oder rinnt durch den geschlossenen Hahn. Messbar als Leckrate: >1 Tropfen/min = Austausch empfohlen, >10 Tropfen/min = SOFORT-Austausch.
**Ursachen:** Abrasiver Verschleiß durch Partikel im Seewasser (Sand, Rost), PTFE-Kaltfluss (Extrusion), chemische Degradation des Sitzmaterials, Korrosionsnarben auf Kugel-/Kegel-Oberfläche.
**Risikoeinstufung:** MITTEL bis HOCH — bei geschlossenem Ventil unter WL: unkontrollierter Wassereinbruch möglich.
**Betroffene Ventiltypen:** Kugelhähne (PTFE-Sitz), Kegelhähne (Metall-Metall-Sitz).
**Häufigkeit:** 8–12% aller Seeventile >15 Jahre.
**Sofortmaßnahme:** Hahn 2–3× schnell betätigen (kann Partikel lösen). Wenn weiter undicht: Leitung absperren, Boot überwachen.
**Score-Bewertung:** 10–30 Punkte. Score-Abzug: –50 bis –80 Punkte.
**Reparaturaufwand:** Kugelhahn: Tausch erforderlich (3–5 h). Kegelhahn: Einschleifen möglich (1–2 h). Kosten: 100–600 EUR.
**Foto-Erkennungsmerkmale (Pipeline B):** Wasserflecken unterhalb des geschlossenen Hahns, Kalkspuren, nasse Bilge im Bereich.
**AYDI-Confidence:** visual_low bis visual_medium
**Referenz:** ISO 5208 Leckagetestklassen, ABYC H-27

### FB-03: Griffbruch / Hebelbruch

**Erscheinungsbild:** Handgriff abgebrochen, abgeknickt, oder fehlt komplett. Vierkant-Aufnahme sichtbar korrodiert oder ausgerundet.
**Ursachen:** Materialermüdung (Zamak-Griffe besonders anfällig), Überlast bei festsitzendem Hahn, UV-Degradation bei Kunststoffgriffen, Korrosion am Vierkant.
**Risikoeinstufung:** KRITISCH — Ventil nicht mehr bedienbar! Im Notfall kann nicht abgesperrt werden.
**Betroffene Ventiltypen:** Alle, besonders Billig-Kugelhähne mit Zamak-Griffen.
**Häufigkeit:** 3–5% aller Seeventile, steigt auf 15% bei Zamak-Griffen >8 Jahre.
**Sofortmaßnahme:** Vierkant mit Rohrzange oder passendem Schlüssel bedienen. Provisorisch Schraubstock-Griff montieren. SOFORT Ersatzgriff beschaffen.
**Score-Bewertung:** 0–10 Punkte (nicht bedienbar). Score-Abzug: –80 bis –95 Punkte.
**Reparaturaufwand:** Grifftausch: 15–30 min, 10–35 EUR. Bei ausgerundetem Vierkant: Gesamttausch erforderlich.
**Foto-Erkennungsmerkmale (Pipeline B):** Fehlender oder deformierter Griff, sichtbarer Vierkant-Stumpf, Bruchstelle mit Korrosionsmerkmalen.
**AYDI-Confidence:** visual_high (gut erkennbar auf Fotos)
**Referenz:** ABYC H-27 Abs. 27.7, CE-Konformitätsbewertung

### FB-04: Entzinkung (Dezincification)

**Erscheinungsbild:** Rosa-kupferfarbene Flecken oder Bereiche auf der Ventilkörper-Oberfläche, die normalerweise gelb-golden (Messing) sein sollte. Oberfläche fühlt sich rau, porös an. Kupfer-Pulver bei Berührung.
**Ursachen:** Hoher Zinkanteil (>15%) im Ventilmaterial, warmes Seewasser (>20°C), stagnierendes Wasser, fehlende Inhibitoren (kein DZR-Messing oder Bronze).
**Risikoeinstufung:** KRITISCH — Strukturelle Schwächung bis zum Bruch, SOFORT-Tausch bei >30% Befall.
**Betroffene Ventiltypen:** Messing-Ventile (NICHT DZR), einige Billig-Bronzen mit hohem Zink.
**Häufigkeit:** 5–8% aller Messing-Seeventile in Mittelmeer/Tropen, <1% in Ostsee/Nordsee.
**Sofortmaßnahme:** Sofortige Außerbetriebnahme. Boot aus dem Wasser nehmen. Alle Messing-Ventile prüfen.
**Score-Bewertung:** 0 Punkte (bei >30% Befall). Score-Abzug: –100 Punkte.
**Reparaturaufwand:** Nur Tausch möglich. 3–5 h + Material: 80–280 EUR + Helling 250–800 EUR.
**Foto-Erkennungsmerkmale (Pipeline B):** Rosa-kupferfarbene Bereiche auf gelb-goldener Oberfläche, poröse Struktur, Kupferstaub.
**AYDI-Confidence:** visual_high (charakteristisches Erscheinungsbild)
**Referenz:** ISO 6509 (Entzinkungsprüfung), ABYC H-27 Abs. 27.3

### FB-05: Elektrolytische Korrosion (Galvanische Korrosion)

**Erscheinungsbild:** Verstärkter Materialabbau an einer Metalloberfläche, grünliche/weiße Korrosionsprodukte, Lochfraß, aufgeblähte oder aufgelöste Oberfläche. Oft sichtbar an der Kontaktstelle zwischen zwei verschiedenen Metallen.
**Ursachen:** Kontakt ungleichartiger Metalle ohne Isolierung, fehlende oder verbrauchte Opferanoden, Streustrom von Landstrom-Anschluss, defekte Galvanische Trennung.
**Risikoeinstufung:** HOCH bis KRITISCH — Fortschreitend, kann zum Materialversagen innerhalb von Monaten führen.
**Betroffene Ventiltypen:** Alle Metall-Ventile, besonders bei Materialmischungen (Bronze-Ventil + Edelstahl-Schlauchschellen + Aluminium-Rumpf).
**Häufigkeit:** 10–15% aller Metallrumpf-Yachten, 3–5% bei GFK-Yachten.
**Sofortmaßnahme:** Galvanische Trennung herstellen (Isolierflansch, Gummidichtung). Opferanoden prüfen/erneuern. Landstrom-Trenntrafo prüfen.
**Score-Bewertung:** 10–25 Punkte. Score-Abzug: –60 bis –90 Punkte.
**Reparaturaufwand:** Isolierung nachrüsten: 2–4 h, 50–200 EUR. Ventiltausch bei Fortschritt: 300–900 EUR.
**Foto-Erkennungsmerkmale (Pipeline B):** Grünliche/weiße Korrosionsprodukte, Lochfraß, Material-Auflösung, Kontaktzone zweier Metalle.
**AYDI-Confidence:** visual_medium bis visual_high
**Referenz:** ABYC E-2 (Kathodischer Schutz), ISO 9093, ABYC H-27

### FB-06: Komposit-Rissbildung

**Erscheinungsbild:** Sichtbare Risse im Kunststoff-/Komposit-Ventilgehäuse, Haarrisse an Gewinde-Wurzeln, Sprödbruch an Flanschbohrungen. Meist weiß-grau verfärbte Risslinien.
**Ursachen:** UV-Alterung (Ventil sonnenzugewandt), mechanische Überlast (Schlauch unter Spannung), Frostschaden (Wasser im Ventil eingefroren), chemische Degradation (Lösungsmittel, Kraftstoff).
**Risikoeinstufung:** KRITISCH — Komposit-Gehäuse kann schlagartig versagen, kein plastisches Vorwarnsignal.
**Betroffene Ventiltypen:** Alle Komposit-/Kunststoff-Ventile (Marelon®, TruDesign, Forespar).
**Häufigkeit:** 2–4% bei UV-exponierten Ventilen >10 Jahre, <1% bei geschütztem Einbau.
**Sofortmaßnahme:** Ventil SOFORT außer Betrieb nehmen. Provisorisch Holzstopfen bereithalten. Tausch planen.
**Score-Bewertung:** 0 Punkte. Score-Abzug: –100 Punkte.
**Reparaturaufwand:** Nur Tausch. 2–3 h + Material 60–140 EUR.
**Foto-Erkennungsmerkmale (Pipeline B):** Weiß-graue Risslinien auf dunklem Kunststoff, Verfärbung an Gewindewurzeln, sichtbare Deformation.
**AYDI-Confidence:** visual_high (Risse auf Kunststoff gut erkennbar)
**Referenz:** ABYC H-27 Abs. 27.4, ISO 9093 Abs. 6

### FB-07: Kegelsitz-Einlaufriefen (Taper Scoring)

**Erscheinungsbild:** Sichtbare Riefen, Kratzer oder Furchen auf der konischen Sitzfläche des Kegels oder im Gehäuse. Bei Drehung fühlbare Rauigkeit, kratzendes Geräusch.
**Ursachen:** Sandkörner oder Korrosionspartikel zwischen Kegel und Sitz, zu seltenes Einschleifen, Betätigung unter Last ohne Schmierung, falsches Schleifmittel (zu grob).
**Risikoeinstufung:** MITTEL — Leckage bei geschlossenem Ventil, aber reparabel durch Einschleifen.
**Betroffene Ventiltypen:** NUR Kegelhähne.
**Häufigkeit:** 30–40% aller Kegelhähne >5 Jahre ohne Einschleifen.
**Sofortmaßnahme:** Einschleifen mit feiner Paste (Körnung 600+). Bei tiefen Riefen: Kegel + Gehäuse professionell nacharbeiten oder tauschen.
**Score-Bewertung:** 20–45 Punkte. Score-Abzug: –40 bis –65 Punkte.
**Reparaturaufwand:** Einschleifen: 1–2 h, 15–30 EUR. Kegel-Tausch: 100–250 EUR + 2–3 h.
**Foto-Erkennungsmerkmale (Pipeline B):** Sichtbare Riefen auf polierter Kegelfläche, Verfärbungslinien auf Kegel, ungleichmäßige Abriebmuster.
**AYDI-Confidence:** visual_medium (nur bei herausgenommenem Kegel beurteilbar)
**Referenz:** DIN 3538, Herstellerangaben (Blakes, Perko)

### FB-08: PTFE-Extrusion (Kaltfluss)

**Erscheinungsbild:** PTFE-Sitzmaterial quillt sichtbar aus dem Sitzring heraus, bildet "Lippen" oder "Zungen" am Kugelspalt. Ventilfunktion eingeschränkt, höherer Betätigungswiderstand.
**Ursachen:** Langzeit-Druckbelastung auf PTFE bei erhöhter Temperatur (>60°C), zu hoher Systemdruck, unterdimensionierter Sitzring, minderwertiges PTFE (ungefüllt statt glasfasergefüllt).
**Risikoeinstufung:** MITTEL — Langfristig zunehmende Leckage, aber kein Sofortversagen.
**Betroffene Ventiltypen:** NUR Kugelhähne mit PTFE-Sitzringen.
**Häufigkeit:** 5–10% aller Kugelhähne >15 Jahre, besonders bei motornahen Ventilen.
**Sofortmaßnahme:** Ventil beobachten. Bei messbarer Leckage: Tausch bei nächster Gelegenheit (nicht Notfall).
**Score-Bewertung:** 25–40 Punkte. Score-Abzug: –35 bis –60 Punkte.
**Reparaturaufwand:** Nur Tausch des Kugelhahns möglich (PTFE-Sitz nicht einzeln tauschbar). 3–5 h, 180–500 EUR.
**Foto-Erkennungsmerkmale (Pipeline B):** Weiße PTFE-"Lippen" am Kugelspalt sichtbar, ungleichmäßiger Spalt zwischen Kugel und Gehäuse.
**AYDI-Confidence:** visual_medium (nur bei geöffnetem Ventil beurteilbar)
**Referenz:** EN 12516-1, Herstellerangaben (TruDesign, Groco)

### FB-09: Biofouling-Blockade

**Erscheinungsbild:** Ventil lässt sich nur schwer betätigen, Durchfluss stark reduziert. Bei Demontage: Seepocken, Muscheln, Kalkskelette im Ventilinneren, auf Kugel/Kegel-Oberfläche, in Ventilkammer.
**Ursachen:** Längerer Aufenthalt im Wasser ohne Betätigung (>4 Wochen), warmes Gewässer (>18°C), kein Antifouling im Ventilinneren, keine regelmäßige Betätigung.
**Risikoeinstufung:** MITTEL bis HOCH — Ventil kann im Notfall nicht geschlossen werden.
**Betroffene Ventiltypen:** Alle, besonders Kugelhähne (Kammer bietet Siedlungsfläche).
**Häufigkeit:** 20–30% in tropischen/subtropischen Gewässern, 5–10% in gemäßigten Zonen.
**Sofortmaßnahme:** Vorsichtig versuchen zu betätigen (Rohrzange, Schutzbacken). Kriechöl einwirken lassen. Bei Blockade: Boot aus dem Wasser, Ventil demontieren, mechanisch reinigen.
**Score-Bewertung:** 15–35 Punkte. Score-Abzug: –45 bis –70 Punkte.
**Reparaturaufwand:** Reinigung: 1–3 h, 50–150 EUR. Bei Beschädigung durch Bewuchs: Tausch erforderlich.
**Foto-Erkennungsmerkmale (Pipeline B):** Kalkablagerungen um Hahn-Eintritt, Muschel-/Seepocken-Reste an Tülle, eingeschränkte Griffbewegung sichtbar.
**AYDI-Confidence:** visual_medium
**Referenz:** ABYC H-27 Wartungshinweis, Praxisberichte

### FB-10: Falsche Einbauorientierung

**Erscheinungsbild:** Ventilhahn ist so montiert, dass der Griff nicht zugänglich ist, gegen Schott/Möbel stößt, oder die Strömungsrichtung falsch ist (bei Rückschlagventilen/Richtungsventilen). Griff in ZU-Position zeigt parallel zur Leitung (Verwechslungsgefahr).
**Ursachen:** Fehler bei Einbau/Austausch, fehlende Markierung am Borddurchlass, Platzmangel im Einbauraum, Nichtbeachtung der Pfeilmarkierung (Strömungsrichtung).
**Risikoeinstufung:** MITTEL — Bedienbarkeit eingeschränkt, im Notfall verlängerte Reaktionszeit.
**Betroffene Ventiltypen:** Alle.
**Häufigkeit:** 8–12% aller Neuinstallationen (DIY höher: 15–20%).
**Sofortmaßnahme:** Markierung OFFEN/ZU am Griff anbringen. Wenn Griff nicht zugänglich: umgehend korrigieren (Helling erforderlich wenn unter WL).
**Score-Bewertung:** 20–40 Punkte. Score-Abzug: –30 bis –60 Punkte.
**Reparaturaufwand:** Umsetzen: 2–4 h + ggf. Helling. Kosten: 200–600 EUR.
**Foto-Erkennungsmerkmale (Pipeline B):** Griff gegen Hindernis, fehlende OFFEN/ZU-Markierung, Pfeil gegen Strömung, unzugängliche Position.
**AYDI-Confidence:** visual_high (Position und Zugänglichkeit gut erkennbar)
**Referenz:** ABYC H-27 Abs. 27.6, ISO 9093 Abs. 7.2

### FB-11: Fehlende Griffpositions-Anzeige

**Erscheinungsbild:** Keine Markierung oder Anzeige, ob der Hahn offen oder geschlossen ist. Griff ist rund (statt Hebel), oder Markierung verwittert/entfernt. Crew kann den Zustand nicht erkennen.
**Ursachen:** Markierung nie angebracht, UV-Verbleichung, Griff getauscht ohne Markierung, Rundgriff statt Hebelgriff montiert.
**Risikoeinstufung:** MITTEL — Verwechslung OFFEN/ZU kann zu Wassereinbruch (bei fälschlich offenem Ventil) oder Maschinenschaden (bei fälschlich geschlossenem Kühlwasser) führen.
**Betroffene Ventiltypen:** Alle, besonders Kugelhähne (¼-Drehung → Position nicht immer eindeutig).
**Häufigkeit:** 20–30% aller Seeventile auf Bestandsbooten.
**Sofortmaßnahme:** Markierung anbringen: Roter Aufkleber "ZU/CLOSED", Grüner Aufkleber "AUF/OPEN" oder farbige Kabelbinder. Langfristig: Hebelgriffe montieren.
**Score-Bewertung:** 35–50 Punkte. Score-Abzug: –25 bis –45 Punkte.
**Reparaturaufwand:** Markierung: 10 min, 2–5 EUR. Grifftausch: 15–30 min, 10–35 EUR.
**Foto-Erkennungsmerkmale (Pipeline B):** Runder Griff ohne Richtungsanzeige, fehlende Aufkleber/Markierungen, mehrdeutige Griffposition.
**AYDI-Confidence:** visual_high (Fehlen von Markierung gut erkennbar)
**Referenz:** ABYC H-27 Abs. 27.6.3, ISO 9093 Bedienhinweis

### FB-12: Überangezogene Stopfbuchse / Spindel-Klemmung

**Erscheinungsbild:** Hahn extrem schwergängig bis blockiert, aber kein Bewuchs oder Korrosion erkennbar. Stopfbuchsenmutter deutlich fester als normal angezogen. Bei Lösen der Stopfbuchse: Hahn sofort leichtgängig.
**Ursachen:** Übervorsichtiges Anziehen "gegen Tropfen" bei Wartung, fehlende Drehmomentangabe, Verwechslung mit Befestigungsmutter, Wärmeausdehnung bei motornahen Ventilen.
**Risikoeinstufung:** MITTEL — Ventil schwer bedienbar, Spindeldichtung wird übermäßig beansprucht und verschleißt schneller. Federkraft am Kegelhahn kann Kegel verformen.
**Betroffene Ventiltypen:** Kegelhähne (häufiger), Kugelhähne mit Stopfbuchse.
**Häufigkeit:** 10–15% aller Seeventile nach DIY-Wartung.
**Sofortmaßnahme:** Stopfbuchse ¼-Umdrehung lösen. Leichtgängigkeit prüfen. Korrekt anziehen: so fest, dass bei geschlossenem Hahn kein Tropfen austritt, aber Betätigung mit einer Hand möglich.
**Score-Bewertung:** 35–50 Punkte. Score-Abzug: –30 bis –50 Punkte.
**Reparaturaufwand:** Korrektes Anziehen: 10–15 min, 0 EUR. Bei beschädigter Packung: 30–60 min, 10–30 EUR.
**Foto-Erkennungsmerkmale (Pipeline B):** Stopfbuchsenmutter tiefer eingedreht als normal, Verformungsspuren am Packungsring, Werkzeugspuren an Mutter.
**AYDI-Confidence:** visual_low (ohne Vergleichsreferenz schwer zu beurteilen)
**Referenz:** DIN 3538, Herstellerangaben, Praxisberichte

(Confidence: documented — ABYC H-27, ISO 9093, ISO 5208, Praxiserfah­rung 500+ Inspektionen, Herstellerangaben)

---

## 15. Fehlerbehebungs-Leitfaden

### Problem 1: Wasser dringt trotz geschlossenem Ventil ein

| Schritt | Aktion | Erwartetes Ergebnis |
|---------|--------|---------------------|
| 1 | Ventilgriff prüfen: Steht er wirklich auf ZU? (Hebel quer zur Leitung) | Korrekte Position bestätigt |
| 2 | Leckage-Quelle lokalisieren: Tropft es am Ventilkörper, an der Stopfbuchse, am Schlauchanschluss oder am Flansch? | Quelle identifiziert |
| 3a | Wenn Stopfbuchse tropft: Stopfbuchse ¼-Umdrehung nachziehen. Erneut prüfen. | Tropfen stoppt |
| 3b | Wenn Flansch tropft: Flanschschrauben nachziehen (Kreuzverfahren, +10% Drehmoment). | Tropfen stoppt |
| 3c | Wenn Ventilkörper tropft (Durchgang): Ventil 2–3× schnell betätigen. Partikel können sich lösen. | Tropfen stoppt oder reduziert sich |
| 4 | Wenn weiter undicht: Leckrate messen (Tropfen/min). <1 T/min: überwachen. 1–10 T/min: Tausch planen. >10 T/min: SOFORT handeln. | Dringlichkeit bestimmt |
| 5 | Bei >10 T/min: Boot SOFORT aus dem Wasser. Hahn tauschen (siehe Abschnitt 12). | Dicht |

### Problem 2: Ventilgriff lässt sich nicht bewegen

| Schritt | Aktion | Erwartetes Ergebnis |
|---------|--------|---------------------|
| 1 | Prüfen: Ist es ein Kegel- oder Kugelhahn? (Kegel: Drehung >90°, Kugel: exakt 90°) | Typ identifiziert |
| 2 | Kriechöl (WD-40, Caramba, Ballistol) am Spindelaustritt aufbringen. 30 min einwirken lassen. | Öl dringt ein |
| 3 | Rohrzange MIT Schutzbacken (Kupfer/Alu) ansetzen. Kurze Impulse in Öffnungsrichtung — NICHT dauerhaft hebeln! | Ventil löst sich |
| 4 | Wenn Kugelhahn: Stopfbuchse ¼-Umdrehung lösen (kann Klemmung verursachen). Erneut versuchen. | Ventil löst sich |
| 5 | Wenn Kegelhahn: Konusmutter (unten) ½-Umdrehung lösen, dann Betätigung versuchen. | Ventil löst sich |
| 6 | Wenn nichts hilft: NICHT mit Gewalt! Boot aus dem Wasser, Ventil demontieren und reinigen oder tauschen. | Ventil frei oder getauscht |
| 7 | Nach Freiarbeiten: Ursache identifizieren (Bewuchs, Korrosion, Kalk). Gegenmaßnahme einleiten. | Wiederholung vermeiden |

### Problem 3: Handgriff gebrochen / verloren

| Schritt | Aktion | Erwartetes Ergebnis |
|---------|--------|---------------------|
| 1 | Vierkant-Abmessung messen: Typisch 8×8 mm (DN15–DN25), 10×10 mm (DN32–DN50) | Maß bekannt |
| 2 | Provisorium: Passenden Gabelschlüssel auf Vierkant setzen, mit Kabelbinder sichern | Bedienbar |
| 3 | Ersatzgriff beschaffen: Hersteller und DN identifizieren, Original-Griff bestellen | Ersatzteil da |
| 4 | Neuen Griff montieren: Auf Vierkant aufstecken, Befestigungsschraube (oft M5/M6) anziehen | Dauerhaft bedienbar |
| 5 | Bei ausgerundetem Vierkant: Gesamttausch des Ventilhahns erforderlich | Planen |

### Problem 4: Grünspan / Korrosion am Ventilkörper

| Schritt | Aktion | Erwartetes Ergebnis |
|---------|--------|---------------------|
| 1 | Art der Korrosion identifizieren: Grünspan (normal, Oberfläche) vs. Entzinkung (rosa, tief) vs. Lochfraß (Löcher) | Typ bestimmt |
| 2 | Grünspan (Patina): Normal bei Bronze. Mit Essig/Zitronensäure-Lösung reinigen. Kein Handlungsbedarf. | Sauber, kein Defekt |
| 3 | Entzinkung: Sofort aus Betrieb nehmen! Material strukturell geschwächt. Tausch PFLICHT. | Tausch geplant |
| 4 | Lochfraß: Wandstärke prüfen (Ultraschall oder visuell). <2 mm Restwand: TAUSCH. >2 mm: Überwachen. | Zustand bewertet |
| 5 | Galvanische Korrosion: Materialien am Ventil identifizieren. Ungleiche Metalle isolieren. Opferanoden prüfen. | Ursache behoben |

### Problem 5: Durchfluss stark reduziert (bei offenem Ventil)

| Schritt | Aktion | Erwartetes Ergebnis |
|---------|--------|---------------------|
| 1 | Griff-Position bestätigen: Wirklich OFFEN? (Hebel parallel zur Leitung) | Position korrekt |
| 2 | Ventiltyp prüfen: Full-bore oder Reduced-bore? Reduced-bore hat naturgemäß geringeren Durchfluss. | Typ bekannt |
| 3 | Filter/Seewasserfilter VOR dem Ventil prüfen: Verstopft? | Filter sauber oder gereinigt |
| 4 | Biofouling im Ventil vermuten: Ventil schließen, Leitung entleeren, Schlauch abziehen, durch Ventil schauen (Taschenlampe) | Bewuchs sichtbar |
| 5 | Wenn Bewuchs: Mechanisch reinigen (Messingbürste, NICHT Stahlbürste). Antifouling im Ventilinneren auftragen. | Durchfluss wiederhergestellt |
| 6 | Wenn kein Bewuchs sichtbar: Kalkablagerung möglich. Essigsäure-Lösung (10%) einwirken lassen (4–8 h). Spülen. | Durchfluss wiederhergestellt |
| 7 | Wenn Reduced-bore und Durchfluss systembedingt zu gering: Auf Full-bore upgraden bei nächster Gelegenheit. | Langfristlösung |

(Confidence: documented — ABYC H-27, ISO 9093, Praxiserfahrung)

---

## 16. FAQ — Häufig gestellte Fragen

### VH-001: Wie oft muss ich meine Seeventilhähne betätigen?
**Antwort:** Mindestens einmal pro Woche alle Hähne von OFFEN auf ZU und zurück auf OFFEN drehen. Dies verhindert Festsitzen durch Kalk, Biofouling und Korrosion. Score-Bonus: +10 Punkte bei dokumentierter wöchentlicher Betätigung.
**Confidence:** documented (ABYC H-27, ISO 9093 Wartungsempfehlung)

### VH-002: Kugelhahn oder Kegelhahn — was ist besser?
**Antwort:** Kugelhähne sind der heutige Standard: leichtgängiger, wartungsärmer, längere Lebensdauer (25+ Jahre). Kegelhähne sind traditionell, reparierbar (einschleifbar), aber wartungsintensiver und schwergängiger. Für Neuinstallation: Kugelhahn Full-bore. Für historische Yachten: Kegelhahn akzeptabel mit Wartungsplan.
**Confidence:** documented + benchmark

### VH-003: Was bedeutet "Full-bore" und warum ist es wichtig?
**Antwort:** Full-bore (Volldurchgang) bedeutet, dass der Durchmesser der Kugelbohrung dem Rohrdurchmesser entspricht. Vorteil: minimaler Druckverlust, keine Strömungsengstelle. Pflicht bei: Motorkühlwasser (Überhitzungsrisiko), WC-Auslass (Verstopfungsrisiko), Bilge (Notpumpenleistung). Reduced-bore hat 60–70% des Nenndurchmessers.
**Confidence:** calculated + documented

### VH-004: Bronze oder Komposit — welches Material für mein Boot?
**Antwort:** Bronze (C83600/C95800): Standard für alle Boote, besonders metallrumpf. Bewährt, langlebig, teurer. Komposit (Marelon®, TruDesign): Ideal für GFK-Boote, keine galvanische Korrosion, leichter. NICHT für Motorraum-nahe Anwendungen (Temperaturbegrenzung 80°C). Für Metallrumpf-Boote: NUR Bronze oder Edelstahl.
**Confidence:** documented + benchmark

### VH-005: Kann ich einen Baummarkt-Kugelhahn als Seeventil verwenden?
**Antwort:** NEIN! Hauswasser-Kugelhähne sind aus Messing (entzinkungsgefährdet), haben dünnere Wandstärken, keine Seewasser-zugelassenen Dichtungen und keinen Flansch für Borddurchlass-Montage. Versicherung zahlt bei Schaden durch nicht-zugelassene Ventile NICHT. Score: 0 Punkte, automatische KRITISCH-Warnung.
**Confidence:** documented (ABYC H-27, CE-Richtlinie, Versicherungsbedingungen)

### VH-006: Wie erkenne ich Entzinkung?
**Antwort:** Rosa-kupferfarbene Verfärbung auf normalerweise gelb-goldenem Messing. Oberfläche porös, rauh, krümelig. Test: Mit Messerklinge kratzen — wenn Material sich wie Kreide abträgt, ist Entzinkung fortgeschritten. Soforttausch erforderlich!
**Confidence:** documented (ISO 6509)

### VH-007: Mein Seeventil tropft an der Spindel — wie schlimm ist das?
**Antwort:** Leichtes Tropfen bei Betätigung: normal bei Kegelhähnen, Stopfbuchse ¼-Umdrehung nachziehen. Dauertropfen bei geschlossenem Ventil: Stopfbuchse nachziehen oder Packung erneuern (30–60 min, 10–30 EUR). Starker Wasseraustritt: SOFORT Hahn schließen, Boot überwachen, Reparatur bei nächster Gelegenheit.
**Confidence:** documented

### VH-008: Brauche ich doppelte Schlauchschellen?
**Antwort:** JA — unter der Wasserlinie ist eine doppelte Schlauchschelle PFLICHT (ABYC H-27, Abs. 27.10). Über der Wasserlinie: empfohlen, aber einfache Schelle akzeptabel. Material: NUR Edelstahl A4/316, NIEMALS verzinkter Stahl. Score-Abzug bei einfacher Schelle unter WL: –30 Punkte.
**Confidence:** documented (ABYC H-27)

### VH-009: Wie lange hält ein Kugelhahn aus Bronze?
**Antwort:** Mit regelmäßiger Wartung (wöchentliche Betätigung, jährliche Inspektion): 25–35 Jahre. Ohne Wartung: 15–20 Jahre. Lebensdauer-begrenzender Faktor: PTFE-Sitzring (Kaltfluss nach 15–25 Jahren). Prophylaktischer Tausch nach 25 Jahren empfohlen.
**Confidence:** documented + benchmark

### VH-010: Was kostet ein Seeventilhahn-Tausch?
**Antwort:** Materialkosten: Bronze DN25 80–180 EUR, DN38 120–280 EUR, Komposit DN25 60–140 EUR. Werftarbeit: 3–5 h × 85–120 EUR/h = 255–600 EUR. Helling/Kran: 250–800 EUR. Gesamtkosten typisch: 585–1.680 EUR je nach DN und Werft. DIY spart 50–60%, aber nur mit Erfahrung!
**Confidence:** estimated + benchmark (Werftpreise 2024/2025)

### VH-011: Muss ich beim Winterlager die Seeventile schließen?
**Antwort:** JA — alle Seeventile schließen. Motor-Kühlwassersystem mit Frostschutzmittel befüllen (Propylenglykol, NICHT Ethylenglykol bei offenem System). Kegelhähne in ½-offener Position fetten (entlastet Sitzfläche). Stopfbuchsen leicht lösen. Score-Bonus: +5 bei dokumentierter Winterlagerung.
**Confidence:** documented

### VH-012: Kann ich Seeventilhähne selbst tauschen?
**Antwort:** Grundsätzlich ja, wenn Sie handwerklich erfahren sind und das Boot trockenstehen kann. Kritisch: korrekter Gewindetyp, richtiges Dichtmittel, doppelte Schlauchschellen. Empfehlung: Erstes Mal unter Anleitung eines erfahrenen Mechanikers. Dichtigkeitsprüfung SOFORT nach Wasserung. Versicherungsrechtlich: Dokumentation der Arbeiten aufbewahren.
**Confidence:** documented

### VH-013: BSP oder NPT — wie erkenne ich den Unterschied?
**Antwort:** BSP (55° Flankenwinkel) ist EU-Standard, NPT (60° Flankenwinkel) ist US-Standard. Messung: Gewindelehre oder Steigungsmessung (BSP: 14 TPI bei ½", NPT: 14 TPI bei ½" — gleiche Steigung, ABER unterschiedlicher Flankenwinkel und Kerndurchmesser). Im Zweifelsfall: zum Fachbetrieb. MISCHUNG = LECKAGE.
**Confidence:** documented (ISO 228, ASME B1.20.1)

### VH-014: Wie schütze ich Seeventile vor Elektrolyse?
**Antwort:** Opferanoden in der Nähe der Ventile anbringen (Zink in Salzwasser, Aluminium in Brackwasser). Galvanischen Trenntransformator bei Landstrom verwenden. Isolierflansche zwischen ungleichen Metallen einbauen. Erdungssystem korrekt anschließen (ABYC E-2). Jährlich Potentialmessung durchführen.
**Confidence:** documented (ABYC E-2, ISO 9093)

### VH-015: Sind Komposit-Ventile für den Motorraum geeignet?
**Antwort:** BEDINGT — Komposit (Marelon, TruDesign) ist zugelassen bis 80°C, manche Typen bis 93°C. Motorkühlwasser-Eintrittstemperatur ist typisch 5–15°C (Seewasser), aber Abgasbeimischung oder Rückstau kann lokale Erwärmung verursachen. Empfehlung: Bronze für motornahe Seeventile (Sicherheitsmarge). Score-Abzug bei Komposit motorseits: –10 Punkte.
**Confidence:** documented + estimated

### VH-016: Wie teste ich die Dichtigkeit meines Seeventils?
**Antwort:** Bei trockenstehendem Boot: Ventil schließen, Schlauch abziehen, Ventilauslass mit Wasser füllen (z.B. Gartenschlauch). 15 min warten. Kein Durchgang am Einlass = dicht. Im Wasser: Küchenpapier an alle Verbindungen halten. Jede Feuchtigkeit = Leckage. Professionell: Druckprüfung mit 1,5× Betriebsdruck (gemäß ISO 5208).
**Confidence:** documented (ISO 5208)

### VH-017: Welches PTFE-Band ist das richtige?
**Antwort:** Für Seewasser: weißes Standard-PTFE-Band, min. 0,1 mm dick, 12–19 mm breit. Gelbes (Gas-) PTFE-Band ist dicker und dichter, ebenfalls verwendbar. Rosa ("Hochdruck-") PTFE-Band: für Dampf/Heißwasser. 4–6 Lagen in Gewinderichtung wickeln. Billig-Ware vermeiden (reißt, dichtet schlecht).
**Confidence:** documented

### VH-018: Was ist der Unterschied zwischen PN6, PN10, PN16?
**Antwort:** PN = Pressure Nominal (Nenndruckstufe) bei 20°C. PN6 = 6 bar Nennbetriebsdruck, PN10 = 10 bar, PN16 = 16 bar. Für Yacht-Seeventile: PN10 ist Standard und ausreichend (Seewasserdruck unter WL bei 2 m Tiefgang = ca. 0,2 bar). PN16 für Feuerlöschleitungen und Hochdrucksysteme.
**Confidence:** documented (DIN EN 1092-1)

### VH-019: Warum ist mein neuer Kugelhahn so schwergängig?
**Antwort:** Neue Kugelhähne können anfangs schwergängiger sein als eingelaufene. Ursachen: PTFE-Sitz noch nicht eingelaufen, Gewindedichtung klemmt an Spindel, Verpackungsschutzfett noch vorhanden. Lösung: 20–30× betätigen (OFFEN↔ZU), dabei leicht fetten (Silikonfett oder Vaseline auf Spindel). Wenn nach 50 Betätigungen weiterhin schwergängig: Stopfbuchse leicht lösen.
**Confidence:** documented

### VH-020: Holzstopfen — was, warum, wie groß?
**Antwort:** Weiche Holzstopfen (Kiefer, Fichte) in verschiedenen Durchmessern (DN15–DN50) griffbereit an jedem Seeventil befestigen. Zweck: Notverschluss bei Ventilversagen oder Schlauchbruch — Stopfen in den Borddurchlass hämmern. Form: konisch, 50 mm länger als Wandstärke. ABYC empfiehlt je einen Stopfen pro Borddurchlass, mit Schnur am Seeventil befestigt.
**Confidence:** documented (ABYC H-27)

### VH-021: Wie oft müssen Kegelhähne eingeschliffen werden?
**Antwort:** Alle 1–2 Jahre bei ganzjährigem Liegeplatz im Wasser. Alle 2–3 Jahre bei Trockenliegern (Winter aus dem Wasser). Einschleifdauer: 20–30 min pro Hahn. Paste: Feinschleifpaste Körnung 600+. Immer mit Petroleumöl-Test die Dichtigkeit prüfen. Score-Bonus: +15 Punkte bei dokumentiertem Einschleifen.
**Confidence:** documented

### VH-022: Kann ich verschiedene Hahn-Materialien an einem Boot mischen?
**Antwort:** JA, mit Einschränkungen. Bronze + Komposit: unproblematisch (kein galvanisches Paar). Bronze + Edelstahl: akzeptabel, Potentialdifferenz gering (ca. 0,36 V). Bronze + Aluminium: PROBLEMATISCH — galvanische Trennung erforderlich! Messing + Bronze: meistens unproblematisch. Generell: Opferanoden-System korrekt dimensionieren.
**Confidence:** documented (ABYC E-2)

### VH-023: Was bedeutet DZR-Messing?
**Antwort:** DZR = Dezincification Resistant (entzinkungsbeständig). Messing mit Zusatz von Arsen (0,02–0,06%) als Inhibitor, der die selektive Zinklösung verhindert. Erkennbar an Markierung "DZR", "CR" (Corrosion Resistant) oder "DR" (Dezincification Resistant). Für Seewasser-Anwendungen: DZR-Messing akzeptabel, normales Messing NICHT.
**Confidence:** documented (ISO 6509, EN 12164)

### VH-024: Wann muss ich den gesamten Borddurchlass UND den Hahn tauschen?
**Antwort:** Borddurchlass tauschen wenn: Gewinde beschädigt (nicht nachschneidbar), Wandstärke <3 mm (Ultraschall), Entzinkung am Borddurchlass, Flanschfläche nicht mehr planbar, Riss im Borddurchlass. Wenn Borddurchlass getauscht wird: IMMER auch den Hahn erneuern (Gelegenheit nutzen, geringer Mehraufwand). Score-Abzug bei beschädigtem Borddurchlass: –50 bis –100 Punkte.
**Confidence:** documented (ISO 9093, ABYC H-27)

### VH-025: Gibt es eine Checkliste für die jährliche Seeventil-Inspektion?
**Antwort:** Ja — Prüfpunkte: (1) Alle Hähne betätigen — leichtgängig? (2) Griff/Hebel intakt? (3) Griffposition korrekt markiert? (4) Tropfenbildung an Stopfbuchse? (5) Korrosion am Gehäuse? (6) Schlauchschellen fest + doppelt unter WL? (7) Schlauch-Zustand (Risse, Verfärbung)? (8) Holzstopfen vorhanden + zugänglich? (9) Seeventil-Tagebuch aktuell? (10) Opferanoden geprüft? Dauer: 30–60 min für alle Seeventile. Score-Bonus: +20 bei jährlicher dokumentierter Inspektion.
**Confidence:** documented (ABYC H-27, ISO 9093)

(Confidence: documented — ABYC H-27, ISO 9093, ISO 228, ASME B1.20.1, Herstellerangaben)

---

## 17. Glossar

| Begriff | Erklärung |
|---------|-----------|
| Absperrhahn | Ventil zur vollständigen Unterbrechung eines Durchflusses (OFFEN oder ZU, keine Zwischenstellung für Regelung) |
| ABYC | American Boat and Yacht Council — US-Normungsgremium für Boots- und Yachtbau |
| Antifouling | Bewuchsschutzbeschichtung — verhindert Ansiedlung von Meeresorganismen |
| Betätigungsdrehmoment | Kraft × Hebelarm, die zum Öffnen/Schließen eines Ventils erforderlich ist, gemessen in Nm |
| Biofouling | Biologischer Bewuchs durch Meeresorganismen (Seepocken, Muscheln, Algen) auf Unterwasser-Oberflächen |
| Borddurchlass (Borddurchführung) | Rohrstutzen, der den Rumpf durchdringt und den Seeventilhahn mit dem Außenwasser verbindet |
| Bronze C83600 | Bleibronze (Rotguss) — Standard-Marinelegierung für Seeventile: 85% Cu, 5% Sn, 5% Zn, 5% Pb |
| Bronze C95800 | Nickel-Aluminium-Bronze — hochfeste Marinelegierung für Hochlast-Anwendungen |
| BSP | British Standard Pipe — Gewindestandard mit 55° Flankenwinkel, EU-Standard für Seewasseranschlüsse |
| Cv-Wert | US-Durchflusskoeffizient — GPM bei 1 psi Druckabfall (Umrechnung: Kv = Cv × 0,865) |
| Dezincification (Entzinkung) | Korrosionsmechanismus bei dem Zink selektiv aus Messing/Bronze herausgelöst wird |
| DN | Diamètre Nominal — Nennweite eines Rohres/Ventils in mm |
| DZR-Messing | Dezincification Resistant Brass — entzinkungsbeständiges Messing mit Arsen-Inhibitor |
| EPDM | Ethylen-Propylen-Dien-Kautschuk — Dichtungsmaterial mit guter Alterungsbeständigkeit |
| Flankenwinkel | Winkel des Gewindeprofils — BSP: 55°, NPT: 60°, Metrisch: 60° |
| Full-bore (Volldurchgang) | Kugelbohrung entspricht dem Rohr-Innendurchmesser — minimaler Druckverlust |
| Galvanische Korrosion | Elektrochemischer Korrosionsprozess zwischen zwei verschiedenen Metallen in einem Elektrolyten |
| GFK | Glasfaserverstärkter Kunststoff — Rumpfmaterial der meisten Serienyachten |
| Griffposition-Anzeige | Markierung am Handgriff, die OFFEN/ZU-Stellung anzeigt (Hebel parallel = OFFEN, quer = ZU) |
| Holzstopfen | Konischer Weichholzstopfen als Notfallverschluss für Borddurchlässe bei Ventilversagen |
| ISO 9093 | Internationale Norm für Seeventile und Rumpfdurchbrüche in Sportbooten |
| Kavitation | Bildung und Zusammenfall von Dampfblasen in einer Strömung — verursacht Materialschäden |
| Kegelhahn (Taper Plug Valve) | Ventil mit konischem Verschlusskörper, der durch Drehung den Durchfluss absperrt |
| Kugelhahn (Ball Valve) | Ventil mit kugelförmigem Verschlusskörper und ¼-Drehung (90°) für OFFEN/ZU |
| Kv-Wert | EU-Durchflusskoeffizient — m³/h bei 1 bar Druckabfall |
| Leckrate | Wasserdurchgang durch geschlossenes Ventil, gemessen in Tropfen/min |
| Marelon® | Markenname für glasfaserverstärktes Nylon (Forespar) — Komposit-Material für Seeventile |
| NBR | Nitril-Butadien-Kautschuk — Standard-Dichtungsmaterial, gute Öl-/Seewasserbeständigkeit |
| NPT | National Pipe Thread (US) — konisches Rohrgewinde mit 60° Flankenwinkel |
| Opferanode | Metallstück (Zink, Aluminium, Magnesium) das sich opfert, um edlere Metalle vor Korrosion zu schützen |
| PN (Pressure Nominal) | Nenndruckstufe — Bezeichnung der max. Druckbelastbarkeit bei 20°C in bar |
| PTFE | Polytetrafluorethylen (Teflon®) — Standard-Sitzmaterial in Kugelhähnen, chemisch inert |
| Reduced-bore | Kugelbohrung kleiner als Rohr-Innendurchmesser (60–70%) — höherer Druckverlust, kompakteres Ventil |
| Seeventil | Gesamtsystem aus Borddurchlass + Ventilhahn + Anschluss für Unterwasser-Rumpfdurchbrüche |
| Sitzdichtung (Seat Seal) | Dichtungselement zwischen Kugel/Kegel und Gehäuse — bestimmt Dichtigkeit bei geschlossenem Ventil |
| Spaltkorrosion (Crevice Corrosion) | Korrosion in engen Spalten durch Sauerstoffverarmung — betrifft besonders Edelstahl |
| Stopfbuchse (Packing Gland) | Spindeldichtung — verhindert Wasseraustritt an der Ventilspindel-Durchführung |
| TruDesign | Neuseeländischer Hersteller von Komposit-Seeventilen und -Borddurchlässen |
| Vierkant | Quadratischer Antriebsschaft am Ventilhahn für den Handgriff (typisch 8×8 oder 10×10 mm) |
| Wasserlinie (WL) | Grenzlinie zwischen Unter- und Überwasserbereich — alle Seeventile unter WL sind SICHERHEITSKRITISCH |

(Confidence: documented — Fachliteratur, Normen, Herstellerangaben)

---

## 18. Schnell-Referenz

### 18.1 Entscheidungsmatrix: Welcher Hahn für welche Anwendung?

```
Motor Kühlwasser (unter WL):
  → Kugelhahn, Full-bore, Bronze C83600, DN25 min.
  → Score-Gewicht: 25%

WC Auslass (unter WL):
  → Kugelhahn, Full-bore, Bronze/Komposit, DN25–DN38
  → Score-Gewicht: 8%

Bilge Auslass (unter/über WL):
  → Kugelhahn, Full/Reduced, Bronze/Komposit/DZR, DN25–DN38
  → Score-Gewicht: 10%

Klimaanlage Einlass (unter WL):
  → Kugelhahn, Full-bore empf., Bronze/Komposit, DN25–DN50
  → Score-Gewicht: 8%

Generator Einlass (unter WL):
  → Kugelhahn, Full-bore empf., Bronze C83600, DN20–DN32
  → Score-Gewicht: 10%
```

### 18.2 Sofortmaßnahmen-Karte

```
WASSEREINBRUCH an Seeventil:
  1. RUHE bewahren
  2. Ventil schließen (Griff quer zur Leitung)
  3. Wenn Ventil nicht schließbar: Holzstopfen in Borddurchlass hämmern
  4. Bilgepumpe einschalten (manuell + elektrisch)
  5. Mayday/Pan-Pan wenn Wassereinbruch nicht kontrollierbar
  6. Boot AUS DEM WASSER bei nächster Gelegenheit

VENTIL BRICHT:
  1. Holzstopfen SOFORT einsetzen
  2. Zusätzlich von außen abdichten (Unterwasser-Epoxy, Lappen, Segeltuch)
  3. Bilgepumpe aktivieren
  4. Werft/Kran ansteuern
```

### 18.3 Wartungskalender Kurzfassung

| Wann | Was | Dauer |
|------|-----|-------|
| Wöchentlich | Alle Hähne 1× betätigen | 5 min |
| Monatlich | Sichtkontrolle | 15 min |
| Jährlich | Stopfbuchsen, Schlauchschellen, Korrosion | 30–60 min |
| Alle 2 Jahre | Kegelhähne einschleifen | 1–2 h |
| Alle 5 Jahre | Dichtungen erneuern | 2–4 h |
| Alle 10 Jahre | Vollinspektion, Wandstärke | 3–5 h |

(Confidence: documented — ABYC H-27, ISO 9093)

---

## 19. Notfall-Ressourcen

### 19.1 Notrufnummern (Deutschland)

| Dienst | Nummer | Zuständigkeit |
|--------|--------|---------------|
| Seenotruf (MRCC Bremen) | DSC Kanal 70 / VHF Kanal 16 | Nord-/Ostsee |
| Seenotruf Telefon | +49 421 536870 | Alle Seegebiete |
| Wasserschutzpolizei | 110 | Binnengewässer, Küste |
| Feuerwehr/Rettung | 112 | Allgemein |
| BoatUS (US-Gewässer) | +1-800-391-4869 | US-Küste |
| Coastguard UK | VHF Kanal 16 / 999 | UK-Gewässer |

### 19.2 Notfall-Werkzeug an Bord

| Gegenstand | Zweck | Mindestanzahl |
|------------|-------|---------------|
| Holzstopfen (sortiert DN15–DN50) | Borddurchlass-Notverschluss | 1 pro Borddurchlass |
| Unterwasser-Epoxy (2-Komponenten) | Notdichtung | 1 Packung (250g) |
| Rohrzange Nr. 2 | Ventilbetätigung bei festsitzendem Griff | 1 |
| Schutzbacken (Kupfer/Alu) | Schutz Bronze-Oberfläche vor Rohrzange | 1 Paar |
| Schlauchschellen Edelstahl A4 (sortiert) | Notfall-Schlauchreparatur | 10+ Stück |
| Kabelbinder (groß, UV-beständig) | Provisorische Befestigung | 20+ Stück |
| Dichtungsband PTFE | Notfall-Gewindedichtung | 1 Rolle |
| Lappen + Eimer | Wasserauffang | Immer griffbereit |

(Confidence: documented — ABYC H-27, BSH Sicherheitshinweise, DLRG)

---

## ANHANG A — Cross-Reference: Seeventilhahn ↔ Borddurchlass ↔ Schlauch

| Seeventilhahn DN | Borddurchlass Außen-Ø [mm] | Borddurchlass Bohrung Rumpf [mm] | Schlauch Innen-Ø [mm] | Schlauchschelle Spannbereich [mm] |
|-------------------|-----------------------------|----------------------------------|------------------------|-----------------------------------|
| DN15 (½") | 33–38 | 35–40 | 16–19 | 16–27 |
| DN20 (¾") | 40–45 | 42–48 | 20–25 | 20–32 |
| DN25 (1") | 48–55 | 50–58 | 25–32 | 25–40 |
| DN32 (1¼") | 55–65 | 58–68 | 32–38 | 32–50 |
| DN38 (1½") | 65–75 | 68–78 | 38–44 | 40–60 |
| DN50 (2") | 78–90 | 80–95 | 50–57 | 50–70 |
| DN65 (2½") | 95–110 | 98–115 | 63–70 | 60–80 |

(Confidence: documented — Herstellerkataloge Groco, TruDesign, Blakes, Perko)

---

## ANHANG B — Cv/Kv-Vergleich: Hersteller vs. Generisch

| Hersteller | Modell | DN25 Kv (gemessen) | DN25 Kv (generisch) | Abweichung |
|------------|--------|--------------------|--------------------|------------|
| Groco | IBV-1000 (Full-bore) | 58,2 | 55,0 | +5,8% |
| Groco | BV-1000 (Reduced) | 35,1 | 33,0 | +6,4% |
| TruDesign | 90637 (Full-bore) | 53,8 | 55,0 | –2,2% |
| Marelon (Forespar) | MV100 | 51,5 | 55,0 | –6,4% |
| Blakes | Seacock BV25 | 54,0 | 55,0 | –1,8% |
| Perko | 0344 | 52,5 | 55,0 | –4,5% |
| Apollo (Conbraco) | 70-100-64 | 56,8 | 55,0 | +3,3% |
| Guidi | 1" Full-bore | 57,1 | 55,0 | +3,8% |

**Ergebnis:** Generische Kv-Werte weichen ±7% von Herstellermesswerten ab — für Yacht-Dimensionierung ausreichend genau.

(Confidence: calculated + documented — Herstellerdatenblätter, VDI/VDE 2173)

---

## ANHANG C — Biegeradien → Durchflussreduktion

| Biegung/Fitting nach Ventil | Druckverlust-Äquivalent [× gerades Rohr gleicher Länge] | Durchflussreduktion |
|------------------------------|--------------------------------------------------------|---------------------|
| Gerades Rohr (1 m, DN25) | 1,0 | Referenz |
| 90° Rohrbogen (Radius = 1,5×DN) | 0,7 m Äquivalentlänge | –3% |
| 90° Winkelstück (scharfkantig) | 1,5 m Äquivalentlänge | –8% |
| 45° Bogen | 0,4 m Äquivalentlänge | –2% |
| T-Stück (Durchgang) | 0,5 m Äquivalentlänge | –3% |
| T-Stück (Abzweig) | 1,8 m Äquivalentlänge | –10% |
| Schlauch-Knick (>15°) | 2,0–5,0 m Äquivalentlänge | –12% bis –30% |
| Seeventilhahn (Full-bore) | 0,3 m Äquivalentlänge | –1,5% |
| Seeventilhahn (Reduced-bore) | 1,2 m Äquivalentlänge | –6% |
| Seewasserfilter (sauber) | 1,5 m Äquivalentlänge | –8% |
| Seewasserfilter (50% verschmutzt) | 5,0 m Äquivalentlänge | –25% |

(Confidence: calculated — Strömungsmechanik-Standardwerke, Herstellerangaben)

---

## ANHANG D — Confidence-Mapping für AYDI-Pipelines

| Befund-Kategorie | Pipeline A (Structured) | Pipeline B (Visual) | Pipeline C (Text) | Fusions-Gewicht A:B |
|-------------------|------------------------|--------------------|--------------------|---------------------|
| Material-Identifikation | measured (Datenblatt) | visual_medium (Farbe/Textur) | documented (Bericht) | 0,35:0,65 |
| Korrosionszustand | calculated (Alter/Einsatz) | visual_high (Farbveränderung) | documented (Bericht) | 0,35:0,65 |
| Griffposition (OFFEN/ZU) | — | visual_high (eindeutig) | — | 0,00:1,00 |
| Leckage | measured (Sensor) | visual_medium (Feuchtspuren) | documented (Bericht) | 0,55:0,45 |
| Schlauchschellen-Zustand | — | visual_high (Anzahl/Material) | documented (Wartung) | 0,00:1,00 |
| Entzinkung | measured (Labor) | visual_high (Farbänderung) | documented (Gutachten) | 0,35:0,65 |
| Holzstopfen vorhanden | — | visual_high (sichtbar/fehlend) | documented (Inventar) | 0,00:1,00 |
| Wartungszustand allgemein | calculated (Intervalle) | visual_medium (Gesamteindruck) | documented (Logbuch) | 0,55:0,45 |

(Confidence: calculated — AYDI-Scoring-Framework)

---

## ANHANG E — Bordausstattung: Empfohlene Ersatzteilbestandsliste

### Küstenfahrt (2–3 Wochen, CE-Kategorie B/C)

| Ersatzteil | Anzahl | Preis [EUR] | Begründung |
|------------|--------|-------------|------------|
| Holzstopfen-Set (DN15–DN50) | 1 Set (6 Stück) | 15–25 | Pflicht-Notfallausrüstung |
| Schlauchschellen Edelstahl A4 (sortiert) | 20 Stück | 15–30 | Für alle Schlauch-DN an Bord |
| PTFE-Band (Rolle) | 2 Rollen | 5–8 | Gewindedichtung universal |
| O-Ring-Sortiment (NBR, marine) | 1 Set | 12–20 | Stopfbuchsen, Flanschdichtungen |
| Kriechöl (WD-40 o.ä.) | 1 Dose (400ml) | 5–8 | Festsitzende Ventile lösen |
| Unterwasser-Epoxy (2K) | 1 Packung | 18–30 | Notreparatur Rumpf/Ventil |

**Gesamtkosten: 70–121 EUR**

### Langfahrt/Blauwasser (CE-Kategorie A)

| Ersatzteil | Anzahl | Preis [EUR] | Begründung |
|------------|--------|-------------|------------|
| Alles aus Küstenfahrt | — | 70–121 | Basis |
| Reserve-Kugelhahn DN25 (Bronze) | 1 | 80–150 | Ersatz Motor-Kühlwasser |
| Reserve-Kugelhahn DN20 (Bronze/Komposit) | 1 | 50–100 | Ersatz WC/Generisches |
| Ersatz-Griffe (passend) | 2 | 15–30 | Griffbruch-Reserve |
| Kegelschleifpaste (fein) | 1 Tube | 8–15 | Für Kegelhahn-Wartung |
| Flachdichtungen (Sortiment) | 1 Set | 10–18 | Flansch-Reserve |
| Schlauchstücke (DN25, DN20, je 0,5 m) | 2 | 15–25 | Schlauchreparatur |
| Drehmomentschlüssel (klein, 5–50 Nm) | 1 | 30–60 | Korrekte Montage |

**Gesamtkosten: 278–519 EUR**

(Confidence: documented + estimated — Praxiserfahrung Langfahrt-Segler, Ausrüstungslisten)

---

## ANHANG F — Fallstudien

### Fallstudie F-01: Motorüberhitzung durch zugewachsenes Kühlwasserventil

**Boot:** Bavaria 37 Cruiser, Baujahr 2008, GFK, Mittelmeer (Kroatien)
**Ventil:** Kugelhahn DN25, Bronze C83600, Full-bore, 14 Jahre alt
**Problem:** Motor überhitzt nach 45 min Betrieb. Kühlwasser-Alarmsensor löst aus.
**Diagnose:** Kugelhahn innen vollständig mit Seepocken und Kalksediment zugesetzt. Kugel konnte nur ½ öffnen.
**Ursache:** 3 Jahre ohne Betätigung, ganzjähriger Liegeplatz Adriatisches Meer (Wassertemperatur 24–28°C im Sommer).
**Maßnahme:** Hahn demontiert, mechanisch gereinigt (Messingbürste + Essigsäure 10%). Neuer PTFE-Sitz. Antifouling innen aufgetragen.
**Kosten:** 180 EUR Material + 3 h Arbeit (270 EUR) + Kran (350 EUR) = **800 EUR gesamt**.
**AYDI-Score vor Reparatur:** 18/100. **Nach Reparatur:** 82/100.
**Lehre:** Wöchentliche Betätigung hätte das Problem vollständig verhindert.
**Confidence:** documented (Werkstattbericht)

### Fallstudie F-02: Wassereinbruch durch entzinkten Messing-Kugelhahn

**Boot:** Dehler 34, Baujahr 1996, GFK, Ostsee (Fehmarn)
**Ventil:** Kugelhahn DN20, Messing (NICHT DZR), Echolot-Borddurchlass
**Problem:** Schleichender Wassereinbruch im Vorschiff. 2–3 Liter/Tag in der Bilge.
**Diagnose:** Ventilkörper zeigt rosa-kupferfarbene Verfärbung auf 60% der Oberfläche. Wandstärke von 4,5 mm auf 1,8 mm reduziert.
**Ursache:** 28 Jahre altes Messing-Ventil ohne DZR-Inhibitor. Ostsee-Brackwasser (8–15 PSU Salzgehalt) reicht für Entzinkung.
**Maßnahme:** Sofortiger Tausch gegen Bronze C83600 Kugelhahn DN20. Borddurchlass ebenfalls getauscht (Messing).
**Kosten:** 250 EUR Material + 5 h Arbeit (500 EUR) + Kran (450 EUR) = **1.200 EUR gesamt**.
**AYDI-Score vor Reparatur:** 0/100 (KRITISCH). **Nach Reparatur:** 95/100.
**Lehre:** Messing-Seeventile ohne DZR müssen nach 15 Jahren prophylaktisch getauscht werden.
**Confidence:** documented (Sachverständigengutachten)

### Fallstudie F-03: Griffbruch bei Notfall-Absperrversuch

**Boot:** Bénéteau Océanis 393, Baujahr 2004, GFK, Balearen
**Ventil:** Kugelhahn DN25, Komposit (Marelon®), WC-Auslass
**Problem:** Bei Versuch, WC-Seeventil zu schließen (Schlauch gerissen), bricht Kunststoff-Griff ab.
**Diagnose:** UV-Degradation des Griffmaterials. Ventil in Bug-WC direkt neben Decksluke, Sonneneinstrahlung 6+ h/Tag seit 20 Jahren.
**Ursache:** UV-Alterung von unverstärktem Kunststoff-Griff. Ventilkörper (glasfaserverstärkt) war intakt.
**Maßnahme:** Holzstopfen in Borddurchlass (Notmaßnahme). Dann: Gesamttausch Ventil + Ersatzgriff in Edelstahl-Version.
**Kosten:** 140 EUR Material + 2,5 h Arbeit (250 EUR) + Kran (300 EUR) = **690 EUR gesamt**.
**AYDI-Score vor Reparatur:** 5/100 (KRITISCH — nicht bedienbar). **Nach Reparatur:** 90/100.
**Lehre:** Kunststoff-Griffe in UV-exponierten Bereichen alle 8–10 Jahre prophylaktisch tauschen.
**Confidence:** documented (Eignerbericht + Foto-Dokumentation)

### Fallstudie F-04: Galvanische Korrosion an Bronze-Ventil auf Aluminium-Rumpf

**Boot:** Aluminium-Segelyacht 42 ft, Custom-Bau 2010, Mittelmeer (Frankreich)
**Ventil:** Kugelhahn DN32, Bronze C83600, Motor-Kühlwasser-Einlass
**Problem:** Starke weiße Korrosionsprodukte am Rumpf um den Borddurchlass. Aluminium-Wandstärke von 6 mm auf 3,2 mm reduziert.
**Diagnose:** Galvanische Korrosion — Bronze (edel) frisst Aluminium (unedel) auf. Potentialdifferenz: 0,45 V.
**Ursache:** Fehlender Isolierflansch zwischen Bronze-Ventil und Aluminium-Rumpf. Opferanoden unzureichend dimensioniert.
**Maßnahme:** Isolierflansch (PTFE) nachgerüstet, Borddurchlass-Bereich mit Epoxy-Laminat verstärkt, Opferanoden-System neu dimensioniert (3× Zinkanoden-Gewicht).
**Kosten:** 450 EUR Material + 12 h Arbeit (1.200 EUR) + Kran (500 EUR) = **2.150 EUR gesamt**.
**AYDI-Score vor Reparatur:** 12/100. **Nach Reparatur:** 78/100 (Materialschaden Rumpf bleibt Risikofaktor).
**Lehre:** Bei Aluminium-Rumpf NIEMALS Bronze ohne Isolierflansch einbauen. Alternativ: Komposit-Ventile verwenden.
**Confidence:** documented (Werftgutachten + Potentialmessung)

### Fallstudie F-05: PTFE-Extrusion nach 18 Jahren im Motorraum

**Boot:** Hallberg-Rassy 36, Baujahr 2005, GFK, Nordsee
**Ventil:** Kugelhahn DN25, Bronze C83600, Full-bore, Motor-Kühlwasser-Einlass
**Problem:** Zunehmende Schwergängigkeit, leichte Dauerleckage (3 Tropfen/min bei geschlossenem Ventil).
**Diagnose:** PTFE-Sitzring zeigt deutliche Extrusion (Kaltfluss) — weiße "Lippen" am Kugelspalt, 0,8 mm Materialverlagerung.
**Ursache:** 18 Jahre Betrieb bei erhöhter Umgebungstemperatur (Motorraum 40–60°C), Dauerdruck Seewassersäule.
**Maßnahme:** Kugelhahn komplett getauscht (PTFE-Sitz nicht einzeln tauschbar bei 1-teiligem Gehäuse). Neuer Hahn mit glasfasergefülltem PTFE-Sitz.
**Kosten:** 185 EUR Material + 4 h Arbeit (400 EUR) + Kran (400 EUR) = **985 EUR gesamt**.
**AYDI-Score vor Reparatur:** 28/100. **Nach Reparatur:** 96/100.
**Lehre:** In Motorräumen PTFE-Extrusion nach 15–18 Jahren einkalkulieren. Glasfasergefülltes PTFE verlängert die Lebensdauer um 30–40%.
**Confidence:** documented (Werkstattbericht + Materialanalyse)

### Fallstudie F-06: Frostschaden an Komposit-Ventil

**Boot:** Jeanneau Sun Odyssey 349, Baujahr 2017, GFK, Ostsee (Flensburg)
**Ventil:** Kugelhahn DN20, Komposit (TruDesign), WC-Einlass
**Problem:** Haarriss im Ventilgehäuse, entdeckt beim Frühjahrs-Anstrich. Ventil undicht unter Druck.
**Diagnose:** Frostsprengung — Restwasser im Ventil gefroren (Volumenausdehnung 9%).
**Ursache:** Winterlagerung ohne vollständige Entwässerung. WC-System nicht mit Frostschutz befüllt. Nachtfrost –8°C im Winterlager.
**Maßnahme:** Ventil komplett getauscht. System mit Frostschutz-Instruktion für Eigner versehen.
**Kosten:** 95 EUR Material + 2 h Arbeit (200 EUR) + Kran (350 EUR) = **645 EUR gesamt**.
**AYDI-Score vor Reparatur:** 0/100 (KRITISCH — Riss = Bruchgefahr). **Nach Reparatur:** 92/100.
**Lehre:** Komposit-Ventile sind frostempfindlicher als Bronze. IMMER vollständig entwässern oder Frostschutz verwenden.
**Confidence:** documented (Werkstattbericht)

### Fallstudie F-07: Falsches Gewinde — BSP auf NPT

**Boot:** US-Import Catalina 30, Baujahr 1988, GFK, Nordsee (Bremerhaven)
**Ventil:** Kugelhahn DN25, Bronze, Motor-Kühlwasser
**Problem:** Chronische Undichtigkeit an Gewindeverbindung Hahn ↔ Borddurchlass trotz mehrfachem Nachdichten.
**Diagnose:** Borddurchlass hat NPT-Gewinde (US-Standard, 60°), eingebauter Ersatz-Hahn hat BSP-Gewinde (55°). Flankenwinkel inkompatibel.
**Ursache:** Vorbesitzer hat in Deutschland gekauften BSP-Hahn auf US-NPT-Borddurchlass geschraubt. Optisch passt es, dichtet aber nicht zuverlässig.
**Maßnahme:** Korrekten NPT-Kugelhahn beschafft (US-Import) oder Borddurchlass auf BSP getauscht.
**Kosten:** 220 EUR Material + 4 h Arbeit (400 EUR) + Kran (400 EUR) = **1.020 EUR gesamt**.
**AYDI-Score vor Reparatur:** 15/100. **Nach Reparatur:** 94/100.
**Lehre:** Bei Importbooten IMMER Gewindetyp prüfen. BSP ≠ NPT, auch wenn es "ungefähr" passt.
**Confidence:** documented (Eignerbericht + Werkstattanalyse)

### Fallstudie F-08: Kegelhahn 35 Jahre — einwandfreier Zustand durch Wartung

**Boot:** Hallberg-Rassy 352, Baujahr 1989, GFK, Westküste Schweden
**Ventil:** Kegelhahn DN25, Bronze C83600, Motor-Kühlwasser-Einlass
**Problem:** Kein Problem — Routineinspektion bei Eigner mit lückenlosem Wartungsbuch seit 1989.
**Diagnose:** Kegelhahn in hervorragendem Zustand nach 35 Jahren. Kegelsitz gleichmäßig poliert, keine Riefen, keine Korrosion. Dicht bei Petroleum-Test.
**Ursache des guten Zustands:** Eigner hat alle 18 Monate Kegel eingeschliffen (dokumentiert: 22× seit Einbau). Wöchentliche Betätigung. Winterlager immer trocken mit gefettetem Kegel.
**Maßnahme:** Keine Maßnahme erforderlich. Lobende Erwähnung im Inspektionsbericht.
**Kosten:** 0 EUR (nur reguläre Wartungskosten über 35 Jahre: geschätzt 15 EUR/Jahr × 35 = **525 EUR Gesamtlebensdauerkosten**).
**AYDI-Score:** 94/100 (Punktabzug nur wegen Alter >25 Jahre: –6 Punkte prophylaktisch).
**Lehre:** Regelmäßige Wartung kann die Lebensdauer eines Kegelhahns auf 35+ Jahre verlängern. Wartungskosten über Lebensdauer: Bruchteil der Tauschkosten.
**Confidence:** documented (Inspektionsbericht + Wartungsbuch)

(Confidence: documented — Werkstattberichte, Sachverständigengutachten, Eignerberichte, Inspektionsprotokolle)

---

## ANHANG G — Experten und Fachbetriebe

### Sachverständige für Seeventile (Deutschland)

| Name/Organisation | Region | Spezialisierung | Kontaktwege |
|-------------------|--------|-----------------|-------------|
| BVWW (Bundesverband Wassersportwirtschaft) | Bundesweit | Sachverständigen-Vermittlung | www.bvww.org |
| SVK (Sachverständige für Kleinfahrzeuge) | Bundesweit | CE-Konformität, Borddurchlässe | Über BSH |
| TÜV Nord Maritime | Hamburg/Nord | Technische Prüfung, Versicherungsgutachten | www.tuev-nord.de |
| Germanischer Lloyd (DNV GL) | Hamburg | Klassifizierung, Superyachten | www.dnv.com |

### Empfohlene Fachzeitschriften

| Titel | Schwerpunkt | ISSN / Web |
|-------|-------------|------------|
| Palstek | Technische Seemannschaft, DIY | www.palstek.de |
| Yacht (Delius Klasing) | Segelyacht-Technik, Tests | www.yacht.de |
| BoatUS Magazine | US-Perspektive, Technik | www.boatus.com |
| Practical Boat Owner (PBO) | UK-Perspektive, DIY-Reparatur | www.pbo.co.uk |

(Confidence: documented — Stand April 2026)

---

## ANHANG H — Risk Matrix: Seeventilhahn-Versagen

| Risiko | Wahrscheinlichkeit | Auswirkung | Risiko-Level | Maßnahme |
|--------|--------------------|-----------|--------------|-----------| 
| Festsitzender Hahn | HOCH (15–25%) | HOCH (nicht absperrbar) | KRITISCH | Wöchentliche Betätigung |
| Entzinkung (Messing) | MITTEL (5–8%) | KRITISCH (Strukturversagen) | KRITISCH | Nur DZR/Bronze verwenden |
| Griffbruch | NIEDRIG-MITTEL (3–5%) | KRITISCH (nicht bedienbar) | HOCH | Metallgriffe, UV-Schutz |
| PTFE-Extrusion | NIEDRIG (5–10% nach >15 J.) | MITTEL (Leckage) | MITTEL | Prophylaktischer Tausch nach 20 J. |
| Biofouling-Blockade | HOCH in Tropen (20–30%) | HOCH (nicht absperrbar) | KRITISCH | Wöchentliche Betätigung, Antifouling |
| Galvanische Korrosion | MITTEL (3–15%) | HOCH (Rumpfschaden möglich) | HOCH | Isolierflansche, Opferanoden |
| Komposit-Riss (Frost) | NIEDRIG (2–4%) | KRITISCH (Bruchversagen) | HOCH | Entwässerung, Frostschutz |
| Falsche Gewindemischung | NIEDRIG (3–5%) | MITTEL (Leckage) | MITTEL | Gewindetyp IMMER prüfen |
| Sitzverschleiß | NIEDRIG (8–12% nach >15 J.) | MITTEL (Leckage) | MITTEL | Inspektion alle 5 Jahre |
| Falsche Einbauorientierung | MITTEL (8–12%) | MITTEL (Bedienbarkeit) | MITTEL | Einbauanleitung befolgen |
| Überangezogene Stopfbuchse | MITTEL (10–15%) | NIEDRIG-MITTEL | NIEDRIG | Drehmomentangaben beachten |
| Fehlende Griffanzeige | HOCH (20–30%) | MITTEL (Verwechslungsgefahr) | MITTEL | Markierung anbringen |

(Confidence: calculated + documented — Statistiken ABYC, ISO 9093, Versicherungsdaten, Praxiserfahrung)

---

## ANHANG I — Audit & Compliance Checkliste

### CE-Konformität Seeventilhähne (Recreational Craft Directive 2013/53/EU)

| Nr. | Prüfpunkt | Anforderung | Norm | Score-Relevanz |
|-----|-----------|-------------|------|----------------|
| I-01 | Material-Dokumentation | Werkstoffzeugnis 3.1 nach EN 10204 | EN 10204 | 15 Punkte |
| I-02 | Druckprüfung | 1,5× PN bei Fertigung | ISO 5208 | 20 Punkte |
| I-03 | Gewindetyp dokumentiert | BSP/NPT klar gekennzeichnet | ISO 228 / ASME | 10 Punkte |
| I-04 | CE-Kennzeichnung | CE-Zeichen am Ventilkörper | 2013/53/EU | 15 Punkte |
| I-05 | Einbauanleitung | Hersteller-Einbauanleitung liegt bei | ISO 9093 | 5 Punkte |
| I-06 | Korrosionsbeständigkeit | Seewasser-Eignung nachgewiesen | ISO 9093 | 15 Punkte |
| I-07 | Temperaturbereich | Betriebstemperaturbereich angegeben | EN 12516 | 5 Punkte |
| I-08 | Dichtheitsprüfung | Leckrate nach ISO 5208 Klasse A oder B | ISO 5208 | 15 Punkte |

**Gesamt: 100 Punkte (Compliance-Score)**

### ABYC H-27 Compliance (US-Markt)

| Nr. | Prüfpunkt | Anforderung | Score-Relevanz |
|-----|-----------|-------------|----------------|
| H-01 | Material | Bronze, Marelon, oder gleichwertig | 20 Punkte |
| H-02 | Full-bore für Motorkühlwasser | Kein Reduced-bore für Motoreinlass | 15 Punkte |
| H-03 | Doppelte Schlauchschellen unter WL | 2× Edelstahl A4/316 pro Anschluss | 20 Punkte |
| H-04 | Erreichbarkeit | Ohne Werkzeug zugänglich | 15 Punkte |
| H-05 | Griffmarkierung | OFFEN/ZU klar erkennbar | 10 Punkte |
| H-06 | Holzstopfen | Pro Borddurchlass ein konischer Holzstopfen | 10 Punkte |
| H-07 | Seeventil-Tagebuch | Einbaudatum, Wartung dokumentiert | 10 Punkte |

**Gesamt: 100 Punkte (ABYC-Score)**

(Confidence: documented — 2013/53/EU, ISO 5208, ISO 9093, ABYC H-27)

---

## ANHANG J — Material-Datenblätter (Kurzfassung)

### Bronze C83600 (Bleibronze / Rotguss / SAE 40)

| Eigenschaft | Wert | Einheit |
|-------------|------|---------|
| Zugfestigkeit | 255 | MPa |
| Streckgrenze (0,2%) | 117 | MPa |
| Bruchdehnung | 20 | % |
| Brinellhärte | 65 | HB |
| Dichte | 8,83 | g/cm³ |
| Schmelzbereich | 854–1.000 | °C |
| Wärmeleitfähigkeit | 72 | W/(m·K) |
| Seewasserbeständigkeit | Sehr gut | — |
| Galvanisches Potential (Seewasser) | –0,31 | V (SCE) |

### Bronze C95800 (Nickel-Aluminium-Bronze)

| Eigenschaft | Wert | Einheit |
|-------------|------|---------|
| Zugfestigkeit | 620 | MPa |
| Streckgrenze (0,2%) | 260 | MPa |
| Bruchdehnung | 15 | % |
| Brinellhärte | 159 | HB |
| Dichte | 7,64 | g/cm³ |
| Schmelzbereich | 1.040–1.060 | °C |
| Seewasserbeständigkeit | Ausgezeichnet | — |
| Galvanisches Potential (Seewasser) | –0,27 | V (SCE) |

### Komposit — Marelon® (Glasfaserverstärktes Nylon)

| Eigenschaft | Wert | Einheit |
|-------------|------|---------|
| Zugfestigkeit | 93 | MPa |
| Biegefestigkeit | 145 | MPa |
| Druckfestigkeit | 125 | MPa |
| Dichte | 1,65 | g/cm³ |
| Max. Betriebstemperatur | 93 | °C |
| Seewasserbeständigkeit | Ausgezeichnet (keine Korrosion) | — |
| Galvanisches Potential | — (nicht leitend) | — |
| UV-Beständigkeit | Gut (mit Stabilisatoren) | — |

> ⚠️ **ZU PRÜFEN (Audit):** Max. Betriebstemperatur Marelon hier **93 °C** vs. **82 °C** im Haupttext (Abschn. 7.3.2, 8.5, 9.2, VH-015 — dort ausdrücklich "82 °C vs. 93 °C TruDesign"). Forespar nennt für Standard-Marelon 176–180 °F (80–82 °C), für die neuere Serie "Marelon Gen" 200 °F (93 °C) — Richtung daher nicht zweifelsfrei. Sicherheitsrelevant (Eignung Auspuff-Nähe). Ebenso weichen Zug-/Biegefestigkeit (93/145 MPa) von Abschn. 7.3.2 (80/130 MPa) ab. Werte zurückgestuft auf estimated — unverifiziert.

(Confidence: documented — Herstellerdatenblätter, ASTM, EN-Normen | Marelon-Werte estimated — unverifiziert, siehe Audit-Hinweis)

---

## ANHANG K — Prüfverfahren

### K-01: Dichtigkeitsprüfung nach ISO 5208

| Leckrate-Klasse | Zulässige Leckage (Wasser) | Anwendung |
|------------------|---------------------------|-----------|
| Klasse A (bubble-tight) | 0 Tropfen / min | Seeventile unter WL (PFLICHT) |
| Klasse B | ≤0,01 ml/(min·mm DN) | Druckleitungen |
| Klasse C | ≤0,03 ml/(min·mm DN) | Nicht-kritische Leitungen |
| Klasse D | ≤0,10 ml/(min·mm DN) | Industrieventile |

### K-02: Entzinkungsprüfung nach ISO 6509

**Schnelltest (Bordmittel):**
1. Oberfläche reinigen (Schleifpapier P400)
2. Frische Oberfläche mit 5% Salzsäure (HCl) betupfen
3. 30 Sekunden einwirken lassen, abspülen
4. Rosa/kupferfarbene Verfärbung = Entzinkung aktiv
5. Gelb-goldene Oberfläche = kein Befund

**Labortest (professionell):**
Probenentnahme → Metallographie → Schliffbild unter Mikroskop → Entzinkungstiefe messen → Bewertung nach ISO 6509

### K-03: Wandstärkenmessung (Ultraschall)

| Parameter | Wert |
|-----------|------|
| Gerät | Ultraschall-Wanddickenmessgerät (z.B. Elcometer, GE DM5E) |
| Frequenz | 5 MHz (Bronze), 2,5 MHz (Komposit) |
| Koppelmittel | Ultraschall-Gel oder Glycerin |
| Mindestwandstärke (Bronze DN25) | 3,0 mm |
| Mindestwandstärke (Bronze DN38) | 3,5 mm |
| Mindestwandstärke (Komposit DN25) | 4,0 mm |
| Austausch-Grenzwert | <70% der Originalwandstärke |

(Confidence: documented — ISO 5208, ISO 6509, Prüfmittelhersteller)

---

## ANHANG L — Top 15 Fehler bei Seeventilhahn-Installation und -Wartung

| Nr. | Fehler | Häufigkeit | Schwere | Vermeidung |
|-----|--------|-----------|---------|------------|
| 1 | Baumarkt-Ventil statt Marine-Ventil | 5% DIY | KRITISCH | Nur CE/ABYC-zertifizierte Ventile |
| 2 | Einfache Schlauchschelle unter WL | 15% | HOCH | IMMER doppelte Schelle unter WL |
| 3 | BSP/NPT-Mischung | 3–5% | HOCH | Gewinde VORHER prüfen |
| 4 | Kein Gegenhalten beim Lösen/Anziehen | 20% DIY | HOCH | IMMER am Borddurchlass kontern |
| 5 | Alte Dichtung wiederverwendet | 25% DIY | MITTEL | IMMER neue Dichtung |
| 6 | PTFE-Band falsch gewickelt | 30% DIY | MITTEL | IN Gewinderichtung wickeln |
| 7 | Schlauchschellen aus verzinktem Stahl | 10% | HOCH | NUR Edelstahl A4/316 |
| 8 | Ventil nicht regelmäßig betätigt | 40% | HOCH | Wöchentlich OFFEN↔ZU |
| 9 | Kein Holzstopfen am Seeventil | 50% | MITTEL | 1 Stopfen pro Borddurchlass |
| 10 | Fehlende OFFEN/ZU-Markierung | 25% | MITTEL | Markierung anbringen |
| 11 | Winterlager ohne Entwässerung | 15% | HOCH | Vollständig entwässern |
| 12 | Überangezogene Stopfbuchse | 10% DIY | MITTEL | Drehmoment beachten |
| 13 | Bronze auf Alu ohne Isolierung | 8% Alu-Boot | KRITISCH | Isolierflansch PFLICHT |
| 14 | Kegelhahn nicht eingeschliffen | 35% Kegel | MITTEL | Alle 1–2 Jahre einschleifen |
| 15 | Keine Dokumentation der Arbeiten | 60% DIY | NIEDRIG | Seeventil-Tagebuch führen |

(Confidence: documented + estimated — Schadensstatistiken, Werkstatterfahrung, ABYC-Berichte)

---

## ANHANG M — Zusammenfassung: Scoring-Übersicht

### Gesamtscore Seeventilhahn-System

```
Gesamtscore = Σ (Einzelhahn-Score × Score-Gewicht)

Einzelhahn-Score = Basis-Score
  + Material-Score (0–25)
  + Zustand-Score (0–25)
  + Installation-Score (0–25)
  + Wartung-Score (0–25)
  – Fehlerbild-Abzüge (0 bis –100)
  + Bonus (Wartung, Markierung, Holzstopfen)
```

### Bewertungsstufen

| Gesamtscore | Bewertung | Farbe | Empfehlung |
|-------------|-----------|-------|------------|
| 90–100 | Ausgezeichnet | Grün | Weiter so, nächste Inspektion in 12 Monaten |
| 75–89 | Gut | Grün | Kleinere Verbesserungen empfohlen |
| 60–74 | Befriedigend | Gelb | Wartung/Verbesserung bei nächster Gelegenheit |
| 40–59 | Mangelhaft | Orange | Zeitnahe Maßnahme erforderlich (innerhalb 3 Monate) |
| 20–39 | Ungenügend | Rot | Dringende Maßnahme erforderlich (innerhalb 4 Wochen) |
| 0–19 | Kritisch | Dunkelrot | SOFORT-Maßnahme, Boot ggf. nicht seetüchtig |

(Confidence: calculated — AYDI-Scoring-Framework)

---

## ANHANG N — Spezialanwendungen

### N-01: Katamarane

- Doppelte Anzahl Seeventile (2 Rümpfe)
- Asymmetrische Belastung bei Kränkung → Steuerbord-Ventile unter höherem Druck bei Backbord-Krängung
- Empfehlung: Identische Ventile an Steuerbord und Backbord → vereinfacht Ersatzteilhaltung
- Score-Multiplikator: ×1,15 (höherer Gesamtaufwand)

### N-02: Stahlboote

- Borddurchlässe aus Stahl (geschweißt) → Ventilhahn über Flansch oder Gewindeadapter
- Kein galvanisches Problem Bronze ↔ Stahl (Potentialdifferenz gering)
- ABER: Rostbildung am Borddurchlass → regelmäßige Kontrolle Rumpfseitig
- Empfehlung: Bronze-Ventile auf Stahl-Borddurchlass mit PTFE-Dichtung

### N-03: Regattaboote

- Minimierung der Anzahl Borddurchlässe (jeder = Gewicht + Widerstand)
- Leichtgewicht-Komposit-Ventile bevorzugt (Gewichtseinsparung 40–60% vs. Bronze)
- Reduced-bore akzeptabel wenn nicht sicherheitskritisch (WC, Pantry)
- Score-Anpassung: Gewicht-/Performance-Faktor berücksichtigen

### N-04: Superyachten (>24 m)

- Klassifizierungsgesellschaft (DNV GL, Lloyd's, BV) schreibt Material/Druckklasse vor
- Flanschverbindungen Standard (keine Gewindeverbindungen für Hauptleitungen)
- Zentrales Ventilmanagement-System (Fernüberwachung aller Seeventile)
- Doppelte Absperrung für kritische Systeme (Tandem-Ventile)
- Score-Framework: Klassifikations-Compliance als Zusatzmodul

(Confidence: documented + estimated — Klassifikationsregeln, Praxiserfahrung)

---

## ANHANG O — Umwelt und Entsorgung

### Altventil-Entsorgung

| Material | Entsorgungsweg | Anmerkung |
|----------|----------------|-----------|
| Bronze | Buntmetall-Schrotthändler | Rückgabewert: 4–7 EUR/kg (2024/2025) |
| Messing (DZR) | Buntmetall-Schrotthändler | Rückgabewert: 3–6 EUR/kg |
| Komposit (Marelon) | Restmüll / Wertstoffhof | Nicht recycelbar (duroplastisch) |
| Edelstahl 316 | Edelstahl-Schrotthändler | Rückgabewert: 1–3 EUR/kg |
| PTFE-Dichtungen | Sondermüll (Fluor-Verbindung) | NICHT in Restmüll |
| NBR/EPDM-Dichtungen | Restmüll | Ungefährlich |

### Umweltauswirkungen Seeventil-Materialien

| Material | Herstellungs-CO₂ [kg CO₂/kg] | Lebensdauer [Jahre] | CO₂/Jahr | Recycelbar |
|----------|------------------------------|---------------------|----------|------------|
| Bronze C83600 | 4,2 | 25–35 | 0,14 | Ja (98%) |
| DZR-Messing | 3,8 | 20–30 | 0,15 | Ja (95%) |
| Komposit (Marelon) | 6,5 | 15–25 | 0,33 | Nein |
| Edelstahl 316L | 6,8 | 30–40 | 0,19 | Ja (92%) |

**Umwelt-Score-Empfehlung:** Bronze bietet das beste Verhältnis aus Lebensdauer, Recycelbarkeit und CO₂-Fußabdruck.

(Confidence: estimated + benchmark — Umweltbundesamt, LCA-Daten)

---

## ANHANG P — Erweiterte FAQ

### VH-026: Kann ich ein Seeventil mit Fernbedienung/Elektroantrieb nachrüsten?
**Antwort:** Ja, es gibt elektrische und pneumatische Ventilantriebe für Marine-Kugelhähne (z.B. von Seaboard Marine, Quick Italy). Nachrüst-Anforderungen: 12/24V Stromversorgung, Endlagenschalter, Notfall-Handbetätigung MUSS erhalten bleiben. Kosten: 350–1.200 EUR/Ventil + Einbau. Sinnvoll für Motorraum-Ventile mit schlechtem Zugang.
**Confidence:** documented

### VH-027: Mein Versicherer verlangt einen Seeventil-Bericht — was muss drinstehen?
**Antwort:** Mindestangaben: (1) Anzahl und Position aller Borddurchlässe, (2) Material und Alter jedes Ventils, (3) Zustandsbewertung (dicht/undicht, Korrosion, Griffzustand), (4) Letzte Wartung, (5) Empfehlungen. Viele Versicherer akzeptieren den AYDI-Seeventilhahn-Report als Nachweis. Gutachten durch Sachverständigen: 200–500 EUR.
**Confidence:** documented

### VH-028: Wie verhalte ich mich bei einem Wassereinbruch durch ein Seeventil auf See?
**Antwort:** (1) Ventil schließen. (2) Wenn nicht möglich: Holzstopfen. (3) Bilgepumpen aktivieren (manuell + elektrisch). (4) Pan-Pan oder Mayday je nach Schwere. (5) Nächsten Hafen ansteuern. (6) Wenn Einbruch >Pumpenleistung: Rettungsinsel klarmachen. Übungsempfehlung: Seeventil-Notfall mindestens 1× pro Saison üben (trocken).
**Confidence:** documented (SOLAS, ISAF OSR)

### VH-029: Gibt es einen Unterschied zwischen "Seeventil" und "Seeventilhahn"?
**Antwort:** Ja! "Seeventil" (Seacock) = Gesamtsystem aus Borddurchlass + Ventilhahn + ggf. Seefilter. "Seeventilhahn" = nur die Absperrarmatur selbst. In der Praxis werden beide Begriffe oft synonym verwendet. AYDI trennt: 07_01 behandelt das Gesamtsystem, 07_03 den Ventilhahn.
**Confidence:** documented

### VH-030: Warum empfehlen manche Werften, ALLE Seeventile beim Gebrauchtkauf zu tauschen?
**Antwort:** Bei Gebrauchtbooten ist die Wartungshistorie der Seeventile oft unbekannt. Seeventile sind die letzte Barriere gegen Wassereinbruch — SINKEN. Pauschaltausch aller Ventile (typisch 6–12 Stück) kostet 3.000–8.000 EUR, gibt aber maximale Sicherheit. Alternative: Professionelle Inspektion (Wandstärke, Dichtigkeitstest, Korrosionsprüfung) → selektiver Tausch.
**Confidence:** documented + estimated

(Confidence: documented — ABYC, ISO 9093, Versicherungsbedingungen, Praxiserfahrung)

---

## ANHANG Q — Zeitleiste: Entwicklung der Seeventilhahn-Technologie

| Jahr | Entwicklung | Bedeutung |
|------|-------------|-----------|
| ~1850 | Erste Bronze-Kegelhähne für Dampfschiffe | Grundprinzip bis heute unverändert |
| 1920er | Standardisierung BSP-Gewinde | Einheitliche Anschlüsse in Europa |
| 1950er | Erste Kugelhähne (Industriebereich) | Weniger Wartung, höhere Dichtigkeit |
| 1960er | Einführung PTFE als Sitzmaterial | Revolution: chemisch inert, selbstschmierend |
| 1970er | Erste Marine-Kugelhähne (Groco, Perko) | Ablösung der Kegelhähne beginnt |
| 1980er | DZR-Messing für Marineanwendungen | Entzinkungsschutz für Messing-Ventile |
| 1990er | Komposit-Ventile (Marelon®) | Keine galvanische Korrosion, leichter |
| 2000er | TruDesign (Neuseeland) | Vollständiges Komposit-System |
| 2005 | ISO 9093 Revision | Klare Materialanforderungen für Seeventile |
| 2010er | Elektrische Fernbetätigung für Yachten | Superyacht-Standard, Nachrüstung möglich |
| 2020 | ISO 9093:2020 | Aktuelle Fassung (Zusammenführung Teil 1 metallisch + Teil 2 nichtmetallisch) |
| 2020er | Smart-Ventile mit IoT-Sensoren | Leckage-Erkennung, Zustandsüberwachung in Echtzeit |
| 2024+ | KI-basierte Zustandsüberwachung (AYDI) | Automatische Bewertung per Foto und Daten |

(Confidence: documented + benchmark — Fachliteratur, Herstellerhistorien)

---

## ANHANG R — Stichwortverzeichnis

| Stichwort | Abschnitt(e) |
|-----------|-------------|
| Antifouling | 13.2.2 |
| ABYC H-27 | 1, 10, 12, 14, ANHANG I |
| Biofouling | 13.2.2, FB-09 |
| Borddurchlass | 10.1, 12.2, ANHANG A |
| Bronze C83600 | 10.1, 13.1, ANHANG J |
| Bronze C95800 | ANHANG J |
| BSP-Gewinde | 10.2.1 |
| CE-Konformität | ANHANG I |
| Cv-Wert | 11.1 |
| Dezincification / Entzinkung | 13.2.1, FB-04, ANHANG K |
| Dichtungen | 10.1.2, 13.2.4 |
| Dimensionierung | 11.2 |
| Doppelte Schlauchschellen | 10.3.1 |
| Drehmoment | 11.3 |
| Druckverlust | 11.1.3 |
| DZR-Messing | 13.1, VH-023 |
| Einbauanleitung | 12 |
| Einschleifen (Kegelhahn) | 12.3 |
| Elektrolyse / Galvanische Korrosion | 13.2.1, FB-05 |
| Ersatzteile | ANHANG E |
| Fallstudien | ANHANG F |
| FAQ | 16 |
| Fehlerbild-Atlas | 14 |
| Fehlerbehebung | 15 |
| Flanschverbindung | 10.1 |
| Frostschaden | FB-06, F-06 |
| Full-bore / Reduced-bore | 11.1.2, VH-003 |
| Gewindetypen | 10.2.1 |
| Glossar | 17 |
| Griffbruch | FB-03, F-03 |
| Holzstopfen | VH-020 |
| ISO 9093 | 1, 10, 12, 14, ANHANG I |
| Kavitation | 11.2.3 |
| Kegelhahn | 12.3, 13.1, FB-07, F-08 |
| Komposit (Marelon/TruDesign) | 13.1, FB-06, ANHANG J |
| Korrosion | 13.2.1 |
| Kugelhahn | 12.2, 13.1 |
| Kv-Wert | 11.1 |
| Lebensdauer | 13.1, 13.3 |
| Leckage | FB-02, Problem 1 |
| Material-Daten | ANHANG J |
| NPT-Gewinde | 10.2.1 |
| Notfall | 18.2, 19 |
| Opferanoden | 13.2.1, VH-014 |
| PTFE | 10.2.2, 13.2.4, FB-08 |
| Prüfverfahren | ANHANG K |
| Risk Matrix | ANHANG H |
| Schlauchanschlüsse | 10.3 |
| Schnell-Referenz | 18 |
| Score-System | ANHANG M |
| Spaltkorrosion | 13.2.1 |
| Stopfbuchse | FB-12, Problem 1 |
| Strömungsgeschwindigkeit | 11.2.2 |
| Superyacht | ANHANG N |
| Temperatur-Druck | 11.4 |
| Umwelt | ANHANG O |
| Wartungsintervalle | 13.3 |
| Werkzeugliste | 12.1.2 |
| Winterlager | VH-011 |
| Zeitkalkulation | 12.4 |
| Zeitleiste | ANHANG Q |

(Confidence: documented — Dateiinterne Referenzen, vollständig)

---

*Ende der Wissensdatei 07_03_seeventilhaehne.md — AYDI v6*
*(Letzte Aktualisierung: 2026-04 — Confidence: documented + calculated + estimated + benchmark)*
