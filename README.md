# AYDI — AI Yacht Design Intelligence

Domänenspezifische Analyseplattform für Yacht- und Bootsdesign. Sie bewertet ein Boot
über drei Eingabemodalitäten — strukturierte Daten (CAD, Specs), Bilder und Freitext
(Serviceberichte) — entlang zehn Systemdomänen und dreizehn Bootsklassen.

**Leitprinzip:** Jedes Ergebnis trägt eine Konfidenzangabe. Wo die Datenlage nicht
reicht, sagt das System „nicht beurteilbar" statt zu raten.

Die inhaltliche und architektonische Referenz ist **[CLAUDE.md](CLAUDE.md)** — dieses
README beschreibt nur, wie du das Projekt zum Laufen bringst.

---

## Schnellstart

Voraussetzungen: **Python 3.12+** (Zielversion 3.12, verifiziert auch unter 3.14),
**Node 20+** (verifiziert unter Node 24 / npm 11). Optional Docker für den Postgres-Weg.

### Backend

```bash
cd backend
pip install -r requirements.txt        # enthält pytest, keine separate requirements-dev.txt
PYTHONPATH=. alembic upgrade head      # 7 Revisionen: 000_initial_schema → 006_analysis_run
PYTHONPATH=. uvicorn app.main:app --reload
```

Läuft auf <http://localhost:8000>, OpenAPI unter `/docs`.

> **`PYTHONPATH=.` ist bei allen Backend-Kommandos nötig** — es gibt kein installiertes
> Package. Ohne gesetzte `DATABASE_URL` landet alles in `backend/aydi.db` (SQLite).

Der erste Start dauert rund 25 Sekunden: Der Wissenskorpus (260 Dokumente, ~848.000
Zeilen) wird vor dem ersten Request in einem Thread vorgewärmt, damit die erste
Anfrage nicht den Event-Loop blockiert.

### Frontend

```bash
cd frontend
npm install
npm run dev        # Vite auf :5173, proxyt /api und /health nach :8000
```

`npm run build` führt `tsc && vite build` aus — der Typcheck ist Teil des Builds.

### Konfiguration

Alle 18 Einstellungen sind in **[.env.example](.env.example)** dokumentiert. Ohne `.env`
startet die App mit sinnvollen Entwicklungs-Defaults. `app/core/config.py` liest `.env`
**relativ zum Arbeitsverzeichnis**.

---

## Tests

```bash
cd backend
PYTHONPATH=. python -m pytest tests/ -q     # 1.666 Tests, ~28 s
```

`pyproject.toml` setzt `asyncio_mode = "auto"` — `@pytest.mark.asyncio` ist nicht nötig.

### Praxistest (End-to-End über HTTP)

```bash
cd backend
PYTHONPATH=. python praxistest_full.py      # 4 Personas, Gruppen A–F, 123 Checks
```

Legt DB und Ergebnisse unter `backend/.praxistest/` ab (per `PRAXISTEST_OUT_DIR`
umlenkbar) und setzt `DATABASE_URL` selbst — die Entwicklungs-DB bleibt unangetastet.

---

## Docker (Postgres statt SQLite)

```bash
cp .env.example .env
docker compose up -d
docker compose exec backend alembic upgrade head   # im Dev-Compose bewusst manuell
```

Das Produktions-Image migriert selbst: `docker/entrypoint.sh` führt `alembic upgrade head`
vor uvicorn aus und bricht bei Migrationsfehlern ab (`set -e`) — es fließt nie Traffic
gegen ein unbekanntes Schema.

---

## Vor dem Deployment

Die App **verweigert den Start**, wenn `ENVIRONMENT=production` gesetzt ist und
`SECRET_KEY` noch der Default oder `COOKIE_SECURE` nicht gesetzt ist. Das ist Absicht:
lieber ein fehlgeschlagenes Deployment als eines mit fälschbaren Tokens.

Checkliste:

- [ ] `SECRET_KEY` — eigener Zufallswert (`python -c "import secrets; print(secrets.token_urlsafe(64))"`)
- [ ] `COOKIE_SECURE=true`
- [ ] `ENVIRONMENT=production` (macht den Boot-Guard scharf — in `render.yaml` bereits gesetzt)
- [ ] `DATABASE_URL` auf Postgres
- [ ] `CORS_ORIGINS` auf die echte Frontend-Domain (mit Cookie-Auth **nie** `["*"]`)
- [ ] `UPLOAD_DIR` auf ein persistentes Volume (sonst sind Bilder nach Neustart weg)
- [ ] `ANTHROPIC_API_KEY` gesetzt, falls die Bildanalyse genutzt wird

Details: [DEPLOY.md](DEPLOY.md), [render.yaml](render.yaml), [railway.toml](railway.toml).

---

## Aufbau

```
backend/
  app/
    api/routes/        19 Routenmodule (FastAPI)
    core/              Auth, Rechte, Tarife, Validierung, i18n, Middleware
    services/
      analysis/        12 Analysemodule + Orchestrator
      visual/          Pipeline B (Claude Vision) mit Prompts und Konfidenz-Wächter
      knowledge/       260 Markdown-Wissensdokumente + Loader/Retrieval
      cad_import/, dxf/, community/, inference/, reports/, diff/
  migrations/          Alembic (7 Revisionen)
  tests/               1.666 Tests
frontend/src/
  components/, services/, pages/, types/
```

---

## Mitarbeiten

- **Deutsch** für alle nutzersichtbaren Texte, **Englisch** für Bezeichner.
- Pydantic v2: `model_config = {...}`, **nie** `class Config`.
- Analysemodule sind reine Funktionen ohne DB-Zugriff.
- Jede Warnung braucht einen Handlungsvorschlag, jedes Ergebnis eine Konfidenzangabe —
  beides ist durch Tests abgesichert (`tests/test_warning_conventions.py`).
- Koordinaten in mm, Scores 0–100, Beträge in EUR.

Vor dem Commit: Testsuite und `npm run build` grün, und bei Änderungen an Verhalten,
das in CLAUDE.md beschrieben ist, die Spezifikation mitziehen —
`tests/test_claude_md_spec_matches_code.py` prüft das.
