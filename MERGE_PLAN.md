# Merge-Plan: `audit/fixes-checkpoint` → `main`

**Zweck:** Übergabe für eine frische Sitzung. Der Merge wurde einmal begonnen
(15 von 40 Konflikten aufgelöst) und bewusst abgebrochen, um keinen halb
aufgelösten Zustand zu hinterlassen. Diese Datei hält fest, was die Analyse
ergeben hat — damit niemand sie wiederholen muss.

**Stand bei Erstellung:** 27.08.2026 · `audit/fixes-checkpoint` = `b12f751` ·
1.775 Tests grün · Praxistest 123/123 · Frontend-Build grün

---

## Ausgangslage

```
gemeinsame Basis        840c999   16.04.2026
origin/main             ed3e67e   28.07.2026    5 eigene Commits
audit/fixes-checkpoint  b12f751   27.08.2026   49 eigene Commits
```

Die Zweige sind **auseinandergelaufen**, nicht nur vorausgeeilt. `main` hat
eigene Arbeit, die dem Branch fehlt. Ein Merge ist kein Fast-Forward.

**Umfang:** 119 Konfliktblöcke in 40 Dateien (`git merge origin/main`).

> **Wichtig für Vercel/Deployment:** Vercel deployt aus `main`. Solange dieser
> Merge nicht durch ist, bleibt die Production-URL auf dem Juli-Stand. GitHub
> zeigt auf der Repo-Startseite ebenfalls `main` — deshalb wirkt das Repo
> „seit einem Monat unverändert", obwohl 49 Commits auf dem Branch liegen.

---

## Beide Seiten haben unabhängig dieselben Probleme gelöst

Keine Seite dominiert. Das ist der Kern der Merge-Arbeit.

| Nur auf `main` | Nur auf `audit/fixes-checkpoint` |
|---|---|
| `core/ownership.py` — Zugriffslücke: jedes angemeldete Konto konnte fremde Materialien, Serviceberichte, Wettbewerbsmodelle lesen/ändern/löschen | Score-Fusion verdrahtet (`visual_fusion.py`) — Fotos beeinflussen Noten |
| `analysis/scoring.py` — `weighted_overall`, `NICHT_BEWERTBAR = None` | `analysis/subscore.py` — `aggregate_subscores`, Absturzbehandlung |
| `core/zone_types.py` — einheitliche Zonentyp-Schreibweise | `ZONE_TYPE_ALIASES` in `validation.py` (galley→pantry, salon→saloon) |
| `core/boat_classes.py` — 13 Klassen, deutsche Labels | `VALID_BOAT_CLASSES` aus dem Enum abgeleitet + i18n-Labels |
| `db/schema_sync.py` — Index-/Spalten-Nachzug beim Start | Bildanalyse als Hintergrundauftrag + Migration `007` |
| `db/types.py` — `UtcDateTime` | `warning_i18n.py` — Übersetzung an der Präsentationsgrenze |
| `--no-server-header` (uvicorn) | `severity_burden` — Schadensschwere wirkt auf die Note |
| Sicherheitsheader | Sicherheitsheader (**echte Doppelung**) |
| Warnungs-Codes: ergonomics 9, volume_storage 4, emotional 0 | Warnungs-Codes: 16 / 15 / 17 |

### Der wichtigste Einzelfund

`main/scoring.py` und `branch/subscore.py` lösen **komplementäre Hälften**
desselben Problems:

- **main:** Teilanalyse gibt `None` zurück, wenn ihr die *Datengrundlage* fehlt.
- **branch:** Teilanalyse *stürzt ab* (Exception) und wird aus der Rechnung genommen.

Beide schließen aus und normieren neu. Mains `None`-Konvention ist die sauberere
API und deckt zusätzlich den „nichts zu prüfen"-Fall ab, den meine nicht kennt.

**Zusammengeführt ergibt das einen besseren Mechanismus als jede Seite für sich:**
`scoring.py` behalten, den Absturzfall einfügen, indem eine abgestürzte
Teilanalyse schlicht `None` einträgt. Ein Konzept statt zwei.

---

## Auflösungsregel

### 1. Analysemodule (11 Dateien) → `main` als Basis
`main`s Fassung ist die gründlichere Überarbeitung (`None`-Konvention, Hinweis
auf unbekannte Zonentypen, `location`-Feld). Danach diese Beiträge des Branches
wieder aufsetzen:

- **`severity_burden`** in `service_patterns.py` — fünfte Teilanalyse, Gewicht
  0,26, übrige auf 0,74 reskaliert (Summe muss exakt 1,0 bleiben, der
  BoatDNA-Resolver prüft das). Ohne sie hat die Schwere eines Schadens **keinen**
  Einfluss auf die Note (gemessen: 10 kosmetische = 10 kritische Befunde).
- **Relativer Filter** in `analyze_zone_type_issues`: greift nur ab 3 Zonentypen.
  Sonst unterdrückt er Befunde ausgerechnet bei viel Evidenz (60 Totalschäden
  wurden besser bewertet als 20).
- **`params`-Dicts** an den 9 i18n-Fundstellen (siehe `warning_i18n.py`).
- **`passage_width` / `known_passage_widths`-Guards** — Durchgänge ohne bekannte
  Breite (DXF-Import) dürfen keine Teilanalyse zum Absturz bringen.
- **Fehlende Warnungs-Codes** ergänzen (v.a. `emotional`: main hat dort 0).

### 2. Rechte, Sicherheit, Seed, Datenbank → `main`
`auth.py`, `competitors.py`, `materials.py`, `service_reports.py`, `seed.py`,
`database.py`, `main.py`. Dort liegt Substanz, die dem Branch fehlt.

**Ausnahme `models.py`: kombinieren, nicht wählen.** Beide Seiten haben Spalten
ergänzt — `main` die Besitzerspalten und `UtcDateTime`, der Branch
`ai_analysis_status` (Migration `007`).

### 3. Bildrouten, Layouts, Schemas, Middleware, Config → Branch
Dort liegt die Substanz des Branches; `main`s Ergänzungen einarbeiten:

- `middleware.py`: **Sicherheitsheader beider Seiten zusammenführen** (Doppelung).
  Vom Branch behalten: Rate-Limit-Regeln (gemustert statt Präfix), CSRF-Ausnahme
  als exakter Pfad, `Accept-Language` mit q-Werten.
- `config.py`: Branch hat `ANTHROPIC_MODEL=claude-opus-5` (mains Wert ist
  zurückgezogen → 404) und `VISUAL_ANALYSIS_TIMEOUT_SEC=120`.

### 4. Infrastruktur → gemischt
- `Dockerfile.backend` + `entrypoint.sh`: **Entrypoint behalten** (führt
  `alembic upgrade head` vor uvicorn aus) **und** `--no-server-header` von `main`
  ergänzen. Erledigt im abgebrochenen Versuch — Vorlage:
  `exec uvicorn app.main:app --host 0.0.0.0 --port "${PORT}" --no-server-header "$@"`
- `docker-compose.yml`: Branch-Fassung (alembic + `--reload`) plus `--no-server-header`.
- `frontend/package.json` + `package-lock.json`: `main` (neueres dompurify + `@types`).

### 5. Tests
`main`s Fassung, danach die Erwartungen des Branches nachziehen. Betroffen:
`test_brand_dna`, `test_cost`, `test_market`, `test_materials`,
`test_service_patterns`, `test_structural`.

### 6. `CLAUDE.md`
Von Hand. Beide Seiten haben umfangreich daran gearbeitet.

---

## Fallen, die beim ersten Versuch aufgefallen sind

- **Migrationen müssen idempotent sein.** Revision `000` baut das Schema per
  `Base.metadata.create_all` aus den **Live-Modellen** — eine frische Datenbank
  hat jede neue Spalte deshalb schon bei `000`. Alle Migrationen ab `001` prüfen
  vorher per Inspector. Migration `007` folgt dem Muster.
- **Hintergrundaufträge brauchen eine eigene DB-Sitzung.** Die der Anfrage ist
  nach der Antwort geschlossen. `images.background_session_factory` ist die
  überschreibbare Indirektion, damit Tests auf dieselbe DB zeigen.
- **Zwei Vokabular-Quellen dürfen nicht wieder entstehen.** Nach dem Merge prüfen:
  `VALID_ZONE_TYPES` ↔ Domänen-Zonentypen und `VALID_BOAT_CLASSES` ↔ `BoatClass`
  müssen deckungsgleich sein (`tests/test_zone_type_vocabulary.py`,
  `tests/test_boat_class_vocabulary.py`).
- **Spezifikations-Wächter schlagen absichtlich an.**
  `tests/test_claude_md_spec_matches_code.py` pinnt u.a. die Migrationszahl (8)
  und dass die Score-Fusion verdrahtet ist. Wenn er rot wird, ist meist
  CLAUDE.md nachzuziehen — nicht der Test aufzuweichen.

---

## Verifikation nach dem Merge

```bash
cd backend
PYTHONPATH=. python -m pytest tests/ -q          # Ziel: keine Fehler
PYTHONPATH=. python praxistest_full.py           # Ziel: 123/123
cd ../frontend && npm run build                  # tsc + vite, muss grün sein
```

Zusätzlich gegen Doppelstrukturen prüfen:

```bash
cd backend
grep -rn "subscore\|scoring" app/services/analysis/*.py | head   # nur EIN Mechanismus
grep -rn "SecurityHeaders\|nosniff" app/core/middleware.py       # nur EINE Stelle
```

Migration gegen eine **frische** Datenbank:

```bash
cd backend && rm -f /tmp/merge.db
DATABASE_URL="sqlite+aiosqlite:////tmp/merge.db" PYTHONPATH=. alembic upgrade head
```

---

## Offene Punkte unabhängig vom Merge

Vollständig in [aydi_verbesserung_protokoll.md](aydi_verbesserung_protokoll.md):

- **E5** — i18n-Mechanismus steht, 20 von 155 Codes übersetzt (33 % der Warnungen
  im Reallauf). Rest ist Fleißarbeit nach feststehendem Muster.
- **E4** — Sechs Korpus-Dubletten sind verlinkt, ein Widerspruch geklärt.
  Zusammenführen wäre ~46.000 Zeilen Redaktionsarbeit.
- **Vercel** — Falls dort ein Projekt verbunden ist, muss die *Root Directory*
  auf `frontend` stehen (im Repo-Wurzelverzeichnis gibt es keine `package.json`).
  Der Rewrite in `frontend/vercel.json` deckt **keine WebSockets** ab — die
  Live-Kollaboration (`/ws/collaborate/…`) funktioniert dort nicht.
