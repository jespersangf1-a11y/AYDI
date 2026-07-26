"""
AYDI Praxistest — Reale Szenarien, Reale Daten, Reale Ergebnisse
================================================================
Systematischer Praxistest des gesamten AYDI-Systems.
4 Personas, 6 Szenario-Gruppen, 22-Punkt-Checkliste.
"""
import json
import os
import sys
import time

# Override DB to writable location BEFORE any app imports
os.environ["DATABASE_URL"] = "sqlite+aiosqlite:////sessions/dreamy-youthful-fermi/aydi_praxis.db"

# Force config reload
import importlib
import app.core.config
importlib.reload(app.core.config)
import app.db.database
importlib.reload(app.db.database)

import asyncio
from app.db.database import engine
from app.models.models import Base

# Create tables
async def _init_db():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.drop_all)
        await conn.run_sync(Base.metadata.create_all)
asyncio.run(_init_db())

from fastapi.testclient import TestClient
from app.main import app

# Patch the app's DB dependency
from app.db import database as db_module
app.dependency_overrides = {}

client = TestClient(app)

# ============================================================
# Test infrastructure
# ============================================================
results = []
tokens = {}
project_ids = {}

def log(scenario, status, detail=""):
    r = {"scenario": scenario, "status": status, "detail": str(detail)[:300]}
    results.append(r)
    icon = "✅" if status == "PASS" else "❌" if status == "FAIL" else "⚠️"
    print(f"{icon} {scenario}: {str(detail)[:150]}")


def auth_headers(name):
    return {"Authorization": f"Bearer {tokens[name]}"}


# ============================================================
# SZENARIO-GRUPPE A: Onboarding & Account-Flows
# ============================================================
print("\n" + "="*70)
print("SZENARIO-GRUPPE A: ONBOARDING & ACCOUNT-FLOWS")
print("="*70)

# A1: Registrierung
personas = [
    {"email": "kai.segler@example.com", "password": "Segeln2024!", "full_name": "Kai Svensson", "role": "Bootseigner"},
    {"email": "sarah.werft@example.com", "password": "Werft2024!", "full_name": "Sarah Lindqvist", "role": "Werftleiterin"},
    {"email": "marc.kaeufer@example.com", "password": "Kaufen2024!", "full_name": "Marc Dupont", "role": "Käufer"},
    {"email": "elena.design@example.com", "password": "Design2024!", "full_name": "Elena Rossi", "role": "Designerin"},
]

for p in personas:
    resp = client.post("/api/v1/auth/register", json={
        "email": p["email"],
        "password": p["password"],
        "full_name": p["full_name"],
    })
    if resp.status_code == 201:
        data = resp.json()
        if "access_token" in data:
            tokens[p["full_name"].split()[0]] = data["access_token"]
            log(f"A1-Register-{p['full_name'].split()[0]}", "PASS", f"{p['role']} registriert")
        else:
            log(f"A1-Register-{p['full_name'].split()[0]}", "FAIL", f"Keine Tokens: {list(data.keys())}")
    else:
        log(f"A1-Register-{p['full_name'].split()[0]}", "FAIL", f"{resp.status_code}: {resp.text[:100]}")

# A2: Doppel-Registrierung
resp = client.post("/api/v1/auth/register", json={
    "email": "kai.segler@example.com", "password": "Anders2024!", "full_name": "Kai Anders"
})
if resp.status_code in (400, 409):
    log("A2-DuplikatReg", "PASS", f"Korrekt abgelehnt: {resp.status_code}")
else:
    log("A2-DuplikatReg", "FAIL", f"Status {resp.status_code}: {resp.text[:100]}")

# A3: Login
for p in personas:
    name = p["full_name"].split()[0]
    resp = client.post("/api/v1/auth/login", json={"email": p["email"], "password": p["password"]})
    if resp.status_code == 200 and "access_token" in resp.json():
        tokens[name] = resp.json()["access_token"]
        log(f"A3-Login-{name}", "PASS", "Login erfolgreich")
    else:
        log(f"A3-Login-{name}", "FAIL", f"{resp.status_code}: {resp.text[:100]}")

# A4: Falsches Passwort
resp = client.post("/api/v1/auth/login", json={"email": "kai.segler@example.com", "password": "Falsch!"})
if resp.status_code == 401:
    log("A4-FalschesPasswort", "PASS", "Korrekt abgelehnt")
else:
    log("A4-FalschesPasswort", "FAIL", f"Status {resp.status_code}")

# A5: Unbekannter User
resp = client.post("/api/v1/auth/login", json={"email": "nobody@ex.com", "password": "Test1234!"})
if resp.status_code == 401:
    log("A5-UnbekannterUser", "PASS", "Korrekt abgelehnt")
else:
    log("A5-UnbekannterUser", "FAIL", f"Status {resp.status_code}")

# A6: Profil abrufen
for name in tokens:
    resp = client.get("/api/v1/auth/me", headers=auth_headers(name))
    if resp.status_code == 200:
        data = resp.json()
        log(f"A6-Profil-{name}", "PASS", f"Email: {data.get('email')}, Name: {data.get('full_name')}")
    else:
        log(f"A6-Profil-{name}", "FAIL", f"Status {resp.status_code}")

# A7: Auth-Guard (geschützte Endpoints ohne Token)
protected = [
    ("GET", "/api/v1/projects"), ("GET", "/api/v1/materials"),
    ("GET", "/api/v1/competitors"), ("GET", "/api/v1/knowledge/categories"),
    ("GET", "/api/v1/community/reports"), ("GET", "/api/v1/service-reports"),
    ("GET", "/api/v1/collaborate/sessions"),
]
all_guarded = True
for method, path in protected:
    resp = client.get(path)
    if resp.status_code != 401:
        log(f"A7-Guard-{path}", "FAIL", f"Erwartet 401, got {resp.status_code}")
        all_guarded = False
if all_guarded:
    log("A7-AuthGuard", "PASS", f"Alle {len(protected)} Endpoints geschützt")

# A8: Token Refresh
resp = client.post("/api/v1/auth/login", json={"email": "kai.segler@example.com", "password": "Segeln2024!"})
if resp.status_code == 200:
    rt = resp.json().get("refresh_token")
    if rt:
        resp2 = client.post("/api/v1/auth/refresh", json={"refresh_token": rt})
        if resp2.status_code == 200 and "access_token" in resp2.json():
            log("A8-Refresh", "PASS", "Token erneuert")
        else:
            log("A8-Refresh", "FAIL", f"Refresh: {resp2.status_code}")

# A9: Schnellanalyse OHNE Login (Level 1)
quick_data = {
    "boat_name": "Hallberg-Rassy 36",
    "boat_class": "sailing_yacht_36",
    "length_m": 10.85,
    "beam_m": 3.50,
    "draft_m": 1.75,
    "year_built": 2008,
    "cabin_count": 2,
    "head_count": 1,
    "displacement_kg": 7200,
}
resp = client.post("/api/v1/quick-analysis", json=quick_data)
if resp.status_code in (200, 201):
    data = resp.json()
    log("A9-Schnellanalyse", "PASS", f"Quick Analysis ID: {data.get('id', 'N/A')}, Keys: {list(data.keys())[:6]}")
else:
    log("A9-Schnellanalyse", "FAIL", f"{resp.status_code}: {resp.text[:150]}")

# A10: Projekt erstellen (Sarah — Werftleiterin)
if "Sarah" in tokens:
    resp = client.post("/api/v1/projects",
        headers=auth_headers("Sarah"),
        json={"name": "HR36 Refitting 2024", "boat_class": "sailing_yacht_36",
              "description": "Hallberg-Rassy 36, BJ 2008, Komplett-Refitting"}
    )
    if resp.status_code in (200, 201):
        project = resp.json()
        project_ids["sarah_hr36"] = project["id"]
        log("A10-Projekt-Sarah", "PASS", f"Projekt: {project['id'][:12]}...")
    else:
        log("A10-Projekt-Sarah", "FAIL", f"{resp.status_code}: {resp.text[:150]}")

# Kai erstellt auch ein Projekt
if "Kai" in tokens:
    resp = client.post("/api/v1/projects",
        headers=auth_headers("Kai"),
        json={"name": "Bavaria 40 Analyse", "boat_class": "sailing_yacht_40",
              "description": "Bavaria 40 Cruiser, BJ 2015, Zustandsprüfung vor Langfahrt"}
    )
    if resp.status_code in (200, 201):
        project = resp.json()
        project_ids["kai_bav40"] = project["id"]
        log("A10-Projekt-Kai", "PASS", f"Projekt: {project['id'][:12]}...")
    else:
        log("A10-Projekt-Kai", "FAIL", f"{resp.status_code}: {resp.text[:150]}")

# A11: User-Isolation (Kai sieht Sarahs Projekte nicht)
if "Kai" in tokens:
    resp = client.get("/api/v1/projects", headers=auth_headers("Kai"))
    if resp.status_code == 200:
        kai_projects = resp.json()
        kai_names = [p["name"] for p in kai_projects]
        if "HR36 Refitting 2024" not in kai_names and len(kai_projects) >= 1:
            log("A11-UserIsolation", "PASS", f"Kai sieht nur eigene Projekte: {kai_names}")
        elif "HR36 Refitting 2024" in kai_names:
            log("A11-UserIsolation", "FAIL", "Kai sieht Sarahs Projekt!")
        else:
            log("A11-UserIsolation", "PASS", f"Kai Projekte: {kai_names}")


# ============================================================
# Summary Gruppe A
# ============================================================
print("\n" + "-"*50)
a_pass = sum(1 for r in results if r["status"] == "PASS")
a_fail = sum(1 for r in results if r["status"] == "FAIL")
print(f"GRUPPE A ERGEBNIS: {a_pass} PASS, {a_fail} FAIL von {len(results)}")
print("-"*50)

# Save state for subsequent groups
with open("/sessions/dreamy-youthful-fermi/praxis_state.json", "w") as f:
    json.dump({"tokens": tokens, "project_ids": project_ids, "results": results}, f, indent=2)
print(f"\nState saved. Tokens: {list(tokens.keys())}, Projects: {list(project_ids.keys())}")
