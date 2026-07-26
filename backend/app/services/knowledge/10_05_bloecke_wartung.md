---
title: "Blöcke Wartung und Troubleshooting"
kategorie: "10 Blöcke und Umlenkrollen"
unterkategorie: "05 Wartung und Troubleshooting"
version: "1.0.0"
datum: "2026-04-25"
autor: "AYDI Research"
status: "validated"
confidence_quellen:
  - measured: "Hersteller-Wartungsanleitungen, Laborprüfungen"
  - documented: "Hersteller-Kataloge, Segelfachpresse, Forum-Konsens"
  - estimated: "Erfahrungswerte, Quervergleiche"
  - benchmark: "Marktdurchschnitte, Branchenstandards"
tags:
  - blöcke
  - wartung
  - troubleshooting
  - lager
  - schmierung
  - verschleiß
  - inspektion
  - instandhaltung
  - laufendes_gut
  - deck_hardware
boot_klassen:
  - jolle (4–8m)
  - fahrtensegler (8–14m)
  - performance_cruiser (10–16m)
  - blauwasseryacht (12–18m)
  - regattayacht (8–20m)
  - motoryacht (8–25m)
  - superyacht (18m+)
---

# 10.05 — Blöcke Wartung und Troubleshooting: Vollständige Wissensreferenz

> **AYDI Wissensdatei 10.05** — Kategorie 10: Blöcke und Umlenkrollen
> **Confidence-Quelle:** measured (Hersteller-TDS), documented (Hersteller-Kataloge, Fachliteratur), estimated (Erfahrungswerte)
> **Letzte Aktualisierung:** 2026-04-25

---

## Inhaltsverzeichnis

1. [Einführung und Übersicht](#1-einführung-und-übersicht)
2. [Grundlagen und Theorie](#2-grundlagen-und-theorie)
3. [Wartungsintervalle](#3-wartungsintervalle)
4. [Schritt-für-Schritt Wartung](#4-schritt-für-schritt-wartung)
5. [Schmiermittel](#5-schmiermittel)
6. [Verschleißerkennung](#6-verschleißerkennung)
7. [Anlagen-spezifische Wartung](#7-anlagen-spezifische-wartung)
8. [Fehlerbild-Atlas](#8-fehlerbild-atlas)
9. [Troubleshooting](#9-troubleshooting)
10. [FAQ](#10-faq)
11. [Glossar](#11-glossar)
12. [Schnell-Referenz](#12-schnell-referenz)
13. [ANHANG A — Fallstudien](#anhang-a--fallstudien)
14. [ANHANG B — Fallstudien (Fortsetzung)](#anhang-b--fallstudien-fortsetzung)
15. [ANHANG C — Fallstudien (Fortsetzung II)](#anhang-c--fallstudien-fortsetzung-ii)
16. [ANHANG D — Fallstudien (Fortsetzung III)](#anhang-d--fallstudien-fortsetzung-iii)
17. [ANHANG E — AYDI-Integration (Pydantic-Modelle)](#anhang-e--aydi-integration-pydantic-modelle)
18. [ANHANG F — Inspektions-Checklisten](#anhang-f--inspektions-checklisten)
19. [ANHANG G — Verschleißgrenzwert-Tabellen](#anhang-g--verschleißgrenzwert-tabellen)
20. [ANHANG H — Werkzeug- und Materialübersicht](#anhang-h--werkzeug--und-materialübersicht)
21. [ANHANG I — Hersteller-Kontakte und Ersatzteilbeschaffung](#anhang-i--hersteller-kontakte-und-ersatzteilbeschaffung)
22. [ANHANG J — Wartungsprotokoll-Vorlagen](#anhang-j--wartungsprotokoll-vorlagen)
23. [ANHANG K — Saisonale Wartungskalender](#anhang-k--saisonale-wartungskalender)
24. [ANHANG L — Confidence-Mapping](#anhang-l--confidence-mapping)
25. [ANHANG M — Normen und Regelwerke](#anhang-m--normen-und-regelwerke)
26. [ANHANG N — Digitale Wartungsüberwachung](#anhang-n--digitale-wartungsüberwachung)
27. [ANHANG O — Kostenmodelle Wartung vs. Austausch](#anhang-o--kostenmodelle-wartung-vs-austausch)
28. [ANHANG P — Umwelt- und Entsorgungshinweise](#anhang-p--umwelt--und-entsorgungshinweise)
29. [ANHANG Q — Schulung und Qualifikation](#anhang-q--schulung-und-qualifikation)
30. [ANHANG R — Weiterführende Ressourcen](#anhang-r--weiterführende-ressourcen)

---

## 1. Einführung und Übersicht

### 1.1 Warum Blockwartung entscheidend ist

Blöcke gehören zu den am stärksten beanspruchten Beschlagteilen auf einer Yacht. Sie arbeiten unter extremen Bedingungen: hohe dynamische Lasten, Salzwasserexposition, UV-Strahlung, Temperaturwechsel und permanente mechanische Reibung. Ein einzelner Großschotblock auf einer 12-Meter-Yacht kann bei einer Wende Spitzenlasten von über 3.000 kg aufnehmen — und das hunderte Male pro Segeltag.

Trotz dieser extremen Beanspruchung werden Blöcke in der Wartungsroutine vieler Eigner sträflich vernachlässigt. Während Motoren regelmäßige Ölwechsel erhalten und Segel professionell gereinigt werden, drehen sich Blöcke oft jahrelang ohne jede Aufmerksamkeit — bis sie versagen.

Die Konsequenzen mangelhafter Blockwartung reichen von erhöhtem Kraftaufwand beim Trimmen über Sicherheitsrisiken durch plötzliches Blockversagen bis hin zu kostspieligen Folgeschäden an Schoten, Fallen und Rigg-Komponenten.

### 1.2 Konsequenzen mangelhafter Wartung

**Sicherheitsrelevante Konsequenzen:**
- Plötzliches Blockversagen unter Last kann zu unkontrolliertem Ausfieren der Schot führen
- Blockierende Blöcke bei Wendemanövern gefährden die Crew durch verzögerte Segelstellung
- Losgelöste Blockteile (Bolzen, Scheiben, Schäkel) werden zu Geschossen
- Versagende Umlenkblöcke können den Rudergänger oder Trimmer treffen
- Bei Reffmanövern unter Starkwind ist jeder schwergängige Block ein kritisches Zeitrisiko

**Leistungsbezogene Konsequenzen:**
- Erhöhte Reibung in verschlissenen Lagern kann die Trimmkraft um 40–80 % steigern
- Rillenbildung in Scheiben beschädigt Schoten und Fallen progressiv
- Schwergängige Blöcke führen zu langsameren Manövern und schlechterem Trimm
- Bei Regattayachten kostet ein einzelner schwergängiger Block messbar Bootsgeschwindigkeit

**Wirtschaftliche Konsequenzen:**
- Folgeschäden an Tauwerk: Eine gerillte Scheibe kann eine 200-€-Schot in einer Saison zerstören
- Kaskadierende Ausfälle: Ein versagender Großschotblock kann den gesamten Traveller beschädigen
- Notfallreparaturen im Ausland kosten typischerweise das 3–5-fache einer planmäßigen Wartung
- Totalausfall eines hochwertigen Blockensembles: 2.000–15.000 € bei Regattayachten

### 1.3 Philosophie der präventiven Wartung

Die Blockwartung folgt einem gestuften Ansatz:

| Stufe | Bezeichnung | Intervall | Aufwand | Ziel |
|-------|------------|-----------|---------|------|
| 1 | Sichtprüfung | Jeder Segeltag | 2 min/Block | Offensichtliche Schäden erkennen |
| 2 | Funktionsprüfung | Monatlich | 5 min/Block | Schwergängigkeit, Geräusche identifizieren |
| 3 | Süßwasserspülung | Nach jedem Salzwassereinsatz | 1 min/Block | Salzkristallbildung verhindern |
| 4 | Schmierung | 3–6 Monate | 10 min/Block | Lagerfunktion erhalten |
| 5 | Vollinspektion | Jährlich (Winterlager) | 30 min/Block | Verschleißmessung, Teileaustausch |
| 6 | Generalüberholung | 3–5 Jahre | 60 min/Block | Vollständige Zerlegung, Lager-/Scheibentausch |

### 1.4 Geltungsbereich dieses Dokuments

Dieses Dokument behandelt die Wartung und Fehlerdiagnose aller gängigen Blocktypen im Yachtbau:
- Kugellagerblöcke (Ball Bearing Blocks)
- Nadellagerblöcke (Needle Bearing Blocks)
- Gleitlagerblöcke (Plain Bearing / Composite Bearing Blocks)
- Ratschenblöcke (Ratchet Blocks)
- Violinblöcke (Fiddle Blocks)
- Mehrfachblöcke (Double, Triple Blocks)
- Umlenkrollen (Turning Blocks, Foot Blocks, Cheek Blocks)
- Leitösenblöcke (Lead Blocks)
- Snatchblöcke (Snatch Blocks)
- Fliegende Blöcke (Flying Blocks, nicht decksmontiert)

Herstellerübergreifend werden Harken, Lewmar, Ronstan, Antal, Seldén, Spinlock, Wichard, Schaefer, Holt und Allen behandelt.

### 1.5 Einordnung im AYDI-System

Im AYDI-Analysesystem ordnet sich die Blockwartung wie folgt ein:
- **Modul:** Materials (Verschleißanalyse), Service Patterns (Wartungsmuster)
- **Confidence-Level:** measured (Hersteller-Spezifikationen), documented (Wartungsanleitungen), estimated (Erfahrungswerte)
- **Zones:** Deck, Cockpit, Mast, Rigg
- **Relevante ISO-Normen:** ISO 12401 (Sicherheitsgurte und -leinen), ISO 15084 (Ankern und Festmachen)

---

## 2. Grundlagen und Theorie

### 2.1 Verschleißmechanismen in Blöcken

Blöcke unterliegen einer Vielzahl von Verschleißmechanismen, die einzeln oder in Kombination auftreten. Das Verständnis dieser Mechanismen ist Voraussetzung für eine effektive Wartungsstrategie.

#### 2.1.1 Lagerdegradation

**Kugellager (Ball Bearings):**
Kugellager in Blöcken bestehen typischerweise aus Edelstahl (AISI 316 oder Keramik-Hybrid). Die Verschleißmechanismen sind:

- **Pittingkorrosion:** Salzwasser dringt in das Lager ein und erzeugt mikroskopische Korrosionsnarben auf den Laufflächen. Diese Narben wachsen unter Last und erzeugen zunächst ein leichtes Knirschen, dann progressiv steigende Reibung.
- **Brinelling:** Punktuelle Überlastung durch Schocklasten (z.B. Halse bei Starkwind) erzeugt dauerhafte Eindrücke der Kugeln in den Laufringen. Das Lager läuft danach unrund und vibriert.
- **Käfigverschleiß:** Der Kugelkäfig (oft Torlon oder Delrin) verschleißt durch Reibung an den Kugeln. Bei fortgeschrittenem Verschleiß können Kugeln kollidieren und das Lager blockieren.
- **Mangelschmierung:** Ohne regelmäßige Nachschmierung steigt die Reibung exponentiell. Trockenlauf erzeugt Abriebpartikel, die den Verschleiß beschleunigen (Autokatalyse).

**Nadellager (Needle Bearings):**
Nadellager bieten höhere Tragfähigkeit bei kompakterer Bauform. Ihre spezifischen Verschleißmodi:

- **Nadelbruch:** Überlast oder Ermüdung bricht einzelne Nadeln. Die Fragmente beschädigen weitere Nadeln kaskadierend.
- **Schiefstellung:** Fehlausrichtung durch verbogene Achsen führt zu einseitigem Nadelverschleiß und erhöhtem Widerstand.
- **Eindringen von Fremdpartikeln:** Sand, Salzkristalle oder Korrosionsprodukte zwischen den Nadeln zerkratzen die Laufflächen.

**Gleitlager (Plain/Composite Bearings):**
Gleitlager aus Acetal (Delrin), Torlon oder PTFE-Composites:

- **Abrasiver Verschleiß:** Sand und Salz wirken wie Schleifmittel zwischen Achse und Lagerbuchse.
- **Adhäsiver Verschleiß:** Bei Mangelschmierung kann das Polymerlager an der Metallachse „kleben" und Material übertragen.
- **Kriechverformung:** Unter dauerhafter Belastung (stehende Rigg-Teile) deformiert sich die Lagerbuchse plastisch und verliert ihre Rundheit.

#### 2.1.2 Scheibenverschleiß (Sheave Wear)

Die Scheibe (Rolle) eines Blocks verschleißt primär durch Kontakt mit dem Tauwerk:

- **Rillenbildung (Grooving):** Das Tauwerk gräbt sich progressiv in die Scheibe ein. Besonders ausgeprägt bei Dyneema/Spectra auf Aluminiumscheiben.
- **Kantenbruch:** Seitliche Belastung durch schlechte Ausrichtung bricht die Scheibenflanken.
- **Materialermüdung:** Wiederholte Belastungszyklen führen zu Mikrorissen, die sich zu Brüchen ausweiten können.
- **Korrosion:** Bei Aluminiumscheiben kann galvanische Korrosion (Kontakt mit Edelstahl-Achsen) die Lauffläche aufrauhen.

**Rillenbildung im Detail:**
Die Rillenbildungsrate hängt von der Scheiben-/Tauwerk-Kombination ab:

| Scheibenmaterial | Tauwerk | Rillenbildungsrate | Typische Lebensdauer |
|-----------------|---------|-------------------|---------------------|
| Aluminium hart-eloxiert | Polyester | Niedrig | 8–12 Jahre |
| Aluminium hart-eloxiert | Dyneema | Mittel | 4–6 Jahre |
| Acetal (Delrin) | Polyester | Sehr niedrig | 10–15 Jahre |
| Acetal (Delrin) | Dyneema | Niedrig | 6–10 Jahre |
| Edelstahl | Polyester | Sehr niedrig | 15+ Jahre |
| Edelstahl | Dyneema | Niedrig | 10+ Jahre |
| Titan | Dyneema | Sehr niedrig | 15+ Jahre |
| Keramikbeschichtet | Dyneema | Minimal | 15+ Jahre |

#### 2.1.3 UV-Degradation von Polymeren

Viele Blockkomponenten bestehen aus Hochleistungspolymeren, die unter UV-Strahlung altern:

**Betroffene Materialien und ihre UV-Empfindlichkeit:**

- **Acetal (Delrin/POM):** Mäßig UV-empfindlich. Vergilbt, wird spröde. Oberflächenverkreidung nach 3–5 Jahren ungeschützter Exposition. Tiefenwirkung begrenzt auf 0,5–1 mm.
- **Nylon (PA6/PA66):** Stark UV-empfindlich. Verliert innerhalb von 2–3 Jahren signifikant an Festigkeit. Vergilbt, wird spröde, bildet Oberflächenrisse.
- **Torlon (PAI):** Gute UV-Beständigkeit. Minimale Degradation über 10+ Jahre. Daher bevorzugt für exponierte Anwendungen.
- **PEEK:** Ausgezeichnete UV-Beständigkeit. Keine signifikante Degradation.
- **Glasfaserverstärktes Polyamid:** UV-Beständigkeit variiert stark nach Additivierung. Hochwertige Blöcke (Harken, Ronstan) verwenden UV-stabilisierte Compounds.
- **Kohlefaserverstärktes Epoxy:** Ausgezeichnete UV-Beständigkeit der Faser, aber Epoxy-Matrix kann ohne UV-Schutzlack degradieren (Verkreidung, Faserfreilegung).

**UV-Degradationsindikatoren:**
1. Farbveränderung (Vergilbung bei hellen Materialien, Ausbleichen bei dunklen)
2. Oberflächenverkreidung (weißer Abrieb beim Reiben)
3. Mikrorissbildung (sichtbar unter Lupe)
4. Erhöhte Sprödigkeit (Bruch bei Biegebelastung, die vorher elastisch aufgenommen wurde)
5. Gewichtsverlust durch Materialabtrag

#### 2.1.4 Salzkristall-Abrasion

Salzwasser ist der primäre Feind aller Blocklager. Der Schadensmechanismus verläuft in Stufen:

1. **Infiltration:** Salzwasser dringt durch Kapillarwirkung in Lager und Spalte ein.
2. **Verdunstung:** Das Wasser verdunstet, hinterlässt Salzkristalle (NaCl, MgCl₂, CaSO₄).
3. **Kristallwachstum:** In Feuchtperioden lösen sich die Kristalle teilweise, bei Trocknung wachsen sie weiter. Dieser Zyklus erzeugt progressive Kristallvergrößerung.
4. **Abrasion:** Die harten, kantigen Salzkristalle wirken als Schleifmittel zwischen beweglichen Teilen.
5. **Korrosionsbeschleunigung:** Salzkristalle sind hygroskopisch und halten Feuchtigkeit auf Metalloberflächen, was Korrosion fördert.

**Maßnahmen gegen Salzkristall-Abrasion:**
- Süßwasserspülung nach jedem Salzwassereinsatz (minimum)
- Regelmäßige Schmierung verdrängt Restwasser aus Lagerspalten
- Vermeidung von Trocknung im Lager (Schmierfilm als Barriere)
- Ultraschallreinigung bei der jährlichen Generalinspektion

#### 2.1.5 Ermüdung und zyklische Belastung

Blöcke unterliegen zyklischer Belastung mit stark variierenden Amplituden:

- **Großschotblöcke:** 500–2.000 Lastzyklen pro Segeltag (Böen, Wellen)
- **Fallblöcke:** 10–50 Volllastzyklen pro Segeltag (Setzen/Bergen, Reffen)
- **Spinnakerblöcke:** 50–200 dynamische Lastzyklen pro Segeltag
- **Traveller-Blöcke:** 200–1.000 Lastzyklen (ständiges Trimmen)

Die Ermüdungslebensdauer wird nach Wöhler-Konzept beschrieben: Bei 50 % der Bruchlast erreichen Edelstahl-Achsen typischerweise 10⁶ Zyklen, Aluminium-Scheiben 10⁵ Zyklen bis zur Ermüdungsrissbildung.

#### 2.1.6 Galvanische Korrosion in Blöcken

In einem typischen Block treffen verschiedene Metalle aufeinander:

| Kontaktpaar | Potentialdifferenz | Korrosionsrisiko | Maßnahme |
|------------|-------------------|-----------------|----------|
| Edelstahl-Achse / Alu-Scheibe | ~0,5 V | Mittel | Isolierbuchse oder Schmierfilm |
| Edelstahl-Bolzen / Alu-Wange | ~0,5 V | Mittel–Hoch | Isolierscheibe, Edelstahl-Buchse |
| Titan-Achse / Alu-Scheibe | ~0,3 V | Niedrig–Mittel | Schmierfilm ausreichend |
| Bronze-Schäkel / Edelstahl-Auge | ~0,15 V | Niedrig | Akzeptabel im Seewasser |
| Edelstahl 316 / Edelstahl 304 | ~0,05 V | Sehr niedrig | Unproblematisch |

#### 2.1.7 Temperatureinflüsse

Extreme Temperaturen beeinflussen die Blockfunktion:

- **Hitze (>50°C, dunkle Blöcke in Tropensonne):** Polymerlager können erweichen, Schmiermittel verflüssigen sich und tropfen ab, thermische Ausdehnung verändert Lagerspiel.
- **Kälte (<0°C):** Schmiermittel werden zähflüssig, Polymerlager verspröden, Kondenswasser gefriert in Lagern und kann Wangen sprengen.
- **Temperaturwechsel:** Zyklische Ausdehnung/Kontraktion lockert Pressverbindungen und fördert Wasserinfiltration.

**Temperaturverhalten von Blockschmiermitteln:**

| Schmiermittel | Optimaler Bereich | Min. Betriebstemp. | Max. Betriebstemp. | Verhalten bei Kälte | Verhalten bei Hitze |
|--------------|------------------|-------------------|-------------------|--------------------|--------------------|
| Harken One Lube | 5–35°C | -20°C | +80°C | Leicht zähflüssig | Dünnflüssig, hält |
| McLube Sailkote | -10–40°C | -30°C | +250°C (Film) | Film stabil | Film stabil |
| McLube OneDrop | 0–35°C | -20°C | +120°C | Zähflüssig | Stabil |
| Boeshield T-9 | 5–30°C | -15°C | +60°C | Wachsfilm hart | Wachs erweicht |
| Silikonspray | -5–30°C | -30°C | +200°C (Film) | Stabil | Verdampft schnell |
| Lithiumfett | 0–40°C | -25°C | +130°C | Hart, schwergängig | Tropft ab |

#### 2.1.8 Biofilm und Bewuchs

In warmen Gewässern können sich Biofilme und marine Organismen auf und in Blöcken ansiedeln:

**Stufen des Biobewuchses auf Blöcken:**
1. **Bakterienfilm (1–7 Tage):** Unsichtbarer Biofilm auf allen Unterwasser-Oberflächen. Erhöht die Reibung minimal. In Blöcken unter der Wasserlinie (z.B. Schwertfall-Umlenkung) relevant.
2. **Algenbelag (1–4 Wochen):** Grüner oder brauner Belag. Dringt in Lagerspalte ein und kann Scheiben schwergängig machen.
3. **Schalenbildner (1–6 Monate):** Seepocken (Balaniden) können sich an Block-Wangen und in Scheibenrillen festsetzen. Harte Kalkschalen beschädigen Tauwerk und blockieren Scheiben.
4. **Bewuchs mit Muscheln (3–12 Monate):** Miesmuscheln und Austern an dauerhaft untergetauchten Blöcken (Mooring-Systeme, Unterwasser-Umlenkungen).

**Entfernung von Biobewuchs:**
- Biofilm/Algen: Bürste und Süßwasser, ggf. Essigwasser (Säure löst organische Filme)
- Seepocken: Vorsichtig mit Kunststoffspachtel abschlagen, NICHT mit Metallwerkzeug (Kratzer!)
- Muscheln: Mechanisch entfernen, dann Oberfläche reinigen und ggf. nacheloxieren
- Prävention: Antifouling-Anstrich auf dauerhaft untergetauchte Blöcke (nicht auf Laufflächen/Scheiben!)

#### 2.1.9 Vibrationsinduzierter Verschleiß (Fretting)

Fretting-Korrosion tritt auf, wenn zwei Oberflächen unter Last relative Mikrobewegungen ausführen:

**Relevante Stellen in Blöcken:**
- Achse in Wangenbohrung (wenn leicht locker)
- Befestigungsbolzen in Deck-Bohrung
- Lageraussenring in Scheibe (wenn Presspassung nachlässt)

**Mechanismus:**
1. Mikrobewegung (Amplitude 1–100 μm) durch Vibration/Last
2. Abtrag der Oxidschicht → blankes Metall
3. Sofortige Neuoxidation → Oxidpartikel
4. Oxidpartikel wirken als Abrasiv → beschleunigter Verschleiß
5. Bei Edelstahl: charakteristischer rotbrauner Abrieb an Kontaktstelle

**Erkennung:**
- Rotbrauner Pulverbelag an Passstellen (bei Edelstahl)
- Schwarzer Abrieb an Aluminium-Kontaktstellen
- Lokaler Materialverlust an Achse/Bohrung (Passungslockerung)

**Vermeidung:**
- Korrekte Passungen einhalten (kein zu großes Spiel)
- Befestigungen mit korrektem Drehmoment anziehen
- Anti-Fretting-Paste (z.B. Molykote 1000) auf statische Passstellen
- Regelmäßige Nachprüfung von Befestigungen

### 2.2 Lebensdauermodelle

#### 2.2.1 Faktorenmodell für Block-Lebensdauer

Die Lebensdauer eines Blocks wird von zahlreichen Faktoren beeinflusst. Das AYDI-System verwendet ein multiplikatives Faktorenmodell:

```
Lebensdauer_effektiv = Lebensdauer_basis × F_nutzung × F_revier × F_wartung × F_material × F_last
```

**Basisllebensdauer** (Kugellagerblock, Fahrtsegler, gemäßigtes Klima, gute Wartung):

| Bauteil | Basis-Lebensdauer |
|---------|------------------|
| Scheibe (Aluminium) | 10 Jahre |
| Scheibe (Acetal) | 12 Jahre |
| Kugellager | 5 Jahre |
| Nadellager | 4 Jahre |
| Gleitlager | 8 Jahre |
| Achse (316L) | 15 Jahre |
| Wangen (Aluminium) | 20 Jahre |
| Wangen (Composite) | 15 Jahre |

**Korrekturfaktoren:**

| Faktor | Wert | Beschreibung |
|--------|------|-------------|
| F_nutzung (Freizeit, <50 Tage/Jahr) | 1,0 | Referenz |
| F_nutzung (Regatta, >100 Tage/Jahr) | 0,5 | Doppelte Beanspruchung |
| F_nutzung (Charter, >200 Tage/Jahr) | 0,35 | Dreifache Beanspruchung |
| F_nutzung (Blauwasser, 365 Tage/Jahr) | 0,4 | Dauerbeanspruchung, aber pfleglich |
| F_revier (Süßwasser) | 1,5 | Minimale Korrosion |
| F_revier (Ostsee) | 1,0 | Moderate Salinität |
| F_revier (Nordsee/Atlantik) | 0,8 | Hohe Salinität, rau |
| F_revier (Mittelmeer) | 0,85 | Hohe Salinität, UV |
| F_revier (Tropen) | 0,6 | Extreme UV, Salinität, Temperatur |
| F_wartung (Exzellent) | 1,5 | Profi-Wartung, alle Intervalle |
| F_wartung (Gut) | 1,0 | Regelmäßig, Referenz |
| F_wartung (Mäßig) | 0,6 | Unregelmäßig, nur bei Problemen |
| F_wartung (Keine) | 0,3 | Keine Wartung |
| F_material (Premium, Harken Ti-Lite) | 1,3 | Hochwertigste Materialien |
| F_material (Standard, Harken/Lewmar) | 1,0 | Referenz |
| F_material (Budget, No-Name) | 0,6 | Mindere Materialqualität |
| F_last (Unterdimensioniert, >80% WLL) | 0,5 | Dauerhaft überlastet |
| F_last (Korrekt dimensioniert, 40–60% WLL) | 1,0 | Referenz |
| F_last (Überdimensioniert, <30% WLL) | 1,3 | Geringe Beanspruchung |

**Beispielrechnung:**
Harken 57mm Kugellagerblock, Regattayacht (100 Tage/Jahr), Ostsee, gute Wartung, korrekt dimensioniert:
- Kugellager-Lebensdauer = 5 Jahre × 0,5 × 1,0 × 1,0 × 1,0 × 1,0 = 2,5 Jahre
- Scheibe-Lebensdauer = 10 Jahre × 0,5 × 1,0 × 1,0 × 1,0 × 1,0 = 5 Jahre

Dies bestätigt die praktische Erfahrung: Regattasegler tauschen Lager typischerweise alle 1–3 Jahre und Scheiben alle 3–5 Jahre.

---

## 3. Wartungsintervalle

### 3.1 Allgemeine Wartungsmatrix

#### 3.1.1 Routinewartung nach Einsatzart

| Wartungsmaßnahme | Freizeitsegler (Süßwasser) | Freizeitsegler (Salzwasser) | Regatta | Charter | Blauwasser |
|------------------|---------------------------|---------------------------|---------|---------|------------|
| Sichtprüfung | Monatlich | Jeder Segeltag | Vor jeder Regatta | Jede Übergabe | Täglich |
| Süßwasserspülung | Nicht nötig | Nach jedem Einsatz | Nach jedem Einsatz | Nach jedem Einsatz | Nach jedem Einsatz |
| Funktionsprüfung | Vierteljährlich | Monatlich | Vor jeder Regatta | Wöchentlich | Wöchentlich |
| Leichte Schmierung | Halbjährlich | Vierteljährlich | Monatlich | Monatlich | Monatlich |
| Vollschmierung | Jährlich | Halbjährlich | Vierteljährlich | Vierteljährlich | Vierteljährlich |
| Demontage/Inspektion | Alle 2 Jahre | Jährlich | Halbjährlich | Halbjährlich | Halbjährlich |
| Lagertausch | Alle 5 Jahre | Alle 3 Jahre | Jährlich | Alle 2 Jahre | Alle 2 Jahre |
| Scheibentausch | Alle 8–12 Jahre | Alle 5–8 Jahre | Alle 2–3 Jahre | Alle 3–5 Jahre | Alle 3–5 Jahre |

#### 3.1.2 Wartungsmatrix nach Blocktyp

| Blocktyp | Schmierintervall | Inspektionsintervall | Besondere Aufmerksamkeit |
|----------|-----------------|---------------------|------------------------|
| Einfacher Gleitlagerblock | 6 Monate | 12 Monate | Lagerspiel, Achsverschleiß |
| Kugellagerblock | 3 Monate | 6 Monate | Laufgeräusch, Kugellaufbahn |
| Nadellagerblock | 3 Monate | 6 Monate | Nadelzustand, Achse |
| Ratschenblock | 2 Monate | 4 Monate | Ratschenmechanismus, Feder |
| Violinblock | 3 Monate | 6 Monate | Beide Scheiben separat prüfen |
| Snatchblock | 3 Monate | 6 Monate | Öffnungsmechanismus, Verriegelung |
| Mehrfachblock | 3 Monate | 6 Monate | Jede Scheibe einzeln, Achsausrichtung |
| Fußblock/Umlenkrolle | 4 Monate | 8 Monate | Befestigung, Schrauben |
| Wangenblock (Cheek Block) | 4 Monate | 8 Monate | Befestigungsschrauben, Dichtigkeit |
| Mastblock | 6 Monate | 12 Monate | Korrosion am Mastbeschlag |
| Fallenumlenkung (innen) | 12 Monate | 24 Monate | Schwer zugänglich, daher gründlich |

### 3.2 Herstellerspezifische Empfehlungen

#### 3.2.1 Harken

Harken ist der weltweit führende Hersteller von Yachtblöcken und gibt detaillierte Wartungsempfehlungen:

**Harken Wartungsempfehlungen (Confidence: documented):**

| Maßnahme | Intervall | Details |
|----------|----------|---------|
| Süßwasserspülung | Nach jedem Salzwassereinsatz | Lauwarmes Wasser, Block in Einbauposition spülen |
| Leichte Schmierung | Alle 2–3 Monate | Harken One Lube auf Scheibe und Lager |
| Vollständige Reinigung | Saisonstart/-ende | Demontage, Reinigung aller Teile, Neuschmierung |
| Kugellager-Check | Jährlich | Kugeln auf Pitting, Laufbahn auf Riefen prüfen |
| Ratschenblock-Service | Halbjährlich | Ratschenmechanismus zerlegen, Federn prüfen |
| Scheibentausch | Bei sichtbarer Rillenbildung | Harken empfiehlt >1 mm Rillentiefe als Grenze |
| Lager-Kompletttausch | Alle 3–5 Jahre (Salzwasser) | Original Harken Lager verwenden |

**Harken-spezifische Hinweise:**
- Harken-Blöcke verwenden proprietäre Roller-Bearing-Systeme (z.B. Harken Black Magic). Diese erfordern original Harken-Schmiermittel oder kompatible Alternativen.
- Die Harken ESP-Blöcke (Element Snatch Pro) haben einen selbstschmierenden Glasfaser-Composite-Lagereinsatz, der weniger Wartung benötigt.
- Harken Ti-Lite-Blöcke (Titanachse) sind korrosionsbeständiger, aber die Titan-Aluminium-Kontaktstelle muss trotzdem geschmiert bleiben.
- Harken Carbo-Blöcke haben Composite-Scheiben, die weniger Rillenbildung zeigen als Aluminium.

**Harken-Ersatzteilnummern (Confidence: measured):**
- Harken Micro-Block Bearing Kit: HAR 163
- Harken 29mm Block Bearing Kit: HAR 294
- Harken 40mm Block Bearing Kit: HAR 404
- Harken 57mm Block Bearing Kit: HAR 504
- Harken 75mm Block Bearing Kit: HAR 750
- Harken Ratchamatic Spring Kit: HAR 2679
- Harken One Lube (Universalschmiermittel): HAR 7461

#### 3.2.2 Lewmar

Lewmar, britischer Traditionshersteller, hat eigene Wartungsphilosophie:

**Lewmar Wartungsempfehlungen (Confidence: documented):**

| Maßnahme | Intervall | Details |
|----------|----------|---------|
| Süßwasserspülung | Nach jedem Salzwassereinsatz | Klarwasser, keine Reinigungsmittel |
| Schmierung | Alle 3 Monate | Lewmar Winch Oil oder McLube |
| Inspektion | Saisonende | Sichtprüfung aller Blöcke, Schäkel, Bolzen |
| Zerlegung | Jährlich (Salzwasser) | Alle 2 Jahre (Süßwasser) |
| Scheibentausch | Bei sichtbarem Verschleiß | Lewmar empfiehlt Austausch bei asymmetrischer Rille |
| Lageraustausch | Alle 3–5 Jahre | Lewmar-Originallager oder gleichwertig |

**Lewmar-spezifische Hinweise:**
- Lewmar Synchro-Blöcke verwenden Composite-Lager, die selbstschmierend sind. Dennoch empfiehlt Lewmar eine jährliche Schmierung.
- Lewmar Open-Shell-Design ermöglicht bei vielen Modellen die Wartung ohne vollständige Demontage.
- Lewmar Size 0-5 Blöcke: Achse ist oft eingepresst, Demontage erfordert spezielles Werkzeug.
- Lewmar HTX-Blöcke (Hard Top X): Verstärkter Kopf, Scheibentausch wie Standard.
- Bei Lewmar-Blöcken mit Dyneema-Loop-Befestigung: Loop jährlich auf Abrieb prüfen.

**Lewmar-Ersatzteilnummern (Confidence: measured):**
- Lewmar Size 1 Block Service Kit: LEW 19901400
- Lewmar Size 2 Block Service Kit: LEW 19901401
- Lewmar Size 3 Block Service Kit: LEW 19901402
- Lewmar Winch & Block Oil: LEW 19701100
- Lewmar Synchro Bearing Replacement: LEW 29901xxx (größenabhängig)

#### 3.2.3 Ronstan

Ronstan, australischer Hersteller, betont salzwasserbeständige Konstruktion:

**Ronstan Wartungsempfehlungen (Confidence: documented):**

| Maßnahme | Intervall | Details |
|----------|----------|---------|
| Süßwasserspülung | Nach jedem Einsatz | Ronstan betont: „Fresh water is your best friend" |
| Schmierung | Alle 4 Monate | Leichtes Silikonspray oder McLube |
| Inspektion | Halbjährlich | Scheibe, Lager, Befestigung |
| Vollservice | Jährlich | Zerlegung, Reinigung, Neuschmierung |
| Scheibentausch | Bei Rillentiefe >0,8 mm | Ronstan-Scheiben sind oft aus Acetal |
| Achsentausch | Bei sichtbarer Korrosion | Edelstahl 316, maßgenau |

**Ronstan-spezifische Hinweise:**
- Ronstan Series 20–75 Orbit-Blöcke haben ein besonderes Befestigungssystem mit dyneema-kompatiblen Weblaschen.
- Ronstan verwendet bei vielen Modellen Acetal-Scheiben (selbstschmierend, geringes Gewicht), die weniger Wartung benötigen als Aluminiumscheiben.
- Ronstan BB-Blöcke (Ball Bearing) verwenden Edelstahl-Kugellager der Qualitätsstufe ABEC-3 oder besser.
- Ronstan Race-Serien haben Torlon-Lager für höhere Lastaufnahme.

**Ronstan-Ersatzteilnummern (Confidence: measured):**
- Ronstan Series 20 Sheave Kit: RF20SHV
- Ronstan Series 30 Sheave Kit: RF30SHV
- Ronstan Series 40 Sheave Kit: RF40SHV
- Ronstan Series 55 Sheave Kit: RF55SHV
- Ronstan Orbit Block Bearing Kit: RF45SHVxxx (modellabhängig)
- Ronstan Friction Ring Set (Alternative zu Blöcken): RF8090-xx

#### 3.2.4 Antal

Antal, italienischer Hersteller, produziert Blöcke vom Jolle- bis Superyacht-Segment:

**Antal Wartungsempfehlungen (Confidence: documented):**

| Maßnahme | Intervall | Details |
|----------|----------|---------|
| Süßwasserspülung | Nach jedem Salzwassereinsatz | Lauwarm, keine Lösungsmittel |
| Schmierung | Alle 3 Monate | Antal empfiehlt PTFE-basiertes Spray |
| Sichtinspektion | Monatlich | Scheibe, Lager, Kopf-/Fußverbindung |
| Demontage | Jährlich | Vollständige Zerlegung und Reinigung |
| Scheibentausch | Bei sichtbarem Verschleiß | Antal-Scheiben aus eloxiertem Aluminium |
| Lageraustausch | Alle 3–4 Jahre | Bei Regattaeinsatz häufiger |

**Antal-spezifische Hinweise:**
- Antal V-Serie verwendet ein zweiteiliges Gehäuse mit Schnappverschluss, das die Demontage ohne Werkzeug ermöglicht.
- Antal Smart-Blöcke haben einen integrierten Lastsensor — Kalibrierung jährlich prüfen.
- Antal Superyacht-Blöcke (KF-Serie) sind aus geschmiedetem Aluminium und erfordern spezielle Wartungsprozeduren.
- Antal bietet Master-Wartungskits für die gesamte Blockflotte einer Yacht an.

### 3.3 Saisonaler Wartungskalender

#### 3.3.1 Einwintern (Oktober–November, Nordeuropa)

**Checkliste Einwintern:**

1. Alle Blöcke gründlich mit Süßwasser spülen (Gartenschlauch, Düse auf „Strahl")
2. Blöcke wenn möglich demontieren oder mindestens öffnen
3. Alle Teile in warmem Süßwasser mit mildem Spülmittel einweichen (30 min)
4. Hartnäckige Salzablagerungen mit weicher Bürste entfernen
5. Alle Teile trocknen (Druckluft oder Luft trocknen lassen)
6. Lager prüfen: Drehbewegung, Geräusche, sichtbare Schäden
7. Scheiben prüfen: Rillenbildung, Kantenbruch, Verfärbung
8. Achsen prüfen: Korrosion, Verschleiß, Rundheit
9. Befestigungen prüfen: Schrauben, Bolzen, Schäkel, Splinte
10. Alle beweglichen Teile schmieren (großzügig für Winterlager)
11. Blöcke in Innenräumen oder unter Persenning lagern (UV-Schutz)
12. Verschleißteile bestellen für Frühjahrsservice

#### 3.3.2 Auswassern (März–April, Nordeuropa)

**Checkliste Saisonstart:**

1. Alte Winterschmierung entfernen (wenn verhärtet)
2. Alle Blöcke auf Feuchtigkeit und Schimmel prüfen
3. Funktionsprüfung: Jede Scheibe einzeln drehen, Leichtgängigkeit prüfen
4. Neue Schmierung auftragen (dünn, gleichmäßig)
5. Ratschenblöcke: Ratschenmechanismus prüfen, Federspannung testen
6. Snatchblöcke: Öffnungsmechanismus prüfen, Verriegelung testen
7. Befestigungen nachziehen (Drehmoment nach Herstellerangabe)
8. Tauwerk durch Blöcke einscheren und Leichtgängigkeit prüfen
9. Unter Last testen (Segel setzen, trimmen, Funktionsprüfung)
10. Protokoll erstellen: Zustand jedes Blocks dokumentieren

#### 3.3.3 Mitsaison-Checks (Juni, August)

**Kurzinspektion Mitsaison:**

1. Sichtprüfung aller zugänglichen Blöcke
2. Leichtgängigkeit per Hand prüfen
3. Ungewöhnliche Geräusche identifizieren (Knirschen, Quietschen)
4. Nachschmierung bei Bedarf
5. Besonderes Augenmerk auf hochbelastete Blöcke (Großschot, Genua, Spi)
6. Ratschenblöcke: Funktion unter Last testen
7. Lose Befestigungen nachziehen

#### 3.3.4 Tropische/Ganzjahres-Wartung

In tropischen Gewässern (Karibik, Mittelmeer Sommer, Südostasien) gelten verkürzte Intervalle:

| Maßnahme | Standard-Intervall | Tropisches Intervall | Grund |
|----------|-------------------|---------------------|-------|
| Süßwasserspülung | Nach Salzwasser | Nach jedem Einsatz | Höhere Verdunstungsrate |
| Schmierung | 3 Monate | 6–8 Wochen | Schmierung tropft bei Hitze ab |
| Inspektion | 6 Monate | 3 Monate | Beschleunigte UV-Degradation |
| Vollservice | 12 Monate | 6 Monate | Höhere Korrosionsrate |
| UV-Schutz | Empfohlen | Pflicht | UV-Index 10+ vs. 4–6 |

### 3.4 Wartungsprotokollierung

Eine systematische Protokollierung ist entscheidend für die Lebensdauerplanung:

**Mindest-Dokumentation pro Block:**
- Blockbezeichnung und Position (z.B. „Großschot-Umlenkblock Stb.")
- Hersteller, Modell, Größe
- Einbaudatum
- Datum jeder Wartungsmaßnahme
- Art der Maßnahme (Schmierung, Inspektion, Tausch)
- Festgestellter Zustand (Skala 1–5 oder verbal)
- Getauschte Teile
- Nächster geplanter Wartungstermin

---

## 4. Schritt-für-Schritt Wartung

### 4.1 Werkzeug und Materialien

#### 4.1.1 Grundwerkzeug für Blockwartung

| Werkzeug | Verwendung | Hinweise |
|----------|-----------|---------|
| Innensechskant-Satz (metrisch + Zoll) | Achsbolzen, Befestigungsschrauben | Harken: metrisch, Lewmar: gemischt |
| Schraubendreher (Kreuz + Schlitz) | Wangenschrauben | Nicht-magnetisch bevorzugt |
| Spitzzange | Sicherungsringe, Splinte | Edelstahl für Salzwasserumgebung |
| Sicherungsring-Zange (innen + außen) | Achssicherungen | Verschiedene Größen |
| Drehmomentschlüssel (1–25 Nm) | Befestigungsschrauben | Unverzichtbar für korrekte Montage |
| Weiche Bürste (Nylon) | Reinigung | Keine Messingbürste auf Aluminium! |
| Reinigungsbecken | Einweichen von Teilen | Flache Schale, lauwarm |
| Druckluft (Dose oder Kompressor) | Trocknung, Ausblasen | Max. 2 bar für Lager |
| Lupe (10x) | Verschleißinspektion | Für Lageroberflächen |
| Messschieber (digital) | Verschleißmessung | 0,01 mm Auflösung |
| Mikrometer | Achsdurchmesser | Für Rundheitsmessung |
| Tiefenmaß | Rillentiefe Scheibe | Oder Messschieber-Tiefenmaß |
| Magnetische Schale | Kleinteile | Kugeln, Nadeln, Schrauben |

#### 4.1.2 Verbrauchsmaterial

| Material | Menge pro Saison (10 Blöcke) | Kosten ca. |
|----------|------------------------------|-----------|
| Harken One Lube oder equivalent | 1 Flasche (100 ml) | 15–20 € |
| McLube Sailkote | 1 Dose (300 ml) | 18–25 € |
| Isopropanol (Reinigung) | 500 ml | 5–8 € |
| Silikonfreies Reinigungsmittel | 250 ml | 8–12 € |
| Ersatz-Sicherungsringe | Diverse | 5–10 € |
| Ersatz-Unterlegscheiben | Diverse | 3–5 € |
| Mikrofasertücher | 5 Stück | 5–8 € |
| Latex-/Nitrilhandschuhe | 20 Stück | 3–5 € |

### 4.2 Zerlegung eines Kugellagerblocks

#### 4.2.1 Vorbereitung

1. Block vom Deck demontieren (Schäkel, Bolzen oder Schrauben lösen).
2. Tauwerk entfernen.
3. Block fotografieren (Orientierung, Einbaurichtung, Zustand).
4. Saubere, helle Arbeitsfläche vorbereiten. Magnetische Schale bereitstellen.
5. Herstelleranleitung bereithalten (falls verfügbar).

#### 4.2.2 Demontage-Prozedur (am Beispiel Harken 57mm Block)

**Schritt 1: Achsbolzen identifizieren**
- Harken 57mm: Innensechskant M5 auf einer Seite, Sicherungsring auf der Gegeniseite.
- Den Sicherungsring mit Sicherungsring-Zange entfernen. Vorsicht: Ring steht unter Spannung.

**Schritt 2: Achse herausdrücken**
- Innensechskantschraube auf der Fixierseite lösen.
- Achse mit leichtem Druck (Durchschlag + Hammer, Kunststoffhammer) heraustreiben.
- ACHTUNG: Niemals mit Gewalt! Wenn die Achse klemmt, liegt Korrosion vor. In diesem Fall einweichen (Kriechöl, 24 h warten).

**Schritt 3: Scheibe entnehmen**
- Scheibe seitlich aus den Wangen heben.
- Kugeln fallen möglicherweise heraus — magnetische Schale bereithalten.
- Kugeln zählen und Zustand notieren.

**Schritt 4: Wangen trennen (falls nötig)**
- Bei einigen Modellen sind die Wangen durch Kopf- und Fußverbindung zusammengehalten.
- Verbindungsbolzen/-schrauben lösen.
- Wangen vorsichtig trennen.

**Schritt 5: Lager entnehmen**
- Innere Lagerschalen aus der Scheibe drücken (oft Presspassung).
- Äußere Lagerschale aus Wange entnehmen (falls separate Bauweise).
- Alle Kugeln in Seifenwasser reinigen.

#### 4.2.3 Reinigung

**Reinigungsprotokoll:**

1. **Grobe Reinigung:** Alle Teile in lauwarmem Süßwasser mit mildem Spülmittel 30 Minuten einweichen.
2. **Detailreinigung:** Mit weicher Bürste alle Flächen reinigen. Besondere Aufmerksamkeit auf Lagersitze und Kugellaufbahnen.
3. **Lösungsmittelreinigung:** Lager und Kugeln in Isopropanol ultraschall-reinigen oder mit Lappen/Pinsel reinigen. Alte Schmierung vollständig entfernen.
4. **Trocknung:** Druckluft (max. 2 bar!) auf alle Teile. Lager NICHT rotieren lassen unter Druckluft (Trockenlauf schädigt Oberflächen).
5. **Endkontrolle:** Alle Teile auf weißem Tuch auslegen, auf Korrosion, Verfärbung, Beschädigung prüfen.

**NICHT verwenden:**
- Aceton auf Polymer-Teile (löst Oberfläche an)
- Aggressive Entfetter auf Aluminium (Oberflächenangriff)
- Messingbürsten auf Aluminium (Kratzer, galvanische Ablagerung)
- Stahlwolle (Partikeleinbettung, Korrosionskeime)
- Hochdruckreiniger direkt auf Lager (presst Wasser in Lagerspalte)

#### 4.2.4 Inspektion nach Reinigung

**Kugeln (Confidence: measured):**
- Sichtprüfung unter 10x Lupe: Pitting, Kratzer, Verfärbung
- Rolltest auf Glasplatte: Kugel muss glatt und geräuschlos rollen
- Messung: Durchmesservarianz <0,005 mm akzeptabel
- Jede beschädigte Kugel → ALLE Kugeln ersetzen (Set)

**Laufbahnen:**
- Innere Lagerschale: Auf Riefen, Pitting, Verfärbung prüfen
- Äußere Lagerschale (Scheibe): Identisch prüfen
- Fingernageltest: Nagel über Lauffläche ziehen — spürbare Riefen = Tausch

**Achse:**
- Durchmesser an 4 Stellen messen (0°, 90°, 180°, 270°)
- Rundheit: Maximale Abweichung <0,02 mm (Fahrt), <0,01 mm (Regatta)
- Oberfläche: Poliert, keine Riefen, keine Korrosionsnarben
- Korrodierte Achse = sofort tauschen

**Scheibe:**
- Rillentiefe messen (Messschieber-Tiefenmaß)
- Max. 1,0 mm bei Fahrtseglern, max. 0,5 mm bei Regatta
- Flankenbruch prüfen (seitliche Kanten)
- Bohrung: Rundheit prüfen, Maß mit Achse vergleichen

#### 4.2.5 Zusammenbau

**Schritt 1: Schmierung**
- Kugeln einzeln mit Harken One Lube oder McLube OneDrop dünn benetzen.
- Lagersitze mit dünnem Schmierfilm versehen.
- Achse dünn einfetten (kein übermäßiges Fett — bindet Schmutz).

**Schritt 2: Lager einsetzen**
- Kugeln in die innere Lagerschale einsetzen.
- Lagerkäfig (wenn vorhanden) richtig orientieren.
- Äußere Lagerschale aufsetzen.

**Schritt 3: Scheibe einsetzen**
- Scheibe zwischen die Wangen positionieren.
- Auf korrekte Laufrichtung achten (bei Ratschenblöcken kritisch!).

**Schritt 4: Achse einsetzen**
- Achse durch Wange → Lager → Scheibe → Lager → Wange führen.
- Leichtgängig — wenn Widerstand: Ausrichtung prüfen, NICHT klopfen.

**Schritt 5: Sicherung**
- Innensechskantschraube eindrehen (Drehmoment nach Hersteller).
- Sicherungsring einsetzen (vollständig im Sitz eingerastet?).
- Scheibe von Hand drehen: muss leichtgängig sein, kein Spiel in Achsrichtung.

**Schritt 6: Funktionstest**
- Scheibe drehen: frei, leise, gleichmäßig.
- Seitliches Spiel prüfen: <0,5 mm akzeptabel.
- Tauwerk einlegen: durch Block ziehen, Leichtgängigkeit prüfen.

### 4.3 Zerlegung eines Nadellagerblocks

#### 4.3.1 Besonderheiten Nadellager

Nadellagerblöcke erfordern erhöhte Vorsicht bei der Demontage:
- Nadeln sind lose oder in einem Käfig — bei loser Anordnung fallen sie heraus.
- Nadeln sind sehr dünn (typisch 1,5–3 mm Durchmesser) und empfindlich.
- Verwechslung von Nadeln verschiedener Blöcke vermeiden (maßgenau!).

#### 4.3.2 Demontage-Prozedur

1. Achsbolzen entfernen (wie bei Kugellagerblock).
2. Achse vorsichtig herausziehen — wenn Nadeln lose sind, Block seitlich halten, damit Nadeln nicht herausfallen.
3. Scheibe entnehmen.
4. Nadeln zählen und auf weißem Tuch auslegen.
5. Nadelkäfig (falls vorhanden) entnehmen und auf Verformung prüfen.

#### 4.3.3 Inspektion Nadellager

**Nadeln:**
- Jede Nadel einzeln unter 10x Lupe prüfen.
- Auf Biegung (Rollentest auf Glasplatte: Nadel muss gerade rollen).
- Auf Korrosion (Pitting, Oberflächenverfärbung).
- Auf Bruch (auch Mikrorisse — Magnetpulverprüfung ideal, aber in der Praxis: Sichtprüfung).
- EINE defekte Nadel → ALLE Nadeln tauschen.

**Nadellaufflächen:**
- Innenfläche der Scheibe und Achse auf Riefen prüfen.
- Fingernageltest (wie bei Kugellager).
- Verfärbung (Blaulauf = Überhitzung durch Trockenlauf).

#### 4.3.4 Zusammenbau Nadellager

1. Laufflächen schmieren (dünn, gleichmäßig).
2. Nadeln einsetzen — bei loser Anordnung: Fett als "Kleber" verwenden, Nadeln einzeln in gefettete Lauffläche setzen.
3. Nadelkäfig einsetzen (korrekte Orientierung!).
4. Scheibe einsetzen, Achse durchführen.
5. Sicherung wie bei Kugellagerblock.
6. Funktionstest: Nadellager laufen typischerweise etwas schwerer als Kugellager bei geringer Last.

### 4.4 Ratschenblock-Service

#### 4.4.1 Funktionsprinzip

Der Ratschenblock erlaubt freie Rotation in Zugrichtung und blockiert in Gegenrichtung (wie eine Freilaufnabe). Dies ermöglicht dem Trimmer, die Schot unter Last zu halten, ohne eine Winch nutzen zu müssen.

**Komponenten des Ratschenmechanismus:**
- Ratschenkörper (mit Sägezahn-Innenprofil)
- Sperrklinken (2–4 Stück, federbelastet)
- Federn (Druck- oder Blattfedern)
- Ratschenring/Ratschensitz
- Rückholfeder (bei automatisch umschaltenden Ratschenblöcken)

#### 4.4.2 Demontage Ratschenmechanismus

**WICHTIG: Vor der Demontage Orientierung markieren (Edding-Punkt auf Wange und Scheibe).**

1. Block wie bei Kugellagerblock öffnen.
2. Scheibe entnehmen — der Ratschenkörper sitzt in oder auf der Scheibe.
3. Ratschenring vom Scheibenkörper trennen (oft Schnappverbindung oder Schrauben).
4. Sperrklinken und Federn entnehmen — Vorsicht, Federn stehen unter Spannung!
5. Alle Teile auf weißem Tuch auslegen und fotografieren.

#### 4.4.3 Inspektion Ratschenmechanismus

| Bauteil | Prüfkriterium | Austauschanzeige |
|---------|--------------|-----------------|
| Sperrklinken | Scharfe Kanten, keine Rundung | Abgerundete Klinkenspitze |
| Sägezahn-Profil | Scharfe Flanken, keine Abplattung | Abgeflachte oder gerundete Zahnflanken |
| Federn | Volle Federkraft, kein Bruch | Gebrochene oder ermüdete Feder (Klinke fällt nicht sofort ein) |
| Ratschenring | Gleichmäßige Oberfläche | Rillen, Korrosion, Verfärbung |
| Ratschensitz | Plan, keine Verformung | Einlaufspuren, Verformung |

#### 4.4.4 Häufige Ratschenblock-Probleme

**Problem: Ratsche greift nicht zuverlässig**
- Ursache 1: Verschmutzte Sperrklinken (Salz, Sand) → Reinigung
- Ursache 2: Ermüdete Federn → Federtausch
- Ursache 3: Abgerundete Klinken/Zähne → Klinken-/Ringtausch
- Ursache 4: Falsche Schmierung (zu viel Fett auf Klinken) → Reinigung, nur minimale Schmierung

**Problem: Ratsche blockiert in beide Richtungen**
- Ursache 1: Verklemmte Sperrklinke (Korrosion, Fremdkörper) → Reinigung
- Ursache 2: Verformter Ratschenring → Tausch
- Ursache 3: Falsche Montage (Scheibe/Ring falsch orientiert) → Korrektur

**Problem: Ratsche macht übermäßigen Lärm**
- Ursache: Normal — Ratschenblöcke klicken konstruktionsbedingt. Übermäßiger Lärm deutet auf verschlissene Klinken oder lockeren Ratschenring hin.

#### 4.4.5 Zusammenbau Ratschenmechanismus

1. Ratschenring und Ratschensitz reinigen, minimal schmieren (KEIN Fett auf Zahnprofil!).
2. Federn einsetzen (korrekte Orientierung prüfen).
3. Sperrklinken einsetzen — jede Klinke muss frei fallen und von der Feder zurückgestellt werden.
4. Ratschenring auf Scheibe setzen (Markierung beachten!).
5. Funktionstest VOR Einbau: Scheibe in einer Richtung drehen = frei; in Gegenrichtung = blockiert.
6. Block zusammenbauen (wie Standard-Kugellagerblock).

### 4.5 Scheibentausch (Sheave Replacement)

#### 4.5.1 Wann tauschen?

**Austauschkriterien (Confidence: documented):**
- Rillentiefe > 1,0 mm (Fahrtsegler) oder > 0,5 mm (Regatta)
- Sichtbarer Flankenbruch
- Einseitige Abnutzung (Block war falsch ausgerichtet)
- Oberflächenrissbildung (UV-Degradation bei Polymer-Scheiben)
- Unrunder Lauf (Scheibe „eiert")
- Unwucht unter Last (Vibration)

#### 4.5.2 Scheibe auswählen

**Dimensionen:**
- Scheibendurchmesser muss exakt passen (Wangenabstand bestimmt Maximaldurchmesser)
- Achsbohrung: Spielpassung mit Originalachse (typisch H7/f7)
- Rillenbreite: passend zum verwendeten Tauwerk (Faustregel: Rillenradius ≈ halber Tauwerk-Ø + 10 %, vgl. Abschnitt 6.3.3)
- Materialwahl: Original-Material beibehalten oder aufwerten

**Material-Upgrade-Pfade:**
| Von | Nach | Vorteil | Nachteil |
|-----|------|---------|----------|
| Acetal | Aluminium hart-eloxiert | Höhere Tragfähigkeit | Schwerer, teurer |
| Aluminium | Aluminium hart-eloxiert | Bessere Verschleißfestigkeit | Kosten |
| Aluminium | Torlon/PEEK | Selbstschmierend, leicht | Begrenzte Tragfähigkeit |
| Aluminium | Keramikbeschichtet | Extreme Verschleißfestigkeit | Sehr teuer (3–5x) |

#### 4.5.3 Einbau neue Scheibe

1. Neue Scheibe auf Maßhaltigkeit prüfen (Messschieber).
2. Achsbohrung: Leichtgängig auf Achse aufschieben (kein Klemmen, kein Wackeln).
3. Lager einsetzen (falls in Scheibe integriert).
4. Scheibe zwischen Wangen positionieren.
5. Achse durchführen, Sicherung wie Original.
6. Tauwerk einlegen, Leichtgängigkeit prüfen.

### 4.6 Lagertausch (Bearing Replacement)

#### 4.6.1 Kugellager tauschen

1. Block zerlegen (s. 4.2).
2. Altes Lager komplett entfernen (Kugeln, Lagerschalen, Käfig).
3. Lagersitze reinigen und auf Korrosion/Verschleiß prüfen.
4. Lagersitz leicht schmieren.
5. Neue Lagerschalen einpressen (Presspassung — gleichmäßig, ohne Verkanten!).
6. Neue Kugeln einsetzen (Fett als Klebehilfe).
7. Käfig einsetzen, Scheibe auf Achse testen.

#### 4.6.2 Nadellager tauschen

1. Block zerlegen (s. 4.3).
2. Alte Nadeln und Käfig komplett entfernen.
3. Laufflächen prüfen — bei Riefen: Achse und/oder Scheibe ebenfalls tauschen.
4. Neue Nadeln einzeln in gefettete Lauffläche einsetzen.
5. Neuen Käfig einsetzen.
6. Achse einführen, Funktionstest.

#### 4.6.3 Gleitlager tauschen

1. Block zerlegen.
2. Alte Lagerbuchse herausdrücken (oft Presspassung in Scheibe).
3. Neue Lagerbuchse einpressen (Ausrichtung beachten — ggf. Schmiernuten-Position).
4. Achse testen: leichtgängig, kein Spiel.

### 4.7 Wangenreparatur (Cheek Repair)

#### 4.7.1 Reparierbare Schäden

- Oberflächenkorrosion auf Aluminium: Abschleifen, nacheloxieren (oder Cerakote)
- Leichte Dellen: Richten (nur bei Aluminium, nicht bei Composite)
- Lockere Befestigungsinserts: Helicoil-Einsatz oder Neugewindeschneiden
- Haarrisse in Composite: Epoxidreparatur (nur wenn nicht strukturkritisch)

#### 4.7.2 Nicht reparierbare Schäden

- Gebrochene Wange → Austausch (Block komplett)
- Ausgeschlagene Achsbohrung → Austausch
- Strukturelle Risse in Lastpfad → Austausch
- Starke Korrosion mit Materialverlust → Austausch

**Grundregel: Im Zweifel tauschen. Ein versagender Block unter Last ist ein Sicherheitsrisiko.**

---

## 5. Schmiermittel

### 5.1 Anforderungen an Block-Schmiermittel

Schmiermittel für Yachtblöcke müssen spezielle Anforderungen erfüllen:

| Anforderung | Begründung |
|------------|-----------|
| Salzwasserbeständig | Permanente Exposition |
| UV-beständig | Decksmontage in direkter Sonne |
| Materialverträglich | Darf Polymere nicht angreifen (Acetal, Torlon, Nylon) |
| Kriechfähig | Muss in enge Lagerspalte eindringen |
| Haftfähig | Darf bei Rotation nicht abgeschleudert werden |
| Nicht klebrig | Darf keinen Schmutz/Sand binden |
| Lebensmittelecht (optional) | Für Blöcke in Pantry-Nähe (Tropfen auf Lebensmittel) |
| Biologisch abbaubar (optional) | Umweltaspekt bei Tropfen ins Wasser |

### 5.2 Empfohlene Schmiermittel

#### 5.2.1 Harken One Lube

| Eigenschaft | Wert |
|------------|------|
| Typ | Synthetisches Lageröl |
| Basis | PTFE-modifiziertes Synthetiköl |
| Viskosität | Mittel (ISO VG 32) |
| Temperaturbereich | -20°C bis +80°C |
| Salzwasserbeständigkeit | Hervorragend |
| Materialverträglichkeit | Alle gängigen Blockmaterlalien |
| Anwendung | Tropfenweise auf Lagerstellen |
| Dosierung | 2–3 Tropfen pro Lagerstelle |
| Gebindegröße | 100 ml Flasche mit Dosierspitze |
| Preis | ca. 15–20 € |
| Hersteller-Empfehlung | „Für alle Harken-Produkte" |

**Bewertung (Confidence: documented):**
Harken One Lube ist der Industriestandard für Blockschmierung. Universell einsetzbar, gute Kriechfähigkeit, hervorragende Salzwasserbeständigkeit. Einziger Nachteil: relativ teuer pro Milliliter.

#### 5.2.2 McLube Sailkote

| Eigenschaft | Wert |
|------------|------|
| Typ | Trockenschmiermittel (Spray) |
| Basis | Fluorpolymer in Lösungsmittelträger |
| Viskosität | Sehr niedrig (verdampft, hinterlässt Trockenfilm) |
| Temperaturbereich | -30°C bis +250°C |
| Salzwasserbeständigkeit | Gut |
| Materialverträglichkeit | Alle Materialien, inklusive Tauwerk |
| Anwendung | Aufsprühen, 5 min trocknen lassen |
| Gebindegröße | 300 ml Spraydose |
| Preis | ca. 18–25 € |

**Bewertung (Confidence: documented):**
McLube Sailkote ist hervorragend für Scheiben und Tauwerk-Kontaktflächen. Als Trockenschmiermittel bindet es keinen Schmutz. Für Kugel- und Nadellager jedoch NICHT ausreichend — dort fehlt die nötige Filmdicke für Vollschmierung.

**Empfohlene Kombination:** McLube Sailkote auf Scheiben + Harken One Lube in Lager.

#### 5.2.3 McLube OneDrop

| Eigenschaft | Wert |
|------------|------|
| Typ | Synthetisches Lageröl |
| Basis | Fluorpolymer-verstärktes Synthetiköl |
| Viskosität | Niedrig–Mittel |
| Temperaturbereich | -20°C bis +120°C |
| Anwendung | Tropfenweise auf Lagerstellen |
| Gebindegröße | 37 ml Flasche mit Nadeldosierer |
| Preis | ca. 12–18 € |

**Bewertung:** Ausgezeichnetes Lagerschmiermittel, gute Alternative zu Harken One Lube. Der Nadeldosierer ermöglicht präzise Dosierung.

#### 5.2.4 Boeshield T-9

| Eigenschaft | Wert |
|------------|------|
| Typ | Wachsbasierter Korrosionsschutz + Schmierung |
| Basis | Paraffinwachs in Lösungsmittel |
| Viskosität | Niedrig (bei Auftrag), mittel (nach Trocknung) |
| Temperaturbereich | -15°C bis +60°C |
| Salzwasserbeständigkeit | Hervorragend |
| Besonderheit | Hinterlässt dauerhaften Wachsfilm |
| Gebindegröße | 118 ml / 355 ml Spray |
| Preis | ca. 15–22 € |

**Bewertung (Confidence: documented):**
Boeshield T-9 wurde von Boeing für die Luftfahrt entwickelt und ist ein ausgezeichneter Korrosionsschutz. Als Schmiermittel für Hochlast-Lager jedoch nur bedingt geeignet — der Wachsfilm hat geringere Schmierwirkung als echte Öle. Ideal für Winterlager-Konservierung und wenig belastete Lager.

#### 5.2.5 Silikonspray

| Eigenschaft | Wert |
|------------|------|
| Typ | Silikonöl in Treibgas |
| Basis | Polydimethylsiloxan (PDMS) |
| Viskosität | Sehr niedrig |
| Anwendung | Aufsprühen |
| Preis | ca. 5–8 € |

**Bewertung (Confidence: documented):**
Silikonspray ist universell verfügbar und günstig, aber für hochbelastete Lager NICHT empfohlen:
- Geringe Tragfähigkeit des Schmierfilms
- Verdampft schnell bei Sonneneinstrahlung
- Kann auf manchen Kunststoffen Spannungsrisskorrosion fördern
- Kurzfristige Notlösung, keine Dauerschmierung

#### 5.2.6 WD-40 — WARNUNG

**WD-40 ist KEIN Schmiermittel und darf NICHT auf Blöcken verwendet werden!**

WD-40 ist ein Wasserverdränger und Kriechöl. Es:
- Löst vorhandene Schmierung auf
- Verdunstet schnell und hinterlässt trockene Oberflächen
- Kann Polymerlager angreifen (Lösungsmittelanteil)
- Wird oft fälschlicherweise als "Allheilmittel" eingesetzt

Einzige akzeptable Verwendung: Lösen festsitzender Achsen/Bolzen vor der Demontage, danach vollständig entfernen und korrekt schmieren.

### 5.3 Schmierstellen und Dosierung

#### 5.3.1 Schmierplan nach Blocktyp

| Schmierstelle | Schmiermittel | Menge | Intervall |
|--------------|--------------|-------|----------|
| Kugellager | Harken One Lube / McLube OneDrop | 2–3 Tropfen | 3 Monate |
| Nadellager | Harken One Lube / McLube OneDrop | 3–4 Tropfen | 3 Monate |
| Gleitlager | Harken One Lube / McLube OneDrop | 2–3 Tropfen | 6 Monate |
| Scheibe (Tauwerk-Kontakt) | McLube Sailkote | Dünn aufsprühen | 3 Monate |
| Achse | Harken One Lube | Dünn auftragen | 6 Monate |
| Ratschenmechanismus | McLube Sailkote (minimal!) | 1 kurzer Sprühstoß | 4 Monate |
| Snatch-Öffnung | Harken One Lube | 1 Tropfen am Gelenk | 3 Monate |
| Schäkel/Bolzen | Boeshield T-9 | Dünn auftragen | 6 Monate |
| Befestigungsschrauben | Tef-Gel oder Duralac | Dünn auf Gewinde | Bei jeder Demontage |

#### 5.3.2 Überschmierung vermeiden

Zu viel Schmiermittel ist fast so schädlich wie zu wenig:
- Überschüssiges Öl/Fett bindet Sand, Staub und Salzkristalle → abrasiver Brei
- Fettreste auf Ratschenmechanismen verhindern das Eingreifen der Sperrklinken
- Fett auf Scheiben-Laufflächen kontaminiert Tauwerk (Dyneema verliert Griffigkeit)
- Überschüssiges Fett tropft auf Deck (Flecken, Rutschgefahr)

**Goldene Regel: So wenig wie möglich, so viel wie nötig.**

### 5.4 Schmiermittel-Kompatibilitätsmatrix

| Schmiermittel | Acetal (POM) | Torlon (PAI) | Nylon (PA) | PEEK | Aluminium | Edelstahl | Titan | Kohlefaser |
|--------------|-------------|-------------|-----------|------|-----------|-----------|-------|-----------|
| Harken One Lube | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
| McLube Sailkote | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
| McLube OneDrop | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
| Boeshield T-9 | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
| Silikonspray | ⚠ | ✓ | ⚠ | ✓ | ✓ | ✓ | ✓ | ✓ |
| WD-40 | ✗ | ⚠ | ✗ | ✓ | ✓ | ✓ | ✓ | ⚠ |
| Lithiumfett | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
| Vaseline | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |

Legende: ✓ = kompatibel, ⚠ = bedingt/kurzzeitig, ✗ = nicht verwenden

---

## 6. Verschleißerkennung

### 6.1 Visuelle Inspektion

#### 6.1.1 Scheibenverschleiß erkennen

**Rillentiefe messen:**
Die Rillentiefe ist das primäre Verschleißmaß für Scheiben. Messung mit Tiefenmessschieber oder Profilometer:

1. Tauwerk entfernen.
2. Scheibe reinigen (Schmutz verfälscht Messung).
3. Messschieber-Tiefenmaß am tiefsten Punkt der Rille ansetzen.
4. Referenz: Oberkante der Scheibenflanke.
5. An 4 Stellen messen (0°, 90°, 180°, 270°) → Mittelwert bilden.

**Grenzwerte Rillentiefe (Confidence: documented/estimated):**

| Einsatzart | Akzeptabel | Beobachten | Austausch |
|-----------|-----------|-----------|----------|
| Regattayacht | < 0,3 mm | 0,3–0,5 mm | > 0,5 mm |
| Performance Cruiser | < 0,5 mm | 0,5–0,8 mm | > 0,8 mm |
| Fahrtensegler | < 0,8 mm | 0,8–1,2 mm | > 1,2 mm |
| Blauwasseryacht | < 0,5 mm | 0,5–1,0 mm | > 1,0 mm |
| Charter | < 0,5 mm | 0,5–0,8 mm | > 0,8 mm |

**Rillenform analysieren:**
- **V-förmige Rille:** Normal bei Dyneema-Seilen. Akzeptabel bis zur Grenztiefe.
- **U-förmige Rille:** Normal bei Polyester-Schoten. Akzeptabel bis zur Grenztiefe.
- **Asymmetrische Rille:** Deutet auf Fehlausrichtung des Blocks hin. Ursache beheben!
- **Mehrfach-Rillen:** Verschiedene Tauwerk-Durchmesser verwendet. Ungünstig für Lebensdauer.
- **Scharfkantige Rille:** Gefahr der Tauwerk-Beschädigung. Ggf. entgraten oder tauschen.

#### 6.1.2 Lagergeräusche interpretieren

| Geräusch | Ursache | Dringlichkeit | Maßnahme |
|----------|---------|--------------|----------|
| Leises Surren | Normaler Lagerlauf | Keine | — |
| Knirschen | Salzkristalle im Lager | Mittel | Spülen, Schmieren |
| Kratzen | Abriebpartikel, Korrosion | Hoch | Zerlegen, Reinigen, ggf. Tausch |
| Klicken (rhythmisch) | Einzelne beschädigte Kugel/Nadel | Hoch | Lagersatz tauschen |
| Quietschen | Mangelschmierung | Mittel | Sofort schmieren |
| Rattern | Lockere Teile, Lagerspiel | Hoch | Zerlegen, Spiel prüfen |
| Kein Geräusch, schwergängig | Verformtes Lager, Korrosion | Sehr hoch | Sofort zerlegen |

#### 6.1.3 Farbveränderungen deuten

| Farbe/Veränderung | Material | Ursache | Bewertung |
|------------------|---------|---------|----------|
| Weiße Ablagerung | Alle | Salzausblühung | Normal, reinigen |
| Grüne Patina | Bronze, Messing | Kupferoxidation | Akzeptabel, schützend |
| Braune Verfärbung | Edelstahl | Tea staining, leichte Korrosion | Beobachten |
| Schwarze Verfärbung | Aluminium | Galvanische Korrosion | Kritisch, Ursache finden |
| Vergilbung | Acetal, Nylon | UV-Degradation | Oberflächlich: tolerabel; tief: tauschen |
| Weißer Belag (kreidig) | Polymer | UV-Degradation fortgeschritten | Austausch prüfen |
| Blaue Verfärbung | Edelstahl | Überhitzung (Trockenlauf) | Lager sofort tauschen |
| Rötliche Verfärbung | Edelstahl | Fremdrost (Kontamination) | Reinigen, Quelle finden |

### 6.2 Taktile Prüfung

#### 6.2.1 Leichtgängigkeit prüfen

**Ohne-Last-Test:**
1. Tauwerk entfernen.
2. Scheibe von Hand drehen.
3. Sollte mit leichtem Fingerdruck frei und gleichmäßig rotieren.
4. Rückdrehtest: Scheibe anstupsen, sollte mindestens 2 Umdrehungen frei nachlaufen (Kugellager) bzw. 0,5 Umdrehungen (Gleitlager).

**Unter-Last-Test:**
1. Tauwerk einlegen.
2. Moderate Last anlegen (10–20 kg, z.B. Wasserkanister).
3. Tauwerk ziehen: Block muss leichtgängig umlenken.
4. Ruckartige Bewegung: Kein Blockieren oder Rucken.

#### 6.2.2 Spiel prüfen

**Radiales Spiel (Scheibe wackelt seitlich):**
- Scheibe seitlich bewegen (zwischen Wangen).
- Akzeptabel: <0,5 mm bei Fahrtblöcken, <0,3 mm bei Regattablöcken.
- Zu viel Spiel: Achse oder Lager verschlissen.
- Kein Spiel: Kann auf Verklemmung/Korrosion hindeuten.

**Axiales Spiel (Scheibe bewegt sich auf Achse):**
- Scheibe auf der Achse hin- und herbewegen.
- Akzeptabel: <0,3 mm.
- Zu viel Spiel: Lagerverschleiß, Sicherungsring locker, Achse dünn.

### 6.3 Messtechnische Prüfung

#### 6.3.1 Achsdurchmesser-Verschleiß

**Messprotokoll:**
1. Achse reinigen.
2. Durchmesser an 3 Positionen messen: links, mitte, rechts.
3. An jeder Position 2 Messungen im 90°-Winkel (Ovalisierung erkennen).
4. Ergebnisse protokollieren.

**Grenzwerte:**

| Achsdurchmesser (Nenn) | Min. Durchmesser | Max. Ovalisierung |
|-----------------------|-----------------|------------------|
| 5 mm | 4,95 mm | 0,02 mm |
| 6 mm | 5,94 mm | 0,02 mm |
| 8 mm | 7,92 mm | 0,03 mm |
| 10 mm | 9,90 mm | 0,03 mm |
| 12 mm | 11,88 mm | 0,04 mm |
| 16 mm | 15,85 mm | 0,05 mm |

#### 6.3.2 Scheiben-Bohrung messen

**Messprotokoll:**
1. Scheibe reinigen, Lager entfernen.
2. Bohrung an 3 Positionen messen (wie Achse).
3. Ovalisierung feststellen.
4. Passungsspiel berechnen: Bohrung - Achse = Spiel.

**Grenzwerte Passungsspiel:**

| Lagertyp | Sollspiel | Max. Spiel (Austausch) |
|----------|----------|----------------------|
| Kugellager | 0,01–0,03 mm | 0,08 mm |
| Nadellager | 0,01–0,03 mm | 0,08 mm |
| Gleitlager | 0,03–0,08 mm | 0,15 mm |

#### 6.3.3 Scheiben-Profil messen

**Rillenradius prüfen:**
- Originalrillenradius = ca. Tauwerk-Durchmesser / 2 + 10 %
- Verschlissene Rille: Radius verkleinert sich (V-Form) oder vergrößert sich (Auswaschung)
- Messkugeln verschiedener Durchmesser in Rille legen → Kontaktstelle identifizieren

**Scheibenflanken-Höhe:**
- Flankenhöhe messen (von Rillenboden bis Flankenoberkante)
- Minimum: Tauwerk-Durchmesser × 0,3
- Unter diesem Wert kann Tauwerk aus der Rille springen

### 6.4 Go/No-Go-Kriterien

#### 6.4.1 Sofortiger Austausch (No-Go)

Ein Block ist sofort auszutauschen oder außer Betrieb zu nehmen bei:

1. **Gebrochene Wange** — Kein Reparaturversuch bei tragenden Teilen
2. **Gebrochene Achse** — Sofortige Gefahr des Scheibenverlusts
3. **Kugel-/Nadelbruch** — Kaskadierende Zerstörung
4. **Sichtbare Ermüdungsrisse** — An Achse, Wange oder Scheibe
5. **Ausgebrochene Befestigung** — Block kann sich lösen
6. **Blockierende Scheibe** — Unter Last keine Rotation
7. **Scheibenschlag > 1 mm** — Unwucht, Tauwerk-Schaden
8. **Achsdurchmesser unter Minimum** — Bruchgefahr
9. **Korrosion mit >20 % Querschnittsverlust** — An Achse oder Bolzen

#### 6.4.2 Bedingter Weiterbetrieb (beobachten)

Folgende Befunde erlauben zeitlich begrenzten Weiterbetrieb mit erhöhter Aufmerksamkeit:

1. Leichte Rillenbildung (unter Austauschgrenze)
2. Oberflächliche Korrosion ohne Materialverlust
3. Leicht erhöhtes Lagerspiel (über Soll, unter Maximum)
4. UV-Vergilbung von Polymerteilen (nur Oberfläche)
5. Leicht schwergängige Scheibe (Schmierung hilft)
6. Einzelne fehlende Befestigungsschraube (wenn redundant)

---

## 7. Anlagen-spezifische Wartung

### 7.1 Großschotblöcke

**Belastungsprofil:**
- Höchste kontinuierliche Lasten aller Blöcke
- Dynamische Belastung durch Böen und Seegang
- Ständige Mikrobewegungen (Trimm-Korrekturen)
- Hohe Zyklenzahl pro Segeltag

**Spezifische Wartungshinweise:**
- Kürzere Schmierintervalle (alle 2 Monate bei aktiver Nutzung)
- Lager jährlich prüfen (Kugellager: Laufgeräusch, Leichtgängigkeit)
- Scheibe halbjährlich auf Rillenbildung prüfen
- Befestigung vierteljährlich nachziehen (Vibration lockert Schrauben)
- Bei Ratschenblöcken: Ratschenmechanismus vierteljährlich prüfen
- Traveller-Wagen und -Schienen in die Wartung einbeziehen

**Typische Lebensdauer (Confidence: estimated):**
- Scheibe: 5–8 Jahre (Fahrt), 2–3 Jahre (Regatta)
- Kugellager: 3–5 Jahre (Fahrt), 1–2 Jahre (Regatta)
- Block komplett: 10–15 Jahre (Fahrt), 5–8 Jahre (Regatta)

### 7.2 Fallenblöcke (Halyard Blocks)

**Belastungsprofil:**
- Hohe statische Lasten (Segel steht stundenlang)
- Wenige, aber extreme Lastzyklen (Segel setzen/bergen)
- Oft Mastmontage → erschwerte Wartung
- Exposition zu Wetter und UV

**Spezifische Wartungshinweise:**
- Schmierung vor jedem Segel-Setzen (McLube Sailkote auf Scheibe)
- Mastblöcke bei Mastlegen warten (sonst nur mit Bosunchair erreichbar)
- Besonderes Augenmerk auf Fallenumlenkungen am Mastfuß (hohe Richtungsänderung)
- Interne Fallenumlenkungen (im Mast): bei Rigg-Check alle 2–3 Jahre inspizieren
- Achskorrosion durch eingeschlossene Feuchtigkeit im Mast → Wasserablauf prüfen

**Typische Lebensdauer:**
- Scheibe: 8–12 Jahre (weniger Zyklen)
- Lager: 5–8 Jahre
- Block komplett: 15–20 Jahre

### 7.3 Spinnakerblöcke

**Belastungsprofil:**
- Hohe dynamische Lasten (Spi schlägt, Böen)
- Schockbelastung bei Halsen
- Oft Snatchblöcke → Öffnungsmechanismus belastet
- Weniger Betriebsstunden, aber intensive Nutzung

**Spezifische Wartungshinweise:**
- Snatchblock-Mechanismus vor jedem Spi-Segeln prüfen
- Verriegelung testen (Muss unter Last sicher schließen!)
- Schmierung des Gelenkmechanismus
- Schäkel und Verbindungen prüfen (Schnellschäkel, Softschäkel)
- Barberholer-Blöcke: oft vergessen, aber hohe Umlenkkraft

### 7.4 Reffblöcke

**Belastungsprofil:**
- Mittlere bis hohe Lasten
- Kritisch: werden bei Starkwind benötigt → müssen IMMER funktionieren
- Oft in schwer zugänglichen Positionen (am Baum, am Mast)
- Salzwasser und Spritzwasser direkt ausgesetzt

**Spezifische Wartungshinweise:**
- Höchste Wartungspriorität! Ein versagender Reffblock bei 35 kn Wind ist gefährlich
- Monatliche Funktionsprüfung (auch wenn kein Reff nötig war)
- Schmierung alle 2 Monate
- Vor jeder Langfahrt und vor jeder Sturmsaison inspizieren
- Ersatz-Schäkel und Notfall-Blöcke bereithalten

### 7.5 Traveller-Blöcke und -Wagen

**Belastungsprofil:**
- Hohe seitliche Kräfte
- Ständige Bewegung auf Schiene
- Traveller-Wagen: Kugellager in Schiene → eigene Wartung
- Enge Toleranzen (Wagen muss frei gleiten)

**Spezifische Wartungshinweise:**
- Schiene reinigen (Süßwasser, Bürste) und schmieren (McLube Sailkote)
- Wagenlager prüfen (Kugeln, Käfig, Laufflächen)
- Traveller-Blöcke: Standard-Blockwartung
- Traveller-Endanschläge prüfen
- Stopper/Klemmen am Traveller warten

### 7.6 Niederholerblöcke (Vang Blocks)

**Belastungsprofil:**
- Hohe Kompressionslasten
- Wenig Rotation, mehr statisch
- Oft mit Flaschenzug-System → Mehrfachblöcke

**Spezifische Wartungshinweise:**
- Jede Scheibe eines Mehrfachblocks einzeln prüfen
- Schwenk-/Universalgelenk am Mastbeschlag schmieren
- Bolzen auf Verformung prüfen (Kompressionslast)
- Doppel-/Dreifachblock: Achsausrichtung über alle Scheiben prüfen

### 7.7 Umlenkblöcke unter Deck

**Belastungsprofil:**
- Moderate Lasten
- Geschützte Position (kein UV, kein Salzspritz)
- Aber: schlechtere Belüftung, Feuchtigkeit kann sich stauen

**Spezifische Wartungshinweise:**
- Längere Wartungsintervalle möglich (Schmierung halbjährlich)
- Auf Kondenswasserbildung achten (besonders in Bilgennähe)
- Befestigung prüfen (Deck-Durchbrüche können undicht werden)
- Seltene Inspektion → umso gründlicher wenn einmal geöffnet

### 7.8 Backstag-Blöcke und Achterstagspanner

**Belastungsprofil:**
- Hohe statische Dauerlast (Mastkompression)
- Dynamische Spitzen bei Böen und Seegang
- Oft exponierte Position (UV, Salzwasser)
- Teilweise in hydraulische Systeme integriert

**Spezifische Wartungshinweise:**
- Befestigung am Heck/Spiegel besonders sorgfältig prüfen
- Schäkel und Gabeln auf Ermüdungsrisse kontrollieren
- Bei Hydraulik-Achterstagspannern: Hydraulikdichtungen in die Blockwartung integrieren
- Backstag-Umlenkblöcke bei Gaffelschiffen: Erhöhte Aufmerksamkeit wegen asymmetrischer Belastung
- Lager halbjährlich schmieren (Dauerbelastung beschleunigt Verschleiß)
- Geteiltes Backstag: Beide Seiten gleichmäßig warten

**Typische Lebensdauer:**
- Scheibe: 6–10 Jahre (wenig Rotation, aber hohe Last)
- Lager: 4–6 Jahre (Standlast fördert Brinelling)
- Achse: 10–15 Jahre

### 7.9 Genuaschot-Barberholer

**Belastungsprofil:**
- Mittlere Lasten
- Häufige Verstellung (bei wechselndem Kurs)
- Oft vergessen in der Wartung (sekundäres System)
- Salzwasserspritz im Vorschiffsbereich

**Spezifische Wartungshinweise:**
- Bei jeder Inspektion bewusst einbeziehen (wird häufig vergessen)
- Barberholer-Blöcke oft auf Schienen → Schienenwartung einbeziehen
- Kontrollstring-Blöcke (Leinen-Führung) mitprüfen
- Tauwerk-Zustand an diesen Blöcken prüfen (oft dünnes Tauwerk → schnellerer Verschleiß)
- Schmierung vierteljährlich

### 7.10 Lazy-Jack-Blöcke und Faulenzer-System

**Belastungsprofil:**
- Geringe bis mittlere Lasten
- Wenig dynamische Beanspruchung
- Aber: permanente UV-Exposition am Baum
- Oft kleine, günstige Blöcke → weniger robust

**Spezifische Wartungshinweise:**
- UV-Schutz besonders wichtig (Baum-Position = maximale Sonneneinstrahlung)
- Kleine Blöcke tendieren zu schnellerem Verschleiß bei Vernachlässigung
- Bei klappbaren Lazy-Jack-Systemen: Gelenke und Schäkel mitschmieren
- Jährliche Inspektion ausreichend bei reinem Fahrteneinsatz
- Bei Austausch: UV-stabilisierte Modelle wählen

### 7.11 Outhaul- und Cunningham-Blöcke

**Belastungsprofil:**
- Mittlere Lasten
- Position am Baum (Outhaul) bzw. Hals (Cunningham)
- Oft in mehrstufigen Flaschenzügen → Systemwirkungsgrad kritisch
- Salzwasser und UV exponiert

**Spezifische Wartungshinweise:**
- Alle Blöcke im Flaschenzug-System gleichzeitig warten
- Systemwirkungsgrad durch Funktionsprüfung bewerten
- Baum-interne Outhaul-Systeme: Bei Baum-Service mitwarten
- Cunningham-Blöcke am Mast: Oft vergessen → in Rigg-Check einbeziehen
- Schmierung alle 3 Monate (mittlere Beanspruchung)

### 7.12 Regatta-spezifische Blocksysteme

**Besonderheiten bei Regattayachten:**
- Twing-/Tweaker-Blöcke: Kleine Blöcke unter hoher dynamischer Last
- Barber-Blöcke: Präzise Genua-Trimm-Kontrolle
- Trimmleinen-Blöcke (Outhaul, Cunningham, Baumniederholer): Viele kleine Blöcke
- Fock-/Genua-Schot-Selbstwendeblöcke: Komplexer Mechanismus
- Spinnaker-System: Halsen-Blöcke, Topping-Lift, Barberholer

**Wartungsstrategie für Regattayachten:**
1. Vor jeder Regatta: Schnellinspektionsrunde (15 min für alle Blöcke)
2. Alle Blöcke auf Leichtgängigkeit prüfen (Finger-Test)
3. Alle Ratschenblöcke auf Funktion testen
4. Alle Snatchblöcke auf Verriegelung testen
5. Schmierung aller Lager (McLube OneDrop, je 2 Tropfen)
6. McLube Sailkote auf alle Scheiben
7. Nach der Regatta: Süßwasserspülung aller Blöcke
8. Monatlich: Vollinspektion der 5 meistbelasteten Blöcke (rotierend)
9. Halbjährlich: Alle Lager und Scheiben detailliert inspizieren
10. Jährlich: Alle Lagersätze tauschen (präventiv bei Regatta-Intensiveinsatz)

**Budgetplanung Regatta-Blockwartung:**

| Posten | Pro Saison | Anmerkung |
|--------|-----------|----------|
| Schmiermittel | 60–80 € | Harken One Lube + McLube Sailkote |
| Lagersätze (präventiv) | 200–400 € | Je nach Blockanzahl und -größe |
| Scheiben (bei Bedarf) | 50–150 € | 1–3 Scheiben pro Saison typisch |
| Ratschenfedern | 20–40 € | 1 Service Kit pro Saison |
| Sonstiges (Schäkel, Sicherungsringe) | 30–50 € | Kleineisen |
| **Gesamt pro Saison** | **360–720 €** | **Für eine typische 10m-Regattayacht** |

---

## 8. Fehlerbild-Atlas

### 8.1 Fehlerbild F-W01: Schwergängige Scheibe

**Erscheinungsbild:**
Scheibe rotiert nur unter erhöhtem Kraftaufwand oder gar nicht. Tauwerk lässt sich schwer durch den Block ziehen. Beim Trimmen erhöhter Kraftbedarf.

**Ursachen (Häufigkeit):**
1. Mangelschmierung (40 %) — Trockenes Lager durch fehlende oder ausgewaschene Schmierung
2. Salzkristalle im Lager (25 %) — Kristallbildung zwischen Kugeln/Nadeln und Lauffläche
3. Korrosion der Achse (15 %) — Oberflächenkorrosion erhöht Reibung
4. Verbogene Achse (10 %) — Durch Überlast oder Schlag
5. Fremdkörper (5 %) — Sand, Textilfasern, Korrosionsprodukte im Lager
6. Deformiertes Lager (5 %) — Durch Überlast (Brinelling) oder thermische Deformation

**Diagnose-Schritte:**
1. Sichtprüfung auf offensichtliche Fremdkörper
2. Süßwasserspülung und Schmierung → Besserung?
3. Wenn nein: Block zerlegen, Lager inspizieren
4. Achse auf Rundheit messen
5. Laufbahnen auf Pitting/Riefen prüfen

**Behebung:**
- Stufe 1: Spülen + Schmieren (löst 60 % aller Fälle)
- Stufe 2: Zerlegen + Reinigen + Neuschmierung (löst weitere 25 %)
- Stufe 3: Lager tauschen (löst weitere 10 %)
- Stufe 4: Achse und/oder Scheibe tauschen (restliche 5 %)

**AYDI-Bewertung:**
- Confidence: visual_medium (kann auf Foto nur indirekt erkannt werden)
- Severity: MEDIUM (Leistungseinschränkung, potenziell sicherheitsrelevant)

### 8.2 Fehlerbild F-W02: Knirschendes/Kratzendes Lager

**Erscheinungsbild:**
Beim Drehen der Scheibe sind deutliche Knirsch- oder Kratzgeräusche hörbar. Unter Last verstärkt sich das Geräusch.

**Ursachen:**
1. Salzkristalle im Lager (35 %)
2. Korrosionsprodukte in Lauffläche (25 %)
3. Sand/Partikel im Lager (20 %)
4. Beschädigte Kugeln/Nadeln (10 %)
5. Beschädigte Lauffläche (Pitting) (10 %)

**Diagnose:**
1. Geräusch lokalisieren: Lager oder Scheibe?
2. Spülen → Geräusch weg? → Salz/Sand
3. Schmieren → Geräusch weg? → Mangelschmierung
4. Geräusch bleibt → Zerlegen und inspizieren

**Behebung:**
- Leicht: Spülen, reinigen, schmieren
- Mittel: Lager reinigen, Kugeln/Nadeln prüfen und ggf. tauschen
- Schwer: Lager komplett tauschen, ggf. Achse/Scheibe bei Laufflächen-Schaden

### 8.3 Fehlerbild F-W03: Scheibenschlag (Wobble)

**Erscheinungsbild:**
Scheibe dreht nicht plan, sondern „eiert". Unter Last kann Tauwerk aus der Rille springen.

**Ursachen:**
1. Verbogene Achse (40 %)
2. Ausgeschlagene/ovale Achsbohrung (30 %)
3. Einseitig verschlissenes Lager (15 %)
4. Lockere Achssicherung (10 %)
5. Deformierte Scheibe (5 %)

**Diagnose:**
1. Achssicherung prüfen (Sicherungsring, Bolzen fest?)
2. Achse ausbauen und auf ebener Fläche rollen (gerade?)
3. Scheiben-Bohrung messen (Ovalisierung?)
4. Lagerspiel prüfen

**Behebung:**
- Verbogene Achse: Tausch (Richten ist nicht dauerhaft!)
- Ovale Bohrung: Scheibe tauschen
- Lockere Sicherung: Nachsichern, ggf. neue Sicherungselemente

### 8.4 Fehlerbild F-W04: Ausgebrochene Scheibenflanke

**Erscheinungsbild:**
Ein Stück der Scheibenflanke ist abgebrochen. Tauwerk kann seitlich herausrutschen.

**Ursachen:**
1. Seitliche Überlast (falsche Ausrichtung) (50 %)
2. Materialermüdung (25 %)
3. Schlagbeschädigung (15 %)
4. UV-Versprödung bei Polymerscheiben (10 %)

**Behebung:**
- SOFORT tauschen. Gebrochene Flanken können Tauwerk beschädigen und sind Sicherheitsrisiko.
- Ursache analysieren: Ist der Block richtig ausgerichtet? Stimmt die Scheibenbreite zum Tauwerk?

### 8.5 Fehlerbild F-W05: Korrosion an Achse/Bolzen

**Erscheinungsbild:**
Braune oder schwarze Verfärbung, Lochfraß (Pitting), Raue Oberfläche, im Extremfall Materialverlust.

**Ursachen:**
1. Crevice-Korrosion (Spaltkorrosion) im Lagerspalt (40 %)
2. Galvanische Korrosion (verschiedene Metalle) (25 %)
3. Mangelhafte Materialqualität (304 statt 316L) (15 %)
4. Fehlende Süßwasserspülung (10 %)
5. Beschädigte Passivschicht (Kratzer) (10 %)

**Diagnose:**
1. Korrosionsart identifizieren (flächig vs. Lochfraß vs. Spalt)
2. Material prüfen (Magnettest: 304 ist leicht magnetisch, 316L nicht)
3. Kontaktpartner identifizieren (galvanisches Paar?)

**Behebung:**
- Oberflächliche Korrosion: Schleifen (Körnung 400+), Polieren, Passivierung (Beizen)
- Lochfraß mit >10 % Querschnittsverlust: Tausch
- Galvanische Korrosion: Isolierung schaffen (Kunststoffbuchse, Duralac)

### 8.6 Fehlerbild F-W06: Ratschenmechanismus versagt

**Erscheinungsbild:**
Ratschenblock greift nicht in Halterichtung, rutscht durch, oder blockiert in beide Richtungen.

**Ursachen (bei Durchrutschen):**
1. Verschmutzte/verklebte Sperrklinken (35 %)
2. Gebrochene/ermüdete Federn (25 %)
3. Abgerundete Klinken oder Zahnprofil (20 %)
4. Falsche Schmierung (Fett auf Klinken) (15 %)
5. Montagefehler (5 %)

**Ursachen (bei Blockierung in beide Richtungen):**
1. Verklemmte Sperrklinke (40 %)
2. Fremdkörper im Mechanismus (30 %)
3. Verformter Ratschenring (20 %)
4. Montagefehler (10 %)

**Behebung:**
- Ratschenmechanismus zerlegen (s. Abschnitt 4.4)
- Reinigen, Federn prüfen/tauschen, Klinken prüfen/tauschen
- Minimal schmieren (NUR McLube Sailkote, KEIN Fett)
- Korrekt zusammenbauen, Funktionstest vor Einbau

### 8.7 Fehlerbild F-W07: Snatchblock-Verriegelung versagt

**Erscheinungsbild:**
Snatchblock öffnet sich unter Last oder lässt sich nicht mehr öffnen/schließen.

**Ursachen (öffnet unter Last):**
1. Verschlissener Verriegelungsmechanismus (40 %)
2. Korrodiertes Gelenk (25 %)
3. Deformierte Verriegelungsnase (20 %)
4. Überlast (15 %)

**Ursachen (öffnet/schließt nicht):**
1. Korrosion im Gelenk (50 %)
2. Verformung durch Schlag (25 %)
3. Salzkristalle im Mechanismus (25 %)

**Behebung:**
- Gelenk reinigen und schmieren
- Verriegelung auf Verschleiß prüfen
- Bei Verformung: Block tauschen (Sicherheitsrisiko!)
- Regelmäßige Schmierung des Gelenks (Harken One Lube, 1 Tropfen)

### 8.8 Fehlerbild F-W08: Tauwerk-Schäden durch Block

**Erscheinungsbild:**
Tauwerk zeigt lokalen Verschleiß, Aufrauhung, Abrieb oder Kernschädigung an der Stelle, wo es über den Block läuft.

**Ursachen:**
1. Gerillte Scheibe schneidet ins Tauwerk (35 %)
2. Scharfe Kante an gebrochener Scheibenflanke (25 %)
3. Korrodierte/raue Scheibe (15 %)
4. Zu kleine Scheibe für Tauwerk-Durchmesser (10 %)
5. Fehlausrichtung → Tauwerk reibt an Wange (10 %)
6. Blockierende Scheibe → Tauwerk reibt statt zu rollen (5 %)

**Behebung:**
- Scheibe inspizieren und ggf. tauschen
- Korrekte Scheibengröße für Tauwerk wählen (Rillenradius ≥ halber Tauwerk-Ø, d.h. Rille etwas größer als der Tauwerk-Radius)
- Block-Ausrichtung korrigieren
- Tauwerk an Schadstelle abschneiden (wenn tragfähiger Kern noch vorhanden) oder ersetzen

### 8.9 Fehlerbild F-W09: Lose Decksbefestigung

**Erscheinungsbild:**
Block wackelt auf dem Deck. Befestigungsschrauben sind locker oder ausgerissen. Unter Last bewegt sich der Block.

**Ursachen:**
1. Vibration hat Schrauben gelockert (40 %)
2. Glasfaser-Kernmaterial unter Befestigung gebrochen (25 %)
3. Unterdimensionierte Befestigung (15 %)
4. Korrodierte Befestigungsschrauben (10 %)
5. Fehlende Gegenmuttern/Unterlegscheiben (10 %)

**Behebung:**
- Schrauben nachziehen (mit Drehmoment)
- Bei ausgerissenen Schrauben: Größere Schrauben oder Helicoil-Einsätze
- Bei Kernbruch: Kernverstärkung (Epoxid, Backing Plate)
- Backing Plate unter Deck installieren (verteilt Last)
- Schraubensicherung (Loctite 243) verwenden

### 8.10 Fehlerbild F-W10: UV-geschädigte Polymerteile

**Erscheinungsbild:**
Kunststoffteile des Blocks sind verfärbt (vergilbt, ausgeblichen), spröde, zeigen Oberflächenrisse oder Verkreidung.

**Ursachen:**
- Langzeit-UV-Exposition ohne Schutz
- Minderwertiger UV-Stabilisator im Material
- Tropische/subtropische Klimazone (UV-Index 10+)

**Diagnose:**
1. Farbvergleich mit neuem Referenzteil
2. Biegetest: Spröde Teile brechen, anstatt sich zu biegen
3. Oberflächentest: Kreideabrieb beim Reiben
4. Tiefe prüfen: Nur Oberfläche oder durchgehend?

**Behebung:**
- Oberflächliche Degradation (<0,5 mm): Tolerabel, beobachten
- Tiefe Degradation: Betroffene Teile tauschen
- Prävention: UV-Schutzlack, Blockabdeckungen, Persenning

### 8.11 Fehlerbild F-W11: Galvanische Korrosion am Block

**Erscheinungsbild:**
Weißer, kristalliner Belag auf Aluminium-Wangen (Aluminiumoxid). Schwarze Verfärbung an Kontaktstellen zwischen verschiedenen Metallen. Materialverlust am unedleren Partner.

**Ursachen:**
1. Edelstahl-Achse in Aluminium-Scheibe (ohne Isolierung)
2. Bronze-Schäkel an Aluminium-Block
3. Kohlefaser-Befestigung an Aluminium-Block
4. Edelstahl-Schrauben in Aluminium-Deck-Insert (ohne Duralac)

**Diagnose:**
1. Kontaktpartner identifizieren
2. Elektrochemische Spannungsreihe konsultieren
3. Potentialdifferenz berechnen (>0,3 V = problematisch in Seewasser)

**Behebung:**
- Kontaktpartner elektrisch isolieren (Kunststoffbuchsen, Unterlegscheiben)
- Duralac oder Tef-Gel auf Kontaktflächen
- Bei fortgeschrittener Korrosion: betroffenes Teil tauschen
- Materialkompatibilität bei Neuinstallation beachten

### 8.12 Fehlerbild F-W12: Ermüdungsriss im Block

**Erscheinungsbild:**
Haarfeiner Riss in Wange, Achse oder Scheibe. Oft nur unter Belastung sichtbar (Riss öffnet sich). Kann sich schlagartig zum Bruch ausweiten.

**Ursachen:**
1. Zyklische Überlast (Dauerbetrieb nahe Lastgrenze) (35 %)
2. Materialermüdung (Lebensdauer erreicht) (25 %)
3. Fertigungsfehler (Einschlüsse, Kerben) (15 %)
4. Korrosionsmüdigkeit (Korrosion + zyklische Last) (15 %)
5. Schlagbeschädigung mit Anriss (10 %)

**Diagnose:**
1. Sichtprüfung unter Last (Riss öffnet sich)
2. Eindringprüfung (Farbeindringverfahren, z.B. Diffu-Therm)
3. Magnetpulverprüfung (nur ferromagnetische Materialien)
4. Unter Lupe (10x): Verlauf des Risses verfolgen

**Behebung:**
- SOFORT außer Betrieb nehmen. Ermüdungsrisse sind nicht reparabel.
- Betroffenes Teil (Wange, Achse, Scheibe) oder ganzen Block tauschen.
- Ursachenanalyse: War der Block unterdimensioniert? Liegt systematische Überlast vor?

---

## 9. Troubleshooting

### 9.1 Entscheidungsbaum: Block dreht schwer

```
Block dreht schwer
│
├─ Tauwerk entfernen → Dreht der Block frei?
│  ├─ JA → Problem liegt am Tauwerk/Ausrichtung
│  │  ├─ Tauwerk zu dick für Scheibe? → Kleineres Tauwerk oder größeren Block
│  │  ├─ Block falsch ausgerichtet? → Ausrichtung korrigieren
│  │  └─ Tauwerk verformt/verknotet? → Tauwerk erneuern
│  │
│  └─ NEIN → Problem im Block
│     ├─ Süßwasser spülen + schmieren → Besserung?
│     │  ├─ JA → Salz/Mangelschmierung war Ursache → Intervalle verkürzen
│     │  └─ NEIN → Weiter
│     │
│     ├─ Block zerlegen → Lager inspizieren
│     │  ├─ Kugeln/Nadeln beschädigt → Lagersatz tauschen
│     │  ├─ Laufflächen beschädigt → Scheibe/Achse tauschen
│     │  ├─ Fremdkörper im Lager → Reinigen, Ursache finden
│     │  └─ Achse verbogen → Achse tauschen
│     │
│     └─ Alles sauber und intakt? → Zusammenbauen mit frischer Schmierung
│        ├─ Dreht frei → Problem gelöst
│        └─ Dreht immer noch schwer → Block defekt, austauschen
```

### 9.2 Entscheidungsbaum: Ungewöhnliche Geräusche

```
Ungewöhnliches Geräusch
│
├─ Art des Geräuschs?
│  ├─ Knirschen/Kratzen
│  │  ├─ Spülen → Weg? → Salz/Sand
│  │  └─ Bleibt? → Lager inspizieren (Pitting, Korrosion)
│  │
│  ├─ Klicken (rhythmisch)
│  │  ├─ Proportional zur Drehzahl? → Beschädigte Kugel/Nadel
│  │  └─ Unregelmäßig? → Lockeres Teil (Sicherungsring, Schraube)
│  │
│  ├─ Quietschen
│  │  ├─ Schmieren → Weg? → Mangelschmierung
│  │  └─ Bleibt? → Achse/Lager korrodiert, zerlegen
│  │
│  ├─ Rattern
│  │  ├─ Unter Last? → Ausgeschlagenes Lager, Spiel prüfen
│  │  └─ Im Leerlauf? → Lose Scheibe, Sicherung prüfen
│  │
│  └─ Knacken (einzeln, unter Last)
│     └─ SOFORT prüfen! Möglicher Riss oder Bruchbeginn!
```

### 9.3 Entscheidungsbaum: Ratschenblock funktioniert nicht

```
Ratschenblock greift nicht
│
├─ In welche Richtung ist das Problem?
│  ├─ Greift nicht (rutscht durch)
│  │  ├─ Reinigen (Klinken frei?) → Besserung?
│  │  │  ├─ JA → Verschmutzung war Ursache
│  │  │  └─ NEIN → Weiter
│  │  ├─ Federn prüfen (alle intakt? Spannung?)
│  │  │  ├─ Feder gebrochen → Feder tauschen
│  │  │  └─ Federn OK → Weiter
│  │  ├─ Klinken prüfen (Kanten scharf?)
│  │  │  ├─ Klinken abgerundet → Klinken tauschen
│  │  │  └─ Klinken OK → Zahnprofil prüfen
│  │  └─ Zahnprofil verschlissen → Ratschenring tauschen
│  │
│  └─ Blockiert in beide Richtungen
│     ├─ Fremdkörper im Mechanismus? → Reinigen
│     ├─ Verklemmte Klinke? → Klinke lösen, Gelenk schmieren
│     ├─ Verformter Ring? → Ring tauschen
│     └─ Falsch montiert? → Demontieren, korrekt montieren
```

### 9.4 Entscheidungsbaum: Tauwerk wird beschädigt

```
Tauwerk zeigt Verschleiß am Block
│
├─ Wo am Block ist der Verschleiß?
│  ├─ An der Scheibe (Lauffläche)
│  │  ├─ Scheibe gerillte? → Scheibe tauschen
│  │  ├─ Scheibe rau? → Scheibe polieren oder tauschen
│  │  └─ Scheibe OK? → Tauwerk-Durchmesser zum Block passend?
│  │
│  ├─ An der Wange (Seitenfläche)
│  │  ├─ Block zu schmal für Tauwerk → Größeren Block verwenden
│  │  └─ Block falsch ausgerichtet → Ausrichtung korrigieren
│  │
│  └─ Am Kopf/Fuß (Einlauf/Auslauf)
│     ├─ Scharfe Kanten? → Kanten entgraten, verrunden
│     └─ Führung fehlt? → Leitöse oder Zusatzblock installieren
```

### 9.5 Entscheidungsbaum: Block löst sich von Befestigung

```
Block löst sich / wackelt
│
├─ Befestigungsart?
│  ├─ Schraubmontage
│  │  ├─ Schrauben locker → Nachziehen mit Drehmoment + Schraubensicherung
│  │  ├─ Gewinde ausgerissen → Helicoil oder größere Schrauben
│  │  └─ Backing Plate gebrochen → Neue, größere Backing Plate
│  │
│  ├─ Bolzenmontage
│  │  ├─ Bolzen verbogen → Bolzen tauschen (nächste Größe?)
│  │  ├─ Bohrung ausgeschlagen → Buchse einsetzen
│  │  └─ Splint/Mutter fehlt → Ersetzen
│  │
│  ├─ Schäkelmontage
│  │  ├─ Schäkelbolzen locker → Festziehen + Sicherungsdraht
│  │  ├─ Schäkel verformt → Schäkel tauschen (nie richten!)
│  │  └─ Schäkel zu klein → Nächste Größe verwenden
│  │
│  └─ Loop-/Dyneema-Befestigung
│     ├─ Loop verschlissen → Neuen Loop anfertigen/kaufen
│     └─ Scheuerstelle am Loop → Schutzschlauch verwenden
```

---

## 10. FAQ

### 10.1 Allgemeine Wartungsfragen

**F1: Wie oft muss ich meine Blöcke wirklich warten?**
A: Das hängt stark von der Nutzung und dem Revier ab. Als Minimum für einen Salzwasser-Freizeitsegler: Süßwasserspülung nach jedem Segeltag, Schmierung alle 3 Monate, Inspektion jährlich. Regattasegler sollten Lager monatlich schmieren und halbjährlich inspizieren. Blauwassersegler sollten wöchentlich Funktionsprüfungen durchführen und vierteljährlich schmieren. Im Zweifelsfall gilt: Lieber einmal zu viel als einmal zu wenig.

**F2: Kann ich alle Blöcke gleichzeitig warten?**
A: Ja, das ist sogar empfohlen. Planen Sie einen „Block-Wartungstag" im Winterlager ein. Alle Blöcke demontieren, systematisch zerlegen, reinigen, inspizieren, schmieren, zusammenbauen. Rechnen Sie mit ca. 30 Minuten pro Block für eine Vollinspektion. Bei 20 Blöcken ist das ein voller Arbeitstag.

**F3: Muss ich original Herstellerersatzteile verwenden?**
A: Für sicherheitsrelevante Teile (Achsen, Lager, Wangen) empfehlen wir dringend Originalteile. Die Toleranzen sind eng, und ein nicht passgenauer Ersatz kann zu vorzeitigem Versagen führen. Für Verbrauchsteile (Schmiermittel, Sicherungsringe, Unterlegscheiben) sind kompatible Alternativen oft akzeptabel.

**F4: Kann ich Blöcke im Ultraschallbad reinigen?**
A: Ja, Ultraschallreinigung ist hervorragend für Blockteile. Verwenden Sie ein mildes Reinigungsmittel (kein Aceton, keine aggressiven Entfetter). Lager und Kugeln profitieren besonders. Polymerteil (Scheiben, Gehäuse) bei niedriger Leistung und kurzer Zeit (max. 5 min) reinigen. Danach gründlich trocknen und sofort schmieren.

**F5: Was mache ich, wenn ein Block auf See versagt?**
A: Notreparatur-Optionen: (1) Reserveblock einsetzen (immer mitführen!). (2) Provisorischen Block aus einem weniger kritischen System umhängen. (3) Tauwerk direkt über Beschlag führen (erhöhte Reibung, aber funktional). (4) Schäkel als Umlenkpunkt verwenden (nur Notfall). NIEMALS einen blockierenden Block unter Last ausbauen — zuerst Last wegnehmen (Segel bergen/fieren).

**F6: Wie lagere ich Ersatzblöcke an Bord richtig?**
A: Kühl, trocken, UV-geschützt. Idealerweise in einem Beutel mit Korrosionsschutz (VCI-Beutel). Leicht geschmiert lagern. Nicht in der Bilge (Feuchtigkeit) oder im Cockpitschapp (UV durch transparenten Deckel). Vor Einsatz Funktionsprüfung — auch gelagerte Blöcke können Standschäden entwickeln.

**F7: Gibt es eine Faustregel, wie viele Ersatzblöcke ich an Bord haben sollte?**
A: Für Küstenfahrt: 1–2 Universalblöcke passender Größe. Für Langfahrt/Blauwasser: je 1 Block pro kritischem System (Großschot, Fall, Reff) plus 2–3 Universalblöcke. Für Regatta: kompletter Satz Ersatzblöcke für das primäre Trimmsystem.

### 10.2 Schmierungsfragen

**F8: Kann ich normales Maschinenöl verwenden?**
A: Nein. Maschinenöl (Motoröl) ist nicht salzwasserbeständig und kann Polymerlager angreifen. Verwenden Sie ausschließlich marine-spezifische Schmiermittel (Harken One Lube, McLube, oder gleichwertig).

**F9: Ist Silikonspray eine gute Alternative zu teureren Spezialölen?**
A: Als kurzzeitige Notlösung akzeptabel, aber keine Dauerlösung. Silikonspray hat geringere Tragfähigkeit und verdampft schneller. Für Scheiben-Laufflächen ist es brauchbar, für Lager nicht ausreichend. Investieren Sie in ein gutes Lageröl — eine 100-ml-Flasche Harken One Lube reicht für ein Jahr und kostet weniger als eine einzige Ersatzscheibe.

**F10: Kann ich Vaseline als Blockschmiermittel verwenden?**
A: Vaseline (Petroleum Jelly) ist materialverträglich und kurzzeitig wirksam, aber als Dauerschmierung nicht ideal: Sie wird bei Hitze zu dünn und bei Kälte zu fest. Als Notfall-Schmiermittel auf See akzeptabel, bei der nächsten Gelegenheit durch geeignetes Produkt ersetzen. Vorteil: Vaseline bindet weniger Schmutz als viele Fette.

**F11: Wie schmiere ich interne Fallblöcke im Mast?**
A: Bei stehendem Mast: McLube Sailkote in den Mastkanal sprühen (erreicht die Blöcke von oben). Bei Mastlegen: Blöcke demontieren und normal warten. Wenn die Blöcke fest eingebaut sind: Sprühröhrchen-Verlängerung verwenden, um das Schmiermittel direkt an die Lagerstelle zu bringen.

**F12: Muss ich nach dem Süßwasserspülen immer nachschmieren?**
A: Idealerweise ja, zumindest ein kurzer Sprühstoß McLube Sailkote. Die Süßwasserspülung entfernt Salz, aber auch Teile der Schmierung. In der Praxis: Wenn Sie regelmäßig spülen (nach jedem Segeltag), reicht es, nach jeder 3.–4. Spülung nachzuschmieren.

### 10.3 Verschleißfragen

**F13: Woran erkenne ich, dass ein Kugellager am Ende ist?**
A: Eindeutige Zeichen: (1) Spürbares Knirschen bei Rotation, das nach Reinigung/Schmierung nicht verschwindet. (2) Sichtbares Pitting auf Kugeln oder Laufflächen (10x Lupe). (3) Deutlich erhöhtes Lagerspiel. (4) Einzelne flache Stellen auf Kugeln (Brinelling). (5) Verfärbung der Kugeln/Laufflächen (Blaulauf = Überhitzung).

**F14: Wie lange halten Blöcke wirklich?**
A: Bei guter Wartung: Fahrtsegler 15–25 Jahre für den Block als Einheit, mit 1–3 Lagertauschen und ggf. 1 Scheibentausch in dieser Zeit. Regattayachten: 5–10 Jahre mit jährlichem Lagertausch. Charter-Yachten: 8–12 Jahre. Die Wangen (Gehäuse) halten am längsten — Lager und Scheiben sind die Verschleißteile.

**F15: Ab welcher Rillentiefe muss die Scheibe getauscht werden?**
A: Fahrtsegler: >1,0 mm. Regatta: >0,5 mm. Blauwasser: >1,0 mm (aber konservativere Eigner tauschen bei 0,8 mm). Wichtiger als die absolute Tiefe ist die Form: Eine symmetrische, saubere Rille ist weniger problematisch als eine scharfkantige, asymmetrische Rille, die das Tauwerk beschädigt.

**F16: Kann ich Scheiben nachbearbeiten statt tauschen?**
A: Bei Aluminiumscheiben: Theoretisch ja (Aufbohren, neue Rille drehen), aber in der Praxis selten wirtschaftlich. Die Kosten für eine CNC-Nachbearbeitung liegen oft nahe am Preis einer Neuteils. Bei Kunststoff-Scheiben: Nein, Nachbearbeitung verändert die Materialstruktur (offene Fasern, veränderte Oberfläche). Empfehlung: Neue Scheibe.

**F17: Was bedeuten die verschiedenen Geräusche meines Blocks?**
A: Leises Surren = normal. Knirschen = Salz/Sand im Lager (spülen!). Quietschen = trocken (schmieren!). Rhythmisches Klicken = beschädigte Kugel/Nadel (Lager tauschen). Rattern = zu viel Lagerspiel (inspizieren). Knacken unter Last = SOFORT prüfen (möglicher Riss!).

### 10.4 Herstellerspezifische Fragen

**F18: Sind Harken-Blöcke wartungsintensiver als Lewmar?**
A: Nein, grundsätzlich nicht. Harken-Blöcke verwenden oft mehr Kugellager (höhere Leichtgängigkeit), die regelmäßig geschmiert werden wollen. Lewmar-Blöcke haben teilweise Composite-Lager, die weniger Schmierung benötigen. Der Wartungsaufwand ist bei sachgemäßer Pflege vergleichbar. Wichtiger als die Marke ist die konsequente Durchführung der Wartung.

**F19: Kann ich Ronstan-Scheiben in Harken-Blöcke einbauen?**
A: In der Regel nein. Scheibendurchmesser, Achsbohrung und Rillengeometrie sind herstellerspezifisch und nicht kompatibel. Verwenden Sie immer Original-Ersatzteile oder explizit kompatibel gekennzeichnete Drittanbieter-Teile.

**F20: Was ist der Vorteil von Harken Carbo-Blöcken bei der Wartung?**
A: Carbo-Blöcke (Composite-Scheiben) zeigen deutlich weniger Rillenbildung als Aluminium-Scheiben, besonders mit Dyneema-Tauwerk. Die Scheiben-Lebensdauer ist ca. 30–50 % länger. Dafür sind sie empfindlicher gegen Schlagbeschädigung (Composite splittert, Aluminium dellt).

### 10.5 Spezielle Situationen

**F21: Mein Block war im Seewasser untergetaucht (Kenterung/Flutung). Was nun?**
A: Sofort: Mit reichlich Süßwasser spülen. Dann: Alle Blöcke zerlegen, in Süßwasser über Nacht einweichen, reinigen, trocknen, inspizieren, schmieren. Besonders auf Lagerschäden achten — Salzwasser im Lager unter Druck dringt tiefer ein als normale Exposition. Lager im Zweifelsfall tauschen.

**F22: Kann ich Blöcke selbst eloxieren lassen?**
A: Theoretisch ja, bei einem lokalen Eloxierbetrieb. Praktisch: Nur sinnvoll bei hochwertigen Blöcken, da die Kosten (30–80 € pro Teil) oft den Neupreis eines einfachen Blocks übersteigen. Hart-Eloxierung (Typ III) bietet deutlich besseren Verschleißschutz als Standard-Eloxierung (Typ II). Alternativ: Cerakote-Beschichtung als moderner Korrosionsschutz.

**F23: Was mache ich mit Blöcken an einem Boot, das ich gerade gekauft habe?**
A: Generelle Empfehlung bei Boots-Übernahme: ALLE Blöcke systematisch inspizieren. Alter und Wartungshistorie sind unbekannt. Jeden Block zerlegen, reinigen, inspizieren, schmieren. Verdächtige Lager sofort tauschen. Protokoll anlegen. Kosten: Material ca. 50–100 €, Arbeitszeit 1–2 Tage. Kann tausende Euro Folgeschäden verhindern.

**F24: Gibt es Blöcke, die „wartungsfrei" sind?**
A: Nein. Kein mechanisches Bauteil im Marineeinsatz ist wartungsfrei. Manche Hersteller werben mit „wartungsarm" (z.B. Composite-Lager, versiegelte Kugellager). Diese Blöcke benötigen weniger häufige Wartung, aber regelmäßige Inspektion und gelegentliche Schmierung sind immer nötig. „Wartungsfrei" in der Werbung bedeutet in der Praxis „weniger Wartung nötig".

**F25: Wie entsorge ich alte Blöcke umweltgerecht?**
A: Blöcke bestehen aus verschiedenen Materialien, die getrennt werden sollten: Aluminium und Edelstahl zum Metallrecycling, Polymere zum Kunststoffrecycling (wenn sortenrein trennbar). Alte Schmiermittel als Altöl entsorgen. Keinesfalls in den Hausmüll oder — schlimmer — ins Wasser. Viele Werft- und Yachthäfen haben Sammelbehälter für Altmetall und Kunststoff.

### 10.6 Fortgeschrittene Fragen

**F26: Kann ich Lager aus dem Industriebedarf (SKF, FAG, INA) in Blöcken verwenden?**
A: Grundsätzlich ja, wenn die Abmessungen exakt passen. Industrie-Kugellager nach DIN/ISO sind maßgenau und oft günstiger als Hersteller-Originale. Wichtig: (1) Material muss Edelstahl AISI 316 oder Keramik-Hybrid sein — Standard-Chromstahl (100Cr6) korrodiert sofort in Salzwasser. (2) Genauigkeitsklasse mindestens P6 (besser P5). (3) Abdichtung: Offene Lager bevorzugen (einfacher zu schmieren), keine Gummidichtungen (behindern Salzwasserdrainage). (4) Achtung: Harken und Ronstan verwenden teilweise nicht-standardisierte Lagerdimensionen — immer nachmessen!

**F27: Welchen Einfluss hat die Scheibengröße auf die Tauwerk-Lebensdauer?**
A: Erheblichen! Die Biegeradius-Regel besagt: Je größer der Scheibendurchmesser relativ zum Tauwerk-Durchmesser, desto geringer die Biegebeanspruchung des Tauwerks. Für Polyester-Tauwerk gilt als Minimum D/d = 4:1 (Scheiben-Ø zu Tauwerk-Ø), empfohlen 6:1. Für Dyneema: Minimum D/d = 5:1, empfohlen 8:1. Bei Unterschreitung dieser Verhältnisse verkürzt sich die Tauwerk-Lebensdauer dramatisch — bis zu 50 % bei D/d = 3:1 gegenüber D/d = 8:1.

**F28: Was ist der Unterschied zwischen WLL, SWL und BL bei Blöcken?**
A: Diese Angaben beschreiben die Belastbarkeit: (1) **BL (Breaking Load/Bruchlast):** Die Last, bei der der Block zerstört wird. Laborwert. (2) **SWL (Safe Working Load):** Die maximal zulässige Gebrauchslast. Typisch SWL = BL / 4 (Sicherheitsfaktor 4:1). (3) **WLL (Working Load Limit):** Moderne Bezeichnung, gleichbedeutend mit SWL. Wichtig für die Wartung: Ein Block, der regelmäßig nahe seiner WLL betrieben wird, verschleißt schneller als einer mit Reserven. Faustregel: Dauerlast sollte unter 50 % WLL liegen.

**F29: Meine Blöcke haben nach dem Winter Schimmel. Ist das problematisch?**
A: Schimmel an sich beschädigt die Block-Materialien (Metall, Polymer) nicht. Er deutet aber auf hohe Feuchtigkeit im Lagerraum hin, die Korrosion fördert. Reinigung: Schimmel mit Isopropanol oder verdünntem Essig abwischen. Danach gründlich trocknen und schmieren. Lager auf Korrosionsanzeichen prüfen. Für die Zukunft: Blöcke in belüftetem Raum lagern, ggf. Luftentfeuchter oder Silikatgel-Beutel verwenden.

**F30: Wie erkenne ich, ob mein Block aus Edelstahl 304 oder 316L besteht?**
A: Einfachster Test: Der Magnettest. Edelstahl 304 ist nach Kaltverformung leicht magnetisch (Bolzen, Achsen nach Pressung). Edelstahl 316L bleibt auch nach Verformung praktisch nicht-magnetisch. Ein starker Neodym-Magnet hilft bei der Unterscheidung. Für genauere Bestimmung: Molybdän-Schnelltest (Tropfentest) aus dem Werkstoffhandel. Oder: Herstellerangaben konsultieren — seriöse Hersteller (Harken, Lewmar, Ronstan) verwenden durchgehend 316L. Vorsicht bei No-Name-Blöcken und günstigen Importen.

**F31: Kann ich defekte Harken-Ratschenfedern durch Standard-Federn ersetzen?**
A: Theoretisch ja, wenn die Maße stimmen. Harken verwendet jedoch spezielle Federstähle und Geometrien, die für die exakte Klinkenkraft optimiert sind. Eine zu starke Feder erhöht die Reibung in Laufrichtung unnötig, eine zu schwache lässt die Ratsche durchrutschen. Empfehlung: Originalfedern von Harken (im Service Kit enthalten) verwenden. Die Kosten sind gering (10–20 € pro Kit), und die Funktionssicherheit ist garantiert.

**F32: Mein Lewmar-Block hat einen Achsbolzen, der sich nicht lösen lässt. Was tun?**
A: Festsitzende Achsbolzen sind meist durch Korrosion oder galvanische Produkte verklebt. Vorgehen: (1) Kriechöl (z.B. Caramba, WD-40 — hier ausnahmsweise erlaubt als Lösemittel!) großzügig auf beide Seiten auftragen. (2) 24 Stunden einwirken lassen. (3) Erneut Kriechöl, weitere 12 Stunden. (4) Mit passendem Durchschlag und Hammer vorsichtig treiben. (5) Wenn immer noch fest: Wärme (Heißluftfön, 80–100°C auf die Wangen, NICHT auf die Scheibe/Polymer!). Durch Wärmeausdehnung der Wange löst sich oft die Achse. (6) Letztes Mittel: Achse ausbohren (Opfer-Achse → neue Achse bestellen). NIEMALS den Block in einen Schraubstock spannen und mit Gewalt arbeiten — Wangenbruch!

**F33: Wie lagere ich Blöcke langfristig (Bootsverkauf, längere Pause)?**
A: Langzeitlagerung (>6 Monate): (1) Alle Blöcke demontieren und gründlich reinigen. (2) Alle Metalloberflächen mit Boeshield T-9 oder Ballistol konservieren. (3) Polymerteil trocken lagern (kein Öl/Fett nötig). (4) In VCI-Beuteln (Volatile Corrosion Inhibitor) einzeln verpacken. (5) In trockenem, temperiertem Raum lagern (10–25°C, <60 % Luftfeuchtigkeit). (6) Silikatgel-Beutel beilegen. (7) Jährlich kurz öffnen, Zustand prüfen, ggf. nachkonservieren. So gelagert halten Blöcke problemlos 5–10 Jahre.

**F34: Gibt es eine Möglichkeit, den Verschleiß meiner Blöcke zu messen, ohne sie zu zerlegen?**
A: Begrenzt. Ohne Zerlegung können Sie feststellen: (1) Leichtgängigkeit (Scheibe von Hand drehen). (2) Geräusche (Knirschen, Quietschen). (3) Seitliches Spiel (Scheibe seitlich bewegen). (4) Sichtbare Rillenbildung (von außen in die Scheibe schauen). (5) Korrosion an sichtbaren Oberflächen. Für präzise Messungen (Rillentiefe, Achsdurchmesser, Lagerspiel) ist eine Zerlegung jedoch unvermeidlich. Das AYDI-System kann aus Fotos eine grobe Einschätzung geben (visual_medium Confidence), ersetzt aber nicht die manuelle Inspektion.

**F35: Welche Auswirkung hat die Beladung (Proviant, Ausrüstung) auf die Blockbelastung?**
A: Indirekt erheblich. Höhere Beladung bedeutet: (1) Größere Segelfläche nötig für gleiche Geschwindigkeit → höhere Schot-/Falllasten. (2) Höhere Stabilität bei Motor-Yachten, aber schlechtere bei Segelyachten → mehr Trimm nötig. (3) Höherer Tiefgang → mehr Wellenbedeckung der Decksbeschläge → mehr Salzwasserexposition. Für die Blockwartung bedeutet das: Bei voll beladenen Blauwasseryachten sind die Blöcke stärker beansprucht als bei einer leichten Wochenendrundseglerei. Die Wartungsintervalle sollten entsprechend angepasst werden.

---

## 11. Glossar

### Fachbegriffe A–Z

**Abrasion (Abrasion)**
Materialabtrag durch mechanische Reibung, insbesondere durch harte Partikel (Sand, Salzkristalle) zwischen beweglichen Flächen.

**Achse (Axle/Pin)**
Zentrales Bauteil, um das die Scheibe rotiert. Material: Edelstahl 316L, Titan oder Keramik-Composite.

**Acetal (POM/Delrin)**
Hochleistungskunststoff für Scheiben und Lagerbuchsen. Selbstschmierend, gute Festigkeit, moderate UV-Beständigkeit.

**Backing Plate**
Verstärkungsplatte unter Deck zur Lastverteilung bei Blockbefestigungen. Material: Edelstahl, Aluminium oder GFK.

**Ball Bearing (Kugellager)**
Lagertyp mit Stahlkugeln zwischen Laufringen. Bietet geringste Reibung bei geringer bis mittlerer Last.

**Brinelling**
Dauerhafte Eindrücke der Kugeln in die Lagerlaufbahn durch statische Überlast oder Schockbelastung.

**Carbo (Composite)**
Harken-Bezeichnung für Composite-Material (glasfaserverstärktes Polymer) für Blockscheiben.

**CE-Kennzeichnung**
Europäische Konformitätskennzeichnung nach Richtlinie 2013/53/EU für Sportboote.

**Cheek Block (Wangenblock)**
Flach bauender Block, der direkt auf dem Deck montiert wird. Nur eine Wange, Scheibe läuft offen.

**Composite Bearing (Gleitlager)**
Lagerbuchse aus Hochleistungspolymer (Torlon, PEEK, Acetal). Wartungsärmer als Kugellager, aber höhere Reibung.

**Crevice Corrosion (Spaltkorrosion)**
Korrosion in engen Spalten (Lager, Achse-Scheibe), wo Sauerstoffmangel die Passivschicht des Edelstahls zerstört.

**Duralac**
Anti-Korrosions-Paste auf Zinkchromat-Basis zur Isolierung verschiedener Metalle bei Kontakt.

**Dyneema (UHMWPE)**
Hochfestes Fasermaterial für moderne Seile. Verursacht stärkere Rillenbildung auf Aluminiumscheiben als Polyester.

**ESP (Element Snatch Pro)**
Harken-Bezeichnung für eine Snatchblock-Serie mit selbstschmierendem Composite-Lager.

**Ermüdungsriss (Fatigue Crack)**
Riss, der durch zyklische Belastung entsteht und sich progressiv ausbreitet. Nicht reparabel.

**Fiddle Block (Violinblock)**
Block mit zwei übereinander angeordneten Scheiben unterschiedlicher Größe.

**Flaschenzug (Tackle)**
System aus mehreren Blöcken und einem Seil zur Kraftübersetzung.

**Foot Block (Fußblock)**
Decksmontierter Block zur Umlenkung von Schoten und Fallen auf Decksniveau.

**Galvanische Korrosion**
Elektrochemische Korrosion an der Kontaktstelle zweier verschiedener Metalle in einem Elektrolyten (Seewasser).

**Grooving (Rillenbildung)**
Einlaufen einer Rille in die Scheibe durch das darüber laufende Tauwerk.

**Harken One Lube**
Universalschmiermittel von Harken für alle Blocktypen. PTFE-basiert.

**Helicoil**
Gewindeeinsatz aus Edelstahldraht zum Reparieren von ausgerissenen Gewindebohrungen.

**HTX (Hard Top X)**
Lewmar-Bezeichnung für Blöcke mit verstärktem Kopf.

**Käfig (Cage/Retainer)**
Bauteil, das Kugeln oder Nadeln in gleichmäßigem Abstand hält und Kollision verhindert.

**Kugellaufbahn (Ball Race)**
Gehärtete Lauffläche in Lagerschalen, auf der die Kugeln rollen.

**Lager (Bearing)**
Bauteil, das die Rotation der Scheibe um die Achse ermöglicht und Reibung minimiert.

**Lastbolzen (Load Pin)**
Bolzen, der den Block am Beschlag befestigt und die gesamte Blocklast überträgt.

**McLube Sailkote**
Trockenschmiermittel auf Fluorpolymer-Basis. Ideal für Tauwerk-Kontaktflächen.

**McLube OneDrop**
Flüssiges Lagerschmiermittel auf Fluorpolymer-Basis.

**Nadellager (Needle Bearing)**
Lagertyp mit zylindrischen Nadeln statt Kugeln. Höhere Tragfähigkeit bei kompakterer Bauform.

**Orbit Block**
Ronstan-Bezeichnung für eine Blockserie mit besonderem Befestigungssystem.

**Passivierung**
Chemische Behandlung von Edelstahl zur Wiederherstellung der schützenden Oxidschicht (Chromoxid).

**PEEK (Polyetheretherketon)**
Hochleistungspolymer mit ausgezeichneter chemischer und UV-Beständigkeit. Für Lager und Scheiben.

**Pitting**
Lochfraßkorrosion — punktuelle Korrosionsnarben auf Metalloberflächen.

**Ratschenblock (Ratchet Block)**
Block mit Freilauf-Mechanismus: dreht frei in Zugrichtung, blockiert in Gegenrichtung.

**Scheibe (Sheave)**
Rotierende Rolle im Block, über die das Tauwerk läuft. Kern-Verschleißteil.

**Schmalblock**
Besonders flach bauender Block für enge Einbausituationen.

**Sicherungsring (Snap Ring/Circlip)**
Federring zur axialen Sicherung der Achse in der Wange.

**Snatchblock**
Block mit öffnungsfähiger Wange zum seitlichen Einlegen des Tauwerks ohne Auffädeln.

**Sperrklinke (Pawl)**
Federbelastetes Bauteil im Ratschenblock, das in die Sägezähne eingreift.

**Spaltkorrosion**
Siehe Crevice Corrosion.

**Tef-Gel**
PTFE-basiertes Anti-Seize-Mittel für Edelstahl-Befestigungen. Verhindert Festfressen und galvanische Korrosion.

**Ti-Lite**
Harken-Bezeichnung für Blöcke mit Titanachse.

**Torlon (PAI)**
Polyamid-Imid — Hochleistungspolymer mit höchster Festigkeit und Temperaturbeständigkeit. Für Lagerbuchsen in Hochlast-Blöcken.

**Turning Block (Umlenkblock)**
Decksmontierter Block zur horizontalen Richtungsänderung von Schoten und Fallen.

**UV-Degradation**
Materialveränderung durch ultraviolette Strahlung. Führt zu Versprödung, Verfärbung, Festigkeitsverlust bei Polymeren.

**Wange (Cheek/Side Plate)**
Seitenplatten des Blocks, die die Scheibe umschließen und die Achse tragen.

**Wöhler-Kurve**
Diagramm, das die Lebensdauer (Lastwechsel bis Bruch) in Abhängigkeit von der Belastungsamplitude zeigt.

---

## 12. Schnell-Referenz

### 12.1 Wartungs-Schnellkarte

```
╔═══════════════════════════════════════════════════════════════╗
║              BLOCK-WARTUNG SCHNELLREFERENZ                    ║
╠═══════════════════════════════════════════════════════════════╣
║                                                               ║
║  NACH JEDEM SEGELTAG (Salzwasser):                           ║
║  → Süßwasser über alle Blöcke spülen                         ║
║                                                               ║
║  MONATLICH:                                                   ║
║  → Sichtprüfung aller Blöcke                                 ║
║  → Funktionsprüfung (dreht frei?)                            ║
║                                                               ║
║  ALLE 3 MONATE:                                              ║
║  → Schmierung aller Lager (2-3 Tropfen Harken One Lube)      ║
║  → McLube Sailkote auf Scheiben                              ║
║  → Ratschenblöcke: Mechanismus prüfen                        ║
║                                                               ║
║  JÄHRLICH (Winterlager):                                     ║
║  → Alle Blöcke zerlegen                                      ║
║  → Reinigen, inspizieren, messen                             ║
║  → Lager prüfen, ggf. tauschen                               ║
║  → Scheiben auf Rillenbildung prüfen                         ║
║  → Achsen auf Korrosion/Verschleiß prüfen                    ║
║  → Alles schmieren, zusammenbauen, protokollieren            ║
║                                                               ║
║  ALLE 3-5 JAHRE:                                             ║
║  → Lagersätze tauschen (Salzwasser)                          ║
║  → Scheiben prüfen und ggf. tauschen                         ║
║                                                               ║
╠═══════════════════════════════════════════════════════════════╣
║  GRENZWERTE:                                                  ║
║  Rillentiefe:   Fahrt >1,0mm = tauschen                      ║
║                 Regatta >0,5mm = tauschen                     ║
║  Achse:         Durchmesser <98% Nenn = tauschen             ║
║  Lagerspiel:    Kugel/Nadel >0,08mm = tauschen               ║
║                 Gleit >0,15mm = tauschen                      ║
╠═══════════════════════════════════════════════════════════════╣
║  SCHMIERMITTEL:                                               ║
║  ✓ Harken One Lube (Lager)                                   ║
║  ✓ McLube Sailkote (Scheiben, Tauwerk-Kontakt)               ║
║  ✓ McLube OneDrop (Lager, Alternative)                       ║
║  ✓ Boeshield T-9 (Korrosionsschutz, Winterlager)            ║
║  ✗ WD-40 (NEIN! Löst Schmierung auf!)                       ║
║  ✗ Motoröl (NEIN! Nicht salzwasserbeständig!)                ║
╠═══════════════════════════════════════════════════════════════╣
║  SOFORT TAUSCHEN BEI:                                        ║
║  ✗ Gebrochene Wange/Achse/Scheibe                            ║
║  ✗ Ermüdungsriss (sichtbar)                                  ║
║  ✗ Blockierende Scheibe unter Last                           ║
║  ✗ >20% Querschnittsverlust durch Korrosion                  ║
╚═══════════════════════════════════════════════════════════════╝
```

### 12.2 Notfall-Referenz

```
╔═══════════════════════════════════════════════════════════════╗
║              BLOCK-NOTFALL AUF SEE                           ║
╠═══════════════════════════════════════════════════════════════╣
║                                                               ║
║  1. RUHE BEWAHREN                                            ║
║  2. Last wegnehmen (Segel bergen/fieren)                     ║
║  3. NIEMALS blockierenden Block unter Last ausbauen!         ║
║  4. Reserveblock einsetzen                                   ║
║  5. Oder: weniger kritischen Block umhängen                  ║
║  6. Oder: Tauwerk direkt über Beschlag führen (Notlösung)   ║
║  7. Schaden dokumentieren                                    ║
║  8. Bei nächster Gelegenheit fachgerecht reparieren          ║
║                                                               ║
╚═══════════════════════════════════════════════════════════════╝
```

---

## ANHANG A — Fallstudien

### Fallstudie 1: Großschotblock-Versagen auf Regattayacht

**Yacht:** X-41, Baujahr 2019, aktiver Regattaeinsatz
**Block:** Harken 57mm Ratchamatic, Großschot-Umlenkblock
**Revier:** Ostsee, Salzwasser
**Betriebsdauer:** 4 Jahre, ca. 200 Segeltage

**Befund:**
Während einer Regatta bei 22 kn Wind blockierte der Großschot-Umlenkblock plötzlich. Die Scheibe drehte nicht mehr, das Tauwerk konnte nicht mehr gefiert werden. Die Crew musste das Großsegel unter erheblichem Risiko bergen.

**Analyse:**
Zerlegung ergab:
- 3 von 14 Kugeln mit fortgeschrittenem Pitting
- Kugellaufbahn innen mit tiefen Riefen
- Salzkristallablagerungen in der gesamten Lagereinheit
- Letzte dokumentierte Schmierung: 14 Monate vor dem Vorfall
- Achse mit leichter Oberflächenkorrosion

**Ursache:**
Mangelhafte Wartung — Schmierintervall von 3 Monaten auf >12 Monate überschritten. Salzkristalle haben die Lagerlaufflächen progressiv beschädigt. Die beschädigten Kugeln erzeugten Abriebpartikel, die den Verschleiß beschleunigten (Autokatalyse).

**Maßnahmen:**
1. Lagersatz komplett getauscht (Harken Kit HAR 504)
2. Achse getauscht (leichte Korrosion → neues Risiko)
3. Scheibe beibehalten (Rillentiefe 0,3 mm — akzeptabel)
4. Wartungsplan erstellt: Schmierung alle 8 Wochen, Inspektion vierteljährlich
5. Zweiter Großschotblock als Reserve an Bord

**Kosten:**
- Lagersatz: 85 €
- Neue Achse: 35 €
- Arbeitszeit: 2 Stunden
- Gesamtkosten der Reparatur: ca. 150 €
- Potenzielle Kosten bei Totalversagen (Rigg-/Segelschaden): 5.000–15.000 €

**Lehre:**
Wartungsintervalle einhalten! Die 150 € Reparaturkosten stehen in keinem Verhältnis zu den potenziellen Folgekosten. Ein einfacher Schmierplan hätte das Versagen verhindert.

### Fallstudie 2: UV-Degradation an Polymerblöcken in den Tropen

**Yacht:** Bavaria 46, Baujahr 2015, Langfahrt Karibik
**Blöcke:** Lewmar Synchro 40mm, diverse Positionen
**Revier:** Karibik (Martinique, Guadeloupe, BVI), 3 Jahre Dauerliegeplatz
**Betriebsdauer:** 8 Jahre, davon 3 in tropischer Sonne

**Befund:**
Bei Routineinspektion: Alle Polymer-Teile der Blöcke (Wangen, Scheiben) stark vergilbt und spröde. Ein Wangenblock am Vorschiff zerbrach bei der Handhabung — das Material war durchgehend versprödet.

**Analyse:**
- UV-Index in der Karibik: durchschnittlich 11 (extrem)
- Blöcke hatten keine UV-Abdeckung (kein Bimini über Vorschiff)
- Lewmar Synchro-Serie: Glasfaserverstärktes Polyamid — UV-stabilisiert, aber nicht für dauerhafte tropische Exposition ausgelegt
- Degradationstiefe: durchgehend (nicht nur Oberfläche)
- Aluminium-Teile und Edelstahl unbeeinträchtigt

**Maßnahmen:**
1. Alle Polymer-Blöcke auf dem Vorschiff und ungeschützten Bereichen getauscht (12 Blöcke)
2. UV-Schutzabdeckungen (Canvas Covers) für alle exponierten Blöcke angefertigt
3. Auf Blöcke mit höherem UV-Schutz gewechselt (Harken Carbo-Serie)

**Kosten:**
- 12 neue Blöcke: ca. 1.800 €
- UV-Abdeckungen: ca. 200 € (Segelmacher)
- Gesamtkosten: ca. 2.000 €

**Lehre:**
In tropischen Revieren sind UV-Schutzmaßnahmen Pflicht, nicht optional. Polymer-Blöcke ohne Abdeckung können innerhalb von 2–3 Jahren ihre Festigkeit verlieren. Alternative: Aluminium-Blöcke oder speziell UV-stabilisierte Serien verwenden.

---

## ANHANG B — Fallstudien (Fortsetzung)

### Fallstudie 3: Galvanische Korrosion an Aluminium-Mastblöcken

**Yacht:** Hallberg-Rassy 40, Baujahr 2012
**Blöcke:** Seldén Aluminium-Fallblöcke am Mastkopf
**Revier:** Nordsee, Salzwasser
**Betriebsdauer:** 10 Jahre

**Befund:**
Bei Mastlegen: Massive weiße Korrosionsablagerungen an den Aluminium-Wangen der Mastblöcke. Mehrere Befestigungsbolzen (Edelstahl) waren „eingewachsen" in das Aluminium. Ein Block war nicht mehr demontierbar.

**Analyse:**
- Kontaktpaar: Edelstahl 316-Bolzen in Aluminium-Wange
- Potentialdifferenz: ca. 0,5 V — problematisch in Salzwasser
- Keine Isolierung zwischen den Metallen (kein Duralac, keine Kunststoffbuchse)
- Feuchtigkeit dauerhaft vorhanden (Kondensation im Masttop)
- Aluminium als unedles Metall war das „Opfer" der galvanischen Zelle

**Maßnahmen:**
1. Betroffene Blöcke mit Wärme (Heißluftfön) und Kriechöl gelöst
2. Korrodierte Blöcke getauscht (Aluminium strukturell geschwächt)
3. Neue Blöcke mit Duralac auf allen Kontaktflächen montiert
4. Kunststoff-Isolierbuchsen zwischen Edelstahl und Aluminium eingefügt
5. Regelmäßige Kontrolle bei jedem Mastlegen

**Kosten:**
- 4 neue Mastblöcke: ca. 600 €
- Duralac, Buchsen, Befestigung: ca. 80 €
- Arbeitszeit: 4 Stunden
- Gesamtkosten: ca. 800 €

**Lehre:**
Galvanische Korrosion ist bei Mastblöcken besonders tückisch, weil sie in geschützter Position unsichtbar arbeitet. Bei jeder Installation verschiedener Metalle: Isolation (Duralac, Tef-Gel, Kunststoffbuchsen) ist Pflicht.

### Fallstudie 4: Snatchblock-Versagen bei Nachtfahrt

**Yacht:** Jeanneau Sun Odyssey 440, Baujahr 2020
**Block:** Harken 40mm Snatchblock, Genua-Schot-Umlenkung
**Revier:** Mittelmeer, Nachtfahrt von Sardinien nach Korsika
**Betriebsdauer:** 3 Jahre

**Befund:**
Während einer Nachtfahrt bei 18 kn Wind öffnete sich der Snatchblock der Genua-Schot. Die Schot sprang aus dem Block und schlug unkontrolliert. Die Genua begann zu schlagen, und die Crew brauchte 15 Minuten, um die Situation zu kontrollieren.

**Analyse:**
- Verriegelungsmechanismus des Snatchblocks war korrodiert
- Federbelastete Verriegelungsnase hatte 50 % ihrer Federkraft verloren
- Salzablagerungen im Gelenk hatten die Beweglichkeit eingeschränkt
- Bei Böen erzeugte die dynamische Belastung Vibrationen, die die geschwächte Verriegelung öffneten

**Maßnahmen:**
1. Snatchblock durch neues Exemplar ersetzt
2. Alle anderen Snatchblöcke inspiziert (2 weitere mit Schwächen)
3. Wartungsplan: Snatchblock-Verriegelungen monatlich prüfen und schmieren
4. Zusätzliche Sicherung (Mausefalle/Seizing) an kritischen Snatchblöcken

**Kosten:**
- Neuer Snatchblock: ca. 95 €
- Arbeitszeit: 1 Stunde
- Gesamtkosten: ca. 120 €

**Lehre:**
Snatchblöcke erfordern besondere Aufmerksamkeit bei der Wartung. Der Öffnungsmechanismus ist ein zusätzliches Verschleißteil, das regelmäßig geprüft und geschmiert werden muss. An kritischen Positionen ggf. Sicherung gegen unbeabsichtigtes Öffnen vorsehen.

---

## ANHANG C — Fallstudien (Fortsetzung II)

### Fallstudie 5: Ratschenblock-Fehlfunktion durch falsche Schmierung

**Yacht:** J/109, Baujahr 2017, Regatta- und Fahrteneinsatz
**Block:** Harken 57mm Ratchamatic, Großschot
**Betriebsdauer:** 6 Jahre

**Befund:**
Eigner beschwerte sich, dass der Ratschenblock „nicht mehr greift" — die Schot rutschte unter Last durch, statt gehalten zu werden.

**Analyse:**
- Der Eigner hatte bei der Winterwartung den gesamten Block großzügig mit Lithiumfett geschmiert
- Das Fett war in den Ratschenmechanismus eingedrungen
- Die Sperrklinken rutschten auf dem Fettfilm über die Sägezähne, statt einzugreifen
- Die Federn waren intakt, die Klinken scharf — das Problem war rein durch Schmierung verursacht

**Maßnahmen:**
1. Ratschenmechanismus komplett zerlegt
2. Alles Fett entfernt (Isopropanol)
3. Ratschenmechanismus nur mit McLube Sailkote minimal geschmiert
4. Lager separat mit Harken One Lube geschmiert
5. Eigner über korrekte Schmierung instruiert

**Kosten:**
- Material (Reiniger, Schmiermittel): ca. 25 €
- Arbeitszeit: 1,5 Stunden
- Gesamtkosten: ca. 50 €

**Lehre:**
Ratschenmechanismen dürfen NICHT mit Fett oder Öl geschmiert werden! Die Sperrklinken müssen „griffig" bleiben. Maximal ein kurzer Sprühstoß Trockenschmiermittel (McLube Sailkote). Das Lager darf und soll geschmiert werden — aber nicht der Ratschenmechanismus.

### Fallstudie 6: Kaskadierende Folgeschäden durch einen einzelnen defekten Block

**Yacht:** Beneteau Oceanis 51.1, Baujahr 2018, Charter-Yacht
**Block:** Lewmar 40mm Umlenkblock, Großfall
**Revier:** Kroatien, Salzwasser
**Betriebsdauer:** 5 Jahre, Charter-Intensivnutzung

**Befund:**
Der Umlenkblock am Mastfuß für das Großfall hatte eine tiefe Rille (1,8 mm) entwickelt. Die scharfe Kante der Rille hatte über Wochen den Mantel des Dyneema-Falls durchgescheuert. Beim Reffen riss das Fall am Block, das Großsegel fiel unkontrolliert herunter, und die Last auf dem Lastenläufer beschädigte den Traveller.

**Analyse:**
- Rillenbildung: 1,8 mm — weit über der Austauschgrenze von 1,0 mm
- Charter-Betrieb: Keine regelmäßige Scheibeninspektion
- Dyneema-Fall: Besonders aggressiv auf Aluminium-Scheiben
- Folgeschäden: Fall (320 €), Traveller-Reparatur (450 €), Segelmacher (180 €)

**Maßnahmen:**
1. Block mit neuer Composite-Scheibe ausgestattet
2. Neues Großfall konfektioniert
3. Traveller repariert
4. Charter-Wartungsplan: Scheiben vierteljährlich auf Rillenbildung prüfen

**Kosten:**
- Neue Scheibe: ca. 45 €
- Neues Großfall: ca. 320 €
- Traveller-Reparatur: ca. 450 €
- Segelmacher: ca. 180 €
- Gesamtkosten: ca. 995 €
- Davon vermeidbar durch rechtzeitigen Scheibentausch: 950 €

**Lehre:**
Ein einzelner defekter Block (Scheibentausch: 45 €) kann Folgeschäden von fast 1.000 € verursachen. Regelmäßige Scheibeninspektion ist besonders bei Dyneema-Tauwerk kritisch.

---

## ANHANG D — Fallstudien (Fortsetzung III)

### Fallstudie 7: Erfolgreiche präventive Wartung auf Blauwasseryacht

**Yacht:** Amel Super Maramu, Baujahr 2005, Weltumsegelung
**Blöcke:** Diverse Harken und Lewmar, ca. 35 Blöcke gesamt
**Revier:** Weltweit (Atlantik, Karibik, Pazifik, Indischer Ozean)
**Betriebsdauer:** 18 Jahre, davon 6 Jahre Weltumsegelung

**Befund:**
Bei Ankunft nach 6-jähriger Weltumsegelung waren alle 35 Blöcke in funktionsfähigem Zustand. Kein einziger Blockausfall während der gesamten Reise.

**Wartungspraxis des Eigners:**
- Wöchentlich: Funktionsprüfung aller zugänglichen Blöcke
- Alle 6 Wochen: Schmierung aller Lager (Harken One Lube)
- Vierteljährlich: Scheiben-Sichtkontrolle, Ratschenblock-Check
- Halbjährlich: Volldemontage und Inspektion von 5–6 Blöcken (rotierend)
- Vor Ozeanüberquerungen: Vollinspektion aller sicherheitskritischen Blöcke
- Ersatzteile an Bord: 4 Universalblöcke, 3 Lagersätze, 2 Achsen, Schmiermittel für 2 Jahre

**Durchgeführte Wartungen während der Reise:**
- 8 Lagersätze getauscht (präventiv, bei ersten Verschleißzeichen)
- 3 Scheiben getauscht (Rillenbildung an Dyneema-Blöcken)
- 1 Snatchblock-Feder getauscht
- 2 Achsen getauscht (leichte Korrosion)
- Geschätzte Gesamtkosten Wartung in 6 Jahren: ca. 800 €

**Lehre:**
Konsequente präventive Wartung ermöglicht jahrzehntelange zuverlässige Blockfunktion — selbst unter härtesten Bedingungen. Die Kosten von 800 € in 6 Jahren (ca. 130 €/Jahr) sind minimal im Vergleich zu möglichen Ausfällen auf See.

### Fallstudie 8: Blockwartung bei Superyacht — professioneller Ansatz

**Yacht:** 25m Custom-Segelyacht, Baujahr 2016
**Blöcke:** Harken und Antal, ca. 80 Blöcke (inkl. Hydraulik-System-Umlenkungen)
**Revier:** Mittelmeer (Sommer), Karibik (Winter)
**Crew:** 3 Festangestellte inkl. Bootswain

**Wartungssystem:**
Der Bootswain führt ein digitales Wartungslogbuch (Dockwa/Helm Connect) mit individueller Identifikation jedes Blocks:

- Jeder Block hat eine ID-Nummer (Gravur)
- Einbaudatum, Hersteller, Modell, Seriennummer erfasst
- Wartungsintervalle automatisch generiert
- Digitale Fotos bei jeder Inspektion
- Messwerte (Rillentiefe, Achsdurchmesser) protokolliert
- Trend-Analyse: Verschleißkurve pro Block

**Ergebnisse nach 7 Jahren:**
- Kein einziger ungeplanter Blockausfall
- 22 präventive Lagertausche
- 8 Scheibentausche
- 3 Komplett-Blockersetzungen (Lebensdauerende)
- Durchschnittliche Wartungskosten: ca. 3.500 €/Jahr (für 80 Blöcke)
- Uptime: 100 %

**Lehre:**
Professionelle, systematische Wartung mit digitaler Dokumentation ist der Goldstandard. Für Fahrtensegler nicht in vollem Umfang nötig, aber die Prinzipien (Protokollierung, Intervalle, Trend-Beobachtung) sind übertragbar.

---

## ANHANG E — AYDI-Integration (Pydantic-Modelle)

### E.1 Datenmodelle für Blockwartung

```python
"""
AYDI Block Maintenance Models
Pydantic v2 models for block maintenance tracking and analysis.
"""

from datetime import date, datetime
from enum import Enum
from typing import Optional

from pydantic import BaseModel, Field


class BlockType(str, Enum):
    """Types of sailing blocks."""
    BALL_BEARING = "ball_bearing"
    NEEDLE_BEARING = "needle_bearing"
    PLAIN_BEARING = "plain_bearing"
    RATCHET = "ratchet"
    FIDDLE = "fiddle"
    SNATCH = "snatch"
    DOUBLE = "double"
    TRIPLE = "triple"
    TURNING = "turning"
    FOOT = "foot"
    CHEEK = "cheek"
    MAST = "mast"
    LEAD = "lead"
    FLYING = "flying"


class BlockManufacturer(str, Enum):
    """Block manufacturers."""
    HARKEN = "harken"
    LEWMAR = "lewmar"
    RONSTAN = "ronstan"
    ANTAL = "antal"
    SELDEN = "selden"
    SPINLOCK = "spinlock"
    WICHARD = "wichard"
    SCHAEFER = "schaefer"
    HOLT = "holt"
    ALLEN = "allen"
    OTHER = "other"


class BlockPosition(str, Enum):
    """Block positions on yacht."""
    MAINSHEET = "mainsheet"
    HALYARD = "halyard"
    GENOA_SHEET = "genoa_sheet"
    SPINNAKER = "spinnaker"
    REEF = "reef"
    TRAVELLER = "traveller"
    VANG = "vang"
    OUTHAUL = "outhaul"
    CUNNINGHAM = "cunningham"
    BACKSTAY = "backstay"
    BARBER_HAULER = "barber_hauler"
    TURNING_BLOCK = "turning_block"
    MAST_HEAD = "mast_head"
    MAST_BASE = "mast_base"
    UNDERDECK = "underdeck"
    OTHER = "other"


class MaintenanceType(str, Enum):
    """Types of maintenance actions."""
    FRESHWATER_RINSE = "freshwater_rinse"
    LUBRICATION = "lubrication"
    VISUAL_INSPECTION = "visual_inspection"
    FUNCTIONAL_CHECK = "functional_check"
    FULL_INSPECTION = "full_inspection"
    BEARING_REPLACEMENT = "bearing_replacement"
    SHEAVE_REPLACEMENT = "sheave_replacement"
    AXLE_REPLACEMENT = "axle_replacement"
    RATCHET_SERVICE = "ratchet_service"
    SNATCH_MECHANISM_SERVICE = "snatch_mechanism_service"
    FULL_OVERHAUL = "full_overhaul"
    BLOCK_REPLACEMENT = "block_replacement"


class ConditionRating(str, Enum):
    """Condition ratings for block components."""
    EXCELLENT = "excellent"  # Like new
    GOOD = "good"  # Normal wear, fully functional
    FAIR = "fair"  # Noticeable wear, monitor
    POOR = "poor"  # Significant wear, plan replacement
    CRITICAL = "critical"  # Replace immediately


class WearPattern(str, Enum):
    """Identifiable wear patterns on sheaves."""
    NONE = "none"
    V_GROOVE = "v_groove"
    U_GROOVE = "u_groove"
    ASYMMETRIC_GROOVE = "asymmetric_groove"
    MULTIPLE_GROOVES = "multiple_grooves"
    EDGE_BREAKOUT = "edge_breakout"
    SURFACE_CRACKING = "surface_cracking"
    CORROSION_PITTING = "corrosion_pitting"


class ConfidenceLevel(str, Enum):
    """AYDI confidence levels."""
    MEASURED = "measured"
    CALCULATED = "calculated"
    VISUAL_HIGH = "visual_high"
    VISUAL_MEDIUM = "visual_medium"
    VISUAL_LOW = "visual_low"
    VISUAL_INSUFFICIENT = "visual_insufficient"
    ESTIMATED = "estimated"
    BENCHMARK = "benchmark"
    DOCUMENTED = "documented"


class BlockIdentification(BaseModel):
    """Identification data for a single block."""
    model_config = {"from_attributes": True}

    block_id: str = Field(..., description="Unique identifier for the block (e.g., BLK-001)")
    manufacturer: BlockManufacturer
    model_name: str = Field(..., description="Manufacturer model name (e.g., Harken 57mm)")
    block_type: BlockType
    position: BlockPosition
    sheave_diameter_mm: float = Field(..., gt=0, description="Sheave diameter in mm")
    max_working_load_kg: float = Field(..., gt=0, description="Maximum working load in kg")
    install_date: date
    serial_number: Optional[str] = None
    notes: Optional[str] = None


class SheaveInspection(BaseModel):
    """Inspection data for a block sheave."""
    model_config = {"from_attributes": True}

    groove_depth_mm: float = Field(
        ..., ge=0, description="Groove depth in mm (0 = no groove)"
    )
    groove_depth_positions: list[float] = Field(
        default_factory=list,
        description="Groove depth measurements at 0, 90, 180, 270 degrees"
    )
    wear_pattern: WearPattern = WearPattern.NONE
    flange_condition: ConditionRating
    surface_condition: ConditionRating
    uv_degradation_visible: bool = False
    bore_diameter_mm: Optional[float] = Field(
        None, description="Bore diameter measurement"
    )
    bore_ovality_mm: Optional[float] = Field(
        None, description="Ovality of bore (max - min diameter)"
    )
    confidence: ConfidenceLevel = ConfidenceLevel.MEASURED


class BearingInspection(BaseModel):
    """Inspection data for block bearings."""
    model_config = {"from_attributes": True}

    bearing_type: str = Field(
        ..., description="ball_bearing, needle_bearing, or plain_bearing"
    )
    condition: ConditionRating
    noise_level: str = Field(
        ..., description="none, slight, moderate, excessive"
    )
    free_rotation: bool = Field(
        ..., description="Does the sheave rotate freely?"
    )
    play_radial_mm: Optional[float] = Field(
        None, description="Radial play in mm"
    )
    play_axial_mm: Optional[float] = Field(
        None, description="Axial play in mm"
    )
    pitting_observed: bool = False
    corrosion_observed: bool = False
    ball_count: Optional[int] = Field(
        None, description="Number of balls (for ball bearings)"
    )
    balls_condition: Optional[ConditionRating] = None
    confidence: ConfidenceLevel = ConfidenceLevel.MEASURED


class AxleInspection(BaseModel):
    """Inspection data for block axle."""
    model_config = {"from_attributes": True}

    diameter_measurements_mm: list[float] = Field(
        default_factory=list,
        description="Diameter measurements at multiple positions"
    )
    nominal_diameter_mm: float = Field(..., gt=0)
    min_diameter_mm: float = Field(..., gt=0)
    ovality_mm: float = Field(
        ..., ge=0, description="Max ovality (max-min diameter)"
    )
    surface_condition: ConditionRating
    corrosion_type: Optional[str] = Field(
        None, description="none, surface, pitting, crevice"
    )
    material_verified: Optional[str] = Field(
        None, description="316L, 304, titanium, etc."
    )
    confidence: ConfidenceLevel = ConfidenceLevel.MEASURED


class RatchetInspection(BaseModel):
    """Inspection data for ratchet mechanism."""
    model_config = {"from_attributes": True}

    ratchet_engages: bool = Field(
        ..., description="Does the ratchet engage properly?"
    )
    pawl_condition: ConditionRating
    spring_condition: ConditionRating
    tooth_profile_condition: ConditionRating
    pawl_count: int = Field(..., gt=0)
    pawls_operational: int = Field(..., ge=0)
    free_direction_smooth: bool = True
    notes: Optional[str] = None
    confidence: ConfidenceLevel = ConfidenceLevel.MEASURED


class BlockMaintenanceRecord(BaseModel):
    """Record of a single maintenance action on a block."""
    model_config = {"from_attributes": True}

    block_id: str
    maintenance_date: datetime
    maintenance_type: MaintenanceType
    technician: str
    sheave_inspection: Optional[SheaveInspection] = None
    bearing_inspection: Optional[BearingInspection] = None
    axle_inspection: Optional[AxleInspection] = None
    ratchet_inspection: Optional[RatchetInspection] = None
    overall_condition: ConditionRating
    lubricant_used: Optional[str] = None
    parts_replaced: list[str] = Field(default_factory=list)
    parts_replaced_cost_eur: float = Field(default=0, ge=0)
    labor_hours: float = Field(default=0, ge=0)
    next_maintenance_date: Optional[date] = None
    next_maintenance_type: Optional[MaintenanceType] = None
    photos: list[str] = Field(
        default_factory=list, description="Photo file paths"
    )
    notes: Optional[str] = None
    confidence: ConfidenceLevel = ConfidenceLevel.DOCUMENTED


class BlockWearAnalysis(BaseModel):
    """Analysis of block wear trends over time."""
    model_config = {"from_attributes": True}

    block_id: str
    analysis_date: datetime
    total_service_days: int = Field(..., ge=0)
    maintenance_records_count: int = Field(..., ge=0)
    current_groove_depth_mm: float = Field(..., ge=0)
    groove_rate_mm_per_year: Optional[float] = Field(
        None, description="Annual groove deepening rate"
    )
    estimated_sheave_remaining_life_years: Optional[float] = None
    bearing_replacements_count: int = Field(default=0, ge=0)
    average_bearing_life_months: Optional[float] = None
    overall_condition_trend: str = Field(
        ..., description="improving, stable, degrading"
    )
    recommended_action: str = Field(
        ..., description="continue_monitoring, schedule_service, replace_parts, replace_block"
    )
    estimated_annual_maintenance_cost_eur: float = Field(default=0, ge=0)
    confidence: ConfidenceLevel = ConfidenceLevel.CALCULATED


class BlockFleetSummary(BaseModel):
    """Summary of all blocks on a yacht."""
    model_config = {"from_attributes": True}

    yacht_id: str
    analysis_date: datetime
    total_blocks: int = Field(..., ge=0)
    blocks_excellent: int = Field(default=0, ge=0)
    blocks_good: int = Field(default=0, ge=0)
    blocks_fair: int = Field(default=0, ge=0)
    blocks_poor: int = Field(default=0, ge=0)
    blocks_critical: int = Field(default=0, ge=0)
    immediate_action_required: list[str] = Field(
        default_factory=list,
        description="Block IDs requiring immediate attention"
    )
    scheduled_replacements: list[dict] = Field(
        default_factory=list,
        description="Planned replacements with block_id and target_date"
    )
    estimated_annual_fleet_cost_eur: float = Field(default=0, ge=0)
    last_full_inspection_date: Optional[date] = None
    next_full_inspection_date: Optional[date] = None
    fleet_health_score: float = Field(
        ..., ge=0, le=100,
        description="Overall fleet health score (0-100)"
    )
    confidence: ConfidenceLevel = ConfidenceLevel.CALCULATED


class MaintenanceFailurePattern(BaseModel):
    """A documented maintenance-related failure pattern."""
    model_config = {"from_attributes": True}

    pattern_id: str = Field(..., description="e.g., F-W01")
    title_de: str = Field(..., description="German title")
    title_en: str = Field(..., description="English title")
    severity: str = Field(
        ..., description="low, medium, high, critical"
    )
    affected_block_types: list[BlockType]
    symptoms: list[str]
    root_causes: list[dict] = Field(
        ..., description="List of {cause, probability_pct}"
    )
    diagnosis_steps: list[str]
    remediation_steps: list[str]
    prevention_measures: list[str]
    estimated_repair_cost_eur: dict = Field(
        ..., description="{min, typical, max}"
    )
    estimated_consequential_damage_eur: dict = Field(
        ..., description="{min, typical, max}"
    )
    visual_detectability: ConfidenceLevel
    confidence: ConfidenceLevel = ConfidenceLevel.DOCUMENTED
```

### E.2 Beispiel-Integration in AYDI-Analyse

```python
"""
Example integration of block maintenance analysis in AYDI service patterns module.
"""

from datetime import datetime, date


def analyze_block_maintenance_status(
    blocks: list[dict],
    maintenance_records: list[dict],
    yacht_class: str,
    usage_profile: str,
) -> dict:
    """
    Analyze maintenance status of all blocks on a yacht.

    Args:
        blocks: List of block identification dicts
        maintenance_records: List of maintenance record dicts
        yacht_class: e.g., 'fahrtensegler', 'regattayacht', 'blauwasseryacht'
        usage_profile: e.g., 'freshwater_leisure', 'saltwater_leisure', 'racing', 'charter', 'bluewater'

    Returns:
        Analysis result dict with scores, findings, and recommendations
    """
    # Define maintenance intervals by usage profile (days)
    intervals = {
        "freshwater_leisure": {
            "lubrication": 180,
            "inspection": 365,
            "bearing_check": 730,
        },
        "saltwater_leisure": {
            "lubrication": 90,
            "inspection": 180,
            "bearing_check": 365,
        },
        "racing": {
            "lubrication": 30,
            "inspection": 90,
            "bearing_check": 180,
        },
        "charter": {
            "lubrication": 90,
            "inspection": 180,
            "bearing_check": 365,
        },
        "bluewater": {
            "lubrication": 45,
            "inspection": 90,
            "bearing_check": 180,
        },
    }

    profile_intervals = intervals.get(usage_profile, intervals["saltwater_leisure"])

    findings = []
    overdue_blocks = []
    critical_blocks = []
    score = 100.0

    today = date.today()

    for block in blocks:
        block_id = block["block_id"]

        # Find latest maintenance for this block
        block_records = [
            r for r in maintenance_records if r["block_id"] == block_id
        ]

        if not block_records:
            findings.append({
                "block_id": block_id,
                "finding": "Keine Wartungshistorie vorhanden",
                "severity": "high",
                "recommendation": "Sofortige Vollinspektion durchführen",
                "confidence": "estimated",
            })
            score -= 5.0
            overdue_blocks.append(block_id)
            continue

        latest = max(block_records, key=lambda r: r["maintenance_date"])
        days_since = (today - latest["maintenance_date"].date()).days

        # Check if overdue
        if days_since > profile_intervals["lubrication"]:
            overdue_days = days_since - profile_intervals["lubrication"]
            severity = "medium" if overdue_days < 90 else "high"
            findings.append({
                "block_id": block_id,
                "finding": f"Schmierung {overdue_days} Tage überfällig",
                "severity": severity,
                "recommendation": "Schmierung durchführen",
                "confidence": "calculated",
            })
            score -= 2.0 if severity == "medium" else 4.0
            overdue_blocks.append(block_id)

        # Check condition from latest record
        if latest.get("overall_condition") == "critical":
            critical_blocks.append(block_id)
            findings.append({
                "block_id": block_id,
                "finding": "Zustand kritisch — sofortiger Handlungsbedarf",
                "severity": "critical",
                "recommendation": "Block inspizieren und ggf. tauschen",
                "confidence": "documented",
            })
            score -= 10.0
        elif latest.get("overall_condition") == "poor":
            findings.append({
                "block_id": block_id,
                "finding": "Zustand schlecht — Austausch planen",
                "severity": "high",
                "recommendation": "Ersatzteile beschaffen, Austausch in nächster Wartung",
                "confidence": "documented",
            })
            score -= 5.0

    # Clamp score
    score = max(0.0, min(100.0, score))

    return {
        "module": "block_maintenance",
        "yacht_class": yacht_class,
        "usage_profile": usage_profile,
        "analysis_date": datetime.now().isoformat(),
        "total_blocks": len(blocks),
        "overdue_blocks": len(overdue_blocks),
        "critical_blocks": len(critical_blocks),
        "score": round(score, 1),
        "findings": findings,
        "recommendations": _generate_fleet_recommendations(
            findings, len(blocks), usage_profile
        ),
        "confidence": "calculated",
    }


def _generate_fleet_recommendations(
    findings: list[dict],
    total_blocks: int,
    usage_profile: str,
) -> list[dict]:
    """Generate fleet-level recommendations based on findings."""
    recommendations = []

    critical_count = sum(1 for f in findings if f["severity"] == "critical")
    high_count = sum(1 for f in findings if f["severity"] == "high")
    overdue_count = sum(1 for f in findings if "überfällig" in f.get("finding", ""))

    if critical_count > 0:
        recommendations.append({
            "priority": "immediate",
            "action_de": f"{critical_count} Block/Blöcke in kritischem Zustand — sofortige Inspektion erforderlich",
            "action_en": f"{critical_count} block(s) in critical condition — immediate inspection required",
            "estimated_cost_eur": critical_count * 150,
        })

    if overdue_count > total_blocks * 0.5:
        recommendations.append({
            "priority": "high",
            "action_de": "Über 50% der Blöcke haben überfällige Wartung — Wartungstag einplanen",
            "action_en": "Over 50% of blocks have overdue maintenance — schedule maintenance day",
            "estimated_cost_eur": total_blocks * 10,
        })

    if high_count > 0:
        recommendations.append({
            "priority": "medium",
            "action_de": f"{high_count} Block/Blöcke benötigen zeitnahe Aufmerksamkeit",
            "action_en": f"{high_count} block(s) need attention soon",
            "estimated_cost_eur": high_count * 80,
        })

    return recommendations
```

---

## ANHANG F — Inspektions-Checklisten

### F.1 Saisonstart-Checkliste (Frühjahr)

| Nr. | Prüfpunkt | OK | Bemerkung |
|-----|----------|-----|----------|
| 1 | Alle Blöcke visuell auf Winterschäden geprüft | ☐ | |
| 2 | Scheiben drehen frei | ☐ | |
| 3 | Keine sichtbare Korrosion | ☐ | |
| 4 | Keine Feuchtigkeit in Lagern (Kondensat) | ☐ | |
| 5 | Alte Winterschmierung entfernt (wenn verhärtet) | ☐ | |
| 6 | Frische Schmierung aufgetragen | ☐ | |
| 7 | Ratschenblöcke: Mechanismus funktioniert | ☐ | |
| 8 | Snatchblöcke: Öffnung/Verriegelung funktioniert | ☐ | |
| 9 | Alle Befestigungen fest | ☐ | |
| 10 | Schäkel/Bolzen: Sicherungen vorhanden | ☐ | |
| 11 | Tauwerk durch Blöcke eingeschoren, läuft frei | ☐ | |
| 12 | Unter-Last-Test (Segel setzen) bestanden | ☐ | |

### F.2 Monatliche Schnell-Checkliste

| Nr. | Prüfpunkt | OK | Bemerkung |
|-----|----------|-----|----------|
| 1 | Sichtprüfung alle zugänglichen Blöcke | ☐ | |
| 2 | Funktionsprüfung (Scheibe dreht frei) | ☐ | |
| 3 | Ungewöhnliche Geräusche? | ☐ | |
| 4 | Befestigungen fest? | ☐ | |
| 5 | Tauwerk-Zustand am Block? | ☐ | |

### F.3 Jährliche Vollinspektion-Checkliste (pro Block)

| Nr. | Prüfpunkt | OK | Messwert | Bemerkung |
|-----|----------|-----|---------|----------|
| 1 | Block-ID und Position dokumentiert | ☐ | — | |
| 2 | Block demontiert | ☐ | — | |
| 3 | Alle Teile gereinigt | ☐ | — | |
| 4 | Scheibe: Rillentiefe gemessen | ☐ | ___ mm | |
| 5 | Scheibe: Rillenform dokumentiert | ☐ | — | |
| 6 | Scheibe: Flanken intakt | ☐ | — | |
| 7 | Scheibe: Oberfläche (UV, Risse) | ☐ | — | |
| 8 | Scheibe: Bohrung gemessen | ☐ | ___ mm | |
| 9 | Scheibe: Bohrung Ovalisierung | ☐ | ___ mm | |
| 10 | Lager: Typ dokumentiert | ☐ | — | |
| 11 | Lager: Zustand bewertet | ☐ | — | |
| 12 | Lager: Kugeln/Nadeln geprüft | ☐ | — | |
| 13 | Lager: Laufflächen geprüft | ☐ | — | |
| 14 | Lager: Spiel gemessen (radial) | ☐ | ___ mm | |
| 15 | Lager: Spiel gemessen (axial) | ☐ | ___ mm | |
| 16 | Achse: Durchmesser gemessen (3 Pos.) | ☐ | ___ mm | |
| 17 | Achse: Ovalisierung berechnet | ☐ | ___ mm | |
| 18 | Achse: Oberfläche (Korrosion, Riefen) | ☐ | — | |
| 19 | Wangen: Risse, Korrosion, Verformung | ☐ | — | |
| 20 | Befestigung: Schrauben/Bolzen Zustand | ☐ | — | |
| 21 | Ratsche: Mechanismus geprüft (wenn zutreffend) | ☐ | — | |
| 22 | Snatch: Verriegelung geprüft (wenn zutreffend) | ☐ | — | |
| 23 | Schmierung aufgetragen | ☐ | — | |
| 24 | Zusammenbau, Funktionstest | ☐ | — | |
| 25 | Gesamtzustand bewertet | ☐ | — | |
| 26 | Nächster Wartungstermin festgelegt | ☐ | — | |
| 27 | Fotos gemacht | ☐ | — | |

---

## ANHANG G — Verschleißgrenzwert-Tabellen

### G.1 Scheiben-Verschleißgrenzwerte

| Scheibendurchmesser | Material | Rillentiefe Max. (Fahrt) | Rillentiefe Max. (Regatta) | Flankenrest-Höhe Min. |
|--------------------|---------|------------------------|--------------------------|---------------------|
| 16–25 mm | Acetal | 0,8 mm | 0,4 mm | 2,0 mm |
| 16–25 mm | Aluminium | 1,0 mm | 0,5 mm | 2,0 mm |
| 29–40 mm | Acetal | 1,0 mm | 0,5 mm | 2,5 mm |
| 29–40 mm | Aluminium | 1,2 mm | 0,5 mm | 2,5 mm |
| 45–57 mm | Acetal | 1,0 mm | 0,5 mm | 3,0 mm |
| 45–57 mm | Aluminium | 1,2 mm | 0,6 mm | 3,0 mm |
| 75 mm + | Aluminium | 1,5 mm | 0,8 mm | 4,0 mm |
| 75 mm + | Edelstahl | 1,0 mm | 0,5 mm | 4,0 mm |

### G.2 Achsen-Verschleißgrenzwerte

| Nenn-Ø (mm) | Min. Ø (Fahrt) | Min. Ø (Regatta) | Max. Ovalisierung | Material |
|-------------|---------------|-----------------|------------------|---------|
| 4,0 | 3,94 | 3,96 | 0,02 | Edelstahl 316L |
| 5,0 | 4,93 | 4,95 | 0,02 | Edelstahl 316L |
| 6,0 | 5,92 | 5,94 | 0,02 | Edelstahl 316L |
| 6,35 (1/4") | 6,27 | 6,30 | 0,02 | Edelstahl 316L |
| 8,0 | 7,90 | 7,94 | 0,03 | Edelstahl 316L |
| 10,0 | 9,88 | 9,92 | 0,03 | Edelstahl 316L |
| 12,0 | 11,85 | 11,90 | 0,04 | Edelstahl 316L |
| 12,7 (1/2") | 12,54 | 12,60 | 0,04 | Edelstahl 316L |
| 16,0 | 15,82 | 15,88 | 0,05 | Edelstahl 316L |
| 20,0 | 19,78 | 19,85 | 0,05 | Edelstahl 316L |

### G.3 Lagerspiel-Grenzwerte

| Lagertyp | Soll-Radialspiel | Max. Radialspiel | Soll-Axialspiel | Max. Axialspiel |
|----------|-----------------|-----------------|----------------|----------------|
| Kugellager (klein, <30mm) | 0,01–0,02 mm | 0,06 mm | 0,01–0,03 mm | 0,08 mm |
| Kugellager (mittel, 30–55mm) | 0,01–0,03 mm | 0,08 mm | 0,02–0,05 mm | 0,10 mm |
| Kugellager (groß, >55mm) | 0,02–0,04 mm | 0,10 mm | 0,03–0,06 mm | 0,12 mm |
| Nadellager (alle) | 0,01–0,03 mm | 0,08 mm | 0,02–0,04 mm | 0,10 mm |
| Gleitlager (Acetal) | 0,03–0,08 mm | 0,15 mm | 0,05–0,10 mm | 0,20 mm |
| Gleitlager (Torlon) | 0,02–0,05 mm | 0,12 mm | 0,03–0,08 mm | 0,15 mm |
| Gleitlager (PEEK) | 0,02–0,05 mm | 0,12 mm | 0,03–0,08 mm | 0,15 mm |

### G.4 Kugel- und Nadel-Grenzwerte

| Bauteil | Prüfkriterium | Akzeptabel | Austausch |
|---------|--------------|-----------|----------|
| Kugel Ø-Abweichung | Messung | <0,005 mm | >0,005 mm |
| Kugel Oberflächenrauhigkeit | Sicht/Taktil | Spiegelglatt | Matte Stellen, Pitting |
| Kugel Rundheit | Rolltest auf Glas | Gerade, leise | Unrund, Klicken |
| Kugel Farbveränderung | Sicht | Gleichmäßig metallisch | Blaulauf, braune Flecken |
| Nadel Geradheit | Rolltest auf Glas | Gerade | Gebogen, kippt |
| Nadel Oberflächenrauhigkeit | Sicht 10x Lupe | Glatt | Riefen, Pitting |
| Nadel Durchmesser-Abweichung | Messung | <0,005 mm | >0,005 mm |

---

## ANHANG H — Werkzeug- und Materialübersicht

### H.1 Werkzeugkasten Block-Wartung

**Basis-Kit (für Eigner, ca. 80–120 €):**

| Werkzeug | Spezifikation | Ca. Preis |
|----------|--------------|----------|
| Innensechskant-Satz metrisch | 1,5–10 mm, Edelstahl | 15 € |
| Innensechskant-Satz Zoll | 1/16"–3/8" | 12 € |
| Schraubendreher-Set | Kreuz + Schlitz, klein–mittel | 15 € |
| Spitzzange | Edelstahl, 150 mm | 10 € |
| Sicherungsring-Zange innen | 10–50 mm | 12 € |
| Sicherungsring-Zange außen | 10–50 mm | 12 € |
| Messschieber digital | 150 mm, 0,01 mm | 25 € |
| Lupe | 10x, mit LED | 8 € |
| Magnetische Schale | 100 mm | 5 € |
| Mikrofasertücher | 5er Pack | 5 € |

**Profi-Kit (zusätzlich, ca. 150–250 €):**

| Werkzeug | Spezifikation | Ca. Preis |
|----------|--------------|----------|
| Drehmomentschlüssel | 1–25 Nm, 1/4" | 45 € |
| Mikrometer | 0–25 mm, 0,01 mm | 35 € |
| Tiefenmessschieber | 150 mm | 20 € |
| Ultraschall-Reiniger | 0,6 L, 35 W | 40 € |
| Eindring-Prüfset | Rot/Weiß, Diffu-Therm | 25 € |
| Pin-Ausdrücker Set | 1–10 mm | 15 € |
| Kunststoff-Durchschläge | 3–12 mm | 10 € |
| Druckluft-Dose | 400 ml | 8 € |

### H.2 Schmiermittel-Vorrat für eine Saison

| Produkt | Menge | Anwendung | Ca. Preis |
|---------|-------|----------|----------|
| Harken One Lube | 1 × 100 ml | Lager aller Blöcke | 18 € |
| McLube Sailkote | 1 × 300 ml | Scheiben, Tauwerk-Kontakt | 22 € |
| Boeshield T-9 | 1 × 118 ml | Korrosionsschutz, Einwintern | 15 € |
| Tef-Gel | 1 × 50 g | Befestigungsschrauben | 18 € |
| Isopropanol | 1 × 500 ml | Reinigung | 6 € |
| Mildes Spülmittel | 1 × 250 ml | Einweichen | 3 € |
| **Gesamtkosten Verbrauchsmaterial** | | | **ca. 82 €** |

---

## ANHANG I — Hersteller-Kontakte und Ersatzteilbeschaffung

### I.1 Hersteller-Kontakte

| Hersteller | Land | Website | Ersatzteil-Service |
|-----------|------|---------|-------------------|
| Harken | USA/IT | harken.com | Einzelteile über Händler, Kits direkt |
| Lewmar | UK | lewmar.com | Ersatzteilkatalog online, Direktversand |
| Ronstan | AUS | ronstan.com | Einzelteile über Händler |
| Antal | IT | antal.it | Direkt und über Händler |
| Seldén | SE | sfrya.com | Über Seldén-Händlernetz |
| Spinlock | UK | spinlock.co.uk | Kits und Einzelteile über Händler |
| Wichard | FR | wichard.com | Über Fachhändler |
| Schaefer | USA | schaefermarine.com | Über US-Händler, international begrenzt |
| Holt | UK | holtmarine.co.uk | Über Fachhändler |
| Allen | UK | allenbrothers.co.uk | Direkt und über Händler |

### I.2 Ersatzteil-Beschaffungsstrategien

**In Europa:**
- Primär: Lokaler Yachtausrüster (SVB, Toplicht, Compass24, Accastillage Diffusion)
- Sekundär: Online-Händler (Amazon Marine, eBay Nautic)
- Tertiär: Direkt beim Hersteller (oft Mindestbestellwert)

**Auf Langfahrt:**
- Ersatzteile vor Abreise in ausreichender Menge beschaffen
- In Hauptrevieren (Karibik: Budget Marine; Mittelmeer: lokale Shipchandler): Harken und Lewmar meist verfügbar
- In abgelegenen Revieren (Pazifik, Indischer Ozean): Selbstversorgung planen
- Generische Ersatzteile (Kugellager, Achsen) bei lokalen Industrielieferanten beschaffbar

**Identifikation von Ersatzteilen:**
1. Hersteller und Modellnummer vom Block ablesen
2. Explosionszeichnung des Modells im Herstellerkatalog suchen
3. Einzelteile anhand der Explosionszeichnung identifizieren
4. Teilenummern notieren und bestellen
5. Im Zweifelsfall: Foto des Blocks und der benötigten Teile an Hersteller senden

---

## ANHANG J — Wartungsprotokoll-Vorlagen

### J.1 Einzelblock-Wartungsprotokoll

```
═══════════════════════════════════════════════════════════════
BLOCK-WARTUNGSPROTOKOLL
═══════════════════════════════════════════════════════════════

Yacht: _________________________ Datum: _______________

BLOCK-IDENTIFIKATION:
Block-ID: _____________ Position: _____________________
Hersteller: ____________ Modell: ______________________
Einbaudatum: ___________ Letzte Wartung: ______________

INSPEKTION:
☐ Scheibe dreht frei    ☐ Keine Geräusche
☐ Kein Seitenschlag     ☐ Befestigung fest

MESSWERTE:
Rillentiefe (mm): _____ / _____ / _____ / _____ (4 Pos.)
Achsdurchmesser (mm): _____ / _____ / _____ (3 Pos.)
Lagerspiel radial (mm): _____
Lagerspiel axial (mm): _____

ZUSTAND:
Scheibe:     ☐ Exzellent  ☐ Gut  ☐ Ausreichend  ☐ Schlecht  ☐ Kritisch
Lager:       ☐ Exzellent  ☐ Gut  ☐ Ausreichend  ☐ Schlecht  ☐ Kritisch
Achse:       ☐ Exzellent  ☐ Gut  ☐ Ausreichend  ☐ Schlecht  ☐ Kritisch
Wangen:      ☐ Exzellent  ☐ Gut  ☐ Ausreichend  ☐ Schlecht  ☐ Kritisch
Befestigung: ☐ Exzellent  ☐ Gut  ☐ Ausreichend  ☐ Schlecht  ☐ Kritisch
Gesamt:      ☐ Exzellent  ☐ Gut  ☐ Ausreichend  ☐ Schlecht  ☐ Kritisch

MASSNAHMEN:
☐ Gereinigt  ☐ Geschmiert  ☐ Lager getauscht
☐ Scheibe getauscht  ☐ Achse getauscht  ☐ Block komplett getauscht
Schmiermittel: ____________________
Getauschte Teile: _________________
Kosten Teile: _______ €   Arbeitszeit: _______ h

NÄCHSTE WARTUNG:
Datum: ______________ Art: __________________________

Techniker: _________________ Unterschrift: __________
═══════════════════════════════════════════════════════════════
```

### J.2 Flotten-Übersichtsblatt

```
═══════════════════════════════════════════════════════════════
BLOCK-FLOTTEN-ÜBERSICHT
═══════════════════════════════════════════════════════════════

Yacht: _________________________ Datum: _______________
Anzahl Blöcke gesamt: _____ Letzte Vollinspektion: _________

Nr | Block-ID | Position         | Hersteller | Zustand | Nächste Wartung
---|----------|-----------------|-----------|---------|---------------
 1 | ________ | ________________ | _________ | _______ | ______________
 2 | ________ | ________________ | _________ | _______ | ______________
 3 | ________ | ________________ | _________ | _______ | ______________
 4 | ________ | ________________ | _________ | _______ | ______________
 5 | ________ | ________________ | _________ | _______ | ______________
 6 | ________ | ________________ | _________ | _______ | ______________
 7 | ________ | ________________ | _________ | _______ | ______________
 8 | ________ | ________________ | _________ | _______ | ______________
 9 | ________ | ________________ | _________ | _______ | ______________
10 | ________ | ________________ | _________ | _______ | ______________
11 | ________ | ________________ | _________ | _______ | ______________
12 | ________ | ________________ | _________ | _______ | ______________
13 | ________ | ________________ | _________ | _______ | ______________
14 | ________ | ________________ | _________ | _______ | ______________
15 | ________ | ________________ | _________ | _______ | ______________
16 | ________ | ________________ | _________ | _______ | ______________
17 | ________ | ________________ | _________ | _______ | ______________
18 | ________ | ________________ | _________ | _______ | ______________
19 | ________ | ________________ | _________ | _______ | ______________
20 | ________ | ________________ | _________ | _______ | ______________

ZUSAMMENFASSUNG:
Exzellent: ___ | Gut: ___ | Ausreichend: ___ | Schlecht: ___ | Kritisch: ___

Sofortiger Handlungsbedarf: ___________________________________
Geplante Austausche: __________________________________________
Geschätzte Kosten nächste Saison: _________ €

Techniker: _________________ Unterschrift: __________
═══════════════════════════════════════════════════════════════
```

---

## ANHANG K — Saisonale Wartungskalender

### K.1 Nordeuropa (Ostsee, Nordsee, Atlantik)

| Monat | Maßnahme | Priorität |
|-------|---------|-----------|
| März | Saisonvorbereitung: Blöcke prüfen, schmieren | Hoch |
| April | Saisonstart: Funktionstest unter Last | Hoch |
| Mai | Monatliche Schnellinspektion | Mittel |
| Juni | Mitsaison-Check, Nachschmierung | Mittel |
| Juli | Monatliche Schnellinspektion | Mittel |
| August | Mitsaison-Check, Nachschmierung | Mittel |
| September | Monatliche Schnellinspektion | Mittel |
| Oktober | Einwintern: Vollinspektion, Konservierung | Hoch |
| November–Februar | Winterlager: Ersatzteile bestellen, Reparaturen planen | Niedrig |

### K.2 Mittelmeer (ganzjährig)

| Monat | Maßnahme | Priorität |
|-------|---------|-----------|
| Januar | Vierteljahres-Inspektion, Schmierung | Mittel |
| Februar | Monatliche Schnellinspektion | Niedrig |
| März | Monatliche Schnellinspektion | Niedrig |
| April | Vierteljahres-Inspektion, Schmierung | Mittel |
| Mai | Monatliche Schnellinspektion | Niedrig |
| Juni | Sommer-Intensivcheck (UV-Schutz prüfen!) | Hoch |
| Juli | Vierteljahres-Inspektion, Schmierung (Hitze!) | Hoch |
| August | Monatliche Schnellinspektion | Mittel |
| September | Monatliche Schnellinspektion | Niedrig |
| Oktober | Vierteljahres-Inspektion, Schmierung | Mittel |
| November | Jahresinspektion / Vollwartung | Hoch |
| Dezember | Monatliche Schnellinspektion | Niedrig |

### K.3 Tropen (Karibik, Südostasien)

| Zeitraum | Maßnahme | Priorität |
|----------|---------|-----------|
| Alle 6 Wochen | Vollschmierung aller Blöcke | Hoch |
| Monatlich | Sichtinspektion, UV-Schutz prüfen | Hoch |
| Vierteljährlich | Vollinspektion, Scheiben messen | Hoch |
| Halbjährlich | Demontage und Generalinspektion | Hoch |
| Vor Hurrikansaison (Mai) | Alle sicherheitskritischen Blöcke Vollservice | Kritisch |
| Nach Hurrikansaison (Dez) | Bestandsaufnahme, Schäden beheben | Hoch |

---

## ANHANG L — Confidence-Mapping

### L.1 Confidence-Zuordnung für Blockwartungs-Befunde

| Befundtyp | Datenquelle | Confidence Level | Anzeige |
|----------|------------|-----------------|---------|
| Rillentiefe gemessen | Messschieber vor Ort | measured | Grünes Badge |
| Achsdurchmesser gemessen | Mikrometer vor Ort | measured | Grünes Badge |
| Lagerspiel gemessen | Messung vor Ort | measured | Grünes Badge |
| Lagerzustand aus Foto | AYDI Visual Analyse | visual_medium | Blaues Badge |
| Rillenbildung aus Foto | AYDI Visual Analyse | visual_medium | Blaues Badge |
| Korrosion aus Foto | AYDI Visual Analyse | visual_high | Blaues Badge |
| UV-Degradation aus Foto | AYDI Visual Analyse | visual_medium | Blaues Badge |
| Wartungsintervall berechnet | Aus Logbuch-Daten | calculated | Grünes Badge |
| Lebensdauerprognose | Statistisches Modell | estimated | Graues Badge |
| Typische Lebensdauer | Branchendurchschnitt | benchmark | Graues Badge |
| Eigner-Bericht | Textanalyse | documented | Blaues Badge |
| Hersteller-Spezifikation | Datenblatt | measured | Grünes Badge |

### L.2 Einschränkungen der visuellen Analyse

Bestimmte Wartungsbefunde können durch Fotoanalyse (Pipeline B) nur eingeschränkt erkannt werden:

| Befund | Visuelle Erkennbarkeit | Confidence | Anmerkung |
|--------|----------------------|-----------|-----------|
| Grobe Rillenbildung | Gut erkennbar | visual_high | Ab ca. 0,5 mm sichtbar |
| Feine Rillenbildung | Schlecht erkennbar | visual_low | Unter 0,5 mm nur bei Nahaufnahme |
| Lagergeräusche | Nicht erkennbar | visual_insufficient | Nur durch Funktionsprüfung |
| Lagerspiel | Nicht erkennbar | visual_insufficient | Nur durch Messung |
| Korrosion (grob) | Gut erkennbar | visual_high | Farbveränderung sichtbar |
| Korrosion (fein) | Mäßig erkennbar | visual_medium | Nur bei Nahaufnahme |
| UV-Degradation | Mäßig erkennbar | visual_medium | Verfärbung sichtbar, Sprödigkeit nicht |
| Gebrochene Flanke | Gut erkennbar | visual_high | Deutliche Kontur-Veränderung |
| Ermüdungsriss | Schlecht erkennbar | visual_low | Oft nur unter Last sichtbar |
| Achskorrosion | Nicht erkennbar | visual_insufficient | Achse meist verdeckt |

---

## ANHANG M — Normen und Regelwerke

### M.1 Relevante Normen für Blockwartung

| Norm | Titel | Relevanz für Blockwartung |
|------|-------|--------------------------|
| ISO 12401:2009 | Deck safety harness and safety line | Befestigung von Sicherheitsblöcken |
| ISO 15084:2003 | Anchoring, mooring and towing | Blöcke in Ankersystemen |
| ISO 12215-5:2019 | Small craft — Hull construction and scantlings — Part 5: Design pressures for monohulls, design stresses, scantlings determination | Lasteneinleitung der Blockbefestigung ins Deck (Deck-Design-Drücke/Scantlings) |
| ISO 15085:2003 | Man-overboard prevention | Blöcke im Sicherheitssystem |
| EN 13411-7:2006 | Terminations for steel wire ropes | Drahtseile in Block-Systemen |
| DIN 15400 | Lastaufnahmemittel | Allgemeine Prüfvorschriften für Hebezeuge (analog anwendbar) |

> ✅ Aufgeloest (Audit): ISO 12215-9:2012 ist „Small craft — Hull construction and scantlings — Part 9: Sailing craft appendages" (Lasten/Scantlings von Kiel/Schwert/Ruder-Anhängen), NICHT die Lasteneinleitung von Deckbeschlägen. Für die Krafteinleitung der Blockbefestigung ins Deck ist ISO 12215-5 (Deck-Design-Drücke/Scantlings) einschlägig; ABYC H-40 (Strong Points/Backing Plates) ist in M.2 gelistet. Zeile auf ISO 12215-5:2019 korrigiert. Quelle: iso.org/standard/55339.html (12215-9), iso.org/standard/69552.html (12215-5).

### M.2 Herstellerstandards

| Standard | Herausgeber | Inhalt |
|---------|------------|--------|
| Harken Technical Bulletin TB-001 | Harken | Wartungsintervalle und -verfahren |
| Lewmar Care & Maintenance Guide | Lewmar | Allgemeine Wartungshinweise |
| Ronstan Maintenance Handbook | Ronstan | Block- und Beschlagwartung |
| ABYC H-40 | American Boat & Yacht Council | Anchoring, Mooring & Strong Points (lasttragende Deck-Beschläge, Backing Plates, Sicherheitsfaktor für Strong Points) |

---

## ANHANG N — Digitale Wartungsüberwachung

### N.1 AYDI-Integration: Automatische Wartungserinnerungen

Das AYDI-System kann Blockwartung digital unterstützen:

**Funktionen:**
- Digitales Block-Inventar mit ID-Nummern und Fotos
- Automatische Wartungserinnerungen basierend auf Nutzungsprofil
- Trend-Analyse: Verschleißkurven pro Block über Jahre
- Kostenprognose für Ersatzteile und Arbeitszeit
- Foto-basierte Zustandserfassung (Pipeline B)
- Integration mit Service-Reports (Pipeline C)

**Datenerfassung:**
- Manuelle Eingabe: Messwerte, Zustandsbewertungen
- Foto-Upload: AYDI analysiert visuell erkennbare Verschleißmuster
- Automatisch: Berechnung von Verschleißraten, Lebensdauer-Prognosen

### N.2 Empfohlene Drittanbieter-Apps

| App | Plattform | Funktion | Preis |
|-----|----------|---------|-------|
| Dockwa Logbook | iOS/Android | Wartungslogbuch, Erinnerungen | Kostenlos |
| Helm Connect | Web | Professionelles Flottenmanagement | Ab 50 $/Monat |
| Boat Maintenance Log | iOS/Android | Einfaches Wartungstagebuch | 5 € |
| Maintainly Marine | Web | Wartungsplanung, Ersatzteil-Tracking | Ab 20 €/Monat |

---

## ANHANG O — Kostenmodelle Wartung vs. Austausch

### O.1 Kostenvergleich: Wartung vs. Vernachlässigung

**Szenario: 12m-Fahrtensegelyacht, 25 Blöcke, 10 Jahre Betrieb**

| Strategie | Jährliche Kosten | 10-Jahres-Kosten | Blockausfälle | Folgeschäden |
|----------|-----------------|------------------|--------------|-------------|
| Präventive Wartung | 150–250 €/Jahr | 1.500–2.500 € | 0–1 | Keine |
| Moderate Wartung | 50–100 €/Jahr | 500–1.000 € + Reparaturen | 2–4 | 500–2.000 € |
| Keine Wartung | 0 €/Jahr | Austausch 3.000–5.000 € | 5–10 | 1.000–5.000 € |

**Fazit:** Präventive Wartung kostet ca. 200 €/Jahr und spart über 10 Jahre typischerweise 2.000–7.000 € gegenüber vollständiger Vernachlässigung.

### O.2 Einzelblock-Kostenmodell

| Maßnahme | Kosten (Material) | Kosten (Arbeit, Selbst) | Kosten (Arbeit, Werft) |
|----------|-------------------|----------------------|----------------------|
| Süßwasserspülung | 0 € | 2 min | — |
| Schmierung | 1–2 € | 5 min | 15–25 € |
| Vollinspektion | 2–5 € | 30 min | 40–60 € |
| Lagertausch | 30–80 € | 45 min | 80–150 € |
| Scheibentausch | 20–60 € | 30 min | 60–120 € |
| Achstausch | 15–40 € | 30 min | 50–100 € |
| Block komplett tauschen | 60–400 € | 20 min | 80–200 € |

### O.3 Break-Even-Analyse: Reparatur vs. Neukauf

**Faustregel:** Wenn die Reparaturkosten (Material + Arbeit) mehr als 60 % des Neupreises betragen, ist ein Neukauf wirtschaftlicher — es sei denn, der Block ist ein Spezialmodell mit langer Lieferzeit.

| Block-Neupreis | Max. sinnvolle Reparaturkosten | Typische Reparatur |
|---------------|------------------------------|-------------------|
| < 50 € | 20 € | Nur Schmierung/Reinigung |
| 50–100 € | 40 € | Lagertausch |
| 100–200 € | 80 € | Lager + Scheibe |
| 200–400 € | 160 € | Vollüberholung |
| > 400 € | 250 € | Alles außer gebrochene Wangen |

---

## ANHANG P — Umwelt- und Entsorgungshinweise

### P.1 Umweltaspekte der Blockwartung

**Schmiermittel:**
- Alle Schmiermittel von Block-Oberflächen können ins Wasser gelangen.
- Bevorzugt biologisch abbaubare Produkte verwenden (wo verfügbar).
- Beim Schmieren im Hafen: Auffangschale unter den Block halten.
- Altöl und Reinigungsflüssigkeiten als Sonderabfall entsorgen.

**Reinigungsmittel:**
- Keine chlorhaltigen Reiniger im Hafenbereich verwenden.
- Isopropanol in kleinen Mengen akzeptabel, größere Mengen als Sonderabfall.
- Süßwasserspülung mit Spülmittel: Biologisch abbaubares Spülmittel verwenden.

### P.2 Entsorgung alter Blockteile

| Material | Entsorgungsweg | Hinweis |
|---------|---------------|--------|
| Aluminium-Scheiben/-Wangen | Metallrecycling (Aluminiumsammlung) | Nicht in Restmüll |
| Edelstahl-Achsen/-Bolzen | Metallrecycling (Stahlsammlung) | Nicht in Restmüll |
| Polymer-Teile (POM, PA) | Kunststoffrecycling (wenn sortenrein) | Sonst Restmüll |
| Kugeln/Nadeln | Metallrecycling | Kleine Mengen im Restmüll akzeptabel |
| Schmiermittelreste | Altöl-Sammlung | Niemals ins Wasser! |
| Reinigungsflüssigkeiten | Sondermüll (Lösungsmittel) | Niemals in Abfluss! |

---

## ANHANG Q — Schulung und Qualifikation

### Q.1 Empfohlene Qualifikation für Blockwartung

| Stufe | Qualifikation | Empfohlene Tätigkeiten |
|-------|--------------|----------------------|
| Eigner-Basis | Grundkenntnisse Segeln + dieses Handbuch | Sichtprüfung, Schmierung, einfache Reinigung |
| Eigner-Fortgeschritten | + Erfahrung mit Demontage/Montage | Vollinspektion, Lagertausch, Scheibentausch |
| Bootswain/Techniker | + Ausbildung Rigging/Bootsbau | Alle Wartungsarbeiten, Fehlerdiagnose |
| Rigger/Spezialist | + Spezialisierung Rigg/Beschläge | Komplexe Reparaturen, Systemoptimierung |

### Q.2 Lernressourcen

**Bücher:**
- Brion Toss: „The Complete Rigger's Apprentice" — Kapitel über Beschläge und Wartung
- Don Casey: „This Old Boat" — Kapitel über Deck-Hardware
- Nigel Calder: „Boatowner's Mechanical and Electrical Manual" — Rigg-Wartung

**Online:**
- Harken YouTube-Kanal: Block-Wartungsvideos
- SailingAnarchy Forum: Block-Diskussionen und Erfahrungsberichte
- Practical Sailor: Testberichte und Wartungstipps

**Kurse:**
- Praktische Rigg-Seminare (z.B. bei Rigger-Ausbildungsstätten)
- Herstellerworkshops (Harken bietet gelegentlich Workshops an)
- Segelschul-Fortbildungen mit Wartungsschwerpunkt

---

## ANHANG R — Weiterführende Ressourcen

### R.1 Weiterführende AYDI-Wissensdateien

| Datei | Thema | Relevanz für Blockwartung |
|-------|-------|--------------------------|
| 10_01_bloecke_grundlagen.md | Blocktypen, Materialien, Dimensionierung | Grundlagenwissen |
| 10_02_harken_bloecke.md | Harken-spezifische Details | Herstellerspezifisch |
| 10_03_lewmar_ronstan_bloecke.md | Lewmar und Ronstan Details | Herstellerspezifisch |
| 01_10_deck_beschlag_abdichtung.md | Abdichtung von Decksbeschlägen | Für Blockbefestigungen |

### R.2 Hersteller-Dokumentation

| Hersteller | Dokument | Verfügbarkeit |
|-----------|---------|---------------|
| Harken | Product Catalog & Technical Guide | harken.com (PDF-Download) |
| Harken | Maintenance & Care Instructions | In jeder Blockverpackung |
| Lewmar | Block Maintenance Guide | lewmar.com (Support-Bereich) |
| Ronstan | Product Care Sheet | ronstan.com (Downloads) |
| Antal | Installation & Maintenance Manual | antal.it (Dokumentation) |

### R.3 Fachzeitschriften und Testberichte

| Publikation | Sprache | Relevante Themen |
|------------|---------|-----------------|
| Practical Sailor | EN | Block-Vergleichstests, Schmiermitteltests |
| YACHT (Delius Klasing) | DE | Produkttests, Wartungstipps |
| Segeln Magazin | DE | Praxisberichte, Erfahrungen |
| Sailing World | EN | Regatta-Equipment, Performance |
| Yachting Monthly | EN | Wartungsserien, Langfahrt-Erfahrungen |
| Cruising World | EN | Blauwasser-Wartungstipps |

### R.4 Online-Communities

| Community | Plattform | Relevanz |
|----------|----------|---------|
| Segeln-Forum.de | Web | Deutschsprachige Diskussionen zu Blockwartung |
| SailingAnarchy.com | Web | Englischsprachig, technisch detailliert |
| Cruisers Forum | Web | Langfahrt-Erfahrungen, Wartungstipps |
| Reddit r/sailing | Reddit | Allgemeine Segelfragen, Wartung |
| YBW Forum | Web | Britische Perspektive, Lewmar-Expertise |

### R.5 Lieferanten für Ersatzteile und Werkzeuge (DACH-Region)

| Lieferant | Land | Spezialisierung | Online-Shop |
|----------|------|----------------|-------------|
| SVB (Sailing & Boating) | DE | Yachtausrüster, breites Sortiment | svb-marine.de |
| Toplicht | DE | Yachtausrüster, Hamburg | toplicht.de |
| Compass24 | DE | Online-Yachtausrüster | compass24.de |
| AWN | DE | Yachtausrüster, Norddeutschland | awn.de |
| Busse Yachtshop | DE | Yachtausrüster, spezialisiert | busse-yachtshop.de |
| HanseNautic | DE | Spezialisiert auf Navigation + Beschläge | hansenautic.de |
| Yachticon | DE | Pflegemittel, Schmierstoffe | yachticon.de |
| Voile et Moteur | CH | Schweizer Yachtausrüster | voileetmoteur.ch |
| Yachtshop24 | AT | Österreichischer Online-Yachtshop | yachtshop24.at |

### R.6 Lieferanten International

| Lieferant | Land | Spezialisierung | Online-Shop |
|----------|------|----------------|-------------|
| Accastillage Diffusion | FR | Frankreichs größter Yachtausrüster | accastillage-diffusion.com |
| Force 4 | FR | Yachtausrüster, Frankreich | force4.fr |
| Marine Warehouse | UK | Online-Yachtausrüster, UK | marinewarehouse.co.uk |
| LFS Marine | UK | Beschlag-Spezialist | lfsmarine.com |
| West Marine | USA | Größter US-Yachtausrüster | westmarine.com |
| Defender Marine | USA | Günstiger Online-Händler | defender.com |
| Budget Marine | Karibik | Karibik-weit, Filialnetz | budgetmarine.com |
| Whitworths | AUS | Australiens Yachtausrüster | whitworths.com.au |
| Burnsco | NZ | Neuseeland-Yachtausrüster | burnsco.co.nz |

### R.7 Vergleich: Gesamtkosten verschiedener Wartungsstrategien über 20 Jahre

Die nachfolgende Tabelle vergleicht drei Wartungsstrategien für eine typische 12m-Segelyacht mit 25 Blöcken über einen Zeitraum von 20 Jahren im Salzwasser-Einsatz:

**Strategie A: Professionelle präventive Wartung**
| Posten | Häufigkeit | Kosten/Ereignis | 20-Jahres-Kosten |
|--------|-----------|----------------|-----------------|
| Schmiermittel | 4×/Jahr | 25 € | 2.000 € |
| Inspektionsmaterial | 1×/Jahr | 30 € | 600 € |
| Lagersätze (5 pro Durchgang) | Alle 3 Jahre | 350 € | 2.100 € |
| Scheibentausch (3 pro Durchgang) | Alle 6 Jahre | 150 € | 450 € |
| Achstausch (2 pro Durchgang) | Alle 8 Jahre | 60 € | 120 € |
| Komplett-Blockersatz (3 Blöcke) | Alle 10 Jahre | 450 € | 900 € |
| Werkzeug (Erstanschaffung + Ersatz) | — | — | 250 € |
| Folgeschäden (Tauwerk, Rigg) | — | — | 0–200 € |
| **Gesamtkosten Strategie A** | | | **6.420–6.620 €** |

**Strategie B: Moderate Wartung (nur jährlich)**
| Posten | Häufigkeit | Kosten/Ereignis | 20-Jahres-Kosten |
|--------|-----------|----------------|-----------------|
| Schmiermittel | 1×/Jahr | 25 € | 500 € |
| Lagersätze (8 pro Durchgang) | Alle 4 Jahre | 560 € | 2.240 € |
| Scheibentausch (5 pro Durchgang) | Alle 5 Jahre | 250 € | 1.000 € |
| Achstausch (3 pro Durchgang) | Alle 6 Jahre | 90 € | 270 € |
| Komplett-Blockersatz (5 Blöcke) | Alle 8 Jahre | 750 € | 1.500 € |
| Notfallreparaturen | 2 in 20 Jahren | 500 € | 1.000 € |
| Folgeschäden (Tauwerk, Rigg) | — | — | 800–2.000 € |
| **Gesamtkosten Strategie B** | | | **7.310–8.510 €** |

**Strategie C: Keine Wartung (nur Austausch bei Ausfall)**
| Posten | Häufigkeit | Kosten/Ereignis | 20-Jahres-Kosten |
|--------|-----------|----------------|-----------------|
| Komplett-Blockersatz | Alle 5–7 Jahre | 3.000–5.000 € | 8.000–15.000 € |
| Notfallreparaturen auf See | 5 in 20 Jahren | 300–1.500 € | 1.500–7.500 € |
| Folgeschäden (Tauwerk, Segel, Rigg) | — | — | 2.000–8.000 € |
| Charterausfall / Regatta-Disqualifikation | — | — | 0–5.000 € |
| **Gesamtkosten Strategie C** | | | **11.500–35.500 €** |

**Fazit:** Die professionelle präventive Wartung (Strategie A) ist langfristig die mit Abstand günstigste Option. Die Einsparung gegenüber Vernachlässigung (Strategie C) beträgt über 20 Jahre typischerweise 5.000–29.000 €.

### R.8 Klimaregion-spezifische Besonderheiten

#### R.8.1 Arktische/Subarktische Reviere (Norwegen, Island, Grönland)

**Besondere Herausforderungen:**
- Temperaturen unter 0°C: Schmiermittel verdicken, Polymere verspröden
- Eisbildung in Lagern nach Süßwasserspülung bei Frost
- Kurze Segelsaison, aber extreme Bedingungen

**Empfehlungen:**
- Kältefeste Schmiermittel verwenden (McLube Sailkote funktioniert bis -30°C)
- Nach Süßwasserspülung: Blöcke sofort trocknen (Druckluft) und nachschmieren
- Scheiben aus PEEK oder Torlon bevorzugen (weniger kälteempfindlich als Acetal)
- Im Hafen bei Frost: Blöcke mit Handwärme oder Fön leicht erwärmen vor Auslaufen
- Winterlager: Blöcke demontieren und in temperiertem Raum lagern

#### R.8.2 Subtropische Reviere mit hoher Luftfeuchtigkeit (Hongkong, Singapur)

**Besondere Herausforderungen:**
- Permanente Luftfeuchtigkeit >80 % fördert Korrosion auch ohne direkte Wasserexposition
- Schimmelbildung auf organischen Schmiermitteln möglich
- Hohe Temperaturen beschleunigen alle chemischen Prozesse

**Empfehlungen:**
- Synthetiköle verwenden (nicht pflanzlich/tierisch basiert)
- Korrosionsschutz (Boeshield T-9) als zusätzliche Barriere
- Schmierintervalle auf 6 Wochen verkürzen
- Silikatgel-Beutel in Aufbewahrungsboxen für Ersatzteile
- Belüftung der Blockstauräume sicherstellen

#### R.8.3 Gezeitenreviere mit starker Verschlickung (Wattenmeer, Themse)

**Besondere Herausforderungen:**
- Schlick und Feinsand dringen in alle Mechanismen ein
- Trockenfallen bedeutet Exposition gegenüber Schlickpartikel
- Extreme Tidal Range = extreme Beanspruchung der Befestigungen

**Empfehlungen:**
- Süßwasserspülung nach jedem Trockenfallen (nicht nur nach Salzwasser!)
- Blöcke mit Abdeckungen schützen beim Trockenfallen
- Schmierintervalle auf 4 Wochen verkürzen
- Snatchblöcke besonders schützen (Schlick im Mechanismus)
- Bei Routineinspektion: Schlickrückstände in Lagern als Priorität behandeln

### R.9 Spezialthema: Blöcke für High-Modulus-Tauwerk

**Problemstellung:**
Modernes High-Modulus-Tauwerk (Dyneema SK78/SK99, Vectran, PBO, Zylon) hat andere Laufeigenschaften als traditionelles Polyester-Tauwerk und beansprucht Scheiben anders.

**Scheibenverschleiß durch High-Modulus-Tauwerk:**

| Tauwerk | Scheibenverschleiß vs. Polyester | Selbstverschleiß | Empfohlene Scheibe |
|---------|--------------------------------|------------------|-------------------|
| Polyester (Referenz) | 1,0× | Niedrig | Alle Materialien |
| Dyneema SK78 | 2,0–3,0× | Niedrig | Keramik, PEEK, Composite |
| Dyneema SK99 | 2,5–3,5× | Niedrig | Keramik, PEEK |
| Vectran | 1,5–2,0× | Mittel | Aluminium hart-elox., PEEK |
| PBO (Zylon) | 1,5–2,5× | Hoch (UV!) | Aluminium hart-elox., Edelstahl |
| Technora | 1,5–2,0× | Niedrig | Alle Materialien |
| Aramid (Kevlar) | 1,5–2,0× | Mittel (UV, Biegung) | Große Scheiben, Aluminium |

**Wartungskonsequenzen:**
- Bei Dyneema-Tauwerk: Scheibeninspektions-Intervall halbieren
- Rillentiefe häufiger messen (vierteljährlich statt jährlich)
- Scheiben aus härterer Legierung oder mit Keramikbeschichtung erwägen
- Tauwerk-Block-Kombination bei Neukonfiguration sorgfältig abstimmen
- Scheibendurchmesser nicht unter dem vom Tauwerkhersteller empfohlenen Minimum

**Minimaler Scheibendurchmesser nach Tauwerk:**

| Tauwerk-Kern | Min. Scheiben-Ø (Dauerbetrieb) | Min. Scheiben-Ø (Gelegentlich) |
|-------------|-------------------------------|-------------------------------|
| Polyester | 6 × Tauwerk-Ø | 4 × Tauwerk-Ø |
| Dyneema | 8 × Tauwerk-Ø | 5 × Tauwerk-Ø |
| Vectran | 8 × Tauwerk-Ø | 5 × Tauwerk-Ø |
| PBO | 10 × Tauwerk-Ø | 6 × Tauwerk-Ø |
| Aramid | 10 × Tauwerk-Ø | 6 × Tauwerk-Ø |
| Stahldraht | 12 × Tauwerk-Ø | 8 × Tauwerk-Ø |

### R.10 Checkliste: Blocksystem-Neuplanung bei Refit

Bei einem Refit bietet sich die Gelegenheit, das gesamte Blocksystem zu überdenken:

| Nr. | Prüfpunkt | Erledigt |
|-----|----------|---------|
| 1 | Bestandsaufnahme aller vorhandenen Blöcke (Position, Typ, Zustand) | ☐ |
| 2 | Lastanalyse für jede Position (aktuelles Segel-/Riggplan) | ☐ |
| 3 | Tauwerk-Durchmesser für jede Anwendung bestimmen | ☐ |
| 4 | Scheibendurchmesser passend zum Tauwerk auswählen | ☐ |
| 5 | Lagertyp nach Einsatzart wählen (Kugel/Nadel/Gleit) | ☐ |
| 6 | Herstellereinheitlichkeit anstreben (Ersatzteilvereinfachung) | ☐ |
| 7 | Befestigungsart und Backing Plates planen | ☐ |
| 8 | Reibung im Gesamtsystem berechnen (Wirkungsgrad-Kette) | ☐ |
| 9 | Wartungszugänglichkeit bei Blockpositionierung beachten | ☐ |
| 10 | Reserveblöcke beschaffen (passend zum neuen System) | ☐ |
| 11 | Wartungsplan für neues System erstellen | ☐ |
| 12 | Digitales Block-Inventar anlegen (Block-ID, Modell, Einbaudatum) | ☐ |
| 13 | Alle Befestigungen mit korrektem Drehmoment anziehen | ☐ |
| 14 | Alle Blöcke geschmiert und funktionsgeprüft | ☐ |
| 15 | Erstfotos für Dokumentation gemacht | ☐ |

### R.11 Wirkungsgrad-Berechnung für Blocksysteme

Der Gesamtwirkungsgrad eines Flaschenzugsystems hängt vom Wirkungsgrad jedes einzelnen Blocks ab:

**Blockwirkungsgrade (Confidence: benchmark):**

| Blocktyp / Zustand | Wirkungsgrad pro Umlenkung |
|--------------------|---------------------------|
| Kugellagerblock, neu, geschmiert | 96–98 % |
| Kugellagerblock, gewartet | 93–96 % |
| Kugellagerblock, vernachlässigt | 80–90 % |
| Kugellagerblock, schwergängig | 60–80 % |
| Nadellagerblock, neu, geschmiert | 94–97 % |
| Gleitlagerblock, neu | 88–93 % |
| Gleitlagerblock, vernachlässigt | 70–85 % |
| Festsitzender Block | 30–50 % |

**Systemwirkungsgrad-Berechnung:**
η_system = η_1 × η_2 × η_3 × ... × η_n

**Beispiel: 6:1 Großschot-System mit 5 Umlenkungen:**

| Blockzustand | η pro Block | η System | Kraft für 100 kg Last |
|-------------|-----------|----------|----------------------|
| Alle neu (98%) | 0,98 | 0,90 (90%) | 18,5 kg |
| Alle gewartet (95%) | 0,95 | 0,77 (77%) | 21,6 kg |
| Alle vernachlässigt (85%) | 0,85 | 0,44 (44%) | 37,9 kg |
| Gemischt (1 schlecht) | 0,70–0,98 | 0,63 (63%) | 26,4 kg |

**Fazit:** Ein einzelner schwergängiger Block in einem 6:1-System kann die Trimmkraft um über 40 % erhöhen. Regelmäßige Wartung ALLER Blöcke ist entscheidend für den Systemwirkungsgrad.

### R.12 Blocktausch-Kompatibilitätsmatrix

Bei Ersatzbedarf stellt sich die Frage der Kompatibilität zwischen Herstellern. Die folgende Matrix gibt eine Orientierung:

**Mechanische Kompatibilität (Befestigungssystem):**

| Von \ Nach | Harken | Lewmar | Ronstan | Antal |
|-----------|--------|--------|---------|-------|
| Harken | ✓ | ✗ | ✗ | ✗ |
| Lewmar | ✗ | ✓ | ✗ | ✗ |
| Ronstan | ✗ | ✗ | ✓ | ✗ |
| Antal | ✗ | ✗ | ✗ | ✓ |

**Hinweis:** Blöcke verschiedener Hersteller sind in der Regel NICHT direkt austauschbar. Befestigungsbohrungen, Schäkelmaße und Achsdimensionen unterscheiden sich. Beim Herstellerwechsel müssen ggf. neue Bohrungen gesetzt werden.

**Funktionale Kompatibilität (gleiche Leistungsklasse):**

| Harken | Lewmar | Ronstan | Antal | SWL ca. |
|--------|--------|---------|-------|---------|
| Micro | Size 0 | Series 15 | V20 | 200 kg |
| 29mm | Size 1 | Series 20 | V25 | 400 kg |
| 40mm | Size 2 | Series 30 | V30 | 750 kg |
| 57mm | Size 3 | Series 40 | V40 | 1.500 kg |
| 75mm | Size 4 | Series 55 | V55 | 3.000 kg |
| 100mm | Size 5 | Series 75 | V75 | 5.000 kg |

Diese Zuordnung ist approximativ — SWL und Scheibendurchmesser variieren innerhalb der Serien.

---

> **Ende der Wissensdatei 10.05**
> Erstellt: 2026-04-25 | AYDI Research
> Nächste Überprüfung: 2026-10-25
