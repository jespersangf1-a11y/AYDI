# Kat 31.03 — Strukturberechnung

**Kategorie:** 31_Design_Konstruktion  
**Unterkategorie:** Strukturberechnung  
**Gültig ab:** 2025-01  
**Version:** 1.0  
**Sprache:** German (Inhalte), English (Code)

---

## 1. Grundlagen Strukturdesign für Boote

### 1.1 Besonderheiten des Schiffs-Strukturproblems

Bootsrümpfe unterscheiden sich fundamental von anderen Strukturen:

- **Wasserumgebung:** Korrosion, Ermüdung durch Wellenkräfte, nicht-lineares Lasten-Spektrum
- **Leichtigkeit kritisch:** Minimales Gewicht ist Kern-Anforderung (Treibstoff, Geschwindigkeit)
- **Großflächig-Schalen:** Dünnwandige FRP-Strukturen anfällig für Versagen durch Beulknicken (buckling)
- **Kombinierten Belastung:** Biegung + Torsion + Druck + dynamisch
- **Komplexe Konstruktion:** Rumpf, Deck, Kajüte, Stringers, Verstärkungen ineinandergreifend

### 1.2 Lasten auf dem Rumpf

**Hydrostatisch (Stillwasser):**
```
Druck(z) = ρ_water × g × (z_under_waterline)  [Pa]
```
Variation: 0 Pa an Wasserlinie bis max. 50–200 kPa an Kiel (abhängig Tiefgang)

**Hydrodynamisch (Seegang):**
```
Impulsive Druck durch Wellenstoß: P_wave ≈ 0.5 × ρ × v_wave²
Typisch: 50–300 kPa für Offshore-Segler
```

**Strukturlast (Eigengewicht):**
```
Eigenlast = Rumpf + Deck + Maschine + Ballast-vertikale Komponente
```

**Dynamische Beschleunigung:**
```
a_vertical = g × (1 + Beschleunigung_Seegang / g)
Seegang-Beschleunigung: 0.2g bis 1.0g abhängig Sea State
```

---

## 2. ISO 12215 — Structural Standards für Boote

### 2.1 ISO 12215-5 Scantlings (Querschnitte)

Die international anerkannte Norm für Rumpf-Scantlings (Dicken, Profile).

**Design-Lastfälle (Load Cases):**

1. **Still Water (SW):** Rumpf in Ruhe, vollbeladen
2. **Wave Bending (WB):** Schiff auf Wellenkamm vs. Wellental
   - Sagging: Welle unter Bug und Heck (Rumpf gebogen oben → Druck oben)
   - Hogging: Welle unter Mittschiff (Rumpf gebogen unten → Zug oben)
3. **Slamming:** Impact durch Bugspray oder Wellenschlag
4. **Torsion:** Winde bei Raumschot oder Ruderkräfte

### 2.2 Scantling-Berechnung (vereinfacht)

**Biegespannung (Bending Stress):**
```
σ_bending = M / W
  M = Biegemoment (kN·m)
  W = Widerstandsmoment (mm³)
```

**Scherspannung (Shear Stress):**
```
τ = V / A_shear
  V = Scherkraft (kN)
  A_shear = effektive Scherfläche (mm²)
```

**Zulässige Spannungen (Allowable):**

| Material | Zulässig Spannung (MPa) | Sicherheitsfaktor |
|----------|------------------|------------------|
| Marine Polyester Laminat | 110–140 | 2.5–3.0 |
| Epoxy-Laminat | 150–180 | 2.5–3.0 |
| Holz (Marine Plywood) | 15–25 | 2.0–2.5 |
| Aluminium (5083-H321) | 130–160 | 2.0–2.5 |
| Stahl | 200–250 | 2.0–2.5 |

---

## 3. Sandwich-Strukturen und Kern-Material

### 3.1 Klassisches Sandwich-Aufbau

```
Deckschicht (Facing):  GFK-Laminat, ~1.5–3 mm
Kern:                   Schaumstoff oder Balsa
Rückenschicht (Facing): GFK-Laminat, ~1.5–3 mm

Gesamtdicke: 20–60 mm (abhängig Anwendung)
```

**Kern-Materialien:**

| Material | Dichte | Scherfestigkeit | Kosten | Haltbarkeit |
|----------|--------|-----------------|--------|------------|
| Polyurethane Schaum | 40–60 kg/m³ | 0.3–0.6 MPa | Niedrig | Gut |
| Polystyrene Schaum (Styrodur) | 30–50 kg/m³ | 0.2–0.4 MPa | Niedrig | Moderat |
| Balsa (select) | 100–150 kg/m³ | 2–5 MPa | Hoch | Ausgezeichnet |
| PVC-Schaumstoff (Divinycell) | 50–100 kg/m³ | 0.5–1.5 MPa | Mittel | Ausgezeichnet |

### 3.2 Sandwich-Vorteile und Grenzen

**Vorteile:**
- Hohe Steifigkeit bei niedrigem Gewicht
- Thermische Isolierung
- Schallabsorption
- Gute Dampfsperre (wenn richtig hergestellt)

**Grenzen:**
- Delamination-Risiko (Schichten trennen sich)
- Feuchte-Eindringlichkeit (kritisch für offene Zellenschäume)
- Kern-Scherversagen unter hoher Kraft
- Komplexe Reparatur

---

## 4. Faserverbund-Laminate (FRP)

### 4.1 Fasermaterial und Harz

**Typische Fasertypen:**

| Faser | E-Modul | Dichte | Kosten | Anwendung |
|-------|---------|--------|--------|-----------|
| Glassfiber (E-Glas) | 72 GPa | 2.58 g/cm³ | Niedrig | Standard |
| Carbon (HS) | 230 GPa | 1.60 g/cm³ | Hoch | Hochleistung |
| Aramid (Kevlar) | 130 GPa | 1.45 g/cm³ | Sehr hoch | Impact-Schutz |

**Harzsysteme:**

| Harz | Verwendung | Eigenschaften |
|------|-----------|-------------|
| Polyester (ungesättigt) | Standard Boote | Kostengünstig, lange Arbeitsdauer, Schrumpf ~8% |
| Epoxy | Premium, Marine | Höhere Festigkeit, niedrigeres Schrumpf ~2%, teurer |
| Vinylester | Marine-aggressive Umgebung | Besser als Polyester gegen Hydrolyse, Zwischenkosten |

### 4.2 Faserausrichtung und Laminataufbau

**Klassischer Aufbau für Rumpf (ausgehend von Mold):**

```
1. Gelcoat: 0.5–1.0 mm (Oberflächenschutz, Ästhetik)
2. Strukturlaminat:
   − Chopped Strand Mat (CSM): ±0° Fasern, Scherfestigkeit
   − Biaxial Woven Roving: 0°/90° Fasern, Festigkeit in beide Richtungen
   − Unidirektional (UD): überwiegend 0° (Längsrichtung), Biegefestigkeit
3. Kern (Sandwich): Schaumstoff oder Balsa
4. Strukturlaminat (analog)
5. Innenlaminat: CSM + 0°/90° für Innenseite Rumpf

Typisches Gewicht: 50–80 kg/m² für 10–15m Rumpf
```

### 4.3 Laminatdicke — Empfehlungen

**Rumpf (Unter Wasserlinie):**
```
Dicke_mm ≈ 4 + 0.1 × LWL_m + 0.03 × Depth_m
Beispiel: 12m LWL, 2m Tiefgang → ~6.8 mm
Range: 5–12 mm typisch
```

**Deck:**
```
Dicke_mm ≈ 3 + 0.08 × LWL_m
Beispiel: 12m → ~4.0 mm
Range: 3–8 mm
```

**Kajüte-Seiten:**
```
Dicke_mm ≈ 2 + 0.05 × LWL_m
Beispiel: 12m → ~2.6 mm
Range: 2–5 mm
```

---

## 5. Lokale Verstärkung — Stringers und Frames

### 5.1 Stringers (Längsversteifung)

Auf Innenseite des Rumpfes angebracht, laufen entlang Schiffslängsrichtung.

**Zweck:**
- Reduzieren Panel-Durchbiegung zwischen Spanten
- Erhöhen Biege-Steifigkeit ohne Massezunahme
- Verhindern Beulknicken (buckling) unter Druck

**Typische Abmessungen (12–16m Segler):**

```
Abstand entlang Rumpf (Spacing):  150–300 mm
Profile-Höhe (h):                 30–60 mm
Profile-Breite (b):               20–40 mm
Materialstärke (t):               3–5 mm
```

**Profile-Typen:**
- **T-Stringer:** Umgekehrtes T, Flansch nach unten
- **L-Stringer:** Winkel-Profil, einfacher zu produzieren
- **Box-Stringer:** Geschlossenes Profil, höchste Steifigkeit

### 5.2 Frames (Querverstärkung)

Spanten-ähnliche Strukturen, aber innere Verstärkung (nicht Außenmold).

**Spacing und Typ:**
```
Abstand (Spantabstand):  600–1200 mm (abhängig LWL)
Profil:                  Flachstab oder Kanal-Profil
Material:                FRP oder lokal Holz
```

---

## 6. Fehleranalyse — 12 Fehlermuster

### 6.1 [F6.1] Zu dünne Rumpf-Laminatdicke (unter ISO 12215 Minimum)

**Symptom:**
- Berechnet Laminatdicke: 4.5 mm
- ISO 12215 empfohlen: 6.5–7.5 mm
- Verwendet: 5.0 mm

**Ursache:**
- Kostenreduktion (dünnere = weniger Material)
- Gewichtsoptimierung übertrieben
- Zu großes Vertrauen in Modellberechnung

**Folgen:**
- Rumpf-Durchbiegung unter Wellenlast
- Delamination-Risiko (Schichten trennen sich unter Biegung)
- Langfristig: Osmotische Bläschen (Feuchte-Eindringung)
- Sicherheit: Bruch unter extremer See

**Empfohlene Korrektion:**
```
Minimum-Dicke ISO 12215 befolgen oder übersteigen
Für Segler und motorisierte Cruiser:
  Rumpf-Dicke ≥ 5 + 0.15 × LWL_m
  Deck ≥ 4 + 0.10 × LWL_m
Sicherheitsfaktor ≥ 1.15 auf berechnete Dicke anwenden
```

**Prüfkriterium:** Laminatdicke < ISO-Minimum → FEHLER

---

### 6.2 [F6.2] Sandwich-Delamination (unzureichende Kernanbindung)

**Symptom:**
- Visuell: Beulen oder weiße Flecken auf Rumpf
- Klopftest: Hohlklingende Stellen
- Querschnitt-Quetsch-Test: Schichten können sich verschieben

**Ursache:**
- Kern nicht ausreichend gebondet (schlechte Haftung Laminat-Kern)
- Feuchte während Herstellung (Dampf in Kern eingelagert)
- Thermische Zyklisierung (Ausdehnungsunterschiede)

**Folgen:**
- Lokale Steifigkeitsverlust (Panel durchbeugt leicht)
- Progrediente Delaminierung unter Belastung
- Struktur-Versagen möglich (Sandwich verliert Kern-Stütze)
- Wasserindringlichkeit (Risse propagieren)

**Empfohlene Korrektion:**
```
Herstellungs-Verfahren überprüfen:
  − Kern-Vorbehandlung: Oberfläche rau für bessere Haftung
  − Druck während Aushärtung: Minimum 0.2 bar Vakuum + Druck
  − Temperatur-Profil: Keramik-Kerne können Feuchtigkeit speichern
  − Nachbehandlung: Kurze Bake-out bei 60–80°C

Reparatur: Delaminierte Stelle muss neu laminiert werden (aufwendig)
```

**Prüfkriterium:** Delaminierung > 10 cm² → Reparatur erforderlich

---

### 6.3 [F6.3] Ungenügende Kern-Scherfestigkeit (zu weicher Kern)

**Symptom:**
- Unter Druck-Last schertsich Kern
- Sandwich biegt durch wie ohne Kern
- Klopftest zeigt weiche Antwort

**Ursache:**
- Kern-Material zu niedrig-Dichte (z.B. 30 kg/m³ PU-Schaum statt 50)
- Falsche Kern-Dicke dimensioniert
- Kern nicht passend für Lastfall

**Folgen:**
- Biegung-Versagen (Sandwich funktioniert nicht als Balken)
- Höhere Spannungen in Facing-Schichten
- Struktur-Unsicherheit

**Empfohlene Korrektion:**
```
Kern-Material überprüfen:
  − Für Boot-Rumpf: Minimum 50 kg/m³ PU oder Balsa
  − Scherfestigkeit: ≥ 0.5 MPa bei Rumpf-Anwendung
  − Dicke: mindestens 25 mm (oft 30–50 mm)

Ladeberechnung: Kern-Scherfestigkeit muss unter allen Lastfällen
  τ_shear < τ_allowable × Safety_Factor (SF ≥ 2.0)
```

**Prüfkriterium:** Kern-Scherfestigkeit < 0.3 MPa → Korrektionerforderlich

---

### 6.4 [F6.4] Fehlerhafte Faserausrichtung (CSM vs. Woven falsch)

**Symptom:**
- Rumpf zeigt hohe Längsbiegesteifigkeit, aber schlechte Scherfestigkeit
- Woven dominiert (zu viel 0°/90°), wenig unidirektionale Faser
- CSM (±0°) unter-bemessen

**Ursache:**
- Designer vertraute unidirektionale Faser allein
- Herstellung sparte CSM (Kosten) ein
- Keine strukturelle Analyse durchgeführt

**Folgen:**
- Scherfestigkeit niedrig (CSM kritisch dafür)
- Torsion-Steifigkeit inadäquat (Richtungs-Mix erforderlich)
- Längsbiegung OK, aber Querbiegung schwach
- Slamming-Impact kann Schäden verursachen

**Empfohlene Korrektion:**
```
Balanced Laminate Aufbau:
  CSM (±0°):            20–30% Volumen
  Woven (0°/90°):       40–50% Volumen
  Unidirektional (0°):  20–30% Volumen

Typ-Beispiel für 6mm Rumpf-Laminat:
  Gelcoat 1mm
  CSM 0.8mm
  Woven 1.2mm
  UD 1.2mm
  [Kern 30mm optional]
  UD 1.2mm
  Woven 1.2mm
  CSM 0.8mm
```

**Prüfkriterium:** CSM < 15% oder UD > 50% → Überprüfung

---

### 6.5 [F6.5] Unzureichende Spanter-Abstützung (Frames zu weit auseinander)

**Symptom:**
- Rumpf zwischen Spanten durchhängend
- Messung: Durchtritt > 5 mm unter Eigenlast
- Visuelle Inspektion: Eindellung

**Ursache:**
- Spanter-Abstand zu groß dimensioniert (Kostenersparnis)
- Keine Durchbiegungs-Analyse durchgeführt
- Stringers ignoriert oder zu schwach

**Folgen:**
- Panel-Durchbiegung unter hydrostatischer Last
- Ermüdungsfestigkeit reduziert (Biegespannungs-Zyklus höher)
- Visuelle Unebenheiten (Qualitätsproblem)
- Mittelfristig: Delamination durch lokale Spannungs-Konzentration

**Empfohlene Korrektion:**
```
Spantabstand überprüfen und ggf. reduzieren:
  Ziel:       Frame Spacing ≤ 800–1000 mm (größere Boote bis 1200 mm)
  Oder:       Stringer-Abstand reduzieren (150–250 mm)

Durchbiegungs-Limit: ≤ 2 mm unter selbst-Gewicht
                     ≤ 4 mm unter Wellenlast (kombiniert mit Eigenlast)
```

**Prüfkriterium:** Panel Deflection > 4mm unter vollständiger Last → Korrektur

---

### 6.6 [F6.6] Hard-Spot Spannungs-Konzentration (scharfe Ecken)

**Symptom:**
- Lokale Beschädigungen oder Beulen in Eckenbereich
- Übergangszone Deck/Kajüte: Risse
- Stringers/Frames mit scharfer Ecke gegen Rumpf

**Ursache:**
- CAD-Design mit scharfen Ecken statt Radius
- Herstellung: Ecke zu spitz ausgeführt
- Keine Fillets (Abrundungen) zum Spannungsabbau

**Folgen:**
- Spannungs-Konzentrationsfaktor (Kt) bis 3–5×
- Ermüdungs-Einkerbung (Fatigue Notch): kritischer als Zug-Bruch
- Risse propagieren (Risswachstum unter Zyklisierung)

**Empforlicht Korrektion:**
```
Fillet-Radien einführen:
  r ≥ 5 mm für kleine Übergänge
  r ≥ 10 mm für größere Ecken (Deck/Kajüte)
  r ≥ Laminat-Dicke (typisch 6–10 mm)

CAD/Herstellung: R-Übergänge überprüfen und iterativ optimieren
Ziel: Spannungs-Konzentrationsfaktor Kt < 2.0
```

**Prüfkriterium:** Scharfe Ecke ohne Radius → Überprüfung

---

### 6.7 [F6.7] Wasserdruck-Eindellung bei zu niedrigem Modul (schwaches Laminat)

**Symptom:**
- Unter Wasserdruck (Tauchgang oder tiefes Wasser): Rumpf "dehnt sich"
- Tiefgang-Unterschiede an verschiedenen Stellen
- Struktur fühlt sich "schwammig" an

**Ursache:**
- Elastizitäts-Modul des Laminats zu niedrig (zu viel Harz, zu wenig Faser)
- Faservolumen-Anteil < 25% (sollte >35%)
- Alte oder degradierte Harze

**Folgen:**
- Formveränderung unter hydrostatischer Last
- Erhöhte Spannungen beim Tauchen
- Struktur kann zu große Verformung erleiden
- Nachhaltige Verformung möglich (kriechend)

**Empforlicht Korrektion:**
```
Faservolumen-Anteil erhöhen:
  Ziel: ≥ 35% Faservolumen (≥ 40% Premium)
  Erreichbar durch: richtige Faser-Menge, Verdichtung, Druck

Elastizitäts-Modul prüfen:
  E_composite ≥ 3–4 GPa für Standard-Polyester-Laminat
  E ≥ 5–6 GPa für Epoxy-Premium

Test-Verfahren: ASTM D3410 oder ISO 527 (Zugtest)
```

**Prüfkriterium:** E_Modul < 3 GPa oder Deflection > 0.5% unter Druck → Korrektur

---

### 6.8 [F6.8] Ungenügende Ballast-Befestigung (Strukturelle Lasten)

**Symptom:**
- Ballast-Kammer hat keine oder schwache Verstärkerungen
- Unter Beschleunigung (Seegang) Ballast "wandert" oder knackt Struktur
- Sichtbar: Risse um Ballast-Behältnis

**Ursache:**
- Ballast-Laden erst später durchgeführt (zu spät für Struktur-Design)
- Ballast-Gewicht größer als erwartet
- Keine Dynamik-Analyse für Seegang-Beschleunigung

**Folgen:**
- Strukturelles Versagen (Rumpf-Bruch unter Ballast-Schlag)
- Ballast kann ausfallen (Sicherheit-Risiko)
- Reparaturen notwendig

**Empforlicht Korrektion:**
```
Ballast-Struktur neugestalten:
  − Ballast-Behälter sollte integral zu Rumpf sein (nicht extern)
  − Verstärkung um Ballast: min. 1.5× Rumpf-Dicke
  − Ballast-Lagerung sollte durch Stringers/Frames verteilt
  − Dynamische Last = Ballast_Masse × (a_vertical / g) (typisch 1.2–1.5× g in Seegang)

Berechnung: Struktur dimensioniert für min. 1.5× statisches Ballast-Gewicht
```

> ⚠️ **ZU PRÜFEN (Audit):** Die oben genannten Auslegungswerte — Dynamiklast „1,2–1,5× g" und Dimensionierung auf „min. 1,5× statisches Ballast-Gewicht" — sind für eine sicherheitskritische Kiel-/Ballastverbindung potenziell unzureichend und ersetzen KEINE Berechnung nach **ISO 12215-9** (Small craft — Hull construction and scantlings — Part 9: Sailing craft appendages). Maßgebend ist nach ISO 12215-9 nicht ein einzelner Vertikal-Faktor, sondern mehrere Lastfälle — insbesondere der **90°-Kränungsfall** (Kiel horizontal: Kielgewicht × g wirkt seitlich am Kiel-Schwerpunkt und erzeugt das i.d.R. größte Quer-Biegemoment an der Kiel-Rumpf-Anbindung), der **Grundberührungs-/Aufsetz-Lastfall** (vertikale Stoßkraft am Kielboden durch den Kiel-Schwerpunkt) sowie der aufrechte Segelfall mit **+40 % Dynamik-Zuschlag**. Zusätzlich fordert ISO 12215-9 einen **Sicherheitsfaktor von 2:1** auf das Biegemoment (Kat. A/B); traditionelle Praxis empfiehlt bis zu **5:1** für Kielbolzen und Bodenwrangen. Werte NICHT ohne Nachweis nach ISO 12215-9 anpassen — Zahlen hier bewusst unverändert belassen.

**Prüfkriterium:** Ballast-Befestigung ohne lokale Verstärkerung → Fehler

---

### 6.9 [F6.9] Feuchte-Eindringlichkeit (Osmotische Bläschen-Vorlauf)

**Symptom:**
- Rumpf-Oberfläche unter Wasserlinie: weiße Kristalle oder Flöckchen
- Auf Druck: Gelcoat platzt auf
- Geruch: Essig-ähnlich (Säure-Hydrolyse)

**Ursache:**
- Unzureichende Gelcoat-Dicke (<0.5 mm)
- Gelcoat-Qualität schlecht (zu porös)
- Lagerung vor Einsatz: Feuchte eindrang
- Wasser diffundiert durch Laminat (wenn nicht versiegelt)

**Folgen:**
- Hydrolyse des Harzes (Laminat wird brüchig)
- Delamination zwischen Gelcoat und Laminat
- Kosmetischer und struktureller Schaden
- Reparatur aufwendig (Schleifen, Neulaminieren)

**Empforlicht Korrektion:**
```
Prävention (Design/Herstellung):
  − Gelcoat-Dicke ≥ 0.8 mm (typisch 1.0 mm)
  − Laminat dichtsperren (Epoxy-Finish oder UV-Lackierung nach 12 h)
  − Cure-Zeit vollständig (nicht zu schnell ins Wasser)
  
Nach Lagerstelle vor Einsatz:
  − Inspekt auf erste Bläschen
  − Lagerung trocken und belüftet

Reparatur:
  − Schleifen bis gesundes Laminat
  − Neulaminieren mit Epoxy-Harz
  − Oberflächenfinish erneuern
```

**Prüfkriterium:** Osmotische Bläschen sichtbar → Reparatur notwendig

---

### 6.10 [F6.10] Unausreichend verstärkte Mastschuh-Durchdringung

**Symptom:**
- Mastdruck: Belastung konzentriert auf kleine Fläche
- Rumpf um Mastschuh: Eindellung sichtbar
- Strukturelle Risse um Durchgang

**Ursache:**
- Mastschuh-Bund zu klein oder zu dünn
- Keine ringförmige Verstärkerung (Doublers) vorhanden
- Mastdruck falsch berechnet

**Folgen:**
- Lokales Laminat-Versagen unter Mast-Lateralkraft
- Mastschuh kann sich verschieben (Sicherheit)
- Wasser-Eindringlichkeit (Lecks um Mastschuh)

**Empforlicht Korrektion:**
```
Verstärkung dimensionieren:
  Mastschuh-Durchmesser: d_inch = d_mast_mm / 25.4 + 50 mm
  Verstärkungsring (Doubler): Breite ≥ 150–200 mm
  Verstärkings-Dicke: 2–3× Rumpf-Laminat-Dicke

Lastverteilung: Mastdruck sollte über >300 mm² verteilt werden
                Druckspannung < Laminat-Druckfestigkeit / Safety_Factor
```

**Prüfkriterium:** Mastschuh ohne lokale Verstärkerung → Fehler

---

### 6.11 [F6.11] Mangelhaft integriert Durchdringungen (Pumpenschächte, Kabel-Gänge)

**Symptom:**
- Viele Durchdringungen (Pumpenschacht, Elektro-Kanäle, Wasser-Durchgang)
- Rumpf um Durchdringungen: Schwach oder lokal verschwächt
- Wasser-Leckage oder Feuchte-Eindring an Schnittsteilen

**Ursache:**
- Nachträgliche Durchdringungen gebohrt (Struktur aufgetrennend)
- Keine lokalen Verstärkungen hinzugefügt
- Abdeckungen nicht wasserdicht

**Folgen:**
- Schwächung der lokalen Struktur
- Wasser-Eindring möglich (Feuchteschaden)
- Risse können propagieren

**Empforlicht Korrektion:**
```
Vor Bau: Alle Durchdringungen in Design planen
  − Durchdringungen sollten integriert werden (während Laminierung)
  − Lokale Verstärkerungen um jeden Durchgang
  
Nachträglich: Wenn Durchgang notwendig,
  − Scheiben oder Doubler rings mit min. 5mm Dicke auf Innenseite
  − Abdichtung mit Sealant (Silikon oder Polysulfid)
  − Kabel-Durchführungen mit Nylon-Dichtring
```

**Prüfkriterium:** Durchdringungen ohne Verstärkerung → Überprüfung/Korrektur

---

### 6.12 [F6.12] Fehlerhafte Scherschicht-Berechnung in Sandwich (Kern versagt vor Facing)

**Symptom:**
- Unter Last: Kern bricht, aber Facing ist noch intakt
- Querschnitt-Quetsch-Test: Kern schert ohne Facing-Versagen
- Scherfestigkeit-Analyse zeigt Kern-Versagen früher als Facing

**Ursache:**
- Kern-Material zu schwach für Last-Niveau
- Dicke-Verhältnis Facing/Kern falsch (Facing zu dick, Kern zu dünn)
- Keine Kern-Scherfestigkeit Berechnung

**Folgen:**
- Kern-Versagen führt zum Sandwich-Funktionsverlust
- Facing biegt durch wie ohne Kern
- Struktur nicht effizient

**Empforlicht Korrektion:**
```
Kern-Scherfestigkeit überprüfen:
  τ_core_applied < τ_core_allowable / SF  (SF ≥ 2.0)
  
Dicke-Optimierung:
  h_core = t_facing × √(E_facing / τ_core / 2)  (ungefähre Regel)
  
Typisch für 6mm-Facing (FRP):
  Kern-Dicke sollte ≥ 25 mm sein, Kern-Scherfestigkeit ≥ 0.5 MPa
```

**Prüfkriterium:** Kern-Spannungs-Faktor > 1.0 (ohne Sicherheit) → Fehler

---

## 7. Finite Element Analysis (FEA) für Boote

### 7.1 Modellierungs-Ansätze

**Vereinfacht (Plate/Shell):**
- Rumpf als 2D-Fläche
- Dicke in Material-Definition
- Schnell zu rechnen, ausreichend für Grundlayout

**Detailliert (Solid + Shell):**
- Stringers, Frames als Balken
- Rumpf als Shell
- Durchdringungen und lokale Verstärkungen explizit
- Genauer, aber 10–20× längere Rechenzeit

### 7.2 Lasten für FEA

**Statisch:**
- Hydrostatischer Druck (Wasserlinie-abhängig)
- Eigenlast (Rumpf, Deck, Maschine)
- Ballast-Last (Trägheits-Komponente für beschleunigte Wasserlinie)

**Dynamisch:**
- Slamming-Impact (Druckpuls über Millisekunden)
- Wellenbiegung (Sagging/Hogging)
- Torsion (Manöver, Wind)

---

## 8. Prüfverfahren für Strukturen

### 8.1 Zug-Test (ASTM D3039 / ISO 527)

Material-Proben aus Laminat gezogen, bis Bruch.
- Zugfestigkeit: 200–350 MPa typisch
- Elastizitäts-Modul: 8–12 GPa typisch
- Bruchdehnung: 1.5–3% typisch

### 8.2 Druck-Test (ASTM D3410)

Ähnlich wie Zug, aber Druck (kniffliger zu testen).
- Druckfestigkeit: 120–180 MPa typisch
- Oft Versagen durch Beulknicken (nicht Zug-Bruch)

### 8.3 Schub-Test (ASTM D4255)

Probe ausgesetzt für Torsion bis Versagen.
- Scherfestigkeit: 40–80 MPa typisch (FRP)
- Schub-Modul: 3–5 GPa typisch

---

## 9. ANHANG — Pydantic v2 Model

```python
from pydantic import BaseModel, Field, validator
from typing import Optional, List
from enum import Enum
from datetime import datetime

class MaterlialTypeEnum(str, Enum):
    POLYESTER_FIBERGLASS = "polyester_fiberglass"
    EPOXY_FIBERGLASS = "epoxy_fiberglass"
    CARBON_EPOXY = "carbon_epoxy"
    MARINE_PLYWOOD = "marine_plywood"
    STEEL = "steel"
    ALUMINIUM = "aluminium"

class CoreMaterialEnum(str, Enum):
    POLYURETHANE_FOAM = "pu_foam"
    STYROFOAM = "styrofoam"
    BALSA = "balsa"
    PVC_FOAM = "pvc_foam"

class LaminateConfiguration(BaseModel):
    """Laminat-Aufbau und Eigenschaften"""
    model_config = {"from_attributes": True}
    
    name: str = Field(..., description="Layer identifier (e.g., 'Hull_Facing')")
    material: MaterlialTypeEnum = Field(..., description="Base material")
    thickness_mm: float = Field(..., gt=0, description="Layer thickness (mm)")
    
    fiber_volume_fraction: Optional[float] = Field(None, ge=0.0, le=1.0, description="Fiber volume fraction (0-1)")
    elastic_modulus_gpa: Optional[float] = Field(None, gt=0, description="E-modulus (GPa)")
    tensile_strength_mpa: Optional[float] = Field(None, gt=0, description="Tensile strength (MPa)")
    shear_strength_mpa: Optional[float] = Field(None, gt=0, description="Shear strength (MPa)")
    
    orientation: str = Field("0/90", description="Fiber orientation (e.g., '0/90', '±45', 'CSM')")
    description: Optional[str] = Field(None, description="Additional notes")

class SandwichStructure(BaseModel):
    """Sandwich-Aufbau (Facing + Kern + Facing)"""
    model_config = {"from_attributes": True}
    
    facing_outer: LaminateConfiguration = Field(..., description="Outer facing laminate")
    core_material: CoreMaterialEnum = Field(..., description="Core type")
    core_density_kg_m3: float = Field(..., gt=0, description="Core density (kg/m³)")
    core_thickness_mm: float = Field(..., gt=0, description="Core thickness (mm)")
    core_shear_strength_mpa: float = Field(..., gt=0, description="Core shear strength (MPa)")
    facing_inner: LaminateConfiguration = Field(..., description="Inner facing laminate")
    
    total_thickness_mm: Optional[float] = Field(None, description="Sandwich total thickness (mm)")

class StructuralElement(BaseModel):
    """Einzelnes Struktur-Element (z.B. Rumpf-Panel, Stringer)"""
    model_config = {"from_attributes": True}
    
    element_id: str = Field(..., description="Element identifier")
    element_type: str = Field(..., description="Type (e.g., 'Hull_Panel', 'Stringer', 'Frame')")
    
    # Laminat oder Sandwich
    construction: str = Field(..., description="'laminate' or 'sandwich'")
    laminate: Optional[List[LaminateConfiguration]] = Field(None, description="Layup schedule")
    sandwich: Optional[SandwichStructure] = Field(None, description="Sandwich configuration")
    
    # Dimensionen
    length_mm: Optional[float] = Field(None, description="Element length (mm)")
    width_mm: Optional[float] = Field(None, description="Element width (mm)")
    height_or_radius_mm: Optional[float] = Field(None, description="Height or radius (mm)")
    
    # Belastung & Analyse
    max_bending_stress_mpa: Optional[float] = Field(None, description="Max bending stress (MPa)")
    max_shear_stress_mpa: Optional[float] = Field(None, description="Max shear stress (MPa)")
    deflection_mm: Optional[float] = Field(None, description="Measured/calculated deflection (mm)")
    
    # Sicherheit
    safety_factor: Optional[float] = Field(None, ge=1.0, description="Safety factor applied")
    failure_mode: Optional[str] = Field(None, description="Expected failure mode")

class StructuralAnalysisReport(BaseModel):
    """Struktur-Analyse-Report"""
    model_config = {"from_attributes": True}
    
    ship_name: str = Field(..., description="Yacht name")
    analysis_date: datetime = Field(default_factory=datetime.now, description="Analysis date")
    
    # Eingaben
    loa_mm: float = Field(..., description="Length overall (mm)")
    lwl_mm: float = Field(..., description="Length waterline (mm)")
    bwl_mm: float = Field(..., description="Beam waterline (mm)")
    draft_mm: float = Field(..., description="Draft (mm)")
    
    # Analyse
    elements: List[StructuralElement] = Field(default_factory=list, description="Structural elements analyzed")
    
    # Ergebnisse
    critical_stress_mpa: Optional[float] = Field(None, description="Maximum stress found (MPa)")
    critical_element_id: Optional[str] = Field(None, description="Element with max stress")
    max_deflection_mm: Optional[float] = Field(None, description="Maximum deflection (mm)")
    
    iso_12215_compliant: bool = Field(..., description="Meets ISO 12215 requirements")
    comments: List[str] = Field(default_factory=list, description="Analysis notes")
    recommendations: List[str] = Field(default_factory=list, description="Design recommendations")
    
    confidence_level: float = Field(0.85, ge=0.0, le=1.0, description="Analysis confidence")

def assess_laminat_thickness(
    lwl_mm: float, depth_mm: float, hull_area_code: str
) -> dict:
    """ISO 12215 Laminatdicke Empfehlung"""
    lwl_m = lwl_mm / 1000
    depth_m = depth_mm / 1000
    
    if hull_area_code == "hull_bottom":
        thickness_min = 4 + 0.1 * lwl_m + 0.03 * depth_m
    elif hull_area_code == "hull_side":
        thickness_min = 3 + 0.08 * lwl_m
    elif hull_area_code == "deck":
        thickness_min = 3 + 0.08 * lwl_m
    elif hull_area_code == "cabin_side":
        thickness_min = 2 + 0.05 * lwl_m
    else:
        thickness_min = 3
    
    return {
        "recommended_thickness_mm": round(thickness_min, 1),
        "safety_factor_applied": 1.15,
        "minimum_absolute_mm": round(thickness_min * 1.15, 1)
    }

def check_deflection_limit(
    deflection_mm: float, length_mm: float, load_type: str
) -> dict:
    """Durchbiegungs-Limit überprüfen"""
    limit_selfweight = length_mm / 200  # L/200
    limit_wave_load = length_mm / 100   # L/100
    
    if load_type == "self_weight":
        acceptable = deflection_mm <= limit_selfweight
        limit = limit_selfweight
    elif load_type == "wave_load":
        acceptable = deflection_mm <= limit_wave_load
        limit = limit_wave_load
    else:
        acceptable = deflection_mm <= limit_selfweight
        limit = limit_selfweight
    
    return {
        "deflection_mm": deflection_mm,
        "limit_mm": limit,
        "acceptable": acceptable,
        "margin_percent": ((limit - deflection_mm) / limit * 100) if limit > 0 else 0
    }
```

---

**Datei abgeschlossen.**  
Kat 31.03 Strukturberechnung — Version 1.0 — 2025-01
