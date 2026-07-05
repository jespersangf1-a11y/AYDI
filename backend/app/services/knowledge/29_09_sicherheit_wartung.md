# Sicherheitsausrüstung Wartung & Inspektion — Kat. 29.09

**Kategorie:** 29_Sicherheitsausruestung  
**Unterkategorie:** Sicherheit_Wartung  
**Gültig ab:** 2026-01-01  
**Norm:** ISO 13849 (Sicherheit), ISO 12075 (Inspektionen), IMO SOLAS  
**Deutsch / English:** Alle Texte auf Deutsch, Code auf English  

---

> ⚠️ **ZU PRÜFEN (Audit):** Kopf-Norm "ISO 12075 (Inspektionen)" ist keine marine Inspektionsnorm — unter dieser Nummer ist nur ISO/IEC TR 12075 (IT-/Token-Ring-Verkabelung) geführt. Die tatsächlich gemeinte Inspektionsnorm ist unklar (Kandidaten: ISO 9650 Rettungsinseln, ISO 18813 Sicherheitsausrüstung, SOLAS); Nummer daher unverändert belassen, bitte fachlich prüfen.

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

**Autor:** AYDI Knowledge Base  
**Kontakt:** knowledge@aydi.de  
**Letzte Überarbeitung:** 2026-05-18  
**Nächste Review:** 2027-05-18
