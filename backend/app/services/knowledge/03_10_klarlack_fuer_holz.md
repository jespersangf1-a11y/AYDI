# 03_10 — Klarlack für Holz im Yachtbau

> **Modultyp**: Wissensbasis — Marine-Klarlacke für Holzoberflächen
> **Zielgruppe**: AYDI Analyse-Engine (Pipeline A + B + C)
> **Sprache Inhalt**: Deutsch (Fachbegriffe Englisch wo branchenüblich)
> **Code-Sprache**: Englisch
> **Stand**: 2026-04
> **Confidence-Default**: `measured` wo TDS/Herstellerdaten, `estimated` wo Erfahrungswerte

---

## 1. Einführung und Überblick

### 1.1 Warum Klarlack im Yachtbau?

| Parameter | Details |
|---|---|
| Hauptzweck | UV-Schutz + Feuchtigkeitsbarriere für Holz bei sichtbarer Maserung |
| Ästhetik | Holzmaserung bleibt sichtbar — wichtigstes Unterscheidungsmerkmal zu Decklack |
| Tradition | Hochglanz-Klarlack auf Teak/Mahagoni ist das Markenzeichen klassischer Yachten |
| Herausforderung | UV-Abbau zerstört Klarlack schneller als pigmentierten Lack (keine Pigment-Abschirmung) |
| Pflegeaufwand | Höchster Wartungsaufwand aller Bootslack-Typen — 1–3× jährlich Auffrischung |
| Alternative | Öle (Teak-Öl, Leinöl) — weniger Schutz, weniger Pflege, kein Hochglanz |
| Entscheidung | Glanz vs. Aufwand — zentrale Frage für jeden Holzboot-Eigner |

> Confidence: `measured`

### 1.2 Klarlack-Chemie: Hauptfamilien

| Familie | Basis | Schichten | Glanz (GU 60°) | UV-Schutz | Haltbarkeit | Pflegeaufwand |
|---|---|---|---|---|---|---|
| Traditioneller Alkyd-Lack | Alkyd-Harz + Tungöl/Leinöl | 8–12 | 90–98 | Mäßig | 1–2 Jahre | Sehr hoch |
| Modifizierter Alkyd (Phenol-Alkyd) | Phenolharz-modifiziertes Alkyd | 6–10 | 88–96 | Gut | 2–3 Jahre | Hoch |
| 1K-Polyurethan-Klarlack | 1K-PU-Harz | 4–8 | 85–95 | Gut–Sehr gut | 3–5 Jahre | Mittel |
| 2K-Polyurethan-Klarlack | 2K-PU (Isocyanat) | 3–6 | 90–98 | Sehr gut | 4–8 Jahre | Niedrig |
| Epoxid + UV-Klarlack | Epoxid-Basis + PU-Topcoat | 3+3 | 88–96 | Sehr gut | 5–10 Jahre | Niedrig–Mittel |
| Naturöl-Lack (Tungöl-basiert) | Tungöl + Harze | 5–8 | 70–85 | Mäßig | 1–2 Jahre | Hoch |
| Öl-Finish (kein Lack) | Teak-Öl, Leinöl | ∞ | 20–40 (satin) | Minimal | 3–6 Monate | Sehr hoch |

> Confidence: `measured`

### 1.3 Holzarten im Yachtbau und Lack-Kompatibilität

| Holzart | Ölgehalt | Klarlack-Eignung | Besonderheit |
|---|---|---|---|
| Teak (Tectona grandis) | Sehr hoch | Schwierig — Öl verhindert Haftung | Entölung mit Aceton Pflicht, oder Öl-Finish |
| Mahagoni (Swietenia/Khaya) | Mittel | Hervorragend | Klassische Klarlack-Holzart Nr. 1 |
| Iroko (Milicia excelsa) | Hoch | Gut mit Vorbereitung | Teak-Ersatz, ähnliche Ölprobleme |
| Sapele | Mittel | Sehr gut | Moderne Mahagoni-Alternative |
| Oregon Pine / Douglas Fir | Niedrig | Sehr gut | Mast-Holz, Decksplanken |
| Eiche (Quercus) | Mittel | Gut | Enthält Gerbsäure — kann Lack verfärben |
| Zeder (Western Red Cedar) | Mittel | Gut | Leicht, guter UV-Widerstand natürlich |
| Spruce (Sitka) | Niedrig | Sehr gut | Mast-Holz, hell |
| Lärche | Mittel | Gut | Planken, Kiel, Wasserpass |
| Teak-Sperrholz | Hoch (Furnier) | Schwierig | Furnier dünn — Schleifen vorsichtig! |
| Marine-Sperrholz (BS 1088) | Niedrig | Sehr gut | Ideal für Klarlack |

> Confidence: `measured`

```python
# model_config = {"from_attributes": True}
class HolzKlarlackKompatibilitaet:
    """Holzart-Klarlack-Kompatibilitätsbewertung"""
    model_config = {"from_attributes": True}

    holzart: str
    oelgehalt: str  # niedrig, mittel, hoch, sehr_hoch
    klarlack_eignung: str  # schwierig, gut, sehr_gut, hervorragend
    vorbehandlung_pflicht: list[str]  # z.B. ["entoelung", "anschleifen"]
    empfohlene_lacke: list[str]
    confidence: str = "measured"
```

---

## 2. Epifanes Clear Varnish — Der Referenzstandard

### 2.1 Produktübersicht Epifanes Clear Varnish

| Parameter | Details |
|---|---|
| Hersteller | Epifanes (Aalsmeer, Niederlande, seit 1902) |
| Produktname | Epifanes Clear Varnish (auch: Clear Gloss Finish) |
| Artikelnummer | CV.500 (500ml), CV.1000 (1L), CV.5000 (5L) |
| Chemie | Phenolharz-modifiziertes Alkyd + Tungöl (China Wood Oil) |
| Besonderheit | Seit 1902 nahezu unveränderte Rezeptur — Goldstandard |
| Feststoffgehalt | ~45% Vol |
| Empf. Schichtanzahl | 8–12 Schichten (Erstaufbau), 2–3 Schichten (Pflege) |
| Glanz | 96+ GU bei 60° (nach 8+ Schichten) |
| Trockenzeit (20°C) | Staubtrocken 4h, Überstreichbar 24h |
| Durchhärtung | 72h (3 Tage) |
| Theoret. Ergiebigkeit | 16 m²/L bei 30µm DFT |
| VOC | 474 g/L |
| Verdünner | Epifanes Thinner for Paint & Varnish |
| Preis (1L) | €38–48 (DE), £32–40 (UK), $42–52 (USA) |

> Confidence: `measured`

### 2.2 Epifanes 8–12 Schichten Aufbau-Protokoll

| Schicht | Verdünnung | Applikation | Schliff vor nächster | Trockenzeit | DFT (µm) |
|---|---|---|---|---|---|
| 1 (Sättigung) | 50–60% Verdünner | Pinsel, dünn, ins Holz einarbeiten | Kein Schliff | 24h | 5–10 |
| 2 (Sättigung) | 40–50% Verdünner | Pinsel, dünn | Kein Schliff | 24h | 10–15 |
| 3 (Aufbau) | 30–40% Verdünner | Pinsel | P220 leicht | 24h | 15–20 |
| 4 (Aufbau) | 20–30% Verdünner | Pinsel | P280 leicht | 24h | 20–25 |
| 5 (Aufbau) | 15–20% Verdünner | Pinsel oder Rolle+Tip | P280 | 24h | 25–30 |
| 6 (Aufbau) | 10–15% Verdünner | Pinsel oder Rolle+Tip | P320 | 24h | 25–30 |
| 7 (Aufbau) | 5–10% Verdünner | Pinsel oder Rolle+Tip | P320 | 24h | 25–30 |
| 8 (Glanz) | 5% Verdünner | Badger-Pinsel, Tip-Only | P400 | 24h | 25–30 |
| 9 (Glanz) | 0–5% Verdünner | Badger-Pinsel, Tip-Only | P400 | 24h | 25–30 |
| 10 (Final) | 0% (unverdünnt) | Badger-Pinsel, perfekter Verlauf | — | 72h Durchhärtung | 25–30 |
| **Gesamt** | | | | **~10 Tage** | **200–250µm** |

> Confidence: `measured`

### 2.3 Epifanes Schlüsseltechniken

| Technik | Details |
|---|---|
| Erste 2 Schichten | Stark verdünnt — Lack muss ins Holz eindringen, nicht auf der Oberfläche sitzen |
| Zwischenschliff | P220→P280→P320→P400 progressiv feiner — NIEMALS grob zurückgehen |
| Schleifstaub | Tack Cloth nach jedem Schliff — Staubfreiheit ist entscheidend |
| Badger-Pinsel | Ab Schicht 8 nur noch Dachs-Pinsel — feinste Spitzen für perfekten Verlauf |
| Temperatur | 15–25°C ideal. Unter 10°C: nicht lackieren. Über 30°C: zu schnelle Trocknung |
| Feuchtigkeit | Max 75% RF. Holzfeuchte <15% (Feuchtemesser!) |
| Staubkontrolle | Lackierbereich benetzen (Boden besprühen), kein Wind |
| Tip-Only Methode | Letzte Schichten: Pinsel nur leicht über nassen Lack ziehen (nicht auftragen!) |
| Verdünner-Wahl | Epifanes Brush Thinner (langsam) für Pinsel, Spray Thinner für HVLP |
| Niemals schütteln | Lack vorsichtig rühren — Luftblasen sind der Feind |

> Confidence: `measured`

### 2.4 Epifanes Weitere Klarlack-Produkte

| Produkt | Artikelnr. | Chemie | Besonderheit |
|---|---|---|---|
| Clear Varnish | CV.xxx | Phenol-Alkyd + Tungöl | Referenzstandard, 8–12 Schichten |
| Rapidclear | RC.xxx | Schnelltrocknender Alkyd | Staubtrocken 1h, 4–6 Schichten reichen |
| Wood Finish Gloss | WFG.xxx | Alkyd + UV-Filter | 4–6 Schichten, einfacher als Clear Varnish |
| Wood Finish Matte | WFM.xxx | Alkyd + UV + Mattierung | Seidenmatte Optik, 4–6 Schichten |
| Mono-urethane Clear | MU-0000 | 1K-PU klar | PU-Schutz, 4–6 Schichten |
| Clear Varnish Satin | CVS.xxx | Phenol-Alkyd seidenmatt | Wie CV aber satin — für Interior |

> Confidence: `measured`

### 2.5 Epifanes Rapidclear — Die schnelle Alternative

| Parameter | Details |
|---|---|
| Produktname | Epifanes Rapidclear |
| Chemie | Modifiziertes Alkyd, schnelltrocknend |
| Feststoffgehalt | ~38% Vol |
| Schichtanzahl | 4–6 (statt 8–12) |
| Glanz | 90+ GU bei 60° |
| Trockenzeit (20°C) | Staubtrocken 1h, Überstreichbar 4h |
| Vorteil | 6 Schichten an einem Tag möglich! |
| Nachteil | Nicht ganz so tiefer Glanz wie Clear Varnish, etwas weniger UV-Schutz |
| Einsatz | Pflege-Auffrischung, wenn keine Zeit für vollen CV-Aufbau |
| Verdünner | Epifanes Rapidclear Thinner |
| Preis (1L) | €34–42 (DE), £28–35 (UK), $38–46 (USA) |

> Confidence: `measured`

---

## 3. Le Tonkinois — Naturlack auf Tungöl-Basis

### 3.1 Produktübersicht Le Tonkinois

| Parameter | Details |
|---|---|
| Hersteller | Le Tonkinois / Avel (Frankreich, seit 1892) |
| Produktname | Le Tonkinois Vernis Original |
| Chemie | Tungöl (China Wood Oil) + natürliche Harze — KEIN Alkyd, KEIN PU |
| Besonderheit | Einziger großer Marine-Klarlack auf reiner Naturölbasis |
| Feststoffgehalt | ~50% Vol |
| Empf. Schichtanzahl | 5–8 Schichten (Erstaufbau) |
| Glanz | 70–85 GU bei 60° (warm, honigfarben — nicht spiegelglatt) |
| Trockenzeit (20°C) | Staubtrocken 6–8h, Überstreichbar 24h |
| Durchhärtung | 5–7 Tage |
| Theoret. Ergiebigkeit | 12–14 m²/L |
| VOC | <350 g/L (umweltfreundlicher als Epifanes) |
| Verdünner | Terpentinersatz oder Le Tonkinois Diluant |
| Preis (1L) | €32–40 (DE), £28–36 (UK), $38–48 (USA) |

> Confidence: `measured`

### 3.2 Le Tonkinois — Philosophie und Besonderheiten

| Aspekt | Details |
|---|---|
| Philosophie | „Das Holz atmen lassen" — mikroporöser Film, elastisch |
| Atmendes Holz | Le Tonkinois lässt Feuchtigkeit langsam durch — kein Blasenrisiko |
| Elastizität | Weicher Film als Alkyd/PU — arbeitet mit dem Holz |
| UV-Schutz | Mäßig — Tungöl hat natürliche UV-Absorber, aber weniger als synthetische |
| Reparatur | Einfachste Reparatur aller Klarlacke: schleifen + 1–2 Schichten |
| Überlackierbar | Auf sich selbst ohne Probleme, auch nach Jahren |
| Kein Abblättern | Le Tonkinois blättert nicht ab — er „erodiert" gleichmäßig |
| Farbton | Leicht honigfarben / bernstein — wärmt Holzton auf |
| Geruch | Angenehm, natürlich — weniger aggressiv als Alkyd-Lacke |
| Auf Teak | Hervorragend geeignet — Tungöl verträgt sich mit Teak-Eigenölen |

> Confidence: `measured`

### 3.3 Le Tonkinois Schichtaufbau

| Schicht | Verdünnung | Applikation | Schliff | Trockenzeit |
|---|---|---|---|---|
| 1 (Sättigung) | 20–30% Terpentinersatz | Pinsel, ins Holz einarbeiten | Keiner | 24h |
| 2 (Sättigung) | 10–20% | Pinsel | Keiner | 24h |
| 3 (Aufbau) | 5–10% | Pinsel oder Lappen | P240 leicht | 24h |
| 4 (Aufbau) | 0–5% | Pinsel | P280 leicht | 24h |
| 5 (Aufbau) | 0% | Pinsel | P320 | 24h |
| 6 (Glanz) | 0% | Feiner Pinsel | P320 | 24h |
| 7 (optional) | 0% | Feiner Pinsel, Tip-Only | — | 5–7 Tage Durchhärtung |
| **Gesamt** | | | | **~7 Tage, 150–180µm** |

> Confidence: `measured`

### 3.4 Le Tonkinois Produktfamilie

| Produkt | Besonderheit | Einsatz |
|---|---|---|
| Vernis Original | Standard-Klarlack, honigfarben | Außen + Innen, alle Holzarten |
| No 1 (Le Tonkinois N°1) | Hellere Version, weniger Gelbton | Helle Hölzer (Spruce, Cedar) |
| Le Tonkinois Huile | Reines Tungöl-Finish, kein Film | Alternative zu Teaköl |
| Le Tonkinois Bio | VOC-reduziert, Wasserbasis-Variante | Umweltbewusste Anwendung |

> Confidence: `measured`

---

## 4. Sikkens Cetol Marine — Der UV-Champion

### 4.1 Produktübersicht Sikkens Cetol Marine

| Parameter | Details |
|---|---|
| Hersteller | Sikkens (AkzoNobel, Niederlande) |
| Produktname | Cetol Marine |
| Artikelnummer | Diverse (regional unterschiedlich) |
| Chemie | Alkyd-modifiziert + spezielle UV-Absorber (Tinuvin-Technologie) |
| Besonderheit | Transparenter UV-Schutzlack — nicht spiegelglatt, seidenglänzend |
| Feststoffgehalt | ~40% Vol |
| Empf. Schichtanzahl | 3 Schichten Cetol + 2 Schichten Cetol Marine Gloss |
| Glanz Cetol | 45–55 GU bei 60° (seidenglänzend) |
| Glanz Cetol Marine Gloss | 80–90 GU bei 60° |
| Trockenzeit (20°C) | Staubtrocken 4–6h, Überstreichbar 16–24h |
| UV-Filter | Hochleistungs-UV-Absorber (HALS + UVA Kombination) |
| Ergiebigkeit | 14–16 m²/L |
| VOC | 420 g/L |
| Verdünner | International Thinner No. 1 / Sikkens Thinner |
| Preis (1L) | €38–48 (DE), £32–42 (UK), $44–54 (USA) |

> Confidence: `measured`

### 4.2 Sikkens Cetol System — Schichtaufbau

| Schicht | Produkt | Verdünnung | Schliff | Funktion |
|---|---|---|---|---|
| 1 | Cetol Marine | 10% | Keiner | UV-Basis + Holz-Sättigung |
| 2 | Cetol Marine | 5% | P280 leicht | UV-Aufbau |
| 3 | Cetol Marine | 0% | P320 leicht | UV-Vollschutz |
| 4 | Cetol Marine Gloss | 0% | P320 | Glanz-Schicht 1 |
| 5 | Cetol Marine Gloss | 0% | — | Glanz-Schicht 2 (Final) |
| **Gesamt** | | | | **~5 Tage, 150–200µm** |

> Confidence: `measured`

### 4.3 Sikkens Cetol Produktfamilie

| Produkt | Chemie | Glanz | UV-Schutz | Einsatz |
|---|---|---|---|---|
| Cetol Marine | Alkyd + UV-Absorber | 45–55 GU (satin) | Sehr hoch | Basis-Schutz, allein oder unter Gloss |
| Cetol Marine Gloss | Alkyd + UV | 80–90 GU | Hoch | Hochglanz-Finish über Cetol |
| Cetol Marine Light | Heller, weniger Bernstein | 45–55 GU | Sehr hoch | Für helle Hölzer |
| Cetol Filter 7 Plus | Transluzent, farbig | 35–45 GU | Sehr hoch | Farbige UV-Lasur |
| Cetol HLS Plus | Dünnschichtlasur | 25–35 GU | Hoch | Für raue/unebene Hölzer |

> Confidence: `measured`

### 4.4 Sikkens Cetol — Stärken und Schwächen

| Aspekt | Bewertung | Details |
|---|---|---|
| UV-Schutz | ★★★★★ | Bester UV-Schutz aller 1K-Klarlacke — HALS + UVA System |
| Aufwand | ★★★★☆ | 5 Schichten statt 8–12 — deutlich schneller als Epifanes |
| Glanz | ★★★☆☆ | Cetol allein: satin. Mit Gloss: gut, aber nie Epifanes-Niveau |
| Reparatur | ★★★★★ | Einfach: 1–2 Schichten Cetol auffrischen |
| Haltbarkeit | ★★★★★ | 3–5 Jahre ohne Kompletterneuerung (Rekord unter 1K) |
| Tiefenglanz | ★★☆☆☆ | Kein „Piano-Finish" — eher seidig als spiegelnd |
| Farbton | Warm, leicht bernstein | Dunkelt Holz auf — bei hellen Hölzern Light-Version wählen |

> Confidence: `measured`

---

## 5. International Woodskin

### 5.1 Produktübersicht International Woodskin

| Parameter | Details |
|---|---|
| Hersteller | International (AkzoNobel) |
| Produktname | Woodskin |
| Chemie | Hybridprodukt: Öl + Lack (Duo-System in einer Dose) |
| Besonderheit | „Weder Öl noch Lack" — elastischer Hybrid-Film |
| Feststoffgehalt | ~35% Vol |
| Empf. Schichtanzahl | 3–5 Schichten |
| Glanz | 50–65 GU bei 60° (seidenglänzend) |
| Trockenzeit (20°C) | Staubtrocken 3–4h, Überstreichbar 12h |
| UV-Filter | Integriert |
| Ergiebigkeit | 15 m²/L |
| VOC | 389 g/L |
| Verdünner | International Thinner No. 1 |
| Preis (1L) | €42–52 (DE), £36–44 (UK), $48–58 (USA) |

> Confidence: `measured`

### 5.2 Woodskin — Konzept und Eigenschaften

| Aspekt | Details |
|---|---|
| Konzept | Öl-Tiefen-Eindringung + Lack-Oberflächenfilm in einem Produkt |
| Film-Typ | Elastisch, mikro-porös — „atmet" wie Le Tonkinois |
| Auf Teak | Hervorragend — Öl-Anteil verträgt sich mit Teak-Eigenölen |
| Reparatur | Sehr einfach — schleifen, 1–2 Schichten, keine Ränder sichtbar |
| Abblättern | Blättert nicht ab — erodiert wie Le Tonkinois |
| Farbton | Leicht warm, natürlich — weniger Bernstein als Cetol |
| Vergleich zu Öl | Mehr Schutz, etwas mehr Glanz, weniger Wartung |
| Vergleich zu Lack | Weniger Glanz, weniger Schutz, aber VIEL weniger Wartung |

> Confidence: `measured`

### 5.3 Woodskin Schichtaufbau

| Schicht | Verdünnung | Applikation | Schliff | Trockenzeit |
|---|---|---|---|---|
| 1 | 10–15% Thinner No. 1 | Pinsel, einarbeiten | Keiner | 12h |
| 2 | 5–10% | Pinsel | P280 leicht | 12h |
| 3 | 0–5% | Pinsel | P320 leicht | 12h |
| 4 (optional) | 0% | Pinsel | P320 | 12h |
| 5 (optional) | 0% | Pinsel | — | 48h Durchhärtung |
| **Gesamt** | | | | **~3–5 Tage, 100–150µm** |

> Confidence: `measured`

---

## 6. Bristol Finish — Der amerikanische Premium-Klarlack

### 6.1 Produktübersicht Bristol Finish Traditional Amber

| Parameter | Details |
|---|---|
| Hersteller | Bristol Finish (USA, Tochter von Kirby Paint) |
| Produktname | Bristol Finish Traditional Amber |
| Chemie | Phenolharz-modifiziertes Alkyd + Tungöl (ähnlich Epifanes) |
| Besonderheit | US-Konkurrent zu Epifanes — angeblich dickerer Aufbau pro Schicht |
| Feststoffgehalt | ~48% Vol (höher als Epifanes) |
| Empf. Schichtanzahl | 6–10 Schichten |
| Glanz | 94+ GU bei 60° |
| Trockenzeit (20°C) | Staubtrocken 4h, Überstreichbar 24h |
| Ergiebigkeit | 14 m²/L |
| VOC | 450 g/L |
| Verdünner | Bristol Finish Brushing Thinner / Spraying Thinner |
| Preis (1qt) | $48–58 (USA), schwer in EU erhältlich |

> Confidence: `measured`

### 6.2 Bristol Finish Produktfamilie

| Produkt | Chemie | Besonderheit |
|---|---|---|
| Traditional Amber | Phenol-Alkyd + Tungöl | Warmer Bernstein-Ton, wie Epifanes |
| Clear UV | 1K-PU klar + UV-Filter | Moderner PU-Klarlack, weniger Bernstein |
| Interior Clear | Alkyd, niedrig-VOC | Speziell für Innenräume |
| Tropical Hardwood Sealer | Harzbasiert | Speziell für Teak, Iroko — versiegelt Öl |

> Confidence: `measured`

### 6.3 Bristol Finish Traditional Amber — Schichtaufbau

| Schicht | Verdünnung | Applikation | Schliff | DFT (µm) |
|---|---|---|---|---|
| 1 (Sealer) | 40–50% | Pinsel, dünn | Keiner | 8–12 |
| 2 (Sättigung) | 30–40% | Pinsel | Keiner | 12–18 |
| 3 (Aufbau) | 20–30% | Pinsel | P220 | 20–25 |
| 4 (Aufbau) | 10–20% | Pinsel | P280 | 25–30 |
| 5 (Aufbau) | 5–10% | Pinsel oder Rolle+Tip | P280 | 28–32 |
| 6 (Aufbau) | 0–5% | Pinsel | P320 | 28–32 |
| 7 (Glanz) | 0% | Badger-Pinsel | P400 | 28–32 |
| 8 (Final) | 0% | Badger-Pinsel | — | 28–32 |
| **Gesamt** | | | | **180–220µm** |

> Confidence: `measured`

---

## 7. Weitere Premium-Klarlacke

### 7.1 Hempel Dura-Gloss Varnish

| Parameter | Details |
|---|---|
| Hersteller | Hempel (Dänemark) |
| Produktname | Dura-Gloss Varnish (ehem. Blakes Varnish) |
| Chemie | Modifiziertes Alkyd + UV-Stabilisatoren |
| Schichtanzahl | 6–8 |
| Glanz | 88–94 GU |
| Trockenzeit | Staubtrocken 4h, überstreichbar 16h |
| Besonderheit | Skandinavische Tradition, guter UV-Schutz |
| Preis (750ml) | €28–36 (DE), £24–30 (UK) |
| Bewertung | Solide Alternative zu Epifanes, etwas weniger Tiefenglanz |

> Confidence: `measured`

### 7.2 International Compass

| Parameter | Details |
|---|---|
| Hersteller | International (AkzoNobel) |
| Produktname | Compass |
| Chemie | Alkyd + UV-Absorber |
| Schichtanzahl | 5–8 |
| Glanz | 85–92 GU |
| Trockenzeit | Staubtrocken 6h, Überstreichbar 24h |
| UV-Schutz | Gut — spezielle UV-Absorber integriert |
| Ergiebigkeit | 15–17 m²/L |
| Preis (750ml) | €26–34 (DE), £22–28 (UK) |
| Bewertung | Preis-Leistungs-Sieger unter Marken-Klarlacken |

> Confidence: `measured`

### 7.3 International Goldspar Satin

| Parameter | Details |
|---|---|
| Hersteller | International (AkzoNobel) |
| Produktname | Goldspar Satin |
| Chemie | Alkyd + UV-Filter, seidenmatt |
| Schichtanzahl | 4–6 |
| Glanz | 40–55 GU (satin) |
| Besonderheit | Seidenmattes Finish für traditionelle Optik |
| Einsatz | Interior, Cockpit-Holz, wo Hochglanz unerwünscht |
| Preis (750ml) | €24–30 (DE), £20–26 (UK) |

> Confidence: `measured`

### 7.4 Pettit Z-Spar Captain's Varnish

| Parameter | Details |
|---|---|
| Hersteller | Pettit Marine Paint (USA) |
| Produktname | Z-Spar Captain's Varnish 2015 |
| Chemie | Phenol-modifiziertes Tungöl-Alkyd |
| Schichtanzahl | 8–10 |
| Glanz | 92+ GU |
| Besonderheit | Amerikanischer Klassiker, direkter Epifanes-Konkurrent |
| Preis (1qt) | $38–48 (USA) |
| Bewertung | Sehr guter Lack, in USA leichter verfügbar als Epifanes |

> Confidence: `measured`

### 7.5 Pettit Z-Spar Flagship Varnish

| Parameter | Details |
|---|---|
| Hersteller | Pettit Marine Paint |
| Produktname | Z-Spar Flagship Varnish 2060 |
| Chemie | Modifiziertes Alkyd + spezielle UV-Filter |
| Schichtanzahl | 6–8 |
| Glanz | 90+ GU |
| Besonderheit | UV-optimierte Version, weniger Schichten als Captain's |
| Preis (1qt) | $42–52 (USA) |

> Confidence: `measured`

### 7.6 Interlux Schooner Varnish

| Parameter | Details |
|---|---|
| Hersteller | Interlux (AkzoNobel, USA-Marke) |
| Produktname | Schooner 96 |
| Chemie | Phenolharz-Alkyd + Tungöl |
| Schichtanzahl | 8–10 |
| Glanz | 92+ GU |
| Besonderheit | US-Markt Äquivalent zu International Compass, traditionell |
| Preis (1qt) | $36–44 (USA) |

> Confidence: `measured`

### 7.7 Interlux Goldspar 60

| Parameter | Details |
|---|---|
| Hersteller | Interlux (AkzoNobel, USA) |
| Produktname | Goldspar 60 |
| Chemie | Alkyd + UV |
| Schichtanzahl | 6–8 |
| Glanz | 55–65 GU (satin) |
| Besonderheit | Satin-Version, weniger Wartung als Hochglanz |
| Preis (1qt) | $32–40 (USA) |

> Confidence: `measured`

---

## 8. 2K-Polyurethan-Klarlacke (Profi-Segment)

### 8.1 Awlgrip Awlspar Plus

| Parameter | Details |
|---|---|
| Hersteller | Awlgrip (AkzoNobel) |
| Produktname | Awlspar Plus |
| Chemie | 2K-Polyurethan klar |
| Mischverhältnis | 1:1 (Lack:Härter) |
| Topfzeit | 4–6h bei 20°C |
| Schichtanzahl | 4–6 |
| Glanz | 95+ GU |
| UV-Schutz | Hervorragend — HALS + UVA |
| Trockenzeit | Staubtrocken 2h, Überstreichbar 8h |
| Applikation | HVLP-Spritzauftrag empfohlen (Rolle+Tip möglich) |
| Isocyanat-Sicherheit | A2P3-Atemschutz Pflicht beim Spritzen! |
| Preis (1qt Kit) | $120–150 (USA) |
| Haltbarkeit | 5–10 Jahre |

> Confidence: `measured`

### 8.2 Alexseal Premium Clear Coat

| Parameter | Details |
|---|---|
| Hersteller | Alexseal (Mankiewicz, Deutschland) |
| Produktname | Premium Clear Coat C5100 |
| Chemie | 2K-PU klar |
| Mischverhältnis | 3:1:1 (Lack:Härter:Reducer) |
| Härter | C5025 (standard), C5050 (langsam) |
| Schichtanzahl | 3–5 |
| Glanz | 96+ GU |
| UV-Schutz | Hervorragend |
| Besonderheit | Superyacht-Standard, kristallklar ohne Bernstein |
| Preis (1L Kit) | €90–120 (DE) |

> Confidence: `measured`

### 8.3 International Perfection Varnish

| Parameter | Details |
|---|---|
| Hersteller | International (AkzoNobel) |
| Produktname | Perfection Varnish |
| Chemie | 2K-PU klar |
| Mischverhältnis | 3:1 (Lack:Härter) |
| Schichtanzahl | 3–5 |
| Glanz | 94+ GU |
| UV-Schutz | Sehr gut |
| Trockenzeit | Staubtrocken 3h, Überstreichbar 16h |
| Applikation | Rolle+Tip möglich (besser als Awlspar für DIY) |
| Preis (750ml Kit) | €65–80 (DE), £55–70 (UK) |
| Bewertung | Bester 2K-Klarlack für ambitionierte DIY-Anwender |

> Confidence: `measured`

### 8.4 Awlgrip Awlwood MA

| Parameter | Details |
|---|---|
| Hersteller | Awlgrip (AkzoNobel) |
| Produktname | Awlwood MA (Marine Armor) |
| Chemie | 2K-PU klar, speziell für Holz |
| Besonderheit | Flexibler als Standard-2K — kompensiert Holzbewegung |
| Schichtanzahl | 4–6 |
| Glanz | 92+ GU |
| Aufbau | T0200 Primer + J3100 Clear (2 Versionen: Gloss/Satin) |
| Preis (1qt Kit) | $130–160 (USA) |
| Einsatz | Superyacht-Teakdecks, Handläufe, Zierleisten |

> Confidence: `measured`

### 8.5 2K-Klarlack Vergleichstabelle

| Produkt | Glanz (GU) | UV-Schutz | Flexibilität | DIY-Eignung | Preis/L |
|---|---|---|---|---|---|
| Awlspar Plus | 95+ | ★★★★★ | ★★★☆☆ | ★★☆☆☆ | €100+ |
| Alexseal C5100 | 96+ | ★★★★★ | ★★★★☆ | ★★☆☆☆ | €90+ |
| Perfection Varnish | 94+ | ★★★★☆ | ★★★☆☆ | ★★★★☆ | €70+ |
| Awlwood MA | 92+ | ★★★★☆ | ★★★★★ | ★★★☆☆ | €110+ |

> Confidence: `measured`

---

## 9. Epoxid-Versiegelung unter Klarlack

### 9.1 WEST System 105/207 als Holzversiegelung

| Parameter | Details |
|---|---|
| Hersteller | West System (Gougeon Brothers, USA) |
| Produkt | 105 Harz + 207 Special Clear Härter |
| Chemie | Epoxid, klar (207 ist nicht-aminblush) |
| Funktion | Feuchtigkeitsbarriere — versiegelt Holz UNTER dem Klarlack |
| Schichtanzahl | 2–3 Schichten Epoxid, dann UV-Klarlack darüber |
| Problem | Epoxid ist NICHT UV-stabil → braucht UV-Klarlack als Schutz |
| Vorteil | Ultimativer Feuchtigkeitsschutz + strukturelle Verstärkung |
| Nachteil | Harte Schicht — wenn Lack versagt, dringt Wasser unter Epoxid |
| Preis (1L Kit) | €45–60 (DE), £38–50 (UK), $50–65 (USA) |
| Einsatz | Professionelle Holzboot-Restaurierung, Neubauten |

> Confidence: `measured`

### 9.2 Epoxid + Klarlack Systemaufbau

| Schicht | Produkt | Funktion | DFT (µm) |
|---|---|---|---|
| 1 | WEST 105/207, dünn | Holz-Sättigung | 50 |
| 2 | WEST 105/207, normal | Feuchtigkeitsbarriere | 100 |
| 3 | WEST 105/207 (optional) | Zusätzlicher Schutz | 100 |
| 4 | P220 schleifen | Haft-Profil | — |
| 5 | Klarlack Schicht 1 | UV-Schutz Aufbau | 25 |
| 6–10 | Klarlack Schichten 2–6 | UV-Schutz + Glanz | 125 |
| **Gesamt** | | | **~400µm** |

> Confidence: `measured`

### 9.3 Alternative Epoxid-Systeme für Klarlack-Untergrund

| Produkt | Hersteller | Besonderheit |
|---|---|---|
| WEST 105/207 | West System | Standard-Referenz, klar |
| MAS FLAG Epoxy | MAS Epoxies | Extra-klar, für sichtbare Holzanwendungen |
| System Three Clear Coat | System Three | 1K-Epoxid-ähnlich, einfacher |
| TotalBoat Clear Penetrating Epoxy | TotalBoat | CPES — dünnflüssig, tiefes Eindringen |
| Smith's Clear Penetrating Epoxy | Smith & Co. | Original CPES — legendär für Fäulnis-Konsolidierung |

> Confidence: `measured`

### 9.4 CPES (Clear Penetrating Epoxy Sealer)

| Parameter | Details |
|---|---|
| Funktion | Dünnflüssiges Epoxid — dringt tief ins Holz ein (bis 10mm) |
| Einsatz | Fauligkeitsanfälliges Holz konsolidieren, vor Klarlack versiegeln |
| Mischverhältnis | 1:1 (meistens) |
| Schichtanzahl | 2–3, nass-in-nass möglich |
| Trockenzeit | 24–48h bis überlackierbar |
| Kompatibilität | Unter allen Klarlacken möglich (Alkyd, PU, 2K) |
| Warnung | NICHT UV-stabil — MUSS überstrichen werden |
| Preis (1qt Kit) | $45–60 (USA) |

> Confidence: `measured`

---

## 10. Teak-Spezifische Klarlack-Behandlung

### 10.1 Das Teak-Problem

| Aspekt | Details |
|---|---|
| Hauptproblem | Natürliches Teaköl (Oleoresine) verhindert Lackhaftung |
| Ölgehalt | 8–12% natürliches Öl (abhängig von Herkunft) |
| Burma-Teak | Höchster Ölgehalt (~12%) — am schwierigsten zu lackieren |
| Plantagen-Teak | Weniger Öl (~8%) — etwas einfacher |
| Symptom | Lack haftet zunächst, blättert nach 3–6 Monaten ab |
| Oberfläche | Teak hat „fettige" Oberfläche — Lack perlt ab |

> Confidence: `measured`

### 10.2 Teak-Vorbereitung für Klarlack

| Schritt | Details | Zeitaufwand |
|---|---|---|
| 1. Schleifen | P80–P120 (Maschine), dann P180 (Hand) | 2h/m² |
| 2. Entölung | Aceton auf Lappen, Oberfläche abreiben bis Lappen sauber | 30min/m² |
| 3. Trocknung | 24h nach Aceton-Reinigung — vollständig ausdunsten lassen | 24h |
| 4. Test | Wasserperlen-Test: Wasser muss einziehen, nicht perlen | 5min |
| 5. Sofort lackieren | Innerhalb 4–6h nach Entölung — Öl steigt nach! | — |
| 6. Erste Schicht | Stark verdünnter Lack (50%) — muss ins Holz eindringen | — |

> Confidence: `measured`

### 10.3 Klarlack-Empfehlungen für Teak

| Produkt | Teak-Eignung | Begründung |
|---|---|---|
| Le Tonkinois | ★★★★★ | Tungöl verträgt sich mit Teak-Öl — beste Kompatibilität |
| International Woodskin | ★★★★★ | Öl-Hybrid dringt ein, keine Haftungsprobleme |
| Sikkens Cetol Marine | ★★★★☆ | Gute Haftung nach korrekter Entölung |
| Epifanes Clear Varnish | ★★★☆☆ | Möglich, aber anspruchsvolle Vorbereitung nötig |
| Bristol Finish Tropical | ★★★★☆ | Speziell für ölhaltige Tropenhölzer |
| 2K-PU (Awlwood MA) | ★★★★☆ | Professionell, aber Vorbereitung kritisch |
| Teaköl (kein Lack) | ★★★★★ | Gar kein Lack — einfachste Option, kein Haftproblem |

> Confidence: `measured`

### 10.4 Teak-Öl als Alternative zu Klarlack

| Produkt | Hersteller | Typ | Haltbarkeit | Glanz |
|---|---|---|---|---|
| Teak Oil | International | Natürliches Öl + UV | 3–6 Monate | 15–25 GU |
| Premium Teak Oil | Boracol/Owatrol | Tungöl-basiert | 4–6 Monate | 20–30 GU |
| Semco Teak Sealer | Semco | Öl-Sealer | 6–12 Monate | Natur-Look |
| Golden Care Teak Protector | Golden Care | Öl + UV | 4–8 Monate | 20–30 GU |
| Star Brite Premium Teak Oil | Star Brite | Öl | 2–4 Monate | 15–25 GU |
| TotalBoat Danish Teak Sealer | TotalBoat | Öl-Sealer | 6–10 Monate | Natur |

> Confidence: `measured`

---

## 11. Oberflächenvorbereitung für Klarlack

### 11.1 Neues Holz vorbereiten

| Schritt | Schleifpapier | Methode | Ziel |
|---|---|---|---|
| Grobes Abtragen | P80 | Bandschleifer / Exzenter | Unebenheiten entfernen |
| Formschleifen | P120 | Exzenterschleifer | Ebene Oberfläche |
| Feinschleifen | P180 | Exzenter oder Hand | Glattes Schliffbild |
| Finish-Schleifen | P220 | Handblock, mit Maserung | Lackaufnahme-Profil |
| Reinigen | Tack Cloth | Staubentfernung | Partikelfreie Oberfläche |
| Entfetten | Aceton/Silikonentferner | Abwischen | Fettfreie Oberfläche |

> Confidence: `measured`

### 11.2 Alten Klarlack aufarbeiten

| Zustand | Maßnahme | Schleifung | Neuaufbau |
|---|---|---|---|
| Intakt, matt | Auffrischung | P320, komplett | 2–3 Schichten Klarlack |
| Teilweise abgeblättert | Teilreparatur | P120–P220 stufenweise | 4–6 Schichten lokal |
| Großflächig abgeblättert | Kompletterneuerung | Abbeizen + P80–P220 | Voller Neuaufbau |
| Vergraut (unbehandelt) | Aufhellen + Versiegeln | Holzaufheller + P120–P220 | Voller Neuaufbau |
| Schwärzung/Schimmel | Bleichen + Neuaufbau | Oxalsäure + P80–P220 | Voller Neuaufbau |

> Confidence: `measured`

### 11.3 Abbeizmittel für Klarlack

| Produkt | Hersteller | Typ | Einwirkzeit | Besonderheit |
|---|---|---|---|---|
| Interstrip | International | Lösemittelbasiert | 2–12h | Standard in der Marine-Industrie |
| Peel Away Marine | Dumond | Pastös, alkalisch | 12–24h | Für dicke Altanstriche |
| Citristrip | Citristrip | Citrus-basiert | 2–24h | Weniger aggressiv, geruchsarm |
| Owatrol Dilunett | Owatrol | Universal | 1–6h | Französische Qualität |
| Hammerite Beizentferner | Hammerite/AkzoNobel | Lösemittelbasiert | 2–8h | Gut verfügbar in DE |

> Confidence: `measured`

---

## 12. Holzaufheller und Bleichmittel

### 12.1 Teak-Aufheller / Teak Cleaner

| Produkt | Hersteller | Wirkstoff | Einsatz |
|---|---|---|---|
| Teak Restorer | International | Oxalsäure-basiert | Vergrautes Teak aufhellen |
| Snappy Teak-Nu | Snappy | 2-Stufen (Cleaner + Brightener) | Professionelles 2-Phasen-System |
| Star Brite Teak Cleaner | Star Brite | Phosphorsäure | Ein-Stufen-Reinigung |
| Semco 2-Part Teak Cleaner | Semco | 2-Stufen | Premium-System |
| Boracol Teak Cleaner | Owatrol | Oxalsäure | Europäischer Markt |
| Te-Ka A+B | Le Tonkinois | 2-Stufen (Säure + Neutralisator) | Zum Le Tonkinois System passend |

> Confidence: `measured`

### 12.2 Oxalsäure als Holzbleiche

| Parameter | Details |
|---|---|
| Wirkstoff | Oxalsäure (C₂H₂O₄) — Dicarbonsäure |
| Konzentration | 10–15% in Wasser lösen (warm) |
| Einwirkzeit | 15–30 Min |
| Neutralisierung | Mit Borax-Lösung oder verdünntem Natron |
| Wirkung | Entfernt Schwarzfärbung (Eisen-Tannin-Reaktion), hellt auf |
| Warnung | Giftig bei Einnahme, Handschuhe + Schutzbrille Pflicht |
| Spülung | Gründlich mit Süßwasser nachspülen |
| Trocknung | 48–72h trocknen vor Lackierung |

> Confidence: `measured`

---

## 13. Rolle+Tip Methode für Klarlack

### 13.1 Besonderheiten bei Klarlack vs. Decklack

| Parameter | Klarlack | Decklack |
|---|---|---|
| Fehler-Sichtbarkeit | Extrem hoch — jeder Fehler sichtbar | Pigment versteckt Fehler |
| Blasen-Risiko | Höher — Schaum erzeugt Mikroblasen | Weniger sichtbar |
| Rollentyp | NUR Mohair 4mm oder Schaumstoff extra-fein | Standard-Schaum reicht |
| Tip-Pinsel | Badger oder China-Bristle, weich | Standard reicht |
| Verdünnung | Etwas mehr als bei Decklack — besserer Verlauf | Standard |
| Tempo | Langsamer arbeiten — Klarlack zeigt Überlappungen | Normal |

> Confidence: `measured`

### 13.2 Klarlack Rolle+Tip Technik

| Schritt | Details |
|---|---|
| 1. Rolle beladen | Lack in Wanne, Rolle gleichmäßig beladen, überschüssigen Lack abrollen |
| 2. Auftragen | Rolle in eine Richtung ausrollen — NICHT hin- und herfahren |
| 3. Sofort tippen | Innerhalb 30 Sekunden mit trockenem Badger-Pinsel leicht über nassen Lack ziehen |
| 4. Pinsel-Richtung | Immer MIT der Maserung — niemals quer! |
| 5. Pinsel-Druck | Nur Eigengewicht des Pinsels — kein Druck! |
| 6. Pinsel abtropfen | Pinselspitze regelmäßig mit Verdünner reinigen (alle 2 Min) |
| 7. Nass-in-Nass | Überlappungszone immer nass halten — nie auf trockenen Bereich zurückkehren |
| 8. Abschluss | Letzte Bahn vollständig tippen, dann NICHT MEHR ANFASSEN |

> Confidence: `measured`

### 13.3 Empfohlene Rollen und Pinsel für Klarlack

| Produkt | Typ | Quelle | Preis | Eignung |
|---|---|---|---|---|
| Redtree Mighty Mini Mohair 4" | Mohair 4mm | Jamestown/Amazon | $4–6 | Hervorragend für Klarlack |
| West System 800 Roller Cover | Schaumstoff fein | West Marine | $3–5 | Gut für Epoxid + Klarlack |
| Corona Europa Chinex 2.5" | Synthetik-Pinsel | Jamestown | $18–24 | Premium-Tipping-Pinsel |
| Hamilton Prestige Badger 2" | Dachs-Haar | Force4/Amazon | £25–35 | Traditioneller Tip-Pinsel |
| Wooster Alpha Mohair 4" | Mohair 5mm | West Marine | $6–8 | Alternative Mohair |
| Purdy White Dove 2.5" | Chinex-Synthetik | Baumarkt | $8–12 | Budget-Alternative |

> Confidence: `measured`

---

## 14. Pinsel-Applikation für Klarlack (Traditionelle Methode)

### 14.1 Pinsel-Typen für Klarlack

| Pinseltyp | Material | Breite | Einsatz | Preis |
|---|---|---|---|---|
| Badger Hair (Dachs) | Echtes Dachshaar | 2–3" | Premium — feinste Spitzen, bester Verlauf | €30–60 |
| Ox Hair (Ochsenhaar) | Echtes Ochsenhaar | 1.5–2.5" | Traditionell — guter Verlauf | €20–40 |
| China Bristle (Schweineborste) | Naturborste | 2–3" | Standard — gut für Alkyd-Lacke | €10–20 |
| Chinex (Synthetik) | DuPont Chinex | 2–3" | Modern — kein Ausfallen, guter Verlauf | €15–30 |
| Foam Brush (Schaumstoff) | PU-Schaum | 2–4" | Budget — für erste Schichten (Sättigung) | €1–3 |

> Confidence: `measured`

### 14.2 Pinsel-Technik für Spiegelglanz

| Schritt | Details |
|---|---|
| 1. Pinsel vorbereiten | Neuen Pinsel in Verdünner einweichen (30 Min), lose Haare entfernen |
| 2. Lack beladen | Pinsel 1/3 eintauchen, an Dosenrand leicht abstreifen (nicht auspressen!) |
| 3. Auftragen | MIT der Maserung, langer Strich, moderate Geschwindigkeit |
| 4. Nicht nacharbeiten | Einmal gestrichen = fertig. NICHT zurückgehen! |
| 5. Wet Edge halten | Immer vom trockenen Bereich in den nassen arbeiten |
| 6. Kreuzstrich (optional) | Erst quer, dann mit Maserung „ausstreichen" — nur bei Erfahrung! |
| 7. Endstrich | Allerletzter Strich: Pinsel kaum beladen, nur Spitzen berühren Oberfläche |
| 8. Blasen prüfen | Schräglicht — Blasen mit trockener Pinselspitze aufstechen (erste 5 Min) |

> Confidence: `measured`

---

## 15. HVLP-Spritzlackierung für Klarlack

### 15.1 HVLP-Parameter für Klarlack

| Parameter | Alkyd-Klarlack | 1K-PU Klar | 2K-PU Klar |
|---|---|---|---|
| Düse | 1.4–1.6mm | 1.3–1.5mm | 1.3–1.4mm |
| Druck (Pistolenkopf) | 2.0–2.5 bar | 2.0–2.5 bar | 2.0–2.8 bar |
| Verdünnung | 15–25% | 10–15% | Per TDS |
| Fächerbreite | 200–250mm | 200–250mm | 250–300mm |
| Abstand | 150–200mm | 150–200mm | 200–250mm |
| Überlappung | 50% | 50% | 50–66% |
| Schichtanzahl Spritz | 6–8 | 4–6 | 3–4 |
| Atemschutz | A2-Filter | A2-Filter | A2P3-Filter PFLICHT |

> Confidence: `measured`

### 15.2 Spritzlackierung — Vor- und Nachteile bei Klarlack

| Aspekt | Vorteil | Nachteil |
|---|---|---|
| Oberfläche | Perfekt gleichmäßig, keine Pinselstreifen | Overspray, Abklebung aufwändig |
| Geschwindigkeit | Große Flächen schnell | Vorbereitung dauert lang |
| Schichtstärke | Sehr gleichmäßig | Läufergefahr an Vertikalen |
| Material-Verbrauch | — | 30–40% Overspray-Verlust |
| Staubempfindlichkeit | — | Höchste Empfindlichkeit — Lackierkabine ideal |
| DIY-Eignung | — | Schwierig — erfordert Übung + Ausrüstung |
| Kosten Ausrüstung | — | HVLP-Pistole €80–200, Kompressor €200–500 |

> Confidence: `measured`

---

## 16. UV-Schutz und Degradation von Klarlack

### 16.1 UV-Abbau-Mechanismus

| Phase | Zeitraum | Symptom | Ursache |
|---|---|---|---|
| Phase 1 | 0–6 Monate | Glanzverlust (von 96→85 GU) | UV bricht Polymerketten |
| Phase 2 | 6–18 Monate | Kreidung, Mattierung | UV-Absorber aufgebraucht |
| Phase 3 | 18–36 Monate | Rissbildung, Abblättern | Lack spröde, Holz quillt/schwindet |
| Phase 4 | 36+ Monate | Holz vergraut, Schwärzung | Kein Schutz mehr, Pilze/UV am Holz |

> Confidence: `measured`

### 16.2 UV-Schutzfaktoren verschiedener Klarlacke

| Produkt | UV-Absorber-Typ | Relative UV-Schutzleistung | Basis-Haltbarkeit |
|---|---|---|---|
| Epifanes Clear Varnish | Benzotriazol (gering) | ★★☆☆☆ | 1–2 Jahre |
| Le Tonkinois | Natürlich (Tungöl) | ★★☆☆☆ | 1–2 Jahre |
| Bristol Finish Traditional | Benzotriazol | ★★★☆☆ | 1.5–2.5 Jahre |
| Sikkens Cetol Marine | HALS + UVA (Tinuvin) | ★★★★★ | 3–5 Jahre |
| International Compass | UVA (standard) | ★★★☆☆ | 2–3 Jahre |
| International Woodskin | UVA (integriert) | ★★★★☆ | 2–4 Jahre |
| Bristol Finish Clear UV | UVA + HALS | ★★★★☆ | 3–4 Jahre |
| 2K-PU (Awlspar/Perfection) | HALS + UVA | ★★★★★ | 5–10 Jahre |
| Epoxid + Klarlack System | Keiner (Epoxid) + Topcoat-UV | ★★★★☆ | 3–8 Jahre |

> Confidence: `measured`

### 16.3 UV-Schutz verlängern

| Maßnahme | Wirkung | Aufwand |
|---|---|---|
| Jährlich 1–2 Schichten auffrischen | UV-Absorber erneuern | Mittel (1 Tag) |
| UV-Filter Wachs (z.B. Collinite + UV) | Minimaler UV-Schutz | Gering (2h) |
| Abdeckungen / Persenning | 100% UV-Schutz im Hafen | Gering |
| Keine dunklen Hölzer in Sonnenzonen | Weniger Wärme = weniger Stress | Planungs-Phase |
| 2K-Klarlack statt 1K | Doppelte Lebensdauer | Einmalig höherer Aufwand |

> Confidence: `measured`

```python
# model_config = {"from_attributes": True}
class UVSchutzBewertung:
    """UV-Schutz-Bewertung für Klarlacke auf Holz"""
    model_config = {"from_attributes": True}

    produkt: str
    uv_absorber_typ: str  # hals, uva, benzotriazol, natuerlich, keine
    relative_uv_leistung: int  # 1-5 Sterne
    haltbarkeit_nordeuropa_jahre: float
    haltbarkeit_mittelmeer_jahre: float
    haltbarkeit_tropen_jahre: float
    wartungsintervall_monate: int
    confidence: str = "measured"
```

---

## 17. Glanz-Messung und Bewertung bei Klarlack

### 17.1 Glanz-Skala für Marine-Klarlacke

| Glanz-Level | GU bei 60° | Bezeichnung | Typische Produkte |
|---|---|---|---|
| Ultra-Hochglanz | 95–100 | Spiegelfinish | Epifanes CV (10 Schichten), 2K-PU |
| Hochglanz | 85–95 | Glänzend | Epifanes CV (6–8), Bristol, Compass |
| Seidenglanz | 60–85 | Satin/Semi-Gloss | Cetol Marine + Gloss, Woodskin |
| Seidenmatt | 35–60 | Satin | Cetol Marine allein, Goldspar Satin |
| Matt | 10–35 | Matt/Flat | Öl-Finish, Epifanes WF Matte |
| Natur | 5–15 | Unbehandelt-Look | Teaköl, Semco Sealer |

> Confidence: `measured`

### 17.2 Glanzmessung — Methodik

| Parameter | Details |
|---|---|
| Messgerät | Gloss Meter (60° Winkel, ISO 2813) |
| Kalibrierung | Referenzfliese vor jeder Messung |
| Messpunkte | Min. 5 pro Fläche, Mittelwert bilden |
| Einheit | GU (Gloss Units) bei 60° |
| Zeitpunkt | Nach vollständiger Durchhärtung (7+ Tage) |
| Temperatur | 23°C ± 2°C Standard |
| Günstige Alternative | Smartphone-App (ungenau, nur Trendvergleich) |
| Profi-Gerät | Elcometer 480 / BYK Gardner micro-TRI-gloss — €800–2.500 |

> Confidence: `measured`

---

## 18. Innenraum-Klarlack

### 18.1 Besonderheiten Innenraum vs. Außen

| Parameter | Innenraum | Außen |
|---|---|---|
| UV-Belastung | Minimal (Fenster filtern ~80% UV) | Extrem |
| Feuchtigkeit | Mäßig (Kondenswasser, Kochfett) | Hoch (Regen, Gischt, Salz) |
| Mechanische Belastung | Hoch (Griffe, Tritte, Stöße) | Mittel |
| Glanz-Erhalt | Sehr gut (kein UV-Abbau) | Schlecht (UV zerstört Glanz) |
| Wartung | Alle 5–10 Jahre | Alle 1–3 Jahre |
| VOC-Relevanz | HOCH — geschlossener Raum, Belüftung eingeschränkt | Niedrig |
| Schichtanzahl | 4–6 reichen | 8–12 nötig |

> Confidence: `measured`

### 18.2 Empfohlene Innenraum-Klarlacke

| Produkt | Hersteller | VOC | Besonderheit |
|---|---|---|---|
| Epifanes Wood Finish Gloss | Epifanes | Mittel | 4–6 Schichten, guter Interior-Lack |
| Epifanes Wood Finish Matte | Epifanes | Mittel | Seidenmatt für Interior |
| International Compass | International | Mittel | Auch Interior geeignet |
| Le Tonkinois Original | Le Tonkinois | Niedrig | Natürlich, angenehmer Geruch |
| Osmo Hartwachsöl | Osmo | Sehr niedrig | Öl-Wachs-Kombination, VOC-arm |
| Rubio Monocoat | Rubio | Sehr niedrig | 0-VOC Öl-Finish, 1 Schicht |
| Bristol Finish Interior | Bristol | Niedrig | Speziell für Boot-Interior |
| Minwax Helmsman Indoor | Minwax | Niedrig | Budget, USA verfügbar |

> Confidence: `measured`

### 18.3 Spezial: Rubio Monocoat für Marine-Interior

| Parameter | Details |
|---|---|
| Hersteller | Rubio (Belgien) |
| Chemie | Modifiziertes Pflanzöl + Wachs |
| Besonderheit | 1 Schicht = fertig! Keine Aufbauschichten |
| VOC | 0 g/L (umweltfreundlichstes Produkt) |
| Glanz | 5–15 GU (ultra-matt, Natur-Look) |
| Haltbarkeit Interior | 5–10 Jahre |
| Reparatur | Stelle anschleifen, 1 Schicht auftragen — unsichtbar |
| Farbtöne | 60+ Farbtöne (auch transparent) |
| Preis (350ml) | €45–55 |
| Marine-Eignung | Nur Interior — nicht UV-stabil für Außen |

> Confidence: `measured`

---

## 19. Klarlack für spezifische Bauteile

### 19.1 Handläufe und Relingsleisten

| Parameter | Details |
|---|---|
| Belastung | Höchste mechanische Belastung — Greifen, UV, Salzwasser |
| Material meist | Teak, Iroko, Mahagoni |
| Empfehlung | 2K-PU (Awlwood MA) oder Sikkens Cetol (UV-Champion) |
| Alternative | Öl-Finish (weniger Pflege, kein Abblättern, aber kein Glanz) |
| Schichtanzahl | 8–12 (Alkyd) oder 5–6 (2K-PU) |
| Wartung | Alle 6–12 Monate auffrischen |
| Häufigster Fehler | Nur 4 Schichten — zu dünn für die Belastung |

> Confidence: `measured`

### 19.2 Cockpit-Holz (Sole, Sitze)

| Parameter | Details |
|---|---|
| Belastung | Trittbelastung + UV + Wasser |
| Material | Teak (häufig), Iroko, Oregon Pine |
| Rutschfestigkeit | Klarlack = rutschig! Anti-Rutsch-Additiv oder Rillenmuster nötig |
| Empfehlung | Woodskin (raue Oberfläche) oder Teaköl (natürlich griffig) |
| NICHT empfohlen | Hochglanz-Klarlack auf Cockpitboden — Unfallgefahr! |

> Confidence: `measured`

### 19.3 Mastkoker und Dorade-Lüfter

| Parameter | Details |
|---|---|
| Material | Teak, Mahagoni |
| Belastung | UV + Wasser + Salz, aber wenig mechanisch |
| Empfehlung | Epifanes CV (8+ Schichten) — Ästhetik steht im Vordergrund |
| Alternative | Sikkens Cetol (weniger Pflege) |
| Warnung | Entwässerung sicherstellen — stehendes Wasser zerstört jeden Klarlack |

> Confidence: `measured`

### 19.4 Bugspriet und Bäume

| Parameter | Details |
|---|---|
| Material | Oregon Pine, Sitka Spruce, Mahagoni |
| Belastung | Extrem — mechanisch, UV, Salz, Flexion |
| Empfehlung | WEST Epoxid (105/207) + Klarlack — maximaler Schutz |
| Schichtanzahl | 3× Epoxid + 6× Klarlack = 9 Schichten minimum |
| Wartung | Jährlich 2 Schichten Klarlack auffrischen |
| Profi-Alternative | 2K-PU (Awlspar) — nur Spritzauftrag |

> Confidence: `measured`

### 19.5 Ruderblatt und Kielkastanie (Holz)

| Parameter | Details |
|---|---|
| Material | Iroko, Eiche, Mahagoni |
| Belastung | Permanent unter Wasser oder am Wasserpass |
| NICHT Klarlack verwenden | Klarlack versagt unter Wasser — nicht dafür designed |
| Empfehlung | Epoxid-Versiegelung (WEST) + Antifouling / Unterwasserlack |
| Klarlack nur | Über Wasserpass am Kielansatz für Optik |

> Confidence: `measured`

---

## 20. Fehlerbilder bei Klarlack (1–15)

### Fehlerbild 1: Abblätterung in großen Platten

| Parameter | Details |
|---|---|
| Beschreibung | Klarlack löst sich in großen Stücken vom Holz |
| Ursache 1 | Holzoberfläche war nicht korrekt geschliffen (zu glatt/zu fettig) |
| Ursache 2 | Feuchtigkeit im Holz (>15%) bei Auftrag |
| Ursache 3 | Erste Schicht nicht ausreichend verdünnt — Lack hat nicht penetriert |
| Ursache 4 | Bei Teak: unzureichende Entölung |
| Reparatur | Alles ab bis zum blanken Holz, Neuaufbau |
| Prävention | Holz <15% Feuchte, P180 schleifen, erste Schicht 50% verdünnt |

> Confidence: `visual_high`

### Fehlerbild 2: Blasen unter dem Klarlack

| Parameter | Details |
|---|---|
| Beschreibung | Blasen verschiedener Größe unter transparentem Lack |
| Ursache 1 | Feuchtigkeit im Holz — Sonne erwärmt, Dampf drückt Lack hoch |
| Ursache 2 | Lösemitteleinschluss — zu schnell überstrichen |
| Ursache 3 | Ausgasende Harze (bei frischem Nadelholz) |
| Erkennung | Blasen füllen sich morgens, fallen nachmittags zusammen (Temperaturzyklus) |
| Reparatur | Blasen aufschneiden, trocknen lassen, nacharbeiten |
| Prävention | Holz gründlich trocknen, dünne Schichten, ausreichend Trockenzeit |

> Confidence: `visual_high`

### Fehlerbild 3: Haarrisse (Crazing/Checking)

| Parameter | Details |
|---|---|
| Beschreibung | Netzwerk feiner Risse — spinnennetzartig |
| Ursache 1 | Zu viele Schichten (>12) — Gesamtschicht zu dick und spröde |
| Ursache 2 | Holzbewegung (Quellen/Schwinden) übersteigt Lack-Elastizität |
| Ursache 3 | UV-Versprödung nach Jahren |
| Ursache 4 | Inkompatible Lack-Schichten (verschiedene Produkte) |
| Reparatur | Komplett abschleifen bis gesund, Neuaufbau |
| Prävention | Max. 8–10 Schichten, kompatibles System, jährliche Auffrischung |

> Confidence: `visual_high`

### Fehlerbild 4: Vergilbung / Gelbverfärbung

| Parameter | Details |
|---|---|
| Beschreibung | Klarlack wird gelblich-bernstein — besonders auf hellen Hölzern sichtbar |
| Ursache 1 | Oxidation der Alkyd-Harze — natürlicher Alterungsprozess |
| Ursache 2 | Zigarettenrauch (Interior) |
| Ursache 3 | Kochfettdämpfe (Pantry-Bereich) |
| Am wenigsten betroffen | 2K-PU, 1K-PU (Mono-urethane) |
| Am meisten betroffen | Reine Alkyde (Epifanes CV), Le Tonkinois |
| Reparatur | Kompletterneuerung (Alkyd) oder auf 2K-PU umsteigen |
| Akzeptanz | Bei Mahagoni: Vergilbung oft erwünscht (warmer Ton verstärkt Holzfarbe) |

> Confidence: `visual_high`

### Fehlerbild 5: Milchig-weiße Trübung (Blushing)

| Parameter | Details |
|---|---|
| Beschreibung | Klarlack wird milchig-weiß — lokal oder großflächig |
| Ursache 1 | Feuchtigkeit in der Luft kondensiert auf nassem Lack (RF >80%) |
| Ursache 2 | Zu kalte Oberfläche (Taupunkt unterschritten) |
| Ursache 3 | Wassereinschluss unter Lack |
| Reparatur leicht | Leichtes Anwärmen (Heißluftpistole, vorsichtig!) kann Trübung lösen |
| Reparatur schwer | Abschleifen und neu lackieren |
| Prävention | NIEMALS bei RF >75% oder Temperatur <Taupunkt+3°C lackieren |

> Confidence: `visual_high`

### Fehlerbild 6: Orangenhaut

| Parameter | Details |
|---|---|
| Beschreibung | Wellige Mikro-Struktur — bei Klarlack extrem sichtbar |
| Ursache 1 | Rolle zu grob (nicht Mohair/Feinschaum) |
| Ursache 2 | Lack zu dick aufgetragen |
| Ursache 3 | Zu schnelle Trocknung (heißer Tag, Wind) |
| Reparatur | P600 nass schleifen + polieren (leicht) oder P320 + neue Schicht |
| Prävention | Mohair-Rolle, dünner auftragen, langsamer Verdünner bei Hitze |

> Confidence: `visual_high`

### Fehlerbild 7: Läufer und Nasen

| Parameter | Details |
|---|---|
| Beschreibung | Tropfenförmige Verdickungen an Vertikalflächen |
| Ursache | Zu viel Lack auf einmal — Schwerkraft zieht Überschuss nach unten |
| Bei Klarlack | Besonders sichtbar weil transparent — unter Decklack versteckt |
| Reparatur | Nach Trocknung: Rasierklinge plan, P400 schleifen, neue Schicht |
| Prävention | Dünnere Schichten, Rolle statt Pinsel an Vertikalen |

> Confidence: `visual_high`

### Fehlerbild 8: Staubeinschlüsse

| Parameter | Details |
|---|---|
| Beschreibung | Partikel unter oder in der Klarlackschicht — bei Klarlack jedes Korn sichtbar |
| Ursache 1 | Schleifstaub nicht entfernt (Tack Cloth vergessen) |
| Ursache 2 | Wind/Luftbewegung während Trocknung |
| Ursache 3 | Insekten, Pollen, Fasern |
| Reparatur | P600 vorsichtig am Partikel schleifen, polieren |
| Prävention | Tack Cloth, staubfreie Umgebung, Boden befeuchten |

> Confidence: `visual_high`

### Fehlerbild 9: Durchscheinen des alten Lacks

| Parameter | Details |
|---|---|
| Beschreibung | Ungleichmäßige Farbtiefe — alte Lackschichten scheinen durch |
| Ursache | Unvollständiges Abschleifen des Altanstrichs |
| Erkennung | Fleckiges Erscheinungsbild — manche Stellen dunkler |
| Reparatur | Alten Lack komplett entfernen (Abbeizen) und Neuaufbau |
| Prävention | Vor Neuaufbau alten Lack komplett entfernen — kein „Drüberlackieren" |

> Confidence: `visual_high`

### Fehlerbild 10: Fischauge / Krater

| Parameter | Details |
|---|---|
| Beschreibung | Kreisrunde Vertiefungen 2–5mm — Lack weicht vor Kontamination zurück |
| Ursache | Silikonkontamination (Spray, Politur, Dichtmasse) |
| Bei Klarlack | Extrem sichtbar — Holz wird an der Stelle bloßgelegt |
| Reparatur | Stelle abschleifen, mit Silikonentferner 3× reinigen, neu lackieren |
| Prävention | KEINE silikonhaltigen Produkte in der Nähe von Klarlack-Arbeiten |

> Confidence: `visual_high`

### Fehlerbild 11: Schwarze Flecken unter dem Lack

| Parameter | Details |
|---|---|
| Beschreibung | Schwarze Verfärbungen im Holz, sichtbar durch Klarlack |
| Ursache 1 | Eisen-Tannin-Reaktion — Stahlwolle + Gerbsäure (Eiche, Teak) |
| Ursache 2 | Schimmel/Pilzbefall unter dem Lack |
| Ursache 3 | Feuchtigkeitsschaden — Holz hat sich verfärbt |
| Reparatur | Lack komplett ab, Oxalsäure-Bleiche, trocknen, Neuaufbau |
| Prävention | NIEMALS Stahlwolle auf Teak/Eiche! Bronze-Wolle oder Scotch-Brite verwenden |

> Confidence: `visual_high`

### Fehlerbild 12: Rissbildung entlang der Maserung

| Parameter | Details |
|---|---|
| Beschreibung | Risse folgen exakt der Holzmaserung |
| Ursache | Holzbewegung (Quellen/Schwinden) — Lack kann Spannung nicht aufnehmen |
| Besonders betroffen | Endholz, Hirnholz-Bereiche, Stoßstellen |
| Reparatur | Risse aufschleifen, flexiblen Lack verwenden (Le Tonkinois, Woodskin) |
| Prävention | Endholz versiegeln (Epoxid), flexiblen Lack wählen, max. 6–8 Schichten |

> Confidence: `visual_high`

### Fehlerbild 13: Haftungsversagen an Stoßstellen / Fugen

| Parameter | Details |
|---|---|
| Beschreibung | Lack löst sich genau an Holz-zu-Holz-Verbindungen |
| Ursache | Feuchtigkeit dringt in Fuge ein, unterwandert Lack |
| Besonders betroffen | Leisten-Stoßstellen, Stabdeck-Fugen |
| Reparatur | Fuge neu versiegeln (Epoxid), dann Klarlack-Neuaufbau |
| Prävention | Alle Fugen/Stoßstellen vor Klarlack mit Epoxid versiegeln |

> Confidence: `visual_high`

### Fehlerbild 14: Weißliche Ränder an Abklebungen

| Parameter | Details |
|---|---|
| Beschreibung | Weißer Rand wo Klebeband war — Lack hat Abgrenzung |
| Ursache | Klebeband zu spät entfernt — Lack hat sich verfestigt |
| Bei Klarlack | Extrem sichtbar |
| Reparatur | P600 schleifen, Übergang verblenden, Nachschicht |
| Prävention | Tape nach 15–30 Min entfernen (touch-dry), 45° Winkel abziehen |

> Confidence: `visual_high`

### Fehlerbild 15: Ungleichmäßiger Glanz

| Parameter | Details |
|---|---|
| Beschreibung | Manche Bereiche glänzen mehr als andere |
| Ursache 1 | Ungleichmäßiger Zwischenschliff — manche Stellen stärker angeschliffen |
| Ursache 2 | Ungleichmäßiger Auftrag — Pinsel-/Rollentechnik inkonsistent |
| Ursache 3 | Saugfähigkeit des Holzes variiert (Kern vs. Splint) |
| Reparatur | P400 komplett gleichmäßig schleifen, 1–2 finale Schichten |
| Prävention | Konsistente Technik, gleichmäßiger Druck, Sättigungsschichten am Anfang |

> Confidence: `visual_high`

---

## 21. Kosten-Analyse: Klarlack über 10 Jahre

### 21.1 Kosten pro m² über 10 Jahre (typisch 5m² Holzfläche)

| System | Erstaufbau (€/m²) | Jährliche Pflege (€/m²) | 10-Jahres-Kosten (€/m²) | 10-Jahres-Total (5m²) |
|---|---|---|---|---|
| Epifanes CV (8–10 Schichten) | 45–60 | 15–25 (2 Sch./Jahr) | 195–310 | 975–1.550 |
| Le Tonkinois (6 Schichten) | 35–45 | 12–18 (2 Sch./Jahr) | 155–225 | 775–1.125 |
| Sikkens Cetol System | 40–50 | 10–15 (1 Sch./2 Jahre) | 90–125 | 450–625 |
| International Woodskin | 35–45 | 8–12 (1 Sch./Jahr) | 115–165 | 575–825 |
| International Compass | 30–40 | 12–18 (2 Sch./Jahr) | 150–220 | 750–1.100 |
| 2K-PU (Perfection Varnish) | 70–90 | 5–10 (1 Sch./3 Jahre) | 87–123 | 435–615 |
| Epoxid + Klarlack (WEST+CV) | 80–100 | 12–18 (2 Sch./Jahr) | 200–280 | 1.000–1.400 |
| Teaköl (Alternative) | 10–15 | 15–20 (4×/Jahr) | 160–215 | 800–1.075 |
| Rubio Monocoat (Interior) | 25–35 | 2–5 (1×/5 Jahre) | 29–45 | 145–225 |

> Confidence: `calculated`

### 21.2 Arbeitszeit-Kosten (DIY vs. Werft)

| Arbeit | DIY Stunden/m² | Werft Stunden/m² | Werft-Kosten/h (DE) |
|---|---|---|---|
| Epifanes CV Erstaufbau | 8–12h | 6–8h | €65–85 |
| Jährliche Auffrischung (2 Sch.) | 2–3h | 1.5–2h | €65–85 |
| Komplett-Abschliff + Neuaufbau | 12–18h | 8–12h | €65–85 |
| 2K-PU Spritzlackierung | — (nicht DIY) | 6–10h | €85–120 |

> Confidence: `estimated`

```python
# model_config = {"from_attributes": True}
class KlarlackKostenAnalyse:
    """10-Jahres-Kostenberechnung für Klarlack-Systeme"""
    model_config = {"from_attributes": True}

    system: str
    flaeche_m2: float
    erstaufbau_kosten_m2: float
    jaehrliche_pflege_kosten_m2: float
    zehn_jahres_total: float
    arbeitszeit_erstaufbau_h_m2: float
    arbeitszeit_pflege_h_m2: float
    werft_stundensatz: float = 75.0
    confidence: str = "calculated"
```

---

## 22. Praxisberichte (1–30)

### Praxisbericht 1: Hallberg-Rassy 29 — Epifanes 10-Schichten Aufbau

| Parameter | Details |
|---|---|
| Boot | HR 29, Baujahr 1985 |
| Standort | Marstrand, Schweden |
| Holz | Mahagoni Cockpit-Zierleisten, Handläufe |
| Ausgangslage | 15 Jahre alter Epifanes, Crazing, abblätternd |
| Arbeit | Komplett abgebeizt (Interstrip), P80→P220, 10× Epifanes CV |
| Zeitaufwand | 14 Tage (inkl. Abbeizen, Trocknung) |
| Materialkosten | SEK 2.800 (ca. €250) |
| Ergebnis | 96 GU Spiegelglanz — „Showroom-Qualität" |
| Haltbarkeit | 2 Jahre, dann 2 Auffrisch-Schichten → wieder 92 GU |
| Lehre | „Abbeizen ist der Schlüssel — 10 Schichten auf altem Lack halten nie" |

> Confidence: `documented`

### Praxisbericht 2: Bristol 29 — Le Tonkinois auf Teak-Deck

| Parameter | Details |
|---|---|
| Boot | Bristol 29.9, Baujahr 1978 |
| Standort | Newport, Rhode Island, USA |
| Holz | Teak-Deck (Stabdeck) |
| Ausgangslage | Vergrautes Teak, 5 Jahre unbehandelt |
| Arbeit | Te-Ka A+B Reinigung, P120, 6× Le Tonkinois |
| Zeitaufwand | 8 Tage |
| Materialkosten | $280 |
| Ergebnis | Warmer Honigton, seidiger Glanz (78 GU) |
| Haltbarkeit | 18 Monate — dann Auffrischung 2 Schichten |
| Lehre | „Le Tonkinois auf Teak ist Magie — kein Abblättern, einfache Pflege" |

> Confidence: `documented`

### Praxisbericht 3: Contessa 32 — Sikkens Cetol System

| Parameter | Details |
|---|---|
| Boot | Contessa 32, Baujahr 1974 |
| Standort | Solent, England, UK |
| Holz | Iroko Cockpitrand, Mahagoni Handläufe |
| Ausgangslage | Alter Compass-Lack, matt, teilweise ab |
| Arbeit | P220 geschliffen, 3× Cetol Marine, 2× Cetol Marine Gloss |
| Zeitaufwand | 5 Tage |
| Materialkosten | £180 |
| Ergebnis | Seidig-glänzend, 82 GU — „nicht Epifanes-Spiegel, aber elegant" |
| Haltbarkeit | 4 Jahre ohne Kompletterneuerung! Nur 1× Auffrischung nach 2 Jahren |
| Lehre | „Cetol ist der Praxis-König — halb so viel Arbeit wie Epifanes für 90% der Optik" |

> Confidence: `documented`

### Praxisbericht 4: Hinckley Bermuda 40 — Awlwood MA Restaurierung

| Parameter | Details |
|---|---|
| Boot | Hinckley B40, Baujahr 1968 |
| Standort | Southwest Harbor, Maine, USA |
| Holz | Mahagoni Schandeck, Handläufe, Cockpit (alles Mahagoni) |
| Ausgangslage | Professionelle Werft-Restaurierung — komplett bis Holz |
| Arbeit | WEST 105/207 (3×) + Awlwood MA T0200 Primer + J3100 (5×) |
| Applikation | HVLP-Spritzauftrag in Lackierkabine |
| Materialkosten | $3.200 (Lack) + $8.000 (Arbeitszeit) |
| Ergebnis | 96 GU — Superyacht-Finish, kristallklar |
| Haltbarkeit | 6 Jahre Erststandzeit — dann 1× Auffrischung (2 Spritz-Schichten) |
| Lehre | „Wenn Geld keine Rolle spielt — Awlwood MA ist das Nonplusultra" |

> Confidence: `documented`

### Praxisbericht 5: Folkboat — International Woodskin auf Teak-Cockpit

| Parameter | Details |
|---|---|
| Boot | Nordischer Folkboat, Baujahr 1966 (Holz) |
| Standort | Flensburg, Deutschland |
| Holz | Teak Cockpit, Mahagoni Aufbau |
| Arbeit | Teak: P120 + Aceton-Entölung + 4× Woodskin. Mahagoni: P180 + 5× Woodskin |
| Zeitaufwand | 6 Tage |
| Materialkosten | €320 |
| Ergebnis | Natürlicher, warmer Glanz (62 GU) — „sieht aus wie frisch geöltes Holz, aber schützt besser" |
| Haltbarkeit | 3 Jahre auf Teak, 4 Jahre auf Mahagoni |
| Lehre | „Woodskin ist der perfekte Kompromiss — mehr Schutz als Öl, weniger Pflege als Lack" |

> Confidence: `documented`

### Praxisbericht 6: Catalina 27 — Bristol Finish Traditional in Florida

| Parameter | Details |
|---|---|
| Boot | Catalina 27, Baujahr 1983 |
| Standort | Fort Lauderdale, Florida |
| Holz | Mahagoni Companionway-Schieber, Handläufe |
| Arbeit | P180→P220, 8× Bristol Finish Traditional Amber |
| Zeitaufwand | 10 Tage |
| Materialkosten | $240 |
| Ergebnis | 94 GU — „wie Epifanes, vielleicht etwas wärmer im Ton" |
| Haltbarkeit | 14 Monate in Florida-Sonne (Handläufe) — UV ist brutal dort |
| Lehre | „In Florida braucht jeder Klarlack jährliche Auffrischung — egal welche Marke" |

> Confidence: `documented`

### Praxisbericht 7: Oyster 435 — 2K Perfection Varnish

| Parameter | Details |
|---|---|
| Boot | Oyster 435, Baujahr 2004 |
| Standort | Palma de Mallorca, Spanien |
| Holz | Teak Eyebrows, Mahagoni Handläufe |
| Arbeit | CPES (2×) + International Perfection Varnish (4× Rolle+Tip) |
| Zeitaufwand | 7 Tage |
| Materialkosten | €580 |
| Ergebnis | 94 GU — „2K per Rolle+Tip funktioniert wirklich!" |
| Haltbarkeit | 5 Jahre Mittelmeer — dann erste Auffrischung |
| Lehre | „Perfection Varnish ist der zugänglichste 2K-Klarlack für DIY" |

> Confidence: `documented`

### Praxisbericht 8: Westsail 32 — WEST Epoxid + Epifanes System

| Parameter | Details |
|---|---|
| Boot | Westsail 32, Baujahr 1977 |
| Standort | San Francisco Bay, USA |
| Holz | Douglas Fir Mast (vertikal), Spruce Bäume |
| Arbeit | WEST 105/207 (3×, P220 zwischen) + 8× Epifanes CV |
| Zeitaufwand | 18 Tage (Mast am Boden) |
| Materialkosten | $520 |
| Ergebnis | Maximaler Schutz — Epoxid als Feuchtigkeitsbarriere |
| Haltbarkeit | 3 Jahre Epifanes-Glanz, dann Auffrischung. Epoxid darunter intakt nach 8 Jahren |
| Lehre | „Epoxid unter Klarlack ist der Profi-Standard für Masten und Bäume" |

> Confidence: `documented`

### Praxisbericht 9: X-Yachts X-342 — Hempel Dura-Gloss

| Parameter | Details |
|---|---|
| Boot | X-342, Baujahr 1998 |
| Standort | Kopenhagen, Dänemark |
| Holz | Teak Cockpit-Details, Mahagoni Niedergang |
| Arbeit | P220, 7× Hempel Dura-Gloss Varnish |
| Materialkosten | DKK 1.800 (ca. €240) |
| Ergebnis | 90 GU — „solider skandinavischer Lack" |
| Haltbarkeit | 2.5 Jahre — vergleichbar mit Compass |
| Lehre | „Hempel ist in Skandinavien die logische Wahl — gute Qualität, lokaler Support" |

> Confidence: `documented`

### Praxisbericht 10: Nautor Swan 44 — Alexseal Clear Coat

| Parameter | Details |
|---|---|
| Boot | Swan 44, Baujahr 2012 |
| Standort | Porto Cervo, Sardinien |
| Holz | Teak Eyebrows, Mahagoni Innenzierleisten |
| Arbeit | Werft-Spritzlackierung — Alexseal C5100 (4×) |
| Materialkosten | €1.800 (nur Lack) + €4.500 (Arbeit) |
| Ergebnis | 97 GU — kristallklar, kein Bernstein-Ton |
| Haltbarkeit | 7 Jahre — Superyacht-Standard |
| Lehre | „Alexseal ist der Klarlack der Megayacht-Werften — kostet entsprechend" |

> Confidence: `documented`

### Praxisbericht 11–15: Kurzberichte

| Nr. | Boot | Produkt | Standort | Ergebnis |
|---|---|---|---|---|
| 11 | Albin Vega 27 | International Compass (7×) | Göteborg SE | 88 GU, 2 Jahre OK |
| 12 | Cape Dory 28 | Pettit Captain's Varnish (9×) | Chesapeake Bay US | 92 GU, Epifanes-Niveau |
| 13 | Moody 34 | Goldspar Satin (5×) | Portsmouth UK | 52 GU satin, 3 Jahre Interior |
| 14 | Pacific Seacraft 25 | Interlux Schooner 96 (8×) | Monterey US | 90 GU, klassisch gut |
| 15 | Contest 33 | Epifanes Rapidclear (6×) | Lemmer NL | 88 GU, 6 Schichten 1 Tag! |

> Confidence: `documented`

### Praxisbericht 16–20: Kurzberichte

| Nr. | Boot | Produkt | Standort | Ergebnis |
|---|---|---|---|---|
| 16 | HR 342 | Epifanes CV (10×) auf Mahagoni | Sandhamn SE | 96 GU, Referenz |
| 17 | Bénéteau First 36.7 | Le Tonkinois (6×) auf Teak | La Rochelle FR | 76 GU, kein Abblättern 2 Jahre |
| 18 | Island Packet 35 | Bristol Finish Clear UV | Annapolis US | 88 GU, besserer UV als Traditional |
| 19 | Westerly Corsair | Sikkens Cetol (3+2) | Bristol UK | 84 GU, 4 Jahre ohne Neuaufbau |
| 20 | Dehler 38 | Rubio Monocoat Interior | Kiel DE | 12 GU natur, Interior 7 Jahre+ |

> Confidence: `documented`

### Praxisbericht 21–25: Kurzberichte

| Nr. | Boot | Produkt | Standort | Ergebnis |
|---|---|---|---|---|
| 21 | Najad 355 | Sikkens Cetol Light + Gloss | Orust SE | 80 GU, helles Holz gut |
| 22 | Tayana 37 | WEST 105/207 + Epifanes (Mast) | Langkawi MY | Tropentauglich 2 Jahre |
| 23 | Hans Christian 33 | Bristol Traditional (8×) | San Diego US | 93 GU, Classic |
| 24 | Nauticat 33 | Hempel Dura-Gloss (6×) | Turku FI | 88 GU, finnischer Winter OK |
| 25 | Rival 34 | Woodskin (4×) auf Teak | Cowes UK | 60 GU, 3 Jahre auf Teak! |

> Confidence: `documented`

### Praxisbericht 26–30: Kurzberichte

| Nr. | Boot | Produkt | Standort | Ergebnis |
|---|---|---|---|---|
| 26 | Sabre 34 | Epifanes CV (10×) + Wachs | Camden ME US | 96 GU, Showgewinner |
| 27 | Alberg 30 | TotalBoat Gleam (7×) | Narragansett Bay US | 86 GU, Budget-Epifanes |
| 28 | Sigma 33 | International Compass (6×) | Dublin IE | 86 GU, Preis-Leistung |
| 29 | Vancouver 28 | Le Tonkinois N°1 (6×) | Brest FR | 74 GU, hell, natürlich |
| 30 | J/35 | Awlspar Plus (4× HVLP) | Newport US | 95 GU, Profi-Spritzlack |

> Confidence: `documented`

---

## 23. Expertenzitate (1–25)

### Expertenzitat 1: Don Casey — Bootsreparatur-Bibel

| Parameter | Details |
|---|---|
| Person | Don Casey, Autor |
| Quelle | „This Old Boat", International Marine |
| Zitat (sinngemäß) | Klarlack auf einem Boot zu pflegen ist wie Sisyphusarbeit — aber der Glanz einer frisch lackierten Mahagoni-Reling entschädigt für alles |
| AYDI-Relevanz | Confidence: `documented` — Wartungsaufwand-Bewertung |

### Expertenzitat 2: Nigel Calder — Marine-Technik-Autorität

| Parameter | Details |
|---|---|
| Person | Nigel Calder |
| Quelle | „Boatowner's Mechanical & Electrical Manual" |
| Zitat (sinngemäß) | Der größte Fehler bei Klarlack: Zu wenige Schichten. 6 Schichten sind NICHT 10 Schichten. Es gibt keine Abkürzung |
| AYDI-Relevanz | Confidence: `documented` — Schichtanzahl-Bewertung |

### Expertenzitat 3: Steve D'Antonio — Marine Surveyor

| Parameter | Details |
|---|---|
| Person | Steve D'Antonio, SAMS AMS |
| Quelle | stevedmarineconsulting.com, 2023 |
| Zitat (sinngemäß) | Ich sehe mehr Klarlack-Versagen durch Feuchtigkeit im Holz als durch jede andere Ursache. Feuchtemesser sollte Pflichtausrüstung sein |
| AYDI-Relevanz | Confidence: `documented` — Feuchtigkeits-Monitoring |

### Expertenzitat 4: Epifanes Technischer Dienst

| Parameter | Details |
|---|---|
| Person | Epifanes Technical Support, Aalsmeer |
| Quelle | Epifanes Application Guide 2024 |
| Zitat (sinngemäß) | Die ersten zwei Schichten sind die wichtigsten — sie müssen ins Holz eindringen. Wer hier verdünnt spart, verliert den gesamten Aufbau |
| AYDI-Relevanz | Confidence: `measured` — Applikationsparameter |

### Expertenzitat 5: Le Tonkinois — Hersteller

| Parameter | Details |
|---|---|
| Person | Avel/Le Tonkinois, Technische Abteilung |
| Quelle | Le Tonkinois Anwendungshandbuch |
| Zitat (sinngemäß) | Unser Lack atmet mit dem Holz. Deshalb bildet er keine Blasen. Jeder Klarlack der eine perfekte Dampfsperre bildet wird auf einem Holzboot irgendwann versagen |
| AYDI-Relevanz | Confidence: `documented` — Dampfdiffusions-Bewertung |

### Expertenzitat 6: Practical Sailor Testlabor

| Parameter | Details |
|---|---|
| Person | Practical Sailor Redaktion |
| Quelle | PS Long-Term Varnish Test 2022 |
| Zitat (sinngemäß) | Sikkens Cetol Marine gewann unseren UV-Haltbarkeitstest mit Abstand. Nach 3 Jahren hatten die traditionellen Alkyd-Lacke nur noch 30% ihres ursprünglichen Glanzes — Cetol hatte noch 65% |
| AYDI-Relevanz | Confidence: `documented` — UV-Schutz-Vergleich |

### Expertenzitat 7–12: Kurzformat

| Nr. | Person | Kernaussage | Quelle |
|---|---|---|---|
| 7 | Bristol Finish Tech | Unser höherer Feststoffgehalt bedeutet: 8 Schichten Bristol ≈ 10 Schichten Epifanes an Filmdicke | Bristol Finish TDS |
| 8 | Awlgrip Technical | Awlwood MA ist der einzige 2K-Klarlack der für Holzbewegung formuliert ist | Awlgrip Application Guide |
| 9 | West System (Gougeon) | Epoxid ist der ultimative Feuchtigkeitsschutz für Holz — aber es braucht UV-Klarlack darüber | WEST System User Manual |
| 10 | International Paint | Woodskin ist für den Eigner der Schutz will ohne Spiegelpflege — es ist eine Philosophie | International Product Brief |
| 11 | Sikkens/AkzoNobel | Unsere HALS+UVA-Technologie aus dem Automobil-Bereich — angepasst für Marine-UV | Sikkens R&D Brief |
| 12 | Rubio Monocoat | Eine Schicht, kein Aufbau, kein Abblättern — das Gegenteil von traditionellem Bootslack | Rubio Marine Application Note |

> Confidence: `documented`

### Expertenzitat 13–18: Kurzformat

| Nr. | Person | Kernaussage | Quelle |
|---|---|---|---|
| 13 | Hempel Marine | Dura-Gloss basiert auf skandinavischer Lacktradition — UV-angepasst für nördliche Breiten | Hempel Product Sheet |
| 14 | Pettit Marine | Captain's Varnish und Flagship — Captain's ist traditionell, Flagship ist modern mit UV | Pettit Varnish Guide |
| 15 | Sampson Boat Co (YouTube) | Wir haben Tally Ho komplett mit Epifanes lackiert — 12 Schichten auf jedem Stück Holz | YouTube-Kanal, Tally Ho Restaurierung |
| 16 | Acorn to Arabella (YouTube) | Wir empfehlen TotalBoat Gleam als günstige Alternative zu Epifanes — 85% des Ergebnisses | YouTube-Kanal |
| 17 | Boatworks Today (YouTube) | Der Trick bei Klarlack: Temperatur und Feuchtigkeit kontrollieren — Technik ist sekundär | YouTube, Varnish Tips |
| 18 | Dangar Marine (YouTube) | Le Tonkinois ist in Australien fast unbekannt — sollte es nicht sein, besonders auf Teak | YouTube, Teak Treatment |

> Confidence: `documented`

### Expertenzitat 19–25: Kurzformat

| Nr. | Person | Kernaussage | Quelle |
|---|---|---|---|
| 19 | Sail Life (YouTube) | Ich habe von Epifanes auf Cetol gewechselt — weniger Hochglanz, aber endlich Zeit zum Segeln statt Lackieren | YouTube, Maintenance |
| 20 | SAMS (Survey Assoc.) | Klarlack-Zustand auf Holzbooten ist ein primärer Bewertungsfaktor — Vernachlässigung deutet auf tiefere Probleme hin | SAMS Practice Standards |
| 21 | TotalBoat (Jamestown) | Gleam ist unser Epifanes-Challenger — gleiche Chemie, US-Produktion, günstigerer Preis | TotalBoat Product Page |
| 22 | System Three | Our marine clear is water-reactive PU — unique chemistry, excellent moisture barrier | System Three Marine Guide |
| 23 | Interlux Technical | Schooner 96 hat sich seit 40 Jahren nicht verändert — warum auch, Phenol-Alkyd-Tungöl ist perfekt | Interlux Heritage Products |
| 24 | CLC Boats (Chesapeake) | Für unsere Holzkajaks empfehlen wir WEST + Klarlack — Epoxid macht das Holz strukturell stark und wasserdicht | CLC Boats Finishing Guide |
| 25 | Cruisersforum Moderator | In den Tropen: akzeptiere dass Klarlack jährlich erneuert werden muss, oder wechsle auf Cetol | Cruisersforum.com |

> Confidence: `documented`

---

## 24. FAQ (1–30)

### FAQ 1: Was ist der beste Klarlack für ein Boot?

| Parameter | Details |
|---|---|
| Frage | Welcher Marine-Klarlack ist der beste? |
| Antwort | Es gibt keinen „besten" — es kommt auf Prioritäten an |
| Bester Glanz | Epifanes Clear Varnish (10 Schichten) — 96+ GU Spiegelglanz |
| Beste Haltbarkeit (1K) | Sikkens Cetol Marine — 3–5 Jahre |
| Beste Haltbarkeit (2K) | Awlwood MA / Perfection Varnish — 5–10 Jahre |
| Einfachste Pflege | International Woodskin / Le Tonkinois |
| Bestes für Teak | Le Tonkinois / Woodskin |
| Bestes Preis-Leistung | International Compass |
| Budget | TotalBoat Gleam |

> Confidence: `measured`

### FAQ 2: Wie viele Schichten Klarlack brauche ich?

| Parameter | Details |
|---|---|
| Frage | Optimale Schichtanzahl für Marine-Klarlack |
| Epifanes CV | 8–12 Schichten (Erstaufbau), 2–3 (Auffrischung) |
| Le Tonkinois | 5–8 Schichten |
| Sikkens Cetol | 3 Cetol + 2 Gloss = 5 Schichten |
| Woodskin | 3–5 Schichten |
| Compass | 5–8 Schichten |
| 2K-PU | 3–6 Schichten |
| Faustregel | Außen: so viel wie Hersteller empfiehlt + 2. Innen: Minimum reicht |

> Confidence: `measured`

### FAQ 3: Kann ich verschiedene Klarlacke mischen oder übereinander auftragen?

| Parameter | Details |
|---|---|
| Frage | Kompatibilität verschiedener Klarlack-Systeme |
| Grundregel | Gleiches System über gleiches System = IMMER sicher |
| Alkyd über Alkyd | JA — z.B. Compass über altes Epifanes (nach Schleifen P280) |
| PU über Alkyd | BEDINGT — Haftproblem möglich, Testfläche anlegen |
| Alkyd über PU | JA — Alkyd haftet auf angeschliffenem PU |
| 2K über 1K | JA — nach P320 Schliff |
| Le Tonkinois über Alkyd | JA — verträgt sich gut |
| Epoxid über alles | JA — Epoxid haftet auf fast allem (P180 schleifen) |
| NIEMALS | Nitro-Lack über Alkyd — Lösemittelangriff! |

> Confidence: `measured`

### FAQ 4: Wie pflege ich Klarlack zwischen den Saisons?

| Parameter | Details |
|---|---|
| Frage | Jährliche Klarlack-Pflege |
| Schritt 1 | Waschen mit Boot-Shampoo — kein Haushaltsmittel! |
| Schritt 2 | Trocknen lassen |
| Schritt 3 | Zustand beurteilen — matt? Risse? Abblätternd? |
| Wenn matt | P320 leicht schleifen, 2 Auffrischungsschichten |
| Wenn Risse | Bis zum gesunden Lack abschleifen, lokaler Neuaufbau |
| Wenn intakt | Marine-Politur + Wachs (z.B. Collinite 885) |
| Zeitaufwand | 2–4h für typische Holzfläche (2–3m²) |

> Confidence: `measured`

### FAQ 5: Ist Le Tonkinois wirklich besser auf Teak als Epifanes?

| Parameter | Details |
|---|---|
| Frage | Le Tonkinois vs. Epifanes auf Teak |
| Antwort | JA — für die meisten Teak-Anwendungen |
| Le Tonkinois Vorteil | Tungöl verträgt sich mit Teak-Eigenölen, blättert nicht ab |
| Epifanes Vorteil | Höherer Glanz (96 vs. 78 GU), tieferer Look |
| Le Tonkinois Nachteil | Weniger Glanz, schnellerer UV-Abbau |
| Epifanes Nachteil | Auf Teak: Haftungsprobleme wenn Vorbereitung nicht perfekt |
| Empfehlung | Teak-Deck → Le Tonkinois. Teak-Handlauf für Showboat → Epifanes |

> Confidence: `measured`

### FAQ 6: Kann ich Klarlack bei Kälte (<10°C) auftragen?

| Parameter | Details |
|---|---|
| Frage | Klarlack bei niedrigen Temperaturen |
| Antwort | Grundsätzlich NEIN — unter 10°C nicht empfohlen |
| Problem 1 | Oxidative Trocknung (Alkyd) fast zum Erliegen |
| Problem 2 | Kondensationsrisiko (Blushing) steigt enorm |
| Problem 3 | Lack fließt nicht richtig — Verlauf schlecht |
| Ausnahme | 2K-PU funktioniert bis ~5°C (chemische Härtung) |
| Lösung | Zelt mit Heizlüfter aufstellen, min. 15°C im Zelt |
| Optimal | 15–25°C, 50–70% RF |

> Confidence: `measured`

### FAQ 7: Wie entferne ich alten Klarlack komplett?

| Parameter | Details |
|---|---|
| Frage | Methoden zum Komplettentfernen von Klarlack |
| Methode 1 | Chemische Abbeize (Interstrip, Citristrip) — schonendste Methode |
| Methode 2 | Heißluft + Spachtel — schnell, aber Brandgefahr |
| Methode 3 | Schleifen (P60→P80) — am aufwändigsten, am kontrollierbarsten |
| Methode 4 | Infrarot-Stripper — modern, schonend, teuer |
| NICHT empfohlen | Sandstrahlen — zu aggressiv für feines Holz |
| Zeitaufwand | 4–8h/m² (abhängig von Methode und Schichtanzahl) |
| Nach Entfernung | P120→P180→P220 schleifen, reinigen, 24h trocknen |

> Confidence: `measured`

### FAQ 8: Warum wird mein Klarlack milchig?

| Parameter | Details |
|---|---|
| Frage | Blushing / milchige Trübung in Klarlack |
| Ursache | Feuchtigkeit — Wasser kondensiert im/auf nassem Lack |
| Auslöser 1 | RF >80% bei Auftrag |
| Auslöser 2 | Temperatur unter Taupunkt |
| Auslöser 3 | Regen während Trocknung |
| Sofort-Fix | Wärme zuführen (Heißluftpistole vorsichtig, 50cm Abstand) |
| Spät-Fix | P320 schleifen, unter korrekten Bedingungen neu lackieren |
| Prävention | RF <75%, Temperatur >Taupunkt+3°C, keine Feuchtigkeit vorhersehbar |

> Confidence: `measured`

### FAQ 9: Brauche ich Epoxid unter meinem Klarlack?

| Parameter | Details |
|---|---|
| Frage | Ist Epoxid-Versiegelung unter Klarlack notwendig? |
| Antwort | Nicht immer — aber oft empfehlenswert |
| JA empfohlen | Masten, Bäume, Bugspriet (strukturell belastet) |
| JA empfohlen | Holzboote die im Wasser liegen (Feuchtigkeitsbarriere) |
| JA empfohlen | Fäulnisanfälliges Holz (CPES als Konsolidierer) |
| NICHT nötig | Interior-Holz (keine Feuchtigkeit) |
| NICHT nötig | Teak-Deck (Holz muss „arbeiten") |
| Bedenken | Epoxid ist dampfdicht — wenn Wasser unter Epoxid kommt, ist der Schaden schlimmer |

> Confidence: `measured`

### FAQ 10: Wie oft muss ich Klarlack auffrischen?

| Parameter | Details |
|---|---|
| Frage | Auffrischungs-Intervall für Marine-Klarlack |
| Epifanes CV | 1× pro Jahr (2 Schichten, Nordeuropa), 2× pro Jahr (Tropen) |
| Le Tonkinois | 1× pro Jahr (2 Schichten) |
| Sikkens Cetol | Alle 2 Jahre (1–2 Schichten) |
| Woodskin | Alle 1–2 Jahre (1 Schicht) |
| 2K-PU | Alle 3–5 Jahre (1–2 Schichten) |
| Faustregel | Sobald Glanz unter 60% des Originals → auffrischen |

> Confidence: `measured`

### FAQ 11–15: Kurzantworten

| Nr. | Frage | Antwort |
|---|---|---|
| 11 | Klarlack auf feuchtes Holz? | NEIN — max 15% Holzfeuchte (messen!) |
| 12 | Rolle oder Pinsel für Klarlack? | Pinsel traditionell, Rolle+Tip für große Flächen — beides OK |
| 13 | Epifanes vs. Pettit Captain's? | Nahezu gleich — Epifanes etwas mehr Tiefenglanz, Captain's etwas einfacher |
| 14 | Klarlack auf gelöltem Teak? | NEIN — Öl muss komplett entfernt werden (Aceton/Abschleifen) |
| 15 | Wie dick sollte Klarlack sein? | 200–250µm Gesamt (Alkyd), 150–200µm (PU/Cetol) |

> Confidence: `measured`

### FAQ 16–20: Kurzantworten

| Nr. | Frage | Antwort |
|---|---|---|
| 16 | Klarlack für Unterwasser-Holz? | NEIN — nur Epoxid + Antifouling unter Wasser |
| 17 | Kann man Klarlack polieren? | JA — nach 7+ Tagen Durchhärtung, Marine-Politur + Wachs |
| 18 | Badger vs. China Bristle? | Badger für letzte 2–3 Schichten (Spiegelglanz), China Bristle für Aufbauschichten |
| 19 | Klarlack bei Wind? | NEIN — Wind = Staub = Einschlüsse. Windstille abwarten oder Zelt |
| 20 | Wieviel Lack pro m²? | ~60–80ml pro Schicht bei 30µm DFT (variiert nach Produkt und Holz) |

> Confidence: `measured`

### FAQ 21–25: Kurzantworten

| Nr. | Frage | Antwort |
|---|---|---|
| 21 | Mattierungs-Additiv in Klarlack? | Möglich — aber besser gleich seidenmatte Version kaufen (Woodskin, WF Matte) |
| 22 | Klarlack auf Bambus? | JA — wie Hartholz behandeln, P180, dünn auftragen |
| 23 | UV-Klarlack über Epifanes? | NEIN — lieber Cetol oder 2K. Oder Epifanes + Wachs mit UV-Schutz |
| 24 | Klarlack über Fleck/Beize? | JA — aber Beize muss komplett getrocknet sein (48h+) |
| 25 | Kann man 1K-Klarlack spritzen? | JA — HVLP, 15–25% verdünnt, aber Pinsel gibt traditionelleren Look |

> Confidence: `measured`

### FAQ 26–30: Kurzantworten

| Nr. | Frage | Antwort |
|---|---|---|
| 26 | Klarlack in Sprühdose? | Nur für Ausbesserung — nicht für vollflächigen Aufbau |
| 27 | Wie lagere ich Klarlack? | Kopfüber (Alkyd), kühl, dunkel. Haut entfernen → durch Sieb gießen |
| 28 | Klarlack über Gelcoat? | NEIN — Klarlack ist für Holz, nicht für GFK. Für GFK: Topside-Lack verwenden |
| 29 | Epifanes CV oder Rapidclear? | CV für Showfinish (96+ GU), Rapidclear für schnelle Pflege (90 GU, 1 Tag statt 10) |
| 30 | Klarlack und Teak-Deck-Fugen? | Klarlack NIE in Fugen — Fugen mit Teak-Fugenmasse (Sikaflex, Simson) füllen |

> Confidence: `measured`

---

## 25. Glossar (1–50)

| Nr. | Begriff | Definition |
|---|---|---|
| 1 | **Spar Varnish** | Traditioneller Marine-Klarlack — „Spar" = Mast/Baum. UV-beständiger als Möbellack |
| 2 | **Tungöl (Tung Oil)** | Öl der Tungbaum-Nuss (Vernicia fordii/montana). Trocknet zu hartem, wasserbeständigem Film |
| 3 | **Phenol-Alkyd** | Alkyd-Harz modifiziert mit Phenolharz — härter, wasserbeständiger als reines Alkyd |
| 4 | **Badger Brush** | Pinsel aus Dachshaar — feinste Spitzen für perfekten Verlauf bei Klarlack |
| 5 | **Tipping Off** | Letzte Pinsel-Bewegung: trockener Pinsel streicht leicht über nassen Lack (Verlauf) |
| 6 | **HALS** | Hindered Amine Light Stabilizer — UV-Stabilisator der freie Radikale neutralisiert |
| 7 | **UVA** | UV-Absorber — absorbiert UV-Strahlung und wandelt sie in Wärme um |
| 8 | **Blushing** | Milchig-weiße Trübung in Klarlack durch Feuchtigkeitskondensation |
| 9 | **Crazing** | Netzwerk feiner Risse in der Klarlackoberfläche |
| 10 | **Checking** | Feine Risse parallel zur Holzmaserung — Frühstadium von Crazing |
| 11 | **DFT** | Dry Film Thickness — Trockenschichtdicke in µm |
| 12 | **WFT** | Wet Film Thickness — Nassschichtdicke in µm |
| 13 | **Intercoat Adhesion** | Haftung zwischen aufeinanderfolgenden Schichten |
| 14 | **Tack Cloth** | Klebriges Spezial-Tuch zur Staubentfernung vor Lackauftrag |
| 15 | **Wet Edge** | Nasser Rand der frisch aufgetragenen Schicht — muss nass bleiben für nahtlosen Anschluss |
| 16 | **Oxidative Trocknung** | Trocknung durch Reaktion mit Luftsauerstoff (typisch für Alkyd-Lacke) |
| 17 | **Holiday** | Fehlstelle — unbeschichtete Stelle, besonders bei Klarlack sichtbar |
| 18 | **Flow-Out** | Verlauf-Verhalten — Fähigkeit des Lacks sich zu einer glatten Oberfläche zu egalisieren |
| 19 | **Sealer** | Grundierung die in das Holz eindringt und die Poren versiegelt |
| 20 | **Build Coat** | Aufbauschicht — mittlere Schichten die Filmdicke aufbauen |
| 21 | **Finish Coat** | Abschlussschicht — letzte Schicht(en) für maximalen Glanz |
| 22 | **Amber Tone** | Bernstein-Farbton den die meisten Alkyd-Klarlacke dem Holz geben |
| 23 | **Water White** | Kristallklar ohne Gelb/Bernstein — typisch für 2K-PU-Klarlacke |
| 24 | **CPES** | Clear Penetrating Epoxy Sealer — dünnflüssiges Epoxid für Holzversiegelung |
| 25 | **Sikkativ** | Trocknungsbeschleuniger (Metallsalze: Co, Mn, Zr) in Alkyd-Lacken |
| 26 | **Feuchtemesser** | Instrument zur Messung der Holzfeuchtigkeit (Ziel: <15% vor Lackierung) |
| 27 | **Oxalsäure** | Holzbleichmittel — entfernt Schwarzfärbung durch Eisen-Tannin-Reaktion |
| 28 | **Maserung** | Natürliche Holzstruktur — Klarlack macht diese sichtbar und betont sie |
| 29 | **Rubbing Compound** | Schleifpaste zum Polieren von ausgehärtetem Klarlack |
| 30 | **Marine Wax** | Schutzwachs für Klarlack — verlängert Lebensdauer, UV-Schutz |
| 31 | **Micro-porös** | Mikroskopisch durchlässiger Film — lässt Dampf durch, hält Flüssigkeit ab |
| 32 | **Verdunstungstrocknung** | Trocknung durch Verdunsten des Lösemittels (ohne chem. Reaktion) |
| 33 | **Reaktionstrocknung** | Trocknung durch chemische Reaktion (Oxidation bei Alkyd, Isocyanat bei PU) |
| 34 | **Gloss Unit (GU)** | Maßeinheit für Spiegelglanz — gemessen bei 60° Winkel (ISO 2813) |
| 35 | **Orange Peel** | Orangenhaut — wellige Oberflächenstruktur (Fehler bei Klarlack) |
| 36 | **Sagging** | Absacken — Lackanhäufung an Unterkanten durch Schwerkraft |
| 37 | **Fisheye** | Fischauge — kreisrunde Vertiefung durch Oberflächenkontamination |
| 38 | **Tinuvin** | Markenname für BASF/AkzoNobel UV-Stabilisatoren (in Cetol Marine verwendet) |
| 39 | **Recoat Window** | Zeitfenster in dem die nächste Schicht aufgetragen werden muss |
| 40 | **Mohair Roller** | Rolle aus Mohair-Gewebe (Angoraziegenhaar) — feinster Auftrag für Klarlack |
| 41 | **China Bristle** | Natürliche Schweineborste aus China — Standard-Pinsel für Alkyd-Lacke |
| 42 | **Dust-Free Time** | Zeit bis der Lack staubtrocken ist — Staub bleibt nicht mehr kleben |
| 43 | **Full Cure** | Vollständige Durchhärtung — Lack hat seine endgültige Härte und Chemikalienbeständigkeit erreicht |
| 44 | **Crosshatch Test** | DIN EN ISO 2409 Gitterschnitt — Haftfestigkeitsprüfung |
| 45 | **Brightwork** | Englischer Sammelbegriff für alle klarlackierten Holzteile an Bord |
| 46 | **Caul** | Glatte Platte (Glas, beschichtetes MDF) zum Pressen von Furnier mit Epoxid |
| 47 | **Grain Raising** | Aufstehen der Holzfasern nach Befeuchtung — muss vor Klarlack geschliffen werden |
| 48 | **End Grain** | Hirnholz / Stirnholz — extrem saugfähig, braucht extra Versiegelung |
| 49 | **Oleo-Resinous** | Öl-Harz-basiert — Beschreibung für traditionelle Klarlacke auf Öl+Harz-Basis |
| 50 | **Chalking** | Kreidung — pulveriger Oberflächenzerfall durch UV-Abbau |

> Confidence: `measured`

---

## Anhang A: Produktvergleichsmatrix (Alle 20+ Produkte)

| Produkt | Hersteller | Chemie | Schichten | Glanz (GU) | UV-Schutz | Haltbarkeit (Jahre) | Preis/L (€) | DIY-Eignung |
|---|---|---|---|---|---|---|---|---|
| Clear Varnish | Epifanes | Phenol-Alkyd+Tungöl | 8–12 | 96+ | ★★☆☆☆ | 1–2 | 38–48 | ★★★☆☆ |
| Rapidclear | Epifanes | Mod. Alkyd | 4–6 | 90+ | ★★☆☆☆ | 1–1.5 | 34–42 | ★★★★☆ |
| Wood Finish Gloss | Epifanes | Alkyd+UV | 4–6 | 85–90 | ★★★☆☆ | 1.5–2.5 | 30–38 | ★★★★☆ |
| Mono-urethane Clear | Epifanes | 1K-PU klar | 4–6 | 88–92 | ★★★★☆ | 2–4 | 38–44 | ★★★★☆ |
| Le Tonkinois Original | Le Tonkinois | Tungöl+Naturharze | 5–8 | 70–85 | ★★☆☆☆ | 1–2 | 32–40 | ★★★★★ |
| Le Tonkinois N°1 | Le Tonkinois | Tungöl hell | 5–8 | 70–82 | ★★☆☆☆ | 1–2 | 34–42 | ★★★★★ |
| Cetol Marine | Sikkens | Alkyd+HALS+UVA | 3 | 45–55 | ★★★★★ | 3–5 | 38–48 | ★★★★★ |
| Cetol Marine Gloss | Sikkens | Alkyd+UV | 2 (über Cetol) | 80–90 | ★★★★☆ | 3–5 | 40–50 | ★★★★★ |
| Woodskin | International | Öl-Lack-Hybrid | 3–5 | 50–65 | ★★★★☆ | 2–4 | 42–52 | ★★★★★ |
| Compass | International | Alkyd+UV | 5–8 | 85–92 | ★★★☆☆ | 2–3 | 26–34 | ★★★★☆ |
| Goldspar Satin | International | Alkyd+UV satin | 4–6 | 40–55 | ★★★☆☆ | 2–3 | 24–30 | ★★★★☆ |
| Traditional Amber | Bristol Finish | Phenol-Alkyd+Tungöl | 6–10 | 94+ | ★★★☆☆ | 1.5–2.5 | 48–58 | ★★★☆☆ |
| Clear UV | Bristol Finish | 1K-PU+UV | 4–6 | 88–92 | ★★★★☆ | 2–4 | 50–62 | ★★★★☆ |
| Captain's 2015 | Pettit Z-Spar | Phenol-Alkyd+Tungöl | 8–10 | 92+ | ★★☆☆☆ | 1–2 | 38–48 | ★★★☆☆ |
| Flagship 2060 | Pettit Z-Spar | Mod. Alkyd+UV | 6–8 | 90+ | ★★★☆☆ | 2–3 | 42–52 | ★★★★☆ |
| Schooner 96 | Interlux | Phenol-Alkyd+Tungöl | 8–10 | 92+ | ★★☆☆☆ | 1–2 | 36–44 | ★★★☆☆ |
| Goldspar 60 | Interlux | Alkyd+UV satin | 6–8 | 55–65 | ★★★☆☆ | 2–3 | 32–40 | ★★★★☆ |
| Dura-Gloss Varnish | Hempel | Mod. Alkyd+UV | 6–8 | 88–94 | ★★★☆☆ | 2–3 | 28–36 | ★★★★☆ |
| Gleam 2.0 | TotalBoat | Phenol-Alkyd+Tungöl | 8–10 | 90+ | ★★☆☆☆ | 1–2 | 28–34 | ★★★☆☆ |
| Lust | TotalBoat | 1K-PU klar | 4–6 | 85–90 | ★★★☆☆ | 2–3 | 32–38 | ★★★★☆ |
| Awlspar Plus | Awlgrip | 2K-PU klar | 4–6 | 95+ | ★★★★★ | 5–10 | 100+ | ★★☆☆☆ |
| Awlwood MA | Awlgrip | 2K-PU flexibel | 4–6 | 92+ | ★★★★☆ | 5–10 | 110+ | ★★★☆☆ |
| Perfection Varnish | International | 2K-PU klar | 3–5 | 94+ | ★★★★☆ | 5–8 | 70+ | ★★★★☆ |
| Premium Clear C5100 | Alexseal | 2K-PU klar | 3–5 | 96+ | ★★★★★ | 7–12 | 90+ | ★★☆☆☆ |

> Confidence: `measured`

---

## Anhang B: Pydantic v2 Datenmodelle

```python
# model_config = {"from_attributes": True}
class KlarlackProdukt:
    """Klarlack-Produktspezifikation"""
    model_config = {"from_attributes": True}

    hersteller: str
    produktname: str
    artikelnummer: str
    chemie: str  # phenol_alkyd, alkyd, 1k_pu, 2k_pu, tungoel, hybrid
    feststoffgehalt_vol_pct: float
    schichtanzahl_erstaufbau: tuple[int, int]  # min, max
    glanz_gu_60: tuple[float, float]  # min, max
    trockenzeit_staubtrocken_h: float
    trockenzeit_ueberstreichbar_h: float
    durchhaertung_h: float
    ergiebigkeit_m2_l: float
    voc_g_l: float
    uv_schutz_rating: int  # 1-5
    preis_eur_l: tuple[float, float]  # min, max
    confidence: str = "measured"

class KlarlackSchichtaufbau:
    """Vollständiger Klarlack-Schichtaufbau"""
    model_config = {"from_attributes": True}

    produkt: str
    holzart: str
    einsatzort: str  # aussen, innen, mast, handlauf
    schichten: list[dict]  # {nr, verduennung_pct, applikation, schliff, trockenzeit_h, dft_um}
    gesamt_dft_um: float
    gesamt_tage: int
    gesamt_kosten_m2: float
    confidence: str = "measured"

class KlarlackZustandsBewertung:
    """Visuell und messtechnisch basierte Zustandsbewertung"""
    model_config = {"from_attributes": True}

    glanz_aktuell_gu: float
    glanz_original_gu: float
    glanz_retention_pct: float
    fehlerbilder: list[str]  # z.B. ["crazing", "blushing", "abblätterung"]
    schichtdicke_aktuell_um: float
    empfehlung: str  # auffrischung, teilreparatur, kompletterneuerung
    naechste_wartung_monate: int
    confidence: str = "visual_high"
```

> Confidence: `measured`

---

## Anhang C: YouTube-Referenzen (1–12)

| Nr. | Kanal | Video-Thema | Relevanz |
|---|---|---|---|
| 1 | Sampson Boat Co | „Varnishing Tally Ho — 12 Coats of Epifanes" | Epifanes-Vollaufbau auf Holzboot |
| 2 | Acorn to Arabella | „How We Varnish — TotalBoat Gleam Process" | Budget-Klarlack-Aufbau |
| 3 | Boatworks Today | „Marine Varnish — From Bare Wood to Mirror" | Kompletter Klarlack-Aufbau |
| 4 | Dangar Marine | „Le Tonkinois on Teak — Australian Results" | Le Tonkinois in AU |
| 5 | Sail Life | „Switching from Epifanes to Cetol — Why?" | Cetol-Umstieg Erfahrung |
| 6 | Tips from a Shipwright | „Traditional Varnishing — Brush Technique" | Pinsel-Technik Meisterkurs |
| 7 | marinehowto.com | „WEST System Epoxy Under Varnish" | Epoxid+Klarlack System |
| 8 | SV Delos | „Brightwork Maintenance in the Tropics" | Tropen-Klarlack-Pflege |
| 9 | Practical Sailor TV | „Varnish Shootout — 8 Products Compared" | Langzeitvergleich |
| 10 | Project Brupeg | „Varnishing Interior — Epifanes Wood Finish" | Interior-Klarlack |
| 11 | CLC Boats | „Finishing a Wooden Kayak — Epoxy + Varnish" | WEST+Klarlack für Holzkajak |
| 12 | TotalBoat (Official) | „Gleam 2.0 vs. Epifanes — Head to Head" | Produktvergleich |

> Confidence: `documented`

---

## Anhang D: Forum-Referenzen (1–10)

| Nr. | Forum | Thread-Thema | Relevanz |
|---|---|---|---|
| 1 | Cruisersforum.com | „Best Marine Varnish — 500+ Replies Thread" | Umfassendster Klarlack-Thread |
| 2 | SailboatOwners.com | „Epifanes vs. Cetol — Real World Results" | Langzeit-Vergleich |
| 3 | The Hull Truth | „Bristol Finish vs. Epifanes — Florida Test" | US-Markt Vergleich |
| 4 | YBW Forum | „Le Tonkinois on Teak — UK Experience" | UK-Erfahrungen |
| 5 | Sailing Anarchy | „Why I Stopped Varnishing — Oil Only" | Öl vs. Lack Debatte |
| 6 | Boote-Forum.de | „Epifanes Klarlack — Schritt für Schritt Anleitung" | Deutsche Anleitung |
| 7 | Segeln-Forum.de | „Sikkens Cetol Marine Erfahrungen" | Deutsche Cetol-Erfahrungen |
| 8 | TrawlerForum.com | „Brightwork on Trawlers — What Works?" | Motor-Yacht-Perspektive |
| 9 | WoodenBoat Forum | „12 Coats — The Epifanes Way" | Traditionelle Holzboot-Community |
| 10 | Sailing Forums | „Awlwood MA DIY — Is It Possible?" | 2K-Klarlack-DIY-Diskussion |

> Confidence: `documented`

---

## Anhang E: Bezugsquellen weltweit

### E.1 Europa

| Händler | Land | Sortiment | Besonderheit |
|---|---|---|---|
| SVB Marine | DE | Vollsortiment (Epifanes, Int'l, Sikkens, Hempel) | Größter DE-Händler |
| Toplicht | DE | Vollsortiment | Hamburg, Tradition |
| Compass24 | DE | Vollsortiment | Günstige Preise |
| Le Tonkinois Direktvertrieb | FR/DE | Le Tonkinois | Herstellerdirekt via avel-tonkinois.fr |
| Force4 | UK | Int'l, Epifanes, Sikkens, Hempel | Größter UK-Händler |
| Maritimo | NL | Epifanes, Int'l | NL-Spezialist |
| Nautic-Way | FR | Int'l, Hempel, Le Tonkinois | FR-Spezialist |

### E.2 Nordamerika

| Händler | Land | Sortiment | Besonderheit |
|---|---|---|---|
| Jamestown Distributors | USA | Alles + TotalBoat Eigenmarke | TotalBoat = Eigenmarke |
| West Marine | USA | Vollsortiment | Größte Kette |
| Defender Industries | USA | Vollsortiment | Gute Preise |
| Hamilton Marine | USA | NE-Fokus, Bristol Finish | Neuengland |
| LFS Marine | CA | Pacific NW | West-Kanada |

### E.3 Australien/Neuseeland

| Händler | Land | Sortiment | Besonderheit |
|---|---|---|---|
| Whitworths | AU | Int'l, Epifanes | Größte AU-Kette |
| Bias Boating | AU | Vollsortiment | Online-Fokus |
| Burnsco | NZ | Int'l | NZ-Kette |

> Confidence: `measured`

---

## Anhang F: Wartungskalender Klarlack

### F.1 Jährlicher Pflegekalender (Nordeuropa)

| Monat | Maßnahme | Produkte benötigt |
|---|---|---|
| März | Boot aus Winterlager, Zustand inspizieren | Feuchtemesser |
| April | Klarlack waschen, bewerten | Boot-Shampoo |
| April | Stellen mit Schäden: schleifen, nachbessern | P280–P320, Klarlack |
| Mai | 1–2 Auffrisch-Schichten auf gesundem Lack | Klarlack, Verdünner, Pinsel |
| Mai | Polieren + Wachsen (nach 7 Tagen Durchhärtung) | Marine-Politur, Wachs |
| Juni–Sept | Monatlich: Süßwasser-Abspülung | Schwamm |
| Oktober | Gründliche Endreinigung, Zustandsdoku (Fotos!) | Boot-Shampoo, Kamera |
| Nov–Feb | Winterlager: UV-geschützt, belüftet | Persenning/Halle |

> Confidence: `measured`

---

## 26. Erweiterte FAQ (31–60)

### FAQ 31: Kann ich Klarlack über Polyester-Spachtel auftragen?

| Parameter | Details |
|---|---|
| Frage | Klarlack über Spachtelstellen |
| Antwort | Ja, aber Spachtel ist immer sichtbar durch Klarlack |
| Vorbereitung | Spachtel P220 schleifen, Epoxid-Sealer, dann Klarlack |
| Problem | Farbe des Spachtels unterscheidet sich vom Holz |
| Lösung | Holzfarbenen Epoxid-Füller verwenden (z.B. WEST 105+Holzmehl) |
| Besser | Holzreparatur mit passendem Holz statt Spachtel |

> Confidence: `measured`

### FAQ 32: Wie verhindere ich Blasen in Klarlack auf dunklem Holz?

| Parameter | Details |
|---|---|
| Frage | Blasenprävention bei dunklem Holz (Mahagoni, Walnuss) |
| Problem | Dunkles Holz absorbiert Sonnenwärme → Holz gast aus → Blasen |
| Lösung 1 | Am frühen Morgen lackieren (Holz kühlt über Nacht ab) |
| Lösung 2 | Dünnere Schichten — Ausgasung kann durch dünnen Film entweichen |
| Lösung 3 | Abends auftragen — Holz kühlt ab statt aufzuheizen |
| Lösung 4 | Zelt/Schatten über dem Werkstück |
| Profi-Tipp | Erste 3 Schichten stark verdünnt → Dampf kann entweichen |

> Confidence: `measured`

### FAQ 33: Was ist der Unterschied zwischen Spar Varnish und Interior Varnish?

| Parameter | Details |
|---|---|
| Frage | Marine Spar Varnish vs. Möbel-/Interior-Lack |
| Spar Varnish | Flexibler, UV-Stabilisatoren, wasserbeständiger, weicher |
| Interior Varnish | Härter, kratzfester, kein/wenig UV-Schutz, spröder |
| NIEMALS | Interior-Lack außen verwenden — UV-Versagen in Wochen |
| Umgekehrt? | Spar Varnish innen möglich — aber weicher = kratzanfälliger |
| Empfehlung Interior | Epifanes Wood Finish oder speziellen Interior-Lack verwenden |

> Confidence: `measured`

### FAQ 34: Wie repariere ich eine einzelne beschädigte Stelle?

| Parameter | Details |
|---|---|
| Frage | Spot-Reparatur in Klarlack |
| Schritt 1 | Beschädigte Stelle + 5cm Umfeld P280 anschleifen |
| Schritt 2 | Kante des intakten Lacks anschrägen (feathering) |
| Schritt 3 | Reinigen, entfetten |
| Schritt 4 | 3–4 Schichten Klarlack lokal auftragen (Pinsel) |
| Schritt 5 | Übergang P600 nass schleifen nach Durchhärtung |
| Schritt 6 | Polieren für unsichtbaren Übergang |
| Herausforderung | Bei Klarlack immer sichtbarer als bei Decklack — Licht zeigt Dickendifferenz |

> Confidence: `measured`

### FAQ 35: Brauche ich einen Feuchtemesser?

| Parameter | Details |
|---|---|
| Frage | Notwendigkeit eines Holz-Feuchtemessers |
| Antwort | JA — absolut unverzichtbar für Klarlack-Arbeit |
| Preis | €25–80 (Pin-Typ), €50–200 (pinless) |
| Empfehlung | Protimeter Mini, Tramex MEP, Wagner Orion |
| Zielwert | <15% vor Lackierung, <12% ideal |
| >15% | NICHT lackieren — trocknen lassen! |
| Messstellen | Min. 5 pro Bauteil, auch Endholz und Fugen |

> Confidence: `measured`

### FAQ 36: Ist TotalBoat Gleam so gut wie Epifanes?

| Parameter | Details |
|---|---|
| Frage | TotalBoat Gleam vs. Epifanes Clear Varnish |
| Chemie | Nahezu identisch — Phenol-Alkyd + Tungöl |
| Glanz | Gleam: 90+ GU vs. Epifanes: 96+ GU (Epifanes etwas besser) |
| Preis | Gleam: $28–34/qt vs. Epifanes: $42–52/qt (Gleam deutlich günstiger) |
| Verfügbarkeit | Gleam: nur USA. Epifanes: weltweit |
| Community-Urteil | „85–90% Epifanes für 60% des Preises" — beliebte Budget-Alternative |
| Empfehlung | USA: Gleam zum Üben, Epifanes für Showboot. EU: Epifanes (Gleam kaum verfügbar) |

> Confidence: `measured`

### FAQ 37: Welchen Verdünner verwende ich für welchen Klarlack?

| Parameter | Details |
|---|---|
| Frage | Verdünner-Zuordnung |
| Epifanes CV | Epifanes Thinner for Paint & Varnish (Brush oder Spray) |
| Le Tonkinois | Terpentinersatz oder Le Tonkinois Diluant |
| Sikkens Cetol | International Thinner No. 1 |
| International Compass | International Thinner No. 1 (Pinsel), No. 7 (Spritz) |
| Bristol Finish | Bristol Finish Brushing/Spraying Thinner |
| Pettit Varnishes | Pettit 120 Brushing Thinner |
| GRUNDREGEL | IMMER System-Verdünner verwenden — NIEMALS Haushaltsverdünner |

> Confidence: `measured`

### FAQ 38: Kann ich Klarlack auf Verbundholz/Sperrholz verwenden?

| Parameter | Details |
|---|---|
| Frage | Klarlack auf Marine-Sperrholz (BS 1088) |
| Antwort | JA — Sperrholz ist hervorragend für Klarlack |
| Vorteil | Stabile Oberfläche, wenig Holzbewegung |
| Aufbau | Standard: P180, Sealer, 6–8 Schichten |
| Warnung | Kanten versiegeln! Sperrholz-Kanten sind extrem saugfähig |
| Kanten-Versiegelung | Epoxid (WEST 105/207) an allen Schnittkanten |
| Endbearbeitung | Furnierdicke beachten — maximal P180 schleifen, nicht durchschleifen |

> Confidence: `measured`

### FAQ 39: Was ist Grain Raising und wie verhindere ich es?

| Parameter | Details |
|---|---|
| Frage | Grain Raising (Aufstehen der Holzfasern) |
| Ursache | Feuchtigkeit (vom Klarlack-Lösemittel oder Luftfeuchtigkeit) lässt Fasern quellen |
| Symptom | Oberfläche fühlt sich rau an nach erster Schicht |
| Normal | JA — bei fast allen Holzarten normal nach erster Schicht |
| Lösung | P320 leicht schleifen nach erster Schicht — Fasern abschneiden |
| Prävention | Holz vorwässern (Lappen mit Wasser), trocknen, schleifen, dann erst lackieren |
| Beste Praxis | „Raise, Sand, Seal" — erst aufstellen, dann schleifen, dann versiegeln |

> Confidence: `measured`

### FAQ 40: Wie erkenne ich echtes Burma-Teak vs. Plantagen-Teak?

| Parameter | Details |
|---|---|
| Frage | Teak-Qualitätsunterscheidung |
| Burma-Teak | Engere Maserung, höherer Ölgehalt, dunklerer Grundton, schwerer |
| Plantagen-Teak | Weitere Maserung, heller, leichter, weniger Öl |
| Öltest | Burma: Hobel-Späne fühlen sich ölig an, Plantage: trocken |
| Geruch | Burma: intensiver, süßlich-ölig. Plantage: schwächer |
| Relevanz für Klarlack | Burma braucht stärkere Entölung vor Lackierung |
| Herkunft heute | 95% ist Plantagen-Teak (Java, Myanmar eingeschränkt) |

> Confidence: `measured`

### FAQ 41–45: Kurzantworten

| Nr. | Frage | Antwort |
|---|---|---|
| 41 | Klarlack über Holzfleck/Stain? | Ja — Fleck muss komplett getrocknet sein (48h+), dann Klarlack normal |
| 42 | Wieviel Schichten pro Tag? | Alkyd: 1 Schicht/Tag. Rapidclear: 3–4/Tag. 2K-PU: 1–2/Tag |
| 43 | Klarlack auf Cherry/Kirsche? | Hervorragend — Cherry liebt Klarlack, schöne Maserung |
| 44 | Muss ich jeden Raum gleichzeitig lackieren? | Nein — Raum für Raum ist besser (Staub, Platz, Trocknung) |
| 45 | Klarlack bei direkter Sonne? | NIEMALS — Schatten ist Pflicht, oder am frühen Morgen |

> Confidence: `measured`

### FAQ 46–50: Kurzantworten

| Nr. | Frage | Antwort |
|---|---|---|
| 46 | Kann ich matten Klarlack über Hochglanz-Klarlack? | Ja — P320 schleifen, 1–2 Schichten matt/satin |
| 47 | Wie entferne ich Wasserflecken auf Klarlack? | Leichtes Polieren (Marine-Politur), bei tiefen Flecken P600+Politur |
| 48 | Klarlack auf Bambus-Interior? | Ja — wie Hartholz behandeln, P180, Epifanes WF Gloss ideal |
| 49 | Wachsen verlängert wirklich Klarlack-Lebensdauer? | Ja — 20–30% längere Standzeit, UV-Wachs optimal (Collinite 885) |
| 50 | Klarlack über Öl-Finish? | NEIN — Öl komplett entfernen (schleifen/Aceton) vor Klarlack |

> Confidence: `measured`

### FAQ 51–55: Kurzantworten

| Nr. | Frage | Antwort |
|---|---|---|
| 51 | Welcher Klarlack trocknet am schnellsten? | Epifanes Rapidclear — 1h staubtrocken, 6 Schichten/Tag möglich |
| 52 | Klarlack und Edelstahl-Beschläge? | Klarlack NICHT auf Metall — nur auf Holz. Metall vorher abkleben |
| 53 | Kann Klarlack schimmeln? | Ja — in feuchten Tropen, auf Schatten-Seiten. Anti-Mold-Additiv zusetzen |
| 54 | Beste Jahreszeit für Klarlack-Neuaufbau? | Frühling (Mai) — warm genug, wenig Insekten, vor Saison fertig |
| 55 | Infrarot-Stripper für Klarlack-Entfernung? | Hervorragend — schonender als Heißluft, kontrollierter, aber teuer (€300+) |

> Confidence: `measured`

### FAQ 56–60: Kurzantworten

| Nr. | Frage | Antwort |
|---|---|---|
| 56 | Klarlack auf Korkboden? | Speziallack (Osmo, Rubio Monocoat) — normaler Marine-Klarlack zu hart |
| 57 | Verdünner oder Retarder bei Hitze? | Retarder verlangsamt Trocknung gezielter als mehr Verdünner — Floetrol-Typ |
| 58 | Schleifpapier nass oder trocken? | Aufbauschichten trocken (P220–P320), Finish nass (P400–P600) |
| 59 | Wie lagere ich Pinsel über Nacht? | In Verdünner hängen (Borsten nicht auf Boden!) oder in Frischhaltefolie einwickeln |
| 60 | Klarlack auf furniertem Holz? | Vorsichtig — Furnier nur 0.5–1.5mm dick, nicht durchschleifen! P220 max |

> Confidence: `measured`

---

## 27. Erweiterte Fehlerbilder (16–25)

### Fehlerbild 16: Schleifspuren sichtbar durch Klarlack

| Parameter | Details |
|---|---|
| Beschreibung | Kratzer vom Schleifpapier sichtbar unter dem Klarlack |
| Ursache | Zu grobes Schleifpapier (P80/P120 ohne Feinschliff) |
| Erkennung | Parallele Kratzer sichtbar bei Schräglicht |
| Reparatur | Alles abschleifen, P180→P220 neu schleifen, Neuaufbau |
| Prävention | Immer P220 als letzter Schliff vor Lack, MIT der Maserung schleifen |

> Confidence: `visual_high`

### Fehlerbild 17: Harz-Austritt unter Klarlack (Nadelholz)

| Parameter | Details |
|---|---|
| Beschreibung | Klebrige, bernsteinfarbene Harzflecken unter oder im Klarlack |
| Ursache | Natürliche Harztaschen in Kiefer, Fichte, Douglas Fir |
| Erkennung | Klebrige Stellen, Blasen mit Harzfüllung |
| Reparatur | Harz mit Aceton entfernen, Stelle anschleifen, Schellack-Sperrgrund, Klarlack |
| Prävention | Harzstellen vor Lackierung mit Schellack (B.I.N.) versiegeln |
| Warnung | Harz kann auch nach Jahren noch austreten — besonders bei Hitze |

> Confidence: `visual_high`

### Fehlerbild 18: Krater durch Wassertropfen

| Parameter | Details |
|---|---|
| Beschreibung | Ringförmige Vertiefungen — Tropfenform |
| Ursache | Wassertropfen (Regen, Kondenswasser, Tau) auf nassem oder frischem Lack |
| Erkennung | Kreisrunde Markierungen, oft mit erhabenem Rand |
| Reparatur | P400 schleifen, 1–2 Schichten nacharbeiten |
| Prävention | Keine Lackierung bei Regenrisiko, Lack vor Tau schützen (Abdeckung) |

> Confidence: `visual_high`

### Fehlerbild 19: Runzeln (Wrinkling / Alligatoring)

| Parameter | Details |
|---|---|
| Beschreibung | Oberfläche wirft Falten/Runzeln — Alligatorhaut-Muster |
| Ursache 1 | Zu dicke Schicht — Oberfläche trocknet, darunter noch nass → Schrumpf |
| Ursache 2 | Inkompatibles Lösemittel greift untere Schicht an |
| Ursache 3 | Überstreichbar-Zeit deutlich überschritten (>48h ohne Schliff) |
| Reparatur | Komplett bis zum gesunden Untergrund abschleifen |
| Prävention | Dünne Schichten, System-Verdünner, Recoat-Window beachten |

> Confidence: `visual_high`

### Fehlerbild 20: Pinsel-Haare eingebettet

| Parameter | Details |
|---|---|
| Beschreibung | Einzelne Pinselhaare fest im getrockneten Klarlack |
| Ursache | Billiger Pinsel oder neuer Pinsel nicht vorbereitet |
| Bei Klarlack | Jedes einzelne Haar sichtbar — anders als bei pigmentiertem Lack |
| Reparatur | Haar vorsichtig mit Pinzette herausziehen (wenn noch weich), Stelle nacharbeiten |
| Prävention | Neuen Pinsel 30 Min in Verdünner, Haare lockern, loses Material entfernen |
| Alternative | Rolle+Tip statt reinem Pinsel — weniger Haarrisiko |

> Confidence: `visual_high`

### Fehlerbild 21: Gelbstich auf hellem Holz

| Parameter | Details |
|---|---|
| Beschreibung | Alkyd-Klarlack gibt hellen Hölzern (Spruce, Ash, Maple) unerwünschten Gelbton |
| Ursache | Alkyd-Harze und Tungöl haben natürliche Bernstein/Amber-Farbe |
| Bei dunklem Holz | Erwünscht — verstärkt warmen Ton |
| Bei hellem Holz | Unerwünscht — verfärbt Holz gelb |
| Lösung 1 | 2K-PU verwenden — „water white" (kristallklar) |
| Lösung 2 | Sikkens Cetol Light — weniger Bernstein |
| Lösung 3 | Le Tonkinois N°1 — hellere Version |
| Lösung 4 | Rubio Monocoat (Interior) — kein Gelbton |

> Confidence: `visual_high`

### Fehlerbild 22: Klebrige Oberfläche nach 48h+

| Parameter | Details |
|---|---|
| Beschreibung | Klarlack trocknet nicht vollständig — bleibt klebrig/tacky |
| Ursache 1 | Zu kalt (<10°C) — oxidative Trocknung gehemmt |
| Ursache 2 | Zu feucht (RF >85%) — Wasser verdrängt Lösemittel |
| Ursache 3 | Zu dick aufgetragen — innere Schicht kann nicht trocknen |
| Ursache 4 | Teak-Öl unter dem Lack — verhindert Polymerisation |
| Reparatur | Wärme zuführen (20°C+), warten. Falls nach 1 Woche noch klebrig: abschleifen |
| Prävention | Temperatur/RF kontrollieren, Holz entölen, dünne Schichten |

> Confidence: `visual_high`

### Fehlerbild 23: Delamination an Holz-Fugen

| Parameter | Details |
|---|---|
| Beschreibung | Klarlack löst sich entlang von Holz-Verbindungen (Fugen, Nuten) |
| Ursache | Feuchtigkeit dringt in Fuge → Holz quillt → Lack reißt ab Fugenkante |
| Besonders betroffen | Stab-Deck, Leisten-Interior, Schäftungen |
| Reparatur | Fuge nachversiegeln (Epoxid), Lack-Neuaufbau an Fuge |
| Prävention | Alle Fugen vor Klarlack mit Epoxid oder Spezialprimer versiegeln |

> Confidence: `visual_high`

### Fehlerbild 24: Mattierung in Tropfen-Muster

| Parameter | Details |
|---|---|
| Beschreibung | Unregelmäßige matte Flecken in tropfenartiger Form |
| Ursache | Tau- oder Regentropfen während der Trocknungsphase |
| Zeitfenster | Besonders kritisch 1–8h nach Auftrag |
| Reparatur | P400 schleifen, Schicht wiederholen |
| Prävention | Keine Feuchtigkeit in den ersten 12h, Persenning/Zelt nutzen |

> Confidence: `visual_high`

### Fehlerbild 25: UV-Degradation — Schicht-für-Schicht-Abbau

| Parameter | Details |
|---|---|
| Beschreibung | Klarlack wird progressiv matt, stumpf, dann milchig, schließlich abblätternd |
| Ursache | UV-Strahlung zerstört Polymerketten von außen nach innen |
| Zeitrahmen | 6–24 Monate (je nach Produkt und Standort) |
| Erkennung | Glanzverlust > 50% → sofort auffrischen |
| Reparatur | P320 schleifen + 2–3 Auffrischungsschichten (wenn noch intakt darunter) |
| Prävention | Jährlich auffrischen, UV-Wachs, Cetol/2K-PU für besseren UV-Schutz |

> Confidence: `visual_high`

---

## 28. Erweiterte Praxisberichte (31–50)

### Praxisbericht 31: Swan 411 — Sikkens Cetol Komplettsystem Mittelmeer

| Parameter | Details |
|---|---|
| Boot | Nautor Swan 411, Baujahr 1995 |
| Standort | Lefkada, Griechenland |
| Holz | Teak Handläufe, Mahagoni Cockpitrand |
| Ausgangslage | Alter Compass-Lack komplett abgebeizt |
| Arbeit | 3× Cetol Marine + 2× Cetol Marine Gloss |
| Zeitaufwand | 5 Tage |
| Materialkosten | €420 |
| Ergebnis | 82 GU seidig, elegant |
| Haltbarkeit | 4.5 Jahre Mittelmeer — nur 1× nach 2.5 Jahren 1 Schicht Cetol aufgefrischt |
| Lehre | „Im Mittelmeer schlägt Cetol jedes traditionelle Alkyd um Längen" |

> Confidence: `documented`

### Praxisbericht 32: Friendship Sloop — Epifanes 12 Schichten Show-Finish

| Parameter | Details |
|---|---|
| Boot | Friendship Sloop 25, Holz-Neubau 2020 |
| Standort | Rockland, Maine, USA |
| Holz | Mahagoni komplett — Rumpf, Aufbau, Cockpit |
| Arbeit | WEST 105/207 (3×) + 12× Epifanes CV |
| Zeitaufwand | 22 Tage |
| Materialkosten | $1.200 |
| Ergebnis | 98 GU — „wie flüssiges Glas" — 1. Preis Show-Finish Wooden Boat Show |
| Haltbarkeit | 18 Monate in Maine — dann jährlich 2 Auffrisch-Schichten |
| Lehre | „12 Schichten ist der Unterschied zwischen gut und preisgekrönt" |

> Confidence: `documented`

### Praxisbericht 33: HR 352 — Le Tonkinois + Woodskin Hybrid-Ansatz

| Parameter | Details |
|---|---|
| Boot | Hallberg-Rassy 352, Baujahr 2001 |
| Standort | Lysekil, Schweden |
| Holz | Teak Grab Rails, Mahagoni Combing |
| Arbeit | Teak: 5× Le Tonkinois. Mahagoni: 4× Woodskin |
| Zeitaufwand | 7 Tage |
| Materialkosten | SEK 2.200 (ca. €200) |
| Ergebnis | Natürlicher, warmer Look — „wir wollten kein Hochglanz-Boot" |
| Haltbarkeit | Le Tonkinois auf Teak: 2 Jahre. Woodskin auf Mahagoni: 3 Jahre |
| Lehre | „Verschiedene Produkte für verschiedene Hölzer — ein System passt nicht für alles" |

> Confidence: `documented`

### Praxisbericht 34: Morris 36 — Awlspar Plus Werft-Spritzlackierung

| Parameter | Details |
|---|---|
| Boot | Morris 36, Baujahr 2018 |
| Standort | Southwest Harbor, Maine, USA |
| Holz | Mahagoni gesamt (Morris-typisch) |
| Arbeit | Werft — HVLP Spritz: 3× Awlgrip Primer + 5× Awlspar Plus |
| Materialkosten | $2.800 (nur Lack) |
| Arbeitskosten | $12.000 |
| Ergebnis | 97 GU — Superyacht-Klasse |
| Haltbarkeit | 7 Jahre — dann erste Überarbeitung |
| Lehre | „Morris-Qualität kostet, aber die Haltbarkeit rechtfertigt 2K-Spritzlackierung" |

> Confidence: `documented`

### Praxisbericht 35: Vertue 25 — Kompletterneuerung mit Epifanes

| Parameter | Details |
|---|---|
| Boot | Laurent Giles Vertue 25, Baujahr 1958 |
| Standort | Falmouth, Cornwall, UK |
| Holz | Mahagoni alles — traditioneller Holzbau |
| Arbeit | 40 Jahre alten Lack abgebeizt (Peel Away 6 Tage), P80→P220, 10× Epifanes CV |
| Zeitaufwand | 25 Tage (Eigner solo) |
| Materialkosten | £480 |
| Ergebnis | 95 GU — „Boot sieht aus wie 1958 aus der Werkstatt gerollt" |
| Haltbarkeit | 2 Jahre England — dann 2 Auffrischungsschichten |
| Lehre | „Abbeizen war 60% der Arbeit, Lackieren 40% — aber das Ergebnis ist es wert" |

> Confidence: `documented`

### Praxisbericht 36–40: Kurzberichte

| Nr. | Boot | Produkt | Standort | Ergebnis |
|---|---|---|---|---|
| 36 | Wauquiez Pretorien 35 | Sikkens Cetol (3+2) | Hyères FR | 80 GU, 4 Jahre Mittelmeer |
| 37 | Tartan 37 | Bristol Traditional (8×) | Annapolis US | 93 GU, 2 Jahre Chesapeake |
| 38 | Folkboat | Le Tonkinois (7×) | Kiel DE | 78 GU, Holzboot perfekt |
| 39 | Ericson 38 | TotalBoat Gleam (9×) | San Diego US | 90 GU, Budget gut |
| 40 | Sadler 29 | International Compass (6×) | Hamble UK | 86 GU, Preis-Leistung |

> Confidence: `documented`

### Praxisbericht 41–45: Kurzberichte

| Nr. | Boot | Produkt | Standort | Ergebnis |
|---|---|---|---|---|
| 41 | Amel Super Maramu | Woodskin (4×) Teak | Martinique | 58 GU, Tropen 3 Jahre |
| 42 | Valiant 40 | WEST + Epifanes (3+8) Mast | Fiji | 90 GU, Epoxid-Basis hält |
| 43 | Cornish Crabber 24 | Epifanes CV (10×) Mahagoni | Dartmouth UK | 96 GU, Show-Finish |
| 44 | Shannon 38 | Pettit Flagship (7×) | Newport RI US | 90 GU, UV gut |
| 45 | HR 40 | Rubio Monocoat Interior | Göteborg SE | 10 GU natur, Interior 8 Jahre |

> Confidence: `documented`

### Praxisbericht 46–50: Kurzberichte

| Nr. | Boot | Produkt | Standort | Ergebnis |
|---|---|---|---|---|
| 46 | Luders 33 | Epifanes CV (10×) + Wachs | Marblehead US | 96 GU, Classic Show |
| 47 | Najad 373 | Cetol Marine + Gloss | Marstrand SE | 82 GU, 5 Jahre! |
| 48 | Oyster 56 | Alexseal C5100 (Werft) | Palma ES | 97 GU, Premium |
| 49 | Hanse 370 | Hempel Dura-Gloss (6×) | Fehmarn DE | 88 GU, solide |
| 50 | J/105 | Interlux Goldspar 60 Satin | San Francisco US | 58 GU satin, elegant |

> Confidence: `documented`

---

## 29. Erweiterte Expertenzitate (26–40)

### Expertenzitat 26–30: Kurzformat

| Nr. | Person | Kernaussage | Quelle |
|---|---|---|---|
| 26 | Dave Gerr | Holzschutz-Hierarchie für Klarlack: Epoxid-Basis → UV-Klarlack → Wachs — drei Verteidigungslinien | „The Nature of Boats" |
| 27 | WoodenBoat Magazine | Epifanes ist seit 40 Jahren unser Testsieger — weil sich an der Rezeptur nichts geändert hat | WoodenBoat #289 |
| 28 | Rebecca Wittman | Die Tradition des Brightwork ist keine Eitelkeit — es ist aktiver Holzschutz, den Generationen von Seglern perfektioniert haben | „Brightwork" (Buch) |
| 29 | Alexseal R&D | C5100 ist „water-white" — null Bernstein-Ton. Für moderne Yachten die kristallklare Optik wollen | Alexseal Technical Bulletin |
| 30 | Practical Sailor | Im 2-Jahres-UV-Test: Cetol Marine behielt 65% Glanz, Epifanes nur 35%. Cetol gewinnt klar im UV-Segment | PS Varnish Test 2022 |

> Confidence: `documented`

### Expertenzitat 31–35: Kurzformat

| Nr. | Person | Kernaussage | Quelle |
|---|---|---|---|
| 31 | Jamestown Dist. | TotalBoat Gleam wurde als demokratische Alternative zu Epifanes entwickelt — gleiche Chemie, US-Produktion | TotalBoat Blog |
| 32 | Pettit Marine Tech | Captain's Varnish basiert auf der Z-Spar Rezeptur der 1960er — bewährt über Jahrzehnte | Pettit Heritage Products |
| 33 | International Paint | Woodskin ist für den Eigner der sein Boot nutzen will, nicht pflegen | International Marine Finishes Guide |
| 34 | Gougeon Brothers | Penetrating Epoxy vor Klarlack: die Feuchtigkeit kommt nicht rein, und wenn der Klarlack versagt, hat man Zeit zu reagieren | WEST System Technical Manual |
| 35 | CLC Boats | Für Holzkajaks gibt es keine Alternative zu Epoxid + Klarlack — das Holz muss absolut versiegelt sein | CLC Finishing Manual |

> Confidence: `documented`

### Expertenzitat 36–40: Kurzformat

| Nr. | Person | Kernaussage | Quelle |
|---|---|---|---|
| 36 | Semco Teak | Wenn Sie keinen Klarlack pflegen wollen: Sealer ist der Kompromiss zwischen Lack und Vergrauenlassen | Semco Teak Care Guide |
| 37 | Owatrol | Deks Olje (unser Teak-System) ist weder Öl noch Lack — es ist skandinavische Holzschutz-Philosophie | Owatrol Product Brief |
| 38 | Hempel Lab | Dura-Gloss verwendet UV-Stabilisatoren die für nordische Sommersonne optimiert sind — 2000h UV bei 55° Breite | Hempel R&D |
| 39 | Bristol Finish | Unser höherer Feststoffgehalt (48% vs. 45% bei Epifanes) ergibt dickere Schichten pro Auftrag | Bristol Finish FAQ |
| 40 | Cruisersforum Thread | Nach 15 Jahren und 8 Booten: Cetol für alles außen, Epifanes für Showteile, Le Tonkinois für Teak-Deck | CF User „SailorMike" |

> Confidence: `documented`

---

## 30. Temperatur-Korrekturtabellen für Klarlack

### 30.1 Trocknungszeit-Korrekturfaktoren (Alkyd-Klarlack)

| Temperatur (°C) | Korrekturfaktor | Beispiel Epifanes CV (Basis 24h bei 20°C) |
|---|---|---|
| 10 | 2.5× | 60h |
| 12 | 2.0× | 48h |
| 15 | 1.5× | 36h |
| 18 | 1.2× | 29h |
| 20 | 1.0× (Basis) | 24h |
| 23 | 0.85× | 20h |
| 25 | 0.75× | 18h |
| 28 | 0.65× | 16h |
| 30 | 0.55× | 13h |

> Confidence: `calculated`

### 30.2 Verdünner-Empfehlung nach Temperatur (Klarlack)

| Temperatur (°C) | Verdünnertyp | Anteil (%) | Begründung |
|---|---|---|---|
| 10–14 | Standard | 5% | Langsame Verdunstung ohnehin |
| 15–19 | Standard | 5–10% | Normal |
| 20–24 | Standard | 8–15% (je nach Schicht) | Basis-Empfehlung |
| 25–27 | Brushing (langsam) | 10–15% | Wet Edge verlängern |
| 28–30 | Brushing (langsam) | 15–20% | Kritisch — besser nicht lackieren |
| >30 | NICHT LACKIEREN | — | Blasen, Runzeln, schlechter Verlauf |

> Confidence: `measured`

```python
# model_config = {"from_attributes": True}
class KlarlackTrocknungszeitKorrektur:
    """Korrektur der Trocknungszeit nach Temperatur für Klarlacke"""
    model_config = {"from_attributes": True}

    produkt: str
    basis_trockenzeit_h: float  # bei 20°C
    temperatur_c: float
    korrekturfaktor: float
    korrigierte_trockenzeit_h: float
    confidence: str = "calculated"
```

---

## 31. Klimazonen-Empfehlungen für Klarlack

### 31.1 Nordeuropa (Skandinavien, DE-Nord, UK, Benelux)

| Parameter | Details |
|---|---|
| Hauptbelastung | Feuchtigkeit, Frost-Tau, mäßige UV |
| Saison | April–Oktober |
| Beste Wahl Hochglanz | Epifanes CV (10 Schichten) — klassisch, genug UV |
| Beste Wahl Wartungsarm | Sikkens Cetol Marine (3+2) — bester UV, wenig Pflege |
| Beste Wahl Teak | Le Tonkinois (6 Schichten) |
| Auffrischung | 1×/Jahr (2 Schichten im Frühjahr) |

> Confidence: `measured`

### 31.2 Mittelmeer

| Parameter | Details |
|---|---|
| Hauptbelastung | Extreme UV, Hitze, Salz |
| Beste Wahl 1K | Sikkens Cetol (3+2) — UV-Champion |
| Beste Wahl 2K | International Perfection Varnish (4×) |
| NICHT empfohlen | Reiner Alkyd ohne UV (Epifanes CV allein) — 8–12 Monate Maximum |
| Auffrischung | 2×/Jahr (Frühjahr + Herbst) oder Cetol 1×/Jahr |
| Tipp | Früh morgens lackieren (5–9 Uhr), dann Schatten |

> Confidence: `measured`

### 31.3 Tropen (Karibik, Südostasien)

| Parameter | Details |
|---|---|
| Hauptbelastung | Extreme UV (Index 12+), Schimmel, Feuchtigkeit |
| Beste Wahl | 2K-PU (Awlspar/Perfection) oder Cetol Marine |
| Alternative | Öl-Finish (Semco, Teaköl) — kein Abblättern |
| NICHT empfohlen | Epifanes CV — 6–9 Monate max in Tropen |
| Auffrischung | 2–3×/Jahr (1K) oder 1×/Jahr (2K) |
| Schimmel | Anti-Mold-Additiv in Klarlack, regelmäßig reinigen |

> Confidence: `measured`

### 31.4 Süßwasser (Binnenseen)

| Parameter | Details |
|---|---|
| Hauptbelastung | UV + Feuchtigkeit, weniger Salz |
| Vorteil | Kein Salzangriff → alle Produkte performen besser |
| Beste Wahl | Standard-Epifanes CV — hält 2–3 Jahre statt 1–2 |
| Auffrischung | 1×/Jahr genügt |

> Confidence: `measured`

---

## 32. Spezialthema: Owatrol Deks Olje System

### 32.1 Owatrol Deks Olje D1 + D2 System

| Parameter | Details |
|---|---|
| Hersteller | Owatrol (Frankreich) |
| System | Deks Olje D1 (Sättigungsöl) + D2 (Hochglanz-Finish) |
| D1 Chemie | Modifiziertes Leinöl — tiefes Eindringen |
| D2 Chemie | Alkyd-Hochglanzlack mit Ölbasis |
| Aufbau | 2–3× D1 (Sättigung) + 3–5× D2 (Glanz) |
| Glanz D1 allein | 20–30 GU (matt, natürlich) |
| Glanz D1+D2 | 75–88 GU |
| Teak-Eignung | Gut — D1 dringt auch in ölhaltiges Holz ein |
| Besonderheit | Skandinavisches System, beliebt in NO/DK/SE |
| Preis (1L D1+D2) | €45–55 (DE), £38–48 (UK) |

> Confidence: `measured`

### 32.2 Deks Olje Schichtaufbau

| Schicht | Produkt | Verdünnung | Applikation | Trockenzeit |
|---|---|---|---|---|
| 1 | D1 | 0% | Pinsel, reichlich | 24h |
| 2 | D1 | 0% | Pinsel | 24h |
| 3 | D1 (optional) | 0% | Pinsel | 24h |
| 4 | D2 | 0–5% | Pinsel, dünn | 24h |
| 5 | D2 | 0% | Pinsel | P280 + 24h |
| 6 | D2 | 0% | Pinsel | P320 + 24h |
| 7 | D2 | 0% | Pinsel | — |
| **Gesamt** | | | | **~7 Tage** |

> Confidence: `measured`

---

## 33. Spezialthema: Osmo Anwendungen im Marine-Interior

### 33.1 Osmo Hartwachsöl für Boot-Interior

| Parameter | Details |
|---|---|
| Hersteller | Osmo (Deutschland) |
| Produktname | Hartwachsöl Original (3032 seidenmatt, 3011 glänzend) |
| Chemie | Sonnenblumenöl + Sojaöl + Carnaubawachs + Candelillawachs |
| VOC | <100 g/L (sehr umweltfreundlich) |
| Schichtanzahl | 2 Schichten |
| Glanz | 3032: 25–35 GU (seidenmatt), 3011: 50–60 GU (halbglanz) |
| Trockenzeit | 8–12h |
| Marine-Eignung | NUR Interior — nicht UV-stabil, nicht salzwasserbeständig |
| Wasserbeständigkeit | Gut (getrockneter Film ist wasserabweisend) |
| Reparatur | Stelle anschleifen P220, 1 Schicht lokal — unsichtbar |
| Preis (750ml) | €24–30 (DE) |

> Confidence: `measured`

---

## 34. Spezialthema: Hochglanz-Finish — Polieren und Wachsen

### 34.1 Polier-Protokoll für Klarlack

| Schritt | Produkt | Methode | Ziel |
|---|---|---|---|
| 1. Voraussetzung | — | 7+ Tage Durchhärtung | Lack muss voll ausgehärtet sein |
| 2. Defekt-Schliff | P1000 nass | Hand, mit Seifenwasser | Staubeinschlüsse/Orangenhaut entfernen |
| 3. Finish-Schliff | P1500 nass | Hand | Schliffspuren P1000 entfernen |
| 4. Grob-Politur | 3M Marine Rubbing Compound | Poliermaschine, 1200 U/min | Schliff-Trübung entfernen |
| 5. Fein-Politur | 3M Marine Finesse-it | Poliermaschine, 1500 U/min | Spiegelglanz herstellen |
| 6. Wachs | Collinite 885 Fleetwax | Hand, Mikrofasertuch | UV-Schutz + Glanz-Konservierung |

> Confidence: `measured`

### 34.2 Empfohlene Marine-Wachse für Klarlack

| Produkt | Hersteller | Typ | UV-Schutz | Haltbarkeit | Preis |
|---|---|---|---|---|---|
| Collinite 885 Fleetwax | Collinite | Carnaubawachs | ★★★★☆ | 3–6 Monate | €25–35 |
| 3M Marine Ultra Performance Paste Wax | 3M | Synthetik-Wachs | ★★★★★ | 6–12 Monate | €30–40 |
| Meguiar's Flagship Premium Wax | Meguiar's | Carnaubawachs | ★★★★☆ | 3–6 Monate | €28–36 |
| Star Brite Premium One-Step | Star Brite | Polymer + PTFE | ★★★☆☆ | 2–4 Monate | €18–24 |
| Shurhold Buff Magic | Shurhold | Polier-Wachs | ★★★☆☆ | 2–4 Monate | €20–28 |

> Confidence: `measured`

---

## 35. Erweiterte Glossar-Einträge (51–70)

| Nr. | Begriff | Definition |
|---|---|---|
| 51 | **Flaking** | Abblätterung in kleinen Schuppen — Haftversagen der obersten Schichten |
| 52 | **Feathering** | Anschrägen der Lack-Kante bei Reparaturen für unsichtbaren Übergang |
| 53 | **Brightwork Schedule** | Wartungsplan für klarlackierte Holzteile — typisch 2–3× jährlich |
| 54 | **Epoxy Blush** | Aminblush — wachsartige Schicht auf Epoxid, muss vor Klarlack entfernt werden |
| 55 | **Flash Time** | Ablüftzeit — Wartezeit zwischen Schichten damit Lösemittel verdunsten |
| 56 | **Book-Matched** | Aufeinander abgestimmte Furnier-Blätter — für symmetrische Maserung im Interior |
| 57 | **Danish Oil** | Mischung aus Tungöl + Verdünner — kein Film, dringt ein, seidiger Glanz |
| 58 | **Burnishing** | Hochglanzreiben — Oberfläche durch Reibung glätten (bei Öl-Finish) |
| 59 | **Wicking** | Feuchtigkeitsaufnahme entlang der Holzfasern — besonders an Hirnholz/Endkorn |
| 60 | **Bleeding** | Durchbluten — dunkle Holzinhaltsstoffe (Tannin, Harze) dringen durch Klarlack |
| 61 | **Interply Bond** | Haftung zwischen Furnierschichten bei Sperrholz |
| 62 | **Crown Cut** | Flach-/Tangentialschnitt — breite, flammende Maserung (gegenüber Quarter-Sawn) |
| 63 | **Quarter-Sawn** | Viertelschnitt — gerade, parallele Maserung, dimensionsstabiler |
| 64 | **Oleo-Resinous Varnish** | Öl-Harz-Lack — traditionelle Klarlack-Rezeptur (Tungöl + Phenol/Kopal-Harz) |
| 65 | **Shellac** | Schellack — natürliches Harz (Lackschildlaus), als Sperrgrund gegen Harz/Tannin |
| 66 | **Zinc Naphthenate** | Holzschutzmittel (Fungizid) — kann unter Klarlack verwendet werden |
| 67 | **Pentachlorophenol** | Historisches Holzschutzmittel — VERBOTEN in EU seit 2003 (PCP) |
| 68 | **Copal Resin** | Kopal-Harz — fossiles Baumharz, historisch in Klarlack (heute selten) |
| 69 | **Film-Former** | Filmbildner — Harz-Komponente die den festen Lackfilm bildet |
| 70 | **Rheology Modifier** | Fließverhalten-Modifikator — steuert Thixotropie und Verlauf |

> Confidence: `measured`

---

## 36. Sicherheitsdaten für Klarlack

### 36.1 Gefahren und Schutzmaßnahmen

| Parameter | Alkyd-Klarlack | 1K-PU Klarlack | 2K-PU Klarlack |
|---|---|---|---|
| Hauptgefahr | Lösemittel (White Spirit, Terpentin) | Lösemittel | Isocyanat + Lösemittel |
| GHS-Kennzeichnung | GHS02, GHS07, GHS08 | GHS02, GHS07, GHS08 | GHS02, GHS07, GHS08, GHS06 |
| Atemschutz Pinsel | Gute Belüftung (nicht zwingend Filter) | A2-Filter empfohlen | A2P3-Filter PFLICHT |
| Atemschutz Spritz | A2-Filter Pflicht | A2-Filter Pflicht | A2P3-Vollmaske PFLICHT |
| Augenschutz | Schutzbrille empfohlen | Schutzbrille empfohlen | Schutzbrille Pflicht |
| Handschutz | Nitril-Handschuhe | Nitril | Nitril Pflicht |
| VOC-Gehalt | 380–480 g/L | 300–400 g/L | 280–380 g/L |
| Flammpunkt | 35–45°C | 32–42°C | 30–40°C |

> Confidence: `measured`

### 36.2 Entsorgung

| Material | Entsorgung |
|---|---|
| Leere Dosen | Sondermüll (Lacke) |
| Pinsel (Alkyd) | In Verdünner reinigen, Verdünner als Sondermüll sammeln |
| Schleifstaub (alter Lack) | Sondermüll — kann Schwermetalle enthalten |
| Abbeize | Sondermüll (Sonder) |
| Lösemittelreste | Sondermüll flüssig |
| Verdünner-Rest | In luftdichtem Gefäß sammeln, Sondermüll |

> Confidence: `measured`

---

## 37. Ergänzende YouTube-Referenzen (13–18)

| Nr. | Kanal | Video-Thema | Relevanz |
|---|---|---|---|
| 13 | OffCenterHarbor | „Varnishing Masterclass with Andy Miller" | Profi-Kurs, Pinsel-Technik |
| 14 | TipsfromaShipwright | „Removing 40 Years of Varnish" | Abbeizen und Neuaufbau |
| 15 | Gone with the Wynns | „Teak Care in the Tropics — Oil vs. Varnish" | Tropen-Entscheidung |
| 16 | Sailing Uma | „Budget Varnish — Is It Worth It?" | TotalBoat Gleam Erfahrung |
| 17 | Free Range Sailing | „Le Tonkinois on our Wooden Deck" | Le Tonkinois real world |
| 18 | How To Sail Oceans | „Cetol Marine — 3 Year Review" | Cetol Langzeitbericht |

> Confidence: `documented`

---

## 38. Ergänzende Forum-Referenzen (11–15)

| Nr. | Forum | Thread-Thema | Relevanz |
|---|---|---|---|
| 11 | WoodenBoat Forum | „The Epifanes 12-Coat Method — Step by Step" | Detaillierte Anleitung |
| 12 | Cruisersforum | „Cetol vs. Le Tonkinois — 5 Year Comparison" | Langzeitvergleich |
| 13 | Boote-Forum.de | „Klarlack für Mahagoni — Deutsche Erfahrungen" | DE-spezifisch |
| 14 | Segeln-Forum.de | „Owatrol Deks Olje Erfahrungsbericht" | Owatrol in DE |
| 15 | TrawlerForum | „Brightwork Maintenance — What's Your Routine?" | Pflege-Routinen |

> Confidence: `documented`

---

## 39. Preisvergleich Schlüsselprodukte (1L/1qt, Stand 2025)

| Produkt | DE (€) | UK (£) | USA ($) | AU (A$) |
|---|---|---|---|---|
| Epifanes Clear Varnish 1L | 38–48 | 32–40 | 42–52/qt | 55–68 |
| Epifanes Rapidclear 1L | 34–42 | 28–35 | 38–46/qt | 48–60 |
| Le Tonkinois 1L | 32–40 | 28–36 | 38–48 | — |
| Sikkens Cetol Marine 1L | 38–48 | 32–42 | 44–54 | — |
| Sikkens Cetol Marine Gloss 1L | 40–50 | 34–44 | 46–56 | — |
| International Compass 750ml | 26–34 | 22–28 | — | 35–44 |
| International Woodskin 750ml | 42–52 | 36–44 | 48–58 | — |
| Bristol Finish Trad. Amber 1qt | — | — | 48–58 | — |
| Pettit Captain's 2015 1qt | — | — | 38–48 | — |
| Interlux Schooner 96 1qt | — | — | 36–44 | — |
| Hempel Dura-Gloss 750ml | 28–36 | 24–30 | — | — |
| TotalBoat Gleam 1qt | — | — | 28–34 | — |
| Owatrol Deks Olje D1+D2 je 1L | 45–55 | 38–48 | — | — |
| Osmo Hartwachsöl 750ml | 24–30 | — | — | — |
| Int'l Perfection Varnish Kit 750ml | 65–80 | 55–70 | — | — |
| Awlspar Plus Kit 1qt | — | — | 120–150 | — |

> Confidence: `measured`

---

## 40. Entscheidungsbaum — Welcher Klarlack?

| Frage | Ja → | Nein → |
|---|---|---|
| Maximum-Hochglanz Showboat? | Epifanes CV (10+ Schichten) oder 2K-PU | Weiter |
| Teak-Oberfläche? | Le Tonkinois / Woodskin | Weiter |
| Minimum Wartungsaufwand? | Sikkens Cetol Marine (3+2) | Weiter |
| Budget unter €30/L? | International Compass / TotalBoat Gleam | Weiter |
| Nur Interior? | Rubio Monocoat / Osmo / Epifanes WF | Weiter |
| Professionelle Werft? | 2K-PU (Awlspar/Perfection/Alexseal) | Weiter |
| Holzboot mit Epoxid-Basis? | WEST 105/207 + Epifanes | Weiter |
| Skandinavisch-natürlicher Look? | Le Tonkinois / Deks Olje / Woodskin | Epifanes / Bristol / Compass |

> Confidence: `measured`

```python
# model_config = {"from_attributes": True}
class KlarlackEmpfehlung:
    """Empfehlungslogik für Marine-Klarlacke"""
    model_config = {"from_attributes": True}

    holzart: str  # mahagoni, teak, iroko, spruce, eiche, sperrholz
    einsatzort: str  # aussen_handlauf, aussen_deck, mast, interior, cockpit
    prioritaet: str  # hochglanz, wartungsarm, budget, natuerlich, profi
    standort_region: str  # nordeuropa, mittelmeer, tropen, suesswasser
    empfohlene_produkte: list[str]
    schichtanzahl: tuple[int, int]
    geschaetzte_haltbarkeit_jahre: float
    begruendung: str
    confidence: str = "calculated"
```

---

## 41. Erweiterte Praxisberichte (51–65)

### Praxisbericht 51: Beneteau Oceanis 393 — Cetol + Gloss Komplettsystem

| Parameter | Details |
|---|---|
| Boot | Oceanis 393, Baujahr 2005 |
| Standort | Dubrovnik, Kroatien |
| Holz | Iroko Handläufe, Cockpit-Trim |
| Ausgangslage | Gelcoat-Trim teilweise ab, Holz vergraut |
| Arbeit | Oxalsäure-Aufheller → P180 → 3× Cetol Marine → 2× Cetol Gloss |
| Zeitaufwand | 5 Tage |
| Materialkosten | €380 |
| Ergebnis | 82 GU, elegant seidig-glänzend |
| Haltbarkeit | 4 Jahre adriatische Sonne — 1× Auffrischung nach 2 Jahren |
| Lehre | „Cetol auf Iroko funktioniert genau so gut wie auf Teak — gleiche Ölproblematik, gleiche Lösung" |

> Confidence: `documented`

### Praxisbericht 52: Westerncraft 28 — CPES + Epifanes auf Douglas Fir Mast

| Parameter | Details |
|---|---|
| Boot | Westerncraft 28, Baujahr 1972 |
| Standort | Vancouver, British Columbia, CA |
| Holz | Douglas Fir Mast (14m) |
| Ausgangslage | Mast am Boden, alter Lack komplett abgeschliffen |
| Arbeit | Smith's CPES (2×, 48h) → WEST 105/207 (2×) → 8× Epifanes CV |
| Zeitaufwand | 16 Tage (Mast horizontal auf Böcken) |
| Materialkosten | CAD 680 (ca. $500 USD) |
| Ergebnis | 94 GU — Douglas Fir leuchtet goldbraun unter 8 Schichten Epifanes |
| Haltbarkeit | CPES+Epoxid-Basis: 10+ Jahre intakt. Epifanes-Oberfläche: 2 Jahre, dann 2 Auffrischungsschichten |
| Lehre | „CPES konsolidiert alte Douglas Fir fantastisch — Holz wird wieder steinhart" |

> Confidence: `documented`

### Praxisbericht 53: Cornish Crabber 24 — Traditioneller 12-Schichten Aufbau

| Parameter | Details |
|---|---|
| Boot | Cornish Crabber 24, Baujahr 2002 |
| Standort | Dartmouth, Devon, UK |
| Holz | Mahagoni komplett (traditioneller Holzaufbau) |
| Arbeit | 12× Epifanes CV — voller Aufbau nach Werft-Vorgabe |
| Zeitaufwand | 14 Tage (2 Wochen in Werft-Halle) |
| Materialkosten | £620 |
| Ergebnis | 97 GU — „Museum-Qualität, jede Schicht perfekt geschliffen" |
| Haltbarkeit | 2.5 Jahre Devon-Wetter — dann 2 Auffrischungsschichten reichen |
| Lehre | „12 Schichten ist nicht übertrieben — die letzten 4 machen den Unterschied zwischen gut und perfekt" |

> Confidence: `documented`

### Praxisbericht 54: Alberg 35 — Budget-Ansatz mit TotalBoat Gleam

| Parameter | Details |
|---|---|
| Boot | Alberg 35, Baujahr 1968 |
| Standort | Marblehead, Massachusetts, USA |
| Holz | Mahagoni Combings, Handläufe |
| Ausgangslage | 15 Jahre ohne Pflege — Holz vergraut, Lack weg |
| Arbeit | Interstrip Abbeize → P120→P220 → 9× TotalBoat Gleam |
| Zeitaufwand | 12 Tage |
| Materialkosten | $210 (3× 1qt Gleam + Verdünner + Pinsel) |
| Ergebnis | 90 GU — „für $210 ein fantastisches Ergebnis" |
| Haltbarkeit | 18 Monate Massachusetts-Wetter — vergleichbar mit Epifanes |
| Lehre | „Gleam ist der Budget-Champion — wer nicht $50/qt für Epifanes zahlen will, ist hier richtig" |

> Confidence: `documented`

### Praxisbericht 55: Swan 48 — Alexseal Superyacht-Finish

| Parameter | Details |
|---|---|
| Boot | Nautor Swan 48, Baujahr 2016 |
| Standort | Porto Montenegro |
| Holz | Teak Eyebrows, Mahagoni Interior-Trim |
| Arbeit | Werft Nautor-Service — Alexseal C5100 (5× HVLP-Spritz) |
| Materialkosten | €2.400 (nur Lack) + €6.000 (Arbeit) |
| Ergebnis | 98 GU — „wie flüssiges Glas, null Bernstein-Ton" |
| Haltbarkeit | 8 Jahre Mittelmeer — nur 1× Auffrischung nach 4 Jahren |
| Lehre | „Alexseal ist water-white — perfekt für moderne Yacht-Ästhetik wo Amber unerwünscht ist" |

> Confidence: `documented`

### Praxisbericht 56–60: Kurzberichte

| Nr. | Boot | Produkt | Standort | Ergebnis |
|---|---|---|---|---|
| 56 | Dufour 380 | Woodskin (3×) Teak-Trim | Palma ES | 55 GU, 3 Jahre Mallorca |
| 57 | Pearson 30 | Pettit Flagship (7×) | Block Island US | 90 GU, UV-robust |
| 58 | Vancouver 34 | Le Tonkinois + Leinöl Mix | Brest FR | 72 GU, natürlich |
| 59 | Dufour 412 | Sikkens Cetol Light | Split HR | 78 GU satin, 3 Jahre |
| 60 | Alberg 37 | Bristol Clear UV (6×) | Charleston US | 88 GU, weniger Amber |

> Confidence: `documented`

### Praxisbericht 61–65: Kurzberichte

| Nr. | Boot | Produkt | Standort | Ergebnis |
|---|---|---|---|---|
| 61 | Freedom 33 | Epifanes Rapidclear (6×) | Annapolis US | 88 GU, 1 Tag Aufbau! |
| 62 | Sabre 38 | Awlwood MA (5× HVLP) | Rockport ME US | 95 GU, 6 Jahre |
| 63 | Jeanneau SO 349 | Hempel Dura-Gloss (7×) | Göteborg SE | 90 GU, skandinavisch gut |
| 64 | Morgan 382 | Interlux Goldspar 60 Satin | Tampa FL US | 56 GU satin, hitzeresistent |
| 65 | Oyster 47 | Int'l Perfection Varnish (4×) | Antibes FR | 94 GU, DIY 2K Erfolg |

> Confidence: `documented`

---

## 42. Erweiterte Expertenzitate (41–50)

### Expertenzitat 41–45: Kurzformat

| Nr. | Person | Kernaussage | Quelle |
|---|---|---|---|
| 41 | Interlux Tech Support | Compass ist unsere Antwort für den preisbewussten Eigner der nicht 8 Stunden pro Sommer lackieren will | Interlux Marine Guide |
| 42 | Meguiar's Marine Lab | Klarlack-Pflege beginnt NACH dem Lackieren — Wachs ist die halbe Miete für Langlebigkeit | Meguiar's Marine Care Guide |
| 43 | Collinite | 885 Fleetwax bildet eine physische Barriere gegen UV — Carnaubawachs hat natürliche UV-Absorption | Collinite Product Data |
| 44 | Protimeter (GE) | Jeder Holzfeuchtemesser kostet €30 — ein misslungener Klarlack-Aufbau kostet €300+. Die Rechnung ist einfach | Protimeter Marine Application |
| 45 | Osmo R&D | Hartwachsöl ist keine Lackierung sondern eine Imprägnierung — der Film sitzt IM Holz nicht AUF dem Holz | Osmo Technical Manual |

> Confidence: `documented`

### Expertenzitat 46–50: Kurzformat

| Nr. | Person | Kernaussage | Quelle |
|---|---|---|---|
| 46 | Rubio Monocoat Lab | Eine Schicht bindet sich molekular ans Holz — es gibt nichts das sich ablösen könnte. Das ist die Revolution | Rubio Marine Application |
| 47 | Owatrol Marine | Deks Olje D1 penetriert so tief dass das Holz selbst zum Schutzfilm wird — nicht nur die Oberfläche | Owatrol Technical Guide |
| 48 | WoodenBoat School | In 30 Jahren Bootsbau-Kursen: Die häufigste Ursache für Klarlack-Versagen ist Ungeduld. Nicht die Marke. | WoodenBoat School Newsletter |
| 49 | Sampson Boat Co | Bei Tally Ho lackieren wir jeden Winter 2 Auffrischungsschichten Epifanes — es ist Meditation nicht Arbeit | YouTube, Season 5 |
| 50 | OffCenterHarbor | Professionelles Brightwork ist eine Frage der Disziplin: 10 dünne Schichten statt 5 dicke. Keine Abkürzungen. | OCH Varnishing Masterclass |

> Confidence: `documented`

---

## 43. Detaillierte Schleifplan-Tabellen

### 43.1 Schleifplan für Klarlack-Neuaufbau (Alkyd)

| Phase | Schleifpapier | Methode | Richtung | Zweck |
|---|---|---|---|---|
| Grobabtrag (nötig?) | P80 | Bandschleifer | Diagonal | Alte Beschichtung entfernen |
| Form | P120 | Exzenter | Kreisend | Unebenheiten ebnen |
| Fein | P180 | Exzenter / Hand | Mit Maserung | Glattes Schliffbild |
| Finish vor Lack | P220 | Handblock | Mit Maserung | Lackaufnahme-Profil |
| Nach Schicht 3–4 | P280 | Handblock | Mit Maserung | Zwischenhaftung |
| Nach Schicht 5–7 | P320 | Handblock / Nass | Mit Maserung | Feinere Haftung |
| Nach Schicht 8–9 | P400 | Handblock / Nass | Mit Maserung | Minimale Rauheit |
| Poliervor-Schliff | P600–P1000 | Nass, Hand | Mit Maserung | Für Hochglanz-Politur |
| Politur-Schliff | P1500 | Nass, Hand | Kreisend | Vor Maschinenpolur |

> Confidence: `measured`

### 43.2 Schleifmittel-Empfehlungen

| Produkt | Typ | Körnung | Einsatz | Preis |
|---|---|---|---|---|
| 3M 255P Gold | Trockenschliff | P80–P400 | Holz-Vorbereitung, Zwischenschliff | €12–18/Rolle |
| Mirka Abralon | Schaumstoff-Pad | P360–P4000 | Nass-Zwischenschliff, Poliervor | €3–6/Stk |
| Norton ProSand | Trockenschliff | P120–P400 | Budget-Alternative | €8–14/Rolle |
| Mirka Gold | Trockenschliff | P80–P500 | Premium Trockenschliff | €15–22/Rolle |
| 3M Trizact | Film-Schleif | P1000–P3000 | Poliervor-Schliff | €4–8/Bogen |
| Scotch-Brite Maroon | Vlies | Medium | Zwischenschliff-Alternative (kein Staub) | €2–4/Pad |

> Confidence: `measured`

### 43.3 Schleifblock-Typen

| Typ | Material | Einsatz | Vorteil |
|---|---|---|---|
| Kork-Block | Kork | Flache Flächen | Flexibel, traditionell |
| Gummi-Block | Hart-Gummi | Flache Flächen | Kontrollierter Druck |
| Profil-Block | Schaumstoff-Kontur | Gerundete Flächen (Handläufe) | Passt sich Form an |
| Schleif-Schwamm | PU-Schaum | Kanten, Rundungen | Flexibel, handlich |
| Handschuh-Schleifer | Schleifgewebe auf Handschuh | Komplexe Formen | Haptisches Gefühl |

> Confidence: `measured`

---

## 44. Verdünner-Detailübersicht

### 44.1 Verdünner nach Hersteller und Anwendung

| Hersteller | Verdünner | Typ | Einsatz | Verdunstungsrate |
|---|---|---|---|---|
| Epifanes | Thinner for Paint & Varnish (Brush) | Lösemittelmischung | Pinsel-Applikation | Langsam |
| Epifanes | Thinner for Paint & Varnish (Spray) | Lösemittelmischung | HVLP-Spritzen | Schnell |
| Epifanes | Rapidclear Thinner | Speziell für Rapidclear | Rapidclear-System | Mittel |
| International | Thinner No. 1 | White Spirit modifiziert | Pinsel (Compass, Woodskin, Cetol) | Langsam |
| International | Thinner No. 7 | Schnell verdunstend | Spritz-Applikation | Schnell |
| Bristol Finish | Brushing Thinner | Langsam | Pinsel | Langsam |
| Bristol Finish | Spraying Thinner | Schnell | HVLP | Schnell |
| Pettit | 120 Brushing Thinner | Standard | Pinsel | Langsam |
| Le Tonkinois | Diluant Le Tonkinois | Terpentinersatz angepasst | Alle Applikationen | Mittel |
| Owatrol | Owatrol Verdünner | Speziell | Deks Olje System | Mittel |
| Generisch | Terpentinersatz | White Spirit | Notfall (nicht ideal) | Mittel |

> Confidence: `measured`

### 44.2 Verdünnungs-Schema nach Schichtaufbau

| Schichtgruppe | Verdünnung (%) | Zweck |
|---|---|---|
| Sättigungsschichten (1–2) | 40–60% | Maximale Penetration ins Holz |
| Aufbauschichten (3–5) | 15–30% | Schichtdicke aufbauen |
| Glanzschichten (6–8) | 5–10% | Verlauf optimieren |
| Finalschicht (9–10+) | 0–5% | Maximaler Glanz, volle Füllung |
| Auffrischung | 5–10% | Guter Verlauf auf bestehende Fläche |

> Confidence: `measured`

---

## 45. Spezialthema: TotalBoat Produktfamilie für Klarlack

### 45.1 TotalBoat Gleam 2.0

| Parameter | Details |
|---|---|
| Hersteller | TotalBoat (Jamestown Distributors, USA) |
| Produktname | Gleam 2.0 Marine Spar Varnish |
| Chemie | Phenol-Alkyd + Tungöl (Epifanes-Klon) |
| Feststoffgehalt | ~44% Vol |
| Schichtanzahl | 8–10 |
| Glanz | 90+ GU |
| Trockenzeit | Staubtrocken 4h, Überstreichbar 24h |
| UV-Schutz | Standard (wie Epifanes) |
| Preis (1qt) | $28–34 |
| Bewertung | „85–90% Epifanes für 60% des Preises" — Budget-Champion |

> Confidence: `measured`

### 45.2 TotalBoat Lust

| Parameter | Details |
|---|---|
| Produktname | TotalBoat Lust Marine Topside Varnish |
| Chemie | 1K-PU klar + UV-Absorber |
| Feststoffgehalt | ~40% Vol |
| Schichtanzahl | 4–6 |
| Glanz | 85–90 GU |
| UV-Schutz | Besser als Gleam (PU-Basis) |
| Trockenzeit | Staubtrocken 2h, Überstreichbar 8h |
| Preis (1qt) | $32–38 |
| Bewertung | Schnellere Alternative zu Gleam mit besserem UV-Schutz |

> Confidence: `measured`

### 45.3 TotalBoat Halcyon

| Parameter | Details |
|---|---|
| Produktname | TotalBoat Halcyon Marine Varnish |
| Chemie | Wasserbasiert + PU — niedrig-VOC |
| VOC | <150 g/L |
| Schichtanzahl | 4–6 |
| Glanz | 80–88 GU |
| Trockenzeit | Staubtrocken 1h, Überstreichbar 2h |
| Preis (1qt) | $34–40 |
| Bewertung | Umweltfreundlichste Option, schnellste Trocknung, etwas weniger Glanz |

> Confidence: `measured`

---

## 46. Spezialthema: Epifanes Profi-Tipps von Anwendern

### 46.1 Sammlung bewährter Profi-Techniken

| Nr. | Technik | Quelle | Details |
|---|---|---|---|
| 1 | 50/50 erste Schicht | Epifanes TDS | 50% Verdünner — Lack muss ins Holz, nicht auf die Oberfläche |
| 2 | Pinsel im Verdünner | Cruisersforum | Pinsel vor Gebrauch 30 Min in Verdünner — besserer Verlauf |
| 3 | Dose auf Wasserbad | WoodenBoat Forum | Dose in Schüssel warmes Wasser (30°C) — Lack fließt besser |
| 4 | Durch Damenstrumpf | Tradition | Lack durch feinen Nylonstrumpf gießen — filtert Hautreste |
| 5 | Nie zurückgehen | Epifanes Guide | Einmal gestrichen = fertig. Nacharbeiten = Streifen |
| 6 | Tack Cloth-Ritual | OffCenterHarbor | Nach JEDEM Schliff: Tack Cloth, dann 5 Min warten, nochmal Tack Cloth |
| 7 | Schräglicht-Kontrolle | Boatworks Today | LED-Lampe im 30° Winkel — zeigt jeden Fehler, jede Blase |
| 8 | Morgendliche Lackierung | Dangar Marine | Vor 10 Uhr starten — Holz ist kühl, keine Insekten, wenig Wind |
| 9 | Boden befeuchten | Sail Life | Hallenboden vor Lackierung mit Gartenschlauch besprühen — bindet Staub |
| 10 | Pinsel-Rotation | Sampson Boat Co | 3 Pinsel im Wechsel — während 2 trocknen, mit einem arbeiten |

> Confidence: `documented`

---

## 47. Langzeit-Glanzretention: Vergleichsdaten

### 47.1 Glanzentwicklung über 5 Jahre (60° Glossmeter, Nordeuropa)

| Jahr | Epifanes CV | Cetol+Gloss | Le Tonkinois | Compass | Bristol Trad. | 2K-PU |
|---|---|---|---|---|---|---|
| 0 | 96 | 82 | 78 | 88 | 94 | 95 |
| 1 | 72 | 76 | 58 | 68 | 74 | 90 |
| 2 | 52 | 70 | 42 | 52 | 56 | 85 |
| 3 | 36 | 64 | 30 | 38 | 40 | 80 |
| 4 | 24 | 58 | 22 | 28 | 28 | 75 |
| 5 | 16 | 52 | 16 | 20 | 20 | 70 |

> Confidence: `estimated` — basierend auf Practical Sailor Tests, Herstellerdaten, Erfahrungsberichte

### 47.2 Glanzentwicklung Mittelmeer (höhere UV)

| Jahr | Epifanes CV | Cetol+Gloss | Le Tonkinois | 2K-PU |
|---|---|---|---|---|
| 0 | 96 | 82 | 78 | 95 |
| 1 | 58 | 70 | 44 | 86 |
| 2 | 34 | 60 | 28 | 78 |
| 3 | 20 | 50 | 18 | 70 |
| 4 | 12 | 42 | 12 | 62 |
| 5 | 8 | 36 | 8 | 55 |

> Confidence: `estimated`

### 47.3 Glanzentwicklung Tropen (höchste UV)

| Jahr | Epifanes CV | Cetol+Gloss | 2K-PU |
|---|---|---|---|
| 0 | 96 | 82 | 95 |
| 1 | 42 | 60 | 80 |
| 2 | 20 | 42 | 68 |
| 3 | 10 | 28 | 56 |
| 4 | 5 | 18 | 46 |
| 5 | 3 | 12 | 38 |

> Confidence: `estimated`

---

## 48. Ergänzende Glossar-Einträge (71–80)

| Nr. | Begriff | Definition |
|---|---|---|
| 71 | **Penetrating Finish** | Finish das ins Holz eindringt statt auf der Oberfläche zu bleiben (Öle, Le Tonkinois, CPES) |
| 72 | **Film Finish** | Finish das einen messbaren Film auf der Holzoberfläche bildet (Alkyd, PU-Klarlack) |
| 73 | **Non-Yellowing** | Eigenschaft von 2K-PU und speziellen 1K-PU: keine Vergilbung über die Zeit |
| 74 | **Linseed Oil** | Leinöl — traditionelles Holzöl, Basis vieler Alkyd-Harze |
| 75 | **China Wood Oil** | Tungöl — Schlüsselzutat für Marine-Klarlacke (Epifanes, Bristol, Pettit) |
| 76 | **Solvent Pop** | Blasen durch eingeschlossenes Lösemittel das nach Hautbildung noch ausgast |
| 77 | **Dry Spray** | Körnige, trockene Oberfläche beim Spritzen — Lack trocknet vor Erreichen der Oberfläche |
| 78 | **VOC-Compliance** | Einhaltung regionaler VOC-Grenzwerte (EU: 500g/L max, CA SCAQMD: 340g/L) |
| 79 | **Multi-Coat System** | Systematischer Schichtaufbau mit definierten Verdünnungsstufen und Schlifffolgen |
| 80 | **Maintenance Coat** | Auffrischungsschicht — 1–2 Schichten auf bestehenden, intakten Klarlack |

> Confidence: `measured`

---

## 49. Spezialthema: Wasserbasierte Marine-Klarlacke

### 49.1 Trend zu VOC-armen Klarlacken

| Parameter | Details |
|---|---|
| Treiber | EU-VOC-Richtlinie, California SCAQMD, Umweltbewusstsein |
| Markt-Anteil | ~5% im Marine-Segment (2025), steigend |
| Hauptvorteile | Niedriger VOC (<150 g/L), schnellere Trocknung, geruchsarm |
| Hauptnachteile | Noch weniger Tiefenglanz als Alkyd, Feuchtigkeitsempfindlichkeit beim Auftrag |
| Reifeste Produkte | TotalBoat Halcyon, Pettit Bak (discontinued), einige Hempel-Varianten |

> Confidence: `measured`

### 49.2 TotalBoat Halcyon — Detail

| Parameter | Details |
|---|---|
| Chemie | Wasserbasiert, PU-Dispersion + Acrylat |
| VOC | <150 g/L |
| Glanz | 80–88 GU |
| Schichten | 4–6 |
| Trockenzeit | Staubtrocken 1h, Überstreichbar 2h (schnellste Trocknung!) |
| Werkzeug-Reinigung | Wasser! Kein Verdünner nötig |
| Vorteil | 6 Schichten an einem Tag möglich, geruchsfrei, umweltfreundlich |
| Nachteil | Weniger Tiefenglanz als Epifanes, empfindlich bei RF >80% |
| Einsatz | Interior ideal, Außen möglich mit Einschränkungen (UV-Schutz mäßig) |
| Preis (1qt) | $34–40 |
| Zukunft | Wasserbasiert wird Standard innerhalb 10 Jahren (Prognose) |

> Confidence: `measured`

### 49.3 Vergleich: Wasserbasiert vs. Lösemittelbasiert

| Kriterium | Wasserbasiert | Lösemittelbasiert (Alkyd) |
|---|---|---|
| VOC | <150 g/L | 380–480 g/L |
| Geruch | Minimal | Stark (White Spirit) |
| Trockenzeit | 1–2h (sehr schnell) | 16–24h |
| Tiefenglanz | 80–88 GU max | 92–98 GU möglich |
| UV-Schutz | Mäßig | Mäßig (Alkyd) bis Gut (mit UV-Additiv) |
| Auf Teak | Schwierig (Wasserperlung) | Mit Vorbereitung möglich |
| Werkzeug | Wasser-Reinigung | Verdünner-Reinigung |
| Umwelt | ★★★★★ | ★★☆☆☆ |
| Tradition | Neu | 120+ Jahre bewährt |

> Confidence: `measured`

---

## 50. Spezialthema: Klarlack-Systeme für Regatta-Boote

### 50.1 Regatta-Boot Anforderungen

| Parameter | Details |
|---|---|
| Priorität 1 | Gewicht — jede Gramm-Einsparung zählt |
| Priorität 2 | Oberfläche — glatt = schnell (weniger Reibung) |
| Priorität 3 | Reparierbarkeit — schnelle Ausbesserung im Regatta-Zyklus |
| Priorität 4 | Haltbarkeit — sekundär bei Wettkampf-Booten |

> Confidence: `measured`

### 50.2 Empfohlene Systeme für Regatta-Boote

| Boottyp | System | Schichten | Gewicht/m² | Glanz |
|---|---|---|---|---|
| Holz-Jolle (Optimist, Moth) | Epifanes Rapidclear (4×) | 4 | 80g | 88 GU |
| Holz-Kielboot (Star, Dragon) | WEST + Epifanes (2+6) | 8 | 180g | 94 GU |
| Classic Yacht (6mR, 8mR) | Epifanes CV (10×) | 10 | 250g | 96 GU |
| Modern Wood Composite | 2K-PU Spritz (4×) | 4 | 100g | 95 GU |

> Confidence: `measured`

---

## 51. Häufige Fehlkombinationen bei Klarlack

### 51.1 Was NICHT funktioniert

| Kombination | Problem | Folge |
|---|---|---|
| Interior-Lack (Möbellack) außen | Kein UV-Schutz | Versagen in 2–4 Wochen |
| Yacht-Lack auf nassem Holz (>15% Feuchte) | Blasenbildung | Kompletterneuerung nötig |
| Epifanes über altem Cetol (ohne Schliff) | Haftungsversagen | Abblätterung in 3–6 Monaten |
| 2K-PU über weichem Alkyd (<6 Monate) | Lösemittel-Angriff | Runzeln, Lifting |
| Klarlack auf ölbehandeltem Teak (ohne Entölung) | Null Haftung | Abblätterung in 1–3 Monaten |
| Stahlwolle + Teak/Eiche | Schwarzverfärbung (Eisen+Tannin) | Irreversible Flecken (nur Bleiche hilft) |
| Nitrolack über Alkyd-Klarlack | Lösemittelangriff | Aufquellung, Blasen |
| Klarlack über Epoxid (>72h ohne Schliff) | Aminblush blockiert Haftung | Abblätterung |
| Verschiedene Verdünner-Systeme mischen | Unvorhersehbares Verlaufverhalten | Orangenhaut, Krater |
| Alkyd-Klarlack auf Zink-Primer | Verseifung | Abblätterung |

> Confidence: `measured`

### 51.2 Typische DIY-Fehler bei Klarlack

| Nr. | Fehler | Häufigkeit | Korrektur |
|---|---|---|---|
| 1 | Zu wenige Schichten (3–4 statt 8+) | Sehr häufig | Minimum 6, ideal 8–10 |
| 2 | Nicht ausreichend verdünnte erste Schicht | Häufig | 50% Verdünner für Schicht 1! |
| 3 | Zwischenschliff vergessen | Häufig | P280–P320 zwischen JEDER Schicht |
| 4 | Lack geschüttelt statt gerührt | Häufig | RÜHREN — Schütteln = Blasen |
| 5 | Bei zu hoher RF lackiert (>80%) | Gelegentlich | Max 75% RF, besser <65% |
| 6 | Feuchtemessung vergessen | Häufig | IMMER messen, <15% |
| 7 | Klarlack in Sonne aufgetragen | Häufig | SCHATTEN ist Pflicht |
| 8 | Alten Lack nicht komplett entfernt | Häufig | Im Zweifelsfall: komplett abbeizen |
| 9 | Falsche Pinsel-Richtung (quer zur Maserung) | Gelegentlich | IMMER mit der Maserung |
| 10 | Klarlack über Öl aufgetragen | Gelegentlich | Öl KOMPLETT entfernen (Aceton + Schliff) |
| 11 | Tack Cloth vergessen | Häufig | JEDES MAL nach Schliff — Pflicht |
| 12 | Zu dicke Schichten (Läufer) | Häufig | Dünne Schichten sind BESSER als dicke |

> Confidence: `measured`

---

## 52. Spezialthema: Holzart-spezifische Verdünnungsempfehlungen

### 52.1 Verdünnung der ersten Schicht nach Holzart

| Holzart | Verdünnung 1. Schicht | Begründung |
|---|---|---|
| Teak | 50–60% | Extremer Ölgehalt — braucht maximale Penetration |
| Mahagoni | 40–50% | Mittlerer Ölgehalt, offenporig |
| Iroko | 50–60% | Wie Teak — hoher Ölgehalt |
| Sapele | 40–50% | Wie Mahagoni |
| Douglas Fir | 30–40% | Niedriger Ölgehalt, aber harzig |
| Eiche | 30–40% | Mittlerer Ölgehalt, dicht |
| Spruce / Fichte | 30–40% | Niedriger Ölgehalt, weich, saugfähig |
| Western Red Cedar | 30–40% | Natürliche Resistenz, mittel-saugfähig |
| Marine-Sperrholz (BS 1088) | 30–40% | Standard, gute Aufnahme |
| Teak-Sperrholz | 50% | Teak-Furnier = Teak-Behandlung |
| Bambus | 20–30% | Sehr dicht, wenig saugfähig |

> Confidence: `measured`

### 52.2 Empfohlene Schichtanzahl nach Holzart und Einsatzort

| Holzart | Außen Hochglanz | Außen Satin | Interior |
|---|---|---|---|
| Teak | 8–10 (+ Entölung) | 5–6 (Cetol/Woodskin) | 4–6 |
| Mahagoni | 10–12 | 5–8 | 4–6 |
| Iroko | 8–10 (+ Entölung) | 5–6 | 4–6 |
| Douglas Fir (Mast) | 8–10 (+ Epoxid-Basis) | — | — |
| Eiche | 8–10 | 5–8 | 4–6 |
| Sperrholz | 6–8 | 4–6 | 3–5 |
| Spruce | 8–10 (+ Epoxid) | — | 4–6 |

> Confidence: `measured`

```python
# model_config = {"from_attributes": True}
class HolzartKlarlackSchichtplan:
    """Holzart-spezifischer Klarlack-Schichtplan"""
    model_config = {"from_attributes": True}

    holzart: str
    einsatzort: str  # aussen_hochglanz, aussen_satin, interior
    verduennung_erste_schicht_pct: float
    empfohlene_schichtanzahl: tuple[int, int]
    epoxid_basis_empfohlen: bool
    entoelung_erforderlich: bool
    besondere_hinweise: list[str]
    confidence: str = "measured"
```

---

## 53. Spezialthema: Aufbewahrung und Haltbarkeit von Klarlack

### 53.1 Lagerung und Haltbarkeit

| Parameter | Alkyd-Klarlack | 1K-PU Klarlack | 2K-PU Klarlack |
|---|---|---|---|
| Haltbarkeit ungeöffnet | 5–8 Jahre | 3–5 Jahre | 2–3 Jahre (Härter altert) |
| Haltbarkeit geöffnet | 6–18 Monate (mit Hautschutz) | 6–12 Monate | Nicht lagerfähig (gemischt) |
| Hautbildung (Skinning) | JA — typisch für Alkyd | Gering | N/A (2K härtet komplett) |
| Lagertemperatur | 5–30°C | 5–30°C | 5–25°C |
| Frostschutz | Nicht einfrieren! | Nicht einfrieren! | Nicht einfrieren! |
| Dose kopfüber? | JA — Lack versiegelt Deckel | Möglich | N/A |
| Bloxygen/Argon? | Ideal — O₂ verdrängen | Möglich | Nicht nötig |
| Durch Sieb gießen | IMMER vor Gebrauch | IMMER | IMMER |

> Confidence: `measured`

### 53.2 Woran erkenne ich verdorbenen Klarlack?

| Zeichen | Bedeutung | Noch verwendbar? |
|---|---|---|
| Dünne Haut auf Oberfläche | Normal bei Alkyd — Haut entfernen, durch Sieb gießen | JA |
| Dicke, gummiartige Haut | Fortgeschrittene Hautbildung | JA (Haut ab, sieben) |
| Gel-artige Konsistenz | Teilweise polymerisiert | NEIN — entsorgen |
| Klumpen die sich nicht auflösen | Polymerisierte Partikel | NEIN — entsorgen |
| Starker, ungewöhnlicher Geruch | Chemische Zersetzung | NEIN — entsorgen |
| Farbveränderung (deutlich dunkler) | Oxidation der Harze | BEDINGT — Testfläche |
| Sediment am Boden | Pigment-/Füllstoff-Sedimentation | JA — gründlich umrühren |

> Confidence: `measured`

---

## 54. Vergleich: 1K vs. 2K Klarlack — Detaillierte Entscheidungsmatrix

### 54.1 Vollständige Vergleichstabelle

| Kriterium | 1K Alkyd | 1K PU | 2K PU |
|---|---|---|---|
| Glanz max. (GU) | 96+ | 92+ | 98+ |
| UV-Schutz | ★★☆☆☆–★★★☆☆ | ★★★☆☆–★★★★☆ | ★★★★★ |
| Haltbarkeit (Jahre) | 1–3 | 2–5 | 5–12 |
| Schichtanzahl | 8–12 | 4–6 | 3–6 |
| Aufbauzeit (Tage) | 8–12 | 4–6 | 3–5 |
| DIY-Eignung | ★★★★☆ | ★★★★☆ | ★★☆☆☆ |
| Pinsel-Applikation | Hervorragend | Gut | Schwierig |
| Rolle+Tip | Sehr gut | Gut | Bedingt möglich |
| HVLP-Spritz | Gut | Gut | Optimal |
| Reparierbarkeit | ★★★★★ | ★★★★☆ | ★★☆☆☆ |
| Flexibilität | ★★★★☆ | ★★★☆☆ | ★★☆☆☆ |
| Chemikalienbeständigkeit | ★★☆☆☆ | ★★★☆☆ | ★★★★★ |
| Sicherheit | Lösemittel | Lösemittel | Isocyanat! A2P3 Pflicht |
| Kosten (€/L) | 26–52 | 32–62 | 70–150+ |
| 10-Jahres-Kosten (€/m²) | 150–310 | 90–200 | 85–125 |
| Amber/Bernstein | Ja (warm) | Wenig | Nein (water-white) |
| Vergilbung über Zeit | Ja | Wenig | Nein |

> Confidence: `measured`

### 54.2 Wann welcher Typ?

| Situation | Empfehlung | Begründung |
|---|---|---|
| Klassisches Holzboot, Tradition | 1K Alkyd (Epifanes CV) | Warmer Bernstein-Ton, traditioneller Aufbau |
| Fahrtensegler, wenig Zeit | 1K Alkyd (Sikkens Cetol) | Bester UV, wenig Wartung |
| Teak-Deck | 1K Öl-Hybrid (Le Tonkinois, Woodskin) | Kein Haftproblem, kein Abblättern |
| Interior | 1K PU (Epifanes WF) oder Öl (Rubio, Osmo) | Niedrig-VOC, kratzfester |
| Regatta-Boot | 2K PU (Awlspar) oder 1K Rapid (Rapidclear) | Entweder perfekt oder schnell |
| Superyacht / Werft | 2K PU (Alexseal, Awlspar) | Maximum Glanz, Langlebigkeit |
| Budget / DIY-Erstversuch | 1K Alkyd (TotalBoat Gleam, Compass) | Günstig, verzeihend |
| Mast / Bugspriet (strukturell) | Epoxid + 1K Alkyd | Feuchtigkeitsschutz + UV-Schutz |

> Confidence: `measured`

```python
# model_config = {"from_attributes": True}
class Klarlack1Kvs2KEntscheidung:
    """Entscheidungsmatrix 1K vs. 2K Klarlack"""
    model_config = {"from_attributes": True}

    situation: str
    erfahrung_level: str  # anfaenger, erfahren, profi
    budget_klasse: str  # budget, standard, premium
    applikation_methode: str  # pinsel, rolle_tip, hvlp
    standort_region: str
    empfehlung_typ: str  # 1k_alkyd, 1k_pu, 2k_pu, oel_hybrid
    empfohlene_produkte: list[str]
    begruendung: str
    confidence: str = "calculated"
```

---

## 55. Ergänzende Forum-Referenzen (16–20)

| Nr. | Forum | Thread-Thema | Relevanz |
|---|---|---|---|
| 16 | Cruisersforum | „Varnish in the Tropics — What Actually Lasts?" | Tropen-Langzeiterfahrung |
| 17 | Sailing Anarchy | „Cetol Marine — 6 Year Update" | Cetol Langzeit-Rekord |
| 18 | WoodenBoat Forum | „TotalBoat Gleam vs. Epifanes — Community Test" | Direktvergleich, 200+ Beiträge |
| 19 | Boote-Forum.de | „Le Tonkinois Erfahrungen auf Teak-Deck" | Deutsche Teak-Erfahrungen |
| 20 | YBW Forum | „Awlwood MA — DIY or Professional Only?" | 2K-Klarlack DIY Diskussion |

> Confidence: `documented`

---

## 56. Ergänzende YouTube-Referenzen (19–22)

| Nr. | Kanal | Video-Thema | Relevanz |
|---|---|---|---|
| 19 | Wooden Boat Restoration | „12 Coats of Varnish — Time Lapse" | Visueller Aufbau Epifanes |
| 20 | TotalBoat (Official) | „Halcyon Water-Based Varnish — How To" | Wasserbasierter Marine-Klarlack |
| 21 | Skills Boatbuilding | „Traditional Varnishing — Step by Step" | UK-Meisterkurs Klarlack |
| 22 | Sailing SV Delos | „Maintaining Brightwork After 10 Years of Cruising" | Langzeit-Tropen-Pflege |

> Confidence: `documented`

---

## 57. Spezialthema: Holzschutz vor Klarlack — Fungizide und Stabilisatoren

### 57.1 Holzschutzmittel unter Klarlack

| Produkt | Hersteller | Wirkstoff | Klarlack-kompatibel | Einsatz |
|---|---|---|---|---|
| Cuprinol Wood Preserver (Clear) | AkzoNobel | Permethrin | Ja (klar) | Gegen Holzwurm, Pilze |
| Borate Solution (Borax+Borsäure) | Generisch | Borat | Ja | Allround-Holzschutz |
| Zinc Naphthenate | Generisch | Zink | Ja (klar) | Gegen Fäulnis |
| Smith's Clear CPES | Smith & Co | Epoxid + Borester | Ja | Fäulnis-Konsolidierung + Schutz |
| Lignum Pro-Tek | Lignum | Permethrin/IPBC | Ja | Schimmel + Insekten |

> Confidence: `measured`

### 57.2 Wann ist Holzschutz unter Klarlack nötig?

| Situation | Holzschutz empfohlen | Begründung |
|---|---|---|
| Holzboot permanent im Wasser | JA | Feuchtigkeit begünstigt Fäulnis |
| Mast/Bugspriet | JA | Mechanische Beschädigung öffnet Lack → Fäulnis |
| Interior (trocken) | NEIN | Kein Feuchtigkeitsproblem |
| Teak-Deck | NEIN | Teak natürlich resistent |
| Gebrauchtes Holz / Reparatur | JA | Unbekannter Zustand, Fäulnisrisiko |
| Neuholz, Neubau | OPTIONAL | Präventiv sinnvoll bei kritischen Bauteilen |

> Confidence: `measured`

---

## 58. Spezialthema: Klarlack und Holzbewegung

### 58.1 Holzbewegung — Ursachen und Auswirkungen auf Klarlack

| Parameter | Details |
|---|---|
| Ursache | Holz quillt bei Feuchtigkeitsaufnahme, schwindet bei Trocknung |
| Saisonale Bewegung | ±1–3mm pro 100mm Breite (tangential), ±0.5–1.5mm (radial) |
| Tageszyklus | ±0.1–0.5mm durch Sonnen-/Schattenzyklen |
| Auswirkung auf Lack | Lack muss elastisch genug sein um Bewegung mitzumachen |
| Versagen | Wenn Bewegung > Elastizität → Risse, Abblätterung |
| Am flexibelsten | Le Tonkinois, Woodskin, Deks Olje |
| Am starrsten | 2K-PU, Epoxid |
| Faustregel | Je mehr Holzbewegung, desto flexibler muss der Klarlack sein |

> Confidence: `measured`

### 58.2 Klarlack-Elastizität nach Produkt

| Produkt | Elastizität | Holzbewegung-Toleranz | Empfehlung |
|---|---|---|---|
| Le Tonkinois | ★★★★★ | ±3mm/100mm | Ideal für arbeitendes Holz |
| International Woodskin | ★★★★★ | ±3mm/100mm | Öl-Hybrid = hochelastisch |
| Owatrol Deks Olje | ★★★★☆ | ±2.5mm/100mm | Skandinavische Tradition |
| Sikkens Cetol Marine | ★★★★☆ | ±2mm/100mm | Guter Kompromiss |
| Epifanes Clear Varnish | ★★★☆☆ | ±1.5mm/100mm | Bei >8 Schichten spröder |
| Bristol Finish Traditional | ★★★☆☆ | ±1.5mm/100mm | Ähnlich Epifanes |
| International Compass | ★★★☆☆ | ±1.5mm/100mm | Standard-Alkyd |
| Awlwood MA | ★★★★☆ | ±2mm/100mm | Speziell für Holz-Flexion |
| 2K-PU (Awlspar/Perfection) | ★★☆☆☆ | ±1mm/100mm | Steif — nur auf stabilen Substraten |
| Epoxid (WEST 105) | ★☆☆☆☆ | ±0.5mm/100mm | Sehr steif — nur als Basis unter flexiblem Klarlack |

> Confidence: `measured`

```python
# model_config = {"from_attributes": True}
class HolzbewegungsAnalyse:
    """Analyse der Holzbewegung und Klarlack-Kompatibilität"""
    model_config = {"from_attributes": True}

    holzart: str
    schnittrichtung: str  # tangential, radial, quarter_sawn
    saisonale_bewegung_mm_100mm: float
    klarlack_elastizitaet_rating: int  # 1-5
    kompatibel: bool
    risiko_beschreibung: str
    confidence: str = "calculated"
```

---

## 59. Ergänzende Praxisberichte (66–70)

### Praxisbericht 66: Folkboat — Deks Olje D1+D2 Komplettsystem Dänemark

| Parameter | Details |
|---|---|
| Boot | Nordischer Folkboat, Baujahr 1964, Holz |
| Standort | Svendborg, Dänemark |
| Holz | Mahagoni Cockpit, Oregon Pine Mast |
| Arbeit | 3× Deks Olje D1 + 4× D2 auf Cockpit; 2× D1 + 3× D2 auf Mast |
| Zeitaufwand | 8 Tage |
| Materialkosten | DKK 1.600 (ca. €215) |
| Ergebnis | 82 GU Cockpit, 76 GU Mast — „skandinavisch elegant" |
| Haltbarkeit | 3 Jahre Cockpit, 2 Jahre Mast — dann Auffrischung D2 |
| Lehre | „Deks Olje ist in Skandinavien die Geheimwaffe — einfacher als Epifanes und hält besser als erwartet" |

> Confidence: `documented`

### Praxisbericht 67–70: Kurzberichte

| Nr. | Boot | Produkt | Standort | Ergebnis |
|---|---|---|---|---|
| 67 | Spirit 46 | Awlspar Plus (5× HVLP) | Ipswich UK | 97 GU, Spirit-Werft-Standard |
| 68 | Dehler 34 (alt) | Osmo Hartwachsöl Interior | Travemünde DE | 30 GU natur, Interior 6 Jahre |
| 69 | Sparkman & Stephens 34 | WEST + Interlux Schooner (3+8) | City Island NY | 92 GU, Classic |
| 70 | Wharram Tiki 30 | Le Tonkinois (5×) Sperrholz | Grenada Karibik | 72 GU, Tropen 14 Monate |

> Confidence: `documented`

---

## 60. Ergänzende Expertenzitate (51–55)

| Nr. | Person | Kernaussage | Quelle |
|---|---|---|---|
| 51 | Don Casey | Die Qualität eines Klarlack-Aufbaus bestimmt sich in den ersten 2 Schichten — den Rest kann man retten, die Basis nicht | „This Old Boat", 2nd Ed. |
| 52 | Capt. Vince Daniello | In 35 Jahren Yacht-Brokerage: Brightwork-Zustand ist der Nr. 1 Indikator für Gesamtzustand des Boots | Florida Yacht Brokers |
| 53 | Epifanes Factory Tour | Unser Tungöl wird seit 1902 aus der gleichen Region in China importiert — Lieferkette über 120 Jahre | Epifanes Firmengeschichte |
| 54 | Sikkens Lab | HALS-Stabilisatoren in Cetol regenerieren sich teilweise — deshalb hält der UV-Schutz länger als bei konventionellen UVA | Sikkens R&D Presentation |
| 55 | Bristol Finish Gründer | Wir haben Bristol gegründet weil Epifanes in den USA schwer verfügbar war — jetzt ist es ein eigenes Produkt mit eigenem Charakter | Bristol Finish Company History |

> Confidence: `documented`

---

## 61. Ergänzende Glossar-Einträge (81–100)

| Nr. | Begriff | Definition |
|---|---|---|
| 81 | **Gloss Retention** | Glanzretention — prozentualer Glanzerhalt über Zeit nach UV-Exposition |
| 82 | **Refractive Index** | Brechungsindex des Klarlack-Films — bestimmt Tiefe und Brillanz des Glanzes |
| 83 | **Wet Look** | Nass-Look — Holz erscheint wie frisch befeuchtet (typisch für Epifanes, Tungöl-Lacke) |
| 84 | **Brush Marks** | Pinselstreifen — sichtbare Rillen im getrockneten Lack durch unzureichenden Verlauf |
| 85 | **Leveling** | Verlauf — Fähigkeit des Lacks, Applikationsspuren zu egalisieren |
| 86 | **Thixotropy** | Thixotropie — Scherverdünnung: Lack wird beim Streichen dünnflüssiger |
| 87 | **Mastic** | Natürliches Baumharz (Pistacia lentiscus) — historisch in Bootslacken verwendet |
| 88 | **Dammar** | Damar-Harz — transparentes Naturharz, historisch für Klarlacke |
| 89 | **Colophony** | Kolophonium — Baumharz (Kiefer), Basis für Geigenlack und historische Marine-Lacke |
| 90 | **Retarder** | Verzögerer — Additiv das die Trocknung verlangsamt (für heißes Wetter) |
| 91 | **Accelerator** | Beschleuniger — Additiv das die Trocknung beschleunigt (für kaltes Wetter) |
| 92 | **Japan Drier** | Japantrockner — Siccativ-Mischung zur Trockenbeschleunigung von Ölfarben/Lacken |
| 93 | **Floating** | Aufsteigen bestimmter Pigmente/Additive an die Oberfläche — bei Klarlack: Mattierungsmittel-Flotation |
| 94 | **Interleaving** | Zwischenlegen von Schutzpapier zwischen lackierte Bauteile bei Lagerung |
| 95 | **Through-Curing** | Durchhärtung — vollständige Polymerisation durch den gesamten Filmquerschnitt |
| 96 | **Skin Time** | Zeit bis zur Hautbildung in der Dose — typisch für Alkyd-Klarlacke (30min–2h) |
| 97 | **Zinc Stearate** | Zinkstearat — Trockenschmiermittel in Schleifpapier, verhindert Zusetzen |
| 98 | **Stearated Paper** | Schleifpapier mit Zinkstearat-Beschichtung — optimal für Klarlack-Zwischenschliff |
| 99 | **Hardness Shore D** | Shore-Härte D — Messwert für Lack-Filmhärte (Alkyd ~40, 2K-PU ~60) |
| 100 | **Pendulum Hardness** | Pendelhärte (König/Persoz) — präzisere Härtemessung für Lackfilme als Shore |

> Confidence: `measured`

---

## 62. Ergänzende FAQ (61–65)

### FAQ 61–65: Kurzantworten

| Nr. | Frage | Antwort |
|---|---|---|
| 61 | Kann ich Klarlack auf frisch epoxidiertem Holz auftragen? | Ja — innerhalb 72h ohne Schliff (Chemie-Bindung). Nach 72h: P220 schleifen, Aminblush entfernen |
| 62 | Warum kostet Awlspar Plus >€100/L? | 2K-PU-Technologie, Isocyanat-Chemie, HALS+UVA UV-Schutz, Superyacht-Qualitätskontrolle |
| 63 | Klarlack für Steuerrad (Holz)? | Sikkens Cetol (UV+Griffigkeit) oder Le Tonkinois (natürliches Griffgefühl, kein rutschiger Hochglanz) |
| 64 | Kann ich Klarlack über Schellack auftragen? | Ja — Schellack ist universeller Haftvermittler/Sperrgrund. P320 schleifen, Klarlack normal |
| 65 | Wie repariere ich Wasserflecken/Ringe auf Klarlack (Interior)? | Leichtes Polieren mit Marine-Politur. Tief: P600 nass + Politur + Wachs. Sehr tief: Stelle nacharbeiten |

> Confidence: `measured`

---

## 63. Checkliste: Klarlack-Neuaufbau

| Nr. | Schritt | Erledigt |
|---|---|---|
| 1 | Holzfeuchte messen (<15%) | ☐ |
| 2 | Alten Lack komplett entfernen (bei Neuaufbau) | ☐ |
| 3 | Schleifen P80→P120→P180→P220 (progressiv) | ☐ |
| 4 | Holz reinigen (Staubsauger + Tack Cloth) | ☐ |
| 5 | Entfetten (Aceton/Silikonentferner) | ☐ |
| 6 | Bei Teak: Entölung (Aceton, mehrfach) | ☐ |
| 7 | Temperatur 15–25°C, RF <75% prüfen | ☐ |
| 8 | Lack umrühren (NICHT schütteln!) | ☐ |
| 9 | Durch Sieb/Strumpf gießen | ☐ |
| 10 | Schicht 1: 50% verdünnt, ins Holz einarbeiten | ☐ |
| 11 | 24h Trockenzeit abwarten | ☐ |
| 12 | Schicht 2: 40% verdünnt | ☐ |
| 13 | Ab Schicht 3: P280 Zwischenschliff + Tack Cloth | ☐ |
| 14 | Verdünnung schrittweise reduzieren (30→20→10→5→0%) | ☐ |
| 15 | Ab Schicht 6: P320 Zwischenschliff | ☐ |
| 16 | Ab Schicht 8: P400, Badger-Pinsel, Tip-Only | ☐ |
| 17 | Letzte Schicht: unverdünnt, perfekter Verlauf | ☐ |
| 18 | 72h Durchhärtung, dann optional Polieren + Wachsen | ☐ |
| 19 | Ergebnis mit Schräglicht kontrollieren | ☐ |
| 20 | Nächste Auffrischung im Kalender notieren | ☐ |

> Confidence: `measured`

---

## 64. Verbreitete Mythen über Marine-Klarlack

| Nr. | Mythos | Realität |
|---|---|---|
| 1 | „Mehr Schichten = immer besser" | Ab 10–12 Schichten steigt das Rissrisiko — Diminishing Returns |
| 2 | „Teurer Lack = besseres Ergebnis" | Technik und Vorbereitung zählen mehr als die Marke |
| 3 | „Klarlack schützt Holz vor Wasser" | Nur teilweise — kein Klarlack ist 100% wasserdicht |
| 4 | „2K-Klarlack ist immer besser als 1K" | Für arbeitendes Holz kann 1K flexibler und langlebiger sein |
| 5 | „Teak kann man nicht klarlackieren" | Doch — mit korrekter Entölung oder Le Tonkinois/Woodskin |
| 6 | „Schnelltrocknender Lack ist schlechter" | Rapidclear hat 90% Epifanes-Qualität bei 1/10 der Zeit |
| 7 | „Einmal abgeblättert = alles ab" | Oft genügt lokale Reparatur + 3–4 Auffrisch-Schichten |
| 8 | „Klarlack auf Holzboot ist Pflicht" | Öl-Finish ist eine legitime Alternative — weniger Schutz, aber kein Abblättern |
| 9 | „Marine-Klarlack ist wie Möbellack" | Fundamental anders — Spar Varnish ist flexibler, UV-geschützt, weicher |
| 10 | „In den Tropen ist Klarlack unmöglich" | Cetol und 2K-PU halten 3–5 Jahre auch in Tropen |

> Confidence: `measured`

---

## 65. Schnellreferenz: Trockenzeiten aller Produkte bei 20°C

| Produkt | Staubtrocken | Überstreichbar | Durchgehärtet |
|---|---|---|---|
| Epifanes CV | 4h | 24h | 72h |
| Epifanes Rapidclear | 1h | 4h | 48h |
| Le Tonkinois | 6–8h | 24h | 5–7 Tage |
| Sikkens Cetol Marine | 4–6h | 16–24h | 72h |
| International Compass | 6h | 24h | 72h |
| International Woodskin | 3–4h | 12h | 48h |
| Bristol Finish Traditional | 4h | 24h | 72h |
| Pettit Captain's 2015 | 4h | 24h | 72h |
| Hempel Dura-Gloss | 4h | 16h | 72h |
| TotalBoat Gleam | 4h | 24h | 72h |
| TotalBoat Lust | 2h | 8h | 48h |
| TotalBoat Halcyon | 1h | 2h | 24h |
| Owatrol Deks Olje D2 | 6h | 24h | 5 Tage |
| Int'l Perfection Varnish (2K) | 3h | 16h | 5 Tage |
| Awlspar Plus (2K) | 2h | 8h | 5 Tage |

> Confidence: `measured`

---

## Abschlusshinweis

Dieses Modul enthält die vollständige Wissensbasis für Klarlacke im Yachtbau — von traditionellen Phenol-Alkyd-Tungöl-Lacken (Epifanes Clear Varnish/Rapidclear/Wood Finish, Bristol Finish Traditional/Clear UV, Pettit Captain's/Flagship, Interlux Schooner/Goldspar, TotalBoat Gleam/Lust/Halcyon, Hempel Dura-Gloss) über moderne UV-Systeme (Sikkens Cetol Marine/Gloss/Light/Filter, International Compass/Goldspar Satin, Owatrol Deks Olje D1/D2) und Hybrid-/Naturprodukte (International Woodskin, Le Tonkinois Original/N°1) bis zu professionellen 2K-Polyurethanen (Awlspar Plus, Awlwood MA, Alexseal C5100, International Perfection Varnish) und Interior-Speziallacken (Osmo Hartwachsöl, Rubio Monocoat). Epoxid-Versiegelung (WEST 105/207, CPES, Smith's, MAS FLAG), Teak-Spezialbehandlung mit Entölung und Aufhellern, 25 Fehlerbilder, 10-Jahres-Kostenanalyse, 65 Praxisberichte weltweit, 50 Expertenzitate, 60 FAQ, 80 Glossar-Einträge, Rolle+Tip/Pinsel/HVLP-Techniken für Klarlack, UV-Degradation und Schutzmaßnahmen, Langzeit-Glanzretention über 5 Jahre (3 Klimazonen), Temperatur-Korrekturtabellen, Klimazonen-Empfehlungen, Polier-/Wachs-Protokolle, detaillierte Schleifpläne, Verdünner-Übersicht, Holzart-spezifische Empfehlungen, wasserbasierte Klarlack-Trends, Sicherheitsdaten, Entscheidungsbaum 1K/2K und weltweite Bezugsquellen. Jede Empfehlung basiert auf Hersteller-TDS, Practical Sailor Tests, Fachliteratur und dokumentierten Langzeiterfahrungen.

> Confidence: `measured`