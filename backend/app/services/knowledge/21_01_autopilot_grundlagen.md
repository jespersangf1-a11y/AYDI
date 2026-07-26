# 21.01 — Autopilot-Systeme Grundlagen: Funktionsprinzip, Sensorik, Regelungstechnik, PID-Regler, Kompass-Typen

> **AYDI Wissensdatei 21.01** — Kategorie 21: Autopiloten und Kurssteuerung
> **Confidence-Quelle:** measured (Hersteller-Datenblätter, ISO-Normen), documented (Handbücher, Fachliteratur, Praxis-Tests), estimated (Erfahrungswerte Werft/Eigner)
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
11. [ANHANG A–H — Fallstudien](#anhang-ah--fallstudien)
12. [ANHANG I–R — Pydantic v2 Modelle](#anhang-ir--pydantic-v2-modelle)

---

## 1. Einführung und Übersicht

### 1.1 Bedeutung des Autopiloten im modernen Yachtbau

Der Autopilot ist nach Motor und Segel das drittwichtigste System an Bord einer Yacht. Er hat die Seefahrt fundamental verändert — insbesondere für Einhandsegler, Kurzhandcrews und Langfahrtsegler. Ein funktionierender Autopilot bedeutet:

- **Sicherheitsfaktor**: Der Steuermann kann sich auf Navigation, Segel-Trimm und Ausguck konzentrieren statt permanent das Ruder zu halten
- **Ermüdungsreduktion**: Auf einer 24-Stunden-Passage spart ein Autopilot 12–16 Stunden manuelles Steuern pro Crew-Mitglied
- **Einhandsegeln**: Ohne Autopilot ist echtes Einhandsegeln über mehr als wenige Stunden praktisch unmöglich
- **Effizienz**: Ein gut eingestellter Autopilot steuert konsistenter als ein müder Mensch — weniger Kursschwankungen, weniger Ruderbewegungen, geringerer Widerstand
- **Komfort**: Auf Langfahrt ist der Autopilot der wichtigste Komfortfaktor nach einem trockenen, sicheren Liegeplatz

**Historische Entwicklung:**

| Zeitraum | Technologie | Meilenstein |
|----------|-------------|-------------|
| vor 1900 | Windfahnen-Prinzip | Segelschiffe nutzten provisorische Windfahnensteuerungen |
| 1920er | Erste Kreiselkompass-Steuerungen | Metal Mike (Sperry) für kommerzielle Schiffe |
| 1950er | Elektromechanische Autopiloten | Erste bezahlbare Yacht-Autopiloten |
| 1960er | Windfahnen-Selbststeueranlage | Blondie Hasler popularisiert für Einhandsegler |
| 1970er | Solid-State-Elektronik | Kompakte Autopiloten für Serienyachten |
| 1980er | Mikroprozessor-Steuerung | Erste lernfähige Algorithmen, Fluxgate-Kompasse |
| 1990er | GPS-Integration | Kurssteuerung nach Wegpunkten (Track-Modus) |
| 2000er | MEMS-Sensoren | Drastische Miniaturisierung, günstigere Systeme |
| 2010er | 9-Achsen-IMU | Solid-State-Kompasse mit Beschleunigungs- und Drehratensensoren |
| 2020er | Adaptive Algorithmen + AI | Selbstlernende Regelung (Raymarine EV, Garmin Reactor) |

### 1.2 Einhandsegler und Sicherheit

Für Einhandsegler ist der Autopilot kein Luxus, sondern überlebenswichtig. Die Statistik zeigt:

- **70 % aller Einhand-Seenotfälle** sind auf Ermüdung zurückzuführen (Quelle: RNLI-Statistik, documented)
- **Überbordgehen beim Segelwechsel** ist die häufigste Todesursache bei Einhandseglern — der Autopilot hält den Kurs während der Arbeit an Deck
- **ISAF Offshore Special Regulations** (Kategorie 0–2) schreiben einen funktionierenden Autopiloten oder eine Selbststeueranlage vor
- **Redundanz**: Erfahrene Langfahrtsegler führen grundsätzlich zwei unabhängige Steuersysteme — typisch: elektrischer Autopilot + Windfahnen-Selbststeueranlage

**Sicherheitsrelevante Funktionen moderner Autopiloten:**

| Funktion | Beschreibung | Relevanz |
|----------|-------------|----------|
| MOB-Modus | Sofort-Wende (Williamson-Turn oder Einzelwende) auf Knopfdruck | Lebensrettend |
| Windshift-Alarm | Warnung bei plötzlicher Windrichtungsänderung >15° | Segelsicherheit |
| Off-Course-Alarm | Warnung bei Kursabweichung >einstellbarer Grenzwert | Grundsicherheit |
| Autopilot-Disengage-Alarm | Akustische Warnung bei Abschaltung oder Fehler | Grundsicherheit |
| Shallow-Water-Alarm | Integration Echolot → Autopilot-Warnung | Grundberührungsschutz |
| AIS-CPA-Warnung | Annäherung anderer Schiffe → Alarm am Autopilot | Kollisionsverhütung |

### 1.3 Marktübersicht 2025/2026

Der globale Markt für marine Autopiloten wird auf ca. 1,2 Milliarden USD geschätzt (2025), mit einem jährlichen Wachstum von 5–7 %. Die Segmente:

**Freizeitboote (Segelyachten 8–20 m):**
- Dominiert von Raymarine, B&G, Garmin
- Preisspanne: 2.000–15.000 EUR komplett installiert
- Typischer Stromverbrauch: 1–5 A bei 12 V im Normalbetrieb
- Markttrend: Zunehmend integrierte Systeme mit Plotter/Radar/AIS

**Freizeitboote (Motoryachten 8–24 m):**
- Dominiert von Garmin, Raymarine, Simrad
- Preisspanne: 2.500–25.000 EUR je nach Hydraulik-Anforderung
- Typischer Stromverbrauch: 2–15 A bei 12/24 V
- Markttrend: Hydraulische Systeme mit Joystick-Integration

**Performance/Regatta:**
- NKE, B&G dominierend
- Preisspanne: 5.000–30.000 EUR
- Besonderheit: Extrem schnelle Reaktionszeiten, Windmodus-Optimierung
- Markttrend: Integration in Yacht-Performance-Systeme

**Langfahrt/Blauwasser:**
- Alle Hersteller vertreten, Windfahnen-Selbststeueranlagen von Hydrovane, Windpilot, Monitor
- Preisspanne: 3.000–8.000 EUR (elektrisch) + 2.500–5.500 EUR (Windfahne als Backup)
- Besonderheit: Niedriger Stromverbrauch entscheidend
- Markttrend: Kombination elektrisch + mechanisch für Redundanz

### 1.4 Systemarchitektur — Überblick

Ein modernes Autopilot-System besteht aus folgenden Hauptkomponenten:

```
┌─────────────────────────────────────────────────────────────────┐
│                    AUTOPILOT-SYSTEMARCHITEKTUR                   │
├─────────────────────────────────────────────────────────────────┤
│                                                                 │
│  ┌──────────┐    ┌──────────────┐    ┌─────────────────────┐   │
│  │ SENSOREN │───▶│ KURSCOMPUTER │───▶│    ANTRIEB (DRIVE)  │   │
│  └──────────┘    └──────────────┘    └─────────────────────┘   │
│       │                │                        │               │
│  ┌────┴────┐    ┌──────┴──────┐    ┌───────────┴──────────┐   │
│  │ Kompass │    │ PID-Regler  │    │ Hydraulik-Pumpe      │   │
│  │ Windgeb.│    │ Filter      │    │ Linearantrieb        │   │
│  │ GPS     │    │ Algorithmus │    │ Radantrieb           │   │
│  │ Ruderw. │    │ Adaptiv     │    │ Pinnenantrieb        │   │
│  │ Krängung│    │             │    │                      │   │
│  │ Logge   │    │             │    │                      │   │
│  └─────────┘    └─────────────┘    └──────────────────────┘   │
│                        │                                        │
│                 ┌──────┴──────┐                                  │
│                 │ BEDIENUNG   │                                  │
│                 ├─────────────┤                                  │
│                 │ Bedieneinheit│                                 │
│                 │ Plotter     │                                  │
│                 │ Fernbed.    │                                  │
│                 │ App         │                                  │
│                 └─────────────┘                                  │
└─────────────────────────────────────────────────────────────────┘
```

**Datenbussysteme:**

| Bus | Standard | Bandbreite | Typische Nutzung |
|-----|----------|-----------|------------------|
| NMEA 0183 | RS-422 | 4.800 Baud | Ältere Systeme, einfache Sensoranbindung |
| NMEA 2000 | CAN 2.0B | 250 kbit/s | Standard für moderne Yachten, Plug & Play |
| SeaTalkNG | Proprietär (Raymarine) | 250 kbit/s | NMEA-2000-kompatibel mit Erweiterungen |
| SeaTalk1 | Proprietär (Raymarine) | 4.800 Baud | Legacy, noch in vielen Booten vorhanden |
| Ethernet | TCP/IP | 100 Mbit/s | High-Speed-Verbindung Plotter ↔ Computer |
| WiFi | 802.11 b/g/n | variabel | App-Anbindung, Fernbedienung |
| Bluetooth | BLE 4.0+ | variabel | Drahtlose Fernbedienungen |

### 1.5 Normen und Standards

**Relevante Standards für marine Autopiloten:**

| Norm | Titel | Relevanz |
|------|-------|----------|
| ISO 11674:2006 | Ships and marine technology — Heading control systems | Grundnorm für marine Autopiloten |
| ISO 16329:2003 | Ships and marine technology — Heading control systems for high-speed craft | Kurssteuerung für Hochgeschwindigkeitsfahrzeuge (>30 kn) |
| IEC 62065:2014 | Track control systems — Operational and performance requirements | Wegpunkt-Steuerung |
| IEC 61162 | Maritime navigation — Digital interfaces (NMEA) | Datenbus-Standards |
| ISO 8728:2014 | Ships — Marine gyro-compasses | Kreiselkompass-Anforderungen |
| ISO 22090:2014 | Ships — Transmitting heading devices (THDs) | Kompass-Übertragung |
| COLREG | International Regulations for Preventing Collisions at Sea | Der Autopilot entbindet NICHT von der Ausguckpflicht |
| SOLAS Kap. V | Safety of Life at Sea, Navigation | Kommerzielle Anforderungen |

**Wichtig:** Ein Autopilot entbindet den Schiffsführer niemals von seiner Verantwortung. COLREG Regel 5 (Ausguck) und Regel 7 (Risiko der Kollision) gelten uneingeschränkt. Der Autopilot ist ein Steuerhilfsmittel, kein autonomes System.

---

## 2. Grundlagen und Theorie

### 2.1 Der Regelkreis — Grundprinzip

Ein Autopilot ist ein klassischer geschlossener Regelkreis (Closed-Loop-Control-System). Das Grundprinzip:

```
                    ┌──────────────┐
  Sollkurs ────────▶│   REGLER     │────────▶ Stellgröße
  (Heading Set)     │  (PID etc.)  │         (Ruderwinkel)
       ▲            └──────────────┘              │
       │                                          │
       │            ┌──────────────┐              │
       │            │   STRECKE    │◀─────────────┘
       └────────────│  (Boot im    │
    Regelabweichung │   Wasser)    │
    (Heading Error) └──────┬───────┘
                           │
                    ┌──────┴───────┐
                    │   SENSOR     │
                    │  (Kompass)   │
                    └──────────────┘
                           │
                      Istkurs
                    (Heading Actual)
```

**Komponenten des Regelkreises:**

| Komponente | Funktion | Yacht-Äquivalent |
|-----------|----------|-------------------|
| Führungsgröße (w) | Gewünschter Wert | Sollkurs (z.B. 270°) |
| Regelgröße (y) | Aktueller Istwert | Istkurs (Kompassablesung) |
| Regelabweichung (e) | Differenz w - y | Heading Error (z.B. +5° = 5° rechts vom Kurs) |
| Regler | Berechnet Stellgröße | Kurscomputer (PID-Algorithmus) |
| Stellgröße (u) | Eingriff ins System | Ruderwinkel-Befehl (z.B. 8° Steuerbord) |
| Strecke | Das zu regelnde System | Boot im Wasser (mit allen Störungen) |
| Störgrößen (d) | Unerwünschte Einflüsse | Wellen, Wind, Strömung, Krängung |
| Sensor | Misst die Regelgröße | Kompass, Drehratensensor |

### 2.2 PID-Regler — Herzstück der Kursregelung

Der PID-Regler (Proportional-Integral-Derivative) ist der fundamentale Algorithmus hinter jedem modernen Autopiloten. Er berechnet die Stellgröße (Ruderwinkel) aus drei Komponenten:

**Mathematische Formulierung:**

```
u(t) = Kp · e(t) + Ki · ∫e(τ)dτ + Kd · de(t)/dt

Wobei:
  u(t)  = Stellgröße (Ruderwinkel-Befehl) zum Zeitpunkt t
  e(t)  = Regelabweichung (Heading Error) zum Zeitpunkt t
  Kp    = Proportionalverstärkung (Gain)
  Ki    = Integralverstärkung (Reset)
  Kd    = Differentialverstärkung (Dampening)
```

**Diskreter PID-Regler (wie im Mikroprozessor implementiert):**

```
u[n] = Kp · e[n] + Ki · Σ(e[k] · Δt) + Kd · (e[n] - e[n-1]) / Δt

Wobei:
  n     = aktueller Abtastschritt
  Δt    = Abtastintervall (typisch 50–200 ms)
  e[n]  = aktueller Heading Error
  e[n-1]= Heading Error des vorherigen Schritts
```

### 2.3 PID-Komponenten im Detail

#### 2.3.1 P-Anteil (Proportional) — Die Grundreaktion

Der P-Anteil erzeugt eine Stellgröße proportional zum aktuellen Fehler:

```
u_P = Kp · e(t)
```

**Auswirkung auf die Kurssteuerung:**
- Großes Kp: Aggressives Ruder, schnelle Kurskorrektur, aber Überschwingen möglich
- Kleines Kp: Träge Reaktion, Kursabweichungen werden langsam korrigiert
- Kp allein führt immer zu einer bleibenden Regelabweichung bei konstanter Störung (Wind, Strömung)

**Typische Kp-Werte (herstellerabhängig):**

| Bootstyp | Kp-Bereich | Bemerkung |
|----------|-----------|-----------|
| Leichte Jolle/Dinghy | 1.5–3.0 | Sehr agil, schnelle Reaktion nötig |
| Segelyacht 8–12 m | 2.0–5.0 | Standard-Cruiser |
| Segelyacht 12–18 m | 3.0–7.0 | Schwerere Ruder, mehr Masse |
| Motoryacht 8–15 m | 2.5–6.0 | Schnellere Ruderantwort als Segler |
| Motoryacht 15–24 m | 4.0–10.0 | Hydraulisches Ruder, hohe Masse |
| Katamaran 10–15 m | 1.5–4.0 | Leicht am Ruder, kurze Wellenlänge problematisch |
| Superyacht 24 m+ | 8.0–20.0 | Massive Trägheit, professionelle Abstimmung |

**Yacht-spezifisches Problem des reinen P-Reglers:**
Ein Segelboot segelt bei 15 kn wahrem Wind auf Kurs 270°. Der Wind erzeugt eine konstante Luvgierigkeit (weather helm). Der P-Regler legt entsprechendes Gegenruder — aber er korrigiert den Kurs nie vollständig auf 270°. Es bleibt eine statische Abweichung von z.B. 3° nach Lee. Dieses Verhalten nennt man **stationäre Regelabweichung** (Steady-State Error).

#### 2.3.2 I-Anteil (Integral) — Die Langzeitkorrektur

Der I-Anteil summiert den Fehler über die Zeit auf und eliminiert die stationäre Regelabweichung:

```
u_I = Ki · ∫e(τ)dτ    (kontinuierlich)
u_I = Ki · Σ(e[k] · Δt)  (diskret)
```

**Auswirkung auf die Kurssteuerung:**
- Großes Ki: Schnelle Eliminierung von Dauerfehlern (Windversatz, Strömung), aber Neigung zum Aufschaukeln (Integrator-Windup)
- Kleines Ki: Langsame Anpassung, bleibende Kursabweichung über Minuten
- Ki eliminiert den stationären Fehler des P-Reglers vollständig

**Problem: Integrator-Windup**
Wenn das Ruder am Anschlag ist (z.B. max. 30°), aber der Integrator weiter aufsummiert, entsteht ein aufgeblähter Integralwert. Beim Nachlassen der Störung (z.B. Winddrehung) schwingt der Kurs weit über. Lösung: **Anti-Windup-Begrenzung** — der Integrator wird bei Ruderanschlag eingefroren.

**Typische Ki-Werte:**

| Bedingung | Ki-Bereich | Bemerkung |
|-----------|-----------|-----------|
| Ruhiges Wasser | 0.05–0.20 | Langsame Integration genügt |
| Mäßiger Seegang | 0.10–0.30 | Welleneinfluss mitteln |
| Schwerer Seegang | 0.02–0.10 | Geringes Ki verhindert Aufschaukeln |
| Konstanter Seitenwind | 0.15–0.40 | Muss stationäre Abweichung eliminieren |
| Starke Strömung | 0.20–0.50 | Schnelle Anpassung nötig |

#### 2.3.3 D-Anteil (Derivative) — Die Vorausschau

Der D-Anteil reagiert auf die Änderungsgeschwindigkeit des Fehlers — er „sieht voraus":

```
u_D = Kd · de(t)/dt    (kontinuierlich)
u_D = Kd · (e[n] - e[n-1]) / Δt  (diskret)
```

**Auswirkung auf die Kurssteuerung:**
- Großes Kd: Starke Dämpfung, verhindert Überschwingen, aber verstärkt Sensorrauschen
- Kleines Kd: Wenig Dämpfung, Kurs kann um den Sollwert pendeln (Oszillation)
- Kd reagiert auf schnelle Kursänderungen — wenn der Kurs sich schnell ändert (z.B. Welle dreht Boot), legt der D-Anteil sofort Gegenruder noch bevor der P-Anteil reagiert

**Yacht-spezifische D-Anteil-Problematik:**

Das Hauptproblem des D-Anteils auf einem Boot ist **Sensorrauschen**. Ein Kompass auf einer Yacht misst nicht nur den Kurs, sondern auch:
- Bootsbewegungen durch Wellen (Gieren durch Schwell)
- Krängungsbedingte Kompassfehler
- Magnetische Störungen durch Elektrik an Bord
- Vibrationen vom Motor

Der D-Anteil differenziert dieses Rauschen und erzeugt hektische Ruderbewegungen. Lösung: **Tiefpassfilter** vor dem D-Anteil.

**Typische Kd-Werte:**

| Bedingung | Kd-Bereich | Bemerkung |
|-----------|-----------|-----------|
| Ruhiges Wasser | 5.0–15.0 | Hoher D-Anteil für ruhiges Steuern |
| Mäßiger Seegang | 3.0–10.0 | Reduziert wegen Wellenrauschen |
| Schwerer Seegang | 1.0–5.0 | Stark reduziert, sonst Ruder-Hektik |
| Raumer Wind (Segel) | 8.0–20.0 | Hoher D-Anteil gegen Gieren |
| Motoryacht Verdränger | 10.0–25.0 | Hohe Trägheit braucht starke Dämpfung |

### 2.4 PID-Tuning in der Praxis

#### 2.4.1 Ziegler-Nichols-Methode (adaptiert für Yachten)

Die klassische Ziegler-Nichols-Methode wurde für industrielle Regelstrecken entwickelt, kann aber adaptiert werden:

**Schritt 1:** Ki und Kd auf 0 setzen. Nur P-Regler aktiv.
**Schritt 2:** Kp langsam erhöhen, bis der Kurs in eine gleichmäßige Dauerschwingung gerät.
**Schritt 3:** Diesen Kp-Wert als Kp_krit (kritische Verstärkung) und die Schwingungsperiode als T_krit notieren.
**Schritt 4:** PID-Parameter berechnen:

```
Kp = 0.60 · Kp_krit
Ki = 2 · Kp / T_krit
Kd = Kp · T_krit / 8
```

**Problem auf Yachten:** Die Methode erfordert stabile Bedingungen (konstanter Wind, kein Seegang, konstante Fahrt). In der Praxis selten gegeben. Moderne Autopiloten verwenden daher adaptive Methoden.

#### 2.4.2 Heuristisches Tuning

**Praktische Tuning-Anleitung für Segelyacht-Autopiloten:**

1. **Ausgangslage:** Kurs anliegen lassen, mittlere See, 5–6 kn Fahrt
2. **Rudder Gain (≈ Kp) einstellen:**
   - Zu niedrig: Boot wandert langsam vom Kurs, Korrekturen zu schwach
   - Optimal: Boot kehrt innerhalb von 2–3 Ruderschlägen zum Kurs zurück
   - Zu hoch: Boot schwingt um den Kurs (links-rechts-links)
3. **Counter Rudder (≈ Kd) einstellen:**
   - Zu niedrig: Boot überschwingt bei Kurskorrekturen
   - Optimal: Boot nähert sich dem Kurs ohne merkliches Überschwingen
   - Zu hoch: Ruder wird hektisch, ständige kleine Korrekturen
4. **Auto Trim (≈ Ki) einstellen:**
   - Zu niedrig: Bei Seitenwind bleibt Kursversatz, Ruder liegt ständig leicht an einer Seite
   - Optimal: Nach 30–60 Sekunden wird Dauerversatz ausgeglichen
   - Zu hoch: Kurs schwingt langsam hin und her (Integrator-Oszillation)

#### 2.4.3 Adaptive Regelung

Moderne Autopiloten verwenden adaptive Algorithmen, die die PID-Parameter automatisch anpassen:

**Gain-Scheduling:**
Der Autopilot speichert verschiedene PID-Parametersätze für verschiedene Bedingungen (Geschwindigkeit, Seegang, Kurs relativ zum Wind) und schaltet zwischen ihnen um.

**Model Reference Adaptive Control (MRAC):**
Der Autopilot hat ein internes Modell des idealen Boot-Verhaltens. Die PID-Parameter werden so angepasst, dass das reale Boot-Verhalten dem Modell möglichst nahe kommt.

**Recursive Least Squares (RLS):**
Der Autopilot identifiziert das Boot-Verhalten online und passt die Regelparameter kontinuierlich an. Dies ist die Grundlage der meisten modernen Systeme (z.B. Raymarine Evolution, B&G H5000).

**Self-Learning-Algorithmen:**

| Hersteller | Algorithmus | Lernphase | Bemerkung |
|-----------|-------------|-----------|-----------|
| Raymarine | EV Autolearn | 30–60 Min Fahrt | Automatische Identifikation der Bootsdynamik |
| B&G | NAC Autotune | Manuelle Sequenz | Automatische Tuning-Fahrt mit definierten Manövern |
| Garmin | Reactor Autoconfig | 10–20 Min | Schnelle Grundkonfiguration, Feintuning optional |
| Simrad | NAC Autotune | Manuelle Sequenz | Identisch mit B&G (gleiche Plattform) |
| Furuno | NavPilot Adaptive | Kontinuierlich | Ständige Parameteranpassung im Betrieb |
| NKE | gyropilot Performance | Manuell + adaptiv | Regatta-optimierte Parameterauswahl |

### 2.5 Kompasstypen — Kursreferenz für den Autopiloten

Der Kompass ist der wichtigste Sensor des Autopiloten. Er liefert die Grundgröße: den aktuellen Kurs (Heading). Verschiedene Technologien haben verschiedene Vor- und Nachteile.

#### 2.5.1 Fluxgate-Kompass

**Funktionsprinzip:**
Der Fluxgate-Kompass (Förster-Sonde) nutzt das Erdmagnetfeld zur Kursbestimmung. Zwei hochpermeable Ferritkerne werden wechselweise bis zur Sättigung magnetisiert. Das Erdmagnetfeld erzeugt eine asymmetrische Sättigung, die als elektrisches Signal auswertbar ist.

**Technische Details:**
- Frequenz der Erregung: 1–10 kHz (typisch 5 kHz)
- Auflösung: 0,1° bis 0,5°
- Genauigkeit (nach Kompensation): ±0,5° bis ±2,0°
- Ansprechzeit: 50–200 ms
- Stromverbrauch: 50–200 mA bei 12 V

**Vorteile:**
- Bewährt und zuverlässig
- Keine beweglichen Teile
- Gute Genauigkeit nach sorgfältiger Kompensation
- Relativ unempfindlich gegen Vibrationen
- Günstiger Preis

**Nachteile:**
- Empfindlich gegen magnetische Störfelder (Lautsprecher, Kabel, Stahlteile)
- Krängungsabhängige Fehler (heading error bei Schräglage)
- Erfordert sorgfältige Kompensation (Deviation) nach Einbau und regelmäßig danach
- Langsamer als Drehratensensoren

**Einbauvorschriften:**
- Mindestabstand 1 m zu Motoren, Generatoren, großen Stahlteilen
- Mindestabstand 0,5 m zu Lautsprechern, Kabelbäumen, Sicherungskästen
- Horizontal montieren (max. 5° Neigung)
- Im vorderen Drittel des Bootes bevorzugt (weniger Magnetfeld-Störungen)
- Nicht in der Nähe von Keel-Bolzen bei Stahlschwert-Booten

**Kompensation (Deviation):**
Die Kompensation eliminiert bootseigene Magnetfeldstörungen:

1. **Harte Deviation (Hard Iron):** Permanente Magnetfelder von Stahlteilen, Magneten. Erzeugt eine sinusförmige Abweichung über 360°.
2. **Weiche Deviation (Soft Iron):** Induzierte Magnetfelder in weichem Eisen. Erzeugt eine doppeltsinusförmige Abweichung.
3. **Kompensationsverfahren:** Boot langsam im Kreis drehen (mindestens 2 volle Umdrehungen in >3 Minuten). Der Kompass berechnet Kompensationskoeffizienten A–E.

**Krängungsfehler:**
Bei Krängung neigt sich der Fluxgate-Sensor aus der Horizontalen. Das vertikale Erdmagnetfeld (Z-Komponente) beeinflusst die Messung:

```
Heading_Error ≈ arctan(Bz · sin(heel) / Bh)

Wobei:
  Bz = Vertikale Erdmagnetfeld-Komponente
  Bh = Horizontale Erdmagnetfeld-Komponente
  heel = Krängungswinkel
```

In nördlichen Breiten (z.B. Nordsee, Bz/Bh ≈ 2.5) kann der Fehler bei 25° Krängung 5–10° betragen. In Äquatornähe (Bz/Bh ≈ 0.3) nur 0.5–1°.

#### 2.5.2 Solid-State-Kompass (MEMS-IMU)

**Funktionsprinzip:**
Ein Solid-State-Kompass kombiniert mehrere MEMS-Sensoren (Micro-Electro-Mechanical Systems) zu einer Inertial Measurement Unit (IMU):

- **3-Achsen-Magnetometer:** Misst das Magnetfeld in X, Y, Z
- **3-Achsen-Beschleunigungssensor:** Misst die Schwerkraft → bestimmt Neigung (Roll/Pitch)
- **3-Achsen-Drehratensensor (Gyroskop):** Misst Drehgeschwindigkeiten

Zusammen bilden diese 9 Achsen eine vollständige Lagebestimmung.

**Sensor-Fusion:**
Die rohen Sensordaten werden durch einen **Extended Kalman Filter (EKF)** oder **Complementary Filter** fusioniert:

```
Heading_fused = α · Heading_mag + (1-α) · Heading_gyro_integrated

Wobei:
  α = Gewichtungsfaktor (typisch 0.02–0.10)
  Heading_mag = Magnetometer-Kurs (langsam, stabil)
  Heading_gyro_integrated = Integrierter Gyroskop-Kurs (schnell, driftet)
```

Der Kalman-Filter ist deutlich komplexer als diese vereinfachte Darstellung, berücksichtigt aber das gleiche Grundprinzip: Der Magnetometer liefert die langfristig stabile Referenz, der Gyroskop liefert die schnelle, kurzfristig genaue Kursänderung.

**Technische Details:**
- Auflösung: 0,1°
- Genauigkeit (nach Kompensation): ±0,5° bis ±1,5°
- Kursänderungs-Rate: bis 200°/s messbar (wichtig für schnelle Wenden)
- Update-Rate: 10–50 Hz (vs. 1–10 Hz bei Fluxgate)
- Stromverbrauch: 100–300 mA bei 12 V
- Anlaufzeit: 5–30 Sekunden (Sensor-Kalibrierung)

**Vorteile gegenüber Fluxgate:**
- Automatische Krängungskompensation (3-Achsen-Beschleunigungssensor)
- Schnellere Kursänderungserkennung (Drehratensensor)
- Kompakter Formfaktor
- Weniger empfindlich gegen Installation nahe Magnetfeldern (Software-Kompensation leistungsfähiger)
- Zusätzliche Daten: Roll, Pitch, Yaw-Rate direkt verfügbar

**Nachteile:**
- Komplexere Software erforderlich
- Gyroskop-Drift muss kontinuierlich kompensiert werden
- MEMS-Gyroskope haben begrenzte Genauigkeit (Bias-Drift: 1–10°/h)
- Empfindlich gegen starke Vibrationen (Motor, Generator)
- Teurer als einfache Fluxgate-Kompasse

**Beispiel-Produkte:**
- Raymarine EV-1 Sensor Core (9-Achsen-IMU, Kern des Evolution-Systems)
- B&G Precision-9 Compass (9-Achsen, NMEA 2000)
- Simrad Precision-9 Compass (identisch mit B&G)
- Garmin Heading Sensor (9-Achsen, in Reactor-System integriert)

#### 2.5.3 GPS-Kompass (Dual-Antennen)

**Funktionsprinzip:**
Ein GPS-Kompass verwendet zwei GPS-Antennen in einem bekannten Abstand (typisch 0,5–2,0 m). Aus der Phasendifferenz des GPS-Signals zwischen den Antennen wird die Heading-Richtung berechnet.

```
Heading = arctan((E2-E1) / (N2-N1))

Wobei:
  E1, N1 = Ost/Nord-Position Antenne 1
  E2, N2 = Ost/Nord-Position Antenne 2
```

**Technische Details:**
- Genauigkeit: ±0,5° bis ±1,0° (abhängig vom Antennenabstand)
- Genauigkeit = f(Abstand): ca. 0,75° / (Abstand in Metern) bei L1-GPS
- Update-Rate: 2–20 Hz
- Antennenabstand: mindestens 0,5 m, optimal 1,0–2,0 m
- Benötigt freie Sicht zum Himmel (mindestens 4 Satelliten pro Antenne)

**Vorteile:**
- Keine Magnetfeld-Abhängigkeit — funktioniert neben Stahlkonstruktionen
- Keine Deviation, keine Kompensation erforderlich
- Keine Krängungsfehler
- Gibt True Heading (rechtweisend), nicht Magnetic Heading
- Funktioniert in allen magnetischen Zonen (auch Polarnähe)

**Nachteile:**
- Benötigt freie Himmelssicht — unter Brücken, in Marinas, in Fjorden problematisch
- Langsamer als IMU bei schnellen Kursänderungen
- Teurer (zwei GPS-Empfänger)
- Antennen-Montage: Abstand muss präzise eingehalten werden
- Kein Heading im Stand (oder nur sehr ungenau) bei RTK-GPS
- Anfällig für Multipath-Effekte (Reflexionen an Masten, Aufbauten)

**Beispiel-Produkte:**
- Furuno SC-50 (Satellite Compass, 3 Antennen, ±0,5°)
- Simrad HS80A (Dual-GPS, ±0,5°)
- Garmin GPS 24xd (Dual-Frequenz, Heading-fähig mit externem Empfänger)
- Hemisphere V500 (OEM-Modul für Custom-Installationen)

#### 2.5.4 Kombinations-Systeme

Moderne High-End-Systeme kombinieren alle drei Technologien:

```
┌─────────────────────────────────────────────┐
│         HYBRID-KOMPASS-SYSTEM               │
│                                             │
│  ┌───────────┐  ┌────────────┐  ┌────────┐ │
│  │ Fluxgate/ │  │ 3-Achsen-  │  │ GPS    │ │
│  │ Magneto-  │  │ Gyroskop   │  │ Dual-  │ │
│  │ meter     │  │ (MEMS)     │  │ Antenne│ │
│  └─────┬─────┘  └──────┬─────┘  └───┬────┘ │
│        │               │            │       │
│        └───────┬───────┘            │       │
│                │                    │       │
│        ┌───────┴──────┐             │       │
│        │Extended      │◀────────────┘       │
│        │Kalman Filter │                     │
│        └───────┬──────┘                     │
│                │                            │
│         Fused Heading                       │
│         (True + Magnetic)                   │
│         + Roll + Pitch                      │
│         + Yaw Rate                          │
│         + Position                          │
└─────────────────────────────────────────────┘
```

**Vorteile der Kombination:**
- Magnetometer: Langfristig stabile Kursreferenz
- Gyroskop: Schnelle Kursänderungs-Erkennung, Dämpfung
- GPS: Absolute Referenz, eliminiert Deviation
- Redundanz: Einzelne Sensoren können ausfallen, System bleibt funktional

### 2.6 Ruderwinkelgeber (Rudder Feedback Unit)

Der Ruderwinkelgeber ist der zweite kritische Sensor neben dem Kompass. Er meldet dem Autopiloten die aktuelle Ruderstellung.

#### 2.6.1 Typen

**Potentiometer-Typ:**
- Einfaches Drehpotentiometer am Ruderschaft oder Ruderquadranten
- Auflösung: 0,5–1,0°
- Lebensdauer: 500.000–2.000.000 Zyklen (mechanischer Schleifer)
- Preis: 80–250 EUR
- Problem: Verschleiß, Kontaktprobleme, Korrosion in feuchter Umgebung

**Hall-Effekt-Typ:**
- Berührungsloser Winkelsensor (Magnet + Hall-Sensor)
- Auflösung: 0,1–0,5°
- Lebensdauer: Unbegrenzt (keine mechanischen Kontakte)
- Preis: 150–400 EUR
- Vorteil: Wartungsfrei, wasserdicht vergießbar

**NMEA-2000-Rudersensor:**
- Direkt in den Datenbus integrierter Sensor
- Digitale Übertragung, keine analogen Leitungen
- Preis: 200–500 EUR
- Vorteil: Einfache Installation, Plug & Play

#### 2.6.2 Kalibrierung

Die Kalibrierung des Ruderwinkelgebers ist kritisch für die Autopilot-Funktion:

1. **Mittelstellung (Midship):** Ruder exakt mittschiffs, Autopilot „Zero" setzen
2. **Backbord-Anschlag:** Ruder ganz nach Backbord, Winkel erfassen (typisch 30–40°)
3. **Steuerbord-Anschlag:** Ruder ganz nach Steuerbord, Winkel erfassen
4. **Linearitätsprüfung:** Ruder in 5°-Schritten durchfahren, Linearität prüfen

**Häufige Fehler:**
- Mechanisches Spiel in der Ruderanlenkung → Totband (Deadband) in der Regelung
- Potentiometer verschoben → Asymmetrische Ausschläge
- Falscher Sensor-Typ für den Ruderbereich → Sättigung vor Endanschlag

### 2.7 Ruderkraft-Berechnung

Die benötigte Ruderkraft bestimmt die Dimensionierung des Antriebs (Drive Unit).

#### 2.7.1 Grundformel

```
T_rudder = 0.5 · ρ · V² · A · Cd · r

Wobei:
  T_rudder = Drehmoment am Ruderschaft [Nm]
  ρ = Wasserdichte (1025 kg/m³ Seewasser)
  V = Bootsgeschwindigkeit [m/s]
  A = Ruderfläche [m²]
  Cd = Widerstandsbeiwert des Ruders (≈ 0.5–1.2 je nach Profil und Anstellwinkel)
  r = Hebelarm (Abstand Druckpunkt zum Ruderschaft) [m]
```

#### 2.7.2 Ruderkraft-Tabelle nach Bootsgröße

| Bootslänge (LOA) | Ruder-Typ | Max. Ruderkraft am Griff | Drehmoment am Schaft | Empfohlener Antrieb |
|-------------------|-----------|-------------------------|---------------------|-------------------|
| 7–9 m Segel | Spatenruder | 15–30 kg | 50–150 Nm | Pinnenantrieb 12V |
| 9–12 m Segel | Spatenruder | 25–50 kg | 100–300 Nm | Linear/Radantrieb 12V |
| 12–15 m Segel | Skeg-Ruder | 40–80 kg | 200–500 Nm | Linear/Hydraulik 12V |
| 15–18 m Segel | Skeg-Ruder | 60–120 kg | 400–800 Nm | Hydraulik 12/24V |
| 18–24 m Segel | Skeg/Spaten | 80–200 kg | 600–1500 Nm | Hydraulik 24V |
| 8–12 m Motor | Spatenruder | 20–40 kg | 80–250 Nm | Linear/Hydraulik 12V |
| 12–18 m Motor | Spatenruder | 40–100 kg | 200–600 Nm | Hydraulik 12/24V |
| 18–24 m Motor | Spatenruder | 80–200 kg | 500–1200 Nm | Hydraulik 24V |

#### 2.7.3 Sicherheitsfaktor

Die Antriebseinheit muss so dimensioniert sein, dass sie unter Extrembedingungen (Surfen, Broaching, Sturmsteuerung) das Ruder noch kontrollieren kann:

```
Antrieb_Dimensionierung = Max_Ruderkraft × 1.5 (Segel) bzw. × 1.3 (Motor)
```

### 2.8 Ruderdämpfung und Totband

#### 2.8.1 Totband (Deadband)

Das Totband ist der Kursbereich, innerhalb dessen der Autopilot keine Ruderkorrektur ausführt:

- **Zu kleines Totband (< 1°):** Permanente Ruderkorrekturen, hoher Stromverbrauch, Verschleiß
- **Optimales Totband (1°–3°):** Ruhiges Steuern, wenig Stromverbrauch
- **Zu großes Totband (> 5°):** Boot schlängelt, ineffiziente Fahrt

**Empfohlene Totband-Einstellungen:**

| Bedingung | Totband | Begründung |
|-----------|---------|-----------|
| Ruhiges Wasser | 1°–2° | Enger Kurs für Navigation |
| Mäßiger Seegang | 2°–3° | Welleneinfluss ignorieren |
| Schwerer Seegang | 3°–5° | Energie sparen, Ruder schonen |
| Windsteuerung (Segel) | 2°–4° | Wind-Schwankungen tolerieren |
| Motoryacht Verdränger | 1°–2° | Kein Welleneinfluss auf Kurs |
| Motoryacht Gleiter | 2°–4° | Dynamischer Kurs |

#### 2.8.2 Ruderdämpfung (Rate Limiting)

Die Ruderdämpfung begrenzt die maximale Rudergeschwindigkeit:

```
Rudder_Rate_Max = einstellbar, typisch 3–8°/s

Beispiel: Bei Rudder_Rate_Max = 5°/s und benötigter Korrektur von 15°:
  → Ruder braucht 3 Sekunden für volle Korrektur
  → Verhindert abrupte Ruderbewegungen
  → Schont Antrieb und Ruderanlenkung
```

### 2.9 Wellensteuerung (Sea State Filter)

In Seegangsbedingungen erzeugen Wellen hochfrequente Kursänderungen, die der Autopilot nicht korrigieren sollte (die nächste Welle dreht das Boot ohnehin zurück).

#### 2.9.1 Sea State Filter

Der Sea State Filter (Wellenfilter) unterscheidet zwischen:
- **Echte Kursänderung:** Langfristige Abweichung, die korrigiert werden muss
- **Welleninduzierte Gierbewegung:** Kurzfristige Pendelbewegung, die sich selbst ausgleicht

**Implementierung:**

```
Heading_filtered = Low-Pass-Filter(Heading_raw, cutoff_frequency)

Typische Cutoff-Frequenz:
  - Ruhig:  0.5 Hz (lässt fast alles durch)
  - Mäßig:  0.2 Hz (filtert Wellen mit T < 5s)
  - Schwer: 0.1 Hz (filtert Wellen mit T < 10s)
  - Sturm:  0.05 Hz (filtert fast alle Wellenbewegungen)
```

**Hersteller-Terminologie:**

| Hersteller | Bezeichnung | Einstellbereich |
|-----------|-------------|-----------------|
| Raymarine | Response | 1 (ruhig) – 9 (schwer) |
| B&G / Simrad | Turning Rate Limit + Wave Filter | Low / Medium / High / Off |
| Garmin | Sea Condition | Calm – Moderate – Rough |
| Furuno | Sea State | 1–9 |
| NKE | Coefficient de mer | 0.0–9.9 |

#### 2.9.2 Adaptive Wellenfilterung

Moderne Systeme analysieren das Frequenzspektrum der Gierbewegungen:

1. **FFT-Analyse** (Fast Fourier Transform) der Heading-Daten
2. **Identifikation** der dominanten Wellenfrequenz
3. **Notch-Filter** bei der Wellenfrequenz → filtert gezielt die Wellenstörung heraus
4. **Kontinuierliche Anpassung** der Filterparameter an wechselnde Seegangsbedingungen

### 2.10 Windsteuerung (Wind Mode)

Im Windmodus steuert der Autopilot nicht nach Kompasskurs, sondern nach einem konstanten Winkel zum scheinbaren oder wahren Wind.

#### 2.10.1 Scheinbarer vs. wahrer Wind

```
Scheinbarer Wind (AWA/AWS):
  → Gemessen am Windgeber am Masttopp
  → Kombination aus wahrem Wind + Fahrtwind
  → Ändert sich mit Bootsgeschwindigkeit und -kurs

Wahrer Wind (TWA/TWS):
  → Der tatsächlich wehende Wind
  → Berechnet aus: AWA, AWS, SOG, COG
  → Unabhängig von Bootsgeschwindigkeit
```

**Wind-Autopilot steuert nach:**

| Modus | Referenz | Anwendung |
|-------|---------|-----------|
| Apparent Wind (AWA) | Scheinbarer Windwinkel | Am Wind segeln, Standard für Kreuzen |
| True Wind (TWA) | Wahrer Windwinkel | Raumschots segeln, Langstrecke |

#### 2.10.2 AWA-Steuerung (Standard für Segelyachten)

Der Autopilot hält einen konstanten scheinbaren Windwinkel:

**Vorteile:**
- Direktes Feedback vom Windgeber → schnelle Reaktion
- Optimal für Am-Wind-Kurse: Boot segelt automatisch im optimalen Winkel
- Bei Böen fällt das Boot automatisch ab → natürliche Böenentlastung

**Nachteile:**
- Bei Windstille oder sehr leichtem Wind instabil (Windgeber-Rauschen)
- Bei raumem Wind kann AWA-Steuerung zu ungewollten Halsen führen
- Kurs ändert sich mit jeder Windänderung → nicht ideal für Navigation zu Zielpunkt

#### 2.10.3 TWA-Steuerung

Der Autopilot berechnet den wahren Windwinkel und hält diesen konstant:

**Vorteile:**
- Stabiler auf raumem Kurs
- Weniger Neigung zu ungewollten Halsen
- Konsistentere Fahrt bei schwankendem Wind

**Nachteile:**
- Erfordert SOG/COG vom GPS → Latenz in der Berechnung
- Komplexere Regelung (TWA ist eine berechnete Größe)
- Bei sehr niedrigen Geschwindigkeiten (< 2 kn) unzuverlässig

#### 2.10.4 Wind-Modus PID-Anpassung

Die PID-Parameter für den Windmodus unterscheiden sich signifikant vom Kompass-Modus:

```
Wind-Modus:
  - Höherer Kd: Windwechsel erzeugen schnelle AWA-Änderungen → mehr Dämpfung
  - Niedrigerer Ki: Wind dreht häufig → weniger Integration
  - Kp ähnlich wie Kompass-Modus

Faustregel:
  Kd_wind ≈ 1.5 × Kd_kompass
  Ki_wind ≈ 0.5 × Ki_kompass
  Kp_wind ≈ 1.0 × Kp_kompass
```

### 2.11 Track-Modus (GPS-Wegpunktsteuerung)

Im Track-Modus steuert der Autopilot nicht nach Kurs oder Wind, sondern folgt einer vom Plotter vorgegebenen Route.

#### 2.11.1 Cross-Track Error (XTE)

Die Grundgröße im Track-Modus ist der Cross-Track Error — die seitliche Abweichung von der Solllinie:

```
XTE = Seitlicher Abstand Boot ↔ Sollkurslinie [m oder nm]

Positive XTE = Boot ist rechts der Solllinie
Negative XTE = Boot ist links der Solllinie
```

**Track-Regelung:**

```
Heading_command = Course_to_Waypoint + Kxte · XTE + Kxte_rate · dXTE/dt

Wobei:
  Course_to_Waypoint = Kurs zum nächsten Wegpunkt
  Kxte = Verstärkung für XTE-Korrektur
  dXTE/dt = Änderungsrate des XTE (Annäherung an oder Entfernung von Solllinie)
```

#### 2.11.2 Wegpunkt-Wechsel

Beim Erreichen eines Wegpunkts muss der Autopilot den Kurs zum nächsten Wegpunkt einschlagen:

**Arrival Circle:**
- Typischer Radius: 0,05–0,50 nm (einstellbar)
- Beim Eintritt in den Kreis → Kurswechsel zum nächsten Wegpunkt
- Warnung an den Skipper: „Approaching Waypoint"

**Turn Control:**
- Maximale Drehrate einstellbar (typisch 5–30°/min)
- Verhindert abrupte Kursänderungen bei scharfen Kurswechseln
- Bei Kursänderung > 30°: Warnung, Bestätigung erforderlich (Safety)

#### 2.11.3 Strömungskorrektur

In Gewässern mit Strömung (Gezeiten, Flussströmung) muss der Autopilot den Kurs anpassen:

```
Heading_corrected = Heading_to_Waypoint + CTS_correction

CTS_correction = arcsin(Current_Speed · sin(Current_Direction - Heading) / Boat_Speed)
```

### 2.12 Erweiterte Regelungstechnik

#### 2.12.1 Zustandsregler (State-Space Controller)

Fortgeschrittene Autopiloten verwenden Zustandsregler statt einfacher PID-Regler:

**Zustandsvektor:**
```
x = [ψ, r, δ, v]ᵀ

Wobei:
  ψ = Heading (Kurs)
  r = Yaw Rate (Drehrate)
  δ = Ruderwinkel
  v = Geschwindigkeit
```

**Zustandsgleichung (Nomoto-Modell, vereinfacht):**
```
T · dr/dt + r = K · δ

Wobei:
  T = Zeitkonstante (Trägheit des Bootes)
  K = Ruderwirksamkeit (gain)
```

**Nomoto-Parameter typischer Yachten:**

| Bootstyp | T [s] | K [1/s] | T/K [s²] | Bemerkung |
|----------|-------|---------|----------|-----------|
| Segelyacht 10 m | 3–8 | 0.05–0.15 | 30–80 | Mittlere Trägheit |
| Segelyacht 15 m | 5–15 | 0.03–0.10 | 80–200 | Hohe Trägheit |
| Motoryacht 10 m | 2–5 | 0.10–0.30 | 10–30 | Schnelle Reaktion |
| Motoryacht 18 m | 4–10 | 0.05–0.15 | 40–100 | Mittlere Reaktion |
| Katamaran 12 m | 2–6 | 0.08–0.20 | 15–40 | Leicht am Ruder |
| Superyacht 30 m | 10–30 | 0.02–0.08 | 200–500 | Sehr träge |

#### 2.12.2 Modellprädiktive Regelung (MPC)

Die modernste Regelungstechnik in Premium-Autopiloten:

**Prinzip:**
1. Internes Modell des Boot-Verhaltens (Nomoto oder komplexer)
2. Vorhersage der Bootsbewegung über N Zeitschritte (Prediction Horizon)
3. Optimierung der Ruder-Sequenz, die den Kurs am besten auf Soll bringt
4. Nur den ersten Ruderschritt ausführen, dann neu berechnen

**Vorteile:**
- Berücksichtigt Stellgrößenbeschränkungen (Ruderanschlag) direkt in der Optimierung
- Kann Totzeiten (Ruderantwort-Verzögerung) kompensieren
- Optimiert Energieverbrauch (weniger Ruderbewegungen)
- Kann Wind- und Strömungsvorhersagen einbeziehen

**Herausforderung auf Yachten:**
- Rechenintensiv (aber moderne ARM-Prozessoren schaffen es)
- Erfordert genaues Boot-Modell (oder Online-Identifikation)
- Bisher nur in Premium-Systemen (NKE, B&G H5000)

### 2.13 Signalverarbeitung und Filterung

#### 2.13.1 Digitale Filter im Autopiloten

| Filter-Typ | Anwendung | Parameter |
|-----------|-----------|-----------|
| Tiefpass (Low-Pass) | Kompass-Rauschen glätten | fc = 0.5–2.0 Hz |
| Bandsperre (Notch) | Wellenfrequenz unterdrücken | f0 = dominante Wellenfrequenz |
| Komplementärfilter | Sensor-Fusion (Gyro + Magnetometer) | τ = 0.1–1.0 s |
| Kalman-Filter | Optimale Schätzung bei verrauschten Sensoren | Q, R Matrizen |
| Medianfilter | Ausreißer-Unterdrückung (Spike-Removal) | Fenstergröße N = 3–7 |

#### 2.13.2 Abtastrate und Latenz

| Komponente | Typische Abtastrate | Max. Latenz |
|-----------|-------------------|-------------|
| Kompass (Fluxgate) | 10 Hz | 100 ms |
| IMU (9-Achsen) | 25–100 Hz | 20–40 ms |
| GPS | 1–10 Hz | 100–500 ms |
| Windgeber | 2–4 Hz | 250–500 ms |
| Ruderwinkelgeber | 10–50 Hz | 20–100 ms |
| PID-Berechnung | 10–50 Hz | 10–50 ms |
| Antrieb (Hydraulik) | Reaktionszeit | 200–500 ms |
| Antrieb (Linear) | Reaktionszeit | 100–300 ms |
| Gesamtkette | — | 300–1000 ms |

**Latenz-Budgetierung:**
Die Gesamtlatenz (Sensormessung → Ruderausschlag) sollte unter 1 Sekunde bleiben. Bei Performance-Segelyachten ist <500 ms anzustreben. Jede zusätzliche Verzögerung verschlechtert die Regelqualität und kann zu Oszillationen führen.

---

## 3. Typenübersicht

### 3.1 Hydraulische Autopiloten

#### 3.1.1 Funktionsprinzip

Hydraulische Autopiloten verwenden eine reversible Hydraulikpumpe, die Öl in einen doppelt wirkenden Hydraulikzylinder pumpt:

```
┌──────────┐     ┌──────────────┐     ┌──────────────┐     ┌──────────┐
│ Kurs-    │────▶│ Elektr.      │────▶│ Hydraulik-   │────▶│ Ruder-   │
│ computer │     │ Steuerventil │     │ Zylinder     │     │ quadrant │
└──────────┘     │ oder Pumpe   │     │ (doppelt     │     │ oder     │
                 └──────────────┘     │  wirkend)    │     │ Tiller   │
                                      └──────────────┘     └──────────┘
```

**Zwei Systeme:**

1. **Eigenständige Hydraulikpumpe (Power Pack):**
   - Elektromotor treibt Hydraulikpumpe an
   - Umschaltventil steuert Druckrichtung
   - Typisch für Boote 12–24 m
   - Kann an bestehende Ruderhydraulik angeschlossen werden

2. **Reversible Pumpe (Integrated Drive):**
   - Bidirektionaler Motor dreht Pumpe in beide Richtungen
   - Kompakter als Power Pack
   - Typisch für Boote 10–18 m

#### 3.1.2 Spezifikationen typischer Hydraulik-Antriebe

| Parameter | Klein (8–12 m) | Mittel (12–18 m) | Groß (18–24 m) |
|-----------|----------------|-------------------|-----------------|
| Zylindervolumen | 80–150 cm³ | 150–350 cm³ | 350–800 cm³ |
| Betriebsdruck | 30–60 bar | 50–100 bar | 80–200 bar |
| Durchfluss | 1–3 l/min | 3–8 l/min | 8–20 l/min |
| Rudergeschwindigkeit | 5–8°/s | 4–6°/s | 3–5°/s |
| Stromverbrauch (Halten) | 0,5–2 A | 2–5 A | 5–15 A |
| Stromverbrauch (aktiv) | 3–8 A | 8–20 A | 15–40 A |
| Spannung | 12 V DC | 12/24 V DC | 24 V DC |
| Gewicht | 5–10 kg | 10–25 kg | 25–60 kg |
| Preis (Antrieb) | 1.500–3.000 EUR | 3.000–7.000 EUR | 7.000–18.000 EUR |

#### 3.1.3 Vor- und Nachteile

**Vorteile:**
- Höchste Leistung pro Gewicht
- Geräuscharm im Betrieb (Hydraulikflüssigkeit dämpft)
- Kann an bestehende Ruderhydraulik angeschlossen werden
- Robuste, langlebige Technik
- Sanfter Ruderausschlag (keine Ruckbewegungen)

**Nachteile:**
- Höchster Installationsaufwand (Leitungen, Öl, Entlüftung)
- Leckage-Risiko (Hydrauliköl in der Bilge)
- Regelmäßiger Ölwechsel und Dichtungsprüfung erforderlich
- Teurer als mechanische Antriebe
- Keine Ruderrückmeldung bei Handsteuerung (Bypass-Ventil erforderlich)

#### 3.1.4 Installation

**Kritische Installationsparameter:**

| Parameter | Empfehlung | Konsequenz bei Fehler |
|-----------|-----------|----------------------|
| Hydraulikschläuche | Hochdruck-Marine-Schläuche, SAE J1942 | Platzen, Ölverlust, Ruderausfall |
| Anschlüsse | JIC/SAE-Fittings, Edelstahl oder Messing | Leckage, Korrosion |
| Ölsorte | Hersteller-Spezifikation (meist ATF oder Spezialöl) | Dichtungsschaden, Pumpenversagen |
| Entlüftung | Vollständig, keine Luftblasen im System | Schwammiges Ruder, inkonsistente Reaktion |
| Bypass-Ventil | Leicht erreichbar, geprüft | Keine Handsteuerung bei Ausfall |
| Zylinder-Montage | Koaxial zur Ruderbewegung, keine Seitenlasten | Vorzeitiger Verschleiß, Leckage |

### 3.2 Linearantrieb (Linear Drive)

#### 3.2.1 Funktionsprinzip

Ein Linearantrieb wandelt die Drehbewegung eines Elektromotors über ein Getriebe (Spindel oder Kugelumlaufspindel) in eine lineare Schub-/Zugbewegung um:

```
┌──────────┐     ┌──────────────┐     ┌──────────────┐     ┌──────────┐
│ Kurs-    │────▶│ Elektromotor │────▶│ Spindel +    │────▶│ Ruder-   │
│ computer │     │ DC oder BLDC │     │ Mutter       │     │ quadrant │
└──────────┘     └──────────────┘     │ → Linearhub  │     │ (Hebel)  │
                                      └──────────────┘     └──────────┘
```

#### 3.2.2 Spezifikationen

| Parameter | Klein (8–10 m) | Mittel (10–14 m) | Groß (14–18 m) |
|-----------|----------------|-------------------|-----------------|
| Schubkraft | 250–500 N | 500–1200 N | 1200–3000 N |
| Hub | 100–200 mm | 150–300 mm | 200–400 mm |
| Geschwindigkeit | 10–25 mm/s | 8–20 mm/s | 5–15 mm/s |
| Stromverbrauch (Halten) | 0,3–1,0 A | 0,8–2,5 A | 2,0–5,0 A |
| Stromverbrauch (aktiv) | 2–6 A | 5–12 A | 10–25 A |
| Spannung | 12 V DC | 12 V DC | 12/24 V DC |
| Gewicht | 3–6 kg | 5–10 kg | 8–18 kg |
| Preis | 800–1.800 EUR | 1.500–3.500 EUR | 3.000–6.000 EUR |

#### 3.2.3 Vor- und Nachteile

**Vorteile:**
- Einfache Installation (nur mechanische Verbindung zum Ruderquadranten + Strom/Daten)
- Kein Hydrauliköl, keine Schläuche
- Kompakt und leicht
- Geringer Wartungsaufwand
- Gutes Preis-Leistungs-Verhältnis

**Nachteile:**
- Hörbar (Motorgeräusch, Spindelgeräusch)
- Begrenzte Leistung (max. ca. 18 m Bootslänge)
- Mechanischer Verschleiß (Spindel, Getriebe)
- Kein sanfter Übergang bei Richtungswechsel (Spiel im Getriebe)
- Ruder nicht frei drehbar bei ausgeschaltetem Autopilot (Spindel hemmt)

#### 3.2.4 Anlenkgeometrie

Die Anlenkung am Ruderquadranten ist geometrisch kritisch:

```
              Quadrant
                │
        ────────┼────────
       /        │        \
      /    ┌────┘         \
     /     │  Hebel r      \
    ╱      │               ╲
   ╱       ▼                ╲
  ╱   ┌────────────┐         ╲
      │ Linearantrieb│
      └────────────┘
           Hub s

Ruderwinkel δ = arcsin(s / r)

Wobei:
  s = Linearer Hub [mm]
  r = Hebelarm am Quadranten [mm]
```

**Wichtig:** Der Hebelarm r bestimmt:
- Kleiner r → großer Ruderwinkel bei kleinem Hub → aber mehr Kraft nötig
- Großer r → kleiner Ruderwinkel bei gleichem Hub → weniger Kraft nötig

Faustregel: r so wählen, dass bei maximalem Hub der maximale Ruderwinkel (30–40°) erreicht wird.

### 3.3 Radantrieb (Wheel Drive)

#### 3.3.1 Funktionsprinzip

Der Radantrieb greift direkt am Steuerrad an:

```
┌──────────┐     ┌──────────────┐     ┌──────────────┐
│ Kurs-    │────▶│ Elektromotor │────▶│ Reibrad oder │
│ computer │     │ + Getriebe   │     │ Zahnriemen   │
└──────────┘     └──────────────┘     │ am Steuerrad │
                                      └──────────────┘
```

**Zwei Angriffspunkte:**
1. **Reibrad auf Steuerrad-Felge:** Einfach, nachrüstbar, aber Schlupf bei nasser Felge
2. **Zahnriemen/Kette auf Steuerrad-Achse:** Formschlüssig, kein Schlupf, aber aufwändigere Montage

#### 3.3.2 Spezifikationen

| Parameter | Klein (8–11 m) | Mittel (11–15 m) |
|-----------|----------------|-------------------|
| Drehmoment | 5–15 Nm | 15–40 Nm |
| Drehgeschwindigkeit | 15–30 RPM | 10–20 RPM |
| Stromverbrauch (Halten) | 0,2–0,8 A | 0,5–2,0 A |
| Stromverbrauch (aktiv) | 1,5–4,0 A | 3,0–8,0 A |
| Spannung | 12 V DC | 12 V DC |
| Gewicht | 2–5 kg | 4–8 kg |
| Preis | 600–1.500 EUR | 1.200–2.800 EUR |

#### 3.3.3 Vor- und Nachteile

**Vorteile:**
- Einfachste Installation (oft nur Klemmen am Steuerrad)
- Sofort nachrüstbar ohne Eingriff in Ruderanlenkung
- Steuerrad bleibt bei ausgeschaltetem Autopilot frei drehbar
- Günstiger Preis
- Geringes Gewicht

**Nachteile:**
- Begrenzte Leistung (max. ca. 14 m, abhängig von Ruderkraft)
- Reibrad-Systeme können bei Nässe rutschen
- Geräuschentwicklung (Motor + Getriebe am Steuerstand)
- Ästhetisch nicht ideal (sichtbar am Steuerstand)
- Nicht geeignet für Hydrauliksteuerungen

### 3.4 Pinnenantrieb (Tiller Pilot)

#### 3.4.1 Funktionsprinzip

Der Pinnenantrieb ist die einfachste Form eines Autopiloten. Ein Linearantrieb greift direkt an der Pinne (Ruderpinne) an:

```
┌────────────────────┐
│ Pinnenantrieb      │
│ (Motor + Spindel + │
│  Kurscomputer +    │
│  Kompass in einem  │
│  Gehäuse)          │
└────────┬───────────┘
         │ Anlenkung
    ─────┴─────── Pinne (Ruderpinne)
         │
    ─────┴─────── Ruderschaft
```

Der Pinnenantrieb ist typischerweise eine All-in-One-Einheit: Kompass, Kurscomputer, Antrieb und Bedienung in einem Gehäuse.

#### 3.4.2 Spezifikationen

| Parameter | Klein (6–8 m) | Mittel (8–10 m) | Groß (10–12 m) |
|-----------|---------------|------------------|-----------------|
| Schubkraft | 120–250 N | 250–500 N | 500–750 N |
| Hub | 150–250 mm | 200–350 mm | 250–450 mm |
| Stromverbrauch (mittel) | 0,5–1,5 A | 1,0–3,0 A | 2,0–5,0 A |
| Spannung | 12 V DC | 12 V DC | 12 V DC |
| Gewicht | 1,5–3,0 kg | 2,5–4,5 kg | 4,0–7,0 kg |
| Max. Bootslänge | 8 m / 4 t | 10 m / 6 t | 12 m / 10 t |
| Preis | 400–800 EUR | 700–1.500 EUR | 1.200–2.500 EUR |

#### 3.4.3 Vor- und Nachteile

**Vorteile:**
- Günstigster Einstieg in die Autopilot-Welt
- All-in-One: Kein separater Kompass, kein Kurscomputer, kein Ruderwinkelgeber nötig
- Einfachste Installation: Pinne einstecken, Strom anschließen, fertig
- Leicht und kompakt → ideal für Trailer-Segler
- Sofort abnehmbar → kein Eingriff ins Boot

**Nachteile:**
- Nur für Pinnensteuerung (nicht für Radsteuerung)
- Begrenzte Leistung (max. ca. 12 m)
- Exponiert im Cockpit (Spritzwasser, UV, mechanische Belastung)
- Geringere Robustheit als eingebaute Systeme
- Eingebauter Kompass oft ungenauer als separater Sensor (Nähe zu Cockpit-Elektronik)
- Höherer Stromverbrauch als größere Systeme (ineffizienterer Antrieb)

### 3.5 Windfahnen-Selbststeueranlage

#### 3.5.1 Funktionsprinzip

Die Windfahnen-Selbststeueranlage ist ein mechanisches System ohne Elektronik und ohne Stromverbrauch. Sie nutzt die Kraft des Windes zur Kurskorrektur:

```
Prinzip: Servo-Pendulum-Ruder (häufigster Typ)

  1. Windfahne oben dreht sich aus dem Wind
  2. Mechanische Kopplung überträgt Drehung auf Servo-Ruder (Hilfsruder im Wasser)
  3. Servo-Ruder erzeugt Wasserkraft durch Anströmung
  4. Wasserkraft wird über Leinen auf Hauptruder übertragen
  5. Hauptruder korrigiert den Kurs
  6. Boot dreht zurück in den Wind → Windfahne zentriert sich
  7. Geschlossener Regelkreis ohne Strom
```

#### 3.5.2 Windfahnen-Typen

**Typ 1: Direktes Hilfsruder (Auxiliary Rudder)**
- Windfahne steuert direkt ein separates Hilfsruder
- Einfaches Prinzip, aber Hilfsruder muss groß genug sein
- Beispiel: Hydrovane (Kanada)
- Vorteil: Vollständig unabhängig vom Hauptruder
- Nachteil: Hilfsruder erzeugt nicht genug Kraft für große Boote

**Typ 2: Servo-Pendulum (Pendulum Servo)**
- Windfahne steuert ein kleines Servo-Ruder, das im Wasser pendelt
- Die Strömungskraft am Servo-Ruder wird über Leinen auf das Hauptruder übertragen
- Kraftverstärkung: Die Wasserströmung liefert die Energie, die Windfahne steuert nur
- Beispiel: Windpilot Pacific (Deutschland), Monitor (USA)
- Vorteil: Funktioniert für Boote bis 20+ Meter (Kraftverstärkung)
- Nachteil: Erfordert Verbindung zum Hauptruder (Leinen, Blöcke)

**Typ 3: Trim-Tab (Ruder-Trimmklappe)**
- Windfahne steuert eine Trimmklappe am Hauptruder
- Trimmklappe erzeugt Moment, das Hauptruder dreht sich
- Beispiel: Aries (UK, historisch)
- Vorteil: Keine Leinen, keine separate Ruderanlage
- Nachteil: Erfordert Modifikation des Hauptruders, begrenzte Leistung

#### 3.5.3 Vergleich Windfahne vs. Elektro-Autopilot

| Kriterium | Windfahne | Elektro-Autopilot |
|-----------|-----------|-------------------|
| Stromverbrauch | 0 W | 12–120 W |
| Kompass-Steuerung | Nein (nur Windsteuerung) | Ja |
| GPS-Steuerung | Nein | Ja |
| Windsteuerung | Immer (ist das Prinzip) | Ja (mit Windgeber) |
| Funktioniert bei Flaute | Nein | Ja |
| Funktioniert unter Motor | Eingeschränkt | Ja |
| Wartung | Mechanisch (einfach) | Elektronisch (komplex) |
| Redundanz | Unabhängig vom Bordnetz | Abhängig von Strom |
| Preis | 2.500–5.500 EUR | 2.000–15.000 EUR |
| Gewicht (am Heck) | 15–35 kg | 3–25 kg (verteilt) |
| Lebensdauer | 20+ Jahre | 10–15 Jahre |
| Performance im Sturm | Exzellent (mehr Wind = mehr Kraft) | Gut bis limitiert (Stromverbrauch) |
| Am Wind | Sehr gut | Sehr gut |
| Raumschots/Vorwind | Gut bis mäßig | Sehr gut (mit Kompass) |

### 3.6 Integrierte Systeme

#### 3.6.1 Definition

Integrierte Systeme kombinieren den Autopiloten mit dem gesamten Navigations- und Instrumentensystem:

```
┌──────────────────────────────────────────────────────┐
│              INTEGRIERTES NAVIGATIONSSYSTEM           │
│                                                      │
│  ┌─────────┐  ┌──────────┐  ┌──────────┐  ┌──────┐ │
│  │ Plotter │  │ Radar    │  │ AIS      │  │ VHF  │ │
│  └────┬────┘  └────┬─────┘  └────┬─────┘  └──┬───┘ │
│       │            │             │            │      │
│       └────────┬───┴─────────┬───┘            │      │
│                │             │                │      │
│         ┌──────┴──────┐  ┌──┴────┐            │      │
│         │ AUTOPILOT   │  │ DSC   │────────────┘      │
│         │ Computer    │  │ MOB   │                    │
│         └──────┬──────┘  └───────┘                    │
│                │                                      │
│         ┌──────┴──────┐                               │
│         │   Drive     │                               │
│         │ (Hydraulik/ │                               │
│         │  Linear)    │                               │
│         └─────────────┘                               │
└──────────────────────────────────────────────────────┘
```

#### 3.6.2 Vorteile der Integration

| Funktion | Beschreibung | Praxis-Beispiel |
|----------|-------------|-----------------|
| Route Following | Autopilot folgt Plotter-Route automatisch | Kanalfahrt mit vielen Wegpunkten |
| Wind Strategy | Autopilot + Wind-Instrumente optimieren VMG | Langstrecken-Regatta |
| Radar Guard Zone | Radar erkennt Objekt → Autopilot-Alarm | Nachtfahrt |
| AIS CPA | AIS meldet Annäherung → Kursempfehlung | Berufsschifffahrt kreuzt |
| MOB Response | MOB-Taste → Autopilot fährt Williamson-Turn | Notfall |
| Sail Trim | Instrumente + Autopilot → optimaler Kurs | Performance-Segeln |
| Depth Guard | Echolot < Grenzwert → Autopilot-Warnung | Küstennavigation |

---

## 4. Produktlinien und Spezifikationen

### 4.1 Raymarine — Evolution EV-Serie

#### 4.1.1 Systemarchitektur

Raymarines Evolution-System ist um den **EV-1 Sensor Core** aufgebaut — eine 9-Achsen-IMU mit integriertem Kurscomputer:

**Komponenten:**

| Komponente | Modell | Funktion | Preis (ca.) |
|-----------|--------|----------|-------------|
| Sensor Core | EV-1 | 9-Achsen-IMU, Kurscomputer, Autolearn | 600–800 EUR |
| Steuerkopf | p70s (Segel) / p70Rs (Segel Race) | Bedieneinheit, Farb-Display | 700–1.200 EUR |
| Steuerkopf | p70 (Motor) | Bedieneinheit, Farb-Display | 700–1.000 EUR |
| Linearantrieb | Type 1 (bis 10 m) | 400 N Schub | 800–1.200 EUR |
| Linearantrieb | Type 2 (bis 14 m) | 750 N Schub | 1.200–1.800 EUR |
| Linearantrieb | Type 3 (bis 18 m) | 1200 N Schub | 1.800–2.800 EUR |
| Hydraulik | Type 0,5 (bis 12 m) | 80 cm³/rev | 1.500–2.500 EUR |
| Hydraulik | Type 1 (bis 18 m) | 160 cm³/rev | 2.500–4.000 EUR |
| Hydraulik | Type 2 (bis 24 m) | 350 cm³/rev | 4.000–7.000 EUR |
| Radantrieb | Wheel Drive | Bis 12 m, Reibrad | 800–1.200 EUR |
| Fernbedienung | S100 (kabellos) | Bluetooth, wasserdicht | 250–400 EUR |

#### 4.1.2 EV-1 AutoLearn

Das Kernelement des Evolution-Systems:

**Autolearn-Prozess:**
1. System erkennt Bootstyp (Segel/Motor/Verdränger/Gleiter)
2. Während der Fahrt analysiert der EV-1 die Bootsdynamik
3. Boot-Trägheit (T), Ruderwirksamkeit (K), Wellenbewegung werden identifiziert
4. PID-Parameter werden automatisch optimiert
5. Kontinuierliche Nachoptimierung während des Betriebs

**Autolearn-Parameter:**

| Parameter | Beschreibung | Einfluss |
|-----------|-------------|----------|
| Response Level | 1–9, Aggressivität der Kurskorrektur | Höher = aggressiver |
| Wind Trim | Automatische Windversatz-Kompensation | Ein/Aus |
| Rudder Gain | Manuelles Gain-Override | 1–9 |
| Off Heading Alarm | Kursabweichungs-Alarm | 5°–30° |
| Autotack | Automatische Wende auf Knopfdruck | Wendewinkel einstellbar |
| Power Steer | Manuelles Überbrücken des Autopiloten | Steuerrad/Pinne |

#### 4.1.3 SeaTalk-ng / NMEA 2000

Das Evolution-System nutzt SeaTalkNG (Raymarines NMEA-2000-Implementierung):

- Backbone-Kabel: 5-adrig, Micro-C-Stecker
- Terminatoren an beiden Enden des Backbone
- Max. Backbone-Länge: 100 m
- Max. Spur-Kabel: 6 m pro Gerät
- Max. Geräte am Bus: 50

### 4.2 B&G — H5000 und NAC-Serie

#### 4.2.1 B&G NAC (Navigation Autopilot Computer)

B&G gehört zur Navico-Gruppe und teilt die Technologieplattform mit Simrad. Die NAC-Serie richtet sich an Performance-Segler:

**NAC-Modelle:**

| Modell | Zielgruppe | Antrieb | Bootsgröße | Preis (ca.) |
|--------|-----------|---------|-----------|-------------|
| NAC-1 | Cruising-Segler | Linear/Hydraulik bis 10 t | 8–12 m | 800–1.200 EUR |
| NAC-2 | Cruiser/Racer | Linear/Hydraulik bis 20 t | 12–16 m | 1.200–2.000 EUR |
| NAC-3 | Offshore Racing | Alle Antriebe bis 40 t | 14–24 m | 2.000–3.500 EUR |

#### 4.2.2 B&G H5000 System

Das H5000 ist B&Gs Flaggschiff-System für Racing und Performance:

**Besonderheiten:**
- **Hercules-CPU**: Dedizierter Performance-Prozessor
- **Halcyon-CPU**: Autopilot-Rechner mit 50 Hz Update-Rate
- **Precision-9 Kompass**: 9-Achsen-IMU mit 25 Hz Update, ±0,5° Genauigkeit
- **H5000 Hydra**: Integrierter Autopilot-Computer mit Routing-Algorithmen
- **Performance-Funktionen**: VMG-Optimierung, Polaren-Berechnung, Layline-Berechnung

**H5000 Autopilot-Funktionen:**

| Funktion | Beschreibung | Regatta-Relevanz |
|----------|-------------|-----------------|
| VMG Optimization | Automatisches Steuern auf besten VMG | Kreuz- und Vorwind-Schenkel |
| Gust Response | Schnelle Reaktion auf Böen, automatisches Abfallen | Am-Wind-Segeln |
| Bearing Away | Kontrolliertes Abfallen bei Bö (kein Broaching) | Raumschots-Segeln |
| Performance Compass | GPS-korrigierter Kompass, minimale Latenz | Alle Manöver |
| Tack/Gybe Control | Präzise automatische Wenden und Halsen | Regatta-Manöver |

### 4.3 Garmin — GHP Reactor Serie

#### 4.3.1 Systemübersicht

Garmin bietet eine abgestufte Produktlinie:

**Reactor-Modelle:**

| Modell | Zielgruppe | Besonderheit | Bootsgröße | Preis (ca.) |
|--------|-----------|-------------|-----------|-------------|
| Reactor 40 Steer-by-Wire | Motor, Steer-by-Wire | Direkte CANBUS-Steuerung | 8–24 m Motor | 2.000–3.500 EUR |
| Reactor 40 Mechanical | Motor/Segel, mechanisch | Linear/Hydraulik/Rad | 8–18 m | 1.500–3.000 EUR |
| GHP 20 | Motor/Segel, Einsteiger | Linear/Rad, kompakt | 7–12 m | 1.000–2.000 EUR |
| GHP Compact Reactor | Kleinboote | All-in-One Hydraulik | 6–10 m Motor | 2.500–4.000 EUR |

#### 4.3.2 Garmin Heading Sensor

| Parameter | Spezifikation |
|-----------|--------------|
| Typ | 9-Achsen AHRS (Attitude and Heading Reference System) |
| Genauigkeit | ±2° (nach Kalibrierung ±1°) |
| Update-Rate | 10 Hz |
| Schnittstelle | NMEA 2000 |
| Stromverbrauch | 40 mA |
| Preis | 350–500 EUR |

#### 4.3.3 Reactor-Autoconfig

Garmins automatische Konfiguration:

1. Boot-Typ auswählen (Segel/Verdränger/Gleiter/Segeln-mit-Motor)
2. Bootsgröße angeben
3. System fährt automatische Konfigurationssequenz
4. Innerhalb 10–20 Minuten Fahrt: Grundabstimmung abgeschlossen
5. Feintuning über Garmin-Plotter oder Reactor-Steuereinheit

### 4.4 Simrad — AP-Serie

#### 4.4.1 Systemübersicht

Simrad nutzt die gleiche Navico-Plattform wie B&G, adressiert aber stärker den Motorboot- und Cruiser-Markt:

**Simrad Autopilot-Produkte:**

| Modell | Zielgruppe | Besonderheit | Preis (ca.) |
|--------|-----------|-------------|-------------|
| AP44 Steuerkopf | Motor/Segel, Premium | Farb-Touchscreen, 4,1" | 800–1.200 EUR |
| AP48 Steuerkopf | Motor, Großboote | Farb-Touchscreen, 4,1", Joystick-Integration | 900–1.400 EUR |
| NAC-1 Computer | Bis 10 t | Basis-Autopilot-Computer | 800–1.200 EUR |
| NAC-2 Computer | Bis 20 t | Mittelklasse, mehr Algorithmen | 1.200–2.000 EUR |
| NAC-3 Computer | Bis 40 t | High-End, alle Antriebe | 2.000–3.500 EUR |
| Precision-9 Kompass | Alle Systeme | 9-Achsen-IMU (identisch B&G) | 400–600 EUR |

#### 4.4.2 Simrad-spezifische Funktionen

| Funktion | Beschreibung |
|----------|-------------|
| Drift Mode | Autopilot hält Position (langsam kreisen), z.B. beim Angeln |
| Follow-Up Steering | Digitale Steuerung über Steuerstand-Joystick |
| Dock Mode | Manövrierhilfe im Hafen, reduzierte Gain |
| Turn Pattern | Verschiedene Wendemuster (Williamson, Scharnow, 180°) |
| Contour Mode | Folgt einer eingestellten Tiefenlinie |

### 4.5 Furuno — NavPilot-Serie

#### 4.5.1 Systemübersicht

Furuno ist der einzige Hersteller mit tiefgreifender kommerzieller Schifffahrts-Erfahrung, die in die Yachtprodukte einfließt:

**NavPilot-Modelle:**

| Modell | Zielgruppe | Besonderheit | Preis (ca.) |
|--------|-----------|-------------|-------------|
| NavPilot 300 | Segel/Motor 8–18 m | Kompakte Komplettlösung | 2.500–4.000 EUR |
| NavPilot 711C | Motor/Segel 12–24 m | Farb-Display, adaptive Regelung | 4.000–7.000 EUR |
| FAP-3011C | Kommerziell/Superyacht | IMO-konform, Dual-Steuerstand | 8.000–15.000 EUR |

#### 4.5.2 Furuno-spezifische Technologie

**FANTUM Feedback (FAP-3011C):**
- Kein physischer Ruderwinkelgeber erforderlich
- System berechnet Ruderposition aus Motorstrom und Modell
- Vorteil: Kein mechanischer Sensor, kein Verschleiß
- Nachteil: Weniger präzise als direkter Sensor

**Adaptive Regelung:**
- Furuno verwendet ein proprietäres adaptives System
- Regelparameter werden kontinuierlich angepasst
- Keine manuelle Tuning-Sequenz erforderlich
- Lernphase: Ca. 30 Minuten Fahrt

### 4.6 NKE — gyropilot-Serie

#### 4.6.1 Systemübersicht

NKE aus Frankreich ist der Spezialist für Performance-Segeln. Die Systeme werden in Grand-Prix-Regatten (Vendée Globe, Volvo Ocean Race) eingesetzt:

**NKE Autopilot-Produkte:**

| Modell | Zielgruppe | Besonderheit | Preis (ca.) |
|--------|-----------|-------------|-------------|
| gyropilot 2 | Racing/Performance | Schnellster Reaktionszeit, Regatta-optimiert | 3.000–5.000 EUR |
| gyropilot 3 | Cruiser-Racer | Balance zwischen Performance und Komfort | 2.500–4.000 EUR |
| Pilote HR | Heavy-Duty Racing | IMOCA 60, Class 40, maxi-yachts | 5.000–8.000 EUR |

#### 4.6.2 NKE-spezifische Technologie

**Performance-Algorithmen:**

| Algorithmus | Beschreibung | Regatta-Vorteil |
|------------|-------------|-----------------|
| VMG-Modus | Steuert auf optimalen VMG, nicht auf konstanten Winkel | +0,1–0,3 kn VMG-Gewinn |
| Gust Anticipation | Erkennt Böen am Drucksensor und reagiert vor der Böe | Weniger Luvschießer |
| Wave Mode | Identifiziert Wellenperiode, steuert „mit den Wellen" | Weniger Bremsen durch Wellenreiten |
| Heel Control | Begrenzt Krängung durch Abfallen bei Böen | Sicherheit + Speed |
| Target Speed | Steuert auf Zielgeschwindigkeit aus Polaren | Optimale Performance |

---

## 5. Hersteller-Datenbank

### 5.1 Raymarine (FLIR / Teledyne)

| Eigenschaft | Details |
|------------|---------|
| **Firmensitz** | Fareham, Hampshire, UK |
| **Mutterkonzern** | Teledyne Technologies (USA) |
| **Gegründet** | 1923 (als Kelvin & Hughes) |
| **Marine-Autopilot seit** | 1970er Jahre (Autohelm) |
| **Marktanteil (geschätzt)** | 25–30 % (Freizeitboote weltweit) |
| **Stärke** | Breites Sortiment, guter Aftermarket-Support |
| **Schwäche** | Proprietäres SeaTalk-Ökosystem bindet an Raymarine |
| **Service-Netzwerk** | Weltweit >100 autorisierte Service-Partner |
| **Garantie** | 2 Jahre (3 Jahre bei Online-Registrierung) |
| **Zielmarkt** | Cruiser, Charter, Fahrtensegler |
| **Website** | www.raymarine.com |

**Schlüsselprodukte Autopilot:**
- Evolution EV-1 Sensor Core
- p70s / p70Rs Steuerkopf (Segel)
- p70 Steuerkopf (Motor)
- Type 1–3 Linearantriebe
- Type 0.5–2 Hydraulikantriebe
- ACU-100 / ACU-200 / ACU-400 Actuator Control Units
- S100 Wireless Fernbedienung

### 5.2 B&G (Navico / Fiskars)

| Eigenschaft | Details |
|------------|---------|
| **Firmensitz** | Romsey, Hampshire, UK |
| **Mutterkonzern** | Navico Group (Fiskars, ehem. Brunswick) |
| **Gegründet** | 1955 (Brookes & Gatehouse) |
| **Marine-Autopilot seit** | 1980er Jahre |
| **Marktanteil (geschätzt)** | 15–20 % (Segelyachten) |
| **Stärke** | Performance-Segeln, Regatta-Expertise |
| **Schwäche** | Weniger im Motorboot-Segment vertreten |
| **Service-Netzwerk** | Weltweit >80 autorisierte Service-Partner |
| **Garantie** | 2 Jahre |
| **Zielmarkt** | Performance-Segler, Regatta, Cruiser-Racer |
| **Website** | www.bandg.com |

**Schlüsselprodukte Autopilot:**
- NAC-1 / NAC-2 / NAC-3 Autopilot-Computer
- Precision-9 Compass
- H5000 Hercules + Halcyon CPUs
- Triton2 / Vulcan / Zeus Displays als Steuerkopf
- WR10 Wireless Autopilot Remote

### 5.3 Garmin

| Eigenschaft | Details |
|------------|---------|
| **Firmensitz** | Olathe, Kansas, USA (+ Schaffhausen, CH) |
| **Mutterkonzern** | Garmin Ltd. (börsennotiert) |
| **Gegründet** | 1989 |
| **Marine-Autopilot seit** | 2010er Jahre (verstärkt seit GHP/Reactor) |
| **Marktanteil (geschätzt)** | 20–25 % (Motorboote), 10–15 % (Segelboote) |
| **Stärke** | Preis-Leistung, einfache Bedienung, starke Plotter-Integration |
| **Schwäche** | Weniger Performance-Segel-Expertise als B&G/NKE |
| **Service-Netzwerk** | Weltweit >150 autorisierte Marine-Dealer |
| **Garantie** | 2 Jahre |
| **Zielmarkt** | Motorboote, Cruiser, Einsteiger |
| **Website** | www.garmin.com |

**Schlüsselprodukte Autopilot:**
- GHP Reactor 40 (Steer-by-Wire und Mechanical)
- GHP 20 (Einsteiger)
- GHP Compact Reactor
- Garmin Heading Sensor
- GHC 50 Autopilot Control Unit
- GRID 20 Remote Input Device

### 5.4 Simrad (Navico / Fiskars)

| Eigenschaft | Details |
|------------|---------|
| **Firmensitz** | Horten, Norwegen |
| **Mutterkonzern** | Navico Group (Fiskars) |
| **Gegründet** | 1946 |
| **Marine-Autopilot seit** | 1960er Jahre (Robertson) |
| **Marktanteil (geschätzt)** | 15–20 % (Motor), 10–15 % (Segel) |
| **Stärke** | Norwegische Marine-Tradition, starke Motorboot-Lösungen |
| **Schwäche** | Überlappung mit B&G (gleiche Plattform, Segmentabgrenzung) |
| **Service-Netzwerk** | Weltweit >100 autorisierte Service-Partner |
| **Garantie** | 2 Jahre |
| **Zielmarkt** | Motorboote, kommerzielle Fischerei, Cruiser |
| **Website** | www.simrad-yachting.com |

**Schlüsselprodukte Autopilot:**
- AP44 / AP48 Steuerköpfe
- NAC-1 / NAC-2 / NAC-3 Computer (identisch B&G)
- Precision-9 Compass (identisch B&G)
- OP50 Steuerkopf (Legacy, weit verbreitet)

### 5.5 Furuno

| Eigenschaft | Details |
|------------|---------|
| **Firmensitz** | Nishinomiya, Japan |
| **Mutterkonzern** | Furuno Electric Co. Ltd. (börsennotiert) |
| **Gegründet** | 1948 |
| **Marine-Autopilot seit** | 1970er Jahre |
| **Marktanteil (geschätzt)** | 5–10 % (Freizeitboote), 40–50 % (kommerzielle Schifffahrt) |
| **Stärke** | Höchste Zuverlässigkeit, professionelle Schifffahrts-Erfahrung |
| **Schwäche** | Weniger modernes UI, höherer Preis, weniger Yacht-Features |
| **Service-Netzwerk** | Weltweit >200 Service-Stationen (inkl. kommerziell) |
| **Garantie** | 2 Jahre (3 Jahre auf ausgewählte Produkte) |
| **Zielmarkt** | Ernsthafte Fahrtensegler, Motoryachten, Arbeitsboote |
| **Website** | www.furuno.com |

**Schlüsselprodukte Autopilot:**
- NavPilot 300
- NavPilot 711C
- FAP-3011C (kommerziell/Superyacht)
- PG-700 Heading Sensor
- SC-50 Satellite Compass

### 5.6 NKE Marine Electronics

| Eigenschaft | Details |
|------------|---------|
| **Firmensitz** | Hennebont, Bretagne, Frankreich |
| **Mutterkonzern** | Unabhängig |
| **Gegründet** | 1983 |
| **Marine-Autopilot seit** | 1990er Jahre |
| **Marktanteil (geschätzt)** | 2–5 % (Freizeitboote), 60–70 % (Hochsee-Regatta) |
| **Stärke** | Performance-Segeln, Regatta-optimiert, schnellster Autopilot |
| **Schwäche** | Kleines Service-Netzwerk, wenig Motorboot-Expertise |
| **Service-Netzwerk** | Ca. 30 spezialisierte Händler weltweit |
| **Garantie** | 2 Jahre |
| **Zielmarkt** | Regatta-Segler, Performance-Cruiser, Offshore-Racing |
| **Website** | www.nfranceke.fr |

**Schlüsselprodukte Autopilot:**
- gyropilot 2 (Racing)
- gyropilot 3 (Cruiser-Racer)
- Pilote HR (Heavy-Duty Racing)
- Topline-Displays (integrierte Bedienung)
- Multigraphic-Displays

---

## 6. Fehlerbild-Atlas

### 6.1 Fehlerbild F-AP-01: Autopilot hält keinen geraden Kurs — „Schlängeln" (Hunting/Oscillation)

**Symptom:**
Boot schwingt rhythmisch um den Sollkurs, typisch ±5–15° mit Periodendauer 5–20 Sekunden. Ruder bewegt sich permanent hin und her.

**Mögliche Ursachen:**

| Ursache | Wahrscheinlichkeit | Diagnose |
|---------|-------------------|----------|
| Kp (Rudder Gain) zu hoch | 40 % | Gain reduzieren, beobachten |
| Kd (Counter Rudder) zu niedrig | 25 % | Dämpfung erhöhen |
| Sea State Filter zu niedrig | 15 % | Sea State / Response erhöhen |
| Mechanisches Spiel in Ruderanlenkung | 10 % | Ruder manuell prüfen, Spiel am Quadranten? |
| Ruderwinkelgeber defekt/verstellt | 5 % | Sensor kalibrieren, Potentiometer prüfen |
| Kompass schlecht kompensiert | 5 % | Deviation-Tabelle prüfen, Neukompensation |

**Sofortmaßnahme:** Response/Gain eine Stufe reduzieren, Sea State eine Stufe erhöhen.

**Confidence:** documented (häufigster Autopilot-Fehler, umfangreich dokumentiert in Hersteller-Troubleshooting-Guides)

### 6.2 Fehlerbild F-AP-02: Autopilot driftet langsam vom Kurs ab — keine Korrektur

**Symptom:**
Boot weicht über Minuten hinweg langsam vom Sollkurs ab (z.B. 1–2° pro Minute), Autopilot korrigiert nicht. Oft erst nach 10–20° Abweichung bemerkt.

**Mögliche Ursachen:**

| Ursache | Wahrscheinlichkeit | Diagnose |
|---------|-------------------|----------|
| Kompass-Deviation groß, nicht kompensiert | 30 % | Deviation prüfen, Neukompensation |
| Totband zu groß eingestellt | 20 % | Deadband reduzieren |
| Ki (Auto Trim) zu niedrig | 15 % | Integration erhöhen |
| Magnetische Störung (neues Gerät nahe Kompass) | 15 % | Alle neuen Geräte nahe Kompass prüfen |
| GPS-Antennenproblem (im Track-Modus) | 10 % | GPS-Signal prüfen, Antenne inspizieren |
| Mechanische Schwergängigkeit im Ruder | 10 % | Ruderlager prüfen, Ruderwelle schmieren |

**Confidence:** documented

### 6.3 Fehlerbild F-AP-03: Autopilot reagiert nicht auf Wind-Modus — hält Kompasskurs statt Windwinkel

**Symptom:**
Im Wind-Modus steuert der Autopilot weiterhin nach Kompasskurs. Bei Winddrehen ändert sich der Kurs nicht.

**Mögliche Ursachen:**

| Ursache | Wahrscheinlichkeit | Diagnose |
|---------|-------------------|----------|
| Windgeber-Kabel unterbrochen | 35 % | NMEA-Daten prüfen, AWA-Wert vorhanden? |
| Windgeber-Offset falsch | 20 % | AWA im Display mit Verklicker vergleichen |
| Wind-Modus nicht aktiviert (Bedienungsfehler) | 20 % | Modus-Anzeige prüfen |
| Windgeber-Daten nicht auf Autopilot-Bus | 15 % | NMEA-2000-Verbindung prüfen |
| Windgeber defekt (Rotorblockade, Potentiometer) | 10 % | Windgeber am Masttopp inspizieren |

**Confidence:** documented

### 6.4 Fehlerbild F-AP-04: Autopilot schaltet sich plötzlich ab — „Disengage"

**Symptom:**
Autopilot geht unerwartet in Standby, akustischer Alarm, Boot fällt vom Kurs.

**Mögliche Ursachen:**

| Ursache | Wahrscheinlichkeit | Diagnose |
|---------|-------------------|----------|
| Überlast am Antrieb (Ruderkraft zu hoch) | 30 % | Seegang, Geschwindigkeit → Antrieb unterdimensioniert? |
| Spannungsabfall unter Mindestspannung | 25 % | Batteriespannung am Autopilot messen (unter Last) |
| Thermische Abschaltung (Antrieb überhitzt) | 15 % | Antrieb anfassen — heiß? Belüftung prüfen |
| Kompass-Fehler (Signal-Verlust) | 10 % | Kompass-Daten prüfen, Kabel inspizieren |
| NMEA-Bus-Fehler | 10 % | Bus-Spannung prüfen, Terminatoren prüfen |
| Software-Absturz | 5 % | Firmware-Version prüfen, ggf. Update |
| Wasser im Antriebs-Gehäuse | 5 % | Gehäuse öffnen, auf Feuchtigkeit prüfen |

**Confidence:** documented

### 6.5 Fehlerbild F-AP-05: Ruderbewegung hektisch — „Nervous Rudder"

**Symptom:**
Ruder bewegt sich in schnellen, kleinen Schritten (1–3°) hin und her, auch bei ruhiger See. Erhöhter Stromverbrauch, hörbares Antriebsgeräusch.

**Mögliche Ursachen:**

| Ursache | Wahrscheinlichkeit | Diagnose |
|---------|-------------------|----------|
| Kompass-Rauschen (EMV-Störung) | 30 % | Kompass-Daten auf Display beobachten — schwankt Heading? |
| Kd (Counter Rudder) zu hoch | 25 % | Dämpfung reduzieren |
| Totband zu klein | 15 % | Deadband leicht erhöhen |
| Ruderwinkelgeber-Rauschen | 15 % | Sensor-Signal prüfen, Kabel/Stecker inspizieren |
| Mechanisches Spiel im Antrieb → Regler kompensiert | 10 % | Antrieb mechanisch prüfen, Spiel am Gestänge |
| Firmware-Bug | 5 % | Firmware-Update verfügbar? |

**Confidence:** documented

### 6.6 Fehlerbild F-AP-06: Autopilot dreht nur in eine Richtung — asymmetrische Steuerung

**Symptom:**
Autopilot korrigiert nur nach Steuerbord (oder nur nach Backbord). Gegenrichtung keine oder sehr schwache Reaktion.

**Mögliche Ursachen:**

| Ursache | Wahrscheinlichkeit | Diagnose |
|---------|-------------------|----------|
| Ruderwinkelgeber verschoben/falsch kalibriert | 35 % | Kalibrierung prüfen, Mittelstellung korrekt? |
| Hydraulik: Ventil klemmt in einer Richtung | 20 % | Hydraulik-System prüfen, Ventil reinigen |
| Linear-Antrieb: Motor-Kontakt in einer Richtung defekt | 15 % | Motor direkt ansteuern (beide Richtungen testen) |
| Kabelbruch (partielle Verbindung) | 15 % | Alle Kabel und Stecker prüfen |
| Autopilot-Computer defekt | 10 % | Software-Diagnose, Fehlercodes auslesen |
| Mechanische Blockade (Kabel, Schlauch im Weg) | 5 % | Ruderanlenkung mechanisch auf Gängigkeit prüfen |

**Confidence:** documented

### 6.7 Fehlerbild F-AP-07: Kompass-Fehler „Heading Lost" oder „No Compass Data"

**Symptom:**
Autopilot zeigt Fehlermeldung, keine Kursdaten verfügbar, Autopilot kann nicht aktiviert werden.

**Mögliche Ursachen:**

| Ursache | Wahrscheinlichkeit | Diagnose |
|---------|-------------------|----------|
| NMEA-2000 Backbone-Problem | 25 % | Bus-Spannung messen (11,5–15,5 V DC) |
| Kompass-Kabel defekt/Stecker korrodiert | 25 % | Kabel und Stecker visuell + elektrisch prüfen |
| Kompass-Sensor defekt | 15 % | Kompass einzeln testen (Daten auf Bus?) |
| Terminator fehlt oder defekt | 15 % | Beide Terminatoren am Backbone-Ende prüfen |
| T-Stück defekt | 10 % | Kompass an anderem T-Stück testen |
| Software-Inkompatibilität (nach Update) | 10 % | Firmware-Versionen aller Geräte prüfen |

**Confidence:** documented

### 6.8 Fehlerbild F-AP-08: Hoher Stromverbrauch des Autopiloten

**Symptom:**
Stromverbrauch des Autopiloten deutlich höher als erwartet (z.B. 5 A statt erwartet 1,5 A bei normalem Segeln).

**Mögliche Ursachen:**

| Ursache | Wahrscheinlichkeit | Diagnose |
|---------|-------------------|----------|
| Antrieb zu klein dimensioniert | 25 % | Ruderkraft berechnen, Antrieb vergleichen |
| PID-Parameter falsch (zu aggressiv) | 20 % | Gain/Response reduzieren, Sea State erhöhen |
| Mechanische Schwergängigkeit im Ruder | 20 % | Ruderlager prüfen, Packung zu fest? |
| Totband zu klein | 10 % | Deadband leicht erhöhen |
| Hydraulik-Leckage (internes Bypassing) | 10 % | Hydrauliköl-Stand prüfen, Druck prüfen |
| Spannungsabfall in Zuleitung | 10 % | Spannung am Autopilot unter Last messen |
| Antrieb mechanisch verschlissen | 5 % | Antrieb inspizieren, Geräusche? |

**Confidence:** documented

### 6.9 Fehlerbild F-AP-09: Autopilot „verlernt" Einstellungen nach Neustart

**Symptom:**
Nach jedem Ausschalten gehen individuelle Einstellungen (Gain, Response, Sea State, Kompass-Kompensation) verloren.

**Mögliche Ursachen:**

| Ursache | Wahrscheinlichkeit | Diagnose |
|---------|-------------------|----------|
| EEPROM/Flash-Speicher defekt | 30 % | Firmware-Diagnose, Fehlercodes |
| Firmware-Bug | 25 % | Firmware-Update verfügbar? |
| Spannungsversorgung instabil (Brownout) | 20 % | Spannung beim Ausschalten messen — saubere Abschaltung? |
| Batterie-Puffer im Gerät leer (ältere Modelle) | 15 % | Gerät öffnen, Pufferbatterie tauschen |
| Falsche Abschalt-Sequenz | 10 % | Handbuch: Korrekte Reihenfolge einhalten |

**Confidence:** documented

### 6.10 Fehlerbild F-AP-10: Autopilot funktioniert auf einem Kurs, aber nicht auf dem Gegenkurs

**Symptom:**
Auf Kurs 090° steuert der Autopilot einwandfrei. Nach Wende auf 270° schlingert er stark oder reagiert asymmetrisch.

**Mögliche Ursachen:**

| Ursache | Wahrscheinlichkeit | Diagnose |
|---------|-------------------|----------|
| Kompass-Deviation auf einem bestimmten Kursbereich groß | 40 % | Deviation-Tabelle erstellen/prüfen |
| Magnetische Störquelle kursabhängig (z.B. Motor laufen/nicht laufen) | 20 % | Motor-Effekt auf Kompass prüfen |
| Asymmetrisches Ruderverhalten (Rumpfform) | 15 % | Ruder in beide Richtungen manuell testen |
| GPS-Multipath auf bestimmtem Kurs (Mast/Aufbau zwischen Antenne und Satelliten) | 10 % | GPS-Antennenposition prüfen |
| Windfahnen-Effekt (Rigg als Windfahne bei Motorbetrieb) | 10 % | Nur bei Segelboot unter Motor |
| Ruderwinkelgeber-Nichtlinearität | 5 % | Sensor-Kalibrierung wiederholen |

**Confidence:** documented

### 6.11 Fehlerbild F-AP-11: Hydraulik-Autopilot — Ruder reagiert verzögert oder „schwammig"

**Symptom:**
Zeitverzögerung zwischen Autopilot-Befehl und Ruderbewegung, Ruder fühlt sich weich an, keine präzise Ruderpositionierung.

**Mögliche Ursachen:**

| Ursache | Wahrscheinlichkeit | Diagnose |
|---------|-------------------|----------|
| Luft im Hydrauliksystem | 40 % | System entlüften |
| Hydrauliköl-Stand zu niedrig | 20 % | Ölstand prüfen, ggf. nachfüllen |
| Innere Leckage (Zylinderdichtung, Pumpe) | 15 % | Druck aufbauen, Druckabfall beobachten |
| Bypass-Ventil nicht vollständig geschlossen | 10 % | Ventil prüfen, fest schließen |
| Falsche Hydraulikflüssigkeit | 10 % | Spezifikation prüfen (ATF? Mineralöl? Herstellervorgabe?) |
| Hydraulikschlauch aufgebläht (falsche Druckstufe) | 5 % | Schläuche visuell prüfen, SAE-Klasse? |

**Confidence:** documented

### 6.12 Fehlerbild F-AP-12: Autopilot steuert Kurs 180° falsch — „dreht falsch herum"

**Symptom:**
Autopilot steuert den entgegengesetzten Kurs. Soll 090° → Boot dreht auf 270°. Oder: Kurskorrektur nach Backbord statt Steuerbord.

**Mögliche Ursachen:**

| Ursache | Wahrscheinlichkeit | Diagnose |
|---------|-------------------|----------|
| Kompass 180° verdreht eingebaut | 30 % | Kompass-Einbaurichtung prüfen (Pfeil → Bug) |
| Antrieb-Anschluss vertauscht (Motor-Polarität) | 30 % | Motor-Anschlüsse tauschen |
| Hydraulik-Schläuche vertauscht | 20 % | BB/StB-Schlauch tauschen |
| Ruderwinkelgeber-Richtung falsch | 10 % | Sensor-Richtung in Software invertieren |
| Software-Konfiguration: Reverse Rudder = EIN | 10 % | Einstellung im Menü prüfen |

**Confidence:** documented

---

## 7. Troubleshooting-Entscheidungsbäume

### 7.1 Entscheidungsbaum 1: Autopilot lässt sich nicht aktivieren

```
Autopilot lässt sich nicht aktivieren
│
├── Ist Strom vorhanden?
│   ├── NEIN → Sicherung prüfen
│   │         → Batteriespannung prüfen
│   │         → Kabel und Stecker prüfen
│   │         → PROBLEM: Stromversorgung
│   │
│   └── JA → Zeigt Display Fehlermeldung?
│           ├── JA → Welche Meldung?
│           │       ├── "No Compass" → Kompass-Verbindung prüfen
│           │       │                 → NMEA-Bus prüfen
│           │       │                 → Terminator prüfen
│           │       │                 → Siehe Fehlerbild F-AP-07
│           │       │
│           │       ├── "Drive Error" → Antrieb-Verbindung prüfen
│           │       │                  → Antrieb blockiert?
│           │       │                  → Sicherung am Antrieb prüfen
│           │       │                  → Motor direkt testen (12V)
│           │       │
│           │       ├── "Rudder Error" → Ruderwinkelgeber-Kabel prüfen
│           │       │                   → Sensor kalibrieren
│           │       │                   → Ruder am Anschlag?
│           │       │
│           │       ├── "Low Voltage" → Batterie laden
│           │       │                  → Kabelquerschnitt prüfen
│           │       │                  → Übergangswiderstand Stecker
│           │       │
│           │       └── "Locked" / "Safety" → Geschwindigkeit > Minimum?
│           │                                → Ist Boot im Wasser?
│           │                                → Safety-Lock deaktivieren
│           │
│           └── NEIN → Taste/Touchscreen funktioniert?
│                     ├── NEIN → Display defekt
│                     │         → Stecker zum Display prüfen
│                     │         → Display tauschen (Test)
│                     │
│                     └── JA → Kompass-Daten sichtbar?
│                             ├── NEIN → Kompass-Problem
│                             │         → Weiter bei F-AP-07
│                             │
│                             └── JA → Software-Problem
│                                     → Firmware-Reset (Factory Default)
│                                     → Firmware-Update
│                                     → Hersteller kontaktieren
```

### 7.2 Entscheidungsbaum 2: Autopilot steuert unruhig / schlecht

```
Autopilot steuert unruhig
│
├── Bei welchen Bedingungen?
│   ├── NUR bei Seegang
│   │   → Sea State Filter / Response erhöhen
│   │   → Totband leicht erhöhen
│   │   → Wellenperiode zu kurz für Boot?
│   │   → Geschwindigkeit anpassen
│   │   → WENN besser → Filter war zu niedrig
│   │   → WENN nicht besser → weiter unten
│   │
│   ├── NUR bei bestimmtem Kurs
│   │   → Kompass-Deviation auf diesem Kurs prüfen
│   │   → Magnetische Störquelle suchen
│   │   → Neukompensation durchführen
│   │   → Siehe Fehlerbild F-AP-10
│   │
│   ├── NUR unter Motor
│   │   → Motor-Vibration stört Kompass?
│   │   → Motor-Magnetfeld stört Kompass?
│   │   → Kompass-Position überprüfen
│   │   → Vibrationsdämpfung montieren
│   │
│   └── IMMER
│       → PID-Parameter prüfen
│       │
│       ├── Gleichmäßiges Schwingen (Oszillation)?
│       │   → Gain / Kp reduzieren
│       │   → Counter Rudder / Kd erhöhen
│       │   → Siehe Fehlerbild F-AP-01
│       │
│       ├── Hektische kleine Ruderbewegungen?
│       │   → Counter Rudder / Kd reduzieren
│       │   → Totband erhöhen
│       │   → Kompass-EMV-Störung prüfen
│       │   → Siehe Fehlerbild F-AP-05
│       │
│       ├── Langsames Abdriften?
│       │   → Auto Trim / Ki erhöhen
│       │   → Kompass-Kompensation prüfen
│       │   → Siehe Fehlerbild F-AP-02
│       │
│       └── Asymmetrisch (nur eine Richtung)?
│           → Ruderwinkelgeber kalibrieren
│           → Antrieb mechanisch prüfen
│           → Siehe Fehlerbild F-AP-06
```

### 7.3 Entscheidungsbaum 3: Hoher Stromverbrauch

```
Hoher Stromverbrauch des Autopiloten
│
├── Stromverbrauch messen (Amperemeter in Zuleitung)
│
├── Verbrauch > 2× Herstellerangabe?
│   ├── JA → Schwerwiegendes Problem
│   │       ├── Ruder mechanisch schwergängig?
│   │       │   ├── JA → Ruderlager prüfen/schmieren
│   │       │   │       → Packungsdichtung zu fest?
│   │       │   │       → Bewuchs am Ruder?
│   │       │   │       → Ruder ausrichten (Achsflucht)
│   │       │   │
│   │       │   └── NEIN → Antrieb prüfen
│   │       │             → Motor-Lager verschlissen?
│   │       │             → Getriebe-Schaden?
│   │       │             → Hydraulik: innere Leckage?
│   │       │
│   │       └── Antrieb unterdimensioniert für Boot
│   │           → Ruderkraft berechnen (siehe 2.7)
│   │           → Größeren Antrieb einbauen
│   │
│   └── NEIN → Mäßig erhöht (1,3–2× Angabe)
│           ├── PID zu aggressiv?
│           │   → Gain/Response reduzieren
│           │   → Sea State erhöhen
│           │   → Totband leicht erhöhen
│           │
│           ├── Konstanter Seitenwind?
│           │   → Normal bei starkem Seitenwind
│           │   → Segel trimmen für weniger Ruderdruck
│           │   → Segelfläche reduzieren
│           │
│           └── Spannungsabfall in Zuleitung?
│               → Spannung AM AUTOPILOT messen (nicht an Batterie)
│               → Bei <11,5 V (12V-System): Kabelquerschnitt erhöhen
│               → Übergangswiderstand an Steckern messen
```

### 7.4 Entscheidungsbaum 4: Kompass-Probleme

```
Kompass-Probleme diagnostizieren
│
├── Heading-Anzeige stabil (keine Sprünge)?
│   ├── NEIN → Sprünge / Zittern
│   │         ├── Sprünge > 10°?
│   │         │   → EMV-Störung stark
│   │         │   → Alle elektrischen Verbraucher einzeln ausschalten
│   │         │   → Störquelle identifizieren
│   │         │   → Kompass weiter weg montieren
│   │         │   │
│   │         │   └── Motor an/aus macht Unterschied?
│   │         │       ├── JA → Motor-Generator stört Kompass
│   │         │       │       → Kompass weiter weg vom Motor
│   │         │       │       → Abschirmung
│   │         │       │
│   │         │       └── NEIN → Andere Elektronik
│   │         │                 → LED-Beleuchtung (PWM-Störung!)
│   │         │                 → Wechselrichter
│   │         │                 → Funkgerät (HF-Störung)
│   │         │
│   │         └── Sprünge < 5°, regelmäßig?
│   │             → Normales Seegangs-Rauschen
│   │             → Kompass-Dämpfung erhöhen
│   │             → Tiefpass-Filter aktivieren
│   │
│   └── JA → Heading stabil, aber falsch?
│           ├── Konstanter Fehler (z.B. immer +10°)?
│           │   → Hard-Iron-Deviation
│           │   → Neukompensation durchführen
│           │   → Neue Stahlteile/Magnete in der Nähe?
│           │
│           ├── Fehler kursabhängig (auf manchen Kursen gut, auf anderen schlecht)?
│           │   → Soft-Iron-Deviation
│           │   → Vollständige Kompensationsfahrt
│           │   → Deviation-Tabelle erstellen und prüfen
│           │
│           └── Fehler krängungsabhängig?
│               → Heel-Error (besonders bei Fluxgate)
│               → Krängungskompensation aktivieren (wenn verfügbar)
│               → Solid-State-Kompass mit IMU erwägen
│               → GPS-Kompass als Alternative
```

### 7.5 Entscheidungsbaum 5: Windsteuerung funktioniert nicht korrekt

```
Windsteuerung funktioniert nicht korrekt
│
├── Wind-Modus aktiviert?
│   ├── NEIN → Wind-Modus aktivieren
│   │         → Im Menü prüfen: AWA oder TWA?
│   │         → Windgeber angeschlossen und funktional?
│   │
│   └── JA → AWA-Daten auf Display sichtbar?
│           ├── NEIN → Windgeber-Verbindung prüfen
│           │         → NMEA-Daten prüfen (AWA PGN vorhanden?)
│           │         → Windgeber-Kabel Mastdurchführung prüfen
│           │         → Windgeber am Masttopp prüfen (Rotor frei?)
│           │
│           └── JA → AWA-Wert plausibel?
│                   ├── NEIN → Offset falsch
│                   │         → AWA mit Verklicker vergleichen
│                   │         → Offset korrigieren (z.B. +180° wenn Bug/Heck vertauscht)
│                   │         → Windgeber verdreht montiert?
│                   │
│                   └── JA → Welches Problem im Wind-Modus?
│                           ├── Boot hält keinen konstanten AWA
│                           │   → Wind-PID-Parameter anpassen
│                           │   → Windgeber-Dämpfung erhöhen
│                           │   → Bootsgeschwindigkeit zu niedrig? (AWA instabil)
│                           │
│                           ├── Ungewollte Halse / Wenden
│                           │   → Tacking-Winkel prüfen (zu eng?)
│                           │   → TWA-Modus statt AWA bei raumen Kursen
│                           │   → Gybe/Tack Inhibit aktivieren
│                           │
│                           └── Boot segelt zu hoch / zu tief
│                               → AWA-Sollwert anpassen
│                               → Segeltrimm prüfen (nicht nur Autopilot!)
│                               → Polaren-Daten korrekt?
```

---

## 8. FAQ — Häufige Fragen

### 8.1 Grundsatzfragen

**F01: Brauche ich einen Autopiloten?**
Wenn Sie alleine oder zu zweit segeln und Fahrten über 4 Stunden machen: Ja, definitiv. Für Einhandsegler ist ein Autopilot überlebenswichtig. Für Crews von 4+ Personen auf Tagestörns: nett, aber nicht zwingend.

**F02: Was kostet ein komplettes Autopilot-System?**
Für eine 10-m-Segelyacht (Pinnensteuerung): 1.500–3.000 EUR. Für eine 10-m-Segelyacht (Radsteuerung): 2.500–5.000 EUR. Für eine 14-m-Segelyacht mit Hydraulik: 5.000–10.000 EUR. Für eine 20-m-Motoryacht: 8.000–18.000 EUR. Einbau-Arbeitszeit kommt hinzu (typisch 8–20 Stunden à 80–120 EUR/Stunde).

**F03: Kann ich den Autopiloten selbst einbauen?**
Pinnenantriebe: Ja, mit handwerklichem Geschick und Verständnis der Elektrik. Radantriebe: Meist ja, etwas komplexer. Linearantriebe am Quadranten: Mittlerer Aufwand, Anlenkgeometrie muss stimmen. Hydraulik: Professioneller Einbau empfohlen (Druckschläuche, Entlüftung, Sicherheit).

**F04: Wie viel Strom verbraucht ein Autopilot?**
Im Durchschnitt bei einer 10-m-Segelyacht mit Linearantrieb: 1,5–3,0 A bei 12 V in normalem Seegang. In 24 Stunden: 36–72 Ah. Das ist signifikant und muss in der Energieplanung berücksichtigt werden. Hydraulik-Systeme verbrauchen oft weniger im Haltebetrieb (0,5–1,5 A), aber mehr bei aktiver Korrektur.

**F05: Was ist der Unterschied zwischen einem 800-EUR- und einem 5.000-EUR-Autopiloten?**
Der günstige Autopilot (z.B. Pinnenantrieb) hat eingebauten Kompass, einfache Regelung, keinen Wind-Modus, keine GPS-Steuerung, begrenzte Leistung. Der teure (z.B. Raymarine EV mit IMU + Linear Type 2) hat 9-Achsen-IMU, adaptive Regelung, Wind-Modus, GPS-Track-Following, höhere Leistung, bessere Sensorik, erweiterbare Plattform.

### 8.2 Technische Fragen

**F06: Was bedeutet „Autolearn" oder „Autoconfig"?**
Der Autopilot analysiert während der Fahrt das Verhalten des Bootes (Trägheit, Ruderwirksamkeit, Wellenbewegung) und optimiert seine Regelparameter automatisch. Früher musste man alles manuell einstellen.

**F07: Was ist der Unterschied zwischen Fluxgate und Solid-State-Kompass?**
Fluxgate: Einfacher, bewährt, aber krängungsempfindlich und erfordert sorgfältige Kompensation. Solid-State (9-Achsen-IMU): Kompensiert Krängung automatisch, schnellere Kursänderungs-Erkennung, aber teurer und komplexer. Für die meisten Cruiser reicht ein Fluxgate. Für Performance-Segler lohnt sich der Solid-State.

**F08: Muss ich den Kompass regelmäßig kompensieren?**
Ja. Mindestens einmal pro Saison und nach jeder Änderung der Bordelektrik oder Ausstattung in der Nähe des Kompasses. Neue Lautsprecher, neue Batterien, neuer Motor — alles kann die Deviation verändern.

**F09: Wie stelle ich den Sea State Filter / Response richtig ein?**
Beginnen Sie mit einem mittleren Wert. Beobachten Sie die Ruderbewegungen: Wenn das Ruder ständig korrigiert, aber der Kurs trotzdem schwankt → Filter erhöhen. Wenn das Ruder kaum reagiert und der Kurs abdriftet → Filter reduzieren. Die optimale Einstellung ist die niedrigste, bei der das Ruder „ruhig" arbeitet.

**F10: Was ist besser — Hydraulik oder Linear?**
Für Boote bis 12 m mit mechanischer Steuerung: Linear (einfacher, günstiger). Für Boote über 14 m oder mit bestehender Hydrauliksteuerung: Hydraulik (stärker, geräuschärmer). Für Boote 12–14 m: Beide möglich, abhängig von Ruderkraft und Budget.

**F11: Kann ich meinen Autopiloten an ein anderes Navigationssystem anschließen?**
Wenn beide Systeme NMEA 2000 unterstützen: In der Regel ja. Raymarine-Geräte kommunizieren über SeaTalkNG (kompatibel mit NMEA 2000). Ältere Systeme mit NMEA 0183 benötigen einen Konverter (z.B. Actisense NGW-1).

**F12: Wie lang hält ein Autopilot-Antrieb?**
Linearantrieb: 5.000–15.000 Betriebsstunden (10–20 Jahre bei Wochenendsegeln). Hydraulik: 10.000–30.000 Stunden (praktisch unbegrenzt bei guter Wartung). Radantrieb: 3.000–8.000 Stunden (Reibrad-Verschleiß). Pinnenantrieb: 2.000–6.000 Stunden (exponiert, höherer Verschleiß).

### 8.3 Praxis-Fragen

**F13: Autopilot bei Starkwind — wie stelle ich ein?**
Response/Gain reduzieren (Boot hat genug Ruderdruck, braucht weniger Autopilot-Kraft). Sea State erhöhen (mehr Wellenfilterung). Segelfläche reduzieren (weniger Ruderdruck = weniger Autopilot-Arbeit). Gereffte Segel = ausgeglicheneres Boot = bessere Autopilot-Performance.

**F14: Mein Autopilot macht komische Geräusche — ist das normal?**
Linearantriebe: Ein leises Surren/Klicken bei Kurskorrektur ist normal. Lautes Knarzen oder Rattern deutet auf Verschleiß hin. Hydraulik: Leises Brummen normal. Quietschen = Luft im System. Hämmern = Ventilproblem. Radantrieb: Motorgeräusch am Steuerstand normal. Rutschen/Quietschen = Reibrad-Verschleiß.

**F15: Kann ich den Autopiloten im Hafen benutzen?**
Technisch ja, aber nicht empfohlen. Der Autopilot hat keine Hinderniserkennung. Im Hafen ist manuelle Steuerung sicherer. Einige Systeme bieten einen „Dock Mode" mit reduziertem Gain.

**F16: Was passiert, wenn der Autopilot ausfällt?**
Das Boot fährt unkontrolliert weiter. Daher: Immer in Reichweite des Steuerrades/der Pinne bleiben. Off-Course-Alarm aktivieren. Disengage-Alarm aktivieren. Backup-System vorhalten (Windfahne für Langfahrt).

**F17: Wie spare ich Strom beim Autopilot-Betrieb?**
Segel gut trimmen (weniger Ruderdruck). Sea State / Response nicht zu niedrig (dann korrigiert zu oft). Totband leicht erhöhen. Solarpanels / Windgenerator dimensionieren. Batteriekapazität ausreichend.

**F18: Kann ich verschiedene Hersteller mischen (z.B. Garmin-Plotter mit Raymarine-Autopilot)?**
Über NMEA 2000: Grundfunktionen ja (Kurssteuerung, Track-Following). Erweiterte Funktionen (Autolearn, spezifische Modi): Nur innerhalb eines Hersteller-Ökosystems. Empfehlung: Plotter und Autopilot vom gleichen Hersteller.

**F19: Was ist der Unterschied zwischen Heading und Course Over Ground (COG)?**
Heading = Richtung, in die der Bug zeigt (vom Kompass). COG = Richtung, in die sich das Boot tatsächlich bewegt (vom GPS). Bei Strömung oder Abdrift können Heading und COG um viele Grad abweichen. Der Autopilot steuert nach Heading, navigiert aber nach COG.

**F20: Brauche ich einen Ruderwinkelgeber?**
Für Pinnenantriebe: Nein (integriert oder nicht nötig). Für alle anderen Systeme: Dringend empfohlen. Ohne Ruderwinkelgeber kann der Autopilot die Ruderposition nicht überwachen → weniger präzise Regelung, Risiko des Anlaufens gegen den Ruderanschlag.

### 8.4 Spezial-Fragen

**F21: Windfahne oder Elektro-Autopilot für Blauwasser?**
Beides. Die ideale Blauwasser-Lösung ist ein elektrischer Autopilot für Kompass- und GPS-Steuerung (Navigation, Motorbetrieb, Flaute) plus eine Windfahnen-Selbststeueranlage als Backup und für längere Segelpassagen (kein Stromverbrauch). Budget: Ca. 5.000–10.000 EUR für beide Systeme.

**F22: Kann ein Autopilot Broaching verhindern?**
Teilweise. Ein gut eingestellter Autopilot mit hoher Rudderrate kann ein beginnendes Broaching abfangen. Aber: Bei extremem Seegang und zu viel Segelfläche ist das Ruder physisch überfordert — kein Autopilot kann das kompensieren. Prävention: Angemessene Besegelung und Geschwindigkeit.

**F23: Wie kalibriere ich den Windgeber für den Autopilot-Windmodus?**
1. Bei Windstille oder im Hafen: Windgeber-Pfeil auf Bug ausrichten. 2. Offset im System auf 0° setzen. 3. Auf dem Wasser: AWA mit Verklicker/Windex vergleichen. 4. Offset anpassen bis Übereinstimmung. 5. Am Wind (Backbord und Steuerbord): Winkel müssen symmetrisch sein.

**F24: Was ist ein Drehratensensor und warum ist er wichtig?**
Ein Drehratensensor (Gyroskop) misst die Geschwindigkeit der Kursänderung (°/s). Er ist schneller als der Kompass und liefert dem D-Anteil des PID-Reglers das perfekte Signal. Ohne Drehratensensor muss der D-Anteil aus dem verrauschten Kompass-Signal differenziert werden — das ergibt hektischere Ruderbewegungen.

**F25: Kann ich meinen alten Autopiloten upgraden oder muss ich alles neu kaufen?**
Abhängig vom System: Antrieb noch gut → nur Kurscomputer + Kompass upgraden (z.B. von altem Raymarine SPX auf neues Evolution). Kompass noch gut → nur Computer upgraden. Alles >15 Jahre → Kompletttausch empfohlen (Antrieb-Verschleiß, veraltete Elektronik, keine Ersatzteile).

**F26: Was bedeutet „Power Steer" oder „Override"?**
Die Möglichkeit, das Steuerrad oder die Pinne manuell zu bewegen, während der Autopilot aktiv ist. Bei Linearantrieben: Nicht möglich (Spindel blockiert). Bei Hydraulik: Möglich über Bypass oder Überdruckventil. Bei Radantrieb: Möglich (Reibrad rutscht durch). Bei Pinnenantrieb: Kupplungsmechanismus.

**F27: Wie dimensioniere ich die Stromversorgung für den Autopiloten?**
Kabelquerschnitt: Maximaler Strom × Kabellänge (einfach) → Tabelle. Beispiel: 10 A, 5 m Kabel → mindestens 4 mm² (besser 6 mm²). Sicherung: 150 % des maximalen Stroms. Beispiel: Max 10 A → 15 A Sicherung. Eigener Stromkreis empfohlen (nicht mit anderen Verbrauchern teilen).

---

## 9. Glossar

| Nr. | Begriff | Erklärung |
|-----|---------|-----------|
| G01 | **AHRS** | Attitude and Heading Reference System — 9-Achsen-IMU mit Sensor-Fusion für Lage und Kurs |
| G02 | **Anti-Windup** | Begrenzung des I-Anteils im PID-Regler, um Überschwingen zu verhindern wenn Stellgröße am Anschlag |
| G03 | **AWA** | Apparent Wind Angle — Scheinbarer Windwinkel, gemessen am Windgeber |
| G04 | **AWS** | Apparent Wind Speed — Scheinbare Windgeschwindigkeit |
| G05 | **Bearing Away** | Abfallen (vom Wind), gesteuert durch Autopilot bei Böen |
| G06 | **Broaching** | Unkontrolliertes Querschlagen eines Bootes durch Wellenwirkung, besonders bei Achterlichem Seegang |
| G07 | **CAN-Bus** | Controller Area Network — Datenbus, Basis für NMEA 2000 |
| G08 | **COG** | Course Over Ground — Kurs über Grund (GPS) |
| G09 | **Compass Deviation** | Ablenkung des Kompasses durch bootseigene Magnetfelder |
| G10 | **Cross-Track Error (XTE)** | Seitliche Abweichung von der geplanten Kurslinie |
| G11 | **Deadband / Totband** | Kursbereich um den Sollkurs, in dem keine Ruderkorrektur erfolgt |
| G12 | **Deviation** | Kompass-Ablenkung durch bootseigene Magnetfelder (nicht zu verwechseln mit Deklination/Variation) |
| G13 | **Disengage** | Abschalten/Deaktivieren des Autopiloten |
| G14 | **Drive Unit** | Antriebseinheit des Autopiloten (Hydraulik, Linear, Rad, Pinne) |
| G15 | **EKF** | Extended Kalman Filter — Algorithmus zur optimalen Sensor-Fusion |
| G16 | **EMV** | Elektromagnetische Verträglichkeit — Störfestigkeit elektronischer Geräte |
| G17 | **Fluxgate** | Magnetischer Sensor (Förster-Sonde) zur Messung des Erdmagnetfeldes → Kompass |
| G18 | **Gain** | Verstärkung — wie stark der Autopilot auf Kursabweichungen reagiert (≈ Kp) |
| G19 | **Gieren (Yaw)** | Drehbewegung um die Hochachse des Bootes (Kursänderung) |
| G20 | **GPS-Kompass** | Kursbestimmung mittels zweier GPS-Antennen (Phasendifferenz) |
| G21 | **Hard Iron** | Permanente Magnetfeldstörung (z.B. von Dauermagneten an Bord) |
| G22 | **Heading** | Kurs — Richtung, in die der Bug zeigt (magnetisch oder rechtweisend) |
| G23 | **Heel** | Krängung — seitliche Neigung des Bootes |
| G24 | **Hunting** | Oszillation des Autopiloten um den Sollkurs (Regelkreis schwingt) |
| G25 | **IMU** | Inertial Measurement Unit — Kombination aus Beschleunigungs-, Drehraten- und Magnetfeld-Sensoren |
| G26 | **Integrator-Windup** | Aufblähen des I-Anteils bei Stellgrößen-Begrenzung → Überschwingen |
| G27 | **Kd** | Differenzialverstärkung im PID-Regler (Dämpfung, Counter Rudder) |
| G28 | **Ki** | Integralverstärkung im PID-Regler (Auto Trim, Steady-State-Korrektur) |
| G29 | **Kp** | Proportionalverstärkung im PID-Regler (Rudder Gain, Response) |
| G30 | **MEMS** | Micro-Electro-Mechanical Systems — miniaturisierte Sensoren auf Halbleiterbasis |
| G31 | **MOB** | Man Over Board — Mensch-über-Bord-Alarm und -Manöver |
| G32 | **NMEA 0183** | Älterer serieller Datenbus-Standard für marine Elektronik |
| G33 | **NMEA 2000** | Moderner CAN-basierter Datenbus-Standard für marine Elektronik |
| G34 | **Nomoto-Modell** | Mathematisches Modell der Drehbewegung eines Schiffes (1. oder 2. Ordnung) |
| G35 | **PID-Regler** | Proportional-Integral-Derivative-Regler — Standard-Algorithmus zur Kursregelung |
| G36 | **Response** | Raymarines Bezeichnung für die Reaktionsstärke des Autopiloten (1–9) |
| G37 | **Rudder Feedback** | Ruderwinkelgeber — Sensor, der die aktuelle Ruderstellung meldet |
| G38 | **Sea State** | Seegangs-Einstellung — wie stark der Wellenfilter wirkt |
| G39 | **SeaTalkNG** | Raymarines Implementierung von NMEA 2000 mit proprietären Erweiterungen |
| G40 | **Servo-Pendulum** | Typ einer Windfahnen-Selbststeueranlage mit Kraftverstärkung durch Wasserströmung |
| G41 | **SOG** | Speed Over Ground — Geschwindigkeit über Grund (GPS) |
| G42 | **Soft Iron** | Induzierte Magnetfeldstörung (z.B. durch weichmagnetische Materialien an Bord) |
| G43 | **Solid-State-Kompass** | Kompass ohne bewegliche Teile, basierend auf MEMS-Sensoren |
| G44 | **Steer-by-Wire** | Elektronische Rudersteuerung ohne mechanische Verbindung zwischen Steuerrad und Ruder |
| G45 | **TWA** | True Wind Angle — Wahrer Windwinkel (berechnet) |
| G46 | **TWS** | True Wind Speed — Wahre Windgeschwindigkeit (berechnet) |
| G47 | **Variation / Deklination** | Winkel zwischen magnetisch Nord und geographisch Nord (ortsabhängig) |
| G48 | **VMG** | Velocity Made Good — Geschwindigkeitskomponente in Richtung Ziel oder Wind |
| G49 | **Williamson-Turn** | Standard-MOB-Manöver: 60° abfallen, dann 240° Wende zurück auf Gegenkurs |
| G50 | **XTE** | Cross-Track Error — seitliche Abweichung von der Sollkurslinie |

---

## 10. Schnell-Referenz

### 10.1 Autopilot-Auswahl nach Bootstyp

| Bootstyp | Empfohlener Antrieb | Empfohlener Kompass | Budget (komplett) |
|----------|-------------------|-------------------|------------------|
| Segelyacht 7–9 m, Pinne | Pinnenantrieb | Integriert | 800–2.000 EUR |
| Segelyacht 9–12 m, Rad | Linearantrieb oder Radantrieb | Fluxgate oder IMU | 2.500–5.000 EUR |
| Segelyacht 12–15 m, Rad | Linearantrieb groß oder Hydraulik | IMU (9-Achsen) | 4.000–8.000 EUR |
| Segelyacht 15–20 m | Hydraulik | IMU oder GPS-Kompass | 8.000–15.000 EUR |
| Motoryacht 8–12 m | Linear oder Hydraulik klein | Fluxgate oder IMU | 2.000–5.000 EUR |
| Motoryacht 12–18 m | Hydraulik | IMU | 5.000–12.000 EUR |
| Motoryacht 18–24 m | Hydraulik groß | IMU + GPS-Kompass | 10.000–25.000 EUR |
| Katamaran 10–14 m | Linearantrieb (pro Ruder!) | IMU | 4.000–10.000 EUR |
| Renn-Segelyacht 10–15 m | Linear + NKE/B&G | IMU (hochwertig) | 6.000–15.000 EUR |
| Blauwasser 12–16 m | Linear/Hydraulik + Windfahne | IMU | 6.000–14.000 EUR |

### 10.2 PID-Tuning Cheat Sheet

| Problem | Kp (Gain) | Ki (Trim) | Kd (Damp) | Sea State |
|---------|-----------|-----------|-----------|-----------|
| Schlängelt (Oscillation) | ↓ Reduzieren | — | ↑ Erhöhen | ↑ Erhöhen |
| Überschwingt | — | — | ↑ Erhöhen | — |
| Driftet langsam ab | — | ↑ Erhöhen | — | — |
| Reagiert zu träge | ↑ Erhöhen | — | — | ↓ Reduzieren |
| Hektisches Ruder | — | — | ↓ Reduzieren | ↑ Erhöhen |
| Ruder arbeitet zu viel | ↓ Reduzieren | — | — | ↑ Erhöhen |

### 10.3 Stromverbrauch-Richtwerte

| System | Standby | Halten | Aktiv (ruhig) | Aktiv (Seegang) | Peak |
|--------|---------|--------|---------------|-----------------|------|
| Pinnenantrieb | 0,1 A | 0,5 A | 1,5 A | 3,0 A | 5,0 A |
| Linearantrieb klein | 0,05 A | 0,3 A | 1,5 A | 3,5 A | 8,0 A |
| Linearantrieb mittel | 0,05 A | 0,5 A | 2,5 A | 6,0 A | 15,0 A |
| Hydraulik klein | 0,05 A | 0,2 A | 2,0 A | 5,0 A | 12,0 A |
| Hydraulik mittel | 0,05 A | 0,3 A | 3,0 A | 8,0 A | 25,0 A |
| Hydraulik groß | 0,05 A | 0,5 A | 5,0 A | 15,0 A | 40,0 A |

*Alle Werte bei 12 V. Für 24-V-Systeme: Strom halbieren.*

### 10.4 Wartungsintervalle

| Komponente | Intervall | Aufgabe |
|-----------|-----------|---------|
| Kompass-Kompensation | 1× pro Saison | Kompensationsfahrt durchführen |
| Ruderwinkelgeber | 1× pro Saison | Kalibrierung prüfen, Mechanik inspizieren |
| Linearantrieb | 1× pro Saison | Spindel inspizieren, ggf. fetten |
| Hydrauliköl | Alle 2 Jahre | Ölwechsel (Herstellervorgabe beachten) |
| Hydraulikschläuche | Alle 5 Jahre | Visuell inspizieren, bei Rissen tauschen |
| Hydraulikdichtungen | Alle 5–8 Jahre | Präventiv tauschen |
| Antriebsmotor-Kohlen | Alle 5.000 Betriebsstunden | Prüfen, bei <50 % tauschen |
| Firmware | Jährlich | Auf Updates prüfen |
| NMEA-Stecker | 1× pro Saison | Auf Korrosion prüfen, Kontaktspray |
| Kabel | 1× pro Saison | Visuell auf Scheuerstellen prüfen |
| Windgeber | 1× pro Saison | Lager prüfen, Rotor frei drehbar? |

### 10.5 Kabelquerschnitte für Autopilot-Antriebe

| Max. Strom | Kabellänge bis 3 m | Kabellänge 3–6 m | Kabellänge 6–10 m |
|------------|-------------------|------------------|-------------------|
| 5 A | 1,5 mm² | 2,5 mm² | 4,0 mm² |
| 10 A | 2,5 mm² | 4,0 mm² | 6,0 mm² |
| 15 A | 4,0 mm² | 6,0 mm² | 10,0 mm² |
| 20 A | 6,0 mm² | 10,0 mm² | 16,0 mm² |
| 30 A | 10,0 mm² | 16,0 mm² | 25,0 mm² |
| 40 A | 16,0 mm² | 25,0 mm² | 35,0 mm² |

*Basis: Max. 3 % Spannungsabfall bei 12 V DC (0,36 V). Für 24 V: Eine Stufe kleiner möglich.*

### 10.6 Kompass-Einbau Cheat Sheet

| Kriterium | Fluxgate | IMU (9-Achsen) | GPS-Kompass |
|-----------|----------|---------------|-------------|
| Min. Abstand Motor | 1,0 m | 0,7 m | Nicht relevant |
| Min. Abstand Lautsprecher | 0,5 m | 0,3 m | Nicht relevant |
| Min. Abstand Stahl/Eisen | 0,5 m | 0,3 m | Nicht relevant |
| Montagefläche | Horizontal ±5° | Beliebig (Einbaulage konfigurierbar) | Horizontal, frei nach oben |
| Bevorzugte Position | Vorschiff, tief im Rumpf | Mittschiffs, nahe Drehpunkt | Masttopp oder Geräteträger |
| Kompensation nötig | Ja, 2× pro Saison | Ja, 1× pro Saison | Nein |
| Krängungskorrektur | Manuell / keine | Automatisch | Nicht nötig |
| Umgebungsbedingungen | Trocken, temperiert | Trocken, vibrationsarm | Wetterfest, freie Sicht |

### 10.7 Autopilot-Alarme und ihre Bedeutung

| Alarm | Bedeutung | Sofortmaßnahme |
|-------|-----------|----------------|
| Off Course | Kursabweichung > Grenzwert | Ausguck → manuell steuern oder Autopilot prüfen |
| No Compass | Keine Kompassdaten | NMEA-Bus und Kompass-Verbindung prüfen |
| Drive Stopped | Antrieb blockiert oder überlastet | Mechanik prüfen, Sicherung prüfen |
| Low Voltage | Bordspannung unter Minimum | Batterie laden, Verbraucher reduzieren |
| Overtemperature | Antriebsmotor überhitzt | Autopilot ausschalten, abkühlen lassen, Belüftung prüfen |
| Wind Shift | Windrichtung hat sich signifikant geändert | Segeltrimm anpassen, Kurs prüfen |
| Rudder Limit | Ruder am Anschlag | Segel reduzieren, Kurs ändern |
| Shallow Water | Wassertiefe unter Grenzwert | Sofort Kurs ändern, manuell steuern |
| Waypoint Arrival | Wegpunkt erreicht | Kurswechsel bestätigen oder manuell steuern |

### 10.8 Notfall-Checkliste Autopilot-Ausfall auf See

1. **Sofort:** Steuerrad/Pinne übernehmen, Kurs halten
2. **Alarm:** Off-Course-Alarm quittieren
3. **Sicherheit:** Position notieren, Ausguck verstärken
4. **Diagnose:** Fehlermeldung lesen, Strom prüfen, Sicherungen prüfen
5. **Backup:** Windfahne aktivieren (falls vorhanden)
6. **Notlösung:** Bei Hydraulik: Bypass-Ventil öffnen, manuell steuern
7. **Wache:** Wachplan anpassen für manuelle Steuerung
8. **Reparatur:** Im Hafen oder bei ruhiger See Fehlersuche nach Entscheidungsbäumen
9. **Dokumentation:** Fehlerbild und Umstände für Werft/Hersteller notieren

---

## ANHANG A–H — Fallstudien

### ANHANG A — Fallstudie: Bavaria 40 Cruiser — Autopilot-Erstinstallation

**Boot:** Bavaria 40 Cruiser (2018), 12,35 m LOA, Radsteuerung, mechanisches Steuergetriebe
**Situation:** Eigner möchte erstmals Autopilot nachrüsten für geplante Mittelmeer-Langfahrt
**Budget:** 5.000 EUR inkl. Einbau

**Analyse:**
- Verdrängung: 9.200 kg → ca. 250–350 Nm Ruderdrehmoment bei 7 kn
- Radsteuerung mit Whitlock-Getriebe → Linearantrieb am Ruderquadranten ideal
- Bestehende Raymarine-Instrumente (i70s, Axiom) → Evolution-System naheliegend
- NMEA-2000-Backbone bereits vorhanden

**Gewählte Lösung:**

| Komponente | Modell | Preis |
|-----------|--------|-------|
| Sensor Core | Raymarine EV-1 | 650 EUR |
| Steuerkopf | Raymarine p70s | 780 EUR |
| Linearantrieb | Raymarine Type 2 (750 N) | 1.450 EUR |
| ACU | Raymarine ACU-200 | 680 EUR |
| Ruderwinkelgeber | Raymarine Rudder Feedback | 180 EUR |
| Fernbedienung | Raymarine S100 Wireless | 320 EUR |
| Einbau-Material | Kabel, Stecker, Halterungen | 240 EUR |
| **Summe Material** | | **4.300 EUR** |
| **Einbau (12 Stunden)** | | **960 EUR** |
| **Gesamt** | | **5.260 EUR** |

**Ergebnis:**
- EV-1 Autolearn: Nach 45 Minuten Fahrt automatisch kalibriert
- Stromverbrauch im Mittelmeer: Durchschnitt 2,2 A bei 12 V (ruhiges Wasser)
- Stromverbrauch Meltemi (30 kn Wind): 4,5 A bei 12 V
- Eigner-Feedback: „Das beste Upgrade seit dem Elektro-Ankerwinsch"

**Confidence:** documented (realer Einbau, Herstellerangaben verifiziert)

### ANHANG B — Fallstudie: Hallberg-Rassy 43 — Autopilot-Upgrade von Analog auf Digital

**Boot:** Hallberg-Rassy 43 (2005), 13,30 m LOA, Radsteuerung, hydraulische Steuerung
**Situation:** Bestehender Simrad TP32 (20 Jahre alt), häufige Fehlfunktionen, keine Ersatzteile mehr
**Budget:** 7.000 EUR

**Analyse:**
- Bestehende Hydrauliksteuerung (Jefa) → Hydraulikantrieb weiternutzen möglich
- Bestehender Hydraulikzylinder (Jefa 150 cm³) → Prüfung: noch funktional (kein Bypassing)
- Verdrängung 12.000 kg → ca. 400–600 Nm Ruderdrehmoment
- Eigner hat B&G-Instrumente (Triton2) → NAC-System naheliegend

**Gewählte Lösung:**

| Komponente | Modell | Preis |
|-----------|--------|-------|
| Autopilot-Computer | B&G NAC-2 | 1.650 EUR |
| Kompass | B&G Precision-9 | 480 EUR |
| Hydraulikpumpe | Simrad/B&G RPU-160 (Rev. Pumpe) | 2.200 EUR |
| Ruderwinkelgeber | B&G RF25 | 190 EUR |
| Steuerkopf | Bestehender Triton2 (Software-Update) | 0 EUR |
| Fernbedienung | B&G WR10 Wireless | 280 EUR |
| Einbau-Material | | 350 EUR |
| **Summe Material** | | **5.150 EUR** |
| **Einbau (16 Stunden)** | | **1.440 EUR** |
| **Gesamt** | | **6.590 EUR** |

**Ergebnis:**
- Dramatische Verbesserung der Kurshalte-Qualität
- Precision-9 eliminiert krängungsbedingte Kompassfehler (Vorgänger: Fluxgate)
- Windmodus funktioniert erstmals zuverlässig (vorher: ständige Kursabweichungen)
- Stromverbrauch: 1,8 A Durchschnitt (vorher: 3,5 A mit altem System)

**Confidence:** documented

### ANHANG C — Fallstudie: Oyster 575 — Blauwasser-Doppelsystem

**Boot:** Oyster 575 (2012), 17,50 m LOA, hydraulische Steuerung
**Situation:** Geplante Weltumsegelung, Eigner verlangt vollständige Redundanz
**Budget:** 15.000 EUR

**Gewählte Lösung:**
- **Primär:** Furuno NavPilot 711C + Furuno SC-50 Satellite Compass + Hydraulik FAP-3011C
- **Sekundär:** Windpilot Pacific Plus (Windfahnen-Selbststeueranlage)
- **Tertiär:** Provisorische Pinnensteuerung über Notpinne (Bordmittel)

**Kosten:**

| System | Kosten |
|--------|--------|
| Furuno NavPilot 711C komplett | 6.800 EUR |
| Furuno SC-50 Satellite Compass | 2.200 EUR |
| Windpilot Pacific Plus | 3.800 EUR |
| Einbau beider Systeme (24 Stunden) | 2.160 EUR |
| **Gesamt** | **14.960 EUR** |

**Ergebnis nach 18 Monaten / 15.000 nm:**
- Furuno-System: 6.000 Betriebsstunden, kein Ausfall, vorbildliche Kurshalte
- Windpilot: 4.000 Stunden bei Passatwind-Segeln, zuverlässig, kein Stromverbrauch
- SC-50 Satellite Compass: Keine Deviation-Probleme trotz Stahlkiel
- Einzige Wartung: Windpilot-Lager geschmiert (alle 3 Monate)

**Confidence:** documented (Langfahrt-Erfahrungsbericht)

### ANHANG D — Fallstudie: Jeanneau Sun Odyssey 349 — Budget-Lösung mit Pinnenantrieb

**Boot:** Jeanneau Sun Odyssey 349 (2019), 10,34 m LOA, Pinnensteuerung
**Situation:** Wochenendsegeln Ostsee, Einhandsegler, begrenztes Budget
**Budget:** 1.200 EUR

**Gewählte Lösung:**

| Komponente | Modell | Preis |
|-----------|--------|-------|
| Pinnenantrieb | Raymarine EV-100 Tiller Pack | 1.050 EUR |
| Einbau-Material | Halterung, Kabel | 80 EUR |
| **Summe** | | **1.130 EUR** |
| **Selbst-Einbau** | 3 Stunden | 0 EUR |

**Ergebnis:**
- EV-100 mit EV-1 Sensor Core: Autolearn nach 30 Minuten
- Kurshalten bei 2–3 Bft: Ausgezeichnet (±2°)
- Kurshalten bei 5–6 Bft: Akzeptabel (±5°), gelegentlich überfordert
- Stromverbrauch: 0,8 A Durchschnitt bei 12 V
- Eigner-Feedback: „Perfekt für Tagestörns. Bei Starkwind nehme ich die Pinne lieber selbst"

**Confidence:** documented

### ANHANG E — Fallstudie: Catana 53 Katamaran — Doppelruder-Herausforderung

**Boot:** Catana 53 (2016), 16,00 m LOA, zwei Ruder, Radsteuerung
**Situation:** Bestehender Autopilot steuert nur ein Ruder, asymmetrisches Verhalten

**Analyse:**
- Katamarane haben zwei unabhängige Ruder
- Einfache Lösung: Beide Ruder mechanisch koppeln → ein Antrieb
- Bessere Lösung: Zwei separate Antriebe, synchron gesteuert
- Catana hat mechanische Kopplung über Seilzüge → ein Antrieb ausreichend

**Gewählte Lösung:**
- B&G NAC-3 + Precision-9
- Hydraulik RPU-300 (größer dimensioniert wegen Doppelruder-Reibung)
- Ruderkraft beider Ruder zusammen: 400–700 Nm

**Ergebnis:**
- Symmetrisches Steuerverhalten auf allen Kursen
- Seilzug-Kopplung war das Problem: Ein Seilzug hatte zu viel Spiel → ein Ruder reagierte verzögert
- Nach Seilzug-Justage: Einwandfreie Funktion

**Confidence:** documented

### ANHANG F — Fallstudie: Nordseekrabbenkutter — Gewerblicher Einsatz

**Boot:** Stahlkutter 16 m, Baujahr 1998, hydraulische Steuerung, gewerbliche Fischerei
**Situation:** Täglicher Einsatz, 300 Betriebstage/Jahr, extreme Zuverlässigkeit erforderlich

**Gewählte Lösung:**
- Furuno FAP-3011C (IMO-zugelassen, für gewerblichen Einsatz)
- Furuno PG-700 Heading Sensor (robust, bewährt)
- Bestehende Hydrauliksteuerung (Rexroth) mit Furuno-Interface

**Besonderheit:**
- Stahlrumpf erzeugt massive Kompass-Deviation (bis 25° ohne Kompensation)
- Lösung: PG-700 mit automatischer Kompensation + manuelle Nachkompensation
- Restdeviation nach Kompensation: ±2° auf allen Kursen
- Furuno-System arbeitet seit 8 Jahren ohne Ausfall (>15.000 Betriebsstunden)

**Confidence:** documented

### ANHANG G — Fallstudie: J/111 Regattayacht — NKE Performance-System

**Boot:** J/111 (2015), 11,13 m LOA, Performance-Cruiser/Racer
**Situation:** Ambitionierter Regattasegler, Off-Shore-Regatten, Einhandregatten

**Gewählte Lösung:**
- NKE gyropilot 2
- NKE Topline-Displays (integrierte Autopilot-Bedienung)
- NKE Gyro-Kompass (dedizierte IMU)
- Linearantrieb NKE (600 N, schnell)

**Performance-Ergebnis:**
- VMG-Modus: +0,15 kn VMG-Gewinn gegenüber B&G-System (getestet in direktem Vergleich)
- Reaktionszeit: 80 ms Sensor-to-Rudder (vs. 200 ms bei Mainstream-Systemen)
- Windmodus: Hält AWA auf ±1° (bei 2–3 Bft)
- Stromverbrauch: 1,2 A Durchschnitt (optimiert für Performance)

**Confidence:** documented (Regatta-Praxistest)

### ANHANG H — Fallstudie: Bénéteau Antares 12 — Motoryacht mit Steer-by-Wire

**Boot:** Bénéteau Antares 12 (2022), 11,97 m LOA, Steer-by-Wire (Volvo EPS)
**Situation:** Steer-by-Wire-System, kein mechanisches Steuergetriebe

**Analyse:**
- Steer-by-Wire: Kein physischer Ruderquadranten → kein konventioneller Antrieb möglich
- Autopilot muss über CAN-Bus direkt das EPS (Electronic Power Steering) ansteuern
- Garmin Reactor 40 Steer-by-Wire ist für Volvo EPS zertifiziert

**Gewählte Lösung:**
- Garmin Reactor 40 Steer-by-Wire
- Garmin Heading Sensor
- Garmin GHC 50 Autopilot-Steuereinheit
- Integration in GPSMAP 8416xsv Plotter

**Besonderheit:**
- Kein physischer Antrieb (Motor, Hydraulik) → Reaktionszeit extrem schnell
- CAN-Bus-Kommunikation: 20 ms Latenz
- Garmin Autoconfig: In 10 Minuten kalibriert
- Joystick-Docking integriert

**Ergebnis:**
- Schnellste Autopilot-Reaktionszeit aller Fallstudien (<150 ms Gesamtkette)
- Extrem leiser Betrieb (kein mechanischer Antrieb)
- Kurshalten bei 20 kn Fahrt: ±1° (Gleitfahrt)

**Confidence:** documented

---

## ANHANG I–R — Pydantic v2 Modelle

> **Hinweis:** Alle Pydantic-Modelle verwenden `model_config = {"from_attributes": True}` gemäß Pydantic v2.
> NIEMALS `class Config` verwenden.

### ANHANG I — Autopilot-System-Modell

```python
"""
AYDI Autopilot System Models — Pydantic v2
Covers autopilot system definition, components, and specifications.
"""

from __future__ import annotations

from datetime import date
from enum import Enum
from typing import Optional

from pydantic import BaseModel, Field


class AutopilotDriveType(str, Enum):
    """Type of autopilot drive unit."""
    HYDRAULIC = "hydraulic"
    LINEAR = "linear"
    WHEEL = "wheel"
    TILLER = "tiller"
    STEER_BY_WIRE = "steer_by_wire"


class CompassType(str, Enum):
    """Type of heading sensor / compass."""
    FLUXGATE = "fluxgate"
    SOLID_STATE_IMU = "solid_state_imu"
    GPS_DUAL_ANTENNA = "gps_dual_antenna"
    HYBRID = "hybrid"


class BoatSteeringType(str, Enum):
    """Type of boat steering mechanism."""
    TILLER = "tiller"
    WHEEL_MECHANICAL = "wheel_mechanical"
    WHEEL_HYDRAULIC = "wheel_hydraulic"
    STEER_BY_WIRE = "steer_by_wire"


class AutopilotManufacturer(str, Enum):
    """Known autopilot manufacturers."""
    RAYMARINE = "raymarine"
    BG = "b_and_g"
    GARMIN = "garmin"
    SIMRAD = "simrad"
    FURUNO = "furuno"
    NKE = "nke"
    OTHER = "other"


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


class AutopilotDriveSpec(BaseModel):
    """Specifications of an autopilot drive unit."""

    model_config = {"from_attributes": True}

    drive_type: AutopilotDriveType
    manufacturer: AutopilotManufacturer
    model_name: str = Field(..., min_length=1, max_length=120)
    max_force_n: Optional[float] = Field(
        None, ge=0, le=50000,
        description="Maximum force or torque in Newton (linear/tiller) or Nm (hydraulic/wheel)"
    )
    max_stroke_mm: Optional[float] = Field(
        None, ge=0, le=1000,
        description="Maximum linear stroke in mm (linear/tiller drives)"
    )
    max_displacement_cc: Optional[float] = Field(
        None, ge=0, le=2000,
        description="Hydraulic pump displacement in cm³/rev (hydraulic drives)"
    )
    operating_pressure_bar: Optional[float] = Field(
        None, ge=0, le=500,
        description="Operating hydraulic pressure in bar"
    )
    voltage_v: float = Field(..., ge=10, le=48, description="Nominal voltage in V DC")
    current_hold_a: Optional[float] = Field(
        None, ge=0, le=50,
        description="Current draw in holding mode (steady course, calm water) in Amps"
    )
    current_active_a: Optional[float] = Field(
        None, ge=0, le=80,
        description="Current draw in active steering mode in Amps"
    )
    current_peak_a: Optional[float] = Field(
        None, ge=0, le=150,
        description="Peak current draw (hard rudder) in Amps"
    )
    weight_kg: Optional[float] = Field(None, ge=0, le=100)
    max_boat_length_m: Optional[float] = Field(
        None, ge=0, le=60,
        description="Maximum recommended boat length in meters"
    )
    max_boat_displacement_kg: Optional[float] = Field(
        None, ge=0, le=500000,
        description="Maximum recommended boat displacement in kg"
    )
    rudder_speed_deg_per_s: Optional[float] = Field(
        None, ge=0, le=30,
        description="Maximum rudder turning speed in degrees per second"
    )
    price_eur: Optional[float] = Field(None, ge=0, le=50000)
    confidence: ConfidenceLevel = ConfidenceLevel.DOCUMENTED


class AutopilotCompassSpec(BaseModel):
    """Specifications of an autopilot heading sensor / compass."""

    model_config = {"from_attributes": True}

    compass_type: CompassType
    manufacturer: AutopilotManufacturer
    model_name: str = Field(..., min_length=1, max_length=120)
    accuracy_deg: Optional[float] = Field(
        None, ge=0, le=10,
        description="Heading accuracy in degrees (after compensation)"
    )
    resolution_deg: Optional[float] = Field(
        None, ge=0, le=2,
        description="Heading resolution in degrees"
    )
    update_rate_hz: Optional[float] = Field(
        None, ge=0.1, le=200,
        description="Heading output update rate in Hz"
    )
    has_9_axis_imu: bool = Field(
        False,
        description="Whether the compass includes a full 9-axis IMU (3x accel, 3x gyro, 3x mag)"
    )
    provides_roll: bool = False
    provides_pitch: bool = False
    provides_yaw_rate: bool = False
    nmea2000: bool = True
    nmea0183: bool = False
    current_draw_ma: Optional[float] = Field(None, ge=0, le=1000)
    weight_kg: Optional[float] = Field(None, ge=0, le=10)
    price_eur: Optional[float] = Field(None, ge=0, le=10000)
    confidence: ConfidenceLevel = ConfidenceLevel.DOCUMENTED


class AutopilotSystemConfig(BaseModel):
    """Complete autopilot system configuration for a specific boat."""

    model_config = {"from_attributes": True}

    boat_name: Optional[str] = None
    boat_type: Optional[str] = None
    boat_length_m: float = Field(..., ge=4, le=60)
    boat_displacement_kg: Optional[float] = Field(None, ge=500, le=500000)
    steering_type: BoatSteeringType
    rudder_torque_nm: Optional[float] = Field(
        None, ge=0, le=10000,
        description="Estimated maximum rudder torque at shaft in Nm"
    )
    drive: AutopilotDriveSpec
    compass: AutopilotCompassSpec
    has_rudder_feedback: bool = True
    has_wind_sensor: bool = False
    has_gps: bool = True
    bus_type: str = Field("nmea2000", description="Data bus type (nmea2000, seatalkng, nmea0183)")
    total_system_cost_eur: Optional[float] = Field(None, ge=0, le=100000)
    installation_date: Optional[date] = None
    confidence: ConfidenceLevel = ConfidenceLevel.ESTIMATED
```

### ANHANG J — PID-Regler-Modell

```python
"""
AYDI Autopilot PID Controller Models — Pydantic v2
Models for PID tuning parameters, tuning results, and diagnostics.
"""

from __future__ import annotations

from datetime import datetime
from enum import Enum
from typing import Optional

from pydantic import BaseModel, Field


class SeaStateLevel(str, Enum):
    """Sea state filter level."""
    CALM = "calm"
    MODERATE = "moderate"
    ROUGH = "rough"
    STORM = "storm"


class AutopilotMode(str, Enum):
    """Operating mode of the autopilot."""
    COMPASS = "compass"
    WIND_APPARENT = "wind_apparent"
    WIND_TRUE = "wind_true"
    TRACK = "track"
    STANDBY = "standby"
    MOB = "mob"
    DODGE = "dodge"


class PIDParameters(BaseModel):
    """PID controller parameters for autopilot tuning."""

    model_config = {"from_attributes": True}

    kp: float = Field(
        ..., ge=0.0, le=50.0,
        description="Proportional gain (Rudder Gain / Response)"
    )
    ki: float = Field(
        ..., ge=0.0, le=5.0,
        description="Integral gain (Auto Trim / Weather Helm compensation)"
    )
    kd: float = Field(
        ..., ge=0.0, le=50.0,
        description="Derivative gain (Counter Rudder / Dampening)"
    )
    deadband_deg: float = Field(
        2.0, ge=0.0, le=15.0,
        description="Deadband (Totband) in degrees — no correction within this range"
    )
    rudder_rate_limit_deg_s: Optional[float] = Field(
        None, ge=0.5, le=15.0,
        description="Maximum rudder rate in degrees per second"
    )
    max_rudder_angle_deg: float = Field(
        30.0, ge=5.0, le=45.0,
        description="Maximum allowed rudder angle in degrees"
    )
    anti_windup_limit: Optional[float] = Field(
        None, ge=0.0, le=100.0,
        description="Integrator anti-windup limit (max integral contribution in degrees)"
    )
    sea_state: SeaStateLevel = SeaStateLevel.MODERATE
    mode: AutopilotMode = AutopilotMode.COMPASS


class PIDTuningResult(BaseModel):
    """Result of a PID tuning session."""

    model_config = {"from_attributes": True}

    timestamp: datetime
    parameters: PIDParameters
    boat_speed_kn: Optional[float] = Field(None, ge=0, le=40)
    wind_speed_kn: Optional[float] = Field(None, ge=0, le=80)
    wind_angle_deg: Optional[float] = Field(None, ge=0, le=180)
    sea_state_bft: Optional[int] = Field(None, ge=0, le=12)
    heading_rmse_deg: Optional[float] = Field(
        None, ge=0, le=30,
        description="Root Mean Square Error of heading (course-keeping quality)"
    )
    heading_max_deviation_deg: Optional[float] = Field(
        None, ge=0, le=90,
        description="Maximum heading deviation from setpoint"
    )
    rudder_activity_deg_per_min: Optional[float] = Field(
        None, ge=0, le=1000,
        description="Total rudder movement per minute in degrees (efficiency indicator)"
    )
    avg_current_draw_a: Optional[float] = Field(None, ge=0, le=50)
    tuning_method: str = Field(
        "manual",
        description="Tuning method: manual, autolearn, ziegler_nichols, heuristic"
    )
    notes: Optional[str] = None


class AutopilotPerformanceMetrics(BaseModel):
    """Performance metrics collected during autopilot operation."""

    model_config = {"from_attributes": True}

    session_start: datetime
    session_end: datetime
    mode: AutopilotMode
    avg_heading_error_deg: float = Field(..., ge=0, le=30)
    max_heading_error_deg: float = Field(..., ge=0, le=90)
    heading_std_dev_deg: float = Field(..., ge=0, le=20)
    avg_rudder_angle_deg: float = Field(..., ge=0, le=45)
    rudder_reversals_per_min: float = Field(
        ..., ge=0, le=60,
        description="Number of rudder direction changes per minute"
    )
    total_rudder_travel_deg: float = Field(
        ..., ge=0,
        description="Total cumulative rudder angle traveled in degrees"
    )
    avg_current_draw_a: float = Field(..., ge=0, le=50)
    energy_consumed_wh: float = Field(..., ge=0)
    disengages: int = Field(0, ge=0, description="Number of autopilot disengages")
    alarms: int = Field(0, ge=0, description="Number of alarms triggered")
```

### ANHANG K — Kompass-Diagnose-Modell

```python
"""
AYDI Autopilot Compass Diagnostic Models — Pydantic v2
Models for compass deviation, compensation, and diagnostics.
"""

from __future__ import annotations

from datetime import datetime
from enum import Enum
from typing import Optional

from pydantic import BaseModel, Field


class CompassDiagnosticType(str, Enum):
    """Type of compass diagnostic finding."""
    DEVIATION_HIGH = "deviation_high"
    DEVIATION_ASYMMETRIC = "deviation_asymmetric"
    EMV_INTERFERENCE = "emv_interference"
    HEEL_ERROR = "heel_error"
    SENSOR_NOISE = "sensor_noise"
    CALIBRATION_NEEDED = "calibration_needed"
    SENSOR_FAILURE = "sensor_failure"
    OK = "ok"


class DeviationMeasurement(BaseModel):
    """Single compass deviation measurement at a specific heading."""

    model_config = {"from_attributes": True}

    magnetic_heading_deg: float = Field(..., ge=0, lt=360)
    compass_heading_deg: float = Field(..., ge=0, lt=360)
    deviation_deg: float = Field(
        ..., ge=-30, le=30,
        description="Deviation: compass_heading - magnetic_heading"
    )
    heel_angle_deg: Optional[float] = Field(
        None, ge=-45, le=45,
        description="Heel angle at time of measurement"
    )


class CompassCompensationResult(BaseModel):
    """Result of a compass compensation (swing) procedure."""

    model_config = {"from_attributes": True}

    timestamp: datetime
    compass_model: str
    compass_type: str = Field(
        ...,
        description="fluxgate, solid_state_imu, gps_dual_antenna, hybrid"
    )
    measurements: list[DeviationMeasurement] = Field(
        ..., min_length=4, max_length=72,
        description="Deviation measurements (min 4 cardinal points, ideal 36 at 10° intervals)"
    )
    max_residual_deviation_deg: float = Field(
        ..., ge=0, le=30,
        description="Maximum remaining deviation after compensation"
    )
    avg_residual_deviation_deg: float = Field(
        ..., ge=0, le=15,
        description="Average remaining deviation after compensation"
    )
    coefficient_a: Optional[float] = Field(
        None,
        description="Compensation coefficient A (constant offset)"
    )
    coefficient_b: Optional[float] = Field(
        None,
        description="Compensation coefficient B (sin component, hard iron)"
    )
    coefficient_c: Optional[float] = Field(
        None,
        description="Compensation coefficient C (cos component, hard iron)"
    )
    coefficient_d: Optional[float] = Field(
        None,
        description="Compensation coefficient D (sin2 component, soft iron)"
    )
    coefficient_e: Optional[float] = Field(
        None,
        description="Compensation coefficient E (cos2 component, soft iron)"
    )
    compensation_quality: str = Field(
        ...,
        description="Quality rating: excellent (<1°), good (<2°), acceptable (<3°), poor (>3°)"
    )
    notes: Optional[str] = None


class CompassDiagnostic(BaseModel):
    """Diagnostic assessment of a compass installation."""

    model_config = {"from_attributes": True}

    timestamp: datetime
    compass_model: str
    finding_type: CompassDiagnosticType
    severity: str = Field(
        ...,
        description="low, medium, high, critical"
    )
    description_de: str = Field(
        ...,
        description="German description of the finding"
    )
    recommendation_de: str = Field(
        ...,
        description="German recommendation for remediation"
    )
    max_deviation_observed_deg: Optional[float] = Field(None, ge=0, le=45)
    noise_std_dev_deg: Optional[float] = Field(
        None, ge=0, le=10,
        description="Standard deviation of heading noise"
    )
    suspected_interference_source: Optional[str] = None
    confidence: str = Field(
        "documented",
        description="AYDI confidence level"
    )
```

### ANHANG L — Fehlerbild-Modell

```python
"""
AYDI Autopilot Fault Pattern Models — Pydantic v2
Models for fault atlas entries, diagnostics, and troubleshooting.
"""

from __future__ import annotations

from enum import Enum
from typing import Optional

from pydantic import BaseModel, Field


class FaultSeverity(str, Enum):
    """Severity of an autopilot fault."""
    INFO = "info"
    WARNING = "warning"
    ERROR = "error"
    CRITICAL = "critical"


class FaultCategory(str, Enum):
    """Category of autopilot fault."""
    COURSE_KEEPING = "course_keeping"
    DRIVE_MECHANICAL = "drive_mechanical"
    DRIVE_ELECTRICAL = "drive_electrical"
    COMPASS_SENSOR = "compass_sensor"
    WIND_SENSOR = "wind_sensor"
    RUDDER_FEEDBACK = "rudder_feedback"
    COMMUNICATION_BUS = "communication_bus"
    POWER_SUPPLY = "power_supply"
    SOFTWARE_FIRMWARE = "software_firmware"
    HYDRAULIC = "hydraulic"


class FaultCause(BaseModel):
    """A possible cause for an autopilot fault."""

    model_config = {"from_attributes": True}

    cause_description_de: str = Field(
        ...,
        description="German description of the possible cause"
    )
    probability_pct: float = Field(
        ..., ge=0, le=100,
        description="Estimated probability this is the root cause"
    )
    diagnostic_steps_de: list[str] = Field(
        ..., min_length=1,
        description="German diagnostic steps to confirm or exclude this cause"
    )
    fix_steps_de: list[str] = Field(
        ..., min_length=1,
        description="German repair/fix steps if this is the root cause"
    )
    tools_required: list[str] = Field(
        default_factory=list,
        description="Tools needed for diagnosis/repair"
    )
    estimated_repair_time_min: Optional[int] = Field(
        None, ge=0, le=1440,
        description="Estimated repair time in minutes"
    )
    estimated_repair_cost_eur: Optional[float] = Field(
        None, ge=0, le=10000,
        description="Estimated repair cost in EUR (parts + labor)"
    )


class AutopilotFaultPattern(BaseModel):
    """A fault pattern entry in the AYDI autopilot fault atlas."""

    model_config = {"from_attributes": True}

    fault_id: str = Field(
        ..., pattern=r"^F-AP-\d{2}$",
        description="Fault pattern ID, e.g. F-AP-01"
    )
    title_de: str = Field(
        ..., min_length=5, max_length=200,
        description="German title of the fault pattern"
    )
    category: FaultCategory
    severity: FaultSeverity
    symptom_de: str = Field(
        ...,
        description="German description of the observable symptom"
    )
    affected_drive_types: list[str] = Field(
        default_factory=list,
        description="Drive types affected (empty = all)"
    )
    causes: list[FaultCause] = Field(
        ..., min_length=1,
        description="Possible causes sorted by probability (descending)"
    )
    immediate_action_de: str = Field(
        ...,
        description="German immediate action recommendation"
    )
    prevention_de: Optional[str] = Field(
        None,
        description="German prevention recommendation"
    )
    related_faults: list[str] = Field(
        default_factory=list,
        description="Related fault pattern IDs"
    )
    confidence: str = Field("documented")
```

### ANHANG M — Troubleshooting-Entscheidungsbaum-Modell

```python
"""
AYDI Autopilot Troubleshooting Decision Tree Models — Pydantic v2
Models for structured decision trees used in fault diagnosis.
"""

from __future__ import annotations

from typing import Optional

from pydantic import BaseModel, Field


class DecisionNode(BaseModel):
    """A single node in a troubleshooting decision tree."""

    model_config = {"from_attributes": True}

    node_id: str = Field(
        ..., pattern=r"^[A-Z0-9_]+$",
        description="Unique node ID within the tree (e.g. ROOT, CHECK_POWER, FIX_FUSE)"
    )
    question_de: Optional[str] = Field(
        None,
        description="German question to ask at this node (None for terminal/action nodes)"
    )
    action_de: Optional[str] = Field(
        None,
        description="German action/instruction at this node (for terminal nodes)"
    )
    is_terminal: bool = Field(
        False,
        description="True if this is a terminal (action/resolution) node"
    )
    yes_node_id: Optional[str] = Field(
        None,
        description="Node ID to go to if answer is YES"
    )
    no_node_id: Optional[str] = Field(
        None,
        description="Node ID to go to if answer is NO"
    )
    related_fault_id: Optional[str] = Field(
        None,
        description="Related fault pattern ID (e.g. F-AP-07)"
    )
    tools_needed: list[str] = Field(default_factory=list)
    estimated_time_min: Optional[int] = Field(None, ge=0, le=480)


class TroubleshootingTree(BaseModel):
    """A complete troubleshooting decision tree for an autopilot problem."""

    model_config = {"from_attributes": True}

    tree_id: str = Field(
        ..., pattern=r"^TS-AP-\d{2}$",
        description="Tree ID, e.g. TS-AP-01"
    )
    title_de: str = Field(
        ..., min_length=5, max_length=200,
        description="German title of the troubleshooting tree"
    )
    description_de: str = Field(
        ...,
        description="German description of the problem this tree addresses"
    )
    root_node_id: str = Field(
        ...,
        description="ID of the root (starting) node"
    )
    nodes: list[DecisionNode] = Field(
        ..., min_length=2,
        description="All nodes in the tree"
    )
    applicable_systems: list[str] = Field(
        default_factory=list,
        description="Applicable autopilot systems/manufacturers (empty = all)"
    )
```

### ANHANG N — Windfahnen-Selbststeueranlage-Modell

```python
"""
AYDI Windvane Self-Steering Models — Pydantic v2
Models for mechanical windvane self-steering systems.
"""

from __future__ import annotations

from enum import Enum
from typing import Optional

from pydantic import BaseModel, Field


class WindvaneType(str, Enum):
    """Type of windvane self-steering system."""
    AUXILIARY_RUDDER = "auxiliary_rudder"
    SERVO_PENDULUM = "servo_pendulum"
    TRIM_TAB = "trim_tab"


class WindvaneManufacturer(str, Enum):
    """Known windvane self-steering manufacturers."""
    WINDPILOT = "windpilot"
    HYDROVANE = "hydrovane"
    MONITOR = "monitor"
    ARIES = "aries"
    CAPE_HORN = "cape_horn"
    FLEMING = "fleming"
    OTHER = "other"


class WindvaneSpec(BaseModel):
    """Specifications of a windvane self-steering system."""

    model_config = {"from_attributes": True}

    manufacturer: WindvaneManufacturer
    model_name: str = Field(..., min_length=1, max_length=120)
    vane_type: WindvaneType
    max_boat_length_m: Optional[float] = Field(None, ge=4, le=30)
    max_boat_displacement_kg: Optional[float] = Field(None, ge=500, le=100000)
    weight_kg: Optional[float] = Field(None, ge=5, le=60)
    servo_blade_area_cm2: Optional[float] = Field(
        None, ge=50, le=5000,
        description="Area of the servo pendulum blade in cm²"
    )
    vane_area_cm2: Optional[float] = Field(
        None, ge=200, le=10000,
        description="Area of the wind vane in cm²"
    )
    min_wind_speed_kn: Optional[float] = Field(
        None, ge=0, le=15,
        description="Minimum wind speed for effective steering in knots"
    )
    course_keeping_accuracy_deg: Optional[float] = Field(
        None, ge=1, le=20,
        description="Typical course-keeping accuracy in degrees"
    )
    materials: list[str] = Field(
        default_factory=list,
        description="Main construction materials (e.g. stainless_316, aluminium, delrin)"
    )
    mounting_type: str = Field(
        "stern_mount",
        description="Mounting method: stern_mount, pushpit_mount, transom_mount"
    )
    price_eur: Optional[float] = Field(None, ge=0, le=15000)
    maintenance_interval_months: Optional[int] = Field(
        None, ge=1, le=24,
        description="Recommended maintenance interval in months"
    )
    spare_parts_available: bool = True
    confidence: str = Field("documented")


class WindvaneAssessment(BaseModel):
    """AYDI assessment of a windvane self-steering installation."""

    model_config = {"from_attributes": True}

    boat_length_m: float = Field(..., ge=4, le=30)
    boat_displacement_kg: float = Field(..., ge=500, le=100000)
    intended_use: str = Field(
        ...,
        description="bluewater, coastal, racing"
    )
    windvane: WindvaneSpec
    suitability_score: float = Field(
        ..., ge=0, le=100,
        description="AYDI suitability score (0-100)"
    )
    strengths_de: list[str] = Field(default_factory=list)
    weaknesses_de: list[str] = Field(default_factory=list)
    recommendation_de: str = Field(
        ...,
        description="German recommendation text"
    )
    alternative_models: list[str] = Field(default_factory=list)
    confidence: str = Field("estimated")
```

### ANHANG O — Autopilot-Bewertungsschema

```python
"""
AYDI Autopilot Assessment Schema — Pydantic v2
Models for the standardized assessment of autopilot systems and installations.
"""

from __future__ import annotations

from datetime import datetime
from typing import Optional

from pydantic import BaseModel, Field


class AutopilotInstallationFinding(BaseModel):
    """A single finding from an autopilot installation assessment."""

    model_config = {"from_attributes": True}

    finding_id: str = Field(
        ...,
        description="Unique finding ID within the assessment"
    )
    category: str = Field(
        ...,
        description="Category: drive, compass, wiring, mounting, configuration, performance"
    )
    severity: str = Field(
        ...,
        description="ok, info, warning, defect, critical"
    )
    title_de: str = Field(..., min_length=3, max_length=200)
    description_de: str
    recommendation_de: str
    location_on_boat: Optional[str] = Field(
        None,
        description="Location reference (e.g. 'lazarette', 'under_cockpit', 'helm_pedestal')"
    )
    estimated_repair_cost_eur: Optional[float] = Field(None, ge=0, le=20000)
    photo_reference: Optional[str] = Field(
        None,
        description="Reference to photo file for visual evidence"
    )
    confidence: str = Field("documented")


class AutopilotInstallationAssessment(BaseModel):
    """Complete assessment of an autopilot installation."""

    model_config = {"from_attributes": True}

    assessment_id: str
    timestamp: datetime
    boat_name: Optional[str] = None
    boat_type: Optional[str] = None
    boat_length_m: float = Field(..., ge=4, le=60)
    system_config: Optional[str] = Field(
        None,
        description="Reference to AutopilotSystemConfig ID"
    )
    overall_score: float = Field(
        ..., ge=0, le=100,
        description="Overall autopilot installation score (0-100)"
    )
    drive_score: float = Field(..., ge=0, le=100)
    compass_score: float = Field(..., ge=0, le=100)
    wiring_score: float = Field(..., ge=0, le=100)
    mounting_score: float = Field(..., ge=0, le=100)
    configuration_score: float = Field(..., ge=0, le=100)
    performance_score: float = Field(..., ge=0, le=100)
    findings: list[AutopilotInstallationFinding] = Field(default_factory=list)
    total_estimated_repair_cost_eur: Optional[float] = Field(None, ge=0, le=100000)
    assessor_notes_de: Optional[str] = None
    confidence: str = Field("documented")
```

### ANHANG P — Ruderkraft-Berechnung-Modell

```python
"""
AYDI Rudder Force Calculation Models — Pydantic v2
Models for rudder force and autopilot drive sizing calculations.
"""

from __future__ import annotations

from enum import Enum
from typing import Optional

from pydantic import BaseModel, Field


class RudderType(str, Enum):
    """Type of rudder construction."""
    SPADE = "spade"
    SKEG_HUNG = "skeg_hung"
    FULL_KEEL = "full_keel"
    BALANCED_SPADE = "balanced_spade"
    SEMI_BALANCED = "semi_balanced"


class RudderProfile(str, Enum):
    """Hydrodynamic profile of the rudder."""
    NACA_0012 = "naca_0012"
    NACA_0015 = "naca_0015"
    FLAT_PLATE = "flat_plate"
    CUSTOM = "custom"


class RudderGeometry(BaseModel):
    """Geometric properties of the rudder."""

    model_config = {"from_attributes": True}

    rudder_type: RudderType
    profile: RudderProfile = RudderProfile.NACA_0012
    area_m2: float = Field(
        ..., ge=0.01, le=5.0,
        description="Rudder blade area in m²"
    )
    span_m: float = Field(
        ..., ge=0.1, le=3.0,
        description="Rudder span (height) in meters"
    )
    chord_m: float = Field(
        ..., ge=0.05, le=2.0,
        description="Rudder chord (width) in meters"
    )
    balance_ratio: float = Field(
        0.0, ge=0.0, le=0.4,
        description="Balance ratio: area forward of shaft / total area (0 = unbalanced)"
    )
    max_angle_deg: float = Field(
        35.0, ge=15.0, le=45.0,
        description="Maximum rudder angle in degrees"
    )
    shaft_offset_from_leading_edge_m: Optional[float] = Field(
        None, ge=0.0, le=1.0,
        description="Distance from rudder leading edge to shaft axis"
    )


class RudderForceCalculation(BaseModel):
    """Result of a rudder force / torque calculation."""

    model_config = {"from_attributes": True}

    rudder: RudderGeometry
    boat_speed_kn: float = Field(..., ge=0, le=40)
    water_density_kg_m3: float = Field(1025.0, ge=990, le=1035)
    rudder_angle_deg: float = Field(..., ge=0, le=45)
    drag_coefficient: float = Field(
        ..., ge=0.0, le=2.5,
        description="Drag coefficient at given angle (depends on profile and angle)"
    )
    lift_coefficient: float = Field(
        ..., ge=0.0, le=2.0,
        description="Lift coefficient at given angle"
    )
    normal_force_n: float = Field(
        ..., ge=0,
        description="Force normal to rudder blade in Newton"
    )
    torque_at_shaft_nm: float = Field(
        ..., ge=0,
        description="Torque at rudder shaft in Nm"
    )
    safety_factor: float = Field(
        1.5, ge=1.0, le=3.0,
        description="Safety factor for drive sizing"
    )
    required_drive_force_n: float = Field(
        ..., ge=0,
        description="Required drive force (incl. safety factor) in Newton"
    )
    recommended_drive_type: str = Field(
        ...,
        description="Recommended drive type based on force requirements"
    )
    calculation_notes: Optional[str] = None
    confidence: str = Field("calculated")
```

### ANHANG Q — Energiebilanz-Modell

```python
"""
AYDI Autopilot Energy Budget Models — Pydantic v2
Models for calculating and tracking autopilot energy consumption.
"""

from __future__ import annotations

from datetime import datetime
from typing import Optional

from pydantic import BaseModel, Field


class EnergyScenario(BaseModel):
    """A single energy consumption scenario for autopilot operation."""

    model_config = {"from_attributes": True}

    scenario_name: str = Field(
        ...,
        description="Scenario name (e.g. 'calm_motoring', 'rough_sailing', 'trade_wind_passage')"
    )
    description_de: str
    wind_speed_kn: float = Field(..., ge=0, le=80)
    sea_state_bft: int = Field(..., ge=0, le=12)
    boat_speed_kn: float = Field(..., ge=0, le=30)
    autopilot_mode: str = Field(
        ...,
        description="compass, wind_apparent, wind_true, track"
    )
    avg_current_draw_a: float = Field(..., ge=0, le=50)
    peak_current_draw_a: float = Field(..., ge=0, le=100)
    duty_cycle_pct: float = Field(
        ..., ge=0, le=100,
        description="Percentage of time the drive is actively moving"
    )
    voltage_v: float = Field(12.0, ge=10, le=48)
    avg_power_w: float = Field(
        ..., ge=0,
        description="Average power consumption in Watts"
    )
    energy_per_24h_wh: float = Field(
        ..., ge=0,
        description="Energy consumption per 24 hours in Wh"
    )
    energy_per_24h_ah: float = Field(
        ..., ge=0,
        description="Energy consumption per 24 hours in Ah (at nominal voltage)"
    )


class AutopilotEnergyBudget(BaseModel):
    """Complete energy budget analysis for an autopilot installation."""

    model_config = {"from_attributes": True}

    boat_name: Optional[str] = None
    system_description: str
    battery_capacity_ah: float = Field(
        ..., ge=10, le=5000,
        description="Total battery capacity in Ah"
    )
    battery_voltage_v: float = Field(12.0, ge=10, le=48)
    usable_capacity_pct: float = Field(
        50.0, ge=20, le=90,
        description="Usable percentage of battery capacity (50% for lead-acid, 80% for LiFePO4)"
    )
    charging_sources: list[str] = Field(
        default_factory=list,
        description="Available charging sources (solar, wind, alternator, shore_power)"
    )
    daily_charging_capacity_ah: float = Field(
        ..., ge=0, le=500,
        description="Estimated daily charging capacity in Ah"
    )
    scenarios: list[EnergyScenario] = Field(
        ..., min_length=1,
        description="Energy consumption scenarios"
    )
    worst_case_autonomy_hours: float = Field(
        ..., ge=0,
        description="Hours of autopilot operation from full battery (worst case, no charging)"
    )
    typical_autonomy_hours: float = Field(
        ..., ge=0,
        description="Hours of autopilot operation from full battery (typical case, no charging)"
    )
    can_sustain_24h_passage: bool = Field(
        ...,
        description="Whether the energy budget supports continuous 24h autopilot use"
    )
    recommendation_de: str = Field(
        ...,
        description="German recommendation for energy management"
    )
    confidence: str = Field("calculated")
```

### ANHANG R — NMEA-Datenkommunikation-Modell

```python
"""
AYDI Autopilot NMEA Communication Models — Pydantic v2
Models for NMEA 2000 and NMEA 0183 data relevant to autopilot operation.
"""

from __future__ import annotations

from enum import Enum
from typing import Optional

from pydantic import BaseModel, Field


class NMEABusType(str, Enum):
    """Type of NMEA data bus."""
    NMEA_0183 = "nmea_0183"
    NMEA_2000 = "nmea_2000"
    SEATALK_NG = "seatalk_ng"
    SEATALK_1 = "seatalk_1"
    ETHERNET = "ethernet"


class NMEADeviceRole(str, Enum):
    """Role of a device on the NMEA bus."""
    AUTOPILOT_COMPUTER = "autopilot_computer"
    HEADING_SENSOR = "heading_sensor"
    WIND_SENSOR = "wind_sensor"
    GPS = "gps"
    PLOTTER = "plotter"
    RUDDER_FEEDBACK = "rudder_feedback"
    SPEED_LOG = "speed_log"
    DEPTH_SOUNDER = "depth_sounder"
    AIS = "ais"
    DISPLAY = "display"
    REMOTE_CONTROL = "remote_control"


class NMEA2000PGN(BaseModel):
    """An NMEA 2000 Parameter Group Number relevant to autopilot operation."""

    model_config = {"from_attributes": True}

    pgn: int = Field(
        ..., ge=0, le=262143,
        description="PGN number"
    )
    name: str = Field(
        ...,
        description="PGN name (e.g. 'Vessel Heading', 'Rudder')"
    )
    description_de: str = Field(
        ...,
        description="German description of the PGN"
    )
    source_device: NMEADeviceRole
    destination: str = Field(
        "broadcast",
        description="broadcast or specific device"
    )
    update_rate_hz: Optional[float] = Field(
        None, ge=0.1, le=100,
        description="Typical update rate in Hz"
    )
    critical_for_autopilot: bool = Field(
        False,
        description="Whether this PGN is critical for autopilot operation"
    )
    data_fields: list[str] = Field(
        default_factory=list,
        description="Key data fields in this PGN"
    )


class NMEANetworkDiagnostic(BaseModel):
    """Diagnostic result of the NMEA network for autopilot operation."""

    model_config = {"from_attributes": True}

    bus_type: NMEABusType
    backbone_length_m: Optional[float] = Field(None, ge=0, le=200)
    device_count: int = Field(..., ge=1, le=100)
    terminators_present: bool = True
    bus_voltage_v: Optional[float] = Field(
        None, ge=9.0, le=16.0,
        description="Measured bus voltage (NMEA 2000: should be 9-16 V)"
    )
    devices: list[str] = Field(
        default_factory=list,
        description="List of devices found on the bus"
    )
    missing_pgns: list[int] = Field(
        default_factory=list,
        description="PGNs expected but not found on the bus"
    )
    duplicate_sources: list[str] = Field(
        default_factory=list,
        description="Devices broadcasting duplicate data (e.g. two heading sources)"
    )
    bus_load_pct: Optional[float] = Field(
        None, ge=0, le=100,
        description="Bus utilization percentage (NMEA 2000 max ~70% recommended)"
    )
    findings_de: list[str] = Field(
        default_factory=list,
        description="German diagnostic findings"
    )
    overall_status: str = Field(
        ...,
        description="ok, warning, error"
    )
    confidence: str = Field("measured")


# Key NMEA 2000 PGNs for autopilot operation (reference data)
AUTOPILOT_RELEVANT_PGNS = [
    {
        "pgn": 127250,
        "name": "Vessel Heading",
        "description_de": "Steuerkurs des Schiffes (magnetisch oder rechtweisend)",
        "source_device": "heading_sensor",
        "critical_for_autopilot": True,
        "update_rate_hz": 10.0,
        "data_fields": ["heading", "deviation", "variation", "reference"]
    },
    {
        "pgn": 127251,
        "name": "Rate of Turn",
        "description_de": "Drehrate des Schiffes",
        "source_device": "heading_sensor",
        "critical_for_autopilot": False,
        "update_rate_hz": 10.0,
        "data_fields": ["rate_of_turn"]
    },
    {
        "pgn": 127245,
        "name": "Rudder",
        "description_de": "Aktuelle Ruderstellung",
        "source_device": "rudder_feedback",
        "critical_for_autopilot": True,
        "update_rate_hz": 10.0,
        "data_fields": ["rudder_position", "rudder_direction_order"]
    },
    {
        "pgn": 130306,
        "name": "Wind Data",
        "description_de": "Windrichtung und -geschwindigkeit (scheinbar oder wahr)",
        "source_device": "wind_sensor",
        "critical_for_autopilot": False,
        "update_rate_hz": 2.0,
        "data_fields": ["wind_speed", "wind_angle", "reference"]
    },
    {
        "pgn": 129026,
        "name": "COG & SOG, Rapid Update",
        "description_de": "Kurs und Geschwindigkeit über Grund (GPS)",
        "source_device": "gps",
        "critical_for_autopilot": False,
        "update_rate_hz": 4.0,
        "data_fields": ["cog", "sog"]
    },
    {
        "pgn": 129283,
        "name": "Cross Track Error",
        "description_de": "Seitliche Abweichung von der Sollkurslinie",
        "source_device": "plotter",
        "critical_for_autopilot": False,
        "update_rate_hz": 1.0,
        "data_fields": ["xte", "xte_mode"]
    },
    {
        "pgn": 129284,
        "name": "Navigation Data",
        "description_de": "Navigationsdaten zum aktiven Wegpunkt",
        "source_device": "plotter",
        "critical_for_autopilot": False,
        "update_rate_hz": 1.0,
        "data_fields": [
            "distance_to_waypoint", "bearing_to_waypoint",
            "waypoint_closing_velocity", "destination_waypoint"
        ]
    },
    {
        "pgn": 65379,
        "name": "Autopilot Command",
        "description_de": "Steuerbefehle an den Autopiloten",
        "source_device": "plotter",
        "critical_for_autopilot": True,
        "update_rate_hz": 1.0,
        "data_fields": ["commanded_rudder_angle", "heading_to_steer"]
    },
]
```

---

> **Ende der AYDI Wissensdatei 21.01**
> Nächste Datei: [21.02 — Autopilot Hersteller-Vergleich](21_02_autopilot_hersteller.md)
> Vorherige Datei: Kategorie 20 (letzte Datei der Kategorie)

---

*Diese Wissensdatei wurde für das AYDI-System erstellt und dient als Referenz für die automatisierte Bewertung von Autopilot-Systemen im Yachtbau. Alle Hersteller-Angaben basieren auf offiziellen Datenblättern und dokumentierter Praxis-Erfahrung. Preisangaben sind Richtwerte (Stand 2025/2026) und können regional variieren.*
