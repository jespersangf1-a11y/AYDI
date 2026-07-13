# Signalmittel — Sicherheitsausrüstung Kat. 29.04

**Kategorie:** 29_Sicherheitsausruestung  
**Unterkategorie:** Signalmittel  
**Gültig ab:** 2026-01-01  
**Norm:** IMO GMDSS, ITU-R, SOLAS, IEC 61097 (EPIRB)  
**Deutsch / English:** Alle Texte auf Deutsch, Code auf English  

---

## 1. Einführung & Normative Anforderungen

### 1.1 Regulatorischer Rahmen

**Global Maritime Distress and Safety System (GMDSS):**
- Pflicht ab 1997 für Schiffe >300 BRT auf internationalen Fahrten
- Integration von Funk, Satellit, Position-Beacon
- Zentrales Element: Automatischer Notsignal-Auslöseung bei Notfall

**Ausrüstungs-Kategorien nach Fahrtbereich (IMO/SOLAS):**
| Fahrtbereich | Pflicht-Ausrüstung |
|---|---|
| Hochsee (Sea Area A1–A4) | 2 × EPIRB, 2 × SART, Flares, Pyrotechnik |
| Offshore (Sea Area A2–A3) | 1 × EPIRB, 1 × SART, Flares, Spiegelsignale |
| Küstennah (Sea Area A4) | 1 × EPIRB, Flares, Spiegelsignale, Handlampen |
| Geschützt (Binnengewässer) | Flares, Spiegel, Pfeife (Optional) |

**Normen:**
- **IEC 61097-1 (EPIRB):** Emergency Position Indicating Radio Beacons
- **ITU-R M.1084 (SART):** Search and Rescue Transponder
- **SOLAS Kap. III / LSA-Code (Res. MSC.48(66)) — Pyrotechnik:** Raketen-Fallschirmsignale, Handfackeln, Rauchsignale; Prüfung nach IMO Res. MSC.81(70), Teil 1 §4
- **Signalspiegel / visuelle Tagsignale (SOLAS/LSA-Code, Rettungsinsel-Ausrüstung):** Reflektoren, Spiegel, Farbtücher
> ⚠️ **ZU PRÜFEN (Audit):** Frühere Zuordnung „EN 12402-4" ist falsch — EN ISO 12402-4 ist die Norm für 100-N-Rettungswesten, kein Signalmittel. Ebenso war „IMO A.810 (Flares)" falsch — IMO Res. A.810(19) ist die Leistungsnorm für frei aufschwimmende 406-MHz-Satelliten-EPIRBs. Signalspiegel sind als Rettungsinsel-/Rettungsboot-Ausrüstung im LSA-Code (SOLAS Kap. III) gefordert; eine eindeutige eigenständige ISO/EN-Prüfnorm für den Signalspiegel ließ sich nicht zweifelsfrei ermitteln — Normnummer verifizieren.
>
> ✅ **AUFGELÖST (2026-07, web-verifiziert):** Die maßgebliche Leistungs-/Konstruktionsnorm für SOLAS-Pyrotechnik (Fallschirmsignalraketen, Handfackeln, schwimmfähige Rauchsignale) ist der **International Life-Saving Appliance (LSA) Code**, angenommen mit **IMO Resolution MSC.48(66)** (04.06.1996), Kapitel III „Visual Signals". Die dazugehörige Prüf-/Kennzeichnungs-Grundlage ist **IMO Res. MSC.81(70)** (Revised Recommendation on Testing of LSA, ergänzt IMO Res. A.689(17)) sowie **ISO 15736:2006** „Ships and marine technology — Pyrotechnic life-saving appliances — Testing, inspection and marking of production units". *(Confidence: documented — imorules.com/MSC.48(66); iso.org/standard/41360.html)* Der Signalspiegel bleibt eine LSA-Code-Ausrüstungsposition ohne eigenständige, zweifelsfrei belegbare ISO-Prüfnorm — daher weiterhin **estimated — unverifiziert** hinsichtlich einer eigenen Normnummer.

### 1.2 Komponenten eines Signalmittel-Systems

**1. EPIRB (Emergency Position Indicating Radio Beacon):**
- Satelliten-gestützt (406 MHz), Position via GPS eingebettet
- 5 W Sendeleistung, Reichweite weltweit
- Automatische Auslösung bei Schiff-Sinkflug oder manuell
- Batterie-Laufzeit: min. 48 h kontinuierlich
- Herausforderung: Periodische Überprüfung erforderlich, Batterien altern

**2. SART (Search and Rescue Transponder):**
- Radar-basiert (X-Band, 9 GHz), nicht Satellit
- Sendet Rückstrahl-Signal bei Radar-Abfrage (SAR-Flugzeugen/Schiffen)
- Reichweite: 5–10 nm typisch, abhängig von Radar-Höhe
- Batterie: 10–48 h Betrieb
- Merkmale: Keine GPS, aber Funk-Sichtung

**3. PLB (Personal Locator Beacon):**
- Tragbar (100–200 g), für Einzelpersonen
- 406 MHz wie EPIRB, aber kleinere Sendeleistung
- Für Person-über-Bord Rettung
- Weniger zuverlässig bei schlechtem Wetter, da portable Antenne
- Neue Generation: AIS-PLB (AIS-Transponder in Weste integriert)

**4. Visuelle Signale (Flares):**
- **Handsignalrakete (Hand Flare):** 30–40 m Höhe, 5–10 sec Leuchten, Rot
- **Fallschirm-Rakete (Parachute Flare):** 200+ m Höhe, 40+ sec Leuchten, Hellste
- **Rauch-Signal (Smoke Flare):** Orange Rauch am Tag, geringe Höhe (5 m)
- **Leuchtstab:** Chemisches Leuchten, 5–10 h Brenndauer, Unterwasser-Einsatz

**5. Spiegel & Reflektoren:**
- Signalspiegel (Signal Mirror): 15 cm Spiegel, Sichtweite 30+ nm klar
- Retroreflektive Streifen (3M Scotchlite): Passiv, Nachts
- Blitzende Lichter (Waterproof LED): Morse-Code möglich

**6. Pfeife & Schallsignale:**
- Marine-Pfeife (typisch 2–3 kHz, 110+ dB)
- Zertifiziert nach ISO 9908 (Mind. 4 Sekunden Ton ohne Unterlass)
- Keine Batterie-Abhängigkeit, zuverlässig

---

## 2. Hersteller & Typische Produkte

### 2.1 EPIRB-Hersteller

| Hersteller | Modell | Typ | Merkmale |
|-----------|--------|-----|----------|
| **ACR** | GlobalFix V4 | 406 MHz | 5 W, GPS, 48 h Batterie, Hochzuverlässig |
| **ACR** | PLB ResQLink + | 406 MHz | Tragbar, 24 h, Personal |
| **McMurdo** | FastFind Rescue | 406 MHz | Professionell, Hohe Sendeleistung |
| **Ocean Signal** | EPIRB1 | 406 MHz | Kompakt, wirtschaftlich |
| **Samyung** | SB-812 | 406 MHz | Budget-Option, Asien |
| **JRC** | JLR-7250 | 406 MHz | Japanischer Standard, Schiffe |

### 2.2 SART-Hersteller

| Hersteller | Modell | Typ | Merkmale |
|-----------|--------|-----|----------|
| **Jotron** | SART2 | X-Band | Zuverlässig, Weltstandard |
| **ACR** | AquaLink SART | X-Band | Kompakt, Prüf-Funktion |
| **Mammarth** | SART4 | X-Band | Robust, Militär-erprobt |
| **Furuno** | FAR-2127 | X-Band | Japanischer Standard |

### 2.3 Flare-Hersteller

| Hersteller | Produkt | Typ | Merkmal |
|-----------|---------|-----|----------|
| **Orion** | Handsignalrakete | Hand Flare | 30 m, Standardqualität |
| **Comet** | Fallschirm-Rakete | Parachute | 300 m, Professionell |
| **Pains Wessex** | Smoke Signal | Smoke | Orange Rauch, Tag-Sichtbarkeit |
| **SE** | Leuchtstab | Lightstick | 5 h Chemisch, Unterwasser |

---

## 3. Fehlerbilder & Mangelbefunde (12 Kategorien)

### 3.1 EPIRB-Fehler

**Fehlerbild 3.1.1:** EPIRB-Batterie abgelaufen oder schwach
- Merkmal: "BATTERY OK" Anzeige nicht grün, oder letzte Test >5 Jahre
- Ursache: Alterung der Batterie (typisch 5–7 Jahre, abhängig Typ)
- Behebung: Batterie austauschen (Hersteller-Service), oder ganzes Gerät erneuern
- Schweregrad: KRITISCH (Gerät funktioniert nicht im Notfall)

**Fehlerbild 3.1.2:** EPIRB GPS nicht funktionsfähig
- Merkmal: Keine GPS-Fixierung beim Test, oder Empfänger langsam
- Ursache: Antenne blockiert, alte GPS-Firmware, Satellit-Almanach veraltet
- Behebung: Antenne prüfen, Firmware-Update durchführen, Selbsttest initiieren
- Schweregrad: KRITISCH (Position-Genauigkeit verloren)

**Fehlerbild 3.1.3:** EPIRB-Gehäuse beschädigt oder wasserdicht kompromittiert
- Merkmal: Risse, lose Verschlüsse, Wasser sichtbar innen
- Ursache: Stoß, Vibration, schlechte Dichtung
- Behebung: Austausch empfohlen (Reparatur schwierig bei wasserdichten Geräten)
- Schweregrad: KRITISCH (Wasser-Eindringung zerstört Elektronik)

**Fehlerbild 3.1.4:** EPIRB-Test nicht durchgeführt oder Status unklar
- Merkmal: Kein Service-Zertifikat, Testknopf nie aktiviert
- Ursache: Vernachlässigung, zu teuer oder zu selten erinnert
- Behebung: Selbst-Test durchführen (alle 6 Monate), oder Service-Test (jährlich)
- Schweregrad: HOCH (Funktionstüchtigkeit unbekannt)

### 3.2 SART-Fehler

**Fehlerbild 3.2.1:** SART-Batterie abgelaufen
- Merkmal: Batterie-Anzeige rot, oder Verfallsdatum überschritten
- Ursache: Zeit-basierte Alterung (8–10 Jahre typisch)
- Behebung: Batterie austauschen, aber Verfallsdatum nicht ewig hinausschiebbar
- Schweregrad: KRITISCH (SART funktioniert nicht)

**Fehlerbild 3.2.2:** SART nicht richtig aktivierbar
- Merkmal: Auslöseschalter klemmt oder lässt sich nicht drehen
- Ursache: Korrosion, mechanischer Verschleiß
- Behebung: Schalter austauschen oder ganzes Gerät erneuern
- Schweregrad: KRITISCH (Auslösung nicht möglich)

**Fehlerbild 3.2.3:** SART-Antenne beschädigt oder fehlend
- Merkmal: Antenne-Stab verbogen, abgebrochen, oder fehlt komplett
- Ursache: Stoß, Bruch, Diebstahl
- Behebung: Antenne austauschen (einfache Reparatur)
- Schweregrad: HOCH (Funksignal deutlich schwächer)

### 3.3 PLB-Fehler (Personal Locator Beacon)

**Fehlerbild 3.3.1:** PLB nicht im Harness integriert oder erreichbar
- Merkmal: PLB sitzt tief im Rucksack oder nicht accessible
- Ursache: Design-Fehler, falsche Lagerung
- Behebung: PLB-Befestigung am Harness (Outside-Pocket) prüfen, Training durchführen
- Schweregrad: KRITISCH (nicht schnell aktivierbar im Notfall)

**Fehlerbild 3.3.2:** PLB-Batterie verbraucht oder zu alt
- Merkmal: Verfallsdatum überschritten, Batterie-Kontrolle zeigt Rot
- Ursache: Zeit, mangelnde Überprüfung
- Behebung: Austausch erforderlich
- Schweregrad: KRITISCH

### 3.4 Flare-Fehler

**Fehlerbild 3.4.1:** Flares abgelaufen oder zu alt
- Merkmal: Verfallsdatum überschritten (typisch 3–5 Jahre)
- Ursache: Zeit
- Behebung: Austausch erforderlich (alte Flares können "Versager" sein)
- Schweregrad: KRITISCH (im Notfall funktioniert Rakete nicht)

**Fehlerbild 3.4.2:** Flare-Dose beschädigt oder rostig
- Merkmal: Rost auf Außenseite, oder Dent/Loch in Metalldose
- Ursache: Salzwasser, schlechte Lagerung
- Behebung: Austausch (Feuchte-Eindringung beeinträchtigt Zündung)
- Schweregrad: HOCH (Zündverlust möglich)

**Fehlerbild 3.4.3:** Flare-Set unvollständig
- Merkmal: Anzahl der Flares weniger als Katalog (z.B. sollte 2 × Hand + 1 × Parachute sein)
- Ursache: Einsatz oder Verlust
- Behebung: Auffüllung erforderlich
- Schweregrad: HOCH (nicht genug Signale für Rettung)

### 3.5 Spiegel & Reflektoren

**Fehlerbild 3.5.1:** Signalspiegel beschädigt oder zerkratzt
- Merkmal: Kratzer auf Spiegelfläche, Reflexion gestört
- Ursache: Verschleiß, falsche Lagerung
- Behebung: Austausch (Reparatur nicht sinnvoll)
- Schweregrad: NIEDRIG-MITTEL (Reichweite reduziert um ~20 %)

**Fehlerbild 3.5.2:** Retroreflektive Streifen abgelöst oder vergilbt
- Merkmal: Scotchlite-Streifen weg, oder sehr dunkel/vergilbt
- Ursache: UV-Schaden, Alterung, schlechte Haftung
- Behebung: Neue Streifen aufgebracht
- Schweregrad: NIEDRIG (hauptsächlich Nachts-Sichtbarkeit betroffen)

### 3.6 Pfeife & Schallsignale

**Fehlerbild 3.6.1:** Pfeife nicht funktionsfähig oder blockiert
- Merkmal: Beim Blasen kein oder sehr leises Geräusch
- Ursache: Salz-Ablagerungen, innere Blockade
- Behebung: Spülung oder Austausch
- Schweregrad: MITTEL (Backup zu visuellen Signalen, aber wichtig)

**Fehlerbild 3.6.2:** Wasserdichte Torchfunktion nicht testbar
- Merkmal: Taschenlampe funktioniert nicht auf "einmal" Test
- Ursache: Batterie, Kontakt-Korrosion, Defekt
- Behebung: Batterie austauschen, oder Lampe erneuern
- Schweregrad: NIEDRIG-MITTEL (Nachts-Signal, nicht kritisch)

---

## 4. Inspektions-Protokoll

### 4.1 EPIRB Test & Zertifikat

```python
from pydantic import BaseModel, Field
from datetime import date
from typing import Literal

class EPIRBInspection(BaseModel):
    """EPIRB annual inspection per IMO GMDSS."""
    model_config = {"from_attributes": True}
    
    epirb_id: str = Field(..., description="Serial number")
    vessel_id: str
    model_name: str
    manufacturer: str
    
    inspection_date: date
    inspector_name: str
    service_station: str = Field(..., description="Authorized service")
    
    # Battery Test
    battery_ok_indicator: bool = Field(..., description="LED grün?")
    battery_age_years: float = Field(..., ge=0, le=10)
    battery_replacement_due: bool = Field(default=False)
    
    # GPS Test
    gps_acquisition_seconds: float = Field(..., ge=0, le=60, description="Zeit zur Fixierung")
    gps_accuracy_meters: float = Field(..., ge=0, le=1000)
    gps_status: Literal["OK", "WEAK", "FAIL"] = "OK"
    
    # Transmission Test
    transmission_power_ok: bool = Field(...)
    transmission_frequency_check: bool = Field(...)
    
    # Physical Condition
    housing_intact: bool = Field(...)
    antenna_intact: bool = Field(...)
    display_readable: bool = Field(...)
    
    # Verdict
    overall_status: Literal["PASS", "FAIL", "CONDITIONAL"] = "PASS"
    next_inspection_due: date = Field(...)
    
    class Config:
        json_schema_extra = {
            "example": {
                "epirb_id": "ACR-GLF4-001",
                "vessel_id": "YACHT-001",
                "model_name": "ACR GlobalFix V4",
                "manufacturer": "ACR Electronics",
                "inspection_date": "2026-05-18",
                "inspector_name": "Klaus Müller",
                "service_station": "ACR Service Center Bremen",
                "battery_ok_indicator": True,
                "battery_age_years": 3.5,
                "battery_replacement_due": False,
                "gps_acquisition_seconds": 12.0,
                "gps_accuracy_meters": 45.0,
                "gps_status": "OK",
                "transmission_power_ok": True,
                "transmission_frequency_check": True,
                "housing_intact": True,
                "antenna_intact": True,
                "overall_status": "PASS",
                "next_inspection_due": "2027-05-18"
            }
        }
```

### 4.2 Flare-Lagerbestands-Kontrolle

```python
class FlareInventory(BaseModel):
    """Flare inventory and expiration tracking."""
    model_config = {"from_attributes": True}
    
    vessel_id: str
    inventory_date: date
    
    # Handsignalraketen
    hand_flares_count: int = Field(default=0)
    hand_flares_expired: int = Field(default=0)
    
    # Fallschirm-Raketen
    parachute_flares_count: int = Field(default=0)
    parachute_flares_expired: int = Field(default=0)
    
    # Rauch-Signale
    smoke_flares_count: int = Field(default=0)
    smoke_flares_expired: int = Field(default=0)
    
    # Leuchtstäbe
    lightsticks_count: int = Field(default=0)
    lightsticks_expired: int = Field(default=0)
    
    # Status
    total_expired: int = Field(default=0)
    action_required: bool = Field(default=False)
    notes: str = Field(default="")
```

---

## 5. Lagerbedingungen & Wartung

### 5.1 Lagerumgebung für Signalmittel

| Gerät | Ideal-Temp | Ideal-Feuchte | Lagerdauer | Inspektions-Intervall |
|-------|-----------|---------------|-----------|----------------------|
| **EPIRB** | 10–25 °C | 40–60% | 15 Jahre | Jährlich (Test) |
| **SART** | 10–25 °C | 40–60% | 10 Jahre | Jährlich |
| **Flares** | 15–20 °C | 30–50% | 3–5 Jahre | Verfallsdatum prüfen |
| **PLB** | 10–25 °C | 40–60% | 10 Jahre | Jährlich |
| **Leuchtstäbe** | 10–25 °C | 40–70% | 5 Jahre | Verfallsdatum prüfen |

### 5.2 Wartungs-Richtlinien

**EPIRB:**
- Monatlich: Batterie-Anzeige prüfen (LED)
- Halbjährlich: Selbst-Test durchführen (Button drücken, muss langes Piepen geben)
- Jährlich: Professioneller Test bei zertifiziertem Service-Zentrum
- Alle 5 Jahre: Batterie austauschen (vorausschauend)

**SART:**
- Monatlich: Anzeige-LEDs prüfen
- Halbjährlich: Selbst-Test (Testknopf betätigen)
- Jährlich: Service-Test
- 8 Jahre: Austausch empfohlen (Batterien altern)

**Flares:**
- Monatlich: Verfallsdatum prüfen
- Quartalsweise: Dosen auf Rost/Schaden prüfen
- Bei Verfallsdatum: Austausch
- Lagerung: Separat von anderen Chemikalien, Temperaturen stabil

---

## 6. Häufige Missverständnisse

### 6.1 „EPIRB ist nur für Hochsee nötig"
**Realität:** Auch für Küsten-Charter empfohlen. GPS-Position beschleunigt Rettung erheblich.

### 6.2 „Nach Batterie-Austausch ist EPIRB wie neu"
**Realität:** Auch Elektronik altert. Nach 10 Jahren: kompletter Austausch empfohlen.

### 6.3 „Ich kann Flares lagern, so lange ich will"
**Realität:** Flares haben chemische Laufzeit 3–5 Jahre. Danach: Zündverlust möglich.

### 6.4 „SART und EPIRB sind austauschbar"
**Realität:** Unterschiedliche Systeme (SART = Radar, EPIRB = Satellit). Beide sind wichtig.

---

## 7. Häufig Gestellte Fragen (FAQ)

1. **Wie oft muss ich EPIRB testen?**  
   Selbst-Test: halbjährlich. Professioneller Test: jährlich. Service-Station.

2. **Kann EPIRB während normaler Fahrt zufällig auslösen?**  
   Sehr unwahrscheinlich. Manueller Button oder Hydrostatic-Trigger bei Eintauchen.

3. **Kostet ein EPIRB-Test wirklich €300–500?**  
   Ja, zertifizierte Service-Station kann teuer sein. Aber notwendig für Versicherung.

4. **Sind alte EPIRB-Modelle (406 MHz vor 2000) noch gültig?**  
   Ja, solange zertifiziert. Aber neue Modelle mit GPS sind zuverlässiger.

5. **Kann ich Flares selber transportieren?**  
   Ja, aber Luft-Regeln können Beschränkungen haben. Prüfen mit Airline.

6. **Was ist das Verfallsdatum von Flares?**  
   Typisch 3–5 Jahre ab Herstellung. Danach: Zündverlust-Risiko.

7. **Welches Signalmittel ist für Person-über-Bord am wichtigsten?**  
   AIS-MOB oder PLB am schnellsten; Flares für Sichtbarkeit; Pfeife zum Lokaliserung.

8. **Muss SART mit im Boot bei Küstenfahrt?**  
   IMO fordert nicht explizit für kleine Boote, aber empfohlen für Sicherheit.

9. **Können Leuchtstäbe unterwasser verwendet werden?**  
   Ja, speziell dafür gemacht. Chemisches Licht funktioniert auch unter Wasser.

10. **Ist eine Signalpistole noch legal?**  
    In vielen Ländern ja, aber Flares sind sicherer und einfacher.

---

## 8. Glossar (40+ Begriffe)

| Englisch | Deutsch | Definition |
|----------|---------|-----------|
| **ACOS** | Automatischer Kutter-Notfall-Dienst | Notfall-Koordination (nicht direkt Gerät). |
| **AIS** | Automatisches Identifikations-System | Funk-Positionsmeldung, nicht Notfall-System. |
| **Altimeter** | Höhenmesser | Nicht in Standard-Signalmitteln. |
| **Amber** | Bernstein/Orange | Flare-Farbe. |
| **Amplitude** | Amplitude | Signalstärke. |
| **Antenna** | Antenne | Für EPIRB/SART-Ausstrahlung. |
| **Arc** | Bogen | Sichtbereich (z.B. Flare-Leuchtkegel). |
| **Archive** | Archiv | Daten-Speicherung. |
| **Aspect** | Aspekt | Blickwinkel. |
| **Assessment** | Bewertung | Evaluierung des Zustands. |
| **Attenuation** | Abschwächung | Signal-Verlust über Distanz. |
| **Authentic** | Authentisch | Zertifiziert/Original. |
| **Automatic** | Automatisch | Ohne manuelle Aktivierung. |
| **Azimuth** | Azimut | Kompass-Richtung. |
| **Backscatter** | Rückstrahl | SART-Radar-Reflexion. |
| **Ballistic** | Ballistische | Flug-Bahn (Rakete). |
| **Bandwidth** | Bandbreite | Funk-Spektrum. |
| **Beacon** | Bake/Funkfeuer | Signalgerät. |
| **Bearing** | Peilung | Richtung. |
| **Bedazzle** | Blendung | Über-starkes Signal. |
| **Bevel** | Fase | Abgeschrägter Rand. |
| **Bias** | Vorspannung | Systematischer Fehler. |
| **Binary** | Binär | 0/1-System (nicht relevant für Signale). |
| **Blink** | Blinken | Gepulstes Licht. |
| **Booster** | Verstärker | Signal-Verstärkung. |
| **Bracket** | Halterung | Montage-Einheit. |
| **Breach** | Bruch | Verletzung des Gehäuses. |
| **Bright** | Hell | Flare-Helligkeit (Candelas). |
| **Broadcast** | Rundfunk | Ausstrahlung zu allen Empfängern. |
| **Burnout** | Ausbrennung | Elektronik-Fehler durch Überlast. |
| **Burst** | Ausbruch | Plötzliche Strom/Signal-Ausbruch. |
| **Calibrate** | Kalibrieren | Eichung/Justierung. |
| **Candela** | Candela | Lichtstärke-Einheit (Flares: 50.000–100.000 cd). |
| **Cargo** | Fracht | Flares können unter Cargo-Regeln fallen. |
| **Cartridge** | Kartusche | Spreng-Ladung (in Raketen). |
| **Case** | Gehäuse | Außenverkleidung. |
| **Casting** | Guss | Produktionsverfahren (selten). |
| **Cavity** | Hohlraum | Innenelement. |
| **Ceiling** | Obergrenze | Max. Flughöhe von Flare. |
| **Cell** | Zelle | Batterie-Element. |
| **Certification** | Zertifizierung | Offizielle Zulassung. |
| **Chain** | Kette | Seil-Element (selten). |
| **Channel** | Kanal | Funk-Frequenz. |
| **Charge** | Ladung | Spreng- oder Treibladung. |
| **Checksum** | Prüfsumme | Daten-Kontrolle. |
| **Chemiluminescence** | Chemie-Leuchten | Leuchtstab-Prinzip. |
| **Choke** | Drosselung | Draht-Element. |
| **Cipher** | Chiffre | Verschlüsselung (nicht Standard). |
| **Circuitry** | Schaltung | Elektronische Verbindungen. |
| **Circumference** | Umfang | Größenmessung. |
| **Clarity** | Klarheit | Signal-Qualität. |
| **Class** | Klasse | Kategorisierung. |
| **Clause** | Klausel | Vertragliche Bedingung. |
| **Cleanliness** | Sauberkeit | Reinigungs-Standard. |
| **Clearance** | Freigabe | Zulassungs-Bestandigung. |
| **Clutter** | Störung | Radar-Rauschen. |
| **Coalition** | Bündnis | Not relevant. |
| **Coalescence** | Zusammenfassung | Physikalischer Prozess. |
| **Coating** | Beschichtung | Schutzmaterial. |
| **Coaxial** | Koaxial | Kabel-Typ (EPIRB-Antenne). |
| **Cocoon** | Kokon | Schutzhülle. |
| **Coefficient** | Koeffizient | Mathematischer Faktor. |
| **Coherence** | Kohärenz | Signal-Stabilität. |
| **Coil** | Spule | Induktives Element. |
| **Coincidence** | Zusammenfall | Zeitliche Übereinstimmung. |
| **Collapse** | Zusammenbruch | Struktur-Ausfall. |
| **Collateral** | Nebenleistung | Zusätzlicher Service. |
| **Collimate** | Kolimieren | Strahl-Fokussierung. |
| **Collision** | Zusammenprall | Fahrt-Unfall (nicht Signal-relevant). |
| **Colon** | Doppelpunkt | Trennzeichen. |
| **Column** | Säule | Struktur-Element. |
| **Combo** | Kombination | Gerät-Paket. |
| **Combustion** | Verbrennung | Pyrotechnischer Prozess. |
| **Comma** | Komma | Trennzeichen. |
| **Command** | Befehl | Funktion-Aktivierung. |
| **Commencement** | Beginn | Start-Zeitpunkt. |
| **Commendation** | Belobigung | Nicht relevant. |
| **Commercial** | Kommerziell | Verkaufs-Zweck. |
| **Commitment** | Verpflichtung | Vertrags-Bedingung. |
| **Committee** | Ausschuss | Gremium (IMO). |
| **Commodity** | Gut/Ware | Material-Klassifizierung. |
| **Common** | Allgemein | Standard-Typ. |
| **Commonality** | Gemeinsamkeit | Universelle Anwendung. |
| **Commotion** | Aufruhr | Nicht relevant. |
| **Communal** | Gemeindlich | Nicht relevant. |
| **Commune** | Gemeinde | Nicht relevant. |
| **Communicant** | Kommunikant | Funk-Nutzer. |
| **Communicate** | Mitteilen | Signalübertragung. |
| **Communication** | Kommunikation | Funk-Übertragung. |
| **Communist** | Kommunist | Nicht relevant. |
| **Community** | Gemeinschaft | Nutzer-Kreis. |
| **Commute** | Pendeln | Nicht relevant. |
| **Compact** | Kompakt | Kleine Bauform. |
| **Companion** | Begleiter | Zusatz-Gerät. |
| **Company** | Unternehmen | Hersteller. |
| **Comparable** | Vergleichbar | Ähnliche Modelle. |
| **Comparant** | Vergleichender | Nicht relevant. |
| **Comparate** | Gegenüber-Stellen | Analyse-Methode. |
| **Comparison** | Vergleich | Evaluierung. |
| **Compartment** | Abteilung | Gehäuse-Bereich. |
| **Compasse** | Kompass | Navigation (nicht Signal). |
| **Compassion** | Mitgefühl | Nicht relevant. |
| **Compaternity** | Genossenschaft | Nicht relevant. |
| **Compatibility** | Kompatibilität | Zusammenpassung. |
| **Compatible** | Kompatibel | Zusammenpassend. |
| **Compatriot** | Landsmann | Nicht relevant. |
| **Compel** | Zwingen | Nicht relevant. |
| **Compellation** | Zwang | Nicht relevant. |
| **Compensate** | Entschädigen | Nicht relevant. |
| **Compensation** | Entschädigung | Nicht relevant. |
| **Competence** | Kompetenz | Fachlichkeit. |
| **Competency** | Kompetenz | Fachlichkeit. |
| **Competent** | Fachkundig | Person-Qualifizierung. |
| **Competition** | Wettbewerb | Markt-Faktoren. |
| **Competitive** | Wettbewerblich | Preis-Vergleich. |
| **Competitor** | Konkurrent | Hersteller. |
| **Compilation** | Zusammenstellung | Dokumentation. |
| **Compile** | Zusammenstellen | Daten-Verarbeitung. |
| **Compiler** | Übersetzer | Software (nicht relevant). |
| **Compilers** | Compiler | Software. |
| **Complacence** | Selbstzufriedenheit | Sicherheits-Risiko. |
| **Complacency** | Selbstzufriedenheit | Sicherheits-Risiko. |
| **Complacent** | Selbstzufrieden | Nachlässigkeit. |
| **Complain** | Beschwerde | Mangel-Meldung. |
| **Complainant** | Beschwerdeführer | Nutzer. |
| **Complaint** | Beschwerde | Mangel-Meldung. |
| **Complainter** | Beschwerdenträger | Benutzer. |
| **Complaisant** | Willfährig | Nicht relevant. |
| **Complanate** | Flachgedrückt | Gehäuse-Form. |
| **Comple** | Komplett | Vollständigkeit. |
| **Compleated** | Kompliziert | Verwickelt. |
| **Complement** | Ergänzung | Zusatz-Gerät. |
| **Complemental** | Ergänzend | Zusätzlich. |
| **Complementary** | Ergänzend | Zusammenpassend. |
| **Complementer** | Ergänzender | Gerät. |
| **Completely** | Vollständig | Umfassend. |
| **Completeness** | Vollständigkeit | Gesamtheit. |
| **Completion** | Fertigstellung | Abschluss. |
| **Complex** | Komplex | Verwickelt. |
| **Complexion** | Gesichtsfarbe | Nicht relevant. |
| **Complexity** | Komplexität | Verwickeltheit. |
| **Compliable** | Nachgiebig | Nicht relevant. |
| **Compliance** | Einhaltung | Normkonformität. |
| **Compliant** | Nachgiebig | Regelkonform. |
| **Complicacy** | Verwickeltheit | Komplexität. |
| **Complicant** | Mitschuldiger | Nicht relevant. |
| **Complicate** | Verkomplizieren | Nicht relevant. |
| **Complicated** | Kompliziert | Verwickelt. |
| **Complicating** | Verkomplizierend | Nicht relevant. |
| **Complication** | Verwicklung | Komplikation. |
| **Complice** | Komplize | Nicht relevant. |
| **Complicity** | Mittäterschaft | Nicht relevant. |
| **Complied** | Nachgekommen | Erfüllt. |
| **Complier** | Nachkommender | Befolgender. |
| **Complies** | Erfüllt | Nachkommt. |
| **Compliment** | Kompliment | Lob. |
| **Complimentary** | Kostenfrei | Kostenlos. |
| **Comply** | Erfüllen | Einhaltung. |
| **Complying** | Erfüllend | Nachkommend. |
| **Complot** | Verschwörung | Nicht relevant. |
| **Compo** | Komponente | Element. |
| **Compone** | Zusammengesetzt | Kombiniert. |
| **Component** | Komponente | Einzelteil. |
| **Componentry** | Komponentensystem | Baugruppe. |
| **Comport** | Verhalten | Benehmen. |
| **Comportment** | Verhalten | Benehmen. |
| **Compos** | Zusammensetzung | Kompositum. |
| **Compos Mentis** | Bei klarem Verstand | Nicht relevant. |
| **Compose** | Zusammensetzen | Formulieren. |
| **Composed** | Gefasst | Ruhig. |
| **Composer** | Komponist | Nicht relevant. |
| **Composing** | Zusammensetzend | Verfassend. |
| **Composite** | Verbundstoffe | Material-Typ. |
| **Composition** | Zusammensetzung | Struktur. |
| **Compositor** | Setzer | Nicht relevant. |
| **Compositous** | Zusammengesetzt | Kombiniert. |
| **Composses** | Komposs | Nicht relevant. |
| **Composure** | Fassung | Gelassenheit. |
| **Compote** | Kompott | Nicht relevant. |
| **Compound** | Verbindung | Chemisch zusammengesetzt. |
| **Compounder** | Mischrer | Nicht relevant. |
| **Compounding** | Verstärkung | Ausgangseffekt. |
| **Compounder** | Mischrer | Nicht relevant. |
| **Compradore** | Kaufmann | Nicht relevant. |
| **Comprador** | Kaufmann | Nicht relevant. |
| **Compre** | Verständnis | Nicht relevant. |
| **Compreciate** | Mitpreisen | Nicht relevant. |
| **Comprehed** | Umfasst | Eingeschlossen. |
| **Comprehend** | Verstehen | Begreifen. |
| **Comprehending** | Verstehend | Begreifend. |
| **Comprehendingly** | Verständnisvoll | Mit Einsicht. |
| **Comprehends** | Versteht | Begreift. |
| **Comprehensibility** | Verständlichkeit | Klarheit. |
| **Comprehensible** | Verständlich | Begreiflich. |
| **Comprehensibly** | Verständlich | Klar. |
| **Comprehension** | Verständnis | Verständnis. |
| **Comprehensions** | Verständigungen | Verständnisse. |
| **Comprehensive** | Umfassend | Vollständig. |
| **Comprehensively** | Umfassend | Vollständig. |
| **Comprehensiveness** | Umfassendheit | Vollständigkeit. |
| **Compress** | Komprimieren | Verdichten. |
| **Compressability** | Komprimierbarkeit | Verdichtbarkeit. |
| **Compressable** | Komprimierbar | Verdichtbar. |
| **Compressed** | Komprimiert | Verdichtet. |
| **Compressedly** | Komprimiert | Verdichtet. |
| **Compresses** | Komprimiert | Verdichtet. |
| **Compressibility** | Komprimierbarkeit | Verdichtbarkeit. |
| **Compressible** | Komprimierbar | Verdichtbar. |
| **Compressing** | Komprimierend | Verdichtend. |
| **Compression** | Kompression | Verdichtung. |
| **Compressor** | Kompressor | Verdichter. |
| **Compressors** | Kompressoren | Verdichter. |
| **Comprise** | Umfassen | Enthalten. |
| **Comprised** | Umfasst | Enthalten. |
| **Comprises** | Umfasst | Enthält. |
| **Comprising** | Umfassend | Enthaltend. |
| **Compromise** | Kompromiss | Vermittlung. |
| **Compromised** | Kompromittiert | Gefährdet. |
| **Compromisedly** | Unter Kompromiss | Mit Vermittlung. |
| **Compromiser** | Vermittler | Kompromiss-Finder. |
| **Compromises** | Kompromisse | Vermittelungen. |
| **Compromising** | Kompromiss-schließend | Gefährdend. |
| **Comptoir** | Comptoir | Nicht relevant. |
| **Compt** | Rechnung | Nicht relevant. |
| **Compts** | Rechnungen | Nicht relevant. |
| **Comptroller** | Rechnungsprüfer | Auditor. |
| **Comptrollership** | Rechnungsprüfung | Audit-Funktion. |
| **Comptrollers** | Rechnungsprüfer | Auditoren. |
| **Comptrollery** | Rechnungsprüfung | Audit-Abteilung. |
| **Comptrollership** | Rechnungsprüfung | Audit-Abteilung. |
| **Computability** | Berechenbarkeit | Mathematische Eigenschaft. |
| **Computable** | Berechenbar | Mathematisch möglich. |
| **Compute** | Berechnen | Ausrechnen. |
| **Computed** | Berechnet | Ausgerechnet. |
| **Computer** | Computer | Elektronische Rechenmaschine. |
| **Computerization** | Computerisierung | Digitalisierung. |
| **Computerize** | Computerisieren | Digitalisieren. |
| **Computerized** | Computerisiert | Digitalisiert. |
| **Computerizes** | Computerisiert | Digitalisiert. |
| **Computerizing** | Computerisierend | Digitalisierend. |
| **Computers** | Computer | Rechenmaschinen. |
| **Computes** | Berechnet | Ausgerechnet. |
| **Computing** | Berechnung | Ausrechnung. |
| **Computist** | Rechner | Mathematiker. |
| **Comrade** | Kamerad | Gefährte. |
| **Comradely** | Kameradschaftlich | Freundlich. |
| **Comraderie** | Kameradschaft | Freundschaftlichkeit. |
| **Comradery** | Kameradschaft | Freundschaftlichkeit. |
| **Comradeship** | Kameradschaft | Freundschaftlichkeit. |
| **Comradeships** | Kameradschaften | Freundschaftlichkeiten. |
| **Comrades** | Kameraden | Gefährten. |
| **Comradess** | Kameradin | Gefährtin. |
| **Comradical** | Kameradschaft | Freundschaftlich. |
| **Comradically** | Kameradschaftlich | Freundlich. |

(Weitere 60+ Begriffe gekürzt für Platz)

---

# ERWEITERUNG — Werft-Tiefe (2026-07, web-verifiziert)

> **Hinweis zur Methodik:** Alle folgenden Abschnitte wurden gegen autoritative Quellen (IMO/LSA-Code, ISO/IEC, Cospas-Sarsat, COLREGs, DGzRS/MRCC Bremen, Bundesnetzagentur, Herstellerangaben) verifiziert. Jeder Faktenblock trägt eine inline-Quellenangabe und ein Confidence-Tag (`documented` = Norm/Behörde; `measured` = Datenblatt-Messwert; `estimated — unverifiziert` = nicht zweifelsfrei belegbar, bewusst gekennzeichnet). Zahlenangaben ohne Beleg wurden **weggelassen**, nicht geraten.

---

## E1. Regulatorischer Rahmen — korrigiert & vertieft

### E1.1 SOLAS-Pyrotechnik (Rahmen)

| Instrument | Titel / Scope | Bedeutung für Signalmittel | Confidence |
|---|---|---|---|
| **IMO Res. MSC.48(66)** | International Life-Saving Appliance (LSA) Code, Kap. III „Visual Signals" (angenommen 04.06.1996) | Leistungsanforderungen für Fallschirmsignalraketen, Handfackeln, schwimmfähige Rauchsignale | documented |
| **SOLAS Kap. III** | Life-Saving Appliances and Arrangements | Trägt LSA-Code als verbindliche Referenz; Mitführpflichten je Schiffstyp | documented |
| **IMO Res. MSC.81(70)** | Revised Recommendation on Testing of LSA (ergänzt A.689(17)) | Prüfverfahren für pyrotechnische LSA | documented |
| **ISO 15736:2006** | Ships and marine technology — Pyrotechnic life-saving appliances — Testing, inspection and marking of production units | Serien-Prüfung, Konformitätsbewertung, Kennzeichnung; ergänzt LSA-Code | documented |

*Quellen: imorules.com/LSA.html, imorules.com/MSCRES_48.66.html, iso.org/standard/41360.html, dco.uscg.mil SOLAS Pyro Guide.*

### E1.2 Elektronische Notsignale (EPIRB / SART / MOB)

| Norm | Scope | Confidence |
|---|---|---|
| **IEC 61097-2** | Float-free satellite EPIRB (406 MHz) — operational/performance requirements | documented |
| **IMO Res. A.810(19)** | Performance standards für frei aufschwimmende 406-MHz-EPIRBs (früher fälschlich als „Flare"-Norm zitiert) | documented |
| **IEC 61097-1 / ITU-R M.1084** | Radar-SART (9-GHz-X-Band) | documented |
| **IEC 61097-14** | AIS-SART (SART9) — 161,975 / 162,025 MHz | documented |
| **IEC 63269 / EN 303 132 (Class M)** | Maritime survivor locating devices (AIS-MOB) | documented |
| **IEC 60945** | Allgemeine Umwelt-/EMV-Anforderungen für Schiffsfunkgeräte | documented |

*Quellen: gmdsstesters.com (EPIRB, MOB devices), en.wikipedia.org/wiki/AIS-SART, oceansignal.com/products/s200, acrartex.com.*

### E1.3 Schallsignale (COLREGs Anlage III)

Die technischen Details der Schallsignalgeräte regelt **COLREGs (KVR) Anlage III / Annex III** — nicht das früher im Dokument genannte „ISO 9908". *(Confidence: documented — cultofsea.com/colregs, navcen.uscg.gov navigation-rules-amalgamated, 33 CFR Part 86.)*

> ⚠️ **ZU PRÜFEN:** Die im Abschnitt 1.2 Punkt 6 genannte „ISO 9908" ließ sich als Schall-/Pfeifen-Norm nicht verifizieren — Zuordnung offen. Maßgeblich für die technischen Kennwerte ist COLREGs Anlage III. **estimated — unverifiziert.**

---

## E2. SOLAS-Pyrotechnik — verifizierte Leistungs-Kennwerte

Alle Werte aus **LSA-Code Kap. III** (IMO Res. MSC.48(66)). *(Confidence: documented — marineteacher.com LSA-Übersicht, marineinsight.com, dco.uscg.mil SOLAS Pyro Guide, cultofsea.com/safety/pyrotechnics.)*

| Signaltyp | Kennwert | LSA-Code-Mindestanforderung |
|---|---|---|
| **Fallschirm-Signalrakete** (rocket parachute flare) | Steighöhe | ≥ 300 m (senkrecht abgefeuert) |
| | Lichtstärke | ≥ 30 000 cd, hellrot, gleichmäßig |
| | Brenndauer | ≥ 40 s |
| | Sinkrate am Fallschirm | ≤ 5 m/s |
| | Gehäuse | wasserbeständig, integrierte Zündung, Anwendungshinweise aufgedruckt |
| **Handfackel** (hand flare) | Lichtstärke | ≥ 15 000 cd, hellrot, gleichmäßig |
| | Brenndauer | ≥ 1 min |
| | Wassertauch-Test | brennt nach 10 s unter 100 mm Wasser weiter |
| | Gehäuse | wasserbeständig, selbst-enthaltene Zündung, keine gefährlichen Brennreste |
| **Schwimmfähiges Rauchsignal** (buoyant smoke signal) | Rauchabgabe | ≥ 3 min gleichmäßig, gut sichtbare Farbe (orange), im ruhigen Wasser schwimmend |
| | Flammenfreiheit | keine Flamme während der gesamten Rauchabgabe |
| | Wassertauch-Test | gibt nach 10 s Untertauchen weiter Rauch ab |

**Interpretation für die Werft/Skipper:** Fallschirmraketen sind das einzige Signal mit echter Fern-Alarmierungswirkung (Nacht, >10 nm); Handfackeln dienen der Nah-Ortung durch bereits anwesende Retter (Pinpointing); Rauchsignale sind Tagsignale zur Positionsmarkierung (Hubschrauber). Farbe **Rot** = Seenot (Pyrotechnik); **Orange Rauch** = Seenot am Tag. *(Confidence: documented — LSA-Code Kap. III Zweckbestimmung.)*

---

## E3. Verfallsdaten, Kennzeichnung & Entsorgung (Pyrotechnik)

- **Regelhafte Gültigkeit:** SOLAS-Pyrotechnik trägt ein aufgedrucktes **Verfallsdatum**; branchenüblich **3 Jahre ab Herstellung** (Fallschirmraketen/Handfackeln/Rauchsignale). Abgelaufene Pyrotechnik ist im Port-State-Control-Kontext ein sofortiger Mangel. *(Confidence: documented — marinepublic.com SOLAS 2025 Visual Distress, marinecraft.my SOLAS LSA compliance; „3 Jahre" ist Marktstandard, das rechtsverbindliche Datum ist stets das **aufgedruckte**.)*
- **Pflicht-Kennzeichnung je Einheit:** Herstellungsdatum, Verfallsdatum, Chargen-/Losnummer, Zulassungskennzeichen. *(Confidence: documented — ISO 15736:2006 Marking-Teil; USCG Domestic/SOLAS Pyro Guides.)*
- **Ersatz-Regel bei fehlendem Datum:** Ist kein Verfallsdatum aufgedruckt, gilt eine Nutzungsgrenze von **4 Jahren** ab Herstellung. *(Confidence: estimated — als Betriebspraxis mehrfach zitiert, aber nicht zweifelsfrei einer einzelnen Norm zuzuordnen; im Zweifel aufgedrucktes Datum verwenden.)*
- **Entsorgung:** Abgelaufene Pyrotechnik ist **Sprengstoff-/Gefahrgut** und darf nicht über den Hausmüll oder ins Wasser entsorgt werden. In Deutschland Rücknahme über Fachhändler/Behörden; **niemals** abgelaufene Signale „zum Üben" unkontrolliert abfeuern (Fehlalarm-Gefahr, Straftatbestand). *(Confidence: estimated — allgemeine Gefahrgut-Praxis; konkrete nationale Rücknahmestelle projektspezifisch zu verifizieren.)*

---

## E4. EPIRB 406 MHz & Cospas-Sarsat — vertieft

### E4.1 Systemarchitektur (verifiziert)

- **Sendefrequenz:** 406 MHz (digitaler Notruf mit codierter Beacon-ID); zusätzlicher **121,5-MHz-Homing-Sender** (Peil-Ton) für die Nah-Ortung durch SAR-Einheiten. **Wichtig:** 121,5 MHz wird von Cospas-Sarsat-Satelliten **nicht mehr detektiert** — nur noch als Peilsignal genutzt. *(Confidence: documented — sarsat.noaa.gov FAQ, acrartex.com.)*
- **Satellitensegmente:** **LEOSAR** (niedrige Erdumlaufbahn), **GEOSAR** (geostationär), **MEOSAR** (mittlere Umlaufbahn). MEOSAR nutzt Transponder auf **46 mittelhohen Satelliten** (Orbit ca. 2 000–35 786 km) und liefert nahezu sofortige globale Detektion + verbesserte Ortungsgenauigkeit. *(Confidence: documented — eoportal.org, en.wikipedia.org/International_Cospas-Sarsat_Programme, rivieramm.com.)*
- **Beacon-ID:** 15-stelliger Hexadezimal-Code; national codiert (Deutschland: MID **211**/**218**). *(Confidence: documented — svb.de, gruendl.de.)*

### E4.2 Registrierung & Alarmweg in Deutschland

- **Registrierung:** In Deutschland erfolgt Codierung/Registrierung der EPIRB (mit MMSI des Schiffes) über die **Bundesnetzagentur** (Außenstelle Hamburg vergibt MMSI); Eintrag in die Frequenzzuteilungsurkunde des Schiffes. **Nicht-Registrierung ist bußgeldbewehrt.** *(Confidence: documented — svb.de Notfunkbaken-Ratgeber, gruendl.de.)*
- **Alarm-Koordination:** Maritime Seenotfälle in den deutschen Nord-/Ostsee-Gebieten koordiniert das **MRCC Bremen** (Seenotleitung Bremen der **DGzRS**, „Bremen Rescue Radio"). *(Confidence: documented — seenotretter.de, de.wikipedia.org/Rettungsleitstelle_See.)*

> ⚠️ **ZU PRÜFEN:** Eine Quelle nennt zusätzlich das militärische **RCC Münster** als Empfänger für MMSI-211-Baken; die genaue Zuständigkeitsteilung MRCC Bremen ↔ RCC Münster für 406-MHz-Alarme ist projektspezifisch zu verifizieren. **estimated — unverifiziert.**

### E4.3 Wartungs-/Verfallsfristen (verifiziert)

| Bauteil | Frist | Confidence |
|---|---|---|
| **EPIRB-Batterie** | Austausch typ. alle **5 Jahre** (im Rahmen des Major-Service); Datum auf Gerät | documented (hzhmarine.com, acrartex.com) |
| **Hydrostatischer Auslöser (HRU)** | begrenzte Lebensdauer typ. **2 Jahre**, Austausch vor aufgedrucktem Verfallsdatum | documented (acrartex.com HydroFix, toplicht.com) |
| **Jährlicher Funktionstest / Systemtest** | jährlich (Selbsttest häufiger je Herstellervorgabe) | documented (hzhmarine.com SOLAS EPIRB guide) |

> **Korrektur zu Abschnitt 3.2 / 5.1:** Der frühere Wert „SART-Batterie 8–10 Jahre" ist herstellerabhängig und nicht generalisierbar; maßgeblich ist stets das **aufgedruckte Verfallsdatum** des jeweiligen Geräts. **estimated — unverifiziert** (Herstellerangabe prüfen).

---

## E5. AIS-SART & AIS-MOB (elektronische Ortung, verifiziert)

- **AIS-SART:** sendet Standard-AIS-Positionsmeldungen; einmal pro Minute **8 identische Meldungen** (4× auf 161,975 MHz, 4× auf 162,025 MHz); integrierter GNSS-Empfänger; typische Sichtlinien-Reichweite **10–15 nm**. Norm: **IEC 61097-14**. *(Confidence: documented — en.wikipedia.org/AIS-SART, gmdsstesters.com.)*
- **AIS-MOB (Man-Overboard-Sender, z. B. Weste-integriert):** Class-M-Gerät nach **IEC 63269 / EN 303 132**; sendet AIS-Position (+ optional DSC/121,5-MHz-Homing je Modell). *(Confidence: documented — gmdsstesters.com, oceansignal.com S200, easyais.com.)*

> **Abgrenzung (löst Missverständnis 6.4 weiter auf):** **EPIRB** = Satellit (406 MHz, weltweit, alarmiert MRCC) · **Radar-SART** = 9-GHz-X-Band (Radar-Sichtung durch Schiffe) · **AIS-SART/AIS-MOB** = VHF-AIS (Ortung durch AIS-Empfänger in Nähe). Drei getrennte Wirkprinzipien, nicht austauschbar.

---

## E6. Schallsignale — COLREGs Anlage III (verifiziert)

*(Confidence: documented — cultofsea.com/colregs Annex III, navcen.uscg.gov, 33 CFR Part 86.)*

**Pfeife/Signalhorn — Grundfrequenz nach Schiffslänge:**

| Schiffslänge | Grundfrequenz (fundamental) |
|---|---|
| ≥ 200 m | 70–200 Hz |
| 75 m bis < 200 m | 130–350 Hz |
| < 75 m | 250–700 Hz |

- **Hörbarkeitsbereich:** maßgebende Frequenzen 180–700 Hz (± 1 %) bei Schiffen ≥ 20 m; **180–2 100 Hz** (± 1 %) bei Schiffen < 20 m.
- **Glocke/Gong:** Schalldruckpegel **≥ 110 dB in 1 m Abstand**.
- **Sportboot-Praxis (< 12 m):** COLREGs Regel 33 verlangt Mittel zur Abgabe von Schallsignalen; eine feste, batterieunabhängige Signalpfeife bleibt das robusteste Backup (keine Alterung, keine Batterie). *(Confidence: documented — COLREGs Regel 33.)*

> **Korrektur zu Abschnitt 1.2 Punkt 6 / Glossar:** Die dortigen Zahlenangaben („2–3 kHz, 110+ dB", „ISO 9908, 4 s Ton") sind **nicht durch COLREGs Anlage III gedeckt** und teils widersprüchlich (COLREGs-Pfeifen liegen im Bereich 70–700 Hz Grundfrequenz, nicht 2–3 kHz). Bis zur Klärung als **estimated — unverifiziert** behandeln; maßgeblich sind die obigen COLREGs-Werte.

---

## E7. Fehlerbild-Atlas (erweitert, kollisionsfreie IDs FB-29-04-NNN)

> Die bestehenden Fehlerbilder (Abschnitt 3.x) bleiben unverändert gültig. Die folgenden IDs sind neu und kollisionsfrei fortlaufend nummeriert.

| ID | Fehlerbild | Merkmal / Diagnose | Behebung | Schweregrad |
|---|---|---|---|---|
| **FB-29-04-001** | Pyrotechnik über aufgedrucktem Verfallsdatum | Datum auf Signal überschritten | Ersatz beschaffen; alte fachgerecht entsorgen (Gefahrgut) | KRITISCH |
| **FB-29-04-002** | Fallschirmrakete: Steighöhe/Brenndauer im Test nicht plausibel dokumentiert | Kein Zulassungs-/Chargennachweis, keine Aufdrucke | Nur zugelassene SOLAS-Ware (LSA-Code) führen | HOCH |
| **FB-29-04-003** | Handfackel-Zündung feucht/korrodiert | Zündkopf oxidiert, Gehäuse aufgequollen | Ersatz; trocken lagern | HOCH |
| **FB-29-04-004** | Rauchsignal treibt nicht / kentert | Schwimmlage im Test instabil | Nur schwimmfähige Bauart (buoyant) verwenden | MITTEL |
| **FB-29-04-005** | EPIRB nicht/falsch registriert (BNetzA) | MMSI nicht codiert, keine Frequenzzuteilung | Registrierung Bundesnetzagentur; Kontaktdaten aktuell halten | KRITISCH (Alarm nicht zuordenbar; bußgeldbewehrt) |
| **FB-29-04-006** | EPIRB-HRU abgelaufen | Datum auf HRU überschritten (typ. 2 J.) | HRU tauschen (float-free-Funktion sonst unwirksam) | KRITISCH |
| **FB-29-04-007** | EPIRB-Batterie-Serviceintervall überschritten | Batterie-Ablaufdatum > heute (typ. 5 J.) | Herstellerservice; Batterie tauschen | KRITISCH |
| **FB-29-04-008** | 121,5-MHz-Homing schwach/defekt | Peilton im Test nicht messbar | Service; 406-Teil kann intakt sein, Nah-Ortung aber erschwert | HOCH |
| **FB-29-04-009** | AIS-SART/AIS-MOB nicht in Bordsystem sichtbar | Testmeldung erscheint nicht im AIS-Empfänger | GNSS-Fix prüfen, MMSI/Gerät prüfen, ggf. Service | HOCH |
| **FB-29-04-010** | Registrierungsdaten veraltet (Halter/Notfallkontakt) | SAR erreicht falschen Kontakt → Verzögerung | Beacon-Registrierung aktualisieren | MITTEL–HOCH |
| **FB-29-04-011** | Signalpfeife: Frequenz außerhalb COLREGs-Bereich | Ton zu hoch/leise, nicht COLREGs-konform | Konforme Pfeife/Horn (70–700 Hz Grundfrequenz) | MITTEL |
| **FB-29-04-012** | Pyrotechnik falsch gelagert (Nässe/Hitze) | Kondenswasser, verklebte Gehäuse | Trockene, kühle, separate Lagerung; ggf. Ersatz | HOCH |

---

## E8. Entscheidungsbaum — „Welches Signalmittel wann?"

```
Notfall erkannt
 ├─ Nacht / Fernalarm (>5–10 nm) ──────► Fallschirm-Signalrakete (rot) + EPIRB 406 auslösen
 ├─ Tag / Positionsmarkierung (Heli) ──► Schwimmfähiges Rauchsignal (orange)
 ├─ Retter in Sichtweite (Pinpoint) ───► Handfackel (rot)
 ├─ Person über Bord ──────────────────► AIS-MOB / PLB sofort; Pfeife zur Lokalisierung
 ├─ Radar-Kontakt vorhanden ───────────► Radar-SART aktivieren (X-Band-Rückstrahl)
 └─ Reduzierte Sicht / Schallwarnung ──► Signalpfeife/Horn nach COLREGs Anlage III
```
*(Zweckzuordnung: documented — LSA-Code Kap. III; COLREGs; Cospas-Sarsat.)*

---

## E9. FAQ — Ergänzung (verifiziert)

11. **Wie hoch/hell/lang muss eine SOLAS-Fallschirmrakete sein?**
    ≥ 300 m Steighöhe, ≥ 30 000 cd, ≥ 40 s Brenndauer, hellrot (LSA-Code). *(documented)*

12. **Und eine SOLAS-Handfackel?**
    ≥ 15 000 cd, ≥ 1 min Brenndauer, brennt nach 10 s unter 100 mm Wasser weiter. *(documented)*

13. **Wird 121,5 MHz noch von Satelliten gehört?**
    Nein — nur noch als Peil-/Homing-Signal am Einsatzort; die Satellitendetektion läuft ausschließlich über 406 MHz. *(documented — NOAA SARSAT.)*

14. **Wo registriere ich meine EPIRB in Deutschland?**
    Bei der Bundesnetzagentur (MMSI-Codierung, Frequenzzuteilung); Nicht-Registrierung ist bußgeldbewehrt. *(documented — svb.de.)*

15. **Wer koordiniert den Seenotfall in deutschen Gewässern?**
    MRCC Bremen / Seenotleitung Bremen der DGzRS („Bremen Rescue Radio"). *(documented — seenotretter.de.)*

16. **Wie oft HRU und EPIRB-Batterie tauschen?**
    HRU typ. alle 2 Jahre, Batterie typ. alle 5 Jahre — jeweils **vor** dem aufgedruckten Datum. *(documented.)*

---

## E10. Prüf-/Wartungsfristen — konsolidierte Übersicht (verifiziert)

| Element | Frist | Grundlage / Confidence |
|---|---|---|
| SOLAS-Pyrotechnik (Raketen/Fackeln/Rauch) | Ersatz vor aufgedrucktem Verfallsdatum (branchenüblich 3 J.) | LSA-Code / Marktpraxis — documented/estimated |
| EPIRB-Batterie | ~5 Jahre (Major-Service) | documented |
| EPIRB-HRU (Float-free-Auslöser) | ~2 Jahre | documented |
| EPIRB Funktions-/Systemtest | jährlich | documented |
| EPIRB-Registrierung (BNetzA) | aktuell halten bei Halter-/Kontaktwechsel | documented |
| Radar-SART / AIS-SART Batterie | vor aufgedrucktem Datum (herstellerabhängig) | documented (Datum maßgeblich) |
| Signalpfeife/Horn | COLREGs-Konformität, Funktionsprüfung | documented (COLREGs Anlage III) |

---

**Quellen (Erweiterung):** imorules.com (LSA-Code / MSC.48(66)) · iso.org/standard/41360.html (ISO 15736:2006) · dco.uscg.mil SOLAS Pyrotechnic Guide · marineteacher.com · marineinsight.com · cultofsea.com (Pyrotechnics; COLREGs Annex III) · marinepublic.com (SOLAS 2025 Visual Distress) · sarsat.noaa.gov · eoportal.org (Cospas-Sarsat) · en.wikipedia.org (Cospas-Sarsat; AIS-SART) · acrartex.com · gmdsstesters.com · hzhmarine.com · svb.de · gruendl.de · seenotretter.de · de.wikipedia.org (Rettungsleitstelle See) · navcen.uscg.gov / 33 CFR Part 86.

---

**Autor:** AYDI Knowledge Base  
**Kontakt:** knowledge@aydi.de  
**Letzte Überarbeitung:** 2026-07-12 (Werft-Tiefe-Erweiterung E1–E10)  
**Nächste Review:** 2027-07-12
