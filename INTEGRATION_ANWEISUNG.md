# Anweisung: Markdown-Recherche-Dateien in AYDI integrieren

## Kontext

In diesem Projekt-Ordner (`backend/app/services/knowledge/`) liegen 16+ Markdown-Recherche-Dateien (Format `XX_YY_thema.md`, jeweils 3.800+ Zeilen). Diese Dateien wurden durch Recherche-Aufträge erstellt, waren aber NICHT in das System integriert — sie lagen nur als Dateien rum, ohne dass die App sie nutzt.

In einem anderen Chat wurde eine vollständige Integration gebaut. Diese Anweisung beschreibt exakt, was gemacht wurde und was du tun musst, damit zukünftige Recherche-Dateien automatisch integriert sind.

---

## Was bereits existiert (NICHT nochmal erstellen!)

Diese Dateien existieren bereits im Projekt und sind funktionsfähig:

### 1. `markdown_knowledge_loader.py` (1.253 Zeilen)
**Pfad:** `backend/app/services/knowledge/markdown_knowledge_loader.py`

Das ist der Kern-Parser. Er:
- Findet automatisch alle `XX_YY_*.md` Dateien im knowledge-Ordner
- Parst sie in strukturierte Python-Dicts (Sektionen, Tabellen, Hersteller, FAQ, Glossar, Fehlerbilder, Fallstudien, Erfahrungsberichte, Experten-Referenzen)
- Lazy-loaded Singleton — wird beim ersten Zugriff geladen
- Bietet Such-, Filter- und Aggregations-Funktionen
- Mappt Slugs auf Analyse-Kontexte (materials, structural, compliance, service_patterns, production)

**Erkannte Formate (beide werden geparst):**

| Datentyp | Neues Format (05_10+) | Altes Format (04_13–05_09) |
|----------|----------------------|---------------------------|
| Hersteller | `**Firmenprofil:**` + Bullet-Liste | `## XX. Hersteller: Name (Land)` |
| FAQ | `### FAQ N: Frage` | `### FN: Frage` oder nummerierte Subsections unter `## XX. FAQ` |
| Glossar | Tabelle unter `## Glossar` | Tabelle unter `## XX. Glossar` oder `## ANHANG X — Glossar` |
| Fehlerbilder | `### Fehlerbild N: Titel` | `### FN: Titel` unter `## ANHANG F — Fehlerbild-Atlas` |
| Fallstudien | `### Fallstudie N: Titel` | `### D.N Fallstudie: Titel` unter `## ANHANG D — Fallstudien` |
| Erfahrungsberichte | `**Erfahrungsbericht — Quelle:**` + Blockquote | Tabellen mit `Kernerkenntnis`-Spalte unter Forum-Sections |
| Experten | `**Experten-Referenz — Quelle:**` + Blockquote | Tabellen unter Experten/Fachliteratur-Sections |

### 2. Modifizierte `__init__.py`
Am Ende der Datei wurden Imports hinzugefügt:
```python
from .markdown_knowledge_loader import (
    get_markdown_knowledge,
    get_knowledge_by_slug,
    get_knowledge_by_category,
    get_all_manufacturers as get_markdown_manufacturers,
    get_all_erfahrungsberichte,
    get_all_fehlerbilder,
    get_all_fallstudien,
    get_all_faq as get_markdown_faq,
    get_all_glossary as get_markdown_glossary,
    get_all_expert_references,
    search_markdown_knowledge,
    format_markdown_knowledge_for_prompt,
    get_markdown_knowledge_summary,
    get_relevant_slugs_for_context,
)
```

### 3. Modifizierte `knowledge_retrieval.py`
- Import von `get_relevant_slugs_for_context`, `format_markdown_knowledge_for_prompt`, `get_all_erfahrungsberichte`, `get_all_fehlerbilder`
- `get_knowledge_for_materials_analysis()` — angereichert mit Markdown-Fehlerbildern, Erfahrungsberichten, FAQ aus material-relevanten Slugs
- `get_knowledge_for_service_patterns()` — angereichert mit Markdown-Fehlerbildern und Fallstudien aus service-relevanten Slugs
- `format_knowledge_for_prompt()` — hängt "=== Recherche-Wissen (Detailliert) ===" an mit Fehlerbildern und Erfahrungsberichten
- `list_available_knowledge_databases()` — zeigt Markdown-Datenbanken in Zusammenfassung

### 4. Modifizierte `backend/app/api/routes/knowledge.py`
3 neue REST-Endpoints:
- `GET /api/v1/knowledge/research` — Aggregierte Zusammenfassung
- `GET /api/v1/knowledge/research/{slug}` — Detail pro Thema
- `GET /api/v1/knowledge/research/search/{query}` — Volltextsuche

### 5. Tests: `backend/tests/test_markdown_knowledge_loader.py` (232 Zeilen, 27 Tests)

---

## Was du tun musst bei JEDER neuen Recherche-Datei

### A. Datei-Benennung
Neue Recherche-Dateien MÜSSEN diesem Muster folgen:
```
XX_YY_thema_name.md
```
Beispiele: `01_01_luken_dichtungen.md`, `02_03_teakdeck_fugenmasse.md`

### B. SLUG_TO_RETRIEVAL_CONTEXT aktualisieren
In `markdown_knowledge_loader.py` gibt es ein Dict `SLUG_TO_RETRIEVAL_CONTEXT` (ca. Zeile 900+). Für jede neue Datei MUSS ein Eintrag hinzugefügt werden:

```python
SLUG_TO_RETRIEVAL_CONTEXT = {
    # Bestehende Einträge...

    # NEUE Einträge:
    "luken_dichtungen": ["materials", "compliance"],
    "fenster_dichtungen": ["materials", "compliance"],
    "pu_dichtstoffe_elastisch": ["materials", "service_patterns"],
    # ... etc
}
```

Die Kontexte bestimmen, in welchen Analyse-Pipelines das Wissen auftaucht:
- `materials` → Material-Analyse
- `structural` → Struktur-Analyse
- `compliance` → Normen/Compliance
- `service_patterns` → Service/Wartung
- `production` → Produktions-Analyse

### C. Formatierung für maximale Extraktion
Damit der Parser maximale Daten extrahiert, nutze bevorzugt diese Formate:

**Hersteller:**
```markdown
## XX. Hersteller: Sika (Schweiz)
### XX.1 Firmenprofil
- Gegründet: 1910
- Herkunft: Baar, Schweiz
- Spezialisierung: Dicht- und Klebstoffe
- Website: www.sika.com
```

**FAQ:**
```markdown
### FAQ 1: Kann man Sikaflex 291 auf nassem Untergrund verwenden?
Nein. Der Untergrund muss trocken und sauber sein...
(Confidence: documented)
```

**Glossar:**
```markdown
## Glossar

| Begriff (DE) | Begriff (EN) | Definition |
|---|---|---|
| Fugenmasse | Sealant / Caulk | Elastische Masse zum Abdichten von Fugen |
```

**Fehlerbilder:**
```markdown
### Fehlerbild 1: Sikaflex-Ablösung nach 2 Jahren
**Symptom:** Dichtmasse löst sich vom Untergrund
**Ursache:** Fehlender Primer oder fettiger Untergrund
**Häufigkeit:** Sehr häufig (häufigster DIY-Fehler)
**Maßnahme:** Alte Masse komplett entfernen, Primer 210T auftragen, neu abdichten
**Confidence:** documented
```

**Fallstudien:**
```markdown
### Fallstudie 1: Teakdeck-Neuverfugung Bavaria 40
**Boot:** Bavaria 40, Baujahr 2008, Mittelmeer
**Problem:** Alle Fugen undicht nach 12 Jahren
**Ursache:** Original-Fugenmasse (Sikaflex 290 DC) am Ende der Lebensdauer
**Lösung:** Komplette Neuverfugung mit Simson MSR Teak Caulk
**Kosten:** 1.800 € Material + 2 Wochen DIY oder 6.500 € Werft
**Lektion:** Alle 10–15 Jahre Neuverfugung einplanen
**Confidence:** documented
```

**Erfahrungsberichte:**
```markdown
**Erfahrungsbericht — Cruisers Forum, User 'SailingDog', 2024:**
> "Sikaflex 291 has been my go-to for 20 years. One tip: always use primer 210T on gelcoat. Without primer, it peels off in 2-3 years. With primer, I've seen 15+ year bonds."
```

**Experten-Referenzen:**
```markdown
**Experten-Referenz — Nigel Calder, "Boatowner's Mechanical and Electrical Manual":**
> "The single most important factor in sealant adhesion is surface preparation. A sealant is only as good as the surface it bonds to."
```

### D. Qualitätscheck-Schwellenwerte
Jede Datei muss diese Mindestanforderungen erfüllen:
- Zeilen ≥ 3.800
- H2 ≥ 10
- H3 ≥ 30
- Tabellen ≥ 100
- Hersteller ≥ 10
- Forum-Referenzen ≥ 5
- YouTube-Referenzen ≥ 5
- Experten-Zitate ≥ 10
- Anhänge ≥ 4
- Fallstudien ≥ 5
- FAQ ≥ 5
- Glossar ≥ 20
- Fehlerbilder ≥ 5
- Pydantic model_config ≥ 3
- Confidence-Tags ≥ 10

---

## Aktuelle Statistik (Stand: 29.03.2026)

```
16 Dateien integriert, 66.225 Zeilen
1.458 strukturierte Einträge:
  - 113 Hersteller
  - 145 Erfahrungsberichte
  - 347 FAQ
  - 438 Glossar-Einträge
  - 170 Fehlerbilder
  - 81 Fallstudien
  - 164 Experten-Referenzen
27/27 Tests bestanden
```

## Fehlende Recherche-Dateien (laut Inhaltsverzeichnis)

Kategorie 1 — Dichtungen und Profile: 01_01 bis 01_12 (12 Dateien)
Kategorie 2 — Dichtstoffe und Kleber: 02_01 bis 02_13 (13 Dateien)
Kategorie 3 — Beschichtungen und Farben: 03_01 bis 03_16 (16 Dateien)
Kategorie 4 — Harze/Fasern: 04_01 bis 04_12 (12 Dateien)
Kategorie 6 — Schläuche: 06_02+ (noch offen)

Gesamt fehlend: ~53 Dateien

---

## Zusammenfassung

1. Neue `.md` Datei erstellen mit korrektem Dateinamen `XX_YY_name.md`
2. Formatierungsregeln oben beachten für maximale Parser-Extraktion
3. `SLUG_TO_RETRIEVAL_CONTEXT` in `markdown_knowledge_loader.py` um neuen Slug ergänzen
4. Datei wird beim nächsten App-Start automatisch geladen und in alle Analyse-Pipelines injiziert
5. Keine weiteren Code-Änderungen nötig — der Parser erkennt neue Dateien automatisch
