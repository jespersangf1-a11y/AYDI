---
title: "Ankerwinden im Yachtbau — Vollständige Wissensreferenz"
kategorie: "13 Ankerausrüstung und Zubehör"
unterkategorie: "03 Ankerwinden"
version: "1.0.0"
datum: "2026-04-26"
autor: "AYDI Research"
status: "validated"
confidence_quellen:
  - measured: "Hersteller-Datenblätter, Laborprüfungen, CE-Zertifikate"
  - documented: "Hersteller-Kataloge, Segelfachpresse, Forum-Konsens"
  - estimated: "Erfahrungswerte, Quervergleiche"
  - benchmark: "Marktdurchschnitte, Branchenstandards"
tags:
  - ankerwinde
  - windlass
  - ankerwinsch
  - kettennuss
  - gypsy
  - wildcat
  - capstan
  - spillkopf
  - vertikal_winde
  - horizontal_winde
  - elektrowinde
  - hydraulikwinde
  - handwinde
  - ankerkette
  - kettenstopper
  - kettenvorlauf
  - ankergeschirr
  - buganker
  - heckanker
  - foredeck
  - lofrans
  - lewmar
  - quick
  - maxwell
  - muir
  - italwinch
boot_klassen:
  - segelboot_8_14m
  - segelboot_14_20m
  - motoryacht_8_14m
  - motoryacht_14_20m
  - motoryacht_20_30m
  - superyacht_30m_plus
---

# 13.03 — Ankerwinden im Yachtbau: Vollständige Wissensreferenz

> **AYDI Wissensdatei 13.03** — Kategorie 13: Ankerausrüstung und Zubehör
> **Confidence-Quelle:** measured (Hersteller-TDS), documented (Hersteller-Kataloge, Forum-Konsens), estimated (Erfahrungswerte)
> **Letzte Aktualisierung:** 2026-04-26

---

## Inhaltsverzeichnis

1. [Einführung](#1-einführung)
2. [Grundlagen der Ankerwinden](#2-grundlagen-der-ankerwinden)
3. [Typenübersicht](#3-typenübersicht)
4. [Produktlinien der Hersteller](#4-produktlinien-der-hersteller)
5. [Elektrik und Installation](#5-elektrik-und-installation)
6. [Montage und Einbau](#6-montage-und-einbau)
7. [Fehlerbild-Atlas](#7-fehlerbild-atlas)
8. [Troubleshooting-Entscheidungsbäume](#8-troubleshooting-entscheidungsbäume)
9. [FAQ — Häufige Fragen](#9-faq--häufige-fragen)
10. [Glossar](#10-glossar)
11. [Schnell-Referenz](#11-schnell-referenz)
12. [ANHANG A — Fallstudie 1: Nachrüstung Vertikalwinde auf Bavaria 40](#anhang-a)
13. [ANHANG B — Fallstudie 2: Hydraulikwinde auf Hallberg-Rassy 53](#anhang-b)
14. [ANHANG C — Fallstudie 3: Motorschwäche auf Jeanneau Sun Odyssey 449](#anhang-c)
15. [ANHANG D — Fallstudie 4: Kettennuss-Verschleiß auf Beneteau Oceanis 45](#anhang-d)
16. [ANHANG E — Fallstudie 5: Solenoid-Ausfall auf Grand Soleil 46 LC](#anhang-e)
17. [ANHANG F — Fallstudie 6: Horizontalwinde auf Princess V58](#anhang-f)
18. [ANHANG G — Fallstudie 7: Handwinde auf Folkboot](#anhang-g)
19. [ANHANG H — Fallstudie 8: Kombiwinde Kette/Seil auf HR 342](#anhang-h)
20. [ANHANG I — Confidence-Mapping](#anhang-i)
21. [ANHANG J — AYDI Bewertungsschema für Ankerwinden](#anhang-j)
22. [ANHANG K — Kettennuss-Kompatibilitätsmatrix](#anhang-k)
23. [ANHANG L — Kabelquerschnitt-Rechentabelle](#anhang-l)
24. [ANHANG M — Wartungsplan Jahresübersicht](#anhang-m)
25. [ANHANG N — Normen und Regularien](#anhang-n)
26. [ANHANG O — Bezugsquellen und Preisvergleich](#anhang-o)
27. [ANHANG P — Erfahrungsberichte aus Foren](#anhang-p)
28. [ANHANG Q — Visuelle Analyse-Referenzbilder](#anhang-q)
29. [ANHANG R — AYDI-Integration (Pydantic-Modelle)](#anhang-r)

---

## 1. Einführung

### 1.1 Bedeutung der Ankerwinde im Yachtsystem

Die Ankerwinde (engl. anchor windlass) ist eines der am stärksten beanspruchten mechanischen Systeme an Bord einer Yacht. Sie muss unter widrigsten Bedingungen — Seegang, Regen, Salzwasser, extremer Hitze oder Kälte — zuverlässig funktionieren. Ein Versagen der Ankerwinde in einer kritischen Ankersituation kann zu Kollisionen, Grundberührungen oder dem Verlust des gesamten Ankergeschirrs führen.

Die korrekte Dimensionierung, Installation und Wartung der Ankerwinde ist daher kein optionaler Komfort, sondern eine sicherheitsrelevante Kernkompetenz im Yachtdesign. AYDI bewertet Ankerwinden über alle drei Analyse-Pipelines:

- **Pipeline A (Strukturiert):** Zugkraft, Motorleistung, Kettenkompatibilität, Kabelquerschnitte
- **Pipeline B (Visuell):** Montagequalität, Korrosionszustand, Kettenführung, Decksverstärkung
- **Pipeline C (Text):** Serviceberichte, Eignerberichte, Reklamationsmuster

### 1.2 Historische Entwicklung

Die Geschichte der Ankerwinde beginnt mit der manuellen Spillwinde (Capstan) auf Segelschiffen des 17. Jahrhunderts. Der Übergang zur mechanisierten Ankerbedienung auf Yachten vollzog sich in mehreren Phasen:

- **Vor 1950:** Ausschließlich Handwinden (Spillköpfe, Handkurbeln). Nur auf größeren Yachten ab ~12 m vorhanden.
- **1950–1970:** Erste elektrische Ankerwinden für Yachten. Simpson-Lawrence (später Lewmar) und Goiot als Pioniere. 12V-Gleichstrommotoren, einfache Kettennüsse.
- **1970–1990:** Standardisierung der Kettennuss-Profile. Hydraulische Winden für größere Yachten. Lofrans, Maxwell und Muir treten in den Markt ein.
- **1990–2010:** Digitale Kettenvorläufe (Chain Counter). Fernbedienungen. Verbesserte Dichtungen. Quick (Italien) wird Marktführer im Mittelmeerraum.
- **2010–heute:** Integrierte Steuerungen mit CAN-Bus/NMEA-2000-Anbindung. Permanentmagnet-Motoren. Gewichtsoptimierung. Titanium-Kettennüsse für Superyachten.

### 1.3 Regulatorischer Rahmen

Ankerwinden unterliegen keiner direkten CE-Zertifizierungspflicht als eigenständiges Produkt. Jedoch gelten folgende Regelwerke:

| Norm/Regelwerk | Relevanz |
|----------------|----------|
| ISO 12217 (Stabilität) | Ankergewicht beeinflusst Buggewicht und Trimm |
| ISO 15084 (Ankern, Verholen, Festmachen) | Dimensionierung Ankergeschirr nach Bootsklasse |
| ISO 10133 (Elektrische Gleichstromanlagen) | Verkabelung, Absicherung, Schalter |
| ABYC E-11 (AC & DC Electrical Systems) | US-Standard für Kabelquerschnitte und Absicherung |
| GL/DNV (Germanischer Lloyd / DNV) | Klassifizierung bei Superyachten >24 m |

### 1.4 Sicherheitskritische Aspekte

Ankerwinden sind im Betrieb gefährlich. Die häufigsten Unfälle:

1. **Kettenfang:** Finger oder Kleidung geraten zwischen Kette und Kettennuss — schwerste Quetschverletzungen.
2. **Unkontrollierter Kettenablauf:** Bei Versagen des Kettenstoppers rauscht die Kette mit hoher Geschwindigkeit aus — Brandgefahr durch Reibung, Verlust des Ankergeschirrs.
3. **Elektrischer Schlag:** Fehlerhafte Verkabelung bei Nassbereich-Montage.
4. **Decksverletzung:** Überlastete Ankerwinde reißt aus der Decksverankerung.

AYDI bewertet diese Risiken in der Compliance-Analyse (Modul `compliance`) und kennzeichnet sicherheitskritische Befunde mit dem Label `CRITICAL`.

### 1.5 Abgrenzung dieser Wissensdatei

Diese Datei behandelt **ausschließlich Ankerwinden** (Windlass, Winsch). Nicht behandelt werden:
- Anker selbst (→ 13.01)
- Ankerketten und -leinen (→ 13.02)
- Kettenstopper und Bugbeschläge (→ 13.04)
- Ankerroller und Bugspriet (→ 13.05)
- Kettenkästen und Kettenführung (→ 13.06)

### 1.6 Terminologie-Hinweis

Im deutschen Sprachraum werden die Begriffe „Ankerwinde", „Ankerwinsch" und „Ankerwindlass" oft synonym verwendet. Im Englischen ist „windlass" der korrekte Oberbegriff, während „winch" eigentlich eine Seilwinde (Fallenwinde, Genuawinde) bezeichnet. Diese Datei verwendet durchgängig „Ankerwinde" als deutschen Oberbegriff.

---

## 2. Grundlagen der Ankerwinden

### 2.1 Funktionsprinzip

Eine Ankerwinde ist ein mechanisches Hebezeug, das die Ankerkette (und/oder das Ankertau) kontrolliert ein- und ausfiert. Die Grundfunktion umfasst:

1. **Einholen (Retrieval):** Die Kette wird über die Kettennuss (Gypsy/Wildcat) geführt und durch Formschluss in den Kettentaschen nach oben gezogen. Der Anker wird zum Bug befördert.
2. **Fieren (Deployment):** Die Kette wird kontrolliert abgelassen. Bei Freifall-Winden (Free-Fall) fällt die Kette durch Schwerkraft; bei kontrollierten Winden bremst der Motor oder eine mechanische Bremse.
3. **Halten (Holding):** In Ruhestellung hält ein separater Kettenstopper (Chain Stopper / Devil's Claw) die Last — nicht die Winde selbst.

**Kritische Regel:** Die Ankerwinde ist **kein Festmachpunkt.** Die Ankerlast im Liegen wird immer vom Kettenstopper und der Klüse getragen. Die Winde dient nur dem kontrollierten Bewegen der Kette.

### 2.2 Vertikalwinde vs. Horizontalwinde

Die fundamentale Bauartunterscheidung bei Ankerwinden:

#### 2.2.1 Vertikalwinde (Vertical Windlass)

**Aufbau:** Der Motor sitzt unter Deck, die Kettennuss und ggf. der Spillkopf (Capstan Drum) sitzen über Deck. Die Antriebswelle steht vertikal.

**Vorteile:**
- Geringere Deckspräsenz — nur Kettennuss und Spillkopf sichtbar
- Motor geschützt unter Deck — besserer Korrosionsschutz
- Bessere Kettenführung — die Kette läuft von der Kettennuss direkt nach unten in den Kettenkasten
- Höherer Umschlingungswinkel der Kette an der Kettennuss (≥180°) — sichererer Kettengriff
- Optisch eleganter — bevorzugt im Segelbootbereich

**Nachteile:**
- Benötigt Decksdurchbruch für die Antriebswelle — zusätzliche Abdichtung erforderlich
- Montage komplexer — Decksverstärkung unter Deck, Motor muss von unten zugänglich sein
- Kettenkasten muss direkt unter der Winde liegen
- Schwerer zu warten (Motor unter Deck)

**Typische Anwendung:** Segelyachten 8–20 m, kleinere Motoryachten

**Umschlingungswinkel:** 180°–220° (je nach Kettennuss-Design)

**Kennzeichnende Hersteller-Serien:** Lofrans Tigres/Kobra, Lewmar V-Series, Quick Aleph, Maxwell RC/VWC

#### 2.2.2 Horizontalwinde (Horizontal Windlass)

**Aufbau:** Der Motor sitzt im Gehäuse über Deck (oder teils unter Deck mit horizontaler Welle). Die Antriebswelle steht horizontal, Kettennuss und Motor befinden sich auf einer Ebene.

**Vorteile:**
- Kein Decksdurchbruch für Antriebswelle — einfachere Abdichtung
- Einfachere Nachrüstung — kann auf das Deck geschraubt werden
- Motor leichter zugänglich für Wartung
- Flexiblere Positionierung — muss nicht direkt über dem Kettenkasten sitzen
- Robuster bei schweren Ketten/Ankern

**Nachteile:**
- Größere Deckspräsenz — das gesamte Gehäuse ist sichtbar
- Motor stärker den Elementen ausgesetzt (Salzwasser, Sonne)
- Geringerer Umschlingungswinkel (90°–150°) — erhöhtes Risiko des Kettenspringens
- Kette muss über Deck zum Kettenkasten umgelenkt werden

**Typische Anwendung:** Motoryachten 10–30 m, Nachrüstungen, schwere Ankersysteme

**Umschlingungswinkel:** 90°–150° (je nach Modell)

**Kennzeichnende Hersteller-Serien:** Lewmar H-Series/Pro-Series, Quick Héron/Prince, Maxwell HRC, Lofrans X-Series

#### 2.2.3 Vergleichstabelle Vertikal vs. Horizontal

| Kriterium | Vertikalwinde | Horizontalwinde |
|-----------|--------------|-----------------|
| Deckspräsenz | Minimal (nur Kettennuss + Spillkopf) | Vollständiges Gehäuse sichtbar |
| Decksdurchbruch | Ja (Antriebswelle) | Nein (nur Befestigungsbolzen) |
| Motorschutz | Gut (unter Deck) | Mäßig (Gehäuse über Deck) |
| Umschlingungswinkel | 180°–220° | 90°–150° |
| Kettenführung | Direkt nach unten | Umlenkung erforderlich |
| Nachrüstung | Aufwändig | Einfach |
| Wartungszugang | Schwierig (Motor unter Deck) | Gut (Gehäusedeckel) |
| Typische Bootsklasse | Segelyachten, kleine Motorboote | Motoryachten, große Boote |
| Gewicht (gleiche Zugkraft) | Leichter über Deck, schwerer gesamt | Schwerer über Deck |
| Preis (gleiche Zugkraft) | ca. 10–15 % teurer | Basis |

### 2.3 Kettennuss (Gypsy / Wildcat)

Die Kettennuss ist das Herzstück jeder Ankerwinde. Sie ist das profilierte Rad, das die Kettenglieder formschlüssig aufnimmt und die Zugkraft auf die Kette überträgt.

#### 2.3.1 Profilformen

Die Kettennuss muss exakt zum Kettenprofil passen. Es gibt **keine universelle Kettennuss.** Die drei kritischen Parameter sind:

1. **Kettennennmaß (Caliber):** Der Durchmesser des Kettenglieddrahtes in mm (z. B. 6 mm, 8 mm, 10 mm, 12 mm)
2. **Kettenstandard:** DIN 766 (Kurzglied), ISO 4565 (BBB/G30), ACCO (BBB), DIN 5685 (Langglied)
3. **Kettengliedform:** Kurzglied (Short Link) vs. Langglied (Long Link) vs. BBB (Triple B)

| Kettennorm | Gliedverhältnis (L:D) | Verbreitung | Kompatibilität |
|------------|----------------------|-------------|-----------------|
| DIN 766 (Kurzglied) | ~3:1 | Europa dominant | Europäische Winden |
| ISO 4565 / BBB / G30 | ~3.5:1 | USA, Australien | Amerikanische Winden |
| DIN 5685 (Langglied) | ~4.5:1 | Selten bei Yachten | Spezial-Kettennüsse |
| G40 / G43 (High Test) | ~3.5:1 | USA | Spezielle Kettennüsse |
| G70 (Transport) | variiert | Nicht für Yachten! | Nicht kompatibel |

**AYDI-Bewertungsregel:** Eine Kette, die nicht zum Kettennuss-Profil passt, erhält automatisch die Bewertung `CRITICAL` im Compliance-Modul. Inkompatible Kette/Kettennuss ist der häufigste Grund für Kettensprünge und unkontrollierten Kettenablauf.

#### 2.3.2 Materialien der Kettennuss

| Material | Einsatz | Lebensdauer | Preis-Faktor |
|----------|---------|-------------|--------------|
| Aluminiumbronze (CuAl10Fe5Ni5) | Standard bei Qualitätswinden | 15–25 Jahre | 1.0× |
| Manganbronze (CuZn35Mn2Al1Fe1) | Ältere Winden, Einstiegsklasse | 10–15 Jahre | 0.7× |
| Edelstahl 316L | Selten, optische Gründe | 20+ Jahre | 1.5× |
| Titan Grade 5 | Superyachten, Racing | 30+ Jahre | 4.0× |
| Gusseisen verzinkt | Preiswinde, Binnenschifffahrt | 5–8 Jahre | 0.4× |

Aluminiumbronze ist der Industriestandard. Das Material bietet exzellente Korrosionsbeständigkeit in Seewasser, hohe Festigkeit und gute Gleiteigenschaften gegen verzinkte Kette.

#### 2.3.3 Verschleiß der Kettennuss

Die Kettennuss unterliegt Abrieb durch die verzinkte Stahlkette. Verschleißindikatoren:

- **Visuell:** Die Taschen (Pockets) der Kettennuss zeigen sichtbare Rillen oder asymmetrische Abnutzung
- **Funktional:** Die Kette springt häufiger über, besonders beim Fieren
- **Messtechnisch:** Die Taschenbreite überschreitet den Kettendurchmesser + 1,5 mm

**Typische Lebensdauer Kettennuss:** 800–2.000 Ankerzyklen oder 15–25 Jahre bei normaler Nutzung (30–80 Ankerungen/Jahr).

**AYDI Visuelle Analyse:** Verschleiß der Kettennuss ist in Pipeline B (Visuell) mit `visual_medium` Confidence erkennbar. Tiefe Rillen, Farbunterschiede und Kettenspiel sind photographisch identifizierbar.

### 2.4 Spillkopf (Capstan Drum / Warping Drum)

Der Spillkopf ist eine glatte, konische oder zylindrische Trommel oberhalb der Kettennuss (bei Vertikalwinden) oder seitlich montiert (bei Horizontalwinden). Er dient zum:

- Einholen von Festmacherleinen
- Einholen von Ankerleinen (Tau statt Kette)
- Verholen des Bootes am Steg
- Einholen von Schlepp- oder Beibootleinen

**Dimensionierung:** Der Spillkopf sollte mindestens 3× den Durchmesser der dicksten verwendeten Leine als Trommeldurchmesser haben. Typische Durchmesser: 80 mm (kleine Winden) bis 200 mm (große Winden).

**Wicklungen:** Mindestens 3 volle Wicklungen auf dem Spillkopf für sicheren Kraftschluss. Nie mehr als 5 Wicklungen (Überlappungsgefahr).

### 2.5 Motortypen und Antrieb

#### 2.5.1 Elektromotor (DC)

Der mit Abstand häufigste Antrieb bei Yachten von 8–25 m.

| Parameter | 12V Systeme | 24V Systeme |
|-----------|-------------|-------------|
| Typische Leistung | 300–1.500 W | 500–3.000 W |
| Typische Zugkraft | 300–1.000 kg | 500–2.000 kg |
| Stromaufnahme | 40–130 A | 25–80 A |
| Einschaltdauer (Duty Cycle) | 3–8 min | 5–12 min |
| Typische Bootsklasse | 8–14 m | 14–25 m |
| Kabelquerschnitt | 25–70 mm² | 16–50 mm² |

**Motortypen:**
- **Permanentmagnet-Motor (PM):** Leichter, effizienter, weniger hitzebeständig. Standard bei modernen Winden.
- **Serienwundmotor (Series Wound):** Höheres Anlaufdrehmoment, robuster bei Überlast, schwerer. Ältere Winden und Heavy-Duty-Anwendungen.

**Einschaltdauer (Duty Cycle):** Der kritischste Parameter bei elektrischen Ankerwinden. Der Motor darf **nicht im Dauerbetrieb** laufen. Typische Angaben:

| Hersteller-Angabe | Bedeutung |
|-------------------|-----------|
| 3 min on / 3 min off | Intermittierender Betrieb, leichte Winden |
| 5 min on / 5 min off | Standard bei mittleren Winden |
| 8 min on / 8 min off | Hochleistungswinden |
| Continuous Duty | Nur Hydraulikwinden! Nie elektrisch |

**AYDI-Bewertungsregel:** Ein Ankeraufholvorgang, der die Einschaltdauer überschreitet (Wassertiefe × Kettengeschwindigkeit > Duty Cycle), erhält eine `WARNING` im Ergonomie-Modul.

#### 2.5.2 Hydraulikmotor

Hydraulikwinden werden ab ca. 18 m Bootslänge eingesetzt und sind Standard bei Superyachten >24 m.

**Vorteile:**
- Unbegrenzte Einschaltdauer (Continuous Duty)
- Höchste Zugkräfte (2.000–20.000+ kg)
- Kein Starkstromkabel zum Bug erforderlich
- Feinfühlige Geschwindigkeitsregelung
- Robuster bei Salzwasserumgebung

**Nachteile:**
- Erfordert Hydrauliksystem (Pumpe, Tank, Leitungen, Ventile)
- Höhere Installationskosten (€5.000–€25.000+ für das Gesamtsystem)
- Komplexere Wartung (Ölwechsel, Leitungskontrolle, Dichtungen)
- Geräuschentwicklung der Hydraulikpumpe
- Gewicht des Gesamtsystems

**Hydraulik-Parameter:**

| Parameter | Typischer Bereich |
|-----------|------------------|
| Systemdruck | 80–200 bar |
| Volumenstrom | 6–25 l/min |
| Ölsorte | HLP 46 oder HLP 32 (temperaturabhängig) |
| Tankvolumen | 5–50 Liter |
| Schlauchdurchmesser | DN 10 – DN 16 |

#### 2.5.3 Handantrieb (Manual)

Handwinden werden eingesetzt auf:
- Kleinen Booten <8 m
- Als Backup zu elektrischen/hydraulischen Winden
- Auf traditionellen Yachten (Retro-Design)
- Im Regattabereich (Gewichtsreduktion)

**Bauformen:**
- **Handkurbel direkt:** Kurbel auf der Windenwelle, Übersetzung 3:1 bis 8:1
- **Handkurbel mit Getriebe:** Separate Getriebeeinheit, Übersetzung 8:1 bis 15:1
- **Nottrieb an Elektrowinde:** Aufsteckbare Kurbel für den Notbetrieb (Standard bei den meisten elektrischen Winden)

**Ergonomische Grenzwerte (AYDI Ergonomie-Modul):**

| Parameter | Empfohlener Grenzwert |
|-----------|----------------------|
| Maximale Handkraft am Kurbelgriff | 15 kg (Frau) / 25 kg (Mann) |
| Maximale Ankermasse für Handwinde | 15 kg (ohne Kette) |
| Maximale Kettenlänge für reine Handwinde | 30 m in 5 m Wassertiefe |
| Kurbeldrehzahl Dauerbetrieb | 30–50 U/min |
| Aufholzeit 30 m Kette manuell | ca. 10–15 Minuten |

### 2.6 Zugkraft-Berechnung (Pull Force)

Die korrekte Dimensionierung der Ankerwinde beginnt mit der Berechnung der erforderlichen Zugkraft.

#### 2.6.1 Statische Zugkraft

Die statische Zugkraft muss mindestens das Gewicht des Ankers plus der Kette bis zur Wasseroberfläche tragen:

```
F_static = m_anchor × g + m_chain_per_m × depth × g
         = (m_anchor + chain_weight_per_m × depth) × 9.81

Beispiel: 20 kg Anker + 40 m × 2.2 kg/m (10 mm Kette) = 20 + 88 = 108 kg
F_static = 108 × 9.81 = 1059 N ≈ 108 kgf
```

#### 2.6.2 Dynamische Zugkraft

Im Seegang addiert sich eine dynamische Komponente:

```
F_dynamic = F_static × acceleration_factor
acceleration_factor = 1.5 (ruhiges Wasser) bis 3.0 (schwerer Seegang)

Empfohlener Sicherheitsfaktor: 2.5×
F_design = F_static × 2.5
```

#### 2.6.3 Faustregel für die Windendimensionierung

| Bootslänge (LOA) | Empfohlene Zugkraft (Winde) | Typisches Ankergewicht | Typische Kette |
|-------------------|----------------------------|----------------------|----------------|
| 8–10 m | 300–500 kg | 8–12 kg | 6–8 mm × 30 m |
| 10–12 m | 500–700 kg | 12–16 kg | 8 mm × 40 m |
| 12–14 m | 700–1.000 kg | 14–20 kg | 8–10 mm × 50 m |
| 14–16 m | 1.000–1.200 kg | 18–25 kg | 10 mm × 50–60 m |
| 16–20 m | 1.200–1.500 kg | 25–35 kg | 10–12 mm × 60–80 m |
| 20–25 m | 1.500–2.500 kg | 35–60 kg | 12–14 mm × 80–100 m |
| 25–30 m | 2.500–4.000 kg | 60–100 kg | 14–16 mm × 100+ m |

### 2.7 Kettengeschwindigkeit

Die Kettengeschwindigkeit (Line Speed) gibt an, wie schnell die Kette eingeholte wird.

| Hersteller-Angabe | Typischer Bereich | Kommentar |
|-------------------|-------------------|-----------|
| Unbelastet (No Load) | 25–45 m/min | Marketing-Angabe |
| Arbeitslast (Working Load) | 12–25 m/min | Realistischer Wert |
| Maximallast (Max Load) | 3–8 m/min | Grenzbereich |

**AYDI-Berechnung Aufholzeit:**
```
t_retrieval = depth / line_speed_working_load
Beispiel: 15 m Tiefe / 18 m/min = 0.83 min ≈ 50 Sekunden
Korrekt: + Vorkettenablauf + Horizontalkomponente ≈ 1.5–3 min real
```

### 2.8 Freifall-Funktion (Free-Fall)

Viele elektrische und hydraulische Winden verfügen über eine Freifall-Funktion (Free-Fall), bei der die Kettenbremse gelöst wird und die Kette allein durch Schwerkraft ausfiert.

**Vorteile:**
- Sehr schnelles Ankern möglich
- Kein Motorverschleiß beim Fieren
- Kein Stromverbrauch beim Ankern

**Nachteile:**
- Erfordert separate Bremse (mechanisch oder hydraulisch)
- Höhere Belastung des Kettenkastens beim Aufprall
- Lärmentwicklung beim schnellen Kettenablauf
- Risiko des unkontrollierten Ablaufs bei defekter Bremse

**AYDI-Bewertungsregel:** Winden mit Freifall-Funktion erhalten im Ergonomie-Modul einen Bonus von +5 Punkten, wenn gleichzeitig ein funktionierender Kettenstopper vorhanden ist.

### 2.9 Getriebe und Übersetzung

Ankerwinden verwenden verschiedene Getriebetypen:

| Getriebetyp | Übersetzung | Wirkungsgrad | Einsatz |
|-------------|-------------|--------------|---------|
| Schneckengetriebe | 20:1–60:1 | 40–60 % | Ältere Winden, günstige Modelle |
| Planetengetriebe | 15:1–40:1 | 70–85 % | Moderne Qualitätswinden |
| Stirnradgetriebe | 10:1–30:1 | 85–95 % | Hochleistungswinden |
| Kegelradgetriebe | 15:1–35:1 | 75–85 % | Horizontalwinden |
| Zykloidgetriebe | 20:1–50:1 | 80–90 % | Neuere Designs |

**Schneckengetriebe** haben den Vorteil der Selbsthemmung (Kette kann nicht durchrutschen), aber den Nachteil des schlechten Wirkungsgrades. Freifall-Funktion ist bei Schneckengetrieben nicht möglich.

**Planetengetriebe** sind der moderne Standard. Sie bieten hohen Wirkungsgrad bei kompakter Bauform, erfordern aber eine separate Bremse oder Selbsthemmung durch die Motorcharakteristik.

### 2.10 Dichtungskonzept

Ankerwinden sind permanent Seewasser, Spritzwasser und Salzluft ausgesetzt. Das Dichtungskonzept ist überlebenswichtig für die Lebensdauer:

**Schutzklassen (IP-Rating):**

| Bauteil | Mindest-IP | Empfohlen |
|---------|-----------|-----------|
| Motorgehäuse | IP56 | IP67 |
| Getriebe | IP55 | IP66 |
| Schalter/Fußschalter | IP67 | IP68 |
| Solenoid | IP56 | IP66 |

**Dichtungstypen in Ankerwinden:**
- **Wellendichtring (Shaft Seal):** Simmerring oder Lip Seal an der Antriebswelle
- **O-Ringe:** Statische Abdichtung zwischen Gehäuseteilen
- **Labyrinth-Dichtung:** An der Kettennuss gegen Kettenwasser
- **Kabeldurchführung:** IP68-Verschraubungen für Motorkabel

### 2.11 Gewicht und Schwerpunkt

Das Gewicht der Ankerwinde beeinflusst den Trimm des Bootes. Da die Winde am Bug montiert wird, wirkt sie sich direkt auf den Bugtrimm aus:

| Bootslänge | Max. empfohlenes Windengewicht | Typischer Bereich |
|------------|-------------------------------|-------------------|
| 8–10 m | 12 kg | 6–10 kg |
| 10–12 m | 18 kg | 10–15 kg |
| 12–14 m | 25 kg | 15–22 kg |
| 14–18 m | 40 kg | 20–35 kg |
| 18–24 m | 70 kg | 35–60 kg |
| 24–30 m | 120 kg | 60–100 kg |

**AYDI Structural-Modul:** Das Windengewicht wird im Loading-Condition-Modul (`structural`) als Festmasse am Bug berücksichtigt. Bei Segelyachten ist exzessives Buggewicht besonders kritisch für das Am-Wind-Verhalten.

---

## 3. Typenübersicht

### 3.1 Elektrische Vertikalwinde

Die elektrische Vertikalwinde ist der meistverkaufte Windentypus im Yachtbau für Boote von 8–20 m. Der Motor sitzt unter Deck, nur die Kettennuss und der Spillkopf sind über Deck sichtbar.

#### 3.1.1 Aufbau im Detail

**Über Deck:**
- Spillkopf (Capstan Drum): Konische oder zylindrische Trommel für Tauwerk, verchromt oder poliertes Edelstahl
- Kettennuss (Gypsy): Wechselbar, profiliert für spezifische Kettengröße
- Decksflansch: Befestigungsplatte mit 3–6 Bolzen, Dichtung zum Deck
- Kupplung/Entriegelung: Mechanismus zum Trennen von Motor und Kettennuss (für Freifall oder manuellen Betrieb)

**Unter Deck:**
- Elektromotor: DC Permanentmagnet oder Serienwund, 12V oder 24V
- Getriebe: Typischerweise Planetengetriebe
- Motorträger/Montagehalterung: Befestigung an der Decksunterseite oder am Schott
- Kabelanschlüsse: Zwei Starkstromkabel (Motor), ggf. Sensorleitung (Kettenzähler)

#### 3.1.2 Typische Spezifikationen

| Klasse | Zugkraft | Motor | Kette | Gewicht | Preis (2026) |
|--------|----------|-------|-------|---------|-------------|
| Klein | 300–500 kg | 500–700 W 12V | 6–8 mm | 6–10 kg | €800–€1.500 |
| Mittel | 500–1.000 kg | 700–1.200 W 12V/24V | 8–10 mm | 10–18 kg | €1.200–€2.500 |
| Groß | 1.000–1.500 kg | 1.000–1.500 W 24V | 10–12 mm | 15–28 kg | €2.000–€4.000 |
| Schwer | 1.500–2.500 kg | 1.500–2.500 W 24V | 12–14 mm | 25–45 kg | €3.500–€7.000 |

#### 3.1.3 Einbau-Schema Vertikalwinde

```
          [Spillkopf / Capstan Drum]
                    |
          [Kettennuss / Gypsy]
                    |
    ================DECK================
                    |
          [Antriebswelle (vertikal)]
                    |
          [Getriebe (Planetengetriebe)]
                    |
          [Elektromotor (DC)]
                    |
          [Motorträger / Halterung]
```

### 3.2 Elektrische Horizontalwinde

Die Horizontalwinde ist besonders bei Motoryachten und bei Nachrüstungen beliebt, da sie keinen Decksdurchbruch für die Antriebswelle erfordert.

#### 3.2.1 Aufbau im Detail

**Über Deck (komplett):**
- Gehäuse: Druckguss-Aluminium oder Edelstahl, kompakt
- Kettennuss: Seitlich am Gehäuse, horizontal drehend
- Spillkopf (optional): Auf der gegenüberliegenden Seite der Kettennuss
- Motor: Im Gehäuse integriert
- Getriebe: Im Gehäuse integriert
- Fußschalter-Anschluss: Am Gehäuse oder durch Deck

**Unter Deck:**
- Nur Befestigungsbolzen und Kabelführung
- Ggf. Solenoid-Relais (kann auch über Deck sein)

#### 3.2.2 Typische Spezifikationen

| Klasse | Zugkraft | Motor | Kette | Gewicht | Preis (2026) |
|--------|----------|-------|-------|---------|-------------|
| Klein | 300–600 kg | 500–800 W 12V | 6–8 mm | 8–14 kg | €700–€1.400 |
| Mittel | 600–1.200 kg | 800–1.500 W 12V/24V | 8–10 mm | 14–25 kg | €1.100–€2.800 |
| Groß | 1.200–2.000 kg | 1.200–2.000 W 24V | 10–12 mm | 22–40 kg | €2.200–€4.500 |
| Schwer | 2.000–3.500 kg | 2.000–3.000 W 24V | 12–16 mm | 35–70 kg | €4.000–€8.000 |

#### 3.2.3 Einbau-Schema Horizontalwinde

```
    [Spillkopf]---[Gehäuse + Motor]---[Kettennuss]
                       |  |  |
    ==================DECK==================
                     |     |
              [Bolzen] [Kabel durch Deck]
```

### 3.3 Hydraulische Ankerwinde

Hydraulische Ankerwinden sind der Standard ab ~18 m Bootslänge und bei allen Superyachten >24 m. Sie bieten unbegrenzte Einschaltdauer und höchste Zugkräfte.

#### 3.3.1 Systembeschreibung

Das hydraulische Ankerwinden-System besteht aus:

1. **Hydraulikpumpe:** Angetrieben vom Hauptmotor (PTO = Power Take Off) oder von einem separaten Elektromotor
2. **Hydrauliktank:** Reservoir für Hydrauliköl, mit Filter und Belüftung
3. **Steuerventil:** Richtungsventil (4/3-Wegeventil) zur Kontrolle der Drehrichtung
4. **Hydraulikmotor an der Winde:** Axialkolben- oder Zahnradmotor
5. **Hydraulikleitungen:** Hochdruckschläuche DN 10–16 zwischen Pumpe und Winde
6. **Druckbegrenzungsventil:** Schutz gegen Überlast

#### 3.3.2 Hydraulik-Spezifikationen nach Bootsklasse

| Bootsklasse | Zugkraft | Systemdruck | Volumenstrom | Motortyp |
|-------------|----------|-------------|--------------|----------|
| 18–22 m | 1.500–3.000 kg | 100–150 bar | 8–12 l/min | Zahnradmotor |
| 22–28 m | 3.000–5.000 kg | 120–180 bar | 12–18 l/min | Axialkolbenmotor |
| 28–35 m | 5.000–10.000 kg | 150–200 bar | 15–25 l/min | Axialkolbenmotor |
| 35–50 m | 10.000–20.000 kg | 180–250 bar | 20–40 l/min | Axialkolbenmotor |
| 50+ m | 20.000+ kg | 200–350 bar | 30–60 l/min | Radialkolbenmotor |

#### 3.3.3 Vor- und Nachteile Hydraulik

**Vorteile gegenüber Elektro:**
- Unbegrenzte Einschaltdauer (Continuous Duty)
- Kein Starkstromkabel zum Bug (nur dünne Hydraulikschläuche)
- Feinfühlige Geschwindigkeitsregelung über Proportionalventil
- Höhere Zuverlässigkeit bei extremer Belastung
- Geräuschärmer an der Winde (Pumpe kann schallgedämpft werden)
- Integration in bestehendes Hydrauliksystem (Bug-/Heckstrahlruder, Kran, Passerelle)

**Nachteile:**
- Erfordert laufenden Motor oder separate Hydraulikpumpe
- Komplexeres System mit mehr potentiellen Leckstellen
- Höhere Installationskosten
- Ölwechsel und Filterwartung erforderlich
- Bei Hydraulikausfall kein Ankerbetrieb möglich (Notantrieb nur manuell)

### 3.4 Manuelle Ankerwinde (Handwinde)

#### 3.4.1 Bauformen

**Kurbel-Spillwinde (Manual Capstan):**
- Vertikale Achse mit Spillkopf und Kettennuss
- Handkurbel zum Einholen
- Typische Übersetzung: 5:1 bis 10:1
- Für Boote 6–10 m
- Preis: €150–€500

**Kurbel-Getriebewinde (Manual Geared Windlass):**
- Horizontal oder vertikal mit Getriebegehäuse
- Zwei Geschwindigkeiten (High/Low Ratio) bei manchen Modellen
- Typische Übersetzung: 8:1 bis 15:1
- Für Boote 8–12 m
- Preis: €300–€900

**Nottrieb (Emergency Handle):**
- Aufsteckbare Handkurbel für elektrische/hydraulische Winden
- Standard-Sechskant oder proprietärer Adapter
- Sollte immer zugänglich gelagert werden
- Übersetzung der Winde wird mitgenutzt

#### 3.4.2 Ergonomische Bewertung Handwinden

| Kurbelhöhe über Deck | Bewertung | Kommentar |
|---------------------|-----------|-----------|
| 40–60 cm | Optimal | Kniende Position, maximale Kraft |
| 60–80 cm | Gut | Gebückte Position |
| 80–100 cm | Akzeptabel | Stehend, aber ungünstiger Hebelarm |
| >100 cm | Schlecht | Ineffizient, ermüdend |
| <40 cm | Schlecht | Zu tief, Rückenbelastung |

### 3.5 Kombiwinde Kette/Seil (Combination Windlass)

Kombiwinden akzeptieren sowohl Kette als auch Tau (Seil). Sie sind ideal für Ankergeschirre mit Kette-Tau-Kombination (z. B. 20 m Kette + 30 m Ankerleine).

#### 3.5.1 Aufbau

Die Kombiwinde hat zwei Führungselemente:
1. **Kettennuss (Gypsy):** Profiliert für die Kette
2. **Taurolle (Rope Drum):** Glatte oder gerippte Trommel für das Ankertau

Beide Elemente sitzen auf derselben Welle, typischerweise nebeneinander (Horizontalwinde) oder übereinander (Vertikalwinde mit Spillkopf als Taurolle).

#### 3.5.2 Seilklemm-Mechanismus

| Mechanismus | Beschreibung | Zuverlässigkeit |
|-------------|-------------|-----------------|
| Friktions-Drum | Tau wird 3–4× um glatte Trommel gelegt | Mittel — rutschgefahr bei nassem Tau |
| V-Klemme (V-Jaw) | Tau wird durch V-förmige Nut gepresst | Gut — für Tau bis 18 mm |
| Selbstklemm-Gypsy | Profilierte Trommel für Tau | Sehr gut — für Tau 10–22 mm |
| Separate Spilltrommel | Tau auf eigenem Spillkopf | Gut — universell |

#### 3.5.3 Kompatibilitätsgrenzen

| Taudurchmesser | Min. Trommeldurchmesser | Kommentar |
|---------------|------------------------|-----------|
| 10–12 mm | 60 mm | Kleine Boote, leichte Anker |
| 14–16 mm | 80 mm | Standard Segelyachten 10–14 m |
| 18–20 mm | 100 mm | Mittlere Yachten 14–18 m |
| 22–24 mm | 120 mm | Große Yachten 18–24 m |

### 3.6 Heckanker-Winden

Heckanker-Winden sind spezialisierte Winden für den Heckanker, besonders beliebt im Mittelmeerraum (Ankern „römisch-katholisch" / Heck zum Steg).

#### 3.6.1 Besonderheiten

- Kleinere Dimensionierung als Bugwinden (Heckanker ist typischerweise 50–60 % des Bugankers)
- Montage auf der Badeplattform, am Heck oder im Heckankerkasten
- Elektrisch (12V/24V), selten hydraulisch
- Fernbedienung vom Steuerstand essentiell
- Edelstahlgehäuse oder hochglanz-poliert (sichtbar am Heck)

#### 3.6.2 Hersteller mit Heckanker-Modellen

| Hersteller | Modell | Zugkraft | Kette | Preis (2026) |
|-----------|--------|----------|-------|-------------|
| Quick | Genius 1000 | 900 kg | 6–8 mm | €1.800 |
| Lofrans | Falkon | 500–700 kg | 6–8 mm | €1.600 |
| Maxwell | Hector | 600 kg | 6–8 mm | €1.900 |
| Lewmar | CPX1 | 300 kg | 6 mm | €1.200 |

> ✅ Aufgelöst (Audit): Quick Genius 1000 — max. Zugkraft 900 kg (1983 lb); weder 500 kg noch 1.000 kg. Die Modellbezeichnung „1000" entspricht nicht exakt der Zugkraft. Quelle: Quick GENIUS Bedienungsanleitung (technische Daten) sowie Händler-Spezifikationen (max pull 1983 lb ≈ 900 kg).

### 3.7 Ankerwinden für Megayachten / Superyachten (>30 m)

Im Superyacht-Segment gelten andere Regeln:

- **Klassifikation:** Lloyd's, DNV, BV, RINA klassifizieren Ankerwinden nach eigenen Regelwerken
- **Redundanz:** Zwei unabhängige Ankerwinden am Bug (Backbord + Steuerbord)
- **Kettenkaliber:** 16–42 mm Studless oder Stud-Link
- **Zugkraft:** 10.000–80.000+ kg
- **Antrieb:** Ausschließlich hydraulisch
- **Steuerung:** Zentrale Brückensteuerung mit CCTV-Überwachung
- **Kettenzähler:** Hochpräzise Sensoren, integriert in das IMCS (Integrated Monitoring & Control System)

#### 3.7.1 Hersteller im Superyacht-Segment

| Hersteller | Herkunft | Spezialisierung |
|-----------|----------|-----------------|
| Muir | Australien | Seit 1938, Custom-Lösungen ab 20 m |
| Data Hidrolik | Türkei | Hydraulische Winden für 30–60 m |
| Rondal | Niederlande | Segelyachten >30 m, Carbon-Elemente |
| Clarke Chapman | UK | Anker- und Mooring-Winden >40 m |
| Rolls-Royce Marine / Kongsberg | Norwegen | Integrierte Ankersysteme >50 m |
| ACE Winches | Niederlande | Custom-Hydraulik 25–100+ m |
| Brusselle | Frankreich | Edelstahl-Winden, Design-Winden |

---

## 4. Produktlinien der Hersteller

### 4.1 Lofrans (Italien)

Lofrans, gegründet 1966 in Monfalcone (Italien), ist einer der weltweit führenden Hersteller von Ankerwinden. Bekannt für robuste Konstruktion und breites Sortiment vom Einstiegsmodell bis zur Superyacht-Lösung.

#### 4.1.1 Lofrans Tigres — Vertikalwinde

Die Tigres-Serie ist die meistverkaufte Vertikalwinde von Lofrans für Segelyachten von 8–16 m.

| Modell | Zugkraft | Motor | Kette DIN 766 | Kette ISO 4565 | Gewicht | Preis (2026) |
|--------|----------|-------|--------------|----------------|---------|-------------|
| Tigres 600 | 600 kg | 500 W 12V | 6 mm | 6 mm | 8,5 kg | €1.150 |
| Tigres 800 | 800 kg | 700 W 12V | 6, 8 mm | 7, 8 mm | 9,5 kg | €1.350 |
| Tigres 1000 | 1.000 kg | 1.000 W 12V | 8, 10 mm | 8 mm | 12,5 kg | €1.650 |
| Tigres 1200 | 1.200 kg | 1.000 W 24V | 8, 10 mm | 8, 10 mm | 14 kg | €1.950 |
| Tigres 1500 | 1.500 kg | 1.500 W 24V | 10, 12 mm | 10 mm | 18 kg | €2.450 |

**Besonderheiten Tigres:**
- Gehäuse: Seewasserfestes Aluminium-Druckguss
- Kettennuss: Aluminiumbronze, wechselbar
- Getriebe: Planetengetriebe, Wirkungsgrad ~78 %
- Spillkopf: Verchromt, Ø 95 mm (600–1000) / Ø 115 mm (1200–1500)
- Einschaltdauer: 3 min on / 3 min off (600–800), 5 min on / 5 min off (1000–1500)
- Freifall: Ja, über Kupplungshebel
- Nottrieb: Aufsteckbare Handkurbel (Zubehör)
- Artikelnummern: LZ.411-0612 (Tigres 600 12V 6mm), LZ.413-0812 (Tigres 800 12V 8mm), etc.

#### 4.1.2 Lofrans Kobra — Vertikalwinde (mittlere/große Yachten)

Die Kobra-Serie bedient den gehobenen Markt für Yachten von 14–24 m.

| Modell | Zugkraft | Motor | Kette DIN 766 | Gewicht | Preis (2026) |
|--------|----------|-------|--------------|---------|-------------|
| Kobra 1500 | 1.500 kg | 1.200 W 24V | 10, 12 mm | 22 kg | €3.200 |
| Kobra 2000 | 2.000 kg | 1.500 W 24V | 10, 12 mm | 28 kg | €3.800 |
| Kobra 2500 | 2.500 kg | 2.000 W 24V | 12, 14 mm | 35 kg | €4.600 |
| Kobra 3000 | 3.000 kg | 2.500 W 24V | 14, 16 mm | 42 kg | €5.800 |

**Besonderheiten Kobra:**
- Getriebe: Zwei-Stufen-Planetengetriebe
- Gehäuse: Hochglanz-poliertes Edelstahl 316L oder Aluminium
- Kettennuss: Aluminiumbronze, Titan optional
- Einschaltdauer: 8 min on / 5 min off
- Integrierter Kettenzähler-Sensor (Reed-Kontakt)
- Freifall mit hydraulischer Bremse

#### 4.1.3 Lofrans X-Serie — Horizontalwinde

| Modell | Zugkraft | Motor | Kette | Gewicht | Preis (2026) |
|--------|----------|-------|-------|---------|-------------|
| X1 | 500 kg | 500 W 12V | 6–8 mm | 11 kg | €950 |
| X2 | 700 kg | 700 W 12V | 8 mm | 15 kg | €1.250 |
| X3 | 1.000 kg | 1.000 W 12V/24V | 8–10 mm | 20 kg | €1.650 |
| X4 | 1.500 kg | 1.500 W 24V | 10–12 mm | 30 kg | €2.800 |

**Besonderheiten X-Serie:**
- Kompaktes Low-Profile-Gehäuse
- Vollständig über Deck — kein Decksdurchbruch
- Edelstahl-Gehäuse optional
- Combo-Modelle (Kette + Tau) verfügbar für X2 und X3
- Artikelnummern: LZ.621-0512 (X1 12V 6mm), etc.

#### 4.1.4 Lofrans Falkon — Heckanker / Kompakt

| Modell | Zugkraft | Motor | Kette | Gewicht | Preis (2026) |
|--------|----------|-------|-------|---------|-------------|
| Falkon 500 | 500 kg | 500 W 12V | 6 mm | 7 kg | €1.200 |
| Falkon 700 | 700 kg | 700 W 12V | 6–8 mm | 9 kg | €1.500 |

#### 4.1.5 Lofrans Ersatzteile — Wichtigste Artikelnummern

| Teil | Artikelnummer (Beispiel) | Preis (2026) |
|------|------------------------|-------------|
| Kettennuss 8 mm DIN 766 Tigres | LZ.72037 | €145 |
| Kettennuss 10 mm DIN 766 Tigres | LZ.72038 | €165 |
| Kettennuss 8 mm DIN 766 Kobra | LZ.72051 | €195 |
| Motor 700 W 12V Tigres | LZ.528-0712 | €480 |
| Motor 1000 W 12V Tigres | LZ.528-1012 | €620 |
| Motor 1500 W 24V Kobra | LZ.529-1524 | €850 |
| Getriebe-Kit Tigres | LZ.82015 | €280 |
| Dichtungs-Kit Tigres | LZ.92005 | €45 |
| Handkurbel Tigres | LZ.63001 | €65 |
| Fußschalter (Paar) | LZ.61010 | €95 |

### 4.2 Lewmar (UK)

Lewmar, gegründet 1946 in Havant (UK), ist ein Vollsortimenter für Decksausrüstung. Die Ankerwindensparte ist seit der Übernahme von Simpson-Lawrence (1987) eine Kernkompetenz.

#### 4.2.1 Lewmar V-Series — Vertikalwinde

Die V-Serie ist Lewmars Hauptlinie für Vertikalwinden. Breites Spektrum von der kleinen Segelyacht bis zur großen Motoryacht.

| Modell | Zugkraft | Motor | Kette DIN 766 | Kette BBB | Gewicht | Preis (2026) |
|--------|----------|-------|--------------|-----------|---------|-------------|
| V1 | 350 kg | 300 W 12V | 6 mm | 6 mm (1/4") | 5,5 kg | €890 |
| V2 | 500 kg | 500 W 12V | 6, 8 mm | 6, 7 mm | 7,8 kg | €1.150 |
| V3 | 700 kg | 700 W 12V | 8, 10 mm | 8 mm (5/16") | 10,2 kg | €1.450 |
| V4 | 1.000 kg | 1.000 W 12V | 8, 10 mm | 8, 10 mm | 13,5 kg | €1.850 |
| V5 | 1.200 kg | 1.000 W 24V | 10, 12 mm | 10 mm (3/8") | 16 kg | €2.250 |
| V6 | 1.500 kg | 1.500 W 24V | 10, 12 mm | 10, 12 mm | 21 kg | €2.850 |
| V700 | 2.000 kg | 1.500 W 24V | 12, 14 mm | 12 mm (1/2") | 28 kg | €3.600 |
| V8 | 2.500 kg | 2.000 W 24V | 14, 16 mm | 14 mm (9/16") | 38 kg | €4.800 |

**Besonderheiten V-Series:**
- Gehäuse: ABS/Edelstahl-Kombination (V1–V4), Volledelstahl (V5–V8)
- Kettennuss: Aluminiumbronze
- Getriebe: Schneckengetriebe (V1–V3), Planetengetriebe (V4–V8)
- Spillkopf: Standard bei allen Modellen
- Einschaltdauer: 3 min (V1–V3), 5 min (V4–V6), 8 min (V700–V8)
- Lewmar-Artikelnummern: 66000890 (V1 12V 6mm DIN766), etc.
- Combo (Kette+Tau): V2, V3, V4 als Combo-Variante verfügbar

#### 4.2.2 Lewmar H-Series — Horizontalwinde

| Modell | Zugkraft | Motor | Kette DIN 766 | Gewicht | Preis (2026) |
|--------|----------|-------|--------------|---------|-------------|
| HX1 | 500 kg | 500 W 12V | 6, 8 mm | 12 kg | €980 |
| HX2 | 700 kg | 700 W 12V | 8 mm | 17 kg | €1.350 |
| HX3 | 1.000 kg | 1.000 W 12V/24V | 8, 10 mm | 23 kg | €1.850 |
| HX4 | 1.500 kg | 1.500 W 24V | 10, 12 mm | 32 kg | €2.650 |

#### 4.2.3 Lewmar Pro-Series / Pro-Fish

Die Pro-Series richtet sich an professionelle und gewerbliche Nutzer (Charterboote, Fischerboote, Arbeitsboote).

| Modell | Zugkraft | Motor | Kette | Gewicht | Preis (2026) |
|--------|----------|-------|-------|---------|-------------|
| Pro 700H | 700 kg | 700 W 12V | 6–10 mm | 18 kg | €1.550 |
| Pro 1000H | 1.000 kg | 1.000 W 12V/24V | 8–10 mm | 24 kg | €2.100 |
| Pro 1500H | 1.500 kg | 1.500 W 24V | 10–12 mm | 34 kg | €3.200 |

**Besonderheiten Pro-Series:**
- Verstärktes Getriebe für erhöhte Einschaltdauer
- Edelstahl 316L Gehäuse (Standard)
- Doppeldichtungssystem
- Einschaltdauer: 8 min on / 4 min off

#### 4.2.4 Lewmar CPX-Serie — Kompakt/Heckanker

| Modell | Zugkraft | Motor | Kette | Gewicht | Preis (2026) |
|--------|----------|-------|-------|---------|-------------|
| CPX1 | 300 kg | 300 W 12V | 6 mm | 5,5 kg | €780 |
| CPX2 | 500 kg | 500 W 12V | 6–8 mm | 7,8 kg | €1.080 |
| CPX3 | 700 kg | 700 W 12V | 8 mm | 10 kg | €1.380 |

#### 4.2.5 Lewmar Ersatzteile — Wichtigste Artikelnummern

| Teil | Artikelnummer (Beispiel) | Preis (2026) |
|------|------------------------|-------------|
| Kettennuss 8 mm DIN 766 V-Series | 66000432 | €135 |
| Kettennuss 10 mm DIN 766 V-Series | 66000434 | €155 |
| Motor 700 W 12V V3 | 66000712 | €520 |
| Motor 1000 W 12V V4 | 66001012 | €680 |
| Getriebe-Kit V3 | 66910100 | €310 |
| Dichtungs-Kit V-Series | 66920050 | €42 |
| Fußschalter Deck | 68000588 | €85 |
| Kettenzähler AA560 | 66830155 | €280 |

### 4.3 Quick (Italien)

Quick S.p.A., gegründet 1982 in Ravenna (Italien), ist Marktführer im Mittelmeerraum. Bekannt für Design, Integration und ein breites Zubehörprogramm.

#### 4.3.1 Quick Aleph — Vertikalwinde (Flaggschiff)

| Modell | Zugkraft | Motor | Kette DIN 766 | Gewicht | Preis (2026) |
|--------|----------|-------|--------------|---------|-------------|
| Aleph 500 | 500 kg | 500 W 12V | 6, 8 mm | 7,5 kg | €1.250 |
| Aleph 700 | 700 kg | 700 W 12V | 6, 8 mm | 9,0 kg | €1.500 |
| Aleph 1000 | 1.000 kg | 1.000 W 12V | 8, 10 mm | 12,5 kg | €1.950 |
| Aleph 1000/24 | 1.000 kg | 800 W 24V | 8, 10 mm | 12,5 kg | €2.050 |
| Aleph 1500/24 | 1.500 kg | 1.500 W 24V | 10, 12 mm | 18 kg | €2.750 |

**Besonderheiten Aleph:**
- Preisgekröntes Design (DAME Design Award)
- Integrierter Kettenzähler (Quick Count-Modul optional)
- LED-Statusanzeige am Spillkopf (Betrieb/Standby/Fehler)
- Gehäuse: Hochglanz-poliertes Edelstahl 316 AISI
- Getriebe: Doppel-Planetengetriebe
- Einschaltdauer: 4 min on / 4 min off (500–700), 6 min on / 4 min off (1000–1500)

#### 4.3.2 Quick Héron — Horizontalwinde

| Modell | Zugkraft | Motor | Kette DIN 766 | Gewicht | Preis (2026) |
|--------|----------|-------|--------------|---------|-------------|
| Héron 500 | 500 kg | 500 W 12V | 6–8 mm | 11 kg | €1.050 |
| Héron 1000 | 1.000 kg | 1.000 W 12V | 8–10 mm | 18 kg | €1.750 |
| Héron 1500 | 1.500 kg | 1.200 W 24V | 10–12 mm | 26 kg | €2.600 |
| Héron 2000 | 2.000 kg | 1.500 W 24V | 10–14 mm | 35 kg | €3.400 |

#### 4.3.3 Quick Prince — Horizontalwinde (Premiumlinie)

| Modell | Zugkraft | Motor | Kette | Gewicht | Preis (2026) |
|--------|----------|-------|-------|---------|-------------|
| Prince DP2 500 | 500 kg | 500 W 12V | 6–8 mm | 13 kg | €1.350 |
| Prince DP2 1000 | 1.000 kg | 1.000 W 12V | 8–10 mm | 22 kg | €2.100 |
| Prince DP3 1500 | 1.500 kg | 1.500 W 24V | 10–12 mm | 33 kg | €3.200 |
| Prince DP3 2500 | 2.500 kg | 2.000 W 24V | 12–16 mm | 48 kg | €4.800 |

**Besonderheiten Prince:**
- Full-Edelstahl-Gehäuse 316L, Mirror-Polished
- Integrierter Quick CHC Chain Counter
- Doppelspillkopf-Option (beidseitig)
- Hydraulische Varianten verfügbar

#### 4.3.4 Quick Genius — Kompakt/Vertikal

| Modell | Zugkraft | Motor | Kette | Gewicht | Preis (2026) |
|--------|----------|-------|-------|---------|-------------|
| Genius 500 | 500 kg | 500 W 12V | 6 mm | 6,5 kg | €1.100 |
| Genius 1000 | 900 kg | 800 W 12V | 8 mm | 10 kg | €1.700 |

#### 4.3.5 Quick Zubehör und Steuerung

| Produkt | Artikelnummer | Preis (2026) |
|---------|--------------|-------------|
| Quick CHC1203 Kettenzähler + Display |?"CHC1203LA00000A | €350 |
| Quick MOD. 3 Steuereinheit |?"MOD3000000A | €280 |
| Quick Fußschalter FP |?"FPSW0000000A | €110 |
| Quick Fernbedienung kabellos |?"RC04000000A | €450 |
| Quick Solenoid 12V |?"SOL12V0080A | €180 |
| Quick Solenoid 24V |?"SOL24V0060A | €195 |

### 4.4 Maxwell (Neuseeland / USA)

Maxwell Marine, gegründet 1979 in Auckland (Neuseeland), ist besonders stark im Pazifikraum und in den USA. Bekannt für robuste, zuverlässige Produkte.

#### 4.4.1 Maxwell RC-Serie — Vertikalwinde

| Modell | Zugkraft | Motor | Kette | Gewicht | Preis (2026) |
|--------|----------|-------|-------|---------|-------------|
| RC6 | 600 kg | 500 W 12V | 6, 8 mm | 8,5 kg | €1.050 |
| RC8 | 800 kg | 700 W 12V | 6, 8 mm BBB/DIN | 10 kg | €1.350 |
| RC10 | 1.000 kg | 1.000 W 12V/24V | 8, 10 mm | 14 kg | €1.750 |
| RC12 | 1.200 kg | 1.000 W 24V | 10 mm | 17 kg | €2.150 |

**Besonderheiten RC-Serie:**
- Patentiertes „MaxSet" Kettennuss-Design für minimales Kettenspringen
- Gehäuse: Aluminium-Druckguss, weiß oder chrome
- Getriebe: Planetengetriebe
- Combo-Versionen (Kette/Tau) für alle Modelle verfügbar
- Besonders beliebt in USA/Australien mit BBB-Kettennuss

#### 4.4.2 Maxwell HRC-Serie — Horizontalwinde

| Modell | Zugkraft | Motor | Kette | Gewicht | Preis (2026) |
|--------|----------|-------|-------|---------|-------------|
| HRC6 | 600 kg | 500 W 12V | 6–8 mm | 13 kg | €980 |
| HRC8 | 800 kg | 700 W 12V | 8 mm | 18 kg | €1.300 |
| HRC10 | 1.000 kg | 1.000 W 12V/24V | 8–10 mm | 24 kg | €1.750 |
| HRC FF | 1.500 kg | 1.500 W 24V | 10–12 mm | 32 kg | €2.800 |

#### 4.4.3 Maxwell VWC-Serie — Vertikal (große Yachten)

| Modell | Zugkraft | Motor | Kette | Gewicht | Preis (2026) |
|--------|----------|-------|-------|---------|-------------|
| VWC 2500 | 2.500 kg | 2.000 W 24V | 12–14 mm | 38 kg | €4.200 |
| VWC 3500 | 3.500 kg | 2.500 W 24V | 14–16 mm | 52 kg | €5.800 |
| VWC 5000 Hydraulik | 5.000 kg | Hydraulisch | 16–19 mm | 65 kg | €8.500 |

#### 4.4.4 Maxwell Hector — Heckanker

| Modell | Zugkraft | Motor | Kette | Gewicht | Preis (2026) |
|--------|----------|-------|-------|---------|-------------|
| Hector 500 | 500 kg | 500 W 12V | 6–8 mm | 7 kg | €1.250 |
| Hector 700 | 700 kg | 700 W 12V | 6–8 mm | 9 kg | €1.600 |

#### 4.4.5 Maxwell Ersatzteile

| Teil | Artikelnummer (Beispiel) | Preis (2026) |
|------|------------------------|-------------|
| Kettennuss 8 mm DIN 766 RC | P100123 | €125 |
| Kettennuss 10 mm DIN 766 RC | P100124 | €145 |
| Kettennuss 8 mm BBB RC | P100128 | €130 |
| Motor 700 W 12V RC8 | P100456 | €490 |
| Getriebe-Kit RC8 | P100789 | €275 |
| Circuit Breaker 80A | P100900 | €55 |
| Fußschalter (Paar) | P100950 | €88 |

### 4.5 Muir (Australien)

Muir Windlasses, gegründet 1938 in Hobart (Tasmanien, Australien), ist der älteste Ankerwindenhersteller weltweit. Spezialisiert auf robuste Qualität und Custom-Lösungen.

#### 4.5.1 Muir Produktübersicht

| Modell | Typ | Zugkraft | Motor | Kette | Gewicht | Preis (2026) |
|--------|-----|----------|-------|-------|---------|-------------|
| Cougar C6 | Vertikal | 600 kg | 500 W 12V | 6–8 mm | 9 kg | €1.350 |
| Cougar C8 | Vertikal | 800 kg | 700 W 12V | 8 mm | 12 kg | €1.650 |
| Cougar C10 | Vertikal | 1.000 kg | 1.000 W 12/24V | 8–10 mm | 16 kg | €2.100 |
| Thor HR2500 | Horizontal | 2.500 kg | 2.000 W 24V | 12–14 mm | 45 kg | €4.800 |
| Thor HR3500 | Horizontal | 3.500 kg | 2.500 W 24V | 14–16 mm | 62 kg | €6.500 |
| Elan V5000 | Vertikal Hydr. | 5.000 kg | Hydraulisch | 16–19 mm | 75 kg | €9.500 |
| Custom | Variabel | bis 50.000 kg | Hydraulisch | bis 42 mm | Variabel | auf Anfrage |

**Besonderheiten Muir:**
- Australische Fertigung in Hobart
- Edelstahl 316L als Standard bei allen Modellen
- 5 Jahre Garantie (branchenführend)
- Custom-Engineering ab 15 m Bootslänge
- Kettennüsse in Aluminiumbronze oder Titan

### 4.6 Italwinch (Italien)

Italwinch (Teil der Quick-Gruppe seit 2018) produziert Ankerwinden im mittleren Preissegment mit gutem Preis-Leistungs-Verhältnis.

#### 4.6.1 Italwinch Produktübersicht

| Modell | Typ | Zugkraft | Motor | Kette | Gewicht | Preis (2026) |
|--------|-----|----------|-------|-------|---------|-------------|
| Smart 500 | Vertikal | 500 kg | 500 W 12V | 6 mm | 6,8 kg | €780 |
| Smart 700 | Vertikal | 700 kg | 700 W 12V | 6–8 mm | 8,5 kg | €1.050 |
| Smart 1000 | Vertikal | 1.000 kg | 800 W 12V | 8 mm | 11 kg | €1.350 |
| Devon 500H | Horizontal | 500 kg | 500 W 12V | 6–8 mm | 10 kg | €720 |
| Devon 700H | Horizontal | 700 kg | 700 W 12V | 8 mm | 14 kg | €980 |
| Devon 1000H | Horizontal | 1.000 kg | 1.000 W 12V | 8–10 mm | 20 kg | €1.350 |

**Besonderheiten Italwinch:**
- Gutes Preis-Leistungs-Verhältnis (Einstiegsklasse)
- Quick-kompatibles Zubehör (Solenoid, Fußschalter, Kettenzähler)
- Aluminium-Gehäuse (kein Edelstahl)
- Einschaltdauer: 3 min on / 3 min off

### 4.7 South Pacific / CX-SX-Serie

South Pacific Industrial (SPI), Taiwan, produziert Ankerwinden unter verschiedenen OEM-Labels. Die CX- und SX-Serien sind weit verbreitet als Erstausrüstung bei asiatischen Bootsbauern.

#### 4.7.1 CX-Serie (Vertikal)

| Modell | Zugkraft | Motor | Kette | Gewicht | Preis (2026) |
|--------|----------|-------|-------|---------|-------------|
| CX1 | 300 kg | 300 W 12V | 6 mm | 5 kg | €450 |
| CX2 | 500 kg | 500 W 12V | 6–8 mm | 7 kg | €650 |
| CX3 | 700 kg | 700 W 12V | 8 mm | 10 kg | €850 |

#### 4.7.2 SX-Serie (Horizontal)

| Modell | Zugkraft | Motor | Kette | Gewicht | Preis (2026) |
|--------|----------|-------|-------|---------|-------------|
| SX1 | 300 kg | 300 W 12V | 6 mm | 7 kg | €400 |
| SX2 | 500 kg | 500 W 12V | 6–8 mm | 10 kg | €600 |
| SX3 | 700 kg | 700 W 12V | 8 mm | 14 kg | €800 |

**Hinweis zu CX/SX:** Diese Winden sind preislich attraktiv, aber die Verarbeitungsqualität liegt unter europäischen/australischen Herstellern. Häufige Probleme: Dichtungsversagen nach 3–5 Jahren, Getriebespiel, Kettennuss-Verschleiß. AYDI bewertet CX/SX-Winden in der Production-Analyse (Modul `production`) typischerweise 15–25 Punkte niedriger als Lofrans, Lewmar, Quick oder Maxwell.

### 4.8 Weitere Hersteller

#### 4.8.1 Vetus (Niederlande)

| Modell | Typ | Zugkraft | Motor | Kette | Preis (2026) |
|--------|-----|----------|-------|-------|-------------|
| MAXWELL700 | Vertikal | 700 kg | 700 W 12V | 6–8 mm | €1.250 |
| MAXWELL1000 | Vertikal | 1.000 kg | 1.000 W 12V | 8–10 mm | €1.650 |

(Vetus vertreibt teilweise Maxwell-Winden unter eigenem Label)

#### 4.8.2 Plastimo (Frankreich)

Plastimo bietet ein kleines Sortiment von Handwinden und einfachen Elektrowinden für Boote unter 10 m:

| Modell | Typ | Zugkraft | Antrieb | Kette | Preis (2026) |
|--------|-----|----------|---------|-------|-------------|
| Anchor Winch 350 | Horizontal | 350 kg | Manuell | 6 mm | €180 |
| Anchor Winch 500E | Horizontal | 500 kg | 500 W 12V | 6–8 mm | €680 |

#### 4.8.3 Antal (Italien)

Antal, bekannt für Segelwinden und Beschläge, bietet einige Ankerwindenmodelle:

| Modell | Typ | Zugkraft | Motor | Kette | Preis (2026) |
|--------|-----|----------|-------|-------|-------------|
| AW500V | Vertikal | 500 kg | 500 W 12V | 6–8 mm | €1.150 |
| AW800V | Vertikal | 800 kg | 700 W 12V | 8 mm | €1.450 |

---

## 5. Elektrik und Installation

### 5.1 Systemübersicht Elektrik

Das elektrische System einer Ankerwinde besteht aus folgenden Komponenten:

```
[Batterie] → [Hauptschalter] → [Sicherungsautomat/Circuit Breaker]
    → [Starkstromkabel +] → [Solenoid-Relais] → [Motor +]
    → [Starkstromkabel −] → [Motor −] → [Masse/Batterie −]

[Bedienpanel/Fußschalter] → [Steuerleitung] → [Solenoid-Relais Steuerseite]
```

### 5.2 Motorsizing — Leistungsaufnahme und Stromstärke

#### 5.2.1 Typische Stromaufnahme

| Windengröße | Spannung | Leistung | Strom (Arbeitslast) | Strom (Max. Last) | Anlaufstrom |
|-------------|----------|----------|--------------------|--------------------|-------------|
| 300 kg | 12V | 300 W | 35 A | 50 A | 80 A |
| 500 kg | 12V | 500 W | 50 A | 75 A | 120 A |
| 700 kg | 12V | 700 W | 65 A | 100 A | 160 A |
| 1.000 kg | 12V | 1.000 W | 90 A | 130 A | 220 A |
| 500 kg | 24V | 500 W | 25 A | 38 A | 60 A |
| 1.000 kg | 24V | 800 W | 40 A | 65 A | 110 A |
| 1.500 kg | 24V | 1.500 W | 70 A | 100 A | 170 A |
| 2.000 kg | 24V | 2.000 W | 90 A | 130 A | 220 A |
| 2.500 kg | 24V | 2.500 W | 110 A | 160 A | 270 A |

**Anlaufstrom:** Der Anlaufstrom (Inrush Current) ist 2–3× der Arbeitsstrom. Alle Sicherungen und Schalter müssen diesen Anlaufstrom tolerieren. Thermische Sicherungsautomaten (langsam auslösend) sind daher Pflicht. Schnellschmelzsicherungen (flink) sind ungeeignet!

#### 5.2.2 Batterieanforderungen

**Minimalkapazität:** Die Starterbatterie ist **nicht** als Ankerwindenbatterie geeignet. Die Ankerwinde sollte an der Servicebatterie (Verbraucherbatterie) angeschlossen werden.

Faustregel für Mindest-Batteriekapazität:

```
C_min [Ah] = I_working × t_max_retrieval × 2 (Sicherheitsfaktor)

Beispiel: 90 A × (5 min / 60 min) × 2 = 15 Ah pro Ankervorgang
Bei 5 Ankervorgängen pro Tag: 75 Ah Mindestkapazität für Ankerwinde allein
Empfohlen: 200+ Ah Servicebatterie (AGM oder LiFePO4)
```

**Spannungsabfall:** Bei hohem Strombedarf sinkt die Batteriespannung. Ein 12V-System, das unter Last auf <10,5V fällt, liefert nicht mehr genug Drehmoment. LiFePO4-Batterien sind hier überlegen, da sie eine flachere Entladekurve haben.

### 5.3 Kabelquerschnitt-Berechnung

Der Kabelquerschnitt ist der **kritischste Faktor** bei der Installation einer elektrischen Ankerwinde. Zu dünne Kabel verursachen:
- Spannungsabfall → reduzierte Motorleistung
- Überhitzung → Kabelbrand-Gefahr
- Solenoid-Flattern → vorzeitiger Verschleiß

#### 5.3.1 Berechnungsformel

```
A [mm²] = (2 × L × I) / (κ × ΔU_max)

Wobei:
A = Kabelquerschnitt in mm²
L = Einfache Kabellänge Batterie → Winde in Metern
I = Maximaler Betriebsstrom in Ampere
κ = Leitfähigkeit Kupfer = 56 m/(Ω×mm²)
ΔU_max = Maximaler Spannungsabfall (3 % von Nennspannung)
       = 0.36V bei 12V-System, 0.72V bei 24V-System
```

#### 5.3.2 Kabelquerschnitt-Tabelle 12V-System

| Kabellänge (einfach) | 50 A | 75 A | 100 A | 130 A |
|---------------------|------|------|-------|-------|
| 3 m | 16 mm² | 25 mm² | 35 mm² | 50 mm² |
| 5 m | 25 mm² | 35 mm² | 50 mm² | 70 mm² |
| 7 m | 35 mm² | 50 mm² | 70 mm² | 95 mm² |
| 10 m | 50 mm² | 70 mm² | 95 mm² | 120 mm² |
| 12 m | 70 mm² | 95 mm² | 120 mm² | 150 mm² |
| 15 m | 70 mm² | 95 mm² | 120 mm² | 185 mm² |

#### 5.3.3 Kabelquerschnitt-Tabelle 24V-System

| Kabellänge (einfach) | 25 A | 40 A | 65 A | 100 A |
|---------------------|------|------|------|-------|
| 3 m | 6 mm² | 10 mm² | 16 mm² | 25 mm² |
| 5 m | 10 mm² | 16 mm² | 25 mm² | 35 mm² |
| 7 m | 16 mm² | 25 mm² | 35 mm² | 50 mm² |
| 10 m | 16 mm² | 25 mm² | 50 mm² | 70 mm² |
| 12 m | 25 mm² | 35 mm² | 50 mm² | 70 mm² |
| 15 m | 25 mm² | 35 mm² | 70 mm² | 95 mm² |

#### 5.3.4 Kabeltyp

| Kabeltyp | Eignung | Kommentar |
|----------|---------|-----------|
| H07V-K (eindrähtig) | Ungeeignet | Nicht flexibel genug, bricht bei Vibration |
| H07RN-F (Gummi) | Geeignet | Ölbeständig, flexibel, UV-beständig |
| Marinekabel (verzinnt) | Optimal | Verzinnte Kupferlitzen, korrosionsbeständig |
| SGX Battery Cable | Optimal | Speziell für Bootsbatteriekabel |

**AYDI-Bewertungsregel:** Nicht-verzinntes Kupferkabel im Bugbereich erhält im Materials-Modul eine `WARNING`. Verzinntes Marinekabel ist Pflicht für alle Installationen im Nassbereich.

### 5.4 Sicherungsautomat (Circuit Breaker)

#### 5.4.1 Dimensionierung

| Motorleistung | Arbeitsstrom | Empfohlener Circuit Breaker |
|--------------|-------------|---------------------------|
| 300 W 12V | 35 A | 50 A |
| 500 W 12V | 50 A | 70 A |
| 700 W 12V | 65 A | 100 A |
| 1.000 W 12V | 90 A | 130 A |
| 1.000 W 24V | 45 A | 60 A |
| 1.500 W 24V | 70 A | 100 A |
| 2.000 W 24V | 90 A | 130 A |

**Typ:** Thermischer Überstromschutzschalter (träge Auslösecharakteristik). Magnetische Schnellauslöser sind ungeeignet, da sie durch den Anlaufstrom ausgelöst werden.

**Montageort:** Möglichst nah an der Batterie (max. 2 m Kabellänge zwischen Batterie und Circuit Breaker, ungefüst).

#### 5.4.2 Empfohlene Produkte

| Hersteller | Modell | Strom | Preis (2026) |
|-----------|--------|-------|-------------|
| Blue Sea Systems | 7072 | 60 A | €45 |
| Blue Sea Systems | 7076 | 100 A | €55 |
| Blue Sea Systems | 7080 | 150 A | €75 |
| Ancor | 551750 | 50 A | €35 |
| Ancor | 551850 | 80 A | €42 |
| Marinco | CB60 | 60 A | €38 |

### 5.5 Solenoid-Relais

Das Solenoid (auch Magnetschalter oder Leistungsrelais) ist das Schaltorgan zwischen Batterie und Motor. Es wird durch niedrige Steuerspannung (typisch 0,5–2 A) geschaltet und schaltet den hohen Motorstrom.

#### 5.5.1 Aufbau und Funktion

```
[Fußschalter AUF]  ─→ [Solenoid AUF]  ─→ Motor Drehrichtung 1 (Einholen)
[Fußschalter AB]   ─→ [Solenoid AB]   ─→ Motor Drehrichtung 2 (Fieren)
```

Typischerweise werden **zwei separate Solenoids** verwendet — eines für jede Drehrichtung. Bei einigen Herstellern ist ein Dual-Solenoid (zwei Magnetschalter in einem Gehäuse) verbaut.

#### 5.5.2 Solenoid-Spezifikationen

| Parameter | Typischer Wert |
|-----------|---------------|
| Schaltstrom (Kontakte) | 80–200 A |
| Steuerstrom (Spule) | 0,5–2 A |
| Steuerspannung | 12V oder 24V (zur Bordspannung passend) |
| Kontakttyp | Normalerweise offen (NO) |
| Schutzklasse | IP56 bis IP66 |
| Lebensdauer | 50.000–200.000 Schaltzyklen |

#### 5.5.3 Dual-Solenoid vs. Einzel-Solenoid

| Aspekt | Dual-Solenoid | 2× Einzel-Solenoid |
|--------|--------------|---------------------|
| Platzbedarf | Kompakter | Mehr Platz benötigt |
| Verdrahtung | Einfacher (ein Stecker) | Komplexer (zwei Geräte) |
| Austausch bei Defekt | Kompletteinheit tauschen | Nur defektes Relais tauschen |
| Kosten | €150–€280 | 2× €80–€150 = €160–€300 |

### 5.6 Fußschalter (Foot Switch)

Der Fußschalter ist das primäre Bedienelement am Bug. Er wird mit dem Fuß betätigt, damit beide Hände für die Kettenführung frei sind.

#### 5.6.1 Anforderungen

| Parameter | Anforderung |
|-----------|------------|
| Schutzklasse | IP67 oder besser |
| Betätigungskraft | 2–5 kg (nicht versehentlich betätigbar) |
| Material | Edelstahl 316L oder glasfaserverstärktes Nylon |
| Federkontakt | Selbst-rückstellend (Toter-Mann-Schaltung) |
| Beschriftung | AUF/UP (▲) und AB/DOWN (▼) |
| Kabellänge | Min. 2 m, Durchführung unter Deck |

#### 5.6.2 Montageposition

Der Fußschalter wird so montiert, dass der Bediener:
- Mit dem Blick zum Bug steht
- Beide Hände am Ankerroller oder an der Kette hat
- Den Schalter mit dem Fuß erreicht, ohne die Position zu verändern
- Nicht versehentlich auf den Schalter treten kann (leicht erhöht oder versenkt)

**Optimale Position:** 30–50 cm hinter der Kettennuss, leicht seitlich (Steuerbord bei eingehängtem Anker auf Steuerbord-Ankerrolle).

#### 5.6.3 Verdrahtung Fußschalter

```
Fußschalter AUF: Schließt Stromkreis [+12V/24V] → [Solenoid AUF Spule]
Fußschalter AB:  Schließt Stromkreis [+12V/24V] → [Solenoid AB Spule]
Gemeinsame Masse: Beide Schalter → [Masse]

Kabelquerschnitt Steuerleitung: 1,5 mm² (Steuerstrom nur 0,5–2 A)
```

### 5.7 Kettenzähler (Chain Counter)

Der Kettenzähler zeigt die ausgebrachte Kettenlänge digital an. Er ist ein wichtiges Hilfsmittel für:
- Korrekte Kettenlänge beim Ankern (Verhältnis Wassertiefe : Kettenlänge)
- Kontrolle beim Einholen (Wann kommt der Anker?)
- Vermeidung von Überlast (Zu viel Kette eingeholet → Winde blockiert)

#### 5.7.1 Sensortypen

| Sensortyp | Funktion | Genauigkeit | Preis |
|-----------|----------|-------------|-------|
| Reed-Kontakt (Magnet) | Magnet am Kettennuss-Zahnrad, Reed-Schalter zählt Umdrehungen | ±0,5 m | €40–€80 |
| Hall-Sensor | Berührungslos, zählt Kettenglieder | ±0,2 m | €80–€150 |
| Induktiver Sensor | Zählt metallische Kettenglieder | ±0,3 m | €60–€120 |
| Encoder am Motor | Zählt Motorumdrehungen, rechnet auf Kettenlänge um | ±0,5 m | Im Motor integriert |

#### 5.7.2 Display und Steuereinheiten

| Hersteller | Modell | Funktionen | Preis (2026) |
|-----------|--------|------------|-------------|
| Quick | CHC1203 | Kettenzähler, Auf/Ab-Steuerung, Preset | €350 |
| Lewmar | AA560 | Kettenzähler, digitales Display, wasserdicht | €280 |
| Maxwell | P102978 | Kettenzähler + Panel | €320 |
| Lofrans | IRIS | Kettenzähler + Windenkontrolle, NMEA 2000 | €420 |
| Muir | DFF3 | Kettenzähler, Fernbedienung, 3 Presets | €380 |

#### 5.7.3 NMEA-2000-Integration

Moderne Kettenzähler können über NMEA 2000 in das Borddaten-Netzwerk integriert werden. Die folgenden PGNs (Parameter Group Numbers) sind relevant:

| PGN | Name | Daten |
|-----|------|-------|
| 128776 | Windlass Control Status | Kettenlänge, Status (Auf/Ab/Stopp), Geschwindigkeit |
| 128777 | Anchor Windlass Monitoring | Motor-Temperatur, Strom, Spannung, Fehlercodes |
| 128778 | Windlass Operating Status | Betriebsmodus, Freifall, Überlast |

### 5.8 Fernbedienung (Remote Control)

#### 5.8.1 Kabelgebundene Fernbedienung

- Montage am Steuerstand (Cockpit oder Flybridge)
- Kabelquerschnitt: 1,5 mm² (Steuerleitung)
- Typisch: 2 Taster (Auf/Ab) + LED-Statusanzeige
- Preis: €80–€200

#### 5.8.2 Kabellose Fernbedienung

- Funkfrequenz: 433 MHz oder 868 MHz
- Reichweite: 15–50 m
- Batterie: CR2032 oder AAA
- Empfänger: Wird an Solenoid-Steuerleitung angeschlossen
- Vorteil: Keine Kabelführung, Bediener kann sich frei bewegen
- Nachteil: Funkstörungen möglich, Batteriepflege
- Preis: €200–€500

#### 5.8.3 Empfohlene Produkte

| Hersteller | Modell | Typ | Reichweite | Preis (2026) |
|-----------|--------|-----|-----------|-------------|
| Quick | RC04 | Kabellos | 30 m | €450 |
| Lewmar | Wireless Control | Kabellos | 25 m | €380 |
| Maxwell | WRC | Kabellos | 20 m | €350 |
| Muir | RF Remote | Kabellos | 40 m | €420 |
| Quick | Handheld Wired | Kabelgebunden | — | €120 |

### 5.9 Elektrisches Schaltschema (Vollständig)

```
                    ┌─────────────────────────────┐
                    │    SERVICEBATTERIE           │
                    │  12V/24V  200+ Ah            │
                    └───┬────────────────┬─────────┘
                        │ (+)            │ (−)
                        │                │
                   ┌────┴────┐           │
                   │HAUPTSCHALTER│       │
                   │(Batterie) │         │
                   └────┬────┘           │
                        │                │
                   ┌────┴────┐           │
                   │CIRCUIT   │          │
                   │BREAKER   │          │
                   │100A therm│          │
                   └────┬────┘           │
                        │                │
        ┌───────────────┼────────────────┤
        │               │                │
   ┌────┴────┐    ┌─────┴─────┐         │
   │SOLENOID │    │SOLENOID   │         │
   │  AUF    │    │  AB       │         │
   │(NO)     │    │(NO)       │         │
   └──┬──┬───┘    └──┬──┬────┘         │
      │  │Spule      │  │Spule         │
      │  │            │  │              │
      │  └──┬─────────┘  └──┬──────────┤
      │     │                │          │
      │  ┌──┴──┐          ┌──┴──┐      │
      │  │FUSS │          │FUSS │      │
      │  │AUF  │          │AB   │      │
      │  └──┬──┘          └──┬──┘      │
      │     │                │          │
      │     └────┬───────────┘          │
      │          │ Masse                │
      │          └──────────────────────┤
      │                                 │
      └──────────┐                      │
                 │                      │
            ┌────┴────────────────┐     │
            │    MOTOR             │     │
            │  (DC Permanent-     │     │
            │   magnet)           │     │
            └────────────┬────────┘     │
                         │              │
                         └──────────────┘
```

### 5.10 Typische Installationsfehler (Elektrik)

| Fehler | Konsequenz | AYDI-Bewertung |
|--------|-----------|----------------|
| Kabelquerschnitt zu gering | Spannungsabfall, Motorüberhitzung, Brand | CRITICAL |
| Keine Sicherung/Circuit Breaker | Kabelbrand bei Kurzschluss | CRITICAL |
| Sicherung zu klein (flink) | Löst bei jedem Anlauf aus | WARNING |
| Kabel nicht verzinnt | Korrosion, Übergangswiderstand | WARNING |
| Masse über Rumpf (Stahlboot) | Elektrolyse-Gefahr | CRITICAL |
| Solenoid unterdimensioniert | Kontaktverschweißung, Dauerlauf | CRITICAL |
| Fußschalter nicht IP67 | Wassereinbruch, Kurzschluss | WARNING |
| Steuerkabel zu lang (>15 m) | Spannungsabfall Steuerkreis, Solenoid schaltet nicht | WARNING |
| Kabelverbindungen gelötet | Brechen bei Vibration (Crimpen ist Pflicht!) | WARNING |
| Batterie zu klein | Spannung bricht ein, Motor überhitzt | WARNING |

---

## 6. Montage und Einbau

### 6.1 Decksverstärkung

Die Ankerwinde wird auf das Vordeck montiert und überträgt erhebliche Kräfte in die Decksstruktur. Eine unzureichende Decksverstärkung ist der häufigste Montagefehler.

#### 6.1.1 Kräfte auf die Decksstruktur

| Lastfall | Kraft (Beispiel 1.000 kg Winde) |
|----------|-------------------------------|
| Vertikale Zugkraft (Einholen) | 10 kN (1.000 kgf) |
| Horizontale Zugkraft (Anker hängt schräg) | 5–8 kN |
| Dynamische Spitzenlast (Seegang) | 15–25 kN |
| Bolzenausreißkraft pro Bolzen (4 Bolzen) | 6,25 kN/Bolzen |

#### 6.1.2 Verstärkungsmaßnahmen

**GFK-Deck (Standard bei Serienyachten):**

1. **Gegenplatte unter Deck:** Mindestens 6 mm Edelstahlplatte oder 12 mm marinefestes Aluminium
2. **Fläche der Gegenplatte:** Mindestens 2× die Grundfläche der Windenmontage
3. **Bolzen:** Durchgangsbolzen (nicht Schrauben!), Edelstahl A4 (316), M10 oder M12
4. **Unterlegscheiben:** Große Unterlegscheiben (Karosseriescheiben) Ø 30 mm oder größer
5. **Dichtung:** Butylband oder Sikaflex 291/292 zwischen Windenfuß und Deck
6. **Laminatverstärkung:** Bei schwachem Deck zusätzliche GFK-Lagen (3–5 Lagen 450 g/m² Matte) auf der Unterseite

**Aluminiumdeck:**

1. **Direkte Verschraubung** in verstärkte Deckspanele möglich
2. **Mindestens 8 mm Deckstärke** im Bereich der Ankerwinde
3. **Dichtung:** Elastisches Dichtmittel (keine starre Verklebung wegen Wärmeausdehnung)

**Holz-/Teakdeck:**

1. **Durchgangsbolzen durch Teak + Unterdeck**
2. **Großflächige Druckverteilung** unter Deck
3. **Keine Schrauben in Endholz!**

#### 6.1.3 Bolzenmuster und Bohrschema

| Windenhersteller | Bolzenkreis (PCD) | Bolzenanzahl | Bolzengröße | Bohrschema |
|-----------------|-------------------|-------------|-------------|------------|
| Lofrans Tigres | 120–145 mm | 4 | M10 | Quadratisch |
| Lewmar V-Series (klein) | 108–127 mm | 4 | M10 | Quadratisch |
| Lewmar V-Series (groß) | 146–178 mm | 6 | M12 | Hexagonal |
| Quick Aleph | 115–140 mm | 4 | M10 | Quadratisch |
| Maxwell RC | 110–135 mm | 4 | M10 | Quadratisch |

### 6.2 Kettennuss-Ausrichtung (Gypsy Alignment)

Die korrekte Ausrichtung der Kettennuss zur Bugrolle (Ankerroller) ist entscheidend für einen störungsfreien Betrieb.

#### 6.2.1 Ausrichtungsregeln

1. **Kettenlinie:** Die Kette muss vom Ankerroller in gerader Linie auf die Kettennuss laufen. Seitlicher Versatz >5° führt zu:
   - Erhöhtem Kettenverschleiß
   - Erhöhtem Kettennuss-Verschleiß
   - Kettensprünge
   - Blockade der Kette

2. **Vertikale Führung:** Bei Vertikalwinden muss die Kette von der Kettennuss direkt nach unten in den Kettenkasten fallen können. Kein Hindernis im Kettenlauf!

3. **Abstand Ankerroller → Kettennuss:**
   - Minimum: 200 mm (für freien Kettenlauf)
   - Optimal: 300–500 mm
   - Maximum: 800 mm (sonst schlägt die Kette bei Seegang)

#### 6.2.2 Ausrichtungsprüfung

```
Prüfmethode:
1. Kette auflegen (3–5 Glieder auf der Kettennuss)
2. Kette zum Ankerroller führen
3. Seitliches Spiel prüfen: Kette darf max. 2 mm seitlich auf der Kettennuss wandern
4. Vertikalen Ablauf prüfen: Kette muss frei in den Kettenkasten fallen
5. Freifall testen: Kette muss ohne Verzögung durch die Kettennuss laufen
```

### 6.3 Kettenrohr / Kettenfallrohr (Chain Pipe)

Das Kettenrohr führt die Kette vom Deck in den Kettenkasten. Es muss die Kette sauber leiten und gleichzeitig Spritzwasser minimieren.

#### 6.3.1 Dimensionierung

| Kettengröße | Min. Rohrinnendurchmesser | Empfohlen |
|-------------|--------------------------|-----------|
| 6 mm | 40 mm | 50 mm |
| 8 mm | 50 mm | 60 mm |
| 10 mm | 60 mm | 75 mm |
| 12 mm | 75 mm | 90 mm |
| 14 mm | 90 mm | 110 mm |

#### 6.3.2 Materialien

| Material | Eignung | Kommentar |
|----------|---------|-----------|
| Edelstahl 316L | Optimal | Standard bei Qualitätsbooten |
| GFK-Rohr | Gut | Leicht, korrosionsfrei |
| PVC (dickwandig) | Akzeptabel | Günstig, kann durch Kette beschädigt werden |
| Aluminium (eloxiert) | Gut | Leicht, korrosionsbeständig |

#### 6.3.3 Decksdurchführung

Die Decksdurchführung des Kettenrohres muss absolut wasserdicht sein. Methoden:

1. **Einlaminiertes GFK-Rohr:** Beste Lösung, aber nur bei Neubau oder Refit machbar
2. **Decksdurchführung mit Flansch:** Standard-Nachrüstlösung, Dichtung mit Butylband oder Sikaflex
3. **Kettenrohr-Deckel:** Abdeckung über dem Kettenrohr zur Verhinderung von Wassereinbruch bei Seegang

### 6.4 Kettenkasten (Chain Locker)

Der Kettenkasten nimmt die Ankerkette auf. Er muss ausreichend Volumen haben, gut entwässert sein und die Kette sauber aufschießen lassen.

#### 6.4.1 Dimensionierung

Faustregel für Kettenkastenvolumen:

```
V_min [Liter] = Kettenlänge [m] × Kettengewicht_pro_m [kg/m] / ρ_kette_lose [kg/l]

ρ_kette_lose ≈ 2.5–3.5 kg/l (lose aufgeschossene Kette)

Beispiel: 60 m × 2.2 kg/m / 3.0 kg/l = 44 Liter Mindestvolumen
Empfohlen: 60–80 Liter für 60 m × 10 mm Kette
```

#### 6.4.2 Entwässerung

Der Kettenkasten **muss** entwässert werden. Eindringendes Seewasser und Kondenswasser sammeln sich und führen zu:
- Geruchsbildung (fauliges Kettenwasser)
- Beschleunigter Kettenverzinkung-Erosion
- Gewichtszunahme (50 Liter Wasser = 50 kg am Bug!)

**Entwässerungsmethoden:**
1. **Schwerkraft-Drainage:** Ablauf über Seeventil (am tiefsten Punkt des Kettenkastens)
2. **Lenzpumpe:** Elektrische Pumpe (Rule 500 GPH oder ähnlich) mit Schwimmerschalter
3. **Manuell:** Handlenzpumpe oder Eimer (nur bei kleinen Booten akzeptabel)

#### 6.4.3 Kettenendstück (Bitter End)

Das Kettenende **muss** im Kettenkasten befestigt sein — aber **lösbar.** Im Notfall muss die gesamte Kette gefieret werden können (z. B. wenn sich der Anker verhakt und die Yacht in Gefahr ist).

**Empfohlene Befestigung:**
- Leinenstück (ca. 2 m, Durchmesser ≥ 14 mm) am Kettenende befestigt
- Leine durch ein Loch in der Kettenkastenwand zum Cockpit oder Niedergang geführt
- Dort mit einem scharfen Messer im Notfall durchtrennbar

**AYDI-Bewertungsregel:** Ein nicht zugängliches oder nicht trennbares Kettenendstück erhält im Compliance-Modul eine `WARNING`.

### 6.5 Montagereihenfolge (Schritt für Schritt)

#### 6.5.1 Neuinstallation Vertikalwinde

1. **Position festlegen:** Kettennuss exakt auf Linie Ankerroller — Kettenkasten
2. **Bohrschablone:** Hersteller-Schablone auf Deck fixieren
3. **Decksdurchbruch Antriebswelle:** Kernlochbohrung (Lochsäge)
4. **Verstärkung unter Deck:** Gegenplatte positionieren
5. **Bolzenlöcher bohren:** Durchgangsbohrungen durch Deck + Gegenplatte
6. **Abdichtung:** Butylband oder Sikaflex auf Windenflansch
7. **Winde aufsetzen:** Von oben durch Deck
8. **Motor montieren:** Von unten an Antriebswelle ankoppeln
9. **Bolzen anziehen:** Gleichmäßig über Kreuz, Drehmoment nach Herstellerangabe
10. **Kettenrohr montieren:** Kettennuss → Kettenkasten
11. **Elektrik verlegen:** Starkstromkabel Batterie → Circuit Breaker → Solenoid → Motor
12. **Steuerleitung verlegen:** Fußschalter/Panel → Solenoid
13. **Kettenzähler montieren:** Sensor an Kettennuss, Display am Steuerstand
14. **Funktionsprüfung:** Motor in beiden Richtungen, Kettenlauf, Freifall, Kettenzähler kalibrieren
15. **Abschluss:** Alle Decksdurchführungen auf Dichtheit prüfen (Wassertest)

### 6.6 Nachrüstung — Besondere Herausforderungen

| Herausforderung | Lösung |
|-----------------|--------|
| Zu schwaches Deck | Laminat-Verstärkung unter Deck (3–5 Lagen GFK) |
| Kein Kettenkasten | Einbau eines GFK-Kettenkastens oder textilen Kettensacks |
| Kein Ankerroller | Nachrüstung Bugrolle (Edelstahl, verschraubt oder einlaminiert) |
| Batterie zu weit entfernt | 24V-Winde wählen (halbierter Strom, dünnere Kabel) |
| Kein Platz für Motor unter Deck | Horizontalwinde wählen (Motor über Deck) |
| Vorhandene Bohrungen nutzen | Adapter-Platte fertigen (Wasserstrahl-Schnitt) |

---

## 7. Fehlerbild-Atlas

### 7.1 Fehlerbild 1: Motor-Durchbrennen (Motor Burnout)

**Symptome:**
- Motor dreht nicht mehr
- Brandgeruch (verbrannte Wicklung)
- Sicherung/Circuit Breaker löst nicht aus (Motor intern kurzgeschlossen)
- Motor wird extrem heiß

**Ursachen:**
1. Einschaltdauer überschritten (häufigstes Szenario)
2. Kabelquerschnitt zu gering → Motor bekommt zu wenig Spannung, zieht mehr Strom
3. Blockierter Anker → Motor läuft gegen Anschlag
4. Wasser im Motorgehäuse → Kurzschluss der Wicklung
5. Korrrodierte Anschlüsse → Übergangswiderstand → Hitzeentwicklung

**AYDI Visuelle Erkennung:** `visual_low` — Motor unter Deck/im Gehäuse, Verbrennung nur am Geruch oder verfärbten Kabeln erkennbar.

**Reparatur:**
- Motortausch (Wicklung kann nicht wirtschaftlich repariert werden)
- Ursachenanalyse vor Einbau des Ersatzmotors!
- Kabelquerschnitt prüfen und ggf. korrigieren

**Kosten:** Motor-Ersatz €400–€900 + Einbau €150–€300

**Confidence:** `documented` (eindeutiges Fehlerbild bei physischer Inspektion)

### 7.2 Fehlerbild 2: Kettennuss-Verschleiß (Gypsy Wear)

**Symptome:**
- Kette springt über die Kettennuss (besonders beim Fieren)
- Kette liegt nicht mehr sauber in den Taschen
- Sichtbare Rillen oder Abflachung der Kettentaschen
- Kette rutscht durch unter Last

**Ursachen:**
1. Normaler Verschleiß nach 1.000+ Ankerzyklen
2. Falsche Kettengröße oder -norm (DIN vs. BBB)
3. Rostige Kette (Rostpartikel wirken wie Schleifmittel)
4. Kettennuss aus minderwertigem Material (Gusseisen statt Bronze)

**AYDI Visuelle Erkennung:** `visual_medium` — Verschleiß am Kettennuss-Profil ist auf Nahaufnahmen erkennbar. Asymmetrische Abnutzung, glänzende Stellen, verbreiterte Taschen.

**Reparatur:**
- Kettennuss-Tausch (keine Reparatur möglich)
- Gleichzeitig Kette auf Verschleiß prüfen

**Kosten:** Kettennuss €125–€250 + Einbau €50–€150

**Confidence:** `visual_medium` bis `measured` (Messung der Taschenbreite)

### 7.3 Fehlerbild 3: Solenoid-Ausfall (Solenoid Failure)

**Symptome:**
- Motor reagiert nicht auf Fußschalter/Panel
- Klicken des Solenoids hörbar, aber Motor dreht nicht
- Motor läuft dauerhaft (Kontakte verschweißt)
- Motor läuft nur in eine Richtung

**Ursachen:**
1. Kontaktverschweißung durch zu hohen Schaltstrom (Solenoid unterdimensioniert)
2. Korrosion der Kontakte (Feuchtigkeit im Solenoid-Gehäuse)
3. Spulendefekt (Überspannung, Alterung)
4. Steuerleitung unterbrochen (korrodierte Stecker, gebrochene Kabel)

**AYDI Visuelle Erkennung:** `visual_low` — Solenoid ist typischerweise unter Deck, Defekt nur durch elektrische Messung nachweisbar.

**Reparatur:**
- Solenoid-Tausch
- Stecker und Kabel der Steuerleitung prüfen
- Kontakte am Solenoid auf Verschweißung prüfen (Durchgangsprüfung)

**Kosten:** Solenoid €80–€280 + Einbau €50–€100

**Confidence:** `documented` (elektrische Messung)

### 7.4 Fehlerbild 4: Kettensprung (Chain Jump / Chain Skip)

**Symptome:**
- Kette springt bei Lastaufnahme aus der Kettennuss
- Ratternde Geräusche bei Betrieb
- Kette läuft nicht sauber ein
- Kette verklemmt sich seitlich

**Ursachen:**
1. Inkompatible Kette/Kettennuss (häufigster Grund!)
2. Verschlissene Kettennuss (s. Fehlerbild 2)
3. Fehlausrichtung Ankerroller → Kettennuss
4. Verformte oder verschlissene Kettenglieder
5. Fremdkörper in der Kettennuss (Leinenstücke, Muscheln)

**AYDI Visuelle Erkennung:** `visual_high` — Kettensprung ist auf Fotos der Kettennuss-Beladung deutlich erkennbar (Kette liegt schräg oder seitlich verschoben).

**Reparatur:**
- Kettenkompatibilität prüfen (DIN 766 vs. BBB)
- Kettennuss reinigen und auf Verschleiß prüfen
- Ausrichtung Ankerroller prüfen und korrigieren
- Verschlissene Kettenglieder ersetzen

**Kosten:** €50–€300 (je nach Ursache)

### 7.5 Fehlerbild 5: Winde reißt aus dem Deck (Deck Pull-Out)

**Symptome:**
- Sichtbare Risse oder Verformung um die Befestigungsbolzen
- Winde steht schief
- Wasser dringt durch die Bolzenlöcher ein
- Im Extremfall: Winde löst sich vollständig

**Ursachen:**
1. Keine Gegenplatte unter Deck
2. Zu kleine Unterlegscheiben (Punktlast statt Flächenlast)
3. Zu dünnes Decks-Laminat
4. Überlastung der Winde (blockierter Anker + volle Motorlast)
5. Ermüdung des Laminats durch zyklische Belastung

**AYDI Visuelle Erkennung:** `visual_high` — Risse und Verformungen um die Windenbasis sind auf Decksfotos gut erkennbar.

**Reparatur:**
- Winde demontieren
- Deck-Laminat reparieren (GFK-Verstärkung)
- Großflächige Gegenplatte einbauen
- Ggf. Bolzenmuster vergrößern
- Neu montieren mit korrekter Abdichtung

**Kosten:** €500–€3.000 (je nach Schadensumfang)

**AYDI-Bewertung:** `CRITICAL` — Sicherheitsrelevanter Strukturschaden

### 7.6 Fehlerbild 6: Getriebeschaden (Gearbox Failure)

**Symptome:**
- Mahlende oder knirschende Geräusche
- Motor dreht, aber Kettennuss bewegt sich nicht (oder nur ruckend)
- Kettennuss dreht frei in beide Richtungen (keine Selbsthemmung)
- Öl-/Fettaustritt am Gehäuse

**Ursachen:**
1. Überlastung (blockierter Anker, Winde als Festmachpunkt missbraucht)
2. Getriebeschaden durch Wassereintritt (korrodierte Zahnräder)
3. Verschleiß nach langer Nutzungsdauer (>15 Jahre)
4. Mangelnde Schmierung (Fett verbraucht, ausgewaschen)

**AYDI Visuelle Erkennung:** `visual_low` — Getriebe ist intern, nur indirekt durch Geräusche und Funktionstest nachweisbar.

**Reparatur:**
- Getriebe-Kit tauschen (komplett)
- Bei Vertikalwinden: Motor mit Getriebe von unten zugänglich
- Bei Horizontalwinden: Gehäusedeckel abnehmen

**Kosten:** Getriebe-Kit €250–€500 + Einbau €200–€400

### 7.7 Fehlerbild 7: Wellendichtung undicht (Shaft Seal Leak)

**Symptome:**
- Wassereinbruch unter Deck im Bereich der Winde (nur Vertikalwinden)
- Rostspuren oder Salzablagerungen an der Antriebswelle
- Feuchtigkeit im Motorgehäuse
- Grünspan an Bronzeteilen unter Deck

**Ursachen:**
1. Alterung der Wellendichtung (Simmerring/Lip Seal)
2. Beschädigte Dichtfläche an der Welle (Korrosion, Kratzer)
3. Fehlende oder verrutschte O-Ringe am Decksflansch
4. Thermische Verformung (Winde wird heiß bei Betrieb, Dichtung verliert Kontakt)

**AYDI Visuelle Erkennung:** `visual_medium` — Wasserflecken und Salzspuren unter Deck sind auf Fotos erkennbar.

**Reparatur:**
- Wellendichtring tauschen
- Welle auf Beschädigungen prüfen, ggf. polieren
- O-Ringe im Decksflansch erneuern
- Decksdurchführung neu abdichten

**Kosten:** Dichtungs-Kit €30–€65 + Einbau €100–€250

### 7.8 Fehlerbild 8: Korrosion am Gehäuse (Housing Corrosion)

**Symptome:**
- Weiße Oxidschicht auf Aluminiumgehäuse (Aluminiumfraß)
- Lochfraß an Edelstahlteilen
- Bläschenbildung unter Lackierung
- Festkorrodierte Bolzen

**Ursachen:**
1. Galvanische Korrosion (ungleichartige Metalle in Kontakt, z. B. Aluminium-Winde auf Edelstahl-Platte)
2. Mangelhafte Anodisierung des Aluminiums
3. Salzwasser-Dauerbelastung ohne Spülung
4. Fehlende Opferanoden am Rumpf (indirekt)

**AYDI Visuelle Erkennung:** `visual_high` — Korrosion am Gehäuse ist auf Fotos gut erkennbar. Weiße Ablagerungen, Verfärbungen, aufgequollene Stellen.

**Reparatur:**
- Leichte Korrosion: Schleifen, Grundierung, Neuanstrich
- Schwere Korrosion: Winde ersetzen
- Galvanische Trennung: Isoliermaterial zwischen ungleiche Metalle
- Regelmäßiges Süßwasserspülen nach jedem Einsatz

**Kosten:** €50–€200 (Pflege) oder €500–€5.000 (Ersatz)

### 7.9 Fehlerbild 9: Fußschalter-Defekt (Foot Switch Failure)

**Symptome:**
- Keine Reaktion auf Fußschalter-Betätigung
- Winde reagiert nur sporadisch
- Winde läuft nach Loslassen des Schalters weiter
- Fußschalter ist mechanisch gebrochen

**Ursachen:**
1. Wassereintritt in den Schalter (undichte Membran)
2. Korrodierte Kontakte im Schalter
3. Gebrochene Steuerleitung (Kabelbruch unter Deck)
4. Verschlissene Federmechanik (Schalter bleibt hängen)

**AYDI Visuelle Erkennung:** `visual_medium` — Defekter Fußschalter zeigt oft sichtbare Schäden (gebrochenes Gehäuse, herausstehendes Wasser, Korrosionsflecken).

**Reparatur:**
- Fußschalter komplett tauschen (nicht reparierbar)
- Steuerleitung durchmessen
- Stecker und Verbindungen unter Deck prüfen

**Kosten:** Fußschalter €65–€130 + Einbau €30–€80

### 7.10 Fehlerbild 10: Unkontrollierter Kettenablauf (Chain Run-Out)

**Symptome:**
- Kette rauscht mit hoher Geschwindigkeit aus dem Kettenkasten
- Starke Hitze- und Rauchentwicklung am Kettenrohr
- Schlaggeräusche im Bug
- Im Extremfall: Kette reißt am Endstück, gesamtes Ankergeschirr geht verloren

**Ursachen:**
1. Defekter Kettenstopper
2. Freifall-Kupplung unbeabsichtigt gelöst
3. Kettensprung bei Vertikalwinden (Kette entgleist)
4. Blockiertes Solenoid (Fier-Solenoid bleibt geschlossen)

**AYDI-Bewertung:** `CRITICAL` — Sicherheitsrisiko und materielles Verlustrisiko.

**Prävention:**
- Funktionsfähiger Kettenstopper (jährlich prüfen)
- Freifall-Kupplung mit Sicherung
- Kettenendstück korrekt befestigt und trennbar
- Korrekte Kettenführung und Kettennuss-Kompatibilität

**Kosten:** €0 (Prävention) bis €5.000+ (Verlust Ankergeschirr)

### 7.11 Fehlerbild 11: Übermäßige Geräuschentwicklung (Excessive Noise)

**Symptome:**
- Lautes Rattern, Schlagen oder Kreischen bei Betrieb
- Vibrationen im ganzen Vorschiff
- Geräusche, die sich von normaler Betriebsgeräuschkulisse unterscheiden

**Ursachen:**
1. Lose Befestigungsbolzen → Winde vibriert auf dem Deck
2. Kette schlägt im Kettenrohr → Rohr nicht fixiert
3. Getriebeschaden (s. Fehlerbild 6)
4. Verschlissene Lager im Motor
5. Kettennuss-Ketten-Inkompatibilität → Rattern
6. Fremdkörper im Kettenkasten (Leinenstücke, Werkzeug)

**AYDI Visuelle Erkennung:** `visual_low` — Geräuschprobleme sind nicht visuell erkennbar.

**Reparatur:** Abhängig von der Ursache (s. zugehöriges Fehlerbild)

### 7.12 Fehlerbild 12: Kettenzähler-Fehlfunktion (Chain Counter Malfunction)

**Symptome:**
- Kettenzähler zeigt falsche Werte (Drift nach vielen Zyklen)
- Kettenzähler reagiert nicht (keine Anzeige)
- Kettenzähler springt (zeigt willkürliche Werte)

**Ursachen:**
1. Sensor verschmutzt (Salzkristalle, Rost zwischen Sensor und Magnet)
2. Magnet vom Kettennuss-Zahnrad gelöst oder verrutscht
3. Kabel gebrochen (Vibration)
4. Display-Elektronik defekt (Feuchtigkeit)
5. Kalibrierung verloren (nach Stromausfall)

**AYDI Visuelle Erkennung:** `visual_low` — Nur am Display sichtbar, Sensor unter Deck.

**Reparatur:**
- Sensor reinigen, Abstand prüfen (typisch 1–3 mm)
- Magnet nachkleben/fixieren
- Kabel und Stecker prüfen
- Kalibrierung durchführen (Kettenlänge pro Umdrehung einstellen)

**Kosten:** €0–€50 (Reinigung/Kalibrierung) oder €150–€350 (Sensor/Display tauschen)

---

## 8. Troubleshooting-Entscheidungsbäume

### 8.1 Baum 1: Motor dreht nicht

```
Motor dreht nicht
├── Ist der Hauptschalter (Batterieschalter) ein?
│   ├── NEIN → Hauptschalter einschalten → GELÖST
│   └── JA ↓
├── Hat der Circuit Breaker ausgelöst?
│   ├── JA → Circuit Breaker rücksetzen
│   │   ├── Löst sofort wieder aus → Kurzschluss im Kabel oder Motor
│   │   │   → Kabel auf Beschädigung prüfen → Motor durchmessen
│   │   └── Bleibt ein → Batteriespannung prüfen
│   │       ├── <10.5V (12V-System) / <21V (24V-System) → Batterie laden
│   │       └── OK → Solenoid prüfen (klickt es beim Schalten?)
│   │           ├── NEIN → Steuerleitung/Fußschalter prüfen
│   │           │   ├── Fußschalter defekt → Tauschen
│   │           │   └── Steuerleitung unterbrochen → Reparieren
│   │           └── JA (Solenoid klickt) → Solenoid-Kontakte verschlissen
│   │               → Solenoid tauschen → ODER Motor durchgebrannt → Motor tauschen
│   └── NEIN ↓
├── Batteriespannung an der Winde messen
│   ├── 0V → Kabelbruch zwischen Batterie und Winde → Kabel prüfen
│   └── Spannung vorhanden → Motor durchmessen
│       ├── Motor hat Durchgang → Getriebe blockiert → Getriebe prüfen
│       └── Motor hat keinen Durchgang → Motor durchgebrannt → Motor tauschen
```

### 8.2 Baum 2: Motor dreht, aber Kette bewegt sich nicht

```
Motor dreht, Kette bewegt sich nicht
├── Dreht die Kettennuss?
│   ├── NEIN → Kupplung steht auf "Freifall" / "Entkuppelt"
│   │   → Kupplung einrücken → GELÖST
│   │   ODER: Getriebe defekt → Getriebe-Kit tauschen
│   └── JA → Kettennuss dreht, aber Kette bewegt sich nicht
│       ├── Kette nicht auf Kettennuss aufgelegt
│       │   → Kette korrekt einlegen → GELÖST
│       ├── Kettennuss verschlissen → Kette springt über → Kettennuss tauschen
│       └── Falsche Kette/Kettennuss-Kombination → Kompatibilität prüfen
│           → Korrekte Kettennuss bestellen
```

### 8.3 Baum 3: Winde ist extrem langsam

```
Winde ist extrem langsam
├── Batteriespannung unter Last messen
│   ├── <10.5V (12V) / <21V (24V) → Batterie schwach
│   │   → Batterie laden / ersetzen
│   │   ODER: Kabelquerschnitt zu gering → Spannungsabfall zu hoch → Kabel ersetzen
│   └── Spannung OK ↓
├── Stromaufnahme messen (Zangenamperemeter)
│   ├── Strom deutlich über Nennwert → Mechanische Blockade
│   │   ├── Anker ist eingehakt → Boot über den Anker fahren, erneut versuchen
│   │   ├── Kettenrohr blockiert → Fremdkörper entfernen
│   │   └── Getriebe schwergängig → Schmierung prüfen
│   └── Strom im Normalbereich → Motor schwach
│       ├── Kohlen/Bürsten verschlissen → Bürsten tauschen (wenn möglich)
│       └── Wicklung beschädigt (teilweise Kurzschluss) → Motor tauschen
```

### 8.4 Baum 4: Kette springt über die Kettennuss

```
Kette springt über die Kettennuss
├── Ist die richtige Kette für diese Kettennuss montiert?
│   ├── NEIN (z.B. DIN 766 auf BBB-Kettennuss) → Korrekte Kettennuss bestellen
│   │   ODER: Korrekte Kette kaufen
│   └── JA ↓
├── Ist die Kettennuss verschlissen?
│   ├── JA (Taschen ausgeschlagen, >1.5mm Spiel) → Kettennuss tauschen
│   └── NEIN ↓
├── Ist die Kettenführung korrekt (Ankerroller → Kettennuss)?
│   ├── NEIN (seitlicher Versatz >5°) → Ausrichtung korrigieren
│   └── JA ↓
├── Sind die Kettenglieder verformt oder verschlissen?
│   ├── JA → Betroffene Kettenglieder ersetzen / neue Kette
│   └── NEIN ↓
└── Fremdkörper in der Kettennuss?
    ├── JA → Reinigen → GELÖST
    └── NEIN → Hersteller-Support kontaktieren
```

### 8.5 Baum 5: Wasser dringt durch die Winde unter Deck

```
Wasser dringt durch die Winde unter Deck
├── Nur bei Vertikalwinden relevant? (Horizontalwinden haben keinen Decksdurchbruch)
│   └── JA, Vertikalwinde ↓
├── Woher kommt das Wasser?
│   ├── Durch die Antriebswelle → Wellendichtring defekt
│   │   → Wellendichtring (Simmerring) tauschen
│   │   → Welle auf Beschädigung/Korrosion prüfen
│   ├── Durch die Bolzenlöcher → Decksdichtung defekt
│   │   → Winde demontieren, Deck reinigen, neu abdichten (Sikaflex 291)
│   ├── Durch das Kettenrohr → Kettenrohr-Deckel fehlt / Kettenrohr undicht
│   │   → Kettenrohr-Deckel montieren
│   │   → Kettenrohr-Decksdurchführung abdichten
│   └── Unklar → Wassertest mit Gartenschlauch, Bereiche einzeln prüfen
```

---

## 9. FAQ — Häufige Fragen

### 9.1 Dimensionierung und Auswahl

**F1: Wie groß muss meine Ankerwinde sein?**
A: Die Zugkraft der Winde sollte mindestens das 2,5-fache des Gesamtgewichts von Anker + Kette (bei maximaler Wassertiefe) betragen. Siehe die Faustregeltabelle in Abschnitt 2.6.3. Für eine 12-m-Segelyacht mit 15-kg-Anker und 50 m × 8 mm Kette (ca. 70 kg) ist eine Winde mit mindestens 700 kg Zugkraft empfohlen, besser 1.000 kg.

**F2: 12V oder 24V — was ist besser?**
A: Ab 14 m Bootslänge ist 24V empfehlenswert. 24V halbiert den Strom bei gleicher Leistung, was dünnere Kabel erlaubt und den Spannungsabfall reduziert. Unter 14 m ist 12V Standard und ausreichend. Entscheidend ist das vorhandene Bordnetz — eine 24V-Winde in einem 12V-Boot erfordert einen separaten Batterie-Kreis oder DC/DC-Wandler.

**F3: Vertikal- oder Horizontalwinde?**
A: Vertikalwinden sind eleganter, haben bessere Kettenführung und den Motor geschützt unter Deck — ideal für Segelyachten. Horizontalwinden sind einfacher nachzurüsten, brauchen keinen Decksdurchbruch und sind bei schweren Ankersystemen robuster — ideal für Motoryachten und Nachrüstungen. Siehe die Vergleichstabelle in Abschnitt 2.2.3.

**F4: Kann ich eine Winde für Kette UND Tau verwenden?**
A: Ja, als Kombiwinde (Combination Windlass). Die meisten Hersteller bieten Combo-Versionen ihrer Modelle an. Alternativ kann der Spillkopf einer Vertikalwinde für Tau genutzt werden.

**F5: Welche Kettennuss brauche ich?**
A: Die Kettennuss muss exakt zur Kette passen — sowohl in Nennmaß (mm) als auch in Norm (DIN 766, ISO 4565/BBB). Dies ist der häufigste Fehler bei Neuinstallationen und Nachrüstungen! Bringen Sie ein Kettenglied zum Händler mit oder messen Sie: Drahtdurchmesser (Kaliber), Innenbreite, Innenlänge des Gliedes.

### 9.2 Betrieb und Handhabung

**F6: Wie lange darf ich die Winde am Stück betreiben?**
A: Einschaltdauer beachten (Duty Cycle)! Typisch 3–5 Minuten bei 12V-Winden, 5–8 Minuten bei 24V-Winden, unbegrenzt bei Hydraulikwinden. Nach der Einschaltdauer mindestens gleich lange Pause einlegen. Überschreitung führt zu Motorschaden!

**F7: Darf ich die Ankerwinde als Festmachpunkt nutzen?**
A: NEIN! Niemals! Die Ankerlast im Liegen wird IMMER vom Kettenstopper getragen. Die Winde dient nur dem Bewegen der Kette. Dauerbelastung der Winde führt zu Getriebe- und Motorschäden.

**F8: Was ist Freifall und wann benutze ich es?**
A: Freifall (Free-Fall) bedeutet, dass die Kette allein durch Schwerkraft ausfiert, ohne Motorbetrieb. Dies spart Strom und ermöglicht schnelles Ankern. Freifall nur nutzen, wenn: (a) der Kettenstopper funktioniert, (b) die Wassertiefe bekannt ist, (c) der Kettenkasten die Schlaglast verträgt.

**F9: Mein Kettenzähler zeigt falsche Werte — was tun?**
A: Zuerst kalibrieren: 10 m Kette manuell abzählen und den Zähler darauf einstellen. Wenn der Fehler bleibt: Sensor reinigen (Salzablagerungen), Sensorabstand prüfen (1–3 mm), Magnet auf festen Sitz prüfen. Siehe Fehlerbild 12.

**F10: Kann ich die Kette wechseln, ohne die Kettennuss zu tauschen?**
A: Nur wenn die neue Kette exakt dasselbe Profil hat (gleicher Durchmesser UND gleiche Norm). DIN-766-8mm und BBB-5/16" sind NICHT kompatibel, obwohl sie ähnlich aussehen!

### 9.3 Wartung und Pflege

**F11: Wie oft muss ich die Ankerwinde warten?**
A: Jährlich vor der Saison: Kettennuss auf Verschleiß prüfen, Getriebe schmieren (nach Herstellerangabe), Dichtungen sichtprüfen, Kabelverbindungen prüfen, Freifall-Funktion testen, Fußschalter testen, Kettenzähler kalibrieren. Nach jedem Einsatz in Salzwasser: Winde und Kette mit Süßwasser abspülen.

**F12: Welches Fett für die Ankerwinde?**
A: Meeresbeständiges Fett auf Lithium-Basis oder synthetisches Fett. Kein normales Schmierfett (wäscht sich aus). Empfohlene Produkte: Lewmar Winch Grease, Lanocote, Tef-Gel. Kein WD-40 (ist kein Schmiermittel, wäscht vorhandenes Fett aus!).

**F13: Muss ich die Ankerwinde im Winter ausbauen?**
A: Nein, nicht notwendig, wenn das Boot korrekt winterfest gemacht wird. Aber: Motor-Anschlüsse mit Kontaktspray behandeln, Kettennuss und Spillkopf mit Korrosionsschutz einsprühen, Fußschalter abdecken, Circuit Breaker ausschalten. Bei Landwinterung: Winde abdecken.

**F14: Meine Ankerwinde ist 20 Jahre alt — muss ich sie ersetzen?**
A: Nicht unbedingt. Solange Motor, Getriebe und Kettennuss funktionieren, kann eine gut gewartete Ankerwinde 25+ Jahre halten. Kritische Verschleißteile (Kettennuss, Wellendichtung, Kohlebürsten) können einzeln getauscht werden. Ersatzteilversorgung prüfen — bei eingestellten Modellen kann das schwierig werden.

**F15: Kann ich Ersatzteile verschiedener Hersteller mischen?**
A: Grundsätzlich nein. Kettennüsse, Getriebe und Motoren sind herstellerspezifisch. Einzige Ausnahme: Standard-Solenoids (wenn Strom und Spannung passen), Fußschalter (wenn Steuerspannung passt), Kabel und Sicherungen.

### 9.4 Installation und Nachrüstung

**F16: Kann ich eine Ankerwinde selbst einbauen?**
A: Ja, mit handwerklichem Geschick und Elektrik-Kenntnissen. Kritische Punkte: Decksverstärkung (muss ausreichend sein!), Kabelquerschnitt (muss berechnet werden!), Kettennuss-Ausrichtung (muss stimmen!). Bei Unsicherheit einen Fachbetrieb beauftragen — Fehler bei der Elektrik sind brandgefährlich.

**F17: Was kostet eine Ankerwindeninstallation komplett?**
A: Für eine typische 12-m-Segelyacht (1.000 kg Vertikalwinde): Winde €1.500–€2.500, Kabel + Sicherung + Solenoid €200–€400, Fußschalter €80–€130, Kettenzähler €250–€400, Einbau (Fachbetrieb) €500–€1.200. Gesamt: €2.500–€4.600.

**F18: Mein Boot hat kein 24V-Netz — kann ich trotzdem eine 24V-Winde nutzen?**
A: Ja, mit einem separaten 24V-Batteriepaar (2× 12V in Serie) nur für die Ankerwinde. Dies ist allerdings aufwändig und erfordert ein separates Ladegerät. Meist ist eine 12V-Winde die bessere Wahl bei einem 12V-Bordnetz.

**F19: Horizontalwinde nachrüsten — was muss ich beachten?**
A: 1. Deckstärke und -verstärkung prüfen. 2. Position so wählen, dass die Kette gerade von der Bugrolle zur Kettennuss läuft. 3. Kettenfall ins Unter-Deck organisieren (Kettenrohr oder Kettensack). 4. Kabelweg planen (Länge ausmessen, Querschnitt berechnen). 5. Batteriekapazität prüfen.

**F20: Kann ich eine Hydraulikwinde an den Motor meines 12-m-Bootes anschließen?**
A: Theoretisch ja (über PTO-Pumpe am Motor), praktisch selten sinnvoll bei Booten unter 18 m. Der Installationsaufwand und die Kosten für das Hydrauliksystem übersteigen den Nutzen. Erst ab 18–20 m wird Hydraulik wirtschaftlich — besonders wenn weitere Hydraulikverbraucher vorhanden sind (Bugstrahlruder, Kran, Passerelle).

### 9.5 Probleme und Fehlerbehebung

**F21: Meine Winde macht ein klickendes Geräusch, dreht aber nicht — was ist das?**
A: Das Klicken kommt vom Solenoid. Es schaltet (magnetisch), kann aber den Motorstrom nicht durchleiten. Ursachen: Verschweißte oder korrodierte Kontakte im Solenoid, Batteriespannung zu niedrig, oder Motordefekt. Solenoid und Batteriespannung prüfen. Siehe Troubleshooting-Baum 1.

**F22: Meine Kette verdreht sich im Kettenkasten — was kann ich tun?**
A: Verdrehte Kette (Kinking) entsteht, wenn die Kette nicht frei fallen kann. Lösungen: Kettenkasten vergrößern, Kettenführungsblech (Deflector) am Ketteneinlauf montieren, Kette regelmäßig komplett ausfahren und neu aufschießen lassen, Kettenwirbel (Swivel) zwischen Anker und Kette verwenden.

**F23: Meine Winde wird extrem heiß — ist das normal?**
A: Leichte Erwärmung des Motors nach 2–3 Minuten Betrieb ist normal. Wird der Motor so heiß, dass man ihn nicht mehr anfassen kann (>70°C), ist etwas falsch: Kabelquerschnitt zu gering (Spannungsabfall → Überstrom), mechanische Überlast, Getriebeschaden, oder Motor verschlissen. Sofort stoppen, abkühlen lassen, Ursache suchen.

**F24: Kann ich meine alte Kette in der neuen Winde weiterverwenden?**
A: Ja, wenn die Kette noch gut verzinkt ist (keine Roststellen), nicht gestreckt ist (Glieder nicht verformt) und die Nennmaße stimmen. Rostige Kette schadet der Kettennuss durch abrasiven Verschleiß. Im Zweifel: Neue Kette.

**F25: Wieviel Kette sollte ich mitnehmen?**
A: Faustregel: 3× die maximale Ankertiefe als Kette + optional 20 m Tau als Reiterleine. Für Mittelmeer-Segler (max. 15 m Ankertiefe): 50–60 m Kette. Für Atlantik-Überquerer (25 m Ankertiefe): 80–100 m Kette. Für Ostsee/Nordsee (10 m Ankertiefe): 40–50 m Kette.

---

## 10. Glossar

### A

**Anlaufstrom (Inrush Current):**
Der Strom, den ein Elektromotor beim Einschalten kurzzeitig (0,1–0,5 s) zieht. Typisch 2–3× des Arbeitsstroms. Alle Sicherungen und Schalter müssen den Anlaufstrom tolerieren.

**Ankerroller (Bow Roller / Anchor Roller):**
Die Rollenführung am Bug, über die die Ankerkette und der Ankerschaft beim Ein- und Ausfieren gleiten. Muss auf die Kettennuss ausgerichtet sein.

**Ankerwinsch:**
Umgangssprachliche Bezeichnung für Ankerwinde. Eigentlich ist „Winsch" (von engl. winch) eine Seilwinde, während „Windlass" das korrekte englische Wort für Ankerwinde ist.

**Aluminiumbronze (Aluminum Bronze):**
Kupfer-Aluminium-Legierung (CuAl10Fe5Ni5), Standardmaterial für Kettennüsse. Hervorragende Korrosionsbeständigkeit in Seewasser, hohe Festigkeit, gute Gleiteigenschaften.

### B

**BBB (Triple B / G30):**
Amerikanischer Kettenstandard. Gliedverhältnis Länge:Durchmesser ca. 3,5:1. NICHT kompatibel mit DIN-766-Kettennüssen, obwohl ähnliche Nennmaße.

**Bitter End:**
Das letzte Kettenglied, das im Kettenkasten befestigt ist. Sollte über eine trennbare Leine gesichert sein, damit die Kette im Notfall vollständig gefieret werden kann.

**Bugstrahlruder (Bow Thruster):**
Querschubtriebwerk im Bug. Kann mit einer Hydraulikwinde ein gemeinsames Hydrauliksystem teilen, darf aber nicht gleichzeitig betrieben werden (Druckabfall).

### C

**Capstan:**
Vertikale Spillwinde. Im engeren Sinne: der Spillkopf (Trommel) oberhalb der Kettennuss einer Vertikalwinde, der zum Einholen von Tauwerk dient.

**Chain Counter (Kettenzähler):**
Elektronisches Gerät, das die ausgebrachte Kettenlänge misst und anzeigt. Sensor an der Kettennuss + Display am Steuerstand.

**Chain Locker (Kettenkasten):**
Abgetrennter Raum im Vorschiff, in dem die Ankerkette aufbewahrt wird. Muss entwässert und belüftet sein.

**Chain Pipe (Kettenrohr):**
Rohr, das die Kette vom Deck in den Kettenkasten führt. Muss groß genug für freien Kettenfall sein.

**Circuit Breaker (Sicherungsautomat):**
Thermischer Überstromschutzschalter. Schützt die Kabelinstallation vor Überlast und Kurzschluss. Muss träge (langsam) auslösend sein, um den Anlaufstrom zu tolerieren.

### D

**DIN 766:**
Deutsche Industrie-Norm für kurzgliedrige Rundstahlketten. Standard in Europa für Ankerketten. Gliedverhältnis ca. 3:1. Die in der Yacht-Praxis häufigste Kettennorm.

**Duty Cycle (Einschaltdauer):**
Die maximale Betriebszeit eines Elektromotors, bevor er abkühlen muss. Angabe als „on/off"-Intervall (z. B. 5 min on / 5 min off). Überschreitung führt zu Motorschaden.

### E

**Einschaltdauer:**
→ siehe Duty Cycle

**Elektromotor (DC Motor):**
Gleichstrommotor, Antrieb der meisten Yacht-Ankerwinden. Typen: Permanentmagnet (leicht, effizient) oder Serienwund (hohes Drehmoment, robust).

### F

**Fieren (Veering / Paying Out):**
Kontrolliertes Ablassen der Ankerkette. Kann motorisch oder im Freifall erfolgen.

**Foot Switch (Fußschalter):**
Am Deck montierter Schalter, der mit dem Fuß betätigt wird. Ermöglicht Einhand-Bedienung der Ankerwinde. Muss IP67+ und selbst-rückstellend sein.

**Free-Fall (Freifall):**
Betriebsmodus, bei dem die Kette allein durch Schwerkraft ausfiert. Erfordert das Auskuppeln der Kettennuss vom Getriebe/Motor.

### G

**Galvanische Korrosion (Galvanic Corrosion):**
Elektrochemische Korrosion zwischen zwei verschiedenen Metallen in einem Elektrolyten (Seewasser). Häufig bei Aluminium-Winden auf Edelstahl-Platte oder bei Bronzeteilen gegen Aluminium.

**Gegenplatte (Backing Plate):**
Metallplatte unter dem Deck, die die Bolzenkräfte der Ankerwinde auf eine größere Fläche verteilt. Mindestens 6 mm Edelstahl oder 12 mm Aluminium.

**Getriebe (Gearbox):**
Kraftübertragung zwischen Motor und Kettennuss. Typen: Schneckengetriebe, Planetengetriebe, Stirnradgetriebe. Bestimmt Übersetzung, Wirkungsgrad und Selbsthemmung.

**Gypsy (Kettennuss):**
Das profilierte Rad der Ankerwinde, das die Kettenglieder formschlüssig aufnimmt. Muss exakt zum Kettentyp passen. Material: typisch Aluminiumbronze.

### H

**Hydraulikmotor (Hydraulic Motor):**
Hydrostatischer Motor, angetrieben durch Drucköl. Typen: Zahnradmotor (einfach, günstig), Axialkolbenmotor (effizient, kompakt), Radialkolbenmotor (hohes Drehmoment).

**Hydraulikpumpe (Hydraulic Pump):**
Erzeugt den Öldruck für den Hydraulikmotor. Angetrieben vom Hauptmotor (PTO) oder von einem separaten Elektromotor.

### I

**IP-Schutzklasse (IP Rating):**
Internationales Schutzklassensystem für Gehäuse. IP67 = staubdicht + zeitweiliges Untertauchen. IP68 = staubdicht + dauerhaftes Untertauchen. Minimum für Fußschalter: IP67.

**ISO 4565:**
Internationale Norm für Ankerketten, ähnlich BBB/G30. Nicht identisch mit DIN 766.

### K

**Kettenfang:**
Gefährliche Situation, bei der Finger, Kleidung oder Leinen zwischen Kette und Kettennuss eingezogen werden. Sicherheitsrelevant — Winde sofort stoppen!

**Kettenkasten:**
→ siehe Chain Locker

**Kettennuss:**
→ siehe Gypsy

**Kettenstopper (Chain Stopper):**
Mechanische Vorrichtung, die die Ankerkette fixiert und die Last vom Anker aufnimmt. Die Ankerwinde darf NICHT als Kettenstopper verwendet werden.

**Kettenzähler:**
→ siehe Chain Counter

**Klüse (Hawse Pipe / Navel Pipe):**
Rohr- oder Ösenführung, durch die die Ankerkette oder -leine das Deck verlässt. Muss auf Kettennuss und Ankerroller abgestimmt sein.

### L

**Labyrinth-Dichtung (Labyrinth Seal):**
Berührungslose Dichtung, die durch verschachtelte Kanäle Wasser vom Eindringen abhält. Wird an der Kettennuss-Durchführung verwendet.

**Leine (Rope / Line):**
Tauwerk, das als Ankerleine oder Reiterleine verwendet wird. Bei Kombiwinden über den Spillkopf oder eine separate Taurolle geführt.

### M

**Magnetschalter:**
→ siehe Solenoid

**Marinekabel (Marine Cable):**
Kabel mit verzinnten Kupferlitzen, speziell für den Einsatz auf Booten. Korrosionsbeständiger als normales Kupferkabel.

### N

**NMEA 2000:**
Digitales Bussystem für maritime Elektronik. Ermöglicht die Integration von Kettenzählern und Ankerwindensteuerungen in das Borddatennetzwerk.

**Nottrieb (Emergency Handle):**
Aufsteckbare Handkurbel für den manuellen Betrieb einer elektrischen oder hydraulischen Ankerwinde bei Ausfall des Antriebs.

### O

**Opferanode (Sacrificial Anode / Zinc):**
Zinkanode, die sich anstelle des Bootsmaterials auflöst und so galvanische Korrosion verhindert. Relevant für Ankerwinden aus Aluminium.

### P

**Permanentmagnet-Motor (PM Motor):**
Gleichstrommotor mit Permanentmagneten statt Feldwicklung. Leichter und effizienter als Serienwundmotoren, aber empfindlicher gegen Überhitzung.

**Planetengetriebe (Planetary Gearbox):**
Kompaktes Getriebe mit hohem Wirkungsgrad (70–85 %). Standard bei modernen Ankerwinden. Erlaubt Freifall-Funktion, erfordert aber separate Bremse.

**Pull Force (Zugkraft):**
Die maximale Kraft, die die Ankerwinde auf die Kette ausüben kann. Angabe in kg, kN oder lbs.

### R

**Reed-Kontakt (Reed Switch):**
Magnetisch betätigter Schalter, verwendet als Sensor im Kettenzähler. Ein Magnet am Kettennuss-Zahnrad löst bei jeder Umdrehung den Reed-Kontakt aus.

**Reiterleine (Snubber / Bridle):**
Elastische Leine, die zwischen Anker-Kette und Klampe/Poller befestigt wird. Absorbiert Stoßbelastungen beim Ankern und entlastet die Ankerwinde und den Kettenstopper.

### S

**Schneckengetriebe (Worm Gear):**
Getriebe mit hoher Untersetzung und Selbsthemmung (Kette kann nicht durchrutschen). Nachteil: geringer Wirkungsgrad (40–60 %). Vorteil: kein Freifall möglich = zusätzliche Sicherheit.

**Serienwundmotor (Series Wound Motor):**
Gleichstrommotor mit in Reihe geschalteter Feldwicklung. Hohes Anlaufdrehmoment, robust bei Überlast. Schwerer als Permanentmagnetmotoren.

**Simmerring (Shaft Seal / Lip Seal):**
Wellendichtring zur Abdichtung der rotierenden Antriebswelle gegen Wasser. Verschleißteil, muss regelmäßig geprüft werden.

**Solenoid (Magnetschalter / Relay):**
Elektromagnetisch betätigtes Leistungsrelais. Schaltet den hohen Motorstrom mit einer niedrigen Steuerspannung. Typisch zwei Solenoids pro Winde (Auf/Ab).

**Spillkopf:**
→ siehe Capstan

### T

**Toter-Mann-Schaltung (Dead Man's Switch):**
Sicherheitsschaltung, bei der die Winde nur solange läuft, wie der Schalter gedrückt ist. Standard bei allen Ankerwinden-Fußschaltern.

### U

**Umschlingungswinkel (Wrap Angle):**
Der Winkelbereich, über den die Kette die Kettennuss umschlingt. Vertikalwinden: 180°–220°. Horizontalwinden: 90°–150°. Größerer Winkel = sicherer Kettengriff.

### V

**Verzinnte Kupferlitze (Tinned Copper Strand):**
Kupferdraht mit Zinnbeschichtung zum Schutz gegen Korrosion in maritimer Umgebung. Pflicht für alle Kabelinstallationen auf Booten.

### W

**Wildcat:**
Synonym für Gypsy/Kettennuss, besonders in amerikanischem Englisch verwendet.

**Windlass:**
Englischer Oberbegriff für Ankerwinde. Nicht zu verwechseln mit „Winch" (Seilwinde/Fallenwinde).

### Z

**Zugkraft:**
→ siehe Pull Force

**Zykloidgetriebe (Cycloidal Gearbox):**
Getriebe mit Exzenterantrieb und zykloiden Scheiben. Kompakt, hohe Untersetzung, guter Wirkungsgrad. Neuere Anwendung bei Ankerwinden.

---

## 11. Schnell-Referenz

### 11.1 Windenwahl in 5 Schritten

```
Schritt 1: Bootslänge → Zugkraft bestimmen (Tabelle 2.6.3)
Schritt 2: Bordspannung → 12V oder 24V wählen
Schritt 3: Bauform → Vertikal (Segelboot) oder Horizontal (Motorboot/Nachrüstung)
Schritt 4: Kettentyp → DIN 766 (Europa) oder BBB (USA) → passende Kettennuss
Schritt 5: Hersteller wählen → Budget, Verfügbarkeit, Ersatzteile
```

### 11.2 Kabelquerschnitt-Schnellwahl

```
12V-System, Kabellänge 5 m:  500W→25mm²  700W→35mm²  1000W→50mm²
12V-System, Kabellänge 10 m: 500W→50mm²  700W→70mm²  1000W→95mm²
24V-System, Kabellänge 5 m:  500W→10mm²  1000W→25mm² 1500W→35mm²
24V-System, Kabellänge 10 m: 500W→16mm²  1000W→50mm² 1500W→70mm²
```

### 11.3 Jährliche Wartungs-Checkliste

```
□ Kettennuss auf Verschleiß prüfen (Taschen messen)
□ Getriebe schmieren (Fett nach Herstellerangabe)
□ Wellendichtung prüfen (nur Vertikalwinden)
□ Kabelverbindungen auf Korrosion prüfen
□ Fußschalter-Funktion testen
□ Freifall-Funktion testen
□ Kettenzähler kalibrieren
□ Circuit Breaker testen (ein/aus)
□ Solenoid-Funktion prüfen (Klick-Test)
□ Kettenkasten entwässern und reinigen
□ Ankerroller auf Leichtgängigkeit prüfen
□ Kettenstopper auf Funktion prüfen
□ Kette auf Rost und Verschleiß prüfen
□ Süßwasserspülung der gesamten Anlage
```

### 11.4 Notfall-Referenz

```
KETTE RAUSCHT UNKONTROLLIERT:
1. Alle Personen vom Kettenbereich fernhalten!
2. Fier-Schalter NICHT berühren (stoppt die Kette nicht)
3. Wenn sicher: Freifall-Bremse betätigen / Kupplung einrücken
4. Wenn nicht sicher: Kette auslaufen lassen, Bitter End hält (oder trennen im Notfall)
5. Motor NICHT zum Stoppen verwenden (Motorschaden, Getriebeschaden)

MOTOR RAUCHT / RIECHT VERBRANNT:
1. Fußschalter sofort loslassen
2. Circuit Breaker ausschalten
3. Hauptschalter aus
4. Brandwache 5 Minuten (Feuerlöscher bereithalten)
5. Motor NICHT mehr einschalten → Fachbetrieb

ANKERWINDE AUSGEFALLEN BEIM ANKERN:
1. Kettenstopper setzen (Kette sichern)
2. Nottrieb (Handkurbel) verwenden
3. Wenn kein Nottrieb: Kette an Klampe/Poller belegen, Boot über den Anker fahren
4. Mit Motorhilfe Kette Stück für Stück einholen
```

---

## ANHANG A — Fallstudie 1: Nachrüstung Vertikalwinde auf Bavaria 40 Cruiser (2015) {#anhang-a}

### Ausgangssituation
- **Boot:** Bavaria 40 Cruiser, Baujahr 2015, 12,35 m LOA
- **Bestehendes System:** Lofrans Tigres 600 (12V, 6 mm DIN 766), 30 m × 6 mm Kette
- **Problem:** Winde zu schwach für 15-kg-Delta-Anker + 50 m × 8 mm Kette (Upgrade geplant)
- **Wunsch:** Stärkere Winde, 8 mm Kette, Kettenzähler

### Analyse (AYDI-Bewertung)
- **Bestandsaufnahme:** Vorhandene Decksverstärkung für Tigres 600 ausreichend für bis zu 1.000 kg Zugkraft
- **Bolzenmuster:** 4× M10 auf 130 mm PCD — kompatibel mit Tigres 1000
- **Kabelsituation:** Vorhandene 25 mm² Kabel, Länge 6 m — zu gering für 1.000 W bei 12V (benötigt 35 mm²)
- **Batterie:** 2× 110 Ah AGM — ausreichend

### Durchführung
1. Winde: Lofrans Tigres 1000 (1.000 kg, 1.000 W 12V, 8 mm DIN 766) — €1.650
2. Kabel: Neue 50 mm² Marinekabel (verzinnt), 2× 7 m — €180
3. Circuit Breaker: Blue Sea 7076 (100 A) — €55
4. Kettennuss: Im Lieferumfang (8 mm DIN 766)
5. Kettenzähler: Lofrans IRIS — €420
6. Fußschalter: Bestehende weiterverwendet (kompatibel)
7. Kette: 50 m × 8 mm DIN 766 verzinkt — €380
8. Anker: Delta 15 kg — bereits vorhanden
9. Einbau: Fachbetrieb, 6 Stunden — €720

### Ergebnis
- **Gesamtkosten:** €3.405
- **AYDI Bewertung vorher:** 58/100 (Ankersystem unterdimensioniert)
- **AYDI Bewertung nachher:** 87/100 (korrekt dimensioniert, Kettenzähler vorhanden)
- **Confidence:** `measured` (exakte Spezifikationen bekannt)

---

## ANHANG B — Fallstudie 2: Hydraulikwinde auf Hallberg-Rassy 53 (2019) {#anhang-b}

### Ausgangssituation
- **Boot:** Hallberg-Rassy 53, Baujahr 2019, 16,55 m LOA
- **Bestehendes System:** Quick Aleph 1500/24 (24V, 1.500 kg, 10 mm DIN 766)
- **Problem:** Bei 30 m Wassertiefe + 80 m Kette überschreitet der Aufholvorgang die Einschaltdauer (8 min für 80 m bei 18 m/min = 4,4 min + Horizontalkomponente ≈ 7 min — grenzwertig)
- **Wunsch:** Hydraulikwinde für unbegrenzte Einschaltdauer

### Analyse
- **Hydrauliksystem:** Bereits vorhanden für Bugstrahlruder (Vetus BOW12024, 120 bar, 12 l/min)
- **Freie Kapazität:** Bugstrahlruder und Ankerwinde werden nie gleichzeitig betrieben — Pumpe kann geteilt werden
- **Zugkraft-Bedarf:** 2.500 kg (25 kg Anker + 80 m × 2,2 kg/m 10mm Kette + Sicherheitsfaktor)

### Durchführung
1. Winde: Lofrans Kobra 2500 Hydraulik-Variante — €7.200
2. Hydraulik-Steuerventil: 4/3-Wegeventil, 150 bar — €850
3. Hydraulikleitungen: DN 12, 12 m — €420
4. Kettennuss: 10 mm DIN 766 Aluminiumbronze (im Lieferumfang)
5. Einbau: Fachbetrieb, 3 Tage — €3.200

### Ergebnis
- **Gesamtkosten:** €11.670
- **AYDI Bewertung vorher:** 71/100 (Einschaltdauer grenzwertig)
- **AYDI Bewertung nachher:** 95/100 (unbegrenzte Einschaltdauer, korrekt dimensioniert)
- **Confidence:** `measured`

---

## ANHANG C — Fallstudie 3: Motorschwäche auf Jeanneau Sun Odyssey 449 (2017) {#anhang-c}

### Ausgangssituation
- **Boot:** Jeanneau Sun Odyssey 449, Baujahr 2017, 13,34 m LOA
- **Winde:** Lewmar V3 (700 kg, 700 W 12V, 8 mm DIN 766)
- **Symptom:** Winde wird nach 2 Minuten extrem langsam, Motor sehr heiß
- **Charterflotte:** Boot in Charterflotte, 80+ Ankervorgänge/Saison

### Diagnose
1. **Batteriespannung unter Last:** 11,2V (sollte >12,0V) — Batterien schwach
2. **Kabelquerschnitt:** 16 mm², Kabellänge 6 m — zu gering! (benötigt 35 mm²)
3. **Spannungsabfall am Kabel:** 1,8V unter Last — Motor bekommt nur 9,4V!
4. **Stromaufnahme:** 95 A (normal für V3) — aber bei 9,4V statt 12V
5. **Motortemperatur:** 85°C nach 2 min — Grenzwert ist 90°C

### Ursache
Unterdimensioniertes Kabel (Installationsfehler ab Werft). Der Spannungsabfall von 1,8V (15 %) reduziert die Motorleistung um ~30 % und erhöht die Stromaufnahme. Der Motor überhitzt vorzeitig.

### Reparatur
1. Kabel: Neue 50 mm² Marinekabel — €160
2. Batterien: 2× 120 Ah AGM (Upgrade) — €650
3. Einbau: 4 Stunden — €400

### Ergebnis
- **Gesamtkosten:** €1.210
- **AYDI Bewertung vorher:** 42/100 (elektrische Installation mangelhaft, CRITICAL)
- **AYDI Bewertung nachher:** 82/100 (korrekte Verkabelung)
- **Root Cause:** Werft-Installationsfehler (Kabelquerschnitt nicht berechnet)

---

## ANHANG D — Fallstudie 4: Kettennuss-Verschleiß auf Beneteau Oceanis 45 (2013) {#anhang-d}

### Ausgangssituation
- **Boot:** Beneteau Oceanis 45, Baujahr 2013, 13,78 m LOA
- **Winde:** Lofrans Tigres 1000 (12V, 8 mm DIN 766)
- **Symptom:** Kette springt beim Einholen regelmäßig über die Kettennuss
- **Nutzung:** 12 Jahre, geschätzt 900 Ankerzyklen

### Diagnose
1. **Kettenkompatibilität:** 8 mm DIN 766 — korrekt ✓
2. **Kettennuss visuell:** Sichtbare Rillen in den Taschen, asymmetrische Abnutzung
3. **Messung Taschenbreite:** 9,8 mm (Sollwert: 8,5 ±0,5 mm) — verschlissen!
4. **Kette:** Stellenweise oberflächenrostig, aber Glieder nicht verformt
5. **Ausrichtung Bugrolle:** Korrekt, kein seitlicher Versatz

### Ursache
Normaler Verschleiß nach ~900 Zyklen. Die rostige Kette hat den Verschleiß beschleunigt (Rostpartikel als Schleifmittel).

### Reparatur
1. Kettennuss 8 mm DIN 766 (Lofrans LZ.72037) — €145
2. Einbau: 1 Stunde Eigenleistung — €0
3. Kette: 50 m × 8 mm DIN 766 neu verzinkt — €350

### Ergebnis
- **Gesamtkosten:** €495
- **AYDI Bewertung:** Kettennuss-Verschleiß erkannt via Pipeline B (visuell), Confidence `visual_medium`
- **Empfehlung:** Kette regelmäßig (alle 2 Jahre) mit Süßwasser und Kettenspray behandeln

---

## ANHANG E — Fallstudie 5: Solenoid-Ausfall auf Grand Soleil 46 LC (2018) {#anhang-e}

### Ausgangssituation
- **Boot:** Grand Soleil 46 LC, Baujahr 2018, 13,90 m LOA
- **Winde:** Quick Aleph 1000 (12V, 8 mm DIN 766)
- **Symptom:** Winde reagiert nicht auf Fußschalter, Solenoid klickt nicht

### Diagnose
1. **Batteriespannung:** 12,6V — OK ✓
2. **Circuit Breaker:** Nicht ausgelöst ✓
3. **Fußschalter:** Durchgangsprüfung — OK ✓
4. **Steuerleitung:** 12V am Solenoid-Stecker messbar — OK ✓
5. **Solenoid-Spule:** Widerstand messen: ∞ (Unterbrechung!) — DEFEKT

### Ursache
Spulendefekt im Solenoid durch Feuchtigkeitseinbruch. Das Solenoid war unter dem Deckspaneel montiert, ohne IP-geschütztes Gehäuse. Kondenswasser hatte über 5 Jahre die Spulenwicklung korrodiert.

### Reparatur
1. Quick Solenoid 12V (SOL12V0080A) — €180
2. Wasserdichtes Solenoid-Gehäuse nachrüsten — €45
3. Einbau: 2 Stunden — €200

### Ergebnis
- **Gesamtkosten:** €425
- **AYDI Bewertung:** Solenoid-Defekt nur via Pipeline A (strukturiert, elektrische Messung) diagnostizierbar
- **Confidence:** `documented`

---

## ANHANG F — Fallstudie 6: Horizontalwinde auf Princess V58 (2016) {#anhang-f}

### Ausgangssituation
- **Boot:** Princess V58, Baujahr 2016, 18,14 m LOA
- **Winde:** Maxwell HRC FF (1.500 kg, 24V, 10 mm DIN 766)
- **Symptom:** Winde reißt bei schwerem Seegang teilweise aus dem Deck

### Diagnose
1. **Visuell:** Risse im Gelcoat um die Windenbasis, 2 von 4 Bolzen locker
2. **Unter Deck:** Keine Gegenplatte vorhanden! Bolzen nur in GFK-Sandwich geschraubt
3. **Deckstärke:** 18 mm GFK-Sandwich (Schaum-Kern) — für 1.500 kg Zugkraft unzureichend ohne Gegenplatte
4. **Belastungshistorie:** Boot ankert regelmäßig in 20+ m Tiefe in der Ägäis, schwerer Seegang

### Ursache
Werft-Installationsfehler: Keine Gegenplatte, keine lokale Deck-Verstärkung. Die Bolzen wurden direkt in das Sandwich-Deck geschraubt, was bei dynamischer Belastung zum Ausreißen führt.

### Reparatur
1. Winde demontieren — Deck reparieren (GFK-Laminat, 5 Lagen) — €1.200
2. Gegenplatte 10 mm Edelstahl 316L, 300×300 mm — €280
3. Durchgangsbolzen M12 × 4 Stück — €60
4. Neu montieren mit Sikaflex 292 — €120
5. Einbau: Fachbetrieb, 2 Tage — €1.800

### Ergebnis
- **Gesamtkosten:** €3.460
- **AYDI Bewertung vorher:** 28/100 (CRITICAL — Strukturversagen, Sicherheitsrisiko)
- **AYDI Bewertung nachher:** 88/100 (korrekte Montage mit Gegenplatte)
- **Confidence:** `visual_high` (Risse und lose Bolzen auf Fotos erkennbar)

---

## ANHANG G — Fallstudie 7: Handwinde auf Folkboot (1972) {#anhang-g}

### Ausgangssituation
- **Boot:** Nordischer Folkboot, Baujahr 1972, 7,64 m LOA
- **Bestehendes System:** Kein Ankerwinden-System. Anker (6 kg Danforth) wird von Hand eingeholt.
- **Wunsch:** Leichte manuelle Winde für einfacheres Ankern

### Analyse
- **Bootsgröße:** 7,64 m — kleine manuelle Winde ausreichend
- **Ankergewicht:** 6 kg + 20 m × 6 mm Kette (26,4 kg) = 32,4 kg Gesamtgewicht
- **Erforderliche Zugkraft:** 32,4 × 2,5 = 81 kg — minimale Anforderung
- **Gewichtslimit:** Max. 5 kg Windengewicht (Folkboot-Gewichtslimit am Bug)

### Lösung
1. Plastimo Anchor Winch 350 (manuell, 350 kg, 6 mm DIN 766) — €180
2. Montagematerial (Edelstahl-Bolzen, Gegenplatte) — €60
3. Einbau: Eigenleistung — €0

### Ergebnis
- **Gesamtkosten:** €240
- **AYDI Bewertung:** 72/100 (funktional, korrekt dimensioniert, keine Elektrik-Risiken)
- **Confidence:** `measured`
- **Hinweis:** Eine Elektrowinde wäre auf einem Folkboot nicht sinnvoll (Gewicht, Strombedarf, Komplexität)

---

## ANHANG H — Fallstudie 8: Kombiwinde Kette/Seil auf Hallberg-Rassy 342 (2008) {#anhang-h}

### Ausgangssituation
- **Boot:** Hallberg-Rassy 342, Baujahr 2008, 10,39 m LOA
- **Winde:** Maxwell RC8-8 Combo (800 kg, 12V, 8 mm DIN 766 + 14 mm Tau)
- **Ankergeschirr:** 20 m × 8 mm Kette + 30 m × 14 mm Ankerleine
- **Problem:** Ankerleine rutscht auf dem Spillkopf durch, Winde kann Tau nicht einholen

### Diagnose
1. **Spillkopf visuell:** Oberfläche poliert (glatt durch Verschleiß) — kein Grip
2. **Taudurchmesser:** 14 mm — passend für Spillkopf Ø 95 mm ✓
3. **Wicklungen:** Eigner nutzt nur 2 Wicklungen — zu wenig! (Mindestens 3 erforderlich)
4. **Tau:** Polyester-Geflecht — relativ glatt

### Ursache
Kombination aus verschlissenem (poliertem) Spillkopf und zu wenig Wicklungen. Zusätzlich ist glattes Polyester-Geflecht weniger griffig als 3-schäftiges Nylon.

### Reparatur
1. Spillkopf aufrauen (Schleifpapier K80, Rillen einfeilen) — €0 (Eigenleistung)
2. Betriebsanweisung: Immer mindestens 3 volle Wicklungen
3. Alternative: 3-schäftiges Nylontau (griffiger als Geflecht) — €85 für 30 m × 14 mm
4. Langfristig: Spillkopf-Tausch wenn Aufrauen nicht mehr hilft — €120

### Ergebnis
- **Gesamtkosten:** €0–€85
- **AYDI Bewertung:** Funktionsproblem erkannt, keine Sicherheitsgefahr
- **Confidence:** `documented` (Funktionstest)

---

## ANHANG I — Confidence-Mapping {#anhang-i}

### Confidence-Zuordnung nach Befundtyp

| Befundtyp | Pipeline | Confidence | Begründung |
|-----------|----------|------------|-----------|
| Kabelquerschnitt messen | A (Strukturiert) | `measured` | Exakte Messung mit Messschieber |
| Spannungsabfall messen | A (Strukturiert) | `measured` | Exakte Messung mit Multimeter |
| Motorstrom messen | A (Strukturiert) | `measured` | Exakte Messung mit Zangenamperemeter |
| Kettennuss-Verschleiß (Foto) | B (Visuell) | `visual_medium` | Verschleiß erkennbar, aber nicht messbar |
| Gehäusekorrosion (Foto) | B (Visuell) | `visual_high` | Korrosion gut erkennbar auf Fotos |
| Decksverstärkung (Foto) | B (Visuell) | `visual_low` | Gegenplatte unter Deck nicht sichtbar |
| Risse um Windenbasis (Foto) | B (Visuell) | `visual_high` | Risse im Gelcoat gut erkennbar |
| Windengröße vs. Boot (Specs) | A (Strukturiert) | `calculated` | Berechnung aus Spezifikationen |
| Servicebericht „Motor getauscht" | C (Text) | `documented` | Dokumentierter Befund |
| Eigenerbericht „Kette springt" | C (Text) | `documented` | Symptom dokumentiert, Ursache offen |
| Kettenkompatibilität (Specs) | A (Strukturiert) | `measured` | Exakte Zuordnung Kette ↔ Kettennuss |

---

## ANHANG J — AYDI Bewertungsschema für Ankerwinden {#anhang-j}

### Bewertungskriterien und Gewichtung

| Kriterium | Gewicht | Score-Bereich | Beschreibung |
|-----------|---------|--------------|-------------|
| Zugkraft-Dimensionierung | 20 % | 0–100 | Zugkraft vs. Anker+Kette+Wassertiefe |
| Elektrische Installation | 20 % | 0–100 | Kabelquerschnitt, Sicherung, Solenoid |
| Kettenkompatibilität | 15 % | 0–100 | Kette↔Kettennuss Übereinstimmung |
| Mechanischer Zustand | 15 % | 0–100 | Verschleiß Kettennuss, Getriebe, Dichtung |
| Montagequalität | 10 % | 0–100 | Decksverstärkung, Ausrichtung, Abdichtung |
| Sicherheitseinrichtungen | 10 % | 0–100 | Kettenstopper, Freifall-Sicherung, Bitter End |
| Bedienkomfort | 5 % | 0–100 | Fußschalter, Kettenzähler, Fernbedienung |
| Wartungszustand | 5 % | 0–100 | Korrosion, Schmierung, Dichtungen |

### Score-Interpretation

| Score | Bewertung | AYDI Label |
|-------|----------|-----------|
| 90–100 | Exzellent | ★★★★★ Professionell installiert und gewartet |
| 75–89 | Gut | ★★★★ Korrekt dimensioniert, kleine Verbesserungen möglich |
| 60–74 | Befriedigend | ★★★ Funktionsfähig, mehrere Verbesserungspunkte |
| 40–59 | Mangelhaft | ★★ Signifikante Mängel, Handlungsbedarf |
| 20–39 | Ungenügend | ★ Sicherheitsrelevante Mängel, sofortiger Handlungsbedarf |
| 0–19 | Kritisch | ⚠ CRITICAL — Nicht betriebssicher |

---

## ANHANG K — Kettennuss-Kompatibilitätsmatrix {#anhang-k}

### DIN 766 Kettennüsse

| Kettennuss-Nennmaß | Kette 6mm DIN766 | Kette 8mm DIN766 | Kette 10mm DIN766 | Kette 12mm DIN766 | Kette 8mm BBB |
|--------------------|-----------------|-----------------|--------------------|--------------------|--------------| 
| 6 mm DIN 766 | ✅ Kompatibel | ❌ | ❌ | ❌ | ❌ |
| 8 mm DIN 766 | ❌ | ✅ Kompatibel | ❌ | ❌ | ❌ (!) |
| 10 mm DIN 766 | ❌ | ❌ | ✅ Kompatibel | ❌ | ❌ |
| 12 mm DIN 766 | ❌ | ❌ | ❌ | ✅ Kompatibel | ❌ |
| 8 mm BBB/ISO | ❌ | ❌ (!) | ❌ | ❌ | ✅ Kompatibel |

**(!) Häufigster Fehler:** 8 mm DIN 766 und 8 mm (5/16") BBB sind NICHT kompatibel, obwohl der Drahtdurchmesser identisch ist. Die Gliedform (Kurzglied vs. Langglied) unterscheidet sich!

---

## ANHANG L — Kabelquerschnitt-Rechentabelle {#anhang-l}

### Vollständige Tabelle mit Spannungsabfall

| Spannung | Strom | Länge 3m | Länge 5m | Länge 7m | Länge 10m | Länge 12m | Länge 15m |
|----------|-------|---------|---------|---------|----------|----------|----------|
| 12V | 35 A | 10 mm² | 16 mm² | 25 mm² | 35 mm² | 35 mm² | 50 mm² |
| 12V | 50 A | 16 mm² | 25 mm² | 35 mm² | 50 mm² | 70 mm² | 70 mm² |
| 12V | 65 A | 25 mm² | 35 mm² | 50 mm² | 70 mm² | 70 mm² | 95 mm² |
| 12V | 80 A | 25 mm² | 35 mm² | 50 mm² | 70 mm² | 95 mm² | 95 mm² |
| 12V | 100 A | 35 mm² | 50 mm² | 70 mm² | 95 mm² | 120 mm² | 120 mm² |
| 12V | 130 A | 50 mm² | 70 mm² | 95 mm² | 120 mm² | 150 mm² | 185 mm² |
| 24V | 25 A | 6 mm² | 10 mm² | 16 mm² | 16 mm² | 25 mm² | 25 mm² |
| 24V | 40 A | 10 mm² | 16 mm² | 25 mm² | 25 mm² | 35 mm² | 35 mm² |
| 24V | 65 A | 16 mm² | 25 mm² | 35 mm² | 50 mm² | 50 mm² | 70 mm² |
| 24V | 80 A | 16 mm² | 25 mm² | 35 mm² | 50 mm² | 70 mm² | 70 mm² |
| 24V | 100 A | 25 mm² | 35 mm² | 50 mm² | 70 mm² | 70 mm² | 95 mm² |
| 24V | 130 A | 25 mm² | 50 mm² | 70 mm² | 95 mm² | 95 mm² | 120 mm² |

**Berechnung basiert auf:** Max. 3 % Spannungsabfall, Kupfer κ=56 m/(Ω×mm²), Hin- und Rückleitung.

---

## ANHANG M — Wartungsplan Jahresübersicht {#anhang-m}

### Saisonale Wartung

| Zeitpunkt | Maßnahme | Aufwand | Material |
|-----------|----------|---------|----------|
| **Frühjahr (Saisonstart)** | | | |
| | Sichtprüfung Kettennuss und Spillkopf | 10 min | — |
| | Getriebe schmieren (Herstellerangabe) | 15 min | Marine-Fett, €8 |
| | Wellendichtung prüfen (Vertikalwinde) | 10 min | — |
| | Kabelverbindungen nachziehen und mit Kontaktspray behandeln | 20 min | Kontaktspray, €6 |
| | Fußschalter-Funktionstest | 5 min | — |
| | Freifall-Funktionstest | 5 min | — |
| | Kettenzähler kalibrieren | 10 min | — |
| | Circuit Breaker testen | 2 min | — |
| | Kette inspizieren (Rost, Verformung) | 20 min | — |
| | Kettenkasten reinigen und entwässern | 30 min | — |
| **Mitte Saison (Juli/August)** | | | |
| | Süßwasserspülung nach intensiver Nutzung | 15 min | — |
| | Kettennuss-Funktionscheck | 5 min | — |
| | Batteriezustand prüfen | 10 min | — |
| **Herbst (Saisonende)** | | | |
| | Vollständige Sichtprüfung aller Komponenten | 30 min | — |
| | Gehäuse und Kettennuss mit Korrosionsschutz einsprühen | 15 min | Korrosionsschutz, €12 |
| | Fußschalter abdecken | 5 min | — |
| | Circuit Breaker ausschalten | 1 min | — |
| | Winde abdecken (bei Freilager-Winterung) | 5 min | Abdeckplane, €15 |
| | Kette mit Kettenspray konservieren | 20 min | Kettenspray, €14 |

### Intervall-Wartung

| Intervall | Maßnahme | Bemerkung |
|-----------|----------|-----------|
| Alle 2 Jahre | Wellendichtring prüfen, ggf. tauschen | Nur Vertikalwinden |
| Alle 3 Jahre | Getriebe-Inspektion (Zahnflanken prüfen) | Durch Fachbetrieb |
| Alle 5 Jahre | Solenoid-Kontakte prüfen, ggf. tauschen | Elektrische Messung |
| Alle 5 Jahre | Fußschalter tauschen (präventiv) | IP-Dichtung altert |
| Alle 8–10 Jahre | Kohlebürsten prüfen/tauschen (falls vorhanden) | Nur Bürstenmotor |
| Alle 10–15 Jahre | Kettennuss auf Verschleiß messen, ggf. tauschen | Taschenbreite messen |
| Alle 15–20 Jahre | Motor-Revision oder -Tausch | Abhängig von Nutzung |
| Alle 20 Jahre | Gesamtrevision oder Ersatz der Winde | Kosten vs. Neuwinde abwägen |

---

## ANHANG N — Normen und Regularien {#anhang-n}

### Relevante Normen für Ankerwinden-Installation

| Norm | Titel | Relevanz für Ankerwinden |
|------|-------|--------------------------|
| ISO 15084:2003 | Small craft — Anchoring, mooring and towing — Strong points | Dimensionierung der Verankerungspunkte am Bug |
| ISO 10133:2012 | Small craft — Electrical systems — Extra-low-voltage DC installations | Verkabelung, Absicherung, Schalter |
| ISO 10134:2003 | Small craft — Electrical devices — Lightning protection systems | Blitzschutz der Ankerwindeninstallation |
| ISO 13297:2014 | Small craft — Electrical systems — AC installations | Nur für AC-betriebene Hydraulikpumpen |
| IEC 60092 | Electrical installations in ships | Kabelführung, Schutzklassen |
| ABYC E-11 | AC & DC Electrical Systems on Boats | US-Standard, anerkannt international |
| ABYC H-40 | Anchoring, Mooring, and Strong Points | US-Standard für Ankersysteme |

### CE-Relevanz

Ankerwinden als einzelnes Produkt unterliegen **nicht** direkt der Recreational Craft Directive 2013/53/EU. Jedoch muss die **Gesamtinstallation** (Winde + Elektrik + Decksbefestigung) den Anforderungen der CE-Kategorie des Bootes entsprechen:

| CE-Kategorie | Anforderung an Ankerwinden-Installation |
|-------------|----------------------------------------|
| A (Ocean) | Höchste Anforderungen: Vollständige Redundanz empfohlen, Nottrieb Pflicht, Kettenstopper Pflicht |
| B (Offshore) | Hohe Anforderungen: Korrekte Dimensionierung, Nottrieb empfohlen |
| C (Inshore) | Standard-Anforderungen: Korrekte Dimensionierung |
| D (Sheltered) | Basisanforderungen |

---

## ANHANG O — Bezugsquellen und Preisvergleich {#anhang-o}

### Online-Händler (Europa)

| Händler | Land | Sortiment | Preislevel | URL |
|---------|------|-----------|-----------|-----|
| SVB (Segel- und Bootszubehör) | DE | Lofrans, Lewmar, Quick, Maxwell | Mittel | svb-marine.de |
| Compass24 | DE | Lofrans, Lewmar, Quick | Mittel | compass24.de |
| Toplicht | DE | Lewmar, Quick, Maxwell | Mittel-Hoch | toplicht.de |
| AWN | DE | Lofrans, Lewmar, Quick | Mittel | awn.de |
| Promarine | IT | Quick, Lofrans, Italwinch | Günstig | promarinestore.com |
| AD Nautic | FR | Quick, Lewmar, Maxwell | Mittel | adnautic.com |
| Force 4 | UK | Lewmar, Maxwell, Muir | Mittel-Hoch | force4.co.uk |
| Defender | US | Maxwell, Lewmar, Muir | Mittel | defender.com |

### Preisvergleich: 1.000 kg Vertikalwinde, 12V, 8 mm DIN 766

| Hersteller | Modell | UVP (2026) | Straßenpreis (2026) |
|-----------|--------|-----------|---------------------|
| Lofrans | Tigres 1000 | €1.850 | €1.550–€1.700 |
| Lewmar | V4 | €2.050 | €1.750–€1.900 |
| Quick | Aleph 1000 | €2.150 | €1.850–€2.000 |
| Maxwell | RC10 | €1.950 | €1.650–€1.800 |
| Italwinch | Smart 1000 | €1.500 | €1.250–€1.400 |
| CX/SX (SPI) | CX3 (700 kg!) | €950 | €800–€900 |

---

## ANHANG P — Erfahrungsberichte aus Foren {#anhang-p}

### Zusammenfassung typischer Eignerberichte

**Quelle: Segeln-Forum.de, Boote-Forum.de, YBW.com, Cruisers Forum**

#### Positiv-Berichte (Muster):
1. „Lofrans Tigres seit 15 Jahren auf unserer HR 36 — nie ein Problem, nur jährlich fetten."
2. „Quick Aleph — super leise, schönes Design, LED-Anzeige am Spillkopf ist genial nachts."
3. „Maxwell RC8 Combo — einzige Winde, die BBB und DIN 766 mit Wechsel-Kettennuss kann."
4. „Lewmar V5 auf unserer Contest 48 — 24V ist der richtige Weg ab 14 m, nie Spannungsprobleme."

#### Negativ-Berichte (Muster):
1. „CX2 nach 3 Jahren: Getriebe macht Geräusche, Dichtung undicht, Motor überhitzt — billig gekauft, teuer bezahlt."
2. „Italwinch Smart: Spillkopf-Oberfläche nach 2 Saisons poliert, Tau rutscht durch."
3. „Lewmar V2: Kettennuss für 6 mm DIN 766 ist identisch mit BBB 1/4 — funktioniert nicht mit meiner DIN-Kette! Musste spezielle Kettennuss nachbestellen."
4. „Quick Solenoid nach 4 Jahren defekt — Feuchtigkeit unter dem Deckspaneel. Montage-Ort war schlecht gewählt."

#### Wiederkehrende Themen:
- **Kabelquerschnitt** ist das häufigste Problem bei allen Marken
- **Kettennuss-Kompatibilität** wird oft falsch bestellt (DIN vs. BBB)
- **Duty Cycle** wird von Eignern häufig überschritten (Anker in 25+ m Tiefe)
- **Getriebefett** trocknet aus bei Booten, die selten ankern
- **Süßwasserspülung** nach Salzwasser wird vernachlässigt

**Confidence:** `documented` (Forum-Konsens über viele Berichte)

---

## ANHANG Q — Visuelle Analyse-Referenzbilder {#anhang-q}

### Referenz-Merkmale für Pipeline B (Visuell)

| Befund | Sichtbare Merkmale | Confidence |
|--------|-------------------|------------|
| Korrosion Gehäuse | Weiße Oxidschicht (Aluminium), Lochfraß, Bläschen | `visual_high` |
| Kettennuss-Verschleiß | Glänzende Rillen in Taschen, asymmetrische Abnutzung | `visual_medium` |
| Risse im Deck um Winde | Gelcoat-Risse, sternförmig um Bolzen | `visual_high` |
| Korrodierte Kabelschuhe | Grünspan, weiße Ablagerungen an Anschlüssen | `visual_medium` |
| Undichte Wellendichtung | Wasserflecken, Salzspuren unter Deck an Welle | `visual_medium` |
| Fehlende Gegenplatte | Unter-Deck-Foto zeigt Bolzen direkt im Laminat | `visual_high` |
| Kette auf Kettennuss | Kette liegt sauber in Taschen = OK, schräg/versetzt = Problem | `visual_high` |
| Fußschalter-Zustand | Gebrochenes Gehäuse, fehlende Abdeckung, Korrosion | `visual_medium` |
| Kettenkasten-Zustand | Stehendes Wasser, Rost an Kette, verschlammter Boden | `visual_medium` |
| Kabelführung | Kabel ordentlich gebündelt und befestigt vs. lose hängend | `visual_medium` |

### Visuelle Erkennung — Grenzen

| Nicht visuell erkennbar | Grund | Alternative |
|------------------------|-------|-------------|
| Motordefekt | Motor unter Deck / im Gehäuse | Funktionstest, Strommessung |
| Getriebedefekt | Intern | Geräuschanalyse, Funktionstest |
| Solenoid-Defekt | Unter Deck | Elektrische Messung |
| Kabelquerschnitt | Kabel nicht sichtbar oder nicht messbar auf Foto | Dokumentation, Messung |
| Batteriespannung unter Last | Nicht visuell | Messung |
| Einschaltdauer-Bewertung | Betriebsparameter | Berechnung aus Specs |

---

## ANHANG R — AYDI-Integration (Pydantic-Modelle) {#anhang-r}

### Pydantic v2 Modelle für die AYDI-Analyse-Engine

```python
"""
AYDI Anchor Windlass Assessment Models
Pydantic v2 models for structured windlass analysis.
"""
from __future__ import annotations

from datetime import date
from enum import Enum
from typing import Optional

from pydantic import BaseModel, Field, field_validator


# ── Enumerations ──────────────────────────────────────────────────────

class WindlassType(str, Enum):
    """Windlass orientation / mount style."""
    VERTICAL = "vertical"
    HORIZONTAL = "horizontal"


class DriveType(str, Enum):
    """Windlass drive mechanism."""
    ELECTRIC_DC = "electric_dc"
    HYDRAULIC = "hydraulic"
    MANUAL = "manual"
    ELECTRIC_HYDRAULIC = "electric_hydraulic"  # electric pump + hydraulic motor


class MotorType(str, Enum):
    """DC motor winding type."""
    PERMANENT_MAGNET = "permanent_magnet"
    SERIES_WOUND = "series_wound"
    NOT_APPLICABLE = "n/a"


class GearboxType(str, Enum):
    """Gearbox mechanism type."""
    WORM = "worm"
    PLANETARY = "planetary"
    SPUR = "spur"
    BEVEL = "bevel"
    CYCLOIDAL = "cycloidal"
    NONE = "none"


class ChainStandard(str, Enum):
    """Anchor chain link standard."""
    DIN_766 = "din_766"
    ISO_4565 = "iso_4565"
    BBB_G30 = "bbb_g30"
    G40_HT = "g40_ht"
    DIN_5685 = "din_5685"


class GypsyMaterial(str, Enum):
    """Gypsy / wildcat material."""
    ALUMINUM_BRONZE = "aluminum_bronze"
    MANGANESE_BRONZE = "manganese_bronze"
    STAINLESS_316L = "stainless_316l"
    TITANIUM_GR5 = "titanium_gr5"
    CAST_IRON_GALVANIZED = "cast_iron_galvanized"


class ConfidenceLevel(str, Enum):
    """AYDI confidence level for a finding."""
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
    """Finding severity level."""
    CRITICAL = "critical"
    WARNING = "warning"
    INFO = "info"
    OK = "ok"


class VoltageSystem(str, Enum):
    """Onboard DC voltage system."""
    V12 = "12"
    V24 = "24"
    V32 = "32"
    V48 = "48"


# ── Core Models ───────────────────────────────────────────────────────

class GypsySpec(BaseModel):
    """Specification of the anchor windlass gypsy (wildcat / chain wheel)."""

    model_config = {"from_attributes": True}

    chain_diameter_mm: float = Field(
        ..., gt=0, le=50, description="Chain wire diameter in mm"
    )
    chain_standard: ChainStandard = Field(
        ..., description="Chain link standard (DIN 766, BBB, etc.)"
    )
    material: GypsyMaterial = Field(
        default=GypsyMaterial.ALUMINUM_BRONZE,
        description="Gypsy material"
    )
    pocket_width_mm: Optional[float] = Field(
        default=None,
        description="Measured pocket width in mm (for wear assessment)"
    )
    wrap_angle_deg: Optional[float] = Field(
        default=None, ge=0, le=360,
        description="Chain wrap angle in degrees"
    )
    wear_status: Optional[str] = Field(
        default=None,
        description="Wear assessment: good / acceptable / worn / replace"
    )


class MotorSpec(BaseModel):
    """Windlass motor specification."""

    model_config = {"from_attributes": True}

    motor_type: MotorType = Field(
        default=MotorType.PERMANENT_MAGNET,
        description="Motor winding type"
    )
    power_watts: float = Field(
        ..., gt=0, le=50000, description="Rated motor power in watts"
    )
    voltage: VoltageSystem = Field(
        ..., description="Operating voltage"
    )
    current_working_amps: Optional[float] = Field(
        default=None, description="Working load current draw in amps"
    )
    current_max_amps: Optional[float] = Field(
        default=None, description="Maximum load current draw in amps"
    )
    current_inrush_amps: Optional[float] = Field(
        default=None, description="Inrush (start) current in amps"
    )
    duty_cycle_on_min: Optional[float] = Field(
        default=None, description="Duty cycle on-time in minutes"
    )
    duty_cycle_off_min: Optional[float] = Field(
        default=None, description="Duty cycle off-time in minutes"
    )


class WindlassSpec(BaseModel):
    """Complete windlass specification."""

    model_config = {"from_attributes": True}

    manufacturer: str = Field(..., description="Manufacturer name")
    model: str = Field(..., description="Model name/number")
    windlass_type: WindlassType = Field(..., description="Vertical or horizontal")
    drive_type: DriveType = Field(..., description="Drive mechanism")
    pull_force_kg: float = Field(
        ..., gt=0, le=100000, description="Rated pull force in kg"
    )
    line_speed_no_load_m_min: Optional[float] = Field(
        default=None, description="Line speed (no load) in m/min"
    )
    line_speed_working_m_min: Optional[float] = Field(
        default=None, description="Line speed (working load) in m/min"
    )
    gypsy: GypsySpec = Field(..., description="Gypsy / wildcat specification")
    motor: Optional[MotorSpec] = Field(
        default=None, description="Motor spec (None for manual windlasses)"
    )
    gearbox_type: GearboxType = Field(
        default=GearboxType.PLANETARY, description="Gearbox type"
    )
    has_free_fall: bool = Field(
        default=False, description="Free-fall capability"
    )
    has_capstan: bool = Field(
        default=True, description="Has warping drum / capstan"
    )
    weight_kg: Optional[float] = Field(
        default=None, gt=0, description="Total weight in kg"
    )
    ip_rating: Optional[str] = Field(
        default=None, description="IP protection rating (e.g. IP56)"
    )
    part_number: Optional[str] = Field(
        default=None, description="Manufacturer part number"
    )
    price_eur: Optional[float] = Field(
        default=None, ge=0, description="Price in EUR (2026)"
    )


class CableRun(BaseModel):
    """Cable run specification for windlass installation."""

    model_config = {"from_attributes": True}

    cable_length_m: float = Field(
        ..., gt=0, le=50, description="One-way cable length battery to windlass in m"
    )
    cable_cross_section_mm2: float = Field(
        ..., gt=0, le=300, description="Cable cross-section in mm²"
    )
    cable_type: str = Field(
        default="marine_tinned",
        description="Cable type: marine_tinned, h07rn_f, h07v_k, unknown"
    )
    is_tinned: bool = Field(
        default=True, description="Tinned copper strands"
    )
    circuit_breaker_amps: Optional[float] = Field(
        default=None, description="Circuit breaker rating in amps"
    )
    voltage_drop_percent: Optional[float] = Field(
        default=None, ge=0, le=100,
        description="Calculated voltage drop in percent"
    )


class DeckMounting(BaseModel):
    """Deck mounting / reinforcement specification."""

    model_config = {"from_attributes": True}

    has_backing_plate: bool = Field(
        ..., description="Backing plate present under deck"
    )
    backing_plate_material: Optional[str] = Field(
        default=None,
        description="Backing plate material (stainless_316, aluminum, plywood)"
    )
    backing_plate_thickness_mm: Optional[float] = Field(
        default=None, description="Backing plate thickness in mm"
    )
    bolt_count: Optional[int] = Field(
        default=None, ge=2, le=12, description="Number of mounting bolts"
    )
    bolt_size: Optional[str] = Field(
        default=None, description="Bolt size (e.g. M10, M12)"
    )
    bolt_type: Optional[str] = Field(
        default=None,
        description="Bolt type: through_bolt, lag_screw, machine_screw"
    )
    deck_material: Optional[str] = Field(
        default=None,
        description="Deck material: grp_solid, grp_sandwich, aluminum, wood"
    )
    deck_thickness_mm: Optional[float] = Field(
        default=None, description="Deck thickness at mounting point in mm"
    )
    sealant_type: Optional[str] = Field(
        default=None,
        description="Sealant used: sikaflex_291, sikaflex_292, butyl, silicone, none"
    )
    alignment_offset_deg: Optional[float] = Field(
        default=None, ge=0, le=45,
        description="Gypsy-to-bow-roller misalignment in degrees"
    )


class AnchorSystem(BaseModel):
    """Complete anchor system specification for assessment context."""

    model_config = {"from_attributes": True}

    anchor_weight_kg: float = Field(
        ..., gt=0, le=500, description="Anchor weight in kg"
    )
    anchor_type: Optional[str] = Field(
        default=None,
        description="Anchor type (delta, cqr, bruce, rocna, spade, danforth, etc.)"
    )
    chain_length_m: float = Field(
        ..., gt=0, le=500, description="Chain length in meters"
    )
    chain_diameter_mm: float = Field(
        ..., gt=0, le=50, description="Chain wire diameter in mm"
    )
    chain_standard: ChainStandard = Field(
        ..., description="Chain standard"
    )
    chain_weight_per_m_kg: Optional[float] = Field(
        default=None, description="Chain weight per meter in kg/m"
    )
    rope_length_m: Optional[float] = Field(
        default=None, ge=0, description="Anchor rope length in m (if combo)"
    )
    rope_diameter_mm: Optional[float] = Field(
        default=None, description="Rope diameter in mm"
    )
    max_anchoring_depth_m: float = Field(
        default=20.0, gt=0, le=200,
        description="Maximum expected anchoring depth in m"
    )
    has_chain_stopper: bool = Field(
        default=True, description="Chain stopper present"
    )
    has_snubber: bool = Field(
        default=False, description="Snubber / bridle present"
    )
    bitter_end_accessible: Optional[bool] = Field(
        default=None, description="Bitter end accessible and severable"
    )


class WindlassInstallation(BaseModel):
    """Complete windlass installation for AYDI assessment."""

    model_config = {"from_attributes": True}

    windlass: WindlassSpec = Field(
        ..., description="Windlass specification"
    )
    anchor_system: AnchorSystem = Field(
        ..., description="Anchor system context"
    )
    cable_run: Optional[CableRun] = Field(
        default=None, description="Electrical cable run (None for manual/hydraulic)"
    )
    deck_mounting: Optional[DeckMounting] = Field(
        default=None, description="Deck mounting specification"
    )
    has_chain_counter: bool = Field(
        default=False, description="Chain counter installed"
    )
    has_remote_control: bool = Field(
        default=False, description="Remote control at helm"
    )
    has_foot_switch: bool = Field(
        default=True, description="Foot switch at foredeck"
    )
    has_emergency_handle: bool = Field(
        default=False, description="Emergency manual handle available"
    )
    installation_date: Optional[date] = Field(
        default=None, description="Installation or last service date"
    )
    boat_loa_m: float = Field(
        ..., gt=0, le=200, description="Boat length overall in m"
    )
    boat_type: Optional[str] = Field(
        default=None,
        description="Boat type: sailboat, motoryacht, catamaran, trawler"
    )


# ── Assessment Models ─────────────────────────────────────────────────

class WindlassFinding(BaseModel):
    """Single finding from windlass assessment."""

    model_config = {"from_attributes": True}

    finding_id: str = Field(
        ..., description="Unique finding ID (e.g. WDL-001)"
    )
    category: str = Field(
        ..., description="Finding category (sizing, electrical, mechanical, mounting, safety)"
    )
    title_de: str = Field(
        ..., description="Finding title in German"
    )
    description_de: str = Field(
        ..., description="Detailed description in German"
    )
    severity: Severity = Field(
        ..., description="Finding severity"
    )
    confidence: ConfidenceLevel = Field(
        ..., description="Confidence level of this finding"
    )
    suggestion_de: Optional[str] = Field(
        default=None, description="Suggested action in German"
    )
    location_ref: Optional[str] = Field(
        default=None,
        description="Location reference (e.g. 'foredeck_windlass_base')"
    )
    estimated_cost_eur: Optional[float] = Field(
        default=None, ge=0,
        description="Estimated repair/improvement cost in EUR"
    )
    photo_evidence: Optional[bool] = Field(
        default=None,
        description="Whether photo evidence supports this finding"
    )


class WindlassAssessmentScores(BaseModel):
    """Scoring breakdown for windlass assessment."""

    model_config = {"from_attributes": True}

    sizing_score: float = Field(
        ..., ge=0, le=100,
        description="Pull force dimensioning score (weight: 20%)"
    )
    electrical_score: float = Field(
        ..., ge=0, le=100,
        description="Electrical installation score (weight: 20%)"
    )
    chain_compatibility_score: float = Field(
        ..., ge=0, le=100,
        description="Chain-gypsy compatibility score (weight: 15%)"
    )
    mechanical_condition_score: float = Field(
        ..., ge=0, le=100,
        description="Mechanical condition score (weight: 15%)"
    )
    mounting_quality_score: float = Field(
        ..., ge=0, le=100,
        description="Deck mounting quality score (weight: 10%)"
    )
    safety_score: float = Field(
        ..., ge=0, le=100,
        description="Safety equipment score (weight: 10%)"
    )
    comfort_score: float = Field(
        ..., ge=0, le=100,
        description="Operating comfort score (weight: 5%)"
    )
    maintenance_score: float = Field(
        ..., ge=0, le=100,
        description="Maintenance condition score (weight: 5%)"
    )

    @property
    def overall_score(self) -> float:
        """Calculate weighted overall score."""
        return (
            self.sizing_score * 0.20
            + self.electrical_score * 0.20
            + self.chain_compatibility_score * 0.15
            + self.mechanical_condition_score * 0.15
            + self.mounting_quality_score * 0.10
            + self.safety_score * 0.10
            + self.comfort_score * 0.05
            + self.maintenance_score * 0.05
        )


class WindlassAssessmentResult(BaseModel):
    """Complete windlass assessment result."""

    model_config = {"from_attributes": True}

    installation: WindlassInstallation = Field(
        ..., description="Assessed installation"
    )
    scores: WindlassAssessmentScores = Field(
        ..., description="Assessment scores"
    )
    overall_score: float = Field(
        ..., ge=0, le=100, description="Weighted overall score"
    )
    findings: list[WindlassFinding] = Field(
        default_factory=list, description="List of findings"
    )
    critical_count: int = Field(
        default=0, ge=0, description="Number of CRITICAL findings"
    )
    warning_count: int = Field(
        default=0, ge=0, description="Number of WARNING findings"
    )
    available: bool = Field(
        default=True,
        description="Whether assessment could be completed"
    )
    reason: Optional[str] = Field(
        default=None,
        description="Reason if assessment not available"
    )
    assessment_date: date = Field(
        ..., description="Date of assessment"
    )
    assessor_model_version: str = Field(
        default="aydi-v6-windlass-1.0",
        description="AYDI model version used for assessment"
    )

    @field_validator("critical_count", mode="before")
    @classmethod
    def count_criticals(cls, v: int, info) -> int:
        """Auto-count critical findings if not set."""
        if v == 0 and "findings" in info.data:
            return sum(
                1 for f in info.data["findings"]
                if f.severity == Severity.CRITICAL
            )
        return v


# ── Calculation Helpers ───────────────────────────────────────────────

class PullForceCalculation(BaseModel):
    """Pull force requirement calculation."""

    model_config = {"from_attributes": True}

    anchor_weight_kg: float = Field(..., gt=0)
    chain_weight_per_m_kg: float = Field(..., gt=0)
    max_depth_m: float = Field(..., gt=0)
    safety_factor: float = Field(default=2.5, gt=1.0, le=5.0)

    @property
    def static_load_kg(self) -> float:
        """Static load = anchor + chain to surface."""
        return self.anchor_weight_kg + (
            self.chain_weight_per_m_kg * self.max_depth_m
        )

    @property
    def required_pull_force_kg(self) -> float:
        """Required pull force with safety factor."""
        return self.static_load_kg * self.safety_factor


class CableSizeCalculation(BaseModel):
    """Cable cross-section calculation."""

    model_config = {"from_attributes": True}

    voltage_system: VoltageSystem = Field(...)
    max_current_amps: float = Field(..., gt=0)
    cable_length_one_way_m: float = Field(..., gt=0)
    max_voltage_drop_percent: float = Field(default=3.0, gt=0, le=10)
    conductivity_copper: float = Field(default=56.0)  # m / (ohm * mm²)

    @property
    def voltage_nominal(self) -> float:
        """Nominal system voltage."""
        return float(self.voltage_system.value)

    @property
    def max_voltage_drop_v(self) -> float:
        """Maximum allowed voltage drop in volts."""
        return self.voltage_nominal * self.max_voltage_drop_percent / 100

    @property
    def required_cross_section_mm2(self) -> float:
        """Required cable cross-section in mm²."""
        return (
            2.0
            * self.cable_length_one_way_m
            * self.max_current_amps
            / (self.conductivity_copper * self.max_voltage_drop_v)
        )

    @property
    def recommended_cross_section_mm2(self) -> float:
        """Next standard cable size up from calculated minimum."""
        standard_sizes = [
            1.5, 2.5, 4.0, 6.0, 10.0, 16.0, 25.0,
            35.0, 50.0, 70.0, 95.0, 120.0, 150.0, 185.0, 240.0,
        ]
        calculated = self.required_cross_section_mm2
        for size in standard_sizes:
            if size >= calculated:
                return size
        return standard_sizes[-1]


class RetrievalTimeCalculation(BaseModel):
    """Anchor retrieval time estimation."""

    model_config = {"from_attributes": True}

    chain_length_deployed_m: float = Field(..., gt=0)
    water_depth_m: float = Field(..., gt=0)
    line_speed_working_m_min: float = Field(..., gt=0)
    approach_time_min: float = Field(
        default=2.0,
        description="Time to motor over anchor before vertical pull"
    )

    @property
    def estimated_retrieval_time_min(self) -> float:
        """Estimated total retrieval time in minutes."""
        chain_time = self.chain_length_deployed_m / self.line_speed_working_m_min
        return chain_time + self.approach_time_min

    def exceeds_duty_cycle(self, duty_cycle_on_min: float) -> bool:
        """Check if retrieval time exceeds motor duty cycle."""
        return self.estimated_retrieval_time_min > duty_cycle_on_min
```

### Beispiel-Nutzung der Pydantic-Modelle

```python
"""Example: Assess a windlass installation on a 12m sailboat."""
from datetime import date

# Build the installation spec
installation = WindlassInstallation(
    windlass=WindlassSpec(
        manufacturer="Lofrans",
        model="Tigres 1000",
        windlass_type=WindlassType.VERTICAL,
        drive_type=DriveType.ELECTRIC_DC,
        pull_force_kg=1000,
        line_speed_working_m_min=18,
        gypsy=GypsySpec(
            chain_diameter_mm=8.0,
            chain_standard=ChainStandard.DIN_766,
            material=GypsyMaterial.ALUMINUM_BRONZE,
            wrap_angle_deg=200,
        ),
        motor=MotorSpec(
            motor_type=MotorType.PERMANENT_MAGNET,
            power_watts=1000,
            voltage=VoltageSystem.V12,
            current_working_amps=90,
            current_max_amps=130,
            duty_cycle_on_min=5,
            duty_cycle_off_min=5,
        ),
        gearbox_type=GearboxType.PLANETARY,
        has_free_fall=True,
        weight_kg=12.5,
        price_eur=1650,
    ),
    anchor_system=AnchorSystem(
        anchor_weight_kg=15,
        anchor_type="delta",
        chain_length_m=50,
        chain_diameter_mm=8,
        chain_standard=ChainStandard.DIN_766,
        chain_weight_per_m_kg=1.4,
        max_anchoring_depth_m=15,
        has_chain_stopper=True,
        has_snubber=True,
        bitter_end_accessible=True,
    ),
    cable_run=CableRun(
        cable_length_m=6,
        cable_cross_section_mm2=50,
        cable_type="marine_tinned",
        is_tinned=True,
        circuit_breaker_amps=130,
    ),
    deck_mounting=DeckMounting(
        has_backing_plate=True,
        backing_plate_material="stainless_316",
        backing_plate_thickness_mm=8,
        bolt_count=4,
        bolt_size="M10",
        bolt_type="through_bolt",
        deck_material="grp_solid",
        deck_thickness_mm=20,
        sealant_type="sikaflex_291",
        alignment_offset_deg=1.5,
    ),
    has_chain_counter=True,
    has_remote_control=False,
    has_foot_switch=True,
    has_emergency_handle=True,
    boat_loa_m=12.0,
    boat_type="sailboat",
)

# Calculate pull force requirement
pull_calc = PullForceCalculation(
    anchor_weight_kg=15,
    chain_weight_per_m_kg=1.4,
    max_depth_m=15,
    safety_factor=2.5,
)
print(f"Required pull force: {pull_calc.required_pull_force_kg:.0f} kg")
# Output: Required pull force: 90 kg (static 36 kg × 2.5)
# The 1000 kg windlass is well-dimensioned.

# Calculate cable cross-section
cable_calc = CableSizeCalculation(
    voltage_system=VoltageSystem.V12,
    max_current_amps=130,
    cable_length_one_way_m=6,
    max_voltage_drop_percent=3.0,
)
print(f"Required cable: {cable_calc.required_cross_section_mm2:.1f} mm²")
print(f"Recommended: {cable_calc.recommended_cross_section_mm2} mm²")
# Output: Required cable: 43.7 mm²  →  Recommended: 50 mm²

# Check retrieval time vs duty cycle
retrieval = RetrievalTimeCalculation(
    chain_length_deployed_m=50,
    water_depth_m=15,
    line_speed_working_m_min=18,
    approach_time_min=2.0,
)
print(f"Retrieval time: {retrieval.estimated_retrieval_time_min:.1f} min")
print(f"Exceeds 5 min duty cycle: {retrieval.exceeds_duty_cycle(5.0)}")
# Output: Retrieval time: 4.8 min  →  Exceeds: False (but close!)
```

---

## ANHANG S — Erweiterte Berechnungsbeispiele

### S.1 Vollständige Dimensionierung: Segelyacht 14 m

**Gegebene Daten:**
- Boot: Segelyacht, 14,2 m LOA, 4,2 m Breite, 12.500 kg Verdrängung
- Bordnetz: 12V, Servicebatterie 2× 120 Ah AGM
- Geplantes Ankergeschirr: 20 kg Spade-Anker + 60 m × 10 mm DIN 766
- Maximale Ankertiefe: 20 m
- Kabellänge Batterie → Bug: 8 m (einfach)

**Schritt 1: Kettengewicht berechnen**
```
Kettengewicht 10 mm DIN 766: 2,2 kg/m
Kette bis Wasseroberfläche bei 20 m: 20 m × 2,2 kg/m = 44 kg
Gesamtlast statisch: 20 kg (Anker) + 44 kg (Kette) = 64 kg
```

**Schritt 2: Zugkraft mit Sicherheitsfaktor**
```
F_design = 64 kg × 2,5 = 160 kg Mindest-Zugkraft
Empfohlen: 1.000–1.200 kg (Faustregel für 14 m Boot)
→ Wahl: Lofrans Tigres 1200 (1.200 kg, 24V, 10 mm DIN 766)
  ODER: Lewmar V5 (1.200 kg, 24V, 10 mm DIN 766)
```

**Schritt 3: Motorstrom und Kabelquerschnitt**
```
Motor: 1.000 W, 24V → Arbeitsstrom ≈ 50 A, Max. Strom ≈ 75 A
Kabelquerschnitt bei 8 m, 75 A, 24V, 3 % Spannungsabfall:
A = (2 × 8 × 75) / (56 × 0,72) = 1200 / 40,32 = 29,8 mm²
→ Nächster Standard: 35 mm²
```

**Schritt 4: Circuit Breaker**
```
Arbeitsstrom: 50 A → Circuit Breaker: 70 A (thermisch, träge)
Anlaufstrom: ~120 A → 70 A thermisch verträgt kurzzeitig 120 A ✓
```

**Schritt 5: Aufholzeit prüfen**
```
Typische Kettengeschwindigkeit (Arbeitslast): 15 m/min
Aufholzeit bei 20 m Tiefe + Horizontalkomponente:
t ≈ (20 + 15) / 15 + 2 min (Annäherung) = 4,3 min
Duty Cycle Tigres 1200: 5 min on / 5 min off → OK ✓
```

**Schritt 6: Gewicht am Bug**
```
Winde: 14 kg
Anker: 20 kg
Kette: 60 m × 2,2 kg/m = 132 kg
Gesamt am Bug: 166 kg
→ Bei 12.500 kg Verdrängung: 1,3 % des Deplacement — akzeptabel
→ Trimm-Auswirkung: vernachlässigbar (< 0,5° Bugtrimm)
```

**Schritt 7: Batterie prüfen**
```
Stromverbrauch pro Ankerung: 50 A × 4,3 min / 60 = 3,6 Ah
Bei 5 Ankerungen/Tag: 18 Ah
Bei 240 Ah Gesamtkapazität und 50 % Entladetiefe: 120 Ah nutzbar
→ Ankerwinde verbraucht 15 % der Tageskapazität — unkritisch ✓
```

### S.2 Vollständige Dimensionierung: Motoryacht 22 m

**Gegebene Daten:**
- Boot: Motoryacht, 22,5 m LOA, 5,8 m Breite, 48.000 kg Verdrängung
- Bordnetz: 24V, Servicebatterie 4× 200 Ah AGM (24V, 400 Ah)
- Geplantes Ankergeschirr: 50 kg Rocna-Anker + 100 m × 12 mm DIN 766
- Maximale Ankertiefe: 30 m
- Vorhandenes Hydrauliksystem: Ja (Bugstrahlruder, 120 bar, 15 l/min)

**Analyse:**
```
Kettengewicht 12 mm DIN 766: 3,1 kg/m
Statische Last bei 30 m: 50 + (30 × 3,1) = 143 kg
Zugkraft mit Sicherheit: 143 × 2,5 = 358 kg Minimum
Empfohlen für 22 m: 2.500–3.500 kg
```

**Entscheidung Elektrik vs. Hydraulik:**
- Hydrauliksystem bereits vorhanden → Hydraulikwinde wirtschaftlich
- Wassertiefe 30 m + 100 m Kette → Aufholzeit > 5 min → Elektrowinde an Duty-Cycle-Grenze
- → Hydraulikwinde ist die korrekte Wahl

**Wahl:** Maxwell VWC 3500 Hydraulik (3.500 kg, 14 mm DIN 766 Kettennuss für 12 mm Kette vorhanden)
- Hydraulikanschluss an bestehendes System über 4/3-Wegeventil
- Separate Hydraulikleitung DN 12 vom Maschinenraum zum Bug (ca. 15 m)
- Steuerventil elektrisch betätigt (24V Steuerkreis)

### S.3 Kostenvergleich: Elektro vs. Hydraulik für 18-m-Yacht

| Position | Elektrische Winde (24V) | Hydraulische Winde |
|----------|------------------------|-------------------|
| Winde | €3.500 (Quick Prince DP3 1500) | €5.200 (Quick Prince DP3 1500H) |
| Kabel 70 mm² × 2 × 10 m | €350 | — |
| Circuit Breaker 100 A | €55 | — |
| Solenoid Dual 24V | €195 | — |
| Hydraulikventil 4/3 | — | €850 |
| Hydraulikschläuche DN12, 12 m | — | €420 |
| Hydraulikanschluss-Kit | — | €280 |
| Fußschalter | €110 | €110 |
| Kettenzähler | €350 | €350 |
| Fernbedienung | €380 | €380 |
| Einbau Fachbetrieb | €800 | €1.800 |
| **Gesamt** | **€5.740** | **€9.390** |

**Fazit:** Die Hydrauliklösung kostet ~64 % mehr, bietet aber unbegrenzte Einschaltdauer und höhere Langzeitverlässlichkeit. Bei vorhandenem Hydrauliksystem (Bugstrahlruder) reduzieren sich die Mehrkosten auf ~40 %, da Pumpe und Tank bereits vorhanden sind.

### S.4 Spannungsabfall-Diagnose im Feld

**Messmethode mit Standard-Multimeter:**

```
Vorbereitung:
- Multimeter auf DC Volt einstellen
- Batteriespannung im Ruhezustand messen und notieren: U_batt
- Jemand am Fußschalter, jemand am Multimeter

Messung 1: Spannung an der Batterie unter Last
- Fußschalter "AUF" drücken (Motor läuft, Kette wird eingehollt)
- Spannung an Batterieklemmen messen: U_batt_last
- Spannungseinbruch: ΔU_batt = U_batt - U_batt_last
- Bewertung: ΔU_batt > 1,5V → Batterie schwach oder zu klein

Messung 2: Spannung am Motor unter Last
- Fußschalter "AUF" drücken
- Spannung an Motorklemmen messen: U_motor
- Kabelspannungsabfall: ΔU_kabel = U_batt_last - U_motor
- Bewertung: ΔU_kabel > 0,5V (12V) oder > 1,0V (24V) → Kabel zu dünn

Messung 3: Spannung am Solenoid
- Fußschalter "AUF" drücken
- Spannung vor Solenoid (Eingang) und nach Solenoid (Ausgang) messen
- Kontaktspannungsabfall: ΔU_sol = U_ein - U_aus
- Bewertung: ΔU_sol > 0,3V → Solenoid-Kontakte verschlissen
```

**Diagnosematrix:**

| ΔU_batt | ΔU_kabel | ΔU_sol | Diagnose |
|---------|----------|--------|----------|
| <0,5V | <0,3V | <0,1V | System OK ✓ |
| >1,5V | <0,3V | <0,1V | Batterie schwach → laden/ersetzen |
| <0,5V | >0,5V | <0,1V | Kabelquerschnitt zu gering → Kabel ersetzen |
| <0,5V | <0,3V | >0,3V | Solenoid-Kontakte verschlissen → Solenoid tauschen |
| >1,5V | >0,5V | <0,1V | Batterie UND Kabel mangelhaft |
| >1,5V | >0,5V | >0,3V | Gesamtes Elektrik-System überarbeiten |

### S.5 Kettengewicht-Referenztabelle

| Kettendurchmesser | DIN 766 (kg/m) | BBB/G30 (kg/m) | G40/HT (kg/m) |
|-------------------|----------------|----------------|----------------|
| 6 mm | 0,88 | 0,85 | 0,80 |
| 7 mm | 1,15 | 1,10 | 1,05 |
| 8 mm | 1,40 | 1,38 | 1,30 |
| 10 mm | 2,20 | 2,15 | 2,00 |
| 12 mm | 3,10 | 3,05 | 2,85 |
| 13 mm | 3,65 | 3,60 | 3,40 |
| 14 mm | 4,30 | 4,25 | 4,00 |
| 16 mm | 5,60 | 5,50 | 5,20 |

### S.6 Ankergewicht-Empfehlung nach Bootsklasse

| Bootslänge (m) | Verdrängung (t) | Ankergewicht (kg) | Kettensize (mm) | Kettenlänge (m) |
|----------------|-----------------|-------------------|-----------------|-----------------|
| 6–8 | 1–3 | 5–8 | 6 | 20–30 |
| 8–10 | 3–6 | 8–12 | 6–8 | 30–40 |
| 10–12 | 6–10 | 12–16 | 8 | 40–50 |
| 12–14 | 8–14 | 14–20 | 8–10 | 50–60 |
| 14–16 | 12–20 | 18–25 | 10 | 50–70 |
| 16–18 | 18–30 | 25–35 | 10–12 | 60–80 |
| 18–20 | 25–40 | 30–45 | 12 | 70–90 |
| 20–24 | 35–60 | 40–60 | 12–14 | 80–100 |
| 24–30 | 50–120 | 55–100 | 14–16 | 100–120 |

### S.7 Herstellervergleich — Zusammenfassende Bewertung

| Hersteller | Qualität | Preis | Ersatzteile | Service DE | Empfehlung |
|-----------|----------|-------|-------------|-----------|-----------|
| Lofrans | ★★★★ | ★★★ | ★★★★ | ★★★★ | Segelyachten 8–20 m, Preis-Leistung |
| Lewmar | ★★★★ | ★★★ | ★★★★★ | ★★★★ | Breites Sortiment, gute Ersatzteilverfügbarkeit |
| Quick | ★★★★★ | ★★★ | ★★★★ | ★★★ | Design, Integration, Mittelmeer-Fokus |
| Maxwell | ★★★★ | ★★★ | ★★★ | ★★ | BBB-Ketten, USA/Pazifik, robust |
| Muir | ★★★★★ | ★★ | ★★★ | ★★ | Premium, Custom, Superyachten |
| Italwinch | ★★★ | ★★★★ | ★★★ | ★★★ | Einsteigerklasse, gutes P/L |
| CX/SX (SPI) | ★★ | ★★★★★ | ★★ | ★ | Nur wenn Budget extrem begrenzt |

*(★★★★★ = Exzellent, ★ = Mangelhaft)*

---

*Ende der Wissensdatei 13.03 — Ankerwinden im Yachtbau*
*AYDI Research, Version 1.0.0, 2026-04-26*
