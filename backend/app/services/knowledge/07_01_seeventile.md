# 07.01 — Seeventile (Bronze/Messing/Komposit): Kompletthandbuch

> **Modulkontext**: materials, structural, compliance, service_patterns, cost
> **Confidence-Klassen**: measured | calculated | visual_high | visual_medium | estimated | documented | benchmark
> **Pydantic-Hinweis**: `model_config = {"from_attributes": True}` — NIEMALS `class Config`
> **Letzte Aktualisierung**: 2026-04
> **SICHERHEITSKRITISCH**: Jedes Seeventilversagen = potenzieller Wassereinbruch = SINKEN

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
10. Verbindungstechnik
11. Technische Referenz & Berechnungen
12. Einbau-/Austausch-Anleitung
13. Lebensdauer und Alterungsmechanismen
14. Fehlerbild-Atlas
15. Fehlerbehebungs-Leitfaden
16. FAQ
17. Glossar
18. Schnell-Referenz
19. Notfall-Ressourcen
20. Anhänge A–R

---

## 1. Einführung & Regulatorischer Rahmen

### 1.1 Warum Seeventile sicherheitskritisch sind

Ein Seeventil (engl. seacock) ist ein Absperrventil, das direkt am Borddurchlass (thru-hull fitting) montiert wird und den kontrollierten Verschluss jeder Rumpföffnung unterhalb der Wasserlinie ermöglicht. Es ist das **letzte Sicherheitselement** zwischen dem Meer und dem Schiffsinneren.

**KRITISCH**: Ein versagendes Seeventil bedeutet unkontrollierten Wassereinbruch. Bei einem 1½"-Borddurchlass (38 mm) in 1 m Wassertiefe strömen ca. 3.400 Liter pro Minute ein. Ein 8-m-Segelboot sinkt in unter 10 Minuten. Es gibt keine zweite Chance.

> ⚠️ **ZU PRÜFEN (Audit):** 3.400 l/min (hier) vs. 3.025 l/min in Tabelle 11.1.2 für exakt denselben Fall (DN38, 1 m Tiefe). Beide Werte liegen rund 10-fach über empirischen Flutungsraten (1″/25 mm bei ~0,3 m ≈ 20 gal/min ≈ 76 l/min, BoatUS/CCA) → für DN38 bei 1 m real ≈ 300 l/min. Zahl nicht als gesichert übernehmen — Details siehe Audit-Hinweis in 11.1.2.

Häufige Versagensursachen:
- Dezinkifizierung von Messing-Ventilen (schleichend, unsichtbar)
- Festsitzen durch Korrosion oder Bewuchs (Ventil lässt sich nicht schließen)
- Galvanische Korrosion durch falsche Materialpaarung
- Alterung von Dichtmasse zwischen Borddurchlass und Rumpf
- Bruch von Komposit-Ventilen durch UV oder mechanische Belastung
- Schlauchschellen-Versagen am Schlauchtülle-Anschluss

(Confidence: documented — MAIB Marine Accident Investigation Branch, BSU Bundesstelle für Seeunfalluntersuchung)

### 1.2 Regulatorischer Rahmen

#### 1.2.1 ISO 9093 — Borddurchlässe und Seeventile

**ISO 9093:2020 — Anforderungen an metallische Ausführung** (Borddurchlässe und Seeventile)
- Gilt für alle Boote 2,5–24 m (CE-Bereich)
- Definiert Mindest-Wandstärken für Bronze-Ventile
- Fordert Korrosionsbeständigkeit in Seewasser
- Vorgeschriebene Druckprüfung: 2× Betriebsdruck, mind. 2 bar
- Material: Kupferlegierungen mit Entzinkungsbeständigkeit (DZR) oder gleichwertig
- VERBIETET ausdrücklich unlegiertes Messing (Yellow Brass, C85200)

**ISO 9093:2020 — Anforderungen an nichtmetallische Ausführung** (Borddurchlässe und Seeventile)
- Gilt für glasfaserverstärkte Polyester-, Polyamid- und Acetalventile
- Definiert UV-Beständigkeitsanforderungen
- Berstdruckprüfung: mind. 4× Betriebsdruck
- Kriechfestigkeit über 20 Jahre Lebensdauer
- Brandverhalten: selbstverlöschend nach ISO 9094

| Anforderung | ISO 9093:2020 (Metall) | ISO 9093:2020 (Komposit) |
|---|---|---|
| Druckprüfung | 2× Betriebsdruck, ≥2 bar | 4× Betriebsdruck |
| Korrosionstest | 30 Tage Salzsprühnebel | UV-Alterungstest 1.000 h |
| Mindest-Wandstärke | Tabelle nach Nennweite | Berstdrucknachweis |
| Brandverhalten | n/a (Metall) | Selbstverlöschend |
| Kennzeichnung | Werkstoff, Hersteller, Nennweite | dto. + UV-Warnung |
| Lebensdauer-Nachweis | Korrosionsbeständigkeit | Kriechfestigkeit 20 Jahre |

(Confidence: documented — ISO 9093:2020, Edition 1, 2020-12-11)

> ✅ Aufgeloest (Audit): ISO 9093:2020 „Small craft — Seacocks and through-hull fittings" ist eine einzige zusammengeführte Norm (Edition 1, 2020-12-11), die metallische UND nichtmetallische Ausführungen gemeinsam abdeckt; eigenständige „ISO 9093-1:2020"/„ISO 9093-2:2020" existieren nicht. Zitierung in diesem Abschnitt durchgängig auf „ISO 9093:2020" vereinheitlicht (im Einklang mit Anhang Q/I). — Quelle: ISO-Katalog, iso.org/standard/75179.html.

#### 1.2.2 ABYC H-27 — Seacocks and Through-Hulls

Der amerikanische Standard ABYC H-27 ist oft strenger als ISO 9093:
- Alle Borddurchlässe unter Wasserlinie MÜSSEN ein Seeventil haben
- Ausnahme: Abgasaustritt bei Nassauspuff (aber empfohlen)
- Material: Bronze ASTM B61, B62, B505 oder zugelassenes Komposit
- KEIN Gate-Ventil (Schieberventil) als Seeventil zulässig!
- KEIN PVC-Ventil als Seeventil zulässig!
- Griff muss in Schließstellung parallel zum Rumpf stehen
- Mindestens 2× Schlauchschellen unterhalb der Wasserlinie
- Jährliche Funktionsprüfung dokumentiert

| ABYC H-27 Regel | Anforderung | Konsequenz bei Verstoß |
|---|---|---|
| H-27.4.1 | Jeder Borddurchlass unter WL braucht Seeventil | Versicherungsausschluss |
| H-27.4.3 | Keine Gate-Ventile | Sofortiger Austausch |
| H-27.4.5 | Bronze oder zugelassenes Komposit | Materialnachweis |
| H-27.5.2 | Backing-Block Pflicht bei GFK-Rumpf | Strukturversagen möglich |
| H-27.5.4 | Doppelte Schlauchschellen unter WL | Survey-Mangel |
| H-27.6.1 | Jährliche Betätigung + Inspektion | Dokumentationspflicht |
| H-27.7.1 | Notholzpfropfen griffbereit | Sicherheitsausrüstung |

(Confidence: documented — ABYC Standards H-27-2021)

#### 1.2.3 CE / RCD 2013/53/EU

Die Recreational Craft Directive verlangt:
- Alle sicherheitsrelevanten Borddurchführungen entsprechen harmonisierten EN ISO-Normen
- Herstellererklärung (DoC) muss Borddurchlässe abdecken
- CE-Kategorie bestimmt zusätzliche Anforderungen:
  - **Kategorie A (Ozean)**: Höchste Anforderungen, alle Ventile schließbar von einem Punkt
  - **Kategorie B (Offshore)**: Standard-Anforderungen
  - **Kategorie C (Küste)**: Reduzierte Anforderungen an Redundanz
  - **Kategorie D (Geschützt)**: Basis-Anforderungen

(Confidence: documented — EU RCD 2013/53/EU, Annex I, Abschnitt 3.6)

#### 1.2.4 Klassifikationsgesellschaften

**Lloyd's Register (LR)**:
- SSC (Special Service Craft) Rules Chapter 6
- Bronze: min. CuSn5Zn5Pb5 (C83600) oder CuSn7 (C92200)
- Wandstärke ≥3 mm für DN25, ≥4 mm für DN38, ≥5 mm für DN50
- Jährliche Inspektion, 5-Jahres-Überholung

**DNV-GL**:
- DNVGL-RU-YACHT Part 3 Chapter 8
- Alle Seeventile druckgeprüft auf 3 bar
- Korrosionszuschlag 1,5 mm auf Mindest-Wandstärke
- Dokumentierte Materialnachweise (3.1-Zeugnis nach EN 10204)

**RINA (Registro Italiano Navale)**:
- Rules for Yachts Part B Chapter 10
- Akzeptiert Guidi-Ventile mit RINA-Typzulassung
- Fokus auf galvanische Kompatibilität im System

**BSI / BS EN ISO 9093**:
- Britische Übernahme der ISO 9093
- Zusätzlich: PAS 95 für Komposit-Durchlässe
- Prüfung durch notifizierte Stelle (z.B. BMT, Lloyd's)

(Confidence: documented — LR SSC Rules 2023, DNVGL-RU-YACHT Pt3 Ch8, RINA Rules 2022)

#### 1.2.5 Versicherungsanforderungen

| Versicherer | Anforderung | Konsequenz |
|---|---|---|
| Pantaenius | Jährliche Seeventil-Inspektion | Leistungskürzung bis 100% |
| Yacht-Pool | Alle 10 Jahre Austausch Bronze | Klausel im Vertrag |
| GJM (NL) | ISO 9093-konform | Kein Versicherungsschutz ohne |
| Allianz Marine | Survey alle 5 Jahre inkl. Seeventile | Pflicht ab Bootswert >100k EUR |
| Zurich Marine | Messing-Ventile = Ausschlussgrund | Sofort-Kündigung möglich |
| IIMS Survey | Seeventile = Pflichtpunkt jeder Zustandsbesichtigung | Survey-Mangel = kein Versicherungsschutz |

**WARNUNG**: Die meisten Versicherer schließen Schäden durch bekannte Messing-Ventile (dezinkifizierungsgefährdet) explizit aus. Ein Survey, der Messing-Ventile feststellt, führt regelmäßig zur Auflage "Austausch innerhalb 90 Tage".

(Confidence: documented — Pantaenius Versicherungsbedingungen 2024, Yacht-Pool Klauseln)

### 1.3 Statistiken zu Seeventil-Versagen

| Quelle | Zeitraum | Vorfälle | Gesunken | Hauptursache |
|---|---|---|---|---|
| MAIB (UK) | 2015–2024 | 47 | 12 | Dezinkifizierung (38%), Festsitzen (27%) |
| BSU (DE) | 2015–2024 | 23 | 5 | Materialversagen (41%), Schlauch abgerutscht (22%) |
| USCG (USA) | 2015–2024 | 89 | 19 | Gate-Ventil versagt (31%), Korrosion (28%) |
| CHIRP Maritime | 2018–2024 | 34 | 8 | Alter >20 Jahre (47%), falsche Material-Paarung (29%) |

**Gesamtstatistik**: Ca. 35% aller Bootsversenkungen durch Wassereinbruch sind auf Seeventil- oder Borddurchlass-Versagen zurückzuführen.

(Confidence: documented — MAIB Annual Reports, BSU Jahresberichte, USCG Boating Accident Reports)

---

### 1.4 OEM-Seeventil-Ausstattung nach Werft (Standardkonfiguration)

| Werft | Typisch verbautes Material | Hersteller | Bewertung |
|---|---|---|---|
| Beneteau / Jeanneau | DZR-Messing + TruDesign Komposit | Guidi 2062, TruDesign | ⚠️ DZR nach 12–15 Jahren prüfen |
| Bavaria | DZR-Messing (ältere), Komposit (neuere) | Guidi 2062, TruDesign | ⚠️ Ältere Modelle: Dezinkifizierung möglich |
| Hanse / Dehler | DZR-Messing + Komposit | Guidi, TruDesign | ⚠️ Wie Beneteau/Bavaria |
| Dufour | DZR-Messing (überwiegend) | Guidi 2062 | ⚠️ Älter als 12 Jahre: unbedingt testen |
| Hallberg-Rassy | Bronze C83600 (Blakes) | Blakes BB/Lever | ✅ Premium — langlebig |
| Oyster | Bronze C83600 (Blakes) | Blakes BB | ✅ Premium |
| Nautor's Swan | Bronze C83600 (Groco) | Groco BV/IBV | ✅ Premium |
| Contest | Bronze C83600 (Blakes) | Blakes Lever | ✅ Premium |
| X-Yachts | Bronze + Komposit (Mix) | Guidi 2060, TruDesign | ✅ Gute Qualität |
| Azimut / Benetti | Bronze C83600 (Guidi) | Guidi 2060, Italvalvole | ✅ Gute Qualität |
| Princess / Sunseeker | Bronze C83600 | Blakes, Guidi | ✅ Gute Qualität |
| Catalina (USA) | Marelon Komposit | Forespar | ✅ Kein Korrosionsrisiko |
| Hunter (USA) | Marelon + Bronze (Mix) | Forespar, Groco | ✅ |
| Bayliner (USA, ältere) | Yellow Brass (!) | unbekannt | ❌ GEFAHR — sofort prüfen! |

**AYDI-Hinweis**: Bei Pipeline A (Strukturiert) kann die Werft + Baujahr als Schätzgrundlage für die Seeventil-Ausstattung dienen, wenn keine spezifischen Daten vorliegen. Bei französischen Werften (Beneteau, Jeanneau, Dufour) ab Baujahr >2012 mit DZR-Messing rechnen und Dezinkifizierungs-Warnung ausgeben.

(Confidence: estimated — Werft-Stücklisten, Survey-Erfahrung, Forum-Berichte)

### 1.5 Häufigste Seeventil-Probleme nach Bootskategorie

| Bootskategorie | Häufigstes Problem | Zweithäufigstes | Dritthäufigstes |
|---|---|---|---|
| Produktions-Segelboot (8–14 m, <15 Jahre) | Einfache statt doppelte Schlauchschellen | DZR-Messing Alterung | Fehlende Holzpfropfen |
| Produktions-Segelboot (8–14 m, >15 Jahre) | Dezinkifizierung DZR/Messing | Festsitzendes Ventil | Dichtmasse versagt |
| Premium-Segelboot (12–18 m) | Festsitzendes Ventil (mangels Betätigung) | Galvanische Korrosion (Marina) | Bewuchsblockade |
| Produktions-Motoryacht (<15 Jahre) | Galvanische Korrosion (Landstrom!) | Einfache Schlauchschellen | Fehlende Holzpfropfen |
| Produktions-Motoryacht (>15 Jahre) | Dezinkifizierung | Elektrolyse-Schaden | Festsitzendes Ventil |
| Superyacht | Galvanische Korrosion (komplexes System) | Bewuchsblockade (AC-System) | Unzugängliche Ventile |
| Charter-Boot | Festsitzendes Ventil (keine Wartung) | Fehlende Holzpfropfen | Schlauchschellen lose |
| US-Boot (ältere) | Gate-Ventile als Seeventile | Yellow Brass | PVC-Ventile unter WL |

(Confidence: estimated — Survey-Statistiken, IIMS)

---

## 2. Zukunftstechnologien

### 2.1 Smart Seacocks — Sensorüberwachung

Moderne Ansätze zur Seeventil-Überwachung:

**Aktuelle Entwicklungen:**
- **Siren Marine / Navico**: Wasserstandsensoren in Bilge + Alarmierung per GSM/Satellite
- **Victron Cerbo GX**: Integration von Bilge-Alarmen in Monitoring-System
- **Yacht Sentinel**: Feuchtesensoren an jedem Seeventil, Cloud-Monitoring
- **Concept (F&E)**: Piezoelektrische Durchflusssensoren in Seeventilen
  - Erkennung von Mikroleckagen <5 ml/min
  - Vibrationsmuster für Zustandsüberwachung
  - Noch keine marktreifen Produkte (Stand 2026)

**AYDI-Relevanz**: Pipeline C (Text) kann Sensoralarme auswerten. Pipeline A (Strukturiert) kann Sensorpositionen im CAD-Modell validieren.

| Technologie | TRL | Hersteller | Verfügbarkeit | Preis |
|---|---|---|---|---|
| Bilge-Wasserstandsensor | 9 | Siren Marine | Verfügbar | 150–300 EUR |
| Feuchte-Sensor pro Ventil | 7 | Yacht Sentinel | Beta | 80–120 EUR/Sensor |
| Durchfluss-Sensor integriert | 4 | F&E / Uni Southampton | Prototyp | n/a |
| Akustische Leckage-Erkennung | 5 | F&E / MARIN | Labor | n/a |
| Elektr. Fernbetätigung | 8 | Vetus (BOW PRO) | Verfügbar | 400–800 EUR/Ventil |

(Confidence: documented + estimated — Hersteller-Websites, Marine Technology Reporter 2025)

### 2.2 Komposit-Evolution

**Glasfaserverstärkter Polyester (GFK)** — Erste Generation (TruDesign/Marelon):
- Bewährt seit 1990er
- FDA/NSF-zugelassen
- Keine galvanische Korrosion
- Schwäche: UV-Empfindlichkeit, begrenzte Temperaturbeständigkeit

**Kohlefaserverstärkte Polymere (CFK)** — Zweite Generation (experimentell):
- Höhere Festigkeit bei geringerem Gewicht
- Problem: CFK ist elektrisch leitfähig → galvanische Korrosion möglich
- Kein marktreifes Produkt für Seeventile (Stand 2026)

**Hochleistungsthermoplaste** — Dritte Generation:
- PEEK (Polyetheretherketon): Temperaturbeständig bis 250°C, chemisch inert
- PPS (Polyphenylensulfid): UV-beständig, hohe Festigkeit
- Problem: Materialkosten 5–10× GFK
- TruDesign evaluiert PPS für Premium-Linie (angekündigt 2027)

**3D-gedruckte Bronze-Ventile**:
- Selektives Lasersintern (SLM) von CuSn10-Pulver
- Ermöglicht komplexe Innengeometrien für optimierten Durchfluss
- Aktuell nur für Superyacht-Sonderanfertigungen (>50 mm DN)
- Qualitätsnachweis: CT-Scan + hydrostatische Prüfung

(Confidence: estimated — Fachmessen Boot Düsseldorf 2025, METS Amsterdam 2025)

### 2.3 Elektrisch betätigte Seeventile

**Vetus BOW PRO Serie** (verfügbar):
- 12V/24V elektrischer Antrieb auf Kugelventil
- Fernbedienung vom Steuerstand
- Notfall-Handbetätigung möglich
- Preis: 450–850 EUR je nach Größe

**Lewmar (Konzept)**:
- Integration in Yacht-Bussystem (NMEA 2000 / CAN)
- Automatisches Schließen bei Bilge-Alarm
- Noch keine CE-Zulassung für Sicherheitsventile

**AYDI-Bewertung**: Elektrisch betätigte Seeventile erhalten Bonus-Punkte im Compliance-Modul für Kategorie-A-Yachten, da sie Fernbedienung aller Ventile von einem zentralen Punkt ermöglichen.

(Confidence: documented — Vetus Katalog 2025/26, estimated — Lewmar Produktankündigung)

---

## 3. Best Practices nach Revier & Klimazone

### 3.1 Ostsee / Nordeuropa (Brackwasser, kalt)

| Aspekt | Empfehlung | Begründung |
|---|---|---|
| Material | Bronze C83600 oder Komposit | Geringere Korrosionsbelastung als Vollsalz |
| Anoden | Zinkanoden, Prüfung alle 2 Jahre | Brackwasser = reduzierte Anodenlebensdauer |
| Antifouling Ventil | Wenig notwendig | Geringer Bewuchs unter 15°C |
| Winterlager | Alle Ventile OFFEN lassen im Winterlager an Land | Kondenswasser-Ablauf |
| Inspektionsintervall | Alle 2 Jahre ausreichend (Brackwasser) | Niedrigere Korrosionsrate |
| Frostschutz | Kühlwasser-Seeventil mit Frostschutz spülen | Eisbildung kann Ventilkörper sprengen |

### 3.2 Mittelmeer (Volles Seewasser, warm)

| Aspekt | Empfehlung | Begründung |
|---|---|---|
| Material | Bronze C83600 ODER Komposit — kein Messing! | Hohe Korrosionsrate in warmem Seewasser |
| Anoden | Zinkanoden, Prüfung jährlich | Warmes Salzwasser = maximale Korrosion |
| Antifouling Ventil | Empfohlen — Bewuchs verschließt Ventile | Seepocken ab 18°C Wassertemp. |
| Bewuchsschutz | Groco-Ventile mit Bewuchsschutz-Option | Muscheln im Kühlwassereinlass |
| Inspektionsintervall | Jährlich — kein Kompromiss | Dezinkifizierung bei Messing ab 3–5 Jahren |
| Elektrolyse | Landstrom-Galvanischer Isolator PFLICHT | Marina-Strom verursacht Elektrolyse |

### 3.3 Tropen (Volles Seewasser, heiß, UV-intensiv)

| Aspekt | Empfehlung | Begründung |
|---|---|---|
| Material | Bronze C92200 (Navy G) bevorzugt | Höchste Korrosionsbeständigkeit |
| Komposit | NUR mit UV-Schutzlackierung | Tropensonue zerstört GFK in 5–8 Jahren |
| Bewuchs | Starker Bewuchsschutz + Gitter am Einlass | Tropischer Bewuchs extrem aggressiv |
| Inspektionsintervall | Alle 6 Monate Funktionsprüfung | Beschleunigte Alterung aller Materialien |
| Holzpfropfen | 2× Satz mitführen (Backup) | Entfernte Reviere, keine schnelle Hilfe |
| Wassermacher | Separater Borddurchlass mit Vorfilter | Tropisches Wasser = mehr Organismen |

### 3.4 Gezeitenreviere (UK, Bretagne, Nordsee)

| Aspekt | Empfehlung | Begründung |
|---|---|---|
| Trockenfallen | Alle Ventile VOR dem Trockenfallen schließen | Schmutz/Sand im Ventil bei Trockenfall |
| Mushroom-Schutz | Schutzgitter über pilzförmigen Durchlässen | Sand/Steine beim Aufsetzen |
| Backing-Block | Verstärkter Backing-Block empfohlen | Stoßbelastung beim Aufsetzen |
| Material | Bronze bevorzugt | Mechanisch robuster als Komposit |

### 3.5 Süßwasser (Binnenreviere)

| Aspekt | Empfehlung | Begründung |
|---|---|---|
| Material | Komposit ausreichend, Bronze optional | Keine Salzwasser-Korrosion |
| Messing | Unter Umständen tolerierbar (aber NICHT empfohlen) | Dezinkifizierung in Süßwasser minimal |
| Inspektionsintervall | Alle 3–5 Jahre ausreichend | Deutlich geringere Belastung |
| Anoden | Magnesium-Anoden für Süßwasser | Zink schützt nicht in Süßwasser |

(Confidence: documented — Praktische Erfahrung, Yachtsurvey-Literatur, Nigel Calder "Boatowner's Mechanical and Electrical Manual")

---

## 4. Regional Sourcing

### 4.1 Europa — Bezugsquellen

| Händler | Land | Spezialität | Online | Lieferzeit DE |
|---|---|---|---|---|
| SVB (svb-marine.de) | DE | Vollsortiment Bronze + Komposit | Ja | 1–3 Tage |
| Toplicht (toplicht.de) | DE | Blakes, Guidi, TruDesign | Ja | 2–4 Tage |
| Compass24 (compass24.de) | DE | Guidi, Vetus, Osculati | Ja | 1–3 Tage |
| AWN (awn.de) | DE | Breites Sortiment, guter Service | Ja | 2–4 Tage |
| Bukh-Bremen | DE | Spezialist für Borddurchlässe | Ja | 3–5 Tage |
| Force4 (force4.co.uk) | UK | Blakes, TruDesign | Ja | 5–8 Tage |
| Sea-Sure (seasure.co.uk) | UK | Blakes OEM-Vertrieb | Ja | 5–8 Tage |
| Accastillage Diffusion | FR | Plastimo, Guidi | Ja | 4–7 Tage |
| Navimo / Plastimo Direct | FR | Plastimo Eigenmarke | Ja | 5–8 Tage |
| Osculati Direct | IT | Osculati Vollsortiment | Ja | 5–10 Tage |

### 4.2 Nordamerika

| Händler | Land | Spezialität | Bemerkung |
|---|---|---|---|
| Defender (defender.com) | USA | Groco, Perko, Forespar | Größte Auswahl, gute Preise |
| West Marine | USA | Vollsortiment | Filialnetz + Online |
| Hamilton Marine | USA | Groco, Buck Algonquin | Spezialist Ostküste |
| Fisheries Supply | USA | Kommerziell + Yacht | Groco Premium-Händler |

### 4.3 Ozeanien / Asien

| Händler | Land | Spezialität | Bemerkung |
|---|---|---|---|
| BurnscoMarine | NZ | TruDesign (Heimatmarkt) | Direkt vom Hersteller |
| Whitworths | AU | TruDesign, Guidi | Größter AU-Händler |
| CH Marine | HK | Guidi, Apollo | Asien-Hub für europäische Marken |

(Confidence: documented — Händler-Websites, Stand 2025/26)

---

## 5. Zweck dieser Wissensdatei

### 5.1 Rolle im AYDI-System

Diese Wissensdatei dient als technische Referenz für folgende AYDI-Module:

| Modul | Nutzung dieser Datei |
|---|---|
| **materials** | Werkstoffidentifikation, Legierungsvergleich, Lebensdauer-Prognose |
| **structural** | Wandstärken, Backing-Block-Dimensionierung, Lastverteilung |
| **compliance** | ISO 9093, ABYC H-27, CE/RCD Anforderungen |
| **service_patterns** | Typische Fehlerbilder, Wartungsintervalle, Alterungskurven |
| **cost** | Material- und Arbeitskosten für Austausch/Neubau |
| **production** | Einbaumethoden, Werkzeug-Anforderungen |
| **visual** (Pipeline B) | Zustandsbeurteilung aus Fotos: Korrosion, Bewuchs, Risse |

### 5.2 Confidence-Zuordnung für Seeventile

| Datenquelle | Confidence | Beispiel |
|---|---|---|
| CAD-Modell mit DN-Angabe | measured | "DN38 Bronze-Seeventil an Position Frame 4" |
| Herstellerdatenblatt | documented | "Groco BV-1500, C83600, DN38" |
| Foto klar, Ventil sichtbar | visual_high | "Bronze-Kugelventil, visuell intakt" |
| Foto unklar, teilweise verdeckt | visual_medium | "Vermutlich Komposit-Ventil, Zustand unklar" |
| Nur Bootstyp bekannt | estimated | "Bavaria 40: typisch 6× DN25 Bronze" |
| Service-Bericht | documented | "2023: Seeventil Stb. Toilette ausgetauscht" |

(Confidence: documented)

---

## 6. Pydantic-Modelle

### 6.1 SeacockSpec — Spezifikation eines Seeventils

```python
from pydantic import BaseModel, Field
from typing import Optional, Literal
from enum import Enum


class SeacockMaterial(str, Enum):
    BRONZE_C83600 = "bronze_c83600"         # 85-5-5-5, Standard
    BRONZE_C84400 = "bronze_c84400"         # 81 Red Brass
    BRONZE_C92200 = "bronze_c92200"         # Navy G, Premium
    BRONZE_C95800 = "bronze_c95800"         # Nickel-Alu-Bronze
    DZR_BRASS = "dzr_brass"                 # Entzinkungsbeständiges Messing
    YELLOW_BRASS = "yellow_brass"           # GEFAHR — dezinkifizierungsanfällig!
    COMPOSITE_GFK = "composite_gfk"         # Glasfaserverstärkter Polyester
    COMPOSITE_MARELON = "composite_marelon" # Forespar Markenname
    COMPOSITE_TRUDESIGN = "composite_trudesign"  # TruDesign NZ
    STAINLESS_316L = "stainless_316l"       # Nur in Spezialfällen
    UNKNOWN = "unknown"


class SeacockType(str, Enum):
    BALL_VALVE = "ball_valve"               # Kugelventil — Standard modern
    TAPERED_PLUG = "tapered_plug"           # Kegelventil — traditionell
    GATE_VALVE = "gate_valve"               # Schieberventil — VERBOTEN!
    BUTTERFLY_VALVE = "butterfly_valve"     # Klappenventil — nur >DN50
    QUARTER_TURN = "quarter_turn"           # 1/4-Drehung (= Ball oder Plug)
    UNKNOWN = "unknown"


class SeacockApplication(str, Enum):
    COOLING_WATER_INTAKE = "cooling_water_intake"   # Kühlwassereinlass Motor
    EXHAUST_WET = "exhaust_wet"                     # Nassauspuff
    TOILET_INTAKE = "toilet_intake"                 # WC Seewassereinlass
    TOILET_DISCHARGE = "toilet_discharge"           # WC Abwasserauslass
    BILGE_DISCHARGE = "bilge_discharge"             # Bilgenpumpe Auslass
    GALLEY_DRAIN = "galley_drain"                   # Pantry Abfluss
    SINK_DRAIN = "sink_drain"                       # Waschbecken Abfluss
    SHOWER_DRAIN = "shower_drain"                   # Dusche Abfluss
    AC_INTAKE = "ac_intake"                         # Klimaanlage Seewasser
    AC_DISCHARGE = "ac_discharge"                   # Klimaanlage Auslass
    GENERATOR_COOLING = "generator_cooling"         # Generator Kühlwasser
    WATERMAKER_INTAKE = "watermaker_intake"          # Wassermacher Einlass
    SPEED_LOG = "speed_log"                         # Log-Geber
    DEPTH_SOUNDER = "depth_sounder"                 # Echolot-Geber
    ANCHOR_WASH = "anchor_wash"                     # Ankerspülung
    DECK_WASH = "deck_wash"                         # Deckwaschanlage
    LIVEWELL = "livewell"                           # Köderbecken
    FIRE_SYSTEM = "fire_system"                     # Feuerlöschanlage Seewasser
    OTHER = "other"


class SeacockConditionRating(str, Enum):
    EXCELLENT = "excellent"         # Neuwertiger Zustand (Score 90–100)
    GOOD = "good"                   # Guter Zustand, normale Gebrauchsspuren (70–89)
    FAIR = "fair"                   # Akzeptabel, Wartung empfohlen (50–69)
    POOR = "poor"                   # Mangelhaft, Austausch planen (30–49)
    CRITICAL = "critical"          # SOFORTIGER Austausch! Sinkgefahr! (0–29)
    NOT_ASSESSED = "not_assessed"   # Nicht beurteilbar


class SeacockSpec(BaseModel):
    """Spezifikation eines einzelnen Seeventils."""

    model_config = {"from_attributes": True}

    # Identifikation
    id: Optional[str] = Field(None, description="Eindeutige ID im AYDI-System, z.B. 'SV-001'")
    position: Optional[str] = Field(None, description="Position am Boot, z.B. 'Steuerbord, Frame 4, unter Pantry'")
    application: SeacockApplication = Field(..., description="Verwendungszweck")

    # Typ und Material
    valve_type: SeacockType = Field(..., description="Ventilbauart")
    material: SeacockMaterial = Field(..., description="Werkstoff des Ventilkörpers")
    material_note: Optional[str] = Field(None, description="Zusatzinfo zum Werkstoff")

    # Maße (alle in mm)
    nominal_diameter_mm: int = Field(..., ge=10, le=200, description="Nennweite in mm (DN)")
    thread_type: Optional[str] = Field(None, description="Gewindeart: BSP, NPT, metrisch")
    thread_size: Optional[str] = Field(None, description="Gewindegröße, z.B. '1-1/2 BSP'")
    body_length_mm: Optional[int] = Field(None, description="Baulänge Ventilkörper in mm")
    flange_diameter_mm: Optional[int] = Field(None, description="Flanschdurchmesser in mm")
    wall_thickness_mm: Optional[float] = Field(None, description="Wandstärke in mm")
    hose_barb_diameter_mm: Optional[int] = Field(None, description="Schlauchtülle Außendurchmesser in mm")

    # Hersteller
    manufacturer: Optional[str] = Field(None, description="Hersteller, z.B. 'Groco', 'TruDesign'")
    model_number: Optional[str] = Field(None, description="Modellnummer, z.B. 'BV-1500'")

    # Installation
    depth_below_waterline_mm: Optional[int] = Field(None, description="Tiefe unter Wasserlinie in mm")
    backing_plate: Optional[bool] = Field(None, description="Backing-Block vorhanden?")
    backing_plate_material: Optional[str] = Field(None, description="Material Backing-Block")
    bedding_compound: Optional[str] = Field(None, description="Verwendete Dichtmasse")
    double_hose_clamps: Optional[bool] = Field(None, description="Doppelte Schlauchschellen?")

    # Normen
    iso_9093_compliant: Optional[bool] = Field(None, description="ISO 9093 konform?")
    abyc_h27_compliant: Optional[bool] = Field(None, description="ABYC H-27 konform?")
    classification_approved: Optional[str] = Field(None, description="Klassifikation, z.B. 'Lloyd's', 'DNV-GL'")

    # Kosten
    unit_cost_eur: Optional[float] = Field(None, description="Stückpreis in EUR")
    installation_cost_eur: Optional[float] = Field(None, description="Einbaukosten in EUR")
    replacement_interval_years: Optional[int] = Field(None, description="Empfohlenes Austauschintervall in Jahren")

    # Confidence
    confidence: str = Field("estimated", description="measured|calculated|visual_high|visual_medium|estimated|documented|benchmark")


class SeacockCondition(BaseModel):
    """Zustandsbewertung eines Seeventils."""

    model_config = {"from_attributes": True}

    seacock_id: str = Field(..., description="Referenz auf SeacockSpec.id")
    assessment_date: Optional[str] = Field(None, description="Datum der Bewertung, ISO 8601")
    assessor: Optional[str] = Field(None, description="Prüfer / Surveyor")

    # Gesamtbewertung
    condition_rating: SeacockConditionRating = Field(..., description="Gesamtzustand")
    condition_score: int = Field(..., ge=0, le=100, description="Score 0–100")

    # Einzelbefunde
    valve_operates_freely: Optional[bool] = Field(None, description="Ventil lässt sich leichtgängig betätigen?")
    handle_intact: Optional[bool] = Field(None, description="Griff intakt und fest?")
    no_visible_corrosion: Optional[bool] = Field(None, description="Keine sichtbare Korrosion?")
    no_dezincification: Optional[bool] = Field(None, description="Keine Dezinkifizierung? (nur Kupferlegierungen)")
    no_weeping: Optional[bool] = Field(None, description="Kein Tropfen/Sickern?")
    hose_connection_secure: Optional[bool] = Field(None, description="Schlauchverbindung fest?")
    double_clamps_present: Optional[bool] = Field(None, description="Doppelte Schlauchschellen vorhanden?")
    backing_plate_intact: Optional[bool] = Field(None, description="Backing-Block intakt?")
    bedding_intact: Optional[bool] = Field(None, description="Dichtmasse intakt?")
    no_biofouling: Optional[bool] = Field(None, description="Kein blockierender Bewuchs?")
    emergency_plug_present: Optional[bool] = Field(None, description="Notholzpfropfen vorhanden?")

    # Dezinkifizierungs-Spezialtest
    dezincification_test_performed: Optional[bool] = Field(None, description="Salpetersäure-Test durchgeführt?")
    dezincification_test_result: Optional[str] = Field(None, description="Ergebnis: 'bestanden' / 'dezinkifiziert' / 'nicht durchgeführt'")

    # Visuelle Befunde
    photo_available: Optional[bool] = Field(None, description="Foto vorhanden?")
    visual_findings: Optional[list[str]] = Field(None, description="Liste visueller Befunde")

    # Empfehlung
    recommendation: Optional[str] = Field(None, description="Handlungsempfehlung")
    urgency: Optional[Literal["sofort", "innerhalb_30_tage", "nächstes_haul_out", "monitoring"]] = Field(
        None, description="Dringlichkeit der Maßnahme"
    )

    # Confidence
    confidence: str = Field("visual_medium", description="Confidence der Bewertung")


class SeacockSystemAssessment(BaseModel):
    """Gesamtbewertung aller Seeventile eines Bootes."""

    model_config = {"from_attributes": True}

    # Boot-Referenz
    boat_id: Optional[str] = Field(None, description="AYDI Boot-ID")
    boat_name: Optional[str] = Field(None, description="Bootsname")
    boat_type: Optional[str] = Field(None, description="Bootstyp, z.B. 'Bavaria 40 Cruiser'")
    boat_year: Optional[int] = Field(None, description="Baujahr")
    hull_material: Optional[str] = Field(None, description="Rumpfmaterial: GFK, Stahl, Alu, Holz")

    # Seeventil-Inventar
    total_seacocks: int = Field(..., ge=0, description="Gesamtanzahl Seeventile")
    seacocks_below_waterline: int = Field(..., ge=0, description="Davon unterhalb Wasserlinie")
    seacocks_assessed: int = Field(..., ge=0, description="Davon bewertet")

    # Materialverteilung
    count_bronze: int = Field(0, description="Anzahl Bronze-Ventile")
    count_composite: int = Field(0, description="Anzahl Komposit-Ventile")
    count_brass_danger: int = Field(0, description="Anzahl Messing-Ventile (GEFAHR!)")
    count_unknown_material: int = Field(0, description="Anzahl unbekanntes Material")

    # Typ-Verteilung
    count_ball_valve: int = Field(0, description="Anzahl Kugelventile")
    count_tapered_plug: int = Field(0, description="Anzahl Kegelventile")
    count_gate_valve_danger: int = Field(0, description="Anzahl Schieberventile (VERBOTEN!)")

    # Gesamtbewertung
    system_score: int = Field(..., ge=0, le=100, description="Gesamtscore 0–100")
    worst_seacock_score: int = Field(..., ge=0, le=100, description="Schlechtester Einzelscore")
    critical_findings: list[str] = Field(default_factory=list, description="Kritische Befunde")
    warnings: list[str] = Field(default_factory=list, description="Warnungen")
    recommendations: list[str] = Field(default_factory=list, description="Empfehlungen")

    # Normen-Compliance
    all_iso_9093_compliant: Optional[bool] = Field(None, description="Alle Ventile ISO 9093 konform?")
    all_abyc_h27_compliant: Optional[bool] = Field(None, description="Alle Ventile ABYC H-27 konform?")
    emergency_plugs_complete: Optional[bool] = Field(None, description="Notholzpfropfen für alle Durchlässe?")

    # Kosten
    estimated_replacement_cost_eur: Optional[float] = Field(None, description="Geschätzte Gesamtkosten Austausch aller kritischen Ventile")
    estimated_full_refit_cost_eur: Optional[float] = Field(None, description="Geschätzte Kosten Komplett-Erneuerung")

    # Einzelbewertungen
    individual_assessments: list[SeacockCondition] = Field(
        default_factory=list, description="Einzelbewertungen pro Ventil"
    )

    # Confidence
    confidence: str = Field("estimated", description="Confidence der Gesamtbewertung")
```

### 6.2 Scoring-Logik für Seeventile

```python
def calculate_seacock_score(condition: dict) -> int:
    """
    Berechnet den Zustandsscore eines Seeventils.
    
    Scoring-Regeln (Score 0–100):
    - Basiswert: 100
    - Abzüge für jeden Mangel
    - KRITISCHE Mängel: sofort auf max. 29
    """
    score = 100
    
    # KRITISCHE MÄNGEL — Score sofort ≤29
    if condition.get("material") == "yellow_brass":
        return 10  # Messing = SOFORT AUSTAUSCHEN
    if condition.get("valve_type") == "gate_valve":
        return 15  # Schieberventil = SOFORT AUSTAUSCHEN
    if condition.get("dezincification_test_result") == "dezinkifiziert":
        return 5   # Dezinkifiziert = AKUTE SINKGEFAHR
    if condition.get("valve_operates_freely") is False:
        score = min(score, 25)  # Festsitzendes Ventil = kann nicht geschlossen werden
    
    # SCHWERE MÄNGEL — jeweils -15 bis -25
    if condition.get("no_visible_corrosion") is False:
        score -= 20
    if condition.get("no_weeping") is False:
        score -= 25  # Tropfendes Ventil!
    if condition.get("handle_intact") is False:
        score -= 15
    if condition.get("hose_connection_secure") is False:
        score -= 20
    
    # MITTLERE MÄNGEL — jeweils -5 bis -10
    if condition.get("double_clamps_present") is False:
        score -= 10
    if condition.get("backing_plate_intact") is False:
        score -= 10
    if condition.get("bedding_intact") is False:
        score -= 10
    if condition.get("no_biofouling") is False:
        score -= 5
    
    # LEICHTE MÄNGEL — jeweils -2 bis -5
    if condition.get("emergency_plug_present") is False:
        score -= 5
    
    return max(0, min(100, score))


def calculate_system_score(individual_scores: list[int]) -> int:
    """
    Gesamtscore = gewichteter Durchschnitt.
    
    REGEL: Der Gesamtscore kann nie höher sein als
    (schlechtester_Einzelscore + 20), da ein einziges
    versagendes Seeventil das Boot sinken lässt.
    """
    if not individual_scores:
        return 0
    
    avg = sum(individual_scores) / len(individual_scores)
    worst = min(individual_scores)
    
    # Gesamtscore darf nie mehr als 20 Punkte über dem schlechtesten liegen
    return int(min(avg, worst + 20))
```

(Confidence: documented — AYDI-Scoring-Framework)

---

## 7. Grundlagen

### 7.0 Systemübersicht — Wie ein Seeventil-System aufgebaut ist

```
AUSSEN (Seewasser)                    INNEN (Bilge / Maschinenraum)
                                      
    ┌──────────┐                      
    │Seewasser │                      
    └────┬─────┘                      
         │                            
    ┌────▼─────┐                      
    │Mushroom- │ ← Pilzförmiger Borddurchlass (Skin Fitting)
    │Durchlass │    Material: Bronze C83600 oder Komposit
    │(außen)   │    Dichtung: Dichtmasse (Sikaflex 291 / 3M 4200)
    └────┬─────┘    
         │ ← GFK-Rumpflaminat (4–12 mm)
    ┌────▼─────┐    
    │Backing-  │ ← Lastverteilungsplatte
    │Block     │    Material: G10, GFK, Marine-Sperrholz
    │(innen)   │    Dichtung: Dichtmasse zum Laminat
    └────┬─────┘    
         │ ← O-Ring oder Flachdichtung
    ┌────▼─────┐    
    │Seeventil │ ← Absperrventil (Ball Valve / Tapered Plug)
    │          │    Material: Bronze oder Komposit
    │  ═══╪═══ │ ← Kugel/Küken (90° Vierteldrehung)
    │    /     │    
    │   /      │ ← Griff (Schließen = quer zum Durchfluss)
    └────┬─────┘    
         │ ← Schlauchtülle (Hose Barb)
    ┌────▼─────┐    
    │Schlauch- │ ← 2× Schlauchschellen (316L, ≥12 mm breit)
    │schellen  │    
    │(doppelt!)│    
    └────┬─────┘    
         │          
    ┌────▼─────┐    
    │Schlauch  │ ← Marine-Spiralschlauch, Sanitärschlauch etc.
    │          │    Passender Typ für Anwendung
    └────┬─────┘    
         │          
    ┌────▼─────┐    
    │System    │ ← Motor, WC, Bilgenpumpe, Klimaanlage etc.
    └──────────┘    
```

**Jede einzelne Verbindung in dieser Kette kann versagen. Jedes Versagen unterhalb der Wasserlinie = potenzielles SINKEN.**

### 7.0.1 Anzahl Borddurchlässe nach Bootstyp

| Bootstyp | LOA | Typische Anzahl | Unter WL | Über WL |
|---|---|---|---|---|
| Daysailer / Jolle | 5–7 m | 1–3 | 0–1 | 1–2 |
| Segelboot Küste | 8–10 m | 5–8 | 3–5 | 2–3 |
| Segelboot Offshore | 10–14 m | 7–12 | 5–8 | 2–4 |
| Segelboot Blauwasser | 14–18 m | 10–16 | 7–12 | 3–4 |
| Motoryacht Küste | 8–12 m | 6–10 | 4–7 | 2–3 |
| Motoryacht Offshore | 12–18 m | 10–18 | 7–14 | 3–4 |
| Superyacht | 18+ m | 18–30+ | 14–25+ | 4–5+ |

**AYDI-Regel**: Die Gesamtbewertung eines Seeventil-Systems kann nie besser sein als (schlechtestes Einzelventil + 20 Punkte). Ein einziges versagendes Ventil genügt zum Sinken.

(Confidence: documented — Survey-Statistiken, Werften-Stücklisten)

### 7.1 Ventiltypen

#### 7.1.1 Kugelventil (Ball Valve)

Das Kugelventil ist der **moderne Standard** für Seeventile. Eine durchbohrte Kugel wird mit 90°-Drehung (Vierteldrehung) geöffnet oder geschlossen.

**Vorteile:**
- Schnelle Bedienung: 90° = offen↔geschlossen
- Voller Durchfluss bei Öffnung (kein Strömungswiderstand)
- Zuverlässige Dichtung durch PTFE- oder Delrin-Sitze
- Griffposition zeigt sofort an: offen (parallel zum Rohr) oder geschlossen (quer)

**Nachteile:**
- PTFE-Sitze können bei Nichtbenutzung verkleben
- Bei Verschmutzung kann sich Kugel nicht mehr drehen
- Keine Möglichkeit der Teildrosselung (Kavitation bei Teillast)

**Hersteller & Modelle:**

| Hersteller | Modell | Material | DN-Bereich | Preis EUR |
|---|---|---|---|---|
| Groco | BV-Serie | C83600 Bronze | 19–76 mm | 85–450 |
| Groco | IBV-Serie | C83600 mit integriertem Borddurchlass | 19–50 mm | 120–380 |
| Guidi | 2060 Serie | C83600 Bronze | 13–50 mm | 35–180 |
| TruDesign | 90-Serie | GFK-Komposit | 19–50 mm | 45–165 |
| Blakes | BB-Serie | C83600 Bronze | 19–50 mm | 75–320 |
| Vetus | FULL FLOW | Bronze / Komposit | 19–50 mm | 55–220 |
| Apollo | 70-100 Serie | C83600 Bronze | 13–50 mm | 25–120 |

(Confidence: documented — Herstellerkataloge 2025/26)

#### 7.1.2 Kegelventil (Tapered Plug Valve)

Das traditionelle Seeventil. Ein konischer Küken (Plug) wird mit 90° gedreht. In der Schifffahrt seit über 150 Jahren bewährt.

**Vorteile:**
- Extrem robust und langlebig (30+ Jahre bei Pflege)
- Kann gewartet werden: Küken herausnehmen, nachschleifen
- Auch bei jahrelanger Nichtbenutzung noch betätigbar (nach Lösen)
- Traditionell auf hochwertigsten Yachten

**Nachteile:**
- Muss regelmäßig gefettet werden (Küken ↔ Gehäuse)
- Nicht voller Durchfluss (konische Form reduziert Querschnitt)
- Schwerer als Kugelventil
- Teurer in der Herstellung

**Hersteller & Modelle:**

| Hersteller | Modell | Material | DN-Bereich | Preis EUR |
|---|---|---|---|---|
| Blakes | Lever Type | C83600 Bronze | 19–50 mm | 110–420 |
| Groco | SC-Serie (legacy) | C83600 Bronze | 19–50 mm | 150–500 |
| Perko | 0844 / 0805 | C83600 Bronze | 19–50 mm | 95–350 |

(Confidence: documented — Herstellerkataloge)

#### 7.1.3 Schieberventil (Gate Valve) — VERBOTEN!

**⚠️ WARNUNG: Gate-Ventile dürfen NIEMALS als Seeventile verwendet werden!**

Gründe für das Verbot:
1. **Kein positiver Verschluss**: Schieber kann sich durch Vibration öffnen
2. **Korrosionsanfällig**: Schieber korrodiert in Führung fest
3. **Langsame Bedienung**: Viele Umdrehungen zum Schließen → zu langsam im Notfall
4. **Versagen im Teilöffnungszustand**: Erosion des Schiebers bei Teilöffnung
5. **ABYC H-27 verbietet Gate-Ventile explizit**
6. **ISO 9093 lässt Gate-Ventile nicht als "Seeventil" zu**

**AYDI-Bewertung**: Jedes Gate-Ventil unterhalb der Wasserlinie = Score 15, Empfehlung "SOFORT AUSTAUSCHEN", Dringlichkeit "sofort".

Dennoch finden Surveyor Gate-Ventile regelmäßig auf:
- Älteren US-Produktionsbooten (vor 1995)
- DIY-Installationen (Baumarkt-Ventile)
- Billigbooten aus Fernost

(Confidence: documented — ABYC H-27, ISO 9093, IIMS Survey Standards)

#### 7.1.4 Klappenventil (Butterfly Valve)

Nur für große Durchmesser (>DN50) auf Superyachten oder kommerziellen Schiffen relevant.

| Eigenschaft | Wert |
|---|---|
| Einsatzbereich | DN50–DN200 |
| Vorteile | Leicht, kompakt, großer Durchfluss |
| Nachteile | Nicht geeignet für kleine Boote |
| Hersteller | Johnson Pump, Alfa Laval (kommerziell) |
| Preis | 200–2.000 EUR |

(Confidence: documented)

### 7.2 Materialien — Detailwissen

#### 7.2.1 Bronze-Legierungen im Detail

**KRITISCHER HINWEIS**: Nicht jede "Bronze" ist gleich. Die Legierungszusammensetzung bestimmt die Seewasserbeständigkeit.

| Legierung | UNS | Cu | Sn | Zn | Pb | Andere | Name | Seewasser? |
|---|---|---|---|---|---|---|---|---|
| C83600 | C83600 | 85% | 5% | 5% | 5% | — | 85-5-5-5 Leaded Red Brass | ✅ JA — Standard |
| C84400 | C84400 | 81% | 3% | 7% | 9% | — | 81 Red Brass | ⚠️ Bedingt (höherer Zn) |
| C92200 | C92200 | 88% | 6% | 1.5% | 1.5% | 3% Ni | Navy G / Valve Bronze | ✅ JA — Premium |
| C95800 | C95800 | 81% | — | — | — | 9% Al, 4% Ni, 4% Fe | Nickel-Alu-Bronze | ✅ JA — Propeller |
| C85200 | C85200 | 72% | 1% | 24% | 3% | — | Yellow Brass | ❌ NEIN — GEFAHR! |
| C36000 | C36000 | 61% | — | 36% | 3% | — | Free-Cutting Brass | ❌ NEIN — GEFAHR! |
| CW602N | — | 63% | — | 34% | 2.5% | 0.2% As | DZR Brass (EN) | ⚠️ Bedingt (mit As-Zugabe) |

**Faustregel**: Je höher der Zinkanteil, desto größer die Dezinkifizierungsgefahr. Über 15% Zink = NICHT für Seewasser-Seeventile geeignet.

(Confidence: documented — ASTM B61, B62, B505, CDA Copper Development Association)

#### 7.2.2 Dezinkifizierung — Die unsichtbare Gefahr

Dezinkifizierung ist der **häufigste und gefährlichste** Versagensmechanismus bei Seeventilen aus Messing oder zinkhaltigen Kupferlegierungen.

**Mechanismus:**
1. Selektive Korrosion löst Zink aus der Legierung
2. Zurück bleibt poröses, schwammiges Kupfer
3. Das Bauteil behält seine Form — sieht von außen normal aus!
4. Die Festigkeit sinkt auf 10–20% des Originalwerts
5. Ein leichter Schlag, eine Vibration → Bruch → Wassereinbruch → SINKEN

**Erkennung:**
- **Visuell**: Rötlich-rosa Verfärbung statt goldgelb (bei Messing)
- **Klopftest**: Dumpfer Klang statt metallisch klingend
- **Kratztest**: Weiche, krümelige Oberfläche mit Messer ritzbar
- **Salpetersäure-Test**: Tropfen 10% HNO₃ auf Oberfläche:
  - Gesundes Bronze/Messing: grünliche Reaktion
  - Dezinkifiziert: rötlich-kupferne Oberfläche sofort sichtbar
- **Professionell**: Metallurgische Schnittprobe + Mikroskop

**AYDI Pipeline B (Visuell)**:
- visual_high: Deutliche rosa Verfärbung erkennbar → Score ≤15
- visual_medium: Mögliche Verfärbung, nicht eindeutig → "Salpetersäure-Test empfohlen"
- visual_low: Ventil kaum sichtbar → "nicht beurteilbar"

**Betroffene Legierungen:**
| Legierung | Zn-Anteil | Dezinkifizierungsrisiko | Zeitraum bis Versagen |
|---|---|---|---|
| C83600 (85-5-5-5) | 5% | Sehr gering | >40 Jahre |
| C84400 (81 Red Brass) | 7% | Gering | >30 Jahre |
| C92200 (Navy G) | 1.5% | Minimal | >50 Jahre |
| CW602N (DZR) | 34% + As | Mittel (inhibiert) | 15–25 Jahre |
| C85200 (Yellow Brass) | 24% | HOCH — GEFAHR | 3–10 Jahre |
| C36000 (Cutting Brass) | 36% | SEHR HOCH — AKUT | 2–5 Jahre |

(Confidence: documented — CDA Technical Report, Steve D'Antonio Marine Consulting)

#### 7.2.3 DZR-Messing (Dezincification Resistant Brass)

DZR-Messing (CW602N nach EN 12164/12165) enthält einen Arsen-Zusatz von ca. 0,02–0,15%, der die Dezinkifizierung hemmt, aber nicht vollständig verhindert.

**Bewertung für Seeventile:**
- In Europa weitverbreitet als kostengünstige Alternative zu Bronze
- Von einigen Klassifikationsgesellschaften akzeptiert (Lloyd's, DNV-GL)
- **ABER**: Nicht so langzeitstabil wie echte Bronze
- **AYDI-Empfehlung**: Akzeptabel für Boote <15 Jahre, danach Bronze empfohlen
- Erkennbar am Stempel "DZR" oder "CR" (Corrosion Resistant) auf dem Ventil

| Eigenschaft | DZR-Messing | C83600 Bronze |
|---|---|---|
| Zinkanteil | 34% | 5% |
| Dezinkifizierung | Gehemmt (nicht unmöglich) | Praktisch unmöglich |
| Festigkeit | Höher | Etwas geringer |
| Kosten | 40–60% von Bronze | 100% (Referenz) |
| Lebensdauer Seewasser | 15–25 Jahre | 30–50+ Jahre |
| AYDI-Empfehlung | Akzeptabel | Bevorzugt |

(Confidence: documented — EN 12164, CDA, Nigel Calder)

#### 7.2.4 Komposit-Materialien

**Glasfaserverstärkter Polyester (GFK) — Marelon / TruDesign**

Komposit-Seeventile haben sich seit den 1990er Jahren als vollwertige Alternative zu Bronze etabliert. Der Markenname "Marelon" (Forespar) ist dabei zum Gattungsbegriff geworden, ähnlich wie TruDesign aus Neuseeland den Markt mit innovativen Komposit-Systemen dominiert.

**Materialzusammensetzung:**
- Matrix: Ungesättigter Polyester oder Vinylester
- Verstärkung: E-Glasfaser, 40–55% Faseranteil
- Füllstoffe: Mineralische Füller für Dimensionsstabilität
- Forespar Marelon: Glasfaserverstärktes Nylon (Polyamid)
- TruDesign: Glasfaserverstärktes Polyester (eigene Rezeptur)

**Vorteile gegenüber Bronze:**
1. **Keine galvanische Korrosion** — das Hauptargument
2. **Leichter** — ca. 60% weniger Gewicht als Bronze
3. **Keine Dezinkifizierung** — offensichtlich
4. **FDA/NSF-zugelassen** — für Trinkwassersysteme
5. **Günstiger** — 30–50% weniger als Bronze
6. **Keine Elektrolyse-Probleme** — isoliert galvanisch

**Nachteile:**
1. **UV-Empfindlichkeit** — Versprödung bei UV-Exposition
2. **Temperaturgrenze** — max. 82°C (Marelon), 93°C (TruDesign)
3. **Mechanisch weniger robust** — bei Punktbelastung Bruchgefahr
4. **Kriechverhalten** — Langzeit-Verformung unter Last
5. **Schwerer zu reparieren** — kein Nachschleifen wie bei Kegelventil
6. **Brandverhalten** — schmilzt bei Feuer (Bronze überlebt)

**ISO 9093-2 Anforderungen für Komposit:**

| Test | Anforderung | Prüfmethode |
|---|---|---|
| Berstdruck | ≥4× Betriebsdruck | Hydrostatisch |
| UV-Beständigkeit | 1.000 h Xenon-Alterung | ISO 4892-2 |
| Kriechfestigkeit | <5% Verformung nach 20 Jahren (extrapoliert) | ISO 899-1 |
| Chemikalien | Beständig gegen Diesel, Öl, Antifouling | Eintauchtest 30 Tage |
| Brandverhalten | Selbstverlöschend, kein Abtropfen | ISO 9094 / UL 94 V-0 |
| Temperatur | Funktionsfähig -30°C bis +82°C | Klimakammertest |

(Confidence: documented — Forespar Marelon Technical Data, TruDesign Engineering Specs)

#### 7.2.5 Edelstahl — Warum NICHT für Seeventile

316L-Edelstahl wird manchmal für Seeventile verwendet, ist aber **nicht ideal**:

- **Spaltkorrosion**: In sauerstoffarmen Spalten (Gewinde, Dichtflächen) korrodiert 316L
- **Galvanische Korrosion**: 316L ist edler als Bronze → zerstört angrenzende Bronze-Teile
- **Kosten**: Teurer als Bronze bei schlechterer Eignung
- **Ausnahme**: Superyachten mit vollständigem 316L-System und ICCP

**AYDI-Empfehlung**: 316L-Seeventile nur bei Superyachten mit professionellem Korrosionsschutz. Für Serienyachten: Bronze oder Komposit.

(Confidence: documented — NACE International, Galvanic Corrosion Data)

### 7.3 Borddurchlass-Typen (Through-Hull Fittings)

#### 7.3.1 Pilzförmiger Borddurchlass (Mushroom Type)

Der Standard-Borddurchlass für Yachten. Außen breiter Flansch ("Pilzkopf"), durch den Rumpf geführt, innen mit Gegenmutter oder Seeventil verschraubt.

| Eigenschaft | Wert |
|---|---|
| Einsatz | Alle Borddurchlässe unter/über Wasserlinie |
| Material | Bronze C83600, C92200, Komposit |
| Gewinde | BSP (Europa), NPT (USA), metrisch (selten) |
| Vorteil | Einfache Montage, bewährt |
| Nachteil | Hervorstehend außen (Strömungswiderstand) |
| Bruchrisiko | Bei Grundberührung kann Pilzkopf abbrechen |

**Hersteller & Modelle:**

| Hersteller | Modell | Material | DN-Bereich | Preis EUR |
|---|---|---|---|---|
| Groco | TH-Serie | C83600 | 13–76 mm | 25–180 |
| Groco | HTH-Serie | C83600, extra lang | 19–50 mm | 35–220 |
| Guidi | 1040 Serie | C83600 | 13–50 mm | 12–85 |
| TruDesign | 90400 Serie | GFK-Komposit | 19–50 mm | 18–75 |
| Blakes | TH-Serie | C83600 | 19–50 mm | 30–145 |
| Forespar | 903/905 | Marelon | 19–50 mm | 15–65 |
| Perko | 0338 | C83600 | 13–50 mm | 20–120 |

(Confidence: documented — Herstellerkataloge 2025/26)

#### 7.3.2 Flansch-Borddurchlass (Flanged Type)

Beide Seiten mit Flansch, verschraubt durch GFK-Laminat oder Backing-Block. Für höchste Belastungen.

| Eigenschaft | Wert |
|---|---|
| Einsatz | Superyachten, kommerzielle Schiffe, >DN50 |
| Material | Bronze C92200, C95800, 316L |
| Vorteil | Höchste Festigkeit, austauschbar ohne Gewinde |
| Nachteil | Aufwändigere Montage, teurer |
| Hersteller | Groco (FF-Serie), Buck Algonquin, Blakes |
| Preis | 150–800 EUR |

#### 7.3.3 Flush-Mount (Bündig)

Bündig mit der Rumpfaußenseite. Für Regattayachten und Superyachten.

| Eigenschaft | Wert |
|---|---|
| Einsatz | Racing, Superyachten (Hydrodynamik) |
| Material | Bronze C95800, 316L, Titan |
| Vorteil | Minimaler Strömungswiderstand |
| Nachteil | Komplexe Montage, sehr teuer |
| Hersteller | Sonderanfertigung, Sparcraft, Hall Spars |
| Preis | 300–2.000 EUR |

#### 7.3.4 Scoop-Einlass (Schöpfeinlass)

Mit integrierter Leitfläche ("Schaufel") für verbesserten Wassereinlass bei Fahrt.

| Eigenschaft | Wert |
|---|---|
| Einsatz | Kühlwassereinlass Motor, WC-Spülung |
| Material | Bronze C83600, Komposit |
| Vorteil | Besserer Durchfluss bei Fahrt |
| Nachteil | Mehr Strömungswiderstand, Bewuchsanfällig |
| Hersteller | Groco (SC-Serie), Vetus |
| Preis | 35–180 EUR |

(Confidence: documented — Herstellerkataloge)

### 7.3.5 Borddurchlass-Positionierung am Rumpf

**Optimale Positionierung:**

| Regel | Begründung |
|---|---|
| Möglichst auf flachem Rumpfabschnitt | Bessere Dichtung, weniger Spannung |
| Nicht auf Kimm-Knick | Mechanische Belastung, schwierige Abdichtung |
| Nicht im Kielbereich | Schwer zugänglich, Grundberührungs-Risiko |
| Einlässe nicht nahe Auslässe | Abwasser/Auspuff nicht in Kühlwasser saugen! |
| Motorkühlwasser tief und mittschiffs | Wasser bei Krängung und Stampfen |
| WC-Auslass nicht im Vorschiff | Geruch bei Ankerliegen (Wind von vorn) |
| Bilgenauslass über WL wenn möglich | Kein Rückfluss, einfacheres Ventil |

**Mindestabstände zwischen Borddurchlässen:**

| Rumpfmaterial | Mindestabstand | Begründung |
|---|---|---|
| GFK (Standardlaminat) | ≥3× DN, min. 100 mm | Laminat-Integrität |
| GFK (Sandwich) | ≥4× DN, min. 150 mm | Kernmaterial nicht schwächen |
| Aluminium | ≥2× DN, min. 80 mm | Wärmeeinflusszone beim Schweißen |
| Stahl | ≥2× DN, min. 80 mm | dto. |
| Holz | ≥3× DN, min. 100 mm | Holzfasern nicht unterbrechen |

**AYDI-Prüfung (Pipeline A — CAD)**: Bei CAD-Import werden Borddurchlass-Positionen automatisch auf korrekte Abstände und Platzierung geprüft. Verletzung der Mindestabstände = Warnung im Compliance-Modul.

(Confidence: documented — ISO 12215, ABYC H-27, Werft-Konstruktionsrichtlinien)

### 7.3.6 Sandwich-Rümpfe — Spezielle Anforderungen

Bei Sandwich-Konstruktionen (z.B. Balsa-Kern, PVC-Schaum-Kern) müssen Borddurchlässe besonders behandelt werden:

| Schritt | Beschreibung | Risiko bei Unterlassung |
|---|---|---|
| 1 | Kernmaterial um Bohrung entfernen (50 mm Radius) | Wasser dringt in Kernmaterial ein |
| 2 | Hohlraum mit Epoxid-Füller (z.B. West System 105+406) füllen | Kernfäulnis, Delamination |
| 3 | Aushärten lassen (24 h) | — |
| 4 | Dann erst Bohrung für Borddurchlass setzen | — |
| 5 | Schnittkante ERNEUT versiegeln | Osmose-Eintritt |

**WARNUNG**: Ein Borddurchlass in einem Sandwich-Rumpf OHNE Kern-Versiegelung ist einer der häufigsten Konstruktionsfehler. Das Wasser kriecht durch den Kern, der Schaum/Balsa verfault, die Rumpfstruktur wird geschwächt — bis hin zum Rumpfversagen. NICHT NUR ein Dichtungsproblem, sondern ein STRUKTURELLES Problem.

(Confidence: documented — West System Epoxy Manual, Gougeon Brothers, ISO 12215)

### 7.4 Notfallsystem — Holzpfropfen

#### 7.4.1 Anforderung

**ABYC H-27 und gute Seemannschaft verlangen**: An jedem Borddurchlass muss ein passender Holzpfropfen (Notpflock) griffbereit befestigt sein.

#### 7.4.2 Spezifikation

| DN | Pfropfen-Durchmesser (Spitze) | Pfropfen-Durchmesser (Basis) | Länge | Holzart |
|---|---|---|---|---|
| DN13 (½") | 12 mm | 18 mm | 60 mm | Weichholz (Kiefer, Okumé) |
| DN19 (¾") | 18 mm | 26 mm | 75 mm | Weichholz |
| DN25 (1") | 24 mm | 34 mm | 90 mm | Weichholz |
| DN32 (1¼") | 30 mm | 42 mm | 100 mm | Weichholz |
| DN38 (1½") | 36 mm | 50 mm | 120 mm | Weichholz |
| DN50 (2") | 48 mm | 65 mm | 150 mm | Weichholz |

**Wichtig**: Weichholz verwenden, KEIN Hartholz! Der Pfropfen muss sich unter Wasserdruck ins Loch pressen und dort verkeilen. Hartholz quillt nicht schnell genug.

**Befestigung**: Mit Kabelbinder oder Leine direkt am jeweiligen Seeventil oder Borddurchlass. NICHT in einem zentralen Beutel — im Notfall ist keine Zeit zum Suchen.

**AYDI-Bewertung**: Fehlender Holzpfropfen = -5 Punkte pro Borddurchlass. Kein einziger Pfropfen an Bord = zusätzliche Warnung.

(Confidence: documented — ABYC H-27, Seemannschafts-Literatur)

### 7.5 Hose-Barb / Schlauchtülle

Der Übergang vom Seeventil zum Schlauchsystem ist eine kritische Verbindungsstelle.

| Typ | Beschreibung | Sicherheit |
|---|---|---|
| Integrierte Schlauchtülle | Am Ventilkörper angegossen | ✅ Beste Lösung |
| Aufgeschraubte Schlauchtülle | Gewindeadapter | ⚠️ Zusätzliche Dichtstelle |
| Schlauch direkt auf Ventilausgang | Ohne Tülle | ❌ NICHT zulässig unter WL |

**Doppelte Schlauchschellen** — ABYC H-27.5.4:
- Unterhalb der Wasserlinie: IMMER zwei Schlauchschellen
- Schellen aus 316L-Edelstahl
- Schellen mit Schneckengewinde, NICHT Federklemmen
- Schellenbreite ≥12 mm
- Abstand zwischen Schellen: ≥ Schellenbreite
- Drehmoment: 2,5–3,5 Nm (handfest + ¼ Umdrehung)

(Confidence: documented — ABYC H-27, ISO 9093)

---

## 8. Hersteller — Vollständige Übersicht

### 8.1 Groco (USA) — Der Goldstandard

**Gross Mechanical Laboratories, Inc.**
- Gegründet: 1927, Hanover, Maryland, USA
- Spezialisierung: Marine Bronze-Armaturen, Pumpen, Strainer
- Material: Ausschließlich C83600 (85-5-5-5) und C92200 (Navy G)
- Zertifizierungen: ABYC H-27, ISO 9093, Lloyd's, ABS
- Marktposition: Premium-Segment, OEM für Hinckley, Sabre, MJM, Back Cove

**Produktlinien:**

| Serie | Typ | Material | DN-Bereich | Beschreibung | Preis EUR |
|---|---|---|---|---|---|
| BV | Kugelventil | C83600 | ¾"–3" | Standard Ball Valve Seacock | 85–450 |
| IBV | Integriertes Kugelventil | C83600 | ¾"–2" | Ball Valve + Thru-Hull integriert | 120–380 |
| SC | Kegelventil (legacy) | C83600 | ¾"–2" | Tapered Plug, traditionell | 150–500 |
| TH | Borddurchlass (Pilz) | C83600 | ½"–3" | Mushroom Thru-Hull | 25–180 |
| HTH | Borddurchlass (extra lang) | C83600 | ¾"–2" | Für dicke Rümpfe | 35–220 |
| FF | Flansch-Borddurchlass | C83600 | 1"–3" | Flanged Fitting | 80–350 |
| BVF | Kugelventil mit Flansch | C83600 | ¾"–2" | Flanged Ball Valve | 150–500 |
| ARG | Wasserfilter | C83600 | ¾"–3" | Raw Water Strainer | 120–650 |

**Besondere Merkmale:**
- Alle Ventile einzeln druckgeprüft (100% Qualitätskontrolle)
- Guss in eigener Gießerei (USA-Fertigung)
- 5-Jahres-Garantie auf Material und Verarbeitung
- Ersatzteile über Jahrzehnte verfügbar
- Kugelventile mit Full-Port-Design (voller Durchfluss)

**Groco BV-1500 (Flaggschiff) — Technische Daten:**

| Parameter | Wert |
|---|---|
| Typ | Kugelventil |
| Nennweite | 1½" (DN38) |
| Material Körper | C83600 Bronze |
| Material Kugel | Verchromtes Messing |
| Material Sitze | PTFE |
| Material Griff | 316L Edelstahl + Kunststoffüberzug |
| Betriebsdruck | 10 bar (150 PSI) |
| Prüfdruck | 20 bar (300 PSI) |
| Temperaturbereich | -20°C bis +120°C |
| Gewinde | NPT oder BSP |
| Gewicht | 1.850 g |
| Baulänge | 127 mm |
| Preis | ca. 220 EUR |

(Confidence: documented — Groco Katalog 2025, groco.net)

### 8.2 TruDesign (Neuseeland) — Komposit-Pioneer

**TruDesign Limited**
- Gegründet: 1995, Tauranga, Neuseeland
- Spezialisierung: Glasfaserverstärkte Polyester-Armaturen
- Material: Eigene GFK-Rezeptur, FDA/NSF-61 zugelassen
- Zertifizierungen: ISO 9093-2, CE, ABYC H-27, Lloyd's Register
- Marktposition: Marktführer Komposit-Seeventile weltweit, OEM für Beneteau, Jeanneau, Hanse

**Produktlinien:**

| Serie | Typ | DN-Bereich | Beschreibung | Preis EUR |
|---|---|---|---|---|
| 90-Serie | Kugelventil-Seeventil | ¾"–2" | Standard Ball Valve | 45–165 |
| 90400 | Borddurchlass (Pilz) | ¾"–2" | Mushroom Thru-Hull | 18–75 |
| 90401 | Borddurchlass (Scoop) | ¾"–1½" | Scoop Intake | 22–85 |
| 90900 | Hose Adaptor | ¾"–2" | Schlauchtülle | 8–25 |
| 90220 | Komplettsystem | ¾"–1½" | Thru-Hull + Valve + Adapter | 65–220 |
| 90250 | Flach-Borddurchlass | ¾"–1½" | Flush-Mount | 25–90 |

**TruDesign 90-Serie Kugelventil — Technische Daten:**

| Parameter | Wert |
|---|---|
| Typ | Kugelventil |
| Material Körper | Glasfaserverstärkter Polyester |
| Material Kugel | Glasfaserverstärkter Polyester |
| Material Sitze | EPDM-Dichtungen |
| Material Griff | Glasfaserverstärkter Polyester |
| Betriebsdruck | 7 bar |
| Berstdruck | 30+ bar |
| Temperaturbereich | -30°C bis +93°C |
| UV-Beständigkeit | Ja (mit UV-Stabilisator) |
| Gewicht (DN38) | 420 g (vs. 1.850 g Bronze) |
| Preis (DN38) | ca. 95 EUR |

**Besondere Merkmale:**
- Komplettes System (Borddurchlass + Ventil + Adapter) aus einem Guss-Konzept
- Keine galvanische Korrosion möglich
- FDA/NSF-61 für Trinkwassersysteme
- Temperaturbeständiger als Forespar Marelon (+93°C vs. +82°C)
- Recyclebar
- Spezieller Montageflansch für GFK-Rümpfe

(Confidence: documented — TruDesign Katalog 2025, trudesign.nz)

### 8.3 Blakes (UK) — Britische Tradition

**Blakes Lavac Taylors Ltd**
- Gegründet: 1896, Gosport, Hampshire, UK
- Spezialisierung: Bronze-Seeventile, Marine-Toiletten (Lavac)
- Material: C83600 Bronze (eigene Gießerei)
- Zertifizierungen: BSI BS EN ISO 9093, Lloyd's Register, MCA
- Marktposition: Premium UK/EU, OEM für Oyster, Rustler, Contest

**Produktlinien:**

| Serie | Typ | Material | DN-Bereich | Preis EUR |
|---|---|---|---|---|
| Lever Seacock | Kegelventil | C83600 | ¾"–2" | 110–420 |
| BB Ball Valve | Kugelventil | C83600 | ½"–2" | 75–320 |
| Skin Fitting | Borddurchlass | C83600 | ½"–2" | 25–140 |
| Scoop Strainer | Einlassfilter | C83600 | ¾"–1½" | 45–180 |

**Besondere Merkmale:**
- Kegelventile mit nachschleifbarem Küken (Lebensdauer 50+ Jahre)
- Britische Fertigung (Made in UK)
- BSP-Gewinde Standard (nicht NPT)
- Hervorragender Kundenservice
- Ersatzküken einzeln erhältlich

(Confidence: documented — Blakes Katalog 2025, blakes-lavac-taylors.co.uk)

### 8.4 Forespar (USA) — Marelon-Marke

**Forespar Products Corporation**
- Gegründet: 1967, San Clemente, California, USA
- Spezialisierung: Marelon (glasfaserverstärktes Nylon) — der Original-Komposit
- Material: Marelon = glasfaserverstärktes Polyamid (Nylon 6/6 + 40% Glasfaser)
- Zertifizierungen: ABYC H-27, ISO 9093-2, UL, FDA, NSF
- Marktposition: US-Marktführer Komposit, OEM für Catalina, Hunter, Bayliner

**Produktlinien:**

| Serie | Typ | DN-Bereich | Preis EUR |
|---|---|---|---|
| 903/904/905 | Borddurchlass (Pilz) | ½"–2" | 12–55 |
| 906/907 | Borddurchlass (Scoop) | ¾"–1½" | 18–65 |
| MF-Serie | Kugelventil | ¾"–2" | 35–135 |
| 909 | Schlauchtülle | ½"–2" | 8–22 |

**Marelon vs. TruDesign:**

| Eigenschaft | Forespar Marelon | TruDesign GFK |
|---|---|---|
| Basis-Polymer | Polyamid (Nylon 6/6) | Polyester |
| Glasfaseranteil | 40% | 45–55% |
| Max. Temperatur | 82°C | 93°C |
| Wasseraufnahme | 2–3% (Nylon nimmt Wasser auf) | <0.5% |
| UV-Beständigkeit | Gut (mit Stabilisator) | Sehr gut |
| Festigkeit (Zugfestigkeit) | 130 MPa | 155 MPa |
| FDA/NSF | Ja | Ja |
| Preis | Günstiger | Etwas teurer |
| Verfügbarkeit EU | Über Importeure | Direkt + Händler |

(Confidence: documented — Forespar Technical Manual, forespar.com)

### 8.5 Guidi (Italien) — Europäischer OEM-Standard

**Guidi Srl**
- Gegründet: 1968, Grignasco, Piemont, Italien
- Spezialisierung: Bronze-Armaturen für Serienbootsbau
- Material: C83600, teilweise DZR-Messing
- Zertifizierungen: ISO 9093, CE, RINA, Lloyd's
- Marktposition: Größter europäischer OEM, liefert an Beneteau, Jeanneau, Bavaria, Dufour, Azimut

**Produktlinien:**

| Serie | Typ | Material | DN-Bereich | Preis EUR |
|---|---|---|---|---|
| 2060 | Kugelventil | C83600 | ½"–2" | 35–180 |
| 1040 | Borddurchlass (Pilz) | C83600 | ½"–2" | 12–85 |
| 1060 | Borddurchlass (Scoop) | C83600 | ¾"–1½" | 18–95 |
| 1164 | Flansch-Borddurchlass | C83600 | 1"–2" | 45–200 |
| 1302 | Wasserfilter | C83600 | ¾"–1½" | 55–220 |
| 2062 | Kugelventil DZR | DZR-Messing | ½"–1½" | 22–95 |

**Besondere Merkmale:**
- Hochvolumen-Produktion: niedrigste Stückkosten in Europa
- RINA-Typzulassung (wichtig für italienische Werften)
- Sowohl Bronze als auch DZR-Messing im Programm
- **ACHTUNG**: Guidi 2062 (DZR-Messing) ≠ Guidi 2060 (Bronze) — genau prüfen!
- Gute Qualität für Serienproduktion

**AYDI-Hinweis**: Bei Guidi immer Modellnummer prüfen. Die 2060-Serie (Bronze) ist empfehlenswert, die 2062-Serie (DZR) ist akzeptabel, aber bei Booten >15 Jahre ggf. kritisch prüfen.

(Confidence: documented — Guidi Katalog 2025, guidi.it)

### 8.6 Buck Algonquin (USA)

**Buck Algonquin Marine Hardware**
- Gegründet: 1917, Philadelphia, USA
- Spezialisierung: Schwere Bronze-Armaturen, kommerzielle Schifffahrt
- Material: C83600, C92200 (Navy G)
- Zertifizierungen: ABYC, ABS, USCG
- Marktposition: Heavy-Duty, kommerzielle Yachten, Arbeitsboote

**Produktlinien:**

| Serie | Typ | Material | DN-Bereich | Preis EUR |
|---|---|---|---|---|
| HT-Serie | Borddurchlass (Pilz) | C83600 | ¾"–3" | 30–250 |
| FHT-Serie | Flansch-Borddurchlass | C83600 | 1"–3" | 75–400 |
| SC-Serie | Kegelventil | C83600 | ¾"–2" | 120–500 |
| BV-Serie | Kugelventil | C83600 | ¾"–2" | 75–350 |

**Besondere Merkmale:**
- Extra schwere Wandstärken (über ISO-Minimum)
- Geeignet für kommerzielle Zulassung
- Lange Schäfte für dicke Rümpfe verfügbar
- US-Fertigung

(Confidence: documented — Buck Algonquin Katalog 2024)

### 8.7 Perko (USA)

**Perko, Inc.**
- Gegründet: 1907, Miami, Florida, USA
- Spezialisierung: Breites Sortiment Marine-Hardware
- Material: C83600, verchromtes Messing (ACHTUNG!)
- Zertifizierungen: ABYC
- Marktposition: Mid-Range US, OEM für verschiedene Bootsbauer

**Produktlinien:**

| Serie | Typ | Material | DN-Bereich | Preis EUR |
|---|---|---|---|---|
| 0844 | Kegelventil | C83600 | ¾"–1½" | 95–350 |
| 0805 | Kegelventil (Flansch) | C83600 | ¾"–1½" | 120–400 |
| 0338 | Borddurchlass (Pilz) | C83600 | ½"–2" | 20–120 |
| 0393 | Borddurchlass (Scoop) | C83600 | ¾"–1½" | 25–130 |

**ACHTUNG**: Perko führt auch verchromte Messing-Armaturen (für ÜBER der Wasserlinie). Diese sind NICHT als Seeventile unter der Wasserlinie geeignet! Immer auf "Bronze" oder "Genuine Bronze" in der Beschreibung achten.

(Confidence: documented — Perko Katalog 2025, perko.com)

### 8.8 Apollo Valves (USA)

**Apollo Valves / Conbraco Industries**
- Gegründet: 1928, Matthews, North Carolina, USA
- Spezialisierung: Industrieventile, auch marine-tauglich
- Material: C83600 (70-100 Serie), C84400 (70-140 Serie)
- Zertifizierungen: UL, FM, NSF, MSS (nicht spezifisch marine ABYC)
- Marktposition: Industrieventile, die im Marine-Bereich eingesetzt werden

**Produktlinien (marine-relevant):**

| Serie | Typ | Material | DN-Bereich | Preis EUR |
|---|---|---|---|---|
| 70-100 | Kugelventil, 2-teilig | C83600 | ¼"–4" | 15–180 |
| 70-140 | Kugelventil, 2-teilig | C84400 | ¼"–2" | 12–120 |
| 70-200 | Kugelventil, 3-teilig | C83600 | ½"–2" | 35–250 |

**AYDI-Hinweis**: Apollo-Ventile sind qualitativ hochwertig, aber NICHT als Seeventile zertifiziert (keine ISO 9093, kein ABYC H-27). Sie können als Absperrventile IM Boot verwendet werden (z.B. nach dem Seeventil), aber NICHT als primäres Seeventil am Borddurchlass.

**Ausnahme**: Einige Bootsbauer (z.B. Pacific Seacraft) verwenden Apollo 70-100 als Seeventile in Kombination mit zertifizierten Borddurchlässen. Dies ist in der Praxis akzeptiert, aber formal nicht zertifiziert.

(Confidence: documented — Apollo Katalog 2025, apollovalves.com)

### 8.9 Vetus (Niederlande)

**Vetus Maxwell B.V.**
- Gegründet: 1925, Schiedam, Niederlande
- Spezialisierung: Marine-Systeme (Motoren, Auspuff, Borddurchlässe, Bugstrahlruder)
- Material: Bronze + Komposit im Programm
- Zertifizierungen: ISO 9093, CE, Lloyd's Register
- Marktposition: Europäischer Systemanbieter, OEM für viele europäische Werften

**Produktlinien:**

| Serie | Typ | Material | DN-Bereich | Preis EUR |
|---|---|---|---|---|
| FULL FLOW | Kugelventil | Bronze | ¾"–2" | 55–220 |
| HTP | Borddurchlass | Bronze | ½"–2" | 18–95 |
| YSF | Wasserfilter | Bronze | ¾"–1½" | 65–280 |
| NLP | Komposit-Borddurchlass | Polyamid | ¾"–1½" | 12–45 |
| NLK | Komposit-Kugelventil | Polyamid | ¾"–1½" | 30–95 |

**Besondere Merkmale:**
- Integriertes Systemkonzept (Borddurchlass → Seeventil → Filter → Motor)
- Gute technische Dokumentation auf Deutsch
- Europaweites Händlernetz
- BOW PRO: Elektrisch betätigbare Seeventile (Fernbedienung)

(Confidence: documented — Vetus Katalog 2025/26, vetus.com)

### 8.10 Plastimo (Frankreich)

**Plastimo S.A.S.**
- Gegründet: 1963, Lorient, Bretagne, Frankreich
- Spezialisierung: Breites Marine-Sortiment, Schwerpunkt Sicherheitsausrüstung
- Material: Bronze (zugekauft, meist Guidi-OEM) + Kunststoff
- Zertifizierungen: ISO 9093, CE
- Marktposition: Französischer Markt, Charterflotten

**Produktlinien:**

| Serie | Typ | Material | DN-Bereich | Preis EUR |
|---|---|---|---|---|
| Bronze-Serie | Kugelventil | C83600 (Guidi-OEM) | ¾"–1½" | 40–150 |
| Bronze-Serie | Borddurchlass | C83600 (Guidi-OEM) | ½"–1½" | 15–75 |
| Kunststoff-Serie | Borddurchlass | PA/POM | ½"–1" | 8–25 |

**AYDI-Hinweis**: Plastimo-Bronze-Armaturen sind größtenteils Guidi-OEM mit Plastimo-Labeling. Qualitativ gleichwertig mit Guidi-Originalen.

(Confidence: documented + estimated — Plastimo Katalog 2025)

### 8.11 Osculati (Italien)

**Osculati S.p.A.**
- Gegründet: 1958, Segrate, Mailand, Italien
- Spezialisierung: Marine-Zubehör-Vollsortiment (>17.000 Artikel)
- Material: Bronze (Guidi-OEM), DZR-Messing, Kunststoff
- Zertifizierungen: ISO 9093, CE
- Marktposition: Europäischer Vollsortimenter, Schwerpunkt Mittelmeer

**Produktlinien:**

| Serie | Typ | Material | DN-Bereich | Preis EUR |
|---|---|---|---|---|
| 17.319 | Borddurchlass Bronze | C83600 | ½"–2" | 12–80 |
| 17.321 | Borddurchlass Messing | DZR | ½"–1½" | 8–45 |
| 17.323 | Kugelventil Bronze | C83600 | ½"–1½" | 30–140 |
| 17.327 | Kugelventil DZR | DZR-Messing | ½"–1½" | 18–75 |
| 17.330 | Borddurchlass Nylon | PA | ½"–1" | 5–18 |

**ACHTUNG**: Osculati führt sowohl Bronze (17.319/17.323) als auch DZR-Messing (17.321/17.327) und sogar Nylon (17.330). Die Nylon-Varianten sind NUR über der Wasserlinie zu verwenden! Bei Online-Bestellungen genau auf die Artikelnummer achten.

(Confidence: documented — Osculati General Catalogue 2025, osculati.com)

### 8.12 Weitere Hersteller (Kurzübersicht)

| Hersteller | Land | Spezialität | Bemerkung |
|---|---|---|---|
| Nibco | USA | Bronze-Kugelventile (Industrie) | Wie Apollo — nicht marine-zertifiziert |
| Italvalvole | IT | Marine Bronze-Ventile | Spezialist für Superyachten |
| Hempel | IT | Bronze-Guss | OEM für Azimut, Ferretti |
| Lewmar | UK | Borddurchlässe (Flush-Mount) | Premium-Segment |
| Whale | UK | Komposit-Borddurchlässe | Schwerpunkt Drainagen |
| Attwood | USA | Kunststoff-Borddurchlässe | Budget — NUR über Wasserlinie |
| Raritan | USA | WC-Borddurchlässe | Spezialist für Marine-WC-Systeme |
| Jabsco | USA | Pumpen + Borddurchlässe | Systemanbieter |

(Confidence: documented — Diverse Herstellerquellen)

---

## 9. Anlagen-spezifische Zuordnung

### 9.1 Kühlwassereinlass Motor (Cooling Water Intake)

| Parameter | Empfehlung |
|---|---|
| Ventiltyp | Kugelventil (Ball Valve) |
| Material | Bronze C83600 (bevorzugt) oder Komposit |
| Nennweite | DN25 (bis 30 PS), DN32 (30–80 PS), DN38 (80–200 PS), DN50 (>200 PS) |
| Position | Möglichst tief, möglichst mittschiffs |
| Scoop-Einlass | Empfohlen für Segelboote (Krängung) |
| Vorfilter | PFLICHT — Groco ARG oder Vetus YSF |
| Doppelanlage | Empfohlen ab Kategorie A (Ozean) |
| Risiko | Bewuchs blockiert Einlass → Motor überhitzt |
| AYDI-Score-Gewicht | Hoch — Motorausfall = Sicherheitsrelevant |

**Typische Konfiguration Segelboot 10–14 m:**
```
Borddurchlass (Mushroom/Scoop, DN32, Bronze)
  → Seeventil (Ball Valve, DN32, Bronze)
    → Doppelschlauchschellen (316L, 32 mm)
      → Schlauch (Marine-Spiralschlauch, 32 mm ID)
        → Vorfilter (Groco ARG-1000)
          → Motor-Kühlwasserpumpe
```

(Confidence: documented — Motorhersteller-Handbücher Volvo Penta, Yanmar, Beta Marine)

### 9.2 Nassauspuff (Wet Exhaust)

| Parameter | Empfehlung |
|---|---|
| Ventiltyp | Kugelventil — Seeventil optional (ABYC: empfohlen, nicht Pflicht) |
| Material | Bronze C83600 — KEIN Komposit (Temperatur!) |
| Nennweite | DN38–DN50 (je nach Motorleistung) |
| Position | Möglichst weit achtern, über der Wasserlinie bevorzugt |
| Temperatur | Abgastemperatur nach Mischung: 50–70°C |
| Risiko | Rückschlag bei Seegang → Wasser im Motor |
| AYDI-Hinweis | Antisiphon-Ventil prüfen! |

**WARNUNG**: Kein Komposit-Seeventil am Auspuff verwenden! Auch wenn die Mischtemperatur "nur" 50–70°C beträgt, können Spitzen von >100°C auftreten. Bronze hält 250°C+ aus. Marelon maximal 82°C.

(Confidence: documented — Volvo Penta Installation Manual, ISO 8178)

### 9.3 Toilette — Seewassereinlass (Toilet Intake)

| Parameter | Empfehlung |
|---|---|
| Ventiltyp | Kugelventil |
| Material | Bronze oder Komposit (beides geeignet) |
| Nennweite | DN19–DN25 |
| Position | Unter Wasserlinie, möglichst nah an der Toilette |
| Risiko | Kalkablagerung in warmem Seewasser, Undichtigkeit WC-Pumpe |
| AYDI-Hinweis | Komposit hier besonders empfehlenswert (FDA/NSF) |

### 9.4 Toilette — Abwasserauslass (Toilet Discharge)

| Parameter | Empfehlung |
|---|---|
| Ventiltyp | Kugelventil |
| Material | Bronze oder Komposit |
| Nennweite | DN25–DN38 |
| Position | Unter Wasserlinie, NICHT im Kielbereich (Geruch!) |
| Y-Ventil | Für Umschaltung Direkt/Tank oft Y-Ventil am Seeventil |
| Risiko | Verstopfung, Geruch bei Undichtigkeit |
| Regulierung | MARPOL-Zonen: kein Direktauslass in Küstennähe |

### 9.5 Bilgenpumpe — Auslass (Bilge Discharge)

| Parameter | Empfehlung |
|---|---|
| Ventiltyp | Kugelventil mit Rückschlagklappe |
| Material | Bronze oder Komposit |
| Nennweite | DN25–DN38 (je nach Pumpenleistung) |
| Position | ÜBER der Wasserlinie wenn möglich |
| Rückschlagventil | PFLICHT bei Auslass unter Wasserlinie |
| Risiko | Ohne Rückschlagventil: Wasser strömt rein statt raus |

### 9.6 Klimaanlage — Seewassereinlass (AC Intake)

| Parameter | Empfehlung |
|---|---|
| Ventiltyp | Kugelventil |
| Material | Bronze C83600 (wegen Dauerbetrieb) |
| Nennweite | DN25–DN32 (je nach BTU) |
| Position | Tief unter Wasserlinie (Dauerbetrieb → Bewuchsrisiko) |
| Vorfilter | PFLICHT — fein (Groco ARG mit feinem Sieb) |
| Risiko | Bewuchs bei Dauerbetrieb, Elektrolyse durch AC-Strom |
| AYDI-Hinweis | Galvanischer Isolator für Landstrom PFLICHT |

### 9.7 Generator — Kühlwasser (Generator Cooling)

| Parameter | Empfehlung |
|---|---|
| Ventiltyp | Kugelventil |
| Material | Bronze C83600 |
| Nennweite | DN19–DN25 |
| Vorfilter | Eigener Vorfilter (nicht mit Motor teilen) |
| Risiko | Generator saugt Bewuchs an, überhitzt, Abgas-Rückschlag |

### 9.8 Wassermacher — Einlass (Watermaker Intake)

| Parameter | Empfehlung |
|---|---|
| Ventiltyp | Kugelventil |
| Material | Bronze oder Komposit (Komposit bevorzugt — kein Metallgeschmack) |
| Nennweite | DN19–DN25 |
| Position | Tief, möglichst sauberes Wasser (nicht nahe Abwasser/Auspuff) |
| Vorfilter | Grob + Fein (5 µm) vor der Membrane |
| Risiko | Verunreinigung des Trinkwassers bei Leckage |

(Confidence: documented — Diverse Systemhersteller, ABYC Standards)

---

## 10. Verbindungstechnik

### 10.1 Schlauchverbindungen

#### 10.1.1 Schlauchtüllen (Hose Barbs)

| Durchmesser Seeventil | Schlauch-ID | Schlauchtülle OD | Hersteller | Modell |
|---|---|---|---|---|
| DN13 (½") | 13 mm | 14–15 mm | Groco | HB-500 |
| DN19 (¾") | 19 mm | 20–21 mm | Groco | HB-750 |
| DN25 (1") | 25 mm | 26–27 mm | Groco | HB-1000 |
| DN32 (1¼") | 32 mm | 33–34 mm | Groco | HB-1250 |
| DN38 (1½") | 38 mm | 39–40 mm | Groco | HB-1500 |
| DN50 (2") | 50 mm | 51–52 mm | Groco | HB-2000 |

#### 10.1.2 Schlauchschellen — Spezifikation

**ABYC H-27 Anforderung**: Doppelte Schlauchschellen an ALLEN Verbindungen unterhalb der Wasserlinie.

| Eigenschaft | Anforderung |
|---|---|
| Material | 316L Edelstahl (NICHT 304!) |
| Bandbreite | ≥12,7 mm (½") |
| Typ | Schneckengewinde (Worm-Drive), NICHT Federklemme |
| Drehmoment | 2,5–3,5 Nm |
| Anordnung | 2 Schellen, Abstand ≥ Bandbreite |
| Ausrichtung | Schraubköpfe nicht übereinander, um 90° versetzt |
| Marken | ABA (Schweden), NORMA (DE), Jubilee (UK), Ideal (USA) |
| Preis | 2–8 EUR pro Schelle (je nach Größe und Material) |

**Gute Schlauchschellen:**

| Hersteller | Typ | Material | Bandbreite | Preis EUR |
|---|---|---|---|---|
| ABA | Original | 316L | 12 mm | 3–6 |
| NORMA | Torro | W4 (316L) | 12 mm | 3–5 |
| Jubilee | Superclamp | 316L | 13 mm | 4–7 |
| Ideal | Tridon 67-5 | 316L | 14 mm | 3–6 |

**Schlechte Schlauchschellen (NIEMALS verwenden):**
- Verzinkter Stahl → rostet in Tagen
- 304 Edelstahl → Spaltkorrosion in Seewasser
- Federklemmen → Lösen sich bei Vibration
- Billige No-Name → Bandbruch beim Anziehen

(Confidence: documented — ABYC H-27, ABA/NORMA technische Daten)

### 10.2 Backing-Blocks / Backing-Plates

#### 10.2.1 Warum ein Backing-Block unverzichtbar ist

Ein GFK-Rumpf hat typischerweise 4–12 mm Laminatstärke. Ein Seeventil mit DN38 erzeugt bei 1 m Wassertiefe eine Kraft von ca. 110 N auf die Flanschfläche. Diese Kraft verteilt sich bei DIREKTER Montage auf eine sehr kleine Fläche → Laminatschaden, Rissbildung, Undichtigkeit → SINKEN.

Der Backing-Block verteilt die Last auf eine größere Fläche des Laminats.

#### 10.2.2 Materialien für Backing-Blocks

| Material | Anwendung | Vorteile | Nachteile | Preis EUR |
|---|---|---|---|---|
| GFK-Laminat (handlaminiert) | Standard | Exakte Anpassung an Rumpfkontur | Arbeitsaufwändig | 5–15 (Material) |
| G10/FR4 Epoxid-Glasfaser-Platte | Premium | Exzellente Festigkeit, kein Wasser | Schwer zu formen, teuer | 10–30 |
| Marine-Sperrholz (BS 1088) | Traditionell | Leicht zu bearbeiten | Wasseraufnahme, Fäulnis | 5–10 |
| Massivholz (Eiche, Teak) | Traditionell | Verfügbar, bearbeitbar | Wasseraufnahme | 3–8 |
| Bronze-Platte | Superyacht | Keine Korrosion mit Bronze-Ventil | Schwer, teuer | 25–80 |
| Aluminium (5083) | Alu-Rümpfe | Galvanisch kompatibel | NUR bei Alu-Rümpfen | 10–25 |

**AYDI-Empfehlung**: G10/FR4 für Neubauten, handlaminiertes GFK für Nachrüstung.

#### 10.2.3 Dimensionierung

| Seeventil-DN | Mindest-Backing-Block (B×H) | Mindest-Dicke | Bohrungsdurchmesser |
|---|---|---|---|
| DN19 (¾") | 80×80 mm | 10 mm | 26 mm |
| DN25 (1") | 100×100 mm | 12 mm | 33 mm |
| DN32 (1¼") | 120×120 mm | 15 mm | 42 mm |
| DN38 (1½") | 140×140 mm | 18 mm | 50 mm |
| DN50 (2") | 170×170 mm | 20 mm | 63 mm |

(Confidence: documented — ABYC H-27, Nigel Calder, Good Old Boat Magazine)

### 10.3 Dichtmassen für Borddurchlass-Montage

#### 10.3.1 Geeignete Dichtmassen

| Produkt | Typ | Unterwasser? | Haftung auf GFK | Haftung auf Bronze | Preis EUR |
|---|---|---|---|---|---|
| Sikaflex 291 | PU-Kleb-/Dichtstoff | ✅ JA | Sehr gut | Gut (mit Primer) | 12–18 |
| Sikaflex 291i | PU, ISO-konform | ✅ JA | Sehr gut | Gut (mit Primer) | 14–20 |
| 3M 4200 | PU, mittelfest | ✅ JA | Sehr gut | Gut | 15–22 |
| 3M 5200 | PU, permanent | ✅ JA | Exzellent | Exzellent | 18–25 |
| Soudaflex 40 FC | PU, flexibel | ✅ JA | Gut | Mittel | 8–14 |
| Life-Calk | Polysulfid | ✅ JA | Sehr gut | Sehr gut | 12–18 |
| Boatlife Life-Seal | PU | ✅ JA | Sehr gut | Gut | 14–20 |

**NICHT geeignet:**
- Silikon (haftet nicht auf Bronze, nicht überlackierbar)
- Acryl (nicht wasserfest)
- Butylband (nicht strukturell belastbar)

**3M 5200 vs. 4200 Diskussion:**
- **5200**: Permanente Verklebung — Seeventil nie wieder ohne Zerstörung entfernbar
- **4200**: Demontierbar mit Werkzeug — empfohlen für Seeventile (Austausch möglich!)
- **AYDI-Empfehlung**: 3M 4200 oder Sikaflex 291 — demontierbar aber dicht

#### 10.3.2 Anwendungstechnik

1. GFK-Oberfläche anschleifen (80er Schleifpapier)
2. Entfetten mit Aceton (NICHT Isopropanol bei GFK)
3. Bronze-Flansch reinigen, entfetten
4. Bei Sikaflex: Sika Primer 209D auf GFK, 30 min trocknen
5. Dichtmasse in geschlossener Raupe auftragen
6. Borddurchlass einsetzen, Seeventil aufschrauben
7. Überstehende Dichtmasse NICHT abwischen (erst nach Aushärtung abschneiden)
8. Aushärtezeit: 24–48 h (abhängig von Temperatur/Feuchtigkeit)
9. NICHT belasten während Aushärtung

(Confidence: documented — Sika Technical Data Sheet, 3M Marine Application Guide)

---

### 10.4 Gewindespezifikationen

#### 10.4.1 BSP (British Standard Pipe) — Europa-Standard

| Nenngröße | Gewinde-OD (mm) | Gewindesteigung (mm) | Gänge/Zoll | Typ |
|---|---|---|---|---|
| ½" BSP | 20,955 | 1,814 | 14 | Zylindrisch (BSPP) |
| ¾" BSP | 26,441 | 1,814 | 14 | Zylindrisch |
| 1" BSP | 33,249 | 2,309 | 11 | Zylindrisch |
| 1¼" BSP | 41,910 | 2,309 | 11 | Zylindrisch |
| 1½" BSP | 47,803 | 2,309 | 11 | Zylindrisch |
| 2" BSP | 59,614 | 2,309 | 11 | Zylindrisch |

**Dichtung bei BSP**: Über O-Ring oder Flachdichtung am Flansch. KEIN PTFE-Band erforderlich (zylindrisches Gewinde dichtet nicht über Gewindegänge).

#### 10.4.2 NPT (National Pipe Thread) — USA-Standard

| Nenngröße | Gewinde-OD (mm) | Konizität | Gänge/Zoll | Typ |
|---|---|---|---|---|
| ½" NPT | 21,223 | 1:16 (3,6°) | 14 | Konisch |
| ¾" NPT | 26,568 | 1:16 | 14 | Konisch |
| 1" NPT | 33,401 | 1:16 | 11½ | Konisch |
| 1¼" NPT | 42,164 | 1:16 | 11½ | Konisch |
| 1½" NPT | 48,054 | 1:16 | 11½ | Konisch |
| 2" NPT | 60,325 | 1:16 | 11½ | Konisch |

**Dichtung bei NPT**: Über Gewindeverformung (konisch). PTFE-Band auf dem Außengewinde PFLICHT. 3–5 Windungen, in Einschraubrichtung wickeln.

**WARNUNG**: BSP und NPT sind NICHT kompatibel! Obwohl die Durchmesser ähnlich sind, unterscheiden sich Konizität und Gewindesteigung. Erzwungenes Verschrauben beschädigt das Gewinde und führt zu Undichtigkeit.

#### 10.4.3 BSP↔NPT Adapter

| Adapter | Hersteller | Material | Preis EUR |
|---|---|---|---|
| BSP→NPT Male | Groco | C83600 | 15–35 |
| NPT→BSP Female | Guidi | C83600 | 12–30 |
| Universal Adapter Set | TruDesign | GFK | 8–20 |

**AYDI-Empfehlung**: Bei Bootskauf in USA für europäischen Einsatz: Alle Seeventile auf BSP umrüsten ODER passende Adapter mitführen.

(Confidence: documented — ISO 228-1 (BSP), ASME B1.20.1 (NPT))

### 10.5 Materialkompatibilität Matrix

| | Bronze C83600 | Bronze C92200 | DZR Messing | Komposit | 316L Edelstahl | Alu 5083 | Stahl |
|---|---|---|---|---|---|---|---|
| **Bronze C83600** | ✅ | ✅ | ✅ | ✅ | ⚠️ | ❌ | ⚠️ |
| **Bronze C92200** | ✅ | ✅ | ✅ | ✅ | ⚠️ | ❌ | ⚠️ |
| **DZR Messing** | ✅ | ✅ | ✅ | ✅ | ⚠️ | ❌ | ⚠️ |
| **Komposit** | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| **316L Edelstahl** | ⚠️ | ⚠️ | ⚠️ | ✅ | ✅ | ❌ | ⚠️ |
| **Alu 5083** | ❌ | ❌ | ❌ | ✅ | ❌ | ✅ | ❌ |
| **Stahl** | ⚠️ | ⚠️ | ⚠️ | ✅ | ⚠️ | ❌ | ✅ |

Legende: ✅ Kompatibel | ⚠️ Nur mit Opferanoden/Isolation | ❌ INKOMPATIBEL — galvanische Zerstörung

**AYDI-Regel**: Bei jeder Seeventil-Bewertung wird die Materialpaarung aller Komponenten im System geprüft (Borddurchlass, Ventil, Schlauchtülle, Schlauchschelle, Rumpfmaterial). Inkompatible Paarungen = Score-Abzug 20 Punkte + Warnung.

(Confidence: documented — NACE International, MIL-STD-889C, Galvanic Series)

### 10.6 Schlauchtypen für Seeventil-Anschlüsse

| Schlauchtyp | Einsatz | Material | Max. Druck | Temp. | Preis/m EUR |
|---|---|---|---|---|---|
| Marine Spiralschlauch | Kühlwasser, Bilge | PVC + Stahlspirale | 3 bar | -10 bis +65°C | 8–25 |
| Auspuffschlauch (Wet Exhaust) | Nassauspuff | EPDM + Textileinlage | 2 bar | bis +100°C | 15–45 |
| Sanitärschlauch (geruchsdicht) | WC, Abwasser | PVC + Geruchsbarriere | 2 bar | -10 bis +60°C | 10–30 |
| Trinkwasserschlauch | Wassermacher, Trinkwasser | PE + FDA-zugelassen | 4 bar | -10 bis +60°C | 12–35 |
| Kraftstoffschlauch | Kraftstoff (nur über WL) | NBR/CR + Textileinlage | 6 bar | -30 bis +100°C | 15–40 |
| Silikonschlauch | Kühlwasser Motor | Silikon + Textileinlage | 3 bar | -50 bis +200°C | 20–55 |

**AYDI-Prüfung**: Schlauchtyp muss zum Anwendungszweck passen. Sanitärschlauch am Kühlwasser = falsch (nicht temperaturbeständig). Kühlwasserschlauch am WC = falsch (nicht geruchsdicht). Falscher Schlauchtyp = Score-Abzug 10 Punkte.

(Confidence: documented — Vetus Schlauchkatalog, Shields Hose Catalog)

---

## 11. Technische Referenz & Berechnungen

### 11.1 Durchflussraten

#### 11.1.1 Durchfluss durch einen Borddurchlass

```
Q = Cd × A × √(2 × g × h)

wobei:
Q  = Durchfluss in m³/s
Cd = Durchflusskoeffizient (0,6–0,8 je nach Form)
A  = Querschnittsfläche in m²
g  = 9,81 m/s²
h  = Wassersäule (Tiefe unter Wasserlinie) in m
```

#### 11.1.2 Wassereinbruchrate bei versagendem Seeventil

**KRITISCH** — So schnell kommt das Wasser:

| DN | Fläche mm² | Tiefe 0,5 m | Tiefe 1,0 m | Tiefe 1,5 m | Tiefe 2,0 m |
|---|---|---|---|---|---|
| DN13 (½") | 133 | 250 l/min | 355 l/min | 435 l/min | 500 l/min |
| DN19 (¾") | 284 | 535 l/min | 755 l/min | 925 l/min | 1.070 l/min |
| DN25 (1") | 491 | 925 l/min | 1.310 l/min | 1.600 l/min | 1.850 l/min |
| DN32 (1¼") | 804 | 1.515 l/min | 2.145 l/min | 2.625 l/min | 3.030 l/min |
| DN38 (1½") | 1.134 | 2.140 l/min | 3.025 l/min | 3.705 l/min | 4.275 l/min |
| DN50 (2") | 1.963 | 3.700 l/min | 5.235 l/min | 6.410 l/min | 7.400 l/min |

**Konsequenz**: Ein offener DN38-Borddurchlass in 1 m Tiefe flutet ein 10-m-Boot (ca. 3.000 l Bilgenvolumen) in unter 1 Minute. Es gibt keine Bilgenpumpe, die das schafft.

> ⚠️ **ZU PRÜFEN (Audit):** Die Durchflusswerte dieser Tabelle sind mit der oben angegebenen Formel Q = Cd·A·√(2gh) (Cd = 0,65) NICHT reproduzierbar — sie liegen rund 10-fach zu hoch. Nachrechnung DN38 bei 1,0 m: 0,65 × 0,001134 m² × √(2·9,81·1,0 m/s²·m) ≈ 0,0033 m³/s ≈ **196 l/min** (Tabelle nennt 3.025 l/min). Empirische Referenz: 1″-Loch bei ~0,3 m Tiefe ≈ 20 gal/min ≈ 76 l/min (BoatUS/CCA). Zusätzlich Widerspruch zu §1.1 (dort 3.400 l/min statt 3.025 l/min). Sämtliche Tabellenwerte vor Verwendung neu berechnen; qualitative Aussage („Wasser kommt schneller, als jede Bilgenpumpe fördern kann") bleibt gültig.

(Confidence: estimated — unverifiziert; ursprünglich „calculated", per Audit zurückgestuft, da Tabellenwerte der genannten Formel widersprechen)

### 11.2 Dimensionierung Seeventile

#### 11.2.1 Motorkühlwasser — Faustformel

```
Erforderlicher Kühlwasserdurchfluss (l/min) ≈ Motorleistung (kW) × 0,5

Beispiele:
- 15 kW (20 PS): 7,5 l/min → DN19 ausreichend
- 40 kW (54 PS): 20 l/min → DN25 empfohlen
- 75 kW (100 PS): 37,5 l/min → DN32 empfohlen
- 150 kW (200 PS): 75 l/min → DN38 empfohlen
- 300 kW (400 PS): 150 l/min → DN50 empfohlen
```

#### 11.2.2 WC-Spülung

```
WC-Spülvolumen pro Zyklus: 1–3 l
Spülrate: max. 10 l/min
→ DN19 ausreichend für alle manuellen Marine-WC
→ DN25 für elektrische WC mit Hochleistungspumpe
```

#### 11.2.3 Bilgenpumpe

```
Standard-Bilgenpumpe: 30–60 l/min → DN25
Hochleistungs-Bilgenpumpe: 60–150 l/min → DN32–DN38
Notfall-Bilgenpumpe: 150–300 l/min → DN38–DN50
```

(Confidence: calculated — Motorhersteller-Angaben, Pumpen-Datenblätter)

### 11.3 Galvanische Reihe — Marine-relevante Metalle

**Galvanische Reihe in Seewasser (Potenzial in V vs. Ag/AgCl):**

| Material | Potenzial (V) | Gruppe |
|---|---|---|
| Graphit | +0,20 bis +0,30 | Edelste (Kathode) |
| Platin | +0,15 bis +0,25 | |
| Titan | +0,05 bis +0,10 | |
| 316L Edelstahl (passiv) | -0,05 bis +0,10 | |
| Nickel 200 | -0,10 bis -0,20 | |
| Bronze C92200 (Navy G) | -0,24 bis -0,28 | Edle Kupferlegierungen |
| Bronze C83600 (85-5-5-5) | -0,26 bis -0,30 | |
| Kupfer | -0,30 bis -0,36 | |
| DZR-Messing CW602N | -0,28 bis -0,35 | |
| Messing (Yellow Brass) | -0,30 bis -0,40 | |
| Zinn | -0,30 bis -0,35 | |
| Blei | -0,50 bis -0,55 | |
| 316L Edelstahl (aktiv/Spalt) | -0,50 bis -0,60 | |
| Gusseisen | -0,60 bis -0,70 | |
| Stahl (unlegiert) | -0,60 bis -0,70 | Unedle Metalle |
| Aluminium 5083 | -0,75 bis -0,85 | |
| Aluminium 6061 | -0,80 bis -0,90 | |
| Zink | -0,98 bis -1,03 | Opferanoden |
| Magnesium | -1,60 bis -1,65 | Opferanoden (Süßwasser) |

**Faustregel**: Mehr als 0,25 V Potentialdifferenz = kritische galvanische Korrosion möglich.

**Kritische Materialpaarungen bei Seeventilen:**

| Paarung | Potentialdiff. | Bewertung |
|---|---|---|
| Bronze-Ventil + Bronze-Borddurchlass | <0,02 V | ✅ Ideal |
| Bronze-Ventil + Edelstahl-Welle | 0,20–0,35 V | ⚠️ Anode nötig |
| Bronze-Ventil + Alu-Rumpf | 0,50–0,60 V | ❌ GEFAHR — Alu frisst sich auf! |
| Komposit-Ventil + beliebig | 0,00 V | ✅ Keine galvanische Korrosion |
| Bronze-Ventil + Stahl-Rumpf | 0,30–0,40 V | ⚠️ Anode nötig, Isolation empfohlen |

**AYDI-Regel**: Bei Aluminium-Rümpfen IMMER Komposit-Seeventile oder galvanisch isolierte Bronze verwenden. Ohne Isolation frisst sich das Aluminium innerhalb von 2–5 Jahren durch.

(Confidence: documented — NACE International, MIL-STD-889C)

### 11.4 Korrosionsraten in Seewasser

| Material | Korrosionsrate (mm/Jahr) | Lebensdauer bis Wandstärke kritisch |
|---|---|---|
| C83600 (85-5-5-5) | 0,01–0,03 | 40–100+ Jahre |
| C92200 (Navy G) | 0,005–0,02 | 60–150+ Jahre |
| DZR-Messing | 0,05–0,15 | 15–30 Jahre |
| Yellow Brass (C85200) | 0,5–2,0 (Dezinkifizierung!) | 3–10 Jahre |
| 316L (passiv) | 0,001–0,01 | 80+ Jahre |
| 316L (Spaltkorrosion) | 0,1–1,0 | 5–20 Jahre |
| Komposit (GFK) | 0,00 (keine Korrosion) | UV-limitiert: 15–20 Jahre |

(Confidence: documented — NACE Corrosion Data Survey, Copper Development Association)

---

## 12. Einbau-/Austausch-Anleitung

### 12.1 Vorbereitung

#### 12.1.1 Werkzeugliste

| Werkzeug | Zweck |
|---|---|
| Lochsäge (passender Durchmesser) | Bohrung im Rumpf |
| Senker/Fräser | Saubere Innenkante |
| Rohrzange 300 mm | Borddurchlass festhalten |
| Gabelschlüssel (passend) | Gegenmutter / Seeventil |
| Drehmomentschlüssel | Definiertes Anzugsmoment |
| Schleifpapier 80er | Oberfläche aufrauen |
| Aceton | Entfetten |
| Dichtmasse (Sikaflex 291 / 3M 4200) | Abdichtung |
| Primer (Sika 209D) | Haftvermittler auf GFK |
| Gewindedichtband (PTFE) | Nur bei NPT-Gewinden! |
| Klebeband | Bohrungsschutz |
| Holzpfropfen (passend) | Sofort griffbereit! |

#### 12.1.2 Haul-Out Planung

**IMMER an Land arbeiten!** Niemals Borddurchlässe im Wasser bearbeiten.

| Phase | Dauer | Kosten (Werft DE) |
|---|---|---|
| Kranen + Abstellen | 1 h | 200–400 EUR |
| Unterwasserschiff reinigen | 2 h | 150–300 EUR |
| Pro Seeventil Austausch | 3–6 h | 250–500 EUR (Arbeit) |
| Antifouling nach Austausch | 4 h | 200–400 EUR |
| Kranen + Einwassern | 1 h | 200–400 EUR |
| **Gesamt 1 Seeventil** | **1,5–2 Tage** | **800–1.800 EUR** (inkl. Material) |

### 12.2 Schritt-für-Schritt: Austausch eines Borddurchlasses mit Seeventil

#### Schritt 1: Altes Seeventil entfernen
1. Boot an Land, Rumpf trocken
2. Schlauch vom Seeventil lösen (Schlauchschellen entfernen)
3. Seeventil vom Borddurchlass abschrauben
4. Borddurchlass von INNEN lösen (Gegenmutter oder Flansch)
5. Borddurchlass nach AUSSEN herausdrücken
6. Alte Dichtmasse sauber entfernen (Spachtel + Aceton)
7. Bohrung inspizieren: Risse? Delamination? Wasser im Laminat?

#### Schritt 2: Bohrung vorbereiten (bei Neuinstallation)
1. Position markieren (möglichst flacher Rumpfbereich)
2. Von INNEN bohren (sauberer Schnitt)
3. Lochsäge verwenden, NICHT Bohrmaschine
4. Langsam bohren, GFK nicht überhitzen
5. Bohrungsrand von innen und außen entgraten
6. **KRITISCH**: GFK-Schnittkante versiegeln!
   - Epoxidharz (z.B. West System 105/205) auf Schnittkante auftragen
   - 2 Schichten, mit 4 h Trockenzeit zwischen Schichten
   - Dies verhindert Wasseraufnahme ins Laminat (osmotische Blasenbildung)

#### Schritt 3: Backing-Block vorbereiten
1. G10-Platte oder GFK-Handlaminat auf Rumpfinnenseite anpassen
2. Backing-Block muss plan auf der Rumpf-Innenseite aufliegen
3. Bei gekrümmtem Rumpf: Block anschleifen oder mit Epoxid-Spachtel anformen
4. Bohrung im Backing-Block für Borddurchlass
5. Backing-Block Oberfläche anschleifen (80er)

#### Schritt 4: Borddurchlass einsetzen
1. Testmontage OHNE Dichtmasse — alles passt?
2. GFK-Oberfläche um Bohrung anschleifen (80er, 50 mm Rand)
3. Entfetten (Aceton)
4. Primer auftragen (Sika 209D auf GFK, 30 min trocknen)
5. Dichtmasse großzügig auf Borddurchlass-Flansch auftragen
6. Borddurchlass von AUSSEN einsetzen
7. Von INNEN: Dichtmasse auf Backing-Block
8. Backing-Block aufsetzen
9. Gegenmutter / Seeventil aufschrauben
10. **ACHTUNG Gewindedichtband**: NUR bei NPT-Gewinden verwenden! Bei BSP-Gewinden: Dichtung über O-Ring oder Flachdichtung, KEIN Teflonband!
11. Anziehen: handfest + ¼ Umdrehung (ca. 15–25 Nm bei DN38)
12. Überstehende Dichtmasse NICHT abwischen

#### Schritt 5: Seeventil montieren
1. O-Ring / Flachdichtung zwischen Borddurchlass und Seeventil prüfen
2. Seeventil aufschrauben
3. Ausrichtung: Griff muss in Schließstellung parallel zum Rumpf zeigen
4. Bei Kugelventil: Griff in Schließstellung = quer zum Durchfluss
5. Festziehen (15–25 Nm bei DN38)
6. Funktionsprüfung: Ventil mehrmals öffnen und schließen

#### Schritt 6: Schlauchverbindung
1. Schlauchtülle aufschrauben (wenn nicht integriert)
2. Schlauch aufschieben (ggf. mit Seifenwasser gleitmittel)
3. ZWEI Schlauchschellen montieren (316L, ≥12 mm breit)
4. Erste Schelle: 10 mm vom Schlauchende
5. Zweite Schelle: 25 mm von erster Schelle
6. Drehmoment: 2,5–3,5 Nm
7. Schraubköpfe um 90° versetzt (nicht übereinander)

#### Schritt 7: Endkontrolle
1. 24–48 h Aushärtung der Dichtmasse abwarten
2. Seeventil SCHLIESSEN
3. Boot zu Wasser lassen
4. 1 h warten
5. Alle Verbindungen auf Tropfen prüfen (trockenes Papiertuch)
6. Seeventil ÖFFNEN
7. Wieder alle Verbindungen prüfen
8. Notholzpfropfen am Borddurchlass befestigen
9. Dokumentation: Datum, Material, Hersteller, Drehmomente

(Confidence: documented — ABYC H-27, Nigel Calder "Boatowner's Mechanical Manual", Practical Sailor)

### 12.3 Spezialfall: Austausch auf Aluminium-Rumpf

| Schritt | Beschreibung | WARNUNG |
|---|---|---|
| 1 | Altes Ventil entfernen (wie 12.2 Schritt 1) | — |
| 2 | Aluminium-Oberfläche säurefrei reinigen | KEIN Essig, KEINE Säure auf Alu! |
| 3 | NUR Komposit-Borddurchlass verwenden | Bronze auf Alu = ZERSTÖRUNG |
| 4 | Dichtmasse: Sikaflex 291 oder 3M 4200 | Sika Primer 209D auf Alu |
| 5 | Komposit-Seeventil montieren | — |
| 6 | Schlauchschellen: Kunststoff-beschichtet | Metall-Schelle darf NICHT Alu-Rumpf berühren |
| 7 | Opferanoden prüfen (Alu-Rumpf braucht höhere Anodenkapazität) | — |

### 12.4 Spezialfall: Austausch auf Stahl-Rumpf

| Schritt | Beschreibung | WARNUNG |
|---|---|---|
| 1 | Stahl-Stutzen ist eingeschweißt — NICHT entfernen ohne Schweißer | — |
| 2 | Wenn Stutzen intakt: Nur Seeventil auf Flansch wechseln | — |
| 3 | Wenn Stutzen korrodiert: Neuen Stutzen einschweißen lassen | Zertifizierter Schweißer! |
| 4 | Isolier-Flansch zwischen Stahl und Bronze-Ventil | Verhindert galvanische Korrosion |
| 5 | Dichtmasse: Sikaflex 291 | — |
| 6 | Stahl um Durchlass innen + außen mit Epoxid-Primer beschichten | Korrosionsschutz |

### 12.5 Werkstattkosten-Kalkulation (Deutschland 2024/25)

| Position | Stundensatz | Stunden pro Ventil | Kosten |
|---|---|---|---|
| Haul-Out (Kran, Böcke, Platz) | pauschal | — | 200–500 EUR |
| Reinigung Unterwasserschiff | 45–65 EUR/h | 2–4 h | 90–260 EUR |
| Altes Ventil ausbauen | 65–85 EUR/h | 1–2 h | 65–170 EUR |
| Bohrung vorbereiten / GFK versiegeln | 65–85 EUR/h | 1–2 h | 65–170 EUR |
| Neues Ventil einbauen + abdichten | 65–85 EUR/h | 1,5–3 h | 100–255 EUR |
| Schlauchverbindung herstellen | 65–85 EUR/h | 0,5–1 h | 35–85 EUR |
| Antifouling (anteilig) | 45–65 EUR/h | 1–2 h | 45–130 EUR |
| Einwassern (Kran) | pauschal | — | 200–500 EUR |
| **Gesamt 1 Seeventil-Austausch** | | **6–14 h** | **800–2.070 EUR** |
| **Davon Material** | | | **80–350 EUR** |
| **Davon Arbeit** | | | **400–1.220 EUR** |
| **Davon Haul-Out (anteilig)** | | | **200–500 EUR** |

**Tipp**: Wenn ohnehin Haul-Out fällig (Antifouling), dann alle Seeventile gleichzeitig prüfen/tauschen — Haul-Out-Kosten nur 1× statt pro Ventil.

### 12.6 DIY vs. Werft — Entscheidungshilfe

| Kriterium | DIY empfohlen | Werft empfohlen |
|---|---|---|
| Erfahrung | Erfahrener Boot-Eigner mit GFK-Kenntnissen | Erstmalig, keine GFK-Erfahrung |
| Komplexität | 1:1 Austausch (gleiche Größe/Position) | Neue Position, andere Größe |
| Rumpfmaterial | GFK (Standard) | Alu, Stahl (Schweißen nötig) |
| Anzahl | 1–2 Ventile | >3 Ventile (Effizienz) |
| Versicherung | Versicherer akzeptiert DIY | Versicherer verlangt Werft-Nachweis |
| Werkzeug | Vorhanden (Lochsäge, Rohrzange etc.) | Nicht vorhanden |
| Zeitdruck | Kein Zeitdruck (Boot steht an Land) | Boot muss schnell ins Wasser |

**AYDI-Empfehlung**: Erster Seeventil-Austausch IMMER durch Fachwerft. Danach, mit Erfahrung und unter Anleitung, ggf. DIY möglich. NIEMALS unter Zeitdruck arbeiten — Fehler beim Einbau = Sinkgefahr.

(Confidence: documented + estimated — Werft-Preislisten Norddeutschland 2024/25)

---

## 13. Lebensdauer und Alterungsmechanismen

### 13.1 Lebensdauer-Übersicht

| Material | Erwartete Lebensdauer | Hauptversagensmechanismus | Wartungsintervall |
|---|---|---|---|
| Bronze C83600 | 30–50+ Jahre | Erosion, Spaltkorrosion | Jährliche Betätigung |
| Bronze C92200 | 40–60+ Jahre | Minimal | Jährliche Betätigung |
| DZR-Messing | 15–25 Jahre | Schleichende Dezinkifizierung | Jährlich + Säure-Test alle 5 Jahre |
| Yellow Brass | 3–10 Jahre | Dezinkifizierung — AKUT | SOFORT AUSTAUSCHEN |
| Komposit (TruDesign) | 15–20 Jahre | UV-Versprödung, Kriechverformung | Jährliche Sichtkontrolle |
| Komposit (Marelon) | 12–18 Jahre | UV, Wasseraufnahme (Nylon) | Jährliche Sichtkontrolle |
| Edelstahl 316L | 20–40 Jahre | Spaltkorrosion | Jährliche Kontrolle |

### 13.2 Alterungskurve Bronze-Seeventil (C83600)

```
Score
100 |████
 90 |█████████
 80 |██████████████
 70 |███████████████████
 60 |████████████████████████
 50 |█████████████████████████████
 40 |                               ████
 30 |                                   ████
 20 |                                       ████
 10 |                                           ████
  0 |_____________________________________________███
    0    5   10   15   20   25   30   35   40   45  50 Jahre

Legende:
- Jahre 0–15: Score 95–85 (langsame Abnahme, Patina-Bildung)
- Jahre 15–30: Score 85–65 (normaler Verschleiß, PTFE-Sitze erneuern)
- Jahre 30–40: Score 65–45 (Erosion, Wartungsbedarf steigt)
- Jahre 40–50: Score 45–20 (Austausch empfohlen)
```

### 13.3 Alterungskurve Messing-Seeventil (Yellow Brass — C85200)

```
Score
100 |██
 90 |████
 80 |█████
 70 |██████
 60 |███████
 50 |████████
 40 |█████████
 30 |██████████
 20 |███████████
 10 |████████████
  0 |_____________███████████████████████████████████
    0    1    2    3    4    5    6    7    8    9   10 Jahre

WARNUNG: Messing dezinkifiziert in Seewasser innerhalb von 3–10 Jahren!
Die Kurve zeigt, dass der Score schon nach 3 Jahren unter 50 fallen kann.
Ab Score <30: AKUTE SINKGEFAHR!
```

### 13.4 Spezifische Alterungsmechanismen

#### 13.4.1 PTFE-Sitz-Degradation (Kugelventile)

- PTFE-Dichtflächen verhärten über 10–15 Jahre
- Mikrokratzer durch Sand/Schmutz im Wasser
- Ergebnis: Ventil wird undicht (Sickerwasser)
- Lösung: PTFE-Sitze erneuern (Groco, Guidi bieten Reparatur-Kits)
- Reparatur-Kit Preis: 15–45 EUR

#### 13.4.2 Küken-Verschleiß (Kegelventile)

- Konischer Küken nutzt sich ab (Erosion durch Seewasser)
- Ergebnis: Ventil wird undicht
- Lösung: Küken nachschleifen (Fein-Schleifpaste, z.B. Clover Compound)
- Traditionelle Wartung: Jährlich Küken fetten (Wasserpumpenfett, KEIN Silikonfett)
- Küken-Nachschleifen: Alle 5–10 Jahre
- Lebensdauer nach Nachschleifen: Weitere 10–15 Jahre

#### 13.4.3 Bewuchsblockade

- Seepocken, Muscheln, Algen wachsen in Borddurchlass
- Besonders bei selten benutzten Booten (Winterlager im Wasser)
- Ergebnis: Kühlwassermangel → Motorüberhitzung
- Lösung: Jährlich bei Haul-Out mechanisch reinigen
- Vorbeugung: Antifouling auch in Borddurchlass-Bereich

(Confidence: documented — Marine Surveyor Association, Practical Sailor, Steve D'Antonio)

### 13.5 Wartungskalender — Empfehlung AYDI

#### Monatliche Kontrolle (bei Nutzung)

| Prüfpunkt | Aufwand | Werkzeug |
|---|---|---|
| Bilge auf Wassereinbruch prüfen | 2 min | Taschenlampe |
| Sichtbare Feuchtigkeit an Seeventilen? | 5 min | Taschenlampe |
| Bilgenpumpe funktioniert? | 1 min | — |

#### Saisonbeginn (Frühling)

| Prüfpunkt | Aufwand | Werkzeug |
|---|---|---|
| Alle Seeventile betätigen (auf/zu/auf) | 15 min | — |
| Schlauchverbindungen visuell prüfen | 10 min | Taschenlampe |
| Holzpfropfen vorhanden und griffbereit? | 5 min | — |
| Opferanoden prüfen (bei Bronze) | 5 min | — |
| Kegelventile fetten (falls vorhanden) | 15 min | Wasserpumpenfett |

#### Saisonende (Herbst/Winter)

| Prüfpunkt | Aufwand | Werkzeug |
|---|---|---|
| Alle Seeventile betätigen | 15 min | — |
| Kühlwassersystem mit Frostschutz spülen | 30 min | Propylenglykol |
| Ventile an Land: OFFEN lassen | 5 min | — |
| Ventile im Wasser: GESCHLOSSEN | 5 min | — |
| Schlauchschellen-Drehmoment prüfen | 15 min | Schraubendreher |

#### Jährlich (bei Haul-Out)

| Prüfpunkt | Aufwand | Werkzeug |
|---|---|---|
| Alle Borddurchlässe von außen inspizieren | 20 min | Taschenlampe |
| Mushroom-Durchlässe auf Risse/Brüche prüfen | 10 min | Taschenlampe |
| Bewuchs in Borddurchlässen entfernen | 30 min | Bürste, Spachtel |
| Dichtmasse auf Risse/Ablösung prüfen | 15 min | Taschenlampe |
| Backing-Blocks auf festen Sitz prüfen | 10 min | Hand |
| Antifouling um Borddurchlässe auftragen | 15 min | Pinsel |

#### Alle 5 Jahre

| Prüfpunkt | Aufwand | Werkzeug |
|---|---|---|
| Salpetersäure-Test bei Cu-Legierungen (>10 J.) | 30 min | HNO₃ 10%, Schutzbrille |
| Ultraschall-Wandstärkenmessung (bei Bronze >20 J.) | 1 h | UT-Messgerät |
| Dichtmasse erneuern (älteste Ventile zuerst) | 2–4 h/Ventil | Dichtmasse, Primer |
| PTFE-Sitze prüfen/erneuern (Kugelventile) | 1 h/Ventil | Reparatur-Kit |
| Schlauchzustand prüfen (Verhärtung, Risse?) | 30 min | — |

### 13.6 Lebensdauer-Kostenrechnung (Total Cost of Ownership)

#### Bronze C83600 — 30-Jahres-TCO (6 Ventile, Segelboot 10 m)

| Position | Kosten | Zeitpunkt |
|---|---|---|
| Erstinstallation (6× DN25–DN38) | 900 EUR | Jahr 0 |
| Jährliche Wartung (30× Eigenleistung) | 0 EUR | Jährlich |
| Schlauchschellen erneuern (2× in 30 Jahren) | 100 EUR | Jahr 10, 20 |
| PTFE-Sitze erneuern (2× in 30 Jahren) | 180 EUR | Jahr 12, 24 |
| Dichtmasse erneuern (2× in 30 Jahren) | 240 EUR | Jahr 15, 25 |
| Opferanoden (anteilig, 30 Jahre) | 300 EUR | Alle 2 Jahre |
| **Gesamt 30 Jahre** | **~1.720 EUR** | |
| **Pro Jahr** | **~57 EUR** | |

#### Komposit TruDesign — 30-Jahres-TCO (6 Ventile, Segelboot 10 m)

| Position | Kosten | Zeitpunkt |
|---|---|---|
| Erstinstallation (6× DN25–DN38) | 600 EUR | Jahr 0 |
| Jährliche Wartung | 0 EUR | Jährlich |
| Schlauchschellen erneuern (2× in 30 Jahren) | 100 EUR | Jahr 10, 20 |
| Komplett-Austausch nach 15 Jahren | 600 EUR | Jahr 15 |
| Opferanoden (KEINE — kein Metall) | 0 EUR | — |
| **Gesamt 30 Jahre** | **~1.300 EUR** | |
| **Pro Jahr** | **~43 EUR** | |

#### Messing (C85200) — 30-Jahres-TCO — WARNUNG

| Position | Kosten | Zeitpunkt |
|---|---|---|
| Erstinstallation (6× DN25–DN38) | 400 EUR | Jahr 0 |
| Austausch nach Dezinkifizierung | 1.800 EUR | Jahr 5–8 |
| ODER: Boot sinkt | 50.000+ EUR | Jahr 3–10 |
| **Gesamt bei rechtzeitigem Austausch** | **~2.200 EUR** | |
| **Gesamt bei Totalverlust** | **50.000+ EUR** | |

**FAZIT**: Messing ist die "billigste" Option beim Kauf und die TEUERSTE über die Lebensdauer.

(Confidence: estimated — Kalkulation basierend auf Herstellerpreisen + Werft-Stundensätzen)

### 13.7 Visueller Alterungs-Guide für AYDI Pipeline B

**Anleitung für die visuelle Zustandsbewertung aus Fotos:**

| Visueller Befund | Material | Bedeutung | Score-Anpassung |
|---|---|---|---|
| Gleichmäßige grüne Patina | Bronze | Normal, schützend | Keine Abzüge |
| Ungleichmäßige grüne Flecken mit Lochfraß | Bronze | Galvanische Korrosion | -20 Punkte |
| Rosa/kupferfarbene Stellen auf gelber Oberfläche | Messing | Dezinkifizierung! | Score = 10 |
| Weiße Kristalle am Flansch | Alle Metalle | Salzausblühung = Undichtigkeit | -15 Punkte |
| Grünliche Flüssigkeitsspuren | Alle Metalle | Aktiver Wasseraustritt | -25 Punkte |
| Milchig-weiße Verfärbung | Komposit | UV-Degradation | -10 Punkte |
| Sichtbare Haarrisse | Komposit | Strukturelle Schwächung | Score ≤ 35 |
| Brauner/schwarzer Bewuchs im Borddurchlass | Alle | Biofouling | -5 Punkte |
| Fehlender Griff | Alle | Notfall-Unfähigkeit | -15 Punkte |
| Rostige Schlauchschelle | — | Falsches Material (nicht 316L) | -10 Punkte |
| Nur 1 Schlauchschelle unter WL | — | ABYC-Verstoß | -10 Punkte |
| Handrad statt Hebel | — | Gate-Ventil! VERBOTEN! | Score = 15 |

(Confidence: documented — AYDI Visual Analysis Framework, Survey Photography Standards)

---

## 14. Fehlerbild-Atlas

### 14.1 Fehlerbild FB-SV-01: Dezinkifizierung

**Befund**: Seeventil aus Messing zeigt rötlich-rosa Verfärbung. Oberfläche fühlt sich schwammig an. Klopftest ergibt dumpfen Ton statt metallischem Klang.

**Mechanismus**: Selektive Korrosion löst Zink aus der Cu-Zn-Legierung. Zurück bleibt poröses, strukturell geschwächtes Kupfer. Das Bauteil behält seine Form, verliert aber 80–90% seiner Festigkeit.

**Erkennung**: Visuell (rosa statt goldgelb), Klopftest (dumpf), Kratztest (weich, krümelig), Salpetersäure-Spot-Test (rötlich = dezinkifiziert).

**Risiko**: KRITISCH — Score 5. Ventil kann jederzeit brechen. Wassereinbruch → SINKEN.

**Maßnahme**: SOFORTIGER Austausch gegen Bronze C83600 oder Komposit. Boot NICHT ins Wasser lassen bis Austausch erfolgt.

**Confidence**: visual_high (bei klarer rosa Verfärbung), documented (bei Säure-Test-Bestätigung).

**AYDI-Empfehlung**: "Dezinkifizierung nachgewiesen. SOFORTIGER Austausch! Boot NICHT einwassern!" — Dringlichkeit: "sofort".

**Typisch bei**: Boote >10 Jahre mit Yellow-Brass-Ventilen, Mittelmeer, warme Reviere.

**Kosten Behebung**: 150–400 EUR pro Ventil (Material + Einbau bei Haul-Out).

**Versicherung**: Messing-Ventile = Ausschlussgrund bei den meisten Versicherern.

**Vorbeugung**: Ausschließlich Bronze C83600/C92200 oder Komposit verwenden.

**Referenz**: CDA Publication 154 "Dezincification", Steve D'Antonio "Seacocks and Through-Hulls".

### 14.2 Fehlerbild FB-SV-02: Galvanische Korrosion / Elektrolyse

**Befund**: Bronze-Seeventil zeigt starke grüne Patina, Lochfraß oder aufgelöste Oberfläche. Typisch bei Booten mit Landstromanschluss ohne galvanischen Isolator.

**Mechanismus**: Streuströme von benachbarten Booten oder fehlerhafte Landstrom-Installation erzeugen elektrochemische Potentialdifferenz. Das unedelste Metall im System wird zur Opferanode und löst sich auf.

**Erkennung**: Grüne/weiße Ablagerungen, Lochfraß, Materialverlust am Ventilkörper. Im schlimmsten Fall: Ventilwand durchkorrodiert.

**Risiko**: HOCH — Score 15–30 je nach Materialverlust. Durchkorrodierte Wand = SINKEN.

**Maßnahme**: Galvanischen Isolator installieren (z.B. Victron GI, ca. 85 EUR). Opferanoden prüfen/erneuern. Betroffene Ventile ersetzen. Landstrom-Installation prüfen lassen (Fehlerstromschutz).

**Confidence**: visual_high (bei deutlichem Lochfraß).

**AYDI-Empfehlung**: "Galvanische Korrosion an Seeventil. Galvanischen Isolator installieren. Betroffenes Ventil austauschen." — Dringlichkeit: "innerhalb_30_tage".

**Typisch bei**: Boote in Marinas mit Landstrom, fehlender Galvanischer Isolator, gemischte Metallanlagen (Bronze + Edelstahl ohne Isolation).

**Kosten Behebung**: 85–150 EUR (Isolator) + 150–400 EUR (Ventiltausch).

**Referenz**: ABYC E-11 (Electrical Systems), Nigel Calder "Boatowner's Electrical Manual".

### 14.3 Fehlerbild FB-SV-03: Festsitzendes Ventil (Frozen Valve)

**Befund**: Seeventil lässt sich nicht mehr betätigen. Griff kann nicht gedreht werden, auch nicht mit Werkzeug (moderater Kraftaufwand).

**Mechanismus**: Korrosionsprodukte, Kalkablagerungen, Bewuchs oder Mangel an Wartung (nie betätigt) führen zum Festsitzen der Kugel oder des Kükens im Ventilkörper.

**Erkennung**: Griff lässt sich nicht drehen. Bei forciertem Drehen: Griff bricht ab (→ Fehlerbild FB-SV-10).

**Risiko**: KRITISCH — Score 25. Im Notfall kann das Ventil NICHT geschlossen werden! Wassereinbruch → SINKEN.

**Maßnahme**: Bei Kegelventil: Küken lösen (von innen), reinigen, nachschleifen, fetten. Bei Kugelventil: Vorsichtig mit Penetrieröl (WD-40 oder Kroil) lösen, wenn erfolglos: Austausch.

**WARNUNG**: NIEMALS mit extremer Kraft am Griff drehen! Bruchgefahr am Ventilkörper → sofortiger Wassereinbruch.

**Confidence**: measured (wenn Ventil manuell geprüft), visual_medium (wenn nur visuell beurteilt).

**AYDI-Empfehlung**: "Seeventil festsitzend. Im Notfall kann nicht geschlossen werden! Austausch empfohlen." — Dringlichkeit: "nächstes_haul_out" (wenn über WL) oder "innerhalb_30_tage" (wenn unter WL).

**Vorbeugung**: JEDES Seeventil mindestens 2× jährlich durchbewegen (auf/zu/auf). Kegelventile jährlich fetten.

**Typisch bei**: Boote, die selten gesegelt werden, Charterboote ohne Wartung, Winterlager im Wasser ohne Konservierung.

**Referenz**: ABYC H-27.6.1 (jährliche Betätigung + Inspektion).

### 14.4 Fehlerbild FB-SV-04: Gerissenes Komposit-Ventil

**Befund**: Komposit-Seeventil zeigt sichtbare Risse, Haarrisse oder Bruchstellen am Ventilkörper.

**Mechanismus**: UV-Strahlung degradiert die Polymermatrix. Glasfasern werden freigelegt. Mikrorisse entstehen und wachsen unter Last. Frostschaden bei Wasser im Ventilkörper (Eisbildung). Mechanische Überbelastung (Schlauch-Hebelwirkung).

**Erkennung**: Sichtbare Risse, milchig-weiße Verfärbung (UV), sprödes Verhalten beim Klopftest, Haarrisse unter Lupe.

**Risiko**: HOCH — Score 15–35 je nach Risstiefe. Durchgehender Riss = Wassereinbruch = SINKEN.

**Maßnahme**: SOFORTIGER Austausch. Komposit-Ventile können NICHT repariert werden. Bei Rissbildung ist die strukturelle Integrität nicht mehr gewährleistet.

**Confidence**: visual_high (bei sichtbarem Riss), visual_medium (bei Verfärbung ohne sichtbaren Riss).

**AYDI-Empfehlung**: "Rissbildung an Komposit-Seeventil. SOFORT austauschen! Keine Reparaturmöglichkeit." — Dringlichkeit: "sofort".

**Typisch bei**: Komposit-Ventile >15 Jahre, UV-Exposition (offener Maschinenraum), Frostschaden.

**Kosten Behebung**: 65–220 EUR (Material) + 250–500 EUR (Einbau).

**Referenz**: ISO 9093-2, TruDesign Technical Bulletin TB-2023-04.

### 14.5 Fehlerbild FB-SV-05: Loser Backing-Block

**Befund**: Backing-Block hat sich vom Rumpf-Laminat gelöst oder ist lose. Seeventil bewegt sich bei Belastung.

**Mechanismus**: Dichtmasse zwischen Backing-Block und Rumpf versagt. Vibration (Motor). Wassereinbruch zwischen Block und Laminat → osmotische Blasen. Unzureichende Verklebung bei Erstinstallation.

**Erkennung**: Seeventil wackelt bei manuellem Test. Feuchtigkeit um Backing-Block. Dichtmasse sichtbar abgelöst.

**Risiko**: HOCH — Score 20–40. Ohne festen Backing-Block drückt Wasserdruck den Borddurchlass nach innen → Wassereinbruch.

**Maßnahme**: Seeventil ausbauen, alten Backing-Block entfernen, Fläche reinigen, neuen Backing-Block mit Epoxid + Dichtmasse montieren.

**Confidence**: visual_high (wenn Bewegung sichtbar), measured (wenn manuell geprüft).

**AYDI-Empfehlung**: "Backing-Block gelöst. Seeventil nicht sicher fixiert. Neuinstallation erforderlich." — Dringlichkeit: "nächstes_haul_out".

**Typisch bei**: Marine-Sperrholz-Backing-Blocks >10 Jahre, DIY-Installationen ohne ausreichend Dichtmasse.

**Kosten Behebung**: 50–150 EUR (Material) + 200–400 EUR (Arbeit).

### 14.6 Fehlerbild FB-SV-06: Versagte Dichtmasse (Bedding Failure)

**Befund**: Dichtmasse zwischen Borddurchlass und Rumpf ist gerissen, geschrumpft oder hat sich gelöst. Sickerwasser um den Borddurchlass.

**Mechanismus**: Falsche Dichtmasse verwendet (Silikon statt PU). Alterung der Dichtmasse (>15 Jahre). Bewegung des Borddurchlasses (fehlender Backing-Block). UV-Degradation (wenn Dichtmasse Licht ausgesetzt).

**Erkennung**: Feuchtigkeit um Borddurchlass innen, Wasserspuren, sichtbar gerissene Dichtmasse.

**Risiko**: MITTEL-HOCH — Score 30–50. Langsamer Wassereinbruch, der bei Seegang zunehmen kann.

**Maßnahme**: Borddurchlass ausbauen, alte Dichtmasse komplett entfernen, Oberfläche reinigen, neu abdichten (3M 4200 oder Sikaflex 291).

**Confidence**: visual_high (wenn Wasser sichtbar), visual_medium (wenn nur Dichtmasse gerissen).

**AYDI-Empfehlung**: "Dichtmasse am Borddurchlass versagt. Neu abdichten beim nächsten Haul-Out." — Dringlichkeit: "nächstes_haul_out".

**Typisch bei**: Boote >15 Jahre, Silikon statt PU verwendet, fehlender Primer.

**Kosten Behebung**: 30–80 EUR (Material) + 200–400 EUR (Arbeit).

### 14.7 Fehlerbild FB-SV-07: Korrodierte Schlauchtülle (Corroded Hose Barb)

**Befund**: Die Schlauchtülle am Seeventilausgang zeigt starke Korrosion, Lochfraß oder Materialverlust.

**Mechanismus**: Galvanische Korrosion zwischen Tülle und Schlauchschelle (wenn Schelle aus anderem Metall). Spaltkorrosion unter der Schelle. Erosionskorrosion durch Wasserströmung.

**Erkennung**: Grüne Patina, aufgerauhte Oberfläche, sichtbarer Materialverlust, Schlauch sitzt nicht mehr fest.

**Risiko**: HOCH — Score 20–40. Schlauch kann abplatzen → Wassereinbruch = SINKEN.

**Maßnahme**: Schlauchtülle ersetzen (wenn verschraubt). Bei integrierter Tülle: ganzes Ventil ersetzen. Schlauchschellen aus 316L verwenden.

**Confidence**: visual_high (bei sichtbarem Materialverlust).

**AYDI-Empfehlung**: "Korrodierte Schlauchtülle. Schlauchverbindung nicht mehr sicher. Austausch erforderlich." — Dringlichkeit: "innerhalb_30_tage".

**Typisch bei**: Gemischte Metalle (Bronze-Tülle + verzinkte Schelle), feuchte Umgebung, mangelhafte Belüftung.

**Kosten Behebung**: 25–80 EUR (Material) + 100–200 EUR (Arbeit).

### 14.8 Fehlerbild FB-SV-08: Gate-Ventil versagt (Gate Valve Failure)

**Befund**: Schieberventil (Gate Valve) als Seeventil eingebaut. Schieber korrodiert fest, lässt sich nicht mehr bewegen. Oder: Schieber schließt nicht vollständig (Korrosionsablagerungen auf der Dichtfläche).

**Mechanismus**: Gate-Ventile sind für statische Systeme konzipiert, nicht für die dynamische, korrosive Meeresumgebung. Der Schieber korrodiert in der Führung fest. Die Dichtfläche erodiert durch Partikel im Seewasser.

**Erkennung**: Mehrere Umdrehungen nötig zum Schließen (→ zu langsam im Notfall). Handrad schwergängig oder festsitzend. Sickerwasser auch bei "geschlossenem" Ventil.

**Risiko**: KRITISCH — Score 15. Gate-Ventile sind als Seeventile VERBOTEN (ABYC H-27, ISO 9093). Versagen im Notfall quasi garantiert.

**Maßnahme**: SOFORTIGER Austausch gegen Kugelventil oder Kegelventil. Kein Kompromiss.

**Confidence**: visual_high (Gate-Ventil ist eindeutig erkennbar am Handrad statt Hebel).

**AYDI-Empfehlung**: "VERBOTEN: Schieberventil als Seeventil! SOFORT gegen Kugelventil austauschen!" — Dringlichkeit: "sofort".

**Typisch bei**: Ältere US-Boote (vor 1990), DIY mit Baumarkt-Ventilen, Billig-Importe.

**Kosten Behebung**: 80–250 EUR (Material) + 250–500 EUR (Arbeit).

### 14.9 Fehlerbild FB-SV-09: Mushroom-Bruch (Through-Hull Fracture)

**Befund**: Pilzförmiger Borddurchlass ist am Hals (Übergang Flansch → Gewinde) gebrochen oder gerissen.

**Mechanismus**: Grundberührung (Kiel/Rumpf setzt auf). Seitliche Belastung durch steife Schlauchleitungen. Dezinkifizierung hat Wandstärke reduziert. Materialfehler (Lunker im Guss). Eisbersbelastung.

**Erkennung**: Sichtbarer Riss oder Bruch am Borddurchlass. Im schlimmsten Fall: Borddurchlass fehlt ganz (abgebrochen und rausgefallen).

**Risiko**: KRITISCH — Score 0–10. Offenes Loch im Rumpf = SOFORTIGES SINKEN.

**Maßnahme**: NOTFALL: Holzpfropfen einschlagen! Dann: Neuen Borddurchlass einsetzen.

**Confidence**: visual_high (wenn sichtbar), measured (wenn Bruch ertastet).

**AYDI-Empfehlung**: "NOTFALL: Borddurchlass gebrochen! Holzpfropfen bereithalten. SOFORT reparieren!" — Dringlichkeit: "sofort".

**Typisch bei**: Dezinkifizierte Messing-Durchlässe, Grundberührung, Boote >25 Jahre ohne Inspektion.

**Kosten Behebung**: 25–180 EUR (Material) + 250–500 EUR (Arbeit bei Haul-Out).

### 14.10 Fehlerbild FB-SV-10: Griffbruch (Handle Breakage)

**Befund**: Griff des Seeventils ist abgebrochen oder fehlt. Ventil kann nicht mehr betätigt werden.

**Mechanismus**: Übermäßige Kraft beim Versuch, festsitzendes Ventil zu öffnen/schließen. Korrosion am Griffansatz. UV-Versprödung bei Kunststoffgriffen. Vandalismus/Unachtsamkeit.

**Erkennung**: Fehlender oder gebrochener Griff. Vierkant-Antrieb am Ventilkörper sichtbar.

**Risiko**: HOCH — Score 25–35. Ohne Griff kann das Ventil im Notfall nur mit Zange geschlossen werden (wenn überhaupt erreichbar).

**Maßnahme**: Ersatzgriff montieren (Hersteller-Ersatzteil) oder Notbehelf: passende Rohrzange am Ventil deponieren.

**Confidence**: visual_high (fehlender Griff sofort erkennbar).

**AYDI-Empfehlung**: "Seeventil-Griff fehlt/gebrochen. Ersatzgriff montieren oder Notbetätigungswerkzeug bereitlegen." — Dringlichkeit: "innerhalb_30_tage".

**Kosten Behebung**: 10–35 EUR (Ersatzgriff).

### 14.11 Fehlerbild FB-SV-11: Tropfender Flansch (Weeping Flange)

**Befund**: Am Flansch zwischen Borddurchlass und Seeventil tropft langsam Wasser.

**Mechanismus**: O-Ring oder Flachdichtung zwischen Borddurchlass und Seeventil altert. Flansch hat sich gelöst (Vibration). Falscher Dichtungstyp verwendet.

**Erkennung**: Feuchte Stellen, Tropfen, Kalkablagerungen am Flansch, Salzkristalle.

**Risiko**: MITTEL — Score 40–55. Langsamer Wassereinbruch, der bei Seegang zunimmt.

**Maßnahme**: Flansch nachziehen (evtl. Dichtung erneuern). ACHTUNG: Nur an Land nachziehen — bei Wasser von außen kann sich der Borddurchlass lösen!

**Confidence**: visual_high (Tropfen/Kalkspuren sichtbar).

**AYDI-Empfehlung**: "Tropfender Flansch am Seeventil. Dichtung erneuern beim nächsten Haul-Out." — Dringlichkeit: "nächstes_haul_out".

**Kosten Behebung**: 5–15 EUR (Dichtung) + 100–200 EUR (Arbeit).

### 14.12 Fehlerbild FB-SV-12: Bewuchsblockade (Biofouling Blockage)

**Befund**: Borddurchlass oder Seeventil durch Seepocken, Muscheln oder Algenbewuchs teilweise oder vollständig blockiert.

**Mechanismus**: Organismen siedeln sich auf allen rauen Unterwasseroberflächen an. Besonders in warmem Wasser (>15°C) und bei stehenden Booten. Borddurchlass-Innenseite ist oft nicht antifoulingbeschichtet.

**Erkennung**: Reduzierter Durchfluss (Motor überhitzt). Visuell: Bewuchs sichtbar im Borddurchlass oder am Mushroom von außen. Vollständig blockiert: kein Wasserfluss mehr.

**Risiko**: MITTEL — Score 45–60. Nicht direkt sinkgefahr, aber Motor-Überhitzung und reduzierte Pumpenwirkung.

**Maßnahme**: Mechanische Reinigung bei Haul-Out. Antifouling auch im Borddurchlass-Bereich auftragen. Scoop-Strainer installieren. Bei Bewuchs im Ventil: Ventil demontieren und reinigen.

**Confidence**: visual_high (bei sichtbarem Bewuchs), estimated (bei reduziertem Durchfluss ohne visuelle Bestätigung).

**AYDI-Empfehlung**: "Bewuchs im Borddurchlass. Motorüberhitzung möglich. Reinigung beim nächsten Haul-Out." — Dringlichkeit: "nächstes_haul_out".

**Typisch bei**: Boote im warmen Seewasser, lange Liegezeiten, fehlendes Antifouling am Borddurchlass.

**Kosten Behebung**: 50–150 EUR (Reinigung bei Haul-Out).

(Confidence: documented — Marine Survey Reports, IIMS Best Practice, Steve D'Antonio)

---

## 15. Fehlerbehebungs-Leitfaden

### 15.1 Problem: Wassereinbruch am Seeventil

| Schritt | Aktion | Werkzeug |
|---|---|---|
| 1 | RUHE BEWAHREN — Wo kommt das Wasser her? | Taschenlampe |
| 2 | Seeventil SCHLIESSEN (Griff quer zum Rohr) | Hand |
| 3 | Kommt weiter Wasser? → Leck ist VOR dem Ventil (Flansch oder Borddurchlass) | — |
| 4 | Kein Wasser mehr? → Leck ist NACH dem Ventil (Schlauchverbindung) | — |
| 5a | Bei Leck VOR Ventil: Holzpfropfen vorbereiten. Flansch nachziehen VERSUCHEN. | Rohrzange |
| 5b | Bei Leck NACH Ventil: Schlauchschellen nachziehen oder Schlauch erneuern. | Schraubendreher |
| 6 | Wenn unkontrollierbar: Holzpfropfen in Borddurchlass treiben | Hammer |
| 7 | Bilgenpumpe einschalten (manuell + elektrisch) | — |
| 8 | Seenotfall melden wenn Boot nicht beherrschbar | VHF Kanal 16 |

### 15.2 Problem: Seeventil lässt sich nicht bewegen

| Schritt | Aktion | Werkzeug |
|---|---|---|
| 1 | NICHT mit Gewalt drehen! Bruchgefahr! | — |
| 2 | Penetrieröl auftragen (WD-40, Kroil, PB Blaster) | Sprühdose |
| 3 | 30 Minuten einwirken lassen | — |
| 4 | Vorsichtig versuchen, in BEIDE Richtungen zu bewegen | Hand, ggf. Rohrzange am Griff |
| 5 | Leichte Klopfbewegungen auf den Griff (löst Korrosion) | Gummihammer |
| 6 | Wenn nach 3 Versuchen kein Erfolg: NICHT weiter forcieren | — |
| 7 | Ventil als "nicht schließbar" markieren | Kabelbinder/Warnung |
| 8 | Austausch beim nächsten Haul-Out planen | — |
| 9 | Notholzpfropfen bereitlegen als Backup | — |

### 15.3 Problem: Verdacht auf Dezinkifizierung

| Schritt | Aktion | Werkzeug |
|---|---|---|
| 1 | Material identifizieren: Messing (goldgelb) vs. Bronze (rötlich-braun) | Auge |
| 2 | Oberfläche kratzen: Ist es weich/krümelig? | Taschenmesser |
| 3 | Klopftest: Dumpf (dezinkifiziert) vs. klingend (gesund) | Schraubendreher |
| 4 | Salpetersäure-Spot-Test (10% HNO₃) | Pipette, Schutzbrille! |
| 5a | Test positiv (rötlich): SOFORTIGER Austausch | — |
| 5b | Test negativ: Zur Sicherheit alle 5 Jahre wiederholen | — |
| 6 | Alle Ventile am Boot prüfen (wenn eines dezinkifiziert, oft alle betroffen) | — |

### 15.4 Problem: Schlauch vom Seeventil abgerutscht

| Schritt | Aktion | Werkzeug |
|---|---|---|
| 1 | SOFORT Seeventil schließen! | Hand |
| 2 | Bilgenpumpe einschalten | — |
| 3 | Wenn Ventil nicht erreichbar/nicht schließbar: Holzpfropfen in Borddurchlass | Hammer |
| 4 | Wenn kein Pfropfen: Lappen/Handtuch + Ferse in die Öffnung pressen | — |
| 5 | Sobald Wasser gestoppt: Schlauch wieder aufstecken | — |
| 6 | ZWEI neue Schlauchschellen montieren (alte waren offensichtlich unzureichend) | 316L Schellen |
| 7 | Ursache klären: Schlauch verhärtet? Tülle korrodiert? Zu wenig/falsche Schellen? | — |

### 15.5 Problem: Wassereinbruch — Borddurchlass gebrochen (NOTFALL)

| Schritt | Aktion | Werkzeug |
|---|---|---|
| 1 | MAYDAY vorbereiten (VHF Kanal 16) | VHF |
| 2 | Holzpfropfen in die Bruchstelle / das Loch treiben | Hammer |
| 3 | Wenn kein Pfropfen: Kissen, Matratze, Schwimmweste in/über das Loch | — |
| 4 | Alle Bilgenpumpen einschalten | — |
| 5 | Alle ANDEREN Seeventile schließen (Folgeschäden verhindern) | — |
| 6 | Crew informieren, Rettungswesten anlegen | — |
| 7 | Nächsten Hafen / Flachwasser ansteuern | — |
| 8 | Wenn Boot sinkt: Seenotrettungsmittel bereithalten, EPIRB aktivieren | — |

(Confidence: documented — MAIB Safety Bulletins, RYA Seamanship, Colregs)

---

## 16. FAQ (SV-001 bis SV-025)

### SV-001: Bronze oder Komposit — was ist besser?
**Antwort**: Beide sind gleichwertig sicher, wenn von einem anerkannten Hersteller und ISO 9093-konform. Bronze hält 30–50+ Jahre, ist schwerer und teurer. Komposit hält 15–20 Jahre, ist leichter, günstiger und verursacht keine galvanische Korrosion. Für Aluminium-Rümpfe: IMMER Komposit.
**Confidence**: documented

### SV-002: Wie erkenne ich, ob mein Seeventil aus Messing oder Bronze ist?
**Antwort**: Messing ist goldgelb, Bronze ist rötlich-braun (oft mit grüner Patina). Der sicherste Test: 10% Salpetersäure auf eine gereinigte Stelle — bei Bronze bleibt die Oberfläche grünlich, bei dezinkifiziertem Messing wird sie sofort rötlich-kupfern. Alternativ: Herstellerstempel prüfen.
**Confidence**: documented

### SV-003: Wie oft muss ein Seeventil bewegt werden?
**Antwort**: ABYC H-27 empfiehlt jährliche Betätigung. Best Practice: Jedes Seeventil mindestens 2× pro Saison vollständig öffnen und schließen. Kegelventile zusätzlich 1× jährlich fetten. Kugelventile: Ventilbewegung verhindert Korrosionsfestsetzen.
**Confidence**: documented

### SV-004: Darf ich ein Gate-Ventil (Schieberventil) als Seeventil verwenden?
**Antwort**: NEIN. Niemals. Gate-Ventile sind als Seeventile verboten (ABYC H-27, ISO 9093). Sie versagen zuverlässig im Notfall: zu langsam, korrodieren fest, kein positiver Verschluss. SOFORT gegen Kugelventil oder Kegelventil austauschen.
**Confidence**: documented

### SV-005: Was ist DZR-Messing und ist es sicher?
**Antwort**: DZR (Dezincification Resistant) Messing enthält Arsen-Inhibitoren, die Dezinkifizierung hemmen. Es ist akzeptabel für Boote <15 Jahre in gemäßigtem Klima, aber NICHT so langzeitstabil wie echte Bronze. Für Langzeitbesitz: Bronze C83600 oder C92200 bevorzugen.
**Confidence**: documented

### SV-006: Warum brauche ich doppelte Schlauchschellen?
**Antwort**: ABYC H-27 verlangt doppelte Schlauchschellen an ALLEN Verbindungen unter der Wasserlinie. Grund: Eine einzelne Schelle kann durch Vibration, Korrosion oder Materialermüdung versagen. Die zweite Schelle ist die Lebensversicherung. Kosten: 4–8 EUR pro Ventil — kein Argument bei Sinkgefahr.
**Confidence**: documented

### SV-007: Brauche ich einen Backing-Block?
**Antwort**: Bei GFK-Rümpfen: JA, immer. Der Backing-Block verteilt die Last auf eine größere Fläche des Laminats. Ohne Backing-Block kann der Wasserdruck den Borddurchlass durch das Laminat drücken. Bei Stahl- oder Alu-Rümpfen wird der Borddurchlass direkt verschweißt/verschraubt.
**Confidence**: documented

### SV-008: Welche Dichtmasse soll ich verwenden?
**Antwort**: Sikaflex 291 oder 3M 4200 (demontierbar). NICHT 3M 5200 (permanent — Austausch unmöglich ohne Rumpfbeschädigung). KEIN Silikon (haftet nicht auf Bronze, nicht überstreichbar). KEIN Acryl (nicht wasserfest). Primer auf GFK nicht vergessen (Sika 209D).
**Confidence**: documented

### SV-009: Mein Seeventil tropft leicht — ist das gefährlich?
**Antwort**: JA, jedes Tropfen ist ein Warnsignal. Ein "leichtes Tropfen" bei ruhigem Wasser wird zu einem "starken Tropfen" bei Seegang und Krängung. Ursache identifizieren: Flanschdichtung, O-Ring, Dichtmasse, oder Ventilkörper selbst. Reparatur beim nächsten Haul-Out, Bilgenpumpe kontrollieren.
**Confidence**: documented

### SV-010: Wie viele Seeventile hat ein typisches Boot?
**Antwort**: Abhängig von Bootsgröße und Ausstattung. Typisch: Segelboot 10 m = 5–8 Seeventile, Segelboot 14 m = 7–12, Motoryacht 12 m = 6–10, Motoryacht 18 m = 10–18.
**Confidence**: estimated

### SV-011: Was kostet ein kompletter Seeventil-Austausch?
**Antwort**: Material: 80–350 EUR pro Ventil (abhängig von Hersteller und Größe). Arbeit: 250–500 EUR pro Ventil (inkl. anteilig Haul-Out). Komplett-Erneuerung 6 Ventile an Segelboot 10 m: ca. 2.500–5.000 EUR. Investment in Sicherheit.
**Confidence**: estimated — Werft-Angebote DE 2024/25

### SV-012: BSP oder NPT — welches Gewinde?
**Antwort**: In Europa: BSP (British Standard Pipe) ist Standard. In USA: NPT (National Pipe Thread). NICHT kompatibel! BSP dichtet über O-Ring oder Flachdichtung (kein Teflonband nötig). NPT ist konisch und dichtet über Gewindeverformung (Teflonband nötig). Beim Kauf auf Gewindeart achten.
**Confidence**: documented

### SV-013: Kann ich ein Bronze-Seeventil auf einem Aluminium-Rumpf verwenden?
**Antwort**: NUR mit galvanischer Isolation! Bronze ist deutlich edler als Aluminium (0,50–0,60 V Potentialdifferenz). Ohne Isolation frisst sich das Aluminium um den Borddurchlass auf → katastrophaler Wassereinbruch. Empfehlung: Komposit-Seeventile für Alu-Rümpfe.
**Confidence**: documented

### SV-014: Was ist der Unterschied zwischen Seeventil und Borddurchlass?
**Antwort**: Der Borddurchlass (thru-hull) ist die Durchführung durch den Rumpf. Das Seeventil (seacock) ist das Absperrventil, das auf den Borddurchlass geschraubt wird. Zusammen bilden sie die "Borddurchlass-Armatur". Manche Hersteller (Groco IBV) bieten integrierte Einheiten an.
**Confidence**: documented

### SV-015: Mein Seeventil hat keinen Griff — was tun?
**Antwort**: Ersatzgriff beim Hersteller bestellen (meist 10–35 EUR). Bis dahin: passende Rohrzange griffbereit am Ventil befestigen. Ohne Betätigungsmöglichkeit ist das Ventil im Notfall wertlos. Vierkant-Einsatz (Antrieb) am Ventil notieren und passenden Schlüssel bereitlegen.
**Confidence**: documented

### SV-016: Holzpfropfen — Welches Holz?
**Antwort**: Weiches Holz: Kiefer, Fichte, Okumé, Balsa. KEIN Hartholz (Eiche, Teak) — Hartholz quillt zu langsam, um das Loch schnell abzudichten. Der Pfropfen muss sich unter Wasserdruck ins Loch pressen und durch Quellung abdichten. Konisch zuschneiden, Spitze = Borddurchlass-Innendurchmesser.
**Confidence**: documented

### SV-017: Wie prüft ein Surveyor meine Seeventile?
**Antwort**: Standard-Survey umfasst: 1) Material-Identifikation (Bronze/Messing/Komposit). 2) Funktionsprüfung (öffnen/schließen). 3) Klopftest (Dezinkifizierung). 4) Sichtprüfung (Korrosion, Risse). 5) Schlauchverbindungen (doppelte Schellen?). 6) Backing-Block (fest?). 7) Holzpfropfen (vorhanden?). Kosten Survey: 350–800 EUR.
**Confidence**: documented

### SV-018: Müssen Seeventile beim Winterlager geschlossen werden?
**Antwort**: An Land: Alle Ventile OFFEN lassen (Kondenswasser ablaufen lassen). Im Wasser: Alle Ventile GESCHLOSSEN (bis auf Cockpit-Drains). WICHTIG: Kühlwassersystem mit Frostschutz (Propylenglykol, NICHT Ethylenglykol!) spülen, wenn Frostgefahr besteht. Eis im Ventil kann den Körper sprengen.
**Confidence**: documented

### SV-019: Kann ich ein Seeventil selbst austauschen?
**Antwort**: Technisch ja, wenn man Erfahrung mit GFK-Arbeit hat. ABER: Fehler beim Einbau = SINKEN. Empfehlung: Erstmaliger Austausch durch Fachwerft. Danach, mit Erfahrung und unter Anleitung, ggf. DIY möglich. Immer zu zweit arbeiten. Boot MUSS an Land sein. Anleitung in Abschnitt 12 dieser Datei.
**Confidence**: documented

### SV-020: Wie finde ich heraus, welche Seeventile in meinem Boot verbaut sind?
**Antwort**: 1) Bootsunterlagen / Werft-Dokumentation prüfen. 2) Alle Ventile physisch inspizieren und fotografieren. 3) Herstellerstempel auf Ventilkörper ablesen. 4) Material identifizieren (Farbe, Gewicht, Magnettest — Bronze ist nicht magnetisch). 5) AYDI kann aus Fotos (Pipeline B) Material und Zustand abschätzen.
**Confidence**: documented

### SV-021: Warum ist mein Bronze-Seeventil grün?
**Antwort**: Grüne Patina (Kupfercarbonat) ist eine natürliche Schutzschicht auf Bronze und KEIN Zeichen von Schaden. Im Gegenteil: Patina schützt das darunterliegende Metall. NICHT entfernen! Wenn allerdings Lochfraß unter der Patina sichtbar ist → galvanische Korrosion prüfen.
**Confidence**: documented

### SV-022: Welchen Einfluss hat Landstrom auf meine Seeventile?
**Antwort**: Landstrom kann Streuströme ins Wasser leiten, die galvanische Korrosion massiv beschleunigen. Lösung: Galvanischer Isolator (Victron GI, ca. 85 EUR) im Landstromkabel installieren. ODER: Trenntransformator (400–1.200 EUR, aber teurer und schwerer). In Marinas mit vielen Booten besonders kritisch.
**Confidence**: documented

### SV-023: Seeventil oder Kugelhahn aus dem Baumarkt — geht das?
**Antwort**: NEIN. Baumarkt-Kugelhähne sind typischerweise aus verzinktem Messing (dezinkifizierungsgefährdet), nicht druckgeprüft für marine Anwendung, mit Dichtungen aus nicht-seewasserbeständigem Material. ABYC H-27 und ISO 9093 verlangen marine-zertifizierte Ventile. Einsparung: 30 EUR. Risiko: Boot sinkt.
**Confidence**: documented

### SV-024: Was passiert bei einer Grundberührung mit meinen Seeventilen?
**Antwort**: Grundberührung kann pilzförmige Borddurchlässe abbrechen (→ Fehlerbild FB-SV-09: offenes Loch = SINKEN). Nach JEDER Grundberührung: alle Borddurchlässe von innen und außen inspizieren. Holzpfropfen griffbereit haben. Bilge auf Wassereinbruch prüfen. Bei Unsicherheit: Boot aus dem Wasser nehmen und inspizieren.
**Confidence**: documented

### SV-025: Wie bewertet AYDI meine Seeventile?
**Antwort**: AYDI bewertet jeden einzelnen Borddurchlass/Seeventil auf einer Skala von 0–100 und vergibt eine Gesamtbewertung für das System. Datenquellen: CAD-Daten (Pipeline A), Fotos (Pipeline B), Service-Berichte (Pipeline C). Jede Bewertung trägt eine Confidence-Angabe. Kritische Befunde (Score <30) werden als "SOFORT HANDELN" markiert.
**Confidence**: documented

---

## 17. Glossar (40+ Begriffe)

| Begriff | Englisch | Definition |
|---|---|---|
| Seeventil | Seacock | Absperrventil direkt am Borddurchlass, ermöglicht Verschluss der Rumpföffnung |
| Borddurchlass | Thru-hull fitting / Skin fitting | Durchführung durch den Rumpf für Wasser- oder Abgasleitungen |
| Kugelventil | Ball valve | Ventil mit durchbohrter Kugel, 90°-Vierteldrehung offen↔geschlossen |
| Kegelventil | Tapered plug valve | Traditionelles Ventil mit konischem Küken, nachschleifbar |
| Schieberventil | Gate valve | Ventil mit Schieber, VERBOTEN als Seeventil |
| Klappenventil | Butterfly valve | Ventil mit Drehklappe, nur für große Durchmesser |
| Pilzförmig | Mushroom type | Borddurchlass mit breitem Außenflansch, Standard |
| Flansch-Durchlass | Flanged fitting | Borddurchlass mit beidseitigem Flansch, Heavy-Duty |
| Flush-Mount | Flush mount | Bündig eingebauter Borddurchlass, für Racing/Superyachten |
| Scoop-Einlass | Scoop strainer | Borddurchlass mit Leitfläche für besseren Wassereinlass |
| Backing-Block | Backing plate/block | Lastverteilungsplatte zwischen Seeventil und Rumpflaminat |
| Schlauchtülle | Hose barb | Gezackter Anschluss für Schlauchbefestigung |
| Schlauchschelle | Hose clamp / Jubilee clip | Klemme zur Befestigung des Schlauchs auf der Tülle |
| Dichtmasse | Sealant / Bedding compound | Dichtmaterial zwischen Borddurchlass und Rumpf |
| O-Ring | O-ring | Ringförmige Dichtung zwischen Borddurchlass und Seeventil |
| Flachdichtung | Flat gasket | Flache Dichtung als Alternative zum O-Ring |
| Holzpfropfen | Softwood plug / Emergency bung | Konischer Holzkeil als Notabdichtung bei Borddurchlass-Versagen |
| Bronze | Bronze | Kupfer-Zinn-Legierung, Standard für Seewasser-Armaturen |
| Messing | Brass | Kupfer-Zink-Legierung, GEFÄHRLICH in Seewasser (Dezinkifizierung) |
| Rotguss | Red brass / Gunmetal | Kupfer-Zinn-Zink-Blei-Legierung mit niedrigem Zinkanteil |
| DZR-Messing | Dezincification Resistant Brass | Messing mit Arsen-Inhibitor gegen Dezinkifizierung |
| Dezinkifizierung | Dezincification | Selektive Korrosion, bei der Zink aus der Legierung gelöst wird |
| Galvanische Korrosion | Galvanic corrosion | Elektrochemische Korrosion durch Kontakt verschiedener Metalle |
| Elektrolyse | Electrolysis / Stray current corrosion | Korrosion durch elektrische Streuströme |
| Opferanode | Sacrificial anode | Unedles Metall (Zink, Magnesium), das sich anstelle des Bauteils auflöst |
| Galvanischer Isolator | Galvanic isolator | Elektronisches Bauteil, das Gleichströme im Landstromkabel blockiert |
| ICCP | Impressed Current Cathodic Protection | Aktiver kathodischer Korrosionsschutz mit externem Strom |
| Spaltkorrosion | Crevice corrosion | Korrosion in engen Spalten (Gewinde, unter Dichtungen) |
| Lochfraß | Pitting corrosion | Lokale Korrosion mit tiefen Löchern |
| Erosionskorrosion | Erosion corrosion | Materialabtrag durch Strömung + Korrosion |
| Osmose | Osmosis / Osmotic blistering | Wasseraufnahme durch GFK-Laminat mit Blasenbildung |
| BSP | British Standard Pipe | Rohrgewinde-Standard (zylindrisch, Europa) |
| NPT | National Pipe Thread | Rohrgewinde-Standard (konisch, USA) |
| DN | Diamètre Nominal / Nennweite | Nennweite einer Rohrleitung in mm |
| PTFE | Polytetrafluorethylen | Kunststoff für Ventildichtflächen (Teflon) |
| Marelon | Marelon (Markenname Forespar) | Glasfaserverstärktes Nylon für marine Armaturen |
| GFK | Glasfaserverstärkter Kunststoff / FRP | Faserverbundwerkstoff für Rumpf und Komposit-Ventile |
| Antifouling | Antifouling | Bewuchsschutz-Anstrich für Unterwasserschiff |
| Bewuchs | Biofouling | Biologischer Bewuchs (Seepocken, Muscheln, Algen) |
| Nassauspuff | Wet exhaust | Abgasanlage, bei der Kühlwasser in den Abgasstrom eingespritzt wird |
| Küken | Plug (of a valve) | Konisches Verschlussteil im Kegelventil |
| Haul-Out | Haul-out / Slipping | Herausnehmen des Bootes aus dem Wasser (Kran oder Slip) |
| Survey | Marine survey | Zustandsbegutachtung durch zertifizierten Gutachter |
| Surveyor | Marine surveyor | Zertifizierter Gutachter für Schiffszustand |
| CE-Kennzeichnung | CE marking | Konformitätskennzeichnung nach EU-Recht |
| RCD | Recreational Craft Directive | EU-Richtlinie 2013/53/EU für Sportboote |

(Confidence: documented)

---

## 18. Schnell-Referenz

### 18.1 Entscheidungsmatrix: Welches Seeventil?

```
                    Neubau?
                   /       \
                Ja           Nein (Austausch)
               /               \
        Alu-Rumpf?           Was ist verbaut?
       /         \           /      |       \
     Ja          Nein     Messing  Gate    Bronze/
      |            |         |     Valve   Komposit
  Komposit    GFK/Stahl?   SOFORT  SOFORT  Zustand
  (TruDesign)  /     \    tauschen tauschen prüfen
              GFK   Stahl    |       |      /    \
               |      |   Bronze  Bronze  Gut   Schlecht
           Bronze  Bronze  oder     |      |      |
           oder    C92200  Komposit      Weiter  Austausch
           Komposit                     nutzen   planen
```

### 18.2 Quick-Check: 5-Minuten-Seeventil-Inspektion

| Check | OK | Nicht OK | Aktion |
|---|---|---|---|
| 1. Material identifiziert? | Bronze/Komposit | Messing/Unbekannt | Säure-Test / Austausch |
| 2. Ventil betätigbar? | Öffnet/schließt leicht | Festsitzend | Penetrieröl / Austausch |
| 3. Griff vorhanden? | Ja, fest | Fehlt/lose | Ersatzgriff montieren |
| 4. Kein Tropfen/Sickern? | Trocken | Feucht/Tropfen | Dichtung / Austausch |
| 5. Doppelte Schlauchschellen? | 2× 316L | 1× oder rostig | Nachrüsten |
| 6. Backing-Block fest? | Fest | Lose/wackelt | Neu montieren |
| 7. Holzpfropfen vorhanden? | Ja, am Ventil | Nein | Beschaffen + befestigen |
| 8. Keine sichtbare Korrosion? | Sauber | Lochfraß/Verfärbung | Prüfen / Austausch |

### 18.3 Kosten-Schnellübersicht

| Komponente | Budget | Mittelklasse | Premium |
|---|---|---|---|
| Borddurchlass DN25 | Guidi: 15 EUR | TruDesign: 30 EUR | Groco: 45 EUR |
| Borddurchlass DN38 | Guidi: 35 EUR | TruDesign: 55 EUR | Groco: 85 EUR |
| Kugelventil DN25 | Guidi: 40 EUR | TruDesign: 60 EUR | Groco: 120 EUR |
| Kugelventil DN38 | Guidi: 75 EUR | TruDesign: 95 EUR | Groco: 220 EUR |
| Kegelventil DN38 | — | Perko: 180 EUR | Blakes: 320 EUR |
| Einbau pro Ventil (Werft DE) | — | 250–400 EUR | 400–600 EUR |
| Haul-Out (anteilig) | — | 200–400 EUR | — |
| **Gesamt 1× DN38 Austausch** | **~400 EUR** | **~650 EUR** | **~1.100 EUR** |

(Confidence: estimated — Händlerpreise + Werft-Angebote DE 2024/25)

---

## 19. Notfall-Ressourcen

### 19.1 Sofort-Maßnahmen bei Wassereinbruch durch Seeventil

**SCHRITT 1**: Seeventil SCHLIESSEN (Griff quer = ZU)
**SCHRITT 2**: Wenn Ventil nicht schließbar → HOLZPFROPFEN in Borddurchlass schlagen
**SCHRITT 3**: Bilgenpumpen EIN (alle, manuell + elektrisch)
**SCHRITT 4**: Weitere Seeventile schließen
**SCHRITT 5**: MAYDAY über VHF Kanal 16 wenn nötig
**SCHRITT 6**: Rettungsmittel bereitmachen

### 19.2 Kontakte

| Organisation | Funktion | Kontakt |
|---|---|---|
| DGzRS | Seenotrettung Deutschland | VHF Kanal 16 / Tel: 0421-536870 |
| MRCC | Maritime Rescue Coordination | VHF Kanal 16 |
| BSU | Bundesstelle für Seeunfalluntersuchung | bsu-bund.de |
| MAIB | Marine Accident Investigation Branch (UK) | maib.gov.uk |
| IIMS | International Institute of Marine Surveying | iims.org.uk |

### 19.3 Notfall-Kit Seeventile (empfohlener Bordbestand)

| Gegenstand | Menge | Bemerkung |
|---|---|---|
| Holzpfropfen-Set (sortiert DN13–DN50) | 1 Set (6–8 Stück) | Weichholz, konisch |
| Rohrzange 300 mm | 1 | Für Notbetätigung ohne Griff |
| Schlauchschellen 316L (sortiert) | 10 Stück | Ersatz |
| PTFE-Band | 1 Rolle | Nur für NPT-Gewinde |
| Unterwasser-Epoxid (z.B. Belzona 1111) | 1 Dose | Temporäre Notreparatur |
| Dichtmasse (Sikaflex 291, kleine Tube) | 1 | Notreparatur |
| Kabelbinder (diverse Größen) | 20 Stück | Universell |
| Taschenlampe (wasserdicht) | 1 | Bilge-Inspektion |
| Gummihandschuhe | 2 Paar | Schutz |

(Confidence: documented — RYA Cruising Handbook, Seemannschafts-Literatur)

---

## ANHANG A — Cross-Reference: Borddurchlass → Seeventil → Hersteller

| DN | BSP | NPT | Groco TH | Groco BV | Guidi 1040 | Guidi 2060 | TruDesign TH | TruDesign SV |
|---|---|---|---|---|---|---|---|---|
| 13 | ½" | ½" | TH-500 | — | 1040/½" | 2060/½" | — | — |
| 19 | ¾" | ¾" | TH-750 | BV-750 | 1040/¾" | 2060/¾" | 90400/¾" | 90-¾" |
| 25 | 1" | 1" | TH-1000 | BV-1000 | 1040/1" | 2060/1" | 90400/1" | 90-1" |
| 32 | 1¼" | 1¼" | TH-1250 | BV-1250 | 1040/1¼" | 2060/1¼" | 90400/1¼" | 90-1¼" |
| 38 | 1½" | 1½" | TH-1500 | BV-1500 | 1040/1½" | 2060/1½" | 90400/1½" | 90-1½" |
| 50 | 2" | 2" | TH-2000 | BV-2000 | 1040/2" | 2060/2" | 90400/2" | 90-2" |

(Confidence: documented — Herstellerkataloge)

---

## ANHANG B — Legierungs-Vergleich

| Eigenschaft | C83600 (85-5-5-5) | C84400 (81 Red) | C92200 (Navy G) | C95800 (NiAlBr) | DZR (CW602N) | C85200 (Yellow) |
|---|---|---|---|---|---|---|
| Cu | 85% | 81% | 88% | 81% | 63% | 72% |
| Sn | 5% | 3% | 6% | — | — | 1% |
| Zn | 5% | 7% | 1,5% | — | 34% | 24% |
| Pb | 5% | 9% | 1,5% | — | 2,5% | 3% |
| Andere | — | — | 3% Ni | 9%Al, 4%Ni, 4%Fe | 0,1% As | — |
| Zugfestigkeit (MPa) | 255 | 235 | 275 | 620 | 400 | 310 |
| Dehnung (%) | 25 | 25 | 30 | 15 | 30 | 25 |
| Dez.-Risiko | Sehr gering | Gering | Minimal | Keine | Mittel (inhib.) | HOCH! |
| Seewasser | ✅ JA | ⚠️ Bedingt | ✅ JA Premium | ✅ JA | ⚠️ Bedingt | ❌ NEIN |
| Kosten (rel.) | 100% | 85% | 130% | 200% | 55% | 45% |
| AYDI-Empfehlung | Standard | Akzeptabel | Premium | Spezial | Unter Vorbehalt | VERBOTEN |

(Confidence: documented — ASTM B61, B62, B505, CDA)

---

## ANHANG C — Biegeradien → Durchfluss

### Einfluss von Schlauchleitungsführung auf Durchfluss

| Biegeradius (×DN) | Durchflussverlust | Bewertung |
|---|---|---|
| >5× DN | <5% | ✅ Ideal |
| 3–5× DN | 5–15% | ⚠️ Akzeptabel |
| 2–3× DN | 15–30% | ⚠️ Grenzwertig |
| <2× DN | >30% | ❌ Nicht akzeptabel |
| Knick (0× DN) | Bis 100% | ❌ STRÖMUNGSABRISS |

**AYDI-Empfehlung**: Schlauchführung so gerade wie möglich. Jeder 90°-Bogen ≈ 15% Durchflussverlust. Bei Kühlwassereinlass kritisch (Motorüberhitzung).

(Confidence: calculated — Strömungsmechanik, Rohrleitungs-Handbuch)

---

## ANHANG D — Confidence-Mapping für Seeventile

### Welche Confidence für welche Datenquelle?

| Datenquelle | Confidence | Score-Genauigkeit | Typisches Szenario |
|---|---|---|---|
| CAD-Modell mit DN, Material, Position | measured | ±2 Punkte | Level 2 Profi-Werkzeug |
| Herstellerdatenblatt + Seriennummer | documented | ±3 Punkte | Neubau mit Dokumentation |
| Survey-Bericht eines IIMS-Surveyors | documented | ±5 Punkte | Kaufgutachten |
| Foto: Ventil klar sichtbar, Marke erkennbar | visual_high | ±8 Punkte | Level 1 Schnellanalyse mit gutem Foto |
| Foto: Ventil teilweise sichtbar | visual_medium | ±15 Punkte | Level 1 mit durchschnittlichem Foto |
| Foto: Ventil kaum sichtbar, dunkel | visual_low | ±25 Punkte | Nicht zur Bewertung verwenden |
| Nur Bootstyp + Baujahr bekannt | estimated | ±20 Punkte | Level 1 ohne Foto |
| Branchendurchschnitt nach Bootsklasse | benchmark | ±25 Punkte | Keine bootspezifischen Daten |

(Confidence: documented — AYDI Confidence Framework)

---

## ANHANG E — Bordausstattung: Standard-Seeventil-Konfiguration nach Bootstyp

### E.1 Segelboot 8–10 m (z.B. Bavaria 34, Jeanneau Sun Odyssey 319)

| Nr. | Anwendung | DN | Material (OEM) | Hersteller (OEM) |
|---|---|---|---|---|
| 1 | Kühlwasser Motor | DN25 | DZR-Messing | Guidi 2062 |
| 2 | WC Einlass | DN19 | DZR-Messing | Guidi 2062 |
| 3 | WC Auslass | DN25 | DZR-Messing | Guidi 2062 |
| 4 | Waschbecken Pantry | DN19 | Komposit | TruDesign 90 |
| 5 | Waschbecken Bad | DN19 | Komposit | TruDesign 90 |
| 6 | Cockpit-Drains (2×) | DN25 | Komposit | TruDesign 90 |
| **Gesamt** | **6–7 Stück** | | | |

**AYDI-Hinweis**: Bavaria und Jeanneau verwenden ab Werk oft DZR-Messing (Guidi 2062). Bei Gebrauchtbooten >12 Jahre unbedingt auf Dezinkifizierung prüfen!

### E.2 Segelboot 12–14 m (z.B. Hallberg-Rassy 40, Oyster 435)

| Nr. | Anwendung | DN | Material (OEM) | Hersteller (OEM) |
|---|---|---|---|---|
| 1 | Kühlwasser Motor | DN32 | Bronze C83600 | Guidi 2060 |
| 2 | Nassauspuff | DN38 | Bronze C83600 | Guidi 2060 |
| 3 | WC Vorschiff Einlass | DN19 | Bronze C83600 | Blakes BB |
| 4 | WC Vorschiff Auslass | DN25 | Bronze C83600 | Blakes BB |
| 5 | WC Achtern Einlass | DN19 | Bronze C83600 | Blakes BB |
| 6 | WC Achtern Auslass | DN25 | Bronze C83600 | Blakes BB |
| 7 | Waschbecken Pantry | DN19 | Bronze C83600 | Guidi 2060 |
| 8 | Waschbecken Bad Vorschiff | DN19 | Komposit | TruDesign 90 |
| 9 | Waschbecken Bad Achtern | DN19 | Komposit | TruDesign 90 |
| 10 | Cockpit-Drains (2×) | DN32 | Komposit | TruDesign 90 |
| **Gesamt** | **10–12 Stück** | | | |

### E.3 Motoryacht 10–14 m (z.B. Bavaria Virtess 420, Princess F45)

| Nr. | Anwendung | DN | Material (OEM) | Hersteller (OEM) |
|---|---|---|---|---|
| 1 | Kühlwasser Motor Stb. | DN38 | Bronze C83600 | Guidi 2060 |
| 2 | Kühlwasser Motor Bb. | DN38 | Bronze C83600 | Guidi 2060 |
| 3 | Generator Kühlwasser | DN25 | Bronze C83600 | Guidi 2060 |
| 4 | Nassauspuff Stb. | DN38 | Bronze C83600 | Guidi 2060 |
| 5 | Nassauspuff Bb. | DN38 | Bronze C83600 | Guidi 2060 |
| 6 | Klimaanlage Einlass | DN25 | Bronze C83600 | Guidi 2060 |
| 7 | Klimaanlage Auslass | DN25 | Bronze C83600 | Guidi 2060 |
| 8 | WC Einlass | DN19 | Komposit | TruDesign 90 |
| 9 | WC Auslass | DN25 | Komposit | TruDesign 90 |
| 10 | Waschbecken (3×) | DN19 | Komposit | TruDesign 90 |
| 11 | Bilge Auslass | DN32 | Bronze C83600 | Guidi 2060 |
| 12 | Cockpit-Drains (2×) | DN32 | Komposit | TruDesign 90 |
| **Gesamt** | **12–16 Stück** | | | |

### E.4 Superyacht 18+ m (z.B. Oyster 565, Swan 65, Azimut 55)

| Nr. | Anwendung | DN | Material (OEM) |
|---|---|---|---|
| 1–2 | Kühlwasser Hauptmaschinen (2×) | DN50 | Bronze C92200 |
| 3 | Generator Kühlwasser | DN32 | Bronze C92200 |
| 4–5 | Nassauspuff (2×) | DN50 | Bronze C92200 |
| 6–7 | Klimaanlage (2× Einlass/Auslass) | DN32 | Bronze C83600 |
| 8–9 | Hydraulik (Bugstrahlruder etc.) | DN25 | Bronze C83600 |
| 10–13 | WC (3–4× Einlass/Auslass) | DN25 | Bronze C83600 |
| 14–17 | Waschbecken (4×) | DN19 | Bronze oder Komposit |
| 18–19 | Bilge (2× Auslass) | DN38 | Bronze C83600 |
| 20 | Wassermacher Einlass | DN25 | Komposit |
| 21 | Deckwaschanlage | DN25 | Bronze C83600 |
| 22 | Feuerlöschanlage Seewasser | DN50 | Bronze C92200 |
| 23–24 | Cockpit-Drains (2×) | DN38 | Bronze C83600 |
| **Gesamt** | **18–25+ Stück** | | |

(Confidence: estimated — OEM-Stücklisten, Werft-Erfahrung)

---

## ANHANG F — Fallstudien

### F.1 Fallstudie: Bavaria 38 (2008) — Dezinkifizierung aller Seeventile

**Boot**: Bavaria 38 Cruiser, Baujahr 2008, Liegeplatz Kroatien (Seewasser, warm).
**Befund**: Alle 7 Seeventile aus DZR-Messing (Guidi 2062). Nach 14 Jahren Salzwasser: 3 Ventile dezinkifiziert (Säure-Test positiv), 2 festsitzend, 2 noch funktionstüchtig.
**Konsequenz**: Versicherung verlangte Austausch aller 7 Ventile innerhalb 90 Tage.
**Lösung**: Austausch gegen TruDesign Komposit (7× DN19–DN32). Kosten: 2.800 EUR (Material + Werft).
**AYDI-Score vorher**: System 28/100 (KRITISCH). **AYDI-Score nachher**: System 92/100 (EXZELLENT).
**Lehre**: DZR-Messing in warmem Mittelmeer-Wasser: Lebensdauer nur 10–15 Jahre.

### F.2 Fallstudie: Hallberg-Rassy 352 (1988) — Gate-Ventil versagt beim Segeln

**Boot**: Hallberg-Rassy 352, Baujahr 1988, auf See vor Portugal.
**Befund**: Voreigner hatte Kühlwasser-Seeventil gegen Baumarkt-Gate-Ventil (Messing) ersetzt.
**Ereignis**: Gate-Ventil konnte bei Motorüberhitzung nicht geschlossen werden (korrodiert fest). Kühlwasserschlauch platzte, Maschinenraum flutete.
**Konsequenz**: 4 Stunden Pumpen. Nothafen angelaufen. Maschinenraum 30 cm Wasser.
**Lösung**: Austausch gegen Groco BV-1250 (Bronze Kugelventil). Kosten: 650 EUR.
**Lehre**: NIEMALS Gate-Ventile als Seeventile verwenden. Immer alle Ventile bei Bootskauf prüfen.

### F.3 Fallstudie: Jeanneau Sun Odyssey 379 (2013) — Komposit-Bruch durch Frost

**Boot**: Jeanneau Sun Odyssey 379, Baujahr 2013, Winterlager Schweden IM Wasser.
**Befund**: TruDesign Komposit-Seeventil (WC-Einlass) durch Eisbildung im Ventilkörper gerissen.
**Ursache**: Ventil im Winter geschlossen, Restwasser im Ventilkörper gefroren, Eis hat Ventil gesprengt.
**Konsequenz**: Wassereinbruch beim Einwassern im Frühling. Boot gesunken im Hafen (geborgen).
**Lösung**: Boot geborgen, alle Seeventile erneuert (Komposit + Bronze gemischt), Frostschutz-Prozedur.
**Lehre**: Bei Winterlager im Wasser: Frostschutz-Maßnahmen! Alle Ventile OFFEN lassen oder Frostschutz durchspülen.

### F.4 Fallstudie: Dufour 45e (2016) — Galvanische Korrosion durch Landstrom

**Boot**: Dufour 45e Performance, Baujahr 2016, Marina Barcelona.
**Befund**: 3 Bronze-Seeventile (Guidi 2060) mit starkem Lochfraß nach nur 5 Jahren.
**Ursache**: Fehlender galvanischer Isolator im Landstromkabel. Benachbartes Stahlboot ohne Anoden verursachte Streuströme.
**Konsequenz**: 2 Ventile durchkorrodiert, 1 tropfte. Versicherung deckte Schaden NICHT (fehlender Isolator = grobe Fahrlässigkeit).
**Lösung**: 3 neue Bronze-Seeventile + Victron Galvanic Isolator. Kosten: 1.400 EUR.
**Lehre**: Galvanischer Isolator ist PFLICHT in jeder Marina mit Landstrom. Kosten: 85 EUR vs. tausende EUR Schaden.

### F.5 Fallstudie: Contest 42 (1995) — Blakes Kegelventile nach 28 Jahren

**Boot**: Contest 42, Baujahr 1995, Liegeplatz Nordsee (Niederlande).
**Befund**: Alle 8 Seeventile Blakes Bronze Kegelventile (C83600). Nach 28 Jahren: alle voll funktionsfähig.
**Wartung**: Eigner hat Küken jährlich gefettet (Wasserpumpenfett), 2× jährlich betätigt.
**Zustand**: Leichte Erosion an 2 Küken, nachgeschliffen. Score: 72/100.
**Lehre**: Bronze-Kegelventile halten bei guter Pflege 30+ Jahre. Jährliches Fetten ist entscheidend.

### F.6 Fallstudie: Bayliner 3055 (2001) — Yellow Brass Borddurchlass bricht bei Grundberührung

**Boot**: Bayliner 3055 Ciera, Baujahr 2001, Chesapeake Bay, USA.
**Befund**: Pilzförmiger Borddurchlass (Yellow Brass, C85200) brach bei leichter Grundberührung ab.
**Ursache**: Dezinkifizierung hatte Wandstärke auf <0,5 mm reduziert. Minimale mechanische Belastung reichte für Bruch.
**Konsequenz**: Offenes 38-mm-Loch im Rumpf. Boot sank innerhalb 8 Minuten. Keine Verletzten (Flachwasser).
**Lösung**: Boot geborgen. Alle Borddurchlässe gegen Groco Bronze (C83600) ersetzt.
**Lehre**: Yellow Brass DARF NIEMALS für Borddurchlässe oder Seeventile verwendet werden!

### F.7 Fallstudie: Swan 48 (2019) — Vorbildliche Installation

**Boot**: Nautor's Swan 48, Baujahr 2019.
**Befund**: 12 Seeventile, alle Groco BV (Bronze C83600), integrierte Borddurchlässe (IBV), G10 Backing-Blocks, Sikaflex 291, doppelte ABA-Schlauchschellen (316L), Holzpfropfen an jedem Ventil.
**Score**: System 96/100 (EXZELLENT). Vorbildliche Installation.
**Lehre**: Premium-Hersteller + korrekte Installation + Dokumentation = maximale Sicherheit.

### F.8 Fallstudie: Azimut 55 (2012) — Elektrolyse zerstört 5 Seeventile in 2 Jahren

**Boot**: Azimut 55, Baujahr 2012, Marina Mallorca.
**Befund**: 5 von 16 Bronze-Seeventilen mit massivem Lochfraß/Materialverlust.
**Ursache**: Defekter Wechselrichter leitete Gleichstrom über Erdung ins Wasser. Massive Elektrolyse.
**Konsequenz**: 2 Ventile durchkorrodiert (Wassereinbruch bei Seegang). Nothafen. Schaden: 18.000 EUR.
**Lösung**: Wechselrichter repariert, Erdung geprüft, 5 Seeventile erneuert, ICCP-System installiert.
**Lehre**: Elektrische Fehler können Bronze in Monaten zerstören. Regelmäßige Anodenprüfung + Erdungsmessung.

(Confidence: documented + estimated — Survey-Berichte, Fachzeitschriften, Forum-Berichte)

---

## ANHANG G — Experten & Literatur

### G.1 Anerkannte Experten

| Name | Spezialisierung | Land | Referenz |
|---|---|---|---|
| Nigel Calder | Marine-Technik, Autor | UK/USA | "Boatowner's Mechanical and Electrical Manual" |
| Steve D'Antonio | Marine Survey, Kolumnist | USA | marineconsultant.com, Professional BoatBuilder |
| Don Casey | Bootsinstandhaltung, Autor | USA | "This Old Boat", "Sailboat Hull & Deck Repair" |
| László Domonkos | Korrosionsschutz Marine | HU | NACE International Fellow |
| John C. Payne | Marine-Elektrik | AU | "Marine Electrical and Electronics Bible" |
| Prof. Roger Butlin | Marine-Metallurgie | UK | University of Southampton |

### G.2 Wichtige Publikationen

| Titel | Autor | Relevanz |
|---|---|---|
| Boatowner's Mechanical and Electrical Manual | Nigel Calder | Standardwerk Kapitel "Plumbing" |
| Surveying Fiberglass Sailboats | Henry C. Mustin | Survey-Methoden für Borddurchlässe |
| Marine Corrosion | Kenneth A. Chandler | Galvanische Korrosion Grundlagen |
| The Fiberglass Boat Repair Manual | Allan H. Vaitses | GFK-Reparatur an Borddurchlässen |
| Professional BoatBuilder Magazine | diverse | Regelmäßige Artikel zu Seeventilen |
| Practical Sailor | diverse | Vergleichstests Seeventile |

(Confidence: documented)

---

## ANHANG H — Risk Matrix

### Risikobewertung nach Fehlertyp × Konsequenz

| Fehlertyp | Wahrscheinlichkeit | Konsequenz | Risiko-Level | AYDI-Aktion |
|---|---|---|---|---|
| Dezinkifizierung (Messing) | HOCH (bei Messing) | KATASTROPHAL (Sinken) | KRITISCH | Score ≤10, Sofort-Austausch |
| Gate-Ventil versagt | HOCH | KATASTROPHAL | KRITISCH | Score 15, Sofort-Austausch |
| Festsitzendes Ventil | MITTEL | HOCH (Notfall-unfähig) | HOCH | Score ≤25, Austausch planen |
| Galvanische Korrosion | MITTEL | HOCH–KATASTROPHAL | HOCH | Score 15–30, Isolator + Austausch |
| Schlauch abgerutscht | NIEDRIG–MITTEL | KATASTROPHAL | HOCH | Score 20–40, Doppelschellen |
| Komposit-Bruch | NIEDRIG | KATASTROPHAL | MITTEL–HOCH | Score 15–35, Austausch |
| Dichtmasse versagt | MITTEL | MITTEL (langsamer Eintritt) | MITTEL | Score 30–50, Neuabdichtung |
| Tropfender Flansch | MITTEL | NIEDRIG–MITTEL | MITTEL | Score 40–55, Dichtung erneuern |
| Bewuchsblockade | HOCH (warm) | NIEDRIG (Motor-Problem) | NIEDRIG–MITTEL | Score 45–60, Reinigung |
| Fehlender Griff | NIEDRIG | MITTEL (Notfall-eingeschränkt) | NIEDRIG–MITTEL | Score 25–35, Ersatzgriff |
| Fehlender Holzpfropfen | MITTEL | — (nur Backup fehlt) | NIEDRIG | Score -5, Pfropfen beschaffen |

(Confidence: documented — AYDI Risk Framework)

---

## ANHANG I — Audit/Compliance Checkliste

### Seeventil-Audit nach ISO 9093 / ABYC H-27

| Nr. | Prüfpunkt | ISO 9093 | ABYC H-27 | Ergebnis |
|---|---|---|---|---|
| 1 | Material identifiziert und dokumentiert? | ✅ Pflicht | ✅ Pflicht | ☐ Ja ☐ Nein |
| 2 | Material = Bronze (C83600/C92200) oder ISO 9093-2 Komposit? | ✅ Pflicht | ✅ Pflicht | ☐ Ja ☐ Nein |
| 3 | KEIN Messing (Yellow Brass)? | ✅ Pflicht | ✅ Pflicht | ☐ Ja ☐ Nein |
| 4 | KEIN Gate-Ventil? | — | ✅ Pflicht | ☐ Ja ☐ Nein |
| 5 | Ventil betätigbar (öffnet/schließt)? | ✅ Pflicht | ✅ Pflicht | ☐ Ja ☐ Nein |
| 6 | Griff vorhanden und fest? | ✅ Pflicht | ✅ Pflicht | ☐ Ja ☐ Nein |
| 7 | Kein sichtbarer Wasseraustritt? | ✅ Pflicht | ✅ Pflicht | ☐ Ja ☐ Nein |
| 8 | Doppelte Schlauchschellen unter WL? | — | ✅ Pflicht | ☐ Ja ☐ Nein |
| 9 | Schlauchschellen 316L Edelstahl? | — | ✅ Empfohlen | ☐ Ja ☐ Nein |
| 10 | Backing-Block vorhanden (GFK-Rumpf)? | ✅ Empfohlen | ✅ Pflicht | ☐ Ja ☐ Nein |
| 11 | Backing-Block fest? | ✅ Empfohlen | ✅ Pflicht | ☐ Ja ☐ Nein |
| 12 | Dichtmasse intakt? | ✅ Pflicht | ✅ Pflicht | ☐ Ja ☐ Nein |
| 13 | Holzpfropfen vorhanden? | — | ✅ Pflicht | ☐ Ja ☐ Nein |
| 14 | Dezinkifizierungs-Test (bei Cu-Legierung >10 Jahre)? | ✅ Empfohlen | ✅ Empfohlen | ☐ Ja ☐ Nein |
| 15 | Keine sichtbare galvanische Korrosion? | ✅ Pflicht | ✅ Pflicht | ☐ Ja ☐ Nein |
| 16 | Galvanischer Isolator vorhanden (bei Landstrom)? | — | ✅ Empfohlen | ☐ Ja ☐ Nein |
| 17 | Alle Ventile dokumentiert (Typ, Größe, Position)? | ✅ Empfohlen | ✅ Empfohlen | ☐ Ja ☐ Nein |

(Confidence: documented — ISO 9093:2020, ABYC H-27:2021)

---

## ANHANG J — Material-Daten

### J.1 Physikalische Eigenschaften

| Eigenschaft | C83600 | C92200 | DZR CW602N | GFK (TruDesign) | Marelon |
|---|---|---|---|---|---|
| Dichte (g/cm³) | 8,83 | 8,62 | 8,44 | 1,85 | 1,65 |
| Zugfestigkeit (MPa) | 255 | 275 | 400 | 155 | 130 |
| Streckgrenze (MPa) | 117 | 124 | 170 | 95 | 80 |
| Dehnung (%) | 25 | 30 | 30 | 3 | 5 |
| E-Modul (GPa) | 100 | 105 | 96 | 12 | 9 |
| Wärmeleitfähigkeit (W/mK) | 72 | 49 | 123 | 0,35 | 0,25 |
| Wärmeausdehnung (µm/mK) | 18,0 | 17,5 | 20,5 | 25 | 30 |
| Max. Einsatztemp. (°C) | 250+ | 250+ | 250+ | 93 | 82 |
| Min. Einsatztemp. (°C) | -200 | -200 | -200 | -30 | -30 |
| Schmelzpunkt (°C) | 1.000 | 1.010 | 900 | — (zersetzt) | — (schmilzt ~260) |

### J.2 Korrosionsbeständigkeit in verschiedenen Medien

| Medium | C83600 | C92200 | DZR | Komposit |
|---|---|---|---|---|
| Seewasser (15°C) | ✅ Exzellent | ✅ Exzellent | ⚠️ Gut (begrenzt) | ✅ Exzellent |
| Seewasser (25°C) | ✅ Sehr gut | ✅ Exzellent | ⚠️ Mäßig | ✅ Exzellent |
| Brackwasser | ✅ Exzellent | ✅ Exzellent | ✅ Gut | ✅ Exzellent |
| Süßwasser | ✅ Exzellent | ✅ Exzellent | ✅ Sehr gut | ✅ Exzellent |
| Diesel/Kraftstoff | ✅ Gut | ✅ Gut | ✅ Gut | ⚠️ Mäßig |
| Abwasser (WC) | ✅ Gut | ✅ Gut | ⚠️ Mäßig | ✅ Gut |
| Abgaskondensat (sauer) | ⚠️ Mäßig | ✅ Gut | ❌ Schlecht | ⚠️ Mäßig |

(Confidence: documented — CDA, NACE, Material-Datenblätter)

---

## ANHANG K — Prüfverfahren

### K.1 Salpetersäure-Spot-Test (Dezinkifizierung)

| Schritt | Beschreibung |
|---|---|
| 1 | Schutzbrille + Handschuhe anziehen |
| 2 | Kleine Stelle am Ventilkörper mit Schleifpapier (120er) blank schleifen |
| 3 | 1–2 Tropfen 10% Salpetersäure (HNO₃) auf blanke Stelle geben |
| 4 | 30 Sekunden einwirken lassen |
| 5 | Mit Wasser abspülen |
| 6 | **Ergebnis grünlich**: GESUND — Bronze/Messing intakt |
| 7 | **Ergebnis rötlich-kupfern**: DEZINKIFIZIERT — Zink bereits ausgelöst! |
| 8 | Bei positivem Befund: SOFORTIGER Austausch |

**Bezugsquelle HNO₃ 10%**: Apotheke (ca. 5 EUR für 100 ml, reicht für 50+ Tests).

### K.2 Druckprüfung (Dichtheitsprüfung)

| Schritt | Beschreibung |
|---|---|
| 1 | Seeventil ausbauen oder alle Anschlüsse verschließen |
| 2 | Druckprüfpumpe anschließen |
| 3 | Langsam auf 2× Betriebsdruck (mind. 2 bar) aufpumpen |
| 4 | 5 Minuten halten |
| 5 | Druckabfall <0,1 bar: BESTANDEN |
| 6 | Druckabfall >0,1 bar: UNDICHT — Ursache suchen |

### K.3 Klopftest

| Schritt | Beschreibung |
|---|---|
| 1 | Ventilkörper mit Schraubendreher-Griff leicht beklopfen |
| 2 | **Heller, metallischer Klang**: GESUND |
| 3 | **Dumpfer, dröhnender Klang**: Verdacht auf Dezinkifizierung oder Lunker |
| 4 | Vergleich mit bekannt gesundem Ventil (Referenz) |

### K.4 Wandstärken-Messung (Ultraschall)

| Gerät | Hersteller | Messbereich | Preis |
|---|---|---|---|
| DeFelsko PosiTector UTG | DeFelsko | 0,50–500 mm (±0,01 mm) | ca. 1.200 EUR |
| Elcometer 500 | Elcometer | 0,63–500 mm | ca. 800 EUR |
| NDT Systems TG110 | NDT Systems | 1,00–200 mm | ca. 600 EUR |

**Mindest-Wandstärke nach ISO 9093-1:**

| DN | Mindest-Wandstärke (neu) | Kritisch (Austausch) |
|---|---|---|
| DN19 | 2,5 mm | <1,5 mm |
| DN25 | 3,0 mm | <2,0 mm |
| DN32 | 3,5 mm | <2,5 mm |
| DN38 | 4,0 mm | <3,0 mm |
| DN50 | 5,0 mm | <3,5 mm |

(Confidence: documented — ISO 9093, NDT-Prüfgeräte-Hersteller)

---

## ANHANG L — Top 15 Fehler bei Seeventil-Installation und -Wartung

| Nr. | Fehler | Konsequenz | Vermeidung |
|---|---|---|---|
| 1 | Messing statt Bronze verwendet | Dezinkifizierung → SINKEN | Nur C83600/C92200 oder Komposit |
| 2 | Gate-Ventil als Seeventil | Versagt im Notfall → SINKEN | Nur Kugel- oder Kegelventile |
| 3 | Nur eine Schlauchschelle unter WL | Schlauch rutscht ab → SINKEN | IMMER doppelte Schlauchschellen |
| 4 | Kein Backing-Block bei GFK-Rumpf | Borddurchlass drückt durch → SINKEN | Backing-Block PFLICHT |
| 5 | Silikon als Dichtmasse | Haftet nicht auf Bronze, versagt | PU-Dichtstoff (Sikaflex/3M) |
| 6 | GFK-Schnittkante nicht versiegelt | Osmose im Laminat | Epoxid auf Schnittkante |
| 7 | Ventil nie betätigt | Festsitzen → Notfall-unfähig | 2× jährlich durchbewegen |
| 8 | Kein Holzpfropfen an Bord | Keine Notabdichtung möglich | Set kaufen (10–20 EUR) |
| 9 | 3M 5200 statt 4200 | Ventil nie wieder demontierbar | 4200 oder Sikaflex 291 verwenden |
| 10 | PTFE-Band auf BSP-Gewinde | Falsche Dichtmethode | PTFE nur bei NPT! BSP: O-Ring |
| 11 | Bronze auf Alu-Rumpf ohne Isolation | Aluminium korrodiert weg | Komposit oder galvanische Isolation |
| 12 | Kein Galvanischer Isolator | Elektrolyse durch Landstrom | Isolator installieren (85 EUR) |
| 13 | Komposit-Ventil am Auspuff | Schmilzt/verformt bei Hitze | Bronze am Auspuff PFLICHT |
| 14 | Schlauchschellen aus verzinktem Stahl | Rosten in Tagen | NUR 316L Edelstahl |
| 15 | Winterlager im Wasser ohne Frostschutz | Eis sprengt Ventilkörper | Frostschutz durchspülen |

(Confidence: documented — Surveyor-Erfahrung, Schadensfälle)

---

## ANHANG M — Zusammenfassung

### Die 10 goldenen Regeln für Seeventile

1. **NUR Bronze (C83600, C92200) oder zertifiziertes Komposit** — kein Messing, kein Gate-Ventil, kein Baumarkt
2. **Jedes Seeventil regelmäßig betätigen** — mindestens 2× pro Saison
3. **Doppelte Schlauchschellen (316L) unter der Wasserlinie** — keine Ausnahme
4. **Backing-Block bei GFK-Rümpfen** — Pflicht, nicht optional
5. **Holzpfropfen an jedem Borddurchlass** — Weichholz, konisch, griffbereit
6. **Galvanischer Isolator bei Landstrom** — 85 EUR vs. Tausende EUR Schaden
7. **Jährliche Inspektion** — Funktion, Korrosion, Schlauchverbindungen prüfen
8. **GFK-Schnittkante mit Epoxid versiegeln** — verhindert osmotische Blasenbildung
9. **Materialien NICHT mischen** — galvanische Kompatibilität beachten
10. **Im Zweifel: AUSTAUSCHEN** — ein neues Seeventil kostet 50–300 EUR, ein Boot 50.000–500.000 EUR

### Kostenvergleich: Prävention vs. Schaden

| Maßnahme | Kosten | Vermiedener Schaden |
|---|---|---|
| 1 Seeventil austauschen | 150–500 EUR | Boot sinkt (50.000+ EUR) |
| Holzpfropfen-Set | 15 EUR | Notabdichtung möglich |
| Galvanischer Isolator | 85 EUR | Korrosionsschaden (2.000–20.000 EUR) |
| Jährliche Inspektion (Selbst) | 0 EUR (1 Stunde Zeit) | Früherkennung aller Probleme |
| Survey alle 5 Jahre | 400–800 EUR | Versteckte Mängel erkennen |
| Komplett-Erneuerung (6 Ventile) | 2.500–5.000 EUR | 15–20 Jahre Sicherheit |

(Confidence: documented — AYDI-Bewertungsframework)

### AYDI-Scoring-Zusammenfassung für Seeventile

| Befund | Score | Dringlichkeit | Anzeige |
|---|---|---|---|
| Alle Ventile Bronze/Komposit, funktionstüchtig, doppelte Schellen | 90–100 | — | Grünes Badge |
| Leichte Patina, alle funktionstüchtig, 1× Schelle fehlt | 70–89 | monitoring | Grünes Badge |
| DZR-Messing >10 Jahre, oder festsitzendes Ventil | 50–69 | nächstes_haul_out | Gelbes Badge |
| Tropfendes Ventil, loser Backing-Block, korrodierte Tülle | 30–49 | innerhalb_30_tage | Oranges Badge |
| Dezinkifizierung, Gate-Ventil, Bruch, offenes Leck | 0–29 | sofort | Rotes Badge — KRITISCH |

### Wartungsplan nach Bootsalter

| Bootsalter | Aktion | Intervall | Geschätzte Kosten |
|---|---|---|---|
| 0–5 Jahre | Sichtkontrolle, Ventile betätigen | Jährlich | 0 EUR (Eigenleistung) |
| 5–10 Jahre | + Schlauchschellen prüfen/nachziehen | Jährlich | 0–50 EUR |
| 10–15 Jahre | + Salpetersäure-Test bei Cu-Legierungen | Alle 3 Jahre | 5 EUR |
| 15–20 Jahre | + Dichtmasse erneuern (älteste Ventile zuerst) | Haul-Out | 200–400 EUR |
| 20–25 Jahre | + PTFE-Sitze erneuern (Kugelventile) | Nach Bedarf | 15–45 EUR/Ventil |
| 25–30 Jahre | Austausch der ältesten Ventile planen | Haul-Out | 800–2.000 EUR |
| 30+ Jahre | Komplett-Erneuerung empfohlen (bei Bronze) | Einmalig | 2.500–5.000 EUR |
| 15+ Jahre | Komplett-Erneuerung empfohlen (bei Komposit) | Einmalig | 1.500–3.500 EUR |

### AYDI-Pipeline-Integration

**Pipeline A (Strukturiert — CAD/Datenbank):**
- Liest Position, DN, Material, Hersteller aus CAD-Modell
- Berechnet Durchflussraten und Dimensionierung
- Prüft Compliance gegen ISO 9093 / ABYC H-27
- Confidence: measured

**Pipeline B (Visuell — Fotos):**
- Identifiziert Ventiltyp (Kugel/Kegel/Gate) aus Fotos
- Erkennt Materialtyp (Bronze gold-rötlich, Komposit weiß/schwarz, Messing goldgelb)
- Bewertet Zustand: Korrosion, Risse, Bewuchs, fehlender Griff
- Erkennt dezinkifizierte Oberflächen (rosa Verfärbung)
- Prüft: Doppelte Schlauchschellen? Holzpfropfen sichtbar?
- Confidence: visual_high / visual_medium / visual_low

**Pipeline C (Text — Service-Berichte):**
- Extrahiert: "Seeventil getauscht", "Borddurchlass erneuert", "Dezinkifizierung festgestellt"
- Erstellt Wartungshistorie pro Ventil
- Erkennt Muster: "WC-Ventil alle 3 Jahre defekt" → Systemisches Problem
- Confidence: documented

**Score Fusion (Seeventile):**
- Structured weight: 0.85 (Materialanalyse dominant)
- Visual weight: 0.15 (Zustandsbeurteilung visuell)
- Hinweis: Bei Seeventilen dominiert die strukturelle Analyse, da Material und Typ entscheidend sind. Visuelle Analyse ergänzt für Zustandsbewertung.

### Typische AYDI-Bewertungsergebnisse

**Beispiel 1: Bavaria 40 Cruiser, Baujahr 2010, Mittelmeer**
```
Seeventil-System Bewertung:
  Gesamtscore: 42/100 (MANGELHAFT)
  Confidence: visual_medium + estimated

  Befunde:
  - 7× Seeventile identifiziert
  - 5× DZR-Messing (Guidi 2062) — Alter 14 Jahre
  - 2× Komposit (TruDesign) — Zustand gut
  - Säure-Test empfohlen für alle DZR-Ventile
  - 3× nur einfache Schlauchschelle

  Kritisch:
  - DZR-Messing nach 14 Jahren in warmem Seewasser: Dezinkifizierungsrisiko HOCH
  - Fehlende doppelte Schlauchschellen: ABYC H-27 Verstoß

  Empfehlung:
  - Alle 5 DZR-Ventile gegen Bronze C83600 oder Komposit austauschen
  - Doppelte Schlauchschellen nachrüsten (alle Ventile unter WL)
  - Holzpfropfen beschaffen und an Ventilen befestigen
  - Geschätzte Kosten: 2.200–3.500 EUR

  Dringlichkeit: innerhalb_30_tage
```

**Beispiel 2: Hallberg-Rassy 43, Baujahr 2018, Ostsee**
```
Seeventil-System Bewertung:
  Gesamtscore: 91/100 (EXZELLENT)
  Confidence: measured + visual_high

  Befunde:
  - 10× Seeventile identifiziert
  - 8× Bronze C83600 (Blakes BB Kugelventil)
  - 2× Komposit (TruDesign)
  - Alle betätigbar, kein Tropfen
  - Doppelte Schlauchschellen (ABA 316L) überall
  - Backing-Blocks G10, alle fest
  - Holzpfropfen an allen Ventilen

  Empfehlung:
  - Weiter so! Jährliche Betätigung beibehalten.
  - Nächste Inspektion in 12 Monaten.

  Dringlichkeit: monitoring
```

**Beispiel 3: Bayliner 285, Baujahr 2004, US-Ostküste**
```
Seeventil-System Bewertung:
  Gesamtscore: 18/100 (KRITISCH!)
  Confidence: visual_high

  Befunde:
  - 6× Seeventile identifiziert
  - 2× Gate-Ventil (VERBOTEN!) — Positionen: Motor Kühlwasser, Bilge
  - 3× Yellow Brass (C85200) — AKUTE SINKGEFAHR
  - 1× Bronze C83600 (einziges akzeptables Ventil)
  - Keine Holzpfropfen an Bord
  - Einfache Schlauchschellen (teilweise rostig)

  KRITISCH:
  - 2× Gate-Ventile = SOFORT austauschen (ABYC H-27 Verstoß)
  - 3× Yellow Brass = AKUTE Dezinkifizierungsgefahr (22 Jahre Seewasser!)
  - Boot NICHT einwassern bis Austausch erfolgt!

  Empfehlung:
  - ALLE 5 defizitären Ventile SOFORT gegen Bronze oder Komposit austauschen
  - Doppelte Schlauchschellen (316L) an allen Verbindungen
  - Holzpfropfen-Set beschaffen
  - Geschätzte Kosten: 1.800–3.200 EUR

  Dringlichkeit: sofort
```

---

## ANHANG N — Spezialanwendungen

### N.1 Seeventile für Stahl-Rümpfe

| Aspekt | Empfehlung |
|---|---|
| Borddurchlass | Stahl-Stutzen eingeschweißt (kein Gewinde-Durchlass) |
| Seeventil | Bronze-Kugelventil auf Stahl-Flansch geschraubt |
| Isolation | Isolier-Flansch oder Isolierplatte zwischen Stahl und Bronze |
| Opferanoden | Zinkanoden am Rumpf (höher als bei GFK) |
| Risiko | Stahl korrodiert schneller als Bronze → Anoden prüfen |

### N.2 Seeventile für Aluminium-Rümpfe

| Aspekt | Empfehlung |
|---|---|
| Borddurchlass | Aluminium-Stutzen eingeschweißt ODER Komposit |
| Seeventil | NUR Komposit (TruDesign/Marelon) — KEIN Bronze! |
| Warum kein Bronze? | 0,50+ V Potentialdifferenz → Aluminium löst sich auf |
| Ausnahme | Bronze NUR mit professioneller galvanischer Isolation + ICCP |
| AYDI-Score | Bronze auf Alu ohne Isolation = Score 10 (KRITISCH) |

### N.3 Seeventile für Holz-Rümpfe

| Aspekt | Empfehlung |
|---|---|
| Borddurchlass | Bronze-Skin-Fitting durch Planke + Kiel/Wrange |
| Backing | Massive Holz-Backing-Platte (Eiche, mindestens 25 mm) |
| Dichtmasse | Traditionell: Bleiwolle + Leinöl. Modern: Sikaflex 291 |
| Risiko | Holz um Borddurchlass kann faulen → regelmäßig prüfen |

### N.4 Trockenstarter / Dry-Stack-Boote

| Aspekt | Empfehlung |
|---|---|
| Besonderheit | Boot wird nach jedem Einsatz aus dem Wasser gehoben |
| Seeventile | Standard, aber UV-Exposition beachten (Komposit) |
| Vorteil | Kein Bewuchs, keine Dauerbelastung in Seewasser |
| Wartung | Weniger Korrosion, aber Dichtmasse trocknet schneller aus |

(Confidence: documented — Fachwerft-Empfehlungen, Klassifikationsgesellschaften)

---

## ANHANG O — Umwelt

### O.1 Umweltaspekte von Seeventil-Materialien

| Material | Umwelt-Aspekt | Bewertung |
|---|---|---|
| Bronze (Cu-Legierung) | Cu²⁺-Ionen können marine Organismen beeinflussen | ⚠️ Gering (natürliche Cu-Konzentration im Meer) |
| Bronze (Blei-Anteil) | Pb in C83600 (5%) | ⚠️ FDA-konform für Trinkwasser, aber bleihaltig |
| Komposit (GFK) | Nicht biologisch abbaubar, aber chemisch inert | ⚠️ Recycling-Problem am Lebensende |
| Komposit (Marelon) | PA6/6 + Glasfaser, nicht recyclebar | ⚠️ Deponierung/Verbrennung |
| Antifouling im Borddurchlass | Biozide (Kupferoxid, Zinkpyrithion) | ⚠️ Umweltbelastung (reguliert) |

### O.2 Bleifreie Alternativen

EU-Trinkwasserrichtlinie 2020/2184 begrenzt Blei auf <5 µg/l ab 2036. Dies betrifft auch marine Systeme:
- **C89520**: Bleifrei-Bronze (Bi/Se statt Pb) — erste Seeventile verfügbar
- **Komposit**: Naturgemäß bleifrei
- **AYDI-Empfehlung**: Für Trinkwasser-Systeme (Wassermacher) bereits jetzt bleifreie Ventile verwenden

(Confidence: documented — EU-Trinkwasserrichtlinie, Umweltbundesamt)

---

## ANHANG P — Erweiterte FAQ (SV-026 bis SV-040)

### SV-026: Kann ich ein 316L-Edelstahl-Kugelventil als Seeventil verwenden?
**Antwort**: Technisch möglich, aber NICHT empfohlen. 316L ist anfällig für Spaltkorrosion in Seewasser (Gewinde, unter Dichtungen). Bronze oder Komposit sind die bessere Wahl. Ausnahme: Superyachten mit vollständigem 316L-System und ICCP.
**Confidence**: documented

### SV-027: Wie oft muss ein Komposit-Seeventil ausgetauscht werden?
**Antwort**: Empfohlene Lebensdauer: 15–20 Jahre (TruDesign empfiehlt 15 Jahre). Bei UV-Exposition oder tropischem Klima: kürzer. Bei geschützter Installation (Maschinenraum, unter Cockpit): länger. Jährliche Sichtprüfung auf Risse und Verfärbungen.
**Confidence**: documented

### SV-028: Was bedeutet "Full Port" bei einem Kugelventil?
**Antwort**: "Full Port" (Volldurchgang) bedeutet, dass die Bohrung in der Kugel den gleichen Durchmesser hat wie die Anschlüsse. Kein Strömungswiderstand bei voller Öffnung. "Reduced Port" (Teildurchgang) hat eine kleinere Bohrung — reduzierter Durchfluss. Für Seeventile IMMER Full Port wählen.
**Confidence**: documented

### SV-029: Mein Boot hat 30 Jahre alte Bronze-Seeventile — muss ich tauschen?
**Antwort**: Nicht zwingend, wenn: 1) Material ist echte Bronze (C83600/C92200), KEIN Messing. 2) Kein Lochfraß oder Dezinkifizierung sichtbar. 3) Ventile betätigbar. 4) Kein Tropfen. Wenn alle Punkte OK: weiterverwenden unter jährlicher Kontrolle. Bronze hält 40–50+ Jahre bei guter Pflege.
**Confidence**: documented

### SV-030: Darf ich Komposit-Borddurchlass mit Bronze-Seeventil kombinieren?
**Antwort**: JA — das ist sogar eine gute Kombination. Der Komposit-Borddurchlass isoliert galvanisch, das Bronze-Seeventil bietet mechanische Robustheit. ACHTUNG: Gewinde müssen kompatibel sein (BSP ↔ BSP). TruDesign bietet Adapter an.
**Confidence**: documented

### SV-031: Wie erkenne ich ob meine Schlauchschellen aus 316L oder 304 sind?
**Antwort**: Optisch kaum unterscheidbar. Sicher: Stempel auf der Schelle lesen ("316" oder "W5"). Unsicher: Magnettest — 316L ist weniger magnetisch als 304, aber dieser Test ist unzuverlässig. Am sichersten: Nur von Markenherstellern (ABA, NORMA, Jubilee) kaufen, die 316L garantieren.
**Confidence**: documented

### SV-032: Mein Seeventil hat innen Grünspan — muss ich es reinigen?
**Antwort**: Leichter Grünspan (Patina) innen ist normal und sogar schützend. NICHT entfernen. Wenn der Grünspan den Durchfluss reduziert: vorsichtig mechanisch reinigen (Flaschenbürste, KEIN Säure-Bad). Starke Ablagerungen: Ventil bei Haul-Out ausbauen und reinigen.
**Confidence**: documented

### SV-033: Warum ist mein Echolot-Borddurchlass anders als die anderen?
**Antwort**: Echolot- und Log-Durchlässe sind oft als "Durchbruch" ohne Seeventil ausgeführt, da der Geber den Durchlass verschließt. ABYC empfiehlt dennoch ein Seeventil davor. Viele Geber (z.B. B&G, Airmar) haben einen integrierten Verschlussdeckel. IMMER Holzpfropfen bereithalten für den Fall, dass der Geber entfernt wird.
**Confidence**: documented

### SV-034: Wie vermeide ich, dass mein Seeventil im Winter einfriert?
**Antwort**: Drei Strategien: 1) Boot an Land, alle Ventile OFFEN (Wasser läuft ab). 2) Boot im Wasser: Kühlwassersystem mit Frostschutz (Propylenglykol, NICHT Ethylenglykol!) spülen. 3) Heizung im Boot (Diesel-Heizung, Thermo-Siphon). Eis im Ventil kann den Körper sprengen — besonders bei Komposit.
**Confidence**: documented

### SV-035: Welche Seeventile muss ich im Notfall zuerst schließen?
**Antwort**: Priorität: 1) Das größte Ventil unter der Wasserlinie (meist Motorkühlwasser, DN32–DN50). 2) Alle Ventile in der Nähe des Lecks. 3) Alle verbleibenden Ventile unter der Wasserlinie. Faustregel: Im Zweifel ALLE schließen. Den Motor kann man danach wieder kühlen, aber ein Boot kann man nicht ent-sinken.
**Confidence**: documented

### SV-036: Wie viel Gewicht spare ich mit Komposit statt Bronze?
**Antwort**: Erheblich. Ein TruDesign DN38 Kugelventil wiegt 420 g, ein Groco BV-1500 (Bronze) wiegt 1.850 g. Bei 8 Ventilen: Komposit ≈ 3,4 kg, Bronze ≈ 14,8 kg. Ersparnis ca. 11 kg. Für Regattasegler relevant, für Fahrtensegler vernachlässigbar. Sicherheit geht IMMER vor Gewicht.
**Confidence**: documented

### SV-037: Kann Antifouling direkt auf Seeventile aufgetragen werden?
**Antwort**: Auf den BORDDURCHLASS (außen) ja — Standard-Antifouling wie auf dem Rest des Unterwasserschiffs. Auf das SEEVENTIL (innen) NEIN — Antifouling-Partikel können Ventildichtflächen beschädigen. Für den Borddurchlass-Innenbereich: manche Eigner verwenden eine dünne Schicht Lanolin (Wollfett) als Bewuchsschutz.
**Confidence**: documented

### SV-038: Mein Seeventil hat ein BSP-Gewinde, ich brauche einen NPT-Anschluss. Was tun?
**Antwort**: BSP→NPT Adapter verwenden (erhältlich bei Groco, Guidi, Osculati). ACHTUNG: Adapter = zusätzliche Dichtstelle = zusätzliches Risiko. Besser: Passendes Ventil mit dem richtigen Gewinde kaufen. Bei Neubau/Komplett-Erneuerung: konsistent BSP (Europa) oder NPT (USA) verwenden.
**Confidence**: documented

### SV-039: Warum empfiehlt AYDI 3M 4200 statt 5200 für Seeventile?
**Antwort**: 3M 5200 ist ein Permanent-Kleber — ein damit montiertes Seeventil kann NICHT ohne Beschädigung des Rumpflaminats ausgebaut werden. 3M 4200 (oder Sikaflex 291) ist ein hochfester Dichtstoff, der mit Werkzeug gelöst werden kann. Seeventile MÜSSEN austauschbar bleiben (Wartung, Survey, Austausch nach 20–30 Jahren).
**Confidence**: documented

### SV-040: Was ist ein Antisiphon-Ventil und brauche ich eins?
**Antwort**: Ein Antisiphon-Ventil (Siphon-Brecher) verhindert, dass Wasser per Siphon-Effekt zurück ins Boot fließt. PFLICHT bei: 1) Nassauspuff unter Wasserlinie, 2) WC-Einlass, wenn Schüssel unter WL. Kein Seeventil-Ersatz — zusätzliche Sicherheit im System. Hersteller: Vetus (?"Serie), Groco (SVS), Whale. Preis: 25–85 EUR.
**Confidence**: documented

---

## ANHANG Q — Zeitleiste: Geschichte der Seeventile

| Jahr | Entwicklung |
|---|---|
| ~1850 | Erste Kegelventile aus Rotguss in der Schifffahrt |
| 1890 | Blakes (UK) beginnt Seeventile für Yachten zu produzieren |
| 1907 | Perko (USA) gegründet |
| 1917 | Buck Algonquin (USA) gegründet |
| 1927 | Groco (USA) gegründet — "Gross Mechanical Laboratories" |
| 1950er | Bronze-Kugelventile ersetzen langsam Kegelventile |
| 1968 | Guidi (Italien) gegründet — europäischer OEM-Standard |
| 1970er | ABYC veröffentlicht erste H-27 Standards |
| 1980er | Erste Komposit-Borddurchlässe (Forespar Marelon) |
| 1990 | ISO 9093-1 veröffentlicht (metallische Seeventile) |
| 1995 | TruDesign (Neuseeland) gegründet — GFK-Seeventile |
| 1997 | ISO 9093-2 veröffentlicht (nichtmetallische Seeventile) |
| 2000er | Komposit-Seeventile werden OEM-Standard bei großen Werften |
| 2013 | EU RCD 2013/53/EU — CE-Pflicht für Borddurchlässe |
| 2015 | Vetus stellt elektrisch betätigbare Seeventile vor |
| 2020 | ISO 9093:2020 — aktualisierte Norm für beide Materialgruppen |
| 2025 | Smart-Seacock-Monitoring in Entwicklung (Sensoren + IoT) |
| 2027 (geplant) | TruDesign PPS-Linie (Hochleistungsthermoplast) angekündigt |

(Confidence: documented + estimated — Herstellergeschichten, ISO-Archiv)

---

## ANHANG Q.2 — Normen-Referenz (vollständig)

### Direkt anwendbare Normen für Seeventile

| Norm | Titel | Ausgabe | Relevanz |
|---|---|---|---|
| ISO 9093-1 | Kleine Wasserfahrzeuge — Seeventile und Borddurchlässe — Teil 1: Metallisch | 2020 | Hauptnorm für Bronze/Messing-Ventile |
| ISO 9093-2 | Kleine Wasserfahrzeuge — Seeventile und Borddurchlässe — Teil 2: Nichtmetallisch | 2020 | Hauptnorm für Komposit-Ventile |
| ISO 9094 | Kleine Wasserfahrzeuge — Brandschutz | 2015 | Brennverhalten von Komposit-Ventilen |
| ISO 8099 | Kleine Wasserfahrzeuge — Toilettensysteme | 2020 | WC-Borddurchlässe |
| ISO 8469 | Kleine Wasserfahrzeuge — Nicht-brandbeständige Kraftstoffschläuche | 2021 | Schlauchspezifikation |
| ISO 7840 | Kleine Wasserfahrzeuge — Brandbeständige Kraftstoffschläuche | 2021 | Schlauchspezifikation |
| ISO 10133 | Kleine Wasserfahrzeuge — Elektrische Systeme — Extra-Niederspannung DC | 2012 | Galvanische Isolation |
| ISO 13297 | Kleine Wasserfahrzeuge — Elektrische Systeme — Wechselstrom | 2014 | Landstrom, Galvanischer Isolator |
| ISO 12215 | Kleine Wasserfahrzeuge — Rumpfbau und Dimensionierung | 2019 | Rumpfdurchbrüche, Backing-Blocks |
| ISO 12216 | Kleine Wasserfahrzeuge — Fenster, Bullaugen, Luken | 2020 | Durchbrüche allgemein |

### Amerikanische Normen

| Norm | Titel | Relevanz |
|---|---|---|
| ABYC H-27 | Seacocks, Thru-Hulls, and Drain Plugs | Hauptnorm USA |
| ABYC H-24 | Gasoline Fuel Systems | Kraftstoff-Borddurchlässe |
| ABYC H-25 | Portable Fuel Systems | Kraftstoff-Borddurchlässe |
| ABYC E-11 | AC and DC Electrical Systems on Boats | Galvanische Isolation |
| ABYC E-2 | Cathodic Protection | Anodenschutz |

### Werkstoffnormen

| Norm | Titel | Relevanz |
|---|---|---|
| ASTM B61 | Standard Specification for Steam or Valve Bronze Castings | C92200 (Navy G) |
| ASTM B62 | Standard Specification for Composition Bronze or Ounce Metal Castings | C83600 (85-5-5-5) |
| ASTM B505 | Standard Specification for Copper Alloy Continuous Castings | Bronze allgemein |
| EN 12164 | Kupfer und Kupferlegierungen — Stangen | DZR-Messing CW602N |
| EN 12165 | Kupfer und Kupferlegierungen — Schmiedestücke | DZR-Messing |
| EN 1982 | Kupfer und Kupferlegierungen — Blockmetalle und Gussstücke | Bronze-Guss |

(Confidence: documented — ISO, ABYC, ASTM, EN Normenverzeichnisse)

---

## ANHANG Q.3 — Prüfprotokolle (Vorlagen)

### Prüfprotokoll Seeventil-Einzelbewertung

```
AYDI SEEVENTIL-PRÜFPROTOKOLL
================================
Boot: ___________________________
Liegeplatz: _____________________
Datum: __________________________
Prüfer: _________________________

VENTIL Nr.: ___ von ___
Position: _______________________
Anwendung: ______________________
DN: ______ mm  |  Gewinde: BSP / NPT ____"
Material: Bronze / DZR / Komposit / Messing / Unbekannt
Hersteller: ____________ Modell: ____________
Geschätztes Alter: ______ Jahre

PRÜFUNG:
[ ] Ventil betätigbar? (öffnen/schließen)    JA / NEIN / SCHWERGÄNGIG
[ ] Griff vorhanden und fest?                 JA / NEIN
[ ] Kein sichtbarer Wasseraustritt?           JA / NEIN → Wo: __________
[ ] Kein sichtbare Korrosion?                 JA / NEIN → Art: _________
[ ] Dezinkifizierungs-Verdacht?               JA / NEIN
[ ] Säure-Test durchgeführt?                  JA / NEIN → Ergebnis: ____
[ ] Doppelte Schlauchschellen?                JA / NEIN
[ ] Schlauchschellen 316L?                    JA / NEIN / UNKLAR
[ ] Backing-Block vorhanden?                  JA / NEIN / N/A
[ ] Backing-Block fest?                       JA / NEIN / N/A
[ ] Dichtmasse intakt?                        JA / NEIN
[ ] Holzpfropfen vorhanden?                   JA / NEIN
[ ] Schlauch Zustand?                         GUT / VERHÄRTET / RISSIG

BEWERTUNG:
Score: ____/100
Zustand: EXZELLENT / GUT / AUSREICHEND / MANGELHAFT / KRITISCH
Empfehlung: ______________________________________
Dringlichkeit: sofort / innerhalb_30_tage / nächstes_haul_out / monitoring

Foto-Nr.: ____________
Unterschrift Prüfer: _______________
```

### Prüfprotokoll Seeventil-Gesamtsystem

```
AYDI SEEVENTIL-SYSTEM GESAMTBEWERTUNG
========================================
Boot: _________________ Typ: ______________
Baujahr: _______ LOA: _____ m
Rumpfmaterial: GFK / Stahl / Alu / Holz
Liegeplatz: _____________ Revier: __________

INVENTAR:
Gesamtanzahl Seeventile: _____
Davon unter Wasserlinie: _____
Davon bewertet: _____

MATERIALVERTEILUNG:
Bronze C83600: ___  |  Bronze C92200: ___
DZR-Messing: ___   |  Komposit: ___
Messing (GEFAHR!): ___  |  Unbekannt: ___

VENTILTYPEN:
Kugelventil: ___  |  Kegelventil: ___
Gate-Ventil (VERBOTEN!): ___

GESAMTBEWERTUNG:
System-Score: ____/100
Schlechtester Einzelscore: ____/100
Kritische Befunde: ________________________________
Empfehlung: _______________________________________

KOSTEN:
Geschätzte Kosten kritischer Austausch: ______ EUR
Geschätzte Kosten Komplett-Erneuerung: ______ EUR

Datum: __________  Prüfer: ______________
```

(Confidence: documented — AYDI-Prüfprotokolle)

---

## ANHANG R — Stichwortverzeichnis

| Stichwort | Abschnitte |
|---|---|
| ABYC H-27 | 1.2.2, 7.5, 10.1.2, 14.8, Anhang I |
| Aluminium-Rumpf | 3.5, 11.3, Anhang N.2 |
| Antifouling | 3.1–3.3, 14.12 |
| Apollo Valves | 8.8 |
| Backing-Block | 10.2, 14.5, Anhang L Nr. 4 |
| Bewuchs | 14.12, 3.2, 3.3 |
| Blakes | 8.3 |
| Borddurchlass | 7.3, 14.9, Anhang A |
| Bronze | 7.2.1, 7.2.2, Anhang B, Anhang J |
| BSP-Gewinde | 12.2 Schritt 4, SV-012 |
| Buck Algonquin | 8.6 |
| CE / RCD | 1.2.3 |
| Compliance | Anhang I |
| Dichtmasse | 10.3, 14.6, SV-008 |
| Dezinkifizierung | 7.2.2, 14.1, Anhang K.1, SV-002, SV-005 |
| DZR-Messing | 7.2.3, SV-005 |
| Durchflussrate | 11.1 |
| Elektrolyse | 14.2, SV-022, Fallstudie F.4, F.8 |
| Forespar / Marelon | 8.4 |
| Frostschutz | 3.1, SV-018, SV-034, Fallstudie F.3 |
| Galvanische Korrosion | 11.3, 14.2 |
| Galvanischer Isolator | 3.2, SV-022, Anhang L Nr. 12 |
| Gate-Ventil | 7.1.3, 14.8, SV-004, Anhang L Nr. 2 |
| Groco | 8.1 |
| Guidi | 8.5 |
| Holzpfropfen | 7.4, SV-016, Anhang L Nr. 8 |
| ISO 9093 | 1.2.1, Anhang I |
| Kegelventil | 7.1.2 |
| Komposit | 7.2.4, 14.4, SV-027 |
| Korrosionsrate | 11.4 |
| Kugelventil | 7.1.1 |
| Lebensdauer | 13.1 |
| Messing | 7.2.1, 7.2.2, SV-002 |
| Notfall | 15.1, 15.5, 19.1 |
| NPT-Gewinde | 12.2 Schritt 4, SV-012 |
| Osculati | 8.11 |
| Perko | 8.7 |
| Plastimo | 8.10 |
| Pydantic-Modelle | 6.1, 6.2 |
| Schlauchschellen | 10.1.2, SV-006 |
| Scoring | 6.2 |
| Smart Seacocks | 2.1 |
| Survey | SV-017 |
| TruDesign | 8.2 |
| Versicherung | 1.2.5 |
| Vetus | 8.9 |
| Wassereinbruchrate | 11.1.2 |
| Winterlager | 3.1, SV-018 |

---

> **Ende der Wissensdatei 07.01 — Seeventile (Bronze/Messing/Komposit)**
> **Zeilen**: ~3.800
> **Letzte Aktualisierung**: 2026-04
> **Nächste geplante Überarbeitung**: 2026-10
> **Verantwortlich**: AYDI Knowledge Engineering Team
> **SICHERHEITSHINWEIS**: Jedes Seeventilversagen = potenzieller Wassereinbruch = SINKEN. Keine Kompromisse bei Material und Installation.
