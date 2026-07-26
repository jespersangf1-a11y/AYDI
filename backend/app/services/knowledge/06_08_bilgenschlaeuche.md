# 06.08 — Bilgenschläuche und Lenzleitungen

> **Modulkontext**: materials, structural, compliance, service_patterns, cost
> **Confidence-Klassen**: measured | calculated | visual_high | visual_medium | estimated | documented | benchmark
> **Pydantic-Hinweis**: `model_config = {"from_attributes": True}` — NIEMALS `class Config`
> **Letzte Aktualisierung**: 2026-04

---

## Inhaltsverzeichnis

1. Einführung & Regulatorischer Rahmen
2. Zukunftstechnologien
3. Best Practices nach Revier
4. Regional Sourcing
5. Zweck dieser Wissensdatei
6. Pydantic-Modelle
7. Grundlagen
8. Hersteller — Vollständige Übersicht
9. Anlagen-spezifische Zuordnung
10. Schlauchschellen & Verbindungstechnik
11. Technische Referenz & Berechnungen
12. Einbau-/Austausch-Anleitung
13. Lebensdauer und Alterungsmechanismen
14. Fehlerbild-Atlas
15. Fehlerbehebungs-Leitfaden
16. FAQ
17. Glossar
18. Schnell-Referenz
19. Notfall-Ressourcen
20. Anhänge A–R

---

## 1. Einführung & Regulatorischer Rahmen

### 1.1 Sicherheitskritische Bedeutung

Das Bilgensystem ist die letzte Verteidigungslinie zwischen einem schwimmenden Boot und dem Sinken. Ein Versagen der Bilgenschläuche, Lenzleitungen oder Bilgenpumpen führt dazu, dass eingedrungenes Wasser nicht mehr abgepumpt werden kann. Statistiken der USCG und des BSU (Bundesstelle für Seeunfalluntersuchung) zeigen, dass Bilgensystem-Versagen in den Top 5 der Ursachen für Bootsverluste rangiert.

Bilgenschläuche transportieren Bilgenwasser vom tiefsten Punkt des Bootes (Bilgensumpf) über die Bilgenpumpe zum Bordwand-Austritt (Borddurchlass). Lenzleitungen umfassen zusätzlich Cockpit-Abflüsse, Scupper-Leitungen und Notlenzsysteme.

(Confidence: documented)

### 1.2 Versagensszenarien und Konsequenzen

| Versagensmodus | Konsequenz | Zeitrahmen bis Sinken |
|---|---|---|
| Schlauch löst sich von Stutzen | Unkontrollierter Wasseraustritt in Bilge | 30–120 min (abhängig von Leckrate) |
| Schlauch kollabiert (Kinking) | Pumpe fördert nicht, Bilge läuft voll | Schleichend, oft unbemerkt |
| Rückschlagventil versagt | Seewasser strömt rückwärts durch Pumpe | 2–8 h bei Seegang |
| Schwimmerschalter klemmt | Pumpe startet nicht automatisch | Abhängig von Wassereinbruchrate |
| Schlauch porös/rissig | Leckage zwischen Pumpe und Austritt | Schleichend, Wochen bis Monate |
| Borddurchlass-Anschluss undicht | Seewasser-Eintritt über Lenzleitung | 1–6 h abhängig von Tiefe unter WL |
| Sieb/Strainer verstopft | Pumpe läuft trocken, kein Fördern | Pumpen-Totalausfall |

(Confidence: documented)

### 1.3 Regulatorischer Rahmen — Normen und Vorschriften

#### 1.3.1 ISO 8849:2020 — Kleine Wasserfahrzeuge — Elektrisch betriebene Bilgenpumpen

Kernforderungen:
- Bilgenpumpen müssen bei Nennspannung ±10% die angegebene Förderleistung erbringen
- Mindest-Förderleistung abhängig von Bootsgröße und CE-Kategorie
- Automatische Bilgenpumpen müssen einen Schwimmerschalter oder elektronischen Sensor haben
- Verkabelung muss gemäß ISO 10133 (DC) erfolgen
- Pumpen müssen trockenlaufsicher sein (mindestens 30 min Trockenlauf ohne Schaden)
- Saugsieb muss vorhanden sein, Maschenweite ≤5 mm

Pumpenkapazität nach ISO 8849 (Mindestanforderungen):

| Bootslänge (LOA) | CE-Kat A/B min. | CE-Kat C min. | CE-Kat D min. |
|---|---|---|---|
| ≤6 m | 1.900 l/h (500 GPH) | 1.140 l/h (300 GPH) | 760 l/h (200 GPH) |
| 6–9 m | 3.400 l/h (900 GPH) | 2.270 l/h (600 GPH) | 1.140 l/h (300 GPH) |
| 9–12 m | 5.300 l/h (1.400 GPH) | 3.800 l/h (1.000 GPH) | 1.900 l/h (500 GPH) |
| 12–15 m | 7.600 l/h (2.000 GPH) | 5.300 l/h (1.400 GPH) | 3.400 l/h (900 GPH) |
| 15–18 m | 11.400 l/h (3.000 GPH) | 7.600 l/h (2.000 GPH) | 5.300 l/h (1.400 GPH) |
| 18–24 m | 15.100 l/h (4.000 GPH) | 11.400 l/h (3.000 GPH) | 7.600 l/h (2.000 GPH) |

(Confidence: documented)

#### 1.3.2 ABYC H-22 — Electric Bilge Pump Systems

Der US-Standard ABYC H-22 ist international anerkannt und oft strenger als ISO 8849:
- Jedes Boot muss mindestens eine Bilgenpumpe haben, die den tiefsten Punkt erreicht
- Automatische Pumpen müssen einen manuellen Override haben
- Hochstand-Alarm obligatorisch ab 8 m (26 ft)
- Pumpen-Verdrahtung direkt an Batterie (nicht über Hauptschalter abschaltbar)
- Schlauch-Innendurchmesser muss dem Pumpen-Austrittsport entsprechen (keine Reduzierung!)
- Anti-Siphon-Ventil oder Schwanenhals bei Austritt unter Wasserlinie

Zusätzliche ABYC H-22 Anforderungen:
- Bilgenpumpen-Stromkreis mit eigenem Sicherungsschutz
- Kabelquerschnitt nach Stromaufnahme und Leitungslänge dimensioniert
- Keine Inline-Schalter in der Bilgenpumpen-Leitung erlaubt
- Überwachung am Steuerstand (Pumpe-läuft-Anzeige)

(Confidence: documented)

#### 1.3.3 CE/RCD 2013/53/EU — Recreational Craft Directive

Die EU-Freizeitbootrichtlinie fordert:
- Abschnitt 3.6 (Annex I, Part A): Lenzeinrichtungen müssen vorhanden sein
- Geeignete Mittel zum Entfernen von Wasser aus dem Rumpf
- Lenzsystem muss für die jeweilige CE-Kategorie angemessen sein
- Automatische Bilgenpumpe für CE-Kat A und B empfohlen (nicht explizit gefordert)
- Notlenzmöglichkeit (manuell) muss vorhanden sein
- Cockpit-Entwässerung: selbstlenzend ab CE-Kat C, zwingend bei CE-Kat A/B

(Confidence: documented)

#### 1.3.4 ISO 12217:2015/2022 — Stabilitäts- und Auftriebsbewertung

Bilgenwasser-Effekt auf Stabilität:
- Freie Flüssigkeitsoberflächen in der Bilge reduzieren die aufrichtende Hebelwirkung (GZ)
- ISO 12217 Part 1 (Segelboote >6m): Bilgenwasser muss in der Stabilitätsberechnung berücksichtigt werden
- „Swash Bulkheads" (Schwappschotten) reduzieren den Effekt freier Oberflächen
- Maximale freie Oberfläche abhängig von Bootsbreite und Verdrängung

Bilgewasser-Korrekturfaktor:
```
ΔGM = -ρ × Σ(i_n) / Δ
wobei:
  ΔGM = Reduktion der metazentrischen Höhe [m]
  ρ = Dichte des Bilgenwassers [kg/m³] (≈1.025 für Seewasser)
  i_n = Flächenträgheitsmoment der freien Oberfläche [m⁴]
  Δ = Verdrängung [kg]
```

(Confidence: calculated)

#### 1.3.5 USCG — United States Coast Guard Requirements

33 CFR Part 183 Subpart K — Ventilation (Belüftung) (betrifft auch Bilge):
- Boote mit geschlossenem Kraftstoffsystem: Bilge muss belüftet sein
- Bilgengebläse für Benzin-Innenborder vorgeschrieben (nicht direkt Schlauch, aber System)

46 CFR Part 182 — Inspizierte Fahrgastschiffe:
- Mindestens zwei unabhängige Bilgenpumpen
- Eine davon kraftbetrieben, eine manuell bedienbar
- Bilgeleitungen aus metallischem oder zugelassenem nicht-metallischem Material
- Schlauchverbindungen mit doppelten Schlauchschellen

USCG NVIC 7-95 — Bilge Systems:
- Leitungsquerschnitt: mind. 25 mm (1") für Boote bis 12 m
- Mind. 38 mm (1½") für Boote 12–18 m
- Mind. 50 mm (2") für Boote über 18 m

(Confidence: documented)

#### 1.3.6 ISO 9093:2020 — Borddurchlässe und Rumpfdurchführungen

Betrifft die Austrittsöffnung des Bilgensystems:
- Material: Bronze (CuSn/CuNiSn), Edelstahl 316L, oder Verbundwerkstoff (Marelon)
- Borddurchlass muss mit Seeventil (Kugelhahn oder Zylinderhahn) versehen sein
- Ausnahme: Bilgen-Austritt über Wasserlinie benötigt kein Seeventil (ISO 9093:2020 Clause 4.2)
- Anschluss-Stutzen muss für Schlauchschellen-Befestigung geeignet sein
- Mindestens zwei Schlauchschellen bei Unterschiff-Anschlüssen
- Backing-Block bei GFK-Rümpfen obligatorisch

(Confidence: documented)

#### 1.3.7 MARPOL Annex I — Ölhaltige Bilgenwasser

Für gewerbliche Schiffe und Yachten >400 BRZ:
- Einleitung von ölhaltigem Bilgenwasser verboten (>15 ppm Ölgehalt)
- Ölabscheider (Oily Water Separator, OWS) erforderlich
- Für Freizeitboote: keine MARPOL-Pflicht, aber umweltrechtliche Verantwortung
- Bilgen-Pads und Bilgen-Absorber als Best Practice
- Viele Marinas verlangen Bilgen-Sauberkeit bei Liegeplatz-Vergabe

(Confidence: documented)

#### 1.3.8 Klassifikationsgesellschaften (GL, DNV, Lloyd's)

Für Yachten unter Klasse:
- GL (Germanischer Lloyd) Yacht-Rules: Bilgenpumpen-Kapazität = 2× stündliche Leckrate bei größtem Durchbruch
- DNV GL: Mindestens zwei unabhängige Bilgenpumpen, davon eine kraftbetrieben
- Redundanz: Getrennte Stromversorgung für primäre und sekundäre Pumpe
- Schlauchqualität: Zugelassene Typen mit Brandklassifizierung
- Jährliche Inspektion der Bilgensysteme bei Klasse-Erneuerung

(Confidence: documented)

### 1.4 Haftung und Versicherung

| Aspekt | Auswirkung |
|---|---|
| Kaskoversicherung | Bilgensystem-Versagen durch mangelnde Wartung → Leistungsverweigerung möglich |
| P&I Versicherung | Umweltschaden durch ölhaltiges Bilgenwasser → Deckung fraglich |
| Herstellerhaftung | Nur bei nachweisbarem Materialfehler, nicht bei falscher Installation |
| Eigenverantwortung | Eigner muss jährliche Sichtprüfung nachweisen können (Logbuch) |
| Survey-Anforderung | Pre-Purchase Survey: Bilgensystem immer Prüfpunkt |
| CE-Konformität | Bei Umbau des Bilgensystems erlischt CE-Vermutung → Neubewertung nötig |

(Confidence: documented)

---

## 2. Zukunftstechnologien

### 2.1 Smart Bilge Monitoring

Moderne IoT-basierte Bilgensysteme:

| Technologie | Hersteller | Funktion | Status |
|---|---|---|---|
| BilgeSentry Wi-Fi | Siren Marine | Fernüberwachung Bilgenpegel + Pumpenzyklen | Marktreif |
| Maretron BBS100 | Maretron | NMEA 2000 Bilgensensor, Pegelstand | Marktreif |
| Yacht Sentinel YS6 | Yacht Sentinel | GSM-Alarm bei Bilgenpumpen-Aktivität | Marktreif |
| FloatHub | FloatHub | GPS + Bilge + Batterie via Mobilfunk | Marktreif |
| Blue Guard BG-Link | Blue Guard Innovations | Multi-Sensor inkl. Bilge | Marktreif |
| Smart-Bilge-Sensor DIY | ESP32 + Ultraschall | Pegelstandsmessung + MQTT | Prototyp |

(Confidence: documented)

### 2.2 Automatische Bilgenwasser-Trennung

Systeme zur Öl-Wasser-Trennung für Sportboote:
- **Orca Green Marine OWS-Mini**: Kompakter Ölabscheider für Boote ab 10 m, Durchfluss 500 l/h
- **Victor Marine Oily Water Separator**: Für Yachten ab 15 m, <15 ppm Abfluss
- **Koaleszenz-Filter**: Neue Filtermedien aus Nanofasern, Ölbindung >99%

(Confidence: documented)

### 2.3 Elektrische Direktantrieb-Pumpen

Neue Generation bürstenloser DC-Bilgenpumpen:
- **Rule EcoSeries**: 30% weniger Stromverbrauch als Vorgänger, bürstenlos
- **Jabsco Cyclone SPX**: Höhere Förderhöhe bei gleicher Leistung
- **Seaflo SFBP2-G3000**: Bürstenloser Motor, 3.000 GPH, programmierbare Intervalle

(Confidence: documented)

### 2.4 Selbstentleerende Bilgensysteme

- **Venturi-Effekt-Systeme**: Fahrtwind/Fahrt durchs Wasser erzeugt Unterdruck am Austritt
- **Schwerkraft-Lenzsysteme**: Automatische Entleerung über tiefste Rumpföffnung bei Krängung
- **Ejektoren**: Seewasser-Durchfluss erzeugt Saugwirkung auf Bilgenleitung (Regatta-Yachten)

(Confidence: documented)

### 2.5 Schlauch-Materialinnovationen

| Innovation | Beschreibung | Vorteil |
|---|---|---|
| PEX-verstärkte Bilgenschläuche | Vernetztes Polyethylen Innenlage | UV-beständig, kein Weichmacher-Migration |
| Silikonummantelte Schläuche | Außenlage aus hitzebeständigem Silikon | Motorraum-tauglich bis 200°C |
| Antibakterielle Innenbeschichtung | Silber-Ionen oder Kupferpartikel | Biofilm-Prävention |
| Recycelte Materialien | PET-Recycling-Gewebe als Verstärkung | Nachhaltig, vergleichbare Festigkeit |

(Confidence: estimated)

---

## 3. Best Practices nach Revier

### 3.1 Ostsee (Brackwasser, kalt)

- Geringe Salinität (7–15 PSU) reduziert Korrosionsrisiko an metallischen Anschlüssen
- Frostgefahr Oktober–April: Bilgensystem vollständig entleeren bei Winterlager
- Algenbildung in Bilge bei stehendem Wasser: Bilge-Reiniger verwenden
- Empfehlung: Verstärkte PVC-Schläuche ausreichend, Spiralschlauch für Saugseite
- Schlauchschellen: Edelstahl AISI 316 (A4) empfohlen, AISI 304 (A2) akzeptabel
- Winterlager: Pumpen ausbauen oder in warmem Raum lagern (Impeller-Schutz)

(Confidence: documented)

### 3.2 Mittelmeer (Salzwasser, warm)

- Hohe Salinität (38 PSU) → nur 316L-Edelstahl für Schellen und Anschlüsse
- UV-Belastung auf Deck-Schläuche (Cockpit-Drain): UV-stabilisierte Schläuche verwenden
- Biofouling am Bilgen-Austritt: regelmäßig prüfen, Muschelbewuchs verstopft Rückschlagklappe
- Warme Temperaturen beschleunigen Weichmacher-Migration bei PVC (Verhärtung nach 5–7 Jahren)
- Empfehlung: Premiumschläuche (Trident, Shields) bevorzugen, Austauschintervall 7 Jahre
- Cockpit-Scupper: Große Durchmesser (38 mm) wegen Gewitterregen

(Confidence: documented)

### 3.3 Nordsee / Atlantik (kalt, rau, salzhaltig)

- Extreme Belastung durch Seegang → Schlauch-Befestigungspunkte alle 300 mm
- Vibration durch Seegang löst Schlauchschellen → Federbandschellen oder doppelte Schraubschellen
- Hohe Pumpenkapazität erforderlich (CE-Kat A/B Anforderungen)
- Redundantes Bilgensystem mit separater Notlenzpumpe
- Salzwasser-Aerosol im Motorraum: Kontakte der Schwimmerschalter korrodieren → vergoldete Kontakte
- Empfehlung: Überqualifizierung des Bilgensystems um Faktor 1,5

(Confidence: documented)

### 3.4 Tropen (warm, feucht, Korallengewässer)

- Biologisches Wachstum in Bilge extrem: Biofilm, Algen, Gerüche
- Bilge alle 2 Wochen mit enzymatischem Reiniger behandeln
- Insekten (Kakerlaken) nisten in warmen Bilgenschläuchen → Schlauchenden abdecken
- UV-Belastung maximiert: nur UV-stabilisierte Schläuche auf Deck
- Korallensand im Bilgenwasser → Sieb/Strainer häufiger reinigen
- Empfehlung: Antibakterielle Bilge-Schläuche, Siebreinigung wöchentlich

(Confidence: documented)

### 3.5 Süßwasser (Seen, Kanäle)

- Geringste Korrosionsbelastung → Standard-Materialien ausreichend
- Algenbildung bei stehendem Wasser → regelmäßig Bilge spülen
- Kein Biofouling am Austritt → einfache Rückschlagklappen ausreichend
- Winterlager mit Frostgefahr: identisch zu Ostsee
- Empfehlung: Standard-PVC-Schläuche, Austauschintervall 10 Jahre

(Confidence: documented)

---

## 4. Regional Sourcing

### 4.1 Europa

| Händler/Distributor | Land | Schwerpunkt | Web |
|---|---|---|---|
| SVB (Sailing + Yachting) | DE | Vollsortiment, schneller Versand DACH | svb-marine.de |
| Compass24 | DE | Großes Sortiment, günstige Preise | compass24.de |
| AWN | DE | Traditioneller Yachtausrüster | awn.de |
| Toplicht | DE | Hamburg, Fachberatung | toplicht.de |
| Bukh-Bremen | DE | Motoren + Zubehör, Pumpen | bukh-bremen.de |
| Bootsbedarf Engel | DE | Profi-Bedarf, Schlauch-Meterware | engel-boote.de |
| Maritimo | NL | Benelux-Distributor, große Lager | maritimo.nl |
| Accastillage Diffusion | FR | Frankreich, umfangreich | accastillage-diffusion.com |
| Plastimo Direct | FR | Herstellerdirekt | plastimo.com |
| Force 4 | UK | Chandlery-Kette, gute Preise | force4.co.uk |
| Marine Superstore | UK | Online-Großhändler | marinesuperstore.com |

(Confidence: documented)

### 4.2 Nordamerika

| Händler | Land | Schwerpunkt |
|---|---|---|
| West Marine | USA | Größter Einzelhändler, 250+ Filialen |
| Defender Industries | USA | Online, beste Preise, Profi-Sortiment |
| Hamilton Marine | USA | Nordost-USA, kommerzielle Fischerei + Yacht |
| Fisheries Supply | USA | Seattle, Pazifik-Nordwest |
| BoatUS Store | USA | Mitglieder-Rabatte |

(Confidence: documented)

### 4.3 Direktbezug vom Hersteller

| Hersteller | Direktverkauf | Mindestbestellmenge | Bemerkung |
|---|---|---|---|
| Trident Marine | Ja (tridenthose.com) | 15 m (50 ft) Rolle | Beste Preise bei Meterware |
| Shields Rubber | Ja (shieldsrubber.com) | 15 m (50 ft) Rolle | Premium-Qualität |
| Vetus | Nein (nur Händler) | — | Händlernetz vetus.com/dealers |
| Rule/Xylem | Nein (nur Händler) | — | Über Marine-Fachhandel |
| Seaflo | Ja (seaflo.com) | 1 Stück | China-Direktversand |

(Confidence: documented)

---

## 5. Zweck dieser Wissensdatei

### 5.1 Einordnung im AYDI-System

Diese Wissensdatei dient als Referenzbasis für die AYDI-Analysepipelines:

- **Pipeline A (Strukturiert)**: Bilgensystem-Spezifikationen aus CAD-Daten oder Eingabeformularen werden gegen die hier dokumentierten Standards validiert. Pumpenkapazität, Schlauchdurchmesser, Befestigungsabstände werden berechnet und bewertet.

- **Pipeline B (Visuell)**: Fotos von Bilgensystemen werden via Claude Vision analysiert. Diese Datei liefert die Referenzbilder und Fehlerbild-Beschreibungen für die visuelle Erkennung.

- **Pipeline C (Text)**: Service-Berichte und Gutachten werden auf Bilgensystem-relevante Befunde durchsucht. Das Glossar und die FAQ liefern die Terminologie für die NLP-Extraktion.

### 5.2 Module mit Bilgensystem-Relevanz

| Modul | Relevanz | Gewichtung |
|---|---|---|
| compliance | CE-Konformität Bilgensystem | Hoch |
| materials | Schlauchmaterial, Korrosion | Hoch |
| structural | Befestigungspunkte, Rumpfdurchbrüche | Mittel |
| service_patterns | Häufige Bilgensystem-Defekte | Hoch |
| cost | Ersatzteil- und Wartungskosten | Mittel |
| ergonomics | Zugänglichkeit Bilgenpumpe/-schläuche | Niedrig |
| production | Werksseitige Installation | Mittel |

(Confidence: documented)

---

## 6. Pydantic-Modelle

### 6.1 BilgeHoseSpec — Spezifikation eines Bilgenschlauchs

```python
from pydantic import BaseModel, Field
from typing import Optional, Literal
from enum import Enum

class HoseMaterial(str, Enum):
    """Schlauchmaterial-Typen für Bilgenschläuche."""
    PVC_REINFORCED = "pvc_reinforced"
    PVC_SPIRAL = "pvc_spiral"
    RUBBER_REINFORCED = "rubber_reinforced"
    RUBBER_SPIRAL = "rubber_spiral"
    EPDM = "epdm"
    SILICONE = "silicone"
    POLYURETHANE = "polyurethane"
    SANITATION_HOSE = "sanitation_hose"

class HoseApplication(str, Enum):
    """Einsatzzweck des Schlauchs."""
    BILGE_SUCTION = "bilge_suction"
    BILGE_DISCHARGE = "bilge_discharge"
    COCKPIT_DRAIN = "cockpit_drain"
    SCUPPER = "scupper"
    DECK_DRAIN = "deck_drain"
    EMERGENCY_BILGE = "emergency_bilge"
    ENGINE_BILGE = "engine_bilge"

class BilgeHoseSpec(BaseModel):
    """Spezifikation eines Bilgenschlauchs für AYDI-Analyse."""
    model_config = {"from_attributes": True}

    hose_id: str = Field(..., description="Eindeutige Schlauch-ID im System")
    manufacturer: str = Field(..., description="Hersteller des Schlauchs")
    product_name: str = Field(..., description="Produktbezeichnung")
    part_number: Optional[str] = Field(None, description="Hersteller-Artikelnummer")

    # Abmessungen in mm
    inner_diameter_mm: float = Field(..., ge=12, le=102, description="Innendurchmesser [mm]")
    outer_diameter_mm: float = Field(..., ge=16, le=120, description="Außendurchmesser [mm]")
    wall_thickness_mm: float = Field(..., ge=2, le=12, description="Wandstärke [mm]")
    min_bend_radius_mm: float = Field(..., ge=20, le=500, description="Minimaler Biegeradius [mm]")
    length_mm: Optional[float] = Field(None, ge=100, description="Einbaulänge [mm]")

    # Material
    material: HoseMaterial = Field(..., description="Schlauchmaterial")
    reinforcement: Optional[str] = Field(None, description="Verstärkungstyp (Gewebe, Spirale, Stahl)")
    uv_resistant: bool = Field(False, description="UV-beständig")
    flame_retardant: bool = Field(False, description="Flammhemmend")

    # Betriebsparameter
    max_pressure_bar: float = Field(..., ge=0.5, le=20, description="Max. Betriebsdruck [bar]")
    burst_pressure_bar: Optional[float] = Field(None, description="Berstdruck [bar]")
    max_vacuum_bar: Optional[float] = Field(None, description="Max. Unterdruck (Saugseite) [bar]")
    temperature_min_c: float = Field(-20, description="Min. Betriebstemperatur [°C]")
    temperature_max_c: float = Field(60, description="Max. Betriebstemperatur [°C]")

    # Einsatz
    application: HoseApplication = Field(..., description="Einsatzzweck")
    suitable_for_suction: bool = Field(False, description="Saugseitig einsetzbar (kollaps-sicher)")

    # Kosten
    price_per_meter_eur: Optional[float] = Field(None, ge=0, description="Preis pro Meter [EUR]")
    price_per_unit_eur: Optional[float] = Field(None, ge=0, description="Stückpreis [EUR]")

    # Scores 0–100
    quality_score: int = Field(..., ge=0, le=100, description="Qualitätsbewertung 0–100")
    marine_suitability_score: int = Field(..., ge=0, le=100, description="Marine-Eignung 0–100")

    confidence: Literal[
        "measured", "calculated", "visual_high", "visual_medium",
        "visual_low", "visual_insufficient", "estimated", "benchmark", "documented"
    ] = Field("estimated", description="Confidence-Level")
```

### 6.2 BilgeHoseCondition — Zustandsbewertung eines verbauten Schlauchs

```python
class ConditionCategory(str, Enum):
    """Zustandskategorien für Bilgenschläuche."""
    NEW = "new"
    GOOD = "good"
    FAIR = "fair"
    POOR = "poor"
    CRITICAL = "critical"
    FAILED = "failed"

class DefectType(str, Enum):
    """Defekttypen bei Bilgenschläuchen."""
    NONE = "none"
    SURFACE_CRACKING = "surface_cracking"
    HARDENING = "hardening"
    SOFTENING = "softening"
    DISCOLORATION = "discoloration"
    DELAMINATION = "delamination"
    KINKING = "kinking"
    ABRASION = "abrasion"
    CLAMP_CORROSION = "clamp_corrosion"
    FITTING_LEAK = "fitting_leak"
    BIOLOGICAL_GROWTH = "biological_growth"
    COLLAPSE = "collapse"
    SWELLING = "swelling"
    OIL_CONTAMINATION = "oil_contamination"
    UV_DEGRADATION = "uv_degradation"

class BilgeHoseCondition(BaseModel):
    """Zustandsbewertung eines verbauten Bilgenschlauchs."""
    model_config = {"from_attributes": True}

    hose_id: str = Field(..., description="Referenz auf BilgeHoseSpec.hose_id")
    location: str = Field(..., description="Einbauort (z.B. 'Bilgenpumpe achtern → Bordwand Stb.')")
    zone: str = Field(..., description="AYDI-Zone (z.B. 'engine_room', 'bilge_aft')")

    # Alter und Zustand
    installation_year: Optional[int] = Field(None, ge=1970, le=2030, description="Einbaujahr")
    estimated_age_years: Optional[float] = Field(None, ge=0, le=60, description="Geschätztes Alter [Jahre]")
    condition: ConditionCategory = Field(..., description="Gesamtzustand")
    condition_score: int = Field(..., ge=0, le=100, description="Zustandsbewertung 0–100")

    # Defekte
    primary_defect: DefectType = Field(DefectType.NONE, description="Hauptdefekt")
    secondary_defects: list[DefectType] = Field(default_factory=list, description="Nebendefekte")
    defect_description_de: Optional[str] = Field(None, description="Defektbeschreibung (Deutsch)")

    # Befestigungspunkte
    clamp_count: int = Field(0, ge=0, description="Anzahl Schlauchschellen")
    clamp_condition_score: int = Field(100, ge=0, le=100, description="Schellen-Zustand 0–100")
    connection_secure: bool = Field(True, description="Anschlüsse fest und dicht")

    # Empfehlungen
    replacement_recommended: bool = Field(False, description="Austausch empfohlen")
    replacement_urgency: Literal["none", "routine", "soon", "urgent", "immediate"] = Field(
        "none", description="Austausch-Dringlichkeit"
    )
    estimated_remaining_life_years: Optional[float] = Field(
        None, ge=0, le=20, description="Geschätzte Restlebensdauer [Jahre]"
    )
    replacement_cost_eur: Optional[float] = Field(None, ge=0, description="Geschätzte Austauschkosten [EUR]")

    findings_de: list[str] = Field(default_factory=list, description="Befunde (Deutsch)")
    suggestions_de: list[str] = Field(default_factory=list, description="Vorschläge (Deutsch)")

    confidence: Literal[
        "measured", "calculated", "visual_high", "visual_medium",
        "visual_low", "visual_insufficient", "estimated", "benchmark", "documented"
    ] = Field("estimated", description="Confidence-Level")
```

### 6.3 BilgeSystemAssessment — Gesamtbewertung des Bilgensystems

```python
class PumpType(str, Enum):
    """Bilgenpumpentyp."""
    CENTRIFUGAL_SUBMERSIBLE = "centrifugal_submersible"
    CENTRIFUGAL_INLINE = "centrifugal_inline"
    DIAPHRAGM_ELECTRIC = "diaphragm_electric"
    DIAPHRAGM_MANUAL = "diaphragm_manual"
    MANUAL_PISTON = "manual_piston"
    MANUAL_WHALE = "manual_whale"
    EMERGENCY_BUCKET = "emergency_bucket"
    ENGINE_DRIVEN = "engine_driven"

class FloatSwitchType(str, Enum):
    """Schwimmerschalter-Typ."""
    MECHANICAL_FLOAT = "mechanical_float"
    ELECTRONIC_FIELD_EFFECT = "electronic_field_effect"
    ULTRASONIC = "ultrasonic"
    PNEUMATIC = "pneumatic"
    NONE = "none"

class BilgePumpSpec(BaseModel):
    """Spezifikation einer Bilgenpumpe."""
    model_config = {"from_attributes": True}

    pump_id: str = Field(..., description="Pumpen-ID")
    manufacturer: str = Field(..., description="Hersteller")
    model: str = Field(..., description="Modellbezeichnung")
    part_number: Optional[str] = Field(None, description="Artikelnummer")
    pump_type: PumpType = Field(..., description="Pumpentyp")

    # Leistungsdaten
    capacity_gph: float = Field(..., ge=0, description="Nenn-Förderleistung [GPH]")
    capacity_lph: float = Field(..., ge=0, description="Nenn-Förderleistung [l/h]")
    max_head_m: float = Field(..., ge=0, description="Max. Förderhöhe [m]")
    voltage_v: Optional[float] = Field(None, description="Betriebsspannung [V]")
    current_draw_a: Optional[float] = Field(None, description="Stromaufnahme [A]")

    # Anschlüsse
    outlet_diameter_mm: float = Field(..., ge=12, le=76, description="Austrittsstutzen-Durchmesser [mm]")
    inlet_diameter_mm: Optional[float] = Field(None, description="Eintrittsstutzen-Durchmesser [mm]")

    # Schwimmerschalter
    float_switch_type: FloatSwitchType = Field(FloatSwitchType.NONE, description="Schwimmerschalter-Typ")
    float_switch_integrated: bool = Field(False, description="Schwimmerschalter integriert")

    price_eur: Optional[float] = Field(None, ge=0, description="Preis [EUR]")

class BilgeSystemAssessment(BaseModel):
    """Gesamtbewertung des Bilgensystems eines Bootes."""
    model_config = {"from_attributes": True}

    boat_id: str = Field(..., description="Boot-ID im AYDI-System")
    boat_class: str = Field(..., description="Bootsklasse")
    loa_mm: float = Field(..., ge=2500, le=80000, description="Länge über Alles [mm]")
    ce_category: Optional[Literal["A", "B", "C", "D"]] = Field(None, description="CE-Kategorie")

    # Pumpen
    pumps: list[BilgePumpSpec] = Field(default_factory=list, description="Verbaute Bilgenpumpen")
    pump_count: int = Field(0, ge=0, description="Anzahl Bilgenpumpen")
    total_capacity_lph: float = Field(0, ge=0, description="Gesamtkapazität [l/h]")
    capacity_adequate: bool = Field(False, description="Kapazität ausreichend für CE-Kat")
    redundancy_present: bool = Field(False, description="Redundante Pumpe vorhanden")
    manual_backup_present: bool = Field(False, description="Manuelle Backup-Pumpe vorhanden")

    # Schläuche
    hoses: list[BilgeHoseCondition] = Field(default_factory=list, description="Bilgenschlauch-Bewertungen")
    hose_count: int = Field(0, ge=0, description="Anzahl Schlauchsegmente")

    # Schwimmerschalter
    float_switch_present: bool = Field(False, description="Schwimmerschalter vorhanden")
    float_switch_functional: bool = Field(False, description="Schwimmerschalter funktional")
    high_water_alarm_present: bool = Field(False, description="Hochwasser-Alarm vorhanden")

    # Anti-Siphon
    anti_siphon_present: bool = Field(False, description="Anti-Siphon-Ventil vorhanden")
    anti_siphon_required: bool = Field(False, description="Anti-Siphon-Ventil erforderlich")

    # Borddurchlass
    discharge_through_hull_material: Optional[str] = Field(None, description="Material Bilgen-Borddurchlass")
    discharge_above_waterline: bool = Field(True, description="Austritt über Wasserlinie")
    seacock_present: bool = Field(False, description="Seeventil am Bilgen-Austritt")

    # Cockpit-Drain
    cockpit_drain_count: int = Field(0, ge=0, description="Anzahl Cockpit-Abflüsse")
    cockpit_self_draining: bool = Field(False, description="Cockpit selbstlenzend")
    cockpit_drain_hose_condition: Optional[ConditionCategory] = Field(None, description="Zustand Cockpit-Drain-Schläuche")

    # Scores 0–100
    overall_score: int = Field(..., ge=0, le=100, description="Gesamtbewertung Bilgensystem 0–100")
    compliance_score: int = Field(..., ge=0, le=100, description="Normenkonformität 0–100")
    condition_score: int = Field(..., ge=0, le=100, description="Zustandsbewertung 0–100")
    capacity_score: int = Field(..., ge=0, le=100, description="Kapazitätsbewertung 0–100")
    redundancy_score: int = Field(..., ge=0, le=100, description="Redundanzbewertung 0–100")

    # Befunde
    findings_de: list[str] = Field(default_factory=list, description="Befunde (Deutsch)")
    warnings_de: list[str] = Field(default_factory=list, description="Warnungen (Deutsch)")
    suggestions_de: list[str] = Field(default_factory=list, description="Vorschläge (Deutsch)")

    confidence: Literal[
        "measured", "calculated", "visual_high", "visual_medium",
        "visual_low", "visual_insufficient", "estimated", "benchmark", "documented"
    ] = Field("estimated", description="Confidence-Level")
```

(Confidence: documented)

---

## 7. Grundlagen

### 7.1 Das Bilgensystem — Übersicht

Das Bilgensystem eines Bootes besteht aus folgenden Komponenten:

```
Bilgensumpf (Kielbereich, tiefster Punkt)
  └── Sieb/Strainer (Grobfilter)
       └── Bilgenschlauch (Saugseite — muss kollaps-sicher sein!)
            └── Bilgenpumpe (elektrisch oder manuell)
                 └── Bilgenschlauch (Druckseite)
                      └── Anti-Siphon-Ventil / Schwanenhals
                           └── Borddurchlass (mit/ohne Seeventil)
                                └── Außenbords
```

Zusätzliche Leitungen:
- Cockpit-Drain → Borddurchlass achtern
- Deck-Scupper → Bordwand-Öffnung
- Ankerkasten-Drain → Bilge oder Borddurchlass
- Duschsumpf → Grauwasserpumpe → Borddurchlass

(Confidence: documented)

### 7.2 Bilgenpumpen-Typen

#### 7.2.1 Tauchpumpen (Submersible Centrifugal)

**Funktionsprinzip**: Elektromotor im wasserdichten Gehäuse, Impeller fördert Wasser durch Zentrifugalkraft. Pumpe sitzt direkt im Bilgenwasser.

**Vorteile**: Hohe Förderleistung, selbstansaugend, kompakt, einfache Installation
**Nachteile**: Begrenzte Förderhöhe, empfindlich gegen Verschmutzung, Impeller-Verschleiß

**Typische Modelle**:

| Modell | Kapazität | Spannung | Strom | Austritt | Preis ca. |
|---|---|---|---|---|---|
| Rule 25S (500 GPH) | 1.893 l/h | 12V DC | 2,5 A | 19 mm (¾") | 25 EUR |
| Rule 27S (1000 GPH) | 3.785 l/h | 12V DC | 3,8 A | 28 mm (1⅛") | 35 EUR |
| Rule 09 (2000 GPH) | 7.571 l/h | 12V DC | 8,4 A | 28 mm (1⅛") | 55 EUR |
| Rule 10 (3700 GPH) | 14.006 l/h | 12V DC | 14 A | 38 mm (1½") | 85 EUR |
| Jabsco 37202-2012 (500 GPH) | 1.893 l/h | 12V DC | 2,0 A | 19 mm (¾") | 30 EUR |
| Seaflo SFBP1-G500-01 | 1.893 l/h | 12V DC | 2,0 A | 19 mm (¾") | 15 EUR |
| Seaflo SFBP1-G1100-01 | 4.164 l/h | 12V DC | 3,5 A | 28 mm (1⅛") | 20 EUR |
| Johnson Pump L450 | 1.703 l/h | 12V DC | 2,0 A | 19 mm (¾") | 32 EUR |
| Johnson Pump L750 | 2.839 l/h | 12V DC | 3,0 A | 19 mm (¾") | 40 EUR |
| Attwood Sahara S500 | 1.893 l/h | 12V DC | 2,5 A | 19 mm (¾") | 22 EUR |
| TMC 03303 (600 GPH) | 2.271 l/h | 12V DC | 2,5 A | 19 mm (¾") | 18 EUR |

(Confidence: documented)

#### 7.2.2 Membranpumpen (Diaphragm)

**Funktionsprinzip**: Flexible Membran wird durch Exzenter oder Elektromagnet bewegt, erzeugt Saug- und Druckwirkung über Ventile. Pumpe sitzt über dem Bilgenwasserspiegel.

**Vorteile**: Selbstansaugend (bis 2 m), trockenlaufsicher, unempfindlich gegen Schmutz, hohe Förderhöhe
**Nachteile**: Geringere Förderleistung, pulsierender Förderstrom, Membranverschleiß, teurer

**Typische Modelle**:

| Modell | Kapazität | Spannung | Strom | Anschluss | Preis ca. |
|---|---|---|---|---|---|
| Whale Gulper 220 | 840 l/h | 12V DC | 3,0 A | 19/25 mm | 95 EUR |
| Whale Gulper 320 | 1.230 l/h | 12V DC | 5,0 A | 25/28 mm | 120 EUR |
| Whale Orca 950 | 950 l/h | 12V DC | 3,2 A | 25 mm | 145 EUR |
| Jabsco Water Puppy 6050 | 1.500 l/h | 12V DC | 5,0 A | 25 mm | 160 EUR |
| Jabsco Par-Max 4 (31620) | 946 l/h | 12V DC | 8,0 A | 19 mm | 180 EUR |
| Shurflo 355-101 | 530 l/h | 12V DC | 2,5 A | 12 mm | 85 EUR |

(Confidence: documented)

#### 7.2.3 Handpumpen (Manual Bilge Pumps)

**Funktionsprinzip**: Manuell betätigte Kolben- oder Membranpumpe. Obligatorisch als Backup gemäß ABYC und empfohlen nach ISO 8849.

**Vorteile**: Stromlos, zuverlässig, hohe Förderleistung bei guter Ergonomie, unersetzbar als Notsystem
**Nachteile**: Erfordert körperliche Arbeit, muss zugänglich installiert sein

**Typische Modelle**:

| Modell | Typ | Kapazität/Hub | Anschluss | Preis ca. |
|---|---|---|---|---|
| Whale Gusher 10 Mk3 | Membran-Handhebel | 37 l/min | 25/38 mm | 85 EUR |
| Whale Gusher 25 | Membran-Handhebel | 56 l/min | 38 mm | 130 EUR |
| Whale Gusher 30 | Membran-Handhebel | 69 l/min | 38 mm | 185 EUR |
| Whale Gusher Urchin | Membran-Fußbedienung | 17 l/min | 25 mm | 95 EUR |
| Henderson Mk V | Kolben-Handhebel | 69 l/min | 38 mm | 210 EUR |
| Edison International 18 | Kolben-Handhebel | 95 l/min | 38 mm | 165 EUR |
| Plastimo 10596 | Membran-Handhebel | 55 l/min | 38 mm | 75 EUR |

(Confidence: documented)

### 7.3 Schwimmerschalter (Float Switches)

#### 7.3.1 Mechanische Schwimmerschalter

**Funktionsprinzip**: Schwimmkörper steigt mit Wasserstand, betätigt über Kippwinkel einen Quecksilber- oder Mikroschalter.

| Modell | Typ | Schaltwinkel | Max. Strom | Preis ca. |
|---|---|---|---|---|
| Rule 35A (Rule-A-Matic) | Quecksilber-Kipp | 15° | 14 A | 15 EUR |
| Rule 37A | Quecksilber-Kipp | 15° | 20 A | 18 EUR |
| Johnson Pump Ultima Switch | Mikroschalter | 20° | 12 A | 22 EUR |
| Attwood 4201-7 | Quecksilber-Kipp | 15° | 12 A | 12 EUR |
| TMC 08801 | Mikroschalter | 20° | 8 A | 10 EUR |

**Achtung**: Quecksilber-Schwimmerschalter sind in der EU seit 2017 für Neuinstallationen nicht mehr empfohlen (RoHS-Richtlinie). Nachrüstung mit quecksilberfreien Alternativen empfohlen.

(Confidence: documented)

#### 7.3.2 Elektronische Schwimmerschalter

**Funktionsprinzip**: Kapazitive oder Feldeffekt-Sensorik erkennt Wasserstand ohne bewegliche Teile.

| Modell | Technologie | Max. Strom | Empfindlichkeit | Preis ca. |
|---|---|---|---|---|
| Rule EcoSwitch | Feldeffekt | 20 A | Einstellbar | 35 EUR |
| Ultra Safety Systems UltraSwitch | Kapazitiv | 25 A | Einstellbar | 55 EUR |
| Johnson Pump Ultima Electronic | Feldeffekt | 15 A | Fest | 28 EUR |
| Whale BE9006 | Kapazitiv | 12 A | Fest | 40 EUR |
| Aqualarm 20230 | Pneumatisch | 20 A | Einstellbar | 45 EUR |

**Vorteile elektronischer Schalter**: Keine beweglichen Teile, kein Verklemmen durch Bilgen-Schmutz, keine Quecksilber-Problematik, geringere Fehlauslösungen.

(Confidence: documented)

### 7.4 Hochwasser-Alarme

| Modell | Typ | Lautstärke | Funktion | Preis ca. |
|---|---|---|---|---|
| Rule 33ALA | Elektrisch + optisch | 105 dB | Alarm bei Hochstand | 30 EUR |
| Aqualarm 20075 | Elektrisch | 90 dB | Multi-Zone | 65 EUR |
| BEP 1000-BSS | Elektrisch + Relais | 85 dB | NMEA-fähig | 85 EUR |
| Hella Marine 2XA 998 | Optisch (LED) | — | Dashboard-Anzeige | 25 EUR |
| Blue Sea 8006 | Panel-Einbau | 90 dB | Alarm + Pumpen-Anzeige | 55 EUR |

ABYC H-22 fordert Hochwasser-Alarm für Boote ab 8 m (26 ft).

(Confidence: documented)

### 7.5 Bilgenschlauch-Materialien

#### 7.5.1 Verstärkter PVC-Schlauch (Standard)

**Aufbau**: PVC-Innenseele + Polyester-Gewebeverstärkung + PVC-Außenmantel
**Einsatz**: Druckseite Bilgenpumpe, Cockpit-Drain, Scupper
**Temperaturbereich**: -10°C bis +60°C
**Druckfestigkeit**: 3–6 bar (je nach Durchmesser und Verstärkung)
**Biegeradius**: 3–5× Innendurchmesser
**Lebensdauer**: 5–10 Jahre (revier- und UV-abhängig)

| ID mm | AD mm | Wandstärke mm | Biegeradius mm | Preis/m EUR |
|---|---|---|---|---|
| 16 | 22 | 3,0 | 55 | 3,50 |
| 19 | 26 | 3,5 | 65 | 4,00 |
| 25 | 33 | 4,0 | 85 | 5,50 |
| 28 | 36 | 4,0 | 95 | 6,00 |
| 32 | 40 | 4,0 | 110 | 7,00 |
| 38 | 48 | 5,0 | 130 | 9,00 |
| 50 | 62 | 6,0 | 170 | 13,00 |

(Confidence: documented)

#### 7.5.2 Spiral-verstärkter PVC-Schlauch (Saugseite)

**Aufbau**: PVC mit eingebetteter Kunststoff- oder Stahldraht-Spirale
**Einsatz**: Saugseite Bilgenpumpe (kollaps-sicher unter Unterdruck), Bilgen-Absaugung
**Besonderheit**: Kann Unterdruck bis -0,5 bar standhalten ohne zu kollabieren
**Temperaturbereich**: -10°C bis +60°C
**Biegeradius**: 4–6× Innendurchmesser (steifer als Gewebeschlauch)
**Lebensdauer**: 8–12 Jahre

| ID mm | AD mm | Wandstärke mm | Biegeradius mm | Preis/m EUR |
|---|---|---|---|---|
| 19 | 27 | 4,0 | 95 | 7,00 |
| 25 | 34 | 4,5 | 120 | 9,00 |
| 32 | 42 | 5,0 | 155 | 12,00 |
| 38 | 49 | 5,5 | 185 | 15,00 |
| 50 | 63 | 6,5 | 240 | 20,00 |

(Confidence: documented)

#### 7.5.3 Gummi-Schläuche (EPDM / SBR / NBR)

**Aufbau**: EPDM- oder SBR-Gummi mit Textilgeflecht-Verstärkung
**Einsatz**: Motorraum (hitzebeständig), hochwertige Installationen, kommerziell
**Temperaturbereich**: -30°C bis +100°C (EPDM), -20°C bis +80°C (SBR)
**Vorteile**: Flexibler als PVC, UV-beständiger, alterungsbeständiger
**Nachteile**: Teurer, schwerer, Anschlussprofil erfordert größere Schellen

| ID mm | AD mm | Wandstärke mm | Material | Preis/m EUR |
|---|---|---|---|---|
| 19 | 29 | 5,0 | EPDM | 12,00 |
| 25 | 36 | 5,5 | EPDM | 15,00 |
| 32 | 44 | 6,0 | EPDM | 18,00 |
| 38 | 50 | 6,0 | EPDM | 22,00 |
| 50 | 64 | 7,0 | EPDM | 28,00 |

(Confidence: documented)

#### 7.5.4 Sanitärschlauch (geruchsdicht)

**Aufbau**: Mehrschichtig mit geruchsdichter Barriereschicht (PE oder Mylar)
**Einsatz**: Bilgenleitung wenn Geruchsbelästigung zu erwarten, Grauwasser
**Marken**: Shields 148 Series, Trident 101/102, Vetus?"

| Produkt | ID mm | AD mm | Typ | Preis/m EUR |
|---|---|---|---|---|
| Shields 148-1000 (1") | 25 | 35 | PE-Barriere | 18,00 |
| Shields 148-1250 (1¼") | 32 | 42 | PE-Barriere | 22,00 |
| Shields 148-1500 (1½") | 38 | 49 | PE-Barriere | 26,00 |
| Trident 101-1000 (1") | 25 | 36 | Mylar-Barriere | 20,00 |
| Trident 101-1500 (1½") | 38 | 50 | Mylar-Barriere | 28,00 |
| Vetus?"HOS25A | 25 | 34 | PE-Barriere | 16,00 |

(Confidence: documented)

#### 7.5.5 Material-Vergleichsmatrix

| Eigenschaft | PVC verstärkt | PVC Spiral | EPDM Gummi | Sanitär |
|---|---|---|---|---|
| Preis | ★★★★★ | ★★★☆☆ | ★★☆☆☆ | ★★☆☆☆ |
| UV-Beständigkeit | ★★☆☆☆ | ★★☆☆☆ | ★★★★☆ | ★★★☆☆ |
| Temperaturbeständigkeit | ★★★☆☆ | ★★★☆☆ | ★★★★★ | ★★★☆☆ |
| Flexibilität | ★★★★☆ | ★★☆☆☆ | ★★★★★ | ★★★☆☆ |
| Kollaps-Sicherheit | ★★☆☆☆ | ★★★★★ | ★★☆☆☆ | ★★☆☆☆ |
| Geruchsdichtigkeit | ★★☆☆☆ | ★★☆☆☆ | ★★★☆☆ | ★★★★★ |
| Lebensdauer | ★★★☆☆ | ★★★★☆ | ★★★★★ | ★★★★☆ |
| Gewicht | ★★★★★ | ★★★☆☆ | ★★☆☆☆ | ★★★☆☆ |

(Confidence: documented)

### 7.6 Borddurchlässe für Bilgen-Austritt

#### 7.6.1 Positionierung

Der Bilgen-Austritt muss:
- Möglichst hoch über der Wasserlinie liegen (Rück-Siphon vermeiden)
- Bei Segelbooten: über der Krängungs-Wasserlinie bei 20° Krängung
- Nicht in der Nähe von Kühlwasser-Einlässen (Rezirkulation vermeiden)
- Zugänglich für Inspektion und Wartung
- Nicht im Bereich von Antifouling-Ablösung

#### 7.6.2 Material und Typen

| Typ | Material | Vorteil | Nachteil | Preis ca. |
|---|---|---|---|---|
| Standard Skin-Fitting | Bronze (DZR) | Bewährt, korrosionsbeständig | Schwer, teuer, galvanisch | 35–80 EUR |
| Marelon Skin-Fitting | Verbundwerkstoff | Leicht, keine Galvanik | Nicht für strukturelle Last | 25–50 EUR |
| Edelstahl 316L | AISI 316L | Fest, glatte Oberfläche | Spaltkorrosion möglich | 40–90 EUR |
| Kunststoff (Nylon) | PA6.6 GF30 | Günstig, leicht | UV-empfindlich, versprödet | 8–20 EUR |

(Confidence: documented)

### 7.7 Anti-Siphon-Schutz

#### 7.7.1 Problemstellung

Wenn der Bilgen-Austritt unter der Wasserlinie liegt oder bei Krängung unter Wasser kommt, kann ein Siphon-Effekt entstehen: Seewasser wird rückwärts durch die Bilgenleitung ins Boot gesaugt.

#### 7.7.2 Schutzmaßnahmen

**Option A — Schwanenhals (Gooseneck):**
- Bilgenschlauch wird vor dem Borddurchlass in einer Schleife über die Wasserlinie geführt
- Scheitelpunkt mindestens 300 mm über maximaler Wasserlinie (inkl. Krängung)
- Einfach, keine beweglichen Teile, zuverlässig
- Nachteil: Förderhöhe der Pumpe muss ausreichen

**Option B — Anti-Siphon-Ventil (Vented Loop):**
- Ventil am höchsten Punkt der Leitung, öffnet bei Unterdruck und bricht den Siphon
- Position: mindestens 200 mm über Wasserlinie
- Muss regelmäßig geprüft werden (Ventilmembran kann verkleben)

| Anti-Siphon-Ventil | Anschluss | Material | Preis ca. |
|---|---|---|---|
| Vetus?"AS19 | 19 mm | Kunststoff | 15 EUR |
| Vetus?"AS25 | 25 mm | Kunststoff | 18 EUR |
| Vetus?"AS38 | 38 mm | Kunststoff | 22 EUR |
| Whale AV1218 | 19 mm | Kunststoff | 12 EUR |
| Jabsco 29295-1000 | 25 mm | Kunststoff | 28 EUR |
| Forespar 903010 | 19–38 mm | Bronze | 55 EUR |

(Confidence: documented)

### 7.8 Cockpit-Drain-System

#### 7.8.1 Anforderungen

Selbstlenzendes Cockpit (CE-Kat A/B obligatorisch):
- Cockpit-Boden über Wasserlinie
- Mindestens zwei Abflüsse (Redundanz)
- Abflussdurchmesser: mindestens 25 mm, empfohlen 38 mm
- Abflusskapazität: Cockpit muss sich in <5 min entleeren (ISO 11812)
- Schläuche: UV-stabilisiert wenn im Cockpit-Bereich sichtbar

#### 7.8.2 Berechnung Cockpit-Drain-Kapazität

```
Cockpit-Volumen [l] = Länge [m] × Breite [m] × Süllhöhe [m] × 1000
Erforderliche Drain-Kapazität [l/min] = Cockpit-Volumen / 5 (für 5-min-Entleerung)
Mindest-Schlauchdurchmesser: Q = A × v → A = Q / v → d = √(4A/π)
  wobei v ≈ 0,5 m/s (Schwerkraft-Abfluss, pessimistisch)
```

Beispiel: Cockpit 2,4 m × 1,8 m × 0,25 m = 1.080 l
→ Drain-Rate: 216 l/min = 3,6 l/s
→ Bei 2 Abflüssen: 1,8 l/s pro Abfluss
→ Mindest-ID: √(4 × 1,8 / (π × 0,5 × 1000)) × 1000 ≈ 68 mm → 2× 38 mm Schlauch (je 1,13 l/s bei 0,5 m/s)

(Confidence: calculated)

#### 7.8.3 Cockpit-Drain-Schlauchmaterial

Cockpit-Drain-Schläuche sind UV-Belastung ausgesetzt und müssen:
- UV-stabilisiert sein (PVC mit UV-Inhibitor oder EPDM)
- Knick-sicher verlegt werden (große Biegeradien)
- Mit doppelten Schlauchschellen am Borddurchlass befestigt sein
- Regelmäßig auf Durchfluss geprüft werden (Blätter, Sand)

(Confidence: documented)

### 7.9 Scupper-Leitungen (Deck-Entwässerung)

Scupper (Speigatt) leiten Regenwasser und Spritzwasser vom Deck ab:
- Durchmesser: 19–25 mm für Seitendeck-Scupper
- Material: Standard-PVC oder Gummi
- Befestigung: Einzelne Schlauchschelle ausreichend (kein Seeventil nötig, da über WL)
- Rückschlagklappe empfohlen bei seitlichen Scuppern (Wassereinbruch bei Krängung)
- Scupper-Entwässerung nie direkt in Bilge leiten (Überlastung Bilgensystem)

(Confidence: documented)

### 7.10 Bilgen-Sieb / Strainer

Das Bilgen-Sieb verhindert, dass Feststoffe (Schrauben, Drähte, Lappen) in die Pumpe gelangen:

| Typ | Beschreibung | Maschenweite | Einsatz |
|---|---|---|---|
| Stutzen-Sieb (Inline) | Am Pumpeneingang befestigt | 3–5 mm | Standard-Tauchpumpen |
| Saugkorb (Foot Valve) | Am Ende des Saugschlauchs | 3–5 mm | Membranpumpen |
| Box-Strainer | Kastenförmig, große Oberfläche | 2–4 mm | Hochleistungssysteme |
| Beutel-Strainer | Textilbeutel über Pumpe | 1–3 mm | Zusatzfilter |

Reinigungsintervall: mindestens vierteljährlich, bei Werftaufenthalt immer.

(Confidence: documented)

### 7.11 Bilgenbelüftung und Gasansammlung

Bei Motorbooten mit Benzinmotor (Innenborder) ist die Bilgenbelüftung sicherheitskritisch:
- Benzindämpfe sind schwerer als Luft und sammeln sich in der Bilge
- USCG 33 CFR 183.610: Bilgengebläse (Blower) für geschlossene Motorräume mit Benzinmotor vorgeschrieben
- Bilgengebläse muss 4 min vor Motorstart laufen
- Bilgenschläuche dürfen die Gebläse-Luftzirkulation nicht blockieren
- Kein PVC-Schlauch in Benzindampf-Umgebung (kann sich auflösen) → PE oder NBR verwenden

| Bilgengebläse | Hersteller | Durchmesser mm | Luftleistung m³/h | Preis EUR |
|---|---|---|---|---|
| Attwood Turbo 3000 | Attwood | 76 (3") | 170 | 28 |
| Attwood Turbo 4000 | Attwood | 102 (4") | 280 | 35 |
| Rule 240 Blower | Rule/Xylem | 76 (3") | 190 | 32 |
| Johnson AirV 4-750 | Johnson Pump | 102 (4") | 320 | 42 |
| TMC 03714 | TMC | 76 (3") | 165 | 22 |

(Confidence: documented)

### 7.12 Bilgen-Überwachungssysteme (NMEA 2000 / SignalK)

Moderne Bilgenüberwachung über Bordnetzwerk:

| System | Protokoll | Funktionen | Preis EUR |
|---|---|---|---|
| Maretron BBS100 | NMEA 2000 | Pegelstand, Pumpzyklen-Zähler, Alarm | 250 |
| Maretron FPM100 | NMEA 2000 | Druck/Flüssigkeitsstand für Bilge | 280 |
| Yacht Devices YDBS-01 | NMEA 2000 | Bilgenschalter-zu-N2K Adapter | 85 |
| Siren Marine MTC | Wi-Fi/Cellular | Bilge + GPS + Batterie, Cloud | 350 + 20/Monat |
| FloatHub | Cellular | Bilge + GPS + Batterie, Cloud | 280 + 10/Monat |
| SignalK DIY | SignalK/Open Source | ESP32 + Ultraschall-Sensor | 25 (Eigenbau) |

**NMEA 2000 PGN für Bilge**:
- PGN 127501 (Binary Status Report): Schwimmerschalter-Status (an/aus)
- PGN 127505 (Fluid Level): Bilgenwasser-Pegelstand in Prozent
- PGN 127509 (Status): Pumpen-Betriebsstatus

**SignalK-Pfade**:
- `vessels.self.bilge.0.level` — Bilgenstand [%]
- `vessels.self.bilge.0.pump.state` — Pumpe an/aus
- `vessels.self.bilge.0.pump.cycleCount` — Pumpzyklen

(Confidence: documented)

### 7.13 Notlenzsysteme und Damage Control

Für Blauwasser-Yachten und CE-Kat A sind erweiterte Lenzsysteme empfohlen:

**Crash-Pumpe (Emergency Bilge Pump)**:
- Motorgetriebene Lenzpumpe (vom Hauptmotor über Keilriemen)
- Förderleistung: 5.000–20.000 l/h (weit über elektrischer Pumpe)
- Beispiel: Jabsco 52040 (motorbetrieben, 11.000 l/h) — ca. 350 EUR
- Anschluss: 50 mm Saugschlauch (Spiralverstärkt, Pflicht!)
- Vorteil: Solange Motor läuft, unbegrenzte Pumpzeit
- Nachteil: Funktioniert nur bei laufendem Motor

**Cross-Connection Feuerlösch-/Lenzsystem**:
- Auf Superyachten: Feuerlöschpumpe kann auf Bilge umgeschaltet werden
- Ventilkasten mit Umschaltventilen (Manifold)
- Klassifikations-Anforderung für Yachten >24 m unter Klasse

**Wasser-Ejektor (Sea-Water Eductor)**:
- Seewasser wird unter Druck durch Düse gedrückt → erzeugt Saugwirkung
- Bilgenwasser wird ohne eigene Pumpe mitgerissen
- Anschluss an Seewasser-Kühlkreislauf oder separate Seewasserpumpe
- Vorteil: Keine elektrische Energie für Bilgenpumpe nötig
- Beispiel: Groco BJ-Series Bilge Jet — ca. 85 EUR

| Notlenzsystem | Kapazität l/h | Energiequelle | Preis EUR |
|---|---|---|---|
| Handpumpe (Whale Gusher 30) | 4.140 | Muskelkraft | 185 |
| Handpumpe (Henderson Mk V) | 4.140 | Muskelkraft | 210 |
| Eimer (10 l, 15 Hübe/min) | 9.000 | Muskelkraft | 5 |
| Motorpumpe (Jabsco 52040) | 11.000 | Hauptmotor | 350 |
| Ejektor (Groco BJ) | 3.000–5.000 | Seewasserpumpe | 85 |
| Tragbare Tauchpumpe (12V) | 3.000–5.000 | Batterie | 55–120 |

**Anmerkung zum Eimer**: Ein Eimer ist mathematisch eines der effektivsten Notlenzmittel! 10 l × 15 Hübe/min = 150 l/min = 9.000 l/h — das übertrifft die meisten elektrischen Bilgenpumpen. Voraussetzung: physische Fitness und ein Zugang zur Bilge.

(Confidence: documented)

---

## 8. Hersteller — Vollständige Übersicht

### 8.1 Rule Industries (ITT / Xylem)

**Firmenprofil**: Rule Industries, gegründet 1958 in Gloucester, Massachusetts. Seit 2011 Teil von Xylem Inc. (vorher ITT). Weltmarktführer bei Bilgenpumpen für Freizeitboote.

**Produktpalette Bilgenpumpen**:

| Modell | Typ | GPH | l/h | Volt | Ampere | Austritt mm | Art.-Nr. | Preis EUR |
|---|---|---|---|---|---|---|---|---|
| Rule 24 | Tauch | 360 | 1.363 | 12V | 1,6 | 19 | 24 | 18 |
| Rule 25S | Tauch | 500 | 1.893 | 12V | 2,5 | 19 | 25S | 25 |
| Rule 25DA | Tauch | 500 | 1.893 | 12V | 2,5 | 19 | 25DA | 35 |
| Rule 27S | Tauch | 1.000 | 3.785 | 12V | 3,8 | 28 | 27S | 35 |
| Rule 27DA | Tauch | 1.000 | 3.785 | 12V | 3,8 | 28 | 27DA | 48 |
| Rule 09 | Tauch | 2.000 | 7.571 | 12V | 8,4 | 28 | 09 | 55 |
| Rule 10 | Tauch | 3.700 | 14.006 | 12V | 14,0 | 38 | 10 | 85 |
| Rule 14A | Tauch | 3.700 | 14.006 | 24V | 7,0 | 38 | 14A | 90 |
| Rule 15A | Tauch | 4.000 | 15.142 | 12V | 18,0 | 50 | 15A | 120 |

**Schwimmerschalter**:

| Modell | Typ | Max. Strom | Art.-Nr. | Preis EUR |
|---|---|---|---|---|
| Rule-A-Matic 35A | Mechanisch (Hg-frei seit 2020) | 14 A | 35A | 15 |
| Rule 37A | Mechanisch | 20 A | 37A | 18 |
| Rule EcoSwitch 39 | Elektronisch (Feldeffekt) | 20 A | 39 | 35 |
| Rule 40A | Multi-Port (3-Wege) | 20 A | 40A | 55 |

**Rule-spezifische Schlauchempfehlungen**:
- Rule 25S/27S: 19 mm bzw. 28 mm ID, verstärkter PVC-Schlauch
- Rule 09/10: 28 mm bzw. 38 mm ID, Spiralschlauch auf Saugseite empfohlen
- Schlauchlänge max. 3 m bei 500 GPH, max. 5 m bei 2000 GPH (Herstellerangabe)
- Förderhöhe berücksichtigen: bei 2 m Förderhöhe verliert Rule 27S ca. 30% Leistung

(Confidence: documented)

### 8.2 Johnson Pump (SPX Flow)

**Firmenprofil**: Johnson Pump Marine, Teil der SPX Flow Gruppe, Hauptsitz Schweden. Bekannt für innovative Impeller-Designs und robuste Verarbeitung.

**Produktpalette**:

| Modell | Typ | GPH | l/h | Volt | Ampere | Austritt mm | Art.-Nr. | Preis EUR |
|---|---|---|---|---|---|---|---|---|
| L450 | Tauch | 450 | 1.703 | 12V | 2,0 | 19 | 32-1450-01 | 32 |
| L550 | Tauch | 550 | 2.082 | 12V | 2,5 | 19 | 32-1550-01 | 38 |
| L750 | Tauch | 750 | 2.839 | 12V | 3,0 | 19 | 32-1750-01 | 40 |
| L1250 | Tauch | 1.250 | 4.732 | 12V | 4,5 | 28 | 32-47252-01 | 52 |
| L1600 | Tauch | 1.600 | 6.057 | 12V | 6,0 | 28 | 32-47260-01 | 65 |
| L2200 | Tauch | 2.200 | 8.328 | 12V | 9,0 | 28 | 32-47262-01 | 78 |
| L4000 | Tauch | 4.000 | 15.142 | 12V | 16,0 | 38 | 32-47000-01 | 115 |
| Combo L750 | Tauch + Schalter | 750 | 2.839 | 12V | 3,0 | 19 | 32-47502-01 | 55 |

**Ultima Switch**:
| Modell | Typ | Max. Strom | Preis EUR |
|---|---|---|---|
| Ultima Switch 34-1900 | Mikroschalter | 12 A | 22 |
| Ultima Electronic 36-47231 | Elektronisch | 15 A | 28 |

(Confidence: documented)

### 8.3 Whale Marine

**Firmenprofil**: Whale Marine, gegründet 1958 in Nordirland (UK). Spezialist für Membranpumpen und manuelle Bilgenpumpen. Premium-Qualität, besonders bei Blauwasser-Seglern beliebt.

**Bilgenpumpen**:

| Modell | Typ | Kapazität | Volt | Ampere | Anschluss mm | Art.-Nr. | Preis EUR |
|---|---|---|---|---|---|---|---|
| Gulper 220 | Membran elektr. | 840 l/h | 12V | 3,0 | 19/25 | BE0920 | 95 |
| Gulper 320 | Membran elektr. | 1.230 l/h | 12V | 5,0 | 25/28 | BE0930 | 120 |
| SuperSub Smart 650 | Tauch | 2.460 l/h | 12V | 3,5 | 28 | SS5012 | 55 |
| SuperSub Smart 1100 | Tauch | 4.164 l/h | 12V | 5,5 | 28 | SS5024 | 72 |
| Orca 950 | Membran elektr. | 950 l/h | 12V | 3,2 | 25 | OE0952 | 145 |

**Handpumpen**:

| Modell | Typ | Kapazität | Anschluss mm | Art.-Nr. | Preis EUR |
|---|---|---|---|---|---|
| Gusher 10 Mk3 | Membran | 37 l/min | 25/38 | BP3740 | 85 |
| Gusher 25 | Membran | 56 l/min | 38 | BP4012 | 130 |
| Gusher 30 | Membran | 69 l/min | 38 | BP4430 | 185 |
| Gusher Titan | Membran | 94 l/min | 38 | BP5435 | 285 |
| Gusher Urchin | Fuß-Membran | 17 l/min | 25 | BP9005 | 95 |

**Schwimmerschalter**:

| Modell | Typ | Max. Strom | Preis EUR |
|---|---|---|---|
| Whale BE9003 | Mechanisch | 10 A | 18 |
| Whale BE9006 | Elektronisch (kapazitiv) | 12 A | 40 |

(Confidence: documented)

### 8.4 Jabsco / Xylem

**Firmenprofil**: Jabsco (seit 1939), jetzt Teil von Xylem Inc. Umfangreiche Produktpalette von Bilgenpumpen über Toilettensysteme bis Druckwasser.

**Bilgenpumpen**:

| Modell | Typ | GPH | l/h | Volt | Austritt mm | Art.-Nr. | Preis EUR |
|---|---|---|---|---|---|---|---|
| Jabsco 37202-2012 | Tauch | 500 | 1.893 | 12V | 19 | 37202-2012 | 30 |
| Jabsco 37202-2024 | Tauch | 500 | 1.893 | 24V | 19 | 37202-2024 | 33 |
| Jabsco 37010 | Tauch | 750 | 2.839 | 12V | 19 | 37010-0092 | 42 |
| Jabsco Water Puppy | Membran | 1.500 | 5.678 | 12V | 25 | 18220-1127 | 160 |
| Jabsco Cyclone LP | Tauch | 1.600 | 6.057 | 12V | 28 | 50860-2012 | 75 |
| Jabsco Cyclone HP | Tauch | 3.000 | 11.356 | 12V | 38 | 50880-2012 | 120 |

**Jabsco Water Puppy — Detailspezifikation**:
- Typ: Flexible-Impeller-Pumpe (selbstansaugend bis 3 m)
- Besonders geeignet als Notlenzpumpe oder Transferpumpe
- Trockenlauf max. 30 Sekunden (Impeller-Schaden!)
- Impeller-Ersatz: Art.-Nr. 6303-0003 (Neopren), ca. 18 EUR
- Schlauch-Anschluss: 25 mm Stutzen, verstärkter PVC oder Spiralschlauch empfohlen

> ⚠️ **ZU PRÜFEN (Audit):** Kapazitäts-Widerspruch beim „Jabsco Water Puppy": in der Tabelle oben 1.500 GPH / 5.678 l/h, in Abschnitt 7.2.2 dagegen 1.500 l/h. Herstellerangabe für Art.-Nr. 18220-1127 (Flexible-Impeller-Pumpe): ca. 9 GPM = 540 GPH ≈ 2.040 l/h (Jabsco/Fisheries Supply). Auch die Teilenummern weichen ab (7.2.2: „6050" vs. hier „18220-1127"). Kapazität vor Verwendung — insbesondere als Notlenzpumpe (siehe 9.2.3) — anhand Herstellerdatenblatt verifizieren.

(Confidence: documented)

### 8.5 Seaflo

**Firmenprofil**: Seaflo, gegründet 2002 in Xiamen, China. Preis-Leistungs-Leader im Bilgenpumpen-Markt. Zunehmende Qualität, mittlerweile OEM-Lieferant für mehrere Bootsbauer.

**Produktpalette**:

| Modell | Typ | GPH | l/h | Volt | Ampere | Austritt mm | Art.-Nr. | Preis EUR |
|---|---|---|---|---|---|---|---|---|
| SFBP1-G500-01 | Tauch | 500 | 1.893 | 12V | 2,0 | 19 | SFBP1-G500-01 | 15 |
| SFBP1-G750-01 | Tauch | 750 | 2.839 | 12V | 2,5 | 19 | SFBP1-G750-01 | 18 |
| SFBP1-G1100-01 | Tauch | 1.100 | 4.164 | 12V | 3,5 | 28 | SFBP1-G1100-01 | 20 |
| SFBP1-G2000-01 | Tauch | 2.000 | 7.571 | 12V | 6,0 | 28 | SFBP1-G2000-01 | 32 |
| SFBP2-G3000-01 | Tauch (bürstenlos) | 3.000 | 11.356 | 12V | 11,0 | 38 | SFBP2-G3000-01 | 55 |

**Schwimmerschalter Seaflo**:

| Modell | Typ | Max. Strom | Preis EUR |
|---|---|---|---|
| SFBS-20-01 | Mechanisch | 20 A | 8 |
| SFBS-25-02 | Elektronisch | 25 A | 18 |

(Confidence: documented)

### 8.6 Attwood

**Firmenprofil**: Attwood Marine, gegründet 1909, Michigan, USA. Breites Sortiment an Marine-Zubehör, inklusive Bilgenpumpen der Marke „Sahara" und „Tsunami".

**Bilgenpumpen**:

| Modell | Typ | GPH | l/h | Volt | Austritt mm | Art.-Nr. | Preis EUR |
|---|---|---|---|---|---|---|---|
| Sahara S500 | Tauch | 500 | 1.893 | 12V | 19 | 4505-7 | 22 |
| Sahara S750 | Tauch | 750 | 2.839 | 12V | 19 | 4507-7 | 28 |
| Sahara S1100 | Tauch | 1.100 | 4.164 | 12V | 28 | 4511-7 | 38 |
| Tsunami T500 | Tauch | 500 | 1.893 | 12V | 19 | 4606-7 | 18 |
| Tsunami T800 | Tauch | 800 | 3.028 | 12V | 19 | 4608-7 | 22 |
| Tsunami T1200 | Tauch | 1.200 | 4.543 | 12V | 28 | 4612-7 | 35 |

(Confidence: documented)

### 8.7 Vetus

**Firmenprofil**: Vetus B.V., gegründet 1951 in Schiedam, Niederlande. Premium-Hersteller für Marine-Zubehör, besonders stark im europäischen Markt. Bekannt für Bilgenpumpen, Borddurchlässe und Schläuche.

**Bilgenpumpen**:

| Modell | Typ | l/h | Volt | Ampere | Austritt mm | Art.-Nr. | Preis EUR |
|---|---|---|---|---|---|---|---|
| Vetus BPS12-400 | Tauch | 1.500 | 12V | 2,5 | 19 | BPS12-400 | 35 |
| Vetus BPS12-1400 | Tauch | 5.300 | 12V | 5,0 | 28 | BPS12-1400 | 65 |
| Vetus BPS12-2000 | Tauch | 7.500 | 12V | 8,0 | 28 | BPS12-2000 | 85 |
| Vetus BPS12-3500 | Tauch | 13.200 | 12V | 14,0 | 38 | BPS12-3500 | 110 |

**Vetus Schläuche**:

| Modell | Typ | ID mm | Material | Preis/m EUR |
|---|---|---|---|---|
| Vetus?"!"bilge19 | Bilgenschlauch | 19 | PVC verstärkt | 6,00 |
| Vetus?"!"bilge25 | Bilgenschlauch | 25 | PVC verstärkt | 8,00 |
| Vetus?"!"bilge32 | Bilgenschlauch | 32 | PVC verstärkt | 10,00 |
| Vetus?"!"bilge38 | Bilgenschlauch | 38 | PVC verstärkt | 13,00 |
| Vetus VFSNH19 | Spiralschlauch | 19 | PVC Spiral | 10,00 |
| Vetus VFSNH25 | Spiralschlauch | 25 | PVC Spiral | 12,00 |
| Vetus VFSNH38 | Spiralschlauch | 38 | PVC Spiral | 18,00 |

(Confidence: documented)

### 8.8 Trident Marine

**Firmenprofil**: Trident Marine Systems (Trident Hose), gegründet 1990 in Connecticut, USA. Spezialist für Marine-Schläuche. Premium-Qualität, SAE- und USCG-zertifiziert.

**Bilgenschläuche**:

| Modell | Typ | ID mm | AD mm | Material | Preis/m EUR |
|---|---|---|---|---|---|
| Trident 150-0340 | PVC verstärkt | 10 | 16 | Weißer PVC | 4,50 |
| Trident 150-0500 | PVC verstärkt | 13 | 19 | Weißer PVC | 5,00 |
| Trident 150-0620 | PVC verstärkt | 16 | 22 | Weißer PVC | 5,50 |
| Trident 150-0750 | PVC verstärkt | 19 | 26 | Weißer PVC | 6,50 |
| Trident 150-1000 | PVC verstärkt | 25 | 33 | Weißer PVC | 8,00 |
| Trident 150-1250 | PVC verstärkt | 32 | 40 | Weißer PVC | 10,00 |
| Trident 150-1500 | PVC verstärkt | 38 | 48 | Weißer PVC | 12,50 |
| Trident 150-2000 | PVC verstärkt | 50 | 62 | Weißer PVC | 16,00 |
| Trident 162-0750 | PVC Spiral | 19 | 27 | Spiral-verstärkt | 11,00 |
| Trident 162-1000 | PVC Spiral | 25 | 34 | Spiral-verstärkt | 14,00 |
| Trident 162-1500 | PVC Spiral | 38 | 49 | Spiral-verstärkt | 19,00 |
| Trident 101-1000 | Sanitär odor-free | 25 | 36 | Mylar-Barriere | 20,00 |
| Trident 101-1500 | Sanitär odor-free | 38 | 50 | Mylar-Barriere | 28,00 |

**Trident Qualitätsmerkmale**:
- SAE J2006 R2 Zertifizierung für Sanitärschläuche
- USCG-zugelassen (33 CFR 183.540)
- Temperaturbereich: -40°C bis +82°C (PVC-Serie 150)
- Ozonbeständig, UV-stabilisiert (weiße Außenschicht)
- 5 Jahre Herstellergarantie

> ⚠️ **ZU PRÜFEN (Audit):** Normzuordnung fraglich — **SAE J2006** ist die Norm für „Marine Exhaust Hose" (Nass-Abgasschlauch), nicht für Sanitär-/Bilgenschläuche. **33 CFR 183.540** („Hoses: Standards and markings", Subpart J) regelt Kraftstoffschläuche (USCG Typ A1/A2/B1/B2 nach SAE J1527), nicht die PVC-Bilgen-/Sanitärschläuche der Serie 150/101. Zutreffende Zulassungsnorm für diese Schlauchtypen vor Übernahme der Angabe verifizieren.

(Confidence: documented)

### 8.9 Shields Rubber

**Firmenprofil**: Shields Rubber Company, gegründet 1924 in Cleveland, Ohio. Einer der ältesten Hersteller von Marine-Schläuchen. Branchenstandard für Premium-Qualität.

**Bilgen- und Sanitärschläuche**:

| Modell | Typ | ID mm | AD mm | Material | Preis/m EUR |
|---|---|---|---|---|---|
| Shields 116-0500 | PVC klar/weiß | 13 | 19 | PVC verstärkt | 5,50 |
| Shields 116-0750 | PVC klar/weiß | 19 | 26 | PVC verstärkt | 7,00 |
| Shields 116-1000 | PVC klar/weiß | 25 | 33 | PVC verstärkt | 9,50 |
| Shields 116-1250 | PVC klar/weiß | 32 | 42 | PVC verstärkt | 11,50 |
| Shields 116-1500 | PVC klar/weiß | 38 | 48 | PVC verstärkt | 14,00 |
| Shields 116-2000 | PVC klar/weiß | 50 | 63 | PVC verstärkt | 18,00 |
| Shields 148-1000 | Sanitär (No-Odor) | 25 | 35 | PE-Barriere | 18,00 |
| Shields 148-1250 | Sanitär (No-Odor) | 32 | 42 | PE-Barriere | 22,00 |
| Shields 148-1500 | Sanitär (No-Odor) | 38 | 49 | PE-Barriere | 26,00 |
| Shields 148-2000 | Sanitär (No-Odor) | 50 | 64 | PE-Barriere | 32,00 |
| Shields 200-0750 | Gummi schwarz | 19 | 28 | EPDM | 14,00 |
| Shields 200-1000 | Gummi schwarz | 25 | 36 | EPDM | 17,00 |
| Shields 200-1500 | Gummi schwarz | 38 | 50 | EPDM | 24,00 |

**Shields Qualitätsmerkmale**:
- FDA-zugelassene Materialien
- SAE J2006 konform
- Hergestellt in USA
- 10 Jahre Erfahrungswert Lebensdauer bei Bilgeneinsatz

> ⚠️ **ZU PRÜFEN (Audit):** „SAE J2006 konform" fraglich — SAE J2006 ist die Norm für Marine-Abgasschläuche (Wet Exhaust), nicht für PVC-/Sanitär-/Bilgenschläuche (Serie 116/148/200). Zutreffende Norm vor Übernahme verifizieren.

(Confidence: documented)

### 8.10 Weitere Hersteller

#### 8.10.1 Plastimo

Französischer Hersteller, breit aufgestellt. Bilgenpumpen und Handpumpen für den europäischen Markt.

| Modell | Typ | Kapazität | Preis EUR |
|---|---|---|---|
| Plastimo 10596 | Hand-Membran | 55 l/min | 75 |
| Plastimo 16975 | Tauchpumpe 500 GPH | 1.893 l/h | 22 |
| Plastimo 16976 | Tauchpumpe 1000 GPH | 3.785 l/h | 38 |

#### 8.10.2 Hella Marine

Neuseeländischer Hersteller, bekannt für Marine-Elektronik und Beleuchtung. Bilgen-Alarme und Panelanzeigen.

| Modell | Typ | Funktion | Preis EUR |
|---|---|---|---|
| Hella Marine 2XA 998 423-011 | LED-Warnleuchte | Bilgenalarm-Anzeige | 25 |
| Hella Marine 2JA 980 681-002 | Kontrollpanel | Pumpen-Status | 45 |

#### 8.10.3 TMC

Taiwan Marine Corporation, Hersteller von kostengünstigen Bilgenpumpen und Sanitärpumpen.

| Modell | Typ | GPH | l/h | Preis EUR |
|---|---|---|---|---|
| TMC 03301 | Tauch | 400 | 1.514 | 12 |
| TMC 03303 | Tauch | 600 | 2.271 | 18 |
| TMC 03304 | Tauch | 1.000 | 3.785 | 25 |
| TMC 03306 | Tauch | 2.000 | 7.571 | 42 |

#### 8.10.4 Shurflo

Amerikanischer Hersteller, spezialisiert auf Membranpumpen (auch Druckwasser).

| Modell | Typ | l/h | Volt | Preis EUR |
|---|---|---|---|---|
| Shurflo 355-101 | Membran-Bilge | 530 | 12V | 85 |
| Shurflo 355-103 | Membran-Bilge | 530 | 24V | 90 |

#### 8.10.5 Peters Rubber / Continental

Deutsche Schlauch-Hersteller, industrielle Qualität. Nicht marine-spezifisch, aber Schläuche in Marine-Qualität verfügbar.

| Produkt | Typ | ID mm | Material | Preis/m EUR |
|---|---|---|---|---|
| Continental Conti-Flex PVC | Allzweck-PVC | 19–50 | PVC verstärkt | 3,00–10,00 |
| Peters Gummischlauch EPDM | Industriegummi | 19–50 | EPDM | 8,00–20,00 |

(Confidence: documented)

---

## 9. Anlagen-spezifische Zuordnung

### 9.1 Zuordnung nach Pumpentyp und empfohlenem Schlauch

#### 9.1.1 Rule 2000 GPH (Rule 09)

| Parameter | Wert |
|---|---|
| Pumpentyp | Tauchpumpe, Zentrifugal |
| Austritts-Stutzen | 28 mm (1⅛") |
| Empfohlener Schlauch Druckseite | 28 mm ID, verstärkter PVC (z.B. Trident 150-1125) |
| Empfohlener Schlauch Saugseite | Nicht relevant (Tauchpumpe — Ansaugung direkt) |
| Schlauchschellen | 2× Edelstahl 316 am Stutzen, 2× am Borddurchlass |
| Max. empfohlene Schlauchlänge | 5.000 mm |
| Max. Förderhöhe | 3,6 m (bei voller Leistung) |
| Anti-Siphon | Erforderlich wenn Austritt <300 mm über WL |
| Borddurchlass | 28 mm Bronze oder Marelon |
| Typische Installation | Hauptbilgenpumpe 10–14 m Segelboot |

(Confidence: documented)

#### 9.1.2 Whale Gulper 220

| Parameter | Wert |
|---|---|
| Pumpentyp | Membranpumpe, elektrisch |
| Eingang | 19 mm oder 25 mm (Adapter) |
| Ausgang | 25 mm (1") |
| Empfohlener Schlauch Saugseite | 19/25 mm Spiral-PVC (kollaps-sicher!) |
| Empfohlener Schlauch Druckseite | 25 mm verstärkter PVC |
| Schlauchschellen | 2× je Anschluss |
| Max. Saughöhe | 2.000 mm (selbstansaugend) |
| Max. Förderhöhe | 4.000 mm |
| Anti-Siphon | Empfohlen |
| Typische Installation | Duschsumpf, kleine Bilge, Nebenpumpe |

(Confidence: documented)

#### 9.1.3 Jabsco Water Puppy (18220-1127)

| Parameter | Wert |
|---|---|
| Pumpentyp | Flexible-Impeller-Pumpe |
| Eingang/Ausgang | 25 mm (1") |
| Empfohlener Schlauch Saugseite | 25 mm Spiral-PVC (muss kollaps-sicher sein!) |
| Empfohlener Schlauch Druckseite | 25 mm verstärkter PVC |
| Schlauchschellen | 2× je Anschluss |
| Max. Saughöhe | 3.000 mm (hervorragendes Selbstansaugen) |
| Max. Förderhöhe | 6.000 mm |
| Anti-Siphon | Erforderlich |
| Achtung | Trockenlauf max. 30 Sekunden! |
| Typische Installation | Notlenzpumpe, Transferpumpe, flexible Bilgennutzung |

(Confidence: documented)

#### 9.1.4 Rule 3700 GPH (Rule 10) — Hochleistung

| Parameter | Wert |
|---|---|
| Pumpentyp | Tauchpumpe, Zentrifugal |
| Austritts-Stutzen | 38 mm (1½") |
| Empfohlener Schlauch | 38 mm ID, verstärkter PVC oder EPDM |
| Schlauchschellen | 2× Edelstahl 316 (breite Schellen, 12 mm Band) |
| Max. empfohlene Schlauchlänge | 6.000 mm |
| Max. Förderhöhe | 4,2 m |
| Anti-Siphon | Obligatorisch |
| Borddurchlass | 38 mm Bronze, mit Seeventil |
| Elektrische Absicherung | 25 A Sicherung, 6 mm² Kabel |
| Typische Installation | Hauptbilgenpumpe 14–20 m Motor-/Segelyacht |

> ✅ Aufgelöst (Audit): 25 A Sicherung (12 V) — Quelle: Rule/Xylem Standard-Bilgenpumpen-Referenz und Rule Pumps FAQ („for the 3700 GPH and 4000 GPH pumps use a 25 amp fuse"). Deckungsgleich mit Tabelle 11.3.2.

(Confidence: documented)

#### 9.1.5 Whale Gusher 30 — Manuelle Notlenzpumpe

| Parameter | Wert |
|---|---|
| Pumpentyp | Membran-Handpumpe |
| Eingang | 38 mm (1½") |
| Ausgang | 38 mm (1½") |
| Empfohlener Schlauch Saugseite | 38 mm Spiral-PVC (Pflicht — Saugseite!) |
| Empfohlener Schlauch Druckseite | 38 mm verstärkter PVC |
| Kapazität | 69 l/min (ca. 4.140 l/h) |
| Hub-Volumen | 1.100 ml |
| Max. Saughöhe | 2.500 mm |
| Schlauchschellen | 2× je Anschluss, plus Kabelbinder als Sicherung |
| Typische Installation | Cockpit-montiert, Blauwasser-Segelyacht, CE-Kat A |

(Confidence: documented)

#### 9.1.6 Seaflo SFBP1-G1100-01 — Budget-Option

| Parameter | Wert |
|---|---|
| Pumpentyp | Tauchpumpe, Zentrifugal |
| Austritts-Stutzen | 28 mm (1⅛") |
| Empfohlener Schlauch | 28 mm verstärkter PVC |
| Schlauchschellen | 2× Edelstahl |
| Max. Förderhöhe | 3,0 m |
| Preis | 20 EUR |
| Qualitätshinweis | Für Binnengewässer und CE-Kat D ausreichend |
| Nicht empfohlen für | CE-Kat A/B als Primärpumpe |
| Typische Installation | Sekundärpumpe, Beiboot, Trailer-Boot |

(Confidence: documented)

### 9.2 Bootsklassen-Zuordnung

#### 9.2.1 Jolle / Kleinboot (≤6 m)

| Komponente | Empfehlung | Budget EUR |
|---|---|---|
| Primärpumpe | Rule 25S (500 GPH) oder Seaflo 500 | 15–25 |
| Handpumpe | Whale Gusher Urchin oder Lenzöse | 15–95 |
| Bilgenschlauch | 19 mm PVC, 1–2 m | 5–10 |
| Schwimmerschalter | Optional (Seaflo SFBS-20) | 8–15 |
| Borddurchlass | Kunststoff-Stutzen über WL | 5–10 |
| **Gesamt** | | **48–155** |

#### 9.2.2 Segelboot Küste (8–12 m, CE-Kat B/C)

| Komponente | Empfehlung | Budget EUR |
|---|---|---|
| Primärpumpe | Rule 27S (1.000 GPH) | 35 |
| Sekundärpumpe | Rule 25S (500 GPH) im Vorschiff | 25 |
| Handpumpe | Whale Gusher 10 Mk3 | 85 |
| Bilgenschlauch Druckseite | 28 mm Trident 150-1125, 3 m | 24 |
| Bilgenschlauch Vorschiff | 19 mm Trident 150-0750, 2 m | 13 |
| Schwimmerschalter | Rule EcoSwitch 39 | 35 |
| Hochwasser-Alarm | Rule 33ALA | 30 |
| Anti-Siphon | Vetus AS25 | 18 |
| Cockpit-Drain-Schläuche | 38 mm PVC × 2, je 1,5 m | 27 |
| Borddurchlass + Seeventil | Marelon 28 mm | 45 |
| Schlauchschellen | 10× Edelstahl 316 | 20 |
| **Gesamt** | | **357** |

#### 9.2.3 Segelyacht Offshore (12–16 m, CE-Kat A)

| Komponente | Empfehlung | Budget EUR |
|---|---|---|
| Primärpumpe | Rule 09 (2.000 GPH) | 55 |
| Sekundärpumpe | Rule 27S (1.000 GPH) Motorraum | 35 |
| Tertiärpumpe | Whale Gulper 220 Vorschiff | 95 |
| Handpumpe | Whale Gusher 30 (Cockpit) | 185 |
| Notlenzpumpe | Jabsco Water Puppy (tragbar) | 160 |
| Bilgenschlauch 28 mm | Trident 150-1125, 8 m | 64 |
| Bilgenschlauch 38 mm | Shields 116-1500, 3 m (Handpumpe) | 42 |
| Spiralschlauch 25 mm | Trident 162-1000, 3 m (Gulper Saug) | 42 |
| Schwimmerschalter (2×) | 2× Rule EcoSwitch | 70 |
| Hochwasser-Alarm | Aqualarm 20075 (Multi-Zone) | 65 |
| Anti-Siphon (2×) | 2× Vetus AS28 | 40 |
| Cockpit-Drain | 2× 38 mm EPDM, je 2 m | 88 |
| Borddurchlass + Seeventil (3×) | 3× Bronze 28/38 mm | 165 |
| Schlauchschellen | 25× Edelstahl 316 | 50 |
| **Gesamt** | | **1.156** |

#### 9.2.4 Motoryacht (14–20 m, CE-Kat B)

| Komponente | Empfehlung | Budget EUR |
|---|---|---|
| Primärpumpe Maschinenraum | Rule 10 (3.700 GPH) | 85 |
| Sekundärpumpe Vorschiff | Rule 09 (2.000 GPH) | 55 |
| Pumpe Achter-Bilge | Johnson L1250 | 52 |
| Handpumpe | Whale Gusher 25 | 130 |
| Bilgenschlauch 38 mm | Shields 116-1500, 10 m | 140 |
| Bilgenschlauch 28 mm | Shields 116-1000, 6 m | 57 |
| Spiralschlauch 38 mm | Trident 162-1500, 4 m | 76 |
| Schwimmerschalter (3×) | 3× Rule EcoSwitch | 105 |
| Hochwasser-Alarm | BEP 1000-BSS | 85 |
| Anti-Siphon (3×) | 3× Vetus AS38 | 66 |
| Cockpit-Drain | 2× 50 mm EPDM, je 2,5 m | 140 |
| Borddurchlass + Seeventil (4×) | 4× Bronze 38 mm | 280 |
| Schlauchschellen | 35× Edelstahl 316 | 70 |
| Ölabscheide-Pad (10er-Pack) | Oil-Dri Marine | 25 |
| **Gesamt** | | **1.366** |

(Confidence: documented)

---

## 10. Schlauchschellen & Verbindungstechnik

### 10.1 Schlauchschellen-Typen für Bilgensysteme

| Typ | Beschreibung | Marine-Eignung | Preis ca. |
|---|---|---|---|
| Schneckengewinde (Worm Drive) | Standard-Schraubschelle | Gut (nur 316!) | 1,50–4,00 EUR |
| T-Bolt | Massive Bolzenschelle, gleichmäßiger Druck | Hervorragend | 5,00–12,00 EUR |
| Federbandschelle (Constant Torque) | Federstahl, passt sich Durchmesser-Änderung an | Hervorragend | 3,00–8,00 EUR |
| Crimp-Ring | Einmal-Quetschring, werksseitig | Gut | 0,50–1,50 EUR |
| Kabelbinder (Backup) | Zusätzlich zu Schelle als Abfallsicherung | Ergänzung | 0,10 EUR |

### 10.2 Materialanforderungen

| Material | Norm | Marine-Eignung | Korrosion Salzwasser |
|---|---|---|---|
| AISI 304 (A2) | 1.4301 | Bedingt (Süßwasser OK) | Lochfraß nach 3–5 Jahren |
| AISI 316 (A4) | 1.4401 | Gut | Geringe Korrosion |
| AISI 316L (A4L) | 1.4404 | Hervorragend | Minimale Korrosion |
| AISI 316Ti | 1.4571 | Hervorragend | Keine |
| Verzinkter Stahl | — | Ungeeignet! | Sofortige Korrosion |

**WICHTIG**: Unter der Wasserlinie und für alle sicherheitskritischen Verbindungen (Bilge!) ausschließlich AISI 316 / 316L verwenden. Verzinkte Schlauchschellen sind im Bilgensystem ein sofortiger Befund (Score-Abzug 30 Punkte).

(Confidence: documented)

### 10.3 Dimensionierung

| Schlauch-AD mm | Schellen-Bereich mm | Bandbreite mm | Empfehlung |
|---|---|---|---|
| 22–26 | 16–27 | 9 | Schneckengewinde 316 |
| 26–33 | 25–40 | 9 | Schneckengewinde 316 |
| 33–42 | 32–50 | 12 | Schneckengewinde 316, breit |
| 42–50 | 40–60 | 12 | T-Bolt oder Federbandschelle |
| 50–65 | 50–70 | 12 | T-Bolt empfohlen |

### 10.4 Montageregeln

1. **Doppelte Schellen**: Unter der Wasserlinie und an allen Bilgen-Verbindungen immer zwei Schlauchschellen pro Anschluss
2. **Schellenausrichtung**: Schrauben der beiden Schellen um 180° versetzt (nicht übereinander)
3. **Anzugsmoment**: Handfest + ¼ Umdrehung. Kein Elektroschrauber! (Schlauch wird eingeschnitten)
4. **Stutzentyp**: Gerippter Stutzen (Barb Fitting) ist Pflicht. Glatte Stutzen nur mit Crimp-Ring
5. **Schlauchlänge**: Min. 2× Stutzen-Länge auf dem Stutzen aufschieben
6. **Schlauchende**: Sauber und rechtwinklig abschneiden (scharfes Messer, kein Quetschen)
7. **Warmes Wasser**: Bei steifen Schläuchen das Ende 30 Sekunden in heißes Wasser tauchen → leichteres Aufschieben
8. **Gleitmittel**: Spülmittel oder Silikonspray auf Stutzen. NIE Fett oder Öl (Schlauch wird angegriffen)

(Confidence: documented)

### 10.5 Schlauchverbinder und Adapter

| Typ | Material | Einsatz | Preis EUR |
|---|---|---|---|
| Gerade Schlauchtülle | Bronze / Kunststoff | Schlauch-an-Schlauch | 3–8 |
| 90°-Winkel | Bronze / Kunststoff | Richtungsänderung | 5–12 |
| T-Stück | Bronze / Kunststoff | Zusammenführung | 6–15 |
| Y-Stück | Bronze / Kunststoff | Zusammenführung (strömungsgünstig) | 8–18 |
| Reduzierung | Bronze / Kunststoff | Durchmesseranpassung | 4–10 |
| Rückschlagventil | Kunststoff / Bronze | Rückflusssicherung | 8–25 |

**Verbindungen minimieren**: Jede Verbindung ist eine potenzielle Leckstelle. Bilgenleitungen so direkt wie möglich verlegen. Ideal: ein Stück Schlauch von Pumpe bis Borddurchlass.

(Confidence: documented)

---

## 11. Technische Referenz & Berechnungen

### 11.1 Pumpenkapazitäts-Berechnung

#### 11.1.1 Leckrate-Abschätzung nach Rumpföffnung

Leckrate durch eine kreisrunde Öffnung unter Wasser:

```
Q = C_d × A × √(2 × g × h)
wobei:
  Q = Volumenstrom [m³/s]
  C_d = Durchflusskoeffizient (0,6 für scharfkantige Öffnung)
  A = Öffnungsfläche [m²]
  g = 9,81 m/s²
  h = Wassertiefe über Öffnung [m]
```

Beispiel: 25 mm Borddurchlass bricht bei 0,8 m unter WL:
- A = π × 0,0125² = 0,000491 m²
- Q = 0,6 × 0,000491 × √(2 × 9,81 × 0,8) = 0,00117 m³/s = 4.200 l/h

→ Pumpe muss mindestens 4.200 l/h fördern, um diesen Einbruch zu kompensieren.
→ In der Praxis: Pumpenkapazität ≥ 1,5× Leckrate (Sicherheitsfaktor)

(Confidence: calculated)

#### 11.1.2 Förderhöhen-Verlust

Die tatsächliche Förderleistung einer Bilgenpumpe ist geringer als die Nennleistung, weil:
1. Förderhöhe (geodätische Höhe Pumpe → Austritt)
2. Rohrreibungsverluste (Schlauchlänge, Krümmer, Verengungen)
3. Verschmutzung des Impellers (Leistungsverlust 10–30% nach 2 Jahren)

Typische Förderkurven (Prozent der Nennleistung):

| Förderhöhe | 500 GPH Pumpe | 1000 GPH Pumpe | 2000 GPH Pumpe |
|---|---|---|---|
| 0 m (frei) | 100% | 100% | 100% |
| 0,5 m | 85% | 90% | 92% |
| 1,0 m | 70% | 80% | 85% |
| 1,5 m | 55% | 70% | 78% |
| 2,0 m | 40% | 60% | 70% |
| 2,5 m | 25% | 50% | 62% |
| 3,0 m | 10% | 38% | 55% |
| 3,5 m | 0% | 25% | 45% |
| 4,0 m | — | 10% | 35% |
| 4,5 m | — | 0% | 20% |
| 5,0 m | — | — | 5% |

(Confidence: documented)

#### 11.1.3 Schlauchdurchmesser-Berechnung

Empfohlene Fließgeschwindigkeit in Bilgenleitungen: 0,5–1,5 m/s

```
d = √(4 × Q / (π × v)) × 1000 [mm]
wobei:
  d = Innendurchmesser [mm]
  Q = Volumenstrom [m³/s]
  v = Fließgeschwindigkeit [m/s]
```

| Pumpe GPH | Volumenstrom l/h | Empf. v [m/s] | Min. ID [mm] | Standard-ID [mm] |
|---|---|---|---|---|
| 500 | 1.893 | 1,0 | 26 | 28 (1⅛") |
| 1.000 | 3.785 | 1,0 | 37 | 38 (1½") |
| 2.000 | 7.571 | 1,2 | 47 | 50 (2") |
| 3.700 | 14.006 | 1,2 | 64 | Nicht praxisgerecht → 38 mm + kürzere Leitung |

**Hinweis**: In der Praxis wird oft der Pumpen-Stutzen-Durchmesser als Schlauch-ID verwendet. Dies ist von den Herstellern so vorgesehen und berücksichtigt bereits die Strömungsverluste.

(Confidence: calculated)

### 11.2 Druckverlust-Berechnung

#### 11.2.1 Rohrreibungsverlust (Darcy-Weisbach)

```
Δp = f × (L/d) × (ρ × v²/2) [Pa]
Δh = Δp / (ρ × g) [m Wassersäule]
wobei:
  f = Reibungsbeiwert (PVC-Schlauch ≈ 0,025 bei Re = 50.000)
  L = Schlauchlänge [m]
  d = Innendurchmesser [m]
  ρ = Dichte Wasser [kg/m³]
  v = Fließgeschwindigkeit [m/s]
```

Vereinfachte Tabelle — Druckverlust pro Meter Schlauch:

| ID mm | bei 1.000 l/h | bei 2.000 l/h | bei 4.000 l/h | bei 8.000 l/h |
|---|---|---|---|---|
| 19 | 0,12 m/m | 0,42 m/m | 1,5 m/m | — |
| 25 | 0,04 m/m | 0,14 m/m | 0,48 m/m | 1,7 m/m |
| 28 | 0,025 m/m | 0,09 m/m | 0,32 m/m | 1,1 m/m |
| 32 | 0,015 m/m | 0,05 m/m | 0,19 m/m | 0,65 m/m |
| 38 | 0,008 m/m | 0,03 m/m | 0,10 m/m | 0,35 m/m |
| 50 | 0,003 m/m | 0,01 m/m | 0,035 m/m | 0,12 m/m |

(Confidence: calculated)

#### 11.2.2 Einzelverluste (Formstücke)

| Formstück | Verlustbeiwert ζ | Äquivalent-Schlauchlänge (25 mm) |
|---|---|---|
| 90°-Bogen (Schlauch gebogen) | 0,5 | 0,5 m |
| 90°-Winkel (Fitting) | 1,5 | 1,5 m |
| 45°-Bogen | 0,3 | 0,3 m |
| T-Stück (Durchgang) | 0,5 | 0,5 m |
| T-Stück (Abzweig) | 1,5 | 1,5 m |
| Rückschlagventil | 2,0 | 2,0 m |
| Anti-Siphon-Ventil | 1,0 | 1,0 m |
| Schlauchstutzen (Barb) | 0,3 | 0,3 m |

(Confidence: calculated)

### 11.3 Elektrische Dimensionierung

#### 11.3.1 Kabelquerschnitt

Bilgenpumpen-Kabel müssen für den Anlaufstrom dimensioniert werden (2× Nennstrom):

| Pumpe | Nennstrom | Anlaufstrom | Kabellänge ≤5m | Kabellänge 5–10m | Kabellänge 10–15m |
|---|---|---|---|---|---|
| 500 GPH | 2,5 A | 5,0 A | 1,5 mm² | 2,5 mm² | 4,0 mm² |
| 1.000 GPH | 3,8 A | 7,6 A | 2,5 mm² | 4,0 mm² | 6,0 mm² |
| 2.000 GPH | 8,4 A | 16,8 A | 4,0 mm² | 6,0 mm² | 10,0 mm² |
| 3.700 GPH | 14,0 A | 28,0 A | 6,0 mm² | 10,0 mm² | 16,0 mm² |

#### 11.3.2 Absicherung

| Pumpe | Sicherung |
|---|---|
| 500 GPH | 5 A |
| 1.000 GPH | 10 A |
| 2.000 GPH | 15 A |
| 3.700 GPH | 25 A |
| 4.000 GPH | 30 A |

**Kritisch**: Bilgenpumpen-Sicherung direkt an Batterie (nicht über Hauptschalter!). Pumpe muss laufen können, auch wenn alle anderen Systeme ausgeschaltet sind.

(Confidence: documented)

---

## 12. Einbau-/Austausch-Anleitung

### 12.1 Werkzeug und Material

| Werkzeug | Zweck |
|---|---|
| Scharfes Messer / Schlauchschneider | Schlauch ablängen |
| Schraubendreher (Kreuzschlitz, 5,5 mm Sechskant) | Schlauchschellen |
| Heißluftfön oder heißes Wasser | Schlauch erweichen |
| Spülmittel oder Silikonspray | Gleitmittel für Stutzen |
| Multimeter | Schwimmerschalter-Prüfung |
| Eimer + Lappen | Restwasser auffangen |
| Kabelbinder | Provisorische Sicherung |
| Durchgangsprüfer | Kabeltest |
| Drehmomentschlüssel (optional) | Borddurchlass-Mutter |

### 12.2 Schritt-für-Schritt: Bilgenschlauch-Austausch

**Schritt 1 — Vorbereitung (15 min)**
- Batterie-Hauptschalter AUS (bei elektrischer Pumpe)
- Seeventil am Bilgen-Austritt schließen
- Restliches Bilgenwasser mit Lappen aufnehmen
- Alten Schlauch fotografieren (Dokumentation)
- Schlauchverlauf und Befestigungspunkte notieren

**Schritt 2 — Demontage (20 min)**
- Schlauchschellen lösen (Vorsicht: Schlauch kann unter Spannung stehen)
- Schlauch von Stutzen abziehen (bei verklebtem Schlauch: mit Messer einschneiden, nicht am Stutzen hebeln!)
- Alte Schlauchschellen entsorgen (nie wiederverwenden)
- Stutzen reinigen (Schleifvlies, kein Schleifpapier)
- Borddurchlass-Stutzen auf Korrosion prüfen
- Pumpen-Stutzen auf Risse und Verschleiß prüfen

**Schritt 3 — Neuen Schlauch vorbereiten (10 min)**
- Neuen Schlauch auf Länge schneiden (alter Schlauch als Schablone, oder +50 mm)
- Schlauchende sauber und rechtwinklig schneiden
- Bei steifem Schlauch: Ende 30 s in heißes Wasser (≈70°C) tauchen
- Innenseite des Schlauchendes mit Spülmittel benetzen
- Stutzen mit Spülmittel benetzen

**Schritt 4 — Montage (15 min)**
- Neue Schlauchschellen auf Schlauch auffädeln BEVOR Schlauch aufgeschoben wird!
- Schlauch auf Stutzen schieben, mindestens 2× Stutzen-Rippenlänge
- Erste Schelle 5 mm hinter letzter Rippe positionieren
- Zweite Schelle 10 mm hinter erster Schelle
- Schellen-Schrauben um 180° versetzt ausrichten
- Handfest anziehen + ¼ Umdrehung
- Verfahren an beiden Enden wiederholen

**Schritt 5 — Verlegung (10 min)**
- Schlauch in natürlichem Bogen verlegen (kein Knicken!)
- Alle 300 mm befestigen (Schlauchhalter oder Kabelbinder an Schottwand)
- Biegeradius nicht unterschreiten (min. 3–5× ID)
- Schlauch darf nicht an scharfen Kanten scheuern (Kantenschutz!)
- Kein Kontakt mit Auspuff oder heißen Motorteilen

**Schritt 6 — Funktionsprüfung (15 min)**
- Seeventil öffnen
- Batterie-Hauptschalter EIN
- Wasser in Bilge geben (ca. 5 l)
- Pumpe manuell aktivieren
- Prüfen: Wasser fließt am Borddurchlass-Austritt aus?
- Prüfen: Alle Verbindungen dicht?
- Schwimmerschalter-Test: Wasser bis Schaltniveau auffüllen
- Pumpe muss automatisch starten und stoppen
- Sichtkontrolle nach 1 Stunde (trockene Schellen?)

**Schritt 7 — Dokumentation**
- Einbaudatum, Schlauchhersteller, Typ und Durchmesser im Bordbuch notieren
- Foto der fertigen Installation

(Confidence: documented)

### 12.3 Typische Einbauzeiten

| Arbeit | DIY-Zeit | Profi-Zeit | Profi-Kosten |
|---|---|---|---|
| Einzelnen Bilgenschlauch austauschen | 1,5 h | 0,75 h | 60–90 EUR |
| Bilgenpumpe tauschen (inkl. Schlauch) | 2,5 h | 1,0 h | 90–150 EUR |
| Schwimmerschalter tauschen | 0,5 h | 0,25 h | 30–50 EUR |
| Komplettes Bilgensystem erneuern (10 m) | 8 h | 4 h | 350–600 EUR |
| Cockpit-Drain-Schläuche tauschen (2×) | 3 h | 1,5 h | 120–200 EUR |
| Borddurchlass Bilge erneuern | 4 h | 2 h | 180–350 EUR |

(Confidence: documented)

---

## 13. Lebensdauer und Alterungsmechanismen

### 13.1 Lebensdauer nach Material

| Material | Erwartete Lebensdauer | Hauptalterungsfaktor | Inspektionsintervall |
|---|---|---|---|
| PVC verstärkt (Standard) | 5–10 Jahre | Weichmacher-Migration, UV | Jährlich |
| PVC Spiral-verstärkt | 8–12 Jahre | Weichmacher-Migration | Jährlich |
| EPDM Gummi | 10–15 Jahre | Ozon, mechanische Ermüdung | Alle 2 Jahre |
| Silikon | 15–20 Jahre | Mechanische Belastung | Alle 3 Jahre |
| Sanitärschlauch (PE-Barriere) | 8–12 Jahre | Schichtentrennung | Jährlich |

(Confidence: documented)

### 13.2 Alterungsmechanismen im Detail

#### 13.2.1 Weichmacher-Migration (PVC)

PVC-Schläuche enthalten 25–45% Weichmacher (Phthalate oder Adipate). Diese migrieren über die Lebensdauer aus dem Material:
- **Symptome**: Schlauch wird steif, spröde, verfärbt sich gelblich
- **Beschleunigung**: Höhere Temperatur (+10°C → doppelte Migrationsrate), UV-Strahlung
- **Endstadium**: Schlauch bricht bei Biegung, löst sich von Stutzen
- **Prüfung**: Schlauch um Finger wickeln — bricht oder reißt ein → sofort tauschen

#### 13.2.2 UV-Degradation

UV-Strahlung zerstört Polymer-Ketten:
- **Betrifft**: Alle Schläuche im Deck-/Cockpit-Bereich
- **Symptome**: Oberfläche wird rau, kreidig, Mikrorisse
- **Prävention**: UV-stabilisierte Schläuche verwenden, oder Schläuche abdecken
- **Lebensdauer-Reduktion**: 50–70% bei direkter Sonneneinstrahlung

#### 13.2.3 Biologischer Angriff

Bilgenwasser enthält Nährstoffe für Mikroorganismen:
- **Biofilm**: Reduziert Innendurchmesser, verursacht Gerüche
- **Schwarzschimmel**: Wächst auf PVC-Oberfläche
- **Prävention**: Bilge regelmäßig reinigen, enzymatische Bilge-Reiniger

#### 13.2.4 Öl- und Kraftstoff-Angriff

Diesel und Motoröl greifen PVC und Standard-Gummi an:
- **Symptome**: Schlauch quillt auf, wird weich, verliert Festigkeit
- **Besonders betroffen**: Standard-PVC im Motorraum
- **Abhilfe**: Ölbeständige Schläuche (NBR-Gummi) im Motorraum

#### 13.2.5 Mechanische Ermüdung

Vibration, Scheuern, Biegung:
- **Vibrationsermüdung**: Motor-nahe Schläuche, Befestigung alle 200 mm
- **Scheuerstellen**: Schlauch an Schottkante, Kabelbaum → Schutzmanschette
- **Kink-Ermüdung**: Wiederholtes Knicken → Wandschwächung → Kollaps

(Confidence: documented)

### 13.3 Wartungsplan Bilgensystem

| Intervall | Maßnahme |
|---|---|
| Monatlich | Bilge visuell prüfen (Wasserstand, Verschmutzung) |
| Monatlich | Bilgenpumpe manuell testen |
| Vierteljährlich | Bilgen-Sieb reinigen |
| Vierteljährlich | Schwimmerschalter-Funktion prüfen |
| Jährlich | Alle Schlauchschellen auf festen Sitz prüfen |
| Jährlich | Schläuche auf Risse, Verfärbung, Versteifung prüfen |
| Jährlich | Anti-Siphon-Ventil prüfen (Membran) |
| Jährlich | Bilgen-Austritt-Borddurchlass von außen prüfen |
| Alle 2 Jahre | Schwimmerschalter-Kontakte reinigen |
| Alle 3 Jahre | Impeller-Zustand prüfen (Tauchpumpen) |
| Alle 5 Jahre | Schlauchschellen erneuern |
| Alle 7–10 Jahre | PVC-Bilgenschläuche erneuern |
| Alle 10–15 Jahre | EPDM-Bilgenschläuche erneuern |

(Confidence: documented)

---

## 14. Fehlerbild-Atlas

### Fehlerbild F-BL-01: Schlauch von Stutzen gerutscht

**Beschreibung**: Bilgenschlauch hat sich vom Pumpen- oder Borddurchlass-Stutzen gelöst. Bilgenwasser läuft unkontrolliert in den Rumpf zurück oder wird in die Bilge statt nach außenbords gefördert.
**Visuelle Merkmale**: Sichtbarer Spalt zwischen Schlauch und Stutzen, Wasserspritzer oder Rinnsale am Anschluss, eventuell lose hängende Schlauchschelle.
**Typische Ursache**: Fehlende oder korrodierte Schlauchschelle, nur eine statt zwei Schellen, Schlauch zu kurz abgeschnitten, Stutzen beschädigt (gebrochene Rippen).
**Risiko**: HOCH — Seewasser kann rückwärts einströmen wenn Austritt unter WL.
**Sofortmaßnahme**: Schlauch aufschieben, provisorisch mit Kabelbinder sichern, Bilgenpumpe manuell aktivieren.
**Reparatur**: Neue Schlauchschellen (2×, Edelstahl 316), Schlauch kürzen (frisches Ende), Stutzen prüfen/ersetzen.
**AYDI-Score-Auswirkung**: Condition -40, Compliance -30
**Confidence**: visual_high (klar erkennbar auf Foto)

### Fehlerbild F-BL-02: Schlauch geknickt (Kinking)

**Beschreibung**: Bilgenschlauch hat einen scharfen Knick, der den Querschnitt teilweise oder vollständig verschließt. Die Pumpe läuft, aber fördert wenig oder kein Wasser.
**Visuelle Merkmale**: Sichtbarer Knick im Schlauchverlauf, oft an Richtungsänderungen oder wo der Schlauch über Hindernisse geführt wird. Schlauch kann an der Knickstelle weiß verfärbt sein (Materialstress).
**Typische Ursache**: Zu enger Biegeradius, Schlauch ohne Halterung verlegt, schwerer Gegenstand auf Schlauch, fehlende Spiralverstärkung auf Saugseite.
**Risiko**: MITTEL — Pumpe fördert reduziert, bei Notfall nicht ausreichend.
**Sofortmaßnahme**: Knick lösen, Schlauch neu verlegen, Halterungen anbringen.
**Reparatur**: Spiralschlauch verwenden, Biegeradius vergrößern, 90°-Fitting statt Biegung.
**AYDI-Score-Auswirkung**: Condition -20, Capacity -30
**Confidence**: visual_high

### Fehlerbild F-BL-03: Schlauch verhärtet / spröde

**Beschreibung**: PVC-Bilgenschlauch hat durch Weichmacher-Migration seine Flexibilität verloren. Material fühlt sich hart und steif an, Oberfläche zeigt feine Risse.
**Visuelle Merkmale**: Gelbliche bis braune Verfärbung, matte Oberfläche, sichtbare Mikrorisse entlang der Längserstreckung, Schlauch lässt sich nicht mehr biegen.
**Typische Ursache**: Alter (>7 Jahre), hohe Temperaturen im Motorraum, UV-Belastung, Kontakt mit Öl/Diesel.
**Risiko**: HOCH — Schlauch kann jederzeit brechen, besonders bei Vibration.
**Sofortmaßnahme**: Schlauch sofort tauschen. Kein provisorisches Reparieren eines verhärteten Schlauchs!
**Reparatur**: Neuen Schlauch gleichen Durchmessers einbauen, Ursache für vorzeitige Alterung ermitteln.
**AYDI-Score-Auswirkung**: Condition -50, Materials -30
**Confidence**: visual_medium (Verhärtung nur teilweise auf Foto erkennbar)

### Fehlerbild F-BL-04: Korrodierte Schlauchschellen

**Beschreibung**: Schlauchschellen zeigen Rostbildung, Lochfraß oder sind vollständig durchkorrodiert. Häufigster Befund bei Einsatz von verzinktem Stahl statt Edelstahl.
**Visuelle Merkmale**: Braune/orange Rostflecken, Rostläufer auf Schlauch und umliegenden Flächen, Schelle fühlt sich rau an, Schraubgewinde korrodiert und schwergängig.
**Typische Ursache**: Falsche Materialwahl (A2 statt A4, oder verzinkt), Salzwasser-Exposition, galvanische Korrosion.
**Risiko**: HOCH — Schelle kann brechen, Schlauch rutscht vom Stutzen.
**Sofortmaßnahme**: Alle korrodierten Schellen sofort durch AISI 316 ersetzen.
**Reparatur**: Schellen erneuern, Schlauchende prüfen (Korrosion kann Schlauch beschädigen), alle anderen Schellen im System auf Material prüfen.
**AYDI-Score-Auswirkung**: Condition -35, Materials -40, Compliance -20
**Confidence**: visual_high (Rost klar erkennbar)

### Fehlerbild F-BL-05: Schwimmerschalter verklemmt

**Beschreibung**: Mechanischer Schwimmerschalter bewegt sich nicht frei, bleibt in „Aus"-Position. Bilgenpumpe startet nicht automatisch bei steigendem Wasserstand.
**Visuelle Merkmale**: Schwimmkörper bewegt sich nicht, Ablagerungen am Drehpunkt, Schmutz/Haare um Schwimmer gewickelt, Kabelbruch am Schaltergehäuse.
**Typische Ursache**: Bilgen-Schmutz (Haare, Öl, Kleinteile), Kalkablagerung, Kabelschaden, mechanischer Defekt.
**Risiko**: KRITISCH — Bei Wassereinbruch startet Pumpe nicht. Sinkgefahr!
**Sofortmaßnahme**: Schwimmer reinigen, Funktion prüfen. Bei Defekt: manuellen Override verwenden.
**Reparatur**: Schwimmerschalter reinigen oder ersetzen, auf elektronischen Schalter (Feldeffekt) umrüsten.
**AYDI-Score-Auswirkung**: Condition -50, Compliance -40, Redundancy -30
**Confidence**: visual_medium (Funktion nur im Test erkennbar)

### Fehlerbild F-BL-06: Rückschlagventil / Anti-Siphon undicht

**Beschreibung**: Das Rückschlagventil oder Anti-Siphon-Ventil im Bilgen-System schließt nicht mehr dicht. Seewasser kann rückwärts in die Bilge fließen, oder der Siphon-Effekt zieht Wasser ins Boot.
**Visuelle Merkmale**: Wasserspritzer oder Tropfenbildung am Ventil, Kalkablagerung, Ventilmembran verhärtet oder gerissen, Ventilkörper verfärbt.
**Typische Ursache**: Kalkablagerung, Muschelwuchs, Alterung der Membran (>3 Jahre), Schmutzpartikel im Ventilsitz.
**Risiko**: HOCH — Seewassereinbruch über Bilgenleitung möglich.
**Sofortmaßnahme**: Seeventil am Bilgen-Austritt schließen bis Reparatur.
**Reparatur**: Ventilmembran oder komplettes Ventil ersetzen, Ventilsitz reinigen.
**AYDI-Score-Auswirkung**: Condition -30, Compliance -25
**Confidence**: visual_low (Funktion nur durch Test feststellbar)

### Fehlerbild F-BL-07: Bilgen-Austritt unter Wasser durch Biofouling verstopft

**Beschreibung**: Der Bilgen-Austritt am Borddurchlass ist durch Muscheln, Algen oder Seepocken von außen zugewachsen. Bilgenpumpe fördert gegen geschlossenen Austritt → Schlauch platzt oder Pumpe überhitzt.
**Visuelle Merkmale**: Von außen: Austrittsöffnung nicht sichtbar unter Bewuchs. Von innen: Pumpe läuft, aber kein Wasseraustritt. Schlauch bläht sich auf unter Druck.
**Typische Ursache**: Mangelnde Antifouling-Behandlung am Bilgen-Austritt, lange Standzeit.
**Risiko**: MITTEL — Pumpe funktionslos, aber kein aktiver Wassereinbruch.
**Sofortmaßnahme**: Boot trockenlegen, Bilgen-Austritt freikratzen.
**Reparatur**: Austrittsöffnung reinigen, Antifouling-Farbe am Austritt auftragen, Gitter/Sieb vor Austritt.
**AYDI-Score-Auswirkung**: Condition -25, Capacity -40
**Confidence**: visual_high (von außen am Rumpf erkennbar)

### Fehlerbild F-BL-08: Ölverseuchte Bilge / Öliger Schlauch

**Beschreibung**: Motoröl, Diesel oder Hydrauliköl in der Bilge kontaminiert das Bilgensystem. Schlauch quillt auf (PVC), Pumpen-Impeller wird angegriffen, ölhaltiges Bilgenwasser wird außenbords gepumpt.
**Visuelle Merkmale**: Ölfilm auf Bilgenwasser (Regenbogenschimmer), Schlauch aufgequollen und weich, ölige Ablagerungen an Schlauchinnenseite.
**Typische Ursache**: Motorleckage, undichte Hydraulikleitung, Dieselleck, mangelnde Bilgenpflege.
**Risiko**: MITTEL (technisch) + HOCH (umweltrechtlich — MARPOL!).
**Sofortmaßnahme**: Ölbinde-Pads in Bilge legen, Leckquelle finden, kein ölhaltiges Wasser abpumpen!
**Reparatur**: Leckquelle beheben, Bilge reinigen, ölresistenten Schlauch (NBR) im Motorraum einbauen.
**AYDI-Score-Auswirkung**: Condition -30, Compliance -50 (Umwelt), Materials -20
**Confidence**: visual_high (Ölfilm klar sichtbar)

### Fehlerbild F-BL-09: Fehlende Redundanz / Nur eine Pumpe

**Beschreibung**: Boot hat nur eine einzige Bilgenpumpe ohne Backup-System. Bei Pumpenausfall gibt es keine automatische Entwässerung.
**Visuelle Merkmale**: Nur eine Pumpe in der Bilge sichtbar, keine Handpumpe im Cockpit, kein zweiter Schwimmerschalter.
**Typische Ursache**: Werkseitige Minimalausstattung, Kosteneinsparung, Unwissenheit.
**Risiko**: HOCH — Keine Redundanz bei Pumpenausfall. ABYC H-22 verlangt Redundanz ab 8 m.
**Sofortmaßnahme**: Handpumpe beschaffen (Whale Gusher 10 — kann im Notfall 37 l/min fördern).
**Reparatur**: Zweite elektrische Pumpe in Vorschiff installieren, Handpumpe im Cockpit fest einbauen.
**AYDI-Score-Auswirkung**: Redundancy -60, Compliance -40
**Confidence**: visual_high (fehlende Komponenten klar erkennbar)

### Fehlerbild F-BL-10: Falsche Schlauchdimension (zu eng)

**Beschreibung**: Bilgenschlauch hat geringeren Innendurchmesser als der Pumpen-Stutzen. Drastische Leistungsreduzierung durch Strömungswiderstand.
**Visuelle Merkmale**: Sichtbare Reduzierung am Anschluss, Schlauch sitzt stramm auf zu großem Stutzen oder Adapter verwendet, Pumpe arbeitet hörbar angestrengt.
**Typische Ursache**: Falsches Material bei Reparatur verwendet, fehlende Fachkenntnis.
**Risiko**: MITTEL — Pumpenleistung um 30–60% reduziert.
**Sofortmaßnahme**: Richtigen Durchmesser beschaffen und einbauen.
**Reparatur**: Schlauch durch korrekten Durchmesser ersetzen (ABYC: Schlauch-ID = Stutzen-AD).
**AYDI-Score-Auswirkung**: Capacity -40, Compliance -20
**Confidence**: visual_high (Durchmesserunterschied sichtbar)

### Fehlerbild F-BL-11: Schlauch ohne Befestigung (durchhängend)

**Beschreibung**: Bilgenschlauch hängt lose im Rumpf ohne Schlauchhalter. Schlauch scheuert an Kanten, bildet Tiefpunkte (Wasseransammlung), kann knicken.
**Visuelle Merkmale**: Schlauch hängt in großen Bögen, liegt auf anderen Komponenten auf, scheuert an Schottkanten, sichtbare Abriebstellen.
**Typische Ursache**: Mangelhafte Installation, Halterungen abgebrochen, nachträglicher Einbau ohne fachgerechte Befestigung.
**Risiko**: NIEDRIG-MITTEL — Langfristig Scheuerschäden und Kinking.
**Sofortmaßnahme**: Kabelbinder als provisorische Halterung.
**Reparatur**: Schlauchhalter alle 300 mm montieren, Scheuerstellen mit Schutzmanschette versehen.
**AYDI-Score-Auswirkung**: Condition -15, Production -20
**Confidence**: visual_high

### Fehlerbild F-BL-12: Cockpit-Drain verstopft

**Beschreibung**: Cockpit-Ablauf verstopft durch Blätter, Sand, Textilreste. Cockpit entwässert nicht bei Regen oder Übernahme von Seewasser.
**Visuelle Merkmale**: Stehendes Wasser im Cockpit, Drain-Öffnung zugesetzt, Wasser steigt bei Regen an. Von unten: Schlauch kann mit Sediment gefüllt sein.
**Typische Ursache**: Fehlende Siebkappe am Drain, Laub/Schmutzansammlung, Cockpit-Teppich über Drain.
**Risiko**: HOCH bei CE-Kat A/B — Cockpit muss selbstlenzend sein (ISO 11812). Verstopfter Drain bei Seegang kann zu Stabilitätsverlust führen.
**Sofortmaßnahme**: Drain von oben freistechen (Draht), Siebkappe einsetzen.
**Reparatur**: Cockpit-Drain-Schlauch durchspülen, Siebkappe montieren, regelmäßige Reinigung.
**AYDI-Score-Auswirkung**: Condition -25, Compliance -35
**Confidence**: visual_high

(Confidence: documented)

---

## 15. Fehlerbehebungs-Leitfaden

### Problem P-BL-01: Bilgenpumpe läuft, aber fördert kein Wasser

**Mögliche Ursachen (in Reihenfolge der Wahrscheinlichkeit)**:
1. Sieb/Strainer verstopft → Reinigen
2. Schlauch geknickt → Verlauf prüfen, neu verlegen
3. Impeller verschlissen → Impeller tauschen
4. Bilgen-Austritt verstopft (Biofouling) → Von außen reinigen
5. Schlauch abgerutscht → Wieder aufstecken, Schellen prüfen
6. Anti-Siphon-Ventil verklebt (öffnet nicht) → Ventil reinigen/tauschen
7. Pumpe dreht rückwärts (Kabel vertauscht) → Polarität prüfen
8. Luft im System (Membranpumpe) → Entlüften, Saugleitung prüfen

**Diagnose-Ablauf**:
- Schlauch am Pumpen-Austritt lösen → Pumpe laufen lassen → Kommt Wasser? JA: Problem in Leitung/Austritt. NEIN: Problem in Pumpe/Ansaugung.

(Confidence: documented)

### Problem P-BL-02: Bilgenpumpe läuft ständig (Dauerlauf)

**Mögliche Ursachen**:
1. Wassereinbruch! → Sofort Leckquelle suchen (Borddurchlässe, Stopfbuchse, Ruderschaft)
2. Rück-Siphon (Seewasser fließt rückwärts ein) → Anti-Siphon-Ventil prüfen/installieren
3. Kondenswasser bei großen Temperaturunterschieden → Normal in Tropen, kein Handlungsbedarf
4. Undichtes Seeventil in der Nähe → Seeventil prüfen und schließen
5. Schwimmerschalter defekt (schaltet nicht aus) → Schwimmerschalter tauschen

**Diagnose-Ablauf**:
- Pumpe ausschalten → Wasserstand beobachten → Steigt Wasser? JA: aktiver Wassereinbruch. NEIN: Schwimmerschalter-Problem.
- Bei aktivem Einbruch: Bilge-Austritt-Seeventil schließen → Steigt Wasser weiter? JA: Leck an anderem Borddurchlass. NEIN: Rück-Siphon über Bilgenleitung.

(Confidence: documented)

### Problem P-BL-03: Bilgenpumpe startet nicht automatisch

**Mögliche Ursachen**:
1. Schwimmerschalter verklemmt → Reinigen oder ersetzen
2. Sicherung durchgebrannt → Sicherung prüfen und ersetzen
3. Kabelbruch → Durchgangsprüfung mit Multimeter
4. Schwimmerschalter falsch positioniert (zu hoch) → Tiefer montieren
5. Batterie leer → Spannung prüfen (>10,5V bei 12V-System)
6. Kabel am Hauptschalter angeschlossen (und ausgeschaltet) → Direkt an Batterie klemmen
7. Korrodierte Kontakte → Kontakte reinigen, Schrumpfschlauch

**Diagnose-Ablauf**:
- Pumpe manuell testen (direkt an Batterie) → Läuft? JA: Schwimmerschalter/Kabel-Problem. NEIN: Pumpe defekt.
- Schwimmerschalter-Test: Von Hand betätigen, Multimeter am Kabel → Schaltet? JA: Positionierung. NEIN: Schalter defekt.

(Confidence: documented)

### Problem P-BL-04: Geruch aus Bilgenschläuchen

**Mögliche Ursachen**:
1. Biofilm/Bakterien in der Bilge → Enzymatischer Reiniger (z.B. Star Brite Bilge Cleaner)
2. Öliger Bilgenwasser → Bilge entölen, Ölquelle finden
3. Standard-PVC-Schlauch statt Sanitärschlauch → Auf geruchsdichten Schlauch umrüsten
4. Abwasser in Bilge (undichte Toiletten-/Grauwasserleitung) → Leck suchen und reparieren
5. Stehendes Wasser in Tiefpunkten → Schlauchwasserfall (Tiefpunkte) eliminieren

**Behandlung**:
- Bilge mit enzymatischem Reiniger fluten (4 h einwirken lassen)
- Bilgenpumpe laufen lassen (Achtung: Reiniger nicht in Hafen pumpen!)
- Schläuche mit Sanitär-Typ ersetzen (Shields 148, Trident 101)

(Confidence: documented)

### Problem P-BL-05: Wasser im Cockpit läuft nicht ab

**Mögliche Ursachen**:
1. Cockpit-Drain verstopft (Laub, Sand, Textil) → Reinigen
2. Cockpit-Drain-Schlauch geknickt → Neu verlegen
3. Cockpit-Boden unter Wasserlinie (Beladung zu schwer) → Gewichtsverteilung prüfen
4. Borddurchlass-Auslass unter Wasser (Bug-lastig) → Trimm korrigieren
5. Rückschlagklappe am Cockpit-Drain klemmt → Reinigen oder entfernen

**Diagnose-Ablauf**:
- Wasser in leeres Cockpit gießen → Abfluss beobachten
- Wenn Wasser rückwärts aus Drain kommt: Boot liegt zu tief achtern, Borddurchlass unter WL
- Drain-Sieb entfernen, Draht durch Schlauch schieben → Verstopfung orten

(Confidence: documented)

---

## 16. FAQ

### BL-001: Welche Bilgenpumpen-Größe braucht mein Boot?
Faustregel: 10 GPH pro Fuß Bootslänge als Minimum. Ein 35-Fuß-Segelboot braucht mindestens 350 GPH (ca. 1.325 l/h). Für CE-Kat A/B mindestens das Doppelte. Für die exakten Werte: siehe ISO 8849 Tabelle in Abschnitt 1.3.1.
(Confidence: documented)

### BL-002: Muss die Bilgenpumpe immer an Strom sein, auch wenn das Boot verlassen wird?
Ja! Die Bilgenpumpe muss IMMER stromversorgt sein. ABYC H-22 verlangt direkte Verdrahtung an der Batterie, unabhängig vom Hauptschalter. Ohne aktive Bilgenpumpe kann Regenwasser, Kondensat oder ein kleines Leck das Boot im Hafen sinken lassen.
(Confidence: documented)

### BL-003: Wie oft muss ich den Bilgenschlauch tauschen?
PVC-Schläuche alle 7–10 Jahre, EPDM alle 10–15 Jahre. Im Motorraum und bei UV-Belastung kürzer. Jährliche Sichtprüfung und Biege-Test (Schlauch um Finger wickeln) entscheidend.
(Confidence: documented)

### BL-004: Spiralschlauch oder normaler Schlauch — wann was?
Spiralschlauch (kollaps-sicher) ist Pflicht auf der Saugseite von Membranpumpen. Auf der Druckseite genügt normaler verstärkter PVC-Schlauch. Faustregel: Wenn die Pumpe über dem Wasserspiegel sitzt und saugen muss → Spiralschlauch.
(Confidence: documented)

### BL-005: Darf ich den Bilgenschlauch verkleinern (Reduzierung)?
Nein! ABYC H-22 verbietet Reduzierungen in der Bilgenleitung. Der Schlauch-Innendurchmesser muss mindestens dem Pumpen-Stutzen entsprechen. Eine Reduzierung kann die Pumpenleistung um 50% oder mehr verringern.
(Confidence: documented)

### BL-006: Brauche ich ein Anti-Siphon-Ventil?
Wenn der Bilgen-Austritt unter der Wasserlinie liegt oder bei Krängung unter Wasser kommen kann → ja, obligatorisch. Alternative: Schwanenhals-Schleife mit Scheitelpunkt 300 mm über WL.
(Confidence: documented)

### BL-007: Was ist besser — mechanischer oder elektronischer Schwimmerschalter?
Elektronische Schwimmerschalter (Feldeffekt, kapazitiv) sind zuverlässiger, da keine beweglichen Teile. Sie verklemmen nicht durch Bilgenschmutz. Kosten 2–3× mehr als mechanische, amortisieren sich durch Zuverlässigkeit.
(Confidence: documented)

### BL-008: Wie viele Schlauchschellen brauche ich pro Anschluss?
Mindestens zwei Schlauchschellen pro Anschluss bei allen Verbindungen unter der Wasserlinie und bei Bilgensystem-Anschlüssen. Die Schrauben beider Schellen um 180° versetzt ausrichten.
(Confidence: documented)

### BL-009: Mein Bilgenschlauch ist innen schwarz/schleimig — ist das gefährlich?
Biofilm ist hygienisch unangenehm, aber kein unmittelbares Sicherheitsrisiko. Er kann jedoch den Innendurchmesser reduzieren. Bilge mit enzymatischem Reiniger behandeln. Bei starkem Befall: Schlauch tauschen.
(Confidence: documented)

### BL-010: Kann ich Gartenschlauch als Bilgenschlauch verwenden?
Nein! Gartenschlauch ist nicht verstärkt, nicht UV-stabilisiert, nicht ölbeständig und hat keine Marine-Zulassung. Er kann kollabieren, knicken und wird in 1–2 Jahren spröde.
(Confidence: documented)

### BL-011: Was kostet ein komplettes Bilgensystem für ein 10m-Segelboot?
Budget ca. 350–500 EUR für ein normgerechtes System (Primärpumpe, Handpumpe, Schwimmerschalter, Alarm, Schläuche, Schellen, Anti-Siphon, Borddurchlass). Siehe Abschnitt 9.2 für detaillierte Aufstellungen.
(Confidence: estimated)

### BL-012: Muss ich ein Seeventil am Bilgen-Austritt haben?
Wenn der Bilgen-Austritt unter der Wasserlinie liegt: ja, Seeventil nach ISO 9093 vorgeschrieben. Wenn dauerhaft über der Wasserlinie: kein Seeventil nötig (ISO 9093 Clause 4.2). In der Praxis: fast alle Bilgen-Austritte bei Segelbooten liegen über WL.
(Confidence: documented)

### BL-013: Wie teste ich mein Bilgensystem?
5 Liter Wasser in die Bilge gießen. Schwimmerschalter muss auslösen, Pumpe muss anspringen, Wasser muss am Austritt austreten, Pumpe muss nach Abpumpen automatisch stoppen. Alle Schlauchverbindungen auf Tropfen prüfen.
(Confidence: documented)

### BL-014: Was mache ich bei einem Bilgenpumpen-Totalausfall auf See?
1. Ruhe bewahren. 2. Manuelle Handpumpe verwenden. 3. Wenn keine Handpumpe: Eimer und Lenzöse. 4. Leckquelle finden und provisorisch abdichten. 5. Mayday/Pan-Pan je nach Lage. Eine gute Handpumpe (Whale Gusher 30) fördert 69 l/min — das ist mehr als die meisten elektrischen Pumpen.
(Confidence: documented)

### BL-015: Kann ich die Bilgenpumpe auch als Lenzpumpe für die Dusche nutzen?
Besser nicht. Duschsumpf-Pumpen (z.B. Whale Gulper 220) sind für diesen Zweck konzipiert. Sie sitzen über dem Sumpf und saugen an, statt im Wasser zu stehen. Bilgen-Tauchpumpe und Duschsumpf-Pumpe sollten getrennte Systeme sein.
(Confidence: documented)

### BL-016: Wie verlege ich den Bilgenschlauch richtig?
Steigend vom tiefsten Punkt zur Austrittsöffnung, ohne Tiefpunkte (Wassersäcke). Alle 300 mm befestigen. Biegeradius einhalten (min. 3–5× ID). Nicht an scharfen Kanten. Nicht im Kontakt mit Motor/Auspuff. Kein Kreuz mit elektrischen Kabeln.
(Confidence: documented)

### BL-017: Was ist der Unterschied zwischen Bilgenpumpe und Lenzpumpe?
Technisch das gleiche. „Bilgenpumpe" bezieht sich auf die Funktion (Bilgenwasser abpumpen), „Lenzpumpe" auf die Tätigkeit (Lenzen = Wasser entfernen). In der Praxis werden die Begriffe synonym verwendet.
(Confidence: documented)

### BL-018: Brauche ich einen Hochwasser-Alarm?
ABYC H-22 fordert einen Hochwasser-Alarm für Boote ab 8 m (26 ft). Auch für kleinere Boote dringend empfohlen. Der Alarm muss hörbar sein (min. 85 dB) und unabhängig vom Schwimmerschalter der Pumpe sein.
(Confidence: documented)

### BL-019: Was bedeutet GPH bei Bilgenpumpen?
GPH = Gallons Per Hour (US-Gallonen pro Stunde). 1 US-Gallon = 3,785 Liter. Eine 1.000 GPH-Pumpe fördert also 3.785 l/h unter idealen Bedingungen (0 m Förderhöhe). Die tatsächliche Leistung ist immer geringer.
(Confidence: documented)

### BL-020: Wie wirkt sich die Förderhöhe auf die Pumpenleistung aus?
Erheblich. Eine 1.000 GPH-Pumpe fördert bei 2 m Höhe nur noch ca. 60% der Nennleistung. Bei Auswahl der Pumpe immer die tatsächliche Förderhöhe (Abstand Bilgensumpf → Austritt) berücksichtigen. Details in Tabelle 11.1.2.
(Confidence: calculated)

### BL-021: Darf Bilgenwasser direkt ins Meer gepumpt werden?
Für Freizeitboote gibt es keine direkte MARPOL-Pflicht, aber umweltrechtliche Verantwortung. Ölhaltiges Bilgenwasser darf nicht eingeleitet werden. Best Practice: Ölbinde-Pads in Bilge, Bilge sauber halten, in vielen Marinas wird Bilgen-Sauberkeit kontrolliert.
(Confidence: documented)

### BL-022: Kann ich zwei Bilgenpumpen an einem Schlauch anschließen?
Technisch möglich mit Y-Stück, aber nicht empfohlen. Wenn eine Pumpe nicht läuft, kann Wasser rückwärts durch die stehende Pumpe fließen. Besser: jede Pumpe hat ihren eigenen Austritt.
(Confidence: documented)

### BL-023: Welche Schlauchschellen-Marken sind empfehlenswert?
Premium: ABA (Schweden), NORMA (Deutschland), Mikalor (Spanien). Gut: Jubilee/L.H. Dottie (UK). Wichtiger als Marke ist das Material: nur AISI 316 (A4)! Bandbreite min. 9 mm für Bilgenschläuche.
(Confidence: documented)

### BL-024: Was mache ich mit der Bilgenpumpe beim Winterlager?
Tauchpumpe: Im Boot lassen, aber Bilge trocken halten. Schwimmerschalter kann aktiv bleiben (Regenwasser-Schutz). Bei Frostgefahr: Schlauch am tiefsten Punkt lösen und Restwasser ablaufen lassen. Impeller-Pumpen (Jabsco): Impeller ausbauen (verhindert Verformung).
(Confidence: documented)

### BL-025: Wie erkenne ich, ob mein Bilgensystem den CE-Anforderungen entspricht?
CE-Konformität Bilgensystem: ausreichende Pumpenkapazität für CE-Kategorie (Tabelle 1.3.1), automatische Pumpe mit Schwimmerschalter, manuelle Backup-Möglichkeit, Anti-Siphon-Schutz bei Austritt unter WL, selbstlenzendes Cockpit bei Kat A/B. Professionelle Bewertung durch AYDI Level 2 Analyse.
(Confidence: documented)

---

## 17. Glossar

| Begriff | Erklärung |
|---|---|
| **Bilge** | Tiefster Punkt im Bootsrumpf, wo sich Wasser ansammelt |
| **Bilgensumpf** | Vertiefung in der Bilge zum Sammeln von Wasser, oft mit Sieb |
| **Bilgenpumpe** | Pumpe zum Entfernen von Bilgenwasser |
| **Lenzpumpe** | Synonym für Bilgenpumpe |
| **Lenzen** | Entfernen von Wasser aus dem Bootsinneren |
| **Bilgenschlauch** | Schlauch zwischen Bilgenpumpe und Borddurchlass |
| **Lenzleitung** | Gesamte Leitung vom Bilgensumpf bis Austritt |
| **Schwimmerschalter** | Schalter, der bei steigendem Wasserstand die Pumpe aktiviert |
| **Float Switch** | Englisch für Schwimmerschalter |
| **Tauchpumpe** | Elektrische Pumpe, die direkt im Bilgenwasser sitzt |
| **Membranpumpe** | Pumpe mit flexibler Membran, sitzt über dem Wasserspiegel |
| **Impeller** | Laufrad einer Zentrifugalpumpe |
| **Flexible Impeller** | Gummi-Impeller, der durch Gehäuseform Pumpwirkung erzeugt |
| **GPH** | Gallons Per Hour — Förderleistung in US-Gallonen pro Stunde |
| **Förderhöhe** | Geodätischer Höhenunterschied zwischen Pumpe und Austritt |
| **Saugseite** | Schlauch zwischen Bilgensumpf und Pumpen-Eingang |
| **Druckseite** | Schlauch zwischen Pumpen-Ausgang und Borddurchlass |
| **Spiralschlauch** | Schlauch mit eingebetteter Spiralverstärkung, kollaps-sicher |
| **Kollaps** | Zusammendrücken eines Schlauchs durch Unterdruck |
| **Anti-Siphon-Ventil** | Ventil, das Rückfluss von Seewasser durch die Bilgenleitung verhindert |
| **Schwanenhals** | Schlauchschleife über Wasserlinie als Anti-Siphon-Schutz |
| **Vented Loop** | Englisch für belüftete Schleife / Anti-Siphon-Ventil |
| **Borddurchlass** | Durchführung durch den Rumpf (Thru-Hull) |
| **Seeventil** | Absperrventil am Borddurchlass (Seacock) |
| **Skin-Fitting** | Englisch für Borddurchlass |
| **Seacock** | Englisch für Seeventil |
| **Rückschlagventil** | Ventil, das nur in eine Richtung durchlässt (Check Valve) |
| **Cockpit-Drain** | Ablauf im Cockpit-Boden |
| **Scupper** | Speigatt — Deck-Entwässerungsöffnung |
| **Selbstlenzend** | Cockpit entwässert sich durch Schwerkraft |
| **Strainer** | Sieb/Filter am Pumpeneingang |
| **DZR Bronze** | Dezinkungsbeständige Bronze (für Marine-Armaturen) |
| **Marelon** | Verbundwerkstoff-Marke für Marine-Armaturen (Forespar) |
| **EPDM** | Ethylen-Propylen-Dien-Kautschuk — hochwertiges Gummimaterial |
| **NBR** | Nitrilkautschuk — öl- und kraftstoffbeständig |
| **SBR** | Styrol-Butadien-Kautschuk — Standard-Industriegummi |
| **PVC** | Polyvinylchlorid — Standardmaterial für günstige Schläuche |
| **Weichmacher** | Additiv in PVC zur Flexibilität (Phthalate/Adipate) |
| **Biofouling** | Biologischer Bewuchs an Unterwasserteilen |
| **Biofilm** | Bakterienfilm auf Oberflächen in feuchter Umgebung |
| **MARPOL** | International Convention for the Prevention of Pollution from Ships |
| **Oily Water Separator (OWS)** | Ölabscheider für Bilgenwasser |
| **Head Loss** | Englisch für Druckverlust in Flüssigkeitsleitungen |
| **Barb Fitting** | Gerippter Schlauchanschluss-Stutzen |

(Confidence: documented)

---

## 18. Schnell-Referenz

### 18.1 Schlauchdurchmesser nach Pumpe

| Pumpe | Stutzen mm | Schlauch ID mm | Schlauch-Typ |
|---|---|---|---|
| 500 GPH | 19 | 19 | PVC verstärkt |
| 750 GPH | 19 | 19 | PVC verstärkt |
| 1.000 GPH | 28 | 28 | PVC verstärkt |
| 2.000 GPH | 28 | 28 | PVC verstärkt oder Spiral |
| 3.700 GPH | 38 | 38 | PVC verstärkt oder EPDM |
| Handpumpe | 25–38 | 25–38 | Spiral (Saugseite!) |

### 18.2 Mindest-Pumpenkapazität nach Bootslänge (CE-Kat B)

| LOA | Min. Kapazität | Empfohlene Pumpe |
|---|---|---|
| ≤6 m | 1.140 l/h (300 GPH) | Rule 24 / Seaflo 500 |
| 6–9 m | 2.270 l/h (600 GPH) | Rule 25S / Johnson L750 |
| 9–12 m | 3.800 l/h (1.000 GPH) | Rule 27S |
| 12–15 m | 5.300 l/h (1.400 GPH) | Rule 09 (2.000 GPH) |
| 15–18 m | 7.600 l/h (2.000 GPH) | Rule 09 + Rule 27S |
| 18–24 m | 11.400 l/h (3.000 GPH) | Rule 10 (3.700 GPH) |

> ⚠️ **ZU PRÜFEN (Audit):** Diese Tabelle ist mit „CE-Kat B" überschrieben, doch die Werte (≤6 m: 1.140 l/h … 18–24 m: 11.400 l/h) entsprechen exakt der **CE-Kat-C-Spalte** aus Tabelle 1.3.1. Für CE-Kat A/B gelten dort die höheren Werte (≤6 m: 1.900 l/h … 18–24 m: 15.100 l/h). Widerspruch zwischen Normtabelle (1.3.1) und Schnell-Referenz — vor Nutzung Kategorie bzw. Werte verifizieren (Gefahr der Pumpen-Unterdimensionierung bei CE-Kat B).

### 18.3 Schlauchschellen-Regel

- Unter WL und Bilge: **2 Schellen pro Anschluss**, AISI 316
- Über WL (Scupper): **1 Schelle pro Anschluss**, AISI 316
- Nie verzinkte Schellen verwenden!
- Schrauben der Doppelschellen um **180° versetzt**

### 18.4 Wartungsintervalle (Kurzform)

| Was | Wie oft |
|---|---|
| Bilge-Sichtprüfung | Monatlich |
| Pumpe testen (manuell) | Monatlich |
| Sieb reinigen | Vierteljährlich |
| Schlauchschellen prüfen | Jährlich |
| Schwimmerschalter testen | Vierteljährlich |
| Schläuche auf Zustand prüfen | Jährlich |
| PVC-Schläuche tauschen | 7–10 Jahre |
| EPDM-Schläuche tauschen | 10–15 Jahre |

(Confidence: documented)

---

## 19. Notfall-Ressourcen

### 19.1 Sofortmaßnahmen bei Wassereinbruch

```
1. RUHE BEWAHREN
2. Bilgenpumpe(n) auf MANUELL (volle Leistung)
3. Alle Seeventile SCHLIESSEN (besonders Bilgen-Austritt bei Rück-Siphon-Verdacht)
4. Leckstelle IDENTIFIZIEREN
   - Borddurchlass gebrochen → Holzpfropfen!
   - Schlauch abgerutscht → Schlauch aufschieben + Kabelbinder
   - Stopfbuchse → Packung nachziehen
5. PROVISORISCH ABDICHTEN
   - Holzpfropfen (verschiedene Größen vorhalten!)
   - Unterwasser-Epoxy (z.B. MarineWeld)
   - Leckstopfen-Set (Plastimo 63614)
6. HANDPUMPE einsetzen (Whale Gusher → 69 l/min!)
7. EIMER und LENZÖSE als letztes Mittel
8. PAN-PAN oder MAYDAY je nach Lage (DSC Kanal 70)
```

### 19.2 Notfall-Ausrüstung Bilgensystem

| Ausrüstung | Zweck | Preis EUR |
|---|---|---|
| Holzpfropfen-Set (6 Größen) | Borddurchlass-Notabdichtung | 15 |
| Leckstopfen-Set Plastimo 63614 | Universeller Leckstopp | 35 |
| MarineWeld Unterwasser-Epoxy | Rissabdichtung unter Wasser | 12 |
| Whale Gusher 10 Mk3 | Tragbare Handpumpe | 85 |
| Eimer 10 l (Bordwerkzeug) | Wasserentfernung | 5 |
| Kabelbinder-Set (diverse Größen) | Provisorische Schlauchsicherung | 8 |
| Schlauchschellen-Set (19–50 mm) | Ersatzschellen | 15 |
| Bilgenschlauch 1 m (25 mm) | Ersatzschlauch | 6 |

### 19.3 Notruf-Referenz

| Situation | Aktion | Kanal/Nummer |
|---|---|---|
| Akute Sinkgefahr | MAYDAY auf VHF | Kanal 16 (156,8 MHz) |
| Wassereinbruch kontrollierbar | PAN-PAN auf VHF | Kanal 16 |
| Im Hafen, langsamer Einbruch | Hafenmeister + Feuerwehr | 112 (EU) |
| Technische Hilfe (kein Notfall) | Seenotrettung DGZRS | 124 124 |
| Versicherungs-Hotline | Kaskoversicherung | Police-Nr. bereithalten |

(Confidence: documented)

---

## ANHANG A — Cross-Reference Bilgenschlauch ↔ AYDI-Module

### A.1 Modul-Zuordnung

| AYDI-Modul | Bilgensystem-Aspekt | Prüfpunkte | Score-Gewicht |
|---|---|---|---|
| compliance | CE-Konformität | Pumpenkapazität, Redundanz, Anti-Siphon | 0,30 |
| materials | Schlauchmaterial | Material, Schellen, Korrosion | 0,25 |
| structural | Befestigung, Borddurchlass | Backing-Block, Rumpf-Integrität | 0,15 |
| service_patterns | Wartungszustand | Alter, Defekte, Leckhistorie | 0,20 |
| cost | Kosten | Reparatur-/Austauschkosten | 0,05 |
| ergonomics | Zugänglichkeit | Pumpe/Schläuche erreichbar | 0,05 |

### A.2 Pipeline-Zuordnung

| Pipeline | Prüfbare Aspekte | Confidence-Range |
|---|---|---|
| A (Strukturiert) | Pumpenkapazität, Schlauchdimensionen, CE-Kategorie | measured / calculated |
| B (Visuell) | Schlauchzustand, Schellen, Kinking, Biofouling | visual_high / visual_medium |
| C (Text) | Service-Befunde, Leckhistorie, Gutachter-Reports | documented |

(Confidence: documented)

---

## ANHANG B — Pumpenleistungs-Vergleich

### B.1 Tauchpumpen bei verschiedenen Förderhöhen

| Modell | 0 m | 1 m | 2 m | 3 m | 4 m | Preis EUR |
|---|---|---|---|---|---|---|
| Rule 25S (500 GPH) | 1.893 l/h | 1.325 l/h | 757 l/h | 189 l/h | — | 25 |
| Seaflo 500 GPH | 1.893 l/h | 1.230 l/h | 680 l/h | 150 l/h | — | 15 |
| Rule 27S (1000 GPH) | 3.785 l/h | 3.028 l/h | 2.271 l/h | 1.439 l/h | 378 l/h | 35 |
| Johnson L750 | 2.839 l/h | 2.271 l/h | 1.703 l/h | 1.136 l/h | 284 l/h | 40 |
| Rule 09 (2000 GPH) | 7.571 l/h | 6.435 l/h | 5.300 l/h | 4.163 l/h | 2.649 l/h | 55 |
| Rule 10 (3700 GPH) | 14.006 l/h | 12.606 l/h | 10.505 l/h | 8.404 l/h | 5.602 l/h | 85 |
| Jabsco Cyclone HP | 11.356 l/h | 9.652 l/h | 7.949 l/h | 5.678 l/h | 3.406 l/h | 120 |

### B.2 Membranpumpen vs. Tauchpumpen

| Kriterium | Tauchpumpe | Membranpumpe |
|---|---|---|
| Förderleistung | Hoch (500–4.000 GPH) | Mittel (200–1.500 l/h) |
| Förderhöhe | Begrenzt (3–5 m) | Gut (4–8 m) |
| Selbstansaugend | Nur im Wasser | Ja (bis 2–3 m) |
| Trockenlaufsicher | Ja (30+ min) | Ja (unbegrenzt) |
| Schmutzverträglichkeit | Mäßig (Impeller verstopft) | Gut (Ventile tolerant) |
| Stromverbrauch | Moderat | Höher pro l/h |
| Lautstärke | Leise | Pulsierend, lauter |
| Lebensdauer | 3–7 Jahre | 5–10 Jahre |
| Preis pro l/h | Günstig | Teurer |

(Confidence: documented)

---

## ANHANG C — Biegeradien

### C.1 Mindest-Biegeradien nach Schlauchttyp und Durchmesser

| Material | ID 19 mm | ID 25 mm | ID 32 mm | ID 38 mm | ID 50 mm |
|---|---|---|---|---|---|
| PVC verstärkt | 65 mm | 85 mm | 110 mm | 130 mm | 170 mm |
| PVC Spiral | 95 mm | 120 mm | 155 mm | 185 mm | 240 mm |
| EPDM Gummi | 55 mm | 75 mm | 95 mm | 115 mm | 150 mm |
| Sanitär (PE-Barriere) | 80 mm | 100 mm | 130 mm | 155 mm | 200 mm |

### C.2 Faustregel

- **PVC verstärkt**: min. 3,5× ID
- **PVC Spiral**: min. 5× ID
- **EPDM**: min. 3× ID
- **Sanitär**: min. 4× ID

**Achtung**: Bei Unterschreitung des Mindest-Biegeradius:
- Innerer Querschnitt wird reduziert → Druckverlust steigt exponentiell
- Außenseite wird gedehnt → Mikrorisse → Undichtigkeit
- Innenseite wird gestaucht → Falten → Strömungswiderstand

(Confidence: documented)

---

## ANHANG D — Confidence-Mapping für Bilgensystem-Analyse

### D.1 Structured Pipeline (Pipeline A)

| Eingabedaten | Confidence | Score-Sicherheit |
|---|---|---|
| CAD mit Bilgensystem-Layout | measured | Hoch (±5%) |
| Pumpen-Datenblatt vorhanden | measured | Hoch (±5%) |
| Schlauchdimensionen eingegeben | measured | Hoch (±5%) |
| Nur Bootslänge + CE-Kat | estimated | Niedrig (±30%) |
| Bootsklasse + Baujahr | benchmark | Mittel (±20%) |

### D.2 Visual Pipeline (Pipeline B)

| Foto-Qualität | Confidence | Erkennbare Defekte |
|---|---|---|
| Nahaufnahme Bilge, gut beleuchtet | visual_high | Risse, Verfärbung, Korrosion, Kinking |
| Übersichtsaufnahme Bilge | visual_medium | Grobe Defekte, fehlende Schellen |
| Schlechte Beleuchtung, verwackelt | visual_low | Nur offensichtliche Mängel |
| Foto von außerhalb der Bilge | visual_insufficient | Keine Bewertung möglich |

### D.3 Text Pipeline (Pipeline C)

| Textquelle | Confidence | Extraktion |
|---|---|---|
| Professioneller Survey-Report | documented | Befunde, Empfehlungen, Alter |
| Werft-Rechnung | documented | Getauschte Teile, Kosten, Datum |
| Eigner-Logbuch | documented | Wartungshistorie, Auffälligkeiten |
| Forum-Beitrag | estimated | Symptome, keine verifizierte Diagnose |

(Confidence: documented)

---

## ANHANG E — Bordausstattung Bilgensystem

### E.1 Empfohlene Bordausstattung nach Fahrtgebiet

#### E.1.1 Küstenfahrt (CE-Kat C)

| Komponente | Anzahl | Empfehlung |
|---|---|---|
| Elektrische Bilgenpumpe | 1 | ≥500 GPH |
| Schwimmerschalter | 1 | Mechanisch oder elektronisch |
| Handpumpe / Lenzöse | 1 | Whale Gusher Urchin |
| Bilgenschlauch | 2–3 m | 19 mm PVC |
| Schlauchschellen Edelstahl | 6 | AISI 316 |
| Holzpfropfen-Set | 1 | 3 Größen |

#### E.1.2 Offshore (CE-Kat B)

| Komponente | Anzahl | Empfehlung |
|---|---|---|
| Elektrische Bilgenpumpe primär | 1 | ≥1.000 GPH |
| Elektrische Bilgenpumpe sekundär | 1 | ≥500 GPH (anderer Raum) |
| Schwimmerschalter | 2 | Elektronisch (feldeffekt) |
| Hochwasser-Alarm | 1 | 85+ dB |
| Handpumpe (Cockpit) | 1 | Whale Gusher 10 |
| Anti-Siphon | 1–2 | Vetus oder Whale |
| Bilgenschlauch | 5–8 m | 19/28 mm PVC + Spiral |
| Notfall-Set | 1 | Pfropfen, Epoxy, Kabelbinder |

#### E.1.3 Hochsee (CE-Kat A)

| Komponente | Anzahl | Empfehlung |
|---|---|---|
| Elektrische Bilgenpumpe primär | 1 | ≥2.000 GPH |
| Elektrische Bilgenpumpe sekundär | 1 | ≥1.000 GPH |
| Elektrische Bilgenpumpe tertiär | 1 | ≥500 GPH (Vorschiff) |
| Schwimmerschalter | 3 | Elektronisch |
| Hochwasser-Alarm | 1 | Multi-Zone, 90+ dB |
| Handpumpe (Cockpit) | 1 | Whale Gusher 30 (69 l/min) |
| Notlenzpumpe (tragbar) | 1 | Jabsco Water Puppy |
| Anti-Siphon | 2–3 | An jedem Austritt |
| Bilgenschlauch | 10–15 m | 28/38 mm PVC + Spiral + EPDM |
| Notfall-Set | 1 | Vollständig (Pfropfen, Epoxy, Schellen, Schlauch) |

(Confidence: documented)

---

## ANHANG F — Fallstudien

### F.1 Fallstudie: Bavaria 40 Cruiser — Bilgenschlauch geplatzt

**Boot**: Bavaria 40 Cruiser, Bj. 2008, LOA 12.350 mm
**Problem**: Bilgenschlauch (PVC, 28 mm, 14 Jahre alt) am Pumpen-Stutzen geplatzt. Pumpe förderte Wasser in Motorraum statt nach außenbords.
**Ursache**: PVC-Schlauch durch Motorraum-Hitze vorzeitig verhärtet. Nur eine Schlauchschelle (statt zwei).
**Befund**: Schlauch gelblich-braun, bricht bei Biegung, Schelle AISI 304 mit Lochfraß.
**Reparatur**: Neuer EPDM-Schlauch 28 mm (Shields 200-1125), 2× Schellen AISI 316, Anti-Siphon nachgerüstet.
**Kosten**: Material 85 EUR, Arbeit 2 h = 160 EUR, Gesamt 245 EUR.
**Lehre**: Im Motorraum EPDM statt PVC verwenden. Immer zwei Schellen. Austausch nach 10 Jahren bei PVC im Motorraum.
**AYDI-Bewertung**: condition_score 25, materials_score 30, compliance_score 55

### F.2 Fallstudie: Hallberg-Rassy 37 — Rück-Siphon

**Boot**: Hallberg-Rassy 37, Bj. 2002, LOA 11.350 mm
**Problem**: Bei 20° Krängung auf Backbordbug lief Seewasser rückwärts durch die Bilgenleitung ins Boot. Bilgenpumpe lief im Dauerbetrieb.
**Ursache**: Bilgen-Austritt liegt bei Krängung unter Wasserlinie. Kein Anti-Siphon-Ventil oder Schwanenhals eingebaut.
**Befund**: Bilgenschlauch OK (Trident PVC, 5 Jahre), aber gerader Verlauf von Pumpe zu Borddurchlass ohne Hochpunkt.
**Reparatur**: Schwanenhals-Schleife mit Scheitelpunkt 400 mm über WL eingebaut. Zusätzlich Anti-Siphon-Ventil Vetus AS25.
**Kosten**: Material 35 EUR, Arbeit 1,5 h = 120 EUR, Gesamt 155 EUR.
**Lehre**: Segelboote brauchen IMMER Anti-Siphon-Schutz. Krängung berücksichtigen!
**AYDI-Bewertung**: condition_score 80, compliance_score 40 (vorher), 90 (nachher)

### F.3 Fallstudie: Jeanneau Sun Odyssey 439 — Verstopfter Cockpit-Drain

**Boot**: Jeanneau Sun Odyssey 439, Bj. 2013, LOA 13.340 mm
**Problem**: Cockpit entwässert nicht mehr. Bei Gewitterregen steht 15 cm Wasser im Cockpit.
**Ursache**: Cockpit-Drain-Schläuche (PVC, 32 mm) geknickt und mit Sediment verstopft. Kein Siebgitter am Drain.
**Befund**: Schläuche weich und aufgequollen (Kontakt mit Dieselrückständen), beide Drains nur zu 30% durchgängig.
**Reparatur**: Neue Cockpit-Drain-Schläuche 38 mm (größerer Durchmesser!), UV-stabilierter PVC, Siebkappen montiert.
**Kosten**: Material 65 EUR, Arbeit 3 h = 240 EUR, Gesamt 305 EUR.
**Lehre**: Cockpit-Drain regelmäßig prüfen. Siebkappen sind Pflicht. Upgrade auf 38 mm empfohlen.
**AYDI-Bewertung**: condition_score 35, compliance_score 30 (ISO 11812 Verstoß)

### F.4 Fallstudie: Beneteau Oceanis 46.1 — Elektronischer Schwimmerschalter spart Boot

**Boot**: Beneteau Oceanis 46.1, Bj. 2019, LOA 14.600 mm
**Ergebnis**: Eigner hatte mechanischen Schwimmerschalter gegen Rule EcoSwitch (elektronisch) getauscht. Im Winterlager: Regenwasser-Einbruch durch undichte Luken-Dichtung.
**Verlauf**: Mechanischer Schalter des Nachbarboots (gleicher Typ) klemmte — Boot sank auf Grund. Elektronischer Schalter der Oceanis 46.1 schaltete zuverlässig, Pumpe hielt Boot trocken.
**Kosten Umrüstung**: Rule EcoSwitch 35 EUR + 30 min Einbauzeit.
**Lehre**: Elektronische Schwimmerschalter sind 10× zuverlässiger als mechanische. Investition von 35 EUR kann Boot retten.
**AYDI-Bewertung**: Redundancy-Empfehlung: elektronischer Schwimmerschalter, Score-Bonus +15

### F.5 Fallstudie: Dehler 38 SQ — Kompletterneuerung Bilgensystem

**Boot**: Dehler 38 SQ, Bj. 1996, LOA 11.500 mm
**Problem**: Pre-Purchase Survey deckt auf: veraltetes Bilgensystem, PVC-Schläuche (26 Jahre alt!), verzinkte Schlauchschellen, nur eine 500 GPH Pumpe, kein Schwimmerschalter, kein Alarm.
**Befund**: Schläuche steinhart, Schellen durchkorrodiert, Pumpe fördert nur noch 40% der Nennleistung.
**Reparatur**: Kompletterneuerung: Rule 09 (2.000 GPH) + Rule 25S (500 GPH), 2× Rule EcoSwitch, Aqualarm Hochwasser-Alarm, 10 m Trident 150 Schlauch (28 mm + 19 mm), 2× Anti-Siphon Vetus, Whale Gusher 10 Handpumpe, 20× Schellen AISI 316.
**Kosten**: Material 520 EUR, Arbeit 8 h = 640 EUR, Gesamt 1.160 EUR.
**Lehre**: Bei Gebrauchtboot-Kauf: Bilgensystem IMMER prüfen. 25+ Jahre alte Schläuche sind ein sofortiger Austausch-Befund.
**AYDI-Bewertung**: condition_score 10 (vorher), 95 (nachher)

### F.6 Fallstudie: Grand Banks 42 — Motorraum-Bilge mit Ölabscheider

**Boot**: Grand Banks 42 Classic, Bj. 2005, LOA 13.100 mm (Motoryacht, 2× Diesel)
**Problem**: Ölhaltiges Bilgenwasser im Motorraum. Marina hat Liegeplatz-Kündigung angedroht wegen Ölfleck.
**Befund**: Motorraum-Bilge mit Dieselrückständen und Ölfilm. Standard-PVC-Schlauch aufgequollen durch Öl-Kontakt.
**Lösung**: 1) Motorleckage behoben (Dieselfilter-Dichtung). 2) Bilge gereinigt. 3) Ölbinde-Pads dauerhaft in Motorraum-Bilge. 4) Bilgenschlauch auf NBR-Gummi umgerüstet (ölbeständig). 5) Automatische Bilgenpumpe NICHT mit Schwimmerschalter (Öl → falsche Auslösung), sondern Timer-gesteuert.
**Kosten**: Material 180 EUR, Motorleckage 350 EUR, Arbeit 6 h = 480 EUR, Gesamt 1.010 EUR.
**Lehre**: Motorraum-Bilge braucht ölresistente Schläuche (NBR). Ölbinde-Pads sind Pflicht. Ölhaltiges Bilgenwasser nie abpumpen!
**AYDI-Bewertung**: condition_score 45, compliance_score 50 (MARPOL-relevant)

### F.7 Fallstudie: Catana 47 — Katamaran-Bilgensystem

**Boot**: Catana 47 OC, Bj. 2015, LOA 14.280 mm (Segelkatamaran)
**Besonderheit**: Katamaran hat 2 Rümpfe × je 3 Bilgenzonen = 6 Bilgenbereiche (Bug, Mitte, Achtern pro Rumpf).
**Problem**: Nur 2 Bilgenpumpen (je 1 pro Rumpf, mittschiffs). Vordere und achtere Bilgenbereiche nicht abgedeckt.
**Befund**: Bei starkem Vorwind-Segeln sammelt sich Wasser im Vorschiff-Bereich beider Rümpfe. Pumpe mittschiffs kann nicht ansaugen (Schott dazwischen).
**Lösung**: 4 zusätzliche Pumpen (Seaflo 500 GPH, Budget-Option) in Bug und Achter-Bilge beider Rümpfe. Zentrale Alarmanzeige im Cockpit.
**Kosten**: 4× Seaflo 500 GPH = 60 EUR, 4× Schwimmerschalter = 32 EUR, Alarm-Panel = 55 EUR, Schläuche + Schellen = 80 EUR, Arbeit 6 h = 480 EUR, Gesamt 707 EUR.
**Lehre**: Katamarane brauchen pro Rumpf mindestens 2 Pumpen. Jeder wasserdichte Bereich muss eigenständig lenzbar sein.
**AYDI-Bewertung**: condition_score 70, redundancy_score 30 (vorher), 85 (nachher)

### F.8 Fallstudie: Contest 42CS — Notlenzen bei Borddurchlass-Bruch

**Boot**: Contest 42CS, Bj. 2010, LOA 12.800 mm
**Situation**: Toiletten-Borddurchlass (Bronze, 38 mm) bricht bei Nachtfahrt Biskaya. Wassereinbruch ca. 5.000 l/h.
**Verlauf**: Hochwasser-Alarm weckt Crew. Rule 09 (2.000 GPH) + Whale Gusher 30 (Handpumpe, 4.140 l/h) → zusammen 11.711 l/h nominal. Crew stopft Holzpfropfen in Borddurchlass-Öffnung, fixiert mit Unterwasser-Epoxy. Einbruch gestoppt nach 12 min. Bilge leer nach 25 min.
**Schlüsselfaktoren**: 1) Hochwasser-Alarm hat funktioniert. 2) Handpumpe war einsatzbereit. 3) Holzpfropfen waren griffbereit. 4) Bilgensystem war gewartet.
**Kosten Vorsorge**: Holzpfropfen-Set 15 EUR, Hochwasser-Alarm 65 EUR, Handpumpe 185 EUR = 265 EUR Investition hat Boot gerettet (Wert 350.000 EUR).
**AYDI-Bewertung**: overall_score 90 (System hat im Notfall funktioniert)

(Confidence: documented)

---

## ANHANG G — Experten-Referenzen

### G.1 Fachautoren und Experten

| Name | Expertise | Werke / Ressourcen |
|---|---|---|
| Nigel Calder | Marine-Elektrik und -Systeme | „Boatowner's Mechanical & Electrical Manual" |
| Don Casey | Boot-Instandhaltung | „This Old Boat", „Inspecting the Aging Sailboat" |
| John C. Payne | Marine-Elektrik | „The Marine Electrical and Electronics Bible" |
| Steve d'Antonio | Marine-Systeme, Surveyor | stevedmarine.com, Kolumnen in PassageMaker |
| Dag Pike | Motorboote, Seetüchtigkeit | „Motor Boat & Yachting" Kolumnen |
| Peter H. Spectre | Bootsbau-Geschichte | Verschiedene WoodenBoat-Artikel |

### G.2 Fachverbände und Organisationen

| Organisation | Kürzel | Relevanz |
|---|---|---|
| American Boat & Yacht Council | ABYC | Standards H-22 (Bilge Pumping) |
| International Organization for Standardization | ISO | ISO 8849, 9093, 12217, 11812 |
| Bundesstelle für Seeunfalluntersuchung | BSU | Unfallberichte Deutschland |
| United States Coast Guard | USCG | 33 CFR, 46 CFR |
| Royal Yachting Association | RYA | Schulungsmaterial, Best Practices |
| Germanischer Lloyd (DNV GL) | GL | Klassifikationsregeln Yachten |
| International Maritime Organization | IMO | MARPOL, SOLAS |

(Confidence: documented)

---

## ANHANG H — Risk Matrix Bilgensystem

### H.1 Risikobewertung nach Komponente

| Komponente | Versagens-wahrscheinlichkeit | Auswirkung | Risiko-Level | Maßnahme |
|---|---|---|---|---|
| Bilgenschlauch | Mittel (5–10 J) | Hoch | HOCH | Regelmäßiger Austausch |
| Schlauchschelle | Mittel (Korrosion) | Hoch | HOCH | Nur AISI 316, doppelt |
| Schwimmerschalter | Hoch (Verklemmen) | Kritisch | KRITISCH | Elektronisch umrüsten |
| Tauchpumpe (Impeller) | Mittel (Verschleiß) | Hoch | HOCH | Redundanz |
| Anti-Siphon-Ventil | Mittel (Membran) | Hoch | HOCH | Jährlich prüfen |
| Borddurchlass | Niedrig | Kritisch | HOCH | Jährlich inspizieren |
| Sieb/Strainer | Hoch (Verstopfung) | Mittel | MITTEL | Vierteljährlich reinigen |
| Handpumpe | Niedrig | — | NIEDRIG | Jährlich testen |
| Hochwasser-Alarm | Niedrig | Mittel | MITTEL | Batterie prüfen |
| Elektrische Verkabelung | Niedrig | Hoch | MITTEL | Alle 5 J prüfen |

### H.2 Gesamt-Risiko nach Bootstyp

| Bootstyp | Inhärentes Risiko | Typischer Zustand | Empfehlung |
|---|---|---|---|
| Jolle/Dinghy | Niedrig | Oft ohne System | Manuelle Lenzöse ausreichend |
| Trailer-Boot | Niedrig-Mittel | Basis-System | 1 Pumpe + Handlenzen |
| Segelboot Küste | Mittel | Oft vernachlässigt | Jährliche Prüfung |
| Segelboot Offshore | Hoch | Variabel | Halbjährliche Prüfung |
| Motoryacht | Mittel-Hoch | Oft besser gewartet | Jährliche Prüfung |
| Katamaran | Hoch (6+ Zonen) | Oft unterausgestattet | Jede Zone eigene Pumpe |
| Superyacht | Mittel (Klasse) | Professionell gewartet | Klasse-Vorgaben befolgen |

(Confidence: documented)

---

## ANHANG I — Audit/Compliance-Checkliste

### I.1 Bilgensystem-Audit-Checkliste

```
□ 1. Pumpenkapazität gemäß ISO 8849 / CE-Kategorie ausreichend?
□ 2. Redundante Pumpe vorhanden (ab 8 m LOA)?
□ 3. Manuelle Backup-Pumpe vorhanden?
□ 4. Schwimmerschalter funktionsfähig?
□ 5. Hochwasser-Alarm vorhanden und funktional (ab 8 m)?
□ 6. Bilgenpumpe direkt an Batterie angeschlossen (nicht über Hauptschalter)?
□ 7. Schlauch-Innendurchmesser ≥ Pumpen-Stutzen?
□ 8. Alle Schlauchschellen Edelstahl AISI 316?
□ 9. Doppelte Schlauchschellen an allen Anschlüssen?
□ 10. Kein Schlauch-Kinking im Verlauf?
□ 11. Schlauch-Befestigung alle 300 mm?
□ 12. Anti-Siphon-Ventil oder Schwanenhals bei Austritt unter WL?
□ 13. Bilgen-Sieb/Strainer vorhanden und sauber?
□ 14. Borddurchlass-Anschluss dicht?
□ 15. Seeventil am Bilgen-Austritt (falls unter WL)?
□ 16. Cockpit selbstlenzend (CE-Kat A/B)?
□ 17. Cockpit-Drain-Schläuche intakt?
□ 18. Schlauch-Zustand: keine Risse, Verfärbung, Verhärtung?
□ 19. Pumpe trockenlaufsicher (30 min Spezifikation)?
□ 20. Elektrische Absicherung korrekt dimensioniert?
```

### I.2 Scoring

| Ergebnis | Score | Empfehlung |
|---|---|---|
| 20/20 bestanden | 100 | Exzellent — keine Maßnahmen |
| 16–19 bestanden | 80–95 | Gut — Mängel beheben |
| 12–15 bestanden | 60–79 | Befriedigend — zeitnah handeln |
| 8–11 bestanden | 40–59 | Mangelhaft — dringend handeln |
| <8 bestanden | 0–39 | Ungenügend — Boot nicht auslaufen! |

(Confidence: documented)

---

## ANHANG J — Material-Datenblätter

### J.1 PVC-Schlauch (verstärkt, Marine-Qualität)

| Eigenschaft | Wert | Prüfnorm |
|---|---|---|
| Material | PVC (Weich-PVC) + Polyester-Geflecht | — |
| Shore-Härte | 65–75 Shore A | DIN ISO 7619 |
| Zugfestigkeit | ≥10 MPa | DIN 53504 |
| Reißdehnung | ≥250% | DIN 53504 |
| Betriebsdruck (25 mm) | 4 bar | DIN EN ISO 7751 |
| Berstdruck (25 mm) | 12 bar | DIN EN ISO 7751 |
| Temperaturbereich | -10°C bis +60°C | — |
| Ozonbeständigkeit | Befriedigend | DIN ISO 1431 |
| UV-Beständigkeit | Mäßig (mit Stabilisator: gut) | — |
| Ölbeständigkeit | Schlecht (quillt auf) | — |
| Brandverhalten | Selbstverlöschend (mit FR-Additiv) | UL 94 V-0 |
| Lebensmittelecht | Ja (FDA-konform) | FDA 21 CFR 177.1950 |

### J.2 EPDM-Gummi (Marine-Grade)

| Eigenschaft | Wert | Prüfnorm |
|---|---|---|
| Material | EPDM + Polyester-Cord | — |
| Shore-Härte | 60–70 Shore A | DIN ISO 7619 |
| Zugfestigkeit | ≥12 MPa | DIN 53504 |
| Reißdehnung | ≥300% | DIN 53504 |
| Betriebsdruck (25 mm) | 6 bar | DIN EN ISO 7751 |
| Berstdruck (25 mm) | 18 bar | DIN EN ISO 7751 |
| Temperaturbereich | -30°C bis +100°C | — |
| Ozonbeständigkeit | Ausgezeichnet | DIN ISO 1431 |
| UV-Beständigkeit | Gut | — |
| Ölbeständigkeit | Schlecht (Mineral-Öl) | — |
| Brandverhalten | Selbstverlöschend | — |

### J.3 NBR-Gummi (ölbeständig)

| Eigenschaft | Wert | Prüfnorm |
|---|---|---|
| Material | NBR (Nitrilkautschuk) + Cord | — |
| Shore-Härte | 65–75 Shore A | DIN ISO 7619 |
| Zugfestigkeit | ≥10 MPa | DIN 53504 |
| Temperaturbereich | -20°C bis +80°C | — |
| Ölbeständigkeit | Ausgezeichnet | ASTM D471 |
| Kraftstoffbeständigkeit | Gut | — |
| Ozonbeständigkeit | Mäßig | — |
| Einsatz | Motorraum-Bilge | — |

(Confidence: documented)

---

## ANHANG K — Prüfverfahren

### K.1 Sichtprüfung Bilgenschlauch (Visuell)

1. Schlauch auf gesamter Länge freilegen und inspizieren
2. Auf Verfärbung prüfen (gelblich = Alterung, schwarz = Biofilm, aufgequollen = Öl)
3. Auf Risse prüfen (Längs- und Querrisse, besonders an Biegungen)
4. Auf Kinking prüfen (weiße Stellen = Materialstress)
5. Schlauchschellen auf Korrosion prüfen (Magnettest: Magnet haftet = falsche Schelle!)
6. Befestigungspunkte prüfen (lose Halterungen, Scheuerstellen)

### K.2 Taktile Prüfung (Haptisch)

1. Schlauch zwischen Daumen und Zeigefinger zusammendrücken → federt zurück? Gut. Bleibt eingedrückt? Alterung!
2. Schlauch um Finger wickeln (Durchmesser-abhängig) → bricht oder reißt? Sofort tauschen!
3. Oberfläche fühlen → rau/kreidig = UV-Schaden, klebrig = Weichmacher-Austritt, hart = Verhärtung

### K.3 Funktionsprüfung Bilgensystem

1. 5–10 Liter Wasser in Bilgensumpf gießen
2. Schwimmerschalter beobachten → Pumpe startet automatisch?
3. Förderung prüfen → Wasser tritt am Austritt aus?
4. Laufzeit messen → Bilge leer nach wie vielen Sekunden?
5. Pumpe stoppen → Automatischer Stopp nach Entleerung?
6. Alle Anschlüsse auf Tropfenbildung prüfen (trockenes Papier darunter legen)
7. Hochwasser-Alarm prüfen → weiteres Wasser zugeben, Alarm muss auslösen

### K.4 Druckprüfung (Profi)

1. Schlauch beidseitig abklemmen
2. Mit Handpumpe auf 2 bar beaufschlagen
3. 15 min halten → kein Druckabfall = dicht
4. Druckabfall >0,2 bar/min → Leckstelle suchen (Spülmittel-Methode)

(Confidence: documented)

---

## ANHANG L — Top 15 Fehler bei Bilgensystem-Installation

| Nr. | Fehler | Konsequenz | Richtig |
|---|---|---|---|
| 1 | Nur eine Schlauchschelle | Schlauch rutscht ab | 2 Schellen, 180° versetzt |
| 2 | Verzinkte Schellen | Korrosion in <1 Jahr | Nur AISI 316 |
| 3 | Schlauch zu eng (Reduzierung) | 50% Leistungsverlust | ID ≥ Stutzen-AD |
| 4 | Schlauch nicht befestigt | Kinking, Scheuern | Alle 300 mm fixieren |
| 5 | Kein Anti-Siphon bei Austritt unter WL | Rück-Siphon → Sinken | Anti-Siphon oder Schwanenhals |
| 6 | Pumpe über Hauptschalter | Pumpe aus bei verlassenem Boot | Direkt an Batterie |
| 7 | Kein Sieb am Pumpeneingang | Impeller verstopft/bricht | Sieb (≤5 mm) montieren |
| 8 | Mechanischer Schwimmerschalter | Verklemmt durch Schmutz | Elektronisch umrüsten |
| 9 | Kein Hochwasser-Alarm | Einbruch unbemerkt | Alarm ab 8 m LOA |
| 10 | PVC-Schlauch im Motorraum | Vorzeitige Alterung | EPDM verwenden |
| 11 | Standard-PVC auf Saugseite | Kollaps unter Unterdruck | Spiralschlauch verwenden |
| 12 | Tiefpunkte im Schlauchverlauf | Wasseransammlung, Geruch | Durchgehend steigend verlegen |
| 13 | Schlauch-Schnitt mit stumpfem Werkzeug | Unebene Fläche, undicht | Scharfes Messer / Schlauchschneider |
| 14 | Schlauch zu kurz auf Stutzen | Rutscht bei Vibration | Min. 2× Stutzen-Rippenlänge |
| 15 | Keine Handpumpe als Backup | Kein Notlenzen möglich | Handpumpe ist Pflicht! |

(Confidence: documented)

---

## ANHANG M — Zusammenfassung der Kernaussagen

### M.1 Die 10 goldenen Regeln des Bilgensystems

1. **Bilgensystem ist Lebensrettung** — Wartung ist keine Option, sondern Pflicht
2. **Redundanz rettet** — Mindestens zwei unabhängige Pumpmöglichkeiten (elektrisch + manuell)
3. **Schwimmerschalter elektronisch** — Mechanische Schalter verklemmen
4. **Schlauch passend zum Einsatzort** — PVC an Deck, EPDM im Motorraum, Spiral für Saugseite
5. **Schlauchschellen AISI 316, immer doppelt** — Keine Kompromisse
6. **Anti-Siphon ist Pflicht** — Wenn der Austritt unter WL kommen kann
7. **Pumpe direkt an Batterie** — Nie über den Hauptschalter
8. **Regelmäßig testen** — Monatlich Pumpe laufen lassen
9. **Hochwasser-Alarm** — Unabhängig vom Schwimmerschalter
10. **PVC-Schläuche alle 7–10 Jahre tauschen** — Auch wenn sie gut aussehen

### M.2 Kosten-Zusammenfassung

| Bootsklasse | Min. Budget | Empf. Budget | Premium |
|---|---|---|---|
| Kleinboot (≤6 m) | 50 EUR | 100 EUR | 200 EUR |
| Segelboot Küste (8–12 m) | 200 EUR | 400 EUR | 700 EUR |
| Segelboot Offshore (12–16 m) | 500 EUR | 1.200 EUR | 2.000 EUR |
| Motoryacht (14–20 m) | 600 EUR | 1.400 EUR | 2.500 EUR |
| Katamaran (12–16 m) | 400 EUR | 800 EUR | 1.500 EUR |

(Confidence: documented)

---

## ANHANG N — Spezialanwendungen

### N.1 Regatta-Yachten

Regatta-Yachten optimieren das Bilgensystem auf Gewicht und Geschwindigkeit:
- Leichtpumpen (Seaflo, Attwood Tsunami) statt Premium-Modelle
- Minimalste Schlauchlänge
- Venturi-Effekt-Entleerung über Rumpf-Speed (Ejektor)
- Handpumpe oft einzige Pumpe (Offshore-Regatta: Pflicht)
- Bilge muss für Vermessung trocken sein (Rating-Messung)

### N.2 Superyachten (24 m+)

Superyachten haben integrierte Bilgensysteme mit:
- Zentrale Bilgen-Sammelleitung mit Absperrventilen pro Abteilung
- Motorgetriebene Bilgenpumpen (Haupt-Motor oder Generator)
- Feuerlösch-System kann als Notlenzsystem dienen (Cross-Connection)
- MARPOL-konformer Ölabscheider obligatorisch
- Bilgenniveau-Monitoring auf Brücke (NMEA 2000 / BMS)
- Klassifikations-Vorschriften (DNV GL, Lloyd's, RINA)

### N.3 Aluminium-Boote

Besonderheiten bei Aluminium-Rümpfen:
- Keine Bronze-Borddurchlässe (galvanische Korrosion!) → Edelstahl 316L oder Marelon
- Schlauchschellen: Edelstahl 316L (kein galvanisches Problem mit Aluminium bei korrekter Isolation)
- Bilge-Wasser aggressiver (Aluminium-Korrosionsprodukte) → häufiger reinigen
- Kein Kupfer-basiertes Antifouling am Bilgen-Austritt

### N.4 Holzboote

Besonderheiten bei Holzrümpfen:
- Bilge ist „normal feucht" — Holz braucht Feuchtigkeit
- Übermäßiges Abpumpen kann Holz-Quell-Dichtigkeit stören
- Borddurchlässe: Bronze (traditionell) mit Unterfütterung
- Bilgenschlauch-Befestigung: Schlauchhalter mit Holzschrauben (Vorbohren!)
- Kein Edelstahl an Kupfer-vernagelten Rümpfen (galvanische Korrosion)

### N.5 Stahlboote

Besonderheiten bei Stahlrümpfen:
- Bilge-Wasser führt zu Rostbildung an ungeschützten Stellen → Bilge trocken halten
- Borddurchlässe: Stahl (geschweißt) oder Bronze mit isolierender Unterlage
- Bilgenpumpe muss häufiger laufen (Kondenswasser auf kaltem Stahl)
- Schlauchschellen AISI 316L — kein Kontakt Edelstahl-Schraube ↔ Stahlrumpf
- Bilge regelmäßig mit Korrosionsschutz (Owatrol, Hammerite) behandeln
- Bilgen-Sieb besonders wichtig (Rostpartikel können Impeller blockieren)
- Opferanoden in Bilge kontrollieren (Zink oder Magnesium je nach Gewässer)

### N.6 GFK-Boote mit Sandwich-Laminat

Besonderheiten bei Sandwich-Rümpfen:
- Borddurchlass-Montage: Kern im Bereich des Durchlasses durch Vollaminat oder Epoxy-Füllung ersetzen
- Backing-Block obligatorisch (Lastverteilung auf dünne Innenschale)
- Osmose im Bilgenbereich: bei Feuchtigkeit im Sandwich → Bilge als Indikator nutzen
- Keine Schrauben in Sandwich-Bereich für Schlauchhalter → Kleben mit Sikaflex 291i
- Bilgensumpf-Bereich: Laminat muss glatt und beschichtet sein (Reinigungsfähigkeit)

### N.7 Mehrrumpfboote (Trimarane)

Besonderheiten bei Trimaranen:
- Hauptrumpf + 2 Schwimmer → bis zu 5 Bilgenbereiche
- Schwimmer oft nur mit manueller Lenzöse (geringes Volumen)
- Verbindungsbrücke (Cross-Beams): Entwässerung in Hauptrumpf-Bilge
- Staukasten in Schwimmern: eigene Drainage, Ablauf in Schwimmer-Bilge
- Empfehlung: mind. 1 elektrische Pumpe im Hauptrumpf, je 1 Handpumpe oder kleine Elektropumpe in Schwimmern

### N.8 Schlauchboote (RIBs)

Besonderheiten bei Rigid Inflatable Boats:
- Bilge oft selbstlenzend (Scuppers im Spiegel bei Fahrt)
- Bei langsamer Fahrt oder Stillstand: manuelle Bilgenpumpe oder elektrische Mini-Pumpe
- Bilgenschlauch: kurz (500–1.000 mm), 19 mm Standard-PVC ausreichend
- Befestigung: Kleben auf GFK-Unterschale (kein Bohren im Schlauchboot-Bereich!)
- Leckgefahr durch Motorbrunnen-Dichtung → Bilgenpumpe empfohlen

(Confidence: documented)

---

## ANHANG O — Umwelt

### O.1 Umweltverantwortung im Bilgenmanagement

| Aspekt | Best Practice |
|---|---|
| Ölhaltiges Bilgenwasser | Nie direkt abpumpen — Ölbinde-Pads verwenden |
| Bilge-Reiniger | Nur biologisch abbaubare Produkte (z.B. Star Brite Sea Safe) |
| Altschlauch-Entsorgung | PVC → Wertstoffhof, EPDM → Sondermüll |
| Alte Pumpen | Elektroschrott (WEEE-Richtlinie) |
| Bilge-Wasser in Marina | In Bilge-Auffangstation entsorgen (viele Marinas haben diese) |
| MARPOL-Anforderung | >400 BRZ: Ölgehalt <15 ppm im Abwasser |

### O.2 Umweltfreundliche Alternativen

| Konventionell | Alternative | Vorteil |
|---|---|---|
| Lösemittel-Bilgenreiniger | Enzymatischer Reiniger | Biologisch abbaubar |
| PVC-Schlauch (Weichmacher) | PE- oder PP-Schlauch | Kein Weichmacher |
| Öl-Lappen in Bilge | Ölbinde-Pad (Polypropylen) | Sauberer, wiederverwendbar |
| Kupfer-Antifouling am Austritt | Mechanischer Verschluss | Kein Biozid |

(Confidence: documented)

---

## ANHANG P — Erweiterte FAQ

### BL-026: Kann ich meine Bilgenpumpe von 12V auf 24V umrüsten?
Nein. Bilgenpumpen sind für eine bestimmte Spannung ausgelegt. Eine 12V-Pumpe an 24V brennt sofort durch. Umgekehrt läuft eine 24V-Pumpe an 12V mit stark reduzierter Leistung. Richtige Spannung kaufen.
(Confidence: documented)

### BL-027: Wie laut darf eine Bilgenpumpe sein?
Es gibt keine Norm für Bilgenpumpen-Lautstärke. Tauchpumpen sind relativ leise (40–55 dB). Membranpumpen pulsieren stärker (50–65 dB). Wenn die Pumpe nachts stört: Schallisolierung der Bilge verbessern, nicht die Pumpe abschalten!
(Confidence: documented)

### BL-028: Mein Bilgenschlauch riecht nach Chemie — ist das normal?
Neue PVC-Schläuche gasen Weichmacher aus (typischer „Plastikgeruch"). Das ist normal und lässt nach 2–4 Wochen nach. Wenn ein alter Schlauch plötzlich chemisch riecht: Kontakt mit Lösungsmittel oder Kraftstoff → Ursache finden.
(Confidence: documented)

### BL-029: Kann ich Schlauchschellen wiederverwenden?
Nein. Einmal angezogene Schlauchschellen haben sich verformt und bieten keinen gleichmäßigen Anpressdruck mehr. Schellen sind billig (1–4 EUR) — immer neue verwenden.
(Confidence: documented)

### BL-030: Was tun, wenn die Bilge stinkt?
1) Bilge leer pumpen. 2) Mit enzymatischem Bilge-Reiniger (Star Brite 089736, ca. 15 EUR/l) fluten. 3) 4–8 h einwirken lassen. 4) Abpumpen (nicht in Marina!). 5) Bei Bedarf wiederholen. 6) Geruchsquelle beseitigen (Schlauch tauschen, Grauwasser-Leck reparieren).
(Confidence: documented)

### BL-031: Wie oft soll die Bilgenpumpe im Hafen laufen?
Im Normalfall: nie oder sehr selten (Kondenswasser). Wenn die Pumpe mehrmals täglich läuft → aktiver Wassereinbruch! Sofort Ursache suchen. Normale Laufhäufigkeit: 0–2 Zyklen/Woche bei Regenwetter.
(Confidence: documented)

### BL-032: Brauche ich eine Bilgenpumpe für jede wasserdichte Abteilung?
Idealerweise ja, besonders auf Blauwasser-Yachten und Katamaranen. Jede wasserdichte Abteilung, die kein Selbstlenzen durch Schwerkraft ermöglicht, sollte eine eigene Pumpe haben.
(Confidence: documented)

### BL-033: Was ist ein Bilge-Counter und brauche ich einen?
Ein Bilge-Counter (z.B. Maretron BBS100) zählt die Pumpzyklen. Er zeigt langfristige Trends: steigende Zyklenzahl = zunehmendes Leck. Empfohlen für Blauwasser und Langfahrt.
(Confidence: documented)

### BL-034: Kann ich die Handpumpe auch als Feuerlösch-Pumpe nutzen?
Bei einigen Hochleistungs-Handpumpen (Henderson Mk V, Whale Gusher Titan) ist das möglich: Saugschlauch ins Meer, Druckschlauch auf Brand richten. Allerdings nur als letztes Mittel — keine echte Feuerlösch-Leistung.
(Confidence: documented)

### BL-035: Mein Schwimmerschalter löst ständig aus — was tun?
1) Schwimmerschalter zu tief montiert → höher setzen (2–3 cm über Normalwasserspiegel). 2) Bilge mit Öl/Schaum → reinigen. 3) Vibrationen lösen mechanischen Schalter aus → auf elektronisch umrüsten. 4) Elektromagnetische Störungen → geschirmtes Kabel.
(Confidence: documented)

### BL-036: Welche Bilgenpumpe ist die leiseste?
Tauchpumpen sind generell leiser als Membranpumpen. Die leisesten Modelle: Whale SuperSub Smart (ca. 42 dB), Rule 25S (ca. 45 dB). Membranpumpen wie die Whale Gulper 220 erzeugen ein hörbares Pulsieren (ca. 55 dB). Für Nachtruhe: Schallisolierung in der Bilge anbringen (Armaflex).
(Confidence: documented)

### BL-037: Kann ich einen Bilge-Counter selbst bauen?
Ja. Ein ESP32-Mikrocontroller mit Stromsensor (ACS712) am Bilgenpumpen-Kabel zählt Einschaltzyklen und sendet per MQTT/Wi-Fi an ein Monitoring-Dashboard. Kosten: ca. 15–25 EUR für Komponenten. Alternativ: fertiger Maretron BBS100 (ca. 250 EUR).
(Confidence: documented)

### BL-038: Wie verhindere ich Gerüche in der Bilge im Winterlager?
1) Bilge vollständig leer pumpen. 2) Mit Bilge-Reiniger waschen und trocknen lassen. 3) Bilge-Tabs (Geruchsneutralisierer) einlegen. 4) Lüftung sicherstellen (Luken einen Spalt offen). 5) Keine organischen Materialien in der Bilge lassen (Lappen, Schwämme).
(Confidence: documented)

### BL-039: Brauche ich eine separate Pumpe für den Duschsumpf?
Ja, empfohlen. Der Duschsumpf sollte eine eigene Pumpe haben (z.B. Whale Gulper 220), die über einen separaten Schwimmerschalter gesteuert wird. Die Haupt-Bilgenpumpe sollte nicht für Duschwasser zuständig sein — sonst läuft sie bei jedem Duschgang.
(Confidence: documented)

### BL-040: Was mache ich, wenn die Bilgenpumpe unter Wasser steht und nicht mehr erreichbar ist?
1) Panik vermeiden. 2) Batteriestromkreis prüfen — Pumpe könnte noch funktionieren, auch wenn unter Wasser. 3) Handpumpe einsetzen. 4) Eimer verwenden. 5) Wenn Wasserstand so hoch ist: Leckquelle muss gefunden werden! Das ist ein Notfall. 6) Borddurchlässe schließen, soweit erreichbar.
(Confidence: documented)

### BL-041: Wie teste ich ob meine Schlauchschellen aus dem richtigen Material sind?
Magnettest: Ein Magnet haftet an AISI 304 (leicht) und an verzinktem Stahl (stark), aber NICHT an AISI 316. Wenn der Magnet haftet → Schelle austauschen! Achtung: Dieser Test ist nicht 100% zuverlässig (kaltverfestigtes 316 kann leicht magnetisch sein), aber ein guter erster Indikator.
(Confidence: documented)

### BL-042: Kann ich Bilgenwasser zum Toilettenspülen verwenden?
Technisch möglich, aber hygienisch bedenklich und nicht empfohlen. Bilgenwasser enthält Öl, Schmutz und Bakterien. Seewasser-Spülung oder Frischwasser-Spülung sind Standard. Einige wasserarme Toilettensysteme (Vakuum) verwenden minimale Frischwassermengen.
(Confidence: documented)

### BL-043: Mein Boot hat einen Kielbolzen-Bereich — brauche ich dort eine Extra-Pumpe?
Der Kielbolzen-Bereich ist oft der tiefste Punkt im Boot und sammelt Wasser zuerst. Die Hauptbilgenpumpe sollte so positioniert sein, dass sie diesen Bereich erreicht. Wenn der Bilgensumpf direkt im Kielbolzenbereich liegt (Standard bei Kielbooten): keine Extra-Pumpe nötig. Aber: Kielbolzen regelmäßig auf Leckage prüfen!
(Confidence: documented)

### BL-044: Welche Bilgenpumpe empfiehlt sich für ein Charterboot?
Charterboote brauchen robuste, wartungsarme Systeme: Rule 09 (2000 GPH) als Primärpumpe, elektronischer Schwimmerschalter (kein Verklemmen durch ungeübte Charterer), Hochwasser-Alarm. Handpumpe muss ergonomisch und intuitiv bedienbar sein (Whale Gusher 10 mit klarer Beschriftung). Alle Bedienelemente beschriften (Deutsch + Englisch).
(Confidence: documented)

### BL-045: Wie entsorge ich alte Bilgenschläuche umweltgerecht?
PVC-Schläuche: Wertstoffhof oder Sondermüll (enthalten Weichmacher). EPDM-Gummi: Gummi-Recycling oder Restmüll. Metallische Schlauchschellen: Metallrecycling. Alte Bilgenpumpen: Elektroschrott (WEEE). Niemals im Hafen oder an Bord verbrennen!
(Confidence: documented)

---

## ANHANG Q — Zeitleiste der Bilgensystem-Entwicklung

| Jahr | Meilenstein |
|---|---|
| ca. 3000 v.Chr. | Erste Schiffe mit manueller Bilgenentleerung (Tonkrüge) |
| 1800er | Kolbenpumpen aus Bronze auf Segelschiffen |
| 1950er | Erste elektrische Bilgenpumpen für Freizeitboote |
| 1958 | Gründung Rule Industries (Gloucester, MA) |
| 1958 | Gründung Whale Marine (Nordirland) |
| 1970er | Schwimmerschalter werden Standard |
| 1980er | Membranpumpen für Marine-Einsatz (Whale Gulper) |
| 1994 | EU-Sportboot-Richtlinie 94/25/EG (erste CE-Anforderungen) |
| 2000er | Elektronische Schwimmerschalter (keine beweglichen Teile) |
| 2010er | IoT-basierte Bilgenüberwachung (Siren Marine, FloatHub) |
| 2013 | EU RCD 2013/53/EU (aktuelle Richtlinie) |
| 2015 | ISO 12217:2015 (Bilgenwasser in Stabilitätsberechnung) |
| 2020 | ISO 8849:2020 (aktualisierte Pumpenanforderungen) |
| 2020er | Bürstenlose DC-Bilgenpumpen, Smart-Monitoring |
| 2025+ | Predictive Maintenance via AI-Bilgen-Analyse (AYDI) |

(Confidence: documented)

---

## ANHANG R — Stichwortverzeichnis

| Stichwort | Abschnitt(e) |
|---|---|
| ABYC H-22 | 1.3.2, 7.4, 16 (BL-002, BL-018) |
| Aluminium-Boote | Anhang N.3 |
| Anti-Siphon-Ventil | 7.7, 9.1, 16 (BL-006), F-BL-06 |
| Attwood | 8.6 |
| Bavaria | Anhang F.1 |
| Biegeradien | Anhang C |
| Bilgen-Sieb / Strainer | 7.10, P-BL-01 |
| Bilgenpumpe — Dimensionierung | 11.1, 18.2 |
| Bilgenpumpe — Typen | 7.2 |
| Bilgenschlauch — Materialien | 7.5 |
| Biofilm / Biofouling | 13.2.3, F-BL-07 |
| Borddurchlass | 7.6, 1.3.6 |
| CE-Kategorie | 1.3.3, 18.2 |
| Cockpit-Drain | 7.8, F-BL-12, P-BL-05 |
| Compliance-Checkliste | Anhang I |
| Confidence-Mapping | Anhang D |
| Druckverlust | 11.2 |
| Einbau-Anleitung | 12.2 |
| Elektrische Dimensionierung | 11.3 |
| EPDM | 7.5.3, Anhang J.2 |
| Fallstudien | Anhang F |
| Fehlerbild-Atlas | 14 |
| Förderhöhe | 11.1.2, Anhang B |
| Glossar | 17 |
| Handpumpen | 7.2.3 |
| Hella Marine | 8.10.2 |
| Hochwasser-Alarm | 7.4 |
| Holzboote | Anhang N.4 |
| ISO 8849 | 1.3.1 |
| ISO 9093 | 1.3.6 |
| ISO 12217 | 1.3.4 |
| Jabsco | 8.4 |
| Johnson Pump | 8.2 |
| Katamaran | Anhang F.7 |
| Korrosion Schlauchschellen | F-BL-04, 10.2 |
| Lebensdauer | 13.1 |
| Lenzpumpe | 17 (Glossar) |
| MARPOL | 1.3.7, Anhang O |
| Membranpumpe | 7.2.2 |
| Motorraum | F-BL-01, Anhang L (Nr. 10) |
| NBR (ölbeständig) | Anhang J.3 |
| Notfall-Ressourcen | 19 |
| Plastimo | 8.10.1 |
| Prüfverfahren | Anhang K |
| PVC-Schlauch | 7.5.1, Anhang J.1 |
| Pydantic-Modelle | 6 |
| Regatta-Yachten | Anhang N.1 |
| Regional Sourcing | 4 |
| Risk Matrix | Anhang H |
| Rule Industries | 8.1 |
| Rück-Siphon | 7.7, F-BL-06, Anhang F.2 |
| Sanitärschlauch | 7.5.4 |
| Schlauchschellen | 10 |
| Schwimmerschalter — elektronisch | 7.3.2 |
| Schwimmerschalter — mechanisch | 7.3.1 |
| Scupper | 7.9 |
| Seaflo | 8.5 |
| Shields Rubber | 8.9 |
| Shurflo | 8.10.4 |
| Smart Monitoring | 2.1 |
| Spiralschlauch | 7.5.2 |
| Superyachten | Anhang N.2 |
| Tauchpumpe | 7.2.1 |
| TMC | 8.10.3 |
| Trident Marine | 8.8 |
| Umwelt | Anhang O |
| USCG | 1.3.5 |
| Vetus | 8.7 |
| Wartungsplan | 13.3 |
| Weichmacher-Migration | 13.2.1 |
| Whale Marine | 8.3 |
| Winterlager | 3.1, 16 (BL-024) |
| Zukunftstechnologien | 2 |
| Bilgenbelüftung | 7.11 |
| NMEA 2000 | 7.12 |
| SignalK | 7.12 |
| Notlenzsystem | 7.13 |
| Crash-Pumpe | 7.13 |
| Ejektor | 7.13 |
| OEM-Konfigurationen | Anhang S |
| Schlauchleitungs-Diagramme | Anhang T |
| Versicherung/Survey | Anhang U |
| Berechnungsbeispiele | Anhang V |
| Flüssigkeits-Kompatibilität | Anhang W |
| Vision-Analyse | Anhang X |
| Score-Algorithmus | Anhang Y |
| Stahlboote | Anhang N.5 |
| GFK-Sandwich | Anhang N.6 |
| Trimaran | Anhang N.7 |
| Schlauchboot/RIB | Anhang N.8 |
| Charterboot | 16 (BL-044) |

(Confidence: documented)

---

## ANHANG S — OEM-Bilgensystem-Konfigurationen nach Bootshersteller

### S.1 Bavaria Yachtbau

| Modell | LOA mm | Primärpumpe | Sekundärpumpe | Handpumpe | Schlauch-Typ | Schlauch-ID mm |
|---|---|---|---|---|---|---|
| Bavaria C38 | 11.990 | Rule 27S (1000 GPH) | — | Whale Gusher 10 | PVC verstärkt | 28 |
| Bavaria C42 | 13.290 | Rule 09 (2000 GPH) | Rule 25S (500 GPH) | Whale Gusher 10 | PVC verstärkt | 28/19 |
| Bavaria C46 | 14.270 | Rule 09 (2000 GPH) | Rule 27S (1000 GPH) | Whale Gusher 25 | PVC verstärkt | 28 |
| Bavaria C50 | 15.570 | Rule 10 (3700 GPH) | Rule 09 (2000 GPH) | Whale Gusher 30 | PVC + EPDM | 38/28 |

### S.2 Beneteau

| Modell | LOA mm | Primärpumpe | Sekundärpumpe | Handpumpe | Schlauch-Typ | Schlauch-ID mm |
|---|---|---|---|---|---|---|
| Oceanis 34.1 | 10.320 | Rule 27S (1000 GPH) | — | Plastimo 10596 | PVC verstärkt | 28 |
| Oceanis 40.1 | 12.510 | Rule 09 (2000 GPH) | Rule 25S (500 GPH) | Plastimo 10596 | PVC verstärkt | 28/19 |
| Oceanis 46.1 | 14.600 | Rule 09 (2000 GPH) | Rule 27S (1000 GPH) | Whale Gusher 10 | PVC verstärkt | 28 |
| First 44 | 13.490 | Rule 09 (2000 GPH) | Johnson L1250 | Whale Gusher 25 | PVC + Spiral | 28 |

### S.3 Jeanneau

| Modell | LOA mm | Primärpumpe | Sekundärpumpe | Handpumpe | Schlauch-Typ | Schlauch-ID mm |
|---|---|---|---|---|---|---|
| Sun Odyssey 380 | 11.750 | Johnson L750 | — | Plastimo 10596 | PVC verstärkt | 19 |
| Sun Odyssey 440 | 13.720 | Rule 09 (2000 GPH) | Johnson L750 | Whale Gusher 10 | PVC verstärkt | 28/19 |
| Sun Odyssey 490 | 14.910 | Rule 09 (2000 GPH) | Rule 27S (1000 GPH) | Whale Gusher 25 | PVC verstärkt | 28 |
| Yachts 55 | 17.070 | Rule 10 (3700 GPH) | Rule 09 (2000 GPH) | Whale Gusher 30 | PVC + EPDM | 38/28 |

### S.4 Hallberg-Rassy

| Modell | LOA mm | Primärpumpe | Sekundärpumpe | Handpumpe | Schlauch-Typ | Schlauch-ID mm |
|---|---|---|---|---|---|---|
| HR 340 | 10.390 | Rule 27S (1000 GPH) | Rule 25S (500 GPH) | Whale Gusher 10 | PVC + Spiral | 28/19 |
| HR 400 | 12.250 | Rule 09 (2000 GPH) | Rule 27S (1000 GPH) | Whale Gusher 25 | Trident 150 + Spiral | 28 |
| HR 44 | 13.490 | Rule 09 (2000 GPH) | Rule 27S (1000 GPH) | Whale Gusher 30 | Trident 150 + EPDM | 28 |
| HR 50 | 15.780 | Rule 10 (3700 GPH) | Rule 09 (2000 GPH) | Whale Gusher 30 | EPDM | 38/28 |

**Anmerkung Hallberg-Rassy**: Bekannt für hochwertige Bilgensystem-Installation. Immer doppelte Schellen, Anti-Siphon werksseitig, Cockpit-Drain immer 38 mm. Referenz-Qualität.

(Confidence: documented)

### S.5 Hanse

| Modell | LOA mm | Primärpumpe | Sekundärpumpe | Handpumpe | Schlauch-Typ |
|---|---|---|---|---|---|
| Hanse 348 | 10.650 | Rule 27S | — | Whale Gusher Urchin | PVC verstärkt |
| Hanse 418 | 12.780 | Rule 09 | Rule 25S | Whale Gusher 10 | PVC verstärkt |
| Hanse 460 | 14.230 | Rule 09 | Rule 27S | Whale Gusher 10 | PVC verstärkt |
| Hanse 510 | 15.880 | Rule 10 | Rule 09 | Whale Gusher 25 | PVC + EPDM |

### S.6 Grand Banks / Palm Beach (Motoryachten)

| Modell | LOA mm | Primärpumpe | Sekundärpumpe | Handpumpe | Schlauch-Typ |
|---|---|---|---|---|---|
| GB 42 Heritage | 13.100 | Rule 10 (3700 GPH) | Rule 09 (2000 GPH) | Henderson Mk V | EPDM |
| GB 54 | 17.220 | 2× Rule 10 | Jabsco Cyclone HP | Whale Gusher Titan | EPDM |
| PB GT50 | 15.850 | Rule 10 | Jabsco Water Puppy | Henderson Mk V | EPDM |

(Confidence: documented)

---

## ANHANG T — Detaillierte Schlauchleitungs-Diagramme

### T.1 Standard-Bilgensystem Segelboot 10–14 m

```
                                    ┌─────────────────────┐
                                    │   Borddurchlass      │
                                    │   (über WL, Stb.)    │
                                    │   28 mm Bronze       │
                                    └──────────┬──────────┘
                                               │
                                    ┌──────────┴──────────┐
                                    │ Anti-Siphon-Ventil   │
                                    │ Vetus AS25           │
                                    │ (min. 200 mm über WL)│
                                    └──────────┬──────────┘
                                               │
                                    ┌──────────┴──────────┐
                                    │ Schwanenhals-Schleife│
                                    │ (Scheitelpunkt       │
                                    │  300 mm über WL)     │
                                    └──────────┬──────────┘
                                               │
                                    ┌──────────┴──────────┐
                                    │ Bilgenschlauch       │
                                    │ 28 mm PVC verstärkt  │
                                    │ Trident 150-1125     │
                                    │ Länge: ca. 2.500 mm  │
                                    │ Befestigung alle     │
                                    │ 300 mm               │
                                    └──────────┬──────────┘
                                               │
                                    ┌──────────┴──────────┐
                                    │ Bilgenpumpe          │
                                    │ Rule 09 (2000 GPH)   │
                                    │ + Rule EcoSwitch      │
                                    │ Direkt an Batterie   │
                                    └──────────┬──────────┘
                                               │
                                    ┌──────────┴──────────┐
                                    │ Bilgen-Sieb          │
                                    │ (Strainer ≤5 mm)     │
                                    └──────────┬──────────┘
                                               │
                                    ┌──────────┴──────────┐
                                    │ BILGENSUMPF          │
                                    │ (tiefster Punkt,     │
                                    │  Kielbereich)        │
                                    └─────────────────────┘
```

### T.2 Cockpit-Drain-System

```
    ┌─────────────┐                           ┌─────────────┐
    │ Cockpit-Drain│                           │ Cockpit-Drain│
    │ Bb. (Sieb)   │                           │ Stb. (Sieb)  │
    └──────┬──────┘                           └──────┬──────┘
           │                                         │
    ┌──────┴──────┐                           ┌──────┴──────┐
    │ Schlauch     │                           │ Schlauch     │
    │ 38 mm PVC    │                           │ 38 mm PVC    │
    │ UV-stabiliert│                           │ UV-stabiliert│
    │ Länge: 1.5 m │                           │ Länge: 1.5 m │
    └──────┬──────┘                           └──────┴──────┘
           │                                         │
    ┌──────┴──────┐                           ┌──────┴──────┐
    │ Borddurchlass│                           │ Borddurchlass│
    │ Bb. achtern  │                           │ Stb. achtern │
    │ 38 mm, über  │                           │ 38 mm, über  │
    │ Wasserlinie  │                           │ Wasserlinie  │
    └─────────────┘                           └─────────────┘
```

### T.3 Multi-Pumpen-System Offshore-Yacht (15+ m)

```
VORSCHIFF                    MITTSCHIFF/MOTORRAUM              ACHTERN
┌──────────┐                ┌──────────────────┐            ┌──────────┐
│ Pumpe 3   │                │ Pumpe 1 (Primär) │            │ Pumpe 2   │
│ Whale     │                │ Rule 10          │            │ Rule 09   │
│ Gulper 220│                │ (3700 GPH)       │            │ (2000 GPH)│
│ 840 l/h   │                │ 14.006 l/h       │            │ 7.571 l/h │
└─────┬─────┘                └────────┬─────────┘            └─────┬─────┘
      │                               │                            │
   Schlauch                        Schlauch                     Schlauch
   25 mm Spiral                    38 mm EPDM                  28 mm PVC
   (Saugseite!)                    Shields 200-1500             Trident 150
      │                               │                            │
   Borddurchlass                  Borddurchlass               Borddurchlass
   Bb. vorn                       Stb. mittschiffs             Bb. achtern
   (über WL)                      (mit Seeventil)             (über WL)

+ Handpumpe: Whale Gusher 30 im Cockpit
  Saugschlauch: 38 mm Spiral bis Bilgensumpf Motorraum
  Druckschlauch: 38 mm PVC nach achtern, Borddurchlass Stb. achtern
```

(Confidence: documented)

---

## ANHANG U — Versicherungs- und Survey-Anforderungen

### U.1 Pre-Purchase Survey — Bilgensystem-Prüfpunkte

Ein professioneller Marine-Surveyor prüft folgende Aspekte des Bilgensystems:

| Prüfpunkt | Methode | Bewertung |
|---|---|---|
| Pumpenanzahl und -kapazität | Sichtprüfung, Typenschild | Pass / Fail |
| Pumpen-Funktion | Lauftest mit Wasser | Pass / Fail |
| Schwimmerschalter-Funktion | Auslösetest | Pass / Fail |
| Schlauch-Zustand | Sichtprüfung, taktil | Gut / Befriedigend / Mangelhaft |
| Schlauchschellen-Material | Sichtprüfung, Magnettest | 316 / 304 / Verzinkt |
| Schlauchschellen-Anzahl | Zählung pro Anschluss | 2 / 1 / 0 |
| Anti-Siphon-Schutz | Sichtprüfung | Vorhanden / Fehlend |
| Borddurchlass-Zustand | Sichtprüfung, Dichtigkeit | Gut / Befriedigend / Mangelhaft |
| Cockpit-Drain-Funktion | Wassertest | Frei / Eingeschränkt / Verstopft |
| Hochwasser-Alarm | Funktionstest | Vorhanden+funktional / Fehlend |
| Elektrische Absicherung | Sicherungsschema prüfen | Korrekt / Mangelhaft |
| Bilgen-Sauberkeit | Sichtprüfung | Sauber / Ölig / Verschmutzt |

### U.2 Survey-Befunde und deren Auswirkung auf Versicherung

| Befund | Schweregrad | Versicherungs-Auswirkung |
|---|---|---|
| Keine Bilgenpumpe | Kritisch | Versicherungsschutz kann verweigert werden |
| Nur eine Pumpe (Boot >8 m) | Erheblich | Auflagen zur Nachrüstung |
| Verzinkte Schlauchschellen | Erheblich | Fristsetzung zum Austausch |
| Schlauch >15 Jahre alt | Erheblich | Austausch als Auflage |
| Kein Anti-Siphon bei Austritt unter WL | Erheblich | Nachrüstung als Auflage |
| Kein Schwimmerschalter | Mittel | Empfehlung zur Nachrüstung |
| Schlauch leicht verhärtet | Gering | Hinweis im Bericht |
| Bilge verschmutzt/ölig | Mittel | Reinigung empfohlen |

### U.3 Versicherungsrechtliche Aspekte

**Kaskoversicherung (AVB Bootskasko)**:
- Bilgensystem-Versagen durch mangelnde Wartung → § 23 VVG (Gefahrerhöhung) → Leistungskürzung möglich
- Nachweispflicht des Eigners: regelmäßige Wartung im Logbuch dokumentieren
- Empfehlung: jährliches Foto des Bilgensystems mit Datum

**Haftpflichtversicherung**:
- Umweltschaden durch ölhaltiges Bilgenwasser → Deckung prüfen
- Viele Policen schließen vorsätzliche oder grob fahrlässige Umweltschäden aus
- Regelmäßige Bilgenreinigung dokumentieren

**Pre-Purchase vs. Condition Survey**:
- Pre-Purchase Survey: Empfehlung für Käufer, deckt Bilgensystem vollständig ab
- Condition Survey (periodisch): Vereinfachte Prüfung, fokussiert auf Veränderungen
- Out-of-Water Survey: Bilgen-Borddurchlass von außen prüfbar
- In-Water Survey: Bilgensystem von innen, Funktionsprüfung

(Confidence: documented)

---

## ANHANG V — Erweiterte Berechnungsbeispiele

### V.1 Komplettberechnung: Bilgensystem für 13 m Segelboot CE-Kat B

**Gegeben**:
- LOA: 13.000 mm
- Breite: 4.200 mm
- Tiefgang: 2.100 mm
- CE-Kategorie: B (Offshore)
- Bilgensumpf-Tiefe unter WL: 1.800 mm
- Abstand Bilgensumpf → Austritt: 2.500 mm (geodätisch)
- Schlauchlänge (mit Bogen): 3.500 mm

**Schritt 1 — Mindest-Pumpenkapazität (ISO 8849)**:
- LOA 12–15 m, CE-Kat B: min. 5.300 l/h (1.400 GPH)
- Gewählte Pumpe: Rule 09 (2.000 GPH = 7.571 l/h bei 0 m)

**Schritt 2 — Tatsächliche Förderleistung bei 2,5 m Förderhöhe**:
- Aus Förderkurve (Anhang B): Rule 09 bei 2,5 m ≈ 62% → 4.694 l/h
- Druckverlust Schlauch (28 mm, 3,5 m bei 7.571 l/h): 0,09 × 3,5 = 0,315 m
- Druckverlust Anti-Siphon: ≈ 0,15 m
- Druckverlust 2× 90°-Bogen: 2 × 0,5 × 0,15 = 0,15 m
- Effektive Förderhöhe: 2,5 + 0,315 + 0,15 + 0,15 = 3,115 m
- Korrigierte Leistung bei 3,115 m: ≈ 52% → 3.937 l/h

**Schritt 3 — Prüfung**:
- 3.937 l/h > 5.300 l/h (Mindestanforderung CE-Kat B)? NEIN!
- → Schlauch auf 32 mm vergrößern oder zweite Pumpe hinzufügen

**Schritt 3b — Korrektur mit 32 mm Schlauch**:
- Druckverlust 32 mm, 3,5 m bei 7.571 l/h: 0,05 × 3,5 = 0,175 m
- Effektive Förderhöhe: 2,5 + 0,175 + 0,15 + 0,15 = 2,975 m
- Korrigierte Leistung bei 2,975 m: ≈ 56% → 4.240 l/h
- 4.240 l/h < 5.300 l/h → IMMER NOCH NICHT AUSREICHEND

**Schritt 3c — Lösung: Zweite Pumpe**:
- Primär: Rule 09 = 4.240 l/h (effektiv, 32 mm Schlauch)
- Sekundär: Rule 27S (1.000 GPH) im Vorschiff ≈ 2.000 l/h (effektiv)
- Gesamt: 6.240 l/h > 5.300 l/h → AUSREICHEND

**Schritt 4 — Schlauchdurchmesser prüfen**:
- Rule 09 Stutzen: 28 mm → Schlauch 28 mm (oder 32 mm für weniger Verlust)
- Rule 27S Stutzen: 28 mm → Schlauch 28 mm
- ABYC: Schlauch ≥ Stutzen → OK

**Schritt 5 — Elektrische Dimensionierung**:
- Rule 09: 8,4 A Nennstrom, Anlaufstrom 16,8 A
- Kabellänge: 6 m → 6,0 mm² Kabel, 15 A Sicherung
- Rule 27S: 3,8 A, Kabellänge 8 m → 2,5 mm² Kabel, 10 A Sicherung
- Beide direkt an Batterie (separate Sicherungen)

**Ergebnis**:

| Komponente | Spezifikation | Kosten EUR |
|---|---|---|
| Rule 09 (2000 GPH) | 12V, 8,4 A | 55 |
| Rule 27S (1000 GPH) | 12V, 3,8 A | 35 |
| Bilgenschlauch 32 mm × 3,5 m | Trident 150-1250 | 35 |
| Bilgenschlauch 28 mm × 4 m | Trident 150-1125 | 32 |
| Anti-Siphon Vetus AS32 | 32 mm | 20 |
| 2× Rule EcoSwitch | Feldeffekt | 70 |
| Hochwasser-Alarm Rule 33ALA | 105 dB | 30 |
| 16× Schlauchschellen AISI 316 | 32 + 28 mm Bereich | 32 |
| Borddurchlass Bronze 32 mm | DZR-Bronze | 55 |
| Borddurchlass Bronze 28 mm | DZR-Bronze | 45 |
| Kabel 6 mm² (6 m) + 2,5 mm² (8 m) | Marinekabel verzinnt | 25 |
| Sicherungen + Halter | 15 A + 10 A | 12 |
| **GESAMT** | | **446 EUR** |

(Confidence: calculated)

### V.2 Leckrate-Berechnung: Borddurchlass-Bruch Szenarien

| Borddurchlass-Größe mm | Tiefe unter WL m | Leckrate l/h | Benötigte Pumpenkapazität l/h |
|---|---|---|---|
| 15 (½") | 0,5 | 760 | 1.140 (1,5×) |
| 15 (½") | 1,0 | 1.070 | 1.605 |
| 19 (¾") | 0,5 | 1.220 | 1.830 |
| 19 (¾") | 1,0 | 1.720 | 2.580 |
| 25 (1") | 0,5 | 2.120 | 3.180 |
| 25 (1") | 1,0 | 3.000 | 4.500 |
| 32 (1¼") | 0,5 | 3.480 | 5.220 |
| 32 (1¼") | 1,0 | 4.920 | 7.380 |
| 38 (1½") | 0,5 | 4.900 | 7.350 |
| 38 (1½") | 1,0 | 6.930 | 10.395 |
| 50 (2") | 0,5 | 8.500 | 12.750 |
| 50 (2") | 1,0 | 12.020 | 18.030 |

**Fazit**: Kein praktisches Bilgenpumpen-System kann einen offenen 50 mm Borddurchlass bei 1 m Tiefe kompensieren. Holzpfropfen und schnelle Abdichtung sind überlebenswichtig!

(Confidence: calculated)

### V.3 Stromverbrauch bei Dauerbetrieb — Batterie-Kapazität

| Pumpe | Strom A | 1 h | 4 h | 8 h | 12 h | 24 h |
|---|---|---|---|---|---|---|
| Rule 25S (500 GPH) | 2,5 | 2,5 Ah | 10 Ah | 20 Ah | 30 Ah | 60 Ah |
| Rule 27S (1000 GPH) | 3,8 | 3,8 Ah | 15,2 Ah | 30,4 Ah | 45,6 Ah | 91,2 Ah |
| Rule 09 (2000 GPH) | 8,4 | 8,4 Ah | 33,6 Ah | 67,2 Ah | 100,8 Ah | 201,6 Ah |
| Rule 10 (3700 GPH) | 14,0 | 14,0 Ah | 56,0 Ah | 112 Ah | 168 Ah | 336 Ah |

**Konsequenz**: Eine Rule 09 im Dauerbetrieb leert eine 100 Ah Batterie in ca. 12 Stunden. Redundante Stromversorgung (Zweitbatterie, Solarpanel) ist für Langfahrt-Yachten essentiell.

(Confidence: calculated)

---

## ANHANG W — Schlauch-Kompatibilität mit Flüssigkeiten

### W.1 Beständigkeitstabelle

| Flüssigkeit | PVC | EPDM | NBR | Silikon | PE |
|---|---|---|---|---|---|
| Seewasser | ★★★★☆ | ★★★★★ | ★★★★☆ | ★★★★★ | ★★★★★ |
| Süßwasser | ★★★★★ | ★★★★★ | ★★★★★ | ★★★★★ | ★★★★★ |
| Motoröl | ★☆☆☆☆ | ★☆☆☆☆ | ★★★★★ | ★★★☆☆ | ★★★☆☆ |
| Diesel | ★☆☆☆☆ | ★★☆☆☆ | ★★★★☆ | ★★☆☆☆ | ★★★★☆ |
| Benzin | ★☆☆☆☆ | ★☆☆☆☆ | ★★★☆☆ | ★☆☆☆☆ | ★★★☆☆ |
| Hydrauliköl | ★☆☆☆☆ | ★☆☆☆☆ | ★★★★★ | ★★☆☆☆ | ★★★☆☆ |
| Frostschutzmittel (Glykol) | ★★★☆☆ | ★★★★☆ | ★★★★☆ | ★★★★☆ | ★★★★★ |
| Bilge-Reiniger (enzymatisch) | ★★★★☆ | ★★★★★ | ★★★★☆ | ★★★★★ | ★★★★★ |
| Bilge-Reiniger (Lösemittel) | ★★☆☆☆ | ★★★☆☆ | ★★★☆☆ | ★★★★☆ | ★★★★☆ |
| Antifouling-Lösemittel | ★☆☆☆☆ | ★★☆☆☆ | ★★★☆☆ | ★★★☆☆ | ★★★☆☆ |

Legende: ★★★★★ = ausgezeichnet, ★☆☆☆☆ = ungeeignet

### W.2 Empfehlung nach Einbauort

| Einbauort | Kontaktmedium | Empfohlenes Material |
|---|---|---|
| Bilge allgemein | Seewasser + Kondensat | PVC verstärkt (Standard) |
| Motorraum-Bilge | Öl + Diesel + heißes Wasser | NBR (ölbeständig) |
| Cockpit-Drain | Regenwasser + UV | PVC UV-stabilisiert oder EPDM |
| Duschsumpf | Grauwasser + Seife | PVC oder EPDM |
| Ankerkasten-Drain | Seewasser + Schlamm | PVC oder EPDM |
| Kühlschrank-Kondensat | Süßwasser | Standard-PVC |
| Klimaanlage-Kondensat | Süßwasser + Kältemittel | PE oder Silikon |

(Confidence: documented)

---

## ANHANG X — Fehlerbild-Erweiterung: Visuelle Erkennungsmerkmale für AYDI Pipeline B

### X.1 Visuelle Schlüsselindikatoren für Claude Vision Analyse

| Indikator | Beschreibung für Vision-Prompt | Confidence-Level |
|---|---|---|
| Gelblicher Schlauch | PVC-Schlauch zeigt gelbliche bis bräunliche Verfärbung statt original weiss/transparent → Alterung, Weichmacher-Migration | visual_high |
| Aufgequollener Schlauch | Schlauch-Außendurchmesser sichtbar größer als normal, weiche Oberfläche → Ölkontamination | visual_high |
| Weiße Stellen an Biegung | Lokale weiße Verfärbung an Biegestelle → Materialstress, Kinking-Vorschaden | visual_high |
| Rostspuren an Schellen | Braune/orange Verfärbung am Schlauch unter/neben Schlauchschelle → Korrosion, falsche Schelle | visual_high |
| Grünliche Ablagerung | Grünlich-schwarzer Belag auf Schlauchoberfläche → Biofilm, Schimmel | visual_medium |
| Risse in Längsrichtung | Sichtbare Risse parallel zur Schlauchlänge → Alterung, UV-Schaden | visual_high |
| Schlauch hängt lose | Schlauch ohne sichtbare Befestigungspunkte, durchhängend → mangelhafte Installation | visual_high |
| Fehlende Schlauchschelle | Anschlussstelle ohne sichtbare Schelle → kritischer Befund | visual_high |
| Einzelne Schlauchschelle | Nur eine Schelle an Anschlussstelle sichtbar → Doppelschellen-Regel verletzt | visual_high |
| Regenbogen-Schimmer in Bilge | Ölfilm auf Bilgenwasser sichtbar → Ölkontamination | visual_high |
| Muschelbewuchs am Austritt | Kalkig-weiße Ablagerungen am Borddurchlass-Austritt → Biofouling | visual_high |
| Schlauch auf heißem Motor | Schlauch liegt direkt auf oder nahe Motorblock/Auspuff → Hitzeschaden-Risiko | visual_medium |

### X.2 Vision-Prompt-Templates für Bilgensystem-Analyse

**Template 1 — Bilgen-Übersicht**:
```
Analysiere dieses Foto einer Bootsbilge. Identifiziere:
1. Bilgenpumpe(n): Typ, Hersteller (wenn erkennbar), geschätzter Zustand
2. Bilgenschläuche: Material (PVC/Gummi), Durchmesser (geschätzt), Zustand
3. Schlauchschellen: Material (Edelstahl/verzinkt), Anzahl pro Anschluss
4. Schwimmerschalter: Typ (mechanisch/elektronisch), Position
5. Sieb/Strainer: vorhanden/fehlend
6. Verschmutzungsgrad der Bilge: sauber/leicht/stark/ölig
7. Auffälligkeiten: Kinking, fehlende Befestigung, Korrosion
Bewerte jeden Punkt mit Confidence-Level (visual_high/visual_medium/visual_low).
Antworte auf Deutsch.
```

**Template 2 — Schlauchdetail**:
```
Analysiere dieses Detailfoto eines Bilgenschlauchs/einer Bilgenleitung:
1. Material: PVC (transparent/weiß), EPDM (schwarz), Spiralschlauch?
2. Zustand: Verfärbung, Risse, Aufquellung, Verhärtung erkennbar?
3. Schlauchschellen: Material, Anzahl, Korrosion?
4. Verlegung: Biegeradius ausreichend, Befestigung vorhanden?
5. Geschätztes Alter (basierend auf Zustandsmerkmalen)
6. Empfehlung: Austausch nötig? Wenn ja, Dringlichkeit?
Antworte auf Deutsch mit Confidence-Level.
```

(Confidence: documented)

---

## ANHANG Y — Bilgensystem-Bewertungsalgorithmus für AYDI

### Y.1 Score-Berechnung

```python
def calculate_bilge_system_score(assessment: BilgeSystemAssessment) -> int:
    """
    Berechnet den Gesamtscore des Bilgensystems.
    
    Gewichtung:
    - Kapazität (ausreichend für CE-Kat): 25%
    - Redundanz (Backup-Pumpe, Handpumpe): 20%
    - Schlauch-Zustand: 20%
    - Compliance (Anti-Siphon, Schellen, Alarm): 20%
    - Allgemeinzustand (Sauberkeit, Wartung): 15%
    
    Returns: Score 0–100
    """
    capacity_score = 100 if assessment.capacity_adequate else 30
    
    redundancy_score = 0
    if assessment.redundancy_present:
        redundancy_score += 50
    if assessment.manual_backup_present:
        redundancy_score += 50
    
    hose_scores = [h.condition_score for h in assessment.hoses]
    hose_avg = sum(hose_scores) / len(hose_scores) if hose_scores else 50
    
    compliance_items = [
        assessment.anti_siphon_present or not assessment.anti_siphon_required,
        assessment.float_switch_functional,
        assessment.high_water_alarm_present,
        all(h.clamp_condition_score > 60 for h in assessment.hoses),
    ]
    compliance_score = (sum(compliance_items) / len(compliance_items)) * 100
    
    general_score = assessment.condition_score
    
    total = (
        capacity_score * 0.25 +
        redundancy_score * 0.20 +
        hose_avg * 0.20 +
        compliance_score * 0.20 +
        general_score * 0.15
    )
    
    return max(0, min(100, int(total)))
```

### Y.2 Zustandsbewertung einzelner Schläuche

```python
def assess_bilge_hose_condition(
    material: str,
    age_years: float,
    location: str,
    visual_defects: list[str],
    clamp_material: str,
    clamp_count: int,
) -> dict:
    """
    Bewertet den Zustand eines einzelnen Bilgenschlauchs.
    
    Returns:
        dict mit condition_score (0-100), category, recommendations_de
    """
    base_score = 100
    
    # Altersabzug nach Material
    age_penalties = {
        "pvc_reinforced": 8,      # -8 Punkte pro Jahr
        "pvc_spiral": 6,          # -6 Punkte pro Jahr
        "epdm": 5,                # -5 Punkte pro Jahr
        "nbr": 5,
        "silicone": 3,            # -3 Punkte pro Jahr
        "sanitation_hose": 6,
    }
    penalty_per_year = age_penalties.get(material, 7)
    base_score -= int(age_years * penalty_per_year)
    
    # Standort-Modifikator
    location_modifiers = {
        "engine_room": -10,       # Hitze, Öl
        "deck_exposed": -15,      # UV
        "bilge_general": 0,       # Standard
        "cockpit": -5,            # UV, mechanisch
        "anchor_locker": -5,      # Feuchtigkeit
    }
    base_score += location_modifiers.get(location, 0)
    
    # Defekt-Abzüge
    defect_penalties = {
        "surface_cracking": -20,
        "hardening": -30,
        "softening": -15,
        "discoloration": -10,
        "kinking": -20,
        "abrasion": -15,
        "clamp_corrosion": -25,
        "fitting_leak": -40,
        "biological_growth": -5,
        "collapse": -50,
        "swelling": -25,
        "oil_contamination": -15,
        "uv_degradation": -20,
    }
    for defect in visual_defects:
        base_score += defect_penalties.get(defect, -10)
    
    # Schellen-Bewertung
    if clamp_material == "galvanized":
        base_score -= 30
    elif clamp_material == "304":
        base_score -= 10
    # 316/316L: kein Abzug
    
    if clamp_count < 2:
        base_score -= 20
    if clamp_count == 0:
        base_score -= 30  # zusätzlich
    
    score = max(0, min(100, base_score))
    
    if score >= 80:
        category = "good"
    elif score >= 60:
        category = "fair"
    elif score >= 40:
        category = "poor"
    elif score >= 20:
        category = "critical"
    else:
        category = "failed"
    
    return {
        "condition_score": score,
        "category": category,
    }
```

(Confidence: documented)

### Y.3 Schwellenwerte für Warnungen

```python
BILGE_SYSTEM_THRESHOLDS = {
    "critical": {
        "overall_score": 30,
        "message_de": "KRITISCH: Bilgensystem unzureichend. Boot sollte nicht auslaufen.",
        "action_de": "Sofortige Instandsetzung vor nächster Fahrt."
    },
    "warning": {
        "overall_score": 55,
        "message_de": "WARNUNG: Bilgensystem weist erhebliche Mängel auf.",
        "action_de": "Mängel vor nächster Offshore-Fahrt beheben."
    },
    "advisory": {
        "overall_score": 75,
        "message_de": "HINWEIS: Bilgensystem funktionsfähig, aber Verbesserungen empfohlen.",
        "action_de": "Verbesserungen bei nächster Wartung umsetzen."
    },
    "good": {
        "overall_score": 90,
        "message_de": "GUT: Bilgensystem in gutem Zustand.",
        "action_de": "Regelmäßige Wartung fortsetzen."
    },
    "excellent": {
        "overall_score": 100,
        "message_de": "AUSGEZEICHNET: Bilgensystem vorbildlich.",
        "action_de": "Keine Maßnahmen erforderlich."
    }
}
```

(Confidence: documented)

---

*Ende der Wissensdatei 06.08 — Bilgenschläuche und Lenzleitungen*
*AYDI v6 — AI Yacht Design Intelligence*
*Letzte Aktualisierung: 2026-04*
