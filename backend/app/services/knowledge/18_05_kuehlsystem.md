---
titel: "Kühlsysteme — Seewasser, Frischwasser und Wärmetauscher"
kategorie: "Motoren und Antrieb"
unterkategorie: "Kühlsystem"
version: "2.0"
letzte_aktualisierung: "2026-04"
autor: "AYDI Maritime Knowledge Base"
---

# 18_05 — Kühlsysteme — Seewasser, Frischwasser und Wärmetauscher

---

## Inhaltsverzeichnis

1. [Einführung](#1-einführung)
2. [Einkreis-Kühlung (Direktkühlung)](#2-einkreis-kühlung-direktkühlung)
3. [Zweikreis-Kühlung (Indirekte Kühlung)](#3-zweikreis-kühlung-indirekte-kühlung)
4. [Kielkühlung (Geschlossenes System)](#4-kielkühlung-geschlossenes-system)
5. [Seewasserkreislauf](#5-seewasserkreislauf)
6. [Frischwasserkreislauf](#6-frischwasserkreislauf)
7. [Wärmetauscher](#7-wärmetauscher)
8. [Ölkühler](#8-ölkühler)
9. [Ladeluftkühler (Intercooler)](#9-ladeluftkühler-intercooler)
10. [Impeller und Seewasserpumpe](#10-impeller-und-seewasserpumpe)
11. [Mischkrümmer und Auspuffkrümmer](#11-mischkrümmer-und-auspuffkrümmer)
12. [Thermostat](#12-thermostat)
13. [Kühlmittel und Frostschutz](#13-kühlmittel-und-frostschutz)
14. [Seewasserfilter und Seeventile](#14-seewasserfilter-und-seeventile)
15. [Zinkanoden im Kühlsystem](#15-zinkanoden-im-kühlsystem)
16. [Fehlerbild-Atlas](#16-fehlerbild-atlas)
17. [Troubleshooting](#17-troubleshooting)
18. [FAQ](#18-faq)
19. [Glossar](#19-glossar)
20. [Schnell-Referenz](#20-schnell-referenz)
21. [ANHANG A–H: Fallstudien](#21-anhang-ah-fallstudien)
22. [ANHANG I–R: Pydantic v2 Datenmodelle](#22-anhang-ir-pydantic-v2-datenmodelle)

---
---

## 1. Einführung

### 1.1 Warum Motorkühlung auf See kritisch ist

Ein Verbrennungsmotor wandelt nur 35–45 % der im Kraftstoff enthaltenen
Energie in mechanische Arbeit um. Die verbleibenden 55–65 % müssen als
Wärme abgeführt werden — etwa je ein Drittel über Kühlsystem, Abgas
und Strahlung. Auf einem Boot ist die Kühlung eine lebenskritische
Funktion:

- **Überhitzung ist die häufigste Ursache für schwere Motorschäden** an
  Bord. Während ein Auto bei Überhitzung am Straßenrand anhalten kann,
  ist ein Schiff im Hafen-Ansteuerungskanal oder bei schwerer See auf
  einen funktionierenden Motor angewiesen.
- **Seewasser ist gleichzeitig Kühlmedium und Feind.** Salz, Kalk,
  Muscheln, Sand, Tang und Elektrolyse greifen jede Komponente an.
- **Plastiktüten, Tang und Quallen** können einen Seewassereinlass in
  Sekunden blockieren und den Motor in Minuten überhitzen.
- **Mischkrümmer-Versagen** ist eine der teuersten und gefährlichsten
  Fehlerquellen — korrodiertes Metall lässt Seewasser in die Zylinder
  laufen (Hydrolock → Motorschaden oder Sinken).

**Statistik (ADAC/BoatUS 2024):**
- 22 % aller Motorausfälle auf See → Kühlsystem
- 35 % aller Liegenbleiber im Sommer → Überhitzung
- Durchschnittliche Reparaturkosten Kühlsystem: 800–4.500 EUR
- Motorschaden durch Überhitzung: 8.000–35.000 EUR
- Mischkrümmer-Versagen mit Wassereinbruch: 12.000–45.000 EUR

### 1.2 Grundprinzip: Wärme muss raus

Jeder Marine-Diesel erzeugt Wärme, die abgeführt werden muss:

| Motorleistung | Abzuführende Wärme | Seewasser-Durchfluss | Frischwasser-Durchfluss |
|:---:|:---:|:---:|:---:|
| 10 PS / 7,5 kW | ~5 kW | ~8 l/min | ~12 l/min |
| 30 PS / 22 kW | ~15 kW | ~25 l/min | ~35 l/min |
| 50 PS / 37 kW | ~25 kW | ~40 l/min | ~55 l/min |
| 100 PS / 74 kW | ~50 kW | ~80 l/min | ~110 l/min |
| 200 PS / 147 kW | ~100 kW | ~160 l/min | ~220 l/min |
| 400 PS / 294 kW | ~200 kW | ~320 l/min | ~440 l/min |

**Faustregel:** Pro kW Motorleistung müssen ca. 0,7 kW Wärme über das
Kühlwasser abgeführt werden. Der Seewasser-Durchfluss beträgt etwa
1–1,2 l/min pro PS.

### 1.3 Die drei Kühlkonzepte im Überblick

| Konzept | Prinzip | Einsatz | Vorteil | Nachteil |
|---------|---------|---------|---------|----------|
| Einkreis | Seewasser fließt direkt durch den Motor | Ältere Motoren, einfache Installationen | Einfach, günstig | Korrosion, Kalkaufbau, keine Temperaturregelung |
| Zweikreis | Frischwasser kühlt Motor, Seewasser kühlt Frischwasser über Wärmetauscher | Standard seit 1980er | Kontrollierte Temperatur, korrosionsarm | Komplexer, mehr Komponenten |
| Kielkühlung | Geschlossener Kreislauf, Wärme über Kielkühler an Rumpf/Wasser | Schmutzwasser, Eis, Trawler, Arbeitsboote | Keine Seewasser-Durchführung, wartungsarm | Teuer, braucht Rumpffläche, ggf. zusätzlicher Auspuffkühler nötig |

### 1.4 Kühlsystem-Ausfälle nach Statistik

**Häufigste Kühlsystem-Probleme (ADAC-Sportschifffahrt-Statistik 2024,
n=4.200 Motorausfälle):**

| Rang | Problem | Anteil | Durchschnittliche Kosten (EUR) |
|:---:|---------|:---:|:---:|
| 1 | Impeller-Versagen | 35 % | 180 (Reparatur) – 5.000 (Folgeschaden) |
| 2 | Seewasserfilter verstopft | 20 % | 0–50 |
| 3 | Wärmetauscher verkalkt | 12 % | 200–800 |
| 4 | Mischkrümmer korrodiert | 10 % | 800–35.000 |
| 5 | Thermostat defekt | 8 % | 80–300 |
| 6 | Schlauch geplatzt | 6 % | 50–200 |
| 7 | Kühlmittelverlust | 5 % | 50–500 |
| 8 | Sonstige (Pumpe, Zinkanode, Elektrolyse) | 4 % | variabel |

**Saisonale Verteilung:**
- 55 % aller Kühlsystem-Ausfälle: Juni–August (Hochsaison,
  warmes Wasser, hohe Belastung).
- 25 % aller Kühlsystem-Ausfälle: April–Mai (Saisonstart,
  Winterschäden, vergessene Wartung).
- 15 % aller Kühlsystem-Ausfälle: September–Oktober.
- 5 % aller Kühlsystem-Ausfälle: November–März (Winterlager,
  Frostschäden).

**Altersverteilung der betroffenen Motoren:**
- 0–5 Jahre: 15 % (meist Impeller, Bedienfehler).
- 5–10 Jahre: 25 % (Impeller, Thermostat, beginnende Krümmer-Korrosion).
- 10–15 Jahre: 30 % (Krümmer, Wärmetauscher, Schläuche).
- 15–25 Jahre: 25 % (alle Komponenten, Grundüberholung nötig).
- >25 Jahre: 5 % (Einkreis-Motoren, Blockkorrosion).

### 1.5 Betriebstemperaturen

| Parameter | Einkreis | Zweikreis | Kielkühlung |
|-----------|:---:|:---:|:---:|
| Motorblock-Temperatur | 50–65 °C | 80–95 °C | 80–95 °C |
| Thermostat-Öffnung | Meist keiner | 71–88 °C (je Hersteller) | 71–88 °C |
| Max. Betriebstemperatur | 65 °C | 95–100 °C | 95–100 °C |
| Alarm-Temperatur | 70 °C | 100–107 °C | 100–107 °C |
| Abschalttemperatur | 75 °C | 107–115 °C | 107–115 °C |
| Seewasser-Austritt am Auspuff | 40–55 °C | 45–65 °C | – (kein Seewasser) |

**Warum Einkreis kälter läuft:** Ohne Thermostat und direkt vom
Seewasser (8–25 °C) gekühlt, wird der Motor auf nur 50–65 °C gehalten.
Das ist zu kalt für optimale Verbrennung → Verglasung, Kondensation,
schlechte Kraftstoffverbrennung, erhöhter Verschleiß.

---
---

## 2. Einkreis-Kühlung (Direktkühlung)

### 2.1 Funktionsprinzip

Bei der Einkreis-Kühlung (englisch: "raw water cooling" oder "direct
cooling") fließt das Seewasser direkt durch den Motorblock und den
Zylinderkopf. Das Wasser nimmt die Wärme auf und wird zusammen mit
den Abgasen über den Auspuff ausgestoßen.

**Kreislauf:**
```
Seeventil → Seewasserfilter → Impeller-Pumpe → Motorblock →
Zylinderkopf → Mischkrümmer/Auspuff → Austritt über Wasserline
```

### 2.2 Typische Einkreis-Motoren

| Motor | Leistung | Baujahr | Bemerkung |
|-------|:---:|:---:|-----------|
| Volvo Penta MD2B | 25 PS | 1968–1983 | Sehr verbreitet in älteren Segelbooten |
| Volvo Penta MD11/MD17 | 23/36 PS | 1975–1990 | Robuste Motoren, oft noch im Einsatz |
| BMC 1.5/1.8 | 30/42 PS | 1970–1985 | Häufig in britischen Booten |
| Bukh DV10/DV20 | 10/20 PS | 1980–2000 | Dänische Kompaktmotoren |
| Perkins 4.108 | 47 PS | 1965–1990 | Klassiker in Motorbooten |
| Farymann A30 | 12 PS | 1970–1995 | Deutsche Einzylinder-Motoren |
| Yanmar YSM8/YSM12 | 8/12 PS | 1977–1993 | Sehr zuverlässig, aber direkt gekühlt |

### 2.3 Probleme der Einkreis-Kühlung

**Kalkbildung:**
- Seewasser enthält ca. 35 g/l Salz und variable Mengen Kalk (CaCO₃).
- Ab 60 °C beginnt Kalk auszufallen und setzt sich an Kühlkanälen ab.
- Nach 5–10 Jahren können Kühlkanäle zu 50–70 % zugesetzt sein.
- Folge: Ungleichmäßige Kühlung → Hot Spots → Zylinderkopfrisse.

**Korrosion:**
- Seewasser ist hoch korrosiv (Chlorid-Ionen, Sauerstoff, Temperatur).
- Gusseisen-Motorblöcke werden von innen angegriffen.
- Galvanische Korrosion zwischen verschiedenen Metallen (Block, Pumpe,
  Leitungen).
- Typische Lebensdauer eines Einkreis-Motorblocks: 15–25 Jahre,
  danach oft Kühlkanaldurchbrüche.

**Keine Temperaturregelung:**
- Ohne Thermostat läuft der Motor zu kalt (Seewassertemperatur + 20–40 °C).
- Im Winter bei 5 °C Wassertemperatur: Motor bei nur 25–45 °C.
- Zu kalter Motor: schlechte Verbrennung, Verglasung, Kondensation,
  saures Kondenswasser frisst Laufbuchsen an.

**Bewuchsprobleme:**
- In warmem Wasser können Algen und Muscheln im Kühlkanal wachsen.
- Besonders problematisch in Liegehäfen der Mittelmeerküste.

### 2.4 Umrüstung Einkreis → Zweikreis

Für viele ältere Motoren sind Nachrüst-Kits verfügbar:

| Motor | Kit-Hersteller | Preis (EUR) | Enthaltene Teile |
|-------|:---:|:---:|-----------------|
| Volvo MD2B | Bowman | 1.200–1.500 | Wärmetauscher, Thermostatgehäuse, Schläuche |
| Volvo MD11 | Bowman | 1.300–1.600 | Wärmetauscher, Ausgleichsbehälter, Thermostat |
| Perkins 4.108 | Bowman | 1.400–1.800 | Wärmetauscher, alle Anschlüsse |
| Bukh DV20 | Vetus | 1.100–1.400 | Wärmetauscher, Leitungen |
| BMC 1.5 | Bowman | 1.300–1.700 | Komplett-Kit |

**Einbauzeit:** 6–12 Stunden (Fachbetrieb).
**Empfehlung:** Beim nächsten Wärmetauschertausch oder größerem
Service sollte jeder Einkreis-Motor auf Zweikreis umgerüstet werden.

### 2.5 Winterfestmachung Einkreis

Da Seewasser direkt im Motorblock steht, ist Winterfestmachung
existenziell:

1. Motor warmlaufen lassen (5 min).
2. Seeventil schließen.
3. Seewasser-Einlassschlauch in Eimer mit Frostschutzmittel
   (Propylenglykol, nicht Ethylenglykol → umweltgefährlich!).
4. Motor starten und laufen lassen, bis Frostschutz aus Auspuff kommt
   (rosa/grüne Farbe sichtbar).
5. Motor abstellen. Seeventil bleibt geschlossen.
6. Alle Ablass-Hähne öffnen (Motorblock, Auspuffkrümmer, Wasserfilter).
7. Impeller ausbauen (verhindert Verformung über Winter).

**KRITISCH:** Wird die Winterfestmachung vergessen und Frost tritt ein,
platzt der Motorblock. Kosten: Totalschaden (8.000–30.000 EUR).

---
---

## 3. Zweikreis-Kühlung (Indirekte Kühlung)

### 3.1 Funktionsprinzip

Die Zweikreis-Kühlung (englisch: "indirect cooling", "heat exchanger
cooling", "freshwater cooling") trennt Seewasser und Motorkühlwasser
in zwei separate Kreisläufe, die über einen Wärmetauscher thermisch
gekoppelt sind.

**Kreislauf 1 — Frischwasser (geschlossen):**
```
Frischwasserpumpe (am Motor) → Motorblock → Zylinderkopf →
Thermostat → Wärmetauscher (warme Seite) → zurück zur Pumpe
```

**Kreislauf 2 — Seewasser (offen):**
```
Seeventil → Seewasserfilter → Impeller-Pumpe → Wärmetauscher
(kalte Seite) → Ölkühler → ggf. Ladeluftkühler →
Mischkrümmer/Auspuff → Austritt
```

### 3.2 Vorteile gegenüber Einkreis

| Vorteil | Erläuterung |
|---------|-------------|
| Kontrollierte Motortemperatur | Thermostat hält 80–88 °C → optimale Verbrennung |
| Kein Kalk im Motor | Frischwasser + Kühlmittel = kalkfrei |
| Weniger Korrosion im Motor | Inhibiertes Kühlmittel schützt Metalloberflächen |
| Längere Motorlebensdauer | 30–50 % längere Lebensdauer als Einkreis |
| Besserer Wirkungsgrad | Höhere Betriebstemperatur = bessere Verbrennung |
| Einfachere Winterfestmachung | Frischwasserkreislauf mit Frostschutz, nur Seewasserkreislauf entwässern |
| Heizungsanschluss möglich | Frischwasserkreislauf kann Kabinenheizung versorgen |

### 3.3 Komponenten des Zweikreis-Systems

#### 3.3.1 Frischwasserkreislauf

| Komponente | Funktion | Lebensdauer | Austauschintervall |
|-----------|----------|:-----------:|:------------------:|
| Frischwasserpumpe | Umwälzung des Kühlmittels | Motorlebensdauer | Gleitringdichtung alle 3.000–5.000 h |
| Thermostat | Temperaturregelung | 3–5 Jahre | Alle 3–5 Jahre oder bei Fehlfunktion |
| Wärmetauscher | Wärmeübertragung FW→SW | 8–15 Jahre | Bei nachlassender Leistung |
| Ausgleichsbehälter | Volumenausgleich, Entlüftung | Motorlebensdauer | Verschlussdeckel alle 5 Jahre |
| Kühlmittelschläuche | Verbindung der Komponenten | 5–8 Jahre | Alle 5–8 Jahre oder bei Rissen |
| Kühlmittel | Frost-/Korrosionsschutz | 2–5 Jahre | OAT alle 5 Jahre, IAT alle 2 Jahre |

#### 3.3.2 Seewasserkreislauf

| Komponente | Funktion | Lebensdauer | Austauschintervall |
|-----------|----------|:-----------:|:------------------:|
| Seeventil (Seacock) | Seewasser-Absperrung | 10–25 Jahre | Jährlich kontrollieren, alle 15 Jahre |
| Seewasserfilter (Strainer) | Filtert Schmutz, Tang, Partikel | 10–20 Jahre | Sieb regelmäßig reinigen |
| Impeller-Pumpe | Seewasser-Förderung | Gehäuse: 15+ Jahre | Impeller: jährlich/500 h |
| Seewasserschläuche | Verbindung der Komponenten | 5–10 Jahre | Alle 5–8 Jahre |
| Mischkrümmer | Seewasser-Einspritzung in Abgas | 5–15 Jahre | Inspektion jährlich, Austausch 5–12 Jahre |
| Zinkanode(n) | Korrosionsschutz | 6–12 Monate | Halbjährlich kontrollieren |

### 3.4 Typische Betriebsparameter

| Parameter | Sollwert | Alarmwert | Abschaltung |
|-----------|:--------:|:---------:|:-----------:|
| Motortemperatur (Frischwasser) | 80–88 °C | 100–107 °C | 107–115 °C |
| Seewasser-Austrittstemperatur | 45–60 °C | 70 °C | – |
| Systemdruck (Frischwasser) | 0,8–1,2 bar | >1,5 bar | >2,0 bar |
| Seewasser-Durchfluss | 1,0–1,2 l/min/PS | <0,7 l/min/PS | <0,5 l/min/PS |
| Kühlmittel-Füllstand | Ausgleichsbehälter ½–¾ voll | Sichtbar niedrig | Min-Markierung |
| Kühlmittel-Konzentration | 33–50 % Glykol | <25 % | <20 % |

### 3.5 Hersteller-spezifische Systeme

#### Yanmar (z.B. 3JH, 4JH-Serie)
- Thermostat: 76 °C Öffnung, 87 °C voll offen
- Kühlmittel: Yanmar Genuine Coolant oder gleichwertiges OAT
- Wärmetauscher: Kupfer-Nickel-Rohrbündel
- Impeller: Jabsco Profil, 10 Flügel
- Ölkühler: integriert im Wärmetauscher-Gehäuse
- Zinkanode: 1× im Wärmetauscher (M8-Gewinde)

#### Volvo Penta (z.B. D1, D2-Serie)
- Thermostat: 82 °C Öffnung, 93 °C voll offen
- Kühlmittel: Volvo Penta Coolant (OAT-basiert, grün)
- Wärmetauscher: Kupfer-Zinn-Rohrbündel
- Impeller: Johnson/Jabsco, 8–12 Flügel je Modell
- Ölkühler: separates Gehäuse am Motorblock
- Zinkanode: 1× im Wärmetauscher + 1× im Ölkühler

#### Nanni Diesel (z.B. N4.38, N4.50)
- Thermostat: 76 °C Öffnung
- Kühlmittel: Standard-OAT, 33 % Mischung
- Wärmetauscher: Kupfer-Nickel (Bowman-Zulieferung)
- Impeller: Jabsco-kompatibel
- Ölkühler: Plattenwärmetauscher

#### Mercruiser / Mercury Diesel (z.B. CMD 2.8 EI)
- Thermostat: 71 °C (160 °F)
- Kühlmittel: Mercury Extended Life Coolant
- Wärmetauscher: Kupfer-Nickel oder Aluminium-Seewasser
- Impeller: Sherwood-Typ
- Besonderheit: Oft Aluminium-Seewasserkomponenten → höhere
  Korrosionsanfälligkeit, Zinkanoden kritisch

### 3.6 Winterfestmachung Zweikreis

**Frischwasserkreislauf:**
1. Kühlmittel-Konzentration prüfen (Refraktometer). Soll: ≥33 % Glykol.
2. Falls <33 %: Kühlmittel ablassen und mit korrekter Mischung
   nachfüllen (50:50 für Frostschutz bis −36 °C).
3. Fertig — der Frischwasserkreislauf ist durch das Kühlmittel
   frostgeschützt.

**Seewasserkreislauf:**
1. Motor warmlaufen lassen.
2. Seeventil schließen.
3. Seewasser-Einlassschlauch in Eimer mit Propylenglykol-Frostschutz
   (ungiftig, lebensmitteltauglich).
4. Motor starten, laufen lassen bis Frostschutz aus Auspuff kommt.
5. Motor abstellen.
6. Impeller ausbauen (empfohlen, verhindert Verformung).
7. Seewasserfilter entleeren.

---
---

## 4. Kielkühlung (Geschlossenes System)

### 4.1 Funktionsprinzip

Bei der Kielkühlung (englisch: "keel cooling", "skin cooling",
"box cooling") wird die Motorwärme über einen am Rumpfaußenhautteil
angebrachten Kühler direkt an das umgebende Wasser abgegeben. Es gibt
keinen offenen Seewasserkreislauf — das System ist vollständig
geschlossen.

**Kreislauf:**
```
Frischwasserpumpe → Motorblock → Zylinderkopf → Thermostat →
Kielkühler (außen am Rumpf) → zurück zur Pumpe
```

**Kein Seewasser im Boot.** Kein Seeventil nötig (für Kühlung), kein
Impeller, kein Seewasserfilter, kein Mischkrümmer.

### 4.2 Arten von Kielkühlern

#### 4.2.1 Rohrkühler (Grid Cooler / Pipe Cooler)

- Kupfer-Nickel-Rohre (CuNi 90/10) werden am Rumpf unter der
  Wasserlinie montiert.
- Typisch: Gitteranordnung, 6–20 Rohre je Kühler.
- Hersteller: Fernstrum (USA, Marktführer), Duramax Marine.
- Vorteil: Einfach, robust, gut geschützt wenn in Kimmung montiert.
- Nachteil: Erhöhter Rumpfwiderstand, Bewuchsrisiko.

#### 4.2.2 Flachkühler (Box Cooler / Tank Cooler)

- Kupfer-Nickel-Platten oder -Rohrbündel in einem am Rumpf montierten
  Kasten (Sea Chest), der zum Seewasser offen ist.
- Hersteller: Vetus (Boxcooler), Blokland.
- Vorteil: Kein externer Rumpfwiderstand, innerhalb des Bootes montiert.
- Nachteil: Sea Chest muss regelmäßig gereinigt werden, komplexer Einbau.

#### 4.2.3 Rumpfkühler (Skin Tank / Skin Cooler)

- Kühlrohre oder -kanäle werden direkt in den Rumpf integriert (bei
  Stahlbooten geschweißt, bei GFK laminiert).
- Hersteller: Bootsspezifisch, oft Eigenanfertigung.
- Vorteil: Kein externer Widerstand, kein Bewuchs.
- Nachteil: Nicht nachrüstbar, Reparatur aufwändig.

### 4.3 Dimensionierung

Die Kühlerfläche richtet sich nach der abzuführenden Wärmeleistung
und der minimalen Wassertemperatur:

| Motorleistung | Min. Kühlerfläche (Rohr) | Min. Kühlerfläche (Box) | Min. Kühlerfläche (Skin) |
|:---:|:---:|:---:|:---:|
| 10 PS / 7,5 kW | 0,10 m² | 0,08 m² | 0,15 m² |
| 30 PS / 22 kW | 0,30 m² | 0,24 m² | 0,45 m² |
| 50 PS / 37 kW | 0,50 m² | 0,40 m² | 0,75 m² |
| 100 PS / 74 kW | 1,00 m² | 0,80 m² | 1,50 m² |
| 200 PS / 147 kW | 2,00 m² | 1,60 m² | 3,00 m² |

**Faustregel Fernstrum:** 0,014 m² Kühlerfläche pro PS (Rohrkühler).

### 4.4 Hersteller und Preise

| Hersteller | Modell | Motorleistung | Preis (EUR) | Typ |
|-----------|--------|:---:|:---:|-----|
| Fernstrum | Gridcooler GC-1206 | bis 25 PS | 850–1.200 | Rohrgitter |
| Fernstrum | Gridcooler GC-2412 | bis 75 PS | 1.600–2.400 | Rohrgitter |
| Fernstrum | Gridcooler GC-3618 | bis 150 PS | 2.800–4.200 | Rohrgitter |
| Vetus | Boxcooler HTC 3814 | bis 30 PS | 1.100–1.500 | Box/Tank |
| Vetus | Boxcooler HTC 6020 | bis 60 PS | 1.800–2.600 | Box/Tank |
| Vetus | Boxcooler HTC 12630 | bis 200 PS | 3.500–5.000 | Box/Tank |
| Duramax |?"Keel Cooler" DM-2416 | bis 100 PS | 1.400–2.000 | Rohrgitter |

### 4.5 Vor- und Nachteile

**Vorteile:**
- Kein Seewasser im Boot → keine Leckgefahr durch Kühlsystem.
- Kein Impeller → keine Impeller-Ausfälle.
- Kein Seewasserfilter → kein Verstopfen.
- Kein Mischkrümmer → keine Mischkrümmer-Korrosion.
- Keine Zinkanoden im Kühlsystem nötig.
- Ideal für schmutziges/sandiges Wasser, Flussbetrieb, Eisbetrieb.
- Extrem wartungsarm.
- Ideal für Langfahrt in abgelegenen Gebieten.

**Nachteile:**
- Höhere Installationskosten (2.000–8.000 EUR vs. 500–1.500 EUR
  für Standard-Wärmetauscher).
- Erhöhter Rumpfwiderstand (Rohrkühler: 1–3 % Geschwindigkeitsverlust).
- Auspuff braucht separate Kühlung (Trockenauspuff oder separater
  Seewasserkreislauf nur für Auspuff).
- Bewuchsproblem bei Liegezeit (Rohrkühler außen am Rumpf).
- Nicht für Gleiter geeignet (Kühler muss immer unter Wasser sein).
- Nachrüstung erfordert Rumpfarbeiten (Bohrungen, Schweißen).

### 4.6 Auspufflösung bei Kielkühlung

Da kein Seewasser den Auspuff kühlt, gibt es zwei Lösungen:

**Trockenauspuff:**
- Isoliertes Edelstahlrohr, keine Seewasser-Einspritzung.
- Hohe Temperatur (300–500 °C) → muss ausreichend isoliert werden.
- Mindestabstände zu brennbaren Materialien: 150–300 mm ohne Isolierung,
  50–100 mm mit geprüfter Marine-Isolierung.
- Hersteller: Vetus (Silencer NLPH), Halyard Marine.
- Kosten: 800–3.000 EUR komplett.

**Mini-Seewasserkreislauf nur für Auspuff:**
- Kleine Seewasserpumpe (elektrisch oder mechanisch) speist nur den
  Mischkrümmer.
- Vorteil: Leiser Nassauspuff möglich.
- Nachteil: Braucht trotzdem Seeventil, Filter, Impeller.
- Kompromiss: Eliminiert Seewasser im Motor, aber nicht komplett im Boot.

### 4.7 Wartung Kielkühlung

| Intervall | Maßnahme |
|-----------|----------|
| Jährlich | Kielkühler auf Bewuchs prüfen und reinigen (bei Rohrkühler) |
| Jährlich | Antifouling auf Kielkühler erneuern (kompatibles Antifouling!) |
| 2 Jahre | Kühlmittel prüfen (Refraktometer + pH-Teststreifen) |
| 5 Jahre | Kühlmittel komplett tauschen |
| 5 Jahre | Alle Schläuche und Schellen prüfen |
| 10 Jahre | Kielkühler-Zustand prüfen (Wandstärke, Korrosion) |

**WICHTIG:** Kein kupferhaltiges Antifouling direkt auf CuNi-Kühlerrohre —
es kann galvanische Korrosion beschleunigen. Spezielle Antifoulings
(z.B. Hempel Mille NCT für CuNi) verwenden.

### 4.8 Kielkühlung — Dimensionierung im Detail

Die korrekte Dimensionierung des Kielkühlers ist entscheidend. Zu
klein dimensioniert → Überhitzung bei warmem Wasser oder Volllast. Zu
groß dimensioniert → unnötige Kosten und Rumpfwiderstand.

**Berechnungsformel (Fernstrum):**
```
Q = k × A × ΔT_lm

Q   = abzuführende Wärmeleistung (kW)
k   = Wärmedurchgangskoeffizient (kW/m²·K)
      Rohrkühler: 0,8–1,2 (sauber), 0,5–0,8 (bewachsen)
      Boxkühler: 1,0–1,5 (sauber)
      Skin Cooler: 0,3–0,6
A   = Kühlerfläche (m²)
ΔT_lm = logarithmische mittlere Temperaturdifferenz (K)
```

**Praxis-Sicherheitsfaktor:**
- Gemäßigte Gewässer (Ostsee, Nordsee): Faktor 1,3 auf berechnete Fläche.
- Tropische Gewässer (Karibik, Rotes Meer): Faktor 1,5–1,8 (Seewasser
  bis 32 °C, reduziert ΔT erheblich).
- Kombination mit Trockenauspuff: Kühler muss nur die Motorwärme
  abführen (nicht die Auspuffwärme).

**Typische Installationszeiten:**
| Kühler-Typ | Rumpfmaterial | Installationszeit | Spezialwerkzeug |
|-----------|:---:|:---:|:---:|
| Rohrgitter (Fernstrum) | GFK | 8–16 h | Bohrung, Laminierung |
| Rohrgitter (Fernstrum) | Stahl/Alu | 6–12 h | Schweißgerät |
| Boxkühler (Vetus) | GFK | 12–20 h | Bohrung, Laminierung |
| Boxkühler (Vetus) | Stahl/Alu | 8–16 h | Schweißgerät |
| Skin Cooler | Stahl | 16–30 h | Schweißgerät, Rohrbiegung |

### 4.9 Kielkühlung — Fehlerdiagnose

Da Kielkühlungssysteme im Vergleich zu Zweikreis-Systemen deutlich
weniger Komponenten haben, beschränkt sich die Fehlersuche auf wenige
Punkte:

| Problem | Mögliche Ursache | Diagnose | Lösung |
|---------|------------------|----------|--------|
| Motor überhitzt | Bewuchs am Kühler | Taucher prüfen lassen | Reinigen + Antifouling |
| Motor überhitzt | Thermostat klemmt | Thermostat prüfen (Kochtest) | Thermostat tauschen |
| Motor überhitzt | Frischwasserpumpe defekt | Durchfluss am Rücklauf prüfen | Pumpe/Dichtung tauschen |
| Motor überhitzt | Luftschloss | System entlüften | Entlüftungsschraube öffnen |
| Motor überhitzt | Kühler zu klein (Tropen) | Motortemperatur bei Volllast beobachten | Zusätzlichen Kühler installieren |
| Kühlmittelverlust | Schlauch undicht | Drucktest 1,5 bar | Schlauch tauschen |
| Kühlmittelverlust | Kühler undicht (CuNi) | Drucktest von außen | Kühler reparieren/tauschen |
| Motor wird nicht warm | Thermostat fehlt/klemmt offen | Thermostat prüfen | Thermostat tauschen |

---
---

## 5. Seewasserkreislauf

### 5.1 Übersicht Komponenten

Der Seewasserkreislauf ist der offene Kreislauf, der Seewasser durch
das Boot führt. Jede Komponente ist potenziell eine Fehlerquelle.

**Flussrichtung:**
```
Seeventil (Seacock) → Seewasserfilter (Strainer) →
Impeller-Pumpe (Seawaterpump) → Wärmetauscher (kalte Seite) →
Ölkühler → [ggf. Ladeluftkühler] → Mischkrümmer (Mixing Elbow) →
Auspuffschlauch → Wassersammler (Waterlock) → Austritt
```

### 5.2 Seeventil (Seacock)

Das Seeventil ist die erste Verteidigungslinie gegen Wassereinbruch.
Es muss jederzeit schließbar sein.

**Typen:**

| Typ | Material | Preis (EUR) | Lebensdauer | Empfehlung |
|-----|----------|:---:|:---:|------------|
| Kugelhahn (Ball Valve) | Bronze (DZR) | 45–180 | 10–20 Jahre | Standard, zuverlässig |
| Kükenhahn (Tapered Plug) | Bronze | 80–250 | 15–25 Jahre | Traditionell, sehr robust |
| Kunststoff-Kugelhahn | Marelon® (glasfaserverst. Nylon) | 35–120 | 15–25 Jahre | Keine Korrosion, CE-zugelassen |
| Edelstahl-Kugelhahn | 316L | 60–200 | 10–15 Jahre | Nicht empfohlen (Spaltkorrosion) |

**WARNUNG:** Billige Messing-Kugelhähne (nicht DZR — Dezincification
Resistant) aus dem Sanitärhandel sind im Seewasser lebensgefährlich.
Messing-Entzinkung führt zu sprödem Material → Bruch → Wassereinbruch
→ Sinken. Nur zertifizierte Marine-Seeventile verwenden!

**Hersteller:**
- TruDesign (NZ): Kunststoff, hohe Qualität, farbcodiert
- Forespar (USA): Marelon®-Pionier
- Groco (USA): Bronze, professionell
- Vetus (NL): Bronze und Kunststoff
- Blakes (UK): Bronze, traditionell

**Wartung:**
- Monatlich: Gängigkeit prüfen (auf/zu drehen)
- Halbjährlich: Vollständig schließen und öffnen unter Last
- Jährlich: Visuell auf Korrosion, Entzinkung prüfen
- Alle 15 Jahre: Austausch empfohlen (Bronze) bzw. nach Herstellerangabe

### 5.3 Seewasserfilter (Strainer)

Der Seewasserfilter fängt Tang, Muscheln, Sand, Plastikteile und
andere Verunreinigungen ab, bevor sie den Impeller oder Wärmetauscher
erreichen.

**Typen:**

| Typ | Durchlass | Preis (EUR) | Filtermasche | Einsatz |
|-----|:---:|:---:|:---:|---------|
| Groco ARG-Serie | ¾"–2" | 80–350 | 1,6 mm Standard | Meistverbreitet |
| Vetus FTR330-Serie | ¾"–1½" | 65–220 | 1,5 mm | Guter Durchfluss |
| Vetus FTR1320 | 1"–2" | 120–320 | 1,2 mm | Größere Motoren |
| Perko 0493 | ¾"–1½" | 55–180 | 1,6 mm | Kompakt |
| Groco SA-Serie | 1"–3" | 200–650 | Verschiedene | Professionell |

**Filterwartung:**
- Vor jedem Motorstart: Sichtprüfung des Filterkorbs (bei
  transparentem Deckel).
- Bei Durchflussabfall: Sofort reinigen.
- Monatlich (in warmen Gewässern): Filterkorb entnehmen und reinigen.
- Jährlich: Dichtungen prüfen und ggf. tauschen. O-Ring einfetten.
- Alle 5 Jahre: Filterkorb auf Korrosion prüfen.

**TIPP:** Ein zweiter Seewasserfilter mit Umschaltventil (Duplex-Filter)
ermöglicht die Reinigung während der Fahrt. Hersteller: Vetus (Dual
FTR), Groco (Dual ARG). Kosten: 250–600 EUR.

### 5.4 Seewasserleitungen

| Material | Durchmesser | Preis/m (EUR) | Lebensdauer | Empfehlung |
|----------|:---:|:---:|:---:|------------|
| Verstärkter Gummischlauch | ¾"–2" | 8–25 | 5–10 Jahre | Standard |
| Silikonschlauch (Marine) | ¾"–2" | 15–45 | 10–15 Jahre | Hochwertig, temperaturbeständig |
| CuNi-Rohr (90/10) | ¾"–2" | 30–80 | 25+ Jahre | Professionell, fest verlegt |
| PVC-Schlauch | ¾"–2" | 3–10 | 3–5 Jahre | Nicht empfohlen für Dauerinstallation |

**Schlauchschellen:**
- Immer Doppelschellen (2 Schellen pro Anschluss) verwenden.
- Material: Edelstahl 316 (A4). Niemals verzinkten Stahl!
- Alle Schläuche unterhalb der Wasserlinie müssen doppelt geschellt sein.
- Schlauchschellen jährlich auf Festsitz prüfen.
- Hersteller: ABA (Schweden), Mikalor (Spanien), Jubilee (UK).
- Preis: 1–5 EUR pro Schelle (A4 Edelstahl).

### 5.5 Seewasserfluss-Überwachung

Moderne Installationen überwachen den Seewasser-Durchfluss:

| Methode | Kosten (EUR) | Zuverlässigkeit | Empfehlung |
|---------|:---:|:---:|------------|
| Sichtfenster am Auspuff | 15–40 | Mittel | Minimum-Standard |
| Durchflusssensor (Paddle-Wheel) | 80–200 | Hoch | Empfohlen |
| Temperaturüberwachung Seewasseraustritt | 30–80 | Hoch | In Kombination ideal |
| Drucksensor Seewasserleitung | 120–300 | Sehr hoch | Professionell |

**Sichtfenster:** Ein transparenter Abschnitt im Auspuffschlauch oder
ein Sichtfenster am Wassersammler zeigt, ob Seewasser fließt. Kosten:
15–40 EUR. Einfachste und effektivste Überwachung.

---
---

## 6. Frischwasserkreislauf

### 6.1 Übersicht

Der Frischwasserkreislauf ist der geschlossene Kreislauf, der Kühlmittel
(Wasser + Glykol + Inhibitoren) durch den Motor zirkuliert. Er arbeitet
unter leichtem Überdruck (0,8–1,5 bar), um den Siedepunkt zu erhöhen.

**Flussrichtung:**
```
Frischwasserpumpe → Motorblock (Zylinderlaufbuchsen) →
Zylinderkopf → Thermostat → [wenn offen:] Wärmetauscher →
[wenn geschlossen:] Bypass zurück zur Pumpe →
Ausgleichsbehälter (angeschlossen)
```

### 6.2 Frischwasserpumpe

Die Frischwasserpumpe (auch: Kühlwasserpumpe, Umwälzpumpe) ist eine
mechanische Kreiselpumpe, die vom Motor angetrieben wird — entweder
direkt über Zahnräder (bei vielen Marine-Dieseln) oder über
Keilriemen.

**Typen:**

| Typ | Antrieb | Lebensdauer | Wartung |
|-----|---------|:---:|---------|
| Zahnradgetriebene Kreiselpumpe | Direkt vom Motor | Motorlebensdauer | Gleitringdichtung alle 3.000–5.000 h |
| Keilriemen-Kreiselpumpe | V-Riemen | 10.000+ h | Riemen + Dichtung |
| Elektrische Umwälzpumpe | 12/24 V | 5.000–10.000 h | Austausch bei Defekt |

**Symptome einer defekten Frischwasserpumpe:**
- Kühlmittelverlust (Dichtung undicht → Tropfen am Pumpengehäuse).
- Überhitzung (Pumpe fördert nicht mehr).
- Geräusche (Lager verschlissen → Quietschen, Schleifen).
- Kühlmittel-Verfärbung (Rost durch undichte Dichtung → Luft im System).

**Reparaturpreise:**
| Maßnahme | Kosten (EUR) |
|----------|:---:|
| Gleitringdichtung tauschen | 60–150 (Material) + 1–2 h Arbeit |
| Pumpe komplett tauschen | 200–600 (Material) + 2–4 h Arbeit |
| Keilriemen tauschen | 15–40 (Material) + 0,5 h Arbeit |

### 6.3 Ausgleichsbehälter

Der Ausgleichsbehälter (Expansion Tank) ist das höchste Element im
Frischwasserkreislauf. Er erfüllt mehrere Funktionen:

1. **Volumenausgleich:** Kühlmittel dehnt sich bei Erwärmung um ca. 5 %
   aus. Der Behälter nimmt die Volumenzunahme auf.
2. **Entlüftung:** Luft im System steigt auf und sammelt sich im
   Behälter.
3. **Druckhaltung:** Der Verschlussdeckel enthält ein Druckventil
   (typisch 0,9–1,2 bar), das den Systemdruck begrenzt.
4. **Überdruckschutz:** Bei zu hohem Druck öffnet das Ventil und lässt
   Kühlmittel in einen Überlaufbehälter ab.
5. **Nachfüllung:** Kühlmittel wird hier nachgefüllt.

**Verschlussdeckel:**
- Druckstufe: 0,9 bar (Standard Marine), 1,0–1,2 bar (Hochleistung).
- Tauschen: Alle 5 Jahre oder bei sichtbarer Dichtungsalterung.
- Preis: 8–25 EUR (Originalersatzteil).
- **ACHTUNG:** Verschlussdeckel nie bei heißem Motor öffnen! Kochendes
  Kühlmittel unter Druck → schwere Verbrühungen.

### 6.4 Kühlmittelschläuche

| Position | Temperatur | Empfohlenes Material | Innendurchmesser |
|----------|:---:|----------------------|:---:|
| Motorblock → Thermostat | 80–95 °C | EPDM Marine-Schlauch, Silikon | 25–38 mm |
| Thermostat → Wärmetauscher | 80–95 °C | EPDM Marine-Schlauch, Silikon | 25–38 mm |
| Wärmetauscher → Pumpe | 60–80 °C | EPDM Marine-Schlauch | 25–38 mm |
| Heizungsvorlauf | 80–95 °C | EPDM Marine-Schlauch | 16–19 mm |
| Heizungsrücklauf | 50–70 °C | EPDM Marine-Schlauch | 16–19 mm |

**Schlauch-Alterung erkennen:**
- Außen: Risse, Verhärtung, Aufquellen, Ölverfärbung.
- Innen: Aufweichung (Schlauch lässt sich zusammendrücken), Delaminierung.
- Schellen: Rost, Lockerung, Einschnürung im Schlauch.
- **Drucktest:** Bei 2 bar über 15 min → kein Druckabfall = OK.

### 6.5 Heizungsanbindung

Der Frischwasserkreislauf kann eine Kabinenheizung versorgen:

```
Motor → [T-Stück] → Heizungswärmetauscher (in Kabine) →
[T-Stück] → zurück zum Motor
```

- Heizleistung: ca. 2–5 kW bei 50-PS-Motor (abhängig von
  Durchfluss und Temperaturdifferenz).
- Absperrventil in der Heizungsleitung ermöglicht Abschaltung im Sommer.
- **WICHTIG:** Die Heizungsleitung muss einen Bypass haben, sonst
  steigt der Strömungswiderstand bei geschlossenem Heizungsventil.
- Hersteller Heizungswärmetauscher: Webasto, Eberspächer, Vetus.
- Kosten: 200–800 EUR (Wärmetauscher + Gebläse).

---
---

## 7. Wärmetauscher

### 7.1 Funktion und Grundprinzip

Der Wärmetauscher (Heat Exchanger, HEX) ist das zentrale Bauteil der
Zweikreis-Kühlung. Er überträgt die Wärme vom geschlossenen
Frischwasserkreislauf auf den offenen Seewasserkreislauf, ohne dass sich
die beiden Medien vermischen.

**Wärmeübertragungsprinzip:**
- Heißes Frischwasser (80–95 °C) fließt auf einer Seite.
- Kaltes Seewasser (8–28 °C) fließt auf der anderen Seite.
- Die Wärme überträgt sich durch die Trennwand (Rohr oder Platte).
- Typische Temperaturdifferenz Frischwasser Ein/Aus: 8–15 °C.
- Typische Temperaturdifferenz Seewasser Ein/Aus: 15–30 °C.

### 7.2 Bauarten

#### 7.2.1 Rohrbündel-Wärmetauscher (Tube Bundle / Shell-and-Tube)

Der häufigste Typ in der Marine. Ein Bündel dünner Rohre (typisch
8–60 Rohre, Ø 6–10 mm) wird von einem zylindrischen Gehäuse umgeben.

**Aufbau:**
- **Rohre (Tubes):** Seewasser fließt durch die Rohre.
- **Mantel (Shell):** Frischwasser umströmt die Rohre.
- **Rohrböden (Tube Sheets):** Halten die Rohre, trennen die Kreisläufe.
- **Endkappen (End Caps):** Verschließen die Seewasserseite, enthalten
  Zinkanode.

**Material:**
| Komponente | Standard | Premium |
|-----------|---------|---------|
| Rohre | Kupfer (Cu) | Kupfer-Nickel (CuNi 90/10) |
| Mantel | Kupfer oder Bronze | CuNi oder Edelstahl 316L |
| Rohrböden | Messing | CuNi oder Bronze |
| Endkappen | Messing oder Bronze | CuNi oder Bronze |

**Lebensdauer:**
- Kupfer-Rohre: 8–12 Jahre (Seewasser)
- CuNi-Rohre: 15–25 Jahre (Seewasser)
- Mantel: 15–30 Jahre

#### 7.2.2 Plattenwärmetauscher (Plate Heat Exchanger)

Parallele gewellte Platten mit wechselnder Durchströmung. Kompaktere
Bauweise, höhere Effizienz pro Volumen.

**Vorteile:**
- 3–5× kompakter als Rohrbündel bei gleicher Leistung.
- Höherer Wärmeübergangskoeffizient.
- Leichter zu reinigen (zerlegbar).

**Nachteile:**
- Empfindlicher gegen Verschmutzung (enge Kanäle, 2–5 mm).
- Dichtungen (Gaskets) altern und müssen getauscht werden.
- Teurer in der Anschaffung.

**Hersteller Marine-Plattenwärmetauscher:**
- Alfa Laval (Schweden): Industriestandard, teuer aber langlebig.
- SWEP (Schweden): Gelötete Plattenwärmetauscher.
- GEA (Deutschland): Professionelle Marine-Lösungen.

#### 7.2.3 Koaxial-Wärmetauscher (Tube-in-Tube)

Ein Rohr in einem Rohr — einfachste Bauweise. Nur für kleine Motoren
oder als Ölkühler eingesetzt.

### 7.3 Hersteller und Preise

| Hersteller | Herkunft | Typ | Motorleistung | Preis (EUR) |
|-----------|---------|-----|:---:|:---:|
| Bowman | UK | Rohrbündel (CuNi) | 10–30 PS | 350–600 |
| Bowman | UK | Rohrbündel (CuNi) | 30–75 PS | 550–900 |
| Bowman | UK | Rohrbündel (CuNi) | 75–200 PS | 800–1.500 |
| Bowman | UK | Rohrbündel (CuNi) | 200–500 PS | 1.400–2.800 |
| Fernstrum | USA | Rohrbündel | 10–50 PS | 400–700 |
| Fernstrum | USA | Rohrbündel | 50–150 PS | 650–1.200 |
| Vetus | NL | Rohrbündel (CuNi) | 10–40 PS | 300–550 |
| Vetus | NL | Rohrbündel (CuNi) | 40–120 PS | 500–900 |
| Alfa Laval | SE | Platte | 50–200 PS | 600–1.800 |

**OEM-Wärmetauscher (Motoren-Hersteller):**
| Motor | OEM-Preis (EUR) | Aftermarket (Bowman) (EUR) |
|-------|:---:|:---:|
| Yanmar 3JH40 | 600–800 | 400–550 |
| Yanmar 4JH80 | 800–1.100 | 550–750 |
| Volvo Penta D1-30 | 550–750 | 380–520 |
| Volvo Penta D2-55 | 700–950 | 480–650 |
| Volvo Penta D2-75 | 850–1.100 | 580–780 |
| Nanni N4.50 | 650–900 | 450–620 |

### 7.4 Wartung und Reinigung

#### 7.4.1 Seewasserseite (Rohre)

Die Seewasserseite verschmutzt durch Kalk, Salz, Bewuchs und
Korrosionsprodukte. Regelmäßige Reinigung ist essentiell.

**Chemische Reinigung (empfohlen jährlich):**
1. Seewasserkreislauf entleeren.
2. Endkappen des Wärmetauschers entfernen.
3. Reinigungslösung einfüllen und einwirken lassen:
   - Rydlyme (USA): 30–60 min, biologisch abbaubar, pH ~2.
   - Barnacle Buster (USA): 30–60 min, für Kalk und Muscheln.
   - Essigessenz (10 %): 2–4 h, günstige Alternative, weniger effektiv.
   - Phosphorsäure (10 %): 30 min, aggressiv, gut spülen!
4. Gründlich mit Frischwasser spülen.
5. Endkappen montieren, neue O-Ringe verwenden.
6. Zinkanode prüfen und ggf. tauschen.

**Mechanische Reinigung:**
- Rohrbürste (passend zum Rohrdurchmesser) durch jedes Rohr führen.
- Bei starker Verkalkung: erst chemisch, dann mechanisch.
- Vorsicht: Keine Stahlbürsten bei Kupfer- oder CuNi-Rohren!
  Nur Nylon- oder Messingbürsten verwenden.

**Kosten chemische Reinigung (Eigenleistung):**
- Rydlyme (5 l): ca. 80 EUR
- Barnacle Buster (4 l): ca. 65 EUR
- Essigessenz (10 l): ca. 15 EUR
- O-Ringe Endkappen: 5–15 EUR

**Kosten professionelle Reinigung (Fachbetrieb):**
- Wärmetauscher ausbauen, reinigen, einbauen: 300–600 EUR

#### 7.4.2 Frischwasserseite (Mantel)

Die Frischwasserseite verschmutzt kaum, wenn das richtige Kühlmittel
verwendet wird. Probleme entstehen durch:

- Falsches Kühlmittel (Leitungswasser ohne Inhibitoren → Rost).
- Gemischte Kühlmittel (OAT + IAT → Gelbildung, Verstopfung).
- Übermäßig altes Kühlmittel (Inhibitoren verbraucht → Korrosion).

**Symptome Frischwasserseite verschmutzt:**
- Kühlmittel bräunlich/rostig verfärbt.
- Schlamm im Ausgleichsbehälter.
- Überhitzung trotz sauberem Seewasserkreislauf.

**Spülung:**
1. Altes Kühlmittel ablassen.
2. Mit Frischwasser + Kühlsystem-Reiniger (z.B. Prestone Flush)
   befüllen und Motor 30 min laufen lassen.
3. Ablassen, 2× mit Frischwasser nachspülen.
4. Mit frischem Kühlmittel in korrekter Mischung befüllen.

### 7.5 Wärmetauscher-Leistungsprüfung

**Einfacher Praxistest:**
1. Motor auf Betriebstemperatur bringen (Thermostat offen).
2. Seewasser-Eintrittstemperatur messen (Infrarot-Thermometer am
   Einlassschlauch des Wärmetauschers).
3. Seewasser-Austrittstemperatur messen (am Auslassschlauch).
4. Frischwasser-Eintrittstemperatur messen (Motoranzeige oder
   Thermometer am Thermostatgehäuse).
5. Frischwasser-Austrittstemperatur messen (am Rücklaufschlauch zur
   Pumpe).

**Bewertung:**
| Parameter | Gut | Akzeptabel | Schlecht |
|-----------|:---:|:---:|:---:|
| Seewasser ΔT (Aus − Ein) | 20–35 °C | 15–20 °C | <15 °C |
| Frischwasser ΔT (Ein − Aus) | 5–12 °C | 12–18 °C | >18 °C |
| Frischwasser Maximaltemp. | <88 °C | 88–95 °C | >95 °C |
| Approach Temp. (FW_aus − SW_ein) | <15 °C | 15–25 °C | >25 °C |

---
---

## 8. Ölkühler

### 8.1 Funktion

Der Ölkühler (Oil Cooler) kühlt das Motoröl und/oder das Getriebeöl.
Warmes Öl gibt seine Wärme an das Seewasser ab (seltener an das
Frischwasser). Die Öltemperatur beeinflusst direkt die Schmierung:

| Öltemperatur | Zustand | Wirkung |
|:---:|---------|---------|
| <40 °C | Zu kalt | Öl zu dickflüssig, hohe Reibung, schlechte Schmierung |
| 40–60 °C | Aufwärmung | Normal bei Kaltstart |
| 60–90 °C | Optimal | Gute Schmierung, niedrige Reibung |
| 90–110 °C | Grenzbereich | Schmierung noch ausreichend, Überwachung nötig |
| >110 °C | Überhitzung | Ölfilm reißt, Schmierung versagt, Motorschaden droht |
| >130 °C | Kritisch | Ölzersetzung beginnt, Lagerschaden wahrscheinlich |

### 8.2 Bauarten

**Seewasser-Ölkühler:**
- Rohrbündel oder Platte, Seewasser auf einer Seite, Öl auf der anderen.
- Häufig direkt am Wärmetauscher-Gehäuse integriert (Yanmar, Volvo Penta).
- Zinkanode erforderlich (Seewasserkontakt).

**Frischwasser-Ölkühler:**
- Weniger verbreitet, aber korrosionsärmer.
- Platten- oder Koaxialtauscher zwischen Ölkreislauf und Frischwasserkreislauf.
- Keine Zinkanode nötig.

**Luft-Ölkühler:**
- Selten bei Marine-Anwendungen (kein Fahrtwind).
- Nur bei Kielkühlung als Ergänzung.

### 8.3 Typische Probleme

**Innere Leckage (Öl → Seewasser oder umgekehrt):**
- Ölfilm auf dem Seewasser am Auspuff → Öl leckt ins Seewasser.
- Kühlmittel milchig/emulsionsartig → Wasser im Öl.
- **KRITISCH:** Seewasser im Motoröl → sofortiger Motorstillstand
  und Ölwechsel. Seewasser zerstört Lagerflächen in Stunden.

**Verschmutzung:**
- Seewasserseite: Kalk, Muscheln (wie Wärmetauscher).
- Ölseite: Ölschlamm, Ölkohle bei überzogenen Ölwechselintervallen.

**Preise Ölkühler:**
| Motor | OEM-Preis (EUR) | Aftermarket (EUR) |
|-------|:---:|:---:|
| Yanmar 3JH-Serie | 350–500 | 200–350 |
| Volvo Penta D1/D2 | 300–500 | 180–320 |
| Nanni N4-Serie | 280–450 | 180–300 |
| Mercruiser CMD 2.8 | 400–600 | 250–400 |

### 8.4 Getriebeölkühler

Getriebe (Saildrive, Wendegetriebe) erzeugen ebenfalls Wärme, die
abgeführt werden muss:

- **Kleine Getriebe (<50 PS):** Oft kein separater Kühler, Wärme
  wird über das Getriebegehäuse abgestrahlt.
- **Mittlere Getriebe (50–150 PS):** Seewasser-Ölkühler am Getriebe
  (ZF, Technodrive).
- **Große Getriebe (>150 PS):** Dedizierter Plattenwärmetauscher.

**Getriebeöl-Temperatur:**
- Sollbereich: 60–90 °C
- Alarm: >110 °C
- Kritisch: >130 °C

### 8.5 Ölkühler-Wartung

| Intervall | Maßnahme |
|-----------|----------|
| Jährlich | Ölkühler-Zinkanode prüfen (falls Seewasser-Typ) |
| 2 Jahre | Seewasserseite chemisch reinigen (wie Wärmetauscher) |
| 5 Jahre | Ölkühler auf Undichtigkeit prüfen (Drucktest) |
| 8–12 Jahre | Austausch erwägen (Seewasser-Ölkühler) |

**Ölkühler-Leckage erkennen:**
- Öl im Seewasser: Ölfilm am Auspuff-Wasserauslass (Regenbogenfilm
  auf der Wasseroberfläche).
- Wasser im Öl: Ölpeilstab zeigt milchige Emulsion (weiß/beige).
  Ölstand steigt unerklärlich. Öl wird dünnflüssiger.
- **Sofortmaßnahme bei Wasser im Öl:** Motor SOFORT abstellen.
  Kompletter Ölwechsel + Filterwechsel VOR dem nächsten Start.
  Ölkühler tauschen. Motor 10 Minuten bei Leerlauf laufen lassen,
  erneuter Ölwechsel (Restwasser ausspülen).

### 8.6 Saildrive-Ölkühlung

Saildrive-Einheiten (Volvo Penta 120S/130S/150S, Yanmar SD) erzeugen
weniger Wärme als konventionelle Getriebe, haben aber im Unterwasserteil
direkten Seewasserkontakt. Die Schmierung und Kühlung erfolgt über das
Getriebeöl, das an der Gehäusewand Wärme an das umgebende Seewasser
abgibt.

**Besonderheiten:**
- Kein separater Ölkühler nötig (Saildrive-Gehäuse wirkt als Kühler).
- Getriebeöl-Wechselintervall: jährlich oder alle 200 h.
- Saildrive-Anoden (Zinkanode am Unterwasserteil): alle 1–2 Jahre.
- Saildrive-Manschette: alle 5–7 Jahre tauschen (Gummi altert).

---
---

## 9. Ladeluftkühler (Intercooler)

### 9.1 Funktion

Turbodiesel-Motoren komprimieren die Ansaugluft, wodurch sie sich auf
120–200 °C erhitzt. Der Ladeluftkühler (Intercooler, Charge Air Cooler)
kühlt die verdichtete Luft vor dem Eintritt in den Zylinder auf
40–60 °C herunter.

**Warum Ladeluftkühlung wichtig ist:**
- Kühlere Luft ist dichter → mehr Sauerstoff → mehr Leistung (+15–25 %).
- Niedrigere Verbrennungstemperatur → weniger NOx-Emissionen.
- Geringere thermische Belastung der Kolben und Ventile.
- Besserer spezifischer Kraftstoffverbrauch.

### 9.2 Typen im Marine-Einsatz

**Seewasser-Ladeluftkühler (Water-to-Air):**
- Standard bei Marine-Turbodieseln.
- Seewasser kühlt die Ladeluft direkt.
- Vorteil: Sehr effizient (Seewasser 8–28 °C).
- Nachteil: Korrosionsgefahr auf der Seewasserseite, Zinkanode nötig.

**Frischwasser-Ladeluftkühler:**
- Seltener, bei einigen Volvo-Penta-Motoren (z.B. D4/D6).
- Separater Niedertemperatur-Frischwasserkreislauf.
- Vorteil: Keine Seewasserkorrosion im Ladeluftkühler.
- Nachteil: Zusätzlicher Kreislauf, Pumpe, Wärmetauscher.

### 9.3 Probleme

**Innere Undichtigkeit (Seewasser → Ladeluft → Zylinder):**
- KRITISCH: Seewasser gelangt über die Ladeluft in die Zylinder.
- Symptome: Weißer Rauch, Leistungsverlust, Motorlauf unruhig.
- Kann zu Hydrolock führen (Wasser ist inkompressibel → Pleuelbruch).
- Prüfung: Ladeluftschlauch abziehen, Seewasserspuren suchen.

**Verschmutzung:**
- Seewasserseite: Kalk, Muscheln.
- Ladeluftseite: Ölnebel + Wärme → Ölverkokung.
- Reinigung: Chemisch (Seewasserseite), Lösungsmittel (Luftseite).

**Kosten:**
| Motor | OEM-Ladeluftkühler (EUR) | Austausch (EUR) |
|-------|:---:|:---:|
| Yanmar 4JH-CR Turbo | 500–800 | 800–1.200 inkl. Einbau |
| Volvo Penta D2-75 | 600–900 | 900–1.400 inkl. Einbau |
| Nanni N4.65 | 450–700 | 700–1.100 inkl. Einbau |

---
---

## 10. Impeller und Seewasserpumpe

### 10.1 Funktionsprinzip

Die Seewasserpumpe ist eine Verdrängerpumpe (Flexible-Impeller-Pumpe).
Ein flexibler Gummi-Impeller dreht sich exzentrisch in einem runden
Gehäuse. Die Flügel werden auf einer Seite zusammengedrückt und
erzeugen so einen Saug- und Druckeffekt.

**Eigenschaften:**
- Selbstansaugend bis ca. 2 m Förderhöhe.
- Fördermenge proportional zur Drehzahl.
- Verträgt keine Trockenlauf (>15 Sekunden → Impeller zerstört).
- Drehrichtung fest vorgegeben (Flügel biegen sich in Drehrichtung).

### 10.2 Impeller-Typen und Hersteller

| Hersteller | Modell-Serie | Material | Flügel | Einsatz |
|-----------|-------------|----------|:---:|---------|
| Jabsco | Profile Serie | Neopren | 6–12 | Standard Marine, am weitesten verbreitet |
| Johnson (SPX) | 09-Series | Neopren | 8–12 | Häufig bei Volvo Penta, Perkins |
| Sherwood | G-Series | Neopren/Buna | 6–10 | Mercruiser, Caterpillar |
| Oberdorfer | N-Series | Neopren | 6–10 | Ältere amerikanische Motoren |
| Yanmar | OEM | Neopren | 10 | Yanmar-spezifisch (Jabsco-kompatibel) |

### 10.3 Impeller-Größen und Zuordnung

| Motor | Impeller | Größe (mm) | Flügel | OEM-Nr. | Aftermarket-Nr. |
|-------|---------|:---:|:---:|---------|-----------------|
| Yanmar 1GM/2GM | Jabsco | 51×22 | 6 | 128170-42070 | Jabsco 1210-0001 |
| Yanmar 3JH | Jabsco | 65×16 | 10 | 129670-42531 | Jabsco 22405-0001 |
| Yanmar 4JH | Jabsco | 76×51 | 10 | 129670-42532 | Jabsco 17370-0001 |
| Volvo Penta 2001/2003 | Johnson | 51×22 | 6 | 875575 | Johnson 09-808B |
| Volvo Penta D1-30 | Johnson | 65×16 | 10 | 3586496 | Johnson 09-812B |
| Volvo Penta D2-55/75 | Johnson | 65×38 | 12 | 21951346 | Johnson 09-824P |
| Nanni N4.38/N4.50 | Jabsco | 65×32 | 10 | 970312711 | Jabsco 22405-0001 |
| Beta Marine 14–25 | Jabsco | 51×22 | 6 | 211-60011 | Jabsco 1210-0001 |
| Mercruiser CMD 2.8 | Sherwood | 76×51 | 10 | 8M0204738 | Sherwood 10077K |

### 10.4 Materialien

| Material | Temperaturbereich | Seewasser | Benzin | Diesel | Lebensdauer |
|----------|:---:|:---:|:---:|:---:|:---:|
| Neopren (Standard) | −25 bis +82 °C | Ja | Nein | Nein | 300–800 h / 1–2 Jahre |
| Neopren (Marine-Grade) | −25 bis +90 °C | Ja | Nein | Nein | 500–1.000 h / 1–3 Jahre |
| Nitril (Buna-N) | −40 bis +107 °C | Ja | Ja | Ja | 400–800 h |
| Viton/FKM | −20 bis +200 °C | Ja | Ja | Ja | 800–2.000 h (aber teuer) |
| Polyurethan | −35 bis +82 °C | Ja | Nein | Nein | 500–1.200 h |

### 10.5 Austauschintervalle

| Bedingung | Intervall | Begründung |
|-----------|:---:|-----------|
| Charterboot / Vercharterung | 300–400 h oder jährlich | Hohe Betriebsstunden, kein Risiko |
| Langfahrt-Yacht | 500 h oder jährlich | Zuverlässigkeit kritisch |
| Segelboot (Wochenendnutzung) | 500 h oder 2 Jahre | Geringere Belastung |
| Motorboot (Wochenendnutzung) | 400 h oder jährlich | Höhere Drehzahlen |
| Vorsorglich vor Saison | Immer empfohlen | Verformte Flügel nach Winterpause |

**Kosten Impeller:**
| Impeller-Größe | OEM (EUR) | Aftermarket (EUR) |
|:--------------:|:---------:|:-----------------:|
| Klein (51 mm) | 25–45 | 12–25 |
| Mittel (65 mm) | 35–65 | 18–35 |
| Groß (76 mm) | 50–90 | 25–50 |
| Sehr groß (95+ mm) | 80–150 | 40–80 |

### 10.6 Impeller-Wechsel — Schritt für Schritt

1. Seeventil schließen!
2. Pumpendeckel entfernen (2–6 Schrauben, Schlitz oder Innensechskant).
3. Alten Impeller herausziehen (Impeller-Abzieher verwenden,
   ca. 15–30 EUR). Nicht mit Schraubendreher hebeln!
4. **Alle Flügel zählen!** Fehlt ein Flügel, steckt er im System
   (Wärmetauscher oder Mischkrümmer). Unbedingt suchen und entfernen!
5. Pumpenkammer und Verschleißplatte (Wear Plate) inspizieren.
   Bei Rillen >0,5 mm: Verschleißplatte tauschen (5–15 EUR).
6. Neuen Impeller mit Glyzerin oder Spülmittel einsetzen
   (niemals Silikonfett → greift Neopren an).
7. O-Ring/Dichtung des Deckels erneuern.
8. Pumpendeckel montieren, Schrauben gleichmäßig anziehen
   (Drehmoment: 5–8 Nm, je nach Hersteller).
9. Seeventil öffnen.
10. Motor starten und Seewasserfluss prüfen.

**KRITISCH — Fehlende Impeller-Flügel:**
Wenn Flügel des alten Impellers fehlen, haben sie sich gelöst und
stecken im System. Typische Fundorte:
- Im Wärmetauscher (häufigster Ort → Endkappe öffnen).
- Im Mischkrümmer.
- Im Ölkühler.
- Im Auspuffschlauch.

Nicht gefundene Flügel blockieren den Seewasserfluss und führen
mittelfristig zur Überhitzung. **Immer suchen, bis alle Flügel
gefunden sind!**

### 10.7 Trockenlauf-Schutz

Da der Impeller bei Trockenlauf in Sekunden zerstört wird, gibt es
Schutzmaßnahmen:

- **Seeventil-Sicherung:** Seeventil mit Kabelband offen sichern
  (nicht verschließen), damit es nicht versehentlich geschlossen wird.
- **Warnsystem:** Seewasser-Durchflusssensor + Alarm. Kosten: 80–200 EUR.
- **Betriebsanweisung:** "Seeventil öffnen" als erster Schritt in der
  Motor-Checkliste.
- **Sichtfenster im Auspuff:** Zeigt sofort, ob Seewasser fließt.

### 10.8 Seewasserpumpen-Gehäuse

| Gehäusematerial | Lebensdauer | Preis (EUR) | Bemerkung |
|----------------|:---:|:---:|-----------|
| Bronze | 15–25 Jahre | 150–400 | Standard Marine, langlebig |
| Edelstahl 316 | 10–20 Jahre | 120–350 | Gute Korrosionsbeständigkeit |
| Gusseisen (ältere Motoren) | 8–15 Jahre | 80–250 | Korrosionsanfällig, wird nicht mehr verbaut |
| Kunststoff/Composite | 10–20 Jahre | 100–300 | Moderne Alternative, keine Korrosion |

---
---

## 11. Mischkrümmer und Auspuffkrümmer

### 11.1 Funktion

Der Mischkrümmer (Mixing Elbow, Injection Elbow, Exhaust Elbow) ist
die Komponente, an der das Seewasser in den Abgasstrom eingespritzt
wird. Das Seewasser kühlt die heißen Abgase (300–500 °C) auf 60–80 °C
herunter und ermöglicht so einen Gummi-Auspuffschlauch (Nassauspuff).

**KRITISCHE KOMPONENTE:** Der Mischkrümmer ist die am stärksten
beanspruchte Komponente im Kühlsystem. Er ist gleichzeitig:
- Hohen Temperaturen ausgesetzt (Abgase 300–500 °C).
- Seewasserkorrosion ausgesetzt (Salzwasser, Chlorid-Ionen).
- Abgaskorrosion ausgesetzt (SO₂, CO₂, Kondensate).
- Mechanischer Belastung ausgesetzt (Vibration, Wärmedehnung).

### 11.2 Aufbau

**Typischer Mischkrümmer:**
```
Abgas vom Auspuffkrümmer → [Einlassseite] →
[Mischzone: Seewasser wird eingespritzt] → [Auslassseite] →
Auspuffschlauch → Wassersammler → Austritt
```

Der Auspuffkrümmer (Exhaust Manifold) sitzt direkt am Zylinderkopf
und sammelt die Abgase aus den einzelnen Zylindern. Oft sind
Auspuffkrümmer und Mischkrümmer ein Bauteil oder direkt verbunden.

### 11.3 Materialien

| Material | Lebensdauer | Preis (EUR) | Einsatz | Bewertung |
|----------|:---:|:---:|---------|-----------|
| Gusseisen (lackiert) | 5–10 Jahre | 200–600 | Standard bei vielen OEMs (Yanmar, Volvo alt) | Günstig, aber korrosionsanfällig |
| Gusseisen (beschichtet) | 8–15 Jahre | 300–800 | Verbesserter Standard | Besser, nicht perfekt |
| Edelstahl 316L | 10–20 Jahre | 500–1.500 | Aftermarket-Upgrade, einige OEMs | Gut, aber teuer |
| Nickelbasis-Legierung (Ni-Resist) | 15–25+ Jahre | 800–2.500 | Premium OEM (einige Yanmar, Nanni) | Ausgezeichnet |
| Aluminium (beschichtet) | 3–7 Jahre | 150–400 | Einige ältere Motoren | Nicht empfohlen für Seewasser |
| Risersystem (Composite) | 10–20 Jahre | 400–1.200 | Nachrüst-Alternativen | Innovative Lösung |

### 11.4 Versagensmechanismus

**Stadien der Mischkrümmer-Korrosion:**

1. **Schutzschicht intakt** (Jahr 0–3): Oberfläche geschützt durch
   Beschichtung, Farbe oder Passivschicht.
2. **Beschichtung bricht auf** (Jahr 3–6): Lokale Angriffe beginnen,
   besonders an Schweiß-/Gussnähten und in der Mischzone.
3. **Lochfraß beginnt** (Jahr 5–10): Einzelne Löcher durchdringen
   die Wandung. Seewasser tropft auf den Auspuffkrümmer.
4. **Durchbruch** (Jahr 8–15): Seewasser fließt unkontrolliert —
   entweder nach außen (Glücksfall) oder in den Abgasstrom zurück
   zum Motor (Katastrophe).

**Worst Case — Seewasser im Motor:**
Wenn der Mischkrümmer korrodiert und bei abgestelltem Motor Seewasser
über den Auspuffkrümmer in die Zylinder zurückfließt:
- Zylinder füllen sich mit Seewasser.
- Nächster Startversuch: Wasser ist inkompressibel → Pleuel verbiegen
  sich (Hydrolock) → Motorschaden.
- **Typische Kosten: 8.000–35.000 EUR** (Motorrevision oder -tausch).
- **Falls Motor nicht sofort gestoppt wird: Totalschaden.**

### 11.5 Inspektion

**Jährliche Sichtprüfung:**
1. Motor abstellen, auskühlen lassen.
2. Mischkrümmer visuell inspizieren (Taschenlampe, Spiegel).
3. Auf Rost, Blasen, weiße Kalkablagerungen, Feuchtigkeit achten.
4. Befestigungsschrauben auf Korrosion prüfen.
5. Dichtungen zwischen Krümmer und Auspuffkrümmer prüfen.

**Endoskopische Inspektion (empfohlen alle 3–5 Jahre):**
- Endoskop (USB-Kamera, ca. 30–80 EUR) durch Seewasser-Einlassöffnung
  einführen.
- Innenwand auf Korrosionstiefe, Lochfraß beurteilen.
- Wandstärke abschätzen (erfahrener Mechaniker).

**Ultraschall-Wandstärkenmessung (professionell):**
- Ultraschall-Dickenmessgerät (ab 500 EUR).
- Wandstärke an kritischen Punkten messen.
- Mindestwandstärke Gusseisen: 3 mm.
- Mindestwandstärke Edelstahl: 1,5 mm.
- Kosten Fachbetrieb: 80–200 EUR.

### 11.6 Austauschintervalle nach Material

| Material | Empfohlener Austausch | Maximaler Einsatz | Kosten Austausch |
|----------|:---:|:---:|:---:|
| Gusseisen (lackiert) | 5–7 Jahre | 10 Jahre | 400–1.200 EUR |
| Gusseisen (beschichtet) | 7–10 Jahre | 12 Jahre | 500–1.500 EUR |
| Edelstahl 316L | 10–15 Jahre | 20 Jahre | 800–2.500 EUR |
| Ni-Resist | 15–20 Jahre | 25 Jahre | 1.200–3.500 EUR |

**EMPFEHLUNG:** Beim ersten Mischkrümmer-Tausch direkt auf Edelstahl
oder Ni-Resist upgraden. Die Mehrkosten von 300–800 EUR amortisieren
sich über die doppelte Lebensdauer.

### 11.7 Hersteller-spezifische Mischkrümmer

| Motor | OEM-Material | OEM-Preis (EUR) | Aftermarket Edelstahl (EUR) | Hersteller Edelstahl |
|-------|-------------|:---:|:---:|:---:|
| Yanmar 1GM/2GM | Gusseisen (beschichtet) | 250–400 | 450–650 | Mixelbow Marine, Custom |
| Yanmar 3JH | Gusseisen (beschichtet) | 350–550 | 550–800 | LSR Marine, MHSP |
| Yanmar 4JH | Gusseisen (beschichtet) | 400–650 | 650–950 | LSR Marine, MHSP |
| Volvo Penta 2001/2003 | Gusseisen | 200–350 | 400–600 | Vetus, Custom |
| Volvo Penta D1-30 | Gusseisen (beschichtet) | 350–500 | 500–750 | Vetus, Custom |
| Volvo Penta D2-55/75 | Gusseisen (beschichtet) | 450–650 | 650–1.000 | Vetus, LSR Marine |
| Nanni N4 | Ni-Resist (OEM) | 600–900 | – (OEM bereits hochwertig) | – |
| Beta Marine | Gusseisen | 300–500 | 500–750 | LSR Marine |
| Perkins 4.108 | Gusseisen | 200–400 | 400–650 | Bowman, Custom |

**Aftermarket-Spezialisten für Edelstahl-Mischkrümmer:**
- LSR Marine (Deutschland): Hochwertige V4A-Krümmer, maßgefertigt.
- MHSP Marine (Niederlande): Edelstahl-Krümmer für japanische Motoren.
- Vetus (Niederlande): Standardisierte Krümmer für verbreitete Motoren.
- Halyard Marine (UK): Auspuff-Komponenten und Komplettlösungen.

### 11.8 Wassersammler (Waterlock) und Auspuffschlauch

Der Wassersammler sitzt im Auspuffweg zwischen Mischkrümmer und
Auspuffaustritt. Er hat zwei Funktionen:

1. **Schalldämpfung:** Seewasser dämpft Abgasgeräusche.
2. **Rückflusssperre:** Verhindert, dass Seewasser über den Auspuff
   ins Boot zurückfließt (bei Seegang).

**Dimensionierung:**
- Mindestvolumen: 2× Seewassermenge, die bei abgestelltem Motor
  im System steht.
- Typisch: 3–10 l je nach Motorleistung.
- Überlauf: Wenn der Wassersammler zu klein ist, kann Seewasser bei
  Seegang durch den Auspuff in den Motor gedrückt werden.

**Einbauhöhe:**
- Oberkante des Wassersammlers mindestens 300 mm unter dem
  Mischkrümmer-Auslass.
- Auspuffaustritt mindestens 150 mm über der Wasserlinie.
- Schwanenhals (Gooseneck) mindestens 300 mm über der Wasserlinie.

**Auspuffschlauch:**
- Material: Verstärkter Gummi mit Textileinlage (Vetus, Trident).
- Temperaturbeständigkeit: mind. 100 °C kontinuierlich.
- Innendurchmesser: 40–90 mm je nach Motor.
- Lebensdauer: 8–15 Jahre.
- Preis: 15–50 EUR/m.

---
---

## 12. Thermostat

### 12.1 Funktion

Der Thermostat regelt die Motortemperatur im Frischwasserkreislauf.
Er ist ein Wachselement-Ventil, das sich temperaturabhängig öffnet
und schließt:

- **Kaltstart (unter Öffnungstemperatur):** Thermostat geschlossen.
  Frischwasser zirkuliert nur im Motor (Bypass-Kreislauf). Motor
  wärmt sich schnell auf.
- **Betriebstemperatur erreicht:** Thermostat beginnt zu öffnen.
  Frischwasser fließt zum Wärmetauscher.
- **Volle Betriebstemperatur:** Thermostat voll offen. Maximaler
  Durchfluss zum Wärmetauscher.

### 12.2 Technische Daten

| Hersteller | Motor | Öffnungstemp. | Voll offen | Hub | OEM-Nr. |
|-----------|-------|:---:|:---:|:---:|---------|
| Yanmar | 1GM–3GM | 71 °C | 82 °C | 8 mm | 105582-49200 |
| Yanmar | 3JH/4JH | 76 °C | 87 °C | 8 mm | 129470-49801 |
| Yanmar | 4JH-CR | 76 °C | 87 °C | 8 mm | 129470-49801 |
| Volvo Penta | 2001/2003 | 75 °C | 87 °C | 10 mm | 838617 |
| Volvo Penta | D1-30 | 82 °C | 93 °C | 10 mm | 3831426 |
| Volvo Penta | D2-55/75 | 82 °C | 93 °C | 10 mm | 3831426 |
| Nanni | N4.38/N4.50 | 76 °C | 88 °C | 8 mm | 970311982 |
| Beta Marine | 14–38 | 82 °C | 93 °C | 10 mm | 209-60002 |
| Mercruiser | CMD 2.8 | 71 °C (160 °F) | 82 °C | 10 mm | 8M0204727 |

### 12.3 Wachselement-Funktionsprinzip

Das Wachselement besteht aus einem Kupfer-Zylinder, gefüllt mit einem
speziellen Wachs (typisch: Mischung aus Paraffin und Kupferpulver).
Beim Erwärmen dehnt sich das Wachs aus und drückt über einen Kolben
das Ventil auf. Beim Abkühlen zieht sich das Wachs zusammen, und eine
Feder drückt das Ventil zu.

**Warum Wachselemente versagen:**
- Wachs verliert über die Jahre an Ausdehnungsfähigkeit (Alterung).
- Ablagerungen (Korrosion, Kalkspuren) blockieren den Kolben.
- Feder ermüdet → Ventil schließt nicht mehr vollständig.
- Dichtung zwischen Wachselement und Gehäuse wird undicht.

### 12.4 Fehlermodi

| Fehler | Symptom | Wirkung | Gefahr |
|--------|---------|---------|--------|
| Thermostat klemmt offen | Motor wird nicht warm (<70 °C) | Wie Einkreis: schlechte Verbrennung, Verglasung | Mittel |
| Thermostat klemmt geschlossen | Motor überhitzt schnell | Kein Kühlwasser zum Wärmetauscher | HOCH |
| Thermostat öffnet zu spät | Motor wird zu heiß (95–105 °C) | Überhitzungsalarm, Motor läuft heiß | HOCH |
| Thermostat öffnet zu früh | Motor läuft zu kühl (60–70 °C) | Suboptimale Verbrennung | Niedrig |
| Thermostat schließt nicht ganz | Motor wird bei Kaltstart nie warm | Dauerhaft zu kühle Betriebstemperatur | Niedrig |

### 12.5 Prüfung

**Kochtest (Werkstatt-Methode):**
1. Thermostat in einen Topf mit Wasser legen.
2. Thermometer ins Wasser stellen.
3. Langsam erhitzen.
4. Notieren: Bei welcher Temperatur beginnt der Thermostat zu öffnen?
5. Notieren: Bei welcher Temperatur ist der Thermostat voll offen?
6. Abkühlen: Schließt der Thermostat vollständig?

**Sollwerte:**
- Öffnung: ±3 °C der Nenntemperatur.
- Volle Öffnung: ±5 °C der Nenntemperatur.
- Schließen: Vollständig, kein Spalt sichtbar.
- Hub: Mindestens Nennhub (z.B. 8 mm bei 82 °C).

**Kosten Thermostat:**
| Motor-Familie | OEM (EUR) | Aftermarket (EUR) |
|:---:|:---:|:---:|
| Yanmar 1GM–4JH | 25–50 | 12–30 |
| Volvo Penta D1/D2 | 30–60 | 15–35 |
| Nanni N4 | 20–45 | 12–25 |
| Beta Marine | 25–50 | 12–30 |

### 12.6 Austausch

**Intervall:** Alle 3–5 Jahre oder bei Fehlfunktion.

**Einbau-Tipps:**
- Neue Dichtung verwenden (immer, auch wenn die alte „gut aussieht").
- Thermostat-Gehäuse reinigen (Ablagerungen entfernen).
- Korrekte Einbaurichtung beachten (Wachselement zum Motor, Feder
  zum Wärmetauscher — je nach Hersteller!).
- Nach Einbau: Motor warmlaufen lassen und Temperaturverlauf beobachten.
- Kühlsystem entlüften (Luft im System nach Thermostat-Tausch häufig).

---
---

## 13. Kühlmittel und Frostschutz

### 13.1 Kühlmittel-Typen

Das Kühlmittel im Frischwasserkreislauf besteht aus Wasser + Glykol +
Inhibitoren. Es gibt zwei Hauptfamilien:

#### 13.1.1 IAT (Inorganic Additive Technology) — Konventionell

- **Inhibitoren:** Silikat, Phosphat, Borat, Nitrit.
- **Farbe:** Meist grün (variiert nach Hersteller).
- **Schutzmechanismus:** Bildet eine dicke Schutzschicht auf allen
  Metalloberflächen.
- **Wechselintervall:** Alle 2 Jahre oder 2.000 Betriebsstunden.
- **Vorteil:** Schnelle Schutzwirkung bei Erstbefüllung.
- **Nachteil:** Schutzschicht verbraucht sich, muss regelmäßig erneuert
  werden. Schicht isoliert teilweise → etwas schlechtere Wärmeübertragung.

#### 13.1.2 OAT (Organic Acid Technology) — Langzeitig

- **Inhibitoren:** Organische Säuren (Sebazat, 2-EHA).
- **Farbe:** Meist orange/rot (Dexcool) oder rosa/violett.
- **Schutzmechanismus:** Bildet dünne Schutzschicht nur an Korrosionsstellen.
- **Wechselintervall:** Alle 5 Jahre oder 5.000 Betriebsstunden.
- **Vorteil:** Längere Lebensdauer, bessere Wärmeübertragung.
- **Nachteil:** Langsame Anfangs-Schutzwirkung, teurer.

#### 13.1.3 HOAT (Hybrid OAT) — Kombination

- **Inhibitoren:** OAT-Basis + Silikate (kein Phosphat).
- **Farbe:** Meist gelb oder türkis.
- **Wechselintervall:** Alle 3–5 Jahre.
- **Vorteil:** Kombination der Vorteile beider Typen.
- **Nachteil:** Nicht mit IAT oder reinem OAT mischbar.

### 13.2 Hersteller-Empfehlungen

| Motor-Hersteller | Empfohlener Typ | Eigenmarke | Preis/l (EUR) |
|-----------------|----------------|------------|:---:|
| Yanmar | OAT (Long Life Coolant) | Yanmar Premium Coolant | 12–18 |
| Volvo Penta | OAT | Volvo Penta Coolant (grün) | 14–20 |
| Nanni | OAT | – (Standard OAT empfohlen) | 8–14 |
| Beta Marine | OAT oder IAT | – | 8–14 |
| Mercruiser | OAT (Extended Life) | Mercury Extended Life | 12–18 |

### 13.3 Mischungsverhältnis

| Glykol-Anteil | Frostschutz bis | Siedeschutz bis (bei 1 bar) | Empfehlung |
|:---:|:---:|:---:|------------|
| 25 % | −12 °C | 103 °C | Minimum (Mittelmeer, Sommer) |
| 33 % | −20 °C | 106 °C | Standard Marine |
| 40 % | −28 °C | 108 °C | Nordeuropa |
| 50 % | −36 °C | 112 °C | Skandinavien, Winterlager |
| 60 % | −52 °C | 118 °C | Extremklima (nicht >60 % — verschlechtert Kühlung!) |

**ACHTUNG:** Mehr als 60 % Glykol verschlechtert die Wärmeübertragung
signifikant (Glykol leitet Wärme schlechter als Wasser). Maximum 60 %.

### 13.4 Ethylenglykol vs. Propylenglykol

| Eigenschaft | Ethylenglykol (EG) | Propylenglykol (PG) |
|------------|:---:|:---:|
| Frostschutz (50 %) | −36 °C | −32 °C |
| Toxizität | GIFTIG (tödlich ab ~100 ml) | Unbedenklich (Lebensmittelzusatz) |
| Wärmeübertragung | Besser (Referenz) | 5–10 % schlechter |
| Viskosität (kalt) | Niedriger | Höher |
| Preis/l | 3–6 EUR | 5–10 EUR |
| Umwelt (Gewässer) | Giftig für Tiere | Ungiftig |
| Einsatz Seewasserkreislauf (Winterfest.) | NEIN (giftig!) | JA (empfohlen) |
| Einsatz Frischwasserkreislauf | Standard | Empfohlen bei Umweltbewusstsein |

**EMPFEHLUNG:**
- Frischwasserkreislauf: Ethylenglykol (besser) oder Propylenglykol
  (umweltfreundlicher). Beide funktionieren.
- Seewasserkreislauf-Winterfestmachung: NUR Propylenglykol
  (ungiftig, biologisch abbaubar → gelangt ins Meer).

### 13.5 Kühlmittel-Überwachung

**Refraktometer (Preis: 15–40 EUR):**
- Misst den Brechungsindex → Glykol-Konzentration.
- Wenige Tropfen Kühlmittel auf das Prisma, Skala ablesen.
- Genauigkeit: ±2 °C Frostschutz.
- Verschiedene Skalen für EG und PG beachten!

**pH-Wert (Teststreifen: 5–10 EUR):**
- Frisches Kühlmittel: pH 7,5–9,0.
- Verbrauchtes Kühlmittel: pH <7,0 → sauer → Korrosion!
- Wenn pH <7,0: Kühlmittel sofort wechseln.

**Optische Prüfung:**
- Klar und farbig (grün/orange/rosa): OK.
- Trüb: Mögliche Vermischung oder Alterung.
- Bräunlich/rostig: Korrosion im System → spülen und wechseln.
- Ölig/milchig: Ölkühler undicht (Öl im Kühlmittel) → SOFORT prüfen!
- Schaumig: Zylinderkopfdichtung undicht (Abgase im Kühlmittel) →
  SOFORT prüfen!

### 13.6 Kühlmittelwechsel

**Intervall:**
- IAT: Alle 2 Jahre oder 2.000 h.
- OAT: Alle 5 Jahre oder 5.000 h.
- HOAT: Alle 3–5 Jahre oder 3.000–5.000 h.

**Ablauf:**
1. Motor auf Betriebstemperatur bringen (Thermostat offen).
2. Motor abstellen.
3. Ablasshahn am Motorblock öffnen (Auffangbehälter!).
4. Ablasshahn am Wärmetauscher öffnen (falls vorhanden).
5. Altes Kühlmittel umweltgerecht entsorgen (Sondermüll bei EG!).
6. System mit Frischwasser spülen (Motor 10 min laufen lassen,
   ablassen, wiederholen).
7. Neue Kühlmittelmischung einfüllen.
8. System entlüften (Entlüftungsschraube am Thermostatgehäuse öffnen,
   bis blasenfreies Kühlmittel kommt).
9. Ausgleichsbehälter auf Sollstand füllen.
10. Motor warmlaufen lassen, auf Undichtigkeiten prüfen.
11. Nach 24 h Kühlmittelstand nachprüfen und ggf. nachfüllen.

**Füllmenge typische Motoren:**
| Motor | Systemvolumen (l) |
|-------|:---:|
| Yanmar 1GM10 | 1,5 |
| Yanmar 3JH40 | 3,5 |
| Yanmar 4JH80 | 5,0 |
| Volvo Penta D1-30 | 3,0 |
| Volvo Penta D2-55 | 4,5 |
| Volvo Penta D2-75 | 5,5 |
| Nanni N4.50 | 4,0 |
| Beta Marine 25 | 3,0 |

---
---

## 14. Seewasserfilter und Seeventile

### 14.1 Seewasserfilter-Systeme im Detail

#### 14.1.1 Standard-Einzelfilter

Der Standard-Seewasserfilter besteht aus einem Gehäuse (Bronze,
Kunststoff oder Edelstahl) mit einem herausnehmbaren Filterkorb
(Edelstahl 316-Sieb, Maschenweite 1,2–2,0 mm) und einem transparenten
oder durchsichtigen Deckel zur Sichtkontrolle.

**Durchfluss-Kapazitäten:**

| Anschluss | Max. Durchfluss | Geeignet für Motor bis |
|:---:|:---:|:---:|
| ¾" (19 mm) | 60 l/min | 30 PS |
| 1" (25 mm) | 100 l/min | 50 PS |
| 1¼" (32 mm) | 160 l/min | 100 PS |
| 1½" (38 mm) | 250 l/min | 160 PS |
| 2" (50 mm) | 400 l/min | 300 PS |

#### 14.1.2 Duplex-Filter (Umschaltfilter)

Zwei Filtergehäuse mit einem Umschaltventil. Während ein Filter in
Betrieb ist, kann der andere gereinigt werden — ohne den Motor zu
stoppen.

**Hersteller und Preise:**
| Hersteller | Modell | Anschluss | Preis (EUR) |
|-----------|--------|:---:|:---:|
| Vetus | FTR3320/D | 1"–1¼" | 280–420 |
| Groco | ARG-D-1000 | 1" | 350–500 |
| Groco | ARG-D-1500 | 1½" | 450–650 |
| Perko | 0493 DP-Serie | 1"–1½" | 300–480 |

#### 14.1.3 Selbstreinigende Filter

Automatische Rückspülung durch Druckdifferenz-Auslösung. In der
Sportschifffahrt selten, aber bei Arbeitsbooten und größeren Yachten
gelegentlich anzutreffen.

### 14.2 Seeventile — Vertiefung

#### 14.2.1 Bronze-Seeventile

**DZR-Bronze (Dezincification Resistant):**
- Legierung: CuZn36Pb2As (CW602N) oder ähnlich.
- Arsen-Zusatz verhindert Entzinkung (selektive Korrosion des Zinks).
- Kennzeichnung: "CR" oder "DZR" eingeprägt.
- Lebensdauer: 15–25 Jahre im Seewasser.
- Preis: 80–250 EUR je nach Größe.

**Standard-Messing (NICHT empfohlen):**
- Legierung: CuZn39Pb3 oder ähnlich — KEIN Entzinkungsschutz.
- Im Sanitärhandel üblich, aber im Seewasser lebensgefährlich.
- Entzinkung: Zink löst sich aus der Legierung, Kupfergerüst bleibt
  zurück → spröde, porös, bricht unter Last.
- **WARNUNG:** Entzinkung ist von außen oft nicht sichtbar! Messing
  sieht intakt aus, ist aber innen zerstört.

#### 14.2.2 Kunststoff-Seeventile (TruDesign / Marelon)

- Material: Glasfaserverstärktes Nylon (Marelon®) oder Composite.
- Keine Korrosion, keine galvanische Wechselwirkung.
- CE-zugelassen für Unterhalb-Wasserlinie (ISO 9093).
- Farbcodiert nach Funktion (rot=Feuerlösch, blau=Wasser, grau=Abwasser).
- Lebensdauer: 15–25 Jahre.
- Preis: 35–120 EUR.
- **Nachteil:** UV-empfindlich (Einbau unter Deck), begrenzte
  Temperaturbeständigkeit (max. 60–80 °C → nicht direkt am
  Seewasser-Auslass eines Motors).

#### 14.2.3 Montage und Borddurchlass

**Borddurchlass (Skin Fitting / Through-Hull):**
- Bronze DZR: Standard, langlebig.
- Kunststoff (TruDesign/Marelon): Korrosionsfrei.
- Edelstahl 316: Nicht empfohlen (Spaltkorrosion am Rumpf).
- MUSS mit Seeventil als Einheit verschraubt sein (Gegenmutter innen).
- Dichtmittel: 3M 5200 (permanent) oder Sikaflex 291i.

**Einbauposition:**
- Möglichst tief (besserer Durchfluss bei Krängung).
- Nicht in der Nähe von Zinkanoden (galvanische Strömung).
- Mindestabstand zwischen zwei Borddurchlässen: 150 mm.
- Alle Borddurchlässe unter Wasserlinie müssen mit Seeventil
  ausgestattet sein (gesetzliche Vorschrift, ISO 9093).

### 14.3 Schmutzwasser-Problematik

In bestimmten Revieren (Wattenmeer, Flüsse, Lagunen, Häfen) ist
das Wasser besonders schmutzig:

| Problem | Lösung |
|---------|--------|
| Sand | Gröberer Vorfilter + Standard-Filter |
| Tang/Algen | Regelmäßige Filterreinigung, Duplex-Filter |
| Muscheln | Bewuchsschutz am Borddurchlass (Antifouling) |
| Plastiktüten | Größerer Filter, Sichtfenster, Duplex |
| Quallen | Gitter vor dem Borddurchlass (Preis: 20–50 EUR) |
| Schlick | Borddurchlass höher positionieren, zusätzlicher Vorfilter |

---
---

## 15. Zinkanoden im Kühlsystem

### 15.1 Funktion

Zinkanoden (auch: Opferanoden, Korrosionsschutzanoden) schützen
edlere Metalle (Kupfer, Bronze, Edelstahl) im Kühlsystem vor
galvanischer Korrosion. Zink ist in der elektrochemischen Spannungsreihe
unedler als Kupfer → Zink korrodiert anstelle der Kühlsystem-Komponenten.

### 15.2 Positionen im Kühlsystem

| Position | Schutz für | Typische Größe | Wechselintervall |
|----------|-----------|:---:|:---:|
| Wärmetauscher (Endkappe) | Wärmetauscher-Rohre | M8×25 bis M12×40 | 6–12 Monate |
| Ölkühler (Endkappe) | Ölkühler-Rohre | M8×20 bis M10×30 | 6–12 Monate |
| Ladeluftkühler | Ladeluftkühler-Rohre | M8×20 bis M10×30 | 6–12 Monate |
| Motorblock (Einschraubposition) | Motorblock-Kühlkanäle | ½"–¾" Gewinde | 6–12 Monate |
| Seewasserpumpe (falls Bronze) | Pumpengehäuse | M6×15 | 6–12 Monate |

### 15.3 Materialien

| Material | Anwendung | Spannung (V) | Schutzbereich |
|----------|-----------|:---:|:---:|
| Zink (Zn) | Seewasser (Salzwasser) | −1,05 V | Standard Marine |
| Magnesium (Mg) | Süßwasser/Brackwasser | −1,60 V | Binnengewässer |
| Aluminium (Al) | Seewasser oder Brackwasser | −1,10 V | Universal |

**WARNUNG:** Zink im Süßwasser → zu geringe Spannungsdifferenz →
kein Schutz. Magnesium im Seewasser → zu hohe Spannung → übermäßiger
Verbrauch und Wasserstoffversprödung möglich.

### 15.4 Prüfung und Austausch

**Prüfung:**
- Sichtprüfung: Oberfläche rau, porös, deutlich kleiner → verbraucht.
- Faustregel: Austausch bei 50 % Volumenverlust.
- Niemals Anoden „bis zum letzten Rest" aufbrauchen → die letzten
  20 % bieten kaum noch Schutz.

**Austausch:**
- Halbjährlich kontrollieren (bei jeder Saisonwartung).
- Spätestens jährlich tauschen.
- In warmen, salzigen Gewässern (Mittelmeer, Tropen): alle 6 Monate.
- In kalten, wenig salzigen Gewässern (Ostsee): alle 12 Monate.

**Kosten:**
| Größe | Preis/Stück (EUR) |
|:---:|:---:|
| M8×20 (klein) | 3–8 |
| M8×30 (mittel) | 5–12 |
| M10×40 (groß) | 8–18 |
| M12×50 (XL) | 12–25 |
| ½" Motorblock-Anode | 8–20 |
| ¾" Motorblock-Anode | 12–28 |

### 15.5 Elektrolyse-Probleme

Galvanische Korrosion kann verstärkt werden durch:

- **Fremde Stromquellen:** Leckstrom von der Landstromversorgung durch
  das Seewasser → beschleunigte Korrosion. Lösung: Galvanischer
  Isolator (z.B. Mastervolt Galvanic Isolator, 120–300 EUR).
- **Falsche Metallkombinationen:** Edelstahl-Borddurchlass + Bronze-
  Seeventil + Kupfer-Wärmetauscher → galvanische Kette. Lösung:
  Einheitliche Materialwahl oder Isolierstücke.
- **Fehlende Erdung:** Motorblock muss über Erdungsband mit dem
  Unterwasserschiff verbunden sein.
- **Marinegrill:** Nachbarboot am Steg mit Erdungsproblem kann über
  das Hafenwasser Ihr Boot angreifen.

---
---

## 16. Fehlerbild-Atlas

### Fehlerbild 16.1 — Motorüberhitzung

**Symptome:**
- Temperaturanzeige steigt über 95–100 °C.
- Überhitzungsalarm (akustisch/optisch).
- Dampf/Dampfgeruch im Maschinenraum.
- Leistungsverlust.
- Kühlmittel kocht über (Ausgleichsbehälter).

**Ursachen (nach Häufigkeit):**
1. Impeller defekt/verschlissen (35 % der Fälle).
2. Seewasserfilter verstopft (20 %).
3. Wärmetauscher verkalkt/verschmutzt (15 %).
4. Thermostat klemmt geschlossen (10 %).
5. Seeventil versehentlich geschlossen (8 %).
6. Seewasserschlauch geknickt (5 %).
7. Kühlmittelverlust im Frischwasserkreislauf (4 %).
8. Frischwasserpumpe defekt (3 %).

**Sofortmaßnahme:**
1. Motordrehzahl auf Leerlauf reduzieren.
2. Seewasserfluss prüfen (Sichtfenster Auspuff).
3. Falls kein Seewasser fließt: Motor sofort abstellen.
4. Falls Seewasser fließt: Ursache im Frischwasserkreislauf suchen.

**Kosten je Ursache:**
| Ursache | Reparaturkosten (EUR) |
|---------|:---:|
| Impeller tauschen | 30–100 (Eigenleistung) / 150–300 (Werft) |
| Seewasserfilter reinigen | 0 (Eigenleistung) |
| Wärmetauscher reinigen | 15–80 (Eigenleistung) / 300–600 (Werft) |
| Thermostat tauschen | 30–70 (Eigenleistung) / 150–300 (Werft) |
| Seeventil öffnen | 0 |

---

### Fehlerbild 16.2 — Impeller-Versagen

**Symptome:**
- Kein oder zu wenig Seewasser am Auspuff.
- Motor überhitzt.
- Gummi-Teile im Seewasserfilter oder Wärmetauscher.
- Impeller-Pumpe läuft laut oder vibriert.

**Ursachen:**
1. Alterung (Gummi verhärtet, Flügel brechen).
2. Trockenlauf (Seeventil geschlossen, Filter verstopft).
3. Sand/Partikel im Seewasser (abrasiver Verschleiß).
4. Falsche Drehrichtung nach Einbau (Flügel falsch herum).
5. Übermäßige Standzeit (Flügel permanent verformt über Winter).

**Bewertungsskala:**
| Zustand | Score | Maßnahme |
|---------|:---:|---------|
| Alle Flügel intakt, flexibel | 90–100 | OK, weiter verwenden |
| Flügel leicht verformt, alle vorhanden | 70–89 | Baldiger Austausch |
| 1–2 Flügel gerissen, alle vorhanden | 40–69 | Sofort tauschen, Fragmente suchen |
| Flügel fehlen | 0–39 | SOFORT tauschen, ALLE Fragmente finden! |

---

### Fehlerbild 16.3 — Wärmetauscher-Verstopfung

**Symptome:**
- Motortemperatur steigt langsam über Wochen/Monate.
- Seewasser-Austritt am Auspuff schwächer.
- Seewasser-Austrittstemperatur höher als normal.

**Ursachen:**
1. Kalkablagerung (Seewasser-Seite).
2. Muschel-/Algenbewuchs (Seewasser-Seite, besonders in Tropen).
3. Impeller-Fragmente blockieren Rohre.
4. Korrosionsprodukte (bei alten Kupferrohren).
5. Sand-/Schlickablagerung.

**Bewertungsskala:**
| Zustand | Score | Maßnahme |
|---------|:---:|---------|
| Sauber, voller Durchfluss | 90–100 | OK |
| Leichte Beläge, 10–20 % Reduktion | 70–89 | Chemische Reinigung planen |
| Deutliche Verkalkung, 20–40 % Reduktion | 50–69 | Chemische + mechanische Reinigung |
| Stark verstopft, >40 % Reduktion | 20–49 | Professionelle Reinigung oder Austausch |
| Komplett blockiert | 0–19 | Austausch erforderlich |

---

### Fehlerbild 16.4 — Mischkrümmer-Korrosion

**Symptome:**
- Rostflecken am Mischkrümmer (außen).
- Weiße/grüne Ablagerungen (Salzausblühungen).
- Seewasser-Tropfen am Krümmer.
- Abgasgeruch ungewöhnlich (Seewasser-Dampf beigemischt).
- Im schlimmsten Fall: Seewasser im Ölpeilstab (milchig).

**Ursachen:**
1. Natürliche Alterung/Korrosion (Hauptursache).
2. Fehlende Zinkanode im System (beschleunigt Korrosion).
3. Mangelnder Seewasserfluss (Hot Spots durch ungleichmäßige Kühlung).
4. Leckstrom (galvanische Korrosion beschleunigt).
5. Falsches Material (Aluminium-Krümmer in Seewasser).

**AYDI-Bewertungsskala:**
| Zustand | Score | Maßnahme |
|---------|:---:|---------|
| Neuwertig, keine Korrosion | 90–100 | Jährliche Inspektion |
| Leichte Oberflächenkorrosion | 70–89 | Monitoring, Austausch in 2–5 Jahren planen |
| Deutliche Korrosion, keine Durchbrüche | 50–69 | Austausch in 1–2 Jahren, engmaschig prüfen |
| Lochfraß sichtbar, keine Undichtigkeit | 20–49 | SOFORT austauschen, Motor überwachen |
| Undichtigkeit, Seewasser tritt aus | 0–19 | KRITISCH: Motor nicht starten! Sofort tauschen |

---

### Fehlerbild 16.5 — Thermostat klemmt

**Symptome (klemmt geschlossen):**
- Motor überhitzt schnell nach Start (5–15 min).
- Seewasserfluss normal (Auspuff OK).
- Frischwasser wird nicht durch Wärmetauscher gepumpt.
- Motorblock heiß, Wärmetauscher-Rücklauf kalt.

**Symptome (klemmt offen):**
- Motor wird nie warm (bleibt unter 70 °C).
- Motorleistung reduziert.
- Erhöhter Kraftstoffverbrauch.
- Schwarzer Rauch (unvollständige Verbrennung).

**Bewertung:**
| Zustand | Score | Maßnahme |
|---------|:---:|---------|
| Thermostat funktioniert korrekt (±3 °C) | 90–100 | OK |
| Öffnung leicht verzögert (±5 °C) | 70–89 | Austausch bei nächster Wartung |
| Klemmt offen | 40–69 | Austausch empfohlen |
| Klemmt geschlossen | 0–39 | SOFORT austauschen, Motor nicht betreiben! |

---

### Fehlerbild 16.6 — Kühlmittelverlust

**Symptome:**
- Kühlmittelstand sinkt (Ausgleichsbehälter).
- Kühlmittelpfütze im Maschinenraum.
- Süßlicher Geruch (Ethylenglykol).
- Motortemperatur steigt langsam.

**Ursachen:**
1. Schlauch undicht (Alterung, Schelle locker).
2. Frischwasserpumpen-Dichtung undicht.
3. Wärmetauscher-Dichtung undicht.
4. Ausgleichsbehälter-Deckel defekt (Druck entweicht).
5. Zylinderkopfdichtung undicht (Kühlmittel → Verbrennungsraum).
6. Frostschaden (gerissener Motorblock).

**Bewertung:**
| Zustand | Score | Maßnahme |
|---------|:---:|---------|
| Kein Verlust über 30 Tage | 90–100 | OK |
| Minimaler Verlust (<50 ml/Monat) | 70–89 | Überwachen, Ursache suchen |
| Deutlicher Verlust (50–200 ml/Monat) | 50–69 | Ursache finden und beheben |
| Starker Verlust (>200 ml/Monat) | 20–49 | Sofort reparieren |
| Plötzlicher Totalverlust | 0–19 | KRITISCH: Motor nicht starten! |

---

### Fehlerbild 16.7 — Zinkanoden-Vernachlässigung

**Symptome:**
- Zinkanoden komplett aufgelöst (nichts mehr am Gewinde).
- Grüne/weiße Ablagerungen im Wärmetauscher.
- Wärmetauscher-Rohre von innen angegriffen.
- Lochfraß in Kupfer-/Bronze-Komponenten.

**Ursachen:**
1. Zinkanoden nicht gewechselt (häufigste Ursache).
2. Falsche Anoden-Materialwahl (Zink statt Magnesium in Süßwasser).
3. Leckstrom von Landstrom (beschleunigter Verbrauch).
4. Falsche/fehlende Erdung.

**Bewertung:**
| Zustand | Score | Maßnahme |
|---------|:---:|---------|
| Anode >75 % vorhanden | 90–100 | OK, nächste Kontrolle in 6 Monaten |
| Anode 50–75 % vorhanden | 70–89 | Austausch empfohlen |
| Anode 25–50 % vorhanden | 40–69 | Sofort austauschen |
| Anode <25 % oder fehlend | 0–39 | KRITISCH: Sofort tauschen, System prüfen |

---

### Fehlerbild 16.8 — Kielkühler-Bewuchs

**Symptome:**
- Motortemperatur steigt langsam über Saison.
- Kielkühler (Rohrgitter) von außen mit Muscheln/Algen bewachsen.
- Antifouling auf dem Kielkühler abgeblättert.

**Bewertung:**
| Zustand | Score | Maßnahme |
|---------|:---:|---------|
| Sauber, kein Bewuchs | 90–100 | OK |
| Leichter Algenbewuchs | 70–89 | Bei nächstem Slipgang reinigen |
| Muschelbewuchs (<50 % Fläche) | 50–69 | Reinigung erforderlich |
| Starker Bewuchs (>50 % Fläche) | 20–49 | Dringend reinigen, Antifouling erneuern |

---

### Fehlerbild 16.9 — Seewasserpumpen-Dichtungsleck

**Symptome:**
- Seewasser tropft am Pumpengehäuse.
- Seewasser in der Bilge (langsamer Einbruch).
- Geräusche: Quietschen, Schleifen (Lager).

**Ursachen:**
1. Wellendichtung (Lip Seal) verschlissen.
2. Lager ausgeschlagen → Welle exzentrisch → Dichtung zerstört.
3. O-Ring am Pumpendeckel defekt.

**Bewertung:**
| Zustand | Score | Maßnahme |
|---------|:---:|---------|
| Kein Tropfen | 90–100 | OK |
| Gelegentliches Tropfen (1× pro Minute) | 60–79 | Dichtung tauschen bei nächster Wartung |
| Permanentes Tropfen | 30–59 | Dichtung bald tauschen |
| Deutlicher Wasseraustritt | 0–29 | SOFORT reparieren, Seeventil schließen bei Liegezeit |

---

### Fehlerbild 16.10 — Schlauchversagen

**Symptome:**
- Kühlmittel oder Seewasser im Maschinenraum.
- Sichtbare Risse, Aufquellungen, Blasen am Schlauch.
- Schlauch hart und spröde (Alterung).
- Schlauch weich und aufgequollen (Ölkontakt).

**Bewertung:**
| Zustand | Score | Maßnahme |
|---------|:---:|---------|
| Flexibel, keine Risse, fest geschellt | 90–100 | OK |
| Leichte Oberflächenrisse, fest | 70–89 | Austausch in 1–2 Jahren planen |
| Tiefe Risse, Aufquellung, hart | 40–69 | Baldiger Austausch |
| Undichtigkeit an Schelle/Riss | 0–39 | SOFORT austauschen |

---

### Fehlerbild 16.11 — Elektrolyse im Wärmetauscher

**Symptome:**
- Wärmetauscher-Rohre von innen angegriffen trotz guter Zinkanoden.
- Zinkanoden werden ungewöhnlich schnell verbraucht (in <3 Monaten).
- Grünliche Verfärbung am Wärmetauscher.
- Andere Metall-Komponenten zeigen Korrosion.

**Ursachen:**
1. Leckstrom von Landstromanlage.
2. Galvanischer Isolator fehlt oder defekt.
3. Erdung des Motors defekt.
4. Unterschiedliche Metalle ohne galvanische Trennung.
5. Nachbarboot mit Erdungsproblem (über Hafenwasser).

**Bewertung:**
| Zustand | Score | Maßnahme |
|---------|:---:|---------|
| Kein Elektrolyse-Anzeichen | 90–100 | OK |
| Leichte Anzeichen, Anoden halten >6 Monate | 70–89 | Erdung und Landstrom prüfen |
| Deutliche Korrosion, Anoden <6 Monate | 40–69 | Galvanischen Isolator installieren, Erdung prüfen |
| Schwere Korrosion, Anoden <3 Monate | 0–39 | SOFORT: Elektriker beauftragen, Isolator, Erdung |

---

### Fehlerbild 16.12 — Luftschloss (Air Lock) im Kühlsystem

**Symptome:**
- Motor überhitzt trotz funktionierendem Seewasserkreislauf.
- Frischwasserpumpe macht ungewöhnliche Geräusche (gurgeln, kavitieren).
- Kühlmittelstand schwankt oder fällt nach Arbeiten am System.
- Kein oder ungleichmäßiger Durchfluss im Frischwasserkreislauf.

**Ursachen:**
1. Nach Kühlmittelwechsel nicht korrekt entlüftet.
2. Nach Thermostat-Tausch Luft im System.
3. Undichte Zylinderkopfdichtung (Abgase drücken Luft ins Kühlsystem).
4. Undichter Ausgleichsbehälter-Deckel (saugt Luft an).
5. Schlauch undicht auf der Saugseite der Frischwasserpumpe.

**Entlüftung:**
1. Motor kalt, Ausgleichsbehälter-Deckel öffnen.
2. Entlüftungsschraube am höchsten Punkt des Systems öffnen
   (meist am Thermostatgehäuse oder am Zylinderkopf).
3. Motor starten und auf Leerlauf laufen lassen.
4. Warten, bis blasenfreies Kühlmittel aus der Entlüftung kommt.
5. Entlüftung schließen.
6. Kühlmittel im Ausgleichsbehälter nachfüllen.
7. Motor warmlaufen lassen, auf Temperatur und Blasen achten.

**Bewertung:**
| Zustand | Score | Maßnahme |
|---------|:---:|---------|
| Kein Luftproblem | 90–100 | OK |
| Luft nach Wartungsarbeiten | 70–89 | Entlüften |
| Wiederkehrende Luft ohne erkennbare Ursache | 40–69 | Zylinderkopfdichtung prüfen! |
| Dauerhaftes Luftproblem | 0–39 | Systematische Ursachensuche, ggf. Zylinderkopf-Test |

---
---

## 17. Troubleshooting

### Troubleshooting-Baum 17.1 — Motor überhitzt

```
Motor überhitzt (Temperatur >95 °C)
│
├── Seewasser fließt NICHT am Auspuff
│   ├── Seeventil geschlossen?
│   │   └── JA → Seeventil öffnen. Problem gelöst.
│   ├── Seewasserfilter verstopft?
│   │   └── JA → Filter reinigen. Weiterfahren.
│   ├── Impeller defekt?
│   │   └── JA → Impeller tauschen. Flügel suchen!
│   ├── Seewasserschlauch geknickt/blockiert?
│   │   └── JA → Schlauch prüfen/tauschen.
│   └── Seewasserpumpe defekt (Gehäuse, Welle)?
│       └── JA → Pumpe reparieren/tauschen.
│
├── Seewasser fließt NORMAL am Auspuff
│   ├── Thermostat klemmt geschlossen?
│   │   └── Prüfung: Thermostat ausbauen, Motor ohne Thermostat
│   │       laufen → Temperatur normal? → Thermostat tauschen.
│   ├── Wärmetauscher Frischwasserseite verstopft?
│   │   └── Prüfung: Frischwasserkreislauf spülen.
│   ├── Frischwasserpumpe defekt?
│   │   └── Prüfung: Durchfluss am Wärmetauscher-Rücklauf prüfen.
│   ├── Luftschloss im Frischwasserkreislauf?
│   │   └── Prüfung: System entlüften.
│   └── Kühlmittelverlust?
│       └── Prüfung: Ausgleichsbehälter, Schläuche, Dichtungen.
│
└── Seewasser fließt SCHWACH am Auspuff
    ├── Wärmetauscher Seewasserseite verkalkt?
    │   └── Chemische + mechanische Reinigung.
    ├── Impeller teilweise defekt (einzelne Flügel fehlen)?
    │   └── Impeller tauschen, Fragmente suchen.
    ├── Ölkühler oder Ladeluftkühler verstopft?
    │   └── Prüfen und reinigen.
    └── Borddurchlass teilweise blockiert (Bewuchs)?
        └── Reinigen (Taucher oder Slip).
```

---

### Troubleshooting-Baum 17.2 — Kein Seewasser am Auspuff

```
Kein Seewasser am Auspuff (SOFORT Motor aus!)
│
├── Seeventil überprüfen
│   ├── Geschlossen → Öffnen. Motor starten.
│   └── Offen → Weiter prüfen.
│
├── Seewasserfilter prüfen
│   ├── Verstopft → Reinigen. Motor starten.
│   └── Sauber → Weiter prüfen.
│
├── Impeller prüfen
│   ├── Defekt (Flügel fehlen/gebrochen) → Tauschen. Fragmente suchen.
│   ├── Verschlissen (kein Vakuum) → Tauschen.
│   └── OK → Weiter prüfen.
│
├── Seewasserleitungen prüfen
│   ├── Knick → Begradigen oder tauschen.
│   ├── Verstopft (Muschel, Gegenstand) → Freiblasen/reinigen.
│   └── OK → Weiter prüfen.
│
├── Wärmetauscher-Seite prüfen
│   ├── Komplett verstopft → Endkappen öffnen, Rohre reinigen.
│   └── OK → Weiter prüfen.
│
└── Seewasserpumpe prüfen
    ├── Pumpengehäuse gerissen → Tauschen.
    ├── Welle gebrochen → Tauschen.
    └── Antrieb defekt (Keilriemen, Zahnrad) → Reparieren.
```

---

### Troubleshooting-Baum 17.3 — Motor wird nicht warm

```
Motor bleibt unter 70 °C
│
├── Einkreis-Motor?
│   └── JA → Normal für Einkreis. Umrüstung auf Zweikreis empfehlen.
│
├── Zweikreis-Motor?
│   ├── Thermostat prüfen
│   │   ├── Klemmt offen → Thermostat tauschen.
│   │   ├── Fehlt (wurde ausgebaut) → Einbauen!
│   │   └── OK → Weiter prüfen.
│   │
│   ├── Thermostat-Bypass prüfen
│   │   └── Bypass-Leitung zu groß/offen? → Einstellen/verschließen.
│   │
│   └── Wärmetauscher zu groß dimensioniert?
│       └── Seltener Fall, normalerweise kein Problem.
│
└── Kielkühlung?
    └── Thermostat prüfen (wie Zweikreis).
```

---

### Troubleshooting-Baum 17.4 — Kühlmittel milchig/emulsionsartig

```
Kühlmittel ist milchig/bräunlich
│
├── Ölkühler-Leckage prüfen
│   ├── Öl im Kühlmittel UND Kühlmittel im Öl?
│   │   └── JA → Ölkühler defekt. Sofort tauschen.
│   └── Nur Kühlmittel milchig, Öl OK?
│       └── Weiter prüfen.
│
├── Zylinderkopfdichtung prüfen
│   ├── CO₂-Test im Ausgleichsbehälter (Testflüssigkeit, 30 EUR)
│   │   ├── Positiv (Farbe schlägt um) → ZKD defekt. Motor nicht
│   │   │   betreiben. Reparaturkosten: 1.500–4.000 EUR.
│   │   └── Negativ → Weiter prüfen.
│   └── Druckprüfung Kühlsystem (Pumpe, 50–100 EUR)
│       ├── Druck fällt ab → Undichtigkeit → Ort finden.
│       └── Druck hält → Unklare Ursache, Fachbetrieb.
│
└── Korrosion im System?
    └── Altes Kühlmittel (>5 Jahre)? → Spülen und wechseln.
```

---

### Troubleshooting-Baum 17.5 — Ungewöhnlicher Auspuff (weiß/dampfig)

```
Weißer Rauch/Dampf aus dem Auspuff
│
├── Nur bei Kaltstart (verschwindet nach 5 min)?
│   └── Normal: Kondenswasser verdampft. Kein Problem.
│
├── Dauerhaft weißer Rauch?
│   ├── Süßlicher Geruch (Glykol)?
│   │   └── Zylinderkopfdichtung defekt → CO₂-Test.
│   │       Kühlmittel gelangt in den Verbrennungsraum.
│   ├── Kein besonderer Geruch, viel Dampf?
│   │   └── Seewasser im Zylinder möglich → Mischkrümmer prüfen.
│   └── Ölige Tropfen im weißen Rauch?
│       └── Turbolader-Dichtung oder Ventilschaftdichtung.
│
└── Nur unter Last weißer Rauch?
    └── Ladeluftkühler undicht (Seewasser in Ladeluft) → Prüfen.
```

---
---

## 18. FAQ

### Grundlagen

**F01: Wie oft muss ich den Impeller wechseln?**
A: Mindestens jährlich oder alle 500 Betriebsstunden (was zuerst
eintritt). Bei Charterbooten oder Langfahrt: alle 300–400 h. Immer
einen Ersatz-Impeller an Bord haben (inkl. O-Ring und Impeller-Abzieher).

**F02: Kann ich Leitungswasser als Kühlmittel verwenden?**
A: Nur in Kombination mit Kühlmittel-Konzentrat (Glykol + Inhibitoren).
Niemals nur Leitungswasser — es enthält Kalk und bietet keinen
Korrosionsschutz. Idealerweise destilliertes Wasser + Konzentrat.

**F03: Was passiert, wenn ich den Motor ohne Seewasser starte?**
A: Der Impeller läuft trocken und wird in 15–30 Sekunden zerstört.
Außerdem steigt die Abgastemperatur schnell (kein Nassdämpfer mehr),
was den Auspuffschlauch und Wassersammler beschädigen kann. Motor
sofort abstellen!

**F04: Wie erkenne ich, dass der Wärmetauscher getauscht werden muss?**
A: Wenn die Motortemperatur trotz gereinigtem Wärmetauscher, neuem
Impeller und funktionierendem Thermostat im oberen Bereich bleibt
(>90 °C), ist der Wärmetauscher vermutlich intern korrodiert und muss
getauscht werden. Ultraschall-Wandstärkenmessung gibt Sicherheit.

**F05: Muss ich das Seeventil bei Liegezeit schließen?**
A: JA. Alle Seeventile, die nicht aktiv gebraucht werden (z.B.
Bilgenpumpe), sollten bei Abwesenheit geschlossen sein. Ein geplatzter
Schlauch bei offenem Seeventil = sinkendes Boot. Versicherungen
können bei offenen Seeventilen die Regulierung kürzen.

### Wartung

**F06: Wie reinige ich den Wärmetauscher selbst?**
A: Seewasserseite: Endkappen abschrauben, Rohre mit Nylonbürste
reinigen, chemisch einweichen (Rydlyme, Barnacle Buster oder
Essigessenz 10 % für 2–4 h). Gründlich spülen. Zinkanode prüfen.
Frischwasserseite: Kühlmittel ablassen, mit Reiniger (Prestone Flush)
und Wasser spülen, neues Kühlmittel einfüllen.

**F07: Wie oft muss ich das Kühlmittel wechseln?**
A: IAT (grün, konventionell): alle 2 Jahre. OAT (orange/rosa): alle
5 Jahre. HOAT (gelb/türkis): alle 3–5 Jahre. Unabhängig davon bei
sichtbarer Verschmutzung, Verfärbung oder pH-Wert <7,0 wechseln.

**F08: Kann ich verschiedene Kühlmittel mischen?**
A: NEIN. Nicht IAT mit OAT mischen (kann zu Gelbildung und Verstopfung
führen). Nicht verschiedene Farben mischen (Farbe ≠ Typ, aber als
Faustregel hilfreich). Im Notfall: lieber mit destilliertem Wasser
auffüllen und bei nächster Gelegenheit komplett wechseln.

**F09: Wie prüfe ich die Zinkanode im Wärmetauscher?**
A: Endkappe abschrauben (eine Schraube), Anode herausdrehen. Wenn
<50 % des Originals vorhanden → tauschen. In Tropen/Mittelmeer alle
6 Monate, in der Ostsee jährlich prüfen.

**F10: Mein Motor hat keine Zinkanode im Kühlsystem — ist das normal?**
A: Einige kleine Motoren (Yanmar 1GM, Bukh DV10) haben keine
werksseitige Zinkanode im Wärmetauscher. Das ist designbedingt, aber
eine Nachrüstung (falls der Wärmetauscher eine Aufnahme hat) wird
empfohlen.

### Probleme

**F11: Mein Motor überhitzt nach 15 Minuten — was tun?**
A: Sofort-Check: 1) Seeventil offen? 2) Seewasserfilter sauber?
3) Impeller OK? 4) Seewasserfluss am Auspuff prüfen. Wenn Seewasser
fließt: Thermostat prüfen (klemmt geschlossen?). Wenn nicht: Impeller
tauschen. Siehe Troubleshooting-Baum 17.1.

**F12: Seewasser am Mischkrümmer — wie schlimm ist das?**
A: SEHR schlimm. Seewasser am Mischkrümmer bedeutet Durchkorrosion.
Es besteht akute Gefahr, dass Seewasser in den Motor zurückfließt
(Hydrolock). Motor sofort abstellen, Mischkrümmer tauschen, Motor
auf Seewassereintritt prüfen (Öl- und Zylindercheck).

**F13: Kühlmittel auf dem Ölpeilstab — was bedeutet das?**
A: Kühlmittel im Motoröl (milchig/emulsionsartig am Peilstab) →
Motor SOFORT abstellen. Mögliche Ursachen: Ölkühler undicht,
Zylinderkopfdichtung defekt, Motorblock gerissen. Professionelle
Diagnose erforderlich. Kosten: 500–8.000 EUR je nach Ursache.

**F14: Kann ich ohne Thermostat weiterfahren?**
A: Als Notlösung kurzzeitig ja — der Motor läuft dann wie ein
Einkreis-Motor (zu kalt, aber nicht überhitzt). Auf Dauer schädlich:
schlechte Verbrennung, Verglasung, Kondenswasser, erhöhter Verschleiß.
Thermostat baldmöglichst ersetzen.

**F15: Was kostet ein komplett neues Kühlsystem?**
A: Für einen typischen 40–50-PS-Motor (z.B. Yanmar 3JH, Volvo D2-40):
Wärmetauscher (400–800 EUR), Mischkrümmer (300–800 EUR), Impeller +
Pumpe (50–200 EUR), Thermostat (25–50 EUR), Schläuche + Schellen
(100–200 EUR), Zinkanoden (10–30 EUR), Kühlmittel (20–40 EUR).
Gesamt: 900–2.200 EUR Material, zzgl. 6–12 h Arbeit (500–1.500 EUR).

### Spezial

**F16: Ich fahre im Süßwasser — brauche ich trotzdem Zinkanoden?**
A: Ja, aber Magnesium- statt Zinkanoden. Zink bietet in Süßwasser
wenig Schutz (zu geringe Spannungsdifferenz). Aluminium-Anoden sind
eine universelle Alternative.

**F17: Ist Kielkühlung besser als Zweikreis-Kühlung?**
A: Kommt auf den Einsatzzweck an. Kielkühlung: ideal für
Langfahrt, schmutziges Wasser, Arbeitsboote, extreme Zuverlässigkeit.
Zweikreis: günstiger, kompakter, Standard für die meisten Yachten.
Kielkühlung ist wartungsärmer, aber teurer in der Installation und
kann nicht einfach nachgerüstet werden.

**F18: Kann ich den Seewasserkreislauf mit einem Elektromotor pumpen?**
A: Ja, es gibt elektrische Seewasserpumpen (z.B. Jabsco 12V/24V).
Vorteil: Unabhängig von der Motordrehzahl, kein Impeller am Motor.
Nachteil: Braucht zuverlässige Stromversorgung, zusätzliche Ausfallquelle.
In der Praxis selten bei Hauptantrieben, häufiger bei Generatoren.

**F19: Mein Boot hat einen Trockenauspuff — brauche ich trotzdem
Seewasser?**
A: Für den Auspuff nicht, aber für den Wärmetauscher (Zweikreis) oder
die Motorkühlung schon — es sei denn, Sie haben zusätzlich eine
Kielkühlung. Ein Trockenauspuff allein spart nur den Mischkrümmer und
den Seewasser-Anteil im Auspuffsystem.

**F20: Wie erkenne ich einen Frostschaden am Motor?**
A: Risse im Motorblock (meist am Frost-Pfropfen / Core Plug oder an
der dünnsten Stelle des Kühlmantels). Frostpfropfen können
herausgedrückt werden. Zylinderkopf kann sich verziehen. Im
Frühjahr: System mit Druck prüfen (1,5 bar, 15 min halten).
Wenn Druck fällt → Frostschaden wahrscheinlich.

**F21: Was ist ein Schwanenhals (Gooseneck) und warum ist er wichtig?**
A: Ein Schwanenhals ist eine nach oben gebogene Schleife im
Auspuffschlauch. Er verhindert, dass bei Seegang Seewasser über den
Auspuff in den Motor gedrückt wird. Mindesthöhe: 300 mm über
Wasserlinie. Pflicht bei Nassauspuff!

**F22: Kann ich Antifouling auf den Kielkühler streichen?**
A: Ja, aber nur kompatibles Antifouling. Kupferhaltiges Antifouling
auf CuNi-Kühlern kann galvanische Korrosion beschleunigen. Empfohlen:
Hempel Mille NCT oder International Trilux 33 (kupferfrei für CuNi).

**F23: Wie erkenne ich Entzinkung an einem Bronze-Seeventil?**
A: Entzinktes Messing/Bronze wird kupferfarben (rötlich) statt
goldgelb. Die Oberfläche ist rau und porös. Kratztest: Normales
Bronze/Messing zeigt goldgelbe Kratzspur. Entzinktes Material zeigt
rötlich-kupferne Spur. Bei Verdacht: Sofort tauschen!

**F24: Was ist der Unterschied zwischen Mischkrümmer und Auspuffkrümmer?**
A: Der Auspuffkrümmer (Exhaust Manifold) sitzt direkt am Zylinderkopf
und sammelt die Abgase. Er ist trocken (kein Seewasser). Der
Mischkrümmer (Mixing Elbow, Injection Elbow) ist der Punkt, an dem
Seewasser in den Abgasstrom eingespritzt wird. Oft sind beide in einem
Bauteil kombiniert.

**F25: Wie lange kann ich mit einem defekten Impeller noch fahren?**
A: Gar nicht. Ohne Impeller kein Seewasser → innerhalb von 5–15 Minuten
Überhitzung → Motorschaden. Einen Ersatz-Impeller, passende O-Ringe
und ein Impeller-Abzieher-Werkzeug gehören auf jedes Boot.

**F26: Mein Motor startet nach dem Winter nicht, und es tropft Wasser
aus dem Auspuff — was ist passiert?**
A: Wahrscheinlich Frostschaden und/oder Seewasser ist über den
Mischkrümmer in die Zylinder gelaufen. NICHT starten (Hydrolock-Gefahr)!
Glühkerzen/Einspritzdüsen herausschrauben, Motor von Hand
durchdrehen. Wenn Wasser aus den Zylindern kommt: Motor muss
professionell geprüft werden.

### Materialien und Produkte

**F27: Welche Impeller-Marke ist die beste?**
A: Jabsco (ITT) und Johnson (SPX Flow) sind die beiden Marktführer
und liefern vergleichbare Qualität. Für die meisten Motoren sind beide
als OEM-Zulieferer aktiv. Aftermarket-Impeller von CEF, Recmar oder
Sierra sind günstiger (50–70 % des OEM-Preises), bieten aber teils
kürzere Lebensdauer. Für Langfahrt und Charterboote: Immer
OEM-Qualität verwenden.

**F28: Kann ich einen Edelstahl-Mischkrümmer selbst einbauen?**
A: Grundsätzlich ja, wenn Sie über Grundkenntnisse verfügen. Der Einbau
erfordert: Entfernung des alten Krümmers (oft festgerostete Schrauben
→ Kriechöl, Wärme), neue Dichtungen, korrekte Schrauben-Anzugsmomente
und eine Dichtheitsprüfung nach dem Einbau. Wenn die Stehbolzen am
Auspuffkrümmer abbrechen, wird es schnell komplex → dann Fachbetrieb.
Einbauzeit Fachmann: 2–4 Stunden. Eigenleistung: 3–6 Stunden.

**F29: Welches Dichtmittel für Kühlsystem-Anschlüsse?**
A: Für Verschraubungen: Hylomar Universal Blue (nicht aushärtend,
temperaturbeständig bis 250 °C, lösungsmittelfrei). Für Flansch-
dichtungen: Original-Papierdichtung oder Dichtmasse. KEIN Teflonband
an Kühlsystem-Gewinden (kann sich lösen und Durchfluss blockieren).
KEIN Silikon (wird vom Kühlmittel angegriffen).

**F30: Welches Antifouling für den Borddurchlass des Seewassereinlasses?**
A: Gleich wie für den Rumpf, aber achten Sie auf Kompatibilität.
Bei Bronze-Borddurchlässen: Standard-Kupfer-Antifouling OK. Bei
Kunststoff-Borddurchlässen (TruDesign/Marelon): Kein zinnhaltiges
Antifouling. Eine dünne Schicht direkt am Borddurchlass reduziert
Bewuchs erheblich und verhindert Blockaden.

### Kosten und Planung

**F31: Was kostet die jährliche Kühlsystem-Wartung bei einer Werft?**
A: Für einen typischen 30–50-PS-Motor (z.B. Yanmar 3JH, Volvo D1/D2):
- Impeller-Wechsel: 150–250 EUR (inkl. Material + Arbeit)
- Zinkanoden tauschen: 50–100 EUR
- Seewasserfilter reinigen: 0–30 EUR
- Kühlmittelstand/-zustand prüfen: im Service enthalten
- Mischkrümmer-Sichtprüfung: im Service enthalten
- Gesamt jährliche Routine: 200–400 EUR bei Werft
- Eigenleistung: 50–120 EUR (nur Material)

**F32: Lohnt sich eine Umrüstung auf Kielkühlung?**
A: Wirtschaftlich lohnt sich die Umrüstung selten — die Kosten liegen
bei 4.000–10.000 EUR (Material + Rumpfarbeiten + Installation). Sie
rechnet sich nur, wenn: (a) Sie in sehr schmutzigem Wasser fahren
(dauerhafte Impeller-/Filterverstopfung), (b) Sie eine Langfahrt
planen, bei der Ersatzteile nicht verfügbar sind, (c) Sie ein
Stahlboot haben, bei dem Kielkühler-Schweißarbeiten einfach sind.
Bei Neubau/Refit ist der Aufpreis deutlich geringer.

**F33: Mein Wärmetauscher ist undicht — reparieren oder tauschen?**
A: Kommt auf den Schaden an. Einzelnes undichtes Rohr: Kann durch
Verstopfen (Pfropfen in das Rohrende treiben) temporär repariert
werden — reduziert aber die Kühlleistung. Undichte Rohrböden: Können
von spezialisierten Firmen gelötet/geschweißt werden (200–500 EUR).
Allgemein: Wenn der Wärmetauscher >10 Jahre alt ist und Rohr-Lochfraß
zeigt, ist ein Austausch langfristig günstiger als eine Reparatur.

**F34: Gibt es universelle Wärmetauscher oder muss ich OEM kaufen?**
A: Bowman (UK) und Fernstrum (USA) bieten universelle Wärmetauscher
an, die über Adapter an verschiedene Motoren passen. Die Anschluss-
maße (Gewinde, Flansche) müssen natürlich übereinstimmen. Bowman hat
ein umfangreiches Austauschprogramm mit Cross-Referenz zu den meisten
OEM-Nummern. Preisvorteil gegenüber OEM: 20–40 %.

### Betrieb und Praxis

**F35: Mein Motor läuft im Mittelmeer heißer als in der Ostsee — normal?**
A: Ja, absolut normal. Die Seewassertemperatur beeinflusst die
Motortemperatur direkt. Ostsee im Sommer: 16–20 °C → Motor bei
82–86 °C. Mittelmeer im Sommer: 26–30 °C → Motor bei 88–94 °C.
Solange die Temperatur unter 95 °C bleibt, ist das unkritisch.
Bei dauerhaft >92 °C im Mittelmeer: Wärmetauscher reinigen,
Impeller-Zustand prüfen.

**F36: Wie lange dauert es, bis ein Motor nach Kaltstart
Betriebstemperatur erreicht?**
A: Zweikreis-Motor: 8–15 Minuten bei Leerlauf, 5–8 Minuten unter
Last. Einkreis-Motor: Erreicht selten volle Betriebstemperatur (nur
50–65 °C). Kielkühlung: Wie Zweikreis, ggf. etwas langsamer (größeres
Kühlvolumen). Bei sehr kaltem Wasser (<5 °C) kann es 15–25 Minuten
dauern. Motor nicht unter Volllast fahren, bevor er Betriebstemperatur
erreicht hat.

**F37: Muss ich den Motor warmlaufen lassen vor Volllast?**
A: Ja, mindestens bis der Thermostat öffnet (Motortemperatur erreicht
Sollwert). Kaltlast schadet dem Motor: enge Toleranzen im kalten
Zustand → erhöhter Verschleiß. Faustregel: 5 Minuten Leerlauf oder
niedrige Drehzahl, dann langsam steigern. Nicht auf Volllast, bevor
Öltemperatur >60 °C und Kühlwassertemperatur >70 °C.

**F38: Kann ich den Seewasserfilter während der Fahrt reinigen?**
A: Bei einem Standard-Einzelfilter: Nein — Seeventil muss geschlossen
werden, und ohne Seewasser überhitzt der Motor. Bei einem Duplex-Filter
(Umschaltfilter): Ja — auf den zweiten Filter umschalten, dann den
ersten reinigen. Investition Duplex: 280–650 EUR. Lohnt sich besonders
für Langstrecken und Reviere mit viel Treibgut.

**F39: Wie stark darf der Motor bei Seegang belastet werden, wenn
die Motortemperatur erhöht ist?**
A: Bei erhöhter Temperatur (90–95 °C) Drehzahl um 200–300 U/min
reduzieren und Ursache suchen. Bei Alarmtemperatur (>100 °C): sofort
auf Leerlauf und prüfen. Nie mit Alarm weiterfahren — der Schaden
steigt exponentiell mit der Temperatur über dem Grenzwert.

**F40: Wie überprüfe ich den korrekten Seewasser-Durchfluss?**
A: Einfachste Methode: Sichtfenster am Auspuff — Seewasser muss
gleichmäßig und kräftig ausströmen. Quantitativ: Auspuffschlauch
kurzzeitig in Eimer leiten und Literleistung pro Minute messen.
Sollwert: ca. 1–1,2 l/min pro PS. Beispiel: 40-PS-Motor → 40–48 l/min.
Wenn deutlich weniger → Wärmetauscher oder Impeller prüfen.

---
---

## 19. Glossar

| Begriff | Erklärung |
|---------|-----------|
| Ausgleichsbehälter | Expansion Tank. Druckbehälter im Frischwasserkreislauf für Volumenausgleich und Entlüftung. |
| Antifouling | Bewuchsschutzbeschichtung am Unterwasserschiff und ggf. Kielkühler. |
| Approach Temperature | Temperaturdifferenz zwischen Frischwasser-Austritt und Seewasser-Eintritt am Wärmetauscher. Maß für Wärmetauscher-Effizienz. |
| Bilge | Tiefster Punkt im Boot, wo sich Leckwasser sammelt. |
| Borddurchlass | Through-Hull / Skin Fitting. Durchführung durch den Rumpf unterhalb der Wasserlinie. |
| Box Cooler | Kielkühler-Typ in einem am Rumpf montierten, zum Wasser offenen Kasten. |
| Bypass | Kurzschlussleitung, die den Wärmetauscher umgeht, wenn der Thermostat geschlossen ist. |
| CE-Kategorie | Klassifizierung nach EU-Richtlinie 2013/53/EU: A (Ozean), B (Offshore), C (Küste), D (geschützt). |
| CuNi 90/10 | Kupfer-Nickel-Legierung (90 % Cu, 10 % Ni). Standardmaterial für seewasserbeständige Komponenten. |
| Doppelschelle | Zwei Schlauchschellen pro Anschluss — Pflicht unterhalb der Wasserlinie. |
| DZR | Dezincification Resistant. Messinglegierung mit Zusätzen (Arsen), die Entzinkung verhindert. |
| Einkreis-Kühlung | Raw Water Cooling / Direct Cooling. Seewasser fließt direkt durch den Motor. |
| Elektrolyse | Galvanische Korrosion durch elektrische Ströme (Leckstrom, unterschiedliche Metalle). |
| Entzinkung | Dezincification. Selektive Korrosion, bei der Zink aus Messing gelöst wird → sprödes Material. |
| EPDM | Ethylen-Propylen-Dien-Monomer. Standard-Gummimaterial für Kühlschläuche. |
| Ethylenglykol | Standard-Frostschutzmittel. GIFTIG. |
| Frischwasserkreislauf | Geschlossener Kühlkreislauf mit Kühlmittel (Wasser + Glykol). |
| Galvanischer Isolator | Gerät, das Leckstrom von der Landstromversorgung blockiert, ohne den Schutzleiter zu unterbrechen. |
| Gleitringdichtung | Mechanical Seal. Dichtung in der Frischwasserpumpe zwischen Welle und Gehäuse. |
| Gooseneck | Schwanenhals. Nach oben gebogene Schleife im Auspuffschlauch. |
| Grid Cooler | Kielkühler-Typ mit Rohrgitter am Rumpf (Fernstrum). |
| Heat Exchanger | Wärmetauscher. Überträgt Wärme zwischen zwei Kreisläufen ohne Vermischung. |
| HOAT | Hybrid Organic Acid Technology. Kühlmittel-Typ mit kombinierten Inhibitoren. |
| Hydrolock | Hydraulischer Kolbenstillstand. Wasser im Zylinder verhindert Kompression → Pleuelbruch. |
| IAT | Inorganic Additive Technology. Konventionelles Kühlmittel mit mineralischen Inhibitoren. |
| Impeller | Flexibles Gummi-Schaufelrad in der Seewasserpumpe. |
| Injection Elbow | Mischkrümmer. Punkt der Seewasser-Einspritzung in den Abgasstrom. |
| Intercooler | Ladeluftkühler. Kühlt die komprimierte Ladeluft eines Turboladers. |
| Kielkühlung | Keel Cooling. Geschlossenes Kühlsystem mit Wärmeabgabe über am Rumpf montierte Kühler. |
| Kühlmittel | Coolant. Mischung aus Wasser, Glykol und Korrosionsinhibitoren. |
| Lochfraß | Pitting. Lokale, tiefe Korrosion, die Löcher in der Materialoberfläche erzeugt. |
| Marelon | Glasfaserverstärktes Nylon für korrosionsfreie Marine-Armaturen (Forespar). |
| Mischkrümmer | Mixing Elbow. Bauteil, an dem Seewasser in den Abgasstrom eingespritzt wird. |
| Nassdämpfer | Wet Exhaust. Auspuffsystem, bei dem Seewasser die Abgase kühlt und dämpft. |
| Ni-Resist | Nickelbasis-Gusseisen. Korrosionsbeständiges Material für Mischkrümmer. |
| OAT | Organic Acid Technology. Langzeit-Kühlmittel mit organischen Inhibitoren. |
| Opferanode | Zinkanode. Unedleres Metall, das anstelle der wertvollen Komponenten korrodiert. |
| Propylenglykol | Ungiftiges Frostschutzmittel (Lebensmittelqualität). Für Seewasser-Winterfestmachung. |
| Refraktometer | Messgerät für Glykol-Konzentration anhand des Brechungsindex. |
| Rohrbündel | Tube Bundle. Paket dünner Rohre im Wärmetauscher. |
| Schwanenhals | Gooseneck. Aufwärts gebogener Auspuffabschnitt oberhalb der Wasserlinie. |
| Seacock | Seeventil. Absperrhahn am Borddurchlass. |
| Seewasserkreislauf | Offener Kühlkreislauf mit Seewasser. |
| Shell-and-Tube | Rohrbündel-Wärmetauscher mit zylindrischem Gehäuse (Mantel). |
| Skin Cooler | Kielkühler-Typ mit Kühlrohren im Rumpf integriert. |
| Strainer | Seewasserfilter. Filtert Partikel vor der Impeller-Pumpe. |
| Thermostat | Temperaturgesteuertes Ventil (Wachselement) zur Regelung der Motortemperatur. |
| Trockenauspuff | Dry Exhaust. Isoliertes Auspuffrohr ohne Seewasser-Kühlung. |
| TruDesign | Neuseeländischer Hersteller von Kunststoff-Seeventilen und -Borddurchlässen. |
| Tube Sheet | Rohrboden im Wärmetauscher. Hält und trennt die Rohre. |
| Verschleißplatte | Wear Plate. Auswechselbare Platte in der Impeller-Pumpe. |
| Wachselement | Wax Element. Temperatursensor im Thermostat, der sich bei Erwärmung ausdehnt. |
| Wassersammler | Waterlock. Auspuff-Schalldämpfer und Rückflusssperre. |
| Zinkanode | Zinc Anode. Opferanode aus Zink zum Korrosionsschutz in Seewassersystemen. |
| Zweikreis-Kühlung | Indirect Cooling. Getrennte Kühlkreisläufe mit Wärmetauscher. |
| Abgasgegendruck | Exhaust Back Pressure. Widerstand im Auspuffsystem, der die Abgase bremst. Zu hoch bei verstopftem Wassersammler. |
| Antikavitationsplatte | Platte an der Impeller-Pumpe, die Kavitation durch Luftblasen verhindert. |
| Cavitation | Kavitation. Dampfblasenbildung in der Pumpe durch Unterdruck. Zerstört Impeller und Gehäuse. |
| Core Plug | Frostpfropfen / Kernstopfen. Metallscheiben im Motorblock, die bei Frost herausgedrückt werden (Sollbruchstelle). |
| Cross-Flow | Kreuzstrom-Wärmetauscher. Medien fließen rechtwinklig zueinander. |
| Counter-Flow | Gegenstrom-Wärmetauscher. Medien fließen entgegengesetzt. Höchste Effizienz. |
| Druckausgleichsventil | Ventil im Ausgleichsbehälter-Deckel, das Überdruck ablässt. |
| Exzentrizität | Versatz der Impeller-Achse im Pumpengehäuse. Erzeugt die Pumpwirkung. |
| Frostpfropfen | Core Plug. Weiche Metallscheibe im Motorblock, gibt bei Frost nach → Schutz vor Blockriss. |
| Galvanische Reihe | Elektrochemische Spannungsreihe der Metalle in Seewasser. Bestimmt, welches Metall als Opfer korrodiert. |
| Korrosionsinhibitor | Chemischer Zusatz im Kühlmittel, der Metalloberflächen vor Korrosion schützt. |
| Lippendichtung | Lip Seal. Einfache Wellendichtung an der Seewasserpumpe. |
| Nachkühler | Aftercooler. Alternativer Begriff für Ladeluftkühler (Intercooler). |
| O-Ring | Ringförmige Elastomer-Dichtung. Standard-Dichtung an Pumpendeckeln und Endkappen. |
| Passivschicht | Dünne Oxidschicht auf Edelstahl oder CuNi, die vor weiterer Korrosion schützt. |
| Plattenwärmetauscher | Plate Heat Exchanger. Wärmetauscher aus parallelen, gewellten Platten. |
| Rohrboden | Tube Sheet. Metallplatte, in die die Wärmetauscher-Rohre eingesetzt sind. |
| Spaltkorrosion | Crevice Corrosion. Korrosion in engen Spalten (z.B. unter Schlauchschellen). Betrifft besonders Edelstahl. |
| Tee-Staining | Teeflecken-Korrosion. Bräunliche Verfärbung auf Edelstahl in Seewasserumgebung. |
| Temperaturlogger | Elektronisches Gerät zur kontinuierlichen Aufzeichnung der Motortemperatur. |
| Ultraschall-Dickenmessung | Zerstörungsfreie Messung der Wandstärke von Metall-Komponenten mittels Ultraschall. |
| Verdränger-Pumpe | Positive Displacement Pump. Pumpentyp, der ein festes Volumen pro Umdrehung fördert (z.B. Impeller-Pumpe). |
| Volumenstrom | Durchflussrate. Menge an Kühlmittel/Seewasser pro Zeiteinheit (l/min). |
| Wärmedurchgangskoeffizient | k-Wert. Maß für die Effizienz eines Wärmetauschers (kW/m²·K). |
| Wärmeleistung | Thermische Leistung, die über das Kühlsystem abgeführt werden muss (kW). |

---
---

## 20. Schnell-Referenz

### 20.1 Wartungsintervalle auf einen Blick

| Komponente | Intervall | Eigenleistung? | Kosten (EUR) |
|-----------|----------|:-:|:---:|
| Impeller | Jährlich / 500 h | Ja | 25–90 |
| Zinkanode Wärmetauscher | Halbjährlich / jährlich | Ja | 5–25 |
| Zinkanode Ölkühler | Halbjährlich / jährlich | Ja | 5–15 |
| Seewasserfilter reinigen | Monatlich / vor jedem Start | Ja | 0 |
| Kühlmittelstand prüfen | Monatlich | Ja | 0 |
| Kühlmittel-Konzentration | Jährlich | Ja | 0 (Refraktometer 15–40) |
| Thermostat | 3–5 Jahre | Ja | 20–60 |
| Schläuche + Schellen | 5–8 Jahre | Ja | 50–200 |
| Wärmetauscher reinigen | Jährlich (chemisch) | Ja | 15–80 |
| Wärmetauscher tauschen | 8–15 Jahre | Werft empf. | 300–1.500 |
| Mischkrümmer (Gusseisen) | 5–10 Jahre | Werft empf. | 300–1.200 |
| Mischkrümmer (Edelstahl) | 10–20 Jahre | Werft empf. | 500–2.500 |
| Frischwasserpumpen-Dichtung | 3.000–5.000 h | Ja/Werft | 60–150 |
| Seewasserpumpen-Gehäuse | 15+ Jahre | Werft | 150–400 |
| Kühlmittel komplett | 2–5 Jahre (je Typ) | Ja | 20–50 |
| Kielkühler Antifouling | Jährlich | Ja | 30–60 |
| Seeventil Gängigkeit | Monatlich | Ja | 0 |
| Ausgleichsbehälter-Deckel | 5 Jahre | Ja | 8–25 |

### 20.2 Notfall-Checkliste Überhitzung

```
□ 1. Drehzahl sofort auf Leerlauf reduzieren
□ 2. Seewasser am Auspuff prüfen (Sichtfenster)
□ 3. Falls KEIN Seewasser → Motor AUS
□ 4. Seeventil prüfen (offen?)
□ 5. Seewasserfilter prüfen (sauber?)
□ 6. Impeller prüfen (Pumpendeckel öffnen)
□ 7. Falls alles OK → Thermostat prüfen
□ 8. Falls Problem gelöst → Temperatur beobachten
□ 9. Falls Problem bestehen bleibt → Fachbetrieb
□ 10. Motorlogbuch aktualisieren
```

### 20.3 Bordvorräte Kühlsystem

| Teil | Menge | Preis (EUR) |
|------|:---:|:---:|
| Ersatz-Impeller (passend) | 2 | 25–90 pro Stück |
| O-Ring Pumpendeckel | 2 | 3–8 pro Stück |
| Impeller-Abzieher | 1 | 15–30 |
| Zinkanode Wärmetauscher | 2 | 5–25 pro Stück |
| Thermostat | 1 | 20–60 |
| Kühlmittel-Konzentrat (1 l) | 1 | 8–18 |
| Dichtmittel (Hylomar) | 1 Tube | 8–15 |
| Schlauchschellen A4 (sortiert) | 10 | 10–25 |
| Seewasserschlauch (1 m, passend) | 1 | 10–25 |
| Dichtungsmaterial (Gummi) | 1 Platte | 8–15 |

**Gesamt-Bordvorrat Kühlsystem:** ca. 150–400 EUR

### 20.4 Temperatur-Referenz

| Messstelle | Normal | Warnung | Alarm |
|-----------|:---:|:---:|:---:|
| Motorblock (Frischwasser) | 80–88 °C | 90–95 °C | >100 °C |
| Seewasser-Austritt Auspuff | 45–60 °C | 65–70 °C | >75 °C |
| Motoröl | 60–90 °C | 95–110 °C | >110 °C |
| Getriebeöl | 50–80 °C | 85–100 °C | >110 °C |
| Ladeluft (nach Intercooler) | 40–60 °C | 65–80 °C | >85 °C |
| Auspuffschlauch (Außenhaut) | 40–60 °C | 65–80 °C | >90 °C |

### 20.5 Kühlsystem-Kosten pro Motorklasse (Übersicht)

**Segelboot 8–12 m, 15–40 PS (z.B. Yanmar 2/3JH, Volvo D1):**

| Posten | Jährlich (EUR) | 5-Jahres (EUR) | 10-Jahres (EUR) |
|--------|:---:|:---:|:---:|
| Impeller + O-Ring | 30–50 | 150–250 | 300–500 |
| Zinkanoden | 10–25 | 50–125 | 100–250 |
| Kühlmittel | 0–15 | 20–50 | 40–100 |
| Thermostat | 0 | 25–50 | 50–100 |
| Schläuche + Schellen | 0 | 50–120 | 100–240 |
| Wärmetauscher-Reinigung | 15–30 | 75–150 | 150–300 |
| Mischkrümmer | 0 | 0–400 | 300–800 |
| Wärmetauscher-Tausch | 0 | 0 | 350–700 |
| **Summe Material** | **55–120** | **370–1.145** | **1.390–2.990** |
| Werft-Arbeit (falls Fremd) | 200–350 | 1.000–1.750 | 2.000–3.500 |
| **Gesamt mit Werft** | **255–470** | **1.370–2.895** | **3.390–6.490** |

**Motorboot 10–15 m, 50–150 PS (z.B. Yanmar 4JH, Volvo D2-75):**

| Posten | Jährlich (EUR) | 5-Jahres (EUR) | 10-Jahres (EUR) |
|--------|:---:|:---:|:---:|
| Impeller + O-Ring | 40–70 | 200–350 | 400–700 |
| Zinkanoden (inkl. Ölkühler) | 15–35 | 75–175 | 150–350 |
| Kühlmittel | 0–20 | 30–70 | 60–140 |
| Thermostat | 0 | 30–60 | 60–120 |
| Schläuche + Schellen | 0 | 80–180 | 160–360 |
| Wärmetauscher-Reinigung | 20–40 | 100–200 | 200–400 |
| Mischkrümmer | 0 | 0–600 | 400–1.200 |
| Wärmetauscher-Tausch | 0 | 0 | 500–1.200 |
| Ladeluftkühler (Turbo) | 0 | 0 | 0–800 |
| **Summe Material** | **75–165** | **515–1.635** | **1.930–5.270** |

### 20.6 Saisonaler Wartungskalender

**Saisonstart (Frühjahr):**
```
□ Seeventil öffnen und auf Gängigkeit prüfen
□ Seewasserfilter reinigen
□ Impeller-Zustand prüfen (tauschen falls >1 Jahr alt)
□ Kühlmittelstand und -konzentration prüfen (Refraktometer)
□ Alle Schläuche visuell auf Risse, Aufquellung prüfen
□ Schlauchschellen auf Festsitz prüfen
□ Mischkrümmer visuell inspizieren
□ Motorprobelauf: Seewasserfluss am Auspuff prüfen
□ Motortemperatur beobachten (Soll: 80–88 °C nach 15 min)
□ Zinkanoden im Wärmetauscher/Ölkühler prüfen
```

**Saisonende (Herbst/Winter):**
```
□ Seewasserkreislauf mit Propylenglykol-Frostschutz befüllen
□ Impeller ausbauen (Verformung über Winter vermeiden)
□ Kühlmittel-Konzentration im Frischwasserkreislauf prüfen (≥33 %)
□ Seeventil schließen
□ Seewasserfilter entleeren
□ Alle Ablass-Hähne öffnen (Seewasserseite)
□ Auspuffschlauch-Zustand prüfen
□ Logbuch: Impeller-Alter, Kühlmittel-Alter, Betriebsstunden notieren
```

### 20.7 Werkzeug-Checkliste Kühlsystem

| Werkzeug | Verwendung | Preis (EUR) |
|----------|-----------|:---:|
| Impeller-Abzieher | Impeller beschädigungsfrei entfernen | 15–30 |
| Infrarot-Thermometer | Temperaturmessung an Komponenten | 20–50 |
| Refraktometer | Kühlmittel-Konzentration messen | 15–40 |
| pH-Teststreifen | Kühlmittel-pH prüfen | 5–10 |
| Endoskop (USB-Kamera) | Mischkrümmer-Inneninspektion | 30–80 |
| Kühlsystem-Druckprüfpumpe | Undichtigkeiten finden | 40–100 |
| CO₂-Tester (Kühlmittel) | Zylinderkopfdichtung prüfen | 25–40 |
| Rohrbürsten-Set (Nylon) | Wärmetauscher-Rohre reinigen | 15–30 |
| Drehmomentschlüssel (klein) | Pumpendeckel korrekt anziehen | 25–60 |
| Schlauchschellen-Sortiment A4 | Ersatzschellen vorrätig | 15–30 |

---
---

## 21. ANHANG A–H: Fallstudien

### ANHANG A — Fallstudie: Impeller-Versagen bei Hafeneinfahrt

**Boot:** Bavaria 37 Cruiser, Baujahr 2014
**Motor:** Volvo Penta D2-40, 1.800 Betriebsstunden
**Revier:** Mittelmeer, Kroatien, Juli (Wassertemperatur: 26 °C)

**Situation:**
Skipper fährt in Marina ein, bemerkt Temperaturalarm bei 98 °C.
Motor wird auf Leerlauf reduziert, Boot erreicht gerade noch den
Liegeplatz. Motor wird sofort abgestellt.

**Diagnose:**
- Seeventil: offen → OK.
- Seewasserfilter: sauber → OK.
- Impeller: Pumpendeckel geöffnet → 4 von 12 Flügeln fehlen.
  Impeller war 2 Jahre alt (letzte Wartung übersprungen).
- Wärmetauscher: Endkappe geöffnet → 3 Flügel-Fragmente gefunden.
- Mischkrümmer: 1 Fragment gefunden → alle 4 gefunden.

**Reparatur:**
- Neuer Impeller: Johnson 09-812B, 35 EUR.
- Neue O-Ringe: 8 EUR.
- Wärmetauscher-Reinigung (Essigessenz): 5 EUR.
- Zinkanode (gleich mit getauscht): 12 EUR.
- Arbeitszeit: 2 Stunden (Eigenleistung).

**Gesamtkosten:** 60 EUR
**Vermiedener Schaden:** Motorüberhitzung hätte ohne rechtzeitiges
Eingreifen Zylinderkopfdichtung und Zylinderkopf kosten können
(3.000–6.000 EUR).

**AYDI-Bewertung:** Dieser Fall wäre durch jährlichen Impeller-Tausch
vollständig vermeidbar gewesen (Kosten: 35 EUR/Jahr).

---

### ANHANG B — Fallstudie: Mischkrümmer-Durchbruch bei Nachtfahrt

**Boot:** Hallberg-Rassy 39, Baujahr 2006
**Motor:** Volvo Penta D2-55, 4.200 Betriebsstunden
**Revier:** Nordsee, September (Wassertemperatur: 16 °C)

**Situation:**
Nachtfahrt bei Windstärke 5–6, Motor als Stütze. Skipper bemerkt
beim Routinecheck im Maschinenraum Seewasser am Mischkrümmer.
Motor wird sofort abgestellt. Segel übernehmen.

**Diagnose:**
- Mischkrümmer (Gusseisen, original, 18 Jahre alt): Lochfraß an der
  Unterseite der Mischzone. Seewasser tropft auf den Auspuffkrümmer.
- Noch kein Seewasser in den Motor gelangt (Glücksfall — Motor war
  in Betrieb, Abgasdruck verhinderte Rückfluss).
- Ölpeilstab: Öl sauber → kein Seewasser im Motor.

**Reparatur:**
- Neuer Mischkrümmer (Edelstahl 316L, Upgrade): 850 EUR.
- Neue Dichtungen: 45 EUR.
- Arbeitszeit Werft: 4 Stunden × 95 EUR = 380 EUR.
- Neue Zinkanoden: 25 EUR.

**Gesamtkosten:** 1.300 EUR
**Vermiedener Schaden:** Hätte der Skipper den Tropfen nicht bemerkt
und den Motor über Nacht laufen gelassen, wäre beim Abstellen
Seewasser in die Zylinder geflossen. Nächster Morgen: Startversuch
→ Hydrolock → Pleuelbruch → Motorschaden (25.000–35.000 EUR).

**AYDI-Bewertung:** Mischkrümmer aus Gusseisen sollte nach 12–15 Jahren
präventiv getauscht werden. Das Upgrade auf Edelstahl amortisiert
sich über die nahezu doppelte Lebensdauer.

---

### ANHANG C — Fallstudie: Winterfestmachung vergessen — Frostschaden

**Boot:** Jeanneau Sun Odyssey 349, Baujahr 2017
**Motor:** Yanmar 3JH40, 320 Betriebsstunden
**Revier:** Ostsee, Deutschland (Wintertemperatur: −15 °C)

**Situation:**
Eigner verlässt das Boot im November ohne Winterfestmachung. Boot
liegt im Wasser (beheizte Halle war voll). Im Januar Frost −15 °C
über 2 Wochen.

**Schaden:**
- Seewasserkreislauf: Seewasser im Seewasserfilter, Impeller-Pumpe
  und Wärmetauscher gefroren → Filtergehäuse gerissen, Pumpengehäuse
  gerissen, 2 Wärmetauscher-Rohre geplatzt.
- Frischwasserkreislauf: Kühlmittel-Konzentration war nur 20 %
  (Frostschutz bis −9 °C) → Kühlmittel im Motorblock gefroren →
  Frostpfropfen herausgedrückt, kleiner Riss im Motorblock.

**Reparatur:**
- Neuer Motorblock: (Yanmar 3JH40 Shortblock): 8.500 EUR.
- Neuer Wärmetauscher: 650 EUR.
- Neue Seewasserpumpe: 280 EUR.
- Neuer Seewasserfilter: 85 EUR.
- Neue Schläuche, Schellen, Dichtungen: 180 EUR.
- Arbeitszeit Werft: 24 Stunden × 95 EUR = 2.280 EUR.

**Gesamtkosten:** 11.975 EUR
**Versicherung:** Regulierung abgelehnt — „mangelnde Sorgfaltspflicht
des Eigners, da Winterfestmachung versäumt wurde."

**AYDI-Bewertung:** Winterfestmachung hätte 2 Stunden Zeit und ca.
30 EUR Material (Propylenglykol + Kühlmittel-Konzentrat) gekostet.
Kosten-Nutzen-Verhältnis: 30 EUR vs. 11.975 EUR.

---

### ANHANG D — Fallstudie: Elektrolyse zerstört Wärmetauscher in 6 Monaten

**Boot:** Beneteau Oceanis 46.1, Baujahr 2020
**Motor:** Yanmar 4JH57, 600 Betriebsstunden
**Revier:** Mittelmeer, Spanien

**Situation:**
Eigner stellt fest, dass nach 6 Monaten am Dauerliegeplatz (mit
Landstrom) die Zinkanode im Wärmetauscher komplett aufgelöst ist.
Wärmetauscher-Endkappe zeigt grünliche Verfärbung.

**Diagnose:**
- Galvanischer Isolator: Keiner installiert.
- Landstrom-Messung: 0,4 A Leckstrom über den Schutzleiter.
- Wärmetauscher: 30 % der Rohre zeigen Lochfraß (nach nur 600 h!).
- Ölkühler: Beginnendes Lochfraß.
- Nachbarboot: Ältere Yacht mit defekter Erdung.

**Reparatur:**
- Neuer Wärmetauscher: 750 EUR.
- Galvanischer Isolator (Mastervolt GI-16): 180 EUR.
- Neue Zinkanoden (2×): 25 EUR.
- Erdung geprüft und verbessert: 150 EUR.
- Arbeitszeit: 6 Stunden × 85 EUR = 510 EUR.

**Gesamtkosten:** 1.615 EUR
**Hätte vermieden werden können durch:** Galvanischen Isolator bei
der Inbetriebnahme installieren (180 EUR + 1 h Einbau).

**AYDI-Bewertung:** Bei Dauerliegeplätzen mit Landstrom ist ein
galvanischer Isolator Pflicht. Ohne Isolator können Leckströme
das komplette Kühlsystem in einer Saison zerstören.

---

### ANHANG E — Fallstudie: Thermostat-Notlösung auf Langfahrt

**Boot:** Amel Super Maramu, Baujahr 1998
**Motor:** Volvo Penta TMD22, 7.500 Betriebsstunden
**Revier:** Atlantik-Überquerung, 800 sm bis Karibik

**Situation:**
Mitten auf dem Atlantik zeigt der Motor 102 °C. Seewasserkreislauf OK.
Verdacht: Thermostat klemmt. Kein Ersatz-Thermostat an Bord.

**Notlösung:**
1. Motor abgestellt, abkühlen lassen (1 h).
2. Thermostat-Gehäuse geöffnet (3 Schrauben).
3. Thermostat entnommen. Visuell: Wachs ausgetreten, klemmt bei 1 mm Hub.
4. Motor ohne Thermostat gestartet.
5. Motortemperatur sinkt auf 58 °C (Seewasser: 24 °C).
6. Restliche 800 sm mit 58 °C gefahren.

**Folge:**
- Motor lief zu kühl → schlechte Verbrennung, leichter Leistungsverlust.
- Nach 800 sm (ca. 120 Betriebsstunden ohne Thermostat):
  leichte Verglasung der Zylinder festgestellt.
- In der Karibik: Neuer Thermostat eingebaut (12 EUR), Motor lief
  wieder normal.
- Verglasung: Behandlung mit Volllast-Lauf (2 h bei 90 % Last).

**AYDI-Bewertung:** Thermostat gehört in jeden Bordvorrat (20–60 EUR).
Fahren ohne Thermostat ist als Notlösung akzeptabel, aber nicht
länger als nötig.

---

### ANHANG F — Fallstudie: Kielkühlung bei Expeditionsyacht

**Boot:** Garcia Exploration 45, Baujahr 2021 (Aluminium)
**Motor:** Nanni N4.80, 1.200 Betriebsstunden
**Revier:** Arktis (Spitzbergen), Tropen (Karibik), Gezeitenreviere

**System:**
- Fernstrum Gridcooler GC-3618 am Rumpf, unterhalb der Wasserlinie.
- Trockenauspuff (isoliertes Edelstahlrohr).
- Kein Seeventil, kein Impeller, kein Seewasserfilter.
- Propylenglykol 50 % im geschlossenen Kreislauf.

**Erfahrung nach 4 Jahren / 1.200 h:**
- Kein einziger Kühlsystem-Ausfall.
- Betrieb in Eiswasser (−1 °C) problemlos.
- Betrieb in Tropenwasser (32 °C): Motortemperatur bei 93 °C
  (Grenzbereich, aber OK).
- Bewuchs am Kielkühler nach 6 Monaten Karibik: Reinigung bei jedem
  Antifouling-Anstrich.
- Einzige Wartung: Kühlmittel-Konzentration jährlich geprüft,
  Antifouling auf Kielkühler erneuert.

**AYDI-Bewertung:** Kielkühlung ist die optimale Lösung für
Langfahrt-/Expeditionsyachten. Höhere Installationskosten (ca.
4.000 EUR mehr als Standardsystem) amortisieren sich über den
Lebenszyklus durch praktisch null Wartungsausfälle.

---

### ANHANG G — Fallstudie: Seewasser im Motor durch defekten Ladeluftkühler

**Boot:** Bavaria C42, Baujahr 2019
**Motor:** Volvo Penta D2-75, 900 Betriebsstunden (Turbo mit Ladeluftkühler)

**Situation:**
Motor läuft unruhig, weißer Rauch, Leistungsverlust. Skipper fährt
weiter (Fehler!). Nach 30 Minuten: ungewöhnliches Klopfen → Motor aus.

**Diagnose:**
- Ladeluftkühler: Internes Leck (Seewasser → Ladeluft).
- Seewasser gelangte über die Ladeluft in die Zylinder.
- 2 Einspritzdüsen durch Wasserschlag beschädigt.
- 1 Pleuel leicht verbogen (Hydrolock-Vorstufe).

**Reparatur:**
- Neuer Ladeluftkühler: 800 EUR.
- 4 neue Einspritzdüsen: 1.200 EUR.
- Pleuel-Tausch (1 Stück): 450 EUR + Motor-Teilzerlegung.
- Arbeitszeit Werft: 16 Stunden × 105 EUR = 1.680 EUR.

**Gesamtkosten:** 4.130 EUR

**AYDI-Bewertung:** Bei weißem Rauch + Leistungsverlust Motor sofort
abstellen und Diagnose durchführen. Weiterfahren kann den Schaden
um ein Vielfaches erhöhen.

---

### ANHANG H — Fallstudie: Plastiktüte im Seewasserfilter

**Boot:** Dehler 34, Baujahr 2012
**Motor:** Volvo Penta D1-30, 1.400 Betriebsstunden
**Revier:** Ostsee, Lübecker Bucht, August

**Situation:**
Motor springt an, Seewasser fließt. Nach 5 Minuten Fahrt:
Temperaturalarm. Skipper prüft Sichtfenster am Auspuff → kein
Seewasser mehr.

**Diagnose:**
- Seeventil: offen → OK.
- Seewasserfilter: Plastiktüte hat sich um den Filterkorb gewickelt
  und den Durchfluss komplett blockiert.

**Reparatur:**
- Plastiktüte entfernt. Motor gestartet. Alles OK.
- Kosten: 0 EUR.
- Zeitaufwand: 5 Minuten.

**Lehre:**
- Transparenter Seewasserfilter-Deckel ermöglicht Sichtprüfung
  in Sekunden.
- In Revieren mit viel Treibgut (Häfen, Flussmündungen): vor dem
  Start und regelmäßig während der Fahrt den Filter prüfen.
- Ein Duplex-Filter (Umschaltfilter) hätte die Reinigung ohne
  Motorstop ermöglicht.

**AYDI-Bewertung:** Seewasserfilter-Sichtprüfung sollte in jede
Motor-Startcheckliste integriert sein.

### Zusammenfassung Fallstudien — Kosten-Nutzen-Analyse

| Fallstudie | Ursache | Vermeidungskosten (EUR) | Schadenskosten (EUR) | Faktor |
|:---:|---------|:---:|:---:|:---:|
| A — Impeller | Übersprungene Wartung | 35/Jahr | 60 (Glück gehabt) | 1,7× |
| B — Mischkrümmer | Alterung (18 Jahre) | 600 (präventiv bei 12 J.) | 1.300 | 2,2× |
| C — Frostschaden | Vergessene Winterfestm. | 30 | 11.975 | 399× |
| D — Elektrolyse | Fehlender Galv. Isolator | 180 | 1.615 | 9× |
| E — Thermostat | Kein Ersatzteil an Bord | 40 (Ersatz vorrätig) | 0 (Notlösung) | – |
| F — Kielkühlung | – (Referenzfall) | 4.000 (Mehrkosten Installation) | 0 (kein Ausfall in 4 J.) | – |
| G — Ladeluftkühler | Weiterfahren trotz Symptome | 0 (sofort abstellen!) | 4.130 | ∞ |
| H — Plastiktüte | Kein Duplex-Filter | 0–400 (Duplex-Filter) | 0 (schnell behoben) | – |

**Kernbotschaften:**
1. Winterfestmachung vergessen = teuerster Fehler (Faktor 399×).
2. Galvanischer Isolator bei Landstrom-Liegeplatz = beste Einzelinvestition.
3. Jährlicher Impeller-Tausch verhindert den häufigsten Kühlsystem-Ausfall.
4. Bei Symptomen (weißer Rauch, Temperaturalarm) → SOFORT Motor abstellen.
5. Mischkrümmer ist die kritischste Einzelkomponente — regelmäßig prüfen.

---
---

## 22. ANHANG I–R: Pydantic v2 Datenmodelle

### Visuelle Analyse — Kühlsystem-spezifische Erkennungsmerkmale

Die AYDI-Bildanalyse (Pipeline B) erkennt Kühlsystem-Komponenten
und deren Zustand auf Fotos des Maschinenraums. Folgende visuelle
Merkmale werden ausgewertet:

**Impeller-Zustand (wenn Pumpendeckel geöffnet):**
- Flügelzahl vs. Soll-Flügelzahl erkennen.
- Verformung der Flügel (permanent gebogen vs. flexibel).
- Farbveränderung (graues Neopren = alt, schwarzes = neu).
- Risse und Bruchstellen an der Flügelbasis.

**Wärmetauscher-Zustand (wenn Endkappen entfernt):**
- Rohre: Kalkbelag (weiß/grau), Korrosion (grün = Kupfer, braun = Eisen).
- Rohrböden: Verfärbung, Lochfraß.
- Zinkanode: Größe im Verhältnis zum Gewinde (>50 % = OK, <50 % = tauschen).

**Mischkrümmer (Außenansicht):**
- Oberflächenkorrosion: Rost (braun), Salzausblühungen (weiß).
- Feuchtigkeit: Nasse Stellen, Tropfspuren, Verfärbungsringe.
- Beschichtungszustand: Abblätternd, Blasen, intakt.

**Seewasserfilter (Sichtfenster):**
- Füllstand und Farbe des Wassers.
- Verschmutzung des Filterkorbs (Tang, Partikel sichtbar).
- Bewuchs im Filtergehäuse.

**Schläuche und Schellen:**
- Schlauchfarbe und -zustand: Risse, Aufquellung, Verfärbung.
- Schellen: Rost an Schellenband, Einfachschelle vs. Doppelschelle.
- Tropfspuren unter Schlauchverbindungen.

**Seeventil (wenn zugänglich):**
- Entzinkung: Kupfer-rötliche Verfärbung statt Gold (bei Bronze/Messing).
- Korrosion: Grünspan, weiße Krustenbildung.
- Typ: Kugelhahn, Kükenhahn, Kunststoff erkennbar.

**Confidence-Level Visuelle Analyse Kühlsystem:**
| Objekt | Typische Confidence | Voraussetzung |
|--------|:---:|:---:|
| Impeller-Zustand | visual_high | Pumpe offen, gute Beleuchtung |
| Wärmetauscher-Rohre | visual_medium | Endkappen entfernt, Rohre sichtbar |
| Mischkrümmer außen | visual_medium | Guter Zugang, Beleuchtung |
| Mischkrümmer innen | visual_low | Endoskop-Bild, oft unscharf |
| Schläuche + Schellen | visual_high | Guter Zugang |
| Seewasserfilter | visual_high | Transparenter Deckel |
| Seeventil | visual_medium | Oft schlecht zugänglich |
| Zinkanode | visual_high | Anode sichtbar, gute Beleuchtung |
| Kühlmittelfarbe | visual_high | Ausgleichsbehälter sichtbar |

---

### ANHANG I — CoolingSystemType (Enum)

```python
from enum import Enum


class CoolingSystemType(str, Enum):
    """Typ des Kühlsystems."""
    SINGLE_CIRCUIT = "single_circuit"     # Einkreis (Direktkühlung)
    DUAL_CIRCUIT = "dual_circuit"         # Zweikreis (Indirekte Kühlung)
    KEEL_COOLING = "keel_cooling"         # Kielkühlung
    HYBRID = "hybrid"                     # Kielkühlung + Seewasser-Auspuff
    UNKNOWN = "unknown"
```

### ANHANG J — CoolingComponentCondition (Enum)

```python
class CoolingComponentCondition(str, Enum):
    """Zustandsbewertung einer Kühlsystem-Komponente."""
    EXCELLENT = "excellent"       # 90–100, neuwertig
    GOOD = "good"                 # 70–89, gebrauchsspuren, funktionsfähig
    FAIR = "fair"                 # 50–69, deutliche Abnutzung, baldiger Austausch
    POOR = "poor"                 # 30–49, stark abgenutzt, Austausch nötig
    CRITICAL = "critical"         # 0–29, defekt oder ausfallgefährdet
    NOT_ASSESSED = "not_assessed" # Nicht beurteilbar
```

### ANHANG K — ImpellerAssessment

```python
from pydantic import BaseModel, Field
from typing import Optional


class ImpellerAssessment(BaseModel):
    """
    Bewertung eines Seewasser-Impellers.
    Erfasst Zustand, Alter und Empfehlungen.
    """
    model_config = {"from_attributes": True}

    impeller_present: bool = Field(
        ..., description="Impeller vorhanden"
    )
    manufacturer: Optional[str] = Field(
        None, description="Hersteller (Jabsco, Johnson, Sherwood)"
    )
    part_number: Optional[str] = Field(
        None, description="Teilenummer"
    )
    material: Optional[str] = Field(
        None, description="Material (neoprene, nitrile, viton)"
    )
    blade_count_nominal: Optional[int] = Field(
        None, ge=4, le=14, description="Soll-Flügelanzahl"
    )
    blade_count_actual: Optional[int] = Field(
        None, ge=0, le=14, description="Ist-Flügelanzahl"
    )
    blades_missing: int = Field(
        0, ge=0, description="Fehlende Flügel"
    )
    fragments_found: int = Field(
        0, ge=0, description="Gefundene Flügel-Fragmente"
    )
    fragments_location: Optional[str] = Field(
        None, description="Fundort der Fragmente"
    )
    flexibility: Optional[str] = Field(
        None, description="Flexibilität: flexible, stiff, brittle"
    )
    age_months: Optional[int] = Field(
        None, ge=0, description="Alter in Monaten"
    )
    operating_hours: Optional[int] = Field(
        None, ge=0, description="Betriebsstunden seit Einbau"
    )
    wear_plate_condition: Optional[str] = Field(
        None, description="Zustand Verschleißplatte"
    )

    condition: CoolingComponentCondition = Field(
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
    estimated_remaining_life_hours: Optional[int] = Field(
        None, ge=0, description="Geschätzte Restlebensdauer (h)"
    )
```

### ANHANG L — HeatExchangerAssessment

```python
class HeatExchangerAssessment(BaseModel):
    """
    Bewertung eines Wärmetauschers.
    Erfasst Zustand beider Seiten und Effizienz.
    """
    model_config = {"from_attributes": True}

    hex_type: str = Field(
        ..., description="Typ: tube_bundle, plate, coaxial"
    )
    manufacturer: Optional[str] = Field(
        None, description="Hersteller (Bowman, Fernstrum, Vetus, OEM)"
    )
    material_tubes: Optional[str] = Field(
        None, description="Rohrmaterial: copper, cupro_nickel, stainless"
    )
    material_shell: Optional[str] = Field(
        None, description="Mantelmaterial"
    )
    age_years: Optional[float] = Field(
        None, ge=0, description="Alter in Jahren"
    )

    # Seewasserseite
    seawater_side_condition: CoolingComponentCondition = Field(
        ..., description="Zustand Seewasserseite"
    )
    seawater_side_score: float = Field(
        ..., ge=0, le=100, description="Bewertung Seewasserseite"
    )
    scaling_percentage: Optional[float] = Field(
        None, ge=0, le=100,
        description="Geschätzte Verkalkung in Prozent"
    )
    blockage_percentage: Optional[float] = Field(
        None, ge=0, le=100,
        description="Geschätzte Verstopfung in Prozent"
    )
    impeller_fragments_found: bool = Field(
        False, description="Impeller-Fragmente gefunden"
    )

    # Frischwasserseite
    freshwater_side_condition: CoolingComponentCondition = Field(
        ..., description="Zustand Frischwasserseite"
    )
    freshwater_side_score: float = Field(
        ..., ge=0, le=100, description="Bewertung Frischwasserseite"
    )
    coolant_contamination: Optional[str] = Field(
        None, description="Kühlmittel-Verunreinigung: none, rust, oil, sludge"
    )

    # Zinkanode
    zinc_anode_present: bool = Field(
        ..., description="Zinkanode vorhanden"
    )
    zinc_anode_remaining_percentage: Optional[float] = Field(
        None, ge=0, le=100,
        description="Verbleibende Zinkanode in Prozent"
    )

    # Effizienz
    approach_temperature_c: Optional[float] = Field(
        None, description="Approach-Temperatur in °C"
    )
    seawater_delta_t_c: Optional[float] = Field(
        None, description="Seewasser-Temperaturdifferenz Ein/Aus (°C)"
    )
    freshwater_delta_t_c: Optional[float] = Field(
        None, description="Frischwasser-Temperaturdifferenz Ein/Aus (°C)"
    )

    # Gesamt
    condition: CoolingComponentCondition = Field(
        ..., description="Gesamtzustand"
    )
    score: float = Field(
        ..., ge=0, le=100, description="Gesamtbewertung (0–100)"
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
        None, ge=0, description="Geschätzte Restlebensdauer (Jahre)"
    )
    replacement_cost_eur: Optional[float] = Field(
        None, ge=0, description="Geschätzte Austauschkosten (EUR)"
    )
```

### ANHANG M — MixingElbowAssessment

```python
class MixingElbowAssessment(BaseModel):
    """
    Bewertung des Mischkrümmers / Injection Elbow.
    KRITISCHE Komponente — Versagen kann zum Motorschaden führen.
    """
    model_config = {"from_attributes": True}

    material: str = Field(
        ..., description="Material: cast_iron, cast_iron_coated, stainless_316l, ni_resist, aluminum"
    )
    age_years: Optional[float] = Field(
        None, ge=0, description="Alter in Jahren"
    )
    operating_hours: Optional[int] = Field(
        None, ge=0, description="Betriebsstunden"
    )

    # Korrosion
    external_corrosion: str = Field(
        ..., description="Außenkorrosion: none, surface, moderate, severe, perforated"
    )
    internal_corrosion: Optional[str] = Field(
        None, description="Innenkorrosion (endoskopisch): none, surface, pitting, severe"
    )
    wall_thickness_mm: Optional[float] = Field(
        None, ge=0, description="Gemessene Wandstärke (mm)"
    )
    min_wall_thickness_mm: Optional[float] = Field(
        None, ge=0, description="Minimale zulässige Wandstärke (mm)"
    )
    water_leak_detected: bool = Field(
        False, description="Seewasser-Leck erkannt"
    )

    # Verbindungen
    gasket_condition: Optional[str] = Field(
        None, description="Dichtungszustand: good, worn, leaking"
    )
    bolt_condition: Optional[str] = Field(
        None, description="Schraubenzustand: good, corroded, seized"
    )

    # Bewertung
    condition: CoolingComponentCondition = Field(
        ..., description="Gesamtzustand"
    )
    score: float = Field(
        ..., ge=0, le=100, description="Bewertung (0–100)"
    )
    confidence: str = Field(
        ..., description="Konfidenzstufe"
    )
    is_critical: bool = Field(
        False, description="KRITISCHER Befund (sofortige Maßnahme nötig)"
    )

    findings: list[str] = Field(
        default_factory=list, description="Befunde"
    )
    recommendations: list[str] = Field(
        default_factory=list, description="Empfehlungen"
    )
    estimated_remaining_life_years: Optional[float] = Field(
        None, ge=0, description="Geschätzte Restlebensdauer (Jahre)"
    )
    replacement_cost_eur: Optional[float] = Field(
        None, ge=0, description="Geschätzte Austauschkosten (EUR)"
    )
    upgrade_recommended: bool = Field(
        False, description="Upgrade auf hochwertigeres Material empfohlen"
    )
    upgrade_material: Optional[str] = Field(
        None, description="Empfohlenes Upgrade-Material"
    )
    upgrade_cost_eur: Optional[float] = Field(
        None, ge=0, description="Upgrade-Kosten (EUR)"
    )
```

### ANHANG N — ThermostatAssessment

```python
class ThermostatAssessment(BaseModel):
    """
    Bewertung des Kühlwasser-Thermostats.
    """
    model_config = {"from_attributes": True}

    thermostat_present: bool = Field(
        ..., description="Thermostat vorhanden"
    )
    nominal_opening_temp_c: Optional[float] = Field(
        None, ge=50, le=100,
        description="Soll-Öffnungstemperatur (°C)"
    )
    actual_opening_temp_c: Optional[float] = Field(
        None, ge=20, le=120,
        description="Gemessene Öffnungstemperatur (°C)"
    )
    nominal_full_open_temp_c: Optional[float] = Field(
        None, ge=60, le=110,
        description="Soll-Vollöffnungstemperatur (°C)"
    )
    actual_full_open_temp_c: Optional[float] = Field(
        None, ge=30, le=130,
        description="Gemessene Vollöffnungstemperatur (°C)"
    )
    stroke_mm: Optional[float] = Field(
        None, ge=0, le=20,
        description="Gemessener Hub (mm)"
    )
    age_years: Optional[float] = Field(
        None, ge=0, description="Alter in Jahren"
    )
    stuck_position: Optional[str] = Field(
        None, description="Klemmposition: none, open, closed, partial"
    )

    condition: CoolingComponentCondition = Field(
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
```

### ANHANG O — CoolantAssessment

```python
class CoolantAssessment(BaseModel):
    """
    Bewertung des Kühlmittels im Frischwasserkreislauf.
    """
    model_config = {"from_attributes": True}

    coolant_type: Optional[str] = Field(
        None, description="Kühlmittel-Typ: iat, oat, hoat, unknown"
    )
    glycol_type: Optional[str] = Field(
        None, description="Glykol-Typ: ethylene_glycol, propylene_glycol, unknown"
    )
    concentration_percent: Optional[float] = Field(
        None, ge=0, le=100,
        description="Glykol-Konzentration (%)"
    )
    frost_protection_c: Optional[float] = Field(
        None, le=0,
        description="Frostschutz bis (°C, negativ)"
    )
    ph_value: Optional[float] = Field(
        None, ge=0, le=14,
        description="pH-Wert"
    )
    color: Optional[str] = Field(
        None, description="Farbe: green, orange, pink, yellow, brown, milky"
    )
    clarity: Optional[str] = Field(
        None, description="Klarheit: clear, cloudy, opaque, oily"
    )
    age_years: Optional[float] = Field(
        None, ge=0, description="Alter in Jahren (seit letztem Wechsel)"
    )
    level: Optional[str] = Field(
        None, description="Füllstand: full, adequate, low, empty"
    )

    # Auffälligkeiten
    oil_contamination: bool = Field(
        False, description="Ölverunreinigung festgestellt"
    )
    rust_contamination: bool = Field(
        False, description="Rost im Kühlmittel"
    )
    foam_present: bool = Field(
        False, description="Schaum vorhanden (mögliche ZKD-Undichtigkeit)"
    )

    condition: CoolingComponentCondition = Field(
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
    next_change_date: Optional[str] = Field(
        None, description="Empfohlenes nächstes Wechseldatum (ISO 8601)"
    )
```

### ANHANG P — SeawaterCircuitAssessment

```python
class SeawaterCircuitAssessment(BaseModel):
    """
    Bewertung des gesamten Seewasserkreislaufs.
    """
    model_config = {"from_attributes": True}

    # Seeventil
    seacock_type: Optional[str] = Field(
        None, description="Seeventil-Typ: ball_valve_bronze, tapered_plug, plastic_marelon, stainless"
    )
    seacock_material: Optional[str] = Field(
        None, description="Seeventil-Material"
    )
    seacock_operable: Optional[bool] = Field(
        None, description="Seeventil gängig (lässt sich öffnen/schließen)"
    )
    seacock_condition: CoolingComponentCondition = Field(
        ..., description="Seeventil-Zustand"
    )
    dezincification_suspected: bool = Field(
        False, description="Entzinkung vermutet"
    )

    # Seewasserfilter
    strainer_type: Optional[str] = Field(
        None, description="Filter-Typ: standard, duplex, self_cleaning"
    )
    strainer_manufacturer: Optional[str] = Field(
        None, description="Hersteller (Groco, Vetus, Perko)"
    )
    strainer_condition: CoolingComponentCondition = Field(
        ..., description="Filter-Zustand"
    )
    strainer_clean: Optional[bool] = Field(
        None, description="Filterkorb sauber"
    )

    # Leitungen
    hose_material: Optional[str] = Field(
        None, description="Schlauchmaterial"
    )
    hose_age_years: Optional[float] = Field(
        None, ge=0, description="Schlauch-Alter (Jahre)"
    )
    hose_condition: CoolingComponentCondition = Field(
        ..., description="Schlauch-Zustand"
    )
    double_clamped: Optional[bool] = Field(
        None, description="Alle Anschlüsse doppelt geschellt"
    )
    clamp_material: Optional[str] = Field(
        None, description="Schellenmaterial: stainless_a4, stainless_a2, galvanized"
    )

    # Seewasserfluss
    seawater_flow_visible: Optional[bool] = Field(
        None, description="Seewasserfluss am Auspuff sichtbar"
    )
    seawater_flow_rate_l_min: Optional[float] = Field(
        None, ge=0, description="Seewasser-Durchfluss (l/min)"
    )
    seawater_exit_temp_c: Optional[float] = Field(
        None, description="Seewasser-Austrittstemperatur am Auspuff (°C)"
    )

    # Gesamt
    condition: CoolingComponentCondition = Field(
        ..., description="Gesamtzustand Seewasserkreislauf"
    )
    score: float = Field(
        ..., ge=0, le=100, description="Gesamtbewertung (0–100)"
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
```

### ANHANG Q — KielCoolerAssessment

```python
class KielCoolerAssessment(BaseModel):
    """
    Bewertung eines Kielkühlers (nur bei Kielkühlung).
    """
    model_config = {"from_attributes": True}

    cooler_type: str = Field(
        ..., description="Typ: grid_cooler, box_cooler, skin_cooler"
    )
    manufacturer: Optional[str] = Field(
        None, description="Hersteller (Fernstrum, Vetus, Duramax, custom)"
    )
    material: Optional[str] = Field(
        None, description="Material: cupro_nickel, copper, stainless"
    )
    cooling_area_m2: Optional[float] = Field(
        None, ge=0, description="Kühlerfläche (m²)"
    )
    required_area_m2: Optional[float] = Field(
        None, ge=0, description="Benötigte Kühlerfläche (m²)"
    )
    age_years: Optional[float] = Field(
        None, ge=0, description="Alter (Jahre)"
    )

    # Zustand
    fouling_percentage: Optional[float] = Field(
        None, ge=0, le=100,
        description="Bewuchs in Prozent der Fläche"
    )
    antifouling_condition: Optional[str] = Field(
        None, description="Antifouling-Zustand: good, worn, missing"
    )
    corrosion_level: Optional[str] = Field(
        None, description="Korrosion: none, surface, moderate, severe"
    )
    wall_thickness_mm: Optional[float] = Field(
        None, ge=0, description="Wandstärke (mm)"
    )

    # Bewertung
    condition: CoolingComponentCondition = Field(
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
```

### ANHANG R — CoolingSystemAnalysis (Orchestrierungs-Modell)

```python
class CoolingSystemAnalysis(BaseModel):
    """
    Orchestrierungs-Modell für die Gesamtanalyse eines Kühlsystems.
    Kombiniert alle Teilanalysen zu einem Gesamtergebnis.
    Wird sowohl für Level 1 (Schnellanalyse) als auch Level 2
    (Profi-Werkzeug) verwendet.
    """
    model_config = {"from_attributes": True}

    analysis_id: str = Field(..., description="Analyse-ID")
    engine_id: str = Field(..., description="Motor-ID")
    boat_id: Optional[str] = Field(None, description="Boot-ID")
    analysis_date: str = Field(
        ..., description="Analysedatum (ISO 8601)"
    )
    analysis_level: str = Field(
        ..., description="Analyselevel: quick (Level 1) oder professional (Level 2)"
    )

    # System-Typ
    cooling_system_type: CoolingSystemType = Field(
        ..., description="Typ des Kühlsystems"
    )

    # Teilanalysen
    impeller: Optional[ImpellerAssessment] = Field(
        None, description="Impeller-Bewertung"
    )
    heat_exchanger: Optional[HeatExchangerAssessment] = Field(
        None, description="Wärmetauscher-Bewertung"
    )
    mixing_elbow: Optional[MixingElbowAssessment] = Field(
        None, description="Mischkrümmer-Bewertung"
    )
    thermostat: Optional[ThermostatAssessment] = Field(
        None, description="Thermostat-Bewertung"
    )
    coolant: Optional[CoolantAssessment] = Field(
        None, description="Kühlmittel-Bewertung"
    )
    seawater_circuit: Optional[SeawaterCircuitAssessment] = Field(
        None, description="Seewasserkreislauf-Bewertung"
    )
    keel_cooler: Optional[KielCoolerAssessment] = Field(
        None, description="Kielkühler-Bewertung (nur bei Kielkühlung)"
    )
    oil_cooler_condition: Optional[CoolingComponentCondition] = Field(
        None, description="Ölkühler-Zustand"
    )
    oil_cooler_score: Optional[float] = Field(
        None, ge=0, le=100, description="Ölkühler-Bewertung"
    )
    intercooler_condition: Optional[CoolingComponentCondition] = Field(
        None, description="Ladeluftkühler-Zustand (nur Turbo)"
    )
    intercooler_score: Optional[float] = Field(
        None, ge=0, le=100, description="Ladeluftkühler-Bewertung"
    )

    # Betriebsparameter
    engine_temp_c: Optional[float] = Field(
        None, description="Aktuelle Motortemperatur (°C)"
    )
    seawater_exit_temp_c: Optional[float] = Field(
        None, description="Seewasser-Austrittstemperatur (°C)"
    )
    oil_temp_c: Optional[float] = Field(
        None, description="Öltemperatur (°C)"
    )

    # Gesamtergebnis
    overall_score: float = Field(
        ..., ge=0, le=100,
        description="Gesamtbewertung Kühlsystem (0–100)"
    )
    overall_condition: CoolingComponentCondition = Field(
        ..., description="Gesamtzustand"
    )

    # Gewichtete Teilbewertungen
    sub_scores: dict[str, float] = Field(
        default_factory=dict,
        description="Teilbewertungen (z.B. {'impeller': 85, 'heat_exchanger': 72})"
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
```
