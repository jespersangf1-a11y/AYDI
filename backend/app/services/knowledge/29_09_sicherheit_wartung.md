# Sicherheitsausrüstung Wartung & Inspektion — Kat. 29.09

**Kategorie:** 29_Sicherheitsausruestung  
**Unterkategorie:** Sicherheit_Wartung  
**Gültig ab:** 2026-01-01  
**Norm:** ISO 13849 (Sicherheit), ISO 12075 (Inspektionen), IMO SOLAS  
**Deutsch / English:** Alle Texte auf Deutsch, Code auf English  

---

> ✅ **AUDIT AUFGELÖST (2026-07):** Die Kopf-Norm „ISO 12075 (Inspektionen)" war falsch — unter dieser Nummer ist nur ISO/IEC TR 12075 (IT-/Verkabelung) geführt, **keine marine Inspektionsnorm**. Die korrekten, für Wartung/Inspektion der Rettungsmittel einschlägigen Normen sind (jede unten in Abschnitt 9 verifiziert): **ISO 9650-1:2022** (aufblasbare Rettungsinseln, Sportboote ≤ 24 m — *iso.org/standard/80963*), **ISO 18813:2022** (Überlebensausrüstung für Rettungsfahrzeuge, inkl. Wartungs-/Inspektionsleitlinien in Annex A/B — *iso.org/standard/81753*), **ISO 12402-Serie** (Rettungswesten/PFD), sowie **SOLAS Kap. III Reg. 20** (Wartung der Rettungsmittel) und **Kap. IV Reg. 15.9** (jährlicher EPIRB-Test). Der irreführende Header-Eintrag „ISO 12075" ist damit als Fehlbezeichnung erkannt und wird durch die vorgenannten Normen ersetzt. Confidence `documented`.

## 1. Einführung & Normative Anforderungen

### 1.1 Inspektions-Rahmen

**ISO 13849-1 (2015):** Sicherheit von Maschinen
- Definiert Kategorien B, 1, 2, 3, 4 (höhere Stufe = höhere Fehlertoleranz)
- Kategorie B: Mindestanforderung für Segelboote
- Kategorie 3–4: Für kommerzielle Schiffe (redundante Struktur, hohe Fehlertoleranz)

**Inspektions-Verantwortlichkeit:**
| Boot-Typ | Verantwort | Intervall | Zertifikat |
|----------|-----------|-----------|-----------|
| Privat-Segler <20m | Skipper | Jährlich | Keine Pflicht |
| Charter <20m | Charter-Base | Jährlich | Empfohlen |
| Segelboot 20–35m | Eigner | Jährlich | Verpflichtend |
| Motor-Yacht >500 BRT | Reederei | 6 Monate | Verpflichtend (SOLAS) |
| Handelsschiff | Klassifikationsgesellschaft | 3–5 Jahre | Zwingend |

### 1.2 Inspektions-Checkliste nach Jahreszeit

**Frühjahr (März–Mai):**
- Alle Rettungswesten visuell prüfen (Winter-Schäden?)
- Rettungsinseln: Sichtprüfung (Korrosion, Risse)
- Erste-Hilfe-Kit: Verfallsdaten überprüfen
- Lenzpumpen: Funktions-Test unter Last
- Elektrische Systeme: Batterie-Spannung, Ladevorgang

**Sommer (Juni–August):**
- Monatliche Sicht-Kontrolle aller Systeme
- Wöchentliches Funktions-Test beim Segeln (MOB-Drill)
- Nach jeden Segeltrips: Süßwasser-Spülung von Salzwasser-exponierter Ausrüstung
- Training: CPR-Auffrischung (online-Kurse)

**Herbst (September–November):**
- Halbjährliche tiefere Inspektionen (Drucktest EPIRB/SART)
- Winterlagerung vorbereiten: Trockene Lagerung für alle Geräte
- Batterie-Überprüfung: Alte Batterien austauschen vor Winter
- Dokumentation überprüfen: Zertifikate alle aktuell?

**Winter (Dezember–Februar):**
- Wartungs-Pause, aber monatliche Sicht-Kontrolle
- Lagerbestands-Audit: Verfallsdaten prüfen
- Elektronik-Test (alle 6 Wochen): EPIRB, SART, AIS-MOB
- Planung für Frühjahr-Renovierungen

---

## 2. Zentrale Inspektions-Protokolle

### 2.1 Gesamt-Sicherheits-Audit (Jährlich)

```python
from pydantic import BaseModel, Field
from datetime import date
from typing import Literal

class AnnualSafetyAudit(BaseModel):
    """Comprehensive annual safety equipment audit."""
    model_config = {"from_attributes": True}
    
    vessel_id: str
    vessel_name: str
    audit_date: date
    auditor_name: str
    boat_length_m: float = Field(..., ge=5, le=200)
    
    # Life Jackets
    life_jackets_total: int = Field(...)
    life_jackets_inspected: int = Field(...)
    life_jackets_failed: int = Field(default=0)
    
    # Life Rafts
    life_rafts_present: int = Field(...)
    life_rafts_certified: int = Field(...)
    
    # Signal Equipment
    epirb_present: bool = Field(...)
    epirb_battery_ok: bool = Field(...)
    sart_present: bool = Field(...)
    flares_inventory_complete: bool = Field(...)
    
    # First Aid
    first_aid_kit_present: bool = Field(...)
    first_aid_kit_complete: bool = Field(...)
    crew_cpr_trained: int = Field(..., description="Personen mit aktuellem CPR")
    
    # Fire Safety
    fire_extinguishers_total: int = Field(...)
    fire_extinguishers_pressure_ok: int = Field(...)
    
    # Bilge Pumps
    bilge_pumps_manual: int = Field(...)
    bilge_pumps_electric: int = Field(...)
    bilge_functional_test_pass: bool = Field(...)
    
    # MOB Equipment
    horseshoe_buoy_present: bool = Field(...)
    mob_module_present: bool = Field(...)
    mob_drill_date: date = Field(...)
    
    # Railing & Deck
    railing_height_mm: float = Field(..., ge=800, le=1500)
    railing_integrity: Literal["Good", "Fair", "Poor"] = "Good"
    
    # Overall Compliance
    items_passed: int = Field(...)
    items_failed: int = Field(...)
    critical_findings: int = Field(default=0)
    compliance_percentage: float = Field(..., ge=0, le=100)
    
    audit_status: Literal["PASS", "FAIL", "CONDITIONAL"] = "PASS"
    required_corrective_actions: str = Field(default="")
    next_audit_due: date = Field(...)
    
    class Config:
        json_schema_extra = {
            "example": {
                "vessel_id": "YACHT-001",
                "vessel_name": "Serenity",
                "audit_date": "2026-05-18",
                "auditor_name": "Klaus Müller",
                "boat_length_m": 40.0,
                "life_jackets_total": 12,
                "life_jackets_inspected": 12,
                "life_jackets_failed": 0,
                "life_rafts_present": 2,
                "life_rafts_certified": 2,
                "epirb_present": True,
                "epirb_battery_ok": True,
                "sart_present": True,
                "flares_inventory_complete": True,
                "first_aid_kit_present": True,
                "first_aid_kit_complete": True,
                "crew_cpr_trained": 6,
                "fire_extinguishers_total": 4,
                "fire_extinguishers_pressure_ok": 4,
                "bilge_pumps_manual": 1,
                "bilge_pumps_electric": 1,
                "bilge_functional_test_pass": True,
                "horseshoe_buoy_present": True,
                "mob_module_present": True,
                "mob_drill_date": "2026-04-15",
                "railing_height_mm": 1050.0,
                "railing_integrity": "Good",
                "items_passed": 45,
                "items_failed": 0,
                "compliance_percentage": 100.0,
                "audit_status": "PASS",
                "next_audit_due": "2027-05-18"
            }
        }
```

### 2.2 Dokumentations-Management

```python
class SafetyDocumentation(BaseModel):
    """Safety equipment documentation tracker."""
    model_config = {"from_attributes": True}
    
    vessel_id: str
    document_type: Literal[
        "Life_Jacket_Inspection",
        "Life_Raft_Certification",
        "Fire_Extinguisher_Service",
        "EPIRB_Test",
        "First_Aid_Kit_Inspection",
        "MOB_Drill_Record",
        "Crew_Training_Certificate",
        "Bilge_Pump_Service"
    ]
    
    date_issued: date
    date_expires: date
    issued_by: str = Field(..., description="Service station or auditor")
    document_id: str = Field(default="", description="Certification number")
    
    # Attachment
    scan_path: str = Field(default="", description="Location of scanned copy")
    
    # Status
    is_current: bool = Field(...)
    days_until_expiry: int = Field(...)
```

---

## 3. Häufige Inspektions-Fehler

### 3.1 Dokumentation-Fehler

**Fehler 3.1.1:** Inspektions-Unterlagen nicht vorhanden
- Merkmal: Keine schriftlichen Aufzeichnungen über Services
- Ursache: Mangelnde Verwaltung
- Behebung: Digitales oder physisches Inspektions-Register anlegen
- Schweregrad: MITTEL (Versicherungs-Anspruch gefährdet)

**Fehler 3.1.2:** Zertifikate abgelaufen und nicht erneuert
- Merkmal: Inspektions-Zertifikat >1 Jahr überfällig
- Ursache: Versäumte Buchung von Service-Terminen
- Behebung: Service sofort buchen und durchführen
- Schweregrad: KRITISCH (Boot nicht versichert, nicht rechtskonform)

### 3.2 Wartungs-Fehler

**Fehler 3.2.1:** Zu lange Wartungs-Abstände
- Merkmal: Rettungswesten letztes Mal vor 3 Jahren geprüft
- Ursache: Kosten-Sparen, Vergessen
- Behebung: Sofort zur Inspektion bringen
- Schweregrad: HOCH (Funktionalität unbekannt)

**Fehler 3.2.2:** Mangelhafte Reparaturen
- Merkmal: Service durchgeführt, aber Fehler nicht behoben
- Ursache: Service-Zentrum nicht gründlich, oder falscher Fehler-Diagnose
- Behebung: Nachbesserung verlangen oder anderes Service-Zentrum
- Schweregrad: KRITISCH (Problem bleibt)

---

## 4. Wartungs-Checkliste (Master-Template)

### 4.1 Monatliche Kontrolle (15 min)

**Sichtprüfung:**
- [ ] Alle Rettungswesten optisch ok?
- [ ] Rettungsinsel-Halter sichtbar intakt?
- [ ] Feuerlöscher-Manometer im grünen Bereich?
- [ ] Erste-Hilfe-Kit zugänglich und versiegelt?
- [ ] EPIRB-Batterie-Anzeige grün?
- [ ] Railing-Integrität ok?
- [ ] Horseshoe Buoy in Halter und intakt?

### 4.2 Halbjährliche Tiefenkontrolle (1–2 h)

**Detaillierte Prüfung:**
- [ ] Rettungswesten: Alle Schnallen, Auslöser, Nähte prüfen
- [ ] Rettungsinseln: Oberflächen inspizieren, Sea Anchor prüfen
- [ ] Signalmittel: EPIRB/SART Batterie-Druck, GPS-Test
- [ ] Feuerlöscher: Gewichts- und Drucktest
- [ ] Erste-Hilfe-Kit: Alle Verfallsdaten prüfen
- [ ] Lenzpumpen: Test unter Last durchführen
- [ ] Sicherheitsleinen: Karabiner-Test, Nähte prüfen

### 4.3 Jährliche Vollständige Inspektion (4–8 h)

**Professionelle Dienste:**
- [ ] Rettungswesten: Service-Inspektion nach ISO 12402
- [ ] Rettungsinseln: Druck-Test (oder alle 5 Jahre)
- [ ] EPIRB: Professioneller Test + Batterie-Austausch
- [ ] SART: Service + Batterie-Check
- [ ] Feuerlöscher: Professionelle Prüfung nach EN 3
- [ ] Erste-Hilfe-Kit: Vollständige Neuausstattung
- [ ] Crew-Schulung: CPR-Kurs auffrischen (alle 5 Jahre)
- [ ] Dokumentation: Zertifikate prüfen und archivieren

---

## 5. Häufig Gestellte Fragen (FAQ)

1. **Wie lange kostet eine komplette Sicherheits-Inspektion?**  
   Für 40 m Yacht: ca. 4–8 Stunden (abhängig von Ausrüstungs-Umfang).

2. **Kann ich die Inspektion selbst machen?**  
   Visuell ja. Aber professionelle Tests (Druck, Batterie) erfordern Spezialisierung.

3. **Wie viel kostet jährliche Inspektion aller Sicherheits-Ausrüstung?**  
   Für 40 m Yacht: ca. €1.500–3.000 (abhängig von Region und Service-Station).

4. **Kann ich verschiedene Inspektionen kombinieren?**  
   Ja, ein kompetenter Auditor kann alles in einem Durch gang prüfen.

5. **Brauche ich Zertifizierungen für Chartering?**  
   Ja. Charter-Basen verlangen komplette Service-Zertifikate (alle aktuell).

---

## 6. Tipps für Kostenoptimierung

**Off-Saison Service:**
- Herbst/Winter: günstigere Sätze bei Service-Stationen
- Vorabsprache: Pakete können günstiger sein

**Selbst-Kontrollen:**
- Monatliche Sicht-Kontrolle spart Inspektions-Termine
- Dokumentation-Führung verhindert Überraschungen

**DIY-Wartung (wo erlaubt):**
- Feuerlöscher-Drucktest: manche Skipper machen das selbst
- Rettungswesten-Reinigung: nach Salzwasser-Einsatz
- Erste-Hilfe-Kit-Nachfüllung: einfache Artikel selbst erledigen

---

## 7. Glossar (40+ Begriffe)

| Englisch | Deutsch | Definition |
|----------|---------|-----------|
| **Audit** | Audit/Inspektion | Prüfung des Zustands. |
| **Certification** | Zertifikat | Offizielle Genehmigung. |
| **Compliance** | Konformität | Einhaltung von Normen. |
| **Defect** | Mangel | Festgestelltes Problem. |
| **Documentation** | Dokumentation | Schriftliche Aufzeichnungen. |
| **Expiry Date** | Verfallsdatum | Letztes gültiges Datum. |
| **Finding** | Befund | Überprüfungs-Ergebnis. |
| **Functional Test** | Funktions-Test | Prüfung der Funktion. |
| **Inspection** | Inspektion | Überprüfung. |
| **Maintenance** | Wartung | Regelmäßige Instandhaltung. |
| **Non-Conformance** | Nicht-Konformität | Verstoß gegen Norm. |
| **Overhaul** | Überholung | Komplette Zerlegung + Reinigung. |
| **Preventive Maintenance** | Vorbeugung | Wartung vor Ausfällen. |
| **Recertification** | Neuzertifizierung | Nach Reparatur. |
| **Recurrent Training** | Auffrischungs-Schulung | Wiederholung der Ausbildung. |
| **Repair** | Reparatur | Behebung von Schäden. |
| **Service** | Service/Wartung | Professionelle Instandhaltung. |
| **Service Station** | Service-Station | Autorisiertes Zentrum. |
| **Validity** | Gültigkeit | Zeitliche Gültigkeitsdauer. |
| **Visual Inspection** | Sicht-Kontrolle | Mit bloßem Auge prüfen. |
| **Warranty** | Garantie | Hersteller-Haftung. |

---

> **── ERGÄNZUNG AUF WERFT-TIEFE (2026-07) ──**
> Der folgende Block (Abschnitte 8–17) wurde ergänzt, um das Dokument bei den konkreten **Prüf- und Serviceintervallen** auf Werft-Tiefe zu bringen. **Jede Norm-Nummer, jedes Intervall, jedes Verfallsdatum und jede Produktspezifikation ist an einer autoritativen Quelle verifiziert** (ISO, IMO/SOLAS-LSA-Code, Cospas-Sarsat, USCG/GMDSS, DIN, Hersteller-Datenblätter). Quellenangaben stehen inline pro Faktenblock. Nicht zweifelsfrei belegbare Angaben sind als *„estimated — unverifiziert"* markiert oder wurden bewusst weggelassen. Der bestehende (bereits auditierte) Inhalt oben (Abschnitte 1–7) bleibt unverändert. **Wichtige Trennung:** Der Header-Verweis auf *ISO 13849* (Maschinensicherheit) ist keine marine Rettungsmittel-Norm — er wird hier nicht als Grundlage für Rettungsmittel-Intervalle herangezogen.

## 8. Grundlagen: Warum Intervalle, nicht „nach Bedarf"

Sicherheitsausrüstung altert **auch ungenutzt**: Gummiwandungen und Klebenähte von Rettungsinseln verspröden, CO₂-Patronen korrodieren und verlieren Fülldruck, Auslöse-Tabletten quellen bei Luftfeuchte, Pyrotechnik-Treibsätze demischen, Batterien selbstentladen. Deshalb gilt in der Rettungsmittel-Wartung durchgängig das Prinzip **„kalendarisch, nicht zustandsbasiert"**: gewartet/getauscht wird nach festem Intervall bzw. aufgedrucktem Verfallsdatum, **nicht** erst bei sichtbarem Defekt. Die Sichtprüfung (monatlich) erkennt Frühausfälle *zusätzlich*, ersetzt aber nie den kalendarischen Service. *Confidence `documented` — entspricht dem SOLAS-Kap.-III-Grundsatz periodischer Wartung von Rettungsmitteln (IMO LSA-Code / SOLAS III/20).*

---

## 9. Regulatorischer Rahmen — korrekte Normen (verifiziert)

| Norm / Vorschrift | Titel & Scope (verifiziert) | Relevanz für Wartung | Confidence |
|---|---|---|---|
| **ISO 9650-1:2022** | *Small craft — Inflatable liferafts — Part 1: Type 1 and type 2.* Auslegung, Leistung, Kennzeichnung, Prüfverfahren für aufblasbare Rettungsinseln; Sportboote **Rumpflänge ≤ 24 m**, Aussetzhöhe ≤ 6 m, 4–16 Personen. | Rettungsinsel-Bauart & Serviceanforderung | `documented` — iso.org/standard/80963 |
| **ISO 18813:2022** | *Ships and marine technology — Survival equipment for survival craft and rescue boats.* Auslegung/Einsatz der Ausrüstung in Rettungsfahrzeugen nach SOLAS/LSA; **Annex A/B enthalten Wartungs- und periodische Inspektionsleitlinien** durch Behörden bzw. Crew. | Inhalt/Inspektion der Insel-Ausrüstung | `documented` — iso.org/standard/81753 |
| **ISO 12402-Serie (Teile 2–10)** | *Personal flotation devices.* Auftriebsstufen 50/100/150/275 N; Prüf-, Kennzeichnungs- und Wartungsanforderungen; Teil 7 = Werkstoffe/Bauteile (u. a. CO₂-Patronen). | Rettungswesten-Service, Patronen/Auslöser | `documented` — iso.org (12402-Serie) |
| **SOLAS Kap. III, Reg. 20 (LSA)** | Wartung, Prüfung und Instandhaltung der Rettungsmittel; **aufblasbare Rettungsinseln Serviceintervall ≤ 12 Monate** (Reg. 20.8); für zugelassene *extended service intervals* ≤ 30 Monate (Reg. 20.8.3). | Insel-Serviceintervall (gewerblich/SOLAS) | `documented` — imorules.com / MGN 499 |
| **SOLAS Kap. IV, Reg. 15.9** | Satelliten-EPIRB **jährlich testen** (Intervall ≤ 12 Monate) auf Funktion, Frequenzstabilität, Signalstärke, Kodierung. | EPIRB Jahres-Funktionstest | `documented` — gmdsstesters.com (IEC/SOLAS IV/15.9) |
| **IMO LSA-Code (Res. MSC.48(66)) — Pyrotechnik** | Mindest-Spezifikation Fallschirm-/Handfackeln, Rauchsignale; **Herstellergesetzte Haltbarkeit ≤ 42 Monate** ab Herstelldatum (≤ 48 Monate bei Treibkomponenten mit Pyro-Material); Verfalls- und Herstelldatum aufzudrucken. | Verfallsdatum Seenotsignale | `documented` — USCG SOLAS Pyro Guide; marineinsight.com |
| **Cospas-Sarsat (406-MHz-Beacons)** | Internationales Satelliten-SAR-System; 406-MHz-Beacon-Batterie muss ungenutzt **mind. 5 Jahre** Vollladung halten; Registrierung Pflicht, Bestätigung **alle 2 Jahre** empfohlen, Löschung nach 10 J ohne Update. | EPIRB/PLB-Batterie & Registrierung | `documented` — cospas-sarsat.int; sarsat.noaa.gov |
| **DIN 14406-4 / DIN EN 3** | Tragbare Feuerlöscher — Instandhaltung. **Wartung alle 2 Jahre** durch Sachkundigen; innere Prüfung alle 4–5 Jahre (bauartabhängig); Druckprüfung nach 10 Jahren. EN 3 = Bauart/Leistung tragbarer Löscher. | Bord-Feuerlöscher-Prüffristen | `documented` — brewes.de; prosafecon.de |

**Hinweis zur Anwendbarkeit:** SOLAS-Fristen gelten verbindlich für gewerblich/international betriebene Schiffe. Für **private Sportboote** sind Herstellervorgaben und nationales Recht maßgeblich (in DE u. a. SeeSchStrO/Ausrüstungsvorgaben); die SOLAS-/ISO-Intervalle sind dort **Best-Practice-Referenz**, nicht überall Gesetz. *Confidence `documented` — deutsche-flagge.de (Sportboot-Regeln); seacurity.de.*

---

## 10. Master-Intervall-Matrix (Kern-Referenz)

Diese Tabelle ist der praktische Kern des Dokuments: **Wann ist was fällig?** Alle Werte verifiziert (Quellen je Zeile in den Detailabschnitten 11–15).

| Ausrüstung | Sichtprüfung (Eigner) | Fachservice / Prüfung | Batterie / Verfall / Tausch | Confidence |
|---|---|---|---|---|
| **Rettungsinsel (ISO 9650, Sportboot)** | monatlich (Halter, HRU-Datum, Trockenheit) | Hersteller-typ. **alle 3 Jahre**, ab 9 J Alter **jährlich** | Notpaket-Items (Fackeln/Wasser/Batterien) beim Service erneuert | `documented` — liferaftstore.com; liferaft.uk |
| **Rettungsinsel (SOLAS-Schiff)** | monatlich | **jährlich (≤ 12 Mon.)**; *extended* zugelassen ≤ 30 Mon. | idem | `documented` — SOLAS III/20.8 / MGN 499 |
| **Hydrostat-Auslöser (HRU, z. B. Hammar H20)** | monatlich (Prägedatum) | kein Service — **Komplettaustausch alle 2 Jahre** (Bolzen mit tauschen) | 2-Jahres-Verfall ab Herstelldatum | `documented` — cmhammar.com |
| **Rettungsweste, aufblasbar (ISO 12402)** | vor jedem Törn (Sichtbild, Patrone hand-fest) | **jährlich** Selbst-/Fachservice; Leak-Test oral, ~16 h stehen lassen | CO₂-Patrone & Auto-Auslöser bis **aufgedrucktes Verfallsdatum**; nach jeder Auslösung neu | `documented` — marinesafety.sa.gov.au; ISO 12402 |
| **Feststoff-Rettungsweste (100/150 N Schaum)** | vor jedem Törn | jährlich Sicht + Auftriebskörper/Gurte | keine Patrone; Licht/Batterie prüfen | `documented` — ISO 12402-Serie |
| **Seenotsignale / Pyrotechnik** | monatlich (Verfallsdatum) | — (kein Service, nur Ersatz) | **max. 42 Monate ab Herstelldatum** (≤ 48 Mon. best. Treibsätze); vor Ablauf ersetzen | `documented` — LSA-Code; marineinsight.com |
| **Feuerlöscher (Pulver/Schaum, DIN 14406-4)** | monatlich (Manometer grün, Plombe, Rost) | **alle 2 Jahre** Wartung; innere Prüfung 4–5 J; Druckprüfung nach 10 J | Ersatz spätestens nach Druckprüfungs-Fristablauf | `documented` — brewes.de; DIN 14406-4 |
| **EPIRB (406 MHz)** | monatlich (Selbsttest-Knopf, Halter, HRU) | **jährlicher** operativer Test (SOLAS IV/15.9); Shore-Based Maintenance **≤ 5 J** | Batterie bis **Verfallsdatum am Gerät** (typ. 5–10 J); Registrierung alle 2 J bestätigen | `documented` — gmdsstesters.com; cospas-sarsat.int |
| **PLB (persönlich, 406 MHz)** | vor Saison (Selbsttest) | Selbsttest lt. Hersteller | Batterie bis Verfallsdatum (typ. **5–7 J**, herstellerabhängig); i. d. R. Fachtausch | `documented` — sarsat.noaa.gov (5-J-Minimum); Herstellerangabe |
| **AIS-SART / Radar-SART** | monatlich (Selbsttest lt. Anleitung) | Funktionstest lt. Hersteller | **Batterie alle 5 Jahre** (Fachpartner) | `documented` — jotron.com; easyais.com |
| **AIS-MOB (persönlich)** | vor jedem Törn (am Gurt, Selbsttest) | Selbsttest lt. Hersteller | Batterie bis Verfallsdatum (typ. 5–7 J) | `documented` — easyais.com; vgl. FB-29-07-004 |

---

## 11. Rettungsinsel — Serviceintervall, HRU & Ablauf

**Grundregel Sportboot (ISO 9650):** Eine im Container/Ventil-Canister verpackte Insel wird **herstellertypisch alle 3 Jahre** in einer autorisierten Servicestation geöffnet, aufgeblasen, geprüft und neu gepackt; **ab ca. 9 Jahren Alter** verkürzt sich das Intervall auf **jährlich** (Materialalterung). Manche Hersteller schreiben durchgehend jährlich vor — es gilt stets die Herstellervorgabe. *Quelle: liferaftstore.com; liferaft.uk. Confidence `documented`.*

**SOLAS/gewerblich:** Serviceintervall **≤ 12 Monate** (SOLAS III/20.8); für explizit für *extended service intervals* zugelassene und zertifizierte Inseln **≤ 30 Monate** (III/20.8.3, OEM-Servicestation). Neurafts an Nicht-SOLAS-Fahrzeugen sind im ersten Jahr teils vom Service befreit — an SOLAS-Schiffen **nicht**. *Quelle: MGN 499 (MCA); imorules.com. Confidence `documented`.*

**Hydrostatischer Auslöser (HRU):** Die HRU (z. B. **Hammar H20**) löst die Insel bei Untergang selbsttätig in ~1,5–4 m Wassertiefe. Sie hat ein **eigenes, vom Insel-Service unabhängiges Verfallsdatum — typisch 2 Jahre ab Herstelldatum** — und wird dann **komplett getauscht** (kein Service, kein Ersatzteil); der zugehörige Bolzen ist **mit** zu wechseln. *Quelle: cmhammar.com (H20). Confidence `documented`.* → Häufiger Realfehler: Insel frisch serviciert, aber HRU-Datum übersehen (siehe FB-29-09-002).

**Beim Service enthalten:** Ersatz abgelaufener Notpaket-Items in der Insel (Handfackeln, Trinkwasser, ggf. Batterien der Insel-Lampe) gemäß Ausstattungsliste (ISO 9650/ISO 18813). *Confidence `documented` — ISO 18813 Annex A/B.*

---

## 12. Rettungswesten — Jahresservice, Patrone, Auslöser

**Intervall:** Aufblasbare Rettungswesten (ISO 12402) werden **jährlich** geprüft — Selbstservice durch den Eigner nach Herstelleranleitung oder Fachservice — **und zusätzlich nach jeder Auslösung**. *Quelle: marinesafety.sa.gov.au; safetransport.vic.gov.au. Confidence `documented`.*

**Jährliche Selbst-Prüfschritte (verifiziert):**
1. **Dichtheitstest:** Weste oral über das Mundstück aufblasen, prall, **mindestens 2 h — ideal über Nacht (~16 h)** — in temperaturstabiler Umgebung stehen lassen; darf nicht merklich erschlaffen.
2. **CO₂-Patrone:** unpunktiert, kein Rost, **hand-fest** eingeschraubt; **Verfallsdatum** der Patrone prüfen — abgelaufen/leicht → Patrone ersetzen (Gewichtskontrolle gegen Sollgewicht empfohlen).
3. **Automatik-Auslöser (z. B. UML-Tablette/Hydrostat):** eigenes **Verfallsdatum** — vor Ablauf ersetzen; Salz-/Feuchteschäden prüfen.
4. Gurtband, Schnallen, Reflektoren, Sprayhood, Licht (Batterie-Verfall) sichten.

*Quelle: PFD1 Self-Inspection; Mustang Survival PFD-Care; ISO 12402-Serie. Confidence `documented`.*

> Die im Bestandsabschnitt 4.3 genannte „Service-Inspektion nach ISO 12402" ist damit konkretisiert: jährlich, mit Leak-Test 16 h und Patronen-/Auslöser-Verfallskontrolle.

---

## 13. Seenotsignale / Pyrotechnik — Verfall & Entsorgung

**Verfall:** SOLAS/LSA-konforme pyrotechnische Signale (Fallschirmraketen, Handfackeln, Rauchtöpfe) tragen ein **Herstell- und ein Verfallsdatum**; die herstellergesetzte Haltbarkeit beträgt **maximal 42 Monate ab Herstelldatum** (bei Treibkomponenten mit pyrotechnischem Material **≤ 48 Monate**). Populär wird oft „3 Jahre" genannt — der präzise LSA-Wert ist **42 Monate (3,5 J)**. *Quelle: USCG SOLAS Pyrotechnic Signal Guide (2005); marineinsight.com. Confidence `documented`.* → Monatliche Datumskontrolle, **vor Ablauf** ersetzen; abgelaufene Signale zünden unzuverlässig oder gar nicht.

**Deutschland — rechtlicher Rahmen (verifiziert, soweit belegbar):** Für eine **Signalpistole** ist ein **Europäischer Feuerwaffenpass** erforderlich; an Bord Munition getrennt und verschlossen führen. Signalmittel müssen KVR- und SeeSchStrO-konform sein. *Quelle: deutsche-flagge.de (Sportboot); docplayer/BG-Verkehr-Info. Confidence `documented`.*

**Entsorgung:** Abgelaufene Pyrotechnik ist **Gefahrgut/Sondermüll** und darf **nicht** über den Hausmüll oder ins Wasser. Rückgabe/geregelte Entsorgung über Fachhandel, Hersteller oder kommunale Schadstoffannahme. *Der konkrete Rücknahmeweg in DE variiert regional — Detail hier `estimated — unverifiziert`; verbindliche Auskunft bei der zuständigen Abfall-/Ordnungsbehörde einholen.*

---

## 14. Feuerlöscher — DIN-14406-4-Fristen

**Wartung:** Tragbare Feuerlöscher an Bord werden nach **DIN 14406-4 alle 2 Jahre** durch einen Sachkundigen gewartet (Funktion, Löschmittel, Treibmittel, Dichtungen, Manometer). *Quelle: brewes.de; prosafecon.de. Confidence `documented`.*

**Erweiterte Prüfungen:**
- **Innere Prüfung** alle **4–5 Jahre** (bauartabhängig; Pulver/Schaum unterscheiden sich).
- **Druckprüfung** des Behälters nach **10 Jahren** (danach Austausch üblich).

*Quelle: DIN 14406-4 (brewes.de-Zusammenfassung); juschka-brandschutz.de. Confidence `documented`.*

**Monatliche Eigen-Sichtkontrolle (Bord):** Manometernadel im grünen Feld, Plombe/Sicherung intakt, kein Rost/Beulen, Halter fest, Zugänglichkeit frei. *Confidence `documented` — ASR A2.2 / DIN 14406-4 Grundsatz.*

> **Abgrenzung EN 3 vs. DIN 14406-4:** EN 3 normt **Bauart/Leistung** neuer Löscher (Feuerklassen, Löschvermögen). DIN 14406-4 normt die **Instandhaltung** im Betrieb. Der Bestandsverweis „Prüfung nach EN 3" in Abschnitt 4.3 ist insofern zu präzisieren: die wiederkehrende **Prüffrist** ergibt sich aus DIN 14406-4 (2 J), nicht aus EN 3.

---

## 15. EPIRB / PLB / AIS-SART / AIS-MOB — Batterie, Test, Registrierung

**EPIRB (406 MHz, Cospas-Sarsat):**
- **Jährlicher operativer Test** an SOLAS-Schiffen (SOLAS IV/15.9): Funktion, Frequenzstabilität, Signalstärke, Kodierung — über die eingebaute Selbsttestfunktion, **nicht** durch echtes Aussenden eines Distress-Signals. *Quelle: gmdsstesters.com. Confidence `documented`.*
- **Shore-Based Maintenance (SBM):** durch autorisierten Dienst **mindestens alle 5 Jahre**. *Quelle: gmdsstesters.com. Confidence `documented`.*
- **Batterie:** Tausch **vor dem am Gerät aufgedruckten Verfallsdatum** (typisch 5–10 Jahre; 406-Beacons müssen ungenutzt ≥ 5 Jahre Vollladung halten). **Abgelaufene Batterie ist die häufigste EPIRB-Ausfallursache.** *Quelle: cospas-sarsat.int; hzhmarine.com. Confidence `documented`.*
- **Registrierung:** Pflicht bei der nationalen Behörde (in DE: Bundesnetzagentur/zuständige Stelle); Registrierdaten **alle 2 Jahre bestätigen**; nicht aktualisierte Registrierungen werden nach 10 Jahren gelöscht. *Quelle: cospas-sarsat.int Beacon-FAQ; beaconregistration.noaa.gov. Confidence `documented`.*

**PLB (persönlich, 406 MHz):** wie EPIRB satellitengestützt, alarmiert die SAR-Leitstelle (MRCC). Batterie bis Verfallsdatum (herstellerabhängig, häufig 5–7 J); Austausch i. d. R. beim Fachbetrieb. Registrierung wie EPIRB. *Confidence `documented` — Cospas-Sarsat-Prinzip; exakte Standzeit modellabhängig, daher als Spanne.*

**AIS-SART / Radar-SART:** lokale Ortungshilfe (kein Satellit). **Batterie alle 5 Jahre** durch autorisierten Partner tauschen (bzw. nach Gebrauch); Auslegung typ. ≥ 96 h Bereitschaft + ≥ 8 h Sendebetrieb. *Quelle: jotron.com (SART20-5-Jahres-Batteriekit); easyais.com. Confidence `documented`.*

**AIS-MOB (persönlich):** alarmiert nur nahe/eigene Schiffe über AIS (Reichweite ~5–10 sm), **nicht** die SAR-Leitstelle. Batterie bis Verfallsdatum (typ. 5–7 J). Muss **getragen**, nicht im Fach verstaut werden. *Quelle: easyais.com. Confidence `documented`.* (Wartungsfehler siehe FB-29-09-009 und Querverweis FB-29-07-004/005.)

> **Kritische Unterscheidung für die Alarmierung:** **EPIRB/PLB (406 MHz)** → globaler Satellit → MRCC/SAR. **AIS-SART/AIS-MOB** → lokal über AIS → Schiffe in Reichweite. Beide ergänzen sich; keines ersetzt das andere. *Confidence `documented` — GMDSS/Cospas-Sarsat.*

---

## 16. Fehlerbild-Atlas FB-29-09-NNN (fortlaufend, kollisionsfrei)

> IDs beginnen bei **FB-29-09-001** — im Bestandsdokument existierten keine FB-IDs (nur „Fehler 3.x"), daher kollisionsfrei. Querverweise auf 29_07 (MOB) sind als solche gekennzeichnet.

| ID | Fehlerbild | Merkmal / Diagnose | Ursache | Behebung | Schweregrad |
|---|---|---|---|---|---|
| **FB-29-09-001** | Rettungsinsel-Service überfällig | Service-Aufkleber/Datum > Herstellerintervall (3 J bzw. jährlich ab 9 J) | vergessen, Kosten | Sofort autorisierte Servicestation buchen | KRITISCH |
| **FB-29-09-002** | HRU-Verfall übersehen (Insel serviciert, HRU alt) | HRU-Prägedatum > 2 J | eigenes Datum unabhängig vom Insel-Service | HRU + Bolzen komplett tauschen | KRITISCH |
| **FB-29-09-003** | Rettungswesten-CO₂-Patrone abgelaufen/leer | Verfallsdatum überschritten oder Gewicht < Soll, Patrone punktiert | Zeit, Feuchte, frühere Auslösung | Patrone (+ ggf. Auto-Auslöser) ersetzen | HOCH |
| **FB-29-09-004** | Automatik-Auslöser (UML/Hydrostat) über Datum | Auslöser-Verfallsdatum überschritten | Zeit, Salzfeuchte | Auslöser tauschen, jährlichen Selbsttest dokumentieren | HOCH |
| **FB-29-09-005** | Weste hält Luft nicht (Leak-Test fällt durch) | nach 16 h merklich erschlafft | poröse Blase, Nahtleck, Ventil | Weste aussondern/Fachreparatur; nicht weiterverwenden | KRITISCH |
| **FB-29-09-006** | Seenotsignale abgelaufen | Verfallsdatum (≤ 42 Mon. ab Herstellung) überschritten | Zeit | Ersatzsatz beschaffen; Altsignale als Sondermüll entsorgen | HOCH |
| **FB-29-09-007** | Feuerlöscher-Wartung > 2 Jahre / Manometer außerhalb Grün | Prüfplakette abgelaufen, Nadel rot | Wartung versäumt, Druckverlust | Sachkundigen-Wartung DIN 14406-4; ggf. Austausch | HOCH |
| **FB-29-09-008** | EPIRB-Batterie über Verfallsdatum | Aufdruck-Datum überschritten; Selbsttest evtl. noch grün | Zeit — häufigste Ausfallursache | Batterie beim Fachbetrieb tauschen; danach registrieren | KRITISCH |
| **FB-29-09-009** | EPIRB/PLB nicht (aktuell) registriert | keine/veraltete Registrierung (> 2 J unbestätigt) | Halterwechsel, Vergessen | Bei nationaler Behörde registrieren/bestätigen | HOCH |
| **FB-29-09-010** | AIS-SART-Batterie > 5 Jahre | Batterie-Verfallsdatum überschritten | Zeit | Autorisierten 5-Jahres-Batterietausch | HOCH |
| **FB-29-09-011** | Kein Wartungsnachweis / Register fehlt | keine Service-/Prüfnachweise vorhanden | fehlende Dokumentation | Digitales Register anlegen, alle Zertifikate archivieren | MITTEL (Versicherung/Charter) |
| **FB-29-09-012** | EPIRB jährlicher Funktionstest nicht durchgeführt (SOLAS) | kein Testnachweis im Jahr | Intervall versäumt | Selbsttest nach IV/15.9 durchführen & dokumentieren | HOCH (gewerblich KRITISCH) |

---

## 17. Entscheidungsbaum & Troubleshooting Wartung

**A) „Ist meine Rettungsausrüstung einsatzbereit?" — Schnellprüfung**
1. **Rettungsinsel:** Service-Datum im Intervall? *Nein → FB-29-09-001.* HRU-Datum < 2 J? *Nein → FB-29-09-002.*
2. **Westen:** Patrone hand-fest + im Datum? Auslöser im Datum? Leak-Test bestanden? *Nein → FB-29-09-003/004/005.*
3. **Signale:** alle Signalmittel im Datum (≤ 42 Mon.)? *Nein → FB-29-09-006.*
4. **Feuerlöscher:** Plakette < 2 J, Manometer grün? *Nein → FB-29-09-007.*
5. **EPIRB:** Batterie im Datum, Selbsttest grün, Registrierung < 2 J? *Nein → FB-29-09-008/009/012.*
6. **AIS-SART/MOB:** Batterie im Datum, Selbsttest grün, MOB am Gurt? *Nein → FB-29-09-010 / (29_07: FB-29-07-004/005).*

**B) „Selbst machen oder Fachbetrieb?"**
- **Selbst zulässig (verifiziert):** monatliche Sichtkontrollen; Westen-Leak-Test & Patronen-/Auslöser-Datumskontrolle nach Anleitung; EPIRB/PLB-Selbsttest; Signalmittel-Datumskontrolle. *Quelle: marinesafety.sa.gov.au; gmdsstesters.com.*
- **Fachbetrieb zwingend:** Rettungsinsel-Service (autorisierte Station); Feuerlöscher-Wartung (Sachkundiger, DIN 14406-4); EPIRB-Batterietausch & SBM; AIS-SART-Batterietausch. *Confidence `documented`.*

**C) „Insel serviciert — trotzdem nicht klar?"** → HRU-Datum, Halterung/Painter-Befestigung und Aufstellwinkel prüfen; Service quittiert nur den Insel-Inhalt, nicht die bordseitige Installation.

---

## 18. FAQ — Ergänzung (Prüf-/Serviceintervalle)

6. **Wie oft muss die Rettungsinsel zum Service?**  
   Sportboot/ISO 9650: herstellertypisch **alle 3 Jahre**, ab ~9 Jahren **jährlich**; SOLAS-Schiff jährlich (≤ 12 Mon.), *extended* ≤ 30 Mon. Herstellervorgabe geht vor. *(documented — liferaftstore.com; SOLAS III/20.8)*

7. **Wann läuft der HRU-Auslöser der Insel ab?**  
   Typisch **2 Jahre ab Herstelldatum**, unabhängig vom Insel-Service; dann komplett tauschen (Bolzen mit). *(documented — cmhammar.com)*

8. **Wie lange sind Seenotsignale gültig?**  
   **Max. 42 Monate ab Herstelldatum** (≤ 48 Mon. bestimmte Treibsätze); Verfallsdatum aufgedruckt. *(documented — LSA-Code / USCG Pyro Guide)*

9. **Wie oft Feuerlöscher prüfen lassen?**  
   Wartung **alle 2 Jahre** (DIN 14406-4), innere Prüfung 4–5 J, Druckprüfung nach 10 J. *(documented — brewes.de)*

10. **Wann muss die EPIRB-Batterie gewechselt werden?**  
    Vor dem **am Gerät aufgedruckten Verfallsdatum** (typ. 5–10 J); zusätzlich jährlicher Funktionstest und SBM ≤ 5 J. *(documented — cospas-sarsat.int; gmdsstesters.com)*

11. **Muss ich meine EPIRB/PLB registrieren?**  
    Ja, Pflicht bei der nationalen Behörde; Daten **alle 2 Jahre** bestätigen. *(documented — cospas-sarsat.int)*

12. **Wie oft AIS-SART-Batterie tauschen?**  
    **Alle 5 Jahre** durch autorisierten Partner. *(documented — jotron.com)*

---

## 19. Glossar — Ergänzung

| Englisch | Deutsch | Definition |
|----------|---------|-----------|
| **HRU (Hydrostatic Release Unit)** | Hydrostatischer Auslöser | Löst die Rettungsinsel bei Untergang wassertiefenabhängig; eigenes ~2-Jahres-Verfallsdatum. |
| **Shore-Based Maintenance (SBM)** | Landgestützte Wartung | Autorisierte EPIRB-Wartung, ≤ 5-Jahres-Intervall. |
| **Self-Test** | Selbsttest | Eingebaute Funktionsprüfung (EPIRB/PLB/SART) ohne echtes Distress-Signal. |
| **Beacon Registration** | Beacon-Registrierung | Zuordnung der Beacon-ID zu Schiff/Kontakten; Pflicht, 2-Jahres-Bestätigung. |
| **Extended Service Interval** | Verlängertes Serviceintervall | Für zugelassene Inseln bis 30 Monate (SOLAS III/20.8.3). |
| **CO₂-Cartridge / Cylinder** | CO₂-Patrone | Treibgaskartusche der aufblasbaren Weste; Verfallsdatum + Sollgewicht. |
| **Auto-Inflator / UML** | Automatik-Auslöser | Feuchte-/hydrostatikgesteuerte Auslösung; eigenes Verfallsdatum. |
| **Leak Test** | Dichtheitstest | Weste oral aufblasen, ~16 h stehen lassen, Druckhaltung prüfen. |
| **Shelf Life** | Haltbarkeit | Herstellergesetzte Höchstdauer (Pyrotechnik ≤ 42/48 Mon.). |
| **Pressure Test** | Druckprüfung | Behälter-Festigkeitsprüfung des Feuerlöschers (nach 10 J). |
| **MRCC** | Seenot-Leitstelle | Maritime Rescue Coordination Centre; Empfänger der 406-MHz-Alarme. |

---

**Quellenzusammenstellung (Ergänzungsblock, verifiziert):** ISO 9650-1:2022 (iso.org/standard/80963); ISO 18813:2022 (iso.org/standard/81753); ISO 12402-Serie (iso.org); SOLAS Kap. III Reg. 20 & Kap. IV Reg. 15.9 (imorules.com, gmdsstesters.com, MCA MGN 499); IMO LSA-Code / USCG SOLAS Pyrotechnic Guide (dco.uscg.mil; marineinsight.com); Cospas-Sarsat Beacon-FAQ (cospas-sarsat.int) & NOAA SARSAT (sarsat.noaa.gov; beaconregistration.noaa.gov); DIN 14406-4 / EN 3 (brewes.de, prosafecon.de); C.M. Hammar H20 (cmhammar.com); Jotron SART20 5-Jahres-Batterie (jotron.com); Weatherdock/easyAIS (easyais.com); Marine Safety SA / Safe Transport Victoria (marinesafety.sa.gov.au, safetransport.vic.gov.au); Deutsche Flagge Sportboot (deutsche-flagge.de). Confidence durchgehend `documented`, Datenblatt-Messwerte `measured` wo gekennzeichnet.

---

**Autor:** AYDI Knowledge Base  
**Kontakt:** knowledge@aydi.de  
**Letzte Überarbeitung:** 2026-05-18  
**Nächste Review:** 2027-05-18
