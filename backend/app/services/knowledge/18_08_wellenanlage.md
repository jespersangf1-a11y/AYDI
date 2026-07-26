---
titel: "Wellenanlage — Welle, Stevenrohr und Wellendichtung"
kategorie: "Motoren und Antrieb"
unterkategorie: "Wellenanlage"
version: "2.0"
letzte_aktualisierung: "2026-04"
autor: "AYDI Maritime Knowledge Base"
---

# 18_08 — Wellenanlage — Welle, Stevenrohr und Wellendichtung

---

## Inhaltsverzeichnis

1. [Einführung](#1-einführung)
2. [Propellerwelle — Material, Dimensionierung und Konstruktion](#2-propellerwelle--material-dimensionierung-und-konstruktion)
3. [Stevenrohr — Aufbau und Lagerung](#3-stevenrohr--aufbau-und-lagerung)
4. [Cutless-Bearing / Wellenlager](#4-cutless-bearing--wellenlager)
5. [Wellendichtung — Stopfbuchse (Packing Gland)](#5-wellendichtung--stopfbuchse-packing-gland)
6. [Wellendichtung — Lippendichtung (PSS / PYI Pacific Seals)](#6-wellendichtung--lippendichtung-pss--pyi-pacific-seals)
7. [Wellendichtung — Tides Marine SureSeal und weitere Systeme](#7-wellendichtung--tides-marine-sureseal-und-weitere-systeme)
8. [Flexible Kupplung](#8-flexible-kupplung)
9. [Motorausrichtung (Engine Alignment)](#9-motorausrichtung-engine-alignment)
10. [Wellenbremse (Shaft Brake)](#10-wellenbremse-shaft-brake)
11. [Drucklager (Thrust Bearing)](#11-drucklager-thrust-bearing)
12. [P-Bracket / A-Bracket / Strut](#12-p-bracket--a-bracket--strut)
13. [Galvanische Korrosion und Elektrolyse](#13-galvanische-korrosion-und-elektrolyse)
14. [Volvo Saildrive — Wellenabdichtung und Manschette](#14-volvo-saildrive--wellenabdichtung-und-manschette)
15. [Fehlerbild-Atlas](#15-fehlerbild-atlas)
16. [Troubleshooting](#16-troubleshooting)
17. [FAQ](#17-faq)
18. [Glossar](#18-glossar)
19. [Schnell-Referenz](#19-schnell-referenz)
20. [ANHANG A–H: Fallstudien](#20-anhang-ah-fallstudien)
21. [ANHANG I–R: Pydantic v2 Datenmodelle](#21-anhang-ir-pydantic-v2-datenmodelle)

---
---

## 1. Einführung

### 1.1 Warum die Wellenanlage eine sicherheitskritische Komponente ist

Die Wellenanlage verbindet Motor und Propeller — sie überträgt Drehmoment,
nimmt den Propellerschub auf und dichtet gleichzeitig das Rumpfinnere
gegen das umgebende Wasser ab. Versagt eine Komponente der Wellenanlage,
drohen schwere Folgen:

- **Wassereinbruch**: Eine undichte oder gebrochene Wellendichtung kann
  zum Sinken führen. Die Wellenöffnung liegt unterhalb der Wasserlinie
  und hat bei einem typischen 1"-Schaft bereits einen Querschnitt von
  ~5 cm² — genug für einen Wassereinbruch von 30–50 l/min bei 1 m Tiefe.
- **Antriebsausfall**: Wellenbruch, Kupplungsversagen oder gelöster Konus
  bedeuten sofortigen Verlust des Antriebs — in schwerem Wetter, in
  Gezeitenströmen oder bei Hafenansteuerung potenziell lebensbedrohlich.
- **Vibration und Folgeschäden**: Schlechte Motorausrichtung,
  verschlissenes Cutless-Bearing oder unwuchtiger Propeller verursachen
  Vibrationen, die Motor, Getriebe, Lager und Rumpfstruktur schädigen.
- **Galvanische Korrosion**: Die Wellenanlage verbindet verschiedene
  Metalle im Seewasser — Bronze-Stevenrohr, Edelstahlwelle,
  Bronze-Propeller — und ist daher ein Hotspot für Elektrolyse.

**Statistik (BSH / BoatUS / ADAC 2025):**
- 12 % aller Antriebsstörungen → Wellenanlage
- 8 % aller Wassereinbrüche → undichte Wellendichtung
- 18 % aller Vibrationsprobleme → Wellenausrichtung / Cutless-Bearing
- Durchschnittliche Reparaturkosten Wellenanlage: 400–8.000 EUR
- Wellenbruch mit Wassereinbruch: 5.000–30.000 EUR (Boot/Bergung)
- Motorschaden durch chronische Fehlausrichtung: 3.000–15.000 EUR

### 1.2 Systemüberblick: Vom Motor zum Propeller

Die Wellenanlage einer typischen Yacht besteht aus folgenden Komponenten
(Motor → Propeller):

```
Motor → Motorkupplung → Getriebe → Getriebeausgangsflansch →
  Flexible Kupplung → Propellerwelle → Stevenrohr (mit Cutless-Bearing) →
  Wellendichtung → P-Bracket (optional) → Propeller
```

| Komponente | Funktion | Typische Lebensdauer |
|-----------|---------|:---:|
| Propellerwelle | Drehmoment-Übertragung, Propellermontage | 20–40+ Jahre |
| Stevenrohr | Wellenführung durch den Rumpf | Bootslebensdauer |
| Cutless-Bearing | Wasserlager der Welle im Stevenrohr | 5–15 Jahre |
| Stopfbuchse / PSS | Abdichtung Welle ↔ Rumpf | 5–20 Jahre |
| Flexible Kupplung | Vibrationsabsorption, Ausrichtungstoleranz | 10–20 Jahre |
| Drucklager | Nimmt axialen Propellerschub auf | Im Getriebe integriert |
| P-Bracket / Strut | Abstützung der Welle am Rumpf | Bootslebensdauer |
| Wellenbremse | Verhindert Wellenrotation unter Segel | 15–25 Jahre |
| Zinkanode(n) | Galvanischer Schutz | 6–18 Monate |

### 1.3 Wellenanlage vs. Saildrive vs. Außenborder

| Merkmal | Wellenanlage | Saildrive | Außenborder |
|---------|:---:|:---:|:---:|
| Typische Bootsgröße | 8–50+ m | 8–16 m Segelboote | <10 m |
| Leistungsbereich | 10–5.000+ PS | 10–75 PS | 2–600 PS |
| Effizienz | 90–97 % | 92–96 % | 50–70 % (Lenk-Verluste) |
| Wartungskomplexität | Mittel–Hoch | Gering–Mittel | Gering |
| Abdichtungsrisiko | Mittel (Dichtung) | Gering (Manschette) | Kein (über Spiegel) |
| Manövrierbarkeit | Gering (Ruder nötig) | Gering (Ruder nötig) | Hoch (lenkbar) |
| Reparierbarkeit | Überall möglich | Nur Volvo-/Yanmar-Werkstatt | Überall möglich |
| Langfahrt-Eignung | Sehr gut | Gut | Eingeschränkt |
| Typische Kosten (Neuinstallation) | 3.000–25.000 EUR | 6.000–15.000 EUR | 2.000–50.000 EUR |

### 1.4 Historische Entwicklung der Wellenanlage

Die Wellenanlage hat sich über 150 Jahre entwickelt:

- **1850er–1900**: Erste Dampfschiffe mit starren Gusseisenwellen,
  Holz-Wellenlager (Lignum vitae), Hanf-Stopfbuchsen.
- **1920er**: Bronzewellen werden Standard, erste Gummi-Wellenlager.
- **1950er**: Monel-400 und rostfreie Stahlwellen.
  Cutless-Bearing (Johnson) wird Industriestandard.
- **1970er**: Flexible Kupplungen ersetzen starre Flanschverbindungen.
  Erste Lippendichtungen (PSS) als Alternative zur Stopfbuchse.
- **1990er**: Aquamet 22 wird Standardwellenmaterial.
  Laserausrichtung wird verfügbar.
- **2000er**: PYI PSS (Pacific Shaft Seal) wird Marktführer bei
  mechanischen Gleitringdichtungen. Tides Marine SureSeal als Alternative.
- **2010er**: Verbesserte Carbon-Graphit-Dichtflächen, keramische
  Gleitringe, Dripless-Systeme werden Standard bei Neubauten.
- **2020er**: Composite-Wellen im Testbetrieb, Smart-Sensoren für
  Vibrationsüberwachung, AGS-Systeme (Active Galvanic Shield).

### 1.5 Normen und Vorschriften

| Norm / Standard | Inhalt | Relevanz |
|----------------|--------|----------|
| ISO 1120 | Fördergurte — Festigkeit mechanischer Verbindungen (kein Bezug zur Wellenanlage) | Nicht anwendbar — frühere Fehlzuordnung |
| ISO 7840 | Brennstoff-Systeme (indirekt: Wellenabdichtung als Bilge-Durchführung) | Brandschutz |
| ISO 8847 | Kleine Wasserfahrzeuge — Ruderanlagen, Seilzug-/Rollensysteme (Steuerung) | Steuerung, nicht Antrieb — frühere Fehlzuordnung |
| Lloyd's Register SSC | Shaft & Stern Tube Classification | Klassifizierungsstandard |
| ABYC P-6 | Propeller Shafts | US-Standard, international referenziert |
| GL Rules | Germanischer Lloyd Vorschriften Sportboote | Wellendimensionierung |
| DNV Rules | Schaftberechnung, Materialanforderungen | Klassifizierungsstandard |
| SAE J755 | Shaft tapers und keyways | Konus-Normen |

> ✅ Aufgelöst (Audit): ISO 1120 = "Fördergurte — Bestimmung der Festigkeit mechanischer Verbindungen" und ISO 8847 = "Kleine Wasserfahrzeuge — Ruderanlagen — Seilzug-/Rollensysteme" (Steuerung) — beide haben KEINEN Bezug zur Wellendimensionierung; die Tabellenzeilen sind entsprechend korrigiert. Maßgeblich für die Wellenanlage sind stattdessen die Klassifikationsregeln (Lloyd's Register, GL, DNV) und ABYC P-6. Confidence: documented. Quelle: ISO-Katalog iso.org/standard/35357.html (ISO 1120), iso.org/standard/38439.html (ISO 8847).

---
---

## 2. Propellerwelle — Material, Dimensionierung und Konstruktion

### 2.1 Wellenmaterialien im Vergleich

Die Wahl des Wellenmaterials ist eine der wichtigsten Entscheidungen
bei der Wellenanlage. Das Material muss korrosionsbeständig, zugfest,
ermüdungsfest und kompatibel mit Lagern und Dichtungen sein.

| Material | Legierung | Zugfestigkeit (MPa) | Streckgrenze (MPa) | Korrosionsbeständigkeit | Preis-Index | Einsatz |
|----------|-----------|:---:|:---:|:---:|:---:|---------|
| Aquamet 22 | UNS S21904 | 760 | 450 | Sehr gut | 1,5 | Standard Yachtbau |
| Aquamet 17 | UNS S17400 (PH 17-4) | 1.000 | 790 | Gut–Sehr gut | 2,0 | Leistungsanwendungen |
| Aquamet 18 | UNS S45500 (PH 15-5) | 1.170 | 1.030 | Gut | 2,2 | Rennboote, Hochleistung |
| Aqualoy 22 | ähnlich Aquamet 22 | 760 | 450 | Sehr gut | 1,5 | Alternative zu Aquamet 22 |
| AISI 316L | UNS S31603 | 480 | 170 | Gut | 1,0 | Budget, Süßwasser |
| AISI 304 | UNS S30400 | 515 | 205 | Mäßig | 0,8 | NICHT empfohlen für Seewasser |
| Monel K-500 | UNS N05500 | 1.100 | 790 | Hervorragend | 4,0 | Superyachten, Marineschiffe |
| Monel 400 | UNS N04400 | 550 | 240 | Hervorragend | 3,0 | Ältere Qualitätswellen |
| Tobin-Bronze | CDA C46400 | 380 | 170 | Gut | 2,5 | Historisch, selten neu |
| Nitronic 50 | UNS S20910 | 690 | 380 | Hervorragend | 2,8 | Spezialanwendungen |

**Empfehlungen nach Bootsklasse:**

| Bootsklasse | Empfohlenes Material | Begründung |
|------------|---------------------|-----------|
| Produktions-Segelboot 8–12 m | Aquamet 22 oder 316L | Preis-Leistung |
| Produktions-Motorboot 8–15 m | Aquamet 22 | Standard |
| Semi-Custom 12–20 m | Aquamet 22 | Bewährt, gute Verfügbarkeit |
| Custom Segelboot 15–25 m | Aquamet 22 / Aquamet 17 | Je nach Leistungsbedarf |
| Motoryacht 20–35 m | Aquamet 17 | Höhere Festigkeit |
| Superyacht 30+ m | Aquamet 17 / Monel K-500 | Klassifikationsanforderungen |
| Rennboot / High Performance | Aquamet 18 / Monel K-500 | Maximale Festigkeit |

### 2.2 Wellendurchmesser-Berechnung

Der Wellendurchmesser wird primär durch das zu übertragende Drehmoment
bestimmt. Die wichtigsten Berechnungsmethoden:

**Methode 1: GL/DNV vereinfacht (Sportboote)**

```
d = K × ³√(P / n)
```

Dabei:
- d = Wellendurchmesser in mm
- P = Motorleistung in kW
- n = Wellendrehzahl in U/min
- K = Materialfaktor (Aquamet 22: 100, 316L: 110, Monel: 85)

**Beispielrechnung:**
- Motor: 40 kW, Drehzahl: 2.500 U/min
- d = 100 × ³√(40/2.500) = 100 × ³√0,016 = 100 × 0,252 = 25,2 mm
- Gewählt: 25 mm (1") — nächster Standarddurchmesser

**Methode 2: ABYC P-6 (US-Standard, international verbreitet)**

```
d = 3,27 × ³√(P × S_f / (n × T_s))
```

Dabei:
- d = Wellendurchmesser in Zoll
- P = Leistung in PS
- n = Wellendrehzahl in U/min
- S_f = Sicherheitsfaktor (2,0 Standard, 2,5 Langfahrt)
- T_s = Zulässige Scherspannung (Aquamet 22: 8.500 psi, 316L: 6.500 psi)

**Standard-Wellendurchmesser nach Leistung:**

| Motorleistung | Wellendrehzahl | Empfohlener Durchmesser | Standard-Zollmaß |
|:---:|:---:|:---:|:---:|
| 10–15 PS | 2.500–3.000 | 20 mm | 3/4" |
| 15–25 PS | 2.500–3.000 | 22 mm | 7/8" |
| 25–40 PS | 2.000–2.800 | 25 mm | 1" |
| 40–60 PS | 2.000–2.800 | 30 mm | 1-1/8" |
| 60–100 PS | 1.800–2.500 | 35 mm | 1-3/8" |
| 100–150 PS | 1.800–2.500 | 40 mm | 1-1/2" |
| 150–250 PS | 1.500–2.200 | 45 mm | 1-3/4" |
| 250–400 PS | 1.500–2.000 | 50 mm | 2" |
| 400–600 PS | 1.200–1.800 | 60 mm | 2-3/8" |
| 600–1.000 PS | 1.000–1.500 | 70 mm | 2-3/4" |

### 2.3 Konus (Taper) und Passfeder (Keyway)

Der Propeller wird auf dem Wellenende über einen Konus (Taper) und
eine Passfeder (Keyway) befestigt. Diese Verbindung muss das gesamte
Drehmoment übertragen und gleichzeitig demontierbar sein.

**Standard-Konus nach SAE J755:**

| Wellendurchmesser | SAE-Taper | Konusverhältnis | Keyway-Breite | Keyway-Tiefe |
|:---:|:---:|:---:|:---:|:---:|
| 3/4" (19 mm) | #1 | 1:16 | 3/16" | 3/32" |
| 7/8" (22 mm) | #2 | 1:16 | 3/16" | 3/32" |
| 1" (25 mm) | #3 | 1:16 | 1/4" | 1/8" |
| 1-1/8" (29 mm) | #4 | 1:12 | 1/4" | 1/8" |
| 1-1/4" (32 mm) | #5 | 1:12 | 5/16" | 5/32" |
| 1-3/8" (35 mm) | #6 | 1:12 | 3/8" | 3/16" |
| 1-1/2" (38 mm) | #7 | 1:12 | 3/8" | 3/16" |
| 1-3/4" (44 mm) | #8 | 1:10 | 1/2" | 1/4" |
| 2" (50 mm) | #9 | 1:10 | 1/2" | 1/4" |

**Konus-Kontakt-Prüfung (Bluing-Test):**
1. Tuschierfarbe (Prussian Blue) dünn auf Wellenkonus auftragen.
2. Propeller aufsetzen und drehen.
3. Kontaktfläche prüfen: Mindestens 70 % gleichmäßiger Kontakt.
4. < 70 % → Konus nachschleifen oder Welle ersetzen.

**Passfeder-Probleme und Diagnose:**
- **Gelängte Passfeder**: Drehmoment hat die Passfeder verformt →
  Passfedernut ausgearbeitet. Ursache: Konus nicht korrekt angezogen.
- **Korrodierte Passfedernut**: Feuchtigkeit in der Nut → Spaltkorrosion.
  Edelstahl-Passfedern verwenden, Konus mit Tef-Gel montieren.
- **Falsches Passfeder-Material**: Messing-Passfedern bei Bronze-Propellern
  auf Edelstahlwelle → galvanische Korrosion. Korrekt: Edelstahl-Passfeder.

### 2.4 Propellermutter und Sicherung

| Sicherungssystem | Beschreibung | Empfehlung |
|-----------------|-------------|-----------|
| Standard-Mutter + Splint | Kronenmutter mit Splint durch Wellenende | Standard, zuverlässig |
| Selbstsichernde Mutter | Nyloc-Mutter (NICHT empfohlen im Seewasser) | Nicht verwenden |
| Doppelmutter | Zwei Muttern gegeneinander gekontert | Gut, schwer zugänglich |
| PYI Propeller Nut | Spezial-Sicherungsmutter mit Zinkanode | Optimal, teurer |
| Tab-Washer | Sicherungsblech mit umgebogener Lasche | Gut, Einmalgebrauch |

**Anzugsdrehmoment Propellermutter:**

| Wellendurchmesser | Anzugsdrehmoment | Methode |
|:---:|:---:|---------|
| 3/4" (19 mm) | 55–70 Nm | Handdrehmomentschlüssel |
| 1" (25 mm) | 100–135 Nm | Handdrehmomentschlüssel |
| 1-1/4" (32 mm) | 170–200 Nm | Handdrehmomentschlüssel |
| 1-1/2" (38 mm) | 270–340 Nm | Multiplikator oder hydraulisch |
| 2" (50 mm) | 500–680 Nm | Hydraulischer Spanner |

### 2.5 Wellenlänge und Steifigkeit

Die Wellenanlage muss ausreichend steif sein, um Durchbiegung unter
Last zu begrenzen. Übermäßige Durchbiegung führt zu Vibrationen,
Lagerversagen und Dichtungsproblemen.

**Maximale freie Wellenlänge (ohne Zwischenlager):**

| Wellendurchmesser | Max. freie Länge (Stahl) | Max. freie Länge (empfohlen) |
|:---:|:---:|:---:|
| 25 mm (1") | 1.200 mm | 900 mm |
| 30 mm (1-1/8") | 1.500 mm | 1.100 mm |
| 35 mm (1-3/8") | 1.800 mm | 1.400 mm |
| 40 mm (1-1/2") | 2.100 mm | 1.600 mm |
| 50 mm (2") | 2.700 mm | 2.000 mm |
| 60 mm (2-3/8") | 3.200 mm | 2.500 mm |

**Faustregel:** Maximale freie Wellenlänge ≤ 40 × Wellendurchmesser.
Bei Überschreitung → P-Bracket oder Zwischenlager einbauen.

### 2.6 Wellenoberfläche und Finish

Die Wellenoberfläche im Bereich des Cutless-Bearings und der Dichtung
ist entscheidend für Lebensdauer und Funktion:

| Bereich | Erforderliche Rauheit (Ra) | Finish | Prüfmethode |
|---------|:---:|---------|-----------|
| Dichtungsbereich (PSS) | ≤ 0,4 µm | Poliert, spiegelnd | Rauheitsmessung / visuell |
| Dichtungsbereich (Stopfbuchse) | ≤ 0,8 µm | Fein geschliffen | Visuell, Fingernagel-Test |
| Cutless-Bearing-Bereich | ≤ 1,6 µm | Geschliffen | Visuell |
| Kupplungsbereich | ≤ 3,2 µm | Gedreht, fein | Visuell |
| Freier Schaft | ≤ 6,3 µm | Gedreht | — |

**Rillen und Scoring:** Jede Umfangsrille > 0,1 mm Tiefe im Dichtungs-
bereich bedeutet Leckage bei Stopfbuchsen und verkürzter Lebensdauer
bei PSS-Systemen. Axiale Kratzer sind weniger kritisch, aber > 0,3 mm
ebenfalls problematisch.

**Wellen-Repair-Hülse (Shaft Sleeve):** Bei verschlissener Welle im
Dichtungsbereich kann eine Edelstahl-Hülse aufgezogen werden
(Presspassung + Kleber). Kosten: 200–600 EUR vs. neue Welle 800–3.000 EUR.

---
---

## 3. Stevenrohr — Aufbau und Lagerung

### 3.1 Funktion und Konstruktion

Das Stevenrohr (Stern Tube) durchdringt den Rumpf und führt die
Propellerwelle aus dem Schiffsinneren ins Wasser. Es ist eine der
kritischsten Rumpfdurchführungen und muss folgende Anforderungen
erfüllen:

- **Wasserdichtheit**: In Verbindung mit der Wellendichtung
- **Wellenführung**: Aufnahme des Cutless-Bearings
- **Strukturelle Integrität**: Kräfte aus Propellerschub und Wellenlast
  in den Rumpf einleiten
- **Korrosionsbeständigkeit**: Dauerkontakt mit Seewasser

### 3.2 Stevenrohr-Materialien

| Material | Einsatz | Vorteile | Nachteile | Lebensdauer |
|----------|---------|----------|-----------|:---:|
| GFK (laminiert) | Produktionsboote GFK | Einfach, günstig, kein galvanisches Potential | Nicht nachträglich änderbar | 25–40 Jahre |
| Bronze (CDA C95500/C95800) | Alle Boots-typen | Hervorragende Seewasser-Beständigkeit, bewährt | Galvanisches Potential zu Stahl | 40–60+ Jahre |
| Edelstahl 316L | Stahlboote | Kompatibel mit Stahlrumpf | Spaltkorrosion möglich | 30–50 Jahre |
| Gusseisen | Ältere Stahlboote | Günstig, leicht einzuschweißen | Korrodiert | 15–25 Jahre |
| Aluminium-Bronze | Aluminium-Boote | Galvanisch kompatibel | Selten, teuer | 40+ Jahre |

### 3.3 Stevenrohr bei GFK-Booten

Bei GFK-Booten wird das Stevenrohr typischerweise in den Rumpf
einlaminiert:

**Konstruktionsvarianten:**

1. **GFK-Rohr einlaminiert**: Das Stevenrohr selbst ist ein GFK-Rohr,
   das mit dem Rumpf-Laminat verbunden wird. Cutless-Bearing wird
   eingepresst. Häufigste Variante bei Produktionsbooten.

2. **Bronze-Rohr einlaminiert**: Bronze-Stevenrohr wird mit GFK in den
   Rumpf eingebettet. Bessere Wärmeableitung, längere Lebensdauer
   des Cutless-Bearings. Standard bei Semi-Custom und Custom.

3. **Zweiteiliges System**: Inneres Rohr (Aufnahme Dichtung) und
   äußeres Rohr (Aufnahme Cutless-Bearing) mit Flansch verschraubt.
   Erleichtert Wartung.

**Einbauwinkel:**
Der Stevenrohr-Winkel muss exakt dem Wellenwinkel entsprechen. Typische
Wellenwinkelvarianten:

| Bootstyp | Wellenwinkel zur Horizontalen |
|----------|:---:|
| Motorboot Verdränger | 5–8° |
| Motorboot Gleiter | 8–15° |
| Segelboot | 8–14° |
| Motoryacht | 6–10° |
| Trawler | 5–7° |

### 3.4 Stevenrohr bei Stahlbooten

Bei Stahlbooten wird das Stevenrohr eingeschweißt. Besondere
Herausforderungen:

- **Galvanische Trennung**: Bronze-Stevenrohr in Stahlrumpf → galvanische
  Korrosion. Lösung: Isolierbuchse oder Edelstahl-Stevenrohr.
- **Schweißnaht-Qualität**: Stevenrohr-Schweißnaht muss wasserdicht und
  rissfrei sein. Prüfung mit Farbeindringverfahren empfohlen.
- **Opferanoden**: Mindestens eine Zinkanode am Stevenrohr-Austritt.

### 3.5 Stevenrohr bei Aluminiumbooten

Aluminium erfordert besondere Sorgfalt bei der Materialwahl:

- **NIE Bronze direkt an Aluminium** → katastrophale galvanische Korrosion.
- Empfohlene Materialien: Aluminium-Bronze (kompatibel) oder GFK-Hülse
  als Isolierung.
- Isolierung mit Tef-Gel oder gleichwertigem Isoliermittel obligatorisch.
- Spaltmaße großzügiger als bei GFK/Stahl wegen höherer Wärmeausdehnung.

### 3.6 Stevenrohr-Inspektion und Zustandsbewertung

**Prüfpunkte bei Trockendock (alle 2–3 Jahre):**

1. **Äußere Inspektion:**
   - Stevenrohr-Austritt: Risse, Spaltbildung zum Rumpf?
   - Bei GFK: Osmose-Blasen im Laminat um das Stevenrohr?
   - Bei Bronze: Grünspan, De-Zinkung (rosa Verfärbung)?
   - Bewuchs am Stevenrohr-Austritt entfernen, Antifouling erneuern.

2. **Innere Inspektion:**
   - Stopfbuchsen-/Dichtungsbereich: Korrosion am Stevenrohr-Ende?
   - GFK-Laminat-Verbindung: Risse, Ablösung?
   - Bronze-Rohre: Wandstärke prüfen (Ultraschall alle 10 Jahre
     bei Booten > 20 Jahre).
   - Wasseraustritt zwischen Stevenrohr und Rumpf? → Laminat-Schaden!

3. **Cutless-Bearing-Sitz:**
   - Bearing sitzt fest im Rohr? Wackelt → Rohr aufgeweitet.
   - Bei Bronze-Rohren: Set-Schraube (Madenschraube) vorhanden und fest?
   - Bei GFK-Rohren: Bearing mit Epoxy fixiert? Gelöst?

**Häufigste Stevenrohr-Probleme nach Bootsalter:**

| Bootsalter | Häufigstes Problem | Typische Kosten |
|:---:|--------|:---:|
| 0–10 Jahre | Cutless-Bearing-Verschleiß | 280–800 EUR |
| 10–20 Jahre | Bearing-Sitz aufgeweitet | 500–1.500 EUR |
| 20–30 Jahre | GFK-Laminat gerissen / Bronze korrodiert | 1.000–5.000 EUR |
| 30+ Jahre | Stevenrohr-Austausch nötig | 3.000–10.000 EUR |

### 3.7 Stevenrohr-Reparatur und Austausch

**GFK-Stevenrohr reparieren:**
1. Risse im Laminat: Mit Epoxy-Harz und Glasfasermatte verstärken.
   Bereich 200 mm beidseits des Risses anschleifen, 3–5 Lagen Matte.
2. Aufgeweiteter Bearing-Sitz: Bearing mit Epoxy-Vergussmasse
   (z.B. Belzona 1111) fixieren.
3. Stevenrohr gelöst vom Rumpf: Komplett neu einlaminieren
   (professionelle Arbeit, 1.500–4.000 EUR).

**Bronze-Stevenrohr ersetzen:**
1. Altes Rohr herausschneiden (bei GFK: Laminat aufschneiden).
2. Neues Rohr passgenau anfertigen lassen.
3. Einlaminieren (GFK) oder Einschweißen (Stahl).
4. Kosten: 2.000–8.000 EUR je nach Bootstyp und Zugänglichkeit.

**Wann muss das Stevenrohr ausgetauscht werden?**
- Wandstärke < 60 % des Originals (Ultraschall-Messung).
- Risse durchgehend (Wassereinbruch zwischen Rohr und Rumpf).
- Bearing-Sitz so stark aufgeweitet, dass kein Bearing mehr hält.
- Korrosion hat das Material strukturell geschwächt.

### 3.8 Schmierungsarten des Stevenrohrs

| System | Medium | Vorteile | Nachteile | Einsatz |
|--------|--------|----------|-----------|---------|
| Wassergeschmiert | Seewasser | Umweltfreundlich, einfach, kühlt Lager | Korrosionsrisiko, Ablagerungen | Standard Sportboote |
| Fettgeschmiert | Marine-Fett | Korrosionsschutz, längere Lager-Lebensdauer | Umweltbelastung, regelmäßig nachfetten | Ältere Boote, Berufsschifffahrt |
| Ölgeschmiert | Marine-Öl | Beste Schmierung, Kühlung | Komplex, Leckagerisiko, Umwelt | Superyachten, Berufsschifffahrt |

**Wassergeschmiertes System (Standard):**
- Seewasser tritt am Heck durch den Spalt zwischen Welle und
  Cutless-Bearing ein.
- Wasser schmiert und kühlt das Gummilager.
- Wasser fließt nach innen zur Wellendichtung.
- Dichtung verhindert Eintritt ins Boot.

**Fettgeschmiertes System:**
- Fettpresse (Stauffer-Büchse) am Stevenrohr-Innenende.
- Regelmäßig Fett nachpressen (alle 50–100 Betriebsstunden).
- Äußere Dichtlippe verhindert Wasseraustritt des Fetts.
- Innere Dichtlippe / Stopfbuchse dichtet nach innen ab.

---
---

## 4. Cutless-Bearing / Wellenlager

### 4.1 Funktion und Aufbau

Das Cutless-Bearing (auch Cutlass-Bearing, Wellenlager, Gummilager)
ist ein wassergeschmiertes Gleitlager, das die Propellerwelle im
Stevenrohr führt. Es besteht aus:

- **Außenhülse**: Bronze, GFK, oder Kunststoff (Nylon/Phenolharz)
- **Innenlager**: Nitril-Gummi (NBR) mit Längsrillen für Wasserfluss
- **Wasserrillen**: 4–8 Längsrillen ermöglichen Wasserdurchfluss zur
  Schmierung und Kühlung. Rillentiefe: typisch 3–5 mm.

Der Name "Cutless" stammt vom Originalhersteller Johnson Duramax —
"cut-less" weil das Gummilager die Welle weniger verschleißt als
alte Metall-auf-Metall-Lager.

### 4.2 Hersteller und Typen

| Hersteller | Modell | Außenhülse | Innenmaterial | Besonderheit |
|-----------|--------|-----------|--------------|-------------|
| Johnson Duramax | 100 (Standard) | Bronze | Nitril-Gummi | Industriestandard, bewährt |
| Johnson Duramax | 200 (Heavy Duty) | Bronze | Nitril-Gummi | Dickeres Gummi, robuster |
| Johnson Duramax | 400 (Naval) | Bronze | Nitril-Gummi | Mil-Spec, höchste Qualität |
| Morse | Standard | Bronze | Nitril-Gummi | Alternative zu Duramax |
| Morse | Non-Metallic | GFK/Nylon | Nitril-Gummi | Für Aluminiumboote |
| ThorDon | SXL | Polymer | UHMWPE/Polymer | Kein Gummi, sehr langlebig |
| ThorDon | Compac | Polymer | UHMWPE/Polymer | Für große Wellen |
| Vesconite | Hilube | — | Polymer (Vesconite) | Selbstschmierend, trockenlauftauglich |
| Duramax Marine | Super Shaft Bearing | Bronze/Nylon | Nitril-Gummi | Breite Verfügbarkeit |

### 4.3 Dimensionierung

Die Cutless-Bearing-Größe wird durch den Wellendurchmesser bestimmt:

| Wellendurchmesser | Bearing-ID | Bearing-OD (Bronze) | Bearing-Länge | Typische Teilenummer |
|:---:|:---:|:---:|:---:|:---:|
| 3/4" (19 mm) | 3/4" | 1-1/8" | 3" | 100-075-112 |
| 7/8" (22 mm) | 7/8" | 1-3/8" | 3-1/2" | 100-087-138 |
| 1" (25 mm) | 1" | 1-1/2" | 4" | 100-100-150 |
| 1-1/8" (29 mm) | 1-1/8" | 1-5/8" | 4-1/2" | 100-112-163 |
| 1-1/4" (32 mm) | 1-1/4" | 1-3/4" | 5" | 100-125-175 |
| 1-3/8" (35 mm) | 1-3/8" | 2" | 5-1/2" | 100-138-200 |
| 1-1/2" (38 mm) | 1-1/2" | 2-1/8" | 6" | 100-150-213 |
| 1-3/4" (44 mm) | 1-3/4" | 2-3/8" | 7" | 100-175-238 |
| 2" (50 mm) | 2" | 2-3/4" | 8" | 100-200-275 |

### 4.4 Verschleißprüfung

**Methode 1: Spiel-Messung (Standard)**
1. Boot an Land / im Wasser (Motor aus).
2. Propellerwelle am Propellerende nach oben/unten bewegen (Hebel).
3. Spiel mit Fühlerlehre oder Messuhr am Stevenrohr-Austritt messen.

| Wellendurchmesser | Max. Verschleißspiel | Austausch empfohlen |
|:---:|:---:|:---:|
| 3/4" (19 mm) | 0,3 mm | > 0,5 mm |
| 1" (25 mm) | 0,4 mm | > 0,6 mm |
| 1-1/4" (32 mm) | 0,4 mm | > 0,7 mm |
| 1-1/2" (38 mm) | 0,5 mm | > 0,8 mm |
| 2" (50 mm) | 0,5 mm | > 1,0 mm |

**Methode 2: Vibrationsanalyse**
- Beschleunigungsaufnehmer am P-Bracket oder Stevenrohr.
- Lagerfrequenz berechnen: f = (n/60) × (D_i/D_o) × Z
  (n=Drehzahl, D=Durchmesser, Z=Rillenanzahl).
- Erhöhte Amplitude bei Lagerfrequenz → Verschleiß.

**Methode 3: Visuelle Inspektion (Boot an Land)**
- Cutless-Bearing von achtern mit Taschenlampe inspizieren.
- Gummirillen < 1 mm Resttiefe → Austausch.
- Gummi ablösend / ausgerissen → sofortiger Austausch.
- Ungleichmäßiger Verschleiß → Wellenausrichtung prüfen.

### 4.5 Austausch des Cutless-Bearings

**Werkzeuge:**
- Bearing-Puller (Spezialwerkzeug) oder lange Gewindestange mit
  Druckplatte und Mutter.
- Bearing-Press-Tool oder hydraulische Presse.
- Kältespray / Trockeneis (Bearing kühlen → schrumpft).
- Hitze (Stevenrohr erwärmen → dehnt sich).
- Marine-Dichtmasse (Loctite 640 oder äquivalent).

**Schritte (wassergeschmiert, Bronze-Bearing in GFK-Stevenrohr):**
1. Propeller abziehen (Propellermutter lösen, Propellerabzieher).
2. Welle nach innen herausziehen oder nach achtern herausdrücken.
3. Altes Bearing mit Puller herausziehen oder -pressen.
4. Stevenrohr-Innenfläche reinigen, auf Riefen prüfen.
5. Neues Bearing mit Kältespray abkühlen.
6. Stevenrohr mit Heißluftfön anwärmen (GFK: max. 80 °C!).
7. Neues Bearing mit Dichtmasse einpressen. Achten auf korrekte
   Ausrichtung der Wasserrillen (eine Rille nach oben).
8. Aushärten lassen (24 h).
9. Welle einführen, Propeller montieren.
10. Laufprobe: sanftes Drehen von Hand, darf nicht klemmen.

**Kosten Cutless-Bearing-Austausch:**

| Bootsklasse | Material | Arbeit | Gesamt |
|------------|:---:|:---:|:---:|
| Segelboot 10 m / 1" Welle | 80–150 EUR | 200–400 EUR | 280–550 EUR |
| Motorboot 12 m / 1-1/4" Welle | 100–200 EUR | 300–600 EUR | 400–800 EUR |
| Motoryacht 15 m / 1-1/2" Welle | 150–300 EUR | 500–1.000 EUR | 650–1.300 EUR |
| Motoryacht 20 m / 2" Welle | 250–500 EUR | 800–1.500 EUR | 1.050–2.000 EUR |

### 4.6 Lebensdauer-Faktoren

| Faktor | Einfluss auf Lebensdauer | Empfehlung |
|--------|:---:|-----------|
| Motorausrichtung | +++ | Jährlich prüfen, ≤ 0,05 mm |
| Propeller-Balance | ++ | Nach jeder Reparatur auswuchten |
| Sediment/Sand im Wasser | +++ | Seewasserfilter, Revierabhängig |
| Betriebsstunden/Jahr | ++ | 200–400 h/Jahr = 8–12 Jahre Bearing-Leben |
| Trockenfall (ohne Wasser) | +++ | NIE Motor starten ohne Wasser am Cutless |
| Wellenoberfläche | ++ | Ra ≤ 1,6 µm im Lagerbereich |
| Korrektes Spiel (Einbau) | ++ | Bearing muss satt im Rohr sitzen |

### 4.7 Alternative Lagermaterialien: ThorDon und Vesconite

Neben dem klassischen Gummi-Cutless-Bearing gibt es moderne
Polymer-Alternativen, die in bestimmten Einsatzszenarien Vorteile
bieten:

**ThorDon SXL / Compac:**
- Material: UHMWPE-basierter Verbundwerkstoff.
- Kein Gummi → keine Gummi-Alterung, kein Quellen, kein Auflösen.
- Selbstschmierend (Polymer gibt Schmierstoffe ab).
- Besonders gut bei Sand/Sediment-Revieren (Polymer ist härter).
- Lebensdauer: 10–25 Jahre (deutlich länger als Gummi).
- Preis: 2–3× teurer als Standard-Cutless (250–500 EUR).
- Nachteil: Höhere Anforderung an Wellenoberfläche (Ra ≤ 0,8 µm).

**Vesconite Hilube:**
- Selbstschmierender Polymer.
- Trockenlauftauglich (kurzzeitig) — ideal für Trockenfaller.
- Extrem verschleißfest.
- Preis: Ähnlich ThorDon.
- Nachteil: Weniger verbreitet, weniger Erfahrungswerte.

**Empfehlung AYDI:**
- **Standard-Reviere (Ostsee, Mittelmeer, Atlantik):** Johnson
  Duramax 100 — bewährt, günstig, überall verfügbar.
- **Sand-Reviere (Nordsee, Karibik-Atolle, Flussmündungen):**
  ThorDon SXL — längere Lebensdauer bei abrasiven Bedingungen.
- **Trockenfaller / Tidenhäfen:** Vesconite — toleriert kurzzeitigen
  Trockenlauf ohne Schaden.
- **Langfahrt:** Johnson Duramax 100 + Ersatz-Bearing an Bord —
  weltweit am einfachsten beschaffbar.

### 4.8 Cutless-Bearing-Geräusche und Diagnose

Ein verschlissenes Cutless-Bearing meldet sich oft akustisch:

| Geräusch | Zustand | Maßnahme |
|----------|---------|----------|
| Sanftes Summen | Normal (Welle dreht im Lager) | Keine |
| Rhythmisches Klopfen (1×/Umdrehung) | Welle schlägt im Lager | Spiel messen, Bearing prüfen |
| Unregelmäßiges Klopfen | Gummi ablösend, Stücke im Lager | Bearing sofort tauschen |
| Quietschen bei Anlauf | Trockenes Bearing (Boot aus Wasser?) | Wasser bereitstellen |
| Konstantes Kratzen | Fremdkörper (Sand, Muschel) | Motor aus, inspizieren |
| Dumpfes Brummen bei bestimmter Drehzahl | Resonanz Welle/Bearing | Drehzahl variieren, prüfen |

---
---

## 5. Wellendichtung — Stopfbuchse (Packing Gland)

### 5.1 Funktionsprinzip

Die traditionelle Stopfbuchse (Packing Gland, Stuffing Box) ist
das älteste und einfachste System zur Wellenabdichtung. Das Prinzip
ist seit Hunderten von Jahren unverändert:

- Ein Hohlraum (Stopfbuchsen-Gehäuse) umgibt die rotierende Welle.
- Weiche, flexible Dichtungsringe (Packung/Packing) werden in den
  Hohlraum gepresst.
- Eine Druckscheibe (Follower/Gland) wird mit Muttern angezogen und
  presst die Packung gegen die Welle.
- Die Packung bildet eine flexible Dichtung um die rotierende Welle.
- Eine kontrollierte Leckage (Tropfrate) ist gewünscht und notwendig.

### 5.2 Aufbau und Komponenten

```
              ┌─────────────────────┐
 Rumpf ───────┤  Stevenrohr         │
              │                     │
  Welle ══════╪══════════════════╪══════ → zum Propeller
              │  ┌──────────┐   │
              │  │ Packung  │   │  ← Dichtungsringe (3–5 Stück)
              │  │ Packung  │   │
              │  │ Packung  │   │
              │  └──────────┘   │
              │  Druckscheibe ──┤  ← Follower/Gland
              │  Muttern ───────┤  ← 2 Schrauben/Muttern
              └─────────────────┘
                     │
              Leckwasser-Auffang
              (in die Bilge)
```

### 5.3 Packungsmaterialien

| Material | Zusammensetzung | Temperaturbereich | Einsatz | Preis |
|----------|---------------|:---:|---------|:---:|
| PTFE/Graphit | PTFE-imprägnierte Graphitfasern | -60 bis +260 °C | Standard modern | Mittel |
| PTFE/Aramid | Kevlar-Fasern, PTFE-beschichtet | -60 bis +230 °C | Leistung, wenig Reibung | Hoch |
| Flachs/Talg | Natürliche Flachsfasern, talgimprägniert | 0 bis +80 °C | Traditionell, günstig | Gering |
| GFO (Gore) | Expanded PTFE mit Graphit | -200 bis +280 °C | Premium, langlebig | Sehr hoch |
| Graphit rein | Flexible Graphitfasern | -200 bis +500 °C | Hochtemperatur | Hoch |
| Baumwolle/Wachs | Gewachste Baumwollschnur | 0 bis +80 °C | Veraltet, Notfall | Minimal |

**Empfehlung für Yachtbereich:** PTFE/Graphit-Packung als bester
Kompromiss aus Lebensdauer, Reibung und Preis. Niemals verschiedene
Packungsmaterialien mischen!

### 5.4 Packungsdimensionierung

| Wellendurchmesser | Packungsquerschnitt | Anzahl Ringe | Gesamttiefe |
|:---:|:---:|:---:|:---:|
| 3/4" (19 mm) | 5/16" (8 mm) | 3 | 24 mm |
| 1" (25 mm) | 3/8" (10 mm) | 3–4 | 30–40 mm |
| 1-1/4" (32 mm) | 3/8" (10 mm) | 4 | 40 mm |
| 1-1/2" (38 mm) | 1/2" (13 mm) | 4 | 52 mm |
| 2" (50 mm) | 5/8" (16 mm) | 4–5 | 64–80 mm |

**Packungsringe schneiden:**
1. Packungsschnur um die Welle wickeln (nicht um einen Dorn!).
2. Im 45°-Winkel schneiden (Schrägschnitt → bessere Abdichtung).
3. Ringe versetzt einlegen (Schnittstellen um 90° versetzt).
4. Jeden Ring einzeln eindrücken, nicht alle gleichzeitig.

### 5.5 Tropfrate — Die kritische Einstellung

Die korrekte Tropfrate ist die wichtigste Einstellung der Stopfbuchse.
Zu wenig → Überhitzung. Zu viel → Wassereinbruch.

**Korrekte Tropfrate:**

| Zustand | Tropfrate | Bedeutung |
|---------|:---:|---------|
| Motor aus, im Wasser | 0–1 Tropfen/min | Normal, Packung darf minimal lecken |
| Motor an, Leerlauf | 2–6 Tropfen/min | Korrekt eingestellt |
| Motor an, Fahrt (Marschfahrt) | 6–12 Tropfen/min | Korrekt eingestellt |
| Motor an, Vollgas | 10–20 Tropfen/min | Akzeptabel, obere Grenze |
| Dauerhaft > 30 Tropfen/min | Zu viel | Packung nachziehen oder erneuern |
| 0 Tropfen bei Fahrt | Zu wenig! | Sofort etwas lösen! Überhitzungsgefahr |

**Kritische Warnung:** Eine Stopfbuchse, die bei laufendem Motor
nicht tropft, überhitzt und kann die Welle beschädigen (Temperatur
bis 200+ °C, Welle verfärbt sich blau, Packung verkohlt). Im schlimmsten
Fall löst sich die Packung komplett und Seewasser strömt unkontrolliert
ein.

### 5.6 Nachziehen und Wartung

**Nachziehen der Stopfbuchse:**
1. Motor starten, Vorwärtsgang einlegen.
2. Tropfrate beobachten.
3. Muttern gleichmäßig anziehen (1/6 Umdrehung, dann warten).
4. 30 Sekunden warten → neue Tropfrate beobachten.
5. Wiederholen bis 6–12 Tropfen/min erreicht.
6. NIEMALS zu fest anziehen!

**Wartungsintervalle:**

| Maßnahme | Intervall | Aufwand |
|----------|:---:|:---:|
| Tropfrate kontrollieren | Jede Fahrt | 1 Minute |
| Nachziehen (wenn nötig) | Alle 50–100 Betriebsstunden | 10 Minuten |
| Packung erneuern | Alle 1–3 Jahre / 300–800 h | 30–60 Minuten |
| Stopfbuchsen-Gehäuse prüfen | Alle 5 Jahre | 30 Minuten |
| Welle im Dichtungsbereich prüfen | Alle 5 Jahre | Im Rahmen Cutless-Wechsel |

### 5.7 Vor- und Nachteile der Stopfbuchse

| Vorteil | Nachteil |
|---------|----------|
| Einfach, robust, bewährt seit Jahrhunderten | Kontrollierte Leckage notwendig |
| Günstig (Material: 10–30 EUR) | Regelmäßige Nachstellung nötig |
| Überall reparierbar, keine Spezialteile | Wasser in der Bilge |
| Toleriert schlechte Ausrichtung besser | Wellenverschleiß durch Packungsreibung |
| Selbst zu warten, kein Fachmann nötig | Bilge-Pumpe muss funktionieren |
| Funktioniert auch bei alten, rauhen Wellen | Druck-abhängige Leckage (tiefer Rumpf = mehr) |

---
---

## 6. Wellendichtung — Lippendichtung (PSS / PYI Pacific Seals)

### 6.1 Funktionsprinzip PSS (Pacific Shaft Seal)

Die PSS-Wellendichtung (oft auch "dripless seal" oder mechanische
Gleitringdichtung genannt) ist die modernste und beliebteste Alternative
zur Stopfbuchse. Das Prinzip:

- Ein stationärer, hochglanzpolierter Graphit/Carbon-Ring wird über
  eine Rohrverbindung mit dem Stevenrohr/Rumpf verbunden (fixiert).
- Ein rotierender Edelstahl-Ring (Rotor) wird mit Edelstahl-Schlauch-
  schellen auf der Propellerwelle fixiert und dreht sich mit.
- Ein Gummi-Balg (Bellows) drückt den stationären Carbon-Ring mit
  definierter Federkraft gegen den rotierenden Edelstahl-Ring.
- Die beiden hochpolierten Flächen gleiten aufeinander und bilden
  eine praktisch wasserfreie Dichtung.
- Ein dünner Wasserfilm zwischen den Flächen sorgt für Schmierung.

### 6.2 Aufbau und Komponenten

```
     Stevenrohr ──┐
                   │     ┌─ Bellows (Gummibalg)
                   │     │   ┌─ Stationärer Ring (Carbon/Graphit)
                   │     │   │    ┌─ Rotierender Ring (Edelstahl)
  Welle ═══════════╪═════╪═══╪════╪═══════ → zum Propeller
                   │     │   │    │
                   │     │   ▼    ▼
                   │   Druckfeder  Schlauchschellen auf Welle
                   │     │
         Adapter ──┘     └─ Schlauchverbindung zum Stevenrohr
```

### 6.3 PSS-Modelle nach Wellendurchmesser

| Wellendurchmesser | PSS-Modell | Stevenrohr-ID (min.) | Preis (ca.) |
|:---:|:---:|:---:|:---:|
| 3/4" (19 mm) | PSS 3/4" | 1-3/8" (35 mm) | 280–350 EUR |
| 7/8" (22 mm) | PSS 7/8" | 1-1/2" (38 mm) | 300–370 EUR |
| 1" (25 mm) | PSS 1" | 1-5/8" (41 mm) | 320–400 EUR |
| 1-1/8" (29 mm) | PSS 1-1/8" | 1-3/4" (44 mm) | 350–430 EUR |
| 1-1/4" (32 mm) | PSS 1-1/4" | 2" (51 mm) | 380–470 EUR |
| 1-3/8" (35 mm) | PSS 1-3/8" | 2-1/8" (54 mm) | 410–500 EUR |
| 1-1/2" (38 mm) | PSS 1-1/2" | 2-1/4" (57 mm) | 450–550 EUR |
| 1-3/4" (44 mm) | PSS 1-3/4" | 2-3/4" (70 mm) | 550–700 EUR |
| 2" (50 mm) | PSS 2" | 3" (76 mm) | 650–850 EUR |
| 2-1/2" (63 mm) | PSS 2-1/2" | 3-1/2" (89 mm) | 900–1.200 EUR |

### 6.4 Installation der PSS

**Voraussetzungen:**
- Wellendurchmesser muss im Toleranzbereich liegen (+0,0 / -0,05 mm).
- Welle muss im Dichtungsbereich poliert sein (Ra ≤ 0,4 µm).
- Stevenrohr-Innendurchmesser muss für Adapter passen.
- Mindestabstand Stevenrohr-Ende bis Kupplung: Bellows-Länge + 50 mm.

**Installationsschritte:**
1. Welle reinigen und im Dichtungsbereich polieren (400er, dann 600er
   Nassschleifpapier).
2. Adapter auf Stevenrohr-Ende montieren (Verschraubung oder Epoxy).
3. Bellows über die Welle streifen.
4. Stationären Carbon-Ring auf den Adapter setzen.
5. Rotierenden Edelstahl-Ring auf die Welle setzen.
6. Rotierenden Ring mit Edelstahl-Schlauchschellen auf Welle fixieren.
   Exakte Position nach Hersteller-Anleitung (Bellows-Kompression
   6–10 mm, je nach Modell).
7. Bellows-Schlauch an Adapter anschließen.
8. Wasser-Versorgung: Seeventil oder Stevenrohr-Wasser über
   Schlauch an PSS Wasseranschluss anschließen (IMMER erforderlich!).
9. Schlauchschellen doppelt montieren (Sicherheit).
10. Testlauf: Welle von Hand drehen — muss leichtgängig sein.
11. Probelauf mit Motor: keine Leckage, kein Quietschen.

**Kritische Einstellungen:**
- Bellows-Kompression zu gering → Wasser tritt ein.
- Bellows-Kompression zu hoch → übermäßige Reibung, Überhitzung,
  vorzeitiger Verschleiß der Carbon-Fläche.
- Empfohlene Kompression: 6–10 mm (je nach Modell und Hersteller).

### 6.5 Wasserversorgung der PSS

Die PSS-Dichtung benötigt Kühlwasser! Ohne Wasserversorgung überhitzt
die Dichtung und versagt innerhalb von Minuten.

**Wasserversorgungsvarianten:**

| Variante | Quelle | Vorteil | Nachteil |
|----------|--------|---------|----------|
| Stevenrohr-Wasser | Seewasser durch Stevenrohr | Einfach, kein extra Ventil | Druck variiert, Ablagerungen |
| Eigenes Seeventil | Separates Seeventil + Schlauch | Kontrollierbarer Druck | Zusätzliche Rumpfdurchführung |
| Druckloses System | Kein aktiver Wasserzulauf | Einfach | Nur bei bestimmten PSS-Modellen |

**Warnung:** Bei trockenem Betrieb (z.B. Boot aus dem Wasser, Welle
dreht bei Transport) → PSS-Dichtflächen innerhalb von 1–2 Minuten
beschädigt! Vor dem Starten sicherstellen, dass Wasser an der
Dichtung ansteht.

### 6.6 Wartung der PSS

| Maßnahme | Intervall | Aufwand |
|----------|:---:|:---:|
| Visuell prüfen (Leckage, Bellows-Zustand) | Monatlich / jede Fahrt | 2 Minuten |
| Bellows auf Risse, Versprödung prüfen | Halbjährlich | 5 Minuten |
| Schlauchschellen nachziehen | Jährlich | 5 Minuten |
| Carbon-Ring-Verschleiß prüfen (Markierung) | Jährlich | 5 Minuten |
| Bellows austauschen | Alle 5–7 Jahre | 30–60 Minuten |
| Carbon-Ring austauschen | Alle 8–12 Jahre | 30–60 Minuten |
| Rotierenden Ring prüfen (Rillen, Scoring) | Alle 5 Jahre | 10 Minuten |
| Wasserversorgung prüfen (Durchfluss) | Halbjährlich | 5 Minuten |

### 6.7 PSS-Problemanalyse im Detail

**Problem: Carbon-Ring verschlissen**
- Erkennbar an der Verschleiß-Markierung (Linie auf dem Carbon-Ring).
  Wenn die Kante des Carbon-Rings die Markierung erreicht → Austausch.
- Typische Lebensdauer: 3.000–6.000 Betriebsstunden oder 8–12 Jahre.
- Kosten Carbon-Ring: 80–150 EUR (je nach Wellengröße).

**Problem: Rotierender Ring (Rotor) hat Rillen**
- Ursache: Sand/Sediment zwischen Carbon und Rotor.
- Ergebnis: Riefen im Edelstahl-Ring → Leckage.
- Lösung: Ring mit 600er/800er Nassschleifpapier polieren.
  Bei tiefen Rillen (> 0,1 mm): Ring ersetzen (100–200 EUR).
- Prävention: Wasserfilter vor der PSS-Wasserversorgung.

**Problem: PSS quietscht beim Anlaufen**
- Ursache: Trockenlauf — kein Wasser zwischen den Dichtflächen.
- Lösung: Vor dem Starten Seeventil öffnen, 30 Sekunden warten.
  Alternativ: Wasser mit Sprühflasche in den PSS-Bereich sprühen.
- Bei chronischem Quietschen: Bellows-Kompression prüfen
  (zu hoch → mehr Reibung).

**Problem: PSS-Schlauchverbindung undicht**
- Ursache: Schlauch vom Stevenrohr zum PSS-Adapter nicht dicht.
- Symptom: Wasser kommt nicht aus der Dichtfläche, sondern aus
  der Schlauchverbindung.
- Lösung: Schlauchschellen nachziehen oder erneuern. Schlauch
  ersetzen, wenn porös oder spröde.

### 6.8 Umrüstung Stopfbuchse → PSS: Schritt-für-Schritt

Die Umrüstung von Stopfbuchse auf PSS ist eine der beliebtesten
Modifikationen im Yachtbereich:

**Materialcheckliste:**
- PSS-Kit passend zum Wellendurchmesser.
- PSS-Adapter passend zum Stevenrohr-Innendurchmesser.
- Schlauch (Kraftstoff-/Wasserschlauch, passende Größe).
- Schlauchschellen (Edelstahl, doppelt!).
- Marine-Dichtmasse (Sealant) für Adapter.
- Nassschleifpapier (400er, 600er, 800er).
- Optional: Seeventil + Schlauch für Wasserversorgung.

**Arbeitsschritte:**
1. Boot aus dem Wasser.
2. Propeller abziehen, Welle herausziehen.
3. Alte Stopfbuchse entfernen (Schrauben lösen, Packung entfernen).
4. Stevenrohr-Innenende reinigen.
5. Welle im Dichtungsbereich polieren (400 → 600 → 800er nass).
6. PSS-Adapter auf Stevenrohr-Ende montieren.
7. Welle einsetzen.
8. PSS nach Herstelleranleitung montieren (Bellows, Ringe, Schellen).
9. Wasserversorgung anschließen.
10. Propeller montieren.
11. Einwassern, Testlauf.

**Zeitaufwand:** 3–5 Stunden (erfahrener Handwerker).
**Kosten gesamt:** 400–900 EUR (Material) + 200–500 EUR (Einbau, wenn Werft).

### 6.9 Vor- und Nachteile PSS

| Vorteil | Nachteil |
|---------|----------|
| Praktisch tropffrei (Dripless) | Teurer als Stopfbuchse (300–850 EUR) |
| Keine Bilge-Belastung | Erfordert polierte Welle |
| Minimale Wartung | Bellows-Versagen = plötzlicher Wassereinbruch |
| Geringe Reibung → weniger Wellenverschleiß | Wasserversorgung zwingend nötig |
| Keine Nachstellung nötig | Installation anspruchsvoller |
| Kein Risiko durch Überziehen (wie Stopfbuchse) | Nicht tolerant gegenüber grober Fehlausrichtung |
| Standard bei Neubauten ab 2005 | Ersatzteile: Originalhersteller empfohlen |

---
---

## 7. Wellendichtung — Tides Marine SureSeal und weitere Systeme

### 7.1 Tides Marine SureSeal

Das SureSeal-System von Tides Marine ist eine alternative mechanische
Gleitringdichtung mit einigen Konstruktionsunterschieden zum PSS:

**Besonderheiten:**
- **Doppel-Lippendichtung**: Zusätzlich zur Gleitringdichtung hat
  das SureSeal eine Sicherheits-Lippendichtung als Backup.
- **Kein Bellows**: Statt Gummibalg verwendet SureSeal einen
  Federmechanismus für den Anpressdruck.
- **Höherer Anpressdruck**: Etwas höhere Reibung, aber robuster.
- **Eingebauter Wasseranschluss**: Standardmäßig mit Waterlock.

**Modellübersicht:**

| Wellendurchmesser | Modell | Preis (ca.) |
|:---:|:---:|:---:|
| 3/4"–1" | SureSeal Small | 350–450 EUR |
| 1"–1-1/2" | SureSeal Medium | 450–600 EUR |
| 1-1/2"–2" | SureSeal Large | 600–900 EUR |
| 2"–3" | SureSeal XL | 900–1.500 EUR |

### 7.2 Volvo Penta Wellendichtung (IPS/Shaft)

Volvo Penta liefert bei Wellenantrieben eine eigene Wellendichtung:

- Doppellippendichtung mit Federdruck.
- Spezifisch für Volvo-Getriebe ausgelegt.
- Ersatzteile nur über Volvo-Vertragshändler.
- Austausch alle 5–7 Jahre empfohlen (Volvo Service Bulletin).
- Preis Original: 200–500 EUR (je nach Modell).

### 7.3 Deep Sea Seal (DSS)

- Für größere Yachten (>20 m) und Berufsschifffahrt.
- Ölgeschmierte Lippendichtung mit Überwachungssystem.
- Druckkontrolliert: automatische Nachstellung.
- Preis: 1.500–5.000 EUR (nach Wellengröße).

### 7.4 SKF / Simplex Compact Seal

- Industriestandard bei Berufsschifffahrt und Superyachten.
- Ölgeschmiert mit Druckausgleichssystem.
- Integrierte Verschleißüberwachung.
- Preis: 2.000–10.000 EUR.

### 7.5 Vergleich aller Dichtungssysteme

| Kriterium | Stopfbuchse | PSS/PYI | Tides SureSeal | Deep Sea Seal | SKF Simplex |
|-----------|:---:|:---:|:---:|:---:|:---:|
| Leckage | Kontrolliert (Tropfen) | Praktisch null | Praktisch null | Null | Null |
| Preis | 10–50 EUR | 280–850 EUR | 350–1.500 EUR | 1.500–5.000 EUR | 2.000–10.000 EUR |
| Wartungsaufwand | Hoch (regelmäßig) | Gering | Gering | Mittel | Gering–Mittel |
| Versagensart | Progressiv (mehr Tropfen) | Plötzlich (Bellows) | Progressiv (Lippenverschleiß) | Progressiv | Progressiv |
| Ausrichtungstoleranz | ±2° | ±0,5° | ±1° | ±0,5° | ±0,3° |
| Wellenoberflächenanforderung | Ra ≤ 0,8 µm | Ra ≤ 0,4 µm | Ra ≤ 0,4 µm | Ra ≤ 0,2 µm | Ra ≤ 0,2 µm |
| Reparierbarkeit | Überall | Ersatzteile nötig | Ersatzteile nötig | Spezialwerkstatt | Spezialwerkstatt |
| Bootsgröße | Alle | 6–25 m | 6–30 m | 15–60 m | 20–100 m |
| Empfehlung | Backup/Budget/Langfahrt | Standard Neubauten | Alternative zu PSS | Semi-professionell | Professionell/Superyacht |

---
---

## 8. Flexible Kupplung

### 8.1 Warum flexible Kupplungen notwendig sind

Die flexible Kupplung zwischen Getriebe und Propellerwelle erfüllt
drei kritische Funktionen:

1. **Vibrationsabsorption**: Motor-Vibrationen werden nicht direkt
   auf Welle und Propeller übertragen.
2. **Ausrichtungstoleranz**: Kompensiert kleine Fluchtungsfehler
   (angular, parallel, axial).
3. **Schockdämpfung**: Plötzliche Lastspitzen (Grundberührung,
   Leinen im Propeller) werden abgefedert und schützen das Getriebe.

### 8.2 Hersteller und Typen

| Hersteller | Modell | Typ | Drehmoment (max.) | Ausrichtungs-Toleranz | Preis |
|-----------|--------|-----|:---:|:---:|:---:|
| R&D Marine | Flexofold | Elastomer-Scheibe | 200–2.000 Nm | ±1° / 0,5 mm | 200–600 EUR |
| R&D Marine | Flexofold HD | Elastomer-Scheibe HD | 500–5.000 Nm | ±1,5° / 0,8 mm | 350–900 EUR |
| Vetus | Bullflex | Gummi-Donut | 100–3.000 Nm | ±2° / 1,0 mm | 150–500 EUR |
| Vetus | Bullflex CT | Gummi-Donut Kompakt | 100–2.000 Nm | ±1,5° / 0,8 mm | 120–400 EUR |
| PYI | PyiDrive | Elastomer | 200–4.000 Nm | ±1° / 0,5 mm | 300–800 EUR |
| Centaflex | M/H/A | Elastomer-Stern | 500–10.000 Nm | ±1° / 0,3 mm | 400–1.200 EUR |
| Aquadrive | Komplettsystem | Kupplung + CVL-Lager | 200–5.000 Nm | ±3° / 15 mm | 800–2.500 EUR |
| Centa | CF-A/CF-H | Elastomer | 200–50.000 Nm | ±1° / 0,5 mm | 300–3.000 EUR |

### 8.3 Aquadrive — Das Komplettsystem

Das Aquadrive-System ist mehr als eine flexible Kupplung — es ist ein
vollständiges Antriebssystem, das Motor und Welle mechanisch entkoppelt:

**Komponenten:**
1. **Flexible Kupplung**: Zwischen Getriebe und Zwischenwelle.
2. **CVL-Lager (Constant Velocity Joint)**: Nimmt den axialen
   Propellerschub auf und leitet ihn in den Rumpf ein — nicht
   über Motor und Motorlager.
3. **Zwischenwelle**: Kurzes Wellenstück zwischen CVL und Propellerwelle.

**Vorteile:**
- Motor ist vollständig von Propellerschub entkoppelt.
- Motorlager nehmen nur Motorgewicht auf, nicht Propellerkräfte.
- Dramatische Vibrations- und Geräuschreduktion (bis 80 %).
- Motor kann einfacher ausgerichtet werden.
- Motorlager halten wesentlich länger.

**Nachteile:**
- Hoher Preis (800–2.500 EUR).
- Mehr Komponenten = mehr potenzielle Fehlerquellen.
- Benötigt mehr Platz in der Länge.
- CVL-Lager erfordert regelmäßige Fett-Schmierung.

### 8.4 Kupplungsverschleiß erkennen

| Symptom | Mögliche Ursache | Maßnahme |
|---------|-----------------|----------|
| Vibration bei bestimmten Drehzahlen | Elastomer verschlissen / verhärtet | Kupplung prüfen, ggf. Elastomer tauschen |
| Dumpfes Klopfen beim Schalten | Spiel in der Kupplung | Kupplung prüfen |
| Gummiabrieb unter der Kupplung | Elastomer zerbröselt | Elastomer sofort tauschen |
| Risse im Elastomer | Alterung, UV, Öl | Elastomer tauschen |
| Metallisches Klappern | Elastomer vollständig verschlissen, Metall-auf-Metall | Sofort Motor aus! Kupplung tauschen |
| Ölige Ablagerungen am Elastomer | Ölkontakt → Material-Degeneration | Quelle finden, Elastomer tauschen |

### 8.5 Wartung und Lebensdauer

| Maßnahme | Intervall | Hinweis |
|----------|:---:|---------|
| Sichtprüfung Elastomer | Halbjährlich | Risse, Verhärtung, Verformung |
| Schrauben/Bolzen prüfen | Jährlich | Anzugsdrehmoment nach Hersteller |
| Elastomer tauschen | 8.000–12.000 h oder 15 Jahre | Auch bei optisch gutem Zustand |
| CVL-Lager schmieren (Aquadrive) | Alle 500 h oder jährlich | Marine-Fett nach Vorschrift |
| Kompletter Austausch | 15.000+ h oder 20+ Jahre | Bei sichtbarem Verschleiß früher |

---
---

## 9. Motorausrichtung (Engine Alignment)

### 9.1 Warum Motorausrichtung kritisch ist

Eine korrekte Motorausrichtung (Engine Alignment) ist die
wichtigste einzelne Wartungsmaßnahme für die gesamte Antriebsanlage.
Fehlausrichtung ist die häufigste Ursache für:

- Vibration (80 % aller Antriebsvibrationen)
- Vorzeitigen Cutless-Bearing-Verschleiß
- Kupplungsversagen
- Getriebeschäden (Ausgangswellenlager)
- Wellenbiegung
- Dichtungsleckage (PSS und Stopfbuchse)
- Erhöhten Kraftstoffverbrauch (5–15 % mehr)

### 9.2 Ausrichtungstoleranzen

| Typ | Parallel-Versatz (max.) | Winkelversatz (max.) | Methode |
|-----|:---:|:---:|---------|
| Starrer Flansch (alt) | 0,03 mm | 0,02 mm/100 mm | Messuhr |
| Flexible Kupplung Standard | 0,05 mm | 0,05 mm/100 mm | Messuhr/Laser |
| Aquadrive | 0,10 mm (weniger kritisch) | 1° (CVL kompensiert) | Messuhr |
| Empfehlung AYDI | ≤ 0,05 mm | ≤ 0,03 mm/100 mm | Laser bevorzugt |

### 9.3 Ausrichtungsmethoden

**Methode 1: Fühlerlehre (einfach, Budget)**

1. Motor auf Lager setzen, Getriebe an Welle kuppeln.
2. Kupplungshälften zusammenbringen, aber nicht verbinden.
3. Fühlerlehre zwischen Kupplungsflansche an 4 Positionen (12, 3, 6, 9 Uhr).
4. Spaltmaße notieren. Differenz ≤ 0,1 mm = OK für flexible Kupplung.
5. Motorlager anpassen (Höhe, Seitversatz).
6. Welle um 90° drehen, erneut messen.

**Genauigkeit:** ±0,05 mm — ausreichend für die meisten Sportboote.

**Methode 2: Messuhr / Dial Gauge (Standard, empfohlen)**

1. Messuhr-Halterung an eine Kupplungshälfte klemmen.
2. Messuhr-Taster an der anderen Kupplungshälfte ansetzen.
3. Welle langsam drehen (360°).
4. TIR (Total Indicator Reading) = Differenz Max − Min.
5. TIR parallel ≤ 0,05 mm → OK.
6. TIR angular ≤ 0,05 mm/100 mm → OK.
7. Motorlager anpassen, erneut messen.
8. Mindestens 3 Durchläufe bis stabile Werte.

**Genauigkeit:** ±0,02 mm — Standard für professionelle Installation.

**Methode 3: Laser-Ausrichtung (Präzision)**

1. Laser-Sender auf eine Kupplungshälfte montieren.
2. Empfänger auf die andere Kupplungshälfte.
3. Software berechnet Versatz und Winkel in Echtzeit.
4. Korrekturwerte werden direkt angezeigt (z.B. "Hinteres Lager
   0,3 mm höher").
5. Motorlager anpassen, sofortige Rückmeldung.

**Genauigkeit:** ±0,01 mm — Premium, für Superyachten und
Berufsschifffahrt.

**Methode 4: Schnur-Methode (Notlösung)**

1. Straffe Schnur durch Stevenrohr-Achse spannen.
2. Motor/Getriebe so ausrichten, dass die Getriebe-Ausgangswelle
   auf der Schnur liegt.

**Genauigkeit:** ±0,5 mm — nur für Notfälle oder als Vor-Ausrichtung.

### 9.4 Motorlager-Einstellung

| Motorlager-Typ | Verstellung | Einstellbereich | Werkzeug |
|----------------|-----------|:---:|---------|
| Standard-Gummilager | Vertikal (Schrauben) | ±10 mm | Gabelschlüssel |
| Adjustable Mount | Vertikal + Lateral | ±15 mm / ±5 mm | Gabelschlüssel |
| Flexible Mount (z.B. Vetus) | Vertikal (Gewindestange) | ±20 mm | Gabelschlüssel |

**Prozedur:**
1. Alle 4 Motorlager-Kontermuttern lösen.
2. Vordere Lager zuerst einstellen (Höhe).
3. Hintere Lager anpassen (Höhe und Seite).
4. Messuhr-Werte prüfen.
5. Kontermuttern anziehen.
6. Erneut messen (Anziehen verändert oft die Ausrichtung!).
7. Mindestens 3–5 Iterationen.

### 9.5 Wann muss neu ausgerichtet werden?

| Anlass | Warum |
|--------|-------|
| Motorlager-Tausch | Neue Lager = neue Höhe |
| Cutless-Bearing-Tausch | Neue Lagerposition |
| Nach Grundberührung | Welle oder Stevenrohr können verzogen sein |
| Motorlager eingesunken | Gummi altert → Motor sinkt → Versatz |
| Neue Kupplung | Andere Flanschlage möglich |
| Jährliche Kontrolle | Empfohlen bei Saisonstart |
| Vibration aufgetreten | Erste Diagnose: Ausrichtung prüfen |
| Nach Slipwagen-Kiel (auf Böcken) | Rumpfverformung durch Böcke möglich |

### 9.6 Häufige Fehler bei der Ausrichtung

| Fehler | Konsequenz | Vermeidung |
|--------|-----------|-----------|
| Nur Fühlerlehre bei professioneller Installation | Genauigkeit unzureichend | Messuhr oder Laser verwenden |
| Kontermuttern nicht nachgeprüft | Anziehen verändert Ausrichtung | Nach jedem Anziehen erneut messen |
| Nur eine Messung (nicht 360° gedreht) | Fehler bei einzelner Position unsichtbar | Immer 360° Messung, 4 Positionen |
| Boot im Kran statt im Wasser ausgerichtet | Rumpfverformung im Wasser anders | Im Wasser nachjustieren (ideal) |
| Motor warm gemessen, kalt betrieben | Thermische Ausdehnung verändert Lage | Motor warm laufen lassen, dann messen |
| Flexible Kupplung als "Ausrichtungs-Korrektur" betrachtet | Kupplung verschleißt schneller | Kupplung kompensiert nur Restfehler |
| Alte Motorlager nicht ersetzt | Gummi gibt nach, Ausrichtung driftet | Lager bei Auffälligkeit ersetzen |

### 9.7 Motorlager-Lebensdauer und Verschleiß

Motorlager bestehen aus einem Gummi-Metall-Verbund, der den Motor
von der Bootsstruktur entkoppelt (Vibrationsdämpfung). Das Gummi
altert jedoch:

**Verschleißmechanismen:**
- **Einsinkung**: Gummi wird unter Last komprimiert → Motor sinkt
  um 0,2–0,5 mm/Jahr. Nach 10–15 Jahren: 2–5 mm Versatz.
- **Verhärtung**: Ölkontakt (Bilge-Öl, Dieselleckagen) macht den
  Gummi hart → Vibrationsdämpfung sinkt.
- **Auflösung**: Diesel auf Gummi → Gummi quillt und löst sich.
- **UV/Ozon**: Bei offenem Maschinenraum → Rissbildung.

**Prüfung der Motorlager:**
1. Motor abstellen, auskühlen lassen.
2. Brechstange unter den Motor → anheben. Bewegt sich der Motor
   merklich (> 3 mm) → Lager zu weich.
3. Gummi visuell prüfen: Risse, Aufquellen, Ölkontakt.
4. Höhe aller 4 Lager vergleichen: Differenz > 2 mm → ungleichmäßig
   eingesunken.

**Kosten Motorlager-Satz (4 Stück):**

| Motorklasse | Lager-Satz | Einbau | Ausrichtung | Gesamt |
|------------|:---:|:---:|:---:|:---:|
| 10–30 PS | 100–200 EUR | 100–200 EUR | 200–400 EUR | 400–800 EUR |
| 30–75 PS | 200–400 EUR | 200–400 EUR | 200–400 EUR | 600–1.200 EUR |
| 75–150 PS | 300–600 EUR | 300–600 EUR | 300–600 EUR | 900–1.800 EUR |
| 150–300 PS | 500–1.000 EUR | 500–800 EUR | 400–800 EUR | 1.400–2.600 EUR |

### 9.8 Kosten Motorausrichtung

| Methode | Selbst | Werft | Spezialist |
|---------|:---:|:---:|:---:|
| Fühlerlehre | 0 EUR | 100–200 EUR | — |
| Messuhr | 50 EUR (Werkzeug) | 200–400 EUR | 300–600 EUR |
| Laser | — | 400–800 EUR | 500–1.000 EUR |

### 9.9 Ausrichtungsprotokolle und Dokumentation

Jede Ausrichtung sollte dokumentiert werden:

**Protokoll-Vorlage:**
- Datum, Bootsname, Motor, Getriebe, Welle.
- Methode (Fühlerlehre/Messuhr/Laser).
- Messwerte: TIR parallel, TIR angular, 4 Positionen (12/3/6/9 Uhr).
- Motorlager-Stellung (Höhe jedes Lagers).
- Ergebnis: innerhalb/außerhalb Toleranz.
- Maßnahmen: Lager angepasst, Lager getauscht, etc.
- Nächster Prüftermin.

**Warum dokumentieren?**
- Trend erkennen: Wenn die Ausrichtung jedes Jahr in dieselbe
  Richtung driftet → Motorlager einsinkend.
- Referenz für Werkstatt: Bei Werftarbeiten können die letzten
  Messwerte als Referenz dienen.
- Beweis bei Streitfall: Wenn ein Motorschaden auf Fehlausrichtung
  zurückgeführt wird, dient das Protokoll als Nachweis.

---
---

## 10. Wellenbremse (Shaft Brake)

### 10.1 Funktion und Einsatzzweck

Eine Wellenbremse verhindert, dass sich die Propellerwelle und damit der
Propeller bei abgeschaltetem Motor drehen. Dies ist relevant bei:

- **Segelbooten**: Unter Segel dreht der freilaufende Propeller und
  erzeugt Widerstand (0,5–1,5 Knoten Geschwindigkeitsverlust).
  Außerdem Verschleiß an Getriebe und Dichtung.
- **Motorbooten mit Segeln**: Gleiche Problematik.
- **Langsamfahrt unter Motor**: Bei einigen Getrieben (ohne Freilauf)
  kann der Propeller im Rückwärtsgang freilaufen.

### 10.2 Typen von Wellenbremsen

| Typ | Hersteller | Prinzip | Preis | Einsatz |
|-----|-----------|---------|:---:|---------|
| Scheibenbremse | Volvo Penta | Scheibe auf Welle, Bremssattel | 300–800 EUR | Volvo-Installationen |
| Scheibenbremse | Beta Marine | Scheibe auf Welle, Bremssattel | 250–600 EUR | Beta-Installationen |
| Bandbremse | Brunton's | Band um Welle | 200–400 EUR | Universell |
| Freilauf-Getriebe | Hurth / ZF | Einweg-Kupplung im Getriebe | Im Getriebe inkl. | Standard ZF/Hurth |
| Feder-Propeller | Flex-O-Fold, Gori | Propellerblätter klappen zusammen | 1.500–4.000 EUR | Segelyachten |

### 10.3 Installation und Wartung

**Scheibenbremse (typisch):**
1. Bremsscheibe auf Propellerwelle montieren (Passfeder + Schraube).
2. Bremssattel an Rumpf/Motorträger verschrauben.
3. Bowdenzug zum Cockpit verlegen.
4. Einstellung: Scheibe darf bei gelöster Bremse nicht schleifen.
5. Wartung: Bremsbeläge alle 5–10 Jahre prüfen, Bowdenzug fetten.

**Wichtig:**
- Wellenbremse IMMER lösen bevor Motor gestartet wird!
- Bremsscheibe muss absolut plan laufen (Schlag < 0,1 mm).
- Kein Öl oder Fett auf die Bremsflächen.

### 10.4 Widerstandsersparnis durch Wellenbremse oder Faltpropeller

Die Widerstandsersparnis unter Segel ist erheblich und direkt in
Geschwindigkeit umsetzbar:

| Lösung | Widerstand (relativ) | Geschwindigkeitsgewinn | Kosten |
|--------|:---:|:---:|:---:|
| Festpropeller, Welle frei drehend | 100 % (Referenz) | — | — |
| Festpropeller + Wellenbremse | 60–70 % | 0,3–0,8 kn | 200–800 EUR |
| Faltpropeller (2-Blatt) | 15–25 % | 0,8–1,5 kn | 1.500–3.000 EUR |
| Faltpropeller (3-Blatt) | 20–30 % | 0,7–1,3 kn | 2.000–4.000 EUR |
| Segelpropeller (Autoprop) | 25–35 % | 0,5–1,0 kn | 2.500–5.000 EUR |
| Festpropeller in Rückwärtsstellung | 70–80 % | 0,2–0,5 kn | 0 EUR |

**Faustregel:** Bei einem typischen 12-m-Segelboot mit 40 PS Motor
und Festpropeller kostet der freilaufende Propeller ca. 0,5–1,0 Knoten
Geschwindigkeit unter Segel. Über eine 200-sm-Etappe sind das
3–7 Stunden Zeitdifferenz.

### 10.5 Fehlerbild Wellenbremse

| Problem | Symptom | Ursache | Maßnahme |
|---------|---------|---------|----------|
| Bremse löst nicht | Motor blockiert beim Starten | Bowdenzug verrostet/gebrochen | Bowdenzug ersetzen, Mechanik gangbar machen |
| Bremse schleift | Quietschen, Wärmeentwicklung, Leistungsverlust | Beläge nicht korrekt eingestellt | Nachstellen, Scheibe auf Schlag prüfen |
| Bremse hält nicht | Welle dreht trotz Bremse | Beläge verschlissen | Beläge erneuern |
| Bremsscheibe lose | Klappern, Vibration | Befestigung gelöst | Schraube/Passfeder prüfen, nachziehen |

---
---

## 11. Drucklager (Thrust Bearing)

### 11.1 Funktion

Das Drucklager nimmt den axialen Propellerschub auf und leitet ihn
in die Bootsstruktur ein. Bei den meisten Sportbooten ist das
Drucklager im Getriebe integriert. Nur bei größeren Booten oder
speziellen Installationen (z.B. Aquadrive) gibt es separate
Drucklager.

### 11.2 Propellerschub-Berechnung

**Schub (vereinfacht):**
```
T = P × η / (v × 1.000)
```

Dabei:
- T = Schub in kN
- P = Motorleistung in kW
- η = Propeller-Wirkungsgrad (0,4–0,6 typisch)
- v = Geschwindigkeit in m/s

**Beispiel:**
- Motor: 40 kW, Geschwindigkeit: 7 kn (3,6 m/s), η = 0,5
- T = 40 × 0,5 / (3,6 × 1.000) = 0,0056 kN = 5,6 N → zu gering?
- Korrektur: T = P × η / v = 40.000 × 0,5 / 3,6 = 5.556 N ≈ 5,6 kN
- Bei niedrigen Geschwindigkeiten (z.B. Anfahren): T kann 10–20 kN
  erreichen (Bollard Pull).

### 11.3 Drucklager im Getriebe

| Getriebe-Hersteller | Drucklager-Typ | Max. Schub | Wartung |
|---------------------|---------------|:---:|---------|
| ZF / Hurth | Axial-Kugellager | 5–50 kN (je Modell) | Getriebeöl nach Vorschrift |
| Technodrive | Axial-Kugellager | 5–30 kN | Getriebeöl nach Vorschrift |
| Velvet Drive | Druckscheibe | 5–20 kN | Getriebeöl, Druckscheibe prüfen |
| Volvo Penta (IPS) | Integriert | >50 kN | Volvo-Service |

### 11.4 Separates Drucklager (Aquadrive CVL)

Das Aquadrive CVL-Drucklager ist ein separates Lager, das den
Propellerschub direkt in den Rumpf einleitet und den Motor entlastet:

- **Schublager**: Axial-Kugellager in einem Gehäuse.
- **CVL-Gelenk**: Constant Velocity Joint für Winkelausgleich.
- **Rumpf-Verschraubung**: 4–8 Bolzen direkt in das Rumpflaminat oder
  einen verstärkten Rumpf-Bereich.

**Wartung:** Fettschmierung alle 500 h oder jährlich. Lagerprüfung
alle 5 Jahre (Spiel, Geräusche).

### 11.5 Drucklager-Versagen erkennen

Ein defektes Drucklager (im Getriebe oder separat) zeigt folgende
Symptome:

| Symptom | Diagnose | Maßnahme |
|---------|---------|----------|
| Axiales Spiel der Welle | Welle lässt sich vor/zurück bewegen (> 0,5 mm) | Drucklager prüfen/tauschen |
| Klappern beim Schalten (Vorwärts ↔ Rückwärts) | Drucklager hat Spiel | Getriebeinspektion |
| Motor "wandert" bei Schub | Propellerschub drückt Motor statt Rumpf | Drucklager-Befestigung oder CVL-Montage prüfen |
| Vibration proportional zum Schub | Drucklager-Rauheit/Korrosion | Lager austauschen |
| Erhöhte Getriebetemperatur | Innere Reibung durch defektes Lager | Getriebeöl und Lager prüfen |

**Kosten Drucklager-Austausch:**
- Im Getriebe: 500–2.000 EUR (Getriebe muss ausgebaut werden).
- Aquadrive CVL: 300–800 EUR (Lager) + 200–500 EUR (Einbau).
- Bei schwerem Getriebelager-Schaden: Getriebe-Überholung 2.000–8.000 EUR
  oder Austausch-Getriebe 3.000–12.000 EUR.

### 11.6 Propellerschub und Motorlager

Wenn kein separates Drucklager vorhanden ist (Standard), nimmt das
Getriebe den Propellerschub auf und leitet ihn über den Motor-
block und die Motorlager in den Rumpf. Die Motorlager müssen
daher nicht nur das Motorgewicht tragen, sondern auch den
Propellerschub aufnehmen:

**Propellerschub-Belastung der Motorlager:**

| Motorleistung | Typischer Schub | Motorgewicht | Schub/Gewicht-Verhältnis |
|:---:|:---:|:---:|:---:|
| 20 PS / 15 kW | 1,5–3,0 kN | 80 kg (0,8 kN) | 2:1 bis 4:1 |
| 40 PS / 30 kW | 3,0–5,0 kN | 150 kg (1,5 kN) | 2:1 bis 3:1 |
| 75 PS / 55 kW | 5,0–8,0 kN | 250 kg (2,5 kN) | 2:1 bis 3:1 |
| 150 PS / 110 kW | 8,0–15,0 kN | 450 kg (4,4 kN) | 2:1 bis 3:1 |

Der Propellerschub übersteigt das Motorgewicht also um den
Faktor 2–4! Dies erklärt, warum die Motorlager bei Standard-
Installationen so stark beansprucht werden und warum das
Aquadrive-System mit separatem Drucklager die Motorlager-
Lebensdauer deutlich verlängert.

---
---

## 12. P-Bracket / A-Bracket / Strut

### 12.1 Funktion

P-Brackets (auch Struts oder A-Brackets) sind Abstützungen, die die
Propellerwelle am Rumpf tragen, wenn die freie Wellenlänge zu groß
für ein einziges Stevenrohr-Lager ist. Sie enthalten ein zusätzliches
Cutless-Bearing.

### 12.2 Bauformen

| Bauform | Beschreibung | Einsatz |
|---------|-------------|---------|
| P-Bracket | P-förmiger Bügel, unten am Rumpf befestigt | Standard, einmotorig |
| A-Bracket | A-förmiger Bügel mit zwei Befestigungspunkten | Größere Boote, mehr Steifigkeit |
| V-Strut | V-förmige Strebe | Doppelmotorig, Arbeitsbote |
| I-Strut | Einzelne vertikale Strebe | Einfach, leicht, weniger steif |

### 12.3 Materialien

| Material | Einsatz | Vorteile | Nachteile |
|----------|---------|----------|-----------|
| Bronze (Manganbronze) | Standard | Korrosionsfest, fest, bewährt | Schwer, galvanisch aktiv |
| Edelstahl 316L | Stahlboote | Kompatibel mit Stahl | Spaltkorrosion möglich |
| Aluminium | Aluminiumboote | Leicht, kompatibel | Galvanisch kritisch |
| GFK (laminiert) | Rennboote, Leichtbau | Sehr leicht, kein galvanisches Potential | Geringere Steifigkeit |

### 12.4 P-Bracket-Dimensionierung und Auswahl

Die Auswahl des P-Brackets richtet sich nach Wellendurchmesser,
Propellerschub und Rumpfmaterial:

| Wellendurchmesser | P-Bracket Größe | Befestigungsfläche | Bolzen |
|:---:|:---:|:---:|:---:|
| 3/4"–1" (19–25 mm) | Small | 80 × 60 mm | 4 × M8 |
| 1"–1-1/4" (25–32 mm) | Medium | 100 × 80 mm | 4 × M10 |
| 1-1/4"–1-1/2" (32–38 mm) | Large | 120 × 100 mm | 6 × M10 |
| 1-1/2"–2" (38–50 mm) | XL | 150 × 120 mm | 6 × M12 |
| 2"–3" (50–75 mm) | XXL | 200 × 160 mm | 8 × M12 |

**Befestigung am Rumpf:**

Bei GFK-Booten wird der P-Bracket von außen mit dem Rumpf
verschraubt und die Befestigungsfläche mit Epoxi-Laminat
verstärkt:

1. Rumpf im Befestigungsbereich anschleifen.
2. Verstärkungsplatte (GFK oder Edelstahl) auf der Rumpfinnenseite
   positionieren (Gegenplatte/Backing Plate).
3. Bolzenlöcher bohren.
4. P-Bracket mit Marine-Sikaflex oder Butyl abdichten.
5. Bolzen durch Rumpf, Unterlegscheibe, Mutter auf Gegenplatte.
6. Alle Bolzen gleichmäßig anziehen.
7. Sealant aushärten lassen (24 h).

**Bei Stahl-/Aluminiumbooten:**
- Direkt an den Rumpf geschweißt (kein Durchbohren).
- Schweißnaht: umlaufend, geprüft (Farbeindringprüfung empfohlen).
- Bei Aluminium: Aluminium-Bracket verwenden (galvanische Trennung!).

### 12.5 P-Bracket-Risse und Ermüdung

P-Brackets sind starken Wechselbelastungen ausgesetzt (Propellerschub,
Vibration, Wellenschlag). Risse sind eine ernste Sicherheitsgefahr:

**Rissanfällige Bereiche:**
- Befestigungsfuß am Rumpf (Spannungskonzentration).
- Übergang von der Strebe zum Lagergehäuse.
- Schweißnähte bei geschweißten Brackets.

**Prüfung:**
1. Visuell alle 2 Jahre (Trockendock).
2. Farbeindringprüfung alle 5 Jahre oder bei Verdacht.
3. Ultraschall-Wanddickenmessung bei Bronze-Brackets > 15 Jahre.

**Kosten P-Bracket-Austausch:**

| Bootsklasse | Material | Arbeit (inkl. Ausrichten) | Gesamt |
|------------|:---:|:---:|:---:|
| Segelboot 10 m | 300–600 EUR | 500–1.000 EUR | 800–1.600 EUR |
| Motorboot 15 m | 500–1.200 EUR | 800–2.000 EUR | 1.300–3.200 EUR |
| Motoryacht 20 m | 1.000–3.000 EUR | 1.500–4.000 EUR | 2.500–7.000 EUR |

### 12.6 Doppelwellenanlage und P-Brackets

Bei Motorbooten mit zwei Motoren und zwei Wellen gibt es
besondere Anforderungen an die P-Brackets:

- **Symmetrie**: Beide P-Brackets müssen exakt symmetrisch zur
  Mittschiffsachse montiert sein, sonst zieht das Boot zur Seite.
- **Wellenwinkel**: Beide Wellen müssen denselben Winkel haben.
- **Abstand**: Mindestabstand der Propellerkreise: 1,5 × Propeller-
  durchmesser (sonst Interaktion/Vibration).
- **Gegenläufige Propeller**: Standardmäßig drehen die Propeller
  gegenläufig (außen nach oben) → weniger Giermoment.
- **P-Bracket-Belastung**: Bei asymmetrischem Fahren (ein Motor aus)
  erfährt der aktive P-Bracket höhere Seitenkräfte.

**Ausrichtung bei Doppelwellen:**
- Beide Motoren unabhängig ausrichten.
- Symmetrie der Wellen zueinander prüfen (String-Methode zwischen
  beiden Stevenrohren).
- Probefahrt mit nur einem Motor: Boot darf nicht mehr als 5° abweichen.

---
---

## 13. Galvanische Korrosion und Elektrolyse

### 13.1 Das Problem

Die Wellenanlage verbindet verschiedene Metalle im Seewasser —
ein klassisches Setup für galvanische Korrosion:

**Typische Metallkombination:**
- Propellerwelle: Edelstahl (Aquamet 22) → edel
- Cutless-Bearing-Hülse: Bronze → mittel
- Propeller: Bronze / Nibral → mittel
- P-Bracket: Bronze / Edelstahl → edel
- Stevenrohr: Bronze / GFK → variabel
- Rumpfbeschläge: Edelstahl → edel
- Zinkanoden: Zink → unedel (Opfer)

**Galvanische Reihe (vereinfacht, Seewasser):**

| Material | Potential (V vs. Ag/AgCl) | Tendenz |
|----------|:---:|:---:|
| Zink | −1,03 | Löst sich auf (Opfer) |
| Aluminium | −0,76 | Löst sich auf |
| Stahl / Gusseisen | −0,60 | Korrodiert |
| Bronze | −0,27 | Relativ stabil |
| Kupfer | −0,22 | Stabil |
| Edelstahl 316L (aktiv) | −0,35 | Korrodiert bei Sauerstoffmangel |
| Edelstahl 316L (passiv) | +0,05 | Edel, geschützt |
| Monel | −0,04 | Stabil |
| Titan | +0,06 | Sehr edel |

### 13.2 Zinkanoden an der Wellenanlage

| Position | Anodengröße (typisch) | Wechselintervall |
|----------|-----------------------|:---:|
| Propellerwelle (Wellenanoden) | Klapp-Anode, passend zum Wellendurchmesser | 6–12 Monate |
| P-Bracket | Bolzen-Anode M8–M12 | 6–12 Monate |
| Propeller-Nabe | PYI Propeller Nut mit Anode | 6–18 Monate |
| Ruder | Bolzen-Anode oder Platte | 6–12 Monate |

**Wellenanoden-Montage:**
1. Welle reinigen (blank Metall → elektrischer Kontakt!).
2. Klapp-Anode um die Welle legen.
3. Schrauben fest anziehen.
4. Kontakt prüfen: Widerstand Anode ↔ Welle < 1 Ω.

**Wichtig:**
- Anode muss elektrischen Kontakt zur Welle haben!
- Lackierte oder beschichtete Wellen → Lack im Kontaktbereich entfernen.
- Anoden > 50 % aufgelöst → sofort wechseln.
- KEINE Anode → Propeller oder Welle werden zum Opfer.

### 13.3 Streustrom-Korrosion (Stray Current)

Streustrom-Korrosion ist deutlich aggressiver als natürliche
galvanische Korrosion und kann einen Propeller innerhalb von Wochen
zerstören:

**Ursachen:**
- Fehlerhafte Bordverkabelung (Gleichstrom-Leck ins Wasser).
- Nachbar-Boot mit Streustrom-Problem (Landstrom-Fehler).
- Defekter Landstrom-Trenntransformator.
- Fehlende galvanische Trennung (Isolation Transformer / Galvanic
  Isolator).

**Erkennung:**
1. Referenz-Elektrode (Silber/Silberchlorid oder Zink) ins Wasser.
2. Multimeter zwischen Referenz-Elektrode und Wellenlager.
3. Spannung > 200 mV (Zink-Referenz) → Strom fließt → Korrosion.
4. Strom messen: > 50 mA → aktive Korrosion!

**Schutzmaßnahmen:**
- Galvanic Isolator (z.B. ProSafe 2, Victron) im Landstromkabel.
- Isolation Transformer für maximalen Schutz.
- Bonding-System korrekt anschließen (alle Unterwasser-Metalle
  miteinander verbinden).
- Regelmäßige Prüfung der Leckströme.

### 13.4 Anodenmaterialien

| Material | Einsatz | Potential (V) | Kapazität (Ah/kg) | Preis |
|----------|---------|:---:|:---:|:---:|
| Zink | Seewasser (Salzwasser) | −1,03 | 780 | Günstig |
| Aluminium | Brackwasser, Seewasser | −1,05 | 2.700 | Mittel |
| Magnesium | Süßwasser | −1,70 | 1.230 | Günstig |

**Warnung:** Magnesium-Anoden in Seewasser → zu hoher Strom →
Überprotection → Wasserstoffversprödung der Welle!
Zink-Anoden in Süßwasser → zu geringer Strom → kein Schutz!

### 13.5 Bonding-System

Das Bonding-System verbindet alle Unterwasser-Metalle elektrisch
miteinander, damit sie alle dasselbe galvanische Potential haben
und die Opferanoden sie schützen können.

**Zu verbindende Komponenten:**
- Propellerwelle
- Propeller (über Welle)
- P-Bracket
- Stevenrohr (wenn Bronze/Metall)
- Ruderschaft
- Seeventile (Bronze)
- Kielbolzen (bei Bleikintel)
- Motorblock (über Masseband)
- Borddurchlässe

**Bonding-Leitung:**
- Material: Verzinntes Kupferkabel, min. 6 mm² (Sportboot),
  min. 16 mm² (> 15 m Bootslänge).
- Verbindungen: Geschraubte Kabelschuhe (keine Klemmverbindungen).
- Prüfung: Widerstand zwischen allen verbundenen Teilen < 1 Ω.
- Jährlich prüfen: Korrodierte oder lose Verbindungen ersetzen.

**Häufige Fehler beim Bonding:**
1. Motor nicht am Bonding angeschlossen → Motorblock als separate
   galvanische Zelle → Korrosion an Motorteilen.
2. Aluminiumteile im Bonding-System → Aluminium opfert sich →
   Aluminium-Rumpfschäden.
3. Kabelschuhe korrodiert → Bonding unterbrochen → einzelne Teile
   ungeschützt.
4. Kein Bonding vorhanden → Jedes Unterwasser-Metall frisst
   für sich → unkontrollierte Korrosion.

### 13.6 Galvanischer Schutz — Kosten und Nutzen

| Schutzmaßnahme | Kosten | Schützt gegen | Effektivität |
|----------------|:---:|---------|:---:|
| Zinkanoden (jährlich) | 30–100 EUR | Natürliche galvanische Korrosion | Gut |
| Korrektes Bonding | 200–500 EUR (einmalig) | Unkontrollierte Potentialdifferenzen | Sehr gut |
| Galvanic Isolator | 200–500 EUR | Streustrom über Landstrom | Gut |
| Isolation Transformer | 1.500–4.000 EUR | Alle externen galvanischen Einflüsse | Hervorragend |
| AGS (Active Galvanic Shield) | 500–2.000 EUR | Streustrom (aktive Kompensation) | Sehr gut |

**Kosten-Nutzen-Analyse (5 Jahre):**
- Anoden + Bonding: 500–1.000 EUR → Schutz gegen normalen Abtrag.
- Galvanic Isolator: 300–500 EUR → Schutz gegen Marina-Streustrom.
  Ein Propeller kostet 1.500–3.000 EUR → Isolator amortisiert sich
  beim ersten verhinderten Schaden.
- Isolation Transformer: 2.000–4.000 EUR → Maximaler Schutz für
  Superyachten und dauerhaften Landstromanschluss.

---
---

## 14. Volvo Saildrive — Wellenabdichtung und Manschette

### 14.1 Saildrive-Prinzip

Der Saildrive (Volvo Penta) ersetzt die klassische Wellenanlage
bei Segelyachten im Bereich 10–75 PS. Statt einer langen Welle
durch ein Stevenrohr wird der Antrieb direkt unter dem Motor
durch den Rumpf geführt:

```
Motor → Getriebe (oben) → Abtriebswelle (vertikal durch Rumpf) →
  Umlenkgetriebe (unter Rumpf) → Propeller
```

### 14.2 Kritische Dichtung: Saildrive-Manschette

Die Saildrive-Manschette ist die einzige Dichtung zwischen
Bootsinnern und Meer. Sie umschließt den Saildrive-Schaft am
Rumpfdurchbruch.

**Material:** Neopren/EPDM-Gummi, mit Edelstahl-Befestigungsring.

**Volvo-Vorschrift (Service Bulletin):**
- Manschette alle 7 Jahre austauschen (unabhängig vom Zustand).
- Jährliche Sichtprüfung auf Risse, Versprödung, Pilzbefall.
- Prüfung auf Festsitz des Spannrings.

**Austauschkosten:**

| Position | Kosten |
|----------|:---:|
| Manschette (Original Volvo 3842630) | 80–120 EUR |
| Spannring + Schrauben | 30–50 EUR |
| Arbeit (Boot an Land, ca. 2 h) | 200–400 EUR |
| Gesamt | 310–570 EUR |

### 14.3 Saildrive-Anode

Der Saildrive hat eine eigene Zinkanode (Ring-Anode um das Getriebe):

- Volvo-Teilenummer: 3888305 (Zink) oder 3888816 (Aluminium).
- Jährlich prüfen, spätestens bei 50 % Abtrag wechseln.
- Preis: 25–50 EUR.
- **Anode NICHT streichen!** (reduziert die Schutzwirkung).

### 14.4 Saildrive-Getriebeöl und Diagnose

Das Saildrive-Getriebe enthält ca. 0,5–1,0 l Getriebeöl, das
entscheidende Diagnoseinformationen liefert:

**Ölzustandsbewertung:**

| Ölzustand | Bedeutung | Maßnahme |
|-----------|-----------|----------|
| Klar, goldbraun | Normal | Jährlicher Wechsel |
| Dunkel, aber nicht trüb | Normaler Verschleiß | Wechseln, überwachen |
| Milchig/emulgiert | Wassereinbruch! Dichtung undicht | Sofort Werft! Saildrive-Dichtung prüfen |
| Metallflitter sichtbar | Getriebe-Verschleiß | Werft, Getriebe inspizieren |
| Geruch nach verbrannt | Überhitzung | Öl wechseln, Ölmenge prüfen |

**Ölwechsel-Intervall:** Jährlich oder alle 200 Betriebsstunden.
Preis: 15–30 EUR (Öl) + 30 Minuten Arbeit.

**Kritisch: Milchiges Öl**
Milchiges Getriebeöl bedeutet, dass Seewasser in das Getriebe
eingedrungen ist — typischerweise über die interne Dichtung zwischen
Unterwasser-Einheit und Motor. Dies ist eine KRITISCHE Situation:
- Wasser im Getriebe → Lagerschäden, Zahnradkorrosion.
- Unbehandelt: Getriebeaustausch nötig (3.000–8.000 EUR).
- Sofortmaßnahme: Boot aus dem Wasser, Getriebe spülen,
  Dichtung ersetzen, ggf. Lager ersetzen.

### 14.5 Yanmar Saildrive (SD20/SD25/SD40/SD50)

Neben Volvo Penta bietet auch Yanmar Saildrive-Systeme an:

| Modell | Motor | Leistung | Besonderheit |
|--------|-------|:---:|-------------|
| SD20 | 3YM20 | 21 PS | Kompakt, bis 10 m |
| SD25 | 3YM30 | 29 PS | Standard, bis 12 m |
| SD40 | 4JH45 | 45 PS | Leistungsstark, bis 14 m |
| SD50 | 4JH57 | 57 PS | Größte Yanmar-Saildrive |

**Yanmar vs. Volvo Saildrive:**
- Yanmar-Manschette: Alle 10 Jahre wechseln (vs. 7 Jahre bei Volvo).
- Yanmar-Anode: Ähnlich Volvo, jährlich prüfen.
- Yanmar-Getriebeöl: SAE 30 oder GL-4/GL-5 (herstellerspezifisch).
- Ersatzteil-Verfügbarkeit: Volvo weltweit besser, Yanmar in Asien
  besser.

> ⚠️ **ZU PRÜFEN (Audit):** Manschetten-Intervall Yanmar "10 Jahre" (hier) vs. "7 Jahre" in ANHANG H — dort auf denselben Yanmar SD20 angewendet. Interner Widerspruch bei einer sicherheitskritischen Dichtung (einzige Barriere gegen Wassereinbruch). Yanmars eigene SD-Servicevorgaben nennen deutlich kürzere Intervalle (SD20 ≈ 5 Jahre, spätere SD-Modelle bis 7 Jahre), nicht 10 Jahre. Confidence: estimated — unverifiziert; im Zweifel das kürzere Intervall wählen.

### 14.6 Saildrive vs. Wellenanlage

| Kriterium | Saildrive | Wellenanlage |
|-----------|:---:|:---:|
| Installation | Werft / Einbauer | Werft / Einbauer |
| Wartung Dichtung | 7-Jahres-Tausch Manschette | Stopfbuchse/PSS: laufend bis 10 J. |
| Propeller-Effizienz | Gut (kurzer Schaft) | Gut (langer Schaft, aber optimierte Strömung) |
| Vibration | Gering (kurzer Antriebsstrang) | Mittel (abhängig von Ausrichtung) |
| Manövrieren | Standard (Ruder nötig) | Standard (Ruder nötig) |
| Reparierbarkeit auf See | Schwierig (Spezialteile) | Gut (Stopfbuchse universal) |
| Kosten Austausch komplett | 6.000–12.000 EUR | 2.000–8.000 EUR |
| Motorausrichtung | Nicht nötig (fixe Einheit) | Kritisch, jährlich prüfen |
| Gewicht | Leichter (kein Stevenrohr) | Schwerer |
| Tiefgang-Einfluss | Minimal (unter dem Rumpf) | Gering bis mittel (Schrägwelle) |
| Geeignet für Langfahrt | Bedingt (Ersatzteile schwierig) | Gut (universell reparierbar) |

### 14.7 Saildrive-Wartungscheckliste

**Jährlich (bei jedem Antifouling-Anstrich):**
1. Manschette visuell prüfen (Risse, Versprödung, Pilz).
2. Spannring-Sitz prüfen (fest?).
3. Zinkanode prüfen, bei > 50 % Abtrag wechseln.
4. Getriebeöl wechseln, auf Wassereinbruch (milchig) prüfen.
5. Antifouling auf Saildrive-Gehäuse erneuern
   (KEIN kupferhaltiges Antifouling auf Aluminium-Saildrive!).
6. Propeller prüfen (Blätter, Passfeder, Mutter).

**Alle 3 Jahre:**
1. Saildrive-Gehäuse auf Korrosion prüfen (besonders Aluminium).
2. Interne Dichtungen prüfen (Ölverlust?).
3. Propeller-Konus prüfen (Bluing-Test).

**Alle 7 Jahre (Volvo) / 10 Jahre (Yanmar):**
1. Manschette austauschen (auch wenn sie gut aussieht!).
2. Alle O-Ringe und Dichtungen erneuern.
3. Lager prüfen lassen (Werkstatt).

---
---

## 15. Fehlerbild-Atlas

### Fehlerbild 1: Vibration im Antriebsstrang

**Symptom:** Vibration bei bestimmten Drehzahlen, spürbar am
Steuerstand, am Motor, am Rumpf. Intensität steigt mit Drehzahl.

**Mögliche Ursachen (häufigste zuerst):**
1. Motorausrichtung fehlerhaft (50 % aller Fälle)
2. Propeller unwuchtig / beschädigt (25 %)
3. Cutless-Bearing verschlissen (10 %)
4. Kupplung verschlissen (5 %)
5. Welle verbogen (5 %)
6. Propeller-Kavitation (3 %)
7. Motorlager verschlissen (2 %)

**Diagnose:**
- Drehzahl der maximalen Vibration notieren.
- Motor im Leerlauf (ohne Welle): vibriert → Motorproblem.
- Motor unter Last, Vorwärts und Rückwärts: vibriert nur Vorwärts → Propeller.
- Vibriert bei allen Drehzahlen → Ausrichtung oder Welle.
- Vibriert nur bei bestimmter Drehzahl → Resonanz, Kupplung.

**AYDI-Bewertung:** Vibration ist NIEMALS "normal". Jede spürbare
Vibration hat eine Ursache und muss beseitigt werden, bevor
Folgeschäden entstehen.

---

### Fehlerbild 2: Motorausrichtung fehlerhaft (Misalignment)

**Symptom:** Vibration, Dichtungsleckage, vorzeitiger Verschleiß
Cutless-Bearing und Kupplung, Geräusche beim Schalten.

**Ursachen:**
1. Motorlager eingesunken (Gummi-Alterung)
2. Rumpfverformung (Böcke, Temperatur, Belastung)
3. Nach Reparatur nicht nachgerichtet
4. Grundberührung mit Wellenverformung
5. Getriebewechsel ohne Nachausrichtung

**Diagnose:**
- Messuhr an Kupplungsflansch: TIR > 0,1 mm → Fehlausrichtung.
- Sichtprüfung Kupplungsspalt: ungleichmäßig → Winkelversatz.
- Fingertest an Kupplungsflansch (Motor aus): Absatz tastbar → Parallelversatz.

**Maßnahme:**
- Motorausrichtung nach Abschnitt 9 durchführen.
- Kosten: 200–600 EUR (Werft), 0–50 EUR (Selbst mit Messuhr).

---

### Fehlerbild 3: Wellendichtung leckt (Seal Leak)

**Symptom:** Wasser in der Bilge, Tropfen an der Stopfbuchse,
nasse Umgebung um die Dichtung.

**Differentialdiagnose nach Dichtungstyp:**

| Dichtung | Normales Verhalten | Anormales Verhalten | Sofortmaßnahme |
|----------|-------------------|-------------------|----------------|
| Stopfbuchse | 6–12 Tropfen/min bei Fahrt | > 30 Tropfen/min oder Strahl | Muttern 1/6 Umdrehung anziehen |
| PSS | 0–1 Tropfen/min | Rinnen oder Spritzen | Motor aus, Bellows + Schlauchschellen prüfen |
| SureSeal | 0–1 Tropfen/min | Rinnen | Motor aus, Lippendichtung prüfen |
| Saildrive | 0 Tropfen | Jede Feuchtigkeit | Boot aus dem Wasser, Manschette prüfen |

**Ursachen Stopfbuchse:**
- Packung verschlissen → neu packen
- Muttern zu locker → nachziehen
- Welle verschlissen (Rillen) → Welle schleifen oder Hülse

**Ursachen PSS:**
- Bellows gerissen → sofort austauschen (NOTSITUATION!)
- Schlauchschellen gelöst → nachziehen
- Carbon-Ring verschlissen → austauschen
- Kein Wasser an der Dichtung (trocken) → Wasserversorgung prüfen
- Welle zu rauh → polieren

**AYDI-Bewertung:** Jede Leckage an der Wellendichtung ist ernst
zu nehmen. Eine gebrochene PSS-Bellows kann zum Sinken führen.
Bilgepumpe muss IMMER funktionsfähig sein.

---

### Fehlerbild 4: Cutless-Bearing verschlissen

**Symptom:** Vibration, Klopfgeräusche bei niedrigen Drehzahlen,
Spiel am Propeller (wackelt), ungleichmäßiger Wellenverschleiß.

**Diagnose:**
- Propeller mit Hand hin- und herbewegen: Spiel > 0,5 mm → verschlissen.
- Visuell (Boot an Land): Gummirillen < 1 mm Resttiefe.
- Vibration, die bei Drehzahl-Änderung verschwindet/erscheint.

**Ursachen vorzeitigen Verschleißes:**
- Sand/Sediment im Wasser (Revierabhängig)
- Fehlausrichtung → einseitiger Verschleiß
- Motor gestartet ohne Wasser (Trockenfall) → Gummi verbrannt
- Mangelnde Wasserschmierung (z.B. verstopfter Stevenrohr-Einlass)

**Maßnahme:** Cutless-Bearing austauschen (siehe Abschnitt 4.5).
Bei einseitigem Verschleiß: Ausrichtung korrigieren.

---

### Fehlerbild 5: Kupplungsversagen

**Symptom:** Metallisches Klappern, Vibrationsänderung beim Schalten,
Gummiabrieb, Spiel in der Kupplung.

**Diagnose:**
- Sichtprüfung Elastomer: Risse, Ablösung, Verhärtung.
- Spiel prüfen: Welle halten, Motor/Getriebe drehen → Spiel > 2° → Verschleiß.
- Gummiabrieb unter der Kupplung → Elastomer zerbröselt.

**Ursachen:**
- Alterung (>15 Jahre)
- Ölkontakt (Getriebeöl, Bilge-Öl)
- Überlast (Grundberührung, Leine im Propeller)
- Fehlausrichtung → ungleichmäßige Belastung

**Maßnahme:** Elastomer oder Kupplung tauschen. Kosten: 150–900 EUR.

---

### Fehlerbild 6: Wellenkorrosion

**Symptom:** Pitting, Oberflächenrauheit, Querschnittsverringerung,
verfärbte Stellen (braun, grün, schwarz).

**Differentialdiagnose:**

| Korrosionsart | Erscheinungsbild | Ursache | Maßnahme |
|--------------|-----------------|---------|----------|
| Galvanisch | Gleichmäßiger Abtrag | Fehlende/verbrauchte Anoden | Anoden erneuern |
| Streustrom | Aggressives Pitting, schnell | Elektrisches Leck | Fehler finden, Isolator einbauen |
| Spaltkorrosion | Korrosion unter Schlauchschellen, Klammern | Sauerstoffarmut unter Spalt | Edelstahl-Schellen, regelmäßig lösen |
| Biologisch | Schwarze Flecken, Biofilm | Sulfatreduzierende Bakterien | Reinigen, Antifouling |

**AYDI-Bewertung:** Welle mit Pitting > 0,5 mm Tiefe im Lager- oder
Dichtungsbereich → Austausch empfohlen. Im Schaftbereich bis 1 mm
akzeptabel, aber überwachen.

---

### Fehlerbild 7: Elektrolyse am Propeller/Welle

**Symptom:** Pinkfarbene oder raue Oberfläche am Propeller (De-Zinkung
bei Messing), Pitting an Welle und Propeller, Anoden verbrauchen sich
in < 3 Monaten.

**Diagnose:**
1. Anoden prüfen: > 50 % in 3 Monaten → abnormaler Verbrauch.
2. Strom messen: Referenz-Elektrode + Multimeter (siehe 13.3).
3. Landstrom abklemmen → Problem verschwindet → Landstrom-Fehler.
4. Nachbar-Boote prüfen (Strom über Wasser/Steg).
5. Bonding-System prüfen: Alle Unterwasser-Metalle verbunden?

**Maßnahme:**
- Sofort: Frische Anoden montieren.
- Galvanic Isolator einbauen (200–500 EUR).
- Bonding-System überprüfen.
- Landstrom-Verkabelung von Elektriker prüfen lassen.
- Im Extremfall: Isolation Transformer (1.500–4.000 EUR).

---

### Fehlerbild 8: Konus/Passfeder-Versagen (Taper/Keyway Failure)

**Symptom:** Propeller sitzt locker, dreht durch auf der Welle,
metallisches Klirren bei Lastwechsel, Propeller wandert nach achtern.

**Diagnose:**
- Propellermutter prüfen: locker → nachziehen + Splint.
- Konus-Sitz prüfen (Bluing-Test): < 70 % Kontakt → Konus beschädigt.
- Passfeder inspizieren: verformt, gelängt, gebrochen.
- Passfedernut inspizieren: aufgeweitet, Grate.

**Ursachen:**
- Propellermutter nicht korrekt angezogen.
- Korrosion am Konus (mangelndes Fetten bei Montage).
- Falsches Passfeder-Material (Messing statt Edelstahl).
- Überlast (Grundberührung, Leine).

**Maßnahme:**
- Neue Passfeder, Konus reinigen, mit Tef-Gel montieren.
- Bei beschädigtem Konus: Welle nachdrehen oder ersetzen.
- Bei beschädigter Propellernabe: Propeller nachbohren oder ersetzen.
- Kosten: 50–300 EUR (Passfeder/Reinigung) bis 2.000–5.000 EUR (neue Welle + Propeller).

---

### Fehlerbild 9: P-Bracket-Riss

**Symptom:** Riss sichtbar am P-Bracket (meist am Befestigungsfuß
oder am Übergang zum Lagergehäuse), Vibration, Wassereinbruch
(bei durchgehendem Riss).

**Diagnose:**
1. Visuell: Risse, Verfärbungen (grüne Patina an Rissenden bei Bronze).
2. Farbeindringprüfung (Penetrant Testing): aufsprühen, warten,
   abwischen, Entwickler → Risse werden sichtbar.
3. Ultraschall: Bei dickwandigen Brackets Innenrisse erkennen.

**Ursachen:**
- Ermüdung (Vibration über Jahre).
- Grundberührung (Schlagbelastung).
- Korrosion (Materialverlust schwächt Querschnitt).
- Fehlausrichtung (übermäßige Biegebelastung).

**Maßnahme:**
- Kleiner Riss (< 20 mm, nicht durchgehend): schweißen (nur Fachbetrieb!).
- Großer Riss oder durchgehend: P-Bracket ersetzen.
- Nach jeder Reparatur: Ausrichtung prüfen.
- Kosten: Schweißreparatur 300–800 EUR, Austausch 800–7.000 EUR.

---

### Fehlerbild 10: Stopfbuchse tropft zu stark oder gar nicht

**Symptom A — Zu stark (> 30 Tropfen/min bei Fahrt):**
- Packung verschlissen → neue Packung.
- Welle verschlissen (Rillen) → Hülse oder neue Welle.
- Muttern zu locker → 1/6 Umdrehung anziehen, 30 s warten.

**Symptom B — Gar nicht (0 Tropfen bei Fahrt):**
- **SOFORT etwas lösen!** Überhitzungsgefahr!
- Muttern 1/4 Umdrehung lösen.
- 1 Minute warten, Tropfrate beobachten.
- Wenn immer noch 0 Tropfen: Packung komplett erneuern (verkohlt/verhärtet).

**AYDI-Bewertung:** Eine Stopfbuchse, die bei laufendem Motor nicht
tropft, ist eine KRITISCHE Situation. Priorität Stufe 1. Die Welle
kann sich blau verfärben (> 200 °C), Packung verkohlt, im schlimmsten
Fall löst sich die Packung und Wasser strömt unkontrolliert ein.

---

### Fehlerbild 11: PSS-Bellows-Versagen

**Symptom:** Plötzlicher Wassereinbruch an der Wellendichtung, PSS
sprüht oder rinnt statt tropffrei zu sein, sichtbare Risse im
Gummibalg.

**Diagnose:**
- Bellows visuell inspizieren: Risse, Versprödung, Aufquellen.
- Schlauchschellen: lose? Korrodiert?
- Carbon-Ring: gerissen, ungleichmäßig abgenutzt?

**Ursachen:**
- Alterung (> 8 Jahre → Gummi versprödet).
- UV-Exposition (wenn Maschinenraum offen).
- Ölkontakt (Bilge-Öl greift Gummi an).
- Ozon (Ozon-Rissbildung bei EPDM).
- Mechanische Beschädigung (Werkzeug, Kabel).

**SOFORT-MAßNAHME bei Wassereinbruch:**
1. Motor aus.
2. Bilgepumpe aktivieren.
3. Notdichtung improvisieren: Handtuch + Schlauchschelle um die Welle.
4. Seeventil (falls vorhanden) schließen.
5. Boot aus dem Wasser oder zur nächsten Werft.

**Prävention:**
- Bellows alle 5–7 Jahre tauschen (auch wenn sie gut aussehen).
- Spare Bellows an Bord haben (Langfahrt!).
- Notdichtmaterial bereithalten (Unterwasser-Epoxy, Gummibandage).

---

### Fehlerbild 12: Grundberührungsschaden (Grounding Damage)

**Symptom:** Vibration nach Grundberührung, Propeller beschädigt,
Welle klopft, Dichtung leckt plötzlich, P-Bracket verbogen.

**Diagnose-Protokoll nach Grundberührung:**
1. Sofort Motor aus, visuelles Prüfen (Taucher oder Kamera).
2. Propeller: Blätter verbogen, abgebrochen, gerissen?
3. Welle: Schlag prüfen (Welle drehen, Messuhr am Stevenrohr).
   Max. Schlag: 0,05 mm bei 1" Welle.
4. P-Bracket: Risse, Verformung?
5. Stevenrohr: Risse im GFK?
6. Cutless-Bearing: Zerstört?
7. Dichtung: Leckt?
8. Motorausrichtung: Kupplungsflansch prüfen.

**Mögliche Schäden und Kosten:**

| Schadenskategorie | Kosten (typisch) | Dringlichkeit |
|-------------------|:---:|:---:|
| Propellerblatt verbogen (reparabel) | 200–500 EUR | Mittel |
| Propeller zerstört | 500–3.000 EUR | Hoch |
| Welle verbogen | 800–3.000 EUR | Hoch |
| P-Bracket gerissen | 800–7.000 EUR | Kritisch |
| Stevenrohr-Laminat gerissen | 1.000–5.000 EUR | Kritisch |
| Cutless-Bearing zerstört | 280–2.000 EUR | Mittel |
| Getriebe-Ausgangswellenlager | 1.000–5.000 EUR | Hoch |
| Rumpfschaden (Osmosegefahr) | 2.000–15.000 EUR | Hoch |

**AYDI-Bewertung:** Nach jeder Grundberührung — auch bei "harmlos
wirkenden" — ist eine vollständige Inspektion der Wellenanlage
obligatorisch. Versteckte Schäden (Mikrorisse, Wellenverformung)
manifestieren sich oft erst nach Wochen oder Monaten als Vibration
oder plötzlicher Ausfall.

---
---

## 16. Troubleshooting

### Troubleshooting 1: Systematische Vibrationsdiagnose

**Problem:** Vibration im Antriebsstrang, Ursache unbekannt.

**Systematische Analyse (Ausschlussverfahren):**

| Schritt | Aktion | Ergebnis → Diagnose |
|:---:|--------|-------------------|
| 1 | Motor im Leerlauf (Neutral) | Vibriert → Motor (Zylinder, Lager, Injektoren) |
| 2 | Motor in Gang, Standgas | Vibriert → Kupplung oder Getriebe |
| 3 | Motor unter Last, 1.000 U/min | Vibriert → Ausrichtung oder Cutless |
| 4 | Motor unter Last, 2.000 U/min | Vibriert → Propeller oder Resonanz |
| 5 | Motor unter Last, Nenndrehzahl | Vibriert → Propeller (Kavitation) oder Welle |
| 6 | Motor unter Last, Rückwärts | Vibriert Rückwärts NICHT → Propeller (Blattriss) |
| 7 | Propeller ab, Motor unter Last | Vibriert → Welle, Cutless, Ausrichtung |
| 8 | Neue Ausrichtung durchführen | Vibration weg → Fehlausrichtung war's |

### Troubleshooting 2: Stopfbuchse lässt sich nicht einstellen

**Problem:** Stopfbuchse tropft trotz Nachziehen zu stark, oder
wird sofort trocken beim Anziehen.

**Diagnose:**
1. Packung > 2 Jahre / > 500 h alt? → Neue Packung.
2. Welle im Dichtungsbereich prüfen: Rillen > 0,1 mm? → Welle
   schleifen oder Hülse.
3. Stopfbuchsen-Gehäuse innen prüfen: Korrosion? → Reinigen oder
   ersetzen.
4. Verschiedene Packungsmaterialien gemischt? → Komplett neu packen,
   nur ein Material.
5. Packungsquerschnitt korrekt? Zu dünn oder zu dick → korrekte Größe.

### Troubleshooting 3: PSS sprüht Wasser bei hohen Drehzahlen

**Problem:** PSS ist bei niedrigen Drehzahlen tropffrei, aber bei
> 2.500 U/min sprüht oder tropft es stark.

**Diagnose:**
1. Bellows-Kompression prüfen: Zu gering? → Schlauchschellen
   korrigieren (6–10 mm Kompression).
2. Wasserversorgung prüfen: Druck zu hoch? → Drosselventil.
3. Carbon-Ring: verschlissen, uneben? → Ersetzen.
4. Rotierender Ring: Scoring, Rillen? → Schleifen oder ersetzen.
5. Wellenoberfläche: zu rauh? → Polieren (Ra ≤ 0,4 µm).
6. Wellenversatz: PSS wird bei Drehzahl dezentriert? → Ausrichtung.

### Troubleshooting 4: Ungewöhnliche Geräusche aus dem Stevenrohr

**Problem:** Klopfen, Quietschen, Brummen, Pfeifen aus dem
Stevenrohr-Bereich.

| Geräusch | Mögliche Ursache | Maßnahme |
|----------|-----------------|----------|
| Klopfen (periodisch, 1×/Umdrehung) | Propeller beschädigt (Blatt) | Propeller prüfen |
| Klopfen (unregelmäßig) | Cutless-Bearing verschlissen, Welle schlägt | Spiel prüfen |
| Quietschen (kontinuierlich) | Trockenes Cutless-Bearing | Wasserversorgung prüfen |
| Quietschen (beim Anlaufen) | PSS trocken angelaufen | Wasser bereitstellen vor Start |
| Brummen (resonant) | Wellenresonanz | Drehzahl variieren, Kupplung prüfen |
| Pfeifen (hochfrequent) | Kavitation am Propeller | Propeller prüfen, Pitch anpassen |
| Kratzen | Fremdkörper im Stevenrohr | Motor aus, inspizieren |

### Troubleshooting 5: Wassereinbruch an der Wellenanlage

**Problem:** Wasser kommt aus dem Bereich der Wellendichtung —
mehr als normale Stopfbuchsen-Tropfrate.

**SOFORT-PROTOKOLL:**
1. **Einschätzung**: Rinnt es oder strömt es?
   - Rinnen (< 1 l/min): Dringend, aber kontrollierbar.
   - Strömen (> 5 l/min): NOTFALL. Bilgepumpe, Mayday erwägen.
2. **Bilgepumpe einschalten** (elektrisch + manuell).
3. **Ursache identifizieren:**
   - Stopfbuchse: Muttern nachziehen (maximal 1 Umdrehung).
   - PSS: Bellows gerissen? → Improvisierte Dichtung (Gummibandage,
     Handtuch + Schlauchschellen, Unterwasser-Epoxy).
   - Saildrive: Manschette gerissen → Boot SOFORT aus dem Wasser.
4. **Seeventil schließen** (wenn separate Wasserversorgung der Dichtung).
5. **Motor aus** (bei PSS — Rotation verschlimmert Bellows-Riss).
6. **Zur nächsten Werft / an Land**.

---
---

## 17. FAQ

### FAQ 1: Wie oft muss die Motorausrichtung geprüft werden?

**Empfehlung AYDI:** Mindestens einmal jährlich bei Saisonstart.
Zusätzlich nach jeder Reparatur an Motor, Getriebe, Kupplung,
Motorlagern oder Wellenanlage. Auch nach Grundberührung und nach
längerer Lagerung an Land (Rumpfverformung durch Böcke).
Aufwand: 30 Minuten mit Messuhr, Kosten 0 EUR bei Eigenarbeit.

### FAQ 2: PSS oder Stopfbuchse — was ist besser?

Beides hat Berechtigung:
- **PSS** für: Neubauten, Komfort-orientierte Eigner, wer keine
  Tropfwasser-Bilge will, Charterbetrieb.
- **Stopfbuchse** für: Langfahrer (universal reparierbar), Budget,
  alte Boote mit rauer Welle, Traditionalisten.
- **Kombination** (selten, aber möglich): Einige Langfahrer bauen eine
  PSS als Primärdichtung und behalten eine Notfall-Stopfbuchse dahinter.

### FAQ 3: Kann ich von Stopfbuchse auf PSS umrüsten?

Ja, in den meisten Fällen. Voraussetzungen:
1. Wellendurchmesser im PSS-Bereich (3/4" bis 3").
2. Welle im Dichtungsbereich polierbar (keine tiefen Rillen).
3. Stevenrohr-Innendurchmesser passt zum PSS-Adapter.
4. Genug Platz zwischen Stevenrohr-Ende und Kupplung.
Kosten: 300–800 EUR (Material) + 200–500 EUR (Einbau).

### FAQ 4: Wie erkenne ich, dass das Cutless-Bearing gewechselt werden muss?

Drei Methoden:
1. **Propeller wackeln**: Am Propellerende nach oben/unten drücken.
   Spiel > 0,5 mm (1" Welle) → Austausch.
2. **Visuell** (Boot an Land): Gummirillen < 1 mm Tiefe → Austausch.
3. **Vibration**: Klopfen bei niedrigen Drehzahlen, das bei höheren
   verschwindet → typisch für Cutless-Verschleiß.

### FAQ 5: Welches Anodenmaterial für mein Boot?

| Revier | Empfohlenes Anodenmaterial |
|--------|:---:|
| Seewasser (> 20 ppt Salzgehalt) | Zink |
| Brackwasser (5–20 ppt) | Aluminium |
| Süßwasser (< 5 ppt) | Magnesium |
| Wechselnde Reviere | Aluminium (universell einsetzbar) |

### FAQ 6: Wie oft Zinkanoden wechseln?

**Faustregel:** Wenn > 50 % des Materials abgetragen ist → wechseln.
Typische Intervalle:
- Segelboot (wenig Betriebsstunden): jährlich prüfen.
- Motorboot (viel Betriebsstunden): halbjährlich prüfen.
- Marina mit Streustrom-Problemen: vierteljährlich prüfen.
- Anoden verbrauchen sich in < 3 Monaten → Streustrom-Problem!

### FAQ 7: Meine Welle hat Rillen im Dichtungsbereich — was tun?

Optionen:
1. **Schleifen/Polieren**: Bei Rillen < 0,1 mm Tiefe. Schmirgelpapier
   600er nass, dann 800er, dann 1000er. Welle muss dabei rotieren.
2. **Repair Sleeve**: Bei Rillen 0,1–0,5 mm. Edelstahlhülse
   aufgepresst (200–600 EUR).
3. **Neue Welle**: Bei Rillen > 0,5 mm oder Pitting. Kosten:
   800–3.000 EUR je nach Länge und Material.

### FAQ 8: Was ist die Aquadrive und brauche ich sie?

Aquadrive ist ein Komplettsystem aus flexibler Kupplung + CVL-Drucklager,
das den Motor vollständig vom Propellerschub entkoppelt. Lohnt sich bei:
- Vibrationsproblemen trotz guter Ausrichtung.
- Komfort-orientierten Eignern (Motoryachten).
- Neuinstallation (einfacher als Nachrüstung).
Nicht nötig bei: kleinen Segelbooten, Budget-Installationen, wenn
die Standard-Ausrichtung gut ist.

### FAQ 9: Kann ich die Motorausrichtung selbst machen?

Ja, mit Grundwissen und einer Messuhr (50–80 EUR):
1. Messuhr-Halter an einer Kupplungshälfte befestigen.
2. Taster an der anderen Hälfte.
3. Welle langsam drehen (360°), Werte ablesen.
4. TIR (Gesamtabweichung) ≤ 0,05 mm ist das Ziel.
5. Motorlager anpassen, erneut messen.
Zeitaufwand: 1–3 Stunden. Geduld ist die wichtigste Zutat.

### FAQ 10: Warum hat mein Boot so starke Vibrationen bei Rückwärtsfahrt?

Ursachen:
1. Propeller ist nicht für Rückwärtsfahrt optimiert (normal bei
   Festpropellern).
2. Wasser-Anströmung zum Propeller ist gestört (Ruderblatt,
   P-Bracket im Propellerstrahl).
3. Cutless-Bearing-Verschleiß (Welle hebt im Rückwärtsgang ab).
4. Motorausrichtung nicht korrekt (bei Rückwärts andere Schubrichtung).
**Leichte Vibration im Rückwärtsgang ist bei vielen Booten normal.**
Starke Vibration → Diagnose nach Troubleshooting 1.

### FAQ 11: Was kostet eine komplett neue Wellenanlage?

| Bootsklasse | Welle | Cutless | Dichtung (PSS) | Kupplung | Einbau | Gesamt |
|------------|:---:|:---:|:---:|:---:|:---:|:---:|
| Segelboot 10 m | 400–800 | 80–150 | 320–400 | 200–400 | 500–1.500 | 1.500–3.250 |
| Motorboot 12 m | 600–1.200 | 100–200 | 350–500 | 250–500 | 800–2.000 | 2.100–4.400 |
| Motoryacht 15 m | 800–2.000 | 150–300 | 450–600 | 400–800 | 1.500–3.500 | 3.300–7.200 |
| Motoryacht 20 m | 1.500–3.000 | 250–500 | 650–900 | 600–1.200 | 2.500–6.000 | 5.500–11.600 |

*Alle Preise EUR, Stand 2025/2026.*

### FAQ 12: Mein Boot hat einen Saildrive — worauf muss ich achten?

Drei kritische Punkte:
1. **Manschette**: Alle 7 Jahre wechseln (Volvo-Vorschrift), jährlich prüfen.
2. **Anode**: Jährlich prüfen, bei > 50 % Abtrag wechseln.
3. **Getriebeöl**: Jährlich wechseln, Ölstand halbjährlich prüfen.
   Ölverlust → Dichtung im Saildrive undicht → Werft!

### FAQ 13: Wie laut darf eine Wellenanlage sein?

**Richtwerte (bei Marschfahrt):**
- Nicht hörbar über Motorgeräusch: Ideal.
- Leises Summen (nur im Maschinenraum): Normal.
- Brummen oder Vibrieren (im Salon hörbar): Prüfung empfohlen.
- Klopfen oder Klappern: Sofort prüfen, Defekt wahrscheinlich.
- Pfeifen oder Quietschen: Sofort prüfen, Trockenlauf möglich.

### FAQ 14: Propellerwelle dreht sich unter Segel — ist das schädlich?

Ja, moderat:
- Getriebe-Verschleiß (Rückwärtsdrehung ohne Öldruck).
- Dichtungsverschleiß (Rotation ohne Schmierung bei Stopfbuchse).
- Cutless-Bearing-Verschleiß (Rotation unter Segel = wenig Last
  aber viele Stunden).
- Geräusch (summender Propeller).
**Lösung**: Wellenbremse oder Faltpropeller.

### FAQ 15: Kann ich Aquamet-22-Welle mit einer 316L-Welle ersetzen?

Ja, aber mit Einschränkungen:
- 316L hat geringere Zugfestigkeit (480 vs. 760 MPa).
- Bei gleichem Durchmesser: Sicherheitsfaktor sinkt um ~30 %.
- Empfehlung: Nächstgrößeren Durchmesser wählen (z.B. 1-1/4" statt 1").
- Für Langfahrt und Hochseeeinsatz: Aquamet 22 bevorzugen.
- Für küstennahen Betrieb und Süßwasser: 316L akzeptabel.

### FAQ 16: Was ist eine Shaft Repair Sleeve?

Eine dünnwandige Edelstahl-Hülse (ca. 1–2 mm Wandstärke), die auf
die verschlissene Welle im Dichtungsbereich aufgezogen wird:
- Presspassung + Marine-Epoxy.
- Neue, glatte Oberfläche für die PSS-Dichtung.
- Kosten: 200–600 EUR (inkl. Einbau).
- Alternative zur neuen Welle (800–3.000 EUR).
- Lebensdauer: 10–20 Jahre bei korrektem Einbau.

### FAQ 17: Warum muss ich die Passfeder beim Propellertausch prüfen?

Die Passfeder überträgt das Drehmoment vom Konus zum Propeller.
Eine verformte, korrodierte oder zu kurze Passfeder kann:
- Propeller durchrutschen lassen (kein Vortrieb).
- Konus beschädigen (Fressen).
- Passfedernut aufweiten (dauerhafter Schaden an Welle und Propeller).
Kosten einer neuen Passfeder: 5–20 EUR. Kosten eines beschädigten
Konus: 500–5.000 EUR. Die Prüfung ist immer lohnend.

### FAQ 18: Wann lohnt sich ein Aquadrive-System?

Kosten-Nutzen:
- **Lohnt sich**: Motoryachten > 12 m, Vibrationsproblem nicht anders
  lösbar, Komfortanspruch, Neuinstallation.
- **Lohnt sich NICHT**: Segelboote < 12 m (Hilfsmotor), Budget-
  Installation, wenn Standard-Ausrichtung gut funktioniert.
- Typische Amortisation: Durch gesparte Motorlager- und
  Getriebelager-Reparaturen nach 5–10 Jahren.

### FAQ 19: Wie prüfe ich den P-Bracket auf Risse?

Methoden (von einfach bis professionell):
1. **Visuell**: Reinigen, mit Lupe inspizieren. Grüne Patina-Streifen
   an Bronze → Rissindikator.
2. **Klopf-Test**: Mit kleinem Hammer abklopfen — dumpfer Klang statt
   hellem Klingen → Riss oder Hohlraum.
3. **Farbeindringprüfung**: Roten Farbstoff aufsprühen, abwischen,
   weißen Entwickler aufsprühen → Risse leuchten rot. Kosten:
   Spray-Set 25–40 EUR.
4. **Ultraschall**: Professionelle Wanddickenmessung. Kosten:
   200–500 EUR beim Gutachter.

### FAQ 20: Meine PSS hat plötzlich angefangen zu tropfen — was tun?

**Sofort-Diagnose:**
1. Bellows prüfen: Riss? → Austauschen (DRINGEND!).
2. Schlauchschellen: Locker? → Nachziehen.
3. Carbon-Ring: Gesprungen, abgenutzt? → Austauschen.
4. Wasserversorgung: Zu viel Druck? → Drosselventil.
5. Welle: Neue Rille im Dichtungsbereich? → Schleifen oder Hülse.
6. Fehlausrichtung: Welle dezentriert? → Ausrichten.

### FAQ 21: Was tun bei Streustrom-Korrosion im Hafen?

Sofortmaßnahmen:
1. Landstrom abklemmen → Problem verschwindet? → Galvanic Isolator
   einbauen (200–500 EUR).
2. Problem bleibt → Nachbar-Boot als Quelle? Hafenmeister informieren.
3. Bonding-System prüfen (alle Unterwasser-Metalle verbunden).
4. Professionelle Strom-Messung: Referenz-Elektrode ins Wasser,
   Strom zwischen Welle und Referenz messen. > 50 mA → aktiv!
5. Langfristig: Isolation Transformer für maximalen Schutz.

### FAQ 22: Kann ich ein verschlissenes Cutless-Bearing selbst tauschen?

Ja, wenn das Boot an Land steht und Sie die Welle ziehen können:
1. Propeller abziehen (Abzieher nötig, 50–100 EUR).
2. Welle nach innen herausziehen.
3. Altes Bearing mit Gewindestange + Druckplatte herauspressen.
4. Neues Bearing einkühlen (Kältespray), Stevenrohr anwärmen.
5. Neues Bearing einpressen (Dichtmasse Loctite 640).
6. 24 h aushärten lassen.
7. Welle einsetzen, Propeller montieren.
Gesamtkosten: 100–250 EUR (Material + Werkzeug) vs. 300–800 EUR (Werft).

### FAQ 23: Wie wichtig ist die Wellenoberfläche für die PSS?

Sehr wichtig. Die PSS-Dichtfläche besteht aus einem Carbon-Ring,
der auf der rotierenden Welle gleitet. Jede Unebenheit:
- Erhöht Verschleiß des Carbon-Rings.
- Kann Leckage verursachen.
- Kann zu Überhitzung führen.
Anforderung: Ra ≤ 0,4 µm (Spiegel-Finish). Prüfung: Fingernagel
über den Dichtungsbereich ziehen — keinerlei Riefen spürbar.

### FAQ 24: Welche Wellendichtung für Langfahrt?

Empfehlung für Langfahrt (> 5.000 sm/Jahr, fern von Werften):
- **Primär**: PSS (tropffrei, wartungsarm).
- **Backup**: Stopfbuchsen-Material und Werkzeug an Bord (universell
  reparierbar, überall auf der Welt Material beschaffbar).
- **Notfall**: Unterwasser-Epoxy, Gummibandage, Schlauchschellen.
- **Spare Parts**: Bellows-Kit, Carbon-Ring, Schlauchschellen, Packung.

### FAQ 25: Wie prüfe ich die flexible Kupplung?

Visuell + mechanisch:
1. **Sichtprüfung**: Elastomer auf Risse, Ablösung, Verhärtung, Ölkontakt.
2. **Spiel-Prüfung**: Welle festhalten, Motor/Getriebe von Hand drehen.
   Spiel > 2° → Verschleiß.
3. **Abrieb**: Gummimehl oder -stücke unter der Kupplung → Elastomer
   bricht auseinander.
4. **Fingertest**: Elastomer eindrücken — federt zurück? Oder hart
   wie Holz? → Ausgetauscht.

### FAQ 26: Propellermutter — wie fest anziehen?

**Methode (ohne Drehmomentschlüssel):**
1. Propeller auf Konus schieben, Passfeder einlegen.
2. Mutter von Hand aufdrehen bis fest.
3. Mit Schraubenschlüssel: 1/4 bis 1/2 Umdrehung über handfest.
4. Splint einsetzen (nächstes Loch in der Kronenmutter).
5. Splintenden umbiegen.
**NIEMALS** mit Schlagschrauber! Konus-Sitz wird beschädigt.

### FAQ 27: Was ist der Unterschied zwischen P-Bracket und A-Bracket?

- **P-Bracket**: Ein einzelner, P-förmiger Bügel mit einem
  Befestigungspunkt am Rumpf. Standard bei kleineren Booten
  (8–15 m). Günstiger, einfacher zu montieren.
- **A-Bracket**: Zwei Streben bilden eine A-Form mit zwei
  Befestigungspunkten am Rumpf. Steifer, weniger Vibration,
  für größere Boote (15–30+ m).
Die Wahl hängt von Bootsgröße, Wellendurchmesser und Belastung ab.

### FAQ 28: Wie reinige ich die Wellenoberfläche für eine PSS-Dichtung?

Schritt-für-Schritt:
1. Groben Schmutz/Bewuchs mit Kunststoffschaber entfernen.
2. 400er Nassschleifpapier um die Welle wickeln (Welle drehen!).
3. 600er Nassschleifpapier (gleiche Methode).
4. 800er Nassschleifpapier für Hochglanz.
5. Abwischen mit sauberem, ölfreiem Lappen.
6. Fingernagel-Test: kein Widerstand beim Überstreichen.
**Tipp**: Scotch-Brite Fine (grau) ist ideal für die letzte Politur.
Niemals Schleifpapier in Längsrichtung verwenden — immer um die
Welle (in Rotationsrichtung).

### FAQ 29: Kann ich einen Faltpropeller als Alternative zur Wellenbremse verwenden?

Ja. Faltpropeller (Flex-O-Fold, Gori, Volvo Sail Performance)
klappen ihre Blätter zusammen, wenn der Motor aus ist:
- Widerstand unter Segel: 50–80 % weniger als Festpropeller.
- Keine Wellenrotation unter Segel → kein Getriebe-/Dichtungsverschleiß.
- Preis: 1.500–4.000 EUR (je nach Größe).
- Nachteil: Komplexer, teurer, gelegentlich Blatt-Blockaden.
- Für Regattasegler und performance-orientierte Fahrtensegler optimal.

### FAQ 30: Was muss ich bei einer Winterlagerung der Wellenanlage beachten?

Checkliste Winterlager:
1. **Stopfbuchse**: Muttern leicht lösen (1/4 Umdrehung), damit
   die Packung nicht am Schaft festklebt. Im Frühjahr wieder anziehen.
2. **PSS**: Bellows-Zustand prüfen, Wasserversorgung entleeren
   (Frostgefahr!).
3. **Cutless-Bearing**: Stevenrohr auf Bewuchs prüfen, ggf. reinigen.
4. **Zinkanoden**: Zustand prüfen, bei > 50 % Abtrag im Frühjahr
   wechseln.
5. **Propeller**: Reinigen, auf Beschädigung prüfen, ggf. polieren.
6. **Welle**: Im Dichtungsbereich mit Korrosionsschutzspray einsprühen
   (z.B. Ballistol, CRC 6-56).
7. **Wellenbremse**: Lösen! Nicht über Winter angezogen lassen
   (Beläge kleben fest).
8. **Motorausrichtung**: Im Frühjahr prüfen (Rumpf verformt sich
   auf Böcken).

### FAQ 31: Gibt es eine Notlösung für eine defekte Wellendichtung auf See?

Ja, mehrere improvisierte Lösungen:
1. **Rescue Tape / Gummi-Bandage**: Selbstverschweißendes Silikonband
   fest um die Welle und den Bellows/Stopfbuchse wickeln.
2. **Handtuch + Schlauchschellen**: Handtuch um die Welle wickeln,
   mit großen Schlauchschellen fixieren.
3. **Unterwasser-Epoxy**: Bei stillstehender Welle Epoxy auf den
   Riss auftragen (z.B. Belzona 1111, Plastic Padding).
4. **Kondom-Trick** (traditionell): Kondom über das Wellenende
   stülpen, mit Klebeband fixieren → kurzfristige Notdichtung.
5. **Motor aus, Segel setzen**: Welle steht still → Leckage reduziert.
   Wellenbremse anziehen.
Alle Lösungen sind TEMPORÄR — zur nächsten Werft fahren!

### FAQ 32: Was ist der Fingernagel-Test für die Wellenoberfläche?

Ein einfacher, aber aussagekräftiger Test:
- Fingernagel quer über den Dichtungsbereich der Welle ziehen.
- Nagel gleitet ohne Widerstand → Oberfläche gut genug für PSS.
- Nagel "klickt" oder fängt sich an einer Rille → Oberfläche zu
  rauh → schleifen oder Hülse nötig.
- Dieser Test entspricht ungefähr Ra 0,4–0,8 µm Unterscheidung.
- Für Stopfbuchsen: Fingernagel-Test ist weniger kritisch, aber
  tiefe Rillen verkürzen auch hier die Packungslebensdauer.

---
---

## 18. Glossar

| Begriff (DE) | Begriff (EN) | Erklärung |
|-------------|-------------|-----------|
| Wellenanlage | Shaft system | Gesamtheit aus Welle, Stevenrohr, Dichtung, Kupplung, Lager |
| Propellerwelle | Propeller shaft | Drehmoment-übertragende Welle zwischen Getriebe und Propeller |
| Stevenrohr | Stern tube | Rohr, das die Welle durch den Rumpf führt |
| Wellendichtung | Shaft seal | Dichtung am Stevenrohr-Innenende gegen Wassereinbruch |
| Stopfbuchse | Stuffing box / Packing gland | Traditionelle Dichtung mit Packungsringen und kontrollierter Leckage |
| Packung | Packing | Weiche Dichtungsringe in der Stopfbuchse (PTFE, Graphit, Flachs) |
| Druckscheibe | Follower / Gland | Pressscheibe, die die Packung zusammendrückt |
| PSS | Pacific Shaft Seal | Mechanische Gleitringdichtung (Dripless Seal) von PYI |
| Bellows | Bellows / Balg | Gummibalg der PSS-Dichtung, erzeugt Anpressdruck |
| Carbon-Ring | Carbon face | Stationärer Graphit-Dichtring der PSS |
| Rotor | Rotor / Collar | Rotierender Edelstahl-Ring der PSS auf der Welle |
| Cutless-Bearing | Cutlass bearing | Wassergeschmiertes Gummi-Gleitlager im Stevenrohr |
| Wellenlager | Shaft bearing | Oberbegriff für alle Wellenlagerbauarten |
| P-Bracket | P-bracket / Strut | Abstützung der Welle am Rumpf |
| A-Bracket | A-bracket | A-förmige Wellenabstützung |
| Strut | Strut | Allgemein: Abstützung (auch I-Strut, V-Strut) |
| Flexible Kupplung | Flexible coupling | Elastische Verbindung Getriebe ↔ Welle |
| Aquadrive | Aquadrive (Marke) | Kupplung + CVL-Lager als Komplettsystem |
| CVL-Lager | CVL bearing | Constant Velocity Joint + Thrust Bearing (Aquadrive) |
| Drucklager | Thrust bearing | Lager, das axialen Propellerschub aufnimmt |
| Wellenbremse | Shaft brake | Bremse, die Wellenrotation bei abgeschaltetem Motor verhindert |
| Motorausrichtung | Engine alignment | Ausrichten von Motor/Getriebe zur Propellerwelle |
| TIR | Total Indicator Reading | Gesamtabweichung bei Messuhr-Messung (max. − min.) |
| Parallelversatz | Parallel offset | Achsen von Getriebe und Welle parallel, aber versetzt |
| Winkelversatz | Angular offset | Achsen von Getriebe und Welle in einem Winkel zueinander |
| Konus | Taper | Konisches Wellenende zur Propellerbefestigung |
| Passfeder | Key / Keyway | Längskeil zur formschlüssigen Drehmoment-Übertragung |
| Kronenmutter | Castle nut | Mutter mit Schlitzen für Splint-Sicherung |
| Splint | Cotter pin / Split pin | Draht-Sicherung durch Kronenmutter und Welle |
| Zinkanode | Zinc anode | Opferanode zum galvanischen Schutz |
| Galvanische Korrosion | Galvanic corrosion | Elektrochemischer Abtrag unedleren Metalls |
| Streustrom-Korrosion | Stray current corrosion | Korrosion durch elektrische Fehlerströme |
| Galvanic Isolator | Galvanic isolator | Bauteil im Landstromkabel gegen galvanische Ströme |
| Isolation Transformer | Isolation transformer | Trenntransformator für galvanische Trennung |
| Bonding-System | Bonding system | Elektrische Verbindung aller Unterwasser-Metalle |
| Farbeindringprüfung | Dye penetrant testing (DPT) | Riss-Prüfverfahren mit Farbstoff |
| Tuschierfarbe | Prussian Blue / Bluing | Blaue Farbe zur Kontaktflächen-Prüfung am Konus |
| Wellenschlag | Shaft runout | Unrundheit der rotierenden Welle (Messuhr am festen Punkt) |
| Saildrive | Saildrive | Antrieb durch den Rumpfboden (Volvo, Yanmar) |
| Saildrive-Manschette | Saildrive diaphragm | Gummi-Dichtung am Saildrive-Rumpfdurchbruch |
| Aquamet 22 | Aquamet 22 | Standard-Wellenstahl für Yachten (UNS S21904) |
| Monel | Monel | Nickel-Kupfer-Legierung für hochwertige Wellen |
| Ra | Roughness average | Mittlere Rauheit einer Oberfläche (µm) |
| Tef-Gel | Tef-Gel | Anti-Galvanik-Paste für Metallverbindungen |
| Kavitation | Cavitation | Implosion von Dampfblasen an Propellerblättern |
| Bollard Pull | Bollard pull | Schub bei Geschwindigkeit null (maximaler Schub) |

---
---

## 19. Schnell-Referenz

### 19.1 Wellendurchmesser-Schnellauswahl

| Motor-PS | Standard-Durchmesser | Material |
|:---:|:---:|:---:|
| 10–20 | 22 mm (7/8") | Aquamet 22 / 316L |
| 20–40 | 25 mm (1") | Aquamet 22 |
| 40–75 | 30 mm (1-1/8") | Aquamet 22 |
| 75–120 | 35 mm (1-3/8") | Aquamet 22 |
| 120–200 | 40 mm (1-1/2") | Aquamet 22 / 17 |
| 200–350 | 50 mm (2") | Aquamet 17 |

### 19.2 Ausrichtungs-Toleranzen

| Methode | Parallel | Angular |
|---------|:---:|:---:|
| Fühlerlehre | 0,10 mm | 0,10 mm |
| Messuhr | 0,05 mm | 0,05 mm/100 mm |
| Laser | 0,02 mm | 0,02 mm/100 mm |
| AYDI-Empfehlung | ≤ 0,05 mm | ≤ 0,03 mm/100 mm |

### 19.3 Tropfrate Stopfbuchse

| Zustand | Tropfen/min |
|---------|:---:|
| Motor aus | 0–1 |
| Leerlauf | 2–6 |
| Marschfahrt | 6–12 |
| Vollgas | 10–20 |
| ZU VIEL | > 30 |
| ZU WENIG | 0 bei Fahrt → SOFORT lösen! |

### 19.4 Cutless-Bearing Verschleißgrenzen

| Wellendurchmesser | Max. Spiel | Austausch |
|:---:|:---:|:---:|
| 3/4" | 0,3 mm | > 0,5 mm |
| 1" | 0,4 mm | > 0,6 mm |
| 1-1/4" | 0,4 mm | > 0,7 mm |
| 1-1/2" | 0,5 mm | > 0,8 mm |
| 2" | 0,5 mm | > 1,0 mm |

### 19.5 Anodenmaterial nach Revier

| Revier | Anode |
|--------|:---:|
| Seewasser | Zink |
| Brackwasser | Aluminium |
| Süßwasser | Magnesium |
| Wechselnd | Aluminium |

### 19.6 Wartungsintervalle Übersicht

| Komponente | Prüfung | Austausch |
|-----------|:---:|:---:|
| Motorausrichtung | Jährlich | Bei Abweichung > 0,05 mm |
| Cutless-Bearing | Jährlich (Spiel) | 5–15 Jahre |
| Stopfbuchse (Packung) | Jede Fahrt (Tropfrate) | 1–3 Jahre |
| PSS (Bellows) | Halbjährlich | 5–7 Jahre |
| PSS (Carbon-Ring) | Jährlich | 8–12 Jahre |
| Flexible Kupplung | Halbjährlich | 10–20 Jahre |
| Zinkanoden | Halbjährlich | Wenn > 50 % abgetragen |
| Wellenbremse | Jährlich | Beläge: 5–10 Jahre |
| P-Bracket | Alle 2 Jahre | Bei Riss / Korrosion |
| Saildrive-Manschette | Jährlich | 7 Jahre (Volvo) |

### 19.7 Kosten-Übersicht Wellenanlage

| Komponente | Material | Arbeit | Gesamt |
|-----------|:---:|:---:|:---:|
| Cutless-Bearing 1" | 80–150 EUR | 200–400 EUR | 280–550 EUR |
| Stopfbuchsen-Packung | 10–30 EUR | 0–100 EUR | 10–130 EUR |
| PSS 1" (komplett) | 320–400 EUR | 200–500 EUR | 520–900 EUR |
| PSS Bellows-Kit | 80–150 EUR | 100–200 EUR | 180–350 EUR |
| Flexible Kupplung | 150–800 EUR | 100–300 EUR | 250–1.100 EUR |
| Motorausrichtung (Messuhr) | 0–50 EUR | 200–400 EUR | 200–450 EUR |
| Wellenbremse | 200–800 EUR | 100–300 EUR | 300–1.100 EUR |
| Zinkanoden (Set) | 20–80 EUR | 0–50 EUR | 20–130 EUR |
| Neue Welle 1" | 400–800 EUR | 500–1.500 EUR | 900–2.300 EUR |
| P-Bracket Bronze | 300–1.200 EUR | 500–2.000 EUR | 800–3.200 EUR |

---
---

## 20. ANHANG A–H: Fallstudien

### ANHANG A — Fallstudie: Chronische Fehlausrichtung bei Segelboot

**Boot:** Hallberg-Rassy 36, Baujahr 2005
**Motor:** Volvo Penta D2-55, 3.200 Betriebsstunden
**Wellenanlage:** Aquamet 22, 1" (25 mm), PSS-Dichtung, Vetus Bullflex

**Symptom:**
Seit 2 Jahren zunehmende Vibration, besonders bei 2.000–2.500 U/min.
PSS tropft gelegentlich. Cutless-Bearing 2021 gewechselt (nach 8 Jahren).
Neues Cutless 2023 schon wieder verschlissen (nach nur 2 Jahren).

**Diagnose:**
- Messuhr an Kupplungsflansch: TIR 0,28 mm parallel, 0,15 mm angular.
  → Massive Fehlausrichtung!
- Motorlager: Hintere Lager 4 mm eingesunken (Gummi-Alterung über 18 Jahre).
- Cutless-Bearing: Einseitig verschlissen (untere Hälfte 3× so stark).

**Ursache:** Motorlager-Gummi über 18 Jahre eingesunken → Motor sinkt
→ Fehlausrichtung → einseitiger Cutless-Verschleiß → Vibration →
PSS kann nicht dicht halten.

**Reparatur:**
1. Neue Motorlager: 4 × 65 EUR = 260 EUR.
2. Neue Motorausrichtung (Messuhr): 350 EUR (Werft).
3. Neues Cutless-Bearing: 180 EUR (Material + Einbau).
4. PSS-Bellows erneuert (vorsorglich): 120 EUR.

**Gesamtkosten:** 910 EUR

**Hätte vermeiden können:** Jährliche Ausrichtungskontrolle (30 min,
0 EUR) und Motorlager-Prüfung alle 5 Jahre.

**AYDI-Bewertung:** Chronische Fehlausrichtung ist ein typisches
Muster bei Booten > 10 Jahre. Die Motorlager sinken unmerklich
ein (0,2–0,5 mm/Jahr), bis die Grenzwerte überschritten werden.
Jährliche Messuhr-Kontrolle ist die effektivste Präventivmaßnahme.

---

### ANHANG B — Fallstudie: PSS-Bellows gerissen auf Atlantiküberquerung

**Boot:** Oyster 53, Baujahr 2012
**Motor:** Yanmar 4JH110, 2.800 Betriebsstunden
**Wellenanlage:** Aquamet 22, 1-1/4" (32 mm), PSS 1-1/4"

**Situation:**
Tag 14 der Atlantiküberquerung (Las Palmas → Barbados). Boot unter
Segel, Motor aus. Eigner bemerkt bei Bilgenkontrolle ungewöhnlich
viel Wasser im Maschinenraum. Etwa 2 l/h.

**Diagnose:**
- PSS-Bellows: 15 cm langer Riss in Längsrichtung.
- Bellows-Alter: 9 Jahre (Herstellerempfehlung: 7 Jahre Austausch).
- Unter Segel drehte die Welle → Rotation vergrößerte den Riss.

**Sofortmaßnahme:**
1. Wellenbremse angezogen (Welle steht still).
2. Wassereinbruch reduziert sich von 2 l/h auf 0,5 l/h.
3. Gummi-Reparaturbandage (Rescue Tape) um den Bellows gewickelt.
4. Wassereinbruch → 0,1 l/h. Bilgepumpe bewältigt dies problemlos.
5. Restliche 800 sm unter Segel ohne Motor gefahren.

**Reparatur in Barbados:**
- Neuer Bellows: 120 EUR.
- Neuer Carbon-Ring (vorsorglich): 85 EUR.
- Arbeit (Selbsteinbau): 2 Stunden.
- Gesamtkosten: 205 EUR.

**Lehre:**
- Bellows nach 7 Jahren wechseln — unbedingt!
- Spare-Bellows an Bord (Langfahrt).
- Rescue Tape / Gummi-Reparaturbandage als Notfallmaterial.
- Wellenbremse ist doppelt wertvoll (weniger Rotation = weniger Leckage).

**AYDI-Bewertung:** Klassisches Versagen eines überalterten
PSS-Bellows. Prävention: 120 EUR alle 7 Jahre. Folgekosten bei
Versagen auf See: potenziell unberechenbar.

---

### ANHANG C — Fallstudie: Elektrolyse zerstört Propeller in 6 Wochen

**Boot:** Bavaria 40 Cruiser, Baujahr 2018
**Motor:** Volvo Penta D2-40, 600 Betriebsstunden
**Liegeplatz:** Marina (Mittelmeer), Landstrom dauerhaft angeschlossen

**Symptom:**
Propeller (3-Blatt Bronze, 2 Jahre alt) zeigt nach 6 Wochen
massives Pitting, raue rosa Oberfläche (De-Zinkung). Zinkanode
an der Welle komplett aufgelöst.

**Diagnose:**
1. Referenz-Elektrode ins Wasser: Spannung Welle → Referenz = +420 mV.
   → Massiver Streustrom!
2. Landstrom abgeklemmt: Spannung sinkt auf +80 mV. → Landstrom
   ist die Ursache.
3. Ursache: Nachbar-Boot mit defekter Landstrom-Verkabelung sendet
   Strom ins Wasser.

**Maßnahme:**
1. Hafenmeister informiert → Nachbar-Boot repariert seine Verkabelung.
2. Galvanic Isolator (Victron VDI-32) eingebaut: 280 EUR.
3. Propeller abgeschliffen, Opferanode erneuert: 150 EUR.
4. Monitoring mit Referenz-Elektrode: Spannung jetzt +30 mV (normal).

**Gesamtkosten:** 430 EUR (Glück gehabt — neuer Propeller wäre 1.800 EUR).

**AYDI-Bewertung:** Streustrom-Korrosion ist 10× aggressiver als
natürliche galvanische Korrosion. Ein Galvanic Isolator (200–500 EUR)
ist Pflicht bei dauerhaftem Landstromanschluss. Referenz-Elektrode
zur Überwachung empfohlen.

---

### ANHANG D — Fallstudie: Grundberührung mit Wellenverformung

**Boot:** Grand Soleil 46, Baujahr 2015
**Motor:** Yanmar 4JH80, 1.100 Betriebsstunden
**Wellenanlage:** Aquamet 22, 1-1/8" (29 mm)

**Situation:**
Grundberührung bei Ansteuerung Ankerbucht (Sand, 1,2 m Tiefe bei
1,8 m Tiefgang). Propellerblatt verbogen, Motor blockiert kurz.
Skipper fährt frei, Motor läuft wieder, aber mit deutlicher Vibration.

**Diagnose:**
1. Taucher: Propellerblatt Nr. 2 um 15° verbogen, Blatt Nr. 3 leicht.
2. Boot an Land:
   - Propeller: Blatt 2 verbogen, Blatt 3 leicht, Blatt 1 OK.
   - Welle: Schlag 0,18 mm (Grenzwert: 0,05 mm) → Welle verbogen!
   - P-Bracket: Haarriss am Befestigungsfuß (Farbeindringprüfung).
   - Cutless-Bearing: einseitig verschlissen (Folge der verbogenen Welle).
   - Motorausrichtung: TIR 0,22 mm (durch verbogene Welle).

**Reparatur:**
- Neue Propellerwelle Aquamet 22, 1-1/8", 2.200 mm: 1.400 EUR.
- P-Bracket-Schweißreparatur: 600 EUR.
- Neues Cutless-Bearing: 180 EUR.
- Propeller richten + auswuchten: 350 EUR.
- Motorausrichtung (Laser): 600 EUR.
- Arbeitszeit Werft (16 h × 110 EUR): 1.760 EUR.

**Gesamtkosten:** 4.890 EUR

**AYDI-Bewertung:** Grundberührung verursacht häufig verdeckte
Schäden (verbogene Welle, Mikrorisse am P-Bracket), die erst nach
Tagen oder Wochen als Vibration auffallen. Komplettinspektion nach
JEDER Grundberührung obligatorisch!

---

### ANHANG E — Fallstudie: Stopfbuchse überhitzt — Welle verfärbt

**Boot:** Dehler 38, Baujahr 2009
**Motor:** Volvo Penta D2-40, 1.800 Betriebsstunden

**Situation:**
Eigner (unerfahren) bemerkt Tropfen an der Stopfbuchse und zieht
die Muttern "richtig fest" an. Motor wird gestartet, 4-Stunden-Fahrt.
Danach: stechender Geruch im Maschinenraum, Welle im Dichtungsbereich
blau verfärbt.

**Diagnose:**
- Stopfbuchse: Packung verkohlt, schwarz, hart.
- Welle im Dichtungsbereich: Blau/Violett verfärbt (> 300 °C erreicht).
  Oberfläche rauh (Abrieb).
- Stevenrohr-Kunststoff im Dichtungsbereich angeschmolzen.

**Maßnahme:**
- Neue Packung: 15 EUR.
- Welle im Dichtungsbereich nachschleifen: 200 EUR (konnte
  gerettet werden, da Verfärbung nur oberflächlich).
- Neue Stopfbuchsen-Buchse (Stevenrohr-Innenende): 180 EUR.
- Arbeit: 4 h × 105 EUR = 420 EUR.

**Gesamtkosten:** 815 EUR

**AYDI-Bewertung:** NIEMALS eine Stopfbuchse so fest anziehen, dass
sie bei laufendem Motor nicht mehr tropft. 6–12 Tropfen/min bei
Fahrt sind korrekt und notwendig. Überhitzung kann zum Lösen der
Packung und unkontrolliertem Wassereinbruch führen.

---

### ANHANG F — Fallstudie: Falsches Anodenmaterial im Süßwasser

**Boot:** Beneteau Oceanis 40.1, Baujahr 2020
**Revier:** Bodensee (Süßwasser)

**Symptom:**
Nach 2 Jahren: Zinkanodon am Propeller und an der Welle nahezu
unverändert (kein Abtrag). Propeller zeigt jedoch Pitting und
grüne Flecken.

**Diagnose:**
- Zink-Anoden im Süßwasser sind NICHT wirksam (Schutzpotential
  reicht nicht aus).
- Propeller war ungeschützt → natürliche Korrosion.

**Maßnahme:**
- Zink-Anoden durch Magnesium-Anoden ersetzt: 40 EUR.
- Propeller abgeschliffen, poliert: 150 EUR.
- Nach 1 Jahr: Magnesium-Anode korrekt abgetragen (30 %),
  Propeller einwandfrei.

**AYDI-Bewertung:** Falsches Anodenmaterial ist ein häufiger Fehler.
Merksatz: Salz = Zink, Brack = Aluminium, Süß = Magnesium.
Ein Propeller-Satz (1.500–3.000 EUR) ist deutlich teurer als die
richtige Anode (20–40 EUR).

---

### ANHANG G — Fallstudie: Aquadrive eliminiert Vibrationsproblem

**Boot:** Moody 45 DS, Baujahr 2017
**Motor:** Volvo Penta D3-110, 1.400 Betriebsstunden
**Problem:** Trotz perfekter Motorausrichtung (Laser, TIR < 0,02 mm)
und neuem Propeller (augewuchtet) persistierende Vibration bei
2.200–2.600 U/min.

**Diagnose:**
- Resonanzanalyse: Eigenfrequenz der Wellenanlage bei 2.400 U/min.
- Welle schwingt in der 1. Eigenform (freie Länge 1.800 mm bei
  30 mm Durchmesser → knapp über Grenzwert).
- Motorschub wird direkt über die Motorlager in den Rumpf eingeleitet
  → Rumpf-Resonanz wird angeregt.

**Lösung:**
- Aquadrive-System (Kupplung + CVL-Lager) eingebaut: 1.800 EUR.
- Arbeit (Werft, 12 h): 1.320 EUR.
- Ergebnis: Vibration bei 2.200–2.600 U/min vollständig eliminiert.
  Gesamte Vibrationslevel um ca. 70 % reduziert.

**Gesamtkosten:** 3.120 EUR

**AYDI-Bewertung:** Aquadrive ist die Lösung für persistierende
Vibrationsprobleme, die nicht durch Ausrichtung, Propeller oder
Cutless-Bearing verursacht werden. Die Entkopplung des Propellerschubs
vom Motor ist besonders bei längeren Wellen und Rumpf-Resonanzen
wirksam.

---

### ANHANG H — Fallstudie: Saildrive-Manschette reißt im Winterlager

**Boot:** Jeanneau Sun Odyssey 349, Baujahr 2018
**Antrieb:** Yanmar 3YM20 mit Saildrive SD20

**Situation:**
Boot steht im Winterlager an Land. Beim Einwassern im Frühling:
Wasser im Maschinenraum. Bilgepumpe hält mit, aber Wassereinbruch
deutlich.

**Diagnose:**
- Saildrive-Manschette: Zwei Risse (je ca. 3 cm) an der Oberseite.
- Manschette-Alter: 8 Jahre (Volvo-Vorschrift: 7 Jahre Wechsel).
- Ursache: Gummi-Alterung + Winterfrost (Restwasser in der Falte
  gefroren → Riss).

**Maßnahme:**
- Boot sofort wieder aus dem Wasser.
- Neue Manschette (Volvo 3842630): 95 EUR.
- Neuer Spannring: 35 EUR.
- Arbeit (2 h): 220 EUR.

**Gesamtkosten:** 350 EUR

**Lehre:**
- Saildrive-Manschette nach 7 Jahren wechseln — immer!
- Vor dem Einwassern: Manschette visuell prüfen (auch wenn < 7 Jahre).
- Im Winterlager: Restwasser an der Manschette abtropfen lassen.

**AYDI-Bewertung:** Die Saildrive-Manschette ist eine der am häufigsten
vernachlässigten Wartungspositionen. 350 EUR alle 7 Jahre vs. potenzielles
Sinken bei Versagen auf See.

> ⚠️ **ZU PRÜFEN (Audit):** Diese Fallstudie betrifft einen **Yanmar** SD20, referenziert aber die **Volvo**-Vorschrift ("7 Jahre Wechsel") und die **Volvo**-Teilenummer **3842630** (95 EUR). Beides gehört zum Volvo-, nicht zum Yanmar-Antrieb — eine Yanmar-SD20-Manschette hat eine eigene Yanmar-Teilenummer, und Yanmars Intervall liegt bei ≈ 5–7 Jahren (nicht bei den 10 Jahren aus §14.5). Norm-/Teilenummer-Zuordnung dieser Fallstudie: unverifiziert.

---
---

## 21. ANHANG I–R: Pydantic v2 Datenmodelle

### ANHANG I — ShaftMaterial (Enum)

```python
from enum import Enum


class ShaftMaterial(str, Enum):
    """Propellerwellen-Material."""
    AQUAMET_22 = "aquamet_22"
    AQUAMET_17 = "aquamet_17"
    AQUAMET_18 = "aquamet_18"
    AQUALOY_22 = "aqualoy_22"
    AISI_316L = "aisi_316l"
    AISI_304 = "aisi_304"
    MONEL_K500 = "monel_k500"
    MONEL_400 = "monel_400"
    TOBIN_BRONZE = "tobin_bronze"
    NITRONIC_50 = "nitronic_50"
    UNKNOWN = "unknown"
```

### ANHANG J — SealType (Enum)

```python
class SealType(str, Enum):
    """Wellendichtungs-Typ."""
    STUFFING_BOX = "stuffing_box"
    PSS_PYI = "pss_pyi"
    TIDES_SURESEAL = "tides_sureseal"
    VOLVO_SHAFT_SEAL = "volvo_shaft_seal"
    DEEP_SEA_SEAL = "deep_sea_seal"
    SKF_SIMPLEX = "skf_simplex"
    OTHER_LIP_SEAL = "other_lip_seal"
    UNKNOWN = "unknown"
```

### ANHANG K — CouplingType (Enum)

```python
class CouplingType(str, Enum):
    """Kupplungs-Typ."""
    RD_MARINE_FLEXOFOLD = "rd_marine_flexofold"
    VETUS_BULLFLEX = "vetus_bullflex"
    PYI_PYIDRIVE = "pyi_pyidrive"
    CENTAFLEX = "centaflex"
    AQUADRIVE = "aquadrive"
    CENTA = "centa"
    RIGID_FLANGE = "rigid_flange"
    OTHER = "other"
    UNKNOWN = "unknown"
```

### ANHANG L — BearingType (Enum)

```python
class BearingType(str, Enum):
    """Cutless-Bearing-Typ."""
    JOHNSON_DURAMAX_100 = "johnson_duramax_100"
    JOHNSON_DURAMAX_200 = "johnson_duramax_200"
    JOHNSON_DURAMAX_400 = "johnson_duramax_400"
    MORSE_STANDARD = "morse_standard"
    MORSE_NON_METALLIC = "morse_non_metallic"
    THORDON_SXL = "thordon_sxl"
    THORDON_COMPAC = "thordon_compac"
    VESCONITE = "vesconite"
    OTHER = "other"
    UNKNOWN = "unknown"
```

### ANHANG M — ShaftSystemCondition (Enum)

```python
class ShaftSystemCondition(str, Enum):
    """Gesamtzustand der Wellenanlage."""
    EXCELLENT = "excellent"       # Neuwertig oder kürzlich überholt
    GOOD = "good"                 # Normaler Verschleiß, voll funktionsfähig
    FAIR = "fair"                 # Erhöhter Verschleiß, Wartung empfohlen
    POOR = "poor"                 # Starker Verschleiß, Reparatur nötig
    CRITICAL = "critical"         # Sicherheitsrelevant, sofortige Maßnahme
    UNKNOWN = "unknown"           # Nicht beurteilbar
```

### ANHANG N — ShaftAssessment

```python
from pydantic import BaseModel, Field
from typing import Optional


class ShaftAssessment(BaseModel):
    """
    Bewertung der Propellerwelle.
    Umfasst Material, Zustand, Oberfläche und Maße.
    """
    model_config = {"from_attributes": True}

    # Identifikation
    shaft_material: ShaftMaterial = Field(
        ..., description="Wellenmaterial"
    )
    shaft_diameter_mm: float = Field(
        ..., gt=0, le=200, description="Wellendurchmesser (mm)"
    )
    shaft_diameter_inch: Optional[str] = Field(
        None, description="Wellendurchmesser (Zoll, z.B. '1-1/4\"')"
    )
    shaft_length_mm: Optional[float] = Field(
        None, gt=0, description="Wellenlänge (mm)"
    )
    free_span_mm: Optional[float] = Field(
        None, gt=0,
        description="Freie Wellenlänge ohne Zwischenlager (mm)"
    )
    age_years: Optional[float] = Field(
        None, ge=0, description="Alter der Welle (Jahre)"
    )

    # Konus und Passfeder
    taper_type: Optional[str] = Field(
        None, description="SAE-Konus-Typ (z.B. '#3', '#5')"
    )
    taper_contact_percent: Optional[float] = Field(
        None, ge=0, le=100,
        description="Konus-Kontaktfläche (Bluing-Test, %)"
    )
    keyway_condition: Optional[str] = Field(
        None,
        description="Passfedernut-Zustand: good, worn, damaged, corroded"
    )
    key_material: Optional[str] = Field(
        None, description="Passfeder-Material: stainless, bronze, brass"
    )

    # Oberfläche
    seal_area_roughness_ra: Optional[float] = Field(
        None, ge=0, le=10,
        description="Rauheit im Dichtungsbereich (Ra, µm)"
    )
    bearing_area_roughness_ra: Optional[float] = Field(
        None, ge=0, le=10,
        description="Rauheit im Lagerbereich (Ra, µm)"
    )
    scoring_depth_mm: Optional[float] = Field(
        None, ge=0,
        description="Tiefe der tiefsten Rille (mm)"
    )
    has_repair_sleeve: bool = Field(
        False, description="Repair-Hülse vorhanden"
    )

    # Korrosion
    corrosion_type: Optional[str] = Field(
        None,
        description="Korrosionstyp: none, galvanic, stray_current, "
                     "crevice, pitting, biological"
    )
    corrosion_severity: Optional[str] = Field(
        None,
        description="Korrosionsschwere: none, minor, moderate, severe"
    )
    pitting_max_depth_mm: Optional[float] = Field(
        None, ge=0, description="Max. Pitting-Tiefe (mm)"
    )

    # Wellenschlag (Runout)
    runout_mm: Optional[float] = Field(
        None, ge=0,
        description="Gemessener Wellenschlag (mm)"
    )
    max_runout_mm: Optional[float] = Field(
        None, ge=0,
        description="Maximal zulässiger Wellenschlag (mm)"
    )

    # Bewertung
    condition: ShaftSystemCondition = Field(
        ..., description="Zustand der Welle"
    )
    score: float = Field(
        ..., ge=0, le=100, description="Bewertung (0–100)"
    )
    confidence: str = Field(
        ..., description="Konfidenzstufe"
    )

    findings: list[str] = Field(
        default_factory=list, description="Befunde"
    )
    recommendations: list[str] = Field(
        default_factory=list, description="Empfehlungen"
    )
    estimated_remaining_life_years: Optional[float] = Field(
        None, ge=0,
        description="Geschätzte Restlebensdauer (Jahre)"
    )
    replacement_cost_eur: Optional[float] = Field(
        None, ge=0, description="Geschätzte Austauschkosten (EUR)"
    )
```

### ANHANG O — SealAssessment

```python
class SealAssessment(BaseModel):
    """
    Bewertung der Wellendichtung (Stopfbuchse, PSS, oder andere).
    """
    model_config = {"from_attributes": True}

    # Identifikation
    seal_type: SealType = Field(
        ..., description="Dichtungstyp"
    )
    seal_brand: Optional[str] = Field(
        None, description="Hersteller/Marke"
    )
    seal_model: Optional[str] = Field(
        None, description="Modell"
    )
    age_years: Optional[float] = Field(
        None, ge=0, description="Alter der Dichtung (Jahre)"
    )

    # Stopfbuchsen-spezifisch
    packing_material: Optional[str] = Field(
        None,
        description="Packungsmaterial: ptfe_graphite, ptfe_aramid, "
                     "flax_tallow, gfo_gore, graphite, cotton_wax"
    )
    packing_age_years: Optional[float] = Field(
        None, ge=0, description="Alter der Packung (Jahre)"
    )
    drip_rate_idle: Optional[int] = Field(
        None, ge=0,
        description="Tropfrate bei Leerlauf (Tropfen/min)"
    )
    drip_rate_cruise: Optional[int] = Field(
        None, ge=0,
        description="Tropfrate bei Marschfahrt (Tropfen/min)"
    )
    drip_rate_full: Optional[int] = Field(
        None, ge=0,
        description="Tropfrate bei Vollgas (Tropfen/min)"
    )
    gland_adjustable: Optional[bool] = Field(
        None, description="Muttern noch verstellbar"
    )
    shaft_scoring_in_seal_area: Optional[bool] = Field(
        None, description="Rillen im Dichtungsbereich"
    )

    # PSS/Dripless-spezifisch
    bellows_condition: Optional[str] = Field(
        None,
        description="Bellows-Zustand: good, hairline_cracks, cracked, "
                     "brittle, swollen, torn"
    )
    bellows_age_years: Optional[float] = Field(
        None, ge=0, description="Bellows-Alter (Jahre)"
    )
    carbon_ring_wear_mm: Optional[float] = Field(
        None, ge=0,
        description="Carbon-Ring-Verschleiß (mm)"
    )
    rotor_condition: Optional[str] = Field(
        None,
        description="Rotor-Zustand: good, minor_scoring, scored, "
                     "grooved, corroded"
    )
    water_supply_present: Optional[bool] = Field(
        None, description="Wasserversorgung vorhanden und funktionsfähig"
    )
    hose_clamps_condition: Optional[str] = Field(
        None,
        description="Schlauchschellen-Zustand: good, surface_rust, "
                     "loose, corroded"
    )

    # Leckage
    leak_detected: bool = Field(
        False, description="Leckage festgestellt (über Normalmaß)"
    )
    leak_rate_description: Optional[str] = Field(
        None,
        description="Leckage-Beschreibung: none, drip, trickle, stream"
    )

    # Bewertung
    condition: ShaftSystemCondition = Field(
        ..., description="Gesamtzustand der Dichtung"
    )
    score: float = Field(
        ..., ge=0, le=100, description="Bewertung (0–100)"
    )
    confidence: str = Field(
        ..., description="Konfidenzstufe"
    )
    is_critical: bool = Field(
        False,
        description="KRITISCHER Befund (Wassereinbruch-Risiko)"
    )

    findings: list[str] = Field(
        default_factory=list, description="Befunde"
    )
    recommendations: list[str] = Field(
        default_factory=list, description="Empfehlungen"
    )
    estimated_remaining_life_years: Optional[float] = Field(
        None, ge=0,
        description="Geschätzte Restlebensdauer (Jahre)"
    )
    replacement_cost_eur: Optional[float] = Field(
        None, ge=0,
        description="Geschätzte Austauschkosten (EUR)"
    )
```

### ANHANG P — CutlessBearingAssessment

```python
class CutlessBearingAssessment(BaseModel):
    """
    Bewertung des Cutless-Bearings (Wellenlager).
    """
    model_config = {"from_attributes": True}

    # Identifikation
    bearing_type: BearingType = Field(
        ..., description="Bearing-Typ/Hersteller"
    )
    bearing_shell_material: Optional[str] = Field(
        None,
        description="Hülsenmaterial: bronze, nylon, gfk, polymer"
    )
    inner_material: Optional[str] = Field(
        None,
        description="Innenmaterial: nitrile_rubber, uhmwpe, vesconite"
    )
    age_years: Optional[float] = Field(
        None, ge=0, description="Alter (Jahre)"
    )
    operating_hours: Optional[int] = Field(
        None, ge=0, description="Betriebsstunden seit Einbau"
    )

    # Verschleiß
    play_mm: Optional[float] = Field(
        None, ge=0,
        description="Gemessenes Spiel (mm)"
    )
    max_play_mm: Optional[float] = Field(
        None, ge=0,
        description="Maximal zulässiges Spiel (mm)"
    )
    groove_remaining_depth_mm: Optional[float] = Field(
        None, ge=0,
        description="Resttiefe der Wasserrillen (mm)"
    )
    wear_pattern: Optional[str] = Field(
        None,
        description="Verschleißmuster: even, uneven_top, "
                     "uneven_bottom, uneven_side"
    )
    rubber_condition: Optional[str] = Field(
        None,
        description="Gummizustand: good, worn, cracked, detaching, "
                     "melted, missing_sections"
    )

    # Lubrication
    lubrication_type: Optional[str] = Field(
        None,
        description="Schmierung: water, grease, oil"
    )
    water_flow_adequate: Optional[bool] = Field(
        None,
        description="Wasserdurchfluss ausreichend"
    )

    # Bewertung
    condition: ShaftSystemCondition = Field(
        ..., description="Gesamtzustand"
    )
    score: float = Field(
        ..., ge=0, le=100, description="Bewertung (0–100)"
    )
    confidence: str = Field(
        ..., description="Konfidenzstufe"
    )

    findings: list[str] = Field(
        default_factory=list, description="Befunde"
    )
    recommendations: list[str] = Field(
        default_factory=list, description="Empfehlungen"
    )
    estimated_remaining_life_years: Optional[float] = Field(
        None, ge=0,
        description="Geschätzte Restlebensdauer (Jahre)"
    )
    replacement_cost_eur: Optional[float] = Field(
        None, ge=0,
        description="Geschätzte Austauschkosten (EUR)"
    )
```

### ANHANG Q — CouplingAssessment

```python
class CouplingAssessment(BaseModel):
    """
    Bewertung der flexiblen Kupplung.
    """
    model_config = {"from_attributes": True}

    # Identifikation
    coupling_type: CouplingType = Field(
        ..., description="Kupplungstyp"
    )
    coupling_brand: Optional[str] = Field(
        None, description="Hersteller"
    )
    coupling_model: Optional[str] = Field(
        None, description="Modell"
    )
    age_years: Optional[float] = Field(
        None, ge=0, description="Alter (Jahre)"
    )
    operating_hours: Optional[int] = Field(
        None, ge=0, description="Betriebsstunden seit Einbau"
    )

    # Elastomer / Kupplung
    elastomer_condition: Optional[str] = Field(
        None,
        description="Elastomer-Zustand: good, hairline_cracks, "
                     "cracked, hardened, swollen, disintegrating, "
                     "oil_contaminated"
    )
    play_degrees: Optional[float] = Field(
        None, ge=0, le=30,
        description="Drehspiel (Grad)"
    )
    debris_present: bool = Field(
        False,
        description="Gummiabrieb unter der Kupplung sichtbar"
    )
    bolts_condition: Optional[str] = Field(
        None,
        description="Schrauben-Zustand: good, corroded, loose"
    )

    # Aquadrive-spezifisch
    cvl_bearing_condition: Optional[str] = Field(
        None,
        description="CVL-Lager-Zustand (Aquadrive): good, noisy, "
                     "play, stiff"
    )
    cvl_greased: Optional[bool] = Field(
        None, description="CVL-Lager geschmiert"
    )

    # Bewertung
    condition: ShaftSystemCondition = Field(
        ..., description="Gesamtzustand"
    )
    score: float = Field(
        ..., ge=0, le=100, description="Bewertung (0–100)"
    )
    confidence: str = Field(
        ..., description="Konfidenzstufe"
    )

    findings: list[str] = Field(
        default_factory=list, description="Befunde"
    )
    recommendations: list[str] = Field(
        default_factory=list, description="Empfehlungen"
    )
    estimated_remaining_life_years: Optional[float] = Field(
        None, ge=0,
        description="Geschätzte Restlebensdauer (Jahre)"
    )
    replacement_cost_eur: Optional[float] = Field(
        None, ge=0,
        description="Geschätzte Austauschkosten (EUR)"
    )
```

### ANHANG R — ShaftSystemOverallAssessment

```python
class AlignmentAssessment(BaseModel):
    """
    Bewertung der Motorausrichtung.
    """
    model_config = {"from_attributes": True}

    method: Optional[str] = Field(
        None,
        description="Ausrichtungsmethode: feeler_gauge, dial_gauge, "
                     "laser, string, unknown"
    )
    parallel_offset_mm: Optional[float] = Field(
        None, ge=0,
        description="Gemessener Parallelversatz (mm)"
    )
    angular_offset_mm_per_100mm: Optional[float] = Field(
        None, ge=0,
        description="Gemessener Winkelversatz (mm/100mm)"
    )
    tir_mm: Optional[float] = Field(
        None, ge=0,
        description="Total Indicator Reading (mm)"
    )
    within_tolerance: Optional[bool] = Field(
        None,
        description="Innerhalb der Toleranz"
    )
    last_alignment_date: Optional[str] = Field(
        None, description="Datum der letzten Ausrichtung (ISO 8601)"
    )
    motor_mount_condition: Optional[str] = Field(
        None,
        description="Motorlager-Zustand: good, soft, sagging, "
                     "cracked, oil_soaked"
    )
    motor_mount_age_years: Optional[float] = Field(
        None, ge=0, description="Motorlager-Alter (Jahre)"
    )

    # Bewertung
    condition: ShaftSystemCondition = Field(
        ..., description="Ausrichtungs-Zustand"
    )
    score: float = Field(
        ..., ge=0, le=100, description="Bewertung (0–100)"
    )
    confidence: str = Field(
        ..., description="Konfidenzstufe"
    )
    findings: list[str] = Field(
        default_factory=list, description="Befunde"
    )
    recommendations: list[str] = Field(
        default_factory=list, description="Empfehlungen"
    )


class PBracketAssessment(BaseModel):
    """
    Bewertung des P-Brackets / Struts.
    """
    model_config = {"from_attributes": True}

    bracket_type: Optional[str] = Field(
        None,
        description="Bracket-Typ: p_bracket, a_bracket, v_strut, "
                     "i_strut, none"
    )
    material: Optional[str] = Field(
        None,
        description="Material: bronze, stainless_316l, aluminum, gfk"
    )
    age_years: Optional[float] = Field(
        None, ge=0, description="Alter (Jahre)"
    )

    # Zustand
    cracks_detected: bool = Field(
        False, description="Risse festgestellt"
    )
    crack_location: Optional[str] = Field(
        None,
        description="Rissposition: foot, transition, weld, bearing_housing"
    )
    crack_length_mm: Optional[float] = Field(
        None, ge=0, description="Risslänge (mm)"
    )
    corrosion_severity: Optional[str] = Field(
        None,
        description="Korrosion: none, surface, moderate, severe"
    )
    mounting_bolts_condition: Optional[str] = Field(
        None,
        description="Befestigungs-Bolzen: good, corroded, loose"
    )
    bearing_housing_condition: Optional[str] = Field(
        None,
        description="Lagergehäuse: good, worn, cracked, corroded"
    )

    # Bewertung
    condition: ShaftSystemCondition = Field(
        ..., description="Gesamtzustand"
    )
    score: float = Field(
        ..., ge=0, le=100, description="Bewertung (0–100)"
    )
    confidence: str = Field(
        ..., description="Konfidenzstufe"
    )
    is_critical: bool = Field(
        False, description="KRITISCHER Befund"
    )

    findings: list[str] = Field(
        default_factory=list, description="Befunde"
    )
    recommendations: list[str] = Field(
        default_factory=list, description="Empfehlungen"
    )
    replacement_cost_eur: Optional[float] = Field(
        None, ge=0, description="Geschätzte Austauschkosten (EUR)"
    )


class GalvanicProtectionAssessment(BaseModel):
    """
    Bewertung des galvanischen Schutzes der Wellenanlage.
    """
    model_config = {"from_attributes": True}

    # Anoden
    anode_material: Optional[str] = Field(
        None,
        description="Anodenmaterial: zinc, aluminum, magnesium, none"
    )
    anode_material_correct_for_water: Optional[bool] = Field(
        None,
        description="Anodenmaterial passend zum Revier"
    )
    shaft_anode_remaining_percent: Optional[float] = Field(
        None, ge=0, le=100,
        description="Wellenanoden-Restmaterial (%)"
    )
    prop_anode_remaining_percent: Optional[float] = Field(
        None, ge=0, le=100,
        description="Propeller-Anoden-Restmaterial (%)"
    )
    anode_electrical_contact: Optional[bool] = Field(
        None,
        description="Elektrischer Kontakt Anode ↔ Welle vorhanden"
    )

    # Bonding
    bonding_system_present: Optional[bool] = Field(
        None,
        description="Bonding-System vorhanden"
    )
    bonding_system_intact: Optional[bool] = Field(
        None,
        description="Bonding-System intakt (alle Verbindungen)"
    )

    # Streustrom
    stray_current_detected: Optional[bool] = Field(
        None,
        description="Streustrom-Korrosion erkannt"
    )
    reference_electrode_voltage_mv: Optional[float] = Field(
        None,
        description="Spannung Welle ↔ Referenz-Elektrode (mV)"
    )
    galvanic_isolator_present: Optional[bool] = Field(
        None,
        description="Galvanic Isolator eingebaut"
    )
    isolation_transformer_present: Optional[bool] = Field(
        None,
        description="Isolation Transformer eingebaut"
    )

    # Bewertung
    condition: ShaftSystemCondition = Field(
        ..., description="Gesamtzustand galvanischer Schutz"
    )
    score: float = Field(
        ..., ge=0, le=100, description="Bewertung (0–100)"
    )
    confidence: str = Field(
        ..., description="Konfidenzstufe"
    )

    findings: list[str] = Field(
        default_factory=list, description="Befunde"
    )
    recommendations: list[str] = Field(
        default_factory=list, description="Empfehlungen"
    )


class ShaftSystemOverallAssessment(BaseModel):
    """
    Gesamtbewertung der Wellenanlage.
    Kombiniert alle Teilbewertungen zu einem Gesamtbild.
    """
    model_config = {"from_attributes": True}

    # Identifikation
    boat_name: Optional[str] = Field(
        None, description="Bootsname"
    )
    boat_type: Optional[str] = Field(
        None, description="Bootstyp"
    )
    boat_length_m: Optional[float] = Field(
        None, gt=0, le=100, description="Bootslänge (m)"
    )
    engine_power_kw: Optional[float] = Field(
        None, gt=0, description="Motorleistung (kW)"
    )
    engine_power_ps: Optional[float] = Field(
        None, gt=0, description="Motorleistung (PS)"
    )
    drive_type: Optional[str] = Field(
        None,
        description="Antriebstyp: shaft_drive, saildrive, outboard, "
                     "pod_drive, jet_drive"
    )

    # Teilbewertungen
    shaft: Optional[ShaftAssessment] = Field(
        None, description="Wellen-Bewertung"
    )
    seal: Optional[SealAssessment] = Field(
        None, description="Dichtungs-Bewertung"
    )
    cutless_bearing: Optional[CutlessBearingAssessment] = Field(
        None, description="Cutless-Bearing-Bewertung"
    )
    coupling: Optional[CouplingAssessment] = Field(
        None, description="Kupplungs-Bewertung"
    )
    alignment: Optional[AlignmentAssessment] = Field(
        None, description="Ausrichtungs-Bewertung"
    )
    p_bracket: Optional[PBracketAssessment] = Field(
        None, description="P-Bracket-Bewertung"
    )
    galvanic_protection: Optional[GalvanicProtectionAssessment] = Field(
        None, description="Galvanischer-Schutz-Bewertung"
    )

    # Vibration
    vibration_detected: Optional[bool] = Field(
        None, description="Vibration festgestellt"
    )
    vibration_severity: Optional[str] = Field(
        None,
        description="Vibrationsschwere: none, slight, moderate, "
                     "severe, dangerous"
    )
    vibration_rpm_range: Optional[str] = Field(
        None,
        description="Drehzahlbereich der Vibration (z.B. '2000-2500')"
    )

    # Wellenbremse
    shaft_brake_present: Optional[bool] = Field(
        None, description="Wellenbremse vorhanden"
    )
    shaft_brake_condition: Optional[str] = Field(
        None,
        description="Wellenbremsen-Zustand: good, worn, seized, "
                     "cable_broken, not_present"
    )

    # Gesamtergebnis
    overall_score: float = Field(
        ..., ge=0, le=100,
        description="Gesamtbewertung Wellenanlage (0–100)"
    )
    overall_condition: ShaftSystemCondition = Field(
        ..., description="Gesamtzustand"
    )

    # Gewichtete Teilbewertungen
    sub_scores: dict[str, float] = Field(
        default_factory=dict,
        description="Teilbewertungen (z.B. {'shaft': 85, 'seal': 72, "
                     "'cutless': 90, 'alignment': 65})"
    )

    # Zusammenfassung
    summary_de: str = Field(
        ..., description="Zusammenfassung in Deutsch"
    )
    critical_findings: list[str] = Field(
        default_factory=list,
        description="Kritische Befunde (sofortige Maßnahme nötig)"
    )
    all_findings: list[str] = Field(
        default_factory=list,
        description="Alle Befunde"
    )
    all_recommendations: list[str] = Field(
        default_factory=list,
        description="Alle Empfehlungen"
    )

    # Kostenschätzung
    estimated_immediate_cost_eur: Optional[float] = Field(
        None, ge=0,
        description="Sofortige Kosten für notwendige Maßnahmen (EUR)"
    )
    estimated_annual_maintenance_cost_eur: Optional[float] = Field(
        None, ge=0,
        description="Geschätzte jährliche Wartungskosten (EUR)"
    )
    estimated_5year_cost_eur: Optional[float] = Field(
        None, ge=0,
        description="Geschätzte 5-Jahres-Kosten inkl. Austausch (EUR)"
    )

    # Metadaten
    confidence: str = Field(
        ..., description="Gesamt-Konfidenzstufe"
    )
    data_sources: list[str] = Field(
        default_factory=list,
        description="Verwendete Datenquellen (structured, visual, text)"
    )
    model_version: str = Field(
        ..., description="AYDI-Modellversion"
    )
