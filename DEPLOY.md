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
4. Im Service-Detail unter **Environment** diese vier Secrets setzen:

   | Key | Wert |
   |---|---|
   | `DATABASE_URL` | der Neon-String von oben (mit `+asyncpg` und `?ssl=require`) |
   | `ANTHROPIC_API_KEY` | dein Claude-API-Key |
   | `SECRET_KEY` | `python -c "import secrets; print(secrets.token_urlsafe(64))"` |
   | `CORS_ORIGINS` | `["https://<dein-frontend>.vercel.app"]` (anpassen, wenn die URL steht) |

5. Manual Deploy → Render baut den Docker-Container und startet ihn.
6. Erfolgs-Check: in den Logs erscheint
   ```
   [entrypoint] Running alembic upgrade head...
   INFO  [alembic.runtime.migration] Running upgrade  -> 000_initial, ...
   INFO  [alembic.runtime.migration] Running upgrade 000_initial -> 001_user_prefs, ...
   [entrypoint] Starting uvicorn on 0.0.0.0:10000...
   ```
7. Backend-URL ist jetzt z. B. `https://aydi-backend.onrender.com` → in `vercel.json` und `frontend/public/_redirects` eintragen, falls die URL anders heißt (Standard ist passend gewählt).

---

## Schritt 3 — Vercel (Frontend)

1. https://vercel.com → Sign up mit GitHub
2. Add New → Project → AYDI-Repo importieren
3. **Root Directory** auf `frontend` setzen
4. Build-Command, Output-Dir und Install-Command werden aus `vercel.json` gezogen — nichts ändern
5. Deploy → ~30 Sek später läuft das Frontend
6. Optional: Custom Domain unter Settings → Domains

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

- **Render-Free schläft.** Nach 15 Min ohne Traffic geht der Container schlafen. Erste Request danach: ~30 Sek Cold-Start. Für Demo/Beta ok, für Produktionskunden nicht.
- **Neon-Free pausiert.** Nach längerer Inaktivität (Tagen) pausiert die Datenbank, wacht aber innerhalb von Sekunden bei der ersten Query wieder auf.
- **Migrationen laufen bei jedem Deploy.** Wenn du eine Alembic-Migration schreibst und pushst, läuft sie automatisch im Render-Entrypoint. Schreib sie idempotent.
- **Skalierung kostet:** sobald du dauerhaft mehr brauchst — Render Starter $7/Monat (kein Sleep), Neon Pro $19/Monat (10 GB), Vercel Pro $20/Monat. In dieser Reihenfolge upgraden, wenn die Limits beißen.
