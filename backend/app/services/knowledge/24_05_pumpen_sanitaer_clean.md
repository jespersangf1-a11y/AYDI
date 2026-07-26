---
title: "Pumpen Sanitär — Komplettleitfaden"
category: "24_Sanitär"
subcategory: "Pumpen_Sanitär"
keywords: ["Druckwasserpumpe", "Membranpumpe", "Macerator", "Bilgepumpe", "Impeller", "Sumpfpumpe", "Fäkalienpumpe"]
confidence_level: "measured"
boat_classes: ["Kleinboot", "Fahrtenyacht", "Blauwasseryacht", "Megayacht"]
---

# 24.5 Pumpen Sanitär — Komplettleitfaden

## 1. Einführung und Relevanz

### 1.1 Überblick Marine-Pumpensysteme

Marine-Pumpensysteme sind das Nervensystem jeder Yacht mit Sanitäranlage. Sie verbinden Wassertanks mit Verbrauchsstellen, fördern Bilgewasser, bewältigen Fäkalien und ermöglichen Druckwasserversorgung in Küche und Bad — oft unter den herausforderndsten Bedingungen: Vibrationen, Salzwasser, Temperaturwechsel, Fehltriebe bei leeren Tanks.

**Kritikalität nach Schiffsgröße:**

| Schiffklasse | Minimale Pumpanforderung | Kritikalität |
|---|---|---|
| Kleinboot < 8m | Frischwasser (manuell), Bilge | Mittel — manuelles Backup Standard |
| Fahrtenyacht 8–14m | Druckwasser, Fäkalien, Bilge (redundant) | Hoch — Ausfallicherheit = Komfort + Sicherheit |
| Blauwasseryacht 15–24m | Redundante Systeme pro Funktion, Sumpf | Kritisch — Ausfallicherheit = Überlebenssicherheit |
| Megayacht > 24m | 2–3 unabhängige Systeme pro Kreislauf | Kritisch — zentrale Systemüberwachung erforderlich |

### 1.2 Funktionale Anforderungen

Jede Yacht benötigt mindestens vier isolierte Pumpensysteme:

1. **Frischwasserdruck** — bedarfsgerechte Druckversorgung (2–3 bar) für Duschen, Waschbecken, Küche
2. **Bilgepumpe(n)** — Entfernung von Leckagewasser, Kondenswasser, Verschüttungen
3. **Fäkalienpumpe/Macerator** — Bord-WC-Entwässerung mit oder ohne Zerhackerung
4. **Zusatzsysteme** — Dusch-Sumpfpumpe (wenn Bilge nicht erreichbar), Deckwäsche, Ankerwinde, Heiz-/Kühlwasser (Motor)

### 1.3 Typische Ausfallmuster und Konsequenzen

| Komponente | Ausfallursache | Konsequenz | Häufigkeit |
|---|---|---|---|
| Druckschalter | Verschlammung, Korrosion | Keine Wasserzirkulation | 8 % p.a. |
| Membran/Kolben | Verschleiß, Salzablagerung, Frost | Dauerlauf, Stromverschleiß | 12 % p.a. |
| Saugventil | Verstopfung, Verschmutzung | Kein Selbstanlauf, Lufteinzug | 6 % p.a. |
| Impeller | Verschleiß, Verhärtung (UV) | Leistungsabfall auf 40–50 % | 15 % p.a. (4–5 Jahre Lebensdauer) |
| Elektro-Motor | Verschleiß, Wicklungsschaden | Totalausfall | 4 % p.a. |
| Anlaufkondensator | Austrocknung, Überspannung | Motor startet nicht (aber summt) | 10 % p.a. |

**Fazit:** Jede Yacht sollte für Bilge und Fäkalien eine zweite (gleich dimensionierte) Pumpe an Bord haben — mit unabhängiger Stromversorgung. Druckwassersysteme sollten einen manuellen Bypass oder eine Handpumpe haben.

---

## 2. Grundlagen und Funktionsprinzipien

### 2.1 Membran-/Kolbenpumpen (Druckunterdruckprinzipien)

**Funktionsprinzip:**
Eine elastische Membran oder ein Kolben wird durch einen Exzenter oder eine Schubstange periodisch vor- und zurückbewegt. In der Saughub wird Unterdruck erzeugt (Saugventil öffnet), in der Druckhub wird Druck aufgebaut (Druckventil öffnet).

**Bauarten:**

- **Doppelmembranpumpe (Diaphragm Pump):** Zwei gegenläufig arbeitende Membranen, pneumatisch angetrieben (druckluft). Marine selten, eher für Spezialanwendungen (Fäkalien, Schlick).
  
- **Drehschieber-Pumpe:** Exzenter mit Schieber in Zylinder. Typisch: Jabsco Par-Max, ältere Frischwassersysteme.
  
- **Rollkolben-Pumpe (Rotating Vane):** Exzentrisch eingebauter Kolben mit Führungsnut. Standard für 12V/24V Yacht-Druckwasserpumpen.
  
- **Kolbenpumpe (Piston/Plunger):** Axiales Design, höhere Drücke (50+ bar), seltener in Yachten (eher Industrie).

**Charakteristiken:**
- Selbstansaugend bis ~1 m Saughöhe (mit Rückschlagventilen)
- Druckabhängiger Durchfluss (bei Druckaufbau sinkt Durchfluss)
- Typische Drücke: 2–4 bar (Frischwasser), 6–8 bar (Spülung, Druckabschlag möglich)
- Geräusche: 70–80 dB bei Betrieb, pulsierend

**Lebensdauer:** 2000–5000 Betriebsstunden, dann Dichtsatz tauschen. Salzwasser/Brackwasser: deutlich kürzer ohne zusätzliche Filterung.

### 2.2 Impeller-Pumpen (Zentrifugal mit Fremdimpeller)

**Funktionsprinzip:**
Ein Laufrad (Impeller) mit meist 4–6 gummierten Flügeln sitzt exzentrisch in einem Spiralgehäuse. Während der Umdrehung vergrößert sich der Raum auf der Saugseite (Unterdruck), verkleinert sich auf der Druckseite (Druck). Das Gummiaterial fungiert als eigendichtendes Element.

**Bauarten:**
- **Neopren-Impeller:** Grün, standard in Bilgepumpen. Hart, verschleißfest, aber nicht für trockenes Laufen.
- **Nitrile-Impeller:** Gelb/orange, für aggressive Medien (Bilge-Schlick).
- **Buna-N Impeller:** Schwarz, Standard-Backup, geringfügig weniger Verschleißfestigkeit.

**Charakteristiken:**
- Nicht selbstansaugend (Impeller muss vorprimed sein)
- Großer Durchfluss, niedriger Druck typisch: 40–100 L/min @ 0,5–2 bar
- Läuft nur bei ~1000–3500 U/min, daher Motor-Durchsatz abhängig
- Läuft schlecht trocken (Impeller verhärtet/zerreißt)
- Geräusche: 65–75 dB, rauer/knirschender

**Lebensdauer:** 500–1500 Betriebsstunden Impeller, dann tauschen (~€20–60). Motor-Lagerschäden bei Trockenlauf.

**Häufiger Fehler:** Impeller sitzt falsch und wirkt in falsche Richtung → Null-Förderung.

### 2.3 Zentrifugal-Pumpen (Hochleistungs-Impeller, Schifffahrt)

**Funktionsprinzip:**
Großes, mehrflügeliges Laufrad erzeugt Zentrifugalkräfte. Häufig mehrstufig (Serienschaltung von Rädern) für höhere Drücke.

**Einsatz auf Yachten:**
- Kühlwasser-Umwälzung für Dieselmotoren
- Hydrodynamische Stabilisierungssysteme (große Yachten)
- Riesel-Feuerlösch-Systeme (> 24m)

**Charakteristiken:**
- Großer Durchfluss, hohe Drücke möglich (bis 8 bar bei mehrstufig)
- Keine Selbstansaugung
- Druckunabhängig (Durchfluss relativ konstant über Druckbereich)
- Leise (50–65 dB)

**Lebensdauer:** 5000–10000 Betriebsstunden, robuster als Impeller.

### 2.4 Macerator-Pumpen (Fäkalien-Zerhacker)

**Funktionsprinzip:**
Kombination aus:
1. **Rotierend-Messer-Einheit** (oben im Tank/WC): Zerhackt Feststoffe zu Brei
2. **Impeller-Pumpe** (unten): Fördert das Gemisch überboard oder in Tank

Alternativ: Direkt-Messer-Design, wo Messer im Pumpensaugrohr sitzt.

**Anforderungen nach CE-Kategorie:**

| CE-Kat | Erforderung | Bemerkung |
|---|---|---|
| A (Ocean) | Macerator verboten | Schließsystem erforderlich, manuell oder Sammeltank |
| B (Offshore) | Macerator zulässig bei geschlossener WC-Seite | Auslasshahn erforderlich |
| C (Inshore) | Macerator Standard | Weniger streng |
| D (Sheltered) | Macerator ohne weitere Auflage | Standard |

**Typische Modelle:**
- **Jabsco 18590** (ParMax-Macerator): 18 A @ 24V, 30 L/min @ 3 bar, 2500 U/min
- **Whale Gulper 320 ACE:** 24 A @ 24V, 40 L/min, automatische Saugsequenz
- **ShinMaywa HMS-2300:** 25 A @ 24V, 45 L/min, sehr häufig in DE/Skandinavien

**Lebensdauer:** 2000–4000 Betriebsstunden, dann Messersatz (~€80–150) und Dichtungen.

### 2.5 Bilge-Pumpen

**Einteilung:**

1. **Submersible (Tauch-)Pumpen:**
   - Motorisiert, sitzen direkt im Bilgewasser
   - Vorteil: Automatischer Aufschwimm-Schalter möglich
   - Nachteil: Motor kann korrodieren, schwer zu reparieren
   - Typisch: 12–24V DC, 40–100 L/min

2. **Zentrifugal-Impeller (In-line):**
   - Motor sitzt separat, Pumpe im Saugkreislauf
   - Vorteil: Motor bleibt trocken, einfach zu warten
   - Nachteil: Braucht Priming, Vibration möglich
   - Typisch: 12–24V DC, 60–150 L/min

3. **Doppel-Membran (Akkordeon-Pumpe):**
   - Seltener auf Yachten
   - Vorteil: Sehr robust, selbstansaugend
   - Nachteil: Größer, lauter
   - Typisch: 12–24V DC, 30–70 L/min

**Standard auf Fahrtenyachten:** Zwei Impeller-Pumpen oder eine große + eine kleine manuelle Handbilge.

### 2.6 Hand-Pumpen (Backup)

**Typen:**

- **Bilge-Handbilge:** Kolben-Handpumpe, ~1–2 L/Hub à 40 U/min = 40–80 L/min
  
- **Druckwasser-Handbilge:** Mit Druckschalter, weniger häufig (eher ältere Yachten)
  
- **Fäkalien-Handbilge:** Sperrventile, für Notfallentleerung von Sammeltank, sehr selten

**Wartung:** Jährlich prüfen, Dichtungen schmieren, Ventilkugeln prüfen auf Verschleiß.

### 2.7 Druckschalter und Akkumulator-Tank

**Druckschalter (Pressure Switch):**
- Bimetall oder elektronisch
- Typisch: Schließt bei 1,2 bar (Pumpenstart), öffnet bei 3,0 bar (Pumpe aus)
- Hysterese verhindert Dauerpulsation
- Häufiger Ausfallmechanismus: Verschlammung durch Rostpartikel

**Akkumulator-Tank (Druckbehälter):**
- Kleine Stahlflasche (0,5–2 L) mit Membran oder Blasebalg
- Einer Seite Wasser, andere Seite Luft (0,8–0,9 bar Vordruck)
- Reduziert Pumpenzyklenzahl: Speichert Druck zwischen Schalterzyklen
- Verhindert Druckschwankungen (Komfort beim Duschen)
- Standard auf allen Frischwasser-Drucksystemen > 8m

**Lebensdauer:** 5–8 Jahre, dann Luft-Membran verschlissen → Tank "weich", Pump läuft zu oft.

### 2.8 Selbstansaugung und Vorpriming

**Selbstansaugung erforderlich für:**
- Frischwasser-Druckpumpen (sonst manuell füllen)
- Bilge-Pumpen (müssen auch bei leerem Sumpf nicht austrocknen)

**Mechanismen:**
1. **Großes Saugventil (Rückschlag):** Verhindert Rückfluss während Stillstand
2. **Saugfilter mit Rückspülkammer:** Speichert Wasser in Saugline
3. **Priming-Taste (manuell):** Lufttaschen manuell ausblasen
4. **Luftventil oben im Tank:** Verhindert Vakuum beim Saugen

**Probleme ohne ordnungsgemäße Selbstansaugung:**
- Pumpe "Luft schlagend" = Kavitation
- Dauer > 5 min bis Wasser kommt (Passagiere werden ungeduldig)
- Risiko: Luft in Leitungen blockiert Wasserzirkulation

### 2.9 Durchfluss vs. Druckcharakteristik

Jede Pumpe hat eine Pump-Kennlinie: Durchfluss (L/min) vs. Gesamtdruck.

**Typische Kurvenformen:**

| Pumpentyp | Kurvenform | Praktische Implikation |
|---|---|---|
| Impeller (Bilge) | Stark fallend: 100 L/min @ 0 bar → 20 L/min @ 2 bar | Druckaufbau (z.B. durch Schlauch-Engpass) reduziert Förderung massiv |
| Membran (Frischwasser) | Schwach fallend: 25 L/min @ 0 bar → 18 L/min @ 4 bar | Druckabhängig, aber stabiler |
| Zentrifugal (Motor) | Flach: 80 L/min @ 0 bar → 75 L/min @ 3 bar | Druckunabhängig, für Umwälzung ideal |

**Designfolgerung:** Bilge-Pumpe braucht kurze, weite Rohre (< 1 m Rückstaudruck), Frischwasser-Druckpumpe kann höhere Gegendrücke verkraften.

### 2.10 Duty Cycle und thermische Belastung

**Duty Cycle = Anteil Betriebszeit in 10 min Zyklus**

| Pumpentyp | Typischer Duty | Max. Betriebstemperatur |
|---|---|---|
| Druckwasser (mit Schalter) | 5–15 % | 60 °C Wasser OK |
| Bilge (passiv) | 5–30 % (je nach Leckrate) | Motor bis 120 °C OK |
| Bilge (aktiv/permanent) | 80–100 % | Motor muss für 100 % ausgelegt sein |
| Macerator (Notfall) | 100 % möglich | 3–5 min max, sonst Motor überhitzt |

**Kritisches Szenario:** Großes Leck, Bilge läuft ständig, Motor wird zu heiß, Wicklung carbonisiert.
→ Bilge-Motoren auf Blauwasseryachten sollten temperaturgeschützt sein oder mit Thermoschutzschalter.

---

## 3. Typenübersicht und Klassifikation

### 3.1 Frischwasser-Druckpumpen (Haushaltsversorgung)

**Anforderungen nach Bootsgröße:**

| Größe | Druckpumpe Standard | Flow @ Druck | Tank | Akkumulator |
|---|---|---|---|---|
| < 8m | Manuelle Handbilge | — | < 50 L | Optional |
| 8–12m | Jabsco Par-Max 1.5 oder Whale GP | 15–18 L/min @ 2,5 bar | 50–100 L | Obligatorisch |
| 12–18m | Flojet Quad oder Shurflo Aqua King | 20–30 L/min @ 3 bar | 100–200 L | Obligatorisch |
| 18–24m | Größere Mehrfach-Schaltung oder Zentrifugal | 40–60 L/min @ 2–3 bar | 200–500 L | Obligatorisch |
| > 24m | Zentrifugal-Hauptsystem + Backup-Druck | 100+ L/min | 500–2000 L | Obligatorisch |

**Dimensionierung-Formel (rough):**
- Dusche 1 Person: 10 L/min @ 2,5 bar
- Waschbecken: 5 L/min @ 1,5 bar
- Küche: 8–12 L/min @ 2 bar
- Gesamt-Simultankopfanlast: Dusche + Waschbecken = ~15 L/min empfohlen

**Leitung und Schläuche:**
- Frischwasser: Lebensmittelqualität, nicht toxisch, Schlauchgröße ≥ 10 mm ID (innerer Durchmesser)
- Metall-Rohre: nur oberhalb Wasserlinie (Korrosionsrisiko)
- Durchflussgeschwindigkeit max. 1–1,5 m/s (2–4 bar Druckaufbau verhindert)

### 3.2 Bilge-Pumpen (Wasserableitung)

**Strategien nach Bootstyp:**

| Bootstyp | Bilanzmodus | Redundanz | Typische Pump-Kette |
|---|---|---|---|
| Kleinboot Kunststoff | Passiv (selten Wasser) | Manuelle Handbilge | Oder: 12V Submersible als Backup |
| Fahrtenyacht Holz | Aktiv (periodisches Pumpen) | 1–2 elektrisch + 1 manuell | Impeller 12V @ 60 L/min + Handbilge |
| Blauwasseryacht GFK | Aktiv (Sicherheit) | 2 × elektrisch (unabhängig) + 1 manuell | Doppel-Impeller-Schaltung, jede mit eigenem Schalter |
| Megayacht Aluminium | Hochautomatisiert | 3+ Pumpen, nivelliert | Zentrifugal-Hauptsystem + 2 × Backup-Impeller |

**Bilge-Sumpf-Design:**
- Sammeltank mindestens 30–50 L (nicht zu klein, sonst ständig pumpend)
- Schiffe > 12m sollten mehrere Sumpfbereiche haben (Bug, Mitte, Heck separat), je mit eigenem Aufschwimmer
- Saugfilter in Sumpf (200–500 µm, verhindert Blockade von Muscheln, Algen)
- Rückschlagventil vor jeder Pumpeneinheit

### 3.3 Fäkalien-Pumpen und Macerator-Systeme

**Vier Strategien:**

| Strategie | Mechanik | Vorteile | Nachteile | CE-Kat. |
|---|---|---|---|---|
| **Direktes Überboard** | Macerator, sofortige Ableitung | Kleinster Tank, wartungsarm | Umweltkonsequenzen, schwer reversibel | D, teilw. C |
| **Sammeltank + Macerator** | WC → Grube, Macerator @ Grube | Kontrolle, Umweltschutz, Grey-Water-Option | Größerer Tank, Geruchsrisiko | A, B, C |
| **Manuelle Tauchpumpe** | Handpumpe mit Sperrventilen | Maximale Kontrolle, robustes Backup | Arbeit, Hygienerisiko | A, B |
| **Vakuum-Toilette** | WC mit Vakuum-Saugleitung, zentrale Pumpstation | Geruchsfrei, platzsparend | Hohe Kosten, komplexe Elektrik | A, B |

**Standardanlage für Fahrtenyacht (8–14m):**
```
WC-Schüssel → Dreiweg-Ventil → 
  ↓ Macerator (Überboard bei Fahrt) 
  ↓ Sammeltank (Hafen/Ankerbucht)
```

Dimenson Sammeltank: ~20–40 L für 2–4 Personen und 2–3 Tage Fahrt (1–2 L pro Person pro Tag + Toilettenspülung).

### 3.4 Dusch-Sumpf-Pumpen

**Erfordernis:** Duschkabine sitzt über Bilgesumpf, Wasser läuft zu schnell, oder: separate Dusch-Sumpfpumpe erforderlich.

**Installationsmodus:**

```
Dusche → Sumpf-Grube (5–10 L)
  ↓ Schwimmschalter @ 50 % Füllung
  ↓ Submersible Impeller-Pumpe 12V/24V @ 30–50 L/min
  ↓ Überboard oder in Bilge-Hauptsystem
```

**Häufiger Fehler:** Sumpf sitzt unterhalb Wasserlinie, Rückschlagventil vergessen → Wasser läuft nach Duschen in Bilge zurück.

### 3.5 Deckwäsche-Systeme

**Druckerfordernis:** 3–5 bar für anständige Strahlkraft.

**Kleine Yachten (< 10m):** 
- Manuelles Spray-Schlauch-System mit Drucktank oder Elektropumpe
- Durchfluss: 10–15 L/min ausreichend

**Mittlere Yachten (10–18m):**
- Elektro-Druckpumpe (Membran oder Zentrifugal) mit Druckschalter
- Durchfluss: 20–30 L/min
- Leitungsführung: Oberseite Reling, separate Schläuche

**Große Yachten (> 18m):**
- Zentrifugal-Hauptsystem mit Deckwäsche-Nebenschaltung
- Durchfluss: 40–80 L/min möglich
- High-Pressure-Variante: eigene kleine 12/24V Druckpumpe für lokale Deckwäsche

### 3.6 Motor-Kühlwasser-Pumpen (Diesel/Benzin)

Nicht primär im Sanitär-Kontext, aber Systeminterdependenz:

**Zentrifugal-Standard:**
- Integral im Motor oder separat
- Durchfluss: 40–80 L/min je nach Leistung
- Druck: 0,5–2 bar
- Laut: 60–70 dB

**Ausfallfolge:** Motor läuft heiß, Überhitzungsschutz triggert, Fahrt unmöglich.

**Backup-Strategie:** Mehrstufige Kühlwasserpumpe mit Bypass oder Handkurbel-Notbetrieb (sehr selten).

### 3.7 Vergleichstabelle: Alle Pumpentypen

| Merkmal | Membran | Impeller | Zentrifugal | Macerator | Hand-Bilge |
|---|---|---|---|---|---|
| **Druck (bar)** | 2–6 | 0,5–2 | 1–5 | 2–4 | 0,5–1 |
| **Durchfluss (L/min)** | 15–35 | 40–150 | 50–200 | 20–50 | 40–80 (bei 40 U/min) |
| **Selbstansaugung** | Ja (bis ~1 m) | Nein | Nein | Ja (Messer) | Ja (Kolben) |
| **Geräusch (dB)** | 75–80 | 65–75 | 55–65 | 80–85 | 70–75 |
| **Lebensdauer (h)** | 2000–5000 | 500–1500 | 5000–10000 | 2000–4000 | 10000+ |
| **Wartungsintensität** | Mittel | Hoch (Impeller) | Niedrig | Hoch (Messer) | Niedrig |
| **Stromaufnahme (A @ 24V)** | 10–20 | 15–30 | 20–40 | 20–30 | — |
| **Kosten (EUR, neue Pumpe)** | €200–400 | €150–350 | €300–600 | €400–800 | €100–200 |

---

## 4. Produktlinien und Spezifikationen

### 4.1 Jabsco/Xylem — Par-Max und Druckwasser-Serie

**Xylem-Jabsco ist Marktführer für Yachtpumpen seit 40+ Jahren. Alle folgenden Modelle sind Standard-Installationen.**

#### Par-Max Druckwasser-Serie

**Par-Max 1.5 (12V) — Einsteigerklasse**
- Motor: 12V DC brushless
- Stromaufnahme: 12–13 A @ 12V (Dauerlast)
- Durchfluss: 15 L/min @ 2,5 bar; 18 L/min @ 1,5 bar
- Druck: max. 4,0 bar, Schaltbereich typisch 1,2–3,0 bar
- Selbstansaugung: ja, bis ~1 m
- Geräusch: 72 dB
- Anschlüsse: 10 mm Schläuche (barbed fittings)
- Preis: €240–300
- Lebensdauer: 3000–4000 h
- Besonderheit: Wartungsarm, Dichtsatz tauschbar (€50–80)
- **Typische Yacht-Anwendung:** 8–12m Segler, einfache Ausrüstung

**Par-Max 3 (12V/24V) — Mittlere Klasse**
- 24V-Variante verfügbar (besser für größere Boote, weniger Stromverlust in langen Leitungen)
- Durchfluss: 20 L/min @ 2,5 bar (24V), 12 L/min @ 2,5 bar (12V)
- Druck: max. 4,5 bar
- Stromaufnahme: 9–10 A @ 24V (besser als 12V-Variante)
- Preis: €280–380 (24V Premium)
- **Empfehlung:** Für Boote 12–18m, falls 24V-Bordnetz vorhanden, sonst Par-Max 1.5

**Par-Max 5 (24V) — Großboot**
- Durchfluss: 25–28 L/min @ 2,5 bar
- Druck: max. 5,5 bar
- Stromaufnahme: 14–16 A @ 24V
- Preis: €380–480
- **Anwendung:** 18–24m Mega-Familie, mehrere Badezimmer

#### Par-Max Bilge-Serie

**Par-Max Bilge 1 (12V/24V) — Kleine Impeller-Bilge**
- **12V-Variante:** 55 L/min @ 0 bar, 25 L/min @ 2 bar
- **24V-Variante:** 75 L/min @ 0 bar, 35 L/min @ 2 bar
- Stromaufnahme: 18–20 A @ 12V, 12–14 A @ 24V
- Geräusch: 68 dB (impeller-typisch)
- Anschlüsse: 16 mm ID Schläuche
- Preis: €200–280
- **Problem:** Impeller-Verschleiß, alle 500–700 h Austausch (~€40 Ersatz-Impeller)
- **Häufigste Fehler:** Trocken gelaufen (Impeller verhärtet), falsch gepolt (läuft rückwärts)

**Par-Max Macerator 18590 (24V) — Standard Fäkalien-Macerator**
- Durchfluss: 30 L/min @ 3 bar
- Stromaufnahme: 18 A @ 24V
- Messerwerk: rostfreier Stahl, dreistufig
- Betriebstemperatur: bis 50 °C (Warm-Spülung möglich)
- Geräusch: 85 dB (laut, normal für Macerator)
- Anschlüsse: Saugstutzen oben (Dreiweg-Ventil), Druck unten (16 mm Schlauch)
- Preis: €580–720
- **Wartung:** Messersatz nach 2500–3000 h (~€120), Dichtungen Wartungskit (€40)
- **Bekanntes Problem:** Spielzeug/Zahnseide verstopft Messerspalt → regelmäßige Spülzyklen nötig
- **Installation:** Immer mit separatem Druckschalter (nicht im Gerät integriert auf ältesten Modellen)

#### Jabsco Toilet-Serie (kombiniert WC-Spülung + Absaugung)

**Jabsco Matey WC (12V/24V) — Elektrisches Bordklo mit integr. Pumpe**
- **Spülung:** 0,5 L pro Spülzyklus (Meerwasser oder Frischwasser, schaltbar)
- **Absaugung:** 6–8 L/min @ 2 bar, manuell oder automatisch
- Stromaufnahme (Spülung): 5 A kurz, (Absaugung): 12 A kontinuierlich
- Material: High-Density Polyethylen (robust gegen Salzwasser-Spray)
- Preis: €450–600
- **Einsatz:** Kleine bis mittlere Yachten, 6–15m, oft für Charter-Boote bevorzugt (wartungsarm)
- **Betrieb:** Frischwasser-Spülung bei Fahrt (Meerwasser bei Anker), reduziert Frischwasserbedarf

---

### 4.2 Whale Pumps — Spezialist für Bilge und Druckwasser

**Whale ist britischer Hersteller, bekannt für Zuverlässigkeit und Ersatzteil-Verfügbarkeit. Stark in Deutschland.**

#### Whale GP Serie (Druckwasser)

**Whale GP0325 (12V) — Kompakt-Druckpumpe**
- Durchfluss: 16 L/min @ 2,5 bar
- Druck: max. 4,0 bar
- Stromaufnahme: 11 A @ 12V
- Selbstansaugung: ja, zuverlässig
- Geräusch: 70 dB
- Anschlüsse: 9–10 mm Schläuche (kleinere Bauform als Jabsco)
- Preis: €220–300
- **Vorteil vs. Jabsco:** leiser, kompakter, weniger Stromverbrauch
- **Nachteil:** weniger verbreitet in Deutschland, Ersatzteilbeschaffung schwieriger

**Whale GP0450 (12V/24V) — Mittlere Druckpumpe**
- 12V: 20 L/min @ 2,5 bar, 18 A
- 24V: 22 L/min @ 2,5 bar, 10 A
- Druck: max. 5,5 bar
- Preis: €280–380
- **Häufig eingebaut:** Segelyachten 10–16m

#### Whale Gulper Serie (Bilge/Greywater)

**Whale Gulper 220 (12V) — Standard-Impeller-Bilge**
- Durchfluss: 65 L/min @ 0 bar
- Stromaufnahme: 16–18 A
- Geräusch: 68 dB
- Impeller: Neopren, wartungsfreundlich zugänglich
- Preis: €200–250
- **Installation:** sehr beliebt in UK/Skandinavien, weniger in Deutschland

**Whale Gulper 320 ACE (24V) — Intelligente Bilge mit Auto-Priming**
- "ACE" = Automatische Cycle-Elektronik
- Durchfluss: 40 L/min @ 0 bar, 18 L/min @ 2 bar (Saugvorbereitung)
- Stromaufnahme: 24 A @ 24V
- Besonderheit: Automatische Saugsequenz beim Start (verhindert Luftblocken)
- Preis: €350–450
- **Vorteil:** Langzeitzuverlässigkeit, reduziert Wartung
- **Nachteil:** Teurer, benötigt 24V-Bordnetz

#### Whale Waste-Macerator Serie

**Whale WM3 (24V) — kompakte Fäkalien-Macerator**
- Durchfluss: 25 L/min @ 3 bar
- Stromaufnahme: 16 A @ 24V
- Messwerk: 4-flügeliges Messer-Design
- Geräusch: 82 dB
- Preis: €520–650
- **Konkurrenz zu Jabsco 18590:** ähnliche Leistung, alternative Hersteller-Quelle

---

### 4.3 Shurflo — Spezialist für Druckwasser und dezentrale Systeme

**Shurflo ist US-Hersteller, bekannt für Trinkwasser-Qualität und Low-Maintenance-Design.**

#### Shurflo Aqua King Series (Druckwasser-Standard)

**Shurflo 4048 (24V) — Bestseller für Fahrtenyacht-Druckwasser**
- Durchfluss: 19 L/min @ 2,5 bar, 23 L/min @ 1,5 bar
- Druck: max. 4,5 bar
- Stromaufnahme: 11 A @ 24V (sehr effizient)
- Selbstansaugung: ja, bis ~1,2 m (besser als Jabsco)
- Motortyp: EC-Motor (elektronisch kommutiert), ultra-langlebig
- Geräusch: 68 dB (leiser als Jabsco)
- Anschlüsse: barbed 10 mm oder Klemmbefestigung
- Preis: €320–420
- **Besonderheit:** Dichtsatz wartbar, Ölbad-Lagerung statt Kunststoff (10000+ h Lebensdauer möglich)
- **Einsatz:** Premium-Yacht-Standard auf Neubau-Segelbooten, sehr gängig bei Hallberg-Rassy, Bavaria, Hanse
- **Deutsche Importeur:** Nautische Systeme GmbH, Lübeck

**Shurflo 2088 (12V/24V) — Backup-Druckpumpe**
- 12V: 11 L/min @ 2,5 bar, 10 A
- 24V: 13 L/min @ 2,5 bar, 6 A
- Druck: max. 4,0 bar
- Preis: €280–350
- **Anwendung:** Kleine Yachten 6–10m, oder als 2. Pumpe auf größeren Booten

#### Shurflo Trilift und Quad-Serie (höherer Druck)

**Shurflo Triplex (24V) — Druckunabhängiger Durchfluss**
- Durchfluss: 20 L/min @ 4,0 bar (deutlich besser als Membran-Pumpen bei Gegendruck)
- Druck: max. 6,5 bar
- Stromaufnahme: 16 A @ 24V
- Motortyp: 3-Zylinder-Kolbenprinzip
- Geräusch: 75 dB
- Preis: €450–580
- **Vorteil:** Konstanter Durchfluss über Druckbereich (ideal für Hochdeckboote mit langen Leitungen)
- **Nachteil:** Schwerer (2,5 kg), komplexere Wartung
- **Installation:** Premium-Yachten 18–30m, oft als Haupt-Druckwassersystem

---

### 4.4 Johnson Pump — Skandinavischer Qualitäts-Hersteller

**Johnson ist schwedisch, sehr verbreitet in Nordeuropa (Norwegen, Schweden), stark in deutschem Markt.**

#### Johnson AquaJet Serie (Druckwasser)

**AquaJet 3.0 (12V/24V) — Budget-Druckpumpe**
- 24V: 18 L/min @ 2,5 bar, 10 A
- Druck: max. 4,0 bar
- Stromaufnahme: niedrig
- Selbstansaugung: gut (mag Luftansaugung nicht)
- Preis: €200–280
- **Häufig verbaut:** kleinere Yachten < 12m, skandinavische Serienproduktion

**AquaJet 5.0 (24V) — Mittlere Leistung**
- Durchfluss: 23 L/min @ 2,5 bar, 25 L/min @ 1,5 bar
- Stromaufnahme: 12 A @ 24V
- Preis: €300–380
- **Konkurrenz:** direkt zu Shurflo 4048, ähnliche Leistung, weniger bekannt im deutschsprachigen Raum

#### Johnson Viking Power Series (Bilge/Mehrzweck)

**Viking Power 12-24 (12V/24V-dual) — Bilge mit Druck-Option**
- Impeller-Bilge: 60 L/min @ 0 bar
- Stromaufnahme: 16 A @ 12V, 9 A @ 24V
- Preis: €250–330
- **Besonderheit:** Dual-Spannungs-Motor, ideal für Boote mit gemischter Elektrik

#### Johnson Fäkalien-Pumpe WM2 (24V)

**WM2 Macerator (24V) — Skandinavischer Standard**
- Durchfluss: 28 L/min @ 3 bar
- Stromaufnahme: 18 A @ 24V
- Geräusch: 84 dB
- Preis: €490–620
- **Häufig in:** Finnischen/Schwedischen Serien-Yachten

---

### 4.5 Rule Industries — US-Standard für Bilge

**Rule ist US-Marktführer für Bilge-Pumpen, sehr robust, aber weniger in Europa verbreitet.**

#### Rule Bilge-Impeller-Serie

**Rule 1100 GPH (24V) — Hohe Förderleistung**
- Durchfluss: 55 L/min @ 0 bar (großes Leck-Szenario)
- Stromaufnahme: 13 A @ 24V
- Geräusch: 70 dB
- Impeller: Flügeldesign (robuster gegen Fremdstoffe als Standard)
- Preis: €220–300 (günstiger als europäische Äquivalente)
- **Einsatz:** große Yachten, Expeditions-Motorboote, User Refit häufig

**Rule 3700 GPH (24V) — Extreme Notfall-Bilge**
- Durchfluss: 140 L/min @ 0 bar (Notszenario, nur kurze Betriebsdauer)
- Stromaufnahme: 25 A @ 24V
- Motor: für 15–20 min Betrieb ausgelegt, dann Überhitzung
- Preis: €180–250
- **Installation:** 2. oder 3. Bilge-Pumpe auf Blauwasseryachten, nicht als Haupt-System

#### Rule WM2500 (24V) — Greywater/Wastewater

**WM2500 (24V) — Wastewater-Pumpe für Dusch-Sumpf**
- Durchfluss: 30 L/min
- Druck: 2–3 bar
- Stromaufnahme: 15 A
- Preis: €280–360
- **Anwendung:** Duschen über Billge, separate Sumpf-Entwässerung

---

### 4.6 Flojet Group — Hochleistungs-Druckpumpen

**Flojet ist spezialisiert auf Mehrfach-Membran-Pumpen (Triplex, Quad) für höhere Drücke und Durchflüsse.**

#### Flojet Triplex 24V Druckwasser-Serie

**Flojet Triplex 3-Zylinder (24V) — Premium-Druckwasser**
- Durchfluss: 25 L/min @ 3,0 bar (konstant über Druckbereich)
- Druck: max. 6,5 bar
- Stromaufnahme: 16–18 A @ 24V
- Geräusch: 76 dB
- Selbstansaugung: ja
- Anschlüsse: 10–12 mm
- Preis: €480–620
- **Vorteil:** sehr druckstabil, ideal für High-Deck-Boote
- **Nachteil:** schwerer, komplexere Wartung
- **Einsatz:** 20–35m Yachten, oft kombiniert mit Akkumulator-Tank

#### Flojet Quad 4-Zylinder (24V) — Maximum-Leistung

**Flojet Quad (24V) — 4-Zylinder-Druckwasser**
- Durchfluss: 35 L/min @ 3,0 bar
- Druck: max. 7,0 bar
- Stromaufnahme: 20–22 A @ 24V
- Selbstansaugung: ja, sehr zuverlässig
- Preis: €650–800
- **Installation:** Große Yachten (> 25m) mit mehreren Bädern, oder zentrale Deckwäsche-Hochdruck-Variante
- **Hersteller-Datenblatt:** Verfügbar, 24-Volt-Dauerbelastung bis 120 h kontinuierlich testifiziert

---

### 4.7 ShinMaywa/Oberdorfer — Spezialist-Macerator

**ShinMaywa ist japanischer Spezialist für Fäkalien-Systeme, sehr häufig OEM-Ausrüstung auf europäischen Yachten.**

#### ShinMaywa HMS 2300 (24V) — Skandinavischer Favorit-Macerator

**HMS 2300 (24V) — Top-Fäkalien-Macerator in Europa**
- Durchfluss: 45 L/min @ 3 bar
- Stromaufnahme: 25 A @ 24V
- Messwerk: Dual-Messer, sehr fein zerkleinernd
- Betriebstemperatur: bis 55 °C (erlaubt Warm-Spülungen)
- Geräusch: 83 dB (noch akzeptabel)
- Anschlüsse: 20 mm Saug- und Druckstutzen
- Preis: €680–850
- **Besonderheit:** Standard auf finnischen/skandinavischen Bootswerften (Azimut, Bavaria Nord, Hanse)
- **Wartung:** Messersatz nach 2500 h (~€140), Dichtungen (€60)
- **Installation:** immer mit Druckschalter und Rückschlagventil

---

### 4.8 Vergleichstabelle Aktuelle Standard-Modelle (2025)

| Modell | Hersteller | Typ | Durchfluss | Druck | Strom | Preis EUR | Lebensd. |
|---|---|---|---|---|---|---|---|
| Par-Max 1.5 | Jabsco | Membran | 15 L/min | 4,0 bar | 12 A/12V | €260 | 3–4 kJ |
| Shurflo 4048 | Shurflo | Membran | 19 L/min | 4,5 bar | 11 A/24V | €380 | 8–10 kJ |
| AquaJet 5.0 | Johnson | Membran | 23 L/min | 4,0 bar | 12 A/24V | €320 | 5–6 kJ |
| Flojet Triplex | Flojet | 3-Zylinder | 25 L/min | 6,5 bar | 18 A/24V | €560 | 8–10 kJ |
| Shurflo Triplex | Shurflo | 3-Zylinder | 20 L/min | 6,5 bar | 16 A/24V | €520 | 8–10 kJ |
| Par-Max Bilge 1 | Jabsco | Impeller | 55 L/min | 2,0 bar | 20 A/12V | €240 | 0,5–1 kJ |
| Whale Gulper 320 | Whale | Impeller | 40 L/min | 2,0 bar | 24 A/24V | €400 | 2–3 kJ |
| Rule 1100 GPH | Rule | Impeller | 55 L/min | 1,5 bar | 13 A/24V | €260 | 1–2 kJ |
| Par-Max Macerator | Jabsco | Macerator | 30 L/min | 3,0 bar | 18 A/24V | €650 | 2–3 kJ |
| HMS 2300 | ShinMaywa | Macerator | 45 L/min | 3,0 bar | 25 A/24V | €780 | 2–3 kJ |
| Whale WM3 | Whale | Macerator | 25 L/min | 3,0 bar | 16 A/24V | €580 | 2–3 kJ |

**Noten:**
- Lebensdauer in Betriebsstunden abgekürzt (kJ = 1000 h)
- Preise sind UVP Deutschland/Österreich 2025, real oft 10–15 % günstiger bei Online-Fachhändlern
- 12V-Modelle werden elektrisch ungünstiger bei Booten > 12m (Spannungsverlust in Kabeln)

---

## 5. Hersteller-Datenbank

### 5.1 Jabsco/Xylem — Vollständiges Produktportfolio

**Hauptsitz:** Illinois, USA (Xylem Inc. — Börse NYSE: XYL)  
**Europäischer Distributor:** Xylem GmbH, Duisburg  
**Deutsche Fachhändler:** Nautische Systeme, Boote Lackner, Schiffszubehör Meyer  

**Kern-Produktlinien für Yachten:**

```
DRUCKWASSER (Haushaltsversorgung)
├─ Par-Max Compact (12V, klein)
├─ Par-Max 1.5–5 (12V/24V, Standard)
├─ Par-Max HyperFlow (24V, hoher Durchfluss)
└─ Par-Max Spa (220V für Großyachten)

BILGE (Wasserableitung)
├─ Par-Max Bilge 1–3 (Impeller, verschiedene Größen)
├─ Accusump (mit Akkumulator kombiniert)
└─ Manual Bilge (Handbilge, verschiedene Gewinde)

FÄKALIEN/GREYWATER
├─ Par-Max Macerator 18590–18610 (verschiedene Leistungen)
├─ Toilet-Systeme (integriert WC + Pumpe)
├─ Greywater Sump Pump
└─ Waste Discharge Valve

SPEZIAL (Kühlwasser, Hydraulik, Heizwasser)
├─ Impeller Pumps für Motorkühlung
├─ Pressure Vessels (Akkumulatoren 0,5–10 L)
└─ Digital Pumpensteuerung (24V mit Fernüberwachung)
```

**Preislich:** Jabsco ist Premium-Hersteller, ca. 15–25 % über Budget-Alsternativen.  
**Verfügbarkeit:** Quasi unbegrenzt (Massenproduktion), Ersatzteile im Maritimen Fachhandel.  
**Zuverlässigkeit:** Stark, aber Impeller-Bilgen (Par-Max Bilge 1) verschleißen schnell (500–700 h).

**Beispiel-Rechnung Systemzusammenstellung 12–14m Fahrtenyacht:**
```
Druckwasser:        Par-Max 3 (24V)        €350
+ Akkumulator:      Jabsco 5 L              €120
+ Schalter:         Druckschalter 1–4 bar  €40
+ Filter:           Frischwasser 100 µm    €50
Bilge Haupt:        Par-Max Bilge 1        €240
Bilge Backup:       Manuelle Handbilge     €150
Fäkalien:           Par-Max Macerator      €650
+ Dreiweg-Ventil:   für Sammeltank          €80
Sonstige Ventile:   Rückschlag, Sperrung    €120
Schläuche, Fittings, Isolierung:             €200
─────────────────────────────────
GESAMTBUDGET PUMPEN/VENTILE:                €1970
```

---

### 5.2 Whale Pumps — Britische Zuverlässigkeit

**Hauptsitz:** Bristol, UK  
**Deutsche Distributoren:** Bootsrevue, Nautische Systeme, Boote Lackner  

**Produktlinien:**

```
DRUCKWASSER
├─ GP-Serie (0325, 0450, 0635)
├─ Larger Capacity Pumps
└─ Dual Voltage (12V/24V kompatibel)

BILGE
├─ Gulper Serie (220, 320, 500)
│  └─ 320 ACE (mit Auto-Priming)
├─ Gusher Serie (höhere Leistung)
└─ Manual Bilge (verschiedene Größen)

FÄKALIEN
├─ WM-Serie (WM2, WM3, WM4)
├─ MU-Serie (Unisex-Toilette-Pumpe)
└─ Combination Systems

ZUSATZ
├─ Pressure Vessels
├─ Sump Pumps
└─ Float Switches
```

**Preislich:** leicht unter Jabsco, sehr kompetitiv (€180–400 je nach Modell).  
**Verfügbarkeit:** Sehr gut in UK/Skandinavien, in Deutschland etwas schwächer (Niche-Import).  
**Zuverlässigkeit:** Sehr gut, Whale ist Qualitäts-Marke, Reparaturen häufig möglich.  

**Besonderheit — Whale Gulper 320 ACE:** Auto-Priming-Elektronik ist einzigartig, reduziert Ausfallrisiko durch Luftblocken erheblich. Kostet ~€400, aber Langzeitinvestition lohnt sich.

---

### 5.3 Shurflo — Amerikanischer Premium-Hersteller

**Hauptsitz:** Corona, Kalifornien, USA  
**Europäischer Importeur:** Nautische Systeme GmbH, Lübeck (seit 1990 Shurflo-Monopolist)  
**Deutsche Fachhändler:** fast alle größeren Bootszubehör-Läden führen Shurflo

**Produktlinien:**

```
DRUCKWASSER-STANDARD
├─ Aqua King (2088, 4048, 4058)
├─ Ult-RA-Low Flow (dezentralisiert, für einzelne Duschen)
└─ Automatic Demand Pumps

DRUCKWASSER-HOCHLEISTUNG
├─ Triplex 3-Zylinder
├─ Quad 4-Zylinder
└─ PowerSurge (Hochdruck 10+ bar)

GREYWATER/SUMPF
├─ Shower Sump Pump
├─ Shower Drain System
└─ Sink Drain Pump

SPEZIAL
├─ Solar-Versionen (für Off-Grid)
├─ Automatic Shutoff Ventile
└─ Pressure Tanks
```

**Preislich:** Premium, aber hohe Langzeitqualität (Shurflo-Geräte halten oft 10+ Jahre).  
**Verfügbarkeit:** Hervorragend in Deutschland (Lübeck-Import = direkte Lieferkette).  
**Zuverlässigkeit:** Spitzenklasse, EC-Motoren sind nicht verschleißanfällig.  

**Empfehlung für Neubau/Retrofit:** Shurflo 4048 ist quasi Standard auf modernen Fahrtenyachten (Bavaria, Hanse, Hallberg-Rassy), weil:
- 24V, sehr effizient (nur 11 A @ 2,5 bar)
- Selbstansaugung zuverlässig
- EC-Motor, 10000+ h Lebensdauer
- Lüftung + Schmierung hervorragend

---

### 5.4 Johnson Pump — Skandinavischer Spezialist

**Hauptsitz:** Västervik, Schweden  
**Europäischer Vertrieb:** Johnson Nordic AB  
**Deutschland-Präsenz:** gut in Skandinavien-Yacht-Märkten, schwächer in Deutschland

**Produktlinien:**

```
DRUCKWASSER
├─ AquaJet 3.0–5.0
├─ AquaJet Compact
└─ Twin Pump (Doppel-Druckpumpe in 1 Gehäuse)

BILGE
├─ Viking Power (Standard)
├─ Viking Power Premium (mit Thermoschutz)
└─ Viking Impact Pump

FÄKALIEN
├─ WM2–WM4 Macerator
├─ Toilet Systems (integriert)
└─ Waste Tank Pumps

HEIZ-/KÜHLWASSER
├─ für Diesel-Motorkühlung
└─ für Hydronic Heating
```

**Preislich:** Mid-Range, günstiger als Shurflo, ähnlich wie Jabsco.  
**Verfügbarkeit:** in Deutschland schwach, stark in Nordeuropa.  
**Zuverlässigkeit:** sehr gut, skandinavischer Massenmarkt.  

**Besonderheit:** Twin-Pump-Konzept (zwei Membranpumpen in 1 Gehäuse mit gemeinsamer Motorsteuerung) — praktisch, aber weniger verbreitet.

---

### 5.5 Rule Industries — US-Budget-Spezialist

**Hauptsitz:** Oceanside, Kalifornien, USA  
**Distributoren Deutschland:** Bootsrevue (vereinzelt), meistens Online-Importe

**Produktlinien:**

```
BILGE (Kerngeschäft)
├─ Standard Series (500–3700 GPH)
├─ Automatic Series (mit Schwimmschalter)
├─ Aerator Series (belüftende Bilge)
└─ High Capacity Series (Notfall-Bilge)

GREYWATER
├─ WM-Serie (Wastewater)
└─ Sump Series

SPEZIAL
├─ 12V Sump Pumps
└─ Manual Bilge
```

**Preislich:** Billig-Segment, 20–30 % unter Jabsco/Whale.  
**Verfügbarkeit:** in Deutschland schlecht (US-Importe, lange Lieferketten).  
**Zuverlässigkeit:** OK für Notfall-Bilgen, aber nicht Langzeit-Standard empfohlen.  

**Problem:** Rule-Bilgen laufen sehr laut (73–75 dB), Impeller-Verschleiß ähnlich wie Jabsco.

---

### 5.6 Flojet — Hochdruck-Spezialist

**Hauptsitz:** Chico, Kalifornien, USA  
**Europäischer Distributor:** verschiedene, weniger zentral als Shurflo

**Produktlinien:**

```
DRUCKWASSER-HOCHLEISTUNG
├─ Triplex 3-Zylinder
├─ Quad 4-Zylinder
├─ 5-Zylinder-Optionen
└─ Pressure Rating bis 7 bar

CUSTOM-LÖSUNGEN
├─ OEM-Integration (für Yacht-Werften)
├─ Volumetrischer Durchfluss (sehr präzise)
└─ Fernüberwachung (24V Digital)
```

**Preislich:** Premium, Triplex ~€550, Quad ~€750.  
**Verfügbarkeit:** in Deutschland via Spezial-Distributoren.  
**Zuverlässigkeit:** Spitze, 3- und 4-Zylinder-Design sehr robust.  

**Einsatz:** hauptsächlich auf Großyachten (> 20m) oder Refit-Projekte mit höheren Anforderungen (lange Leitungen, mehrere Badezimmer, Hochdeck).

---

### 5.7 ShinMaywa/Oberdorfer — Macerator-Spezialist

**Hauptsitz:** Tokio, Japan (ShinMaywa), auch unter US-Label Oberdorfer bekannt  
**Europäischer Handel:** Wird oft als OEM-Standard verbaut, direkter Einzelkauf schwierig

**Produktlinien:**

```
FÄKALIEN-SYSTEME
├─ HMS-Serie (2300, 2400, 3000)
├─ Hochleistungs-Macerator (45+ L/min)
└─ Dual-Motor-Versionen (für extreme Anforderungen)

GREYWATER
├─ Universal Sump Pumps
└─ Shower Drain Systems
```

**Preislich:** HMS 2300 ~€750–850, teuer, aber OEM-Standard auf skandinavischen Booten.  
**Verfügbarkeit:** Oft nur über Bootswerft (Einbau-Neuausstattung).  
**Zuverlässigkeit:** Ausgezeichnet, japanischer Engineering-Standard.  

**Besonderheit:** HMS-Messerwerk ist mehrfach gehärtet und feinere Zerkleinerung als westliche Konkurrenz → weniger Verstopfungen bei Zahnseide, Feuchttüchern, etc.

---

### 5.8 Marktanteile und Verbreitungs-Index (Deutschland 2025)

**Nach Bootstyp und Hersteller:**

| Hersteller | Klein-Boot | Fahrtenyacht | Blauwasser | Megayacht |
|---|---|---|---|---|
| Jabsco/Xylem | 35 % | 40 % | 25 % | 20 % |
| Shurflo | 15 % | 35 % | 40 % | 30 % |
| Whale | 10 % | 12 % | 18 % | 12 % |
| Johnson | 5 % | 5 % | 10 % | 8 % |
| Rule | 5 % | 3 % | 3 % | 2 % |
| Flojet | 2 % | 2 % | 2 % | 15 % |
| ShinMaywa | 8 % | 8 % | 12 % | 18 % |
| Sonstige/generisch | 20 % | 15 % | 10 % | 5 % |

**Fazit:** Shurflo wächst (Premium, Effizienz), Jabsco bleibt Marktführer (Häufigkeit Ersatzteil-Verfügbarkeit), Whale stabil in UK/Skandinavien, andere = Nischen.

---

### 5.9 Preisliste Standard-Modelle (2025)

**Alle Preise in EUR, UVP Deutschland/Österreich, Real oft 10–15 % Rabatt bei Fachhändlern.**

#### Druckwasser-Pumpen

| Modell | Typ | Leistung | UVP EUR |
|---|---|---|---|
| Jabsco Par-Max 1.5 (12V) | Membran | 15 L/min @ 2,5 bar | €260 |
| Jabsco Par-Max 3 (24V) | Membran | 20 L/min @ 2,5 bar | €320 |
| Whale GP0450 (24V) | Membran | 22 L/min @ 2,5 bar | €300 |
| Shurflo 4048 (24V) | Membran-EC | 19 L/min @ 2,5 bar | €380 |
| Johnson AquaJet 5.0 (24V) | Membran | 23 L/min @ 2,5 bar | €310 |
| Shurflo Triplex (24V) | 3-Zylinder | 25 L/min @ 3,0 bar | €520 |
| Flojet Triplex (24V) | 3-Zylinder | 25 L/min @ 3,0 bar | €560 |
| Flojet Quad (24V) | 4-Zylinder | 35 L/min @ 3,0 bar | €750 |

#### Bilge-Pumpen

| Modell | Typ | Leistung | UVP EUR |
|---|---|---|---|
| Jabsco Par-Max Bilge 1 (12V) | Impeller | 55 L/min @ 0 bar | €240 |
| Whale Gulper 220 (12V) | Impeller | 65 L/min @ 0 bar | €220 |
| Whale Gulper 320 ACE (24V) | Impeller mit Auto-Prime | 40 L/min @ 0 bar | €400 |
| Rule 1100 GPH (24V) | Impeller | 55 L/min @ 0 bar | €260 |
| Rule 3700 GPH (24V) | Impeller-Notfall | 140 L/min @ 0 bar | €200 |
| Jabsco Par-Max Bilge 2 (24V) | Impeller | 75 L/min @ 0 bar | €280 |

#### Fäkalien-Maceratoren

| Modell | Typ | Leistung | UVP EUR |
|---|---|---|---|
| Jabsco Par-Max Macerator (24V) | Macerator | 30 L/min @ 3 bar | €650 |
| Whale WM3 (24V) | Macerator | 25 L/min @ 3 bar | €580 |
| Johnson WM2 (24V) | Macerator | 28 L/min @ 3 bar | €620 |
| ShinMaywa HMS 2300 (24V) | Macerator Premium | 45 L/min @ 3 bar | €800 |
| ShinMaywa HMS 2400 (24V) | Macerator Extra | 50 L/min @ 3 bar | €920 |

#### Zubehör (Akkumulatoren, Schalter, Filter)

| Komponente | Größe/Typ | UVP EUR |
|---|---|---|
| Akkumulator-Tank (Membran) | 1 L | €70 |
| Akkumulator-Tank (Membran) | 2 L | €100 |
| Akkumulator-Tank (Membran) | 5 L | €160 |
| Druckschalter (mechanisch) | 1–4 bar | €40 |
| Druckschalter (digital) | 0,5–5 bar | €120 |
| Frischwasser-Filter | 100 µm | €50 |
| Rückschlagventil | 10 mm barbed | €25 |
| Sperrventil (3-Wege) | für Macerator | €80 |
| Priming-Taste | manuell | €30 |
| Luftventil (oben Tank) | Standard | €20 |

---

### 5.10 Kaufempfehlungen nach Bootsklasse (2025)

#### Kleinboot (< 8m)

**Druckwasser:**
- Manuell (Handbilge mit Schlauch-Aufsatz) oder
- Budget: Jabsco Par-Max 1.5 (12V) ~ €260

**Bilge:**
- Manuelle Handbilge (€120–150, Backup Standard) +
- Optional: Jabsco Par-Max Bilge 1 (12V) für Nacht-Automatik

**Fäkalien:**
- Sammeltank (20 L) + manuelles Pumpensystem oder
- Kleine Macerator (Par-Max 18590, wenn Platz vorhanden)

**Gesamtbudget:** €500–800

#### Fahrtenyacht (8–14m)

**Standard-Spezifikation (empfohlen):**

**Druckwasser:**
- Haupt: Shurflo 4048 (24V) + 2 L Akkumulator ~ €380 + €100

**Bilge:**
- Haupt: Impeller 12V/24V Doppel-Schaltung (Jabsco oder Whale) ~ €240 × 2 = €480
- Backup: Manuelle Handbilge ~ €150

**Fäkalien:**
- Sammeltank (40 L) + Macerator (Par-Max 18590) ~ €200 + €650

**Zubehör:** Druckschalter, Filter, Ventile, Schläuche ~ €300

**Gesamtbudget:** €2200–2600

#### Blauwasseryacht (15–24m)

**Premium-Spezifikation (Sicherheit):**

**Druckwasser:**
- Haupt: Shurflo Triplex (24V) + 5 L Akkumulator ~ €520 + €160
- Backup: Shurflo 4048 oder manueller Bypass ~ €380

**Bilge:**
- Doppel-Schaltung (2× unabhängig): Whale Gulper 320 ACE ~ €400 + €400
- Notfall-Bilge: Rule 3700 GPH ~ €200
- Manuelle Handbilge ~ €150

**Fäkalien:**
- Sammeltank (60 L) + HMS 2300 Macerator ~ €300 + €800

**Zubehör & Verdopplung:** ~€500 (digitale Schalter, redundante Ventile)

**Gesamtbudget:** €4200–5000

#### Megayacht (> 24m)

**Professionelle Installation:**

**Druckwasser:**
- Zentrifugal-Hauptsystem oder Flojet Quad (24V) ~ €750
- 2×Backup-Druckpumpen (Shurflo 4048) ~ €380 × 2 = €760
- Akkumulator 10 L ~ €250
- Fernüberwachung (digitale Druckmelder, Durchfluss) ~ €1000

**Bilge:**
- 3–4 × unabhängige Impeller-Pumpen (verschiedene Größen) ~ €1500
- Zentrale Bilge-Monitoring (Alarme, Redundanz) ~ €800

**Fäkalien:**
- Zentrale Greywater-Behandlung + Sammeltank (150 L) ~ €1500
- HMS 2300 oder 2400 Macerator × 2 ~ €1600

**Zubehör & Engineering:** ~€2000

**Gesamtbudget:** €9500–12000 (+ Installation/Engineering)

---

**Nächste Schritte (Abschnitte 6–10):**
- 6. Installationsrichtlinien (Rohrbau, Elektro, Material-Kompatibilität)
- 7. Fehlerdiagnose und Wartung (Checklisten, Reparatur-Szenarios)
- 8. Häufige Fehler und Ausfallmuster (mit Fallbeispielen)
- 9. Redundanz-Strategien für sichere Fahrt (Backup-Konzepte)
- 10. Retrofit-Leitfaden für ältere Yachten

---

**END OF SECTIONS 1–5 (≈1200 lines)**

---

## 6. Fehlerbild-Atlas

### FB-24-05-001: Pumpe startet nicht

**Schweregrad:** Kritisch (Druckwasser, Bilge) | Hoch (Greywater, Macerator)

**Symptome:**
- Motor läuft, Pumpe bewegt sich nicht
- Motor läuft nicht an
- Schaltrelais klickt, kein Anlauf
- Sicherung durchgebrannt

**Ursachen:**
- Stromversorgung unterbrochen (Sicherung, Schalter, korrodierte Kontakte)
- Pumpe trocken gelaufen (Impeller blockiert/verschweißt)
- Druckschalter defekt (Kontakt offen)
- Motor-Kondensator defekt (bei AC-Motoren)
- Mechanische Blockade (Schmutz, Fremdkörper im Pumpengehäuse)

**Diagnose:**
- Stromspannung an Stecker messen (sollte 24V oder 110/230V entsprechend sein)
- Sicherung sichtprüfung + Multimeter-Durchgang-Test
- Schaltrelais mit Ohmmeter prüfen (bei Betätigung: 0Ω, sonst ∞Ω)
- Pumpen-Einlass mit Saugtest prüfen (saugt Luft an?)
- Motor-Fremdlauf prüfen (von Hand drehen möglich?)

**Sofortmaßnahmen:**
1. Stromversorgung prüfen (Batterie, Schalter, Sicherung)
2. Notsaugpumpe (manuell oder mobil) einsetzen
3. Wenn kritisch (Druckwasser, Bilge): Backup-Pumpe aktivieren
4. Druck-/Bilge-Alarme auslösen, Maschinenraum kontrollieren

**Reparatur:**
- Sicherung austauschen (richtige Amperage nutzen: z.B. 20A für Flojet Quad)
- Schaltrelais austauschen (~€50–120)
- Motor-Kondensator austauschen (~€20–40)
- Pumpe ausbauen, Impeller prüfen, ggf. fremdkörper entfernen
- Motor-Freigängigkeit prüfen; ggf. Motorlager ausbauen/schmieren
- Gesamte Pumpe austauschen wenn Motor beschädigt (~€400–1500 je nach Typ)

**Prävention:**
- Sicherungsplan nach Herstellerangaben respektieren
- Stromkreise unter Last testen (kein Leerlauf-Test!)
- Batterie-Zustand wöchentlich prüfen (Spannung, Säuredichte)
- Kontakte alle 6 Monate reinigen (Batterieclips, Schalterkontakte)
- Jährliche Funktionsprobe ohne Last + mit Last

**Kostenrahmen EUR:**
- Sicherung: 5–10
- Schaltrelais: 50–120
- Motor-Kondensator: 20–40
- Kompletter Pumpenmotor: 400–1500
- Facharbeitszeit: 100–300 (diagnostizieren + reparieren)

---

### FB-24-05-002: Pumpe läuft ständig

**Schweregrad:** Hoch (Versorgung, Batterie) | Mittel (Komfort)

**Symptome:**
- Pumpe schaltet nicht ab (Druckschalter reagiert nicht)
- Druckmesser zeigt ständig 2–3 bar (zykliert nicht)
- Summen/Vibrieren kontinuierlich
- Batterie erschöpft sich schneller

**Ursachen:**
- Druckschalter kontakt verschweißt (hängt in Schließposition)
- Druckschalter-Ansprechpunkt verstellt oder nicht kalibriert
- Durchfluss-Schalter defekt (Kontakt bleibt geschlossen)
- Lecks in der Leitung (Druck kann nicht gehalten werden, Pumpe läuft nach)
- Akkumulator entladen oder defekt (kein Druckpolster)

**Diagnose:**
- Druckmesser beobachten: sollte bei Anlauf auf max. ansteigen, dann zur Solldruck-Haltung absinken
- Druckschalter manuell betätigen: Klick hörbar? Schließ- und Öffnungspunkte prüfen
- Leckage-Test: Alle Verbindungen mit Seifenwasser prüfen, Druckleitung unter Wasser (Badewanne)
- Akkumulator Druckprüfung: sollte 0,5–1 bar unter Solldruck stehen (mit Reifen-Druckmesser)
- Stromaufnahme messen: bei stehender Pumpe sollte keine Stromaufnahme erfolgen

**Sofortmaßnahmen:**
1. Druckschalter von Hand ausschalten (Not-Aus-Knopf drücken)
2. Pumpe manuel abstellen (Breaker/Sicherung ausschalten)
3. Leckagestelle identifizieren und abdichten (Tuch, Provisorisches Tape)
4. Batterie-Spannungsverlauf überwachen (nicht unter 10.5V bei 24V-System fallen)

**Reparatur:**
- Druckschalter ausbauen, reinigen, Kontakte mechanisch säubern mit feiner Feile/Poliertuch
- Druckschalter-Ansprechpunkte neukalibrieren (vergleich: Herstellerdatenblatt). ggf. Feder nachspannen
- Druckschalter austauschen wenn beschädigt (~€80–180)
- Durchfluss-Schalter prüfen: Messingkörper auf Verschleiß, ggf. austauschen (~€40–100)
- Alle Leckagen abdichten: Verschraubungen nachziehen, Dichtungen austauschen
- Akkumulator:
  - Luft-Druck prüfen (sollte 0.5 bar unter Min-Systemdruck = ca. 1 bar für 2-bar-Anwendungen)
  - Wenn < 0.5 bar: Druckluft-Pumpe nutzen, auf korrekten Druck aufpumpen
  - Wenn Membran gerissen: Akkumulator austauschen (~€150–300)

**Prävention:**
- Druckschalter wöchentlich manuel betätigen (Kontakt-Check)
- Alle Verbindungen alle 3 Monate unter Wasser prüfen (Seifentest)
- Akkumulator-Luftdruck alle 6 Monate prüfen
- Wasserfiltration vor Pumpe (5–20 µm) um Verschmutzung zu vermeiden

**Kostenrahmen EUR:**
- Druckschalter-Reinigung: 0 (DIY) oder 50–80 (Fachperson)
- Druckschalter-Austausch: 80–180
- Durchfluss-Schalter: 40–100
- Akkumulator-Membran-Austausch: 150–300
- Leckage-Behebung: 50–300 (je nach Umfang)
- Gesamtarbeitszeit: 150–400

---

### FB-24-05-003: Kein oder zu wenig Druck

**Schweregrad:** Kritisch (Dusche, Küche, Drucktoilette)

**Symptome:**
- Wasser kommt nicht an, oder nur Tropfen (Druck <0.5 bar)
- Durchfluss deutlich unter normal (z.B. Dusche tropft statt sprüht)
- Druck fällt schnell nach Pumpe-Abschaltung ab
- Häufige Pumpen-Zyklierung (Anlauf–Abschaltung–Neuanlauf im <2min Rhythmus)

**Ursachen:**
- Ansaugfilter verstopft (Sand, Algen, Sediment)
- Trockenlauf (Wassertank leer, Ansaugleitung hat Luft)
- Impeller verschlissen oder verstopft
- Rohre/Schlangen blockiert (Verkalkung, Biofilm, Fremdkörper)
- Rückschlagventil klemmt oder ist blockiert
- Pumpen-Auslass-Schlange gerissen oder abgeknickt
- Zerstoerer Macerator bei Greywater vorgelagert

**Diagnose:**
- Wassertank sichtprüfung (genug Wasser vorhanden?)
- Ansaugfilter sichtprüfung (Farbe, Verschmutzung)
- Druck an Pumpen-Ausgang messen (Druckmanometer anschrauben, sollte >1.5 bar für Dusche)
- Druck bei entlastetem System (Hahn geschlossen) messen (sollte auf Schaltdruck ansteigen)
- Ansaugleitung inspizieren (Luft-Lecks an Schläuchen/Anschlüssen)
- Rohre/Schlangen durchprüfen: mit Druckluft durchblasen oder Spülwasser testen
- Rückschlagventil: Öffnungs-Widerstand prüfen (manuell leichter Druck sollte öffnen)

**Sofortmaßnahmen:**
1. Ansaugfilter inspizieren und reinigen (Wasser abgießen, Sediment entfernen, mit Süßwasser spülen)
2. Wassertank auffüllen
3. Ansaugleitung auf Luft-Lecks prüfen (Hand über Ansaug-Schlauchende halten: sollte Saugkraft spüren)
4. Wenn kritisch: manuell Wasser mit Hand-Pumpe oder Eimer schöpfen bis System priming läuft

**Reparatur:**
- Ansaugfilter austauschen (alle 6–12 Monate je nach Wassergüte)
- Impeller ausbauen: Verschleiß sichtprüfen
  - Leichte Abnutzung: mit feiner Feile polieren (0.1–0.2mm)
  - Starker Verschleiß oder Schäden: austauschen (~€80–200)
- Rohre/Schlangen durchspülen:
  - Kalk-Ablagerungen: mit Essig/Zitronensäure-Lösung durchspülen (12–24h einweichen)
  - Biofilm: mit Wasserstoffperoxid (3–6%) oder spez. Biofilm-Reiniger
  - Fremdkörper: Druckluft (2–3 bar) durchblasen
- Rückschlagventil:
  - Öffnungs-Widerstand prüfen (sollte mit leichtem Druck öffnen)
  - Wenn verklemmt: mit Essig einweichen, vorsichtig klopfen, neu einspülen
  - Wenn defekt: austauschen (~€60–150)
- Ansaugleitung auf Luft-Lecks prüfen und neu abdichten

**Prävention:**
- Wassertank regelmäßig spülen (quartalsweise bei stillgestandenem Boot)
- Ansaugfilter alle 6 Monate inspizieren
- Wasserleitungen jährlich durchspülen
- Rückschlagventil halbjährlich manuell betätigen (präventivatische Wartung)
- Druckwasser-Anlagen außerhalb Saison mit Frostschutzmittel (Glykol) oder trocken lagern

**Kostenrahmen EUR:**
- Ansaugfilter-Austausch: 30–80
- Impeller-Austausch: 80–200
- Rohrreinigung (DIY Essig): 20–50 | (Fachperson): 150–300
- Rückschlagventil: 60–150
- Gesamtarbeitszeit: 200–500

---

### FB-24-05-004: Impeller verschlissen

**Schweregrad:** Mittel bis Hoch (Leistungsverlust, Geräusche)

**Symptome:**
- Druck/Durchfluss nimmt kontinuierlich ab (über Wochen/Monate)
- Ungewöhnliche Geräusche (Schleifen, Rattern, Brummen)
- Vibration deutlich stärker als früher
- Kleine Plastik-Partikel im Filterauslauf sichtbar
- Pumpe verbraucht mehr Strom für gleiches Ergebnis

**Ursachen:**
- Normale Verschleiß (elastische Materialermüdung nach 5–10 Jahren)
- Sand/Sediment im Wasser (angesaugt während Frischwasser-Betankung)
- Chlor-Desinfektionsmittel (zerstört Elastomer, wenn keine speziellen FDA-Impeller)
- Zu hohe Betriebstemperatur (Impeller >40°C erweicht)
- Zu hohe Drehzahl über längere Zeit
- Abrasive Fremdkörper (Metallspäne, Sediment)

**Diagnose:**
- Impeller visuell inspizieren (Spalten, Risse, Abflachungen?)
- Impeller-Oberfläche ertasten (sollte glatt sein, kein Rauheit)
- Druck- und Durchflussmessung: Abfall dokumentieren
- Filterauslauf unter Lupe prüfen (Plastik-Partikel?)
- Motorstrom messen: Vergleich zu Neumaschine
- Temperaturprüfung: Pumpengehäuse sollte lauwarm sein (~30–35°C), nicht heiß (>45°C)

**Sofortmaßnahmen:**
- Betrieb reduzieren (nicht auf Dauerleistung fahren)
- Wassertank besser filtern (Inline-Filter 20 µm vor Pumpe einbauen)
- Betriebstemperatur prüfen und ggf. Kühlsystem verbessern

**Reparatur:**
- **Leichte Verschleißmarken:**
  - Mit feiner Feile/Poliertuch vorsichtig oberflächlich polieren (max. 0.2mm Material)
  - Mit Seifenwasser gründlich spülen
  - Neuinstallation und Test
- **Mittlere Beschädigungen:**
  - Impeller austauschen:
    - Typ identifizieren (Flojet, Shurflo, Jabsco: Hersteller-Nr., Material)
    - Material auswählen:
      - EPDM = Süßwasser/Standardanwendungen (€30–60)
      - FDA-Gummi = Trinkwasser, Chlor-Toleranz (€50–100)
      - Wechselvorlage-Impeller-Set (€80–150, mehrere Größen)
    - Pump ausbauen, alte Impeller entfernen, neue Impeller einpressen
  - Betrieb testen (prüfen auf Druckaufbau, Geräusche)
- **Schwere Beschädigungen:**
  - Komplette Pumpe austauschen (€400–1500)

**Prävention:**
- Frischwasser-Betankung mit Sediment-Filter (20 µm) durchführen
- Chlor-Desinfektionsmittel nur kurzzeitig nutzen (dann sofort mit Süßwasser spülen)
- Betriebstemperatur überwachen (Kühlwasser-Zirkulation, Beschattung)
- Jährliche Sichtprüfung der Impeller durchführen
- Impeller-Austausch alle 5–7 Jahre (vorausschauend, nicht erst bei Ausfall)

**Kostenrahmen EUR:**
- Impeller-Austausch-Kit (einfach): 30–60
- FDA-Gummi-Impeller: 50–100
- Arbeitszeit (Aus-/Einbau): 80–150
- Komplette Pumpe: 400–1500

---

### FB-24-05-005: Membran gerissen

**Schweregrad:** Hoch (Akkumulator) | Kritisch (Membran-Pumpen wie Flojet)

**Symptome:**
- Akkumulator: Druckaufbau funktioniert nicht, Systemdruck fällt schnell nach Pumpen-Stopp
- Membran-Pumpen: Wasser dringt in Gaschamber ein, Leistung sinkt drastisch
- Prüfung mit Reifen-Druckmesser zeigt 0 bar oder sehr niedriger Wert im Akkumulator
- Ölflecken an der Akkumulator-Unterseite (Hydrauliköl tritt aus)

**Ursachen:**
- Normale Alterung (Membrane 5–8 Jahre Lebensdauer)
- Zu hoher oder zu niedriger Vordruck (sollte 0.5–1 bar unter Min-Systemdruck sein)
- Zu hohe Systemtemperatur (Membran erweicht über 50°C)
- Druckstoße (Druckschalter schaltet zu abrupt, erzeugt Hammer-Effekt)
- Falsche Membran-Material (nicht EPDM oder Fluor-Gummi für Salzwasser)
- Zu hohe Zyklierungs-Frequenz (häufiges On/Off auf Membran-Spannung)

**Diagnose:**
- Akkumulator-Druckprüfung (ohne Systemdruck): sollte ~0.7 bar zeigen (bei 2-bar-Anwendungen)
- Wenn 0 bar: Membran ist gerissen oder Ventil ist undicht
- Wasser-Eindringprüfung: Wasserausgang aus Luft-Ventil prüfen (sollte trocken sein)
- Akkumulator-Gewicht: gerissene Membran = deutlich schwerer (weil wassergefüllt)
- System-Zyklustest: Nach Pumpen-Stopp sollte Druck mindestens 3min halten bleiben (mit Druckmesser prüfen)

**Sofortmaßnahmen:**
1. Akkumulator isolieren (Ventil schließen wenn möglich)
2. System in Notbetrieb umschalten (Pumpe manuell schalten statt auf Druckschalter-Automatik)
3. Häufig prüfen, dass Systemdruck nicht unter Min-Wert fällt

**Reparatur:**
- **Akkumulator-Membran-Austausch:**
  - Akkumulator drucklos ablassen (Sicherheitsventil öffnen oder Schlauch lösen)
  - Akkumulator-Gehäuse abbauen
  - Alte Membran entfernen (zwei-teiliges Design: Schraube öffnen, Membran herausziehen)
  - Neue Membran einsetzen (Material-Typ beachten: EPDM für Süßwasser, Fluor-Gummi für Salzwasser)
  - Gewinde mit PTFE-Tape einwickeln (2–3 Lagen)
  - Zusammenbauen und Vordruck neu einstellen (0.5–1 bar unter Min-Systemdruck)
  - System Funktionsprobe durchführen
  - Kosten Austausch-Kit: ~€150–300 | Arbeitszeit: 120–200 EUR
- **Akkumulator komplett austauschen:**
  - Wenn Gehäuse beschädigt oder korrodiert
  - Neuer 10-L-Akkumulator: ~€250–400
  - Einbau + Kalibrierung: 200–300 EUR

**Prävention:**
- Vordruck alle 6 Monate prüfen und ggf. anpassen
- Systemtemperatur überwachen (<40°C ideal)
- Druckstoße vermeiden: Druckschalter sanft kalibrieren (nicht zu steile Schaltflanke)
- Akkumulator alle 5–7 Jahre prophylaktisch austauschen (auch wenn noch funktioniert)
- Hochwertige Akumulatoren mit stabilisiertem Gummimaterial nutzen

**Kostenrahmen EUR:**
- Membran-Austausch-Kit: 150–300
- Arbeit Aus-/Einbau: 120–200
- Neuer Akkumulator: 250–400
- Kompletter Austausch + Einbau: 400–700

---

### FB-24-05-006: Druckschalter defekt

**Schweregrad:** Hoch (Automatik funktioniert nicht)

**Symptome:**
- Schalter reagiert nicht auf Druckänderung (Pumpe läuft ständig oder gar nicht)
- Schaltpunkt ist nicht reproduzierbar (manchmal Anlauf, manchmal nicht bei gleichem Druck)
- Klick/Geräusch nicht hörbar bei Druckaufbau
- Stromkreis-Durchgang mit Ohmmeter zeigt ∞Ω (offener Kontakt) auch unter Druck

**Ursachen:**
- Kontakt verschweißt oder verrußt (Schmutzfilm auf Kontakten)
- Feder-Spannung verloren (Federmaterial ermüdet)
- Kalk-Ablagerungen auf Druck-Ventil (blockiert Betätigung)
- Verschleiß Kontakt-Nase (~100.000 Zyklierungen)
- Überschuss-Druck angewendet (z.B. 5 bar auf 2-bar-Schalter = Kontakt verklemmt)
- Elektrolytische Korrosion bei Salzwasser-Umgebung

**Diagnose:**
- Ohmmeter-Messung: Widerstand sollte sich ändern wenn manuell Betätigung angewendet wird (offen = ∞Ω, geschlossen = <1Ω)
- Sichtprüfung Kontakte: unter Lupe prüfen auf Rußfilm, Verfärbung, Abnutzung
- Druck-Test: Druckmesser anschlißen, langsam Druck aufbauen, Schalter-Klick beobachten
- Ansprechpunkt kalibrieren: sollte bei Hersteller-spezifischem Wert schalten (z.B. 1.5–2.0 bar)

**Sofortmaßnahmen:**
- Schalter manuell betätigen und halten (leidet vorübergehend)
- Pumpe mit manuellem Breaker/Schalter fahren statt auf Druckschalter-Automatik
- Spannung prüfen (sollte Nennspannung an Schalter-Anschlüssen anliegen)

**Reparatur:**
- **Kontakt-Reinigung:**
  - Schalter ausbauen
  - Gehäuse öffnen (Schrauben, keine Klebung!)
  - Kontakte mit feiner Feile oder Kontakt-Poliertuch (Grain 320–600) vorsichtig reiben
  - Mit Druckluft oder Pinsel Rußreste entfernen
  - Gehäuse wieder zusammenbauen und abdichten (ggf. neu mit Isolierband wickeln)
  - Prüfdruck anwenden und Schaltpunkt prüfen
  - Kosten (DIY): 0 EUR | Fachperson: 50–100 EUR
- **Feder-Spannung anpassen:**
  - Wenn Schaltpunkt zu hoch oder zu niedrig: Feder nachspannen (Schraubenhahn vorsichtig drehen)
  - Prüfung nach jeder Verstellung durchführen
  - Kosten: 0 EUR (DIY) | 30–60 EUR (Fachperson)
- **Schalter komplett austauschen:**
  - Typ und Schaltpunkt-Bereich notieren (z.B. "1.5–2.5 bar, 24V DC")
  - Neuen Schalter bestellen (vergleichbares Modell von gleicher oder ähnlicher Herstellern)
  - Alten Schalter ausbauen, neuen mit PTFE-Tape und Dichtpaste einschrauben
  - Prüfung durchführen
  - Kosten neuer Schalter: 80–180 EUR | Arbeit: 100–150 EUR

**Prävention:**
- Druckschalter wöchentlich manuell betätigen (Kontakt-Test)
- Alle 6–12 Monate prophylaktisch reinigen
- Schalter mit Schutzkappe vor Salzwasser-Spray abdecken
- Jährlich Schaltpunkte dokumentieren (Zyklustest mit Druckmesser)
- Schalter alle 8–10 Jahre austauschen (prophylaktisch auch bei noch Funktion)

**Kostenrahmen EUR:**
- Kontakt-Reinigung: 0 (DIY) | 50–100 (Fachperson)
- Feder-Einstellung: 0 (DIY) | 30–60 (Fachperson)
- Neuer Druckschalter: 80–180
- Ausbau/Einbau: 100–150
- Gesamtkosten (Austausch + Installation): 200–350

---

### FB-24-05-007: Leckage am Pumpenkopf

**Schweregrad:** Mittel bis Hoch (Wasserschaden möglich)

**Symptome:**
- Wasser tropft aus Pumpenkopf-Naht (unterhalb Druckhauptschlauch-Anschlusses)
- Feuchte Stelle an Pumpen-Flansch
- Salzverkrustung um Leck-Stelle (Salzwasser ausgetrocknet)
- Wasser in Bilge unter Pumpen-Installation

**Ursachen:**
- Verschraubung gelockert (Vibration, thermische Ausdehnung)
- Dichtung verschlissen oder porös (Alter, Salzwasser-Korrosion, Öl-Durchtritt)
- Überdruckbetrieb (Druckschalter falsch eingestellt, >2 bar bei 1.5-bar-Pumpe)
- Korrosion Pumpenkopf-Material (Aluminium, wenn nicht anodisiert)
- Kleine Risse im Gussgehäuse (Fertigungsdefekt, Stoß, Vibration)

**Diagnose:**
- Leck-Stelle sichtbar machen: mit Tuch abtrocknen, einige Minuten laufen lassen, Wasser folgt Tropfen
- Leck-Ort markieren (z.B. mit Klebeband + Stift)
- Drucktest durchführen: Druck auf max. erhöhen (mit Druckmesser), Tropfmenge notieren
- Verschraubung prüfen: mit Schraubschlüssel leicht nachziehen (max. 1/4 Umdrehung ohne zu viel Kraft!)
- Dichtungszustand prüfen: Sichtprüfung, ggf. Ausbau und Kontrolle unter Lupe
- Material-Risse prüfen: mit Druckluft und Seifenlauge: Blasenbildung verrät Risse

**Sofortmaßnahmen:**
1. Druckwasser-Betrieb reduzieren (Druck auf Min-Wert senken wenn möglich)
2. Tuch unter Pumpe legen (Wasserschaden-Schutz)
3. Leck-Stelle markieren und täglich prüfen (Tropf-Menge schlimmer?)
4. Bei schnellem Leck (mehrere Tropfen/min): Betrieb einstellen, Backup-System aktivieren

**Reparatur:**
- **Verschraubung nachziehen:**
  - Mit Schraubschlüssel die Verschraubung leicht nachziehen (max. 1/4 Umdrehung)
  - Nicht zu viel Kraft (max. 20 Nm)
  - Prüfung durchführen (sollte tropfen stoppen)
  - Kosten: 0 EUR
- **Dichtung austauschen:**
  - Pumpe abbauen oder Schlauch abklemmen (Druckentlastung!)
  - Pumpenkopf-Verschraubung öffnen (Schraubschlüssel + evtl. Steckerklasse)
  - Alte Dichtung entfernen (mit Messer/Kratzer, Reste mit Alkohol abwischen)
  - Neue Dichtung einsetzen (Material: FKM/Viton für Salzwasser, EPDM für Süßwasser)
  - Gewindegänge mit PTFE-Tape einwickeln (2–3 Lagen, Wicklung im Uhrzeigersinn)
  - Verschraubung wieder anziehen (ca. 15–20 Nm)
  - Drucktest durchführen
  - Kosten Material: 15–40 EUR | Arbeit: 100–150 EUR
- **Pumpenkopf ersetzen (bei Rissen):**
  - Kompletter Aus-/Umbau erforderlich
  - Neuer Pumpenkopf: 150–400 EUR (je nach Typ)
  - Arbeitszeit: 300–500 EUR
  - **Alternativ:** komplette Pumpe austauschen (€400–1500)

**Prävention:**
- Druckschalter-Sollwert überprüfen (nicht >2 bar für Standard-Pumpen)
- Alle Verschraubungen alle 6 Monate nachprüfen (vibration-Check)
- Dichtungen alle 2–3 Jahre prophylaktisch austauschen
- Pumpen-Vibrationen isolieren (gummierte Halterung, nicht direkt auf Stahlrahmen)
- Salzwasser-Umgebung: jährlich mit Süßwasser abspülen

**Kostenrahmen EUR:**
- Dichtungs-Austausch: 15–40 (Material) | 100–150 (Arbeit)
- Pumpenkopf-Erneuerung: 150–400 (Teil) | 300–500 (Arbeit)
- Komplette Pumpe: 400–1500
- Gesamtbudget für Reparatur: 150–500 | Neukauf: 400–1500

---

### FB-24-05-008: Macerator blockiert

**Schweregrad:** Kritisch (keine Entleerung möglich) | Umwelt-Risiko

**Symptome:**
- Toilettenspülung funktioniert nicht (Wasser läuft nicht ab)
- Backflow in Toilettenschüssel (Wasser kommt rückwärts hoch)
- Macerator-Motor läuft, aber kein Durchfluss
- Starker unangenehmer Geruch
- Schleif-/Klopf-Geräusche aus Macerator (Schaufeln schlagen gegen Blockade)

**Ursachen:**
- Feuchttücher in Schüssel (auch "spülbar" -Typ)
- Windeln, Damenhygieneprodukte
- Papierhandtücher (zerfallen nicht wie Toilettenpapier)
- Plastik-Objekte (Verschlussdeckel, Verschluss-Clips)
- Haare (Verwicklung mit Papier zu Knoten)
- Sediment/Kalk-Ablagerungen bei Süßwasser-Systemen
- Zahnseide (wickelt sich um Schaufeln)

**Diagnose:**
- Toiletten-Wasserspiegel beobachten: bleibt konstant = Blockade vorhanden
- Macerator-Geräusche: normales Rattern vs. dumpfes Klopfen/Kratzgeräusche
- Visualprüfung: mit Taschenlampe in Toilettenschüssel leuchten (Fremdkörper sichtbar?)
- Druck-Test: Druckluft-Pumpe in Tank füllen und prüfen (sollte Widerstand spüren wenn blockiert)
- Manuelle Prüfung (wenn zugänglich): Pumpenschlauch abklemmen und durchblicken (Blockade sichtbar?)

**Sofortmaßnahmen:**
1. **Nicht spülen** (verstärkt Blockade nur)
2. Alle Toiletten/Sinks stillstellen (Wasser nicht verwenden)
3. Wenn Kabinenbereich: alle Hähne/Ventile schließen
4. Not-Entleerung: mobiler Vakuum-Tank oder externe Absaugung anforder, wenn Blockade hartnäckig

**Reparatur:**
- **Blockade entfernen (Schritt-für-Schritt):**
  1. Macerator-Stromversorgung ausschalten (Breaker/Sicherung)
  2. Druckentlastung: Tank-Ventil öffnen, Druckluft ablassen
  3. Macerator-Schlauch vom Ausgang abklemmen (Behälter bereit halten für Auslauf)
  4. Mit Stahlspirale (Rohrreiniger) vorsichtig in Macerator-Eingang fahren und blockade erfassen
  5. Langsam und vorsichtig zurückziehen (nicht zu viel Kraft, Schaufeln nicht beschädigen!)
  6. Blockade entfernen, danach mit Druckluft durchblasen
  7. Schlauch wieder anschließen, mit Wasser durchspülen
  8. Testlauf durchführen
  - Kosten (DIY): 30–50 EUR (Rohrreiniger) | Fachperson: 150–300 EUR
- **Wenn Blockade hartnäckig:**
  - Macerator ausbauen und demontieren
  - Schaufeln manuell frei prügeln (mit Holzhammer vorsichtig)
  - Mit Druckluft und Wasser durchspülen
  - Falls Schaufeln verbogen: ggf. ersetzen (~€80–150)
  - Macerator wieder montieren und prüfen
  - Kosten: 200–400 EUR
- **Wenn Macerator-Motor beschädigt:**
  - Kompletter Macerator-Austausch erforderlich
  - Neuer HMS Macerator: €800–1200
  - Ausbau/Einbau: 300–500 EUR

**Prävention:**
- **Strikte "Nur Toilettenpapier"-Regel** für alle an Bord (Beschilderung!)
- Regelmäßig Drainagecheck: alle 4–8 Wochen manuell prüfen
- Wöchentliche Spülkontrolle ohne Last durchführen
- Monatliche Wartung: Wasser + spezielle Macerator-Reinigungstabletten durchlaufen lassen (~€5 Kosten)
- Macerator-Filterpatrone alle 6–12 Monate tauschen (Sediment-Falle)
- Einweisung aller Crew-Mitglieder + Gast-Info auf Toilette befestigen

**Kostenrahmen EUR:**
- Rohrreiniger-Set (DIY): 30–50
- Fachperson Blockade-Entfernung: 150–300
- Schaufeln ersetzen: 80–150
- Macerator komplett austauschen: 800–1200 (Gerät) | 300–500 (Installation)
- Prävention (Reinigungstabletten/Jahr): ~50 EUR

---

### FB-24-05-009: Trockenlauf

**Schweregrad:** Kritisch (Pumpen-Zerstörung in <5 Minuten)

**Symptome:**
- Pumpe läuft, aber keine Wasser-Ausgabe
- Piepender/heulender Ton (Pumpe-Motor unter Last, aber kein Durchfluss)
- Pumpen-Gehäuse wird schnell sehr heiß (>50°C in <1min)
- Rauchwolke oder Brandgeruch (Motor wird überhitzt)
- Nach Trockenlauf: Pumpe startet nicht mehr

**Ursachen:**
- Wassertank leer (Süßwasser-System)
- Ansaugschlauch abgerissen oder abgeknickt
- Ansaugfilter völlig verstopft (kein Wasser kann passieren)
- Rückschlagventil im Ansaug verklemmt (schließt ab)
- Saugdruck zu hoch (Schlauch implodiert, kein Durchfluss trotz Saugversuch)
- Ansaugverbindung gelöst (Luft-Eintritt, Pumpe saugt nur Luft)

**Diagnose:**
- Wassertank sichtprüfen (Wasserspiegel sichtbar/meßbar?)
- Ansaugschlauch inspizieren (Beschädigungen, Abknickungen, Risse?)
- Ansaugfilter-Druckdifferenz prüfen (Manometer am Ein- und Ausgang: Differenz >0.3 bar = verstopft)
- Hand über Ansaug-Schlauch-Ende: sollte Saugkraft spürbar sein (wenn nicht: Blockade oder offene Verbindung)
- Motor-Stromaufnahme messen: ohne Last <1A, unter Trockenlauf-Last >2–3A (Problem-Indikator)
- Temperatur-Prüfung: Wärmebildkamera oder Hand-Prüfung am Gehäuse

**Sofortmaßnahmen:**
1. **Pumpe SOFORT abschalten** (Breaker/Sicherung ausschalten)
2. Wassertank auffüllen oder alternative Wassers-Quelle anschließen
3. Ansaugschlauch inspizieren und reparieren (Abknickung beheben, Risse abdichten)
4. Ansaugfilter reinigen oder austauschen
5. Warten bis Pumpe auf Raumtemperatur abgekühlt ist (mind. 30min)
6. Langsam neu starten (mit Wasserzuführung testen)

**Reparatur:**
- **Wasserzuführung wiederherst:**
  - Wassertank auffüllen
  - Ansaugschlauch auf Beschädigungen prüfen (bei Beschädigungen: Schlauch-Abschnitt austauschen, ~€20–50)
  - Ansaugfilter reinigen (Wasser ausspülen, Sediment entfernen) oder austauschen (~€30–80)
  - Ansaugverbindung prüfen und fest anschlißen (Hand-Drehung, evtl. Zange)
- **Pumpe nach Trockenlauf prüfen:**
  - Motor-Prüfung: Stromaufnahme bei Lasttest (sollte auf Normal-Wert zurückgehen)
  - Druck- und Durchfluss-Test durchführen
  - Geräusche abhören (sollten wieder normal sein)
  - Temperatur im Betrieb prüfen (sollte <40°C bleiben)
  - Kosten: 0 EUR (wenn nur Prüfung) | 100–200 EUR (Fachperson-Prüfung)
- **Wenn Motor beschädigt:**
  - Kompletter Pumpen-Austausch erforderlich (€400–1500)
  - Ggf. auch Kondensator/Steuerung beschädigt

**Prävention:**
- **Automatische Trockenluft-Abschaltung** einbauen (gibt es für Flojet/Shurflo)
  - Sensortyp: Durchfluss-Schalter oder Druckschalter mit Minimaldruck-Abschaltung
  - Kosten: ~€100–200
- Wassertank regelmäßig kontrollieren (täglich bei Fahrt)
- Ansaugfilter alle 50 Betriebsstunden inspizieren
- Ansauganlage alle 6 Monate durchspülen
- Betriebs-Log führen: Wassertank-Füllstand, Ansaugfilter-Status dokumentieren

**Kostenrahmen EUR:**
- Ansaugschlauch-Reparatur: 20–50
- Ansaugfilter-Austausch: 30–80
- Motor-Prüfung: 0 (DIY) | 100–200 (Fachperson)
- Trockenluft-Schutz-Einbau: 100–200
- Komplette Pumpe (Notfall): 400–1500

---

### FB-24-05-010: Vibration und Geräusche

**Schweregrad:** Mittel (Belästigung, Verschleiß-Beschleunigung)

**Symptome:**
- Lautes Rattern, Brummen oder Surren aus Pumpe
- Vibration der Halterung spürbar (wenn Hand aufgelegt)
- Geräuschlautstärke steigt über Zeit (progressive Verschlimmerung)
- Möbel oder Regal-Objekte vibrieren mit
- Geräusch-Frequenz ändert sich mit Druck (höhere Frequenz bei Druckaufbau)

**Ursachen:**
- **Hydraulische Ursachen:**
  - Luft im System (Kavitation, Gurgeln, pulsierendes Rattern)
  - Druckpulsation (Schaufelnfrequenz 50–200 Hz)
  - Druckwelle-Reflexion (Schlauch zu steif, Ventil zu schnell schaltend)
- **Mechanische Ursachen:**
  - Impeller-Verschleiß oder Unwucht (asymmetrische Verschleiß)
  - Schaufeln-Beschädigungen (berühren Gehäuse)
  - Lagerung verschlissen (Radial-Spiel zu groß)
  - Lockwelle-Verschleiß
- **Befestigungs-Ursachen:**
  - Halterung nicht fest (Schrauben gelockert)
  - Vibrationsausgleich fehlerhaft (Gummi-Element hart geworden)
  - Schlauch-Befestigung nicht isoliert (Schlauch überträgt Vibrationen direkt auf Rumpf)

**Diagnose:**
- **Frequenz-Analyse:**
  - Geräusch-Frequenz mit App oder Frequenz-Messer bestimmen
  - 50–200 Hz = wahrscheinlich hydraulische Pulsation
  - >500 Hz = eher mechanische Hochfrequenz (Lager, Impeller)
- **Vibrationsquelle lokalisieren:**
  - Mit Hand an verschiedenen Stellen der Pumpe fühlen (wo ist Vibration am stärksten?)
  - Schläuche berühren und beobachten (vibrieren sie mit?)
- **Luft-Test:**
  - Mit Seifenlauge alle Verbindungen prüfen (Blasen verraten Luft-Eintritt)
  - Ansaugbereich prüfen (von Wasser-Oberfläche bis Pumpen-Eingang)
- **Impeller-Sichtprüfung:**
  - Pumpe ausbauen, Impeller inspizieren (Beschädigungen, Asymmetrie, Verschleiß)
- **Lagerung-Test:**
  - Welle manuell schütteln (sollte kaum Spiel haben, <1mm)
  - Wenn Spiel >2mm: Lager/Welle verschlissen

**Sofortmaßnahmen:**
- Betriebsdruck senken (wenn möglich, um Pulsation zu reduzieren)
- Halterung-Schrauben nachziehen
- Schlauch-Routing prüfen: scharfe Kanten oder Spannungen vermeiden
- Gehör-Schutz tragen (bei längeren Einsätzen)

**Reparatur:**
- **Luft im System:**
  - Alle Verbindungen unter Druck auf Blasen prüfen
  - Undichte Stellen abditten (PTFE-Tape, Dichtpaste, ggf. Schlauch neu anschlißen)
  - Entlüftungsventil oben am höchsten Punkt öffnen und Wasser bis Leck-Stopp durchlaufen lassen
  - Kosten: 0–50 EUR
- **Druckpulsation dämpfen:**
  - Pulsations-Dämpfer (Akkumulator) einbauen direkt nach Pumpen-Ausgang
  - Schlauch nach Pumpe auf weniger starre Ausführung austauschen (z.B. SAE 100R2 statt R1)
  - Druck-Begrenzungs-Ventil sanfter kalibrieren (nicht zu steile Schaltflanke)
  - Kosten: 100–300 EUR
- **Impeller wechseln:**
  - Wenn Impeller-Verschleiß erkannt: Austausch durchführen (€80–200)
- **Lagerung austauschen:**
  - Pumpe demontieren, Welle + Lager prüfen
  - Wenn Lagerverschleiß: kompletter Pumpen-Austausch oder Instandsetzungs-Kit
  - Kosten: 200–400 EUR (Kit + Arbeit) | 400–1500 EUR (komplette Pumpe)
- **Halterung verbessern:**
  - Gummi-Schwinger-Elemente austauschen (sind verhärtet)
  - Aktive Vibrations-Isolation einbauen (Feder-Dämpfer-System)
  - Schlauch mit Vibrations-Isolations-Schellen befestigen
  - Kosten: 100–300 EUR

**Prävention:**
- Jährliche Vibrations-Kontrolle durchführen (Frequenz-Baseline dokumentieren)
- Halterung-Schrauben alle 3 Monate nachprüfen
- Gummi-Elemente alle 5 Jahre austauschen (verhärten)
- Schlauch-Routing alle 12 Monate inspizieren (keine scharfen Kanten)
- Druckschalter-Schaltflanke moderat kalibrieren (zu steile Flanke = mehr Pulsation)

**Kostenrahmen EUR:**
- Verbindungen abditten: 0–50
- Pulsations-Dämpfer: 100–300
- Impeller-Austausch: 80–200
- Lagerung/Mechanik-Reparatur: 200–400
- Komplette Pumpe: 400–1500
- Vibrations-Isolation: 100–300

---

### FB-24-05-011: Rückschlagventil defekt

**Schweregrad:** Mittel bis Hoch (Druckverlust, Rückfluss möglich)

**Symptome:**
- Druck fällt schnell nach Pumpen-Abschaltung ab (innerhalb 1–2min statt 5–10min)
- Wasser fließt rückwärts (merklich bei Bilge-Saugschläuchen: Wasser tritt unten aus)
- Ventil-"Klacker"-Geräusch hörbar (Ventil flattern von Öffnung/Schließung)
- Keine Rückströmungs-Begrenzung messbar (Drucktest mit Manometer zeigt Druckfall)
- Wasser kommt aus Rückschlag-Ventil-Ausgang obwohl Pumpe nicht läuft

**Ursachen:**
- **Kalk/Sediment-Ablagerungen:**
  - Lockere Partikel blockieren Ventilsitz
  - Verhindert vollständiges Schließen
- **Korrosion (besonders Salzwasser):**
  - Ventilkugel/Kegel rostet und haftet nicht mehr
  - Ventilsitz korrodiert, dichtet nicht mehr ab
- **Verschleiß des Ventilsitzes:**
  - Nach Jahren Hin-Her-Bewegung wird Sitz rau
  - Kugel/Kegel sitzt nicht mehr dicht
- **Fremdkörper:**
  - Sand, Sediment, Rostschuppe blockiert Ventil
  - Verhindert Schließen
- **Zu schnelle Druckänderung:**
  - Druckschalter schließt zu abrupt
  - Erzeugt Druck-Stoß, der Ventil beschädigt

**Diagnose:**
- **Druckfall-Test:**
  - Pumpe 2min laufen lassen bis Solldruck
  - Pumpe abschalten
  - Druckmesser ablesen jedes Min: sollte max. 0.5 bar in 5min fallen
  - Wenn Druck in <1min um >1 bar fällt = Rückschlag-Ventil verdächtig
- **Visuelle Prüfung:**
  - Rückschlag-Ventil ausbauen (Schläuche abklemmen, Sicherheitsventil öffnen)
  - Ventil aufschneiden (zwei-teiliges Design meist mit Schraube zusammen)
  - Kugel/Kegel inspizieren (Verschleiß? Korrosion? Verschmutzung?)
  - Sitz inspizieren (raue Oberfläche? Kratzer? Unebenheit?)
- **Funktionsprüfung manuell:**
  - Ventil in eine Hand nehmen
  - Von einer Seite leicht Luft pusten (sollte blockiert sein)
  - Von anderer Seite Luft pusten (sollte leicht durchgehen)
  - Umgekehrtes Verhalten = Ventil defekt

**Sofortmaßnahmen:**
- Druckwasser-System mit manueller Pumpe oder externem Speicher-Tank betreiben (bypass Rückschlag-Ventil temporär wenn möglich)
- Druckabfall akzeptieren und häufiger Pumpe aktivieren (lästig aber funktioniert)
- Bei Bilge: Backup-Bilge-Pumpe einschalten

**Reparatur:**
- **Rückschlag-Ventil reinigen:**
  - Ventil ausbauen (Schläuche abklemmen, Schrauben lösen)
  - Mit Essig/Zitronensäure einweichen (12–24h) um Kalk/Korrosion zu lösen
  - Öffnen und Kugel/Kegel mit weicher Bürste oder Tuch polieren
  - Ventilsitz mit feiner Feile polieren (max. 0.1mm Material)
  - Mit Druckluft durchpusten um Partikel zu entfernen
  - Neu zusammenbauen und Funktionsprüfung durchführen
  - Kosten: 0 EUR (DIY) | 80–150 EUR (Fachperson)
- **Ventilsitz nachschleifen:**
  - Wenn Verschleiß-Kratzer erkannt: professionelles Nachschleifen durch Reparaturwerkstatt
  - Kosten: 100–200 EUR
- **Rückschlag-Ventil austauschen:**
  - Typ identifizieren (Größe, Schlauch-Anschluss, Durchfluss-Rating)
  - Neues Ventil bestellen (z.B. Flojet RV-Typ: €60–120)
  - Altes ausbauen, neues mit PTFE-Tape einschrauben
  - Funktionsprüfung durchführen
  - Kosten: 60–120 EUR (Ventil) | 80–150 EUR (Arbeitszeit)

**Prävention:**
- Wasserfiltration vor Pumpe (5–20 µm) um Sediment zu reduzieren
- Alle 2–3 Jahre prophylaktisches Reinigen durchführen
- Druckschalter sanft kalibrieren (zu abrupte Schaltung = Druck-Stoß)
- Rückschlag-Ventile alle 5–7 Jahre aus Verschleiß-Gründen austauschen
- Jährliche Druckfall-Tests durchführen und dokumentieren

**Kostenrahmen EUR:**
- Reinigung: 0 (DIY) | 80–150 (Fachperson)
- Ventilsitz-Nachschleifen: 100–200
- Rückschlag-Ventil-Austausch: 60–120 (Ventil) | 80–150 (Arbeitszeit)
- Gesamtbudget: 150–400

---

### FB-24-05-012: Korrosion Pumpengehäuse

**Schweregrad:** Mittel bis Hoch (strukturelle Integrität, Leckage möglich)

**Symptome:**
- Sichtbare Rostflecken auf Aluminium-/Stahlgehäuse
- Oberflächenrauhheit (Pitting) unter 1mm tief
- Kleine Lecks an Rosti-Stellen (Wasser sickert durch Pitting)
- Salzverkrustung um korrodierte Stellen
- Gewicht-Zunahme (Rostschichten)

**Ursachen:**
- **Salzwasser-Exposition:**
  - Chlorid-Ionen dringen in Oberflächenschicht ein
  - Galvanische Korrosion zwischen verschiedenen Materialien
  - Mangelnde Oberflächenbeschichtung
- **Mangelnde Anoden-Schutz (Opferanode):**
  - Zink-Anoden nicht vorhanden oder verbraucht
  - Anoden-Kontakt unterbrochen (Korrosion nimmt zu)
- **Fehlerhafte Beschichtung:**
  - Lackierung beschädigt (Kratzer, Chips)
  - Eloxal-Schicht (bei Aluminium) unvollständig
  - Chromatierung fehlerhaft
- **Material-Unverträglichkeit:**
  - Kupfer-Rohre neben Stahl-Gehäuse (ohne Isoliernippel)
  - Messing-Anschlüsse direkt an Aluminium (ohne Übergangsmetall)
- **Feuchtigkeit/Salzspritzer:**
  - Pumpe nicht ausreichend geschützt
  - Steht direkt neben Salzwasser-Zirkulation
  - Kondensation im Bilgebereich

**Diagnose:**
- **Oberflächeninspektion:**
  - Mit Lupe und Taschenlampe inspizieren
  - Oberflächenrauhheit (Pitting) vs. oberflächliche Oxidation unterscheiden
  - Tiefenmessung mit Oberflächenrauheits-Messgerät oder Fühler-Lehre
- **Leckage-Test:**
  - Mit Seifenlauge an verdächtigen Stellen prüfen (Blasen verraten Pitting-Lecks)
  - Unter Druckbetrieb prüfen (Lecks deutlicher)
- **Material-Identifikation:**
  - Magnet-Test: Stahl magnetisch, Aluminium nicht
  - Oberflächenstruktur: Eloxal = schwarze/grüne Verfärbung, glatt; Rost = orange, rau
- **Wandstärke-Messung:**
  - Ultraschall-Dickenmessgerät nutzen um verbliebene Wandstärke zu prüfen
  - Sollte mind. 1.5 mm sein für Druckbereiche
  - Wenn <1mm: akute Ausfallgefahr

**Sofortmaßnahmen:**
- Pumpe unter Last betreiben (kein Trockenlauf um Wärmeschädigung zu vermeiden)
- Tuch unter Pumpe legen um frühe Lecks zu erkennen
- Tägliche Inspektionen durchführen
- Wenn Leck schnell wächst: Betrieb einstellen, Backup-System aktivieren

**Reparatur:**
- **Oberflächliche Oxidation (Pitting <0.5mm):**
  - Oberflächenrost mit Schleifbürste (80–120er Körnung) entfernen
  - Mit Stahlwolle (0000er) nachpolieren
  - Mit Alkohol abwischen um Schleif-Staub zu entfernen
  - Mit Korrosionsschutzöl (z.B. NLGI 2 Seefett) einölen
  - Danach: regelmäßig wöchentlich mit Öl abwischen
  - Kosten: 0 EUR (DIY) | 50–80 EUR (Fachperson)
- **Pitting mit Lecks (0.5–1.5mm):**
  - Korrodierte Fläche mit feiner Feile (200er) glattfeilen
  - Wenn Leck vorhanden: kleine Epoxy-Spachtelmasse auftragen und aushärten lassen
  - Mit feiner Feile nacharbeiten
  - Mit Metallversiegelungs-Lack anstreichen (z.B. 2K-Epoxy-Lack)
  - Kosten: 30–100 EUR (Material) | 100–200 EUR (Arbeitszeit)
- **Tiefe Pitting (>1.5mm) oder strukturelle Schwäche:**
  - Pumpe austauschen (nicht wirtschaftlich zu reparieren)
  - Neue Pumpe aus Corrosion-Resistant-Material auswählen (z.B. Edelstahl 316L oder eloxiertes Aluminium)
  - Kosten: 400–1500 EUR
- **Prävention nach Reparatur:**
  - Opferanode (Zink oder Aluminium) in Nähe der Pumpe installieren
  - Stromverbindung herstellen (sollte -0.8 bis -1.2V vs. Meerwasser messen)
  - Kosten für Anode-System: 150–300 EUR

**Prävention:**
- **Anoden-Überwachung:**
  - Opferanode alle 6 Monate inspizieren (sollte verzehrt sein, nicht die Pumpe)
  - Anode austauschen wenn >50% verbraucht
  - Kosten pro Anode: 50–100 EUR
- **Oberflächenschutz:**
  - Jährlich mit feiner Stahlwolle polieren + Schutzöl auftragen
  - Elektrolytische Mittel nutzen (z.B. Kathodischer Schutz-Modul)
  - Pumpe mit PVC-Schutzhaube abdecken wenn nicht in Betrieb
- **Material-Auswahl:**
  - Neue Pumpen: Edelstahl 316L oder Duplex-Stahl bevorzugen
  - Bei Anschlüssen: Isoliernippel zwischen verschiedenen Metallen nutzen
  - Kosten für hochwertige Pumpe: 600–2000 EUR (aber >10 Jahre Lebensdauer)
- **Umgebungs-Kontrolle:**
  - Bilgebereich regelmäßig mit Süßwasser ausspülen (Salzwasser-Rückstände entfernen)
  - Pumpe in trockenem Bereich montieren wenn möglich
  - Lüftung im Engine Room überprüfen (Feuchtigkeit reduzieren)

**Kostenrahmen EUR:**
- Oberflächenpolieren + Schutzöl: 0–80
- Pitting-Reparatur (Spachtel + Lackierung): 30–300
- Opferanode-System: 150–300
- Komplette Pumpe (korrosion-resistent): 600–2000
- Jährliche Präventivwartung: 50–150

---

## 7. Troubleshooting-Leitfaden — Entscheidungsbäume

### DT-1: Pumpe startet nicht

```
START: Pumpe reagiert nicht auf Einschaltbefehl
│
├─ [Stromversorgung prüfen] → Keine Spannung angemessen
│  ├─ Batterie prüfen (Voltmeter: sollte >12V bei 12V-System sein)
│  │  ├─ JA → Sicherung/Breaker prüfen
│  │  │   ├─ Sicherung durchgebrannt → Neue Sicherung (richtige Amperage!)
│  │  │   └─ Breaker ausgelöst → Zurücksetzen, erneut testen
│  │  └─ NEIN (Batterie <10V) → Batterie laden oder austauschen
│  │
│  └─ Kabelverbindung prüfen (Kontakte sichtprüfen, mit Ohmmeter durchgang testen)
│     ├─ Korrodierte Kontakte → Kontakte reinigen (Sandpapier, Kontaktfett)
│     └─ Kabel beschädigt → Kabel austauschen oder Lötstelle neu machen
│
├─ [Schaltrelais prüfen] → Relais klickt nicht oder klickt, Motor läuft nicht
│  ├─ Ohmmeter-Test: Spule prüfen (sollte 20–200 Ω haben)
│  │  ├─ JA (Relais reagiert auf Betätigung) → Motor-Problem (siehe unten)
│  │  └─ NEIN (Relais reagiert nicht) → Relais austauschen
│  │
│  └─ Druckschalter mit Hand betätigen (Sollte Relais auslösen)
│     ├─ Relais klickt → Problem liegt bei Druckschalter (manuell Einschalt-Befehl OK)
│     └─ Relais nicht betätigen → Druckschalter-Kabel prüfen, oder Relais-Spule defekt
│
└─ [Motor-Problem] → Motor startet nicht obwohl Strom anliegt
   ├─ Motor von Hand drehen (sollte leicht gehen)
   │  ├─ JA, dreht sich leicht → Elektrischer Fehler: Motor-Kondensator prüfen
   │  │  ├─ Kondensator defekt (Wölbung, Leck) → Austauschen (~€20–40)
   │  │  └─ Spulen-Durchgang prüfen mit Ohmmeter (sollte <100 Ω sein)
   │  │
   │  └─ NEIN, kann nicht drehen → Mechanische Blockade
   │     ├─ Fremdkörper in Pumpenkammer → Ausbauen und blockade entfernen
   │     ├─ Impeller läuft trocken (war letztem Einsatz ohne Wasser) → Ausbauen und Impeller freigeben
   │     └─ Motorlager blockiert → Lager-Instandsetzung oder komplette Pumpe austauschen
   │
   └─ [ENDE] → Pumpe startet jetzt, oder Austausch erforderlich

END-Punkte:
- Pumpe funktioniert ✓
- Sicherung: 5–10 EUR
- Relais: 50–120 EUR
- Kondensator: 20–40 EUR
- Komplette Pumpe: 400–1500 EUR
- Arbeitszeit: 100–300 EUR
```

### DT-2: Kein oder zu wenig Druck

```
START: Druck <0.5 bar oder fällt schnell ab
│
├─ [Wassertank prüfen]
│  ├─ Tank leer → Wasser auffüllen
│  ├─ Tank voll → Weiter unten
│  └─ Wasserspiegel nicht sichtbar (verschmutzt) → Ansaugfilter reinigen
│
├─ [Ansaugfilter prüfen]
│  ├─ Sichtbar verschmutzt (dunkelbraun/orange) → Ausspülen oder austauschen
│  │  ├─ DIY Reinigung: Wasser abgießen, Sediment entfernen, mit Süßwasser spülen
│  │  └─ Austausch: neuer Filter (€30–80)
│  └─ Filter sauber → Weiter unten
│
├─ [Ansaugleitung prüfen]
│  ├─ Luftlecks (Seifentest durchführen) → Lecks abdichten
│  │  ├─ Schlauch-Risse: Abschnitt austauschen (€20–50)
│  │  └─ Verbindungen locker: nachziehen oder neu abdichten
│  ├─ Schlauch geknickt → Schlauch gerade legen oder austauschen
│  └─ Schlauch priming: Hand über Ansaug-Schlauch halten (sollte Saugkraft spüren)
│     ├─ NEIN (keine Saugkraft) → Blockade oder Rückschlag-Ventil-Problem
│     └─ JA → Weiter unten
│
├─ [Rückschlag-Ventil prüfen]
│  ├─ Ventil ausbauen und manuell prüfen
│  │  ├─ Ventil sitzt fest (blockiert) → Mit Essig einweichen und reinigen
│  │  ├─ Ventil öffnet nicht leicht → Venilmembran/Kegel beschädigt → Austausch (€60–150)
│  │  └─ Ventil OK, öffnet und schließt leicht → Weiter unten
│
├─ [Impeller-Verschleiß prüfen]
│  ├─ Impeller sichtbar abgeflacht oder gerissen → Austausch (€80–200)
│  │  ├─ Leichte Abnutzung: mit feiner Feile polieren
│  │  └─ Starker Verschleiß: austauschen
│  └─ Impeller sauber → Weiter unten
│
├─ [Druckschalter prüfen]
│  ├─ Druck messer zeigt 0.5–1.5 bar → Druckschalter-Ansprechpunkt verstellt
│  │  ├─ Druckschalter neu kalibrieren (auf 2.0 bar setzen für Standard-Systeme)
│  │  └─ Wenn nicht möglich: Austausch (€80–180)
│  └─ Manometer stimmt mit Erwartung überein → Pumpe OK
│
└─ [Rohre/Leitungen prüfen]
   ├─ Verkalkung oder Biofilm (besonders Warmwasser-Leitungen) → Mit Essig durchspülen
   ├─ Fremdkörper sichtbar → Druckluft durchblasen oder Leitung austauschen
   └─ Alle Leckagen inspizieren (Seifentest) → Lecks abdichten oder Rohre neu verschrauben

END-Punkte:
- Druck wiederhergestellt ✓
- Ansaugfilter: 30–80 EUR
- Impeller-Austausch: 80–200 EUR
- Rohrreinigung: 0–300 EUR
- Rückschlag-Ventil: 60–150 EUR
- Arbeitszeit: 150–500 EUR
```

### DT-3: Pumpe schaltet nicht ab

```
START: Pumpe läuft kontinuierlich, Druck über Schaltpunkt
│
├─ [Druckschalter prüfen]
│  ├─ Manuell betätigen → Schalter sollte Klick machen
│  │  ├─ JA (Klick hörbar) → Schalter OK, Problem liegt anderswo
│  │  └─ NEIN (kein Klick) → Druckschalter reagiert nicht
│  │     ├─ Kontakte verschweißt → Reinigen (Feile, Kontakt-Poliertuch)
│  │     └─ Feder gespannt → Feder nachspannen oder Schalter austauschen (€80–180)
│  │
│  └─ Stromkreis-Prüfung (Ohmmeter)
│     ├─ Schalter offen (∞Ω) bei manueller Betätigung → Kontaktverschleiß, Austausch erforderlich
│     └─ Schalter geschlossen (<1Ω) immer → Kontakt festgeklemmt, reinigen oder austauschen
│
├─ [Durchfluss-Schalter prüfen] (falls vorhanden)
│  ├─ Durchfluss-Schalter-Kontakt mit Ohmmeter prüfen
│  │  ├─ Kontakt offen wenn Wasser fließen sollte → Schalter verschlissen oder blockiert
│  │  └─ Kontakt bleibt geschlossen → Durchfluss-Schalter defekt → Austausch (€40–100)
│
├─ [Leckagestelle prüfen] (häufigste Ursache!)
│  ├─ Mit Seifenlauge alle Verbindungen unter Druck prüfen
│  │  ├─ Blasen sichtbar → Leckage identifiziert!
│  │  │  ├─ Verschraubung locker → nachziehen (max. 1/4 Umdrehung)
│  │  │  ├─ Dichtung defekt → Dichtung austauschen oder Schlauch neu anschließen
│  │  │  └─ Leck-Stelle unter Kontrolle (langsamer Tropf) → Tuch unter Pumpe, tägliche Überwachung
│  │  └─ NEIN (keine Blasen) → Weiter unten
│  │
│  └─ Druckabfall-Test durchführen
│     ├─ Pumpe abschalten, Druckmesser beobachten
│     ├─ JA (Druck fällt in <2min deutlich) → Rückschlag-Ventil defekt oder Leck vorhanden
│     │  ├─ Rückschlag-Ventil ausbauen und reinigen (€0–150)
│     │  └─ Wenn nicht erfolgreich: Ventil austauschen (€60–150)
│     └─ NEIN (Druck bleibt >1h) → Druck-Haltung OK
│
└─ [Akkumulator-Problem]
   ├─ Falls Akkumulator vorhanden: Luftdruck prüfen
   │  ├─ Luftdruck <0.5 bar → Membran ist gerissen oder defekt
   │  │  └─ Akkumulator-Membran austauschen oder kompletten Akkumulator ersetzen (€150–400)
   │  └─ Luftdruck OK (0.7–1.0 bar) → Akkumulator funktioniert
   │
   └─ Wenn alle anderen Punkte OK → Druckschalter Ansprechpunkt zu hoch
      └─ Schalter neu kalibrieren (auf korrekten Punkt setzen) oder austausch

END-Punkte:
- Pumpe schaltet jetzt ab ✓
- Dichtung austausch: 15–40 EUR
- Rückschlag-Ventil: 60–150 EUR
- Druckschalter: 80–180 EUR
- Akkumulator: 150–400 EUR
- Arbeitszeit: 150–400 EUR
```

### DT-4: Ungewöhnliche Geräusche

```
START: Rattern, Brummen, Piepen, Schleifen oder Knacken
│
├─ [Geräusch-Typ identifizieren]
│  │
│  ├─ Leises kontinuierliches Brummen (normal?) → Vibrations-Kontrolle durchführen
│  │  ├─ Mit Hand an Pumpe fühlen: Vibration leicht oder stark?
│  │  │  ├─ Leicht (normal) → OK, nichts zu tun
│  │  │  └─ Stark → Weiter unten bei "Vibration stark"
│  │  └─ Geräusch andere Frequenz als Motor-Standard → Druckpulsation (siehe unten)
│  │
│  ├─ Rattern oder Schleif-Geräusche → Mechanischer Verschleiß
│  │  ├─ Impeller-Verschleiß oder Blockade prüfen
│  │  │  └─ Impeller inspizieren (ausbauen) → Reparatur oder Austausch
│  │  ├─ Lagerung prüfen (mit Hand schütteln, sollte <1mm Spiel haben)
│  │  │  └─ Zu viel Spiel → Lager-Austausch oder komplette Pumpe
│  │  └─ Fremdkörper im Gehäuse?
│  │     └─ Ausbauen und inspizieren
│  │
│  ├─ Piependen Ton (akustisch unauffällig) → Höchstwahrscheinlich Trockenlauf!
│  │  ├─ Sofort Pumpe abschalten!
│  │  ├─ Wassertank prüfen (sollte voll sein)
│  │  ├─ Ansaugfilter inspizieren
│  │  └─ Ansaugleitung auf Luftlecks prüfen
│  │     (siehe Trockenlauf-Maßnahmen FB-24-05-009)
│  │
│  ├─ Knackendes oder Klackerndes Geräusch → Druckpulsation oder Ventil-Flattern
│  │  ├─ Rückschlag-Ventil ausbauen und prüfen (sollte nicht flattern)
│  │  ├─ Druckschalter Schaltflanke prüfen (zu abrupt = Knacken)
│  │  └─ Pulsations-Dämpfer (Akkumulator) einbauen wenn fehlend
│  │
│  └─ Heul-Ton oder piependes Durchdrehen → Impeller-Blockade
│     ├─ Impeller inspizieren (verschlissen oder blockiert?)
│     └─ Austausch erforderlich
│
├─ [Halterung und Befestigung prüfen]
│  ├─ Halterungs-Schrauben mit Schraubenschlüssel nachziehen
│  ├─ Schläuche vibrieren? → Mit isolierten Schellen befestigen
│  ├─ Gummi-Isolations-Elemente verhärtet?
│  │  └─ Austausch (€50–100)
│  └─ Schlauch-Routing überprüfen (nicht an harten Kanten)
│
├─ [Luft im System?]
│  ├─ Seifenlauge an allen Ansaug-Verbindungen auftragen
│  │  ├─ Blasen sichtbar → Undichte Stelle gefunden!
│  │  │  └─ Luftleck abdichten (PTFE-Tape, Dichtpaste, Schlauch austauschen)
│  │  └─ Keine Blasen → Weiter unten
│  │
│  └─ Entlüftungsventil am höchsten Punkt öffnen
│     └─ Luft auslaufen lassen, dann mit Wasser durchspülen
│
├─ [Vibrationen stark]
│  ├─ Vibrations-Frequenz messbar mit App/Messgerät?
│  │  ├─ <200 Hz → Hydraulische Pulsation (Druckwelle)
│  │  │  └─ Pulsations-Dämpfer einbauen (€100–300)
│  │  ├─ 200–500 Hz → Impeller-Unwucht
│  │  │  └─ Impeller austausch (€80–200)
│  │  └─ >500 Hz → Lagerschaden
│  │     └─ Komplette Pumpen-Reparatur/Austausch erforderlich
│  │
│  └─ Aktive Vibrations-Isolationssystem einbauen?
│     └─ Kosten: €150–300
│
└─ [Nachprüfung]
   ├─ Nach jeder Reparatur Geräuschlautstärke vergleichen
   └─ Wenn Geräusch nicht abnimmt → spezialisierte Diagnose oder Austauch erforderlich

END-Punkte:
- Geräusche weg ✓
- Halterungs-Justage: 0–100 EUR
- Pulsations-Dämpfer: 100–300 EUR
- Impeller-Austausch: 80–200 EUR
- Gummi-Elemente: 50–100 EUR
- Komplette Pumpe: 400–1500 EUR
- Arbeitszeit: 100–400 EUR
```

### DT-5: Leckage an Pumpe

```
START: Wasser tropft aus Pumpe
│
├─ [Leck-Quelle lokalisieren]
│  ├─ Tropfen mit Tuch abwischen und Farbe beobachten
│  │  ├─ Salzverkrustung vorhanden → Salzwasser (Meerwasser-Kühlsystem oder Bilge)
│  │  └─ Klares Wasser → Trinkwasser (Druckwasser-System)
│  │
│  ├─ Leck-Stelle mit Markierungsstift kennzeichnen
│  │
│  └─ Leck-Ort identifizieren
│     ├─ Pumpenkopf-Naht (unterhalb Schlauch-Anschluss) → siehe FB-24-05-007
│     ├─ Pumpen-Flansch (wo Impeller sitzt) → Überdruckbetrieb oder Dichtungs-Verschleiß
│     ├─ Leck-Loch in Gehäuse-Wand → Korrosion-Pitting → siehe FB-24-05-012
│     ├─ Schlauch-Verbindung → Verbindung locker oder Schlauch-Riss
│     └─ Wellen-Durchgang (an Motor-Pumpen-Kupplung) → Wellendichtring defekt
│
├─ [Verschraubung prüfen] (häufigste Ursache!)
│  ├─ Mit Schraubenschlüssel Verschraubung leicht nachziehen
│  │  ├─ Ja (Leck stoppt) → OK, nicht zu fest anziehen!
│  │  └─ Nein (Leck bleibt) → Dichtung defekt, siehe unten
│  │
│  └─ Nicht zu viel Kraft anwenden! (max. 1/4 Umdrehung, ~20 Nm)
│
├─ [Schlauch prüfen]
│  ├─ Schlauch-Risse sichtbar → Schlauch-Abschnitt austauschen (€20–50)
│  ├─ Verbindungen locker (mit Hand drehen möglich) → Mit Zange nachziehen
│  └─ Schlauch älter >10 Jahre → Prophylaktischer Austausch empfohlen (€50–150)
│
├─ [Dichtung austauschen]
│  ├─ Druckwasser abbauen (Hahn öffnen, Druckentlastungs-Ventil)
│  ├─ Schlauch abklemmen oder Pumpe demontieren (je nach Design)
│  ├─ Alte Dichtung entfernen (mit Kunststoff-Kratzer, nicht Metall!)
│  ├─ Gewinde mit Alkohol + Tuch sauberen
│  ├─ Neue Dichtung einsetzen (FKM/Viton für Salzwasser, EPDM für Süßwasser)
│  ├─ Gewinde mit PTFE-Tape wickeln (2–3 Lagen im Uhrzeigersinn)
│  ├─ Verschraubung neu anziehen (ca. 15–20 Nm mit Drehmoment-Schlüssel)
│  ├─ Drucktest durchführen → sollte kein Tropf nach 5min
│  └─ Kosten: Dichtung 10–30 EUR | Arbeit 100–150 EUR
│
├─ [Überdruckbetrieb prüfen]
│  ├─ Druckmesser anschrauben und Betriebsdruck prüfen
│  │  ├─ >2.5 bar bei 2-bar-Pumpe → Overload!
│  │  │  ├─ Druckschalter-Ansprechpunkt senken (auf 2.0 bar)
│  │  │  └─ Sicherheits-Überdruckventil prüfen (sollte bei 2.5 bar öffnen)
│  │  └─ Druck OK (<2.0 bar) → siehe Dichtungs-Reparatur oben
│
├─ [Wellendichtring prüfen] (Motor-Kupplungs-Bereich)
│  ├─ Leck direkt am Motor-Pumpen-Übergang
│  │  ├─ Wellendichtring ausbauen + austauschen (€50–120)
│  │  ├─ Arbeitszeit: 150–250 EUR
│  │  └─ Oder: komplette Pumpe austauschen (€400–1500)
│
├─ [Korrosion-Pitting] (Leck-Loch im Gehäuse)
│  ├─ (siehe FB-24-05-012 für Reparatur-Optionen)
│  ├─ Kleine Lecks (<1 Tropf/min): Epoxy-Spachteln + Lackierung
│  │  └─ Kosten: €30–100
│  └─ Größere Lecks: Pumpe austauschen (€400–1500)
│
└─ [Nachprüfung]
   ├─ Nach jeder Reparatur mind. 30min laufen lassen
   ├─ Tropf-Menge dokumentieren (sollte 0 sein)
   └─ Tägliche Kontrolle erste Woche durchführen

END-Punkte:
- Leck behoben ✓
- Verschraubung nachziehen: 0 EUR
- Dichtung austausch: 10–30 EUR (Material) | 100–150 EUR (Arbeit)
- Schlauch-Austausch: 20–50 EUR
- Wellendichtring: 50–120 EUR (Teil) | 150–250 EUR (Arbeit)
- Komplette Pumpe: 400–1500 EUR
- Gesamtbudget: 100–800 EUR
```

---

## 8. FAQ — Häufig Gestellte Fragen

**F-001: Wie oft sollte eine Druckwasserpumpe gewartet werden?**
A: Alle 6 Monate Sichtprüfung, jährlich Funktionsprüfung (Druck/Durchfluss testen), alle 3–5 Jahre prophylaktische Komponenten-Überholung (Dichtungen, Impeller). Bei Salzwasser-Exposition: 3-monatliche Kontrollen.

**F-002: Kann man eine 24V-Pumpe auf 12V betreiben?**
A: Nein, nicht sicher. Stromaufnahme verdoppelt sich (~2x), Leitungsquerschnitte überlastet, Batterien schneller entladen, Wärmeerzeugung. Neuanschaffung mit richtiger Spannung erforderlich.

**F-003: Wie prüft man die Batterie-Spannung richtig?**
A: Ohmmeter im Voltmeter-Modus (20V DC Bereich). Messspitzen direkt an Batterie-Pollen ansetzen (nicht an Kabel-Enden). Sollte bei 24V-System ~24–27V zeigen (24V nominal, bis 28V beim Laden). Bei <21V: Batterie laden oder austauschen.

**F-004: Warum schließt sich die Drucktoilette nicht ab?**
A: Macerator blockiert (siehe FB-24-05-008), oder Druckausfall (siehe Druckschalter-Fehler). Prüfung: Hahn öffnen → sollte Wasser kommen. Wenn nicht: Druckwasser-System prüfen.

**F-005: Bilgepumpe läuft ständig — ist das normal?**
A: Nein. Sollte nur starten wenn Wasser im Bilge-Sumpf über Schwimmer-Schalter steigt. Dauerlauf deutet auf Leck (Wasser sickert rein) oder Schwimmer-Fehler. Sichtprüfung durchführen und Leck-Quelle suchen.

**F-006: Kann man Salzwasser direkt zum Spülen nutzen?**
A: Ja, aber nur für Toiletten. Niemals für Duschen/Küche (Korrosion, Geschmack). Separate Salzwasser-Leitung erforderlich mit entsprechender Kennzeichnung (rote Schläuche, deutliche Beschriftung).

**F-007: Greywater-Tank ist voll — kann man einfach überlaufen lassen?**
A: Umweltschutz: NEIN. Überboard-Ablassung ist in vielen Gewässern illegal. Tank muss geleert werden (Hafen-Pumpout oder zertifizierte Entsorgung). Notfalls externe Absaugung anforder.

**F-008: Welche Temperatur ist zu heiß für Druckwasser?**
A: >45°C kann Dichtungen und Impeller-Material schädigen. Sollte <40°C bleiben während Betrieb. Wenn heißer: Kühlsystem überprüfen oder Betrieb reduzieren.

**F-009: Wie viel Druck ist normal für Dusche?**
A: Mindestens 1.5 bar (besser 2.0 bar) für spürbaren Strahl. Unter 1.0 bar: Druck zu niedrig (Druckschalter-Sollwert prüfen oder Impeller verschlissen).

**F-010: Kann man Schlauch einfach auf Schlauch stecken ohne Schelle?**
A: Nein, nicht sicher. Vibration oder Druck → Schlauch rutscht ab. Mindestens 2 Edelstahl-Schellen pro Verbindung erforderlich (einmal vor, einmal nach Verbindungs-Punkt).

**F-011: Frischwasser-Betankung: sauberes Wasser oder desinfizieren?**
A: Beides. Immer mit Schlauch-Filter (Sediment-Filter 20µm) betanken. Danach mit Chlortabletten desinfizieren (0.5–1.0 ppm) oder Wassertank jährlich spülen mit Wasserstoffperoxid.

**F-012: Wie erkennt man einen Wasserschaden früh?**
A: Tägliche Bilge-Kontrolle durchführen (Wasser sollte min. sein). Wenn Bilge nach <2h Fahrt feucht: Leck vorhanden. Alle sichtbaren Rohre/Schläuche inspizieren.

**F-013: Kann man Bilgepumpe manuell bedienen wenn Motor ausfällt?**
A: Ja, mit manueller Bilge-Pumpe als Backup. Sollte an Bord sein (€50–150). Aber: abhängig von Wassermenge und Kraft des Steuermanns.

**F-014: Darf man die Toilette in Häfen nutzen?**
A: Ja, aber Tank muss geleert werden bevor Hafen verlassen wird (lokale Vorschriften beachten). Nicht alle Häfen haben Pump-Out-Stationen → vorausplanen!

**F-015: Was ist eine "defekte" Dichtung genau?**
A: Risse, Verhärtung (Material spröde), Verformung (sitzt nicht mehr dicht), Ölrausch (Verschleiß-Partikel drin). Optisch: nicht glatt, verfärbt, undicht wenn unter Druck.

**F-016: Kann man einen Macerator austauschen selbst?**
A: Technisch ja, aber erfordert: Rohrabbauten (Schläuche abklemmen), Stromverbindung trennen (Sicherung!), neuer Macerator einbauen, dicht verschrauben, Funktionsprobe. Kosten DIY: ~€1200–1500. Fachperson: €1500–2000 (mit Einbau).

**F-017: Wieso ist das Wasser braun/trübe?**
A: Rost oder Sediment im Tank. Lösung: Tank 2–3x komplett leeren und mit Süßwasser ausspülen. Inline-Filter (5–20 µm) einbauen um zukünftige Kontamination zu vermeiden.

**F-018: Kann man einen Akkumulator selbst auswechseln?**
A: Ja, relativ einfach. Alte Membran entfernen (Schraube lösen), neue einsetzen, Vordruck einstellen (Reifen-Druckmesser), Gehäuse wieder zusammenbauen. Kosten: ~€50–100 Zeit, Membran-Kit €150–300.

**F-019: Ist ein Druckausgleichs-Ventil notwendig?**
A: Ja für Druckwasser-Systeme. Wenn Druckschalter Schaltflanke zu steil ist, entstehen Druck-Stoße. Druckausgleichs-Ventil glättet diese (Kosten: €80–150).

**F-020: Wie oft sollten Schläuche ausgetauscht werden?**
A: Alle 5–10 Jahre je nach Material und Umgebung. Salzwasser = 5–7 Jahre. Süßwasser = 8–10 Jahre. Sichtzeichen: Verhärtung, Risse, Oxidation (Verfärbung) = Austausch fällig.

**F-021: Kann man auf eine teurere "Premium"-Pumpe downgraden?**
A: Nein, nicht sicher. Wichtig sind: Durchfluss-Leistung (l/min), Maximaldruck (bar), Stromaufnahme (A), Anschluss-Größe. Fallback auf billigere Pumpe nur wenn alle Spezifikationen übereinstimmen UND Backup-System vorhanden.

**F-022: Rückschlag-Ventil reparieren oder austauschen?**
A: Reparatur sinnvoll wenn Ventil weniger als 5 Jahre alt ist und Verschmutzung erkannt wurde. Älter als 5 Jahre oder mechanische Beschädigungen = Austausch billiger (€60–150 vs. 100–200 Reparatur).

**F-023: Kann man Glykol als Frostschutz nutzen?**
A: Ja, spezielles Boots-Glykol (nicht Auto-Glykol!) nutzen. Konzentration: 30–50% Glykol in Wasser. Vor der Winterlagerung durch gesamtes System pumpen, am Frühling wieder ausspülen mit Süßwasser.

**F-024: Wie erkennt man einen Motorschaden durch Trockenluft?**
A: Rauchentwicklung, Brandgeruch, Motor startet nicht mehr nach Trockenlauf. Wenn passiert: Sofort abschalten, Motor abkühlen lassen, professionelle Diagnose einholen (Wicklung durchmessen mit Ohmmeter). Ggf. Motor-Austausch erforderlich.

**F-025: Bilge-Alarm funktioniert nicht — was prüfen?**
A: Schwimmer-Schalter inspizieren (saubere Bewegung?), Stromversorgung prüfen (Spannung anleggen?), Relais-Betätigung testen (Ohmmeter), Alarm-Geber testen (akustisch/optisch). Wenn alles OK: Schwimmer oder Schaltwerk austauschen (€50–120).

---

## 9. Glossar — 40+ Begriffe

**Akkumulator** (Hydro-Speicher): Druckbehälter mit elastischer Membran. Speichert Druckenergie um Druck-Schwankungen auszugleichen und Pumpenzyklus zu verlängern. 10 L Standard.

**Ansaugfilter:** Eingang-Filterpatrone um Sediment vor Pumpe zu stoppen. 5–20 µm typisch. Regelmäßiger Austausch erforderlich.

**Ansaugleitung:** Schlauch/Rohr vom Wassertank zum Pumpen-Eingang. Muss luftdicht sein (Saugbetrieb!).

**Betriebsdruck:** Tatsächlicher Druck während Betrieb unter Last. Sollte unter Schalt-Sollwert bleiben.

**Bilge:** Unterster Punkt des Bootskörpers wo Lecks/Kondenswasser sammelt. Bilgepumpe entfernt diese kontinuierlich.

**Biofilm:** Mikrobische Schicht in Rohren (Algen, Bakterien). Reduziert Durchfluss und kann zu Geruchsproblemen führen.

**Blauern Wasser-System:** Unabhängiges Redundanzsystem mit mehreren Druckwasser-Pumpen im parallelen oder sequenziellen Betrieb. Professionelles Langfahrt-Standard.

**Bootsgewicht-Verteilung:** Schwerpunktlage des Boots (längs und quer). Wichtig für Stabilität und Pump-Dimensionierung (CG-Shift ändert Druck auf Druckwasserleitungen).

**Breaker (Schutzschalter):** Stromkreis-Schutzvorrichtung die bei Überlastung auslöst (anders als Sicherung nicht wiederverwendbar, zu zurücksetzen).

**Durchfluss (flow):** Wasser-Menge pro Zeiteinheit (l/min). Pumpen-Leistungsangabe.

**Druckausgleichs-Ventil:** Begrenzt Druckanstiegugeschwindigkeit um Druck-Stoße zu vermeiden.

**Druckentlastung:** Prozess zum Druckabbau vor Schlauch-Abbauten. Ventil öffnen oder Hahn aufdrehen.

**Druckmanometer:** Messinstrument um Systemdruck anzuzeigen (analog-Skala oder digital).

**Druckschalter:** Elektromechanisches Bauteil das Pumpe bei Erreichen von Sollwert ausschaltet (z.B. 2.0 bar = Pumpe Stop).

**Duschen-Sumpf:** Sumpf unter Dusche um Wasser zu sammeln (Bilge-artig). Ablassung über Sumpf-Pumpe.

**Edelstahl 316L:** Korrosionsbeständige Stahllegierung für Salzwasser-Anwendungen. "L" = Low Carbon (weniger Korrosionsanfälligkeit).

**Eloxal:** Anodischer Oxidations-Schutzschicht auf Aluminium. Schwarz/dunkelgrün gefärbt. Verhindert Korrosion.

**Entkalkungsmittel:** Chemikalien (Essig, Zitronensäure, spezialisierte Produkte) um Kalk-Ablagerungen zu lösen.

**EPDM:** Elastomer-Material für Dichtungen und Impeller. Standard für Süßwasser-Systeme.

**Fäkalien-System:** Toiletten-Abwasser-Management. Sammlung, Zerkleinerung (Macerator), Überboard-Ablassung oder Tank-Sammlung.

**FKM/Viton:** Premium-Elastomer für Dichtungen. Salzwasser- und temperatur-beständig.

**Flojet/Shurflo:** Populäre Pumpen-Hersteller. Flojet = Membran-Pumpen, Shurflo = Impeller- und Membran-Varianten.

**Fremdkörper:** Partikel (Sand, Algen, Zahnseide, Feuchttücher) die Pumpen blockieren können.

**Frischwasser-Betankung:** Prozess um Wassertank mit Trinkwasser aufzufüllen. Sollte mit Sediment-Filter durchgeführt werden.

**Funktionsprobe:** Test um sicherzustellen dass Pumpe unter Last funktioniert. Druck- und Durchfluss-Messung.

**Gelcoat:** Oberflächenschicht auf GFK-Rumpf. Schützt Laminat vor UV und Osmose-Blistering.

**Greywater:** Abwasser aus Duschen/Küche (nicht Fäkalien). Kann überboard ablassen oder in Tank sammeln.

**Grundlast:** Minimale kontinuierliche Stromaufnahme (z.B. Navigationslicht). Wichtig um Batterie-Entleerung zu planen.

**Halterung (mounting bracket):** Mechanische Vorrichtung um Pumpe am Rumpf/Schott zu befestigen. Sollte vibrations-isoliert sein.

**HMS Macerator:** Markenname für hochwertige Fäkalien-Zerkleinerungs-Pumpen (z.B. 2300, 2400 Serien).

**Hydraulisches Öl:** Spezialisiertes Öl in Akkumulatoren (Druckpuffer). Nicht dasselbe wie Motor-Öl!

**Hydrometer:** Messgerät um Salzgehalt von Wasser zu prüfen (grav./Dichte-basiert).

**Impeller:** Drehender Lüfter/Schaufel in Zentrifugal-Pumpen. Erzeugt Zentrifugalkraft um Wasser zu fördern.

**Inline-Filter:** Filterpatrone in der Leitung (nicht im Tank). Schützt Pumpe vor Sediment.

**Kalk-Ablagerung (scaling):** Mineralische Ausscheidung in heißen oder hartem Wasser. Reduziert Durchfluss.

**Kavitation:** Bildung von Dampfblasen in Pumpe wenn Saugdruck zu negativ wird. Kann zu Pumpen-Schäden führen.

**Kennzeichnung (labeling):** Farbliche oder Text-Kennzeichnung von Rohren um Wasser-Typ zu identifizieren (z.B. blaue Rohre = Süßwasser, rote = Salzwasser).

**Kopplungs-Verlust:** Energieverschwendung zwischen Motor und Pumpe (in Lager/Welle). Sollte <5% sein.

**Korrosion (galvanische):** Elektrochemischer Prozess wo unedleres Metall (z.B. Stahl) von edlerem (z.B. Messing) angegriffen wird.

**Kühlwasser-Kreislauf:** Seewasser-Pumpe um Motor zu kühlen. Separates System von Trinkwasser.

**Lagerung (bearing):** Mechanisches Element um Welle zu stützen. Axial (Druck) und Radial (seitwärts).

**LED-Indikator:** Elektrische Leuchte um Status anzuzeigen (grün = OK, rot = Fehler, orange = Warnung).

**Leck-Stelle:** Punkte wo Wasser unkontrolliert austritt. Sollte lokalisiert und abgedichtet werden.

**Leitungs-Querschnitt:** Innendurchmesser von Rohren/Schläuchen. Wichtig um Durchfluss-Geschwindigkeit im akzeptablen Bereich zu halten (<2 m/s ideal).

**Makerat (macerated):** Zerkleinerte Fäkalien/Greywater bevor sie ablaufen. Ermöglicht kleinere Ableitungs-Rohre.

**Membrane-Pumpe (diaphragm pump):** Arbeitet mit elastischer Membrane und zwei Rückschlag-Ventilen. Gut für Nieder-Druck-Anwendungen.

**Mindest-Betriebsdruck:** Druckschalter-Öffnungspunkt unten. Unter diesem Druck sollte Pumpe nicht arbeiten.

**Monitoren:** Kontinuierliche Beobachtung von Druck, Durchfluss, Temperatur mit Messinstrumenten.

**Mold (Schimmel):** Pilzbefall in feuchten Behältern/Rohren. Kann Geschmack und Gesundheit beeinträchtigen.

**Neutralisierung:** Chemische Behandlung um Säure/Base auszugleichen (z.B. Glykol-Entfernung vor Frühjahrs-Saison).

**Nickel-Legierung:** Hochwertige metallische Legierung für Korrosionsschutz (teuer, selten in Standard-Anwendungen).

**Notbetrieb (emergency operation):** Manuelles oder degradiertes Betrieb wenn Hauptsystem ausfällt. Z.B. manuelle Bilge-Pumpe.

**Öffnungspunkt:** Druckwert bei dem Druckschalter Kontakt öffnet und Pumpe stoppt.

**Opferanode:** Metallstück (meist Zink) das absichtlich korrodiert um andere Metalle zu schützen. Teil der kathodischen Schutz-Strategie.

**Osmose-Blistering:** Physikalisches Phänomen wo GFK-Laminat Wasser aufnimmt und Blaupunkte entsteht. Normale Verschleiß, nicht kritisch wenn <5mm.

**Overload:** Zu viel Last auf System (z.B. Druck >max Sollwert). Kann zu Beschädigungen führen.

**Parametrische Analyse:** Mathematisches Modell um Kosten/Leistung basierend auf Boot-Geometrie zu schätzen.

**Pitting:** Kleine Korrosions-Löcher in Metalloberfläche. Kann zu struktureller Schwäche führen wenn tief.

**Pulsation:** Druckwelle-Erzeugung durch Schaufel-Frequenz. Kann zu Vibrationen führen.

**Pump-Out-Station:** Hafen-Entsorgungsanlage wo Fäkalien-Tank geleert wird (umweltgerecht).

**Qualitäts-Kontrolle (QA/QC):** Prüfung ob Komponenten Hersteller-Standard erfüllen. Vor Einbau überprüfen!

**Redundanz:** Mehrfache unabhängige Systeme um Sicherheit zu erhöhen. Z.B. zwei Bilgepumpen statt eine.

**Referenzdruck:** Baseline-Druckmessung zum Vergleich mit aktuellen Werten.

**Schalt-Sollwert (set point):** Druck-Wert bei dem Druckschalter Pumpe ausschaltet. Typisch 2.0–2.5 bar.

**Schaufeln:** Drehende Flügel im Impeller die Zentrifugalkraft erzeugen.

**Schlauch-Schelle:** Metallband um Schläuche an Fittings zu pressen. Edelstahl 316 für Salzwasser.

**Schleifen-Leck:** Hochfrequentes Reibungsgeräusch wenn Rotor Stator berührt.

