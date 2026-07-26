---
titel: "Snubber, Kettenstopper und Ruckdämpfer"
kategorie: "Anker und Kette"
unterkategorie: "Snubber und Kettenstopper"
version: "2.0"
letzte_aktualisierung: "2026-04"
autor: "AYDI Maritime Knowledge Base"
---

# 17_05 — Snubber, Kettenstopper und Ruckdämpfer

---

## Inhaltsverzeichnis

1. [Einführung](#1-einführung)
2. [Snubber — Grundlagen und Physik](#2-snubber--grundlagen-und-physik)
3. [Snubber-Materialien](#3-snubber-materialien)
4. [Dimensionierung](#4-dimensionierung)
5. [Kettenhaken (Chain Hooks)](#5-kettenhaken-chain-hooks)
6. [Kettenstopper und Devil's Claw](#6-kettenstopper-und-devils-claw)
7. [Ruckdämpfer und Mooring-Kompensatoren](#7-ruckdämpfer-und-mooring-kompensatoren)
8. [Bridle-Systeme für Katamarane](#8-bridle-systeme-für-katamarane)
9. [Kellet und Ankergewicht (Sentinel)](#9-kellet-und-ankergewicht-sentinel)
10. [Installation und Befestigung](#10-installation-und-befestigung)
11. [Nacht-Ankern Routine](#11-nacht-ankern-routine)
12. [Fehlerbild-Atlas](#12-fehlerbild-atlas)
13. [Troubleshooting](#13-troubleshooting)
14. [Entscheidungshilfe](#14-entscheidungshilfe)
15. [FAQ](#15-faq)
16. [Glossar](#16-glossar)
17. [Schnell-Referenz](#17-schnell-referenz)
18. [ANHANG A–H: Fallstudien](#18-anhang-ah-fallstudien)
19. [ANHANG I–R: Pydantic v2 Datenmodelle](#19-anhang-ir-pydantic-v2-datenmodelle)

---
---

## 1. Einführung

### 1.1 Warum ein Snubber unverzichtbar ist

Der Snubber (auch Ruckdämpfer, Ankerfeder oder Nylon-Vorleine genannt) gehört
zu den am meisten unterschätzten Ausrüstungsgegenständen auf einer Yacht. Er
erfüllt gleich mehrere kritische Funktionen, die das gesamte Ankersystem
schützen und den Komfort an Bord erheblich verbessern.

**Die vier Kernfunktionen eines Snubbers:**

1. **Windenschutz (Windlass Protection)**
   Die Ankerwinde ist ein mechanisches Gerät, das zum Aufholen und Fieren
   der Kette konstruiert ist — nicht zum Halten des Bootes bei Zugbelastung.
   Liegt die gesamte Ankerlast auf der Winde, werden Getriebe, Welle und
   Befestigung extrem beansprucht. Windenhersteller wie Lewmar, Quick und
   Lofrans weisen ausdrücklich darauf hin, dass die Kette niemals dauerhaft
   über die Winde belastet werden darf.

   - **Lewmar**: „Verwenden Sie stets einen Kettenstopper oder Snubber,
     um die Ankerlast von der Winde zu nehmen."
   - **Quick**: „Die Winde ist ein Arbeitsgerät, kein Haltepunkt."
   - **Lofrans**: Garantieausschluss bei nachweislicher Dauerbelastung.

2. **Stoßdämpfung (Shock Absorption)**
   In Böen und bei Seegang entstehen dynamische Lasten, die das Vielfache
   der statischen Windlast betragen können. Eine Stahlkette ist praktisch
   unelastisch — die gesamte kinetische Energie des Bootes wird in einem
   kurzen, harten Ruck auf Anker, Kette und Bugbeschläge übertragen.
   Ein Nylon-Snubber dehnt sich um 15–35 % seiner Länge und wandelt die
   Stoßenergie in Wärme um (viskoelastische Dämpfung).

   Dynamische Lastberechnung ohne Snubber:
   ```
   F_peak = m × v² / (2 × s_chain)
   m = Bootsmasse (z. B. 12.000 kg)
   v = Rückfallgeschwindigkeit (z. B. 1,5 m/s bei Böe)
   s_chain = Federweg Kette (ca. 0,01 m bei 50 m Kette)
   F_peak = 12.000 × 1,5² / (2 × 0,01) = 1.350.000 N ≈ 135 t
   ```

   Mit 8-m-Nylon-Snubber (30 % Dehnung):
   ```
   s_snubber = 8 m × 0,30 = 2,4 m
   F_peak = 12.000 × 1,5² / (2 × 2,4) = 5.625 N ≈ 0,57 t
   ```

   Der Unterschied beträgt den Faktor 240 — dies verdeutlicht die enorme
   Bedeutung des Snubbers als Sicherheitselement.

3. **Geräuschreduktion (Noise Reduction)**
   Eine unter Last stehende Ankerkette überträgt jede Wellenbewegung als
   metallisches Rasseln und Klirren über den Bugbeschlag in den Rumpf.
   In einer ruhigen Ankerbucht kann dieses Geräusch den Schlaf nachhaltig
   stören. Der Snubber entkoppelt das Boot von der Kette und eliminiert
   diese Geräuschübertragung fast vollständig.

   Typische Geräuschpegel:
   - Ohne Snubber bei leichtem Seegang: 55–65 dB in der Bugkabine
   - Mit Snubber: 30–40 dB — Reduktion um 20–30 dB

4. **Kettenkatarakt-Verbesserung (Catenary Enhancement)**
   Ein Snubber mit einigen Metern Länge fügt dem Ankersystem einen
   elastischen Abschnitt hinzu, der bei zunehmender Last nachgibt und so
   den Abgangswinkel am Anker flacher hält. Dies verbessert die Haltekraft
   des Ankers, da der horizontale Zug am Anker maximiert und der vertikale
   Hubanteil minimiert wird.

### 1.2 Die versteckte Gefahr: Ermüdungsbrüche

Boote, die regelmäßig ohne Snubber vor Anker liegen, zeigen nach wenigen
Saisons typische Schäden:

- **Windengetriebe-Verschleiß**: Spiel in den Zahnrädern, Getriebeöl
  verfärbt sich metallisch. Reparaturkosten: 800–2.500 EUR.
- **Bugrolle-Verformung**: Die Bugrolle wird durch die permanente
  Ketten-Reibung oval. Austausch: 200–600 EUR.
- **Kettenkasten-Risse**: Die Stoßbelastung überträgt sich auf die
  Kastenbefestigung im Rumpf. Strukturelle Reparatur: 1.500–5.000 EUR.
- **Bugbeschlag-Ausriss**: Im schlimmsten Fall löst sich der gesamte
  Bugbeschlag aus dem Deck. Katastrophales Versagen.

### 1.3 Historischer Hintergrund

In der traditionellen Seefahrt war der Snubber nicht nötig — Segelschiffe
ankerten mit Ankertau (Nylon/Hanf), das von Natur aus elastisch war. Erst
mit der Verbreitung von Vollketten-Ankersystemen in den 1960er/70er Jahren
wurde der Snubber als separates Bauteil notwendig.

Der Begriff „Snubber" stammt vom englischen „to snub" — „abfangen" oder
„bremsen". Im deutschen Sprachraum sind die Bezeichnungen uneinheitlich:

- **Snubber** — international gebräuchlich, zunehmend auch im Deutschen
- **Ruckdämpfer** — technisch korrekt, betont die Dämpfungsfunktion
- **Ankerfeder** — betont die elastische Komponente
- **Vorleine** — traditioneller Begriff, eher im Binnenbereich
- **Ankerleinenstück** — formelle deutsche Bezeichnung

### 1.4 Kosten-Nutzen-Analyse

Die Investition in ein Snubber-System ist eine der wirtschaftlichsten
Sicherheitsmaßnahmen auf einer Yacht. Eine Gegenüberstellung:

**Kosten eines Snubber-Systems (12-m-Boot):**
- Snubber 16 mm × 8 m: ca. 50 EUR
- Kettenhaken: ca. 99 EUR
- Schamfilschutz: ca. 15 EUR
- Installation: 0 EUR (Eigenleistung)
- **Gesamt: ca. 164 EUR**

**Potenzielle Schäden ohne Snubber (über 5 Jahre):**
- Windengetriebe-Reparatur: 1.500–2.500 EUR
- Bugrolle-Austausch: 200–600 EUR
- Bugbeschlag-Reparatur: 500–2.000 EUR
- Kettenkasten-Strukturreparatur: 1.500–5.000 EUR
- Schlafstörungen, Komfortverlust: nicht bezifferbar
- **Potenzielle Gesamtschäden: 3.700–10.100 EUR**

**Return on Investment (ROI):**
```
ROI = (Vermiedene Schäden - Investition) / Investition × 100
ROI = (6.900 - 164) / 164 × 100 = 4.107 %
```

Selbst bei konservativster Betrachtung (nur Getriebeschaden) beträgt
der ROI über 800 %. Ein Snubber-System gehört damit zu den
wirtschaftlichsten Investitionen an Bord.

### 1.5 Regelwerk und Normen

Für Snubber und Kettenstopper gibt es keine dedizierte ISO-Norm. Relevante
Normen und Richtlinien:

| Regelwerk | Relevanz |
|-----------|----------|
| ISO 15083 (2003) | Bilge-Pump-Systeme — enthält Anforderungen an Kettenkästen |
| ABYC H-40 | Ankersysteme — empfiehlt Snubber für alle Kettenanker-Systeme |
| GL/DNV Rules for Yachts | Ankersystem-Dimensionierung, keine Snubber-Spezifikation |
| ISAF OSR (2024) | Offshore-Regeln erwähnen Snubber nicht explizit |
| CE/RCD 2013/53/EU | Keine Snubber-Anforderung, aber Ankersystem muss „sicher" sein |

Die ABYC-Empfehlung H-40 ist die detaillierteste verfügbare Richtlinie:
- Snubber-Durchmesser mindestens Kettendurchmesser × 2,5
- Snubber-Länge mindestens 5 × Bootslänge in Fuß (in Zoll) — ca. 3–5 m
- Bruchlast des Snubbers ≥ 3 × maximale Windlast bei 42 kn

---
---

## 2. Snubber — Grundlagen und Physik

### 2.1 Funktionsprinzip

Ein Snubber besteht aus einem elastischen Seil (typisch Nylon), das an
einem Ende am Bugbeschlag oder an einer Klampe befestigt ist und am
anderen Ende über einen Kettenhaken (Chain Hook) an der Ankerkette
eingehängt wird. Die Kette wird dann so weit nachgefiert, dass sie
einen Durchhang bildet und der Snubber die gesamte Last übernimmt.

**Schematische Darstellung:**

```
         ┌─────────────────────────────────────────┐
         │  BOOT                                    │
         │                                          │
    ┌────┤ Bugklampe                                │
    │    │                                          │
    │    └─────────────────────────────────────────┘
    │
    │  Snubber (Nylon, elastisch)
    │  Länge: 5–12 m
    │  Dehnung: 15–35 %
    │
    ├──── Kettenhaken (Chain Hook)
    │
    │  Kette (Durchhang/Slack)
    │  ca. 2–4 m Durchhang
    │
    ┆  Ankerkette (unter Wasser)
    ┆  Gesamtlänge: 40–100 m
    ┆
    ⚓ Anker (am Grund)
```

### 2.2 Physik der Stoßdämpfung

Die Energieabsorption eines Snubbers basiert auf der viskoelastischen
Eigenschaft von Nylon. Beim Dehnen wird kinetische Energie in Wärme
umgewandelt (Hysterese-Effekt).

**Energieabsorptionskapazität:**

```
E_abs = ∫₀^ε_max F(ε) × L₀ × dε

Für Nylon 3-strand (näherungsweise linear bis 20 % Dehnung):
E_abs ≈ 0,5 × F_max × ε_max × L₀

Beispiel für 14 mm Nylon, 8 m Länge:
F_max bei 20 % Dehnung: ca. 8.000 N
E_abs = 0,5 × 8.000 × 0,20 × 8 = 6.400 J

Vergleich: Kinetische Energie eines 10-t-Bootes bei 1 m/s:
E_kin = 0,5 × 10.000 × 1² = 5.000 J

→ Der Snubber kann die gesamte Stoßenergie absorbieren.
```

**Resonanzfrequenz:**

Das Boot-Snubber-System hat eine Eigenfrequenz:
```
f₀ = 1/(2π) × √(k/m)

k = Federsteifigkeit des Snubbers [N/m]
m = Bootsmasse [kg]

Beispiel: k = 5.000 N/m, m = 10.000 kg:
f₀ = 1/(2π) × √(5.000/10.000) = 0,112 Hz → T = 8,9 s

Typische Wellenperioden: 3–8 s
→ Eigenfrequenz liegt knapp über dem Wellenspektrum
→ Keine Resonanzgefahr bei normalen Bedingungen
```

### 2.3 Statische vs. dynamische Belastung

| Bedingung | Statische Last | Dynamischer Faktor | Effektive Last |
|-----------|---------------|-------------------|----------------|
| Leichte Brise (10 kn) | 200 N | 1,2 | 240 N |
| Mäßiger Wind (20 kn) | 800 N | 1,5 | 1.200 N |
| Starker Wind (30 kn) | 1.800 N | 2,0 | 3.600 N |
| Sturm (40 kn) | 3.200 N | 2,5 | 8.000 N |
| Schwerer Sturm (50 kn) | 5.000 N | 3,0 | 15.000 N |
| Orkan (60 kn) | 7.200 N | 3,5 | 25.200 N |

*Werte für ein typisches 12-m-Segelboot (ca. 10 t Verdrängung)*

Der dynamische Faktor berücksichtigt Böen, Seegang und das Rückschwingen
des Bootes am Anker. Ohne Snubber kann der dynamische Faktor auf 5–10
ansteigen, da die Kette die Energie nicht absorbiert.

### 2.4 Kraftübertragung im Ankersystem

```
Windkraft + Strömungskraft + Wellenkraft
            ↓
       Bugbeschlag/Klampe
            ↓
       Snubber (Dehnung → Dämpfung)
            ↓
       Kettenhaken
            ↓
       Ankerkette (Kanar → Gewichtsdämpfung)
            ↓
       Wirbelschäkel
            ↓
       Anker (Haltekraft im Grund)
```

Jede Komponente in dieser Kette muss für die maximale dynamische Last
dimensioniert sein. Die schwächste Komponente bestimmt die Gesamtfestigkeit.

### 2.5 Temperatureinfluss auf Nylon

Nylon ist temperaturempfindlich — die Elastizität ändert sich mit der
Temperatur:

| Temperatur | Relative Elastizität | Bruchlast (relativ) |
|-----------|---------------------|---------------------|
| 0 °C | 70 % | 110 % |
| 10 °C | 85 % | 105 % |
| 20 °C | 100 % (Referenz) | 100 % |
| 30 °C | 115 % | 95 % |
| 40 °C | 130 % | 90 % |

In kaltem Wasser (Skandinavien, Nachtankern) ist der Snubber steifer und
absorbiert weniger Energie. In diesen Bedingungen sollte ein längerer
Snubber verwendet oder der Durchmesser vergrößert werden.

### 2.6 UV-Degradation von Nylon

Nylon ist UV-empfindlich. Im Mittelmeer-Sommer (hohe UV-Belastung)
verliert ein ungeschützter Nylon-Snubber pro Saison ca. 10–15 % seiner
Bruchlast. Schutzmaßnahmen:

1. **UV-Schutzhülle (Chafe Guard)**: Reduziert UV-Einwirkung um 80 %
2. **Dunkle Farben**: Schwarz/navy absorbieren UV besser, werden aber heißer
3. **Lagerung**: Bei Nichtgebrauch im Kettenkasten oder unter Deck
4. **Austauschintervall**: Alle 3–5 Jahre, bei sichtbarer Faserung sofort

---
---

## 3. Snubber-Materialien

### 3.1 Nylon 3-Strand (Dreischlag)

**Eigenschaften:**
- **Material**: Polyamid 6.6 (PA 6.6)
- **Dehnung unter Last**: 15–25 % bei 30 % Bruchlast
- **Bruchlast**: ca. 2.200–22.000 N (je nach Durchmesser)
- **Energieabsorption**: Hervorragend — bester Wert aller gängigen Seile
- **Lebensdauer**: 3–5 Jahre bei regelmäßiger Nutzung
- **Preis**: Günstig — 2–6 EUR/m

**Vorteile:**
- Höchste Energieabsorption aller Snubber-Materialien
- Einfach zu spleißen (Augspleiß, Rückspleiß)
- Günstig in der Anschaffung
- Bewährte Technik, seit Jahrzehnten Standard
- Gute Knotenfestigkeit

**Nachteile:**
- UV-empfindlich (10–15 % Festigkeitsverlust pro Saison)
- Wasseraufnahme 4–8 % → Gewichtszunahme, leichter Steifigkeitsverlust
- Schrumpft beim Trocknen nach Nassbelastung
- Kann sich bei dauerhafter Belastung „setzen" (bleibende Verformung)
- Scheuert relativ leicht an Bugbeschlägen

**Typische Produkte:**

| Hersteller | Produkt | Durchmesser | Bruchlast | Preis/m |
|-----------|---------|-------------|-----------|---------|
| Liros | Anchor Nylon | 12 mm | 15.800 N | 3,20 EUR |
| Liros | Anchor Nylon | 14 mm | 21.200 N | 4,10 EUR |
| Liros | Anchor Nylon | 16 mm | 27.500 N | 5,40 EUR |
| Marlow | Anchor Line | 12 mm | 14.900 N | 3,80 EUR |
| Marlow | Anchor Line | 14 mm | 20.300 N | 4,90 EUR |
| Marlow | Anchor Line | 16 mm | 26.800 N | 6,20 EUR |
| Gleistein | Anchor Warp | 12 mm | 15.200 N | 3,50 EUR |
| Gleistein | Anchor Warp | 14 mm | 20.600 N | 4,30 EUR |
| Gleistein | Anchor Warp | 16 mm | 27.000 N | 5,60 EUR |
| New England Ropes | 3-Strand Nylon | 14 mm | 21.800 N | 5,20 EUR |
| Yale Cordage | Premium 3-Strand | 14 mm | 22.100 N | 5,50 EUR |

### 3.2 Nylon 8-Plait (Achtfach-Geflecht)

**Eigenschaften:**
- **Material**: Polyamid 6.6 (PA 6.6), geflochten
- **Dehnung unter Last**: 12–20 % bei 30 % Bruchlast
- **Bruchlast**: ca. 10 % niedriger als 3-Strand gleichen Durchmessers
- **Energieabsorption**: Sehr gut — etwas geringer als 3-Strand
- **Lebensdauer**: 4–6 Jahre
- **Preis**: 20–30 % teurer als 3-Strand

**Vorteile:**
- Kein Kinking (Kinkenbildung) — bleibt formstabil
- Lässt sich gut auf der Bugrolle führen
- Etwas abriebfester als 3-Strand
- Spleißbar (spezieller Achtergeflecht-Spleiß)
- Besseres Handling als 3-Strand

**Nachteile:**
- Etwas geringere Dehnung als 3-Strand
- Teurer in der Anschaffung
- Spleiß aufwändiger als bei 3-Strand
- Gleiche UV-Empfindlichkeit wie 3-Strand

**Typische Produkte:**

| Hersteller | Produkt | Durchmesser | Bruchlast | Preis/m |
|-----------|---------|-------------|-----------|---------|
| Liros | Multifil 8-Plait | 14 mm | 18.700 N | 5,20 EUR |
| Liros | Multifil 8-Plait | 16 mm | 24.500 N | 6,80 EUR |
| Marlow | Anchor 8-Plait | 14 mm | 18.200 N | 5,80 EUR |
| Marlow | Anchor 8-Plait | 16 mm | 24.100 N | 7,20 EUR |
| Gleistein | Octoplait | 14 mm | 18.900 N | 5,40 EUR |
| New England Ropes | 8-Plait Anchor | 14 mm | 19.300 N | 6,10 EUR |

### 3.3 Dyneema-Nylon-Hybrid mit Gummielement

**Eigenschaften:**
- **Aufbau**: Dyneema (HMPE) Leine mit eingespleißtem Gummi-Dämpfer
- **Dehnung**: 20–40 % im Gummielement, <1 % in der Dyneema-Leine
- **Bruchlast**: Abhängig vom Gummielement (typisch 3.000–15.000 N)
- **Energieabsorption**: Gut — konzentriert auf das Gummielement
- **Lebensdauer**: 5–8 Jahre (Dyneema ist UV-resistent)
- **Preis**: 80–250 EUR pro Einheit

**Vorteile:**
- Sehr UV-beständig (Dyneema hat keine UV-Degradation)
- Kompakter als Nylon-Snubber
- Definierte Dämpfungscharakteristik
- Kein Wasseraufnahme-Problem

**Nachteile:**
- Teuer in der Anschaffung
- Gummielement kann bei extremer Belastung versagen
- Nicht reparierbar — bei Defekt komplett austauschen
- Begrenzte Größenauswahl

**Typische Produkte:**

| Hersteller | Produkt | Für Boote | Bruchlast | Preis |
|-----------|---------|-----------|-----------|-------|
| Wichard | Snubber Gypsea | 8–12 m | 8.000 N | 89 EUR |
| Wichard | Snubber Gypsea | 12–16 m | 12.000 N | 119 EUR |
| Wichard | Snubber Gypsea | 16–20 m | 16.000 N | 159 EUR |
| Unimer | Mooring Compensator | 8–12 m | 7.000 N | 95 EUR |
| Unimer | Mooring Compensator | 12–16 m | 11.500 N | 135 EUR |
| Unimer | Mooring Compensator | 16–20 m | 15.000 N | 175 EUR |
| Eval | Snubber EQ | 10–15 m | 10.000 N | 110 EUR |

### 3.4 Bungee-Cord (Gummiseil)

**Eigenschaften:**
- **Material**: Latex/Naturkautschuk-Kern mit Textilumantelung
- **Dehnung**: 50–100 % (sehr hoch)
- **Bruchlast**: Gering (typisch 500–3.000 N)
- **Energieabsorption**: Mäßig — federt eher als dämpft
- **Lebensdauer**: 1–3 Jahre
- **Preis**: 3–8 EUR/m

**Vorteile:**
- Sehr hohe Dehnung
- Günstig
- Leicht und kompakt

**Nachteile:**
- Geringe Bruchlast — niemals als alleiniger Snubber verwenden
- Keine viskoelastische Dämpfung — gibt Energie zurück (Federeffekt)
- UV-empfindlich, altert schnell
- Gummi-Kern kann brechen ohne äußerlich sichtbar zu sein

**Einsatz:** Nur als Zusatzdämpfer in Kombination mit Nylon-Snubber oder
an Mooringleinen. Für Ankersysteme allein nicht geeignet.

### 3.5 Polyester (Dacron)

**Hinweis:** Polyester ist als Snubber-Material ungeeignet, da die Dehnung
nur 3–5 % beträgt. Polyester wird manchmal irrtümlich als Snubber
verkauft, bietet aber praktisch keine Stoßdämpfung.

| Eigenschaft | Nylon | Polyester |
|------------|-------|-----------|
| Dehnung bei 30 % BL | 15–25 % | 3–5 % |
| Energieabsorption | Hervorragend | Minimal |
| UV-Beständigkeit | Mäßig | Gut |
| Wasseraufnahme | 4–8 % | <1 % |
| Snubber-Eignung | ★★★★★ | ★☆☆☆☆ |

### 3.6 Materialvergleich — Zusammenfassung

| Kriterium | Nylon 3-Strand | Nylon 8-Plait | Dyneema/Gummi | Bungee |
|-----------|---------------|--------------|---------------|--------|
| Dehnung | ★★★★★ | ★★★★☆ | ★★★☆☆ | ★★★★★ |
| Bruchlast | ★★★★☆ | ★★★★☆ | ★★★☆☆ | ★☆☆☆☆ |
| UV-Resistenz | ★★☆☆☆ | ★★☆☆☆ | ★★★★★ | ★☆☆☆☆ |
| Abriebfestigkeit | ★★★☆☆ | ★★★★☆ | ★★★★★ | ★★☆☆☆ |
| Lebensdauer | ★★★☆☆ | ★★★★☆ | ★★★★★ | ★★☆☆☆ |
| Preis | ★★★★★ | ★★★★☆ | ★★☆☆☆ | ★★★★★ |
| Energiedämpfung | ★★★★★ | ★★★★☆ | ★★★★☆ | ★★☆☆☆ |
| Handling | ★★★☆☆ | ★★★★☆ | ★★★★★ | ★★★☆☆ |

**Empfehlung nach Bootstyp:**

- **Fahrtensegler 8–12 m**: Nylon 3-Strand 14 mm — bestes Preis-Leistungs-Verhältnis
- **Fahrtensegler 12–16 m**: Nylon 3-Strand 16 mm oder 8-Plait 16 mm
- **Blauwasser-Yacht 12–18 m**: Zwei Snubber: Nylon 3-Strand 18 mm + Reserve
- **Motoryacht 10–16 m**: Dyneema/Gummi oder Nylon 8-Plait 14 mm
- **Katamaran 10–14 m**: Bridle-System mit 2× Nylon 3-Strand 14 mm
- **Katamaran 14–18 m**: Bridle-System mit 2× Nylon 3-Strand 16–18 mm

---
---

## 4. Dimensionierung

### 4.1 Snubber-Durchmesser nach Bootsgröße

Die Dimensionierung des Snubbers richtet sich nach der Bootsgröße,
dem Bootstyp und den erwarteten Bedingungen. Grundregel:

```
Snubber-Durchmesser [mm] ≥ Kettendurchmesser [mm] × 2,5
```

**Dimensionierungstabelle:**

| Bootslänge | Verdrängung | Kette | Snubber Ø min | Snubber Ø empfohlen | Snubber Ø Sturm |
|-----------|-------------|-------|--------------|--------------------|--------------------|
| 6–8 m | 1,5–3 t | 6 mm | 12 mm | 14 mm | 16 mm |
| 8–10 m | 3–5 t | 8 mm | 14 mm | 16 mm | 18 mm |
| 10–12 m | 5–8 t | 8 mm | 16 mm | 16 mm | 20 mm |
| 12–14 m | 8–12 t | 10 mm | 16 mm | 18 mm | 22 mm |
| 14–16 m | 12–18 t | 10 mm | 18 mm | 20 mm | 24 mm |
| 16–18 m | 18–25 t | 12 mm | 20 mm | 22 mm | 26 mm |
| 18–20 m | 25–35 t | 12 mm | 22 mm | 24 mm | 28 mm |
| 20–24 m | 35–50 t | 14 mm | 24 mm | 26 mm | 30 mm |

### 4.2 Snubber-Länge

Die Länge des Snubbers beeinflusst direkt die Dämpfungscharakteristik.
Längere Snubber bieten mehr Federweg und sanftere Dämpfung.

**Berechnungsformel:**

```
L_snubber [m] = Bootslänge [m] × 0,5 bis 0,8

Minimum: 5 m
Maximum: 15 m (darüber hinaus wird die Handhabung schwierig)
```

**Empfohlene Längen:**

| Bootslänge | Normale Bedingungen | Starker Wind (30+ kn) | Sturm (45+ kn) |
|-----------|--------------------|-----------------------|-----------------|
| 6–8 m | 5 m | 6 m | 8 m |
| 8–10 m | 5–6 m | 7 m | 9 m |
| 10–12 m | 6–7 m | 8 m | 10 m |
| 12–14 m | 7–8 m | 9 m | 12 m |
| 14–16 m | 8–10 m | 10 m | 14 m |
| 16–18 m | 9–11 m | 12 m | 15 m |
| 18–20 m | 10–12 m | 13 m | 15 m |

### 4.3 Dehnung und Energieabsorption

**Dehnungskurve Nylon 3-Strand:**

| Belastung (% Bruchlast) | Dehnung |
|-------------------------|---------|
| 5 % | 3–4 % |
| 10 % | 6–8 % |
| 15 % | 9–12 % |
| 20 % | 12–16 % |
| 30 % | 18–22 % |
| 40 % | 24–28 % |
| 50 % | 28–32 % |
| Bruch | 35–45 % |

**Arbeitslastbereich (Working Load):**

Der Snubber sollte im Normalbetrieb bei 10–20 % seiner Bruchlast
arbeiten. Bei Sturm darf die Last bis 40 % der Bruchlast ansteigen.
Über 50 % besteht die Gefahr bleibender Verformung.

```
Arbeitsbereich normal: 10–20 % BL → Dehnung 6–16 %
Arbeitsbereich Sturm:  20–40 % BL → Dehnung 16–28 %
Grenzbereich:          40–50 % BL → Dehnung 28–32 %
Bruchgefahr:           > 50 % BL  → Dehnung > 32 %
```

### 4.4 Sicherheitsfaktor-Berechnung

```
SF = Bruchlast_Snubber / (Max_Windlast × Dynamischer_Faktor)

Empfohlene Sicherheitsfaktoren:
- Normales Ankern:     SF ≥ 5
- Nachtankern:         SF ≥ 4
- Starker Wind:        SF ≥ 3
- Sturmvorbereitung:   SF ≥ 2,5
- Absolutes Minimum:   SF ≥ 2
```

**Berechnungsbeispiel für 12-m-Segelboot:**

```
Verdrängung: 10 t
Windlastfläche (mit Mast): 15 m²
Windgeschwindigkeit: 35 kn = 18 m/s
Windlast F_wind = 0,5 × ρ × Cd × A × v²
       = 0,5 × 1,225 × 1,2 × 15 × 18²
       = 3.572 N

Dynamischer Faktor bei 35 kn mit Seegang: 2,0
Effektive Last: 3.572 × 2,0 = 7.144 N

Snubber 16 mm Nylon 3-Strand: Bruchlast 27.500 N
SF = 27.500 / 7.144 = 3,85 ✓ (Sturmtauglich)

Snubber 14 mm Nylon 3-Strand: Bruchlast 21.200 N
SF = 21.200 / 7.144 = 2,97 ✓ (Sturmtauglich, aber knapp)

Snubber 12 mm Nylon 3-Strand: Bruchlast 15.800 N
SF = 15.800 / 7.144 = 2,21 ⚠ (Grenzbereich bei Sturm)
```

### 4.5 Kettendurchhang (Slack)

Nach dem Setzen des Snubbers muss genügend Kettendurchhang nachgefiert
werden, damit die Kette bei normaler Last nicht durchgestreckt wird.

**Empfohlener Durchhang:**

| Bedingung | Kettendurchhang |
|-----------|----------------|
| Leichter Wind (< 15 kn) | 1,5–2,0 m |
| Mäßiger Wind (15–25 kn) | 2,0–3,0 m |
| Starker Wind (25–35 kn) | 3,0–4,0 m |
| Sturm (> 35 kn) | 4,0–6,0 m |

**Berechnung des optimalen Durchhangs:**

```
Durchhang [m] ≥ Snubber-Länge × Max_Dehnung × 1,5

Beispiel: 8 m Snubber, 25 % max. Dehnung:
Durchhang ≥ 8 × 0,25 × 1,5 = 3,0 m
```

Zu wenig Durchhang: Die Kette wird bei Böen durchgestreckt und die
gesamte Last geht auf die Winde — der Snubber ist wirkungslos.

Zu viel Durchhang: Die Kette schleift am Grund und kann sich an
Hindernissen verfangen. Außerdem wird das Einholen erschwert.

### 4.6 Doppelsnubber-Setup (Sturm)

Bei erwarteten Starkwindbedingungen (> 35 kn) empfiehlt sich ein
Doppelsnubber-System:

```
                    ┌─── Snubber A (Hauptsnubber)
                    │
    Klampe Bb ──────┤
                    │
                    ├─── Snubber B (Reservesnubber, 10 % länger)
                    │
    Klampe Stb ─────┘
                    │
              Kettenhaken (gemeinsam oder getrennt)
                    │
               Ankerkette
```

- **Snubber A**: Normale Länge, trägt die Hauptlast
- **Snubber B**: 10–15 % länger, übernimmt erst bei extremer Dehnung
  von Snubber A. Fungiert als Backup bei Bruch von Snubber A.

**Wichtig:** Beide Snubber an verschiedenen Klampen befestigen, um die
Last auf den Bugbereich zu verteilen.

---
---

## 5. Kettenhaken (Chain Hooks)

### 5.1 Grundlagen

Der Kettenhaken (Chain Hook) ist das Verbindungselement zwischen dem
Snubber-Seil und der Ankerkette. Er muss einfach ein- und auszuhängen
sein, zuverlässig halten und für die jeweilige Kettengröße passen.

**Anforderungen an einen guten Kettenhaken:**

1. **Passgenauigkeit**: Muss exakt zur Kettengröße passen (6, 8, 10, 12 mm)
2. **Zuverlässige Verriegelung**: Darf sich unter Last nicht lösen
3. **Einhändige Bedienung**: Muss sich bei Nacht und Seegang sicher bedienen lassen
4. **Korrosionsbeständigkeit**: Edelstahl 316L oder verzinkter Stahl
5. **Bruchlast**: Muss zur Snubber-Bruchlast passen (schwächstes Glied!)
6. **Keine Kettenbeschädigung**: Darf die Verzinkung der Kette nicht beschädigen

### 5.2 Hakentypen

#### 5.2.1 Offener Haken (Open Hook)

Der einfachste Typ — ein gebogener Haken aus Edelstahl oder verzinktem
Stahl, der in ein Kettenglied eingehängt wird.

**Vorteile:**
- Günstig (15–40 EUR)
- Einfache Bedienung
- Funktioniert mit verschiedenen Kettengrößen

**Nachteile:**
- Kann sich bei Richtungswechsel aushängen
- Kein Verriegelungsmechanismus
- Bei Schwellwellen und Dreher unzuverlässig

**Empfehlung:** Nur für kurzzeitiges Tagesankern bei ruhigen Bedingungen.

#### 5.2.2 Geschlossener Haken mit Sicherung (Latch Hook)

Ein Haken mit Federverriegelung oder Schraubsicherung, der ein
unbeabsichtigtes Aushängen verhindert.

**Vorteile:**
- Zuverlässige Verriegelung
- Funktioniert bei Richtungswechsel
- Sicher auch bei Schwellwellen

**Nachteile:**
- Teurer (40–120 EUR)
- Verriegelung kann korrodieren
- Bedienung bei Nacht und kalten Fingern schwieriger

#### 5.2.3 Klauenhaken (Claw Hook / Devil's Claw)

Ein zweiteiliger Haken, der das Kettenglied von beiden Seiten umfasst
und sich unter Last selbst verriegelt.

**Vorteile:**
- Höchste Sicherheit
- Selbstverriegelnd unter Last
- Kann nicht versehentlich aushängen
- Auch als permanenter Kettenstopper nutzbar

**Nachteile:**
- Am teuersten (80–250 EUR)
- Schwerer
- Größenspezifisch — passt nur für eine Kettengröße

### 5.3 Kettenhaken — Herstellervergleich

#### 5.3.1 Mantus Chain Hook

**Hersteller:** Mantus Marine, USA
**Material:** Edelstahl 316L (geschmiedet)
**Typ:** Geschlossener Haken mit Sicherungsbolzen

| Modell | Kettengröße | WLL (Working Load Limit) | Bruchlast | Gewicht | Preis |
|--------|------------|-------------------------|-----------|---------|-------|
| Mantus Chain Hook S | 6–8 mm | 2.270 kg | 9.070 kg | 280 g | 79 EUR |
| Mantus Chain Hook M | 8–10 mm | 3.400 kg | 13.600 kg | 420 g | 99 EUR |
| Mantus Chain Hook L | 10–13 mm | 4.500 kg | 18.140 kg | 580 g | 119 EUR |
| Mantus Chain Hook XL | 12–16 mm | 5.670 kg | 22.680 kg | 780 g | 149 EUR |

**Besonderheiten:**
- Patentierter Sicherungsbolzen mit Federmechanismus
- Kann mit Handschuhen bedient werden
- Integrierte Seilöse für Snubber-Spleiß
- Lebenslange Garantie des Herstellers

**AYDI-Bewertung:** ★★★★★ — Referenzprodukt, sehr zuverlässig

#### 5.3.2 Kong Chain Hook

**Hersteller:** Kong S.p.A., Italien
**Material:** Edelstahl AISI 316, geschmiedet
**Typ:** Geschlossener Haken mit Wirbel

| Modell | Kettengröße | WLL | Bruchlast | Gewicht | Preis |
|--------|------------|-----|-----------|---------|-------|
| Kong Anchor Chain Hook 8 | 6–8 mm | 1.500 kg | 6.000 kg | 350 g | 65 EUR |
| Kong Anchor Chain Hook 10 | 8–10 mm | 2.500 kg | 10.000 kg | 480 g | 85 EUR |
| Kong Anchor Chain Hook 12 | 10–12 mm | 3.500 kg | 14.000 kg | 620 g | 105 EUR |
| Kong Anchor Chain Hook 14 | 12–14 mm | 4.500 kg | 18.000 kg | 780 g | 135 EUR |

**Besonderheiten:**
- Integrierter Wirbel reduziert Torsionsbelastung
- Italienische Fertigung, CE-gekennzeichnet
- Auch als Bergungshaken verwendbar
- Farbcodierung für Kettengröße

**AYDI-Bewertung:** ★★★★☆ — Sehr gut, Wirbel ist Bonus

#### 5.3.3 Wichard Chain Hook

**Hersteller:** Wichard, Frankreich
**Material:** Edelstahl 316L HR (hochfest), geschmiedet
**Typ:** Forged Snap Hook mit Sicherung

| Modell | Kettengröße | WLL | Bruchlast | Gewicht | Preis |
|--------|------------|-----|-----------|---------|-------|
| Wichard 2483 | 6–8 mm | 1.200 kg | 4.800 kg | 180 g | 55 EUR |
| Wichard 2484 | 8–10 mm | 1.800 kg | 7.200 kg | 260 g | 72 EUR |
| Wichard 2485 | 10–12 mm | 2.400 kg | 9.600 kg | 380 g | 89 EUR |
| Wichard 2486 | 12–14 mm | 3.200 kg | 12.800 kg | 500 g | 115 EUR |

**Besonderheiten:**
- Extrem leicht (Wichard ist bekannt für optimierte Konstruktionen)
- HR-Stahl (hochfest kaltgewalzt) — höhere Festigkeit bei geringerem Gewicht
- Bewährtes Marinedesign
- Auch für Dyneema-Snubber geeignet (glatte Öse)

**AYDI-Bewertung:** ★★★★☆ — Sehr leicht und gut verarbeitet, geringere WLL

#### 5.3.4 Yale Cordage Chain Grab

**Hersteller:** Yale Cordage, USA
**Material:** Edelstahl 316, gegossen + geschmiedet
**Typ:** Chain Grab mit formschlüssiger Kettenaufnahme

| Modell | Kettengröße | WLL | Bruchlast | Gewicht | Preis |
|--------|------------|-----|-----------|---------|-------|
| Yale Chain Grab 5/16" | 8 mm | 2.700 kg | 10.800 kg | 520 g | 89 EUR |
| Yale Chain Grab 3/8" | 10 mm | 3.600 kg | 14.400 kg | 680 g | 109 EUR |
| Yale Chain Grab 1/2" | 12–13 mm | 5.000 kg | 20.000 kg | 880 g | 139 EUR |

**Besonderheiten:**
- Formschlüssige Kettenaufnahme — sitzt extrem stabil
- Verkantet nicht in der Kette
- Für professionellen Einsatz (Fischereifahrzeuge, Arbeitsboote)
- Mitgeliefertes Softschäkel (Dyneema) für Snubber-Verbindung

**AYDI-Bewertung:** ★★★★★ — Professionelle Qualität, formschlüssig

#### 5.3.5 Ultra Marine Chain Hook

**Hersteller:** Ultra Marine, Neuseeland
**Material:** Edelstahl 316L, CNC-gefräst
**Typ:** Precision Chain Hook

| Modell | Kettengröße | WLL | Bruchlast | Gewicht | Preis |
|--------|------------|-----|-----------|---------|-------|
| Ultra Hook 8 | 8 mm | 2.000 kg | 8.000 kg | 390 g | 95 EUR |
| Ultra Hook 10 | 10 mm | 3.000 kg | 12.000 kg | 550 g | 115 EUR |
| Ultra Hook 12 | 12 mm | 4.000 kg | 16.000 kg | 720 g | 145 EUR |

**Besonderheiten:**
- CNC-gefräst aus Vollmaterial (keine Gussfehler)
- Passgenau für ISO-Kette (DIN 766)
- Vom gleichen Hersteller wie der Ultra-Anker
- Lebenslange Garantie

**AYDI-Bewertung:** ★★★★☆ — Hochwertig, Premium-Preis

### 5.4 Kettenhaken — Vergleichsmatrix

| Kriterium | Mantus | Kong | Wichard | Yale | Ultra |
|-----------|--------|------|---------|------|-------|
| WLL (10 mm) | 3.400 kg | 2.500 kg | 1.800 kg | 3.600 kg | 3.000 kg |
| Bruchlast (10 mm) | 13.600 kg | 10.000 kg | 7.200 kg | 14.400 kg | 12.000 kg |
| Gewicht (10 mm) | 420 g | 480 g | 260 g | 680 g | 550 g |
| Preis (10 mm) | 99 EUR | 85 EUR | 72 EUR | 109 EUR | 115 EUR |
| Sicherung | Bolzen | Feder | Feder | Formschluss | Feder |
| Wirbel | Nein | Ja | Nein | Nein | Nein |
| Einhändige Bedienung | Ja | Ja | Ja | Mäßig | Ja |
| Garantie | Lebenslang | 5 Jahre | 3 Jahre | 5 Jahre | Lebenslang |
| Verfügbarkeit DE | Gut | Sehr gut | Sehr gut | Mäßig | Mäßig |

### 5.5 DIY-Kettenhaken — Selbstbau

Für Notfälle oder als Sparmaßnahme kann ein Kettenhaken aus einem
Edelstahl-Karabiner und einer Kettenklemme improvisiert werden:

**Materialien:**
- Edelstahl-Schäkel 10 mm: ca. 12 EUR
- Softschäkel Dyneema 6 mm: ca. 8 EUR
- Edelstahl-Draht 3 mm für Sicherung: ca. 2 EUR

**Warnung:** Improvisierte Kettenhaken sind für den Dauereinsatz nicht
geeignet. Sie dienen ausschließlich als Notlösung bis ein professioneller
Haken beschafft werden kann.

### 5.6 Snubber-Kettenhaken-Verbindung

Die Verbindung zwischen Snubber und Kettenhaken ist ein kritischer Punkt.
Empfohlene Verbindungsmethoden (in Reihenfolge der Zuverlässigkeit):

1. **Augspleiß direkt in den Haken** — Beste Lösung. Bruchlastverlust
   nur 5–10 %. Dauerhafte, untrennbare Verbindung.

2. **Augspleiß + Schäkel** — Gute Lösung. Ermöglicht Haken-Wechsel.
   Bruchlastverlust 10–15 % durch Schäkel-Belastung auf den Spleiß.

3. **Softschäkel (Dyneema)** — Sehr gute Lösung. Leicht, stark, keine
   Korrosion. Bruchlastverlust minimal (5 %).

4. **Palstek-Knoten** — Akzeptable Lösung. Bruchlastverlust 30–40 %.
   Leicht lösbar, gut für temporären Einsatz.

5. **Klemm-Verbindung** — Nicht empfohlen. Kann unter dynamischer Last
   rutschen. Bruchlastverlust 50–70 %.

---
---

## 6. Kettenstopper und Devil's Claw

### 6.1 Grundlagen

Ein Kettenstopper (Chain Stopper) ist ein fest am Deck oder am Bugbeschlag
montiertes Bauteil, das die Ankerkette mechanisch blockiert und die Last
von der Ankerwinde auf das Deck überträgt. Im Unterschied zum Snubber
bietet ein Kettenstopper keine elastische Dämpfung — er ist ein starrer
Haltepunkt.

**Wichtig:** Ein Kettenstopper ersetzt keinen Snubber. Beide Komponenten
haben unterschiedliche Aufgaben und sollten idealerweise zusammen
verwendet werden:

- **Kettenstopper**: Sichert die Kette mechanisch, entlastet die Winde
- **Snubber**: Dämpft dynamische Lasten, schützt das gesamte System

### 6.2 Typen von Kettenstoppern

#### 6.2.1 Wippen-Kettenstopper (Hinged Chain Stopper)

Der am weitesten verbreitete Typ auf modernen Yachten. Eine klappbare
Stahlwippe presst sich unter Last gegen ein Kettenglied und blockiert
die Kette formschlüssig.

**Aufbau:**
```
      ┌──── Wippe (klappbar)
      │
  ════╪════ Grundplatte (am Deck verschraubt)
      │
  ~~~~│~~~~ Kette läuft durch
      │
  ════╪════ Bugrolle
```

**Funktionsweise:**
1. Kette unter Last einholen
2. Wippe umklappen → presst gegen Kettenglied
3. Sicherungsbolzen oder Federsicherung einsetzen
4. Kette ist blockiert, Winde kann entlastet werden

#### 6.2.2 Devil's Claw (Klauenkettenstopper)

Ein zweiteiliger Haken, der auf einer Grundplatte montiert ist und
das Kettenglied von beiden Seiten umfasst. Wird oft als zusätzlicher
Sicherungspunkt am Bugbeschlag montiert.

```
      ╔══╗
     ╱    ╲    ← Klauen (umfassen Kettenglied)
    ║  ⊙⊙  ║   ← Kettenglied
     ╲    ╱
      ╚══╝
       ||
    Grundplatte (auf Deck)
```

#### 6.2.3 Bolzen-Kettenstopper (Pin Stopper)

Ein Bolzen wird durch die Grundplatte geschoben und blockiert die
Kette zwischen zwei Kettengliedern. Einfachste Konstruktion, aber
erfordert, dass der Bolzen genau zwischen zwei Gliedern sitzt.

### 6.3 Kettenstopper — Herstellervergleich

#### 6.3.1 Mantus Chain Stopper

**Hersteller:** Mantus Marine, USA
**Material:** Edelstahl 316L, geschmiedet + geschweißt
**Typ:** Wippen-Kettenstopper mit Federsicherung

| Modell | Kettengröße | WLL | Gewicht | Preis |
|--------|------------|-----|---------|-------|
| Mantus Chain Stopper S | 6–8 mm | 3.000 kg | 680 g | 129 EUR |
| Mantus Chain Stopper M | 8–10 mm | 4.500 kg | 920 g | 159 EUR |
| Mantus Chain Stopper L | 10–12 mm | 6.000 kg | 1.250 g | 189 EUR |
| Mantus Chain Stopper XL | 12–14 mm | 8.000 kg | 1.580 g | 229 EUR |

**Besonderheiten:**
- Passt auf Standard-Bugrollen (Lochabstand anpassbar)
- Federsicherung verhindert versehentliches Öffnen
- Auch nachrüstbar auf vorhandene Bugbeschläge
- Integrierte Ablaufbohrung für Wasser

**AYDI-Bewertung:** ★★★★★ — Marktführer, zuverlässig und gut konstruiert

#### 6.3.2 Maxwell Chain Stopper

**Hersteller:** Maxwell Marine, Neuseeland (jetzt Vetus)
**Material:** Edelstahl 316L, gegossen
**Typ:** Integrierter Kettenstopper (in Maxwell-Winden-Plattform)

| Modell | Kettengröße | WLL | Gewicht | Preis |
|--------|------------|-----|---------|-------|
| Maxwell P105020 | 6–8 mm | 2.500 kg | 1.200 g | 189 EUR |
| Maxwell P105021 | 8–10 mm | 3.800 kg | 1.600 g | 229 EUR |
| Maxwell P105022 | 10–12 mm | 5.000 kg | 2.100 g | 279 EUR |
| Maxwell P105023 | 12–14 mm | 6.500 kg | 2.800 g | 349 EUR |

**Besonderheiten:**
- Integrale Bugrolle mit Kettenstopper
- Designed für Maxwell-Windensysteme
- Hochglanzpoliert (optisch ansprechend)
- Einhändige Bedienung durch Hebelmechanismus

**AYDI-Bewertung:** ★★★★☆ — Sehr gut integriert, aber systemgebunden

#### 6.3.3 Lewmar Chain Stopper

**Hersteller:** Lewmar, UK
**Material:** Edelstahl 316L + GfK-verstärkte Grundplatte
**Typ:** Wippen-Kettenstopper

| Modell | Kettengröße | WLL | Gewicht | Preis |
|--------|------------|-----|---------|-------|
| Lewmar Chain Stopper 6-8 | 6–8 mm | 2.000 kg | 550 g | 109 EUR |
| Lewmar Chain Stopper 8-10 | 8–10 mm | 3.200 kg | 780 g | 139 EUR |
| Lewmar Chain Stopper 10-12 | 10–12 mm | 4.500 kg | 1.050 g | 169 EUR |

**AYDI-Bewertung:** ★★★★☆ — Solide Qualität, gutes Preis-Leistung

#### 6.3.4 Custom Devil's Claw (Edelstahl-Manufakturen)

Viele Blauwasser-Segler lassen sich individuelle Devil's Claw anfertigen,
die perfekt auf ihr Boot und ihre Kette passen.

**Typische Spezifikationen:**
- Material: Edelstahl 316L, 12–16 mm Rundmaterial
- Grundplatte: 6–10 mm Edelstahl, 4× M10/M12 Befestigung
- Kettengröße: exakt angepasst (nicht universal)
- WLL: 5.000–10.000 kg
- Preis: 200–500 EUR (Edelstahl-Schlosser)

**Vorteile Individualbau:**
- Perfekte Passform zum Boot und zum Bugbeschlag
- Höhere WLL als Standardprodukte möglich
- Integration zusätzlicher Funktionen (z. B. Snubber-Öse)
- Oft optisch ansprechender als Standardware

**Nachteile:**
- Keine Zertifizierung
- Qualität abhängig vom Handwerker
- Schweißnähte müssen erstklassig sein (316L-Schweißen erfordert Erfahrung)
- Nachbestellung/Ersatz schwierig

### 6.4 Installation Kettenstopper

**Anforderungen an die Befestigung:**

1. **Decksstärke**: Mindestens 8 mm GFK oder 5 mm Edelstahl unter dem
   Kettenstopper. Bei dünneren Decks: Verstärkungsplatte unterlegen.

2. **Schrauben**: Mindestens 4× M10 Edelstahl-Bolzen mit Unterlegscheibe
   und Kontermutter. Durchgangsbolzen — keine Blechschrauben!

3. **Unterfütterung**: Epoxid-Verguss zwischen Kettenstopper und Deck,
   um Spannungsspitzen an den Schraubenlöchern zu vermeiden.

4. **Dichtung**: Butylband oder Sikaflex 291 zwischen Grundplatte und
   Deck. Kein Silikon — wird durch UV und mechanische Belastung undicht.

5. **Lastverteilung**: Gegenplatte unter Deck (mindestens 6 mm Edelstahl
   oder 12 mm Sperrholz mit Glaslaminat) zur Verteilung der Zugkräfte.

**Montage-Checkliste:**

- [ ] Position markieren (Kettenlauf zur Winde prüfen)
- [ ] Bohrungen setzen (Schablone verwenden)
- [ ] Kanten entgraten und Deck-Laminat anschleifen
- [ ] Gegenplatte positionieren
- [ ] Butylband/Dichtstoff auftragen
- [ ] Kettenstopper aufsetzen, Bolzen einsetzen
- [ ] Mit Drehmomentschlüssel anziehen (Herstellervorgabe)
- [ ] Dichtigkeitskontrolle nach 24 h
- [ ] Funktionstest unter Last

**Detaillierte Montageanleitung:**

**Schritt 1 — Positionsbestimmung:**
Den Kettenstopper so positionieren, dass die Kette in gerader Linie
von der Bugrolle zum Kettenstopper und weiter zum Kettenkasten bzw.
zur Winde läuft. Jeder Knick im Kettenverlauf erzeugt Reibung und
erhöhte Belastung. Mit einem Stück Kette den Verlauf simulieren und
die optimale Position markieren.

**Schritt 2 — Bohrungsplanung:**
Die Schablone des Herstellers auf das Deck legen und mit einem
wasserfesten Stift die Bohrpositionen markieren. Mindestabstand der
Bohrungen zur Deckkante: 3× Bolzendurchmesser. Vor dem Bohren mit
einem kleinen Bohrer (3 mm) vorbohren, dann auf Endmaß aufbohren.
Bohrung immer von oben (Gelcoat-Seite) nach unten, um Ausrisse im
Laminat zu vermeiden.

**Schritt 3 — Laminat-Vorbereitung:**
Den Bereich um die Bohrungen auf der Unterseite (ca. 5 cm Radius)
anschleifen (Körnung 80). Dies ermöglicht eine bessere Haftung des
Epoxid-Vergusses, der die Bohrungen wasserdicht verschließt.
Bei dünnem Deck (< 10 mm): Laminat mit 2–3 Lagen Glas + Epoxid
aufdoppeln. Aushärtezeit einhalten (24 h bei Raumtemperatur).

**Schritt 4 — Gegenplatte:**
Gegenplatte (Edelstahl 316L, 6 mm oder Aluminium 5083, 8 mm oder
Marine-Sperrholz 12 mm mit Epoxid-Versiegelung) unter Deck
positionieren. Die Gegenplatte muss mindestens 2× so groß sein wie
die Grundplatte des Kettenstoppers, um die Kräfte auf eine größere
Decksfläche zu verteilen.

**Schritt 5 — Abdichtung und Montage:**
Butylband (z. B. Terostat) auf die Auflagefläche des Kettenstoppers
legen oder Sikaflex 291 als Perle um die Bohrungen auftragen.
Kettenstopper aufsetzen, Bolzen von oben durchstecken, Unterlegscheiben
(groß, Edelstahl A4) und Muttern (selbstsichernd oder mit
Schraubensicherung) ansetzen. Mit Drehmomentschlüssel anziehen:
M10: 25 Nm, M12: 40 Nm. Überschüssigen Dichtstoff entfernen.

**Schritt 6 — Funktionstest:**
24 h nach der Montage (Dichtstoff-Aushärtung) einen Funktionstest
durchführen: Kette durch den Kettenstopper führen, Wippe schließen,
mit der Winde moderate Last aufbauen (ca. 500 N). Prüfen:
Kette blockiert sicher, keine Verformung sichtbar, kein Wasseraustritt
an den Bohrungen.

---
---

## 7. Ruckdämpfer und Mooring-Kompensatoren

### 7.1 Grundlagen

Neben dem klassischen Nylon-Snubber gibt es spezialisierte
Ruckdämpfer-Systeme, die für bestimmte Anwendungen optimiert sind:
Mooringleinen-Dämpfer, Dalben-Kompensatoren und Fenderfeder-Systeme.

### 7.2 Mooring Compensator (Festmacher-Dämpfer)

**Funktion:** Wird in die Mooringleine eingeschleift und kompensiert
Tidenhub, Sog von vorbeifahrenden Schiffen und Windböen beim Liegen
am Steg.

**Typische Produkte:**

| Hersteller | Produkt | Für Boote | Bruchlast | Hub | Preis |
|-----------|---------|-----------|-----------|-----|-------|
| Unimer | Mooring Compensator U-Cleat | 6–10 m | 5.000 N | 0,5 m | 45 EUR |
| Unimer | Mooring Compensator U-Cleat | 10–14 m | 8.000 N | 0,7 m | 65 EUR |
| Unimer | Mooring Compensator U-Cleat | 14–18 m | 12.000 N | 0,9 m | 85 EUR |
| Unimer | Mooring Compensator U-Cleat | 18–24 m | 18.000 N | 1,2 m | 115 EUR |
| Dock Edge | Mooring Snubber | 8–12 m | 6.000 N | 0,6 m | 35 EUR |
| Dock Edge | Mooring Snubber | 12–18 m | 10.000 N | 0,8 m | 55 EUR |
| Eval | EQ Mooring | 8–14 m | 8.000 N | 0,7 m | 55 EUR |
| Eval | EQ Mooring | 14–20 m | 14.000 N | 1,0 m | 85 EUR |

### 7.3 DockLine Snubber

**Funktion:** Speziell für die Integration in Festmacherleinen
konstruierte Inline-Dämpfer. Anders als Mooring-Kompensatoren werden
sie nicht über einen Gummizug, sondern über eine interne Nylon-Schlaufe
gedämpft.

**Typische Produkte:**

| Hersteller | Produkt | Leinendurchmesser | Bruchlast | Preis |
|-----------|---------|-------------------|-----------|-------|
| Davis Instruments | Dock Line Snubber | 10–14 mm | 4.500 N | 25 EUR |
| Davis Instruments | Dock Line Snubber | 14–18 mm | 7.000 N | 35 EUR |
| Greenfield | Dock Snubber | 12–16 mm | 5.500 N | 30 EUR |
| Greenfield | Dock Snubber | 16–20 mm | 9.000 N | 45 EUR |

### 7.4 Fender-Feder-Systeme

Für Boote an exponierten Liegeplätzen (Tidenhub, starke Strömung,
Schiffswellen) bieten Fender-Feder-Systeme eine Kombination aus
Ruckdämpfung und Fenderschutz.

| Hersteller | Produkt | Für Boote | Hub | Preis |
|-----------|---------|-----------|-----|-------|
| Ocean Fender | Spring Fender | 8–12 m | 0,4 m | 120 EUR |
| Ocean Fender | Spring Fender | 12–18 m | 0,6 m | 180 EUR |
| Polyform | Fender mit integrierter Feder | 10–16 m | 0,5 m | 150 EUR |

### 7.5 Vergleich: Snubber vs. Mooring Compensator vs. DockLine Snubber

| Eigenschaft | Nylon-Snubber | Mooring Comp. | DockLine Snubber |
|------------|--------------|---------------|-----------------|
| Anwendung | Ankern | Steg/Boje | Steg/Boje |
| Dämpfungsweg | 1–3 m | 0,5–1,2 m | 0,3–0,8 m |
| Energieabsorption | Sehr hoch | Mittel | Gering |
| Bruchlast | Hoch | Mittel | Gering |
| Lebensdauer | 3–5 Jahre | 5–8 Jahre | 2–4 Jahre |
| Installation | Manuell (Haken) | Inline (Spleiß) | Inline (Klemme) |
| Preis | 30–80 EUR | 35–115 EUR | 25–45 EUR |

---
---

## 8. Bridle-Systeme für Katamarane

### 8.1 Warum Katamarane ein Bridle brauchen

Katamarane haben im Gegensatz zu Einrumpf-Booten keinen zentralen
Bugbeschlag, an dem der Snubber befestigt werden kann. Die beiden Rümpfe
sind durch ein Brückendeck verbunden, und der Anker wird typischerweise
über eine zentrale Bugrolle oder eine Bugplattform bedient.

**Problem ohne Bridle:**

```
     Rumpf Bb       Rumpf Stb
        │               │
        │    (Brücke)    │
        │       │        │
        │    Bugrolle     │
        │       │        │
        │    Snubber      │
        │       │        │
        │    Kette        │
        └───────┘
             ⚓

→ Gesamte Ankerlast auf dem zentralen Bugbeschlag
→ Keine Querstabilität bei seitlichem Wind/Strömung
→ Boot segelt am Anker (pendelt stark)
```

**Lösung mit Bridle (Y-Bridle):**

```
     Rumpf Bb       Rumpf Stb
        │               │
     Klampe Bb       Klampe Stb
        │               │
        │  Bridle Bb    │  Bridle Stb
        │     (Nylon)   │    (Nylon)
        │       \       │    /
        │        \      │   /
        │         ======│=
        │         Bridle-Schäkel/
        │         Kettenhaken
        │              │
        │           Kette
        │              │
        └──────────────┘
                ⚓
```

### 8.2 Bridle-Dimensionierung

**Bridle-Länge:**

```
L_bridle [m] = 1,2 × Rumpfabstand [m] + 2 m

Typische Werte:
- 10 m Katamaran (Rumpfabstand 4 m): L = 1,2 × 4 + 2 = 6,8 m → 7 m
- 12 m Katamaran (Rumpfabstand 5 m): L = 1,2 × 5 + 2 = 8,0 m → 8 m
- 14 m Katamaran (Rumpfabstand 6 m): L = 1,2 × 6 + 2 = 9,2 m → 9 m
```

**Bridle-Durchmesser:**

| Katamaran-Länge | Verdrängung | Bridle Ø | Material |
|----------------|-------------|----------|----------|
| 8–10 m | 3–5 t | 14 mm | Nylon 3-Strand |
| 10–12 m | 5–8 t | 16 mm | Nylon 3-Strand |
| 12–14 m | 8–12 t | 18 mm | Nylon 3-Strand |
| 14–16 m | 12–18 t | 20 mm | Nylon 3-Strand |
| 16–18 m | 18–25 t | 22 mm | Nylon 3-Strand |

### 8.3 Bridle-Konfigurationen

#### 8.3.1 Y-Bridle (Standard)

Zwei separate Leinen von den Bug-Klampen beider Rümpfe, die über einen
gemeinsamen Schäkel oder Kettenhaken an der Ankerkette zusammenlaufen.

**Vorteile:**
- Einfach und bewährt
- Gleichmäßige Lastverteilung
- Reduziert Segeln am Anker erheblich

**Nachteile:**
- Drei Verbindungspunkte (2× Klampe, 1× Kettenhaken)
- Kann sich bei Richtungswechsel verwickeln
- Kettenhaken-Punkt liegt unter Wasser → schwer zugänglich

#### 8.3.2 V-Bridle mit zentralem Snubber

Ein Y-Bridle mit einem zusätzlichen zentralen Snubber, der vom
V-Punkt zur Kette führt.

```
     Klampe Bb         Klampe Stb
        \               /
    Bridle Bb      Bridle Stb
          \          /
           V-Punkt (Ring/Schäkel)
              |
         Snubber (Nylon, 3–5 m)
              |
         Kettenhaken
              |
           Kette
```

**Vorteile:**
- Zusätzliche Dämpfung durch zentralen Snubber
- Bridle-Leinen können aus nicht-elastischem Material sein (Dyneema)
- Bessere Entkopplung

**Nachteile:**
- Komplexerer Aufbau
- Mehr Verbindungspunkte
- Teurer

#### 8.3.3 Delta-Bridle mit Fairlead

Für Katamarane mit zentraler Bugplattform wird das Bridle durch
Fairleads (Umlenkungen) an den Rumpfinnenseiten geführt.

**Vorteile:**
- Saubere Leinenführung
- Kein Scheuern am Brückendeck
- Optisch unauffällig

**Nachteile:**
- Erfordert Fairlead-Installation
- Höherer Reibungsverlust
- Aufwändiger einzurichten

### 8.4 Bridle-Fairleads

Fairleads verhindern, dass die Bridle-Leinen am Rumpf oder Brückendeck
scheuern und führen die Last sauber auf die Klampen.

**Empfohlene Fairleads für Bridle:**

| Hersteller | Produkt | Material | Max. Seil Ø | Preis |
|-----------|---------|----------|-------------|-------|
| Wichard | Fairlead 60 mm | Edelstahl 316L | 20 mm | 45 EUR |
| Wichard | Fairlead 80 mm | Edelstahl 316L | 24 mm | 65 EUR |
| Harken | Micro Fairlead | Aluminium eloxiert | 16 mm | 35 EUR |
| Lewmar | Bull's Eye | Edelstahl 316L | 22 mm | 55 EUR |
| Antal | Fairlead Ring | Edelstahl 316L | 20 mm | 40 EUR |

### 8.5 Spezielle Katamaran-Snubber-Produkte

| Hersteller | Produkt | Für Kats | Inhalt | Preis |
|-----------|---------|----------|--------|-------|
| Mantus | Bridle Hook Set | 10–14 m | 2× Chain Hook + Schäkel | 179 EUR |
| Mantus | Bridle Hook Set | 14–18 m | 2× Chain Hook + Schäkel | 219 EUR |
| SailRite | Cat Bridle Kit | 10–14 m | 2× 14 mm Nylon, 7 m + Haken | 129 EUR |
| SailRite | Cat Bridle Kit | 14–18 m | 2× 18 mm Nylon, 9 m + Haken | 179 EUR |
| Rocna | Bridle System | 12–16 m | Komplettsystem | 249 EUR |

### 8.6 Katamar-Anker-Segeln verhindern

„Segeln am Anker" (Anchor Sailing) ist ein bekanntes Problem bei
Katamaranen — der große Windwiderstand und die breite Bugfläche lassen
den Katamaran am Anker hin und her pendeln, manchmal in Figur-8-Mustern.

**Gegenmaßnahmen:**

1. **Bridle verwenden** — Grundvoraussetzung
2. **Bridle-Winkel optimieren** — 60–90° Öffnungswinkel zwischen den Leinen
3. **Kellet (Ankergewicht)** am Bridle-V-Punkt — reduziert Pendeln
4. **Flopper-Stopper** — Stabilisierungsplatten (reduzieren Rollen)
5. **Mehr Kette fieren** — erhöht die Haltekraft am Grund
6. **Segel bergen** — kein Segeltuch an Deck lassen

---
---

## 9. Kellet und Ankergewicht (Sentinel)

### 9.1 Grundlagen

Ein Kellet (auch Sentinel, Ankergewicht oder Angel-Guardian genannt)
ist ein Gewicht, das an der Ankerkette herabgelassen wird und den
Katarakt (Durchhang) der Kette vergrößert. Dies hat mehrere positive
Effekte:

1. **Flacherer Abgangswinkel am Anker** → höhere Haltekraft
2. **Vergrößerter Kettenkatarakt** → bessere Stoßdämpfung
3. **Reduziertes Schwingen** → weniger Segeln am Anker
4. **Effektiv mehr Scope** bei begrenzter Kettenlänge

### 9.2 Physik des Kellets

```
Ohne Kellet:
                     Boot
                    /
                   /  Kette (Katarakt)
                  /
                 /
    ────────────⚓───── Grund

Mit Kellet (5–10 kg bei ~1/3 der Kettenlänge):
                     Boot
                    /
                   /
                  /
      Kellet ●  /
              \/
               \
    ────────────⚓───── Grund

→ Die Kette bildet einen steileren Winkel vom Boot zum Kellet
   und einen flacheren Winkel vom Kellet zum Anker.
→ Der Zug am Anker ist horizontaler → bessere Haltekraft.
```

### 9.3 Kellet-Dimensionierung

| Bootslänge | Verdrängung | Kellet-Gewicht min | Kellet-Gewicht empfohlen |
|-----------|-------------|-------------------|-------------------------|
| 6–8 m | 1,5–3 t | 3 kg | 5 kg |
| 8–10 m | 3–5 t | 5 kg | 7 kg |
| 10–12 m | 5–8 t | 7 kg | 10 kg |
| 12–14 m | 8–12 t | 10 kg | 14 kg |
| 14–16 m | 12–18 t | 14 kg | 18 kg |
| 16–18 m | 18–25 t | 18 kg | 22 kg |

### 9.4 Kellet-Position

**Optimale Position:** Bei 1/3 bis 1/2 der gefierten Kettenlänge,
gemessen vom Bug.

```
Beispiel: 50 m Kette gefiert
→ Kellet bei 15–25 m vom Bug entfernt
→ Kellet hängt in ca. 3–5 m Wassertiefe
```

### 9.5 Kellet-Produkte

| Hersteller | Produkt | Gewicht | Material | Preis |
|-----------|---------|---------|----------|-------|
| Mantus | Anchor Mate | 5 kg | Blei/Edelstahl | 89 EUR |
| Mantus | Anchor Mate | 10 kg | Blei/Edelstahl | 129 EUR |
| Mantus | Anchor Mate | 15 kg | Blei/Edelstahl | 179 EUR |
| Greenfield | Sentinel | 6 kg | Gusseisen | 45 EUR |
| Greenfield | Sentinel | 12 kg | Gusseisen | 75 EUR |
| Kiwi Anchor Rider | Kellet | 8 kg | Blei/Kunststoff | 95 EUR |
| Kiwi Anchor Rider | Kellet | 14 kg | Blei/Kunststoff | 145 EUR |
| DIY | Tauchblei/Kettenstück | 5–15 kg | Blei/Kette | 20–50 EUR |

### 9.6 Kellet-Leine

Das Kellet wird über eine separate Leine (Kellet-Leine) am
Kettenglied befestigt und vom Boot aus bedient.

**Anforderungen:**
- Material: Leichtes, gut sichtbares Seil (Polyester, 6–8 mm)
- Länge: Kettenlänge + 5 m Reserve
- Befestigung: Karabiner oder Schäkel am Kellet, Reiterschnur an der Kette
- Rückholleine: Muss das Kellet zurück an die Wasseroberfläche bringen
  können

**Kellet-Befestigungsmethoden:**

1. **Reiterschnur (Prusik) um die Kette:**
   Eine dünne Leine (4–6 mm Dyneema) wird als Prusik-Knoten um die
   Ankerkette gelegt. Der Prusik greift unter Last und lässt sich im
   entlasteten Zustand verschieben. Die Kellet-Halteleine wird an
   der Reiterschnur befestigt.

2. **Karabiner an Kettenglied:**
   Ein Edelstahl-Karabiner wird durch ein Kettenglied gehängt. Einfach,
   aber der Karabiner kann bei langer Kette schwer zu erreichen sein.
   Vorteil: Exakte Positionierung möglich.

3. **Laufschlitten (siehe 9.7):**
   Modernste Methode — der Schlitten gleitet auf der Kette und kann
   von Deck aus bedient werden.

**Kellet-Rückhol-System:**
Das Kellet muss beim Ankerlichten einfach zurückgeholt werden können.
Zwei bewährte Methoden:
- **Separate Rückholleine**: Vom Kellet zum Bug, parallel zur Kette.
  Beim Einholen der Kette: Rückholleine einholen, wenn Kellet an der
  Wasseroberfläche erscheint.
- **Laufschlitten mit Rückhol-Automatik**: Gleitet beim Einholen
  automatisch zum Bug zurück (siehe 9.7).

### 9.7 Kellet-Laufschlitten (Anchor Rider)

Modernere Kellet-Systeme verwenden einen Laufschlitten, der auf der
Ankerkette gleitet und beim Einholen der Kette automatisch zum Bug
zurückwandert.

| Hersteller | Produkt | Kettengröße | Gewicht | Preis |
|-----------|---------|-------------|---------|-------|
| Kiwi Anchor Rider | Standard | 8–10 mm | 3,5 kg (+ Zusatzgewicht) | 95 EUR |
| Kiwi Anchor Rider | Heavy | 10–12 mm | 5 kg (+ Zusatzgewicht) | 135 EUR |
| Rocna | Chain Rider | 8–12 mm | 4 kg (+ Zusatzgewicht) | 110 EUR |

**Funktionsweise:**
1. Schlitten auf Kette fädeln (wenn Kette eingeholt ist)
2. Kette fieren — Schlitten gleitet mit
3. Am gewünschten Punkt: Sicherungsleine belegen
4. Beim Einholen: Schlitten gleitet zurück zum Bug

---
---

## 10. Installation und Befestigung

### 10.1 Snubber-Befestigungspunkt am Boot

Der Befestigungspunkt des Snubbers am Boot ist kritisch. Er muss die
gesamte dynamische Ankerlast aufnehmen können.

**Empfohlene Befestigungspunkte (in Reihenfolge der Eignung):**

1. **Bug-Klampen (Belegklampen)**
   - Beste Lösung für die meisten Boote
   - Klampe muss für die Ankerlast dimensioniert sein
   - Minimum: Klampe mit 4× Durchgangsbolzen und Gegenplatte
   - Snubber wird auf der Klampe belegt (Kreuzschlag + Kopfschlag)

2. **Kettenkasten-Poller**
   - Auf größeren Yachten vorhanden
   - Sehr solide Befestigung (oft direkt mit dem Rumpf verbunden)
   - Snubber über den Poller belegen

3. **Bugbeschlag-Auge**
   - Einige Bugbeschläge haben eine integrierte Snubber-Öse
   - Muss separat geprüft werden (oft unterdimensioniert)

4. **Ankerrolle mit Klampe**
   - Kombiniertes System (z. B. Maxwell, Lewmar)
   - Praktisch, aber Lastaufnahme prüfen

**Nicht geeignet:**

- ❌ Reling (zu schwach, kann sich verbiegen)
- ❌ Bugrolle allein (Snubber kann abrutschen)
- ❌ Durch den Kettenkastendeckel (Reibung, Undichtigkeit)
- ❌ Windenbefestigung (genau das soll der Snubber entlasten!)

### 10.2 Schamfilschutz (Chafe Protection)

Die größte Gefahr für einen Snubber ist das Durchscheuern an der
Bugrolle, am Deck oder am Bugbeschlag. Statistisch versagen mehr
Snubber durch Scheuerbruch als durch Überlastung.

**Schamfilschutz-Methoden:**

1. **Schlauch über den Snubber (Standard)**
   - Gartenschlauch oder PVC-Schlauch über den Snubber ziehen
   - Muss die gesamte Kontaktstelle abdecken
   - Billige, effektive Lösung
   - Preis: 2–5 EUR

2. **Leder-Schamfilschutz**
   - Genähter Lederstreifen um den Snubber
   - Traditionell, langlebig, sehr effektiv
   - Preis: 15–30 EUR (Maßanfertigung)

3. **Dyneema-Chafe Guard**
   - Gewebter Dyneema-Schlauch über dem Snubber
   - Extrem abriebfest
   - Preis: 20–40 EUR
   - Hersteller: Robline, Yale Cordage

4. **Kederschiene am Bugbeschlag**
   - Teflon- oder HDPE-Einsatz in der Bugrolle
   - Reduziert Reibung dauerhaft
   - Preis: 25–60 EUR

5. **Fairlead (Umlenkung)**
   - Geschlossener Führungsring am Bug
   - Verhindert, dass der Snubber seitlich abrutscht
   - Preis: 30–80 EUR (Wichard, Lewmar)

### 10.3 Snubber-Setup: Schritt-für-Schritt

**Standard-Einrichtung nach dem Ankern:**

1. **Anker setzen und Haltekraft bestätigen**
   - Rückwärts eingraben (Motor oder Wind)
   - GPS-Position notieren
   - Peilungen zu Landmarken aufnehmen

2. **Gewünschte Kettenlänge fieren**
   - Scope 5:1 (normal) bis 7:1 (Starkwind)
   - Kette markieren (Farbe oder Kabelbinder alle 10 m)

3. **Kette auf Winde oder Kettenstopper sichern**

4. **Snubber vorbereiten**
   - Schamfilschutz positionieren
   - Kettenhaken anbringen (wenn nicht dauerhaft verbunden)

5. **Kettenhaken in die Kette einhängen**
   - Haken ca. 1–2 m vor der Bugrolle einsetzen
   - Sicherung des Hakens überprüfen

6. **Snubber am Befestigungspunkt belegen**
   - Kreuzschlag + Kopfschlag auf der Klampe
   - Ausreichend Lose für Dehnung lassen

7. **Kette nachfieren (Slack geben)**
   - 2–4 m Durchhang fieren (je nach Bedingungen)
   - Kette muss sichtbar durchhängen

8. **Funktionskontrolle**
   - Boot fällt in den Snubber zurück
   - Kette hängt lose
   - Snubber übernimmt die gesamte Last
   - Kein Kontakt der Kette mit der Bugrolle

9. **Reservesicherung (empfohlen)**
   - Zweites Seil lose um die Kette legen
   - Dient als Backup bei Snubber-Versagen
   - Etwas länger als Snubber + Dehnung

10. **GPS-Ankeralarm setzen**
    - Radius: Kettenlänge + Snubber-Dehnung + 20 m
    - Akustischer Alarm auf Plotter und Handy

### 10.4 Snubber bei verschiedenen Ankergeschirr-Konfigurationen

**Reine Kettensysteme:**
Standard-Setup wie oben beschrieben.

**Kette + Leine (Gemischtes System):**
Snubber nicht nötig, da die Nylon-Leine bereits die Dämpfungsfunktion
übernimmt. Kettenstopper trotzdem empfohlen für den Kettenanteil.

**Zweiankersystem (Buganker + Heckanker):**
Jeweils ein separater Snubber pro Anker.

**Bahamian Moor (zwei Buganker, 180°):**
Snubber auf der Hauptkette. Zweite Kette mit separatem Snubber oder
direkt auf Klampe.

---
---

## 11. Nacht-Ankern Routine

### 11.1 Bedeutung der Nachtroutine

Beim Übernachten vor Anker ist eine systematische Kontrollroutine
entscheidend für die Sicherheit. Der Snubber spielt dabei eine
zentrale Rolle, da er die Anzeichen für Probleme (Segeln am Anker,
Dragging, Windänderung) sichtbar und hörbar macht.

### 11.2 Vor-dem-Schlafengehen-Checkliste

**Schritt 1: Snubber-Kontrolle**
- [ ] Snubber-Belastung visuell prüfen (unter moderater Spannung?)
- [ ] Schamfilschutz sitzt korrekt?
- [ ] Kettenhaken fest in der Kette?
- [ ] Kette hat Durchhang?
- [ ] Keine Kinken oder Verdrehungen im Snubber?

**Schritt 2: Ankerlage-Kontrolle**
- [ ] GPS-Position stimmt mit der Setzposition überein?
- [ ] Peilungen zu Landmarken unverändert?
- [ ] Ankeralarm auf Plotter aktiviert?
- [ ] Ankeralarm auf Smartphone aktiviert?
- [ ] Radius korrekt eingestellt?

**Schritt 3: Wetter-Check**
- [ ] Windvorhersage für die Nacht?
- [ ] Tidenvorhersage geprüft?
- [ ] Genügend Wassertiefe bei Niedrigwasser?
- [ ] Fluchtweg im Notfall geplant?

**Schritt 4: Boot vorbereiten**
- [ ] Ankerlaterne gesetzt (360° weiß)?
- [ ] Motorschlüssel griffbereit?
- [ ] Motor in Startbereitschaft (Batterie, Kraftstoff)?
- [ ] Schneidewerkzeug am Bug (Snubber kappen im Notfall)?
- [ ] Funkgerät auf Kanal 16?
- [ ] AIS eingeschaltet?

**Schritt 5: Sturmvorbereitung (bei Starkwind-Prognose)**
- [ ] Doppelsnubber gesetzt?
- [ ] Mehr Kette gefiert (Scope 7:1)?
- [ ] Kellet ausgebracht (optional)?
- [ ] Alle losen Gegenstände gesichert?
- [ ] Luken und Niedergang gesichert?
- [ ] Rettungsweste und Lifeline griffbereit?

### 11.3 Nachtwache (bei unsicheren Bedingungen)

Bei Starkwind, unbekanntem Ankerplatz oder vielen Nachbarbooten:

**Wachintervall: alle 30–60 Minuten**

1. Blick auf GPS/Plotter — Position unverändert?
2. Blick über die Bugrolle — Snubber unter normaler Spannung?
3. Blick auf die Kette — immer noch Durchhang?
4. Windstärke/Richtung — verändert?
5. Nachbarboote — Kollisionsgefahr?

**Alarmsignale (sofortiges Aufstehen):**

- ⚠ Snubber völlig straff (kein Durchhang in der Kette mehr)
- ⚠ Snubber völlig schlaff (Anker hat Grund verloren?)
- ⚠ Boot steht anders als erwartet (Windwechsel? Strömungswechsel?)
- ⚠ Ungewöhnliche Geräusche (Kette über Grund kratzen)
- ⚠ GPS-Ankeralarm ausgelöst
- ⚠ Nachbarboot nähert sich

### 11.4 Morgenroutine (Snubber-Bergen)

1. Kette einholen bis straff (Snubber wird entlastet)
2. Kette auf Kettenstopper oder Winde sichern
3. Kettenhaken aushängen
4. Snubber einpacken
5. Kette weiter einholen, Anker bergen
6. Snubber auf Schäden prüfen (Scheuerstellen, Faserung)
7. Kettenhaken auf Verformung prüfen
8. Snubber trocknen lassen oder unter Deck verstauen

---
---

## 12. Fehlerbild-Atlas

### Fehlerbild 12.1 — Snubber durchgescheuert

**Bezeichnung:** Scheuerbruch des Snubbers an der Bugrolle

**Beschreibung:**
Der Snubber liegt auf der Bugrolle oder am Bugbeschlag auf und wird
durch die ständige Hin- und Herbewegung (Wellenbewegung, Windpendeln)
durchgescheuert. Die äußeren Fasern werden sukzessive durchtrennt,
bis der Snubber bricht.

**Erkennungsmerkmale:**
- Sichtbare Faserung an der Kontaktstelle
- Abflachung des Seilquerschnitts
- Weiße Fasern werden sichtbar (bei dunkel ummantelten Seilen)
- Staubige/pudrige Ablagerungen an der Kontaktstelle

**Ursachen:**
- Fehlender Schamfilschutz
- Verrutschter Schamfilschutz
- Zu enge Bugrolle (Seil klemmt)
- Scharfe Kanten am Bugbeschlag
- Langer Aufenthalt in einer ungeschützten Ankerbucht mit Schwell

**Schweregrad:** KRITISCH — Totaler Lastverlust bei Bruch

**Sofortmaßnahme:**
1. Neuen Snubber setzen (immer Reservesnubber an Bord!)
2. Schamfilschutz anbringen
3. Kontaktstelle am Bugbeschlag überprüfen und ggf. abrunden

**Langfristige Abhilfe:**
- Teflon-Einsatz in der Bugrolle
- Fairlead für saubere Seilführung
- Regelmäßige Kontrolle des Schamfilschutzes

**AYDI-Konfidenz:** visual_high (sichtbare Faserung ist eindeutig erkennbar)

---

### Fehlerbild 12.2 — Kettenhaken ausgehängt

**Bezeichnung:** Unbeabsichtigtes Lösen des Kettenhakens

**Beschreibung:**
Der Kettenhaken hat sich aus der Kette gelöst. Die gesamte Last liegt
auf der Winde. Der Snubber hängt lose im Wasser.

**Erkennungsmerkmale:**
- Snubber lose und schlaff
- Kette straff unter Last (direkt auf Winde)
- Metallisches Rasseln der Kette über die Bugrolle
- Boot liegt unruhiger (keine Dämpfung)

**Ursachen:**
- Offener Haken ohne Sicherung verwendet
- Sicherungsmechanismus nicht eingerastet
- Haken passt nicht zur Kettengröße (zu groß)
- Kette und Snubber haben sich verdreht
- Starker Richtungswechsel (180°-Dreher)

**Schweregrad:** HOCH — Windenschaden möglich

**Sofortmaßnahme:**
1. Kette auf Winde oder Kettenstopper sichern
2. Snubber einholen
3. Kettenhaken prüfen und erneut setzen
4. Sicherung verifizieren

**Langfristige Abhilfe:**
- Auf geschlossenen Haken mit Sicherung umsteigen
- Haken passend zur Kettengröße kaufen
- Anti-Twist-System verwenden (Wirbel/Swivel)

**AYDI-Konfidenz:** visual_high (lose hängender Snubber ist eindeutig)

---

### Fehlerbild 12.3 — Snubber zu kurz / keine Dämpfung

**Bezeichnung:** Unzureichende Snubber-Länge

**Beschreibung:**
Der Snubber ist zu kurz, um die auftretenden Lasten zu dämpfen. Bei
Böen wird der Snubber vollständig durchgedehnt, und die Stoßlast wird
auf die Kette und den Anker übertragen.

**Erkennungsmerkmale:**
- Snubber wird bei Böen „Gitarrensaiten-straff"
- Hörbare Schläge, wenn die Kette durchgestreckt wird
- Boot springt ruckartig an der Kette
- Kette hat keinen Durchhang mehr

**Ursachen:**
- Snubber unterdimensioniert (zu kurz, zu dünn)
- Zu wenig Ketten-Slack nachgefiert
- Windverhältnisse haben sich verschlechtert

**Schweregrad:** MITTEL — Erhöhte Belastung, Ankerversagen möglich

**Sofortmaßnahme:**
1. Mehr Kettendurchhang nachfieren
2. Wenn möglich: längeren Snubber setzen
3. Doppelsnubber-Setup einrichten

**AYDI-Konfidenz:** visual_medium (erfordert Beobachtung bei Böen)

---

### Fehlerbild 12.4 — Nylon-Snubber UV-geschädigt

**Bezeichnung:** UV-Degradation des Nylon-Snubbers

**Beschreibung:**
Der Snubber wurde über eine oder mehrere Saisons intensiver UV-Strahlung
ausgesetzt. Die Nylonfasern sind spröde geworden und haben an Bruchlast
verloren.

**Erkennungsmerkmale:**
- Seil fühlt sich trocken und spröde an (normalerweise geschmeidig)
- Oberfläche ist aufgeraut, fasert aus
- Farbveränderung (Ausbleichen bei farbigen Seilen)
- Pulveriger Abrieb beim Biegen
- Seil knickt statt sich zu biegen

**Ursachen:**
- Permanente Sonneneinstrahlung über Monate
- Snubber dauerhaft auf dem Vordeck ausgelegt
- Kein UV-Schutz (Schlauch, Tuch, Stauung)

**Schweregrad:** HOCH — Bruchlast kann um 30–50 % reduziert sein

**Sofortmaßnahme:**
1. Snubber sofort ersetzen
2. Alten Snubber nur noch als Reserveleine verwenden
3. Neuen Snubber bei Nichtgebrauch UV-geschützt verstauen

**AYDI-Konfidenz:** visual_medium (Sichtprüfung + Tastprüfung nötig)

---

### Fehlerbild 12.5 — Klampe unterdimensioniert

**Bezeichnung:** Snubber-Befestigungsklampe zu klein oder zu schwach

**Beschreibung:**
Die Klampe, an der der Snubber belegt ist, ist für die Ankerlast nicht
dimensioniert. Unter hoher Last verbiegt sich die Klampe, löst sich
aus dem Deck oder der Snubber rutscht ab.

**Erkennungsmerkmale:**
- Klampe ist sichtbar verbogen
- Risse im Deck um die Befestigungsschrauben
- Snubber rutscht von der Klampe
- Deck wölbt sich um die Klampenbefestigung

**Ursachen:**
- Klampe als Zierklampe ausgelegt, nicht als Lastklampe
- Befestigung mit Blechschrauben statt Durchgangsbolzen
- Keine Gegenplatte unter Deck
- Deck an der Stelle zu dünn

**Schweregrad:** KRITISCH — Totaler Lastverlust bei Klampenausriss

**Sofortmaßnahme:**
1. Snubber auf stärkeren Befestigungspunkt umlegen
2. Notfalls: Snubber an der Kette selbst befestigen (Palstek um Kettenglied)
3. Kettenstopper als primären Haltepunkt verwenden

**Langfristige Abhilfe:**
- Klampe durch größere ersetzen
- Durchgangsbolzen mit Gegenplatte installieren
- Deck ggf. verstärken (Laminataufdopplung)

**AYDI-Konfidenz:** visual_high (sichtbare Verformung/Risse)

---

### Fehlerbild 12.6 — Kettendurchhang unzureichend

**Bezeichnung:** Zu wenig Kettendurchhang nach dem Snubber-Setzen

**Beschreibung:**
Nach dem Setzen des Snubbers wurde nicht genügend Kette nachgefiert.
Bei moderater Belastung streckt sich die Kette, und die Last wird
direkt auf die Winde übertragen — der Snubber verliert seine
Schutzfunktion.

**Erkennungsmerkmale:**
- Kette steht unter Spannung (kein sichtbarer Durchhang)
- Kettenlauf liegt am Bugbeschlag an (metallisches Klicken)
- Snubber und Kette sind parallel unter Last
- Windenlast-Anzeige (wenn vorhanden) zeigt Last an

**Ursachen:**
- Vergessen, Kette nachzufieren
- Zu wenig Kette nachgefiert
- Wind hat aufgefrischt → Dehnung hat Slack aufgebraucht

**Schweregrad:** MITTEL — Snubber wirkungslos, Windenbelastung

**Sofortmaßnahme:**
1. 2–4 m Kette nachfieren
2. Erneut prüfen, dass Kette Durchhang hat

**AYDI-Konfidenz:** visual_high (sichtbar ob Durchhang vorhanden)

---

### Fehlerbild 12.7 — Snubber verdreht/verdrillt

**Bezeichnung:** Torsion und Kinking des Snubbers

**Beschreibung:**
Der Snubber (besonders 3-Strand Nylon) hat sich durch Richtungswechsel
und Schwoien verdreht und Kinken gebildet. Kinken reduzieren die
Bruchlast und verhindern gleichmäßige Dehnung.

**Erkennungsmerkmale:**
- Sichtbare Schlaufen und Kinken im Snubber
- Snubber verdrillt sich um den Kettenhaken
- Ungleichmäßige Lastverteilung (eine Seite straffer)

**Ursachen:**
- 3-Strand Nylon neigt zum Verdrehen unter Last
- Fehlender Wirbelschäkel (Swivel)
- Boot hat sich mehrfach um 360° gedreht (Tidenwechsel)

**Schweregrad:** MITTEL — Reduzierte Bruchlast, Hakenaushängen möglich

**Sofortmaßnahme:**
1. Snubber entlasten (Kette einholen)
2. Kinken ausdrehen
3. Ggf. Wirbelschäkel einsetzen
4. Bei starker Kinkenbildung: 8-Plait Nylon verwenden

**AYDI-Konfidenz:** visual_high (Kinken sind klar sichtbar)

---

### Fehlerbild 12.8 — Kettenhaken korrodiert

**Bezeichnung:** Korrosion am Kettenhaken

**Beschreibung:**
Der Kettenhaken zeigt Korrosionserscheinungen — insbesondere am
Federverriegelungsmechanismus oder an Schweißnähten.

**Erkennungsmerkmale:**
- Rostbraune Verfärbungen am Haken
- Federverriegelung lässt sich schwer bewegen
- Oberfläche rau und pitting (Lochfraß)
- Tea-Staining (gelbbraune Flecken auf Edelstahl)

**Ursachen:**
- Falscher Stahl (304 statt 316L)
- Kontaktkorrosion (ungleiche Metalle)
- Beschädigte Oberfläche (Kratzer durchbrechen Passivschicht)
- Reinigungsmittel-Rückstände (chlorhaltig)

**Schweregrad:** HOCH — Tragfähigkeitsverlust, Versagen möglich

**Sofortmaßnahme:**
1. Haken reinigen und auf Rissbildung prüfen
2. Leichtgängigkeit der Sicherung prüfen
3. Bei sichtbaren Rissen oder Pitting: sofort ersetzen

**AYDI-Konfidenz:** visual_medium (Oberflächenkorrosion vs. Tiefenkorrosion
nicht immer visuell unterscheidbar)

---

### Fehlerbild 12.9 — Falsche Kettengröße am Haken

**Bezeichnung:** Kettenhaken passt nicht zur Kette

**Beschreibung:**
Der Kettenhaken ist für eine andere Kettengröße ausgelegt als die
verwendete Ankerkette. Der Haken sitzt entweder zu locker (kann sich
aushängen) oder zu eng (klemmt und lässt sich nicht richtig einsetzen).

**Erkennungsmerkmale:**
- Haken wackelt im Kettenglied (zu groß)
- Haken klemmt beim Einsetzen (zu klein)
- Haken sitzt nicht plan im Kettenglied

**Ursachen:**
- Falsches Modell gekauft
- Kette nachträglich gewechselt (andere Größe)
- Metrische vs. imperiale Kettenmaße verwechselt

**Schweregrad:** HOCH — Aushängen oder Klemmen unter Last

**Sofortmaßnahme:**
1. Korrekte Kettengröße messen (Materialdurchmesser!)
2. Passenden Haken beschaffen

**AYDI-Konfidenz:** visual_high (Passgenauigkeit visuell erkennbar)

---

### Fehlerbild 12.10 — Mooring Compensator erschöpft

**Bezeichnung:** Ermüdung des Gummielements im Mooring Compensator

**Beschreibung:**
Das Gummielement eines Dyneema/Gummi-Snubbers oder Mooring Compensators
hat seine Elastizität verloren. Das System federt nicht mehr zurück
und bietet keine Dämpfung mehr.

**Erkennungsmerkmale:**
- Gummielement ist permanent gedehnt (keine Rückfederung)
- Sichtbare Risse oder Rissbildung im Gummi
- Gummi fühlt sich hart und spröde an
- System ist deutlich länger als im Neuzustand

**Ursachen:**
- Alterung (3–8 Jahre je nach Qualität)
- Dauerhafte UV-Belastung
- Überlastung (über WLL hinaus belastet)
- Ozon-Einwirkung (beschleunigt Gummi-Alterung)

**Schweregrad:** MITTEL — Dämpfungsverlust, System noch haltbar

**Sofortmaßnahme:**
1. Auf Nylon-Snubber umsteigen
2. Compensator als Reserveleine verwenden

**AYDI-Konfidenz:** visual_medium (Beurteilung der Rest-Elastizität
erfordert Belastungstest)

---

### Fehlerbild 12.11 — Bridle-Leinen ungleich lang

**Bezeichnung:** Asymmetrie im Katamaran-Bridle

**Beschreibung:**
Die beiden Bridle-Leinen haben unterschiedliche Längen, sodass ein
Rumpf mehr Last trägt als der andere.

**Erkennungsmerkmale:**
- Boot steht schräg am Anker (ein Rumpf weiter vorne)
- Eine Bridle-Leine ist straff, die andere hat Durchhang
- Verstärktes Segeln am Anker in eine Richtung

**Ursachen:**
- Ungleich abgemessene Leinen
- Ungleiche Dehnung (ein Leine älter/abgenutzter)
- Klampen sind nicht symmetrisch positioniert

**Schweregrad:** NIEDRIG — Komfort und Gleichmäßigkeit beeinträchtigt

**Sofortmaßnahme:**
1. Leinen nachmessen und angleichen
2. Gleiches Material/Alter für beide Leinen verwenden

**AYDI-Konfidenz:** visual_high (Asymmetrie deutlich sichtbar)

---

### Fehlerbild 12.12 — Kettenstopper nicht arretiert

**Bezeichnung:** Kettenstopper nicht korrekt verriegelt

**Beschreibung:**
Der Kettenstopper wurde nicht richtig arretiert — die Wippe oder
der Bolzen sind nicht eingerastet. Bei Last könnte die Kette
durchrutschen.

**Erkennungsmerkmale:**
- Wippe steht nicht vollständig in Arretierungsposition
- Sicherungsbolzen fehlt oder ist nicht eingesetzt
- Federverriegelung hat nicht eingerastet (kein Klick-Geräusch)

**Ursachen:**
- Bedienungsfehler (Eile, Dunkelheit)
- Korrodierter Verriegelungsmechanismus
- Falsches Kettenglied unter der Wippe (Kette liegt schräg)

**Schweregrad:** HOCH — Kette kann unter Last durchrutschen

**Sofortmaßnahme:**
1. Kettenstopper korrekt arretieren
2. Visuell und taktil bestätigen (Klick-Geräusch)
3. Bei defekter Verriegelung: Snubber als primäre Sicherung verwenden

**AYDI-Konfidenz:** visual_high (Arretierungsposition eindeutig sichtbar)

---
---

## 13. Troubleshooting

### 13.1 Entscheidungsbaum — Snubber setzt auf Klampe nicht richtig

```
PROBLEM: Snubber sitzt nicht sicher auf der Klampe
│
├─ Snubber-Durchmesser zu groß für die Klampe?
│   ├─ JA → Kleinere Klampe? → Größere Klampe installieren
│   │        oder dünneren Snubber verwenden (Bruchlast prüfen!)
│   └─ NEIN ↓
│
├─ Snubber-Durchmesser zu klein für die Klampe?
│   ├─ JA → Snubber rutscht von der Klampe → Mehr Windungen,
│   │        dickeren Snubber verwenden
│   └─ NEIN ↓
│
├─ Belegtechnik korrekt? (Kreuzschlag + Kopfschlag)
│   ├─ NEIN → Korrekte Belegtechnik anwenden
│   └─ JA ↓
│
├─ Klampe verschlissen/abgerundet?
│   ├─ JA → Klampe ersetzen
│   └─ NEIN ↓
│
└─ Snubber nass und glitschig?
    ├─ JA → Mehr Windungen, ggf. Sicherungsschlag
    └─ NEIN → Klampe und Snubber-Material überprüfen
```

### 13.2 Entscheidungsbaum — Snubber bricht / reißt

```
PROBLEM: Snubber ist gebrochen oder gerissen
│
├─ Bruchstelle an der Bugrolle / Kontaktstelle?
│   ├─ JA → Scheuerbruch
│   │   ├─ Schamfilschutz nachrüsten
│   │   ├─ Bugrolle auf scharfe Kanten prüfen
│   │   └─ Fairlead installieren
│   └─ NEIN ↓
│
├─ Bruchstelle am Spleiß / Knoten?
│   ├─ JA → Verbindungsfehler
│   │   ├─ Spleiß korrekt ausgeführt? (min. 5 Stiche)
│   │   ├─ Knoten korrekt? (Palstek, nicht Webleinstek)
│   │   └─ Kausche verwendet? (reduziert Knicklast)
│   └─ NEIN ↓
│
├─ Bruchstelle im freien Bereich?
│   ├─ JA → Material-/Überlastungsversagen
│   │   ├─ Snubber UV-geschädigt? → Ersetzen
│   │   ├─ Snubber unterdimensioniert? → Dickeren verwenden
│   │   └─ Extrembelastung? → Doppelsnubber verwenden
│   └─ NEIN ↓
│
└─ Bruchstelle am Kettenhaken?
    ├─ JA → Haken-Verbindungsproblem
    │   ├─ Haken scharfkantig? → Haken entgraten oder ersetzen
    │   └─ Snubber-Auge zu klein? → Größere Kausche
    └─ NEIN → Gesamtsystem überprüfen
```

### 13.3 Entscheidungsbaum — Kettenhaken löst sich wiederholt

```
PROBLEM: Kettenhaken löst sich regelmäßig aus der Kette
│
├─ Haken für korrekte Kettengröße?
│   ├─ NEIN → Korrekten Haken beschaffen
│   └─ JA ↓
│
├─ Sicherungsmechanismus funktionsfähig?
│   ├─ NEIN → Haken warten (WD-40, Fett) oder ersetzen
│   └─ JA ↓
│
├─ Haken korrekt eingehängt? (Öffnung in Zugrichtung?)
│   ├─ NEIN → Haken in korrekter Orientierung einsetzen
│   └─ JA ↓
│
├─ Boot dreht sich häufig (Tidenwechsel)?
│   ├─ JA → Wirbelschäkel zwischen Haken und Snubber
│   │        oder Haken mit integriertem Wirbel verwenden
│   └─ NEIN ↓
│
└─ Kette hat ungewöhnliche Glieder (Verbindungsglied)?
    ├─ JA → Haken auf normalem Kettenglied setzen,
    │        Verbindungsglieder meiden
    └─ NEIN → Auf Klauenhaken (Devil's Claw) umsteigen
```

### 13.4 Entscheidungsbaum — Laute Geräusche trotz Snubber

```
PROBLEM: Metallische Geräusche trotz gesetztem Snubber
│
├─ Kette hat keinen Durchhang?
│   ├─ JA → Mehr Kette nachfieren (2–4 m)
│   └─ NEIN ↓
│
├─ Kette berührt die Bugrolle?
│   ├─ JA → Mehr Durchhang, Kettenhaken weiter vom Bug
│   │        entfernt einsetzen
│   └─ NEIN ↓
│
├─ Kette schlägt im Kettenkasten?
│   ├─ JA → Kette im Kettenkasten fixieren (Leine um Kette)
│   │        oder Schaumstoff-Polsterung im Kasten
│   └─ NEIN ↓
│
├─ Kette schleift am Bug/Anker-Befestigung?
│   ├─ JA → Bugrolle/Ankerrolle auf freien Lauf prüfen
│   └─ NEIN ↓
│
└─ Geräusch kommt von der Kette am Grund?
    ├─ JA → Normal bei Fels/Kies-Grund
    │        Kellet kann helfen, Kette vom Grund zu heben
    └─ NEIN → Geräuschquelle genauer lokalisieren
```

### 13.5 Entscheidungsbaum — Katamaran segelt stark am Anker

```
PROBLEM: Katamaran pendelt stark am Anker
│
├─ Bridle verwendet?
│   ├─ NEIN → Bridle setzen (primäre Maßnahme!)
│   └─ JA ↓
│
├─ Bridle-Leinen gleich lang?
│   ├─ NEIN → Angleichen
│   └─ JA ↓
│
├─ Bridle-Winkel > 60°?
│   ├─ NEIN → Leinen verlängern für breiteren Winkel
│   └─ JA ↓
│
├─ Segel an Deck? (Lazy Bag, Genua nicht gerollt)
│   ├─ JA → Alles Segeltuch bergen/einrollen
│   └─ NEIN ↓
│
├─ Bimini/Sprayhood offen?
│   ├─ JA → Wenn möglich, schließen/abnehmen
│   └─ NEIN ↓
│
├─ Kellet am Bridle-V-Punkt?
│   ├─ NEIN → Kellet (5–10 kg) am V-Punkt setzen
│   └─ JA ↓
│
├─ Genügend Kette? (Scope ≥ 5:1)
│   ├─ NEIN → Mehr Kette fieren
│   └─ JA ↓
│
└─ Flopper-Stopper verfügbar?
    ├─ JA → Flopper-Stopper ausbringen
    └─ NEIN → Pendeln akzeptieren oder Ankerplatz wechseln
```

---
---

## 14. Entscheidungshilfe

### 14.1 Snubber-Auswahl nach Bootstyp

```
Welcher Bootstyp?
│
├─ Segelboot (Einrumpf)
│   ├─ < 10 m → Nylon 3-Strand 14 mm, 5–6 m
│   ├─ 10–14 m → Nylon 3-Strand 16 mm, 7–8 m
│   ├─ 14–18 m → Nylon 3-Strand 18–20 mm, 9–12 m
│   └─ > 18 m → Nylon 3-Strand 22–24 mm, 12–15 m + Reserve
│
├─ Motoryacht
│   ├─ < 10 m → Nylon 8-Plait 14 mm oder Dyneema/Gummi
│   ├─ 10–14 m → Nylon 8-Plait 16 mm, 6–8 m
│   └─ > 14 m → Nylon 3-Strand 18–22 mm, 8–12 m
│
├─ Katamaran
│   ├─ < 12 m → Bridle 2× 14 mm, je 7 m
│   ├─ 12–16 m → Bridle 2× 16–18 mm, je 8–9 m
│   └─ > 16 m → Bridle 2× 20 mm, je 10–12 m
│
└─ Multihull (Trimaran)
    ├─ Ähnlich Einrumpf (Snubber am Hauptrumpf)
    └─ Bei breitem Trimaran: ggf. Bridle
```

### 14.2 Kettenhaken-Auswahl

```
Budget und Anforderungen?
│
├─ Preis-Leistung (< 80 EUR)
│   └─ Wichard 2484 (8–10 mm) → 72 EUR
│
├─ Standard (80–110 EUR)
│   ├─ Mantus Chain Hook M → 99 EUR (Empfehlung)
│   └─ Kong Anchor Chain Hook 10 → 85 EUR
│
├─ Professionell (> 110 EUR)
│   ├─ Yale Chain Grab 3/8" → 109 EUR
│   └─ Ultra Hook 10 → 115 EUR
│
└─ Katamaran (Bridle-System)
    └─ Mantus Bridle Hook Set → 179 EUR (2× Haken + Schäkel)
```

---
---

## 15. FAQ

### FAQ 15.1 — Brauche ich einen Snubber, wenn ich eine Kette-Leine-Kombination habe?

**Frage:** Ich ankere mit 20 m Kette + 30 m Nylon-Leine. Brauche ich
trotzdem einen Snubber?

**Antwort:** Nein, bei einer Kette-Leine-Kombination übernimmt die
Nylon-Leine die Dämpfungsfunktion. Allerdings empfiehlt sich ein
Kettenstopper für den Kettenanteil, um die Winde zu entlasten.
Der Übergang Kette-Leine muss mit einem ordentlichen Spleiß oder
einem hochwertigen Schäkel ausgeführt sein.

---

### FAQ 15.2 — Wie oft muss ich den Snubber ersetzen?

**Frage:** Wie lange hält ein Nylon-Snubber?

**Antwort:** Bei regelmäßiger Nutzung (Fahrtensegeln, 50–100 Ankernächte
pro Saison) hält ein Nylon-Snubber 3–5 Jahre. Entscheidend ist der
UV-Schutz und die Vermeidung von Scheuerung. Jährliche Inspektion:
Seil biegen — wenn es knickt statt sich rund zu biegen oder wenn Fasern
sichtbar aufbrechen, sofort ersetzen.

---

### FAQ 15.3 — Kann ich den Snubber auch als Mooringleine verwenden?

**Frage:** Kann ich den Snubber am Steg als Festmacherleine nutzen?

**Antwort:** Grundsätzlich ja — Nylon-Snubber sind hervorragende
Festmacherleinen, da sie die gleiche Dämpfungsfunktion bieten. Allerdings
verschleißt der Snubber am Steg schneller (Klampen, Dalben, Poller sind
scheuernde Kontaktstellen). Empfehlung: Separate Leinen für Steg und
Anker verwenden.

---

### FAQ 15.4 — Welcher Kettenhaken für DIN 766 vs. ISO 4565?

**Frage:** Meine Kette ist DIN 766 (kurze Glieder). Passen alle Haken?

**Antwort:** Die meisten Kettenhaken sind für ISO/DIN-Kurzgliederkette
(DIN 766) ausgelegt. Achtung bei Langgliederkette (DIN 763) oder
Ankerkette nach speziellen Normen (BBB Chain, US-Standard) — hier kann
der Haken nicht greifen oder zu locker sitzen. Vor dem Kauf: Kettentyp
und Gliedmaße (Innenlänge × Innenbreite) mit den Haken-Spezifikationen
abgleichen.

---

### FAQ 15.5 — Snubber bei Starkwind: Einer oder zwei?

**Frage:** Ab welcher Windstärke sollte ich einen zweiten Snubber setzen?

**Antwort:** Ab 30 Knoten Wind (Beaufort 7) ist ein Doppelsnubber-Setup
empfehlenswert. Der zweite Snubber sollte 10–15 % länger sein als der
erste, damit er erst bei extremer Dehnung des ersten Snubbers zum Tragen
kommt. Beide Snubber an verschiedenen Klampen befestigen.

---

### FAQ 15.6 — Muss der Snubber ins Wasser tauchen?

**Frage:** Soll der Snubber über oder unter Wasser verlaufen?

**Antwort:** Der Snubber verläuft typischerweise vom Bug-Klampe über die
Bugrolle ins Wasser zum Kettenhaken, der an der Kette unter Wasser
hängt. Ein kurzes Stück des Snubbers ist im Wasser — das ist normal
und sogar vorteilhaft (das Wasser kühlt den Nylon bei Belastung).
Wichtig ist, dass der Schamfilschutz die Stelle an der Bugrolle
abdeckt, wo der Snubber vom Trockenen ins Nasse übergeht.

---

### FAQ 15.7 — Kettenstopper ODER Snubber — oder beides?

**Frage:** Reicht ein Kettenstopper, oder brauche ich auch einen Snubber?

**Antwort:** Beide! Der Kettenstopper sichert die Kette mechanisch und
entlastet die Winde. Der Snubber dämpft dynamische Lasten und
reduziert Geräusche. Ohne Snubber übertragen sich alle Stoßlasten
über den Kettenstopper direkt auf die Decksbefestigung — das kann auf
Dauer zu Deckschäden führen.

---

### FAQ 15.8 — Warum nicht einfach mehr Kette fieren?

**Frage:** Kann ich statt eines Snubbers einfach mehr Kette ausbringen?

**Antwort:** Mehr Kette verbessert den Katarakt und die Haltekraft, aber
sie ersetzt keinen Snubber. Auch bei Scope 10:1 bleibt die Kette
unelastisch — die Stoßlasten werden lediglich etwas durch das
Kettengewicht gedämpft. Außerdem vergrößert mehr Kette den
Schwoikreis erheblich (in engen Buchten problematisch) und belastet
die Winde stärker.

---

### FAQ 15.9 — Augspleiß oder Knoten am Snubber?

**Frage:** Soll ich den Snubber spleißen oder einen Knoten machen?

**Antwort:** Spleißen ist immer vorzuziehen:
- Augspleiß: 90–95 % Restbruchlast
- Palstek: 60–70 % Restbruchlast
- Achtknoten: 65–75 % Restbruchlast
- Webleinstek: 50–60 % Restbruchlast (zudem rutschgefährdet)

Ein gespleißter Snubber mit Kausche ist die professionelle Lösung.
Wer nicht spleißen kann: Segelmaker oder Takelage-Fachbetrieb
beauftragen (20–40 EUR pro Spleiß).

---

### FAQ 15.10 — Kellet: Wann sinnvoll, wann nicht?

**Frage:** Wann lohnt sich ein Kellet/Ankergewicht?

**Antwort:** Ein Kellet ist sinnvoll bei:
- Begrenzter Kettenlänge (kann keinen größeren Scope fieren)
- Engem Ankerplatz (Schwoikreis reduzieren)
- Katamaran (reduziert Segeln am Anker)
- Schlick/Lehm-Grund (flacherer Winkel verbessert Halten)

Nicht sinnvoll bei:
- Ausreichend Kettenlänge und Platz
- Tiefen Ankerbuchten (> 15 m — Kellet zu schwer)
- Kurzen Ankerstopps (Aufwand steht nicht im Verhältnis)

---

### FAQ 15.11 — Snubber-Länge für Nachtankern im Mittelmeer?

**Frage:** Wie lang sollte der Snubber für eine typische Mittelmeer-Nacht sein?

**Antwort:** Im Mittelmeer herrschen nachts oft thermische Fallwinde
(Katabatik), die plötzlich 25–30 Knoten erreichen können. Für ein
typisches 12-m-Boot empfehlen wir mindestens 8 m Snubber, besser
10 m. Der Kettendurchhang sollte 3 m betragen. Immer einen
Reservesnubber griffbereit haben.

---

### FAQ 15.12 — Wie bewahre ich den Snubber auf?

**Frage:** Wie lagere ich den Snubber richtig?

**Antwort:**
1. Nach Gebrauch mit Süßwasser spülen (Salzreste entfernen)
2. Trocknen lassen (nicht in der Sonne!)
3. Lose aufgeschossen in einem UV-dichten Beutel verstauen
4. Nicht knicken oder unter schweren Gegenständen lagern
5. Nicht neben Säuren, Bleichmitteln oder Lösungsmitteln lagern
6. Jährlich auf UV-Schäden und Abrieb prüfen

---

### FAQ 15.13 — Kann ich einen zu dicken Snubber verwenden?

**Frage:** Schadet ein überdimensionierter Snubber?

**Antwort:** Ein zu dicker Snubber ist steifer und dehnt sich weniger.
Die Dämpfungswirkung ist geringer als bei einem korrekt dimensionierten
Snubber. Außerdem passt er möglicherweise nicht auf die Klampe und
ist schwerer zu handhaben. Faustformel: Snubber-Durchmesser maximal
3× Kettendurchmesser.

---

### FAQ 15.14 — Snubber bei Heckanker?

**Frage:** Brauche ich auch am Heckanker einen Snubber?

**Antwort:** Ja, wenn der Heckanker mit Kette ausgeführt ist. Besonders
wichtig bei Mittelmeer-Moorings (Bug zum Steg, Heck am Anker oder an
der Mooringleine). Der Heckanker-Snubber kann etwas kleiner
dimensioniert werden, da der Heckanker typischerweise nur 50 % der
Belastung des Bugankers trägt.

---

### FAQ 15.15 — Was ist der Unterschied zwischen Snubber und Bridle?

**Frage:** Snubber, Bridle — ist das nicht dasselbe?

**Antwort:**
- **Snubber**: Einzelleine vom Bug zur Kette → Hauptfunktion: Dämpfung
- **Bridle**: Zwei Leinen von beiden Seiten des Bugs → Hauptfunktion:
  Stabilisierung + Dämpfung (primär bei Katamaranen)
Ein Bridle ist immer auch ein Snubber, aber ein Snubber ist nicht immer
ein Bridle.

---

### FAQ 15.16 — Snubber für Dauerlieger am Bojenfeld?

**Frage:** Brauche ich einen Snubber, wenn ich dauerhaft an einer Boje liege?

**Antwort:** Unbedingt! Bojenlieger sind oft stärkerem Schwell und Strom
ausgesetzt als Ankerer in geschützten Buchten. Ein Mooring Compensator
oder Nylon-Snubber zwischen Mooringleine und Boot ist Pflicht.
Empfehlung: 2× Mooring Compensator (je eine pro Leine) plus separate
Sicherungsleine.

---

### FAQ 15.17 — Kann Dyneema als Snubber-Material dienen?

**Frage:** Dyneema ist doch viel stärker als Nylon — warum nicht als Snubber?

**Antwort:** Dyneema (HMPE) hat eine Dehnung von nur 1–2 % — praktisch
null Stoßdämpfung. Als reiner Snubber ist Dyneema ungeeignet. Dyneema
wird nur in Kombination mit einem Gummi-Dämpfungselement verwendet
(siehe Dyneema/Gummi-Hybrid in Kapitel 3.3). Die Dyneema-Leinen in
einem Bridle-System können unelastisch sein, wenn ein zentraler
Nylon-Snubber die Dämpfung übernimmt.

---

### FAQ 15.18 — Wieviel kostet ein komplettes Snubber-Setup?

**Frage:** Was muss ich für ein komplettes System ausgeben?

**Antwort:** Kostenübersicht für ein 12-m-Segelboot:

| Komponente | Budget | Standard | Premium |
|-----------|--------|----------|---------|
| Snubber (Nylon 16 mm, 8 m) | 35 EUR | 50 EUR | 70 EUR |
| Kettenhaken | 55 EUR | 99 EUR | 139 EUR |
| Schamfilschutz | 3 EUR | 15 EUR | 40 EUR |
| Reservesnubber | 35 EUR | 50 EUR | 70 EUR |
| Kettenstopper | — | 159 EUR | 229 EUR |
| **Gesamt** | **128 EUR** | **373 EUR** | **548 EUR** |

---

### FAQ 15.19 — Snubber im Sturm verloren — was tun?

**Frage:** Mein Snubber ist in einem Sturm gerissen. Was sind die
Sofortmaßnahmen?

**Antwort:**
1. Ruhe bewahren — die Kette hält noch (auf Winde/Kettenstopper)
2. Reservesnubber setzen (sollte immer an Bord sein!)
3. Kein Reservesnubber? Improvisieren:
   - Längere Festmacherleine als Snubber verwenden
   - Nylon-Fallleine (Genua-Fall) vom Mast zum Ketten
   - Fenderleine als Not-Snubber
4. Mehr Kette fieren (erhöht den Katarakt)
5. Motor in Bereitschaft (bei Ankerversagen sofort starten)
6. GPS-Ankeralarm kontrollieren

---

### FAQ 15.20 — Snubber und Tidenhub — Besonderheiten?

**Frage:** Wie beeinflusst der Tidenhub den Snubber?

**Antwort:** Bei starkem Tidenhub (Nordsee: 2–4 m, Bretagne: 8–12 m)
ändert sich die effektive Kettenlänge und der Abgangswinkel erheblich.
Der Snubber muss lang genug sein, um den gesamten Tidenbereich
abzudecken. Bei Niedrigwasser ist der Scope kleiner und die Last
höher. Empfehlung: Kettenlänge für die geringste Wassertiefe berechnen
und Snubber-Durchhang entsprechend anpassen.

---

### FAQ 15.21 — Snubber an Ankerball/Ankerlicht befestigen?

**Frage:** Kann ich die Ankerlicht-Leine am Snubber befestigen?

**Antwort:** Nein! Die Ankerlicht-Leine (oder Ankerkugel-Leine) darf
nicht am Snubber befestigt werden, da der Snubber sich dehnt und die
Lampe/Kugel dann unkontrolliert bewegt. Das Ankerlicht gehört an den
Mast oder Bugkorb — fest montiert, unabhängig vom Ankersystem.

---

### FAQ 15.22 — Snubber und elektrische Ankerwinden-Fernbedienung?

**Frage:** Ich bediene meine Winde per Funk-Fernbedienung. Wie setze ich
den Snubber?

**Antwort:** Die Fernbedienung erleichtert das Snubber-Setzen erheblich:
1. Kette fieren bis gewünschte Länge (Fernbedienung)
2. Winde stoppen, Kettenstopper setzen
3. Snubber und Kettenhaken über die Bugrolle einsetzen
4. Per Fernbedienung langsam 2–4 m Kette nachfieren
5. Boot fällt in den Snubber — fertig

---

### FAQ 15.23 — Bridle-Länge bei Katamaran mit Bowsprit?

**Frage:** Mein Katamaran hat einen Bowsprit. Wie beeinflusst das die
Bridle-Länge?

**Antwort:** Der Bowsprit verlängert den Abstand vom Kettenablaufpunkt
zu den Bug-Klampen. Die Bridle-Leinen müssen entsprechend länger sein.
Faustregel: Bridle-Standardlänge + Bowsprit-Länge + 1 m.
Beispiel: 12-m-Kat mit 2 m Bowsprit → 8 m + 2 m + 1 m = 11 m Bridle.

---

### FAQ 15.24 — Gibt es Snubber mit integriertem Kettenhaken?

**Frage:** Gibt es fertige Snubber-Sets mit Haken?

**Antwort:** Ja, mehrere Hersteller bieten Komplettsysteme an:

| Hersteller | Produkt | Für Kette | Snubber | Haken | Preis |
|-----------|---------|-----------|---------|-------|-------|
| Mantus | Snubber Kit | 8 mm | 14 mm × 6 m | Mantus Hook S | 149 EUR |
| Mantus | Snubber Kit | 10 mm | 16 mm × 8 m | Mantus Hook M | 189 EUR |
| Mantus | Snubber Kit | 12 mm | 18 mm × 10 m | Mantus Hook L | 229 EUR |
| Wichard | Gypsea Kit | 8–10 mm | Dyneema/Gummi | Wichard 2484 | 159 EUR |
| SailRite | Snubber Set | 8 mm | 14 mm × 6 m | Yale Grab | 129 EUR |
| SailRite | Snubber Set | 10 mm | 16 mm × 8 m | Yale Grab | 169 EUR |

---

### FAQ 15.25 — Snubber-Pflege auf Langfahrt

**Frage:** Wie pflege ich den Snubber auf einer Langfahrt (6+ Monate)?

**Antwort:** Auf Langfahrt ist der Snubber nahezu täglich im Einsatz:
1. Alle 2 Wochen mit Süßwasser spülen
2. Monatlich auf Scheuerstellen inspizieren
3. Schamfilschutz regelmäßig kontrollieren und ggf. erneuern
4. Snubber halbjährlich um 180° drehen (Scheuerstelle verlagern)
5. Reservesnubber mitführen (identische Spezifikation)
6. Nach 2 Jahren auf Langfahrt: Snubber ersetzen (UV + Abrieb)
7. Kettenhaken vierteljährlich auf Korrosion prüfen
8. Spleiße auf Aufdröseln prüfen

---

### FAQ 15.26 — Snubber bei Ankerversagen — hilft er?

**Frage:** Kann ein Snubber Ankerversagen (Dragging) verhindern?

**Antwort:** Indirekt ja. Ein Snubber absorbiert die Stoßlasten, die den
Anker bei Böen aus dem Grund reißen können. Ein Boot mit Snubber zieht
gleichmäßig am Anker, ein Boot ohne Snubber ruckt mit Spitzenlasten,
die das 5–10-fache der statischen Last betragen können. Diese Rucke
sind die häufigste Ursache für das Losbrechen eines gut gesetzten Ankers.

---

### FAQ 15.27 — Snubber und Korallengrund?

**Frage:** Schadet der Snubber auf Korallengrund?

**Antwort:** Der Snubber selbst berührt den Korallenboden nicht — er
verläuft nur zwischen Bug und Kette über Wasser und im oberen
Wasserbereich. Allerdings kann die durchhängende Kette (Slack) auf
Korallen scheuern. In Korallengebieten: weniger Kettendurchhang,
dafür längeren Snubber verwenden.

---

### FAQ 15.28 — Snubber bei Mehrfach-Ankern (Stern-zu-Pier)?

**Frage:** Wie setze ich den Snubber bei einer Mittelmeer-Mooring
(Bug zur Pier, Heckanker im Wasser)?

**Antwort:** Bei Stern-zu-Pier-Ankerung wird der Buganker typischerweise
100–150 m achteraus geworfen, bevor das Boot rückwärts an den Steg
fährt. Der Snubber wird wie beim normalen Ankern eingesetzt:
1. Kette auf gewünschte Länge fieren
2. Snubber über Heck-Klampe und Kettenhaken setzen
3. Kettendurchhang nachfieren
4. Festmacherleinen zum Steg belegen
Der Snubber ist hier besonders wichtig, da der Heckanker hohen
Wechsellasten durch vorbeifahrende Boote im Hafen ausgesetzt ist.

---

### FAQ 15.29 — Warum kein Polypropylen als Snubber?

**Frage:** Polypropylen schwimmt und wäre doch praktisch als Snubber?

**Antwort:** Polypropylen (PP) hat zwar den Vorteil, dass es schwimmt
und damit die Bugrolle nicht belastet, aber es ist als Snubber-Material
völlig ungeeignet:
- Dehnung nur 5–8 % (viel weniger als Nylon mit 15–25 %)
- UV-Empfindlichkeit noch höher als bei Nylon
- Geringe Bruchlast im Vergleich zu Nylon
- Wird unter Sonneneinstrahlung schnell spröde
- Schlechte Abriebfestigkeit
PP wird nur als schwimmende Schleppleine oder als Beiboot-Leine
eingesetzt, niemals als Snubber.

---

### FAQ 15.30 — Kann ich einen gebrauchten Snubber kaufen?

**Frage:** Auf dem Gebrauchtmarkt gibt es günstige Nylon-Seile — taugen
die als Snubber?

**Antwort:** Grundsätzlich raten wir davon ab. Die Restbruchlast eines
gebrauchten Nylon-Seils ist ohne Labortest nicht zuverlässig zu
bestimmen. UV-Degradation und Ermüdung durch dynamische Belastung
können die Bruchlast um 30–60 % reduziert haben, ohne dass dies
äußerlich erkennbar ist. Ein neuer Snubber kostet 30–80 EUR — das
ist eine Sicherheitsinvestition, bei der nicht gespart werden sollte.

---

### FAQ 15.31 — Wie teste ich die Restfestigkeit meines Snubbers?

**Frage:** Wie kann ich prüfen, ob mein Snubber noch sicher ist?

**Antwort:** Einfache Feldtests:
1. **Biegetest**: Seil knicken — formt es einen runden Bogen (gut)
   oder knickt es scharf (schlecht)?
2. **Fasertest**: Seiloberfläche mit Fingernagel kratzen — lösen sich
   Fasern leicht (schlecht)?
3. **Dehntest**: Seil von Hand dehnen — federt es elastisch zurück
   (gut) oder bleibt es gedehnt (schlecht)?
4. **Farbtest**: Deutliches Ausbleichen deutet auf UV-Schaden hin.
5. **Geruchstest**: Muffiger Geruch deutet auf innere Schimmelbildung
   durch Wasseraufnahme hin.

Im Zweifel: Ersetzen. 50 EUR für einen neuen Snubber sind billiger
als die Konsequenzen eines Snubber-Versagens.

---

### FAQ 15.32 — Snubber und Ankertrossen — historische Entwicklung

**Frage:** Wie hat sich die Snubber-Technologie über die Jahre verändert?

**Antwort:** Die Geschichte in Kurzform:
- **Vor 1960**: Ankertau aus Naturfasern (Hanf, Manila) — elastisch,
  kein separater Snubber nötig
- **1960–1980**: Übergang zu Vollketten-Systemen, erste Snubber aus
  Nylon, meist einfache Leinen mit Knoten
- **1980–2000**: Professionalisierung — gespleißte Snubber, erste
  Kettenhaken mit Sicherung, Schamfilschutz wird Standard
- **2000–2015**: Dyneema/Gummi-Hybrid-Systeme, spezialisierte Kettenhaken
  (Mantus, Kong), Devil's Claw wird populär
- **2015–heute**: Komplettsysteme, integrierte Kettenstopper,
  Bridle-Systeme für die wachsende Katamaran-Flotte

---

### FAQ 15.33 — Snubber und Versicherung — Relevanz?

**Frage:** Hat ein fehlender Snubber Auswirkungen auf den
Versicherungsschutz?

**Antwort:** Direkt ist ein Snubber in keiner uns bekannten
Versicherungspolice als Pflichtausrüstung genannt. Indirekt kann
ein fehlender Snubber aber bei einem Schadensfall (z. B. Ankerversagen
führt zu Strandung) als Mitschuld gewertet werden: „Der Versicherte
hat nicht alle zumutbaren Maßnahmen zur Schadensvermeidung getroffen."
Die ABYC-Empfehlung H-40, Herstellerhandbücher der Ankerwinden und
die allgemeine gute Seemannschaft verlangen einen Snubber — ein
fehlender Snubber könnte als Fahrlässigkeit ausgelegt werden.

---

### FAQ 15.34 — Snubber bei Swing-Mooring (Boje)?

**Frage:** Wie befestige ich den Snubber an einer Boje?

**Antwort:** Bei einer Festmacherboje wird der Snubber anders eingesetzt
als beim Ankern:
1. Hauptleine zur Boje belegen (Palstek oder Spleiß um den Bojenring)
2. Snubber als separate Leine vom Bug zur Boje setzen
3. Hauptleine etwas Lose geben → Snubber übernimmt Last
4. Alternativ: Mooring Compensator in die Hauptleine einschleifen

Wichtig: Bei Bojen-Mooring immer zwei unabhängige Leinen zur Boje —
eine als Hauptleine, eine als Sicherungsleine. Der Snubber kann
eine davon sein.

---

### FAQ 15.35 — Wie vermeide ich Kinken im 3-Strand Snubber?

**Frage:** Mein 3-Strand Snubber verdreht sich ständig — was tun?

**Antwort:** 3-Strand (Dreischlag) Nylon hat eine natürliche Tendenz
zum Verdrehen unter Last. Gegenmaßnahmen:
1. **Vor dem Einsatz ausdrehen**: Snubber auf dem Steg ausrollen und
   Verdrehungen entfernen
2. **Wirbelschäkel**: Wirbel zwischen Snubber und Kettenhaken einsetzen
3. **Auf 8-Plait umsteigen**: 8-Plait Nylon verdreht sich nicht
4. **Kausche verwenden**: Reduziert Torsion am Augspleiß
5. **Regelmäßig kontrollieren**: Kinken vor dem Anlegen entfernen

---

## 16. Glossar

| Nr. | Begriff | Erklärung |
|-----|---------|-----------|
| 16.01 | **Snubber** | Elastisches Seil (typisch Nylon) zwischen Boot und Ankerkette zur Stoßdämpfung |
| 16.02 | **Ruckdämpfer** | Deutsche Bezeichnung für Snubber — betont die Dämpfungsfunktion |
| 16.03 | **Ankerfeder** | Alternative deutsche Bezeichnung für Snubber — betont die Elastizität |
| 16.04 | **Chain Hook** | Kettenhaken — Verbindungselement zwischen Snubber und Ankerkette |
| 16.05 | **Chain Stopper** | Kettenstopper — fest montiertes Bauteil zur mechanischen Blockierung der Kette |
| 16.06 | **Devil's Claw** | Klauenhaken — zweiteiliger, selbstverriegelnder Kettenstopper |
| 16.07 | **Bridle** | Y-förmiges Leinensystem an Katamaranen — verteilt Last auf beide Rümpfe |
| 16.08 | **Kellet** | Ankergewicht (Sentinel) — am Kettenabschnitt befestigt, verbessert Katarakt |
| 16.09 | **Sentinel** | Englische Bezeichnung für Kellet/Ankergewicht |
| 16.10 | **Katarakt** | Durchhang/Bogen der Ankerkette (Catenary) — dämpft Lasten durch Kettengewicht |
| 16.11 | **Catenary** | Englische Bezeichnung für den Kettenkatarakt |
| 16.12 | **Scope** | Verhältnis Kettenlänge zu Wassertiefe (z. B. 5:1) |
| 16.13 | **Chafe Guard** | Schamfilschutz — Schutzhülle gegen Scheuerung |
| 16.14 | **Schamfilen** | Scheuerung — mechanischer Abrieb durch Reibung |
| 16.15 | **Fairlead** | Umlenkbeschlag — führt Leinen um Ecken und über Kanten |
| 16.16 | **WLL** | Working Load Limit — maximale Arbeitslast (typisch 1/4 der Bruchlast) |
| 16.17 | **Bruchlast** | Kraft, bei der ein Bauteil versagt (MBL = Minimum Breaking Load) |
| 16.18 | **Augspleiß** | Schlaufe am Seilende, durch Zurückflechten der Kardeele hergestellt |
| 16.19 | **Kausche** | Metalleinsatz in einem Augspleiß — schützt vor Knicken und Abrieb |
| 16.20 | **Palstek** | Seemannsknoten — erzeugt eine feste, nicht zuziehende Schlaufe |
| 16.21 | **Kreuzschlag** | Belegtechnik auf einer Klampe — erste Runde über Kreuz |
| 16.22 | **Kopfschlag** | Abschluss auf der Klampe — sichert gegen Lösen |
| 16.23 | **Schwoien** | Drehen des Bootes um den Ankerpunkt (durch Wind/Strömung) |
| 16.24 | **Dragging** | Anker-Dragging — der Anker hält nicht und gleitet über den Grund |
| 16.25 | **Kinking** | Kinkenbildung — Verdrehung/Verschlingung in Tauwerk |
| 16.26 | **Nylon PA 6.6** | Polyamid 6.6 — Standardmaterial für Snubber und Ankerleinen |
| 16.27 | **Dyneema (HMPE)** | Hochfeste Polyethylenfaser — minimal dehnbar, UV-resistent |
| 16.28 | **3-Strand** | Dreischlag-Seil — drei Kardeele miteinander verdreht |
| 16.29 | **8-Plait** | Achtfach-Geflecht — acht Kardeele miteinander verflochten |
| 16.30 | **Viskoelastisch** | Materialverhalten, das elastische und viskose (dämpfende) Eigenschaften kombiniert |
| 16.31 | **Hysterese** | Energieverlust bei Belastung-Entlastung-Zyklus — wird als Wärme abgegeben |
| 16.32 | **DIN 766** | Deutsche Norm für kurzgliedrige Rundstahlkette |
| 16.33 | **316L** | Marine-Edelstahllegierung — korrosionsbeständig in Salzwasser |
| 16.34 | **Mooring Compensator** | Festmacher-Dämpfer — Gummielement in der Mooringleine |
| 16.35 | **Flopper-Stopper** | Platte an Leine — reduziert Rollbewegung vor Anker |
| 16.36 | **Bahamian Moor** | Ankersetzen mit zwei Ankern in entgegengesetzter Richtung (180°) |
| 16.37 | **Anchor Sailing** | Segeln am Anker — Boot pendelt durch Windangriffsfläche |
| 16.38 | **Katabatik** | Thermischer Fallwind — nachts von Bergen herabströmend |
| 16.39 | **Softschäkel** | Schäkel aus Dyneema-Seil — leicht, stark, korrosionsfrei |
| 16.40 | **Wirbelschäkel** | Schäkel mit Drehgelenk (Swivel) — verhindert Verdrehung |
| 16.41 | **Bugrolle** | Rolle am Bug — führt Kette und Anker über den Bugbeschlag |
| 16.42 | **Ankerrolle** | Synonym für Bugrolle — speziell für das Ankersystem |
| 16.43 | **Windlass** | Ankerwinde — elektrisches oder hydraulisches Gerät zum Ketten-Einholen |
| 16.44 | **Anchor Rider** | Laufschlitten auf der Ankerkette — trägt ein Kellet und gleitet beim Einholen zurück |
| 16.45 | **Bowsprit** | Bugspriet — Spiere am Bug, oft bei Katamaranen für Code-0-Segel |
| 16.46 | **Chafe** | Englisch für Scheuerung/Abrieb |
| 16.47 | **Rode** | Englisch für die Gesamtheit des Ankersystems (Kette + Leine + Snubber) |
| 16.48 | **Belegklampe** | Klampe zum Belegen (Befestigen) von Leinen und Festmachern |
| 16.49 | **Gegenplatte** | Verstärkungsplatte unter Deck — verteilt Zugkräfte auf eine größere Fläche |
| 16.50 | **Butylband** | Dauerelastisches Dichtband — ideal für Verschraubungen auf dem Deck |
| 16.51 | **Sikaflex 291** | Polyurethan-Dichtstoff für maritime Anwendungen — flexibel, UV-beständig |
| 16.52 | **Kardeele** | Die einzelnen Stränge eines Tauwerks — werden zu Seilen verdreht oder verflochten |
| 16.53 | **Rückspleiß** | Spleiß am Seilende — verhindert Aufdröseln der Kardeele |
| 16.54 | **Webleinstek** | Einfacher Seemannsknoten — nicht für Snubber geeignet (kann rutschen) |
| 16.55 | **Tide / Tidenhub** | Gezeitenbedingte Wasserstandsänderung — beeinflusst Scope und Ankerlast |
| 16.56 | **Schwoikreis** | Kreisfläche, die das Boot um den Ankerpunkt beschreibt |
| 16.57 | **MBL** | Minimum Breaking Load — kleinste zu erwartende Bruchlast |
| 16.58 | **PA 6.6** | Polyamid 6.6 (Nylon) — Standard-Polymermaterial für Ankertauwerk |
| 16.59 | **HMPE** | High Modulus Polyethylene — Hochleistungsfaser (Handelsname: Dyneema, Spectra) |
| 16.60 | **Edelstahl 316L** | Austenitischer Chrom-Nickel-Molybdän-Stahl — Standard für Marinebeschläge |
| 16.61 | **Edelstahl 304** | Günstigerer Edelstahl — nicht seewasserbeständig, nicht für Marineeinsatz |
| 16.62 | **Kontaktkorrosion** | Korrosion durch direkten Kontakt verschiedener Metalle (galvanisches Element) |
| 16.63 | **Passivschicht** | Schützende Oxidschicht auf Edelstahl — kann durch Kratzer beschädigt werden |
| 16.64 | **Tea Staining** | Gelbbraune Verfärbung auf Edelstahl — oberflächliche Korrosion, oft harmlos |
| 16.65 | **Pitting** | Lochfraß — tiefgreifende Korrosion in Form kleiner Löcher, strukturell gefährlich |

---
---

## 17. Schnell-Referenz

### 17.1 Snubber-Dimensionierung (Kurzformel)

```
Durchmesser [mm] = Kettendurchmesser × 2,5 (aufgerundet auf gerade Zahl)
Länge [m] = Bootslänge × 0,6 (Minimum 5 m, Maximum 15 m)
Bruchlast Snubber ≥ 3 × max. Windlast bei 42 kn × Dynamikfaktor 2
```

### 17.2 Setup-Checkliste (Kurzversion)

```
□ Anker gesetzt und bestätigt
□ Kette gefiert (Scope 5:1 bis 7:1)
□ Schamfilschutz auf Snubber
□ Kettenhaken in Kette eingehängt
□ Snubber auf Klampe belegt
□ 2–4 m Kettendurchhang nachgefiert
□ Kette hängt lose — Snubber trägt Last
□ GPS-Ankeralarm aktiviert
```

### 17.3 Kontroll-Checkliste (Nachtankern)

```
□ Snubber unter moderater Spannung
□ Kette hat Durchhang
□ GPS-Position stabil
□ Schamfilschutz sitzt korrekt
□ Kettenhaken gesichert
□ Ankerlaterne brennt
□ Motor startbereit
```

### 17.4 Sturm-Checkliste

```
□ Doppelsnubber gesetzt (2. Snubber 10–15 % länger)
□ Beide Snubber an verschiedenen Klampen
□ Mehr Kette gefiert (Scope 7:1 bis 10:1)
□ Kettendurchhang 4–6 m
□ Kellet ausgebracht (optional)
□ Motor warmgelaufen und startbereit
□ Fluchtweg geplant
□ Reserveanker klar zum Werfen
□ Wache eingeteilt
```

### 17.5 Preisübersicht — Komplette Systeme (12-m-Segelboot)

| Konfiguration | Komponenten | Gesamtpreis |
|--------------|-------------|-------------|
| Minimal | 16 mm Nylon 8 m + offener Haken | 65 EUR |
| Standard | 16 mm Nylon 8 m + Mantus Hook M + Schamfilschutz | 165 EUR |
| Empfohlen | Standard + Kettenstopper + Reservesnubber | 370 EUR |
| Premium | Empfohlen + Kellet + 2. Kettenhaken | 530 EUR |
| Katamaran | 2× 16 mm Nylon 8 m + Mantus Bridle Set | 290 EUR |

### 17.6 Lebensdauer-Übersicht

| Komponente | Lebensdauer | Inspektion |
|-----------|-------------|-----------|
| Nylon-Snubber (3-Strand) | 3–5 Jahre | Jährlich + nach jedem Sturm |
| Nylon-Snubber (8-Plait) | 4–6 Jahre | Jährlich |
| Dyneema/Gummi-Snubber | 5–8 Jahre | Halbjährlich (Gummi!) |
| Kettenhaken (Edelstahl) | 8–15 Jahre | Jährlich |
| Kettenstopper | 10–20 Jahre | Jährlich (Mechanismus fetten) |
| Schamfilschutz (Schlauch) | 1–2 Saisons | Vor jedem Ankern |
| Schamfilschutz (Leder) | 3–5 Jahre | Jährlich |

---
---

## 18. ANHANG A–H: Fallstudien

### ANHANG A — Windlass-Schaden durch fehlenden Snubber

**Yacht:** Bavaria 40 Cruiser (2018), 12,35 m
**Eigner:** Deutsche Crew, Charterablöser
**Revier:** Ionisches Meer, Griechenland

**Situation:**
Die Crew ankerte regelmäßig ohne Snubber — die Ankerwinde (Lewmar V3)
trug die gesamte Last. Nach 3 Saisons (ca. 200 Ankernächte) versagte
das Windengetriebe: Die Zahnräder waren so verschlissen, dass die Winde
die Kette nicht mehr halten konnte. Beim Einholen des Ankers in einer
Bucht auf Ithaka rutschte die Kette durch — nur der Kettenstopper
(glücklicherweise vorhanden) verhinderte den Verlust des Ankersystems.

**Schaden:**
- Lewmar V3 Getriebeaustausch: 1.850 EUR
- Arbeit (Windendemontage, Getriebe, Einbau): 650 EUR
- 3 Tage Liegezeit in der Werft

**Lehre:**
Ein Snubber-Set (Nylon 16 mm + Mantus Hook M) hätte 165 EUR gekostet
und den 2.500-EUR-Schaden verhindert.

**AYDI-Analyse:**
- Fehlerbild: 12.6 (kein Snubber → Windenbelastung)
- Konfidenz: documented (Werftbericht vorhanden)
- Score Impact: production -15, cost -20

---

### ANHANG B — Snubber-Scheuerbruch bei Nachtankern

**Yacht:** Hallberg-Rassy 43, 13,15 m
**Eigner:** Erfahrene Blauwasser-Segler (20.000+ sm)
**Revier:** Sardinien, Westküste

**Situation:**
Die Crew ankerte in einer Bucht an der Westküste Sardiniens. Nachts
drehte der Wind von SE auf NW (Mistral-Vorläufer). Der Snubber
(14 mm Nylon, 3 Jahre alt) lag auf der Bugrolle und scheuerte über
8 Stunden an der Edelstahlkante der Bugrolle. Um 04:00 brach der
Snubber — die Kette ruckte auf die Winde und weckte die Crew.

**Schaden:**
- Snubber verloren (im Wasser versunken): 45 EUR
- Keine weiteren Schäden dank schneller Reaktion

**Lehre:**
1. Schamfilschutz hätte den Bruch verhindert (3 EUR für Schlauch)
2. 14 mm war für eine HR43 grenzwertig — 16 mm empfohlen
3. Nach 3 Jahren war der Snubber UV-geschwächt

**AYDI-Analyse:**
- Fehlerbild: 12.1 (Scheuerbruch) + 12.4 (UV-Degradation)
- Konfidenz: documented (Crew-Bericht)
- Score Impact: materials -10, ergonomics -5

---

### ANHANG C — Katamaran-Bridle erfolgreich im Sturm

**Yacht:** Lagoon 42 (2020), 12,80 m
**Eigner:** Französisch-deutsches Paar, Weltumsegelung
**Revier:** Karibik, Dominica

**Situation:**
Tropischer Sturm (45 Knoten sustained, Böen 55 Knoten) traf die
Ankerbucht vor Prince Rupert Bay, Dominica. Die Crew hatte ein
professionelles Bridle-System:
- 2× 18 mm Nylon 3-Strand, je 10 m
- 2× Mantus Chain Hook M
- 10 mm Kette, 70 m gefiert (Scope 7:1 bei 10 m Tiefe)
- Kellet (10 kg) am Bridle-V-Punkt

Das Boot lag ruhig, schwoite gleichmäßig und hielt sicher. Mehrere
andere Boote (ohne Bridle/Snubber) draggten und mussten Anker lichten.

**Lehre:**
1. Professionelles Bridle-System ist entscheidend für Katamarane
2. Kellet am V-Punkt reduziert Pendeln erheblich
3. 18 mm Nylon bietet ausreichende Reserve für tropische Stürme

**AYDI-Analyse:**
- Kein Fehlerbild — System hat einwandfrei funktioniert
- Konfidenz: documented (Crew-Logbuch)
- Referenz für Best Practice

---

### ANHANG D — Devil's Claw rettet Ankersystem

**Yacht:** Oyster 485 (2016), 14,90 m
**Eigner:** Britisches Ehepaar, Transatlantik + Karibik-Saison
**Revier:** Tobago Cays, Grenadinen

**Situation:**
Die Crew verwendete einen offenen Kettenhaken (Standardhaken vom
Bootshersteller). Bei einem 180°-Dreher (Tidenstrom + Windwechsel)
hängte sich der Haken aus. Die gesamte Last fiel auf die Winde.
Zum Glück lief die Crew gerade Wache.

Daraufhin investierte die Crew in eine Devil's Claw (Custom, Edelstahl,
350 EUR) — in den folgenden 2 Jahren und 500 Ankernächten hängte sich
der Haken kein einziges Mal mehr aus.

**Lehre:**
1. Offene Haken sind für Langfahrt ungeeignet
2. Devil's Claw ist die sicherste Lösung
3. Investition von 350 EUR vs. potenzieller Windenschaden (2.000+ EUR)

**AYDI-Analyse:**
- Fehlerbild: 12.2 (Kettenhaken ausgehängt)
- Konfidenz: documented (Crew-Bericht)
- Score Impact: materials +15 (nach Umrüstung)

---

### ANHANG E — Überdimensionierter Snubber — zu steif

**Yacht:** Sun Odyssey 349 (2019), 10,34 m
**Eigner:** Wochenendsegler, Ostsee
**Revier:** Dänische Südsee

**Situation:**
Der Eigner hatte auf Empfehlung eines Freundes einen 22 mm Snubber
gekauft — korrekt wäre 14 mm gewesen. Der Snubber war so steif, dass
er kaum Dämpfungswirkung entfaltete. Das Boot lag genauso unruhig wie
ohne Snubber, und die Geräuschübertragung war nur minimal reduziert.

**Lehre:**
1. Überdimensionierung ist kontraproduktiv
2. 22 mm bei 10-m-Boot → Dehnung bei normaler Last: nur 2–3 %
3. Korrekte Dimensionierung (14 mm) hätte 10–15 % Dehnung ergeben

**AYDI-Analyse:**
- Kein technisches Versagen, aber Komfort-Einbuße
- Konfidenz: estimated (Erfahrungsbericht)
- Score Impact: ergonomics -5

---

### ANHANG F — Kellet bei begrenzter Kettenlänge

**Yacht:** Moody 31 Mk II (1988), 9,50 m
**Eigner:** Pensionierter Segler, Atlantikküste Frankreich
**Revier:** Bretagne (Tidenhub 8–12 m)

**Situation:**
Die Moody 31 hatte nur 40 m 8-mm-Kette an Bord — in der Bretagne bei
bis zu 12 m Tidenhub ist das grenzwertig. Bei Niedrigwasser (3 m Tiefe)
konnte der Eigner nur Scope 4:1 fahren (12 m Kette + 3 m Tiefe = 15 m,
aber 40/3 = 13:1 bei NW, 40/15 = 2,7:1 bei HW). Der Scope bei
Hochwasser war gefährlich niedrig.

Lösung: 14 kg Kellet (Gusseisen, Greenfield, 75 EUR) bei 1/3 der
Kettenlänge. Der Kellet reduzierte den effektiven Scope-Bedarf und
verbesserte die Haltekraft erheblich.

**Lehre:**
1. In Tidenrevieren mit begrenzter Kette: Kellet ist unverzichtbar
2. 14 kg Kellet für 9,5-m-Boot ist korrekt dimensioniert
3. Alternative: 60 m Kette nachrüsten (aber: Gewicht, Kosten)

**AYDI-Analyse:**
- Konfidenz: documented (Eigner-Erfahrung über 5 Saisons)
- Score Impact: structural +10 (Sicherheitsverbesserung)

---

### ANHANG G — Mooring Compensator am Hafenliegeplatz

**Yacht:** Beneteau Gran Turismo 36 (2021), 11,34 m
**Eigner:** Motoryacht-Eigner, Adria
**Revier:** Marina Kornati, Kroatien

**Situation:**
Die GT36 lag an einem exponierten Steg in der Marina Kornati. Starker
Bora-Wind (40–50 Knoten) belastete die Festmacherleinen erheblich.
Ohne Mooring Compensator ruckten die Leinen bei jeder Böe, und die
Klampen zeigten nach einer Saison Haarrisse in der Decksbefestigung.

Nach Installation von 4× Unimer Mooring Compensator U-Cleat (10–14 m
Modell, je 65 EUR, gesamt 260 EUR) waren die Ruckbelastungen eliminiert.
Die Deckschäden stoppten.

**Lehre:**
1. Mooring Compensatoren gehören an jeden exponierten Liegeplatz
2. 260 EUR Investition vs. 3.000+ EUR Decksreparatur
3. Alle vier Leinen dämpfen — nicht nur die Windward-Leine

**AYDI-Analyse:**
- Fehlerbild: vergleichbar 12.5 (Klampen-/Deckbelastung)
- Konfidenz: documented (Marina-Berichte, Fotos)
- Score Impact: structural +10, cost +15

---

### ANHANG H — Improvisierter Snubber nach Verlust

**Yacht:** Dufour 382 Grand Large (2017), 11,25 m
**Eigner:** Chartercrew (3 Personen, erfahren)
**Revier:** Kykladen, Griechenland

**Situation:**
Beim Ankern vor Paros riss der Snubber (alter, UV-geschädigter 12 mm
Nylon). Der Reservesnubber war nicht an Bord (Charterbasis hatte ihn
nicht bereitgestellt). Die Crew improvisierte:

1. Genua-Schot (14 mm Polyester) als Notleine vom Bug zur Kette
2. Palstek um ein Kettenglied (da kein Kettenhaken vorhanden)
3. 2 m extra Kette nachgefiert

Das Polyester-Seil bot praktisch keine Dämpfung (3 % Dehnung vs.
20 % bei Nylon), aber es entlastete die Winde über Nacht. Am nächsten
Tag wurde in Parikia ein neuer Nylon-Snubber gekauft.

**Lehre:**
1. Charterbasis kontrollieren: Snubber + Reservesnubber vorhanden?
2. Polyester ist als Snubber-Ersatz ungeeignet, aber besser als nichts
3. Palstek um Kettenglied funktioniert als Not-Kettenhaken
4. Im Mittelmeer-Sommer: Nylon-Snubber nach 2 Jahren ersetzen

**AYDI-Analyse:**
- Fehlerbild: 12.4 (UV-Degradation) → Bruch
- Konfidenz: documented (Charterbericht)
- Score Impact: materials -10, safety -15

---
---

## 19. ANHANG I–R: Pydantic v2 Datenmodelle

### ANHANG I — SnubberType (Enum)

```python
from enum import Enum


class SnubberType(str, Enum):
    """Snubber-Typen nach Material und Konstruktion."""
    NYLON_3_STRAND = "nylon_3_strand"
    NYLON_8_PLAIT = "nylon_8_plait"
    DYNEEMA_RUBBER = "dyneema_rubber"
    BUNGEE = "bungee"
    POLYESTER = "polyester"  # Nicht empfohlen als Snubber
    CUSTOM = "custom"
```

### ANHANG J — ChainHookType (Enum)

```python
from enum import Enum


class ChainHookType(str, Enum):
    """Kettenhaken-Typen."""
    OPEN_HOOK = "open_hook"
    LATCH_HOOK = "latch_hook"
    CLAW_HOOK = "claw_hook"
    CHAIN_GRAB = "chain_grab"
    DEVILS_CLAW = "devils_claw"
    IMPROVISED = "improvised"
```

### ANHANG K — ChainStopperType (Enum)

```python
from enum import Enum


class ChainStopperType(str, Enum):
    """Kettenstopper-Typen."""
    HINGED = "hinged"
    DEVILS_CLAW = "devils_claw"
    PIN_STOPPER = "pin_stopper"
    INTEGRATED = "integrated"  # In Winden-Plattform integriert
    CUSTOM = "custom"
```

### ANHANG L — SnubberSpec

```python
from pydantic import BaseModel, Field


class SnubberSpec(BaseModel):
    """Spezifikation eines Snubber-Seils."""
    model_config = {"from_attributes": True}

    snubber_type: SnubberType = Field(
        ..., description="Typ des Snubbers"
    )
    manufacturer: str = Field(
        "", description="Hersteller"
    )
    product_name: str = Field(
        "", description="Produktbezeichnung"
    )
    diameter_mm: float = Field(
        ..., ge=8, le=32,
        description="Durchmesser in mm"
    )
    length_m: float = Field(
        ..., ge=3, le=20,
        description="Länge in m"
    )
    breaking_load_kn: float = Field(
        ..., ge=1, le=100,
        description="Bruchlast in kN"
    )
    working_load_kn: float = Field(
        ..., ge=0.5, le=25,
        description="Arbeitslast (WLL) in kN"
    )
    elongation_at_30pct_bl: float = Field(
        ..., ge=1, le=50,
        description="Dehnung bei 30 % Bruchlast in %"
    )
    material: str = Field(
        "PA 6.6", description="Material (z. B. PA 6.6, HMPE)"
    )
    uv_resistance: str = Field(
        "low", description="UV-Beständigkeit: low, medium, high"
    )
    chafe_guard_installed: bool = Field(
        False, description="Schamfilschutz vorhanden?"
    )
    splice_type: str = Field(
        "none", description="Spleiß-Typ: none, eye_splice, back_splice, knot"
    )
    age_years: float = Field(
        0, ge=0, le=20,
        description="Alter des Snubbers in Jahren"
    )
    condition: str = Field(
        "good", description="Zustand: new, good, fair, poor, replace"
    )
    price_eur: float = Field(
        0, ge=0,
        description="Preis in EUR"
    )

    notes: list[str] = Field(default_factory=list)
```

### ANHANG M — ChainHookSpec

```python
from pydantic import BaseModel, Field


class ChainHookSpec(BaseModel):
    """Spezifikation eines Kettenhakens."""
    model_config = {"from_attributes": True}

    hook_type: ChainHookType = Field(
        ..., description="Typ des Kettenhakens"
    )
    manufacturer: str = Field(
        "", description="Hersteller"
    )
    product_name: str = Field(
        "", description="Produktbezeichnung"
    )
    chain_size_min_mm: float = Field(
        ..., ge=4, le=20,
        description="Minimale Kettengröße in mm"
    )
    chain_size_max_mm: float = Field(
        ..., ge=4, le=20,
        description="Maximale Kettengröße in mm"
    )
    wll_kg: float = Field(
        ..., ge=100, le=20000,
        description="Working Load Limit in kg"
    )
    breaking_load_kg: float = Field(
        ..., ge=500, le=80000,
        description="Bruchlast in kg"
    )
    material: str = Field(
        "316L", description="Material (z. B. 316L, 316, verzinkt)"
    )
    weight_g: float = Field(
        ..., ge=50, le=3000,
        description="Gewicht in Gramm"
    )
    has_swivel: bool = Field(
        False, description="Integrierter Wirbel vorhanden?"
    )
    has_latch: bool = Field(
        True, description="Verriegelungsmechanismus vorhanden?"
    )
    price_eur: float = Field(
        0, ge=0,
        description="Preis in EUR"
    )

    condition: str = Field(
        "good", description="Zustand: new, good, fair, corroded, replace"
    )
    corrosion_noted: bool = Field(
        False, description="Korrosion festgestellt?"
    )

    notes: list[str] = Field(default_factory=list)
```

### ANHANG N — ChainStopperSpec

```python
from pydantic import BaseModel, Field


class ChainStopperSpec(BaseModel):
    """Spezifikation eines Kettenstoppers."""
    model_config = {"from_attributes": True}

    stopper_type: ChainStopperType = Field(
        ..., description="Typ des Kettenstoppers"
    )
    manufacturer: str = Field(
        "", description="Hersteller"
    )
    product_name: str = Field(
        "", description="Produktbezeichnung"
    )
    chain_size_min_mm: float = Field(
        ..., ge=4, le=20,
        description="Minimale Kettengröße in mm"
    )
    chain_size_max_mm: float = Field(
        ..., ge=4, le=20,
        description="Maximale Kettengröße in mm"
    )
    wll_kg: float = Field(
        ..., ge=500, le=30000,
        description="Working Load Limit in kg"
    )
    material: str = Field(
        "316L", description="Material"
    )
    weight_g: float = Field(
        ..., ge=200, le=5000,
        description="Gewicht in Gramm"
    )
    mounting_bolts: int = Field(
        4, ge=2, le=8,
        description="Anzahl Befestigungsbolzen"
    )
    bolt_size_mm: float = Field(
        10, ge=6, le=16,
        description="Bolzengröße in mm"
    )
    deck_thickness_min_mm: float = Field(
        8, ge=4, le=20,
        description="Minimale Decksstärke in mm"
    )
    backing_plate_installed: bool = Field(
        False, description="Gegenplatte installiert?"
    )
    sealant_type: str = Field(
        "", description="Verwendeter Dichtstoff"
    )
    price_eur: float = Field(
        0, ge=0,
        description="Preis in EUR"
    )

    condition: str = Field(
        "good", description="Zustand: new, good, fair, corroded, replace"
    )

    notes: list[str] = Field(default_factory=list)
```

### ANHANG O — BridleSpec

```python
from pydantic import BaseModel, Field


class BridleSpec(BaseModel):
    """Spezifikation eines Katamaran-Bridle-Systems."""
    model_config = {"from_attributes": True}

    bridle_type: str = Field(
        "y_bridle",
        description="Bridle-Typ: y_bridle, v_bridle_with_snubber, delta_bridle"
    )
    line_diameter_mm: float = Field(
        ..., ge=10, le=28,
        description="Leinendurchmesser in mm"
    )
    line_length_m: float = Field(
        ..., ge=4, le=18,
        description="Leinenlänge je Seite in m"
    )
    line_material: SnubberType = Field(
        SnubberType.NYLON_3_STRAND,
        description="Material der Bridle-Leinen"
    )
    breaking_load_kn: float = Field(
        ..., ge=5, le=80,
        description="Bruchlast je Leine in kN"
    )
    hull_separation_m: float = Field(
        ..., ge=2, le=12,
        description="Rumpfabstand in m"
    )

    # Kettenhaken
    hook_type: ChainHookType = Field(
        ChainHookType.LATCH_HOOK,
        description="Typ der Kettenhaken"
    )
    hooks_count: int = Field(
        1, ge=1, le=2,
        description="Anzahl Kettenhaken (1 = gemeinsam, 2 = getrennt)"
    )

    # Optional: zentraler Snubber (bei V-Bridle)
    central_snubber: bool = Field(
        False, description="Zentraler Snubber vorhanden?"
    )
    central_snubber_diameter_mm: float | None = Field(
        None, ge=10, le=24,
        description="Durchmesser des zentralen Snubbers in mm"
    )
    central_snubber_length_m: float | None = Field(
        None, ge=2, le=8,
        description="Länge des zentralen Snubbers in m"
    )

    # Fairleads
    fairleads_installed: bool = Field(
        False, description="Fairleads für Leinenführung installiert?"
    )

    # Kellet am V-Punkt
    kellet_attached: bool = Field(
        False, description="Kellet am V-Punkt befestigt?"
    )
    kellet_weight_kg: float | None = Field(
        None, ge=1, le=30,
        description="Kellet-Gewicht in kg"
    )

    notes: list[str] = Field(default_factory=list)
    condition: str = Field(
        "good", description="Zustand: new, good, fair, poor, replace"
    )
    price_eur: float = Field(
        0, ge=0,
        description="Gesamtpreis in EUR"
    )
```

### ANHANG P — KelletSpec

```python
from pydantic import BaseModel, Field


class KelletSpec(BaseModel):
    """Spezifikation eines Kellets (Ankergewicht/Sentinel)."""
    model_config = {"from_attributes": True}

    weight_kg: float = Field(
        ..., ge=1, le=30,
        description="Gewicht in kg"
    )
    material: str = Field(
        "cast_iron",
        description="Material: cast_iron, lead, lead_stainless, chain_section"
    )
    manufacturer: str = Field(
        "", description="Hersteller"
    )
    product_name: str = Field(
        "", description="Produktbezeichnung"
    )
    rider_type: str = Field(
        "fixed",
        description="Typ: fixed (Festposition), sliding (Laufschlitten)"
    )
    chain_size_mm: float = Field(
        ..., ge=6, le=16,
        description="Passende Kettengröße in mm"
    )
    retrieval_line_length_m: float = Field(
        0, ge=0, le=100,
        description="Länge der Rückholleine in m"
    )
    position_from_bow_pct: float = Field(
        33, ge=10, le=60,
        description="Position auf der Kette (% vom Bug)"
    )
    price_eur: float = Field(
        0, ge=0,
        description="Preis in EUR"
    )

    notes: list[str] = Field(default_factory=list)
```

### ANHANG Q — SnubberSystemAssessment

```python
from pydantic import BaseModel, Field


class SnubberSystemAssessment(BaseModel):
    """Gesamtbewertung des Snubber-/Kettenstopper-Systems einer Yacht."""
    model_config = {"from_attributes": True}

    # Boot-Grunddaten
    boat_name: str = Field("", description="Bootsname")
    boat_loa_m: float = Field(..., ge=4, le=40, description="Bootslänge in m")
    boat_displacement_kg: float = Field(
        ..., ge=500, le=100000,
        description="Verdrängung in kg"
    )
    boat_type: str = Field(
        "sailboat",
        description="Bootstyp: sailboat, motorboat, catamaran, trimaran"
    )
    chain_diameter_mm: float = Field(
        ..., ge=6, le=16,
        description="Kettendurchmesser in mm"
    )

    # Snubber
    snubber: SnubberSpec | None = Field(
        None, description="Hauptsnubber"
    )
    reserve_snubber: SnubberSpec | None = Field(
        None, description="Reservesnubber"
    )

    # Kettenhaken
    chain_hook: ChainHookSpec | None = Field(
        None, description="Kettenhaken"
    )

    # Kettenstopper
    chain_stopper: ChainStopperSpec | None = Field(
        None, description="Kettenstopper"
    )

    # Bridle (nur Katamaran)
    bridle: BridleSpec | None = Field(
        None, description="Bridle-System (nur Katamaran)"
    )

    # Kellet
    kellet: KelletSpec | None = Field(
        None, description="Kellet/Ankergewicht"
    )

    # Befestigungspunkt
    attachment_point: str = Field(
        "cleat",
        description="Befestigungspunkt: cleat, bollard, eye, roller_cleat"
    )
    attachment_adequate: bool = Field(
        True, description="Befestigungspunkt ausreichend dimensioniert?"
    )
    backing_plate_present: bool = Field(
        False, description="Gegenplatte vorhanden?"
    )

    # Bewertung
    overall_score: float = Field(
        0, ge=0, le=100,
        description="Gesamtbewertung Snubber-System (0–100)"
    )
    score_breakdown: dict[str, float] = Field(
        default_factory=dict,
        description="Teilbewertungen (snubber_sizing, snubber_condition, "
                    "chain_hook, chain_stopper, attachment, chafe_protection)"
    )

    # Dimensionierungscheck
    snubber_diameter_adequate: bool = Field(
        True, description="Snubber-Durchmesser korrekt dimensioniert?"
    )
    snubber_length_adequate: bool = Field(
        True, description="Snubber-Länge korrekt dimensioniert?"
    )
    safety_factor: float = Field(
        0, ge=0, le=20,
        description="Sicherheitsfaktor (Bruchlast / Max. dyn. Last)"
    )
    safety_factor_adequate: bool = Field(
        True, description="Sicherheitsfaktor ≥ 3,0?"
    )

    # Befunde
    warnings: list[str] = Field(default_factory=list)
    critical_findings: list[str] = Field(default_factory=list)
    recommendations: list[str] = Field(default_factory=list)

    confidence: str = Field("estimated")
    analysis_version: str = Field("2.0")
```

### ANHANG R — SnubberLoadCalculation

```python
from pydantic import BaseModel, Field


class SnubberLoadCalculation(BaseModel):
    """Berechnung der Snubber-Belastung und Dimensionierungsprüfung."""
    model_config = {"from_attributes": True}

    # Eingabeparameter — Boot
    boat_loa_m: float = Field(..., ge=4, le=40)
    boat_displacement_kg: float = Field(..., ge=500, le=100000)
    windage_area_m2: float = Field(..., ge=1, le=150)

    # Eingabeparameter — Bedingungen
    wind_speed_kn: float = Field(..., ge=0, le=80)
    current_speed_kn: float = Field(0, ge=0, le=10)
    wave_height_m: float = Field(0, ge=0, le=8)

    # Eingabeparameter — Snubber
    snubber_diameter_mm: float = Field(..., ge=8, le=32)
    snubber_length_m: float = Field(..., ge=3, le=20)
    snubber_material: SnubberType = Field(SnubberType.NYLON_3_STRAND)
    snubber_breaking_load_kn: float = Field(..., ge=1, le=100)
    snubber_elongation_pct: float = Field(..., ge=1, le=50)

    # Berechnete Werte — Kräfte
    wind_force_kn: float = Field(
        ..., ge=0,
        description="Windkraft in kN"
    )
    current_force_kn: float = Field(
        0, ge=0,
        description="Strömungskraft in kN"
    )
    wave_force_kn: float = Field(
        0, ge=0,
        description="Wellenkraft in kN"
    )
    static_load_kn: float = Field(
        ..., ge=0,
        description="Statische Gesamtlast in kN"
    )
    dynamic_factor: float = Field(
        1.0, ge=1.0, le=5.0,
        description="Dynamischer Lastfaktor"
    )
    peak_load_kn: float = Field(
        ..., ge=0,
        description="Spitzenlast in kN"
    )

    # Berechnete Werte — Snubber
    snubber_extension_m: float = Field(
        ..., ge=0,
        description="Snubber-Dehnung in m bei Spitzenlast"
    )
    snubber_load_pct_bl: float = Field(
        ..., ge=0, le=100,
        description="Snubber-Belastung in % der Bruchlast"
    )
    energy_absorbed_j: float = Field(
        ..., ge=0,
        description="Absorbierte Energie in Joule"
    )

    # Bewertung
    safety_factor: float = Field(
        ..., ge=0,
        description="Sicherheitsfaktor (Bruchlast / Spitzenlast)"
    )
    safety_adequate: bool = Field(
        ..., description="Sicherheitsfaktor ≥ 2,5?"
    )
    working_range_ok: bool = Field(
        ..., description="Snubber im Arbeitsbereich (< 40 % BL)?"
    )

    # Empfohlener Kettendurchhang
    recommended_chain_slack_m: float = Field(
        ..., ge=0, le=10,
        description="Empfohlener Kettendurchhang in m"
    )

    # Dimensionierungsempfehlung
    min_recommended_diameter_mm: float = Field(
        ..., ge=8, le=32,
        description="Mindestens empfohlener Snubber-Durchmesser in mm"
    )
    min_recommended_length_m: float = Field(
        ..., ge=3, le=20,
        description="Mindestens empfohlene Snubber-Länge in m"
    )
    diameter_adequate: bool = Field(
        ..., description="Aktueller Durchmesser ausreichend?"
    )
    length_adequate: bool = Field(
        ..., description="Aktuelle Länge ausreichend?"
    )

    notes: list[str] = Field(default_factory=list)
    confidence: str = Field("calculated")
```

---
---

*Dokument erstellt: 2026-04 | AYDI Maritime Knowledge Base v2.0*
*Nächste Überprüfung geplant: 2026-10*
*Autor: AYDI AI Yacht Design Intelligence*

*Quellen: Practical Sailor, YACHT Magazin, Sailing World, Cruising World,
Herstellerangaben (Mantus Marine, Kong, Wichard, Yale Cordage, Ultra Marine,
Lewmar, Maxwell, Lofrans, Quick, Unimer, Eval, Davis Instruments, Greenfield,
Kiwi Anchor Rider, Rocna, SailRite), ABYC H-40, ISO 15083,
EU-Richtlinie 2013/53/EU, DIN 766, Langfahrt-Erfahrungsberichte,
Segelmagazin, Palstek Magazin, ADAC-Seenotstatistiken.*

---
