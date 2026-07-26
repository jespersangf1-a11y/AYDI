---
titel: "Motor-Wartung — Intervalle, Prozeduren und Winterlager"
kategorie: "Motoren und Antrieb"
unterkategorie: "Motor-Wartung"
version: "2.0"
letzte_aktualisierung: "2026-04"
autor: "AYDI Maritime Knowledge Base"
---

# 18_13 — Motor-Wartung — Intervalle, Prozeduren und Winterlager

---

## Inhaltsverzeichnis

1. [Einführung](#1-einführung)
2. [Wartungsintervalle nach Betriebsstunden](#2-wartungsintervalle-nach-betriebsstunden)
3. [Motoröl — Typen, Spezifikationen und Analyse](#3-motoröl--typen-spezifikationen-und-analyse)
4. [Ölfilter — Genuine und Aftermarket](#4-ölfilter--genuine-und-aftermarket)
5. [Kraftstofffilter und Wasserabscheider](#5-kraftstofffilter-und-wasserabscheider)
6. [Impeller und Kühlwasserpumpen](#6-impeller-und-kühlwasserpumpen)
7. [Keilriemen und Zahnriemen](#7-keilriemen-und-zahnriemen)
8. [Kühlmittel — Mischung, Wechsel und Spülung](#8-kühlmittel--mischung-wechsel-und-spülung)
9. [Ventilspiel-Einstellung](#9-ventilspiel-einstellung)
10. [Zinkanoden am Motor](#10-zinkanoden-am-motor)
11. [Winterlager-Prozedur](#11-winterlager-prozedur)
12. [Inbetriebnahme im Frühjahr](#12-inbetriebnahme-im-frühjahr)
13. [Betriebsstunden-Tracker und Wartungsbuch](#13-betriebsstunden-tracker-und-wartungsbuch)
14. [Fehlerbild-Atlas](#14-fehlerbild-atlas)
15. [Troubleshooting](#15-troubleshooting)
16. [FAQ](#16-faq)
17. [Glossar](#17-glossar)
18. [Schnell-Referenz](#18-schnell-referenz)
19. [ANHANG A–H: Fallstudien](#19-anhang-ah-fallstudien)
20. [ANHANG I–R: Pydantic v2 Datenmodelle](#20-anhang-ir-pydantic-v2-datenmodelle)

---
---

## 1. Einführung

### 1.1 Warum Motorwartung über Lebensdauer und Wert entscheidet

Die regelmäßige und fachgerechte Wartung eines Marine-Dieselmotors ist der
wichtigste Einzelfaktor für dessen Lebensdauer, Zuverlässigkeit und Werterhalt.
Ein vernachlässigter Motor kann bereits nach 2.000–3.000 Betriebsstunden
gravierende Schäden aufweisen, während ein gut gewarteter Motor 8.000–15.000
Stunden erreicht — ein Unterschied von Faktor 3–5 in der Nutzungsdauer.

**Wirtschaftliche Betrachtung:**
- Wartungskosten über 10 Jahre: 3.000–8.000 EUR (je nach Motor)
- Motorüberholung bei Vernachlässigung: 8.000–25.000 EUR
- Motoraustausch bei Totalschaden: 15.000–60.000 EUR
- Wertminderung bei mangelhaftem Wartungsbuch: 15–30 % des Bootswertes

Ein lückenlos geführtes Wartungsbuch mit dokumentierten Intervallen ist
beim Bootsverkauf einer der stärksten Wertindikatoren. Käufer und Gutachter
prüfen zuerst das Wartungsbuch, dann den Motor selbst.

### 1.2 Wartungsphilosophie im maritimen Bereich

Marine-Diesel unterscheiden sich fundamental von Automobilmotoren in ihrer
Wartungsanforderung:

- **Salzwasserumgebung**: Korrosion ist der permanente Feind. Jedes offene
  Metallstück korrodiert. Kühlwassersysteme mit Salzwasser erfordern
  penible Pflege.
- **Saisonaler Betrieb**: In Nord- und Mitteleuropa stehen Boote 4–6 Monate
  still. Diese Standzeit ist gefährlicher als der Betrieb selbst —
  Feuchtigkeit, Kondenswasser, Schimmel, verharzende Dichtungen.
- **Unterlast-Betrieb**: Segelboot-Hilfsmotoren laufen oft unter 40 %
  Last. Das führt zu Zylinderverglasung, Rußaufbau und Injektorverkokung.
- **Vibration**: Ständige Vibration lockert Verbindungen, ermüdet Leitungen
  und beansprucht Schläuche.
- **Schwer zugänglich**: Motoren in Yachten sind häufig schlecht zugänglich.
  Wartung dauert 2–3× so lang wie am Prüfstand.

### 1.3 Herstellerspezifische Wartungsvorgaben

Die Wartungsintervalle variieren zwischen Herstellern und Motorserien
erheblich. Dieses Dokument behandelt die vier wichtigsten Hersteller
für Yachtmotoren im europäischen Markt:

| Hersteller | Typische Serien | Leistungsbereich | Marktanteil EU |
|------------|----------------|-------------------|----------------|
| Yanmar | 1GM10, 2YM15, 3YM20/30, 3JH, 4JH, 4LHA, 6LY | 9–440 PS | ~35 % |
| Volvo Penta | D1, D2, D3, D4, D6, D8, D11, D13 | 10–900 PS | ~30 % |
| Beta Marine | 14–150 (Kubota-basiert) | 14–150 PS | ~10 % |
| Nanni Diesel | N2.14, N3.21, N4.38, T4 Serie | 10–300 PS | ~8 % |

### 1.4 Intervallsysteme: Betriebsstunden vs. Zeit

Marine-Motoren werden nach **Betriebsstunden ODER Kalenderzeit** gewartet —
je nachdem, was zuerst eintritt. Dies ist entscheidend, da viele Yachtmotoren
nur 100–300 Stunden pro Saison laufen.

**Grundregel:**
```
Wartung fällig, wenn:
  Betriebsstunden seit letzter Wartung ≥ Intervall
  ODER
  Kalendermonate seit letzter Wartung ≥ 12
```

Ein Motor mit nur 50 Betriebsstunden, der 18 Monate nicht gewartet wurde,
benötigt dennoch Ölwechsel — das Öl hat durch Kondenswasser und Alterung
seine Schmiereigenschaften verloren.

### 1.5 Originalteile vs. Aftermarket

Die Frage „Original oder Nachbau?" ist im Marine-Bereich differenziert
zu betrachten:

**Immer Original verwenden:**
- Injektoren und Düsen
- Zylinderkopfdichtungen
- Turbolader-Komponenten
- Elektronische Steuergeräte
- Zahnriemen (wenn vorhanden)

**Aftermarket gleichwertig:**
- Ölfilter (z.B. Fleetguard, MANN)
- Impeller (z.B. Jabsco, Johnson)
- Keilriemen (z.B. Continental, Gates)
- Zinkanoden
- Kühlmittel (sofern Spezifikation eingehalten)

**Aftermarket mit Vorsicht:**
- Kraftstofffilter (Racor-Einsätze sind Standard, aber Filterfeinheit beachten)
- Thermostate (müssen exakte Öffnungstemperatur haben)
- Dichtungssätze (Material und Toleranzen kritisch)

---
---

## 2. Wartungsintervalle nach Betriebsstunden

### 2.1 Universelle Intervallübersicht

Die folgende Tabelle zeigt die herstellerübergreifend geltenden
Standardintervalle. Herstellerspezifische Abweichungen werden in den
Unterkapiteln 2.2–2.5 detailliert.

#### 50-Stunden-Intervall (Erstservice / Einlaufphase)

| Aufgabe | Gültig für | Hinweis |
|---------|-----------|---------|
| Motoröl wechseln | Alle | Einlauföl enthält Metallabrieb |
| Ölfilter wechseln | Alle | Immer mit Ölwechsel |
| Schraubenmomente Zylinderkopf prüfen | Alle | Nur bei Erstinbetriebnahme |
| Ventilspiel prüfen | Alle | Setzt sich nach Einlauf |
| Keilriemenspannung prüfen | Alle | Neuer Riemen dehnt sich |
| Alle Schlauchklemmen nachziehen | Alle | Vibration lockert neue Verbindungen |
| Motorlager-Schrauben prüfen | Alle | Erste Setzung |
| Kraftstoffsystem entlüften und prüfen | Alle | Undichtigkeiten finden |
| Kühlmittelstand prüfen | Alle | Luftblasen entweichen beim Einlauf |
| Getriebeöl prüfen | Alle | Auf metallischen Abrieb achten |

#### 100-Stunden-Intervall (oder jährlich)

| Aufgabe | Yanmar | Volvo Penta | Beta | Nanni |
|---------|--------|------------|------|-------|
| Motoröl wechseln | ✓ (250h) | ✓ | ✓ | ✓ |
| Ölfilter wechseln | ✓ (250h) | ✓ | ✓ | ✓ |
| Kraftstoff-Vorfilter prüfen/reinigen | ✓ | ✓ | ✓ | ✓ |
| Impeller prüfen | ✓ | ✓ | ✓ | ✓ |
| Keilriemen prüfen | ✓ | ✓ | ✓ | ✓ |
| Kühlmittelstand prüfen | ✓ | ✓ | ✓ | ✓ |
| Luftfilter reinigen | ✓ | ✓ | ✓ | ✓ |
| Zinkanoden prüfen | ✓ | ✓ | ✓ | ✓ |

**Hinweis Yanmar:** Die 1GM/2YM/3YM-Serien haben offizielle 250h-Intervalle
für Öl und Filter. In der Praxis empfehlen erfahrene Yanmar-Mechaniker
dennoch 150–200h oder jährlich.

#### 250-Stunden-Intervall (oder jährlich)

| Aufgabe | Yanmar | Volvo Penta | Beta | Nanni |
|---------|--------|------------|------|-------|
| Motoröl wechseln | ✓ | (bei 200h) | ✓ | ✓ |
| Ölfilter wechseln | ✓ | ✓ | ✓ | ✓ |
| Kraftstoff-Hauptfilter wechseln | ✓ | ✓ | ✓ | ✓ |
| Kraftstoff-Vorfilter wechseln | ✓ | ✓ | ✓ | ✓ |
| Impeller wechseln | ✓ | ✓ | ✓ | ✓ |
| Keilriemen wechseln | Prüfen | Prüfen | Prüfen | Prüfen |
| Ventilspiel prüfen | ✓ | ✓ | ✓ | ✓ |
| Zinkanoden wechseln (wenn >50 % abgetragen) | ✓ | ✓ | ✓ | ✓ |
| Thermostat prüfen | ✓ | — | ✓ | ✓ |
| Getriebeöl wechseln | ✓ | ✓ | ✓ | ✓ |
| Keilriemenspannung einstellen | ✓ | ✓ | ✓ | ✓ |

#### 500-Stunden-Intervall (oder alle 2 Jahre)

| Aufgabe | Yanmar | Volvo Penta | Beta | Nanni |
|---------|--------|------------|------|-------|
| Keilriemen wechseln | ✓ | ✓ | ✓ | ✓ |
| Kühlmittel wechseln | ✓ | ✓ (1000h) | ✓ | ✓ |
| Kühlsystem spülen | ✓ | — | ✓ | ✓ |
| Thermostat wechseln | ✓ | ✓ | ✓ | ✓ |
| Wärmetauscher inspizieren | ✓ | ✓ | ✓ | ✓ |
| Kraftstoffleitungen prüfen | ✓ | ✓ | ✓ | ✓ |
| Abgaskrümmer/Mischer inspizieren | ✓ | ✓ | ✓ | ✓ |
| Motorlager prüfen | ✓ | ✓ | ✓ | ✓ |
| Elektrik-Anschlüsse prüfen | ✓ | ✓ | ✓ | ✓ |
| Kompression messen | Empfohlen | Empfohlen | Empfohlen | Empfohlen |

#### 1.000-Stunden-Intervall (oder alle 4–5 Jahre)

| Aufgabe | Yanmar | Volvo Penta | Beta | Nanni |
|---------|--------|------------|------|-------|
| Kühlmittel wechseln | ✓ | ✓ | ✓ | ✓ |
| Kühlsystem komplett spülen | ✓ | ✓ | ✓ | ✓ |
| Wärmetauscher reinigen (Seewasserseite) | ✓ | ✓ | ✓ | ✓ |
| Injektoren prüfen/überholen | ✓ | ✓ | ✓ | ✓ |
| Turbolader inspizieren (wenn vorhanden) | ✓ | ✓ | ✓ | ✓ |
| Abgaskrümmer/Mischer ersetzen prüfen | ✓ | ✓ | ✓ | ✓ |
| Starter und Lichtmaschine prüfen | ✓ | ✓ | ✓ | ✓ |
| Motorlager ersetzen prüfen | ✓ | ✓ | ✓ | ✓ |
| Zahnriemen wechseln (wenn vorhanden) | — | ✓ (D3!) | — | — |
| Seewasserpumpe komplett überholen | ✓ | ✓ | ✓ | ✓ |
| Alle Schläuche inspizieren und ggf. ersetzen | ✓ | ✓ | ✓ | ✓ |

#### 2.000-Stunden-Intervall (oder alle 8–10 Jahre)

| Aufgabe | Yanmar | Volvo Penta | Beta | Nanni |
|---------|--------|------------|------|-------|
| Wärmetauscher ersetzen | Prüfen | Prüfen | Prüfen | Prüfen |
| Abgaskrümmer/Mischer ersetzen | ✓ | ✓ | ✓ | ✓ |
| Seewasserpumpe ersetzen (komplett) | ✓ | ✓ | ✓ | ✓ |
| Injektoren ersetzen | Prüfen | ✓ | Prüfen | Prüfen |
| Alle Schläuche ersetzen | ✓ | ✓ | ✓ | ✓ |
| Grundüberholung erwägen | Prüfen | Prüfen | Prüfen | Prüfen |
| Turbolader überholen | Prüfen | Prüfen | Prüfen | Prüfen |
| Kompression messen und dokumentieren | ✓ | ✓ | ✓ | ✓ |
| Motorlager ersetzen | ✓ | ✓ | ✓ | ✓ |
| Kabelbaum inspizieren | ✓ | ✓ | ✓ | ✓ |

### 2.2 Yanmar — Spezifische Wartungsintervalle

#### Yanmar 1GM10 / 2YM15 / 3YM20 / 3YM30

Diese kompakten Segelboot-Hilfsantriebe (9–29 PS) sind die meistverbreiteten
Marine-Diesel in der europäischen Segelschifffahrt.

**Ölwechselintervall:**
- Yanmar Werksvorgabe: 250 Betriebsstunden oder jährlich
- Praxis-Empfehlung: 150–200 Stunden oder jährlich
- Erstservice: 50 Stunden

**Ölmenge und -typ:**
| Motor | Ölmenge (mit Filter) | Öltyp | Viskosität |
|-------|---------------------|-------|-----------|
| 1GM10 | 1,3 Liter | CF/CD | 15W-40 |
| 2YM15 | 2,0 Liter | CF/CD | 15W-40 |
| 3YM20 | 3,0 Liter | CF/CD | 15W-40 |
| 3YM30 | 3,0 Liter | CF/CD | 15W-40 |
| 3JH40 | 3,6 Liter | CH-4 | 15W-40 |
| 3JH57 | 3,6 Liter | CH-4 | 15W-40 |
| 4JH45 | 5,1 Liter | CH-4 | 15W-40 |
| 4JH57 | 5,1 Liter | CH-4 | 15W-40 |
| 4JH80 | 5,6 Liter | CH-4 | 15W-40 |
| 4JH110 | 6,5 Liter | CH-4 | 15W-40 |
| 4LHA-STP | 8,8 Liter | CH-4 | 15W-40 |
| 4LHA-DTP | 8,8 Liter | CH-4 | 15W-40 |
| 6LY-STP | 13,0 Liter | CH-4 | 15W-40 |
| 6LY-UTP | 13,0 Liter | CH-4 | 15W-40 |
| 6LY3-ETP | 16,5 Liter | CJ-4 | 15W-40 |

**Yanmar-Teilenummern (Genuine):**
| Motor | Ölfilter | Kraftstofffilter | Impeller |
|-------|---------|-----------------|----------|
| 1GM10 | 119305-35151 | 104500-55710 | 128176-42071 |
| 2YM15 | 119305-35151 | 104500-55710 | 128176-42071 |
| 3YM20 | 119305-35170 | 104500-55710 | 128990-42200 |
| 3YM30 | 119305-35170 | 104500-55710 | 128990-42200 |
| 3JH40 | 119305-35170 | 129470-55810 | 129470-42530 |
| 3JH57 | 119305-35170 | 129470-55810 | 129470-42530 |
| 4JH45 | 129150-35170 | 129470-55810 | 129470-42530 |
| 4JH57 | 129150-35170 | 129470-55810 | 129470-42530 |
| 4JH80 | 129150-35170 | 129470-55810 | 129470-42530 |
| 4JH110 | 129150-35170 | 129470-55810 | 129470-42530 |
| 4LHA-STP | 119593-35400 | 129574-55711 | 119773-42600 |
| 6LY-STP | 119593-35400 | 129574-55711 | 119773-42600 |

**Yanmar Ventilspiel (kalt, Motor aus):**
| Motor | Einlass | Auslass |
|-------|---------|---------|
| 1GM10 | 0,20 mm | 0,20 mm |
| 2YM15 | 0,20 mm | 0,20 mm |
| 3YM20/30 | 0,20 mm | 0,20 mm |
| 3JH-Serie | 0,20 mm | 0,20 mm |
| 4JH-Serie | 0,20 mm | 0,20 mm |
| 4LHA-Serie | 0,10 mm | 0,30–0,50 mm* |
| 6LY-Serie | 0,20 mm | 0,25 mm |

*4LHA — Auslass variantenabhängig (Yanmar 4LHA-Betriebshandbuch, kalt): HTP/HTZP = 0,30 mm, DTP/DTZP = 0,40 mm, STP/STZP = 0,50 mm; Einlass durchgängig 0,10 mm.

> ✅ Aufgeloest (Audit): 4LHA Ventilspiel (kalt) — Einlass 0,10 mm (alle Varianten), Auslass 0,30 mm (HTP), 0,40 mm (DTP) bzw. 0,50 mm (STP). Der frühere Wert 0,20/0,25 mm war falsch. Quelle: Yanmar 4LHA-HTP Operation Manual (Adjustment of Valve Clearance, Ventilspiel-Tabelle).

### 2.3 Volvo Penta — Spezifische Wartungsintervalle

#### Volvo Penta D1 / D2 Serie

Die D1/D2-Serie (13–75 PS) basiert auf kompakten Industriemotoren und ist
Standard in Segelbooten der 30–50-Fuß-Klasse.

**Ölwechselintervall:**
- Volvo Penta Werksvorgabe: 200 Betriebsstunden oder jährlich
- Erstservice: 50 Stunden

**Ölmenge und -typ:**
| Motor | Ölmenge (mit Filter) | Öltyp | Viskosität |
|-------|---------------------|-------|-----------|
| D1-13 | 2,6 Liter | VDS-3 / CI-4 | 15W-40 |
| D1-20 | 2,6 Liter | VDS-3 / CI-4 | 15W-40 |
| D1-30 | 3,5 Liter | VDS-3 / CI-4 | 15W-40 |
| D2-40 | 4,5 Liter | VDS-4 / CJ-4 | 15W-40 |
| D2-50 | 4,5 Liter | VDS-4 / CJ-4 | 15W-40 |
| D2-55 | 4,5 Liter | VDS-4.5 / CK-4 | 15W-40 |
| D2-60 | 4,5 Liter | VDS-4.5 / CK-4 | 15W-40 |
| D2-75 | 5,2 Liter | VDS-4.5 / CK-4 | 15W-40 |

#### Volvo Penta D3 / D4 / D6 Serie

**ACHTUNG — ZAHNRIEMEN D3:**
Der Volvo Penta D3 (110–220 PS) ist der einzige gängige Marine-Diesel mit
Zahnriemen (Timing Belt). Ein Zahnriemenriss führt zum sofortigen
Totalschaden des Motors (Ventile treffen Kolben → „Biegeventile").

```
╔══════════════════════════════════════════════════════════════╗
║  KRITISCH: Volvo Penta D3 Zahnriemen                       ║
║                                                              ║
║  Wechselintervall: 1.000 Betriebsstunden ODER 5 Jahre       ║
║  (was zuerst eintritt!)                                      ║
║                                                              ║
║  Volvo Penta Teilenummer: 3583895                            ║
║  Spannrolle: 3583897                                         ║
║  Umlenkrolle: 3583896                                        ║
║                                                              ║
║  Immer Zahnriemen UND beide Rollen zusammen wechseln!        ║
║  Arbeitszeit: 4–6 Stunden (Motorraum-abhängig)               ║
║  Kosten: Material ~350 EUR + Arbeit ~600–1.000 EUR           ║
║                                                              ║
║  Totalschaden bei Versäumnis: 15.000–25.000 EUR              ║
╚══════════════════════════════════════════════════════════════╝
```

**Ölmenge und -typ D3/D4/D6:**
| Motor | Ölmenge (mit Filter) | Öltyp | Viskosität |
|-------|---------------------|-------|-----------|
| D3-110 | 8,0 Liter | VDS-4.5 / CK-4 | 5W-30 |
| D3-150 | 8,0 Liter | VDS-4.5 / CK-4 | 5W-30 |
| D3-170 | 8,0 Liter | VDS-4.5 / CK-4 | 5W-30 |
| D3-220 | 8,0 Liter | VDS-4.5 / CK-4 | 5W-30 |
| D4-180 | 10,5 Liter | VDS-4.5 / CK-4 | 15W-40 |
| D4-210 | 10,5 Liter | VDS-4.5 / CK-4 | 15W-40 |
| D4-225 | 10,5 Liter | VDS-4.5 / CK-4 | 15W-40 |
| D4-260 | 10,5 Liter | VDS-4.5 / CK-4 | 15W-40 |
| D4-300 | 10,5 Liter | VDS-4.5 / CK-4 | 15W-40 |
| D6-280 | 18,0 Liter | VDS-4.5 / CK-4 | 15W-40 |
| D6-310 | 18,0 Liter | VDS-4.5 / CK-4 | 15W-40 |
| D6-330 | 18,0 Liter | VDS-4.5 / CK-4 | 15W-40 |
| D6-370 | 18,0 Liter | VDS-4.5 / CK-4 | 15W-40 |
| D6-400 | 18,0 Liter | VDS-4.5 / CK-4 | 15W-40 |
| D6-440 | 18,0 Liter | VDS-4.5 / CK-4 | 15W-40 |

**Volvo Penta Teilenummern (Genuine):**
| Motor | Ölfilter | Kraftstofffilter | Impeller |
|-------|---------|-----------------|----------|
| D1-13/20 | 3840525 | 3840335 | 3593573 |
| D1-30 | 3840525 | 3840335 | 3593573 |
| D2-40/50 | 21549544 | 21624740 | 3593660 |
| D2-55/60/75 | 21549544 | 21624740 | 3593660 |
| D3-110–220 | 22030848 | 21718912 | 21951346 |
| D4-180–300 | 22030848 | 21718912 | 21951346 |
| D6-280–440 | 21632901 | 21718912 | 3588475 |

**Volvo Penta Ventilspiel (kalt, Motor aus):**
| Motor | Einlass | Auslass |
|-------|---------|---------|
| D1-13/20 | 0,20 mm | 0,20 mm |
| D1-30 | 0,20 mm | 0,20 mm |
| D2-40/50 | 0,20 mm | 0,35 mm |
| D2-55/60/75 | 0,20 mm | 0,20 mm |
| D3-Serie | Hydraulisch (kein Einstellen) | Hydraulisch |
| D4-Serie | 0,30 mm | 0,55 mm |
| D6-Serie | 0,30 mm | 0,55 mm |

### 2.4 Beta Marine — Spezifische Wartungsintervalle

Beta Marine verwendet Kubota-Industriemotoren als Basis und marinisiert
diese im eigenen Werk in Gloucester, England. Die Motoren gelten als
besonders robust und wartungsfreundlich.

**Ölwechselintervall:**
- Beta Marine Werksvorgabe: 250 Betriebsstunden oder jährlich
- Erstservice: 25–50 Stunden

**Ölmenge und -typ:**
| Motor | Ölmenge (mit Filter) | Öltyp | Viskosität |
|-------|---------------------|-------|-----------|
| Beta 14 | 2,5 Liter | CF/CD | 15W-40 |
| Beta 16 | 2,5 Liter | CF/CD | 15W-40 |
| Beta 20 | 3,5 Liter | CF/CD | 15W-40 |
| Beta 25 | 3,5 Liter | CF/CD | 15W-40 |
| Beta 30 | 3,5 Liter | CF/CD | 15W-40 |
| Beta 35 | 4,5 Liter | CF/CD | 15W-40 |
| Beta 38 | 4,5 Liter | CF/CD | 15W-40 |
| Beta 43 | 5,8 Liter | CH-4 | 15W-40 |
| Beta 50 | 5,8 Liter | CH-4 | 15W-40 |
| Beta 60 | 7,5 Liter | CH-4 | 15W-40 |
| Beta 75 | 7,5 Liter | CH-4 | 15W-40 |
| Beta 90 | 9,0 Liter | CH-4 | 15W-40 |
| Beta 105 | 9,0 Liter | CH-4 | 15W-40 |
| Beta 115 | 10,5 Liter | CJ-4 | 15W-40 |
| Beta 150 | 12,0 Liter | CJ-4 | 15W-40 |

**Beta Marine Teilenummern (Genuine):**
| Motor | Ölfilter | Kraftstofffilter | Impeller |
|-------|---------|-----------------|----------|
| Beta 14–20 | 211-63250 | 211-63240 | 211-60001 |
| Beta 25–30 | 211-63250 | 211-63240 | 211-60001 |
| Beta 35–38 | 211-63250 | 211-63241 | 211-60002 |
| Beta 43–50 | 211-63252 | 211-63241 | 211-60002 |
| Beta 60–75 | 211-63252 | 211-63242 | 211-60003 |
| Beta 90–105 | 211-63253 | 211-63242 | 211-60003 |
| Beta 115–150 | 211-63253 | 211-63243 | 211-60004 |

**Beta Marine Ventilspiel (kalt, Motor aus):**
| Motor | Einlass | Auslass |
|-------|---------|---------|
| Beta 14–30 (3-Zylinder) | 0,15 mm | 0,15 mm |
| Beta 35–50 (4-Zylinder) | 0,18 mm | 0,18 mm |
| Beta 60–105 (4-Zylinder) | 0,20 mm | 0,20 mm |
| Beta 115–150 (4-Zylinder Turbo) | 0,20 mm | 0,25 mm |

### 2.5 Nanni Diesel — Spezifische Wartungsintervalle

Nanni Diesel (heute Nanni Industries) verwendet verschiedene Basisblöcke
(Toyota, Kubota) und ist besonders in Frankreich und im Mittelmeerraum
verbreitet.

**Ölwechselintervall:**
- Nanni Werksvorgabe: 200 Betriebsstunden oder jährlich
- Erstservice: 50 Stunden

**Ölmenge und -typ:**
| Motor | Ölmenge (mit Filter) | Öltyp | Viskosität |
|-------|---------------------|-------|-----------|
| N2.10 | 1,8 Liter | CF/CD | 15W-40 |
| N2.14 | 2,2 Liter | CF/CD | 15W-40 |
| N3.21 | 3,3 Liter | CF/CD | 15W-40 |
| N3.30 | 3,8 Liter | CH-4 | 15W-40 |
| N4.38 | 5,0 Liter | CH-4 | 15W-40 |
| N4.50 | 5,5 Liter | CH-4 | 15W-40 |
| N4.60 | 6,2 Liter | CH-4 | 15W-40 |
| N4.80 | 7,0 Liter | CJ-4 | 15W-40 |
| N4.100 | 8,5 Liter | CJ-4 | 15W-40 |
| T4.155 | 10,0 Liter | CJ-4 | 15W-40 |
| T4.180 | 10,0 Liter | CJ-4 | 15W-40 |
| T4.200 | 12,0 Liter | CJ-4 | 15W-40 |
| T4.230 | 12,0 Liter | CK-4 | 15W-40 |
| T4.270 | 14,0 Liter | CK-4 | 15W-40 |

**Nanni Diesel Teilenummern (Genuine):**
| Motor | Ölfilter | Kraftstofffilter | Impeller |
|-------|---------|-----------------|----------|
| N2.10/14 | 970312711 | 970311102 | 970305401 |
| N3.21/30 | 970312721 | 970311102 | 970305401 |
| N4.38/50 | 970312731 | 970311103 | 970305402 |
| N4.60/80 | 970312731 | 970311104 | 970305403 |
| N4.100 | 970312741 | 970311104 | 970305403 |
| T4.155–270 | 970312751 | 970311105 | 970305404 |

**Nanni Diesel Ventilspiel (kalt, Motor aus):**
| Motor | Einlass | Auslass |
|-------|---------|---------|
| N2-Serie | 0,15 mm | 0,15 mm |
| N3-Serie | 0,18 mm | 0,18 mm |
| N4-Serie | 0,20 mm | 0,20 mm |
| T4-Serie | 0,20 mm | 0,25 mm |

### 2.6 Wartungsmatrix — Kostenabschätzung pro Intervall

| Intervall | Material (EUR) | Arbeitszeit (h) | Gesamtkosten (EUR) |
|-----------|---------------|-----------------|-------------------|
| 50h (Erstservice) | 50–120 | 1–2 | 150–350 |
| 100h (Ölwechsel) | 40–80 | 0,5–1 | 80–180 |
| 250h (Standardservice) | 120–280 | 2–4 | 350–750 |
| 500h (Großer Service) | 250–500 | 4–8 | 700–1.500 |
| 1.000h (Majorservice) | 500–1.500 | 8–16 | 1.500–4.000 |
| 2.000h (Revision) | 2.000–6.000 | 20–40 | 5.000–12.000 |

---
---

## 3. Motoröl — Typen, Spezifikationen und Analyse

### 3.1 Öltypen im Vergleich

#### Mineralöl

Mineralöle sind die traditionelle Wahl für Marine-Diesel, insbesondere
für ältere Motoren ohne Turbolader.

**Eigenschaften:**
- Basis: raffiniertes Erdöl (Gruppe I/II)
- Viskosität: typisch 15W-40
- Ölwechselintervall: Standard (keine Verlängerung)
- Preis: 6–10 EUR/Liter
- Geeignet für: alle Saugmotoren, ältere Turbomotoren

**Vorteile:**
- Bewährt und zuverlässig
- Keine Kompatibilitätsprobleme mit alten Dichtungen
- Günstiger Preis
- Von allen Herstellern freigegeben

**Nachteile:**
- Schnellere Alterung bei hohen Temperaturen
- Geringere Scherstabilität
- Mehr Ablagerungen bei Unterlastbetrieb

**Empfohlene Produkte:**
- Shell Rimula R4 L 15W-40 (CI-4)
- Mobil Delvac MX 15W-40 (CH-4)
- Castrol Vecton 15W-40 (CJ-4)
- Total Rubia TIR 7400 15W-40 (CI-4)

#### Teilsynthetisches Öl

Teilsynthetische Öle bieten einen Kompromiss zwischen Leistung und Kosten.

**Eigenschaften:**
- Basis: Mineralöl + synthetische Anteile (Gruppe II/III)
- Viskosität: typisch 15W-40 oder 10W-40
- Ölwechselintervall: Standard
- Preis: 10–16 EUR/Liter
- Geeignet für: alle modernen Marine-Diesel

**Vorteile:**
- Besserer Verschleißschutz als Mineralöl
- Stabilere Viskosität über Temperaturbereich
- Weniger Ablagerungen

**Nachteile:**
- Teurer als Mineralöl
- Kein signifikant längeres Ölwechselintervall
- Nicht immer nötig für Saugmotoren

**Empfohlene Produkte:**
- Shell Rimula R5 E 10W-40 (CI-4)
- Mobil Delvac MX Extra 10W-40 (CI-4)
- Castrol Vecton Long Drain 10W-40 (CJ-4)

#### Vollsynthetisches Öl

Vollsynthetische Öle werden für moderne Common-Rail-Motoren mit
engen Toleranzen empfohlen.

**Eigenschaften:**
- Basis: synthetisch (Gruppe III/IV/V)
- Viskosität: 5W-30, 5W-40 oder 10W-30
- Ölwechselintervall: teilweise verlängerbar
- Preis: 16–28 EUR/Liter
- Geeignet für: D3, moderne Common-Rail-Motoren

**Vorteile:**
- Beste Fließeigenschaften bei Kaltstart
- Höchste Scherstabilität
- Geringste Ablagerungsneigung
- Bester Schutz bei hohen Temperaturen

**Nachteile:**
- Hoher Preis
- Bei alten Motoren (vor 2000) können Dichtungen quellen/schrumpfen
- Nicht für alle Motoren freigegeben

**Empfohlene Produkte (für Volvo Penta D3):**
- Volvo Penta Genuine Engine Oil 5W-30 (VDS-4.5)
- Shell Rimula R6 LME 5W-30 (CK-4)
- Mobil Delvac 1 5W-40 (CJ-4)

### 3.2 Viskositätsklassen: 15W-40 vs. 10W-30 vs. 5W-30

| Parameter | 15W-40 | 10W-30 | 5W-30 |
|-----------|--------|--------|-------|
| Pumpbar ab | −15 °C | −25 °C | −30 °C |
| Kaltstart-Schutz | Gut | Sehr gut | Ausgezeichnet |
| Filmstärke bei 100 °C | Hoch | Mittel | Mittel |
| Geeignet für Tropen | Ja | Bedingt | Nein |
| Geeignet für Nordeuropa Winter | Bedingt | Ja | Ja |
| Kraftstoffersparnis | Basis | +1–2 % | +2–3 % |
| Ölverbrauch bei alten Motoren | Gering | Mittel | Hoch |

**Empfehlung nach Einsatzgebiet:**
- **Mittelmeer/Tropen**: 15W-40 (dickerer Film bei Hitze)
- **Nordeuropa, Sommersaison**: 15W-40 oder 10W-40
- **Nordeuropa, Ganzjahresbetrieb**: 10W-30 oder 10W-40
- **Volvo D3 (alle Regionen)**: 5W-30 (Herstellervorgabe!)

### 3.3 Ölanalyse — Zustandsüberwachung durch Labortest

Ölanalyse (Oil Analysis, Tribologie) ist das effektivste Frühwarnsystem
für Motorprobleme. Durch Analyse der Verschleißmetalle, Additive und
Verunreinigungen im Altöl können Probleme erkannt werden, bevor sie
zu Ausfällen führen.

**Was wird gemessen:**

| Parameter | Normal | Warnung | Kritisch | Mögliche Ursache |
|-----------|--------|---------|----------|-----------------|
| Eisen (Fe) | <50 ppm | 50–100 ppm | >100 ppm | Zylinder, Nockenwelle, Zahnräder |
| Kupfer (Cu) | <20 ppm | 20–40 ppm | >40 ppm | Lager, Buchsen, Ölkühler |
| Blei (Pb) | <15 ppm | 15–30 ppm | >30 ppm | Pleuellager, Hauptlager |
| Aluminium (Al) | <15 ppm | 15–30 ppm | >30 ppm | Kolben, Lagerschalen |
| Chrom (Cr) | <5 ppm | 5–15 ppm | >15 ppm | Kolbenringe, Ventilschäfte |
| Zinn (Sn) | <10 ppm | 10–20 ppm | >20 ppm | Lagerbeschichtung |
| Silizium (Si) | <15 ppm | 15–30 ppm | >30 ppm | Schmutz/Staub, defekter Luftfilter |
| Natrium (Na) | <20 ppm | 20–50 ppm | >50 ppm | Kühlmittel-Leck |
| Kalium (K) | <20 ppm | 20–50 ppm | >50 ppm | Kühlmittel-Leck |
| Wasser | <0,1 % | 0,1–0,3 % | >0,3 % | Kondenswasser, Dichtung |
| Kraftstoff | <2 % | 2–5 % | >5 % | Injektor-Leck, Kolbenringe |
| Ruß (Soot) | <1 % | 1–3 % | >3 % | Unterlast, Injektoren |
| TBN (Basenzahl) | >5 | 3–5 | <3 | Öl verbraucht, Intervall zu lang |
| TAN (Säurezahl) | <2 | 2–4 | >4 | Öl oxidiert, aggressive Verbrennungsprodukte |
| Viskosität @100 °C | ±10 % | ±10–20 % | >±20 % | Kraftstoffeintrag oder Oxidation |

**Anbieter für Ölanalyse:**
- **Oelcheck (Deutschland)**: 35–50 EUR pro Probe, marine-spezifische Auswertung
- **WearCheck/Spectro (UK)**: 25–40 GBP, internationaler Standard
- **Polaris Labs (USA/EU)**: 25–35 USD, große Datenbank
- **Bureau Veritas**: 40–60 EUR, professionelle Bewertung

**Probenahme-Anleitung:**
1. Motor warmfahren (min. 20 Minuten unter Last)
2. Motor abstellen
3. Probenahme sofort über Peilstab-Öffnung (nicht aus Ablass)
4. Spezielle Probenahme-Spritze verwenden (im Analysekit enthalten)
5. Flasche sofort verschließen, Formular ausfüllen
6. Per Post an Labor senden
7. Ergebnis nach 3–5 Werktagen

**Kosten-Nutzen:**
- Analyse: 35–50 EUR pro Probe
- Frühwarnung erspart: 2.000–20.000 EUR Reparaturkosten
- Empfehlung: jährlich ODER alle 250 Betriebsstunden

### 3.4 Ölwechsel-Prozedur

**Benötigtes Material:**
- Motoröl (richtige Menge und Spezifikation)
- Neuer Ölfilter
- Ölfilter-Schlüssel (passend)
- Ölabsaugpumpe (Reverso, Jabsco oder manuelle Pumpe)
- Auffangbehälter (Altöl)
- Lappen, Ölbindemittel
- Dichtring für Ablassschraube (wenn Ablassschraube verwendet wird)

**Schritt-für-Schritt:**

1. **Motor warmfahren** (15–20 Minuten unter Last)
   - Warmes Öl fließt besser, Partikel sind in Suspension
2. **Motor abstellen**
3. **Öl absaugen** über Peilstab-Öffnung
   - Absaugpumpe einführen bis zum Boden der Ölwanne
   - Pumpe betätigen bis kein Öl mehr kommt
   - ALTERNATIV: Ablassschraube öffnen (wenn zugänglich)
4. **Abgesaugte Menge prüfen** — muss der Soll-Menge entsprechen
   - Wenn weniger: Peilstab-Rohr verstopft oder Absaugschlauch zu kurz
5. **Ölfilter wechseln**
   - Alten Filter mit Filterschlüssel lösen
   - Dichtfläche am Motor reinigen
   - Neuen Filter-Dichtungsring leicht einölen
   - Neuen Filter handfest anziehen + ¾ Umdrehung
   - NICHT mit Werkzeug anziehen!
6. **Neues Öl einfüllen**
   - Richtige Menge laut Handbuch (mit Filter)
   - Über Einfüllstutzen einfüllen (Trichter verwenden)
7. **Ölstand prüfen**
   - Peilstab ziehen, abwischen, erneut einstecken, ablesen
   - Ölstand zwischen MIN und MAX Markierung
8. **Motor starten und 30 Sekunden laufen lassen**
   - Öldruckwarnleuchte muss nach 3–5 Sekunden erlöschen
   - Auf Undichtigkeiten am Filter prüfen
9. **Motor abstellen, 5 Minuten warten, Ölstand erneut prüfen**
   - Nachfüllen bis MAX-Markierung
10. **Dokumentieren**
    - Betriebsstunden, Datum, Ölsorte, Menge im Wartungsbuch eintragen

### 3.5 Ölwechsel über Ablassschraube vs. Absaugpumpe

| Methode | Vorteile | Nachteile |
|---------|---------|-----------|
| Absaugpumpe | Sauber, kein Tropfen in der Bilge, einfach | Nicht 100 % Entleerung, Schlauch kann verstopfen |
| Ablassschraube | Vollständige Entleerung, gründlicher | Bilge verschmutzbar, schwer zugänglich, Dichtring nötig |

**Empfehlung:** Absaugpumpe als Standard, alle 3–4 Wechsel zusätzlich über
Ablassschraube (um Bodensatz zu entfernen).

---
---

## 4. Ölfilter — Genuine und Aftermarket

### 4.1 Filterbauarten im Marine-Bereich

**Anschraubfilter (Spin-on):**
- Standard bei 95 % aller Marine-Diesel
- Einteilig, Filtermedium + Gehäuse als Einheit
- Einfacher Wechsel: abschrauben, neuen aufschrauben
- Rücklaufventil verhindert Öl-Rücklauf bei Stillstand

**Filtereinsatz (Cartridge):**
- Selten bei Marine-Diesel (einige Volvo Penta D-Serie)
- Nur Filtereinsatz wird gewechselt, Gehäuse bleibt
- Umweltfreundlicher (weniger Metallabfall)
- Aufwändigerer Wechsel (Gehäuse öffnen, reinigen)

### 4.2 Filtermedien und Filterfeinheit

| Filtertyp | Filterfeinheit | Rückhaltegrad | Einsatz |
|-----------|---------------|--------------|---------|
| Zellulose | 20–25 µm | 95 % @20 µm | Standard OEM |
| Zellulose/Synthetik Kombi | 15–20 µm | 98 % @20 µm | Premium OEM |
| Vollsynthetisch | 10–15 µm | 99 % @15 µm | High-End Aftermarket |

### 4.3 Cross-Reference: Genuine → Aftermarket

#### Yanmar Ölfilter Cross-Reference

| Yanmar Genuine | MANN | Fleetguard | Hengst | Preis Genuine | Preis Aftermarket |
|---------------|------|-----------|--------|--------------|------------------|
| 119305-35151 | W 67/1 | LF3462 | H97W06 | 18–22 EUR | 6–10 EUR |
| 119305-35170 | W 712/83 | LF3586 | H14W30 | 22–28 EUR | 8–12 EUR |
| 129150-35170 | W 920/17 | LF3806 | H17W20 | 28–35 EUR | 10–15 EUR |
| 119593-35400 | W 940/44 | LF3806 | H17W23 | 35–45 EUR | 12–18 EUR |

#### Volvo Penta Ölfilter Cross-Reference

| Volvo Genuine | MANN | Fleetguard | Hengst | Preis Genuine | Preis Aftermarket |
|--------------|------|-----------|--------|--------------|------------------|
| 3840525 | W 712/83 | LF3586 | H14W30 | 25–32 EUR | 8–12 EUR |
| 21549544 | W 940/62 | LF3806 | H17W23 | 32–42 EUR | 12–18 EUR |
| 22030848 | HU 816 x | LF16250 | E108H D227 | 38–48 EUR | 15–22 EUR |
| 21632901 | W 11 102/37 | LF3972 | H19W10 | 42–55 EUR | 18–25 EUR |

#### Beta Marine Ölfilter Cross-Reference

| Beta Genuine | MANN | Fleetguard | Kubota Equiv. | Preis Genuine | Preis Aftermarket |
|-------------|------|-----------|--------------|--------------|------------------|
| 211-63250 | W 67/1 | LF3462 | HH150-32094 | 16–20 EUR | 6–10 EUR |
| 211-63252 | W 712/83 | LF3586 | HH164-32430 | 22–28 EUR | 8–12 EUR |
| 211-63253 | W 920/17 | LF3806 | HH1C0-32430 | 28–35 EUR | 10–15 EUR |

#### Nanni Diesel Ölfilter Cross-Reference

| Nanni Genuine | MANN | Fleetguard | Preis Genuine | Preis Aftermarket |
|--------------|------|-----------|--------------|------------------|
| 970312711 | W 67/1 | LF3462 | 18–24 EUR | 6–10 EUR |
| 970312721 | W 712/83 | LF3586 | 24–30 EUR | 8–12 EUR |
| 970312731 | W 920/17 | LF3806 | 30–38 EUR | 10–15 EUR |
| 970312741 | W 940/44 | LF3806 | 35–45 EUR | 12–18 EUR |
| 970312751 | W 11 102/37 | LF3972 | 40–52 EUR | 18–25 EUR |

### 4.4 Filterwechsel-Fehler und ihre Folgen

| Fehler | Folge | Vermeidung |
|--------|-------|-----------|
| Filter zu fest angezogen | Dichtung verformt, Leck beim nächsten Wechsel | Handfest + ¾ Umdrehung, kein Werkzeug |
| Dichtung nicht eingeölt | Trockenlauf der Dichtung, undicht | Dichtring leicht mit neuem Öl einölen |
| Alter Dichtring am Motor verblieben | Doppeldichtung → sofortiges Leck | Kontrolle: alter Dichtring muss am alten Filter sein |
| Falscher Filter verwendet | Zu wenig Durchfluss, Bypass öffnet | Teilenummer prüfen, Cross-Reference verwenden |
| Filter nicht vorgefüllt | 5–8 Sek. Trockenlauf beim Start | Bei waagerechtem Einbau vorfüllen |

---
---

## 5. Kraftstofffilter und Wasserabscheider

### 5.1 Zweistufige Kraftstofffiltration

Marine-Diesel erfordern zwingend eine zweistufige Kraftstofffiltration:

```
Tank → Vorfilter/Wasserabscheider (10–30 µm) → Feinfilter am Motor (2–5 µm) → Injektoren
         ↓                                          ↓
    Wasser + Grobschmutz                      Feinpartikel
    entfernt                                  entfernt
```

**Warum zweistufig:**
- Marine-Diesel enthält fast immer Wasser (Kondensation im Tank)
- Wasser in Injektoren = sofortiger Schaden (2.000–8.000 EUR)
- Grobschmutz (Rost, Algen) würde Feinfilter sofort verstopfen
- Vorfilter = Sicherheitsnetz, Feinfilter = Präzisionsfilter

### 5.2 Vorfilter / Wasserabscheider

#### Racor-Filter (Branchenstandard)

Racor (Parker Hannifin) Turbine-Serie ist der De-facto-Standard für
Marine-Kraftstoff-Vorfilter.

| Modell | Durchfluss | Filterfeinheit | Anschluss | Einsatz |
|--------|-----------|---------------|-----------|---------|
| Racor 110A | 57 l/h | 10 µm (R12T) | M14×1,5 | Segelboote bis 30 PS |
| Racor 215R | 95 l/h | 10 µm (R15T) | M14×1,5 | Segelboote 30–60 PS |
| Racor 230R | 114 l/h | 10 µm (S3213) | 3/8" NPTF | Motorboote bis 100 PS |
| Racor 320R | 227 l/h | 10 µm (R30T) | 3/8" NPTF | Standard Segelboote |
| Racor 500FG | 227 l/h | 10 µm (2010TM) | 3/4"-16 UNF | Standard Motorboote |
| Racor 900FG | 341 l/h | 10 µm (2040TM) | 1"-12 UNF | Große Motorboote |
| Racor 1000FG | 681 l/h | 10 µm (2020TM) | 1"-12 UNF | Superyachten |

**Racor Filtereinsätze:**
| Einsatz | Filterfeinheit | Farbe Endscheibe | Einsatz |
|---------|---------------|-----------------|---------|
| R12T / 120RT | 10 µm | Braun | Racor 110A/120A |
| R15T | 10 µm | Braun | Racor 215R |
| R20T | 10 µm | Braun | Racor 220R |
| R25T | 10 µm | Braun | Racor 225R |
| S3213 | 10 µm | — | Racor 230R |
| 2010TM-OR | 10 µm | Braun | Racor 500FG |
| 2010SM-OR | 2 µm | Blau | Racor 500FG (Fein) |
| 2020TM-OR | 10 µm | Braun | Racor 1000FG |
| 2020SM-OR | 2 µm | Blau | Racor 1000FG (Fein) |
| 2040TM-OR | 10 µm | Braun | Racor 900FG |
| 2040SM-OR | 2 µm | Blau | Racor 900FG (Fein) |

**Wechselintervall Racor-Einsätze:**
- Sichtprüfung: transparente Schauglas-Schale prüfen
- Wasser ablassen: sobald Wasser sichtbar (wöchentlich prüfen!)
- Einsatz wechseln: alle 250 Betriebsstunden oder jährlich
- Bei Dieselpest (Algenbefall): sofort wechseln

#### Volvo Penta Vorfilter

| Modell | Genuine Teilenummer | Einsatz-Nr. | Anwendung |
|--------|-------------------|-------------|-----------|
| D1-Serie | 3862228 | 3862228 | Kompaktfilter mit Wasserabscheider |
| D2-Serie | 21380475 | 21380475 | Kompaktfilter mit Wasserabscheider |
| D3-Serie | 21718912 | 21718912 | Vorfilter mit Schauglas |
| D4/D6-Serie | 21718912 | 21718912 | Vorfilter mit Schauglas |

#### Yanmar Vorfilter

| Motor | Genuine Teilenummer | Beschreibung |
|-------|-------------------|-------------|
| 1GM/2YM/3YM | 104500-55710 | Kraftstofffilter-Element |
| 3JH-Serie | 129470-55810 | Kraftstofffilter-Element |
| 4JH-Serie | 129470-55810 | Kraftstofffilter-Element |
| 4LHA/6LY | 129574-55711 | Kraftstofffilter-Element |

### 5.3 Feinfilter am Motor (Sekundärfilter)

Der motormontierte Feinfilter ist die letzte Barriere vor den Injektoren.

**Filterfeinheit nach Einspritzsystem:**
| Einspritzsystem | Erforderliche Filterfeinheit | Toleranz Injektoren |
|----------------|----------------------------|-------------------|
| Mechanische Einspritzpumpe | 5–10 µm | 5–10 µm Spiel |
| Elektronische Pumpe-Düse | 3–5 µm | 3–5 µm Spiel |
| Common-Rail (1.600 bar) | 2–3 µm | 1–3 µm Spiel |
| Common-Rail (2.000+ bar) | 1–2 µm | <2 µm Spiel |

**Folgen eines verstopften Feinfilters:**
- Leistungsverlust (Motor bekommt zu wenig Kraftstoff)
- Ruckeln bei Last
- Kavitation in der Einspritzpumpe
- Luftziehen an der Filterflachdichtung
- Motor stirbt bei Lastaufnahme ab

### 5.4 Dieselpest — Mikrobieller Befall

Dieselpest (Diesel Bug) ist ein bakterieller/mykologischer Befall des
Kraftstoffs, der an der Wasser-Diesel-Grenzschicht im Tank wächst.

**Erreger:**
- Hormoconis resinae (Hauptverursacher)
- Cladosporium resinae
- Pseudomonas aeruginosa
- Sulfatreduzierende Bakterien (SRB)

**Symptome:**
- Dunkle Schlieren im Kraftstoff
- Brauner/schwarzer Schleim in Filtern
- Verstopfte Filter nach kurzer Zeit (<50h)
- Übler Geruch aus dem Tank (Schwefelwasserstoff)
- Korrosion im Tank (bei SRB)

**Behandlung:**
1. Tank vollständig entleeren und reinigen
2. Alle Filter wechseln
3. Biozid-Behandlung: Grotamar 82 (100 ml pro 200 l Diesel)
4. Dieselqualität verbessern: EN 590 zertifiziert tanken
5. Tankbelüftung mit Trockenmittelfilter
6. Langzeitprävention: Grotamar 82 bei jeder Betankung (25 ml/200 l)

### 5.5 Kraftstofffilter-Wechsel — Prozedur

**Benötigtes Material:**
- Neuer Filtereinsatz (Vor- UND Feinfilter)
- Dichtungen/O-Ringe (im Filterkit enthalten)
- Handpumpe zum Entlüften (wenn keine elektrische Förderpumpe)
- Lappen, Auffangschale
- Kraftstoff zum Vorfüllen

**Schritt-für-Schritt (Racor-Vorfilter):**
1. Kraftstoffhahn am Tank schließen
2. Schauglas-Schale abschrauben (Wasser ablassen)
3. Zentralschraube oben lösen
4. Filtereinsatz herausnehmen
5. Gehäuse innen reinigen (mit sauberem Diesel)
6. Neuen O-Ring einsetzen (leicht einölen)
7. Neuen Filtereinsatz einsetzen
8. Schauglas-Schale wieder anschrauben
9. Zentralschraube festziehen
10. Kraftstoffhahn öffnen
11. Entlüften (Handpumpe betätigen bis Widerstand spürbar)

**Schritt-für-Schritt (Motor-Feinfilter, Spin-On):**
1. Kraftstoffhahn schließen (wenn vorhanden)
2. Alten Filter abschrauben (Lappen darunter!)
3. Dichtfläche am Motor reinigen
4. Neuen Filter-Dichtring einölen
5. Neuen Filter handfest + ¾ Umdrehung anziehen
6. Kraftstoffhahn öffnen
7. System entlüften

**Entlüften des Kraftstoffsystems:**

Methode A — Handpumpe (bei mechanischer Einspritzung):
1. Entlüftungsschraube an der Einspritzpumpe lösen (½ Umdrehung)
2. Handpumpe betätigen, bis blasenfreier Kraftstoff austritt
3. Entlüftungsschraube festziehen
4. Handpumpe weiterbetätigen bis hart
5. Motor starten (kann einige Sekunden Anlasser brauchen)

Methode B — Elektrische Förderpumpe (bei Common-Rail):
1. Zündung einschalten (Motor nicht starten)
2. Förderpumpe läuft automatisch 30 Sekunden
3. 3× wiederholen (Zündung aus/ein)
4. Motor starten

### 5.6 Kraftstoffqualität und Additive

| Additiv-Typ | Zweck | Produkt (Beispiel) | Dosierung |
|-------------|-------|-------------------|-----------|
| Biozid | Gegen Dieselpest | Grotamar 82 | 100 ml/200 l (Behandlung) |
| Cetanbooster | Bessere Zündung | Liqui Moly Diesel Cetane Booster | 150 ml/75 l |
| Fließverbesserer | Winterfest | Liqui Moly Diesel Fließ-Fit | 150 ml/75 l |
| Injektorreiniger | Verkokung lösen | Liqui Moly Diesel Spülung | 500 ml/75 l |
| Stabilisator | Lagerung >3 Monate | Sta-Bil Diesel | 30 ml/10 l |
| Wasseremulgator | Wasser im Tank binden | Fuel Right Marine | 100 ml/200 l |

---
---

## 6. Impeller und Kühlwasserpumpen

### 6.1 Funktionsprinzip der Seewasser-Impellerpumpe

Die Seewasser-Impellerpumpe (auch „Flügelzellenpumpe" oder „Gummiflügelpumpe")
ist eine selbstansaugende Verdrängerpumpe, die Seewasser durch den
Wärmetauscher oder direkt durch den Motor fördert.

**Funktionsweise:**
```
     ┌─── Saugseite (Seewasser-Einlass)
     │
     │   ╔═══════════════╗
     │   ║  ┌──────────┐ ║
     ▼   ║  │ Impeller  │ ║
    ─────►║  │  ████████ │ ║──────► Druckseite (zum Wärmetauscher)
         ║  │ ████████  │ ║
         ║  └──────────┘ ║
         ╚═══════════════╝
              │
              ▼
         Exzentrisch gelagerter Rotor
         presst flexible Flügel zusammen
         → Verdrängungseffekt fördert Wasser
```

**Kritische Eigenschaft:** Der Impeller darf NIEMALS trocken laufen.
Bereits 10–15 Sekunden Trockenlauf können die Gummiflügel beschädigen.
Bei Winterlager oder Slipaufenthalt: Seeventil geschlossen = Motor
nicht starten!

### 6.2 Impeller-Materialien

| Material | Farbe | Temperaturbereich | Lebensdauer | Einsatz |
|----------|-------|------------------|-------------|---------|
| Neopren (CR) | Schwarz | -10 bis +80 °C | 1–3 Jahre | Standard, Seewasser |
| Nitril (NBR) | Schwarz/Braun | -20 bis +100 °C | 1–3 Jahre | Ölhaltige Medien |
| Polyurethan (PU) | Gelb/Orange | -5 bis +60 °C | 3–5 Jahre | Sandiges Wasser |
| EPDM | Schwarz | -30 bis +130 °C | 2–4 Jahre | Süßwasser, Kühlmittel |

**Standard im Marine-Bereich:** Neopren für Seewasser, EPDM für Süßwasserkühlung.

### 6.3 Jabsco und Johnson Pumpen — Die zwei Haupthersteller

#### Jabsco (Xylem)

Jabsco ist der weltweit größte Hersteller von Marine-Impellerpumpen.
Die meisten Marine-Diesel verwenden Jabsco-Pumpen oder kompatible Kopien.

**Häufige Jabsco-Pumpen in Marine-Diesel:**
| Jabsco Modell | Impeller-Nr. | Flügel | Durchfluss | Einbau bei |
|--------------|-------------|--------|-----------|-----------|
| 29460-0001 | 1210-0001-P | 12 | 12 l/min | Yanmar 1GM/2YM |
| 29470-0001 | 1210-0001-P | 12 | 15 l/min | Yanmar 3YM |
| 29500-1001 | 4528-0001-P | 9 | 25 l/min | Yanmar 3JH/4JH |
| 29500-1201 | 4528-0001-P | 9 | 28 l/min | Volvo D1/D2 |
| 29610-1001 | 6303-0001-P | 6 | 40 l/min | Volvo D3/D4 |
| 29630-1001 | 17936-0001-P | 6 | 65 l/min | Volvo D6 |
| 29440-0001 | 920-0001-P | 8 | 20 l/min | Beta 14–38 |
| 29500-0001 | 4528-0001-P | 9 | 25 l/min | Beta 43–75 |
| 29620-1001 | 6303-0001-P | 6 | 45 l/min | Beta 90–150 |
| 29440-0501 | 920-0001-P | 8 | 18 l/min | Nanni N2/N3 |
| 29500-0501 | 4528-0001-P | 9 | 25 l/min | Nanni N4 |
| 29610-0501 | 6303-0001-P | 6 | 40 l/min | Nanni T4 |

#### Johnson Pump (SPX Flow)

Johnson ist der zweite große Hersteller und wird oft als OEM in
skandinavischen Motoren (Volvo Penta) verbaut.

**Häufige Johnson-Pumpen:**
| Johnson Modell | Impeller-Nr. | Flügel | Einbau bei |
|---------------|-------------|--------|-----------|
| F4B-8 | 09-808B-1 | 8 | Volvo D1 |
| F4B-9 | 09-810B-1 | 8 | Volvo D2 |
| F5B-9 | 09-812B-1 | 8 | Diverse |
| F35B-8 | 09-821BT-1 | 10 | Volvo D3/D4 |
| F7B-8 | 09-824P-1 | 10 | Volvo D6 |
| F8B-8 | 09-826B-9 | 10 | Große Motoren |

### 6.4 Impeller-Wechsel — Schritt-für-Schritt

**Benötigtes Werkzeug:**
- Schraubendreher oder Inbus für Pumpendeckel
- Impellerzieher (spezial) oder 2× Schraubendreher (flach)
- Neuer Impeller mit Dichtung/O-Ring
- Vaseline oder Glycerin (KEIN Silikonfett!)
- Taschenlampe
- Lappen

**Prozedur:**
1. **Seeventil schließen**
2. **Pumpendeckel abschrauben** (2–6 Schrauben, je nach Pumpe)
3. **Alten Impeller herausziehen**
   - Impellerzieher ist das richtige Werkzeug
   - Notfalls: 2 Schraubendreher vorsichtig unter die Flügel schieben
   - NICHT mit Zange greifen (beschädigt Welle und Gehäuse)
4. **Gehäuse inspizieren**
   - Innenwand auf Riefen und Verschleiß prüfen
   - Verschlissenes Gehäuse: kein Unterdruck → keine Ansaugung
   - Wear-Plate (Verschleißplatte) prüfen, wenn vorhanden
5. **Alle Flügel zählen!**
   - Fehlende Flügel sind im Kühlsystem → suchen und entfernen!
   - Flügel im Wärmetauscher blockieren Kühlwasserfluss
   - Typische Fundorte: Wärmetauscher-Eingang, Auspuffkrümmer
6. **Neuen Impeller einsetzen**
   - Flügel mit Vaseline einreiben (erleichtert Drehen)
   - In Drehrichtung biegen und einsetzen
   - Auf der Rückseite muss der Stift/die Keilnut korrekt sitzen
7. **Neue Dichtung/O-Ring einsetzen**
8. **Pumpendeckel montieren**
   - Schrauben gleichmäßig kreuzweise anziehen
   - Nicht zu fest (Deckel kann brechen bei Kunststoff)
9. **Seeventil öffnen**
10. **Motor starten und Wasseraustritt am Auspuff prüfen**
    - Innerhalb von 5–10 Sekunden muss Wasser sichtbar sein
    - Kein Wasser → sofort Motor stoppen!

### 6.5 Häufige Impeller-Probleme

| Problem | Symptom | Ursache | Lösung |
|---------|---------|---------|--------|
| Abgebrochene Flügel | Überhitzung, kein Wasserfluss | Trockenlauf, Alter | Impeller + Gehäuse prüfen, Fragmente suchen |
| Verhärteter Impeller | Reduzierter Wasserfluss | Alter, UV, Wärme | Wechseln (auch wenn optisch ok) |
| Impeller dreht auf Welle | Pumpe läuft, kein Wasserfluss | Keilnut/Stift verschlissen | Impeller + Welle/Stift prüfen |
| Kavitation | Geräusche, ungleichmäßiger Fluss | Zu hohe Saughöhe, verstopfter Seiher | Seiher reinigen, Saughöhe prüfen |
| Undichter Pumpendeckel | Wassertropfen an Pumpe | Defekte Dichtung, verzogener Deckel | Dichtung wechseln, Deckel prüfen |

### 6.6 Seewasserpumpe komplett überholen (1.000h)

Bei 1.000 Betriebsstunden sollte die gesamte Seewasserpumpe überholt werden:

**Überholungsumfang:**
- Neuer Impeller
- Neue Wellendichtung (Mechanical Seal)
- Neuer O-Ring / Deckeldichtung
- Wear-Plate ersetzen (wenn vorhanden)
- Welle auf Schlag prüfen
- Gehäuse auf Verschleiß prüfen

**Jabsco Service-Kits:**
| Pumpe | Service-Kit Nr. | Inhalt | Preis |
|-------|----------------|--------|-------|
| 29460/29470 | SK260-0001 | Impeller, Dichtung, O-Ring | 35–50 EUR |
| 29500 | SK506-0001 | Impeller, Seal, O-Ring, Wear-Plate | 55–80 EUR |
| 29610 | SK611-0001 | Impeller, Seal, O-Ring, Wear-Plate | 70–100 EUR |
| 29630 | SK631-0001 | Impeller, Seal, O-Ring, Wear-Plate | 90–130 EUR |

---
---

## 7. Keilriemen und Zahnriemen

### 7.1 Keilriemen (V-Belt) — Funktion und Typen

Der Keilriemen treibt üblicherweise die Lichtmaschine und — je nach Motor —
die Kühlwasserpumpe (Süßwasserseite) an. Bei einigen Motoren sitzt auch
die Seewasserpumpe am Keilriemen.

**Keilriemen-Typen:**
| Typ | Profil | Breite | Einsatz |
|-----|--------|--------|---------|
| Klassisch V (A/B/C) | Trapezförmig | 10–22 mm | Ältere Motoren |
| Schmalkeil (SPZ/SPA/SPB) | Schmaler Trapez | 8–17 mm | Standard Marine |
| Zahnkeil (XPZ/XPA) | Gezahnte Unterseite | 8–17 mm | Hohe Drehzahlen |
| Poly-V (Rippenriemen) | Multi-Rillen | Variabel | Moderne Motoren (D3, D4) |

### 7.2 Keilriemenspannung prüfen und einstellen

**Methode 1 — Daumendrucktest (Praxis):**
1. Riemen in der Mitte zwischen den Scheiben drücken
2. Eindrücken mit ~5 kg Kraft (Daumen)
3. Richtige Spannung: 10–15 mm Durchbiegung
4. Zu locker: >15 mm → Riemen rutscht, quietscht, Batterie lädt nicht
5. Zu fest: <10 mm → Lager der Lichtmaschine/Pumpe werden überlastet

**Methode 2 — Riemenspannungsmesser (professionell):**
- GATES Sonic Tension Meter 507C
- Korrekte Frequenz je nach Riemenlänge und Gewicht
- Genauer als Daumendrucktest

**Spannung einstellen:**
1. Befestigungsschrauben der Lichtmaschine lösen (nicht entfernen)
2. Lichtmaschine nach außen hebeln (mit Brecheisen oder Riemenspanner)
3. Schrauben festziehen
4. Spannung erneut prüfen
5. Nach 10 Betriebsstunden nachspannen (neuer Riemen dehnt sich)

### 7.3 Keilriemen-Teilenummern nach Motor

#### Yanmar Keilriemen

| Motor | Genuine Nr. | Profil | Länge | Aftermarket |
|-------|-----------|--------|-------|-----------|
| 1GM10 | 128170-77350 | A | 710 mm | A28 / 13×710 |
| 2YM15 | 128170-77370 | A | 750 mm | A30 / 13×750 |
| 3YM20/30 | 128670-77111 | SPZ | 887 mm | SPZ 887 |
| 3JH40 | 129612-42290 | SPZ | 950 mm | SPZ 950 |
| 3JH57 | 129612-42290 | SPZ | 950 mm | SPZ 950 |
| 4JH45/57 | 129612-42290 | SPZ | 1000 mm | SPZ 1000 |
| 4JH80 | 129612-42300 | SPZ | 1060 mm | SPZ 1060 |
| 4JH110 | 129612-42300 | SPZ | 1060 mm | SPZ 1060 |
| 4LHA-STP | 119593-42280 | SPA | 1332 mm | SPA 1332 |
| 6LY-STP | 119593-42290 | SPA | 1532 mm | SPA 1532 |

#### Volvo Penta Keilriemen

| Motor | Genuine Nr. | Profil | Aftermarket |
|-------|-----------|--------|-----------|
| D1-13/20 | 966934 | SPZ | SPZ 862 |
| D1-30 | 966934 | SPZ | SPZ 912 |
| D2-40/50 | 21951188 | Poly-V 5PK | 5PK 890 |
| D2-55/60/75 | 21951188 | Poly-V 5PK | 5PK 890 |
| D3-Serie | 21405494 | Poly-V 6PK | 6PK 1120 |
| D4-Serie | 21405494 | Poly-V 6PK | 6PK 1220 |
| D6-Serie | 21405495 | Poly-V 8PK | 8PK 1520 |

### 7.4 Zahnriemen (Timing Belt) — Volvo Penta D3

```
╔══════════════════════════════════════════════════════════════════╗
║  WIEDERHOLUNG — KRITISCH:                                        ║
║                                                                   ║
║  Der Volvo Penta D3 ist der einzige gängige Marine-Diesel mit    ║
║  Zahnriemen. Dieser treibt die Nockenwelle an.                   ║
║                                                                   ║
║  Zahnriemenriss = Motorschaden = 15.000–25.000 EUR               ║
║                                                                   ║
║  Wechselintervall: 1.000h ODER 5 Jahre (was zuerst eintritt)     ║
║                                                                   ║
║  Teilenummern:                                                    ║
║  - Zahnriemen:    3583895                                         ║
║  - Spannrolle:    3583897                                         ║
║  - Umlenkrolle:   3583896                                         ║
║  - Dichtung Kit:  3583898                                         ║
║  - Wasserpumpe:   3583891 (bei Zugang gleich mit wechseln!)       ║
║                                                                   ║
║  IMMER Riemen + beide Rollen + Dichtungen zusammen wechseln!     ║
║  Wasserpumpe bei Zugang empfohlen (sitzt hinter dem Zahnriemen)  ║
║                                                                   ║
║  Arbeitszeit: 4–6 Stunden (sehr motorraum-abhängig)              ║
║  Material: ~450–600 EUR (mit Wasserpumpe)                        ║
║  Arbeit: ~600–1.200 EUR                                          ║
║  Gesamt: ~1.100–1.800 EUR                                        ║
╚══════════════════════════════════════════════════════════════════╝
```

**Zahnriemenwechsel D3 — Kurzanleitung:**

1. Obere Abdeckung abnehmen
2. Zahnriemenabdeckung abnehmen
3. Motor auf OT Zylinder 1 drehen (Markierungen beachten!)
4. Nockenwellenrad mit Fixierstift arretieren (Spezialwerkzeug 9995452)
5. Kurbelwelle mit Fixierstift arretieren (Spezialwerkzeug 9995451)
6. Spannrolle lösen
7. Zahnriemen abnehmen
8. Umlenkrolle wechseln
9. Spannrolle wechseln
10. Ggf. Wasserpumpe wechseln (jetzt zugänglich)
11. Neuen Zahnriemen auflegen (Richtung und Markierungen beachten!)
12. Spannrolle nach Vorgabe spannen
13. Kurbelwelle 2× komplett drehen (von Hand!)
14. OT-Markierungen erneut prüfen
15. Abdeckungen montieren
16. Testlauf

**WARNUNG:** Zahnriemenwechsel am D3 erfordert Spezialwerkzeug (Fixierstifte).
Ohne korrekte Arretierung besteht die Gefahr einer falschen Steuerzeiten-
Einstellung → Motorschaden beim ersten Start.

### 7.5 Keilriemen-Verschleiß erkennen

| Verschleißbild | Ursache | Maßnahme |
|---------------|---------|----------|
| Risse quer zum Riemen | Alterung, UV, Wärme | Sofort wechseln |
| Risse längs | Zu lockere Spannung, Flucht falsch | Wechseln + Ursache beheben |
| Glasige Oberfläche | Durchrutschen | Spannung prüfen, wechseln |
| Ausgefranste Kanten | Fluchtungsfehler der Scheiben | Flucht prüfen, wechseln |
| Quietschen bei Start | Zu locker, nass, verschlissen | Spannung prüfen oder wechseln |
| Schwarzer Abrieb | Durchrutschen | Spannung prüfen, wechseln |

---
---

## 8. Kühlmittel — Mischung, Wechsel und Spülung

### 8.1 Kühlmittelsysteme im Marine-Diesel

Moderne Marine-Diesel verwenden ein Zweikreis-Kühlsystem:

```
Kreislauf 1 (geschlossen — Süßwasser/Kühlmittel):
  Motor → Thermostat → Wärmetauscher → Motor
  Temperatur: 75–90 °C (thermostatgeregelt)
  Medium: Wasser + Frostschutz/Korrosionsschutz

Kreislauf 2 (offen — Seewasser):
  Seeventil → Impellerpumpe → Wärmetauscher → Auspuff-Mischer → Über Bord
  Temperatur: Seewasser-Temperatur + 5–15 °C
  Medium: Seewasser
```

### 8.2 Kühlmitteltypen

| Typ | Basis | Farbe | Lebensdauer | Kompatibilität |
|-----|-------|-------|-------------|---------------|
| IAT (konventionell) | Anorganische Additive (Silikat, Phosphat) | Grün/Blau | 2 Jahre | Universal |
| OAT (Organic Acid Technology) | Organische Säuren | Orange/Rot | 5 Jahre | NICHT mit IAT mischbar! |
| HOAT (Hybrid) | Mix aus IAT + OAT | Gelb/Orange | 3–5 Jahre | Bedingt kompatibel |
| Si-OAT (Silicated OAT) | OAT + Silikat | Violett | 5 Jahre | Volvo Penta bevorzugt |

**Herstellervorgaben:**
| Hersteller | Empfohlener Typ | Spezifikation | Genuine Produkt |
|------------|----------------|--------------|----------------|
| Yanmar | IAT oder HOAT | ASTM D3306 | Yanmar Premium Antifreeze |
| Volvo Penta | Si-OAT | Volvo VCS (Volvo Coolant System) | Volvo Penta Coolant (22567233) |
| Beta Marine | IAT oder HOAT | BS 6580 | Keine eigene Marke |
| Nanni | OAT oder HOAT | ASTM D3306 | Nanni Coolant |

### 8.3 Mischungsverhältnis

**Standard-Mischung:** 50 % Kühlmittel-Konzentrat + 50 % demineralisiertes Wasser

| Mischung | Frostschutz bis | Siedeschutz bis | Korrosionsschutz |
|----------|----------------|-----------------|-----------------|
| 30 % Konzentrat + 70 % Wasser | −15 °C | +107 °C | Eingeschränkt |
| 40 % Konzentrat + 60 % Wasser | −25 °C | +110 °C | Gut |
| 50 % Konzentrat + 50 % Wasser | −37 °C | +115 °C | Optimal |
| 60 % Konzentrat + 40 % Wasser | −52 °C | +120 °C | Gut (zu viskos) |

**NIEMALS:**
- Leitungswasser verwenden (Kalk verstopft Kanäle)
- Mehr als 60 % Konzentrat (verschlechtert Wärmeübertragung)
- Verschiedene Typen mischen (IAT + OAT = Gelierung!)
- Reines Wasser fahren (Korrosion, kein Siedeschutz)

### 8.4 Kühlmittelkapazitäten nach Motor

| Motor | Kühlmittel-Kapazität (Kreislauf 1) |
|-------|-----------------------------------|
| Yanmar 1GM10 | 1,5 Liter |
| Yanmar 2YM15 | 2,5 Liter |
| Yanmar 3YM20/30 | 3,5 Liter |
| Yanmar 3JH40/57 | 5,0 Liter |
| Yanmar 4JH45/57 | 6,5 Liter |
| Yanmar 4JH80/110 | 7,5 Liter |
| Volvo D1-13/20 | 3,0 Liter |
| Volvo D1-30 | 3,8 Liter |
| Volvo D2-40/50 | 6,0 Liter |
| Volvo D2-55/60/75 | 7,5 Liter |
| Volvo D3-110–220 | 12,0 Liter |
| Volvo D4-180–300 | 16,0 Liter |
| Volvo D6-280–440 | 22,0 Liter |
| Beta 14–30 | 3,5 Liter |
| Beta 35–50 | 5,0 Liter |
| Beta 60–75 | 7,0 Liter |
| Beta 90–150 | 10,0 Liter |
| Nanni N2 | 2,0 Liter |
| Nanni N3 | 3,5 Liter |
| Nanni N4 | 5,5 Liter |
| Nanni T4 | 9,0 Liter |

### 8.5 Kühlmittelwechsel-Prozedur

**Wechselintervall:** 500–1.000 Betriebsstunden oder alle 2–3 Jahre

**Benötigtes Material:**
- Kühlmittel-Konzentrat (richtige Spezifikation)
- Demineralisiertes Wasser
- Auffangbehälter (10–25 Liter)
- Kühlsystemreiniger (z.B. Prestone Flush, Yanmar Cooling System Cleaner)
- Refraktometer oder Teststreifen zur Kontrolle
- Trichter, Schlauch

**Prozedur:**

1. **Motor kalt** (Verbrennungsgefahr bei heißem Kühlmittel!)
2. **Druckdeckel am Ausgleichsbehälter öffnen**
3. **Ablassschraube(n) öffnen** (Position: Motorblock unten, ggf. Wärmetauscher)
4. **Altes Kühlmittel auffangen** (umweltgerechte Entsorgung!)
5. **Spülung vorbereiten:**
   - Ablassschrauben schließen
   - Mit demineralisiertem Wasser + Reiniger auffüllen
   - Motor 15–20 Minuten laufen lassen (Thermostat muss öffnen)
   - Motor abstellen, abkühlen lassen
6. **Spülwasser ablassen**
7. **Bei starker Verschmutzung:** Schritt 5–6 mit reinem Wasser wiederholen
8. **Neues Kühlmittel einfüllen:**
   - Mischung vorbereiten (50:50)
   - Langsam einfüllen (Luftblasen entweichen lassen)
   - Ausgleichsbehälter bis Markierung füllen
9. **Entlüften:**
   - Motor starten, Heizung auf MAX (wenn vorhanden)
   - Motor auf Betriebstemperatur bringen
   - Entlüftungsschraube(n) öffnen, bis blasenfrei Kühlmittel austritt
   - Nachfüllen am Ausgleichsbehälter
10. **Kontrolle:**
    - Kühlmittelstand nach 1 Stunde Betrieb prüfen
    - Frostschutzkonzentration mit Refraktometer prüfen
    - Auf Undichtigkeiten prüfen

### 8.6 Kühlmittelprobleme erkennen

| Symptom | Mögliche Ursache | Maßnahme |
|---------|-----------------|----------|
| Braune Brühe im Ausgleichsbehälter | Rost, verbrauchte Additive | Spülen + neu befüllen |
| Ölfilm auf Kühlmittel | Zylinderkopfdichtung defekt | SOFORT Motor stoppen, Werkstatt |
| Weißer Schaum | Abgase im Kühlmittel (Kopfdichtung) | SOFORT Motor stoppen, Werkstatt |
| Kühlmittelstand sinkt ständig | Leck (extern oder intern) | Drucktest, Leck suchen |
| Gelartiger Brei | Falsche Typen gemischt (IAT+OAT) | Komplett spülen, richtig befüllen |
| Grünliche Kristalle an Schlauchklemmen | Elektrolyse/Korrosion | System spülen, Erdung prüfen |

---
---

## 9. Ventilspiel-Einstellung

### 9.1 Warum Ventilspiel einstellen?

Das Ventilspiel (Valve Clearance) ist der Abstand zwischen Kipphebel und
Ventilschaft bei geschlossenem Ventil. Dieser Abstand ist notwendig, um
die Wärmeausdehnung der Ventile im Betrieb zu kompensieren.

**Zu großes Ventilspiel:**
- Lautes Klappern/Ticken im Ventiltrieb
- Reduzierte Ventilöffnung → Leistungsverlust
- Erhöhter Verschleiß an Kipphebel und Ventilschaft

**Zu kleines Ventilspiel:**
- Ventil schließt nicht vollständig → Kompressionsverlust
- Verbrannter Ventilsitz → teurer Schaden
- Motor springt schlecht an, unrunder Lauf
- Im Extremfall: durchgebranntes Ventil (Zylinderkopf-Reparatur nötig)

### 9.2 Prüfintervall

- **Erstservice:** 50 Betriebsstunden
- **Danach:** alle 250–500 Betriebsstunden (je nach Hersteller)
- **Ausnahme:** Hydraulische Ventilspielausgleicher (Volvo D3) — kein Einstellen

### 9.3 Ventilspiel-Einstellung — Prozedur

**Benötigtes Werkzeug:**
- Ventildeckel-Schlüssel
- Fühllehrenset (0,05–0,50 mm)
- Ring-/Maulschlüssel für Kontermutter (10 mm oder 12 mm, motorabhängig)
- Schraubendreher (flach) für Einstellschraube
- Kurbel oder Werkzeug zum Motordrehen
- Drehmomentschlüssel (Ventildeckel)
- Neue Ventildeckeldichtung (empfohlen)

**Vorbereitung:**
1. Motor KALT (mindestens 4 Stunden Stillstand, besser über Nacht)
2. Ventildeckel abschrauben (Schrauben aufheben)
3. Kipphebel und Ventile sichtbar

**Methode — Einzelzylinder:**
1. Zylinder 1 auf OT (Verdichtungstakt) drehen:
   - Beide Ventile (Ein+Aus) müssen geschlossen sein
   - Kipphebel dürfen Spiel haben (wackeln)
2. Fühllehre zwischen Kipphebel und Ventilschaft einführen
3. Soll-Wert: siehe Tabelle (Kapitel 2.2–2.5)
4. Fühllehre soll mit leichtem Widerstand durchziehbar sein
   - „Schleifend leichtgängig" = korrekt
   - Zu locker = Spiel zu groß
   - Klemmt = Spiel zu klein
5. Zum Einstellen:
   a. Kontermutter lösen (Ring-/Maulschlüssel halten)
   b. Einstellschraube drehen (Schraubendreher)
   c. Fühllehre erneut prüfen
   d. Kontermutter festziehen (dabei Einstellschraube festhalten!)
   e. Nochmals prüfen (Kontermutter kann Einstellung verziehen)
6. Nächsten Zylinder auf OT drehen und wiederholen

**Zündfolge und Zylinderreihenfolge:**
| Motor | Zylinder | Zündfolge |
|-------|----------|-----------|
| 1-Zylinder | 1 | 1 |
| 2-Zylinder (Yanmar 2YM) | 1-2 | 1-2 |
| 3-Zylinder (Yanmar 3YM, 3JH) | 1-2-3 | 1-2-3 |
| 3-Zylinder (Volvo D1) | 1-2-3 | 1-2-3 |
| 4-Zylinder (Yanmar 4JH) | 1-2-3-4 | 1-3-4-2 |
| 4-Zylinder (Volvo D2) | 1-2-3-4 | 1-3-4-2 |
| 5-Zylinder (Volvo D3) | 1-2-3-4-5 | Hydraulisch — kein Einstellen |
| 6-Zylinder (Yanmar 6LY) | 1-2-3-4-5-6 | 1-5-3-6-2-4 |
| 6-Zylinder (Volvo D6) | 1-2-3-4-5-6 | 1-5-3-6-2-4 |

### 9.4 Ventilspiel-Tabelle (Zusammenfassung aller Hersteller)

| Motor | Einlass (mm) | Auslass (mm) | Kalt/Warm |
|-------|-------------|-------------|-----------|
| Yanmar 1GM10 | 0,20 | 0,20 | Kalt |
| Yanmar 2YM15 | 0,20 | 0,20 | Kalt |
| Yanmar 3YM20/30 | 0,20 | 0,20 | Kalt |
| Yanmar 3JH40/57 | 0,20 | 0,20 | Kalt |
| Yanmar 4JH45–110 | 0,20 | 0,20 | Kalt |
| Yanmar 4LHA | 0,20 | 0,25 | Kalt |
| Yanmar 6LY | 0,20 | 0,25 | Kalt |
| Volvo D1-13/20/30 | 0,20 | 0,20 | Kalt |
| Volvo D2-40/50 | 0,20 | 0,35 | Kalt |
| Volvo D2-55/60/75 | 0,20 | 0,20 | Kalt |
| Volvo D3 | Hydraulisch | Hydraulisch | — |
| Volvo D4 | 0,30 | 0,55 | Kalt |
| Volvo D6 | 0,30 | 0,55 | Kalt |
| Beta 14–30 | 0,15 | 0,15 | Kalt |
| Beta 35–50 | 0,18 | 0,18 | Kalt |
| Beta 60–105 | 0,20 | 0,20 | Kalt |
| Beta 115–150 | 0,20 | 0,25 | Kalt |
| Nanni N2 | 0,15 | 0,15 | Kalt |
| Nanni N3 | 0,18 | 0,18 | Kalt |
| Nanni N4 | 0,20 | 0,20 | Kalt |
| Nanni T4 | 0,20 | 0,25 | Kalt |

---
---

## 10. Zinkanoden am Motor

### 10.1 Galvanische Korrosion im Marine-Motor

Marine-Diesel mit Seewasserkühlung enthalten verschiedene Metalle
(Gusseisen, Messing, Kupfer, Edelstahl), die in Kontakt mit Salzwasser
eine galvanische Zelle bilden. Ohne Opferanoden würden die unedleren
Metalle (insbesondere Gusseisen im Motorblock) korrodieren.

**Korrosionsreihe (maritim relevant):**
```
Unedel (korrodiert zuerst)        Edel (wird geschützt)
──────────────────────────────────────────────────────►
Zink → Aluminium → Stahl → Gusseisen → Messing → Kupfer → Edelstahl 316
 ▲
 │
 Opferanode (wird aufgeopfert, um Motor zu schützen)
```

### 10.2 Anodentypen am Motor

#### Bleistift-Anoden (Pencil Anodes)

Zylindrische Zinkanoden, die in den Motorblock oder Wärmetauscher
eingeschraubt werden.

**Typische Positionen:**
- Motorblock (Kühlwasserkanal, Seewasserseite)
- Wärmetauscher (Enddeckel, 1–2 Stück)
- Ölkühler (wenn seewassergekühlt)
- Ladeluftkühler (wenn seewassergekühlt)

**Bleistift-Anoden-Maße nach Motor:**

| Motor | Position | Gewinde | Länge | Durchmesser | Genuine Nr. |
|-------|----------|---------|-------|-------------|-----------|
| Yanmar 1GM/2YM/3YM | Block | M8×1,25 | 25 mm | 8 mm | 27210-200300 |
| Yanmar 3JH/4JH | Block | M10×1,25 | 35 mm | 10 mm | 27210-200400 |
| Yanmar 3JH/4JH | Wärmetauscher | 1/4" NPT | 40 mm | 12 mm | 27210-200500 |
| Yanmar 4LHA/6LY | Block | M12×1,5 | 45 mm | 14 mm | 27210-200600 |
| Yanmar 4LHA/6LY | Wärmetauscher | 3/8" NPT | 50 mm | 16 mm | 27210-200700 |
| Volvo D1/D2 | Block | M10×1,25 | 30 mm | 10 mm | 838929 |
| Volvo D1/D2 | Wärmetauscher | 1/4" NPT | 40 mm | 12 mm | 3858399 |
| Volvo D3/D4 | Block | M12×1,5 | 40 mm | 14 mm | 22996441 |
| Volvo D3/D4 | Wärmetauscher | 3/8" NPT | 50 mm | 16 mm | 3588506 |
| Volvo D6 | Block | M14×1,5 | 50 mm | 16 mm | 22996442 |
| Volvo D6 | Wärmetauscher | 1/2" NPT | 60 mm | 20 mm | 3588507 |
| Beta (alle) | Block | M8 oder M10 | 25–40 mm | 8–12 mm | 211-62501 |
| Beta (alle) | Wärmetauscher | 1/4" NPT | 40 mm | 12 mm | 211-62502 |
| Nanni (alle) | Block | M10×1,25 | 30 mm | 10 mm | 970310801 |
| Nanni (alle) | Wärmetauscher | 1/4" NPT | 40 mm | 12 mm | 970310802 |

### 10.3 Prüfung und Wechsel

**Prüfintervall:** alle 100–250 Betriebsstunden oder halbjährlich

**Wechselkriterium:** Anode wechseln, wenn >50 % des Zink-Materials
abgetragen ist. Eine „gute" Anode zeigt gleichmäßige Korrosion über
die gesamte Oberfläche.

**Warnsignale:**
| Befund | Bedeutung | Maßnahme |
|--------|----------|----------|
| Anode fast unverändert | Kein elektrischer Kontakt (isoliert) | Sitz prüfen, Gewinde reinigen |
| Anode komplett aufgelöst | Intervall zu lang, starke Korrosion | Häufiger prüfen, Ursache klären |
| Anode einseitig korrodiert | Streuströme | Erdung und Galvanik prüfen |
| Anode mit weißem Belag | Elektrolyse (zu viel Strom) | Landstrom-Isolierung prüfen |
| Keine Anode mehr vorhanden | Vergessen oder herausgefallen | SOFORT ersetzen |

**Wechsel-Prozedur (Bleistift-Anode):**
1. Seeventil schließen (wenn Wärmetauscher-Anode)
2. Alte Anode herausschrauben (Maulschlüssel auf dem Sechskant)
3. Gewinde reinigen (kein Teflon-Band verwenden!)
4. Neue Anode einschrauben (handfest + ¼ Umdrehung)
5. Seeventil öffnen
6. Auf Undichtigkeit prüfen

### 10.4 Zink vs. Aluminium vs. Magnesium

| Material | Einsatzgebiet | Potential (V) | Lebensdauer |
|----------|--------------|--------------|-------------|
| Zink | Salzwasser | −1,05 V | Standard |
| Aluminium | Brackwasser / beides | −1,10 V | Längere Standzeit |
| Magnesium | Süßwasser | −1,60 V | Nur Süßwasser! |

**WARNUNG:** Magnesium-Anoden in Salzwasser lösen sich extrem schnell auf
und bieten keinen nachhaltigen Schutz. Zink ist der Standard für
Salzwasseranwendungen.

---
---

## 11. Winterlager-Prozedur

### 11.1 Warum korrektes Winterlager entscheidend ist

Die Winterlager-Prozedur (Winterization) ist die wichtigste einzelne
Wartungsmaßnahme des Jahres. Mehr Motorschäden entstehen durch
falsches oder unterlassenes Winterlager als durch alle anderen
Ursachen zusammen.

**Risiken bei falschem/fehlendem Winterlager:**
- **Frostschaden**: Wasser im Motor gefriert → Motorblock reißt (Totalschaden)
- **Korrosion**: Kondenswasser + Salzreste → Innenkorrosion
- **Verharzung**: Kraftstoff verharzt in Injektoren und Pumpe
- **Batterietod**: Tiefentladung über Winter → Batterie defekt
- **Schimmel**: Feuchtigkeit → Schimmelbefall im Motorraum
- **Mäuse/Marder**: Nisten in Ansaug-/Auspuffschläuchen

### 11.2 Vollständige Winterlager-Checkliste

#### Phase 1 — Motoröl und Filter (30 Minuten)

```
□ Motor warmfahren (20 Minuten unter Last)
□ Motor abstellen
□ Motoröl ablassen/absaugen (WARM!)
□ Ölfilter wechseln
□ Frisches Öl einfüllen (Soll-Menge)
□ Ölstand prüfen (Peilstab)
□ Motor 1 Minute laufen lassen (Öl verteilen)
□ Ölstand erneut prüfen
```

**Warum VOR dem Winter Öl wechseln?**
Verbrauchtes Öl enthält Säuren, Wasser und Verbrennungsrückstände.
Über den Winter greifen diese den Motor von innen an. Frisches Öl
enthält Additive, die den Motor schützen.

#### Phase 2 — Kraftstoffsystem (20 Minuten)

```
□ Tank VOLL tanken (minimiert Kondensation im Tank)
□ Kraftstoff-Stabilisator zugeben (z.B. Sta-Bil Diesel: 30 ml/10 l)
□ Motor 10 Minuten laufen lassen (Additiv verteilen)
□ Kraftstoff-Vorfilter (Racor): Wasser ablassen
□ Optional: Vorfilter und Feinfilter wechseln
  (wenn sowieso fällig — sonst im Frühjahr)
```

#### Phase 3 — Kühlsystem Seewasser (30 Minuten)

```
□ Seeventil schließen
□ Seewasser-Einlassschlauch vom Seeventil lösen
□ Schlauchende in Eimer mit Frostschutz stecken
  (Propylenglykolbasiert, ungiftig — z.B. Starbrite −60°C)
□ Motor starten und laufen lassen bis Frostschutzlösung
  aus dem Auspuff austritt (rosa/blaue Farbe sichtbar)
□ Motor abstellen
□ Schlauch wieder anschließen (NICHT am Seeventil)
□ Seeventil geschlossen lassen
```

**WICHTIG:** Nur UNGIFTIGEN Propylenglyko-Frostschutz für die
Seewasserseite verwenden (geht über Bord beim Frühjahrsstart).
KEIN Ethylenglykol (giftig, umweltschädlich)!

#### Phase 4 — Kühlsystem Süßwasser (15 Minuten)

```
□ Kühlmittelstand prüfen
□ Frostschutzkonzentration messen (Refraktometer)
□ Mindestens −25 °C Frostschutz sicherstellen
□ Bei Bedarf: Konzentrat nachfüllen
□ Kühlsystem auf Undichtigkeiten prüfen
```

#### Phase 5 — Zylinder konservieren / Fogging (10 Minuten)

```
□ Luftfilter abnehmen
□ Motor starten und auf mittlere Drehzahl bringen
□ Fogging-Oil (z.B. CRC Marine Fogging Oil, Mercury Stor-N-Start)
  in die Ansaugöffnung sprühen (kurze Stöße, 3–5 Sekunden)
□ Motor wird rußen und stottern — normal
□ Motor mit Fogging Oil abstellen (Spray weiter halten)
□ Luftfilter wieder montieren
```

**Alternativ bei kleinen Motoren (1GM/2YM):**
- Dekompressionsventil öffnen (wenn vorhanden)
- Einige Tropfen Motoröl in jeden Zylinder durch Glühkerzen-/Injektoröffnung
- Motor von Hand 2–3 Umdrehungen drehen
- Glühkerzen/Injektoren wieder montieren

#### Phase 6 — Auspuffsystem (10 Minuten)

```
□ Wassersammelschalldämpfer (Waterlock) entleeren
□ Frostschutzmittel ist durch den Auspuff gelaufen (Phase 3)
□ Bei Bedarf: Auspuffschlauch am tiefsten Punkt lösen und Wasser ablassen
□ Auspuffauslass-Klappe schließen oder Stopfen einsetzen
  (verhindert Rückfluss bei Sturm und Nagetierbefall)
```

#### Phase 7 — Batterie (15 Minuten)

```
□ Batterie-Pole reinigen (Drahtbürste)
□ Batterie-Pole mit Polfett einstreichen
□ Batterie laden (Ladegerät anschließen)
□ Batterie-Spannung messen:
  - 12,7 V = 100 % geladen
  - 12,4 V = 75 % geladen
  - 12,0 V = 25 % geladen → sofort laden!
  - <11,8 V = tiefentladen → möglicherweise defekt
□ Erhaltungsladegerät anschließen (wenn Landstrom verfügbar)
□ ODER: Batterie abklemmen (beide Pole) und monatlich nachladen
□ Elektrolytstand prüfen (nur bei offenen Blei-Säure-Batterien)
```

#### Phase 8 — Getriebe und Saildrive (10 Minuten)

```
□ Getriebeöl prüfen (Peilstab):
  - Milchig = Wassereinbruch → Dichtung defekt → Werkstatt!
  - Dunkel mit Metallpartikeln = Verschleiß → Werkstatt
  - Klar/bernsteinfarben = OK
□ Getriebeöl wechseln (wenn fällig, alle 250–500h)
□ Bei Saildrive: Faltenbalg auf Risse prüfen (kritisch!)
□ Saildrive-Öl wechseln (ATF oder SAE 80W-90, laut Hersteller)
□ Saildrive-Anode prüfen
```

#### Phase 9 — Äußere Konservierung (15 Minuten)

```
□ Motor äußerlich reinigen (Kaltreiniger, Bürste)
□ Blanke Metallflächen mit Korrosionsschutzöl behandeln
  (z.B. CRC Marine 6-66, Bällistol, WD-40 Specialist Marine)
□ Gaszug/Schaltzug schmieren
□ Keilriemen entlasten (wenn möglich — bei langem Stand)
□ Motorraum trocknen lassen (Entfeuchterbeutel einlegen)
□ Motorraum-Abdeckung leicht offen lassen (Luftzirkulation)
```

### 11.3 Winterlager-Materialien — Einkaufsliste

| Material | Menge | Produkt (Beispiel) | Preis (ca.) |
|----------|-------|-------------------|-------------|
| Motoröl | Motor-spezifisch | Shell Rimula R4 L 15W-40 | 20–50 EUR |
| Ölfilter | 1 Stück | Motor-spezifisch | 10–25 EUR |
| Frostschutz (Seewasserseite) | 10–20 Liter | Starbrite Non-Toxic −60 °C | 25–40 EUR |
| Kraftstoff-Stabilisator | 1 Flasche | Sta-Bil Diesel (236 ml) | 12–18 EUR |
| Fogging Oil | 1 Dose | CRC Marine Fogging Oil (340g) | 12–16 EUR |
| Korrosionsschutzöl | 1 Dose | CRC Marine 6-66 (400 ml) | 8–12 EUR |
| Polfett | 1 Tube | Liqui Moly Batterie-Polfett | 4–8 EUR |
| Entfeuchterbeutel | 2–4 Stück | Pingi Luftentfeuchter | 8–15 EUR |
| **Gesamt** | | | **100–185 EUR** |

### 11.4 Winterlager-Zeitplan

| Zeitpunkt | Aufgabe |
|-----------|---------|
| Oktober/November | Vollständige Winterlager-Prozedur |
| Dezember | Batterieladung prüfen, Motorraum-Feuchtigkeit prüfen |
| Januar | Batterieladung prüfen |
| Februar | Batterieladung prüfen, Motorraum-Feuchtigkeit prüfen |
| März | Inbetriebnahme vorbereiten (Material bestellen) |
| April | Inbetriebnahme (siehe Kapitel 12) |

---
---

## 12. Inbetriebnahme im Frühjahr

### 12.1 Frühjahrs-Checkliste

Die Inbetriebnahme im Frühjahr (De-Winterization, Commissioning) ist
das Gegenstück zur Winterlager-Prozedur und ebenso wichtig.

#### Phase 1 — Sichtprüfung (15 Minuten)

```
□ Motorraum auf Feuchtigkeit, Schimmel, Nagerspuren prüfen
□ Alle Schläuche auf Risse, Quellungen, Scheuerstellen prüfen
□ Alle Schlauchklemmen auf festen Sitz prüfen
□ Keilriemen auf Risse und Spannung prüfen
□ Abgasschlauch auf Durchhängen und Wasseransammlung prüfen
□ Motorlager auf Risse im Gummi prüfen
□ Auspuffauslass-Stopfen entfernen!
```

#### Phase 2 — Flüssigkeiten (15 Minuten)

```
□ Motorölstand prüfen (muss auf MAX stehen)
□ Kühlmittelstand prüfen
□ Getriebeölstand prüfen
□ Kraftstoff-Vorfilter: auf Wasser prüfen, ggf. ablassen
□ Kraftstoff-Qualität prüfen (Geruch, Farbe, Trübung)
```

#### Phase 3 — Seewassersystem (10 Minuten)

```
□ Seeventil öffnen (WICHTIG — häufigster Vergessens-Fehler!)
□ Seewasserfilter/Seiher reinigen
□ Impeller prüfen (Deckel öffnen, Flügel prüfen)
□ Impeller wechseln wenn nötig (oder wenn >1 Jahr alt)
□ Pumpendeckel wieder montieren
```

#### Phase 4 — Elektrik (10 Minuten)

```
□ Batterie anschließen (wenn abgeklemmt)
□ Batteriespannung messen (muss >12,6 V sein)
□ Ggf. Batterie nachladen
□ Zündschlüssel: Warnleuchten prüfen
□ Glühkerzen-Vorglühung testen (Kontrolleuchte muss leuchten)
```

#### Phase 5 — Erster Start (10 Minuten)

```
□ Motoröldruck vorab aufbauen:
  - Anlasser kurz betätigen (1–2 Sekunden), NICHT starten
  - Warten bis Öldruckwarnleuchte erlischt
  - Wiederholen bis Öldruck da ist
□ Motor starten
□ Sofort prüfen:
  - Öldruckwarnleuchte AUS?
  - Ladelampe AUS? (nach Drehzahlerhöhung)
  - Kühlwasseraustritt am Auspuff? (MUSS innerhalb 15 Sek.)
  - Ungewöhnliche Geräusche?
  - Undichtigkeiten?
□ Motor 5 Minuten im Leerlauf laufen lassen
□ Drehzahl langsam auf 1.500 U/min erhöhen
□ Betriebstemperatur erreichen lassen
□ Motor abstellen
□ Nochmals alle Flüssigkeitsstände prüfen
```

### 12.2 Häufige Probleme beim Frühjahrsstart

| Problem | Mögliche Ursache | Lösung |
|---------|-----------------|--------|
| Motor springt nicht an | Batterie leer, Kraftstoff verharzt | Laden, Kraftstoff-System entlüften |
| Motor springt an, stirbt sofort ab | Luft im Kraftstoff | Entlüften (siehe 5.5) |
| Kein Kühlwasser aus Auspuff | Seeventil zu, Impeller defekt | Seeventil öffnen (!), Impeller prüfen |
| Öldruckwarnleuchte bleibt an | Öl zu dick (kalt), Öldruckschalter | 30 Sek. warten, prüfen |
| Weißer Rauch | Feuchtigkeit im Zylinder (Fogging Oil) | Normal, verschwindet nach 5 Min. |
| Schwarzer Rauch | Verstopfter Luftfilter, Injektoren | Luftfilter prüfen, Injektoren reinigen |
| Starkes Vibrieren | Motorlager gesetzt, Propeller | Lager und Ausrichtung prüfen |
| Quietschendes Geräusch | Keilriemen locker/nass | Spannung prüfen |

### 12.3 Einfahrprozedur nach langer Standzeit

Nach der Winterpause sollte der Motor die erste Stunde schonend
behandelt werden:

1. **0–15 Minuten**: Leerlauf, Betriebstemperatur erreichen
2. **15–30 Minuten**: Leichte Last (30–40 % Drehzahl)
3. **30–45 Minuten**: Mittlere Last (50–60 % Drehzahl)
4. **45–60 Minuten**: Normale Last (70–80 % Drehzahl)
5. **Ab 60 Minuten**: Volle Last möglich

**Während der Einfahrphase besonders beobachten:**
- Kühlwassertemperatur (stabil 75–90 °C)
- Öldruck (stabil, keine Schwankungen)
- Wasseraustritt am Auspuff (gleichmäßig)
- Ungewöhnliche Geräusche oder Vibrationen
- Undichtigkeiten (Öl, Kühlmittel, Kraftstoff, Wasser)

---
---

## 13. Betriebsstunden-Tracker und Wartungsbuch

### 13.1 Betriebsstundenzähler

**Einbau-Typen:**
| Typ | Genauigkeit | Preis | Einbau |
|-----|-----------|-------|--------|
| Mechanisch (Hobbs) | ±1 % | 25–50 EUR | Am Motor, riemengetrieben |
| Elektronisch (Vibrationssensor) | ±5 % | 40–80 EUR | Am Motor geklebt, batteriebetrieben |
| Elektronisch (Zündungssignal) | ±1 % | 30–60 EUR | Am Zündschloss/Anlasser |
| Digital mit Drehzahlanzeige | ±1 % | 60–150 EUR | Am Motorblock (induktiv) |
| Motorsteuergerät (CAN-Bus) | ±0,1 % | Im Motor integriert | Keine Nachrüstung nötig |

**Empfehlung:** Jeder Motor ohne eingebauten Betriebsstundenzähler
sollte nachrüstet werden. Ohne Zähler ist keine verlässliche Wartungsplanung
möglich.

### 13.2 Wartungsbuch-Vorlage

Ein professionelles Wartungsbuch enthält folgende Einträge pro Wartung:

```
┌─────────────────────────────────────────────────────────────────┐
│                    WARTUNGSPROTOKOLL                              │
├─────────────────────────────────────────────────────────────────┤
│ Datum:           ___.___.______                                  │
│ Betriebsstunden: ___________ h                                   │
│ Wartungstyp:     □ 50h  □ 100h  □ 250h  □ 500h  □ 1000h       │
│                  □ Sonstig: ________________                     │
│                                                                   │
│ Durchgeführte Arbeiten:                                           │
│ □ Motoröl gewechselt     Sorte: _______ Menge: _____ Liter     │
│ □ Ölfilter gewechselt    Teilenr.: _______________              │
│ □ Kraftstoff-Vorfilter   Teilenr.: _______________              │
│ □ Kraftstoff-Feinfilter  Teilenr.: _______________              │
│ □ Impeller gewechselt    Teilenr.: _______________              │
│ □ Keilriemen gewechselt  Teilenr.: _______________              │
│ □ Kühlmittel gewechselt  Sorte: _______ Menge: _____ Liter     │
│ □ Ventilspiel geprüft    E: ___ mm  A: ___ mm                  │
│ □ Zinkanoden geprüft     Zustand: _______________               │
│ □ Zinkanoden gewechselt  Anzahl: ___                            │
│ □ Getriebeöl gewechselt  Sorte: _______ Menge: _____ Liter     │
│ □ Kompression gemessen   Zyl1: ___ Zyl2: ___ Zyl3: ___ Zyl4: ___│
│ □ Sonstiges: _______________________________________________     │
│                                                                   │
│ Bemerkungen:                                                      │
│ ________________________________________________________________ │
│ ________________________________________________________________ │
│                                                                   │
│ Durchgeführt von: ________________  Unterschrift: _____________ │
│ Werft/Firma: ___________________                                │
└─────────────────────────────────────────────────────────────────┘
```

### 13.3 Digitale Wartungsdokumentation

Moderne Wartungsdokumentation erfolgt zunehmend digital:

**Vorteile digitaler Dokumentation:**
- Automatische Erinnerungen an fällige Wartung
- Fotodokumentation (Zustand vor/nach)
- Kostenerfassung und Auswertung
- Export für Versicherung/Verkauf
- Teilenummern und Bezugsquellen hinterlegt

**Empfohlene Apps/Systeme:**
| System | Typ | Preis | Besonderheit |
|--------|-----|-------|-------------|
| AYDI (dieses System) | Web-App | Professionell | Vollständige Analyse + Wartung |
| Boatyard | App (iOS/Android) | 4,99 EUR/Monat | Einfache Wartungsverwaltung |
| Yacht Manager | App (iOS/Android) | Kostenlos/Premium | Grundlegende Protokolle |
| Excel/Spreadsheet | Desktop | Kostenlos | Flexibel, aber kein Auto-Reminder |
| Papier-Wartungsbuch | Physisch | 15–25 EUR | Bewährt, wetterbeständig |

### 13.4 Wartungskosten-Tracker (Lebenszykluskosten)

**Typische jährliche Wartungskosten nach Motorklasse:**

| Motorklasse | Jährliche Wartung | 5-Jahres-Kosten | 10-Jahres-Kosten |
|-------------|------------------|-----------------|------------------|
| Segelboot-Hilfsmotor 10–30 PS | 200–400 EUR | 1.500–3.000 EUR | 4.000–8.000 EUR |
| Segelboot-Motor 30–60 PS | 300–600 EUR | 2.500–5.000 EUR | 6.000–12.000 EUR |
| Motorboot 60–150 PS | 500–1.000 EUR | 4.000–8.000 EUR | 10.000–20.000 EUR |
| Motorboot 150–300 PS | 800–1.500 EUR | 6.000–12.000 EUR | 15.000–30.000 EUR |
| Motoryacht 300–600 PS (×2) | 2.000–4.000 EUR | 15.000–30.000 EUR | 35.000–70.000 EUR |

---
---

## 14. Fehlerbild-Atlas

### 14.1 Fehlerbild: Schwarzer, dicker Ölschlamm

**Aussehen:** Schwarze, teerartige Ablagerungen auf Ventildeckel-Innenseite,
im Öleinfüllstutzen sichtbar.

**Ursachen:**
- Zu lange Ölwechselintervalle
- Dauerhafter Unterlastbetrieb (Segelboot-Syndrom)
- Minderwertiges Öl
- Defekter Thermostat (Motor wird nicht warm genug)

**Schweregrad:** MITTEL — langfristig schädlich, Ölkanäle verstopfen

**Maßnahme:**
- Ölwechsel mit Spülöl (Motor 10 Min. mit Spülöl laufen lassen)
- Künftig kürzere Intervalle (150h statt 250h)
- Motor regelmäßig unter Last fahren (30 Min. >75 % Last)
- Thermostat prüfen (Öffnungstemperatur 76–82 °C)

### 14.2 Fehlerbild: Milchiges Öl (Wasser im Öl)

**Aussehen:** Cremig-weiße bis hellbraune Emulsion am Peilstab
oder Öleinfülldeckel.

**Ursachen:**
- Kondensation (kurze Laufzeiten, häufiges An/Aus)
- Defekte Zylinderkopfdichtung (Kühlmittel ins Öl)
- Defekter Ölkühler (Seewasser ins Öl)
- Gerissener Motorblock (selten)

**Schweregrad:** HOCH bis KRITISCH

**Diagnose:**
- Kleine Menge am Öleinfülldeckel = wahrscheinlich Kondensation
- Ölstand steigt + Kühlmittelstand sinkt = Zylinderkopfdichtung
- Ölstand steigt stark + salziger Geschmack = Ölkühler

**Maßnahme:**
- Bei Kondensation: Motor länger laufen (>30 Min. unter Last)
- Bei Zylinderkopfdichtung: SOFORT Motor stoppen, Werkstatt
- Bei Ölkühler: Motor stoppen, Ölkühler austauschen

### 14.3 Fehlerbild: Übermäßiger Ölverbrauch

**Symptom:** Ölstand sinkt zwischen Wechseln deutlich, blauer Rauch.

**Ursachen:**
- Verschlissene Kolbenringe
- Verschlissene Ventilschaftdichtungen
- Undichtigkeit (extern: Ölwanne, Filter, Öldruckschalter)
- Turbolader-Wellendichtung defekt

**Normalverbrauch:**
| Motorklasse | Normaler Ölverbrauch |
|-------------|---------------------|
| Saugmotor <30 PS | <0,05 l/100h |
| Saugmotor 30–100 PS | <0,1 l/100h |
| Turbomotor 100–300 PS | <0,2 l/100h |
| Turbomotor >300 PS | <0,3 l/100h |

### 14.4 Fehlerbild: Schwarzer Rauch aus dem Auspuff

**Ursachen:**
- Verstopfter Luftfilter
- Defekte/verkokte Injektoren
- Überlastung (Propeller zu groß)
- Turbolader-Problem (kein Ladedruck)
- Falsches Ventilspiel
- Dieselpest (Mikroorganismen im Kraftstoff)

**Schweregrad:** MITTEL

**Diagnose-Reihenfolge:**
1. Luftfilter prüfen/reinigen
2. Propeller-Drehzahl bei Volllast messen (muss Nenndrehzahl erreichen)
3. Kraftstofffilter prüfen (Dieselpest?)
4. Ladedruck messen (Turbomotoren)
5. Injektoren prüfen lassen

### 14.5 Fehlerbild: Weißer Rauch aus dem Auspuff

**Ursachen:**
- Kaltstart (normal, verschwindet nach 5 Min.)
- Wasser im Zylinder (Zylinderkopfdichtung)
- Falsches Ventilspiel (Zylinder zündet nicht)
- Defekte Glühkerze (Zylinder zu kalt)
- Falscher Einspritzzeitpunkt

**Schweregrad:** NIEDRIG (Kaltstart) bis KRITISCH (Kopfdichtung)

**Diagnose:**
- Verschwindet nach Warmfahren → normal
- Bleibt + süßlicher Geruch → Kühlmittel → Kopfdichtung
- Bleibt + Dieselgeruch → Injektor/Timing → Werkstatt

### 14.6 Fehlerbild: Blauer Rauch aus dem Auspuff

**Ursachen:**
- Motoröl wird verbrannt
- Verschlissene Kolbenringe
- Verschlissene Ventilschaftdichtungen
- Turbolader-Wellendichtung defekt
- Zu viel Öl eingefüllt

**Schweregrad:** MITTEL bis HOCH

**Diagnose:**
- Rauch bei Kaltstart, dann weg → Ventilschaftdichtungen
- Rauch unter Last → Kolbenringe
- Rauch + Öl am Turbolader → Turbolader-Dichtung
- Ölstand über MAX → abpumpen

### 14.7 Fehlerbild: Überhitzungsalarm

**Ursachen:**
- Seeventil geschlossen (häufigster Fehler!)
- Impeller defekt
- Seewasserfilter/Seiher verstopft (Plastiktüte, Algen)
- Thermostat klemmt (geschlossen)
- Wärmetauscher verstopft (Kalk, Impeller-Fragmente)
- Keilriemen gerissen (wenn Süßwasserpumpe am Keilriemen)
- Kühlmittel fehlt

**Schweregrad:** KRITISCH — sofortiges Handeln!

**Sofortmaßnahme:**
1. Last reduzieren (Gas zurück)
2. Wenn Temperatur >100 °C: Motor stoppen
3. Kühlwasseraustritt am Auspuff prüfen
4. Wenn kein Wasser: Seeventil prüfen!
5. Seiher prüfen
6. Impeller prüfen

### 14.8 Fehlerbild: Motor springt nicht an

**Häufigste Ursachen nach Wahrscheinlichkeit:**

1. **Batterie leer** (60 % aller Fälle)
   - Spannung messen (<11,8 V → laden)
   - Polklemmen korrodiert → reinigen
2. **Luft im Kraftstoff** (20 %)
   - Filter gewechselt und nicht entlüftet
   - Undichte Kraftstoffleitung (saugt Luft)
   - Tank leer (Peilung täuscht!)
3. **Kraftstoff-Problem** (10 %)
   - Filter verstopft (Dieselpest)
   - Kraftstoff-Absperrhahn zu
   - Wasser im Kraftstoff
4. **Glühkerzen defekt** (5 %)
   - Vorglühen nicht möglich
   - Besonders bei Kälte relevant
5. **Sonstiges** (5 %)
   - Sicherung Anlasser
   - Startsperre (Gangschaltung nicht in Neutral)
   - Getriebe-Sicherheitsschalter defekt

### 14.9 Fehlerbild: Ungewöhnliche Motorgeräusche

| Geräusch | Mögliche Ursache | Schweregrad | Maßnahme |
|----------|-----------------|-------------|----------|
| Metallisches Klopfen (rhythmisch) | Kolbenspiel, Pleuellager | HOCH | Motor stoppen, Werkstatt |
| Ticken (schnell, oben) | Ventilspiel zu groß | NIEDRIG | Ventilspiel einstellen |
| Quietschen bei Start | Keilriemen rutscht | NIEDRIG | Spannung prüfen |
| Pfeifen unter Last | Turbolader-Schaufelbruch | MITTEL | Turbo prüfen |
| Schleifendes Geräusch | Impellerpumpe trocken | MITTEL | Seeventil prüfen |
| Klackern (unregelm.) | Injektor verkokt | MITTEL | Injektoren prüfen |
| Dumpfes Brummen | Motorlager defekt | NIEDRIG | Lager wechseln |
| Rasseln bei Gaswechsel | Zahnriemen/Steuerkette | HOCH (D3!) | Sofort prüfen! |

### 14.10 Fehlerbild: Motorvibrationen

**Ursachen:**
- Motorlager defekt/verschlissen
- Motor/Getriebe-Ausrichtung falsch (Misalignment)
- Propeller beschädigt oder bewachsen
- Flexkupplung verschlissen
- Zylinder zündet nicht (Unwucht)
- Schwingungsdämpfer defekt (Drehschwingungsdämpfer)

**Diagnose:**
1. Motor im Leerlauf (ohne Gang): Vibration vorhanden?
   - Ja → Motorproblem (Lager, Zünder)
   - Nein → Antriebsstrang-Problem
2. Im Gang, langsame Fahrt: Vibration vorhanden?
   - Ja → Ausrichtung, Propeller
   - Nein → Geschwindigkeitsabhängig → Resonanz

### 14.11 Fehlerbild: Kraftstoffleck

**Erkennungsmerkmale:**
- Dieselgeruch im Motorraum
- Nasse Stellen an Leitungen oder Fittings
- Kraftstoffverbrauch auffällig hoch
- Bilge riecht nach Diesel

**Schweregrad:** HOCH (Brand-/Umweltgefahr)

**Typische Leckstellen:**
- Kraftstofffilter-Dichtungen
- Einspritzleitungen (Vibrationsbruch)
- Rücklaufleitungen (Alterung)
- Tankabsperrhahn
- Kraftstoffschläuche (Alterung, UV)

### 14.12 Fehlerbild: Kühlmittelverlust ohne sichtbares Leck

**Ursachen:**
- Zylinderkopfdichtung (Kühlmittel → Verbrennungsraum)
- Mikroriss im Zylinderkopf
- Ölkühler-Leck (Kühlmittel → Öl, intern)
- Ausgleichsbehälter-Deckel undicht (Verdampfung)
- Wärmetauscher-Innenriss (Kühlmittel → Seewasser, intern)

**Diagnose:**
1. Ölpeilstab: milchig/cremig? → Kopfdichtung oder Ölkühler
2. Auspuff: weißer Rauch + süß? → Kopfdichtung
3. Drucktest Kühlsystem: Druck fällt → Leck
4. CO2-Test im Kühlmittel: positiv → Abgase im Kühlkreislauf → Kopfdichtung

---
---

## 15. Troubleshooting

### 15.1 Motor startet nicht — Entscheidungsbaum

```
Motor startet nicht
│
├── Anlasser dreht nicht
│   ├── Batteriespannung <11,8 V → Laden/Ersetzen
│   ├── Polklemmen korrodiert → Reinigen
│   ├── Startschalter/Sicherung → Prüfen
│   ├── Gangschaltung nicht in Neutral → In Neutral schalten
│   └── Anlasser defekt → Reparieren/Ersetzen
│
├── Anlasser dreht, Motor zündet nicht
│   ├── Kraftstoff vorhanden? → Tanken
│   ├── Luft im Kraftstoff → Entlüften
│   ├── Kraftstoffhahn offen? → Öffnen!
│   ├── Kraftstofffilter verstopft → Wechseln
│   ├── Glühkerzen defekt → Prüfen/Ersetzen
│   ├── Kompression zu niedrig → Messen
│   └── Einspritzzeitpunkt falsch → Werkstatt
│
└── Motor startet kurz und stirbt ab
    ├── Luft im Kraftstoff → Entlüften
    ├── Kraftstofffilter verstopft → Wechseln
    ├── Dieselpest → Filter + Tank reinigen
    ├── Wasser im Kraftstoff → Wasserabscheider leeren
    └── Motor überhitzt sofort → Kühlwasser prüfen
```

### 15.2 Motor überhitzt — Entscheidungsbaum

```
Überhitzungsalarm
│
├── Kein Wasser am Auspuff
│   ├── Seeventil geschlossen → ÖFFNEN!
│   ├── Seewasserfilter/Seiher verstopft → Reinigen
│   ├── Impeller defekt → Wechseln
│   ├── Seewasserpumpe defekt → Reparieren
│   └── Seewasserleitung verstopft → Spülen
│
├── Wasser kommt am Auspuff, Motor dennoch heiß
│   ├── Thermostat klemmt (geschlossen) → Ersetzen
│   ├── Wärmetauscher verstopft → Reinigen/Ersetzen
│   ├── Kühlmittelstand zu niedrig → Nachfüllen
│   ├── Keilriemen gerissen (Süßwasserpumpe) → Ersetzen
│   └── Süßwasserpumpe defekt → Reparieren
│
└── Temperaturanzeige unplausibel
    ├── Temperaturfühler defekt → Ersetzen
    ├── Anzeigeinstrument defekt → Prüfen
    └── Kabelbruch → Verbindung prüfen
```

### 15.3 Leistungsverlust — Entscheidungsbaum

```
Motor hat Leistungsverlust
│
├── Schwarzer Rauch
│   ├── Luftfilter verstopft → Reinigen/Wechseln
│   ├── Turbolader-Problem → Ladedruck messen
│   ├── Injektoren verkokt → Reinigen/Wechseln
│   └── Propeller zu groß → Drehzahl bei Vollgas prüfen
│
├── Weißer/Blauer Rauch
│   ├── Zylinder zündet nicht → Kompression, Glühkerze, Injektor
│   └── Öl wird verbrannt → Kolbenringe, Ventilschaftdichtung
│
├── Kein Rauch, aber wenig Leistung
│   ├── Propeller bewachsen → Reinigen
│   ├── Unterwasserschiff bewachsen → Reinigen
│   ├── Kraftstofffilter verstopft → Wechseln
│   ├── Getriebe rutscht → Getriebeöl und Kupplung prüfen
│   └── Ventilspiel falsch → Einstellen
│
└── Motor erreicht Nenndrehzahl nicht
    ├── Propeller überdimensioniert → Max-Drehzahl bei Vollgas prüfen
    ├── Turbolader defekt → Ladedruck messen
    └── Einspritzmenge falsch → Werkstatt
```

### 15.4 Ungewöhnlicher Ölverbrauch — Entscheidungsbaum

```
Ölverbrauch erhöht
│
├── Blauer Rauch vorhanden
│   ├── Nur bei Kaltstart → Ventilschaftdichtungen
│   ├── Dauerhaft unter Last → Kolbenringe verschlissen
│   └── Nach Turbolader → Turbolader-Wellendichtung
│
├── Kein Rauch, aber Ölstand sinkt
│   ├── Externe Undichtigkeit sichtbar → Abdichten
│   ├── Öl im Kühlmittel → Ölkühler-Leck
│   ├── Öl in der Bilge → Dichtungen prüfen
│   └── Ölstand über MAX eingefüllt → Zuviel, absaugen
│
└── Ölstand steigt (!!)
    ├── Kraftstoff im Öl → Injektor-Leck, Kolbenringe
    └── Kühlmittel im Öl → Kopfdichtung, Ölkühler
```

### 15.5 Ungewöhnliche Geräusche — Entscheidungsbaum

```
Ungewöhnliches Geräusch
│
├── Klopfen (rhythmisch, dumpf)
│   ├── Im Takt der Kurbelwelle → Hauptlager (KRITISCH!)
│   ├── Im Takt der Zündfolge → Pleuellager (KRITISCH!)
│   └── Nur bei Kaltstart → Kolbenspiel (beobachten)
│
├── Ticken (schnell, metallisch)
│   ├── Ventilspiel zu groß → Einstellen
│   └── Injektor-Geräusch → Normal oder verkokt
│
├── Quietschen
│   ├── Bei Start → Keilriemen
│   └── Dauerhaft → Lager (Lichtmaschine, Wasserpumpe)
│
├── Pfeifen
│   ├── Unter Last → Turbolader-Problem
│   └── Im Leerlauf → Ansaugluft-Leck
│
└── Rasseln
    ├── Steuerkettenspanner → Nachspannen/Wechseln
    └── Zahnriemen (D3!) → SOFORT prüfen! Motorschaden-Risiko!
```

---
---

## 16. FAQ

### 16.1 Ölwechsel

**F: Kann ich verschiedene Ölmarken mischen?**
A: Ja, sofern die Spezifikation (API-Klasse) und Viskosität identisch
sind. Mineralöl + Vollsynthetik sollte vermieden werden, ist aber
kurzzeitig nicht schädlich (z.B. Nachfüllen unterwegs).

**F: Ist teureres Öl automatisch besser?**
A: Nicht zwingend. Ein 15W-40 Mineralöl der API-Klasse CI-4 von einer
Marke wie Shell oder Mobil erfüllt alle Anforderungen eines Saugmotors.
Vollsynthetik lohnt sich bei Common-Rail-Motoren und bei extremen
Temperaturen.

**F: Muss ich bei 50 Stunden pro Jahr wirklich jährlich Öl wechseln?**
A: Ja, unbedingt. Öl altert auch durch Standzeit — Kondenswasser,
Oxidation, Additivverbrauch. Gerade bei wenig Betrieb ist der jährliche
Wechsel essentiell.

**F: Kann ich den Erstservice (50h) überspringen?**
A: Nein. Neue Motoren produzieren Metallabrieb beim Einlaufen. Ohne
Erstservice zirkulieren diese Partikel und verursachen Verschleiß.

**F: Sollte ich zwischen den Wechseln den Ölstand prüfen?**
A: Ja, mindestens alle 25 Betriebsstunden. Ein plötzlicher Ölstandsverlust
deutet auf ein Problem hin.

### 16.2 Kraftstoff

**F: Wie lange hält Diesel im Tank?**
A: 6–12 Monate bei guter Tankbelüftung und ohne Wasser. Mit Stabilisator
(Sta-Bil) bis 24 Monate. Diesel-Bug kann schon nach 3 Monaten auftreten,
wenn Wasser im Tank ist.

**F: Kann ich Bio-Diesel verwenden?**
A: EN 590 Diesel in Deutschland enthält bis zu 7 % Bio-Diesel (B7) und
ist unproblematisch. Reiner Bio-Diesel (B100) wird von den meisten
Marine-Diesel-Herstellern NICHT freigegeben — er greift Dichtungen an
und begünstigt mikrobiellen Befall.

**F: Mein Kraftstofffilter verstopft ständig — was tun?**
A: Häufigste Ursache ist Dieselpest. Tank inspizieren (Endoskop),
bei Befall: Tank reinigen, Biozid-Behandlung, Filter wechseln.
Zweithäufigste Ursache: Rost im Tank (Stahltanks).

**F: Kann ich den Racor-Wasserabscheider weglassen?**
A: Absolut nicht. Der Racor (oder gleichwertiger Vorfilter) ist die
Lebensversicherung der Einspritzpumpe und Injektoren. Einspritzanlagen-
Reparatur: 2.000–8.000 EUR. Racor-Einsatz: 15–30 EUR.

### 16.3 Impeller

**F: Wie oft muss der Impeller gewechselt werden?**
A: Alle 250 Betriebsstunden oder jährlich (Saisonbeginn). Bei
Chartereinsatz (>400h/Jahr) alle 200 Stunden.

**F: Mein Impeller sieht noch gut aus — muss ich ihn trotzdem wechseln?**
A: Ja. Neopren-Impeller werden mit der Zeit hart (insbesondere bei
Standzeit). Ein optisch intakter, aber verhärteter Impeller kann
bei der nächsten Belastung spontan versagen.

**F: Was passiert mit abgebrochenen Impeller-Flügeln?**
A: Sie wandern in den Wärmetauscher und verstopfen die Rohre. Beim
Impellerwechsel IMMER alle Flügel zählen. Fehlende Flügel müssen
gesucht und entfernt werden!

**F: Kann ich Vaseline zum Schmieren verwenden?**
A: Ja, Vaseline (Petroleumgelee) oder Glycerin. KEIN Silikonfett
(quellet den Gummi auf) und KEIN mineralisches Fett.

**F: Darf ich einen Aftermarket-Impeller verwenden?**
A: Ja, Jabsco und Johnson Aftermarket-Impeller sind gleichwertig zu
den (identischen) OEM-Impellern der Motorhersteller. Tatsächlich sind
Jabsco-Impeller oft die OEM-Impeller unter anderer Teilenummer.

### 16.4 Kühlsystem

**F: Kann ich Leitungswasser als Kühlmittel verwenden?**
A: Niemals als Dauerlösung. Leitungswasser enthält Kalk, der die
Kühlkanäle verstopft. Im Notfall (auf See): ja, aber schnellstmöglich
durch korrekte Mischung ersetzen.

**F: Mein Kühlmittel ist braun — muss ich es wechseln?**
A: Ja. Braunes Kühlmittel zeigt Korrosion und verbrauchte Additive.
System spülen und mit frischem Kühlmittel befüllen.

**F: Kann ich OAT- und IAT-Kühlmittel mischen?**
A: NEIN. Die Additive reagieren miteinander und bilden Gel, das die
Kühlkanäle verstopft. Bei Typwechsel: System komplett spülen.

**F: Muss ich die Seewasserseite auch im Winter schützen?**
A: Ja! Restwasser in Wärmetauscher, Auspuffkrümmer und Leitungen
gefriert und kann die Komponenten sprengen. Propylenglyko-Frostschutz
durchlaufen lassen (siehe Winterlager).

### 16.5 Keilriemen und Zahnriemen

**F: Mein Keilriemen quietscht beim Start — was tun?**
A: Spannung prüfen (10–15 mm Durchbiegung bei Daumendruck). Zu locker
→ nachspannen. Riemen glasig/alt → wechseln. Nass → trocken werden
lassen.

**F: Ist der Zahnriemenwechsel am D3 wirklich so kritisch?**
A: Ja. Der D3 ist ein „Interferenzmotor" — bei Zahnriemenriss treffen
Kolben auf Ventile = Totalschaden. Das Wechselintervall (1.000h/5 Jahre)
ist NICHT verhandelbar.

**F: Kann ich den Zahnriemen am D3 selbst wechseln?**
A: Technisch möglich, aber nur mit den Volvo-Spezialwerkzeugen
(Fixierstifte 9995451/9995452) und Erfahrung. Ein Fehler bei der
Steuerzeiten-Einstellung = Motorschaden beim ersten Start. Empfehlung:
Werkstatt.

### 16.6 Winterlager

**F: Muss ich wirklich Fogging Oil verwenden?**
A: Bei Motoren mit langer Standzeit (>4 Monate): dringend empfohlen.
Fogging Oil bildet einen Schutzfilm auf Zylindern und Ventilen gegen
Korrosion. Alternative: einige Tropfen Motoröl durch Glühkerzenöffnung.

**F: Was passiert, wenn ich das Winterlager vergesse?**
A: Frostschaden (Seewasserseite friert → Block/Wärmetauscher reißt),
Korrosion im Zylinder (Kondenswasser), verharzter Kraftstoff,
Batterie-Tod. Kosten: 500–15.000 EUR je nach Schaden.

**F: Kann ich den Motor auch im Winter gelegentlich laufen lassen?**
A: Nur, wenn das Boot im Wasser liegt und alle Systeme in Betrieb
sind. Am Winterlager-Platz an Land: NEIN — kein Kühlwasser → Motor
überhitzt sofort. Motor muss mindestens 30 Minuten unter Last laufen,
um Kondenswasser zu verdampfen.

**F: Reicht es, den Tank voll zu machen?**
A: Voller Tank minimiert Kondensation, ersetzt aber nicht die übrige
Winterlager-Prozedur (Öl, Seewassersystem, Fogging, Batterie).

### 16.7 Ventilspiel

**F: Wie erkenne ich, dass das Ventilspiel zu groß ist?**
A: Lautes, regelmäßiges Ticken/Klappern im Ventilbereich, besonders
im Leerlauf. Wird leiser bei hoher Drehzahl.

**F: Muss ich beim Volvo D3 das Ventilspiel einstellen?**
A: Nein. Der D3 hat hydraulische Ventilspielausgleicher (Hydrostößel).
Wenn der D3 tickt, sind möglicherweise die Hydrostößel verschmutzt
oder defekt → Werkstatt.

**F: Kann ich das Ventilspiel selbst einstellen?**
A: Ja, mit Fühllehrenset und Grundkenntnissen. Werkzeuge: Fühllehren,
Ringschlüssel, Schraubendreher. Wichtig: Motor KALT, korrekte Zylinder-
position (OT/Verdichtungstakt).

### 16.8 Zinkanoden

**F: Wie oft Zinkanoden prüfen?**
A: Alle 100–250 Betriebsstunden oder halbjährlich. In Häfen mit
schlechter Erdung: monatlich.

**F: Meine Anoden lösen sich extrem schnell auf — warum?**
A: Streuströme! Häufig durch fehlerhafte Landstrom-Anschlüsse anderer
Boote in der Marina. Galvanischen Isolator (ProSafe/Galvanic Isolator)
installieren.

**F: Meine Anoden sehen nach 2 Jahren unverändert aus — ist das gut?**
A: NEIN. Das bedeutet, die Anode hat keinen elektrischen Kontakt und
schützt nicht. Gewinde reinigen, Kontaktfläche blank machen, Sitz prüfen.

### 16.9 Allgemeine Wartung

**F: Was ist die wichtigste einzelne Wartungsmaßnahme?**
A: Der regelmäßige Ölwechsel mit Filter. Wenn Sie nur EINE Sache tun:
Öl wechseln.

**F: Kann ich die Wartung komplett selbst machen?**
A: Die meisten Routinearbeiten (Öl, Filter, Impeller, Keilriemen,
Zinkanoden, Winterlager) sind für technisch begabte Eigner machbar.
Injektoren, Zahnriemen (D3), Turbolader und Kompressionstest sollten
der Werkstatt überlassen werden.

**F: Wie finde ich eine gute Marine-Motorwerkstatt?**
A: Herstellerautorisierung prüfen (Yanmar/Volvo Service Partner),
Referenzen anderer Eigner im Hafen, Mitgliedschaft im DBSV
(Deutscher Boots- und Schiffbauer-Verband).

**F: Mein Motor hat wenige Betriebsstunden aber ist alt — worauf achten?**
A: Standschäden! Kolbenringe verharzen, Dichtungen werden spröde,
Kraftstoff verharzt, Kühlmittel wird sauer. Ein 20 Jahre alter Motor
mit 500 Stunden kann in schlechterem Zustand sein als ein 10 Jahre
alter mit 3.000 Stunden.

### 16.10 Kosten

**F: Was kostet ein typischer Jahresservice?**
A: Für einen Segelboot-Motor (20–40 PS): Material 150–250 EUR,
Arbeitszeit (wenn Werft) 150–300 EUR, gesamt 300–550 EUR.
Selbstgemacht: nur Materialkosten.

**F: Lohnt sich ein Motor-Servicevertrag?**
A: Bei professionellem Charterservice ja. Für Privat-Eigner selten —
die Materialkosten sind gering, und Eigenarbeit ist bei Routinewartung
gut machbar.

**F: Was kostet eine Motorüberholung (Grundüberholung)?**
A: Abhängig von Motor und Umfang:
- Kleiner Motor (1GM/2YM): 3.000–6.000 EUR
- Mittlerer Motor (3JH/4JH): 5.000–12.000 EUR
- Großer Motor (D4/D6): 10.000–25.000 EUR
- Inklusive Ausbau/Einbau: +2.000–5.000 EUR

### 16.11 Digitale Diagnose

**F: Kann ich den CAN-Bus meines Motors selbst auslesen?**
A: Volvo Penta EVC (ab D3): Ja, mit VODIA-Diagnosetool (Werkstatt)
oder kompatibler Software. Yanmar: eingeschränkt, kein Standard-OBD.
Ältere Motoren (vor 2010): meist kein CAN-Bus vorhanden.

**F: Was zeigt mir die Motor-Diagnose?**
A: Betriebsstunden, Fehlerspeicher, Temperaturen, Drücke,
Einspritzmenge, Turboladerdruck, Batteriespannung. Bei Common-Rail:
Injektorkorrekturen (Hinweis auf Verschleiß).

### 16.12 Umwelt

**F: Wohin mit dem Altöl?**
A: Kommunale Schadstoffsammelstelle (kostenlos für Privat), Marina-
Entsorgung (oft vorhanden), Werft. NIEMALS in die Bilge, ins Wasser
oder in den Hausmüll.

**F: Ist Propylenglyko-Frostschutz umweltverträglich?**
A: Propylenglykol ist biologisch abbaubar und nur gering wassergefährdend
(WGK 1). Es darf dennoch nicht absichtlich ins Wasser eingeleitet werden.
Bei der Frühjahrs-Inbetriebnahme gelangt eine geringe Menge über den
Auspuff ins Wasser — dies ist unvermeidlich und unkritisch.

### 16.13 Ersatzteile

**F: Wo kaufe ich Marine-Motor-Ersatzteile?**
A: Hersteller-Vertragshändler, Online-Shops (SVB, Compass, AWN,
Bootsteile24), internationale Shops (MarinePartsEurope für Volvo Penta).
Teilenummern aus dem Werkstatthandbuch oder den Tabellen in diesem
Dokument verwenden.

**F: Sind „Marine-Ölfilter" anders als KFZ-Ölfilter?**
A: Oft identisch! Viele Marine-Filter sind identische KFZ-Filter unter
anderer Teilenummer und höherem Preis. Die Cross-Reference-Tabellen in
Kapitel 4 zeigen die Äquivalenzen.

### 16.14 Betriebsstunden

**F: Wie viele Betriebsstunden pro Jahr sind normal?**
A: Segelboot: 100–300h, Motorboot Wochenende: 100–200h, Motorboot
intensiv: 200–500h, Charter: 500–1.500h, Berufsschifffahrt: 2.000–5.000h.

**F: Ab wie vielen Stunden ist ein Motor „verbraucht"?**
A: Bei guter Wartung: Saugmotoren 8.000–15.000h, Turbomotoren
5.000–10.000h. Ohne Wartung: bereits ab 2.000–3.000h kritisch.

**F: Wie kann ich die Betriebsstunden eines Gebrauchtboots überprüfen?**
A: Betriebsstundenzähler ablesen, Wartungsbuch prüfen (Stunden bei jedem
Service eingetragen?), Zustand des Motors mit den angegebenen Stunden
abgleichen (Kompressionstest, Ölanalyse). Bei elektronischen Motoren
(CAN-Bus): Auslesen des Motorsteuergeräts — dort sind die Stunden
manipulationssicher gespeichert. Bei mechanischen Zählern: Manipulation
ist leider möglich.

### 16.15 Spezielle Situationen

**F: Kann ich mit einem Zylinder weniger nach Hause fahren?**
A: Ja, bei einem Mehrzylindermotor mit defektem Injektor (1 Zylinder
zündet nicht) können Sie mit reduzierter Leistung weiterfahren.
Nicht empfohlen bei Klopfgeräuschen oder Lagerschaden.

**F: Was tun bei Wassereinbruch im Motor?**
A: Durch Auspuff (Rückfluss bei Seegang): Wasser über Dekompressionsventil
oder Injektoröffnung ablassen, Öl wechseln, trockenkurbeln, neu befüllen.
Durch Überflutung (Havarie): Motor NICHT starten! Professionelle
Konservierung und Überholung erforderlich.

**F: Mein Boot liegt im Süßwasser — brauche ich trotzdem Zinkanoden?**
A: Ja, aber Magnesium-Anoden statt Zink. Süßwasser ist ein schwächerer
Elektrolyt, Zink-Anoden erzeugen zu wenig Schutzstrom. Magnesium hat
ein höheres Potential und schützt im Süßwasser besser. NIEMALS
Magnesium im Salzwasser verwenden (löst sich extrem schnell auf).

**F: Kann ich meinen Motor auf Biodiesel umrüsten?**
A: Die meisten Marine-Diesel vertragen B7 (7 % Biodiesel-Anteil, EU-Standard)
problemlos. Höhere Bio-Anteile (B20, B100) werden von den meisten
Herstellern nicht freigegeben. Probleme: Dichtungsquellung, erhöhte
Dieselpest-Anfälligkeit, Verstopfung bei Kälte. Yanmar gibt maximal B5
frei, Volvo Penta B7, Beta Marine B10.

---
---

## 17. Glossar

### A

| Begriff | Erklärung |
|---------|-----------|
| **Ablassschraube** | Schraube am tiefsten Punkt der Ölwanne zum Ablassen des Motoröls |
| **Abgaskrümmer** | Gusseisenteil, das die Abgase der einzelnen Zylinder zusammenführt. Im Marine-Bereich oft mit Wassereinspritzung (Nassmischer) kombiniert |
| **API-Klasse** | American Petroleum Institute Klassifikation für Motoröle (z.B. CI-4, CJ-4, CK-4). Höhere Buchstaben = neuere/bessere Spezifikation |
| **Ausgleichsbehälter** | Behälter für Kühlmittel-Überlauf bei Wärmeausdehnung, zugleich Nachfüllpunkt |

### B

| Begriff | Erklärung |
|---------|-----------|
| **Betriebsstunden** | Laufzeit des Motors, gemessen durch Betriebsstundenzähler. Primäres Wartungsintervall-Kriterium |
| **Biozid** | Chemischer Wirkstoff gegen biologischen Befall im Kraftstoff (z.B. Grotamar 82) |
| **Bleistift-Anode** | Zylindrische Zinkanode, die in Motorblock oder Wärmetauscher eingeschraubt wird |
| **Bilge** | Tiefster Punkt im Bootsinneren, wo sich Wasser und Leckflüssigkeiten sammeln |

### C

| Begriff | Erklärung |
|---------|-----------|
| **CAN-Bus** | Controller Area Network — Datenbus für elektronische Motorsteuerung und Diagnose |
| **Common-Rail** | Hochdruck-Einspritzsystem mit gemeinsamer Druckleitung. Drücke: 1.600–2.500 bar |
| **Coolant** | Englisch für Kühlmittel (Frostschutz-Wasser-Gemisch) |

### D

| Begriff | Erklärung |
|---------|-----------|
| **Dekompressionsventil** | Handventil zum manuellen Öffnen der Zylinderventile, erleichtert das Durchdrehen von Hand |
| **Dieselpest** | Mikrobieller Befall des Kraftstoffs (Bakterien/Pilze) an der Wasser-Diesel-Grenzschicht |
| **Drehmoment** | Kraft × Hebelarm, gemessen in Nm. Dieselmotoren haben hohes Drehmoment bei niedrigen Drehzahlen |
| **Drehschwingungsdämpfer** | Masse am Schwungrad-Ende der Kurbelwelle, dämpft Torsionsschwingungen |

### E

| Begriff | Erklärung |
|---------|-----------|
| **Einspritzdüse** | Feinst gefertigte Düse am Injektor, spritzt Kraftstoff in den Brennraum. Toleranzen: 1–5 µm |
| **Einspritzzeitpunkt** | Zeitpunkt der Kraftstoff-Einspritzung relativ zur Kolbenposition. Falsch eingestellt → Leistungsverlust, Rauch |
| **Entlüften** | Entfernen von Luft aus dem Kraftstoffsystem nach Filterwechsel oder Tankenleerung |
| **EPDM** | Ethylen-Propylen-Dien-Monomer — synthetischer Gummi für Kühlwasserschläuche und Impeller |
| **Erstservice** | Erster Ölwechsel nach 50 Betriebsstunden bei neuem Motor |

### F

| Begriff | Erklärung |
|---------|-----------|
| **Feinfilter** | Sekundärfilter am Motor (2–10 µm), letzte Filtrationsstufe vor den Injektoren |
| **Flexkupplung** | Elastische Kupplung zwischen Motor und Getriebe/Welle, gleicht Vibrationen und minimale Versätze aus |
| **Fogging Oil** | Konservierungsöl-Spray, das im Winterlager in die Ansaugung gesprüht wird und einen Schutzfilm auf Zylindern und Ventilen bildet |
| **Frostschutz** | Glykol-basiertes Konzentrat, das dem Kühlwasser zugesetzt wird. Senkt den Gefrierpunkt und schützt vor Korrosion |
| **Fühllehre** | Genormte Metallblättchen zum Messen von Spaltmaßen (z.B. Ventilspiel). Sets: 0,05–0,50 mm |

### G

| Begriff | Erklärung |
|---------|-----------|
| **Galvanische Korrosion** | Elektrochemische Korrosion zwischen verschiedenen Metallen in einem Elektrolyt (Seewasser) |
| **Getriebeöl** | Schmieröl für das Wendegetriebe oder Saildrive. Typisch: ATF oder SAE 80W-90 |
| **Glühkerze** | Elektrisches Heizelement im Brennraum, erleichtert den Kaltstart des Dieselmotors |
| **Grotamar 82** | Standard-Biozid für die Behandlung von Dieselpest. Wirkstoff: CMIT/MIT |

### H

| Begriff | Erklärung |
|---------|-----------|
| **Hobbs-Zähler** | Mechanischer Betriebsstundenzähler (benannt nach dem Hersteller) |
| **Hydrostößel** | Hydraulischer Ventilspielausgleicher, eliminiert die Notwendigkeit manueller Ventilspiel-Einstellung (z.B. Volvo D3) |

### I

| Begriff | Erklärung |
|---------|-----------|
| **IAT** | Inorganic Acid Technology — konventionelles Kühlmittel mit anorganischen Additiven (Silikat, Phosphat) |
| **Impeller** | Flexibler Gummi-Rotor in der Seewasserpumpe, fördert Kühlwasser durch Verdrängungsprinzip |
| **Injektor** | Einspritzventil, bringt Kraftstoff in den Brennraum. Bei Common-Rail: elektronisch gesteuert, Drücke bis 2.500 bar |

### K

| Begriff | Erklärung |
|---------|-----------|
| **Keilriemen** | V-förmiger Antriebsriemen für Lichtmaschine und Pumpen. Spannung: 10–15 mm Durchbiegung bei Daumendruck |
| **Kipphebel** | Hebelmechanismus im Ventiltrieb, überträgt Nockenwellenbewegung auf das Ventil |
| **Kompression** | Verdichtungsdruck im Zylinder, gemessen mit Kompressionstester. Sollwerte: 25–35 bar (motorabhängig) |
| **Kondenswasser** | Wasser, das durch Temperaturwechsel im Motor/Tank aus der Luft kondensiert. Hauptursache für Korrosion bei Standzeiten |
| **Kühlmittel** | Gemisch aus Frostschutz-Konzentrat und Wasser im geschlossenen Kühlkreislauf |

### L

| Begriff | Erklärung |
|---------|-----------|
| **Lichtmaschine** | Generator am Motor, lädt die Bordbatterie und versorgt die Elektrik. Angetrieben per Keilriemen |
| **Lagerschale** | Halbschalenförmiges Gleitlager für Kurbelwelle (Hauptlager) und Pleuel (Pleuellager). Material: Blei-Zinn oder Aluminium-Zinn |

### M

| Begriff | Erklärung |
|---------|-----------|
| **Marinisierung** | Anpassung eines Industrie-/Automobilmotors für den maritimen Einsatz (Kühlung, Korrosionsschutz, Elektrik, Lagerung) |
| **Misalignment** | Fehlausrichtung zwischen Motor und Getriebe/Welle. Verursacht Vibrationen, Lagerschäden, Kupplungsverschleiß |
| **Motorlager** | Gummi-Metall-Element, auf dem der Motor steht. Isoliert Vibrationen und trägt das Motorgewicht |

### N

| Begriff | Erklärung |
|---------|-----------|
| **Nassmischer** | Abgasmischer (Mixing Elbow), in den Seewasser zur Kühlung der Abgase eingespritzt wird. Verschleißteil (Korrosion) |
| **Neopren** | Synthetischer Gummi (Chloropren), Standardmaterial für Seewasser-Impeller |
| **Nenndrehzahl** | Maximale Dauerdrehzahl des Motors laut Hersteller. Propeller muss darauf abgestimmt sein |

### O

| Begriff | Erklärung |
|---------|-----------|
| **OAT** | Organic Acid Technology — langlebiges Kühlmittel mit organischen Korrosionsinhibitoren. NICHT mit IAT mischbar |
| **Ölanalyse** | Laboruntersuchung des Altöls auf Verschleißmetalle, Verunreinigungen und Additivzustand. Bestes Frühwarnsystem für Motorprobleme |
| **Ölkühler** | Wärmetauscher, der das Motoröl kühlt. Bei Marine-Diesel: seewassergekühlt (Korrosionsrisiko) |
| **OT (Oberer Totpunkt)** | Höchste Position des Kolbens im Zylinder. Referenzpunkt für Steuerzeiten und Ventilspiel-Einstellung |

### P

| Begriff | Erklärung |
|---------|-----------|
| **Peilstab** | Messstab zur Kontrolle des Motoröl-Standes. MIN und MAX Markierungen beachten |
| **Pleuellager** | Gleitlager am Pleuel (Verbindung Kolben-Kurbelwelle). Verschleiß = Klopfgeräusch |
| **Propylenglykol** | Ungiftiger Frostschutz für die Seewasserseite (Winterlager). NICHT mit Ethylenglykol (giftig) verwechseln! |

### R

| Begriff | Erklärung |
|---------|-----------|
| **Racor** | Markenname (Parker Hannifin) für marine Kraftstoff-Vorfilter mit Wasserabscheidung. Branchenstandard |
| **Refraktometer** | Optisches Messgerät zur Bestimmung der Frostschutzkonzentration im Kühlmittel |

### S

| Begriff | Erklärung |
|---------|-----------|
| **Saildrive** | Antriebseinheit, die Getriebe und Unterwasser-Antrieb in einem Gehäuse vereint (statt klassischer Welle). Hersteller: Volvo Penta, Yanmar SD |
| **Seeventil** | Absperrhahn am Rumpfdurchlass für Seewasser. MUSS geschlossen werden bei Impeller-Arbeit und Winterlager |
| **Seiher** | Seewasserfilter (Gitterkorb) am Rumpfdurchlass, hält Grobschmutz, Algen und Quallen zurück |
| **Spülöl** | Spezielles Motoröl mit erhöhtem Reinigungsvermögen, wird vor dem Ölwechsel eingesetzt, um Ablagerungen zu lösen |
| **Sta-Bil** | Markenname für Kraftstoff-Stabilisator. Verhindert Alterung und Verharzung bei langer Lagerung |

### T

| Begriff | Erklärung |
|---------|-----------|
| **TBN (Total Base Number)** | Basenzahl des Öls — Maß für die Fähigkeit, Säuren zu neutralisieren. Sinkt mit Nutzung. <3 = Öl verbraucht |
| **TAN (Total Acid Number)** | Säurezahl des Öls — Maß für Säuren im Öl. Steigt mit Nutzung. >4 = Öl aggressiv |
| **Thermostat** | Temperaturgesteuertes Ventil im Kühlkreislauf. Öffnet bei 76–82 °C, regelt die Motortemperatur |
| **Timing Belt** | Englisch für Zahnriemen (Steuerzahnriemen). Treibt die Nockenwelle an. Kritisch am Volvo D3! |
| **Turbolader** | Abgasgetriebenes Verdichterrad, presst mehr Luft in den Motor → mehr Leistung aus gleichem Hubraum |

### V

| Begriff | Erklärung |
|---------|-----------|
| **Ventilspiel** | Abstand zwischen Kipphebel und Ventilschaft bei geschlossenem Ventil. Kompensiert Wärmedehnung. Gemessen in mm |
| **Verglasung** | Glatte, spiegelnde Oberfläche der Zylinderlaufbahn durch Unterlastbetrieb. Öl haftet nicht mehr → erhöhter Verbrauch |
| **Vorfilter** | Primärfilter im Kraftstoffsystem (10–30 µm), typisch mit Wasserabscheider (Racor). Schützt den Feinfilter |
| **VDS (Volvo Drain Specification)** | Volvo-eigene Öl-Spezifikation (VDS-3, VDS-4, VDS-4.5). Muss bei Volvo-Motoren eingehalten werden |

### W

| Begriff | Erklärung |
|---------|-----------|
| **Wärmetauscher** | Gerät zur Wärmeübertragung zwischen zwei Kreisläufen (Süßwasser ↔ Seewasser) ohne Vermischung |
| **Wasserabscheider** | Vorrichtung im Kraftstoff-Vorfilter, die Wasser vom Diesel trennt (durch Schwerkraft oder Zentrifugaleffekt) |
| **Waterlock** | Wassersammelschalldämpfer im Abgassystem. Verhindert Wassereintritt in den Motor bei Seegang |
| **Wear-Plate** | Austauschbare Verschleißplatte in der Impellerpumpe. Verschleißt mit dem Impeller zusammen |
| **Wendegetriebe** | Mechanisches Getriebe zwischen Motor und Propellerwelle. Ermöglicht Vorwärts, Rückwärts, Neutral |
| **Winterization** | Englisch für Winterlager-Prozedur. Konservierung des Motors für die Winterpause |

### U

| Begriff | Erklärung |
|---------|-----------|
| **Unterlastbetrieb** | Betrieb des Motors bei weniger als 40 % der Nennleistung über längere Zeit. Führt zu Verglasung, Rußaufbau und Injektorverkokung. Typisches Segelboot-Problem |
| **Umpumpen** | Transferieren von Kraftstoff zwischen Tanks oder aus dem Tank zur Reinigung. Erfolgt mit separater Umfüllpumpe |

### Z

| Begriff | Erklärung |
|---------|-----------|
| **Zahnriemen** | Gezahnter Gummiriemen zum Antrieb der Nockenwelle (nur Volvo D3!). Riss = Motorschaden |
| **Zinkanode** | Opferanode aus Zink, schützt edlere Metalle (Motorblock, Wärmetauscher) vor galvanischer Korrosion |
| **Zündfolge** | Reihenfolge, in der die Zylinder eines Mehrzylinder-Motors zünden. Bestimmt die Reihenfolge bei Ventilspiel-Einstellung |
| **Zylinderkopfdichtung** | Dichtung zwischen Motorblock und Zylinderkopf. Dichtet Brennraum, Ölkanäle und Kühlwasserkanäle gegeneinander ab |
| **Zylinderverglasung** | Glätten der Zylinderhonierung durch Unterlastbetrieb. Öl haftet nicht, Verbrauch steigt, Kompression sinkt |

---
---

## 18. Schnell-Referenz

### 18.1 Ölwechsel-Schnellreferenz

| Motor | Ölmenge (mit Filter) | Viskosität | Filter-Nr. | Intervall |
|-------|---------------------|-----------|-----------|-----------|
| Yanmar 1GM10 | 1,3 l | 15W-40 | 119305-35151 | 250h/jährlich |
| Yanmar 2YM15 | 2,0 l | 15W-40 | 119305-35151 | 250h/jährlich |
| Yanmar 3YM20/30 | 3,0 l | 15W-40 | 119305-35170 | 250h/jährlich |
| Yanmar 4JH45/57 | 5,1 l | 15W-40 | 129150-35170 | 250h/jährlich |
| Yanmar 4JH80/110 | 5,6–6,5 l | 15W-40 | 129150-35170 | 250h/jährlich |
| Volvo D1-13/20 | 2,6 l | 15W-40 | 3840525 | 200h/jährlich |
| Volvo D1-30 | 3,5 l | 15W-40 | 3840525 | 200h/jährlich |
| Volvo D2-40–75 | 4,5–5,2 l | 15W-40 | 21549544 | 200h/jährlich |
| Volvo D3 | 8,0 l | 5W-30 | 22030848 | 200h/jährlich |
| Volvo D4 | 10,5 l | 15W-40 | 22030848 | 200h/jährlich |
| Volvo D6 | 18,0 l | 15W-40 | 21632901 | 200h/jährlich |
| Beta 14–30 | 2,5–3,5 l | 15W-40 | 211-63250 | 250h/jährlich |
| Beta 35–75 | 4,5–7,5 l | 15W-40 | 211-63252 | 250h/jährlich |
| Nanni N2–N3 | 1,8–3,8 l | 15W-40 | 970312711/21 | 200h/jährlich |
| Nanni N4–T4 | 5,0–14,0 l | 15W-40 | 970312731/51 | 200h/jährlich |

### 18.2 Impeller-Schnellreferenz

| Motor | Genuine Impeller | Jabsco Equiv. | Wechselintervall |
|-------|-----------------|--------------|-----------------|
| Yanmar 1GM/2YM | 128176-42071 | 1210-0001-P | 250h/jährlich |
| Yanmar 3YM | 128990-42200 | 1210-0001-P | 250h/jährlich |
| Yanmar 3JH/4JH | 129470-42530 | 4528-0001-P | 250h/jährlich |
| Yanmar 4LHA/6LY | 119773-42600 | 6303-0001-P | 250h/jährlich |
| Volvo D1 | 3593573 | 1210-0001-P | 200h/jährlich |
| Volvo D2 | 3593660 | 4528-0001-P | 200h/jährlich |
| Volvo D3/D4 | 21951346 | 6303-0001-P | 200h/jährlich |
| Volvo D6 | 3588475 | 17936-0001-P | 200h/jährlich |
| Beta 14–38 | 211-60001/02 | 920-0001-P | 250h/jährlich |
| Beta 43–150 | 211-60002/04 | 4528/6303-0001-P | 250h/jährlich |
| Nanni N2/N3 | 970305401 | 920-0001-P | 200h/jährlich |
| Nanni N4/T4 | 970305402/04 | 4528/6303-0001-P | 200h/jährlich |

### 18.3 Kritische Drehmomente

| Bauteil | Drehmoment (Nm) | Hinweis |
|---------|----------------|---------|
| Ölablassschraube | 25–35 | Neuen Dichtring verwenden |
| Ölfilter (Spin-On) | Handfest + ¾ Umdrehung | KEIN Werkzeug! |
| Ventildeckel | 8–12 | Gleichmäßig, kreuzweise |
| Zylinderkopf | Motor-spezifisch (80–120) | Immer in Stufen, Reihenfolge beachten |
| Glühkerze | 15–25 | Nicht überdrehen! |
| Impeller-Pumpendeckel | 5–10 | Bei Kunststoff: vorsichtig! |
| Zinkanode (Bleistift) | 15–20 | Handfest + ¼ Umdrehung |
| Seeventil | 20–30 | Nicht klemmen |
| Kraftstofffilter | Handfest + ¾ Umdrehung | Analog Ölfilter |

### 18.4 Winterlager-Kurzliste

```
□ Öl + Filter wechseln (Motor warm!)
□ Tank VOLL tanken + Stabilisator
□ Seewasserseite mit Propylenglykol-Frostschutz durchlaufen lassen
□ Kühlmittel-Frostschutz prüfen (min. −25 °C)
□ Fogging Oil in Ansaugung sprühen
□ Waterlock entleeren
□ Auspuffauslass verschließen
□ Batterie laden + Erhaltungsladung ODER abklemmen
□ Getriebeöl prüfen
□ Motor außen mit Korrosionsschutz einsprühen
□ Entfeuchterbeutel in Motorraum
```

---
---

## 19. ANHANG A–H: Fallstudien

### ANHANG A — Fallstudie: Yanmar 3YM30 nach 3.000h ohne Motorüberholung

**Ausgangslage:**
- Bavaria 36, Baujahr 2008, Yanmar 3YM30 (29 PS)
- 3.100 Betriebsstunden, Motor nie überholt
- Wartung: regelmäßiger Ölwechsel (alle 200h), Impeller jährlich
- Problem: leichter blauer Rauch, Ölverbrauch 0,15 l/100h

**Diagnose:**
- Kompression: Zyl. 1 = 26 bar, Zyl. 2 = 28 bar, Zyl. 3 = 25 bar
  (Sollwert: 30–32 bar → alle niedrig, aber gleichmäßig)
- Ölanalyse: Eisen 65 ppm (erhöht), Chrom 8 ppm (erhöht) → Kolbenringverschleiß
- Ventilspiel: Auslass Zyl. 3 auf 0,25 mm (soll: 0,20 mm)
- Turbolader: nicht vorhanden (Saugmotor)

**Maßnahmen:**
1. Ventilspiel alle Zylinder eingestellt (Kosten: 120 EUR)
2. Injektoren überholt (Kosten: 3×180 = 540 EUR)
3. Keine Grundüberholung — Zustand für weitere 1.500–2.000h akzeptabel
4. Ölwechsel-Intervall auf 150h verkürzt
5. Halbjährliche Ölanalyse empfohlen

**Ergebnis:** Blauer Rauch deutlich reduziert, Ölverbrauch auf 0,08 l/100h
gesunken. Motor läuft weitere geschätzte 2.000h ohne Überholung.
Gesamtkosten: 660 EUR statt 5.000 EUR für Überholung.

### ANHANG B — Fallstudie: Volvo D2-40 mit Dieselpest

**Ausgangslage:**
- Jeanneau Sun Odyssey 40, Baujahr 2015, Volvo D2-40
- 800 Betriebsstunden, Boot überwintert in Kroatien (nicht genutzt)
- Problem: Motor startet, stirbt nach 5 Minuten ab. Ruckeln unter Last.

**Diagnose:**
- Kraftstoff-Vorfilter: braun-schwarzer Schleim im Schauglas
- Racor 320R Einsatz nach 30h komplett verstopft
- Tank-Inspektion (Endoskop): brauner Biofilm an Tankwänden
- Probenahme: Hormoconis resinae bestätigt

**Maßnahmen:**
1. Tank komplett entleert und gereinigt (Tankwäsche-Service, 450 EUR)
2. Racor-Einsatz + Motor-Feinfilter gewechselt (65 EUR)
3. Kraftstoffleitungen gespült (80 EUR)
4. Biozid-Behandlung: Grotamar 82 (100 ml/200 l Erstdosis)
5. Tank mit frischem EN 590 Diesel befüllt
6. Laufende Prävention: Grotamar 82 bei jeder Betankung (25 ml/200 l)
7. Regelmäßige Wasserabscheidung im Racor (monatlich)

**Ergebnis:** Motor läuft problemlos. Filter nach 250h: sauber.
Gesamtkosten: 750 EUR. Ohne Behandlung: Injektorschaden absehbar (4.000+ EUR).

### ANHANG C — Fallstudie: Volvo D3-170 Zahnriemenversäumnis

**Ausgangslage:**
- Hallberg-Rassy 37, Baujahr 2012, Volvo D3-170 (170 PS)
- 1.400 Betriebsstunden, Zahnriemen NICHT gewechselt (fällig bei 1.000h)
- Eigner war sich des Zahnriemen-Intervalls nicht bewusst
- Motor lief problemlos — bis er nicht mehr lief

**Schadensereignis:**
- Bei Hafenmanöver (Volllast rückwärts): lauter Knall, Motor steht
- Zahnriemen gerissen
- 4 von 5 Auslassventile verbogen
- 3 Kolben beschädigt (Eindellungen)
- Zylinderkopf irreparabel

**Reparatur:**
- Neuer Zylinderkopf (komplett): 4.200 EUR
- Neue Kolben (3 Stück): 1.800 EUR
- Neue Ventile (komplett): 900 EUR
- Neuer Zahnriemen + Rollen + Wasserpumpe: 550 EUR
- Dichtungssatz: 380 EUR
- Arbeit (Ausbau, Überholung, Einbau): 3.500 EUR
- **Gesamtkosten: 11.330 EUR**

**Vergleich:**
- Rechtzeitiger Zahnriemenwechsel: ~1.500 EUR
- Schaden durch Versäumnis: 11.330 EUR
- Faktor 7,5× teurer

**Lehre:** Zahnriemenwechsel am Volvo D3 ist NICHT optional.
Jeder D3-Eigner muss dieses Intervall kennen.

### ANHANG D — Fallstudie: Beta 43 — Impeller-Flügel im Wärmetauscher

**Ausgangslage:**
- Moody 425, Baujahr 2004, Beta 43 (43 PS)
- Impeller gewechselt (richtig), aber nicht alle Flügel gezählt
- 2 Flügel fehlten am alten Impeller

**Symptome (3 Wochen später):**
- Motortemperatur stieg langsam über Soll (85 → 92 → 98 °C)
- Wasseraustritt am Auspuff normal
- Alarm bei 105 °C, Motor abgestellt

**Diagnose:**
- Impeller neu und intakt
- Seeventil offen, Seiher sauber
- Wärmetauscher: 2 Neopren-Flügel im Rohrbündel gefunden!
- Flügel hatten ~30 % der Wärmetauscherfläche blockiert

**Maßnahme:**
- Wärmetauscher demontiert, gereinigt, Flügel entfernt (180 EUR Arbeit)
- Alternative (wenn nicht möglich): Wärmetauscher ersetzen (500–900 EUR)

**Lehre:** IMMER alle Flügel des alten Impellers zählen! Fehlende Flügel
müssen gesucht werden — sie verstopfen garantiert den Wärmetauscher.

### ANHANG E — Fallstudie: Nanni N4.50 — Überhitzung durch falsches Kühlmittel

**Ausgangslage:**
- Beneteau Oceanis 41, Baujahr 2016, Nanni N4.50
- Eigner hat Kühlmittel selbst gewechselt
- Versehentlich OAT-Kühlmittel zu bestehendem IAT-Kühlmittel gegeben

**Symptome (nach 2 Monaten):**
- Motortemperatur schwankend (75–95 °C)
- Kühlmittel trüb, geleeartige Klumpen im Ausgleichsbehälter
- Schließlich Überhitzungsalarm

**Diagnose:**
- Inkompatible Kühlmitteltypen (IAT + OAT) → Gelbildung
- Gel verstopfte Kühlkanäle im Motor und Wärmetauscher
- Thermostat verklebt

**Maßnahme:**
1. Kühlsystem komplett entleert (mühsam, Gel in allen Leitungen)
2. 3× mit Reiniger gespült (Prestone Flush)
3. Thermostat ersetzt (45 EUR)
4. Wärmetauscher professionell gereinigt (250 EUR Arbeit)
5. Korrekt mit OAT-Kühlmittel befüllt (50:50)

**Gesamtkosten:** 520 EUR + 4 Stunden Eigenarbeit

**Lehre:** NIEMALS verschiedene Kühlmitteltypen mischen.
Im Zweifel: System komplett spülen und mit einem Typ neu befüllen.

### ANHANG F — Fallstudie: Yanmar 4JH80 — Winterfrostschaden

**Ausgangslage:**
- Hanse 445, Baujahr 2013, Yanmar 4JH80 (80 PS)
- Boot im November an Land gestellt, Eigner hat kein Winterlager durchgeführt
- „Seeventil war ja geschlossen, reicht doch"
- Temperaturen im Januar: −12 °C

**Schadensbild:**
- Wärmetauscher geplatzt (Restwasser in der Seewasserseite gefroren)
- Auspuff-Nassmischer gerissen
- Seewasserleitungen geplatzt (3 Stück)
- Impeller-Pumpengehäuse gerissen

**Reparatur:**
- Wärmetauscher: 850 EUR
- Nassmischer: 380 EUR
- Seewasserleitungen + Schellen: 120 EUR
- Impeller-Pumpengehäuse: 280 EUR
- Arbeit: 650 EUR
- **Gesamtkosten: 2.280 EUR**

**Vergleich:**
- Propylenglyko-Frostschutz für Winterlager: 30 EUR + 30 Min. Arbeit
- Schadenskosten: 2.280 EUR
- Faktor 76× teurer

**Lehre:** Seewassersystem MUSS mit Frostschutz konserviert werden.
Seeventil schließen allein reicht NICHT — Restwasser in Motor,
Wärmetauscher und Leitungen gefriert.

### ANHANG G — Fallstudie: Volvo D1-30 — Motor springt nach Winter nicht an

**Ausgangslage:**
- Dehler 34, Baujahr 2018, Volvo D1-30 (30 PS)
- Winterlager korrekt durchgeführt
- Im April beim Frühjahrsstart: Motor springt nicht an

**Diagnose-Verlauf:**
1. Batterie: 12,8 V — OK
2. Anlasser dreht kräftig — OK
3. Kraftstoff: Racor-Schauglas leer (!) — kein Kraftstoff
4. Kraftstoffhahn: OFFEN — OK
5. Handpumpe betätigt: kein Widerstand
6. Kraftstoffleitung am Racor-Eingang gelöst: kein Kraftstoff
7. Tank geprüft: Tank voll (700 Liter)
8. Tank-Entnahmeleitung: verstopft!

**Ursache:** Paraffin-Ausscheidung im Diesel durch Kälte (Diesel ohne
Winteradditiv, Temperaturen −8 °C im Dezember). Paraffin hatte
Tank-Entnahmeleitung verstopft.

**Maßnahme:**
- Entnahmeleitung gespült (warmer Diesel)
- Racor + Feinfilter gewechselt
- System entlüftet
- Motor lief sofort

**Kosten:** 80 EUR (Filter) + 2 Stunden Arbeit

**Lehre:** Auch bei Winterlager an Diesel-Winterfestigkeit denken.
Winter-Diesel (EN 590 ab November) verwenden oder Fließverbesserer
(Liqui Moly Diesel Fließ-Fit) zugeben.

### ANHANG H — Fallstudie: Volvo D4-260 — Ölanalyse rettet Motor

**Ausgangslage:**
- Princess V42, Baujahr 2016, 2× Volvo D4-260 (260 PS)
- 1.200 Betriebsstunden, regelmäßige Wartung
- Eigner hat auf Empfehlung jährliche Ölanalyse begonnen

**Ölanalyse-Verlauf:**
| Parameter | Jahr 1 | Jahr 2 | Jahr 3 | Grenzwert |
|-----------|--------|--------|--------|-----------|
| Eisen (Fe) | 32 ppm | 38 ppm | 85 ppm | <50 ppm |
| Kupfer (Cu) | 12 ppm | 15 ppm | 42 ppm | <20 ppm |
| Blei (Pb) | 5 ppm | 8 ppm | 28 ppm | <15 ppm |
| Natrium (Na) | 8 ppm | 10 ppm | 12 ppm | <20 ppm |

**Auffälligkeit Jahr 3:** Sprunghafte Erhöhung von Eisen, Kupfer und Blei
auf dem Steuerbord-Motor. Backbord-Motor unauffällig.

**Diagnose:**
- Pleuellager Nr. 3 zeigt beginnendes Auswaschen
- Lagerschale: Blei-Zinn-Schicht partiell abgetragen
- Ursache: wahrscheinlich kurzzeitiger Ölmangel (Ölpumpen-Seiher teilweise verstopft)

**Maßnahme:**
- Ölwanne ab, Ölpumpen-Seiher gereinigt
- Pleuellager Nr. 3 erneuert (Lagerschalen: 180 EUR)
- Alle Hauptlager geprüft (OK)
- Ölwechsel mit Spülung
- **Gesamtkosten: 1.200 EUR**

**Ohne Ölanalyse:** Pleuellager wäre bei ~2.000h komplett ausgefallen →
Pleuelbruch → Motorblock durchgeschlagen → Totalschaden: 25.000–35.000 EUR

**Lehre:** Ölanalyse (35–50 EUR/Jahr) ist die günstigste Versicherung
für teure Motoren.

---
---

## 20. ANHANG I–R: Pydantic v2 Datenmodelle

### ANHANG I — MaintenanceInterval

```python
from pydantic import BaseModel, Field
from typing import Optional
from enum import Enum


class IntervalType(str, Enum):
    """Wartungsintervall-Typ."""
    FIRST_SERVICE = "first_service"         # Erstservice (50h)
    REGULAR_100 = "regular_100"             # 100h / jährlich
    REGULAR_250 = "regular_250"             # 250h / jährlich
    REGULAR_500 = "regular_500"             # 500h / 2 Jahre
    MAJOR_1000 = "major_1000"               # 1.000h / 4-5 Jahre
    OVERHAUL_2000 = "overhaul_2000"         # 2.000h / 8-10 Jahre


class MaintenanceInterval(BaseModel):
    """
    Wartungsintervall-Definition.
    Beschreibt ein Intervall mit Betriebsstunden und/oder Kalenderzeit.
    """
    model_config = {"from_attributes": True}

    interval_type: IntervalType = Field(
        ..., description="Typ des Wartungsintervalls"
    )
    hours: int = Field(
        ..., ge=0,
        description="Betriebsstunden-Intervall"
    )
    months: int = Field(
        ..., ge=0,
        description="Kalender-Intervall in Monaten"
    )
    description_de: str = Field(
        ..., description="Beschreibung in Deutsch"
    )
    tasks: list[str] = Field(
        default_factory=list,
        description="Liste der Wartungsaufgaben"
    )
    estimated_duration_hours: float = Field(
        ..., ge=0,
        description="Geschätzte Arbeitszeit in Stunden"
    )
    estimated_material_cost_eur: float = Field(
        ..., ge=0,
        description="Geschätzte Materialkosten in EUR"
    )
    estimated_labor_cost_eur: float = Field(
        ..., ge=0,
        description="Geschätzte Arbeitskosten in EUR"
    )
```

### ANHANG J — MaintenanceTask

```python
class TaskPriority(str, Enum):
    """Priorität einer Wartungsaufgabe."""
    CRITICAL = "critical"       # Muss gemacht werden, Motorschaden droht
    HIGH = "high"               # Sollte gemacht werden, Leistung/Zuverlässigkeit
    MEDIUM = "medium"           # Empfohlen, verlängert Lebensdauer
    LOW = "low"                 # Nice-to-have, Komfort/Optik


class TaskCategory(str, Enum):
    """Kategorie der Wartungsaufgabe."""
    OIL = "oil"                 # Motoröl und Filter
    FUEL = "fuel"               # Kraftstoffsystem
    COOLING = "cooling"         # Kühlsystem
    IMPELLER = "impeller"       # Seewasserpumpe
    BELT = "belt"               # Keil-/Zahnriemen
    VALVE = "valve"             # Ventiltrieb
    ANODE = "anode"             # Zinkanoden
    EXHAUST = "exhaust"         # Abgassystem
    ELECTRICAL = "electrical"   # Elektrik
    STRUCTURAL = "structural"   # Motorlager, Ausrichtung
    WINTERIZATION = "winterization"  # Winterlager
    GENERAL = "general"         # Allgemein


class MaintenanceTask(BaseModel):
    """
    Einzelne Wartungsaufgabe mit allen Details.
    """
    model_config = {"from_attributes": True}

    task_id: str = Field(..., description="Eindeutige Aufgaben-ID")
    name_de: str = Field(..., description="Aufgabenname in Deutsch")
    description_de: str = Field(..., description="Beschreibung in Deutsch")
    category: TaskCategory = Field(..., description="Aufgabenkategorie")
    priority: TaskPriority = Field(..., description="Priorität")

    interval_hours: Optional[int] = Field(
        None, ge=0,
        description="Intervall in Betriebsstunden"
    )
    interval_months: Optional[int] = Field(
        None, ge=0,
        description="Intervall in Kalendermonaten"
    )

    applicable_engines: list[str] = Field(
        default_factory=list,
        description="Liste der Motoren, für die die Aufgabe gilt"
    )

    parts_required: list[str] = Field(
        default_factory=list,
        description="Benötigte Ersatzteile (Teilenummern)"
    )
    tools_required: list[str] = Field(
        default_factory=list,
        description="Benötigtes Werkzeug"
    )
    estimated_duration_minutes: int = Field(
        ..., ge=0,
        description="Geschätzte Dauer in Minuten"
    )
    skill_level: str = Field(
        ..., description="Erforderliches Skill-Level: owner, experienced, professional"
    )

    procedure_steps: list[str] = Field(
        default_factory=list,
        description="Schrittweise Anleitung"
    )
    warnings: list[str] = Field(
        default_factory=list,
        description="Warnhinweise"
    )
    tips: list[str] = Field(
        default_factory=list,
        description="Tipps und Tricks"
    )
```

### ANHANG K — OilSpecification

```python
class OilBase(str, Enum):
    """Ölbasis-Typ."""
    MINERAL = "mineral"
    SEMI_SYNTHETIC = "semi_synthetic"
    FULL_SYNTHETIC = "full_synthetic"


class OilSpecification(BaseModel):
    """
    Motoröl-Spezifikation für einen bestimmten Motor.
    """
    model_config = {"from_attributes": True}

    engine_model: str = Field(..., description="Motor-Modell")
    manufacturer: str = Field(..., description="Motorhersteller")

    oil_base: OilBase = Field(..., description="Ölbasis")
    viscosity: str = Field(..., description="Viskositätsklasse (z.B. 15W-40)")
    api_class: str = Field(..., description="API-Klassifikation (z.B. CI-4, CK-4)")
    manufacturer_spec: Optional[str] = Field(
        None, description="Herstellerspezifikation (z.B. VDS-4.5)"
    )

    capacity_with_filter_liters: float = Field(
        ..., gt=0,
        description="Ölmenge mit Filter in Litern"
    )
    capacity_without_filter_liters: Optional[float] = Field(
        None, gt=0,
        description="Ölmenge ohne Filter in Litern"
    )

    change_interval_hours: int = Field(
        ..., ge=0,
        description="Wechselintervall in Betriebsstunden"
    )
    change_interval_months: int = Field(
        default=12,
        description="Wechselintervall in Monaten"
    )

    recommended_products: list[str] = Field(
        default_factory=list,
        description="Empfohlene Produkte"
    )

    genuine_filter_part_number: str = Field(
        ..., description="Original-Ölfilter-Teilenummer"
    )
    aftermarket_filter_options: list[str] = Field(
        default_factory=list,
        description="Aftermarket-Ölfilter-Alternativen"
    )
```

### ANHANG L — FuelFilterSpec

```python
class FilterStage(str, Enum):
    """Filterstufe."""
    PRIMARY = "primary"         # Vorfilter / Wasserabscheider
    SECONDARY = "secondary"     # Feinfilter am Motor


class FuelFilterSpec(BaseModel):
    """
    Kraftstofffilter-Spezifikation.
    """
    model_config = {"from_attributes": True}

    engine_model: str = Field(..., description="Motor-Modell")
    filter_stage: FilterStage = Field(..., description="Filterstufe")

    genuine_part_number: str = Field(
        ..., description="Original-Teilenummer"
    )
    filter_fineness_micron: float = Field(
        ..., gt=0,
        description="Filterfeinheit in Mikrometer"
    )
    has_water_separator: bool = Field(
        ..., description="Mit Wasserabscheider"
    )

    aftermarket_options: list[str] = Field(
        default_factory=list,
        description="Aftermarket-Alternativen mit Teilenummern"
    )

    change_interval_hours: int = Field(
        ..., ge=0,
        description="Wechselintervall in Betriebsstunden"
    )
    change_interval_months: int = Field(
        default=12,
        description="Wechselintervall in Monaten"
    )

    racor_compatible_model: Optional[str] = Field(
        None, description="Kompatibles Racor-Modell (wenn zutreffend)"
    )
    racor_element_number: Optional[str] = Field(
        None, description="Racor-Einsatz-Nummer"
    )
```

### ANHANG M — ImpellerSpec

```python
class ImpellerMaterial(str, Enum):
    """Impeller-Material."""
    NEOPRENE = "neoprene"
    NITRILE = "nitrile"
    POLYURETHANE = "polyurethane"
    EPDM = "epdm"


class ImpellerSpec(BaseModel):
    """
    Impeller-Spezifikation für einen bestimmten Motor.
    """
    model_config = {"from_attributes": True}

    engine_model: str = Field(..., description="Motor-Modell")
    pump_manufacturer: str = Field(
        ..., description="Pumpen-Hersteller (Jabsco, Johnson)"
    )
    pump_model: str = Field(..., description="Pumpen-Modell")

    genuine_impeller_number: str = Field(
        ..., description="Original-Impeller-Teilenummer des Motorherstellers"
    )
    pump_impeller_number: str = Field(
        ..., description="Impeller-Teilenummer des Pumpenherstellers"
    )

    material: ImpellerMaterial = Field(
        ..., description="Material"
    )
    blade_count: int = Field(
        ..., ge=1,
        description="Anzahl der Flügel"
    )
    flow_rate_lpm: float = Field(
        ..., gt=0,
        description="Förderrate in Litern pro Minute"
    )

    change_interval_hours: int = Field(
        ..., ge=0,
        description="Wechselintervall in Betriebsstunden"
    )
    service_kit_number: Optional[str] = Field(
        None, description="Service-Kit-Teilenummer (Impeller + Dichtung + Seal)"
    )
    overhaul_kit_number: Optional[str] = Field(
        None, description="Überholungs-Kit-Teilenummer (Komplett)"
    )
```

### ANHANG N — BeltSpec

```python
class BeltType(str, Enum):
    """Riementyp."""
    V_BELT = "v_belt"               # Klassischer Keilriemen
    NARROW_V = "narrow_v"           # Schmalkeilriemen (SPZ/SPA)
    COGGED_V = "cogged_v"           # Zahnkeilriemen
    POLY_V = "poly_v"              # Rippenriemen (Poly-V)
    TIMING = "timing"               # Zahnriemen (Steuerriemen)


class BeltSpec(BaseModel):
    """
    Riemen-Spezifikation (Keilriemen oder Zahnriemen).
    """
    model_config = {"from_attributes": True}

    engine_model: str = Field(..., description="Motor-Modell")
    belt_type: BeltType = Field(..., description="Riementyp")
    function: str = Field(
        ..., description="Funktion: alternator, coolant_pump, timing"
    )

    genuine_part_number: str = Field(
        ..., description="Original-Teilenummer"
    )
    profile: str = Field(
        ..., description="Profil (z.B. A, SPZ, SPA, 5PK, RPP)"
    )
    length_mm: Optional[int] = Field(
        None, gt=0,
        description="Länge in mm (wenn bekannt)"
    )
    aftermarket_equivalent: Optional[str] = Field(
        None, description="Aftermarket-Äquivalent (z.B. SPZ 950)"
    )

    change_interval_hours: int = Field(
        ..., ge=0,
        description="Wechselintervall in Betriebsstunden"
    )
    change_interval_months: Optional[int] = Field(
        None, ge=0,
        description="Wechselintervall in Monaten"
    )

    is_critical: bool = Field(
        default=False,
        description="Kritischer Riemen (Zahnriemen → Motorschaden bei Riss)"
    )
    failure_consequence: str = Field(
        ..., description="Folge bei Versagen (z.B. 'engine_damage', 'no_charging')"
    )

    tension_spec: Optional[str] = Field(
        None, description="Spannungsspezifikation (z.B. '10-15mm Durchbiegung')"
    )
    associated_parts: list[str] = Field(
        default_factory=list,
        description="Zusammen zu wechselnde Teile (z.B. Spannrolle)"
    )
```

### ANHANG O — CoolantSpec

```python
class CoolantType(str, Enum):
    """Kühlmitteltyp."""
    IAT = "iat"         # Inorganic Acid Technology
    OAT = "oat"         # Organic Acid Technology
    HOAT = "hoat"       # Hybrid
    SI_OAT = "si_oat"   # Silicated OAT


class CoolantSpec(BaseModel):
    """
    Kühlmittel-Spezifikation für einen bestimmten Motor.
    """
    model_config = {"from_attributes": True}

    engine_model: str = Field(..., description="Motor-Modell")
    coolant_type: CoolantType = Field(..., description="Kühlmitteltyp")
    specification: str = Field(
        ..., description="Spezifikation (z.B. ASTM D3306, Volvo VCS)"
    )

    total_capacity_liters: float = Field(
        ..., gt=0,
        description="Gesamtkapazität Kühlkreislauf 1 in Litern"
    )
    mixing_ratio_percent: int = Field(
        default=50,
        description="Konzentrat-Anteil in Prozent"
    )
    frost_protection_celsius: float = Field(
        ..., lt=0,
        description="Frostschutz bis (Grad Celsius)"
    )

    change_interval_hours: int = Field(
        ..., ge=0,
        description="Wechselintervall in Betriebsstunden"
    )
    change_interval_months: int = Field(
        default=24,
        description="Wechselintervall in Monaten"
    )

    genuine_product: Optional[str] = Field(
        None, description="Original-Kühlmittel des Herstellers"
    )
    compatible_products: list[str] = Field(
        default_factory=list,
        description="Kompatible Kühlmittel-Produkte"
    )
    incompatible_types: list[str] = Field(
        default_factory=list,
        description="NICHT kompatible Kühlmitteltypen"
    )
```

### ANHANG P — AnodeSpec

```python
class AnodeMaterial(str, Enum):
    """Anodenmaterial."""
    ZINC = "zinc"
    ALUMINUM = "aluminum"
    MAGNESIUM = "magnesium"


class AnodeLocation(str, Enum):
    """Anodenposition."""
    ENGINE_BLOCK = "engine_block"
    HEAT_EXCHANGER = "heat_exchanger"
    OIL_COOLER = "oil_cooler"
    INTERCOOLER = "intercooler"


class AnodeSpec(BaseModel):
    """
    Zinkanoden-Spezifikation am Motor.
    """
    model_config = {"from_attributes": True}

    engine_model: str = Field(..., description="Motor-Modell")
    location: AnodeLocation = Field(..., description="Position der Anode")
    material: AnodeMaterial = Field(
        default=AnodeMaterial.ZINC,
        description="Anodenmaterial"
    )

    genuine_part_number: str = Field(
        ..., description="Original-Teilenummer"
    )
    thread_size: str = Field(
        ..., description="Gewindegröße (z.B. M10×1,25, 1/4 NPT)"
    )
    length_mm: int = Field(
        ..., gt=0,
        description="Länge in mm"
    )
    diameter_mm: int = Field(
        ..., gt=0,
        description="Durchmesser in mm"
    )

    check_interval_hours: int = Field(
        default=250,
        description="Prüfintervall in Betriebsstunden"
    )
    replacement_threshold_percent: int = Field(
        default=50,
        description="Wechsel-Schwelle: Abtragung in Prozent"
    )
```

### ANHANG Q — WinterizationChecklist

```python
class WinterizationPhase(str, Enum):
    """Phase der Winterlager-Prozedur."""
    OIL_AND_FILTER = "oil_and_filter"
    FUEL_SYSTEM = "fuel_system"
    SEAWATER_SYSTEM = "seawater_system"
    FRESHWATER_COOLING = "freshwater_cooling"
    CYLINDER_FOGGING = "cylinder_fogging"
    EXHAUST_SYSTEM = "exhaust_system"
    BATTERY = "battery"
    GEARBOX = "gearbox"
    EXTERNAL = "external"


class ChecklistItem(BaseModel):
    """Einzelner Punkt der Winterlager-Checkliste."""
    model_config = {"from_attributes": True}

    item_id: str = Field(..., description="Eindeutige Item-ID")
    phase: WinterizationPhase = Field(..., description="Phase")
    description_de: str = Field(..., description="Beschreibung in Deutsch")
    is_completed: bool = Field(default=False, description="Erledigt")
    notes: Optional[str] = Field(None, description="Bemerkungen")
    is_critical: bool = Field(
        default=False,
        description="Kritischer Punkt (Unterlassung = Schaden)"
    )


class WinterizationChecklist(BaseModel):
    """
    Vollständige Winterlager-Checkliste für einen Motor.
    """
    model_config = {"from_attributes": True}

    engine_model: str = Field(..., description="Motor-Modell")
    engine_id: Optional[str] = Field(None, description="Motor-ID (wenn bekannt)")
    boat_name: Optional[str] = Field(None, description="Bootsname")
    date: str = Field(..., description="Datum (ISO 8601)")
    operating_hours: float = Field(
        ..., ge=0,
        description="Aktuelle Betriebsstunden"
    )

    items: list[ChecklistItem] = Field(
        default_factory=list,
        description="Checklisten-Punkte"
    )

    materials_used: dict[str, str] = Field(
        default_factory=dict,
        description="Verwendete Materialien (z.B. {'oil': 'Shell Rimula R4 L 15W-40'})"
    )
    total_material_cost_eur: Optional[float] = Field(
        None, ge=0,
        description="Gesamte Materialkosten in EUR"
    )
    total_labor_hours: Optional[float] = Field(
        None, ge=0,
        description="Gesamte Arbeitszeit in Stunden"
    )

    performed_by: str = Field(
        ..., description="Durchgeführt von (Name/Firma)"
    )
    is_complete: bool = Field(
        default=False,
        description="Gesamte Checkliste abgeschlossen"
    )

    confidence: str = Field(
        ..., description="Konfidenzstufe der Dokumentation"
    )
```

### ANHANG R — MaintenanceAnalysis (Orchestrierungs-Modell)

```python
class MaintenanceStatus(str, Enum):
    """Gesamtstatus der Motorwartung."""
    EXCELLENT = "excellent"     # Vorbildlich gewartet
    GOOD = "good"               # Gut gewartet, kleine Lücken
    FAIR = "fair"               # Akzeptabel, Verbesserungen nötig
    POOR = "poor"               # Mangelhaft, Schäden drohen
    CRITICAL = "critical"       # Kritisch, sofortige Maßnahmen nötig


class OverdueTask(BaseModel):
    """Überfällige Wartungsaufgabe."""
    model_config = {"from_attributes": True}

    task_name_de: str = Field(..., description="Aufgabenname")
    due_at_hours: int = Field(..., description="Fällig bei Betriebsstunden")
    current_hours: int = Field(..., description="Aktuelle Betriebsstunden")
    overdue_hours: int = Field(..., description="Überfällig um Stunden")
    due_at_date: Optional[str] = Field(None, description="Fällig am Datum")
    overdue_months: Optional[int] = Field(None, description="Überfällig um Monate")
    priority: TaskPriority = Field(..., description="Priorität")
    estimated_cost_eur: Optional[float] = Field(None, description="Geschätzte Kosten")


class MaintenanceAnalysis(BaseModel):
    """
    Orchestrierungs-Modell für die Wartungsanalyse eines Marine-Dieselmotors.
    Bewertet den Wartungszustand und identifiziert überfällige Aufgaben.
    """
    model_config = {"from_attributes": True}

    analysis_id: str = Field(..., description="Analyse-ID")
    engine_id: str = Field(..., description="Motor-ID")
    engine_model: str = Field(..., description="Motor-Modell")
    boat_id: Optional[str] = Field(None, description="Boot-ID")
    analysis_date: str = Field(..., description="Analysedatum (ISO 8601)")
    analysis_level: str = Field(
        ..., description="Analyselevel: quick (Level 1) oder professional (Level 2)"
    )
    current_operating_hours: float = Field(
        ..., ge=0,
        description="Aktuelle Betriebsstunden"
    )

    # Wartungsstatus
    overall_status: MaintenanceStatus = Field(
        ..., description="Gesamtstatus der Wartung"
    )
    maintenance_score: float = Field(
        ..., ge=0, le=100,
        description="Wartungs-Score (0–100)"
    )

    # Überfällige Aufgaben
    overdue_tasks: list[OverdueTask] = Field(
        default_factory=list,
        description="Liste überfälliger Wartungsaufgaben"
    )
    upcoming_tasks: list[str] = Field(
        default_factory=list,
        description="Bald fällige Aufgaben (nächste 50h)"
    )

    # Spezifische Bewertungen
    oil_condition_score: Optional[float] = Field(
        None, ge=0, le=100,
        description="Ölzustand-Bewertung (0–100)"
    )
    cooling_condition_score: Optional[float] = Field(
        None, ge=0, le=100,
        description="Kühlsystem-Bewertung (0–100)"
    )
    fuel_system_score: Optional[float] = Field(
        None, ge=0, le=100,
        description="Kraftstoffsystem-Bewertung (0–100)"
    )
    belt_condition_score: Optional[float] = Field(
        None, ge=0, le=100,
        description="Riemen-Bewertung (0–100)"
    )
    anode_condition_score: Optional[float] = Field(
        None, ge=0, le=100,
        description="Anoden-Bewertung (0–100)"
    )

    # Winterlager
    winterization_status: Optional[str] = Field(
        None, description="Winterlager-Status: completed, partial, not_done, not_applicable"
    )
    winterization_checklist: Optional[WinterizationChecklist] = Field(
        None, description="Winterlager-Checkliste (wenn verfügbar)"
    )

    # Kostenprognose
    estimated_immediate_cost_eur: float = Field(
        ..., ge=0,
        description="Sofortige Kosten für überfällige Maßnahmen"
    )
    estimated_annual_cost_eur: float = Field(
        ..., ge=0,
        description="Geschätzte jährliche Wartungskosten"
    )
    estimated_5year_cost_eur: float = Field(
        ..., ge=0,
        description="Geschätzte 5-Jahres-Wartungskosten"
    )

    # Zusammenfassung
    summary_de: str = Field(
        ..., description="Zusammenfassung in Deutsch"
    )
    critical_findings: list[str] = Field(
        default_factory=list,
        description="Kritische Befunde"
    )
    recommendations: list[str] = Field(
        default_factory=list,
        description="Empfehlungen"
    )
    warnings: list[str] = Field(
        default_factory=list,
        description="Warnungen"
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
