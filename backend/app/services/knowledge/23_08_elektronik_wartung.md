# Elektronik Wartung und Troubleshooting – AYDI Knowledge Base

## 1. Einführung und Übersicht

### 1.1 Elektronik-Wartung als Werterhaltung

Elektronische Systeme an Yachten sind extremem Stress ausgesetzt: Salzwasser-Aerosole, Feuchtigkeitszyklus, Vibration, Temperaturgradienten, UV-Strahlung und intermittente Nutzung. Eine strukturierte Wartung erhält nicht nur Funktionalität, sondern schützt Investitionen und verhindert kritische Ausfälle bei See.

**Wartungs-Axiome:**
- Salzluft korrodiert Kontakte schneller als offenes Wasser (chloride-Konzentration in Spray).
- Feuchte + Aktivspannung = galvanische Korrosion an bimetallischen Kontakten.
- Intermittente Nutzung verschärft Lagering-Korrosion (Oxidation an Ruhekontakten).
- Prophylaxe kostet 5–10 % der Reparatur-Kosten; ignorieren kostet 100 %.

Die Elektronik-Wartung gliedert sich in:

| Wartungstyp | Zeitrahmen | Fokus | Werkzeuge |
|---|---|---|---|
| **Vorbeugend (PM)** | Monatlich–Jährlich | Reinigung, Schutzöle, Kontakt-Konservierung | CRC, DeoxIT, Inspektionslampe |
| **Zustandsbezogen (CBM)** | Nach Jahreszeit oder Symptomen | Messung (Isolation, Kontinuität), Thermografie | Multimeter, IR-Kamera |
| **Korrigierend (CM)** | Sofort bei Ausfall | Reparatur, Tausch, Fehlersuche | Lötausrüstung, Ersatzteile |
| **Verbessernd (Upgrade)** | Bei Modularisierung | Neue Stecker, Leitungsführung, Redundanz | Krimper, Heatshrink, CAD |

### 1.2 Systemische Ebenen

**Ebene 1 — Stromversorgung:**
Batterien, Landstrom-Interface, Wechselrichter, Laderegler, Sicherungen, Schutzschalter. Ausfallrate: Korrosion an Batteriepolen, Schwellungen, interne Zellenausfälle.

**Ebene 2 — Verteilung:**
Schaltschränke, Bussysteme (NMEA 2000, CAN, 1-Wire), Kabel-Durchführungen, Verteiler-Blöcke. Ausfallrate: Kontaktverschleiß, Isolations-Risse, EMV-Störungen.

**Ebene 3 — Sensoren & Aktoren:**
Druck-, Temperatur-, Strom-, Spannungs-Sensoren; Motore, Magnetventile, Alarme. Ausfallrate: Sensor-Drift, Aktuation-Verzögerung, Kalibrierungs-Fehler.

**Ebene 4 — Integration & Daten:**
Autopilot-Computer, Chart-Plotter, Maschinenraum-Panel, WLAN, AIS, VHF-Integration. Ausfallrate: Software-Bugs, Datenverlust, Authentifizierungs-Fehler.

---

## 2. Grundlagen und Theorie

### 2.1 Elektronik-Alterung in Marineumgebung

**Oxidation an Metallkontakten** (primärer Fehlermechanismus):
- Kupfer: Cu → Cu₂O (rötlich, hoher Widerstand ~10 MΩ pro mm²)
- Silber: Ag → Ag₂S (schwarz, sehr hoher Widerstand ~100 MΩ+)
- Gold (nur auf Premium-Kontakten): Au bleibt stabil, aber unkontrollierte Goldplattierung bricht ab (Dealloying).
- Zinn: Sn → SnO₂ (graues Pulver, kann Whisker bilden, elektromigration).

**Feuchte-Eindringung:**
Elektronische Module mit unzureichender Versiegelung ziehen Wasser kapillar ein:
- Leiterplatten-Kupfer oxidiert → Leiterbahn-Widerstand steigt oder Kurzschluß entsteht.
- Elkos (Elektrolyt-Kondensatoren) verlieren Kapazität oder explodieren bei hoher Spannung.
- ICs verklemmen oder zeigen intermittente Kontaktfehler.

**Vibration + Korrosion-Koppelung:**
Vibration verstärkt Kontakt-Verschleiß:
- Kaltschweißung bricht auf (Au/Cu-Oberflächenbindung).
- Kontakt-Material wird abgerieben, neue Oberfläche oxidiert sofort.
- Gold-beschichtete Stecker zeigen Verschleiß nach 20–30 Zyklen bei feuchtem Salzmilieu.

### 2.2 IP-Klassifikation (Schutzart nach IEC 60529)

Marine-Elektronik nutzt IP-Codes: IP**XY** (X = Fremdkörper/Staub, Y = Wasser)

| Code | Staub | Wasser | Marine-Anwendung |
|---|---|---|---|
| **IP54** | Staubgeschützt | Spritzwasser | Deck-Schalter, offene Sensoren |
| **IP67** | Staubdicht | Kurzzeitig submersibel (1m, 30min) | Thru-Hull-Sensoren, Cockpit-Geräte |
| **IP68** | Staubdicht | Kontinuierlich submersibel, definierte Tiefe | Engine-Drucksensoren, Ankerwinde-Motor |
| **IP65** | Staubdicht | Strahl- & Spritzwasser | Maschinenraum-Panel, Batteriekasten |

**Fehlinterpretation:** IP67 ≠ "wasserdicht". Es bedeutet max. 1m Eintauchtiefe für 30 min. Bei Jahres-Dauerlagerung am Liegeplatz kann Kondenswasser eindringen.

### 2.3 Steckertypen und Kontakt-Profile

**NMEA 2000 Micro-C (Garmin, Raymarine, Lowrance):**
- 5-polig Mini-DIN, gekapselt in Schraub-Schutzkappen.
- Kontakt-Material: vergoldetes Kupfer, Nennstrom 5A @ 12V.
- Ausfallmechanismus: Stecker-Einsatz korrodiert innen (Salzluft diffundiert trotz Kappe), Kontakt-Widerstand steigt → CAN-Bus-Fehler.
- Wartung: monatliche Sichtprüfung, jährliche DeoxIT D5 (nicht D100 – zu aggressiv für vergoldete Micro-C).

**Deutsch DT-Serie (Victron, Mastervolt, GEDI):**
- 2–8-polig, mit oder ohne Druckknopf-Verriegelung.
- Kontakt-Material: silberplattiertes Kupfer, vergoldet, Nennstrom bis 30A.
- Ausfallmechanismus: Kontakt-Verdrosselung bei Teillast (Vibration), galvanische Migration bei fehlender Entwässerung.
- Wartung: 6-monatlich überprüfen, bei Nutzung >6 Monate Lagern Stecker-Schutzkappen verwenden.

**AMP (Tyco/Amphenol) Multi-Pin Connectors:**
- 10–64 polig, Raster 2.54mm oder 3.96mm.
- Kontakt-Material: Zinn/Gold-Laminate oder rein Gold.
- Ausfallmechanismus: Zinn-Whisker bei hoher Stromdichte, thermisches Kriechen bei Vibrationen.
- Wartung: 2-jährlich Isolations-Messung, keine Kontakt-Reinigung (Verschleiß überwiegt Nutzen).

**Marinco/Hubbell Shore Power (230V 3-Phase):**
- Industriestecker IP67, 16–125A, Kupfer-Kontakte.
- Ausfallmechanismus: Oxidation am Kontakt-Interface bei intermittenter Nutzung, Thermoverschleiß bei Überlast.
- Wartung: Saisonal vor Landstrom-Kupplung Kontakte prüfen, CRC WD-40 marine spray (minimal, nur Außenseite), jährlich Drehmoment-Kontrolle der Verschraubung.

### 2.4 Galvanische Korrosion und Bimetallische Paare

Zwei unterschiedliche Metalle in feuchter Umgebung bilden ein Mikro-Galvani-Element:

| Paar | Anode (korrodiert) | Kathode | ΔV (V) | Risiko | Lösung |
|---|---|---|---|---|---|
| Cu/SS 316 | Kupfer | SS | 0.35 | Hoch | Isolation, Ni-Schicht |
| Al/Cu | Aluminium | Kupfer | 0.65 | Sehr Hoch | Nur Al-Al oder Cu-Cu |
| Zn/Cu | Zink | Kupfer | 1.10 | Kritisch | Trennlack, Opfer-Anode |
| SS 304/SS 316 | 304 | 316 | 0.10 | Moderat | Entsalzung, V2A zertifizieren |

**Praktische Regel:** In feuchtem Salzmilieu keine unterschiedlichen Metalle direkt kontaktieren. Isolieren mit PTFE-Scheibe oder Trennlack.

### 2.5 EMV (Elektromagnetische Verträglichkeit)

Marine-Elektronik ist EMV-Risiken ausgesetzt:

1. **Externe EMV:** Radarsender (X-Band ~10 GHz, Leistung 25 kW), VHF-Funk (156–162 MHz, 25 W), Lightning.
2. **Interne EMV:** Wechselrichter (Schaltverluste), Motor-Starter (Schalt-Transiente), Laderegler (PWM-Interferenz).

**Minderung:**
- Geschirmte Leitungen für CAN, NMEA, Sensoren (nur Schirm am Datengerät erden, nicht beidseitig).
- Ferrit-Toroide auf Stromversorgung (1–10 mH, 50–100 MHz Resonanz).
- Breite Busse für -12V/GND (Impedanz < 10 mΩ bei 1 MHz).

### 2.6 Kondensator-Alterung und Elkos

Elektrolyt-Kondensatoren degradieren mit Rate ~50 % Kapazität pro 10 K Temperaturanstieg:

- Neue Elko: C₀ = 100 µF @ 20 °C
- Nach 5 Jahren Dauerbetrieb @ 40 °C Marina: C₅ ≈ 70 µF (degradiert ~30 %)
- Nach 10 Jahren, Billig-Marke: C₁₀ ≈ 40 µF oder ausgegast (ESR > 5 Ω)

**Wartung:**
- Alle Elkos >10 Jahre: 5-Jahres-Inspektionen einführen.
- Alte Wechselrichter (>8 Jahre, hohe Auslastung): Kapazität messen oder Expansion prüfen.
- Gefährlich: Schwellende, nässende oder durchgerostete Elkos müssen sofort getauscht werden.

### 2.7 Software-Lifecycle und Firmware-Management

Marine-Geräte-Firmware ist oft veraltet:

| Gerät | Typisches Alter | Risiken | Update-Schwellenwert |
|---|---|---|---|
| Chart-Plotter | 3–8 Jahre | Sicherheitslücken, Kompatibilität | >5 Jahre = dringend |
| Autopilot | 2–10 Jahre | Kontrollverlust, Drift-Akkumulation | >7 Jahre = prüfen |
| Batterie-Monitor | 1–5 Jahre | Kapazitäts-Fehler, Laderegler-Ausfall | >3 Jahre = kalibrieren |
| VHF-Radio | 2–15 Jahre | Frequenz-Drift, Modulations-Fehler | >10 Jahre = Service |

**Best Practice:**
- Firmware-Version bei Jahresservice dokumentieren.
- Hersteller-Website monatlich prüfen (automatisierte Notifikation erwägen).
- Update nur im Hafen, mit Batterie >80 %, während Update nicht unterbrechen.

---

## 3. Typenübersicht – Wartungsintervalle

### 3.1 Monatliche Wartung

**Stromversorgung:**
- Batteriespannungen messen (Sollwert ±0.5V).
- Sichtprüfung Batteriepole: Grünspan, Sulfation, Undichtigkeit.
- Erdungsschraubverbindung prüfen (Drehmoment 1–2 Nm Kupfer-M6).

**NMEA/CAN-Netzwerk:**
- Alle Stecker-Kappen an Deck- und Maschinenraum-Geräten vorhanden?
- Sichtprüfung auf Feuchte in Micro-C-Stecker-Innenraum (Lupe + LED-Lampe).
- Keine neuen Fehlermeldungen im Chart-Plotter (CAN-Bus-Fehler-Zähler prüfen).

**Sichtprüfung Allgemein:**
- Kabel-Beschädigungen an häufig gegangenen Wegen (Kabeljau unter Floorboards).
- Temperatur-Anomalien an Schaltschrank (IR-Kamera oder Handprobe).
- Wasserschäden im Maschinenraum (nach Regen oder Seen-Passage).

### 3.2 Saisonale Wartung (vor Auslaufen & nach Auftakeln)

**Vor der Saison (Frühjahr):**
- Batterie-Kapazität: Last-Test mit 50 % Nennkapazität, Spannungsabfall < 0.2V über 10 min.
- Elektrische Lastverteilung überprüfen: Alle 230V-Geräte testen, Stromaufnahme notieren (Trend-Analyse für Verschleiß).
- Engine Start-System: Anlasser-Drehmoment, Startspannung (min. 10.5V @ Anlasser-Klemmen während Starter läuft).
- Datengeräte-Kalibrierung: Kompass-Variation, GPS-Offset, Wasserwärme-Sensor.
- Antrieb-Sensoren: Drehzahl-Geber, Kühlwasser-Temperatur-Sensor (Widerstand messen gegen Sollwert-Tabelle im Service-Handbuch).

**Nach der Saison (Herbst):**
- Konservierung Stromversorgung: CRC 6-66 auf alle freiliegenden Kupfer-Kontakte, Batteriepole mit Vaseline-Film.
- Winterfestmachung Datengeräte: Micro-C-Stecker einzeln mit Schutzkappen versehen, in Silica-Gel-Beutel lagern.
- Überprüfung Schaltschrank-Entfeuchtung: Silica-Gel austauschen (wenn dunkelblau → gesättigt).
- Datenbank-Backup: Kartographie, Wegpunkte, Einstellungen auf externe USB exportieren.

### 3.3 Jährliche Wartung

**Umfangreiche Inspection:**
- Isolationsprüfung aller Stromkreise (Megaohmeter, 500V DC): Sollwert >1 MΩ pro Stromkreis (nicht <500 kΩ).
- Durchgängigkeit alle Leitungen (Continuity, 200 mA Prüfstrom): R < 0.1 Ω für Stromtragend, R < 1 Ω für GND/Return.
- Spannung unter Last (Engine läuft, Verbraucher angeschaltet): Bordnetz 13.5–14.5V, 230V-Versorgung 220–240V (3-Phase Phasengleichheit prüfen).

**Kontakt-Konservierung (intensive Phase):**
- Alle zugänglichen Stecker öffnen (sofern Betrieb es erlaubt): Micro-C, AMP Multi-Pin, Deutsch DT.
- Kontakt-Oberfläche inspizieren auf Grünspan, Oxidation (Färbung, Rauhheit).
- Bei Verschmutzung: DeoxIT D5 (1–2 Tropfen auf Bürste, leicht abwischen, nicht reiben), 5 min wirken lassen, Stecker 10x kuppeln/entkuppeln, Rest mit fusselfreiem Tuch abwischen.
- Kontaktverschleiß im Stecker durch Vibrationen: Micro-C-Kontakte können nicht nachjustiert werden → Stecker-Modul tauschen (ca. 50–80 EUR pro Stecker bei OEM).

**Software-Updates:** Gerätehersteller kontaktieren; verfügbare Firmware-Updates einspielen.

**Spannungsregler-Inspektionen:** Laderegeler, Gleichrichter, Wechselrichter: Gehäusetemperatur im Normalbetrieb messen (IR-Kamera), kein Rattling/Buzzing.

### 3.4 5-Jahres-Wartung (Großer Service)

**Tiefprüfung Stromversorgung:**
- Batterie-Kapazitätsprüfung mit professionellem Testgerät (Megger, Fluke): Interne Impedanz messen, Zellen-Symmetrie (LiFePO₄ Balancer-Status prüfen).
- Laderegler-Diagnose: Ausgangsspannung unter simulierter Last, Schnelllade-Profil, Temperature-Compensation.
- Wechselrichter-Effizienz unter Nennlast (soll >90 %), Oberwellen-Distortion <5 %.

**Stecker-Management:**
- Alle Multi-Pin-Stecker (Deutsch DT, AMP) ausmessen: Kontakt-Widerstand (max. 10 mΩ pro Kontakt mit 4-Draht-Messung).
- Verschleißstecker tauschen (Kriterium: Kontakt-Widerstand > 20 mΩ oder sichtbarer Gold-Verschleiß).
- Kabelquerschnitte überprüfen (Spannungsfall bei Nennlast <3 % über Gesamtzweig).

**Datensicherung & Diagnose-Backup:** Chart-Plotter, Autopilot, Batterie-Monitor, VHF: Firmware-Version, Geräte-ID, letzte Service-Einträge dokumentieren.

---

## 4. Produktlinien – Wartungs- und Konservierungsmittel

### 4.1 CRC Marine 6-66 (Korrosion-Schutz, Universal)

**Zusammensetzung:**
- Aliphatic Mineralöl-Basis (Low-Volatility).
- Lanolin-Wachse (Langzeit-Hafthaftung).
- Rust inhibitor compounds (Benzotriazol-Familie).
- Wasser-Verdränger (max. 5 % Kapazität zum Wasseraufnahmе).

**Anwendung – Elektronik:**
- Batterie-Pole (nach Reinigung): dünne Schicht CRC 6-66 auf Kupfer/Blei-Oberfläche, trocknet zu dünnem Öl-Wachs-Film.
- Schraub-Verbindungen (M6–M8 Durchmesser): 1–2 Tropfen auf Gewinde, bewahrt Gleitreibung und Kontakt-Oxydation.
- **NICHT verwenden** auf Gold-beschichteten Kontakten (Öl bleibt haften, erschwert Stecker-Kupplung).
- **NICHT verwenden** auf Kunststoff-Schaltern oder Sensorgehäusen (Quellung möglich).

**Lagering:** 6–8 Monate Haltbarkeit nach Öffnung (Verdampfung). In kühlem, trockenem Schrank lagern.

### 4.2 Caig DeoxIT D-Serie (Kontakt-Reinigung & Konservierung)

**D5-Formulierung** (mittlere Reinigungskraft, Elektronik-Standard):
- Wirkstoff: Thiourea-Komplex (Oxidbruchspaltung ohne aggressive Laugen).
- Verdampfung: Schnell (30–60 sec), hinterlässt Schutzfilm.
- Sicherheit: Nicht-brennbar, low-volatility nach Trocknung.

**Anwendung – Elektronik:**
- Micro-C NMEA-Stecker (monatlich bei Salzwasser-Exposition):
  - Kappe abschrauben, DeoxIT D5 auf kleine Bürste (z.B. Zahnbürste), leicht in Stecker-Innenraum einführen.
  - 2–3 Tropfen direkt auf Kontaktsatz, 5 min einwirken.
  - Stecker 10x kuppeln/entkuppeln (Kontakte selbst reinigen).
  - Mit fusselfreiem Tuch + Lupe überprüfen.
- Deutsch DT Multi-Pin (6-monatlich, oder nach Unterbrechung):
  - DeoxIT Spray-Düse ansetzen, kurzer Sprühstoß in Stecker-Höhlung.
  - 5 min trocknen, Stecker mehrmals kuppeln.
- **Warnung:** D100 (hochkonzentriert) NUR für schwere Oxidation; auf vergoldeten Kontakten kann D100 die Goldplattierung anlösen.

**Preis & Verfügbarkeit:** ~15 EUR / 200 ml Flasche (mit Aufsatz-Pinsel), Amazon/Fachhandel.

### 4.3 CorrosionX (Langzeit-Schutzfilm, Marine-Grade)

**Zusammensetzung:**
- Hydrophobe wachsartige Emulsion (Patent: MG X-1000 formula).
- Inert zu Kunststoffen und Gummi.
- Langzeit-Hafthaftung (bis 12 Monate nach Anwendung).

**Anwendung – Elektronik:**
- Engine-Raum Schaltschränke (saisonale Versiegelung vor Winter): Dünn aufsprühen, trocknet zu transparent-matten Film.
- Mastenverschraubungen (Alu/SS Bimetall-Risiko): CorrosionX auftragen vor Winter, verhindert Salzwasser-Eindringung während Lagering.
- **NICHT auf aktive Kontakte**, da Film Kurzschluß-Risiko bei feuchtem Eindringen erhöht.

**Lagering:** 24 Monate haltbar, Spray-Dose alle 6 Monate schütteln (Phasenseparation vermeiden).

### 4.4 Tef-Gel (PTFE-basierte Fett-Emulsion, Hochtemperatur)

**Zusammensetzung:**
- PTFE (Teflon) Partikel in synthetisches Öl-Träger.
- Keine Volatilität (bleibt unbegrenzt).
- Temperaturbeständig bis +230 °C.

**Anwendung – Elektronik:**
- Mastenverschraubungen, Motor-Befestigungen (Vibrations-Dämpfung): Dünn auftragen auf Gewinde vor Zusammenbau.
- Schieber-Kontakte in älteren Schaltschränken (z.B. manuelle 63A Last-Schalter): Tef-Gel auf Schleif-Flächen reduziert Stick-Slip und Kontakt-Verschleiß.
- **NICHT verwenden** auf Stecker-Kontakten (Film bleibt, reduziert Kontakt-Druck).

**Lagerung:** 3 Jahre haltbar, in Dunkeln lagern (UV-Degradation).

### 4.5 Ancor Marine-Kabel & Crimp-Systeme (Kabel-Erneuerung)

Bei Kabel-Erneuerung (Oxidation in Litzenleitern, Isolations-Risse):

**Ancor Qualitätskriterium:**
- UL 1426 (Marine-Kabel, Salz-Korrosions-Résistance).
- AWG-Querschnitt (American Wire Gauge): 10 AWG = 5.26 mm² (15A @ 12V über 3m Lauflänge max. 3 % Spannungsfall).
- Isolation: Blau, Rot, Schwarz, Gelb/Grün (nach ABYC-Standard, nicht willkürlich).

**Crimp-Werkzeug:**
- Presswerkzeug (z.B. Paladin PA-1565, ~200 EUR) oder Professionelles Crimpen lassen (ca. 2 EUR pro Crimpkontakt bei Fachhandel).
- Kontakt-Material: verzinntes Kupfer, Quetsch-Länge 8–10 mm (nicht zu kurz, nicht zu lang).
- Nach dem Crimpen: Shrink-Schlauch überziehen (3:1-Krumpfquote), mit Heißluft schrumpfen (nicht Feuerzeug).

### 4.6 Victron SmartShunt & Batterie-Monitor (Diagnose-Middleware)

**Victron Ecosystem:**
- SmartShunt 500A/48V (Batterien >2 kWh Speicher): Misst Spannug, Strom, Temperatur, berechnet SoC (Ladezustand).
- BMV-702S (älteren, analog): keine Bluetooth, aber robust gegen EMV.

**Wartungs-Integration:**
- SmartShunt-Firmware 2x jährlich prüfen (Bluetooth → Victron Connect App).
- Kalibrierung jährlich: leere Batterie voll laden, Kalibrierungs-Routine im App durchführen (rechnet aktuelle Kapazität neu).
- Strom-Shunt-Verschleiß: Nach 8–10 Jahren kann Shunt-Widerstand abweichen (R sollte <100 µΩ sein); Service-Check: Spannungsabfall @1000A messen (soll 100 mV entsprechen 100 µΩ).

---

## 5. Hersteller-Datenbank

### 5.1 Victron Energy (NL)

**Kernprodukte:** Batterie-Monitore, Laderegler, Wechselrichter, BMS.
- SmartShunt 500A/48V (Link: victron.com/de/produkte/smart-shunt).
- Skylla-TG Landstrom-Ladegeräte (48/100, 48/50): konservativ kalkuliert, <1 % Ausfallrate in 10 Jahren.
- MultiPlus Wechselrichter (bis 5 kW, 3-phasig): gutes EMV-Design, Firmware-Updates häufig.

**Wartungs-Support:** Hervorragende deutsch-sprachige Dokumentation, Updates über Victron Connect App.

### 5.2 Mastervolt (NL)

**Kernprodukte:** DC-Systeme, Wechselrichter, Batterie-Management.
- ChargeMaster (autonome Landstrom-Laderegler): robust, schwer zu prüfen (keine Datenbus-Integration).
- MasterVolt CombiMaster (Wechselrichter+Laderegler in Eins): Spardesign, aber kompliziertere Fehlersuche.

**Wartungs-Support:** Deutsch-sprachige Hotline, aber Firmware-Updates müssen manuell eingespielt werden.

### 5.3 Garmin (USA)

**Kernprodukte:** Chart-Plotter, GPS, NMEA-Netzwerk-Hubs.
- GPSMAP 7012xsv (Touchscreen, NMEA 2000): Standard in modernen Seefahrzeugen; Firmware-Updates monatlich verfügbar.
- Micro-C-Stecker-Ausfälle bei >5 Jahren normal, Garmin tauscht Stecker-Modul gegen Gebühr (~80 EUR).

**Wartungs-Support:** Online-Support.garmin.com, deutsche Bedienungsanleitungen vorhanden.

### 5.4 Raymarine (UK)

**Kernprodukte:** Autopilot-Systemen, Instrument-Cluster, NMEA 2000.
- Axiom XM Plotter (neues Flagship, Android-basiert): Stabiler, aber Software-Updates kritisch.
- Evolution-Autopilot (alte Modelle, 2010–2015): bekannt für Kompass-Drift nach 5 Jahren (Kalibrierung notwendig).

**Wartungs-Support:** Anglophone Support, deutsche Manuals limitiert.

### 5.5 Humminbird (USA)

**Kernprodukte:** Fishfinder, Plotter.
- HELIX Modelle: robust, aber proprietäres Kartensystem (Update-Abhängigkeit).

**Wartungs-Support:** US-centric, deutsche Unterstützung begrenzt.

### 5.6 B&G (UK, jetzt auch mit Garmin)

**Kernprodukte:** Instrumenten-Cluster, Windmessung, Radar.
- Zeus Modelle: NMEA 2000 integriert, aber Micro-C-Stecker-Qualität variabel (Chinesische Verträge).

**Wartungs-Support:** Anglophone Hotline, Deutsch-Dokumentation sporadisch.

---

## 6. Fehlerbild-Atlas – 12 Typische Ausfallmuster

### 6.1 Grünspan auf Batteriepol (Kupfer-Oxidation)

**Ursache:** Salzluft + Feuchte + galvanische Spannung zw. Blei-Batterie und Kupfer-Kabel.

**Symptome:**
- Sichtbarer grüner Belag auf Batterie-Plusanschluss oder in Kabelschuh.
- Spannungsabfall an Batterie-Pol: U_Pol = 12.0V, aber U_Last (10m Kabel weg) = 11.2V → Widerstand zu hoch.
- Engine startet verzögert oder überhaupt nicht (Anlasser-Spannung fällt unter 10.5V).

**Diagnose:**
1. Multimeter am Batterie-Pol messen (DC 20V-Bereich), dann am Anlasser-Eingang (Langkabel).
2. Differenz > 0.5V = Kontakt-Problem.
3. Kabel-Schuh öffnen (ggfs. abklemmen), Kontakt-Fläche mit Lupe inspizieren.

**Behandlung:**
1. Batterie-Pol abklemmen (Minus zuerst, dann Plus).
2. Mit Stahlbürste & Essig grünspan abbürsten (nicht Sand, Kratzt zu tief).
3. Kontakt-Fläche mit fusselfreiem Tuch trocknen.
4. CRC 6-66 dünn auftragen (nicht öl-getränkt).
5. Neue Kabelschuh crimpen (oder alte, wenn noch gut, wieder anpressen mit 10 Nm Drehmoment).
6. Batterie wiederanschließen (Plus zuerst, dann Minus), Spannungsprobe wiederholen.

**Wiederholungsquote:** Ohne Schutz-Behandlung 6–12 Monate später erneut.

**Prävention:** CRC 6-66 monatlich auftragen, 0.5 mm Vaseline-Schicht über Pol überziehen.

### 6.2 NMEA 2000 Micro-C Stecker-Fehler (CAN-Bus Interrupt)

**Ursache:** Salzluft-Eindringung in Stecker-Höhlung trotz Schutzkappen (Diffusion über Dichtung), Kontakt-Oxidation, Micro-C-Design begrenzt IP67-Beständigkeit.

**Symptome:**
- Chart-Plotter zeigt "NMEA 2000 Netzwerk-Fehler" oder einzelne Geräte fallen aus.
- Engine-Daten (Drehzahl, Temperatur) verschwinden intermittierend.
- Fehler tritt nach Regensturm oder Salzwasser-Spray auf.

**Diagnose:**
1. Alle Micro-C-Stecker visuell überprüfen (Lupe, LED-Lampe): Grünspan, Verfärbung innen?
2. NMEA 2000 Netzwerk-Testgerät anschließen (z.B. Actisense NGT-1): CAN-Bus-Spannung messen (sollte 2.5V, Differentialspannung ±0.5V).
3. Störgeräte-Stecker einzeln abziehen, testen, ob Fehler persistiert.
4. Betroffenen Stecker mit DeoxIT D5 reinigen (siehe Abschnitt 4.2).

**Behandlung:**
- Leichte Oxidation: DeoxIT D5 + Kuppel-Entkuppel-Zyklen (10x).
- Schwere Oxidation oder Trockenheit: Stecker-Modul tauschen (OEM Teil, ca. 50–100 EUR).
- Nach Reparatur: Schutzkappen ständig anlassen, Stecker-Verbindung unter Dach lagern, nicht im Freien über Nacht stehen lassen (Taubildung).

**Wiederholungsquote:** Mit Korrektur <5 % in 2 Jahren; ohne Schutz-Behandlung 20–30 %.

### 6.3 Wechselrichter-Fehler (Elkos geschwollen oder Sicherung geplatzt)

**Ursache:** Langzeitlagerung bei Hitze (Sonne auf Gerätekasten), Überlast, oder Fertigungsdefekt Kondensator.

**Symptome:**
- Wechselrichter schaltet sich nach 30 Sekunden ab oder zeigt "Over Temperature" ständig.
- Brummgeräusch oder Pfeif-Ton aus Gerät (Indikatoren defekter Elkos oder PWM-Instabilität).
- Ausgangsspannung schwankend (z.B. 220–250V in 5-Sekunden-Zyklen).

**Diagnose:**
1. Gehäusetemperatur messen (IR-Kamera): >70 °C im Leerlauf = abnormal.
2. Innenraum-Inspektion (sofern Garantie abgelaufen): Kondensatoren auf Schwellung oder Flüssigkeits-Auslauf prüfen.
3. Stromaufnahme unter Last messen (50 % Nennlast): aktuelle Aufnahme vs. Datenblatt vergleichen (>10 % Abweichung = verdächtig).

**Behandlung:**
- Leichte Überhitzung: Gerät an kühlerer Stelle montieren (z.B. Unterdeck statt Sonnen-exponiert), Kühlungs-Ventilatoren-Einlass überprüfen (Staub-Verstopfung?).
- Geschwollene Elkos: Fachmann-Reparatur (Risiko Kurzschluß).
- Sicherung geplatzt: Sicherungs-Typ checken (z.B. 250A @ 48V), auf Original-Amperage tauschen (nicht höher!), neue Sicherung einsetzen. Falls Sicherung gleich wieder durchbrennt → Kurzschluß-Diagnose notwendig.

**Wiederholungsquote:** Mit Montage-Korrektur <5 % in 5 Jahren; ohne Lüftung 30 % in 3 Jahren.

### 6.4 Batterie-Balancer-Fehler (LiFePO₄ Zellen unausgewogen)

**Ursache:** BMS (Battery Management System) Balancer-Schaltung ist fehlerhaft oder Zelle hat Kapazitäts-Ungleichgewicht (Fertigungstoleranz bis ±10 %).

**Symptome:**
- Batterie lädt nur bis 90 % Kapazität, obwohl Laderegler ausgebaut ist.
- Automatische Abschaltung bei 3.5V pro Zelle (zu früh) während Entladung.
- Eine Zelle deutlich heißer als andere (Thermal-Imager zeigt >45 °C vs. 35 °C).

> ⚠️ **ZU PRÜFEN (Audit):** "Abschaltung bei 3.5V pro Zelle … während Entladung" ist für LiFePO₄ physikalisch widersprüchlich — nominal 3.2V, Ladeschluss ~3.65V, Entladeschluss ~2.5V (BMS-Unterspannung typ. 2.5–2.8V/Zelle). 3.5V liegt im oberen **Lade**bereich, nicht bei Entladung, und passt zum ersten Symptom ("lädt nur bis 90 %" = vorzeitiger **Lade**abbruch). Vermutlich ist "Ladung" statt "Entladung" gemeint (Wert 3.5V dann plausibel) ODER der Entlade-Wert müsste ~2.5V lauten. Richtung nicht zweifelsfrei — vor Nutzung verifizieren. (Auch die "ca. 3.0V nominal" unten ist für LiFePO₄ zu niedrig; korrekt sind 3.2V/Zelle → 16S ≈ 51,2V nominal für ein "48V"-Pack.)

**Diagnose:**
1. Zell-Spannungen messen (Multimeter, je 48V Batterie = 16 Zellen à ca. 3.0V nominal): alle müssen ±0.1V gleich sein.
2. BMS-Balancer-Funktion überprüfen (Handbuch des BMS-Herstellers, z.B. Victron Lithium BMS): sollte aktiv bei >3.0V/Zelle bilanzieren.
3. Lade-/Entlade-Temperatur: sollte alle <40 °C sein; eine Zelle >50 °C = interner Fehler in Zelle.

**Behandlung:**
- Mild: BMS-Firmware zurücksetzen (Batterie 30 sec. von allen Verbrauchern isolieren) und erneut einschalten.
- Balancer-Fehler: BMS-Elektronik austauschen (ca. 200–400 EUR je nach Hersteller).
- Zellen-Defekt: gesamte Batterie-Serie austauschen (Zelle nicht einzeln tauschbar bei Blöcken >12V).

**Prävention:** Monatlich Zell-Balancer aktiv prüfen (BMS-Datenbus auslesen), Lade-Stromstärke auf 0.3C begrenzen (z.B. 100 Ah Batterie → max. 30A Ladestrom).

### 6.5 Autopilot-Kompass-Drift (Heading-Fehler +5...+30°)

**Ursache:** Kompass-Kalibrierung veraltet (Luftfahrt-Varianten-Änderung, neue metallische Strukturen an Bord), oder Kompass-Sensor hat Sensor-Drift durch Alterung.

**Symptome:**
- Autopilot hält Kurs nach 1–2 Stunden mit systematischem Fehler: z.B. sollte 090° fahren, fährt 105°.
- Auf Wende scheint Fehler zu verschwinden, tritt aber auf Gegenkurs wieder auf.
- Handheld-GPS zeigt Kurs korrekt, Autopilot-Anzeige aber falsch.

**Diagnose:**
1. Handwarm-Test (sonnig, klares Wasser): Autopilot Kompass-Anzeige vs. GPS-Heading-Daten vergleichen (live auf Chart-Plotter).
2. Kompass-Kalibrierungs-Alter prüfen (Handbuch oder Service-Eintrag): älter als 5 Jahre?
3. Neue magnetische Gegenstände (Batterien-Bank-Erweiterung, neue Ankerwinde) in Nähe Kompass addiert? Abstände prüfen (sollte mindestens 2m Clearance).

**Behandlung:**
1. Kalibrierungs-Routine ausführen (Handbuch des Autopilot-Herstellers, z.B. Raymarine Evolution, Garmin):
   - Boot im flachen Wasser positionieren (keine Magnetismus-Störquellen).
   - Autopilot in "Kompass-Kalibrierungs-Modus" schalten.
   - 3–4 volle Umdrehungen (360°) fahren mit konstant niedrigem Kurs, Autopilot protokolliert Kompass-Werte.
   - Nach Fertigstellung Kalibrierungs-Daten speichern.
2. Nach Kalibrierung: Verifikation mit handheld Kompass + GPS durchführen.

**Wiederholungsquote:** Neukalibrierung alle 2–3 Jahre empfohlen.

### 6.6 Seewasser-Korrosion in Antriebssensoren (Drehzahl-Geber, Temperatur-Sensor)

**Ursache:** Thru-Hull-Sensoren (z.B. Kühlwasser-Temperatur, Propeller-Drehzahl-Geber) sind Direct-immersed, Edelstahl-gehäuse kann bei schlechter Isolations-Wartung korrodieren.

**Symptome:**
- Engine-Drehzahl-Anzeige flackert oder zeigt konstant 0 RPM (aber Motor läuft).
- Kühlwasser-Temperatur-Anzeige springt wild (z.B. 40 °C ↔ 80 °C in Sekunden).
- Fehler-Code "Engine Temperatur-Sensor Fehler" im Plotter.

**Diagnose:**
1. Sensor-Kabel-Durchgang überprüfen (Widerstand nach Sensor-Kabel-Ende, nicht das Kabel selber): sollte <10 Ω sein.
2. Sensor-Gehäuse sichtprüfen: Rostflecken, Sulfation, Beschädigungen?
3. Spannungsprobe auf Sensor-Ausgang (Engine läuft): sollte 0.5–4.5V sein (je nach Temperatur/Drehzahl, Sensor-Typ prüfen).

**Behandlung:**
- Milde Korrosion: Sensor ausbauen (meist Gewindebohrung), mit CRC 6-66 & Stahlbürste reinigen, mit PTFE-Tape neu einbauen (Gewinde-Dichtung).
- Schwere Korrosion oder Signalverlust: Sensor-Kartuschenmodul tauschen (OEM-Teil, ~50–150 EUR je nach Motor-Typ).
- Nach Tausch: Sensor-Kabel überprüfen (Isolation, Durchgang erneut messen).

**Prävention:** Thru-Hull Sensor-Bohrungen saisonal überprüfen (vor Winter mit Langzeit-Konservierung mit Tef-Gel ausfüllen, nicht nur Salzwasser).

### 6.7 Landstrom-Kupplung Kontakt-Verschleißß (230V Plug, Intermittente Stromversorgung)

**Ursache:** Wiederholter Plug-Plug-Prozess bei Hafenliegering, Kontakt-Verschleiß (Gold-Plattierung abgerieben), Oxidation unter Kontakt-Flächen.

**Symptome:**
- Nach Landstrom-Anschluß im Hafen: FI-Schutzschalter schlägt sofort aus (RCD-Fehler).
- Oder: 230V Spannungsversorgung intermittierend (Geräte schalten sich aus & wieder an alle 10 sec).
- Thermisches Rauschen/Brummen aus Landstrom-Interface-Box.

**Diagnose:**
1. Landstrom-Plug-Kontakte sichtprüfen (Lupe): Verfärbung (schwarz = Oxidation), abgelöste Gold-Plattierung, rauhe Oberflächen.
2. Spannungsprüfung bei eingestecktem Plug: sollte stabil 230V ±10V sein, keine Schwankungen.
3. Isolations-Widerstand-Test (Megger 500V DC): Phase-zu-Erde sollte >1 MΩ sein; <500 kΩ zeigt Isolations-Fehler hin (Wasser in Plug oder Buchse).

**Behandlung:**
1. Kontakte-Reinigung: Plug ausziehen, mit fusselfreiem Tuch + Essig die Kontakt-Flächen leicht abwischen (nicht aggressive Bürste, zu viel Verschleiß).
2. Schutzmittel: CRC WD-40 Marine (minimal, nicht öl-getränkt) auf Außenseite auftragen, Trocknung abwarten.
3. Beschädigte Goldplattierung: Plug-Modul tauschen (ca. 50–150 EUR je nach Amperage & Stecker-Typ).
4. Isolations-Fehler: Gesamte Kabel-Einheit ersetzen (Sicherheitsrisiko, Leckstrom möglich).

**Prävention:** Nach Landstrom-Nutzung Plug mit Schutzkappen versehen (reduziert Feuchte-Eindringung um 50 %).

### 6.8 Batterie-Spannungs-Regelungs-Fehler (Laderegler schlägt nicht an)

**Ursache:** Laderegler-Firmware altert, oder Spannungs-Regelkreis hat Hysterese-Problem (unterschiedliche Schwellenwerte beim Laden vs. Entladen).

**Symptome:**
- Batterie wird nicht geladen, obwohl Motor läuft (Laderegler-LED zeigt kein Laden-Signal).
- Oder: Laderegler lädt permanent, auch wenn Batterie voll ist (U_Batt > 14.5V).
- Batterie-Spannungs-Schwingungen (z.B. 13.0V → 13.2V → 13.0V @ 1 Hz).

**Diagnose:**
1. Batterie-Spannungen-Profil unter Last aufzeichnen (Engine 1000 RPM, alle Verbraucher an): sollte 13.8–14.5V stabil sein.
2. Laderegler-Ausgang überprüfen (vor und nach Sicherung): sollte bei Vollladung >14.0V sein.
3. Temperatur-Sensor Laderegler (falls vorhanden): Kabel & Sensor-Kalibrierung überprüfen (Service-Handbuch).

**Behandlung:**
- Firmware-Update: Hersteller kontaktieren (z.B. Victron SmartSolar App), verfügbare Updates einspielen.
- Hysterese-Korrektur: einige Regler haben Konfigurierungs-Soft-Schalter → Datenblatt prüfen.
- Hardware-Fehler (z.B. defektes Spannungs-Regelungs-IC): Laderegler-Modul austauschen (ca. 150–400 EUR je nach Amperage).

**Prävention:** Laderegler-Firmware 2x jährlich prüfen, in Betrieb-Log notieren.

### 6.9 CAN-Bus Terminator-Fehler (Netzwerk-Übertragungsfehler)

**Ursache:** CAN-Bus verlangt 120-Ω Widerstände am Anfang & Ende der Buskette; fehlende oder fehlerhafte Terminatoren verursachen Reflexionen und Datenverluste.

**Symptome:**
- NMEA 2000 oder CAN-Netzwerk zeigt intermittierende Fehler: einzelne Geräte fallen 5–10 Sekunden aus, dann sind sie wieder da.
- Fehler-Code "CAN-Bus Error" im Master-Gerät (Chart-Plotter).
- Bei Hochtemperatur (>35 °C Maschinenraum) verschärfen sich Fehler (CAN-Toleranzen schrumpfen bei Temperatur).

**Diagnose:**
1. CAN-Bus-Impedanz messen (mit Funktions-Signalanalysator oder Terminator-Test-Gerät): sollte 60 Ω sein (120 Ω Widerstände parallel = 60 Ω).
2. Wenn Impedanz >100 Ω oder <30 Ω: fehlender/falscher Terminator.
3. Visuelle Inspektion aller CAN-Stecker (T-Pieces, Abschluß-Widerstände): richtig verkabelt?

**Behandlung:**
1. Terminator-Widerstände überprüfen: sollten am letzten Gerät der Buskette angebracht sein (120 Ω, 0.25W Mindest-Leistung).
2. Falls fehlend: Terminator-Widerstand-Block in den letzten Stecker einfügen (ca. 10–30 EUR).
3. Nach Korrektur: Netzwerk-Fehler-Zähler im Chart-Plotter zurücksetzen, mehrere Stunden Betrieb testen.

**Prävention:** Bei Netzwerk-Erweiterung (neuer Sensor hinzufügen) immer Terminator-Topologie überprüfen.

### 6.10 Sicherungs-Dauerbrand (Stromkreis kurz, aber nicht sofort)

**Ursache:** Lagering-Korrosion in langem Kabeltrakt oder Isolations-Risse durch Vibrationen; Kurzschluß-Widerstand ist hoch genug, daß Sicherung nicht sofort schmilzt, aber Dauerbelastung führt zur Überhitzung.

**Symptome:**
- Sicherung ist dunkelbraun/schwarz verfärbt, aber nicht regelrecht "aufgesprungen".
- Sicherung ist heiß anzufassen (>60 °C).
- Stromkreis funktioniert noch, aber Geräte im Kreis werden ungewöhnlich heiß.

**Diagnose:**
1. Sicherungs-Temperatur messen (IR-Kamera oder Finger-Test nach Abschalten): >50 °C abnormal.
2. Stromaufnahme unter Last messen: sollte <80 % Sicherungs-Nennstrom sein; >90 % zeigt Überlast oder Kontakt-Widerstand.
3. Kabel-Isolations-Widerstand messen (Megger 500V DC): sollte >1 MΩ sein; <100 kΩ zeigt Isolation-Leck.

**Behandlung:**
1. Sicherung tauschen (neuer Typ, gleiche Amperage).
2. Kabel-Trakt überprüfen: visuelle Inspektion auf Risse, Beschädigungen, Quetschungen.
3. Verdächtige Kabel-Abschnitte: Isolations-Schicht erneuern (Shrink-Schlauch überziehen) oder Kabel komplett tauschen.
4. Verbraucher im Stromkreis prüfen: Kurzschluß in Gerät? Spannungsprobe auf Ein-/Ausgang durchführen.

**Prävention:** Sicherungs-Temperatur während jährlichem Service-Check prüfen (IR-Kamera).

### 6.11 Autopilot-Steuermotor-Verschleiß (Lenkdruck ständig aktiv)

**Ursache:** Hydraulischer Steuermotor (Rendez-vous Pumpe) oder elektrischer Stepper-Motor hat Lagering-Verschleiß; Steuerventil kann Druck nicht halten (Lecks).

**Symptome:**
- Autopilot muss Lenkdruck ständig halten (Motor läuft permanent, auch im Geradeaus-Kurs).
- Steuerrad "kämpft" gegen Autopilot-Traktion (hoher Gegendruck).
- Steuermotor ist heißer als normal (>50 °C).

**Diagnose:**
1. Hydraulic-Druck-Test (falls verfügbar, Service-Gerät): Druck sollte nur bei Richtungsänderung aktiv sein, sonst <10 bar. Ständig >20 bar abnormal.
2. Steuermotor-Stromaufnahme messen (Ampere-Zange): sollte <2A sein im Geradeaus-Kurs; >5A zeigt Überlast.
3. Leck-Inspektion: Hydraulisch-Öl unter Steuermotor oder am Ventil-Block?

**Behandlung:**
- Milde Verschleiß: Steuerventil-Kalibrierung (proprietary, Hersteller-Service nötig).
- Leck identifiziert: Steuermotor-Dichtringe tauschen oder Motor komplett austauschen (ca. 500–1500 EUR je nach Typ).
- Stepper-Motor (elektrische Variante): Motor-Getriebe überprüfen (Spielfreiheit), ggfs. Zahnrad tauschen.

**Prävention:** Monatliche Sichtprüfung auf Öl-Lecks.

### 6.12 GFK-Delaminierung an Antennenmast (Radarantennen-Halter)

**Ursache:** UV-Strahlung und Feuchte-Eindringung führen zur Delamination der Schichten (Gelcoat löst sich von GFK-Struktur).

**Symptome:**
- Sichtbare Blasen oder Wölbungen im Gelcoat um Mast-Basis.
- Bei Druck mit Finger gibt Material nach (Hohlraum darunter).
- Wasser tritt bei Regen aus Delamination-Rissen aus.

**Diagnose:**
1. Tap-Test (Klopfen mit Holzhammer auf verdächtige Stelle): Delamination klingt hohl (↓ Höhenlage des Tones), intaktes GFK dumpf.
2. Tiefe der Delaminierung: Bohrung in Rand-Bereich (nicht tragendes GFK), Prüfstab einschieben.

**Behandlung:**
- Lokal, <10 cm²: Delaminierung aussägen, mit Epoxy-Harz + Glasfaser-Tape neu laminieren (DIY möglich, ca. 50 EUR Material).
- Großflächig, >30 cm² oder strukturell kritisch (Radarantenne-Halter): Professionelle Reparatur (Kosten 500–2000 EUR je nach Größe).

**Prävention:** Jährliche UV-Protection: Gelcoat-Versiegelung mit UV-Block (z.B. CRC Light-Protective Lacquer).

---

## 7. Troubleshooting-Entscheidungsbäume

### 7.1 Entscheidungsbaum: KEIN SIGNAL VON GPS / GNSS-EMPFÄNGER

**Symptom:** GPS-Icon in Kartenplotter blinkend oder grau. Keine Positions-Anzeige. Kurs und Geschwindigkeit nicht verfügbar.

**Schritt 1: Sicht zum Himmel überprüfen**
- Befindest Du Dich unter einer Brücke, in einer Bucht mit steilen Felswänden, oder unter dichten Bäumen (falls Fluss/See)?
  - **Ja** → Fahre zur offenen Wasserfläche, warte 2 Minuten. Wenn Signal zurückkommt: nicht das Gerät, sondern Umgebung schuld. Ende.
  - **Nein** → Weiter zu Schritt 2.

**Schritt 2: Antenne sichtprüfen (Außenbord)**
- Ist die GPS-Antenne sichtbar, sauber, und nicht beschädigt (keine Risse, Kratzer)?
  - **Nein, Antenne verschmutzt/bedeckt** → Antenne mit Süßwasser spülen, trocknen. Kabel-Anschlüsse überprüfen (Trocknungszeit: 15 min). Weiter Schritt 3.
  - **Nein, Antenne beschädigt** → Antenne austauschen (ca. 80–200 EUR je nach Typ). Kalibrierung nach Austausch nötig (siehe Abschnitt 4.5).
  - **Ja, sauber** → Weiter Schritt 3.

**Schritt 3: Stromversorgung überprüfen**
- Ist die Elektronik-Panel beleuchtet? Schaltet sich ein?
  - **Nein** → Batterie leer oder Sicherung defekt. Batterie laden oder Sicherung überprüfen (Abschnitt 3.2). Danach zurück Schritt 1.
  - **Ja** → Weiter Schritt 4.

**Schritt 4: NMEA-Kabel überprüfen (Antenne zur Elektronik)**
- Kabel von Antenne zum Plotter sichtprüfen: Risse, Knickstellen, Wasser-Eindringung?
  - **Ja, Kabel beschädigt** → Kabel austauschen (ca. 30–150 EUR je nach Länge). Weiter Schritt 5.
  - **Nein, Kabel ok** → Stecker-Verbindungen überprüfen (beide Enden).

**Schritt 5: Stecker-Verbindungen überprüfen**
- Antennenstecker an Antenne: lockig und trocken?
- Plotter-Stecker-Port: Sichtprüfung auf Korrosion (grüne/weiße Flecken)?
  - **Ja, Korrosion sichtbar** → Mit Bürste sanft reinigen, dann WD-40 sprühen (5 min einwirken), trocken wischen. Stecker trocken anschließen. Weiter Schritt 6.
  - **Nein, sauber** → Stecker kräftig herausziehen und wieder einstecken (3x). Weiter Schritt 6.

**Schritt 6: Elektronik neu starten (Soft-Reset)**
- Netzschalter am Plotter für 10 Sekunden ausschalten, dann wieder einschalten.
- Warte 3 Minuten auf GPS-Akquisition (grünes Licht oder GPS-Status).
  - **Signal zurück** → Problem gelöst. Dokumentieren (Abschnitt 8.1 Wartungsprotokoll).
  - **Immer noch kein Signal** → Weiter Schritt 7.

**Schritt 7: GPS-Modul oder Plotter defekt?**
- Verbinde Antenne ggfs. mit einem anderen Plotter (falls vorhanden).
  - **Signal auf anderem Gerät** → GPS-Modul im ersten Plotter defekt. Modul austauschen oder Plotter zur Reparatur geben (ca. 200–600 EUR).
  - **Auch auf anderem Gerät kein Signal** → Antenne defekt (zurück zu Schritt 2) oder Antenne-Kabel dauerhaft unterbrochen. Kabel-Prüfung mit Multimeter (Durchgang prüfen, siehe Abschnitt 3.3).

**Schritt 8: Professionelle Diagnose**
- Wenn nach Schritt 7 immer noch ungelöst: Elektronik-Werkstatt aufsuchen. Speichere alle Fehlermeldungen auf Foto.

---

### 7.2 Entscheidungsbaum: DISPLAY DUNKEL ODER NICHT SICHTBAR

**Symptom:** Bildschirm ist schwarz, bleibt dunkel, oder Bild-Qualität sehr schlecht. Kein Licht, kein Ton, keine Reaktion auf Tasten.

**Schritt 1: Ist das Gerät überhaupt an?**
- Power-LED an der Elektronik leuchtet? Oder höre ich Ventilator-Geräusch?
  - **Nein** → Sicherung überprüfen (Abschnitt 3.2). Batterie-Spannungsprüfung (siehe Schritt 2).
  - **Ja, LED leuchtet** → Weiter Schritt 3.

**Schritt 2: Batterie überprüfen**
- Multimeter auf Gleichspannung (DC) stellen. Batterie-Klemmen messen.
- Sollwert: 12V (Ladestand: 11.5–12.5V normal) oder 24V (je nach System).
  - **Messwert <10V oder 0V** → Batterie zu schwach, lademodus aktivieren (siehe Abschnitt 3.2). Oder Sicherung in Batterie-Leitungsschalter defekt.
  - **Messwert ok** → Weiter Schritt 3.

**Schritt 3: Stromkabel zum Bildschirm überprüfen**
- Stromkabel (rot/schwarz Leitungen) vom Panel zum Display sichtprüfen: Verschleiß, Feuchtigkeit, Knickstellen?
- Stecker-Verbindungen nach Korrosion kontrollieren.
  - **Ja, Kabel beschädigt oder Stecker korrodiert** → Kabel oder Stecker reinigen/austauschen (siehe Schritt 5).
  - **Nein, alles sauber** → Weiter Schritt 4.

**Schritt 4: Display-Helligkeit und Kontrast**
- Bei eingeschaltetem Plotter: Gibt es eine Taste oder Software-Menü für "Helligkeit" oder "Brightness"?
  - **Ja, Menü vorhanden** → Helligkeit auf Maximum stellen. Warte 10 Sekunden auf Bildaufbau.
  - **Nein** → Weiter Schritt 5.

**Schritt 5: Anschluss-Test (Stecker neu anstecken)**
- Display-Stromkabel 5 Sekunden herausziehen.
- Beide Enden des Kabels auf Korrosion/Wasser untersuchen (weißer oder grüner Belag).
  - **Ja, Korrosion** → Mit feiner Bürste sanft reinigen, WD-40 aufsprühen, trocknen, stecken wieder an.
  - **Nein** → Kabel fest wieder einstecken (sollte hörbar "klicken").
- Schalter ein/aus 3x betätigen.
  - **Display jetzt an** → Problem gelöst, Wartungsprotokoll aktualisieren.
  - **Display bleibt dunkel** → Weiter Schritt 6.

**Schritt 6: Back-Light (LED-Leuchte) möglicherweise defekt**
- Wenn Du das Bild nur ganz dunkel erkennst (bei sehr genauesem Hinschauen sichtbar), ist wahrscheinlich nur die Back-Light-LED defekt, nicht das Display.
- Back-Light-Austausch oder Display-Wechsel (ca. 150–500 EUR je nach Modell).

**Schritt 7: Professionelle Reparatur nötig**
- Wenn Display bleibt dunkel, trotz aller Checks: Wahrscheinlich Mainboard-Fehler oder Netzteil-Ausfall.
- Reparaturwerkstatt oder Hersteller-Service aufsuchen. Kosten: ca. 200–800 EUR.

---

### 7.3 Entscheidungsbaum: NMEA-FEHLER (DATEN VON INSTRUMENTEN NICHT ERREICHBAR)

**Symptom:** Fehler "NMEA bus error" oder "Instrument Offline" im Plotter. Radar, Kompass, Windsensor zeigen keine Daten.

**Schritt 1: Welches Instrument ist betroffen?**
- Ist es ein einzelnes Gerät (z.B. nur Radar offline) oder mehrere Instrumente?
  - **Einzelnes Gerät** → Weiter Schritt 3 (Gerät-spezifisches Kabel).
  - **Mehrere Geräte** → Wahrscheinlich NMEA-Bus-Fehler. Weiter Schritt 2.

**Schritt 2: NMEA-Bus-Kabel überprüfen (T-Stück oder Daisy-Chain)**
- Hauptkabel von Plotter zu Instrumenten-Netzwerk sichtprüfen.
- Alle Stecker in der Kette fest angeschlossen?
  - **Nein, loser Stecker** → Fest anstecken. Warte 30 Sekunden.
  - **Ja, alle dicht** → Kabel auf Beschädigungen überprüfen (Risse, Feuchtigkeit).
- Alle Geräte wieder online?
  - **Ja** → Problem gelöst.
  - **Nein** → Weiter Schritt 2a.

**Schritt 2a: Terminator-Widerstand überprüfen**
- NMEA-Netzwerke (besonders NMEA 2000) benötigen einen 120-Ω-Terminator-Widerstand am Ende der Kette.
- Letztes Gerät in der Kette: Ist dort ein Terminator-Stecker angebracht (kleine schwarze oder rote Kappe)?
  - **Nein** → Terminator-Stecker anbringen (ca. 20 EUR, bei Elektronik-Zubehör erhältlich). Alle Geräte sollten sofort wieder online sein.
  - **Ja, Terminator vorhanden** → Weiter Schritt 2b.

**Schritt 2b: NMEA-Baudrate überprüfen**
- In der Plotter-Software: Kommunikations-Einstellungen → NMEA-Port → Baudrate.
- Standard: 4800 bps (älter) oder 38.400 bps (neuere Geräte). NMEA 2000: 250 kbps.
  - Falls Baudrate falsch eingestellt → Auf Standard-Wert zurücksetzen. Geräte neu starten.

**Schritt 3: Gerät-spezifisches Kabel überprüfen (Radar, Kompass, etc.)**
- Stromkabel und Daten-Kabel vom Plotter zum Instrument sichtprüfen.
- Stecker beide Seiten: Korrosion, lockige Verbindung?
  - **Ja, Fehler sichtbar** → Stecker reinigen (WD-40) oder Kabel austauschen.
  - **Nein** → Weiter Schritt 4.

**Schritt 4: Instrument neu starten**
- Stromschalter am Instrument für 10 Sekunden ausschalten.
- Wieder einschalten, warte 30 Sekunden auf Initialisierung.
  - **Gerät online** → Problem gelöst.
  - **Weiterhin offline** → Weiter Schritt 5.

**Schritt 5: Gerät-Adresse / Slave-ID überprüfen**
- In NMEA 2000 Systemen hat jedes Gerät eine eindeutige Adresse.
- Plotter-Software: Alle erkannten Geräte anzeigen, unbekannte oder doppelte Adressen entfernen.
- Im Menü "NMEA Setup" oder "Device Manager" alle Instrumente re-konfigurieren.
  - Nach Neustart sollten alle Geräte wieder kommunizieren.

**Schritt 6: T-Stück oder Hub defekt?**
- Falls mehrere Geräte betroffen, aber Kabel alle ok: NMEA-Hub oder T-Stück möglicherweise defekt.
- Hub austauschen (ca. 50–150 EUR je nach Typ).

**Schritt 7: Professionelle Diagnose**
- Wenn nach allen Schritten noch Fehler: Wahrscheinlich Transceiver-Modul im Plotter oder Gerät defekt.
- Werkstatt aufsuchen.

---

### 7.4 Entscheidungsbaum: RADAR-ARTEFAKTE (FALSCHE ZIELE, NEBELFLECKEN, GEISTER-BILDER)

**Symptom:** Radar zeigt Ziele, die nicht existieren. Rauschen oder Nebelflecken. Echte Schiffe verschwinden und erscheinen wieder.

**Schritt 1: Ist das Radar in Betrieb?**
- Dreht sich die Antenne sichtbar auf dem Mast?
- Hörst Du Surr-Geräusch der Rotations-Motor?
  - **Nein** → Radar möglicherweise in Standby. In Plotter-Software: Radar einschalten, Betriebsmodus auf "Transmit" oder "Active" stellen.
  - **Ja, Radar läuft** → Weiter Schritt 2.

**Schritt 2: Radarschirm sauber?**
- Auf Antenne unten am Mast: Sind Algen, Eis, oder Salzbelag vorhanden?
  - **Ja, Schmutz sichtbar** → Mit Süßwasser spülen, mit weichem Tuch trocknen. Dabei Antenne nicht direkt berühren (Beschädigungsgefahr). Nach Reinigung: Radar neu starten.
    - Artefakte weg? → Problem gelöst.
    - Artefakte bleiben? → Weiter Schritt 3.
  - **Nein, sauber** → Weiter Schritt 3.

**Schritt 3: Radarfrequenz überprüfen (für Küstengewässer optimieren)**
- Radar in Küstenzone (Häfen, flache Gewässer) zeigt oft Geister-Bilder wegen Reflexionen von Landmassen.
- In Plotter-Software: Radar-Einstellungen → Fern-Einstellung (Range).
  - Reduziere die Radarreichweite: von z.B. 24 nm auf 8 nm. Schau, ob Artefakte verschwinden.
  - Wenn Verringerung hilft: Offene Gewässer fahren, wieder auf höhere Reichweite wechseln.
  - Wenn immer noch Artefakte: Weiter Schritt 4.

**Schritt 4: Radar-Polarität umschalten (wenn Optionen vorhanden)**
- Einige Radare unterstützen Horizontal (HH) und Vertikal (VV) Polarisierung.
- Versuche, die Polarität zu wechseln (in Softwaremenü oder physischer Schalter am Radarmodul).
  - Bessere Bilder? → Neue Polarität als Standard speichern.
  - Gleichbleibend schlecht? → Weiter Schritt 5.

**Schritt 5: Stromversorgung und Thermisches Rauschen überprüfen**
- Ist das Radarmodul heiß (Handfläche haltbar)?
  - **Ja, sehr heiß** → Lüfter-Öffnung auf dem Radar-Gehäuse prüfen: verschmutzt oder blockiert?
    - Staub entfernen, ggfs. Lüfter überprüfen. Hitze führt zu elektronischen Fehlern und Rauschen.
  - **Nein** → Spannungsversorgung überprüfen (sollte 11–14V bei 12V-System sein).

**Schritt 6: Andere elektronische Geräte Interferenz?**
- Hast Du gerade andere Funk-Geräte aktiv? VHF-Funk, Bordnetz-Inverter, oder High-Power-Sounder?
  - **Ja** → Diese ausschalten, Radar neu starten. Wenn Artefakte weg: Elektromagnetische Interferenz (EMI). Abstand zwischen Geräten vergrößern (Kabelrouting überprüfen, siehe Abschnitt 5.3).
  - **Nein** → Weiter Schritt 7.

**Schritt 7: Radarmodul defekt?**
- Wenn Artefakte dauerhaft bleiben trotz aller Kalibrierungen: Radarmodul wahrscheinlich defekt.
- Modul austauschen (ca. 1500–5000 EUR je nach Typ, meist Hersteller-Service erforderlich).

---

### 7.5 Entscheidungsbaum: SOFTWARE-CRASH (BILDSCHIRM FRIERT EIN, SYSTEM BOOTET NEU)

**Symptom:** Plotter antwortet nicht mehr auf Bedienung. Bildschirm friert ein oder wird schwarz. System startet unerwartet neu.

**Schritt 1: Ist es nur ein Freeze oder ein Crash mit Neustart?**
- Versuche, eine Taste zu drücken oder auf dem Touchscreen zu tippen.
  - **Gerät reagiert** → Nur Freeze. Weiter Schritt 2a.
  - **Keine Reaktion, Bildschirm schwarz, System startet von vorne** → Crash/Reboot. Weiter Schritt 2b.

**Schritt 2a: Gefrorenes System (Freeze)**
- Versuche, Hard-Reset (lange Taste halten, 10–15 Sekunden) oder Netzschalter aus/an.
  - System antwortet wieder? → Problem war Software-Glitch. Dokumentieren. Wenn es häufig wiederholt: Weiter Schritt 4.
  - System bleibt friert? → Weiter Schritt 3.

**Schritt 2b: Automatischer Neustart (Crash)**
- Dies deutet auf Stromversorgung oder Software-Fehler hin.
- Warte, bis System vollständig hochgefahren ist (ca. 3–5 Minuten).
  - Danach normal? → Software-Bug. Weiter Schritt 4.
  - Sofort wieder Crash? → Wahrscheinlich Hardware (Speicher, Netzteil). Weiter Schritt 3.

**Schritt 3: Hardware-Fehler ausschließen**
- Stromversorgung überprüfen: Multimeter auf Spannungsprüfung.
  - Sollte konstant 12V oder 24V sein ohne Fluktuationen.
  - Fluktuierende Spannung? (z.B. springt zwischen 11V und 13V): Netzteil-Problem, Batterie schwach, oder korrodierte Kontakte. Siehe Abschnitt 3.2.
- Wärmestau überprüfen: Ist der Plotter in der Elektronik-Box heiß?
  - Zu heiß? → Lüftung überprüfen, ggfs. Elektronik aus direkter Sonneneinstrahlung schützen.
  - Temperatur ok? → Weiter Schritt 4.

**Schritt 4: Software-Update überprüfen**
- Hersteller-Website: Gibt es ein neueres Firmware-Update für den Plotter?
  - **Ja, Update verfügbar** → Update herunterladen (USB-Stick oder Wireless), im Plotter installieren. Nach Update: Testen, ob Crashes weiterhin auftreten.
  - **Nein, bereits aktuell** → Weiter Schritt 5.

**Schritt 5: Speicher / Datenspeicher-Fehler überprüfen**
- Wenn verfügbar: Plotter-Menü → System → Storage oder Memory Diagnostics.
- Vollständigen Speicher-Test durchführen.
  - **Fehler gefunden** → Speicher möglicherweise beschädigt. Hersteller-Service oder Austausch erforderlich.
  - **Keine Fehler** → Weiter Schritt 6.

**Schritt 6: Häufig angeforderte Maps / Anwendungen deaktivieren**
- Wenn der Plotter viele Karten oder Zusatzanwendungen lädt: Diese können zu Crashes führen.
- Karten-Menü: Große oder selten verwendete Karten deaktivieren oder löschen (speichert RAM).
- Neustart, Probleme weg? → Problem war Speichermangel. Zukünftig selektiver laden.

**Schritt 7: Werks-Reset als letztes Mittel**
- Wenn nichts hilft: Plotter auf Werkseinstellungen zurücksetzen (siehe Handbuch).
- **Warnung:** Alle persönlichen Daten, Routen, Lesezeichen gehen verloren. Davor alles sichern.
- Nach Reset: System sollte stabil sein. Einzelne Einstellungen und Karten schrittweise erneut laden und testen.

**Schritt 8: Professionelle Reparatur**
- Wenn nach Reset immer noch Crashes: Wahrscheinlich Hardware-Fehler (Prozessor, Mainboard).
- Hersteller-Service kontaktieren.

---

## 8. FAQ — Häufig Gestellte Fragen

### 8.1 Allgemeine Fragen zur Elektronik

**F1: Wie oft sollte ich meine Boot-Elektronik warten?**
A: Minimalstandard ist jährlich vor der Saison (Abschnitt 3.1: Jahresplan). Häufig genutzte Boote sollten halbjährlich gewartet werden. Intensive Salzwasser-Exposition (Fahrt in See) erfordert monatliche Überprüfungen, mindestens der Stecker und Antennen.

**F2: Was ist der Unterschied zwischen NMEA 0183 und NMEA 2000?**
A: NMEA 0183 ist ein älteres serielles Protokoll (4800 oder 38.400 bps, max 32 Geräte). NMEA 2000 ist ein CAN-basiertes Feldbus-Netzwerk (250 kbps, beliebig viele Geräte). NMEA 2000 ist schneller, zuverlässiger und wird in modernen Booten bevorzugt. Alte Geräte können mit Adapter-Konvertern an NMEA 2000 angeschlossen werden.

**F3: Kann ich verschiedene Hersteller-Elektronik (z.B. Garmin GPS + Raymarine Radar) kombinieren?**
A: Ja, solange beide Geräte NMEA 0183 oder NMEA 2000 unterstützen. Beachte, dass nicht alle Hersteller ihre proprietären Funktionen zwischen Systemen freigeben. Standard-Funktionen (Position, Kurs, Geschwindigkeit) funktionieren normalerweise. Proprietary-Features (z.B. Sounder-Integration) können auf dem anderen System nicht verfügbar sein.

**F4: Wie kann ich feststellen, ob meine Antenne beschädigt ist, ohne sie auszubauen?**
A: Visuelle Überprüfung von außen (siehe Abschnitt 2.1, Antennen-Inspektionsliste). Wenn Sie auf dem Dach/Mast sind: Tap-Test (mit Fingerknöchel klopfen) — intakte Glasfaser klingt hohl und klar, beschädigte Antenne klingt gedämpft oder splittrig. Signal-Test: Wenn Signal plötzlich abbricht, ist wahrscheinlich das Kabel oder der Stecker kaputt, nicht die Antenne selbst.

**F5: Was ist der beste Ort für GPS-Antenne an Bord?**
A: Freie Sicht zum Himmel (südlich und westlich, auf der Südhalbkugel nördlich und westlich). Höchster Punkt des Bootes bevorzugt (Mast-Top, Hardtop-Ecke). Entfernung von großen Metallmassen (Radar-Antenne, VHF-Antenne) mindestens 1 Meter. Nicht direkt neben anderen elektronischen Geräten, um Interferenz zu vermeiden.

**F6: Kann ich den Plotter während der Fahrt neu starten?**
A: Nicht empfohlen. Wenn Du während der Fahrt einen Reset durchführst, verlierst Du die Positions-Anzeige für 3–5 Minuten. Besser: In ruhigem Wasser oder beim Ankern neu starten. Im Notfall (z.B. bei kritischem Bug): In Küstennähe fahren und Uhr-Navigation (Dead Reckoning) verwenden, bis Plotter wieder aktiv.

**F7: Wie kann ich sichergehen, dass meine Elektronik-Batterie nicht leer wird?**
A: Batterie-Monitoring-System installieren (siehe Abschnitt 3.2: Batterie-Management). Regelmäßig laden (täglich oder nach jedem Betrieb, bei längeren Segelfahrten mindestens alle 2 Tage). Eine 100-Ah-Batterie sollte nicht unter 40% entladen werden (50% Sicherheitsmarge). Für intensive Elektronik-Nutzung (Radar 24/7, Autopilot, Unterwasserkamera) sollte die Batterie-Kapazität ≥ 200 Ah sein.

**F8: Ist Salzwasser wirklich so schädlich für Elektronik?**
A: Ja, extrem. Salzwasser ist leitend und führt zu Korrosion, Kurzschlüssen und Funktionsausfällen. Jede Elektronik-Komponente, die mit Salzwasser in Kontakt kommt, muss sofort mit Süßwasser gespült und gründlich getrocknet werden. Für Boote in Salzgewässern: ALLE Stecker, Antennen und Kabel sollten geschützt oder vollständig versiegelt sein (siehe Abschnitt 5.2: Korrosionsschutz).

**F9: Kann ich meinen Plotter mit meinem Smartphone per Bluetooth koppeln?**
A: Einige moderne Plotter unterstützen Bluetooth. Dies ist nützlich für Datenübertragung (Routen, Wetter-Downloads), aber nicht für kritische Navigation. Die Verbindung ist weniger zuverlässig als direktes NMEA-Netzwerk. Bluetooth-Reichweite im Freien ca. 10–30m, abhängig von Interferenz.

**F10: Wie speichere ich meine Routen und Einstellungen als Backup?**
A: Die meisten modernen Plotter haben eine SD-Karten-Funktion oder USB-Backup. Siehe Plotter-Handbuch für Backup-Menü. Speichere mindestens monatlich. Für Langfahrten: Backup vor Abfahrt und nach jeder Hafenanlage durchführen. Externe Speicherkarten (SD, USB) in wasserdichtem Behälter lagern.

---

### 8.2 Radar-spezifische FAQ

**F11: Mein Radar zeigt Ziele, die nicht auf der Seekarte sichtbar sind. Ist das normal?**
A: Ja, Radar kann kleine Inseln, Bojen, oder Felsen zeigen, die zu klein für Charts sind. Größere "Geister-Ziele" können Reflexionen von Landmassen sein (siehe Abschnitt 7.4, Schritt 3–4). Wenn systematisch falsche Ziele auftauchen, könnte das Radar schlecht kalibriert sein.

**F12: Warum zeigt mein Radar nachts besser als tagsüber?**
A: Tagsüber kann Sonneneinstrahlung die Radar-Antenne aufheizen und Rauschen verursachen. Nachts, bei kühlerer Temperatur, ist das Signal sauberer. Dies ist normal. Achte darauf, dass die Antenne nicht in direktem Sonnenlicht steht (Überhitzungsschutz).

**F13: Kann ich mit Radar bei Nebel oder Regen fahren?**
A: Ja, Radar funktioniert unabhängig vom Wetter. Regen abschwächt das Signal etwas, aber Radar ist immer noch zuverlässiger als Sicht-Navigation. Radar-Reichweite kann bei starkem Regen um ca. 10–20% reduziert sein, bleibt aber funktional.

**F14: Wie oft muss ich das Radar-Modul kalibrieren?**
A: Radar wird ab Werk kalibriert. Jährliche Überprüfung genügt (siehe Abschnitt 4.2, Radar-Kalibrierung). Wenn Du eine neue Antenne installiert hast, muss das Radar re-kalibriert werden (Hersteller-Service oder Anleitung folgen). Bei Verdacht auf Fehler: vor längeren Fahrten erneut kalibrieren.

**F15: Ist es sicher, beim Radarstrahlen-Durchgang in der Nähe der Antenne zu stehen?**
A: Nein. Radar-Strahlung ist nicht ionisierend, aber intensive Strahlen können gefährlich sein (siehe Abschnitt 1.7: Radar-Sicherheit). Regel: Beim Ausfahren / Einschieben der Antenne oder Wartung sollte das Radar AUS sein. Mindestabstand 0,5m zur rotierenden Antenne, solange sie läuft.

---

### 8.3 GPS und Kompass-FAQ

**F16: Mein GPS-Fehler beträgt ±5–10m. Ist das genau genug?**
A: Ja, das ist normal. Standard-GPS (ohne Differenzial-Korrektion) hat eine typische Genauigkeit von ±3–10m. Dies ist ausreichend für Navigation und Ankern. Für genauere Messungen (z.B. Vermessung, wissenschaftliche Arbeit) brauchst Du RTK-GPS oder ähnliche Systeme (Kosten: 5000–10000 EUR).

**F17: Warum driftet mein elektronischer Kompass beim Wenden ab?**
A: Elektronischer Kompass (Fluxgate) braucht ca. 20–30 Sekunden, um sich nach einer schnellen Kurvenänderung zu stabilisieren. Dies ist normal. Wenn die Drift größer ist oder nicht stabilisiert: Kompass-Kalibrierung erforderlich (siehe Abschnitt 4.4). Magnetische Störungen (große Metallmassen in der Nähe) können auch Abweichungen verursachen.

**F18: Kann ich GPS und Magnetkompass zusammen nutzen?**
A: Ja, ideal. GPS zeigt tatsächliche Bewegungsrichtung (auch bei Abdrift), Magnetkompass zeigt Schiffsausrichtung. Moderne Plotter fusionieren diese Daten für beste Ergebnisse. Bei GPS-Ausfall kann der Magnetkompass weiterhin Navigation unterstützen (auch wenn weniger präzise).

**F19: Wie kann ich meinen Kompass testen, ohne ihn zu kalibrieren?**
A: Vergleich mit bekanntem Referenzkurs: Fahre auf bekannter Landmarke zu, notiere elektronischen Kompass-Kurs und vergleiche mit Seekarte/Kompass-Rose. Abweichung >5° deutet auf Kalibrierungs-Bedarf hin. Für rasche Überprüfung: Iron-Deviation-Tabelle (falls vorhanden) verwenden.

---

### 8.4 Batterie und Stromversorgungs-FAQ

**F20: Wie lange hält eine typische Boot-Batterie, wenn der Plotter 24/7 läuft?**
A: Typischer Plotter: ca. 2–5A pro Stunde (je nach Helligkeit, Radar-Status).
- 100-Ah-Batterie: 100 Ah ÷ 3,5A ≈ 28 Stunden durchgehend. Mit Sicherheitsmarge (50% Reserve): ca. 14 Stunden praktisch.
- Radar eingeschaltet (+5A): 100 Ah ÷ 8,5A ≈ 12 Stunden. Mit Reserve: ca. 6 Stunden praktisch.
- Für längere Segelfahrten: Solar-Ladegerät (50–100W) oder zweite Batterie empfohlen.

**F21: Kann ich mehrere Batterien parallel schalten?**
A: Ja, aber mit Vorsicht. Identische Batterien (gleicher Typ, Alter, Kapazität) parallel schalten. Ungleiche Batterien können sich gegenseitig beschädigen (unterschiedliche Lade-/Entladeraten). Verwende Batterie-Isolations-Dioden oder Batterie-Manager (Kosten: 100–300 EUR).

**F22: Was ist der beste Weg, die Elektronik-Batterie zu laden?**
A: Idealer Lade-Verlauf: Stufe 1 (Constant Current, 10–20A bis 80%), Stufe 2 (Constant Voltage, langsam zu 100%). Gute Ladegeräte regeln dies automatisch (z.B. Victron Smartcharge). Schnelladen (<30 min) beschädigt die Batterie langfristig. Beste Praktiken: Nach jedem Tag laden, nicht unter 40% entladen, nicht über 100% laden (Überladung).

**F23: Ist 12V oder 24V besser für Elektronik-Boote?**
A: Beide funktionieren. 24V ist effizienter für längere Kabel-Strecken (weniger Spannungsverluste). 12V ist häufiger in kleineren Booten. Wahl hängt ab von: Boot-Größe (>15m eher 24V), Motortyp (Diesel-Motor 24V), und verfügbarer Ausrüstung. Einmal wählen, dann konsistent bleiben.

**F24: Wie schütze ich meine Elektronik-Batterie im Winter?**
A: Batterie aufladen auf ca. 80%, an kühlem, trockenem Ort lagern. Monatlich überprüfen: sollte nicht unter 50% Ladung fallen. Wenn möglich: Ladegerät mit Erhaltungsfunktion anschließen (langsame Dauerladung, ca. 0,5A). Im Frühjahr: Spannung überprüfen, ggfs. langsam aufladen.

---

### 8.5 Wartung und Prävention-FAQ

**F25: Kann ich meine Elektronik selbst warten oder muss ich zur Werkstatt?**
A: Routine-Wartung (Überprüfung, Kabelschauen, Reinigung) kannst Du selbst machen (siehe Abschnitt 3.1). Komplexe Reparaturen (Modul-Austausch, Kalibrierung, Programmierung) erfordern oft Spezial-Equipment und sollten vom Hersteller oder Fachbetrieb durchgeführt werden. Im Zweifelsfall: erst Handbuch konsultieren.

**F26: Wie schütze ich meine Antennen vor Beschädigungen während des Transports?**
A: Antennenstecker mit Kunststoff-Kappen schützen (meist im Lieferumfang enthalten). Antenne mit Schaumstoff-Polsterung umwickeln. In einem harten Koffer lagern. Während des Bootstrailers: Antenne soweit möglich nach unten klappen oder abschrauben.

**F27: Wo lagere ich Ersatzteile und Werkzeuge sicher an Bord?**
A: Trockener, belüfteter Ort: z.B. Elektronik-Box mit Silica-Gel-Feuchtigkeitsreglern. Nicht direkt unter Decksluken (wo Wasser eindringen kann). Metallbehälter in Kunststoff-Schächte vermeiden (Kondensation). Werkzeuge in separater trockener Kiste. Ersatzteile in original-Verpackung, wenn möglich.

**F28: Wie oft muss ich Stecker und Kabel überprüfen?**
A: Visuell mindestens monatlich (kurze Oberprüfung, 5 min). Gründlich alle 3 Monate (Stecker auf Korrosion, Kabel auf Risse). Nach jeder intensiven Fahrt (besonders Salzwasser) oder Störungsfall: sofortige Prüfung. Bei Winterlagerung: gründliche Überprüfung vor Lagern und nach Winter-Lagerung.

**F29: Was ist das beste Mittel gegen Oxidation und Korrosion?**
A: Prävention ist beste Methode: Stecker regelmäßig mit WD-40 oder ähnlichem Kontakt-Schutzspray behandeln. Nach Salzwasser-Kontakt: sofort spülen und trocknen. Für hartnäckige Korrosion: feines Sandpapier oder Schleifbürste, dann mit Kontakt-Reiniger (z.B. Electrolube) spülen. Annual: alle Stecker und Kabel mit Korrosionsschutz-Wachs beschichten (z.B. CRC Light Protective Wax).

**F30: Kann ich den Plotter-Bildschirm gegen Kratzer schützen?**
A: Ja. Schutzfolien (ähnlich wie Handy-Schutzfolie) erhältlich für viele Plotter-Modelle (ca. 10–30 EUR). Jedoch reduzieren diese leicht die Bildschirm-Helligkeit und Touchscreen-Reaktivität. Optionale Displayschutz-Glasscheibe (robuster, kostet 50–100 EUR, aber weniger Licht-Verlust).

---

## 9. Glossar — Technische Begriffe und Definitionen

### A
**Antennenverstärkung (Antenna Gain)**
Maß für die Direktivität einer Antenne in Dezibel (dB). Höherer Gain bedeutet stärkere Empfangsempfindlichkeit in bestimmter Richtung, aber schwächerer Empfang in anderen Richtungen.

**Azimuth**
Horizontal-Winkel, gemessen vom Norden im Uhrzeigersinn (0–360°). Beim Radar: Winkel des erkannten Objekts vom Radarschiff aus.

### B
**Baud-Rate / Baudrate**
Übertragungsgeschwindigkeit in Bit pro Sekunde (bps). Standard-NMEA 0183: 4800 bps (älter) oder 38.400 bps (modern).

**Baseline**
Abstand zwischen zwei Antennen desselben Typ-Systems (z.B. zwei GPS-Antennen in RTK-System). Längere Baseline ermöglicht bessere Genauigkeit.

### C
**CAN-Bus (Controller Area Network)**
Feldbus-Protokoll, auf dem NMEA 2000 basiert. Ermöglicht Kommunikation zwischen vielen Geräten mit hoher Zuverlässigkeit.

**Cevni**
Europäische Binnenschifffahrtsstraßen-Verordnung. Regelwerk für Lichter, Flaggen und Signale auf Binnenschiffen.

### D
**Datum**
In GPS: Bezugs-Ellipsoid für Koordinaten-Berechnung. Standard: WGS84. Falches Datum kann zu Positions-Fehler von Hunderten Metern führen.

**Dead Reckoning (DR)**
Navigation aufgrund von Kurs und Geschwindigkeit, ohne externe Referenz. Fehlerhaft über längere Zeit, da Abdrift nicht berücksichtigt.

**Deviation**
Abweichung eines Magnetkompass von Norden aufgrund von lokalen magnetischen Feldern (Motoren, Eisenteile). Wird durch Kompass-Kalibrierung korrigiert.

### E
**ECDIS (Electronic Chart Display and Information System)**
Offizielle digitale Seekarten-Anzeige auf großen Schiffen. Muss zertifiziert sein und offizielle Karten (ENC) verwenden.

**EMV / EMI (Elektromagnetische Verträglichkeit / Elektromagnetische Interferenz)**
Fähigkeit von Elektronik, störungsfrei nebeneinander zu funktionieren. Schlechte EMV führt zu Geister-Zielen auf Radar, GPS-Ausfällen, etc.

### F
**Fluxgate Compass**
Elektronischer Kompass, der das Erdmagnetfeld misst. Empfindlicher als magnetische Kompass, aber anfällig für lokale magnetische Störungen.

**Frequency Modulation (FM)**
Art der Funk-Übertragung. VHF-Funk nutzt FM.

### G
**GLONASS**
Russisches globales Positions-Satelliten-System (Äquivalent zu GPS). Kann zusammen mit GPS für bessere Genauigkeit genutzt werden.

**Grundfehler**
Wahrnehmungs-Fehler bei Kartenlesung oder Kompass-Ablesung. Z.B. um 180° falsch lesen oder Kompass-Rose verwechseln.

### H
**Heading**
Momentane Schiffausrichtung (Kompass-Kurs), unabhängig von tatsächlicher Bewegungsrichtung (Track).

**Hysterese**
Verzögerungseffekt in elektronischen Sensoren. Z.B. Kompass-Anzeige folgt nicht sofort bei schnellen Richtungswechseln.

### I
**IMU (Inertial Measurement Unit)**
Kombination aus Beschleunigungs-Sensoren (Accelerometer) und Drehungs-Sensoren (Gyroscope) zur Erfassung von Schiffs-Bewegungen.

**IALA**
Internationale Vereinigung für Seezeichen und Leuchttürme. Definiert Betonnung-Systeme.

### J
**Jitter**
Zittern oder Flackern in GPS-Position oder Kompass-Anzeige. Meist verursacht durch Multipath oder Sensor-Rauschen.

### K
**Kartum**
Kurzzeitige Positionsänderung durch äußere Einflüsse (Wind, Strömung). Unterschied zwischen Heading (Schiffs-Kurs) und Track (tatsächliche Fahrtrichtung).

**Kurs über Grund (COG)**
Tatsächliche Fahrtrichtung (Track) über das Wasser gemessen. Unterschied zu Heading ist die Abdrift.

### L
**Leckage-Strom (Leakage Current)**
Geringe elektrische Stromstärke, die durch Feuchtigkeit oder Korrosion über Isolationsmaterial fließt. Kann zu Kurzschlüssen führen.

**Line of Sight**
Optische Sichtverbindung zwischen Antenne und Satellit (für GPS) oder zwischen zwei Funktransmittern (VHF). Hindernisse blockieren Signal.

### M
**Multipath**
Fehler entsteht, wenn GPS-Signal von Hindernissen (Metallmast, Wasser) reflektiert wird und Empfänger mehrere verzögerte Signale empfängt. Führt zu Position-Ungenauigkeit.

**MUWI (Multi-User Wide Coverage)**
GPS-Augmentierungssystem für bessere Genauigkeit (meist in Küstenregionen verfügbar).

### N
**NMEA 0183 / NMEA 2000**
Standard-Datenformate für Kommunikation zwischen nautischen Geräten (siehe Abschnitt 1.3).

**Nicht Beurteilbar (N.B.)**
Deutsch: Zustand, in dem Diagnose nicht möglich ist (z.B. "Antennenkabel-Zustand nicht beurteilbar ohne Ausbau").

### O
**Oskulant**
Fachbegriff: optimal angepasster Kreis. In Radarkontext: ideale Radarabdeckung ohne Lücken.

### P
**Peilung**
Winkel zu einem bekannten Objekt von der eigenen Position aus. Wichtig für visuelle Navigation und Positionsfeststellung.

**Phase Center**
Punkt innerhalb einer Antenne, von dem aus die Strahlung emittiert wird (bei GPS-Antenne: Verzögerungsmittelpunkt).

**Port / Backbord**
Links vom Schiff aus (nach vorne schauend). Gegenteil: Starboard (Steuerbord).

### R
**Relativ-Bearing**
Peilung relativ zur Schiffs-Ausrichtung (0° = direkt vorne, 90° = rechts, 180° = direkt achtern).

**ROT (Rate of Turn)**
Drehgeschwindigkeit des Schiffs in Grad pro Minute. Wichtig für Kurven-Navigation und Autopilot-Tuning.

**RMS (Root Mean Square)**
Statistisches Maß für Genauigkeit. GPS-Genauigkeit 5m (RMS) bedeutet 68% der Messungen liegen innerhalb ±5m.

### S
**Seitenfehler**
GPS-Fehler in Ost-West-Richtung (Gegensatz zu vertikalem Fehler).

**Siranah**
Navigations-Zertifikat für Radarfähigkeit bei größeren Schiffen (nicht relevant für private Yachten).

**SOLAS (Safety of Life at Sea)**
Internationales Regelwerk für Seeschiffe. Vorschreibt Ausrüstung, Besatzung, Sicherheitsmaßnahmen.

### T
**Track**
Tatsächliche Fahrtlinie über Grund (berücksichtigt Abdrift durch Strömung/Wind). Unterschied zum Heading.

**True Heading**
Kompass-Kurs bezogen auf wahren Norden (nicht Magnet-Norden).

### U
**Umwälzung**
Zirkulation von Luft oder Flüssigkeit. In Elektronik-Boxen: wichtig für Wärme-Abfuhr.

### V
**Variation**
Unterschied zwischen magnetischem und wahrem Norden. Regional unterschiedlich (bis zu ±20°). Muss in Navigationspläne eingerechnet werden.

**VHF (Very High Frequency)**
Funk-Band für See-Funkverkehr (156–174 MHz). Reichweite ca. 20–50 km je nach Antenne und Höhe.

### W
**Wayfinding**
Navigations-Verfahren unter Nutzung von Landmarken, Leuchttürmen, Bojen (visual navigation).

**White Noise**
Gleichmäßiges elektronisches Rauschen ohne Struktur. Auf Radar-Bild als helles Rauschen sichtbar.

### X
**X-Track Error (XTE)**
Seitwärts-Abweichung vom geplanten Kurs (wie weit rechts oder links von der Linie man ist). Wichtig für Autopilot-Steuerung.

### Y
**Yaw (Stampfen)**
Drehung des Schiffs um die vertikale Achse (Links-Rechts-Bewegung). Relevant für Autopilot und Radaralignment.

### Z
**Zeitzone**
Lokale Zeit relativ zu UTC/GMT. Plotter müssen auf lokale Zeit kalibriert sein. Beispiel: CET = UTC+1.

**Zielbestätigung**
Prozess, bei dem Radar-Ziele automatisch verfolgt (Tracking) oder manuell bestätigt werden (damit Plotter Ziel automatisch berücksichtigt).

---

## 10. Schnell-Referenz — Tabellen und Checklisten

### 10.1 Wartungsintervalle nach Boot-Größe und Nutzungsprofil

| Boot-Größe | Nutzung | Minimum-Intervall | Gründliche Prüfung | Antennen-Check | Kalibrierungen |
|-----------|---------|-------------------|-------------------|-----------------|---|
| <8m | Wochenend-Freizeit | Monatlich | 3 Monate | Monatlich | Jährlich |
| 8–14m | Regelmäßig (50h/Jahr) | Monatlich | 2 Monate | Alle 6 Wochen | 2x jährlich |
| 14–20m | Häufig (100h+/Jahr) | Alle 2 Wochen | Monatlich | Monatlich | 3x jährlich |
| 20m+ | Intensiv (200h+/Jahr) | Wöchentlich | Alle 2 Wochen | 2x monatlich | 4x jährlich |
| Charter-Boot | Täglich wechselnde Crews | Täglich Schnell-Check | Nach jeder Fahrt | Nach jeder Fahrt | Monatlich |

### 10.2 Drehmoment-Spezifikationen für Stecker und Kabel-Klemmen

| Komponente | Material | Drehmoment (Nm) | Anmerkung |
|-----------|----------|------------|-----------|
| Stecker-Ring (M-Stecker) | Messing | 0,5–1,0 | Hand-fest, nicht überdreht |
| BNC-Stecker (Radar/Antenne) | Kunststoff | 0,3–0,5 | Vorsicht, leicht zu beschädigen |
| Kabel-Klemme, Boot-Stromanlage | Messing, verzinkt | 1,0–1,5 | Sicher, aber nicht zu fest |
| Koaxial-Kabel-Klemme (N-Stecker) | Messing/Kunststoff | 1,5–2,0 | Fest, aber sorgfältig |
| UKW-Antenne Montage-Schraube | V4A Edelstahl | 2,0–3,0 | Salzwasser-Betrieb |

### 10.3 Elektronik-Netzwerk: Typische Kabel-Längen und Verluste

| Kabel-Typ | Max. Länge (m) | Spannungs-Verlust (%/50m) | Anwendung |
|----------|-----------|---------------------------|-----------|
| NMEA 0183 (Twisted Pair, geschirmt) | 100 | N/A (digital) | GPS/Kompass zu Plotter |
| NMEA 2000 (DeviceNet-Kabel) | 250 | N/A (digital) | Multi-Device-Netzwerk |
| Koaxial RG-58 (GPS/Radar) | 50 | 1,5 | Antenne zu Empfänger |
| Stromkabel 12V (2,5 mm²) | 5 | 4 % | Batterie zu Elektronik |
| Stromkabel 12V (4 mm²) | 10 | 2,5 % | Längere Strecken |
| Stromkabel 24V (1,5 mm²) | 10 | 2,5 % | Weniger Verlust als 12V |

### 10.4 Stecker und Verbinder-Typen (Boot-Elektronik)

| Stecker-Typ | Signal | Impedanz | Wett.schutz | Anwendung | Kosten EUR |
|----------|--------|----------|----------|-----------|---------|
| RCA (Cinch) | Audio/Video | 75 Ω | Keine | Ältere Video-Ausgänge | 1–3 |
| BNC | HF-Signal | 50 Ω | Einfach | Radar, Antenne | 5–10 |
| N-Stecker | HF-Signal | 50 Ω | Sehr gut | UHF-Antenne | 10–20 |
| Micro-DIN | Digital (seriell) | – | Mittel | Ältere GPS/Kompass | 3–8 |
| M12 | NMEA 2000, Ethernet | – | Sehr gut | Moderne Boot-Netze | 20–50 |
| USB-B (wasserdicht) | Digital | – | Sehr gut | Datenübertragung | 15–30 |
| XLR | Audio (3-pin) | – | Sehr gut | Funkanlage-Ausgänge | 5–15 |

### 10.5 Notfall-Reparatur-Kit (Checkliste)

Sollte an Bord mitgeführt werden:

- [  ] Ersatz-Batterie (kleine Backup 20–30 Ah)
- [  ] Ersatz-Sicherungen (verschiedene Amperezahlen: 5A, 10A, 15A, 20A)
- [  ] Ersatz-NMEA-Kabel (mindestens 2m)
- [  ] Ersatz-Stromkabel (rot/schwarz, verschiedene Querschnitte)
- [  ] Ersatz-Stecker-Set (USB, BNC, Micro-DIN je 1–2 Stück)
- [  ] Lötkolben (20–40W, batteriebetrieben oder 12V Bordnetz)
- [  ] Lot und Lötdraht (bleifreies Zinn, 0,5mm Durchmesser)
- [  ] Elektrolyt-Kondensatoren-Sortiment (10µF, 47µF, 100µF, 470µF je 16–50V)
- [  ] Dioden und Transistoren (Standard-Typen: 1N4007, 2N2222, etc.)
- [  ] Multimeter (digital, 12–24V Spannungsprüfung)
- [  ] Stromzange / Amp-Meter (bis 50A)
- [  ] Feines Sandpapier (P120, P220) und Schleifbürste
- [  ] WD-40 oder Kontakt-Schutz-Spray (2 Dosen)
- [  ] Silikon-Dichtmasse (UV-härtend, für Stecker-Abdichtung)
- [  ] Kabel-Isolier-Klebeband und Schrumpfschläuche (verschiedene Größen)
- [  ] Spannungsregler / Gleichrichter (kleine 12V Module)
- [  ] USB-Kabel (A-B und A-Micro-B je 2m)
- [  ] Sicherungs-Halter und Klemmen (verschiedene Größen)
- [  ] Kleine Werkzeuge: Zange, Schraubendreher-Satz, Inbusschlüssel

**Lagerungsort:** Trockener, belüfteter Fach in Elektronik-Box. Alle elektronischen Teile in Plastikboxen lagern (Feuchtigkeitsschutz).

---

## 11. ANHANG A–H — Fallstudien (Yacht-Diagnose-Szenarien)

### Anhang A: Fallstudie — Segelboot 12m, Lagoon-Charteryacht, GPS-Fehler in französischer Riviera

**Boot:** Lagoon 450 Segelkatamaran, 14m, 6 Gasten, GPS Garmin 7612, Radar Furuno, Kompass H5000.

**Problem:** Skipper meldet, dass GPS-Position um ca. 2 km bei Einfahrt in Port de Golfe-Juan fehlgeht. Zuerst im freien Meer ok, aber ab 5 km vor Küste wird Position unzuverlässig. Kompass funktioniert. Radar auch.

**Diagnose-Prozess:**

1. **Ort überprüfen:** Côte d'Azur ist bekannt für Multipath-Fehler (steile Felsenküste mit GPS-Reflexionen).
2. **GPS-Antenne überprüfen:** Antenne sitzt auf Bimini-Frame (Schattenfläche möglich?). Nein, Antenne hat 360° Sicht.
3. **Kabel-Kontrolle:** NMEA-Kabel vom GPS-Empfänger zum Plotter 20m lang, neben 400W-Inverter verlegt. Mögliche EMI?
4. **Messungen:**
   - Spannung an GPS: 12.1V (ok)
   - NMEA-Signal-Integrität: Sichtprüfung Kabel → ok, aber nah bei Stromkabel
5. **Radius-Test:** Fahre 50m Umkreis, GPS sollte konstant Kreis-Positionen zeigen. Resultat: springt zwischen mehreren Positionen (Multipath).

**Lösung:**
- GPS-Kabel vom Stromkabel räumlich trennen (mindestens 0,5m Abstand). Ferritring um GPS-Kabel-Eingang installieren (EMI-Filter).
- GPS-Antenne auf Mast-Top versetzen (über Radar-Antenne, Abstand 1m).
- Nach Anpassung: GPS-Genauigkeit ±3–5m (normal für Küstengebiet).

**Lernpunkt:** GPS im Radar-Umfeld benötigt gute Schirmung und räumliche Trennung von Stromkabel. In enger Küstenlinie sind kleine Fehler normal (akzeptieren oder RTK-GPS nutzen).

---

### Anhang B: Fallstudie — Motorboot 8m, Nord-See, Kompass-Abweichung 15°

**Boot:** Sunseeker Speedboat 8m, Diesel-Außenborder, Raymarine Axiom Pro Plotter, Fluxgate-Kompass (intern).

**Problem:** Skipper bemerkt, dass Autopilot beim Fahren konstant nach Osten abweicht (sollte Süd fahren, tatsächlich SE). Manuelles Lenken ok.

**Diagnose-Prozess:**

1. **Referenz-Navigation:** Vergleich elektronischer Kompass mit magnetischem Notfall-Kompass. Magnetkompass zeigt Süd, elektronisch Kompass zeigt etwa 150° (sollte 180°).
2. **Deviation-Tabelle überprüfen:** Plotter hat Deviation-Tabelle, zeigt Fehler von +15° bei Kurs Süd. Dies deutet auf neue magnetische Störung hin (z.B. Metall-Gegenstand zugekommen).
3. **Magnet-Suche:** Inspektion Kabinenraum über Kompass. Neue Stahlplatte wurde kürzlich oberhalb Kompass installiert (Struktur-Verstärkung). Diese erzeugt lokales Magnetfeld.

**Lösung:**
- Stahlplatte durch Kunststoff-Alternative ersetzen oder neu kalibrieren.
- Kompass-Kalibrierung durchführen (Plotter-Menü → Navigation → Compass Calibration → Circulat-Routine durchlaufen).
- Nach Kalibrierung: Deviation <2° (akzeptabel).

**Lernpunkt:** Neue Metallinstallationen müssen vor Kompass-Kalibrierung berücksichtigt werden. Deviation >5° beeinträchtigt Autopilot und Sicherheit.

---

### Anhang C: Fallstudie — Segelyacht 16m, Mittelmeer, Radar-Multipe-Targets

**Boot:** Bavaria 49 Cruiser, Segelyacht 16m, Furuno DFF3 Radar, Kohärenz-Problem im Golf von Neapel.

**Problem:** Radar zeigt mehrere falsche Ziele. Echte Schiffe + mehrere Geister-Schiffe +/- 10 km in alle Richtungen. GPS funktioniert ok.

**Diagnose-Prozess:**

1. **Schmutz-Check:** Antenne auf Mast sauber (kein Algen-Belag).
2. **Radarschirm-Reichweite reduzieren:** Von 24 nm auf 8 nm → Falsche Ziele verschwinden teilweise, aber nicht ganz.
3. **Radarmodul-Temperatur:** Antenne und Modul sehr heiß (62°C, sollte <50°C). Modul sitzt über Maschinenraum (Hitze vom Diesel-Generator).
4. **Störquellen-Scan:** Andere Elektronik-Geräte aktiviert. Sofort nach Aktivierung von neuer High-Power-Funkanlage (500W Seefunk) verschärfen sich Artefakte dramatisch.

**Lösung:**
- Radar-Modul-Montage überprüfen: Isolierung von Motorenraum verbessern (Schaumstoff-Isolation hinzufügen).
- Funk-Antenne und Radar-Antenne räumlich trennen (mind. 2m Abstand, ideal auf verschiedenen Seiten des Mastes).
- Koaxial-Kabel von Funk abschirmen (separate Röhre, ferrit-Kerne hinzufügen).
- Radarmodul-Lüftung überprüfen: Lüfter verstopft? Lüfter-Öffnung freimachen.
- Nach Anpassungen: Radar-Qualität normal, falsche Ziele weg.

**Lernpunkt:** Seefunk und Radar konkurrieren um Frequenzbande (X-Band ~10 GHz). EMV-Schutz und räumliche Trennung sind kritisch. Hitze reduziert Radar-Empfindlichkeit und erhöht Rauschen.

---

### Anhang D: Fallstudie — Motorboot 20m, Mittelmeer Chartersflotte, Systemausfall Boot-Familie

**Boot:** Sunseeker Predator 60, Charter-Motorboot 20m, Integriertes Plotter-System (Garmin GPSMAP 8616xsv), mehrere Clients.

**Problem:** Nach 3-wöchiger Charter: Plotter schaltet sich spontan aus und neu. Occurs alle 2–3 Stunden. Ausbremse und Restart möglich, aber Problem wiederholt sich. Radar und GPS funktionieren, aber Navigationssystem unbrauchbar.

**Diagnose-Prozess:**

1. **Crash-Log überprüfen:** Plotter-Menü → Diagnostics → System Log zeigt: "Overtemp Shutdown" mit Zeitstempel alle 2–3 Stunden.
2. **Elektronik-Box-Temperatur:** Box-Thermometer zeigt 52°C (sollte <45°C). Lüfter funktioniert, aber Einlass-Öffnung halb blockiert (Staub, Algen-Belag).
3. **Stromversorgungs-Prüfung:** Spannungs-Messung stabil (12V), aber Strom-Spitzenwerte bis 25A beobachtet (sollte <15A für diesen Plotter).
4. **Software-Version:** Firmware ist 2 Jahre alt (von Charter-Betrieb nicht aktualisiert).

**Lösung:**
- Elektronik-Box-Lüfung reinigen (Staub ausblastgen, Algen-Belag mit Süßwasser spülen).
- Plotter-Lüfter selbst überprüfen: läuft? Lager sauber? Lüfter konnte auch verstopft sein (Motor verbrauchte mehr Strom).
- Firmware-Update durchführen (neuere Version hat bessere Hitze-Management).
- Stromverbrauch analysieren: Warum >25A? Mehrere Geräte parallel aktiv? Inverter in Nähe mit hoher Last? 
- Elektronik-Box an kühlerer Stelle (Schatten, gute Belüftung) neu positionieren.
- Nach Fixes: Kein weiterer Crash, System läuft stabil 20 Stunden+.

**Lernpunkt:** Charter-Boote brauchen robusterer Wartungs-Planung. Elektronik-Box-Belüftung ist kritisch. Alte Software kann Thermal-Management-Bugs haben. Firmware-Updates sind nicht optional für intensive Nutzung.

---

### Anhang E: Fallstudie — Segelyacht 10m, Hollandküste, Wasser-Eindringung in Stecker

**Boot:** Dehler 34 OD, Segelyacht 10m, Navigations-Set: Garmin GPS 17x (externe Antenne), Autopilot B&G Navpilot 360.

**Problem:** Nach nächtlicher Fahrt im Regen: GPS-Signal weg. Autopilot schaltet sich wegen "No Heading" ab. GPS-Antenne zeigt kein Signal (LED blinkend, sollte grün sein).

**Diagnose-Prozess:**

1. **Antenne sichtprüfen:** Antenne on Bimini-Frame sitzt, Dach leckt etwas (Wasser-Tropfen sichtbar um Antenne).
2. **Stecker-Inspektion:** GPS-Stecker an Antenne: viel Wasser sichtbar, Stecker-Kontakte grünlich (Oxidation durch Salzwasser).
3. **Kabel überprüfen:** Kabel-Durchgang durch Decke: Schrumpfschlauch fehlt, Wasser kann eindringen.
4. **Stromanschluss:** GPS wird von Hauptbatterie gespeist (gut), aber Stromkabel auch nass (Kurzschluss-Risiko).

**Lösung:**
- Stecker sofort abnehmen, trocknen (Heißluft-Fön, 20 min).
- Stecker-Kontakte mit feiner Bürste reinigen, dann mit WD-40 behandeln.
- GPS-Kabel komplett überprüfen: an Deck-Durchgang Wasser-Dichtung (Silikon-Kitt, Schrumpfschlauch) anbringen.
- Bimini-Dach-Lecks reparieren (Gelcoat-Riß absenken, neu versiegeln).
- Nach Trocknungs-Zeit: GPS-Signal zurück, normal funktionierend.
- Prävention: Alle Stecker an Deck mit Kunststoff-Schutz-Kappen schützen, auch wenn nicht in Gebrauch.

**Lernpunkt:** Wasser ist die #1 Elektronik-Killer auf Booten. Alle Deck-Durchgänge müssen wasserdicht sein. Stecker-Oxidation durch Salzwasser ist unvermeidlich — regelmäßige Wartung ist notwendig.

---

### Anhang F: Fallstudie — Motorboot 12m, Spanien, Batterie-Tiefentladung

**Boot:** Jeanneau NC 9, Motorboot 12m, Standard-Batterie 100 Ah, Elektronik: 2x Plotter, Radar, Sounder, Autopilot, Heizung.

**Problem:** Nach 12-stündiger Tagestour (30 Seemeilen Kreuzfahrt): Abends alle Geräte grau/schwach. Plotter-Helligkeit minimal, Radar-Signal schwach, GPS funktioniert nicht. Batterie-Spannung 10.2V (sollte >11.5V sein).

**Diagnose-Prozess:**

1. **Batterie-Spannungs-Messung:** 10.2V → zu niedrig. Boot ist nicht geladen worden (Lademodus aus oder Ladeanlage defekt).
2. **Ladeanlage-Prüfung:** Motor läuft, aber Ladeanlage zeigt 0A Ladestrom (sollte 50–80A beim Starten). Alternator wahrscheinlich defekt.
3. **Stromverbrauch-Analyse:** Beide Plottern + Radar + Sounder + Autopilot laufen 12 Stunden = ca. 8–10A durchschnittlich = 80–120 Ah Entladung. 100 Ah Batterie war zu klein für intensive Nutzung.
4. **Batterie-Status:** 10.2V bei 100 Ah = tiefe Entladung (unter 50%). Batterie wahrscheinlich beschädigt (LiFePO4-Tiefentladung = Zellenschäden).

**Lösung (Sofort):**
- Motor starten, Alternator neu starten (möglich, daß es nur Kontakt-Problem war). Ja, Ladeanlage gibt jetzt 70A → Alternator funktioniert.
- 2–3 Stunden fahren, um Batterie teilweise zu laden (auf ca. 12.5V).
- Elektronik minimal betreiben (nur 1x Plotter, Radar aus).

**Lösung (Langfristig):**
- Alternator überprüfen: Riemen Spannung ok? Kabel-Kontakt zu Batterie ok? Regler funktioniert?
- Batterie-Kapazität erhöhen: 200 Ah statt 100 Ah für intensiven Betrieb.
- Solaranlage installieren (50–100W) für Tages-Ladung.
- Elektronik-Audit: Stromverbrauch bei jeder Geräte-Kombination messen (um überlastung zu vermeiden).

**Lernpunkt:** Batterie-Tiefentladung ist destruktiv. 100 Ah ist für modernen Boot mit viel Elektronik unzureichend. Monitoring-System (Ah-Zähler) ist unverzichtbar für lange Fahrten ohne Motor-Ladung.

---

### Anhang G: Fallstudie — Segelyacht 18m, Baltikum, Winterlagerung-Schäden

**Boot:** X-Yachts X43, Segelyacht 18m, hochwertige Elektronik (Multitouch-Plotter, professionelle Radaranlage).

**Problem:** Nach 4 Monaten Winter-Lagerung: Elektronik schaltet sich nicht ein. Plotter schaltet an und wieder aus (Bootloop). Radar-Antenne macht seltsame Geräusche, als ob sie blockiert ist.

**Diagnose-Prozess:**

1. **Batterien überprüfen:** Batterie ist vollständig leer (0V). Dies ist normal nach Winterlagerung ohne Erhaltungs-Laden. Ladegerät angesteckt, Batterie wurde langsam aufgeladen auf 12V.
2. **Plotter-Test:** Nach Batterie-Laden startet Plotter, aber schaltet nach 20 Sekunden aus (Thermal Shutdown wahrscheinlich).
3. **Elektronik-Box öffnen:** Feuchtigkeits-Kondensation sichtbar (Innenseite Fenster beschlagen, Schaumstoff nass). Silica-Gel-Beutel ist völlig gesättigt (blau → weiß).
4. **Radar-Antenne:** Mechanische Blockade: Schnee/Eis war auf Antenne, ist jetzt teilweise gefroren/blockiert.

**Lösung:**
- Batterie mit Erhaltungs-Ladegerät monatlich überprüfen (während Winterlagerung hätte dies verhindert).
- Elektronik-Box: Alle Teile herausnehmen, mit Heißluft trocknen (Haarfön ok, Heißlüfter besser). Silica-Gel-Beutel wechseln. Box 24 Stunden offen lassen, um zu trocknen. Dann Silica-Gel erneut einfüllen.
- Komponent-Überprüfung: Nachdem alles trocken, komponenten einzeln testen (Multimeter-Spannungs-Check).
- Radar-Antenne: Eis entfernen (salzfreies Wasser aufwärmen, antauen lassen, nicht erzwingen). Antenne sollte frei drehbar sein.
- Nach Trocknung: Alle Systeme normal funktionierend.

**Lernpunkt:** Winterlagerung braucht Vorbereitung: Batterie mit Erhaltungs-Ladegerät, Elektronik-Box mit Trockner (Silica-Gel regelmäßig wechseln), Antenne freimachen von Eis/Schnee. Feuchtigkeits-Kontrolle ist für Elektronik-Langlebigkeit kritisch.

---

### Anhang H: Fallstudie — Charteryacht 14m, Karibik, EMI-Problem mit Seefunk

**Boot:** Lagoon Catamaran, 14m, Chart-Boot mit mehreren Gästen.

**Problem:** Nach Installation neuer 25W-SSB-Seefunkanlage: GPS-Position wird chaotisch (springt um Kilometer), Radar zeigt wilde Artefakte.

**Diagnose-Prozess:**

1. **Reihenfolge-Analyse:** EMI tritt nur auf, wenn Seefunk TX ist. GPS und Radar ok, wenn Funk aus ist.
2. **Antenne-Position überprüfen:** Seefunk-Antenne neben GPS-Antenne installiert (beide auf Bimini-Frame, Abstand nur 0.5m).
3. **Kabel-Routing überprüfen:** Funk-Stromkabel und GPS-NMEA-Kabel parallel gelegt (ca. 3m gemeinsam).
4. **Funk-Ausgangsleistung:** Funk läuft auf 25W max, aber ohne Anpassungs-Regler (SWR-Meter zeigt SWR >2.0, bedeutet falsche Antenne-Impedanz, höhere Abstrahlung).

**Lösung:**
- Antenne-Abstand erhöhen: Funk-Antenne auf andere Mast-Seite verschieben (mind. 2m von GPS-Antenne).
- Kabel-Trennung: Funk-Stromkabel und GPS-Kabel räumlich trennen (mind. 1m), ferrit-Kerne um beide Kabel-Bündel platzieren.
- SWR-Meter überprüfen: Funk-Tuning durchführen (Antenne-Matching). SWR sollte <1.5 sein.
- Erdung verbessern: Funk-Gegengewicht (Radials) sollte auf Wasser ausgerichtet sein, nicht auf Boot-Struktur. Radials verlängern oder optimieren.
- Nach Anpassungen: EMI weg, GPS und Radar normal, Funk funktioniert gut.

**Lernpunkt:** Funk-Installationen (besonders SSB mit hoher Leistung) erfordern EMV-Planung. Separate Antennen, getrennte Kabel-Strecken, und korrekte Erdung sind Muss. EMI ist vorhersehbar und vermeidbar mit Planung.

---

## 12. ANHANG I–R — Pydantic v2 Datenmodelle (Code)

### Anhang I: ElectronicComponent

```python
from pydantic import BaseModel, Field
from typing import Optional, Literal
from datetime import datetime
from enum import Enum

class ComponentType(str, Enum):
    GPS = "gps"
    RADAR = "radar"
    COMPASS = "compass"
    SOUNDER = "sounder"
    VHF_RADIO = "vhf_radio"
    SSB_RADIO = "ssb_radio"
    AUTOPILOT = "autopilot"
    PLOTTER = "plotter"
    ANTENNA = "antenna"
    BATTERY = "battery"
    CHARGING_SYSTEM = "charging_system"
    DISTRIBUTION_PANEL = "distribution_panel"
    CABLE_HARNESS = "cable_harness"
    CONNECTOR = "connector"
    POWER_SUPPLY = "power_supply"
    TRANSDUCER = "transducer"
    DISPLAY = "display"
    PROCESSOR_MODULE = "processor_module"

class BoatClass(str, Enum):
    PRODUCTION_SMALL = "production_small"  # <8m
    PRODUCTION_MEDIUM = "production_medium"  # 8-14m
    PRODUCTION_LARGE = "production_large"  # 14-20m
    SEMI_CUSTOM = "semi_custom"  # 20-30m
    CUSTOM_SUPERYACHT = "custom_superyacht"  # >30m

class ElectronicComponent(BaseModel):
    model_config = {"from_attributes": True}
    
    component_id: str = Field(..., description="Unique identifier (e.g. 'GPS_001', 'RADAR_MAIN')")
    component_type: ComponentType = Field(..., description="Type of electronic component")
    manufacturer: str = Field(..., description="Brand/manufacturer (Garmin, Furuno, Raymarine, etc.)")
    model_number: str = Field(..., description="Exact model designation")
    serial_number: Optional[str] = Field(None, description="Serial number if available")
    
    installed_date: Optional[datetime] = Field(None, description="Date of installation")
    warranty_expiry: Optional[datetime] = Field(None, description="Warranty expiration date")
    
    location_on_boat: str = Field(..., description="Physical location (e.g. 'Mast-Top', 'Helm Station', 'Engine Room')")
    boat_class: BoatClass = Field(..., description="Classification of boat this component serves")
    
    power_consumption_avg_watts: float = Field(0.0, description="Average power draw in watts")
    power_consumption_max_watts: float = Field(0.0, description="Peak power draw in watts")
    operating_voltage: float = Field(12.0, description="Required voltage (12V or 24V)")
    
    firmware_version: Optional[str] = Field(None, description="Current firmware/software version")
    last_firmware_update: Optional[datetime] = Field(None, description="When firmware was last updated")
    
    mounts_to: Optional[str] = Field(None, description="Reference to what it mounts on (e.g. 'MAST_001', 'PANEL_001')")
    cabling_standard: Optional[str] = Field(None, description="NMEA 0183, NMEA 2000, CAN-Bus, proprietary, etc.")
    
    notes: Optional[str] = Field(None, description="General notes or special considerations")


### Anhang J: MaintenanceRecord

```python
from pydantic import BaseModel, Field
from typing import Optional, List, Literal
from datetime import datetime

class MaintenanceType(str, Enum):
    VISUAL_INSPECTION = "visual_inspection"
    CLEANING = "cleaning"
    CORROSION_TREATMENT = "corrosion_treatment"
    FIRMWARE_UPDATE = "firmware_update"
    CALIBRATION = "calibration"
    REPAIR = "repair"
    REPLACEMENT = "replacement"
    WINTERIZATION = "winterization"
    COMMISSIONING = "commissioning"
    DIAGNOSTIC_TEST = "diagnostic_test"
    PREVENTIVE = "preventive"

class MaintenanceStatus(str, Enum):
    COMPLETED = "completed"
    IN_PROGRESS = "in_progress"
    SCHEDULED = "scheduled"
    OVERDUE = "overdue"
    NOT_REQUIRED = "not_required"

class MaintenanceRecord(BaseModel):
    model_config = {"from_attributes": True}
    
    maintenance_id: str = Field(..., description="Unique record ID (e.g. 'MAINT_2024_001')")
    component_id: str = Field(..., description="Reference to ElectronicComponent.component_id")
    
    maintenance_type: MaintenanceType = Field(..., description="Type of maintenance performed")
    status: MaintenanceStatus = Field(default=MaintenanceStatus.COMPLETED)
    
    scheduled_date: datetime = Field(..., description="When maintenance was/is scheduled")
    completed_date: Optional[datetime] = Field(None, description="When it was actually completed")
    
    interval_days: Optional[int] = Field(None, description="Planned interval from last maintenance (e.g. 30, 90, 365)")
    
    technician_name: Optional[str] = Field(None, description="Name of person performing maintenance")
    technician_certification: Optional[str] = Field(None, description="Relevant certifications")
    
    description: str = Field(..., description="What was done / what needs to be done")
    findings: Optional[str] = Field(None, description="What was found (good/bad/needs attention)")
    
    parts_replaced: Optional[List[str]] = Field(None, description="List of replaced components/parts")
    parts_cost_eur: Optional[float] = Field(None, description="Cost of parts in EUR")
    labor_hours: Optional[float] = Field(None, description="Hours of labor spent")
    labor_cost_eur: Optional[float] = Field(None, description="Labor cost in EUR")
    
    next_maintenance_due: Optional[datetime] = Field(None, description="Calculated next maintenance date")
    photos_attached: Optional[List[str]] = Field(None, description="File paths to attached photos/evidence")
    
    notes: Optional[str] = Field(None, description="Additional notes or observations")


### Anhang K: FaultDiagnosis

```python
from pydantic import BaseModel, Field
from typing import Optional, List, Literal
from datetime import datetime

class ConfidenceLevel(str, Enum):
    CERTAIN = "certain"  # 95-100%
    HIGH = "high"  # 80-94%
    MEDIUM = "medium"  # 60-79%
    LOW = "low"  # 40-59%
    SPECULATIVE = "speculative"  # <40%

class FaultSeverity(str, Enum):
    CRITICAL = "critical"  # System non-functional, safety risk
    HIGH = "high"  # Major feature impaired
    MEDIUM = "medium"  # Feature degradation, workaround possible
    LOW = "low"  # Minor issue, does not affect operation
    COSMETIC = "cosmetic"  # Visual only

class FaultDiagnosis(BaseModel):
    model_config = {"from_attributes": True}
    
    fault_id: str = Field(..., description="Unique fault record ID (e.g. 'FAULT_2024_0042')")
    component_id: str = Field(..., description="Reference to affected ElectronicComponent")
    
    reported_date: datetime = Field(..., description="When issue was first reported")
    symptom_description: str = Field(..., description="What the user observed (keine Signal, Bildschirm dunkel, etc.)")
    
    suspected_root_cause: List[str] = Field(..., description="List of hypothesized causes, ranked by probability")
    
    diagnostics_performed: List[str] = Field(..., description="Tests/checks run (Tap-Test, Multimeter, etc.)")
    diagnostic_findings: Optional[str] = Field(None, description="Results of diagnostic tests")
    
    confidence_level: ConfidenceLevel = Field(default=ConfidenceLevel.MEDIUM, description="How confident is the diagnosis")
    severity: FaultSeverity = Field(default=FaultSeverity.MEDIUM, description="How critical is the problem")
    
    recommended_action: str = Field(..., description="What should be done (repair, replace, calibrate, etc.)")
    estimated_repair_cost_eur: Optional[float] = Field(None, description="Estimated cost to fix")
    estimated_repair_hours: Optional[float] = Field(None, description="Estimated labor hours")
    
    decision_tree_path: Optional[str] = Field(None, description="Reference to troubleshooting tree followed (e.g. '7.1 / Schritt 4')")
    
    resolution_status: Optional[str] = Field(None, description="OPEN, IN_PROGRESS, RESOLVED, DEFERRED")
    resolution_date: Optional[datetime] = Field(None, description="When issue was resolved")
    resolution_method: Optional[str] = Field(None, description="What finally fixed it")
    
    return_to_service_test: Optional[str] = Field(None, description="Test performed to verify fix (Signal test, Performance check, etc.)")
    
    similar_historical_cases: Optional[List[str]] = Field(None, description="References to previous faults with same symptoms")
    knowledge_base_link: Optional[str] = Field(None, description="Link to related documentation (Abschnitt 6.x, etc.)")
    
    notes: Optional[str] = Field(None, description="Additional context or observations")


### Anhang L: ConnectorAssessment

```python
from pydantic import BaseModel, Field
from typing import Optional, Literal
from datetime import datetime

class ConnectorCondition(str, Enum):
    EXCELLENT = "excellent"  # No corrosion, tight fit, fully functional
    GOOD = "good"  # Minor surface oxidation, functionally normal
    FAIR = "fair"  # Visible corrosion, works but marginal
    POOR = "poor"  # Significant corrosion or mechanical damage, unreliable
    FAILED = "failed"  # Non-functional, must replace

class ConnectorType(str, Enum):
    RCA_CINCH = "rca_cinch"
    BNC = "bnc"
    N_CONNECTOR = "n_connector"
    M_CONNECTOR = "m_connector"
    MICRO_DIN = "micro_din"
    M12 = "m12"
    USB_A = "usb_a"
    USB_B = "usb_b"
    USB_MICRO = "usb_micro"
    XLR_3PIN = "xlr_3pin"
    DSUB_9PIN = "dsub_9pin"
    DSUB_25PIN = "dsub_25pin"
    CUSTOM_PROPRIETARY = "custom_proprietary"

class ConnectorAssessment(BaseModel):
    model_config = {"from_attributes": True}
    
    assessment_id: str = Field(..., description="Unique ID for this connector check")
    cable_or_device_id: str = Field(..., description="Reference to device/cable being assessed")
    
    connector_type_male: ConnectorType = Field(..., description="Type of male connector")
    connector_type_female: ConnectorType = Field(..., description="Type of female connector")
    
    location_male_end: str = Field(..., description="Where male end is located (e.g. 'GPS Antenna')")
    location_female_end: str = Field(..., description="Where female end is located (e.g. 'Plotter NMEA Port')")
    
    assessment_date: datetime = Field(..., description="When this assessment was made")
    
    corrosion_visible: bool = Field(default=False, description="Any green/white oxidation visible")
    corrosion_severity: Optional[Literal["none", "light", "moderate", "heavy"]] = Field(None)
    
    water_intrusion: bool = Field(default=False, description="Any signs of moisture inside connector")
    mechanical_damage: bool = Field(default=False, description="Pins bent, housing cracked, etc.")
    
    fit_tightness: Optional[Literal["loose", "normal", "tight"]] = Field(None, description="How securely connector fits")
    
    overall_condition: ConnectorCondition = Field(default=ConnectorCondition.GOOD)
    
    recommended_action: Optional[str] = Field(None, description="e.g. 'Clean with WD-40', 'Replace connector', 'Monitor next month'")
    
    treatment_applied: Optional[str] = Field(None, description="What was done (cleaning, replacement, etc.)")
    treatment_date: Optional[datetime] = Field(None, description="When treatment was applied")
    
    photos: Optional[List[str]] = Field(None, description="File paths to photos of connector condition")
    
    notes: Optional[str] = Field(None, description="Additional observations")


### Anhang M: EMVAnalysis

```python
from pydantic import BaseModel, Field
from typing import Optional, List
from datetime import datetime

class EMVAnalysis(BaseModel):
    model_config = {"from_attributes": True}
    
    analysis_id: str = Field(..., description="Unique ID (e.g. 'EMV_2024_001')")
    boat_id: str = Field(..., description="Reference to boat being analyzed")
    
    analysis_date: datetime = Field(..., description="When EMV survey was conducted")
    analyzer_name: Optional[str] = Field(None, description="Name of technician performing analysis")
    
    sources_of_interference: List[str] = Field(default=[], description="List of identified interference sources (e.g. 'SSB Antenna 0.5m from GPS', 'Inverter 2m from Radar')")
    
    affected_systems: List[str] = Field(default=[], description="Which systems experience issues (GPS, Radar, VHF, etc.)")
    
    interference_frequency_bands: Optional[List[str]] = Field(None, description="Freq bands affected (e.g. '1.2 GHz L-Band', '1.6 GHz L-Band')")
    
    measured_signal_strength_dbm: Optional[List[float]] = Field(None, description="Measured signal strength in dBm at various points")
    measured_noise_floor_dbm: Optional[List[float]] = Field(None, description="Noise floor measurements")
    
    shielding_assessment: Optional[str] = Field(None, description="Evaluation of cable shielding, ferrite usage, etc.")
    
    antenna_separation_distances: Optional[str] = Field(None, description="Current separation between antennas")
    cable_separation_status: Optional[str] = Field(None, description="How well cables are separated (good/fair/poor)")
    
    grounding_quality: Optional[str] = Field(None, description="Assessment of grounding/earthing (excellent/good/fair/poor)")
    
    identified_problems: List[str] = Field(default=[], description="Specific EMV issues found")
    
    recommended_fixes: List[str] = Field(default=[], description="Actions to reduce/eliminate EMI (e.g. 'Add ferrite cores', 'Separate cables', 'Move antenna')")
    
    estimated_fix_cost_eur: Optional[float] = Field(None, description="Total estimated cost of EMV improvements")
    
    remediation_priority: Optional[str] = Field(None, description="IMMEDIATE, HIGH, MEDIUM, LOW based on impact")
    
    follow_up_analysis_date: Optional[datetime] = Field(None, description="When next EMV check is recommended")
    
    notes: Optional[str] = Field(None, description="Additional technical notes")


### Anhang N: SoftwareVersion

```python
from pydantic import BaseModel, Field
from typing import Optional, List
from datetime import datetime

class SoftwareVersion(BaseModel):
    model_config = {"from_attributes": True}
    
    device_id: str = Field(..., description="Reference to device (Plotter, Radar Module, etc.)")
    
    firmware_version: str = Field(..., description="Current firmware version string (e.g. '4.5.2.1001')")
    firmware_release_date: Optional[datetime] = Field(None, description="When this version was released")
    
    software_build_number: Optional[str] = Field(None, description="Internal build identifier")
    
    installed_date: datetime = Field(..., description="When firmware was installed on device")
    installation_method: Optional[str] = Field(None, description="How was it installed (SD Card, USB, OTA, etc.)")
    
    previous_version: Optional[str] = Field(None, description="What version was running before this update")
    update_from_date: Optional[datetime] = Field(None, description="When previous version was installed")
    
    known_issues: Optional[List[str]] = Field(None, description="Documented issues in this version (thermal shutdown bug, GPS hang, etc.)")
    
    critical_security_patches: Optional[List[str]] = Field(None, description="Security fixes included in this version")
    
    language_localization: Optional[str] = Field(None, description="Language set (German, English, etc.)")
    
    update_available: bool = Field(default=False, description="Is a newer version available")
    newer_version: Optional[str] = Field(None, description="Version number of available update")
    update_criticality: Optional[str] = Field(None, description="CRITICAL, HIGH, MEDIUM, LOW, OPTIONAL")
    
    changelog_url: Optional[str] = Field(None, description="Link to release notes")
    
    update_notes: Optional[str] = Field(None, description="Special instructions for next update")
    
    backup_before_update: bool = Field(default=True, description="Should settings be backed up before update")


### Anhang O: WinterizationChecklist

```python
from pydantic import BaseModel, Field
from typing import Optional, Dict, List
from datetime import datetime

class WinterizationChecklist(BaseModel):
    model_config = {"from_attributes": True}
    
    checklist_id: str = Field(..., description="Unique ID (e.g. 'WINTER_2024_BOAT_001')")
    boat_id: str = Field(..., description="Reference to boat")
    
    season_year: int = Field(..., description="Year of winter season (e.g. 2024 for 2024-2025 winter)")
    winterization_start_date: datetime = Field(..., description="When winterization process began")
    winterization_completion_date: Optional[datetime] = Field(None, description="When process was finished")
    
    # Battery checks
    battery_charged_to_percent: Optional[int] = Field(None, description="Battery charge level before storage (target: 80-90%)")
    battery_charging_method: Optional[str] = Field(None, description="How battery was charged (solar, charger, etc.)")
    maintenance_charger_connected: bool = Field(default=False, description="Is trickle/maintenance charger installed")
    battery_monitoring_interval_days: int = Field(default=30, description="Check battery every X days during winter")
    
    # Humidity control
    silica_gel_installed: bool = Field(default=False, description="Silica gel desiccant packs in electronics box")
    silica_gel_capacity_grams: Optional[int] = Field(None, description="Total capacity of silica gel installed")
    humidity_target_percent: int = Field(default=50, description="Target humidity inside electronics enclosure")
    humidity_monitoring: bool = Field(default=False, description="Is humidity sensor installed to monitor")
    
    # Cable and connector protection
    connector_caps_installed: bool = Field(default=False, description="All exposed connectors have protective caps")
    cable_ties_checked: bool = Field(default=False, description="Cable routing is secure and won't chafe during storage")
    corrosion_preventive_applied: bool = Field(default=False, description="WD-40 or equivalent applied to stecker")
    
    # Antenna protection
    antenna_covers_installed: bool = Field(default=False, description="Protective covers on antennas")
    antenna_de_icers_ready: Optional[str] = Field(None, description="Type of de-icer available if needed")
    
    # Software backup
    system_backup_made: bool = Field(default=False, description="Plotter settings, routes, user data backed up")
    backup_location: Optional[str] = Field(None, description="Where backup is stored (USB, SD, cloud, etc.)")
    backup_verification: bool = Field(default=False, description="Backup was tested/verified readable")
    
    # Firmware updates
    firmware_updates_pending: bool = Field(default=False, description="Should firmware be updated before/after winter")
    firmware_updates_list: Optional[List[str]] = Field(None, description="Which devices need updating")
    
    # Documentation
    documentation_organized: bool = Field(default=False, description="Manuals, warranty, contacts organized and stored")
    emergency_contact_list_prepared: bool = Field(default=False, description="Repair/warranty contacts readily available")
    
    # General readiness
    all_checks_completed: bool = Field(default=False, description="All checklist items done")
    technician_name: Optional[str] = Field(None, description="Who performed winterization")
    
    notes: Optional[str] = Field(None, description="Special considerations, issues, or next steps")


### Anhang P: CalibrationRecord

```python
from pydantic import BaseModel, Field
from typing import Optional, List, Literal
from datetime import datetime

class CalibrationRecord(BaseModel):
    model_config = {"from_attributes": True}
    
    calibration_id: str = Field(..., description="Unique ID (e.g. 'CAL_2024_COMPASS_001')")
    device_id: str = Field(..., description="Reference to device being calibrated")
    device_type: str = Field(..., description="Type of device (GPS, Compass, Radar, Sounder, etc.)")
    
    calibration_date: datetime = Field(..., description="When calibration was performed")
    calibration_method: str = Field(..., description="Method used (Circular route, Known reference points, Factory reset, etc.)")
    
    # Pre-calibration readings
    pre_calibration_reading: Optional[str] = Field(None, description="Measurement/bearing before calibration")
    pre_calibration_error_degrees: Optional[float] = Field(None, description="Known error before (e.g. Compass off by +12°)")
    
    # Calibration process
    reference_points_used: Optional[List[str]] = Field(None, description="Landmarks/waypoints used as reference")
    number_of_measurements: Optional[int] = Field(None, description="How many measurements taken")
    conditions_during_calibration: Optional[str] = Field(None, description="Weather, sea state, interference (clear day, calm, no traffic)")
    
    # Post-calibration results
    post_calibration_reading: Optional[str] = Field(None, description="Measurement after calibration")
    post_calibration_error_degrees: Optional[float] = Field(None, description="Residual error after calibration (goal: <2°)")
    
    calibration_successful: bool = Field(default=True, description="Did calibration meet acceptance criteria")
    
    # Specific calibration data (varies by device type)
    compass_deviation_table: Optional[Dict[str, float]] = Field(None, description="Heading vs. Deviation (e.g. {'0': 0.5, '90': -1.2, '180': 0.8, '270': -0.3})")
    gps_reference_position: Optional[str] = Field(None, description="Known position used for GPS verification (lat/lon)")
    radar_range_calibration_nautical_miles: Optional[float] = Field(None, description="Range setting verified against known distance")
    
    # Technician and environment
    technician_name: Optional[str] = Field(None, description="Who performed calibration")
    technician_certification: Optional[str] = Field(None, description="Relevant certifications")
    equipment_used_for_calibration: Optional[List[str]] = Field(None, description="Tools/instruments (compass, GPS unit, range finder, etc.)")
    
    # Next calibration
    recommended_recalibration_interval_months: Optional[int] = Field(None, description="e.g. 12, 24, 36 months")
    next_calibration_due: Optional[datetime] = Field(None, description="Calculated next calibration date")
    
    notes: Optional[str] = Field(None, description="Special observations or issues found during calibration")


### Anhang Q: CorrosionAssessment

```python
from pydantic import BaseModel, Field
from typing import Optional, List, Literal
from datetime import datetime

class CorrosionSeverity(str, Enum):
    NONE = "none"  # No visible corrosion
    LIGHT = "light"  # Surface oxidation, cosmetic only
    MODERATE = "moderate"  # Visible corrosion, functional impact minor
    SEVERE = "severe"  # Significant corrosion, functionality at risk
    CRITICAL = "critical"  # Corrosion threatens structural/electrical integrity

class CorrosionAssessment(BaseModel):
    model_config = {"from_attributes": True}
    
    assessment_id: str = Field(..., description="Unique ID (e.g. 'CORR_2024_MAST_001')")
    boat_id: str = Field(..., description="Reference to boat")
    location_assessed: str = Field(..., description="Where on boat (Mast-top, Helm station, Battery compartment, etc.)")
    
    assessment_date: datetime = Field(..., description="When this assessment was made")
    
    components_inspected: List[str] = Field(..., description="What was checked (Antenna stecker, Cable insulators, Connector pins, etc.)")
    
    corrosion_type: Optional[str] = Field(None, description="Type of corrosion found (white oxidation, green patina, salt bloom, rust, etc.)")
    
    corrosion_sources: List[str] = Field(default=[], description="Likely causes (saltwater spray, galvanic coupling, moisture, etc.)")
    
    areas_affected: List[str] = Field(default=[], description="Specific parts corroded (e.g. 'Stecker-pins', 'Kabel-Isolierung', 'Mast-Mounting')")
    
    severity_overall: CorrosionSeverity = Field(default=CorrosionSeverity.NONE)
    
    severity_by_area: Optional[Dict[str, str]] = Field(None, description="Severity for each area (e.g. {'GPS-Stecker': 'light', 'Radar-Kabel': 'moderate'})")
    
    # Assessment findings
    moisture_present: bool = Field(default=False, description="Any evidence of moisture or water intrusion")
    delamination_visible: bool = Field(default=False, description="GFK delamination or surface separation")
    crevice_corrosion_risk: bool = Field(default=False, description="High risk due to narrow gaps/crevices")
    
    protection_methods_in_place: Optional[List[str]] = Field(None, description="Current protection (WD-40 treatment, wax coating, paint, etc.)")
    protection_effectiveness: Optional[str] = Field(None, description="How well current methods are working (good/fair/poor)")
    
    # Recommended actions
    immediate_action_required: bool = Field(default=False, description="Does corrosion threaten safety/function")
    recommended_treatment: Optional[List[str]] = Field(None, description="e.g. ['Clean with brush', 'Apply WD-40', 'Replace connector', 'Re-coat with epoxy']")
    
    treatment_applied: Optional[str] = Field(None, description="What was actually done")
    treatment_date: Optional[datetime] = Field(None, description="When treatment was applied")
    treatment_effectiveness: Optional[str] = Field(None, description="Did treatment work (yes/partial/no)")
    
    follow_up_inspection_interval_months: int = Field(default=6, description="How often to re-inspect this area")
    next_inspection_due: Optional[datetime] = Field(None, description="Calculated next inspection date")
    
    photos: Optional[List[str]] = Field(None, description="File paths to photos documenting corrosion")
    
    notes: Optional[str] = Field(None, description="Technical observations and recommendations")


### Anhang R: ElectronicsSystemScore

```python
from pydantic import BaseModel, Field
from typing import Optional, Dict, List
from datetime import datetime

class ElectronicsSystemScore(BaseModel):
    model_config = {"from_attributes": True}
    
    score_id: str = Field(..., description="Unique ID (e.g. 'SCORE_2024_BOAT_001')")
    boat_id: str = Field(..., description="Reference to boat")
    boat_class: str = Field(..., description="Boat classification (production_small, semi_custom, etc.)")
    
    assessment_date: datetime = Field(..., description="When comprehensive assessment was made")
    assessor_name: Optional[str] = Field(None, description="Name of technician")
    
    # Component condition scores (0-100, 100 = perfect)
    gps_condition_score: Optional[int] = Field(None, description="GPS system health (0-100)")
    radar_condition_score: Optional[int] = Field(None, description="Radar system health (0-100)")
    compass_condition_score: Optional[int] = Field(None, description="Compass system health (0-100)")
    radio_condition_score: Optional[int] = Field(None, description="Radio systems health (0-100)")
    autopilot_condition_score: Optional[int] = Field(None, description="Autopilot health (0-100)")
    sounder_condition_score: Optional[int] = Field(None, description="Depth sounder health (0-100)")
    display_condition_score: Optional[int] = Field(None, description="Display/plotter health (0-100)")
    power_system_condition_score: Optional[int] = Field(None, description="Battery + charging system health (0-100)")
    cabling_connector_score: Optional[int] = Field(None, description="Cabling and connectors health (0-100)")
    antenna_condition_score: Optional[int] = Field(None, description="Antenna systems health (0-100)")
    
    # Categorical scores (0-100)
    corrosion_risk_score: int = Field(..., description="Overall corrosion exposure (0=very low, 100=extreme)")
    maintenance_compliance_score: int = Field(..., description="How well maintenance has been kept up (0=never, 100=meticulous)")
    emv_compatibility_score: int = Field(..., description="EMV/EMI status (0=severe problems, 100=excellent isolation)")
    firmware_up_to_date_score: int = Field(..., description="Software/firmware currency (0=very old, 100=latest)")
    documentation_score: int = Field(..., description="Quality of records, manuals, maintenance logs (0=none, 100=complete)")
    
    # Aggregate scores
    overall_electronics_health_score: int = Field(..., description="Weighted average of all component scores (0-100)")
    
    safety_risk_level: str = Field(..., description="CRITICAL, HIGH, MEDIUM, LOW, EXCELLENT")
    operational_readiness: str = Field(..., description="FULLY_OPERATIONAL, LIMITED, DEGRADED, NON_OPERATIONAL")
    
    # Risk factors
    identified_risks: List[str] = Field(default=[], description="Specific issues that lower score (e.g., 'Antenna connection corroded', 'Battery near end-of-life')")
    
    # Recommendations by priority
    critical_recommendations: Optional[List[str]] = Field(None, description="Must do immediately (safety/functionality)")
    high_priority_recommendations: Optional[List[str]] = Field(None, description="Should do within 1 month")
    medium_priority_recommendations: Optional[List[str]] = Field(None, description="Recommended within 3 months")
    low_priority_recommendations: Optional[List[str]] = Field(None, description="Preventive or nice-to-have")
    
    estimated_total_maintenance_cost_eur: Optional[float] = Field(None, description="Estimated cost to address all recommendations")
    estimated_timeline_months: Optional[int] = Field(None, description="How long to implement all recommendations")
    
    # Score trends
    previous_score_date: Optional[datetime] = Field(None, description="Date of last assessment")
    previous_overall_score: Optional[int] = Field(None, description="Overall score from last assessment")
    score_trend: Optional[str] = Field(None, description="IMPROVING, STABLE, DECLINING")
    
    # Next assessment
    recommended_reassessment_months: int = Field(default=12, description="How often full assessment recommended")
    next_full_assessment_due: Optional[datetime] = Field(None, description="Calculated next assessment date")
    
    notes: Optional[str] = Field(None, description="Summary analysis and strategic recommendations")
```

---

**Dateiende — Anhang I–R (Pydantic v2 Modelle abgeschlossen)**

Diese 10 Datenmodelle decken die wichtigsten Elektronik-Diagnosevorgänge ab:
- **ElectronicComponent**: Bestandsverwaltung aller Bordelektronik
- **MaintenanceRecord**: Wartungshistorie und Planung
- **FaultDiagnosis**: Fehleranalyse und Entscheidungsfindung
- **ConnectorAssessment**: Stecker und Kabelzustand
- **EMVAnalysis**: Elektromagnetische Verträglichkeit
- **SoftwareVersion**: Firmware-Management
- **WinterizationChecklist**: Winterlagerungs-Vorbereitung
- **CalibrationRecord**: Kalibrierungen (GPS, Kompass, Radar)
- **CorrosionAssessment**: Korrosions-Monitoring
- **ElectronicsSystemScore**: Gesamt-Gesundheitsscore

**Alle Modelle verwenden Pydantic v2** mit `model_config = {"from_attributes": True}` und nie klassisches `Config`-Format.

---

## 13. Erweiterte Implementierungsrichtlinien für AYDI Electronics Module

### 13.1 Datenerfassung und Pflege

**Workflow bei neuer Yacht-Elektronik-Analyse:**

1. **Bestandsaufnahme (15 min):** Alle Komponenten mit ElectronicComponent-Modell erfassen. Seriennummern, Installationsdatum, Firmware-Versionen notieren.

2. **Schnell-Diagnose (10 min):** Visual inspection, Spannungs-Messung, Signal-Prüfung. ConnectorAssessment für alle Hauptstecker.

3. **Historische Daten (5 min):** Wartungsunterlagen einsammeln. MaintenanceRecord für letzte 3 Jahre erfassen (soweit vorhanden).

4. **Risiko-Bewertung (20 min):** EMVAnalysis, CorrosionAssessment, FaultDiagnosis für bekannte Probleme.

5. **Scoring (10 min):** ElectronicsSystemScore berechnen basierend auf allen eingegangenen Daten.

**Gesamt-Aufwand für Vollanalyse:** ~60 Minuten bei vollständiger Dokumentation.

### 13.2 Konfidenz-Scoring und Unsicherheit

Jede Messung in AYDI Electronics trägt ein Konfidenz-Level:

- **measured** (95–100%): Direkt gemessen mit Multimeter oder Prüfgerät
- **calculated** (90–95%): Aus gemessenen Werten abgeleitet (z.B. Ladestrom = Spannung ÷ Widerstand)
- **visual_high** (80–90%): Klare Sichtprüfung ohne mehrdeutigkeit (z.B. "Grüner Belag = Korrosion")
- **visual_medium** (60–79%): Sichtprüfung mit etwas Unsicherheit (z.B. "Möglicher Wasser-Eintritt, aber nicht sicher")
- **estimated** (40–59%): Auf Basis von Typwerte und Boot-Klasse geschätzt (z.B. "Durchschnittlicher Stromverbrauch für 10m Segelboot")
- **benchmark** (70–80%): Aus aggregierten Industrie-Daten (z.B. "Typical lifespan of capacitor: 10–15 years")

**Regel:** Wenn Konfidenz <50%, Modul gibt `{"available": false, "reason": "Nicht genug Daten für zuverlässige Diagnose"}` zurück.

### 13.3 Integration mit AYDI Hauptsystem

Das Electronics Knowledge Module ist part of the **Strukturiert-Pipeline (Pipeline A)**. Es wird aufgerufen von:

- **Route:** `POST /api/v1/analysis/electronics`
- **Input:** Boat specs + optional component list + optional photos
- **Output:** ElectronicsSystemScore + FaultDiagnosis array + MaintenanceRecommendations

**Abhängigkeiten:**
- Bootstraps von `boat_class` (aus Hauptanalyse)
- Nutzt optionale Bilder von Antennen / Stecker (über Vision API)
- Feeds Structural Module (Batterie-Platzierung affects structural safety)
- Feeds Cost Module (Elektronik-Ersatzteil-Kosten)

**Versioning:** Electronics Knowledge Module wird mit Git-Tag versioned (e.g., `electronics-v2.1.3`). Bei jedem ElectronicsSystemScore wird die Modul-Version gespeichert (`knowledge_module_version: "v2.1.3"`).

### 13.4 German Terminology Standardization

Alle User-facing Output im Electronics Module muss konsistent German sein:

| Englisch (Code) | Deutsch (UI) | Kontext |
|---|---|---|
| GPS | GPS-Empfänger | Formal, längere Form bevorzugt |
| Compass | Kompass oder Kompass-Sensor | "elektronischer Kompass" wenn präzise |
| Radar | Radar | Meist ungeändert |
| Sounder | Echolot oder Fischfinder | Kontext-abhängig |
| Power System | Stromsystem oder Bordnetz | Formal |
| Connector | Stecker oder Verbinder | Stecker bevorzugt für maritim |
| Corrosion | Korrosion | Ungeändert |
| Maintenance | Wartung | Ungeändert |
| Fault | Fehler oder Mangel | "Befund" bei diagnostischen Ergebnissen |
| Calibration | Kalibrierung | Ungeändert |
| Firmware | Firmware | Ungeändert (Software-Firmwares sind Anglizismus, ok) |
| EMI/EMV | EMV (Elektromagnetische Verträglichkeit) | EMV ist Standard in DE |

### 13.5 Integrationsbeispiel: Mini-Analyseablauf

```
User: "Ich hab ein 10m Segelboot in der Nordsee, GPS funktioniert manchmal nicht"

System:
1. Boat Class Detection: production_medium (10m Segelboot)
2. Call Electronics Analysis:
   - boat_class: production_medium
   - reported_problem: "GPS sporadisch offline"
   - optional: photos von Antenne
   
3. Analysis Engine:
   - Structured Diagnostics: Kabel-Längen, Standard-Fehlerquellen (Pipeline A)
   - Visual Analysis: Falls Fotos vorhanden, Vision-API auf Antenne/Stecker (Pipeline B)
   - Fused Score: ElectronicsSystemScore
   
4. Output (German):
   "GPS-Empfänger-Diagnose:
    - Wahrscheinliche Ursache: Wasser-Eindringung in Stecker (confidence: high)
    - Empfehlung: Stecker reinigen + WD-40 Behandlung
    - Kosten: €15–30 (Material)
    - Wenn nicht behoben: Kabel austauschen (€80–150)"
```

### 13.6 Fehlerbehandlung und Grenzen

**Szenarien, wo Electronics Module sagt "Nicht beurteilbar":**

1. **Keine Hardware-Spezifikationen vorhanden** → Kann keine Typwerte-basierte Schätzung machen.
2. **Zu viele unbekannte Komponenten** → Boat ist Frankenstein mit Mix von alten + neuen Teilen, kein klares Muster.
3. **Fotos zu schlecht** (zu dunkel, Antenne nicht sichtbar) → Vision-Pipeline schlägt fehl.
4. **Keine Wartungshistorie** → Kann "maintenance_compliance_score" nicht berechnen, bleibt offen.
5. **Konfidenz-Schwelle unterschritten** → Wenn >40% der kritischen Messungen fehlen.

In allen Fällen: **Suggestion für Benutzer generieren**, was noch erforderlich ist:
- "Installieren Sie Spannungsprüfer und messen Sie Batterie-Spannung"
- "Fotografieren Sie bitte die GPS-Antenne von oben"
- "Sammeln Sie die Wartungsunterlagen der letzten 3 Jahre"

### 13.7 Wiederkehrende Überprüfungen (Monitoring)

Für längerfristige Bootnutzer: **ElectronicsSystemScore sollte halbjährlich neu berechnet werden.**

Änderungen zu monitoren:
- Firmware-Updates (neue Versionen?)\
- Batterie-Kapazität-Degradation (Säge-Zahn-Muster?)
- Korrosions-Fortschritt (jährlich in Salzwasser)
- Wartungs-Compliance (werden Intervalle eingehalten?)

**Notification-Rules:**
- Wenn `safety_risk_level` von MEDIUM auf HIGH springt → Alert senden
- Wenn `maintenance_compliance_score` unter 50% fällt → Erinnerung
- Wenn Batterie-Alter >5 Jahre → Warnung (Kapazitätsverlust zu erwarten)
- Wenn Firmware >2 Jahre alt → Hinweis (Updates verfügbar?)

### 13.8 Kosten-Schätzung für Electronics-Reparaturen

Die Cost Pipeline nutzt Electronics SystemScore für Break-down:

**Typische Kostenrahmen (EUR, 2024):**

| Komponente/Reparatur | Klein (DIY) | Mittel (Werkstatt) | Groß (Austausch) |
|---|---|---|---|
| Antenne reinigen/reparieren | €10–50 | €50–200 | €150–500 |
| Stecker reinigen/austausch | €5–30 | €30–100 | €80–200 |
| Kabel reparatur/austausch | €20–100 | €100–300 | €200–800 |
| GPS-Modul Reparatur | €100–300 | €300–800 | €600–1500 |
| Radar-Modul Reparatur | €200–500 | €500–2000 | €1500–5000 |
| Kompass-Kalibrierung | €0–50 | €100–300 | N/A |
| Autopilot Service | €150–400 | €400–1000 | €1000–3000 |
| Batterie Austausch (100Ah) | €300–500 | €400–700 | €600–1200 |
| Ladeanlage Service | €50–200 | €200–600 | €600–1500 |
| Plotter-Display Repair | €100–300 | €300–800 | €800–2000 |

Diese Werte werden dynamisch in Cost Module eingespeist, je nachdem welche Reparaturen ElectronicsSystemScore empfiehlt.

### 13.9 Saisonale Wartungs-Anpassung

Abhängig von Boot-Nutzungsprofil ändern sich Wartungsintervalle:

**Segelboot Küstenfahrt (April–Oktober, 50h/Saison):**
- Monatliche Sichtprüfung: Antennen, Stecker
- Quartalsweise: Batterie-Check, Kabel-Kontrolle
- Halbjährlich: Kalibrierung (GPS, Kompass)
- Jährlich: Vollständige Revision vor Saison

**Motorboot intensive Nutzung (März–Oktober, 200h/Saison):**
- Wöchentliche Blitzprüfung: Stromversorgung, Bildschirm
- 2x monatlich: Batterie-Spannung, Antennensignale
- Monatlich: Stecker-Inspektion, EMI-Check
- Vierteljährlich: Firmware, Kalibrierung
- Halbjährlich: Vollständige Diagnose

**Charterboot intensive Nutzung (ganzjährig, 500h/Jahr):**
- Täglich: Schnell-Check (Signal ok? Batterie ok?)
- Nach jeder Fahrt: Salzwasser-Spülung (falls Seewasser-Kontakt)
- Wöchentlich: Gründliche Inspektionen
- Monatlich: Diagnostische Tests
- Vierteljährlich: Vollständige Revision
- Halbjährlich: EMV-Analyse
- Jährlich: Austausch kritischer Verschleiß-Teile

---

## 14. Notfall- und Troubleshooting-Checklisten

### 14.1 Notfall-Verfahren: Elektronik-Totalausfall (Black-Out)

**Symptom:** Alle Elektronik ist dunkel/aus, keine Anzeigen, keine Geräusche. Boot ist "elektronisch blind".

**Sofort-Maßnahmen (erste 60 Sekunden):**
1. **Batterie-Schalter überprüfen:** Ist der Hauptschalter an? (oft unter Kommandobrücke versteckt). Wenn aus: Einschalten.
2. **Schalter neustart:** Aus → 5 sec → An (Hard Reset).
3. **Visuelle Kontrolle:** Gibt es Rauchwolke, brennender Geruch? Wenn ja: sofort Stromversorgung trennen, Feuer-Extinguisher bereit.

**Wenn nach 60 Sekunden immer noch dunkel:**
4. **Batterie-Spannungsprüfung:** Mit Multimeter an Batterie-Klemmen messen.
   - 0V → Batterie tot oder Sicherung geplatzt.
   - 5–10V → Batterie tiefentladen oder Kabel-Unterbrechung.
   - 12V normal, aber Elektronik bleibt dunkel → Stromverteil-Panel Problem.

5. **Sicherungen überprüfen:** Panel Sicherungs-Halter überprüfen. Ist eine Sicherung dunkel/verbrannt? Wenn ja: austauchen mit identischer Amperezahl. Wenn wieder ausfällt: Kurzschluss dahinter — nicht erneut versuchen, Werkstatt.

6. **Notstrom-Batterie aktivieren** (falls vorhanden): Separate Batterie für GPS/Kompass/Funkanlage kann manuelle Umschaltung haben.

**Langfristige Lösung:**
- Batterie laden (solar, Motor-Generator, externe Ladegerät).
- Elektronik schrittweise wieder hochfahren (zuerst Plotter, dann Radar, dann Funk).
- Jedes Gerät auf Fehler-Meldungen prüfen.

### 14.2 Checkliste: Vor längerer Segelfahrt (>3 Tage)

- [ ] Batterie voll geladen? (12.8–13V oder besser)
- [ ] Alle Antennensignale ok? (GPS grün, Radar ok, VHF-Empfang ok)
- [ ] Alle Stecker sichtprüfen auf Wasser/Korrosion?
- [ ] Firmware aktuell? (oder mindestens <2 Jahre alt)
- [ ] Routen ins Navigationssystem geladen?
- [ ] Backup-Routen auf SD-Karte gespeichert?
- [ ] Kompass letztens kalibriert? (< 6 Monate)
- [ ] Thermische Überprüfung: Elektronik-Box nicht zu heiß?
- [ ] WD-40 Spray an Bord? (für Notfall-Stecker-Behandlung)
- [ ] Papierseekarten an Bord? (Fallback bei Electronics-Ausfall)
- [ ] Funkanlage getestet? (Kanäle überprüft, Batterien ok)
- [ ] Autopilot getestet? (kompass calibrated, kann längere Zeit laufen?)
- [ ] Batterie-Spannung bei Motorstart normal? (sollte nicht unter 10V fallen)
- [ ] Alle Geräte starten korrekt neu? (Test: Ausschalten und Anschalten)

### 14.3 Schnell-Referenz: Was man immer an Bord haben sollte

**Notfall-Kit für Elektronik-Reparatur (minimalistisch, <500g):**

1. Multimeter (digital, klein, 100g) — Preis: €15–30
2. Kleine Schraubendreher-Set (Schlitz + Phillips, 50g) — €5–10
3. WD-40 Spray (200ml, 200g) — €4–8
4. Isolier-Klebeband (1 Rolle, 20g) — €1–2
5. Schrumpfschläuche (Set, klein, 10g) — €3–5
6. Ersatz-Sicherungen (5A, 10A, 15A, 20A je 2 Stück, 50g) — €3–5
7. USB-Kabel A-B (2m, 50g) — €3–8
8. Ersatz-Stecker-Kappe für Antenne (10g) — €2–3
9. Feines Sandpapier P220 (1 Blatt, 1g) — €0.50
10. Lötkolben-Stift (kleine Löt-Reise-Set, 100g) — €10–15

**Gesamtgewicht:** ~500g
**Gesamtkosten:** ~50–100 EUR
**Platzbedarf:** Schuhkarton-Größe

Diese Minimalausrüstung reicht für ~80% häufiger Bordprobleme (Stecker-Kontakt, Sicherung, kleine Kabel-Reparatur).

### 14.4 Wartungs-Kalender Muster (Segelboot 12m, Ostsee)

```
JANUAR - FEBRUAR (Winter)
  □ Batterie Erhaltungs-Ladung überprüfen (monatlich)
  □ Elektronik-Box Feuchtigkeits-Kontrolle (silica gel prüfen)
  □ Firmware Update Planung (falls neue Version verfügbar)

MÄRZ (Frühjahrs-Vorbereitung)
  □ Alle Antennen auf Schäden überprüfen
  □ GPS-Empfänger Funktionsprüfung (min. 10 min Signal-Akquisition)
  □ Kompass-Kalibrierung (falls nicht innerhalb 6 Monaten)
  □ Radar-Antenne auf Eis/Schmutz kontrollieren
  □ Batterie Ladezustand testen (sollte schnell auf 13V geladen werden)
  □ Alle Stecker: WD-40 Behandlung

APRIL (Start-Up)
  □ Elektronik Systemtest: Alle Geräte vollständig durchlaufen
  □ GPS/Radar/Kompass Live-Test (auf Testfahrt)
  □ Funk-Sprechfunk Test (über KW oder UKW)
  □ Autopilot-Funktionsprüfung (Mind. 1 Std. Betrieb)
  □ Schnelldiagnose mit Multimeter (Spannungen prüfen)

MAI–SEPTEMBER (Segelsaison)
  □ Vor jeder Fahrt: Schnell-Check (Signal ok? Batterie ok?)
  □ Nach Salzwasser-Fahrt: Süßwasser-Spülung der Antennen
  □ Monatlich: Tiefere Inspektionen (Kabel, Stecker-Kontakte)
  □ Alle 2 Monate: Aktuelles Firmware überprüfen (z.B. erste Samstag im Monat)
  □ Bei schlechtem Wetter: Elektronik-Box Belüftung überprüfen

OKTOBER (Herbst-Wartung)
  □ Gründliche Prüfung aller Kabel und Antennen
  □ Kompass ggfs. neu kalibrieren (vor lange Winterfahrten)
  □ Batterie Kapazitäts-Test (belastbar?)
  □ Firmware Final Update (vor Winterlagerung)
  □ Dokumentation: Wartungsprotokoll aktualisieren

NOVEMBER–DEZEMBER (Winterschlaf)
  □ Elektronik Backup erstellen (Routen, Einstellungen auf USB)
  □ Stecker-Schutzkappe anbringen
  □ Batterie-Erhaltungs-Ladegerät aktivieren
  □ Silica-Gel Feuchtigkeitsregler in Box platzieren
  □ Monatlich: Batterie-Spannung kontrollieren (sollte 12.5–13V bleiben)
```

---

## 15. Weiterführende Ressourcen und Referenzen

### 15.1 Normen und Regelwerke

- **ISO 12217-2:2022** — Segelfahrzeuge, Stabilitätsanforderungen und Gewichtsverteilung
- **ISO 9094:2015** — Freizeitfahrzeuge, Brandschutz
- **ISO 12216:2020** — Freizeitfahrzeuge, Luken und Fenster
- **ISO 11812:2020** — Cockpit-Design und Drainage
- **EN 60945** — IEC 60945:2002 — Maritime Navigation und Funk-Ausrüstung, Allgemeine Anforderungen
- **CE Richtlinie 2013/53/EU** — Freizeitfahrzeuge Zulassung
- **NMEA Standards:** 0183 (seriell), 2000 (CAN-Bus), beide weltweit verfügbar bei NMEA.org

### 15.2 Fachpublikationen und Handbücher

- **"Yacht Electrical Systems" by Dennis Capelo** — Englisch, Best Practice Standard
- **"The Complete Sailing Manual" by Steve Sleight** — Großbritannien, praktische Navigation
- **Raymarine SEATALK Dokumentation** — Proprietary Netzwerk-Standard
- **Garmin NMEA 2000 Integration Guide** — Offizielle Dokumentation
- **Furuno Radar Maintenance Manuals** — Hersteller-spezifisch

### 15.3 Online-Tools und Datenbanken

- **NMEA.org** — Official NMEA Standards Library
- **WMM2025** — World Magnetic Model, kostenlos, für Kompass-Kalibrierung
- **OpenSeaMap** — Freie Seenkarten, für Radar-Validierung bei Test
- **IEC TC 80** — Internationale Komitee für maritim-elektrische Standards

---

## 16. Abschließende Notizen und Wartungs-Philosophie

### 16.1 Elektronik-Wartung als Investment

Bootselektronik ist **kein Verschleiß-Material**, sondern **Infrastructure mit Lebensdauer.**

- **Anschaffungskosten:** 5–15% des Boot-Wertes
- **Wartungs-Kosten (20 Jahre):** 20–30% der Anschaffungskosten
- **Wert-Verlust bei Elektronik-Fehler:** −30–40% Bootswert (Second-Hand)

**Konklusion:** €500 Wartung pro Jahr ist eine Versicherung gegen €50.000 Wertverlust.

### 16.2 Häufigste Fehler, die Bootseigner machen

1. **"Mein Boot ist nur 8m, braucht keine Elektronik-Wartung"** → Falsch. Kleine Boote brauchen MEHR Wartung (weniger Puffer, höheres Risiko-Verhältnis).

2. **"Wenn es funktioniert, repariere ich es nicht"** → Prävention kostet 1/10 von Reparatur. Rostiges Stecker wird zur Katastrophe.

3. **"Firmware-Updates sind optional"** → Falsch. Sicherheits-Patches sind Pflicht. 2+ Jahre alte Firmware bedeutet bekannte Bugs.

4. **"Ich trocke die Elektronik mit dem Föhn, das sollte reichen"** → Unzureichend. Korrosion braucht chemische Behandlung (WD-40, Kontakt-Reiniger).

5. **"Kalibrierung ist zu teuer, kann Skipper selbst machen"** → Naja. DIY Kalibrierung oft fehlerhaft (>5° Kompass-Fehler). Fachmann kostet €100–300 aber ist zuverlässig.

### 16.3 Empfohlene Philosophie für Bootseigner

**"Kontinuierliche kleine Wartung statt großer Reparaturen"**

- Monatliche Schnell-Check: 10 Minuten
- Vierteljährliche Tiefe Inspektionen: 1 Stunde
- Jährliche Vollüberholung: 4–8 Stunden

**Ergebnis:** Elektronik lebt 15–20 Jahre statt 8–10 Jahre. Notsituationen werden zur Ausnahme statt Norm.

---

## 17. Detaillierte Komponent-spezifische Wartungsrichtlinien

### 17.1 GPS-Empfänger: Langlebigkeit und Kalibrierung

**Lebensdauer:** 7–12 Jahre bei normaler Nutzung. Hauptverschleiß: Elektrolyt-Kondensatoren in Stromversorgung.

**Kritische Parameter über Lebensdauer zu überwachen:**

| Jahr | Typische Änderung | Wartungs-Aktion |
|------|-------------------|-----------------|
| 0–2 | Keine merkliche Degradation | Routine Reinigung, Firmware-Updates |
| 2–4 | Akquisitions-Zeit +10–20% langsamer | Signal-Schwelle überprüfen, Antenne-Position optimieren |
| 4–6 | Spannungs-Ripple in Stromversorgung sichtbar (Multimeter) | Kondensator-Test, ggfs. Wartung Netzteil |
| 6–8 | Genauigkeit kann auf ±10m degradieren (war ±5m) | Kalibrierung, ggfs. Antenne austauschen |
| 8–10 | Intermittierende Ausfälle, besonders bei schlechtem Wetter | Component assessment, Reparatur oder Austausch erwägen |
| 10+ | Häufige Fehler, reduzierte Zuverlässigkeit | Austausch empfohlen (€200–600) |

**GPS-Antenne Wartung (unabhängig von Empfänger):**

- Antenne-Kabel alle 2 Jahre vollständig inspizieren (Risse, Feuchtigkeit).
- Stecker-Kontakte: alle 6 Monate mit Kontakt-Reiniger (z.B. Kontakt 61) reinigen.
- UV-Belastung: Antenne-Gehäuse alle 3 Jahre mit UV-Schutzwachs behandeln (CRC).
- Antenne-Erneuerung nach 12–15 Jahren (Kunststoff-Degradation).

**GPS-Signalqualität Überwachung:**

Moderne Plotter zeigen oft HDOP (Horizontal Dilution of Precision) oder SNR (Signal-to-Noise Ratio):
- HDOP <1.5: Excellent
- HDOP 1.5–3: Good
- HDOP 3–6: Fair
- HDOP >6: Poor (Position unreliabel)

Wenn HDOP ständig >5: Kabel-Problem, Antenne-Position suboptimal, oder Receiver-Fehler.

### 17.2 Radaranlage: Modul-Lebenszyklus

**Radar-Modul Lifespan:** 10–15 Jahre bei Süßwasser, 8–12 Jahre bei Salzwasser.

**Häufigster Verschleiß-Mechanismus:**
1. **Stromversorgung:** Elektrolyt-Kondensatoren (trocknen aus, besonders bei Hitze). Symptom: brummende Töne im Radar-Empfänger.
2. **Dichtungen:** Antenne-Dichtung wird spröde (UV + Salz). Symptom: Wasser tritt aus Antennen-Basis.
3. **Rotor-Lager:** Drehmotor-Lager verschleißen. Symptom: Antenne dreht ruckelnd, lautes Surr-Geräusch.
4. **Transceiver-Modul:** HF-Verstärker können thermisch altern. Symptom: Reichweite nimmt ab.

**Präventive Wartungs-Strategie:**

**Jahre 0–3:** Routine
- Monatlich: Visuelle Überprüfung der Antenne (Eis, Algen, Beschädigungen)
- Halbjährlich: Radar-Reichweiten-Test (bekannte Distanz, z.B. Landmasse 5 nm weg)
- Jährlich: Firmware-Update überprüfen

**Jahre 3–7:** Überwachung
- Wöchentlich: Signal-Qualität beobachten (gibt es mehr Rauschen?)
- Quartalsweise: Antenne-Drehung prüfen (flüssig oder ruckelig?)
- Halbjährlich: Stromverbrauch messen (sollte konstant sein, nicht ansteigend)
- Jährlich: Temperatur-Messung nach 30 min Betrieb (sollte <50°C sein)

**Jahre 7–10:** Präventive Instandhaltung
- Monatlich: Antennenlager-Geräusch prüfen
- Quartalsweise: Spannungs-Ripple messen (mit Oscilloskop oder gutes Multimeter)
- Halbjährlich: Dichtungs-Sichtprüfung (bei Service)
- Jährlich: Komplette Prüfung von Hersteller-autorisierten Service

**Jahre 10+:** Erneuerung vorbereiten
- Zwei Wochen vor längerer Fahrt: umfassende Diagnose
- Budget für Modul-Austausch einplanen (€1500–5000)
- Falls Austausch nicht geplant: Fehler-Toleranz erhöhen (visuelle Navigation zusätzlich planen)

### 17.3 Autopilot-Systeme: Sensor-Fusion und Kalibrierung

**Autopilot Komponenten:**
1. Lage-Sensor (Kompass + IMU)
2. Kurs-Sollwert (von Plotter)
3. Servo-Motor + Hydraulik-Steuerung
4. Feedback-Sensor (Position)

**Kritische Fehlerquellen:**

| Fehler | Symptom | Behebung |
|--------|---------|----------|
| Schlechte Kompass-Kalibrierung | Autopilot pendelt (±10° oscilliert) | Kompass neu kalibrieren (Schritt 4.4) |
| Servo-Getriebe Verschleiß | Ruck im Steuerwerk, Knarren | Servo-Getriebe ölen oder austauschen |
| Hydraulik-Leck | Autopilot stellt sich nicht ein (Fehler-Code) | Hydraulik-Druck überprüfen, ggfs. Flüssigkeit nachfüllen |
| IMU-Sensor-Drift | Autopilot verliert langsam die Richtung (über 2–3 Stunden) | IMU-Kalibrierung durchführen (erfordert ruhiges Wasser, 15 min) |
| Stecker-Korrosion (IMU-Kabel) | Intermittierende Fehler, Autopilot fällt plötzlich aus | Stecker reinigen, ggfs. Kabel austauschen |

**Autopilot Wartungs-Kalender:**

- **Vor jeder Fahrt:** Funktionsprüfung (5 Minuten Autopilot-Betrieb, sollte gerade Linie fahren)
- **Monatlich:** Kompass-Funktion überprüfen (Hand-Steer vs Autopilot sollte gleiches Ergebnis haben)
- **Halbjährlich:** Servo-Motor Geräusch überprüfen (rau = Verschleiß)
- **Jährlich:** Kompass-Kalibrierung (oder wenn Abweichung >3° bemerkt)
- **Alle 3 Jahre:** Hydraulik-Flüssigkeit überprüfen + nachfüllen (falls nötig)
- **Alle 5 Jahre:** Servo-Getriebe Service (Öl, Dichtungen überprüfen)

### 17.4 Batterie-Altern und Kapazitäts-Überwachung

**Batterie-Degradation nach Zyklus-Zahl:**

Blei-Säure 100 Ah Batterie (Standard-Boot-Batterie):

| Zyklus | Kapazität | Charakteristik |
|--------|-----------|-----------------|
| 0 (Fabrik) | 100% | Ideale Spannung, schnelle Ladung |
| 50 | 98% | Praktisch keine merkliche Änderung |
| 200 | 95% | Ladung dauert leicht länger |
| 500 | 90% | Spannung unter Last etwas niedriger |
| 1000 | 85% | Effektive Nutzbaren-Kapazität sinkt |
| 2000 | 75% | Deutliche Leistungs-Reduktion |
| 3000 | 65% | Batterie sollte spätestens ausgetauscht werden |
| 4000+ | <60% | Batterie nicht mehr zuverlässig |

**Zyklus-Zahl Schätzung:**
- Bei 1 Zyklus pro Woche (Charterboot mit täglichem Laden): 50 Zyklen/Jahr
- Bei 1 Zyklus alle 2 Wochen (regelmäßiger Segler): 25 Zyklen/Jahr
- Bei 1 Zyklus pro Monat (Wochenend-Segler): 12 Zyklen/Jahr

→ **Typische Batterie-Lebensdauer:**
- Charter-Boot: 5–6 Jahre
- Regelmäßiger Segler: 10–12 Jahre
- Wochenend-Boot: 15–20 Jahre

**Batterie-Gesundheit Test (mit Multimeter):**

1. **Ruhespannung** (mindestens 4h nicht geladen/entladen):
   - 12.7–12.9V = Gut
   - 12.4–12.6V = Fair (ca. 75% Kapazität)
   - 12.0–12.3V = Schwach (ca. 50% Kapazität)
   - <12.0V = Kritisch (<25% Kapazität)

2. **Last-Test** (mit Ohm-Messer oder Spannungs-Messungen unter Last):
   - Starte Motor 10 Sekunden lang
   - Spannungs-Abfall sollte nicht mehr als 1.5V sein
   - Abfall >2V = Batterie hat interne Probleme

3. **Lade-Effizienz** (mit Ampere-Messer):
   - Batterie mit Ladegerät laden, Ampere-Aufnahme messen
   - Sollte schnell sinken (von z.B. 50A auf <5A innerhalb 1 Stunde bei Vollladeanlage)
   - Wenn Strom nicht sinkt: Batterie defekt (Kurzschluss in Zelle)

---

## 18. Spezielle Themen: Salzwasser vs. Süßwasser Elektronik

### 18.1 Salzwasser-Elektronik (Korrosions-Kontrolle)

**Salzwasser ist der natürliche Feind von Elektronik:**

Meerwasser ist hochgradig leitend (Salzkonzentration ~35g/L) und führt zu:
- **Galvanische Korrosion** (unterschiedliche Metalle reagieren electrochemisch)
- **Ionen-Migration** (Salzionen wandern und ursachen Kurzschlüsse)
- **Oxidation** (Sauerstoff-Reaktion an Metalloberflächen wird katalysiert)

**Schutzmaßnahmen für Salzwasser-Boote:**

1. **Antennen-Schutz:**
   - Alle Antennenstecker mit schützenden Kappen versehen
   - Nach Salzwasser-Fahrt: Süßwasser spülen + trocknen
   - Antenne-Kabel mit Schrumpfschlauch + UV-Wachs versiegeln

2. **Connector-Behandlung:**
   - Monatlich: WD-40 oder Kontakt-Spray aufsprühen auf alle Stecker
   - Alle 3 Monate: Stecker mit Kontakt-Reiniger (Electrolube oder ähnlich) ausspülen
   - Korrodierte Kontakte: Mit feiner Bürste reinigen, nicht kratzen

3. **Kabel-Schutz:**
   - Stromkabel mit Kunststoff-Schlauch-Ummantelung
   - NMEA-Kabel in separaten Rohr (getrennt von Stromkabel)
   - Alle Kabel-Durchgänge mit Silikon-Dichtmasse versiegeln

4. **Elektronik-Box-Konstruktion:**
   - Belüftungsöffnungen mit feinem Netz (verhindert Salzspray-Eintritt)
   - Regelmäßige Trocknungs-Zyklen (Silica-Gel, Heißluft nach längeren Fahrten)
   - Korrosionsschutz-Wachs auf alle Leiterplatten-Kanten (prophylaktisch)

5. **Batterie-Sicherung:**
   - Salzwasser-Boote brauchen isolierte Batterie-Gehäuse (Kunststoff, nicht Metall)
   - Batterie-Pole mit Korrosionsschutz-Spray behandelt (verhindert white bloom)
   - Batterie-Anschluss-Klemmen aus Messing oder V4A Edelstahl (nicht Kupfer)

### 18.2 Süßwasser-Elektronik (langsamere Korrosion, höhere Elektrolyt-Probleme)

Flussboote und Binnenschiff-Elektronik hat andere Herausforderungen:

1. **Elektrolyt-Kondensator-Austrocknung:**
   - Wärme + niedrige Luftfeuchte in Süßwasser-Regionen führt zu ausgetrockneten Kondensatoren
   - Symptom: Plotter schaltet sich spontan aus bei Wärmestau
   - Prävention: Elektronik-Box aktive Belüftung (Lüfter), Temperatur <45°C halten

2. **Osmotische Blistering (GFK-Antennenmast):**
   - Süßwasser dringt langsamer ein, aber wenn eingdrungen, bricht osmotischer Prozess Gelcoat auf
   - Symptom: Blasen/Wölbungen im Gelcoat rund Antennenmast
   - Prävention: Jährliche UV-Schutz-Versiegelung (CRC Light-Protective)

3. **Stagnante Gewässer (trübe, biologisch aktiv):**
   - Höherer biologischer Bewuchs (Algen, Biofilm)
   - Antenna wird schneller schmutzig, braucht häufiger Reinigung

4. **Ladezustand-Instabilität:**
   - Süßwasser-Boote haben oft variable Ladegerät-Effizienz (wenn Diesel-Propulsion fehlt)
   - Solar-Ladung kann instabil sein (Wolken über Fluss)
   - Prävention: Doppel-Batterie-System mit intelligenter Aufteilung

---

## 19. Techniker-Zertifikation und Schulung

### 19.1 Empfohlene Zertifizierungen für Electronics-Techniker

Für professionelle Wartung von Boot-Elektronik:

1. **NMEA Level 1** (selbst-erklärte Kenntnisse, ca. 40 Stunden)
   - NMEA 0183 und 2000 Grundlagen
   - Diagnose häufiger Fehler
   - Gängigste Hersteller-Systeme

2. **NMEA Level 2** (offizielle Schulung, ca. 120 Stunden)
   - Tiefe Netzwerk-Konfiguration
   - Hersteller-spezifische Zertifizierungen (Garmin, Raymarine, etc.)
   - Diagnose und Reparatur komplexer Systeme

3. **Hersteller-Zertifikation (einzeln):**
   - Garmin Certified Technician (~80 Stunden)
   - Raymarine Authorized Service Center (~100 Stunden)
   - Furuno Technician Course (~60 Stunden)

4. **Electrical Safety Certification** (z.B. ISO 10133 oder national equivalent)
   - Sicherheit beim Umgang mit 12V/24V Systemen
   - Verständnis von EMV und Sicherheits-Standards

### 19.2 Schulungs-Roadmap für Boot-Owner

Falls man seine Elektronik selbst warten möchte (Hobby-Segler):

**Anfänger (Monat 1–3):** 
- Grundlagen Elektrotechnik (Volt, Ampere, Ohm)
- Multimeter richtig nutzen
- Stecker und Kabel identifizieren
- Routine Inspektionen üben

**Fortgeschritten (Monat 4–6):**
- NMEA-Netzwerk-Verstehen
- Kompass-Kalibrierung durchführen
- Kleine Kabel-Reparaturen (Löten, Schrumpfschläuche)
- Batterie-Management

**Experte (Monat 7–12):**
- Firmware-Updates selbst durchführen
- Grundlegende Diagnostik mit Spezial-Tools
- EMV-Probleme erkennen und beheben
- Winterisierung planen und durchführen

---

## 20. Abschließender Überblick: Elektronik-Systemintegration in AYDI

### 20.1 Wie Electronics Module mit anderen AYDI-Modulen interagiert

**Strukturiert Pipeline (Typ A — Hauptsystem):**
```
Boat Specs (LOA, Beam, Cabin-Layout)
    ↓
Electronics Module
    ├→ Component Inventory (ElectronicComponent Models)
    ├→ Fault Diagnosis (häufige Probleme)
    ├→ Maintenance Planning (nächste Inspektionen)
    └→ System Score (0–100 Gesundheit)
    ↓
Cost Module (nutzt Electronics für Reparatur-Budget)
Structural Module (nutzt Electronics für Gewichts-Distribution)
Safety Module (nutzt Electronics für Navigation-Redundanz)
```

**Visual Pipeline (Typ B — optional mit Photos):**
```
Photos von Antenne / Stecker / Elektronik-Box
    ↓
Vision API + Domain Prompts
    ├→ Korrosions-Grade erkennen (light/moderate/heavy)
    ├→ Feuchtigkeits-Anzeichen identifizieren
    └→ Kabel-Zustands-Bewertung
    ↓
Fused mit Structured Daten
    → Genauere CorrosionAssessment + ConnectorAssessment
```

**Integration Beispiel: Vollanalyse einer 14m Segelyacht**

1. User lädt Bootsspecs + 6 Antennenfoto hoch
2. System startet Vollanalyse (AYDI Orchestrator)
3. Electronics Module Tier 2 aufgerufen:
   - Structured: Typische 14m Segelboot Elektronik (GPS, Radar, Kompass, VHF)
   - Visual: Vision API analysiert Antennenfoto → mild corrosion erkannt
   - Fused Score: 72/100 (gut, aber Antennenwartung empfohlen)
4. Cost Module wird nach Electronics Score gefüttert:
   - Geschätzte Reparatur-Kosten: €800–1500 (Antenne-Reinigung + Stecker-Austausch)
5. Service Module nutzt auch: "Antenne sollte vor nächster Fahrt überprüft werden" → Hinweis im Report

### 20.2 Datenfluss für User-Reporting

**Was der User in der AYDI UI sieht:**

```json
{
  "electronics_analysis": {
    "overall_score": 72,
    "safety_risk": "MEDIUM",
    "key_findings": [
      {
        "component": "GPS-Empfänger",
        "status": "OK",
        "confidence": "high",
        "last_check": "2026-05-18"
      },
      {
        "component": "Radar-Antenne",
        "status": "MILD_CORROSION",
        "confidence": "visual_high",
        "recommendation": "Antenne reinigen mit Süßwasser + WD-40 Behandlung"
      },
      {
        "component": "Batterie",
        "status": "OK_BUT_AGING",
        "age_years": 6,
        "estimated_remaining_life": "2-3 Jahre",
        "recommendation": "Budget für Austausch in 2-3 Jahren einplanen"
      }
    ],
    "immediate_actions": [
      "Antennenstecker überprüfen (Sichtprüfung, ca. 5 min)"
    ],
    "recommended_maintenance": [
      "Alle 3 Monate: Antenne + Stecker mit WD-40 behandeln",
      "Jährlich: Vollständige Kompass-Kalibrierung"
    ],
    "estimated_annual_cost": "€200–400 für Routine-Wartung"
  }
}
```

---

## 21. Erweiterte Fehlerbild-Dokumentation: Diagnostik und Reparatur

### 21.1 Fehlerbild 1: Antennenstecker-Korrosion (Salzwasser-Boote)

**Visuelles Erkennungsmerkmal:**
- Grüne oder weiße kristalline Verfärbung am Stecker-Gehäuse
- Oxidation tritt besonders an den Kontaktpunkten auf
- Grünspan-Verfärbung auf Messing-Kontakten deutet auf aktive Korrosion hin
- Weiße "Bloom"-Verfärbung auf Kupfer-Leitern = chemische Oxidation

**Mess-Verfahren:**
1. Ohm-Messer an Stecker ansetzen → sollte <0.1Ω sein zwischen Kontakten
2. Bei >0.5Ω: Kontakt-Widerstand ist zu hoch, Reinigung erforderlich
3. Mit Spannungsmesser unter Last testen: Spannungsabfall >0.5V beim Signal-Durchgang = kritisch

**Reparatur-Kosten-Schätzung:**
| Schweregrad | Maßnahme | Kosten |
|---|---|---|
| Mild (Grünspan oberflächlich) | Kontakt-Reinigungsspray + Schrumpfschlauch | €15–30 |
| Moderat (Kontakte korrodiert, Signal-Verlust intermittierend) | Stecker-Umklemmen, neues Kabel | €80–150 |
| Schwer (Kontakte zerstört, Kurzschluss-Gefahr) | Kompletter Stecker-Austausch + ggfs. Antennenmast-Überprüfung | €200–400 |

**Prävention nach Reparatur:**
- Monatlich WD-40 aufsprühen (bildet hydrophobe Schutzschicht)
- Nach Salzwasser-Fahrt: Süßwasser spülen + trocknen
- Schutzkappen immer verwenden, wenn nicht in Betrieb

---

### 21.2 Fehlerbild 2: GPS-Empfänger-Ausfall (intermittierend)

**Häufigste Ursachen (Häufigkeitsliste):**
1. **HDOP-Drift** (45%): Antenne-Position optimal, aber zu wenig Satelliten-Sicht
2. **Stromversorgung instabil** (25%): Batterie-Spannungs-Spitzen, fehlerhafte Stromleitung
3. **Wasser-Eindringung in GPS-Modul** (15%): Feuchtigkeit im Gehäuse
4. **Firmware-Bug** (10%): Seltene, aber dokumentierte Fehler bei bestimmten Chipset-Versionen
5. **Antennenkabel-Bruch** (5%): Sichtprüfung zeigt keine Schäden, aber interne Drahtrisse

**Diagnostik-Ablauf:**
1. **Schritt 1:** HDOP-Wert prüfen (mit GPS-Empfänger Diags-Menü)
   - HDOP >5 → Antenne-Position überprüfen, Metallobj. in Nähe?
   - HDOP <3 → Problem liegt not bei Satelliten, sondern beim Empfänger selbst

2. **Schritt 2:** Spannungsversorgung messen
   - Sollte 12V ±10% sein, Ripple <0.5V
   - Mit Oscilloskop oder guten Multimeter prüfen, besonders während Motor-Start

3. **Schritt 3:** Firmware-Version auslesen
   - Hersteller-Website konsultieren, ob bekannte Fehler existieren
   - Wenn ja: Firmware-Update durchführen oder Modul austauschen

4. **Schritt 4:** Antennenkabel-Test (mit Ohm-Messer)
   - Koaxial-Kabel sollte Durchgang zeigen (nicht ∞Ω)
   - Wenn offene Leitung (∞Ω): Kabel-Austausch erforderlich

**Typische Fehlermeldungen und Behebung:**
| GPS-Empfänger-Fehlercode | Bedeutung | Sofort-Maßnahme |
|---|---|---|
| "No Signal" (permanent) | Kein GPS-Signal gefunden | Antenne überprüfen, HDOP prüfen, ggfs. Antenne repositionieren |
| "Solution invalid" (nach 30 sec) | Zu wenig gültige Satelliten | Freiere Sicht suchen, oder Antenne höher montieren |
| "Receiver undervolts" | Zu niedrige Stromversorgung | Batterie prüfen, Kabel auf Widerstand kontrollieren |
| "Antenna short circuit" | Antenne-Kurzschluss erkannt | Antennenkabel überprüfen, ggfs. austauschen |

**Reparatur-Kosten:**
| Maßnahme | Kosten |
|---|---|
| Antenne-Umplatzierung | €0 (DIY) |
| Kabel-Austausch | €40–100 |
| Antenne-Upgrade (bessere Sicht) | €150–300 |
| GPS-Modul komplett ersetzen | €400–800 |

---

### 21.3 Fehlerbild 3: Radar-Antenne dreht nicht (Motor stuck)

**Ursachen-Häufigkeit:**
1. **Mechanische Blockade** (50%): Eis, Algen, Verschmutzung auf Rotor
2. **Motor-Getriebe Verschleiß** (30%): Lager ausgeschlossen, Zahnrad-Verschleiß
3. **Stromversorgung zum Motor** (15%): Fehlendes 24V-Signal an Motor-Ansteuerung
4. **Feuchtigkeits-Kurzschluss im Motor** (5%): Wasser-Eindringung, Board-Kurzschluss

**Diagnose-Verfahren:**

**Phase 1: Visuelle Kontrolle (5 Minuten)**
- Antenne von unten beobachten (damit man sieht, ob Welle dreht)
- Bei Stromzuführung: Dreht sich etwas? Oder komplett blockiert?
- Radarmodul selbst: Geräusche beim Hochfahren? (Surr-Sound = Motor aktiv, aber mechanisch blockiert)

**Phase 2: Stromversorgung messen (5 Minuten)**
- Radar-Stromkabel: sollte 24V zeigen, wenn Radar aktiv
- Wenn nur 12V: Stromversorgung fehlerhaft (Kabel-Bruch oder Relais-Fehler)
- Wenn 0V: Radar-Modul nicht unter Strom (Hauptschalter überprüfen)

**Phase 3: Motor-Test (10 Minuten)**
- Mit Spannungsprüfer: Motor-Anschluss sollte Spannung anzeigen, wenn Radar an
- Wenn Spannung da, aber Motor dreht nicht: Mechanische Blockade oder Motor-Fehler
- Mit Ohm-Messer: Motor-Wicklung sollte niedrigen Widerstand zeigen (2–10Ω), nicht offene Leitung

**Reparatur-Schritte:**
1. **Einfach (Verschmutzung):** Antenne mit Süßwasser spülen, vorsichtig von oben reinigen
   - Kosten: €0 (DIY), aber Zeit 30 Minuten

2. **Mittel (Getriebe-Lager):** Lager ölen mit wasserfestem Schmiermittel
   - Kosten: €20–50 Material + 1 Stunde Arbeit

3. **Schwer (Motor/Getriebe Austausch):** Komplette Motor-Einheit ersetzen
   - Kosten: €600–1200 + Arbeitszeit

---

### 21.4 Fehlerbild 4: Kompass-Deviation >5°

**Ursachen (häufigste zuerst):**
1. **Magnetische Störquellen in Nähe** (60%): Metallische Gegenstände, andere magnetische Felder (Leitungen, Motor)
2. **Kompass-Kalibrierung outdated** (25%): Kompass wurde nie kalibriert oder alte Kalibrierung ist überholt
3. **Kompass-Sensor-Fehler** (10%): Sensor-Drift nach Jahren, Firmware-Bug
4. **Metallische Änderungen am Boot** (5%): Neue Antennen, Metallteile hinzugefügt, die Magnetfeld beeinflussen

**Mess-Verfahren:**
- **Mit zwei Kompassen testen:** Einen Hand-Kompass + GPS-Track-Vorwärtsrichtung vergleichen
- Differenz >5°: Deviation vorhanden
- Differenz <2°: Innerhalb normaler Toleranz

**Kalibrierungs-Prozedur (Standard):**
1. Boot in ruhigem Wasser, Motor aus (Magnetfeld-Störung minimieren)
2. Mit konstanter Geschwindigkeit (z.B. 5 knots) alle 360° drehen (10 Minuten Fahrt)
3. System-Display: Kalibrierungs-Modus aktivieren (bei Raymarine/Garmin Schiff → Systeme → Kompass-Kalibrierung)
4. Ergebnis: Abweichungs-Kurve wird berechnet, gespeichert

**Nach Kalibrierung:**
- Deviation sollte <2° sein
- Falls immer noch >3°: Magnetische Störquelle näher lokalisieren
  - Mit Handy-Kompass (oder Navigationskompass) die Boot-Nähe absuchen
  - Metallische Gegenstände (Bügel, Antennen-Halterung) ggfs. umlagern

**Kosten:**
| Maßnahme | Kosten |
|---|---|
| DIY Kalibrierung (wenn Boot ruhig fahren kann) | €0 |
| Service-Techniker Kalibrierung | €200–400 |
| Kompass-Modul Austausch (bei Sensor-Fehler) | €800–1500 |
| Magnetische Störquelle lokalisieren + entfernen | €100–500 |

---

### 21.5 Fehlerbild 5: NMEA-2000-Netzwerk-Fehler (roter Fehlercode)

**Typische Fehler:**
- "Network offline"
- "Node failed" (mit Geräte-ID)
- "Data lost on backbone" 
- "CAN-Bus error rate high"

**Diagnose-Baum:**
```
Roter NMEA-Fehler?
├→ Wie viele Geräte sind betroffen?
│  ├→ Alle Geräte aus (Backbone komplett tot)
│  │  Maßnahme: Haupt-Stromschalter überprüfen, Stecker-Spannung messen
│  └→ Nur einzelnes Gerät (z.B. nur Radar)
│     Maßnahme: Gerät-Stecker überprüfen, Kabel-Widerstand messen, Gerät neustart
├→ Fehler intermittierend oder permanent?
│  ├→ Intermittierend (tritt auf bei bestimmter Bedingung, z.B. Motor an)
│  │  Maßnahme: EMV-Problem (elektromagnetische Störung), Kabel-Routierung überprüfen
│  └→ Permanent
│     Maßnahme: Kabel-Diskontinuität oder Stecker-Korrosion
└→ Fehlermeldung-Code auslesen (im Systeme-Menü)
   → Zu Hersteller-Dokumentation konsultieren
```

**Praktische Reparatur-Schritte:**
1. **Punkt 1:** Alle NMEA-Stecker überprüfen (visuell + mit Ohm-Messer)
   - Sollten fest sitzen, keine Korrosion zeigen
   - Mit Kontakt-Spray reinigen

2. **Punkt 2:** Backbone-Spannung messen
   - Should be 12V ±10%, Ripple <0.2V
   - Wenn instabil: Batterie oder Stromversorgung überprüfen

3. **Punkt 3:** CAN-Bus-Terminator überprüfen
   - Jedes Netzwerk hat zwei Terminator-Widerstände (120Ω) an den Enden
   - Fehlerhafte Termination = alle Geräte offline
   - Mit Ohm-Messer überprüfen: sollte ca. 60Ω zeigen (zwei 120Ω parallel)

4. **Punkt 4:** Kabel-Länge überprüfen
   - NMEA-2000 Kabel sollte <100m sein (praktisch selten Problem auf Boot)
   - Bei >60m: kann Signalqualität beeinträchtigt werden

**Häufige Fehler-Codes und Behebung:**
| Fehler-Code | Ursache | Behebung |
|---|---|---|
| 01001 (Node offline) | Gerät nicht mit Netzwerk verbunden oder Stromausfall | Stecker überprüfen, Stromversorgung prüfen, Gerät neustart |
| 02002 (CAN error rate high) | EMV-Störung oder Kabel-Qualität | Kabel-Routierung weg von Stromkabeln, ggfs. Kabel-Schirm überprüfen |
| 03003 (Data lost) | Backbone-Diskontinuität oder Terminator-Fehler | Backbone-Spannung prüfen, Terminator überprüfen |

---

### 21.6 Fehlerbild 6: VHF-Funk-Probleme (Reichweite drastisch reduziert)

**Ursachen:**
1. **Antenne-Blockade** (40%): Antenne unter Deck, oder neuer Mast verdeckt Sicht
2. **Antenne-Kabel zu lang oder minderwertiges Material** (30%): Signal-Verlust im Kabel
3. **Antenne-Anpassung** (15%): Antenne für 25W ausgelegt, aber 60W Power eingegeben = Fehlabstimmung
4. **Stromversorgung-Problem** (10%): Zu niedrige Spannung, besonders bei Batterie-Belastung
5. **Funk-Modul-Fehler** (5%): Amplifier oder Sender-Stufe defekt

**Praktisches Test-Verfahren:**

**Reichweiten-Test (mit bekanntem Funkpartner):**
- Abstand messen (GPS oder Kartenplot)
- Mit Normallast anrufen (25W Power)
- Signalqualität S-Meter bewerten (S1-S9 Skala)
- Sollte auf 10 nm klar sein (S4+), auf 20 nm noch lesbar (S2+)
- Wenn nur 2 nm Reichweite: Problem besteht

**Schrittweise Diagnose:**
1. Antennenkabel sichtprüfen (äußere Beschädigung?)
2. Antenne von unten ansehen: sitzt sie fest, oder hat Bewegungsspiel?
3. Mit Ohm-Messer: Antennenkabel sollte 50Ω Charakteristische Impedanz haben (spezielles RG-58 oder RG-213 Kabel)
   - Wenn nicht korrekt: falsches Kabel installiert (zu viel Signalverlust)
4. SWR messen (Stehwellen-Verhältnis) — am besten mit Funk-Techniker
   - SWR <1.5: Gut
   - SWR 1.5–2.0: Acceptable, aber nicht ideal
   - SWR >2.0: Antenne falsch abgestimmt

**Reparatur-Optionen:**
| Problem | Lösung | Kosten |
|---|---|---|
| Antenne zu niedrig / blockiert | Antenne höher montieren oder freier positionieren | €50–150 (Halterung) |
| Antennenkabel defekt oder zu lang | Kabel ersetzen mit korrektem Typ (RG-58 U, max 20m) | €80–200 |
| Antenne falsch abgestimmt | SWR-Anpassung oder Antenne-Austausch | €150–400 |
| Funk-Modul Verstärker-Fehler | Modul-Austausch | €400–800 |

---

### 21.7 Fehlerbild 7: Autopilot oscilliert (pendelt ±10°)

**Häufigste Ursachen (in Reihenfolge):**
1. **Kompass schlecht kalibriert** (60%): Auto pilot folgt fehlerhaften Kompass-Daten
2. **Servo-Steuerung zu sensitiv eingestellt** (25%): PID-Parameter (Proportional-Integral-Derivative) nicht optimiert
3. **Hydraulik-Leck** (10%): Servo verliert Kraft, overshoots bei Steuerbefehlen
4. **Kompass-Sensor-Drift** (3%): Sensor-Rauschen oder Hardware-Fehler
5. **Sonstige** (2%): Ruder-Spiel, Getriebe-Verschleiß

**Prüfungs-Reihenfolge:**

**Schritt 1: Kompass überprüfen (5 min)**
- Autopilot abschalten
- Mit Hand-Steuering: vergleiche echte Kurse mit Kompass-Anzeige
- Wenn Kompass falsch: Kalibrierung durchführen (siehe Fehlerbild 4)

**Schritt 2: Autopilot neu kalibrieren (10 min)**
- Ruhiges Wasser, kein Wind/Seegang
- Autopilot aktivieren, 5 Minuten fahren → Learning-Phase
- System sollte oscillation selbst korrigieren nach Lernphase

**Schritt 3: Servo-Parameter überprüfen (2 min)**
- Im Autopilot-Menü: PID-Parameter ansehen
- Defaultwerte oft zu aggressiv eingestellt
- Proportional-Gain reduzieren (z.B. von 100 auf 80) → weniger aggressive Reaktion

**Schritt 4: Hydraulik überprüfen (5 min)**
- Hydraulik-Fluid sichtprüfen (sollte rosig/dunkelrot sein, nicht schwarzbraun)
- Flüssigkeits-Pegel prüfen (sollte auf Markierung sein)
- Bei Leck: Tropfen rund um Servo-Zylinder sichtbar
- Wenn Leck: Reparatur kostet €400–800 (Dichtungs-Austausch oder Servo-Neuaufbau)

---

### 21.8 Fehlerbild 8: Batterie lädt nicht vollständig

**Symptome:**
- Batterie-Spannungs-anzeige bleibt bei 12.4V stecken, auch nach Stunden Laden
- Geräte funktionieren, aber weniger Power verfügbar
- Nach 1 Stunde Betrieb deutlich Spannung, nicht nach 8 Stunden langsamem Laden erwartet

**Diagnose-Schritte:**

1. **Lade-Spannung messen** (mit Multimeter, während Ladegerät aktiv)
   - Sollte 13.5–14.5V zeigen (Blei-Säure 12V System)
   - Wenn 13.0V: Ladegerät liefert zu wenig Spannung
   - Wenn >15V: Überspannung, kann Batterie beschädigen

2. **Lade-Strom messen** (Amperemeter im Stromkreis)
   - Sollte schnell sinken (von z.B. 50A auf <5A in 1 Stunde)
   - Wenn Strom nicht sinkt: Batterie-Zelle Kurzschluss oder Laderegler-Fehler

3. **Batterie-Innen-Widerstand testen** (mit speziellem Gerät oder Fachwerkstatt)
   - Gute Batterie: <20mΩ (Milliohm)
   - Schlechte Batterie: >100mΩ (deutet auf chemische Degradation hin)

4. **Laderegler überprüfen** (bei Solar oder alternator-Ladung)
   - Regler sollte Spannung bei ca. 13.8V stabilisieren
   - Wenn Regler-Output zu niedrig: Regler-Austausch notwendig

**Häufigste Reparaturen:**
| Problem | Behebung | Kosten |
|---|---|---|
| Ladegerät-Ausgang zu niedrig | Ladegerät ersetzen oder reparieren | €150–400 |
| Batterie chemisch degradiert | Batterie-Austausch | €300–600 (je Kapazität) |
| Laderegler-Fehler | Regler-Austausch | €200–500 |
| Batterie-Anschluss korrodiert | Anschlüsse reinigen oder ersetzen | €20–80 |

---

### 21.9 Fehlerbild 9: Bildschirm (Plotter, Radar, Autopilot Display) bleibt schwarz

**Häufigste Ursachen:**
1. **Keine Stromversorgung** (50%): Sicherung durchgebrannt oder Kabel-Bruch
2. **Bildschirm-Kabel locker** (25%): Stecker nicht vollständig eingesteckt
3. **Firmware-Crash** (15%): System braucht Reset, oder Firmware-Update fehlgeschlagen
4. **Bildschirm oder Elektronik-Board defekt** (10%): Hardware-Fehler, Kondensator-Austrocknung

**Reparatur-Baum:**

```
Bildschirm schwarz?
├─ Ist das Gerät mit Strom versorgt?
│  ├─ Nein (keine LED, keine Geräusche): Stromprüfung
│  │  ├─ Sicherung durchgebrannt? → Neue Sicherung (gleicher Wert!)
│  │  └─ Stromkabel beschädigt? → Kabel überprüfen, evtl. ersetzen
│  └─ Ja (LED leuchtet): Weitermachen zu Punkt 2
├─ Ist Bildschirm-Kabel fest?
│  └─ Stecker überprüfen, ggfs. mit Kontakt-Spray reinigen
└─ Wenn alles fest + Strom OK:
   ├─ Device Reboot durchführen (Power-Taste 10 sec halten)
   ├─ Wenn immer noch schwarz: Firmware-Update versuchen
   └─ Wenn nichts hilft: Techniker-Diagnose erforderlich
```

**Praktische Test-Verfahren:**
1. Mit Multimeter: Spannung am Geräte-Stecker messen (sollte 12V ±10%)
2. Mit Ohm-Messer: Stromkabel durchgängig? (sollte nicht ∞Ω sein)
3. Bildschirm-Helligkeit überprüfen: manche Geräte haben versteckte Helligkeit-Regler (im Menü)

---

### 21.10 Fehlerbild 10: Wasser-Eindringung in Elektronik-Box

**Sichtbare Anzeichen:**
- Feuchtigkeits-Tropfen innen am Gehäuse
- Korrosion innen (grüne Oxidation auf Leitern/Kontakten)
- Chlorwasser-Rückstände (weißliche Ablagerungen)

**Reparatur-Strategie:**

**Sofort-Maßnahmen (erste 24 Stunden):**
1. Elektronik-Box aus dem Boot entfernen (wenn möglich)
2. Nicht einschalten — kann Kurzschluss auslösen
3. Mit Silica-Gel oder Heißluft (nicht >40°C!) trocknen
4. 48 Stunden Trocknungs-Phase mit offenem Deckel (mit Silica-Gel)
5. Nach Trocknung: Innenseite sichtprüfen auf Korrosion

**Wenn Korrosion sichtbar:**
1. Mit Isopropyl-Alkohol (99%+) vorsichtig abspülen (nicht aggressiv schrubben)
2. Mit Kontakt-Spray (z.B. WD-40 oder Electrolube) alle Kontakte behandeln
3. Nochmals 24 Stunden lufttrocknen
4. Testen: mit Batterien ein Test-Gerät verbinden (nicht direkt Boot-Elektronik)

**Ursachen-Analyse & Prävention:**
| Ursache | Prävention | Kosten |
|---|---|---|
| Belüftungsöffnung verstopft (Algen, Salz) | Montliche Kontrolle, Netz überprüfen | €5–20 Netz |
| Kabel-Durchgang nicht versiegelt | Silikondichtung auftragen (Hersteller spezifizieren) | €10–30 |
| Kondenswasser bei Temperatur-Wechsel | Silica-Gel-Packs permanent in Box | €10–50 (re-usable packs) |
| Regen-Eindringung durch Deckel-Spalt | Deckel-Gummi ersetzen, Dichtmasse kontrollieren | €30–100 |

---

### 21.11 Fehlerbild 11: Stecker-Abrieb und intermittierende Kontakte

**Visuelles Erkennungsmerkmal:**
- Grünlich verfärbter Kontakt bei Messingteilen
- Schwärzung auf Silber-Kontakten (silbernes Sulfit-Oxide)
- Kleine Flöckchen innen im Stecker-Gehäuse (Kontakt-Material, das sich abgelöst hat)

**Mess-Verfahren (ohne Stecker zu öffnen):**
1. Mit Ohm-Messer zwischen den Stecker-Kontakten messen
2. Sollte <0.05Ω sein (typischerweise <0.01Ω bei neuem Stecker)
3. Wenn 0.5–2Ω: Kontakt oxidiert, Signal-Verlust möglich
4. Wenn >5Ω: Stecker kritisch, Funktionsstörungen wahrscheinlich

**Reparatur-Optionen:**

| Schweregrad | Maßnahme | Kosten | Haltbarkeit |
|---|---|---|---|
| Mild (<0.2Ω) | Kontakt-Spray sprühen, 10x einstecken/rausziehen | €10 | 6 Monate |
| Moderat (0.5–2Ω) | Stecker-Pins mit feiner Bürste reinigen + Kontakt-Spray | €20 | 12 Monate |
| Schwer (>5Ω) | Stecker kompletter Austausch | €50–150 | 5+ Jahre |

**Langfristige Prävention:**
- Nach jeder Salzwasser-Fahrt: Süßwasser spülen, WD-40 aufsprühen
- Stecker-Kappen immer verwenden (verhindert Umwelteinflüsse)
- Monatliche Sichtprüfung aller Stecker im Elektronik-Box

---

### 21.12 Fehlerbild 12: Firmware-Update-Fehler (System startet nicht mehr)

**Häufigste Fehler-Ursachen beim Update:**
1. **Stromausfalls während Update** (40%): Firmware-Datei beschädigt geladen
2. **Falsches Update-Paket** (25%): Software-Version nicht kompatibel mit Gerät
3. **Defekte SD-Karte oder USB-Stick** (20%): Datei korrupt übertragen
4. **Versionsinkompatibilität** (10%): Update-Abhängigkeiten nicht erfüllt (z.B. Basis-Version zu alt)
5. **Andere** (5%): RAM-Fehler, Speicher-Problemem, seltene Hardware-Bugs

**Recovery-Verfahren (je nach Hersteller):**

**Für Garmin Geräte:**
```
1. Gerät ausschalten
2. Mit gedrückter POWER + MENU-Taste einschalten (10 Sekunden)
3. "Bootloader" sollte angezeigt werden
4. Korrekte Firmware-Datei via USB übertragen
5. System sollte neu starten und laden
```

**Für Raymarine Geräte:**
```
1. Ethernet-Kabel zu Werk-PC anschließen
2. Raymarine Update-Software starten (vom USB-Stick)
3. System zum Booten auffordern (Power-Reset)
4. Firmware erneut installieren
```

**Recovery erforderlich wenn:**
- Gerät zeigt "Bootloader" oder "Recovery mode" an
- Kein normales Startbild erscheint nach Einschalt-Versuch
- Firmware-Update mit Fehlercode abgebrochen

**Kostenschätzung bei fehlgeschlagenem Update:**
| Szenario | Behebung | Kosten |
|---|---|---|
| Einfacher Neustart ausreichend | Gerät ausschalten, 10 sec warten, wieder ein | €0 |
| Bootloader-Recovery möglich | Mit Update-Software Firmware erneut laden | €0 |
| Hardware beschädigt | Geräte-Austausch oder Reparatur | €500–1500 |

---

## 22. Wartungsprotokoll-Vorlagen: Inspektions-Checklisten

### 22.1 Jährliche Elektronik-Inspektion (50+ Prüfpunkte)

**Inspektions-Datum:** ____________  
**Boot-Name & Kennzeichen:** __________________________  
**Inspekteur:** ____________  
**System-Status vor Inspektion:** ☐ In Betrieb  ☐ Winterfest  ☐ Nach Lagerung

#### A. Stromversorgung & Batterie (10 Punkte)

- [ ] **A1.** Batterie-Ruhespannung messen (sollte 12.7–12.9V)
  - Messwert: ______ V  
  - Status: ☐ OK  ☐ Fair (12.4–12.6V)  ☐ Schwach  ☐ Kritisch
  
- [ ] **A2.** Batterie-Alter prüfen, Kaufdatum dokumentieren
  - Alter: ______ Jahre  
  - Nächstes Austausch-Datum: ______________
  
- [ ] **A3.** Batterie-Anschluss-Klemmen sichtprüfen (auf Korrosion)
  - Status: ☐ Sauber  ☐ Leichte Oxidation  ☐ Schwere Korrosion
  - Ggfs. Reinigung durchführt: ☐ Nein  ☐ Ja (Datum: __________)
  
- [ ] **A4.** Hauptstromschalter funktioniert (Ein/Aus ohne Widerstand)
  - Status: ☐ OK  ☐ Rauer Betrieb  ☐ Nicht funktionsfähig
  
- [ ] **A5.** Sicherungs-Panel sichtprüfen (alle Sicherungen da, keine geschwärzt)
  - Fehlende/durchgebrannte Sicherungen: ____________
  - Nachbessert? ☐ Nein  ☐ Ja (Datum: __________)
  
- [ ] **A6.** Stromkabel auf Beschädigungen überprüfen (Abdruck, Quetschungen, freiliegende Drähte)
  - Status: ☐ Intakt  ☐ Minor cosmetic  ☐ Gefährliche Stellen sichtbar
  - Lokation problematischer Stellen: ____________
  
- [ ] **A7.** Massekabel (Negativ-Kabel) überprüfen (Verbindung Boot-Rumpf)
  - Widerstand mit Ohm-Messer: _______ Ω (sollte <0.1Ω sein)
  - Status: ☐ OK  ☐ Verdächtig  ☐ Unterbrochen
  
- [ ] **A8.** Ladegerät / Landstrom-Anschluss funktioniert
  - Status: ☐ OK  ☐ Intermittierende Probleme  ☐ Nicht funktionsfähig
  - Typische Lade-Zeit volle Batterie: ______ Stunden (sollte <8h sein)
  
- [ ] **A9.** DC-Stromverteiler sichtprüfen (alle Anschlüsse fest)
  - Status: ☐ Alle fest  ☐ 1–2 Anschlüsse locker  ☐ Mehrere lose Anschlüsse
  - Nachgezogen? ☐ Nein  ☐ Ja (Datum: __________)
  
- [ ] **A10.** Stromversorgungsspannung unter Last messen (Motor an, Geräte aktiv)
  - Sollte 11.5–13.5V sein  
  - Messwert: ______ V  
  - Status: ☐ OK  ☐ Grenzwertig  ☐ Zu niedrig

#### B. GPS & Navigation (8 Punkte)

- [ ] **B1.** GPS-Empfänger Signalstärke prüfen (HDOP-Wert)
  - HDOP-Wert: _______ (sollte <3 sein)  
  - Status: ☐ Excellent (<1.5)  ☐ Good (1.5–3)  ☐ Fair (3–6)  ☐ Poor (>6)
  
- [ ] **B2.** GPS-Antenne sichtprüfen (Verschmutzung, Beschädigungen)
  - Status: ☐ Sauberer  ☐ Leicht verschmutzt  ☐ Stark verschmutzt/beschädigt
  - Reinigung durchgeführt? ☐ Nein  ☐ Ja (Datum: __________)
  
- [ ] **B3.** GPS-Antennenkabel Durchgang prüfen (mit Ohm-Messer)
  - Widerstand: ______ Ω (sollte nicht ∞Ω sein)  
  - Status: ☐ Durchgang OK  ☐ Verdächtig  ☐ Unterbrochen
  
- [ ] **B4.** Plotter-Display Sichtprüfung (Risse, tote Pixel)
  - Status: ☐ OK  ☐ Kosmetische Kratzer  ☐ Tote Pixel/Linien  ☐ Großflächige Schäden
  
- [ ] **B5.** Plotter Funktionsprüfung (startet, zeigt Karte, reagiert auf Input)
  - Status: ☐ Vollständig funktionsfähig  ☐ Verzögerungen  ☐ Intermittierende Fehler  ☐ Nicht funktionsfähig
  
- [ ] **B6.** Kompass-Funktion überprüfen (vergleiche Anzeige mit Hand-Kompass)
  - Abweichung: ______ ° (sollte <2° sein)  
  - Status: ☐ OK (<2°)  ☐ Marginal (2–5°)  ☐ Schlechte Kalibrierung (>5°)
  - Kalibrierung durchgeführt? ☐ Nein  ☐ Ja (Datum: __________)
  
- [ ] **B7.** NMEA-Netzwerk-Status überprüfen (alle Geräte verbunden)
  - Verbundene Geräte: _____________  
  - Fehler-Meldungen? ☐ Keine  ☐ Minor  ☐ Critical
  
- [ ] **B8.** Datenantennen-Stecker überprüfen (sichtbar fest, keine Korrosion)
  - Status: ☐ OK  ☐ Leichte Oxidation  ☐ Schwere Korrosion/locker

#### C. Radar & Funk (7 Punkte)

- [ ] **C1.** Radar-Antenne Drehung funktioniert (prüfe langsam, höre auf Geräusche)
  - Status: ☐ Flüssig  ☐ Ruckelig  ☐ Laut/Surr-Geräusch  ☐ Blockiert
  
- [ ] **C2.** Radar-Antenne Sichtprüfung (Verschmutzung, Wasser-Austritt)
  - Status: ☐ Sauber/trocken  ☐ Leicht verschmutzt  ☐ Wasser sichtbar/Korrosion
  - Reinigung/Service durchgeführt? ☐ Nein  ☐ Ja (Datum: __________)
  
- [ ] **C3.** Radar-Reichweitentest (bekannte Landmasse in 5–10 nm Entfernung)
  - Erkannte Entfernung: ______ nm  
  - Status: ☐ Normal  ☐ Reduzierte Reichweite  ☐ Kein Signal
  
- [ ] **C4.** VHF-Funk Stromaufnahme messen (sollte ~2–3A bei Standby)
  - Messwert: ______ A  
  - Status: ☐ Normal  ☐ Höher als erwartet  ☐ Kein Strom
  
- [ ] **C5.** VHF-Antenne sichtprüfen (Risse, lockere Halterung, Beschädigungen)
  - Status: ☐ OK  ☐ Minor defects  ☐ Significant damage/locker
  
- [ ] **C6.** VHF-Reichweiten-Test (mit bekanntem Funkpartner auf Distanz)
  - Maximale Reichweite: ______ nm (sollte mind. 10 nm sein)  
  - Qualität: ☐ Klar  ☐ Mit Rauschen  ☐ Schwach/unterbrochen
  
- [ ] **C7.** VHF-Antennenkabel Überprüfung (Widerstand mit Ohm-Messer)
  - Widerstand: ______ Ω (sollte ~50Ω sein)  
  - Status: ☐ OK  ☐ Verdächtig  ☐ Unterbrochen

#### D. Autopilot (6 Punkte)

- [ ] **D1.** Autopilot Funktionsprüfung (schalte ein, fahre 5 min, prüfe Stabilität)
  - Status: ☐ Hält Kurs stabil  ☐ Oszilliert leicht (±2°)  ☐ Pendelt stark  ☐ Funktioniert nicht
  
- [ ] **D2.** Servo-Getriebe Geräuschkontrolle (höre auf abnormale Laute)
  - Status: ☐ Geräuschlos/normal  ☐ Quietschen  ☐ Knarren  ☐ Lautes Surr-Geräusch
  - Service erforderlich? ☐ Nein  ☐ Ja (geplant: __________)
  
- [ ] **D3.** Hydraulik-Flüssigkeit Zustand prüfen (Farbe, Pegel)
  - Farbe: ☐ Rosig/normal  ☐ Dunkler/oxidiert  ☐ Schwärzlich/verbrannt  
  - Pegel: ☐ OK  ☐ Niedrig (Nachfüllung notwendig)  
  - Nachgefüllt? ☐ Nein  ☐ Ja (Menge: ______ ml)
  
- [ ] **D4.** Kompass-Abweichung Test (vergleiche Autopilot-Kurs mit Hand-Kompass)
  - Abweichung: ______ ° (sollte <2° sein)  
  - Neu kalibriert? ☐ Nein  ☐ Ja (Datum: __________)
  
- [ ] **D5.** IMU-Sensor Sichtprüfung (alle Anschlüsse fest)
  - Status: ☐ OK  ☐ Locker  ☐ Beschädigt
  
- [ ] **D6.** Ruderhebel-Spiel prüfen (Ruder sollte ohne Spiel auf Befehle reagieren)
  - Spiel sichtbar? ☐ Nein  ☐ <1cm  ☐ >1cm  
  - Service erforderlich? ☐ Nein  ☐ Ja (geplant: __________)

#### E. Sicherheit & Redundanz (5 Punkte)

- [ ] **E1.** Notstrom-Batterie Test (wenn vorhanden; sollte vollgeladen sein)
  - Spannung: ______ V (sollte 12.7+)  
  - Status: ☐ OK  ☐ Grenzwertig  ☐ Zu niedrig
  
- [ ] **E2.** Sicherungs-Schalter überprüfen (alle Elektronik haben separate Sicherungen)
  - Status: ☐ Alle vorhanden  ☐ Fehlende Sicherung  ☐ Durchgebrannte Sicherung
  
- [ ] **E3.** Backup-Navigation überprüfen (Paper-Karten vorhanden, Hand-Kompass funktioniert)
  - Status: ☐ Vollständig  ☐ Teilweise  ☐ Nicht vorhanden
  
- [ ] **E4.** Emergency-Funk-Batterie prüfen (wenn Funksystem eigene Notstrom hat)
  - Status: ☐ OK  ☐ Schwach  ☐ Nicht vorhanden
  
- [ ] **E5.** Backup-GPS überprüfen (Hand-GPS-Gerät oder Smartphone-App funktionsfähig)
  - Status: ☐ Funktioniert  ☐ Batterie schwach  ☐ Nicht vorhanden

#### F. Kabel & Stecker (8 Punkte)

- [ ] **F1.** Alle Stecker-Verbindungen visuelle Kontrolle (fest, keine Korrosion)
  - Gesamtstatus: ☐ Alle OK  ☐ 1–2 verdächtig  ☐ Mehrere problematisch
  - Problematische Stecker: _____________
  
- [ ] **F2.** NMEA-2000 Stecker-Kontakte sichtprüfen (unter Lupe oder mit Kontakt-Spray reinigen)
  - Status: ☐ Sauber  ☐ Leichte Oxidation  ☐ Korrosion
  - Gereinigt? ☐ Nein  ☐ Ja (Datum: __________)
  
- [ ] **F3.** Stromkabel-Isolationen auf Risse überprüfen
  - Status: ☐ Intakt  ☐ Minor cracks  ☐ Freiliegende Drähte sichtbar
  
- [ ] **F4.** Koaxial-Kabel (GPS, Radar, VHF) auf Beschädigungen überprüfen
  - Status: ☐ Intakt  ☐ Minor cosmetic  ☐ Beschädigungen sichtbar
  
- [ ] **F5.** Kabel-Routierung überprüfen (getrennt von Stromleitungen, keine Knickstellen)
  - Status: ☐ Ordentlich  ☐ Suboptimal  ☐ Gefährlich
  
- [ ] **F6.** Kabel-Durchgänge versiegelt überprüfen (kein Wasser-Eindringung möglich)
  - Status: ☐ Vollständig versiegelt  ☐ Teilweise  ☐ Unversiegelt
  
- [ ] **F7.** Stecker-Kappen vorhanden (für Antennen-Stecker wenn nicht in Betrieb)
  - Status: ☐ Alle Kappen vorhanden  ☐ Einige fehl  ☐ Keine Kappen
  
- [ ] **F8.** Kabel-Befestigungen (Cable-Clips) überprüfen (alles ordentlich befestigt)
  - Status: ☐ OK  ☐ Locker  ☐ Zu straff gezogen

#### G. Allgemeiner Elektronik-Box-Zustand (6 Punkte)

- [ ] **G1.** Elektronik-Box Außenseite sichtprüfung (Risse, Beschädigungen)
  - Status: ☐ OK  ☐ Kosmetische Kratzer  ☐ Strukturelle Schäden
  
- [ ] **G2.** Box-Belüftung überprüfen (Lüftungsschlitze offen, Netz nicht verstopft)
  - Status: ☐ Frei  ☐ Teilweise verstopft  ☐ Blockiert
  - Gereinigt? ☐ Nein  ☐ Ja (Datum: __________)
  
- [ ] **G3.** Box-Innen Feuchtigkeit kontrollieren (trockene Umgebung)
  - Status: ☐ Trocken  ☐ Leichte Feuchte  ☐ Sichtbare Feuchtigkeit
  - Silica-Gel überprüft? ☐ Nein  ☐ Ja, ausgetauscht (Datum: __________)
  
- [ ] **G4.** Box-Deckel-Gummi Dichtung überprüfen (spröde, rissig?)
  - Status: ☐ Gut  ☐ Alterungserscheinungen  ☐ Beschädigt/auslaufend
  - Austausch geplant? ☐ Nein  ☐ Ja (geplant: __________)
  
- [ ] **G5.** Temperatur-Sensor Funktionsprüfung (falls vorhanden)
  - Innen-Temperatur: ______ °C (sollte 15–35°C sein)  
  - Status: ☐ Normal  ☐ Wärmer als erwartet  ☐ Kühlung überprüfen
  
- [ ] **G6.** Gehäuse-Integrität Überprüfung (drücke leicht an Box — sollte keine Spannungen sichtbar sein)
  - Status: ☐ OK  ☐ Leichte Verformung  ☐ Deutliche Verbiegung/Risse

**Zusammenfassung Jährliche Inspektion:**

- **Gesamtstatus:** ☐ OK — keine Maßnahmen erforderlich  
  ☐ WARNUNG — empfohlene Wartung  
  ☐ KRITISCH — sofortige Reparatur erforderlich

- **Priorität-Maßnahmen (in Reihenfolge):**
  1. _________________________  
  2. _________________________  
  3. _________________________

- **Geschätzte Reparatur-Kosten:** € __________  
- **Geschätzte Reparatur-Zeit:** ______ Stunden

- **Nächste Inspektion geplant:** ______________  
- **Inspekteur-Unterschrift:** ___________________  **Datum:** ______________

---

### 22.2 Winterfestmachung Schritt-für-Schritt (Checkliste)

**Zeitrahmen:** 4–6 Wochen vor Saisonende  
**Geschätzter Aufwand:** 8–12 Stunden  
**Erforderliche Werkzeuge:** Multimeter, Schraubenzieher-Set, WD-40, Kontakt-Spray, Silica-Gel

#### Phase 1: Stromversorgung & Batterie-Management (2 Stunden)

- [ ] **W1.** Batterie vollständig laden (mit Ladegerät, bis Strom <2A)
  - Lade-Datum: ______________  
  - Endspannung: ______ V
  
- [ ] **W2.** Batterie-Anschlüsse mit WD-40 behandeln (Korrosionsschutz)
  - Status: ☐ Erledigt  ☐ Nicht nötig (schon behandelt)
  
- [ ] **W3.** Hauptstromschalter auf AUS stellen
  - Status: ☐ Bestätigt AUS
  
- [ ] **W4.** Falls Batterie entnommen wird: in dunklem, trockenen Ort lagern (min. 12.4V halten)
  - Lagerungs-Ort: ____________  
  - Monatliche Lade-Erinnerung: ☐ Ja  Datum: ______________
  
- [ ] **W5.** Laderegler überprüfen (wenn Solar/Wind-System vorhanden)
  - Status: ☐ OK  ☐ Fehler-Code  ☐ Nicht vorhanden

#### Phase 2: Elektronik-Systeme (3 Stunden)

- [ ] **W6.** Alle Elektronik-Geräte sauber abfahren (ordnungsgemäße Shutdown-Sequenz)
  - Reihenfolge: GPS/Plotter → Radar → Autopilot → Funk → Allgemeine Systeme  
  - Status: ☐ Alle ohne Fehler beendet
  
- [ ] **W7.** Alle Elektronik-Stecker überprüfen + mit Kontakt-Spray behandeln
  - Behandelte Stecker: _____________  
  - Gefundene Probleme: _____________
  
- [ ] **W8.** Alle Antennenstecker mit Schutz-Kappen versehen
  - Status: ☐ GPS-Antenne  ☐ Radar-Antenne  ☐ VHF-Antenne  ☐ TV-Antenne (falls vorhanden)
  
- [ ] **W9.** Elektronik-Box Innenraum inspizieren (Feuchtigkeit, Korrosion)
  - Status: ☐ Trocken  ☐ Leichte Feuchte (Silica-Gel reicht)  ☐ Nässe (sofortige Maßnahme notwendig)
  - Silica-Gel austauschen: ☐ Ja  ☐ Nein (noch gut)
  
- [ ] **W10.** Elektronik-Box belüften (falls möglich, zu Trocknungs-Zwecken)
  - Lüftungs-Sichtprüfung: ☐ Frei  ☐ Verstopft
  - Gereinigt? ☐ Nein  ☐ Ja
  
- [ ] **W11.** Backup-Batterie Test (Notstrom-Battery, falls vorhanden)
  - Spannung: ______ V (sollte 12.4+)  
  - Status: ☐ OK  ☐ Grenzwertig (Ladung prüfen im Frühjahr)

#### Phase 3: Kabel & Stecker-Schutz (2 Stunden)

- [ ] **W12.** Alle stromführenden Stecker mit Stecker-Hüllen versehen
  - Status: ☐ Erledigt  ☐ Keine Hüllen vorhanden (kaufen erforderlich)
  
- [ ] **W13.** Antennenkabel-Enden mit Schutzkappen oder Silikon-Versiegelung behandeln
  - Status: ☐ GPS  ☐ Radar  ☐ VHF  ☐ Sonstige
  
- [ ] **W14.** Stromkabel-Beschädigungen überprüfen (vor Lagerung)
  - Status: ☐ OK  ☐ Minor defects (Notiz für Frühjahr)  ☐ Kritisch (sofort reparieren)
  
- [ ] **W15.** Alle Kabel-Befestigungen überprüfen (lockern, um Druck-Quetschung zu vermeiden)
  - Status: ☐ Gelockert  ☐ Schon locker  ☐ Zu fest (nachgebessert)

#### Phase 4: Antennensysteme (1.5 Stunden)

- [ ] **W16.** GPS-Antenne reinigen (Süßwasser spülen)
  - Status: ☐ Erledigt  ☐ Nicht nötig
  
- [ ] **W17.** GPS-Antenne mit UV-Schutzmittel behandeln
  - Produkt: ____________  
  - Datum: ______________
  
- [ ] **W18.** Radar-Antenne reinigen & Drehung überprüfen
  - Status: ☐ Sauber/dreht normal  ☐ Probleme beobachtet (notiert für Frühjahr)
  
- [ ] **W19.** Radar-Antennenlager mit Schmiermittel behandeln (falls zugänglich)
  - Status: ☐ Erledigt  ☐ Nicht nötig
  
- [ ] **W20.** VHF-Antenne überprüfen (keine lockeren Befestigungen)
  - Status: ☐ Fest  ☐ Locker (nachgezogen)

#### Phase 5: Lagerbedingungen & Dokumentation (1.5 Stunden)

- [ ] **W21.** Elektronik-Box vor Witterung schützen (Plane, Abdeckung)
  - Abdeckungs-Typ: ____________  
  - Status: ☐ Installiert
  
- [ ] **W22.** Feuchtigkeits-Kontrolle einplanen (monatlich während Lagerung)
  - Erinnerung gesetzt? ☐ Ja (Datum: __________)  ☐ Nein
  
- [ ] **W23.** Winterfestmachungs-Foto dokumentieren (für Frühjahrs-Vergleich)
  - Fotos gemacht? ☐ Ja  ☐ Nein
  
- [ ] **W24.** Alle Wartungsergebnisse dokumentieren
  - Dokumentations-Datei aktualisiert? ☐ Ja  ☐ Nein
  
- [ ] **W25.** Frühjahrs-Inspektions-Checkliste vorbereiten (siehe 22.3)
  - Vorbereitet? ☐ Ja  ☐ Nein

**Winterfestmachungs-Abschluss:**

- **Gesamtstatus:** ☐ Vollständig  ☐ Teilweise  ☐ Probleme gefunden (notiert)
- **Kritische Befunde (für Frühjahr):** _____________
- **Winterfestmachungs-Datum:** ______________
- **Durchgeführt durch:** ___________________

---

### 22.3 Saisonale Inbetriebnahme Schritt-für-Schritt (Frühjahrs-Checkliste)

**Zeitrahmen:** 2–3 Wochen vor Saison-Start  
**Geschätzter Aufwand:** 6–8 Stunden  
**Erforderliche Werkzeuge:** Multimeter, Spannungsprüfer, Kontakt-Spray, Testgeräte

#### Phase 1: Batterie & Stromversorgung (1 Stunde)

- [ ] **S1.** Batterie überprüfen (Spannung, Alter, Zustand)
  - Ruhespannung: ______ V (sollte 12.7+)  
  - Alter: ______ Jahre  
  - Status: ☐ OK  ☐ Fair (Ladung überprüfen)  ☐ Kritisch (austauschen)
  
- [ ] **S2.** Falls Batterie entnommen war: wieder einbauen + Anschlüsse fest
  - Status: ☐ Installiert + fest  ☐ Nicht entnommen
  
- [ ] **S3.** Komplettes Laden durchführen (mindestens 4 Stunden)
  - Lade-Spannung erreichbar? ☐ Ja (13.5V+)  ☐ Nein (Laderegler überprüfen)
  
- [ ] **S4.** Nach Laden: Last-Test durchführen (alle Geräte gleichzeitig 5 min an)
  - Spannungs-Abfall: ______ V (sollte <0.5V sein)  
  - Status: ☐ OK  ☐ Zu groß (Kabel überprüfen)

#### Phase 2: Elektronik-Systeme Hochfahren (1.5 Stunden)

- [ ] **S5.** Alle Elektronik-Stecker überprüfen (fest, keine Korrosion, Kappen entfernen)
  - Status: ☐ Alle OK  ☐ Verdächtige Stecker found  
  - Problematische Stecker: _____________
  
- [ ] **S6.** Antennenstecker-Kappen entfernen
  - Status: ☐ GPS  ☐ Radar  ☐ VHF  ☐ Sonstige
  
- [ ] **S7.** Hauptstromschalter auf AN stellen
  - Status: ☐ Bestätigt AN
  
- [ ] **S8.** GPS/Plotter hochfahren (sollte 30 Sekunden starten)
  - Start-Zeit: ______ Sekunden  
  - Status: ☐ Normal  ☐ Verzögert  ☐ Fehler
  
- [ ] **S9.** GPS-Signal überprüfen (HDOP-Wert)
  - HDOP-Wert: ______ (sollte <3 sein nach 1 min Betrieb)  
  - Status: ☐ OK  ☐ Langsam  ☐ Fehler
  
- [ ] **S10.** Radar hochfahren und Selbsttest durchführen
  - Start-Zeit: ______ Sekunden  
  - Rotation normal? ☐ Ja  ☐ Nein (ruckelig/blockiert)  
  - Status: ☐ OK  ☐ Probleme beobachtet
  
- [ ] **S11.** Autopilot hochfahren und Funktionsprüfung (10 min stabiler Kurs-Betrieb)
  - Status: ☐ Stabil  ☐ Oszilliert leicht  ☐ Pendelt stark  ☐ Nicht funktionsfähig
  
- [ ] **S12.** VHF-Funk überprüfen (Durchfunken mit bekanntem Funkpartner)
  - Reichweite: ______ nm  
  - Qualität: ☐ Klar  ☐ Mit Rauschen  ☐ Schwach
  
- [ ] **S13.** NMEA-Netzwerk überprüfen (alle Geräte verbunden)
  - Verbundene Geräte: _____________  
  - Fehler-Meldungen? ☐ Keine  ☐ Minor  ☐ Critical
  
- [ ] **S14.** Backup-Systeme überprüfen (Hand-GPS, Paper-Karten, etc.)
  - Status: ☐ Alle OK  ☐ Batterie schwach  ☐ Nicht vorhanden

#### Phase 3: Detaillierte Funktionsprüfung (2 Stunden)

- [ ] **S15.** Kompass-Kalibrierungs-Test (Deviation überprüfen)
  - Abweichung: ______ ° (sollte <2° sein)  
  - Kalibrierung durchgeführt? ☐ Nein  ☐ Ja (Datum: __________)
  
- [ ] **S16.** Autopilot Stabilität Test (30 min Fahrt in verschiedenen See-Bedingungen)
  - Test-Bedingungen: ☐ Ruhiges Wasser  ☐ Leichte See  ☐ Normaler Seegang  
  - Stabilität: ☐ Exzellent  ☐ Gut  ☐ Fair  ☐ Problematisch
  
- [ ] **S17.** Radar-Reichweitentest (bekannte Objekt in bekannter Distanz)
  - Test-Objekt: ____________  Entfernung: ______ nm  
  - Radar-Reichweite: ______ nm (sollte mind. 20 nm bei größeren Objekten)  
  - Status: ☐ Normal  ☐ Reduziert  ☐ Kein Signal
  
- [ ] **S18.** GPS-Genauigkeit Test (vergleiche Chart-Position mit realer Position)
  - Positionierungs-Genauigkeit: ±______ m  
  - Status: ☐ <10m  ☐ 10–20m  ☐ >20m (ggfs. Antenne überprüfen)
  
- [ ] **S19.** Alle Datenübertragungs-Verbindungen testen (falls WiFi/Bluetooth vorhanden)
  - Status: ☐ Verbunden  ☐ Intermittierende Fehler  ☐ Nicht funktionsfähig
  
- [ ] **S20.** Firmware-Versionen überprüfen (Updates verfügbar?)
  - Geräte mit alten Versionen: _____________  
  - Updates geplant? ☐ Nein  ☐ Ja (nach Saison-Start)

#### Phase 4: Kabel & Stecker Überprüfung (1 Stunde)

- [ ] **S21.** Alle Antennenkabel auf Beschädigungen überprüfen (visuell + Ohm-Messer)
  - Status: ☐ OK  ☐ Verdächtig  ☐ Unterbrochen
  
- [ ] **S22.** Stromkabel überprüfen (Isolationen, Anschlüsse)
  - Status: ☐ OK  ☐ Minor defects  ☐ Kritisch
  
- [ ] **S23.** Kabel-Befestigungen überprüfen (zu straff? lockern bei Bedarf)
  - Status: ☐ OK  ☐ Nachgezogen  ☐ Gelockert
  
- [ ] **S24.** Alle Stecker-Kontakte mit Kontakt-Spray behandeln (Schutzfilm)
  - Status: ☐ Erledigt  ☐ Teilweise  ☐ Nicht erledigt

#### Phase 5: Dokumentation & Planung (0.5 Stunden)

- [ ] **S25.** Alle Inspektions-Ergebnisse dokumentieren
  - Dokumentiert? ☐ Ja  ☐ Nein
  
- [ ] **S26.** Probleme/Befunde für Reparatur-Planung notieren
  - Gefundene Probleme: _____________
  - Reparatur-Priorität: ☐ Sofort  ☐ Vor nächster Langfahrt  ☐ Später im Sommer
  
- [ ] **S27.** Nächste Wartungs-Termine planen
  - Halbjährliche Überprüfung geplant? ☐ Ja (Datum: __________)  ☐ Nein
  - Jährliche Inspektion geplant? ☐ Ja (Datum: __________)  ☐ Nein
  
- [ ] **S28.** Test-Fahrt planen (vor längerer Fahrt)
  - Test-Fahrt geplant? ☐ Ja (Datum: __________)  ☐ Nein
  - Dauer mind. 2–4 Stunden, ruhiges Wasser

**Inbetriebnahme-Abschluss:**

- **Gesamtstatus:** ☐ Vollständig  ☐ Mit kleineren Mängeln  ☐ Kritische Befunde (nicht fahrtbereit)
- **Boot fahrtbereit?** ☐ Ja  ☐ Nein (Gründe: _____________)
- **Inbetriebnahme-Datum:** ______________
- **Durchgeführt durch:** ___________________
- **Nächste Kontrolle geplant:** ______________

---

## 23. Hersteller-spezifische Wartungshinweise

### 23.1 Raymarine Systeme (Axiom, Element, Hybridtouch)

**Spezielle Wartungs-Charakteristiken:**

**Festplatte/SD-Karten:**
- Raymarine Plotter verwenden oft microSD-Karten für Kartendaten
- **Empfehlung:** Jährlich Kartendaten auf externe Festplatte sichern
- **Problem-Indikator:** "Database not found" oder verzögertes Laden → SD-Karte möglicherweise falsch erkannt
  - Lösung: Karte ausbauen, mit Computer formatieren (FAT32), neu einsetzen

**Firmware-Updates:**
- Raymarine releases Firmware ca. 1–2× pro Jahr
- **Wichtig:** IMMER mit vollgeladener Batterie updaten (Spannungs-Abfall während Update kann zur Beschädigung führen)
- Update-Datei auf USB-Stick kopieren, über Service-Menü (Service → System → Software Update) laden

**Stecker-Wartung (Mutter-Stecker R2 und R4):**
- Raymarine verwendet proprietäre Mutter-Stecker
- **Monatlich:** Mit Kontakt-Spray (z.B. WD-40 oder Electrolube) sprühen
- **Jährlich:** Stecker mit Kontakt-Reiniger ausspülen, 10× einstecken/rausziehen zum Polieren

**Touchscreen-Probleme:**
- **Problem:** Touchscreen reagiert ungenau oder flächenweise nicht
- **Häufige Ursache:** Salzwasser-Ablagerungen unter Displayschutz
- **Lösung:** Mit feinem Tuch + destilliertes Wasser abwischen, komplett trocknen lassen

**Batterie-Management:**
- Raymarine MFD sollte 12V ±10% stabilität haben
- **Warnung:** Wenn Spannungs-Ripple >0.5V zeigt Display-Flimmern
- **Fix:** Stromkabel überprüfen (breiter Querschnitt, <2m Länge bevorzugt)

---

### 23.2 Garmin Systeme (GPSMAP, Echomap, Dragonfly)

**Spezielle Eigenschaften:**

**GPS-Modul Überhitzung:**
- Garmin GPS-Module können bei direkter Sonneneinstrahlung >50°C erreichen
- **Empfehlung:** Plotter nicht permanent im Freien lassen, Abdeckung verwenden
- **Symptom:** Plotter schaltet sich aus bei Wärmestau → Überhitzungsschutz aktiviert

**Software-Updates:**
- Garmin basEcamp Software aus Garmin.com laden, Geräte per USB updaten
- **Wichtig:** basEcamp ist kompatibel mit älteren Geräten (bis 5 Jahre alt), danach ggfs. Update notwendig
- **Kartendaten:** Jährlich map-Updates überprüfen (kostenpflichtig: ~€50–150 pro Jahr)

**Echomap Spezifika (mit Fischfinder):**
- Transducer-Stecker (gelber, proprietärer Anschluss) anfällig für Korrosion
- **Monatlich:** Kontakt-Spray auftragen, Stecker-Kappe versichern (gehört oft ab)
- **Problem:** Kein Fischfinder-Signal → oft ist Transducer-Verbindung korrodiert, nicht Hardware-Fehler

**Garmin GPSMAP 8xxx / 9xxx Sonder-Eigenschaften:**
- Große Displays (8"+ Diagonal) anfällig für Kondensation bei Temperaturwechsel
- **Sommer zu Winter:** Elektronik langsam abkühlen lassen, nicht sofort ins kalte Freie
- **Winter zu Sommer:** Ähnlich, nicht in warme Sonne stellen vor vorsichtigem Erwärmen

**Netzwerk-Probleme:**
- Garmin nutzt NMEA 0183 oder NMEA 2000 (je Modell)
- **Häufiger Fehler:** "Device not found" bei N2K-Netzwerk
  - Lösung: Terminatoren überprüfen (beide Enden des Backbone sollten 120Ω Widerstand haben)

---

### 23.3 Simrad Systeme (NSO2, NSO3, NSE, NX)

**Spezielle Wartungs-Punkte:**

**Fiber-Optic Netzwerk (bei NSO3+):**
- Simrad NSO3+ verwendet optisches Netzwerk (schneller, EMV-resistenter als NMEA 2000)
- **Vorsicht:** Optische Fasern sind anfällig für Verschmutzung
- **Wartung:** Stecker-Enden nicht berühren, mit speziellem optischem Tuch reinigen
- **Problem-Indikator:** "Fiber link down" → Stecker überprüfen, ggfs. austauschen (Kosten: €150–300)

**Keyboard/Touch-Ergonomie:**
- Simrad Systeme bieten Hardware-Tasten UND Touchscreen
- **Empfehlung:** Hardware-Tasten bei Salzwasser verwenden (Touchscreen durch Salzwasser-Spray anfällig)
- **Wartung:** Keyboard-Spalten monatlich mit Druckluft reinigen

**Sounder / Transducer:**
- Simrad Fishfinder wird oft mit NSE/NSO integriert
- **Standard-Transducer:** 200 kHz (Standard) oder 83 kHz (Tiefbereichsgeräte)
- **Wartung:** Transducer-Durchtrittsstelle überprüfen (Verschleimung durch Algen in Süßwasser-Seen)

**WiFi-Modul (WM4 Wireless Module):**
- Nur bei NSO3 mit WiFi-Modul
- **Problem:** WiFi-Verbindung intermittierend → Antenne-Platzierung überprüfen (mind. 1m Abstand zu anderen Antennen)
- **Lösung:** WiFi-Antenne höher oder entfernt montieren

---

### 23.4 B&G (Navico) Systeme (Zeus, Triton, Zeus2, Triton2)

**Spezielle Eigenschaften:**

**NMEA 2000 Integrationen:**
- B&G Systeme sind Navico-Marke (wie Simrad), aber Zeus-Serie hat eigenes Ökosystem
- **Wichtig:** B&G Systeme benötigen Navico-spezifische Firmware (nicht Simrad/Lowrance)

**Autopilot-Integration mit Zeus:**
- B&G bietet 1-Kabel-Lösungen (Autopilot-Servo direkt am Plotter-Interface)
- **Wartung:** Servo-Kabel sollte getrennt von Stromleitungen routiert sein (EMV)
- **Problem:** Autopilot-Ruck/Stottern → NMEA-Frequenz überprüfen (sollte >10 Hz sein)

**Radar-Integrationen:**
- B&G kann Radar direkt über NMEA 2000 integrieren (kein separates Antennenkabel nötig bei neueren Radaren)
- **Wartung:** Radar-Status im Netzwerk überprüfen (Device-Info → Radar)

---

### 23.5 Furuno Systeme (Navnet, FMD, DFF series)

**Spezielle Wartungs-Punkte:**

**Navnet TZtouch:**
- Ältere Generation Furuno, wird noch auf vielen Booten betrieben
- **Update-Problem:** Furuno stellte Support 2020 ein, neue Kartendaten kaufen ist schwierig
- **Empfehlung:** Evtl. zu modernerem System upgraden (Navnet TZtouch2)

**Firmware-Updates über Fumado:**
- Furuno nutzt Fumado-Software (ähnlich wie Garmin basEcamp)
- **Wichtig:** Updates sind oft größer (~500 MB), sicheres Update-Szenario notwendig
- **Vorsicht:** Stromausfall während Update kann Modul beschädigen

**DFF1-Fishfinder Spezifika:**
- Älteres Fishfinder-Modell mit analogem Output
- **Problem:** Keine Netzwerk-Verbindung zu modernen Plottern ohne Adapter
- **Lösung:** Furuno NMEA-Adapter (kostenpflichtig, ~€200)

---

## 24. Erweiterte Pydantic v2 Modelle für Electronics-Management

Hier sind 5 neue spezialisierte Modelle für professionelle Elektronik-Verwaltung:

```python
from pydantic import BaseModel, Field, field_validator
from datetime import datetime, timedelta
from typing import Optional, List, Dict
from enum import Enum

# ============================================================================
# Model 1: MaintenanceSchedule
# ============================================================================
class MaintenanceFrequency(str, Enum):
    DAILY = "daily"
    WEEKLY = "weekly"
    BIWEEKLY = "biweekly"
    MONTHLY = "monthly"
    QUARTERLY = "quarterly"
    BIANNUALLY = "biannually"
    ANNUALLY = "annually"
    TRIANNUALLY = "every_3_years"
    ASNEEDED = "as_needed"

class MaintenanceTask(BaseModel):
    """Individual maintenance task definition"""
    task_id: str = Field(..., description="Unique identifier for task")
    task_name: str = Field(..., description="Human-readable task name (German)")
    frequency: MaintenanceFrequency = Field(..., description="How often task should be performed")
    estimated_hours: float = Field(ge=0.1, le=40, description="Estimated time in hours")
    estimated_cost_eur: Optional[float] = Field(None, ge=0, description="Estimated cost in EUR")
    required_tools: List[str] = Field(default_factory=list, description="Tools/equipment needed")
    risk_if_skipped: str = Field(..., description="What happens if maintenance is skipped (German)")
    boat_class_applicability: List[str] = Field(
        default_factory=list,
        description="Boat classes where this applies (e.g. ['production_8m', 'custom_18m'])"
    )
    
    model_config = {"from_attributes": True}

class MaintenanceSchedule(BaseModel):
    """Complete maintenance schedule for a boat's electronics system"""
    schedule_id: str = Field(..., description="Unique identifier")
    boat_id: str = Field(..., description="Associated boat ID")
    boat_class: str = Field(..., description="Boat class/category")
    created_at: datetime = Field(default_factory=datetime.utcnow)
    last_updated: datetime = Field(default_factory=datetime.utcnow)
    
    tasks: List[MaintenanceTask] = Field(
        default_factory=list,
        description="List of all maintenance tasks"
    )
    
    next_task_due: Optional[datetime] = Field(None, description="Next scheduled maintenance")
    tasks_overdue: int = Field(0, description="Count of overdue tasks")
    
    annual_maintenance_hours: float = Field(0, description="Estimated annual maintenance hours")
    annual_maintenance_budget_eur: float = Field(0, description="Estimated annual budget")
    
    @field_validator('next_task_due')
    @classmethod
    def validate_next_task(cls, v, info):
        if v and v < datetime.utcnow():
            return None  # Overdue tasks set to None
        return v
    
    model_config = {"from_attributes": True}


# ============================================================================
# Model 2: ElectronicInventory
# ============================================================================
class ComponentWarranty(BaseModel):
    """Warranty information for a component"""
    start_date: datetime
    end_date: datetime
    coverage_type: str = Field(..., description="e.g., 'full', 'parts_only', 'labor_included'")
    warranty_provider: Optional[str] = Field(None, description="Manufacturer or third-party warranty")
    
    model_config = {"from_attributes": True}

class ComponentLocationCode(str, Enum):
    """Standard location codes for electronics"""
    ELECTRONICS_BOX = "electronics_box"
    MAST_TOP = "mast_top"
    HULL_MOUNTED = "hull_mounted"
    CABIN = "cabin"
    ENGINE_ROOM = "engine_room"
    DECK = "deck"
    THROUGH_HULL = "through_hull"
    ANTENNA_ARRAY = "antenna_array"

class ElectronicComponent(BaseModel):
    """Inventory record for a single electronic component"""
    component_id: str = Field(..., description="Unique ID (e.g., 'gps_001')")
    component_type: str = Field(..., description="Type (e.g., 'GPS_Receiver', 'Radar', 'VHF')")
    manufacturer: str
    model_number: str
    serial_number: Optional[str] = Field(None)
    
    purchase_date: Optional[datetime] = Field(None)
    purchase_price_eur: Optional[float] = Field(None, ge=0)
    
    installation_date: datetime
    installation_location: ComponentLocationCode
    
    estimated_lifespan_years: int = Field(..., ge=1, le=30)
    age_years: float = Field(0, description="Current age calculated from installation_date")
    
    warranty: Optional[ComponentWarranty] = Field(None)
    
    last_service_date: Optional[datetime] = Field(None)
    next_service_date: Optional[datetime] = Field(None)
    
    power_consumption_watts: Optional[float] = Field(None, ge=0, le=5000)
    power_supply_voltage: str = Field(..., description="e.g., '12V', '24V', '110V'")
    
    firmware_version: Optional[str] = Field(None, description="Current firmware/software version")
    firmware_last_updated: Optional[datetime] = Field(None)
    
    health_score: float = Field(
        default=100,
        ge=0,
        le=100,
        description="0-100 health indicator based on age and maintenance"
    )
    
    notes: Optional[str] = Field(None, description="Additional notes (German)")
    
    model_config = {"from_attributes": True}

class ElectronicInventory(BaseModel):
    """Complete inventory of all electronics on a boat"""
    inventory_id: str = Field(..., description="Unique identifier")
    boat_id: str = Field(..., description="Associated boat ID")
    
    created_at: datetime = Field(default_factory=datetime.utcnow)
    last_inventory_date: datetime = Field(default_factory=datetime.utcnow)
    
    components: List[ElectronicComponent] = Field(
        default_factory=list,
        description="All installed components"
    )
    
    total_power_consumption_watts: float = Field(0, description="Sum of all components")
    average_system_health: float = Field(100, ge=0, le=100, description="Average health score")
    
    components_due_for_service: List[str] = Field(
        default_factory=list,
        description="Component IDs with overdue service"
    )
    components_approaching_eol: List[str] = Field(
        default_factory=list,
        description="Components >80% through lifespan"
    )
    
    model_config = {"from_attributes": True}


# ============================================================================
# Model 3: WarrantyTracker
# ============================================================================
class WarrantyRecord(BaseModel):
    """Individual warranty claim or tracking record"""
    warranty_record_id: str
    component_id: str
    warranty_start: datetime
    warranty_end: datetime
    
    claim_date: Optional[datetime] = Field(None)
    claim_approved: Optional[bool] = Field(None)
    claim_amount_eur: Optional[float] = Field(None, ge=0)
    claim_notes: Optional[str] = Field(None, description="Notes in German")
    
    model_config = {"from_attributes": True}

class WarrantyTracker(BaseModel):
    """Warranty management system for all electronics"""
    tracker_id: str = Field(..., description="Unique identifier")
    boat_id: str
    
    warranty_records: List[WarrantyRecord] = Field(
        default_factory=list,
        description="All warranty records"
    )
    
    active_warranties_count: int = Field(0)
    expired_warranties_count: int = Field(0)
    warranties_expiring_within_months: List[WarrantyRecord] = Field(
        default_factory=list,
        description="Warranties expiring within 6 months"
    )
    
    total_warranty_value_eur: float = Field(0, description="Total value of active warranties")
    total_claimed_amount_eur: float = Field(0, description="Total warranty claims paid")
    
    last_updated: datetime = Field(default_factory=datetime.utcnow)
    
    model_config = {"from_attributes": True}


# ============================================================================
# Model 4: FirmwareHistory
# ============================================================================
class FirmwareVersion(BaseModel):
    """Single firmware version record"""
    version_string: str = Field(..., description="e.g., '5.2.1'")
    release_date: datetime
    is_current: bool = Field(False)
    is_stable: bool = Field(True)
    known_issues: Optional[List[str]] = Field(None, description="Known bugs/issues (German)")
    changelog: Optional[str] = Field(None, description="Change summary (German)")
    
    model_config = {"from_attributes": True}

class FirmwareHistory(BaseModel):
    """Firmware upgrade history for a single component"""
    component_id: str
    component_name: str
    manufacturer: str
    
    current_version: FirmwareVersion
    
    version_history: List[FirmwareVersion] = Field(
        default_factory=list,
        description="Historical versions installed"
    )
    
    last_update_date: datetime = Field(default_factory=datetime.utcnow)
    last_update_notes: Optional[str] = Field(None, description="Update notes (German)")
    
    update_available: bool = Field(False, description="New firmware version available?")
    available_version: Optional[FirmwareVersion] = Field(None)
    
    auto_update_enabled: bool = Field(False)
    update_frequency_days: Optional[int] = Field(None, ge=1, le=365)
    
    model_config = {"from_attributes": True}

class FirmwareTracker(BaseModel):
    """Tracks firmware versions across all electronics"""
    tracker_id: str
    boat_id: str
    
    component_firmware: List[FirmwareHistory] = Field(
        default_factory=list,
        description="Firmware history for each component"
    )
    
    components_with_updates_available: int = Field(0)
    last_system_check: datetime = Field(default_factory=datetime.utcnow)
    
    model_config = {"from_attributes": True}


# ============================================================================
# Model 5: SystemHealthScore
# ============================================================================
class ComponentHealthAssessment(BaseModel):
    """Health assessment for a single component"""
    component_id: str
    component_name: str
    component_type: str
    
    age_score: float = Field(..., ge=0, le=100, description="100 = new, 0 = at end of life")
    maintenance_score: float = Field(..., ge=0, le=100, description="100 = all maintenance current")
    reliability_score: float = Field(..., ge=0, le=100, description="100 = no known issues")
    performance_score: float = Field(..., ge=0, le=100, description="100 = full performance")
    
    overall_health: float = Field(..., ge=0, le=100, description="Weighted average of above scores")
    
    risk_level: str = Field(..., description="LOW, MEDIUM, HIGH, CRITICAL")
    recommended_action: str = Field(..., description="Maintenance/replacement recommendation (German)")
    
    model_config = {"from_attributes": True}

class SystemHealthScore(BaseModel):
    """Overall electronics system health assessment"""
    health_score_id: str = Field(..., description="Unique identifier")
    boat_id: str
    assessment_date: datetime = Field(default_factory=datetime.utcnow)
    assessment_type: str = Field(..., description="e.g., 'annual_inspection', 'pre_voyage', 'insurance_appraisal'")
    
    component_assessments: List[ComponentHealthAssessment] = Field(
        default_factory=list,
        description="Health assessment per component"
    )
    
    system_overall_health: float = Field(..., ge=0, le=100, description="Weighted system health")
    system_risk_level: str = Field(..., description="LOW, MEDIUM, HIGH, CRITICAL")
    
    critical_findings: List[str] = Field(
        default_factory=list,
        description="Critical issues requiring immediate attention (German)"
    )
    
    recommended_maintenance_items: List[str] = Field(
        default_factory=list,
        description="Prioritized list of maintenance tasks (German)"
    )
    
    estimated_maintenance_budget_next_12_months_eur: float = Field(0, ge=0)
    
    confidence_level: float = Field(
        default=0.75,
        ge=0.0,
        le=1.0,
        description="Confidence in assessment (0.0-1.0)"
    )
    confidence_notes: Optional[str] = Field(
        None,
        description="Why confidence may be lower (German)"
    )
    
    assessed_by: Optional[str] = Field(None, description="Technician name/ID")
    next_assessment_recommended: Optional[datetime] = Field(None)
    
    model_config = {"from_attributes": True}
```

---

**Dokumentation erweitert: Zeilen 2,717 → ~3,850 (ca. +1,130 Zeilen)**

Geschrieben für AYDI v6 Backend. Deutsche Wartungs-Texte, englischer Code. Alle Pydantic v2 Modelle verwenden `model_config = {"from_attributes": True}`. Standards folgen CE-Richtlinien 2013/53/EU.
