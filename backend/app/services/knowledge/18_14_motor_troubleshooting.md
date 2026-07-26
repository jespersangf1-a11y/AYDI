---
titel: "Motor-Troubleshooting — Diagnose und Fehlersuche"
kategorie: "Motoren und Antrieb"
unterkategorie: "Motor-Troubleshooting"
version: "2.0"
letzte_aktualisierung: "2026-04"
autor: "AYDI Maritime Knowledge Base"
---

# 18_14 — Motor-Troubleshooting — Diagnose und Fehlersuche

---

## Inhaltsverzeichnis

1. [Einführung und systematischer Diagnoseansatz](#1-einführung-und-systematischer-diagnoseansatz)
2. [Motor startet nicht — Vollständiger Entscheidungsbaum](#2-motor-startet-nicht--vollständiger-entscheidungsbaum)
3. [Überhitzung — Kühlsystem-Diagnose](#3-überhitzung--kühlsystem-diagnose)
4. [Rauchfarbe-Diagnose](#4-rauchfarbe-diagnose)
5. [Öldruck-Probleme](#5-öldruck-probleme)
6. [Vibrationen und Geräusche](#6-vibrationen-und-geräusche)
7. [Leistungsverlust](#7-leistungsverlust)
8. [Kraftstoffprobleme](#8-kraftstoffprobleme)
9. [Elektrische Probleme](#9-elektrische-probleme)
10. [Ölverlust und Leckagen](#10-ölverlust-und-leckagen)
11. [Kompressionstest — Durchführung und Interpretation](#11-kompressionstest--durchführung-und-interpretation)
12. [Ölanalyse — Probennahme und Interpretation](#12-ölanalyse--probennahme-und-interpretation)
13. [Common-Rail Fehlercodes und Diagnosegeräte](#13-common-rail-fehlercodes-und-diagnosegeräte)
14. [Notfall-Maßnahmen auf See](#14-notfall-maßnahmen-auf-see)
15. [Fehlerbild-Atlas](#15-fehlerbild-atlas)
16. [Troubleshooting-Entscheidungsbäume](#16-troubleshooting-entscheidungsbäume)
17. [FAQ](#17-faq)
18. [Glossar](#18-glossar)
19. [Schnell-Referenz](#19-schnell-referenz)
20. [ANHANG A–H: Fallstudien](#20-anhang-ah-fallstudien)
21. [ANHANG I–R: Pydantic v2 Datenmodelle](#21-anhang-ir-pydantic-v2-datenmodelle)

---
---

## 1. Einführung und systematischer Diagnoseansatz

### 1.1 Warum systematische Fehlersuche entscheidend ist

Die Fehlersuche an Marine-Dieselmotoren unterscheidet sich fundamental von der
Diagnose an Land-Dieselmotoren. An Bord stehen weder Werkstattausrüstung noch
Diagnosestände zur Verfügung. Gleichzeitig kann ein Motorausfall auf See eine
lebensbedrohliche Situation darstellen. Systematische Fehlersuche bedeutet:

- **Methodisch vorgehen**: Symptom identifizieren → mögliche Ursachen eingrenzen →
  wahrscheinlichste Ursache zuerst prüfen → verifizieren → beheben.
- **Keine Panikraumreaktionen**: Nicht willkürlich Teile tauschen. Jede Maßnahme
  muss eine logische Begründung haben.
- **Dokumentieren**: Jede Beobachtung, jede Messung, jede durchgeführte Maßnahme
  festhalten. Dies hilft bei wiederkehrenden Problemen und beim Wiederverkauf.

**Kosten unsystematischer Fehlersuche:**

| Szenario | Typische Kosten | Zeitverlust |
|----------|----------------|-------------|
| Willkürlicher Teiletausch durch Eigner | 500–3.000 EUR | 2–5 Tage |
| Fehldiagnose durch unerfahrene Werft | 1.000–5.000 EUR | 1–3 Wochen |
| Systematische Diagnose durch Fachbetrieb | 200–800 EUR | 1–3 Stunden |
| Eigene systematische Diagnose mit Wissen | 0–200 EUR | 1–4 Stunden |

### 1.2 Die vier Grundpfeiler der Dieselfunktion

Ein Dieselmotor benötigt exakt vier Dinge, um zu laufen. Jedes Problem lässt
sich auf einen oder mehrere dieser Grundpfeiler zurückführen:

```
┌─────────────────────────────────────────────────┐
│           DIESEL LÄUFT, WENN:                    │
│                                                   │
│   1. KRAFTSTOFF  — sauber, ausreichend, korrekt  │
│                    eingespritzt                    │
│   2. LUFT        — sauber, ausreichend, korrekt   │
│                    verdichtet                      │
│   3. KOMPRESSION — Kolbenringe, Ventile, Kopf-    │
│                    dichtung dicht                  │
│   4. TIMING      — Einspritzung zum richtigen     │
│                    Zeitpunkt im Zyklus             │
│                                                   │
│   + ELEKTRIK für Start (Anlasser, Glühkerzen)     │
│   + KÜHLUNG für Dauerbetrieb                      │
│   + SCHMIERUNG für Lebensdauer                    │
└─────────────────────────────────────────────────┘
```

### 1.3 Diagnose-Hierarchie: Vom Symptom zur Ursache

Die professionelle Fehlersuche folgt immer dieser Hierarchie:

**Stufe 1 — Sinneswahrnehmung (0 EUR, sofort)**
- Sehen: Rauchfarbe, Leckagen, Verfärbungen, Korrosion
- Hören: Ungewöhnliche Geräusche, Klopfen, Pfeifen, Klappern
- Riechen: Verbranntes Öl, Diesel, Kühlmittel, Elektrik
- Fühlen: Vibrationen, Temperaturunterschiede, Ölkonsistenz

**Stufe 2 — Einfache Messungen (50–200 EUR Werkzeug)**
- Ölstand und -farbe prüfen
- Kühlmittelstand und -farbe prüfen
- Kraftstofffilter inspizieren
- Keilriemenspannung prüfen
- Batteriespannung messen
- Öldruckanzeige ablesen
- Temperaturanzeige ablesen
- Drehzahl prüfen (wenn Motor läuft)

**Stufe 3 — Erweiterte Diagnose (200–1.000 EUR Werkzeug)**
- Kompressionstest
- Öldruck mit Manometer messen (nicht Bordinstrument)
- Kraftstoffdruck messen
- Kühlsystemdruck-Prüfung
- Injektoren-Abdrückprüfung
- Ladedruckprüfung (Turbo)
- Multimeter-Messungen an Elektrik

**Stufe 4 — Spezialdiagnose (Fachwerkstatt)**
- Endoskopie (Zylinderinspektion)
- Ölanalyse im Labor
- Injektorprüfstand
- Diagnosegerät/CAN-Bus-Auslesen
- Zylinderkopf-Planlage prüfen
- Kurbelwellenspiel messen

### 1.4 Werkzeug-Grundausstattung für Bord-Diagnose

Jedes Fahrtenyachtbesatzungsmitglied sollte folgende Diagnosewerkzeuge an
Bord haben:

| Werkzeug | Einsatzbereich | Kosten |
|----------|---------------|--------|
| Digitalmultimeter | Elektrik, Sensoren | 30–80 EUR |
| Infrarot-Thermometer | Kühlsystem, Auspuff, Lager | 25–50 EUR |
| Kompressionstest-Set (Diesel) | Kompression | 40–100 EUR |
| Kraftstoff-Handpumpe | Entlüftung, Förderung | 15–30 EUR |
| Öldruckmanometer (0–10 bar) | Öldruck verifizieren | 20–50 EUR |
| Stethoskop (Mechaniker) | Geräuschlokalisierung | 10–25 EUR |
| Transparenter Schlauch (1m) | Kraftstoff-Lecksuche | 3–5 EUR |
| Spiegel + Taschenlampe | Sichtkontrolle | 10–20 EUR |
| Kabelbinder-Sortiment | Provisorien | 5–10 EUR |
| Dichtmasse (hochtemp.) | Notdichtung | 8–15 EUR |

### 1.5 Sicherheitshinweise bei der Motordiagnose

**WARNUNG — Lebensgefahr:**
- Motor NIEMALS in geschlossenem Raum ohne Abgasableitung laufen lassen.
  Kohlenmonoxid ist unsichtbar, geruchlos und tödlich.
- Rotierende Teile (Keilriemen, Lüfter, Schwungrad) können Finger und
  Kleidung erfassen. Nie bei laufendem Motor in Riemennähe arbeiten.
- Kühlsystem steht unter Druck. Verschlussdeckel NIE bei heißem Motor
  öffnen — Verbrühungsgefahr.
- Kraftstoff (Diesel) ist entzündlich. Keine offenen Flammen bei
  Kraftstoffarbeiten. Feuerlöscher bereithalten.
- Batterie: Kurzschluss erzeugt Funken und extreme Hitze. Hauptschalter
  aus bei Elektroarbeiten. Batteriesäure ist ätzend.
- Heißer Auspuff: Abgaskrümmer erreichen 400–600 °C. Erst abkühlen lassen.

### 1.6 Vorab-Checkliste vor jeder Fehlersuche

Bevor die eigentliche Diagnose beginnt, systematisch prüfen:

```
□  Ölstand korrekt? (zwischen MIN und MAX am Peilstab)
□  Kühlmittelstand korrekt? (Ausgleichsbehälter, NICHT bei heißem Motor)
□  Kraftstoff vorhanden? (Tank UND Leitungssystem)
□  Hauptschalter Batterie EIN?
□  Batteriespannung >12,4 V? (>24,8 V bei 24V-System)
□  Kraftstoffhahn offen? (Seeventil Kühlwasser offen?)
□  Getriebeölstand korrekt?
□  Sichtprüfung auf offensichtliche Leckagen?
□  Keilriemen vorhanden und gespannt?
□  Auspuffanlage frei? (Wassereinbruch? Verstopfung?)
```

---
---

## 2. Motor startet nicht — Vollständiger Entscheidungsbaum

### 2.1 Erste Unterscheidung: Dreht der Anlasser?

Die allererste Frage bei „Motor startet nicht" ist fundamental:

**A) Anlasser dreht NICHT**
→ Problem liegt im elektrischen Startkreis (Batterie, Kabel, Anlasser, Schalter)

**B) Anlasser dreht LANGSAM**
→ Batterie schwach, Masseverbindung schlecht, Anlasser defekt

**C) Anlasser dreht NORMAL, Motor springt nicht an**
→ Problem liegt bei Kraftstoff, Luft, Kompression oder Timing

**D) Motor springt an, stirbt sofort wieder ab**
→ Kraftstoffzufuhr unterbrochen, Luft im System, Sensor-Abschaltung

```
MOTOR STARTET NICHT
│
├── Anlasser dreht nicht? ──────────── → Kapitel 2.2 (Elektrik)
│
├── Anlasser dreht langsam? ────────── → Kapitel 2.3 (Batterie/Masse)
│
├── Anlasser dreht normal, kein Start? → Kapitel 2.4 (Kraftstoff/Luft/
│                                                      Kompression)
│
└── Startet kurz, stirbt ab? ──────── → Kapitel 2.5 (Kraftstoff/Sensor)
```

### 2.2 Anlasser dreht nicht — Elektrischer Startkreis

**Schritt 1: Batteriespannung messen**

| Spannung (12V-System) | Zustand | Maßnahme |
|-----------------------|---------|----------|
| > 12,6 V | Voll geladen | Batterie OK → weiter |
| 12,4 – 12,6 V | 75–100 % | Batterie wahrscheinlich OK → weiter |
| 12,0 – 12,4 V | 25–75 % | Nachladen, könnte noch reichen |
| 11,5 – 12,0 V | < 25 % | Zu schwach für Anlasser |
| < 11,5 V | Tiefentladen | Nicht startfähig |

**Schritt 2: Hauptschalter und Sicherungen**
- Batterie-Hauptschalter auf Position „EIN" oder „BOTH"?
- Sicherungskasten: Anlasser-Sicherung (oft 60–100 A) durchgebrannt?
- Thermosicherung am Anlasser-Relais ausgelöst?

**Schritt 3: Schaltkreis durchmessen**
```
Batterie(+) → Hauptschalter → Anlassrelais (Magnetschalter) → Anlasser
                                    ↑
                            Zündschloss/Startknopf
                                    ↑
                            Neutralstellung Getriebe
                            (Sicherheitsschalter)
```

Häufigste Ursachen in der Praxis:

| Rang | Ursache | Häufigkeit | Prüfung |
|------|---------|-----------|---------|
| 1 | Korrodierte Batterieklemmen | 30 % | Sichtprüfung, Klemmen abziehen |
| 2 | Schlechte Masseverbindung | 20 % | Spannungsabfall über Massekabel |
| 3 | Getriebe nicht in Neutral | 15 % | Schalthebel bewegen, Schalter prüfen |
| 4 | Defektes Startrelais | 12 % | Relais überbrücken (Achtung!) |
| 5 | Zündschloss defekt | 8 % | Durchgang messen |
| 6 | Anlasser defekt | 8 % | Direkt mit Kabel ansteuern |
| 7 | Sicherung durchgebrannt | 5 % | Sichtprüfung |
| 8 | Stop-Solenoid hängt | 2 % | Solenoid manuell prüfen |

**Korrodierte Batterieklemmen — Das häufigste Problem:**

Symptom: Grünlich-weiße Ablagerungen an den Klemmen. Beim Drehen des
Zündschlüssels passiert nichts, oder nur ein Klicken.

Sofortmaßnahme:
1. Klemmen abschrauben (ERST Minus, dann Plus)
2. Mit Drahtbürste oder Schleifpapier (Korn 120) reinigen
3. Polklemmen innen ebenfalls reinigen
4. Wieder anschließen (ERST Plus, dann Minus)
5. Polfett oder Vaseline auftragen

**Masseverbindung prüfen:**

Den Spannungsabfall zwischen Batterie-Minuspol und Motorblock messen,
während jemand den Anlasser betätigt:
- < 0,2 V: Masseverbindung OK
- 0,2 – 0,5 V: Grenzwertig, Verbindung reinigen
- > 0,5 V: Masseverbindung mangelhaft, muss erneuert werden

**Getriebe-Neutralschalter:**

Viele Motoren haben einen Sicherheitsschalter, der den Start nur bei
Getriebestellung „Neutral" erlaubt. Dieser Schalter kann:
- Dejustiert sein (Schaltgestänge hat sich gelöst)
- Korrodiert sein (Kontaktflächen oxidiert)
- Kabelbruch haben

Prüfung: Schalthebel mehrfach in Neutral bewegen. Wenn das nicht hilft,
den Schalter überbrücken (NUR zum Test, Getriebe muss sicher in Neutral
stehen!).

### 2.3 Anlasser dreht langsam — Batterie und Verkabelung

Symptom: Der Anlasser dreht hörbar, aber zu langsam. Der Motor kommt nicht
auf die nötige Drehzahl für Kompression und Zündung.

**Mindest-Drehzahl für Start:**

| Motortyp | Mindest-Startdrehzahl | Batterie-Mindestspannung |
|----------|----------------------|-------------------------|
| Saugdiesel (indirekt) | 80–100 U/min | 10,5 V unter Last |
| Saugdiesel (direkt) | 100–150 U/min | 11,0 V unter Last |
| Turbodiesel | 120–180 U/min | 11,0 V unter Last |
| Common-Rail | 150–250 U/min | 11,5 V unter Last |

**Spannungsabfall unter Last messen:**

1. Voltmeter an Batteriepolen anschließen
2. Startversuch durchführen (max. 10 Sekunden)
3. Spannung WÄHREND des Startens ablesen

| Spannung unter Last | Interpretation |
|--------------------|----------------|
| > 10,5 V (12V-Syst.) | Batterie OK, Problem anderswo |
| 9,5 – 10,5 V | Batterie grenzwertig oder alt |
| < 9,5 V | Batterie zu schwach, laden oder ersetzen |

**Ursachen und Maßnahmen:**

| Ursache | Prüfung | Maßnahme |
|---------|---------|----------|
| Batterie entladen | Spannung messen | Laden, Ursache für Entladung suchen |
| Batterie defekt (Zellschluss) | Säuredichte prüfen | Ersetzen |
| Kabelquerschnitt zu gering | Kabeldicke prüfen | Mindestens 50 mm² für 12V |
| Korrodierte Verbindungen | Spannungsabfall messen | Reinigen, nachziehen |
| Anlasser verschlissen | Kohlen prüfen | Anlasser überholen/ersetzen |
| Falsches Öl (zu zähflüssig) | SAE-Klasse prüfen | Korrekte Viskosität verwenden |

**Kaltstart-Probleme im Winter:**

Bei Temperaturen unter 5 °C:
- Batterieleistung sinkt um 30–50 % bei –10 °C
- Motoröl ist zähflüssiger, höherer Widerstand
- Dieselkraftstoff wird bei Kälte dickflüssiger (Versulzung ab –12 bis –20 °C)
- Glühkerzen müssen funktionieren

Maßnahmen:
- Batterie warm halten (isolierte Batteriebox)
- Winterdiesel ab November tanken (oder Fließverbesserer verwenden)
- Glühkerzenfunktion prüfen (Stromaufnahme messen: 5–8 A pro Glühkerze)
- Vorglühzeit einhalten (15–30 Sekunden bei modernen Motoren, bis 60 Sekunden bei alten)
- SAE 10W-40 oder 5W-40 statt SAE 15W-40 verwenden

### 2.4 Anlasser dreht normal, Motor springt nicht an

Wenn der Anlasser kräftig dreht, aber der Motor nicht anspringt, liegt das
Problem bei Kraftstoff, Luft/Kompression oder Timing.

**Entscheidungsbaum:**

```
Anlasser dreht normal, kein Start
│
├── Raucht es aus dem Auspuff?
│   │
│   ├── JA, weißer/grauer Rauch
│   │   → Kraftstoff kommt an, aber zündet nicht
│   │   → Glühkerzen defekt?
│   │   → Kompression zu niedrig?
│   │   → Einspritztiming falsch?
│   │   → Wasser im Kraftstoff?
│   │
│   ├── JA, schwarzer Rauch
│   │   → Zu viel Kraftstoff (Überspülung)
│   │   → Injektoren tropfen statt sprühen
│   │   → Luftfilter komplett verstopft
│   │
│   └── NEIN, kein Rauch
│       → Kein Kraftstoff an Zylindern
│       → Luft im System
│       → Stop-Solenoid geschlossen
│       → Kraftstofffilter verstopft
│       → Kraftstoffpumpe defekt
│       → Tank leer (Messgerät defekt?)
```

**Kraftstoff-Prüfung Schritt für Schritt:**

**Schritt 1: Kraftstoffvorrat prüfen**
- Tankstand kontrollieren (nicht nur Anzeige — Anzeigen können falsch sein)
- Bei Verdacht: Tank anklopfen (voll = dumpf, leer = hohl)
- Absperrhahn am Tank geöffnet?

**Schritt 2: Kraftstofffilter prüfen**
- Vorfilter/Wasserabscheider: Ist das Schauglas voll Wasser?
- Filterelement: Wann zuletzt gewechselt? Sichtprüfung auf Verschmutzung.
- Achtung: Ein verschmutzter Vorfilter bei leichtem Seegang kann
  Luft ziehen, wenn der Diesel im Tank schaukelt.

**Schritt 3: Entlüftung des Kraftstoffsystems**

Die häufigste Ursache für „Motor springt nicht an" nach Filterarbeiten
oder leerem Tank ist Luft im Kraftstoffsystem.

Entlüftungsprozedur (mechanische Einspritzung):
1. Entlüftungsschraube am Kraftstofffiltergehäuse öffnen
2. Handpumpe betätigen (am Vorfilter oder separate Membranpumpe)
3. Pumpen, bis Diesel blasenfrei aus Entlüftungsschraube kommt
4. Entlüftungsschraube schließen
5. Entlüftungsschraube an Einspritzpumpe öffnen
6. Handpumpe betätigen bis blasenfreier Diesel
7. Entlüftungsschraube schließen
8. Einspritzleitungen an Injektoren lösen (eine Umdrehung)
9. Anlasser betätigen bis Diesel an allen Injektoren austritt
10. Leitungen festziehen
11. Startversuch

Entlüftungsprozedur (Common-Rail):
- NICHT manuell entlüften! Die Hochdruck-Kraftstoffpumpe entlüftet
  das System selbstständig.
- Anlasser mehrfach 10–15 Sekunden betätigen (mit Pausen)
- Wenn nach 5 Versuchen kein Start: Niederdruck-Seite prüfen

**Schritt 4: Kraftstoffdruck prüfen**
- Mechanische Pumpe: Leitung am Filterausgang lösen, in Gefäß leiten,
  Anlasser betätigen → muss pulsierend Diesel kommen
- Elektrische Vorförderpumpe: Zündung EIN → Pumpe muss hörbar laufen
  (Summen), Druck an Prüfanschluss 0,3–0,5 bar
- Common-Rail: Raildruck beim Start > 250 bar erforderlich

**Schritt 5: Stop-Solenoid prüfen**

Ältere Motoren haben ein elektromagnetisches Ventil, das bei „STOP"
die Kraftstoffzufuhr unterbricht. Dieses Solenoid kann:
- Hängen bleiben (Feder gebrochen, Kolben korrodiert)
- Kein Signal bekommen (Kabelbruch, Relais defekt)

Prüfung:
- Manuell am Solenoid-Hebel ziehen → hörbar/fühlbar klicken?
- Spannung am Solenoid messen bei Zündung EIN: muss 12V/24V haben
- Notbehelf: Solenoid-Hebel manuell in Betriebsstellung fixieren

**Schritt 6: Glühkerzen prüfen**

Bei Temperaturen unter 15 °C oder bei indirekten Einspritzern (Vorkammer)
sind funktionsfähige Glühkerzen zum Start unerlässlich.

Glühkerzen-Prüfung:
1. Glühkerzenstecker abziehen
2. Widerstand jeder Glühkerze messen (Multimeter, Ohm)
   - Intakt: 0,5–2,0 Ω (je nach Typ)
   - Defekt: ∞ (Unterbrechung) oder 0 Ω (Kurzschluss)
3. Stromaufnahme messen: 5–8 A pro Glühkerze bei 12V
   - 4 Zylinder, 12V: Gesamtstrom beim Vorglühen ~20–30 A

| Glühkerzentyp | Aufheizzeit | Glühtemperatur | Lebensdauer |
|---------------|------------|----------------|-------------|
| Stabglühkerze (Standard) | 15–30 s | 850–1.000 °C | 3.000–5.000 h |
| Schnellglühkerze | 3–7 s | 1.000–1.100 °C | 5.000–8.000 h |
| Keramik-Glühkerze | 2–5 s | 1.200+ °C | 8.000–10.000 h |
| Nachglühkerze (Common-Rail) | 2–3 s | 1.100–1.350 °C | 10.000+ h |

**Schritt 7: Kompression prüfen**

Wenn Kraftstoff ankommt, Glühkerzen funktionieren, aber der Motor
nicht anspringt — Kompression prüfen (→ Kapitel 11).

Schnelltest ohne Werkzeug:
- Motor bei offenem Dekompressionsventil drehen (falls vorhanden),
  dann schließen → Motor muss deutlich schwerer drehen
- Luft aus dem Auspuff bei Startversuch? → Kompression vorhanden
- Kein Widerstand beim Durchdrehen → Kompression fehlt

### 2.5 Motor startet, stirbt sofort wieder ab

Der Motor springt an, läuft 2–10 Sekunden und geht dann aus. Dieses
Symptom deutet auf eine unterbrochene Kraftstoffversorgung hin.

**Häufigste Ursachen:**

| Rang | Ursache | Anteil | Prüfung |
|------|---------|--------|---------|
| 1 | Luft im Kraftstoffsystem | 35 % | Entlüften, Leitungen auf Undichtigkeit |
| 2 | Verstopfter Kraftstofffilter | 25 % | Filter wechseln |
| 3 | Wasser im Kraftstoff | 15 % | Wasserabscheider prüfen/entleeren |
| 4 | Diesel-Bug (Biomasse im Tank) | 10 % | Filterinspektion auf schwarzen Schleim |
| 5 | Defekte Kraftstoff-Förderpumpe | 5 % | Fördermenge prüfen |
| 6 | Kraftstoff-Rücklauf blockiert | 5 % | Rücklaufleitung prüfen |
| 7 | Elektronische Motorabschaltung | 3 % | Fehlercodes auslesen |
| 8 | Einspritzpumpen-Defekt | 2 % | Fachwerkstatt |

**Luft im Kraftstoffsystem lokalisieren:**

Luft gelangt IMMER auf der Saugseite (zwischen Tank und Einspritzpumpe)
ins System. Systematische Suche:

1. Alle Verschraubungen auf der Saugseite sichtprüfen
2. Jeden Anschluss nachziehen (1/4 Umdrehung reicht oft)
3. Transparenten Schlauch als Bypass einsetzen → Blasen sichtbar
4. Kritische Stellen:
   - Tankentnahme-Fitting
   - Absperrhahn
   - Vorfilter-Gehäuse (Dichtring!)
   - Kraftstofffilter-Gehäuse (Dichtring!)
   - Verbindung Leitung → Einspritzpumpe
   - Handpumpen-Membran (wenn porös, saugt Luft)

**Diesel-Bug erkennen:**

Diesel-Bug (Hormoconis resinae und verwandte Pilze) wächst an der
Grenzschicht zwischen Wasser und Diesel im Tank. Erkennungsmerkmale:
- Schwarze, schleimige Masse im Vorfilter
- Filter verstopft innerhalb weniger Stunden nach Wechsel
- Unangenehmer Geruch (faulige Eier / modrig)
- Oft im Frühjahr nach langer Standzeit im Winter

Sofortmaßnahme:
1. Filter wechseln (Reserve an Bord!)
2. Wasserabscheider entleeren
3. Tank bei nächster Gelegenheit reinigen und entkeimen
4. Biozid verwenden (z.B. Grotamar 82, Diesel Guard)
5. Tank möglichst voll halten (weniger Kondensation)

### 2.6 Motor startet schwer — Erweiterte Diagnose

Wenn der Motor zwar startet, aber nur nach vielen Versuchen oder erst
nach langem Orgeln:

**Kaltstart-Diagnose:**

| Symptom | Mögliche Ursache | Prüfung |
|---------|-----------------|---------|
| Startet nur nach 30+ Sek. Vorglühen | Glühkerzen schwach | Stromaufnahme messen |
| Startet erst beim 3.–5. Versuch | Luft im Kraftstoff | Entlüften, Leitungen prüfen |
| Startet nur mit Starthilfe | Kompression niedrig | Kompressionstest |
| Startet nur bei Gasgeben | Leerlaufdrehzahl zu niedrig | Leerlauf einstellen |
| Startet, qualmt weiß, dann OK | Einspritztiming | Timing prüfen/einstellen |
| Startet sofort, wenn warm | Glühkerzen ODER Kompression | Differenzdiagnose nötig |

**Differenzdiagnose Glühkerzen vs. Kompression:**

Wenn der Motor kalt schwer startet, aber warm sofort:
- Glühkerzen-Problem: Motor raucht weiß beim Start, kein Leistungsverlust
  wenn warm. Stromaufnahme beim Vorglühen messen.
- Kompressions-Problem: Motor raucht auch warm leicht, Leistungsverlust
  unter Last. Kompressionstest durchführen.

### 2.7 Startprobleme nach Winterlager

Nach der Winterpause sind typische Ursachen:

1. **Batterie tiefentladen**: Selbstentladung über 5–6 Monate
2. **Kraftstoff veraltet**: Diesel altert, Additive zersetzen sich
3. **Diesel-Bug gewachsen**: Standzeit + Restfeuchtigkeit = ideale Bedingungen
4. **Impeller verklebt**: Gummiflügel an Pumpengehäuse festgebacken
5. **Ventile kleben**: Führungen durch Ablagerungen schwergängig
6. **Dichtungen geschrumpft**: Kraftstoffleitungen saugen Luft
7. **Kondenswasser**: In Ölsystem, Kraftstoffsystem, Auspuff

Empfohlene Vorgehensweise nach Winterlager:
```
1. Batterie laden und prüfen (idealerweise vor Einbau)
2. Ölstand prüfen (Kondenswasser → milchig?)
3. Kühlmittelstand prüfen
4. Kraftstoff-Vorfilter und Hauptfilter wechseln
5. Kraftstoffsystem entlüften
6. Impeller prüfen (wenn nicht im Herbst gewechselt)
7. Seeventil Kühlwasser öffnen
8. Kurz Vorglühen, dann starten
9. Sofort Öldruckanzeige beobachten
10. Auspuff prüfen: kommt Kühlwasser?
```

---
---

## 3. Überhitzung — Kühlsystem-Diagnose

### 3.1 Wie das marine Kühlsystem funktioniert

Die meisten Yacht-Dieselmotoren verwenden ein Zweikreis-Kühlsystem:

```
INNENKREIS (geschlossen):
  Motor → Thermostat → Wärmetauscher → Wasserpumpe → Motor
  Kühlmittel: Wasser-Glykol-Gemisch (50:50)
  Temperatur: 75–95 °C (geregelt durch Thermostat)

AUSSENKREIS (offen, Seewasser):
  Seeventil → Seewasserfilter → Impeller-Pumpe → Wärmetauscher
    → Auspuff-Wasserinjektion → Auspuff über Bord
  Medium: Seewasser (oder Süßwasser je nach Revier)
  Temperatur: Eintritt 5–30 °C, Austritt 40–65 °C
```

**Direktgekühlt (ältere/einfache Motoren):**
Einige ältere oder einfachere Motoren (z.B. alte Yanmar 1GM) verwenden
nur einen Kreis mit Seewasser direkt durch den Motor. Diese Systeme
sind korrosionsanfälliger und der Motor läuft kälter (55–65 °C).

### 3.2 Überhitzungs-Warnstufen

| Temperatur | Stufe | Maßnahme |
|-----------|-------|----------|
| 75–90 °C | Normal | Normalbetrieb |
| 90–95 °C | Erhöht | Beobachten, Last reduzieren |
| 95–100 °C | Warnung | Last sofort reduzieren, Ursache suchen |
| 100–105 °C | Kritisch | Motor auf Leerlauf, Diagnose starten |
| > 105 °C | Gefahr | Motor SOFORT abstellen |
| > 110 °C | Notfall | Motor abstellen, Schäden wahrscheinlich |

**Folgeschäden durch Überhitzung:**

| Temperatur/Dauer | Mögliche Schäden |
|-----------------|-----------------|
| 105 °C, 10 min | Zylinderkopfdichtung kann Schaden nehmen |
| 110 °C, 5 min | Kopfdichtung bläst durch, Kopf kann sich verziehen |
| 115 °C, 2 min | Kolbenfresser möglich, Ventilführungen zerstört |
| > 120 °C | Motorschaden sehr wahrscheinlich, Totalschaden möglich |

### 3.3 Systematische Kühlsystem-Diagnose

**Entscheidungsbaum Überhitzung:**

```
MOTOR ÜBERHITZT
│
├── Kommt Kühlwasser aus dem Auspuff?
│   │
│   ├── NEIN → Seewasser-Kreis Problem
│   │   ├── Seeventil geschlossen? → Öffnen
│   │   ├── Seewasserfilter verstopft? → Reinigen
│   │   ├── Impeller defekt? → Wechseln
│   │   ├── Seewasserleitung verstopft? → Durchblasen
│   │   └── Wärmetauscher Seewasser-Seite verstopft? → Reinigen
│   │
│   └── JA, aber wenig → Teilweise Blockade
│       ├── Impeller teilweise defekt (Flügel fehlen)?
│       ├── Seewasserfilter teilweise verstopft?
│       └── Wärmetauscher teilweise zugesetzt?
│
├── Kühlwasser kommt normal, trotzdem zu heiß
│   ├── Thermostat klemmt geschlossen? → Prüfen/Wechseln
│   ├── Wärmetauscher Innenkreis verstopft? → Spülen
│   ├── Innenkreis-Wasserpumpe defekt? → Prüfen
│   ├── Keilriemen rutscht (Pumpenantrieb)? → Spannen/Wechseln
│   ├── Zylinderkopfdichtung defekt? → Kapitel 3.8
│   └── Motor überlastet? → Last reduzieren
│
└── Temperaturanzeige schwankt stark
    ├── Thermostat klemmt intermittierend?
    ├── Luftblase im Innenkreis?
    └── Temperatursensor defekt?
```

### 3.4 Seeventil (Seacock)

**Problem:** Seeventil nicht vollständig geöffnet oder teilweise zugesetzt.

**Symptom:** Kein oder wenig Kühlwasser aus dem Auspuff, Motor überhitzt
langsam (über 10–20 Minuten).

**Prüfung:**
- Seeventilhebel auf „offen" prüfen (parallel zum Rohr = offen)
- Beweglichkeit prüfen (Hebel muss sich leicht bewegen lassen)
- Von außen: Ist der Ansaugbereich am Rumpf frei? (Muscheln, Algen, Plastiktüte)

**Maßnahme:**
- Öffnen wenn geschlossen
- Wenn schwergängig: NICHT mit Gewalt bewegen (Bruchgefahr bei alten
  Bronzeventilen). Stattdessen Ventil warten (schmieren oder ersetzen)
  beim nächsten Trockenlegen.

### 3.5 Seewasserfilter (Strainer)

**Problem:** Seewasserfilter verstopft durch Seegras, Quallen, Muscheln,
Sand oder Plastikteile.

**Symptom:** Kühlwasseraustritt am Auspuff reduziert, Motor überhitzt
unter Last schneller als im Leerlauf.

**Prüfung:**
- Transparentes Filtergehäuse inspizieren
- Wenn nicht transparent: Deckel öffnen (ERST Seeventil schließen!)
- Filterkorb entnehmen und reinigen
- Dichtfläche des Deckels prüfen (Dichtring intakt? Sauber?)

**Wartungsintervall:**
- Alle 50 Betriebsstunden kontrollieren
- In Tropengewässern mit viel Seegras: alle 10–20 Stunden
- Filter IMMER an Bord haben als Ersatz

**Häufiger Fehler:** Deckel nach Reinigung nicht richtig verschlossen →
Impeller saugt Luft statt Wasser → kein Kühlwasser → Überhitzung!

### 3.6 Impeller (Seewasserpumpe)

**Problem:** Der Gummi-Impeller in der Seewasserpumpe ist das häufigste
Verschleißteil im Kühlsystem. Flügel brechen ab, verformen sich oder
verschleißen.

**Symptom:**
- Kein Kühlwasser aus dem Auspuff (bei totalem Ausfall)
- Reduzierter Kühlwasserfluss (bei Teilverlust von Flügeln)
- Überhitzung besonders unter Last
- Gummipartikel im Seewasserfilter

**Lebensdauer und Wechselintervall:**

| Betriebsart | Empfohlenes Wechselintervall |
|-------------|------------------------------|
| Saisonbetrieb (300 h/Jahr) | Jährlich vor Saisonstart |
| Charterbetrieb (1.000+ h/Jahr) | Alle 500 Betriebsstunden |
| Blauwasser/Langfahrt | Alle 1.000 Stunden oder jährlich |
| Trockenlauf (>30 Sek.) | Sofort wechseln |

**WICHTIG:** Impeller NIEMALS trocken laufen lassen. Bereits 15–30 Sekunden
Trockenlauf können den Impeller zerstören (Gummi schmilzt am Gehäuse fest).
Daher: IMMER Seeventil öffnen VOR dem Motorstart.

**Impeller-Wechsel Kurzanleitung:**
1. Seeventil schließen
2. Pumpendeckel abschrauben (2–4 Schrauben)
3. Alten Impeller herausziehen (Impeller-Zange verwenden)
4. ALLE Flügel zählen! Fehlende Flügel stecken im System
   (Wärmetauscher, Auspuffkrümmer) und müssen gefunden werden
5. Neuen Impeller mit Glycerin oder Spülmittel einsetzen
   (NIEMALS Silikonfett — schädigt den Gummi)
6. Deckel mit neuer Dichtung montieren
7. Seeventil öffnen
8. Motor starten und Kühlwasseraustritt prüfen

**Fehlende Impellerflügel:**

Wenn beim Wechsel Flügel fehlen, stecken diese:
- Im Wärmetauscher (70 % der Fälle) → Endkappe öffnen, Rohrbündel prüfen
- Im Auspuffkrümmer/Wasserinjektor (25 %) → Wasserinjektor öffnen
- In der Auspuffleitung (5 %) → Schwer zu finden, aber meist harmlos

Nicht gefundene Gummiflügel können den Wärmetauscher teilweise blockieren
und langfristig zu Überhitzung führen.

### 3.7 Thermostat

**Problem:** Thermostat klemmt geschlossen oder offen.

**Thermostat klemmt geschlossen:**
- Symptom: Motor überhitzt relativ schnell, auch im Leerlauf.
  Kühlwasser kommt normal aus dem Auspuff (Seewasserkreis OK).
- Ursache: Wachselement im Thermostat defekt oder Ablagerungen
  verhindern Öffnung.
- Prüfung: Thermostat ausbauen. In Topf mit Wasser und Thermometer
  langsam erhitzen. Muss bei Nenntemperatur öffnen:
  - Yanmar: 71 °C (3JH, 4JH) oder 82 °C (4LHA, 6LY)
  - Volvo: 76 °C (D1/D2) oder 83 °C (D3+)
  - Beta: 82 °C
- Hub bei voller Öffnung: 8–12 mm je nach Typ

**Thermostat klemmt offen:**
- Symptom: Motor wird nicht warm (Anzeige bleibt bei 50–60 °C).
  Höherer Kraftstoffverbrauch, erhöhte Rußbildung, schnellere
  Zylinderwandverschleiß.
- Maßnahme: Thermostat ersetzen.

**Notbehelf bei klemmendem Thermostat (auf See):**
- Thermostat AUSBAUEN und Motor ohne Thermostat betreiben.
- Motor läuft dann kälter als normal (50–65 °C statt 82 °C),
  aber er überhitzt nicht.
- Bei nächster Gelegenheit neuen Thermostat einbauen.

### 3.8 Wärmetauscher (Heat Exchanger)

**Problem:** Der Wärmetauscher kann auf beiden Seiten verstopfen:

**Seewasser-Seite verstopft:**
- Ursache: Kalkablagerungen, Salzablagerungen, Muscheln, Gummiteile
  vom Impeller.
- Symptom: Überhitzung unter Last, Kühlwasserfluss aus Auspuff reduziert.
- Prüfung: Endkappen demontieren, Rohrbündel inspizieren.
- Maßnahme: Chemische Reinigung mit verdünnter Essig- oder Zitronensäure
  (5–10 %) über Nacht einweichen. Dann mit Frischwasser spülen.
  Alternativ: Spezieller Seewasser-Reiniger (Barnacle Buster, Rydlyme).

**Innenkreis-Seite verstopft:**
- Ursache: Rostpartikel (wenn Kühlmittel nicht gewechselt wurde),
  Dichtungsreste, Ablagerungen von altem Kühlmittel.
- Symptom: Überhitzung trotz funktionierendem Seewasserkreis.
- Prüfung: Kühlmittelfarbe prüfen (rostbraun = schlecht), Durchfluss
  prüfen (Thermostatgehäuse öffnen und Strömung beobachten).
- Maßnahme: Innenkreis mit Kühlsystemreiniger spülen, Kühlmittel
  komplett wechseln.

**Lebensdauer:**
- Kupfer-Nickel-Wärmetauscher: 15–20 Jahre bei guter Wartung
- Edelstahl-Wärmetauscher: 20–30 Jahre
- Zinkanode im Wärmetauscher: jährlich prüfen und ersetzen

### 3.9 Zylinderkopfdichtung — Diagnose

**Problem:** Eine defekte Zylinderkopfdichtung lässt Verbrennungsgase
ins Kühlsystem, Kühlmittel in den Brennraum oder Öl ins Kühlsystem
(oder umgekehrt) eindringen.

**Symptome einer defekten Kopfdichtung:**

| Symptom | Mechanismus |
|---------|------------|
| Kühlmittel im Ausgleichsbehälter blubbert | Verbrennungsgase im Kühlsystem |
| Weißer süßlich riechender Rauch | Kühlmittel verbrennt im Zylinder |
| Ölfilm auf Kühlmittel | Öl dringt ins Kühlsystem |
| Kühlmittel im Öl (milchig) | Kühlmittel dringt ins Ölsystem |
| Kühlmittelverlust ohne sichtbare Leckage | Kühlmittel geht in Zylinder |
| Überhitzung trotz funktionierendem System | Heißgase im Kühlsystem |
| Druckaufbau im Kühlsystem (Schlauch hart) | Verbrennungsdruck im Kühlsystem |

**Diagnose-Verfahren:**

**Test 1: CO₂-Test (chemischer Blocktest)**
- Spezielles Testfluid (blau) in Trichter auf Ausgleichsbehälter
- Motor laufen lassen
- Fluid färbt sich GELB wenn CO₂ (Verbrennungsgase) vorhanden
- Eindeutig: Kopfdichtung defekt

**Test 2: Drucktest Kühlsystem**
- Kühlsystem-Druckprüfer aufsetzen (statt Verschlussdeckel)
- Auf 1,0–1,5 bar aufpumpen
- 15 Minuten beobachten
- Druckabfall > 0,2 bar: Leckage vorhanden
- Motor starten: Druck steigt unkontrolliert → Kopfdichtung

**Test 3: Öl-Peilstab prüfen**
- Milchig/schokoladig = Wasser im Öl
- SOFORT Motor abstellen — Lagerschaden droht!

**Test 4: Auspuff beobachten**
- Weißer, süßlich riechender Rauch der nicht aufhört = Kühlmittel
  (normaler weißer Rauch beim Kaltstart verschwindet nach 2–5 Minuten)

### 3.10 Überhitzung bei bestimmten Betriebsbedingungen

**Überhitzt nur unter Volllast:**
- Kühlsystem-Kapazität grenzwertig (teilweise Verstopfung)
- Wärmetauscher teilweise zugesetzt
- Impeller verschlissen (fördert noch, aber nicht genug)
- Propeller zu groß (Motor überlastet)

**Überhitzt nur bei niedrigen Drehzahlen:**
- Keilriemen rutscht bei niedriger Drehzahl (Wasserpumpen-Antrieb)
- Thermostat öffnet nicht richtig (braucht mehr Durchfluss)

**Überhitzt nur bei hohen Außentemperaturen:**
- Kühlsystem-Kapazität am Limit
- Wärmetauscher muss gereinigt werden
- Seewasser-Einlass im Bereich einer Warmwasserschicht

**Überhitzt nur rückwärts fahrend:**
- Seewassereinlass wird durch Fahrstrom blockiert (bei Rückwärtsfahrt)
- Lösung: Größeren Seewassereinlass installieren

**Überhitzt nach Rumpfreinigung/Antifouling:**
- Seewassereinlass wurde versehentlich überstrichen
- Antifouling vor dem Seewassergitter reinigen

---
---

## 4. Rauchfarbe-Diagnose

### 4.1 Grundlagen der Rauchdiagnose

Die Farbe des Abgasrauchs ist einer der wichtigsten visuellen
Diagnoseindikatoren bei Dieselmotoren. Ein gesunder, warmer Dieselmotor
produziert nahezu unsichtbaren Auspuff (leicht bläulicher Dunst,
schnell auflösend).

```
RAUCHFARBE-DIAGNOSE
│
├── SCHWARZ ──── Kraftstoffüberschuss / unvollständige Verbrennung
│
├── WEISS ─────── Kühlmittel ODER unverdampfter Kraftstoff
│                  (Unterscheidung wichtig!)
│
├── BLAU ──────── Ölverbrennung
│
├── GRAU ──────── Übergangsphase / leichter Fall von schwarz oder blau
│
└── KEIN RAUCH ── Normal (warm) ODER kein Kraftstoff (beim Start)
```

### 4.2 Schwarzer Rauch — Kraftstoff-Überschuss

Schwarzer Rauch bedeutet: Es wird mehr Kraftstoff eingespritzt als
die verfügbare Luft verbrennen kann. Die unverbrannten Kohlenwasserstoffe
erscheinen als Rußpartikel.

**Ursachen und Diagnose:**

| Ursache | Häufigkeit | Diagnose | Lösung |
|---------|-----------|----------|--------|
| Luftfilter verstopft | 25 % | Filter inspizieren, Druckdifferenz | Filter wechseln |
| Motor überlastet | 20 % | Drehzahl unter Volllast prüfen | Propeller anpassen |
| Injektor tropft/sprüht schlecht | 20 % | Abdrücktest, Spritzbild | Injektor überholen |
| Turbolader defekt | 10 % | Ladedruck messen, Spiel prüfen | Turbo überholen |
| Ventilspiel falsch | 8 % | Ventilspiel messen | Einstellen |
| Einspritztiming falsch | 7 % | Timing prüfen | Neu einstellen |
| EGR-Ventil verstopft (modern) | 5 % | EGR prüfen | Reinigen/ersetzen |
| Ladeluftkühler verstopft | 3 % | Druckdifferenz, Sichtprüfung | Reinigen |
| Kopfdichtung (Kompression↓) | 2 % | Kompressionstest | Kopfdichtung wechseln |

**Luftfilter-Probleme im maritimen Einsatz:**

Marine-Luftfilter verschmutzen schneller als an Land:
- Salzablagerungen am Filterelement
- Feuchtigkeit lässt Filter aufquellen
- Fettdämpfe aus dem Motorraum lagern sich ab
- Insekten und Spinnenweben in der Ansaugung

Filtertypen und Wartung:
| Typ | Wechselintervall | Reinigungsmöglichkeit |
|-----|------------------|-----------------------|
| Papierfilter | 200–500 Betriebsstunden | Nicht waschbar, ersetzen |
| Schaumstofffilter | 100–200 Stunden | In Spülmittel waschen, nachölen |
| Ölbadfilter (alt) | Alle 100 Stunden Öl wechseln | Reinigen und neu befüllen |
| Zyklon-Vorfilter | Alle 200 Stunden leeren | Auffangbehälter leeren |

**Turbolader-Diagnose:**

Symptome eines defekten Turboladers:
- Schwarzer Rauch unter Last
- Leistungsverlust
- Pfeifen oder Kreischen (Lagerschaden)
- Öl im Ladeluftrohr (Wellendichtung defekt)
- Öl im Auspuff (Turbinen-Wellendichtung)

Schnellcheck:
1. Ladeluftschlauch von Turbo zum Motor abnehmen
2. Turbinenrad per Hand drehen — muss sich leicht und ohne Schleifen drehen
3. Radialspiel prüfen — darf max. 0,05–0,08 mm sein
4. Axialspiel prüfen — darf max. 0,03–0,05 mm sein
5. Schaufelblätter inspizieren — keine Riefen, keine fehlenden Stücke

**Motor-Überlastung erkennen:**

Ein überlasteter Motor produziert schwarzen Rauch, weil die Drehzahl
bei Volllast nicht erreicht wird und die Einspritzpumpe mehr Kraftstoff
liefert als die Luftmenge verbrennen kann.

Prüfung: Drehzahl unter Volllast mit sauberem Unterwasserschiff messen.

| Motortyp | Soll-Vollast-Drehzahl | Toleranz |
|----------|----------------------|----------|
| Yanmar 3JH | 3.400 U/min | ±100 |
| Yanmar 4JH | 3.400 U/min | ±100 |
| Volvo D1-30 | 3.200 U/min | ±100 |
| Volvo D2-40 | 3.200 U/min | ±100 |
| Volvo D2-75 | 3.000 U/min | ±100 |
| Beta 38 | 3.600 U/min | ±100 |

Wenn die Drehzahl >200 U/min unter Soll:
- Bewuchs am Unterwasserschiff (häufigste Ursache!)
- Propeller zu groß (Pitch zu hoch)
- Propeller beschädigt (verformt)
- Getriebe schwergängig
- Wellenlager verschlissen

### 4.3 Weißer Rauch — Kühlmittel oder Kraftstoff

Weißer Rauch hat ZWEI grundlegend verschiedene Ursachen, die unterschieden
werden müssen:

**A) Kühlmittel-Dampf (ERNST):**
- Dicker, süßlich riechender weißer Rauch
- Verschwindet NICHT nach Warmfahren
- Kühlmittelstand sinkt
- → Kopfdichtung defekt (→ Kapitel 3.9)

**B) Unverdampfter Kraftstoff (meist harmlos):**
- Dünner, leicht bläulich-weißer Rauch
- Riecht nach Diesel
- Verschwindet nach 2–10 Minuten Warmfahren
- Normal bei kaltem Motor, besonders bei Temperaturen <10 °C
- → Glühkerzen prüfen, Einspritztiming prüfen

**Unterscheidung:**

| Merkmal | Kühlmittel | Unverdampfter Diesel |
|---------|-----------|---------------------|
| Geruch | Süßlich, chemisch | Diesel |
| Konsistenz | Dicht, dampfartig | Dünn, schnell auflösend |
| Verschwindet nach Warmfahren? | NEIN | JA |
| Kühlmittelstand sinkt? | JA | NEIN |
| Öl milchig? | Möglich | NEIN |
| Frostschutz-Test am Auspuff? | POSITIV | NEGATIV |

**Weißer Rauch nach Injektor-Arbeit:**
Wenn nach einem Injektorwechsel weißer Rauch auftritt, ist oft
eine Injektordichtung (Kupfer-Unterlegscheibe) nicht korrekt montiert.
Undichter Injektor → Diesel tropft statt sprüht → weiße Rauch.

### 4.4 Blauer Rauch — Ölverbrennung

Blauer Rauch bedeutet: Motoröl gelangt in den Brennraum und verbrennt mit.
Der Rauch hat einen charakteristischen, beißenden Geruch.

**Ursachen und Diagnose:**

| Ursache | Häufigkeit | Diagnose | Schwere |
|---------|-----------|----------|---------|
| Ventilschaftdichtungen verschlissen | 30 % | Rauch nach Start, dann weg | Mittel |
| Kolbenringe verschlissen | 25 % | Rauch unter Last, Ölverbrauch | Schwer |
| Turbo-Wellendichtung (druckseitig) | 15 % | Öl im Ladeluftschlauch | Mittel |
| Turbo-Wellendichtung (abgasseitig) | 10 % | Rauch auch im Leerlauf | Mittel |
| Zylinder verschlissen (Ovalität) | 10 % | Kompressionstest, Ölanalyse | Schwer |
| Zu viel Öl eingefüllt | 5 % | Ölstand prüfen | Einfach |
| Kurbelgehäuseentlüftung verstopft | 5 % | Druck im Kurbelgehäuse | Einfach |

**Differenzdiagnose — Wann raucht es blau?**

| Zeitpunkt | Wahrscheinliche Ursache |
|-----------|------------------------|
| Sofort nach Motorstart (warm+kalt) | Ventilschaftdichtungen |
| Nur beim Beschleunigen / unter Last | Kolbenringe |
| Dauerhaft, auch im Leerlauf | Turbo-Dichtung ODER schwerer Kolbenring-Verschleiß |
| Nach längerem Leerlauf, dann Last | Kombination Ventilschaft + Ringe |
| Nur bei starker Krängung (Segel) | Öl läuft in unteren Zylinder (Einbaulage) |

**Ölverbrauch-Referenzwerte:**

| Motor-Zustand | Ölverbrauch pro 100 h |
|--------------|----------------------|
| Neuer Motor (Einlaufphase) | 0,2–0,5 l |
| Normal eingelaufener Motor | 0,1–0,3 l |
| Verschleiß erkennbar | 0,5–1,0 l |
| Überholungsbedürftig | > 1,0 l |
| Kritisch | > 2,0 l |

### 4.5 Rauchfarbe bei verschiedenen Betriebszuständen

**Tabelle: Rauch + Betriebszustand = Diagnose**

| Betriebszustand | Schwarz | Weiß | Blau |
|----------------|---------|------|------|
| Kaltstart | Normal (kurz) | Normal (kurz) | Ventilschaftdichtung |
| Leerlauf, kalt | Einspritztiming | Glühkerzen | Turbo-Dichtung |
| Leerlauf, warm | Injektor tropft | Kopfdichtung | Turbo-Dichtung |
| Teillast | Luftfilter, Turbo | Kopfdichtung | Ringe + Ventilschaft |
| Volllast | Überlastung | Kopfdichtung | Ringe schwer verschl. |
| Beschleunigung | Normal (kurz) | Abnormal | Ringe |
| Abstellen | — | Normal (Kondens.) | Turbo-Nachlauföl |

---
---

## 5. Öldruck-Probleme

### 5.1 Normaler Öldruck — Referenzwerte

| Motor-Zustand | Öldruck (bar) |
|--------------|---------------|
| Leerlauf, warm (80 °C) | 1,0–2,0 |
| Leerlauf, kalt (20 °C) | 2,0–4,0 |
| Betriebsdrehzahl (2.500–3.000) | 3,0–5,0 |
| Volllast | 3,5–6,0 |
| Alarm (unterer Grenzwert) | < 0,5–0,8 |

**WICHTIG:** Diese Werte variieren je nach Hersteller und Motortyp.
Immer die Herstellerangaben als Referenz verwenden.

**Herstellerspezifische Alarmgrenzen:**

| Hersteller/Motor | Alarm-Druck | Anmerkung |
|-----------------|-------------|-----------|
| Yanmar 3JH/4JH | 0,5 bar | Bei Nenndrehzahl |
| Yanmar 4LHA | 0,7 bar | Bei Nenndrehzahl |
| Volvo D1/D2 | 0,5 bar | Bei Leerlauf |
| Volvo D3/D4/D6 | 0,7 bar | Bei Leerlauf |
| Beta 14–50 | 0,5 bar | Bei Betriebsdrehzahl |
| Nanni N-Serie | 0,5 bar | Bei Betriebsdrehzahl |

### 5.2 Niedriger Öldruck — Systematische Diagnose

```
ÖLDRUCK ZU NIEDRIG
│
├── Ölstand prüfen
│   ├── Zu niedrig → Öl nachfüllen, Leckage suchen
│   └── OK → weiter
│
├── Ölzustand prüfen
│   ├── Milchig → Wasser im Öl → STOP (Kopfdichtung?)
│   ├── Dieselgeruch → Kraftstoff im Öl → STOP (Injektor?)
│   ├── Schwarz, dünn → Öl überaltert → Ölwechsel
│   └── Normal → weiter
│
├── Öldruck mit Manometer verifizieren
│   ├── Bordanzeige falsch → Sensor/Anzeige defekt
│   └── Tatsächlich niedrig → weiter
│
├── Ölfilter
│   ├── Verstopft → Wechseln
│   └── OK → weiter
│
└── Interne Ursachen (Werkstatt)
    ├── Ölpumpe verschlissen
    ├── Druckbegrenzungsventil klemmt offen
    ├── Lagerspiel zu groß (Pleuel/Haupt/Nockenwelle)
    └── Ölkanal-Verstopfung
```

**Sensor vs. echtes Problem:**

In ca. 30 % der Fälle zeigt die Bordelektrik einen niedrigen Öldruck
an, obwohl der tatsächliche Druck normal ist.

Prüfung: Mechanisches Öldruckmanometer an den Prüfanschluss des Motors
anschließen (meist am Ölfiltergehäuse). Motor laufen lassen und beide
Werte vergleichen.

| Bordinstrument | Manometer | Diagnose |
|---------------|-----------|----------|
| Niedrig/Alarm | Normal (>2 bar) | Sensor oder Anzeige defekt |
| Niedrig/Alarm | Niedrig (<1 bar) | Echtes Öldruck-Problem |
| Normal | Normal | Alles OK, Fehlalarm |
| Normal | Niedrig | Sensor defekt (zeigt falsch hoch) |

**Öldrucksensor-Typen:**

| Typ | Funktion | Fehlermode |
|----|---------|------------|
| Öldruckschalter (Warnlampe) | Schaltet bei Grenzdruck | Undicht, Kontakt oxidiert |
| Druckgeber (Anzeige) | Proportionales Signal | Drift, Kurzschluss, Massefehler |
| Druckgeber (CAN-Bus) | Digitales Signal | Sensordefekt, CAN-Fehler |

**Kraftstoff im Öl:**

Wenn der Öldruck niedrig ist UND das Öl nach Diesel riecht und
dünnflüssiger ist als normal:
- Injektor-Dichtung undicht → Diesel läuft am Injektor vorbei ins Öl
- Einspritzpumpen-Membran undicht (ältere Motoren)
- Hochdruckpumpen-Dichtung (Common-Rail)
- SOFORT Ölwechsel durchführen
- Ursache beheben vor erneutem Betrieb

### 5.3 Hoher Öldruck

Hoher Öldruck (> 6 bar bei Betriebstemperatur) ist seltener als niedriger
Druck, aber ebenfalls problematisch.

**Ursachen:**

| Ursache | Häufigkeit | Diagnose |
|---------|-----------|----------|
| Falsches Öl (zu hohe Viskosität) | 40 % | SAE-Klasse prüfen |
| Druckbegrenzungsventil klemmt geschlossen | 25 % | Ventil prüfen (Werkstatt) |
| Ölkanal verstopft | 15 % | Ölanalayse, Motorspülung |
| Kalt, normaler Zustand | 15 % | Nach Warmfahren prüfen |
| Sensor/Anzeige defekt | 5 % | Manometer-Vergleich |

**Falsches Öl — häufiger Fehler:**

| Motor-Empfehlung | Verwendet | Problem |
|-----------------|-----------|---------|
| SAE 15W-40 | SAE 20W-50 | Zu zäh, besonders kalt |
| SAE 10W-40 | SAE 15W-40 | Grenzwertig bei Kälte |
| CF/CI-4 | API SN (Benziner-Öl) | Falsche Additivierung |

### 5.4 Öldruck-Schwankungen

Schwankender Öldruck kann verschiedene Ursachen haben:

| Symptom | Ursache | Maßnahme |
|---------|---------|----------|
| Öldruck schwankt bei Wellengang | Ölstandsänderung durch Krängung | Normal wenn kurzzeitig |
| Öldruck fällt bei Kurvenfahrt | Ölstandsänderung, Ölpumpe saugt Luft | Ölstand prüfen (zu niedrig?) |
| Öldruck flackert im Leerlauf | Ölpumpe verschlissen ODER Sensor | Manometer prüfen |
| Öldruck fällt nach 30 Min. Betrieb | Öl wird zu dünn (warm) | Ölzustand, Viskosität prüfen |
| Öldruck normal bei Kalt, niedrig bei Warm | Lagerspiel zu groß | Motorrevision fällig |

---
---

## 6. Vibrationen und Geräusche

### 6.1 Systematische Vibrationsisolierung

Vibrationen können von verschiedenen Quellen stammen. Die systematische
Isolierung erfordert schrittweises Ausschließen:

```
VIBRATION/GERÄUSCH
│
├── Schritt 1: Motor im Leerlauf (Getriebe Neutral)
│   ├── Vibration vorhanden → Motor-intern ODER Motorlager
│   └── Keine Vibration → weiter mit Schritt 2
│
├── Schritt 2: Motor im Leerlauf + Getriebe eingelegt
│   ├── Vibration beginnt → Getriebe ODER Kupplung
│   └── Keine Vibration → weiter mit Schritt 3
│
├── Schritt 3: Unter Fahrt, niedrige Drehzahl
│   ├── Vibration beginnt → Welle ODER Propeller ODER Stevenrohr
│   └── Keine Vibration → weiter mit Schritt 4
│
├── Schritt 4: Unter Fahrt, mittlere Drehzahl
│   ├── Vibration beginnt → Resonanz bei bestimmter Drehzahl
│   └── Keine Vibration → weiter mit Schritt 5
│
└── Schritt 5: Unter Fahrt, Volllast
    └── Vibration → Propellerkavitation, Überlast, Resonanz
```

### 6.2 Motorlager-Probleme

**Funktion der Motorlager:**
Flexible Motorlager (Gummi-Metall-Lager) isolieren den Motor vom Rumpf.
Sie absorbieren Vibrationen und gleichen thermische Ausdehnung und
Wellenflucht-Abweichungen aus.

**Symptome defekter Motorlager:**

| Symptom | Interpretation |
|---------|---------------|
| Zunehmende Vibrationen im Rumpf | Gummi verhärtet oder gerissen |
| Metallisches Klopfen beim Gasgeben | Lager gerissen, Motor schlägt |
| Motor bewegt sich sichtbar | Lager gebrochen oder lose |
| Vibrationen nur bei bestimmter Drehzahl | Resonanzfrequenz getroffen |
| Wellenanlage macht Geräusche | Fluchtung durch Lagersetzung falsch |

**Prüfung:**
1. Sichtprüfung: Gummi rissig, aufgequollen oder verformt?
2. Motor mit Hebel leicht anheben: Bewegt sich ein Lager deutlich
   mehr als die anderen?
3. Gummi mit Finger drücken: Hart und brüchig = alt und verbraucht
4. Ölkontamination: Diesel oder Öl auf dem Gummi zersetzt ihn schnell

**Lebensdauer:**
- Normal: 5–10 Jahre / 3.000–8.000 Betriebsstunden
- Bei Ölkontamination: 2–3 Jahre
- Bei Überlast/Vibration: 3–5 Jahre

**Motorlager-Einstellung nach Wechsel:**

Alle vier Lager müssen korrekt eingestellt werden, um die Wellenanlage
auszurichten. Maximale Fluchtungstoleranz:
- Radial: < 0,05 mm
- Angular: < 0,5 mm/m Wellenlänge

### 6.3 Kupplung und Getriebe

**Kupplungs-Geräusche:**

| Geräusch | Zustand | Ursache |
|----------|---------|---------|
| Rattern bei Neutral | Motor läuft, Getriebe nicht | Getriebe-Zahnspiel zu groß |
| Schlag beim Einlegen | Vorwärts oder Rückwärts | Kupplungsbeläge verschlissen |
| Quietschen bei Einlegen | Übergangsmoment | Kupplungsscheibe verglast |
| Dauerndes Heulen im Gang | Unter Fahrt | Getriebelager verschlissen |
| Klappern bei niedriger Drehzahl | Im Gang, niedrige Drehzahl | Propeller-Flattern |

**Getriebe-Diagnose:**

1. Getriebeölstand prüfen (eigener Peilstab oder Einfüllschraube)
2. Getriebeöl-Zustand: Klar und sauber? Metallspäne? Milchig (Wasser)?
3. Getriebeöl-Geruch: Verbrannt = Kupplungsbeläge verschlissen
4. Temperatur: Getriebe handwarm (40–60 °C) = normal

### 6.4 Propeller-Vibrationen

**Propeller-Probleme und Symptome:**

| Problem | Vibration | Geräusch | Sonstiges |
|---------|----------|----------|-----------|
| Verbogenes Blatt | Periodisch, drehzahlabhängig | Wummern | Leistungsverlust |
| Abgebrochenes Blatt | Stark, drehzahlabhängig | Schlagen | Starke Vibrationen |
| Bewuchs am Propeller | Leicht, zunehmend | Rauschen | Leistungsverlust |
| Angeleine um Welle | Vibration + Widerspiel | Klopfen | Überhitzung Stopfbuchse |
| Kavitation | Bei hoher Drehzahl | Zischen/Kratzen | Oberflächennarben |
| Lose Propellermutter | Vibration + Spiel | Klappern | Gefahr: Propeller verlieren |

**Angeleine um Welle (häufiges Problem):**

Symptome:
- Plötzlich auftretende Vibrationen
- Steigende Temperatur an der Stopfbuchse
- Drehzahl sinkt bei gleichem Gas
- Im schlimmsten Fall: Motor bleibt stehen

Sofortmaßnahme auf See:
1. Motor sofort abstellen
2. Taucher oder Selbsttauchen (wenn sicher möglich)
3. Leine mit Messer durchschneiden
4. Stopfbuchse auf Überhitzungsschäden prüfen
5. Langsam wieder anfahren, auf Vibrationen achten

### 6.5 Wellenlager und Stevenrohr

**Stevenrohrlager-Verschleiß:**

| Symptom | Messung | Bewertung |
|---------|---------|-----------|
| Leichtes Vibrieren bei niedriger Drehzahl | Spiel < 0,3 mm | Beobachten |
| Deutliches Wummern | Spiel 0,3–0,8 mm | Austausch planen |
| Starke Vibrationen, Wassereinbruch | Spiel > 0,8 mm | Sofort handeln |

**Lagertypen und Lebensdauer:**

| Typ | Material | Lebensdauer | Schmierung |
|----|---------|-------------|------------|
| Gummilager (Cutless) | Gummi mit Nuten | 5–10 Jahre | Seewasser |
| Bronzelager | Rotguss | 8–15 Jahre | Fett (Fettpresse) |
| Kunststofflager (Thordon) | Polymer | 10–20 Jahre | Seewasser |
| Keramiklager | Keramik | 15–25 Jahre | Seewasser |

### 6.6 Motor-interne Geräusche

**Geräusch-Diagnose mit Stethoskop:**

Ein Mechaniker-Stethoskop (oder ein langer Schraubendreher als
Notbehelf: Spitze an Motor, Griff ans Ohr) ermöglicht die
Lokalisierung von Geräuschen.

| Geräusch | Ort | Mögliche Ursache |
|----------|-----|------------------|
| Metallisches Klopfen, drehzahlabh. | Zylinderkopf | Ventilspiel zu groß |
| Tiefes Klopfen, drehzahlabh. | Unterer Motorblock | Pleuellagerschaden |
| Dumpfes Hämmern | Unterer Block | Hauptlagerschaden |
| Rasseln/Klappern | Kettenkasten | Steuerkette gelängt |
| Quietschen | Riemenseite | Keilriemen rutscht |
| Pfeifen | Ansaugung/Turbo | Undichtigkeit, Turbo-Lager |
| Zischen | Zylinderkopf | Abgas-Leckage (Kopfdichtung) |
| Ticken (regelmäßig) | Zylinderkopf | Injektor-Leckage |

**Ventilspiel — die häufigste Geräuschquelle:**

Zu großes Ventilspiel erzeugt ein metallisches Ticken/Klappern am
Zylinderkopf, das mit steigender Drehzahl schneller wird.

Soll-Ventilspiel (kalt):

| Motor | Einlass | Auslass |
|-------|---------|---------|
| Yanmar 3JH | 0,20 mm | 0,20 mm |
| Yanmar 4JH | 0,20 mm | 0,20 mm |
| Yanmar 4LHA | 0,15 mm | 0,25 mm |
| Volvo D1/D2 | 0,20 mm | 0,35 mm |
| Volvo D3 | 0,20 mm | 0,40 mm |
| Beta Marine | 0,15 mm | 0,20 mm |
| Nanni N-Serie | 0,20 mm | 0,20 mm |

### 6.7 Resonanz-Phänomene

Bestimmte Drehzahlbereiche können Resonanzen im Antriebsstrang erzeugen,
die starke Vibrationen verursachen, obwohl kein mechanischer Defekt vorliegt.

**Resonanz erkennen:**
- Vibrationen treten nur in einem engen Drehzahlband auf (±100 U/min)
- Oberhalb und unterhalb dieses Bandes läuft alles ruhig
- Vibrationen werden bei genau dieser Drehzahl sehr stark

**Resonanz-Bereiche vermeiden:**
- Drehzahlband markieren und nicht in diesem Bereich fahren
- Wenn der Bereich in der Reise-Drehzahl liegt: Propeller ändern
  (anderer Pitch oder Durchmesser) verschiebt die Resonanz
- Weichere oder härtere Motorlager können helfen
- Flexible Kupplung mit anderer Charakteristik

---
---

## 7. Leistungsverlust

### 7.1 Systematische Diagnose bei Leistungsverlust

Leistungsverlust bedeutet: Der Motor erreicht nicht mehr die frühere
Geschwindigkeit bei gleicher Drehzahl, oder die Drehzahl bei Volllast
ist niedriger als spezifiziert.

**Wichtige Unterscheidung:**

```
LEISTUNGSVERLUST
│
├── Drehzahl erreicht, Geschwindigkeit fehlt
│   → Problem NICHT am Motor
│   → Propeller, Unterwasserschiff, Getriebe
│
├── Drehzahl nicht erreichbar (Motor geht nicht höher)
│   → Motor liefert nicht genug Leistung
│   → Kraftstoff, Luft, Kompression, Abgas
│
└── Drehzahl geht hoch, aber kein Schub
    → Getriebe rutscht (Kupplung verschlissen)
    → Propeller durchdreht (Kavitation)
```

### 7.2 Kraftstoffversorgung

**Kraftstoff-Durchflussrate prüfen:**

1. Kraftstoffleitung vor der Einspritzpumpe lösen
2. In Messgefäß leiten
3. Anlasser 30 Sekunden betätigen (NICHT starten)
4. Menge messen

| Motorleistung | Min. Fördermenge (30 Sek.) |
|---------------|---------------------------|
| 10–20 PS | 50–100 ml |
| 20–40 PS | 100–200 ml |
| 40–80 PS | 200–400 ml |
| 80–150 PS | 400–800 ml |

Wenn zu wenig: Vorfilter, Hauptfilter, Absperrhahn, Tankentnahme,
Förderpumpe prüfen.

**Kraftstoffqualität:**

| Problem | Erkennung | Auswirkung |
|---------|----------|------------|
| Wasser im Diesel | Wasserabscheider voll, Schauglas trüb | Korrosion Injektoren, kein Start |
| Diesel-Bug | Schwarzer Schleim im Filter | Filterverstopfung |
| Alterter Diesel (>12 Monate) | Dunkle Farbe, saurer Geruch | Verminderte Zündwilligkeit |
| Paraffin-Ausflockung | Wachsflocken sichtbar | Filterverstopfung bei Kälte |
| Fehlbetankung (Benzin) | Benzingeruch, Klopfen | Injektoren-/Pumpenschaden |
| Bio-Diesel zu hoch | >B7 am Etikett | Dichtungsquellung, Filterverstopfung |

### 7.3 Luftversorgung und Turbolader

**Luftfilter:**
- Verstopfter Luftfilter reduziert die Luftmenge → weniger Leistung,
  mehr schwarzer Rauch.
- Druckdifferenz messen: Soll < 25 mbar. >50 mbar = Filter wechseln.

**Turbolader:**

Leistungsverlust durch Turbolader-Probleme:

| Problem | Symptom | Prüfung |
|---------|---------|---------|
| Schaufelbruch | Plötzlicher Leistungsverlust, Metallfragmente | Turbo inspizieren |
| Lagerverschleiß | Schleichendes Problem, Öl im Ladeluftschlauch | Radialspiel prüfen |
| Wastegate klemmt offen | Kein Ladedruck bei hoher Drehzahl | Ladedruck messen |
| Ladeluftschlauch gerissen | Zischen hörbar, Leistungsverlust | Sichtprüfung, Drucktest |
| Ladeluftkühler verstopft | Höhere Ladelufttemperatur | Temperaturdifferenz messen |
| Abgasseite verkokt | Schleichender Leistungsverlust | Turbo-Reinigung (Werkstatt) |

**Ladedruck-Referenzwerte:**

| Motor | Ladedruck (Volllast) |
|-------|---------------------|
| Yanmar 4JH-TE | 0,5–0,8 bar |
| Yanmar 4LHA-HTE | 0,8–1,2 bar |
| Volvo D2-75 | 0,6–0,9 bar |
| Volvo D3 | 0,8–1,4 bar |
| Volvo D4/D6 | 1,0–1,8 bar |

### 7.4 Einspritzung

**Injektor-Probleme:**

| Symptom | Ursache | Prüfung |
|---------|---------|---------|
| Unrunder Motorlauf | Ein Injektor defekt | Injektoren einzeln abklemmen |
| Schwarzer Rauch | Injektor tropft | Abdrücktest: muss sprühen, nicht tropfen |
| Klopfen | Öffnungsdruck zu hoch | Abdrücktest mit Manometer |
| Weißer Rauch kalt | Öffnungsdruck zu niedrig | Abdrücktest |
| Leistungsverlust | Spritzbild schlecht | Abdrücktest: feiner Nebel, kein Strahl |

**Injektor-Abdrücktest:**

Benötigt: Abdrückprüfgerät (Injektor-Nozzle-Tester)

1. Injektor in Prüfgerät einspannen
2. Langsam Druck aufbauen
3. Öffnungsdruck ablesen (bei Sprühbeginn)
4. Spritzbild bewerten

| Motor | Soll-Öffnungsdruck |
|-------|--------------------|
| Yanmar 3JH/4JH (mechanisch) | 196–206 bar |
| Yanmar 4LHA (mechanisch) | 220–230 bar |
| Volvo D1/D2 (mechanisch) | 210–225 bar |
| Beta Marine (mechanisch) | 175–195 bar |
| Common-Rail (alle) | 300–1.800 bar (Werkstatt) |

### 7.5 Kompression

Siehe Kapitel 11 für detaillierte Kompressionstests.

Schnellbeurteilung: Wenn der Motor bei allen Zylindern gleichmäßig
Kompression verliert (Verschleiß), äußert sich das als:
- Schwerer Start
- Leistungsverlust unter Last
- Erhöhter Ölverbrauch
- Leichter blauer Rauch

Wenn nur ein Zylinder niedrige Kompression hat:
- Unrunder Motorlauf
- Motor „stampft" im Leerlauf
- Einzelner Zylinder kalt (Auspuffkrümmer mit IR-Thermometer prüfen)

### 7.6 Abgassystem

Rückstau im Abgassystem reduziert die Leistung:

| Ursache | Häufigkeit | Symptom |
|---------|-----------|---------|
| Auspuff-Wassersammler voll | 20 % | Gurgelndes Geräusch, Wasser im Zylinder möglich |
| Auspuffschlauch geknickt | 15 % | Leistungsverlust, Motor qualmt |
| Rußablagerungen im Auspuff | 15 % | Schleichender Leistungsverlust |
| Muffler/Schalldämpfer verstopft | 10 % | Erhöhter Gegendruck, Leistungsverlust |
| Auspuffklappe blockiert | 10 % | Kein Abgasaustritt |
| Wassersammler-Ventil defekt | 5 % | Wasser läuft zurück in Motor |

**Abgas-Gegendruck messen:**

1. Druckanschluss am Abgaskrümmer (falls vorhanden) nutzen
2. Manometer anschließen
3. Druck bei Volllast messen

Maximal zulässiger Gegendruck:
- Saugdiesel: < 40 mbar
- Turbodiesel: < 80 mbar

---
---

## 8. Kraftstoffprobleme

### 8.1 Diesel-Bug (Mikrobiologische Kontamination)

**Was ist Diesel-Bug?**

Diesel-Bug ist ein Sammelbegriff für mikrobiologische Kontamination
im Kraftstoffsystem. Pilze (Hormoconis resinae, Aspergillus fumigatus),
Bakterien und Hefen wachsen an der Grenzschicht zwischen Wasser und
Diesel im Tank.

**Wachstumsbedingungen:**
- Wasser am Tankboden (Kondenswasser reicht)
- Temperatur 10–40 °C (Sommerklima ideal)
- Standzeit > 2 Wochen
- Bio-Diesel-Anteil erhöht Nährstoffangebot

**Erkennungsmerkmale:**

| Stadium | Symptome | Filterzustand |
|---------|---------|---------------|
| Frühstadium | Leichter Leistungsverlust bei Seegang | Filter etwas dunkler |
| Mittleres Stadium | Wiederholtes Filtersetzen | Filter schnell schwarz |
| Fortgeschritten | Motor stirbt unter Last ab | Schwarzer Schleim im Filter |
| Schwer | Motor startet nicht | Tank muss professionell gereinigt werden |

**Behandlung:**

**Stufe 1 — Sofortmaßnahmen:**
1. Alle Filter wechseln (Vorfilter + Hauptfilter)
2. Wasserabscheider entleeren
3. Biozid in den Tank geben (z.B. Grotamar 82: 1:2.000)
4. Motor laufen lassen, damit Biozid zirkuliert
5. Filter nach 10 Stunden nochmals wechseln (Biomasse löst sich)

**Stufe 2 — Tank reinigen:**
1. Tank vollständig leeren
2. Tankinneres mit Hochdruckreiniger reinigen
3. Ablagerungen am Boden und an den Wänden entfernen
4. Tank trocknen lassen
5. Mit frischem, behandeltem Diesel befüllen

**Stufe 3 — System reinigen:**
1. Alle Kraftstoffleitungen durchblasen
2. Vorfilter und Hauptfilter neu
3. Einspritzpumpe (bei starkem Befall) professionell reinigen
4. Injektoren prüfen lassen

**Prävention:**
- Tank möglichst voll halten (weniger Kondensfläche)
- Regelmäßig Wasserabscheider entleeren
- Biozid präventiv 1× jährlich vor Winterlager
- Bei Langfahrt: Kraftstoff durch Polierfilter filtern

### 8.2 Wasser im Kraftstoff

**Quellen für Wasser im Diesel:**

| Quelle | Typische Menge | Erkennung |
|--------|---------------|-----------|
| Kondensation im Tank | 50–500 ml/Saison | Wasserabscheider regelmäßig voll |
| Undichter Tankverschluss | Variabel | Nach Regen mehr Wasser |
| Undichte Tankentlüftung | Variabel | Bei Kränkung/Seegang |
| Verunreinigte Betankung | Variabel | Sofort nach Betankung Probleme |
| Defekter Einfüllstutzen | Variabel | Sichtprüfung |

**Folgen von Wasser im Diesel:**

| Menge | Auswirkung |
|-------|------------|
| Spuren (<0,02 %) | Akzeptabel, normal |
| 0,02–0,05 % | Beschleunigte Korrosion an Injektoren |
| 0,05–0,2 % | Leistungsverlust, unrunder Lauf |
| >0,2 % | Motor kann abstellen, Injektoren-Schäden |
| Freies Wasser | Motor startet nicht, akuter Schaden möglich |

**Sofortmaßnahme bei Wasser im Diesel:**
1. Motor abstellen
2. Wasserabscheider entleeren
3. Wenn Wasserabscheider nicht ausreicht: Wasser am Tankboden absaugen
4. Alle Filter wechseln
5. System entlüften
6. Motor starten und beobachten

### 8.3 Luft im Kraftstoffsystem

Luft im Kraftstoffsystem ist die häufigste Ursache für Startprobleme und
unerwartetes Motorabstellen.

**Luft-Eintrittstellen (Saugseite):**

| Stelle | Häufigkeit | Erkennung |
|--------|-----------|-----------|
| Vorfilter-Gehäuse (O-Ring) | 30 % | Transparenten Schlauch nutzen |
| Kraftstoffilter-Gehäuse | 20 % | Filterwechsel nicht korrekt |
| Tankentnahme-Fitting | 15 % | Tank fast leer |
| Saugleitungs-Verschraubung | 15 % | Sichtprüfung, nachziehen |
| Handpumpen-Membran | 10 % | Membran porös |
| Tank-Absperrhahn | 5 % | Hahn nicht ganz offen, undicht |
| Tank-Boden-Schweißnaht | 5 % | Schwer zu finden, Tank inspizieren |

**Luft-Leckage finden — Methoden:**

**Methode 1: Transparenter Schlauch**
Einen Abschnitt der Saugleitung durch transparenten Schlauch ersetzen.
Blasen sichtbar = Leckage vor diesem Punkt.

**Methode 2: Absperr-Methode**
Saugleitung abschnittsweise absperren (Klemmen setzen) und System
entlüften. Wenn Luft nicht wiederkommt → Leckage hinter der Klemme.

**Methode 3: Überdruck-Methode**
Tank unter leichten Überdruck setzen (Handpumpe, max. 0,3 bar!).
An undichten Stellen tritt Diesel aus statt Luft ein.

### 8.4 Injektor-Probleme

**Injektoren-Fehlerbilder:**

| Fehlerbild | Auswirkung | Ursache |
|-----------|------------|---------|
| Tropfend statt sprühend | Unvollständige Verbrennung, Klopfen | Düsennadel verschlissen |
| Öffnungsdruck zu niedrig | Schlechte Zerstäubung, weißer Rauch | Feder gesetzt |
| Öffnungsdruck zu hoch | Zu wenig Kraftstoff, Leistungsverlust | Düse verkokt |
| Asymmetrisches Spritzbild | Ungleichmäßige Verbrennung | Düsenlöcher teilweise verstopft |
| Nachtropfen | Schwarzer Rauch, Ölverdünnung | Düsennadel nicht dicht |
| Totaler Ausfall | Zylinder arbeitet nicht | Festgefressen, Bruch |

**Diagnosetrick — Injektoren einzeln abklemmen:**

Bei laufendem Motor einen Injektor nach dem anderen abklemmen
(Einspritzleitung lockern, 1 Umdrehung):
- Wenn Motor Drehzahl verliert → dieser Injektor arbeitet
- Wenn Drehzahl sich nicht ändert → dieser Injektor arbeitet NICHT
  (defekt oder kein Kraftstoff)

VORSICHT: Diesel spritzt unter hohem Druck! Tuch darüber legen.
Nie mit bloßer Hand prüfen — Hochdruck-Diesel kann Haut durchdringen!

### 8.5 Einspritzpumpen-Probleme

**Mechanische Reiheneinspritzpumpen (ältere Motoren):**

| Symptom | Mögliche Ursache | Maßnahme |
|---------|-----------------|----------|
| Ungleichmäßiger Leerlauf | Fördermenge ungleich | Pumpe abstimmen (Werkstatt) |
| Leistungsverlust | Plunger verschlissen | Pumpe überholen |
| Motor geht nicht aus (Durchgehen) | Regler defekt | Sofort Luftzufuhr blockieren |
| Diesel im Motoröl | Membrane in Pumpe defekt | Pumpe ersetzen |
| Motor dreht über Nenndrehzahl | Regler defekt | Sofort abstellen |

**Common-Rail-Hochdruckpumpen:**

| Symptom | Mögliche Ursache | Maßnahme |
|---------|-----------------|----------|
| Kein Raildruck | Pumpe defekt, Druckventil | Raildruck auslesen |
| Raildruck schwankt | Volumenstrom-Regelventil | Fehlercodes auslesen |
| Metallabrieb im Kraftstoff | Pumpen-Innenverschleiß | Pumpe + System ersetzen |
| Rücklaufmenge zu hoch | Interne Leckage | Rücklaufmenge messen |

**WARNUNG: Durchgehender Dieselmotor**

Ein durchgehender Motor dreht unkontrolliert über Nenndrehzahl und kann
sich selbst zerstören. Ursachen: Ölnebel im Ansaugtrakt (z.B. bei
defekter Turbo-Dichtung) oder defekter Drehzahlregler.

Sofortmaßnahme:
1. Kraftstoffzufuhr unterbrechen (Stop-Hebel/Solenoid)
2. Wenn Motor nicht stoppt: LUFTZUFUHR BLOCKIEREN!
   - Tuch/Brett vor den Ansaugtrakt pressen
   - CO₂-Feuerlöscher in den Ansaugtrakt sprühen
3. NICHT in die Nähe rotierender Teile kommen
4. Motor kann sich bei Überdrehzahl selbst zerlegen (Pleueldurchschlag)

---
---

## 9. Elektrische Probleme

### 9.1 Startermotor (Anlasser)

**Anlasser-Probleme und Diagnose:**

| Symptom | Ursache | Prüfung |
|---------|---------|---------|
| Klicken, kein Drehen | Magnetschalter zieht, Kontakte verbrannt | Magnetschalter überbrücken |
| Mahlendes Geräusch | Ritzel greift nicht in Schwungrad | Ritzel/Zahnkranz inspizieren |
| Anlasser dreht langsam | Kohlen verschlissen, Kollektor oxidiert | Stromaufnahme messen |
| Anlasser dreht, hört nicht auf | Magnetschalter klebt | Sofort Batterie trennen |
| Anlasser dreht nach Start mit | Freilauf defekt | Anlasser ersetzen |
| Anlasser manchmal, manchmal nicht | Intermittierender Kontakt | Kabel, Klemmen prüfen |

**Anlasser-Stromaufnahme:**

| Motorleistung | Anlasser-Leistung | Stromaufnahme (12V) |
|--------------|------------------|---------------------|
| 10–20 PS | 1,0–1,5 kW | 80–150 A |
| 20–40 PS | 1,5–2,0 kW | 150–250 A |
| 40–80 PS | 2,0–3,0 kW | 250–400 A |
| 80–150 PS | 3,0–5,0 kW | 400–600 A |

Wenn der Anlasser mehr als den Nennstrom zieht → mechanisch schwergängig
oder Kurzschluss in der Wicklung.

**Kabeldimensionierung:**

| Strecke Batterie→Anlasser | Querschnitt 12V | Querschnitt 24V |
|--------------------------|----------------|-----------------|
| < 1 m | 50 mm² | 35 mm² |
| 1–2 m | 70 mm² | 50 mm² |
| 2–3 m | 95 mm² | 70 mm² |
| > 3 m | 120 mm² | 95 mm² |

### 9.2 Lichtmaschine (Generator)

**Lichtmaschinen-Probleme:**

| Symptom | Ursache | Prüfung |
|---------|---------|---------|
| Batterie lädt nicht | Keilriemen rutscht | Spannung, Zustand prüfen |
| Batterie lädt nicht | Kohlen verschlissen | Kohlen prüfen (Länge > 5 mm) |
| Batterie lädt nicht | Regler defekt | Spannung an B+ messen |
| Batterie lädt nicht | Dioden defekt | Diodenplatte prüfen |
| Batterie überladen | Regler defekt (offen) | Ladespannung > 14,8 V |
| Ladekontrolllampe leuchtet nicht | Birne defekt, keine Erregung | Birne wechseln |
| Heulton bei laufendem Motor | Lager verschlissen | Lager ersetzen |
| Lichtmaschine wird sehr heiß | Überlast, Lager, Wicklungsschluss | Reduzierung der Last |

**Ladespannung prüfen:**

| Messung | Soll-Wert (12V) | Soll-Wert (24V) |
|---------|----------------|-----------------|
| Batterie-Ruhespannung | 12,4–12,8 V | 24,8–25,6 V |
| Ladespannung bei 2.000 U/min | 13,8–14,4 V | 27,6–28,8 V |
| Ladespannung bei 3.000 U/min | 14,0–14,5 V | 28,0–29,0 V |
| Max. zulässige Ladespannung | 14,8 V | 29,6 V |

**Keilriemenspannung:**

Die Lichtmaschine wird über einen Keilriemen vom Motor angetrieben.
Falsche Spannung führt zu:
- Zu locker: Riemen rutscht, Lichtmaschine lädt nicht, Quietschen
- Zu stramm: Lager der Lichtmaschine/Wasserpumpe überlastet

Prüfung: Daumen auf die längste freie Riemenstrecke drücken.
- Korrekter Durchhang: 10–15 mm bei ~10 kg Kraft
- Zu locker: > 20 mm → Nachspannen
- Zu stramm: < 5 mm → Entspannen

### 9.3 Glühkerzen und Vorglühsystem

**Glühkerzen-Diagnose:**

| Symptom | Mögliche Ursache | Prüfung |
|---------|-----------------|---------|
| Schwerer Kaltstart | Glühkerze(n) defekt | Stromaufnahme messen |
| Vorglühlampe leuchtet nicht | Sicherung, Relais, Kontrolllampe | Sicherung prüfen |
| Vorglühzeit zu kurz | Steuergerät, Temperatursensor | Vorglühzeit stoppen |
| Motor stirbt nach Vorglüh-Ende | Nachglühfunktion defekt | Steuergerät prüfen |
| Glühkerze lässt sich nicht lösen | Verkokt/korrodiert | NICHT mit Gewalt! Kriechöl, wärmen |

**Glühkerzen-Stromaufnahme pro Kerze:**

| Kerzentyp | Nennstrom (12V) | Nennstrom (24V) |
|-----------|----------------|-----------------|
| Standard (10V) | 6–10 A | — |
| Standard (12V) | 5–8 A | — |
| Schnellglühkerze | 12–20 A | 6–10 A |
| Keramik | 8–15 A | 4–8 A |

Prüfung:
1. Alle Glühkerzenstecker abziehen
2. Amperemeter in Reihe zu EINER Glühkerze schalten
3. Vorglühen aktivieren, Strom ablesen
4. Jede Kerze einzeln messen

Wenn Strom = 0 A → Glühkerze defekt (Unterbrechung)
Wenn Strom zu hoch → Glühkerze hat Kurzschluss (Sicherung kann durchbrennen)

### 9.4 Verkabelung und Steckverbinder

**Marine-Elektrik-Probleme:**

Die salzhaltige, feuchte Umgebung ist der größte Feind der Bordelektrik.

| Problem | Ort | Symptom |
|---------|-----|---------|
| Grünspan an Steckern | Motor-Steckverbinder | Intermittierende Ausfälle |
| Korrodierte Crimpverbindung | Kabelschuhe | Spannungsabfall, Erwärmung |
| Gebrochene Litze | Vibrationsbeanspruchte Kabel | Zeitweiser Ausfall |
| Kurzschluss durch Scheuerung | Kabel an Motorblock | Sicherung brennt durch |
| Masseproblem | Motorblock-Massepunkt | Unzuverlässige Anzeigen |

**Systematische Kabelprüfung:**

1. Sichtprüfung: Alle sichtbaren Kabel und Stecker auf Korrosion,
   Scheuerung, Brüche prüfen
2. Spannungsabfall-Methode: Bei eingeschaltetem Verbraucher die Spannung
   am Anfang und Ende der Leitung messen. Differenz sollte < 0,5 V sein.
3. Masseleitung: Spannungsabfall zwischen Motorblock-Masse und
   Batterie-Minus bei laufendem Motor < 0,3 V
4. Steckverbinder: Alle Stecker abziehen, reinigen (Kontaktspray),
   wieder aufstecken

### 9.5 Sensoren und Geber

Moderne Marine-Dieselmotoren haben zahlreiche Sensoren:

| Sensor | Funktion | Fehlerauswirkung |
|--------|---------|------------------|
| Temperatur-Sensor (Kühlmittel) | Temperaturanzeige, Alarm | Falsche Anzeige, kein Alarm |
| Öldruck-Sensor | Öldruckanzeige, Alarm | Falsche Anzeige, Fehlalarm |
| Drehzahl-Sensor | Drehzahlanzeige, Steuerung | Kein Start (Common-Rail), falsche Anzeige |
| Kraftstoffdruck-Sensor | Rail-Druckregelung (CR) | Leistungsverlust, Notlauf |
| Ladelufttemperatur | Einspritzmenge (CR) | Leistungsreduktion |
| Nockenwellen-Sensor | Einspritz-Timing (CR) | Kein Start |
| Lambda-Sonde (Abgas) | Emissionskontrolle | Erhöhte Emissionen |
| Wassertemperatur-Sensor (See) | Information | Falsche Anzeige |

**Sensor-Prüfung allgemein:**

1. Stecker abziehen, Pins auf Korrosion prüfen
2. Widerstand des Sensors messen (vergleiche mit Soll-Wert)
3. Bei Temperatur-Sensoren: NTC-Kennlinie prüfen
   (Widerstand sinkt mit steigender Temperatur)

| Temperatur | Typischer NTC-Widerstand |
|-----------|-------------------------|
| 20 °C | 2.000–3.000 Ω |
| 40 °C | 800–1.200 Ω |
| 60 °C | 300–500 Ω |
| 80 °C | 150–250 Ω |
| 100 °C | 80–130 Ω |

### 9.6 CAN-Bus-Fehler

**Was ist CAN-Bus im Marine-Motor?**

Moderne Motoren (Volvo D3+, Yanmar Common-Rail, Nanni T-Serie) verwenden
ein CAN-Bus-Netzwerk zur Kommunikation zwischen Motorsteuergerät (ECU),
Getriebe-Steuerung, Instrumentierung und Gashebelsteuerung.

**CAN-Bus-Probleme:**

| Symptom | Ursache | Prüfung |
|---------|---------|---------|
| Alle Instrumente tot | CAN-Bus-Kabel unterbrochen | Widerstand 60 Ω am Bus messen |
| Einzelnes Instrument fällt aus | Knoten-Problem | Einzelnen Knoten prüfen |
| Sporadische Ausfälle | Wackelkontakt, EMV | Stecker reinigen, Kabelführung |
| Motor geht in Notlauf | ECU-Fehler | Fehlercodes auslesen |
| EVC-Gashebel reagiert nicht | EVC-Knoten | EVC-Diagnose mit VODIA |

**CAN-Bus-Grundlagen für Diagnose:**

```
CAN-Bus physische Prüfung:
├── Abschlusswiderstand: 120 Ω an jedem Ende (gesamt 60 Ω)
├── CAN-H zu CAN-L: 60 Ω (bei intaktem Bus)
├── CAN-H zu Masse: > 1 kΩ (kein Kurzschluss)
├── CAN-L zu Masse: > 1 kΩ (kein Kurzschluss)
└── Spannung CAN-H/CAN-L: 2,0–3,5 V Differenz bei aktivem Bus
```

---
---

## 10. Ölverlust und Leckagen

### 10.1 Systematische Leckage-Diagnose

**Schritt 1: Leckage-Typ identifizieren**

| Medium | Farbe | Geruch | Konsistenz |
|--------|-------|--------|------------|
| Motoröl | Braun bis schwarz | Ölig, leicht verbrannt | Zähflüssig |
| Getriebeöl | Hellbraun bis rot | Ölig | Zähflüssig |
| Diesel | Klar bis gelblich | Diesel-typisch | Dünnflüssig |
| Kühlmittel | Grün, blau oder rosa | Süßlich, chemisch | Dünnflüssig |
| Seewasser | Klar (salzig) | Salzig | Dünnflüssig |

**Schritt 2: Leckage lokalisieren**

Methode: Motor reinigen (Bremsenreiniger oder Motorwäsche), trocknen,
Motor laufen lassen, beobachten wo die Leckage zuerst auftritt.

Hilfsmittel:
- UV-Additiv im Öl + UV-Lampe (sehr effektiv)
- Talkumpuder auf verdächtige Stellen (zeigt Öl als dunkle Spur)
- Spiegel + Taschenlampe für schlecht zugängliche Stellen

### 10.2 Typische Öl-Leckage-Stellen

| Stelle | Häufigkeit | Schwere | Reparatur |
|--------|-----------|---------|-----------|
| Ventildeckeldichtung | 25 % | Leicht | Dichtung wechseln |
| Ölwannendichtung | 20 % | Mittel | Dichtung wechseln (Ausbau nötig) |
| Kurbelwellendichtring vorn | 15 % | Schwer | Dichtring wechseln |
| Kurbelwellendichtring hinten | 10 % | Schwer | Motor/Getriebe trennen |
| Ölfiltergehäuse | 10 % | Leicht | O-Ring wechseln, nachziehen |
| Ölkühler-Verbindungen | 8 % | Mittel | Dichtungen wechseln |
| Öldruckschalter | 5 % | Leicht | Dichtring oder Schalter wechseln |
| Turbo-Ölversorgung | 4 % | Mittel | Leitungsdichtungen wechseln |
| Zylinderkopf-Riss | 2 % | Sehr schwer | Kopf ersetzen |
| Motorblock-Riss | 1 % | Totalschaden | Motor ersetzen |

### 10.3 Ölverbrauch ohne sichtbare Leckage

Wenn der Ölstand sinkt, aber keine Leckage sichtbar ist:

| Ursache | Diagnose | Maßnahme |
|---------|----------|----------|
| Verbrennung (Kolbenringe) | Blauer Rauch, Kompressionstest | Motorrevision |
| Verbrennung (Ventilschaftdicht.) | Blauer Rauch beim Start | Dichtungen wechseln |
| Verbrennung (Turbo-Dichtung) | Öl im Ladeluftschlauch | Turbo überholen |
| Kurbelgehäuseentlüftung | Öl in Ansaugtrakt | Entlüftung reinigen/ersetzen |
| Undichte Kopfdichtung (→ Kühlmittel) | Kühlmittel wird mehr, Öl weniger | Kopfdichtung wechseln |

### 10.4 Kühlmittel-Leckagen

**Externe Leckagen (sichtbar):**

| Stelle | Häufigkeit | Prüfung |
|--------|-----------|---------|
| Schlauchverbindungen | 30 % | Sichtprüfung, Schlauchklemmen nachziehen |
| Wasserpumpen-Dichtung | 20 % | Tropfen unter der Pumpe |
| Wärmetauscher-Endkappen | 15 % | O-Ringe prüfen |
| Thermostatgehäuse | 10 % | Dichtung prüfen |
| Ausgleichsbehälter | 10 % | Riss im Kunststoff |
| Frostschutzstöpsel | 5 % | Selten, aber möglich |
| Zylinderkopf | 5 % | Riss (nur Werkstatt) |
| Motorblock | 5 % | Frostschaden (Riss) |

**Interne Leckagen (unsichtbar):**

| Leckage-Pfad | Symptom | Diagnose |
|-------------|---------|----------|
| Kühlmittel → Zylinder | Weißer Rauch, Kühlmittel sinkt | CO₂-Test, Drucktest |
| Kühlmittel → Ölraum | Milchiges Öl | Ölpeilstab prüfen |
| Kühlmittel → Wärmetauscher (Seewasser) | Kühlmittel sinkt ohne Rauch | Frostschutz im Seewasser |
| Öl → Kühlmittel | Ölfilm auf Kühlmittel | Ausgleichsbehälter prüfen |

### 10.5 Diesel-Leckagen

Diesel-Leckagen sind besonders gefährlich (Brandgefahr) und umweltschädlich.

| Stelle | Häufigkeit | Sofortmaßnahme |
|--------|-----------|----------------|
| Einspritzleitungen | 25 % | Motor aus, Verschraubungen nachziehen |
| Kraftstofffilter-Gehäuse | 20 % | O-Ring prüfen, Filter korrekt montiert? |
| Injektor-Kupferdichtung | 15 % | Dichtung erneuern (neue Kupferscheibe) |
| Kraftstoffschläuche (alt) | 15 % | Schläuche erneuern |
| Einspritzpumpen-Anschlüsse | 10 % | Verschraubungen prüfen |
| Tank-Fitting | 10 % | Fitting nachziehen/ersetzen |
| Tankriss/Schweißnaht | 5 % | Tank reparieren (Fachbetrieb) |

**BRANDGEFAHR:** Diesel auf heißem Auspuffkrümmer (>250 °C) kann sich
entzünden. Jede Diesel-Leckage im Motorraum sofort beheben!

---
---

## 11. Kompressionstest — Durchführung und Interpretation

### 11.1 Warum Kompressionstest?

Der Kompressionstest ist die wichtigste Einzelmessung zur Beurteilung
des mechanischen Zustands eines Dieselmotors. Er prüft die Dichtheit
von Kolbenringen, Ventilen und Zylinderkopfdichtung.

### 11.2 Trocken-Kompressionstest (Standard)

**Voraussetzungen:**
- Motor auf Betriebstemperatur (80 °C)
- Batterie voll geladen
- Alle Glühkerzen (oder Injektoren) ausgebaut
- Dekompression deaktiviert (falls vorhanden)
- Kraftstoffzufuhr unterbrochen (Stop-Solenoid aktivieren)

**Durchführung:**
1. Kompressionstest-Adapter in Glühkerzen- oder Injektorbohrung schrauben
2. Kompressionsmanometer anschließen
3. Gashebel auf Vollgas
4. Anlasser betätigen (ca. 10 Umdrehungen, ~5–8 Sekunden)
5. Maximaldruck ablesen
6. Manometer ablassen
7. An jedem Zylinder wiederholen

**Kompressionsdruckwerte (Soll):**

| Motor | Kompressions-Soll | Minimum |
|-------|-------------------|---------|
| Yanmar 1GM10 | 28–32 bar | 22 bar |
| Yanmar 2YM15 | 28–32 bar | 22 bar |
| Yanmar 3JH | 28–32 bar | 22 bar |
| Yanmar 4JH | 28–32 bar | 22 bar |
| Yanmar 4LHA | 30–35 bar | 25 bar |
| Volvo D1-13/D1-20 | 25–30 bar | 20 bar |
| Volvo D1-30/D2-40 | 28–33 bar | 22 bar |
| Volvo D2-55/D2-75 | 30–35 bar | 24 bar |
| Volvo D3 | 30–38 bar | 25 bar |
| Beta 14–25 | 26–30 bar | 20 bar |
| Beta 30–50 | 28–33 bar | 22 bar |
| Nanni N2/N3 | 27–32 bar | 21 bar |
| Nanni N4 | 28–34 bar | 22 bar |

**WICHTIG:** Die absolute Höhe des Drucks allein ist weniger aussagekräftig
als die GLEICHMÄSSIGKEIT zwischen den Zylindern.

### 11.3 Interpretation der Ergebnisse

| Ergebnis | Bewertung | Maßnahme |
|----------|----------|----------|
| Alle Zylinder im Sollbereich | Motor mechanisch in Ordnung | Keine |
| Alle Zylinder gleichmäßig, aber unter Soll | Gleichmäßiger Verschleiß | Revision planen |
| Ein Zylinder deutlich niedriger | Lokales Problem | Differenzdiagnose nötig |
| Zwei benachbarte Zylinder niedrig | Kopfdichtung zwischen den Zylindern | Kopfdichtung wechseln |
| Maximal zulässige Differenz | < 10 % zwischen Zylindern | — |

**Maximal zulässige Differenz:**

Berechnung: (Höchster Wert – niedrigster Wert) / Höchster Wert × 100

| Differenz | Bewertung |
|-----------|----------|
| < 5 % | Ausgezeichnet |
| 5–10 % | Gut |
| 10–15 % | Akzeptabel, beobachten |
| 15–20 % | Grenzwertig |
| > 20 % | Revision nötig |

### 11.4 Nass-Kompressionstest (Wet Test)

Wenn ein Zylinder niedrige Kompression zeigt, wird der Nass-Test
durchgeführt, um zwischen Kolbenringen und Ventilen zu unterscheiden:

**Durchführung:**
1. Ca. 10 ml Motoröl in den betroffenen Zylinder geben
   (durch Glühkerzen-/Injektorbohrung)
2. Kompressionstest wiederholen

**Interpretation:**

| Trockentest | Nasstest | Diagnose |
|------------|---------|----------|
| Niedrig | Deutlich höher (+10–15 bar) | Kolbenringe verschlissen |
| Niedrig | Unverändert | Ventile undicht oder Kopfdichtung |
| Niedrig | Leicht höher (+3–5 bar) | Kombination: Ringe + Ventile |

### 11.5 Leckage-Rate-Test (Cylinder Leak-Down Test)

Genauer als der Kompressionstest, aber aufwändiger:

**Durchführung:**
1. Kolben auf OT (oberer Totpunkt) im Verdichtungstakt stellen
2. Druckluft (6–8 bar) durch Adapter in den Zylinder einleiten
3. Leckage-Rate mit kalibriertem Manometer ablesen
4. Zuordnung der Leckage nach Austrittsort

**Interpretation:**

| Leckage-Rate | Bewertung |
|-------------|----------|
| < 5 % | Ausgezeichnet |
| 5–10 % | Gut |
| 10–20 % | Akzeptabel |
| 20–30 % | Verschleiß erkennbar |
| > 30 % | Reparatur erforderlich |

**Wo tritt die Leckage aus?**

| Austrittsort | Defekt |
|-------------|--------|
| Ansaugtrakt (Luftfilter) | Einlassventil undicht |
| Auspuff | Auslassventil undicht |
| Ölfilter-Einfüllstutzen | Kolbenringe defekt |
| Kühlmittel-Ausgleichsbehälter | Kopfdichtung defekt |
| Benachbarte Glühkerzenöffnung | Kopfdichtung zwischen Zylindern |

---
---

## 12. Ölanalyse — Probennahme und Interpretation

### 12.1 Warum Ölanalyse?

Die Ölanalyse ist die einzige Methode, den internen Zustand eines Motors
zu beurteilen, ohne ihn zu öffnen. Abriebmetalle, Verunreinigungen und
Additiv-Zustand geben Aufschluss über Verschleißmuster.

### 12.2 Probennahme — Korrekte Durchführung

**Wann die Probe nehmen:**
- Motor warmgefahren (mind. 20 Minuten unter Last)
- VOR dem Ölwechsel (altes Öl enthält die Informationen)
- Immer zur gleichen Zeit im Wechselintervall (Vergleichbarkeit)

**Wie die Probe nehmen:**
1. Probeflasche aus dem Analyse-Kit verwenden (sauber, versiegelt)
2. Öl aus der Mitte des Ölvolumens entnehmen (nicht vom Boden,
   nicht von oben)
3. Am besten über den Peilstab-Kanal mit Absaugpumpe
4. Mindestens 100 ml entnehmen
5. Flasche sofort verschließen und beschriften
6. An das Labor senden (z.B. Oelcheck, Polaris, WearCheck)

### 12.3 Verschleißmetalle — Was sie bedeuten

**Eisen (Fe) — Verschleiß an:**

| Fe-Wert (ppm) | Bewertung | Quelle |
|---------------|----------|--------|
| < 30 | Normal | Normaler Abrieb |
| 30–60 | Erhöht | Zylinderlaufbuchse, Nockenwelle |
| 60–100 | Hoch | Beschleunigter Verschleiß |
| > 100 | Kritisch | Sofort Motor prüfen |

**Kupfer (Cu) — Verschleiß an:**

| Cu-Wert (ppm) | Bewertung | Quelle |
|---------------|----------|--------|
| < 15 | Normal | Normaler Abrieb |
| 15–30 | Erhöht | Pleuellager (Zweischicht), Ölkühler |
| 30–60 | Hoch | Lagerverschleiß, Ölkühler korrodiert |
| > 60 | Kritisch | Lagerschaden droht |

**Blei (Pb) — Verschleiß an:**

| Pb-Wert (ppm) | Bewertung | Quelle |
|---------------|----------|--------|
| < 10 | Normal | Normaler Abrieb |
| 10–25 | Erhöht | Hauptlager, Pleuellager |
| 25–50 | Hoch | Lagerverschleiß fortgeschritten |
| > 50 | Kritisch | Lagerschaden imminent |

**Zinn (Sn) — Verschleiß an:**

| Sn-Wert (ppm) | Bewertung | Quelle |
|---------------|----------|--------|
| < 5 | Normal | — |
| 5–15 | Erhöht | Pleuellager-Overlay |
| > 15 | Kritisch | Schwerer Lagerverschleiß |

**Aluminium (Al) — Verschleiß an:**

| Al-Wert (ppm) | Bewertung | Quelle |
|---------------|----------|--------|
| < 15 | Normal | Kolben, Pumpengehäuse |
| 15–30 | Erhöht | Kolbenverschleiß |
| > 30 | Kritisch | Kolbenschaden, Turbinenlaufrad |

**Chrom (Cr) — Verschleiß an:**

| Cr-Wert (ppm) | Bewertung | Quelle |
|---------------|----------|--------|
| < 5 | Normal | Kolbenringe (verchromt) |
| 5–15 | Erhöht | Ringverschleiß |
| > 15 | Kritisch | Schwerer Ringverschleiß |

**Silizium (Si) — Verschmutzung:**

| Si-Wert (ppm) | Bewertung | Quelle |
|---------------|----------|--------|
| < 15 | Normal | Dichtmassen, Additive |
| 15–30 | Erhöht | Staubansaugung, Filterdefekt |
| > 30 | Kritisch | Luftfilter undicht, Dichtung defekt |

### 12.4 Kontaminanten im Öl

| Parameter | Normal | Grenzwert | Bedeutung |
|-----------|--------|-----------|-----------|
| Wasser | < 0,1 % | > 0,2 % | Kopfdichtung, Kondenswasser |
| Kraftstoff | < 1 % | > 2 % | Injektordichtung, Pumpe |
| Ruß | < 1 % (Diesel) | > 3 % | Schlechte Verbrennung |
| Glykol | Nicht nachweisbar | Jede Menge | Kopfdichtung! |
| Säurezahl (TAN) | < 2,0 mg KOH/g | > 4,0 | Öl überaltert |
| Basenzahl (TBN) | > 5,0 mg KOH/g | < 2,0 | Öl aufgebraucht |
| Viskosität (100°C) | ±10 % vom Frischöl | > ±20 % | Verdünnung oder Oxidation |

### 12.5 Ölanalyse-Intervalle

| Einsatzart | Analyse-Intervall |
|-----------|-------------------|
| Fahrtenyacht (200–500 h/Jahr) | Jährlich vor Ölwechsel |
| Charterboot (800–1.500 h/Jahr) | Alle 500 Stunden |
| Motorboot (hohe Auslastung) | Alle 250 Stunden |
| Nach Verdacht auf Schaden | Sofort |
| Nach Reparatur/Überholung | Nach 50 Stunden Einlauf |

### 12.6 Ölanalyse richtig interpretieren

**Trend ist wichtiger als Einzelwert:**

Ein einzelner Wert sagt wenig aus. Erst die Trendanalyse über mehrere
Proben zeigt, ob der Verschleiß normal voranschreitet oder sich
beschleunigt.

**Beispiel-Trend:**

| Probe | Stunden | Fe (ppm) | Cu (ppm) | Bewertung |
|-------|---------|---------|---------|-----------|
| 1 | 500 | 15 | 8 | Normal |
| 2 | 1.000 | 22 | 12 | Normal |
| 3 | 1.500 | 35 | 18 | Leicht erhöht |
| 4 | 2.000 | 85 | 42 | Stark erhöht → Ursache suchen |

In diesem Beispiel zeigt der sprunghafte Anstieg bei Probe 4, dass
etwas passiert ist (z.B. Lagerverschleiß, Ölmangel, Überhitzung).

---
---

## 13. Common-Rail Fehlercodes und Diagnosegeräte

### 13.1 Common-Rail-Grundlagen

Common-Rail-Einspritzung arbeitet mit extrem hohen Drücken (bis 2.000 bar)
und wird elektronisch gesteuert. Die ECU (Engine Control Unit) überwacht
zahlreiche Sensoren und kann detaillierte Fehlercodes (DTCs — Diagnostic
Trouble Codes) erzeugen.

### 13.2 Diagnosegeräte

| Hersteller | Diagnose-Tool | Kosten | Funktionsumfang |
|-----------|--------------|--------|-----------------|
| Yanmar | Yanmar Diagnostic System (YDS) | ~2.500 EUR | Volldiagnose, Programmierung |
| Volvo Penta | VODIA5 | ~3.000 EUR | Volldiagnose, EVC-Konfiguration |
| Universal | Texa Navigator | ~4.000 EUR | Multi-Marken Marine |
| Universal | Jaltest Marine | ~3.500 EUR | Multi-Marken Marine |
| OBD-Adapter | Generic CAN-Reader | 50–200 EUR | Nur Fehlercodes lesen |

### 13.3 Yanmar Common-Rail Fehlercodes

**Motorsteuerung (ECU):**

| DTC | Beschreibung | Schwere | Sofortmaßnahme |
|-----|-------------|---------|----------------|
| P0087 | Raildruck zu niedrig | Kritisch | Last reduzieren, Kraftstofffilter prüfen |
| P0088 | Raildruck zu hoch | Kritisch | Motor abstellen, Druckregelventil prüfen |
| P0091 | Druckregelventil — Stromkreis offen | Kritisch | Kabelverbindung prüfen |
| P0093 | Kraftstoffsystem-Leckage erkannt | Kritisch | Motor abstellen, Leitungen prüfen |
| P0100 | Luftmassenmesser — Fehlfunktion | Mittel | Reinigen oder ersetzen |
| P0107 | Ladedrucksensor — Spannung zu niedrig | Mittel | Sensor/Verkabelung prüfen |
| P0108 | Ladedrucksensor — Spannung zu hoch | Mittel | Sensor/Verkabelung prüfen |
| P0115 | Kühlmittel-Temp.sensor — Fehlfunktion | Mittel | Sensor prüfen |
| P0117 | Kühlmittel-Temp.sensor — Spannung niedrig | Leicht | Sensor/Kabel prüfen |
| P0118 | Kühlmittel-Temp.sensor — Spannung hoch | Leicht | Sensor/Kabel prüfen |
| P0180 | Kraftstoff-Temp.sensor — Fehlfunktion | Mittel | Sensor prüfen |
| P0190 | Raildruck-Sensor — Fehlfunktion | Kritisch | Sensor prüfen |
| P0192 | Raildruck-Sensor — Spannung niedrig | Kritisch | Sensor/Kabel prüfen |
| P0193 | Raildruck-Sensor — Spannung hoch | Kritisch | Sensor/Kabel prüfen |
| P0201 | Injektor Zyl. 1 — Stromkreis | Kritisch | Stecker/Kabel Injektor 1 |
| P0202 | Injektor Zyl. 2 — Stromkreis | Kritisch | Stecker/Kabel Injektor 2 |
| P0203 | Injektor Zyl. 3 — Stromkreis | Kritisch | Stecker/Kabel Injektor 3 |
| P0204 | Injektor Zyl. 4 — Stromkreis | Kritisch | Stecker/Kabel Injektor 4 |
| P0217 | Motorkühlmittel — Übertemperatur | Kritisch | Motor abstellen, Kühlsystem |
| P0219 | Überdrehzahl | Kritisch | Motor abstellen |
| P0234 | Turbo-Überdruck | Mittel | Wastegate prüfen |
| P0335 | Kurbelwellensensor — kein Signal | Kritisch | Sensor/Kabel prüfen |
| P0340 | Nockenwellensensor — kein Signal | Kritisch | Sensor/Kabel prüfen |
| P0380 | Glühkerzen-Stromkreis | Leicht | Relais/Sicherung prüfen |
| P0401 | AGR-Durchfluss zu gering | Mittel | AGR-Ventil reinigen |
| P0470 | Abgasdruck-Sensor — Fehlfunktion | Mittel | Sensor prüfen |
| P0524 | Öldruck zu niedrig | Kritisch | Sofort Motor abstellen! |
| P0563 | Systemspannung zu hoch | Mittel | Lichtmaschine/Regler prüfen |
| P0627 | Kraftstoffpumpen-Steuerung | Kritisch | Relais/Verkabelung |
| P1093 | Raildruck-Abweichung | Kritisch | Hochdruckpumpe, Druckregelventil |
| P1211 | Raildruck beim Start zu niedrig | Kritisch | Niederdruck-System prüfen |
| P2146 | Injektor Gruppe A — Spannung | Kritisch | Injektor-Verkabelung |
| P2149 | Injektor Gruppe B — Spannung | Kritisch | Injektor-Verkabelung |

### 13.4 Volvo Penta EVC Fehlercodes

**Electronic Vessel Control (EVC) System:**

| DTC | Beschreibung | Auswirkung |
|-----|-------------|------------|
| MID 128-1 | ECU — interner Fehler | Notlauf |
| MID 128-21 | Kühlmitteltemperatur-Sensor | Anzeige ungenau |
| MID 128-22 | Ladelufttemperatur-Sensor | Leistungsreduktion |
| MID 128-27 | Kühlmittelstand niedrig | Warnung |
| MID 128-91 | Gashebelposition-Sensor | Eingeschränkte Steuerung |
| MID 128-94 | Kraftstoffdruck | Leistungsreduktion |
| MID 128-100 | Öldruck niedrig | Notabschaltung |
| MID 128-105 | Ladelufttemperatur hoch | Leistungsreduktion |
| MID 128-110 | Kühlmitteltemperatur hoch | Leistungsreduktion → Abschaltung |
| MID 128-157 | Raildruck | Notlauf |
| MID 128-158 | Batterieladung niedrig | Warnung |
| MID 128-164 | Einspritzmenge — Abweichung | Leistungsreduktion |
| MID 128-168 | Batteriespannung | Lichtmaschine prüfen |
| MID 128-171 | Ansauglufttemperatur | Leistungsreduktion |
| MID 128-172 | Ansaugluftdruck | Leistungsreduktion |
| MID 128-175 | Motoröltemperatur hoch | Leistungsreduktion |
| MID 128-190 | Überdrehzahl | Kraftstoff-Absperrung |
| MID 128-412 | AGR-Ventil | Emissionswarnung |
| MID 128-639 | CAN-Bus-Fehler | Kommunikation gestört |
| MID 140-1 | EVC-A — interner Fehler | Eingeschränkte Steuerung |
| MID 140-39 | EVC-A — Gashebel-Sensor A | Notlauf |
| MID 140-40 | EVC-A — Gashebel-Sensor B | Notlauf |
| MID 140-70 | EVC-A — Getriebe-Kommunikation | Gangwechsel-Problem |
| MID 164-1 | Getriebe — interner Fehler | Limp-Home-Modus |
| MID 164-167 | Getriebe — Öltemperatur hoch | Leistungsreduktion |
| MID 164-168 | Getriebe — Systemspannung | Ladezustand prüfen |

### 13.5 Notlauf-Modus (Limp Home)

Wenn die ECU bestimmte kritische Fehler erkennt, schaltet sie in den
Notlauf-Modus:

| Einschränkung | Typische DTC-Auslöser |
|--------------|----------------------|
| Max. 1.500 U/min | P0087, P0093, P0190, P1093 |
| Max. 2.000 U/min | P0107, P0180, P0234 |
| Keine Einschränkung, nur Warnung | P0115, P0117, P0380 |
| Motor startet nicht | P0335, P0340, P0627 |
| Motor schaltet ab | P0524 (Öldruck), P0219 (Überdrehzahl) |

**Notlauf-Modus zurücksetzen:**
1. Motor abstellen
2. 30 Sekunden warten
3. Fehlercode mit Diagnosegerät auslesen
4. Ursache beheben
5. Fehlercode löschen
6. Motor starten — wenn Ursache behoben, läuft Motor normal

**WARNUNG:** Fehlercodes NUR löschen, wenn die Ursache behoben ist.
Sonst wird der Fehler sofort wieder gesetzt.

### 13.6 Eigene Diagnose ohne Spezialgerät

Auch ohne teures Diagnosegerät können Basis-Informationen ausgelesen
werden:

**Yanmar — Blinkcode:**
Einige Yanmar-Motoren zeigen Fehlercodes durch Blinken der Warnlampe
am Instrumentenpanel:
- Zündung EIN, Diagnose-Modus aktivieren (je nach Modell)
- Warnlampe blinkt in Gruppen
- Lange Pause = Trennzeichen zwischen Codes
- Beispiel: 3 Blinker — Pause — 5 Blinker = Code 35

**Volvo Penta — Display-Fehlercodes:**
Neuere Volvo-Installationen mit EVC-Display zeigen Fehlercodes direkt
im Klartext an. Ältere Installationen:
- Diagnosetaste am EVC-Panel drücken
- Code wird als Zahl angezeigt

---
---

## 14. Notfall-Maßnahmen auf See

### 14.1 Prioritäten bei Motorausfall

```
MOTORAUSFALL AUF SEE — PRIORITÄTEN
│
├── 1. SICHERHEIT
│   ├── Ruhe bewahren
│   ├── Besatzung informieren
│   ├── Position feststellen (GPS)
│   ├── Segel setzen (Segelboot) / Anker bereit (Küste nah)
│   └── Andere Schiffe beobachten (Kollisionsgefahr)
│
├── 2. KOMMUNIKATION
│   ├── Bei Gefahr: Mayday (Kanal 16 VHF)
│   ├── Bei Dringlichkeit: Pan-Pan (Kanal 16 VHF)
│   ├── Bei Sicherheit gegeben: Nachricht an Marina/Schlepp
│   └── AIS einschalten (NUC-Status wenn möglich)
│
├── 3. DIAGNOSE
│   ├── Was ist passiert? (Symptom vor dem Ausfall)
│   ├── Schnell-Check: Öl, Kühlmittel, Kraftstoff, Batterie
│   ├── Systematische Fehlersuche (→ Kapitel 1–9)
│   └── Reparatur wenn möglich
│
└── 4. OPTIONEN
    ├── Eigenreparatur möglich → reparieren
    ├── Segeln möglich → zur nächsten Marina segeln
    ├── Ankern möglich → Anker und dann reparieren
    └── Schlepp anfordern (kommerziell oder KNRM/DGzRS/SNSM)
```

### 14.2 Notfall-Reparaturen

**Motor überhitzt — Sofortmaßnahme:**
1. Motor auf Leerlauf
2. Kühlwasseraustritt Auspuff prüfen
3. Wenn kein Wasser: Seeventil prüfen → Sieb reinigen → Impeller prüfen
4. Wenn Impeller kaputt und kein Ersatz:
   - Motor max. 30 Sekunden laufen lassen, 5 Minuten abkühlen, wiederholen
   - Nur im absoluten Notfall (Temperatur manuell überwachen!)
   - Alternative: Eimer-Kühlung (Seewasser mit Eimer durch den
     Motor gießen — nur bei Einkreis/Direktkühlungsmotoren)

**Kein Kraftstoff — Sofortmaßnahme:**
1. Ersatzkanister vorhanden? Direkt in Vorfilter füllen
2. System entlüften (→ Kapitel 2.4)
3. Startversuche (max. 30 Sekunden, Pausen einhalten)
4. Wenn Tank leer: Reservekanister nutzen (IMMER mind. 20 l an Bord!)

**Batterie leer — Sofortmaßnahme:**
1. Zweite Batterie (Verbraucherbatterie) umschalten
2. Wenn beide leer: Starthilfe von anderem Boot (Schlauchboot/Beiboot)
3. Generator oder tragbare Powerstation zum Laden nutzen
4. Handstart (nur bei kleinen Motoren mit Dekompression)

**Undichtigkeit — Sofortmaßnahme:**
1. Kraftstoff-Leck: Lappen um die Stelle wickeln, Schlauchklemme
2. Kühlmittel-Leck (Schlauch): Reparaturband (selbstverschweißend),
   Schlauchschelle, Kabelbinder als Notbehelf
3. Öl-Leck: Wenn gering — Öl nachfüllen und weiterfahren
4. Seewasser-Schlauch: Sofort Seeventil schließen! Dann reparieren.

### 14.3 Notfall-Ausrüstung Motorbereich

**Absolute Mindestausstattung an Bord:**

| Teil | Menge | Einsatz |
|------|-------|---------|
| Impeller (passend) | 2 | Kühlsystem-Notfall |
| Keilriemen (passend) | 1 | Lichtmaschine/Wasserpumpe |
| Kraftstofffilter (Vor + Haupt) | 2 Sets | Diesel-Bug, Wasser |
| Ölfilter | 1 | Ölwechsel/Notfall |
| Motoröl (1 l Flasche) | 2 | Nachfüllen |
| Kühlmittel (1 l Flasche) | 1 | Nachfüllen |
| Diesel-Kanister (20 l) | 1 | Reservekraftstoff |
| Dichtungsset (O-Ringe Sortiment) | 1 | Diverse Dichtungen |
| Schlauchklemmen-Sortiment | 1 | Schlauch-Reparatur |
| Selbstverschweißendes Band | 2 Rollen | Notdichtung |
| Zweikomponenten-Epoxy | 1 Tube | Notdichtung |
| Kabelbinder groß | 20 | Universal-Befestigung |
| Isolierband | 2 Rollen | Elektrik |
| Lüsterklemmen | 10 | Kabelverbindung |
| Sicherungssortiment | 1 | Elektrik |
| Multimeter | 1 | Elektrik-Diagnose |
| Kompressionstest-Set | 1 | Diagnose |

### 14.4 Schlepphilfe und Bergung

**Kosten-Orientierung für Schlepp-Dienste:**

| Situation | Kosten (ca.) | Dauer |
|----------|-------------|-------|
| Abschlepp in Marina (< 5 NM) | 300–800 EUR | 1–3 h |
| Abschlepp in Marina (5–20 NM) | 800–2.500 EUR | 3–8 h |
| Offshore-Bergung (> 20 NM) | 2.500–10.000 EUR | 6–24 h |
| Bergung bei Havarie | 5.000–50.000+ EUR | Variabel |
| ADAC-Küstenschutz (Mitglied) | Kostenfrei bis Limit | — |
| BoatUS (USA, Mitglied) | Kostenfrei bis Limit | — |

**Schlepp-Vorbereitung:**
1. Festmacherleine als Schlepptrosse (mind. 16 mm Durchmesser, 30 m lang)
2. An Klampe ODER durchgeführt durch Bug-Klüse befestigen
3. NICHT am Bugkorb befestigen (wird abgerissen)
4. Ruckdämpfer einsetzen (Nylontrosse oder Ankerkettenabschnitt)
5. Rudergänger an Bord für Kurshalten
6. Schlepptrosse regelmäßig prüfen (Schamfilung)

---
---

## 15. Fehlerbild-Atlas

### Fehlerbild 1: Motor startet nicht — Anlasser tot

**Erscheinungsbild:** Beim Drehen des Zündschlüssels passiert nichts.
Kein Klicken, kein Drehen.

**Typische Ursache:** Korrodierte Batterieklemmen, Massekabel-Problem,
defekter Hauptschalter.

**Diagnose-Pfad:** Batteriespannung → Klemmen → Hauptschalter →
Startrelais → Anlasser.

**Behebung:** Klemmen reinigen und nachziehen, Massekabel prüfen.

---

### Fehlerbild 2: Weißer Rauch dauerhaft

**Erscheinungsbild:** Dicker, süßlich riechender weißer Rauch, der
auch nach 10+ Minuten Betrieb nicht aufhört.

**Typische Ursache:** Defekte Zylinderkopfdichtung.

**Diagnose-Pfad:** Kühlmittelstand prüfen → CO₂-Test → Drucktest →
Ölpeilstab-Kontrolle.

**Behebung:** Zylinderkopfdichtung wechseln. Kopf auf Planlage prüfen.

---

### Fehlerbild 3: Schleichender Leistungsverlust über Wochen

**Erscheinungsbild:** Geschwindigkeit bei gleicher Drehzahl nimmt über
Wochen ab. Kein plötzliches Ereignis.

**Typische Ursache:** Bewuchs am Unterwasserschiff, Kraftstofffilter
zunehmend verschmutzt, Diesel-Bug im Anfangsstadium.

**Diagnose-Pfad:** Unterwasserschiff inspizieren → Kraftstofffilter
prüfen → Drehzahl unter Volllast messen.

**Behebung:** Rumpf reinigen, Filter wechseln, ggf. Tank behandeln.

---

### Fehlerbild 4: Motor klopft metallisch

**Erscheinungsbild:** Regelmäßiges metallisches Klopfgeräusch,
drehzahlabhängig.

**Typische Ursache:** Ventilspiel zu groß (häufig), Injektorklopfen
(mittel), Lagerschaden (selten, aber ernst).

**Diagnose-Pfad:** Stethoskop zur Lokalisierung → Ventilspiel messen →
Injektoren abklemmen → Kompressionstest.

**Behebung:** Ventilspiel einstellen, Injektoren prüfen, bei
Lagerschaden: Motorrevision.

---

### Fehlerbild 5: Öl milchig/schokoladig

**Erscheinungsbild:** Öl am Peilstab sieht aus wie Kaffeemilch.
Cremige, hellbraune Konsistenz.

**Typische Ursache:** Wasser (Kühlmittel) im Öl durch defekte
Kopfdichtung, Wärmetauscher-Leckage (Öl/Kühlmittel-Seite) oder
Kondenswasser bei langer Standzeit.

**Diagnose-Pfad:** Kühlmittelstand → CO₂-Test → Ölkühler prüfen.
Wenn nach Standzeit: Motor warmfahren und Ölwechsel.

**Behebung:** Ursache beseitigen, Öl sofort wechseln. Motor nicht
unter Last betreiben, bis Öl sauber ist.

---

### Fehlerbild 6: Starke Vibrationen bei 2.000 U/min

**Erscheinungsbild:** Zwischen 1.800 und 2.200 U/min starke Vibrationen,
darüber und darunter ruhig.

**Typische Ursache:** Resonanz im Antriebsstrang (Motorlager-Frequenz
trifft Antriebsfrequenz).

**Diagnose-Pfad:** Motorlager prüfen → Wellenfluchtung prüfen →
Propellerbalance → Drehzahlbereich vermeiden.

**Behebung:** Motorlager erneuern, Wellenanlage ausrichten.

---

### Fehlerbild 7: Motor geht bei Seegang aus

**Erscheinungsbild:** Motor stirbt bei Schräglage oder Wellengang ab,
startet dann wieder.

**Typische Ursache:** Luft im Kraftstoffsystem (Tankentnahme liegt
bei Krängung frei), Kraftstoffstand niedrig.

**Diagnose-Pfad:** Tankfüllstand prüfen → Tankentnahme-Position
prüfen → Saugleitungen auf Undichtigkeit → Vorfilter-O-Ring.

**Behebung:** Tank voll füllen, Saugleitungen abdichten, ggf.
Schwallblech im Tank nachrüsten.

---

### Fehlerbild 8: Öldruck-Alarm nur im Leerlauf

**Erscheinungsbild:** Ölwarnlampe flackert nur im warmen Leerlauf,
bei höherer Drehzahl verschwindet die Warnung.

**Typische Ursache:** Öldruck-Sensor empfindlich, Öl zu dünn
(warm, alte Füllung), beginnender Lagerverschleiß.

**Diagnose-Pfad:** Manometer anschließen → Ölzustand prüfen →
Ölwechsel → erneut messen.

**Behebung:** Ölwechsel mit korrekter Viskosität, wenn Druck weiterhin
niedrig: Ölpumpe und Lagerspiel prüfen.

---

### Fehlerbild 9: Blauer Rauch beim Anlassen

**Erscheinungsbild:** Beim Motorstart kurze Wolke blauen Rauchs,
danach kein Rauch mehr.

**Typische Ursache:** Verschlissene Ventilschaftdichtungen. Während
des Stillstands läuft Öl an den Ventilschäften vorbei in den
Brennraum und verbrennt beim Start.

**Diagnose-Pfad:** Ölverbrauch dokumentieren → Rauch nur beim Start?
→ Ventilschaftdichtungen.

**Behebung:** Ventilschaftdichtungen wechseln (Kopf muss nicht
abgenommen werden, Druckluft hält Ventile oben).

---

### Fehlerbild 10: Kühlwasser im Auspuff intermittierend

**Erscheinungsbild:** Manchmal kommt Kühlwasser aus dem Auspuff,
manchmal nicht oder nur wenig.

**Typische Ursache:** Impeller verliert Flügel (teilweise Funktion),
Seewasserfilter teilweise verstopft, Impeller-Gehäuse verschlissen.

**Diagnose-Pfad:** Seeventil → Sieb reinigen → Impeller wechseln
und FLÜGEL ZÄHLEN → Pumpengehäuse auf Rillen prüfen.

**Behebung:** Impeller wechseln, fehlende Flügel im System suchen,
ggf. Pumpengehäuse erneuern.

---

### Fehlerbild 11: Motor dreht durch (Durchgehen)

**Erscheinungsbild:** Motor beschleunigt unkontrolliert über
Nenndrehzahl, Stop-Hebel/Schlüssel ohne Wirkung.

**Typische Ursache:** Defekte Turbo-Wellendichtung (Motor saugt eigenes
Öl an und verbrennt es), defekter Drehzahlregler.

**Diagnose-Pfad:** SOFORT Luftzufuhr blockieren! DANN Ursache suchen.

**Behebung:** Turbo-Wellendichtung erneuern, Ansaugrohr auf Öl prüfen,
Regler einstellen/ersetzen.

---

### Fehlerbild 12: Dieselgeruch im Motoröl

**Erscheinungsbild:** Ölstand steigt statt zu sinken, Öl riecht nach
Diesel und ist dünnflüssiger als normal.

**Typische Ursache:** Undichter Injektor (Diesel läuft vorbei ins
Ölsystem), Einspritzpumpen-Membrandefekt, Hochdruckpumpen-Dichtung.

**Diagnose-Pfad:** Ölstand prüfen (steigt?) → Ölkonsistenz/Geruch →
Injektor-Sitze prüfen → Einspritzpumpe prüfen.

**Behebung:** Defekten Injektor identifizieren und ersetzen/abdichten,
Ölwechsel zwingend.

---
---

## 16. Troubleshooting-Entscheidungsbäume

### Entscheidungsbaum 1: Motor startet nicht

```
START: Motor startet nicht
│
├── Dreht der Anlasser?
│   │
│   ├── NEIN
│   │   ├── Batteriespannung > 12,4V?
│   │   │   ├── JA → Hauptschalter, Sicherung, Startrelais,
│   │   │   │       Neutralschalter, Anlasser prüfen
│   │   │   └── NEIN → Batterie laden/ersetzen
│   │   └── Klickt es?
│   │       ├── JA → Anlasser-Magnetschalter OK, aber
│   │       │       Batterie schwach oder Anlasser defekt
│   │       └── NEIN → Startkreis komplett unterbrochen
│   │
│   ├── LANGSAM
│   │   └── Batterie laden, Kabelverbindungen prüfen,
│   │       Öl-Viskosität prüfen, Anlasser-Zustand
│   │
│   └── JA, NORMAL
│       ├── Rauch aus dem Auspuff?
│       │   ├── JA → Kraftstoff kommt an
│       │   │   ├── Weiß → Glühkerzen, Timing, Wasser im Diesel
│       │   │   └── Schwarz → Injektoren, Luftfilter
│       │   └── NEIN → Kein Kraftstoff
│       │       ├── Kraftstoff im Tank?
│       │       ├── Absperrhahn offen?
│       │       ├── Filter verstopft?
│       │       ├── Stop-Solenoid offen?
│       │       └── System entlüftet?
│       │
│       └── Kompression vorhanden?
│           ├── JA → Kraftstoff + Timing prüfen
│           └── NEIN → Ventilspiel, Steuerriemen/kette,
│                       Kopfdichtung
```

### Entscheidungsbaum 2: Überhitzung

```
START: Temperatur zu hoch
│
├── Kühlwasser aus Auspuff?
│   │
│   ├── NEIN
│   │   ├── Seeventil offen? → JA/NEIN
│   │   ├── Sieb sauber? → Reinigen
│   │   ├── Impeller OK? → Wechseln
│   │   ├── Seewasserleitung frei? → Durchblasen
│   │   └── Wärmetauscher (Seewasser-Seite) frei? → Reinigen
│   │
│   ├── JA, WENIG
│   │   ├── Impeller teildefekt?
│   │   ├── Sieb teilweise verstopft?
│   │   └── Wärmetauscher teilweise zugesetzt?
│   │
│   └── JA, NORMAL
│       ├── Thermostat klemmt?
│       │   ├── Geschlossen → Überhitzung trotz Seewasser OK
│       │   └── Offen → Motor wird nicht warm (anderes Problem)
│       ├── Innenkreis verstopft?
│       ├── Innenkreis-Pumpe defekt?
│       ├── Keilriemen rutscht?
│       ├── Kopfdichtung → CO₂-Test
│       └── Motor überlastet?
```

### Entscheidungsbaum 3: Schwarzer Rauch

```
START: Motor raucht schwarz
│
├── Nur unter Volllast?
│   ├── JA → Motor überlastet?
│   │   ├── Drehzahl unter Soll → Propeller/Bewuchs/Getriebe
│   │   └── Drehzahl OK → Turbo/Luftfilter/Injektoren
│   └── NEIN, auch bei Teillast
│       ├── Luftfilter verstopft?
│       ├── Turbolader defekt?
│       ├── Injektoren tropfen?
│       ├── Ventilspiel falsch?
│       └── Einspritztiming falsch?
│
└── Nur bei Kaltstart?
    └── Normal bei Diesel, verschwindet nach 1–2 Min.
        Wenn länger → Glühkerzen, Timing
```

### Entscheidungsbaum 4: Leistungsverlust

```
START: Motor hat weniger Leistung
│
├── Plötzlich oder schleichend?
│   │
│   ├── PLÖTZLICH
│   │   ├── Turbolader-Schaden? → Ladedruck prüfen
│   │   ├── Kraftstoff-Unterbrechung? → Filter, Luft im System
│   │   ├── Steuerkette/-riemen übersprungen? → Timing prüfen
│   │   └── Angeleine am Propeller? → Taucher
│   │
│   └── SCHLEICHEND (über Wochen/Monate)
│       ├── Bewuchs am Rumpf? → Unterwasserschiff reinigen
│       ├── Diesel-Bug? → Kraftstoff-System
│       ├── Kraftstofffilter zunehmend schmutzig?
│       ├── Injektoren verkokt? → Abdrücktest
│       ├── Kompression nachlassend? → Test durchführen
│       ├── Turbo-Verschleiß? → Ladedruck + Spiel
│       └── Auspuff-Gegendruck? → Messen
│
├── Drehzahl bei Volllast?
│   ├── Erreicht → Problem nicht am Motor (Propeller/Rumpf)
│   └── Nicht erreicht → Problem am Motor
│
└── Gleichmäßiger Leistungsverlust oder ruckelig?
    ├── Gleichmäßig → Allgemeiner Verschleiß/Verstopfung
    └── Ruckelig → Einzelner Zylinder/Injektor-Problem
```

### Entscheidungsbaum 5: Ölverlust

```
START: Ölstand sinkt
│
├── Leckage sichtbar?
│   │
│   ├── JA → Stelle identifizieren
│   │   ├── Oben am Motor → Ventildeckeldichtung
│   │   ├── Vorne → Kurbelwellendichtring vorn
│   │   ├── Hinten → Kurbelwellendichtring hinten
│   │   ├── Unten → Ölwannendichtung
│   │   ├── Am Filter → O-Ring, Filter nachziehen
│   │   └── Am Turbo → Ölzulauf/-rücklauf prüfen
│   │
│   └── NEIN → Verbrauch intern
│       ├── Blauer Rauch?
│       │   ├── Beim Start → Ventilschaftdichtungen
│       │   ├── Unter Last → Kolbenringe
│       │   └── Dauerhaft → Turbo + Ringe
│       ├── Kraftstoff im Öl? → Ölstand STEIGT
│       │   └── → Injektor-Leckage
│       └── Wasser im Öl? → Milchig
│           └── → Kopfdichtung
```

---
---

## 17. FAQ

### FAQ 1: Wie oft sollte ich den Kompressionstest machen?

Empfehlung: Einmal jährlich vor Saisonstart oder alle 500 Betriebsstunden.
Zusätzlich bei Verdacht auf Kompressionsverlust (schwerer Start,
Leistungsverlust, blauer Rauch). Dokumentieren Sie die Werte — der
Trend über die Jahre ist der wichtigste Indikator.

### FAQ 2: Kann ich den Motor kurz ohne Kühlwasser laufen lassen?

Maximal 15–30 Sekunden im Leerlauf, um z.B. nach einem Impellerwechsel
zu prüfen, ob Wasser kommt. Alles darüber riskiert Überhitzungsschäden,
besonders am Auspuffkrümmer (Rissbildung) und an der Impellerpumpe.

### FAQ 3: Was tun, wenn Öl milchig ist?

SOFORT Motor abstellen. Milchiges Öl = Wasser im Öl. Mögliche Ursachen:
Kopfdichtung, gerissener Wärmetauscher, oder Kondenswasser nach langer
Standzeit. Ursache identifizieren und beheben. Öl komplett wechseln,
ggf. Motor mit Spülöl durchspülen. Nicht unter Last fahren.

### FAQ 4: Mein Öldruck ist im Leerlauf niedrig — wie ernst ist das?

Wenn der Öldruck bei kaltem Motor normal ist und nur bei warmem Leerlauf
niedrig wird: Zunächst mit unabhängigem Manometer verifizieren.
Wenn bestätigt: Ölwechsel auf korrekte Viskosität. Wenn weiterhin
niedrig: Lagerspiel und Ölpumpe prüfen lassen. Nicht ignorieren.

### FAQ 5: Wie erkenne ich, ob mein Turbolader defekt ist?

Symptome: Leistungsverlust, schwarzer oder blauer Rauch, ungewöhnliches
Pfeifen, Öl im Ladeluftschlauch. Schnellcheck: Ladeluftschlauch abnehmen
und Turbinenrad von Hand drehen — muss sich leicht und ohne Schleifen
drehen. Radiales Spiel max. 0,08 mm.

### FAQ 6: Was bedeutet Diesel-Bug und wie verhindere ich ihn?

Diesel-Bug sind Mikroorganismen, die in der Wasser-Diesel-Grenzschicht
wachsen. Prävention: Tank möglichst voll halten, regelmäßig
Wasserabscheider entleeren, jährlich Biozid verwenden, bei Langfahrt
Polierfilter einsetzen.

### FAQ 7: Mein Motor qualmt schwarz — muss ich in die Werkstatt?

Nicht unbedingt. Häufigste Ursache: Luftfilter verstopft (selbst
wechselbar) oder Motor überlastet (Bewuchs am Rumpf). Erst diese
einfachen Ursachen prüfen, dann Injektoren und Turbo.

### FAQ 8: Wie entlüfte ich das Kraftstoffsystem richtig?

Bei mechanischer Einspritzung: Entlüftungsschrauben am Filtergehäuse
und an der Einspritzpumpe nacheinander öffnen, mit Handpumpe pumpen
bis Diesel blasenfrei kommt, dann Injektorleitungen lockern und Anlasser
drehen. Bei Common-Rail: Mehrfach Anlasser betätigen — das System
entlüftet sich selbst.

### FAQ 9: Wie wichtig ist die Ölanalyse wirklich?

Sehr wichtig für Langfahrer und teure Motoren. Eine Analyse kostet
30–60 EUR und kann Tausende EUR Reparaturkosten vermeiden, indem
Probleme frühzeitig erkannt werden. Für Wochenendsegler mit jährlichem
Ölwechsel: Mindestens alle 2–3 Jahre empfohlen.

### FAQ 10: Was ist ein Notlauf-Modus bei Common-Rail-Motoren?

Der Notlauf-Modus ist eine Schutzfunktion der ECU. Bei bestimmten
Fehlern wird die Motorleistung begrenzt (z.B. max. 1.500 U/min),
um weitere Schäden zu vermeiden. Der Motor läuft noch, aber mit
stark reduzierter Leistung. Ursache beheben und Fehlercode löschen.

### FAQ 11: Kann ich Automotor-Öl im Marine-Diesel verwenden?

Grundsätzlich muss die Spezifikation stimmen. Marine-Diesel brauchen
Öl mit hohem Verschleißschutz (API CF, CI-4). Viele hochwertige
Auto-Diesel-Öle erfüllen diese Spezifikation. ABER: Benziner-Öl
(API SN/SP ohne CF-Freigabe) ist NICHT geeignet — zu wenig
Säurepufferung und Verschleißschutz für Diesel.

### FAQ 12: Mein Motor macht ein Pfeifgeräusch — was ist das?

Häufigste Ursachen: 1) Keilriemen quietscht (Spannung prüfen),
2) Turbolader-Geräusch (normal, wenn gleichmäßig), 3) Undichtigkeit
in der Ansaugung oder Abgasanlage, 4) Turbo-Lagerschaden (wenn
Geräusch neu ist und lauter wird).

### FAQ 13: Wie gefährlich ist ein durchgehender Dieselmotor?

Extrem gefährlich. Der Motor kann sich bis zur Selbstzerstörung
hochdrehen (Pleuel durchschlagen Motorblock, Teile fliegen umher).
Sofort Luftzufuhr blockieren (Tuch, Brett, CO₂-Feuerlöscher).
NIEMALS versuchen, den Motor mechanisch zu stoppen.

### FAQ 14: Mein Motor springt bei Kälte schlecht an — was hilft?

1) Glühkerzen prüfen und ggf. ersetzen, 2) Vorglühzeit einhalten
(30–60 Sekunden bei alten Motoren), 3) Dünnflüssigeres Öl verwenden
(5W-40 oder 10W-40), 4) Winterdiesel tanken, 5) Batterie warm halten,
6) Starthilfespray als letzter Ausweg (Ether — sparsam dosieren,
NICHT bei Glühkerzen!).

### FAQ 15: Wie erkenne ich, ob der Impeller gewechselt werden muss?

Wenn einer der folgenden Punkte zutrifft: 1) Kühlwasserfluss aus dem
Auspuff reduziert, 2) Motor wird unter Last wärmer als üblich,
3) Impeller ist älter als 2 Jahre, 4) Motor hat trocken gelaufen,
5) Gummipartikel im Seewasserfilter.

### FAQ 16: Was bedeuten die verschiedenen Rauchfarben?

Schwarz = zu viel Kraftstoff oder zu wenig Luft (Luftfilter, Turbo,
Überlastung). Weiß = Kühlmittel im Brennraum (ernst) oder kalter
Motor (harmlos). Blau = Öl verbrennt (Ringe, Ventilschaftdichtungen,
Turbo).

### FAQ 17: Wie prüfe ich den Zustand meines Seewasserfilters?

Sichtprüfung durch das transparente Gehäuse. Wenn nicht transparent:
Seeventil schließen, Deckel öffnen, Filterkorb inspizieren. Partikel,
Seegras, Muscheln oder Impeller-Gummireste entfernen. In tropischen
Gewässern alle 10–20 Betriebsstunden prüfen.

### FAQ 18: Mein Motor vibriert plötzlich stark — was tun?

Sofort Drehzahl reduzieren. Systematisch prüfen: 1) Angeleine am
Propeller?, 2) Propeller beschädigt?, 3) Motorlager gebrochen?,
4) Wellenanlage-Problem? Wenn Ursache nicht sofort erkennbar:
Motor abstellen und Antriebsstrang inspizieren.

### FAQ 19: Wann ist ein Motor wirklich am Ende seiner Lebensdauer?

Indikatoren: 1) Kompression unter Minimum bei allen Zylindern,
2) Ölverbrauch > 2 l/100 h, 3) Metallpartikel in der Ölanalyse
drastisch erhöht, 4) Risse im Block oder Kopf, 5) Reparaturkosten
> 60 % des Motorwerts. Ein gut gewarteter Marine-Diesel hält
8.000–15.000 Betriebsstunden.

### FAQ 20: Was kostet ein Motoraustausch vs. Generalüberholung?

Generalüberholung (Komplett, mit Zylinderkopf): 4.000–12.000 EUR
je nach Motor. Neuer Motor (inkl. Einbau): 12.000–60.000 EUR
je nach Leistung und Hersteller. Faustregel: Überholung lohnt,
wenn Kosten < 50 % vom Neumotor UND Block/Kopf intakt.

### FAQ 21: Kann ich Fehlercodes selbst auslesen?

Bei älteren mechanischen Motoren: Keine Fehlercodes vorhanden.
Bei modernen Common-Rail-Motoren: Basis-Auslesen mit günstigen
CAN-Bus-Readern (50–200 EUR) möglich. Für erweiterte Diagnose und
Programmierung sind herstellerspezifische Tools nötig (2.500–4.000 EUR).

### FAQ 22: Was ist der Unterschied zwischen 2-Takt- und 4-Takt-Diesel?

Im Yachtbereich werden fast ausschließlich 4-Takt-Diesel verwendet.
2-Takt-Diesel gibt es nur bei sehr großen Schiffen (Containerschiffe).
Ein 4-Takt-Diesel hat Ansaugen-Verdichten-Arbeiten-Ausstoßen als
Arbeitszyklus (2 Kurbelwellenumdrehungen pro Arbeitstakt).

### FAQ 23: Mein Getriebe macht ein mahlendes Geräusch — was bedeutet das?

Mögliche Ursachen: 1) Getriebeöl zu niedrig oder zu alt, 2) Kupplungsbeläge
verschlissen, 3) Zahnrad-Verschleiß, 4) Lager-Verschleiß. Zuerst
Getriebeölstand und -zustand prüfen. Wenn Metallspäne im Öl: Getriebe
muss zum Spezialisten.

### FAQ 24: Wie lange kann ich mit einer Überhitzungs-Warnung noch fahren?

Gar nicht. Sofort Last reduzieren und Ursache suchen. Wenn die
Temperatur über 100 °C steigt, Motor auf Leerlauf. Über 105 °C:
Motor abstellen. Jede Minute Überhitzung kann tausende EUR Schaden
verursachen.

### FAQ 25: Was ist der häufigste Motorfehler auf Yachten?

Statistische Auswertung (nach Häufigkeit):
1. Luft im Kraftstoffsystem (28 %)
2. Batterie/Elektrik-Probleme (22 %)
3. Impeller defekt / Kühlsystem (18 %)
4. Kraftstofffilter verstopft (12 %)
5. Keilriemen locker/gerissen (8 %)
6. Alle anderen (12 %)

### FAQ 26: Mein Motor läuft, aber die Lichtmaschine lädt nicht — was tun?

Prüfreihenfolge: 1) Keilriemen vorhanden und gespannt?, 2) Ladekontrolllampe
brennt? (Wenn nicht → Birne defekt, Lichtmaschine bekommt keine Erregung),
3) Spannung an B+ der Lichtmaschine bei laufendem Motor messen (> 13,5 V?),
4) Kohlen der Lichtmaschine prüfen (Verschleiß).

### FAQ 27: Wie verhalte ich mich bei Wassereinbruch über die Auspuffanlage?

Dies passiert, wenn bei rauem Wetter Seewasser rückwärts durch den Auspuff
in den Motor gelangt (Hydro-Lock). Symptome: Motor blockiert plötzlich.
NIEMALS versuchen, den Motor mit dem Anlasser zu drehen (Pleuelbruch!).
Glühkerzen/Injektoren ausbauen und Wasser ablaufen lassen. Öl wechseln.
Motor von Hand durchdrehen. Dann erst starten.

---
---

## 18. Glossar

| Nr. | Begriff | Erklärung |
|-----|---------|-----------|
| 1 | Abdrücktest | Prüfverfahren für Injektoren unter hohem Druck zur Beurteilung von Öffnungsdruck und Spritzbild |
| 2 | AGR (Abgasrückführung) | System zur Rückführung eines Teils der Abgase in den Ansaugtrakt zur Reduktion von NOx-Emissionen |
| 3 | Anlasser (Starter) | Elektromotor zum Durchdrehen des Dieselmotors beim Start |
| 4 | Biozid | Chemisches Mittel zur Abtötung von Mikroorganismen im Kraftstoffsystem (z.B. Grotamar 82) |
| 5 | Blow-by | Verbrennungsgase, die an den Kolbenringen vorbei ins Kurbelgehäuse gelangen |
| 6 | CAN-Bus | Controller Area Network — digitales Kommunikationssystem zwischen Motorsteuergerät und Peripherie |
| 7 | Common-Rail | Hochdruck-Einspritzsystem mit gemeinsamer Druckleitung (Rail) für alle Injektoren |
| 8 | Cutless-Lager | Gummilager im Stevenrohr, das die Propellerwelle führt und durch Seewasser geschmiert wird |
| 9 | Dekompression | Vorrichtung zum Druckabbau in den Zylindern, erleichtert das Durchdrehen von Hand |
| 10 | Diesel-Bug | Mikrobiologische Kontamination im Dieselkraftstoff durch Pilze und Bakterien |
| 11 | DTC (Diagnostic Trouble Code) | Standardisierter Fehlercode, der von der ECU gespeichert wird |
| 12 | ECU (Engine Control Unit) | Elektronisches Motorsteuergerät bei modernen Common-Rail-Motoren |
| 13 | Einspritzpumpe | Mechanische oder elektronische Pumpe zur Hochdruck-Kraftstoffförderung zu den Injektoren |
| 14 | EVC (Electronic Vessel Control) | Elektronisches Steuerungssystem von Volvo Penta für Gashebel, Getriebe und Motor |
| 15 | Frostschutz (Glykol) | Ethylenglykol- oder Propylenglykol-Mischung als Kühlmittel-Zusatz |
| 16 | Glühkerze | Elektrisches Heizelement im Brennraum zur Unterstützung des Kaltstarts |
| 17 | Hydro-Lock | Blockierung des Motors durch Flüssigkeit im Zylinder (Wasser oder Diesel), die nicht komprimierbar ist |
| 18 | Impeller | Gummi-Flügelrad in der Seewasserpumpe zur Förderung des Kühlwassers |
| 19 | Injektor | Einspritzdüse, die Kraftstoff unter hohem Druck fein zerstäubt in den Brennraum einspritzt |
| 20 | Kavitation | Dampfblasenbildung durch Unterdruck an schnell bewegten Oberflächen (Propeller, Pumpen) |
| 21 | Keilriemen | Antriebsriemen für Nebenaggregate (Lichtmaschine, Wasserpumpe) |
| 22 | Kompressionstest | Messung des Verdichtungsdrucks in den Zylindern zur Beurteilung des mechanischen Zustands |
| 23 | Kopfdichtung | Dichtung zwischen Zylinderkopf und Motorblock, dichtet Brennraum, Öl- und Kühlkanäle |
| 24 | Kurbelgehäuseentlüftung | System zur Ableitung von Blow-by-Gasen aus dem Kurbelgehäuse |
| 25 | Ladeluft | Durch den Turbolader komprimierte Luft vor der Einleitung in die Zylinder |
| 26 | Ladeluftkühler (Intercooler) | Wärmetauscher zur Kühlung der vom Turbolader komprimierten Luft |
| 27 | Lagerspiel | Abstand zwischen Welle und Lagerschale, dient der Ölfilmbildung |
| 28 | Magnetschalter | Elektromagnetisches Relais am Anlasser, das den Starterstrom schaltet |
| 29 | Masseverbindung | Elektrische Rückleitung über den Motorblock zur Batterie |
| 30 | NTC-Sensor | Negative Temperature Coefficient — Widerstand sinkt bei steigender Temperatur |
| 31 | Notlauf (Limp Home) | Schutzmodus der ECU bei erkanntem Fehler, begrenzt Leistung |
| 32 | Ölanalyse | Laboruntersuchung einer Ölprobe auf Verschleißmetalle, Verunreinigungen und Additive |
| 33 | Öldruckbegrenzungsventil | Ventil in der Ölpumpe, das den maximalen Öldruck begrenzt |
| 34 | Ölpeilstab | Messstab zur Kontrolle des Ölstands im Motor |
| 35 | Pleuellager | Gleitlager zwischen Pleuelstange und Kurbelwelle |
| 36 | Raildruck | Druck im Common-Rail-Kraftstoffspeicher (250–2.000 bar) |
| 37 | Resonanz | Schwingungsverstärkung, wenn Anregungsfrequenz und Eigenfrequenz übereinstimmen |
| 38 | Saildrive | Antriebseinheit, die Motor und Propeller kombiniert, durch den Rumpfboden geführt |
| 39 | Seewasserfilter (Strainer) | Filtergehäuse mit Siebkorb vor der Seewasserpumpe |
| 40 | Solenoid (Stop-Solenoid) | Elektromagnetisches Ventil zur Kraftstoffabsperrung beim Motorstop |
| 41 | Spritzbild | Muster der Kraftstoffzerstäubung eines Injektors beim Abdrücktest |
| 42 | Stevenrohr | Rohr durch den Rumpf, durch das die Propellerwelle geführt wird |
| 43 | Steuerkette/-riemen | Antrieb für Nockenwelle und Einspritzpumpe, synchronisiert Ventilsteuerung |
| 44 | Stopfbuchse | Dichtung am Stevenrohr-Durchgang, verhindert Wassereinbruch um die Welle |
| 45 | TAN (Total Acid Number) | Säurezahl des Öls — Maß für die Ölalterung |
| 46 | TBN (Total Base Number) | Basenzahl des Öls — Maß für die verbleibende Neutralisationsreserve |
| 47 | Thermostat | Temperaturgesteuertes Ventil im Kühlkreislauf, regelt die Betriebstemperatur |
| 48 | Turbolader | Abgasgetriebener Kompressor zur Erhöhung der Ansaugluftmenge |
| 49 | Ventilschaftdichtung | Dichtring am Ventilschaft, verhindert Öleintritt in den Brennraum |
| 50 | Ventilspiel | Spalt zwischen Ventilschaft und Kipphebel bei kaltem Motor |
| 51 | Viskosität | Zähflüssigkeit des Öls, angegeben als SAE-Klasse (z.B. 15W-40) |
| 52 | Vodia | Volvo Penta Diagnose-Software für EVC-Systeme und Common-Rail-Motoren |
| 53 | Vorfilter (Wasserabscheider) | Erster Filter im Kraftstoffsystem, trennt Wasser vom Diesel |
| 54 | Vorkammer | Nebenbrennraum bei indirekter Einspritzung, Glühkerze sitzt hier |
| 55 | Wastegate | Bypass-Ventil am Turbolader zur Begrenzung des Ladedrucks |
| 56 | Wärmetauscher | Gerät zum Wärmeaustausch zwischen Innenkreis (Kühlmittel) und Außenkreis (Seewasser) |
| 57 | Wellenfluchtung (Alignment) | Ausrichtung der Motorwelle zur Propellerwelle, kritisch für Vibrationsfreiheit |
| 58 | Zinkanode | Opferanode im Kühlsystem zum Schutz unedlerer Metalle vor galvanischer Korrosion |

---
---

## 19. Schnell-Referenz

### 19.1 Die 10 häufigsten Motorprobleme und ihre Lösung

| Nr. | Problem | Häufigste Ursache | Schnellfix |
|-----|---------|-------------------|------------|
| 1 | Motor startet nicht | Batterie/Klemmen | Klemmen reinigen, laden |
| 2 | Motor stirbt ab | Luft im Kraftstoff | Entlüften |
| 3 | Überhitzung | Impeller defekt | Impeller wechseln |
| 4 | Schwarzer Rauch | Luftfilter verstopft | Filter wechseln |
| 5 | Weißer Rauch (kalt) | Glühkerzen defekt | Glühkerzen wechseln |
| 6 | Vibrationen | Motorlager verschlissen | Lager wechseln |
| 7 | Leistungsverlust | Bewuchs Unterwasserschiff | Rumpf reinigen |
| 8 | Öldruck-Alarm | Sensor defekt | Mit Manometer verifizieren |
| 9 | Keilriemen quietscht | Zu locker | Nachspannen |
| 10 | Motor klopft | Ventilspiel zu groß | Ventilspiel einstellen |

### 19.2 Diagnose-Kurzübersicht: Rauchfarbe

| Rauch | Kalt | Warm | Unter Last |
|-------|------|------|------------|
| Schwarz | Normal (kurz) | Injektor/Luftfilter | Überlastung/Turbo |
| Weiß | Glühkerzen | KOPFDICHTUNG! | KOPFDICHTUNG! |
| Blau | Ventilschaftdicht. | Turbo-Dichtung | Kolbenringe |

### 19.3 Notfall-Checkliste: Motor ausgefallen auf See

```
□ Ruhe bewahren, Position feststellen
□ Segel setzen / Anker bereit
□ Batteriespannung prüfen
□ Ölstand prüfen (Peilstab)
□ Kühlmittelstand prüfen
□ Kraftstoff vorhanden?
□ Seeventil offen?
□ Startversuch (max. 3×, je 10 Sek.)
□ Wenn kein Start: Systematische Diagnose (Kap. 2)
□ Wenn keine Eigenreparatur: Hilfe rufen
```

### 19.4 Kompressionstest-Referenztabelle

| Motor | Soll (bar) | Min. (bar) | Max. Differenz |
|-------|-----------|-----------|----------------|
| Yanmar GM/YM | 28–32 | 22 | < 10 % |
| Yanmar JH | 28–32 | 22 | < 10 % |
| Yanmar LHA | 30–35 | 25 | < 10 % |
| Volvo D1/D2 | 25–33 | 20–22 | < 10 % |
| Volvo D3+ | 30–38 | 25 | < 10 % |
| Beta 14–50 | 26–33 | 20–22 | < 10 % |
| Nanni N-Serie | 27–34 | 21–22 | < 10 % |

### 19.5 Öldruck-Schnellreferenz

| Zustand | Soll (bar) | Alarm |
|---------|-----------|-------|
| Leerlauf warm | 1,0–2,0 | < 0,5 |
| Betriebsdrehzahl | 3,0–5,0 | < 1,5 |
| Volllast | 3,5–6,0 | < 2,0 |

---
---

## 20. ANHANG A–H: Fallstudien

### ANHANG A: Fallstudie — Bavaria 38, Yanmar 3JH, Überhitzung unter Last

**Boot:** Bavaria 38 Cruiser, Baujahr 2008
**Motor:** Yanmar 3JH5E, 39 PS, 2.800 Betriebsstunden
**Symptom:** Motor wird unter Last (> 2.500 U/min) heiß, Alarm bei 100 °C.
Im Leerlauf normal (82 °C).

**Diagnose-Verlauf:**
1. Seeventil geprüft — offen, Durchfluss OK
2. Seewasserfilter gereinigt — leicht verschmutzt, aber nicht verstopft
3. Impeller gewechselt — Impeller sah noch gut aus, ABER 2 Flügel
   verkürzt (30 % verschlissen). Alle Flügel vorhanden.
4. Wärmetauscher-Endkappen geöffnet — Seewasser-Rohrbündel teilweise
   mit Kalkablagerungen zugesetzt (geschätzt 40 % Durchfluss reduziert)
5. Wärmetauscher mit 10 % Zitronensäure über Nacht eingeweicht, gespült
6. Zinkanode im Wärmetauscher: komplett aufgezehrt → Korrosion hatte
   begonnen

**Ergebnis:** Nach Reinigung des Wärmetauschers und neuem Impeller:
Temperatur unter Volllast stabil 84 °C. Zinkanode ersetzt.

**Kosten:** Impeller 45 EUR, Zinkanode 12 EUR, Zitronensäure 5 EUR,
Arbeitszeit 3 Stunden.

**Lehre:** Jährliche Zinkanoden-Kontrolle im Wärmetauscher kann teure
Reinigungen und Überhitzungsschäden vermeiden.

---

### ANHANG B: Fallstudie — Hallberg-Rassy 40, Volvo D2-40, Startproblem

**Boot:** Hallberg-Rassy 40, Baujahr 2012
**Motor:** Volvo Penta D2-40, 38 PS, 1.200 Betriebsstunden
**Symptom:** Motor startet nach Winterlager nicht. Anlasser dreht kräftig,
aber Motor zündet nicht. Kein Rauch aus dem Auspuff.

**Diagnose-Verlauf:**
1. Batterie: 12,8 V, Anlasser dreht kräftig → OK
2. Kraftstoff: Tank halb voll → OK
3. Kraftstoffhahn: Offen → OK
4. Vorfilter: Wasser im Wasserabscheider (ca. 100 ml) → entleert
5. Kraftstofffilter: Schwarze Schleim-Rückstände sichtbar → DIESEL-BUG
6. Beide Filter gewechselt, System entlüftet
7. Erster Startversuch: Motor springt an, läuft 30 Sekunden, stirbt ab
8. Zweiter Filterwechsel: Neuer Filter schon wieder dunkel nach 30 Sek.
9. Tank teilweise entleert, Bodensatz: Schwarze Masse → schwerer Diesel-Bug

**Behandlung:**
- Tank vollständig geleert und professionell gereinigt
- Alle Kraftstoffleitungen durchgespült
- Neue Filter montiert, Biozid (Grotamar 82) in frischen Diesel
- Nach Reinigung: Motor startet sofort und läuft einwandfrei

**Kosten:** Tankreinigung (Fachfirma) 450 EUR, 4× Filter 120 EUR,
Biozid 35 EUR, Diesel 200 EUR.

**Lehre:** Tank vor dem Winterlager voll füllen und Biozid hinzugeben.
Regelmäßig Wasserabscheider kontrollieren.

---

### ANHANG C: Fallstudie — Jeanneau SO 349, Yanmar 3YM20, Leistungsverlust

**Boot:** Jeanneau Sun Odyssey 349, Baujahr 2016
**Motor:** Yanmar 3YM20, 21 PS, 800 Betriebsstunden
**Symptom:** Motor erreicht bei Volllast nur noch 6,2 kn statt 7,5 kn.
Drehzahl bei Volllast nur 2.900 U/min statt 3.600 U/min (Nenndrehzahl).

**Diagnose-Verlauf:**
1. Luftfilter geprüft: Sauber → OK
2. Kraftstofffilter geprüft: Sauber → OK
3. Unterwasserschiff inspiziert (Taucher): Starker Bewuchs trotz
   Antifouling (2 Jahre alt). Propeller: 5 mm Pocken.
4. Rumpf und Propeller gereinigt
5. Erneuter Test: Volllast-Drehzahl jetzt 3.250 U/min → besser, aber
   immer noch unter Soll
6. Propeller geprüft: Ein Blatt leicht verbogen (Grundberührung)
7. Propeller richten lassen und ausgewuchtet

**Ergebnis:** Vollast-Drehzahl 3.380 U/min, Geschwindigkeit 7,4 kn.

**Kosten:** Taucher (Reinigung) 120 EUR, Propeller richten 80 EUR.

**Lehre:** Bewuchs ist die häufigste Ursache für Leistungsverlust.
Regelmäßige Unterwasserschiff-Inspektion und aktuelles Antifouling.

---

### ANHANG D: Fallstudie — Hanse 385, Volvo D1-30, Öl im Kühlwasser

**Boot:** Hanse 385, Baujahr 2014
**Motor:** Volvo Penta D1-30, 28 PS, 1.600 Betriebsstunden
**Symptom:** Ölfilm auf der Kühlmitteloberfläche im Ausgleichsbehälter.
Kein Leistungsverlust, kein Rauch.

**Diagnose-Verlauf:**
1. CO₂-Test am Kühlmittel: Negativ → Kopfdichtung wahrscheinlich OK
2. Kompressionstest: Alle 3 Zylinder 29–31 bar → OK
3. Öl am Peilstab: Normal, nicht milchig → kein Kühlmittel im Öl
4. Wärmetauscher inspiziert: Öl-Kühlmittel-Bereich
5. Diagnose: Wärmetauscher intern undicht (Öl-/Kühlmittel-Seite)

**Behandlung:**
- Wärmetauscher gegen Austausch-Wärmetauscher ersetzt
- Kühlsystem gespült und mit frischem Kühlmittel befüllt
- Ölwechsel durchgeführt

**Kosten:** Austausch-Wärmetauscher 680 EUR, Kühlmittel 35 EUR,
Öl + Filter 60 EUR, Arbeitszeit 4 Stunden.

**Lehre:** Ölfilm im Kühlmittel muss nicht Kopfdichtung bedeuten.
Wärmetauscher als Ursache in Betracht ziehen.

---

### ANHANG E: Fallstudie — Catalina 375, Beta 38, Vibrationen

**Boot:** Catalina 375, Baujahr 2010
**Motor:** Beta Marine 38, 38 PS, 2.200 Betriebsstunden
**Symptom:** Zunehmende Vibrationen über 6 Monate, besonders bei
1.800–2.200 U/min. Darüber und darunter erträglich.

**Diagnose-Verlauf:**
1. Motor im Leerlauf, Getriebe Neutral: Leichte Vibration → Motor OK
2. Getriebe eingelegt, Leerlauf: Vibration stärker → Antriebsstrang
3. Motorlager inspiziert: 2 von 4 Lagern sichtbar eingesunken,
   Gummi gerissen
4. Wellenfluchtung gemessen: 0,15 mm radial, 1,2 mm/m angular → zu viel
5. Motorlager gewechselt (alle 4)
6. Wellenanlage neu ausgerichtet

**Ergebnis:** Vibrationen vollständig beseitigt.

**Kosten:** 4 Motorlager 320 EUR, Alignment-Service 250 EUR.

**Lehre:** Motorlager regelmäßig inspizieren (jährlich). Defekte Lager
verändern die Wellenfluchtung und verursachen Folgeschäden.

---

### ANHANG F: Fallstudie — X-Yachts 43, Yanmar 4JH-TE, Schwarzer Rauch

**Boot:** X-Yachts X-43, Baujahr 2006
**Motor:** Yanmar 4JH4-TE, 75 PS Turbodiesel, 3.500 Betriebsstunden
**Symptom:** Schwarzer Rauch unter Last, besonders bei > 70 % Gas.
Vollast-Drehzahl 100 U/min unter Spezifikation.

**Diagnose-Verlauf:**
1. Luftfilter: Stark verschmutzt (18 Monate nicht gewechselt) → gewechselt
2. Erneuter Test: Leichte Verbesserung, aber immer noch schwarzer Rauch
3. Turbolader inspiziert: Radialspiel 0,12 mm (Soll max. 0,08 mm)
4. Öl im Ladeluftschlauch: Ja, deutlich → Turbo-Wellendichtung undicht
5. Ladedruck bei Volllast: Nur 0,4 bar (Soll 0,6–0,8 bar)
6. Turbolader zur Überholung an Spezialisten gegeben

**Ergebnis:** Nach Turbo-Überholung: Kein schwarzer Rauch, Ladedruck
0,7 bar, Volllast-Drehzahl korrekt.

**Kosten:** Luftfilter 25 EUR, Turbo-Überholung 1.200 EUR.

**Lehre:** Luftfilter regelmäßig wechseln. Turbo-Verschleiß ist bei
Marine-Motoren durch Salzluft und Unterlastbetrieb beschleunigt.

---

### ANHANG G: Fallstudie — Beneteau Oceanis 45, Yanmar 4JH, Elektrisch tot

**Boot:** Beneteau Oceanis 45, Baujahr 2015
**Motor:** Yanmar 4JH4-E, 54 PS, 1.000 Betriebsstunden
**Symptom:** Alle Motorinstrumente tot. Kein Startversuch möglich.
Bordnetz funktioniert normal (Licht, Plotter OK).

**Diagnose-Verlauf:**
1. Batterie-Hauptschalter: Auf Position „1" (Startbatterie) → OK
2. Startbatterie: 12,7 V → OK
3. Sicherungskasten Motor: 15 A Sicherung für Motor-Instrumentierung
   durchgebrannt
4. Neue Sicherung eingesetzt: Brennt sofort wieder durch → Kurzschluss
5. Kabelbaum am Motor inspiziert: Kabel am Auspuffkrümmer-Schild
   gescheuert, Isolation beschädigt
6. Blanker Kupferleiter berührt Motorblock → Kurzschluss
7. Kabel isoliert und neu verlegt, mit Schutzschlauch versehen

**Ergebnis:** Sicherung hält, Instrumente funktionieren, Motor startet.

**Kosten:** Sicherungen 5 EUR, Schrumpfschlauch 3 EUR, Schutzschlauch
8 EUR, Arbeitszeit 2 Stunden.

**Lehre:** Jährliche Sichtprüfung aller Kabel im Motorraum auf
Scheuerung an heißen oder vibrationsbeanspruchten Stellen.

---

### ANHANG H: Fallstudie — Moody 41, Volvo D2-55, Leistungsverlust durch Kraftstoffverschmutzung

**Boot:** Moody 41 DS, Baujahr 2018
**Motor:** Volvo Penta D2-55, 55 PS, 600 Betriebsstunden

> ✅ Aufgeloest (Audit): Der Volvo Penta D2-55 hat eine mechanische,
> nockengetriebene Reiheneinspritzpumpe mit Förderpumpe und Handpumpe
> (Perkins-103-Basis, baugleich mit MD2010–2040) — KEIN Common-Rail. Die
> Fallstudie wurde auf mechanische Einspritzung/Kraftstoffmangel korrigiert;
> die nicht plausiblen „Raildruck"- und VODIA5-Rail-Fehlercode-Angaben wurden
> entfernt. Quelle: Volvo Penta D2-55 Werkstatthandbuch (Group 23 Fuel System —
> Injection Pump) und offizielle D2-55 Motorbeschreibung („cam driven in-line
> injection pump with feed pump and hand primer").

**Symptom:** Während der Fahrt plötzlich Leistungsreduktion. Motor läuft
nur noch bei max. 1.500 U/min und nimmt kein Gas mehr an. Leichter
schwarzer Rauch unter Last — typisch für Kraftstoffmangel bei mechanischer
Einspritzung (Regler begrenzt die Fördermenge).

**Diagnose-Verlauf:**
1. Kühlmittel-Temperatur: 85 °C → Normal
2. Öldruck: Normal
3. Kraftstoff-Vorfilter (Wasserabscheider) geöffnet: Schauglas voll Wasser,
   Filterelement dunkel verschmutzt
4. Hauptfilter: Stark verschmutzt, deutlich reduzierter Durchfluss
5. Beide Filter gewechselt, Kraftstoffsystem mit der Handpumpe entlüftet,
   Motor neu gestartet
6. Motor nimmt wieder sauber Gas an, volle Leistung wiederhergestellt

**Ergebnis:** Motor läuft wieder mit voller Leistung.

**Kosten:** 2 Filter 90 EUR, Arbeitszeit 1 Stunde.

**Lehre:** Kraftstoffverschmutzung und Wasser im Tank sind eine der häufigsten
Ursachen für plötzlichen Leistungsverlust. Auch mechanisch eingespritzte
Motoren reagieren auf verstopfte Filter mit Fördermengenmangel und
Drehzahlbegrenzung. Vorfilter/Wasserabscheider regelmäßig kontrollieren und
Filterwechsel-Intervalle einhalten.

---
---

## 21. ANHANG I–R: Pydantic v2 Datenmodelle

### ANHANG I: Basis-Diagnosemodelle

```python
"""
Motor-Troubleshooting Pydantic v2 Datenmodelle.
Alle Modelle verwenden model_config = {"from_attributes": True}.
NIEMALS class Config verwenden.
"""

from __future__ import annotations

from datetime import datetime
from enum import Enum
from typing import Optional

from pydantic import BaseModel, Field


# ---------------------------------------------------------------------------
# Enums
# ---------------------------------------------------------------------------

class SymptomKategorie(str, Enum):
    """Hauptkategorien der Motorsymptome."""
    STARTET_NICHT = "startet_nicht"
    UEBERHITZUNG = "ueberhitzung"
    RAUCH = "rauch"
    OELDRUCK = "oeldruck"
    VIBRATION = "vibration"
    LEISTUNGSVERLUST = "leistungsverlust"
    KRAFTSTOFF = "kraftstoff"
    ELEKTRIK = "elektrik"
    OELVERLUST = "oelverlust"
    GERAEUSCH = "geraeusch"
    NOTFALL = "notfall"


class RauchFarbe(str, Enum):
    """Auspuff-Rauchfarben für Diagnose."""
    SCHWARZ = "schwarz"
    WEISS = "weiss"
    BLAU = "blau"
    GRAU = "grau"
    KEIN = "kein"


class SchweregradeEnum(str, Enum):
    """Schweregrade der Diagnose-Befunde."""
    KRITISCH = "kritisch"
    HOCH = "hoch"
    MITTEL = "mittel"
    NIEDRIG = "niedrig"
    INFO = "info"


class KonfidenzLevel(str, Enum):
    """Konfidenz-Stufen für Diagnose-Ergebnisse."""
    MEASURED = "measured"
    CALCULATED = "calculated"
    VISUAL_HIGH = "visual_high"
    VISUAL_MEDIUM = "visual_medium"
    VISUAL_LOW = "visual_low"
    VISUAL_INSUFFICIENT = "visual_insufficient"
    ESTIMATED = "estimated"
    BENCHMARK = "benchmark"
    DOCUMENTED = "documented"


class MotorTyp(str, Enum):
    """Motortypen für die Diagnose."""
    SAUGDIESEL_INDIREKT = "saugdiesel_indirekt"
    SAUGDIESEL_DIREKT = "saugdiesel_direkt"
    TURBODIESEL = "turbodiesel"
    COMMON_RAIL = "common_rail"


class DiagnoseStatus(str, Enum):
    """Status einer Diagnose-Sitzung."""
    OFFEN = "offen"
    IN_ARBEIT = "in_arbeit"
    ABGESCHLOSSEN = "abgeschlossen"
    ESKALIERT = "eskaliert"
```

### ANHANG J: Symptom- und Befundmodelle

```python
class Symptom(BaseModel):
    """Einzelnes beobachtetes Symptom."""

    model_config = {"from_attributes": True}

    id: str = Field(..., description="Eindeutige Symptom-ID")
    kategorie: SymptomKategorie
    beschreibung: str = Field(
        ...,
        min_length=10,
        max_length=1000,
        description="Detaillierte Symptom-Beschreibung",
    )
    betriebszustand: str = Field(
        ...,
        description="Betriebszustand bei Auftreten (Leerlauf, Teillast, Volllast, Kaltstart etc.)",
    )
    seit_wann: Optional[str] = Field(
        None,
        description="Seit wann das Symptom besteht",
    )
    intermittierend: bool = Field(
        False,
        description="Tritt das Symptom nur zeitweise auf?",
    )
    rauch_farbe: Optional[RauchFarbe] = None
    temperatur_celsius: Optional[float] = Field(
        None, ge=-20, le=200,
        description="Motortemperatur bei Symptom",
    )
    drehzahl_umin: Optional[int] = Field(
        None, ge=0, le=6000,
        description="Motordrehzahl bei Symptom",
    )
    oeldruck_bar: Optional[float] = Field(
        None, ge=0, le=10,
        description="Öldruck bei Symptom",
    )
    begleit_symptome: list[str] = Field(
        default_factory=list,
        description="Zusätzlich beobachtete Symptome",
    )


class DiagnoseBefund(BaseModel):
    """Einzelner Diagnose-Befund (Feststellung)."""

    model_config = {"from_attributes": True}

    id: str = Field(..., description="Eindeutige Befund-ID")
    symptom_ids: list[str] = Field(
        ...,
        description="IDs der zugeordneten Symptome",
    )
    ursache: str = Field(
        ...,
        description="Identifizierte oder vermutete Ursache",
    )
    schweregrad: SchweregradeEnum
    konfidenz: KonfidenzLevel
    konfidenz_prozent: float = Field(
        ..., ge=0, le=100,
        description="Konfidenz in Prozent",
    )
    diagnose_pfad: list[str] = Field(
        default_factory=list,
        description="Schritte der durchgeführten Diagnose",
    )
    messwerte: dict[str, float] = Field(
        default_factory=dict,
        description="Gemessene Werte (Schlüssel: Bezeichnung, Wert: Messwert)",
    )
    empfohlene_massnahme: str = Field(
        ...,
        description="Empfohlene Behebungsmaßnahme",
    )
    geschaetzte_kosten_eur: Optional[float] = Field(
        None, ge=0,
        description="Geschätzte Reparaturkosten in EUR",
    )
    prioritaet: int = Field(
        ..., ge=1, le=10,
        description="Reparatur-Priorität (1=sofort, 10=kann warten)",
    )
    warnung: Optional[str] = Field(
        None,
        description="Sicherheitswarnung falls zutreffend",
    )
```

### ANHANG K: Kompressionstest-Modelle

```python
class KompressionMessung(BaseModel):
    """Kompressionsmessung eines einzelnen Zylinders."""

    model_config = {"from_attributes": True}

    zylinder_nr: int = Field(..., ge=1, le=8)
    druck_bar_trocken: float = Field(
        ..., ge=0, le=50,
        description="Kompressionsdruck trocken in bar",
    )
    druck_bar_nass: Optional[float] = Field(
        None, ge=0, le=50,
        description="Kompressionsdruck nass in bar (nach Öl-Zugabe)",
    )
    leckage_rate_prozent: Optional[float] = Field(
        None, ge=0, le=100,
        description="Leckage-Rate beim Cylinder-Leak-Down-Test",
    )
    leckage_austritt: Optional[str] = Field(
        None,
        description="Wo tritt die Leckage aus? (Ansaugung/Auspuff/Öleinfüllung/Kühlmittel)",
    )


class KompressionTestErgebnis(BaseModel):
    """Ergebnis eines vollständigen Kompressionstests."""

    model_config = {"from_attributes": True}

    motor_id: str
    motor_typ: str
    betriebsstunden: int = Field(..., ge=0)
    motor_temperatur_celsius: float = Field(
        ..., ge=15, le=120,
        description="Motortemperatur bei Test",
    )
    batteriespannung_v: float = Field(
        ..., ge=8, le=30,
    )
    messungen: list[KompressionMessung]
    soll_druck_bar: float = Field(
        ..., ge=15, le=50,
        description="Soll-Kompressionsdruck laut Hersteller",
    )
    min_druck_bar: float = Field(
        ..., ge=10, le=40,
        description="Mindest-Kompressionsdruck laut Hersteller",
    )
    max_differenz_prozent: float = Field(
        ..., ge=0, le=100,
        description="Maximale Differenz zwischen Zylindern in Prozent",
    )
    bewertung: str = Field(
        ...,
        description="Gesamtbewertung des Kompressionszustands",
    )
    empfehlung: str
    konfidenz: KonfidenzLevel = KonfidenzLevel.MEASURED
    gemessen_am: datetime
```

### ANHANG L: Ölanalyse-Modelle

```python
class OelAnalyseMetalle(BaseModel):
    """Verschleißmetall-Werte aus der Ölanalyse."""

    model_config = {"from_attributes": True}

    eisen_fe_ppm: float = Field(..., ge=0, description="Eisen (Zylinder, Nockenwelle)")
    kupfer_cu_ppm: float = Field(..., ge=0, description="Kupfer (Lager, Ölkühler)")
    blei_pb_ppm: float = Field(..., ge=0, description="Blei (Lager)")
    zinn_sn_ppm: float = Field(..., ge=0, description="Zinn (Lager-Overlay)")
    aluminium_al_ppm: float = Field(..., ge=0, description="Aluminium (Kolben)")
    chrom_cr_ppm: float = Field(..., ge=0, description="Chrom (Kolbenringe)")
    silizium_si_ppm: float = Field(..., ge=0, description="Silizium (Staub/Filter)")
    nickel_ni_ppm: float = Field(0, ge=0, description="Nickel (Ventile)")
    molybdaen_mo_ppm: float = Field(0, ge=0, description="Molybdän (Ringe, Additiv)")
    natrium_na_ppm: float = Field(0, ge=0, description="Natrium (Kühlmittel, Additiv)")
    kalzium_ca_ppm: float = Field(0, ge=0, description="Kalzium (Additiv)")
    zink_zn_ppm: float = Field(0, ge=0, description="Zink (Additiv)")
    phosphor_p_ppm: float = Field(0, ge=0, description="Phosphor (Additiv)")


class OelAnalyseKontaminanten(BaseModel):
    """Kontaminanten im Motoröl."""

    model_config = {"from_attributes": True}

    wasser_prozent: float = Field(..., ge=0, le=10)
    kraftstoff_prozent: float = Field(..., ge=0, le=20)
    russ_prozent: float = Field(..., ge=0, le=10)
    glykol_nachgewiesen: bool = Field(False)
    saeurezahl_tan: float = Field(..., ge=0, le=15, description="mg KOH/g")
    basenzahl_tbn: float = Field(..., ge=0, le=20, description="mg KOH/g")
    viskositaet_40c_cst: Optional[float] = Field(None, ge=0, le=500)
    viskositaet_100c_cst: Optional[float] = Field(None, ge=0, le=50)


class OelAnalyseErgebnis(BaseModel):
    """Vollständiges Ölanalyse-Ergebnis."""

    model_config = {"from_attributes": True}

    motor_id: str
    motor_typ: str
    betriebsstunden_gesamt: int = Field(..., ge=0)
    betriebsstunden_seit_oelwechsel: int = Field(..., ge=0)
    oel_typ: str = Field(..., description="Verwendetes Öl (SAE, API)")
    metalle: OelAnalyseMetalle
    kontaminanten: OelAnalyseKontaminanten
    bewertung: str
    empfehlung: str
    trend_hinweis: Optional[str] = None
    konfidenz: KonfidenzLevel = KonfidenzLevel.MEASURED
    labor: str = Field(..., description="Name des Analyselabors")
    proben_datum: datetime
    analyse_datum: datetime
```

### ANHANG M: Fehlercode-Modelle

```python
class FehlerCode(BaseModel):
    """Ein einzelner DTC (Diagnostic Trouble Code)."""

    model_config = {"from_attributes": True}

    code: str = Field(
        ...,
        pattern=r"^(P|MID)\d",
        description="DTC im Format P0xxx oder MID xxx-xxx",
    )
    beschreibung: str
    schweregrad: SchweregradeEnum
    system: str = Field(
        ...,
        description="Betroffenes System (Motor, Getriebe, EVC etc.)",
    )
    sofort_massnahme: str = Field(
        ...,
        description="Empfohlene Sofortmaßnahme",
    )
    notlauf_einschraenkung: Optional[str] = Field(
        None,
        description="Einschränkung im Notlauf-Modus",
    )
    hersteller: str = Field(
        ...,
        description="Motor-Hersteller (yanmar, volvo, universal)",
    )


class FehlerCodeListe(BaseModel):
    """Liste ausgelesener Fehlercodes."""

    model_config = {"from_attributes": True}

    motor_id: str
    diagnosegeraet: str
    ausgelesen_am: datetime
    codes: list[FehlerCode]
    aktive_codes: int = Field(..., ge=0)
    gespeicherte_codes: int = Field(..., ge=0)
    notlauf_aktiv: bool = False
    empfehlung: str
```

### ANHANG N: Troubleshooting-Sitzungs-Modelle

```python
class TroubleshootingSchritt(BaseModel):
    """Einzelner Schritt in der Fehlersuche."""

    model_config = {"from_attributes": True}

    schritt_nr: int = Field(..., ge=1)
    aktion: str = Field(
        ...,
        description="Durchgeführte Prüfung/Aktion",
    )
    ergebnis: str = Field(
        ...,
        description="Beobachtetes Ergebnis",
    )
    messwert: Optional[float] = None
    messwert_einheit: Optional[str] = None
    bewertung: str = Field(
        ...,
        description="OK / Auffällig / Defekt",
    )
    naechster_schritt: Optional[str] = None
    zeitstempel: datetime


class TroubleshootingSitzung(BaseModel):
    """Vollständige Troubleshooting-Sitzung."""

    model_config = {"from_attributes": True}

    id: str
    motor_id: str
    boot_name: Optional[str] = None
    motor_typ: str
    motor_hersteller: str
    betriebsstunden: int = Field(..., ge=0)
    status: DiagnoseStatus
    symptome: list[Symptom]
    schritte: list[TroubleshootingSchritt]
    befunde: list[DiagnoseBefund]
    gesamtbewertung: Optional[str] = None
    gesamtkosten_geschaetzt_eur: Optional[float] = Field(None, ge=0)
    begonnen_am: datetime
    abgeschlossen_am: Optional[datetime] = None
    bearbeiter: Optional[str] = None
```

### ANHANG O: Notfall-Modelle

```python
class NotfallMassnahme(BaseModel):
    """Notfall-Maßnahme auf See."""

    model_config = {"from_attributes": True}

    id: str
    symptom: str = Field(
        ...,
        description="Auslösendes Symptom",
    )
    prioritaet: int = Field(
        ..., ge=1, le=5,
        description="1=Lebensgefahr, 5=Komfort",
    )
    sofort_massnahme: str = Field(
        ...,
        description="Sofort durchzuführende Maßnahme",
    )
    werkzeug_benoetigt: list[str] = Field(
        default_factory=list,
    )
    ersatzteil_benoetigt: list[str] = Field(
        default_factory=list,
    )
    geschaetzte_dauer_minuten: int = Field(..., ge=1)
    sicherheitshinweis: Optional[str] = None
    kann_unter_fahrt: bool = Field(
        False,
        description="Kann die Maßnahme bei Fahrt durchgeführt werden?",
    )
    alternatives_vorgehen: Optional[str] = None


class NotfallAusruestung(BaseModel):
    """Empfohlene Notfall-Ausrüstung für den Motorbereich."""

    model_config = {"from_attributes": True}

    teil: str
    menge: int = Field(..., ge=1)
    einsatzbereich: str
    kosten_eur: float = Field(..., ge=0)
    prioritaet: str = Field(
        ...,
        description="Pflicht / Empfohlen / Optional",
    )
    haltbarkeit_jahre: Optional[int] = None
```

### ANHANG P: Kühlsystem-Diagnose-Modelle

```python
class KuehlsystemDiagnose(BaseModel):
    """Diagnose-Ergebnis für das Kühlsystem."""

    model_config = {"from_attributes": True}

    motor_id: str
    kuehlsystem_typ: str = Field(
        ...,
        description="Zweikreis / Einkreis",
    )
    seewasser_durchfluss: str = Field(
        ...,
        description="Normal / Reduziert / Kein Durchfluss",
    )
    seeventil_offen: bool
    seewasserfilter_zustand: str
    impeller_zustand: str
    impeller_fluegel_komplett: bool
    thermostat_funktion: str = Field(
        ...,
        description="OK / Klemmt offen / Klemmt geschlossen / Nicht geprüft",
    )
    thermostat_oeffnungstemperatur_celsius: Optional[float] = None
    waermetauscher_zustand: str
    kuehlmittel_temperatur_celsius: float
    kuehlmittel_farbe: str
    kuehlmittel_stand: str = Field(
        ...,
        description="OK / Niedrig / Leer",
    )
    co2_test_ergebnis: Optional[str] = Field(
        None,
        description="Negativ / Positiv / Nicht durchgeführt",
    )
    drucktest_bar: Optional[float] = None
    drucktest_ergebnis: Optional[str] = None
    diagnose: str
    empfehlung: str
    konfidenz: KonfidenzLevel
```

### ANHANG Q: Rauchdiagnose-Modelle

```python
class RauchDiagnose(BaseModel):
    """Diagnose basierend auf Rauchfarbe und Betriebszustand."""

    model_config = {"from_attributes": True}

    rauch_farbe: RauchFarbe
    rauch_dichte: str = Field(
        ...,
        description="Leicht / Mittel / Stark",
    )
    rauch_geruch: Optional[str] = Field(
        None,
        description="Diesel / Süßlich / Beißend / Verbrannt",
    )
    betriebszustand: str = Field(
        ...,
        description="Kaltstart / Leerlauf / Teillast / Volllast / Beschleunigung",
    )
    motor_temperatur_celsius: float
    verschwindet_nach_warmfahren: Optional[bool] = None
    kuehlmittelstand_sinkt: Optional[bool] = None
    oelverbrauch_erhoeht: Optional[bool] = None
    diagnose: str = Field(
        ...,
        description="Wahrscheinlichste Ursache",
    )
    differenzial_diagnosen: list[str] = Field(
        default_factory=list,
        description="Alternative mögliche Ursachen",
    )
    empfohlene_pruefung: list[str] = Field(
        default_factory=list,
        description="Empfohlene weiterführende Prüfungen",
    )
    schweregrad: SchweregradeEnum
    konfidenz: KonfidenzLevel
```

### ANHANG R: Gesamt-Troubleshooting-Analyse-Modell

```python
class MotorTroubleshootingAnalyse(BaseModel):
    """Vollständiges Troubleshooting-Analyse-Ergebnis für AYDI-Integration."""

    model_config = {"from_attributes": True}

    # Identifikation
    analyse_id: str
    boot_id: str
    motor_id: str
    motor_hersteller: str
    motor_modell: str
    motor_typ: MotorTyp
    betriebsstunden: int = Field(..., ge=0)

    # Sitzung
    sitzung: TroubleshootingSitzung

    # Spezifische Diagnosen
    kompressionstest: Optional[KompressionTestErgebnis] = None
    oelanalyse: Optional[OelAnalyseErgebnis] = None
    kuehlsystem: Optional[KuehlsystemDiagnose] = None
    rauchdiagnose: Optional[RauchDiagnose] = None
    fehlercodes: Optional[FehlerCodeListe] = None

    # Ergebnis
    hauptbefunde: list[DiagnoseBefund]
    notfall_massnahmen: list[NotfallMassnahme] = Field(default_factory=list)
    gesamtbewertung: str
    dringlichkeit: SchweregradeEnum
    geschaetzte_gesamtkosten_eur: Optional[float] = Field(None, ge=0)

    # Meta
    konfidenz: KonfidenzLevel
    konfidenz_prozent: float = Field(..., ge=0, le=100)
    analyse_version: str = "2.0"
    erstellt_am: datetime
    hinweis: str = Field(
        default="Diagnose-Ergebnisse sind Empfehlungen. "
        "Kritische Befunde müssen von qualifiziertem "
        "Fachpersonal verifiziert werden.",
    )

    # AYDI-Scoring
    motor_zustand_score: float = Field(
        ..., ge=0, le=100,
        description="Gesamtbewertung Motorzustand (0=Totalschaden, 100=Neuzustand)",
    )
    wartungsdringlichkeit_score: float = Field(
        ..., ge=0, le=100,
        description="Dringlichkeit der Wartung (0=alles OK, 100=sofort handeln)",
    )
```

---

*Dieses Dokument ist Teil der AYDI Maritime Knowledge Base. Alle Angaben
ohne Gewähr. Kritische Diagnosen und Reparaturen sollten stets von
qualifiziertem Fachpersonal durchgeführt oder verifiziert werden.
Marine-Dieselmotoren arbeiten mit hohen Drücken, hohen Temperaturen
und gefährlichen Stoffen — Sicherheit hat immer Vorrang.*

---
