---
category: "28_Interieur_Materialien"
subcategory: "Interieur_Wartung"
version: "1.1"
last_updated: "2026-07-13"
lang: "de"
---

# Kat 28.07 — Interieur-Wartung & Pflege (Interior Maintenance & Care)

## 0. Normativer & regulatorischer Rahmen

Interieur-Wartung ist überwiegend Pflege- und Werkstoffthema, berührt aber an mehreren Stellen **verbindliche Normen** (Brandschutz, CO-Detektion, Kochstellen) sowie **anerkannte bauphysikalische Schwellenwerte** (Feuchte/Schimmel). Wartung darf normrelevante Eigenschaften (z. B. Flammschutz von Polstern/Verkleidungen, Fluchtwege, Mindestabstände zu Wärmequellen) **niemals nachträglich verschlechtern**.

### 0.1 Verbindliche Normen (small craft, LH ≤ 24 m)

| Norm (Nummer + Titel) | Scope / Relevanz für Interieur-Wartung | Confidence |
|---|---|---|
| **ISO 9094:2022 — Small craft — Fire protection** | Legt praktischen Brandschutz fest, der genug Zeit zum Verlassen des Fahrzeugs bei Brand gibt; gilt für Boote mit Rumpflänge LH ≤ 24 m (ausser Wassermotorräder). Betrifft brennbare Materialien im Innenraum, Mindestabstände zu Wärmequellen und Fluchtwege — bei Retrofit/Neubezug von Polstern und Verkleidungen zu beachten. | `documented` |
| **ISO 14895:2016 — Liquid-fuelled galley stoves / heating appliances** | Von ISO 9094 **ausgenommen** und separat geregelt: Auslegung/Installation fest eingebauter, mit bei Atmosphärendruck flüssigen Brennstoffen betriebener Koch-/Heizgeräte. Relevant für die Wärmequellen-Umgebung in Pantry/Kombüse. | `documented` |
| **ISO 12133 — Small craft — Carbon monoxide detecting systems** | CO-Warnsysteme; von ISO 9094 ausgenommen und separat geregelt. Bei Innenraumarbeiten mit Verbrennungsgeräten (Heizung, Kocher) mitzudenken. | `documented` |

> Scope-Beleg ISO 9094: [iso.org/standard/78242](https://www.iso.org/standard/78242.html) · Ausnahmen (14895, 12133): ISO 9094:2022 Vorschau [standards.iteh.ai – ISO-9094-2022](https://cdn.standards.iteh.ai/samples/78242/482780416b894e35bc83742b9e9378f1/ISO-9094-2022.pdf)

**Wichtig:** Ältere Ausgaben existieren (ISO 9094-1:2003 für LH ≤ 15 m, ISO 9094-2 für > 15 m; ISO 9094:2015). Die konsolidierte **ISO 9094:2022** deckt LH ≤ 24 m ab. Für das anwendbare Baujahr/CE-Modul ist die zum Zeitpunkt des Inverkehrbringens gültige Fassung massgeblich — nicht raten, im CE-Handbuch des Boots prüfen.

### 0.2 Anerkannte Feuchte-/Schimmel-Schwellenwerte (bauphysikalisch, nicht ISO)

Keine ISO-Norm, aber breiter fachlicher Konsens (EPA, Building Science). Diese Werte sind die Basis der Schimmel-Prävention in Abschnitt 5:

| Kenngrösse | Wert | Bedeutung | Confidence |
|---|---|---|---|
| Raumluft-RH-Zielband | **30–50 % RH** | Idealbereich, Schimmel kann sich nicht etablieren | `documented` |
| EPA-Obergrenze Raumluft | **< 60 % RH** | oberhalb dieses Werts kann Schimmel auf organischen Oberflächen keimen | `documented` |
| Kritische **Oberflächen**-RH | **70 % RH an der Oberfläche** | maszgeblich ist die lokale RH an (kalten) Oberflächen, nicht die Raummitte — diese darf nie erreicht werden | `documented` |
| Keimzeit bei > 70 % RH + 21–32 °C | **24–48 h** | auf feuchtem organischem Material entsteht sichtbares Wachstum bereits in 1–2 Tagen | `documented` |

> Quellen: [US-EPA / buildingscience.com – Relative Humidity RR-0203](https://buildingscience.com/documents/reports/rr-0203-relative-humidity/view) · [truesightenvironmental.com – Humidity Thresholds for Mold](https://truesightenvironmental.com/learn/mold-science/building-science/humidity-thresholds/)

**Konsequenz für die Praxis:** Ein Raum bei komfortablen 50 % RH kann an einer kalten, unisolierten Bordwand oder an einem Metallspant lokal > 70 % Oberflächen-RH erreichen und dort schimmeln, obwohl das Hygrometer in Kabinenmitte „grün" zeigt. Deshalb Hygrometer **mehrfach** platzieren (Abschnitt 5.2) und kalte Oberflächen (Rumpf hinter Möbeln, Fensterlaibungen) gezielt beobachten.

---

## 1. Überblick: Wartungs-Strategie im Yachtbau

Marine-Interieure sind hochgradig variable Umgebungen: Temperatur-Schwankungen, Feuchte-Exposition, UV-Strahlung, Salzwassernebel, und konstante Bewegung (Schiffsbewegung) stellen Material unter dauernden Stress.

**Kernprinzipien der Instandhaltung:**
1. **Prävention > Reparatur:** 1€ Prävention spart 10€ Reparatur
2. **Material-Bewusstsein:** Unterschiedliche Materialien brauchen unterschiedliche Pflege
3. **Regelmäßigkeit:** Monatliche Kontrolle + jährliche Intensiv-Pflege
4. **Dokumentation:** Wartungs-Log für Resale-Wert
5. **Schnell handeln:** Kleine Probleme werden nicht größer, wenn sofort behoben

**Kostenmodell über 10 Jahre:**
- Vernachlässigung: 0€ Ausga → Großschäden nach 5 Jahren (5000–15000€ Reparatur)
- Minimal-Wartung: 200 €/Jahr → Moderate Reparaturen (2000–5000€)
- Proaktive Pflege: 500–800 €/Jahr → Quasi keine Reparaturen (<500€)

---

## 2. Holz-Pflege-Systematik

### 2.1 Massivholz (Teak, Mahagoni, Buche)

**Feuchte-Management:**
- **Zielbereich:** 10–14% Holzfeuchte (marine Standard)
- **Messung:** Mit Holzfeuchtemessgerät (30–150 €, z.B. Gann Hydromette)
- **Kontrolle-Häufigkeit:** Monatlich, oder nach längeren Regenpausen

**Kritische Werte:**
| Feuchte | Status | Aktion |
|---------|--------|--------|
| <10% | Zu trocken | Befeuchter, Lüftung reduzieren |
| 10–14% | Ideal | Wartungsmodus |
| 14–16% | Erhöht | Aufmerksamkeit, Belüftung erhöhen |
| 16–18% | Hoch | Aktive Trocknung, Heizung |
| >18% | Kritisch | Sofort Entlüftung, Heizung max |

**Oberflächen-Finishes Wartung:**

#### Option A: Cetol UV / Sikkens Finish
- Häufigkeit: Jährliche Auffrischung (leichte Neulackierung)
- Mittel: Cetol UV 0.1 L/10m² (80 €/L)
- Prozess:
  1. Oberflächenreinigung (Seife + Wasser)
  2. Leichtes Abschleifen (Körnung 220–280, sehr sanft)
  3. Auftrag: Dünne Schicht Cetol (Pinsel)
  4. Trocknungszeit: 24h

**Kosten:** 150–300 € jährlich (Material + Arbeit)

#### Option B: Hartwachs-Öl (Osmo, Livos)
- Häufigkeit: MONATLICH (wichtig!)
- Mittel: Auffrischöl (40–60 €/L)
- Prozess:
  1. Oberflächenreinigung
  2. Ölrakel oder breiter Pinsel dünn auftragen
  3. Mit Bürste einarbeiten
  4. Nach 2–3h Trockenzeit kann Schiff benutzt werden
- Kosten: 50–100 € monatlich (Material nur, Eigen-Arbeit)

**Gesamtkosten pro Jahr:**
- Cetol: 150–300 €
- Hartwachs-Öl: 600–1200 €

**Entscheidung:** Cetol = wartungsärmer langfristig, Hartwachs-Öl = natürlicher Look + mehr Arbeit

#### Option C: Epifanes / 2K-Polyurethane
- Häufigkeit: Alle 3–5 Jahre komplett erneuern
- Unterhalts-Abschleifen: Alle 2 Jahre (200–400 €)
- Kosten: 400–800 € alle 5 Jahre (amortisiert ~100–160 €/Jahr)

### 2.2 Sperrholz & Furniere

**Quellung-Prävention:**
- Kanten IMMER versiegeln (Epoxy oder Polyurethane-Versiegelung)
- Feuchte <12% kritisch
- Belüftung unter Sperrholz (min. 50 mm Luft-Spalt)

**Wartungs-Prozedur:**
1. Monatliche Feuchte-Kontrolle
2. Jährliche Oberflächenfinish erneuern (wie Massivholz)
3. Kanten prüfen (Quellung, Risse?)
4. 5-Jahres-Tiefenkontrolle (Delaminierung?)

**Schädigung-Erkennung:**
- Aufwölbung an Rändern → Quellung (Belüftung prüfen)
- Risse in Furnier → Schwindung (zu trocken oder Unterbau-Problem)
- Delamination sichtbar → Material-Ausfall (Austausch erforderlich)

### 2.3 Schimmel-Prävention an Holz

**Kritische Bedingungen:**
- Relative Feuchte >70% + Temperatur 15–25°C = Schimmel-Risiko
- Mangelnde UV-Exposition (dunkle Kabinen-Ecken)
- Schlechte Belüftung (Luft staut)

**Früherkennung:**
- Schwarze/grüne Flecken in Ecken (visuell)
- Muffiger Geruch (olfaktorisch)
- Feuchte-Messung >75% RH über längere Zeit (hygometrisch)

**Sanierung Holz-Schimmel:**
1. **Ursachen-Behebung:** Belüftung verbessern, Feuchte senken
2. **Oberflächenbehandlung:** Oxalsäure-Lösung (500 ml in 5L Wasser) auftragen
   - Kontaktzeit: 1–2 Stunden
   - Kosten: 20–30 € Material
   - Arbeit: 1–2 Stunden (Eigene oder 50 €/h)
3. **Neulackierung:** Nach Behandlung komplett neu versiegeln
4. **Prävention:** Monatliche Lüftung (min. 4–6 Stunden/Tag)

**Kosten Schimmel-Sanierung:** 100–300 € (Material + Arbeit), Großflächen: 500–1500 €

---

## 3. Farb- & Oberflächenschutz gegen UV

### 3.1 UV-Exposition & Degradation

**Material-Suszeptibilität:**
| Material | UV-Empfindlichkeit | Symptom | Schutz |
|----------|-------------------|---------|--------|
| Teak (unversiegelt) | Sehr hoch | Vergraut nach 2–3 Jahren | Cetol UV oder Finishing |
| Kunststoff (Vinyl, Polyurethane) | Hoch | Vergilbung, Bruchkanten | UV-Filter Lacke |
| Leder/Kunstleder | Sehr hoch | Rissbildung, Farbverlust | UV-Fensterfolie |
| Metall-Beschläge | Mittel | Mattwerden, Korrosion | Wachsschutz |

### 3.2 UV-Filter-Techniken

**Fensterfolie (UV-Filterung):**
- Material: Polyester + UV-Blocker-Additive
- Transmission: 60–80% Licht, 0–5% UV
- Installation: Auf Innenseite Fenster kleben
- Kosten: 20–50 €/m² (Material + Kleben)
- Haltbarkeit: 5–7 Jahre

**Rollos/Jalousien:**
- Material: Blickdicht, UV-undurchlässig
- Vorteil: Kombiniert Licht-Kontrolle + Sicht-Privatsphäre
- Kosten: 100–300 € pro Fenster

**Lack-basierte UV-Filter (in Oberflächenfinishes):**
- Integrated in Cetol UV, Spar Polyurethane UV
- Filter-Wirksamkeit: 90–95% UV-Blockade
- Kosten: In Lack-Preis enthalten (keine Zusatzkosten)

### 3.3 Farbton-Management

**Fading-Prognose:**
- Südseite Fenster: 20–30% Farbverlust über 10 Jahre (ohne UV-Schutz)
- Nördseite: 5–10% Farbverlust
- Mit UV-Fensterfolie: <5% Farbverlust über 10 Jahre

**Reparatur verblasster Bereiche:**
- Kleine Flächen: Gezielter Farb-Ausgleich (Lack oder Öl)
- Große Flächen: Komplette Neulackierung (teuer)
- Prävention: UV-Schutz installieren VOR Degradation

---

## 4. Salzwasser-Korrosions-Management

### 4.1 Salzwasser-Exposition-Zonen

**Innen-Bereiche mit Salzwasser-Risiko:**
1. **Bilgen-Nähe:** Spritzer durch Bilgen-Pumpe möglich
2. **Untere Kabinen-Wände:** Eindringung durch undichte Fenster
3. **Grenzflächen:** Bordwand-Decke (Kondenswasser + Salzwasser)

**Schutz-Maßnahmen:**

#### Metall-Beschläge (316L Edelstahl erforderlich)
- **Reinigung:** Monatlich mit Süßwasser + Tuch
- **Öl-Schutz:** Nach Reinigung leichtes Öl (Silikon-Spray) auftragen
- **Wachs-Versiegelung:** Jährlich (Autowachs geht auch)
- Kosten: 50–150 €/Jahr

#### Holz-Beschichtung in Salzwasser-Zone
- **Finish:** Polyurethane-basiert besser als Öl
- **Häufigkeit:** Jährliche Neulackierung
- **Spezial-Primer:** Epoxy-Primer mit Fungizid + Korrosions-Inhibitor
- Kosten: 200–400 €/Fläche jährlich

#### Kupfer/Messing-Beschläge
- **Patina-Entwicklung:** Normal (optisch OK, aber monatsweise reinigen)
- **Flugrost-Entfernung:** Mit Zahnbürste + Essig (monatlich)
- **Lackschutz:** Klarlack-Beschichtung (100–150 €) oder akzeptiere Patina

### 4.2 Rost-Entfernung & Prävention

**Früherkennung Rostansatz:**
- Kleine rote/braune Flecken auf Edelstahl
- Grüne Verfärbung (Kupfer/Messing)
- Weiße Kristalle (Salz-Ausblühung)

**Reinigung:**
1. **Mechanisch:** Stahlwolle (fein, 0000er) + Öl reiben (30 min)
2. **Chemisch:** Zitronensäure-Lösung (natürlich) oder Phosphorsäure-Sprüh (RostConverter)
3. **Nachschutz:** Öl oder Wachs auftragen nach Trocknung

**Kosten:** 20–50 € Material, Arbeit = Eigenleistung oder 50 €/h Fachmann

---

## 5. Schimmel-Prävention & Feuchte-Management

### 5.1 Luftzirkulation & Belüftungs-Stragegie

**Kritische Räume:**
- Schlafkabinen (stehende Luft, Feuchtigkeit)
- Bad/Kopfsteinzone (höchste Feuchte)
- Engine Room (Kondenswasser-Bildung)
- Speisekammer (Lebensmittel + Feuchte)

**Belüftungs-Mindestanforderung:**
- Sommer: 4–6 Stunden/Tag Querlüftung (Luken offen)
- Winter: 2–4 Stunden/Tag (verursacht Wärmeverlust, aber nötig)
- Nachts: Mindestens 1–2 Stunden nach Sonnenuntergang

**Technische Lüftung:**
| System | Kosten | Wirksamkeit | Wartung |
|--------|--------|-----------|---------|
| Solar-Ventilator | 100–200 € | Gut tagsüber | 6-monatliche Kontrolle |
| 12V Gebläse | 150–300 € | Gut (aktiv steuerbar) | Jährliche Kontrolle |
| Deckenventilator | 200–500 € | Gut (auch Luftzirkulation) | Wartung wie Schiffe-Motor |
| Kanalwerk mit Filters | 800–1500 € | Sehr gut | Monatliche Filter-Wechsel |

**DIY-Lösung:**
- Offene Luke + strategische Gebläse-Positionierung
- Kosten: 50–100 € (kleine Ventilatoren)

### 5.2 Hygrometer & Feuchte-Kontrolle

**Zielwerte:**
- 40–60% RH ideal
- 60–70% RH akzeptabel
- >70% RH Warnung
- >80% RH kritisch

**Geräte:**
- Digitales Hygrometer: 20–80 € (genau, einfach)
- Beschlag-Fenster Test: Kostenlos, aber weniger präzise
- Professionelle Messung: 500–1000 € (seltener nötig)

**Platzierung Hygrometer:**
- Wohnbereiche: 5–10 verschiedene Positionen
- Kontinuierliche Messung (oder tägliche Kontrolle)
- Log führen (monatliche Durchschnitte)

### 5.3 Trocknungs-Protokoll nach Wasser-Eindringung

**Ursachen-Vorkommen:**
- Undichte Fenster/Bullaugen (häufig)
- Defekte Dachwassablauf-Systeme
- Lecks in Kabinen-Decken
- Überschwemmung durch Seegang

**Notfall-Maßnahmen (erste 24 Stunden):**
1. Feuchtigkeitsquelle stoppen (Fenster schließen, Leck abdichten)
2. Offene Luken + max. Gebläse (Belüftung)
3. Heizung max. (wenn möglich, ohne Feuer-Risiko)
4. Dehumidifiers einschalten (falls vorhanden)
5. Alle Schränke öffnen (Luft-Zirkulation)
6. Feuchte-Messungen alle 2–4 Stunden

**Langfristige Trocknung (1–2 Wochen):**
- Geheizt + belüftet kontinuierlich
- Tägliche Feuchte-Kontrolle
- Zielwert: <60% RH erreichen
- Kosten: ~5–10 € Heiz-Energie/Tag + Gebläse

**Nachbehandlung bei Schimmel-Risiko:**
- Oxalsäure-Behandlung wenn schwarze Flecken sichtbar
- Komplette Neulackierung betroffener Flächen
- Kosten: 300–1000 € (je nach Umfang)

---

## 6. Leder & Kunstleder-Pflege

### 6.1 Material-Charakteristiken

**Echtleder (marine-typisch Leder):**
- Material: Rindsleder, oft mit chromarer Gerbung
- Oberflächenschutz: Wachs, Öl, oder Versiegelung
- Empfindlichkeit: Sehr hoch gegen UV + Wasser

**Kunstleder (Vinyl, Polyurethan-Oberflächenschicht):**
- Material: Basis (Polyester) + Kunststoff-Oberflächenschicht
- Oberflächenschutz: UV-Additive
- Empfindlichkeit: Mittel gegen UV, Gut gegen Wasser

### 6.2 Wartungs-Protokoll

**Monatliche Reinigung:**
1. Oberflächenstaub: Weiches Tuch abwischen (kein Wasser)
2. Flecken: Mit feuchtem Tuch (nur Wasser) reiben
3. Trocknen: Schnell mit Tuch trocknen (nicht austrocknen lassen)

**Jährliche Pflege:**

#### Echtleder:
- **Reiniger:** Ledershampoo (20–30 € pro Flasche)
- **Prozess:** Aufschäumen + Abwischen + Trocknen
- **Öl/Wachs:** Lederöl oder Bienenwachs-Creme auftragen (10–20 €)
- **Trocknung:** 24h vor Benutzung
- Kosten: 50–100 € jährlich (Material + Zeit)

#### Kunstleder:
- **Reiniger:** Mildes Seifenwasser oder UV-Schutz-Spray
- **Prozess:** Abwischen + trocknen
- **UV-Schutz:** Jährliche Behandlung mit UV-Spray (15–30 €)
- Kosten: 20–50 € jährlich

### 6.3 Häufige Leder-Probleme

| Problem | Ursache | Lösung | Kosten |
|---------|---------|--------|--------|
| Rissbildung | UV-Strahlung + Austrocknung | UV-Fensterfolie, regelmäßiges Ölen | 100–200 € |
| Schimmel | Feuchte >70% RH | Belüftung, Oxalsäure-Behandlung | 50–150 € |
| Verfärbung | Salzwasser-Tropfen | Sofort abwischen, Lederöl | 10–20 € |
| Verschleißstellen | Normale Abnutzung | Lokale Reparatur oder Austausch | 200–500 € |

---

## 7. Möbel-Schutz & Vibrations-Reduktion

### 7.1 Schiffsbewegung & Verschleiß

**Typische Verschleißmuster:**
- Schublade-Bewegung erzeugt Kratzer (hinter Schiene)
- Türe-Bewegung erzeugt Gelenksverschleiß
- Möbel-Bewegung erzeugt Lärm/Vibration
- Gegenstände verschieben sich bei Seegang

**Prävention:**
1. **Unterlegmatten:** Gummi oder Kork unter Möbel-Füße (30–80 €/Set)
2. **Vibrations-Dämpfer:** Kleine Gummi-Pads unter Schubladen-Schienen (20–40 €)
3. **Soft-Close Systeme:** Hydraulisch/pneumatisch bremsen Bewegung (siehe Kat 28.05)

### 7.2 Belüftungs-Lücken unter Möbeln

**Wichtigkeit:**
- Ohne Belüftung staut sich Feuchte
- Schimmel-Risiko unter Matratzen, unter Schränken
- Holzquellen sichtbar (nach 1–2 Jahren)

**Minimum-Anforderung:**
- 50 mm Bodenfreiheit unter Möbeln (ideal)
- 30 mm akzeptabel (weniger, aber möglich)
- <20 mm nicht empfohlen (Schimmel-Risiko)

**Retrofit (bestehende Möbel):**
- Möbel anheben mit kleinen Keilblöcken (Holz, 50 mm hoch)
- Kosten: 50–100 € Material + Arbeit

---

## 8. Inspektions- & Wartungs-Kalender

### 8.1 Monatliches Wartungs-Checkliste

```
HOLZ-PFLEGE:
  [ ] Holzfeuchte prüfen (Messgerät, sollte 10–14% sein)
  [ ] Oberflächenfinish prüfen (Glanz, Kratzer?)
  [ ] Schimmel-Früherkennung (Flecken, Geruch?)
  [ ] Fugen inspizieren (Risse, Schmutz?)

METALLISCHE BESCHLÄGE:
  [ ] Korrosion-Check (Rost, Grünspan?)
  [ ] Oberflächenreinigung (Salzwasser abwischen)
  [ ] Schrauben-Sitz (wackeln?)

LEDER:
  [ ] Oberflächenreinigung (Tuch)
  [ ] Flecken-Behandlung (wenn nötig)
  [ ] Risse-Kontrolle (frühe Warnung)

ARBEITSPLATTEN:
  [ ] Flecken-Entfernung
  [ ] Kratzer-Kontrolle
  [ ] Fugen-Inspektion (Schimmel?)

BELÜFTUNG:
  [ ] Relative Feuchte prüfen (Hygrometer)
  [ ] Lüftungs-Öffnungen offen? (4–6 Stunden täglich)
  [ ] Gebläse funktioniert? (wenn vorhanden)
```

### 8.2 Jährliche Wartungs-Checkliste

```
HOLZ-OBERFLÄCHENFINISH:
  [ ] Komplett abschleifen + Auffrischung (Cetol/Epifanes)
  [ ] Oder monatliche Hartwachs-Öl-Auffrischung(12x im Jahr)

SCHRÄNKE & SCHUBLADEN:
  [ ] Soft-Close Scharnier prüfen (Öl-Lecks?)
  [ ] Schienen schmieren (Silikon-Spray)
  [ ] Schrauben alle straffen

KORROSIONS-SCHUTZ:
  [ ] Alle Edelstahl-Beschläge polieren + Wachs
  [ ] Kupfer-Flecken mit Essig entfernen
  [ ] Engine Room: Öl-Schutz erneuern

LEDER:
  [ ] Intensive Reinigung (Ledershampoo)
  [ ] Öl-Behandlung
  [ ] UV-Fensterfolie prüfen (Verschleiß?)

UV-SCHUTZ:
  [ ] Fensterfolien prüfen (Risse, Ablösungen?)
  [ ] Rollos funktionieren? (Witterung)
  [ ] Farbtöne prüfen (Vergilbung sichtbar?)

BELÜFTUNGS-SYSTEM:
  [ ] Gebläse-Filter wechseln
  [ ] Lüftungs-Kanäle prüfen (Verstopfung?)
  [ ] Hygrometer kalibrieren

FEUCHTE-KONTROLLE:
  [ ] Jährliche Durchschnitt berechnen
  [ ] Langfristige Trend prüfen (steigt an?)
  [ ] Gegenmittel planen (Lüftung, Heizung)

DOKUMENTATION:
  [ ] Wartungs-Log aktualisieren
  [ ] Fotos vor/nach Arbeiten
  [ ] Reparatur-Rechnungen archivieren
```

### 8.3 5-Jahres-Groß-Wartung (Professionell)

- Komplette Holz-Neubeschichtung in kritischen Zonen
- Tiefenversiegelung aller Arbeitsplatten
- Möbel-Kontrolle auf Delaminierung/Quellung
- Leder-Restauration (falls große Schäden)
- Elektrolytische Entrostung von Metallen (falls nötig)
- Schimmelpräventions-Tiefenbehandlung (wenn Feuchte-Problem)
- Kosten: 2000–5000 € (je nach Schiffsgröße)

---

## 9. Spezial-Reinigungsmittel & -Techniken

### 9.1 Empfehlung Reinigungsmittel

**Allgemein-Reiniger:**
- **Neutral-Reiniger pH 6–8:** Seifen, pH-neutrale Detergentien (20–40 € pro Liter)
- **Beispiele:** Pril, Fairy (Spülmittel)
- **Anwendung:** 1 Teil Reiniger : 10 Teile Wasser (nicht zu konzentriert)

**Spezial-Reiniger nach Material:**

| Material | Reiniger | Kosten | Vorsicht |
|----------|----------|--------|---------|
| Holz (allgemein) | Neutral-Reiniger + Wasser | 5–10 € | Nicht zu nass (Quellung) |
| Teak | Oxalsäure (Flecken) | 15–25 € | Handschuhe! Säure-Kontakt |
| Edelstahl | Edelstahl-Reiniger (pH 7–8) | 15–30 € | Nicht mit Chlorid-Reinigern |
| Leder | Ledershampoo | 20–40 € | Nicht zu viel Wasser |
| Laminate | Neutral-Reiniger | 5–10 € | Minimal Wasser (Quellung-Risiko) |
| Granit | Neutral-Reiniger (nicht sauer!) | 10–20 € | Keine Säure (Loch-Fraß) |
| Glas | Glasreiniger (Ethanol-basiert) | 5–15 € | Streifenfrei austrocknen |

### 9.2 Hochdruck-Reinigung (Grenzen)

**Gefahren im Boot-Interieur:**
- Wasser-Eindringung durch Dichtungen
- Material-Erosion (zu hoher Druck)
- Schimmel-Sporen in Luft verteilt

**Empfehlung (KORRIGIERT, web-verifiziert):**
- **Hochdruckreiniger gehören NICHT ins Interieur.** Kein sinnvoller Druckwert existiert — jede Strahlanwendung im Innenraum treibt Wasser hinter Verkleidungen, in Furnier-Kanten und durch Fenster-/Lukendichtungen.
- Zur Einordnung: Selbst der *für Auto-Aussenlack sichere* Druck liegt nur bei ca. **8–10 bar (≈120–140 psi)**, oberhalb ~13 bar / 2000 psi drohen Lack- und Dichtungsschäden (Quelle: Autopflege-Fachquellen). Die früher hier genannten "250–300 bar" bzw. "500+ bar wie Auto" waren falsch — Konsumenten-Hochdruckreiniger liefern typisch nur ~100–150 bar *am Gerät*, und für Lack/Dichtung relevant ist der weit niedrigere Wirk-Druck an der Oberfläche.
- Confidence: `documented` (Autopflege-Fachquellen). Marine-Interieur-Grenzwert: es gibt keinen — Anwendung unterlassen.

**Besser (verbindliche Interieur-Methode):** Feuchte (nicht nasse) Mikrofaser-Bürste + sofortige Lappen-Trocknung. Kontrolliert, keine Wasser-Eindringung, keine Faser-Erosion.

> Quellen (Druck-Verifikation): [autozcrave.com – Best PSI & BAR for car washing](https://autozcrave.com/best-psi-bar-settings-car-wash) · [cardetailingplanet.com – Pressure Washer PSI for Cars](https://cardetailingplanet.com/psi-safe-wash-your-car/)

---

## 10. Dokumentation & Wartungs-Log

### 10.1 Wartungs-Logbuch (Digital oder Papier)

**Eintrag-Format:**
```
Datum: [TT.MM.JJJJ]
Bereich: [Holz/Metall/Leder/etc.]
Zone: [Salon/Kabine_Backbord/etc.]
Tätigkeit: [kurze Beschreibung]
Material-Verbrauch: [Menge, Kosten]
Arbeitsstunden: [Eigene oder Fachmann]
Kosten-Gesamt: [€]
Nächste geplante Wartung: [Datum]
Notizen: [Besonderheiten, Probleme, Empfehlungen]
```

**Beispiel-Eintrag:**
```
Datum: 2026-04-15
Bereich: Holz-Finish
Zone: Salon Teak
Tätigkeit: Jährliche Auffrischung Cetol UV
Material: 0.5 L Cetol UV (40 €), Schleifpapier (5 €)
Arbeit: 4h Eigene Arbeit
Kosten-Gesamt: 45 €
Nächste: April 2027
Notizen: Kleine Kratzer entfernt, Finish gleichmäßig aufgetragen
```

### 10.2 Digitale Tools

**Empfehlung:**
- Excel/Google Sheets: Einfach, durchsuchbar, synchron
- Spezielle Apps (z.B. MyBoatLog): Automatische Erinnerungen
- Fotos: Vergleich Vor/Nachher (für Resale-Wert)

**Wichtig für Resale-Wert:**
- Vollständiges Wartungs-Log (>50% höherer Resale-Preis!)
- Professionelle Inspektionen dokumentiert
- Material-Herkunft (Originalteile vs. Ersatz) notiert

---

## 11. Fehlermuster & Häufige Wartungs-Fehler

### FB-28-07-001 — Vernachlässigung (häufigster Fehler)

**Symptom:**
- Schimmel in Ecken
- Holz-Quellung sichtbar
- Rost auf Beschlägen
- Leder rissig
- Oberflächenfinish matt/grau

**Vermeidung:**
- Monatliche Checkliste befolgen
- Belüftung aktiv halten
- Kleine Probleme sofort beheben

### FB-28-07-002 — Zu aggressive Reinigung

**Symptom:**
- Oberflächenrauheit (Material abgerieben)
- Kratzer + Dellen
- Hochdruckreiniger-Schäden

**Vermeidung:**
- Sanfte Tücher (Mikrofaser bevorzugt)
- Neutrale pH-Reiniger nur
- Keine Scheuermittel auf empfindliche Flächen

### FB-28-07-003 — Falsche Putzmittel verwendet

**Beispiel:**
- Chlor-Reiniger auf Edelstahl → Loch-Fraß
- Säure auf Granit → Oberfläche matt
- Zu viel Wasser auf Holz → Quellung

**Vermeidung:**
- Immer material-spezifische Reiniger verwenden
- PH-Wert prüfen (6–8 sicher)
- Testfläche zuerst

---

## ANHANG A — Pydantic v2 Modelle für Backend-Wartungs-Tracking

```python
from pydantic import BaseModel, Field, validator
from enum import Enum
from typing import List, Optional
from datetime import datetime, timedelta

class MaintenanceType(str, Enum):
    WOOD_FINISHING = "wood_finishing"
    METAL_PROTECTION = "metal_protection"
    LEATHER_CARE = "leather_care"
    VENTILATION = "ventilation"
    MOLD_PREVENTION = "mold_prevention"
    UV_PROTECTION = "uv_protection"
    GENERAL_CLEANING = "general_cleaning"
    INSPECTION = "inspection"

class MaintenanceFrequency(str, Enum):
    MONTHLY = "monthly"
    QUARTERLY = "quarterly"
    ANNUALLY = "annually"
    EVERY_5_YEARS = "every_5_years"
    AS_NEEDED = "as_needed"

class MaintenanceRecord(BaseModel):
    model_config = {"from_attributes": True}
    
    record_id: str
    maintenance_type: MaintenanceType
    zone: str  # "salon", "master_cabin", etc.
    performed_date: datetime
    next_due_date: datetime
    frequency: MaintenanceFrequency
    material_cost_eur: float = 0.0
    labor_cost_eur: float = 0.0
    materials_used: List[str] = []  # "Cetol UV 0.5L", "Oxalsäure-Lösung", etc.
    labor_hours: float = 0.0
    notes: str
    performed_by: str  # "Owner", "Fachmann John", etc.
    photos_before_url: Optional[List[str]] = None
    photos_after_url: Optional[List[str]] = None

class MaintenanceSchedule(BaseModel):
    model_config = {"from_attributes": True}
    
    schedule_id: str
    zone_id: str
    material_type: str  # "teak", "edelstahl", "corian", etc.
    maintenance_type: MaintenanceType
    frequency: MaintenanceFrequency
    estimated_cost_per_cycle_eur: float
    last_performed: Optional[datetime] = None
    next_due_date: datetime
    estimated_hours_per_cycle: float
    instructions: str
    critical: bool = False  # Flag für überfällige Wartung

class InteriorHealthReport(BaseModel):
    model_config = {"from_attributes": True}
    
    vessel_id: str
    analysis_date: datetime
    humidity_avg_rh: float = Field(0.0, ge=0.0, le=100.0)
    humidity_status: str = Field("good", pattern="^(good|warning|critical)$")
    mold_risk_zones: List[str] = []
    uv_exposure_high_zones: List[str] = []
    maintenance_records_count: int
    last_5_years_maintenance_cost_eur: Optional[float]
    estimated_next_year_cost_eur: Optional[float]
    critical_maintenance_items: List[str] = []
    recommendations: List[str]
    overall_interior_condition_score: float = Field(0.0, ge=0.0, le=100.0)
```

---

## ANHANG B — Ersatzteil & Material-Lagerbestand

**Empfohlen zu lagern (für Eigene Wartung):**

| Material | Menge | Kosten | Lagerort |
|----------|-------|--------|----------|
| Cetol UV | 1 L | 80–100 € | Dunkel, kühl |
| Hartwachs-Öl | 0.5 L | 30–40 € | Dunkel, kühl |
| Polyurethane-Kleber | 1 Tube | 15 € | Kühl (2K trennt sich) |
| Holzfeuchtemessgerät | 1 Stück | 50–100 € | Trocken |
| Schleifmittel-Set | Körnung 80–400 | 20–30 € | Trocken |
| Ledershampoo | 0.5 L | 20 € | Dunkel, kühl |
| Oxalsäure (Pulver) | 500 g | 15 € | Dunkel, kühl, Gift-Label |
| Edelstahl-Reiniger | 1 L | 20 € | Beliebig |
| Silikon-Spray | 1 Dose | 8–12 € | Beliebig |
| Diverse Bürsten/Tücher | Set | 30–50 € | Trocken |

**Gesamt Lagerbestand:** 250–400 € (amortisiert über 2–3 Jahre Wartung)

---

## Zusammenfassung & Empfehlung

**Kernstragie für langlebiges Interieur:**

1. **Prävention:** Monatliche Belüftung + Feuchte-Kontrolle (beste Investition)
2. **Material-Bewusstsein:** Unterschiedliche Materialien = unterschiedliche Pflege
3. **Regelmäßigkeit:** Jährliche Auffrischung länger als Notfall-Reparaturen
4. **Dokumentation:** Log führen = besserer Resale-Wert + Wissenstransfer

**Kosten über 10 Jahre Schiffsbetrieb:**
- **Vernachlässigung:** 0 € → Schäden nach 5 Jahren = 5000–15000 € Reparaturen
- **Proaktive Pflege:** 500–800 €/Jahr = 5000–8000 € über 10 Jahre = Schiff wie neu
- **ROI:** 100% (Reparaturkosten vermieden > Wartungskosten)

**Zeitaufwand:**
- Monatlich: 2–3 Stunden (Begehung + Kontrolle)
- Jährlich: 10–20 Stunden intensiv
- Gesamt: ~50 Stunden/Jahr (< 1 Stunde/Woche)

---

## 12. Holzfeuchte ↔ Raumluft-Feuchte: verifizierte EMC-Referenz

Die in Abschnitt 2.1 genannten „10–14 % Holzfeuchte (marine Standard)" sind ein **betrieblicher Toleranzbereich** für Marine-Interieure — nicht der Konstruktions-Zielwert der Tischlerei. Der physikalische Zusammenhang (Ausgleichsfeuchte, engl. *equilibrium moisture content*, EMC) ist web-verifiziert:

| Raumluft (RH bei ~21 °C) | Holz-Ausgleichsfeuchte (EMC) | Einordnung | Confidence |
|---|---|---|---|
| 30 % RH | ~6 % | zu trocken → Schwind-/Rissgefahr an Furnier | `documented` |
| 40–45 % RH | ~8 % | **Konstruktions-Zielwert für Möbel/Innenausbau** | `documented` |
| 50 % RH | ~9 % | ideal, langzeitstabil | `documented` |
| 30–50 % RH (Band) | 6–9 % EMC | empfohlenes Innenraum-Band | `documented` |
| 60 % RH | ~11 % | oberes Limit, EMC steigt überproportional | `documented` |
| > 85 % RH | > 16 % (stark steigend) | Quellung, Schimmel-Terrain | `documented` |

> Quellen: [wood-database.com – Wood and Moisture](https://www.wood-database.com/wood-and-moisture/) · [wagnermeters.com – How RH Affects Wood MC](https://www.wagnermeters.com/moisture-meters/wood-info/how-rh-affects-wood-mc/)

**Interpretation für die Werft:** Ein gemessener Holzfeuchte-Wert von 12–14 % im laufenden Bootsbetrieb ist normal (Marine-Ambiente liegt feuchter als eine beheizte Wohnung), signalisiert aber, dass die Raumluft dauerhaft eher bei 55–65 % RH liegt — also nahe der Schimmel-Warnschwelle (Abschnitt 0.2). Werte **> 16 %** korrespondieren mit > 85 % RH und sind ein Quell-/Schimmel-Alarm. Der Konstruktions-Zielwert von ~8 % (40–45 % RH) ist an Bord im Sommer selten dauerhaft haltbar; entscheidend ist Stabilität statt Absolutwert — starke, schnelle Schwankungen reissen Furnier eher als ein konstant leicht erhöhtes Niveau.

---

## 13. Verifizierte Produkt- & Verfahrensdaten (Holz-Finishes)

Nur reale, am Markt verfügbare Systeme mit herstellerbelegten Kennwerten. Preise sind Marktschätzungen (`estimated`), technische Kennwerte sind herstellerbelegt (`documented`).

### 13.1 Sikkens Cetol Marine (dünnschicht, penetrierend)

| Kennwert | Wert | Confidence |
|---|---|---|
| Theoretische Ergiebigkeit | ~305–400 ft²/gal ≈ **7,5–9,8 m²/L** pro Schicht (Erstschicht auf Rohholz weniger, da penetrierend) | `documented` |
| Trocknung bis Überarbeitung | **24 h** aushärten vor nächster Schicht | `documented` |
| Aufbau-Fenster | alle Schichten innerhalb **1–2 Wochen** auftragen | `documented` |
| Unterhalt | **jährliche** Pflegeschicht; bei Überschreiten des 1-Jahres-Intervalls deutlich aufwändigere Wiederherstellung | `documented` |

> Quelle: [Jamestown Distributors – Sikkens Cetol Marine application](https://support.jamestowndistributors.com/hc/en-us/articles/360015442354-Sikkens-Cetol-Marine-application) · [AkzoNobel – Cetol Marine Guide (PDF)](https://specialtycoatings.brand.akzonobel.com/m/3bab590623c6b32b/original/cetol-marine-guide.pdf)

### 13.2 Epifanes Clear (Gloss) Varnish (dickschicht, hochglänzend)

| Kennwert | Wert | Confidence |
|---|---|---|
| Festkörper | 50 ± 2 Vol-%; Dichte 0,92 kg/dm³ | `documented` |
| Applikations-Bedingungen | **8–30 °C**, relative Luftfeuchte **50–75 %** | `documented` |
| Unterhalt (Sonnenexposition) | bei voller Sommer-Sonne **2–4 Schichten/Jahr**; abgedeckte Flächen ggf. nur 1–2 Schichten alle paar Jahre | `documented` |
| Lagerfähigkeit | ~3 Jahre, geschlossen, dunkel, 5–25 °C | `documented` |

> Quelle: [Epifanes Clear Varnish – Technical Datasheet (PDF)](https://galwaymaritime.com/wp-content/uploads/2021/03/Epifanes-Clear-Varnish-Technical-Datasheet.pdf) · [epifanes.com – Clear Finishes](https://www.epifanes.com/page/clear-finishes)

### 13.3 Osmo Hartwachs-Öl Original (Innenraum, Öl/Wachs)

| Kennwert | Wert | Confidence |
|---|---|---|
| Basis | natürliche Pflanzenöle (Sonnenblume, Soja, Distel) + Wachse, entaromatisiertes Testbenzin (benzolfrei) | `documented` |
| Verbrauch | ~**35 ml/m²** (Bodenbürste), ~25 ml/m² (Möbel-Pad), ~16 ml/m² (Mikrofaser-Rolle) | `documented` |
| Auftrag | Rohholz 2 Schichten; **Renovierung meist 1 Schicht ohne Zwischenschliff** | `documented` |
| Trocknung | 8–10 h (farblos) bzw. 24 h (Natural/getönt), gute Belüftung | `documented` |

> Quelle: [osmo.de – Hartwachs-Öl Original](https://www.osmo.de/en/finishes/interior-finishes/finishes-for-flooring/hartwachs-oel-original)

**Verfahrensmerker (herstellerübergreifend belegt):** Cetol/Öl-Systeme sind *penetrierend/dünnschichtig* und werden „nass in die Fläche aufgefrischt" (wenig bis kein Schliff); klassischer Klarlack (Epifanes) baut *Schichtdicke* auf, braucht Zwischenschliff und ist bei UV-Belastung schicht-hungriger. Systeme **nicht mischen** ohne Verträglichkeitsprüfung — Öl unter Lack führt zu Haftungsverlust.

---

## 14. Zwei-Komponenten-Teakreiniger & Oxalsäure: Wirkprinzip und Grenzen

Der in Abschnitten 2.3/4.2/9 genannte Oxalsäure-Einsatz ist verifiziert — mit einer wichtigen Materialkunde-Warnung:

- **Aufbau der 2-Komponenten-Reiniger:** Teil 1 = alkalischer/kaustischer Reiniger (typisch TSP, Natriumsilikat oder Natriumpercarbonat) löst die graue Vergrauungsschicht; Teil 2 = **Oxalsäure** als Aufheller, bricht Flecken und neutralisiert. Confidence: `documented`.
- **Wirk-Nebenwirkung:** Der Prozess trägt die weiche Frühholz-Faser mit ab — das „graue Wasser" beim Schrubben ist teils abgetragenes Teak. Pro aggressiver Reinigung können bis zu ~0,010 inch (≈0,25 mm) Oberfläche verloren gehen. Confidence: `documented`.

> Quellen: [Practical Sailor – Two-Part Teak Cleaners](https://www.practical-sailor.com/boat-maintenance/two-part-teak-cleaners/) · [KKMI – How to clean teak decks](https://www.kkmi.com/clean-teak-decks/)

**Interieur-Konsequenz:** Für Innen-Teak (Sohlen, Handläufe, Verkleidung) sind aggressive 2-Komponenten-Systeme **selten angebracht** — sie „verjüngen" optisch, kosten aber Substanz und müssen anschliessend zwingend neu versiegelt/geölt werden. Bevorzugt: milde Reinigung (Abschnitt 9.1) + Auffrischung des Finishes. Oxalsäure gezielt nur für **punktuelle** Wasser-/Schwarzflecken und Schimmel-Sanierung einsetzen; Handschuhe/Augenschutz (Oxalsäure ist giftig, GHS).

---

## 15. Feuchte-Absorber: Calciumchlorid vs. Silikagel (verifiziert)

Ergänzung zu Abschnitt 5 für Winterlager/Nicht-Nutzung ohne Landstrom:

| Kenngrösse | Silikagel | Calciumchlorid (CaCl₂) | Confidence |
|---|---|---|---|
| Wirkprinzip | Adsorption an Oberfläche | Absorption ins Innere (zerfliesst zu Sole) | `documented` |
| Aufnahme bei Sättigung | ~25–30 % des Eigengewichts | **> 250 %** des Eigengewichts bei ~90 % RH | `documented` |
| Kapazität-Verhältnis bei hoher RH | Referenz | **~10× höher** als Silikagel bei 90 % RH | `documented` |
| Einsatzfeld | niedrige RH, wiederverwendbar (regenerierbar) | **hohe RH / Langzeit** (Winterlager, feuchtes Ambiente) | `documented` |

> Quellen: [streampeak.com.sg – Silica Gel vs Calcium Chloride](https://streampeak.com.sg/moisture-absorbers/silica-gel-vs-calcium-chloride/) · [West Marine – Boat Dehumidifiers & Moisture Absorbers](https://www.westmarine.com/dehumidifiers/)

**Praxis-Regeln (verifiziert):**
- Belüftung ist die wirksamste Grund-Massnahme; passive Absorber und/oder ein niederwattiger Marine-Entfeuchter ergänzen. Schimmel kann bereits ab ~60 % RH beginnen → Ziel dauerhaft **< 60 % RH**. Confidence: `documented`. Quelle: [Defender – Prevent Mold & Mildew in Winter Storage](https://defender.com/en_us/winterizing-guide/mold-mildew-prevention).
- CaCl₂-Boxen (z. B. unter Kojen, in Pantry, nahe Elektronik) platzieren; die abgeschiedene **Sole ist korrosiv** — Auffangbehälter regelmässig leeren, Kontakt mit Metall/Textil vermeiden.
- Bei Schrumpffolien-Winterlager Lüftungsöffnungen/Solar-Lüfter einplanen — sonst kondensiert Feuchte unter der Folie.

---

## 16. Leder- & Marine-Vinyl-Pflege: Korrekturen und Werkstoffregeln

Ergänzung/Präzisierung zu Abschnitt 6 (web-verifiziert):

### 16.1 Echtleder (meist chromgegerbt an Bord)

- **pH-neutral, wasserbasiert, sparsam:** Chromgegerbtes Leder braucht leichte, pH-ausgewogene Reiniger und *milchige/wasserbasierte* Pflege in dünner Schicht. **Über-Pflege** mit schweren Ölen verstopft die dichtere Narbe und hinterlässt Fettfilm. Confidence: `documented`.
- **Sattelseife vermeiden** auf modernem/fein zugerichtetem Möbelleder — sie reinigt zu aggressiv, kann Öle herausziehen und Farbe aufhellen. Confidence: `documented`.
- Ablauf: entstauben → milde Seifenlösung mit weicher Bürste → mit klarem Wasser abnehmen → **vollständig lufttrocknen** → erst dann konditionieren.

> Quellen: [Stridewise – Chromexcel / Chrome-tan care](https://stridewise.com/chromexcel-leather-care/) · [ColsenKeane – Saddle Soap & Oils mistakes](https://colsenkeane.com/blogs/leather-insights-navigating-patina-styles-and-traditional-craftsmanship/avoid-these-leather-care-mistakes-a-short-guide-to-saddle-soap-and-oils)

### 16.2 Marine-Vinyl (Kunstleder-Polster)

- **NIEMALS Chlorbleiche** oder bleich-/ammoniak-/scheuerhaltige Reiniger: sie greifen das Vinyl chemisch an, machen es spröde, zerstören Nähte und hinterlassen dauerhaften Gelbstich; sie strippen die Weichmacher/Schutzschicht. Confidence: `documented`.
- **Schimmel:** dedizierten Marine-Schimmel-/Stockflecken-Entferner verwenden, mit weicher Bürste (alte Zahnbürste) in Narbe und Naht einarbeiten, Einwirkzeit lt. Etikett, dann gründlich mit Süsswasser spülen. Ziel: Schimmel **abtöten**, nicht nur den Fleck ausbleichen. Confidence: `documented`.
- **Milde DIY-Alternative:** Weissweinessig 1:1 mit Wasser gegen Stockflecken/leichte Verschmutzung. Immer **lufttrocknen** (Restfeuchte fördert Neubefall). Confidence: `documented`.

> Quellen: [Sailrite – How to Clean Marine Vinyl](https://www.sailrite.com/how-to-clean-marine-vinyl) · [Mercury Marine – Clean & Care for Boat Vinyl](https://www.mercurymarine.com/ca/en/lifestyle/dockline/how-to-clean-and-care-for-boat-vinyl)

> Merker: Die Essig-Empfehlung gilt für **Vinyl/Leder-Flecken**, NICHT für **Naturstein** (Granit/Marmor) — dort ätzt Säure (siehe Abschnitt 9.1 „Granit: keine Säure").

---

## 17. Fehlerbild-Atlas (Interieur-Wartung)

IDs im kollisionsfreien Schema **FB-28-07-NNN**, fortgeführt ab den bestehenden FB-28-07-001…003 (Abschnitt 11). Jedes Fehlerbild: Symptom → Ursache → Diagnose → Massnahme → Prävention.

### FB-28-07-004 — Furnier-Aufwölbung/Blasenbildung an Kanten
- **Symptom:** Furnier hebt sich an Rändern/Fugen, Blasen, dunkle Verfärbung darunter.
- **Ursache:** Feuchte-Eintritt über ungesiegelte Kante; Holzfeuchte > 16 % (≈ > 85 % RH, Abschnitt 12); Klebstoffversagen.
- **Diagnose:** Holzfeuchtemessung an Kante; RH-Log prüfen; Delaminierung durch Abklopfen (hohler Klang).
- **Massnahme:** Ursache (Leck/Belüftung) beheben → trocknen bis < 12 % → Kante nachsiegeln (Epoxy/PU); grossflächig = Furnier-Austausch.
- **Prävention:** Kanten IMMER versiegeln (Abschnitt 2.2); 50 mm Belüftungsspalt; RH < 60 %.

### FB-28-07-005 — Schwarze Punkt-/Stockflecken auf Vinyl-Polster
- **Symptom:** kleine schwarze Punkte in Narbe und entlang Nähten.
- **Ursache:** Schimmel/Stockflecken bei > 60–70 % RH; Restfeuchte nach Reinigung; Hautfette als Nährboden.
- **Diagnose:** riecht muffig; Punkte sitzen in Narbe (nicht abwischbar).
- **Massnahme:** Marine-Schimmelentferner + weiche Bürste einarbeiten, spülen, **lufttrocknen** (Abschnitt 16.2). KEINE Bleiche.
- **Prävention:** nach Nutzung trocknen/lüften; RH < 60 %; Belüftung unter Polstern.

### FB-28-07-006 — Tea-Staining an „Edelstahl"-Beschlägen
- **Symptom:** bräunlicher Belag/rote Pünktchen auf vermeintlich rostfreiem Stahl.
- **Ursache:** oft 304 statt 316L in Salzatmosphäre; Chlorid-Angriff; Ablagerung + stehende Salzfeuchte. (Werkstoff: 316L Pflicht im Salzwasser — vgl. Projekt-Materialdomäne.)
- **Diagnose:** Belag mit mildem Edelstahlreiniger entfernbar? Wiederkehr an gleicher Stelle → Werkstoff-/Spaltproblem.
- **Massnahme:** milder Edelstahlreiniger (pH 7–8), **keine chloridhaltigen Reiniger**; danach Wachs/Öl-Schutz. Wiederkehrend → Beschlag auf 316L tauschen.
- **Prävention:** monatlich Süsswasser abwischen; jährlich wachsen; Chloridreiniger meiden (vgl. FB-28-07-008).

### FB-28-07-007 — Muffiger Dauergeruch trotz sauberer Oberflächen
- **Symptom:** Geruch kehrt nach Lüften zurück, keine sichtbaren Flecken.
- **Ursache:** verborgener Schimmel an kalten Oberflächen (Rumpf hinter Möbeln, Bilge, unter Kojen); lokale Oberflächen-RH > 70 % trotz „grünem" Raum-Hygrometer (Abschnitt 0.2).
- **Diagnose:** Hygrometer an mehreren/kalten Punkten; Stauzonen öffnen; hinter Verkleidung/Polster prüfen.
- **Massnahme:** Quelle freilegen, Oxalsäure/Schimmelentferner materialgerecht, Ursache = Belüftung/Isolation der Kaltfläche.
- **Prävention:** Querlüftung; Absorber (Abschnitt 15); 50 mm Möbel-Bodenfreiheit; kalte Flächen beobachten.

### FB-28-07-008 — Loch-/Spaltkorrosion nach Chlor-/Bleichreiniger
- **Symptom:** punktuelle Grübchen/Löcher auf Edelstahl nach „Grundreinigung".
- **Ursache:** chlorid-/bleichhaltiger Reiniger auf 316/304 → Lochfrass; oder Bleiche auf Vinyl → Versprödung/Gelbstich.
- **Diagnose:** zeitlicher Zusammenhang mit Reinigeraktion; Reiniger-Etikett auf Hypochlorit/„Chlor" prüfen.
- **Massnahme:** irreversibel am Grundmaterial — Bauteil/Polster tauschen; Reinigerregime umstellen.
- **Prävention:** materialspezifische, chlorid-/bleichfreie Reiniger (Abschnitte 9.1, 16.2); Testfläche.

### FB-28-07-009 — Haftungsverlust neuer Finish-Schicht
- **Symptom:** frische Öl-/Lackschicht perlt ab, haftet nicht, bleibt klebrig.
- **Ursache:** inkompatible Systeme (Öl unter Lack), Rückstände von Trennmitteln/Silikonspray, zu hohe Holzfeuchte/RH ausserhalb Applikationsfenster (Epifanes: 8–30 °C, 50–75 % RH, Abschnitt 13.2).
- **Diagnose:** Untergrundhistorie klären (welches System zuletzt?); Feuchte/RH prüfen; Silikon-Kontamination (Krater).
- **Massnahme:** vollständig entfernen, Untergrund entfetten/anschleifen, systemkonform neu aufbauen im richtigen Klimafenster.
- **Prävention:** Systeme nicht mischen (Abschnitt 13); Silikonspray fern von zu lackierenden Flächen; RH/Temperatur einhalten.

### FB-28-07-010 — Riss-/Krakelee im Klarlack (UV/Schichtalterung)
- **Symptom:** feine Netzrisse, Milchigkeit, Ablösung bei dickschichtigem Klarlack an Südfenstern.
- **Ursache:** UV-Abbau + versäumtes jährliches Nachschichten; Klarlack ist bei voller Sonne schicht-hungrig (2–4 Schichten/Jahr, Abschnitt 13.2).
- **Diagnose:** Exposition prüfen (Süd/Deck); letztes Pflegeintervall im Log.
- **Massnahme:** anschleifen bis intakter Film, Aufbauschichten ergänzen; bei durchgehendem Versagen komplett strippen und neu.
- **Prävention:** UV-Schutz (Folie/Rollo, Abschnitt 3.2); jährliches Nachschichten; expositionsgerechte Schichtzahl.

---

## 18. Troubleshooting-Entscheidungsbäume

### 18.1 „Muffiger Geruch / Schimmelverdacht"
```
Sichtbare Flecken?
├─ JA → Material bestimmen
│   ├─ Holz  → Ursache (Belüftung/Leck) beheben → trocknen < 12 % → Oxalsäure → neu versiegeln (FB-004/2.3)
│   ├─ Vinyl → Marine-Schimmelentferner, KEINE Bleiche → spülen → lufttrocknen (FB-005/16.2)
│   └─ Leder → pH-neutral reinigen → trocknen → leicht konditionieren (16.1)
└─ NEIN (Geruch, keine Flecken) → Hygrometer an mehreren/kalten Punkten
    ├─ lokal > 70 % Oberflächen-RH → verborgene Kaltflächen prüfen (Rumpf/Bilge/unter Kojen) (FB-007)
    └─ überall < 60 % RH → Quelle woanders (Bilgenwasser, Tank, Abwasser) — ausserhalb dieses Dokuments
```

### 18.2 „Holzfeuchte-Messwert einordnen" (Ergänzung zu Tabelle 2.1)
```
Messwert am Bauteil?
├─ < 8 %   → sehr trocken; Schwind-/Rissrisiko an Furnier; RH anheben/stabilisieren (12)
├─ 8–12 %  → gut; Wartungsmodus
├─ 12–16 % → erhöht (Ambiente ~55–65 % RH); Belüftung erhöhen, Absorber (15), beobachten
└─ > 16 %  → Alarm (~> 85 % RH); aktive Trocknung + Ursachensuche (Leck/Belüftung) (FB-004)
```

### 18.3 „Welches Holz-Finish auffrischen — welches System?"
```
Vorhandenes System bekannt?
├─ NEIN → kleine Testfläche + Verträglichkeit prüfen (Öl/Lack nicht mischen, FB-009)
├─ Öl/Wachs (Osmo)      → reinigen → dünn auffrischen, kein/kaum Schliff (13.3)
├─ Dünnschicht (Cetol)  → reinigen → leicht anschleifen → 1 Pflegeschicht/Jahr (13.1)
└─ Klarlack (Epifanes)  → anschleifen → Aufbauschichten; Süd/Deck 2–4/Jahr (13.2)
```

---

## 19. FAQ

**F: Reicht ein Hygrometer in Kabinenmitte?**
A: Nein. Massgeblich ist die **Oberflächen**-RH an kalten Stellen (Rumpf hinter Möbeln, Fensterlaibung). Dort kann sie 70 % überschreiten, während die Raummitte 50 % zeigt. Mehrere Messpunkte, kalte Flächen gezielt (Abschnitt 0.2/5.2). `documented`

**F: Darf ich Bleiche gegen Schimmel auf Polstern nehmen?**
A: Nein. Bleiche/Chlor macht Marine-Vinyl spröde, zerstört Nähte, hinterlässt Gelbstich und strippt Weichmacher. Dedizierten Marine-Schimmelentferner oder Essig 1:1 verwenden, danach lufttrocknen (16.2). `documented`

**F: 10–14 % Holzfeuchte — ist mein Boot zu feucht?**
A: 12–14 % ist im Bootsbetrieb normal (Ambiente feuchter als Wohnung). Erst > 16 % (≈ > 85 % RH) ist ein Quell-/Schimmel-Alarm. Wichtiger als der Absolutwert ist Stabilität — schnelle Schwankungen schädigen Furnier stärker (Abschnitt 12). `documented`

**F: Öl oder Klarlack für Innen-Teak?**
A: Öl/Dünnschicht (Osmo/Cetol) = wartungsfreundlich, „nass auffrischen", natürlicher Look. Klarlack (Epifanes) = harte Schicht, hoher Glanz, aber schliff- und schicht-intensiv, v. a. an Südfenstern. Systeme nicht mischen (13, FB-009). `documented`

**F: Kann ich einen Hochdruckreiniger für hartnäckigen Innenschmutz nehmen?**
A: Nein. Kein sinnvoller Druck existiert fürs Interieur — Wasser wird hinter Verkleidungen und durch Dichtungen getrieben. Feuchte Mikrofaserbürste + Trocknung (Abschnitt 9.2). `documented`

**F: Welcher Feuchte-Absorber fürs Winterlager?**
A: Bei hoher RH/Langzeit **Calciumchlorid** (nimmt > 250 % Eigengewicht auf, ~10× Silikagel bei 90 % RH). Silikagel für niedrige RH/regenerierbar. Belüftung bleibt Grund-Massnahme; Sole ist korrosiv — Behälter leeren (Abschnitt 15). `documented`

**F: Verändert Wartung den Brandschutz?**
A: Kann sie — Neubezug von Polstern/Verkleidungen mit nicht-flammgeschütztem Material oder das Zustellen von Fluchtwegen/Wärmequellen-Abständen kann ISO-9094-Anforderungen unterlaufen. Im Zweifel CE-Handbuch/zertifizierten Ausrüster prüfen (Abschnitt 0.1). `documented`

---

## 20. Glossar

| Begriff | Bedeutung |
|---|---|
| **EMC / Ausgleichsfeuchte** | Holzfeuchte, die sich bei gegebener Raumluft-RH/Temperatur langfristig einstellt (Abschnitt 12) |
| **RH (relative Feuchte)** | Wasserdampfsättigung der Luft in %; Schimmel-Leitgrösse |
| **Oberflächen-RH** | lokale RH direkt an einer (kalten) Oberfläche; entscheidend für Schimmel, oft höher als Raum-RH |
| **Tea-Staining** | bräunlicher Oberflächenbelag auf Edelstahl in Salzatmosphäre (meist 304 statt 316L) |
| **Lochfrass/Spaltkorrosion** | punktuelle/verdeckte Chlorid-Korrosion an Edelstahl |
| **Dünnschicht-Finish** | penetrierendes Öl-/Alkyd-System (Cetol, Osmo), „nass" auffrischbar |
| **Dickschicht-Finish** | filmbildender Klarlack (Epifanes), baut Schichtdicke, schliff-/UV-intensiv |
| **Oxalsäure** | Aufheller/Rost-/Schwarzfleckenentferner; giftig (GHS), Handschuh-/Augenschutz |
| **Chromgerbung** | häufigste Ledergerbung an Bord; braucht pH-neutrale, sparsame Pflege |
| **Desiccant** | Trockenmittel; Silikagel (Adsorption) vs. Calciumchlorid (Absorption) |

---

**Ende Kat 28.07 — Interieur-Wartung & Pflege**

Version 1.1 | 2026-07-13 | erweitert auf Werft-Tiefe (Normrahmen ISO 9094/14895/12133, verifizierte EMC-/Produkt-/Desiccant-Daten, Leder-/Vinyl-Korrekturen, Fehlerbild-Atlas FB-28-07-004…010, Entscheidungsbäume, FAQ, Glossar). Alle neuen Faktenangaben web-verifiziert; unbelegte Werte als `estimated` markiert oder weggelassen.
