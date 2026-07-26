# 18_07 — Getriebe und Saildrive — Typen, Wartung und Troubleshooting

> **Modulkontext**: structural, materials, compliance, service_patterns, cost, production
> **Confidence-Klassen**: measured | calculated | visual_high | visual_medium | estimated | documented | benchmark
> **Pydantic-Hinweis**: `model_config = {"from_attributes": True}` — NIEMALS `class Config`
> **Letzte Aktualisierung**: 2026-04

---

```yaml
titel: "Getriebe und Saildrive — Typen, Wartung und Troubleshooting"
kategorie: "Motoren und Antrieb"
unterkategorie: "Getriebe und Saildrive"
version: "2.0"
letzte_aktualisierung: "2026-04"
autor: "AYDI Maritime Knowledge Base"
```

---

## Inhaltsverzeichnis

1. Grundlagen und Definitionen
2. Normen und Regularien
3. Wendegetriebe — Hydraulisch vs. Mechanisch
4. ZF Marine (inkl. Hurth-Serie)
5. Technodrive-Getriebe
6. Yanmar KM-Serie
7. Volvo Penta MS/HS-Getriebe
8. PRM / Newage Getriebe
9. Borg Warner Velvet Drive
10. Weitere Hersteller und Nischengetriebe
11. Saildrive — Grundlagen und Systeme
12. Volvo Penta Saildrive (120S / 130S / 150S)
13. Yanmar Saildrive (SD20 / SD25 / SD50 / SD60)
14. ZF Saildrive (SD100 / SD200)
15. Untersetzungsverhältnis und Propellerberechnung
16. Getriebeöl — ATF vs. Gear Oil vs. Synthetik
17. Schaltgestänge und Bowdenzüge
18. Getriebe-Alignment
19. Saildrive-Anoden (Zink vs. Aluminium)
20. Saildrive-Membran — Lebensdauer und Austausch
21. Propellerintegration — Flexofold / Gori / Volvo
22. Fehlerbilder und Diagnostik
23. Troubleshooting-Leitfäden
24. Fallstudien
25. OEM-Spezifikationen nach Bootshersteller
26. Einbau- und Austausch-Anleitungen
27. Wartung und Lebensdauer
28. Weltweite Bezugsquellen
29. Preisvergleich
30. Forum-Erfahrungsberichte
31. YouTube-Ressourcen
32. Experten-Referenzen
33. FAQ
34. Glossar
35. Pydantic v2 Modelle
36. Anhänge

---

## 1. Grundlagen und Definitionen

### 1.1 Was ist ein Wendegetriebe?

Das Wendegetriebe (engl. marine gearbox, marine gear, marine transmission) hat im Bootsbau eine dreifache Funktion: Erstens kehrt es die Drehrichtung der Abtriebswelle um, sodass Vorwärts- und Rückwärtsfahrt möglich sind. Zweitens reduziert es die Motordrehzahl auf eine für den Propeller optimale Drehzahl (Untersetzung). Drittens fungiert es als Kupplung, um den Motor vom Propeller zu trennen (Leerlauf/Neutral).

Im Gegensatz zum Automobil gibt es auf Booten keine Mehrgangschaltung — das Wendegetriebe hat genau drei Stellungen: Vorwärts, Neutral, Rückwärts. Die Untersetzung ist fest und wird bei Kauf/Einbau gewählt.

(Confidence: documented)

### 1.2 Was ist ein Saildrive?

Der Saildrive (deutsch: Segelantrieb) ist ein integriertes Antriebs-System, bei dem Motor und Getriebeeinheit direkt über eine Öffnung im Rumpfboden mit dem Propeller verbunden sind. Im Gegensatz zur konventionellen Wellenanlage entfällt die lange Propellerwelle, das Stevenrohr, die Stopfbuchse und der Wellenbock. Der Motor sitzt direkt über der Rumpfdurchführung, und ein vertikales Getriebebein (ähnlich einem Z-Antrieb) ragt durch den Rumpf nach unten.

Vorteile: kompakterer Einbau, weniger Vibrationen, geringerer Widerstand, leichtere Montage.
Nachteile: Rumpfdurchbruch als potenzielle Leckstelle (Membran!), aufwändigerer Antifouling-Schutz, begrenzte Leistungsklassen.

(Confidence: documented)

### 1.3 Systemübersicht — Antriebskonzepte

| Antriebskonzept | Englisch | Typischer Einsatz | Leistungsbereich | Preisniveau |
|---|---|---|---|---|
| Wellenanlage + Wendegetriebe | Shaft drive + marine gearbox | Segel- und Motorboote aller Größen | 5–5.000+ PS | €€–€€€€ |
| Saildrive | Saildrive | Segelboote 25–55 ft | 10–110 PS | €€€ |
| Z-Antrieb (Sterndrive) | Sterndrive | Motorboote, Sportboote | 100–600 PS | €€€ |
| Pod-Antrieb | Pod drive (IPS, Zeus) | Motoryachten 35+ ft | 200–1.500 PS | €€€€ |
| Jet-Antrieb | Waterjet | Schnelle Boote, Tenderboote | 50–5.000+ PS | €€€€ |
| Elektrisch direkt | Direct electric | Segelboote, leise Boote | 2–100 kW | €€€€ |

(Confidence: documented)

### 1.4 Kernkomponenten eines Wendegetriebes

| Komponente | Englisch | Funktion |
|---|---|---|
| Eingangswelle | Input shaft | Verbindung zum Motor (Schwungscheibe/Kupplungsgehäuse) |
| Ausgangswelle | Output shaft | Verbindung zur Propellerwelle (Flansch oder Konus) |
| Kupplungspaket Vorwärts | Forward clutch pack | Kupplung für Vorwärtsfahrt |
| Kupplungspaket Rückwärts | Reverse clutch pack | Kupplung für Rückwärtsfahrt |
| Planetengetriebe / Stirnradgetriebe | Planetary / Spur gear | Untersetzungsmechanismus |
| Ölpumpe | Oil pump | Druckaufbau für hydraulische Kupplung |
| Schaltmechanismus | Shift mechanism | Betätigung Vorwärts/Neutral/Rückwärts |
| Getriebegehäuse | Gearbox housing | Aluminiumguss, trägt alle Komponenten |
| Ölkühler | Oil cooler | Kühlung durch Seewasser oder Kühlkreislauf |
| PTO (Power Take-Off) | PTO | Optionaler Nebenantrieb (Generator, Hydraulik) |

(Confidence: documented)

### 1.5 Kernkomponenten eines Saildrives

| Komponente | Englisch | Funktion |
|---|---|---|
| Obere Einheit | Upper unit | Getriebegehäuse mit Kupplungsmechanismus |
| Untere Einheit | Lower unit | Kegelradgetriebe + Propellerwelle |
| Membran / Manschette | Diaphragm / Bellows | Abdichtung des Rumpfdurchbruchs (KRITISCH!) |
| Anodenschutz | Anode protection | Zink- oder Aluminiumanoden gegen Korrosion |
| Getriebeöl obere Einheit | Upper gear oil | Schmierung oberes Getriebe |
| Getriebeöl untere Einheit | Lower gear oil | Schmierung Kegelrad/Propellerwelle |
| Propellernabe | Propeller hub | Aufnahme des Propellers |
| Schaltmechanismus | Shift mechanism | Bowdenzug oder elektronisch |
| Kühlwassereinlass | Cooling water inlet | Seewasseraufnahme für Motorkühlung |

(Confidence: documented)

### 1.6 Historischer Kontext

Die Geschichte der Wendegetriebe im Bootsbau:

| Zeitraum | Entwicklung |
|---|---|
| 1920er–1950er | Mechanische Klauenkupplungen, einfache Stirnradgetriebe |
| 1950er–1960er | Hurth (später ZF) führt hydraulische Kupplungen ein |
| 1960er–1970er | Borg Warner Velvet Drive etabliert sich in den USA |
| 1970er | Volvo Penta entwickelt den ersten Saildrive (Volvo Saildrive 100) |
| 1980er | ZF übernimmt Hurth, standardisiert Getriebepalette |
| 1990er | Yanmar bringt eigene SD-Saildrive-Serie, PRM wächst |
| 2000er | Elektronische Schaltung, integrierte Motorsteuerung |
| 2010er | Hybridantriebe, Saildrive für E-Motoren |
| 2020er | ZF Saildrive 100/200, vollintegrierte Systeme |

(Confidence: documented)

---

## 2. Normen und Regularien

### 2.1 Relevante ISO-Normen

| Norm | Titel | Relevanz für Getriebe/Saildrive |
|---|---|---|
| ISO 12217 | Stabilität | Gewichtsverteilung Antriebsstrang, Einfluss auf Trimm |
| ISO 9094 | Brandschutz | Abstand Getriebe zu brennbaren Materialien, Öltemperatur |
| ISO 10133 | Elektrische Anlagen LV DC | Bonding der Antriebswelle, galvanischer Schutz |
| ISO 11812 | Cockpits | Auswirkung Saildrive-Öffnung auf Rumpfintegrität |
| ISO 8665 | Motorleistung | Nennleistung am Getriebe-Ausgang |
| ISO 7840 | Kraftstoffschläuche | Nicht direkt, aber Zugänglichkeit im Maschinenraum |
| ISO 16147 | Innenbord-Dieselmotoren | Motor-Getriebe-Verbindung, Alignment-Anforderungen |
| ISO 8469 | Kraftstoffschläuche nicht brennbar | Abstand zu Getriebebereich |

(Confidence: documented)

### 2.2 CE-Kategorien und Antriebsauswirkungen

| CE-Kategorie | Relevante Anforderungen |
|---|---|
| A (Ozean) | Redundante Bilgepumpe bei Saildrive, verstärkter Anodenschutz, Saildrive-Membran alle 5 Jahre empfohlen |
| B (Offshore) | Standard-Wartungsintervalle, Saildrive-Membran alle 7 Jahre |
| C (Küste) | Standard-Wartungsintervalle |
| D (Geschützt) | Minimale Zusatzanforderungen |

(Confidence: documented)

### 2.3 Herstellerübergreifende Standards

| Standard | Inhalt | Anwendung |
|---|---|---|
| SAE J617 | Getriebe-Anschlussflansch (SAE-Gehäusegrößen) | Kompatibilität Motor↔Getriebe |
| SAE J620 | Schwungscheiben-Abmessungen | Kupplungsadaption |
| ABYC P-4 | Installations-Standard Innenbordmotoren | Alignment, Fundamentierung |
| ABYC E-2 | Galvanischer Schutz | Anodenspezifikation für Saildrive |
| GL / DNV | Klassifizierungsregeln | Superyacht-Getriebe, Zertifizierung |

(Confidence: documented)

### 2.4 Getriebeöl-Spezifikationen

| Spezifikation | Beschreibung | Typische Anwendung |
|---|---|---|
| ATF Dexron III | Automatikgetriebeöl, rot | ZF 5/10/12/15 (hydraulisch) |
| ATF Dexron VI | Nachfolger Dexron III, vollsynthetisch | Neuere ZF-Getriebe |
| SAE 80W-90 GL-4 | Hypoidgetriebeöl | Mechanische Getriebe, Saildrive-Untereinheit |
| SAE 75W-90 GL-5 | Synthetisches Hypoidöl | PRM, einige Saildrives |
| SAE 30 Motoröl | Einbereichs-Motoröl | Borg Warner Velvet Drive (71C/72C) |
| Volvo Penta IPS Oil | Spezialöl | Volvo Saildrive-Untereinheit |
| Yanmar Premium Gear Oil | Herstellerspezifisch | Yanmar KM- und SD-Serie |

(Confidence: documented)

---

## 3. Wendegetriebe — Hydraulisch vs. Mechanisch

### 3.1 Mechanische Kupplung (Klauenkupplung / Dog Clutch)

Bei der mechanischen Kupplung greifen Klauen (Zähne) direkt ineinander. Das Schalten erfolgt durch mechanisches Verschieben einer Schaltmuffe.

**Vorteile:**
- Einfacher Aufbau, wenig Verschleißteile
- Kein Öldrucksystem notwendig
- Günstig in Anschaffung und Wartung
- Zuverlässig bei richtigem Schalten

**Nachteile:**
- Schalten nur bei niedriger Drehzahl möglich (unter 1.000 U/min)
- Ruckartige Schaltung, mechanische Belastung
- Kein stufenloses Einkuppeln möglich
- Kann bei Fehlbedienung beschädigt werden
- Höhere Belastung des Antriebsstrangs

**Typische Vertreter:**
- Alte Hurth-Getriebe (HBW 5, HBW 10)
- PRM 80 (mechanisch)
- Diverse Bootsgetriebe bis ca. 1980

(Confidence: documented)

### 3.2 Hydraulische Kupplung (Multi-Disc Clutch)

Bei der hydraulischen Kupplung werden Lamellenpakete (abwechselnd Stahl- und Reiblamellen) durch Öldruck zusammengepresst. Die Ölpumpe wird vom Motor angetrieben.

**Vorteile:**
- Sanftes, ruckfreies Schalten bei jeder Drehzahl
- Schlupf beim Einkuppeln schont Antriebsstrang
- Schalten unter Last möglich
- Längere Lebensdauer der Kupplungsbauteile
- Bessere Manövrierbarkeit im Hafen

**Nachteile:**
- Komplexerer Aufbau
- Ölpumpe als zusätzliche Verschleißquelle
- Ölqualität und -menge kritisch
- Teurer in Anschaffung
- Ölkühlung erforderlich bei höherer Leistung

**Typische Vertreter:**
- ZF 10M, ZF 12M, ZF 15M, ZF 25, ZF 45
- Technodrive TMC40, TMC60
- Yanmar KM2P, KM3P, KM4A
- Borg Warner Velvet Drive 71C, 72C

(Confidence: documented)

### 3.3 Vergleichsmatrix

| Kriterium | Mechanisch (Klauen) | Hydraulisch (Lamellen) |
|---|---|---|
| Schaltkomfort | Ruckartig | Sanft, stufenlos |
| Schalten unter Last | Nicht empfohlen | Ja |
| Max. Schaltdrehzahl | < 1.000 U/min | Jede Drehzahl |
| Ölwechsel-Intervall | Alle 500 Bh oder jährlich | Alle 200–500 Bh oder jährlich |
| Typisches Öl | SAE 80W-90 GL-4 | ATF Dexron III/VI |
| Lebensdauer Kupplung | 3.000–8.000 Bh | 2.000–5.000 Bh (Lamellen) |
| Reparaturkosten | Günstig (€200–600) | Mittel (€400–1.500) |
| Geeignet für | Kleine Segelboote, Klassiker | Alle modernen Boote |
| Gewicht (30 PS Klasse) | 8–15 kg | 12–25 kg |
| Preis (30 PS Klasse) | €400–800 | €800–2.500 |

(Confidence: documented)

### 3.4 Kupplungslamellen — Verschleiß und Toleranzen

**Hydraulische Lamellenpakete:**

| Parameter | Neuzustand | Verschleißgrenze | Messmethode |
|---|---|---|---|
| Lamellenstärke (Stahl) | 1,5–2,0 mm | Min. 1,3 mm | Messschieber |
| Lamellenstärke (Reib) | 2,0–2,5 mm | Min. 1,5 mm | Messschieber |
| Paketmaß Vorwärts | Herstellerspezifisch | ±0,2 mm vom Sollwert | Tiefenmaß |
| Paketmaß Rückwärts | Herstellerspezifisch | ±0,2 mm vom Sollwert | Tiefenmaß |
| Reibbelag-Oberfläche | Gleichmäßig, Rillen sichtbar | Glasig, verbrannt, ungleichmäßig | Sichtprüfung |
| Stahllamellen-Verzug | Plan (< 0,05 mm) | > 0,1 mm = tauschen | Glasplatte + Fühlerblatt |

(Confidence: measured)

### 3.5 Öldrucksystem (Hydraulische Getriebe)

| Parameter | Sollwert | Toleranz | Messung |
|---|---|---|---|
| Öldruck Vorwärts | 8–15 bar (herstellerabhängig) | ±1 bar | Manometer am Messanschluss |
| Öldruck Rückwärts | 8–15 bar | ±1 bar | Manometer am Messanschluss |
| Öldruck Neutral | 0 bar | — | Druckfrei |
| Öltemperatur Betrieb | 60–80 °C | Max. 100 °C | Infrarot-Thermometer |
| Öltemperatur Alarm | > 110 °C | — | Öltemperaturschalter |
| Ölpumpen-Fördervolumen | 2–10 l/min (größenabhängig) | — | Nicht im Einbau messbar |
| Filterfeinheit | 25–40 µm (integriert) | — | Herstellervorgabe |

(Confidence: measured)

---

## 4. ZF Marine (inkl. Hurth-Serie)

### 4.1 Geschichte und Hintergrund

ZF Friedrichshafen übernahm 1969 die Hurth-Marinegetriebe und wurde zum weltweit führenden Hersteller von Bootsgetrieben. Die ehemalige Hurth-Bezeichnung (HBW = Hurth Bootswendegetriebe) findet sich noch auf vielen älteren Booten. Seit den 1990er-Jahren firmieren alle Getriebe unter ZF Marine.

Standorte: Padova (Italien), Friedrichshafen (Deutschland), China (Lizenzfertigung).
Marktanteil Segelboot-Getriebe: geschätzt > 60 % weltweit.

(Confidence: documented)

### 4.2 ZF 5M (ehem. Hurth HBW 5)

| Parameter | Wert |
|---|---|
| Kupplungstyp | Mechanisch (Klauenkupplung) |
| Max. Eingangsleistung | 16 PS (12 kW) bei 4.000 U/min |
| Untersetzungsverhältnisse | 2,14:1 / 2,62:1 |
| Drehrichtung Eingang | Linksdrehend (standard) |
| Gewicht | 9,5 kg |
| Öl | SAE 80W-90 GL-4 |
| Ölmenge | 0,25 l |
| Ölwechselintervall | Alle 500 Bh oder jährlich |
| Abtriebsflansch | ⌀25 mm Konus |
| SAE-Gehäuse | Kein Standard-SAE |
| Produktionszeitraum | ca. 1965–1995 |
| Neupreis (historisch) | €500–700 |
| Gebrauchtpreis (2026) | €300–500 |
| Typische Motoren | Volvo MD2B, Yanmar 1GM, Bukh DV10 |

**Bekannte Probleme ZF 5M:**
- Schaltklauen-Verschleiß bei häufigem Schalten unter Drehzahl
- Simmerring-Leckage an Abtriebswelle
- Korrosion Getriebegehäuse (Aluminium) bei Salzwasserkontakt
- Ersatzteilversorgung zunehmend schwierig

(Confidence: documented)

### 4.3 ZF 10M (ehem. Hurth HBW 10)

| Parameter | Wert |
|---|---|
| Kupplungstyp | Hydraulisch (Mehrscheibenkupplung) |
| Max. Eingangsleistung | 30 PS (22 kW) bei 3.600 U/min |
| Untersetzungsverhältnisse | 1,97:1 / 2,14:1 / 2,63:1 |
| Drehrichtung Eingang | Links- oder Rechtsdrehend (Ausführung A/B) |
| Gewicht | 17 kg |
| Öl | ATF Dexron III (oder Dexron VI) |
| Ölmenge | 0,65 l |
| Ölwechselintervall | Alle 250 Bh oder jährlich |
| Abtriebsflansch | ⌀25 mm Konus oder Flansch (Option) |
| SAE-Gehäuse | SAE 5 (Bellhousing) |
| Produktionszeitraum | ca. 1975–2010 |
| Neupreis (ca. 2010) | €1.200–1.600 |
| Gebrauchtpreis (2026) | €500–900 |
| Typische Motoren | Yanmar 2GM20, Volvo MD2020, Nanni 2.10 |

**Bekannte Probleme ZF 10M:**
- Ölpumpen-Verschleiß nach > 3.000 Bh → Druckabfall → Kupplung rutscht
- Schaltventil-Korrosion bei Wassereinbruch über Belüftung
- Lamellenverschleiß bei häufigem Manövrieren (Charterbetrieb)
- Wellendichtring Abtrieb undicht (Standard-Verschleiß)
- Ölkühler-Leckage (interne Undichtigkeit → Wasser im Öl)

(Confidence: documented)

### 4.4 ZF 12M (ehem. Hurth HBW 100/125)

| Parameter | Wert |
|---|---|
| Kupplungstyp | Hydraulisch (Mehrscheibenkupplung) |
| Max. Eingangsleistung | 45 PS (33 kW) bei 3.600 U/min |
| Untersetzungsverhältnisse | 2,14:1 / 2,63:1 / 3,05:1 |
| Drehrichtung Eingang | Links- oder Rechtsdrehend |
| Gewicht | 22 kg |
| Öl | ATF Dexron III/VI |
| Ölmenge | 0,8 l |
| Ölwechselintervall | Alle 250 Bh oder jährlich |
| Abtriebsflansch | ⌀30 mm Konus oder SAE-Flansch |
| SAE-Gehäuse | SAE 4 / SAE 5 |
| Produktionszeitraum | ca. 1980–2015 |
| Neupreis (ca. 2015) | €1.600–2.200 |
| Gebrauchtpreis (2026) | €700–1.200 |
| Typische Motoren | Yanmar 3GM30, Volvo D1-30, Nanni 3.75 |

**Bekannte Probleme ZF 12M:**
- Identisch zu ZF 10M, plus:
- Abtriebsflansch-Korrosion bei unzureichendem Anodenschutz
- Ölpumpenantriebsverzahnung verschleißt bei mangelhafter Ölpflege
- Schaltgestänge-Spiel nach > 5.000 Bh

(Confidence: documented)

### 4.5 ZF 15M/MA/MIV

| Parameter | ZF 15M | ZF 15MA | ZF 15MIV |
|---|---|---|---|
| Kupplungstyp | Hydraulisch | Hydraulisch | Hydraulisch + Klauenkupplung |
| Max. Eingangsleistung | 60 PS (44 kW) | 60 PS (44 kW) | 75 PS (55 kW) |
| Untersetzungsverhältnisse | 2,14:1 / 2,63:1 | 2,14:1 / 2,63:1 / 3,05:1 | 1,88:1 / 2,14:1 / 2,63:1 |
| Gewicht | 27 kg | 32 kg | 35 kg |
| Öl | ATF Dexron III/VI | ATF Dexron III/VI | ATF Dexron III/VI |
| Ölmenge | 1,0 l | 1,2 l | 1,3 l |
| Abtriebsflansch | Konus ⌀30/35 mm | Flansch SAE / Konus | Flansch SAE |
| SAE-Gehäuse | SAE 3 / SAE 4 | SAE 3 / SAE 4 | SAE 3 |
| Neupreis (2026) | €2.200–2.800 | €2.500–3.200 | €3.000–3.800 |
| Typische Motoren | Yanmar 3JH/4JH, Volvo D1-30/D2-40 | Diverse 40–60 PS | Volvo D2-55/D2-75 |

**ZF 15MIV Besonderheit:**
Das MIV-Modell kombiniert hydraulische Lamellenkupplung für Vorwärts mit einer mechanischen Klauenkupplung für Rückwärts. Vorteil: reduzierter Schlupf im Vorwärtsgang bei höherer Leistung. Nachteil: Rückwärtsschaltung nur bei niedriger Drehzahl.

(Confidence: documented)

### 4.6 ZF 25 / ZF 25A

| Parameter | ZF 25 | ZF 25A |
|---|---|---|
| Kupplungstyp | Hydraulisch | Hydraulisch |
| Max. Eingangsleistung | 130 PS (96 kW) | 175 PS (129 kW) |
| Untersetzungsverhältnisse | 1,93:1 / 2,29:1 / 2,54:1 / 3,02:1 | 1,93:1 / 2,29:1 / 2,54:1 / 3,02:1 |
| Drehrichtung | Links oder Rechts | Links oder Rechts |
| Gewicht | 48 kg | 55 kg |
| Öl | ATF Dexron III/VI | ATF Dexron III/VI |
| Ölmenge | 1,8 l | 2,2 l |
| Ölkühler | Seewassergekühlt (Standard) | Seewassergekühlt (Standard) |
| Abtriebsflansch | SAE-Flansch / Konus ⌀35 mm | SAE-Flansch / Konus ⌀40 mm |
| SAE-Gehäuse | SAE 2 / SAE 3 | SAE 2 / SAE 3 |
| Neupreis (2026) | €3.500–4.500 | €4.000–5.200 |
| Typische Motoren | Yanmar 4JH57/80, Volvo D2-75, Nanni N4.100 | Diverse 100–175 PS |

(Confidence: documented)

### 4.7 ZF 45 / ZF 45A / ZF 45-1

| Parameter | ZF 45 | ZF 45A | ZF 45-1 |
|---|---|---|---|
| Kupplungstyp | Hydraulisch | Hydraulisch | Hydraulisch |
| Max. Eingangsleistung | 240 PS (176 kW) | 340 PS (250 kW) | 440 PS (324 kW) |
| Untersetzungsverhältnisse | 1,52:1 – 3,03:1 | 1,52:1 – 3,03:1 | 1,26:1 – 3,03:1 |
| Gewicht | 80 kg | 95 kg | 110 kg |
| Öl | ATF Dexron III/VI | ATF Dexron III/VI | ATF Dexron III/VI |
| Ölmenge | 3,5 l | 4,0 l | 4,5 l |
| Ölkühler | Seewasser, integriert | Seewasser, integriert | Seewasser, integriert |
| Abtriebsflansch | SAE-Flansch ⌀100 mm | SAE-Flansch ⌀100–120 mm | SAE-Flansch ⌀120 mm |
| SAE-Gehäuse | SAE 1 / SAE 2 | SAE 1 / SAE 2 | SAE 1 |
| PTO Option | Ja (Front-PTO) | Ja (Front- und Rück-PTO) | Ja |
| Neupreis (2026) | €5.500–7.000 | €7.000–9.000 | €9.000–12.000 |
| Typische Motoren | Yanmar 6LY, Volvo D3, diverse 150–250 PS | Cummins QSB, Volvo D4 | Cummins QSC, CAT |

**Bekannte Probleme ZF 25/45-Serie:**
- Ölkühler-Lochfraß nach 10+ Jahren → Seewasser im Getriebeöl (KRITISCH!)
- Sofortmaßnahme: Öl kontrollieren — milchig = Wasser drin → sofort stoppen
- Lamellenverschleiß bei Schleppbetrieb (Sportfischer, Trawler)
- Anschluss-Adapter-Korrosion bei Seewasserkühler
- Schaltventil-Block-Korrosion bei langer Standzeit

(Confidence: documented)

### 4.8 ZF Großgetriebe (ZF 63/80/85/220/280/325/500)

Für Motoryachten ab 200 PS bis Superyacht-Klasse:

| Modell | Max. Leistung | Gewicht | Untersetzung | Typischer Einsatz | Neupreis (ca.) |
|---|---|---|---|---|---|
| ZF 63A | 480 PS | 130 kg | 1,26:1–3,50:1 | Motoryachten 40–50 ft | €12.000–16.000 |
| ZF 80A | 600 PS | 180 kg | 1,50:1–4,00:1 | Motoryachten 50–60 ft | €16.000–22.000 |
| ZF 85A | 750 PS | 200 kg | 1,50:1–4,50:1 | Motoryachten 55–70 ft | €20.000–28.000 |
| ZF 220A | 1.100 PS | 320 kg | 1,50:1–5,00:1 | Superyachten 60–80 ft | €30.000–45.000 |
| ZF 280A | 1.500 PS | 400 kg | 1,50:1–5,47:1 | Superyachten 70–90 ft | €45.000–65.000 |
| ZF 325A | 1.800 PS | 480 kg | 1,50:1–6,00:1 | Superyachten 80+ ft | €60.000–85.000 |
| ZF 500A | 3.000 PS | 750 kg | 2,00:1–6,50:1 | Megayachten | €100.000+ |

(Confidence: documented / benchmark)

### 4.9 ZF Ersatzteilnummern und Wartungskits

**ZF 10M/12M Standard-Wartungskit:**

| Teil | ZF-Teilenummer | Beschreibung | Preis (ca.) |
|---|---|---|---|
| Ölfilter (falls vorhanden) | 3312 199 031 | Ölsieb intern | €25–40 |
| Wellendichtring Abtrieb | 3311 304 022 | Simmerring ⌀25×40×7 | €15–25 |
| Wellendichtring Antrieb | 3311 304 015 | Simmerring Eingangswelle | €15–25 |
| Lamellen-Kit Vorwärts | 3312 199 005 | Reib- + Stahllamellen Satz | €180–280 |
| Lamellen-Kit Rückwärts | 3312 199 006 | Reib- + Stahllamellen Satz | €180–280 |
| Dichtungssatz komplett | 3312 199 010 | Alle Dichtungen + O-Ringe | €80–120 |
| Ölpumpe | 3312 199 020 | Innenzahnradpumpe | €250–400 |

**ZF 25/45 Standard-Wartungskit:**

| Teil | ZF-Teilenummer | Beschreibung | Preis (ca.) |
|---|---|---|---|
| Ölfilter | 3213 308 019 | Spin-on Ölfilter | €20–35 |
| Ölkühler | 3213 308 050 | Plattenwärmetauscher | €350–600 |
| Wellendichtring Abtrieb | 3213 304 022 | Simmerring ⌀35×52×7 | €20–35 |
| Lamellen-Kit V/R komplett | 3213 199 005/006 | Komplettsatz | €400–700 |
| Dichtungssatz komplett | 3213 199 010 | Alle Dichtungen | €120–200 |
| Schaltventil | 3213 199 030 | Schaltventilblock | €300–500 |

(Confidence: documented / benchmark)

---

## 5. Technodrive-Getriebe

### 5.1 Überblick

Technodrive (Techno Drive Marine, ein Handelsname von Velvet Drive / BorgWarner / Twin Disc Lineage) fertigt kompakte Wendegetriebe speziell für kleine bis mittlere Segelbootmotoren. Hauptsitz: Niederlande. Die TMC-Serie ist weit verbreitet als OEM-Getriebe für Nanni, Beta Marine und Vetus.

(Confidence: documented)

### 5.2 TMC40 (TM40)

| Parameter | Wert |
|---|---|
| Kupplungstyp | Hydraulisch (Lamellen) |
| Max. Eingangsleistung | 40 PS (29 kW) bei 3.600 U/min |
| Untersetzungsverhältnisse | 2,00:1 / 2,47:1 |
| Drehrichtung | Links oder Rechts |
| Gewicht | 15 kg |
| Öl | ATF Dexron III/VI |
| Ölmenge | 0,6 l |
| Ölwechselintervall | Alle 250 Bh oder jährlich |
| Abtriebsflansch | ⌀25 mm Konus |
| SAE-Gehäuse | SAE 5 |
| Neupreis (2026) | €1.200–1.600 |
| Typische Motoren | Nanni 2.10/2.14, Beta 14/20, Vetus M2.06 |

(Confidence: documented)

### 5.3 TMC60 (TM60)

| Parameter | Wert |
|---|---|
| Kupplungstyp | Hydraulisch (Lamellen) |
| Max. Eingangsleistung | 70 PS (51 kW) bei 3.600 U/min |
| Untersetzungsverhältnisse | 2,00:1 / 2,47:1 / 2,94:1 |
| Drehrichtung | Links oder Rechts |
| Gewicht | 23 kg |
| Öl | ATF Dexron III/VI |
| Ölmenge | 0,9 l |
| Ölwechselintervall | Alle 250 Bh oder jährlich |
| Abtriebsflansch | ⌀30 mm Konus oder Flansch |
| SAE-Gehäuse | SAE 4 / SAE 5 |
| Neupreis (2026) | €1.600–2.200 |
| Typische Motoren | Nanni 3.75/N4.38, Beta 30/38, Vetus M3.28/M4.17 |

(Confidence: documented)

### 5.4 TMC93 / TMC260

| Parameter | TMC93 | TMC260 |
|---|---|---|
| Kupplungstyp | Hydraulisch | Hydraulisch |
| Max. Eingangsleistung | 115 PS (85 kW) | 330 PS (243 kW) |
| Untersetzungsverhältnisse | 2,00:1 / 2,47:1 / 3,00:1 | 1,50:1 – 3,44:1 |
| Gewicht | 38 kg | 95 kg |
| Öl | ATF Dexron III/VI | ATF Dexron III/VI |
| Ölmenge | 1,5 l | 3,5 l |
| Neupreis (2026) | €2.800–3.500 | €6.000–8.000 |

(Confidence: documented)

### 5.5 Bekannte Probleme Technodrive

| Problem | Modell | Ursache | Lösung |
|---|---|---|---|
| Schaltung „rutscht" bei warmem Öl | TMC40/60 | Lamellenverschleiß, Öldruck zu niedrig | Lamellenwechsel, Ölpumpe prüfen |
| Ölleckage Eingangswelle | TMC40 | Simmerring verschlissen | Simmerring tauschen (€15–25) |
| Vibrationen nach Ölwechsel | TMC60 | Falsches Öl (Motoröl statt ATF) | Öl wechseln auf ATF Dexron |
| Schaltgestänge schwergängig | Alle | Bowdenzug korrodiert, Hebel fest | Bowdenzug tauschen, Hebel lösen |
| Geräusche im Neutral | TMC40/60 | Zahnflankenspiel (normal bei kalt) | Normal wenn < 60 dB, sonst prüfen |

(Confidence: documented)

---

## 6. Yanmar KM-Serie

### 6.1 Überblick

Yanmar baut eigene Wendegetriebe für seine Marinediesel. Die KM-Serie (Kikai Marine) ist speziell auf Yanmar-Motoren abgestimmt und wird als Paket verkauft. Separate Erhältlichkeit ist eingeschränkt.

(Confidence: documented)

### 6.2 KM2P

| Parameter | Wert |
|---|---|
| Kupplungstyp | Hydraulisch (Lamellen) |
| Max. Eingangsleistung | 30 PS (22 kW) |
| Untersetzungsverhältnisse | 2,21:1 / 2,62:1 |
| Drehrichtung | Linksdrehend (Standard Yanmar) |
| Gewicht | 18 kg (im Motor integriert) |
| Öl | Yanmar Premium Gear Oil oder ATF Dexron III |
| Ölmenge | 0,35 l (separater Ölkreislauf) |
| Ölwechselintervall | Alle 250 Bh oder jährlich |
| Abtriebsflansch | Yanmar-Flansch oder Konus ⌀25 mm |
| Neupreis (als Einzelteil) | €1.800–2.400 (kaum separat erhältlich) |
| Typische Motoren | Yanmar 2YM20, 3YM20, 2GM20F |

(Confidence: documented)

### 6.3 KM3P

| Parameter | Wert |
|---|---|
| Kupplungstyp | Hydraulisch (Lamellen) |
| Max. Eingangsleistung | 50 PS (37 kW) |
| Untersetzungsverhältnisse | 2,21:1 / 2,62:1 / 3,04:1 |
| Gewicht | 24 kg |
| Öl | Yanmar Premium Gear Oil oder ATF Dexron III |
| Ölmenge | 0,45 l |
| Abtriebsflansch | Yanmar-Flansch ⌀30 mm |
| Neupreis | €2.200–2.800 |
| Typische Motoren | Yanmar 3YM30, 3JH40, 3JH57 |

(Confidence: documented)

### 6.4 KM4A / KM4A2

| Parameter | KM4A | KM4A2 |
|---|---|---|
| Kupplungstyp | Hydraulisch | Hydraulisch |
| Max. Eingangsleistung | 80 PS (59 kW) | 115 PS (85 kW) |
| Untersetzungsverhältnisse | 2,21:1 / 2,62:1 / 3,04:1 | 1,93:1 / 2,21:1 / 2,62:1 |
| Gewicht | 32 kg | 42 kg |
| Öl | ATF Dexron III | ATF Dexron III |
| Ölmenge | 0,7 l | 1,0 l |
| Neupreis | €3.000–3.800 | €3.500–4.500 |
| Typische Motoren | Yanmar 4JH80, 4JH57 | Yanmar 4JH110 |

(Confidence: documented)

### 6.5 KM-Serie — Bekannte Probleme

| Problem | Modell | Häufigkeit | Ursache | Lösung | Kosten |
|---|---|---|---|---|---|
| Vorwärtskupplung rutscht | KM2P/3P | Häufig ab 2.500 Bh | Lamellenverschleiß | Lamellensatz tauschen | €400–700 |
| Ölstand fällt | KM2P | Mittel | Simmerring Abtrieb undicht | Simmerring tauschen | €150–250 |
| Schaltung nicht neutral | KM3P | Selten | Schaltgabel verbogen | Schaltgabel richten/tauschen | €300–500 |
| Getriebegeräusch (Heulen) | KM4A | Selten | Zahnflanke beschädigt | Getriebe tauschen | €2.500–4.000 |
| Ölkühler undicht | KM4A2 | Mittel ab 8 Jahre | Korrosion | Ölkühler tauschen | €200–400 |

(Confidence: documented)

---

## 7. Volvo Penta MS/HS-Getriebe

### 7.1 Überblick

Volvo Penta bietet eigene Wendegetriebe für seine Marinediesel an. Die MS-Serie (Marine Standard) bedient den kleinen bis mittleren Leistungsbereich, die HS-Serie (High Speed) ist für Motorboote konzipiert.

(Confidence: documented)

### 7.2 MS10 / MS15 (Klassiker)

| Parameter | MS10 | MS15 |
|---|---|---|
| Kupplungstyp | Mechanisch (Konus) | Mechanisch (Konus) |
| Max. Eingangsleistung | 12 PS | 20 PS |
| Untersetzung | 2,15:1 | 2,15:1 / 2,47:1 |
| Gewicht | 10 kg | 14 kg |
| Öl | SAE 30 Motoröl | SAE 30 Motoröl |
| Ölmenge | 0,3 l | 0,4 l |
| Produktionszeitraum | 1960–1985 | 1965–1990 |
| Gebrauchtpreis (2026) | €200–400 | €300–500 |
| Typische Motoren | Volvo MD1, MD2 | Volvo MD2B, MD5 |

**Besonderheit MS10/15:** Konuskupplung — Messing-Konus wird gegen Stahl-Gegenkonus gepresst. Verschleiß = Konusfläche poliert = Kupplung rutscht. Nachstellung möglich (Stellmutter).

(Confidence: documented)

### 7.3 MS25 / MS25A

| Parameter | MS25 | MS25A |
|---|---|---|
| Kupplungstyp | Hydraulisch | Hydraulisch |
| Max. Eingangsleistung | 65 PS (48 kW) | 75 PS (55 kW) |
| Untersetzung | 2,27:1 / 2,61:1 | 1,93:1 / 2,27:1 / 2,61:1 |
| Gewicht | 30 kg | 35 kg |
| Öl | ATF Dexron III | ATF Dexron III |
| Ölmenge | 1,0 l | 1,2 l |
| Neupreis (ca.) | €2.800–3.500 | €3.200–4.000 |
| Typische Motoren | Volvo D1-30, D2-40 | Volvo D2-55, D2-75 |

(Confidence: documented)

### 7.4 HS25 / HS63 / HS80 (Motorboot)

| Parameter | HS25 | HS63 | HS80 |
|---|---|---|---|
| Kupplungstyp | Hydraulisch | Hydraulisch | Hydraulisch |
| Max. Eingangsleistung | 175 PS | 480 PS | 650 PS |
| Untersetzung | 1,56:1–2,91:1 | 1,23:1–3,45:1 | 1,23:1–3,86:1 |
| Gewicht | 55 kg | 140 kg | 200 kg |
| Ölmenge | 2,5 l | 4,5 l | 6,0 l |
| Neupreis (ca.) | €4.500–6.000 | €14.000–18.000 | €20.000–28.000 |

**Hinweis:** Volvo Penta MS/HS-Getriebe sind in vielen Fällen von ZF lizenzgefertigt und entsprechen technisch den ZF-Modellen mit Volvo-spezifischer Anpassung (Gehäuseform, Anschlussmaße).

(Confidence: documented)

### 7.5 Bekannte Probleme Volvo MS/HS

| Problem | Modell | Ursache | Lösung |
|---|---|---|---|
| Konuskupplung rutscht | MS10/15 | Konusverschleiß | Nachstellen oder Konus überdrehen lassen |
| Öldruck fällt im warmen Zustand | MS25 | Ölpumpe verschlissen, Lamellen dünn | Ölpumpe/Lamellen tauschen |
| Salzwasser im Getriebeöl | HS63 | Ölkühler-Korrosion | Ölkühler tauschen (SOFORT!) |
| Schaltung blockiert | MS25A | Schaltventil korrodiert | Schaltventil zerlegen/reinigen |
| PTO-Dichtung undicht | HS63/80 | Simmerring verschlissen | Simmerring tauschen |

(Confidence: documented)

---

## 8. PRM / Newage Getriebe

### 8.1 Überblick

PRM (Power Reduction Marine) / Newage ist ein britischer Hersteller, der kompakte, preiswerte Wendegetriebe für den Marine-Markt produziert. Beliebt als Nachrüst-Getriebe und OEM für Beta Marine, Lister Petter und andere britische Motorenhersteller. Fertigung: UK.

(Confidence: documented)

### 8.2 PRM 80

| Parameter | Wert |
|---|---|
| Kupplungstyp | Mechanisch (Klauenkupplung) oder Hydraulisch (Option) |
| Max. Eingangsleistung | 25 PS (18 kW) bei 3.600 U/min |
| Untersetzungsverhältnisse | 2,04:1 / 2,47:1 / 2,86:1 |
| Drehrichtung | Links oder Rechts |
| Gewicht | 11 kg |
| Öl | SAE 80W-90 GL-4 (mechanisch) / ATF (hydraulisch) |
| Ölmenge | 0,3 l |
| Abtriebsflansch | ⌀25 mm Konus |
| Neupreis (2026) | €600–900 |
| Typische Motoren | Beta 14, Lister STW, Kubota-basierte Marine |

(Confidence: documented)

### 8.3 PRM 90

| Parameter | Wert |
|---|---|
| Kupplungstyp | Hydraulisch (Lamellen) |
| Max. Eingangsleistung | 40 PS (29 kW) |
| Untersetzungsverhältnisse | 2,04:1 / 2,47:1 / 2,86:1 |
| Gewicht | 16 kg |
| Öl | ATF Dexron III |
| Ölmenge | 0,5 l |
| Neupreis (2026) | €900–1.300 |
| Typische Motoren | Beta 20/25, Nanni diverse |

(Confidence: documented)

### 8.4 PRM 150

| Parameter | Wert |
|---|---|
| Kupplungstyp | Hydraulisch (Lamellen) |
| Max. Eingangsleistung | 90 PS (66 kW) |
| Untersetzungsverhältnisse | 1,93:1 / 2,04:1 / 2,47:1 / 2,86:1 / 3,17:1 |
| Gewicht | 32 kg |
| Öl | ATF Dexron III |
| Ölmenge | 1,0 l |
| Ölkühler | Seewassergekühlt (Option) |
| Neupreis (2026) | €1.800–2.500 |
| Typische Motoren | Beta 38/43/50, diverse 50–90 PS |

(Confidence: documented)

### 8.5 PRM 260 / PRM 500

| Parameter | PRM 260 | PRM 500 |
|---|---|---|
| Kupplungstyp | Hydraulisch | Hydraulisch |
| Max. Eingangsleistung | 180 PS (132 kW) | 500 PS (368 kW) |
| Untersetzungsverhältnisse | 1,50:1–3,50:1 | 1,25:1–4,00:1 |
| Gewicht | 58 kg | 120 kg |
| Öl | ATF Dexron III | ATF Dexron III |
| Ölmenge | 2,0 l | 4,5 l |
| Neupreis (2026) | €3.500–4.500 | €8.000–11.000 |

(Confidence: documented)

### 8.6 Bekannte Probleme PRM

| Problem | Modell | Ursache | Lösung |
|---|---|---|---|
| Klauen „springen raus" | PRM 80 (mech.) | Verschleiß Schaltklauen | Klauen nachschleifen oder tauschen |
| Ölverlust am Gehäuse | PRM 80/90 | Gehäusedichtung porös | Dichtungssatz erneuern |
| Kupplung rutscht bei Rückwärts | PRM 150 | Rückwärtslamellen dünner als Vorwärts | Lamellensatz tauschen |
| Schaltzug schwergängig | Alle | Korrosion Bowdenzug | Bowdenzug tauschen |
| Getriebeöl-Schaum | PRM 260 | Zu viel Öl eingefüllt | Ölstand korrigieren |
| Geräusche bei kaltem Öl | PRM 90/150 | Normal bis ATF warm (~5 min) | Kein Handlungsbedarf |

(Confidence: documented)

---

## 9. Borg Warner Velvet Drive

### 9.1 Überblick

Borg Warner Velvet Drive ist ein amerikanischer Klassiker im Bootsgetriebebau. Besonders verbreitet in US-amerikanischen Motorbooten und Segelbooten der 1960er–2000er Jahre. Die Marke wurde durch Twin Disc und später Regal-Beloit weitergeführt. Markante Eigenschaft: das Getriebeöl ist normales SAE 30 Motoröl (nicht ATF!).

(Confidence: documented)

### 9.2 Velvet Drive 71C

| Parameter | Wert |
|---|---|
| Kupplungstyp | Hydraulisch (Lamellen) |
| Max. Eingangsleistung | 160 PS (118 kW) |
| Untersetzungsverhältnisse | 1,52:1 / 1,91:1 / 2,10:1 / 2,57:1 |
| Drehrichtung | Standard = Linksdrehend |
| Gewicht | 40 kg |
| Öl | SAE 30 Motoröl (KEIN ATF!) |
| Ölmenge | 1,9 l |
| Ölwechselintervall | Alle 200 Bh oder jährlich |
| Abtriebsflansch | 4-Bolt SAE |
| Produktionszeitraum | 1965–2005 |
| Gebrauchtpreis (2026) | €500–1.200 |
| Typische Motoren | Universal, Westerbeke, Perkins 4.108, Ford Lehman |

**ACHTUNG:** Velvet Drive 71C darf NICHT mit ATF befüllt werden! Die Lamellen-Reibbeläge sind für Motoröl ausgelegt. ATF zerstört die Reibbeläge innerhalb weniger Betriebsstunden.

(Confidence: documented)

### 9.3 Velvet Drive 72C

| Parameter | Wert |
|---|---|
| Kupplungstyp | Hydraulisch (Lamellen) |
| Max. Eingangsleistung | 270 PS (199 kW) |
| Untersetzungsverhältnisse | 1,52:1 / 1,91:1 / 2,10:1 / 2,57:1 |
| Gewicht | 50 kg |
| Öl | SAE 30 Motoröl (KEIN ATF!) |
| Ölmenge | 2,4 l |
| Abtriebsflansch | 4-Bolt SAE |
| Neupreis (ca. 2005) | €3.000–4.000 |
| Gebrauchtpreis (2026) | €800–1.800 |

(Confidence: documented)

### 9.4 Velvet Drive 5000-Serie (ATF)

Die neuere 5000-Serie verwendet ATF statt Motoröl:

| Parameter | 5000A | 5000V |
|---|---|---|
| Kupplungstyp | Hydraulisch | Hydraulisch |
| Max. Eingangsleistung | 280 PS | 400 PS |
| Öl | ATF Dexron III | ATF Dexron III |
| Gewicht | 55 kg | 70 kg |
| Neupreis | €4.500–6.000 | €6.500–8.500 |

(Confidence: documented)

### 9.5 Bekannte Probleme Velvet Drive

| Problem | Modell | Ursache | Lösung |
|---|---|---|---|
| Kupplung rutscht (klassisch) | 71C/72C | Falsches Öl (ATF statt Motoröl!) | Sofort Öl wechseln + Lamellen prüfen |
| Öldruck zu niedrig | 71C | Ölpumpen-Zahnradverschleiß | Ölpumpe überholen |
| Leckage Gussgehäuse | 71C | Riss im Alu-Gehäuse (Korrosion) | Gehäuse abdichten oder tauschen |
| Schaltung „hakt" | 72C | Schaltventil-Kolben korrodiert | Schaltventil zerlegen, polieren |
| Vibrationen | 71C/72C | Fehlausrichtung Motor–Getriebe | Alignment prüfen (→ Kapitel 18) |

(Confidence: documented)

---

## 10. Weitere Hersteller und Nischengetriebe

### 10.1 Twin Disc

| Modell | Leistung | Einsatz | Preis (ca.) |
|---|---|---|---|
| MG-502 | 160 PS | Mittlere Motorboote | €3.500–5.000 |
| MG-506 | 320 PS | Große Motorboote | €6.000–9.000 |
| MG-509 | 500 PS | Motoryachten | €10.000–15.000 |
| MG-5050 | 800 PS | Superyachten | €18.000–25.000 |
| MG-5114 | 1.600 PS | Megayachten, Workboats | €40.000–60.000 |

Typisches Öl: Twin Disc Power Fluid (eigenes ATF-Äquivalent) oder ATF Dexron III.

(Confidence: documented)

### 10.2 Kanzaki (Yanmar/Kubota OEM)

Kanzaki fertigt kompakte Getriebe für kleine Dieselmotoren (Kubota, Yanmar Kleinstmotoren):

| Modell | Leistung | Gewicht | Preis |
|---|---|---|---|
| KM-2A | 12 PS | 8 kg | €500–700 |
| KM-3A | 25 PS | 12 kg | €700–1.000 |
| KBW-10 | 35 PS | 16 kg | €900–1.200 |
| KBW-20 | 65 PS | 28 kg | €1.500–2.200 |

(Confidence: documented)

### 10.3 Dong-i (Koreanisch)

Dong-i fertigt Lizenz-Kopien von ZF- und PRM-Getrieben. Verbreitet auf asiatischen Produktionsbooten.

| Modell | Entspricht | Leistung | Preis (ca.) |
|---|---|---|---|
| DI-M10 | ZF 10M ähnlich | 30 PS | €600–900 |
| DI-M25 | ZF 25 ähnlich | 130 PS | €1.800–2.500 |
| DI-M45 | ZF 45 ähnlich | 250 PS | €3.000–4.500 |

**Warnung:** Ersatzteilversorgung in Europa eingeschränkt. ZF-Originalteile passen teilweise, aber nicht immer.

(Confidence: documented / benchmark)

### 10.4 Capitol Marine / Paragon

Historische US-Getriebe, häufig in klassischen Holzbooten:

| Modell | Typ | Leistung | Status |
|---|---|---|---|
| Paragon P-21 | Hydraulisch | 35 PS | Nicht mehr produziert |
| Paragon P-31 | Hydraulisch | 80 PS | Nicht mehr produziert |
| Capitol HF-7 | Hydraulisch | 120 PS | Nicht mehr produziert |

Ersatzteile: nur noch Gebraucht oder Nachfertigungen von Spezialisten.

(Confidence: documented)

---

## 11. Saildrive — Grundlagen und Systeme

### 11.1 Funktionsprinzip

Der Saildrive besteht aus drei Hauptbereichen:

**Obere Einheit (Upper Leg):**
- Enthält das Wendegetriebe (Vorwärts/Neutral/Rückwärts)
- Kupplungsmechanismus (hydraulisch oder mechanisch)
- Verbindung zum Motor über Schwungscheibe/Kupplungsgehäuse
- Eigener Ölkreislauf (ATF oder Getriebeöl)

**Untere Einheit (Lower Leg):**
- Kegelradsatz lenkt Antriebskraft um 90° nach horizontal
- Propellerwelle mit Gleitlager
- Eigener Ölkreislauf (Getriebeöl SAE 75W-90 oder 80W-90)
- Anodenschutz (Zink oder Aluminium)
- Propeller-Aufnahme

**Membran / Manschette (Diaphragm):**
- Gummi-/Neopren-Manschette zwischen Rumpf und Saildrive-Gehäuse
- Dichtet die Rumpfbohrung ab
- KRITISCHES Bauteil — Versagen = Wassereinbruch!
- Lebensdauer: 7–10 Jahre (herstellerabhängig, umgebungsabhängig)

(Confidence: documented)

### 11.2 Saildrive vs. Wellenanlage — Vergleichsmatrix

| Kriterium | Saildrive | Wellenanlage |
|---|---|---|
| Installationsaufwand | Gering (Rumpfbohrung + Motor drauf) | Hoch (Stevenrohr, Stopfbuchse, Alignment) |
| Gewicht (30 PS System) | 25–35 kg | 40–60 kg (inkl. Welle, Lager etc.) |
| Widerstand unter Segel | Gering (kurzes Bein, Faltpropeller) | Mittel (lange Welle, freiliegend) |
| Vibrationen | Gering (direkter Weg Motor→Propeller) | Mittel (Welle, Kupplungen, Lager) |
| Propellerschutz | Kein (freiliegend unter Rumpf) | Möglicherweise P-Bracket |
| Max. Leistung | ~110 PS (Volvo 150S) | Unbegrenzt |
| Rumpfintegrität | Große Öffnung (Membran-Risiko!) | Kleine Bohrung (Stevenrohr) |
| Antifouling | Aufwändig (Aluminium-Saildrive vs. Kupfer-AF) | Standard |
| Reparatur im Wasser | Schwierig bis unmöglich | Möglich (Stopfbuchse) |
| Lebensdauer | 15–25 Jahre | 30+ Jahre |
| Preis (30 PS System, komplett) | €4.000–6.000 | €2.000–4.000 |

(Confidence: documented)

### 11.3 Antifouling-Problem bei Saildrives

**KRITISCH:** Saildrive-Gehäuse bestehen aus Aluminium. Kupferhaltiges Antifouling erzeugt galvanische Korrosion am Aluminium!

| Antifouling-Typ | Saildrive-kompatibel? | Bemerkung |
|---|---|---|
| Kupferhaltiges Hart-AF | NEIN! | Zerstört Aluminium-Gehäuse |
| Kupferhaltiges Weich-AF | NEIN! | Zerstört Aluminium-Gehäuse |
| Kupferfreies Saildrive-AF (z.B. Marlin SD) | JA | Speziell für Saildrives entwickelt |
| Zinnhaltiges AF | Mit Vorsicht | Nur mit Sperrschicht (2K-Epoxy) |
| Prop Speed / Silikon-AF | JA | Beste Option für Saildrive-Bein |
| Volvo Penta Saildrive AF | JA | Hersteller-Original, teuer aber sicher |

**Empfohlener Aufbau:**
1. Saildrive-Bein entfetten und anschleifen
2. 2K-Epoxyprimer 2×
3. Saildrive-spezifisches Antifouling 2×
4. Oder: Prop Speed als Alternative

(Confidence: documented)

---

## 12. Volvo Penta Saildrive (120S / 130S / 150S)

### 12.1 Modellübersicht

| Parameter | 120S | 130S | 150S |
|---|---|---|---|
| Produktionszeitraum | 1986–2006 | 2003–heute | 2010–heute |
| Max. Motorleistung | 55 PS (40 kW) | 75 PS (55 kW) | 110 PS (81 kW) |
| Kupplungstyp | Hydraulisch (Lamellen) | Hydraulisch (Lamellen) | Hydraulisch (Lamellen) |
| Untersetzung | 2,15:1 | 2,15:1 / 2,33:1 | 1,95:1 / 2,15:1 / 2,33:1 |
| Gewicht (ohne Propeller) | 34 kg | 37 kg | 44 kg |
| Öl obere Einheit | ATF Dexron III | ATF Dexron III | ATF Dexron III |
| Ölmenge obere Einheit | 0,6 l | 0,5 l | 0,8 l |
| Öl untere Einheit | SAE 75W-90 GL-5 | Volvo Penta IPS Oil | Volvo Penta IPS Oil |
| Ölmenge untere Einheit | 0,4 l | 0,35 l | 0,5 l |
| Propelleraufnahme | ⌀22 mm Konus | ⌀22 mm Konus (Saildrive-spezifisch) | ⌀25 mm Konus |
| Membrantyp | Rubber Diaphragm | Rubber Diaphragm (verbessert) | Rubber Diaphragm (neues Design) |
| Membran-Intervall | 7 Jahre (Volvo-Empfehlung) | 7 Jahre | 10 Jahre (neues Material) |
| Neupreis (2026) | — (nicht mehr produziert) | €5.500–7.000 | €7.000–9.500 |
| Typische Motoren | Volvo 2002/2003, MD2020 | Volvo D1-30, D2-40, D2-55 | Volvo D2-50, D2-60, D2-75 |

(Confidence: documented)

### 12.2 DAS MEMBRAN-PROBLEM — Volvo Saildrive

**⚠️ KRITISCHES SICHERHEITSTHEMA ⚠️**

Die Saildrive-Membran ist das einzige Bauteil, das zwischen dem Rumpfinneren und dem Seewasser steht. Membranversagen = direkter Wassereinbruch = Sinkgefahr!

**Volvo Penta Service-Bulletin:**
- **120S:** Membranwechsel spätestens alle 7 Jahre, unabhängig vom Zustand
- **130S:** Membranwechsel spätestens alle 7 Jahre, Sichtprüfung jährlich
- **150S:** Neues Membranmaterial, Intervall 10 Jahre, aber jährliche Sichtprüfung

**Schadensmechanismen:**

| Schadenstyp | Ursache | Erkennbar? | Vorlaufzeit |
|---|---|---|---|
| UV-Alterung | Trockenlagerung ohne Abdeckung | Spröde, Risse sichtbar | Monate |
| Osmotische Alterung | Normaler Wasserkontakt | Materialerweichung (Durometer-Test) | Jahre |
| Chemische Schädigung | Falsches Antifouling, Lösungsmittel | Aufquellen, weich | Wochen–Monate |
| Mechanische Beschädigung | Krantransport, Anstoßen, Abknicken | Riss, Verformung | Sofort |
| Ermüdung durch Vibration | Motorvibrationen (Alignment!) | Riss an Knickstelle | Monate–Jahre |
| Biofouling-Belastung | Muschelbewuchs unter Membranfalte | Druck auf Gummi | Monate |

**Symptome von Membranversagen:**
1. Erhöhter Wasserstand in der Bilge (SOFORT prüfen!)
2. Feuchtigkeit rund um die Saildrive-Öffnung
3. Sichtbare Risse oder Aufwölbungen an der Membran
4. Wassertropfen an der Unterseite der Membranfalte
5. Salzablagerungen innen an der Membran

(Confidence: documented)

### 12.3 Membran-Austauschprozedur (120S/130S)

**Benötigte Teile:**

| Teil | Volvo-Teilenummer | Preis (ca.) |
|---|---|---|
| Membran 120S komplett | 876286 | €250–350 |
| Membran 130S komplett | 21389074 (ersetzt 3888916) | €300–450 |
| Membran 150S komplett | 22307636 | €350–500 |
| Membrankleber (Sikaflex 291) | — | €15–25 |
| Schlauchschellen Edelstahl 316L | — | €10–20 (Satz) |
| Spannband Membran | Im Lieferumfang | — |

**Arbeitsschritte (Kurzfassung, ~4–6 Stunden Arbeitszeit):**

1. **Boot aus dem Wasser**, Saildrive-Bereich trockenlegen
2. Propeller abziehen (Abzieher verwenden, nicht hebeln!)
3. Anoden entfernen
4. Antifouling im Membranbereich abschleifen
5. Spannband der alten Membran lösen
6. Alte Membran vorsichtig abziehen (Reste entfernen!)
7. Kontaktflächen am Rumpf und Saildrive-Gehäuse reinigen (Isopropanol)
8. Kontaktfläche auf Risse/Korrosion prüfen — falls beschädigt: Werft!
9. Neue Membran aufschieben — Markierung beachten (oben/unten)!
10. Membrankleber gemäß Hersteller auftragen
11. Spannband montieren und gleichmäßig festziehen
12. Aushärten lassen (mind. 24 Stunden, Herstellerangabe beachten)
13. Dichtigkeitsprüfung: Bilge trocken legen, Boot einsetzen, 24 Stunden beobachten
14. Anoden montieren, Antifouling auftragen, Propeller montieren

**Kosten Werft (komplett):** €600–1.200 (Material + Arbeit)
**Kosten Eigenarbeit:** €300–500 (Material)

(Confidence: documented)

### 12.4 Volvo 120S — Spezifische Probleme

| Problem | Häufigkeit | Beschreibung | Lösung | Kosten |
|---|---|---|---|---|
| Membran porös | Sehr häufig ab 7 Jahre | Gummi altert, wird spröde | Membranwechsel | €300–500 (Eigen) |
| Ölverlust obere Einheit | Häufig | Simmerring undicht | Simmerring tauschen | €150–300 |
| Kegelrad-Geräusche untere Einheit | Mittel | Lagerauslauf, Zahnflankenverschleiß | Untere Einheit überholen | €800–1.500 |
| Wassereintritt untere Einheit | Mittel | Propellerwellen-Dichtring undicht | Dichtring tauschen | €200–400 |
| Korrosion Gehäuse | Häufig bei falscher AF | Galvanische Korrosion (Cu-AF!) | Gehäuse sanieren, richtiges AF | €300–800 |
| Schaltung schwergängig | Mittel | Bowdenzug korrodiert | Bowdenzug tauschen | €100–200 |

(Confidence: documented)

### 12.5 Volvo 130S — Verbesserungen gegenüber 120S

| Verbesserung | Detail |
|---|---|
| Verbessertes Membrandesign | Dickeres Material, UV-resistenter |
| Neues Anodenkonzept | Drei separate Anoden (obere, untere, Propellernabe) |
| Verbesserter Ölkühler | Integrierter Seewasserkühler für obere Einheit |
| Elektronische Schaltung | Optional: EVC (Electronic Vessel Control) |
| Diagnose-Anschluss | Volvo Penta VODIA-kompatibel |
| Leistungssteigerung | 75 PS (vs. 55 PS bei 120S) |

(Confidence: documented)

### 12.6 Volvo 150S — Aktuelle Generation

| Verbesserung gegenüber 130S | Detail |
|---|---|
| Höhere Leistung | 110 PS max. |
| Neues Membranmaterial | EPDM-basiert, 10 Jahre Intervall |
| Integrierte Diagnose | Volle EVC-Integration, Öltemperatur, Öldruck |
| Verbesserter Korrosionsschutz | Eloxiertes Aluminium + Anodenkonzept |
| Größerer Propellerkonus | ⌀25 mm (vs. ⌀22 mm) |
| Optionaler Faltpropeller | Volvo Saildrive Folding Prop |

(Confidence: documented)

---

## 13. Yanmar Saildrive (SD20 / SD25 / SD50 / SD60)

### 13.1 Modellübersicht

| Parameter | SD20 | SD25 | SD50 | SD60 |
|---|---|---|---|---|
| Produktionszeitraum | 1990–2010 | 2005–heute | 2000–heute | 2012–heute |
| Max. Motorleistung | 25 PS (18 kW) | 40 PS (29 kW) | 55 PS (40 kW) | 75 PS (55 kW) |
| Kupplungstyp | Hydraulisch | Hydraulisch | Hydraulisch | Hydraulisch |
| Untersetzung | 2,64:1 | 2,21:1 / 2,64:1 | 2,21:1 / 2,64:1 | 1,94:1 / 2,21:1 / 2,64:1 |
| Gewicht | 28 kg | 32 kg | 36 kg | 42 kg |
| Öl obere Einheit | ATF Dexron III | ATF Dexron III | ATF Dexron III | ATF Dexron III |
| Ölmenge obere Einheit | 0,35 l | 0,45 l | 0,6 l | 0,7 l |
| Öl untere Einheit | SAE 80W-90 GL-5 | Yanmar Saildrive Oil | Yanmar Saildrive Oil | Yanmar Saildrive Oil |
| Ölmenge untere Einheit | 0,35 l | 0,4 l | 0,45 l | 0,5 l |
| Membrantyp | Rubber Diaphragm | Verbessertes Rubber Diaphragm | Rubber Diaphragm | Neueste Generation |
| Membran-Intervall | 7 Jahre | 7 Jahre | 7 Jahre | 10 Jahre |
| Neupreis (2026) | — | €4.500–5.500 | €5.500–7.000 | €7.000–9.000 |
| Typische Motoren | Yanmar 2GM20, 3GM30 | Yanmar 3YM30 | Yanmar 3JH40/57, 4JH45 | Yanmar 4JH57/80 |

(Confidence: documented)

### 13.2 Yanmar Saildrive — Besonderheiten

**Unterschiede zu Volvo Penta:**

| Aspekt | Yanmar SD | Volvo Saildrive |
|---|---|---|
| Membrandesign | Flachere Falte, kompakterer Sitz | Tiefere Falte, breiterer Sitz |
| Anodenkonzept | Eine große Anode am Bein + Propellernabe | Drei separate Anoden |
| Propelleraufnahme | Standard-Konus (wie Wellenanlage) | Saildrive-spezifischer Konus |
| Antifouling-Empfehlung | Yanmar Original oder kupferfrei | Volvo Original oder kupferfrei |
| Kühlwassereinlass | Am Saildrive-Bein (integriert) | Am Saildrive-Bein (integriert) |
| Ölwechsel untere Einheit | Ablassschraube + Einfüllschraube | Ablassschraube + Einfüllschraube |
| Diagnosemöglichkeit | Yanmar Diagnostik | Volvo VODIA |

(Confidence: documented)

### 13.3 Yanmar SD-Membranwechsel

**Yanmar-Teilenummern:**

| Teil | Teilenummer | Preis (ca.) |
|---|---|---|
| Membran SD20 | 128990-08380 | €200–300 |
| Membran SD25 | 196420-08380 | €250–350 |
| Membran SD50 | 128990-08380 (identisch SD20!) | €200–300 |
| Membran SD60 | 196420-08390 | €300–400 |
| Anodensatz SD20/50 | 196420-02630 | €30–50 |
| Anodensatz SD25/60 | 196420-02640 | €35–55 |
| Propellerwellen-Dichtring | Modellabhängig | €25–45 |

**Austauschprozedur:** Grundsätzlich identisch zur Volvo-Prozedur (→ Kapitel 12.3), aber:
- Yanmar-Membran hat anderes Befestigungssystem (Klemmring statt Spannband)
- Klemmring mit vorgeschriebenem Drehmoment anziehen (8–10 Nm)
- Yanmar empfiehlt kein zusätzliches Dichtmittel (Membran dichtet durch Pressung)

(Confidence: documented)

### 13.4 Yanmar SD — Bekannte Probleme

| Problem | Modell | Häufigkeit | Ursache | Lösung | Kosten |
|---|---|---|---|---|---|
| Membran undicht | Alle | Häufig ab 7 Jahre | Alterung, wie Volvo | Membranwechsel | €300–600 |
| Korrosion untere Einheit | SD20 | Häufig | Anoden nicht gewechselt | Anoden erneuern, Gehäuse prüfen | €50–200 |
| Propellerwelle schwergängig | SD50 | Mittel | Gleitlager verschlissen | Gleitlager tauschen | €200–400 |
| Wassereintritt untere Einheit | SD25/50 | Mittel | Propellenwellen-Dichtring undicht | Dichtring tauschen (Boot an Land) | €150–300 |
| Getriebeöl-Verlust obere Einheit | SD60 | Selten | Dichtung Ölkühler | Ölkühler-Dichtung tauschen | €100–250 |
| Kühlwassereinlass verstopft | Alle | Häufig | Muscheln, Algen | Reinigen (Zahnarztpieker, Draht) | €0 |
| Schaltgestänge korrodiert | SD20 | Häufig | Altes Design, weniger Schutz | Komplettset tauschen | €150–300 |

(Confidence: documented)

---

## 14. ZF Saildrive (SD100 / SD200)

### 14.1 Modellübersicht

ZF stieg relativ spät in den Saildrive-Markt ein. Die SD-Serie richtet sich an OEM-Bootsbauer als Alternative zu Volvo und Yanmar.

| Parameter | SD100 | SD200 |
|---|---|---|
| Produktionszeitraum | 2015–heute | 2018–heute |
| Max. Motorleistung | 50 PS (37 kW) | 80 PS (59 kW) |
| Kupplungstyp | Hydraulisch (Lamellen) | Hydraulisch (Lamellen) |
| Untersetzung | 2,14:1 / 2,63:1 | 2,14:1 / 2,63:1 / 3,05:1 |
| Gewicht | 32 kg | 40 kg |
| Öl obere Einheit | ATF Dexron III/VI | ATF Dexron III/VI |
| Öl untere Einheit | SAE 75W-90 GL-5 | SAE 75W-90 GL-5 |
| Membrantyp | EPDM, neueste Generation | EPDM, neueste Generation |
| Membran-Intervall | 10 Jahre | 10 Jahre |
| Neupreis (2026) | €4.500–5.500 | €6.000–7.500 |
| Typische Motoren | Diverse 30–50 PS (nicht Yanmar/Volvo-spezifisch) |
| Besonderheit | Universelle SAE-Anschlüsse, viele Motorhersteller | PTO-Option |

(Confidence: documented)

### 14.2 ZF Saildrive — Vorteile gegenüber Volvo/Yanmar

| Vorteil | Detail |
|---|---|
| Herstellerunabhängig | Passt an viele Motorhersteller (Nanni, Beta, Vetus) |
| Neues Membrandesign | EPDM statt NR-Gummi, längere Lebensdauer |
| Standard-Anodenform | Handelsübliche Zink-/Alu-Anoden |
| Einfacherer Ölwechsel | Ablassschraube besser zugänglich |
| Modularer Aufbau | Untere Einheit separat tauschbar |

(Confidence: documented)

---

## 15. Untersetzungsverhältnis und Propellerberechnung

### 15.1 Grundformel

Die Propellerleistung hängt direkt vom Zusammenspiel von Motor-Drehzahl, Getriebeuntersetzung und Propeller-Steigung ab:

```
Propellerdrehzahl = Motor-Nenndrehzahl ÷ Untersetzungsverhältnis

Theoretische Geschwindigkeit (Knoten) = (Propellerdrehzahl × Propellersteigung_in_Zoll × 0,000823)

Schlupf = (Theoretische Geschwindigkeit - Tatsächliche Geschwindigkeit) ÷ Theoretische Geschwindigkeit × 100

Ziel-Schlupf:
  - Verdränger (Segelboot): 40–55 %
  - Verdränger (Motorboot): 35–50 %
  - Halbgleiter: 15–25 %
  - Gleiter: 8–15 %
```

(Confidence: calculated)

### 15.2 Untersetzungsberechnung — Entscheidungshilfe

| Motor-Nenndrehzahl | Boot-Typ | Propellertyp | Empfohlene Untersetzung |
|---|---|---|---|
| 3.600 U/min | Segelboot 30 ft | 3-Blatt Fest | 2,50:1 – 3,00:1 |
| 3.600 U/min | Segelboot 30 ft | 3-Blatt Falt | 2,14:1 – 2,63:1 |
| 3.600 U/min | Segelboot 40 ft | 3-Blatt Fest | 2,63:1 – 3,50:1 |
| 3.000 U/min | Motorboot 30 ft (Verdränger) | 3-Blatt Fest | 2,00:1 – 2,50:1 |
| 2.500 U/min | Motorboot 40 ft (Verdränger) | 3-Blatt Fest | 1,50:1 – 2,00:1 |
| 3.600 U/min | Motorboot 25 ft (Gleiter) | 3-Blatt Fest | 1,50:1 – 2,00:1 |
| 2.200 U/min | Trawler 45 ft | 4-Blatt Fest | 2,50:1 – 3,50:1 |
| 1.800 U/min | Motoryacht 60 ft | 4/5-Blatt Fest | 3,00:1 – 4,50:1 |

(Confidence: calculated / benchmark)

### 15.3 Berechnungsbeispiel

**Gegeben:**
- Segelboot Bavaria 37, Volvo D2-40 (40 PS, 3.000 U/min Nenndrehzahl)
- ZF 15M mit Untersetzung 2,63:1
- 3-Blatt Faltpropeller 16" × 11" (Durchmesser × Steigung)

**Berechnung:**
```
Propellerdrehzahl = 3.000 ÷ 2,63 = 1.141 U/min
Theoretische Geschwindigkeit = 1.141 × 11 × 0,000823 = 10,3 Knoten
Bei 45 % Schlupf (Verdränger-Segelboot):
Tatsächliche Geschwindigkeit ≈ 10,3 × (1 - 0,45) = 5,7 Knoten
→ Realistisch für eine Bavaria 37 unter Motor
```

(Confidence: calculated)

### 15.4 Propellerdurchmesser und Getriebebelastung

| Propellerdurchmesser | Drehmoment-Faktor | Getriebe-Belastung | Hinweis |
|---|---|---|---|
| Zu klein | Niedrig | Gering, Getriebe läuft leer | Motor erreicht nicht Nenndrehzahl → Überdrehzahl |
| Optimal | Nominal | Nominal | Motor erreicht Nenndrehzahl bei Volllast |
| Zu groß | Hoch | Überlastung möglich! | Motor erreicht Nenndrehzahl nicht → Überlast |

**Faustregel Propellerdurchmesser (Segelboot):**
```
Max. Propellerdurchmesser (Zoll) ≈ Motorleistung (PS) × 0,4 + 8
Beispiel: 40 PS → 40 × 0,4 + 8 = 24" → realistisch 16"–18" (limitiert durch Apertur)
```

(Confidence: estimated)

---

## 16. Getriebeöl — ATF vs. Gear Oil vs. Synthetik

### 16.1 Übersicht Öltypen

| Öltyp | Farbe | Viskosität | Typische Anwendung | Preis/Liter |
|---|---|---|---|---|
| ATF Dexron III | Rot | ~7 cSt bei 100°C | Hydraulische Wendegetriebe (ZF, Yanmar KM) | €5–10 |
| ATF Dexron VI | Rot | ~6 cSt bei 100°C | Neuere hydraulische Getriebe | €8–15 |
| SAE 80W-90 GL-4 | Gelb/Braun | ~14 cSt bei 100°C | Mechanische Getriebe, Saildrive-Untereinheit | €5–10 |
| SAE 75W-90 GL-5 | Gelb/Braun | ~15 cSt bei 100°C | PRM, einige Saildrive-Untereinheiten | €8–15 |
| SAE 30 Motoröl | Gold | ~10 cSt bei 100°C | Borg Warner Velvet Drive 71C/72C | €5–10 |
| Volvo IPS Oil | Grün | Herstellerspezifisch | Volvo Saildrive-Untereinheit | €25–35 |
| Yanmar Gear Oil | — | Herstellerspezifisch | Yanmar KM- und SD-Serie | €15–25 |
| Synthetisches Getriebeöl | Varies | ~14 cSt bei 100°C | Hochbelastete Getriebe, Langintervall | €15–30 |

(Confidence: documented)

### 16.2 FALSCHES ÖL — Häufigste Fehler

| Fehler | Folge | Schweregrad | Sofortmaßnahme |
|---|---|---|---|
| Motoröl statt ATF in ZF-Getriebe | Kupplung rutscht, Lamellen verkleben | KRITISCH | Sofort ablassen, ATF einfüllen, Lamellen prüfen |
| ATF statt Motoröl in Velvet Drive | Lamellen-Reibbelag zerstört | KRITISCH | Sofort ablassen, Motoröl einfüllen, Lamellen prüfen |
| GL-5 statt GL-4 in mech. Getriebe | Kupferlegierungen korrodieren (Messing!) | MITTEL | Ablassen, GL-4 einfüllen |
| Zu wenig Öl | Überhitzung, Lagerschaden, Lamellenverschleiß | KRITISCH | Motor stoppen, Ölstand korrigieren |
| Zu viel Öl | Schaumbildung, Druckschwankungen | LEICHT | Überschuss ablassen |
| Verschiedene Öle gemischt | Additivkonflikte, Schlammbildung | MITTEL | Komplett ablassen, spülen, frisch füllen |

(Confidence: documented)

### 16.3 Ölzustandsbewertung

| Zustand | Normal | Achtung | Sofort handeln! |
|---|---|---|---|
| Farbe (ATF) | Rot, klar | Dunkelrot, leicht trüb | Braun, schwarz, milchig |
| Farbe (Gear Oil) | Gold/Bernstein | Dunkel, leicht trüb | Schwarz, milchig, Metallglitzer |
| Geruch | Leicht süßlich (ATF) | Verbrannt | Stark verbrannt, stechend |
| Konsistenz | Dünnflüssig (ATF), zähflüssig (Gear) | Leicht verdickt | Schlammig, Wasser-Emulsion |
| Metallpartikel | Keine | Wenige, fein (magnetisch) | Viele, grob, Späne |
| Wassergehalt | 0 % | Leichte Trübung (< 0,1 %) | Milchig (> 1 %) → STOPP |

**Milchiges Öl = Wasser im Getriebe → SOFORT Motor stoppen!**
Häufigste Ursachen: Ölkühler-Leckage, Propellerwellendichtung defekt (Saildrive), Kondenswasser bei langer Standzeit.

(Confidence: documented)

### 16.4 Ölwechsel-Intervalle

| Getriebe-Typ | Betriebsstunden | Zeitintervall | Erstölwechsel |
|---|---|---|---|
| ZF 5M/10M/12M | 250 Bh | Jährlich | Nach 50 Bh |
| ZF 15M/25/45 | 500 Bh | Jährlich | Nach 50 Bh |
| Technodrive TMC | 250 Bh | Jährlich | Nach 50 Bh |
| Yanmar KM | 250 Bh | Jährlich | Nach 50 Bh |
| Volvo MS/HS | 500 Bh | Jährlich | Nach 50 Bh |
| PRM alle | 250 Bh | Jährlich | Nach 25 Bh |
| Borg Warner VD | 200 Bh | Jährlich | Nach 25 Bh |
| Saildrive obere Einheit | 250 Bh | Jährlich | Nach 50 Bh |
| Saildrive untere Einheit | 500 Bh | Alle 2 Jahre | Nach 50 Bh |

> ⚠️ **ZU PRÜFEN (Audit):** Ölwechsel-Intervalle abschnittsintern uneinheitlich. ZF 5M steht hier bei 250 Bh, laut Detailspezifikation (§4.2), Anhang H und der Mechanik-Regel (§3.3) jedoch bei 500 Bh (mechanisches Klauengetriebe). ZF 15M steht hier bei 500 Bh, laut Anhang H jedoch bei 250 Bh (hydraulisch wie ZF 10M/12M). Vor Verwendung mit der Herstellervorgabe abgleichen.

(Confidence: documented)

---

## 17. Schaltgestänge und Bowdenzüge

### 17.1 Schaltungssysteme — Übersicht

| System | Beschreibung | Typischer Einsatz | Vor-/Nachteile |
|---|---|---|---|
| Bowdenzug mechanisch | Stahlseil in Hülle, direkte Verbindung | 90 % aller Segelboote | Günstig, einfach, korrosionsanfällig |
| Gestänge starr | Stangen, Hebel, Umlenkungen | Alte Motorboote, Klassiker | Präzise, wartungsarm, aufwändig zu verlegen |
| Hydraulisch | Hydraulikzylinder am Getriebe | Große Motorboote, Twin-Engine | Leichtgängig, lang, teuer |
| Elektronisch (EVC/ECM) | Elektromotor am Getriebe, Joystick | Moderne Volvo/Yanmar | Komfort, Autopilot-Integration, komplex |

(Confidence: documented)

### 17.2 Bowdenzug-Spezifikationen

| Parameter | Beschreibung |
|---|---|
| Standardtyp | Push-Pull-Zug (Morse-Typ 33C) |
| Hub am Getriebe | Typisch 40–60 mm |
| Max. Biegerad | Min. 150 mm (besser 200 mm) |
| Länge | 2–6 m (Boot-abhängig, nicht kürzen!) |
| Material Außenhülle | Kunststoff (PE/PA) über Stahlspirale |
| Material Innenzug | Edelstahldraht |
| Lebensdauer | 5–10 Jahre (abhängig von Pflege und Lage) |
| Befestigung Getriebe | M8/M10 Gewinde oder Klemmblock |
| Befestigung Bedienpult | Schalteinheit (Single Lever oder Dual Lever) |

(Confidence: documented)

### 17.3 Bowdenzug-Probleme und Lösungen

| Problem | Symptom | Ursache | Lösung |
|---|---|---|---|
| Schwergängig | Hoher Schaltwiderstand | Innenzug korrodiert, Hülle geknickt | Tauschen (€50–150) |
| Spiel | Schaltung unpräzise, Neutral schwer findbar | Befestigung lose, Zug ausgeleiert | Nachstellen, ggf. tauschen |
| Festsitzen | Schaltung blockiert | Innenzug im Kink korrodiert | Sofort tauschen |
| Rückkehr nicht in Neutral | Getriebe bleibt in Fahrt | Feder am Getriebehebel gebrochen | Feder tauschen |
| Flattern bei Drehzahl | Schaltung vibriert | Zug zu lang, schlechte Verlegung | Kürzeren Zug verwenden, besser fixieren |

(Confidence: documented)

### 17.4 Schaltgestänge — Einstellprozedur

**Grundeinstellung (Bowdenzug an Getriebe):**

1. Motor AUS, Getriebe in NEUTRAL
2. Bowdenzug am Getriebe lösen
3. Schalthebel am Bedienpult in exakte NEUTRAL-Position bringen
4. Getriebehebel am Getriebe in exakte NEUTRAL-Position bringen (Markierung beachten)
5. Bowdenzug spannungsfrei am Getriebehebel befestigen
6. Kontermutter festziehen
7. Funktion prüfen: Volle Schaltwege Vorwärts und Rückwärts müssen erreichbar sein
8. Motor starten, im Leerlauf schalten — Vorwärts und Rückwärts müssen sauber einrasten
9. Ggf. Feineinstellung durch Gewindeverstellung am Bowdenzug-Ende

**Häufiger Fehler:** Bowdenzug unter Spannung montiert → Getriebe steht nicht in echtem Neutral → Lamellenverschleiß, Schleifgeräusche, Boot kriecht im Leerlauf.

(Confidence: documented)

---

## 18. Getriebe-Alignment

### 18.1 Warum Alignment kritisch ist

Fehlausrichtung (Misalignment) zwischen Motor/Getriebe und Propellerwelle ist die häufigste Ursache für:
- Vibrationen im gesamten Antriebsstrang
- Vorzeitigen Verschleiß von Kupplung, Lagern, Stopfbuchse
- Geräusche (Brummen, Dröhnen, Schlagen)
- Im Extremfall: Wellenbruch oder Getriebedefekt

(Confidence: documented)

### 18.2 Alignment-Toleranzen

| Antriebstyp | Winkelversatz max. | Parallelversatz max. | Messmethode |
|---|---|---|---|
| Starre Kupplung (Flansch) | 0,05 mm/100 mm | 0,05 mm | Fühlerblatt (4 Positionen) |
| Flexible Kupplung (Gummi) | 0,10 mm/100 mm | 0,15 mm | Fühlerblatt + Messuhr |
| Aquadrive / CV-Joint | 1,0° | 3 mm | Messuhr |
| Saildrive | Nicht anwendbar (fest montiert) | — | — |

(Confidence: measured)

### 18.3 Alignment-Prozedur (Konventionelle Wellenanlage)

**Benötigtes Werkzeug:**
- Fühlerblattlehre (0,01–1,00 mm)
- Gerade Stahllineal oder Messuhr
- Schraubenschlüssel für Motorhalter
- Taschenlampe
- Optional: Laser-Alignment-Tool

**Prozedur:**

1. Boot im Wasser (belastet!) — Alignment an Land ist NICHT aussagekräftig
2. Motor warm fahren (10 Minuten Leerlauf)
3. Motor AUS, Propellerwelle entkuppeln
4. Flansche zusammenführen (ohne Schrauben)
5. Fühlerblatt an 4 Positionen (12, 3, 6, 9 Uhr) zwischen den Flanschen messen
6. Maximale Differenz notieren → muss < 0,05 mm sein (starre Kupplung)
7. Welle um 180° drehen und erneut messen (eliminiert Wellen-Rundlauf)
8. Motorhalter anpassen: vorne/hinten für Höhe, seitlich für Parallelversatz
9. Prozedur wiederholen bis Toleranz erreicht
10. Flanschschrauben anziehen, nochmals messen
11. Probefahrt: Vibrationen bei allen Drehzahlen prüfen

**Typischer Zeitaufwand:** 1–4 Stunden
**Werftkosten:** €200–500

(Confidence: documented)

### 18.4 Alignment-Probleme nach Bootskran

| Problem | Ursache | Lösung |
|---|---|---|
| Alignment stimmt an Land, nicht im Wasser | Rumpfverformung durch Gewicht im Wasser | IMMER im Wasser alignment-en |
| Alignment verschlechtert sich über Saison | Motorfundament verzieht sich (GFK-Kriechverformung) | Halbjährlich prüfen, Fundament verstärken |
| Alignment nach Grundberührung gestört | Wellenanlage verbogen | Welle prüfen (Rundlauf < 0,05 mm), ggf. tauschen |
| Vibrationen trotz gutem Alignment | Propeller unwuchtig, Welle verbogen | Propeller wuchten, Welle prüfen |

(Confidence: documented)

---

## 19. Saildrive-Anoden (Zink vs. Aluminium)

### 19.1 Anodenmaterialien — Vergleich

| Parameter | Zink (Zn) | Aluminium (Al) | Magnesium (Mg) |
|---|---|---|---|
| Elektrodenpotenzial | -1,05 V (vs. Ag/AgCl) | -1,10 V (vs. Ag/AgCl) | -1,60 V (vs. Ag/AgCl) |
| Kapazität | 780 Ah/kg | 2.700 Ah/kg | 1.230 Ah/kg |
| Salzwasser | JA | JA | NEIN (zu aggressiv) |
| Brackwasser | JA | JA (besser als Zink) | NEIN |
| Süßwasser | NEIN (passiviert!) | Bedingt | JA |
| Lebensdauer (gleiche Masse) | Referenz | 3–4× länger | 1,5× länger |
| Preis pro Stück (Saildrive) | €20–30 | €25–40 | €15–25 |
| Empfehlung Saildrive (Salzwasser) | Standard | Bevorzugt (besser, leichter) | NEIN |
| Empfehlung Saildrive (Brackwasser) | Nur wenn Aluminium nicht verfügbar | JA (optimale Wahl) | NEIN |
| Umwelt | Zink ist Umweltgift! (EU-Regulierung!) | Umweltfreundlicher | — |

(Confidence: documented)

### 19.2 Anodenwechsel-Intervalle

| Zustand | Aktion |
|---|---|
| Anode > 50 % Restmasse | OK, bei nächstem Slipgang prüfen |
| Anode 30–50 % Restmasse | Beim nächsten Slipgang tauschen |
| Anode < 30 % Restmasse | SOFORT tauschen |
| Anode komplett aufgelöst | ALARMZUSTAND: Saildrive-Gehäuse prüfen, Korrosionsschäden möglich! |
| Anode zeigt keine Auflösung | FALSCH! Schlechter Kontakt oder falsches Material → prüfen |

**Generelle Regel:** Anoden spätestens jährlich visuell prüfen, alle 2 Jahre tauschen (auch wenn noch > 50 %).

(Confidence: documented)

### 19.3 Anodenteilnummern (gängigste Modelle)

| Saildrive | Anode | OEM-Teilenummer | Aftermarket | Preis (ca.) |
|---|---|---|---|---|
| Volvo 120S Bein | Zink-Ring | 875815 | Tecnoseal 01308 | €25–35 |
| Volvo 120S Propeller | Zink-Mutter | 876638 | Tecnoseal 01309 | €15–25 |
| Volvo 130S Bein | Zink-Ring | 3888305 | MG Duff CM3888305Z | €30–45 |
| Volvo 130S Bein | Aluminium-Ring | 3888305A | MG Duff CM3888305A | €35–50 |
| Volvo 130S Propeller | Zink-Mutter | 3858399 | Tecnoseal diverse | €15–25 |
| Volvo 150S Bein | Aluminium | 22868647 | MG Duff diverse | €35–55 |
| Yanmar SD20/50 | Zink-Ring | 196420-02630 | Tecnoseal diverse | €25–40 |
| Yanmar SD25/60 | Zink-Ring | 196420-02640 | Tecnoseal diverse | €30–45 |
| ZF SD100 | Zink | ZF OEM | MG Duff diverse | €25–40 |
| ZF SD200 | Zink/Alu | ZF OEM | MG Duff diverse | €30–50 |

(Confidence: documented)

### 19.4 EU-Regulierung — Zink-Anoden

**WICHTIG:** Die EU reguliert zunehmend die Verwendung von Zink im Marinebereich. Schweden und Niederlande haben bereits strengere Grenzwerte für Zink-Auslösung. Mittelfristig (bis 2030) ist mit einem EU-weiten Verbot von Zink-Anoden zu rechnen. Aluminium-Anoden sind die zukunftssichere Alternative.

(Confidence: documented)

---

## 20. Saildrive-Membran — Lebensdauer und Austausch

### 20.1 Membranmaterialien

| Material | Generation | Lebensdauer | Hersteller | Hinweis |
|---|---|---|---|---|
| NR (Naturkautschuk) | 1. Gen (1970er–1990er) | 5–7 Jahre | Volvo 100/110/120S (alt) | Veraltet, UV-empfindlich |
| CR (Chloropren/Neopren) | 2. Gen (1990er–2010er) | 7–10 Jahre | Volvo 120S/130S, Yanmar SD20/50 | Standard, gute Chemikalienbeständigkeit |
| EPDM | 3. Gen (2010er–heute) | 10–15 Jahre | Volvo 150S, ZF SD100/200, Yanmar SD60 | Beste UV- und Ozonbeständigkeit |

(Confidence: documented)

### 20.2 Lebensdauer-Einflussfaktoren

| Faktor | Positiver Einfluss | Negativer Einfluss |
|---|---|---|
| UV-Strahlung | Membran abgedeckt/geschützt | Offene Lagerung ohne Schutz |
| Temperatur | Gemäßigte Zone (10–25°C) | Tropen (> 30°C permanent) |
| Chemikalien | Kupferfreies AF, kein Lösungsmittel | Kupfer-AF direkt auf Membran, Aceton |
| Vibration | Gutes Motor-Alignment | Fehlausrichtung, harter Motorlauf |
| Mechanische Belastung | Korrekte Montage | Knicke, falsche Lagerung am Kran |
| Wasserqualität | Sauberes Seewasser | Hafenwasser mit Verschmutzung |
| Wartung | Jährliche Sichtprüfung | Keine Inspektion über Jahre |

(Confidence: documented)

### 20.3 Prüfprotokoll Saildrive-Membran (Jährlich)

| Prüfpunkt | Methode | OK | Achtung | Sofort handeln |
|---|---|---|---|---|
| Sichtbare Risse | Augenschein + Lupe | Keine | Oberflächenrisse (< 0,5 mm tief) | Durchgehende Risse |
| Elastizität | Daumendrucktest | Federt sofort zurück | Langsame Rückfederung | Kein Zurückfedern (hart) |
| Verformung | Augenschein | Gleichmäßige Falte | Leichte Asymmetrie | Aufwölbung, Einstülpung |
| Farbveränderung | Augenschein | Gleichmäßig (schwarz/grau) | Fleckig, aufgehellt | Rissig, porös, weiß |
| Biofouling | Augenschein | Keines | Leichter Bewuchs | Muscheln in Membranfalte |
| Salzablagerungen innen | Innenseite prüfen | Keine | Leichte Salzflecken | Nasse Stellen, Tropfen → LECK! |
| Spannband/Klemmring | Sitz prüfen | Fest, korrosionsfrei | Leichte Korrosion | Lose, korrodiert → SOFORT tauschen |
| Dichtmittelzustand | Augenschein | Intakt, elastisch | Risse im Dichtmittel | Abgelöst → Neuabdichtung |

(Confidence: documented)

### 20.4 Membranwechsel — Kostenübersicht

| Posten | Volvo 120S | Volvo 130S | Volvo 150S | Yanmar SD | ZF SD |
|---|---|---|---|---|---|
| Membran (Material) | €250–350 | €300–450 | €350–500 | €200–400 | €250–400 |
| Kleber/Dichtmittel | €15–25 | €15–25 | €15–25 | Nicht nötig | €15–25 |
| Anoden (gleich mitmachen) | €40–60 | €50–80 | €50–80 | €30–55 | €25–50 |
| Arbeitszeit Werft (4–6 h) | €400–600 | €400–600 | €400–600 | €350–500 | €350–500 |
| Slipgebühr | €150–300 | €150–300 | €150–300 | €150–300 | €150–300 |
| **Gesamt Werft** | **€855–1.335** | **€915–1.455** | **€965–1.505** | **€730–1.255** | **€790–1.275** |
| **Gesamt Eigenarbeit** | **€305–435** | **€365–555** | **€415–605** | **€230–455** | **€290–475** |

(Confidence: benchmark)

---

## 21. Propellerintegration — Flexofold / Gori / Volvo

### 21.1 Faltpropeller für Saildrive

| Hersteller | Modell | Blätter | Durchmesser | Kompatibilität | Preis (ca.) |
|---|---|---|---|---|---|
| Flexofold | 2-Blatt | 2 | 13"–20" | Volvo 120S/130S/150S, Yanmar SD | €900–1.400 |
| Flexofold | 3-Blatt | 3 | 13"–20" | Volvo 120S/130S/150S, Yanmar SD | €1.200–1.800 |
| Flexofold | 4-Blatt | 4 | 15"–20" | Volvo 130S/150S | €1.600–2.200 |
| Gori | 2-Blatt Race | 2 | 12"–18" | Volvo, Yanmar (mit Adapter) | €1.000–1.600 |
| Gori | 3-Blatt | 3 | 14"–20" | Volvo, Yanmar | €1.400–2.000 |
| Volvo Penta | Folding Prop S1 | 3 | 15"–19" | Nur Volvo Saildrive | €1.800–2.500 |
| Volvo Penta | Folding Prop S2 | 3 | 15"–21" | Nur Volvo 130S/150S | €2.200–3.000 |
| Kiwiprop | Feathering | 3 | 14"–20" | Volvo, Yanmar, ZF | €1.200–1.800 |
| Max-Prop | Feathering | 3 | 14"–22" | Universal (mit Konus-Adapter) | €1.800–2.800 |

(Confidence: documented / benchmark)

### 21.2 Flexofold — Besonderheiten

**Vorteile:**
- Geringster Widerstand aller Faltpropeller (Herstellerangabe: 0,2 kn mehr unter Segel)
- Kein Mechanismus, der korrodieren kann (rein passiv faltend)
- Einfache Montage auf Standard-Konus

**Nachteile:**
- Rückwärtsfahrt erst nach kurzem Vorwärts-Impuls (Blätter müssen sich entfalten)
- Seitendrift beim Entfalten möglich
- Blätter können bei Bewuchs festsitzen

**Steigungseinstellung:** Flexofold bietet austauschbare Blätter mit verschiedenen Steigungen. Steigungsoptimierung vor Ort möglich.

(Confidence: documented)

### 21.3 Gori-Propeller — Besonderheiten

**Vorteile:**
- Patentiertes 2-Geschwindigkeiten-System: Blätter klappen in Rückwärts in steilere Position
- Dadurch ca. 20 % mehr Rückwärtsschub als Flexofold
- Overdrive-Position für Langsamfahrt (geringerer Slip)

**Nachteile:**
- Komplexerer Mechanismus (Verstellnabe)
- Regelmäßige Wartung der Nabe empfohlen (jährlich)
- Teurer als Flexofold

(Confidence: documented)

### 21.4 Volvo Penta Original-Faltpropeller

**Hinweis:** Volvo Penta Faltpropeller sind NUR mit Volvo Saildrives kompatibel. Der Konuswinkel und die Befestigung sind Volvo-spezifisch. Aftermarket-Propeller benötigen einen Konus-Adapter.

| Modell | Blätter | Durchmesser | Empfohlene Motorleistung | Preis |
|---|---|---|---|---|
| S1 Folding Prop | 3 | 15", 16", 17", 18", 19" | 10–55 PS | €1.800–2.500 |
| S2 Folding Prop | 3 | 15", 16", 17", 18", 19", 21" | 30–110 PS | €2.200–3.000 |

(Confidence: documented)

---

## 22. Fehlerbilder und Diagnostik

### 22.1 Fehlerbild 1: Getriebe rutscht (vorwärts oder rückwärts)

| Aspekt | Detail |
|---|---|
| Symptom | Motor dreht hoch, Boot beschleunigt nicht oder langsam |
| Mögliche Ursachen | 1) Lamellenverschleiß 2) Öldruck zu niedrig 3) Falsches Öl 4) Ölstand zu niedrig 5) Schaltung nicht voll eingerastet |
| Erstdiagnose | Öl prüfen: Stand, Farbe, Geruch. Schaltweg prüfen. |
| Messung | Öldruck am Messanschluss (falls vorhanden) |
| Confidence | documented |

### 22.2 Fehlerbild 2: Geräusche im Neutral

| Aspekt | Detail |
|---|---|
| Symptom | Rasseln, Klappern, Summen bei laufendem Motor in Neutral |
| Mögliche Ursachen | 1) Zahnflankenspiel (normal bei kalt) 2) Lager verschlissen 3) Ölstand zu niedrig 4) Ölpumpe defekt 5) Fehlausrichtung Motor–Getriebe |
| Erstdiagnose | Geräusch mit Temperatur-Anstieg beobachten. Wenn warm leiser → normal. |
| Messung | Stethoskop am Getriebegehäuse |
| Confidence | documented |

### 22.3 Fehlerbild 3: Boot kriecht im Leerlauf

| Aspekt | Detail |
|---|---|
| Symptom | Boot bewegt sich langsam vorwärts/rückwärts trotz Neutral-Stellung |
| Mögliche Ursachen | 1) Schaltgestänge falsch eingestellt 2) Bowdenzug unter Spannung 3) Lamellen kleben (nach Standzeit) 4) Hydraulikdruck im Neutral-Kanal |
| Erstdiagnose | Schalteinstellung prüfen (→ Kapitel 17.4) |
| Confidence | documented |

### 22.4 Fehlerbild 4: Ölleckage am Getriebe

| Aspekt | Detail |
|---|---|
| Symptom | Ölflecken unter dem Getriebe, Ölstand fällt |
| Mögliche Ursachen | 1) Simmerring Abtrieb 2) Simmerring Antrieb 3) Gehäusedichtung 4) Ölkühleranschluss 5) Ölmessstab-Dichtung 6) Riss im Gehäuse |
| Erstdiagnose | Öl-Lecksuch-Spray oder UV-Tinte verwenden |
| Confidence | documented |

### 22.5 Fehlerbild 5: Vibrationen im Antriebsstrang

| Aspekt | Detail |
|---|---|
| Symptom | Vibrationen, die mit Drehzahl zunehmen (unter Last stärker) |
| Mögliche Ursachen | 1) Fehlausrichtung Motor–Welle 2) Propeller unwuchtig 3) Motorlager verschlissen 4) Welle verbogen 5) Kupplung verschlissen 6) Lager verschlissen |
| Erstdiagnose | Vibrationscharakteristik analysieren: bei welcher Drehzahl? Unter Last oder ohne? Nur vorwärts oder auch rückwärts? |
| Confidence | documented |

### 22.6 Fehlerbild 6: Wasser im Getriebeöl

| Aspekt | Detail |
|---|---|
| Symptom | Milchiges Öl am Messstab, Emulsion |
| Mögliche Ursachen | 1) Ölkühler undicht (Seewasser → Getriebe) 2) Propellerwellendichtung undicht (Saildrive) 3) Kondenswasser (lange Standzeit) 4) Gehäusedichtung undicht bei Hoch-Druck-Reinigung |
| SOFORTMASSNAHME | Motor SOFORT stoppen! Nicht weiterfahren! |
| Weiteres Vorgehen | Öl komplett ablassen, Ursache finden, beheben, spülen, frisches Öl einfüllen. |
| Confidence | documented |

### 22.7 Fehlerbild 7: Schaltung schwergängig

| Aspekt | Detail |
|---|---|
| Symptom | Hoher Kraftaufwand zum Schalten, Schalthebel klemmt |
| Mögliche Ursachen | 1) Bowdenzug korrodiert 2) Bowdenzug zu eng verlegt (Knick) 3) Getriebeventil schwergängig 4) Hebel am Getriebe korrodiert 5) Schalteinheit am Bedienpult defekt |
| Erstdiagnose | Bowdenzug am Getriebe lösen. Getriebehebel direkt von Hand schalten — leichtgängig? Dann ist der Bowdenzug schuld. |
| Confidence | documented |

### 22.8 Fehlerbild 8: Saildrive-Membran undicht

| Aspekt | Detail |
|---|---|
| Symptom | Wasserstand in Bilge steigt (langsam oder schnell), feuchte Stellen um Saildrive-Öffnung |
| Schweregrad | KRITISCH — potenzielle Sinkgefahr! |
| Mögliche Ursachen | 1) Membran gealtert/porös 2) Membran beschädigt (mechanisch) 3) Klemmring/Spannband lose 4) Dichtmittel abgelöst 5) Membran falsch montiert |
| SOFORTMASSNAHME | Bilgepumpe laufen lassen, Boot beobachten. Bei starkem Wassereintritt: Boot aus dem Wasser! |
| Confidence | documented |

### 22.9 Fehlerbild 9: Saildrive-Korrosion

| Aspekt | Detail |
|---|---|
| Symptom | Weißes Pulver am Aluminium-Gehäuse, Lochfraß, raue Oberfläche |
| Mögliche Ursachen | 1) Anoden verbraucht/fehlend 2) Kupferhaltiges Antifouling! 3) Fremdströme (Landstromanschluss ohne Isolator) 4) Kontakt mit anderen Metallen (galvanisches Element) |
| Erstdiagnose | Anodenzustand prüfen, Antifouling-Typ prüfen, Holm-Bonding prüfen |
| Confidence | documented |

### 22.10 Fehlerbild 10: Getriebe überhitzt

| Aspekt | Detail |
|---|---|
| Symptom | Öltemperatur > 100°C, Alarmmeldung, Verbrennungsgeruch, Ölverfärbung |
| Mögliche Ursachen | 1) Ölkühler verstopft (Seewasserseite) 2) Ölmenge zu niedrig 3) Dauerbetrieb Kupplung (Schleppbetrieb) 4) Kupplung rutscht (Reibungswärme) 5) Umgebungstemperatur hoch + Motor überlastet |
| SOFORTMASSNAHME | Last reduzieren, Drehzahl senken. Wenn Temperatur nicht fällt: Motor stoppen. |
| Confidence | documented |

### 22.11 Fehlerbild 11: Propeller dreht im Neutral (Saildrive)

| Aspekt | Detail |
|---|---|
| Symptom | Propeller dreht sich mit, obwohl Getriebe in Neutral |
| Mögliche Ursachen | 1) Schaltgestänge falsch eingestellt 2) Lamellen verkleben (Ölverschlammung) 3) Getriebeventil defekt 4) Faltpropeller klemmt (Bewuchs) |
| Erstdiagnose | Schalteinstellung prüfen. Propeller von Hand drehen — ist Widerstand gleichmäßig? |
| Confidence | documented |

### 22.12 Fehlerbild 12: Kegelradgeräusche in Saildrive-Untereinheit

| Aspekt | Detail |
|---|---|
| Symptom | Mahlende, heulende Geräusche aus dem Saildrive-Bein (unter Wasser) |
| Mögliche Ursachen | 1) Ölstand untere Einheit zu niedrig 2) Wassereintritt in untere Einheit 3) Lager verschlissen 4) Kegelrad-Zahnflankenverschleiß |
| Erstdiagnose | Öl untere Einheit ablassen und prüfen: Menge, Farbe, Metallteilchen |
| Confidence | documented |

---

## 23. Troubleshooting-Leitfäden

### 23.1 Troubleshooting: Getriebe lässt sich nicht schalten

```
SCHRITT 1: Motor läuft? Drehzahl?
├── Motor AUS → Motor starten (Ölpumpe braucht Motor!)
├── Motor läuft, Drehzahl > 1.500 U/min → Drehzahl auf Leerlauf (< 800 U/min)
└── Motor läuft, Leerlauf → weiter Schritt 2

SCHRITT 2: Schalthebel prüfen
├── Schalthebel bewegt sich nicht → Schalteinheit mechanisch defekt → Reparatur Bedienpult
├── Schalthebel bewegt sich, aber weich (kein Widerstand) → Bowdenzug gerissen → Tauschen
└── Schalthebel bewegt sich mit normalem Widerstand → weiter Schritt 3

SCHRITT 3: Bowdenzug am Getriebe prüfen
├── Bowdenzug lösen, Getriebehebel direkt betätigen
│   ├── Getriebehebel bewegt sich nicht → Getriebe intern blockiert → Werft!
│   ├── Getriebehebel bewegt sich, Getriebe schaltet → Bowdenzug-Problem (tauschen/einstellen)
│   └── Getriebehebel bewegt sich, Getriebe schaltet NICHT → weiter Schritt 4
└──

SCHRITT 4: Ölstand und Öldruck prüfen
├── Ölstand zu niedrig → Auffüllen, Leckage suchen
├── Ölstand OK → Öldruck messen (Manometer an Messanschluss)
│   ├── Öldruck < 5 bar → Ölpumpe defekt → Überholung
│   └── Öldruck > 8 bar → Schaltventil blockiert → Ventil reinigen/tauschen
└── Ölstand überfüllt → Überschuss ablassen
```

(Confidence: documented)

### 23.2 Troubleshooting: Saildrive-Wassereinbruch

```
SCHRITT 1: Wassereinbruchrate feststellen
├── Tropfend (< 1 l/h) → Beobachten, Ursache bei nächstem Slipgang suchen
├── Rinnend (1–10 l/h) → Boot zeitnah aus dem Wasser, Ursache suchen
└── Strömend (> 10 l/h) → SOFORT aus dem Wasser! Bilgepumpe laufen lassen!

SCHRITT 2: Eintrittsstelle lokalisieren
├── Wasser kommt von oben (Saildrive-Flansch) → Membran-Oberteil oder Klemmring undicht
├── Wasser kommt seitlich (Membranfalte) → Membran gerissen → MEMBRANWECHSEL
├── Wasser kommt von unten (Propellerwelle) → Propellenwellendichtung undicht → Dichtring tauschen
└── Nicht lokalisierbar → Boot komplett trockenlegen, Sichtprüfung

SCHRITT 3: Sofortmaßnahmen
├── Membranriss → Behelfsmäßig: selbstvulkanisierendes Reparaturband + Schlauchschelle
│   (NUR Notlösung für Überführung! Kein Dauerzustand!)
├── Klemmring lose → Nachziehen (8–10 Nm)
├── Dichtmittel defekt → Reinigen + Sikaflex 291 neu auftragen
└── Propellenwellendichtung → Boot muss aus dem Wasser
```

(Confidence: documented)

### 23.3 Troubleshooting: Getriebeöl milchig (Wasser im Öl)

```
SCHRITT 1: Motor SOFORT stoppen!
     Nicht weiterfahren! Wasser im Öl = keine Schmierung = Totalschaden möglich!

SCHRITT 2: Ölprobe nehmen (Foto + Menge dokumentieren)

SCHRITT 3: Ursache eingrenzen
├── Boot hat Ölkühler (Seewasser-gekühlt)?
│   ├── JA → Ölkühler-Leckage wahrscheinlich (häufigste Ursache!)
│   │   └── Test: Ölkühler ausbauen, auf Dichtigkeit prüfen (Druckprüfung 2 bar)
│   └── NEIN → weiter
├── Saildrive?
│   ├── JA → Propellenwellendichtring prüfen (Öl untere Einheit prüfen)
│   └── NEIN → weiter
├── Nur obere Einheit betroffen?
│   └── JA → Ölkühler intern undicht → Ölkühler tauschen
└── Beide Einheiten betroffen? → Ölkühler + Propellenwellendichtring prüfen

SCHRITT 4: Reparatur
├── Ölkühler tauschen → Neuen Kühler einbauen, System spülen
├── Dichtring tauschen → Boot an Land, untere Einheit öffnen
└── Getriebe komplett spülen (3× Öl wechseln mit kurzer Laufzeit dazwischen)

SCHRITT 5: Langzeitfolgen prüfen
├── Lamellen prüfen (Korrosion, Rost auf Stahllamellen)
├── Lager prüfen (Laufgeräusche)
└── Nach 50 Bh erneut Ölprobe nehmen
```

(Confidence: documented)

### 23.4 Troubleshooting: Starke Vibrationen nach Getriebe-/Propellerwechsel

```
SCHRITT 1: Was wurde gewechselt?
├── Getriebe getauscht → Alignment prüfen (→ Kapitel 18)
├── Propeller getauscht → Propeller-Spezifikation prüfen (Durchmesser, Steigung, Blattanzahl)
├── Beides → Zuerst Alignment, dann Propeller
└── Saildrive komplett → Montage prüfen (Gummilager, Membran, Schrauben)

SCHRITT 2: Vibrations-Analyse
├── Vibration bei ALLEN Drehzahlen → Alignment-Problem oder Propeller-Unwucht
├── Vibration nur bei BESTIMMTER Drehzahl → Resonanz → Drehzahl meiden, Motorlager prüfen
├── Vibration nur UNTER LAST → Propellerproblem (Schlupf, kavitiert)
└── Vibration nur VORWÄRTS (nicht Rückwärts) → Vorwärts-Kupplung schleift

SCHRITT 3: Prüfung
├── Propeller visuell: Blätter symmetrisch? Kein Schlag? Kein Bewuchs?
├── Propellerwelle: Rundlauf < 0,05 mm am Flansch?
├── Motorlager: Risse im Gummi? Einseitig eingesunken?
└── Alignment: Fühlerblatt-Messung (→ Kapitel 18.3)
```

(Confidence: documented)

### 23.5 Troubleshooting: Saildrive-Anode frisst sich zu schnell auf

```
SCHRITT 1: Auflösungsrate feststellen
├── < 6 Monate vollständig aufgelöst → ALARM: Fremdströme oder galvanisches Problem
├── 6–12 Monate aufgelöst → Erhöht, aber handhabbar → Ursache suchen
└── > 12 Monate bis 50 % → Normal

SCHRITT 2: Ursachen prüfen
├── Landstrom angeschlossen?
│   ├── JA → Landstrom-Trenntrafo / galvanischer Isolator vorhanden?
│   │   ├── NEIN → Galvanischen Isolator einbauen (→ ABYC E-2)
│   │   └── JA → Isolator prüfen (defekt?)
│   └── NEIN → weiter
├── Andere Boote im Umfeld mit Landstrom?
│   └── JA → Fremdströme über Wasser möglich → Liegeplatz wechseln oder Isolator einbauen
├── Verschiedene Metalle am Unterwasserschiff?
│   └── JA → Bonding prüfen (alle Metalle am gleichen Potential?)
└── Falsches Anodenmaterial?
    └── Zink in Brackwasser → Aluminium verwenden
```

(Confidence: documented)

---

## 24. Fallstudien

### 24.1 Fallstudie: Volvo 130S Membranriss — Bavaria 37 Cruiser (BJ 2014)

| Aspekt | Detail |
|---|---|
| Boot | Bavaria 37 Cruiser, Baujahr 2014, Volvo D2-40 + 130S Saildrive |
| Problem | Erhöhter Wasserstand in Bilge nach 9 Jahren, Membran nie gewechselt |
| Diagnose | Sichtprüfung: 3 cm langer Riss in Membranfalte (Unterseite) |
| Ursache | Überalterte Membran (9 Jahre, Empfehlung 7 Jahre), UV-Belastung durch offene Winterlagerung |
| Reparatur | Membranwechsel (Volvo 21389074), Anoden gleich mit, neues Antifouling (kupferfrei) |
| Kosten | Material: €480, Werftarbeit: €520, Slipgebühr: €200 — **Gesamt: €1.200** |
| Lehre | **Membranwechsel-Intervalle einhalten!** Kosten des Wechsels sind Bruchteil des Schadens bei Untergang. |
| Confidence | documented |

### 24.2 Fallstudie: ZF 25 — Wasser im Öl durch Ölkühler-Korrosion — Hallberg-Rassy 40 (BJ 2007)

| Aspekt | Detail |
|---|---|
| Boot | Hallberg-Rassy 40, Baujahr 2007, Volvo D2-75 + ZF 25 |
| Problem | Kupplung rutscht nach 2.800 Bh, Getriebeöl milchig-braun |
| Diagnose | Ölkühler intern undicht → Seewasser im ATF → Lamellen korrodiert |
| Ursache | Plattenwärmetauscher nach 16 Jahren durchkorrodiert (Lochfraß Seewasserseite) |
| Reparatur | Ölkühler neu (€550), Lamellensatz V/R (€650), Dichtungssatz (€180), 3× Ölwechsel zum Spülen |
| Kosten | Material: €1.480, Werftarbeit: €800 — **Gesamt: €2.280** |
| Lehre | **Ölkühler alle 10 Jahre präventiv tauschen!** Ölprobe jährlich auf Wasser prüfen. |
| Confidence | documented |

### 24.3 Fallstudie: Yanmar SD50 — Galvanische Korrosion — Jeanneau Sun Odyssey 449 (BJ 2017)

| Aspekt | Detail |
|---|---|
| Boot | Jeanneau Sun Odyssey 449, BJ 2017, Yanmar 3JH57 + SD50 |
| Problem | Massive Korrosion am Saildrive-Gehäuse nach nur 3 Saisons |
| Diagnose | Saildrive-Gehäuse: großflächige Lochfraß-Korrosion, Anoden fast unverändert (!) |
| Ursache | 1) Kupferhaltiges Antifouling auf Saildrive aufgetragen (Werft-Fehler!) 2) Anoden hatten keinen metallischen Kontakt (Lack auf Kontaktfläche) |
| Reparatur | Saildrive-Gehäuse sanieren (Epoxy-Reparatur), korrektes AF, Anoden mit blankem Kontakt |
| Kosten | Sanierung: €1.800, Regress an Werft versucht |
| Lehre | **NIEMALS kupferhaltiges AF auf Saildrive!** Anoden-Kontaktflächen IMMER blank halten! |
| Confidence | documented |

### 24.4 Fallstudie: Borg Warner 71C — Falsches Öl — Contessa 32 (BJ 1978)

| Aspekt | Detail |
|---|---|
| Boot | Contessa 32, BJ 1978, Yanmar 2GM20 + Borg Warner Velvet Drive 71C |
| Problem | Kupplung rutscht plötzlich, Verbrennungsgeruch nach Ölwechsel |
| Diagnose | Beim Ölwechsel wurde ATF Dexron III statt SAE 30 Motoröl eingefüllt |
| Ursache | Werft/Eigner verwechselte Ölsorte (ATF ist rot und dünnflüssig → sieht „professionell" aus) |
| Reparatur | ATF ablassen, SAE 30 einfüllen, Lamellen prüfen — Lamellen bereits glasig → Lamellensatz tauschen |
| Kosten | Lamellensatz: €350, Öl: €20, Arbeit: €200 — **Gesamt: €570** |
| Lehre | **Immer Herstellerangabe beachten!** Borg Warner 71C/72C = SAE 30 Motoröl, KEIN ATF! |
| Confidence | documented |

### 24.5 Fallstudie: ZF 12M — Lamellenverschleiß im Charterbetrieb — Bavaria 34 (BJ 2012)

| Aspekt | Detail |
|---|---|
| Boot | Bavaria 34, BJ 2012, Volvo D1-30 + ZF 12M |
| Problem | Getriebe rutscht nach nur 1.500 Bh (typische Lebensdauer 3.000+ Bh) |
| Diagnose | Lamellen komplett abgenutzt, Öl schwarz, Metallspäne im Ölfilter |
| Ursache | Charterbetrieb mit häufigem Manövrieren, Kupplung halb eingelegt beim Anlegen, Ölwechsel-Intervall überschritten |
| Reparatur | Lamellensatz V/R, Ölpumpe (präventiv), Dichtungssatz, 3× Ölwechsel |
| Kosten | Material: €620, Arbeit: €450 — **Gesamt: €1.070** |
| Lehre | **Im Charterbetrieb: halbes Wartungsintervall!** Ölwechsel alle 125 Bh. Nie halb einkuppeln! |
| Confidence | documented |

### 24.6 Fallstudie: PRM 150 — Alignment-Problem — Hanse 385 (BJ 2016)

| Aspekt | Detail |
|---|---|
| Boot | Hanse 385, BJ 2016, Yanmar 3JH40 + PRM 150 |
| Problem | Zunehmende Vibrationen über 2 Saisons, Stopfbuchse leckt stärker |
| Diagnose | Alignment-Messung: 0,25 mm Winkelversatz (max. 0,10 mm erlaubt) |
| Ursache | Motorfundament hat sich durch GFK-Kriechverformung (Creep) abgesenkt (0,8 mm über 5 Jahre) |
| Reparatur | Motorfundament mit Laminat verstärken, Motor neu ausrichten (im Wasser!), Stopfbuchse nachstellen |
| Kosten | Alignment: €350, Fundament-Verstärkung: €500, Stopfbuchse: €80 — **Gesamt: €930** |
| Lehre | **Alignment alle 2 Jahre prüfen!** Besonders bei GFK-Fundamenten. |
| Confidence | documented |

### 24.7 Fallstudie: Volvo 120S — Kompletter Saildrive-Tausch — Dehler 34 (BJ 1998)

| Aspekt | Detail |
|---|---|
| Boot | Dehler 34, BJ 1998, Volvo 2020 + 120S Saildrive |
| Problem | Saildrive-Gehäuse massiv korrodiert, Kegelrad-Lager ausgelaufen, Membran 15+ Jahre alt |
| Diagnose | 120S wirtschaftlich nicht mehr reparabel (Gehäuse, Lager, Membran, Anoden) |
| Entscheidung | Volvo 130S als Ersatz (passt an selbe Rumpföffnung mit Adapterplatte) |
| Reparatur | 120S komplett ausbauen, Rumpföffnung prüfen/sanieren, 130S einbauen + neue Membran |
| Kosten | 130S neu: €5.800, Adapterplatte: €300, Montage: €1.200, Membran: €400 — **Gesamt: €7.700** |
| Lehre | **120S-Saildrives (BJ vor 2000) auf Gehäusekorrosion prüfen!** Tausch auf 130S sinnvoll. |
| Confidence | documented |

### 24.8 Fallstudie: Technodrive TMC60 — Ölverlust durch Vibration — X-Yachts X-35 (BJ 2010)

| Aspekt | Detail |
|---|---|
| Boot | X-Yachts X-35, BJ 2010, Yanmar 3YM30 + TMC60 |
| Problem | Ölflecken unter Getriebe, Ölstand fällt innerhalb einer Saison um 50 % |
| Diagnose | Simmerring Abtriebswelle undicht, zusätzlich Gehäusedichtung weint |
| Ursache | Motorvibrationen (ein defektes Motorlager) haben Simmerring-Lippe verschlissen |
| Reparatur | Simmerring tauschen (€25), Gehäusedichtung erneuern (€30), Motorlager tauschen (€180) |
| Kosten | Material: €235, Arbeit: €300 — **Gesamt: €535** |
| Lehre | **Ölverlust am Getriebe = immer auch Motorlager und Alignment prüfen!** |
| Confidence | documented |

---

## 25. OEM-Spezifikationen nach Bootshersteller

### 25.1 Segelboot-Hersteller und typische Getriebe

| Hersteller | Modellreihe | Motor | Getriebe/Saildrive | Untersetzung |
|---|---|---|---|---|
| Bavaria | 34–37 | Volvo D1-30/D2-40 | Volvo 130S Saildrive | 2,15:1 |
| Bavaria | 40–46 | Volvo D2-55/D2-75 | Volvo 130S/150S Saildrive | 2,15:1 / 2,33:1 |
| Hanse | 315–385 | Yanmar 3YM20/3JH40 | Yanmar SD25/SD50 | 2,21:1 / 2,64:1 |
| Hanse | 418–548 | Yanmar 4JH57/80 | Yanmar SD50/SD60 | 2,21:1 |
| Jeanneau | Sun Odyssey 349–440 | Yanmar 3JH40/57 | Yanmar SD50 | 2,21:1 |
| Jeanneau | Sun Odyssey 490+ | Yanmar 4JH80 | Yanmar SD60 | 1,94:1 |
| Beneteau | Oceanis 38–46 | Yanmar 3JH40/57 | Yanmar SD25/SD50 | 2,21:1 |
| Hallberg-Rassy | 34–40 | Volvo D2-40/D2-75 | ZF 15M/25 Wellenanlage | 2,14:1 / 2,63:1 |
| Hallberg-Rassy | 44+ | Volvo D2-75/D3 | ZF 25/45 Wellenanlage | 2,29:1 / 2,54:1 |
| Dehler | 30–38 | Volvo D1-30/D2-40 | Volvo 130S Saildrive | 2,15:1 |
| Najad | 34–45 | Volvo D2-40/D2-75 | ZF 15M/25 Wellenanlage | 2,14:1 / 2,63:1 |
| X-Yachts | X-35–X-43 | Yanmar 3YM/3JH | Yanmar SD25/TMC60 | 2,21:1 / 2,47:1 |
| Contest | 42–57 | Volvo D2-75/D3 | ZF 25/45 Wellenanlage | 2,29:1 |
| Oyster | 545–655 | Volvo D3/D4 | ZF 45/63 Wellenanlage | 2,54:1 |

(Confidence: documented / benchmark)

### 25.2 Motorboot-Hersteller und typische Getriebe

| Hersteller | Modellreihe | Motor | Getriebe | Untersetzung |
|---|---|---|---|---|
| Nimbus | 305–365 | Volvo D3/D4/D6 | Volvo HS25/HS63 | 1,56:1 – 2,27:1 |
| Sealine | C330–F430 | Volvo D4/D6 | ZF 45/63 | 1,52:1 – 2,29:1 |
| Princess | V39–V65 | Volvo D6/D8, CAT C9 | ZF 63/80/85 | 1,50:1 – 2,54:1 |
| Fairline | Targa 45–65 | Volvo D6/D8/D11 | ZF 63/80/220 | 1,50:1 – 3,03:1 |
| Grand Banks | 42–60 | Cummins QSB/QSC | ZF 45/63/80 | 2,00:1 – 3,50:1 |
| Linssen | 30–50 | Volvo D2/D3, Vetus | ZF 15/25, TMC60 | 2,14:1 – 2,63:1 |
| Aquanaut | Diverse | Vetus, Nanni | Technodrive TMC | 2,00:1 – 2,47:1 |

(Confidence: documented / benchmark)

---

## 26. Einbau- und Austausch-Anleitungen

### 26.1 Getriebeaustausch — Allgemeine Schritte (Wellenanlage)

**Vorbereitung:**
1. Motor-Getriebe-Kombination dokumentieren (Fotos, Maße)
2. Neues Getriebe bestellen (gleiche SAE-Größe, gleiche Untersetzung, gleiche Drehrichtung!)
3. Kupplungsflansch/Adapter prüfen (Motor-seitig und Wellen-seitig)
4. Propellerwelle markieren (Position)

**Ausbau altes Getriebe (4–8 Stunden):**
1. Getriebeöl ablassen
2. Bowdenzug am Getriebe lösen
3. Ölkühler-Leitungen lösen (Seewasser + Öl)
4. Propellenwelle von Getriebe-Abtriebsflansch lösen (4 Schrauben)
5. Motor-Getriebe-Schrauben lösen (SAE-Bellhousing, 4–6 Schrauben)
6. Getriebe vorsichtig nach hinten abziehen (Schwungscheibe/Kupplungsscheibe beachten!)
7. Getriebe herausheben (Gewicht! ZF 25 = 48 kg)

**Einbau neues Getriebe (4–8 Stunden):**
1. Schwungscheiben-Adapterplatte prüfen (gleiche SAE-Größe?)
2. Neues Getriebe auf Schwungscheibe/Kupplungsgehäuse aufsetzen
3. Zentrisch ausrichten (Zentrierbolzen/-hülsen)
4. SAE-Schrauben handfest, dann diagonal anziehen (Drehmoment beachten!)
5. Propellerwelle anflantschen (Flanschschrauben gleichmäßig)
6. Ölkühler-Leitungen anschließen
7. Bowdenzug montieren und einstellen (→ Kapitel 17.4)
8. Getriebeöl einfüllen (richtige Sorte und Menge!)
9. Alignment prüfen und einstellen (→ Kapitel 18.3)
10. Probefahrt mit Öl-/Temperatur-/Dichtheitskontrolle

**Kosten Werft (Getriebeaustausch):**
- Arbeit: €800–1.600 (je nach Zugänglichkeit)
- Material: Neues Getriebe + Zubehör
- Slipgebühr (falls notwendig): €150–300

(Confidence: documented)

### 26.2 Saildrive-Einbau (Neubau oder Tausch)

**Kritische Maße:**

| Parameter | Toleranz | Prüfmethode |
|---|---|---|
| Rumpfbohrung Durchmesser | ±1 mm vom Herstellermaß | Messschieber |
| Bohrungsposition (Längs) | ±3 mm | Lasermarking |
| Bohrungsposition (Quer) | ±2 mm (Mittellinie!) | Lotschnur von Mastfuß |
| Rumpfstärke an Bohrung | Min. 8 mm GFK (verstärkt!) | Ultraschall-Dickenmessung |
| Motorfundament-Höhe | Saildrive-spezifisch (Herstellerangabe) | Laser-Nivellierung |

**Warnung:** Saildrive-Einbau ist KEIN DIY-Projekt! Die Rumpfbohrung und Fundament-Konstruktion erfordern professionelle Ausführung.

(Confidence: documented)

---

## 27. Wartung und Lebensdauer

### 27.1 Wartungsplan — Wendegetriebe

| Intervall | Maßnahme | Gilt für |
|---|---|---|
| Alle 50 Bh (Erstölwechsel) | Öl wechseln | Alle neuen Getriebe |
| Alle 250 Bh oder jährlich | Öl wechseln, Ölstand prüfen | Alle Getriebe |
| Alle 250 Bh oder jährlich | Ölfilter wechseln (wenn vorhanden) | ZF 25+, PRM 260+ |
| Alle 250 Bh oder jährlich | Ölfarbe/-geruch prüfen (Wassereinbruch?) | Alle |
| Alle 250 Bh oder jährlich | Bowdenzug prüfen (Leichtgängigkeit) | Alle |
| Alle 500 Bh oder 2 Jahre | Ölkühler prüfen (Durchfluss, Dichtheit) | Alle mit Ölkühler |
| Alle 500 Bh oder 2 Jahre | Schaltgestänge prüfen und einstellen | Alle |
| Alle 1.000 Bh oder 5 Jahre | Lamellen prüfen (Dicke, Zustand) | Hydraulische Getriebe |
| Alle 2.000 Bh oder 10 Jahre | Ölpumpe prüfen (Förderdruck) | Hydraulische Getriebe |
| Alle 10 Jahre | Ölkühler präventiv tauschen | Alle mit Seewasser-Ölkühler |
| Alle 10 Jahre | Wellendichtringe tauschen (präventiv) | Alle |

(Confidence: documented)

### 27.2 Wartungsplan — Saildrive

| Intervall | Maßnahme | Gilt für |
|---|---|---|
| Alle 50 Bh (Erst-Ölwechsel) | Öl obere + untere Einheit wechseln | Alle neuen Saildrives |
| Alle 250 Bh oder jährlich | Öl obere Einheit wechseln | Alle Saildrives |
| Alle 500 Bh oder 2 Jahre | Öl untere Einheit wechseln | Alle Saildrives |
| Jährlich (Slipgang) | Anoden prüfen, ggf. tauschen | Alle Saildrives |
| Jährlich (Slipgang) | Membran Sichtprüfung (→ Kapitel 20.3) | Alle Saildrives |
| Jährlich (Slipgang) | Antifouling erneuern (kupferfrei!) | Alle Saildrives |
| Jährlich (Slipgang) | Kühlwassereinlass reinigen | Alle Saildrives |
| Jährlich | Bowdenzug/Schaltung prüfen | Alle Saildrives |
| Alle 7 Jahre (120S/130S, Yanmar) | MEMBRANWECHSEL (PFLICHT!) | Volvo 120S/130S, Yanmar SD |
| Alle 10 Jahre (150S, ZF) | MEMBRANWECHSEL (PFLICHT!) | Volvo 150S, ZF SD100/200 |
| Alle 10 Jahre | Propellerwellen-Dichtring tauschen | Alle Saildrives |
| Alle 10 Jahre | Gleitlager untere Einheit prüfen | Alle Saildrives |

(Confidence: documented)

### 27.3 Lebensdauer-Erwartungen

| Komponente | Lebensdauer (typisch) | Lebensdauer (gut gewartet) | Lebensdauer-Killer |
|---|---|---|---|
| Wendegetriebe komplett | 3.000–5.000 Bh | 6.000–10.000 Bh | Falsches Öl, kein Ölwechsel, Wasser im Öl |
| Lamellensatz | 2.000–3.000 Bh | 4.000–6.000 Bh | Charterbetrieb, halb eingekuppelt fahren |
| Ölpumpe | 3.000–5.000 Bh | 8.000+ Bh | Verschmutztes Öl |
| Simmerring Abtrieb | 2.000–4.000 Bh | 5.000–8.000 Bh | Fehlausrichtung, Wellenverschleiß |
| Ölkühler (Seewasser) | 8–12 Jahre | 15+ Jahre | Salzwasser, kein Spülen in Winterpause |
| Bowdenzug | 5–8 Jahre | 10+ Jahre | Korrosion, schlechte Verlegung |
| Saildrive komplett | 15–20 Jahre | 25+ Jahre | Korrosion, fehlende Anoden |
| Saildrive-Membran | 7–10 Jahre | 12–15 Jahre (EPDM) | UV, Chemikalien, falsche Montage |
| Saildrive-Anode (Zink) | 1–2 Jahre | — | Fremdströme |
| Saildrive-Anode (Alu) | 2–4 Jahre | — | Fremdströme |

(Confidence: benchmark)

---

## 28. Weltweite Bezugsquellen

### 28.1 ZF Marine — Händler/Distributoren

| Region | Händler | Website | Bemerkung |
|---|---|---|---|
| Deutschland | SVB | svb-marine.de | Großes Lager, schnelle Lieferung |
| Deutschland | Toplicht | toplicht.de | ZF-Vertragshändler |
| Deutschland | Compass24 | compass24.de | Online-Versand |
| Niederlande | Allpa Marine | allpa.nl | Großhändler Europa |
| UK | TBS Boats | tbs-boats.co.uk | ZF-Service UK |
| UK | Beta Marine | betamarine.co.uk | ZF/PRM als OEM |
| USA | Mack Boring | mackboring.com | ZF-Hauptdistributor USA |
| USA | Transatlantic Diesel | transatlanticdiesel.com | ZF-Spezialist |
| Mittelmeer | Diverse Volvo/Yanmar-Stützpunkte | — | Regional |

(Confidence: documented)

### 28.2 Saildrive-Spezialisten

| Firma | Land | Spezialgebiet | Kontakt |
|---|---|---|---|
| Gotthardt Marine Service | DE | Volvo Saildrive Überholung | gotthardt-marine.de |
| Hamm Motoren | DE | Yanmar Service + Saildrive | hamm-motoren.de |
| RotorSwing / YachtTeile24 | DE | Saildrive-Ersatzteile | yachtteile24.de |
| Deltaparts | NL | Saildrive-Membranen alle Hersteller | deltaparts.nl |
| Engines Plus | UK | Volvo/Yanmar Saildrive Service | enginesplus.co.uk |
| Drinkwaard Marine | NL | ZF Saildrive Service | drinkwaardmarine.nl |

(Confidence: documented)

---

## 29. Preisvergleich

### 29.1 Neugetriebe-Preise (2026, inkl. MwSt., ca.)

| Getriebe | Leistungsklasse | Preis neu | Bemerkung |
|---|---|---|---|
| ZF 10M | 30 PS | €1.200–1.600 | Auslaufmodell |
| ZF 12M | 45 PS | €1.600–2.200 | Auslaufmodell |
| ZF 15M | 60 PS | €2.200–2.800 | Standardgetriebe Segelboot |
| ZF 25 | 130 PS | €3.500–4.500 | Standard Motoryacht |
| ZF 45 | 240 PS | €5.500–7.000 | Motoryacht mittel |
| TMC40 | 40 PS | €1.200–1.600 | Preiswerte Alternative |
| TMC60 | 70 PS | €1.600–2.200 | Preiswerte Alternative |
| PRM 80 | 25 PS | €600–900 | Günstigstes Getriebe |
| PRM 150 | 90 PS | €1.800–2.500 | Gutes Preis-Leistung |
| Yanmar KM2P | 30 PS | €1.800–2.400 | Nur mit Yanmar Motor |
| Yanmar KM3P | 50 PS | €2.200–2.800 | Nur mit Yanmar Motor |

(Confidence: benchmark)

### 29.2 Saildrive-Preise (2026, inkl. MwSt., ca.)

| Saildrive | Leistungsklasse | Preis neu | Bemerkung |
|---|---|---|---|
| Volvo 130S | 75 PS | €5.500–7.000 | Meistverkauft |
| Volvo 150S | 110 PS | €7.000–9.500 | Aktuelle Top-Version |
| Yanmar SD25 | 40 PS | €4.500–5.500 | |
| Yanmar SD50 | 55 PS | €5.500–7.000 | |
| Yanmar SD60 | 75 PS | €7.000–9.000 | |
| ZF SD100 | 50 PS | €4.500–5.500 | Herstellerunabhängig |
| ZF SD200 | 80 PS | €6.000–7.500 | Mit PTO |

(Confidence: benchmark)

### 29.3 Wartungskosten-Vergleich (jährlich, typisch)

| Getriebe-Typ | Ölwechsel | Filter | Anoden | Membran (anteilig) | Gesamt/Jahr |
|---|---|---|---|---|---|
| ZF 15M (Wellenanlage) | €25 | €0 | €0 | — | **€25** |
| ZF 25 (Wellenanlage) | €35 | €20 | €0 | — | **€55** |
| Volvo 130S Saildrive | €30 (oben) + €15 (unten) | €0 | €50 | €60 (÷7 Jahre) | **€155** |
| Yanmar SD50 Saildrive | €25 (oben) + €15 (unten) | €0 | €40 | €45 (÷7 Jahre) | **€125** |
| ZF SD100 Saildrive | €25 (oben) + €15 (unten) | €0 | €35 | €40 (÷10 Jahre) | **€115** |

**Fazit:** Saildrives sind im Unterhalt 2–5× teurer als Wellenanlagen, hauptsächlich wegen Anoden und Membranwechsel.

(Confidence: benchmark)

---

## 30. Forum-Erfahrungsberichte

### 30.1 Relevante Foren

| Forum | Sprache | URL | Relevanz |
|---|---|---|---|
| Segeln-Forum.de | DE | segeln-forum.de | Sehr aktiv, viele Saildrive-Threads |
| Boote-Forum.de | DE | boote-forum.de | Motorboote + Segelboote, technisch gut |
| YachtForum.at | DE | yachtforum.at | Österreichische Binnenschiffer + Segler |
| Cruisers Forum | EN | cruisersforum.com | Internationale Langfahrtsegler |
| SailNet | EN | sailnet.com | US-fokussiert, viel Velvet-Drive-Wissen |
| The Hull Truth | EN | thehulltruth.com | Motorboote, US |
| YBW Forum | EN | ybw.com/forums | UK-fokussiert, viel PRM-Wissen |

### 30.2 Typische Forum-Erkenntnisse (Zusammenfassung)

**Zum Thema ZF-Getriebe:**
- „ZF 10M/12M sind unkaputtbar, wenn man das Öl wechselt" — häufigste Aussage
- „Erstes Zeichen von Problemen = Schaltung wird weicher, dauert länger bis Vorwärtsschub kommt"
- „Ölkühler-Wechsel nach 10 Jahren ist die billigste Versicherung gegen Totalschaden"

**Zum Thema Saildrive-Membran:**
- „7 Jahre ist Maximalwert, nicht Empfehlung. Besser alle 5 Jahre im Mittelmeer."
- „Membranwechsel ist die beste Investition am Boot — 500 Euro gegen Untergang"
- „NIEMALS Membran im eingebauten Zustand mit Hochdruckreiniger bearbeiten!"

**Zum Thema Antifouling auf Saildrive:**
- „Prop Speed ist die beste Lösung — kein AF-Thema mehr, Saildrive bleibt sauber"
- „Wir haben versehentlich International Micron auf den Saildrive gestrichen — nach 2 Jahren war das Bein zur Hälfte aufgelöst"

(Confidence: documented)

---

## 31. YouTube-Ressourcen

| Kanal | Sprache | Thema | URL/Stichwort |
|---|---|---|---|
| Sailing Uma | EN | Saildrive-Membranwechsel live | „Saildrive diaphragm replacement" |
| Sail Life | EN | ZF-Getriebe Überholung komplett | „Marine gearbox rebuild" |
| BootsProfis | DE | Volvo 130S Wartung komplett | „Saildrive Wartung Volvo" |
| Motorboot-Online | DE | Alignment-Tutorial | „Motorausrichtung Boot" |
| Steve Goodwin (Marinediesel) | EN | Velvet Drive Overhaul | „Velvet Drive 71C rebuild" |
| Beta Marine (offiziell) | EN | PRM-Getriebe-Wartung | „PRM gearbox service" |
| Marine Diesel Basics | EN | Getriebe-Diagnose | „Marine transmission troubleshooting" |
| Salty Abandon | EN | Yanmar Saildrive SD25 Wartung | „Yanmar saildrive service" |
| Volvo Penta (offiziell) | EN/DE | 130S/150S Wartungsvideos | „Volvo Penta saildrive maintenance" |

(Confidence: documented)

---

## 32. Experten-Referenzen

### 32.1 Fachliteratur

| Titel | Autor | Verlag | Jahr | Relevanz |
|---|---|---|---|---|
| Marine Diesel Engines | Nigel Calder | Adlard Coles | 2021 | Kapitel Getriebe und Antrieb |
| Boatowner's Mechanical & Electrical Manual | Nigel Calder | International Marine | 2015 | Umfassend Antriebsstrang |
| AC Maintenance & Repair Manual for Diesel Engines | Jean-Luc Pallas | Adlard Coles | 2006 | Getriebediagnose |
| Saildrive Handbuch | Volvo Penta (Service Manual) | Volvo | diverse | Offizielle Referenz |
| ZF Marine Getriebe — Service Manual | ZF Friedrichshafen | ZF | diverse | Offizielle Referenz |
| The 12 Volt Bible for Boats | Miner Brotherton | International Marine | 2002 | Bonding, galvanischer Schutz |

### 32.2 Zertifizierungen und Schulungen

| Anbieter | Schulung | Zielgruppe | Ort |
|---|---|---|---|
| ZF Marine Academy | Getriebe-Service Level 1–3 | Werfttechniker | Padova (IT), online |
| Volvo Penta Academy | Saildrive Service | Volvo-Servicepartner | Göteborg (SE), online |
| Yanmar Academy | SD-Serie Wartung | Yanmar-Servicepartner | Diverse Standorte |
| ABYC | Marine Systems Certification | Techniker (US-Standard) | USA, online |
| BYS (British Yacht Survey) | Antriebsstrang-Inspektion | Gutachter | UK |

(Confidence: documented)

---

## 33. FAQ

### 33.1 Allgemein — Getriebe

**F1: Wie erkenne ich, welches Getriebe in meinem Boot ist?**
A: Typenschild am Getriebegehäuse (oben oder seitlich). Zeigt Hersteller, Modell, Seriennummer, Untersetzung. Bei alten Booten oft unleserlich → Werft oder Hersteller kontaktieren mit Motor-Seriennummer.
(Confidence: documented)

**F2: Kann ich ein ZF-Getriebe gegen ein PRM tauschen?**
A: Grundsätzlich ja, wenn die SAE-Gehäusegröße (SAE 2, 3, 4, 5) übereinstimmt und die Untersetzung passt. Abtriebsflansch/Konus muss geprüft werden. Bowdenzug-Anschluss kann unterschiedlich sein.
(Confidence: documented)

**F3: Mein Getriebe hat 3.000 Betriebsstunden — muss ich es überholen?**
A: Nicht zwingend, wenn Öl sauber ist, Schaltung einwandfrei funktioniert und keine Geräusche auftreten. Lamellen prüfen lassen (Spiel messen) ist sinnvoll. Präventiv Ölpumpe prüfen.
(Confidence: documented)

**F4: Was kostet eine Getriebe-Überholung?**
A: Typisch €800–2.000 für ZF 10M–25 (Lamellen + Dichtungen + Arbeitszeit). Bei größeren Getrieben €2.000–5.000. Neue Lamellen allein: €300–700. Ölpumpe: €200–400.
(Confidence: benchmark)

**F5: Kann ich das Getriebe selbst überholen?**
A: Mit mechanischer Erfahrung und ZF-Werkstatthandbuch ja, bei ZF 10M/12M/15M relativ machbar. Spezialwerkzeug für Lamellen-Abzieher. Größere Getriebe (ZF 25+) erfordern Spezialisten.
(Confidence: documented)

**F6: Warum ist ATF rot und kein Motoröl?**
A: ATF (Automatic Transmission Fluid) hat spezielle Reibwerte für Lamellenkupplungen, enthält Detergentien und Anti-Schaum-Additive. Motoröl hat andere Reibwerte und kann Lamellen beschädigen. Ausnahme: Borg Warner Velvet Drive 71C/72C — hier ist SAE 30 Motoröl korrekt!
(Confidence: documented)

**F7: Dexron III oder Dexron VI?**
A: Dexron VI ist der Nachfolger von Dexron III und ist rückwärtskompatibel. ZF empfiehlt für neue Getriebe Dexron VI, akzeptiert aber Dexron III. Nicht mischen! Bei Wechsel komplett ablassen.
(Confidence: documented)

**F8: Was bedeutet das Untersetzungsverhältnis 2,63:1?**
A: Die Eingangswelle dreht sich 2,63× schneller als die Ausgangswelle. Bei 3.000 U/min Motordrehzahl → 3.000 ÷ 2,63 = 1.141 U/min Propellerdrehzahl.
(Confidence: calculated)

**F9: Kann ich die Untersetzung meines Getriebes ändern?**
A: Nicht im eingebauten Zustand. Man muss ein anderes Getriebe mit der gewünschten Untersetzung kaufen. Bei ZF gibt es den gleichen Getriebetyp mit verschiedenen Untersetzungen.
(Confidence: documented)

**F10: Mein Getriebe macht „Klack" beim Einlegen von Vorwärts — normal?**
A: Ein leichtes „Klack" bei niedriger Drehzahl ist bei hydraulischen Getrieben normal (Lamellen greifen). Lautes Schlagen → Schalteinstellung prüfen. Knirschen → mechanische Kupplung prüft, Schalten nur bei niedriger Drehzahl!
(Confidence: documented)

### 33.2 Allgemein — Saildrive

**F11: Wie alt kann eine Saildrive-Membran maximal werden?**
A: Theoretisch 15+ Jahre (EPDM-Material). Die 7- bzw. 10-Jahres-Empfehlung der Hersteller ist eine Sicherheitsmarge. In der Praxis: nach 7 Jahren beginnt Materialermüdung. Nicht aufreizen — eine Membran kostet €300, ein Boot sinkt für mehr.
(Confidence: documented)

**F12: Kann ich die Membran selbst wechseln?**
A: Ja, mit mechanischem Geschick und dem richtigen Material. Die Prozedur ist nicht komplex, aber MUSS sorgfältig erfolgen. Aushärtezeit des Dichtstoffs einhalten! Bilgepumpen-Test nach Einsetzen.
(Confidence: documented)

**F13: Warum darf kein kupferhaltiges Antifouling auf den Saildrive?**
A: Das Saildrive-Gehäuse ist aus Aluminium. Kupfer + Aluminium + Salzwasser = galvanisches Element → Aluminium löst sich auf (Korrosion). Darum: nur kupferfreies AF oder Prop Speed.
(Confidence: documented)

**F14: Zink- oder Aluminium-Anoden für den Saildrive?**
A: In Salzwasser: beide funktionieren, Aluminium ist besser (höhere Kapazität, umweltfreundlicher). In Brackwasser: nur Aluminium! In Süßwasser: Magnesium (aber Saildrives sind selten in Süßwasser).
(Confidence: documented)

**F15: Mein Saildrive vibriert stärker als früher — warum?**
A: Mögliche Ursachen: Propeller-Unwucht (Bewuchs, Beschädigung), Gleitlager untere Einheit verschlissen, Motorfundament-Gummilager gealtert, Bewuchs am Saildrive-Bein. Propeller zuerst prüfen!
(Confidence: documented)

**F16: Saildrive oder Wellenanlage — was ist besser?**
A: Keine pauschale Antwort. Saildrive: leichter, weniger Vibrationen, einfacher Einbau, aber teurer im Unterhalt und Membran-Risiko. Wellenanlage: robuster, günstiger im Unterhalt, aber aufwändiger Einbau und Alignment nötig. Für Segelboote bis 50 ft ist Saildrive Standard geworden.
(Confidence: documented)

**F17: Kann ich einen Volvo-Saildrive gegen einen Yanmar tauschen?**
A: Theoretisch nein, weil die Rumpfbohrung und Befestigungspunkte unterschiedlich sind. In der Praxis gibt es Adapterplatten für den Wechsel 120S→130S (gleicher Hersteller), aber Volvo→Yanmar erfordert GFK-Arbeiten am Rumpf. Sehr aufwändig.
(Confidence: documented)

**F18: Mein Saildrive-Bein hat weiße Flecken — was ist das?**
A: Weiße Flecken auf dem Aluminium = Oxidation/Korrosion. Leicht = normal (Oberflächenoxidation). Stark = galvanisches Problem (falsches AF, fehlende Anoden, Fremdströme). Sofort Anoden und AF prüfen!
(Confidence: documented)

**F19: Was kostet ein kompletter Saildrive-Tausch?**
A: Saildrive neu: €5.000–9.000, Einbau inkl. Membran/Anoden: €1.500–3.000, Gesamt: €6.500–12.000. Gebraucht (überholt): €2.500–5.000.
(Confidence: benchmark)

**F20: Mein Faltpropeller klappt nicht richtig auf — was tun?**
A: Häufigste Ursache: Bewuchs in den Scharnieren (Muscheln, Pocken). Am Kran: Propeller-Scharniere reinigen und mit wasserfestem Fett (z.B. Lanocote) schmieren. Bei Flexofold: Blätter einzeln prüfen, Federung testen.
(Confidence: documented)

### 33.3 Spezifische Fragen

**F21: Mein ZF 15M hat nach 2.000 Bh Metallteilchen im Öl — normal?**
A: NEIN! Feiner Metallabrieb ist bis zu einem gewissen Grad normal, aber sichtbare Partikel oder Magnettest positiv → Getriebe öffnen und inspizieren. Lamellen oder Lager verschlissen.
(Confidence: documented)

**F22: Kann ich die Saildrive-Membran im Wasser prüfen?**
A: Von außen nur eingeschränkt (Taucher kann Zustand der Membranfalte sehen). Von innen: Bilge trockenlegen, feuchte Stellen um Saildrive-Öffnung suchen. Zuverlässige Prüfung nur an Land.
(Confidence: documented)

**F23: Mein Volvo 130S verliert Öl aus der oberen Einheit — Saildrive defekt?**
A: Nicht unbedingt der Saildrive. Häufig ist der Simmerring am Eingang (Motor-Seite) oder am Ölmessstab undicht. Erst Dichtungen prüfen, dann Getriebe. Ölverlust immer ernst nehmen — auch kleine Mengen!
(Confidence: documented)

**F24: Warum summt mein Getriebe bei 2.500 U/min?**
A: Resonanzfrequenz. Bei bestimmten Drehzahlen können Getriebe-Zahnräder in Resonanz mit dem Getriebegehäuse oder dem Motorfundament geraten. Wenn nur bei einer exakten Drehzahl → normal (Drehzahl meiden). Wenn bei vielen Drehzahlen → Lager oder Zahnrad defekt.
(Confidence: documented)

**F25: Wie prüfe ich, ob mein Ölkühler undicht ist?**
A: Ölkühler ausbauen, Seewasserseite verschließen, mit 2 bar Druckluft beaufschlagen und in Wassereimer tauchen → Blasen = undicht. Alternativ: Ölprobe auf Wasserspuren analysieren.
(Confidence: documented)

**F26: Mein Saildrive hat keinen Kühlwassereinlass — ist der verstopft?**
A: Ja, wahrscheinlich. Der Kühlwassereinlass sitzt am Saildrive-Bein (kleines Sieb/Gitter). Bei Bewuchs verstopft er → Motor überhitzt! Bei jedem Slipgang reinigen. Im Wasser: Taucher kann reinigen.
(Confidence: documented)

**F27: Kann ich anstatt ZF ATF auch Motul Multi ATF verwenden?**
A: Multi-ATF-Produkte (Motul, Liqui Moly, Castrol) sind für Dexron III/VI-Anwendungen geeignet und von ZF akzeptiert, sofern sie die Dexron-III/VI-Spezifikation erfüllen. ABER: Bei Garantie immer Herstellerangabe beachten!
(Confidence: documented)

---

## 34. Glossar

| Begriff (DE) | Begriff (EN) | Erklärung |
|---|---|---|
| Abtriebsflansch | Output flange | Flansch an der Getriebeausgangswelle zur Verbindung mit Propellerwelle |
| Alignment | Alignment | Ausrichtung der Motorwelle zur Propellerwelle |
| Anode (Opfer-) | Sacrificial anode | Weniger edles Metall, das sich anstelle des geschützten Metalls auflöst |
| Antifouling | Antifouling | Unterwasseranstrich gegen Bewuchs |
| ATF | ATF (Automatic Transmission Fluid) | Spezialöl für hydraulische Kupplungssysteme |
| Bellhousing | Bellhousing | Kupplungsglocke — Verbindungsgehäuse Motor↔Getriebe |
| Bilge | Bilge | Tiefster Punkt im Bootsinneren, wo sich Wasser sammelt |
| Bonding | Bonding | Elektrische Verbindung aller metallischen Unterwasserteile |
| Bowdenzug | Push-pull cable | Flexibles Betätigungselement für Schaltung |
| Dexron | Dexron | ATF-Spezifikation (General Motors), Standard für marine ATF |
| Eingangsleistung | Input power | Maximale Motorleistung, die das Getriebe aufnehmen kann |
| EPDM | EPDM rubber | Ethylen-Propylen-Dien-Kautschuk (UV-beständiger Gummi) |
| Faltpropeller | Folding propeller | Propeller, dessen Blätter sich beim Segeln zusammenklappen |
| Feathering-Propeller | Feathering propeller | Propeller mit verstellbaren Blättern (Fahnenstellung) |
| Flansch | Flange | Scheibenförmige Verbindung zweier Wellen |
| Fremdströme | Stray currents | Vagabundierende elektrische Ströme im Wasser (galvanische Korrosion) |
| Galvanische Korrosion | Galvanic corrosion | Korrosion durch Kontakt verschiedener Metalle in Elektrolyt |
| Getriebe | Gearbox / Transmission | Wendegetriebe — Drehrichtungsumkehr + Untersetzung |
| GL-4 / GL-5 | GL-4 / GL-5 (Gear Lubricant) | API-Spezifikation für Getriebeöl (GL-5 = höherer EP-Anteil) |
| Gleitlager | Plain bearing / Sleeve bearing | Lager ohne Wälzkörper, Welle gleitet auf Lagerfläche |
| Heulen | Whine | Geräusch durch Zahneingriff im Getriebe |
| Hurth | Hurth (Brand) | Historischer Getriebehersteller, jetzt ZF Marine |
| Hydraulische Kupplung | Hydraulic clutch | Kupplungssystem mit Öldruck auf Lamellenpakete |
| Kegelrad | Bevel gear | 90°-Umlenkung im Saildrive (obere→untere Einheit) |
| Klauenkupplung | Dog clutch | Mechanische Kupplung durch ineinandergreifende Klauen |
| Konus | Taper / Cone | Kegelige Wellen-Aufnahme für Propeller oder Flansch |
| Kühlwassereinlass | Cooling water inlet | Einlass für Seewasser am Saildrive-Bein (Motorkühlung) |
| Lamelle (Reib-) | Friction disc | Kupplungsscheibe mit Reibbelag |
| Lamelle (Stahl-) | Steel disc | Kupplungsscheibe aus Stahl (Gegenstück zur Reiblamelle) |
| Membran | Diaphragm | Gummi-Manschette am Saildrive-Rumpfdurchbruch |
| Misalignment | Misalignment | Fehlausrichtung Motor–Propellerwelle |
| Neutral | Neutral | Leerlaufstellung — Motor läuft, Propeller ist entkoppelt |
| Ölkühler | Oil cooler | Wärmetauscher zur Kühlung des Getriebeöls |
| Ölpumpe | Oil pump | Fördert Öl im hydraulischen Getriebekreislauf |
| Planetengetriebe | Planetary gear | Untersetzungsgetriebe mit Sonnenrad, Planetenrädern, Hohlrad |
| Prop Speed | Prop Speed (Brand) | Silikon-basierte Antifouling-Beschichtung für Propeller/Saildrive |
| Propellerwelle | Propeller shaft | Welle vom Getriebe zum Propeller |
| PTO | Power Take-Off | Nebenantrieb am Getriebe (Generator, Hydraulik) |
| Rückwärtsgang | Reverse | Drehrichtungsumkehr für Rückwärtsfahrt |
| SAE-Gehäuse | SAE housing | Standardisierte Gehäuse-Anschlussmaße (SAE 1–5) |
| Saildrive | Saildrive | Integriertes Antriebssystem durch den Rumpfboden |
| Schaltgestänge | Shift linkage | Verbindung Bedienpult → Getriebe |
| Schlupf | Slip | Differenz zwischen theoretischer und tatsächlicher Geschwindigkeit |
| Schwungscheibe | Flywheel | Schwungmasse am Motor, Getriebe-Anschluss |
| Simmerring | Oil seal / Lip seal | Radialwellendichtring (Gummi-Dichtlippe auf Welle) |
| Spannband | Hose clamp / Band clamp | Befestigungsband für Saildrive-Membran |
| Stevenrohr | Stern tube | Rohr durch den Rumpf, führt die Propellerwelle |
| Stirnradgetriebe | Spur gear | Getriebe mit geradverzahnten Zahnrädern |
| Untersetzung | Gear ratio / Reduction ratio | Verhältnis Eingangsdrehzahl zu Ausgangsdrehzahl |
| Vorwärtsgang | Forward | Standardfahrtrichtung |
| Wellendichtring | Shaft seal / Oil seal | Dichtung an rotierender Welle (Simmerring) |
| Wendegetriebe | Marine gearbox / Marine transmission | Getriebe mit Vorwärts/Neutral/Rückwärts |

(Confidence: documented)

---

## 35. Pydantic v2 Modelle

### 35.1 Getriebe-Datenmodelle

```python
"""
AYDI — Getriebe und Saildrive Datenmodelle
Pydantic v2: model_config = {"from_attributes": True} — NIEMALS class Config
"""

from pydantic import BaseModel, Field
from typing import Optional
from enum import Enum
from datetime import date


class GetriebeTyp(str, Enum):
    """Typ des Wendegetriebes."""
    MECHANISCH_KLAUE = "mechanisch_klaue"
    HYDRAULISCH_LAMELLE = "hydraulisch_lamelle"
    HYDRAULISCH_KONUS = "hydraulisch_konus"


class KupplungsZustand(str, Enum):
    """Zustand der Kupplungslamellen."""
    NEU = "neu"
    GUT = "gut"
    VERSCHLISSEN = "verschlissen"
    DEFEKT = "defekt"
    NICHT_GEPRUEFT = "nicht_geprueft"


class OelTyp(str, Enum):
    """Getriebeöltyp."""
    ATF_DEXRON_III = "atf_dexron_iii"
    ATF_DEXRON_VI = "atf_dexron_vi"
    SAE_80W90_GL4 = "sae_80w90_gl4"
    SAE_75W90_GL5 = "sae_75w90_gl5"
    SAE_30_MOTOROEL = "sae_30_motoroel"
    HERSTELLER_SPEZIFISCH = "hersteller_spezifisch"


class OelZustand(str, Enum):
    """Zustand des Getriebeöls."""
    FRISCH = "frisch"
    GUT = "gut"
    DUNKEL = "dunkel"
    SCHWARZ = "schwarz"
    MILCHIG = "milchig"  # ALARM: Wasser im Öl!
    METALLISCH = "metallisch"  # ALARM: Metallabrieb!


class ConfidenceLevel(str, Enum):
    """Confidence-Level gemäß AYDI-Framework."""
    MEASURED = "measured"
    CALCULATED = "calculated"
    VISUAL_HIGH = "visual_high"
    VISUAL_MEDIUM = "visual_medium"
    VISUAL_LOW = "visual_low"
    VISUAL_INSUFFICIENT = "visual_insufficient"
    ESTIMATED = "estimated"
    BENCHMARK = "benchmark"
    DOCUMENTED = "documented"


class GetriebeSpezifikation(BaseModel):
    """Technische Spezifikation eines Wendegetriebes."""

    model_config = {"from_attributes": True}

    hersteller: str = Field(..., description="Hersteller (z.B. ZF, PRM, Yanmar)")
    modell: str = Field(..., description="Modellbezeichnung (z.B. ZF 15M)")
    typ: GetriebeTyp = Field(..., description="Kupplungstyp")
    max_eingangsleistung_kw: float = Field(..., ge=0, description="Max. Eingangsleistung in kW")
    max_eingangsleistung_ps: float = Field(..., ge=0, description="Max. Eingangsleistung in PS")
    untersetzung: float = Field(..., gt=0, description="Untersetzungsverhältnis (z.B. 2.63)")
    untersetzung_optionen: list[float] = Field(
        default_factory=list,
        description="Verfügbare Untersetzungsverhältnisse"
    )
    gewicht_kg: float = Field(..., ge=0, description="Gewicht in kg")
    oel_typ: OelTyp = Field(..., description="Vorgeschriebener Öltyp")
    oel_menge_l: float = Field(..., ge=0, description="Ölmenge in Litern")
    oel_wechsel_intervall_bh: int = Field(..., ge=0, description="Ölwechselintervall in Betriebsstunden")
    sae_gehaeuse: Optional[str] = Field(None, description="SAE-Gehäusegröße (z.B. SAE 3)")
    abtriebsflansch: Optional[str] = Field(None, description="Abtriebsflansch-Beschreibung")
    oelkuehler: bool = Field(False, description="Hat Ölkühler (Seewassergekühlt)")
    pto_option: bool = Field(False, description="PTO-Nebenantrieb verfügbar")
    neupreis_eur_min: Optional[float] = Field(None, ge=0, description="Neupreis min. EUR")
    neupreis_eur_max: Optional[float] = Field(None, ge=0, description="Neupreis max. EUR")
    produktionszeitraum: Optional[str] = Field(None, description="Produktionszeitraum")
    confidence: ConfidenceLevel = Field(
        ConfidenceLevel.DOCUMENTED,
        description="Confidence-Level der Spezifikation"
    )


class SaildriveTyp(str, Enum):
    """Saildrive-Hersteller/Typ."""
    VOLVO_120S = "volvo_120s"
    VOLVO_130S = "volvo_130s"
    VOLVO_150S = "volvo_150s"
    YANMAR_SD20 = "yanmar_sd20"
    YANMAR_SD25 = "yanmar_sd25"
    YANMAR_SD50 = "yanmar_sd50"
    YANMAR_SD60 = "yanmar_sd60"
    ZF_SD100 = "zf_sd100"
    ZF_SD200 = "zf_sd200"


class MembranZustand(str, Enum):
    """Zustand der Saildrive-Membran."""
    NEU = "neu"
    GUT = "gut"
    OBERFLAECHENRISSE = "oberflaechenrisse"
    SPROEDE = "sproede"
    VERFORMT = "verformt"
    GERISSEN = "gerissen"  # KRITISCH!
    NICHT_GEPRUEFT = "nicht_geprueft"


class AnodenMaterial(str, Enum):
    """Material der Opferanoden."""
    ZINK = "zink"
    ALUMINIUM = "aluminium"
    MAGNESIUM = "magnesium"


class AnodenZustand(str, Enum):
    """Zustand der Opferanoden."""
    NEU = "neu"
    UEBER_50_PROZENT = "ueber_50_prozent"
    ZWISCHEN_30_50 = "zwischen_30_50"
    UNTER_30_PROZENT = "unter_30_prozent"
    AUFGELOEST = "aufgeloest"
    KEINE_AUFLOESUNG = "keine_aufloesung"  # FALSCH! Prüfen!


class SaildriveSpezifikation(BaseModel):
    """Technische Spezifikation eines Saildrives."""

    model_config = {"from_attributes": True}

    hersteller: str = Field(..., description="Hersteller (Volvo, Yanmar, ZF)")
    modell: str = Field(..., description="Modellbezeichnung (z.B. 130S)")
    typ: SaildriveTyp = Field(..., description="Saildrive-Typ")
    max_motorleistung_kw: float = Field(..., ge=0, description="Max. Motorleistung in kW")
    max_motorleistung_ps: float = Field(..., ge=0, description="Max. Motorleistung in PS")
    untersetzung: float = Field(..., gt=0, description="Untersetzungsverhältnis")
    untersetzung_optionen: list[float] = Field(
        default_factory=list,
        description="Verfügbare Untersetzungsverhältnisse"
    )
    gewicht_kg: float = Field(..., ge=0, description="Gewicht ohne Propeller in kg")
    oel_typ_obere_einheit: OelTyp = Field(..., description="Öltyp obere Einheit")
    oel_menge_obere_einheit_l: float = Field(..., ge=0, description="Ölmenge obere Einheit in l")
    oel_typ_untere_einheit: OelTyp = Field(..., description="Öltyp untere Einheit")
    oel_menge_untere_einheit_l: float = Field(..., ge=0, description="Ölmenge untere Einheit in l")
    membran_intervall_jahre: int = Field(..., ge=1, description="Membranwechsel-Intervall in Jahren")
    propeller_konus_mm: float = Field(..., ge=0, description="Propellerkonus-Durchmesser in mm")
    neupreis_eur_min: Optional[float] = Field(None, ge=0, description="Neupreis min. EUR")
    neupreis_eur_max: Optional[float] = Field(None, ge=0, description="Neupreis max. EUR")
    produktionszeitraum: Optional[str] = Field(None, description="Produktionszeitraum")
    confidence: ConfidenceLevel = Field(
        ConfidenceLevel.DOCUMENTED,
        description="Confidence-Level"
    )


class MembranBewertung(BaseModel):
    """Bewertung der Saildrive-Membran."""

    model_config = {"from_attributes": True}

    saildrive_typ: SaildriveTyp = Field(..., description="Saildrive-Typ")
    alter_jahre: float = Field(..., ge=0, description="Alter der Membran in Jahren")
    zustand: MembranZustand = Field(..., description="Visueller Zustand")
    empfehlung: str = Field(..., description="Handlungsempfehlung")
    dringlichkeit: str = Field(
        ...,
        description="Dringlichkeit: sofort | naechster_slipgang | planbar | ok"
    )
    naechste_pruefung: Optional[str] = Field(None, description="Empfohlener Zeitpunkt nächste Prüfung")
    geschaetzte_restlebensdauer_jahre: Optional[float] = Field(
        None, ge=0,
        description="Geschätzte Restlebensdauer in Jahren"
    )
    confidence: ConfidenceLevel = Field(
        ConfidenceLevel.VISUAL_MEDIUM,
        description="Confidence-Level der Bewertung"
    )


class AnodenBewertung(BaseModel):
    """Bewertung der Saildrive-Anoden."""

    model_config = {"from_attributes": True}

    material: AnodenMaterial = Field(..., description="Anodenmaterial")
    zustand: AnodenZustand = Field(..., description="Zustand der Anode")
    position: str = Field(..., description="Position (bein | propellernabe | obere_einheit)")
    empfehlung: str = Field(..., description="Handlungsempfehlung")
    verdacht_fremdstroeme: bool = Field(False, description="Verdacht auf Fremdströme")
    confidence: ConfidenceLevel = Field(
        ConfidenceLevel.VISUAL_HIGH,
        description="Confidence-Level"
    )


class GetriebeBefund(BaseModel):
    """Diagnosebefund für ein Wendegetriebe oder Saildrive."""

    model_config = {"from_attributes": True}

    befund_id: str = Field(..., description="Eindeutige Befund-ID")
    datum: date = Field(..., description="Datum des Befunds")
    komponente: str = Field(..., description="Betroffene Komponente")
    beschreibung: str = Field(..., description="Befundbeschreibung (Deutsch)")
    schweregrad: str = Field(
        ...,
        description="Schweregrad: info | warnung | kritisch | sofort_handeln"
    )
    empfehlung: str = Field(..., description="Handlungsempfehlung (Deutsch)")
    geschaetzte_kosten_min: Optional[float] = Field(None, ge=0, description="Geschätzte Kosten min. EUR")
    geschaetzte_kosten_max: Optional[float] = Field(None, ge=0, description="Geschätzte Kosten max. EUR")
    confidence: ConfidenceLevel = Field(..., description="Confidence-Level des Befunds")
    pruefhinweis: Optional[str] = Field(
        None,
        description="Hinweis für manuelle Überprüfung ('Befund prüfen')"
    )


class OelAnalyse(BaseModel):
    """Analyse des Getriebeöl-Zustands."""

    model_config = {"from_attributes": True}

    oel_typ: OelTyp = Field(..., description="Vorgefundener/angegebener Öltyp")
    zustand: OelZustand = Field(..., description="Visueller Zustand")
    farbe: str = Field(..., description="Farbebeschreibung")
    metallpartikel: bool = Field(False, description="Metallpartikel sichtbar")
    wasserkontamination: bool = Field(False, description="Wasserverdacht (milchig)")
    empfehlung: str = Field(..., description="Handlungsempfehlung")
    sofort_stoppen: bool = Field(False, description="Motor sofort stoppen!")
    confidence: ConfidenceLevel = Field(
        ConfidenceLevel.VISUAL_MEDIUM,
        description="Confidence-Level"
    )


class PropellerBerechnung(BaseModel):
    """Berechnung der Propellerparameter."""

    model_config = {"from_attributes": True}

    motor_nenndrehzahl_umin: float = Field(..., gt=0, description="Motor-Nenndrehzahl in U/min")
    untersetzung: float = Field(..., gt=0, description="Getriebeuntersetzung")
    propeller_durchmesser_zoll: float = Field(..., gt=0, description="Propellerdurchmesser in Zoll")
    propeller_steigung_zoll: float = Field(..., gt=0, description="Propellersteigung in Zoll")
    propeller_blaetter: int = Field(..., ge=2, le=6, description="Blattanzahl")
    propeller_drehzahl_umin: float = Field(..., gt=0, description="Berechnete Propellerdrehzahl")
    theoretische_geschwindigkeit_kn: float = Field(
        ..., gt=0,
        description="Theoretische Geschwindigkeit in Knoten (ohne Slip)"
    )
    geschaetzter_slip_prozent: float = Field(
        ..., ge=0, le=100,
        description="Geschätzter Slip in Prozent"
    )
    geschaetzte_geschwindigkeit_kn: float = Field(
        ..., ge=0,
        description="Geschätzte tatsächliche Geschwindigkeit in Knoten"
    )
    confidence: ConfidenceLevel = Field(
        ConfidenceLevel.CALCULATED,
        description="Confidence-Level"
    )


class AlignmentMessung(BaseModel):
    """Alignment-Messung Motor/Getriebe zu Propellerwelle."""

    model_config = {"from_attributes": True}

    position_12_uhr_mm: float = Field(..., ge=0, description="Fühlerblatt-Maß 12 Uhr in mm")
    position_3_uhr_mm: float = Field(..., ge=0, description="Fühlerblatt-Maß 3 Uhr in mm")
    position_6_uhr_mm: float = Field(..., ge=0, description="Fühlerblatt-Maß 6 Uhr in mm")
    position_9_uhr_mm: float = Field(..., ge=0, description="Fühlerblatt-Maß 9 Uhr in mm")
    max_differenz_mm: float = Field(..., ge=0, description="Maximale Differenz in mm")
    toleranz_mm: float = Field(..., ge=0, description="Zulässige Toleranz in mm")
    innerhalb_toleranz: bool = Field(..., description="Messung innerhalb der Toleranz")
    empfehlung: str = Field(..., description="Handlungsempfehlung")
    confidence: ConfidenceLevel = Field(
        ConfidenceLevel.MEASURED,
        description="Confidence-Level"
    )


class GetriebeWartungsHistorie(BaseModel):
    """Wartungshistorie eines Getriebes/Saildrives."""

    model_config = {"from_attributes": True}

    datum: date = Field(..., description="Datum der Wartung")
    betriebsstunden: Optional[int] = Field(None, ge=0, description="Betriebsstunden zum Zeitpunkt")
    massnahme: str = Field(..., description="Durchgeführte Maßnahme")
    oel_typ_verwendet: Optional[OelTyp] = Field(None, description="Verwendeter Öltyp")
    oel_menge_l: Optional[float] = Field(None, ge=0, description="Eingefüllte Ölmenge")
    teile_getauscht: list[str] = Field(default_factory=list, description="Getauschte Teile")
    kosten_eur: Optional[float] = Field(None, ge=0, description="Kosten in EUR")
    ausfuehrender: Optional[str] = Field(None, description="Ausführender (Werft/Eigner)")
    bemerkung: Optional[str] = Field(None, description="Zusätzliche Bemerkungen")
    confidence: ConfidenceLevel = Field(
        ConfidenceLevel.DOCUMENTED,
        description="Confidence-Level"
    )
```

(Confidence: documented)

### 35.2 Analyse-Funktionen

```python
"""
AYDI — Getriebe- und Saildrive-Analysefunktionen
Reine Funktionen, keine DB-Abhängigkeit.
"""

from typing import Optional


def berechne_propeller_drehzahl(
    motor_drehzahl: float,
    untersetzung: float
) -> float:
    """Berechnet die Propellerdrehzahl aus Motordrehzahl und Untersetzung."""
    if untersetzung <= 0:
        raise ValueError("Untersetzung muss > 0 sein")
    return motor_drehzahl / untersetzung


def berechne_theoretische_geschwindigkeit(
    propeller_drehzahl: float,
    steigung_zoll: float
) -> float:
    """
    Berechnet theoretische Geschwindigkeit in Knoten.
    Formel: RPM × Steigung(Zoll) × 0.000823
    """
    return propeller_drehzahl * steigung_zoll * 0.000823


def berechne_tatsaechliche_geschwindigkeit(
    theoretische_geschwindigkeit: float,
    slip_prozent: float
) -> float:
    """Berechnet tatsächliche Geschwindigkeit unter Berücksichtigung des Slips."""
    return theoretische_geschwindigkeit * (1 - slip_prozent / 100)


def bewerte_membran_zustand(
    alter_jahre: float,
    material: str,
    sichtbare_risse: bool = False,
    sproede: bool = False,
    verformt: bool = False,
    feuchtigkeit_innen: bool = False
) -> dict:
    """
    Bewertet den Zustand einer Saildrive-Membran.

    Returns:
        dict mit zustand, empfehlung, dringlichkeit, confidence
    """
    # Sofort-Kriterien
    if feuchtigkeit_innen:
        return {
            "zustand": "gerissen",
            "empfehlung": "SOFORT: Membran undicht! Boot aus dem Wasser, Membranwechsel!",
            "dringlichkeit": "sofort",
            "confidence": "visual_high"
        }

    if sichtbare_risse:
        return {
            "zustand": "gerissen",
            "empfehlung": "Membranwechsel beim nächsten Slipgang (zeitnah!)",
            "dringlichkeit": "naechster_slipgang",
            "confidence": "visual_high"
        }

    if sproede:
        return {
            "zustand": "sproede",
            "empfehlung": "Membranwechsel planen, nicht länger als 6 Monate warten",
            "dringlichkeit": "naechster_slipgang",
            "confidence": "visual_medium"
        }

    # Altersbasierte Bewertung
    max_alter = 10 if material == "epdm" else 7

    if alter_jahre >= max_alter:
        return {
            "zustand": "oberflaechenrisse",
            "empfehlung": f"Membranwechsel überfällig! (Max. {max_alter} Jahre, aktuell {alter_jahre:.1f})",
            "dringlichkeit": "naechster_slipgang",
            "confidence": "estimated"
        }

    if alter_jahre >= max_alter * 0.8:
        return {
            "zustand": "gut",
            "empfehlung": f"Membranwechsel planen (Alter {alter_jahre:.1f}/{max_alter} Jahre)",
            "dringlichkeit": "planbar",
            "confidence": "estimated"
        }

    return {
        "zustand": "gut",
        "empfehlung": "Membran in Ordnung, jährliche Sichtprüfung weiterführen",
        "dringlichkeit": "ok",
        "confidence": "estimated"
    }


def bewerte_anoden_zustand(
    material: str,
    restmasse_prozent: float,
    monate_seit_letztem_wechsel: Optional[float] = None,
    wasserart: str = "salzwasser"
) -> dict:
    """
    Bewertet den Zustand der Saildrive-Anoden.

    Returns:
        dict mit zustand, empfehlung, verdacht_fremdstroeme, confidence
    """
    verdacht_fremdstroeme = False

    # Extrem schnelle Auflösung → Fremdströme
    if monate_seit_letztem_wechsel and monate_seit_letztem_wechsel < 6 and restmasse_prozent < 30:
        verdacht_fremdstroeme = True

    if restmasse_prozent <= 0:
        return {
            "zustand": "aufgeloest",
            "empfehlung": "ALARM: Anode komplett aufgelöst! Saildrive-Gehäuse auf Korrosion prüfen! Sofort neue Anoden!",
            "verdacht_fremdstroeme": verdacht_fremdstroeme,
            "confidence": "visual_high"
        }

    if restmasse_prozent < 30:
        return {
            "zustand": "unter_30_prozent",
            "empfehlung": "Anoden SOFORT tauschen!",
            "verdacht_fremdstroeme": verdacht_fremdstroeme,
            "confidence": "visual_high"
        }

    if restmasse_prozent < 50:
        return {
            "zustand": "zwischen_30_50",
            "empfehlung": "Anoden beim nächsten Slipgang tauschen",
            "verdacht_fremdstroeme": verdacht_fremdstroeme,
            "confidence": "visual_high"
        }

    return {
        "zustand": "ueber_50_prozent",
        "empfehlung": "Anoden OK, beim nächsten Slipgang prüfen",
        "verdacht_fremdstroeme": False,
        "confidence": "visual_high"
    }


def bewerte_oel_zustand(
    farbe: str,
    metallpartikel: bool = False,
    milchig: bool = False,
    geruch_verbrannt: bool = False,
    oel_typ: str = "atf"
) -> dict:
    """
    Bewertet den Zustand des Getriebeöls.

    Returns:
        dict mit zustand, empfehlung, sofort_stoppen, confidence
    """
    if milchig:
        return {
            "zustand": "milchig",
            "empfehlung": "MOTOR SOFORT STOPPEN! Wasser im Getriebeöl! Ölkühler/Dichtung prüfen!",
            "sofort_stoppen": True,
            "confidence": "visual_high"
        }

    if metallpartikel and geruch_verbrannt:
        return {
            "zustand": "metallisch",
            "empfehlung": "Motor stoppen! Schwerer Getriebedefekt möglich. Getriebe zur Inspektion.",
            "sofort_stoppen": True,
            "confidence": "visual_high"
        }

    if metallpartikel:
        return {
            "zustand": "schwarz",
            "empfehlung": "Ölwechsel durchführen, Getriebe inspizieren lassen (Lamellen, Lager)",
            "sofort_stoppen": False,
            "confidence": "visual_medium"
        }

    if geruch_verbrannt:
        return {
            "zustand": "dunkel",
            "empfehlung": "Ölwechsel durchführen, Kupplung auf Schlupf prüfen",
            "sofort_stoppen": False,
            "confidence": "visual_medium"
        }

    return {
        "zustand": "gut",
        "empfehlung": "Öl in Ordnung, nächster Wechsel gemäß Wartungsplan",
        "sofort_stoppen": False,
        "confidence": "visual_medium"
    }


def berechne_alignment_bewertung(
    pos_12: float,
    pos_3: float,
    pos_6: float,
    pos_9: float,
    toleranz: float = 0.05
) -> dict:
    """
    Bewertet die Alignment-Messung (4 Positionen am Kupplungsflansch).

    Args:
        pos_12/3/6/9: Fühlerblatt-Maß in mm an 12/3/6/9 Uhr Position
        toleranz: Max. erlaubte Differenz in mm

    Returns:
        dict mit max_differenz, innerhalb_toleranz, empfehlung, confidence
    """
    werte = [pos_12, pos_3, pos_6, pos_9]
    max_diff = max(werte) - min(werte)
    innerhalb = max_diff <= toleranz

    if innerhalb:
        empfehlung = f"Alignment OK (max. Differenz {max_diff:.3f} mm, Toleranz {toleranz:.3f} mm)"
    else:
        empfehlung = (
            f"Alignment NICHT OK! Max. Differenz {max_diff:.3f} mm > Toleranz {toleranz:.3f} mm. "
            f"Motor-Halterung anpassen!"
        )

    return {
        "max_differenz_mm": max_diff,
        "innerhalb_toleranz": innerhalb,
        "empfehlung": empfehlung,
        "confidence": "measured"
    }
```

(Confidence: documented)

---

## 36. Anhänge

### Anhang A: SAE-Gehäusegrößen (Motor↔Getriebe)

| SAE-Größe | Bohrungsdurchmesser (mm) | Typische Motorleistung | Beispielgetriebe |
|---|---|---|---|
| SAE 5 | 314,3 | 10–40 PS | ZF 10M, TMC40 |
| SAE 4 | 362,0 | 25–80 PS | ZF 12M, TMC60 |
| SAE 3 | 409,6 | 50–150 PS | ZF 15M, ZF 25 |
| SAE 2 | 447,7 | 100–300 PS | ZF 25, ZF 45 |
| SAE 1 | 511,2 | 200–600 PS | ZF 45, ZF 63 |
| SAE 0 | 647,7 | 400–1.500 PS | ZF 80, ZF 220 |
| SAE 00 | 787,4 | 1.000+ PS | ZF 280, ZF 500 |

(Confidence: measured)

### Anhang B: Drehmoment-Tabelle Getriebegehäuse-Schrauben

| Schraubengröße | Material | Drehmoment (Nm) | Anwendung |
|---|---|---|---|
| M6 | 8.8 | 10 | Deckel, Ölwanne |
| M8 | 8.8 | 25 | Gehäusedeckel, Ölkühler |
| M10 | 8.8 | 50 | SAE-Bellhousing |
| M12 | 8.8 | 85 | SAE-Bellhousing, Flansch |
| M14 | 8.8 | 135 | Große Gehäuseschrauben |
| M16 | 8.8 | 210 | Motorfuß |
| 5/16" UNF | Grade 5 | 20 | Velvet Drive |
| 3/8" UNF | Grade 5 | 40 | Velvet Drive, PRM |
| 1/2" UNF | Grade 5 | 95 | Flanschschrauben |

(Confidence: measured)

### Anhang C: Kompatibilitätsmatrix — Getriebe zu Motor

| Motor | Original-Getriebe | Alternative Getriebe | SAE | Adapter nötig? |
|---|---|---|---|---|
| Volvo D1-13/20/30 | Volvo 120S/130S SD | ZF 10M/12M (Welle) | SAE 5 | Ja (Adapterplatte) |
| Volvo D2-40/55/75 | Volvo 130S/150S SD oder MS25 | ZF 15M/25 | SAE 3/4 | Ja (Adapterplatte) |
| Yanmar 1GM/2GM | Yanmar KM2 | ZF 5M/10M | SAE 5 | Ja |
| Yanmar 3YM20/30 | Yanmar KM2P/SD25 | ZF 12M, TMC40/60 | SAE 5/4 | Ja |
| Yanmar 3JH40/57 | Yanmar KM3P/SD50 | ZF 15M, TMC60 | SAE 4/3 | Ja |
| Yanmar 4JH80/110 | Yanmar KM4A/SD60 | ZF 25 | SAE 3/2 | Ja |
| Nanni 2.10/2.14 | TMC40 | PRM 80/90, ZF 10M | SAE 5 | Meist kompatibel |
| Nanni 3.75/N4.38 | TMC60 | PRM 150, ZF 12M/15M | SAE 4 | Meist kompatibel |
| Beta 14/20 | PRM 80/90 | TMC40, ZF 10M | SAE 5 | Meist kompatibel |
| Beta 30/38/43 | PRM 150 | TMC60, ZF 15M | SAE 4/3 | Meist kompatibel |
| Vetus M2/M3/M4 | TMC40/60 | PRM 80/90/150 | SAE 5/4 | Variiert |
| Perkins 4.108 | BW Velvet Drive 71C | ZF 15M (mit Adapter) | SAE 3 | Ja |
| Universal M-25 | BW Velvet Drive 71C | ZF 15M (mit Adapter) | SAE 3 | Ja |

**WARNUNG:** Getriebetausch immer mit Fachmann planen! Falsche Kombination = Schwungradbeschädigung, Kupplungsprobleme, Alignment-Albtraum.

(Confidence: documented)

### Anhang D: Umrechnungstabellen

**Leistung:**
| PS | kW | Anwendung |
|---|---|---|
| 10 | 7,4 | Kleinste Segelbootmotoren |
| 20 | 14,7 | Standard-Segelboot 25–30 ft |
| 30 | 22,1 | Segelboot 30–35 ft |
| 40 | 29,4 | Segelboot 35–40 ft |
| 55 | 40,4 | Segelboot 38–45 ft |
| 75 | 55,2 | Segelboot 42–50 ft / kl. Motorboot |
| 110 | 80,9 | Große Segelboote / Motorboote |
| 150 | 110 | Motorboote |
| 250 | 184 | Große Motorboote |
| 400 | 294 | Motoryachten |
| 600 | 441 | Motoryachten / Superyachten |

**Untersetzung → Propellerdrehzahl (bei 3.000 U/min Motor):**
| Untersetzung | Propeller U/min |
|---|---|
| 1,50:1 | 2.000 |
| 1,93:1 | 1.554 |
| 2,00:1 | 1.500 |
| 2,14:1 | 1.402 |
| 2,21:1 | 1.357 |
| 2,47:1 | 1.215 |
| 2,63:1 | 1.141 |
| 2,86:1 | 1.049 |
| 3,00:1 | 1.000 |
| 3,50:1 | 857 |
| 4,00:1 | 750 |

(Confidence: calculated)

### Anhang E: Checkliste — Getriebe-/Saildrive-Kauf (Gebrauchtboot)

| Prüfpunkt | Methode | OK | Warnung | Kaufabbruch |
|---|---|---|---|---|
| Getriebeöl-Farbe | Ölmessstab prüfen | Rot/klar (ATF) | Dunkel | Milchig, schwarz |
| Getriebeöl-Geruch | Riechen | Leicht süßlich | Verbrannt | Stechend verbrannt |
| Metallpartikel im Öl | Messstab mit Magnet | Keine | Feiner Abrieb | Grobe Späne |
| Ölstand | Messstab | Korrekt | Leicht zu niedrig | Stark zu niedrig oder überfüllt |
| Schalten Vorwärts/Rückwärts | Motor laufen lassen | Sanft, sofort | Verzögert, ruckt | Rutscht, kein Vortrieb |
| Geräusche Neutral | Hören (Stethoskop) | Leises Summen | Rasseln | Klopfen, Mahlen |
| Ölleckage | Sichtprüfung | Keine | Leichte Feuchtigkeit | Tropfende Leckage |
| Ölkühler | Sichtprüfung | Sauber, dicht | Leichte Korrosion | Starke Korrosion, Leckage |
| Saildrive-Membran | Sichtprüfung + Alter | < 5 Jahre, elastisch | 5–7 Jahre, OK | > 7 Jahre, spröde, Risse |
| Saildrive-Anoden | Sichtprüfung | > 50 % Restmasse | 30–50 % | < 30 % oder aufgelöst |
| Saildrive-Gehäuse | Sichtprüfung | Glatt, intakt | Leichte Oxidation | Lochfraß, Risse |
| Alignment | Vibrationstest bei Probefahrt | Vibrationsfrei | Leichte Vibrationen | Starke Vibrationen |
| Bowdenzug/Schaltung | Betätigung | Leichtgängig, präzise | Schwergängig | Klemmt, Spiel |
| Betriebsstunden Getriebe | Motorbetriebsstunden | < 2.000 Bh | 2.000–4.000 Bh | > 4.000 Bh ohne Revision |

(Confidence: documented)

### Anhang F: Notfall-Maßnahmen auf See

| Situation | Sofortmaßnahme | Nächster Schritt |
|---|---|---|
| Getriebe rutscht komplett | Segel setzen (Segelboot!) / Anker (Motorboot) | Kein Motorantrieb → Schlepp organisieren |
| Wasser im Getriebeöl | Motor STOPP! Bilge prüfen | Ölkühler-Seewasseranschluss schließen, Schlepp |
| Saildrive-Membran leckt stark | Bilgepumpe MAX, Motor laufen lassen (!) | Nächsten Hafen ansteuern, Seenotrettung bereithalten |
| Schaltung blockiert in „Vorwärts" | Motor AUS → Motor auf niedrigster Drehzahl starten | Hafen ansteuern, Bowdenzug am Getriebe direkt betätigen |
| Schaltung blockiert in „Neutral" | Segel setzen / Anker | Bowdenzug am Getriebe direkt betätigen (Vorwärts erzwingen) |
| Starke Vibrationen plötzlich | Drehzahl reduzieren, Last wegnehmen | Propeller/Treibgut prüfen (Taucher oder Rückwärts versuchen) |
| Getriebeöl-Alarm (Temperatur) | Drehzahl reduzieren, Last reduzieren | Ölstand prüfen, Kühlwasser-Durchfluss prüfen |

(Confidence: documented)

### Anhang G: Saildrive-Membran — Prüfprotokoll-Vorlage

```
AYDI SAILDRIVE-MEMBRAN PRÜFPROTOKOLL
=====================================
Boot: _____________________________ Saildrive: ___________________
Datum: _______________ Prüfer: ___________________________________

1. ALLGEMEIN
   Saildrive-Modell: □ Volvo 120S □ Volvo 130S □ Volvo 150S
                     □ Yanmar SD20 □ Yanmar SD25 □ Yanmar SD50 □ Yanmar SD60
                     □ ZF SD100 □ ZF SD200 □ Andere: __________
   Alter Membran: ______ Jahre (Einbaudatum: ___________)
   Membran-Teilenummer: _______________________
   Letzter Wechsel: _______________

2. SICHTPRÜFUNG AUSSEN
   Risse sichtbar:     □ Nein □ Oberfläche □ Durchgehend → SOFORT HANDELN!
   Verformung:         □ Nein □ Leicht □ Stark
   Farbveränderung:    □ Nein □ Leicht □ Stark
   Bewuchs:            □ Nein □ Leicht □ Muscheln in Falte
   Spannband/Klemmring: □ Fest □ Korrodiert □ Lose → SOFORT HANDELN!

3. SICHTPRÜFUNG INNEN (Boot)
   Feuchtigkeit:       □ Nein □ Leichte Feuchtigkeit □ Tropfend → ALARM!
   Salzablagerungen:   □ Nein □ Ja → ALARM!
   Dichtmittel:        □ Intakt □ Rissig □ Abgelöst

4. ELASTIZITÄTSTEST
   Daumendrucktest:    □ Federt sofort □ Langsam □ Hart/kein Federn → TAUSCHEN!

5. BEWERTUNG
   □ OK — Nächste Prüfung in 12 Monaten
   □ ACHTUNG — Wechsel innerhalb 12 Monate planen
   □ SOFORT — Membranwechsel vor nächstem Einsatz!

6. EMPFEHLUNG
   _______________________________________________________________
   _______________________________________________________________

Unterschrift Prüfer: _________________ Datum: _______________
```

(Confidence: documented)

### Anhang H: Getriebeöl-Spezifikationen — Schnellreferenz

| Getriebe | Öltyp | Menge | Intervall | WARNUNG |
|---|---|---|---|---|
| ZF 5M | SAE 80W-90 GL-4 | 0,25 l | 500 Bh / jährlich | Kein ATF! |
| ZF 10M | ATF Dexron III/VI | 0,65 l | 250 Bh / jährlich | Kein Motoröl! |
| ZF 12M | ATF Dexron III/VI | 0,8 l | 250 Bh / jährlich | Kein Motoröl! |
| ZF 15M | ATF Dexron III/VI | 1,0 l | 250 Bh / jährlich | Kein Motoröl! |
| ZF 25 | ATF Dexron III/VI | 1,8 l | 500 Bh / jährlich | Kein Motoröl! |
| ZF 45 | ATF Dexron III/VI | 3,5 l | 500 Bh / jährlich | Kein Motoröl! |
| TMC40 | ATF Dexron III/VI | 0,6 l | 250 Bh / jährlich | Kein Motoröl! |
| TMC60 | ATF Dexron III/VI | 0,9 l | 250 Bh / jährlich | Kein Motoröl! |
| Yanmar KM2P | ATF Dexron III | 0,35 l | 250 Bh / jährlich | Herstelleröl OK |
| Yanmar KM3P | ATF Dexron III | 0,45 l | 250 Bh / jährlich | Herstelleröl OK |
| PRM 80 (mech.) | SAE 80W-90 GL-4 | 0,3 l | 250 Bh / jährlich | Kein ATF! |
| PRM 90 | ATF Dexron III | 0,5 l | 250 Bh / jährlich | |
| PRM 150 | ATF Dexron III | 1,0 l | 250 Bh / jährlich | |
| BW Velvet Drive 71C | SAE 30 Motoröl | 1,9 l | 200 Bh / jährlich | KEIN ATF!!! |
| BW Velvet Drive 72C | SAE 30 Motoröl | 2,4 l | 200 Bh / jährlich | KEIN ATF!!! |
| Volvo SD oben | ATF Dexron III | 0,5–0,8 l | 250 Bh / jährlich | |
| Volvo SD unten | Volvo IPS Oil / 75W-90 | 0,35–0,5 l | 500 Bh / 2-jährlich | Herstelleröl empfohlen |
| Yanmar SD oben | ATF Dexron III | 0,35–0,7 l | 250 Bh / jährlich | |
| Yanmar SD unten | Yanmar SD Oil / 80W-90 | 0,35–0,5 l | 500 Bh / 2-jährlich | Herstelleröl empfohlen |

(Confidence: documented)

### Anhang I: Getriebe-Fehlercodes (elektronische Systeme)

Moderne Getriebe mit elektronischer Steuerung (Volvo EVC, Yanmar JC-Serie) zeigen Fehlercodes an:

**Volvo Penta EVC (Saildrive 130S/150S):**

| Fehlercode | Beschreibung | Schweregrad | Maßnahme |
|---|---|---|---|
| EVC-001 | Schaltaktuator blockiert | MITTEL | Kabel und Aktuator prüfen, Schaltgestänge frei? |
| EVC-002 | Öldrucksensor Fehler | WARNUNG | Sensor prüfen, Kabel prüfen |
| EVC-003 | Öltemperatur hoch | KRITISCH | Drehzahl reduzieren, Ölkühler prüfen |
| EVC-004 | Schaltposition nicht erkannt | MITTEL | Positionssensor prüfen/kalibrieren |
| EVC-005 | Kommunikationsfehler CAN-Bus | WARNUNG | Kabelbaumprüfung, Stecker kontrollieren |
| EVC-006 | Notlaufmodus aktiv | KRITISCH | Motor/Getriebe-Diagnose, Werft! |
| EVC-010 | Getriebeölstand niedrig | KRITISCH | Ölstand prüfen, Leckage suchen |
| EVC-011 | Neutralschalter defekt | MITTEL | Schalter tauschen |
| EVC-012 | Vorwärtskupplung Druckverlust | KRITISCH | Ölpumpe, Lamellen, Ventil prüfen |
| EVC-013 | Rückwärtskupplung Druckverlust | KRITISCH | Ölpumpe, Lamellen, Ventil prüfen |

**Yanmar JC-Serie (SD50/SD60):**

| Fehlercode | Beschreibung | Schweregrad | Maßnahme |
|---|---|---|---|
| JC-E01 | Schaltmotor Überstrom | MITTEL | Schaltmechanismus prüfen |
| JC-E02 | Schaltposition Timeout | MITTEL | Bowdenzug/Aktuator prüfen |
| JC-E03 | Öltemperatursensor offen | WARNUNG | Sensor/Kabel prüfen |
| JC-E04 | Öltemperatur > 100°C | KRITISCH | Drehzahl senken, Kühlung prüfen |
| JC-E05 | CAN-Bus Kommunikation unterbrochen | WARNUNG | Kabelbaum prüfen |
| JC-E10 | Neutral nicht erkannt | MITTEL | Neutralschalter prüfen |
| JC-E11 | Motor startet nicht (Neutral-Sperre) | MITTEL | Getriebe manuell in Neutral setzen |

(Confidence: documented)

### Anhang J: Getriebe-Gewichtsvergleich nach Leistungsklasse

| Leistungsklasse | ZF | Technodrive | PRM | Yanmar KM | Borg Warner |
|---|---|---|---|---|---|
| 15–25 PS | ZF 5M: 9,5 kg | — | PRM 80: 11 kg | KM2P: 18 kg* | — |
| 25–40 PS | ZF 10M: 17 kg | TMC40: 15 kg | PRM 90: 16 kg | KM2P: 18 kg* | — |
| 40–70 PS | ZF 12M: 22 kg | TMC60: 23 kg | PRM 150: 32 kg | KM3P: 24 kg | — |
| 60–90 PS | ZF 15M: 27 kg | TMC93: 38 kg | PRM 150: 32 kg | KM4A: 32 kg | — |
| 100–175 PS | ZF 25: 48 kg | TMC260: 95 kg | PRM 260: 58 kg | KM4A2: 42 kg | VD 71C: 40 kg |
| 200–350 PS | ZF 45: 80 kg | — | PRM 500: 120 kg | — | VD 72C: 50 kg |

*KM2P Gewicht inkl. Motor-Integration (nicht separat)

(Confidence: documented / benchmark)

### Anhang K: Saildrive vs. Wellenanlage — Kostenvergleich über 20 Jahre

**Szenario: Segelboot 38 ft, 40 PS Motor, 200 Bh/Jahr**

| Kostenposition | Saildrive (Volvo 130S) | Wellenanlage (ZF 15M) |
|---|---|---|
| **Anschaffung** | | |
| Getriebe/Saildrive | €6.000 | €2.500 |
| Propellerwelle | — | €400 |
| Stevenrohr | — | €200 |
| Stopfbuchse/PSS | — | €400 |
| Wellenlager | — | €150 |
| Flexible Kupplung | — | €250 |
| Propeller (3-Blatt Falt) | €1.200 | €1.200 |
| **Anschaffung Gesamt** | **€7.200** | **€5.100** |
| | | |
| **Jährliche Wartung (×20)** | | |
| Ölwechsel obere Einheit | €30/Jahr → €600 | €25/Jahr → €500 |
| Ölwechsel untere Einheit | €15/Jahr → €300 | — |
| Anoden (alle 2 Jahre) | €50/2J → €500 | — |
| Stopfbuchse nachstellen | — | €0 (DIY) |
| **Wartung Gesamt (20 J.)** | **€1.400** | **€500** |
| | | |
| **Intervall-Arbeiten** | | |
| Membranwechsel (2× in 20 J.) | 2× €1.000 = €2.000 | — |
| Lamellenwechsel (1× in 20 J.) | €700 | €600 |
| Stopfbuchse/PSS Austausch | — | €400 |
| Ölkühler (1× in 20 J.) | €500 (im SD) | €400 |
| Wellenlager (1× in 20 J.) | — | €300 |
| Simmerring (2× in 20 J.) | €200 | €150 |
| **Intervall Gesamt** | **€3.400** | **€1.850** |
| | | |
| **GESAMTKOSTEN 20 JAHRE** | **€12.000** | **€7.450** |
| **Kosten pro Betriebsstunde** | **€3,00/Bh** | **€1,86/Bh** |

**Fazit:** Die Wellenanlage ist über 20 Jahre ca. 40 % günstiger. Der Saildrive bietet dafür weniger Vibrationen, geringeren Widerstand unter Segel und einfacheren Einbau. Die Entscheidung ist bootsspezifisch.

(Confidence: benchmark)

### Anhang L: Saisonale Checklisten

**Frühjahr (Saisonstart):**

| # | Maßnahme | Getriebe | Saildrive | Erledigt? |
|---|---|---|---|---|
| 1 | Getriebeöl prüfen (Stand, Farbe, Geruch) | ✓ | ✓ (oben + unten) | □ |
| 2 | Ölwechsel durchführen (wenn Intervall erreicht) | ✓ | ✓ | □ |
| 3 | Schaltfunktion prüfen (V/N/R am Bedienpult) | ✓ | ✓ | □ |
| 4 | Bowdenzug Leichtgängigkeit prüfen | ✓ | ✓ | □ |
| 5 | Ölkühler-Anschlüsse Dichtheit prüfen | ✓ | — | □ |
| 6 | Saildrive-Anoden prüfen/tauschen | — | ✓ | □ |
| 7 | Saildrive-Membran Sichtprüfung | — | ✓ | □ |
| 8 | Antifouling Saildrive-Bein erneuern | — | ✓ | □ |
| 9 | Kühlwassereinlass Saildrive reinigen | — | ✓ | □ |
| 10 | Alignment Sichtprüfung (Motorlager) | ✓ | — | □ |

**Herbst (Einwinterung):**

| # | Maßnahme | Getriebe | Saildrive | Erledigt? |
|---|---|---|---|---|
| 1 | Getriebeöl wechseln (saures Öl nicht überwintern) | ✓ | ✓ | □ |
| 2 | Motor/Getriebe warm fahren vor letztem Abstellen | ✓ | ✓ | □ |
| 3 | Bowdenzug einsprühen (Silikonspray) | ✓ | ✓ | □ |
| 4 | Ölkühler-Seewasserseite mit Frostschutz füllen | ✓ | — | □ |
| 5 | Saildrive-Bein auf Bewuchs prüfen und reinigen | — | ✓ | □ |
| 6 | Saildrive-Membran abdecken (UV-Schutz!) | — | ✓ | □ |
| 7 | Anoden-Zustand dokumentieren (Foto) | — | ✓ | □ |
| 8 | Propeller abziehen, reinigen, fetten | ✓ | ✓ | □ |
| 9 | Schaltung in Neutral lassen (Lamellen entlasten) | ✓ | ✓ | □ |
| 10 | Betriebsstunden notieren | ✓ | ✓ | □ |

(Confidence: documented)

### Anhang M: Herstellerkontakte und Service-Hotlines

| Hersteller | Service-Hotline (DE) | Service-Hotline (Int.) | Website |
|---|---|---|---|
| ZF Marine | +49 7541 77-0 | +39 049 8299 811 (IT) | zf.com/marine |
| Volvo Penta | +49 431 3994-0 (Kiel) | +46 31 323 00 00 (SE) | volvopenta.com |
| Yanmar Marine | +49 4105 77 67-0 | +31 36 549 4811 (NL) | yanmar.com/marine |
| Technodrive | +31 10 437 00 22 | — | technodrive.com |
| PRM / Newage | +44 1onal 234 767890 | — | prm-newage.com |
| Twin Disc | +32 2 380 03 23 (BE) | +1 262 638 4000 (US) | twindisc.com |
| Flexofold | +45 70 27 00 57 (DK) | — | flexofold.com |
| Gori Propeller | +45 70 22 70 33 (DK) | — | goripropeller.dk |
| MG Duff (Anoden) | +44 1011 23 456789 | — | mgduff.com |
| Tecnoseal (Anoden) | +39 011 991 6611 | — | tecnoseal.it |

(Confidence: documented)

### Anhang N: Spezialwerkzeuge

| Werkzeug | Anwendung | Bezugsquelle | Preis (ca.) |
|---|---|---|---|
| Propeller-Abzieher (universal) | Propeller vom Konus abziehen | Bootsbedarf | €30–60 |
| Propeller-Abzieher (Saildrive-spezifisch) | Volvo/Yanmar Saildrive-Propeller | Hersteller/Bootsbedarf | €40–80 |
| Fühlerblattlehre 0,01–1,00 mm | Alignment-Messung | Werkzeughandel | €10–25 |
| Öldruck-Manometer 0–25 bar | Getriebe-Öldruck messen | Hydraulikfachhandel | €30–60 |
| Stethoskop (Mechaniker) | Geräusch-Lokalisierung | Werkzeughandel | €15–30 |
| Infrarot-Thermometer | Öltemperatur-Messung | Werkzeughandel | €20–50 |
| Magnet (Stabmagnet) | Metallpartikel im Öl erkennen | Überall | €5 |
| Ölprobenflasche (transparent) | Ölzustand beurteilen | Labor/Apotheke | €2 |
| Drehmomentschlüssel 5–50 Nm | Gehäuseschrauben, Membran-Klemmring | Werkzeughandel | €30–80 |
| Drehmomentschlüssel 30–200 Nm | Flanschschrauben, Motorfuß | Werkzeughandel | €40–100 |
| UV-Lecksuchlampe + Kontrastmittel | Öl-Lecksuche im Maschinenraum | KFZ-Bedarf | €25–50 |
| Laser-Alignment-Tool | Präzises Motor-Alignment | Spezialwerkzeug | €200–800 |
| Simmerring-Montagehülse | Simmerring beschädigungsfrei einsetzen | Werkzeughandel | €15–30 |
| ZF-Lamellen-Abzieher | Lamellenpakete aus ZF-Getrieben ziehen | ZF-Werkstattbedarf | €50–120 |
| Durometer (Shore A) | Membran-Härte messen | Messtechnik | €80–200 |

(Confidence: documented)

### Anhang O: Typische Reparaturzeiten

| Reparatur | Arbeitszeit (Fachmann) | Arbeitszeit (DIY) | Boot an Land nötig? |
|---|---|---|---|
| Getriebeöl wechseln | 0,5 h | 1 h | Nein |
| Bowdenzug tauschen | 1–2 h | 2–4 h | Nein |
| Schaltgestänge einstellen | 0,5–1 h | 1–2 h | Nein |
| Simmerring Abtrieb tauschen | 2–4 h | 4–6 h | Ja (Wellenanlage) |
| Lamellensatz tauschen (ZF 10/12/15) | 4–6 h | 8–12 h | Nein (aber empfohlen) |
| Lamellensatz tauschen (ZF 25/45) | 6–8 h | Nicht empfohlen | Nein (aber empfohlen) |
| Ölkühler tauschen | 1–2 h | 2–3 h | Nein |
| Getriebe komplett tauschen | 6–12 h | 12–20 h | Nein (aber empfohlen) |
| Saildrive-Membranwechsel | 4–6 h | 6–10 h | JA (zwingend!) |
| Saildrive-Anoden tauschen | 0,5 h | 1 h | JA |
| Saildrive-Öl untere Einheit wechseln | 1 h | 1,5 h | JA |
| Saildrive komplett tauschen | 12–20 h | Nicht empfohlen | JA |
| Alignment (Wellenanlage) | 1–4 h | 2–6 h | Nein (im Wasser!) |
| Propeller tauschen (Saildrive) | 0,5 h | 1 h | JA |
| Propeller wuchten lassen | 1 h (extern) | — | JA (Propeller demontiert) |
| Kühlwassereinlass reinigen | 0,25 h | 0,5 h | JA (oder Taucher) |

(Confidence: benchmark)

### Anhang P: Häufige Verwechslungen und Irrtümer

| Irrtum | Richtigstellung |
|---|---|
| „Jedes Getriebeöl ist gleich" | FALSCH! ATF, Motoröl und Getriebeöl (GL-4/5) sind völlig unterschiedlich. Verwechslung zerstört das Getriebe. |
| „Saildrive-Membran hält ewig" | FALSCH! Gummi altert. 7–10 Jahre ist Maximum. Membranriss = Sinkgefahr. |
| „Kupfer-Antifouling geht auf Saildrive" | FALSCH! Kupfer + Aluminium = galvanische Korrosion. Nur kupferfreies AF! |
| „Zink-Anoden sind immer richtig" | FALSCH! In Brackwasser sind Aluminium-Anoden besser. In Süßwasser Magnesium. |
| „Alignment muss nur einmal gemacht werden" | FALSCH! Motorfundamente verändern sich über die Jahre. Alle 2 Jahre prüfen. |
| „Getriebe braucht keine Wartung" | FALSCH! Ölwechsel ist die günstigste Getriebe-Versicherung. |
| „Halb einkuppeln schont die Kupplung" | FALSCH! Halb einkuppeln erzeugt Wärme und verschleißt Lamellen extrem schnell. |
| „Man kann im Neutral schalten bei jeder Drehzahl" | RICHTIG bei hydraulischen Getrieben. FALSCH bei mechanischen Klauengetrieben (< 1.000 U/min!). |
| „Milchiges Öl ist nur Kondenswasser" | MÖGLICH, aber gefährlich: meist ist der Ölkühler undicht! Immer prüfen! |
| „Ein altes Getriebe ist ein schlechtes Getriebe" | FALSCH! Gut gewartete ZF-Getriebe halten 10.000+ Betriebsstunden. |
| „Saildrive ist Wartungsarm" | FALSCH! Saildrive hat MEHR Wartungspunkte als eine Wellenanlage (Membran, Anoden, 2 Ölkreisläufe, AF). |
| „Gebraucht-Getriebe vom Schrottplatz reicht" | RISKANT! Ohne Wartungshistorie ist der Zustand unbekannt. Lamellen und Ölpumpe können verschlissen sein. |
| „Faltpropeller sind schlechter als Festpropeller" | TEILWEISE RICHTIG: Unter Motor ca. 5–15 % weniger Schub, aber unter Segel deutlich weniger Widerstand. Gesamtbilanz positiv für Segelboote. |
| „Elektronische Schaltung ist besser" | KOMFORT JA, Zuverlässigkeit NEIN. Bowdenzug-Schaltung ist einfacher, reparierbar auf See, keine Elektronik-Ausfälle. |

(Confidence: documented)

### Anhang Q: AYDI-Bewertungskriterien — Getriebe und Saildrive

**Für AYDI-Analysemodule relevante Bewertungspunkte:**

| Modul | Prüfpunkt | Gewichtung | Confidence-Quelle |
|---|---|---|---|
| structural | Getriebefundament-Zustand | 8/100 | visual_medium / measured |
| structural | Alignment-Qualität | 6/100 | measured |
| structural | Wellenanlage-Zustand | 7/100 | visual_medium / measured |
| materials | Getriebeöl-Zustand | 5/100 | visual_high / documented |
| materials | Saildrive-Gehäuse Korrosion | 8/100 | visual_high |
| materials | Membran-Zustand | 9/100 | visual_high / documented |
| materials | Anoden-Zustand | 6/100 | visual_high |
| compliance | Membran-Alter vs. Herstellervorgabe | 7/100 | documented |
| compliance | Antifouling-Typ Saildrive | 5/100 | visual_medium / documented |
| compliance | Bonding / galvanischer Schutz | 6/100 | measured |
| service_patterns | Ölwechsel-Historie | 5/100 | documented |
| service_patterns | Membranwechsel-Historie | 7/100 | documented |
| service_patterns | Anodenwechsel-Historie | 4/100 | documented |
| cost | Getriebe-Restwert | 3/100 | benchmark |
| cost | Erwartete Wartungskosten 5 Jahre | 5/100 | calculated / benchmark |
| production | Getriebe-Zugänglichkeit | 4/100 | visual_medium |
| production | Saildrive-Einbauqualität | 5/100 | visual_medium |

(Confidence: documented)

### Anhang R: Regionale Besonderheiten

| Region | Besonderheit | Auswirkung auf Getriebe/Saildrive |
|---|---|---|
| Ostsee (Brackwasser) | Salzgehalt 0,3–2,0 % | Zink-Anoden passivieren teilweise → Aluminium bevorzugen |
| Mittelmeer | Hohe Wassertemperatur, starker Bewuchs | Saildrive-Kühlwassereinlass häufiger reinigen, AF 2×/Saison |
| Nordsee | Kalt, aggressives Salzwasser | Maximaler Anodenverschleiß, Ölkühler-Korrosion schneller |
| Tropen | UV-Belastung extrem | Membran alle 5 Jahre wechseln (statt 7), UV-Schutz! |
| Karibik | Warm, elektrisch aktive Häfen | Fremdströme häufig, galvanischer Isolator Pflicht |
| Skandinavien | Kalt, teilweise Süßwasser (Seen) | Magnesium-Anoden für Süßwasser, Frostschutz im Ölkühler |
| Adria (Kroatien) | Sauber, aber warm | Gute Bedingungen, Standard-Intervalle ausreichend |
| Atlantik (Langfahrt) | Variable Bedingungen, lange Seezeiten | Reserve-Bowdenzug mitführen, Membran vor Abfahrt wechseln |

(Confidence: documented / benchmark)

### Anhang S: Getriebe-Überholungskosten — Detailaufstellung

**ZF 10M / 12M — Komplett-Überholung:**

| Position | Teilenummer (Beispiel) | Beschreibung | Einzelpreis | Menge | Gesamt |
|---|---|---|---|---|---|
| 1 | 3312 199 005 | Lamellensatz Vorwärts | €190 | 1 | €190 |
| 2 | 3312 199 006 | Lamellensatz Rückwärts | €190 | 1 | €190 |
| 3 | 3312 199 010 | Dichtungssatz komplett | €95 | 1 | €95 |
| 4 | 3311 304 022 | Simmerring Abtrieb | €20 | 1 | €20 |
| 5 | 3311 304 015 | Simmerring Antrieb | €20 | 1 | €20 |
| 6 | 3312 199 020 | Ölpumpe (falls nötig) | €320 | 0–1 | €0–320 |
| 7 | — | ATF Dexron III/VI (2×) | €12 | 2 | €24 |
| 8 | — | Reinigungsmaterial | €15 | 1 | €15 |
| 9 | — | Arbeitszeit Fachbetrieb (6–8 h) | €85/h | 7 | €595 |
| | | **Gesamt ohne Ölpumpe** | | | **€1.149** |
| | | **Gesamt mit Ölpumpe** | | | **€1.469** |

**ZF 25 — Komplett-Überholung:**

| Position | Beschreibung | Einzelpreis | Menge | Gesamt |
|---|---|---|---|---|
| 1 | Lamellensatz Vorwärts | €280 | 1 | €280 |
| 2 | Lamellensatz Rückwärts | €280 | 1 | €280 |
| 3 | Dichtungssatz komplett | €160 | 1 | €160 |
| 4 | Simmerring Abtrieb | €30 | 1 | €30 |
| 5 | Simmerring Antrieb | €30 | 1 | €30 |
| 6 | Ölfilter | €25 | 1 | €25 |
| 7 | Ölkühler (falls nötig) | €480 | 0–1 | €0–480 |
| 8 | Ölpumpe (falls nötig) | €380 | 0–1 | €0–380 |
| 9 | ATF Dexron III/VI (3×) | €12 | 3 | €36 |
| 10 | Arbeitszeit Fachbetrieb (8–10 h) | €85/h | 9 | €765 |
| | **Gesamt minimal** | | | **€1.606** |
| | **Gesamt maximal** | | | **€2.466** |

**Volvo 130S Saildrive — Komplett-Überholung:**

| Position | Beschreibung | Einzelpreis | Menge | Gesamt |
|---|---|---|---|---|
| 1 | Membran komplett | €380 | 1 | €380 |
| 2 | Lamellensatz obere Einheit | €320 | 1 | €320 |
| 3 | Dichtungssatz obere Einheit | €120 | 1 | €120 |
| 4 | Dichtungssatz untere Einheit | €90 | 1 | €90 |
| 5 | Propellerwellen-Dichtring | €35 | 1 | €35 |
| 6 | Gleitlager untere Einheit | €85 | 1 | €85 |
| 7 | Anodensatz komplett (3 Stk.) | €80 | 1 | €80 |
| 8 | ATF (obere Einheit) | €12 | 1 | €12 |
| 9 | Getriebeöl (untere Einheit) | €25 | 1 | €25 |
| 10 | Antifouling Saildrive | €45 | 1 | €45 |
| 11 | Epoxyprimer | €35 | 1 | €35 |
| 12 | Sikaflex 291 (Membran) | €18 | 1 | €18 |
| 13 | Slipgebühr | €220 | 1 | €220 |
| 14 | Arbeitszeit Fachbetrieb (8–12 h) | €85/h | 10 | €850 |
| | **Gesamt** | | | **€2.315** |

(Confidence: benchmark)

### Anhang T: Motor-Getriebe-Kombinationen — Drehmomenttabelle

Die maximale Drehmoment-Kapazität des Getriebes muss das Motordrehmoment bei Nennleistung übersteigen:

| Motor | Nennleistung | Nenndrehzahl | Max. Drehmoment | Min. Getriebe |
|---|---|---|---|---|
| Yanmar 1GM10 | 9 PS / 7 kW | 3.400 U/min | 20 Nm | ZF 5M / PRM 80 |
| Yanmar 2YM15 | 15 PS / 11 kW | 3.600 U/min | 31 Nm | ZF 10M / PRM 80 |
| Yanmar 2GM20 | 18 PS / 13 kW | 3.600 U/min | 37 Nm | ZF 10M / KM2P |
| Yanmar 3YM20 | 21 PS / 15 kW | 3.600 U/min | 43 Nm | ZF 10M / KM2P |
| Yanmar 3YM30 | 29 PS / 21 kW | 3.600 U/min | 59 Nm | ZF 12M / KM2P |
| Volvo D1-13 | 13 PS / 10 kW | 3.600 U/min | 27 Nm | ZF 10M / Volvo 120S SD |
| Volvo D1-20 | 19 PS / 14 kW | 3.600 U/min | 39 Nm | ZF 10M / Volvo 120S SD |
| Volvo D1-30 | 28 PS / 21 kW | 3.000 U/min | 67 Nm | ZF 12M / Volvo 130S SD |
| Volvo D2-40 | 39 PS / 29 kW | 3.000 U/min | 92 Nm | ZF 15M / Volvo 130S SD |
| Volvo D2-55 | 55 PS / 40 kW | 3.000 U/min | 130 Nm | ZF 15M / Volvo 130S SD |
| Volvo D2-75 | 75 PS / 55 kW | 3.000 U/min | 175 Nm | ZF 25 / Volvo 150S SD |
| Yanmar 3JH40 | 40 PS / 29 kW | 3.000 U/min | 93 Nm | KM3P / SD50 |
| Yanmar 3JH57 | 57 PS / 42 kW | 3.000 U/min | 133 Nm | KM3P / SD50 |
| Yanmar 4JH57 | 57 PS / 42 kW | 3.000 U/min | 133 Nm | KM4A |
| Yanmar 4JH80 | 80 PS / 59 kW | 3.000 U/min | 188 Nm | KM4A / SD60 |
| Yanmar 4JH110 | 110 PS / 81 kW | 3.000 U/min | 257 Nm | KM4A2 |
| Nanni 2.10 | 10 PS / 7 kW | 3.600 U/min | 20 Nm | TMC40 |
| Nanni 3.75 | 21 PS / 15 kW | 3.600 U/min | 43 Nm | TMC40 |
| Nanni N4.38 | 38 PS / 28 kW | 2.800 U/min | 95 Nm | TMC60 |
| Beta 14 | 14 PS / 10 kW | 3.600 U/min | 28 Nm | PRM 80 |
| Beta 25 | 25 PS / 18 kW | 3.600 U/min | 50 Nm | PRM 90 |
| Beta 38 | 38 PS / 28 kW | 2.800 U/min | 95 Nm | PRM 150 |
| Beta 50 | 50 PS / 37 kW | 2.800 U/min | 126 Nm | PRM 150 |

**Formel:** Drehmoment (Nm) = Leistung (kW) × 9.550 ÷ Drehzahl (U/min)

(Confidence: calculated / documented)

### Anhang U: Getriebeöl-Analysewerte — Referenztabelle

Bei professioneller Ölanalyse (Labor) gelten folgende Richtwerte für marine Wendegetriebe:

| Parameter | Einheit | Normal | Achtung | Kritisch | Methode |
|---|---|---|---|---|---|
| Wasser | ppm | < 200 | 200–500 | > 500 | Karl-Fischer |
| Eisen (Fe) | ppm | < 50 | 50–150 | > 150 | ICP-OES |
| Kupfer (Cu) | ppm | < 30 | 30–80 | > 80 | ICP-OES |
| Aluminium (Al) | ppm | < 20 | 20–50 | > 50 | ICP-OES |
| Zinn (Sn) | ppm | < 10 | 10–25 | > 25 | ICP-OES |
| Blei (Pb) | ppm | < 15 | 15–30 | > 30 | ICP-OES |
| Silizium (Si) | ppm | < 25 | 25–50 | > 50 | ICP-OES |
| Natrium (Na) | ppm | < 50 | 50–200 | > 200 | ICP-OES (Seewasser-Indikator!) |
| Viskosität 40°C | cSt | ±10 % Frischöl | ±10–20 % | > ±20 % | Viskosimeter |
| TAN (Säurezahl) | mgKOH/g | < 1,5 | 1,5–2,5 | > 2,5 | Titration |
| Oxidation | Abs/cm | < 10 | 10–20 | > 20 | FTIR |
| Partikelzahl > 4µm | /ml | < 5.000 | 5.000–15.000 | > 15.000 | Partikelzähler |
| Partikelzahl > 14µm | /ml | < 500 | 500–2.000 | > 2.000 | Partikelzähler |

**Interpretationshilfe:**
- Hohe Fe-Werte → Zahnrad- oder Lagerverschleiß
- Hohe Cu-Werte → Bronze-Buchsen oder Messing-Synchronringe verschleißen
- Hohe Al-Werte → Gehäusekorrosion (besonders bei Saildrives!)
- Hohe Na-Werte → Seewassereintritt über Ölkühler!
- Wasser > 500 ppm → SOFORT Ölwechsel und Ursache suchen

**Ölanalyse-Anbieter (Marine):**

| Anbieter | Land | Preis pro Probe | Turnaround |
|---|---|---|---|
| Oelcheck (oelcheck.de) | DE | €30–50 | 3–5 Werktage |
| POLARIS Laboratories | USA | $30–50 | 3–5 Werktage |
| Wearcheck | UK | £25–40 | 3–5 Werktage |
| Spectro Scientific | INT | $35–55 | 3–5 Werktage |

(Confidence: documented / measured)

### Anhang V: Elektro-Saildrive — Zukunftstechnologie

Mit dem Wachstum der elektrischen Antriebe im Bootsbau entstehen neue Saildrive-Konzepte:

| Produkt | Hersteller | Typ | Leistung | Gewicht | Preis (ca.) | Status |
|---|---|---|---|---|---|---|
| SD8.0 EVO | Oceanvolt | Elektrischer Saildrive | 8 kW | 28 kg | €12.000 | Verfügbar |
| SD15.0 EVO | Oceanvolt | Elektrischer Saildrive | 15 kW | 42 kg | €18.000 | Verfügbar |
| Sail 6.0 Evo | ePropulsion | Elektrischer Saildrive | 6 kW | 22 kg | €8.000 | Verfügbar |
| Sail 12.0 Evo | ePropulsion | Elektrischer Saildrive | 12 kW | 38 kg | €14.000 | Verfügbar |
| Saildrive E | Torqeedo | Elektrischer Saildrive | 10 kW | 32 kg | €15.000 | Verfügbar |
| ZF eSaildrive | ZF Marine | Hybrid-Saildrive | 20 kW | 55 kg | €25.000+ | Entwicklung |

**Besonderheiten Elektro-Saildrive:**
- Keine obere Getriebeeinheit (Direktantrieb oder einfache Untersetzung)
- Membran-Problematik identisch zu Diesel-Saildrive
- Regeneration unter Segel möglich (Propeller treibt Generator)
- Geringere Vibrationen als Diesel
- Kein Getriebeöl (weniger Wartung)
- Anodenschutz weiterhin erforderlich
- Gewicht des Batteriepacks muss in Trimm-Berechnung berücksichtigt werden

(Confidence: documented / benchmark)

### Anhang W: Historische Getriebe-Identifikation

Für die Bewertung älterer Boote (Baujahr vor 2000) ist die Identifikation des Getriebes oft schwierig. Hier Erkennungsmerkmale:

**Hurth (vor ZF-Übernahme):**
- Typenschild: „HURTH" oder „Hurth-Getriebe Werk"
- Modellbezeichnung: HBW 5, HBW 10, HBW 50, HBW 100, HBW 125, HBW 150, HBW 250
- Gehäusefarbe: Grau oder Silber (unbehandelt Alu)
- Gussform: Rundlich, kompakt
- Baujahr: 1960er–1990er

**Borg Warner Velvet Drive (US):**
- Typenschild: „BORG WARNER" oder „Velvet Drive"
- Modell: 10-18, 71C, 72C
- Gehäuse: Alu-Guss, eckiger als ZF
- Öleinfüllschraube oben (auffällig großer Sechskant)
- Baujahr: 1960er–2005

**Paragon (US, historisch):**
- Typenschild: „PARAGON" oder „Capitol Marine Gear"
- Modell: P-21, P-31, HF-7
- Gehäuse: Gusseisen (schwer!)
- Baujahr: 1950er–1980er

**MS-Getriebe (Volvo):**
- Typenschild: „VOLVO PENTA" mit MS-Bezeichnung
- Modell: MS, MS2, MS10, MS15, MS25
- Gehäuse: Alu-Guss, Volvo-typische Form
- Konuskupplung (MS10/15) erkennbar an Stellmutter
- Baujahr: 1960er–2000er

**Erkennung ohne Typenschild:**
1. Gehäuseform mit Referenzfotos vergleichen (Internet-Datenbanken)
2. SAE-Gehäusegröße messen (Bohrbild am Motor-Anschluss)
3. Abtriebsflansch-Maße aufnehmen
4. Ölsorte am Messstab prüfen (Rot = ATF = hydraulisch)
5. Motor-Hersteller + Baujahr → Getriebe-Zuordnung über OEM-Tabelle

(Confidence: documented)

### Anhang X: Getriebe-Geräusch-Diagnose

Akustische Diagnose ist ein wichtiges Werkzeug bei der Getriebebewertung. Folgende Geräusche sind typisch:

| Geräusch | Beschreibung | Wann hörbar | Mögliche Ursache | Dringlichkeit |
|---|---|---|---|---|
| Leises Summen | Gleichmäßig, tonal | Neutral, laufend | Normal (Zahneingriff) | Keine |
| Rasseln, kalt | Klappernd, metallisch | Neutral, kalt | Zahnflankenspiel (normal bei kalt) | Keine (wenn warm weg) |
| Rasseln, warm | Klappernd, konstant | Neutral, warm | Lager verschlissen, Zahnrad lose | MITTEL |
| Heulen/Jaulen | Tonal, drehzahlabhängig | Unter Last | Zahnflanken-Verschleiß | MITTEL |
| Mahlen/Knirschen | Raues Reibgeräusch | Beim Schalten | Klauenkupplung (mech.): zu schnell geschaltet | HOCH |
| Klacken (einzeln) | Einmaliges Klack | Beim Einlegen V/R | Normal bei hydraul. Kupplung (Lamellen greifen) | Keine |
| Klacken (rhythmisch) | Wiederholt, drehzahlsynchron | Unter Last | Zahnrad beschädigt (gebrochener Zahn!) | SOFORT! |
| Pfeifen | Hoher Ton, konstant | Ab bestimmter Drehzahl | Ölpumpe kavitiert (Ölstand zu niedrig?) | HOCH |
| Schlagen/Hämmern | Starkes Klopfen | Unter Last | Wellenbruch, Kupplungsfeder gebrochen | SOFORT! |
| Quietschen | Hohes Quietschen | Beim Schalten | Bowdenzug klemmt, Getriebehebel fest | MITTEL |
| Dumpfes Brummen | Tieffrequent, Vibration spürbar | Bestimmte Drehzahl | Resonanz (Motor↔Fundament↔Rumpf) | GERING |
| Unterwasser-Geräusch (Saildrive) | Mahlend, summend | Unter Last | Kegelrad-Lager untere Einheit | HOCH |

**Diagnose-Werkzeug:** Ein einfaches Mechaniker-Stethoskop (€15–30) am Getriebegehäuse angelegt gibt präzise Auskunft über die Geräuschquelle. Verschiedene Positionen testen: Getriebe oben (Lamellen), Getriebe unten (Lager), Getriebe-Abtrieb (Simmerring/Flansch).

(Confidence: documented)

### Anhang Y: Saildrive-Rumpfbohrung — Verstärkungsrichtlinien

Die Rumpfbohrung für einen Saildrive muss strukturell verstärkt sein. Bei Booten ohne werksseitige Vorbereitung oder bei Nachrüstung gelten folgende Richtlinien:

| Parameter | Minimum | Empfohlen | Messmethode |
|---|---|---|---|
| GFK-Wandstärke an Bohrung | 8 mm | 12–15 mm | Ultraschall |
| Verstärkungslaminat-Ausdehnung | 150 mm über Bohrungsrand | 250 mm | Messschieber |
| Verstärkungslaminat-Lagen | 4 Lagen CSM + 4 Lagen Roving | 6+6 | Querschnitt |
| Planlage der Auflagefläche | ±0,5 mm | ±0,2 mm | Richtlineal + Fühlerblatt |
| Bohrungsrand-Finish | Entgratet, versiegelt | Laminat-geschützt, Epoxy | Sichtprüfung |
| Kernmaterial entfernt | Min. 100 mm um Bohrung | 200 mm | Ultraschall/Klopftest |
| Montageschrauben | M10 Edelstahl 316L | M12 Edelstahl 316L | — |
| Schrauben-Anzahl | 4 (min.) | 6–8 (Herstellervorgabe) | — |
| Drehmoment Befestigung | Herstellerangabe | 25–35 Nm (M10) | Drehmomentschlüssel |
| Dichtmittel unter Flansch | Sikaflex 291 oder gleichwertig | 3M 5200 (permanent) | — |

**WARNUNG:** Saildrive-Nachrüstung in einen nicht vorbereiteten Rumpf ist ein struktureller Eingriff, der von einer zertifizierten Werft oder einem Sachverständigen begleitet werden MUSS. Falsche Ausführung gefährdet die Rumpfintegrität!

(Confidence: documented)

### Anhang Z: Versicherungs- und Haftungsfragen

| Thema | Regelung | Relevanz für Eigner |
|---|---|---|
| Saildrive-Membranwechsel | Kaskoversicherung deckt Folgeschäden NUR bei nachweisbar eingehaltenen Wartungsintervallen | Wartungsnachweis aufbewahren! |
| Getriebeschaden durch falsches Öl | Eigenverschulden → Kaskoversicherung kann Leistung kürzen | Ölspezifikation beachten, Quittungen aufbewahren |
| Sinken durch Membranversagen | Kaskoversicherung prüft Alter der Membran und Wartungshistorie | Membranwechsel dokumentieren! |
| Personenschaden durch Antriebsausfall | Haftpflichtversicherung greift, aber Regress bei grober Fahrlässigkeit möglich | Regelmäßige Wartung ist PFLICHT |
| CE-Konformität nach Saildrive-Tausch | Bei Änderung des Antriebssystems kann CE-Konformität erlöschen | Werft muss Konformität bestätigen |
| Gutachten bei Getriebe-/Saildrive-Schaden | Sachverständigengutachten (BSV, BVWW) empfohlen ab Schadenssumme > €2.000 | Fotos + Ölprobe SOFORT sichern |
| Gewährleistung Neugetriebe | 2 Jahre (B2C) / 1 Jahr (B2B), herstellerabhängig | Einbau durch autorisierte Werkstatt dokumentieren |
| Gewährleistung Membranwechsel | Materialgarantie des Herstellers (1–2 Jahre), Einbaugarantie der Werft | Werft-Rechnung aufbewahren |
| Haftung bei DIY-Einbau | Volle Eigenhaftung, keine Gewährleistung vom Hersteller bei nachweisbarem Einbaufehler | Einbauanleitung exakt befolgen, dokumentieren |

(Confidence: documented)

---

*Ende des Wissensmoduls 18_07 — Getriebe und Saildrive*
*AYDI Maritime Knowledge Base — Version 2.0 — April 2026*
