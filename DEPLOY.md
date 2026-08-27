# AYDI Deployment — Kostenloser Production-Stack

Drei kostenlose Dienste decken AYDI vollständig ab:

| Schicht | Dienst | Free-Limit | Notiz |
|---|---|---|---|
| Frontend | **Vercel** *oder* **Cloudflare Pages** | unbegrenzte Builds + Bandwidth | Vite-Build, statisches Hosting |
| Backend | **Render** Free Web Service | 750 h/Monat (24/7 möglich), Cold-Start nach 15 Min Idle | Docker-Build, Frankfurt-Region |
| Datenbank | **Neon** Postgres | 0.5 GB Storage, kein Zeitlimit | asyncpg-kompatibel, gut für SQLAlchemy |

Gesamt: 0 €/Monat. Cold-Start ist der einzige spürbare Trade-off — die erste Request nach 15 Min Pause braucht ~30 Sek bis das Container hochfährt.

---

## Schritt 1 — Neon (Datenbank zuerst, der Rest hängt dran)

1. https://neon.tech → Sign up (GitHub oder Google reicht)
2. New Project → Name `aydi`, Region `Frankfurt (eu-central-1)`, Postgres 16
3. Im Dashboard auf das Projekt klicken → **Connection Details**
4. **Wichtig:** wähle `Connection string` und schalte auf den **Pooled connection**
5. Kopier den String, ersetz das Schema in der URL:
   ```
   postgres://user:pass@ep-xxx.eu-central-1.aws.neon.tech/aydi
   ```
   wird zu
   ```
   postgresql+asyncpg://user:pass@ep-xxx.eu-central-1.aws.neon.tech/aydi?ssl=require
   ```
   (Schema `postgres://` → `postgresql+asyncpg://`, `?ssl=require` anhängen.)

6. Diesen Connection-String später in Render als `DATABASE_URL` setzen.

---

## Schritt 2 — Render (Backend)

1. https://render.com → Sign up (GitHub-Login empfehlenswert, dann sieht Render dein AYDI-Repo)
2. New → **Blueprint** → AYDI-Repo auswählen
3. Render liest `render.yaml` und schlägt `aydi-backend` als Web Service vor → bestätigen
4. Im Service-Detail unter **Environment** diese drei Secrets setzen. Alles
   Übrige steht bereits in `render.yaml` und wird von Render übernommen —
   auch `CORS_ORIGINS` und `TRUST_PROXY_HEADERS`.

   | Key | Wert |
   |---|---|
   | `DATABASE_URL` | der Neon-String von oben (mit `+asyncpg` und `?ssl=require`) |
   | `ANTHROPIC_API_KEY` | dein Claude-API-Key — ohne ihn läuft Pipeline B (Bildanalyse) nicht, alles Übrige schon |
   | `SECRET_KEY` | `python -c "import secrets; print(secrets.token_urlsafe(64))"` |

   `SECRET_KEY` ist Pflicht: mit `ENVIRONMENT=production` und dem
   Repo-Default bricht der Boot-Guard in `app/core/config.py` den Start ab.
   Das ist Absicht — lieber ein fehlgeschlagenes Deployment als eines mit
   fälschbaren Tokens.

5. Manual Deploy → Render baut den Docker-Container und startet ihn.
6. Erfolgs-Check: in den Logs erscheint
   ```
   [entrypoint] Running alembic upgrade head...
   INFO  [alembic.runtime.migration] Running upgrade  -> 000_initial, ...
   ... 9 Revisionen, zuletzt 007_image_analysis_status -> 008_merge_owner_and_utc
   [entrypoint] Starting uvicorn on 0.0.0.0:10000...
   AYDI starting up (json_logs=True)
   Knowledge corpus warmed: 260 documents
   ```
   Die letzte Zeile ist die wichtige: der Korpus wird **vor** dem ersten
   Request geparst, der Dienst nimmt bis dahin nichts an. Rechne beim ersten
   Deploy mit ein bis zwei Minuten, bis `/health/ready` antwortet — Render
   markiert den Deploy erst danach als erfolgreich.

7. Backend-URL notieren. Render vergibt `https://aydi-backend.onrender.com`,
   **hängt aber eine Kennung an, wenn der Name schon vergeben ist.** Weicht sie
   ab, muss sie an zwei Stellen nachgetragen werden:
   `vercel.json` im Repo-Wurzelverzeichnis (Rewrite-Ziel für `/api/*`) und
   `frontend/public/_redirects` (Cloudflare-Pages-Variante).

---

## Schritt 3 — Vercel (Frontend)

Es ist **keine Einstellung im Dashboard nötig.** `vercel.json` liegt im
Repo-Wurzelverzeichnis und bringt Install-, Build- und Output-Pfad mit; ein
Import des Repos baut damit von selbst richtig.

**Warum nicht unter `frontend/`:** Vercel liest `vercel.json` ausschließlich
aus dem konfigurierten *Root Directory*. Stand das auf dem Vorgabewert
(Repo-Wurzel), wurde `frontend/vercel.json` nie gelesen — dort gab es weder
`package.json` noch Konfiguration, der Build lief in einer Sekunde durch,
erzeugte nichts, und **jeder** Pfad antwortete mit `404: NOT_FOUND`. Genau so
lief dieses Projekt von April bis August. Erkennungsmerkmal im Build-Log:

```
Running "vercel build"
Build Completed in /vercel/output [1s]
Skipping cache upload because no files were prepared
```

Kein `npm ci`, kein `vite build`, keine Dateien. Ein korrekter Build zeigt
stattdessen `npm ci`, `vite build` und `dist/index.html`.

1. Projekt mit dem Repo verbinden (bei `aydi` bereits geschehen)
2. **Root Directory unverändert lassen** — also Repo-Wurzel
3. Deploy; Build-Command und Output-Dir kommen aus `vercel.json`
4. Optional: Custom Domain unter Settings → Domains

Es gibt genau **eine** `vercel.json`. Wer lieber mit `Root Directory =
frontend` arbeitet, verschiebt sie nach `frontend/` und nimmt die
`cd frontend &&`-Präfixe wieder heraus — beides gleichzeitig ergäbe zwei
Wahrheiten über das Rewrite-Ziel.

**Alternative — Cloudflare Pages:**
- https://dash.cloudflare.com → Pages → Create application → AYDI-Repo
- Build-Command: `cd frontend && npm ci && npm run build`
- Output-Directory: `frontend/dist`
- `frontend/public/_redirects` wird automatisch übernommen
- Vorteil: unbegrenzte Bandwidth statt 100 GB/Monat bei Vercel

---

## Schritt 4 — Erste Verifikation

```bash
# Backend-Health-Check
curl https://aydi-backend.onrender.com/health/ready
# {"status":"ready","db":"ok"}

# Frontend lädt
curl -I https://<dein-frontend>.vercel.app
# HTTP/2 200
```

Wenn beide stehen, ist AYDI online. Erst-Login: `/auth/register` über die UI.

---

## Was du im Hinterkopf behalten musst

- **Render-Free schläft.** Nach 15 Min ohne Traffic geht der Container schlafen. Der Aufwachvorgang ist mehr als nur Containerstart: `alembic upgrade head` läuft durch, danach parst der Lifespan den 260-Dokumente-Korpus, bevor der erste Request angenommen wird (lokal 3 s, auf Renders geteilter CPU deutlich mehr). Rechne mit 30–60 Sek. Für Demo/Beta ok, für Produktionskunden nicht.
- **Hochgeladene Bilder überleben keinen Neustart.** Der Free-Plan hat keine persistente Platte; `UPLOAD_DIR` liegt im Container. Nach Neustart oder Deploy zeigen die `image_uploads`-Zeilen auf Dateien, die es nicht mehr gibt. Für echten Betrieb braucht es eine Render-Disk oder Objektspeicher.
- **`/docs` ist zu.** Mit `ENVIRONMENT=production` liefern `/docs`, `/redoc` und `/openapi.json` bewusst 404 — die interaktive Doku listet jede Route und jede Prüfregel. Zum Nachsehen vorübergehend `DOCS_ENABLED=true` setzen.
- **`TRUST_PROXY_HEADERS=true` gehört zu Render, nicht in jede Umgebung.** Der Schalter steht im Blueprint, weil hinter Render ein vertrauenswürdiger Proxy sitzt und `X-Forwarded-For` sonst die tatsächliche Absenderadresse verdeckt — Ratenbegrenzung und Anmeldesperre würden dann für alle Besucher gemeinsam zählen. Läuft das Backend je direkt aus dem Netz erreichbar, muss der Schalter wieder aus, sonst ist die Kopfzeile fälschbar.
- **Neon-Free pausiert.** Nach längerer Inaktivität (Tagen) pausiert die Datenbank, wacht aber innerhalb von Sekunden bei der ersten Query wieder auf.
- **Migrationen laufen bei jedem Deploy.** Wenn du eine Alembic-Migration schreibst und pushst, läuft sie automatisch im Render-Entrypoint. Schreib sie idempotent.
- **Skalierung kostet:** sobald du dauerhaft mehr brauchst — Render Starter $7/Monat (kein Sleep), Neon Pro $19/Monat (10 GB), Vercel Pro $20/Monat. In dieser Reihenfolge upgraden, wenn die Limits beißen.
