# 23.05 — Instrumente und Sensoren im Yachtbau: Vollständige Wissensreferenz

> **AYDI Wissensdatei 23.05** — Kategorie 23: Bordelektronik und Navigation
> **Confidence-Quelle:** measured (Hersteller-Datenblätter), documented (Installationshandbücher, Praxisberichte), estimated (Erfahrungswerte)
> **Letzte Aktualisierung:** 2026-05-13

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
11. [ANHANG A–H — Fallstudien](#anhang-a--fallstudien)
12. [ANHANG I–R — Pydantic v2 Modelle](#anhang-i--pydantic-v2-modelle)

---

## 1. Einführung und Übersicht

### 1.1 Bedeutung der Bordsensorik

Instrumente und Sensoren bilden das Nervensystem einer jeden Yacht. Sie liefern die Daten, die für sichere Navigation, effizientes Segeln, vorausschauende Wartung und komfortablen Bordaufenthalt unverzichtbar sind. Ohne zuverlässige Sensorik operiert ein Skipper blind — Windstärke, Wassertiefe, Geschwindigkeit und Tankniveau werden zu Schätzwerten mit potentiell gefährlichen Konsequenzen.

**Warum Sensorik über Leben und Tod entscheiden kann:**
- Ein defekter Echolotgeber auf einer Küstenfahrt führt zur Grundberührung
- Ein falsch kalibrierter Windmesser verhindert rechtzeitige Segelreduzierung bei aufkommendem Sturm
- Ein ausgefallener Barograph verschleiert den Druckfall vor einer Kaltfront
- Ein ungenauer Tankgeber suggeriert ausreichend Kraftstoff für die Überfahrt

**Instrumentierung nach CE-Designkategorie:**

| Kategorie | Mindestausrüstung | Empfohlene Zusatzsensorik |
|-----------|-------------------|---------------------------|
| A (Ozean) | Kompass, Log, Lot, Barometer, Windmesser | AIS, Radar, Satellitenkompass, Langzeit-Barograph |
| B (Offshore) | Kompass, Log, Lot, Barometer, Windmesser | AIS, optionaler Radarreflektor, Windprozessor |
| C (Küstennahe) | Kompass, Log, Lot | Windmesser empfohlen, einfacher Barograph |
| D (Geschützt) | Kompass | Log und Lot empfohlen |

### 1.2 Entwicklungsgeschichte

**Vor 1960 — Ära der mechanischen Instrumente:**
Die klassische Yachtinstrumentierung bestand aus mechanischen Geräten: Walker-Patent-Log (Schlepplogge), Handlot mit Bleigewicht und Talg, Kompensierter Magnetkompass und Aneroid-Barometer. Diese Instrumente erforderten keinerlei Strom und waren prinzipiell unzerstörbar, lieferten aber nur punktuelle Messwerte.

**1960–1980 — Erste elektronische Instrumente:**
Brookes & Gatehouse (B&G) brachte 1960 das erste elektronische Bootsinstrument auf den Markt — den „Heron" Fahrtmesser mit Paddle-Wheel-Geber. VDO Marine und Signet folgten mit einfachen analogen Anzeigen. Die Messwerte waren zwar elektronisch erfasst, aber jeder Sensor hatte seine eigene Anzeige und eigene Verkabelung.

**1980–1995 — Bus-Systeme und Multiplex:**
Die Einführung von NMEA 0183 (1983) ermöglichte erstmals die Kommunikation zwischen Geräten verschiedener Hersteller. Seatalk (Raytheon/Raymarine, 1989) und FastNet (B&G) schufen proprietäre Hochgeschwindigkeitsbusse. Die Datenfusion — etwa die Berechnung wahrer Windwerte aus scheinbarem Wind, Geschwindigkeit und Kurs — wurde zum Standard.

**1995–2010 — Digitalisierung und Integration:**
NMEA 2000 (ab 2001) brachte den CAN-Bus in die Marineelektronik. Farbdisplays, Touchscreens und Multifunktionsdisplays (MFD) ersetzten zunehmend Einzelinstrumente. Die Vernetzung aller Sensoren über ein gemeinsames Backbone wurde zum Industriestandard.

**2010–heute — WiFi, Cloud und IoT:**
Drahtlose Sensoren (B&G WS320, Garmin gWind Wireless), Tablet-Integration, Cloud-Datenlogging und KI-gestützte Analyse erweitern die Instrumentierung über den klassischen Rahmen hinaus. Sensoren kommunizieren via WiFi, Bluetooth und proprietären Funkprotokollen.

### 1.3 Klassifizierung der Bordsensorik

**Nach Messdomäne:**

| Domäne | Sensoren | Kritikalität |
|--------|----------|-------------|
| Meteorologisch | Windmesser, Barometer, Thermometer, Hygrometer | Sicherheit + Performance |
| Hydrographisch | Echolot, Wassertemperatur, Strömungssensor | Sicherheit |
| Kinematisch | Log (STW/SOG), GPS, Kompass, Neigungssensor, Gyroskop | Navigation + Performance |
| Systemüberwachung | Tankgeber, Motordrehzahl, Batteriemonitor, Temperatur | Betriebssicherheit |
| Strukturell | Mastbiegung, Wantspannung, Ruderlage | Performance (Regatta) |

**Nach Installationsart:**

| Art | Beschreibung | Beispiele |
|-----|-------------|-----------|
| Masttop | Am Masttopp montiert | Windgeber, Antennen |
| Durchbruch | Durch den Rumpf | Lot-Geber, Log-Geber, Wassertemp. |
| Innenanliegend | Ohne Rumpfdurchbruch | Ultraschall-Lot, Neigungssensor |
| Deck-montiert | Auf Deck geschraubt | GPS-Antenne, Satellitenkompass |
| Konsole | Im Cockpit/Steuerstand | Displays, Bedieneinheiten |
| Motor-montiert | Am oder im Motor | Drehzahlgeber, Öldrucksensor |

### 1.4 AYDI-Relevanz

Die Instrumentierung einer Yacht ist ein zentraler Bewertungsfaktor in der AYDI-Analyse:

- **Sicherheitsbewertung**: Vorhandensein und Zustand sicherheitsrelevanter Sensoren
- **Performance-Bewertung**: Qualität der Segeldaten-Erfassung
- **Modernisierungsgrad**: Alter und Technologiestand der Instrumentierung
- **Integrationsniveau**: Vernetzung der Sensoren, NMEA-2000-Backbone
- **Wartungszustand**: Kalibrierstatus, bekannte Fehlerbilder
- **Nachrüstpotential**: Möglichkeit zur Aufrüstung ohne Struktureingriffe

---

## 2. Grundlagen und Theorie

### 2.1 Windmessung

#### 2.1.1 Anemometer — Prinzipien der Windgeschwindigkeitsmessung

**Schalenkreuz-Anemometer (Cup Anemometer):**
Das klassische Schalenkreuz mit drei oder vier Halbkugelschalen auf Armen rotiert unter Windeinwirkung. Die Rotationsfrequenz ist proportional zur Windgeschwindigkeit. Magnetische oder optische Impulsgeber wandeln die Drehzahl in ein elektrisches Signal.

- **Messbereich**: typisch 0–70 kn (0–130 km/h)
- **Auflösung**: 0,1 kn
- **Anlaufgeschwindigkeit**: 1,5–3 kn (je nach Lagerqualität)
- **Trägheit**: mittel — bei Böen 1–2 Sekunden Verzögerung
- **Lebensdauer Lager**: 5.000–15.000 Betriebsstunden (kugellager), 20.000+ (Gleitlager)
- **Einsatz**: Standard auf Fahrtenyachten, Wetterstationen

**Flügelrad-Anemometer (Vane Anemometer):**
Ein kleiner Propeller richtet sich in den Wind aus und dreht sich proportional zur Windgeschwindigkeit. Seltener auf Yachten, häufiger als Handinstrument.

- **Messbereich**: 0,5–50 kn
- **Auflösung**: 0,1 kn
- **Vorteil**: geringere Trägheit als Schalenkreuz
- **Nachteil**: muss exakt in den Wind ausgerichtet sein

**Ultraschall-Anemometer:**
Zwei oder mehr Ultraschall-Transducer-Paare messen die Laufzeitdifferenz von Schallpulsen in und gegen die Windrichtung. Die Windgeschwindigkeit ergibt sich aus:

```
v_wind = (L / 2) × (1/t_downwind - 1/t_upwind)

L = Abstand der Transducer [m]
t_downwind = Laufzeit mit Wind [s]
t_upwind = Laufzeit gegen Wind [s]
```

- **Messbereich**: 0–100 kn (manche Modelle bis 150 kn)
- **Auflösung**: 0,01 kn
- **Anlaufgeschwindigkeit**: 0 kn (keine beweglichen Teile)
- **Trägheit**: minimal — Abtastrate bis 20 Hz
- **Genauigkeit**: ±0,5 kn oder ±2 %, je nachdem was größer ist
- **Lebensdauer**: 10+ Jahre bei Marine-Ausführung (keine Verschleißteile)
- **Einsatz**: Regattayachten, Superyachten, moderne Fahrtenyachten
- **Modelle**: B&G WS320 (drahtlos), Calypso ULP, Airmar 220WX, LCJ Capteurs CV7

**Heißdraht-Anemometer:**
In der Yachtpraxis ohne Bedeutung — zu empfindlich gegenüber Salz und Feuchtigkeit.

#### 2.1.2 Windfahne — Windrichtungsmessung

**Mechanische Windfahne (Vane):**
Eine drehbar gelagerte Fahne richtet sich in den Wind. Die Winkelposition wird über ein Potentiometer, einen induktiven Geber (Synchro/Resolver) oder einen optischen Encoder in ein elektrisches Signal gewandelt.

- **Auflösung**: 1° (Potentiometer), 0,5° (Resolver), 0,1° (Encoder)
- **Anlaufempfindlichkeit**: ab 2–4 kn
- **Hysterese**: ±2° (Potentiometer), ±1° (Resolver)
- **Typische Fehler**: Potentiometer-Abrieb, Lager-Korrosion, Fahnenbruch

**Ultraschall-Windrichtung:**
Bei Ultraschall-Anemometern wird die Windrichtung simultan mit der Geschwindigkeit gemessen — gleicher Sensor, keine zusätzliche Mechanik. Die Berechnung erfolgt aus den Laufzeitdifferenzen der orthogonalen Transducer-Paare:

```
θ = arctan(v_y / v_x)

v_x = Windkomponente N-S-Achse
v_y = Windkomponente O-W-Achse
```

#### 2.1.3 Scheinbarer und Wahrer Wind

**Scheinbarer Wind (Apparent Wind, AW):**
Der Wind, den die Instrumente am Masttop messen, ist immer der scheinbare Wind — eine Überlagerung aus dem tatsächlichen (wahren) Wind und dem Fahrtwind des Bootes. Die Masttopp-Instrumente liefern:

- **AWA (Apparent Wind Angle)**: Winkel des scheinbaren Windes relativ zur Bootslängsachse, typisch 0°–180° Steuerbord/Backbord
- **AWS (Apparent Wind Speed)**: Geschwindigkeit des scheinbaren Windes in kn

**Wahrer Wind (True Wind, TW):**
Der tatsächliche, auf die Wasseroberfläche bezogene Wind. Muss berechnet werden aus AWA, AWS und der Bootsgeschwindigkeit (STW = Speed Through Water oder SOG = Speed Over Ground):

```
TWS = √(AWS² + STW² - 2 × AWS × STW × cos(AWA))
TWA = arccos((AWS × cos(AWA) - STW) / TWS)

TWS = True Wind Speed [kn]
TWA = True Wind Angle [°]
AWS = Apparent Wind Speed [kn]
AWA = Apparent Wind Angle [°]
STW = Speed Through Water [kn]
```

**Praxisrelevante Korrekturfaktoren:**

| Faktor | Beschreibung | Typischer Wert |
|--------|-------------|----------------|
| Mastbiegung | Verändert die Ausrichtung des Sensors | 1°–5° je nach Segeldruck |
| Krängung | Kippt den Sensor aus der Horizontalen | cos(φ)-Korrektur, bis 30° |
| Upwash | Segel beeinflussen Strömung am Masttop | 2°–8° Abweichung in AWA |
| Eigengeschwindigkeit | Hängt von STW-Quelle ab | GPS-SOG enthält Strom |
| Höhe über Wasser | Windgradient (Grenzschicht) | +10 % pro Verdoppelung der Höhe |

**Windkorrektur in der Praxis:**
Professionelle Windprozessoren (B&G H5000, Orca Core) bieten konfigurierbare Korrekturtabellen für Upwash und Mastbiegung. Die Kalibrierung erfolgt typischerweise durch Kreissegeln bei konstantem Wind:

1. Auf konstantem Kurs segeln, AWA/AWS notieren
2. Boot um 360° drehen, AWA/AWS auf jedem Kurs notieren
3. Systematische Abweichungen als Korrekturtabelle einpflegen
4. Bei verschiedenen Windstärken wiederholen (Upwash ist windstärkeabhängig)

### 2.2 Logge — Geschwindigkeitsmessung durchs Wasser

#### 2.2.1 Paddle-Wheel-Log (Flügelrad-Log)

Das verbreitetste Messprinzip auf Fahrtenyachten. Ein kleines Schaufelrad (Paddle-Wheel) ragt durch einen Durchbruchgeber in die Strömung und wird vom Wasser angetrieben. Magnete im Schaufelrad passieren einen Hallsensor oder Reed-Kontakt und erzeugen Impulse proportional zur Geschwindigkeit.

**Funktionsprinzip:**
```
STW = (Impulse / Zeit) × Kalibrierfaktor

Typisch: 1 Impuls pro 0,05–0,10 m Fahrstrecke
→ bei 6 kn ≈ 30–60 Impulse/Sekunde
```

**Technische Daten (typisch):**

| Parameter | Wert |
|-----------|------|
| Messbereich | 0,5–50 kn |
| Auflösung | 0,01 kn |
| Genauigkeit | ±5 % (unkalibriert), ±2 % (kalibriert) |
| Anlaufgeschwindigkeit | 0,5–1,5 kn |
| Einbautiefe unter Rumpf | 5–15 mm |
| Durchbruch-Durchmesser | 38 mm (Standard), 50 mm (Flush-mount) |
| Rumpfdicke | 8–25 mm (Standard-Geber) |
| Kabeltyp | 2-adrig geschirmt, 0,5 mm² |

**Einbauregeln:**
- Mindestens 300 mm von der Mittschiffslinie entfernt (Kiel-Turbulenzen)
- Vorzugsweise im vorderen Drittel des Rumpfes
- Nicht hinter Durchbrüchen, Wulstbug oder Kiel-Ansatz
- Ausrichtung: Schaufelrad-Achse quer zur Fahrtrichtung
- Bei Segelyachten: Lee-Seite bevorzugen (weniger Luftblasen)

**Bekannte Probleme:**
- Bewuchs: Seepocken blockieren das Schaufelrad → STW = 0 oder zu niedrig
- Luftblasen: Bei Krängung >20° Luft am Geber → instabile Anzeige
- Plastiktüten/Seetang: Kurzzeitige Blockade → STW-Aussetzer
- Kavitation: Bei STW >25 kn Hohlraumbildung am Schaufelrad → zu niedrige Werte

#### 2.2.2 Ultraschall-Log (Doppler-Log)

Zwei Ultraschall-Transducer sind schräg (typisch 45°) zur Strömungsrichtung angeordnet. Die Laufzeitdifferenz der Schallpulse ergibt die Strömungsgeschwindigkeit:

```
v = (c² / (2 × L × cos(α))) × Δt

c = Schallgeschwindigkeit im Wasser (~1500 m/s)
L = Transducer-Abstand [m]
α = Neigungswinkel zur Strömung [°]
Δt = Laufzeitdifferenz [s]
```

**Technische Daten:**

| Parameter | Wert |
|-----------|------|
| Messbereich | 0,05–99 kn |
| Auflösung | 0,01 kn |
| Genauigkeit | ±1 % nach Kalibrierung |
| Anlaufgeschwindigkeit | 0,05 kn |
| Einbau | Durchbruch oder Flush-mount |
| Durchbruch-Durchmesser | 50–76 mm |
| Abtastrate | 2–10 Hz |

**Vorteile gegenüber Paddle-Wheel:**
- Keine beweglichen Teile → kein Bewuchsproblem am Rotor
- Höhere Genauigkeit und Auflösung
- Kein Verschleiß an Lagern oder Magneten
- Funktioniert bei hohen Geschwindigkeiten ohne Kavitation

**Nachteile:**
- Bewuchs auf den Transducer-Flächen kann Signal stören
- Luftblasen am Geber sind kritischer als beim Paddle-Wheel
- Höherer Preis (Faktor 3–5 gegenüber Paddle-Wheel)
- Empfindlicher gegenüber Turbulenzen am Einbauort

#### 2.2.3 GPS-SOG (Speed Over Ground)

GPS liefert keine Geschwindigkeit durchs Wasser, sondern über Grund. Die Differenz zwischen STW (Logge) und SOG (GPS) ergibt den Strom:

```
Strom ≈ SOG - STW  (vereinfacht, nur in Fahrtrichtung)

Genauer als Vektoroperation:
Strom_N = SOG × cos(COG) - STW × cos(HDG)
Strom_E = SOG × sin(COG) - STW × sin(HDG)

COG = Course Over Ground (GPS)
HDG = Heading (Kompass)
```

**GPS-SOG-Genauigkeit:**

| GPS-Typ | Genauigkeit Position | SOG-Genauigkeit |
|---------|---------------------|-----------------|
| Standard GPS | ±3–5 m | ±0,1 kn (>2 kn) |
| DGPS/SBAS | ±0,5–2 m | ±0,05 kn |
| RTK-GPS | ±0,02 m | ±0,01 kn |

**Wann SOG statt STW verwenden:**
- Motorboote in bekanntem Revier (kein Strom relevant für Navigation)
- Backup bei defektem Log
- Niemals für Segelperformance-Analyse (wahrer Wind braucht STW!)

### 2.3 Echolot — Tiefenmessung

#### 2.3.1 Grundprinzip

Ein piezoelektrischer Schwinger sendet Ultraschall-Pulse zum Meeresgrund. Aus der Laufzeit des Echos wird die Tiefe berechnet:

```
d = (c × t) / 2

d = Tiefe [m]
c = Schallgeschwindigkeit im Wasser [m/s]
t = Laufzeit Sende→Empfangspuls [s]

Schallgeschwindigkeit Seewasser: ~1500 m/s (variiert mit T, S, p)
Schallgeschwindigkeit Süßwasser: ~1480 m/s bei 20°C
```

#### 2.3.2 Frequenzen und ihre Eigenschaften

**200 kHz — Hochfrequenz:**

| Parameter | Wert |
|-----------|------|
| Kegelwinkel | 6°–12° |
| Max. Messtiefe | 200–400 m (je nach Grundbeschaffenheit) |
| Auflösung | sehr gut (5–10 cm bei flachem Wasser) |
| Bodendetail | hoch — Einzelfische sichtbar |
| Einsatz | Küstennavigation, Ankerplatzsuche |

**50 kHz — Niederfrequenz:**

| Parameter | Wert |
|-----------|------|
| Kegelwinkel | 30°–45° |
| Max. Messtiefe | 600–3000 m |
| Auflösung | mittel (0,5–1 m) |
| Bodendetail | gering — Bodenstruktur erkennbar, keine Einzelfische |
| Einsatz | Hochsee, Tiefwasser-Navigation |

**CHIRP (Compressed High Intensity Radar Pulse):**

Statt einer einzelnen Frequenz wird ein Frequenzsweep gesendet (z. B. 130–210 kHz oder 42–65 kHz). Durch Korrelationsfilterung im Empfänger ergibt sich:

- **5–10× bessere Zielauflösung** als Single-Frequency
- **Weniger Rauschen** (höherer Signal-Rauschabstand)
- **Bessere Tiefenleistung** bei gleicher Sendeleistung
- **Grund-Klassifizierung** möglich (Sand, Schlick, Fels)

**Dual-Frequency vs. CHIRP:**
Moderne Echolotgeber bieten häufig CHIRP in beiden Frequenzbereichen. Für die Yachtnavigation ist ein CHIRP-fähiger 200-kHz-Geber optimal — er liefert exzellente Detailauflösung bis 200 m Tiefe und reicht für alle Küsten- und Offshore-Reviere.

#### 2.3.3 Gebertypen

**Durchbruchgeber (Thru-Hull):**
- Direkter Wasserkontakt → beste Signalqualität
- Erfordert Rumpfdurchbruch mit Seeventil oder gewidmeter Bohrung
- Typischer Durchmesser: 50 mm (Standard), 76 mm (Flush-mount)
- Bronze-Gehäuse (GFK-Rumpf) oder Kunststoff (alle Rumpftypen)
- **Achtung:** Bronze-Geber auf Aluminiumrumpf → galvanische Korrosion!

**Einschwinger (In-Hull / Shoot-Through):**
- Geber wird innen auf den Rumpfboden geklebt (Epoxid oder Silikon)
- Signal geht durch den Rumpf → Signaldämpfung 30–50 %
- Funktioniert nur bei Einschalenrumpf (massives GFK)
- Nicht bei Sandwichbauweise, Holz oder Aluminium
- Kein Antifouling-Problem, kein Durchbruch

**Heckspiegel-Geber (Transom-Mount):**
- Auf den Heckspiegel geschraubt, ragt unter die Wasserlinie
- Einfachste Installation — kein Rumpfdurchbruch
- Problem: Turbulenzen bei hoher Fahrt, Belüftung, Querneigung bei Krängung
- Typisch für kleine Sportboote, Trailer-Boote

**Spiegelmontage mit Motormontage-Halterung:**
- Geber am Außenborder-Spiegel oder Motorschaft
- Für Kleinboote und Anglerboote
- Begrenzte Genauigkeit durch Motor-Turbulenzen

#### 2.3.4 Tiefenkorrektur und Kalibration

Die angezeigte Tiefe muss korrigiert werden:

```
Tiefe_unter_Kiel = Tiefe_gemessen - Offset_Geber_bis_Kiel
Tiefe_unter_WL = Tiefe_gemessen + Offset_WL_bis_Geber

Typische Offsets:
  Geber → Kiel: +0,3 bis +2,0 m (Segelyacht mit Kiel)
  Geber → Wasserlinie: -0,2 bis -0,8 m
```

**Anzeige-Konventionen:**
- **Tiefe unter Geber**: Rohdaten, ohne Korrektur
- **Tiefe unter Kiel**: Für Sicherheitsnavigation — zeigt den Abstand Kielunterkante↔Grund
- **Tiefe unter Wasserlinie**: Für Kartenbezug — korrespondiert mit Seekartentiefen

**Kalibrationsmethode:**
1. Boot an bekannter Position mit verlässlicher Kartentiefe
2. Handlot zur Kontrolle (Bleilot an markierter Leine)
3. Tiefenoffset im Instrument einstellen
4. Bei unterschiedlichen Geschwindigkeiten prüfen (Blasenbildung ändert Lesung)
5. Salzgehalt berücksichtigen (Schallgeschwindigkeit Süß-/Salzwasser)

### 2.4 Barometer und Druckmessung

#### 2.4.1 Messprinzip

**Aneroid-Barometer (mechanisch):**
Eine evakuierte Metall-Dose (Aneroid-Kapsel) verformt sich mit dem Luftdruck. Über ein Hebelwerk wird die Verformung auf einen Zeiger übertragen.

- **Messbereich**: 950–1060 hPa (marinerelevant)
- **Auflösung**: 0,5–1 hPa (visuell), 0,1 hPa (Präzisionsgeräte)
- **Genauigkeit**: ±1–2 hPa (gute Geräte)
- **Temperaturkompensation**: Bimetall-Kompensation in Präzisionsgeräten
- **Lebensdauer**: 30+ Jahre bei Pflege

**Elektronischer Drucksensor (piezoresistiv/kapazitiv):**
Ein MEMS-Sensor (Micro-Electro-Mechanical System) misst die druckinduzierte Verformung einer Silizium-Membran.

- **Messbereich**: 300–1100 hPa (absolut)
- **Auflösung**: 0,01 hPa
- **Genauigkeit**: ±0,1–0,5 hPa
- **Abtastrate**: 1 Hz (typisch für Marine-Barographen)
- **Temperaturkompensation**: Digitale Kalibrierkoeffizienten

#### 2.4.2 Barograph — Druckaufzeichnung

Der Barograph zeichnet den Luftdruck über die Zeit auf. Moderne digitale Barographen speichern typisch:
- 48-Stunden-Verlauf mit 1-Minute-Auflösung
- 30-Tage-Verlauf mit 15-Minuten-Auflösung

**Wetterrelevante Druckänderungen:**

| Druckänderung | Zeitraum | Bedeutung |
|---------------|----------|-----------|
| <1 hPa | 3 h | Stabile Wetterlage |
| 1–3 hPa Abfall | 3 h | Verschlechterung, Warmfront |
| 3–6 hPa Abfall | 3 h | Deutliche Verschlechterung, Tiefdruckgebiet |
| >6 hPa Abfall | 3 h | Sturmwarnung, schnell ziehendes Tief |
| >10 hPa Abfall | 3 h | Orkanpotential |
| 1–3 hPa Anstieg | 3 h | Wetterbesserung, Hochdruckaufbau |
| Schneller Anstieg nach Tief | 1–2 h | Kaltfrontdurchgang, Böen möglich |

### 2.5 Tankgeber — Füllstandsmessung

#### 2.5.1 Widerstandsgeber (Resistiv)

Das verbreitetste Messprinzip auf Yachten. Ein Schwimmer gleitet auf einer Führungsstange, an der ein Widerstandsdraht oder eine Widerstandsbahn montiert ist. Der Schwimmer bewegt einen Schleifkontakt, dessen Position den Widerstand ändert.

**Varianten:**

| Typ | Widerstand | Signal | Kompatibilität |
|-----|-----------|--------|----------------|
| Europäisch (VDO/Wema) | 0–180 Ω (leer→voll) | Widerstand | VDO, Wema, NMEA-Adapter |
| US-Standard (Faria) | 240–33 Ω (leer→voll) | Widerstand | Faria, Teleflex, US-Instrumente |
| Universal | 10–180 Ω (konfigurierbar) | Widerstand | Mit Anpassungswiderstand |

**Konfiguration nach Tankform:**
- **Rechteckiger Tank**: Lineare Kennlinie — Widerstand proportional zum Füllstand
- **Keel-Tank (trapezförmig)**: Nichtlineare Kennlinie — erfordert Kennlinienprogrammierung oder mehrstufigen Geber
- **Flexibler Bladder-Tank**: Nur Ultraschall-Geber oder Drucksensor sinnvoll

**Technische Daten:**

| Parameter | Wert |
|-----------|------|
| Messbereich | 150–1200 mm Eintauchtiefe (Standard) |
| Auflösung | 5–10 % Füllstand |
| Genauigkeit | ±5–10 % (gut), ±15–20 % (bei ungünstiger Tankform) |
| Material Führungsstange | Edelstahl 316L oder Kunststoff (kraftstoffbeständig) |
| Schwimmer | Kork, Schaumstoff (Diesel), Nitrophyl (Benzin) |
| Anschlussgewinde | 1¼"–5-Loch-Flansch (52 mm PCD) oder M5 Bolzen |
| Lebensdauer | 5–15 Jahre (Abrieb am Schleifkontakt limitierend) |

#### 2.5.2 Ultraschall-Tankgeber

Ein Ultraschall-Transducer wird außen auf den Tank geklebt und misst den Füllstand durch die Tankwand hindurch — berührungslos.

**Funktionsprinzip:**
```
Füllstand = c_medium × t_echo / 2

c_medium ≈ 1250 m/s (Diesel), 1150 m/s (Benzin), 1480 m/s (Wasser)
t_echo = Laufzeit des Echos von der Flüssigkeitsoberfläche
```

**Technische Daten:**

| Parameter | Wert |
|-----------|------|
| Messbereich | 50–1500 mm |
| Auflösung | 1 mm |
| Genauigkeit | ±1 % (kalibriert) |
| Tankwandmaterial | GFK, Polyethylen, Edelstahl (nicht Aluminium) |
| Tankwanddicke | max. 6 mm (GFK), max. 4 mm (PE), max. 3 mm (Edelstahl) |
| Montage | Außen auf Tankboden geklebt |
| Lebensdauer | 15+ Jahre (keine beweglichen Teile) |

**Vorteile:**
- Kein Tankdurchbruch → kein Leckrisiko
- Keine beweglichen Teile im Tank → kein Verschleiß
- Unabhängig vom Medium → gleicher Geber für Wasser, Diesel, Abwasser
- Nachrüstung ohne Tanköffnung

**Nachteile:**
- Funktioniert nicht bei Aluminium-Tanks (Schallreflexion zu hoch)
- Empfindlich gegen Luftblasen oder Schaum auf der Oberfläche
- Muss exakt horizontal auf Tankboden montiert sein
- Kalibrierung für Schallgeschwindigkeit des Mediums erforderlich

#### 2.5.3 Kapazitiver Tankgeber

Ein Rohr oder Stab im Tank misst die Kapazitätsänderung zwischen zwei konzentrischen Elektroden. Da die Dielektrizitätskonstante der Flüssigkeit (Diesel ε ≈ 2, Wasser ε ≈ 80) anders ist als die von Luft (ε ≈ 1), ändert sich die Kapazität proportional zum Füllstand.

```
C = (2π × ε₀ × ε_r × L) / ln(r_außen / r_innen)

L = eingetauchte Länge [m]
ε_r = Dielektrizitätskonstante des Mediums
r_außen, r_innen = Radien der Elektroden
```

**Technische Daten:**

| Parameter | Wert |
|-----------|------|
| Messbereich | 100–2000 mm |
| Auflösung | 1 % |
| Genauigkeit | ±2 % (kalibriert) |
| Medien | Diesel, Benzin, Wasser (getrennte Kalibrierung) |
| Material | Edelstahl 316L |
| Signal | 4–20 mA oder 0–5 V |
| Lebensdauer | 20+ Jahre (keine beweglichen Teile) |

**Vorteil:** Keine beweglichen Teile, unempfindlich gegen Schiffsbewegung.
**Nachteil:** Kalibrierung mediumabhängig, Verschmutzung der Elektroden verfälscht Messwerte.

#### 2.5.4 Hydrostatischer Druckgeber

Ein Drucksensor am Tankboden misst den hydrostatischen Druck der Flüssigkeitssäule:

```
h = p / (ρ × g)

h = Füllhöhe [m]
p = gemessener Druck [Pa]
ρ = Dichte des Mediums [kg/m³] (Diesel ≈ 840, Wasser ≈ 1025)
g = 9,81 m/s²
```

Einsatz auf Yachten selten — überwiegend bei großen Tanks auf Superyachten.

### 2.6 Temperaturmessung

#### 2.6.1 NTC-Thermistor

**Negative Temperature Coefficient** — der Widerstand sinkt mit steigender Temperatur. Meistverwendeter Temperatursensor auf Yachten wegen niedrigem Preis und einfacher Verkabelung.

```
R(T) = R₀ × exp(B × (1/T - 1/T₀))

R₀ = Widerstand bei T₀ (typisch 10 kΩ bei 25°C)
B = Materialkonstante (typisch 3380–4000 K)
T = Temperatur [K]
```

**Technische Daten:**

| Parameter | Wert |
|-----------|------|
| Messbereich | -40°C bis +125°C (marinerelevant: -10 bis +100°C) |
| Genauigkeit | ±0,5°C (Klasse B), ±1°C (Klasse C) |
| Ansprechzeit | 5–30 s (je nach Gehäuse und Medium) |
| Typischer R25 | 10 kΩ (Motortemperatur), 6,8 kΩ (VDO-kompatibel) |
| Lebensdauer | 10+ Jahre |

**Einsatz auf Yachten:**
- Kühlwassertemperatur (Motor)
- Motoröl-Temperatur
- Abgas-Temperatur (begrenzt — max. ~300°C mit Spezial-NTC)
- Kabinen-Temperatur
- Kühlschrank-/Tiefkühler-Temperatur

#### 2.6.2 PT100/PT1000 (Platin-Widerstandsthermometer)

**Funktionsprinzip:** Der Widerstand von Platin steigt nahezu linear mit der Temperatur. PT100 hat 100 Ω bei 0°C, PT1000 hat 1000 Ω bei 0°C.

```
R(T) = R₀ × (1 + A×T + B×T²)

A = 3,9083 × 10⁻³ °C⁻¹
B = -5,775 × 10⁻⁷ °C⁻²
R₀ = 100 Ω (PT100) oder 1000 Ω (PT1000)
```

**Technische Daten:**

| Parameter | Wert |
|-----------|------|
| Messbereich | -200°C bis +850°C |
| Genauigkeit | ±0,1°C (Klasse A), ±0,3°C (Klasse B) |
| Linearität | Sehr gut (nahezu linear über gesamten Bereich) |
| Langzeitstabilität | Hervorragend (<0,05°C/Jahr Drift) |
| Anschluss | 2-, 3- oder 4-Leiter |

**Einsatz auf Yachten:**
- Präzise Wassertemperaturmessung (Wetterstation, Fischfinder)
- Motorüberwachung auf Superyachten
- Klimaanlagen-Regelung

#### 2.6.3 Wassertemperatur-Geber

Spezielle Variante der Temperaturmessung durch den Rumpf oder als Durchbruchgeber:

**Durchbruchgeber:** NTC oder PT100 in Bronze- oder Kunststoffgehäuse, montiert im Borddurchlass. Direkter Wasserkontakt für schnelle Ansprechzeit.

**Einschwingergeber:** NTC in Metallgehäuse, auf die Rumpfinnenseite geklebt. Messwertverzögerung durch Rumpfdicke — typisch 2–5 Minuten bis zur Stabilisierung.

### 2.7 Kompass — Kursreferenz

#### 2.7.1 Fluxgate-Kompass

Ein elektromagnetischer Kompass, der das Erdmagnetfeld über zwei oder drei Fluxgate-Sonden misst. Im Gegensatz zum magnetischen Steuermannskompass liefert er ein digitales Signal für die Bordelektronik.

**Funktionsprinzip:**
Zwei hochpermeable Ferritkerne werden periodisch mit Wechselstrom gesättigt. In der Sättigungsphase wird der Kern für das externe Erdfeld durchlässig — das Erdfeld induziert eine messbare Spannung in der Sekundärwicklung. Aus dem Verhältnis zweier orthogonaler Sonden ergibt sich der magnetische Kurs.

**Technische Daten:**

| Parameter | Wert |
|-----------|------|
| Genauigkeit | ±1° (nach Kompensation) |
| Auflösung | 0,1° |
| Abtastrate | 10–40 Hz |
| Neigungskompensation | ±25°–±35° (elektronisch) |
| Deviation | Softwaregestützte Kompensation (Lernkreis) |
| Einbau | Horizontal, vibrationsfrei, fern von Eisen/Magneten |
| NMEA-Output | HDG (Heading), HDM (Magnetic), HDT (True) |

**Kompensationsverfahren:**
1. Boot dreht langsam 360° bei ruhiger See
2. Sensor misst Deviation auf jedem Kurs
3. Algorithmus berechnet Kompensationskoeffizienten (A–E nach Admiralitätsmodell)
4. Restdeviation typisch <1° nach guter Kompensation

**Bekannte Fehlerquellen:**
- Elektrische Geräte in der Nähe (Lautsprecher, Motoren, Kabel)
- Eisenhaltige Gegenstände, die bewegt werden (Werkzeug, Konserven)
- Magnetische Störungen durch Gleich- oder Wechselstromkabel
- Erdmagnetfeld-Anomalien in Hafennähe (Stahlspundwände)

#### 2.7.2 Satellitenkompass (GNSS-Kompass)

Zwei oder mehr GPS-Antennen in definiertem Abstand (typisch 0,5–2 m) bestimmen den Kurs aus der Phasendifferenz der GPS-Signale. Unabhängig vom Erdmagnetfeld.

**Technische Daten:**

| Parameter | Wert |
|-----------|------|
| Genauigkeit (Heading) | ±0,5° (1 m Baseline), ±0,2° (2 m Baseline) |
| Auflösung | 0,01° |
| Abtastrate | 10–20 Hz |
| Neigungskompensation | Integriert (3D-GNSS) |
| Deviation | Keine (nicht magnetisch) |
| GNSS-Systeme | GPS, GLONASS, Galileo, BeiDou |
| Kaltstart | 60–180 s |
| Warmstart | 5–15 s |

**Vorteile gegenüber Fluxgate:**
- Keine Kompensation erforderlich
- Keine magnetischen Störungen
- Höhere Genauigkeit auf Stahlbooten
- Liefert True Heading (kein Missweisung-Problem)

**Nachteile:**
- Teurer (Faktor 5–10)
- Braucht GPS-Empfang (nicht im Tunnel, unter Brücken)
- Mindestabstand der Antennen für Genauigkeit
- Stromverbrauch höher

#### 2.7.3 Heading-Sensor mit MEMS-Gyroskop

Moderne IMU-basierte Kurssensoren (Inertial Measurement Unit) kombinieren:
- 3-Achsen-Beschleunigungssensor
- 3-Achsen-Gyroskop
- 3-Achsen-Magnetometer (Fluxgate oder Hall)
- Sensorfusion via Kalman-Filter

**Technische Daten:**

| Parameter | Wert |
|-----------|------|
| Genauigkeit | ±0,5°–±2° (je nach Kalibrierung und Qualität) |
| Auflösung | 0,1° |
| Abtastrate | 50–200 Hz |
| Dynamische Genauigkeit | Besser als reiner Fluxgate bei Seegang |
| Neigungsmessung | ±0,1°–±0,5° |
| Gier-Erkennung | Ja (Gyroskop) |
| Rate of Turn | Ja, ±180°/s |

### 2.8 Neigungssensor

#### 2.8.1 Pendel-Neigungsmesser (mechanisch)

Klassischer Krängungs-Anzeiger: Ein gedämpftes Pendel zeigt die Querlage des Bootes. Einfach, robust, ohne Strom.

- **Genauigkeit**: ±2°
- **Auflösung**: 1°
- **Dämpfung**: Öl- oder Silikonbad
- **Einsatz**: Visueller Indikator, keine Datenausgabe

#### 2.8.2 MEMS-Neigungssensor

Mikromechanischer Beschleunigungssensor (MEMS-Accelerometer) misst die Schwerkraftkomponenten in zwei oder drei Achsen:

```
Krängung (Heel) = arctan(a_y / a_z)
Trimm (Pitch) = arctan(a_x / √(a_y² + a_z²))

a_x, a_y, a_z = Beschleunigung in Boots-Achsen [m/s²]
```

**Technische Daten:**

| Parameter | Wert |
|-----------|------|
| Messbereich | ±90° Heel, ±45° Pitch |
| Auflösung | 0,1° |
| Genauigkeit | ±0,5° (statisch), ±1° (dynamisch bei Seegang) |
| Abtastrate | 10–100 Hz |
| NMEA-Output | XDR (Transducer Data) |
| Einbau | Mittschiffs, nahe Schwerpunkt |

**AYDI-Relevanz:**
- Krängung beeinflusst effektive Passagenbreite (Ergonomie-Modul)
- Trimm beeinflusst Segeltrimm-Empfehlung
- Dynamische Krängung bei Manövern → Stabilitätsbewertung
- Heel-Korrektur für wahren Wind

### 2.9 Drehzahlmessung (Tachometer)

**Mechanisch (Seilzug-Tachometer):** Historisch, nur noch auf Oldtimer-Yachten.

**Induktiver Impulsgeber:**
Sensor am Schwungrad oder Zahnkranz zählt Zähne pro Umdrehung:

```
RPM = (Impulse × 60) / Zähnezahl

Typisch: 115–160 Zähne je nach Motor
Flywheel-Geber: W-Anschluss der Lichtmaschine (Halbwellen/Umdrehung)
```

**Alternator W-Signal:**
Das W-Signal der Lichtmaschine liefert Wechselspannungs-Pulse proportional zur Drehzahl. Die Frequenz ergibt sich aus:

```
f_W = RPM × Polpaare / 60

Typische Polpaare: 6 (12-polig) → f_W = RPM × 6 / 60
Bei 3000 RPM: f_W = 300 Hz
```

---

## 3. Typenübersicht

### 3.1 Masttop-Einheit

**Beschreibung:** Kombinationseinheit aus Windgeber (Anemometer + Windfahne) und optional UHF/VHF-Antenne, LED-Toplicht, am Masttopp montiert. Gewicht und Kabelführung sind kritische Faktoren.

**Montagearten:**

| Montage | Beschreibung | Vorteile | Nachteile |
|---------|-------------|----------|-----------|
| Fest verschraubt | Direkt am Masttopp | Stabil, keine Vibrationen | Schwer zu warten |
| Klappbar | Scharnier-Halterung | Lässt sich für Wartung umlegen | Mögliches Spiel |
| Steckbar | Konischer Zapfen | Einfachster Austausch | Korrosion im Stecker |
| Wireless | Batterie-/Solarbetrieb | Kein Mastkabel, nachträglicher Einbau | Batterie-Management, Funk-Zuverlässigkeit |

**Verkabelung im Mast:**

| Kabeltyp | Querschnitt | Abschirmung | Für |
|----------|-------------|-------------|-----|
| Wind-Daten | 8-adrig, 0,5 mm² | Geschirmt | AWA/AWS Signale |
| Strom | 2-adrig, 1,0 mm² | Nicht erforderlich | Versorgung 12V |
| NMEA 2000 | CAN-Bus Micro-C | Geschirmt | Digitale Sensoren |
| Ethernet | Cat5e Marine | Geschirmt | H5000-Systeme |
| Composite | Kombikabel 10-adrig | Gesamt-Schirm | Wind + Toplicht |

**Typische Probleme:**
- Korrosion der Masttopp-Steckverbindung (häufigster Fehler!)
- Kabelbruch durch Mastbiegung und Vibration
- Wasser im Mastkabel-Kanal → Oxidation der Adern
- UV-Degradation der Kabel-Isolation
- Vogelkot auf Ultraschall-Transducern → Messfehler

### 3.2 Durchbruch-Geber

**Beschreibung:** Sensoren, die durch den Rumpf montiert werden und direkten Wasserkontakt haben. Erfordern einen Rumpfdurchbruch mit Seeventil oder dediziertem Gebergehäuse.

**Standard-Gebersysteme:**

| System | Durchbruch ⌀ | Sensoren | Typ |
|--------|-------------|----------|-----|
| Airmar B45 | 50 mm | Tiefe | Bronze, 200 kHz |
| Airmar DST800 | 50 mm | Tiefe + STW + Temp | Kunststoff, Smart-Sensor NMEA 2000 |
| Airmar B744V | 50 mm | Tiefe + STW + Temp | Bronze, Paddle-Wheel |
| Airmar P79 | 50 mm | Tiefe | Kunststoff, 200 kHz |
| B&G DT800 | 50 mm | Tiefe + STW + Temp | Kunststoff, NMEA 2000 |
| Garmin GT20-TM | Heckspiegel | Tiefe + Temp | Kunststoff, CHIRP |
| Furuno 525T-BSD | 50 mm | Tiefe + Temp | Bronze, 50/200 kHz |

**Materialwahl nach Rumpfmaterial:**

| Rumpfmaterial | Gebergehäuse | Begründung |
|---------------|-------------|------------|
| GFK | Kunststoff oder Bronze | Kein galvanisches Problem |
| Stahl | Kunststoff oder Edelstahl | Bronze erzeugt galvanische Korrosion |
| Aluminium | Nur Kunststoff | Bronze und Edelstahl → massive Korrosion! |
| Holz | Bronze oder Kunststoff | Bronze mit Stopfbuchse, Holz muss versiegelt sein |

### 3.3 Innenliegende Sensoren

**Beschreibung:** Sensoren, die keinen Rumpfdurchbruch erfordern. Werden innen auf den Rumpf geklebt, auf Schotten geschraubt oder frei im Boot platziert.

| Sensor | Montage | Messgrößen | NMEA |
|--------|---------|------------|------|
| Fluxgate-Kompass | Horizontal, vibrationsfrei | HDG, Deviation | 0183/2000 |
| Neigungssensor | Mittschiffs, nahe CG | Heel, Pitch, Roll | 2000 |
| Barometer | Geschützt, belüftet | Luftdruck | 2000 |
| Innen-Thermometer | Kabine | Lufttemperatur | 2000 |
| Ultraschall-Lot | Auf Rumpfboden geklebt | Tiefe | 2000 |
| GPS-Empfänger | Innen (bei GFK-Rumpf) | Position, SOG, COG | 0183/2000 |
| Batteriemonitor | Am Batterie-Shunt | V, A, Ah, SOC | 2000 |

### 3.4 Display-Instrumente

#### 3.4.1 Analoge Rundinstrumente

Klassische Zeigerinstrumente mit beleuchteten Skalen. Nach wie vor beliebt für:
- Magnetkompass (nach SOLAS/ISO unverzichtbar)
- Barometer (traditionelles Schiffsbarometer in Messing)
- Quecksilberthermometer (Nostalgie/Backup)
- VDO/Wema-Motorinstrumente (Drehzahl, Temperatur, Öldruck)

**VDO ViewLine Marine-Instrumentierung:**

| Instrument | Durchmesser | Messbereich | Beleuchtung |
|-----------|-------------|-------------|------------|
| Drehzahlmesser | 85 mm | 0–4000/6000/8000 RPM | LED rot/weiß |
| Kühlwasser-Temp. | 52 mm | 40–120°C | LED rot/weiß |
| Öldruck | 52 mm | 0–10 bar | LED rot/weiß |
| Voltmeter | 52 mm | 8–16 V | LED rot/weiß |
| Tankgeber | 52 mm | 0–100 % | LED rot/weiß |

#### 3.4.2 Digitale Einzelinstrumente

Spezialisierte Displays, die jeweils einen oder wenige Sensorwerte anzeigen:

| Typ | Displaygröße | Ablesbarkeit | Blickwinkel |
|-----|-------------|-------------|-------------|
| Rund (B&G Triton2) | 4,1" LCD | 30 m bei Sonnenlicht | 170° |
| Rund (Raymarine i70s) | 4" LCD | 25 m | 160° |
| Rund (Garmin GNX 20) | 4" LCD | 25 m | 170° |
| Quadratisch (Simrad IS42) | 4,1" LCD | 25 m | 170° |
| Großformat (B&G Nemesis) | 6,5" LCD | 40 m | 170° |

**Anforderungen an Marine-Displays:**
- Sonnenlicht-Ablesbarkeit: min. 1000 cd/m² (besser 1500+)
- Betriebstemperatur: -15°C bis +55°C
- Schutzklasse: IPX6 oder IPX7 (wasserdicht)
- Nachtmodus: Rote Hintergrundbeleuchtung, dimmbar
- Anti-Beschlag: Belüftungsbohrung oder Hydrophob-Beschichtung

#### 3.4.3 Multifunktionsdisplays (MFD)

Moderne MFDs vereinen Kartenplotter, Radar-Anzeige, Motorüberwachung und Instrumentenanzeige in einem Gerät. Für die reine Instrumentenanzeige relevant:

- **Instrument-Dashboards**: Konfigurierbare Anzeigenseiten mit beliebigen Sensorwerten
- **Segelanzeige**: Windrose, Polarkurve, Startlinie, Laylines
- **Motorüberwachung**: Alle NMEA-2000-Motorparameter auf einem Bildschirm
- **Tankübersicht**: Alle Tanks mit Füllstand und Verbrauch

### 3.5 Prozessor-Einheiten

**Beschreibung:** Zentrale Recheneinheiten, die rohe Sensordaten verarbeiten, kalibrieren und erweiterte Berechnungen durchführen (wahrer Wind, Laylines, VMG, optimaler Segelwinkel).

| Prozessor | Hersteller | Eingänge | Berechnungen | Bus |
|-----------|-----------|----------|-------------|-----|
| H5000 CPU | B&G | 6×NMEA 2000, 4×Analog, Ethernet | TWS/TWA, VMG, Laylines, Strom, Polar | NMEA 2000 + Ethernet |
| Orca Core | Sailmon | NMEA 2000, WiFi | TWS/TWA, VMG, Polar, Leg-Analyse | NMEA 2000 + WiFi |
| Expedition (PC) | Expedition Marine | NMEA 0183/2000 über USB | Alles (PC-basiert) | USB-NMEA-Adapter |
| NX2 Server | Nexus/Garmin | Proprietär (NX2-Bus) | TWS/TWA, VMG, Log-Trip | NX2 + NMEA 0183 |
| iTC-5 | Raymarine | SeaTalkng (NMEA 2000) | Analog-Digital-Wandlung | SeaTalkng |
| GI 10 | Garmin | NMEA 2000 | Analog-Digital-Wandlung | NMEA 2000 |

### 3.6 WiFi-Sensoren und drahtlose Integration

**Drahtlose Windgeber:**

| Modell | Messprinzip | Funk | Reichweite | Stromversorgung | Datenrate |
|--------|-----------|------|-----------|----------------|-----------|
| B&G WS320 | Ultraschall | WiFi 2,4 GHz | 50 m | Solarzelle + Akku | 4 Hz |
| Calypso ULP | Ultraschall | Bluetooth LE | 30 m | Solarzelle + Akku | 1 Hz |
| Garmin gWind Wireless | Schalenkreuz + Fahne | ANT+ | 15 m | AAA-Batterien | 1 Hz |
| Weatherflow WF-100 | Ultraschall | Bluetooth LE | 30 m | Akku (USB laden) | 1 Hz |
| Scarlet SW-1 | Ultraschall | WiFi | 50 m | Solar + Akku | 4 Hz |

**WiFi-Sensorgateways:**

| Gateway | Funktion | Ein | Aus |
|---------|---------|-----|-----|
| Yacht Devices YDWG-02 | NMEA 2000 → WiFi | NMEA 2000 | WiFi (TCP/UDP) |
| Digital Yacht iKonvert | NMEA 2000 → USB → WiFi | NMEA 2000 | USB + opt. WiFi |
| Vesper Cortex | VHF + AIS + NMEA 2000 → WiFi | NMEA 2000, AIS | WiFi, Bluetooth |
| Actisense W2K-1 | NMEA 2000 → WiFi | NMEA 2000 | WiFi (TCP) |
| Ship Modul MiniPlex-3Wi | NMEA 0183 → WiFi | 4× NMEA 0183 | WiFi (TCP/UDP) |

---

## 4. Produktlinien und Spezifikationen

### 4.1 B&G — Sailing Performance

#### 4.1.1 H5000 System

Das H5000 ist B&Gs professionelles Regatta- und Hochsee-Instrumentensystem. Es bildet das Rückgrat der Instrumentierung auf Hochsee-Regattayachten (IMOCA, Class 40, VO65) und anspruchsvollen Fahrtenyachten.

**H5000 CPU (Hydra CPU):**

| Parameter | Wert |
|-----------|------|
| Eingänge | 4× Analog (0–5V), 6× NMEA 2000, 1× Ethernet |
| Ausgänge | 2× NMEA 2000, 1× Ethernet |
| Berechnungen | TWS/TWA, VMG, Optimal Heading, Current, Laylines |
| Polar-Unterstützung | Ja, konfigurierbare Polarkurven |
| Kalibriertabellen | Wind (AWA/AWS per Winkel), Speed (STW per Heel), Tiefe |
| Dampening | Konfigurierbar 1–30 s pro Datenwert |
| Logging | Ja, internes Logging mit Export |
| Stromverbrauch | 2,5 W bei 12V |
| Schutzklasse | IPX6 |
| Abmessungen | 165 × 100 × 52 mm |

**H5000 Analog-Eingänge:**

| Eingang | Typ | Für |
|---------|-----|-----|
| Analog 1 | 0–5V Widerstand | Ruderlage |
| Analog 2 | 0–5V Frequenz | Mast-Rotation (Multihull) |
| Analog 3 | 0–5V Widerstand | Backstage-Spannung (Loadcell) |
| Analog 4 | 0–5V Widerstand | Frei konfigurierbar |

**H5000 Hercules (Performance-Prozessor):**

| Parameter | Wert |
|-----------|------|
| Plattform | Linux-basiert, ARM-Prozessor |
| Ethernet-Ports | 2× (Ringnetzwerk möglich) |
| NMEA 2000 | 2× CAN-Bus |
| WiFi | 802.11 b/g/n |
| Funktionen | Start-Analyse, Wind-Kalibrierung, Daten-Logging, Fernzugriff |
| Webinterface | Ja, über Browser erreichbar |
| Stromverbrauch | 5 W bei 12V |
| Schutzklasse | IPX6 |

**B&G WS320 (Windgeber drahtlos/kabelgebunden):**

| Parameter | Wert |
|-----------|------|
| Messprinzip | Ultraschall (keine beweglichen Teile) |
| Windgeschwindigkeit | 0–80 kn |
| Windrichtung | 0°–360° |
| Genauigkeit | ±2° Richtung, ±0,5 kn oder ±5 % |
| Abtastrate | 4 Hz |
| Verbindung | WiFi (drahtlos) oder NMEA 2000 (kabelgebunden) |
| Stromversorgung | Solar + interner Akku (wireless), 12V (kabelgebunden) |
| Akku-Laufzeit | 2+ Wochen ohne Sonne bei täglichem Segeln |
| Gewicht | 370 g (wireless), 250 g (kabelgebunden) |
| Schutzklasse | IPX7 |

#### 4.1.2 Triton2

B&Gs Fahrtenyacht-Instrumentensystem. Einstiegslösung mit voller NMEA-2000-Integration.

**Triton2 Display:**

| Parameter | Wert |
|-----------|------|
| Displaytyp | 4,1" Sunlight-visible LCD |
| Auflösung | 240 × 160 px (Segmented LCD) |
| Ablesbarkeit | Bis 30 m bei Sonnenlicht |
| Blickwinkel | 170° |
| Seiten | Bis 10 konfigurierbare Seiten |
| Felder pro Seite | 1–4 Datenfelder |
| Funktionen | Wind, Tiefe, Speed, Motor, Segeln, Autopilot-Steuerung |
| Bus | NMEA 2000 (DeviceNet Micro-C) |
| Strom | 0,2 W (Tag), 0,5 W (Nacht mit Beleuchtung) |
| Schutzklasse | IPX7 |
| Einbau | Bündig (52 mm Ausschnitt) oder Aufputz |
| Preis (UVP) | ca. 380 € |

**Triton2 Autopilot-Integration:**
Das Triton2 kann als Bedienpanel für B&G-Autopiloten (NAC-2, NAC-3) dienen — direkte Kursänderung, Windsteuerung und Halsen-Funktion über die Tasten.

### 4.2 Raymarine — iNstrument-Serie

#### 4.2.1 i70s Multifunktions-Instrument

| Parameter | Wert |
|-----------|------|
| Display | 4" TFT-Farbdisplay, 320 × 240 px |
| Helligkeit | 1000 cd/m², tageslicht-tauglich |
| Datenseiten | Bis 8, frei konfigurierbar |
| Felder pro Seite | 1–4 |
| Bus | SeaTalkng (NMEA 2000 kompatibel) |
| Besonderheit | LightHouse-Stil, konsistent mit Axiom MFD |
| Autopilot | Steuerung von Evolution-Autopiloten |
| Alarme | Tiefe, Geschwindigkeit, Wind, Temperatur, benutzerdefiniert |
| Strom | 3 W bei 12V |
| Schutzklasse | IPX6 |
| Einbau | Bündig oder Aufputz |
| Preis (UVP) | ca. 440 € |

#### 4.2.2 Raymarine Wind-Sensoren

**Raymarine iTC-5 (Instrument Transducer Converter):**
Wandelt analoge Signale klassischer Raymarine-Geber (Rotavecta-Wind, ST60-Sensoren) in SeaTalkng/NMEA 2000 um:

| Parameter | Wert |
|-----------|------|
| Eingänge | 2× Wind, 1× Speed, 1× Temp, 1× Tiefe |
| Ausgang | SeaTalkng (NMEA 2000) |
| Kalibrierung | Über i70s Display |
| Strom | 1 W |
| Preis (UVP) | ca. 250 € |

### 4.3 Garmin — Marine Instruments

#### 4.3.1 GNX-Serie

**GNX 20 (4" Sailing-Instrument):**

| Parameter | Wert |
|-----------|------|
| Display | 4" IPX7, 640 × 480 px |
| Helligkeit | 1200 cd/m² |
| Segelfunktionen | Wind, VMG, Laylines, Startlinie |
| Bus | NMEA 2000 |
| Alarme | Konfigurierbar |
| Preis (UVP) | ca. 400 € |

**GNX 120/130 (7" Großformat-Instrument):**

| Parameter | GNX 120 | GNX 130 |
|-----------|---------|---------|
| Display | 7" LCD, 800 × 480 | 7" LCD, 800 × 480 |
| Layout | Bis 8 Felder | Bis 8 Felder + Grafiken |
| Segeldaten | Nein (Motor-fokussiert) | Ja (Wind, Polar, VMG) |
| Preis (UVP) | ca. 700 € | ca. 700 € |

#### 4.3.2 Garmin GST 43 (Smart Transducer)

| Parameter | Wert |
|-----------|------|
| Sensoren | Geschwindigkeit (Paddle-Wheel) + Temperatur |
| Ausgang | NMEA 2000 (direkt, kein Adapter nötig) |
| Durchbruch | 50 mm Standard |
| Material | Kunststoff (Thru-Hull) |
| Kalibrierung | Über GNX-Display oder Garmin MFD |
| Preis (UVP) | ca. 200 € |

#### 4.3.3 Garmin gWind / gWind Wireless

**gWind (kabelgebunden):**

| Parameter | Wert |
|-----------|------|
| Messprinzip | Schalenkreuz + Windfahne |
| Windgeschwindigkeit | 0–70 kn |
| Windrichtung | 0°–360° |
| Genauigkeit | ±3° Richtung, ±5 % Geschwindigkeit |
| Ausgang | NMEA 2000 |
| Kabel | 25 m mitgeliefert |
| Preis (UVP) | ca. 350 € |

**gWind Wireless:**

| Parameter | Wert |
|-----------|------|
| Messprinzip | Schalenkreuz + Windfahne |
| Funk | ANT+ (2,4 GHz) |
| Reichweite | 15 m (typisch) |
| Stromversorgung | 3× AAA-Batterien (1 Jahr bei 8 h/Tag) |
| Empfänger | GNX Wind-Display oder GND 10 Gateway |
| Preis (UVP) | ca. 500 € |

### 4.4 Simrad — IS42 Digital Display

| Parameter | Wert |
|-----------|------|
| Display | 4,1" Sunlight-visible LCD |
| Auflösung | 230 × 230 px |
| Seiten | Bis 6 konfigurierbar |
| Felder | 1–3 pro Seite |
| Bus | NMEA 2000 (SimNet-kompatibel) |
| Autopilot | AP44/AP48 Steuerung |
| Segelfunktionen | Wind, VMG, Steuerkurs |
| Strom | 0,3 W |
| Schutzklasse | IPX7 |
| Preis (UVP) | ca. 360 € |

**Besonderheit:** Simrad IS42 ist technisch nahezu identisch mit B&G Triton2 (gleicher Navico-Konzern), unterscheidet sich aber in der Software — IS42 ist auf Motorboote optimiert, Triton2 auf Segelboote.

### 4.5 Furuno — FI-70 Instrument

| Parameter | Wert |
|-----------|------|
| Display | 4,1" TFT-Farb-LCD |
| Auflösung | 320 × 240 px |
| Helligkeit | 1000 cd/m² |
| Datenseiten | Bis 10, frei konfigurierbar |
| Felder | 1–4 pro Seite |
| Bus | NMEA 2000 (CAN-Bus) |
| Besonderheit | Kompatibel mit allen Furuno NavNet TZtouch MFDs |
| Alarme | Tiefe, Geschwindigkeit, Temperatur, benutzerdefiniert |
| Strom | 3,6 W |
| Schutzklasse | IP56 |
| Preis (UVP) | ca. 500 € |

**Furuno FI-50 (Single-Function Displays):**
Separate Rundanzeigen für jeweils eine Funktion:

| Modell | Funktion | Preis (UVP) |
|--------|---------|-------------|
| FI-501 | Tiefe | ca. 400 € |
| FI-503 | Speed | ca. 400 € |
| FI-504 | Wind (analog) | ca. 550 € |
| FI-506 | Compass (analog) | ca. 500 € |

### 4.6 NASA Marine — Budget-Instrumentierung

**NASA Marine Clipper:**
Einfache, preiswerte Einzelinstrumente für kleine Yachten und Nachrüstung:

| Modell | Funktion | Display | Bus | Preis (UVP) |
|--------|---------|---------|-----|-------------|
| Clipper Wind | AWA/AWS | LCD, 95×65 mm | Proprietär | ca. 250 € |
| Clipper Duet | Tiefe + Speed | LCD, 95×65 mm | Proprietär | ca. 300 € |
| Clipper Depth | Tiefe | LCD, 60×40 mm | Proprietär | ca. 180 € |
| Clipper Log | Speed + Trip | LCD, 60×40 mm | Proprietär | ca. 200 € |

**NASA Marine Target:**
Mittlere Preisklasse mit NMEA-0183-Ausgang:

| Modell | Funktion | Bus | Preis (UVP) |
|--------|---------|-----|-------------|
| Target Wind | AWA/AWS | NMEA 0183 | ca. 350 € |
| Target 2 | Tiefe + Speed + Temp | NMEA 0183 | ca. 400 € |
| Target Compass | Heading | NMEA 0183 | ca. 300 € |

**Bewertung NASA Marine:**
- Preis-Leistung: Sehr gut für Einsteiger und kleine Boote
- Qualität: Ausreichend, Lebensdauer 5–8 Jahre
- Integration: Begrenzt — proprietärer Bus, NMEA 0183 maximal
- Upgrade-Pfad: Keiner — Systemwechsel bei Aufrüstung nötig
- Geber: Einfache Paddle-Wheel und Transducer, nicht austauschbar

---

## 5. Hersteller-Datenbank

### 5.1 B&G (Navico / Brunswick Corporation)

| Feld | Wert |
|------|------|
| Gründung | 1956 (als Brookes & Gatehouse, Oxford, UK) |
| Hauptsitz | Egham, Surrey, UK |
| Mutterkonzern | Navico Group (seit 2009), Brunswick Corporation (seit 2021) |
| Spezialisierung | Segelsport-Instrumentierung, Regatta-Elektronik |
| Marktposition | Marktführer Segel-Instrumente (geschätzt 40–50 % Marktanteil bei Regattayachten) |
| Preissegment | Mittel bis Premium |
| Service | Weltweites Händlernetz, Online-Konfigurationstools |
| Website | www.bandg.com |

**Produktfamilien:**

| Familie | Segment | Bus | Besonderheit |
|---------|---------|-----|------------|
| H5000 | Regatta/Offshore | NMEA 2000 + Ethernet | Professionelle Kalibrierung, Logging |
| Triton2 | Fahrtenyacht | NMEA 2000 | Autopilot-Steuerung, erschwinglich |
| Nemesis | Großformat | NMEA 2000 | 6,5" Display für Ablesbarkeit |
| WS320 | Windgeber | NMEA 2000 / WiFi | Ultraschall, drahtlos möglich |
| ZG100 | GPS/Heading | NMEA 2000 | GPS-Antenne mit Heading |

**AYDI-Bewertung:**

| Kriterium | Score | Begründung |
|-----------|-------|-----------|
| Segel-Performance | 95/100 | Industriestandard für Regatta |
| Motorboot-Eignung | 60/100 | Segelfokus, Motorboot-Features begrenzt |
| Preis-Leistung | 75/100 | Premium-Preis, aber entsprechende Qualität |
| Nachrüstbarkeit | 85/100 | NMEA 2000, gute Dokumentation |
| Langzeit-Support | 80/100 | Navico-Übernahmen bergen Risiko |

### 5.2 Raymarine (FLIR Systems / Teledyne)

| Feld | Wert |
|------|------|
| Gründung | 1923 (als Kelvin Hughes), 1997 als Raymarine |
| Hauptsitz | Fareham, Hampshire, UK |
| Mutterkonzern | Teledyne Technologies (seit 2020, vorher FLIR Systems 2010–2020) |
| Spezialisierung | Marine-Elektronik Vollsortiment |
| Marktposition | Nummer 2–3 weltweit, stark bei Motor-/Fahrtenyachten |
| Preissegment | Mittel |
| Service | Weltweites Händlernetz, YachtSense-Plattform |
| Website | www.raymarine.com |

**Produktfamilien:**

| Familie | Segment | Bus | Besonderheit |
|---------|---------|-----|------------|
| i70s | Instrument | SeaTalkng (NMEA 2000) | Universelles Display, Motor + Segel |
| iTC-5 | Transducer-Converter | SeaTalkng | Analoggeber → NMEA 2000 |
| Evolution | Autopilot | SeaTalkng | AI-basierte Steuerung |
| Axiom | MFD | SeaTalkng + Ethernet | Kartenplotter mit Instrument-Pages |
| Quantum | Radar | Ethernet | CHIRP-Radar |

**AYDI-Bewertung:**

| Kriterium | Score | Begründung |
|-----------|-------|-----------|
| Segel-Performance | 65/100 | Grundfunktionen ok, kein Performance-Fokus |
| Motorboot-Eignung | 85/100 | Stark in Motorboot-Integration |
| Preis-Leistung | 80/100 | Gutes Preisniveau |
| Nachrüstbarkeit | 90/100 | SeaTalkng = NMEA 2000, iTC-5 für Legacy |
| Langzeit-Support | 75/100 | Mehrfache Übernahmen, Support war gut |

### 5.3 Garmin

| Feld | Wert |
|------|------|
| Gründung | 1989 (Lenexa, Kansas) |
| Hauptsitz | Olathe, Kansas, USA |
| Spezialisierung | GPS/Navigation (alle Segmente), Marine seit ~2000 |
| Marktposition | Weltweit Nr. 1–2 bei Marine-Elektronik gesamt |
| Preissegment | Mittel |
| Service | Weltweites Händlernetz, umfangreiche Online-Ressourcen |
| Website | www.garmin.com/marine |

**Produktfamilien Instrumente:**

| Familie | Segment | Bus | Besonderheit |
|---------|---------|-----|------------|
| GNX 20/21 | Segeldisplay | NMEA 2000 | Sail-Racing-Funktionen |
| GNX 120/130 | Großformat | NMEA 2000 | 7" Ablesbarkeit |
| GMI 20 | Universal | NMEA 2000 | Farb-TFT, Marine-Standard |
| GST 43 | Smart Transducer | NMEA 2000 | Speed + Temp, kein Adapter nötig |
| gWind | Windgeber | NMEA 2000 / ANT+ | Kabelgebunden + Wireless |
| GND 10 | NMEA-Bridge | NMEA 2000 ↔ 0183 | Gateway |

**AYDI-Bewertung:**

| Kriterium | Score | Begründung |
|-----------|-------|-----------|
| Segel-Performance | 70/100 | GNX-Segelfunktionen solide, aber kein H5000 |
| Motorboot-Eignung | 90/100 | Hervorragende Motor-Integration |
| Preis-Leistung | 85/100 | Gutes Preisniveau, viel Funktion |
| Nachrüstbarkeit | 90/100 | NMEA 2000 durchgängig |
| Langzeit-Support | 90/100 | Finanziell stabil, guter Update-Zyklus |

### 5.4 Simrad (Navico / Brunswick Corporation)

| Feld | Wert |
|------|------|
| Gründung | 1947 (Horten, Norwegen) |
| Hauptsitz | Egham, UK (Navico-Hauptsitz) |
| Mutterkonzern | Navico Group / Brunswick Corporation |
| Spezialisierung | Marine-Elektronik, Fischfinder, Motorboot |
| Marktposition | Stark bei Sport- und Motorbooten, kommerzieller Fischerei |
| Preissegment | Mittel |
| Website | www.simrad-yachting.com |

**AYDI-Bewertung:**

| Kriterium | Score | Begründung |
|-----------|-------|-----------|
| Segel-Performance | 55/100 | Motorboot-Fokus, Segeldaten via B&G-Plattform |
| Motorboot-Eignung | 90/100 | Kernkompetenz |
| Preis-Leistung | 80/100 | Gutes Preisniveau |
| Nachrüstbarkeit | 85/100 | NMEA 2000, SimNet |
| Langzeit-Support | 80/100 | Navico/Brunswick stabil |

### 5.5 Furuno

| Feld | Wert |
|------|------|
| Gründung | 1948 (Nishinomiya, Japan) |
| Hauptsitz | Nishinomiya, Hyogo, Japan |
| Spezialisierung | Marine-Elektronik, Radar, Echolote, kommerzielle Schifffahrt |
| Marktposition | Weltweit Nr. 1 bei kommerzieller Marine-Elektronik |
| Preissegment | Mittel bis Premium |
| Service | Weltweites Händlernetz, hervorragender Langzeit-Support |
| Website | www.furuno.com |

**AYDI-Bewertung:**

| Kriterium | Score | Begründung |
|-----------|-------|-----------|
| Segel-Performance | 50/100 | Kommerzielle DNA, wenig Segel-spezifisch |
| Motorboot-Eignung | 85/100 | Hervorragend für Fahrtenyachten |
| Preis-Leistung | 70/100 | Premium-Preis, aber Langlebigkeit |
| Nachrüstbarkeit | 75/100 | NMEA 2000, aber proprietäre Tendenzen |
| Langzeit-Support | 95/100 | Legendärer Langzeit-Support, Ersatzteile über Jahrzehnte |

### 5.6 NASA Marine

| Feld | Wert |
|------|------|
| Gründung | 1990 (Stevenage, UK) |
| Hauptsitz | Stevenage, Hertfordshire, UK |
| Spezialisierung | Budget-Marine-Instrumente |
| Marktposition | Einstiegsmarkt, Nachrüstung kleiner Yachten |
| Preissegment | Budget bis Mittel |
| Website | www.nasamarine.com |

**AYDI-Bewertung:**

| Kriterium | Score | Begründung |
|-----------|-------|-----------|
| Segel-Performance | 35/100 | Grundfunktionen, keine Performance-Analyse |
| Motorboot-Eignung | 50/100 | Basis-Instrumente ausreichend |
| Preis-Leistung | 90/100 | Unschlagbar günstig |
| Nachrüstbarkeit | 40/100 | Proprietärer Bus, NMEA 0183 max. |
| Langzeit-Support | 50/100 | Kleine Firma, Ersatzteile begrenzt |

### 5.7 Airmar (OEM-Geber)

| Feld | Wert |
|------|------|
| Gründung | 1982 (Milford, New Hampshire, USA) |
| Hauptsitz | Milford, NH, USA |
| Spezialisierung | OEM-Geber (Transducer) für alle großen Marken |
| Marktposition | Welt-Marktführer bei Marine-Gebern |
| Preissegment | Mittel |
| Website | www.airmar.com |

**Bedeutung:** Airmar liefert die Geber (Lot, Log, Temperatur) für praktisch alle Instrumentenhersteller. Wenn auf einem Boot ein Garmin-, Raymarine- oder B&G-Logge verbaut ist, stammt der Geber oft von Airmar. Die Airmar-Modellnummer ist der Schlüssel zur Ersatzteilbeschaffung und Kompatibilitätsprüfung.

**Wichtige Airmar-Geber:**

| Modell | Typ | Sensoren | Frequenz | Anschluss |
|--------|-----|----------|----------|-----------|
| B45 | Thru-Hull Bronze | Tiefe | 200 kHz | Verschieden |
| P79 | In-Hull Kunststoff | Tiefe | 200 kHz | Verschieden |
| B744V | Thru-Hull Bronze | Tiefe + Speed + Temp | 200 kHz | Verschieden |
| DST800 | Thru-Hull Smart | Tiefe + Speed + Temp | 235 kHz CHIRP | NMEA 2000 |
| DX900+ | Thru-Hull Smart | Tiefe + Speed + Temp | CHIRP | NMEA 2000 |
| 220WX | Masttop | Wind + GPS + Kompass | — | NMEA 0183/2000 |
| PB200 | Masttop | Wind + GPS + Heading | — | NMEA 0183/2000 |

### 5.8 Yacht Devices

| Feld | Wert |
|------|------|
| Gründung | 2012 (Tallinn, Estland) |
| Hauptsitz | Tallinn, Estland |
| Spezialisierung | NMEA-2000-Gateways, Adapter, Sensoren |
| Marktposition | Nischenhersteller, Integrationslösungen |
| Preissegment | Budget bis Mittel |
| Website | www.yachtd.com |

**Produkte:**

| Modell | Funktion | Preis (UVP) |
|--------|---------|-------------|
| YDWG-02 | NMEA 2000 → WiFi Gateway | ca. 180 € |
| YDBM-01 | Batteriemonitor | ca. 220 € |
| YDTC-13 | Temperatur-Sensoren (13 Kanäle) | ca. 170 € |
| YDBC-05 | Barometer | ca. 160 € |
| YDAB-01 | Alarm-Bridge | ca. 100 € |
| YDCC-04 | Current/Voltage Sensor | ca. 150 € |

---

## 6. Fehlerbild-Atlas

### 6.1 Fehlerbild FB-INST-001: Windgeber zeigt konstant 0 kn

**Symptom:** Die Windgeschwindigkeitsanzeige zeigt dauerhaft 0 kn, unabhängig von der tatsächlichen Windstärke. Windrichtung funktioniert möglicherweise noch.

**Mögliche Ursachen:**

| Rang | Ursache | Wahrscheinlichkeit | Prüfung |
|------|---------|-------------------|---------|
| 1 | Schalenkreuz blockiert (Vogelkot, Eisbildung) | 35 % | Visuell vom Deck aus (Fernglas) |
| 2 | Kabelbruch in der Mastzuführung | 25 % | Widerstandsmessung am Fuß des Mastes |
| 3 | Korrision im Masttopp-Stecker | 20 % | Stecker öffnen, visuell prüfen |
| 4 | Lager des Schalenkreuzes fest | 10 % | Schalenkreuz von Hand drehen — muss leichtgängig sein |
| 5 | Elektronikdefekt im Display/Prozessor | 5 % | Anderen Sensor anschließen |
| 6 | NMEA-2000-Bus-Problem | 5 % | Gerätliste im Display prüfen — erscheint der Windgeber? |

**Confidence:** documented (häufigstes Fehlerbild, vielfach in Praxis bestätigt)

**AYDI-Relevanz:** Dieser Fehler macht die gesamte Windkette unbrauchbar — kein AWA, kein AWS, kein TWA, kein TWS. Die Performance-Analyse ist auf visuelle Einschätzung beschränkt.

### 6.2 Fehlerbild FB-INST-002: Echolot zeigt unrealistische Tiefen oder springt

**Symptom:** Die Tiefenanzeige springt zwischen extremen Werten (z. B. 2,3 m → 85 m → 0,5 m) oder zeigt Fixwerte wie 0,0 m oder 999 m.

**Mögliche Ursachen:**

| Rang | Ursache | Wahrscheinlichkeit | Prüfung |
|------|---------|-------------------|---------|
| 1 | Bewuchs auf der Geberfläche | 30 % | Boot trockenfallen lassen oder tauchen lassen |
| 2 | Luftblasen am Geber (bei Fahrt) | 20 % | Tritt nur bei Fahrt >5 kn auf? Bei Stillstand korrekt? |
| 3 | Einschwinger: Lufteinschluss im Klebstoff | 15 % | Epoxid-Schicht prüfen, ggf. erneuern |
| 4 | Kabeldefekt oder lose Verbindung | 15 % | Kabel und Stecker prüfen |
| 5 | Geber-Kristall defekt | 10 % | Geber durch bekannten funktionierenden ersetzen |
| 6 | Interferenz mit anderen Gebern | 5 % | Andere Echolote/Geber abschalten |
| 7 | Falsche Frequenzeinstellung | 5 % | 200 kHz für Flachwasser, 50 kHz für Tiefwasser prüfen |

**Confidence:** documented

### 6.3 Fehlerbild FB-INST-003: Logge zeigt zu niedrige Geschwindigkeit

**Symptom:** Die angezeigte STW ist systematisch 20–50 % niedriger als GPS-SOG bei Stillwasser.

**Mögliche Ursachen:**

| Rang | Ursache | Wahrscheinlichkeit | Prüfung |
|------|---------|-------------------|---------|
| 1 | Bewuchs am Paddle-Wheel | 40 % | Geber herausziehen, Schaufelrad prüfen |
| 2 | Kalibrierfaktor zu niedrig | 25 % | GPS-SOG und STW über 10 min vergleichen |
| 3 | Schaufelrad-Lager schwergängig | 15 % | Schaufelrad von Hand drehen — leichtgängig? |
| 4 | Ungünstiger Einbauort (Turbulenzzone) | 10 % | Prüfen: Kiel-Nachlauf, Strut, Borddurchlass in der Nähe |
| 5 | Magnet im Schaufelrad geschwächt | 5 % | Impulse pro Umdrehung zählen |
| 6 | Elektronikfehler | 5 % | Bekannten Geber anschließen |

**Confidence:** documented

### 6.4 Fehlerbild FB-INST-004: Barograph zeigt konstanten Druck (keine Änderung)

**Symptom:** Der Barograph zeichnet eine horizontale Linie auf — keinerlei Druckänderung über Stunden oder Tage, obwohl sich das Wetter ändert.

**Mögliche Ursachen:**

| Rang | Ursache | Wahrscheinlichkeit | Prüfung |
|------|---------|-------------------|---------|
| 1 | Drucksensor defekt (MEMS-Membran) | 35 % | Referenzbarometer daneben halten |
| 2 | Software-Bug (Anzeige aktualisiert nicht) | 25 % | Gerät aus/ein, Firmware-Version prüfen |
| 3 | Belüftungsbohrung verstopft | 20 % | Prüfen ob Gehäuse belüftet ist |
| 4 | Abtastrate auf >1 h gestellt | 15 % | Konfiguration prüfen |
| 5 | Datenspeicher voll | 5 % | Log löschen und neu aufzeichnen |

**Confidence:** documented

### 6.5 Fehlerbild FB-INST-005: Tankgeber zeigt immer „voll"

**Symptom:** Die Tankanzeige zeigt unabhängig vom tatsächlichen Füllstand immer 100 % oder den maximalen Wert.

**Mögliche Ursachen:**

| Rang | Ursache | Wahrscheinlichkeit | Prüfung |
|------|---------|-------------------|---------|
| 1 | Schwimmer klemmt (aufgequollen, verformt) | 30 % | Geber ausbauen, Schwimmer-Beweglichkeit prüfen |
| 2 | Kabelkurzschluss (bei 0–180 Ω = Kurzschluss = voll) | 25 % | Kabel abklemmen, Widerstand am Geber messen |
| 3 | Falscher Widerstandsbereich konfiguriert | 20 % | Europäisch (0–180 Ω) vs. US (240–33 Ω) prüfen |
| 4 | Ablagerungen blockieren Führungsstange | 15 % | Geber ausbauen, reinigen |
| 5 | Geber zu kurz für Tanktiefe | 10 % | Einbaulänge vs. Tanktiefe vergleichen |

**Confidence:** documented

### 6.6 Fehlerbild FB-INST-006: Kompass weicht nach Einbau neuer Geräte ab

**Symptom:** Nach dem Einbau eines neuen elektrischen Geräts (Lautsprecher, Bordcomputer, Winsch-Motor) weicht der elektronische Kompass um 5°–30° ab.

**Mögliche Ursachen:**

| Rang | Ursache | Wahrscheinlichkeit | Prüfung |
|------|---------|-------------------|---------|
| 1 | Magnetische Störung durch neues Gerät | 50 % | Neues Gerät abschalten — ändert sich der Kurs? |
| 2 | Kabelführung nahe Kompass geändert | 25 % | Gleichstromkabel mit hohem Strom in Kompassnähe? |
| 3 | Neukompensation erforderlich | 20 % | Kompensationsroutine im Display starten |
| 4 | Eisenhaltiger Gegenstand in Kompassnähe platziert | 5 % | Metallische Gegenstände in 1 m Umkreis entfernen |

**Confidence:** documented

### 6.7 Fehlerbild FB-INST-007: NMEA-2000-Netzwerk: Sensor erscheint nicht

**Symptom:** Ein neu installierter NMEA-2000-Sensor erscheint nicht in der Geräteliste des Displays oder MFDs.

**Mögliche Ursachen:**

| Rang | Ursache | Wahrscheinlichkeit | Prüfung |
|------|---------|-------------------|---------|
| 1 | T-Stück nicht richtig eingerastet | 30 % | Alle Steckverbindungen lösen und neu stecken |
| 2 | Backbone-Terminierung fehlt oder doppelt | 25 % | Genau 2 Terminierungswiderstände im Netzwerk? |
| 3 | Stromversorgung am Backbone fehlt | 15 % | 12V am Backbone messen (Pin 1 und 4) |
| 4 | Stich-Leitung zu lang (>6 m) | 10 % | NMEA-2000-Standard: max. 6 m Stichleitung |
| 5 | Defektes Kabel oder T-Stück | 10 % | Tauschen und testen |
| 6 | Inkompatibilität (seltener PGN) | 5 % | Hersteller-Kompatibilitätsliste prüfen |
| 7 | Backbone-Gesamtlänge >100 m | 5 % | NMEA-2000-Standard: max. 100 m Backbone |

**Confidence:** documented

### 6.8 Fehlerbild FB-INST-008: Ultraschall-Windgeber — Phantom-Wind bei Regen

**Symptom:** Der Ultraschall-Windgeber zeigt bei starkem Regen oder Gischt Windgeschwindigkeiten an, die 5–15 kn höher sind als tatsächlich vorhanden, oder die Windrichtung springt erratisch.

**Mögliche Ursachen:**

| Rang | Ursache | Wahrscheinlichkeit | Prüfung |
|------|---------|-------------------|---------|
| 1 | Regentropfen brechen Ultraschall-Pfad | 40 % | Symptom nur bei Regen/Gischt? |
| 2 | Salzablagerungen auf Transducern | 25 % | Transducer-Flächen reinigen (Frischwasser) |
| 3 | Firmware veraltet (bessere Regenfilter in Updates) | 20 % | Firmware-Version prüfen, Update installieren |
| 4 | Sensor mechanisch beschädigt (Riss in Schutzkappe) | 10 % | Visuell prüfen |
| 5 | Eisbildung auf Transducern | 5 % | Nur bei Frostbedingungen relevant |

**Confidence:** documented

### 6.9 Fehlerbild FB-INST-009: Wassertemperatur springt beim Ankern

**Symptom:** Die angezeigte Wassertemperatur schwankt beim Ankern um ±2–5°C, obwohl die tatsächliche Temperatur stabil ist.

**Mögliche Ursachen:**

| Rang | Ursache | Wahrscheinlichkeit | Prüfung |
|------|---------|-------------------|---------|
| 1 | Thermokline (Temperaturschichtung) | 40 % | Normal in Sommermonaten, Ankerlage bei 5–15 m |
| 2 | Sonneneinstrahlung auf Rumpf heizt Geber | 25 % | Südseite des Rumpfes? Dunkler Rumpf? |
| 3 | Kühlwasserausstoß des Motors erwärmt Geber | 20 % | Tritt nur bei laufendem Motor auf? |
| 4 | Süßwassereintrag (Flussmündung) | 10 % | Gezeitenabhängig? |
| 5 | Defekter Geber | 5 % | Referenzthermometer vergleichen |

**Confidence:** estimated

### 6.10 Fehlerbild FB-INST-010: GPS-SOG weicht stark von Log-STW ab (ohne Strom)

**Symptom:** In einem Revier ohne bekannten Strom zeigt GPS-SOG konstant 1–3 kn mehr oder weniger als die Logge (STW).

**Mögliche Ursachen:**

| Rang | Ursache | Wahrscheinlichkeit | Prüfung |
|------|---------|-------------------|---------|
| 1 | Logge nicht kalibriert | 40 % | Kalibrierfaktor prüfen, Vergleichsfahrt |
| 2 | Unbekannter Strom (doch vorhanden) | 25 % | Seekarte prüfen, Tiden-Atlas konsultieren |
| 3 | Bewuchs am Log-Geber | 15 % | Geber prüfen |
| 4 | GPS-Multipath (Hafen, enge Bucht) | 10 % | HDOP prüfen (>2,0 = schlecht) |
| 5 | GPS-Antenne schlecht positioniert | 5 % | Freie Sicht zum Himmel? Abschattung? |
| 6 | Log-Geber in Turbulenzzone | 5 % | Einbauort prüfen |

**Confidence:** documented

### 6.11 Fehlerbild FB-INST-011: Display-Ausfall bei Kälte

**Symptom:** Ein oder mehrere Instrumenten-Displays werden bei Temperaturen unter 0°C unleserlich, reagieren träge oder fallen ganz aus.

**Mögliche Ursachen:**

| Rang | Ursache | Wahrscheinlichkeit | Prüfung |
|------|---------|-------------------|---------|
| 1 | LCD-Betriebstemperatur unterschritten | 45 % | Datenblatt prüfen — typisch -15°C bis +55°C |
| 2 | Kondenswasser im Display gefroren | 25 % | Display langsam aufwärmen, Beschlag innen? |
| 3 | Spannung zu niedrig (Batterie bei Kälte) | 15 % | Bordspannung messen — unter 10,5 V? |
| 4 | Kabelverbindung spröde/gebrochen | 10 % | Steckverbindungen prüfen |
| 5 | Display-Controller defekt | 5 % | Erwärmen — erholt sich das Display? |

**Confidence:** documented

### 6.12 Fehlerbild FB-INST-012: NMEA-2000-Netzwerk instabil — Geräte fallen periodisch aus

**Symptom:** Geräte im NMEA-2000-Netzwerk verschwinden periodisch aus der Geräteliste und tauchen nach Sekunden oder Minuten wieder auf. Daten fallen zeitweise aus.

**Mögliche Ursachen:**

| Rang | Ursache | Wahrscheinlichkeit | Prüfung |
|------|---------|-------------------|---------|
| 1 | Unterdimensionierte Stromversorgung | 30 % | Spannung am Backbone bei Last messen (min. 9 V) |
| 2 | Korrodierte Steckverbindungen | 25 % | Alle T-Stücke und Verbindungen visuell prüfen |
| 3 | EMV-Störungen (Motor, Inverter, Funk) | 15 % | Tritt Ausfall nur bei bestimmten Geräten auf? |
| 4 | Backbone zu lang ohne Repeater | 10 % | Gesamtlänge >100 m? Stichleitungen >6 m? |
| 5 | Defektes T-Stück (partielle Verbindung) | 10 % | T-Stücke tauschen |
| 6 | Terminierung fehlt/doppelt/dreifach | 10 % | Genau 2 × 120 Ω an den Enden? |

**Confidence:** documented

---

## 7. Troubleshooting-Entscheidungsbäume

### 7.1 Entscheidungsbaum: Windgeber-Fehlersuche

```
START: Windanzeige zeigt keine oder falsche Werte
│
├── Windgeschwindigkeit = 0 und Windrichtung = 0?
│   ├── JA → Kein Signal vom Geber
│   │   ├── NMEA-2000-Gerät sichtbar im Netzwerk?
│   │   │   ├── JA → Geber wird erkannt, sendet aber keine Daten
│   │   │   │   ├── Ultraschall-Geber? → Transducer verschmutzt? Reinigen
│   │   │   │   ├── Mechanisch? → Schalenkreuz und Fahne blockiert? → Prüfen
│   │   │   │   └── Firmware-Update verfügbar? → Installieren
│   │   │   └── NEIN → Geber nicht im Netzwerk
│   │   │       ├── Spannung am Geber? (12V an NMEA-2000-Backbone)
│   │   │       │   ├── JA → Kabel zum Geber prüfen (Durchgang, Isolation)
│   │   │       │   │   ├── Kabel OK → Geber defekt → Austauschen
│   │   │       │   │   └── Kabel defekt → Kabel erneuern
│   │   │       │   └── NEIN → Backbone-Stromversorgung prüfen
│   │   │       │       ├── Sicherung? → Prüfen/Tauschen
│   │   │       │       └── Batteriespannung? → Unter 10,5 V → Laden
│   │   │       └── Wireless-Geber? → WiFi/ANT+ Verbindung prüfen
│   │   │           ├── Akku leer? → Laden (Solar prüfen)
│   │   │           ├── Pairing verloren? → Neu pairen
│   │   │           └── Zu weit entfernt? → Empfänger-Position prüfen
│   │
│   └── NEIN → Teilweises Signal
│       ├── Nur AWS = 0, AWA funktioniert?
│       │   ├── Mechanisch: Schalenkreuz fest, Fahne frei → Lager/Schalen prüfen
│       │   └── Ultraschall: Ein Transducer-Paar defekt → Geber tauschen
│       └── Nur AWA = 0, AWS funktioniert?
│           ├── Mechanisch: Fahne blockiert oder Potentiometer defekt
│           └── Ultraschall: Anderes Transducer-Paar defekt → Geber tauschen
│
├── Windwerte springen erratisch?
│   ├── Bei Regen/Gischt? → Ultraschall-Regenproblem → Firmware-Update
│   ├── Bei Seegang? → Krängungskorrektur prüfen → Heel-Sensor ok?
│   ├── Nur bei Motorbetrieb? → EMV-Störung → Kabelführung prüfen
│   └── Immer? → Kabeldefekt (partielle Verbindung) oder Geber-Elektronik
│
└── Wahrer Wind (TWA/TWS) falsch, scheinbarer Wind (AWA/AWS) korrekt?
    ├── Log (STW) prüfen — stimmt STW?
    │   ├── NEIN → Log-Problem lösen (siehe Baum 7.2)
    │   └── JA → Kompass (HDG) prüfen — stimmt HDG?
    │       ├── NEIN → Kompass-Problem lösen (siehe Baum 7.4)
    │       └── JA → Windprozessor-Kalibrierung prüfen
    │           ├── Upwash-Tabelle korrekt?
    │           ├── Mastbiegungs-Korrektur aktiv?
    │           └── Heel-Korrektur aktiv?
```

### 7.2 Entscheidungsbaum: Logge/Geschwindigkeitsmessung

```
START: Geschwindigkeitsanzeige (STW) zeigt keine oder falsche Werte
│
├── STW = konstant 0?
│   ├── Paddle-Wheel-Geber?
│   │   ├── Geber herausziehen (Blindstopfen bereithalten!)
│   │   │   ├── Schaufelrad dreht frei? → Kabel/Elektronik prüfen
│   │   │   └── Schaufelrad blockiert → Reinigen (Bewuchs, Fremdkörper)
│   │   └── Geber im Display erkannt? (NMEA-2000-Geräteliste)
│   │       ├── JA → Geber erkannt, kein Signal → Magnet/Hall-Sensor defekt
│   │       └── NEIN → NMEA-2000-Verbindung prüfen (siehe Baum 7.5)
│   ├── Ultraschall-Geber?
│   │   ├── Bewuchs auf Transducer-Flächen? → Reinigen
│   │   ├── Luftblasen am Geber? → Einbauort prüfen, Turbulenzen?
│   │   └── Geber im Netzwerk sichtbar? → NMEA-Verbindung prüfen
│   └── GPS-SOG als Ersatz verfügbar? → Temporär umschalten
│
├── STW systematisch zu niedrig?
│   ├── Bewuchs am Geber (auch partiell)? → Reinigen
│   ├── Kalibrierfaktor prüfen → Vergleichsfahrt mit GPS-SOG bei Stillwasser
│   │   ├── Differenz konstant (Prozent)? → Kalibrierfaktor anpassen
│   │   └── Differenz geschwindigkeitsabhängig? → Einbauort prüfen
│   └── Schaufelrad-Lager schwergängig? → Geber reinigen/tauschen
│
├── STW systematisch zu hoch?
│   ├── Kalibrierfaktor zu hoch → Anpassen
│   ├── Geber im Bereich starker Strömung (z. B. Kiel-Nachlauf)? → Versetzen
│   └── Seltener: Fremdimpulse (EMV) → Geschirmtes Kabel prüfen
│
└── STW springt oder ist instabil?
    ├── Nur bei Krängung? → Geber taucht aus Wasser → Lee-Seite prüfen
    ├── Nur bei Welle? → Luft am Geber bei Stampfen → Einbautiefe prüfen
    ├── Immer? → Kabeldefekt (Wackelkontakt) → Stecker/Kabel prüfen
    └── Nur bei Motorbetrieb? → EMV-Störung → Kabel von Motorkabel trennen
```

### 7.3 Entscheidungsbaum: Echolot-Fehlersuche

```
START: Echolot zeigt keine oder falsche Tiefe
│
├── Anzeige = 0 oder keine Tiefe?
│   ├── Geber im Netzwerk sichtbar?
│   │   ├── JA → Geber erkannt, kein Echo
│   │   │   ├── Tiefe >Reichweite des Gebers? → Frequenz wechseln (50 kHz)
│   │   │   ├── Einschwinger: Lufteinschluss in Epoxid? → Geber neu kleben
│   │   │   ├── Sendeleistung auf Minimum? → Erhöhen
│   │   │   └── Bewuchs auf Geberfläche (Thru-Hull)? → Reinigen
│   │   └── NEIN → NMEA-2000/Kabel prüfen
│   │       ├── Spannung am Geber? → Backbone-Stromversorgung
│   │       └── Kabelbruch? → Durchgangsprüfung
│
├── Tiefe springt/ist instabil?
│   ├── Nur bei Fahrt? → Luftblasen am Geber
│   │   ├── Einbauort in Turbulenzzone? → Geber versetzen
│   │   ├── Speed >15 kn? → Fahrtstufen-Problem, Geber-Typ prüfen
│   │   └── Ventilation bei Krängung? → Geber tiefer montieren
│   ├── Auch bei Stillstand? → Geber oder Elektronik defekt
│   │   ├── Harter Grund (Fels)? → Echostreuung normal
│   │   ├── Dichtes Seegras? → Echostreuung normal
│   │   └── Geber-Kristall degradiert? → Geber tauschen
│   └── Nur in der Nähe anderer Boote? → Interferenz mit deren Echolot
│       └── Interferenzfilter aktivieren
│
├── Tiefe systematisch falsch (Offset)?
│   ├── Offset-Einstellung prüfen → Geber↔Kiel, Geber↔Wasserlinie
│   ├── Salzgehalt-Einstellung prüfen → Süß-/Salzwasser
│   └── Einschwinger: Rumpfdicke falsch kompensiert? → Nachmessen
│
└── Tiefenalarm löst ohne Grund aus?
    ├── Alarmschwelle zu hoch eingestellt? → Anpassen
    ├── Fische/Schwärme unter dem Boot? → Echo von Fischschwarm
    ├── Thermokline (Temperaturschicht)? → Normal, Filter aktivieren
    └── Gasblasen vom Grund? → Seltenes Phänomen, Ankerlage wechseln
```

### 7.4 Entscheidungsbaum: Kompass-Fehlersuche

```
START: Kompass zeigt falschen Kurs oder ist instabil
│
├── Kurs weicht konstant um X° ab?
│   ├── X° < 5° → Normale Rest-Deviation nach Kompensation
│   │   └── Neukompensation durchführen
│   ├── X° = 5°–30° → Neue magnetische Störquelle
│   │   ├── Neues elektrisches Gerät installiert? → Störquelle identifizieren
│   │   ├── Metallische Gegenstände in Kompassnähe? → Entfernen
│   │   └── Gleichstromkabel in Kompassnähe? → Kabel umverlegen
│   └── X° > 30° → Schwere magnetische Störung
│       ├── Lautsprecher-Magnet in Kompassnähe? → Entfernen
│       ├── Starker Motor/Generator nahe Kompass? → Kompass versetzen
│       └── Kompass-Sensor defekt? → Kompass tauschen
│
├── Kurs driftet langsam?
│   ├── Fluxgate: Temperatur-Drift? → Normal bei billigen Sensoren
│   ├── Gyro-Drift (MEMS-Sensor)? → Sensor-Fusion prüfen, GPS-Heading nutzen
│   └── GPS-Heading: Baseline zu kurz? → Antennenabstand vergrößern
│
├── Kurs springt erratisch (±5°–±20°)?
│   ├── Starker Seegang? → Dampening erhöhen
│   ├── Fluxgate in Vibrationszone? → Sensor versetzen oder dämpfen
│   ├── Elektrisches Rauschen auf dem Bus? → EMV-Filterung prüfen
│   └── Satelliten-Kompass: Wenige Satelliten? → GNSS-Status prüfen
│
└── Kompass reagiert nicht oder zeigt 000°?
    ├── Gerät im NMEA-Netzwerk? → Verbindung prüfen
    ├── Kompass-Kompensation nie durchgeführt? → Durchführen
    └── Sensor-Hardware defekt? → Austauschen
```

### 7.5 Entscheidungsbaum: NMEA-2000-Netzwerk-Diagnose

```
START: NMEA-2000-Netzwerk-Problem
│
├── Kein Gerät erkannt?
│   ├── Backbone-Stromversorgung prüfen
│   │   ├── Sicherung ok? → Spannung messen: 9–16V zwischen Pin 1 (+) und Pin 4 (-)
│   │   │   ├── Spannung ok → Terminierung prüfen
│   │   │   │   ├── 2 Terminatoren (120 Ω) an den Enden? → OK
│   │   │   │   │   └── Backbone-Kabel Durchgang prüfen → defektes Segment ersetzen
│   │   │   │   └── Terminierung fehlt/falsch → 120 Ω Widerstände einsetzen
│   │   │   └── Spannung nicht ok → Stromversorgung reparieren
│   │   └── Sicherung defekt → Tauschen, Kurzschluss suchen
│
├── Einzelnes Gerät fehlt?
│   ├── T-Stück am Gerät prüfen → Einrasten, Kontakte
│   ├── Stichleitung <6 m? → Kürzen oder Gerät näher an Backbone
│   ├── Gerät an anderem T-Stück testen → Ausschlussverfahren
│   └── Gerät an separatem NMEA-2000-Segment testen → Gerät defekt?
│
├── Intermittierende Ausfälle?
│   ├── Stromversorgung stabil? → Spannung unter Last messen
│   │   └── Einbrüche bei Motorstart/Winschen? → Separater Stromkreis
│   ├── Korrosion an Steckern? → Reinigen, Kontaktspray
│   ├── EMV-Störungen? → Backbone nahe Motorkabeln? → Umverlegen
│   └── Zu viele Geräte? → Max. 50 Geräte pro Segment, Strom prüfen
│       └── Gesamtstrom aller Geräte < verfügbare Backbone-Leistung?
│
└── Daten kommen, aber verspätet oder lückenhaft?
    ├── Bus-Auslastung zu hoch? → Selten bei Yacht-Installation
    ├── Firmware-Inkompatibilität? → Alle Geräte updaten
    └── Gateway-Problem (0183↔2000)? → Gateway-Konfiguration prüfen
```

---

## 8. FAQ

### 8.1 Allgemein

**F1: Welche Instrumente braucht eine Yacht als Mindestausrüstung?**
A: Abhängig von der CE-Designkategorie. Für Kategorie A/B (Offshore/Ozean): Kompass, Echolot, Log (STW), Windmesser (AWA/AWS), Barometer, GPS. Für Kategorie C (Küste): Kompass, Echolot, Log. Für Kategorie D (geschütztes Gewässer): Kompass genügt formal, Echolot und Log werden aber dringend empfohlen.

**F2: Was kostet eine komplette Instrumentierung für eine 10-m-Segelyacht?**
A: Budget-System (NASA Marine): 800–1.200 €. Mittelklasse (Garmin GNX + Geber): 1.800–3.000 €. Premium (B&G Triton2 + WS320): 3.000–5.000 €. Regatta (B&G H5000): 6.000–15.000 €. Jeweils ohne MFD/Kartenplotter und ohne Einbau.

**F3: Soll ich NMEA 0183 oder NMEA 2000 installieren?**
A: Bei Neuinstallation immer NMEA 2000 (auch „N2K" oder „SignalK" via Gateway). NMEA 0183 nur, wenn ein einzelnes Legacy-Gerät integriert werden muss. NMEA 2000 bietet Plug-and-Play, Mehrgeräte-Bus, höhere Datenrate und bidirektionale Kommunikation.

**F4: Was ist der Unterschied zwischen SeaTalkng, SimNet und NMEA 2000?**
A: SeaTalkng (Raymarine) und SimNet (Simrad) sind physisch kompatible NMEA-2000-Implementierungen mit proprietären Steckern. Alle drei verwenden das CAN-Bus-Protokoll und die gleichen PGNs. Mit passenden Adapterkabeln (SeaTalkng↔DeviceNet-Micro-C oder SimNet↔Micro-C) sind die Systeme interoperabel.

**F5: Wie oft muss ich meine Instrumente kalibrieren?**
A: Logge (STW): Zu Beginn jeder Saison und nach Antifouling-Erneuerung. Windgeber: Bei Erstinstallation und nach strukturellen Änderungen am Rigg. Kompass: Nach jedem Einbau neuer elektrischer Geräte und zu Saisonbeginn. Echolot: Einmalig bei Installation (Offset), danach stabil. Barometer: Jährlich gegen Referenz abgleichen.

### 8.2 Windmessung

**F6: Ultraschall oder mechanisch — was ist besser?**
A: Ultraschall ist technisch überlegen: keine Anlaufverzögerung, keine beweglichen Teile, höhere Genauigkeit. Nachteil: empfindlicher bei starkem Regen und deutlich teurer. Für Fahrtenyachten ist ein guter mechanischer Geber ausreichend. Für Regatta und Performance-Segeln ist Ultraschall Standard.

**F7: Warum zeigt mein Windmesser bei Flaute manchmal 3–5 kn an?**
A: Mechanische Geber: Restmagnetismus oder Vibration des Mastes erzeugt Schein-Impulse. Ultraschall-Geber: Windgradient am Masttop (Thermik), Mastbewegung bei Dünung, oder Regentropfen stören die Messung. Lösungsansatz: Dampening erhöhen oder Mindest-Geschwindigkeitsschwelle (Noise Gate) im Prozessor einstellen.

**F8: Wie kalibriere ich den wahren Wind?**
A: Die beste Methode ist das Kreissegeln: Bei konstantem Wind (10–20 kn) langsam 360° segeln und auf jedem Kurs AWS/AWA und SOG notieren. Die Upwash-Korrektur wird aus der Asymmetrie zwischen Steuerbord- und Backbord-Kursen berechnet. Professionelle Systeme (H5000) bieten automatische Kalibrierroutinen.

**F9: Was bedeutet „Upwash" und warum ist es für den wahren Wind relevant?**
A: Upwash ist die Ablenkung des Luftstroms durch die Segel. Am Masttop, wo der Windgeber sitzt, ist der Luftstrom bereits durch Groß- und Vorsegel umgelenkt. Die gemessene AWA ist daher systematisch zu hoch (zum Bug hin verzerrt). Die Korrektur beträgt typisch 2°–8° und ist windstärke- und kursabhängig.

**F10: Mein drahtloser Windgeber (B&G WS320) verliert regelmäßig die Verbindung — was tun?**
A: 1) Akku-Ladezustand prüfen (Solarpanel verschmutzt?). 2) WiFi-Kanal am Empfänger wechseln (Interferenz mit Bord-WiFi oder Nachbarbooten im Hafen). 3) Empfänger-Position prüfen — muss Sichtverbindung zum Masttop haben, nicht im Stahl-Kartenraum. 4) Firmware-Update auf Geber und Empfänger.

### 8.3 Echolot

**F11: Warum verliert mein Echolot bei Geschwindigkeiten über 12 kn das Signal?**
A: Bei hoher Fahrt bilden sich Luftblasen unter dem Rumpf, die den Ultraschall-Strahl absorbieren oder reflektieren. Lösung: Geber in einer turbulenzarmen Zone installieren (vorderes Drittel, hinter einer Stufe im Rumpf, die Blasen weglenkt), oder einen Fairing-Block verwenden, der den Geber schräg nach hinten neigt.

**F12: Funktioniert ein Einschwinger (In-Hull-Geber) in einem Sandwichrumpf?**
A: Nein, in der Regel nicht. Die Luft- oder Schaumschicht im Sandwich reflektiert den Ultraschall vollständig. Es gibt spezielle Hochleistungs-Einschwinger, die bei dünnem Sandwich (Gesamtdicke <15 mm) mit reduzierter Leistung funktionieren, aber ein Durchbruchgeber ist die zuverlässigere Lösung.

**F13: Was ist der Unterschied zwischen CHIRP und normalem Echolot?**
A: Ein normales Echolot sendet einen Puls auf einer festen Frequenz (z. B. 200 kHz). CHIRP sendet einen modulierten Sweep über einen Frequenzbereich (z. B. 150–250 kHz). Durch die Korrelationsverarbeitung im Empfänger ergibt sich eine 5–10-fach bessere Auflösung und ein höherer Signal-Rausch-Abstand — das bedeutet bessere Tiefenleistung bei weniger Sendeleistung.

### 8.4 Logge und Geschwindigkeit

**F14: Wie oft muss das Paddle-Wheel gereinigt werden?**
A: In europäischen Gewässern: mindestens monatlich während der Saison, wöchentlich in warmen Gewässern mit starkem Bewuchs. In tropischen Revieren: wöchentlich oder sogar täglich. Tipp: Geber mit herausnehmbarem Paddle-Wheel-Einsatz (z. B. Airmar DST800) ermöglicht Reinigung im Wasser ohne Tauchgang.

**F15: Mein Boot hat keinen Log-Geber — kann ich nur GPS-SOG verwenden?**
A: Für die Navigation ja. Für die Berechnung des wahren Windes ist STW jedoch essentiell — GPS-SOG enthält den Strömungsanteil und führt zu systematischen Fehlern im wahren Wind. Für Motorboote ohne Segelperformance-Anspruch ist GPS-SOG ausreichend.

### 8.5 Tankgeber

**F16: Mein Tankgeber zeigt bei Seegang stark schwankende Werte — ist das normal?**
A: Ja, das ist physikalisch unvermeidbar — die Flüssigkeitsoberfläche im Tank bewegt sich mit dem Seegang. Die Lösung ist elektronische Dämpfung im Display oder Prozessor. Typische Dampening-Einstellungen: 30–120 Sekunden. Schallblech (Baffle) im Tank reduziert die Schwappbewegung.

**F17: Welcher Tankgeber ist für einen Diesel-Tank am besten?**
A: Widerstandsgeber (VDO/Wema) für einfache Installation und niedrigen Preis bei rechteckigen Tanks. Kapazitiver Geber für hohe Genauigkeit und lange Lebensdauer. Ultraschall-Geber für berührungslose Messung ohne Tankdurchbruch — ideal für Nachrüstung. Hydrostatischer Druckgeber nur bei großen Tanks (>500 l) auf Superyachten.

**F18: Wie genau sind Tankgeber wirklich?**
A: Widerstandsgeber: ±5–10 % bei rechteckigem Tank, ±15–20 % bei unregelmäßiger Tankform. Ultraschall: ±1–3 % nach Kalibrierung. Kapazitiv: ±2–5 %. Die schlechteste Genauigkeit hat jeder Geber bei niedrigem Füllstand (<25 %), weil die Restkraftstoff-Verteilung im Tank stark von der Schiffslage abhängt.

### 8.6 Kompass und Kursreferenz

**F19: Fluxgate oder Satellitenkompass — wann lohnt sich der Aufpreis?**
A: Ein Satellitenkompass lohnt sich auf Stahlbooten (keine magnetische Kompensation nötig), auf Booten mit starken magnetischen Störungen (große Generatoren, Wechselrichter), und wenn True Heading für AIS und Radar benötigt wird. Auf GFK-Segelyachten ist ein gut kompensierter Fluxgate ausreichend und deutlich günstiger.

**F20: Was ist der Unterschied zwischen Heading, Course Over Ground und Bearing?**
A: Heading (HDG) = die Richtung, in die der Bug zeigt (Kompass). Course Over Ground (COG) = die tatsächliche Kursrichtung über Grund (GPS). Die Differenz ist der Strom- und Leeversatz. Bearing (BRG) = die Richtung zu einem Wegpunkt. Bei Seitenwind kann HDG erheblich von COG abweichen.

### 8.7 NMEA und Integration

**F21: Wie viele Geräte kann ein NMEA-2000-Netzwerk maximal haben?**
A: Laut Standard: 50 Geräte pro Segment. Die Backbone-Länge darf 100 m nicht überschreiten, Stichleitungen max. 6 m. Die Gesamtstromaufnahme aller Geräte darf die Backbone-Versorgung nicht überschreiten (typisch 3–8 A je nach Netzteil). In der Yacht-Praxis sind 10–25 Geräte üblich.

**F22: Kann ich NMEA-0183-Geräte in ein NMEA-2000-Netzwerk einbinden?**
A: Ja, mit einem Gateway/Bridge. Beispiele: Actisense NGW-1 (bidirektional, 1 NMEA 0183 ↔ NMEA 2000, ca. 200 €), Garmin GND 10, Digital Yacht iKonvert, Yacht Devices YDNR-02. Die Konfiguration der PGN-Zuordnung ist wichtig — nicht alle Sätze werden automatisch konvertiert.

**F23: Was ist SignalK und brauche ich das?**
A: SignalK ist ein offenes Datenformat für Bootsinstrumente, basierend auf JSON über TCP/IP. Es ermöglicht die Integration von NMEA-Daten in moderne Web-Anwendungen, Tablet-Displays und Cloud-Dienste. Für Standard-Instrumentierung nicht nötig, aber relevant für DIY-Projekte, Open-Source-Navigation (OpenCPN) und AYDI-Integration.

### 8.8 Wartung und Pflege

**F24: Wie pflege ich meine Instrumente über den Winter?**
A: 1) Masttop-Windgeber: Bei Mastlegen prüfen, Lager fetten, Stecker kontaktsprühen. 2) Durchbruch-Geber: Bewuchs entfernen, Antifouling erneuern. 3) Displays: Schutzabdeckung, Stecker auf Korrosion prüfen. 4) NMEA-2000-Backbone: Alle Stecker auf Korrosion prüfen, ggf. Kontaktspray. 5) Batterien der Wireless-Geber entfernen. 6) Barometer gegen Referenz prüfen.

**F25: Wie lange halten Marine-Instrumente typischerweise?**
A: Displays: 7–15 Jahre (LCD-Degradation, Sonnenlicht). Durchbruch-Geber: 10–20 Jahre (Bronze), 5–10 Jahre (Kunststoff). Windgeber mechanisch: 5–10 Jahre (Lager, Potentiometer). Windgeber Ultraschall: 10–15+ Jahre. Kompass (Fluxgate): 15–25 Jahre. NMEA-2000-Backbone: 15–20 Jahre (Kabel), 10–15 Jahre (Stecker, T-Stücke).

**F26: Welche Ersatzteile sollte ich an Bord haben?**
A: Ersatz-Paddle-Wheel (wenn Paddle-Wheel-Log), Sicherungen für alle Instrumentenkreise, T-Stück und Terminierungswiderstand für NMEA-2000, Kontaktspray (WD-40 Marine oder Ballistol), Schrumpfschlauch und Kabelverbinder, Multimeter (zum Messen). Auf Langfahrt: Ersatz-Display oder Tablet mit WiFi-Gateway als Backup.

**F27: Kann ich meine alten Seatalk-1-Instrumente (Autohelm/Raymarine) weiter verwenden?**
A: Ja, mit einem Seatalk-1-zu-SeaTalkng-Adapter (Raymarine A06045 oder äquivalent). Dieser konvertiert die proprietären Seatalk-1-Datagramme in NMEA-2000-PGNs. Einschränkung: Nicht alle Seatalk-1-Funktionen werden unterstützt, und die Kalibrierung alter Geber ist begrenzt. Bei einer Neuinstallation ist ein kompletter Systemwechsel langfristig sinnvoller.

**F28: Wie schütze ich Masttopp-Stecker gegen Korrosion?**
A: 1) Selbstvulkanisierendes Band (Isolierband aus Silikonkautschuk) um den Stecker wickeln. 2) Kontaktfett (Vaseline, Tef-Gel oder marine Kontaktfett) auf die Pins. 3) Schrumpfschlauch mit Heißkleber-Innenring über den Übergang Kabel↔Stecker. 4) Silikonhülle oder Tauchkappe über den gesamten Stecker. 5) Beim jährlichen Mastlegen: öffnen, prüfen, erneuern.

**F29: Meine Instrumentenbeleuchtung ist zu hell für die Nachtwache — was tun?**
A: 1) Nachtmodus aktivieren (rote Hintergrundbeleuchtung). 2) Helligkeit auf Minimum dimmen. 3) Rote Folie über Display kleben (notfalls). 4) Automatische Helligkeitsregelung (LDR-Sensor) aktivieren, falls vorhanden. 5) Bei B&G/Simrad: NIGHT-Modus über Tastenkombination.

**F30: Gibt es eine Norm für Marine-Instrumenten-Schutzklassen?**
A: Ja, die IP-Schutzklassen nach IEC 60529. Marine-Instrumente sollten mindestens IPX6 (Schutz gegen starkes Strahlwasser) haben. IPX7 (Schutz gegen zeitweiliges Untertauchen) ist besser. IPX8 (dauerhaftes Untertauchen) ist für Unterwasser-Geber relevant. Die meisten Hersteller geben IPX6 oder IPX7 für Cockpit-Instrumente an.

---

## 9. Glossar

| Begriff | Erklärung |
|---------|-----------|
| **AWA** | Apparent Wind Angle — Scheinbare Windrichtung relativ zum Bug in Grad (0°–180° Bb/Stb) |
| **AWS** | Apparent Wind Speed — Scheinbare Windgeschwindigkeit in Knoten |
| **TWA** | True Wind Angle — Wahrer Windwinkel relativ zum Bug in Grad |
| **TWS** | True Wind Speed — Wahre Windgeschwindigkeit in Knoten |
| **TWD** | True Wind Direction — Wahre Windrichtung als Kompasskurs in Grad |
| **STW** | Speed Through Water — Geschwindigkeit durchs Wasser (Logge) in Knoten |
| **SOG** | Speed Over Ground — Geschwindigkeit über Grund (GPS) in Knoten |
| **COG** | Course Over Ground — Kurs über Grund (GPS) in Grad |
| **HDG** | Heading — Steuerkurs (Kompass) in Grad |
| **VMG** | Velocity Made Good — Geschwindigkeitskomponente in Richtung Ziel oder Wind |
| **BSP** | Boat Speed — Synonym für STW in einigen Systemen |
| **NMEA 0183** | National Marine Electronics Association Standard (1983), serielles Protokoll, max. 4800 Baud (Standard) oder 38400 Baud (High Speed) |
| **NMEA 2000** | Nachfolger von NMEA 0183, basiert auf CAN-Bus, 250 kBit/s, Plug-and-Play |
| **PGN** | Parameter Group Number — NMEA-2000-Nachrichtentyp (z. B. PGN 130306 = Wind Data) |
| **CAN-Bus** | Controller Area Network — Feldbus-Standard aus der Automobilindustrie, Basis für NMEA 2000 |
| **SeaTalkng** | Raymarines NMEA-2000-Implementierung mit proprietärem Steckerformat (kompatibel per Adapter) |
| **SimNet** | Simrads NMEA-2000-Implementierung mit proprietärem Steckerformat (kompatibel per Adapter) |
| **FastNet** | B&Gs proprietärer Hochgeschwindigkeitsbus (alt, nicht mehr für Neuinstallationen) |
| **SignalK** | Offenes JSON-basiertes Datenformat für Boots-Sensordaten über TCP/IP |
| **Fluxgate** | Magnetfeld-Sensorprinzip für elektronische Kompasse |
| **CHIRP** | Compressed High Intensity Radar Pulse — Frequenz-Sweep-Verfahren für Echolote |
| **MEMS** | Micro-Electro-Mechanical System — Miniaturisierte Sensoren (Beschleunigung, Gyroskop, Druck) |
| **IMU** | Inertial Measurement Unit — Kombination aus Accelerometer, Gyroskop und Magnetometer |
| **NTC** | Negative Temperature Coefficient — Thermistor, dessen Widerstand bei steigender Temperatur sinkt |
| **PT100** | Platin-Widerstandsthermometer mit 100 Ω bei 0°C |
| **Transducer** | Allgemeinbegriff für einen Messwertaufnehmer/Geber |
| **Thru-Hull** | Durch den Rumpf montierter Geber (Durchbruchgeber) |
| **In-Hull** | Auf der Rumpfinnenseite montierter Geber (Einschwinger) |
| **Transom-Mount** | Am Heckspiegel montierter Geber |
| **Paddle-Wheel** | Schaufelrad-Geber zur Geschwindigkeitsmessung durchs Wasser |
| **Dampening** | Elektronische Dämpfung/Glättung von Messwerten über einen Zeitraum |
| **Upwash** | Ablenkung des Luftstroms durch die Segel am Masttop |
| **Deviation** | Kompass-Ablenkung durch bordeigene Magnetfelder |
| **Variation/Missweisung** | Differenz zwischen magnetischem und geographischem Nord an einem Ort |
| **IPX6/IPX7** | Schutzklasse gegen Strahlwasser (IPX6) bzw. zeitweiliges Untertauchen (IPX7) |
| **Barograph** | Gerät zur zeitlichen Aufzeichnung des Luftdrucks |
| **Aneroid** | Evakuierte Metalldose als druckempfindliches Element im Barometer |
| **Backbone** | Hauptkabel des NMEA-2000-Netzwerks, an das Geräte über T-Stücke angeschlossen werden |
| **Terminator** | 120-Ω-Abschlusswiderstand an den Enden des NMEA-2000-Backbone |
| **Stichleitung (Drop)** | Kabel vom NMEA-2000-Backbone zum einzelnen Gerät (max. 6 m) |
| **Fairing Block** | Kunststoff-Formteil für Durchbruchgeber, das die Strömung am Geber optimiert |
| **Kalibrierfaktor** | Multiplikator zur Korrektur systematischer Messfehler (z. B. Log-Kalibrierung) |

---

## 10. Schnell-Referenz

### 10.1 NMEA-2000-Schnellinstallation

```
Checkliste NMEA-2000-Netzwerk:
□ Backbone-Kabel verlegt (max. 100 m Gesamtlänge)
□ 2× Terminierungswiderstand (120 Ω) an den Enden
□ Stromversorgung am Backbone (12V, abgesichert, min. 3 A)
□ T-Stücke alle eingerastet
□ Stichleitungen <6 m
□ Geräte in Geräteliste sichtbar
□ Firmware aller Geräte aktuell
□ Kalibrierung durchgeführt (Log, Wind, Kompass, Tiefe)
```

### 10.2 Kalibrierungsroutine Saisonstart

```
1. Echolot:
   □ Offset prüfen (Tiefe unter Kiel oder Wasserlinie?)
   □ Handlot-Vergleichsmessung
   □ Geber auf Bewuchs prüfen

2. Logge (STW):
   □ Paddle-Wheel reinigen / Ultraschall-Geber prüfen
   □ Vergleichsfahrt: GPS-SOG vs. STW bei Stillwasser
   □ Kalibrierfaktor anpassen (Ziel: <3 % Abweichung)

3. Windgeber:
   □ Mechanisch: Lager prüfen, Schalen/Fahne leichtgängig?
   □ Ultraschall: Transducer reinigen
   □ Masttopp-Stecker prüfen
   □ Kreissegeln zur Kalibrierung (wenn Performance-System)

4. Kompass:
   □ Neue Geräte installiert? → Neukompensation
   □ Kompensationsroutine durchführen (360° langsam drehen)
   □ Restdeviation <3° akzeptabel

5. Barometer:
   □ Gegen Referenz (Flughafen-METAR oder Wetterstation) prüfen
   □ Höhenkorrektur einstellen (Sensor ~1 m über MSL)
   □ Barograph-Verlauf auf Plausibilität prüfen

6. Tankgeber:
   □ Bei vollem Tank: Anzeige 100 %?
   □ Bei leerem Tank (Werft): Anzeige 0 %?
   □ Schwimmer-Beweglichkeit prüfen (Widerstandsgeber)
```

### 10.3 Instrumenten-Empfehlung nach Bootstyp

| Bootstyp | Budget | Empfehlung |
|----------|--------|------------|
| Segelyacht 8–10 m, Fahrt | 1.000–2.000 € | B&G Triton2 + Standard-Geber + gWind |
| Segelyacht 10–14 m, Fahrt | 2.000–4.000 € | B&G Triton2 × 2 + WS320 + DST800 |
| Segelyacht 10–14 m, Regatta | 4.000–10.000 € | B&G H5000 + WS320 + DST800 + Prozessor |
| Segelyacht 14–18 m, Fahrt | 3.000–6.000 € | B&G Triton2 × 3 + Nemesis + WS320 |
| Motoryacht 8–12 m | 1.500–3.000 € | Garmin GMI 20 × 2 + GST 43 + Motorintegration |
| Motoryacht 12–18 m | 3.000–8.000 € | Garmin GNX 120 × 2 + vollständige NMEA-2000-Integration |
| Superyacht 18 m+ | 10.000–50.000 € | Furuno + B&G H5000 + Satellitenkompass + redundant |
| Kleinboot/Trailer | 300–800 € | NASA Marine Clipper Duet + Clipper Wind |

### 10.4 NMEA-2000-PGN-Referenz (wichtigste für Instrumente)

| PGN | Name | Daten |
|-----|------|-------|
| 127250 | Vessel Heading | Heading (magnetic/true), Deviation, Variation |
| 127251 | Rate of Turn | Drehrate in °/s |
| 127257 | Attitude | Yaw, Pitch, Roll |
| 128259 | Speed, Water Referenced | STW |
| 128267 | Water Depth | Tiefe, Offset |
| 128275 | Distance Log | Trip + Total Log |
| 129025 | Position, Rapid Update | Latitude, Longitude |
| 129026 | COG & SOG, Rapid Update | COG, SOG |
| 130306 | Wind Data | Wind Speed, Wind Angle, Reference (App/True) |
| 130310 | Environmental Parameters | Water Temp, Air Temp, Pressure |
| 130311 | Environmental Parameters | Temp, Humidity, Pressure |
| 130312 | Temperature | Temp Source + Value |
| 127505 | Fluid Level | Tank Instance, Type, Level, Capacity |
| 127489 | Engine Parameters, Dynamic | RPM, Oil Pressure, Temp, Fuel Rate |
| 127488 | Engine Parameters, Rapid | RPM |

### 10.5 Kabelfarben NMEA 2000 (DeviceNet Micro-C)

| Pin | Farbe | Funktion |
|-----|-------|----------|
| 1 | Rot | V+ (12V, 9–16V) |
| 2 | Weiß | CAN-H (Daten High) |
| 3 | Frei | Shield/Drain (Schirm) |
| 4 | Schwarz | V- (Masse) |
| 5 | Blau | CAN-L (Daten Low) |

---

## ANHANG A — Fallstudie: Instrumenten-Upgrade Bavaria 37 Cruiser (2008)

### Ausgangslage
Bavaria 37 Cruiser, Baujahr 2008, original ausgestattet mit Raymarine ST60+ Instrumenten (Seatalk 1). Logge-Geber (Paddle-Wheel) stark bewachsen, Windanzeige sporadisch ausgefallen, kein NMEA 2000.

### Problemanalyse

| Komponente | Zustand | Bewertung |
|-----------|---------|-----------|
| ST60+ Tridata | Display pixelfehler, Hintergrundbeleuchtung schwach | AYDI: 35/100 |
| ST60+ Wind | Funktioniert sporadisch, Masttopp-Stecker korrodiert | AYDI: 25/100 |
| Log-Geber | Paddle-Wheel blockiert, Bewuchs massiv | AYDI: 20/100 |
| Lot-Geber | Funktioniert, aber Bewuchs | AYDI: 55/100 |
| Kompass (ST60+) | Deviation >8° auf mehreren Kursen | AYDI: 40/100 |
| NMEA | Seatalk 1, kein NMEA 2000 | AYDI: 20/100 |

### Lösung
Kompletter Systemwechsel auf B&G Triton2 mit NMEA 2000:

| Komponente | Modell | Preis |
|-----------|--------|-------|
| 2× B&G Triton2 Display | Cockpit + Niedergang | 760 € |
| 1× B&G WS320 Windgeber (kabelgebunden) | Masttop | 450 € |
| 1× Airmar DST800 (Tiefe+Speed+Temp) | Thru-Hull | 380 € |
| 1× B&G Precision-9 Kompass | Unter Cockpitboden | 320 € |
| NMEA-2000-Backbone + T-Stücke | 15 m Backbone, 6 T-Stücke | 180 € |
| Einbau (Werft) | 12 Stunden à 85 € | 1.020 € |
| **Gesamt** | | **3.110 €** |

### Ergebnis

| Komponente | Bewertung nachher |
|-----------|------------------|
| Instrumentierung gesamt | AYDI: 85/100 |
| Windmessung | AYDI: 90/100 (Ultraschall, zuverlässig) |
| Geschwindigkeit | AYDI: 85/100 (Smart Sensor, NMEA 2000) |
| Tiefenmessung | AYDI: 85/100 (CHIRP, Smart Sensor) |
| Kompass | AYDI: 90/100 (9-Achsen, auto-kalibrierend) |
| Integration | AYDI: 90/100 (volles NMEA 2000) |

**Confidence:** documented (realer Umbau, verifiziert)

---

## ANHANG B — Fallstudie: NMEA-2000-Netzwerkprobleme auf einer Hallberg-Rassy 412

### Ausgangslage
Hallberg-Rassy 412, Baujahr 2015, ab Werk mit NMEA-2000-Netzwerk und B&G-Instrumentierung. Nach 7 Jahren sporadische Ausfälle: Instrumente verschwinden aus der Geräteliste und tauchen nach Minuten wieder auf.

### Diagnose

| Prüfschritt | Befund |
|------------|--------|
| Backbone-Spannung | 11,8 V (OK) |
| Terminierung | 3 Terminatoren gefunden (1 zu viel!) |
| T-Stücke visuell | 2 Stecker mit Grünspan (Korrosion) |
| Backbone-Widerstand | 40 Ω (sollte 60 Ω sein — 3. Terminator!) |
| Stichleitung zum Windgeber | 8,5 m (max. erlaubt: 6 m!) |

### Ursache
1. Beim nachträglichen Einbau eines AIS-Transponders wurde ein drittes Terminatorsegment hinzugefügt — mit eigenem Terminator. Ergebnis: 3 Terminatoren statt 2, was die Bus-Impedanz veränderte.
2. Die Stichleitung zum Masttop-Windgeber war zu lang (8,5 m statt max. 6 m).
3. Zwei T-Stücke im Motorraum waren korrodiert (Kondenswasser).

### Lösung

| Maßnahme | Kosten |
|----------|--------|
| Dritten Terminator entfernt | 0 € |
| Backbone bis zur Mastbasis verlängert (Stichleitung auf 3 m verkürzt) | 85 € |
| 2 korrodierte T-Stücke ersetzt | 40 € |
| Alle Stecker mit Kontaktfett behandelt | 15 € |
| **Gesamt** | **140 €** |

### Ergebnis
Netzwerk seitdem stabil, keine Ausfälle in 12 Monaten Betrieb.

**Confidence:** documented

---

## ANHANG C — Fallstudie: Tankgeber-Problematik auf einer Hanse 505

### Ausgangslage
Hanse 505, Baujahr 2017. Eigner klagt über unzuverlässige Diesel-Tankanzeige. Tank zeigt 80 % nach dem Tanken (sollte 100 %), fällt dann auf 40 % innerhalb der ersten 2 Stunden Motorbetrieb, bleibt dann lange bei 40 % und springt plötzlich auf 0 %.

### Diagnose

| Prüfschritt | Befund |
|------------|--------|
| Tankform | Stark trapezförmig (Keel-Tank, schmaler Boden, breiter Oberteil) |
| Geber-Typ | Widerstandsgeber (Wema), linear |
| Geber-Länge | 650 mm (maximaler Füllstand) |
| Tankkapazität | 200 l |
| Tankvermessung | 50 % Volumen in oberen 30 % der Tankhöhe |

### Ursache
Der lineare Widerstandsgeber in einem nicht-linearen (trapezförmigen) Tank erzeugt eine systematische Fehlmessung. Bei 50 % Tankfüllstand (100 l) steht die Flüssigkeit nur bei 30 % der Geberhöhe, weil das Volumen im unteren Teil wesentlich kleiner ist als im oberen.

### Lösung

| Option | Beschreibung | Kosten |
|--------|-------------|--------|
| A) Tankform-Kalibrierung im Anzeigegerät | NMEA-2000-Display mit Tankform-Tabelle (z. B. B&G H5000) | 0 € (wenn H5000 vorhanden) |
| B) Ultraschall-Tankgeber (Gobius) | Berührungslos, konfigurierbare Kennlinie | 250 € |
| C) Multi-Sender-Geber | Wema mit 5 Widerstandsstufen | 180 € + Einbau |

Gewählte Lösung: B) Gobius-Ultraschall-Geber, auf Tankboden geklebt, mit NMEA-2000-Konverter.

### Ergebnis
Tankanzeige nach Kalibrierung auf ±3 % genau. AYDI-Bewertung Tankgeber: vorher 30/100, nachher 85/100.

**Confidence:** documented

---

## ANHANG D — Fallstudie: Windgeber-Kalibrierung für Regatta (J/111)

### Ausgangslage
J/111 (11 m Sportsegler), ausgestattet mit B&G H5000 und WS320 Windgeber. Team klagt über inkonsistente wahre Winddaten — auf Backbord-Bug systematisch 5–8° mehr TWA als auf Steuerbord-Bug.

### Diagnose

| Test | Befund |
|------|--------|
| AWA Steuerbord 45° | AWS 14 kn |
| AWA Backbord 45° | AWS 14 kn |
| TWA Steuerbord (berechnet) | 33° |
| TWA Backbord (berechnet) | 41° |
| Differenz | 8° (sollte symmetrisch sein) |

### Ursache
Upwash-Korrektur nicht kalibriert. Die Segel (insbesondere das Groß) lenken den Luftstrom auf Steuerbord-Bug anders als auf Backbord-Bug — Asymmetrie durch Großsegel-Twist und Vorsegel-Position.

### Lösung
Systematische Kalibrierung durch Kreissegeln:

1. Bei 12–15 kn wahrem Wind (stabil, wenig Böen)
2. Boot in 10°-Schritten von 30° bis 180° auf beiden Bugen segeln
3. Auf jedem Kurs 60 s Daten loggen (AWA, AWS, STW, HDG)
4. Upwash-Tabelle aus der Differenz Steuerbord↔Backbord berechnen
5. Tabelle in H5000-CPU eingeben

### Ergebnis

| Parameter | Vorher | Nachher |
|-----------|--------|---------|
| TWA-Asymmetrie | 8° | <1° |
| TWS-Fehler | ±12 % | ±3 % |
| VMG-Anzeige nutzbar | Nein (irreführend) | Ja (zuverlässig) |
| AYDI-Bewertung Wind | 55/100 | 92/100 |

**Confidence:** documented

---

## ANHANG E — Fallstudie: Echolot-Upgrade auf einer Dehler 38 SQ

### Ausgangslage
Dehler 38 SQ, Baujahr 2012. Original-Echolot (Raymarine ST60+ Tridata) mit Einschwinger-Geber im vorderen Drittel. Echolot fällt bei Geschwindigkeiten >7 kn aus (Tiefe = ---).

### Diagnose

| Prüfschritt | Befund |
|------------|--------|
| Gebertyp | Einschwinger (In-Hull), aufgeklebt mit Sikaflex |
| Rumpfaufbau | GFK Sandwich (Balkonstruktur im Boden) |
| Klebefuge | Lufteinschlüsse sichtbar (blasige Oberfläche) |
| Signal bei 0 kn | OK, Tiefe korrekt |
| Signal bei 3 kn | OK |
| Signal bei 7 kn | Intermittierend, Tiefe springt |
| Signal bei 10 kn | Totalausfall |

### Ursache
Doppelproblem: 1) Sandwich-Struktur im Rumpf dämpft das Ultraschall-Signal erheblich. 2) Bei höherer Geschwindigkeit lösen sich Luftblasen vom Rumpfboden, die den Ultraschallpfad zusätzlich stören. Der Einschwinger-Geber war von Anfang an eine Kompromiss-Installation.

### Lösung
Einbau eines Airmar P79 Durchbruchgebers in Kunststoff:

| Maßnahme | Kosten |
|----------|--------|
| Airmar P79 Durchbruchgeber | 120 € |
| Rumpfdurchbruch (Werft) | 250 € |
| NMEA-2000-Adapter (wenn nötig) | 180 € |
| **Gesamt** | **550 €** |

### Ergebnis
Echolot funktioniert zuverlässig bis >20 kn. AYDI-Bewertung Tiefenmessung: vorher 40/100, nachher 88/100.

**Confidence:** documented

---

## ANHANG F — Fallstudie: Komplettsystem Superyacht (24 m Motor)

### Ausgangslage
Neubauprojekt einer 24-m-Motoryacht mit Aluminium-Rumpf. Spezifikation der Instrumentierung für drei Steuerstände (Flybridge, Salon, Backup).

### Anforderung

| Anforderung | Spezifikation |
|------------|---------------|
| Redundanz | Dual-NMEA-2000-Backbone |
| Windmessung | Nicht primär (Motoryacht) |
| Echolot | CHIRP, 200 kHz + 50 kHz, Tiefwasser-fähig |
| Kompass | Satellitenkompass (Aluminium-Rumpf!) |
| Motordaten | 2× Caterpillar C12.9, vollständige NMEA-2000-Integration |
| Tankgeber | 4× Diesel, 2× Frischwasser, 1× Abwasser |
| Displays | 3× Steuerstände, jeweils unabhängig |

### Instrumenten-Spezifikation

| Komponente | Modell | Anzahl | Stückpreis | Gesamt |
|-----------|--------|--------|-----------|--------|
| Satellitenkompass | Furuno SC-70 | 1 | 4.200 € | 4.200 € |
| Echolotgeber | Airmar B175HW (CHIRP, Bronze) | 1 | 1.800 € | 1.800 € |
| Instrument-Display | Garmin GNX 120 (7") | 6 | 700 € | 4.200 € |
| Motorüberwachung | Garmin GMI 20 | 2 | 400 € | 800 € |
| GPS-Antenne | Garmin GA 38 | 2 | 120 € | 240 € |
| Tankgeber Ultraschall | Gobius Pro (NMEA 2000) | 7 | 280 € | 1.960 € |
| Barometer | Yacht Devices YDBC-05 | 1 | 160 € | 160 € |
| Temperatur-Sensoren | Yacht Devices YDTC-13 | 1 | 170 € | 170 € |
| Batteriemonitor | Victron SmartShunt (NMEA 2000) | 2 | 150 € | 300 € |
| NMEA-2000-Backbone (dual) | Garmin NMEA 2000 Starter Kit × 2 | 2 | 250 € | 500 € |
| WiFi-Gateway | Yacht Devices YDWG-02 | 1 | 180 € | 180 € |
| Einbau (Werft) | 60 Stunden à 95 € | — | — | 5.700 € |
| **Gesamt** | | | | **20.210 €** |

### Besonderheit Aluminium-Rumpf
- **Kein Fluxgate-Kompass** möglich (massive magnetische Störung durch Aluminium-Aufbauten, Motoren, Generatoren)
- **Nur Kunststoff-Geber** für Rumpfdurchbrüche (galvanische Korrosion!)
- **Opferanoden** an allen Durchbrüchen
- **GPS-Antenne auf Flybridge** mit freier Himmelssicht (Aluminium schirmt GPS ab)

**Confidence:** estimated (Planungsbeispiel, Preise 2025)

---

## ANHANG G — Fallstudie: DIY-Instrumentierung mit Raspberry Pi und SignalK

### Ausgangslage
Contessa 32, Baujahr 1978. Eigner möchte günstige Instrumentierung mit modernen Funktionen (Tablet-Anzeige, Datenlogging, Cloud-Upload).

### Konzept
Raspberry Pi 4 mit SignalK-Server als zentrale Datenplattform. Vorhandene NMEA-0183-Geber (Log, Lot, Windgeber) über USB-Adapter eingebunden. Tablet als Display.

### Komponenten

| Komponente | Modell | Preis |
|-----------|--------|-------|
| Raspberry Pi 4 (4 GB) | In wasserdichtem Gehäuse | 80 € |
| USB-NMEA-0183-Adapter | Ship Modul MiniPlex-Lite USB | 150 € |
| WiFi-Access-Point | TP-Link (12V Marine-Adapter) | 30 € |
| Tablet (Anzeige) | Samsung Galaxy Tab A, in Klemmhalterung | 200 € |
| GPS-Maus | USB GPS-Empfänger (u-blox) | 25 € |
| Barometer-Sensor | BME280 über I²C am Raspberry Pi | 5 € |
| SignalK-Server | Open Source (kostenlos) | 0 € |
| WilhelmSK (Tablet-App) | iOS/Android, Instrumenten-App | 20 € |
| Einbau (DIY) | 15 Stunden Eigenarbeit | 0 € |
| **Gesamt** | | **510 €** |

### Ergebnis

| Kriterium | Bewertung |
|-----------|-----------|
| Funktionsumfang | 75/100 (alle Grunddaten + Datenlogging + Cloud) |
| Zuverlässigkeit | 55/100 (Raspberry Pi nicht marinefest, Tablet bei Sonnenlicht schlecht) |
| Nachrüstbarkeit | 90/100 (SignalK unterstützt fast alles) |
| Preis-Leistung | 95/100 (unschlagbar günstig) |
| AYDI-Gesamtbewertung | 65/100 (Abzug für Zuverlässigkeit und Ablesbarkeit) |

**Confidence:** documented

---

## ANHANG H — Fallstudie: Barograph rettet Crew vor Sturm (Atlantiküberquerung)

### Ausgangslage
Hallberg-Rassy 48, Atlantiküberquerung (ARC 2023, Las Palmas → Barbados). Tag 8: Barograph zeigt Druckfall von 4,5 hPa in 3 Stunden.

### Ereigniskette

| Zeitpunkt | Druck (hPa) | Maßnahme |
|-----------|-------------|----------|
| 06:00 | 1018 | Normal, keine Auffälligkeit |
| 09:00 | 1016 | Leichter Druckfall bemerkt — Beobachtung |
| 12:00 | 1013,5 | 4,5 hPa in 6 h — Barograph-Alarm (>3 hPa/3h) |
| 12:30 | — | Crew beginnt Sturmvorbereitung: Segel reduzieren, Luken sichern |
| 15:00 | 1009 | Squall-Linie erreicht Boot: 45 kn Wind, Regen |
| 18:00 | 1006 | Stärkstes Tief, 50+ kn Böen |
| 00:00 | 1012 | Druckanstieg, Front durchgezogen |

### Bewertung
Der digitale Barograph (B&G-Display mit 48-h-Barograph-Funktion) warnte die Crew 3 Stunden vor dem Sturm. Die GFS-Wetterkarten hatten das lokale Tief nicht korrekt aufgelöst. Ohne Barograph hätte die Crew möglicherweise unter vollem Segel in die Squall-Linie gesegelt.

**AYDI-Bewertung:** Barograph ist ein sicherheitsrelevantes Instrument der höchsten Kategorie für Offshore-Segler. Empfehlung: Immer installieren, Alarm auf 3 hPa/3h einstellen.

**Confidence:** documented

---

## ANHANG I — Pydantic v2 Modelle: Sensordaten

```python
"""
AYDI Pydantic v2 Models — Instrument & Sensor Data
All models use model_config = {"from_attributes": True}
NEVER use class Config — always use model_config dict.
"""

from __future__ import annotations
from datetime import datetime
from enum import Enum
from typing import Optional
from pydantic import BaseModel, Field, field_validator


class ConfidenceLevel(str, Enum):
    """Confidence levels for sensor data."""
    MEASURED = "measured"
    CALCULATED = "calculated"
    VISUAL_HIGH = "visual_high"
    VISUAL_MEDIUM = "visual_medium"
    VISUAL_LOW = "visual_low"
    VISUAL_INSUFFICIENT = "visual_insufficient"
    ESTIMATED = "estimated"
    BENCHMARK = "benchmark"
    DOCUMENTED = "documented"


class SensorType(str, Enum):
    """Types of marine sensors."""
    WIND_MECHANICAL = "wind_mechanical"
    WIND_ULTRASONIC = "wind_ultrasonic"
    LOG_PADDLEWHEEL = "log_paddlewheel"
    LOG_ULTRASONIC = "log_ultrasonic"
    LOG_GPS = "log_gps"
    DEPTH_SINGLE_FREQ = "depth_single_freq"
    DEPTH_DUAL_FREQ = "depth_dual_freq"
    DEPTH_CHIRP = "depth_chirp"
    COMPASS_FLUXGATE = "compass_fluxgate"
    COMPASS_SATELLITE = "compass_satellite"
    COMPASS_MEMS = "compass_mems"
    BAROMETER = "barometer"
    THERMOMETER_NTC = "thermometer_ntc"
    THERMOMETER_PT100 = "thermometer_pt100"
    TANK_RESISTIVE = "tank_resistive"
    TANK_ULTRASONIC = "tank_ultrasonic"
    TANK_CAPACITIVE = "tank_capacitive"
    TANK_HYDROSTATIC = "tank_hydrostatic"
    INCLINOMETER_MEMS = "inclinometer_mems"
    TACHOMETER = "tachometer"


class MountType(str, Enum):
    """Sensor mounting types."""
    MASTHEAD = "masthead"
    THRU_HULL = "thru_hull"
    IN_HULL = "in_hull"
    TRANSOM = "transom"
    DECK = "deck"
    INTERNAL = "internal"
    ENGINE = "engine"
    WIRELESS = "wireless"


class BusType(str, Enum):
    """Communication bus types."""
    NMEA_0183 = "nmea_0183"
    NMEA_2000 = "nmea_2000"
    SEATALK_1 = "seatalk_1"
    SEATALKNG = "seatalkng"
    SIMNET = "simnet"
    FASTNET = "fastnet"
    SIGNALK = "signalk"
    WIFI = "wifi"
    BLUETOOTH = "bluetooth"
    ANT_PLUS = "ant_plus"
    ANALOG = "analog"
    PROPRIETARY = "proprietary"


class SensorCondition(str, Enum):
    """Condition assessment of a sensor."""
    EXCELLENT = "excellent"
    GOOD = "good"
    FAIR = "fair"
    POOR = "poor"
    DEFECTIVE = "defective"
    MISSING = "missing"


# ──────────────────────────────────────────────
# Core Sensor Models
# ──────────────────────────────────────────────


class SensorBase(BaseModel):
    """Base model for all sensor types."""

    model_config = {"from_attributes": True}

    sensor_id: str = Field(..., description="Unique sensor identifier")
    sensor_type: SensorType
    manufacturer: str
    model_name: str
    mount_type: MountType
    bus_type: BusType
    installation_year: Optional[int] = None
    last_calibration: Optional[datetime] = None
    condition: SensorCondition = SensorCondition.GOOD
    confidence: ConfidenceLevel = ConfidenceLevel.ESTIMATED
    notes: Optional[str] = None


class WindSensorData(BaseModel):
    """Wind sensor measurement data."""

    model_config = {"from_attributes": True}

    awa_deg: Optional[float] = Field(None, ge=-180, le=180, description="Apparent Wind Angle [°]")
    aws_kn: Optional[float] = Field(None, ge=0, le=200, description="Apparent Wind Speed [kn]")
    twa_deg: Optional[float] = Field(None, ge=-180, le=180, description="True Wind Angle [°]")
    tws_kn: Optional[float] = Field(None, ge=0, le=200, description="True Wind Speed [kn]")
    twd_deg: Optional[float] = Field(None, ge=0, le=360, description="True Wind Direction [°]")
    measurement_type: str = Field("apparent", description="'apparent' or 'true'")
    upwash_corrected: bool = False
    heel_corrected: bool = False
    confidence: ConfidenceLevel = ConfidenceLevel.ESTIMATED

    @field_validator("awa_deg", "twa_deg")
    @classmethod
    def validate_wind_angle(cls, v: Optional[float]) -> Optional[float]:
        if v is not None and abs(v) > 180:
            raise ValueError("Wind angle must be between -180 and 180 degrees")
        return v


class WindSensorSpec(SensorBase):
    """Wind sensor specification."""

    model_config = {"from_attributes": True}

    measurement_principle: str = Field(..., description="'cup', 'vane', 'ultrasonic'")
    speed_range_kn: tuple[float, float] = (0.0, 70.0)
    speed_accuracy_kn: float = Field(0.5, description="Speed accuracy [kn]")
    direction_accuracy_deg: float = Field(2.0, description="Direction accuracy [°]")
    sample_rate_hz: float = Field(1.0, ge=0.1, le=50.0)
    startup_speed_kn: float = Field(1.5, ge=0.0, description="Min speed for measurement")
    wireless: bool = False
    solar_powered: bool = False
    weight_g: Optional[int] = None


class DepthSensorData(BaseModel):
    """Depth sounder measurement data."""

    model_config = {"from_attributes": True}

    depth_m: Optional[float] = Field(None, ge=0, le=12000, description="Measured depth [m]")
    depth_below_keel_m: Optional[float] = Field(None, description="Depth below keel [m]")
    depth_below_waterline_m: Optional[float] = Field(None, description="Depth below waterline [m]")
    offset_to_keel_m: float = Field(0.0, description="Offset sensor to keel [m]")
    offset_to_waterline_m: float = Field(0.0, description="Offset sensor to waterline [m]")
    frequency_khz: float = Field(200.0, description="Operating frequency [kHz]")
    water_temp_c: Optional[float] = Field(None, description="Water temperature [°C]")
    confidence: ConfidenceLevel = ConfidenceLevel.ESTIMATED

    @field_validator("depth_m")
    @classmethod
    def validate_depth(cls, v: Optional[float]) -> Optional[float]:
        if v is not None and v < 0:
            raise ValueError("Depth cannot be negative")
        return v


class DepthSensorSpec(SensorBase):
    """Depth sensor specification."""

    model_config = {"from_attributes": True}

    frequency_khz: list[float] = Field(default_factory=lambda: [200.0])
    chirp_capable: bool = False
    chirp_range_khz: Optional[tuple[float, float]] = None
    max_depth_m: float = Field(300.0, ge=1.0)
    beam_angle_deg: float = Field(12.0, ge=1.0, le=60.0)
    transducer_material: str = Field("plastic", description="'plastic', 'bronze', 'stainless'")
    hull_material_compatible: list[str] = Field(
        default_factory=lambda: ["grp", "wood", "steel", "aluminum"]
    )


class SpeedSensorData(BaseModel):
    """Speed log measurement data."""

    model_config = {"from_attributes": True}

    stw_kn: Optional[float] = Field(None, ge=0, le=100, description="Speed Through Water [kn]")
    sog_kn: Optional[float] = Field(None, ge=0, le=100, description="Speed Over Ground [kn]")
    trip_nm: Optional[float] = Field(None, ge=0, description="Trip log [nm]")
    total_nm: Optional[float] = Field(None, ge=0, description="Total log [nm]")
    calibration_factor: float = Field(1.0, ge=0.5, le=2.0)
    confidence: ConfidenceLevel = ConfidenceLevel.ESTIMATED


class SpeedSensorSpec(SensorBase):
    """Speed sensor specification."""

    model_config = {"from_attributes": True}

    measurement_principle: str = Field(..., description="'paddlewheel', 'ultrasonic', 'gps'")
    speed_range_kn: tuple[float, float] = (0.0, 50.0)
    accuracy_percent: float = Field(5.0, ge=0.1, le=20.0)
    startup_speed_kn: float = Field(0.5, ge=0.0)
    through_hull_diameter_mm: Optional[float] = Field(None, description="Thru-hull diameter [mm]")


class CompassData(BaseModel):
    """Compass / heading sensor data."""

    model_config = {"from_attributes": True}

    heading_magnetic_deg: Optional[float] = Field(None, ge=0, le=360)
    heading_true_deg: Optional[float] = Field(None, ge=0, le=360)
    deviation_deg: Optional[float] = Field(None, ge=-30, le=30)
    variation_deg: Optional[float] = Field(None, ge=-30, le=30)
    rate_of_turn_deg_s: Optional[float] = Field(None, ge=-180, le=180)
    confidence: ConfidenceLevel = ConfidenceLevel.ESTIMATED


class CompassSpec(SensorBase):
    """Compass sensor specification."""

    model_config = {"from_attributes": True}

    compass_type: str = Field(..., description="'fluxgate', 'satellite', 'mems_imu'")
    accuracy_deg: float = Field(1.0, ge=0.1, le=10.0)
    resolution_deg: float = Field(0.1, ge=0.01, le=1.0)
    tilt_compensation_deg: float = Field(25.0, ge=0.0, le=90.0)
    sample_rate_hz: float = Field(10.0, ge=1.0, le=200.0)
    deviation_compensation: bool = True
    gnss_systems: Optional[list[str]] = None  # For satellite compass


class BarometerData(BaseModel):
    """Barometric pressure data."""

    model_config = {"from_attributes": True}

    pressure_hpa: Optional[float] = Field(None, ge=870, le=1084)
    pressure_trend_hpa_3h: Optional[float] = Field(None, ge=-30, le=30)
    altitude_correction_hpa: float = Field(0.0)
    timestamp: datetime = Field(default_factory=datetime.utcnow)
    confidence: ConfidenceLevel = ConfidenceLevel.MEASURED


class TankSensorData(BaseModel):
    """Tank level sensor data."""

    model_config = {"from_attributes": True}

    tank_id: str = Field(..., description="Tank identifier")
    tank_type: str = Field(..., description="'fuel', 'water', 'waste', 'holding'")
    level_percent: Optional[float] = Field(None, ge=0, le=100)
    volume_liters: Optional[float] = Field(None, ge=0)
    capacity_liters: Optional[float] = Field(None, ge=0)
    temperature_c: Optional[float] = None
    confidence: ConfidenceLevel = ConfidenceLevel.ESTIMATED

    @field_validator("level_percent")
    @classmethod
    def validate_level(cls, v: Optional[float]) -> Optional[float]:
        if v is not None and (v < 0 or v > 100):
            raise ValueError("Tank level must be between 0 and 100 percent")
        return v


class TankSensorSpec(SensorBase):
    """Tank level sensor specification."""

    model_config = {"from_attributes": True}

    measurement_principle: str = Field(
        ..., description="'resistive', 'ultrasonic', 'capacitive', 'hydrostatic'"
    )
    max_depth_mm: float = Field(..., ge=50, le=3000)
    accuracy_percent: float = Field(5.0, ge=0.1, le=25.0)
    compatible_media: list[str] = Field(
        default_factory=lambda: ["diesel", "water"]
    )
    resistance_range_ohm: Optional[tuple[float, float]] = None  # For resistive
    signal_output: str = Field("resistance", description="'resistance', '4-20mA', '0-5V', 'nmea2000'")


class InclinometerData(BaseModel):
    """Inclinometer / heel and pitch sensor data."""

    model_config = {"from_attributes": True}

    heel_deg: Optional[float] = Field(None, ge=-90, le=90, description="Heel angle [°]")
    pitch_deg: Optional[float] = Field(None, ge=-45, le=45, description="Pitch/trim angle [°]")
    roll_rate_deg_s: Optional[float] = None
    pitch_rate_deg_s: Optional[float] = None
    confidence: ConfidenceLevel = ConfidenceLevel.MEASURED
```

---

## ANHANG J — Pydantic v2 Modelle: NMEA-Integration

```python
"""
AYDI Pydantic v2 Models — NMEA Network and Integration
All models use model_config = {"from_attributes": True}
NEVER use class Config — always use model_config dict.
"""

from __future__ import annotations
from datetime import datetime
from enum import Enum
from typing import Optional
from pydantic import BaseModel, Field, field_validator


class NMEAProtocol(str, Enum):
    """NMEA protocol versions."""
    NMEA_0183 = "nmea_0183"
    NMEA_2000 = "nmea_2000"
    SEATALK_1 = "seatalk_1"
    SEATALKNG = "seatalkng"
    SIMNET = "simnet"


class NMEADeviceStatus(str, Enum):
    """Device status on NMEA bus."""
    ONLINE = "online"
    OFFLINE = "offline"
    INTERMITTENT = "intermittent"
    ERROR = "error"
    NOT_CONFIGURED = "not_configured"


class NMEANetworkTopology(BaseModel):
    """NMEA 2000 network topology description."""

    model_config = {"from_attributes": True}

    backbone_length_m: float = Field(..., ge=0.1, le=200.0, description="Total backbone length [m]")
    terminator_count: int = Field(2, ge=0, le=4, description="Number of terminators (should be 2)")
    max_drop_length_m: float = Field(6.0, ge=0.1, le=10.0, description="Longest drop cable [m]")
    device_count: int = Field(0, ge=0, le=100)
    power_supply_amps: float = Field(3.0, ge=0.5, le=20.0)
    backbone_voltage_v: Optional[float] = Field(None, ge=7.0, le=16.0)
    dual_backbone: bool = False
    protocol: NMEAProtocol = NMEAProtocol.NMEA_2000

    @field_validator("terminator_count")
    @classmethod
    def validate_terminators(cls, v: int) -> int:
        if v != 2:
            # Don't raise error, but this will be flagged in analysis
            pass
        return v


class NMEADevice(BaseModel):
    """A device on the NMEA 2000 network."""

    model_config = {"from_attributes": True}

    device_instance: int = Field(..., ge=0, le=252)
    device_name: str
    manufacturer: str
    model: str
    firmware_version: Optional[str] = None
    status: NMEADeviceStatus = NMEADeviceStatus.ONLINE
    pgns_transmitted: list[int] = Field(default_factory=list)
    pgns_received: list[int] = Field(default_factory=list)
    drop_cable_length_m: Optional[float] = Field(None, ge=0.1, le=10.0)
    current_draw_ma: Optional[float] = Field(None, ge=0, le=2000)
    last_seen: Optional[datetime] = None


class NMEANetworkDiagnostics(BaseModel):
    """NMEA 2000 network diagnostic results."""

    model_config = {"from_attributes": True}

    topology: NMEANetworkTopology
    devices: list[NMEADevice] = Field(default_factory=list)
    total_current_draw_ma: Optional[float] = None
    bus_load_percent: Optional[float] = Field(None, ge=0, le=100)
    error_count_24h: int = Field(0, ge=0)
    termination_correct: bool = True
    backbone_within_spec: bool = True
    drops_within_spec: bool = True
    issues: list[str] = Field(default_factory=list)
    confidence: str = "measured"

    def diagnose(self) -> list[str]:
        """Run diagnostic checks and return list of issues."""
        issues = []

        if self.topology.terminator_count != 2:
            issues.append(
                f"Falsche Anzahl Terminatoren: {self.topology.terminator_count} "
                f"(soll: 2). Bus-Impedanz fehlerhaft."
            )

        if self.topology.backbone_length_m > 100:
            issues.append(
                f"Backbone-Länge {self.topology.backbone_length_m} m überschreitet "
                f"Maximum von 100 m."
            )

        if self.topology.max_drop_length_m > 6.0:
            issues.append(
                f"Längste Stichleitung {self.topology.max_drop_length_m} m "
                f"überschreitet Maximum von 6 m."
            )

        if self.topology.device_count > 50:
            issues.append(
                f"Geräteanzahl {self.topology.device_count} überschreitet "
                f"Maximum von 50 pro Segment."
            )

        if self.total_current_draw_ma is not None:
            max_current = self.topology.power_supply_amps * 1000
            if self.total_current_draw_ma > max_current:
                issues.append(
                    f"Stromverbrauch {self.total_current_draw_ma} mA überschreitet "
                    f"Netzteil-Kapazität von {max_current} mA."
                )

        offline_devices = [d for d in self.devices if d.status == NMEADeviceStatus.OFFLINE]
        if offline_devices:
            names = ", ".join(d.device_name for d in offline_devices)
            issues.append(f"Offline-Geräte: {names}")

        intermittent = [d for d in self.devices if d.status == NMEADeviceStatus.INTERMITTENT]
        if intermittent:
            names = ", ".join(d.device_name for d in intermittent)
            issues.append(f"Instabile Geräte: {names}")

        self.issues = issues
        return issues
```

---

## ANHANG K — Pydantic v2 Modelle: Instrumentenbewertung

```python
"""
AYDI Pydantic v2 Models — Instrument Assessment and Scoring
All models use model_config = {"from_attributes": True}
NEVER use class Config — always use model_config dict.
"""

from __future__ import annotations
from datetime import datetime
from enum import Enum
from typing import Optional
from pydantic import BaseModel, Field, field_validator


class InstrumentCategory(str, Enum):
    """Categories of marine instruments for assessment."""
    WIND = "wind"
    SPEED = "speed"
    DEPTH = "depth"
    COMPASS = "compass"
    BAROMETER = "barometer"
    TANK = "tank"
    TEMPERATURE = "temperature"
    INCLINOMETER = "inclinometer"
    TACHOMETER = "tachometer"
    DISPLAY = "display"
    PROCESSOR = "processor"
    NETWORK = "network"


class AssessmentSeverity(str, Enum):
    """Severity levels for instrument findings."""
    CRITICAL = "critical"       # Safety risk
    WARNING = "warning"         # Performance impact
    INFO = "info"              # Improvement suggestion
    OK = "ok"                  # No issue


class InstrumentFinding(BaseModel):
    """A single finding during instrument assessment."""

    model_config = {"from_attributes": True}

    finding_id: str = Field(..., description="Unique finding identifier")
    category: InstrumentCategory
    severity: AssessmentSeverity
    title_de: str = Field(..., description="Finding title in German")
    description_de: str = Field(..., description="Finding description in German")
    suggestion_de: str = Field(..., description="Improvement suggestion in German")
    location: Optional[str] = Field(None, description="Physical location on yacht")
    estimated_cost_eur: Optional[float] = Field(None, ge=0)
    confidence: str = "estimated"
    error_code: Optional[str] = Field(None, description="Reference to Fehlerbild-Atlas")


class InstrumentScore(BaseModel):
    """Score for a single instrument category."""

    model_config = {"from_attributes": True}

    category: InstrumentCategory
    score: float = Field(..., ge=0, le=100, description="Score 0-100")
    max_possible: float = Field(100.0, ge=0, le=100)
    weight: float = Field(1.0, ge=0, le=5.0, description="Category weight")
    findings: list[InstrumentFinding] = Field(default_factory=list)
    available: bool = True
    reason_unavailable: Optional[str] = None
    confidence: str = "estimated"

    @field_validator("score")
    @classmethod
    def validate_score(cls, v: float) -> float:
        return round(v, 1)


class InstrumentAssessment(BaseModel):
    """Complete instrument assessment for a yacht."""

    model_config = {"from_attributes": True}

    yacht_id: str
    assessment_date: datetime = Field(default_factory=datetime.utcnow)
    assessor: str = Field("aydi_engine", description="'aydi_engine' or surveyor name")
    boat_class: str = Field(..., description="Boat class for calibration")
    ce_category: Optional[str] = Field(None, description="A, B, C, or D")

    # Individual scores
    scores: list[InstrumentScore] = Field(default_factory=list)

    # Network assessment
    nmea_protocol: Optional[str] = None
    network_score: Optional[float] = Field(None, ge=0, le=100)

    # Overall
    overall_score: Optional[float] = Field(None, ge=0, le=100)
    safety_critical_issues: int = Field(0, ge=0)
    total_findings: int = Field(0, ge=0)
    estimated_upgrade_cost_eur: Optional[float] = Field(None, ge=0)

    confidence: str = "estimated"

    def calculate_overall_score(self) -> float:
        """Calculate weighted overall instrument score."""
        if not self.scores:
            return 0.0

        available_scores = [s for s in self.scores if s.available]
        if not available_scores:
            return 0.0

        total_weight = sum(s.weight for s in available_scores)
        if total_weight == 0:
            return 0.0

        weighted_sum = sum(s.score * s.weight for s in available_scores)
        self.overall_score = round(weighted_sum / total_weight, 1)

        self.safety_critical_issues = sum(
            1 for s in self.scores
            for f in s.findings
            if f.severity == AssessmentSeverity.CRITICAL
        )

        self.total_findings = sum(len(s.findings) for s in self.scores)

        return self.overall_score


# Weight configuration per boat type
INSTRUMENT_WEIGHTS = {
    "sailing_cruiser": {
        InstrumentCategory.WIND: 2.0,
        InstrumentCategory.SPEED: 1.5,
        InstrumentCategory.DEPTH: 2.0,
        InstrumentCategory.COMPASS: 2.0,
        InstrumentCategory.BAROMETER: 1.5,
        InstrumentCategory.TANK: 1.0,
        InstrumentCategory.TEMPERATURE: 0.5,
        InstrumentCategory.INCLINOMETER: 0.5,
        InstrumentCategory.TACHOMETER: 0.5,
        InstrumentCategory.DISPLAY: 1.5,
        InstrumentCategory.PROCESSOR: 1.0,
        InstrumentCategory.NETWORK: 1.5,
    },
    "sailing_racer": {
        InstrumentCategory.WIND: 3.0,
        InstrumentCategory.SPEED: 2.5,
        InstrumentCategory.DEPTH: 1.5,
        InstrumentCategory.COMPASS: 2.0,
        InstrumentCategory.BAROMETER: 1.0,
        InstrumentCategory.TANK: 0.5,
        InstrumentCategory.TEMPERATURE: 0.5,
        InstrumentCategory.INCLINOMETER: 1.5,
        InstrumentCategory.TACHOMETER: 0.0,
        InstrumentCategory.DISPLAY: 2.0,
        InstrumentCategory.PROCESSOR: 2.5,
        InstrumentCategory.NETWORK: 2.0,
    },
    "motor_cruiser": {
        InstrumentCategory.WIND: 0.5,
        InstrumentCategory.SPEED: 1.5,
        InstrumentCategory.DEPTH: 2.0,
        InstrumentCategory.COMPASS: 2.0,
        InstrumentCategory.BAROMETER: 1.0,
        InstrumentCategory.TANK: 2.5,
        InstrumentCategory.TEMPERATURE: 1.5,
        InstrumentCategory.INCLINOMETER: 0.5,
        InstrumentCategory.TACHOMETER: 2.0,
        InstrumentCategory.DISPLAY: 1.5,
        InstrumentCategory.PROCESSOR: 0.5,
        InstrumentCategory.NETWORK: 1.5,
    },
    "superyacht": {
        InstrumentCategory.WIND: 1.0,
        InstrumentCategory.SPEED: 1.5,
        InstrumentCategory.DEPTH: 2.0,
        InstrumentCategory.COMPASS: 2.5,
        InstrumentCategory.BAROMETER: 1.5,
        InstrumentCategory.TANK: 2.5,
        InstrumentCategory.TEMPERATURE: 2.0,
        InstrumentCategory.INCLINOMETER: 1.0,
        InstrumentCategory.TACHOMETER: 2.0,
        InstrumentCategory.DISPLAY: 2.0,
        InstrumentCategory.PROCESSOR: 1.5,
        InstrumentCategory.NETWORK: 2.5,
    },
}
```

---

## ANHANG L — Pydantic v2 Modelle: Windkalibrierung

```python
"""
AYDI Pydantic v2 Models — Wind Calibration
All models use model_config = {"from_attributes": True}
NEVER use class Config — always use model_config dict.
"""

from __future__ import annotations
from datetime import datetime
from typing import Optional
from pydantic import BaseModel, Field, field_validator


class WindCalibrationPoint(BaseModel):
    """A single calibration data point from circle sailing."""

    model_config = {"from_attributes": True}

    heading_deg: float = Field(..., ge=0, le=360, description="Compass heading [°]")
    awa_deg: float = Field(..., ge=-180, le=180, description="Measured AWA [°]")
    aws_kn: float = Field(..., ge=0, le=150, description="Measured AWS [kn]")
    stw_kn: float = Field(..., ge=0, le=50, description="Speed through water [kn]")
    heel_deg: float = Field(0.0, ge=-45, le=45, description="Heel angle [°]")
    sog_kn: Optional[float] = Field(None, ge=0, le=50)
    cog_deg: Optional[float] = Field(None, ge=0, le=360)
    timestamp: datetime = Field(default_factory=datetime.utcnow)
    duration_s: float = Field(60.0, ge=10, le=600, description="Sampling duration [s]")


class UpwashCorrectionTable(BaseModel):
    """Upwash correction table for wind calibration."""

    model_config = {"from_attributes": True}

    boat_name: str
    calibration_date: datetime
    reference_tws_kn: float = Field(..., ge=0, le=80)
    corrections: list[UpwashCorrectionEntry] = Field(default_factory=list)
    valid_tws_range_kn: tuple[float, float] = (5.0, 25.0)
    confidence: str = "measured"

    def get_correction(self, awa_deg: float) -> float:
        """Interpolate upwash correction for given AWA."""
        if not self.corrections:
            return 0.0

        # Find surrounding entries
        sorted_entries = sorted(self.corrections, key=lambda e: e.awa_deg)

        if awa_deg <= sorted_entries[0].awa_deg:
            return sorted_entries[0].upwash_correction_deg

        if awa_deg >= sorted_entries[-1].awa_deg:
            return sorted_entries[-1].upwash_correction_deg

        # Linear interpolation
        for i in range(len(sorted_entries) - 1):
            if sorted_entries[i].awa_deg <= awa_deg <= sorted_entries[i + 1].awa_deg:
                fraction = (
                    (awa_deg - sorted_entries[i].awa_deg)
                    / (sorted_entries[i + 1].awa_deg - sorted_entries[i].awa_deg)
                )
                return (
                    sorted_entries[i].upwash_correction_deg
                    + fraction * (
                        sorted_entries[i + 1].upwash_correction_deg
                        - sorted_entries[i].upwash_correction_deg
                    )
                )

        return 0.0


class UpwashCorrectionEntry(BaseModel):
    """Single entry in the upwash correction table."""

    model_config = {"from_attributes": True}

    awa_deg: float = Field(..., ge=0, le=180, description="AWA for this correction [°]")
    upwash_correction_deg: float = Field(
        ..., ge=-15, le=15, description="Upwash correction to apply [°]"
    )
    aws_correction_percent: float = Field(
        0.0, ge=-20, le=20, description="AWS speed correction [%]"
    )


class WindCalibrationResult(BaseModel):
    """Result of a wind calibration session."""

    model_config = {"from_attributes": True}

    boat_id: str
    calibration_date: datetime = Field(default_factory=datetime.utcnow)
    calibration_points: list[WindCalibrationPoint] = Field(default_factory=list)
    upwash_table: Optional[UpwashCorrectionTable] = None
    heading_offset_deg: float = Field(0.0, ge=-10, le=10)
    speed_calibration_factor: float = Field(1.0, ge=0.8, le=1.2)
    twa_asymmetry_deg: Optional[float] = Field(
        None, ge=0, le=20, description="Max TWA asymmetry Stb/Bb [°]"
    )
    quality_score: float = Field(0.0, ge=0, le=100, description="Calibration quality [0-100]")
    confidence: str = "measured"

    def assess_quality(self) -> float:
        """Assess the quality of the calibration data."""
        score = 100.0

        n_points = len(self.calibration_points)
        if n_points < 12:
            score -= (12 - n_points) * 5  # -5 per missing heading
        if n_points < 6:
            score -= 30  # Major penalty for too few points

        if self.twa_asymmetry_deg is not None:
            if self.twa_asymmetry_deg > 5:
                score -= (self.twa_asymmetry_deg - 5) * 5
            if self.twa_asymmetry_deg > 10:
                score -= 20

        self.quality_score = max(0.0, min(100.0, score))
        return self.quality_score
```

---

## ANHANG M — Pydantic v2 Modelle: Fehlerbild-Referenz

```python
"""
AYDI Pydantic v2 Models — Instrument Error Pattern Reference
All models use model_config = {"from_attributes": True}
NEVER use class Config — always use model_config dict.
"""

from __future__ import annotations
from enum import Enum
from typing import Optional
from pydantic import BaseModel, Field


class ErrorSeverity(str, Enum):
    """Severity of an instrument error."""
    CRITICAL = "critical"
    MAJOR = "major"
    MINOR = "minor"
    COSMETIC = "cosmetic"


class ErrorCategory(str, Enum):
    """Category of instrument error."""
    MECHANICAL = "mechanical"
    ELECTRICAL = "electrical"
    CALIBRATION = "calibration"
    ENVIRONMENTAL = "environmental"
    INSTALLATION = "installation"
    NETWORK = "network"
    SOFTWARE = "software"


class ErrorCause(BaseModel):
    """A possible cause for an instrument error."""

    model_config = {"from_attributes": True}

    rank: int = Field(..., ge=1, le=10)
    cause_de: str = Field(..., description="Cause description in German")
    probability_percent: float = Field(..., ge=0, le=100)
    verification_de: str = Field(..., description="How to verify this cause (German)")
    fix_de: str = Field(..., description="How to fix this cause (German)")
    estimated_cost_eur: Optional[float] = Field(None, ge=0)
    diy_possible: bool = True
    tools_required: list[str] = Field(default_factory=list)


class InstrumentErrorPattern(BaseModel):
    """A documented instrument error pattern (Fehlerbild)."""

    model_config = {"from_attributes": True}

    error_id: str = Field(..., description="Error ID, e.g. 'FB-INST-001'")
    title_de: str = Field(..., description="Error title in German")
    symptom_de: str = Field(..., description="Observable symptom in German")
    affected_sensors: list[str] = Field(default_factory=list)
    severity: ErrorSeverity
    category: ErrorCategory
    causes: list[ErrorCause] = Field(default_factory=list)
    frequency: str = Field("common", description="'rare', 'uncommon', 'common', 'very_common'")
    boat_types_affected: list[str] = Field(
        default_factory=lambda: ["all"]
    )
    related_errors: list[str] = Field(default_factory=list)
    confidence: str = "documented"

    def get_most_likely_cause(self) -> Optional[ErrorCause]:
        """Return the most probable cause."""
        if not self.causes:
            return None
        return max(self.causes, key=lambda c: c.probability_percent)

    def get_diy_causes(self) -> list[ErrorCause]:
        """Return causes that can be fixed by the owner."""
        return [c for c in self.causes if c.diy_possible]


class ErrorPatternDatabase(BaseModel):
    """Collection of all known instrument error patterns."""

    model_config = {"from_attributes": True}

    patterns: list[InstrumentErrorPattern] = Field(default_factory=list)
    version: str = "1.0.0"
    last_updated: str = "2026-05-13"

    def find_by_symptom(self, keywords: list[str]) -> list[InstrumentErrorPattern]:
        """Find error patterns matching symptom keywords."""
        results = []
        for pattern in self.patterns:
            symptom_lower = pattern.symptom_de.lower()
            if any(kw.lower() in symptom_lower for kw in keywords):
                results.append(pattern)
        return results

    def find_by_sensor(self, sensor_type: str) -> list[InstrumentErrorPattern]:
        """Find error patterns for a specific sensor type."""
        return [
            p for p in self.patterns
            if sensor_type in p.affected_sensors or "all" in p.affected_sensors
        ]
```

---

## ANHANG N — Pydantic v2 Modelle: Display-Konfiguration

```python
"""
AYDI Pydantic v2 Models — Display and Instrument Layout Configuration
All models use model_config = {"from_attributes": True}
NEVER use class Config — always use model_config dict.
"""

from __future__ import annotations
from enum import Enum
from typing import Optional
from pydantic import BaseModel, Field


class DisplayPosition(str, Enum):
    """Position of instrument display on the yacht."""
    HELM_PRIMARY = "helm_primary"
    HELM_SECONDARY = "helm_secondary"
    COMPANIONWAY = "companionway"
    CHART_TABLE = "chart_table"
    MAST_BASE = "mast_base"
    COCKPIT_BULKHEAD = "cockpit_bulkhead"
    FLYBRIDGE = "flybridge"
    SALON = "salon"


class DisplayDataField(BaseModel):
    """A single data field on an instrument display page."""

    model_config = {"from_attributes": True}

    field_position: int = Field(..., ge=1, le=8, description="Position on display page")
    data_type: str = Field(..., description="NMEA data type, e.g. 'aws', 'depth', 'stw'")
    label_de: str = Field(..., description="Display label in German")
    unit: str = Field(..., description="Display unit, e.g. 'kn', 'm', '°C'")
    dampening_s: float = Field(3.0, ge=0, le=120, description="Smoothing time [s]")
    alarm_low: Optional[float] = None
    alarm_high: Optional[float] = None
    decimal_places: int = Field(1, ge=0, le=3)
    font_size: str = Field("large", description="'small', 'medium', 'large', 'xlarge'")


class DisplayPage(BaseModel):
    """A single display page configuration."""

    model_config = {"from_attributes": True}

    page_number: int = Field(..., ge=1, le=20)
    page_name_de: str = Field(..., description="Page name in German")
    fields: list[DisplayDataField] = Field(default_factory=list)
    auto_switch: bool = Field(False, description="Auto-switch to this page on alarm")
    refresh_rate_hz: float = Field(1.0, ge=0.1, le=10.0)


class InstrumentDisplayConfig(BaseModel):
    """Complete configuration for a single instrument display."""

    model_config = {"from_attributes": True}

    display_id: str
    manufacturer: str
    model: str
    position: DisplayPosition
    screen_size_inch: float = Field(..., ge=2.0, le=16.0)
    pages: list[DisplayPage] = Field(default_factory=list)
    brightness_percent: float = Field(80.0, ge=0, le=100)
    night_mode_enabled: bool = True
    night_color: str = Field("red", description="'red', 'green', 'white', 'amber'")
    backlight_auto: bool = True
    buzzer_enabled: bool = True


class HelmInstrumentLayout(BaseModel):
    """Layout of all instruments at a helm station."""

    model_config = {"from_attributes": True}

    helm_id: str = Field(..., description="Helm station identifier")
    helm_position: str = Field(..., description="'main', 'flybridge', 'backup'")
    displays: list[InstrumentDisplayConfig] = Field(default_factory=list)
    analog_instruments: list[str] = Field(
        default_factory=list,
        description="List of analog instrument types present"
    )
    mfd_present: bool = False
    mfd_model: Optional[str] = None
    autopilot_control: bool = False
    autopilot_model: Optional[str] = None
    visibility_score: float = Field(
        0.0, ge=0, le=100,
        description="How well instruments are visible from helm"
    )
    ergonomic_score: float = Field(
        0.0, ge=0, le=100,
        description="Ergonomic assessment of instrument placement"
    )
```

---

## ANHANG O — Pydantic v2 Modelle: Sensor-Wartungsplanung

```python
"""
AYDI Pydantic v2 Models — Sensor Maintenance Planning
All models use model_config = {"from_attributes": True}
NEVER use class Config — always use model_config dict.
"""

from __future__ import annotations
from datetime import datetime, timedelta
from enum import Enum
from typing import Optional
from pydantic import BaseModel, Field


class MaintenanceInterval(str, Enum):
    """Standard maintenance intervals."""
    WEEKLY = "weekly"
    MONTHLY = "monthly"
    QUARTERLY = "quarterly"
    SEASONAL = "seasonal"
    ANNUAL = "annual"
    BIENNIAL = "biennial"
    AS_NEEDED = "as_needed"


class MaintenanceTask(BaseModel):
    """A single maintenance task for a sensor or instrument."""

    model_config = {"from_attributes": True}

    task_id: str
    sensor_category: str = Field(..., description="Instrument category")
    task_de: str = Field(..., description="Task description in German")
    interval: MaintenanceInterval
    estimated_time_min: int = Field(..., ge=5, le=480)
    tools_required: list[str] = Field(default_factory=list)
    materials_required: list[str] = Field(default_factory=list)
    diy_difficulty: str = Field("easy", description="'easy', 'medium', 'hard', 'professional'")
    estimated_cost_eur: float = Field(0.0, ge=0)
    safety_relevant: bool = False
    last_performed: Optional[datetime] = None
    next_due: Optional[datetime] = None

    def is_overdue(self) -> bool:
        """Check if this maintenance task is overdue."""
        if self.next_due is None:
            return False
        return datetime.utcnow() > self.next_due

    def days_until_due(self) -> Optional[int]:
        """Return number of days until task is due (negative if overdue)."""
        if self.next_due is None:
            return None
        delta = self.next_due - datetime.utcnow()
        return delta.days


class SensorMaintenancePlan(BaseModel):
    """Complete maintenance plan for all instruments on a yacht."""

    model_config = {"from_attributes": True}

    yacht_id: str
    plan_created: datetime = Field(default_factory=datetime.utcnow)
    season_start: str = Field("april", description="Month when season starts")
    season_end: str = Field("october", description="Month when season ends")
    tasks: list[MaintenanceTask] = Field(default_factory=list)
    total_annual_cost_eur: Optional[float] = Field(None, ge=0)
    total_annual_time_hours: Optional[float] = Field(None, ge=0)

    def get_overdue_tasks(self) -> list[MaintenanceTask]:
        """Get all overdue maintenance tasks."""
        return [t for t in self.tasks if t.is_overdue()]

    def get_seasonal_tasks(self) -> list[MaintenanceTask]:
        """Get tasks due at season start."""
        return [t for t in self.tasks if t.interval == MaintenanceInterval.SEASONAL]

    def calculate_annual_totals(self) -> None:
        """Calculate total annual cost and time."""
        interval_multiplier = {
            MaintenanceInterval.WEEKLY: 26,  # ~26 weeks sailing season
            MaintenanceInterval.MONTHLY: 7,  # ~7 months season
            MaintenanceInterval.QUARTERLY: 3,
            MaintenanceInterval.SEASONAL: 1,
            MaintenanceInterval.ANNUAL: 1,
            MaintenanceInterval.BIENNIAL: 0.5,
            MaintenanceInterval.AS_NEEDED: 2,  # Assume twice per year
        }

        total_cost = 0.0
        total_time = 0.0

        for task in self.tasks:
            multiplier = interval_multiplier.get(task.interval, 1)
            total_cost += task.estimated_cost_eur * multiplier
            total_time += (task.estimated_time_min / 60) * multiplier

        self.total_annual_cost_eur = round(total_cost, 2)
        self.total_annual_time_hours = round(total_time, 1)


# Default maintenance tasks for common instruments
DEFAULT_MAINTENANCE_TASKS = [
    MaintenanceTask(
        task_id="MT-WIND-01",
        sensor_category="wind",
        task_de="Windgeber visuell prüfen (Schalenkreuz frei drehbar, Fahne beweglich)",
        interval=MaintenanceInterval.MONTHLY,
        estimated_time_min=5,
        tools_required=["Fernglas"],
        diy_difficulty="easy",
        safety_relevant=True,
    ),
    MaintenanceTask(
        task_id="MT-WIND-02",
        sensor_category="wind",
        task_de="Masttopp-Steckverbindung prüfen und Kontaktspray auftragen",
        interval=MaintenanceInterval.ANNUAL,
        estimated_time_min=30,
        tools_required=["Bootsmannstuhl", "Kontaktspray", "Isolierband"],
        diy_difficulty="medium",
        estimated_cost_eur=15.0,
        safety_relevant=True,
    ),
    MaintenanceTask(
        task_id="MT-LOG-01",
        sensor_category="speed",
        task_de="Paddle-Wheel-Geber herausziehen, reinigen, Lager prüfen",
        interval=MaintenanceInterval.MONTHLY,
        estimated_time_min=15,
        tools_required=["Blindstopfen"],
        materials_required=["Frischwasser", "Bürste"],
        diy_difficulty="easy",
        safety_relevant=False,
    ),
    MaintenanceTask(
        task_id="MT-LOG-02",
        sensor_category="speed",
        task_de="Log-Kalibrierung gegen GPS-SOG prüfen (Vergleichsfahrt 30 min)",
        interval=MaintenanceInterval.SEASONAL,
        estimated_time_min=45,
        diy_difficulty="medium",
        safety_relevant=False,
    ),
    MaintenanceTask(
        task_id="MT-DEPTH-01",
        sensor_category="depth",
        task_de="Echolotgeber (Durchbruch) auf Bewuchs prüfen und reinigen",
        interval=MaintenanceInterval.SEASONAL,
        estimated_time_min=20,
        tools_required=["Schaber", "Schleifpapier 240er"],
        diy_difficulty="easy",
        estimated_cost_eur=5.0,
        safety_relevant=True,
    ),
    MaintenanceTask(
        task_id="MT-COMPASS-01",
        sensor_category="compass",
        task_de="Kompass-Kompensation durchführen (Kreisdrehen bei ruhiger See)",
        interval=MaintenanceInterval.ANNUAL,
        estimated_time_min=45,
        diy_difficulty="medium",
        safety_relevant=True,
    ),
    MaintenanceTask(
        task_id="MT-NMEA-01",
        sensor_category="network",
        task_de="Alle NMEA-2000-Steckverbindungen auf Korrosion prüfen",
        interval=MaintenanceInterval.ANNUAL,
        estimated_time_min=60,
        tools_required=["Kontaktspray", "Visuell"],
        estimated_cost_eur=10.0,
        diy_difficulty="easy",
        safety_relevant=False,
    ),
    MaintenanceTask(
        task_id="MT-TANK-01",
        sensor_category="tank",
        task_de="Tankgeber-Anzeige bei vollem und leerem Tank prüfen",
        interval=MaintenanceInterval.SEASONAL,
        estimated_time_min=15,
        diy_difficulty="easy",
        safety_relevant=False,
    ),
    MaintenanceTask(
        task_id="MT-BARO-01",
        sensor_category="barometer",
        task_de="Barometer gegen Referenz prüfen (Flughafen-METAR oder Wetterstation)",
        interval=MaintenanceInterval.ANNUAL,
        estimated_time_min=10,
        diy_difficulty="easy",
        safety_relevant=True,
    ),
    MaintenanceTask(
        task_id="MT-DISPLAY-01",
        sensor_category="display",
        task_de="Alle Displays auf Pixelfehler, Hintergrundbeleuchtung und Dichtigkeit prüfen",
        interval=MaintenanceInterval.SEASONAL,
        estimated_time_min=15,
        diy_difficulty="easy",
        safety_relevant=False,
    ),
]
```

---

## ANHANG P — Pydantic v2 Modelle: Sensor-Empfehlung

```python
"""
AYDI Pydantic v2 Models — Sensor Recommendation Engine
All models use model_config = {"from_attributes": True}
NEVER use class Config — always use model_config dict.
"""

from __future__ import annotations
from enum import Enum
from typing import Optional
from pydantic import BaseModel, Field


class PriceSegment(str, Enum):
    """Price segments for instrument recommendations."""
    BUDGET = "budget"
    MID_RANGE = "mid_range"
    PREMIUM = "premium"
    PROFESSIONAL = "professional"


class BoatUseCase(str, Enum):
    """Primary use case for instrument recommendation."""
    COASTAL_CRUISING = "coastal_cruising"
    OFFSHORE_CRUISING = "offshore_cruising"
    RACING = "racing"
    MOTOR_CRUISING = "motor_cruising"
    SUPERYACHT = "superyacht"
    DAYSAILING = "daysailing"
    CHARTER = "charter"


class SensorRecommendation(BaseModel):
    """A specific sensor product recommendation."""

    model_config = {"from_attributes": True}

    sensor_category: str
    manufacturer: str
    model_name: str
    price_eur: float = Field(..., ge=0)
    price_segment: PriceSegment
    suitability_score: float = Field(..., ge=0, le=100)
    pros_de: list[str] = Field(default_factory=list)
    cons_de: list[str] = Field(default_factory=list)
    installation_complexity: str = Field(
        "medium", description="'simple', 'medium', 'complex', 'professional'"
    )
    requires_hull_penetration: bool = False
    nmea_2000_native: bool = True
    notes_de: Optional[str] = None


class InstrumentRecommendationRequest(BaseModel):
    """Request for instrument recommendations."""

    model_config = {"from_attributes": True}

    boat_length_m: float = Field(..., ge=4, le=80)
    boat_type: str = Field(..., description="'sail', 'motor', 'multihull_sail', 'multihull_motor'")
    hull_material: str = Field(..., description="'grp', 'steel', 'aluminum', 'wood', 'composite'")
    use_case: BoatUseCase
    budget_eur: Optional[float] = Field(None, ge=0)
    existing_nmea_protocol: Optional[str] = None
    existing_instruments: list[str] = Field(default_factory=list)
    ce_category: Optional[str] = Field(None, description="A, B, C, or D")
    priorities: list[str] = Field(
        default_factory=list,
        description="Priority areas: 'safety', 'performance', 'comfort', 'value'"
    )


class InstrumentRecommendationResponse(BaseModel):
    """Complete instrument recommendation for a yacht."""

    model_config = {"from_attributes": True}

    request: InstrumentRecommendationRequest
    recommendations: list[SensorRecommendation] = Field(default_factory=list)
    total_cost_eur: float = Field(0.0, ge=0)
    installation_cost_estimate_eur: float = Field(0.0, ge=0)
    summary_de: str = Field("", description="Summary recommendation in German")
    warnings_de: list[str] = Field(default_factory=list)
    confidence: str = "estimated"

    def calculate_totals(self) -> None:
        """Calculate total costs from recommendations."""
        self.total_cost_eur = sum(r.price_eur for r in self.recommendations)
        # Rough installation estimate: 40% of hardware cost
        self.installation_cost_estimate_eur = round(self.total_cost_eur * 0.4, 2)
```

---

## ANHANG Q — Pydantic v2 Modelle: Datenlogging

```python
"""
AYDI Pydantic v2 Models — Sensor Data Logging
All models use model_config = {"from_attributes": True}
NEVER use class Config — always use model_config dict.
"""

from __future__ import annotations
from datetime import datetime
from typing import Optional
from pydantic import BaseModel, Field


class SensorLogEntry(BaseModel):
    """A single logged sensor data point."""

    model_config = {"from_attributes": True}

    timestamp: datetime
    sensor_id: str
    data_type: str = Field(..., description="PGN name or sensor type")
    value: float
    unit: str
    quality: str = Field("good", description="'good', 'suspect', 'bad', 'missing'")
    source: str = Field("nmea_2000", description="Data source identifier")


class SensorLogSession(BaseModel):
    """A logging session with metadata."""

    model_config = {"from_attributes": True}

    session_id: str
    yacht_id: str
    start_time: datetime
    end_time: Optional[datetime] = None
    sample_rate_hz: float = Field(1.0, ge=0.1, le=10.0)
    entries_count: int = Field(0, ge=0)
    sensors_logged: list[str] = Field(default_factory=list)
    trip_distance_nm: Optional[float] = Field(None, ge=0)
    notes: Optional[str] = None


class SensorDataSummary(BaseModel):
    """Statistical summary of logged sensor data."""

    model_config = {"from_attributes": True}

    sensor_id: str
    data_type: str
    unit: str
    period_start: datetime
    period_end: datetime
    sample_count: int = Field(0, ge=0)
    value_min: Optional[float] = None
    value_max: Optional[float] = None
    value_mean: Optional[float] = None
    value_median: Optional[float] = None
    value_std_dev: Optional[float] = None
    quality_good_percent: float = Field(100.0, ge=0, le=100)
    quality_suspect_percent: float = Field(0.0, ge=0, le=100)
    quality_bad_percent: float = Field(0.0, ge=0, le=100)
    gaps_count: int = Field(0, ge=0, description="Number of data gaps")
    longest_gap_seconds: Optional[float] = Field(None, ge=0)


class SensorHealthReport(BaseModel):
    """Health report for a sensor based on logged data analysis."""

    model_config = {"from_attributes": True}

    sensor_id: str
    sensor_type: str
    report_date: datetime = Field(default_factory=datetime.utcnow)
    analysis_period_days: int = Field(30, ge=1)
    data_availability_percent: float = Field(0.0, ge=0, le=100)
    data_quality_score: float = Field(0.0, ge=0, le=100)
    drift_detected: bool = False
    drift_rate_per_day: Optional[float] = None
    anomalies_count: int = Field(0, ge=0)
    calibration_recommended: bool = False
    replacement_recommended: bool = False
    findings_de: list[str] = Field(default_factory=list)
    confidence: str = "calculated"
```

---

## ANHANG R — Pydantic v2 Modelle: Visuelle Analyse von Instrumenten

```python
"""
AYDI Pydantic v2 Models — Visual Analysis of Instrument Installations
All models use model_config = {"from_attributes": True}
NEVER use class Config — always use model_config dict.
"""

from __future__ import annotations
from datetime import datetime
from enum import Enum
from typing import Optional
from pydantic import BaseModel, Field


class VisualConfidence(str, Enum):
    """Confidence levels specific to visual analysis."""
    HIGH = "visual_high"
    MEDIUM = "visual_medium"
    LOW = "visual_low"
    INSUFFICIENT = "visual_insufficient"


class InstrumentVisualFinding(BaseModel):
    """A finding from visual analysis of instrument installation."""

    model_config = {"from_attributes": True}

    finding_id: str
    category: str = Field(..., description="Instrument category assessed")
    description_de: str = Field(..., description="What was observed (German)")
    assessment_de: str = Field(..., description="Assessment of observation (German)")
    suggestion_de: str = Field(..., description="Improvement suggestion (German)")
    severity: str = Field("info", description="'critical', 'warning', 'info', 'ok'")
    confidence: VisualConfidence
    image_region: Optional[str] = Field(
        None, description="Description of the image region analyzed"
    )


class InstrumentVisualAnalysis(BaseModel):
    """Complete visual analysis of instrument installation from photos."""

    model_config = {"from_attributes": True}

    analysis_id: str
    yacht_id: str
    analysis_date: datetime = Field(default_factory=datetime.utcnow)
    images_analyzed: int = Field(0, ge=0)
    model_version: str = Field(..., description="AI model version used")

    # What was identified
    instruments_identified: list[str] = Field(default_factory=list)
    manufacturers_identified: list[str] = Field(default_factory=list)
    bus_type_estimated: Optional[str] = None
    installation_age_estimated: Optional[str] = Field(
        None, description="'new', 'recent', 'mature', 'old', 'obsolete'"
    )

    # Assessment
    findings: list[InstrumentVisualFinding] = Field(default_factory=list)
    layout_score: Optional[float] = Field(
        None, ge=0, le=100, description="Instrument layout/ergonomics score"
    )
    condition_score: Optional[float] = Field(
        None, ge=0, le=100, description="Visual condition score"
    )
    completeness_score: Optional[float] = Field(
        None, ge=0, le=100, description="Completeness of instrumentation"
    )
    integration_score: Optional[float] = Field(
        None, ge=0, le=100, description="System integration level"
    )
    overall_visual_score: Optional[float] = Field(None, ge=0, le=100)
    overall_confidence: VisualConfidence = VisualConfidence.MEDIUM

    # Limitations
    not_assessable_de: list[str] = Field(
        default_factory=list,
        description="Aspects that could not be assessed from photos (German)"
    )

    def calculate_overall(self) -> float:
        """Calculate overall visual score from component scores."""
        scores = [
            s for s in [
                self.layout_score,
                self.condition_score,
                self.completeness_score,
                self.integration_score,
            ]
            if s is not None
        ]
        if not scores:
            return 0.0

        weights = {
            "layout": 0.20,
            "condition": 0.30,
            "completeness": 0.25,
            "integration": 0.25,
        }

        weighted_scores = []
        if self.layout_score is not None:
            weighted_scores.append(self.layout_score * weights["layout"])
        if self.condition_score is not None:
            weighted_scores.append(self.condition_score * weights["condition"])
        if self.completeness_score is not None:
            weighted_scores.append(self.completeness_score * weights["completeness"])
        if self.integration_score is not None:
            weighted_scores.append(self.integration_score * weights["integration"])

        total_weight = sum(
            w for key, w in weights.items()
            if getattr(self, f"{key}_score") is not None
        )

        if total_weight == 0:
            return 0.0

        self.overall_visual_score = round(sum(weighted_scores) / total_weight, 1)
        return self.overall_visual_score
```
