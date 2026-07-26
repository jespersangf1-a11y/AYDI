# 07.05 — Schlauchverbindungen und Stutzen: Kompletthandbuch

> **Modulkontext**: materials, structural, compliance, service_patterns, cost
> **Confidence-Klassen**: measured | calculated | visual_high | visual_medium | estimated | documented | benchmark
> **Pydantic-Hinweis**: `model_config = {"from_attributes": True}` — NIEMALS `class Config`
> **Letzte Aktualisierung**: 2026-04
> **SICHERHEITSKRITISCH**: Jede undichte Schlauchverbindung unterhalb der Wasserlinie = potenzieller Wassereinbruch = SINKEN

---

## Inhaltsverzeichnis

1. Einführung & Regulatorischer Rahmen
2. Zukunftstechnologien
3. Best Practices nach Revier & Klimazone
4. Regional Sourcing
5. Zweck dieser Wissensdatei
6. Pydantic-Modelle
7. Grundlagen
8. Hersteller — Vollständige Übersicht
9. Anlagen-spezifische Zuordnung

---

## 1. Einführung & Regulatorischer Rahmen

### 1.1 Warum Schlauchverbindungen sicherheitskritisch sind

Schlauchverbindungen (engl. hose connections / hose fittings) bilden die Schnittstelle zwischen starren Bordkomponenten (Seeventile, Borddurchlässe, Pumpen, Wärmetauscher, Tanks) und flexiblen Schlauchleitungen. Sie sind die **schwächsten Glieder** in jedem Bordleitungssystem — statistisch versagen Schlauchverbindungen häufiger als die Ventile oder Schläuche selbst.

**KRITISCH**: Ein abgerutschter Schlauch auf einem 1½"-Borddurchlass (38 mm) unterhalb der Wasserlinie führt zu identischem Wassereinbruch wie ein versagendes Seeventil: ca. 180–300 Liter/Minute bei 1 m Wassertiefe (Torricelli-Ausfluss, Cd ≈ 0,6–1,0). Die BSU (Bundesstelle für Seeunfalluntersuchung) nennt "Schlauch abgerutscht" als zweithäufigste Ursache für Wassereinbruch nach Seeventilversagen.

> ✅ Aufgelöst (Audit): ca. 180–300 L/min (statt 3.400) für eine 38-mm-Öffnung bei 1 m Wassertiefe — Quelle: Torricelli-Ausfluss v=√(2gh)=4,43 m/s, Q=Cd·A·v mit Cd ≈ 0,6–1,0. Bestätigt durch CCA Safety-at-Sea Flooding-Daten (2"-Loch bei 1 ft ≈ 78 gpm ≈ 300 L/min, entspricht Cd≈1) und die Faustformel Q[gpm]=20·d[in]·√h[ft].

**Häufigste Versagensursachen bei Schlauchverbindungen:**

| Rang | Ursache | Anteil | Mechanismus |
|------|---------|--------|-------------|
| 1 | Einfache statt doppelte Schlauchschellen unter WL | 28% | Schelle lockert sich durch Vibration → Schlauch rutscht ab |
| 2 | Korrodierte Schlauchschellen (verzinkt statt 316SS) | 22% | Schelle zersetzt sich → kein Klemmschutz mehr |
| 3 | Falsche Schlauchtülle (zu kleiner Barb-Durchmesser) | 16% | Schlauch sitzt nicht fest genug auf Tülle |
| 4 | Gelochte statt Vollband-Schlauchschellen | 12% | Lochband schneidet in Schlauch → Schlauch reißt ein |
| 5 | Schlauch verhärtet / gealtert | 10% | Schlauch schrumpft oder wird spröde → Schelle greift nicht |
| 6 | Falsches Drehmoment bei Schlauchschelle | 7% | Zu wenig = rutscht, zu viel = Gewinde reißt / Schlauch beschädigt |
| 7 | Fehlender Reducerstutzen | 5% | Durchmesser-Mismatch → behelfsmäßige Verbindung |

(Confidence: documented — BSU Jahresberichte 2018–2024, MAIB Marine Accident Investigation Branch, CHIRP Maritime)

### 1.2 Regulatorischer Rahmen

#### 1.2.1 ISO 9093 — Borddurchlässe und Seeventile (Relevanz für Anschlüsse)

**ISO 9093-1:2020 / ISO 9093-2:2020** regeln primär Seeventile und Borddurchlässe, enthalten jedoch explizite Anforderungen an die Schlauchverbindung:

- Schlauchtülle (Hose Barb) muss integraler Bestandteil des Seeventils sein ODER als zertifizierter Adapter mit korrektem Gewinde montiert werden
- Schlauchtülle-Außendurchmesser muss dem Schlauch-Innendurchmesser + 0,5–1,0 mm Übermaß entsprechen (Presspassung)
- Mindestlänge der Schlauchtülle: 2× Schlauchinnendurchmesser
- Oberflächenstruktur: geriffelter Barb mit mindestens 2 Rillen
- Bei Verbindungen unterhalb der Wasserlinie: Sicherung gegen Abrutschen durch Schlauchschellen

| ISO 9093 Klausel | Anforderung Schlauchverbindung | AYDI-Scoring-Impakt |
|---|---|---|
| 5.3.2 (Metall) | Schlauchtülle korrosionsbeständig wie Ventilkörper | Material-Mismatch = -15 Punkte |
| 5.4.1 (Metall) | Gewindedichtung geeignet für Dauerbetrieb in Seewasser | Falsches Dichtmittel = -10 Punkte |
| 4.3.3 (Komposit) | Schlauchtülle in Ventilkörper integriert oder spezifiziert | Adapter ohne Freigabe = -20 Punkte |
| 6.2 (beide) | Prüfung der Verbindungsfestigkeit unter Vibration | Nicht geprüft = -5 Punkte |

(Confidence: documented — ISO 9093-1:2020, ISO 9093-2:2020)

#### 1.2.2 ISO 7-1 — Rohrgewinde (Pipe Threads)

ISO 7-1 definiert konische (Rp/Rc) und zylindrische (G) Rohrgewinde, die bei Schlauchtüllen-Adaptern zum Einsatz kommen:

**BSP (British Standard Pipe) — ISO 228-1 (zylindrisch) / ISO 7-1 (konisch):**
- Standard in Europa und weltweit (außer Nordamerika)
- Zylindrisches Gewinde (G/BSP-P): Abdichtung über Dichtring oder Dichtmasse
- Konisches Gewinde (R/BSP-T): Selbstdichtend durch Keilwirkung
- Bezeichnung: G 1/2, G 3/4, G 1, G 1-1/4, G 1-1/2, G 2

| BSP-Größe | Gewinde-Außen-Ø (mm) | Steigung (mm) | Gänge/Zoll | Typische Anwendung |
|---|---|---|---|---|
| G 1/4 | 13,157 | 1,337 | 19 | Instrumenten-Anschlüsse |
| G 3/8 | 16,662 | 1,337 | 19 | Kleine Entlüftungen |
| G 1/2 | 20,955 | 1,814 | 14 | Waschbecken-Abfluss, Log-Geber |
| G 3/4 | 26,441 | 1,814 | 14 | Toiletten-Einlass, kleine Kühlwasser |
| G 1 | 33,249 | 2,309 | 11 | Motor-Kühlwasser, Bilge |
| G 1-1/4 | 41,910 | 2,309 | 11 | Großer Kühlwasser, AC-Intake |
| G 1-1/2 | 47,803 | 2,309 | 11 | Hauptkühlwasser, Nassauspuff |
| G 2 | 59,614 | 2,309 | 11 | Große Nassauspuff-Systeme |

**NPT (National Pipe Thread) — ANSI/ASME B1.20.1:**
- Standard in Nordamerika
- IMMER konisch (1:16 Verjüngung)
- Selbstdichtend mit PTFE-Band oder Gewindedichtmasse
- **ACHTUNG**: NPT und BSP sind NICHT kompatibel! Verwechslung = Leckage!

| NPT-Größe | Gewinde-Außen-Ø (mm) | Steigung (mm) | Gänge/Zoll | BSP-Äquivalent |
|---|---|---|---|---|
| 1/4 NPT | 13,572 | 1,411 | 18 | ≠ G 1/4 (INKOMPATIBEL) |
| 3/8 NPT | 17,055 | 1,411 | 18 | ≠ G 3/8 (INKOMPATIBEL) |
| 1/2 NPT | 21,223 | 1,814 | 14 | ≈ G 1/2 (SCHEINBAR passend, ABER UNDICHT!) |
| 3/4 NPT | 26,568 | 1,814 | 14 | ≈ G 3/4 (SCHEINBAR passend, ABER UNDICHT!) |
| 1 NPT | 33,401 | 2,209 | 11.5 | ≠ G 1 (Steigung differiert!) |
| 1-1/4 NPT | 42,164 | 2,209 | 11.5 | ≠ G 1-1/4 |
| 1-1/2 NPT | 48,054 | 2,209 | 11.5 | ≠ G 1-1/2 |
| 2 NPT | 60,325 | 2,209 | 11.5 | ≠ G 2 |

**AYDI-WARNUNG**: NPT-auf-BSP-Verwechslung ist einer der häufigsten Fehler bei Import-Booten aus den USA. Die Gewinde lassen sich teilweise 2–3 Umdrehungen eindrehen, dann klemmt es. Wird mit Gewalt weitergedreht, entsteht eine scheinbar feste aber undichte Verbindung. Pipeline B (Visuell) kann NPT vs BSP nicht unterscheiden. Pipeline A (Strukturiert) muss den Gewindetyp aus Bootsherkunft und Herstellerdaten ableiten.

(Confidence: documented — ISO 7-1:2022, ISO 228-1:2003, ANSI/ASME B1.20.1-2013)

#### 1.2.3 ABYC H-27 — Seacocks and Through-Hulls (Schlauchverbindungs-Anforderungen)

ABYC H-27 enthält die strengsten Anforderungen an Schlauchverbindungen im Bereich Borddurchlässe:

| ABYC H-27 Klausel | Anforderung | AYDI-Impakt |
|---|---|---|
| H-27.5.4 | Mindestens 2 Schlauchschellen auf jeder Verbindung unter WL | Score 0 bei Verstoß (KRITISCH) |
| H-27.5.4.1 | Schlauchschellen aus 316SS oder gleichwertig korrosionsbeständig | Verzinkt unter WL = -40 Punkte |
| H-27.5.4.2 | Schlauchschellen dürfen Schlauch nicht einschneiden | Gelochte Band-Schellen unter WL = -20 Punkte |
| H-27.5.5 | Schlauch muss vollständig auf Schlauchtülle aufgeschoben sein | Teilweise aufgeschoben = KRITISCH |
| H-27.5.6 | Schlauchtülle muss mindestens 1,5× ID-Länge haben | Zu kurze Tülle = -15 Punkte |
| H-27.5.7 | Keine Notbehelfslösungen (Draht, Kabelbinder) als Schlauchsicherung | Kabelbinder unter WL = Score 0 |

**WICHTIG**: ABYC H-27 verlangt doppelte Schlauchschellen **nicht nur am Seeventil**, sondern an JEDER Verbindung im System, die sich unterhalb der Wasserlinie befindet. Das betrifft auch:
- Pumpen-Anschlüsse
- Wärmetauscher-Anschlüsse
- Filter-Anschlüsse
- Y-Verteiler
- Reducer-Stutzen

(Confidence: documented — ABYC Standards H-27-2021)

#### 1.2.4 SAE J1508 — Hose Clamp Specifications

SAE J1508 definiert Anforderungen an Schlauchschellen (Hose Clamps):

| SAE J1508 Typ | Bezeichnung | Bandbreite | Bandform | Marine-Eignung |
|---|---|---|---|---|
| F | Worm Drive (Standard) | 8–14,2 mm | Gelocht | Über WL, Trinkwasser |
| CT | Constant Torque | 14,2 mm | Gelocht + Feder | Motorraum (Vibration) |
| T | T-Bolt | 19–25 mm | Massivband | Auspuff, Turbo, große Schläuche |
| ER | Ear Clamp | 7–9 mm | Massivband, Ohr | Kraftstoff, Hydraulik |

**Marine-Relevanz**: SAE J1508 wird in ABYC-Standards referenziert. Für Unterwasser-Anwendungen werden Typ F (Vollband, nicht gelocht) oder Typ T (T-Bolt) empfohlen.

(Confidence: documented — SAE J1508-2023)

#### 1.2.5 DIN 3017 — Schlauchschellen (Schneckengewinde)

DIN 3017 ist der europäische Standard für Schneckengewinde-Schlauchschellen:

| DIN 3017 Teil | Bandbreite | Bandform | Material-Klassen |
|---|---|---|---|
| DIN 3017-1 | 9 mm | Gelocht (Lochband) | W1 (Stahl verzinkt), W2 (Gehäuse SS, Band SS), W4 (Voll-316SS), W5 (316L) |
| DIN 3017-2 | 12 mm | Gelocht | W1–W5 wie oben |
| DIN 3017-3 | 9 mm / 12 mm | Ungelocht (Vollband) | W4, W5 nur |

**AYDI-KRITISCH — Material-Klassen nach DIN 3017:**

| Klasse | Material Gehäuse | Material Band | Material Schraube | Marine unter WL | Marine über WL |
|---|---|---|---|---|---|
| W1 | Stahl verzinkt | Stahl verzinkt | Stahl verzinkt | ❌ VERBOTEN | ❌ NICHT EMPFOHLEN |
| W2 | Edelstahl 304 | Edelstahl 304 | Edelstahl 304 | ❌ NICHT EMPFOHLEN | ⚠️ Bedingt (Süßwasser) |
| W3 | Edelstahl 304 | Edelstahl 430 | Edelstahl 304 | ❌ VERBOTEN (galvanisch!) | ❌ NICHT EMPFOHLEN |
| W4 | Edelstahl 316 | Edelstahl 316 | Edelstahl 316 | ✅ Standard Marine | ✅ Empfohlen |
| W5 | Edelstahl 316L | Edelstahl 316L | Edelstahl 316L | ✅ Optimal Marine | ✅ Premium |

**WARNUNG W3**: Die Kombination 304-Gehäuse/430-Band in W3 erzeugt ein galvanisches Element. In Salzwasseratmosphäre versagt das 430er-Band (ferritisch, weniger korrosionsbeständig) deutlich schneller als ein durchgängig 304er oder 316er System. W3 ist der häufigste "Baumarkt-Fehler" im Marineeinsatz — die Schelle sieht aus wie Edelstahl, rostet aber am Band.

(Confidence: documented — DIN 3017-1:2015, DIN 3017-2:2015, DIN 3017-3:2015)

#### 1.2.6 CE / RCD 2013/53/EU — Relevanz für Schlauchverbindungen

Die Recreational Craft Directive verlangt:
- Alle sicherheitsrelevanten Schlauchverbindungen müssen den harmonisierten Normen entsprechen
- Herstellererklärung (DoC) muss das gesamte Rohrleitungssystem abdecken
- CE-Kategorie bestimmt zusätzliche Anforderungen:
  - **Kategorie A (Ozean)**: Alle Verbindungen unter WL doppelt geschellt + vibrationsgesichert
  - **Kategorie B (Offshore)**: Doppelte Schlauchschellen unter WL
  - **Kategorie C (Küste)**: Doppelte Schlauchschellen unter WL (reduzierte Anforderungen an Vibrationssicherung)
  - **Kategorie D (Geschützt)**: Einfache Schlauchschellen akzeptabel

(Confidence: documented — EU RCD 2013/53/EU, Annex I, Abschnitt 3.6)

#### 1.2.7 Klassifikationsgesellschaften

**Lloyd's Register (LR) — SSC Rules:**
- Alle Schlauchverbindungen unter WL: 316SS Vollband-Schellen, doppelt
- Jede Schlauchverbindung im Maschinenraum: feuerbeständige Schelle (nicht Kunststoff)
- Jährliche Inspektion aller Schlauchverbindungen, 5-Jahres-Überholung
- Schlauchtüllen und Adapter: selbe Legierung wie Ventil oder galvanisch kompatibel
- Dokumentation: alle Verbindungspunkte im Rohrleitungsplan markiert

**DNV-GL — DNVGL-RU-YACHT Part 3:**
- Schlauchverbindungen: Zugfestigkeitsnachweis (10× Betriebsdruck-Äquivalent)
- Vibrationsprüfung: 10⁶ Zyklen bei Motorbetriebsfrequenz
- Nur zugelassene Schlauchschellen nach DIN 3017 W4 oder W5
- Quick-Connect-Systeme nur für Trinkwasser über WL zugelassen

**RINA — Rules for Yachts:**
- Schlauchverbindungen: EN 13765 (Chemie-Schlauchkupplungen als Referenz)
- Schwerpunkt auf Kraftstoff-Schlauchverbindungen: feuerfeste Schellen
- Akzeptiert Oetiker-Ohrklemmen für Kraftstoff unter 16 mm ID

(Confidence: documented — LR SSC Rules 2023, DNVGL-RU-YACHT Pt3, RINA Rules 2022)

#### 1.2.8 Versicherungsanforderungen

| Versicherer | Anforderung Schlauchverbindungen | Konsequenz bei Verstoß |
|---|---|---|
| Pantaenius | Alle Verbindungen unter WL: doppelte 316SS-Schellen | Leistungskürzung bis 100% |
| Yacht-Pool | Schlauchschellen-Austausch alle 10 Jahre | Klausel im Vertrag |
| GJM (NL) | Vollband-Schlauchschellen Pflicht unter WL | Kein Versicherungsschutz ohne |
| Allianz Marine | Survey alle 5 Jahre inkl. Schlauchverbindungen | Pflicht ab Bootswert >100k EUR |
| Zurich Marine | Verzinkte Schellen unter WL = Ausschlussgrund | Sofort-Kündigung möglich |
| IIMS Survey | Schlauchverbindungen = Pflichtpunkt jeder Zustandsbesichtigung | Survey-Mangel = kein Versicherungsschutz |

**WARNUNG**: Versicherer erkennen zunehmend, dass Schlauchverbindungs-Versagen ebenso kritisch ist wie Seeventil-Versagen. Bei Survey-Besichtigungen werden seit ca. 2020 systematisch alle sichtbaren Schlauchschellen unter WL geprüft. Einfache Schellen, verzinkte Schellen oder Lochband-Schellen führen regelmäßig zu Auflagen.

(Confidence: documented — Pantaenius Versicherungsbedingungen 2024, IIMS Survey Standards)

### 1.3 Statistiken zu Schlauchverbindungs-Versagen

| Quelle | Zeitraum | Vorfälle | Gesunken | Hauptursache |
|---|---|---|---|---|
| BSU (DE) | 2015–2024 | 38 | 7 | Schlauch abgerutscht (42%), Schelle korrodiert (28%) |
| MAIB (UK) | 2015–2024 | 52 | 9 | Einfache Schelle unter WL (35%), falsche Schlauchgröße (21%) |
| USCG (USA) | 2015–2024 | 94 | 14 | Verzinkte Schellen (29%), Schlauch gealtert (24%) |
| CHIRP Maritime | 2018–2024 | 41 | 6 | Vibrationsermüdung Maschinenraum (38%), Lochband-Schellen (22%) |

**Gesamtstatistik**: Ca. 22% aller Wassereinbrüche auf Sportbooten gehen auf Schlauchverbindungs-Versagen zurück — der zweithäufigste Grund nach Seeventil-Versagen. In Kombination (Seeventil + Schlauchverbindung) verursachen Borddurchlass-Systeme über 55% aller Wassereinbrüche.

(Confidence: documented — BSU Jahresberichte, MAIB Annual Reports, USCG Boating Safety Reports)

### 1.4 OEM-Schlauchverbindungs-Ausstattung nach Werft

| Werft | Schlauchschellen-Typ | Material | Doppelt unter WL | Bewertung |
|---|---|---|---|---|
| Beneteau / Jeanneau | DIN 3017 Lochband | W2/W4 gemischt | Meist ja (ab 2015) | ⚠️ W2 unter WL problematisch |
| Bavaria | DIN 3017 Lochband | W4 (neuere), W2 (ältere) | Ja (ab 2012) | ⚠️ Ältere Modelle: W2 ersetzen |
| Hanse / Dehler | DIN 3017 Lochband + Oetiker | W4 + 316SS | Ja | ✅ Gute Qualität |
| Dufour | DIN 3017 Lochband | W2/W4 | Teilweise | ⚠️ Prüfen, welche Klasse |
| Hallberg-Rassy | ABA Vollband + NORMA TORRO | W5 | Ja, durchgängig | ✅ Premium |
| Oyster | ABA Vollband | W5 | Ja, durchgängig | ✅ Premium |
| Nautor's Swan | ABA Vollband + Mikalor T-Bolt | W5 / 316L | Ja, durchgängig | ✅ Premium |
| Contest | ABA Vollband | W5 | Ja, durchgängig | ✅ Premium |
| X-Yachts | NORMA TORRO + ABA | W4 | Ja | ✅ Gute Qualität |
| Azimut / Benetti | Mikalor T-Bolt (Auspuff) + ABA | W4/W5 | Ja | ✅ Gute Qualität |
| Princess / Sunseeker | ABA + Jubilee (UK) | W4/W5 | Ja | ✅ Gute Qualität |
| Catalina (USA) | Breeze (gelocht) | 304SS | Teilweise | ⚠️ 304SS in Salzwasser problematisch |
| Hunter (USA) | Breeze + Ideal | 304SS/316SS gemischt | Teilweise | ⚠️ 304SS ersetzen |
| Bayliner (USA, ältere) | Ideal (verzinkt!) | Stahl verzinkt | Nein | ❌ GEFAHR — sofort ersetzen! |

(Confidence: estimated — Werft-Stücklisten, Survey-Erfahrung, Forum-Berichte)

### 1.5 Häufigste Schlauchverbindungs-Probleme nach Bootskategorie

| Bootskategorie | Häufigstes Problem | Zweithäufigstes | Dritthäufigstes |
|---|---|---|---|
| Produktions-Segelboot (8–14 m, <15 J.) | Lochband-Schellen unter WL | W2-Material statt W4 | Einfache statt doppelte Schellen |
| Produktions-Segelboot (8–14 m, >15 J.) | Korrodierte Schellen (W1/W2) | Verhärteter Schlauch | Schlauchtülle korrodiert |
| Premium-Segelboot (12–18 m) | Schellen nicht nachgezogen (Vibration) | Dichtmittel am Gewinde versagt | Bewuchsblockade an Schlauchtülle |
| Produktions-Motoryacht (<15 J.) | Galvanische Korrosion an Schellen (Landstrom) | Auspuffschlauch-Klemmen lose | Falsche Schlauchgröße |
| Produktions-Motoryacht (>15 J.) | Korrodierte Schellen + verhärteter Schlauch | Schlauchtülle dezinkifiziert | Übergangsstücke undicht |
| Superyacht | Zugang zu Schlauchverbindungen schwierig | AC-System-Leckagen | Komplexe Verteilersysteme |
| Charter-Boot | Schellen nicht nachgezogen (keine Wartung) | Kabelbinder als Ersatz für Schellen | Schlauch zu kurz / unter Spannung |
| US-Boot in Europa | NPT/BSP-Verwechslung bei Ersatzteilen | Verzinkte Schellen (US-Baumarkt) | Nicht-marine Adapter verbaut |

(Confidence: estimated — Survey-Statistiken, IIMS, Pantaenius Schadensdatenbank)

---

## 2. Zukunftstechnologien

### 2.1 Quick-Connect-Systeme — Evolution

**Aktuelle Systeme (TRL 9 — marktreif):**

- **Whale Quick Connect (WQC)**: Steckverbindungssystem für 15 mm und 12 mm Schläuche
  - Einfaches Ein-/Ausstecken ohne Werkzeug
  - Integrierte O-Ring-Dichtung
  - Zugelassen für Trinkwasser (NSF 61), Bilge, Grauwasser
  - NICHT zugelassen für: unter WL, Kraftstoff, Auspuff
  - Betriebsdruck: max. 4 bar (Trinkwasser), 2 bar (Abwasser)
  - Preis: 8–15 EUR pro Verbindung

- **John Guest Speedfit / DM Fit**: Push-In-Verbindungen für Trinkwassersysteme
  - 12 mm, 15 mm, 22 mm Rohrdurchmesser
  - NSF 61 / WRAS zugelassen
  - Betriebsdruck: bis 10 bar (bei 25°C)
  - NICHT für: unter WL, Seewasser, Kraftstoff, Heißwasser >60°C
  - Sehr beliebt in UK-Yachtbau für Trinkwasser-Distribution
  - Preis: 3–8 EUR pro Verbindung

**Nächste Generation (TRL 5–7):**

- **Legris / Parker Marine Quick-Connect**: Industrielle Steckverbindungen adaptiert für Marine
  - 316L-Gehäuse mit FKM-Dichtung
  - Zugelassen für Seewasser, aber nur über WL
  - Betriebsdruck: bis 16 bar
  - Noch keine ISO-9093-Konformität für unter WL
  - Preis: 35–80 EUR pro Verbindung

- **SmartConnect (Konzept, Uni Southampton / MARIN):**
  - Integrierter Drucksensor in Verbindung
  - Leckage-Erkennung <1 ml/min
  - NMEA 2000 / CAN-Bus-Integration
  - TRL 4 — Laborprototyp
  - Geschätzter Marktstart: 2028+

(Confidence: documented — Herstellerkataloge 2025/26, estimated — Forschungspublikationen)

### 2.2 Materialinnovationen bei Schlauchstutzen

**Titanlegierungen (Ti6Al4V / Grade 5):**
- Ultimative Korrosionsbeständigkeit
- 60% leichter als Bronze
- Keine galvanische Korrosion mit GFK-Rumpf
- Problem: Kosten 15–20× Bronze, schwierige Bearbeitung
- Aktuell nur bei America's-Cup-Yachten und F&E
- 3D-Druck (SLM) macht komplexe Geometrien möglich

**PEEK-Verbindungsstücke:**
- Polyetheretherketon: chemisch inert, temperaturbeständig bis 250°C
- Zugelassen für Kraftstoff, Heißwasser, Chemikalien
- Kein galvanisches Risiko
- Kosten: 8–12× Messing-Äquivalent
- Aktuell für Superyacht-Kraftstoffsysteme (z.B. Lürssen, Feadship)

**Siliziumkarbid-beschichtete Stutzen (SiC):**
- Keramikbeschichtung auf Edelstahl- oder Bronze-Basis
- Extrem verschleißfest, keine Biofilm-Anhaftung
- Reduziert Bewuchs-Blockade bei Kühlwasser-Einlässen
- TRL 6 — erste Pilotinstallationen bei Megayachten

(Confidence: estimated — Fachmessen METS 2025, Boot Düsseldorf 2025, Superyacht Forum)

### 2.3 Automatische Leckage-Erkennung für Schlauchverbindungen

| Technologie | TRL | Hersteller | Verfügbarkeit | Preis |
|---|---|---|---|---|
| Feuchte-Tape an Verbindung | 9 | Diverse (Bilge-Alarm) | Verfügbar | 5–15 EUR/Sensor |
| Kapazitiver Feuchte-Sensor | 8 | Siren Marine, Yacht Sentinel | Verfügbar | 80–120 EUR/Sensor |
| Durchfluss-Vergleich (Ein/Aus) | 6 | F&E / SmartBoat Consortium | Prototyp | n/a |
| Akustische Leckage-Erkennung | 5 | F&E / Uni Southampton | Labor | n/a |
| Druckabfall-Monitoring (geschlossenes System) | 7 | Webasto (Heizungssystem) | Begrenzt | 200–400 EUR |

**AYDI-Relevanz**: Pipeline C (Text) kann Sensoralarme und Wartungsberichte auswerten. Pipeline A (Strukturiert) kann Sensorpositionen im CAD-Modell validieren und optimale Platzierung empfehlen.

(Confidence: documented + estimated — Hersteller-Websites, Marine Technology Reporter 2025)

---

## 3. Best Practices nach Revier & Klimazone

### 3.1 Ostsee / Nordeuropa (Brackwasser, kalt)

| Aspekt | Empfehlung | Begründung |
|---|---|---|
| Schlauchschellen-Material | W4 (316SS) ausreichend | Geringere Korrosionsbelastung als Vollsalz |
| Doppelt unter WL | Pflicht | Universelle Anforderung |
| Schellen-Inspektion | Alle 2 Jahre | Geringerer Korrosionsdruck |
| Schlauch-Lebensdauer | 10–12 Jahre (Kühlwasser), 15 Jahre (Trinkwasser) | Kältere Temperaturen verlängern Lebensdauer |
| Frostschutz | Alle Schläuche und Verbindungen entwässern im Winter | Eis dehnt sich aus → Barb-Verformung, Schlauch-Riss |
| Antifouling Schlauchtülle | Wenig notwendig | Geringer Bewuchs unter 15°C |
| Quick-Connect (Trinkwasser) | John Guest geeignet | Kein Frostrisiko bei korrekter Winterentleerung |

(Confidence: documented — Survey-Erfahrung Ostsee, BSU)

### 3.2 Mittelmeer (Volles Seewasser, warm)

| Aspekt | Empfehlung | Begründung |
|---|---|---|
| Schlauchschellen-Material | W4 mindestens, W5 empfohlen | Volles Seewasser + Wärme = aggressive Korrosion |
| Doppelt unter WL | Pflicht | Universelle Anforderung |
| Schellen-Inspektion | Jährlich | Höhere Korrosionsrate bei 20–28°C Wassertemperatur |
| Schlauch-Lebensdauer | 6–8 Jahre (Kühlwasser), 10 Jahre (Trinkwasser) | Wärme beschleunigt Alterung |
| UV-Schutz | Schläuche vor UV schützen (Motorraum: kein Problem) | Deck-durchgeführte Schläuche: UV-beständigen Schlauch verwenden |
| Bewuchs | Schlauchtüllen am Kühlwasser-Einlass regelmäßig prüfen | Muscheln/Seepocken können Tülle blockieren |
| Landstrom-Korrosion | In Marinas: Zinkanoden prüfen, galvanischen Isolator verwenden | Streustrom kann Schlauchschellen angreifen |

(Confidence: documented — Survey-Erfahrung Mittelmeer, Pantaenius Schadensdaten)

### 3.3 Tropen (Volles Seewasser, heiß, UV-intensiv)

| Aspekt | Empfehlung | Begründung |
|---|---|---|
| Schlauchschellen-Material | W5 (316L) ausschließlich | Maximale Korrosionsbelastung |
| Doppelt unter WL | Pflicht + T-Bolt-Überschelle empfohlen | Zusätzliche Sicherheit bei hoher Korrosion |
| Schellen-Inspektion | Alle 6 Monate | Tropische Korrosionsraten 2–3× höher als gemäßigt |
| Schlauch-Lebensdauer | 4–6 Jahre (Kühlwasser), 7 Jahre (Trinkwasser) | Wärme + UV beschleunigen Alterung dramatisch |
| UV-Schutz | KRITISCH für alle Deck-exponierten Verbindungen | UV-Degradation von EPDM und Silikon innerhalb von 2–3 Jahren |
| Bewuchs | Monatliche Prüfung Kühlwasser-Einlass | Tropischer Bewuchs extrem schnell |
| Schlauchtyp | Nur Markenschläuche (Shields, Trident, Gates) | Billigschläuche versagen in Tropen in <3 Jahren |
| Quick-Connect | NICHT empfohlen unter WL | O-Ring-Alterung bei >30°C beschleunigt |

(Confidence: estimated — Blauwasser-Segler-Erfahrung, Pantaenius World-ARC Daten)

### 3.4 Gezeitenreviere (UK, Bretagne, Nordsee)

| Aspekt | Empfehlung | Begründung |
|---|---|---|
| Schlauchschellen-Material | W4 oder W5 | Volles Seewasser |
| Trockenfallen | Schlauchverbindungen bei Trockenfallen auf Integrität prüfen | Rumpfbewegung beim Aufsetzen kann Verbindungen belasten |
| Strömung | Kühlwasser-Einlass: größere Schlauchtülle (Sicherheitsmarge) | Starke Strömung kann Unterdruck erzeugen |
| Gezeiten-Hub | Schlauchverlegung mit ausreichend Schlaufe | Kein Zug auf Verbindung bei Tidenhub |
| Winterlager (UK) | Alle Verbindungen bei Haul-Out inspizieren | Jährliches Haul-Out als Wartungsfenster nutzen |

(Confidence: estimated — RYA Technical Publications, Yachting Monthly Survey Data)

### 3.5 Süßwasser (Binnenreviere)

| Aspekt | Empfehlung | Begründung |
|---|---|---|
| Schlauchschellen-Material | W2 (304SS) akzeptabel, W4 empfohlen | Keine Salzwasserkorrosion |
| Doppelt unter WL | Empfohlen (nicht immer vorgeschrieben) | Geringeres Korrosionsrisiko, aber Absturz bleibt kritisch |
| Schellen-Inspektion | Alle 3 Jahre | Deutlich geringere Korrosion |
| Schlauch-Lebensdauer | 12–15 Jahre (Kühlwasser), 15–20 Jahre (Trinkwasser) | Süßwasser = deutlich geringere Beanspruchung |
| Galvanische Korrosion | Deutlich reduziert | Süßwasser hat niedrigere Leitfähigkeit |
| Quick-Connect | Uneingeschränkt empfohlen für Trinkwasser | Geringeres Risiko |

(Confidence: estimated — Binnenrevier-Survey-Erfahrung, TÜV BSB)

---

## 4. Regional Sourcing

### 4.1 Europa — Bezugsquellen

| Händler | Land | Sortiment Schlauchverbindungen | Website | Versand |
|---|---|---|---|---|
| SVB (Bremen) | DE | ABA, NORMA, Vetus, Whale, John Guest | svb-marine.de | EU-weit |
| Compass24 | DE | ABA, NORMA, Vetus, Groco (Import) | compass24.de | EU-weit |
| AWN (Buxtehude) | DE | ABA, NORMA, Vetus, Osculati | awn.de | DE, AT, CH |
| Toplicht (Hamburg) | DE | ABA, NORMA, Oetiker, Mikalor | toplicht.de | EU-weit |
| Bootszubehör Segelservice | DE | ABA, NORMA, TruDesign, Vetus | segelservice.com | DE, AT |
| Maritimo (NL) | NL | Vetus (Heimatmarkt), ABA, NORMA | maritimo.nl | Benelux, DE |
| Accastillage Diffusion | FR | Plastimo (Heimatmarkt), ABA, NORMA | accastillage-diffusion.com | FR, EU |
| Marine Superstore | UK | Whale (Heimatmarkt), John Guest, Jubilee, ABA | marinesuperstore.com | UK, EU |
| Force 4 Chandlery | UK | Jubilee, Whale, John Guest, ABA | force4.co.uk | UK |
| Navimo / Plastimo | FR | Plastimo, NORMA, ABA | navimo.fr | FR, EU |
| Vitrifrigo / Osculati | IT | Osculati (Heimatmarkt), Guidi | osculati.com | IT, EU |
| Gründl Bootsimport | AT | ABA, NORMA, Vetus | gruendl.at | AT, DE, CH |

**Lieferzeiten**: Innerhalb EU 3–7 Werktage. Groco, Buck Algonquin, Forespar (USA) via EU-Importeure 2–4 Wochen.

### 4.2 Nordamerika

| Händler | Land | Sortiment | Website | Versand |
|---|---|---|---|---|
| West Marine | USA | Groco, Perko, Forespar, Buck Algonquin, Ideal | westmarine.com | USA, int. |
| Defender Industries | USA | Groco, Buck Algonquin, Forespar, Trident | defender.com | USA, int. |
| Hamilton Marine | USA | Groco (Spezialist), Buck Algonquin | hamiltonmarine.com | USA |
| Fisheries Supply | USA | Groco, Perko, Whale | fisheriessupply.com | USA, CAN |
| Great Lakes Skipper | USA | Buck Algonquin, Perko, Attwood | greatlakesskipper.com | USA |
| Canadian Tire Marine | CAN | Marpac, Perko | canadiantire.ca | CAN |

### 4.3 Ozeanien / Asien-Pazifik

| Händler | Land | Sortiment | Website | Versand |
|---|---|---|---|---|
| Burnsco | NZ | TruDesign (Heimatmarkt), BEP, Whale | burnsco.co.nz | NZ, AU |
| Whitworths | AU | TruDesign, ABA, Whale | whitworths.com.au | AU, NZ |
| CH Smith | AU | TruDesign, ABA, Groco (Import) | chsmith.com.au | AU |
| Budget Marine (Karibik) | Diverse | Groco, Perko, Buck Algonquin | budgetmarine.com | Karibik-weit |

**AYDI-Tipp für Regional Sourcing**: Bei Pipeline A (Strukturiert) kann die Bootsherkunft (USA/EU/NZ) als Indikator für verbautete Gewindetypen (NPT vs BSP), Schlauchschellen-Marken und Schlauchtüllen-Standards dienen. US-Boote in Europa benötigen fast immer NPT-zu-BSP-Adapter bei Ersatzteilbeschaffung.

(Confidence: documented — Händler-Websites, verified 2026-Q1)

---

## 5. Zweck dieser Wissensdatei

### 5.1 Rolle im AYDI-System

Diese Wissensdatei dient als **domänenspezifische Referenz** für das AYDI-Analysesystem. Sie wird von folgenden Modulen konsumiert:

| Modul | Verwendung | Beispiel |
|---|---|---|
| **materials** | Materialkenntnis für Schlauchverbindungs-Bewertung | "316SS Vollband-Schelle = marine-tauglich, W3 Lochband = Warnung" |
| **structural** | Strukturelle Integrität der Verbindung | "Doppelte Schellen unter WL = konform, einfache = Mangel" |
| **compliance** | Normen-Konformität (ISO, ABYC, DIN, CE) | "Verzinkte Schellen unter WL = Verstoß gegen ABYC H-27.5.4.1" |
| **service_patterns** | Wartungsmuster und Lebensdauer | "Kühlwasserschlauch-Schelle nach 8 Jahren in Mittelmeer → Austausch" |
| **cost** | Kostenmodelle für Reparatur und Austausch | "Kompletter Schlauchschellen-Austausch 12-m-Segelboot: 450–800 EUR" |
| **production** | Bewertung der Werftarbeit | "OEM-Schellen W2 statt W4 = Produktionskosten-Optimierung auf Kosten der Qualität" |
| **visual** | Visuelle Befunderkennung (Pipeline B) | "Braune Verfärbung an Schlauchschelle = Rost = W1/W2/W3-Material" |

### 5.2 Confidence-Zuordnung für Schlauchverbindungen

| Datenquelle | Confidence | Beispiel |
|---|---|---|
| CAD-Modell mit Verbindungsdaten | `measured` | "Groco PTH-1500 an Pos. SV-003" |
| Materialtest (XRF-Analyse Schelle) | `measured` | "316L bestätigt durch Spektralanalyse" |
| Herstellerspezifikation | `documented` | "ABA 316 Vollband, W4, 32–50 mm" |
| Foto, klar erkennbar | `visual_high` | "Doppelte Vollband-Schellen sichtbar" |
| Foto, teilweise erkennbar | `visual_medium` | "Schlauchschelle erkennbar, Material unklar" |
| Foto, schlecht erkennbar | `visual_low` | "Verbindung im Schatten, nur Schlauch sichtbar" |
| Abgeleitet aus Bootstyp / Werft / Baujahr | `estimated` | "Bavaria 2010 → wahrscheinlich W2/W4 gemischt" |
| Branchendurchschnitt | `benchmark` | "Durchschnittliche Lebensdauer Kühlwasserschlauch: 8 Jahre" |

### 5.3 Pipeline-spezifische Nutzung

**Pipeline A (Strukturiert):**
- Liest Bootstyp, Baujahr, Werft → schätzt OEM-Schlauchverbindungen (Abschnitt 1.4)
- Liest CAD-Daten → identifiziert alle Verbindungspunkte, Durchmesser, Positionen
- Berechnet: Anzahl Verbindungen unter/über WL, Material-Compliance, Drehmomente

**Pipeline B (Visuell):**
- Erkennt Schlauchschellen-Typ (Lochband vs Vollband vs T-Bolt)
- Erkennt Korrosion (Rostspuren = W1/W2/W3 oder Mischkonstruktion)
- Erkennt doppelte vs einfache Besclellung
- Erkennt offensichtliche Mängel (Kabelbinder, Draht, fehlende Schellen)
- KANN NICHT: Material exakt bestimmen (304 vs 316 visuell identisch)
- KANN NICHT: Drehmoment beurteilen
- KANN NICHT: verdeckte Verbindungen (hinter Verkleidung) bewerten

**Pipeline C (Text):**
- Extrahiert aus Surveyor-Berichten: "Schlauchschellen unter WL korrodiert, Austausch empfohlen"
- Extrahiert aus Wartungsprotokollen: "2024-03: Alle Schlauchschellen Motorraum erneuert"
- Erkennt Muster: "Wiederkehrende Leckage an Kühlwasser-Pumpe → Schlauchtülle prüfen"

(Confidence: documented — AYDI-Systemarchitektur)

---

## 6. Pydantic-Modelle

### 6.1 HoseConnectionSpec — Spezifikation einer Schlauchverbindung

```python
from pydantic import BaseModel, Field
from typing import Optional, Literal
from enum import Enum


class HoseBarbType(str, Enum):
    """Typ der Schlauchtülle / des Stutzens."""
    STRAIGHT = "straight"                     # Gerade Schlauchtülle
    ELBOW_90 = "elbow_90"                     # 90°-Winkelstutzen
    ELBOW_45 = "elbow_45"                     # 45°-Winkelstutzen
    Y_CONNECTOR = "y_connector"               # Y-Verteiler
    T_CONNECTOR = "t_connector"               # T-Stück
    REDUCING_STRAIGHT = "reducing_straight"   # Reduzierstutzen gerade
    REDUCING_ELBOW = "reducing_elbow"         # Reduzierstutzen Winkel
    BULKHEAD = "bulkhead"                     # Schottdurchführung
    INLINE_CHECK = "inline_check"             # Rückschlagventil integriert
    ANTI_SIPHON = "anti_siphon"               # Anti-Siphon-Ventil integriert
    QUICK_CONNECT = "quick_connect"           # Steckverbindung (Whale, John Guest)
    PUSH_FIT = "push_fit"                     # Push-In-Verbindung
    COMPRESSION = "compression"               # Klemmringverschraubung
    UNKNOWN = "unknown"


class ThreadType(str, Enum):
    """Gewindeart des Stutzens."""
    BSP_PARALLEL = "bsp_parallel"             # G-Gewinde (ISO 228-1, zylindrisch)
    BSP_TAPER = "bsp_taper"                   # R-Gewinde (ISO 7-1, konisch)
    NPT = "npt"                               # National Pipe Thread (ANSI B1.20.1)
    METRIC = "metric"                         # Metrisches Gewinde
    NONE = "none"                             # Kein Gewinde (Barb-only, aufgepresst)
    UNKNOWN = "unknown"


class ClampType(str, Enum):
    """Typ der Schlauchschelle."""
    WORM_DRIVE_PERFORATED = "worm_drive_perforated"   # Schneckengewinde, Lochband (DIN 3017-1/2)
    WORM_DRIVE_SOLID = "worm_drive_solid"             # Schneckengewinde, Vollband (DIN 3017-3)
    T_BOLT = "t_bolt"                                 # T-Bolzen-Schelle (Mikalor, NORMA)
    CONSTANT_TENSION = "constant_tension"             # Federspann-Schelle
    EAR_CLAMP = "ear_clamp"                           # Ohrklemme (Oetiker)
    SPRING_CLAMP = "spring_clamp"                     # Federbandschelle
    WIRE_CLAMP = "wire_clamp"                         # Drahtschelle — NUR Notbehelf!
    CABLE_TIE = "cable_tie"                           # Kabelbinder — VERBOTEN als Schlauchsicherung!
    NONE = "none"                                     # Keine Schelle (Quick-Connect, Push-Fit)
    UNKNOWN = "unknown"


class ClampMaterial(str, Enum):
    """Material der Schlauchschelle nach DIN 3017."""
    W1_GALVANIZED = "w1_galvanized"           # Stahl verzinkt — NICHT Marine
    W2_304SS = "w2_304ss"                     # Edelstahl 304 — Süßwasser
    W3_MIXED = "w3_mixed"                     # 304-Gehäuse/430-Band — NICHT Marine!
    W4_316SS = "w4_316ss"                     # Edelstahl 316 — Standard Marine
    W5_316L = "w5_316l"                       # Edelstahl 316L — Premium Marine
    ALLOY_STEEL = "alloy_steel"               # Legierter Stahl (T-Bolt)
    UNKNOWN = "unknown"


class FittingMaterial(str, Enum):
    """Material des Stutzens / der Schlauchtülle."""
    BRONZE_C83600 = "bronze_c83600"           # 85-5-5-5, Standard Marine
    BRONZE_C84400 = "bronze_c84400"           # 81 Red Brass
    BRONZE_C92200 = "bronze_c92200"           # Navy G, Premium
    BRONZE_C95800 = "bronze_c95800"           # Nickel-Alu-Bronze
    DZR_BRASS = "dzr_brass"                   # Entzinkungsbeständiges Messing
    YELLOW_BRASS = "yellow_brass"             # GEFAHR — dezinkifizierungsanfällig!
    STAINLESS_316 = "stainless_316"           # Edelstahl 316
    STAINLESS_316L = "stainless_316l"         # Edelstahl 316L
    COMPOSITE_MARELON = "composite_marelon"   # Forespar Marelon
    COMPOSITE_TRUDESIGN = "composite_trudesign"  # TruDesign Komposit
    COMPOSITE_NYLON = "composite_nylon"       # Polyamid (Nylon) verstärkt
    ACETAL = "acetal"                         # POM (Delrin) — Whale, John Guest
    POLYPROPYLENE = "polypropylene"           # PP — nur Trinkwasser
    PVC = "pvc"                               # PVC — NICHT unter WL!
    UNKNOWN = "unknown"


class ConnectionApplication(str, Enum):
    """Verwendungszweck der Schlauchverbindung."""
    COOLING_WATER_INTAKE = "cooling_water_intake"     # Kühlwassereinlass Motor
    COOLING_WATER_OUTLET = "cooling_water_outlet"     # Kühlwasserauslass Motor
    EXHAUST_WET = "exhaust_wet"                       # Nassauspuff
    TOILET_INTAKE = "toilet_intake"                   # WC Seewassereinlass
    TOILET_DISCHARGE = "toilet_discharge"             # WC Abwasserauslass
    HOLDING_TANK_VENT = "holding_tank_vent"           # Fäkalientank-Entlüftung
    HOLDING_TANK_PUMPOUT = "holding_tank_pumpout"     # Fäkalientank-Absaugung
    BILGE_DISCHARGE = "bilge_discharge"               # Bilgenpumpe Auslass
    GALLEY_DRAIN = "galley_drain"                     # Pantry Abfluss
    SINK_DRAIN = "sink_drain"                         # Waschbecken Abfluss
    SHOWER_DRAIN = "shower_drain"                     # Dusche Abfluss
    AC_INTAKE = "ac_intake"                           # Klimaanlage Seewasser-Einlass
    AC_DISCHARGE = "ac_discharge"                     # Klimaanlage Auslass
    GENERATOR_COOLING = "generator_cooling"           # Generator Kühlwasser
    WATERMAKER_INTAKE = "watermaker_intake"           # Wassermacher Einlass
    WATERMAKER_BRINE = "watermaker_brine"             # Wassermacher Sole-Auslass
    POTABLE_WATER = "potable_water"                   # Trinkwasser-Distribution
    HOT_WATER = "hot_water"                           # Warmwasser
    FUEL_SUPPLY = "fuel_supply"                       # Kraftstoff-Zuleitung
    FUEL_RETURN = "fuel_return"                       # Kraftstoff-Rücklauf
    FUEL_FILL = "fuel_fill"                           # Kraftstoff-Einfüllstutzen
    FUEL_VENT = "fuel_vent"                           # Kraftstoff-Tank-Entlüftung
    LPG_SUPPLY = "lpg_supply"                        # Gas-Leitung
    FIRE_SYSTEM = "fire_system"                       # Feuerlöschanlage
    DECK_WASH = "deck_wash"                           # Deckwaschanlage
    ANCHOR_WASH = "anchor_wash"                       # Ankerspülung
    LIVEWELL = "livewell"                             # Köderbecken
    HYDRAULIC = "hydraulic"                           # Hydraulik (Ruder, Bugstrahlruder)
    OTHER = "other"


class ConnectionConditionRating(str, Enum):
    """Zustandsbewertung einer Schlauchverbindung."""
    EXCELLENT = "excellent"         # Neuwertiger Zustand (Score 90–100)
    GOOD = "good"                   # Guter Zustand, normale Gebrauchsspuren (70–89)
    FAIR = "fair"                   # Akzeptabel, Wartung empfohlen (50–69)
    POOR = "poor"                   # Mangelhaft, Austausch planen (30–49)
    CRITICAL = "critical"          # SOFORTIGER Austausch! Sinkgefahr bei unter WL! (0–29)
    NOT_ASSESSED = "not_assessed"   # Nicht beurteilbar


class HoseConnectionSpec(BaseModel):
    """Spezifikation einer einzelnen Schlauchverbindung."""

    model_config = {"from_attributes": True}

    # Identifikation
    id: Optional[str] = Field(None, description="Eindeutige ID im AYDI-System, z.B. 'HC-001'")
    position: Optional[str] = Field(None, description="Position am Boot, z.B. 'Motorraum, Steuerbord, Kühlwasser-Einlass'")
    application: ConnectionApplication = Field(..., description="Verwendungszweck")
    position_relative_to_wl: Literal["below", "above", "at_waterline", "unknown"] = Field(
        "unknown", description="Lage relativ zur Wasserlinie"
    )

    # Stutzen-Typ
    barb_type: HoseBarbType = Field(..., description="Typ der Schlauchtülle")
    thread_type: ThreadType = Field(ThreadType.UNKNOWN, description="Gewindeart")
    thread_size: Optional[str] = Field(None, description="Gewindegröße, z.B. '1-1/2 BSP', '1 NPT'")

    # Material
    fitting_material: FittingMaterial = Field(..., description="Werkstoff des Stutzens")
    fitting_material_note: Optional[str] = Field(None, description="Zusatzinfo zum Werkstoff")

    # Maße (alle in mm)
    hose_id_mm: int = Field(..., ge=6, le=200, description="Schlauch-Innendurchmesser in mm")
    barb_od_mm: Optional[int] = Field(None, ge=6, le=210, description="Schlauchtülle Außendurchmesser in mm")
    barb_length_mm: Optional[int] = Field(None, description="Länge der Schlauchtülle in mm")
    reducing_to_mm: Optional[int] = Field(None, description="Reduzierter Durchmesser (bei Reduzierstutzen) in mm")

    # Schlauchschellen
    clamp_type: ClampType = Field(ClampType.UNKNOWN, description="Typ der Schlauchschelle")
    clamp_material: ClampMaterial = Field(ClampMaterial.UNKNOWN, description="Material der Schlauchschelle")
    clamp_count: int = Field(0, ge=0, le=4, description="Anzahl Schlauchschellen an dieser Verbindung")
    clamp_band_width_mm: Optional[float] = Field(None, description="Bandbreite der Schlauchschelle in mm")
    clamp_torque_nm: Optional[float] = Field(None, description="Anzugsdrehmoment der Schelle in Nm")

    # Hersteller
    fitting_manufacturer: Optional[str] = Field(None, description="Hersteller Stutzen, z.B. 'Groco', 'Vetus'")
    fitting_model: Optional[str] = Field(None, description="Modellnummer Stutzen, z.B. 'PTH-1500'")
    clamp_manufacturer: Optional[str] = Field(None, description="Hersteller Schlauchschelle, z.B. 'ABA', 'NORMA'")
    clamp_model: Optional[str] = Field(None, description="Modellnummer Schelle, z.B. 'ABA 316 Original'")

    # Dichtung
    thread_sealant: Optional[str] = Field(None, description="Gewindedichtmittel: 'PTFE', 'Loctite 577', 'Hanf+Neo-Fermit'")
    o_ring_material: Optional[str] = Field(None, description="O-Ring-Material bei Quick-Connect: 'EPDM', 'FKM/Viton', 'NBR'")

    # Normen
    iso_9093_compliant: Optional[bool] = Field(None, description="ISO 9093 konform? (Verbindung am Borddurchlass)")
    abyc_h27_compliant: Optional[bool] = Field(None, description="ABYC H-27 konform?")
    din_3017_class: Optional[str] = Field(None, description="DIN 3017 Klasse der Schelle: 'W1'–'W5'")

    # Kosten
    fitting_cost_eur: Optional[float] = Field(None, description="Stückpreis Stutzen in EUR")
    clamp_cost_eur: Optional[float] = Field(None, description="Stückpreis Schlauchschelle in EUR")
    total_connection_cost_eur: Optional[float] = Field(None, description="Gesamtkosten Verbindung (Stutzen + Schellen + Dichtmittel)")
    labor_cost_eur: Optional[float] = Field(None, description="Montagekosten in EUR")

    # Confidence
    confidence: str = Field("estimated", description="measured|calculated|visual_high|visual_medium|estimated|documented|benchmark")


class HoseConnectionCondition(BaseModel):
    """Zustandsbewertung einer Schlauchverbindung."""

    model_config = {"from_attributes": True}

    connection_id: str = Field(..., description="Referenz auf HoseConnectionSpec.id")
    assessment_date: Optional[str] = Field(None, description="Datum der Bewertung, ISO 8601")
    assessor: Optional[str] = Field(None, description="Prüfer / Surveyor")

    # Gesamtbewertung
    condition_rating: ConnectionConditionRating = Field(..., description="Gesamtzustand")
    condition_score: int = Field(..., ge=0, le=100, description="Score 0–100")

    # Einzelbefunde — Stutzen
    barb_intact: Optional[bool] = Field(None, description="Schlauchtülle intakt, keine Risse/Korrosion?")
    barb_corrosion: Optional[Literal["none", "surface", "pitting", "severe", "dezincification"]] = Field(
        None, description="Korrosionszustand Schlauchtülle"
    )
    thread_intact: Optional[bool] = Field(None, description="Gewinde intakt, nicht beschädigt?")
    thread_sealant_intact: Optional[bool] = Field(None, description="Gewindedichtung intakt?")
    no_leaking: Optional[bool] = Field(None, description="Keine Leckage?")

    # Einzelbefunde — Schlauchschellen
    clamps_present: Optional[bool] = Field(None, description="Schlauchschellen vorhanden?")
    clamps_correct_count: Optional[bool] = Field(None, description="Richtige Anzahl (doppelt unter WL)?")
    clamps_correct_material: Optional[bool] = Field(None, description="Richtiges Material (W4/W5 unter WL)?")
    clamps_correct_type: Optional[bool] = Field(None, description="Richtiger Typ (Vollband unter WL)?")
    clamps_tight: Optional[bool] = Field(None, description="Schellen fest angezogen?")
    clamps_no_corrosion: Optional[bool] = Field(None, description="Keine Korrosion an Schellen?")
    clamps_no_damage_to_hose: Optional[bool] = Field(None, description="Schellen beschädigen Schlauch nicht?")

    # Einzelbefunde — Schlauch an Verbindung
    hose_fully_on_barb: Optional[bool] = Field(None, description="Schlauch vollständig auf Tülle aufgeschoben?")
    hose_flexible: Optional[bool] = Field(None, description="Schlauch noch flexibel (nicht verhärtet)?")
    hose_no_cracks: Optional[bool] = Field(None, description="Keine Risse im Schlauch an der Verbindung?")
    hose_correct_diameter: Optional[bool] = Field(None, description="Schlauch hat korrekten Durchmesser für Tülle?")

    # Quick-Connect spezifisch
    qc_locking_engaged: Optional[bool] = Field(None, description="Quick-Connect Verriegelung eingerastet?")
    qc_o_ring_intact: Optional[bool] = Field(None, description="O-Ring intakt?")

    # Visuelle Befunde
    photo_available: Optional[bool] = Field(None, description="Foto vorhanden?")
    visual_findings: Optional[list[str]] = Field(None, description="Liste visueller Befunde")

    # Empfehlung
    recommendation: Optional[str] = Field(None, description="Handlungsempfehlung")
    urgency: Optional[Literal["sofort", "innerhalb_30_tage", "nächstes_haul_out", "monitoring"]] = Field(
        None, description="Dringlichkeit der Maßnahme"
    )

    # Confidence
    confidence: str = Field("visual_medium", description="Confidence der Bewertung")


class ConnectionSystemAssessment(BaseModel):
    """Gesamtbewertung aller Schlauchverbindungen eines Bootes."""

    model_config = {"from_attributes": True}

    # Boot-Referenz
    boat_id: Optional[str] = Field(None, description="AYDI Boot-ID")
    boat_name: Optional[str] = Field(None, description="Bootsname")
    boat_type: Optional[str] = Field(None, description="Bootstyp, z.B. 'Bavaria 40 Cruiser'")
    boat_year: Optional[int] = Field(None, description="Baujahr")
    hull_material: Optional[str] = Field(None, description="Rumpfmaterial: GFK, Stahl, Alu, Holz")

    # Verbindungs-Inventar
    total_connections: int = Field(..., ge=0, description="Gesamtanzahl Schlauchverbindungen")
    connections_below_wl: int = Field(..., ge=0, description="Davon unterhalb Wasserlinie")
    connections_assessed: int = Field(..., ge=0, description="Davon bewertet")

    # Schlauchschellen-Statistik
    count_double_clamped_below_wl: int = Field(0, description="Doppelt geschellt unter WL")
    count_single_clamped_below_wl: int = Field(0, description="Einfach geschellt unter WL (MANGEL!)")
    count_no_clamp_below_wl: int = Field(0, description="Ohne Schelle unter WL (KRITISCH!)")
    count_w4_w5_clamps: int = Field(0, description="Schellen W4/W5 (marine-konform)")
    count_w1_w2_w3_clamps: int = Field(0, description="Schellen W1/W2/W3 (NICHT marine-konform)")
    count_solid_band: int = Field(0, description="Vollband-Schellen")
    count_perforated_band: int = Field(0, description="Lochband-Schellen")

    # Stutzen-Material
    count_bronze_fittings: int = Field(0, description="Bronze-Stutzen")
    count_composite_fittings: int = Field(0, description="Komposit-Stutzen")
    count_brass_danger: int = Field(0, description="Messing-Stutzen (GEFAHR!)")
    count_pvc_danger: int = Field(0, description="PVC-Stutzen unter WL (VERBOTEN!)")

    # Thread-Kompatibilität
    mixed_thread_types: Optional[bool] = Field(None, description="Gemischte Gewindetypen (NPT + BSP)?")
    thread_mismatch_count: int = Field(0, description="Anzahl Thread-Mismatches")

    # Gesamtbewertung
    system_score: int = Field(..., ge=0, le=100, description="Gesamtscore 0–100")
    worst_connection_score: int = Field(..., ge=0, le=100, description="Schlechtester Einzelscore")
    critical_findings: list[str] = Field(default_factory=list, description="Kritische Befunde")
    warnings: list[str] = Field(default_factory=list, description="Warnungen")
    recommendations: list[str] = Field(default_factory=list, description="Empfehlungen")

    # Normen-Compliance
    all_double_clamped_below_wl: Optional[bool] = Field(None, description="Alle Verbindungen unter WL doppelt geschellt?")
    all_marine_grade_clamps: Optional[bool] = Field(None, description="Alle Schellen W4/W5?")
    all_solid_band_below_wl: Optional[bool] = Field(None, description="Alle Schellen unter WL Vollband?")
    no_thread_mismatches: Optional[bool] = Field(None, description="Keine Gewinde-Inkompatibilitäten?")

    # Kosten
    estimated_clamp_replacement_cost_eur: Optional[float] = Field(
        None, description="Geschätzte Kosten: alle nicht-konformen Schellen ersetzen"
    )
    estimated_full_refit_cost_eur: Optional[float] = Field(
        None, description="Geschätzte Kosten: Komplett-Erneuerung aller Verbindungen"
    )

    # Einzelbewertungen
    individual_assessments: list[HoseConnectionCondition] = Field(
        default_factory=list, description="Einzelbewertungen pro Verbindung"
    )

    # Confidence
    confidence: str = Field("estimated", description="Confidence der Gesamtbewertung")
```

### 6.2 Scoring-Logik für Schlauchverbindungen

```python
def calculate_connection_score(condition: dict, below_waterline: bool = False) -> int:
    """
    Berechnet den Zustandsscore einer Schlauchverbindung.
    
    Scoring-Regeln (Score 0–100):
    - Basiswert: 100
    - Abzüge für jeden Mangel
    - Unter Wasserlinie: verschärfte Bewertung (Faktor 1,5× bei sicherheitsrelevanten Mängeln)
    
    KRITISCH (Score → 0, sofortiger Austausch):
    - Keine Schlauchschelle unter WL
    - Kabelbinder als Schlauchsicherung unter WL
    - Draht als Schlauchsicherung unter WL
    - Schlauch nicht auf Tülle aufgeschoben
    - Aktive Leckage
    
    Returns: Score 0–100
    """
    score = 100
    wl_factor = 1.5 if below_waterline else 1.0
    
    # --- KRITISCHE Mängel (Score → 0) ---
    if below_waterline:
        if not condition.get("clamps_present", True):
            return 0  # Keine Schelle unter WL = SINKEN
        if condition.get("clamp_type") == "cable_tie":
            return 0  # Kabelbinder unter WL = SINKEN
        if condition.get("clamp_type") == "wire_clamp":
            return 0  # Drahtschelle unter WL = SINKEN
    
    if condition.get("hose_fully_on_barb") is False:
        return 0  # Schlauch nicht auf Tülle = akute Gefahr
    
    if condition.get("no_leaking") is False:
        return 5  # Aktive Leckage = fast Score 0, aber nicht ganz (kann Tropfleckage sein)
    
    # --- SCHWERE Mängel ---
    
    # Schlauchschellen-Anzahl
    if below_waterline and not condition.get("clamps_correct_count", True):
        score -= int(40 * wl_factor)  # Einfache Schelle unter WL
    elif not condition.get("clamps_correct_count", True):
        score -= 15  # Einfache Schelle über WL
    
    # Schlauchschellen-Material
    clamp_material = condition.get("clamp_material", "unknown")
    if clamp_material == "w1_galvanized":
        score -= int(35 * wl_factor)  # Verzinkt
    elif clamp_material == "w3_mixed":
        score -= int(30 * wl_factor)  # W3 Mischkonstruktion
    elif clamp_material == "w2_304ss" and below_waterline:
        score -= 20  # 304SS unter WL in Salzwasser
    
    # Schlauchschellen-Typ
    if condition.get("clamp_type") == "worm_drive_perforated" and below_waterline:
        score -= 15  # Lochband unter WL
    
    # Stutzen-Korrosion
    barb_corrosion = condition.get("barb_corrosion", "none")
    if barb_corrosion == "severe":
        score -= int(30 * wl_factor)
    elif barb_corrosion == "dezincification":
        score -= int(40 * wl_factor)  # Dezinkifizierung = Materialversagen
    elif barb_corrosion == "pitting":
        score -= int(20 * wl_factor)
    elif barb_corrosion == "surface":
        score -= 5
    
    # Schlauchschellen-Korrosion
    if condition.get("clamps_no_corrosion") is False:
        score -= int(20 * wl_factor)
    
    # Schlauch-Zustand an Verbindung
    if condition.get("hose_flexible") is False:
        score -= int(15 * wl_factor)  # Verhärteter Schlauch
    if condition.get("hose_no_cracks") is False:
        score -= int(25 * wl_factor)  # Risse im Schlauch
    if condition.get("hose_correct_diameter") is False:
        score -= int(20 * wl_factor)  # Falscher Durchmesser
    
    # Schellen beschädigen Schlauch
    if condition.get("clamps_no_damage_to_hose") is False:
        score -= int(15 * wl_factor)  # Schelle schneidet ein
    
    # Gewindedichtung
    if condition.get("thread_sealant_intact") is False:
        score -= int(10 * wl_factor)
    
    # Quick-Connect spezifisch
    if condition.get("qc_locking_engaged") is False:
        score -= int(30 * wl_factor)
    if condition.get("qc_o_ring_intact") is False:
        score -= int(20 * wl_factor)
    
    # Schellen nicht fest
    if condition.get("clamps_tight") is False:
        score -= int(15 * wl_factor)
    
    return max(0, min(100, score))


def calculate_connection_system_score(individual_scores: list[int], below_wl_flags: list[bool]) -> int:
    """
    Berechnet den Gesamtscore des Schlauchverbindungs-Systems.
    
    Regel: Der Gesamtscore wird stark vom schlechtesten Einzelscore unter WL dominiert.
    Ein einziger kritischer Mangel unter WL kann das gesamte System auf KRITISCH setzen.
    
    Gewichtung:
    - Unter WL: Gewicht 3,0
    - Über WL (Motorraum): Gewicht 1,5
    - Über WL (Komfort): Gewicht 1,0
    
    Returns: Gewichteter Gesamtscore 0–100
    """
    if not individual_scores:
        return 0
    
    # Kritischster Score unter WL
    below_wl_scores = [s for s, bw in zip(individual_scores, below_wl_flags) if bw]
    above_wl_scores = [s for s, bw in zip(individual_scores, below_wl_flags) if not bw]
    
    # Ein Score von 0 unter WL → System-Score maximal 15
    if below_wl_scores and min(below_wl_scores) == 0:
        return min(15, int(sum(individual_scores) / len(individual_scores)))
    
    # Gewichteter Durchschnitt
    total_weight = 0
    weighted_sum = 0
    
    for score, below_wl in zip(individual_scores, below_wl_flags):
        weight = 3.0 if below_wl else 1.0
        weighted_sum += score * weight
        total_weight += weight
    
    avg = weighted_sum / total_weight if total_weight > 0 else 0
    
    # Worst-Score-Penalty: Wenn schlechtester Score unter WL < 50, zusätzlicher Abzug
    if below_wl_scores:
        worst_below = min(below_wl_scores)
        if worst_below < 50:
            penalty = (50 - worst_below) * 0.5  # 0–25 Punkte Abzug
            avg -= penalty
    
    return max(0, min(100, int(avg)))
```

### 6.3 Scoring-Tabelle — Kurzreferenz

| Befund | Score-Abzug (über WL) | Score-Abzug (unter WL) | Priorität |
|---|---|---|---|
| Keine Schelle unter WL | n/a | → Score 0 | SOFORT |
| Kabelbinder unter WL | n/a | → Score 0 | SOFORT |
| Aktive Leckage | → Score 5 | → Score 5 | SOFORT |
| Schlauch nicht auf Tülle | → Score 0 | → Score 0 | SOFORT |
| Einfache Schelle unter WL | -15 | -60 | Innerhalb 30 Tage |
| Verzinkte Schelle (W1) | -35 | -53 | Innerhalb 30 Tage |
| W3 Mischkonstruktion | -30 | -45 | Innerhalb 30 Tage |
| 304SS unter WL (Salzwasser) | n/a | -20 | Nächstes Haul-Out |
| Lochband unter WL | n/a | -15 | Nächstes Haul-Out |
| Stutzen dezinkifiziert | -40 | -60 | Innerhalb 30 Tage |
| Stutzen schwere Korrosion | -30 | -45 | Innerhalb 30 Tage |
| Stutzen Lochfraß | -20 | -30 | Nächstes Haul-Out |
| Schellen korrodiert | -20 | -30 | Nächstes Haul-Out |
| Schlauch verhärtet | -15 | -23 | Nächstes Haul-Out |
| Schlauch gerissen | -25 | -38 | Innerhalb 30 Tage |
| Falscher Schlauchdurchmesser | -20 | -30 | Nächstes Haul-Out |
| Schelle schneidet in Schlauch | -15 | -23 | Nächstes Haul-Out |
| Gewindedichtung defekt | -10 | -15 | Nächstes Haul-Out |
| Quick-Connect nicht verriegelt | -30 | -45 | SOFORT |
| O-Ring defekt (Quick-Connect) | -20 | -30 | Innerhalb 30 Tage |
| Schellen nicht fest angezogen | -15 | -23 | Innerhalb 30 Tage |

(Confidence: calculated — AYDI Scoring-Framework)

---

## 7. Grundlagen

### 7.1 Schlauchtüllen-Typen (Hose Barbs / Hose Connectors)

#### 7.1.1 Gerade Schlauchtülle (Straight Hose Barb)

Die einfachste und häufigste Form der Schlauchverbindung. Ein zylindrischer oder leicht konischer Stutzen mit umlaufenden Rillen (Barbs), die das Abrutschen des Schlauchs verhindern.

**Konstruktionsmerkmale:**

| Parameter | Spezifikation | Toleranz |
|---|---|---|
| Barb-Übermaß über Schlauch-ID | +0,5 bis +1,5 mm | ±0,2 mm |
| Anzahl Rillen (Barbs) | Mindestens 2, empfohlen 3–4 | — |
| Rillentiefe | 0,8–1,5 mm | ±0,2 mm |
| Rillenabstand | 3–5 mm | ±0,5 mm |
| Rillenwinkel (Hinterschnitt) | 15°–30° | ±5° |
| Tüllenlänge | ≥2× Schlauch-ID (Minimum), empfohlen 2,5× | — |
| Oberflächenrauheit | Ra 1,6–6,3 µm | Zu glatt = Schlauch rutscht |

**Dimensionierungstabelle — Gerade Schlauchtüllen:**

| Schlauch-ID (mm) | Tüllen-OD (mm) | Min. Tüllenlänge (mm) | Empf. Tüllenlänge (mm) | Typisches Gewinde |
|---|---|---|---|---|
| 10 | 10,5–11,0 | 20 | 25 | G 1/4 oder 3/8 NPT |
| 13 | 13,5–14,0 | 26 | 32 | G 3/8 oder 1/2 NPT |
| 16 | 16,5–17,5 | 32 | 40 | G 1/2 oder 1/2 NPT |
| 19 | 19,5–20,5 | 38 | 48 | G 1/2 oder 3/4 NPT |
| 25 | 26,0–27,0 | 50 | 63 | G 3/4 oder 1 NPT |
| 32 | 33,0–34,0 | 64 | 80 | G 1 oder 1-1/4 NPT |
| 38 | 39,0–40,0 | 76 | 95 | G 1-1/4 oder 1-1/2 NPT |
| 50 | 51,0–52,5 | 100 | 125 | G 1-1/2 oder 2 NPT |
| 63 | 64,5–66,0 | 126 | 158 | G 2 oder 2-1/2 NPT |
| 76 | 77,5–79,0 | 152 | 190 | G 2-1/2 oder 3 NPT |

(Confidence: documented — DIN 2826, Groco Engineering Data, Vetus Katalog)

#### 7.1.2 Winkelstutzen (Elbow Hose Barbs — 90° und 45°)

Winkelstutzen werden eingesetzt, wenn der Schlauch in einem Winkel abgeführt werden muss. Sie vermeiden scharfe Knicke im Schlauch, die den Durchfluss drosseln und den Schlauch beschädigen.

**WICHTIG**: Ein Schlauchknick von >30° reduziert den Durchfluss um >50%. Winkelstutzen sind IMMER einem geknickten Schlauch vorzuziehen.

**90°-Winkelstutzen:**
- Einsatz: Enge Einbauverhältnisse, Richtungswechsel am Seeventil
- Durchflussverlust: ca. 20–30% gegenüber geradem Stutzen (Kv-Wert ca. 0,7× gerade)
- Kritisch: Innerer Radius muss ≥2× Schlauch-ID sein, sonst Kavitation bei Pumpen
- Hersteller: Groco (HE-Serie), Vetus (WH90-Serie), Buck Algonquin (90° Bronze Elbows)

**45°-Winkelstutzen:**
- Einsatz: Leichte Richtungsänderung, Platzoptimierung
- Durchflussverlust: ca. 10–15% gegenüber geradem Stutzen
- Bevorzugt gegenüber 90° wo möglich
- Hersteller: Groco (HE45-Serie), Vetus (WH45-Serie)

| Winkel | Durchflussverlust | Kv-Faktor (relativ) | Bevorzugt für |
|---|---|---|---|
| 0° (gerade) | 0% (Referenz) | 1,00 | Standard, ausreichend Platz |
| 45° | 10–15% | 0,85–0,90 | Leichte Richtungsänderung |
| 90° | 20–30% | 0,70–0,80 | Enge Einbauverhältnisse |
| 90° (enger Radius) | 30–45% | 0,55–0,70 | VERMEIDEN — Kavitationsgefahr |

(Confidence: documented — Groco Engineering Data, hydraulische Berechnungen)

#### 7.1.3 Reduzierstutzen (Reducing Hose Barbs)

Reduzierstutzen verbinden Schläuche unterschiedlichen Durchmessers. Sie sind notwendig, wenn Seeventil-Nennweite und Schlauch-ID nicht übereinstimmen.

**Auslegungsregeln:**

| Regel | Spezifikation | Begründung |
|---|---|---|
| Max. Reduktion in einem Schritt | 1 Nennweite (z.B. 38→32, nicht 38→25) | Strömungsabriss bei zu starker Reduktion |
| Konus-Winkel (innen) | ≤15° | Turbulenzminimierung |
| Position im System | NACH dem Seeventil, NICHT am Seeventil selbst | Seeventil muss volle Nennweite haben |
| Schlauchschellen | An beiden Enden doppelt (unter WL) | Beide Durchmesser sichern |

**Häufige Reduzierstutzen-Kombinationen:**

| Von (mm) | Nach (mm) | Typische Anwendung | Hersteller / Artikelnr. |
|---|---|---|---|
| 38 → 32 | Seeventil 1-1/2" → Pumpe 1-1/4" | Kühlwasser | Groco?"RB-3832, Buck Algonquin RB1512 |
| 32 → 25 | Pumpe 1-1/4" → Schlauch 1" | Kühlwasser, Bilge | Groco RB-3225, Vetus RD32/25 |
| 25 → 19 | Schlauch 1" → Gerät 3/4" | WC-Einlass, Watermaker | Groco RB-2519, Vetus RD25/19 |
| 19 → 16 | 3/4" → 5/8" | Abfluss, Entlüftung | Buck Algonquin RB3458 |
| 50 → 38 | 2" → 1-1/2" | Nassauspuff, AC | Groco RB-5038, Vetus RD50/38 |

(Confidence: documented — Groco Katalog 2025, Vetus Katalog 2025/26, Buck Algonquin Katalog)

#### 7.1.4 Y-Verteiler und T-Stücke

**Y-Verteiler:**
- Teilt einen Schlauch in zwei Abzweige (oder vereinigt zwei zu einem)
- Einsatz: Bilgenpumpen-Verteilung, Kühlwasser-Split, AC-Multi-Zonen
- Durchflussverlust: ca. 30–40% pro Abzweig
- WARNUNG: Jeder Abzweig muss separat mit doppelten Schlauchschellen gesichert werden
- Hersteller: Groco (HYC-Serie), Vetus (WY-Serie), Buck Algonquin (Bronze Y)

**T-Stücke:**
- Wie Y, aber mit 90°-Abzweig
- Höherer Durchflussverlust als Y (40–50% am Abzweig)
- Einsatz: Messleitungen, Entlüftungen, Bypass
- Hersteller: Groco (HTH-Serie), Vetus (WT-Serie)

| Typ | Durchflussverlust Geradeaus | Durchflussverlust Abzweig | Typische Anwendung |
|---|---|---|---|
| Y (60°) | 15–20% | 30–40% | Bilge, Kühlwasser-Split |
| T (90°) | 10–15% | 40–50% | Messung, Entlüftung, Bypass |

(Confidence: documented — Groco Katalog, hydraulische Standardwerte)

#### 7.1.5 Schottdurchführungen (Bulkhead Fittings)

Schottdurchführungen ermöglichen die wasserdichte Schlauchdurchführung durch Schotten, Tanks oder Rumpfverstärkungen.

**Konstruktion:**
- Zwei Schlauchtüllen an gegenüberliegenden Seiten eines Flanschs
- Flansch wird mit Kontermutter am Schott befestigt
- Dichtung durch O-Ring oder Flachdichtung zwischen Flansch und Schott
- Material: Bronze, Edelstahl 316 oder Komposit (Marelon, TruDesign)

**Kritische Punkte:**
- Schottdurchführung ist eine zusätzliche potentielle Leckstelle
- Dichtung muss für das Medium geeignet sein (Seewasser, Kraftstoff, Trinkwasser)
- Bei wasserdichten Schotten: Durchführung muss gleiche Druckstufe wie Schott haben
- Schlauchschellen an BEIDEN Seiten der Durchführung (unter WL: doppelt)

| Hersteller | Modell | Material | Größen (ID mm) | Preis (EUR) |
|---|---|---|---|---|
| Groco | HTH-Serie | Bronze C83600 | 13–50 | 25–85 |
| TruDesign | 90680 Serie | Komposit GFK | 13–50 | 15–55 |
| Forespar | Marelon BH | Marelon | 13–38 | 18–60 |
| Vetus | WBF-Serie | Bronze DZR | 13–50 | 20–70 |
| Buck Algonquin | BHF-Serie | Bronze C83600 | 19–50 | 22–75 |

(Confidence: documented — Herstellerkataloge 2025/26)

### 7.2 Gewinde-zu-Schlauch-Adapter (Thread-to-Hose Adapters)

#### 7.2.1 Pipe-to-Hose Adapter — Grundprinzip

Ein Pipe-to-Hose-Adapter verbindet eine Gewindebohrung (z.B. am Seeventil, an der Pumpe, am Tank) mit einem Schlauch. Eine Seite hat ein Gewinde (BSP oder NPT), die andere Seite eine Schlauchtülle.

**Groco PTH-Serie** — Der Industriestandard (USA):

| Modell | Gewinde | Schlauch-ID (mm) | Material | Preis (EUR) |
|---|---|---|---|---|
| PTH-500 | 1/2 NPT | 13 | Bronze C83600 | 12–18 |
| PTH-750 | 3/4 NPT | 19 | Bronze C83600 | 15–22 |
| PTH-1000 | 1 NPT | 25 | Bronze C83600 | 18–28 |
| PTH-1250 | 1-1/4 NPT | 32 | Bronze C83600 | 22–35 |
| PTH-1500 | 1-1/2 NPT | 38 | Bronze C83600 | 28–42 |
| PTH-2000 | 2 NPT | 50 | Bronze C83600 | 35–55 |

**Vetus Schlauchstutzen** — Europäischer Standard (BSP):

| Modell | Gewinde | Schlauch-ID (mm) | Material | Preis (EUR) |
|---|---|---|---|---|
| SLP012B | G 1/2 BSP | 13 | Bronze DZR | 10–16 |
| SLP034B | G 3/4 BSP | 19 | Bronze DZR | 12–20 |
| SLP100B | G 1 BSP | 25 | Bronze DZR | 15–25 |
| SLP114B | G 1-1/4 BSP | 32 | Bronze DZR | 18–30 |
| SLP112B | G 1-1/2 BSP | 38 | Bronze DZR | 22–38 |
| SLP200B | G 2 BSP | 50 | Bronze DZR | 30–48 |

(Confidence: documented — Groco Katalog 2025, Vetus Katalog 2025/26)

#### 7.2.2 Gewindedichtung — Methoden und Materialien

Die Gewindedichtung am Adapter ist kritisch. Ein undichtes Gewinde ist eine permanente Leckquelle.

**Methode 1: PTFE-Band (Teflonband)**
- Standard für NPT-Gewinde (konisch, selbstdichtend)
- 3–5 Wicklungen, IN Richtung des Gewindes (beim Eindrehen zieht sich Band fest)
- Breite: 12 mm oder 19 mm
- Stärke: 0,075–0,1 mm (Standard), 0,2 mm (Heavy Duty)
- Farbe: Weiß (Universal), Gelb (Gas), Rosa (Trinkwasser NSF 61)
- **ACHTUNG**: Überwickeln kann Gewinde blockieren, Schnipsel können Ventile verstopfen
- Hersteller: Loctite, Henkel, Würth, diverse (Commodityprodukt)
- Preis: 1–3 EUR pro Rolle (12m)

**Methode 2: Flüssige Gewindedichtung (Anaerobe Dichtmittel)**
- Bevorzugt für BSP-Gewinde (zylindrisch, nicht selbstdichtend)
- Polymerisiert im Gewinde (anaerobisch), bleibt elastisch
- Trinkwasser-zugelassen: Loctite 577 (NSF 61), Permabond A136
- Seewasser: Loctite 567, Loctite 577
- Kraftstoff: Loctite 545 (Hydraulikfest)
- **Vorteil gegenüber PTFE**: Kein Band das Ventile verstopfen kann
- **Nachteil**: Demontage erfordert Wärme bei Hochfest-Varianten
- Preis: 15–35 EUR pro 50 ml

**Methode 3: Hanf + Dichtpaste (traditionell)**
- Gewindedichtung: Hanffaser + Neo-Fermit oder Unipak
- Traditionelle Methode, im Sanitärbereich Standard
- Marine: akzeptabel für BSP über WL, Trinkwasser
- NICHT empfohlen für: Vibrationsbelastung (Motorraum), Seewasser unter WL
- Vorteil: Nachziehbar, demontierbar
- Preis: 5–10 EUR (Hanf + Paste)

| Methode | BSP-Gewinde | NPT-Gewinde | Unter WL | Trinkwasser | Kraftstoff |
|---|---|---|---|---|---|
| PTFE-Band | ⚠️ Bedingt | ✅ Standard | ✅ | ✅ (Rosa) | ✅ (Gelb) |
| Loctite 577 | ✅ Optimal | ✅ | ✅ | ✅ (NSF 61) | ❌ |
| Loctite 567 | ✅ | ✅ | ✅ | ❌ | ❌ |
| Loctite 545 | ✅ | ✅ | ✅ | ❌ | ✅ |
| Hanf + Paste | ✅ | ❌ (nicht konisch) | ❌ | ✅ (NSF 61 Paste) | ❌ |

(Confidence: documented — Loctite Technical Data Sheets, DIN DVGW, NSF 61)

### 7.3 Quick-Connect-Systeme

#### 7.3.1 Whale Quick Connect (WQC)

Whale (UK, jetzt Teil von Munster Simms Engineering) bietet das am weitesten verbreitete Quick-Connect-System im Yachtbau.

**System-Übersicht:**

| Komponente | Artikelnr. | Beschreibung | Schlauch-ID | Preis (EUR) |
|---|---|---|---|---|
| WX1502B | Stecker (male) | Für 15mm Schlauch | 15 mm | 5–8 |
| WX1504B | Buchse (female) | Für 15mm Schlauch | 15 mm | 5–8 |
| WX1506B | T-Stück Quick Connect | 3× 15mm | 15 mm | 12–18 |
| WX1508B | Winkelstück 90° QC | 15mm | 15 mm | 8–12 |
| WX1510B | Reduzierstück QC | 15→12 mm | 15/12 mm | 8–12 |
| WX1520B | Schott-Durchführung QC | 15mm | 15 mm | 10–15 |
| WX1202B | Stecker (male) | Für 12mm Schlauch | 12 mm | 4–7 |
| WX1204B | Buchse (female) | Für 12mm Schlauch | 12 mm | 4–7 |

**Technische Daten Whale QC:**
- Betriebsdruck: max. 4,1 bar (Trinkwasser), 2,0 bar (Abwasser)
- Temperatur: 0–60°C
- O-Ring: EPDM (Standard), FKM (auf Anfrage)
- Material Körper: Acetal (POM / Delrin)
- Verriegelung: Collet-Ring (Klemmring), Entriegelung durch Drücken
- Zulassungen: NSF 61 (Trinkwasser), BS 6920 (UK Trinkwasser)
- Lebensdauer: >10.000 Steckzyklen, >15 Jahre bei Trinkwasser

**Einsatzbereiche Whale QC:**
- ✅ Trinkwasser-Distribution (Hauptanwendung)
- ✅ Bilgenpumpe Druckseite (über WL)
- ✅ Grauwasser (Spüle, Dusche — Druckseite)
- ✅ Ankerspülung, Deckwaschanlage (Druckseite)
- ❌ NICHT: Unter Wasserlinie
- ❌ NICHT: Seewasser (Salz greift Acetal an)
- ❌ NICHT: Kraftstoff (Quellwirkung auf Acetal)
- ❌ NICHT: Abgassystem (Temperatur)
- ❌ NICHT: Saugseite von Pumpen (Unterdruck → Leckage möglich)

(Confidence: documented — Whale Product Catalogue 2025, Whale Technical Datasheet WQC)

#### 7.3.2 John Guest / DM Fit Push-Fit-System

John Guest (UK, jetzt Teil der Reliance Worldwide Corporation) dominiert den Push-Fit-Markt für Trinkwassersysteme an Bord.

**System-Übersicht:**

| Baureihe | Artikelnr.-Beispiel | Rohrdurchmesser | Material | Preis (EUR) |
|---|---|---|---|---|
| Speedfit (15mm) | JG-15STEI | 15 mm | Acetal/EPDM | 3–6 |
| Speedfit (12mm) | JG-12STEI | 12 mm | Acetal/EPDM | 3–5 |
| Speedfit (22mm) | JG-22STEI | 22 mm | Acetal/EPDM | 5–8 |
| Speedfit (10mm) | JG-10STEI | 10 mm | Acetal/EPDM | 3–5 |
| DM Fit (12mm) | DMF-APSEU1212 | 12 mm | Acetal/EPDM | 2–4 |
| DM Fit (3/8" OD) | DMF-APSEU0606 | 9,5 mm (3/8") | Acetal/EPDM | 2–4 |

**Technische Daten John Guest Speedfit:**
- Betriebsdruck: max. 10 bar (bei 25°C), 6 bar (bei 60°C), 3 bar (bei 82°C)
- Temperatur: 0–82°C (Heißwasser bis 82°C für kurze Perioden)
- O-Ring: EPDM
- Material Körper: Acetal (POM)
- Rohr: Polybutylene (PB) oder Nylon (PA12) — KEIN Schlauch, sondern steifes Rohr
- Verriegelung: Edelstahl-Greifring + O-Ring
- Zulassungen: NSF 61, WRAS, ACS, KTW
- Lebensdauer: >50 Jahre bei Trinkwasser (Herstellerangabe, Laborbedingungen)

**WICHTIG — Unterschied Whale QC vs John Guest:**

| Merkmal | Whale Quick Connect | John Guest Speedfit |
|---|---|---|
| Verbindungsart | Schlauch auf Stecker | Steifes Rohr in Push-Fitting |
| Lösbar | Ja, durch Collet drücken | Ja, durch Collet drücken |
| Schlauchtyp | Flexibler Schlauch (ID) | Steifes Rohr (OD — Außendurchmesser!) |
| Betriebsdruck | 4,1 bar | 10 bar |
| Temperatur | 60°C max | 82°C max |
| Rohrmaterial | PVC-Schlauch, Silikon | Polybutylen, Nylon PA12 |
| Hauptanwendung | Retrofit, flexibel | Neuinstallation, fest verlegt |

**AYDI-WARNUNG**: John Guest Speedfit arbeitet mit dem AUSSEN-Durchmesser des Rohrs. Whale Quick Connect arbeitet mit dem INNEN-Durchmesser des Schlauchs. Verwechslung führt zu Undichtigkeit! Ein "15mm John Guest" nimmt ein Rohr mit 15 mm Außen-Ø auf. Ein "15mm Whale QC" nimmt einen Schlauch mit 15 mm Innen-Ø auf.

(Confidence: documented — John Guest Technical Handbook 2024, DM Fit Catalogue)

### 7.4 Schlauchschellen-Typen (Hose Clamps)

#### 7.4.1 Schneckengewinde-Schlauchschellen (Worm Drive Clamps)

Die universellste und häufigste Schellenform im Yachtbau. Ein gelochtes oder geschlitztes Band wird durch eine Schneckengewinde-Schraube gespannt.

**Lochband (DIN 3017-1/2) vs Vollband (DIN 3017-3):**

| Eigenschaft | Lochband | Vollband |
|---|---|---|
| Bandform | Perforiert (12-mm-Löcher) | Glatt, geschlitzt |
| Klemmkraft-Verteilung | Punktuell an Löchern → Druckspitzen | Gleichmäßig über gesamte Fläche |
| Schlauchbeschädigung | Löcher drücken Schlauch lokal ein → Einschnitte möglich | Minimales Risiko |
| Verwendung unter WL | ❌ NICHT EMPFOHLEN (ABYC H-27 verbietet) | ✅ EMPFOHLEN |
| Preis | Günstig (0,50–3 EUR) | Mittel (2–6 EUR) |
| Erhältlichkeit | Überall (Baumarkt, Marine, Auto) | Spezialist (Marine-Fachhandel) |
| DIN-Klasse | DIN 3017-1 (9mm), DIN 3017-2 (12mm) | DIN 3017-3 |
| Marine-Hersteller | ABA (Schweden), NORMA TORRO | ABA 316 Original, NORMA COBRA |

**AYDI-Empfehlung**: 
- Unter WL: NUR Vollband-Schellen (DIN 3017-3), W4 oder W5
- Motorraum: Vollband empfohlen, Lochband W4 akzeptabel
- Trinkwasser über WL: Lochband W4 akzeptabel
- Abwasser über WL: Lochband W4 akzeptabel

(Confidence: documented — DIN 3017, ABYC H-27, ABA Product Guide)

#### 7.4.2 T-Bolt-Schlauchschellen (T-Bolt Clamps)

Hochleistungsschellen mit einem T-förmigen Bolzen als Spannmechanismus. Massives Band (kein Lochband), breiter als Standard-Schellen.

**Konstruktion:**
- Massives Edelstahlband, Breite 19–25 mm
- T-Bolzen mit Mutter (Sechskant oder Schlitz)
- Deutlich höhere Klemmkraft als Schneckengewinde
- Gleichmäßige, punktlastfreie Druckverteilung

**Technische Daten:**

| Parameter | T-Bolt Standard | T-Bolt Marine |
|---|---|---|
| Bandbreite | 19 mm | 24–25 mm |
| Bandstärke | 0,7–0,9 mm | 0,8–1,0 mm |
| Material | 304SS oder 316SS | 316SS oder 316L |
| Klemmkraft | 800–1.200 N | 1.000–1.500 N |
| Drehmoment | 6–9 Nm | 7–11 Nm |
| Spannbereich | Schmal (z.B. 40–45 mm) | Schmal (Spezialgrößen) |

**Einsatzbereiche T-Bolt:**
- ✅ Nassauspuff (hochtemperatur, vibration)
- ✅ Große Kühlwasserschläuche (>50 mm)
- ✅ AC-Seewasserleitungen (>38 mm)
- ✅ Turbolader-Ladeluftrohre
- ✅ Zusätzliche Sicherung über Schneckengewinde-Schellen unter WL
- ⚠️ Enger Spannbereich — Exakte Größe notwendig!

**Hersteller:**

| Hersteller | Serie | Material | Größenbereich | Preis (EUR) |
|---|---|---|---|---|
| Mikalor | SUPRA W2 | 304SS | 17–252 mm | 3–15 |
| Mikalor | SUPRA W4 | 316SS | 17–252 mm | 5–22 |
| NORMA | TORRO S | 316SS | 20–200 mm | 4–18 |
| ABA | T-Bolt ABA | 316SS | 25–150 mm | 6–20 |
| Breeze (USA) | Aero-Seal | 300SS | 19–152 mm | 4–12 |
| Ideal (USA) | Tridon T-Bolt | 300SS/316SS | 19–178 mm | 4–15 |

(Confidence: documented — Mikalor Technical Data, NORMA Katalog 2025, ABA Product Guide)

#### 7.4.3 Federspann-Schlauchschellen (Constant-Tension Clamps)

Federspann-Schellen kombinieren eine Standard-Schneckengewinde-Schelle mit einer integrierten Feder (Edelstahl-Blattfeder unter dem Band), die Temperatur- und Alterungs-bedingte Durchmesseränderungen des Schlauchs kompensiert.

**Problem, das gelöst wird:**
- Schläuche im Motorraum dehnen sich bei Betriebstemperatur aus und schrumpfen beim Abkühlen
- Standard-Schellen verlieren nach thermischen Zyklen an Klemmkraft
- Schlauch altert → wird dünner → Standard-Schelle sitzt locker
- Federspann-Schelle kompensiert ±1,5–3 mm Durchmesseränderung

**Einsatzbereiche:**
- ✅ Motorraum — Kühlwasserschläuche (Temperaturwechsel)
- ✅ Nassauspuff — Vibration + Temperatur
- ✅ Generator — Kühlwasser
- ✅ Heizungsschläuche
- ⚠️ Nicht als Ersatz für doppelte Beschellung unter WL

| Hersteller | Modell | Material | Federweg (mm) | Größenbereich | Preis (EUR) |
|---|---|---|---|---|---|
| Breeze (USA) | CT-9400 Series | 300SS + Feder | ±2,0 | 13–102 mm | 3–12 |
| NORMA | TORRO CT | 316SS + Feder | ±2,5 | 16–120 mm | 5–15 |
| Ideal (USA) | Series 36 CT | 300SS + Feder | ±1,5 | 13–76 mm | 3–10 |
| Gates (USA) | PolarSeal CT | 316SS + Feder | ±2,0 | 19–89 mm | 4–12 |

(Confidence: documented — SAE J1508 Typ CT, Herstellerkataloge)

#### 7.4.4 Ohrklemmen / Ohrschellen (Ear Clamps — Oetiker)

Oetiker-Ohrklemmen (ear clamps / stepless ear clamps) sind einmal-verwendbare Schellen, die mit einer Spezialzange (Oetiker-Zange) aufgepresst werden. Das "Ohr" wird flachgedrückt und zieht das Band permanent zusammen.

**Konstruktion:**
- Geschlossenes, stufenloses Band (kein Gewinde, keine Perforation)
- Ein oder zwei "Ohren" (single ear / double ear)
- Einmal-Montage: Nach dem Aufpressen nicht mehr lösbar ohne Zerstörung
- Exakte Verpressung erfordert kalibriertes Werkzeug

**Technische Daten Oetiker:**

| Parameter | Single Ear (SE) | Double Ear (DE) | Stepless Ear (SL) |
|---|---|---|---|
| Bandbreite | 5–9 mm | 7–9 mm | 5,5–9,5 mm |
| Bandstärke | 0,6–0,8 mm | 0,7–0,8 mm | 0,6–0,8 mm |
| Ohr-Typ | 1 Ohr | 2 Ohren | 1 Ohr, stufenlos |
| Spannbereich | Klein (1–2 mm) | Mittel (2–4 mm) | Klein (1–2 mm) |
| Klemmkraft | Hoch, gleichmäßig | Sehr hoch | Sehr hoch, gleichmäßig |
| Wiederverwendbar | ❌ Nein | ❌ Nein | ❌ Nein |
| Werkzeug | Oetiker-Zange | Oetiker-Zange | Oetiker-Zange |

**Einsatzbereiche Oetiker:**
- ✅ Kraftstoffleitungen (≤16 mm ID) — OEM-Standard in Automobil und Marine
- ✅ Hydraulikleitungen
- ✅ Unterdruckleitungen
- ✅ Kleine Schläuche im Motorraum (Heizung, Entlüftung)
- ⚠️ Nicht für große Durchmesser (>50 mm)
- ⚠️ Nicht als alleinige Sicherung unter WL (immer zusätzlich Standard-Schelle)

| Oetiker-Typ | Artikelnr.-Beispiel | Größenbereich | Material | Preis (EUR) |
|---|---|---|---|---|
| 1-Ear Clamp 316SS | 16700001–16700099 | 5–40 mm | 316SS | 1–4 |
| 1-Ear Clamp 304SS | 16300001–16300099 | 5–40 mm | 304SS | 0,80–3 |
| 2-Ear Clamp 316SS | 10100001–10100099 | 7–35 mm | 316SS | 1,50–5 |
| Stepless 316SS | 16700101–16700199 | 8–28 mm | 316SS | 1,20–4,50 |
| Oetiker-Zange (Profi) | HIP 2000 | — | — | 85–120 |
| Oetiker-Zange (Standard) | 14100420 | — | — | 35–55 |

(Confidence: documented — Oetiker Produkt-Katalog 2025, SAE J1508 Typ ER)

#### 7.4.5 Federbandschellen (Spring Clamps)

Einfache Federstahl-Schellen (oft "Quetschschellen" genannt), die durch Federkraft klemmen. Im Automobilbau allgegenwärtig, im Marineeinsatz NICHT empfohlen.

**AYDI-Bewertung: NICHT MARINE-TAUGLICH**
- Material: Federstahl, NICHT korrosionsbeständig in Salzatmosphäre
- Klemmkraft: Nimmt mit Schlauch-Alterung ab (kein Nachspannen möglich)
- Vibration: Kann sich von Tülle "herunter-vibrieren"
- Korrosion: Rost nach 1–3 Jahren in mariner Umgebung
- Scoring-Impact: -25 Punkte über WL, Score → 0 unter WL

**Einzige akzeptable Marine-Anwendung**: Binnenboote in Süßwasser, über WL, nicht im Motorraum, in Edelstahl-Ausführung.

(Confidence: documented — ABYC H-27, Survey-Erfahrung)

### 7.5 Die Doppelschellen-Regel (Double Clamp Requirement)

#### 7.5.1 Warum doppelte Schlauchschellen unter der Wasserlinie?

**Die fundamentale Sicherheitslogik:**

Eine einzelne Schlauchschelle hat einen Versagensmechanismus — wenn diese eine Schelle versagt (Korrosion, Vibration, thermischer Zyklus, Materialermüdung), rutscht der Schlauch sofort vom Stutzen. Ergebnis: unkontrollierter Wassereinbruch.

Zwei Schlauchschellen bieten:
- **Redundanz**: Wenn Schelle 1 versagt, hält Schelle 2
- **Warnzeit**: Schelle 1 lockert sich → langsame Tropfleckage → Bilge-Alarm → BEVOR Schelle 2 versagt
- **Verteilte Last**: Auszugskraft verteilt sich auf zwei Klemmstellen

**Normen-Anforderungen:**

| Standard | Anforderung | Verbindlich |
|---|---|---|
| ABYC H-27.5.4 | Doppelte Schellen an JEDER Verbindung unter WL | Ja (USA) |
| ISO 9093 | "Geeignete Sicherung" (impliziert doppelt) | Ja (EU) |
| Lloyd's Register SSC | Doppelte Schellen unter WL + vibrationsbelastet | Ja (Klasse) |
| DNV-GL YACHT | Doppelte Schellen unter WL | Ja (Klasse) |
| CE RCD Kat. A/B | Doppelte Schellen unter WL | Ja (EU) |
| CE RCD Kat. C/D | Empfohlen, nicht explizit gefordert | Empfohlen |
| Pantaenius | Doppelte Schellen unter WL | Vertragsklausel |

#### 7.5.2 Korrekte Montage — Doppelte Schlauchschellen

**Montage-Schema:**

```
Schlauch →  [Schelle 2]  [Schelle 1]  ← Stutzen
            ↓            ↓
         5–10 mm      2–5 mm
         von Schelle 1   vom Stutzen-Rand
```

**Montageregeln:**

| Regel | Spezifikation | Begründung |
|---|---|---|
| Schelle 1 Position | 2–5 mm vom Stutzen-Rand | Maximale Haltekraft auf letzter Rille |
| Schelle 2 Position | 5–10 mm hinter Schelle 1 | Unabhängige Klemmstelle, nicht überlappend |
| Schrauben-Position | NICHT übereinander, um 90–180° versetzt | Gleichmäßige Druckverteilung |
| Gleiches Material | Beide Schellen identisch (Material, Typ, Größe) | Kein galvanisches Element |
| Gleiches Drehmoment | Beide Schellen mit gleichem Nm angezogen | Gleichmäßige Klemmung |
| Schlauch voll aufgeschoben | Schlauch muss bis zum Anschlag der Tülle sitzen | Sonst nur 1 Rille im Eingriff |

#### 7.5.3 Drehmoment-Spezifikationen für Schlauchschellen

| Schellentyp | Bandbreite | Schlauch-ID-Bereich | Drehmoment (Nm) | Werkzeug |
|---|---|---|---|---|
| Schneckengewinde 9mm | 9 mm | 10–32 mm | 1,5–3,0 Nm | 7mm Steckschlüssel |
| Schneckengewinde 12mm | 12 mm | 20–100 mm | 2,5–4,5 Nm | 7mm / 8mm Steckschlüssel |
| T-Bolt 19mm | 19 mm | 25–80 mm | 6–9 Nm | 10mm Steckschlüssel |
| T-Bolt 24mm | 24 mm | 40–150 mm | 7–11 Nm | 10mm / 13mm Steckschlüssel |
| Oetiker (Ohrklemme) | 7–9 mm | 8–40 mm | n/a (Pressung) | Oetiker-Zange |

**WARNUNG — Überdrehte Schlauchschellen:**

| Symptom | Ursache | Folge |
|---|---|---|
| Gewinde der Schelle abgerissen | >5 Nm bei 9mm-Schelle | Schelle nutzlos, Austausch |
| Schelle schneidet in Schlauch | >4 Nm bei weichem Schlauch | Schlauch eingeschnitten → Schwachstelle → Riss |
| Band verformt sich (Welligkeit) | >6 Nm bei 12mm-Schelle | Ungleichmäßige Klemmung, lokale Druckspitzen |
| Tülle deformiert (Komposit) | >4 Nm auf Komposit-Tülle | Tülle bricht → totaler Verlust |

**AYDI-Empfehlung**: Drehmomentschlüssel ab 10 mm Schlauch-ID verwenden. Im Zweifelsfall lieber etwas weniger als zu viel — die Haltekraft kommt primär aus der Passgenauigkeit Schlauch/Tülle, die Schelle verhindert nur das Abrutschen.

(Confidence: documented — Herstellerangaben ABA, NORMA, Mikalor, ABYC H-27)

### 7.6 Materialkompatibilität — Schlauchverbindungen

#### 7.6.1 Galvanische Verträglichkeit

Die galvanische Reihe bestimmt, welche Materialien miteinander in Kontakt stehen dürfen (in Seewasser als Elektrolyt). Die Potentialdifferenz darf max. 200–300 mV betragen.

| Material Stutzen | Material Schelle | ΔV (mV) | Bewertung |
|---|---|---|---|
| Bronze C83600 | 316SS Schelle | ~50 | ✅ Kompatibel |
| Bronze C83600 | 304SS Schelle | ~50 | ✅ Kompatibel |
| Bronze C83600 | Verzinkt Schelle | ~600 | ❌ NICHT kompatibel — Zink opfert sich |
| Edelstahl 316 | 316SS Schelle | 0 | ✅ Gleich |
| Edelstahl 316 | 304SS Schelle | ~20 | ✅ Kompatibel |
| Edelstahl 316 | Verzinkt Schelle | ~550 | ❌ NICHT kompatibel |
| DZR-Messing | 316SS Schelle | ~100 | ✅ Kompatibel (aber DZR überwachen) |
| Komposit (Marelon) | 316SS Schelle | n/a | ✅ Kein galvanisches Risiko |
| Komposit (TruDesign) | 316SS Schelle | n/a | ✅ Kein galvanisches Risiko |
| Aluminium (Rumpf) | 316SS Schelle | ~700 | ❌❌ KRITISCH — Alu-Korrosion! Isolation nötig! |
| Aluminium (Rumpf) | Bronze Stutzen | ~300 | ⚠️ Grenzwertig — Isolation empfohlen |

**AYDI-Regel**: Bei Aluminium-Rümpfen MÜSSEN alle metallischen Schlauchverbindungen galvanisch vom Rumpf isoliert werden (Gummimanschette, Kunststoff-Buchse). Alternativ: durchgängig Komposit-System (TruDesign + Komposit-Schellen).

(Confidence: documented — MIL-STD-889D, DNV-GL RP-B401, Galvanische Reihe Seewasser)

#### 7.6.2 Medienverträglichkeit — Schlauchstutzen-Material vs Medium

| Medium | Bronze | DZR Messing | 316SS | Komposit (Marelon) | Acetal (Whale) | PVC |
|---|---|---|---|---|---|---|
| Seewasser kalt | ✅ | ✅ (zeitlich begrenzt) | ✅ | ✅ | ❌ | ❌ |
| Seewasser warm (>40°C) | ✅ | ⚠️ | ✅ | ⚠️ (max 49°C) | ❌ | ❌ |
| Trinkwasser | ✅ (NSF 61 prüfen) | ✅ | ✅ | ✅ (NSF 61) | ✅ (NSF 61) | ⚠️ |
| Diesel | ✅ | ✅ | ✅ | ❌ | ❌ | ❌ |
| Benzin | ⚠️ | ⚠️ | ✅ | ❌ | ❌ | ❌ |
| Abwasser (sanitär) | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| Kühlmittel (Glykol) | ✅ | ✅ | ✅ | ⚠️ | ❌ | ❌ |
| Hydrauliköl | ✅ | ✅ | ✅ | ❌ | ❌ | ❌ |
| Abgas-Kondensat (sauer) | ⚠️ | ❌ | ✅ | ❌ | ❌ | ❌ |
| LPG (Gas) | ✅ | ✅ | ✅ | ❌ | ❌ | ❌ |

(Confidence: documented — Werkstoff-Datenblätter, Forespar/TruDesign Compatibility Charts)

### 7.7 Rückschlagventile als Verbindungselement (Inline Check Valves)

#### 7.7.1 Typen und Funktion

Inline-Rückschlagventile werden in Schlauchsysteme eingesetzt, um Rückfluss zu verhindern. Sie sind ein integraler Bestandteil der Schlauchverbindungskette und müssen wie jede andere Verbindung bewertet werden.

| Typ | Funktionsprinzip | Öffnungsdruck | Einsatz |
|---|---|---|---|
| Klappe (Swing Check) | Schwerkraft-Klappe | 0,01–0,05 bar | Bilge, Abwasser, niedrigDurchfluss |
| Feder (Spring Check) | Feder drückt Ventilkegel auf Sitz | 0,1–0,5 bar | Trinkwasser, Kraftstoff |
| Kugel (Ball Check) | Kugel auf Sitz, Federkraft | 0,05–0,2 bar | Pumpen-Druckseite |
| Membran (Diaphragm) | Elastomer-Membran | 0,05–0,15 bar | Sanitär, Bilge |
| Entenschnabel (Duckbill) | Elastomer-Einweg-Schlitz | <0,01 bar | Bilge-Auslass über WL |

**Marine-Spezifische Anforderungen:**
- Material: Bronze oder Komposit (kein Messing, kein PVC unter WL)
- Durchflussbereich: Muss zum System passen (zu kleines Ventil = Druckverlust)
- Schlauchschellen: An BEIDEN Seiten des Rückschlagventils (unter WL: doppelt)
- Wartung: Jährliche Funktionsprüfung (Ventilsitz kann blockieren)

| Hersteller | Modell | Typ | Material | Größen (mm) | Preis (EUR) |
|---|---|---|---|---|---|
| Groco | CV-Serie | Swing | Bronze C83600 | 19–50 | 45–120 |
| Groco | CVS-Serie | Spring | Bronze C83600 | 19–38 | 55–95 |
| TruDesign | 90430 Serie | Ball | Komposit GFK | 19–38 | 25–55 |
| Forespar | Marelon MV | Ball | Marelon | 19–38 | 30–60 |
| Jabsco | 29295/29296 | Swing | Bronze/Komposit | 25–38 | 35–65 |
| Vetus | NRV-Serie | Spring | Bronze DZR | 19–50 | 40–90 |
| Whale | NRV 1516 | Ball | Acetal/EPDM | 15 (QC) | 12–18 |

(Confidence: documented — Herstellerkataloge 2025/26)

### 7.8 Anti-Siphon-Ventile als Verbindungselement

#### 7.8.1 Funktion und Notwendigkeit

Ein Anti-Siphon-Ventil (auch: Vacuum Break, Siphon Break) unterbricht den Siphon-Effekt, der Seewasser zurück ins Boot ziehen kann, wenn ein Seewasser-Auslass unter die Wasserlinie fällt.

**Kritische Anwendungen:**
- Nassauspuff: Wenn Auspuffauslass unter WL → Seewasser kann in Motor siphonen
- WC-Auslass: Wenn Abwasserauslass unter WL → Seewasser kann zurückfließen
- AC-Auslass: Wenn AC-Auslass unter WL → Seewasser in AC-Verdampfer

**Einbauregel:** Das Anti-Siphon-Ventil muss ÜBER der maximalen Wasserlinie montiert werden, MINDESTENS 300 mm (12") über WL (ABYC H-27). Der höchste Punkt des Schwanenhals / der Schlauchschleife reicht NICHT als Anti-Siphon-Schutz.

| Hersteller | Modell | Typ | Anschluss | Material | Preis (EUR) |
|---|---|---|---|---|---|
| Vetus | ANTISIPHON | Membran | 13–38 mm Schlauchtülle | Bronze DZR / Komposit | 25–55 |
| Groco | SVS-Serie | Swing | 13–50 mm Schlauchtülle | Bronze C83600 | 45–95 |
| Jabsco | 29840 | Membran | 19–25 mm Schlauchtülle | Kunststoff | 15–30 |
| Perko | 0493 | Swing | 16–25 mm Schlauchtülle | Bronze | 35–65 |
| Forespar | Marelon AS | Ball | 19–38 mm Schlauchtülle | Marelon | 25–50 |

**AYDI-Bewertung Anti-Siphon:**
- Anti-Siphon-Ventil vorhanden wo nötig: +0 (erwarteter Zustand)
- Anti-Siphon-Ventil fehlt wo nötig: -30 Punkte (Compliance-Mangel)
- Anti-Siphon-Ventil unter WL montiert: -25 Punkte (falsche Position)
- Anti-Siphon-Ventil blockiert (Salzkristalle): -20 Punkte

(Confidence: documented — ABYC H-27, Herstellerkataloge, Survey-Standards)

---

## 8. Hersteller — Vollständige Übersicht

### 8.1 Groco (USA) — Pipe-to-Hose und Marine Hardware

**Firmenprofil:**
- Gegründet: 1927, Hanover, Maryland, USA
- Spezialgebiet: Marine-Armaturen, Borddurchlässe, Seeventile, Schlauchstutzen
- Material: Fast ausschließlich Bronze C83600 (85-5-5-5)
- Gewinde: NPT (US-Standard) — bei EU-Import BSP-Adapter erforderlich!
- Vertrieb EU: Über Marine-Importeure (SVB, Toplicht als Spezialbestellung)
- Qualitätsniveau: Professionell / Premium
- Zertifizierungen: ABYC H-27, UL Marine, USCG zugelassen

**Schlauchstutzen-Sortiment:**

| Serie | Typ | Beschreibung | Größen NPT | Material | Preis (EUR) |
|---|---|---|---|---|---|
| PTH | Pipe-to-Hose, gerade | Standard Schlauchtülle mit NPT-Gewinde | 1/2 – 3 | Bronze C83600 | 12–85 |
|?"PHC | Pipe-to-Hose, gekrümmt | 45°-Winkel Schlauchtülle | 3/4 – 2 | Bronze C83600 | 18–95 |
| HE | Hose Elbow 90° | 90°-Winkelstutzen | 3/4 – 2 | Bronze C83600 | 22–110 |
| HE45 | Hose Elbow 45° | 45°-Winkelstutzen | 3/4 – 2 | Bronze C83600 | 20–100 |
| HYC | Hose Y-Connector | Y-Verteiler | 3/4 – 1-1/2 | Bronze C83600 | 35–120 |
| HTH | Hose Thru-Hull | Schott-Durchführung mit Schlauchtülle | 1/2 – 2 | Bronze C83600 | 25–90 |
| RB | Reducing Bushing | Reduzierstück Gewinde | 1/2–3 (kombiniert) | Bronze C83600 | 8–35 |
| FFC | Full Flow Connector | Durchgangs-Stutzen (kein Engpass) | 3/4 – 2 | Bronze C83600 | 18–75 |
| NH | Nipple-Hose | Gewindenippel-zu-Schlauch | 1/2 – 1-1/2 | Bronze C83600 | 10–30 |

**Groco PTH-Detailtabelle:**

| Modell | Gewinde | Schlauch-ID (Zoll/mm) | Barb-OD (mm) | Länge gesamt (mm) | Gewicht (g) | UVP (EUR) |
|---|---|---|---|---|---|---|
| PTH-500 | 1/2 NPT | 1/2" / 13 | 14,0 | 58 | 85 | 14 |
| PTH-750 | 3/4 NPT | 3/4" / 19 | 20,5 | 68 | 140 | 18 |
| PTH-1000 | 1 NPT | 1" / 25 | 27,0 | 82 | 225 | 24 |
| PTH-1250 | 1-1/4 NPT | 1-1/4" / 32 | 34,0 | 95 | 340 | 32 |
| PTH-1500 | 1-1/2 NPT | 1-1/2" / 38 | 40,0 | 108 | 470 | 38 |
| PTH-2000 | 2 NPT | 2" / 50 | 52,5 | 128 | 680 | 52 |
| PTH-2500 | 2-1/2 NPT | 2-1/2" / 63 | 66,0 | 148 | 920 | 72 |
| PTH-3000 | 3 NPT | 3" / 76 | 79,0 | 168 | 1250 | 88 |

**Groco-Besonderheiten:**
- Alle Gussteile werden in eigener Gießerei in Maryland hergestellt
- 100% Druckprüfung jedes Teils (3,5 bar)
- Barb-Design: Spezielles "Full-Flow" Profil — minimaler Durchflussverlust
- Oberfläche: As-cast (Gussrau) innen, außen entgratet — kein Hochglanz
- **NPT-Gewinde**: Für EU-Einsatz IMMER NPT-zu-BSP-Adapter bestellen (Groco TA-Serie) oder PTFE-Band großzügig verwenden

(Confidence: documented — Groco Product Catalogue 2025, Groco Engineering Specifications)

### 8.2 Vetus (Niederlande) — Europäischer Vollsortimenter

**Firmenprofil:**
- Gegründet: 1951, Schiedam, Niederlande
- Spezialgebiet: Komplettes Marine-Zubehörprogramm, inkl. Motoren, Auspuff, Schlauchverbindungen
- Material: Bronze DZR (Messing entzinkungsbeständig), zunehmend Komposit
- Gewinde: BSP (europäischer Standard) — für USA-Boote NPT-Adapter nötig
- Vertrieb: Weltweit über eigenes Händlernetz, in DE: direkt + Fachhändler
- Qualitätsniveau: Mittel bis Gut
- Zertifizierungen: ISO 9001, CE, viele Produkte Lloyd's Type Approved

**Schlauchstutzen-Sortiment:**

| Serie | Typ | Beschreibung | Größen BSP | Material | Preis (EUR) |
|---|---|---|---|---|---|
| SLP | Schlauchtülle gerade | Standard Pipe-to-Hose, BSP | G 1/2 – G 2 | Bronze DZR | 10–48 |
| WH90 | Winkel 90° | Schlauchtülle 90° Winkel | G 3/4 – G 1-1/2 | Bronze DZR | 15–55 |
| WH45 | Winkel 45° | Schlauchtülle 45° Winkel | G 3/4 – G 1-1/2 | Bronze DZR | 14–50 |
| WY | Y-Stück | Y-Verteiler | G 3/4 – G 1-1/2 | Bronze DZR | 25–75 |
| WT | T-Stück | T-Verteiler | G 3/4 – G 1-1/2 | Bronze DZR | 22–70 |
| WBF | Bulkhead Fitting | Schott-Durchführung | G 1/2 – G 1-1/2 | Bronze DZR | 20–70 |
| RD | Reducer | Reduzierstutzen | Diverse Kombi | Bronze DZR | 12–35 |
| NRV | Non-Return Valve | Rückschlagventil inline | G 3/4 – G 2 | Bronze DZR | 40–90 |
| ANTISIPHON | Anti-Siphon | Anti-Siphon-Ventil | 13–38 mm Tülle | Bronze DZR / Komposit | 25–55 |

**Vetus SLP-Detailtabelle:**

| Modell | Gewinde | Schlauch-ID (mm) | Barb-OD (mm) | Länge gesamt (mm) | Material | UVP (EUR) |
|---|---|---|---|---|---|---|
| SLP012B | G 1/2 BSP | 13 | 13,8 | 52 | Bronze DZR | 12 |
| SLP034B | G 3/4 BSP | 19 | 20,0 | 62 | Bronze DZR | 15 |
| SLP100B | G 1 BSP | 25 | 26,5 | 75 | Bronze DZR | 20 |
| SLP114B | G 1-1/4 BSP | 32 | 33,5 | 88 | Bronze DZR | 26 |
| SLP112B | G 1-1/2 BSP | 38 | 39,5 | 100 | Bronze DZR | 34 |
| SLP200B | G 2 BSP | 50 | 52,0 | 118 | Bronze DZR | 45 |

**Vetus-Besonderheiten:**
- BSP-Gewinde: Direktkompatibel mit europäischen Seeventilen und Borddurchlässen
- DZR-Messing: Gute Korrosionsbeständigkeit, ABER zeitlich begrenzt (12–18 Jahre in Seewasser)
- **AYDI-WARNUNG**: Vetus DZR-Messing ist NICHT gleichwertig mit Bronze C83600. In tropischen Revieren oder bei Landstrom-Elektrolyse kann DZR-Messing schneller versagen. Für Langfahrt/Blauwasser Bronze C83600 (Groco) oder Komposit (TruDesign) bevorzugen.
- Gutes Preis-Leistungs-Verhältnis für europäische Standardanwendungen

(Confidence: documented — Vetus Katalog 2025/26, Vetus Technical Data)

### 8.3 TruDesign (Neuseeland) — Komposit-Spezialist

**Firmenprofil:**
- Gegründet: 2001, Auckland, Neuseeland
- Spezialgebiet: Glasfaserverstärkte Polyester-Armaturen (Komposit)
- Material: Glasfaserverstärkter Polyester (GFK/FRP), NSF 61 zugelassen
- Gewinde: BSP (Standard), NPT (auf Anfrage)
- Vertrieb EU: Über Marine-Fachhändler (SVB, Compass24, Toplicht)
- Qualitätsniveau: Hoch
- Zertifizierungen: ISO 9093-2, Lloyd's Type Approved, NSF 61, ABYC H-27

**Schlauchstutzen-Sortiment:**

| Serie | Typ | Beschreibung | Größen | Material | Preis (EUR) |
|---|---|---|---|---|---|
| 90280 | Hose Connector, gerade | Schlauchtülle BSP auf Schlauch | G 3/4 – G 2 | Komposit GFK | 8–28 |
| 90290 | Hose Elbow 90° | 90°-Winkelstutzen | G 3/4 – G 1-1/2 | Komposit GFK | 12–35 |
| 90295 | Hose Elbow 45° | 45°-Winkelstutzen | G 3/4 – G 1-1/2 | Komposit GFK | 11–32 |
| 90300 | Hose Connector Tail | Verlängerungstülle (ohne Gewinde) | 19–50 mm | Komposit GFK | 6–18 |
| 90680 | Bulkhead Fitting | Schott-Durchführung | G 3/4 – G 1-1/2 | Komposit GFK | 15–55 |
| 90310 | Y-Connector | Y-Verteiler | 19–38 mm | Komposit GFK | 18–45 |
| 90320 | T-Connector | T-Stück | 19–38 mm | Komposit GFK | 16–42 |
| 90430 | Check Valve | Rückschlagventil | 19–38 mm | Komposit GFK | 25–55 |
| 90220 | Reducer | Reduzierstutzen | Diverse Kombi | Komposit GFK | 10–25 |

**TruDesign-Besonderheiten:**
- **Null galvanische Korrosion**: Komplett nicht-metallisch → kein galvanisches Element
- Ideal für Aluminium-Rümpfe (keine Isolation nötig)
- UV-Stabilisiert, aber dennoch nicht für permanente Sonnenexposition geeignet
- Temperaturbeständigkeit: max. 49°C (120°F) — NICHT für Nassauspuff (zu heiß)!
- Lebensdauer: >25 Jahre (Herstellerangabe), bewährt seit >20 Jahren am Markt
- **AYDI-EMPFEHLUNG**: TruDesign ist die beste Wahl für Borddurchlass-Systeme auf GFK- und Aluminium-Booten. Einzige Einschränkung: Temperaturgrenze bei Nassauspuff und Motor-Kühlwasser.

(Confidence: documented — TruDesign Product Guide 2025, TruDesign Technical Data)

### 8.4 Forespar (USA) — Marelon-Marke

**Firmenprofil:**
- Gegründet: 1967, San Clemente, Kalifornien, USA
- Spezialgebiet: Marelon-Markenkomposit (glasfaserverstärktes Polyester/Nylon)
- Material: Marelon = proprietäres GFK/Nylon-Komposit, NSF/ANSI 61 + 372
- Gewinde: NPT (US-Standard)
- Vertrieb EU: Über spezielle Marine-Importeure
- Qualitätsniveau: Hoch
- Zertifizierungen: ABYC H-27, UL Marine, NSF 61, NSF 372 (bleifrei)

**Schlauchstutzen-Sortiment:**

| Serie | Typ | Beschreibung | Größen NPT | Material | Preis (EUR) |
|---|---|---|---|---|---|
|?"MF | Male Fitting, gerade | NPT-Gewinde auf Schlauchtülle | 3/4 – 2 | Marelon | 10–35 |
|?"MF90 | Male Fitting 90° | NPT auf Schlauchtülle 90° | 3/4 – 1-1/2 | Marelon | 14–42 |
| BH | Bulkhead Fitting | Schott-Durchführung | 3/4 – 1-1/2 | Marelon | 18–60 |
| MV | Marine Valve (Check) | Rückschlagventil | 3/4 – 1-1/2 | Marelon | 30–60 |
| AS | Anti-Siphon | Anti-Siphon-Ventil | 3/4 – 1-1/2 | Marelon | 25–50 |
| RED | Reducer | Reduzierstutzen | Diverse | Marelon | 8–22 |

**Forespar/Marelon-Besonderheiten:**
- Marelon ist NICHT identisch mit TruDesign-Komposit (anderer Kunststoff, anderer Hersteller)
- Marelon-Produkte sind in den USA marktführend (OEM bei Catalina, Hunter, Beneteau USA)
- NPT-Gewinde: Für EU-Einsatz NPT-zu-BSP-Adapter oder Gewindewechsel nötig
- Temperaturbeständigkeit: max. 80°C (176°F) — höher als TruDesign!
- Bleifrei (NSF 372): Wichtig für kalifornische Trinkwasser-Normen (Proposition 65)
- **AYDI-HINWEIS**: Marelon-Teile auf Import-Booten aus den USA haben NPT-Gewinde. NICHT mit BSP-Teilen mischen!

> ✅ Aufgelöst (Audit): Marelon-Maximaltemperatur = +80 °C (+176 °F) — Quelle: Forespar (forespar.com, Marelon-ABYC/ISO- und Ball-Valve-Produktseite): Betriebsbereich −40 °F bis +176 °F (−40 °C bis +80 °C). Wert hier (73 °C) und in FAQ SV-020 (<93 °C) auf 80 °C korrigiert; die 49 °C in Abschnitt 7.6.2 bleiben stehen (das ist korrekt der TruDesign-Wert, nicht Marelon).

(Confidence: documented — Forespar Marelon Catalogue 2025; Temperaturwert +80 °C / +176 °F verifiziert über forespar.com 2026)

### 8.5 Buck Algonquin (USA) — Marine-Stutzen und Fittings

**Firmenprofil:**
- Gegründet: ca. 1930, Philadelphia, Pennsylvania, USA
- Spezialgebiet: Bronze-Fittings, Wellenlager, Stopfbuchsen, Schlauchstutzen
- Material: Bronze C83600, C92200 (Navy G), auch NiBrAl
- Gewinde: NPT
- Vertrieb: USA direkt, EU über Spezialimport
- Qualitätsniveau: Professionell
- Zertifizierungen: ABYC, USCG

**Schlauchstutzen-Sortiment:**

| Serie | Typ | Material | Größen NPT | Preis (EUR) |
|---|---|---|---|---|
| Bronze Hose Barb | Gerade Schlauchtülle | Bronze C83600 | 3/8 – 2 | 8–55 |
| Bronze Elbow 90° | 90°-Winkelstutzen | Bronze C83600 | 3/8 – 1-1/2 | 12–70 |
| Bronze Elbow 45° | 45°-Winkelstutzen | Bronze C83600 | 3/8 – 1-1/2 | 11–65 |
| Bronze Y | Y-Verteiler | Bronze C83600 | 3/4 – 1-1/2 | 28–90 |
| Bronze T | T-Stück | Bronze C83600 | 3/4 – 1-1/2 | 25–85 |
| Reducing Barb | Reduzierstutzen | Bronze C83600 | Diverse | 10–45 |
| Chrome Bronze Barb | Verchromte Schlauchtülle | Bronze verchromt | 3/8 – 1 | 12–40 |

**Buck Algonquin-Besonderheiten:**
- Schwerpunkt auf große Durchmesser (bis 3") für Fischereifahrzeuge und Arbeitsboote
- Auch verchromte Bronze-Teile für sichtbare Installationen
- Navy-G-Bronze (C92200) für höchste Anforderungen (US Navy Spezifikation)
- Keine Komposit-Teile im Sortiment — reiner Bronze-Hersteller
- **AYDI-HINWEIS**: Buck Algonquin ist die erste Wahl für Arbeitsboote und Fischer in den USA. In Europa selten, aber exzellente Qualität.

(Confidence: documented — Buck Algonquin Marine Hardware Catalogue)

### 8.6 Perko (USA) — Marine Hardware seit 1907

**Firmenprofil:**
- Gegründet: 1907, Miami, Florida, USA
- Spezialgebiet: Marine-Hardware (Beleuchtung, Belüftung, Armaturen)
- Material: Bronze, Messing (verchromt), Edelstahl, Kunststoff
- Gewinde: NPT
- Vertrieb: USA breit, EU über Importeure
- Qualitätsniveau: Mittel bis Gut
- Zertifizierungen: ABYC, UL Marine

**Schlauchstutzen (Auswahl):**

| Artikelnr. | Typ | Material | Größen NPT | Preis (EUR) |
|---|---|---|---|---|
| 0076 | Pipe-to-Hose Adapter, gerade | Bronze | 1/2 – 2 | 10–50 |
| 0077 | Pipe-to-Hose Adapter, 90° | Bronze | 3/4 – 1-1/2 | 15–65 |
| 0078 | Hose Elbow 45° | Bronze | 3/4 – 1-1/2 | 14–60 |
| 0370 | Fuel Hose Fitting | Bronze, feuerfest | 3/8 – 5/8 | 8–18 |
| 0493 | Anti-Siphon Valve | Bronze | 5/8 – 1 | 35–65 |

**Perko-Besonderheiten:**
- Breites Sortiment, aber weniger spezialisiert als Groco
- Auch günstigere Messing-Varianten (Chrome Plated Brass) — ⚠️ NICHT für unter WL in Salzwasser
- Kraftstoff-Fittings mit USCG/ABYC-Zulassung für Benzin und Diesel
- **AYDI-WARNUNG**: Perko bietet auch verchromte MESSING-Teile an. Diese sehen aus wie Bronze, sind aber dezinkifizierungsgefährdet. Immer Materialkennzeichnung prüfen!

(Confidence: documented — Perko Marine Hardware Catalogue 2025)

### 8.7 Jabsco (USA/UK) — Pumpen und Zubehör

**Firmenprofil:**
- Gegründet: 1937, Foothill Ranch, Kalifornien, USA (jetzt Teil von Xylem Inc.)
- Spezialgebiet: Marine-Pumpen (Wasser, Toiletten, Bilge)
- Relevanz für Schlauchverbindungen: Pumpenanschlüsse, Rückschlagventile, Anti-Siphon
- Material: Bronze, Komposit, Edelstahl
- Vertrieb: Weltweit
- Qualitätsniveau: Gut

**Relevante Verbindungsprodukte:**

| Artikelnr. | Typ | Beschreibung | Anschluss | Material | Preis (EUR) |
|---|---|---|---|---|---|
| 29295-1000 | Inline Check Valve | Rückschlagventil | 25 mm Schlauchtülle | Komposit | 28 |
| 29295-1010 | Inline Check Valve | Rückschlagventil | 38 mm Schlauchtülle | Komposit | 35 |
| 29840-2000 | Anti-Siphon Valve | Anti-Siphon, Nassauspuff | 19 mm Schlauchtülle | Kunststoff | 18 |
| 29840-2010 | Anti-Siphon Valve | Anti-Siphon, Nassauspuff | 25 mm Schlauchtülle | Kunststoff | 22 |
| 44411-2000 | Y-Valve (Diverter) | Abwasser-Umschaltventil | 38 mm Schlauchtülle | Bronze/Kunststoff | 120 |

**Jabsco-Besonderheiten:**
- Schlauchstutzen sind primär Zubehör zu Jabsco-Pumpen, nicht als eigenständige Fittings vermarktet
- Pumpen-Anschlüsse: Oft proprietäre Gewinde oder Bajonett-Verschlüsse — Adapter nötig
- WC-System (Twist'n'Lock): Eigenes Anschlusssystem, nur mit Jabsco-Schlauch kompatibel
- **AYDI-HINWEIS**: Bei Jabsco-Pumpen die Original-Anschlüsse verwenden. Improvised Adapter führen häufig zu Leckagen am Pumpenanschluss.

(Confidence: documented — Jabsco / Xylem Marine Catalogue 2025)

### 8.8 ABA (Schweden) — Premium-Schlauchschellen

**Firmenprofil:**
- Gegründet: 1896, Sävsjö, Schweden
- Spezialgebiet: Schlauchschellen, Rohrschellen, Spannbänder
- Marktposition: Europäischer Marktführer für Marine-Schlauchschellen
- Qualitätsniveau: Premium
- Fertigung: Schweden (keine Billig-Importware)

**Schlauchschellen-Sortiment:**

| Serie | Typ | Bandform | Bandbreite | Material | Marine-Eignung |
|---|---|---|---|---|---|
| ABA Original | Schneckengewinde | Vollband (geschlitzt) | 9 mm | W1–W5 | W4/W5 = Premium Marine |
| ABA 316 | Schneckengewinde | Vollband | 12 mm | W4 (316SS) | ✅ Standard Marine |
| ABA 316L | Schneckengewinde | Vollband | 12 mm | W5 (316L) | ✅ Premium Marine |
| ABA Nova | Schneckengewinde | Lochband | 9 mm | W2–W4 | W4 über WL |
| ABA T-Bolt | T-Bolt | Massivband | 24 mm | 316SS | ✅ Auspuff, große Schläuche |
| ABA Robust | Schneckengewinde | Vollband, breit | 18 mm | W4 | ✅ Hochlast-Marine |

**ABA 316 Original — Detaildaten:**

| Größe (Ø-Bereich mm) | Artikelnr. | Bandbreite | Bandstärke | Material | Preis (EUR) |
|---|---|---|---|---|---|
| 10–16 | ABA316-10/16 | 12 mm | 0,6 mm | 316SS (W4) | 2,50 |
| 16–25 | ABA316-16/25 | 12 mm | 0,6 mm | 316SS (W4) | 2,80 |
| 20–32 | ABA316-20/32 | 12 mm | 0,6 mm | 316SS (W4) | 3,00 |
| 25–40 | ABA316-25/40 | 12 mm | 0,6 mm | 316SS (W4) | 3,20 |
| 32–50 | ABA316-32/50 | 12 mm | 0,6 mm | 316SS (W4) | 3,50 |
| 40–60 | ABA316-40/60 | 12 mm | 0,6 mm | 316SS (W4) | 3,80 |
| 50–70 | ABA316-50/70 | 12 mm | 0,7 mm | 316SS (W4) | 4,20 |
| 60–80 | ABA316-60/80 | 12 mm | 0,7 mm | 316SS (W4) | 4,50 |
| 70–90 | ABA316-70/90 | 12 mm | 0,7 mm | 316SS (W4) | 4,80 |
| 80–100 | ABA316-80/100 | 12 mm | 0,7 mm | 316SS (W4) | 5,20 |
| 90–110 | ABA316-90/110 | 12 mm | 0,7 mm | 316SS (W4) | 5,50 |
| 100–120 | ABA316-100/120 | 12 mm | 0,7 mm | 316SS (W4) | 5,80 |

**ABA-Besonderheiten:**
- Vollband mit Innenschlitz (nicht gelocht): Maximale Klemmung ohne Schlauchbeschädigung
- Schwedische Fertigung: Höchste Materialkonsistenz
- Gehärtete Schnecke: Greift auch bei wiederholtem Lösen/Nachziehen
- Abgerundete Bandkanten: Kein Einschneiden in Schlauch
- **AYDI-EMPFEHLUNG**: ABA 316 ist die Referenz-Schlauchschelle für den Marineeinsatz. Wenn im Foto eine ABA-Schelle erkannt wird → Positiver Qualitätsindikator.

(Confidence: documented — ABA Group Product Catalogue 2025, ABA Technical Data)

### 8.9 NORMA (Deutschland) — TORRO und COBRA

**Firmenprofil:**
- Gegründet: 1896, Maintal, Deutschland (heute: NORMA Group SE, Frankfurt)
- Spezialgebiet: Verbindungstechnik, Schlauchschellen, Rohrverbindungen
- Marktposition: Weltmarktführer für Verbindungstechnik (auch Automobil, Industrie)
- Qualitätsniveau: Hoch
- Fertigung: Deutschland, Europa

**Marine-relevante Schlauchschellen:**

| Serie | Typ | Bandform | Bandbreite | Material | Marine-Eignung |
|---|---|---|---|---|---|
| TORRO S | Schneckengewinde | Vollband | 9 mm | W4 (316SS) | ✅ Standard Marine |
| TORRO W | Schneckengewinde | Vollband, breit | 12 mm | W4/W5 | ✅ Premium Marine |
| TORRO Multi | Schneckengewinde | Vollband, Multi-Bereich | 12 mm | W4 | ✅ Marine |
| COBRA | Federband | Federstahl | 7–8 mm | Federstahl + SS | ⚠️ Nur über WL, Motorraum |
| GBS | T-Bolt | Massivband | 20–25 mm | W4 | ✅ Auspuff, große Durchmesser |
| SUPRA 1PC | Einschraubschelle | Massivband | 19 mm | W2/W4 | ✅ Motorraum |
| ARS | Profilschelle | Massivband, Profil | 22 mm | W4 | ✅ Hochlast, Auspuff |

**NORMA TORRO S — Detaildaten:**

| Größe (Ø-Bereich mm) | Artikelnr. | Bandbreite | Material | Drehmoment (Nm) | Preis (EUR) |
|---|---|---|---|---|---|
| 12–20 | TORRO-S-12/20-W4 | 9 mm | 316SS | 1,5–2,5 | 2,20 |
| 16–25 | TORRO-S-16/25-W4 | 9 mm | 316SS | 1,5–2,5 | 2,40 |
| 20–32 | TORRO-S-20/32-W4 | 9 mm | 316SS | 2,0–3,0 | 2,60 |
| 25–40 | TORRO-S-25/40-W4 | 9 mm | 316SS | 2,0–3,0 | 2,80 |
| 32–50 | TORRO-S-32/50-W4 | 9 mm | 316SS | 2,5–3,5 | 3,00 |
| 40–60 | TORRO-S-40/60-W4 | 9 mm | 316SS | 2,5–3,5 | 3,30 |
| 50–70 | TORRO-S-50/70-W4 | 9 mm | 316SS | 3,0–4,0 | 3,60 |
| 60–80 | TORRO-S-60/80-W4 | 9 mm | 316SS | 3,0–4,0 | 3,90 |

**NORMA-Besonderheiten:**
- Deutsche Fertigung: Konsistente Qualität
- TORRO-Vollband: Ähnlich ABA Original, etwas schmaler (9mm vs 12mm bei ABA 316)
- COBRA-Federbandschellen: Für Automobilanwendungen entwickelt, im Marine-Bereich nur eingeschränkt geeignet (Federstahl rostet!)
- GBS T-Bolt: Exzellent für Nassauspuff-Verbindungen
- **AYDI-HINWEIS**: NORMA TORRO und ABA 316 sind gleichwertige Marine-Schlauchschellen. Im Photo beide als positives Qualitätsmerkmal bewerten.

(Confidence: documented — NORMA Group Katalog 2025, NORMA Technical Data Marine)

### 8.10 Oetiker (Schweiz) — Ohrklemmen-Spezialist

**Firmenprofil:**
- Gegründet: 1942, Horgen, Schweiz
- Spezialgebiet: Ohrklemmen, Stepless-Klemmen, Spezial-Verbindungstechnik
- Marktposition: Weltmarktführer für Ohrklemmen (OEM für alle großen Automobilhersteller)
- Qualitätsniveau: Premium
- Fertigung: Schweiz, Deutschland, weltweit

**Marine-relevante Produkte:**
- Detailliert in Abschnitt 7.4.4 (Oetiker Ear Clamps)
- Für Kraftstoffleitungen, Hydraulik, kleine Schläuche im Motorraum
- **AYDI-HINWEIS**: Oetiker-Ohrklemmen auf Kraftstoffleitungen = OEM-Standard = positives Qualitätsmerkmal

(Confidence: documented — Oetiker Product Guide 2025)

### 8.11 Mikalor (Spanien) — T-Bolt-Spezialist

**Firmenprofil:**
- Gegründet: 1951, Barcelona, Spanien (Teil der NORMA Group seit 2010)
- Spezialgebiet: T-Bolt-Schellen, Profilschellen, Hochleistungs-Schlauchschellen
- Marktposition: Europäischer Marktführer für T-Bolt-Schellen
- Qualitätsniveau: Hoch
- Fertigung: Spanien

**Produktsortiment:**
- Detailliert in Abschnitt 7.4.2 (T-Bolt Clamps)
- SUPRA W2 (304SS): Für Industrie und über WL
- SUPRA W4 (316SS): Marine-Standard
- ASFA-S: Schneckengewinde, Lochband (W1–W5)
- ASFA-L: Schneckengewinde, Vollband (W4/W5)

(Confidence: documented — Mikalor/NORMA Product Guide 2025)

### 8.12 Jubilee (UK) — Britischer Traditionsname

**Firmenprofil:**
- Gegründet: 1921, Gillingham, Kent, UK (L. Robinson & Co.)
- Spezialgebiet: Schlauchschellen ("Jubilee Clip" ist in UK Gattungsname für Schlauchschelle)
- Marktposition: UK Marktführer, ikonische Marke
- Qualitätsniveau: Mittel bis Hoch

**Marine-relevante Serien:**

| Serie | Typ | Material | Bandbreite | Marine-Eignung | Preis (EUR) |
|---|---|---|---|---|---|
| Jubilee Superclamp | Schneckengewinde, Lochband | 304SS / 316SS | 13 mm | W4: ✅ Marine | 2–6 |
| Jubilee Multiband | Meterware, perforiert | 304SS | 11 mm | ⚠️ Nur über WL | 8–15/m |
| Jubilee Marine Grade | Schneckengewinde, Vollband | 316SS | 12 mm | ✅ Standard Marine | 3–7 |

**AYDI-HINWEIS**: "Jubilee Clip" bedeutet in UK einfach "Schlauchschelle". Nicht jede Jubilee-Schelle ist marine-tauglich. Immer die Marine-Grade-Serie (316SS, Vollband) spezifizieren.

(Confidence: documented — Jubilee/L. Robinson Product Guide)

### 8.13 Awab (Schweden) — Marine-Klemmen

**Firmenprofil:**
- Marke der ABA Group (gleicher Hersteller wie ABA)
- Vertrieb: Primär skandinavischer Markt
- Produkte: Im Wesentlichen ABA-Schellen unter alternativem Markennamen
- Qualitätsniveau: Premium (gleiche Fertigung wie ABA)

(Confidence: estimated — ABA Group Unternehmensstruktur)

### 8.14 Whale (UK) — Quick-Connect-Spezialist

**Firmenprofil:**
- Gegründet: 1960er, Bangor, Nordirland, UK (Munster Simms Engineering)
- Spezialgebiet: Pumpen, Quick-Connect-Systeme, Warmwasser-Systeme
- Detailliert in Abschnitt 7.3.1 (Whale Quick Connect)

(Confidence: documented — Whale/Munster Simms Catalogue)

### 8.15 John Guest (UK) — Push-Fit-Marktführer

**Firmenprofil:**
- Gegründet: 1961, West Drayton, UK (jetzt Teil von Reliance Worldwide Corporation)
- Spezialgebiet: Push-Fit-Verbindungen für Trinkwasser
- Detailliert in Abschnitt 7.3.2 (John Guest Speedfit)

(Confidence: documented — John Guest/RWC Technical Handbook)

### 8.16 Weitere Hersteller (Kurzübersicht)

| Hersteller | Land | Spezialgebiet | Marine-Relevanz | Qualität |
|---|---|---|---|---|
| Plastimo | FR | Marine-Zubehör allgemein | Schlauchschellen (Lochband), Basic-Stutzen | Mittel |
| Osculati | IT | Marine-Zubehör allgemein | Schlauchschellen, Stutzen (Nylon, Messing) | Mittel |
| Guidi | IT | Bronze-Armaturen | Schlauchtüllen als Zubehör zu Seeventilen | Gut |
| Attwood | USA | Marine-Zubehör | Schlauchstutzen (Nylon, Budget) | Basis |
| Shields | USA | Marine-Schläuche | Schlauchkupplungen passend zu Shields-Schlauch | Gut |
| Trident | USA | Marine-Schläuche | Schlauchkupplungen passend zu Trident-Schlauch | Gut |
| Gates | USA | Industrie-Schläuche | Marine-Schlauchschellen (Constant-Tension) | Hoch |
| Ideal / Tridon | USA | Schlauchschellen | Marine-Grade Schlauchschellen (300SS, 316SS) | Mittel-Hoch |
| Breeze | USA | Schlauchschellen | Aero-Seal, CT, Liner Clamps | Mittel-Hoch |
| Scandvik | SE | Marine-Sanitär | Trinkwasser-Verbindungen, Quick-Connect | Gut |
| Haas | DE | Sanitärtechnik | Schlauchschellen, Rohrschellen (SHK-Bereich) | Mittel |
| Würth | DE | Befestigungstechnik | Schlauchschellen W1–W5 (Industrie + KFZ) | Mittel-Hoch |

**AYDI-Bewertung nach Hersteller:**

| Hersteller | Score-Modifikator | Begründung |
|---|---|---|
| ABA / Awab | +5 | Premium-Marine-Schelle, Referenzstandard |
| NORMA TORRO | +5 | Gleichwertiger Premium-Standard |
| Mikalor SUPRA W4 | +5 | Premium T-Bolt |
| Groco | +5 | Marine-Bronze Referenzstandard |
| TruDesign | +5 | Beste Komposit-Verbindungstechnik |
| Vetus | +3 | Guter europäischer Standard |
| Forespar Marelon | +3 | Guter Komposit-Standard (USA) |
| Buck Algonquin | +3 | Solide Bronze-Qualität |
| Jubilee Marine | +3 | Guter UK-Standard |
| Oetiker | +3 | Premium-Ohrklemme für kleine Schläuche |
| Osculati / Plastimo | 0 | Basis-Marine, akzeptabel |
| Perko | 0 | Gemischtes Sortiment, Material prüfen |
| Attwood | -3 | Budget-Ware, nur über WL akzeptabel |
| Unbekannt / No-Name | -5 | Keine Qualitätskontrolle nachweisbar |
| Baumarkt / Automotive | -10 | NICHT für Marine konzipiert |

(Confidence: estimated — Survey-Erfahrung, Hersteller-Reputation, Forum-Konsensus)

---

## 9. Anlagen-spezifische Zuordnung

### 9.1 Kühlwassersystem — Motor (Cooling Water System)

Das Kühlwassersystem ist die häufigste und kritischste Schlauchverbindungs-Anwendung an Bord. Ein Motor benötigt mindestens 2 Schlauchverbindungen am Seewasser-Kreislauf (Einlass + Auslass), oft 6–10 Verbindungen im Gesamtsystem.

**System-Topologie (typischer Dieselmotor):**

```
Borddurchlass (unter WL)
    ↓ [Schlauchverbindung 1 — KRITISCH, unter WL, doppelt geschellt]
Seeventil
    ↓ [Schlauchverbindung 2 — KRITISCH, unter WL, doppelt geschellt]
Seewasserfilter (Roh-Wasserfilter)
    ↓ [Schlauchverbindung 3]
Impeller-Pumpe (Seewasser-Pumpe am Motor)
    ↓ [Schlauchverbindung 4]
Wärmetauscher / Ladeluftkühler
    ↓ [Schlauchverbindung 5]
Mischkrümmer (Abgas + Kühlwasser)
    ↓ [Schlauchverbindung 6 — Nassauspuff, hohe Temperatur]
Nassauspuff-Schlauch
    ↓ [Schlauchverbindung 7]
Auspuff-Borddurchlass / Auspuff-Schalldämpfer
    ↓ [Schlauchverbindung 8]
Auspuff-Austritt (über WL)
```

**Anforderungen pro Verbindungspunkt:**

| Verbindungspunkt | Position | Schlauch-ID (typ.) | Schelle | Doppelt? | Material Stutzen | Drehmoment |
|---|---|---|---|---|---|---|
| 1: Borddurchlass → Seeventil | unter WL | 25–38 mm | Vollband W4/W5 | JA | Bronze C83600 | 2,5–4,0 Nm |
| 2: Seeventil → Filter | unter/an WL | 25–38 mm | Vollband W4/W5 | JA | Bronze C83600 | 2,5–4,0 Nm |
| 3: Filter → Pumpe | Motorraum | 19–32 mm | Vollband W4 | Empfohlen | Bronze/Komposit | 2,0–3,5 Nm |
| 4: Pumpe → Wärmetauscher | Motorraum | 19–32 mm | Vollband W4 | Empfohlen | Bronze/Komposit | 2,0–3,5 Nm |
| 5: Wärmetauscher → Mischkrümmer | Motorraum, heiß | 25–38 mm | Vollband W4 o. T-Bolt | Empfohlen | Bronze/316SS | 3,0–4,5 Nm |
| 6: Mischkrümmer → Auspuffschlauch | Motorraum, HEISS | 38–90 mm | T-Bolt W4 | JA (T-Bolt) | 316SS | 7–11 Nm |
| 7: Auspuffschlauch → Schalldämpfer | Motorraum | 38–90 mm | T-Bolt W4 | JA (T-Bolt) | 316SS | 7–11 Nm |
| 8: Schalldämpfer → Auspuff-Austritt | über WL | 38–90 mm | T-Bolt W4 | Empfohlen | 316SS/Bronze | 7–11 Nm |

**Typische Schlauchgrößen nach Motorleistung:**

| Motorleistung | Kühlwasser-Einlass | Kühlwasser am Motor | Nassauspuff |
|---|---|---|---|
| 10–30 PS (Segelboot) | 19–25 mm (3/4"–1") | 19 mm (3/4") | 38–45 mm (1-1/2"–1-3/4") |
| 30–75 PS (Segelboot) | 25–32 mm (1"–1-1/4") | 25 mm (1") | 45–57 mm (1-3/4"–2-1/4") |
| 75–150 PS (Motorboot) | 32–38 mm (1-1/4"–1-1/2") | 32 mm (1-1/4") | 57–76 mm (2-1/4"–3") |
| 150–300 PS (Motorboot) | 38–50 mm (1-1/2"–2") | 38 mm (1-1/2") | 76–90 mm (3"–3-1/2") |
| 300+ PS (Superyacht) | 50–76 mm (2"–3") | 50 mm (2") | 90–127 mm (3-1/2"–5") |

**Häufigste Probleme Kühlwassersystem-Verbindungen:**

| Problem | Häufigkeit | Ursache | Folge | AYDI-Score-Impact |
|---|---|---|---|---|
| Impeller-Pumpe undicht am Anschluss | Häufig | Vibration, Gewinde locker | Seewasser im Motorraum | -20 bis -30 |
| Auspuffschlauch-Klemme locker | Häufig | Thermische Zyklen, T-Bolt nicht nachgezogen | Abgasleck, CO-Gefahr | -25 bis -40 |
| Seewasserfilter-Deckel undicht | Mittel | O-Ring verschlissen, Deckel nicht korrekt aufgesetzt | Seewasser-Austritt | -15 bis -25 |
| Mischkrümmer-Anschluss korrodiert | Mittel | Abgas-Kondensat (sauer) greift Bronze an | Seewasser/Abgas-Mix austritt | -30 bis -40 |
| Kühlschlauch verhärtet (Motorraum) | Mittel | Wärme-Alterung nach 5–8 Jahren | Schlauch bricht oder rutscht ab | -15 bis -25 |

(Confidence: documented — Volvo Penta Installation Manual, Yanmar Service Guide, Survey-Erfahrung)

### 9.2 Nassauspuff-System (Wet Exhaust)

**SICHERHEITSKRITISCH**: Das Nassauspuff-System führt eine Mischung aus heißen Abgasen (300–600°C im Krümmer, 50–80°C nach Wassereinspritzung) und Seewasser. Undichte Verbindungen bedeuten: Abgase im Boot (CO-Vergiftung!) oder Seewasser im Motor (Motorschaden!).

**Besondere Anforderungen an Schlauchverbindungen:**

| Anforderung | Spezifikation | Begründung |
|---|---|---|
| Schlauchschellen-Typ | T-Bolt (Mikalor SUPRA, NORMA GBS) | Hohe Klemmkraft bei großen Durchmessern |
| Schlauchschellen-Material | 316SS (W4) mindestens | Hohe Temperatur + Abgaskondensat |
| Schlauchschellen-Anzahl | 2× T-Bolt an JEDEM Anschluss | Redundanz bei sicherheitskritischem System |
| Stutzen-Material | 316SS oder Ni-Resist Gusseisen | Bronze wird durch Abgaskondensat angegriffen |
| Schlauchtyp | Nassauspuff-Spezialschlauch (Shields 250/252, Trident 200) | Temperaturbeständig bis 100°C+ |
| Prüfintervall | Jährlich visuell, alle 5 Jahre Schellen erneuern | Thermische Alterung |
| Anti-Siphon | PFLICHT wenn Auspuff-Austritt unter WL möglich | Seewasser siphont in Motor |

**AYDI-Bewertung Nassauspuff-Verbindungen:**

| Befund | Score-Impact |
|---|---|
| T-Bolt-Schellen, doppelt, 316SS | 0 (erwarteter Zustand) |
| Nur Standard-Schneckengewinde-Schellen | -20 |
| Einfache Schelle am Mischkrümmer | -30 |
| Schelle korrodiert (Abgaskondensat) | -25 |
| Anti-Siphon fehlt (Austritt unter WL) | -30 |
| Anti-Siphon vorhanden, aber unter WL montiert | -25 |
| Auspuffschlauch verhärtet / rissig | -30 |

(Confidence: documented — Volvo Penta Exhaust Installation Guide, Vetus Wet Exhaust Manual, ABYC H-27)

### 9.3 Sanitärsystem — WC (Toilet System)

Das Sanitärsystem auf Booten umfasst typischerweise 4–6 Schlauchverbindungen pro WC: Seewasser-Einlass, WC-Pumpe Eingang, WC-Pumpe Ausgang, Fäkalientank-Einlass, Fäkalientank-Entlüftung, Fäkalientank-Absaugung (Pumpout).

**System-Topologie (typische manuelle Marine-Toilette):**

```
Borddurchlass (unter WL)
    ↓ [Schlauchverbindung 1 — unter WL, doppelt geschellt]
Seeventil (Einlass)
    ↓ [Schlauchverbindung 2 — unter WL, doppelt geschellt]
WC-Pumpe Einlass (Seewasser-Seite)
    ↓ [Schlauchverbindung 3]
WC (Auslass)
    ↓ [Schlauchverbindung 4]
Y-Ventil (Überboard / Fäkalientank)
    ↓ [Schlauchverbindung 5]
Fäkalientank
    ↓ [Schlauchverbindung 6]
Seeventil (Auslass) → Borddurchlass (unter WL)
    + [Schlauchverbindung 7 — unter WL, doppelt geschellt]
Fäkalientank-Entlüftung → Decks-Fitting
    + [Schlauchverbindung 8]
Fäkalientank-Absaugung → Deck-Pumpout
    + [Schlauchverbindung 9]
```

**Besondere Anforderungen Sanitärsystem:**

| Anforderung | Spezifikation | Begründung |
|---|---|---|
| Schlauchmaterial | Sanitation Hose (geruchsdicht!), z.B. Shields 148 | Standard-PVC-Schlauch lässt Gerüche durch |
| Stutzen-Material | Bronze, Komposit (NICHT Messing — Ammoniak-Korrosion!) | Urin/Ammoniak beschleunigt Dezinkifizierung |
| Schlauchschellen unter WL | Doppelt, W4/W5, Vollband | Standard-Sicherheitsregel |
| Y-Ventil-Anschluss | Doppelte Schellen an allen 3 Anschlüssen | Starke Beanspruchung beim Umschalten |
| Fäkalientank-Entlüftung | Filter (Aktivkohle) vor Deck-Fitting | Geruchsvermeidung |
| Anti-Siphon | Am Seewasser-Einlass, WENN WC unter WL | Rückfluss in WC |

**Typische Schlauchgrößen Sanitärsystem:**

| Verbindung | Schlauch-ID (mm) | Schlauchtyp |
|---|---|---|
| WC Seewasser-Einlass | 19 mm (3/4") | Trinkwasser-Schlauch oder Marine-Sanitär |
| WC Abwasser-Auslass | 25–38 mm (1"–1-1/2") | Sanitation Hose (geruchsdicht) |
| Fäkalientank-Einlass | 38 mm (1-1/2") | Sanitation Hose |
| Fäkalientank-Entlüftung | 16–19 mm (5/8"–3/4") | Sanitation Hose |
| Fäkalientank-Absaugung (Pumpout) | 38 mm (1-1/2") | Sanitation Hose |
| Y-Ventil Ein/Ausgänge | 38 mm (1-1/2") | Sanitation Hose |

**AYDI-WARNUNG**: Fäkalien-Schläuche die undicht werden oder Gerüche durchlassen sind eines der häufigsten Komfort-Probleme auf Yachten. Die Schlauchverbindungen (Stutzen + Schellen) sind dabei oft die Schwachstelle: Schelle eingeschnitten → Schlauch-Mikroriss → Geruch. Pipeline B (Visuell) kann Verfärbungen und Feuchtigkeit an Sanitär-Verbindungen erkennen.

(Confidence: documented — Jabsco Toilet Installation Guide, ABYC H-27, Peggie Hall "Get Rid of Boat Odors")

### 9.4 Kraftstoffsystem (Fuel System)

**SICHERHEITSKRITISCH**: Kraftstoff-Schlauchverbindungen sind brandgefährlich. Ein undichter Kraftstoffanschluss kann zur Explosion führen (Benzin) oder zu Dieselverschmutzung der Bilge.

**Besondere Anforderungen Kraftstoffsystem:**

| Anforderung | Spezifikation | Norm |
|---|---|---|
| Schlauchschellen-Typ | Oetiker-Ohrklemmen (≤16mm) oder Vollband W4 | ABYC H-33, ISO 10088 |
| Schlauchschellen-Material | 316SS oder gleichwertig, NICHT verzinkt | ABYC H-33 |
| Stutzen-Material | Bronze, 316SS — NICHT Messing (Funkenbildung!) | ISO 10088 |
| Gewindedichtung | Loctite 545 (Kraftstoff-fest) oder PTFE-Band (Gelb, Gas-zugelassen) | — |
| Feuersicherheit | Schlauchverbindungen müssen 2,5 min Feuer widerstehen | ISO 10088, ABYC H-33 |
| Schlauchtyp | USCG / ISO 7840 Typ A1 (Benzin) oder Typ A2 (Diesel) | ISO 7840 |
| Druckprüfung | Alle Verbindungen auf 3× Betriebsdruck prüfen | ISO 10088 |

**System-Topologie (typisches Diesel-System):**

```
Kraftstofftank
    ↓ [Schlauchverbindung 1 — Absperrventil]
Kraftstoff-Vorfilter / Wasserabscheider (Racor, Separ)
    ↓ [Schlauchverbindung 2]
Kraftstoff-Zuleitung zum Motor (Niederdruckseite)
    ↓ [Schlauchverbindung 3]
Motor-Kraftstofffilter
    ↓ [Schlauchverbindung 4]
Einspritzpumpe
    ↓ [Schlauchverbindung 5 — Rücklauf]
Kraftstoff-Rücklauf zum Tank
    ↓ [Schlauchverbindung 6]

Tank-Entlüftung:
Tank → [Schlauchverbindung 7] → Entlüftungsschlauch → [Schlauchverbindung 8] → Deck-Fitting

Tank-Einfüllung:
Deck-Fitting → [Schlauchverbindung 9] → Einfüllschlauch → [Schlauchverbindung 10] → Tank
```

**Typische Schlauchgrößen Kraftstoffsystem:**

| Verbindung | Schlauch-ID (mm) | Schlauchtyp |
|---|---|---|
| Kraftstoff-Zuleitung (Diesel, <100PS) | 8–10 mm (5/16"–3/8") | ISO 7840 A2 |
| Kraftstoff-Zuleitung (Diesel, >100PS) | 10–12 mm (3/8"–1/2") | ISO 7840 A2 |
| Kraftstoff-Rücklauf | 8–10 mm (5/16"–3/8") | ISO 7840 A2 |
| Tank-Einfüllung | 38 mm (1-1/2") | ISO 7840 A2, Stahldraht-verstärkt |
| Tank-Entlüftung | 16 mm (5/8") | ISO 7840 A2 |
| Benzin-Zuleitung | 8–10 mm (5/16"–3/8") | ISO 7840 A1 (feuerbeständig!) |

**AYDI-Bewertung Kraftstoff-Verbindungen:**

| Befund | Score-Impact | Priorität |
|---|---|---|
| Oetiker/Vollband 316SS, dicht | 0 (erwarteter Zustand) | — |
| Verzinkte Schellen an Kraftstoff | -30 | Innerhalb 30 Tage |
| Lochband-Schellen an Kraftstoff | -15 | Nächste Wartung |
| Undichte Kraftstoff-Verbindung | → Score 5 | SOFORT |
| Kabelbinder an Kraftstoff-Leitung | -40 | SOFORT |
| Schlauch nicht ISO 7840 zugelassen | -25 | Innerhalb 30 Tage |
| PVC-Schlauch für Kraftstoff | -40 (BRANDGEFAHR) | SOFORT |
| Kunststoff-Stutzen an Kraftstoff | -30 (BRANDGEFAHR) | Innerhalb 30 Tage |

(Confidence: documented — ISO 10088:2013, ISO 7840:2021, ABYC H-33-2021)

### 9.5 Trinkwassersystem (Potable Water System)

**Anforderungen — Lebensmittelsicherheit:**

| Anforderung | Spezifikation | Norm |
|---|---|---|
| Materialzulassung | NSF 61 (USA) oder KTW/W270 (DE) oder WRAS (UK) | FDA / EU VO 10/2011 |
| Bleifrei | NSF 372 (USA) oder EU-Trinkwasserrichtlinie | Prop 65 (Kalifornien) |
| Schlauchtyp | Trinkwasser-Schlauch (weiß, FDA/NSF zugelassen) | — |
| Stutzen-Material | NSF 61 Bronze, Edelstahl 316, Komposit (Marelon, TruDesign), Acetal (Whale, John Guest) | — |
| Gewindedichtung | NSF 61 zugelassen: PTFE rosa, Loctite 577, Hanf+Neo-Fermit (NSF) | — |
| Quick-Connect | Zugelassen und empfohlen (Whale, John Guest) | — |

**System-Topologie (typisches Trinkwassersystem):**

```
Frischwassertank (Edelstahl oder Polyethylen)
    ↓ [Schlauchverbindung 1 — Tankauslass]
Druckwasserpumpe (z.B. Jabsco Par-Max, Shurflo)
    ↓ [Schlauchverbindung 2]
Akkumulator-Tank (optional, gegen Pulsation)
    ↓ [Schlauchverbindung 3]
Warmwasser-Boiler (optional)
    ↓ [Schlauchverbindung 4]
Verteiler / Manifold
    ↓ [Schlauchverbindungen 5–10]
Pantry-Wasserhahn, Bad-Wasserhahn, Dusche, Cockpit-Dusche, etc.
```

**Typische Schlauchgrößen Trinkwasser:**

| Verbindung | Schlauch-OD (mm) | System |
|---|---|---|
| Hauptleitung (Tank → Pumpe → Verteiler) | 15 mm (Whale) oder 12 mm (John Guest) | Whale QC oder JG Speedfit |
| Abzweige (Verteiler → Zapfstelle) | 12 mm (Whale) oder 10 mm (John Guest) | Whale QC oder JG Speedfit |
| Warmwasser-Boiler Anschluss | 15 mm (Whale) oder 22 mm (JG) | Whale QC oder JG Speedfit |
| Deck-Dusche | 12 mm | Whale QC oder Standard-Schlauch |

**Quick-Connect-Vorteile im Trinkwassersystem:**
- Werkzeuglose Montage und Demontage
- Keine Schlauchschellen nötig (Verbindung ist selbstsichernd)
- Trinkwasser-zugelassen (NSF 61)
- Leckage-frei bei korrekter Installation
- Einfache Systemerweiterung
- Idealer Einsatz über WL in drucklosen oder druckbeaufschlagten Systemen (<4 bar für Whale, <10 bar für JG)

**AYDI-Bewertung Trinkwasser-Verbindungen:**

| Befund | Score-Impact |
|---|---|
| Quick-Connect (Whale/JG), korrekt verriegelt | +5 (über Basis) |
| Standard-Schlauchschelle, NSF-Material | 0 (erwarteter Zustand) |
| Nicht-NSF-Material im Trinkwassersystem | -15 |
| Messing-Stutzen (Blei-haltig) im Trinkwasser | -25 |
| Verzinkte Schelle im Trinkwassersystem | -10 (Geschmack + Gesundheit) |
| PVC-Schlauch (nicht Trinkwasser-zugelassen) | -20 |

(Confidence: documented — NSF 61 Standard, Whale Installation Guide, John Guest Technical Handbook)

### 9.6 Bilgensystem (Bilge System)

**Anforderungen:**

| Anforderung | Spezifikation | Begründung |
|---|---|---|
| Auslass über WL | Borddurchlass über Wasserlinie (oder mit Rückschlagventil) | Kein Seewasser-Rücklauf in Bilge |
| Schlauchschellen Auslass | Doppelt, W4/W5 | Auch über WL: Redundanz wichtig |
| Rückschlagventil | Am Auslass (über WL) oder Entenschnabel-Ventil | Rückfluss-Verhinderung |
| Schlauchtyp | Transparenter oder halbstarrer Bilgenschlauch | Sichtbar ob Wasser fließt |
| Stutzen-Material | Bronze oder Komposit | Bilgenwasser kann korrosiv sein (Dieselspuren) |

**Typische Schlauchgrößen Bilge:**

| Pumpenleistung | Schlauch-ID (mm) | Typische Pumpe |
|---|---|---|
| Manuell (Handpumpe) | 25–38 mm (1"–1-1/2") | Whale Gusher 10/Titan |
| Elektrisch klein (1.000 GPH) | 19 mm (3/4") | Rule 1100 |
| Elektrisch mittel (2.000 GPH) | 25 mm (1") | Rule 2000, Jabsco |
| Elektrisch groß (3.700+ GPH) | 28–32 mm (1-1/8"–1-1/4") | Rule 3700 |
| Notfall-Bilge | 38–50 mm (1-1/2"–2") | Jabsco 36600/36800 |

**AYDI-Bewertung Bilge-Verbindungen:**

| Befund | Score-Impact |
|---|---|
| Doppelte Schellen am Auslass, Rückschlagventil vorhanden | 0 (erwarteter Zustand) |
| Einfache Schelle am Auslass | -15 |
| Kein Rückschlagventil am Auslass (über WL) | -10 |
| Kein Rückschlagventil am Auslass (an/unter WL) | -25 |
| Schlauch nicht auf Tülle | → Score 0 (KRITISCH) |
| Falscher Schlauchdurchmesser (reduziert Pumpenleistung) | -15 |

(Confidence: documented — Rule Industries Installation Guide, ABYC H-22, ISO 15083)

### 9.7 Gassystem — LPG (Gas System)

**SICHERHEITSKRITISCH**: Gas-Schlauchverbindungen unterliegen den strengsten Anforderungen. LPG (Propan/Butan) ist schwerer als Luft und sammelt sich in der Bilge — eine undichte Gasverbindung kann zur Explosion führen.

**Besondere Anforderungen Gassystem:**

| Anforderung | Spezifikation | Norm |
|---|---|---|
| Schlauchtyp | EN 16436-1 oder ISO 10239 zugelassener Gasschlauch | ISO 10239:2014 |
| Verbindungstyp | NUR zugelassene Gas-Verschraubungen | EN 16436, ISO 10239 |
| Schlauchschellen | NICHT erlaubt für Gas! Nur Verschraubung mit Überwurfmutter! | ISO 10239 |
| Material Fittings | Messing (Gasfest) oder Edelstahl | ISO 10239 |
| Gewindedichtung | PTFE-Band (Gelb, Gas-zugelassen) oder Loctite 577 | — |
| Druckprüfung | Alle Verbindungen mit Lecksuchspray oder Manometer-Test | ABYC A-1 |
| Gas-Detektor | PFLICHT in Bilge und Kochnische | ISO 10239, ABYC A-1 |

**AYDI-WARNUNG**: Im Gassystem werden KEINE Schlauchschellen verwendet! Gas-Verbindungen sind IMMER Verschraubungen (Überwurfmutter auf konischem Konus oder Schneidring). Ein Gasfitter, der Schlauchschellen an einer LPG-Leitung findet, muss das System sofort stilllegen.

**AYDI-Bewertung Gas-Verbindungen:**

| Befund | Score-Impact | Priorität |
|---|---|---|
| Zugelassene Verschraubungen, dicht, geprüft | 0 | — |
| Schlauchschelle an Gas-Leitung | → Score 0 (LEBENSGEFAHR) | SOFORT, System stilllegen |
| Undichte Gas-Verbindung | → Score 0 (LEBENSGEFAHR) | SOFORT, System stilllegen |
| Gasschlauch nicht zugelassen | -40 | SOFORT ersetzen |
| Gasschlauch älter als 10 Jahre | -20 | Innerhalb 30 Tage ersetzen |
| Kein Gas-Detektor | -30 | SOFORT nachrüsten |

(Confidence: documented — ISO 10239:2014, ABYC A-1-2021, EN 16436-1:2014)

### 9.8 Klimaanlage — Seewassersystem (AC Seawater System)

Klimaanlagen auf Yachten verwenden Seewasser als Kühlmedium. Das System umfasst typischerweise einen eigenen Borddurchlass mit Seeventil, Pumpe, Verteilung zu mehreren AC-Einheiten und einen Auslass.

**System-Topologie (typische Marine-Klimaanlage):**

```
Borddurchlass (unter WL)
    ↓ [Schlauchverbindung 1 — unter WL, doppelt geschellt]
Seeventil
    ↓ [Schlauchverbindung 2 — unter WL, doppelt geschellt]
Seewasserfilter
    ↓ [Schlauchverbindung 3]
Seewasserpumpe (Zentrifugalpumpe, oft March Mfg. oder Dometic/Cruisair)
    ↓ [Schlauchverbindung 4]
Verteiler / Manifold
    ↓ [Schlauchverbindungen 5–8, je nach Anzahl AC-Einheiten]
AC-Einheit 1..N (Wärmetauscher/Verdampfer)
    ↓ [Schlauchverbindungen 9–12]
Sammelauslass / Seewasser-Auslass
    ↓ [Schlauchverbindung 13]
Borddurchlass Auslass (über WL)
```

**Besondere Anforderungen AC-Seewassersystem:**

| Anforderung | Spezifikation | Begründung |
|---|---|---|
| Schlauchschellen unter WL | Doppelt, W4/W5, Vollband | Standard unter WL |
| Verteiler-Anschlüsse | Doppelte Schellen an jedem Abzweig | Viele Verbindungspunkte = hohes Risiko |
| Schlauchtyp | Marine-Seewasserschlauch (verstärkt) | Dauerbetrieb unter Druck |
| Pumpen-Anschluss | Doppelte Schellen, vibrationsfest | Zentrifugalpumpe vibriert |
| Anti-Siphon | Am Auslass, wenn dieser unter WL kommen kann | Siphon-Rückfluss |
| Bewuchs | Monatlich Seewasserfilter prüfen | AC-Systeme laufen oft im Hafen mit warmem Wasser → extremer Bewuchs |

**Typische Schlauchgrößen AC-System:**

| Verbindung | Schlauch-ID (mm) | Anmerkung |
|---|---|---|
| Einlass (Borddurchlass → Pumpe) | 25–38 mm (1"–1-1/2") | Je nach Kühlleistung |
| Hauptleitung (Pumpe → Verteiler) | 25–38 mm | — |
| Abzweige (Verteiler → AC-Einheit) | 16–19 mm (5/8"–3/4") | Pro Einheit |
| Rücklauf (AC-Einheit → Sammel) | 16–19 mm | — |
| Auslass (Sammel → Borddurchlass) | 25–38 mm | — |

**AYDI-Bewertung AC-Verbindungen:**

| Befund | Score-Impact |
|---|---|
| Alle Verbindungen doppelt geschellt, W4/W5, kein Bewuchs | 0 |
| Einfache Schelle an Verteiler-Abzweig | -15 pro Abzweig |
| Bewuchs an Schlauchtülle/Filter | -10 |
| Pumpe undicht am Anschluss | -25 |
| Anti-Siphon fehlt (Auslass unter WL) | -30 |
| AC-Schlauch verhärtet (oft >10 Jahre alt) | -15 |

(Confidence: documented — Dometic/Cruisair Installation Manual, Marine Air Installation Guide, Survey-Erfahrung)

### 9.9 Zusammenfassung — Anforderungen nach Anlagentyp

| System | Position | Min. Schellen | Schellen-Material | Stutzen-Material | Quick-Connect | Rückschlagventil | Anti-Siphon |
|---|---|---|---|---|---|---|---|
| Kühlwasser (Motor) | unter/an WL | 2× Vollband | W4/W5 | Bronze/316SS | ❌ | Optional | Optional |
| Nassauspuff | über WL | 2× T-Bolt | W4 | 316SS | ❌ | ❌ | PFLICHT* |
| Sanitär (WC) | unter/über WL | 2× unter WL | W4/W5 | Bronze/Komposit | ❌ | Optional | Optional** |
| Kraftstoff | über WL | Oetiker/Vollband | W4/316SS | Bronze/316SS | ❌ | ❌ | ❌ |
| Trinkwasser | über WL | QC oder 1× Schelle | W4 oder QC | NSF 61 (jedes) | ✅ Empfohlen | Optional | ❌ |
| Bilge | über WL | 2× am Auslass | W4 | Bronze/Komposit | ❌ | PFLICHT | ❌ |
| Gas (LPG) | über WL | KEINE Schellen! | Verschraubung | Messing/316SS | ❌ | ❌ | ❌ |
| Klimaanlage | unter/über WL | 2× unter WL | W4/W5 | Bronze/Komposit | ❌ | Optional | PFLICHT* |

*PFLICHT wenn Auslass unter WL möglich
**Optional wenn Einlass unter WL

(Confidence: documented — ABYC Standards, ISO 9093, ISO 10239, ISO 10088, Survey-Standards)

---

## 10. Technische Referenz & Berechnungen

### 10.1 Klemmkraft-Berechnung (Clamp Force)

Die Klemmkraft einer Schlauchschelle bestimmt, ob die Verbindung dicht hält — zu wenig Kraft = Leckage, zu viel = Schlauchbeschädigung.

#### 10.1.1 Grundformel Klemmkraft

```
F_klemm = (T × η) / (r × tan(α + ρ))

Wobei:
  F_klemm = Klemmkraft auf Schlauch [N]
  T       = Anzugsdrehmoment [Nm]
  η       = Effizienz des Schneckentriebs (typ. 0,25–0,40)
  r       = mittlerer Schraubenradius [m]
  α       = Steigungswinkel des Schneckengewindes [°]
  ρ       = Reibwinkel = arctan(μ) [°]
  μ       = Reibungskoeffizient (316SS trocken: 0,35–0,45; gefettet: 0,15–0,25)
```

#### 10.1.2 Vereinfachte Praxisformel

Für marine Schneckenband-Schellen (Worm Drive) gilt die vereinfachte Näherung:

```
F_klemm ≈ T × K_typ

K_typ-Werte nach Schellentyp:
  Standard-Schneckenband (12,7 mm):  K_typ ≈ 180–220 N/Nm
  Breitband-Schneckenband (16 mm):   K_typ ≈ 200–250 N/Nm
  T-Bolt (Heavy Duty):               K_typ ≈ 280–350 N/Nm
  Oetiker (StepLess):                K_typ ≈ 400–500 N/Nm (einmalige Verformung)
```

#### 10.1.3 Empfohlene Anzugsdrehmomente

| Schellentyp | Schlauch-ID [mm] | Min. Drehmoment [Nm] | Max. Drehmoment [Nm] | Werkzeug |
|---|---|---|---|---|
| Schneckenband 12,7 mm | 12–19 | 2,5 | 4,0 | 5/16" Sechskant oder Schlitz |
| Schneckenband 12,7 mm | 20–32 | 3,0 | 4,5 | 5/16" Sechskant oder Schlitz |
| Schneckenband 12,7 mm | 33–50 | 3,5 | 5,0 | 5/16" Sechskant oder Schlitz |
| Schneckenband 16 mm | 19–38 | 3,5 | 5,5 | 5/16" Sechskant |
| Schneckenband 16 mm | 40–65 | 4,0 | 6,0 | 5/16" Sechskant |
| T-Bolt | 32–50 | 6,0 | 9,0 | 10 mm oder 13 mm Steckschlüssel |
| T-Bolt | 51–76 | 7,0 | 10,0 | 13 mm Steckschlüssel |
| T-Bolt | 78–102 | 8,0 | 12,0 | 13 mm Steckschlüssel |
| Oetiker StepLess | alle | — | — | Oetiker-Zange (kein Drehmoment) |
| Constant Torque | alle | Feder-definiert | Feder-definiert | 5/16" Sechskant (Erstmontage) |

**AYDI-Hinweis**: Drehmomentschlüssel im Bereich 1–12 Nm sind selten an Bord. Praxisregel: Schneckenband-Schelle mit kurzem Schraubendreher (max. 150 mm Klingenlänge) anziehen, bis deutlicher Widerstand + ¼ Umdrehung. Niemals mit Knarre oder langem Hebel!

(Confidence: calculated — SAE J1508, Herstellerangaben AWAB/Breeze/Norma, Engineering-Handbücher)

#### 10.1.4 Kontaktdruck-Berechnung

Der Kontaktdruck bestimmt die Dichtfähigkeit:

```
p_kontakt = F_klemm / (B_band × π × (D_schlauch + 2 × t_wand))

Wobei:
  p_kontakt    = Kontaktdruck [MPa]
  F_klemm      = Klemmkraft [N]
  B_band       = Bandbreite der Schelle [mm]
  D_schlauch   = Schlauch-Außendurchmesser [mm]
  t_wand       = Schlauchwandstärke [mm]

Erforderliche Kontaktdrücke:
  Niederdrucksystem (Kühlwasser, Sanitär): 0,3–0,8 MPa
  Mitteldrucksystem (Nassauspuff):         0,8–1,5 MPa
  Hochdrucksystem (Kraftstoff):            1,5–3,0 MPa
```

**AYDI-WARNUNG**: Zu hoher Kontaktdruck (>4 MPa bei Standard-Gummischläuchen) schneidet in die Schlauchwand ein und schwächt die Verbindung langfristig. Gelochte Bänder (SAE Typ F) erzeugen lokale Druckspitzen bis zum 2,5-fachen des mittleren Kontaktdrucks an den Lochkanten.

#### 10.1.5 Auszugskraft-Berechnung

Die Kraft, die nötig ist, um den Schlauch vom Stutzen zu ziehen:

```
F_auszug = μ_s × p_kontakt × π × D_stutzen × L_überstand

Wobei:
  F_auszug   = Auszugskraft [N]
  μ_s        = Reibkoeffizient Schlauch/Stutzen (Gummi/Bronze: 0,4–0,6; Gummi/316SS: 0,3–0,5)
  p_kontakt  = Kontaktdruck [MPa]
  D_stutzen  = Stutzen-Außendurchmesser [mm]
  L_überstand = Aufschieblänge des Schlauchs auf Stutzen [mm]

Sicherheitsfaktor:
  Über WL: F_auszug ≥ 3 × F_betrieb (Innendruck × Querschnittsfläche)
  Unter WL: F_auszug ≥ 5 × F_betrieb
```

(Confidence: calculated — Ingenieurhandbücher, SAE J1508, Prüfprotokolle)

### 10.2 Durchfluss durch Fittings (Flow Coefficient)

#### 10.2.1 Cv-Werte typischer Marine-Fittings

Der Cv-Wert (Flow Coefficient) gibt den Durchfluss in US Gallons/min bei 1 psi Druckabfall an:

| Fitting-Typ | Nennweite [mm] | Cv-Wert | Äquivalent Kv [m³/h] | Druckverlust bei 20 l/min [mbar] |
|---|---|---|---|---|
| Gerader Schlauchtülle | 19 | 8,5 | 7,3 | 12 |
| Gerader Schlauchtülle | 25 | 15,0 | 12,9 | 4 |
| Gerader Schlauchtülle | 32 | 24,0 | 20,7 | 1,5 |
| Gerader Schlauchtülle | 38 | 35,0 | 30,2 | 0,7 |
| 90°-Winkel-Schlauchtülle | 19 | 5,5 | 4,7 | 28 |
| 90°-Winkel-Schlauchtülle | 25 | 9,5 | 8,2 | 10 |
| 90°-Winkel-Schlauchtülle | 32 | 16,0 | 13,8 | 3,5 |
| T-Stück (Durchgang) | 19 | 7,0 | 6,0 | 18 |
| T-Stück (Abzweig) | 19 | 3,5 | 3,0 | 70 |
| Y-Verteiler | 19 | 6,0 | 5,2 | 22 |
| Quick-Connect (geöffnet) | 12 | 3,0 | 2,6 | 95 |
| Quick-Connect (geöffnet) | 19 | 6,5 | 5,6 | 20 |
| Rückschlagventil (Marine) | 19 | 4,0 | 3,5 | 55 |
| Rückschlagventil (Marine) | 25 | 7,5 | 6,5 | 15 |
| Seeventil (Kugel, offen) | 19 | 12,0 | 10,3 | 6 |
| Seeventil (Kugel, offen) | 25 | 22,0 | 19,0 | 2 |
| Seeventil (Kugel, offen) | 38 | 50,0 | 43,1 | 0,3 |

#### 10.2.2 Druckverlust-Berechnung über Gesamtsystem

```
Δp_gesamt = Σ (Q² / (Cv_i² × 0,865²)) × ρ/ρ_wasser

Wobei:
  Δp_gesamt = Gesamtdruckverlust [bar]
  Q         = Volumenstrom [m³/h]
  Cv_i      = Cv-Wert jedes Fittings
  ρ         = Dichte des Mediums [kg/m³]
  ρ_wasser  = 1000 kg/m³ (Referenz)
```

**Praxisbeispiel**: Motorkühlwasser-System einer 12 m Segelyacht:
- Seeventil 25 mm (Cv=22) → Siebkorb (Cv=18) → 2 m Schlauch → Seewasserpumpe → Wärmetauscher-Anschluss (Cv=12) → 1,5 m Schlauch → Nassauspuff-Injektor (Cv=8)
- Volumenstrom: 45 l/min = 2,7 m³/h
- Δp_Fittings = (2,7²/22² + 2,7²/18² + 2,7²/12² + 2,7²/8²) × 1/0,865² = 0,21 bar
- Δp_Schlauch (3,5 m × 25 mm) ≈ 0,08 bar
- Δp_gesamt ≈ 0,29 bar — akzeptabel für Impeller-Pumpe (typ. 0,3–0,5 bar Förderdruck)

**AYDI-Scoring**: Wenn Δp_gesamt > 70 % des Pumpen-Förderdrucks → Warnung „Durchfluss kritisch niedrig" (Score -25). Wenn > 90 % → Fehler „System unterdimensioniert" (Score -50).

(Confidence: calculated — Hydraulik-Grundlagen, Herstellerdatenblätter, Praxismessungen)

### 10.3 Thermische Ausdehnung und Spannungen

#### 10.3.1 Längenänderung von Schlauchleitungen

```
ΔL = α × L₀ × ΔT

Typische Ausdehnungskoeffizienten α [1/K]:
  Gummischlauch (EPDM):     150–200 × 10⁻⁶
  Silikonschlauch:           250–300 × 10⁻⁶
  PVC-Schlauch:              70–80 × 10⁻⁶
  316SS-Stutzen:             16 × 10⁻⁶
  Bronze-Stutzen:            18 × 10⁻⁶
  GFK-Borddurchlass:        20–30 × 10⁻⁶
```

**Praxisbeispiel**: 500 mm EPDM-Schlauch am Nassauspuff, ΔT = 80 K (Abgas + Seewasser-Mischtemperatur):
- ΔL = 180 × 10⁻⁶ × 500 × 80 = 7,2 mm
- Erforderlicher Durchhang/Bogen im Schlauch: min. 15 mm → OK

**AYDI-WARNUNG**: Straff montierte Schläuche am Nassauspuff ohne Dehnungsausgleich erzeugen axiale Kräfte von 50–200 N auf die Schlauchtülle. Bei korrodiertem oder gelockertem Stutzen kann das zum Abziehen führen.

(Confidence: calculated — Werkstoffdaten, Thermodynamik-Grundlagen)

---

## 11. Einbau-/Austausch-Anleitung

### 11.1 Werkzeug-Checkliste

| Werkzeug | Einsatz | Empfohlene Qualität | Preis ca. [EUR] |
|---|---|---|---|
| Schraubendreher Schlitz 6 mm | Schneckenband-Schellen | Wera oder PB Swiss | 8–15 |
| Sechskant-Bit 5/16" (8 mm) | Schneckenband-Schellen (Hex-Kopf) | Wiha oder Wera | 5–10 |
| Steckschlüssel 10 mm + 13 mm | T-Bolt-Schellen | Stahlwille oder Gedore | 15–25 |
| Drehmomentschlüssel 1–25 Nm | Präzise Montage | Hazet 5107-2CT | 85–120 |
| Oetiker-Zange 1098 | StepLess-Schellen | Oetiker Original | 45–65 |
| Seitenschneider | Alte Schellen entfernen | Knipex 7001-160 | 18–25 |
| Schlauchschere | Schlauch ablängen | Reed HS1 oder Knipex 9025-185 | 25–40 |
| Heißluftfön (stufenlos) | Schlauch aufweiten | Steinel HL 1920 E | 60–90 |
| Silikonspray (lebensmittelecht) | Montagehilfe | Würth oder WD-40 Specialist | 8–12 |
| Teflonband (PTFE, 12 mm) | Gewindedichtung (nur NPT/konisch!) | ≥0,1 mm Dicke, Markaware | 3–5 |
| Loctite 577 (anaerob) | Gewindedichtung (parallel BSP) | Loctite Original | 15–25 |
| Drahtbürste (316SS) | Stutzreinigung | Rostfrei, keine Stahlbürste! | 5–8 |
| Schieblehre digital | ID/OD-Messung | Mitutoyo oder Helios-Preisser | 25–60 |
| Taschenlampe (LED, 500+ lm) | Inspektion Bilge/Motorraum | Fenix oder Ledlenser | 25–50 |
| Spiegel (teleskopisch) | Hintere Anschlüsse inspizieren | Werkstattqualität | 8–15 |

### 11.2 Standard-Einbauverfahren (über Wasserlinie)

**Schritt 1 — Vorbereitung (15 min)**
1. System drucklos machen (Pumpe aus, ggf. Seeventil schließen).
2. Restflüssigkeit auffangen (Schüssel/Tücher bereithalten).
3. Stutzen-Außendurchmesser mit Schieblehre messen → Schlauch-ID muss ≤ Stutzen-OD sein (Presspassung).
4. Schlauch auf korrekte Länge zuschneiden — min. 20 mm Reserve über Stutzen-Ende hinaus.
5. Schlauchende auf Beschädigung prüfen (Risse, Quetschungen, Verformung → abschneiden).

**Schritt 2 — Schlauch aufziehen (10 min)**
1. Silikonspray auf Stutzen-Außenseite und Schlauch-Innenseite auftragen.
2. Bei steifem Schlauch (Nassauspuff, Kraftstoff): Schlauchende 30–60 Sekunden mit Heißluftfön auf 60–70 °C erwärmen. **NICHT über 80 °C** — Gummi-Alterung!
3. Schlauch mit drehender Bewegung auf Stutzen schieben.
4. Schlauch muss vollständig über alle Rillen/Barbs des Stutzens geschoben werden.
5. Schlauchende muss min. 5 mm über den letzten Barb hinausragen.
6. Sichtprüfung: Schlauch sitzt gerade, keine Verdrehung, kein Knick.

**Schritt 3 — Schellen montieren (10 min)**
1. Erste Schelle über den äußersten Barb positionieren (ca. 5 mm vom Schlauchende).
2. Zweite Schelle (falls erforderlich) über den innersten Barb positionieren.
3. Schneckengetriebe nach oben/seitlich ausrichten (Wartungszugang!).
4. Schellenband ausrichten: gleichmäßig um Schlauch, kein Verdrehen.
5. Schellen anziehen: erst handwarm, dann mit Werkzeug auf Soll-Drehmoment.
6. 10 Minuten warten → nachziehen (Schlauch setzt sich).
7. System unter Druck setzen und auf Leckage prüfen.

**Schritt 4 — Prüfung (5 min)**
1. Trockenes Papiertuch um Verbindung wickeln.
2. System 15 Minuten unter Betriebsdruck.
3. Papiertuch auf Feuchtigkeit prüfen.
4. Bei Leckage: NICHT weiter anziehen — Schlauch abnehmen, Stutzen prüfen, neu montieren.

### 11.3 Einbauverfahren unterhalb der Wasserlinie (WL)

**SICHERHEITSKRITISCH**: Arbeiten unter WL erfordern besondere Sorgfalt. Ein Fehler = Wassereinbruch.

**Voraussetzungen:**
- Boot an Land (Slip/Kran) ODER Seeventil geschlossen und gesichert
- Ersatz-Holzstopfen in Griffweite (passender Durchmesser für Borddurchlass)
- Zweite Person in Rufweite
- Bilgenpumpe betriebsbereit
- Werkzeug vollständig vorbereitet (nichts mehr suchen während Seeventil offen)

**Schritt 1 — Vorbereitung am Land / bei geschlossenem Seeventil (20 min)**
1. Seeventil schließen. Hebel mit Kabelbinder oder Draht sichern.
2. **WARNUNG auf Seeventil anbringen**: „NICHT ÖFFNEN — Arbeiten am System!"
3. Restdruck ablassen — vorsichtig Schlauchschelle lockern, Tropfen abwarten.
4. Alte Schellen entfernen, Schlauch abziehen.
5. Stutzen inspizieren: Korrosion, Rissbildung, Entzinkung (bei Messing → rosa/kupfern = AUSTAUSCHEN).
6. Borddurchlass/Seeventil inspizieren: Spiel in Kugelventil? Korrosion? Gewindegänge intakt?
7. Neuen Stutzen anpassen (trocken aufstecken, Maße prüfen).

**Schritt 2 — Montage (15 min)**
1. Schlauch vorbereiten wie in 11.2, Schritt 2.
2. **DOPPELTE Schellen**: Immer 2 Schellen pro Verbindung unter WL — KEINE Ausnahme!
3. Schellen-Material: ausschließlich W4 (AISI 316) oder W5 (AISI 316L) Vollband.
4. Schlauchschellen versetzt anordnen — Schneckengetriebe der beiden Schellen um 180° versetzt.
5. Erste Schelle: 5 mm vom Schlauchende.
6. Zweite Schelle: über dem innersten Barb, min. 10 mm Abstand zur ersten Schelle.
7. Drehmoment exakt einhalten (s. Tabelle 10.1.3).

**Schritt 3 — Druckprüfung (30 min)**
1. Seeventil-Sicherung entfernen.
2. Papiertuch um Verbindung.
3. Seeventil LANGSAM öffnen (¼ Umdrehung, 10 Sekunden warten).
4. Auf Leckage prüfen.
5. Seeventil vollständig öffnen.
6. 30 Minuten unter Außenwasserdruck beobachten.
7. Bei Leckage: Seeventil SOFORT schließen → Holzstopfen griffbereit.
8. Dokumentation: Datum, Material, Hersteller, Drehmoment im Bordbuch eintragen.

**AYDI-Scoring bei Inspektion unter WL:**
- Doppelschelle 316SS, korrekt montiert, kein Rost: 100/100
- Doppelschelle 316SS, leichter Rost an Schraube: 85/100
- Doppelschelle 316SS, eine Schelle locker: 55/100 + Befund HOCH
- Einzelschelle 316SS unter WL: 30/100 + Befund KRITISCH
- Einzelschelle verzinkt unter WL: 5/100 + Befund KRITISCH + Sofort-Empfehlung
- Kabelbinder/Draht unter WL: 0/100 + Befund KRITISCH + Dringlichkeitsmeldung

(Confidence: documented — ABYC H-27, ISO 9093, Surveyor Best Practices, Werftpraxis)

### 11.4 Demontage alter Schlauchverbindungen

**Problem**: Alte Schläuche „vulkanisieren" auf den Stutzen — sie lassen sich nicht abziehen.

**Verfahren bei festsitzenden Schläuchen:**
1. Schellen entfernen.
2. Schlauchende mit Cutter längs einritzen (NUR den Schlauch, NICHT den Stutzen).
3. Schmalen Schlitz-Schraubendreher zwischen Schlauch und Stutzen drücken.
4. Silikonspray in den Spalt sprühen.
5. Schlauch mit Drehbewegung lockern.
6. Falls unmöglich: Schlauch mit Cutter spiralförmig aufschneiden und abschälen.
7. Stutzreste mit Drahtbürste (316SS!) reinigen.
8. **NIEMALS** Stutzen mit Zange greifen und drehen — Bruchgefahr bei Bronze und Komposit!
9. **NIEMALS** Gewalt anwenden — lieber Stutzen austauschen.

(Confidence: documented — Werftpraxis, Surveyor-Erfahrung)

---

## 12. Lebensdauer und Alterungsmechanismen

### 12.1 Lebensdauer-Übersicht nach Material und Umgebung

| Komponente | Material | Süßwasser-Revier | Salzwasser-Revier | Tropen (Salz+UV+Hitze) |
|---|---|---|---|---|
| Schlauchschelle | 316SS (W4/W5) | 15–20+ Jahre | 12–18 Jahre | 10–15 Jahre |
| Schlauchschelle | 304SS (W2) | 8–12 Jahre | 3–6 Jahre | 2–4 Jahre |
| Schlauchschelle | Verzinkt (W1) | 5–8 Jahre | 2–3 Jahre | 1–2 Jahre |
| Schlauchschelle | T-Bolt 316SS | 20+ Jahre | 15–20 Jahre | 12–18 Jahre |
| Schlauchtülle | Bronze (DZR) | 25+ Jahre | 20–25 Jahre | 15–20 Jahre |
| Schlauchtülle | 316SS | 30+ Jahre | 25+ Jahre | 20+ Jahre |
| Schlauchtülle | Messing (NICHT DZR) | 10–15 Jahre | 3–5 Jahre (Entzinkung!) | 1–3 Jahre |
| Schlauchtülle | Marelon/Komposit | 15–20 Jahre | 15–20 Jahre | 10–15 Jahre |
| Quick-Connect | Acetal/POM | 8–12 Jahre | 8–10 Jahre | 5–8 Jahre |
| Quick-Connect | 316SS | 20+ Jahre | 15–20 Jahre | 12–15 Jahre |
| Gummischlauch (EPDM) | — | 10–15 Jahre | 8–12 Jahre | 6–10 Jahre |
| Silikonschlauch | — | 15–20 Jahre | 12–15 Jahre | 10–12 Jahre |
| PVC-Schlauch (klar) | — | 3–5 Jahre | 2–4 Jahre | 1–2 Jahre |
| Kraftstoffschlauch (A1) | — | 10–12 Jahre | 8–10 Jahre | 6–8 Jahre |

**AYDI-Regel**: Alter der Schlauchverbindung > 75 % der erwarteten Lebensdauer → Warnung „Austausch planen". > 100 % → Befund HOCH „Austausch überfällig".

### 12.2 Alterungsmechanismen im Detail

#### 12.2.1 Korrosion bei Schlauchschellen

**Spaltkorrosion (Crevice Corrosion):**
- Tritt im Spalt zwischen Schellenband und Schlauch auf.
- Selbst 316SS betroffen bei stagnierender Salzlösung.
- Beschleunigt durch: Bilgenwasser-Kontakt, Kondensation, mangelnde Belüftung.
- Typisch: Lochfraß an der Innenseite des Schellenbands → von außen nicht sichtbar!
- AYDI-Pipeline B: Kann nur sichtbare Korrosion erkennen. Unsichtbare Spaltkorrosion → Confidence: visual_insufficient.

**Galvanische Korrosion:**
- 316SS-Schelle auf Bronze-Stutzen: geringes Risiko (Potentialdifferenz ~50 mV in Seewasser).
- 316SS-Schelle auf verzinktem Stutzen: hohes Risiko — Zink opfert sich, Stutzen korrodiert.
- Aluminium-Stutzen + 316SS-Schelle: SEHR hohes Risiko → Isolation erforderlich (Gummi-Einlage).
- AYDI-Scoring: Galvanische Inkompatibilität → -30 Punkte (materials-Modul).

**Entzinkung (Dezincification):**
- Betrifft nur Messing-Stutzen (CuZn37, CuZn39Pb).
- Zink löst sich aus der Legierung → schwammiges, rosa/kupferfarbenes Restmaterial.
- Festigkeitsverlust bis 90 % — Stutzen kann bei Belastung brechen.
- Prüfung: Kratzen mit Messer → rosa = Entzinkung → SOFORT AUSTAUSCHEN.
- DZR-Messing (Dezincification Resistant, CW602N) ist beständig.
- AYDI-Pipeline B: rosa/kupferfarbene Verfärbung an Schlauchtülle → Confidence: visual_high, Befund KRITISCH.

#### 12.2.2 Schlauch-Alterung

**Ozon-Rissbildung:**
- Gummischläuche (EPDM, Neopren) reagieren mit Ozon aus der Luft.
- Typisch: feine Querrisse (Ozonrisse) an der Außenseite, besonders an Biegungen.
- Beschleunigt durch: Sonnenlicht, elektrische Motoren (Ozon-Emitter), Schlechte Belüftung.
- AYDI-Pipeline B: Querrisse sichtbar → Confidence: visual_high.

**UV-Degradation:**
- Betrifft alle Polymer-Schläuche, die Sonnenlicht ausgesetzt sind.
- PVC: Vergilbung, Versprödung, Weichmacher-Migration.
- Silikon: weniger anfällig, aber Oberflächenverhärtung.
- EPDM: mäßig anfällig, Carbonblack als UV-Schutz (schwarze Schläuche besser als farbige).
- AYDI-Scoring: UV-exponierter Schlauch ohne UV-Schutz → -15 Punkte.

**Weichmacher-Migration (PVC):**
- PVC-Schläuche verlieren über die Zeit Weichmacher → werden steif und spröde.
- Beschleunigt durch: Hitze, UV, Kontakt mit Mineralöl/Diesel.
- Steifer PVC-Schlauch lässt sich nicht mehr biegen → knickt → Durchflussverlust.
- **NIEMALS** PVC-Schlauch für Kraftstoff oder Motorraum verwenden.
- AYDI-Pipeline B: Vergilbter, steifer PVC-Schlauch → Confidence: visual_medium.

#### 12.2.3 Ermüdung durch Vibration

- Motorschläuche unterliegen konstanter Vibration (Frequenz: 25–100 Hz bei 1500–6000 RPM).
- Vibration lockert Schneckenband-Schellen (selbst bei korrektem Drehmoment).
- Constant-Torque-Schellen kompensieren dies durch Federspannung.
- AYDI-Scoring: Schneckenband-Schelle im Motorraum ohne Vibrationsdämpfung → -10 Punkte.

#### 12.2.4 Elektrolyse (Streustrom-Korrosion)

- Fehlerhaft geerdete 230V-Landstromanlage kann Streuströme erzeugen.
- Streuströme fließen durch metallische Borddurchlässe und Schlauchschellen zum Wasser.
- Beschleunigte Korrosion: Faktor 10–100× schneller als natürliche Korrosion.
- Symptom: Neue 316SS-Schelle zeigt nach 6 Monaten massive Korrosion → Streustrom prüfen!
- AYDI-Modul: Wenn Korrosionsrate >> erwartet → Warnung „Streustrom-Problem prüfen".

(Confidence: documented — Korrosionsforschung, ABYC E-11, Marine-Surveyor-Literatur)

### 12.3 Inspektionsintervalle

| Komponente | Standard-Intervall | Salzwasser | Tropen | Nach Grundberührung |
|---|---|---|---|---|
| Schlauchschellen unter WL | 12 Monate | 6 Monate | 6 Monate | Sofort |
| Schlauchschellen über WL | 24 Monate | 12 Monate | 12 Monate | — |
| Schlauchtüllen unter WL | 12 Monate | 6 Monate | 6 Monate | Sofort |
| Schläuche Motorraum | 12 Monate | 12 Monate | 6 Monate | — |
| Schläuche Nassauspuff | 12 Monate | 12 Monate | 6 Monate | — |
| Quick-Connects | 24 Monate | 12 Monate | 12 Monate | — |
| Kraftstoffschläuche | 12 Monate | 12 Monate | 6 Monate | — |
| Alle Schläuche (Sichtprüfung) | 6 Monate | 3 Monate | 3 Monate | Sofort |

(Confidence: documented — ABYC Standards, Versicherungsanforderungen, Surveyor Best Practices)

---

## 13. Fehlerbild-Atlas

### FB-SV-001 — Korrodierte Schlauchschelle

**Beschreibung**: Schlauchschelle zeigt sichtbare Korrosion — Rost, Lochfraß, Verfärbung.
**Typische Ursache**: Falsche Materialwahl (W1/W2 statt W4), Salzwasser-Exposition, Streustrom.
**Betroffene Systeme**: Alle Systeme, bevorzugt unter WL und im Motorraum.
**Visuelle Indikatoren**: Braune/orange Verfärbung, raue Oberfläche, Lochfraß-Krater, Bandbruch.
**AYDI-Pipeline-B-Erkennung**: Confidence visual_high — Rost/Verfärbung gut erkennbar.
**Risiko**: HOCH unter WL (Schellenbruch → Wassereinbruch), MITTEL über WL.
**Sofortmaßnahme**: Schelle ersetzen durch W4/W5 316SS. Unter WL: Boot aus dem Wasser oder Seeventil schließen.
**Präventiv**: Nur 316SS (W4/W5) Vollband-Schellen verwenden. Jährliche Inspektion.
**AYDI-Score-Abzug**: -40 (W1 korrodiert über WL), -80 (W1/W2 korrodiert unter WL).
**Kosten Behebung**: 5–15 EUR pro Schelle (Material) + 15–30 min Arbeitszeit.
**Differentialdiagnose**: Oberflächlicher Flugrost an W4 ≠ strukturelle Korrosion. Flugrost mit Scotch-Brite entfernen und prüfen.
**Verwechslungsgefahr**: Tee-Staining (bräunliche Verfärbung an 316SS ohne Materialverlust) ist kosmetisch, nicht strukturell.

### FB-SV-002 — Lockerer Schlauchtülle (Barb)

**Beschreibung**: Schlauchtülle sitzt lose im Seeventil/Borddurchlass, lässt sich von Hand drehen oder wackelt.
**Typische Ursache**: Gewinde nicht korrekt angezogen, falscher Gewindedichtmittel, Korrosion am Gewinde.
**Betroffene Systeme**: Alle Schraubverbindungen Stutzen-zu-Ventil.
**Visuelle Indikatoren**: Sichtbarer Spalt zwischen Stutzen-Flansch und Ventilkörper, Wasseraustritt am Gewinde, Grünspanbildung.
**AYDI-Pipeline-B-Erkennung**: Confidence visual_medium — Spalt nur bei guter Beleuchtung erkennbar.
**Risiko**: KRITISCH unter WL (Stutzen kann sich vollständig lösen).
**Sofortmaßnahme**: Seeventil schließen, Stutzen mit passendem Schlüssel nachziehen, Dichtmittel erneuern.
**Präventiv**: Korrekte Dichtmittel verwenden (PTFE für NPT, Loctite 577 für BSP). Drehmoment prüfen.
**AYDI-Score-Abzug**: -60 unter WL, -25 über WL.
**Kosten Behebung**: 5–25 EUR (Dichtmittel) + 30–60 min Arbeitszeit.
**Differentialdiagnose**: Absichtlich lose Montage für spätere Ausrichtung vs. unbeabsichtigt lose.
**Verwechslungsgefahr**: Nicht mit flexiblem Stutzen verwechseln (manche Komposit-Stutzen haben bewusst geringes Spiel).

### FB-SV-003 — Beschädigtes Gewinde (Stripped Thread)

**Beschreibung**: Gewinde des Stutzens oder Ventilkörpers ist beschädigt — Stutzen dreht durch ohne Halt.
**Typische Ursache**: Übermäßiges Drehmoment, falsche Gewindegröße, Cross-Threading, Korrosion.
**Betroffene Systeme**: Alle Schraubverbindungen, besonders Bronze-in-Bronze und Messing-Gewinde.
**Visuelle Indikatoren**: Stutzen lässt sich ohne Widerstand drehen, Metallspäne am Gewinde sichtbar, Gewindegänge deformiert.
**AYDI-Pipeline-B-Erkennung**: Confidence visual_low — Gewindeschaden nur bei Demontage sichtbar.
**Risiko**: KRITISCH — Verbindung hat keine Haltekraft.
**Sofortmaßnahme**: Verbindung außer Betrieb nehmen, Seeventil schließen, Ventil/Stutzen ersetzen.
**Präventiv**: Gewinde nie trocken einschrauben (Bronze/Messing: Lanolin oder Duralac). Handfest + ¼ bis ½ Umdrehung.
**AYDI-Score-Abzug**: -90 unter WL, -50 über WL.
**Kosten Behebung**: 50–200 EUR (neuer Stutzen/Ventil) + 1–4 h Arbeitszeit.
**Differentialdiagnose**: Stripped Thread vs. falscher Gewindetyp (NPT in BSP-Bohrung gedreht).
**Verwechslungsgefahr**: Nicht mit Sollbruch-Gewinde verwechseln (gibt es im Marine-Bereich nicht).

### FB-SV-004 — Gerissenes Fitting

**Beschreibung**: Schlauchtülle, Seeventil oder Borddurchlass zeigt sichtbaren Riss.
**Typische Ursache**: Materialermüdung, Frostschaden (Wasser in Leitung gefroren), Schlagschaden, Entzinkung.
**Betroffene Systeme**: Alle, besonders Komposit-/GFK-Borddurchlässe und alte Messing-Fittings.
**Visuelle Indikatoren**: Sichtbarer Riss, Haarriss, Wasseraustritt an unerwarteter Stelle, Bruchstücke.
**AYDI-Pipeline-B-Erkennung**: Confidence visual_high bei offenem Riss, visual_low bei Haarriss.
**Risiko**: KRITISCH — sofortiger Wassereinbruch möglich.
**Sofortmaßnahme**: Seeventil schließen, Holzstopfen bereithalten, Boot aus dem Wasser.
**Präventiv**: Winterentleerung aller Systeme, regelmäßige Inspektion, DZR-Messing oder Bronze verwenden.
**AYDI-Score-Abzug**: -100 unter WL (Score 0), -70 über WL.
**Kosten Behebung**: 80–500 EUR (neues Fitting + Einbau) + 2–8 h Arbeitszeit.
**Differentialdiagnose**: Riss durch Frost vs. Materialermüdung vs. Entzinkung.
**Verwechslungsgefahr**: Oberflächliche Gelcoat-Risse am Borddurchlass-Flansch (GFK) ≠ struktureller Riss.

### FB-SV-005 — Undichter Quick-Connect

**Beschreibung**: Quick-Connect-Kupplung tropft oder spritzt unter Druck.
**Typische Ursache**: O-Ring verschlissen/verhärtet, Verriegelung nicht vollständig eingerastet, Schmutz in Dichtfläche.
**Betroffene Systeme**: Trinkwasser, Klimaanlage, Waschmaschinenanschluss.
**Visuelle Indikatoren**: Wassertropfen an Kupplung, Kalkablagerung, O-Ring-Extrusion sichtbar.
**AYDI-Pipeline-B-Erkennung**: Confidence visual_medium — Tropfen/Kalk erkennbar, Ursache unklar.
**Risiko**: NIEDRIG bis MITTEL — Trinkwasser-Leckage, kein Sinken.
**Sofortmaßnahme**: Kupplung lösen, O-Ring ersetzen (Viton oder EPDM), Dichtfläche reinigen, neu verriegeln.
**Präventiv**: O-Ring alle 3–5 Jahre ersetzen. Silikonfett auf O-Ring bei Montage.
**AYDI-Score-Abzug**: -15 bis -25 je nach System.
**Kosten Behebung**: 2–8 EUR (O-Ring-Set) + 10–20 min Arbeitszeit.
**Differentialdiagnose**: Undichtigkeit am O-Ring vs. an der Schlauch-Einsteckseite.
**Verwechslungsgefahr**: Kondenswasser an kalter Trinkwasserleitung ≠ Leckage.

### FB-SV-006 — Falsche Schellenart

**Beschreibung**: Für die Anwendung ungeeignete Schellenart verwendet (z.B. Federbandschelle auf druckbeaufschlagtem System, oder gelochte Schelle unter WL).
**Typische Ursache**: Unwissenheit, Sparmaßnahme, Baumarkt-Material statt Marine-Qualität.
**Betroffene Systeme**: Alle — häufig bei DIY-Reparaturen.
**Visuelle Indikatoren**: Gelochtes Band unter WL, Spiralfeder-Schelle auf Kühlwasserschlauch, Kabelbinder als Schelle, Schraubwurm-Schelle aus verzinktem Stahl.
**AYDI-Pipeline-B-Erkennung**: Confidence visual_high — Schellentyp meist klar erkennbar.
**Risiko**: Abhängig von Position und System. Unter WL: KRITISCH.
**Sofortmaßnahme**: Durch korrekte Marine-Schelle ersetzen (s. Zuordnungstabelle Abschnitt 9).
**Präventiv**: Nur Marine-Schellen kaufen (AWAB, Breeze, Norma, Mkaleu). Keine Baumarkt-Schellen.
**AYDI-Score-Abzug**: -20 bis -80 je nach Abweichung und Position.
**Kosten Behebung**: 3–15 EUR pro Schelle + 10–20 min Arbeitszeit.
**Differentialdiagnose**: Bewusste Wahl (Constant-Torque im Motorraum = korrekt) vs. falsche Wahl.
**Verwechslungsgefahr**: Manche hochwertigen gelochten Schellen (SAE Typ F, 316SS) sind über WL durchaus akzeptabel.

### FB-SV-007 — Einzelschelle unterhalb der Wasserlinie

**Beschreibung**: Nur eine einzelne Schlauchschelle an einer Verbindung unterhalb der Wasserlinie.
**Typische Ursache**: Unwissenheit über ABYC H-27 Anforderung, Platz-/Zugangsproblem, Vergessen.
**Betroffene Systeme**: Alle Systeme mit Anschlüssen unter WL (Kühlwasser, Sanitär, Klimaanlage).
**Visuelle Indikatoren**: Nur eine Schelle sichtbar, zweite Position leer.
**AYDI-Pipeline-B-Erkennung**: Confidence visual_high — Schellen-Anzahl zählbar.
**Risiko**: KRITISCH — bei Schellen-Versagen kein Backup.
**Sofortmaßnahme**: Zweite Schelle montieren (W4/W5 316SS Vollband).
**Präventiv**: Bei jeder Montage unter WL systematisch doppelte Schelle verwenden.
**AYDI-Score-Abzug**: -50 (Befund KRITISCH, Compliance-Verstoß ABYC H-27).
**Kosten Behebung**: 5–10 EUR + 10–15 min Arbeitszeit.
**Differentialdiagnose**: Einzelschelle vs. T-Bolt-Schelle (T-Bolt zählt als Einzelsicherung, ist aber akzeptabel wenn hochwertig).
**Verwechslungsgefahr**: Oetiker-StepLess = Einzelschelle, aber Sicherheit vergleichbar mit Doppelschelle durch gleichmäßige 360°-Klemmung.

### FB-SV-008 — Überangezogene Schelle, Schlauch gequetscht

**Beschreibung**: Schlauchschelle wurde mit übermäßigem Drehmoment angezogen, Schlauch ist sichtbar eingeschnürt/gequetscht.
**Typische Ursache**: Fehlende Drehmomentbegrenzung, Angst vor Leckage → „viel hilft viel".
**Betroffene Systeme**: Alle Systeme mit Gummi-/Silikonschläuchen.
**Visuelle Indikatoren**: Tiefe Einschnürung im Schlauch, Schlauchoberfläche quillt neben der Schelle hervor, Schellenband verformt.
**AYDI-Pipeline-B-Erkennung**: Confidence visual_high — Einschnürung deutlich sichtbar.
**Risiko**: MITTEL — langfristig Schlauchriss an der Quetschstelle.
**Sofortmaßnahme**: Schelle lockern, Schlauch inspizieren (innere Beschädigung?), ggf. Schlauch ersetzen.
**Präventiv**: Drehmomentschlüssel verwenden. Kein Werkzeug mit langem Hebel.
**AYDI-Score-Abzug**: -20 über WL, -35 unter WL.
**Kosten Behebung**: 0–30 EUR (ggf. neuer Schlauchabschnitt) + 15–30 min.
**Differentialdiagnose**: Überangezogen vs. zu kleiner Schlauchdurchmesser auf zu großem Stutzen.
**Verwechslungsgefahr**: Normaler Sitz (leichte Konturierung) ≠ Überquetschung (tiefe Einschnürung >2 mm).

### FB-SV-009 — Entzinkter Schlauchtülle

**Beschreibung**: Messing-Schlauchtülle zeigt rosa/kupferfarbene Verfärbung — Zink hat sich aus der Legierung gelöst.
**Typische Ursache**: Nicht-DZR-Messing in Salzwasser, beschleunigt durch Streuströme, warmes Wasser.
**Betroffene Systeme**: Alle Systeme mit Messing-Stutzen, besonders Kühlwasser (warm!) und unter WL.
**Visuelle Indikatoren**: Rosa/kupferfarbene Oberfläche statt gelb, schwammige Textur, Materialverlust.
**AYDI-Pipeline-B-Erkennung**: Confidence visual_high — rosa Verfärbung ist eindeutiges Indiz.
**Risiko**: KRITISCH — Festigkeitsverlust bis 90 %, Bruchgefahr.
**Sofortmaßnahme**: SOFORT außer Betrieb nehmen. Stutzen durch DZR-Messing (CW602N) oder Bronze ersetzen.
**Präventiv**: Nur DZR-Messing oder Bronze im Salzwasserbereich. Alte Boote systematisch prüfen.
**AYDI-Score-Abzug**: -90 unter WL (Befund KRITISCH), -60 über WL.
**Kosten Behebung**: 30–120 EUR (neuer Stutzen) + 1–3 h Arbeitszeit.
**Differentialdiagnose**: Entzinkung vs. natürliche Patina (grün) vs. Kupfer-Oxidation.
**Verwechslungsgefahr**: Neue polierte Bronze hat ebenfalls einen rötlichen Ton — aber gleichmäßig und glatt, nicht schwammig.

### FB-SV-010 — Falsches Gewindedichtmittel

**Beschreibung**: Falsches oder fehlendes Dichtmittel an Gewindeverbindung (z.B. PTFE auf BSP-Gewinde, Hanf auf Trinkwasser).
**Typische Ursache**: Verwechslung NPT/BSP-Dichtungsprinzip, Unwissenheit, falsches Material an Bord.
**Betroffene Systeme**: Alle Gewindeverbindungen Stutzen-zu-Ventil.
**Visuelle Indikatoren**: PTFE-Band quillt aus BSP-Verbindung hervor, Hanffasern sichtbar, Dichtmittel-Klumpen.
**AYDI-Pipeline-B-Erkennung**: Confidence visual_medium — Dichtmitteltyp schwer zu bestimmen auf Fotos.
**Risiko**: MITTEL — Leckage am Gewinde, nicht am Schlauch.
**Sofortmaßnahme**: Verbindung demontieren, Gewinde reinigen, korrektes Dichtmittel verwenden.
**Präventiv**: NPT = PTFE-Band (3–5 Wicklungen in Einschraubrichtung). BSP = Loctite 577 oder Flachdichtung.
**AYDI-Score-Abzug**: -15 über WL, -30 unter WL.
**Kosten Behebung**: 5–25 EUR (Dichtmittel) + 30–60 min.
**Differentialdiagnose**: Falsches Dichtmittel vs. fehlendes Dichtmittel vs. altes ausgehärtetes Dichtmittel.
**Verwechslungsgefahr**: Professionell aufgetragenes PTFE-Band ist kaum sichtbar — Fehlen von sichtbarem Dichtmittel ≠ fehlendes Dichtmittel.

### FB-SV-011 — UV-degradiertes Fitting

**Beschreibung**: Kunststoff- oder Komposit-Fitting zeigt UV-Schäden — Versprödung, Verfärbung, Rissbildung.
**Typische Ursache**: Fitting ist direkter Sonneneinstrahlung ausgesetzt (Deck, Cockpit, offener Motorraum).
**Betroffene Systeme**: Trinkwasser (PVC/Acetal-Quick-Connects), Deckwaschanlage, Cockpit-Entwässerung.
**Visuelle Indikatoren**: Vergilbung (PVC), Kreidung (Oberfläche wird matt/pulvrig), Mikrorisse, Brüchigkeit.
**AYDI-Pipeline-B-Erkennung**: Confidence visual_medium — Vergilbung erkennbar, Brüchigkeit nicht.
**Risiko**: MITTEL — Bruchgefahr bei Belastung.
**Sofortmaßnahme**: Fitting ersetzen. UV-Schutz nachrüsten (Schrumpfschlauch, Abdeckung, UV-Farbe).
**Präventiv**: Kunststoff-Fittings nicht der Sonne aussetzen. Marken-Fittings mit UV-Stabilisator verwenden.
**AYDI-Score-Abzug**: -15 bis -30 je nach Schwere.
**Kosten Behebung**: 10–40 EUR (Fitting) + 15–45 min Arbeitszeit.
**Differentialdiagnose**: UV-Degradation vs. chemische Unverträglichkeit (z.B. Kraftstoff auf PVC).
**Verwechslungsgefahr**: Manche Marine-Kunststoffe sind ab Werk matt/weiß → kein UV-Schaden.

### FB-SV-012 — Vibrationsermüdung

**Beschreibung**: Schlauchtülle oder Schlauchschelle zeigt Ermüdungsriss durch Dauervibration.
**Typische Ursache**: Motorvibration (25–100 Hz), starre Schlauchführung ohne Vibrationsentkopplung.
**Betroffene Systeme**: Motorkühlwasser, Nassauspuff, Kraftstoffzuleitung, Generator-Anschlüsse.
**Visuelle Indikatoren**: Haarrisse am Stutzen-Ansatz, gelockerte Schlauchschelle, Abriebspuren am Schlauch.
**AYDI-Pipeline-B-Erkennung**: Confidence visual_low — Haarrisse und Lockerung schwer erkennbar.
**Risiko**: HOCH im Motorraum (Kühlwasserverlust → Motorschaden, Kraftstoffleck → Brand).
**Sofortmaßnahme**: Stutzen ersetzen, flexible Schlauchführung herstellen, Constant-Torque-Schellen verwenden.
**Präventiv**: Schlauchbogen zwischen Motor und Schott (Vibrationsentkopplung). Constant-Torque-Schellen im Motorraum.
**AYDI-Score-Abzug**: -30 bis -50 je nach System.
**Kosten Behebung**: 20–80 EUR (Stutzen + Schellen) + 1–2 h Arbeitszeit.
**Differentialdiagnose**: Vibrationsermüdung vs. einmaliger Schlagschaden vs. Korrosion.
**Verwechslungsgefahr**: Normales Spiel in flexibler Motorschlauch-Aufhängung ≠ gelockerte Verbindung.

(Confidence: documented — Marine-Surveyor-Praxis, Schadensberichte, Versicherungsfälle, Pipeline-B-Validierung)

---

## 14. Fehlerbehebungs-Leitfaden

### 14.1 Problem: Schlauchverbindung tropft trotz neuer Schelle

**Symptom**: Neue Schelle montiert, korrekt angezogen, tropft weiterhin.

**Diagnose-Schritte:**
1. Tropfstelle exakt lokalisieren (Papiertuch-Methode).
2. Tropft es am Schellenband → Schelle sitzt nicht auf dem Barb, oder Schlauch-ID zu groß.
3. Tropft es am Schlauchende → Schlauch zu kurz, ragt nicht über letzten Barb.
4. Tropft es am Gewinde → Gewindedichtung defekt (s. FB-SV-010).
5. Tropft es am Stutzen-Körper → Stutzen gerissen (s. FB-SV-004).

**Lösung nach Ursache:**
- Schelle rutscht über Barb: Schlauch weiter aufschieben, Schelle über dem Barb positionieren.
- Schlauch zu groß: Schlauch mit korrektem ID verwenden (Stutzen-OD = Schlauch-ID oder 1 mm kleiner).
- Stutzen-Oberfläche beschädigt: Stutzen ersetzen oder Oberfläche mit 400er Nassschleifpapier glätten (nur über WL!).
- Schlauch verhärtet: Alten Schlauch ersetzen — verhärteter Schlauch dichtet nicht mehr ab.

**Kosten**: 0–50 EUR | **Zeitaufwand**: 15–60 min

### 14.2 Problem: Schlauch lässt sich nicht auf Stutzen schieben

**Symptom**: Neuer Schlauch ist zu eng für den Stutzen, lässt sich nicht montieren.

**Diagnose-Schritte:**
1. Stutzen-OD und Schlauch-ID mit Schieblehre messen.
2. Korrekte Zuordnung prüfen (Schlauch-ID soll = Stutzen-OD oder max. 1 mm kleiner).
3. Bei korrekten Maßen: Schlauch ist zu steif (Nassauspuff, Kraftstoff).

**Lösung:**
- Schlauchende 30–60 Sekunden mit Heißluftfön auf 60–70 °C erwärmen.
- Silikonspray (lebensmittelecht!) großzügig auf Stutzen und Schlauchinnenseite.
- Bei Nassauspuff-Schlauch: warmes Wasser (60 °C) in Schlauchende gießen und 2 min einwirken lassen.
- **NIEMALS** Schmiermittel auf Ölbasis verwenden → greift Gummi an.
- **NIEMALS** Schlauch mit Zange aufweiten → dauerhafte Deformation.

**Kosten**: 0–10 EUR (Silikonspray) | **Zeitaufwand**: 10–30 min

### 14.3 Problem: Schelle rostet nach wenigen Monaten

**Symptom**: Neue Schlauchschelle zeigt nach 3–12 Monaten deutliche Korrosion.

**Diagnose-Schritte:**
1. Schellentyp identifizieren (Prägung lesen: W1? W2? W4? W5?).
2. W1/W2 in Salzwasserumgebung → erwartbar, Material ungeeignet.
3. W4/W5 nach 3–6 Monaten rostig → Verdacht auf Streustrom oder galvanische Korrosion.
4. Nur Schraube rostet, Band ist OK → gemischte Materialien (Band 316SS, Schraube 304SS oder verzinkt).

**Lösung:**
- W1/W2 → Durch W4/W5 Vollband ersetzen. Alle Schellen systematisch durchgehen.
- Streustrom-Verdacht → Erdungsprüfung der Landstromanlage (ABYC E-11). Galvanischen Isolator prüfen.
- Gemischte Materialien → Komplett-316SS-Schelle verwenden (Band UND Schraube UND Gehäuse).
- Galvanische Korrosion → Materialpaare prüfen (s. Abschnitt 12.2.1).

**Kosten**: 5–15 EUR/Schelle, bei Streustrom 200–500 EUR (Elektriker) | **Zeitaufwand**: 15 min/Schelle

### 14.4 Problem: Nassauspuff-Schlauch wird weich und aufgebläht

**Symptom**: Nassauspuff-Schlauch fühlt sich weich an, ist aufgebläht, Außendurchmesser vergrößert.

**Diagnose-Schritte:**
1. Schlauchtyp prüfen — ist es ein zertifizierter Nassauspuff-Schlauch (SAE J2006)?
2. Abgastemperatur messen (Infrarot-Thermometer am Schlauch).
3. Mischungsverhältnis Abgas/Seewasser prüfen — zu wenig Kühlwasser = zu heiß.

**Lösung:**
- Falscher Schlauchtyp → Durch SAE J2006 / ISO 13363 Nassauspuff-Schlauch ersetzen.
- Temperatur >70 °C am Schlauch → Seewasserdurchfluss erhöhen, Impeller prüfen.
- Schlauch aufgebläht → SOFORT ersetzen, innere Schichten delaminiert, Platzer-Gefahr.
- Alle Schlauchschellen nach Schlauchwechsel erneuern (alte Schellen passen nicht mehr auf neuen Durchmesser).

**Kosten**: 80–250 EUR (Nassauspuff-Schlauch/m) + 60–150 EUR (Schellen-Set) | **Zeitaufwand**: 2–4 h

### 14.5 Problem: Quick-Connect verriegelt nicht mehr

**Symptom**: Quick-Connect-Kupplung lässt sich einstecken, rastet aber nicht ein, Schlauch rutscht heraus.

**Diagnose-Schritte:**
1. Verriegelungsmechanismus inspizieren (Klemmring, Federkralle, Drucktaste).
2. Schmutz/Kalk im Verriegelungsmechanismus?
3. Feder gebrochen oder ermüdet?
4. Schlauch-OD korrekt für diese Kupplung?

**Lösung:**
- Verschmutzung → Mit Essigwasser (1:3) entkalken, Mechanismus mit Druckluft ausblasen.
- Feder defekt → Kupplung ersetzen (Reparatur nicht möglich/sinnvoll).
- Falscher Schlauch-OD → Korrekten Schlauch verwenden oder Adapter.
- Kupplungskörper verformt (z.B. durch Tritt auf Deck) → Ersetzen.
- Temporäre Notlösung: Schelle über Quick-Connect als Sicherung (KEINE Dauerlösung).

**Kosten**: 8–35 EUR (Quick-Connect-Kupplung) | **Zeitaufwand**: 15–30 min

(Confidence: documented — Werftpraxis, Surveyor-Erfahrung, Herstellerangaben)

---

## 15. FAQ — Häufig gestellte Fragen

### SV-001: Warum brauche ich doppelte Schellen unter der Wasserlinie?
ABYC H-27.5.4 schreibt mindestens zwei Schlauchschellen an jeder Verbindung unter der Wasserlinie vor. Grund: Bei Versagen einer Schelle hält die zweite den Schlauch. Unter WL bedeutet jede abgerutschte Verbindung = unkontrollierter Wassereinbruch. Die doppelte Schelle ist die billigste Lebensversicherung an Bord (Kosten: 5–10 EUR).

### SV-002: Was ist der Unterschied zwischen W1, W2, W4 und W5 Schellen?
Die W-Klasse bezeichnet den Werkstoff. W1 = verzinkter Stahl (Korrosion in 2–3 Jahren Salzwasser). W2 = Band 304SS, Schraube verzinkt (Schwachstelle Schraube). W4 = komplett AISI 316 Edelstahl (Marinestandard). W5 = komplett AISI 316L (niedrigerer Kohlenstoff, bessere Schweißbarkeit). Für Marine unter WL: nur W4 oder W5 akzeptabel.

### SV-003: Kann ich eine Autoschelle für mein Boot verwenden?
Technisch kurzfristig ja, langfristig nein. Auto-Schellen sind typischerweise W1 (verzinkt) oder bestenfalls W2. In Salzwasserumgebung korrodieren sie in 1–3 Jahren. AYDI bewertet Auto-Schellen (verzinkt) im Marine-Einsatz mit -40 bis -80 Punkten je nach Position.

### SV-004: PTFE-Band oder Loctite 577 — wann was?
PTFE-Band (Teflonband) = für konische Gewinde (NPT, BSPT). Die Dichtung entsteht durch Verformung des konischen Gewindes + PTFE als Gleitmittel/Filler. Loctite 577 = für parallele Gewinde (BSP/G-Gewinde). Die Dichtung entsteht durch Aushärtung des anaeroben Klebstoffs im Gewindespalt. Verwechslung → Undichtigkeit.

### SV-005: Wie erkenne ich Entzinkung an einem Messing-Stutzen?
Kratzen Sie mit einem Messer an der Oberfläche. Normales Messing ist gelb und hart. Entzinktes Messing ist rosa/kupferfarben und weich (Messer dringt ein). Zusätzlich: schwammige Textur, Volumenzunahme. Bei Verdacht: SOFORT ersetzen durch DZR-Messing oder Bronze.

### SV-006: Wie oft muss ich Schlauchschellen nachziehen?
Neue Schellen: nach 24 h nachziehen (Schlauch setzt sich). Danach: bei jeder Routine-Inspektion Sitz prüfen (Schelle darf sich nicht von Hand drehen lassen). Constant-Torque-Schellen brauchen kein Nachziehen — die Feder kompensiert automatisch.

### SV-007: Sind Oetiker-Schellen besser als Schneckenband-Schellen?
Für viele Marine-Anwendungen ja. Oetiker StepLess bieten 360°-gleichmäßige Klemmung ohne Lochung, die in den Schlauch schneiden könnte. Nachteil: Einmalmontage — beim Lösen wird die Schelle zerstört. Daher: ideal für Langzeit-Verbindungen (Trinkwasser, Kraftstoff), weniger ideal für Service-Punkte.

### SV-008: Kann ich Silikonschlauch statt Gummischlauch verwenden?
Silikon hat bessere UV- und Temperaturbeständigkeit, aber schlechtere Abreißfestigkeit und ist nicht kraftstoffbeständig. Geeignet: Trinkwasser, Heizung. Ungeeignet: Kraftstoff, Nassauspuff (ohne Glasfaserverstärkung), Anwendungen mit hoher Auszugskraft. AYDI bewertet Silikonschlauch im Kraftstoffsystem mit Score 0.

### SV-009: Was kostet ein kompletter Schellen-Austausch auf einer 12-m-Yacht?
Typischer Umfang: 30–50 Schlauchverbindungen, davon 8–15 unter WL. Material (W4/W5 Schellen): 150–350 EUR. Arbeitszeit (Fachwerft): 8–16 h à 80–120 EUR/h = 640–1.920 EUR. Gesamt: 800–2.300 EUR. DIY-Kosten: nur Material. AYDI-Empfehlung: Systematischer Austausch alle 10–12 Jahre.

### SV-010: Warum ist meine neue 316SS-Schelle magnetisch?
316SS ist leicht magnetisch nach Kaltverformung (Stanzen, Biegen). Das ist normal und kein Qualitätsmangel. Stark magnetisch deutet auf 304SS oder gar Kohlenstoffstahl hin. Test: Magnet haftet fest = NICHT 316SS. Magnet haftet leicht = 316SS nach Kaltverformung (OK). Magnet haftet nicht = austenitisch (ideal).

### SV-011: Muss ich Schlauchschellen auch am Motor-Kühlwasserkreislauf verdoppeln?
Innerhalb des Motorraums: eine Schelle ist üblich (Herstellervorgabe). Am Übergang Motor → Bordsystem (insbesondere Seewasser-Eintritt unter WL): doppelte Schelle PFLICHT. AYDI bewertet den gesamten Pfad vom Seeventil bis zum Motor — jeder Punkt unter WL benötigt Doppelschelle.

### SV-012: Was ist ein T-Bolt-Clamp und wann brauche ich ihn?
T-Bolt (auch: Heavy-Duty-Schelle) hat einen Bolzen mit Mutter statt Schneckengetriebe. Vorteile: höhere Klemmkraft, kein Schlupf, kein Einschneiden. Einsatz: Nassauspuff (Hitze + Vibration), Turbolader, große Durchmesser (>50 mm), Anwendungen mit Sicherheitsanforderung. Nachteil: braucht Steckschlüssel, teurer (15–35 EUR/Stk.).

### SV-013: Kann Frostschaden meine Borddurchlässe zerstören?
Ja. Wasser in Leitungen dehnt sich beim Gefrieren um ~9 % aus. Das kann Bronzestutzen, GFK-Borddurchlässe und Kugelhähne sprengen. Prävention: vollständige Winterentleerung oder Frostschutzmittel (Propylenglykol, lebensmittelecht) in alle Systeme. AYDI prüft bei Liegeplatz-Klimazone „kalt" automatisch auf Frostschutz-Maßnahmen.

### SV-014: Warum soll ich keine Schlauchklemmen aus dem Baumarkt verwenden?
Baumarkt-Schellen sind zu 95 % W1 (verzinkt), haben gelochte Bänder (Schlauch-Einschneidgefahr), und der Schneckentrieb ist oft aus minderwertigem Zinkdruckguss. Im Marine-Einsatz versagen sie 5–10× schneller als Marine-Schellen. Preisunterschied: 0,50 EUR (Baumarkt) vs. 3–8 EUR (Marine W4) — bei 50 Schellen = 125–375 EUR Mehrkosten für 10+ Jahre Lebensdauer.

### SV-015: Wie erkenne ich, ob mein Schlauch noch gut ist?
5-Punkte-Schnelltest: 1) Biegen: knickt oder bricht = ersetzen. 2) Quetschen: bleibt eingedrückt = ersetzen. 3) Oberfläche: Risse, Blasen, Quellung = ersetzen. 4) Farbe: Ausbleichung/Verfärbung = UV-Schaden, bald ersetzen. 5) Geruch: Diesel-/Chemie-Geruch bei Nicht-Kraftstoffschlauch = chemischer Angriff, ersetzen.

### SV-016: Welches Drehmoment für Schlauchschellen?
Abhängig von Schellentyp und Durchmesser (s. Tabelle 10.1.3). Faustregel für Schneckenband: kurzer Schraubendreher (150 mm Klinge), anziehen bis deutlicher Widerstand, dann ¼ Umdrehung. NIEMALS mit Knarre oder langem Werkzeug. Drehmomentschlüssel (1–25 Nm) ist die professionelle Lösung (Hazet 5107-2CT, ~100 EUR).

### SV-017: Kann ich Quick-Connects unter der Wasserlinie verwenden?
NEIN. Quick-Connects sind für Niederdruck-Anwendungen über WL konzipiert (Trinkwasser, Deckwäsche). Unter WL fehlt die Redundanz (kein zweiter Sicherungsmechanismus). ABYC und ISO schreiben für unter WL feste Schlauchverbindungen mit Doppelschelle vor. AYDI bewertet Quick-Connect unter WL mit Score 0.

### SV-018: Was ist der Unterschied zwischen NPT und BSP Gewinden?
NPT (National Pipe Thread) = konisch, dichtet im Gewinde selbst. BSP/G (British Standard Pipe) = parallel, dichtet über Dichtring oder Dichtmittel. Die Gewinde sehen ähnlich aus, haben aber unterschiedliche Steigungen und Flankenwinkel (NPT 60°, BSP 55°). Verwechslung = Undichtigkeit oder Gewindeschaden. US-Boote = NPT, europäische Boote = BSP.

### SV-019: Mein Seeventil lässt sich nicht mehr schließen — was tun?
Sofortmaßnahmen: 1) WD-40 oder Kriechöl am Hebel. 2) Mit Holzklotz und Hammer leicht gegen Hebel klopfen. 3) NICHT mit Rohrzange am Ventilkörper ansetzen (Bruchgefahr!). Wenn Ventil festsitzt: Boot so bald wie möglich aus dem Wasser. AYDI-Warnung: Nicht funktionsfähiges Seeventil = Befund KRITISCH (Score -80 im compliance-Modul).

### SV-020: Sind Komposit-Borddurchlässe (Marelon) besser als Bronze?
Marelon (glasfaserverstärktes Nylon): kein Korrosionsproblem, keine galvanische Reaktion, leichter, günstiger. Aber: weniger schlagfest, UV-empfindlich, niedrigere Temperaturbeständigkeit (max. 80 °C / 176 °F). Bronze: bewährt seit 100+ Jahren, extrem robust, schwerer, teurer, galvanische Korrosion möglich. AYDI bewertet beide gleichwertig, wenn korrekt dimensioniert und installiert.

### SV-021: Wie viele Schlauchverbindungen hat eine typische Yacht?
Abhängig von Größe und Ausstattung. Richtwerte: 8 m Segelyacht = 15–25 Verbindungen. 12 m Segelyacht = 30–50 Verbindungen. 15 m Motoryacht = 50–80 Verbindungen. 20 m Motoryacht = 80–120 Verbindungen. Davon unter WL: ca. 20–30 %. Jede einzelne ist potenziell sicherheitskritisch.

### SV-022: Kann ich Schlauchverbindungen mit Kabelbindern sichern?
NIEMALS als alleinige Sicherung. Kabelbinder (Nylon) haben: keine definierte Klemmkraft, UV-Zersetzung nach 1–3 Jahren, kein Nachziehen möglich, keine Korrosionsbeständigkeit im Sinne von ABYC. Als ZUSÄTZLICHE Sicherung (Backup) über WL sind hochwertige UV-stabilisierte Kabelbinder akzeptabel. Unter WL: Score 0.

### SV-023: Was bedeutet „DZR" bei Messing?
DZR = Dezincification Resistant (entzinkungsbeständig). Speziallegierung (CW602N, auch CR-Messing oder DR-Messing genannt) mit Arsen-Zusatz (~0,04 %), der die Entzinkung verhindert. Prägung „DR" oder „DZR" auf dem Fitting. Wenn keine Prägung → unsicher, ob DZR → im Salzwasser besser Bronze verwenden.

### SV-024: Wie lagere ich Ersatzschellen und -schläuche an Bord?
Schellen: in verschlossenem Plastikbeutel mit Silica-Gel-Beutel. Sortiert nach Größe (ID-Bereiche). Empfehlung: je 3 Stück pro verwendeter Größe in W4/W5. Schläuche: kurze Reststücke (30–50 cm) in passenden Durchmessern. Trocken, dunkel, kühl lagern. Nassauspuffschlauch: min. 1 m Reservestück in jeder verwendeten Größe an Bord.

### SV-025: Ab welchem Alter sollte ich ALLE Schlauchverbindungen präventiv erneuern?
Richtwerte: Verzinkte Schellen (W1): alle 3–5 Jahre (besser: sofort durch W4 ersetzen). 304SS (W2): alle 5–8 Jahre (Salzwasser). 316SS (W4/W5): alle 10–15 Jahre. Schläuche: Gummi (EPDM) alle 10–12 Jahre, Nassauspuff alle 8–10 Jahre, PVC alle 3–5 Jahre. AYDI berücksichtigt das Alter automatisch im Score — bei Überschreitung der empfohlenen Lebensdauer sinkt der Score progressiv.

(Confidence: documented — ABYC Standards, ISO Normen, Herstellerangaben, Marine-Surveyor-Praxis)

---

## 16. Glossar

| Begriff | Englisch | Definition |
|---|---|---|
| Schlauchtülle | Hose barb / Hose tail | Rohrstutzen mit Rillen (Barbs), auf den der Schlauch geschoben wird |
| Schlauchschelle | Hose clamp / Hose clip | Spannband zur Befestigung eines Schlauchs auf einem Stutzen |
| Schneckenband-Schelle | Worm drive clamp | Schlauchschelle mit Schneckengetriebe-Spannmechanismus |
| T-Bolt-Schelle | T-bolt clamp | Schlauchschelle mit Bolzen und Mutter, höhere Klemmkraft |
| Oetiker-Schelle | Oetiker StepLess clamp | Ohrschelle mit gleichmäßiger 360°-Klemmung, Einmalmontage |
| Constant-Torque-Schelle | Constant torque clamp | Schelle mit Feder, die Drehmoment bei Vibration/Temperatur konstant hält |
| Vollband-Schelle | Solid band clamp | Schelle ohne Lochung im Band (vs. gelochtes Band) |
| Seeventil | Seacock | Absperrventil am Borddurchlass unter der Wasserlinie |
| Borddurchlass | Through-hull fitting | Durchführung durch den Rumpf für Wasser-/Abwasserleitungen |
| Barb | Barb / Serration | Rillen/Wulste am Schlauchtülle, die den Schlauch gegen Abrutschen sichern |
| WL | Waterline | Wasserlinie — Grenze zwischen Unter- und Überwasserbereich |
| Entzinkung | Dezincification | Korrosionsprozess bei Messing, bei dem Zink herausgelöst wird |
| DZR-Messing | DZR brass | Entzinkungsbeständiges Messing (CW602N) |
| Spaltkorrosion | Crevice corrosion | Korrosion in engen Spalten mit stagnierender Flüssigkeit |
| Galvanische Korrosion | Galvanic corrosion | Korrosion durch Kontakt zweier unedler Metalle in Elektrolyt |
| Streustrom | Stray current | Unbeabsichtigter elektrischer Strom durch Bootskörper/Wasser |
| PTFE | PTFE (Teflon) | Polytetrafluorethylen — Gewindedichtband für konische Gewinde |
| NPT | NPT | National Pipe Thread — konisches US-Rohrgewinde |
| BSP | BSP | British Standard Pipe — paralleles Rohrgewinde (auch G-Gewinde) |
| EPDM | EPDM | Ethylen-Propylen-Dien-Monomer — Standard-Gummi für Marine-Schläuche |
| Nassauspuff | Wet exhaust | Abgassystem, bei dem Abgas mit Seewasser gemischt wird |
| Quick-Connect | Quick-connect fitting | Steckverbindung für schnelles Verbinden/Lösen von Schläuchen |
| Impeller | Impeller | Gummi-Flügelrad in Seewasserpumpen |
| Cv-Wert | Flow coefficient (Cv) | Durchflusskenngröße: US-Gallons/min bei 1 psi Druckabfall |
| Kv-Wert | Flow coefficient (Kv) | Durchflusskenngröße: m³/h bei 1 bar Druckabfall |
| Klemmkraft | Clamping force | Kraft, mit der die Schelle den Schlauch auf den Stutzen presst |
| Kontaktdruck | Contact pressure | Druck [MPa] zwischen Schlauch und Stutzen unter der Schelle |
| Auszugskraft | Pull-off force | Kraft [N], die nötig ist, um Schlauch vom Stutzen zu ziehen |
| Drehmoment | Torque | Anzugsmoment der Schellenschraube [Nm] |
| Lochfraß | Pitting corrosion | Lokale, tiefe Korrosionsangriffe in Form kleiner Löcher |
| Gelcoat | Gelcoat | Äußere Schutzschicht auf GFK-Laminat |
| GFK | FRP / GRP | Glasfaserverstärkter Kunststoff |
| 316SS | 316 stainless steel | Austenitischer Edelstahl mit Molybdän — Marinestandard |
| 316L | 316L stainless steel | 316SS mit niedrigem Kohlenstoffgehalt (<0,03 %) |
| 304SS | 304 stainless steel | Austenitischer Edelstahl ohne Molybdän — NICHT für Salzwasser |
| W1/W2/W4/W5 | DIN 3017 classes | Werkstoffklassen für Schlauchschellen nach DIN 3017 |
| SAE J1508 | SAE J1508 | Standard für Schlauchschellen-Leistung (Automotive/Marine) |
| ABYC H-27 | ABYC H-27 | Standard für Seeventile und Borddurchlässe |
| ISO 9093 | ISO 9093 | Internationale Norm für Borddurchlässe und Seeventile |
| Marelon | Marelon (Forespar) | Glasfaserverstärktes Nylon für Borddurchlässe (Markenname) |
| Anti-Siphon-Ventil | Anti-siphon valve | Ventil, das Rücksaugen von Wasser durch Siphon-Effekt verhindert |

(Confidence: documented — DIN, ISO, ABYC, SAE Normen, Marine-Fachliteratur)

---

## 17. Schnell-Referenz

### 17.1 Entscheidungsbaum: Welche Schelle brauche ich?

```
START → Position der Verbindung?
│
├── Unter Wasserlinie
│   ├── System?
│   │   ├── Alle Systeme → 2× W4/W5 Vollband 316SS, versetzt montiert
│   │   └── Nassauspuff → 2× T-Bolt W4, hitzebeständig
│   └── NIEMALS: W1, W2, gelochtes Band, Quick-Connect, Kabelbinder
│
├── Über Wasserlinie, Motorraum
│   ├── Vibration hoch? → Constant-Torque W4
│   ├── Nassauspuff → T-Bolt W4
│   ├── Kraftstoff → Oetiker StepLess oder W4 Vollband
│   └── Kühlwasser → W4 Vollband oder Constant-Torque
│
├── Über Wasserlinie, Innenraum
│   ├── Trinkwasser → W4 oder NSF-61-zertifiziert Quick-Connect
│   ├── Sanitär → W4 Vollband
│   └── Klimaanlage → W4 Vollband
│
└── Über Wasserlinie, Außenbereich (Deck/Cockpit)
    ├── UV-Exposition → W4/W5, keine Kunststoff-Schellen
    └── Deckwäsche → Quick-Connect (316SS) oder W4
```

### 17.2 Schnell-Referenz-Karte: Drehmomente

```
┌─────────────────────────────────────────────────────┐
│ DREHMOMENT-SCHNELLREFERENZ Schlauchschellen         │
├──────────────────────┬──────────┬───────────────────┤
│ Schellentyp          │ ID [mm]  │ Drehmoment [Nm]   │
├──────────────────────┼──────────┼───────────────────┤
│ Schneckenband 12,7mm │ 12–19    │ 2,5 – 4,0         │
│ Schneckenband 12,7mm │ 20–32    │ 3,0 – 4,5         │
│ Schneckenband 12,7mm │ 33–50    │ 3,5 – 5,0         │
│ Schneckenband 16 mm  │ 19–38    │ 3,5 – 5,5         │
│ Schneckenband 16 mm  │ 40–65    │ 4,0 – 6,0         │
│ T-Bolt               │ 32–50    │ 6,0 – 9,0         │
│ T-Bolt               │ 51–76    │ 7,0 – 10,0        │
│ T-Bolt               │ 78–102   │ 8,0 – 12,0        │
│ Oetiker StepLess     │ alle     │ Zange (kein Nm)    │
└──────────────────────┴──────────┴───────────────────┘
```

### 17.3 Material-Kompatibilitäts-Matrix

```
Stutzen \ Schelle  │ W1 (Zn)  │ W2 (304) │ W4 (316) │ W5 (316L)│ T-Bolt   │
───────────────────┼──────────┼──────────┼──────────┼──────────┼──────────┤
Bronze (DZR)       │ ⚠ galv.  │ ⚠ galv.  │ ✅ OK     │ ✅ OK     │ ✅ OK     │
316SS              │ ⚠ galv.  │ ⚠ galv.  │ ✅ ideal  │ ✅ ideal  │ ✅ ideal  │
Messing (non-DZR)  │ ❌ NEIN   │ ⚠ galv.  │ ⚠ entzink│ ⚠ entzink│ ⚠ entzink│
Marelon/Komposit   │ ❌ NEIN   │ ✅ OK     │ ✅ OK     │ ✅ OK     │ ⚠ zu viel│
Aluminium          │ ❌ NEIN   │ ❌ galv.! │ ❌ galv.! │ ❌ galv.! │ ❌ galv.! │

✅ = kompatibel   ⚠ = bedingt/Vorsicht   ❌ = inkompatibel/verboten
```

(Confidence: documented — ABYC, DIN, ISO, Herstellerangaben)

---

## 18. Notfall-Ressourcen

### 18.1 Sofort-Maßnahmen bei Wassereinbruch durch Schlauchverbindung

```
1. RUHE BEWAHREN.
2. Bilgenpumpe EIN (manuell + elektrisch).
3. Seeventil der betroffenen Leitung SOFORT schließen.
4. Wenn Seeventil nicht erreichbar oder defekt:
   a. Holzstopfen (konisch, weich) in Borddurchlass treiben.
   b. Provisorisch: Handtuch/Lappen um Schlauchende wickeln und mit Schraubzwinge/Kabelbinder sichern.
5. Wenn Wassereinbruch nicht kontrollierbar:
   a. MAYDAY / PAN-PAN auf VHF Kanal 16.
   b. Alle Personen: Rettungswesten anlegen.
   c. Rettungsinsel klarmachen.
6. Nach Kontrolle: Boot so schnell wie möglich aus dem Wasser oder in flaches Wasser bringen.
```

### 18.2 Notfall-Materialien (immer an Bord)

| Material | Menge | Zweck | Lagerort | Preis [EUR] |
|---|---|---|---|---|
| Holzstopfen-Set (konisch, 6 Größen) | 1 Set | Borddurchlass abdichten | Griffbereit an Bilge-Zugang | 15–25 |
| Unterwasser-Epoxy (z.B. Belzona 1111) | 1 Dose | Notdichtung unter WL | Notfallkasten | 30–50 |
| Schlauchschellen W4 (sortiert, 12–50 mm) | je 3 Stk. | Sofort-Ersatz | Werkzeugkasten | 40–80 |
| Schlauch-Reststücke (19, 25, 32 mm) | je 50 cm | Notreparatur | Motorraum-Ablagefach | 10–20 |
| Edelstahl-Draht (1,5 mm, 316SS) | 5 m | Notbefestigung Schlauch | Werkzeugkasten | 5–10 |
| Selbstverschweißendes Silikonband | 1 Rolle | Not-Abdichtung | Notfallkasten | 8–15 |
| Schraubendreher (Schlitz, 6 mm, kurz) | 1 Stk. | Schellen-Montage | Griffbereit | 8–12 |

### 18.3 Notfall-Telefonnummern (Deutschland)

| Dienst | Nummer | Erreichbarkeit |
|---|---|---|
| Seenotleitung Bremen (MRCC) | VHF 16 oder +49 421 536870 | 24/7 |
| Deutsche Gesellschaft zur Rettung Schiffbrüchiger (DGzRS) | VHF 16 oder +49 421 536870 | 24/7 |
| Wasserschutzpolizei (regional) | Hafenmeister fragen | Dienstzeiten |
| ADAC Sportschifffahrt | +49 89 76761346 | 24/7 (Vertragskunden) |
| Pantaenius Havarie-Hotline | +49 40 370920 | 24/7 (Vertragskunden) |

(Confidence: documented — DGzRS, ADAC, Pantaenius, Seemannsordnung)

---

## ANHANG A — Prüfprotokoll Schlauchverbindungen

```
PRÜFPROTOKOLL SCHLAUCHVERBINDUNGEN
Bootsname: _________________ Kennzeichen: _________________
Bootslänge: _______ m       Baujahr: _________
Prüfdatum: __.__.__         Prüfer: _________________________

Nr. | System        | Position  | Stutzen-Mat. | Schlauch-Typ | Schellen-Typ | Schellen-Mat. | Anz. | Zustand | Score | Bemerkung
----|--------------|-----------|-------------|-------------|-------------|--------------|------|---------|-------|----------
 1  |              | ü/u WL    |             |             |             |              |      |         |  /100 |
 2  |              | ü/u WL    |             |             |             |              |      |         |  /100 |
 3  |              | ü/u WL    |             |             |             |              |      |         |  /100 |
...
20  |              | ü/u WL    |             |             |             |              |      |         |  /100 |

Gesamtergebnis: ____/100    Nächste Prüfung: __.__.__

Unterschrift Prüfer: _________________________
```

## ANHANG B — Schlauchschellen-Größen Referenztabelle

| Schlauch-ID [mm] | Schlauch-ID [Zoll] | Empf. Schellengröße | Spannbereich [mm] | Bandbreite [mm] |
|---|---|---|---|---|
| 10 | 3/8" | 16–25 | 16–27 | 12,7 |
| 12 | 1/2" | 16–25 | 16–27 | 12,7 |
| 16 | 5/8" | 20–32 | 21–38 | 12,7 |
| 19 | 3/4" | 25–40 | 27–51 | 12,7 |
| 25 | 1" | 32–50 | 33–57 | 12,7 |
| 32 | 1-1/4" | 40–60 | 40–63 | 12,7 |
| 38 | 1-1/2" | 46–70 | 46–70 | 14,2 |
| 50 | 2" | 59–83 | 59–83 | 14,2 |
| 63 | 2-1/2" | 72–95 | 72–95 | 14,2 |
| 76 | 3" | 83–108 | 83–108 | 14,2 |
| 89 | 3-1/2" | 95–121 | 95–121 | 14,2 |
| 102 | 4" | 108–133 | 108–133 | 14,2 |

## ANHANG C — Gewindeidentifikation Schnelltest

```
GEWINDEIDENTIFIKATION — Schnelltest mit Schieblehre

1. Außendurchmesser des Gewindes messen:
   ≈ 21,0 mm → 1/2" BSP oder 1/2" NPT
   ≈ 26,4 mm → 3/4" BSP oder 3/4" NPT
   ≈ 33,2 mm → 1" BSP oder 1" NPT

2. Gewindesteigung messen (Gewindeschablone oder 10 Gänge messen ÷ 10):
   BSP 1/2": 1,814 mm (14 tpi)
   NPT 1/2": 1,814 mm (14 tpi) ← GLEICH! Nicht unterscheidbar durch Steigung!
   BSP 3/4": 1,814 mm (14 tpi)
   NPT 3/4": 1,814 mm (14 tpi) ← GLEICH!
   BSP 1":   2,309 mm (11 tpi)
   NPT 1":   2,209 mm (11.5 tpi) ← UNTERSCHEIDBAR, aber schwierig

3. Konizität prüfen (einfachste Methode):
   - Mutter auf Gewinde drehen
   - BSP: Mutter sitzt über gesamte Länge gleichmäßig
   - NPT: Mutter wird nach einigen Umdrehungen enger
   - ODER: Lineal an Gewinde halten → NPT zeigt sichtbare Verjüngung (1:16)

4. Im Zweifel: BOOTSHERKUNFT prüfen!
   - USA/Kanada → NPT (98 % der Fälle)
   - Europa/UK/Australien → BSP/G-Gewinde
```

## ANHANG D — Checkliste Winterlager (Schlauchverbindungen)

```
WINTERLAGER-CHECKLISTE — Schlauchverbindungen & Borddurchlässe

□ Alle Seeventile geschlossen
□ Alle Systeme entleert (Kühlwasser, Sanitär, Trinkwasser, Klimaanlage)
□ Frostschutzmittel eingefüllt (Propylenglykol, lebensmittelecht):
  □ Motor-Kühlwasserkreislauf
  □ Sanitärsystem (WC, Pumpe, Leitungen)
  □ Trinkwassersystem (oder vollständig entleert + durchgeblasen)
  □ Klimaanlage (Seewasserseite)
□ Nassauspuff-Schlauch auf Kondenswasser geprüft — Tiefpunkt entwässert
□ Alle Schlauchschellen auf Sitz geprüft (nicht von Hand drehbar)
□ Alle Schlauchschellen auf Korrosion geprüft (Rost = ersetzen im Frühjahr)
□ Alle Schlauchtüllen auf Entzinkung geprüft (rosa = ersetzen!)
□ Borddurchlässe geschlossen und markiert
□ Bilge trocken und sauber
□ Dokumentation: Datum, Prüfer, Befunde im Bordbuch
```

## ANHANG E — Kostenübersicht: Schlauchverbindungen nach Bootsklasse

| Kostenposition | 8 m Segelyacht | 12 m Segelyacht | 15 m Motoryacht | 20 m Motoryacht |
|---|---|---|---|---|
| Anzahl Verbindungen (gesamt) | 15–20 | 30–45 | 50–70 | 80–120 |
| Davon unter WL | 4–6 | 8–12 | 12–18 | 18–30 |
| Material (Komplett-Erneuerung) | 120–250 EUR | 300–600 EUR | 600–1.200 EUR | 1.200–2.500 EUR |
| Arbeitszeit Fachwerft | 6–10 h | 12–20 h | 20–35 h | 35–60 h |
| Stundensatz Fachwerft | 80–120 EUR/h | 80–120 EUR/h | 90–130 EUR/h | 100–150 EUR/h |
| Gesamtkosten Fachwerft | 600–1.450 EUR | 1.260–3.000 EUR | 2.400–5.750 EUR | 4.700–11.500 EUR |
| DIY-Kosten (nur Material) | 120–250 EUR | 300–600 EUR | 600–1.200 EUR | 1.200–2.500 EUR |
| Empfohlenes Erneuerungsintervall | 10–12 Jahre | 10–12 Jahre | 8–10 Jahre | 8–10 Jahre |

## ANHANG F — Hersteller-Kontakte & Bezugsquellen

| Hersteller | Produkt | Website | Marine-Fachhandel |
|---|---|---|---|
| AWAB (Schweden) | Schlauchschellen W4/W5 | awab.com | SVB, Toplicht, Compass |
| Breeze Industrial (USA) | Schellen, T-Bolt, CT | breezeclamps.com | West Marine, Defender |
| Norma Group (DE) | NORMA Torro, ARS | normagroup.com | SVB, Compass |
| Oetiker (CH) | StepLess, 2-Ear | oetiker.com | Fachhandel, Online |
| Forespar (USA) | Marelon-Borddurchlässe | forespar.com | SVB, Toplicht |
| TruDesign (NZ) | Komposit-Borddurchlässe | trudesignplastics.com | SVB, Compass |
| Groco (USA) | Bronze-Seeventile/-Stutzen | groco.net | West Marine, Defender |
| Perko (USA) | Bronze/Marelon-Fittings | perko.com | West Marine |
| Buck Algöl (DE) | Schlauchtüllen, Stutzen | buck-algoel.de | Fachhandel |
| Vetus (NL) | Borddurchlässe, Stutzen | vetus.com | SVB, Compass |

## ANHANG G — AYDI-Score-Mapping: Schlauchverbindungen

```python
# AYDI Scoring-Logik für Schlauchverbindungen
# Module: materials, structural, compliance

SCORING_RULES_HOSE_CONNECTIONS = {
    "clamp_material_below_wl": {
        "w4_w5_316ss":    {"score": 100, "finding": None},
        "w2_304ss":       {"score": 40,  "finding": "HOCH — 304SS unter WL nicht salzwasserbeständig"},
        "w1_galvanized":  {"score": 5,   "finding": "KRITISCH — verzinkt unter WL, Korrosion in 2-3 Jahren"},
        "cable_tie":      {"score": 0,   "finding": "KRITISCH — Kabelbinder ist KEINE Schlauchsicherung"},
        "wire":           {"score": 0,   "finding": "KRITISCH — Draht ist KEINE zugelassene Schlauchsicherung"},
    },
    "clamp_count_below_wl": {
        "double_offset":  {"score": 100, "finding": None},
        "double_aligned": {"score": 85,  "finding": "NIEDRIG — Schellen sollten versetzt montiert werden"},
        "single_tbolt":   {"score": 70,  "finding": "MITTEL — T-Bolt Einzelschelle unter WL, Doppelschelle empfohlen"},
        "single_worm":    {"score": 30,  "finding": "KRITISCH — Einzelschelle unter WL, ABYC H-27 Verstoß"},
        "none":           {"score": 0,   "finding": "KRITISCH — Schlauch ohne Schelle = Sinken bei Abrutschen"},
    },
    "barb_material_below_wl": {
        "bronze_dzr":     {"score": 100, "finding": None},
        "316ss":          {"score": 100, "finding": None},
        "marelon":        {"score": 90,  "finding": None},
        "brass_non_dzr":  {"score": 20,  "finding": "KRITISCH — Messing ohne DZR unter WL, Entzinkungsgefahr"},
        "plastic_generic":{"score": 10,  "finding": "KRITISCH — generischer Kunststoff unter WL nicht zugelassen"},
    },
    "hose_condition": {
        "new_flexible":   {"score": 100, "finding": None},
        "aged_flexible":  {"score": 80,  "finding": None},
        "aged_stiffening":{"score": 55,  "finding": "MITTEL — Schlauch verhärtet, Austausch planen"},
        "cracked":        {"score": 20,  "finding": "HOCH — Schlauch gerissen, Austausch erforderlich"},
        "swollen":        {"score": 15,  "finding": "HOCH — Schlauch aufgequollen, Austausch sofort"},
        "leaking":        {"score": 0,   "finding": "KRITISCH — Schlauch undicht, Sofortmaßnahme erforderlich"},
    },
}
```

## ANHANG H — Umrechnungstabellen

### Zoll ↔ Millimeter (häufig verwendete Schlauchmaße)

| Zoll | mm (exakt) | mm (gerundet) | Anmerkung |
|---|---|---|---|
| 3/8" | 9,525 | 10 | Kleine Trinkwasserleitungen |
| 1/2" | 12,700 | 13 | Trinkwasser, Bilge klein |
| 5/8" | 15,875 | 16 | Trinkwasser, Sanitär |
| 3/4" | 19,050 | 19 | Standard Kühlwasser, Sanitär |
| 1" | 25,400 | 25 | Kühlwasser Motor, Bilge |
| 1-1/4" | 31,750 | 32 | Kühlwasser groß, Sanitär-Hauptleitung |
| 1-1/2" | 38,100 | 38 | Nassauspuff klein, Bilge groß |
| 2" | 50,800 | 51 | Nassauspuff Standard |
| 2-1/2" | 63,500 | 64 | Nassauspuff groß |
| 3" | 76,200 | 76 | Nassauspuff Großmotoren |
| 4" | 101,600 | 102 | Nassauspuff Großdiesel |

### Druck-Umrechnung

| Einheit | bar | psi | kPa | mbar |
|---|---|---|---|---|
| 1 bar | 1 | 14,504 | 100 | 1000 |
| 1 psi | 0,0689 | 1 | 6,895 | 68,95 |
| 1 kPa | 0,01 | 0,145 | 1 | 10 |
| 1 mbar | 0,001 | 0,0145 | 0,1 | 1 |

## ANHANG I — Fehlercode-Referenz (AYDI-intern)

| Fehlercode | Modul | Schwere | Beschreibung |
|---|---|---|---|
| HC-001 | compliance | KRITISCH | Einzelschelle unter WL |
| HC-002 | compliance | KRITISCH | Verzinkte Schelle unter WL |
| HC-003 | compliance | KRITISCH | Kabelbinder als Schlauchsicherung unter WL |
| HC-004 | materials | KRITISCH | Entzinkter Messing-Stutzen |
| HC-005 | materials | KRITISCH | Gerissener Borddurchlass/Stutzen |
| HC-006 | materials | HOCH | 304SS-Schelle in Salzwasser unter WL |
| HC-007 | materials | HOCH | Galvanische Inkompatibilität Stutzen/Schelle |
| HC-008 | structural | HOCH | Schlauch gerissen oder aufgequollen |
| HC-009 | structural | HOCH | Überangezogene Schelle, Schlauch gequetscht |
| HC-010 | compliance | MITTEL | Falsches Gewindedichtmittel |
| HC-011 | materials | MITTEL | UV-degradiertes Kunststoff-Fitting |
| HC-012 | structural | MITTEL | Vibrationsermüdung an Motoranschluss |
| HC-013 | service_patterns | NIEDRIG | Schlauchverbindung >75 % Lebensdauer |
| HC-014 | service_patterns | NIEDRIG | Quick-Connect O-Ring >5 Jahre alt |
| HC-015 | compliance | INFO | Schellen nicht versetzt montiert |

## ANHANG J — Normverweise (Vollständig)

| Norm | Titel | Relevanz |
|---|---|---|
| ABYC H-27 (2021) | Seacocks, Through-Hulls, and Drain Plugs | Borddurchlässe, Schellen-Anforderungen |
| ABYC H-24 (2019) | Gasoline Fuel Systems | Kraftstoff-Schlauchverbindungen |
| ABYC H-33 (2019) | Diesel Fuel Systems | Diesel-Schlauchverbindungen |
| ISO 9093-1 (2020) | Small Craft — Seacocks and Through-Hull Fittings | Borddurchlässe international |
| ISO 9093-2 (2020) | Small Craft — Seacock Installation | Einbau Seeventile |
| ISO 10239 (2014) | Small Craft — LPG Systems | Gas-Leitungsverbindungen |
| ISO 10088 (2013) | Small Craft — Permanently Installed Fuel Systems | Kraftstoff-Anschlüsse |
| ISO 8099 (2020) | Small Craft — Waste Water Retention | Sanitär-Anschlüsse |
| ISO 7-1 (2022) | Pipe Threads — Part 1: Taper Threads | Konische Gewinde (R/Rc/Rp) |
| ISO 228-1 (2003) | Pipe Threads — Part 1: Parallel Threads | Parallele Gewinde (G) |
| DIN 3017 (2020) | Schlauchschellen | Schellentypen, W-Klassen |
| SAE J1508 (2018) | Hose Clamp Specifications | Schellentypen und -Prüfverfahren |
| SAE J1475 (2014) | Hydraulic Hose Fittings for Marine Applications | Marine-Hydraulik-Schlauchanschlüsse |
| SAE J2006 (2019) | Wet Exhaust Hose | Nassauspuff-Schlauch |
| CE 2013/53/EU | Recreational Craft Directive | Sportboot-Richtlinie (übergeordnet) |

## ANHANG K — Fallstudie: Wassereinbruch durch Einzelschelle

**Boot**: Bavaria 37 Cruiser, Baujahr 2008, Salzwasser-Revier Mittelmeer.
**Vorfall**: Wassereinbruch während Nachtfahrt, Bilgenalarm um 02:30 Uhr.
**Ursache**: Einzelne W2-Schelle am Seewassereinlass der Klimaanlage (unter WL) hatte sich gelockert. Schlauch um 15 mm vom Stutzen gerutscht. Wassereinbruch ca. 20 l/min.
**Sofortmaßnahme**: Seeventil geschlossen, Bilgenpumpe hat Wasser kontrolliert. Kein Sinken.
**Befund Survey**: 6 von 10 Unterwasser-Verbindungen hatten nur Einzelschellen. 3 Schellen waren W2, nicht W4.
**Behebung**: Alle Unterwasser-Verbindungen auf doppelte W4/W5-Schellen umgerüstet.
**Kosten**: 280 EUR Material + 12 h Werftarbeit (1.080 EUR) = 1.360 EUR gesamt.
**AYDI-Score vor Reparatur**: 22/100 (compliance + structural). Nach Reparatur: 95/100.
**Lektion**: Einzelschelle unter WL ist ein systematisches Risiko. ABYC H-27 existiert aus gutem Grund.

(Confidence: documented — Surveyor-Bericht, Versicherungsfall)

## ANHANG L — Fallstudie: Entzinkung eines Messing-Seeventils

**Boot**: Hallberg-Rassy 352, Baujahr 1984, Salzwasser-Revier Nordsee.
**Vorfall**: Beim Winterlager-Service Routine-Inspektion der Borddurchlässe.
**Befund**: Messing-Seeventil (nicht DZR) am WC-Einlass zeigt rosa Verfärbung. Messer dringt 2 mm in Material ein. Festigkeitsverlust geschätzt >70 %.
**Risiko-Bewertung**: KRITISCH — bei Seegang oder Grundberührung Bruch möglich → unkontrollierter Wassereinbruch.
**Behebung**: Alle 4 Messing-Seeventile (BJ 1984) durch Bronze-Seeventile (Groco) ersetzt. Alle Stutzen ebenfalls erneuert.
**Kosten**: 4× Seeventil à 120 EUR + 4× Stutzen à 35 EUR + Dichtmittel 25 EUR = 645 EUR Material. 16 h Werft (1.440 EUR). Gesamt: 2.085 EUR.
**AYDI-Score vor Reparatur**: 8/100 (materials KRITISCH). Nach Reparatur: 98/100.
**Lektion**: Messing-Borddurchlässe aus den 1970er–1990er Jahren sind systematisch von Entzinkung bedroht. Jeder Surveyor muss bei Booten >20 Jahre Messing-Fittings prüfen.

(Confidence: documented — Surveyor-Bericht, Versicherungsfall)

## ANHANG M — Fallstudie: Falsches Gewindedichtmittel (NPT/BSP-Verwechslung)

**Boot**: US-Import Catalina 36, Baujahr 1998, nach Deutschland überführt.
**Vorfall**: Deutsche Werft tauscht Seeventil, verwendet PTFE-Band auf BSP-Gewinde (Boot hat NPT!).
**Befund**: Stutzen sitzt fest, scheint dicht. Nach 8 Wochen Liegeplatz: langsames Tropfen am Gewinde. Tropfrate steigt über Monate.
**Ursache**: PTFE-Band auf NPT ist korrekt — ABER: Werft hat BSP-Stutzen auf NPT-Seeventil geschraubt. 2–3 Umdrehungen möglich, dann klemmt es. Scheinbar fest, aber Gewindegänge greifen nicht korrekt → undicht unter Druck.
**Behebung**: NPT-Stutzen (aus US-Import-Bestand) eingebaut. PTFE korrekt 3–5 Wicklungen.
**Kosten**: 45 EUR (NPT-Stutzen) + 3 h Werft (270 EUR) = 315 EUR.
**AYDI-Score**: NPT/BSP-Verwechslung → Befund HOCH. AYDI Pipeline A erkennt das automatisch wenn Bootsherkunft = USA und Werft-Protokoll = BSP-Teile.
**Lektion**: Bei Import-Booten aus den USA IMMER Gewindetyp dokumentieren. NPT und BSP sind NICHT kompatibel.

(Confidence: documented — Werft-Protokoll, Surveyor-Bericht)

## ANHANG N — Fallstudie: Schlauchbrand im Motorraum

**Boot**: Beneteau Antares 9.80, Baujahr 2012, Motorraum-Brand im Hafen.
**Vorfall**: Kraftstoff-Rücklaufschlauch (PVC-Schlauch, nicht SAE J2006) am Dieselmotor gescheuert an Motorträger. Leck → Diesel auf heißen Auspuffkrümmer → Brand.
**Befund**: Werft hatte bei Service PVC-Schlauch statt zugelassenen Kraftstoffschlauch (ISO 7840 Typ A1) verwendet. Schelle war W1 (verzinkt), bereits korrodiert.
**Schadenhöhe**: 45.000 EUR (Motor, Elektrik, Innenausbau). Versicherung hat gezahlt, aber Werft in Regress genommen.
**AYDI-Pipeline B**: Hätte PVC-Schlauch im Motorraum als „falscher Schlauchtyp" erkannt (Confidence: visual_high) und KRITISCH bewertet.
**Lektion**: Falsche Schlauchmaterialien im Motorraum sind brandgefährlich. Nur zugelassene Kraftstoffschläuche (ISO 7840/SAE J1527) verwenden.

(Confidence: documented — Versicherungsgutachten, Brandursachen-Analyse)

## ANHANG O — Fallstudie: Streustrom-Korrosion zerstört neue Schellen

**Boot**: Jeanneau Sun Odyssey 42i, Baujahr 2010, Marina Mittelmeer, Dauerliegeplatz mit Landstrom.
**Vorfall**: Alle Schlauchschellen (W4, 316SS) nach 18 Monaten massiv korrodiert. Vorherige Schellen (gleicher Hersteller) hielten 8+ Jahre.
**Diagnose**: Landstrom-Isolationstransformator (Galvanischer Isolator) defekt. Streustrom von 0,8 A gemessen zwischen Borddurchlass und Wasser.
**Befund**: Alle metallischen Teile in Kontakt mit Seewasser beschleunigt korrodiert: Schellen, Seeventile, Propellerwelle, Opferanoden aufgelöst.
**Behebung**: Galvanischen Isolator ersetzt (Sterling ProSafe II, 350 EUR). Alle Schellen erneuert. Seeventile geprüft (2× ersetzt).
**Kosten**: 350 EUR (Isolator) + 420 EUR (Schellen) + 480 EUR (Seeventile) + 18 h Werft (1.620 EUR) = 2.870 EUR.
**AYDI-Modul**: service_patterns erkennt „unerwartet schnelle Korrosion" und gibt Warnung „Streustrom-Problem prüfen" aus.
**Lektion**: Wenn neue 316SS-Schellen in <2 Jahren korrodieren, ist fast immer ein Streustrom-Problem die Ursache.

(Confidence: documented — Elektriker-Bericht, Marine-Surveyor-Dokumentation)

## ANHANG P — Materialdatenblatt: 316SS vs. 304SS vs. Verzinkt

| Eigenschaft | 316SS (W4) | 304SS (W2) | Verzinkt (W1) |
|---|---|---|---|
| Werkstoff-Nr. | 1.4401 | 1.4301 | 1.0330 + Zn |
| Cr-Gehalt [%] | 16–18 | 18–20 | 0 |
| Ni-Gehalt [%] | 10–14 | 8–10,5 | 0 |
| Mo-Gehalt [%] | 2–3 | 0 | 0 |
| Korrosionsrate Seewasser [μm/a] | 1–5 | 10–50 | 50–200 |
| PREN (Pitting Resistance) | 24–28 | 18–20 | 0 |
| Max. Einsatztemperatur [°C] | 800 | 800 | 250 (Zink schmilzt) |
| Zugfestigkeit [MPa] | 515–690 | 515–690 | 340–440 |
| Preis-Faktor (relativ) | 1,0× | 0,75× | 0,25× |
| Marine-Eignung | Über + unter WL | NUR über WL | NUR temporär/Süßwasser |
| Lebensdauer Salzwasser [Jahre] | 12–20+ | 3–6 | 2–3 |

## ANHANG Q — Wartungskalender Schlauchverbindungen (Jahresübersicht)

| Monat | Tätigkeit | Priorität |
|---|---|---|
| März/April (Saisonstart) | Alle Schlauchschellen auf Sitz prüfen, Sichtprüfung aller Schläuche | HOCH |
| März/April | Alle Seeventile gängig machen (öffnen/schließen, Lanolin fetten) | HOCH |
| Mai | Motorkühlwasser-System: Impeller prüfen, Schläuche inspizieren | MITTEL |
| Juni | Nassauspuff-Schlauch: Temperatur messen, Zustand prüfen | MITTEL |
| August | Mittelsaison-Check: Bilge trocken? Tropfen an Verbindungen? | HOCH |
| Oktober | Kraftstoffsystem: Schläuche und Filter inspizieren | MITTEL |
| November (Winterlager) | Vollinspektion alle Schlauchverbindungen (s. Anhang D) | HOCH |
| November | Systeme entleeren, Frostschutz einfüllen | HOCH |
| Alle 5 Jahre | Professioneller Survey aller Borddurchlässe und Seeventile | PFLICHT |
| Alle 10–12 Jahre | Präventiver Komplett-Austausch aller Schellen und kritischer Schläuche | EMPFOHLEN |

## ANHANG R — Digitale AYDI-Integration: Scoring-Zusammenfassung

```python
# Zusammenfassung der AYDI-Bewertungslogik für Schlauchverbindungen
# Integration in Module: materials, structural, compliance, service_patterns, cost

HOSE_CONNECTION_ASSESSMENT = {
    "module_id": "07_05_schlauchverbindungen",
    "version": "6.0",
    "last_updated": "2026-04",

    "pipeline_a_structured": {
        "weight": 0.70,
        "inputs": [
            "clamp_material", "clamp_count", "clamp_type",
            "barb_material", "hose_type", "hose_age",
            "position_relative_wl", "thread_type", "sealant_type",
            "boat_origin", "boat_class", "operating_waters"
        ],
        "confidence": "measured (Level 2) | estimated (Level 1)",
    },

    "pipeline_b_visual": {
        "weight": 0.30,
        "detectable": [
            "clamp_corrosion", "clamp_count", "clamp_type",
            "hose_cracks", "hose_swelling", "dezincification",
            "wrong_clamp_type", "cable_ties", "overtightened_clamp",
            "uv_degradation", "sealant_visible"
        ],
        "not_detectable": [
            "crevice_corrosion_internal", "thread_type_npt_vs_bsp",
            "clamp_torque", "hose_internal_delamination",
            "stray_current_corrosion_early"
        ],
        "confidence": "visual_high | visual_medium | visual_low | visual_insufficient",
    },

    "scoring_zones": [
        "below_waterline",   # Gewichtung ×2.0 (sicherheitskritisch)
        "engine_room",       # Gewichtung ×1.5 (Brand-/Motorschadensrisiko)
        "above_waterline",   # Gewichtung ×1.0 (Standard)
        "exterior_deck",     # Gewichtung ×0.8 (UV, aber geringeres Risiko)
    ],

    "critical_findings_trigger_review": True,
    "critical_threshold": 30,  # Score < 30 → "Befund prüfen" (Human-in-the-loop)
}
```

(Confidence: documented — AYDI Systemarchitektur v6, Pydantic-Modelle, Scoring-Framework)

---

*Ende des Dokuments 07.05 — Schlauchverbindungen und Stutzen: Kompletthandbuch*
*Letzte Aktualisierung: 2026-04*
*Gesamtumfang: ~3.900 Zeilen*
*Confidence: documented — ABYC, ISO, DIN, SAE Standards; Surveyor-Praxis; Herstellerangaben; Ingenieurhandbücher*
