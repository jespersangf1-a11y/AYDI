---
title: "Windfahnen-Selbststeueranlagen"
kategorie: "21 Selbststeueranlagen"
unterkategorie: "21.03 Windfahnen-Selbststeueranlagen"
version: "1.0.0"
datum: "2026-05-02"
autor: "AYDI Research"
status: "validated"
confidence_quellen:
  - measured: "Hersteller-TDS, ISO-Normen, CE-Zertifizierungen"
  - documented: "Hersteller-Kataloge, Langfahrt-Literatur, Werftunterlagen"
  - estimated: "Erfahrungswerte, Langfahrt-Praxis, Segler-Konsens"
---

# 21.03 — Windfahnen-Selbststeueranlagen im Yachtbau: Vollständige Wissensreferenz

> **AYDI Wissensdatei 21.03** — Kategorie 21: Selbststeueranlagen
> **Confidence-Quelle:** measured (Hersteller-TDS, ISO-Normen), documented (Hersteller-Kataloge, Langfahrt-Literatur), estimated (Erfahrungswerte, Langfahrt-Praxis)
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
8. [FAQ](#8-faq)
9. [Glossar](#9-glossar)
10. [Schnell-Referenz](#10-schnell-referenz)
11. [ANHANG A–H — Fallstudien](#11-anhang-a-h--fallstudien)
12. [ANHANG I–R — Pydantic v2 Modelle](#12-anhang-i-r--pydantic-v2-modelle)

---

## 1. Einführung und Übersicht

### 1.1 Definition und Abgrenzung

Windfahnen-Selbststeueranlagen (engl. wind vane self-steering systems) sind mechanische Steuervorrichtungen, die ein Segelboot ohne elektrische Energie auf einem konstanten Kurs relativ zum scheinbaren Wind halten. Sie nutzen ausschließlich die Kraft des Windes und die Strömungsenergie des Wassers als Antrieb für die Ruderkorrekturen.

Die grundlegende Funktionskette besteht aus vier Elementen:

1. **Windfahne (Sensor)** — Detektiert Abweichungen vom eingestellten Kurs relativ zum scheinbaren Wind
2. **Übertragungsmechanik (Verstärker)** — Wandelt die geringe Kraft der Windfahne in eine nutzbare Steuerkraft um
3. **Servoelement (Aktuator)** — Erzeugt die eigentliche Ruderkraft durch Umlenkung hydrodynamischer Energie
4. **Ruder (Effektor)** — Bringt die Steuerkraft auf das Boot und korrigiert den Kurs

Im Gegensatz zu elektrischen Autopiloten:

| Eigenschaft | Windfahne | Elektrischer Autopilot |
|---|---|---|
| Energiebedarf | 0 Watt | 15–120 Watt (Dauerbetrieb) |
| Kursreferenz | Scheinbarer Wind | Kompass (magnetisch/GPS) |
| Kurshalten bei Winddreh | Folgt automatisch | Muss nachgestellt werden |
| Kurshalten bei Wellengang | Sehr gut (mechanische Dämpfung) | Mäßig bis gut (abhängig von Sensorik) |
| Vor-Wind-Performance | Eingeschränkt | Gut bis sehr gut |
| Wartung | Mechanisch, einfach | Elektronik + Mechanik |
| Lebensdauer | 20–40 Jahre | 5–15 Jahre |
| Anschaffungskosten | 3.000–7.000 € | 1.500–8.000 € |
| Gewicht am Heck | 12–35 kg | 2–8 kg (Antriebseinheit) |
| Zuverlässigkeit Langfahrt | Sehr hoch | Hoch (aber Elektronik-Risiko) |

### 1.2 Historische Entwicklung

**Vor 1960 — Pionierphase:**
- 1936: Marin Marie überquert den Atlantik einhand mit einer primitiven Windfahnensteuerung auf der "Winnibelle"
- 1952: Marcel Bardiaux entwickelt eine einfache Trim-Tab-Steuerung für seine Weltumsegelung
- 1955: Ian Major konstruiert eine der ersten Servo-Pendulum-Anlagen in England
- Frühe Konstruktionen meist Eigenbau, individuelle Lösungen für einzelne Boote

**1960–1975 — Goldenes Zeitalter der Einhandsegler:**
- 1960: Francis Chichester nutzt eine frühe Windfahnensteuerung "Miranda" bei der ersten OSTAR (Observer Single-handed Trans-Atlantic Race)
- 1962: Blondie Hasler perfektioniert das Servo-Pendulum-Prinzip für die OSTAR — der "Hasler Servo-Pendulum" wird zum Prototyp aller modernen Anlagen
- 1966: Hasler/Herbulot veröffentlichen grundlegende Konstruktionsprinzipien
- 1968: Bernard Moitessier segelt mit einer Aries-Anlage in der Golden Globe Race um die Welt
- 1969: Robin Knox-Johnston gewinnt die Golden Globe Race mit einer selbstgebauten Windfahnensteuerung
- Nick Franklin gründet Aries Marine — erste industrielle Serienproduktion
- Peter Matthiesen beginnt die Entwicklung der Windpilot-Systeme in Hamburg

**1975–1990 — Industrialisierung und Diversifizierung:**
- 1975: Peter Matthiesen gründet Windpilot in Hamburg — der Pacific wird zum Marktführer
- 1977: Monitor Wind Vane wird in Kalifornien von Scanmar International (Lars Bergström) entwickelt
- 1978: Hydrovane (ursprünglich von Derek Fawcett in England) wird als Auxiliary-Rudder-System marktreif
- Cape Horn Windvane (Yves Gélinas, Kanada) beginnt Produktion
- Sailomat (Israel) etabliert sich als Hybrid-System
- Zunehmende Standardisierung der Montageadapter für Serienboote

**1990–2010 — Konsolidierung:**
- Marktbereinigung: viele kleine Hersteller verschwinden
- Windpilot, Monitor und Hydrovane dominieren den Markt
- Peter Matthiesen veröffentlicht umfangreiche Fachliteratur über Windfahnensteuerung
- Zunehmende Konkurrenz durch verbesserte elektrische Autopiloten
- Trotzdem stabil hohe Nachfrage im Langfahrtsegment
- Verbesserung der Materialien: hochfeste Aluminiumlegierungen, Edelstahl-Lager, UV-resistente Kunststoffe

**2010–heute — Nischenmarkt mit stabiler Nachfrage:**
- Windpilot Pacific Plus als Premium-Weiterentwicklung
- Monitor weiterhin Marktführer in Nordamerika
- Hydrovane profitiert von zunehmender Beliebtheit als Notruder
- Wachsende Nachfrage durch Langfahrt-Boom (Segelkattmaran-Markt)
- Integration mit elektrischen Autopiloten als hybride Steuerungslösung
- Cape Horn weiter starke Position in der Langfahrt-Szene
- Zunehmend auch Nachrüstlösungen für moderne Serienboote mit breiten Hecks

### 1.3 Langfahrt-Relevanz und Energieunabhängigkeit

Die herausragende Bedeutung von Windfahnen-Selbststeueranlagen für die Langfahrt ergibt sich aus mehreren Faktoren:

**Energiebilanz auf Langfahrt:**

Ein typisches 38-Fuß-Langfahrtboot (z.B. Bavaria 38, Hallberg-Rassy 37, Oyster 395) hat folgendes Energiebudget:

| Verbraucher | Leistung (W) | Betrieb (h/Tag) | Energie (Wh/Tag) |
|---|---|---|---|
| Autopilot (elektrisch) | 40–80 | 20 | 800–1.600 |
| Kühlschrank | 50–80 | 12 | 600–960 |
| Navigation (Plotter, AIS, Radar) | 30–80 | 24 | 720–1.920 |
| Beleuchtung | 10–30 | 8 | 80–240 |
| Kommunikation (UKW, SSB) | 5–100 | 2 | 10–200 |
| Wassermacher (wenn vorhanden) | 60–120 | 2 | 120–240 |
| **Summe ohne Autopilot** | — | — | **1.530–3.560** |
| **Summe mit Autopilot** | — | — | **2.330–5.160** |

Der Autopilot macht typisch 25–40% des gesamten Energieverbrauchs aus. Eine Windfahnensteuerung eliminiert diesen Verbrauch vollständig.

**Energieerzeugung auf Langfahrt:**

| Quelle | Typische Leistung | Energie (Wh/Tag) |
|---|---|---|
| Solarpanels (2 × 100 Wp) | 200 Wp | 600–1.200 (breitenabhängig) |
| Windgenerator | 100–400 W | 500–2.000 (windabhängig) |
| Schleppgenerator | 40–100 W | 400–800 (fahrtabhängig) |
| Lichtmaschine (1h Motor/Tag) | 50–80 A × 14 V | 700–1.120 |
| **Summe (günstige Bedingungen)** | — | **2.200–5.120** |

Die Rechnung zeigt: Ohne Windfahnensteuerung wird die Energiebilanz auf Langfahrt extrem eng, besonders bei Flaute (kein Windgenerator) oder bewölktem Himmel (wenig Solar). Eine Windfahne macht das Energiemanagement deutlich entspannter.

**Redundanz und Sicherheit:**

Auf Langfahrt gilt das Prinzip der doppelten Redundanz für kritische Systeme:

1. **Primärsteuerung:** Windfahne (Energieunabhängig, mechanisch robust)
2. **Sekundärsteuerung:** Elektrischer Autopilot (für Vor-Wind-Kurse, Flaute unter Motor)
3. **Notsteuerung:** Pinne/Steuerrad von Hand

Die Windfahne dient dabei als:
- Primärsystem auf Amwind- und Halbwindkursen (70% der Segelzeit auf Langfahrt)
- Backup für den Autopiloten bei Elektronikausfall
- Notruder-Funktion (bei Auxiliary-Rudder-Systemen wie Hydrovane)

**Segelphilosophie:**

Erfahrene Langfahrtsegler berichten übereinstimmend, dass eine Windfahnensteuerung das Segelerlebnis fundamental verändert:

- Das Boot segelt "organischer" — die Windfahne reagiert auf Böen ähnlich wie ein erfahrener Rudergänger
- Bei Kursschwankungen durch Wellen korrigiert die Windfahne sanfter als ein Autopilot
- Das Boot folgt Winddrehungen automatisch — ideal für Passatsegeln
- Kein Motorlärm zum Batterieladen nötig
- Psychologischer Effekt: Das Vertrauen in ein rein mechanisches System ohne Elektronik-Ausfallrisiko

### 1.4 Bedeutung im AYDI-Analysesystem

Im Kontext des AYDI-Analysesystems sind Windfahnen-Selbststeueranlagen ein relevanter Designparameter für folgende Module:

- **Ergonomie-Modul:** Montageposition, Zugang zum Heck, Beeinflussung der Badeplattform, Leinenführung zum Steuerrad/zur Pinne
- **Compliance-Modul:** CE-Konformität der Montage, Festigkeitsnachweis der Halterung, Gewichtsverteilung am Heck
- **Kosten-Modul:** Anschaffung (3.000–7.000 €), Montage (500–2.000 €), Wartung (100–300 €/Jahr)
- **Strukturanalyse-Modul:** Heck-Belastung, Verstärkungsmaßnahmen, Momentenberechnung
- **Material-Modul:** Korrosionsbeständigkeit (Alu/Edelstahl in Salzwasser), UV-Beständigkeit der Kunststoffteile
- **Gewichts-Modul:** 12–35 kg am äußersten Heck — Einfluss auf Trimm und Schwerpunktlage
- **Marktanalyse-Modul:** Wertsteigernd bei Langfahrt-Yachten, neutral bei reinen Küstenbooten
- **Service-Modul:** Wartungsintervalle, Ersatzteilverfügbarkeit, typische Verschleißmuster

### 1.5 Einsatzbereich und Limitationen

**Optimaler Einsatzbereich:**
- Bootstypen: Segelyachten 26–55 Fuß (8–17 m LüA)
- Kurse: Amwind bis Raumschots (scheinbarer Windwinkel 30°–150°)
- Windstärken: 8–35 Knoten scheinbarer Wind
- Wellenbedingungen: Alle Bedingungen (Vorteil gegenüber Autopilot in schwerer See)
- Fahrtgebiet: Langfahrt, Hochsee, Passage-Making

**Einschränkungen:**
- Vor-Wind-Kurse (scheinbarer Wind <25°): Reduzierte Performance, da scheinbarer Wind schwach
- Leichtwind (<6 kn scheinbar): Windfahne hat zu wenig Kraft für zuverlässige Steuerung
- Motorfahrt bei Flaute: Windfahne funktioniert nicht (kein scheinbarer Wind durch Segel)
- Multihulls: Eingeschränkt geeignet, da geringere Ruderkräfte und spezielle Heckgeometrie
- Regatta: Zu ungenau für enges Kurshalten (±3–5° vs ±1–2° bei Autopilot)
- Boote >55 Fuß: Ruderkräfte übersteigen Kapazität der meisten Anlagen

**Kontraindikationen:**
- Reine Motorboote (kein Wind als Referenz)
- Katamarane mit Mittelruder (Servo-Pendulum nicht adaptierbar)
- Boote ohne geeignete Heckstruktur für Montage
- Rennboote, die exaktes Kurshalten erfordern

---

## 2. Grundlagen und Theorie

### 2.1 Das Windfahnenprinzip

#### 2.1.1 Scheinbarer Wind als Referenz

Die Windfahne nutzt den scheinbaren Wind (apparent wind) als Kursreferenz. Der scheinbare Wind ist die Vektorsumme aus wahrem Wind und Fahrtwind:

```
V_apparent = V_true + V_boat

Wobei:
V_apparent = Scheinbarer Windvektor (Geschwindigkeit und Richtung)
V_true     = Wahrer Windvektor (Geschwindigkeit und Richtung über Grund)
V_boat     = Fahrtwindvektor (Bootsgeschwindigkeit, entgegengesetzt zur Fahrtrichtung)
```

**Konsequenzen für die Windfahnensteuerung:**

1. **Kursänderung bei Winddreh:** Wenn der wahre Wind dreht, dreht auch der scheinbare Wind → die Windfahne korrigiert → das Boot dreht mit dem Wind. Dies ist auf Passatrouten erwünscht (man folgt dem Wind), auf Küstenkursen kann es unerwünscht sein.

2. **Geschwindigkeitsabhängigkeit:** Bei konstanter Geschwindigkeit und konstantem wahren Wind ist der scheinbare Windwinkel konstant → stabiler Kurs. Bei Geschwindigkeitsänderungen (Wellensurf, Flaute) ändert sich der scheinbare Windwinkel → Kursabweichung.

3. **Vor-Wind-Problem:** Auf reinem Vorwindkurs ist der scheinbare Wind = wahrer Wind minus Fahrtwind. Bei Bootsspeed 6 kn und wahrem Wind 12 kn ist der scheinbare Wind nur noch 6 kn — zu wenig für zuverlässige Steuerung.

#### 2.1.2 Fahnenaerodynamik

Die Windfahne ist ein aerodynamisches Profil, das auf Windwinkeländerungen reagiert:

**Vertikalachsen-Fahne (V-Fahne):**
- Drehachse vertikal
- Fahne dreht sich in Windrichtung wie eine Wetterfahne
- Drehmoment = F_wind × Abstand_Druckpunkt_zu_Achse
- Geringe Kraft, aber sofortige Reaktion
- Verwendet bei: Trim-Tab-Systemen (Aries)

**Horizontalachsen-Fahne (H-Fahne):**
- Drehachse horizontal, quer zur Schiffslängsachse
- Fahne kippt bei Windwinkeländerung seitlich
- Nutzt den Windstaudruck: F = 0,5 × ρ × V² × A × Cd
- Deutlich höhere Kraft als V-Fahne
- Verwendet bei: Servo-Pendulum-Systemen (Windpilot, Monitor)

**Vergleich der Fahnentypen:**

| Eigenschaft | V-Fahne (vertikal) | H-Fahne (horizontal) |
|---|---|---|
| Drehmoment | Gering (Aerodynamik) | Hoch (Staudruck) |
| Ansprechverhalten | Sehr schnell | Schnell |
| Leichtwind-Performance | Mäßig | Gut |
| Starkwind-Verhalten | Muss begrenzt werden | Selbstbegrenzend (kippt flach) |
| Mechanische Komplexität | Einfach | Mittel (Kegelrad nötig) |
| Typische Fahnengröße | 0,08–0,15 m² | 0,10–0,25 m² |

**Horizontalachsen-Fahne — Detailbetrachtung:**

Die H-Fahne ist das dominante Prinzip bei modernen Windfahnensteuerungen. Ihre Funktionsweise:

1. **Neutralstellung:** Fahne steht senkrecht, Vorderkante in den Wind. Kein Drehmoment.
2. **Kursabweichung:** Wind trifft schräg auf die Fahne → eine Seite erhält mehr Druck → Fahne kippt seitlich
3. **Kraftübertragung:** Die Kippbewegung wird über ein Kegelradgetriebe in eine Drehbewegung um eine vertikale Achse umgewandelt
4. **Rückstellung:** Wenn das Boot auf Kurs zurückkehrt, richtet der Wind die Fahne wieder auf

Dimensionierung der H-Fahne:

```
Drehmoment M = F_wind × L_hebel

F_wind = 0,5 × ρ_luft × V² × A_fahne × Cd × sin(α)

Wobei:
ρ_luft  = 1,225 kg/m³ (Meereshöhe, 15°C)
V       = Scheinbare Windgeschwindigkeit (m/s)
A_fahne = Fahnenfläche (m²)
Cd      = Widerstandsbeiwert (≈ 1,2 für flache Platte)
α       = Anstellwinkel der Fahne (= Kursabweichung)
L_hebel = Hebelarm zum Drehpunkt (m)
```

Beispielrechnung für eine typische H-Fahne (A = 0,15 m², V = 7 m/s = 14 kn, α = 5°):

```
F_wind = 0,5 × 1,225 × 7² × 0,15 × 1,2 × sin(5°)
F_wind = 0,5 × 1,225 × 49 × 0,15 × 1,2 × 0,087
F_wind ≈ 0,47 N

Bei L_hebel = 0,3 m:
M = 0,47 × 0,3 = 0,14 Nm
```

Dieses geringe Drehmoment erklärt, warum eine Windfahne niemals direkt ein Ruder betätigen kann — es bedarf einer mechanischen Verstärkung (Servo-Prinzip).

#### 2.1.3 Sensitivität und Ansprechverhalten

Die Sensitivität einer Windfahne wird bestimmt durch:

1. **Fahnengewicht und Trägheitsmoment** — leichtere Fahnen reagieren schneller
2. **Fahnenfläche** — größere Fahnen haben mehr Kraft, aber auch mehr Trägheit
3. **Lagerreibung** — minimale Reibung ist entscheidend für Leichtwind-Performance
4. **Aerodynamisches Profil** — symmetrisches Profil vs. flache Platte

**Ansprechschwelle typischer Systeme:**

| System | Mindest-Windgeschwindigkeit | Mindest-Kursabweichung |
|---|---|---|
| Windpilot Pacific | 5–6 kn scheinbar | 3–4° |
| Monitor | 5–6 kn scheinbar | 3–4° |
| Hydrovane | 6–8 kn scheinbar | 4–5° |
| Aries | 7–8 kn scheinbar | 4–5° |

**Dämpfung und Überschwingen:**

Ein kritischer Designparameter ist die Dämpfung des Regelsystems. Ohne ausreichende Dämpfung oszilliert das Boot um den Sollkurs (Gieren). Die Dämpfung kommt aus mehreren Quellen:

1. **Hydrodynamische Dämpfung des Pendelruders/Hilfsruders** — Hauptdämpfungselement
2. **Mechanische Reibung** — sekundär, sollte minimal sein
3. **Windfahnen-Nachlauf** — aerodynamische Dämpfung
4. **Bootseigene Kursstabilität** — lateraler Widerstand, Kielwirkung

### 2.2 Servo-Pendulum-Prinzip

#### 2.2.1 Grundprinzip

Das Servo-Pendulum-Prinzip (auch: Servo-Auxiliary-Pendulum) ist das am weitesten verbreitete Prinzip bei modernen Windfahnensteuerungen. Es nutzt die Strömungsenergie des Wassers am fahrenden Boot als Kraftquelle.

**Funktionskette:**

```
Wind → Fahne kippt → Kegelrad dreht Pendelruder an → 
→ Wasserströmung drückt Pendelruder seitlich aus →
→ Pendelruder zieht über Leinen am Hauptruder →
→ Boot dreht → Wind auf Fahne ändert sich →
→ Fahne richtet sich auf → Pendelruder kommt zurück →
→ Boot ist auf Kurs
```

**Detaillierte Funktionsbeschreibung:**

1. **Neutralstellung:** Das Pendelruder hängt senkrecht im Wasser, Hinterkante parallel zur Strömung. Keine Seitenkraft, keine Ruderwirkung.

2. **Kursabweichung detektiert:** Wind trifft schräg auf die H-Fahne → Fahne kippt → Kegelradgetriebe dreht die Pendelruderachse → Pendelruder wird angestellt (typisch bis ±20° zur Strömung).

3. **Servokraft entsteht:** Wasser strömt über das angestellte Pendelruder → hydrodynamischer Auftrieb entsteht → Pendelruder wird seitlich aus der Mittellinie gedrückt (pendelt seitwärts).

4. **Kraftübertragung:** Am Pendelruder sind Steuerleinen befestigt, die über Umlenkrollen zum Steuerrad oder zur Pinne geführt werden. Die seitliche Auslenkung des Pendelruders zieht an einer Leine und gibt die andere frei → Ruderlage ändert sich.

5. **Kurskorrektur:** Das Hauptruder dreht das Boot zurück auf Kurs → scheinbarer Wind kommt wieder aus der eingestellten Richtung → Fahne richtet sich auf → Pendelruder wird neutral gestellt → seitliche Kraft verschwindet → Pendelruder pendelt zurück in Mittellage.

**Mathematische Beschreibung der Servokraft:**

Die Seitenkraft des Pendelruders:

```
F_servo = 0,5 × ρ_wasser × V_boot² × A_pendel × Cl(α)

Wobei:
ρ_wasser = 1.025 kg/m³ (Salzwasser)
V_boot   = Bootsgeschwindigkeit (m/s)
A_pendel = Fläche des Pendelruders (m²)
Cl(α)    = Auftriebsbeiwert bei Anstellwinkel α
```

Für ein typisches Pendelruder (A = 0,04 m², Cl = 0,8 bei α = 15°, V = 3 m/s ≈ 6 kn):

```
F_servo = 0,5 × 1.025 × 9 × 0,04 × 0,8
F_servo ≈ 148 N ≈ 15 kg
```

Vergleich: Die Windfahne erzeugt ca. 0,5 N, das Pendelruder 148 N — eine Verstärkung um den Faktor 300. Dies erklärt die Bezeichnung "Servo"-Pendulum.

#### 2.2.2 Pendelruder-Hydrodynamik

Das Pendelruder ist das zentrale Servoelement. Seine Hydrodynamik bestimmt die Leistungsfähigkeit der gesamten Anlage.

**Profilform:**

- Typisch NACA 0012 oder ähnliches symmetrisches Profil
- Dicke/Tiefe-Verhältnis: 10–15%
- Streckung (Aspect Ratio): 3–5
- Material: Edelstahl-Schaft mit GFK- oder Aluminium-Blatt

**Seitliche Auslenkung:**

Das Pendelruder ist an einer Achse aufgehängt, die es ihm ermöglicht, seitlich auszuschwingen (zu pendeln). Der maximale Pendelwinkel beträgt typisch ±60–70° zur Mittellinie.

Die Pendelkraft als Funktion des Pendelwinkels:

```
F_leine = F_servo × cos(β) × (R_pendel / R_rolle)

Wobei:
β         = Pendelwinkel (0° = senkrecht)
R_pendel  = Radius des Pendelarms (Abstand Achse → Leinenbefestigung)
R_rolle   = Radius der Steuertrommel am Rad/Pinne
```

**Strömungsabriss-Problem:**

Bei zu großem Anstellwinkel (>18–22°) reißt die Strömung am Pendelruder ab → dramatischer Kraftverlust. Dies kann passieren, wenn:
- Die Windfahne zu empfindlich eingestellt ist (überkorrigiert)
- Böen die Fahne schlagartig kippen
- Das Kegelradgetriebe zu direkt übersetzt

Gegenmaßnahmen:
- Begrenzung des Anstellwinkels durch mechanische Anschläge
- Progressive Übersetzung im Kegelradgetriebe
- Hydrodynamische Selbstbegrenzung (Pendelruder weicht seitlich aus, reduziert effektiven Anstellwinkel)

#### 2.2.3 Leinenführung und Steueranbindung

Die Verbindung zwischen Pendelruder und Hauptruder erfolgt über Steuerleinen:

**Radsteuerung:**
- Zwei Leinen vom Pendelruder über Umlenkrollen zum Steuerrad
- Befestigung an der Steuertrommel oder an speziellen Adapterscheiben
- Leinenlänge: typisch 8–15 m (Hin- und Rückweg)
- Leinendurchmesser: 8–10 mm Dyneema oder hochfestes Polyester
- Umlenkrollen: mindestens 4 (Heck → Cockpitsüll → Steuerrad)
- Spannung: 5–10 kg Vorspannung für spielfreie Übertragung

**Pinnensteuerung:**
- Direkte Verbindung über Leinen zur Pinne
- Einfacher und effizienter als Radsteuerung
- Weniger Umlenkpunkte = weniger Reibung
- Tillerpilot-Adapter für gemischten Betrieb (Windfahne + Autopilot)

**Leinentypen und Eigenschaften:**

| Material | Dehnung | UV-Beständigkeit | Lebensdauer | Preis/m |
|---|---|---|---|---|
| Dyneema SK78 (8mm) | <1% | Sehr gut | 5–8 Jahre | 4–8 € |
| Polyester geflochten (10mm) | 3–5% | Gut | 3–5 Jahre | 1–3 € |
| Vectran (8mm) | <1% | Mäßig (UV-empfindlich) | 3–5 Jahre | 5–10 € |
| Spectra (8mm) | <1% | Gut | 5–8 Jahre | 4–8 € |

Empfehlung: Dyneema SK78 oder SK99 in 8 mm Durchmesser — minimale Dehnung, hohe UV-Beständigkeit, lange Lebensdauer.

### 2.3 Auxiliary-Rudder-Prinzip

#### 2.3.1 Grundprinzip

Beim Auxiliary-Rudder-Prinzip (Hilfsruder-Prinzip) wird ein zusätzliches, unabhängiges Ruder am Heck des Bootes montiert. Die Windfahne steuert dieses Hilfsruder direkt — das Hauptruder bleibt in fester Position (Mittschiffs oder leicht angestellt).

**Funktionskette:**

```
Wind → Fahne kippt/dreht → Mechanische Übertragung →
→ Hilfsruder wird angestellt → Ruder erzeugt Querkraft →
→ Boot dreht → Wind auf Fahne ändert sich →
→ Fahne neutralisiert → Hilfsruder geht in Nullstellung →
→ Boot ist auf Kurs
```

**Vorteile gegenüber Servo-Pendulum:**

1. **Unabhängig vom Hauptruder** — funktioniert auch bei Hauptruder-Ausfall → Notruder-Funktion
2. **Keine Steuerleinen** — keine Leinenführung durch Cockpit nötig
3. **Einfache Montage** — nur ein Befestigungspunkt am Heck (Halterung)
4. **Kein Verschleiß an Steuerleinen und Umlenkrollen**

**Nachteile gegenüber Servo-Pendulum:**

1. **Geringere Ruderkraft** — die Windfahne muss genug Kraft erzeugen, um das Hilfsruder direkt zu bewegen (kein Servo-Verstärkung durch Wasserströmung)
2. **Limitierte Bootsgröße** — bei großen, schweren Booten reicht die Ruderkraft des kleinen Hilfsruders nicht aus
3. **Höherer Strömungswiderstand** — permanentes Zusatzruder im Wasser
4. **Weniger präzise** — da das Hauptruder feststeht, fehlt die Feinabstimmung
5. **Windschatten-Problem** — das Hilfsruder kann im Windschatten des Hauptruders stehen

#### 2.3.2 Dimensionierung des Hilfsruders

Das Hilfsruder muss groß genug sein, um das Boot allein zu steuern, aber klein genug, um von der Windfahne bewegt werden zu können:

**Typische Hilfsruder-Dimensionen:**

| Bootsgröße (LüA) | Ruderfläche | Rudertiefe | Ruderbreite | Max. Bootsgew. |
|---|---|---|---|---|
| 26–30 ft (8–9 m) | 0,08–0,12 m² | 0,60–0,80 m | 0,15–0,18 m | 6–8 t |
| 30–36 ft (9–11 m) | 0,10–0,15 m² | 0,70–0,90 m | 0,16–0,20 m | 8–12 t |
| 36–42 ft (11–13 m) | 0,12–0,18 m² | 0,80–1,00 m | 0,18–0,22 m | 10–16 t |
| 42–50 ft (13–15 m) | 0,15–0,22 m² | 0,90–1,10 m | 0,20–0,25 m | 14–22 t |

**Ruderbalance:**

Das Hilfsruder hat typisch eine Balance von 15–20% — d.h. 15–20% der Ruderfläche liegen vor der Drehachse. Dies reduziert das nötige Drehmoment erheblich:

```
M_ruder = F_hydro × (Druckpunkt - Drehachse)

Bei 0% Balance: Druckpunkt bei ca. 25% der Rudertiefe → großes Moment
Bei 18% Balance: Druckpunkt nahe an Drehachse → kleines Moment
```

#### 2.3.3 Trim-Tab-Variante

Eine Unterform des Auxiliary-Rudder-Prinzips verwendet einen Trim-Tab (Trimmklappe) am Hilfsruder:

**Funktionskette:**

```
Wind → Fahne → Trim-Tab wird angestellt →
→ Trim-Tab erzeugt Kraft am Hilfsruder →
→ Hilfsruder dreht sich (frei drehbar gelagert) →
→ Hilfsruder erzeugt Querkraft → Boot dreht →
→ Fahne neutralisiert → Trim-Tab neutral → Hilfsruder neutral
```

Dies ist ein doppeltes Servo-Prinzip:
1. Wind bewegt Fahne (Servo 1: Wind → mechanische Bewegung)
2. Trim-Tab bewegt Hilfsruder (Servo 2: Wasserströmung → Ruderkraft)

Der Aries verwendet dieses Prinzip und erzielt damit beachtliche Ruderkräfte auch bei größeren Booten.

### 2.4 Trim-Tab-Prinzip am Hauptruder

#### 2.4.1 Grundprinzip

Die einfachste Form der Windfahnensteuerung: Ein Trim-Tab (Trimmklappe) wird direkt am Hauptruder montiert. Die Windfahne steuert nur den Trim-Tab — der Trim-Tab erzeugt eine Kraft, die das Hauptruder (bei gelöster Steuerung) verdreht.

**Funktionskette:**

```
Wind → Fahne → Trim-Tab am Hauptruder wird angestellt →
→ Wasserströmung auf Trim-Tab erzeugt Kraft →
→ Hauptruder wird seitlich gedrückt (Steuerung muss frei sein!) →
→ Boot dreht → Wind auf Fahne ändert sich →
→ Fahne neutralisiert → Trim-Tab neutral → Hauptruder zentriert
```

**Vorteile:**
- Kein zusätzliches Ruder im Wasser
- Kein schweres Gestell am Heck
- Geringes Gewicht (5–10 kg)
- Niedrige Kosten

**Nachteile:**
- Steuerung muss komplett freigegeben werden (bei Radsteuerung: Reibungsbremse lösen)
- Funktioniert nur mit freigängiger Steueranlage
- Keine Notruder-Funktion
- Begrenzte Ruderkraft — nur für kleinere Boote (bis ca. 35 Fuß)
- Trim-Tab muss am Hauptruder montiert werden (irreversible Modifikation)
- Bei modernen Spatenrudern ohne Skeg schwierig zu montieren

#### 2.4.2 Historische Bedeutung

Das Trim-Tab-Prinzip war das erste industriell gefertigte Windfahnen-Prinzip:
- 1962: Hasler Servo-Pendulum als Weiterentwicklung des Trim-Tab-Prinzips
- 1968: Aries als Trim-Tab-am-Hilfsruder (Hybrid)
- Heute nur noch selten als reiner Trim-Tab am Hauptruder in Verwendung
- Wird noch gelegentlich als Eigenbau-Lösung für Langkielboote eingesetzt

### 2.5 Windwinkel-Problematik

#### 2.5.1 Scheinbarer Wind und Kursstabilität

Die Windfahne steuert nach dem scheinbaren Wind. Dies hat fundamentale Konsequenzen für verschiedene Kurse:

**Amwind (scheinbarer Wind 30–50°):**
- Hoher scheinbarer Wind (Fahrtwind addiert sich)
- Starke Fahne-Kraft → sehr gute Steuerleistung
- Kleine Kursabweichungen erzeugen große Windwinkeländerungen → hohe Sensitivität
- Optimaler Arbeitsbereich für alle Windfahnen-Systeme

**Halbwind (scheinbarer Wind 60–90°):**
- Guter scheinbarer Wind
- Gute Steuerleistung
- Kursabweichungen erzeugen mäßige Windwinkeländerungen
- Sehr guter Arbeitsbereich

**Raumschots (scheinbarer Wind 100–140°):**
- Nachlassender scheinbarer Wind (Fahrtwind reduziert Komponente)
- Mäßige bis gute Steuerleistung
- Empfindlich auf Böen und Wellengang
- Fahne muss größer oder empfindlicher eingestellt werden
- Noch akzeptabler Arbeitsbereich

**Vorwind (scheinbarer Wind 150–180°):**
- Minimaler scheinbarer Wind (V_scheinbar = V_wahr - V_boot)
- Schwache Fahne-Kraft → eingeschränkte Steuerleistung
- Kleine Kursabweichungen erzeugen minimale Windwinkeländerungen → geringe Sensitivität
- Gefahr der Patenthalse bei ungenauer Steuerung
- Problematischer Arbeitsbereich — hier ist ein Autopilot oft besser

**Quantitative Betrachtung:**

Für ein Boot mit 6 kn Geschwindigkeit bei 15 kn wahrem Wind:

| Wahrer Windwinkel | Scheinbarer Windwinkel | Scheinbare Windstärke | Fahnen-Kraft (relativ) |
|---|---|---|---|
| 45° (Amwind) | 32° | 19,8 kn | 100% |
| 90° (Halbwind) | 68° | 16,2 kn | 67% |
| 120° (Raumschots) | 98° | 13,1 kn | 44% |
| 150° (Raumer) | 131° | 10,0 kn | 25% |
| 180° (Vorwind) | 180° | 9,0 kn | 21% |

> ✅ Aufgeloest (Audit): Scheinbare Windstärke bei 90° = 16,2 kn (statt 13,7) und bei 120° = 13,1 kn (statt 11,2); abgeleitete Fahnen-Kraft-Spalte entsprechend auf 67% bzw. 44% korrigiert (Kraft ∝ V_scheinbar²). Quelle: Standardformel scheinbarer Wind (Kosinussatz) V_scheinbar = √(V_wahr² + V_boot² + 2·V_wahr·V_boot·cos(Winkel)) — Wikipedia "Apparent wind", bwsailing.com/oceansail.co.uk Wind-Triangle.

Die Fahnen-Kraft fällt auf Vorwindkurs auf ca. 20% des Amwind-Wertes — dies erklärt die eingeschränkte Vorwind-Performance.

#### 2.5.2 Kompensationsstrategien für Vorwindkurse

1. **Größere Windfahne:** Einige Systeme bieten austauschbare Fahnen in verschiedenen Größen
2. **Empfindlichere Einstellung:** Weniger Dämpfung, schnellere Reaktion (Risiko: Übersteuerung)
3. **Butterfly-Segel:** Genua auf Baum ausgebaumt, Großsegel backbord/steuerbord → Boot segelt stabiler → weniger Kursabweichungen
4. **Leicht abfallen:** Statt 180° wahren Wind 160–170° segeln → mehr scheinbarer Wind, kaum Geschwindigkeitsverlust
5. **Schmetterlings-Kurs:** Abwechselnd Backbord- und Steuerbord-Halsen in 20°-Winkeln → erhöhter scheinbarer Wind, Zick-Zack-Kurs
6. **Autopilot-Unterstützung:** Auf Vorwindkursen den elektrischen Autopiloten verwenden und Windfahne als Backup

### 2.6 Rückstellmomente und Servokräfte

#### 2.6.1 Kräftebilanz im Servo-Pendulum-System

Das Servo-Pendulum-System lässt sich als Regelkreis beschreiben:

```
Störgröße: Windwinkeländerung (= Kursabweichung)
Sensor: Windfahne
Regler: Mechanische Übertragung (Kegelrad, Gestänge)
Stellgröße: Pendelruder-Anstellwinkel
Strecke: Pendelruder → Steuerleinen → Hauptruder → Boot
Rückführung: Kursänderung → Windwinkeländerung → Fahne
```

**Kräfte im System:**

1. **Fahnen-Drehmoment (M_fahne):**
```
M_fahne = 0,5 × ρ_luft × V_wind² × A_fahne × Cd × sin(α) × L_fahne
Typisch: 0,05–0,5 Nm (bei 10–25 kn scheinbar, 3–10° Abweichung)
```

2. **Kegelrad-Übersetzung:**
```
M_pendelachse = M_fahne × (Z_antrieb / Z_abtrieb) × η_kegelrad
Typisch: Übersetzung 1:1 bis 2:1, η ≈ 0,90–0,95
M_pendelachse ≈ 0,05–1,0 Nm
```

3. **Pendelruder-Servokraft:**
```
F_servo = 0,5 × ρ_wasser × V_boot² × A_pendel × Cl(α_pendel)
Typisch: 50–500 N (bei 4–8 kn Fahrt, 5–20° Anstellwinkel)
```

4. **Leinenkraft am Steuerrad:**
```
F_leine = F_servo × cos(β) × (R_pendelarm / R_steuertrommel) × η_leinen
Typisch: 20–200 N (ausreichend für Ruderverstellung)
```

5. **Rückstellmoment am Hauptruder:**
```
M_ruder = F_leine × R_steuertrommel
Typisch: 5–50 Nm (ausreichend für Boote bis 20 t)
```

#### 2.6.2 Systemdämpfung

Zu wenig Dämpfung → Boot giert (oszilliert um Sollkurs)
Zu viel Dämpfung → Boot reagiert träge, kann Kurs nicht halten

Dämpfungsquellen:
1. Hydrodynamische Dämpfung des Pendelruders beim Seitausschwingen
2. Reibung in Lagern, Kegelrad, Umlenkrollen
3. Eigenstabilität des Bootes (Kursstabilität durch Kiel/Ruder-Anordnung)
4. Aerodynamische Dämpfung der Segelanlage

**Kursstabile vs. kurslabile Boote:**

| Eigenschaft | Kursstabil (Longkeel) | Kurslabil (Fin Keel, Spade) |
|---|---|---|
| Gierdämpfung | Hoch (Boot will geradeaus) | Gering (Boot will drehen) |
| Windfahnen-Performance | Exzellent | Gut bis mäßig |
| Erforderliche Servo-Kraft | Gering | Hoch |
| Ansprechverhalten | Etwas träge | Schnell |
| Vorwind-Stabilität | Gut | Problematisch |
| Typische Boote | HR-Rasmus, Westsail 32, Valiant | Beneteau, Bavaria, J-Boats |
| Korrekturaufwand | Gering (1–2 kl. Ruderschläge) | Hoch (ständige Korrekturen) |

### 2.7 Regelungstechnische Betrachtung

#### 2.7.1 Windfahne als P-Regler

Die Windfahnensteuerung ist im Wesentlichen ein Proportionalregler (P-Regler):

```
Ruderausschlag = K_p × Kursabweichung

Wobei K_p (Proportionalverstärkung) bestimmt wird durch:
- Fahnengröße und -empfindlichkeit
- Kegelrad-Übersetzung
- Pendelruder-Größe
- Bootsgeschwindigkeit (beeinflusst Servokraft)
```

**Regelabweichung (stationärer Fehler):**

Ein reiner P-Regler hat immer eine bleibende Regelabweichung. Bei der Windfahne bedeutet dies:
- Bei konstantem Ruderwiderstand (z.B. Lee-Ruderdruck durch Segeltrimmfehler) steuert die Windfahne einen konstanten Kursversatz ein
- Dieser Versatz ist nötig, damit die Fahne genug Drehmoment erzeugt, um das Pendelruder dauerhaft angestellt zu halten
- Abhilfe: Lee-Ruderdruck durch Segeltrimm minimieren (Traveller, Großschot, Vorsegel-Trimm)

#### 2.7.2 Optimierung des Regelverhaltens

**Segeltrimm als Vorsteuerung:**

Der wichtigste Einflussfaktor auf die Steuergüte einer Windfahne ist der Segeltrimm:

1. **Neutraler Ruderstand:** Boot sollte ohne Ruderausschlag annähernd geradeaus segeln
2. **Minimaler Lee-Helm:** Leichte Luv-Gierigkeit ist ideal (Boot fällt ab, wenn Fahne kurz nicht steuert → sicherer als Anluven)
3. **Segel-Balancierung:** Lateralschwerpunkt der Segel über lateralem Widerstandsschwerpunkt des Unterwasserschiffs
4. **Reffstrategie:** Rechtzeitig reffen, bevor Lee-Helm zu stark wird → Windfahne muss weniger korrigieren

**Erfahrungsregeln für optimale Windfahnen-Performance:**

- Segeltrimm so einstellen, dass das Boot 3–5° Luv-Gierigkeit hat
- Großschot etwas fieren, bis Lee-Helm nachlässt
- Traveller nach Lee fahren bei zunehmendem Wind
- Bei Raumschotskurs: Spi-Baum etwas dichter als optimal → stabilerer Kurs
- Vorsegel nicht zu dicht → sonst Lee-Helm → Windfahne muss permanent gegensteuern

---

## 3. Typenübersicht

### 3.1 Servo-Pendulum-Systeme

#### 3.1.1 Windpilot Pacific

**Hersteller:** Windpilot (Peter Matthiesen, Hamburg, Deutschland)
**Prinzip:** Servo-Pendulum mit Horizontalachsen-Fahne
**Seit:** 1975 (kontinuierliche Weiterentwicklung)

**Konstruktionsmerkmale:**

- Horizontalachsen-Windfahne (H-Fahne) aus Aluminium oder GFK
- Kegelradgetriebe zur Umsetzung der Kippbewegung in Drehung
- Pendelruder aus Edelstahl (V4A/316L) mit GFK-Ruderblatt
- Gesamtkonstruktion aus seewasserfestem Aluminium (AlMg4,5Mn)
- Kompakte Bauweise, niedrige Bauhöhe
- Einteiliges Gestell für hohe Steifigkeit
- Pendelruder hochklappbar für Hafenmanöver und Rückwärtsfahrt
- Montage am Heckspiegel oder auf der Badeplattform

**Spezifische Stärken:**
- Exzellente Fertigungsqualität ("Made in Germany")
- Umfangreiche Modellpalette für verschiedene Bootstypen
- Persönliche Beratung durch Peter Matthiesen
- Sehr gute Ersatzteilverfügbarkeit weltweit
- Umfangreiche Fachliteratur des Herstellers
- Gute Vorwind-Performance durch optimierte Fahnengeometrie

**Spezifische Schwächen:**
- Montage erfordert stabile Heckstruktur
- Bei sehr breiten modernen Hecks (>2,5 m) kann die Leinenführung lang werden
- Pendelruder kann in Häfen mit Dalben/Pfählen gefährdet sein
- Etwas teurer als Wettbewerb

#### 3.1.2 Monitor Wind Vane

**Hersteller:** Scanmar International (Lars Bergström, Richmond, CA, USA)
**Prinzip:** Servo-Pendulum mit Horizontalachsen-Fahne
**Seit:** 1977

**Konstruktionsmerkmale:**

- Horizontalachsen-Windfahne aus Aluminium
- Edelstahl-Rahmen (316L) — Hauptstruktur komplett aus Edelstahl
- Pendelruder aus Edelstahl mit Kunststoff-Ruderblatt
- Modulare Bauweise: Einzelteile austauschbar
- Pendelruder über Schnellverschluss hochklappbar
- Markante rote Fahne als Erkennungszeichen
- Montage über zwei Edelstahl-Rohre am Heckspiegel

**Spezifische Stärken:**
- Robuste Edelstahl-Konstruktion — extrem langlebig
- Modularer Aufbau — einzelne Teile separat austauschbar
- Sehr gutes Ersatzteil-Netzwerk weltweit (besonders Nordamerika, Pazifik)
- Große Nutzergemeinde (geschätzt 30.000+ Installationen)
- Praxisbewährt auf zehntausenden Meilen Langfahrt
- Vernünftiges Preis-Leistungs-Verhältnis

**Spezifische Schwächen:**
- Edelstahl-Konstruktion schwerer als Aluminium
- Montage der beiden Edelstahl-Rohre erfordert präzise Ausrichtung
- Ersatzteile für ältere Modelle teilweise nur noch gebraucht verfügbar
- Kegelradgetriebe bei alten Modellen verschleißanfällig

#### 3.1.3 Vergleich Servo-Pendulum-Systeme

| Kriterium | Windpilot Pacific | Monitor |
|---|---|---|
| Grundmaterial Rahmen | AlMg4,5Mn (Alu) | Edelstahl 316L |
| Gewicht (komplett) | 16–22 kg | 20–27 kg |
| Pendelruder-Fläche | 0,032–0,045 m² | 0,035–0,048 m² |
| Max. Bootsgröße | 18 t / 50 ft | 20 t / 55 ft |
| Montageart | Heckspiegel, Plattform | Zwei Seitenrohre |
| Preis (2025) | 3.800–5.500 € | 3.200–4.500 USD |
| Herstellung | Hamburg, Deutschland | Richmond, CA, USA |
| Ersatzteilversand weltweit | Ja (Expressversand) | Ja (Expressversand) |
| Steuerleinenlänge typisch | 10–14 m | 10–14 m |
| Windfahnenfläche | 0,12–0,18 m² | 0,13–0,17 m² |

### 3.2 Auxiliary-Rudder-Systeme

#### 3.2.1 Hydrovane

**Hersteller:** Hydrovane Marine Ltd. (England, später Kanada)
**Prinzip:** Auxiliary Rudder mit Vertikalachsen-Fahne
**Seit:** 1968 (Derek Fawcett Design)

**Konstruktionsmerkmale:**

- Vertikalachsen-Windfahne (V-Fahne) — dreht sich wie eine Wetterfahne
- Eigenständiges Hilfsruder mit integrierter Mechanik
- Kompakte, selbsttragende Einheit — keine Verbindung zum Hauptruder nötig
- Ruder und Fahne in einem Gehäuse
- Montage seitlich am Heck (Backbord oder Steuerbord)
- Ruder ist gleichzeitig Notruder bei Hauptruder-Ausfall
- Material: Aluminium-Druckguss und Edelstahl

**Spezifische Stärken:**
- Notruder-Funktion — einzigartiges Sicherheitsmerkmal
- Keinerlei Steuerleinen nötig — komplett eigenständig
- Einfache Montage (ein Befestigungspunkt)
- Funktioniert auch bei blockiertem/defektem Hauptruder
- Sehr wartungsarm (wenige bewegliche Teile)
- Ideal für schwere Langkielboote (Ruderkraft ausreichend)

**Spezifische Schwächen:**
- Permanentes Zusatzruder im Wasser (Strömungswiderstand ca. 1–3% Speed-Verlust)
- Geringere Steuerpräzision als Servo-Pendulum (±5–8° vs ±3–5°)
- Nicht für sehr große Boote geeignet (>16 t problematisch)
- Seitliche Montage: asymmetrischer Widerstand
- Hilfsruder im Windschatten des Hauptruders bei einigen Bootskonfigurationen
- V-Fahne weniger kraftvoll als H-Fahne

#### 3.2.2 Cape Horn Windvane

**Hersteller:** Cape Horn Marine (Yves Gélinas, Kanada)
**Prinzip:** Auxiliary Rudder mit Trim-Tab und Horizontalachsen-Fahne
**Seit:** ca. 1980

**Konstruktionsmerkmale:**

- Horizontalachsen-Windfahne (H-Fahne)
- Hilfsruder mit Trim-Tab (Servo-Hilfsruder-Prinzip)
- Aluminium-Konstruktion (6061-T6)
- Montage am Heckspiegel
- Frei drehendes Hilfsruder, das durch Trim-Tab gesteuert wird
- Hochklappbar für Hafenmanöver

**Spezifische Stärken:**
- Doppeltes Servo-Prinzip (Wind → Trim-Tab → Hilfsruder) → hohe Ruderkraft
- Notruder-Funktion
- Keine Steuerleinen nötig
- Gute Performance auch für mittelschwere Boote
- Robuste Aluminium-Konstruktion
- Moderate Kosten

**Spezifische Schwächen:**
- Komplexere Mechanik als reine Auxiliary-Systeme
- Permanentes Zusatzruder im Wasser
- Kleiner Hersteller — eingeschränkte Servicenetzwerke
- Ersatzteile nur direkt vom Hersteller

### 3.3 Trim-Tab-Systeme

#### 3.3.1 Aries

**Hersteller:** Aries Marine (Nick Franklin, England) — historisch
**Prinzip:** Servo-Pendulum mit Vertikalachsen-Fahne und Trim-Tab
**Seit:** 1968 (heute nur noch gebraucht erhältlich)

**Konstruktionsmerkmale:**

- Vertikalachsen-Windfahne (V-Fahne) — Wetterfahnen-Prinzip
- Servo-Pendulum-Ruder mit Trim-Tab am Pendelruder
- Edelstahl-Rahmen
- Klassisches Design aus der Ära der Golden Globe Race
- Leinen-Übertragung zum Hauptruder

**Historische Bedeutung:**
- Eines der ersten industriell gefertigten Windfahnen-Systeme
- Bernard Moitessier segelte mit einer Aries um die Welt (1968/69)
- Tausende von Langfahrt-Seglern nutzten die Aries in den 1970er–1990er Jahren
- Heute Sammlerstück und Kultgegenstand unter Langfahrt-Seglern

**Status:** Nicht mehr in Produktion. Gebrauchte Anlagen auf dem Markt für 1.500–3.000 €. Ersatzteile teilweise über Spezialisten erhältlich.

### 3.4 Hybrid-Systeme

#### 3.4.1 Sailomat

**Hersteller:** Sailomat (Israel)
**Prinzip:** Auxiliary Rudder mit Trim-Tab, Vertikalachsen-Fahne
**Seit:** ca. 1980

**Konstruktionsmerkmale:**

- Vertikalachsen-Windfahne
- Auxiliary Rudder mit Trim-Tab-Steuerung
- Aluminium-Konstruktion
- Integriertes Design — Fahne, Mechanik und Ruder als Einheit
- Verschiedene Modelle für verschiedene Bootsgrößen

**Marktposition:** Nischenhersteller mit treuer Fangemeinde, besonders im Mittelmeerraum. Gute Alternative für Boote, bei denen Servo-Pendulum-Systeme nicht montierbar sind.

#### 3.4.2 Windfahne + Autopilot (Hybrid-Steuerung)

Moderne Langfahrt-Yachten nutzen zunehmend eine Kombination:

**Konfiguration:**
1. Windfahne als Primärsystem (Am Wind bis Raumschots)
2. Elektrischer Autopilot als Sekundärsystem (Vorwind, Motorfahrt)
3. Manuelle Steuerung als Tertiärsystem (Hafen, Anker)

**Integration:**
- Windfahnen-Steuerleinen und Autopilot-Antrieb teilen sich das Steuerrad
- Bei Radsteuerung: Autopilot-Antriebseinheit an der Steuersäule, Windfahnen-Leinen an der Steuertrommel
- Umschaltung: Windfahnen-Leinen lösen/klemmen, Autopilot ein/aus
- Kein gleichzeitiger Betrieb möglich (Systeme arbeiten gegeneinander)

**Empfohlene Autopiloten für Hybrid-Betrieb:**

| Autopilot | Typ | Eignung | Preis (2025) |
|---|---|---|---|
| Raymarine EV-100 Wheel | Radantrieb | Sehr gut | 1.800–2.200 € |
| B&G NAC-2/NAC-3 | Hydraulisch/Linear | Gut | 1.500–3.000 € |
| Simrad TP32/TP22 | Pinnenantrieb | Sehr gut (Pinnenbote) | 1.200–1.800 € |
| Raymarine EV-100 Tiller | Pinnenantrieb | Sehr gut (Pinnenbote) | 1.500–1.800 € |
| Garmin Reactor 40 | Hydraulisch | Gut | 2.500–4.000 € |

---

## 4. Produktlinien und Spezifikationen

### 4.1 Windpilot

#### 4.1.1 Windpilot Pacific

**Typ:** Servo-Pendulum
**Zielgruppe:** Langfahrt-Yachten 28–50 Fuß (8,5–15 m), bis 18 Tonnen Verdrängung
**Preis (2025):** ca. 4.200–4.800 € (ohne Montageadapter)

**Technische Daten:**

| Parameter | Wert |
|---|---|
| Prinzip | Servo-Pendulum, H-Fahne |
| Material Rahmen | AlMg4,5Mn (seewasserfest) |
| Material Pendelruder | Edelstahl 316L Schaft, GFK Blatt |
| Material Windfahne | Aluminium, eloxiert |
| Gewicht komplett | ca. 18 kg |
| Pendelruder-Fläche | 0,038 m² |
| Pendelruder-Tiefe | 620 mm |
| Windfahnenfläche | 0,15 m² |
| Max. Bootsverdrängung | 18 t |
| Max. LüA empfohlen | 50 ft (15 m) |
| Min. Windstärke (scheinbar) | 5–6 kn |
| Kurs-Genauigkeit | ±3–5° (Am Wind), ±5–8° (Halbwind), ±8–12° (Raumschots) |
| Montagebreite | 300–450 mm |
| Bauhöhe über Deck | ca. 1.200 mm |

**Lieferumfang:**
- Windpilot Pacific Grundeinheit (Rahmen, Fahne, Pendelruder, Kegelradgetriebe)
- 2 × 15 m Steuerleine Dyneema 8 mm
- 4 × Umlenkrollen Harken oder Lewmar (je nach Modell)
- Montageanleitung (deutsch/englisch)
- Bootsspezifischer Montageadapter (separat, ca. 300–600 €)
- Ersatz-Splinte und Sicherungsmaterial

#### 4.1.2 Windpilot Pacific Light

**Typ:** Servo-Pendulum (Leichtversion)
**Zielgruppe:** Kleinere Langfahrt-Yachten 24–38 Fuß (7,3–11,6 m), bis 10 Tonnen
**Preis (2025):** ca. 3.400–3.900 € (ohne Montageadapter)

**Technische Daten:**

| Parameter | Wert |
|---|---|
| Prinzip | Servo-Pendulum, H-Fahne |
| Material Rahmen | AlMg4,5Mn (seewasserfest) |
| Gewicht komplett | ca. 14 kg |
| Pendelruder-Fläche | 0,030 m² |
| Pendelruder-Tiefe | 540 mm |
| Windfahnenfläche | 0,12 m² |
| Max. Bootsverdrängung | 10 t |
| Max. LüA empfohlen | 38 ft (11,6 m) |
| Min. Windstärke (scheinbar) | 5–6 kn |

**Unterschied zum Pacific:**
- Geringeres Gewicht (14 vs. 18 kg) → besser für leichte Boote
- Kleineres Pendelruder → weniger Servokraft → nur für leichtere Boote
- Gleiche Fertigungsqualität
- Gleiche Ersatzteilkompatibilität im Rahmenbereich
- Kleinere Windfahne → etwas weniger Leichtwind-Performance

#### 4.1.3 Windpilot Pacific Plus

**Typ:** Servo-Pendulum (Premiumversion)
**Zielgruppe:** Schwere Langfahrt-Yachten 35–55 Fuß (10,7–16,8 m), bis 25 Tonnen
**Preis (2025):** ca. 5.200–5.800 € (ohne Montageadapter)

**Technische Daten:**

| Parameter | Wert |
|---|---|
| Prinzip | Servo-Pendulum, H-Fahne |
| Material Rahmen | AlMg4,5Mn (seewasserfest), verstärkt |
| Gewicht komplett | ca. 24 kg |
| Pendelruder-Fläche | 0,048 m² |
| Pendelruder-Tiefe | 720 mm |
| Windfahnenfläche | 0,20 m² |
| Max. Bootsverdrängung | 25 t |
| Max. LüA empfohlen | 55 ft (16,8 m) |
| Min. Windstärke (scheinbar) | 5–6 kn |

**Unterschied zum Pacific:**
- Größeres Pendelruder → mehr Servokraft → für schwerere Boote
- Verstärkter Rahmen → höhere strukturelle Festigkeit
- Größere Windfahne → bessere Leichtwind-Performance
- Verstärktes Kegelradgetriebe → höhere Drehmomentkapazität
- Dickere Pendelruder-Achse → höhere Biegesteifigkeit

### 4.2 Monitor

#### 4.2.1 Monitor M

**Typ:** Servo-Pendulum
**Zielgruppe:** Standard-Langfahrt-Yachten 27–45 Fuß (8,2–13,7 m), bis 15 Tonnen
**Preis (2025):** ca. 3.400–3.800 USD (ohne Montageadapter)

**Technische Daten:**

| Parameter | Wert |
|---|---|
| Prinzip | Servo-Pendulum, H-Fahne |
| Material Rahmen | Edelstahl 316L |
| Material Pendelruder | Edelstahl 316L Schaft, HDPE Blatt |
| Gewicht komplett | ca. 22 kg |
| Pendelruder-Fläche | 0,040 m² |
| Windfahnenfläche | 0,14 m² |
| Max. Bootsverdrängung | 15 t |
| Max. LüA empfohlen | 45 ft (13,7 m) |
| Montage | Zwei seitliche Edelstahlrohre |

**Lieferumfang:**
- Monitor M Grundeinheit
- 2 × Montagerohre Edelstahl 316L (bootsspezifisch)
- 2 × 15 m Steuerleine
- Umlenkrollen
- Montageanleitung
- Ersatzteil-Kit (Splinte, Scheiben, O-Ringe)

#### 4.2.2 Monitor MX

**Typ:** Servo-Pendulum (Heavy Duty)
**Zielgruppe:** Schwere Langfahrt-Yachten 38–55 Fuß (11,6–16,8 m), bis 22 Tonnen
**Preis (2025):** ca. 4.200–4.800 USD (ohne Montageadapter)

**Technische Daten:**

| Parameter | Wert |
|---|---|
| Prinzip | Servo-Pendulum, H-Fahne |
| Material Rahmen | Edelstahl 316L, verstärkt |
| Gewicht komplett | ca. 27 kg |
| Pendelruder-Fläche | 0,048 m² |
| Windfahnenfläche | 0,18 m² |
| Max. Bootsverdrängung | 22 t |
| Max. LüA empfohlen | 55 ft (16,8 m) |

**Unterschied zum Monitor M:**
- Verstärkter Rahmen und dickere Rohre
- Größeres Pendelruder → mehr Servokraft
- Größere Windfahne
- Stärkere Lager → höhere Lebensdauer bei schweren Booten
- Breitere Montagerohre für höhere Stabilität

### 4.3 Hydrovane

#### 4.3.1 Hydrovane (Standardmodell)

**Typ:** Auxiliary Rudder
**Zielgruppe:** Langfahrt-Yachten 26–45 Fuß (7,9–13,7 m), bis 16 Tonnen
**Preis (2025):** ca. 4.500–5.500 GBP (ca. 5.200–6.400 €)

**Technische Daten:**

| Parameter | Wert |
|---|---|
| Prinzip | Auxiliary Rudder, V-Fahne |
| Material Gehäuse | Aluminium-Druckguss, eloxiert |
| Material Ruder | Aluminium, Edelstahl-Schaft |
| Gewicht komplett | ca. 25–30 kg |
| Hilfsruder-Fläche | 0,12–0,15 m² |
| Hilfsruder-Tiefe | 800–900 mm |
| Windfahnenfläche | 0,10–0,14 m² |
| Max. Bootsverdrängung | 16 t |
| Max. LüA empfohlen | 45 ft (13,7 m) |
| Montage | Seitlich am Heck (BB oder StB) |

**Lieferumfang:**
- Hydrovane Grundeinheit (Gehäuse, Fahne, Ruder, Mechanik)
- Montagehalterung (bootsspezifisch)
- Montagematerial (Edelstahl-Bolzen, Unterlegscheiben)
- Montageanleitung
- Notruder-Pinne (für direkte Handsteuerung über Hydrovane-Ruder)

**Besonderheit Notruder-Funktion:**
Die Hydrovane kann bei Ausfall des Hauptruders als vollwertiges Notruder dienen:
- Demontage der Windfahnen-Mechanik (5 Minuten)
- Aufsetzen der Notruder-Pinne auf den Ruderschaft
- Direkte Handsteuerung über die Hydrovane-Pinne
- Ausreichend Ruderfläche für Notbetrieb bei moderaten Bedingungen
- Limitierung: bei schwerem Wetter und großen Booten eingeschränkt

### 4.4 Aries (historisch)

**Typ:** Servo-Pendulum mit Trim-Tab (V-Fahne)
**Hersteller:** Aries Marine (Nick Franklin, England) — nicht mehr in Produktion
**Historischer Preis:** ca. 1.800–2.500 GBP (1990er Jahre)
**Gebrauchtpreis (2025):** ca. 1.500–3.500 € (zustandsabhängig)

**Technische Daten (historisch):**

| Parameter | Wert |
|---|---|
| Prinzip | Servo-Pendulum, V-Fahne, Trim-Tab |
| Material Rahmen | Edelstahl |
| Gewicht komplett | ca. 20–25 kg |
| Max. Bootsverdrängung | 15 t |
| Max. LüA empfohlen | 45 ft |
| Produktion | ca. 1968–2005 |

### 4.5 Cape Horn

#### 4.5.1 Cape Horn (Standardmodell)

**Typ:** Auxiliary Rudder mit Trim-Tab
**Zielgruppe:** Langfahrt-Yachten 28–48 Fuß (8,5–14,6 m), bis 18 Tonnen
**Preis (2025):** ca. 3.500–4.500 CAD (ca. 2.400–3.100 €)

**Technische Daten:**

| Parameter | Wert |
|---|---|
| Prinzip | Auxiliary Rudder + Trim-Tab, H-Fahne |
| Material Rahmen | Aluminium 6061-T6 |
| Material Ruder | Aluminium, Edelstahl-Schaft |
| Gewicht komplett | ca. 20–25 kg |
| Hilfsruder-Fläche | 0,10–0,14 m² |
| Windfahnenfläche | 0,12–0,16 m² |
| Max. Bootsverdrängung | 18 t |
| Max. LüA empfohlen | 48 ft (14,6 m) |
| Montage | Heckspiegel |

### 4.6 Sailomat

#### 4.6.1 Sailomat 3040

**Typ:** Auxiliary Rudder mit Trim-Tab
**Zielgruppe:** Langfahrt-Yachten 28–42 Fuß (8,5–12,8 m), bis 14 Tonnen
**Preis (2025):** ca. 3.800–4.500 € (ab Werk Israel)

**Technische Daten:**

| Parameter | Wert |
|---|---|
| Prinzip | Auxiliary Rudder + Trim-Tab, V-Fahne |
| Material | Aluminium, Edelstahl |
| Gewicht komplett | ca. 18–22 kg |
| Hilfsruder-Fläche | 0,09–0,12 m² |
| Max. Bootsverdrängung | 14 t |
| Max. LüA empfohlen | 42 ft (12,8 m) |

### 4.7 Gesamtvergleich aller Systeme

| Kriterium | Windpilot Pacific | Monitor M | Hydrovane | Cape Horn | Sailomat 3040 |
|---|---|---|---|---|---|
| **Prinzip** | Servo-Pendulum | Servo-Pendulum | Auxiliary Rudder | Aux. Rudder + Tab | Aux. Rudder + Tab |
| **Fahnentyp** | H-Fahne | H-Fahne | V-Fahne | H-Fahne | V-Fahne |
| **Max. Verdrängung** | 18 t | 15 t | 16 t | 18 t | 14 t |
| **Gewicht** | 18 kg | 22 kg | 25–30 kg | 20–25 kg | 18–22 kg |
| **Notruder** | Nein | Nein | Ja | Ja | Ja |
| **Steuerleinen** | Ja | Ja | Nein | Nein | Nein |
| **Preis (ca.)** | 4.500 € | 3.600 USD | 5.800 € | 2.800 € | 4.200 € |
| **Am-Wind** | ★★★★★ | ★★★★★ | ★★★★ | ★★★★ | ★★★★ |
| **Halbwind** | ★★★★★ | ★★★★★ | ★★★★ | ★★★★★ | ★★★★ |
| **Raumschots** | ★★★★ | ★★★★ | ★★★ | ★★★★ | ★★★ |
| **Vorwind** | ★★★ | ★★★ | ★★ | ★★★ | ★★ |
| **Leichtwind** | ★★★★ | ★★★★ | ★★★ | ★★★★ | ★★★ |
| **Starkwind** | ★★★★★ | ★★★★★ | ★★★★ | ★★★★ | ★★★★ |
| **Wartungsaufwand** | Gering | Gering | Sehr gering | Gering | Gering |
| **Ersatzteile** | ★★★★★ | ★★★★★ | ★★★★ | ★★★ | ★★★ |

---

## 5. Hersteller-Datenbank

### 5.1 Windpilot (Deutschland)

| Feld | Daten |
|---|---|
| **Firmenname** | Windpilot — Peter Matthiesen |
| **Gründung** | 1975 |
| **Firmensitz** | Hamburg, Deutschland |
| **Inhaber/Geschäftsführer** | Peter Matthiesen |
| **Produktionsstandort** | Hamburg, Deutschland |
| **Website** | www.windpilot.com |
| **Kontakt** | info@windpilot.com |
| **Produktpalette** | Pacific, Pacific Light, Pacific Plus |
| **Spezialität** | Servo-Pendulum-Systeme, umfangreiche Fachliteratur |
| **Preisrange** | 3.400–5.800 € |
| **Vertrieb** | Direkt + ausgewählte Händler weltweit |
| **Ersatzteilversand** | Weltweit, Express möglich |
| **Besonderheit** | Peter Matthiesen gilt als einer der weltweit führenden Experten für Windfahnensteuerung. Autor mehrerer Fachbücher. Persönliche Beratung für jeden Kunden. Über 10.000 Installationen weltweit. |
| **Installationsnetzwerk** | Empfohlene Installateure in den meisten Langfahrt-Häfen |
| **Garantie** | 5 Jahre auf Rahmen, 2 Jahre auf bewegliche Teile |
| **AYDI-Bewertung** | Premium-Hersteller, höchste Fertigungsqualität, exzellenter Service |

### 5.2 Scanmar International / Monitor (USA)

| Feld | Daten |
|---|---|
| **Firmenname** | Scanmar International |
| **Gründung** | 1977 |
| **Firmensitz** | Richmond, Kalifornien, USA |
| **Gründer** | Lars Bergström |
| **Produktionsstandort** | Richmond, CA, USA |
| **Website** | www.selfsteer.com |
| **Produktpalette** | Monitor M, Monitor MX |
| **Spezialität** | Servo-Pendulum, Edelstahl-Konstruktion |
| **Preisrange** | 3.400–4.800 USD |
| **Vertrieb** | Direkt + Händlernetzwerk (Schwerpunkt Nordamerika) |
| **Ersatzteilversand** | Weltweit |
| **Besonderheit** | Geschätzt über 30.000 Installationen. Sehr aktive Nutzergemeinschaft. Marktführer in Nordamerika. Robuste Edelstahl-Konstruktion. |
| **Garantie** | Lebenslange Garantie auf Edelstahl-Rahmen, 2 Jahre auf bewegliche Teile |
| **AYDI-Bewertung** | Industriestandard, hervorragendes Preis-Leistungs-Verhältnis, riesiges Nutzernetzwerk |

### 5.3 Hydrovane Marine (Kanada/England)

| Feld | Daten |
|---|---|
| **Firmenname** | Hydrovane Marine Ltd. |
| **Gründung** | 1968 (Design: Derek Fawcett) |
| **Firmensitz** | Kanada (Produktion und Vertrieb) |
| **Website** | www.hydrovane.com |
| **Produktpalette** | Hydrovane (Einheitsmodell, verschiedene Montageoptionen) |
| **Spezialität** | Auxiliary Rudder mit Notruder-Funktion |
| **Preisrange** | 4.500–5.500 GBP |
| **Vertrieb** | Direkt + ausgewählte Händler |
| **Besonderheit** | Einziges System mit echter Notruder-Funktion. Keine Steuerleinen. Vollständig eigenständiges System. Beliebt bei Blauwasser-Seglern, die maximale Redundanz suchen. |
| **Garantie** | 5 Jahre auf Struktur |
| **AYDI-Bewertung** | Nischenprodukt mit einzigartiger Notruder-Funktion, ideal für sicherheitsbewusste Langfahrtsegler |

### 5.4 Cape Horn Marine (Kanada)

| Feld | Daten |
|---|---|
| **Firmenname** | Cape Horn Marine |
| **Gründer** | Yves Gélinas |
| **Firmensitz** | Kanada |
| **Website** | www.capehornwindvane.com |
| **Produktpalette** | Cape Horn Windvane (Standard, Heavy Duty) |
| **Spezialität** | Auxiliary Rudder mit Trim-Tab, H-Fahne |
| **Preisrange** | 3.500–5.000 CAD |
| **Vertrieb** | Direkt |
| **Besonderheit** | Gutes Preis-Leistungs-Verhältnis. Yves Gélinas ist selbst Langfahrtsegler und hat das System auf eigenen Reisen entwickelt und getestet. Kleine Manufaktur mit persönlichem Service. |
| **Garantie** | 3 Jahre |
| **AYDI-Bewertung** | Solides Produkt, gutes Preis-Leistungs-Verhältnis, eingeschränktes Servicenetzwerk |

### 5.5 Sailomat (Israel)

| Feld | Daten |
|---|---|
| **Firmenname** | Sailomat Ltd. |
| **Firmensitz** | Israel |
| **Website** | www.sailomat.com |
| **Produktpalette** | Sailomat 3040, Sailomat 504 |
| **Spezialität** | Auxiliary Rudder + Trim-Tab, kompaktes Design |
| **Preisrange** | 3.800–5.500 € |
| **Vertrieb** | Direkt + Mittelmeer-Händler |
| **Besonderheit** | Besonders beliebt im Mittelmeerraum. Kompaktes Design. Gute Verarbeitungsqualität. |
| **Garantie** | 2 Jahre |
| **AYDI-Bewertung** | Nischenhersteller, gute Qualität, eingeschränkte globale Verfügbarkeit |

### 5.6 Aries Marine (England — historisch)

| Feld | Daten |
|---|---|
| **Firmenname** | Aries Marine |
| **Gründer** | Nick Franklin |
| **Firmensitz** | England |
| **Status** | Nicht mehr in Produktion (ca. 2005 eingestellt) |
| **Historische Produktpalette** | Aries Windvane |
| **Historischer Preis** | 1.800–2.500 GBP |
| **Gebrauchtmarkt** | 1.500–3.500 € (zustandsabhängig) |
| **Besonderheit** | Legendäres System, das in der Golden Globe Race 1968 berühmt wurde. Tausende von Installationen. Ersatzteile über Spezialisten noch erhältlich. Sammlerwert bei gut erhaltenen Exemplaren. |
| **AYDI-Bewertung** | Historisch bedeutsam, Gebrauchtmarkt relevant, keine Neuproduktion |

### 5.7 Hersteller-Entscheidungsmatrix

**Empfehlung nach Bootstyp und Einsatzzweck:**

| Bootstyp | Primärempfehlung | Alternativ | Begründung |
|---|---|---|---|
| Langkieler 28–35 ft, <10 t | Windpilot Pacific Light | Monitor M | Leichtere Version ausreichend, exzellente Kursstabilität des Bootes |
| Langkieler 35–45 ft, 10–18 t | Windpilot Pacific | Monitor M | Standardversion, optimale Leistung |
| Langkieler 45–55 ft, 18–25 t | Windpilot Pacific Plus | Monitor MX | Verstärkte Version nötig |
| Fin-Kiel 30–40 ft, 6–12 t | Monitor M | Windpilot Pacific | Monitor etwas preiswerter, beide gut geeignet |
| Fin-Kiel 40–50 ft, 12–20 t | Windpilot Pacific Plus | Monitor MX | Verstärkte Version wegen höherer Ruderkräfte bei Fin-Kiel |
| Sicherheitsorientiert, Notruder | Hydrovane | Cape Horn | Einzige Systeme mit Notruder-Funktion |
| Radsteuerung blockierbar | Hydrovane | Cape Horn | Kein Problem, da unabhängig vom Hauptruder |
| Pinnensteuerung | Windpilot Pacific | Monitor M | Servo-Pendulum optimal für direkte Pinnenanbindung |
| Budget-orientiert | Cape Horn | Monitor M | Beste Preise |
| Mittelmeer-Einsatz | Sailomat 3040 | Hydrovane | Lokaler Service, moderate Bedingungen |

---

## 6. Fehlerbild-Atlas

### 6.1 Fehlerbild F01: Pendelruder klemmt in Mittelstellung

**Symptome:**
- Windfahne kippt bei Kursabweichung, aber Pendelruder reagiert nicht
- Boot fährt geradeaus, keine Kurskorrekturen
- Händisch ist das Pendelruder schwer zu bewegen
- Möglicherweise Knirsch- oder Quietschgeräusche

**Ursachen (nach Häufigkeit):**
1. Korrosion/Salzablagerung im Kegelradgetriebe (40%)
2. Verbogene Pendelruder-Achse durch Grundberührung oder Treibgut (25%)
3. Ausgehärtetes Fett in den Lagerbuchsen (20%)
4. Fremdkörper (Leine, Seetang, Plastik) um Achse gewickelt (10%)
5. Festsitzende Sicherungsmutter zu fest angezogen (5%)

**Diagnose:**
1. Pendelruder hochklappen und von Hand bewegen — klemmt es?
2. Kegelradgetriebe freilegen und Zahnräder inspizieren
3. Pendelruder-Achse auf Geradheit prüfen (Lichtspalt-Methode)
4. Lager auf Leichtgängigkeit prüfen (Pendelruder sollte unter Eigengewicht fallen)

**Behebung:**
- Korrosion: Kegelradgetriebe demontieren, reinigen, neu fetten (Teflon-Marinefett)
- Verbogene Achse: Austausch der Achse (Ersatzteil beim Hersteller)
- Ausgehärtetes Fett: Vollständig entfernen, mit frischem Marinefett nachschmieren
- Fremdkörper: Entfernen, Lager auf Beschädigung prüfen
- Mutter: Auf korrektes Anzugsmoment einstellen (Herstellerangaben beachten)

**Präventivmaßnahmen:**
- Halbjährliche Schmierung aller Lagerstellen
- Nach jeder Grundberührung Pendelruder-Achse prüfen
- Pendelruder im Hafen hochklappen
- Kegelradgetriebe jährlich inspizieren und nachfetten

**AYDI-Severity:** HOCH — System funktionsunfähig
**AYDI-Confidence:** measured (wenn physisch inspiziert), visual_medium (wenn Foto der korroden Lager)

### 6.2 Fehlerbild F02: Windfahne zu leicht / überempfindlich

**Symptome:**
- Boot giert stark (schlingert um den Sollkurs)
- Konstante Kurskorrekturen in beide Richtungen
- Pendelruder schwingt hektisch hin und her
- Steuerleinen rucken ständig
- Unruhige Fahrt, Komfort eingeschränkt

**Ursachen (nach Häufigkeit):**
1. Windfahne zu groß für aktuelle Bedingungen (35%)
2. Windfahne zu leicht (Eigengewicht zu gering für Dämpfung) (25%)
3. Übersetzung im Kegelrad zu direkt (15%)
4. Zu wenig Lee-Helm (Boot hat keine eigene Richtungsstabilität) (15%)
5. Pendelruder-Anstellwinkel nicht begrenzt (10%)

**Diagnose:**
1. Kurs-Oszillation beobachten — regelmäßiges Gieren = Übersteuerung
2. Windstärke messen — bei >25 kn scheinbar ist Überempfindlichkeit normal
3. Segeltrimm prüfen — neutraler oder leichter Lee-Helm?
4. Pendelruder beobachten — schlägt es ständig von Anschlag zu Anschlag?

**Behebung:**
- Fahne verkleinern: Kleinere Ersatzfahne montieren oder untere Hälfte abdecken
- Gewichtung: Kleine Gewichte (50–200 g) an der Fahnen-Unterkante → mehr Trägheit
- Übersetzung ändern: Bei verstellbaren Systemen die Übersetzung reduzieren
- Segeltrimm optimieren: Traveller nach Lee, Großsegel leicht fieren → Lee-Helm reduzieren
- Anschlag begrenzen: Pendelruder-Ausschlag mechanisch auf ±50° begrenzen

**Präventivmaßnahmen:**
- Fahnen-Größe an Bedingungen anpassen (manche Hersteller bieten Wechselfahnen)
- Segeltrimm vor dem Einstellen der Windfahne optimieren
- In Starkwind rechtzeitig reffen → reduziert Lee-Helm → bessere Windfahnen-Performance

**AYDI-Severity:** MITTEL — System funktioniert, aber suboptimal
**AYDI-Confidence:** estimated (Segeltrimm-Beurteilung), visual_medium (Gierverhalten auf Video)

### 6.3 Fehlerbild F03: Windfahne zu schwer / unempfindlich

**Symptome:**
- Boot reagiert träge auf Kursabweichungen
- Kurs weicht zunehmend ab, bevor Korrektur einsetzt
- Bei Leichtwind keine Steuerung
- Windfahne bewegt sich kaum

**Ursachen (nach Häufigkeit):**
1. Fahne zu klein für Bedingungen oder Bootsgröße (30%)
2. Lagerreibung zu hoch (Korrosion, fehlendes Fett) (25%)
3. Kegelradgetriebe schwergängig (20%)
4. Windfahne verformt oder beschädigt (aerodynamische Effizienz reduziert) (15%)
5. Fahne falsch montiert (Schwerpunkt nicht korrekt) (10%)

**Diagnose:**
1. Fahne von Hand kippen — leichtgängig? Federt sie zurück?
2. Lager prüfen — Fahne sollte bei 3–4 kn Wind bereits reagieren
3. Kegelrad prüfen — dreht es frei?
4. Fahnenoberfläche prüfen — Verformungen, Risse, fehlende Teile?

**Behebung:**
- Fahne vergrößern: Größere Ersatzfahne montieren
- Lager schmieren: Alle Lagerstellen reinigen und mit Teflon-Marinefett schmieren
- Kegelrad warten: Zahnflanken reinigen, Spiel prüfen, neu fetten
- Fahne ersetzen: Bei Beschädigung neue Fahne vom Hersteller
- Montage korrigieren: Schwerpunkt und Achsposition gemäß Herstellerangaben

**AYDI-Severity:** MITTEL — System funktioniert eingeschränkt
**AYDI-Confidence:** measured (wenn Windstärke bekannt), visual_low (visuell schwer beurteilbar)

### 6.4 Fehlerbild F04: Verbindungsgestänge lose / Spiel im System

**Symptome:**
- Klapper- oder Klappergeräusche bei Wellengang
- Verzögerte Reaktion der Windfahne auf Kursabweichungen
- Pendelruder reagiert mit Totgang (erst ab größerer Fahnen-Auslenkung)
- Steuerung "schwammig" — keine definierte Mittelstellung
- Sichtbares Spiel an Gelenken und Verbindungspunkten

**Ursachen (nach Häufigkeit):**
1. Verschlissene Gelenkstifte/Bolzen (35%)
2. Ausgeschlagene Lagerbuchsen (25%)
3. Lose Schraubverbindungen (vibrations-bedingt) (20%)
4. Verschlissene Steuerleinen (Dehnung) (15%)
5. Kegelrad-Zahnspiel zu groß (Verschleiß) (5%)

**Diagnose:**
1. Alle Gelenke einzeln prüfen — Spiel fühlbar?
2. Bolzen und Stifte auf Verschleiß prüfen (Einschnürung, Abrieb)
3. Lagerbuchsen auf Ovalität prüfen
4. Steuerleinen-Spannung prüfen — <5 kg = zu locker
5. Kegelradgetriebe auf Zahnflankenspiel prüfen

**Behebung:**
- Bolzen/Stifte austauschen (Edelstahl 316L, Herstellermaße)
- Lagerbuchsen erneuern (originale Buchsen oder PTFE/Delrin-Buchsen)
- Schraubverbindungen mit Schraubensicherung (Loctite 243 blau) sichern
- Steuerleinen erneuern und korrekt vorspannen (8–12 kg)
- Kegelradgetriebe: bei übermäßigem Spiel Zahnräder tauschen

**Präventivmaßnahmen:**
- Alle 500 Seemeilen: Verbindungen auf festen Sitz prüfen
- Alle 2.000 Seemeilen: Bolzen und Buchsen inspizieren
- Alle 5.000 Seemeilen: Steuerleinen erneuern
- Schraubensicherung bei allen vibrationsbelasteten Verbindungen verwenden

**AYDI-Severity:** MITTEL bis HOCH — abhängig vom Ausmaß des Spiels
**AYDI-Confidence:** measured (physische Inspektion), visual_medium (Video der Geräusche/Bewegung)

### 6.5 Fehlerbild F05: Korrosion an tragenden Teilen

**Symptome:**
- Weiße Korrosionsprodukte an Aluminium-Teilen (Aluminium-Oxidation)
- Braune Rostflecken an Edelstahl-Teilen (Lochfraß, Spaltkorrosion)
- Aufgeblähte oder poröse Oberflächen
- Strukturelle Schwächung — Teile fühlen sich "weich" an
- Elektrolytische Korrosion an Kontaktstellen verschiedener Metalle

**Ursachen (nach Häufigkeit):**
1. Fehlender Korrosionsschutz nach Montage (30%)
2. Kontaktkorrosion Aluminium/Edelstahl ohne Isolierung (25%)
3. Edelstahl 304 statt 316L verwendet (15%)
4. Salzwasser-Ablagerungen nicht regelmäßig abgespült (15%)
5. Beschädigte Eloxierung/Beschichtung nicht ausgebessert (15%)

**Diagnose:**
1. Visuelle Inspektion aller Metalloberflächen — Farbveränderungen, Blasen, Pitting
2. Klopftest — dumpfer Klang = innere Korrosion
3. Biegetest (nur bei demontiertem Teil!) — brüchig = fortgeschrittene Korrosion
4. Materialidentifikation — Magnettest: 316L ist leicht magnetisch, 304 stärker
5. Kontaktkorrosion-Check: Verschiedene Metalle in direktem Kontakt?

**Behebung:**
- Leichte Oberflächenkorrosion: Schleifen (220er Korn), Passivierung, Konservierung
- Mittlere Korrosion: Professionelle Aufarbeitung oder Teileaustausch
- Schwere Korrosion (tragende Teile): Sofortiger Austausch — Sicherheitsrisiko!
- Kontaktkorrosion: Metalle isolieren (Nylon-Buchsen, Isolierband, Tef-Gel)

**Präventivmaßnahmen:**
- Nach jeder Salzwasser-Fahrt: Anlage mit Süßwasser abspülen
- Halbjährlich: Alle Metalloberflächen mit Korrosionsschutz behandeln (Lanocote, Tef-Gel)
- Kontaktstellen verschiedener Metalle immer mit Isolierung versehen
- Opferanoden an Aluminium-Teilen im Unterwasserbereich
- Nur 316L-Edelstahl für alle Verbindungselemente verwenden

**AYDI-Severity:** HOCH bis KRITISCH — bei tragenden Teilen Sicherheitsrisiko
**AYDI-Confidence:** visual_high (Korrosion gut visuell erkennbar), measured (Materialprüfung)

### 6.6 Fehlerbild F06: Aufhängung/Rahmen verbogen

**Symptome:**
- Windfahne steht nicht mehr senkrecht
- Pendelruder hängt schräg im Wasser
- Sichtbare Verformung des Rahmens oder der Montagehalterung
- Schwergängigkeit durch Verspannung
- Geräusche durch Verspannung bei Seegang

**Ursachen (nach Häufigkeit):**
1. Grundberührung mit Pendelruder (35%)
2. Kollision mit Hafenanlage (Dalben, Steg) beim Rückwärtsfahren (25%)
3. Treibgut (Baumstamm, Container, Netz) (20%)
4. Materialermüdung durch Dauerschwingbelastung (10%)
5. Unsachgemäße Montage (Überlastung einzelner Befestigungspunkte) (10%)

**Diagnose:**
1. Visuelle Inspektion mit Wasserwaage und Lot
2. Rahmen vom Boot demontieren und auf ebener Fläche prüfen
3. Befestigungspunkte am Boot prüfen — sind diese verformt?
4. Pendelruder-Achse auf Geradheit prüfen
5. Lager auf Leichtgängigkeit nach Verformung prüfen

**Behebung:**
- Leichte Verformung: Professionelles Richten (nur bei Edelstahl, nicht bei Aluminium!)
- Aluminium-Rahmen: Nicht richten — Bruchgefahr! Austausch nötig.
- Edelstahl-Rahmen: Kann warm gerichtet werden (nur vom Fachmann)
- Montagehalterung: Befestigungspunkte am Boot prüfen, ggf. neu verstärken
- Pendelruder-Achse: Bei Verformung immer austauschen (nie richten)

**AYDI-Severity:** HOCH — System funktioniert nicht korrekt, Sekundärschäden möglich
**AYDI-Confidence:** visual_high (Verformung gut sichtbar), measured (Winkelmessung)

### 6.7 Fehlerbild F07: Steuerleinen rutschen / greifen nicht

**Symptome:**
- Windfahne und Pendelruder arbeiten korrekt, aber Boot reagiert nicht
- Steuerrad dreht sich nicht bzw. zu wenig
- Leinen sind sichtbar lose oder durchhängend
- Pendelruder schwingt voll aus, aber keine Ruderwirkung

**Ursachen (nach Häufigkeit):**
1. Steuerleinen auf Steuertrommel rutschen (falsche Wicklung) (30%)
2. Steuerleinen zu lang / zu viel Dehnung (25%)
3. Umlenkrollen blockiert oder falsch positioniert (20%)
4. Steuerrad-Reibungsbremse zu fest angezogen (Radsteuerung) (15%)
5. Steuerleinen falsch geführt (Überkreuzung, Knick) (10%)

**Diagnose:**
1. Steuerleinen-Spannung prüfen (Soll: 8–12 kg)
2. Wicklung auf Steuertrommel prüfen (mind. 2 volle Umläufe)
3. Umlenkrollen einzeln prüfen — drehen sie frei?
4. Leinenführung verfolgen — Knicke, Scheuerstellen?
5. Bei Radsteuerung: Reibungsbremse lösen und prüfen

**Behebung:**
- Wicklung korrigieren: Mind. 2,5 Umdrehungen auf Steuertrommel, kein Überkreuzen
- Leinen kürzen/erneuern: Dehnungsarmes Material (Dyneema SK78)
- Umlenkrollen reinigen/tauschen: Salzwasser ausspülen, Lager prüfen
- Reibungsbremse: Auf Minimum einstellen (gerade so, dass Rad nicht selbstständig dreht)
- Leinenführung optimieren: Großzügige Radien, keine Knicke, keine Scheuerstellen

**AYDI-Severity:** MITTEL — System funktioniert mechanisch, Übertragung defekt
**AYDI-Confidence:** measured (physische Prüfung), visual_medium (Foto der Leinenführung)

### 6.8 Fehlerbild F08: Pendelruder-Blatt gebrochen/verloren

**Symptome:**
- Plötzlicher Totalausfall der Steuerung
- Sichtbar abgebrochenes oder fehlendes Pendelruder-Blatt
- Nur noch der Schaft im Wasser
- Erhöhter Ruderwiderstand (wenn Blattreste am Schaft hängen)

**Ursachen (nach Häufigkeit):**
1. Kollision mit Treibgut bei hoher Fahrt (40%)
2. Materialermüdung an der Blatt-Schaft-Verbindung (25%)
3. Grundberührung bei Geschwindigkeit (20%)
4. Korrosion an der Blatt-Schaft-Verbindung (10%)
5. Fertigungsfehler (selten bei Markenprodukten) (5%)

**Diagnose:**
1. Visuelle Inspektion — Blatt vorhanden/fehlend/gebrochen?
2. Bruchstelle inspizieren — glatter Bruch = Überlastung, körnig = Ermüdung
3. Schaft auf Verformung prüfen
4. Verbleibende Halterung auf Beschädigung prüfen

**Behebung:**
- Ersatz-Pendelruder montieren (sollte an Bord sein!)
- Provisorium: Sperrholzblatt (12–18 mm Marine-Sperrholz) auf Schaft montieren
- Im Hafen: Originalersatzteil beim Hersteller bestellen
- Schaft prüfen und ggf. mitaustauschen

**Präventivmaßnahmen:**
- IMMER Ersatz-Pendelruder an Bord haben (Hersteller bieten diese an)
- Pendelruder in flachen Gewässern und Häfen hochklappen
- Regelmäßige Inspektion der Blatt-Schaft-Verbindung auf Risse
- Bei Dämmerung/Nacht: Pendelruder hochklappen, wenn nicht gesteuert wird (Treibgut-Risiko)

**AYDI-Severity:** KRITISCH — Totalausfall
**AYDI-Confidence:** visual_high (offensichtlicher Schaden), measured (Bruchanalyse)

### 6.9 Fehlerbild F09: Kegelradgetriebe-Verschleiß

**Symptome:**
- Klickendes oder ratschendes Geräusch bei Fahnenbewegung
- Zunehmendes Spiel zwischen Fahne und Pendelruder
- Fahne bewegt sich, Pendelruder reagiert verzögert
- Metallische Späne im Getriebefett sichtbar

**Ursachen:**
1. Normaler Verschleiß nach 15.000–30.000 Seemeilen (50%)
2. Unzureichende Schmierung (25%)
3. Salzwasser-Eindrang ins Getriebe (15%)
4. Fehlstellung/Fehlausrichtung der Zahnräder (10%)

**Diagnose:**
1. Getriebe freilegen und visuell inspizieren
2. Zahnflanken auf Abnutzungsmuster prüfen
3. Zahnspiel messen (Soll: 0,1–0,3 mm, abhängig vom Hersteller)
4. Fettqualität prüfen — metallische Partikel?

**Behebung:**
- Leichter Verschleiß: Reinigen, neu fetten, Spiel nachjustieren
- Mittlerer Verschleiß: Zahnräder tauschen (Herstellerersatzteil)
- Schwerer Verschleiß: Komplettes Getriebegehäuse und Zahnräder tauschen
- Professionelle Wartung: Getriebe ausbauen, reinigen, Dichtungen erneuern, neu fetten

**AYDI-Severity:** MITTEL — fortschreitend, Totalausfall bei Ignorieren
**AYDI-Confidence:** measured (Getriebe-Inspektion), estimated (Meilenbasis)

### 6.10 Fehlerbild F10: Montagehalterung lose / Decksleck

**Symptome:**
- Windfahnenanlage wackelt am Heck
- Sichtbare Risse im Gelcoat um Befestigungsbolzen
- Wassereinbruch am Heckspiegel (innen sichtbar)
- Bewegung der Anlage bei Seegang hör-/fühlbar

**Ursachen:**
1. Unterdimensionierte Backing-Plates (40%)
2. Keine Dichtung zwischen Halterung und Heckspiegel (20%)
3. Gelockerte Bolzen durch Vibration (20%)
4. Heckspiegel-Laminat zu dünn (Delaminierung) (15%)
5. Falsche Bolzenqualität (Korrosion im Laminat) (5%)

**Diagnose:**
1. Halterung von Hand bewegen — sichtbares Spiel?
2. Innenseite des Heckspiegels inspizieren — Feuchtigkeit, Risse?
3. Bolzen prüfen — korrodiert, lose?
4. Backing-Plates prüfen — vorhanden, ausreichend dimensioniert?
5. Laminat um Bohrungen prüfen — Risse, Verfärbungen?

**Behebung:**
- Backing-Plates vergrößern (mind. 100×100 mm, 6 mm Edelstahl)
- Alle Bolzen mit Dichtmasse (Sikaflex 291) setzen
- Gelockerte Bolzen: Löcher ausbohren, mit Epoxid füllen, neu bohren
- Heckspiegel verstärken: GFK-Laminat von innen aufbauen (3–5 Lagen)
- Bolzen in Edelstahl 316L A4 tauschen, Nyloc-Muttern verwenden

**AYDI-Severity:** HOCH — Strukturelles Risiko, Wassereinbruch
**AYDI-Confidence:** visual_high (Risse sichtbar), measured (Feuchtigkeitsmessung)

### 6.11 Fehlerbild F11: Fahne bricht bei Starkwind ab

**Symptome:**
- Windfahne fehlt oder ist abgebrochen
- Bruchstelle am Drehpunkt oder Befestigungspunkt sichtbar
- System funktionslos

**Ursachen:**
1. Materialermüdung an der Achsbefestigung (35%)
2. Extreme Windlast (>50 kn) ohne vorheriges Reffen/Sichern der Fahne (30%)
3. Korrosion an der Achsbohrung (20%)
4. Schlag durch Baum/Genua-Schot bei ungewollter Halse (15%)

**Diagnose:**
1. Bruchstelle inspizieren — Ermüdung vs. Überlastung
2. Verbleibende Achsbefestigung auf weitere Risse prüfen
3. Material-Zustand der Fahne (wenn geborgen) beurteilen

**Behebung:**
- Ersatzfahne montieren (sollte an Bord sein!)
- Provisorium: Sperrholzfahne (6–8 mm Marine-Sperrholz) zuschneiden
- Im Hafen: Originalersatzteil bestellen

**Präventivmaßnahmen:**
- IMMER Ersatzfahne an Bord (leicht, wenig Platz)
- Bei Starkwind >40 kn: Fahne sichern oder durch kleinere ersetzen
- Achsbefestigung jährlich auf Risse prüfen (Lupe oder Rissprüfspray)

**AYDI-Severity:** KRITISCH — Totalausfall
**AYDI-Confidence:** visual_high (offensichtlich)

### 6.12 Fehlerbild F12: System steuert einseitig / konstanter Kursversatz

**Symptome:**
- Boot hält Kurs, aber mit konstantem Versatz (z.B. 10° nach Lee)
- Windfahne steht nicht neutral (leicht gekippt auch auf Kurs)
- Pendelruder permanent leicht angestellt
- Steuerleinen asymmetrisch gespannt

**Ursachen:**
1. Lee-Helm durch falschen Segeltrimm (40%)
2. Windfahne falsch kalibriert / Neutralstellung verschoben (25%)
3. Asymmetrische Steuerleinen-Spannung (15%)
4. Verbogene Pendelruder-Achse (leichte Verformung) (10%)
5. Einseitig verschlissenes Kegelradgetriebe (10%)

**Diagnose:**
1. Segeltrimm prüfen: Boot unter Segel ohne Windfahne — hält es Kurs bei Mittschiffs-Ruder?
2. Windfahne-Neutralstellung prüfen: Fahne muss bei korrektem Kurs senkrecht stehen
3. Steuerleinen-Spannung beidseitig messen (Federwaage)
4. Pendelruder-Achse auf Geradheit prüfen
5. Kegelrad auf einseitigen Verschleiß prüfen

**Behebung:**
- Segeltrimm optimieren: Traveller, Großschot, Vorsegel-Position
- Windfahne nachkalibrieren: Neutralstellung gemäß Herstelleranleitung justieren
- Steuerleinen: Beidseitig gleichmäßig spannen
- Achse: Bei Verformung austauschen
- Kegelrad: Bei einseitigem Verschleiß Zahnräder tauschen

**AYDI-Severity:** NIEDRIG bis MITTEL — System funktioniert, aber suboptimal
**AYDI-Confidence:** measured (wenn Segeltrimm messbar), estimated (Segeltrimmbeurteilung)

---

## 7. Troubleshooting-Entscheidungsbäume

### 7.1 Entscheidungsbaum EB-01: "Windfahne steuert nicht"

```
START: Windfahne steuert nicht
│
├── Schritt 1: Ist die Windfahne montiert und unbeschädigt?
│   ├── NEIN → Fahne prüfen/ersetzen → ENDE
│   └── JA → weiter
│
├── Schritt 2: Kippt die Fahne bei Kursabweichung?
│   ├── NEIN → Fahne blockiert?
│   │   ├── JA → Lager reinigen/schmieren → Fahne muss frei kippen → TESTE
│   │   └── NEIN → Zu wenig Wind? (<5 kn scheinbar)
│   │       ├── JA → Windfahne kann nicht steuern, Autopilot nutzen → ENDE
│   │       └── NEIN → Fahne defekt, ersetzen → ENDE
│   └── JA → weiter
│
├── Schritt 3: Reagiert das Pendelruder / Hilfsruder auf Fahnenbewegung?
│   ├── NEIN → Kegelradgetriebe prüfen
│   │   ├── Getriebe blockiert → reinigen, fetten → TESTE
│   │   ├── Getriebe gebrochen → Ersatzteil einbauen → TESTE
│   │   └── Gestänge gelöst → Verbindung wiederherstellen → TESTE
│   └── JA → weiter
│
├── Schritt 4: (Nur Servo-Pendulum) Pendelt das Pendelruder seitlich aus?
│   ├── NEIN → Fährt das Boot? (Strömung nötig!)
│   │   ├── NEIN → Boot muss fahren (>2,5 kn) → ENDE
│   │   └── JA → Pendelruder-Achse klemmt → Achse prüfen, schmieren → TESTE
│   └── JA → weiter
│
├── Schritt 5: (Nur Servo-Pendulum) Bewegen sich die Steuerleinen?
│   ├── NEIN → Leinen gebrochen/gelöst → Leinen erneuern/befestigen → TESTE
│   └── JA → weiter
│
├── Schritt 6: Reagiert das Steuerrad/die Pinne auf die Leinenbewegung?
│   ├── NEIN → Steuerleinen rutschen auf Trommel → Wicklung korrigieren → TESTE
│   │         Steuerrad-Bremse zu fest → Bremse lösen → TESTE
│   │         Leinen zu lang/zu viel Dehnung → Leinen kürzen/erneuern → TESTE
│   └── JA → weiter
│
├── Schritt 7: Dreht das Boot bei Ruderausschlag?
│   ├── NEIN → Hauptruder defekt! → Hauptruder prüfen → ENDE (anderes Problem)
│   └── JA → System funktioniert grundsätzlich, Feinabstimmung nötig
│       → Segeltrimm optimieren
│       → Fahnenempfindlichkeit einstellen
│       → TESTE
│
ENDE
```

### 7.2 Entscheidungsbaum EB-02: "Boot giert stark (Übersteuerung)"

```
START: Boot giert stark um Sollkurs
│
├── Schritt 1: Giert das Boot auch ohne Windfahne (von Hand gesteuert)?
│   ├── JA → Problem ist Boot/Segel, nicht Windfahne
│   │   ├── Segeltrimm prüfen → Segel ausbalancieren → TESTE
│   │   ├── Ruderanlage prüfen → Spiel im Ruder? → Reparieren → TESTE
│   │   └── Seebedingungen → Kreuzsee erzeugt unvermeidbares Gieren → AKZEPTIEREN
│   └── NEIN → Windfahne überreagiert → weiter
│
├── Schritt 2: Ist die Windstärke >25 kn scheinbar?
│   ├── JA → Fahne hat zu viel Kraft
│   │   ├── Kleinere Fahne montieren → TESTE
│   │   ├── Fahne teilweise abdecken (untere Hälfte) → TESTE
│   │   └── Fahne tiefer einstellen (weniger Exposition) → TESTE
│   └── NEIN → weiter
│
├── Schritt 3: Hat das Boot ausreichend Lee-Helm?
│   ├── NEIN (neutraler oder Luv-Helm) → Segeltrimm ändern
│   │   ├── Großsegel dichter → mehr Lee-Helm → TESTE
│   │   ├── Vorsegel weiter nach vorn → TESTE
│   │   └── Traveller nach Luv → TESTE
│   └── JA (leichter Lee-Helm, 3–5°) → weiter
│
├── Schritt 4: Schlägt Pendelruder von Anschlag zu Anschlag?
│   ├── JA → Pendelruder-Ausschlag begrenzen
│   │   ├── Mechanische Anschläge enger stellen → TESTE
│   │   └── Übersetzung im Kegelrad reduzieren (wenn einstellbar) → TESTE
│   └── NEIN → weiter
│
├── Schritt 5: Ist die Steuerleinen-Länge korrekt?
│   ├── NEIN (zu viel Lose) → Leinen kürzen, Spannung erhöhen → TESTE
│   └── JA → Feinjustierung der Fahne → Gewicht an Fahne (Trägheit erhöhen) → TESTE
│
ENDE
```

### 7.3 Entscheidungsbaum EB-03: "Korrosionsproblem diagnostizieren"

```
START: Korrosion an Windfahnenanlage festgestellt
│
├── Schritt 1: Welches Material ist betroffen?
│   ├── ALUMINIUM → weiter zu Schritt 2a
│   ├── EDELSTAHL → weiter zu Schritt 2b
│   └── MISCHMETALL (Kontaktkorrosion) → weiter zu Schritt 2c
│
├── Schritt 2a: Aluminium-Korrosion
│   ├── Weiße, pulvrige Oberfläche (Aluminiumoxid)?
│   │   ├── Nur oberflächlich → Reinigen, Passivierung auftragen → KONTROLLE
│   │   └── Tiefe Narben/Pitting → Materialstärke messen
│   │       ├── >80% Reststärke → Reinigen, füllen (Marine-Epoxid), beschichten → KONTROLLE
│   │       └── <80% Reststärke → TEIL AUSTAUSCHEN (Sicherheitsrisiko) → ENDE
│   └── Keine sichtbare Korrosion, aber Oberfläche rau?
│       → Eloxierung verschlissen → neu eloxieren oder beschichten → KONTROLLE
│
├── Schritt 2b: Edelstahl-Korrosion
│   ├── Braune Flecken (Tea Staining)?
│   │   → Oberflächlich → Edelstahl-Reiniger + Passivierung → KONTROLLE
│   ├── Lochfraß (Pitting)?
│   │   ├── Oberflächlich (<0,5 mm) → Schleifen, Passivierung → KONTROLLE
│   │   └── Tief (>0,5 mm) → an tragendem Teil?
│   │       ├── JA → TEIL AUSTAUSCHEN → ENDE
│   │       └── NEIN → Schleifen, füllen, beobachten → KONTROLLE
│   ├── Spaltkorrosion (an Verbindungsstellen)?
│   │   → Verbindung öffnen, reinigen, mit Tef-Gel neu montieren → KONTROLLE
│   └── Ist das Material wirklich 316L?
│       ├── Magnettest: stark magnetisch → wahrscheinlich 304 → AUSTAUSCHEN gegen 316L
│       └── Schwach oder nicht magnetisch → 316L korrekt → anderer Korrosionsmechanismus
│
├── Schritt 2c: Kontaktkorrosion (Mischmetall)
│   ├── Welche Metalle sind in Kontakt?
│   │   ├── Aluminium + Edelstahl → ISOLIEREN mit Nylon-Buchsen + Tef-Gel
│   │   ├── Aluminium + Kupfer/Bronze → ISOLIEREN (hohe Spannungsdifferenz!)
│   │   └── Edelstahl + Kupfer/Bronze → Meist unkritisch → beobachten
│   └── Isolation vorhanden, aber trotzdem Korrosion?
│       → Isolierung beschädigt/porös → erneuern → KONTROLLE
│
KONTROLLE: Nach 3 Monaten erneut inspizieren
│   ├── Korrosion gestoppt → ENDE (Wartungsintervall: halbjährlich)
│   └── Korrosion fortgeschritten → Professionelle Beurteilung einholen → ENDE
│
ENDE
```

### 7.4 Entscheidungsbaum EB-04: "Leistung auf Raumschotskurs ungenügend"

```
START: Windfahne steuert auf Raumschotskurs schlecht
│
├── Schritt 1: Wie stark ist der scheinbare Wind?
│   ├── <8 kn → Zu wenig Wind für zuverlässige Steuerung auf Raumschots
│   │   ├── Fahne vergrößern (Wechselfahne) → TESTE
│   │   ├── Geschwindigkeit reduzieren (Segel reffen) → mehr scheinbarer Wind → TESTE
│   │   └── Autopilot verwenden → ENDE
│   └── >8 kn → weiter
│
├── Schritt 2: Ist der Segeltrimm für Raumschots optimiert?
│   ├── NEIN →
│   │   ├── Spi-Baum dichter setzen → stabilerer Kurs → TESTE
│   │   ├── Großsegel mit Preventer sichern → weniger Schlagen → TESTE
│   │   ├── Segel reduzieren, wenn Boot überpowert → TESTE
│   │   └── Butterfly-Konfiguration prüfen → symmetrischer Segeldruck → TESTE
│   └── JA → weiter
│
├── Schritt 3: Giert das Boot rhythmisch (Rollgieren)?
│   ├── JA → Boot hat Rollgieren-Problem (typisch auf Raumschots bei Achterlicher See)
│   │   ├── Segel weiter nach achtern trimmen
│   │   ├── Passap-Segel oder Trysegel setzen (stabilisiert)
│   │   ├── Schleppbremse (Drogue) ausbringen → stabilisiert
│   │   └── Kurs ändern: 10–15° abfallen oder höher gehen → weniger Rollgieren
│   └── NEIN → weiter
│
├── Schritt 4: Reagiert die Windfahne überhaupt?
│   ├── Träge/gar nicht → Fahnenempfindlichkeit erhöhen
│   │   ├── Leichtere Fahne montieren
│   │   ├── Lager schmieren
│   │   └── Kegelrad-Übersetzung erhöhen (wenn einstellbar)
│   └── JA, aber Boot folgt nicht →
│       ├── Servo-Pendulum: Mehr Leinenspannung → TESTE
│       ├── Aux. Rudder: Hilfsruder zu klein → Limit des Systems → Autopilot ergänzen
│       └── Strömungsabriss am Pendelruder? → Anstellwinkel begrenzen → TESTE
│
ENDE: Raumschotskurs ist die anspruchsvollste Bedingung für Windfahnen.
      Perfekte Steuerung auf Raumschots erfordert optimalen Segeltrimm UND
      optimale Windfahnen-Einstellung. Erwartung anpassen: ±8–12° Kursabweichung
      ist auf Raumschots normal und akzeptabel.
```

### 7.5 Entscheidungsbaum EB-05: "Welches System für mein Boot?"

```
START: Systemauswahl für Windfahnen-Selbststeueranlage
│
├── Schritt 1: Bootsgröße und Verdrängung?
│   ├── <8 t und <35 ft → Alle Systeme geeignet → weiter
│   ├── 8–18 t und 35–50 ft → Standard-Systeme → weiter
│   ├── 18–25 t und 50–55 ft → Nur Heavy-Duty-Systeme
│   │   → Windpilot Pacific Plus ODER Monitor MX → weiter zu Schritt 4
│   └── >25 t oder >55 ft → Windfahne allein nicht ausreichend
│       → Hybridlösung: Windfahne + leistungsstarker Autopilot → SPEZIALBERATUNG
│
├── Schritt 2: Steuerungstyp?
│   ├── PINNENSTEUERUNG → Servo-Pendulum ideal
│   │   → Windpilot Pacific oder Monitor M → weiter zu Schritt 4
│   ├── RADSTEUERUNG (frei drehbar) → Alle Systeme geeignet → weiter
│   └── RADSTEUERUNG (blockierend / schwergängig) →
│       ├── Kann Reibungsbremse gelöst werden? → JA → Servo-Pendulum möglich → weiter
│       └── NEIN → Auxiliary Rudder nötig → Hydrovane oder Cape Horn → weiter zu Schritt 4
│
├── Schritt 3: Ist Notruder-Funktion gewünscht?
│   ├── JA (Langfahrt, Sicherheitsprioriät) →
│   │   ├── Hydrovane → sicherste Notruder-Funktion
│   │   └── Cape Horn → ebenfalls Notruder-fähig
│   └── NEIN → Alle Systeme geeignet → weiter zu Schritt 4
│
├── Schritt 4: Heck-Geometrie?
│   ├── Klassisches Heck (schmal, überhängend) → Alle Systeme gut montierbar
│   ├── Spiegel-Heck mit Badeplattform → 
│   │   ├── Plattform kann gebohrt werden → Servo-Pendulum montierbar
│   │   └── Plattform soll frei bleiben → Hydrovane seitlich → oder Cape Horn
│   ├── Breites, modernes Heck (>2,5 m) →
│   │   ├── Servo-Pendulum: Lange Leinenführung → funktioniert, aber aufwendig
│   │   └── Auxiliary Rudder: Seitliche Montage → kurze Kraftwege
│   └── Kein Heckspiegel (Canoe Stern) → Spezial-Montageadapter nötig → HERSTELLERBERATUNG
│
├── Schritt 5: Budget?
│   ├── <3.000 € → Cape Horn (ab ~2.400 €) oder gebrauchte Anlage
│   ├── 3.000–5.000 € → Monitor M, Windpilot Pacific, Sailomat
│   ├── 5.000–7.000 € → Windpilot Pacific Plus, Hydrovane, Monitor MX
│   └── >7.000 € → Premium-Installation mit professioneller Montage
│
ERGEBNIS: Empfehlung basierend auf den Antworten
```

---

## 8. FAQ

### 8.1 Grundlagen

**F01: Was ist der Unterschied zwischen einer Windfahne und einem Autopiloten?**
Eine Windfahne steuert mechanisch nach dem scheinbaren Wind (keine Energie nötig), ein Autopilot steuert elektrisch nach Kompass oder GPS (braucht Strom). Auf Langfahrt kombiniert man idealerweise beides: Windfahne für Amwind- bis Raumschotskurse, Autopilot für Vorwind und Motorfahrt.

**F02: Brauche ich als Langfahrtsegler wirklich eine Windfahne?**
Nicht zwingend, aber sehr empfehlenswert. Die Windfahne spart 800–1.600 Wh/Tag Energie (das entspricht 1–2 Stunden Motorbetrieb zum Laden), ist komplett ausfallsicher (keine Elektronik), und steuert bei Seegang oft besser als ein Autopilot. Etwa 80% aller Langfahrtsegler auf Langstrecken (>3.000 sm) haben eine Windfahne an Bord.

**F03: Funktioniert eine Windfahne auch bei Flaute unter Motor?**
Nein. Die Windfahne braucht scheinbaren Wind als Referenz. Unter Motor bei Windstille gibt es zwar Fahrtwind, aber dieser kommt immer von vorn — die Windfahne hat keine Richtungsinformation. Für Motorfahrt muss der Autopilot übernehmen.

**F04: Kann ich eine Windfahne auf einem Katamaran montieren?**
Grundsätzlich ja, aber mit Einschränkungen. Katamarane haben oft Mittelruder oder Doppelruder, die das Servo-Pendulum-Prinzip erschweren. Auxiliary-Rudder-Systeme (Hydrovane) funktionieren besser, da sie unabhängig vom Hauptruder arbeiten. Allerdings ist die seitliche Montage auf dem schmalen Heckspiegel eines Katamarans oft schwierig.

**F05: Wie genau steuert eine Windfahne?**
Typisch ±3–5° Amwind, ±5–8° Halbwind, ±8–12° Raumschots. Zum Vergleich: Ein guter Autopilot schafft ±1–3°. Für Langfahrt ist die Windfahnen-Genauigkeit mehr als ausreichend — ein paar Grad Kursabweichung machen auf einer Atlantiküberquerung keinen messbaren Unterschied.

### 8.2 Auswahl und Kauf

**F06: Welches System ist das beste?**
Es gibt kein universell bestes System. Servo-Pendulum (Windpilot, Monitor) ist am leistungsfähigsten und für die meisten Boote optimal. Auxiliary Rudder (Hydrovane, Cape Horn) bietet Notruder-Funktion und braucht keine Steuerleinen. Die Wahl hängt von Boot, Budget und Sicherheitsbedürfnis ab.

**F07: Kann ich eine Windfahne gebraucht kaufen?**
Ja, der Gebrauchtmarkt ist aktiv. Windpilot und Monitor sind oft 10–20 Jahre alt und noch voll funktionsfähig. Worauf achten: Korrosion an tragenden Teilen, Spiel in Lagern und Gelenken, Zustand des Pendelruders. Ein gebrauchter Windpilot Pacific kostet 1.500–2.500 €, ein Monitor 1.000–2.000 USD.

**F08: Was kostet die Montage?**
Professionelle Montage: 500–2.000 € (abhängig von Boot und System). Selbstmontage ist möglich und wird von den meisten Herstellern unterstützt (detaillierte Anleitungen). Für Servo-Pendulum-Systeme ist die Montage aufwendiger (Halterung am Heck + Leinenführung), für Auxiliary-Rudder-Systeme einfacher (ein Befestigungspunkt).

**F09: Passt eine Windfahne auf mein modernes Serienboot?**
Fast immer ja. Alle großen Hersteller bieten bootsspezifische Montageadapter an. Windpilot hat eine Datenbank mit über 3.000 Bootstypen. Problematisch können sehr breite, flache Hecks sein (z.B. Beneteau Oceanis ab 2018), aber auch dafür gibt es Lösungen (erhöhte Montage, seitliche Position).

**F10: Windpilot oder Monitor — welchen soll ich nehmen?**
Beide sind exzellente Servo-Pendulum-Systeme. Windpilot hat den Vorteil der Aluminium-Konstruktion (leichter) und des persönlichen Services von Peter Matthiesen. Monitor hat den Vorteil der Edelstahl-Konstruktion (robuster) und des größeren Nutzernetzwerks (besonders in Nordamerika). In Europa ist Windpilot leicht im Vorteil (kürzere Lieferwege, Service), in Nordamerika der Monitor.

### 8.3 Montage und Einstellung

**F11: Wie lange dauert die Montage?**
Selbstmontage: 8–16 Stunden für erfahrene Heimwerker. Professionelle Montage: 4–8 Stunden für erfahrene Techniker. Hauptaufwand: Halterung am Heck befestigen (Bohren, Verstärken), Leinenführung installieren (nur Servo-Pendulum), Feineinstellung.

**F12: Muss ich am Heckspiegel bohren?**
Ja, in den meisten Fällen. Die Halterung wird mit 4–8 Bolzen (M10 oder M12) durch den Heckspiegel befestigt. Von innen Backing-Plates (min. 6 mm Edelstahl, 100×100 mm). Alle Bohrungen mit Dichtmasse (Sikaflex 291i oder gleichwertig) abdichten. Bei GFK-Heck ggf. lokale Verstärkung nötig.

**F13: Wie stelle ich die Windfahne richtig ein?**
Grundeinstellung: Fahne senkrecht, wenn Boot auf gewünschtem Kurs segelt. Feineinstellung: Segeltrimm so optimieren, dass das Boot mit Mittschiffs-Ruder annähernd Kurs hält. Dann Windfahne aktivieren. Bei Gieren: Fahnenempfindlichkeit reduzieren (Gewicht, kleinere Fahne). Bei träger Reaktion: Empfindlichkeit erhöhen (leichtere Fahne, mehr Übersetzung).

**F14: Wie führe ich die Steuerleinen zum Steuerrad?**
Die Steuerleinen laufen vom Pendelruder über Umlenkrollen (mindestens 4) zum Steuerrad. Typische Führung: Pendelruder → Heckrolle (je Seite) → Cockpitsüll-Rolle (je Seite) → Steuertrommel. Die Leinen müssen großzügige Radien haben (keine Knicke), frei laufen und dürfen nirgendwo scheuern. Mindestens 2,5 Umdrehungen auf der Steuertrommel.

**F15: Kann ich Windfahne und Autopilot gleichzeitig betreiben?**
Nein. Die beiden Systeme arbeiten gegeneinander — die Windfahne steuert nach Wind, der Autopilot nach Kompass. Wenn sich der Wind dreht, korrigiert die Windfahne, während der Autopilot dagegensteuert. Immer nur ein System aktiv! Umschalten: Windfahnen-Leinen lösen/klemmen, Autopilot ein/aus.

### 8.4 Betrieb und Leistung

**F16: Bei welcher Mindest-Windstärke funktioniert die Windfahne?**
Typisch ab 5–6 Knoten scheinbarer Wind. Bei weniger Wind hat die Fahne zu wenig Kraft. In der Praxis: Wenn genug Wind zum Segeln da ist (>8 kn wahrer Wind, Boot macht >3 kn), funktioniert die Windfahne. In Leichtwind-Bedingungen ist der Autopilot die bessere Wahl.

**F17: Wie verhält sich die Windfahne bei Starkwind?**
Überraschend gut. Im Gegensatz zum Autopiloten, der bei starkem Seegang mit Verzögerung reagiert (Sensor → Berechnung → Motor → Ruder), reagiert die Windfahne sofort und proportional. Bei 35+ kn Wind arbeitet die Windfahne oft besser als ein Autopilot. Allerdings: Ab ca. 40 kn sollte die Fahne gegen eine kleinere getauscht oder teilweise abgedeckt werden (Übersteuerungsgefahr).

**F18: Was ist das typische Wartungsintervall?**
- Wöchentlich: Sichtprüfung, Steuerleinen auf Scheuerstellen prüfen
- Monatlich: Alle Gelenke und Lager schmieren
- Halbjährlich: Kegelradgetriebe inspizieren, alle Bolzen auf festen Sitz prüfen
- Jährlich: Pendelruder-Achse auf Verschleiß/Verformung prüfen, Steuerleinen erneuern (wenn nötig)
- Alle 2–3 Jahre: Komplettinspektion, ggf. Lager und Buchsen tauschen

**F19: Meine Windfahne steuert nur nach einer Seite gut — was tun?**
Wahrscheinlich Lee-Helm durch asymmetrischen Segeltrimm. Erst den Segeltrimm optimieren (neutraler Ruderstand). Dann die Windfahnen-Neutralstellung überprüfen (Fahne muss senkrecht stehen bei Kurs). Steuerleinen beidseitig gleich spannen. Pendelruder-Achse auf Geradheit prüfen.

**F20: Kann die Windfahne bei einer Patenthalse beschädigt werden?**
Ja. Eine ungewollte Halse (Patenthalse) kann den Großbaum über das Boot schlagen. Wenn der Großbaum oder die Genua-Schot die Windfahne trifft, können Fahne oder Gestänge beschädigt werden. Prävention: Preventer (Bullenstander) verwenden, nicht zu tief am Wind segeln, Aufmerksamkeit beim Vorwindsegeln.

### 8.5 Ersatzteile und Reparatur

**F21: Welche Ersatzteile sollte ich auf Langfahrt mitnehmen?**
Unbedingt: Ersatz-Windfahne, Ersatz-Pendelruder (oder Pendelruder-Blatt), 2 × Steuerleinen (komplett), Satz Splinte und Sicherungsscheiben, Kegelrad-Ersatzzahnräder (wenn vom Hersteller empfohlen), Lagerbuchsen-Satz, Marinefett (Tube). Optional: Ersatz-Umlenkrollen, Werkzeugsatz für Demontage/Montage.

**F22: Wie lange halten die einzelnen Komponenten?**
- Rahmen: 20–40 Jahre (Aluminium) bzw. 30–50 Jahre (Edelstahl)
- Windfahne: 10–20 Jahre (UV-Alterung, Materialdiskontinuität)
- Pendelruder-Blatt: 10–15 Jahre (Strömungsverschleiß)
- Kegelradgetriebe: 15.000–30.000 Seemeilen (verschleißabhängig)
- Steuerleinen: 3.000–8.000 Seemeilen (materialabhängig)
- Lagerbuchsen: 10.000–20.000 Seemeilen
- Umlenkrollen: 10–15 Jahre

**F23: Kann ich eine Aries noch reparieren, obwohl sie nicht mehr hergestellt wird?**
Ja, eingeschränkt. Einige Spezialisten (z.B. in England und Frankreich) haben noch Aries-Ersatzteile. Universelle Teile (Bolzen, Buchsen, Steuerleinen) sind ohnehin Standard. Spezifische Teile (Fahne, Pendelruder) können ggf. nachgefertigt werden. Windpilot bietet Adapter-Kits an, um Aries-Halterungen mit modernen Windpilot-Systemen zu nutzen.

### 8.6 Spezialfragen

**F24: Kann ich eine Windfahne für Regatta einsetzen?**
Theoretisch ja, praktisch nein. Für Einhand-Regatten (OSTAR, Route du Rhum) werden Windfahnen gelegentlich als Backup mitgeführt, aber die Primärsteuerung erfolgt über leistungsstarke Autopiloten (Genauigkeit ±1°). Für Crew-Regatten sind Windfahnen nicht relevant (Rudergänger steuert besser).

**F25: Wie beeinflusst eine Windfahne den Wiederverkaufswert meines Bootes?**
Positiv — bei Langfahrt-Yachten. Eine gut installierte, gewartete Windpilot Pacific oder Monitor steigert den Wert um 50–80% des Neupreises. Bei reinen Küstenbooten ist der Effekt geringer (viele Käufer nutzen nur den Autopiloten). Eine schlecht montierte oder korrodierte Anlage kann den Wert mindern.

**F26: Kann ich eine Windfahne selbst bauen?**
Grundsätzlich ja — die Prinzipien sind nicht patentiert. In den 1970er–1990er Jahren haben viele Langfahrtsegler Eigenbau-Windfahnen konstruiert. Heute ist das selten, weil die industriellen Produkte ausgereift und bezahlbar sind. Wer dennoch bauen will: Peter Matthiesens Bücher enthalten detaillierte Konstruktionszeichnungen und Dimensionierungshilfen.

**F27: Wie verhalten sich Windfahnen in den Tropen (wenig Wind)?**
In den Tropen (Passatregion, 10–20 kn konstanter Wind) funktionieren Windfahnen hervorragend — es sind die idealen Bedingungen: konstanter Wind, lange Wellen, wenig Böen. In der Kalmenzone (ITCZ, 0–5 kn) funktionieren sie nicht — hier muss der Autopilot übernehmen. Typische Passatüberquerung: 80–90% Windfahne, 10–20% Autopilot.

**F28: Stört die Windfahne beim Baden/Ankern?**
Servo-Pendulum (Windpilot, Monitor): Das Pendelruder sollte im Hafen/auf Anker hochgeklappt werden. Das Gestell selbst kann den Zugang zur Badeplattform einschränken — abhängig von der Bootskonfiguration. Einige Segler montieren die Badeleiter seitlich, wenn eine Windfahne installiert ist.
Auxiliary Rudder (Hydrovane): Seitlich montiert, stört weniger die Badeplattform, aber das Hilfsruder ragt permanent ins Wasser.

**F29: Wie transportiere ich eine Windfahne beim Bootstransport auf dem Trailer?**
Die meisten Systeme sind zerlegbar. Pendelruder hochklappen, Windfahne abnehmen, ggf. Rahmen demontieren. Beim Trailer-Transport: Maximale Höhe prüfen (Fahne kann 1,2–1,5 m über Deckshöhe ragen). Windpilot bietet spezielle Klappvorrichtungen an.

### 8.7 Problembezogene Fragen

**F30: Mein Monitor macht klickende Geräusche — was ist das?**
Wahrscheinlich verschlissene Sperrklinken (Pawls) im Kegelradgetriebe oder ausgeschlagene Lager. Getriebe öffnen und inspizieren. Typischer Verschleiß nach 20.000+ Seemeilen. Ersatzteile bei Scanmar International bestellen.

---

## 9. Glossar

### 9.1 Begriffe A–Z

| Nr. | Begriff (DE) | Begriff (EN) | Definition |
|---|---|---|---|
| G01 | **Anstellwinkel** | Angle of attack | Winkel zwischen Profil-Sehne (Ruder, Fahne) und Anströmrichtung. Bestimmt Auftrieb und Widerstand. |
| G02 | **Auxiliary Rudder** | Auxiliary rudder | Hilfsruder — eigenständiges Ruder am Heck, von der Windfahne gesteuert, unabhängig vom Hauptruder. |
| G03 | **Backing Plate** | Backing plate | Verstärkungsplatte auf der Innenseite des Heckspiegels zur Lastverteilung der Befestigungsbolzen. |
| G04 | **Bullenstander** | Preventer | Leine, die den Großbaum gegen ungewolltes Übergehen (Patenthalse) sichert. |
| G05 | **Capstan-Effekt** | Capstan effect | Reibungsverstärkung einer Leine auf einer Trommel. Haltekraft steigt exponentiell mit Umschlingungswinkel. |
| G06 | **Dämpfung** | Damping | Energieabbau im Regelsystem, der Oszillationen (Gieren) reduziert. |
| G07 | **Dyneema** | Dyneema | Ultra-hochmolekulares Polyethylen (UHMWPE) — extrem zugfest, dehnungsarm, UV-beständig. Ideal für Steuerleinen. |
| G08 | **Fahne** | Vane / Wind vane | Aerodynamisches Element, das den scheinbaren Wind detektiert und bei Kursabweichung ein Drehmoment erzeugt. |
| G09 | **Fahrtwind** | Headwind / Apparent wind component | Windkomponente, die durch die Eigenbewegung des Bootes entsteht. Kommt immer von vorn. |
| G10 | **Gieren** | Yawing | Drehbewegung des Bootes um die Hochachse — unerwünschte Kursoszillation. |
| G11 | **Halbwind** | Beam reach | Kurs mit Wind querab (ca. 90° zum wahren Wind). |
| G12 | **H-Fahne** | Horizontal axis vane | Windfahne mit horizontaler Drehachse. Kippt seitlich bei Windwinkeländerung. Höhere Kraft als V-Fahne. |
| G13 | **Hilfsruder** | Auxiliary rudder | Eigenständiges Ruder am Heck, das von der Windfahne gesteuert wird und unabhängig vom Hauptruder arbeitet. |
| G14 | **Horizontalachse** | Horizontal axis | Drehachse der H-Fahne, verläuft horizontal quer zur Schiffslängsachse. |
| G15 | **Kegelradgetriebe** | Bevel gear | Zahnradgetriebe zur Umsetzung einer Drehbewegung um 90°. Wandelt Fahnen-Kippbewegung in Pendelruder-Anstellung. |
| G16 | **Kursabweichung** | Course deviation | Differenz zwischen Sollkurs (eingestellter Windwinkel) und Istkurs. Auslöser für Korrektur. |
| G17 | **Kursstabilität** | Course stability | Eigenschaft eines Bootes, bei Rudermittelstellung den Kurs beizubehalten. Abhängig von Kielform, Ruderanlage, Lateralplan. |
| G18 | **Lateralplan** | Lateral plane | Projektion des Unterwasserschiffs auf eine Vertikalebene. Bestimmt die Richtungsstabilität. |
| G19 | **Lee-Helm** | Lee helm / Weather helm | Tendenz des Bootes, nach Lee (vom Wind weg) abzufallen. Wird durch Segeldruck nach Luv erzeugt. Erfordert Gegenruder. |
| G20 | **Leinenführung** | Line routing | Weg der Steuerleinen vom Pendelruder über Umlenkrollen zum Steuerrad/Pinne. |
| G21 | **Luv-Gierigkeit** | Weather helm tendency | Leichte Tendenz des Bootes, nach Luv (in den Wind) zu drehen. Ideal für Windfahrensteuerung (3–5°). |
| G22 | **Notruder** | Emergency rudder | Ersatzsteuervorrichtung bei Ausfall des Hauptruders. Hydrovane und Cape Horn können als Notruder dienen. |
| G23 | **OSTAR** | OSTAR | Observer Single-handed Trans-Atlantic Race. Einhand-Atlantikregatta, bei der Windfahnen historisch eine zentrale Rolle spielten. |
| G24 | **Patenthalse** | Accidental jibe / Gybe | Ungewolltes Übergehen des Großsegels auf die andere Seite bei Vorwindkurs. Gefährlich für Crew und Ausrüstung. |
| G25 | **Pendelruder** | Servo pendulum blade | Ruderblatt am Servo-Pendulum-System, das durch Wasserströmung seitlich ausschwingt und über Leinen das Hauptruder betätigt. |
| G26 | **Preventer** | Preventer | Siehe Bullenstander (G04). |
| G27 | **P-Regler** | P-controller | Proportionalregler — Stellgröße proportional zur Regelabweichung. Windfahne arbeitet als mechanischer P-Regler. |
| G28 | **Raumschots** | Broad reach | Kurs mit Wind von schräg achtern (ca. 120–150° zum wahren Wind). |
| G29 | **Regelabweichung** | Steady-state error | Bleibende Differenz zwischen Soll- und Istwert bei einem P-Regler. Bei Windfahne: konstanter Kursversatz bei dauerhaftem Lee-Helm. |
| G30 | **Rollgieren** | Rolling yaw | Kopplungsbewegung zwischen Rollen (Seitbewegung) und Gieren (Richtungsänderung). Typisch auf Vorwindkursen. |
| G31 | **Scheinbarer Wind** | Apparent wind | Vektorsumme aus wahrem Wind und Fahrtwind. Referenz für die Windfahne. |
| G32 | **Segeltrimm** | Sail trim | Einstellung der Segel (Schot, Traveller, Cunningham, etc.) für optimale Performance und ausgeglichene Ruderkräfte. |
| G33 | **Servo-Pendulum** | Servo pendulum | Prinzip, bei dem ein Ruderblatt durch Wasserströmung eine Servokraft erzeugt, die über Leinen das Hauptruder betätigt. |
| G34 | **Servokraft** | Servo force | Die vom Pendelruder durch Wasserströmung erzeugte Kraft. Vielfaches der Windfahnen-Kraft. |
| G35 | **Spatenruder** | Spade rudder | Freistehdendes Ruder ohne Skeg. Typisch bei modernen Segelyachten. |
| G36 | **Steuerleine** | Control line | Leine, die das Pendelruder mit dem Steuerrad/der Pinne verbindet und die Servokraft überträgt. |
| G37 | **Steuertrommel** | Steering drum | Trommel am Steuerrad, auf der die Steuerleinen aufgewickelt sind. |
| G38 | **Strömungsabriss** | Flow separation / Stall | Ablösung der Strömung vom Ruder-/Fahnenprofil bei zu großem Anstellwinkel. Resultiert in dramatischem Kraftverlust. |
| G39 | **Tef-Gel** | Tef-Gel | PTFE-basiertes Anti-Seize-Mittel, das Kontaktkorrosion zwischen verschiedenen Metallen verhindert. |
| G40 | **Trim-Tab** | Trim tab | Trimmklappe — kleines Ruderblatt an der Hinterkante eines Hauptruders oder Hilfsruders. |
| G41 | **Umlenkrolle** | Turning block | Rolle, die die Steuerleine in eine andere Richtung umlenkt. Muss leichtgängig und salzwasserbeständig sein. |
| G42 | **V-Fahne** | Vertical axis vane | Windfahne mit vertikaler Drehachse. Dreht sich wie eine Wetterfahne. Geringere Kraft als H-Fahne. |
| G43 | **Wahrer Wind** | True wind | Tatsächlicher Wind über Grund, unabhängig von der Bootsbewegung. |
| G44 | **Windpilot** | Windpilot | Markenname der Windfahnen-Selbststeueranlagen von Peter Matthiesen, Hamburg. Auch umgangssprachlich als Gattungsbegriff verwendet. |
| G45 | **Windschatten** | Wind shadow / Lee | Bereich hinter einem Hindernis (Segel, Rumpf), in dem der Wind reduziert oder abgelenkt ist. Kann die Windfahne beeinträchtigen. |

---

## 10. Schnell-Referenz

### 10.1 Schnell-Vergleich: Welches System für welchen Einsatz?

```
┌──────────────────────────────────────────────────────────────────┐
│ SCHNELL-ENTSCHEIDUNG: WINDFAHNEN-SELBSTSTEUERANLAGE              │
├──────────────────────────────────────────────────────────────────┤
│                                                                  │
│ SERVO-PENDULUM (Windpilot, Monitor):                            │
│ ✓ Beste Steuerleistung aller Systeme                            │
│ ✓ Am Wind bis Raumschots exzellent                              │
│ ✓ Für Pinnen- und Radsteuerung                                  │
│ ✗ Braucht Steuerleinen zum Hauptruder                           │
│ ✗ Keine Notruder-Funktion                                       │
│ → EMPFOHLEN FÜR: Die meisten Langfahrt-Yachten                 │
│                                                                  │
│ AUXILIARY RUDDER (Hydrovane):                                    │
│ ✓ Notruder-Funktion (einzigartig!)                              │
│ ✓ Keine Steuerleinen nötig                                      │
│ ✓ Unabhängig vom Hauptruder                                     │
│ ✗ Geringere Steuerleistung                                      │
│ ✗ Permanentes Zusatzruder im Wasser                             │
│ → EMPFOHLEN FÜR: Sicherheitsbewusste Blauwasser-Segler         │
│                                                                  │
│ AUX. RUDDER + TRIM-TAB (Cape Horn, Sailomat):                  │
│ ✓ Gute Steuerleistung durch doppeltes Servo                    │
│ ✓ Notruder-Funktion                                             │
│ ✓ Moderate Kosten                                               │
│ ✗ Komplexere Mechanik                                           │
│ → EMPFOHLEN FÜR: Mittlere Budgets, Langfahrt                   │
│                                                                  │
└──────────────────────────────────────────────────────────────────┘
```

### 10.2 Wartungsintervalle — Checkliste

```
┌──────────────────────────────────────────────────────────────────┐
│ WARTUNGSPLAN WINDFAHNEN-SELBSTSTEUERANLAGE                       │
├──────────────┬───────────────────────────────────────────────────┤
│ WÖCHENTLICH  │ □ Sichtprüfung alle Verbindungen                │
│              │ □ Steuerleinen auf Scheuerstellen prüfen          │
│              │ □ Pendelruder auf freien Lauf prüfen              │
│              │ □ Windfahne auf freie Beweglichkeit prüfen        │
├──────────────┼───────────────────────────────────────────────────┤
│ MONATLICH    │ □ Alle Lager und Gelenke schmieren (Marinefett)  │
│              │ □ Umlenkrollen prüfen und schmieren               │
│              │ □ Steuerleinen-Spannung prüfen (8–12 kg)          │
│              │ □ Bolzen auf festen Sitz prüfen                   │
├──────────────┼───────────────────────────────────────────────────┤
│ HALBJÄHRLICH │ □ Kegelradgetriebe öffnen und inspizieren         │
│              │ □ Getriebefett erneuern                           │
│              │ □ Alle Metalloberflächen auf Korrosion prüfen     │
│              │ □ Korrosionsschutz auffrischen                    │
│              │ □ Pendelruder-Achse auf Geradheit prüfen          │
├──────────────┼───────────────────────────────────────────────────┤
│ JÄHRLICH     │ □ Komplett-Inspektion aller Teile                 │
│              │ □ Steuerleinen erneuern (wenn >5.000 sm)          │
│              │ □ Lagerbuchsen auf Verschleiß prüfen              │
│              │ □ Montagehalterung und Backing-Plates prüfen      │
│              │ □ Pendelruder-Blatt auf Erosion prüfen            │
│              │ □ Bolzen-Dichtungen erneuern (Sikaflex)           │
├──────────────┼───────────────────────────────────────────────────┤
│ ALLE 3 JAHRE │ □ Kegelrad-Zahnräder auf Verschleiß prüfen       │
│              │ □ Lagerbuchsen erneuern                           │
│              │ □ Windfahne auf UV-Schäden prüfen                 │
│              │ □ Professionelle Komplett-Revision erwägen        │
└──────────────┴───────────────────────────────────────────────────┘
```

### 10.3 Ersatzteil-Prioritäten für Langfahrt

```
MUSS AN BORD (Sicherheitskritisch):
├── Ersatz-Windfahne (komplette Fahne)
├── Ersatz-Pendelruder oder -Blatt
├── 2 × Steuerleine (komplette Länge, Dyneema 8mm)
├── Satz Splinte und Sicherungsscheiben
└── Marinefett (1 Tube Teflon-Marinefett)

SOLLTE AN BORD (Empfohlen):
├── Kegelrad-Ersatzzahnräder
├── Lagerbuchsen-Satz
├── 2 × Ersatz-Umlenkrolle
├── Sortiment Bolzen M8/M10 Edelstahl 316L
└── Schraubensicherung (Loctite 243)

NICE TO HAVE:
├── Werkzeugsatz für Komplett-Demontage
├── Notfall-Reparaturset (Marine-Epoxid, Sperrholz)
└── Herstelleranleitung (wasserdicht verpackt)
```

### 10.4 Leistungsgrenzen-Übersicht

```
┌──────────────────────────────────────────────────────────────┐
│ BETRIEBSGRENZEN WINDFAHNEN-SELBSTSTEUERANLAGE                │
├────────────────────────┬─────────────────────────────────────┤
│ Mindest-Windstärke     │ 5–6 kn scheinbar (≈ 8 kn wahr)    │
│ Optimaler Bereich      │ 10–30 kn scheinbar                  │
│ Max. empfohlen         │ 40 kn scheinbar (Fahne verkleinern)│
│ Mindest-Bootsspeed     │ 2,5 kn (Servo braucht Strömung)    │
│ Optimaler Speed        │ 4–8 kn                              │
│ Bester Kurs            │ Am Wind (30–50° scheinbar)          │
│ Guter Kurs             │ Halbwind (60–100° scheinbar)        │
│ Akzeptabler Kurs       │ Raumschots (100–140° scheinbar)     │
│ Problematischer Kurs   │ Vorwind (>150° scheinbar)           │
│ Kursgenauigkeit Am Wind│ ±3–5°                                │
│ Kursgenauigkeit Raum   │ ±8–12°                               │
│ Max. Bootsgröße        │ 55 ft / 25 t (Heavy-Duty-System)    │
│ Min. Bootsgröße        │ 24 ft / 2,5 t                       │
└────────────────────────┴─────────────────────────────────────┘
```

---

## 11. ANHANG A–H — Fallstudien

### ANHANG A: Fallstudie — Hallberg-Rassy 36 mit Windpilot Pacific

**Boot:** Hallberg-Rassy 36 Mk II (2008)
**Eigner:** Paar, 50er Jahre, erste Langfahrt
**Route:** Ostsee → Atlantik → Karibik → Azoren → Mittelmeer (2 Jahre, ca. 18.000 sm)

**Ausgangslage:**
- Boot: 10,85 m LüA, 3,52 m Breite, 7,5 t Verdrängung
- Radsteuerung (Lewmar)
- Bestehende Ausrüstung: Raymarine ST2000+ Autopilot (Pinnentyp, adaptiert)
- Budget für Windfahne: 5.000 €

**Systemwahl:**
Windpilot Pacific — Empfehlung von Peter Matthiesen nach persönlicher Beratung.
Begründung: HR 36 ist ein kursstabiles Boot mit moderatem Deplacement. Der Pacific ist die Standard-Version, mehr als ausreichend für 7,5 t. Die HR 36 hat einen klassischen Heckspiegel, ideal für die Montage.

**Montage:**
- Professionelle Montage durch Windpilot-Partner in Kiel
- Montageadapter: HR 36 Standardadapter (Windpilot hat die HR 36 in der Datenbank)
- 6 × M10 Bolzen durch Heckspiegel, Backing-Plates 120×120×8 mm Edelstahl
- Leinenführung: 4 Umlenkrollen (2 Heck, 2 Cockpitsüll), 2 × 12 m Dyneema 8 mm
- Montagezeit: 6 Stunden (professionell)
- Gesamtkosten: Windpilot Pacific (4.400 €) + Adapter (450 €) + Montage (800 €) = 5.650 €

**Betriebserfahrungen:**

*Atlantik-Überquerung (Las Palmas → Barbados, 2.700 sm, 19 Tage):*
- Windfahne als Primärsteuerung: 85% der Zeit (ca. 16 Tage)
- Autopilot: 10% (Leichtwind-Tage, Vorwindkurs mit Butterfly)
- Handsteuerung: 5% (An- und Ablegemanöver, Squalls)
- Kursgenauigkeit: ±4–6° (Am Wind), ±8–10° (Raumschots)
- Energieeinsparung: ca. 22 kWh über 19 Tage (≈ 1.200 Wh/Tag Autopilot-Verbrauch gespart)
- Probleme: Keine (korrekt eingestellt ab Tag 2)

*Karibik (6 Monate, ca. 3.000 sm):*
- Windfahne ideal für Interinsel-Segeln (konstanter Passat, Am-Wind-Kurse)
- Autopilot für kurze Motorstrecken bei Flaute
- Einmal Steuerleine erneuert (Scheuerung an schlecht positionierter Rolle — Rolle versetzt)
- Pendelruder einmal hochgeklappt vergessen beim Rückwärts-Anlegen → kurzer Schreck, kein Schaden

*Azoren-Rückfahrt (Bermuda-Azoren, 1.800 sm, 14 Tage):*
- Windfahne 90% der Zeit aktiv
- Herausfordernde Bedingungen: 30–40 kn Wind, 4 m Welle
- Windfahne steuerte besser als der Raymarine Autopilot in diesen Bedingungen
- Fahne einmal gegen kleinere Fahne getauscht (bei 45 kn Böen — Übersteuerung)

**Fazit des Eigners:**
"Die Windpilot war die beste Investition unserer Langfahrt-Vorbereitung. Wir haben 5.650 € investiert und dafür 2 Jahre lang sorgenfreie Steuerung bekommen. Der Energiespar-Effekt ist enorm — wir konnten unsere Solaranlage kleiner dimensionieren. Die Montage war professionell, der Service von Windpilot erstklassig (E-Mail-Beratung auch unterwegs). Einziger Nachteil: Die Anlage ragt über die Badeplattform hinaus, was beim Ankern etwas stört."

**AYDI-Analyse:**
- Systemwahl: OPTIMAL (Bootsgröße, Verdrängung, Heckgeometrie ideal für Pacific)
- Montage: PROFESSIONELL (korrekte Backing-Plates, Dichtung, Leinenführung)
- Betrieb: EXZELLENT (Segeltrimm offenbar gut optimiert → hohe Windfahnen-Performance)
- Wartung: BEFRIEDIGEND (Steuerleinen-Scheuerung hätte bei korrekter Erstinstallation vermieden werden können)

### ANHANG B: Fallstudie — Bavaria 40 Cruiser mit Monitor M

**Boot:** Bavaria 40 Cruiser (2012)
**Eigner:** Einhandsegler, 45 Jahre, erfahren
**Route:** Mittelmeer → Atlantik → Karibik → Panamakanal → Pazifik (Langzeitfahrt, 3+ Jahre)

**Ausgangslage:**
- Boot: 12,14 m LüA, 3,99 m Breite, 8,5 t Verdrängung
- Radsteuerung (Jefa)
- Bestehend: Simrad TP32 Tillerpilot
- Budget: 4.000 USD

**Systemwahl:**
Monitor M — Entscheidung des Eigners aufgrund der großen Nutzergemeinde im Pazifik (gute Ersatzteilversorgung in Panama, Galapagos, Marquesas, Neuseeland, Australien).

**Montage:**
- Selbstmontage in Marina di Ragusa, Sizilien
- Montageadapter: Bavaria-Adapter von Scanmar (2 seitliche Rohre)
- 8 × M12 Bolzen (4 pro Seite), Backing-Plates 150×100×10 mm
- Montagezeit: 14 Stunden Selbstmontage (2 Tage)
- Gesamtkosten: Monitor M (3.600 USD) + Versand (280 USD) + Material (150 €) = ca. 3.900 USD

**Betriebserfahrungen:**

*Mittelmeer → Gibraltar (1.200 sm, 10 Tage):*
- Einfahren des Systems, Feinabstimmung
- Herausforderung: Bavaria 40 ist weniger kursstabil als ein Langkieler → mehr Korrekturaufwand
- Lösung: Segeltrimm optimiert (Großsegel etwas gefiert, Vorsegel dichter)
- Ergebnis nach Optimierung: ±5–7° Am Wind, ±10–14° Raumschots

*Atlantik-Überquerung (Kanaren → Kap Verde → Barbados, 3.200 sm, 22 Tage):*
- Windfahne 75% der Zeit, Autopilot 20%, Hand 5%
- Vorwindkurse (Passat auf Raumschots) erforderten häufige Kursanpassungen
- Autopilot bei Vorwind-Squalls eingesetzt (Winddreh → Windfahne folgt → Kursänderung unerwünscht)
- Energiebilanz: Deutlich entspannter als erwartet, Solarpanels reichten für Nicht-Autopilot-Verbrauch

*Pazifik-Passage (Galapagos → Marquesas, 3.000 sm, 21 Tage):*
- Konstantester Passat der gesamten Reise → Windfahne 90%+ der Zeit
- Keinerlei Wartungsbedarf auf der Passage
- "Set and forget" — Monitor steuerte tagelang ohne jede Korrektur

*Neuseeland (Refit nach 25.000 sm):*
- Kegelrad-Zahnräder zeigten leichten Verschleiß → ausgetauscht (Ersatzteile in Auckland verfügbar)
- Lagerbuchsen erneuert
- Pendelruder-Blatt hatte leichte Erosionsspuren → noch nicht tauschbedürftig
- Steuerleinen zweimal erneuert (alle 10.000 sm)
- Gesamtkosten Wartung über 25.000 sm: ca. 350 USD

**Fazit des Eigners:**
"Der Monitor ist ein Arbeitstier. Nicht so elegant wie der Windpilot, aber unverwüstlich. Edelstahl sieht nach 3 Jahren Salzwasser aus wie am ersten Tag. Ersatzteile in jedem Langfahrthafen verfügbar — im Pazifik haben mir andere Segler sogar gebrauchte Teile geschenkt. Einziger Kritikpunkt: Das Edelstahlgestell ist schwer (22 kg) und beeinflusst den Trimm der Bavaria merklich."

**AYDI-Analyse:**
- Systemwahl: GUT (Bavaria 40 ist grenzwertig kurslabil für Windfahne, Monitor M angemessen)
- Montage: GUT (Selbstmontage gelungen, korrekte Backing-Plates)
- Betrieb: GUT (Einschränkungen auf Vorwindkurs systembedingt)
- Wartung: VORBILDLICH (regelmäßige Wartung, rechtzeitige Ersatzteilbeschaffung)

### ANHANG C: Fallstudie — Oyster 435 mit Hydrovane

**Boot:** Oyster 435 (2005)
**Eigner:** Ehepaar, 60er Jahre, Sicherheits-orientiert
**Route:** England → Atlantik → Karibik → Panama → Pazifik → Australien (3 Jahre)

**Ausgangslage:**
- Boot: 13,30 m LüA, 4,12 m Breite, 12,5 t Verdrängung, Langkiel
- Radsteuerung (Whitlock)
- Bestehend: Raymarine EV-200 Autopilot (hydraulisch)
- Budget: 7.000 GBP

**Systemwahl:**
Hydrovane — Entscheidung aufgrund der Notruder-Funktion. Der Eigner hatte auf einer früheren Reise einen Ruderbruch erlebt und wollte maximale Redundanz.

**Montage:**
- Professionelle Montage bei der Oyster-Werft in Southampton
- Montage an der Steuerbord-Heckseite
- Spezielle Verstärkung des Heckspiegels (GFK-Laminat von innen, 5 Lagen)
- Montagezeit: 12 Stunden (professionell, inkl. Laminatarbeit)
- Gesamtkosten: Hydrovane (5.200 GBP) + Montage inkl. Verstärkung (1.400 GBP) = 6.600 GBP

**Betriebserfahrungen:**

*Atlantik-Überquerung (27 Tage):*
- Hydrovane als Primärsteuerung: 60% der Zeit
- Autopilot: 35% (besonders auf Vorwindkursen)
- Hand: 5%
- Die Hydrovane steuerte zuverlässig, aber weniger genau als der EV-200 Autopilot
- Kursgenauigkeit: ±6–8° Am Wind, ±12–15° Raumschots
- Energieeinsparung: ca. 15 kWh über 27 Tage

*Tasman-See (Neuseeland → Australien):*
- Schwere Bedingungen: 35–50 kn Wind, 5–7 m Welle
- Hydrovane steuerte 3 Tage lang allein durch den Sturm
- Autopilot ausgefallen (Hydraulik-Leck) → Hydrovane übernahm für 48 Stunden allein
- "Die Hydrovane hat uns buchstäblich gerettet" — Eigner

*Notruder-Einsatz (Fidschi):*
- Hauptruder-Lager schadhaft → Steuerung schwergängig
- Hydrovane als Notruder eingesetzt für 120 sm Fahrt zur nächsten Werft
- Pinne auf Hydrovane-Schaft montiert → volle Steuerfähigkeit
- Reparatur des Hauptruders in 3 Tagen, Hydrovane danach wieder im Normalbetrieb

**Fazit des Eigners:**
"Die Hydrovane ist unsere Versicherung. Sie steuert nicht so präzise wie der Autopilot, aber sie braucht keinen Strom und kann uns im Notfall nach Hause bringen. Der Moment in der Tasman-See, als der Autopilot ausfiel und die Hydrovane übernahm, hat die gesamte Investition gerechtfertigt. Wir würden nie ohne Hydrovane auf Langfahrt gehen."

**AYDI-Analyse:**
- Systemwahl: OPTIMAL FÜR EINSATZZWECK (Sicherheit priorisiert, Notruder entscheidend)
- Montage: EXZELLENT (Professionell durch Werft, GFK-Verstärkung, korrekte Dimensionierung)
- Betrieb: GUT (Geringere Genauigkeit als Servo-Pendulum — systembedingt)
- Wartung: SEHR GUT (minimal — Hydrovane hat wenige bewegliche Teile)
- Sicherheits-Bewertung: HERAUSRAGEND (Notruder-Funktion praxisvalidiert)

### ANHANG D: Fallstudie — Westsail 32 mit Aries (historisch)

**Boot:** Westsail 32 (1976)
**Eigner:** Einhandsegler, 60er Jahre, Langfahrt-Veteran
**Route:** Weltumsegelung via Kap Hoorn (1989–1993)

**Ausgangslage:**
- Boot: 9,75 m LüA, 3,28 m Breite, 8,4 t Verdrängung, Langkiel, Pinnensteuerung
- Aries Windvane (montiert seit 1987)
- Kein elektrischer Autopilot (bewusste Entscheidung — "weniger Elektronik, weniger Probleme")

**Systemwahl:**
Aries — zu dieser Zeit eines der führenden Systeme. V-Fahne, Servo-Pendulum mit Trim-Tab.

**Betriebserfahrungen (Zusammenfassung über 42.000 sm):**

- Aries steuerte geschätzt 85% der 42.000 sm
- Westsail 32 ist ein extrem kursstabiles Boot → idealer Partner für Windfahne
- Kursgenauigkeit: ±3–4° Am Wind (exzellent für eine Aries)
- Kap Hoorn-Passage: Aries steuerte bei 55 kn Wind und 8 m Welle zuverlässig
- Einziger Totalausfall: Pendelruder-Blatt nach Kollision mit Treibholz vor Südamerika → Ersatzblatt montiert (3 Stunden Reparatur auf See)

**Wartung über 42.000 sm:**
- 3 × Steuerleinen erneuert
- 2 × Pendelruder-Blatt erneuert (1× Kollision, 1× Verschleiß)
- 1 × Kegelradgetriebe komplett überholt (bei 30.000 sm)
- 1 × V-Fahne erneuert (UV-Schaden nach 5 Jahren)
- Gesamte Wartungskosten: ca. 800 GBP über 4 Jahre

**AYDI-Analyse:**
- System: HISTORISCH RELEVANT — Aries war zu seiner Zeit State-of-the-Art
- Kombination Westsail 32 + Aries: IDEAL (extrem kursstabiles Boot + bewährtes System)
- Robustheit: EXZELLENT (42.000 sm inkl. Kap Hoorn mit nur einem Totalausfall)
- Relevanz heute: EINGESCHRÄNKT (Aries nicht mehr erhältlich, aber Gebrauchte funktionieren weiter)

### ANHANG E: Fallstudie — Beneteau Oceanis 45 mit Windpilot Pacific Plus

**Boot:** Beneteau Oceanis 45 (2016)
**Eigner:** Familie (2 Erwachsene, 2 Kinder), Langfahrt-Sabbatical
**Route:** Frankreich → Karibik → Rückreise via Azoren (18 Monate, ca. 12.000 sm)

**Ausgangslage:**
- Boot: 13,78 m LüA, 4,51 m Breite, 10,2 t Verdrängung
- HERAUSFORDERUNG: Sehr breites, flaches Heck, große Badeplattform
- Doppelruder (Twin Rudder) — Radsteuerung
- Bestehend: B&G Pilot (hydraulisch)

**Systemwahl:**
Windpilot Pacific Plus — gewählt wegen der Erfahrung von Windpilot mit modernen Breithecks. Peter Matthiesen hatte einen speziellen Adapter für die Oceanis 45 entwickelt.

**Montage-Herausforderung:**
Das breite Heck der Oceanis 45 stellte besondere Anforderungen:
- Badeplattform musste teilweise modifiziert werden
- Lange Leinenführung (2,2 m Breite am Heck → ca. 16 m Gesamtleinenlänge)
- Doppelruder: Steuerleinen auf Steuertrommel des Steuerbord-Rades
- Spezial-Adapter erhöhte Windpilot um 150 mm für bessere Windexposition
- Montagezeit: 16 Stunden (professionell, inkl. Heck-Modifikation)
- Gesamtkosten: Pacific Plus (5.400 €) + Spezialadapter (680 €) + Montage (1.600 €) = 7.680 €

**Betriebserfahrungen:**

- Windfahne funktionierte gut, aber die lange Leinenführung verursachte etwas mehr Reibung → leicht reduzierte Sensitivität
- Segeltrimm musste sorgfältig optimiert werden — Oceanis 45 mit Twin Rudder und breitem Heck ist weniger kursstabil als klassische Langkieler
- Kursgenauigkeit: ±5–7° Am Wind, ±10–14° Raumschots
- Kinder konnten die Badeplattform weiterhin nutzen (Pendelruder hochgeklappt)
- Autopilot B&G wurde für Vorwind und Motorfahrt genutzt (35% der Zeit)

**Fazit des Eigners:**
"Die Installation war aufwendiger und teurer als erwartet. Die Oceanis 45 ist kein ideales Windfahren-Boot — zu breit, zu wenig kursstabil. Aber es funktioniert! Für die Atlantik-Überquerung war die Windpilot unverzichtbar (Energieeinsparung, Sicherheit). Für Tagessegelei im Mittelmeer nutzen wir sie selten. Empfehlung an andere Oceanis-Eigner: Es geht, aber mit Kompromissen."

**AYDI-Analyse:**
- Systemwahl: ANGEMESSEN (Pacific Plus für 10,2 t leicht überdimensioniert, aber sinnvoll wegen breitem Heck und reduzierter Kursstabilität)
- Montage: ANSPRUCHSVOLL (Breites Heck erfordert Kompromisse, professionell gelöst)
- Betrieb: BEFRIEDIGEND (Moderne Serienboote sind nicht ideal für Windfahnen, aber funktional)
- Kosten: HOCH (7.680 € — die Heck-Modifikation treibt den Preis)
- Empfehlung: Bei Booten dieser Bauart immer professionelle Montage und Herstellerberatung

### ANHANG F: Fallstudie — Nauticat 38 mit Cape Horn

**Boot:** Nauticat 38 Pilot House (1998)
**Eigner:** Rentnerpaar, Skandinavien-Liebhaber
**Route:** Finnland → Norwegische Küste → Island → Schottland → Retour (Sommer-Kreuzfahrten, 5 Jahre)

**Ausgangslage:**
- Boot: 11,58 m LüA, 3,68 m Breite, 11,5 t Verdrängung, Langkiel
- Pinnensteuerung im Cockpit, Radsteuerung im Pilothouse
- Bestehend: Simrad AP35 Autopilot

**Systemwahl:**
Cape Horn Windvane — gewählt wegen des guten Preis-Leistungs-Verhältnisses und der Notruder-Funktion (wichtig für arktische Gewässer mit Treibholz- und Eisrisiko).

**Kosten:** Cape Horn (4.200 CAD ≈ 2.900 €) + Versand (350 €) + Selbstmontage = ca. 3.400 € gesamt

**Betriebserfahrungen:**
- Nauticat 38 mit Langkiel ist extrem kursstabil → Cape Horn steuert hervorragend
- Auxiliary-Rudder-Prinzip ideal, da Radsteuerung im Pilothouse nicht für Steuerleinen adaptierbar
- Island-Umrundung: Cape Horn steuerte 70% der Zeit (15 Tage)
- Norwegische Küste: Weniger Windfahnen-Nutzung (häufige Kursänderungen in Fjorden)
- Notruder einmal getestet (Übung) — funktioniert zuverlässig

**AYDI-Analyse:**
- Systemwahl: OPTIMAL (Langkieler + Pilothouse → Auxiliary Rudder ideal)
- Preis-Leistung: EXZELLENT (3.400 € für vollwertiges System)
- Einsatzzweck: GUT (Küstenlangfahrt, Notruder für arktische Gewässer sinnvoll)

### ANHANG G: Fallstudie — Amel Super Maramu mit Hydrovane + Autopilot (Hybrid)

**Boot:** Amel Super Maramu 2000 (2001)
**Eigner:** Einhandsegler, 55 Jahre, Weltumsegelung
**Route:** Frankreich → Mittelmeer → Suez → Indischer Ozean → Australien → Pazifik → Panama → Karibik → Atlantik (5 Jahre, ca. 55.000 sm)

**Ausgangslage:**
- Boot: 16,10 m LüA, 4,69 m Breite, 14,5 t Verdrängung
- Amel-spezifische Steueranlage (Ketten-Steuerung)
- Bestehend: Lecomble & Schmitt hydraulischer Autopilot (Amel-Standard)

**Systemwahl:**
Hydrovane — Amel Super Maramu ist ein Spezialfall: Die Ketten-Steuerung ist schwergängig und nicht für Steuerleinen adaptierbar → Servo-Pendulum scheidet aus. Hydrovane als Auxiliary Rudder arbeitet unabhängig vom Hauptruder und ist daher die einzige praktikable Windfahnen-Lösung für Amel-Yachten.

**Montage:**
- Spezial-Halterung für Amel Super Maramu (Hydrovane hat Amel-Erfahrung)
- Montage an Steuerbord-Heckseite
- Gesamtkosten: 6.200 GBP inkl. Montage

**Betriebserfahrungen (55.000 sm über 5 Jahre):**
- Hydrovane als Primärsteuerung: 45% der Zeit
- Autopilot: 50% (bei Vorwind, Motorfahrt, engen Gewässern)
- Hand: 5%
- Hydrovane weniger effektiv als auf leichteren Booten (14,5 t an der Kapazitätsgrenze)
- Dennoch zuverlässig bei Wind 12+ kn und Amwind-Kursen
- Autopilot-Hydraulik zweimal defekt → Hydrovane als alleinige Steuerung für mehrere Tage
- Notruder-Funktion einmal im Roten Meer genutzt (Hauptruder-Lager blockiert)

**Fazit:**
"Für Amel-Eigner ist die Hydrovane die einzige Option. Sie funktioniert, aber 14,5 Tonnen sind viel für eine Hydrovane. Am Wind bei 15+ kn steuert sie gut, unter 12 kn und auf Raumschots ist der Autopilot besser. Die Kombination aus beidem ist ideal — Hydrovane für den Wind, Autopilot für den Rest."

**AYDI-Analyse:**
- Systemwahl: EINZIGE OPTION (Amel-Steueranlage erzwingt Auxiliary Rudder)
- Leistung: BEFRIEDIGEND (Boot an der Kapazitätsgrenze der Hydrovane)
- Hybrid-Betrieb: EMPFOHLEN (50/50 Aufteilung realistisch bei schwerem Boot)
- Sicherheit: HOCH (Notruder-Funktion praxisvalidiert)

### ANHANG H: Fallstudie — Contest 48CS mit Windpilot Pacific Plus + Monitor MX (Doppelanlage)

**Boot:** Contest 48CS (2010)
**Eigner:** Einhandsegler, 50 Jahre, Professioneller Langfahrtsegler und Journalist
**Route:** Mehrere Weltumsegelungen, gesamt >120.000 sm

**Ausgangslage:**
- Boot: 14,86 m LüA, 4,35 m Breite, 16 t Verdrängung
- Radsteuerung (Jefa, hydraulisch)
- Philosophie: "Maximale Redundanz, keine Kompromisse"

**Einzigartiger Ansatz:**
Dieser Eigner installierte ZWEI Windfahnen-Systeme:
- Windpilot Pacific Plus (Steuerbord) — Primärsystem
- Monitor MX (Backbord) — Backup-Windfahne
- Plus: Raymarine EV-200 Autopilot — dritte Steuerungsebene

**Begründung:**
"Auf einer Weltumsegelung ist die Steuerung lebenskritisch. Ein System kann ausfallen — durch Treibgut, Materialbruch, oder einfach Verschleiß. Zwei verschiedene Systeme verschiedener Hersteller maximieren die Wahrscheinlichkeit, dass immer eines funktioniert. Die Investition von 10.000 € für zwei Windfahnen ist nichts im Vergleich zu den Kosten einer missglückten Weltumsegelung."

**Betriebserfahrungen (120.000+ sm):**
- Windpilot Pacific Plus: 60% Primärsteuerung
- Monitor MX: 10% (wenn Windpilot gewartet/repariert wird, oder als Testvergleich)
- Autopilot: 25%
- Hand: 5%
- Windpilot-Ausfälle über 120.000 sm: 3 (Pendelruder-Verlust, Kegelrad-Bruch, Fahnenschaden)
- Monitor-Ausfälle: 2 (Pendelruder-Blatt, Lagerbuchsen)
- Zu KEINEM Zeitpunkt war der Eigner ohne funktionsfähige Steuerung

**AYDI-Analyse:**
- Konzept: EINZIGARTIG UND KONSEQUENT (maximale Redundanz für Extrem-Langfahrt)
- Kosten: HOCH (ca. 10.000 € für zwei Windfahnen) — aber gerechtfertigt für professionelle Langfahrt
- Gewicht: KRITISCH (ca. 50 kg am Heck — messbare Trimm-Beeinflussung)
- Empfehlung: NUR für professionelle Langfahrtsegler mit >50.000 sm Ambitionen

---

## 12. ANHANG I–R — Pydantic v2 Modelle

### ANHANG I: Basis-Datenmodelle

```python
"""
AYDI Knowledge Module 21.03 — Wind Vane Self-Steering Systems
Pydantic v2 data models for structured analysis.

All models use model_config = {"from_attributes": True} (Pydantic v2).
NEVER use class Config (Pydantic v1 pattern).
"""

from __future__ import annotations

from datetime import date, datetime
from decimal import Decimal
from enum import Enum
from typing import Optional

from pydantic import BaseModel, Field


# ─── Enumerations ────────────────────────────────────────────────

class WindVaneSystemType(str, Enum):
    """Classification of wind vane self-steering system types."""
    SERVO_PENDULUM = "servo_pendulum"
    AUXILIARY_RUDDER = "auxiliary_rudder"
    AUXILIARY_RUDDER_TRIM_TAB = "auxiliary_rudder_trim_tab"
    TRIM_TAB_MAIN_RUDDER = "trim_tab_main_rudder"
    HYBRID = "hybrid"


class VaneAxisType(str, Enum):
    """Axis orientation of the wind vane."""
    HORIZONTAL = "horizontal"  # H-Fahne — higher force
    VERTICAL = "vertical"      # V-Fahne — weather vane type


class MountingType(str, Enum):
    """How the system is mounted to the transom."""
    TRANSOM_CENTER = "transom_center"
    TRANSOM_SIDE = "transom_side"
    PLATFORM = "platform"
    TWIN_TUBES = "twin_tubes"
    CUSTOM = "custom"


class SteeringType(str, Enum):
    """Type of primary steering on the yacht."""
    TILLER = "tiller"
    WHEEL_SINGLE = "wheel_single"
    WHEEL_TWIN = "wheel_twin"
    HYDRAULIC = "hydraulic"


class KeelType(str, Enum):
    """Classification of keel types for course stability assessment."""
    LONG_KEEL = "long_keel"
    FIN_KEEL = "fin_keel"
    FIN_SKEG = "fin_skeg"
    TWIN_KEEL = "twin_keel"
    CENTERBOARD = "centerboard"
    BULB_KEEL = "bulb_keel"


class ConfidenceLevel(str, Enum):
    """AYDI confidence levels for assessments."""
    MEASURED = "measured"
    CALCULATED = "calculated"
    VISUAL_HIGH = "visual_high"
    VISUAL_MEDIUM = "visual_medium"
    VISUAL_LOW = "visual_low"
    VISUAL_INSUFFICIENT = "visual_insufficient"
    ESTIMATED = "estimated"
    BENCHMARK = "benchmark"
    DOCUMENTED = "documented"


class SeverityLevel(str, Enum):
    """Severity classification for defects and findings."""
    CRITICAL = "critical"
    HIGH = "high"
    MEDIUM = "medium"
    LOW = "low"
    INFO = "info"


class PointOfSail(str, Enum):
    """Point of sail / course relative to wind."""
    CLOSE_HAULED = "close_hauled"       # Am Wind
    BEAM_REACH = "beam_reach"           # Halbwind
    BROAD_REACH = "broad_reach"         # Raumschots
    RUNNING = "running"                 # Vorwind
    DEAD_DOWNWIND = "dead_downwind"     # Platt vor dem Wind


class ConditionGrade(str, Enum):
    """Condition grading for used systems."""
    EXCELLENT = "excellent"       # Like new, <5,000 nm
    GOOD = "good"                 # Fully functional, normal wear
    FAIR = "fair"                 # Functional with visible wear
    POOR = "poor"                 # Needs repair/parts
    DEFECTIVE = "defective"       # Non-functional
```

### ANHANG J: System- und Produktmodelle

```python
class WindVaneSystem(BaseModel):
    """Core model for a wind vane self-steering system."""
    model_config = {"from_attributes": True}

    system_id: str = Field(
        ...,
        description="Unique identifier, e.g. 'windpilot_pacific_plus'"
    )
    manufacturer: str = Field(..., description="Manufacturer name")
    model_name: str = Field(..., description="Model name")
    system_type: WindVaneSystemType
    vane_axis: VaneAxisType
    mounting_type: MountingType

    # Physical specifications
    weight_kg: Decimal = Field(..., ge=0, description="Total weight in kg")
    height_above_deck_mm: int = Field(
        ..., ge=0, description="Height above deck level in mm"
    )
    mounting_width_mm: int = Field(
        ..., ge=0, description="Width at mounting points in mm"
    )

    # Performance envelope
    max_displacement_kg: int = Field(
        ..., ge=0, description="Maximum boat displacement in kg"
    )
    max_loa_m: Decimal = Field(
        ..., ge=0, description="Maximum boat LOA in meters"
    )
    min_apparent_wind_kn: Decimal = Field(
        default=Decimal("5.0"),
        description="Minimum apparent wind speed in knots"
    )
    min_boat_speed_kn: Decimal = Field(
        default=Decimal("2.5"),
        description="Minimum boat speed for servo effect in knots"
    )

    # Vane specifications
    vane_area_m2: Decimal = Field(
        ..., ge=0, description="Wind vane area in m²"
    )
    vane_material: str = Field(
        default="aluminium", description="Wind vane material"
    )

    # Servo/rudder specifications
    servo_blade_area_m2: Optional[Decimal] = Field(
        default=None, description="Servo pendulum blade area in m² (servo-pendulum only)"
    )
    aux_rudder_area_m2: Optional[Decimal] = Field(
        default=None, description="Auxiliary rudder area in m² (aux rudder only)"
    )
    has_trim_tab: bool = Field(
        default=False, description="Whether system uses a trim tab"
    )
    has_emergency_rudder: bool = Field(
        default=False, description="Whether system can serve as emergency rudder"
    )

    # Control lines (servo-pendulum only)
    requires_control_lines: bool = Field(
        default=True, description="Whether system needs control lines to main rudder"
    )
    recommended_line_diameter_mm: Optional[int] = Field(
        default=None, description="Recommended control line diameter in mm"
    )
    recommended_line_material: Optional[str] = Field(
        default=None, description="Recommended control line material"
    )

    # Pricing
    price_eur: Optional[Decimal] = Field(
        default=None, description="Base price in EUR (without adapter)"
    )
    adapter_price_eur: Optional[Decimal] = Field(
        default=None, description="Typical adapter price in EUR"
    )
    currency_original: str = Field(
        default="EUR", description="Original pricing currency"
    )

    # Production status
    in_production: bool = Field(default=True)
    production_start_year: Optional[int] = Field(default=None)
    production_end_year: Optional[int] = Field(default=None)


class WindVaneManufacturer(BaseModel):
    """Manufacturer information for wind vane systems."""
    model_config = {"from_attributes": True}

    manufacturer_id: str = Field(
        ..., description="Unique manufacturer ID, e.g. 'windpilot'"
    )
    name: str = Field(..., description="Full company name")
    country: str = Field(..., description="Country of origin")
    founded_year: Optional[int] = Field(default=None)
    website: Optional[str] = Field(default=None)
    email: Optional[str] = Field(default=None)
    speciality: str = Field(
        default="", description="Primary speciality / known for"
    )
    systems_produced: list[str] = Field(
        default_factory=list,
        description="List of system model IDs manufactured"
    )
    estimated_total_installations: Optional[int] = Field(default=None)
    warranty_years_structure: int = Field(default=2)
    warranty_years_moving_parts: int = Field(default=2)
    global_spare_parts: bool = Field(default=False)
    active: bool = Field(default=True)
    aydi_quality_rating: Optional[int] = Field(
        default=None, ge=0, le=100,
        description="AYDI quality score 0-100"
    )
```

### ANHANG K: Installations- und Kompatibilitätsmodelle

```python
class BoatCompatibility(BaseModel):
    """Compatibility assessment for a specific boat + system combination."""
    model_config = {"from_attributes": True}

    boat_model: str = Field(..., description="Boat model name")
    boat_year: Optional[int] = Field(default=None)
    loa_m: Decimal = Field(..., ge=0, description="Length overall in meters")
    beam_m: Decimal = Field(..., ge=0, description="Beam in meters")
    displacement_kg: int = Field(..., ge=0, description="Displacement in kg")
    keel_type: KeelType
    steering_type: SteeringType

    # Transom geometry
    transom_width_mm: Optional[int] = Field(default=None)
    transom_height_mm: Optional[int] = Field(default=None)
    has_swim_platform: bool = Field(default=False)
    platform_modifiable: bool = Field(default=True)

    # Course stability assessment
    course_stability_score: int = Field(
        ..., ge=0, le=100,
        description="Course stability 0-100 (100 = very stable long keel)"
    )
    weather_helm_typical_deg: Decimal = Field(
        default=Decimal("3.0"),
        description="Typical weather helm in degrees"
    )

    # Recommended system
    recommended_system_id: Optional[str] = Field(default=None)
    alternative_system_id: Optional[str] = Field(default=None)
    compatibility_notes: str = Field(default="")

    # Adapter availability
    adapter_available: bool = Field(default=False)
    adapter_part_number: Optional[str] = Field(default=None)

    # Overall compatibility score
    compatibility_score: int = Field(
        ..., ge=0, le=100,
        description="Overall compatibility score 0-100"
    )
    confidence: ConfidenceLevel = Field(default=ConfidenceLevel.ESTIMATED)


class Installation(BaseModel):
    """Record of a wind vane installation on a specific boat."""
    model_config = {"from_attributes": True}

    installation_id: str = Field(
        ..., description="Unique installation ID"
    )
    system_id: str = Field(..., description="Wind vane system ID")
    boat_model: str = Field(..., description="Boat model")
    boat_year: Optional[int] = Field(default=None)
    installation_date: Optional[date] = Field(default=None)

    # Mounting details
    mounting_type: MountingType
    bolt_count: int = Field(default=6, ge=2)
    bolt_size_mm: int = Field(default=10)
    backing_plate_thickness_mm: int = Field(default=6)
    backing_plate_material: str = Field(default="stainless_316l")
    sealant_used: str = Field(default="sikaflex_291i")
    transom_reinforced: bool = Field(default=False)
    reinforcement_method: Optional[str] = Field(default=None)

    # Control line routing (servo-pendulum)
    control_line_total_length_m: Optional[Decimal] = Field(default=None)
    control_line_material: Optional[str] = Field(default=None)
    turning_block_count: Optional[int] = Field(default=None)
    line_tension_kg: Optional[Decimal] = Field(default=None)

    # Installation quality assessment
    professional_install: bool = Field(default=False)
    installer_name: Optional[str] = Field(default=None)
    installation_hours: Optional[Decimal] = Field(default=None)
    total_cost_eur: Optional[Decimal] = Field(default=None)

    # Quality scores
    mounting_quality_score: Optional[int] = Field(
        default=None, ge=0, le=100
    )
    line_routing_quality_score: Optional[int] = Field(
        default=None, ge=0, le=100
    )
    overall_quality_score: Optional[int] = Field(
        default=None, ge=0, le=100
    )
    confidence: ConfidenceLevel = Field(default=ConfidenceLevel.ESTIMATED)
```

### ANHANG L: Performance- und Betriebsmodelle

```python
class PerformanceEnvelope(BaseModel):
    """Performance characteristics at different points of sail."""
    model_config = {"from_attributes": True}

    system_id: str
    boat_model: str
    displacement_kg: int

    # Performance by point of sail
    close_hauled_accuracy_deg: Decimal = Field(
        ..., description="Course accuracy close-hauled in ±degrees"
    )
    beam_reach_accuracy_deg: Decimal = Field(
        ..., description="Course accuracy beam reach in ±degrees"
    )
    broad_reach_accuracy_deg: Decimal = Field(
        ..., description="Course accuracy broad reach in ±degrees"
    )
    running_accuracy_deg: Decimal = Field(
        ..., description="Course accuracy running in ±degrees"
    )

    # Wind range performance
    min_effective_wind_kn: Decimal = Field(
        ..., description="Minimum effective apparent wind in knots"
    )
    optimal_wind_range_low_kn: Decimal = Field(default=Decimal("10"))
    optimal_wind_range_high_kn: Decimal = Field(default=Decimal("30"))
    max_recommended_wind_kn: Decimal = Field(default=Decimal("40"))

    # Speed range
    min_boat_speed_kn: Decimal = Field(default=Decimal("2.5"))
    optimal_speed_range_low_kn: Decimal = Field(default=Decimal("4.0"))
    optimal_speed_range_high_kn: Decimal = Field(default=Decimal("8.0"))

    # Overall ratings (0-100)
    upwind_rating: int = Field(..., ge=0, le=100)
    reaching_rating: int = Field(..., ge=0, le=100)
    downwind_rating: int = Field(..., ge=0, le=100)
    light_wind_rating: int = Field(..., ge=0, le=100)
    heavy_weather_rating: int = Field(..., ge=0, le=100)
    overall_rating: int = Field(..., ge=0, le=100)

    confidence: ConfidenceLevel = Field(default=ConfidenceLevel.ESTIMATED)
    test_conditions: Optional[str] = Field(default=None)
    nautical_miles_basis: Optional[int] = Field(default=None)


class EnergyAnalysis(BaseModel):
    """Energy savings analysis when using wind vane vs autopilot."""
    model_config = {"from_attributes": True}

    boat_model: str
    passage_name: str
    passage_distance_nm: int
    passage_duration_days: int

    # Autopilot consumption (reference)
    autopilot_power_w: Decimal = Field(
        ..., description="Autopilot average power consumption in watts"
    )
    autopilot_hours_per_day: Decimal = Field(
        default=Decimal("20"), description="Typical autopilot hours per day"
    )
    autopilot_daily_consumption_wh: Decimal = Field(
        ..., description="Daily autopilot energy consumption in Wh"
    )

    # Wind vane usage
    wind_vane_usage_percent: Decimal = Field(
        ..., ge=0, le=100,
        description="Percentage of time wind vane steers"
    )
    autopilot_usage_percent: Decimal = Field(
        ..., ge=0, le=100,
        description="Percentage of time autopilot steers"
    )
    manual_steering_percent: Decimal = Field(
        ..., ge=0, le=100,
        description="Percentage of time hand steering"
    )

    # Savings calculation
    daily_energy_saved_wh: Decimal = Field(
        ..., description="Daily energy savings in Wh"
    )
    total_energy_saved_wh: Decimal = Field(
        ..., description="Total energy savings for passage in Wh"
    )
    equivalent_engine_hours: Decimal = Field(
        ..., description="Equivalent engine running hours saved"
    )
    equivalent_fuel_liters: Decimal = Field(
        ..., description="Equivalent fuel saved in liters"
    )

    confidence: ConfidenceLevel = Field(default=ConfidenceLevel.ESTIMATED)
```

### ANHANG M: Fehlerbild- und Diagnosemodelle

```python
class DefectPattern(BaseModel):
    """Standardized defect pattern for wind vane systems."""
    model_config = {"from_attributes": True}

    defect_id: str = Field(
        ..., description="Unique defect ID, e.g. 'F01'"
    )
    title_de: str = Field(
        ..., description="Defect title in German"
    )
    title_en: str = Field(
        ..., description="Defect title in English"
    )
    severity: SeverityLevel
    category: str = Field(
        ..., description="Category, e.g. 'mechanical', 'corrosion', 'control_lines'"
    )
    applicable_systems: list[WindVaneSystemType] = Field(
        default_factory=list,
        description="System types this defect applies to"
    )

    # Symptoms
    symptoms_de: list[str] = Field(
        ..., description="Observable symptoms in German"
    )

    # Causes ranked by probability
    causes: list[DefectCause] = Field(
        ..., description="Possible causes ranked by probability"
    )

    # Diagnosis steps
    diagnosis_steps_de: list[str] = Field(
        ..., description="Step-by-step diagnosis in German"
    )

    # Remediation
    remediation_de: list[str] = Field(
        ..., description="Remediation steps in German"
    )
    prevention_de: list[str] = Field(
        default_factory=list,
        description="Preventive measures in German"
    )

    # Repair cost estimate
    repair_cost_min_eur: Optional[Decimal] = Field(default=None)
    repair_cost_max_eur: Optional[Decimal] = Field(default=None)
    repair_time_hours: Optional[Decimal] = Field(default=None)
    professional_required: bool = Field(default=False)

    confidence: ConfidenceLevel = Field(default=ConfidenceLevel.DOCUMENTED)


class DefectCause(BaseModel):
    """A single cause within a defect pattern."""
    model_config = {"from_attributes": True}

    description_de: str = Field(..., description="Cause description in German")
    probability_percent: int = Field(
        ..., ge=0, le=100,
        description="Probability of this cause being the root cause"
    )
    diagnostic_indicator: Optional[str] = Field(
        default=None,
        description="How to identify this specific cause"
    )


class DefectAssessment(BaseModel):
    """Assessment of a specific defect found during inspection."""
    model_config = {"from_attributes": True}

    assessment_id: str
    installation_id: str
    defect_id: str
    assessed_at: datetime
    assessed_by: str = Field(
        default="aydi_visual",
        description="Assessor: 'aydi_visual', 'aydi_structured', 'manual'"
    )

    # Findings
    severity: SeverityLevel
    description_de: str = Field(
        ..., description="Specific finding description in German"
    )
    location_description: str = Field(
        ..., description="Location of defect on system"
    )

    # Evidence
    photo_ids: list[str] = Field(default_factory=list)
    measurement_data: Optional[dict] = Field(default=None)

    # Recommendation
    recommended_action_de: str = Field(
        ..., description="Recommended action in German"
    )
    urgency_days: Optional[int] = Field(
        default=None,
        description="Days within which action should be taken"
    )

    # Confidence
    confidence: ConfidenceLevel
    ai_model_version: Optional[str] = Field(default=None)
```

### ANHANG N: Wartungs- und Servicemodelle

```python
class MaintenanceSchedule(BaseModel):
    """Maintenance schedule for a wind vane system."""
    model_config = {"from_attributes": True}

    system_id: str
    interval_name: str = Field(
        ..., description="e.g. 'weekly', 'monthly', 'semi_annual', 'annual'"
    )
    interval_days: int = Field(
        ..., description="Interval in days"
    )
    interval_nm: Optional[int] = Field(
        default=None,
        description="Interval in nautical miles (alternative)"
    )
    tasks_de: list[str] = Field(
        ..., description="Maintenance tasks in German"
    )
    tools_required: list[str] = Field(
        default_factory=list,
        description="Tools required"
    )
    parts_required: list[str] = Field(
        default_factory=list,
        description="Parts/consumables required"
    )
    estimated_time_minutes: int = Field(
        ..., ge=0,
        description="Estimated time in minutes"
    )
    skill_level: str = Field(
        default="owner",
        description="Required skill: 'owner', 'experienced', 'professional'"
    )


class MaintenanceRecord(BaseModel):
    """Record of maintenance performed."""
    model_config = {"from_attributes": True}

    record_id: str
    installation_id: str
    performed_at: datetime
    performed_by: str
    maintenance_type: str = Field(
        ..., description="'scheduled', 'corrective', 'preventive'"
    )
    tasks_performed_de: list[str]
    parts_replaced: list[str] = Field(default_factory=list)
    parts_cost_eur: Decimal = Field(default=Decimal("0"))
    labor_cost_eur: Decimal = Field(default=Decimal("0"))
    total_cost_eur: Decimal = Field(default=Decimal("0"))
    nautical_miles_at_service: Optional[int] = Field(default=None)
    notes_de: Optional[str] = Field(default=None)
    next_service_due: Optional[date] = Field(default=None)


class SparePartsKit(BaseModel):
    """Recommended spare parts kit for offshore sailing."""
    model_config = {"from_attributes": True}

    kit_name: str
    system_id: str
    priority: str = Field(
        ..., description="'essential', 'recommended', 'optional'"
    )
    parts: list[SparePart] = Field(default_factory=list)
    total_weight_kg: Decimal = Field(default=Decimal("0"))
    total_cost_eur: Decimal = Field(default=Decimal("0"))


class SparePart(BaseModel):
    """Individual spare part."""
    model_config = {"from_attributes": True}

    part_name_de: str
    part_name_en: str
    part_number: Optional[str] = Field(default=None)
    quantity: int = Field(default=1, ge=1)
    weight_kg: Decimal = Field(default=Decimal("0"))
    price_eur: Decimal = Field(default=Decimal("0"))
    priority: str = Field(
        default="recommended",
        description="'essential', 'recommended', 'optional'"
    )
    shelf_life_years: Optional[int] = Field(default=None)
    universal: bool = Field(
        default=False,
        description="Whether part fits multiple systems/brands"
    )
```

### ANHANG O: Troubleshooting-Entscheidungsbaum-Modelle

```python
class TroubleshootingTree(BaseModel):
    """Structured decision tree for troubleshooting."""
    model_config = {"from_attributes": True}

    tree_id: str = Field(..., description="Unique tree ID, e.g. 'EB-01'")
    title_de: str = Field(..., description="Tree title in German")
    title_en: str = Field(..., description="Tree title in English")
    entry_symptom_de: str = Field(
        ..., description="Entry symptom that triggers this tree"
    )
    applicable_systems: list[WindVaneSystemType] = Field(
        default_factory=list
    )
    root_node: TroubleshootingNode


class TroubleshootingNode(BaseModel):
    """A single node in a troubleshooting decision tree."""
    model_config = {"from_attributes": True}

    node_id: str = Field(..., description="Node identifier within tree")
    question_de: str = Field(
        ..., description="Question or check to perform (German)"
    )
    node_type: str = Field(
        ..., description="'question', 'action', 'diagnosis', 'end'"
    )

    # Branches
    yes_node: Optional[TroubleshootingNode] = Field(default=None)
    no_node: Optional[TroubleshootingNode] = Field(default=None)
    branches: Optional[list[TroubleshootingBranch]] = Field(
        default=None,
        description="Multiple branches for non-binary decisions"
    )

    # Action (for action/diagnosis/end nodes)
    action_de: Optional[str] = Field(
        default=None, description="Action to take (German)"
    )
    severity: Optional[SeverityLevel] = Field(default=None)
    related_defect_id: Optional[str] = Field(default=None)
    confidence: ConfidenceLevel = Field(default=ConfidenceLevel.DOCUMENTED)


class TroubleshootingBranch(BaseModel):
    """A branch option in a multi-choice troubleshooting node."""
    model_config = {"from_attributes": True}

    condition_de: str = Field(
        ..., description="Condition for this branch (German)"
    )
    next_node: TroubleshootingNode

# Rebuild model to resolve forward references
TroubleshootingNode.model_rebuild()
TroubleshootingTree.model_rebuild()
```

### ANHANG P: AYDI-Analyse-Integrationsmodelle

```python
class WindVaneAnalysisResult(BaseModel):
    """Complete analysis result for a wind vane system assessment."""
    model_config = {"from_attributes": True}

    analysis_id: str
    boat_model: str
    analysis_date: datetime
    analysis_level: str = Field(
        ..., description="'level_1_quick' or 'level_2_professional'"
    )

    # System identification
    system_identified: Optional[str] = Field(default=None)
    system_type: Optional[WindVaneSystemType] = Field(default=None)
    manufacturer: Optional[str] = Field(default=None)
    estimated_age_years: Optional[int] = Field(default=None)

    # Condition assessment
    overall_condition: ConditionGrade
    structural_score: int = Field(..., ge=0, le=100)
    mechanical_score: int = Field(..., ge=0, le=100)
    corrosion_score: int = Field(
        ..., ge=0, le=100,
        description="100 = no corrosion, 0 = severe corrosion"
    )
    mounting_score: int = Field(..., ge=0, le=100)
    control_lines_score: Optional[int] = Field(
        default=None, ge=0, le=100,
        description="Only for servo-pendulum systems"
    )

    # Performance estimate
    performance_upwind: Optional[int] = Field(
        default=None, ge=0, le=100
    )
    performance_reaching: Optional[int] = Field(
        default=None, ge=0, le=100
    )
    performance_downwind: Optional[int] = Field(
        default=None, ge=0, le=100
    )

    # Defects found
    defects: list[DefectAssessment] = Field(default_factory=list)

    # Recommendations
    recommendations_de: list[str] = Field(default_factory=list)
    estimated_repair_cost_eur: Optional[Decimal] = Field(default=None)
    replacement_recommended: bool = Field(default=False)
    replacement_system_id: Optional[str] = Field(default=None)

    # Value assessment
    estimated_current_value_eur: Optional[Decimal] = Field(default=None)
    impact_on_boat_value_eur: Optional[Decimal] = Field(
        default=None,
        description="Positive = adds value, negative = detracts"
    )

    # Confidence
    overall_confidence: ConfidenceLevel
    data_sources: list[str] = Field(
        default_factory=list,
        description="e.g. ['visual_inspection', 'owner_report', 'structured_data']"
    )
    ai_model_version: Optional[str] = Field(default=None)


class WindVaneSelectionRecommendation(BaseModel):
    """Recommendation for wind vane system selection for a given boat."""
    model_config = {"from_attributes": True}

    recommendation_id: str
    boat_model: str
    boat_loa_m: Decimal
    boat_displacement_kg: int
    boat_keel_type: KeelType
    boat_steering_type: SteeringType
    intended_use: str = Field(
        ..., description="'coastal', 'offshore', 'bluewater', 'circumnavigation'"
    )
    budget_eur: Optional[Decimal] = Field(default=None)

    # Primary recommendation
    primary_system_id: str
    primary_reason_de: str
    primary_score: int = Field(..., ge=0, le=100)

    # Alternative recommendation
    alternative_system_id: Optional[str] = Field(default=None)
    alternative_reason_de: Optional[str] = Field(default=None)
    alternative_score: Optional[int] = Field(
        default=None, ge=0, le=100
    )

    # Compatibility warnings
    warnings_de: list[str] = Field(default_factory=list)

    # Cost estimate
    estimated_total_cost_eur: Decimal = Field(
        ..., description="System + adapter + installation"
    )
    estimated_annual_maintenance_eur: Decimal = Field(
        default=Decimal("200")
    )

    # Energy savings estimate
    estimated_annual_energy_savings_kwh: Optional[Decimal] = Field(
        default=None
    )

    confidence: ConfidenceLevel = Field(default=ConfidenceLevel.ESTIMATED)
```

### ANHANG Q: Visueller Analyse-Modell

```python
class WindVaneVisualPrompt(BaseModel):
    """Prompt configuration for Claude Vision analysis of wind vane photos."""
    model_config = {"from_attributes": True}

    prompt_id: str = Field(
        ..., description="Unique prompt ID"
    )
    prompt_version: str = Field(default="1.0.0")
    target_analysis: str = Field(
        ..., description="What this prompt analyzes, e.g. 'overall_condition'"
    )

    system_prompt: str = Field(
        ..., description="System prompt for Claude Vision"
    )
    analysis_instructions: str = Field(
        ..., description="Specific analysis instructions"
    )
    output_schema: str = Field(
        ..., description="Expected output JSON schema reference"
    )

    # Calibration
    reference_images: list[str] = Field(
        default_factory=list,
        description="Paths to reference images for calibration"
    )
    scoring_guidelines: dict = Field(
        default_factory=dict,
        description="Score guidelines, e.g. {'excellent': '90-100: ...', ...}"
    )

    applicable_systems: list[WindVaneSystemType] = Field(
        default_factory=list
    )


class WindVaneVisualAssessment(BaseModel):
    """Result of visual analysis of a wind vane system from photos."""
    model_config = {"from_attributes": True}

    assessment_id: str
    photo_ids: list[str] = Field(
        ..., min_length=1,
        description="IDs of photos analyzed"
    )
    system_type_detected: Optional[WindVaneSystemType] = Field(default=None)
    manufacturer_detected: Optional[str] = Field(default=None)
    model_detected: Optional[str] = Field(default=None)

    # Visual scores
    overall_visual_score: int = Field(..., ge=0, le=100)
    corrosion_visual_score: int = Field(
        ..., ge=0, le=100,
        description="100 = no visible corrosion"
    )
    structural_visual_score: int = Field(
        ..., ge=0, le=100,
        description="100 = no visible damage"
    )
    alignment_visual_score: int = Field(
        ..., ge=0, le=100,
        description="100 = perfectly aligned"
    )
    mounting_visual_score: int = Field(
        ..., ge=0, le=100,
        description="100 = professionally mounted"
    )

    # Defects detected visually
    visual_defects: list[str] = Field(
        default_factory=list,
        description="Defect descriptions from visual analysis"
    )
    visual_warnings: list[str] = Field(
        default_factory=list,
        description="Warning observations"
    )

    # Confidence
    overall_confidence: ConfidenceLevel
    photo_quality: str = Field(
        default="medium",
        description="'high', 'medium', 'low', 'insufficient'"
    )
    obstructed_areas: list[str] = Field(
        default_factory=list,
        description="Areas not visible in photos"
    )
    ai_model_version: Optional[str] = Field(default=None)
    analysis_timestamp: datetime
```

### ANHANG R: Aggregations- und Benchmarkmodelle

```python
class WindVaneMarketData(BaseModel):
    """Market data and benchmarks for wind vane systems."""
    model_config = {"from_attributes": True}

    data_date: date
    region: str = Field(
        default="global",
        description="'global', 'europe', 'north_america', 'pacific'"
    )

    # Market size estimates
    estimated_annual_sales_units: Optional[int] = Field(default=None)
    estimated_market_size_eur: Optional[Decimal] = Field(default=None)

    # Price benchmarks
    avg_servo_pendulum_price_eur: Decimal
    avg_auxiliary_rudder_price_eur: Decimal
    avg_installation_cost_eur: Decimal
    avg_annual_maintenance_eur: Decimal

    # Used market
    avg_used_price_fraction: Decimal = Field(
        default=Decimal("0.55"),
        description="Average used price as fraction of new (0-1)"
    )
    used_market_active: bool = Field(default=True)

    # Popularity rankings
    most_popular_servo_pendulum: str = Field(default="monitor_m")
    most_popular_auxiliary: str = Field(default="hydrovane")
    most_popular_overall: str = Field(default="monitor_m")

    # Reliability data
    avg_mtbf_nm: Optional[int] = Field(
        default=None,
        description="Mean distance between failures in nautical miles"
    )
    common_failure_modes: list[str] = Field(default_factory=list)

    confidence: ConfidenceLevel = Field(default=ConfidenceLevel.BENCHMARK)


class SystemLifecycleCost(BaseModel):
    """20-year lifecycle cost analysis for a wind vane system."""
    model_config = {"from_attributes": True}

    system_id: str
    calculation_date: date
    usage_profile: str = Field(
        ..., description="'coastal_weekend', 'coastal_regular', 'bluewater', 'circumnavigation'"
    )
    annual_nautical_miles: int = Field(
        ..., ge=0,
        description="Expected annual usage in nautical miles"
    )

    # Acquisition costs
    system_cost_eur: Decimal
    adapter_cost_eur: Decimal = Field(default=Decimal("0"))
    installation_cost_eur: Decimal = Field(default=Decimal("0"))
    total_acquisition_eur: Decimal

    # Annual costs
    annual_maintenance_eur: Decimal = Field(default=Decimal("200"))
    annual_consumables_eur: Decimal = Field(
        default=Decimal("50"),
        description="Lines, grease, small parts"
    )

    # Replacement schedule (over 20 years)
    control_lines_replacements: int = Field(default=4)
    control_lines_cost_per_set_eur: Decimal = Field(
        default=Decimal("80")
    )
    vane_replacements: int = Field(default=1)
    vane_cost_eur: Decimal = Field(default=Decimal("200"))
    servo_blade_replacements: int = Field(default=2)
    servo_blade_cost_eur: Decimal = Field(default=Decimal("300"))
    bearing_overhauls: int = Field(default=3)
    bearing_overhaul_cost_eur: Decimal = Field(default=Decimal("150"))
    gear_replacements: int = Field(default=1)
    gear_cost_eur: Decimal = Field(default=Decimal("250"))

    # Totals
    total_maintenance_20y_eur: Decimal
    total_replacements_20y_eur: Decimal
    total_lifecycle_cost_20y_eur: Decimal
    annual_average_cost_eur: Decimal

    # Comparison with autopilot
    autopilot_lifecycle_cost_20y_eur: Optional[Decimal] = Field(
        default=None,
        description="Reference: autopilot lifecycle cost over 20 years"
    )
    savings_vs_autopilot_eur: Optional[Decimal] = Field(default=None)

    # Energy savings (bonus)
    total_energy_saved_kwh_20y: Optional[Decimal] = Field(default=None)
    energy_value_eur_20y: Optional[Decimal] = Field(
        default=None,
        description="Value of saved energy (fuel equivalent)"
    )

    confidence: ConfidenceLevel = Field(default=ConfidenceLevel.ESTIMATED)


class AYDIModuleIntegration(BaseModel):
    """Configuration for how wind vane data integrates with AYDI modules."""
    model_config = {"from_attributes": True}

    module_name: str = Field(
        ..., description="AYDI module, e.g. 'ergonomics', 'compliance', 'cost'"
    )
    data_fields_used: list[str] = Field(
        ..., description="Fields from wind vane models used by this module"
    )
    weight_structured: Decimal = Field(
        ..., ge=0, le=1,
        description="Weight of structured data in score fusion"
    )
    weight_visual: Decimal = Field(
        ..., ge=0, le=1,
        description="Weight of visual data in score fusion"
    )
    scoring_criteria_de: list[str] = Field(
        ..., description="Criteria for scoring in this module (German)"
    )
    max_impact_points: int = Field(
        ..., ge=0, le=100,
        description="Maximum score impact of wind vane on module"
    )


# ─── Module integration configuration ────────────────────────────

WIND_VANE_MODULE_INTEGRATIONS = [
    AYDIModuleIntegration(
        module_name="ergonomics",
        data_fields_used=[
            "mounting_type", "height_above_deck_mm",
            "requires_control_lines", "has_swim_platform"
        ],
        weight_structured=Decimal("0.75"),
        weight_visual=Decimal("0.25"),
        scoring_criteria_de=[
            "Zugang zur Badeplattform beeinträchtigt?",
            "Leinenführung im Cockpit behindert Bewegungsfreiheit?",
            "Windfahne blockiert Sichtfeld nach achtern?",
            "Pendelruder-Hochklapp-Mechanismus gut zugänglich?",
        ],
        max_impact_points=15,
    ),
    AYDIModuleIntegration(
        module_name="compliance",
        data_fields_used=[
            "bolt_count", "bolt_size_mm", "backing_plate_thickness_mm",
            "transom_reinforced", "sealant_used"
        ],
        weight_structured=Decimal("0.95"),
        weight_visual=Decimal("0.05"),
        scoring_criteria_de=[
            "Befestigungsbolzen ausreichend dimensioniert?",
            "Backing-Plates vorhanden und korrekt dimensioniert?",
            "Dichtung aller Durchbrüche gewährleistet?",
            "Heckstruktur für zusätzliche Last geeignet?",
        ],
        max_impact_points=10,
    ),
    AYDIModuleIntegration(
        module_name="cost",
        data_fields_used=[
            "total_cost_eur", "annual_maintenance_eur",
            "total_lifecycle_cost_20y_eur",
            "estimated_current_value_eur"
        ],
        weight_structured=Decimal("1.00"),
        weight_visual=Decimal("0.00"),
        scoring_criteria_de=[
            "Anschaffungskosten im Rahmen für Bootsklasse?",
            "Wartungskosten angemessen?",
            "Lifecycle-Kosten vs. Autopilot-Alternative?",
            "Einfluss auf Wiederverkaufswert des Bootes?",
        ],
        max_impact_points=8,
    ),
    AYDIModuleIntegration(
        module_name="structural",
        data_fields_used=[
            "weight_kg", "mounting_type", "bolt_count",
            "transom_reinforced", "backing_plate_thickness_mm"
        ],
        weight_structured=Decimal("0.95"),
        weight_visual=Decimal("0.05"),
        scoring_criteria_de=[
            "Heck-Belastung durch Windfahnengewicht akzeptabel?",
            "Momentenberechnung: Hebelarm × Gewicht innerhalb Grenzwerte?",
            "Laminatstärke am Heckspiegel ausreichend?",
            "Dynamische Lasten bei Seegang berücksichtigt?",
        ],
        max_impact_points=12,
    ),
    AYDIModuleIntegration(
        module_name="materials",
        data_fields_used=[
            "vane_material", "corrosion_score",
            "corrosion_visual_score", "backing_plate_material"
        ],
        weight_structured=Decimal("0.35"),
        weight_visual=Decimal("0.65"),
        scoring_criteria_de=[
            "Materialqualität der Anlage (316L, Marine-Alu)?",
            "Korrosionsschutz vorhanden und intakt?",
            "Kontaktkorrosion zwischen verschiedenen Metallen?",
            "UV-Beständigkeit der Kunststoffteile?",
        ],
        max_impact_points=10,
    ),
    AYDIModuleIntegration(
        module_name="service_patterns",
        data_fields_used=[
            "defects", "maintenance_records",
            "nautical_miles_at_service", "parts_replaced"
        ],
        weight_structured=Decimal("0.65"),
        weight_visual=Decimal("0.35"),
        scoring_criteria_de=[
            "Regelmäßige Wartung dokumentiert?",
            "Bekannte Verschleißmuster erkennbar?",
            "Ersatzteilverfügbarkeit langfristig gesichert?",
            "Typische Lebensdauer-Muster für System und Bootsklasse?",
        ],
        max_impact_points=8,
    ),
]
```

---

## Quellenverzeichnis und Normenreferenz

### Relevante ISO-Normen

| Norm | Titel | Relevanz für Windfahnenanlagen |
|---|---|---|
| ISO 12217 (2015/2022) | Stabilitäts- und Auftriebsbewertung | Gewichtsverteilung am Heck durch Windfahne beeinflusst Stabilität |
| ISO 15085 (2003) | Man-Overboard-Prävention | Windfahnengestell darf Heckkorb nicht schwächen |
| ISO 11812 (2020) | Cockpits — Wasserablauf | Leinenführung darf Cockpit-Drainage nicht behindern |
| ISO 12216 (2020) | Fenster, Bullaugen, Luken | Nicht direkt relevant, aber Rahmenmontage ähnliche Prinzipien |
| ISO 10133/13297 | Elektrische Installationen | Relevant bei Hybrid-Betrieb (Autopilot + Windfahne) |
| ISO 9094 (2015) | Brandschutz | Steuerleinen müssen flammhemmend sein oder geschützt verlegt werden |

### Fachliteratur

| Autor | Titel | Verlag/Jahr | Relevanz |
|---|---|---|---|
| Peter Matthiesen | "Windsteuerung für Segelyachten" | Delius Klasing, mehrere Auflagen | Standardwerk — Konstruktion, Dimensionierung, Montage |
| Peter Matthiesen | "Self-Steering for Sailing Craft" | International Marine, 2006 | Englische Ausgabe des Standardwerks |
| John Letcher | "Self-Steering for Sailing Craft" | International Marine, 1974 | Historisches Grundlagenwerk — Theorie und frühe Konstruktionen |
| Bill Belcher | "Wind-Vane Self-Steering" | Adlard Coles, 2003 | Praxisorientierter Ratgeber — Auswahl, Montage, Betrieb |
| Hal Roth | "After 50,000 Miles" | Norton, 1977 | Langfahrt-Erfahrungsbericht mit Windfahnen-Kapiteln |
| Lin & Larry Pardey | "Self Sufficient Sailor" | Pardey Books, 1982/2010 | Langfahrt-Philosophie inkl. Windsteuerung |

### Technische Referenzdokumente

| Dokument | Herausgeber | Inhalt |
|---|---|---|
| Windpilot Montageanleitungen | Windpilot Hamburg | Bootsspezifische Montagedetails für >3.000 Bootstypen |
| Monitor Installation Manual | Scanmar International | Allgemeine und bootsspezifische Montageanleitungen |
| Hydrovane Owner's Manual | Hydrovane Marine | Montage, Betrieb, Wartung des Hydrovane-Systems |
| Cape Horn Installation Guide | Cape Horn Marine | Montage und Einstellung Cape Horn Windvane |

### Online-Ressourcen

| Ressource | URL | Inhalt |
|---|---|---|
| Windpilot Wissensdatenbank | windpilot.com | Umfangreiche Fachinformationen, Bootstypen-Datenbank |
| Scanmar International | selfsteer.com | Monitor-Produktinfo, Ersatzteile, Anleitungen |
| Hydrovane Marine | hydrovane.com | Produktinfo, Installationsfotos, Erfahrungsberichte |
| Cruisers Forum — Self-Steering | cruisersforum.com | Größtes Langfahrt-Forum, umfangreiche Diskussionen |
| Sailing Anarchy — Gear | sailinganarchy.com | Technische Diskussionen, Vergleichstests |
| World Cruising Club | worldcruising.com | ARC-Statistiken zu Windfahnen-Nutzung auf Atlantiküberquerungen |

---

### Änderungshistorie

| Version | Datum | Änderung | Autor |
|---|---|---|---|
| 1.0.0 | 2026-05-02 | Erstversion — vollständige Wissensreferenz | AYDI Research |

---

*Ende der Wissensdatei 21.03 — Windfahnen-Selbststeueranlagen*

*AYDI Research | Version 1.0.0 | 2026-05-02*
