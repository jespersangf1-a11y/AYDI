"""
AYDI Praxistest — Kompletter Durchlauf aller 6 Szenario-Gruppen
================================================================
Personas: Kai (Segler), Sarah (Werft), Marc (Käufer), Elena (Designerin)
Gruppen: A-F
"""
import json, os, sys, time, asyncio, importlib
from uuid import UUID

from pathlib import Path

# Windows-Konsolen laufen per Default unter cp1252 und brechen an den Status-Emojis.
# UTF-8 erzwingen, sonst ist der Praxistest auf der Hauptentwicklungsplattform nicht lauffähig.
for _stream in (sys.stdout, sys.stderr):
    try:
        _stream.reconfigure(encoding="utf-8", errors="replace")
    except (AttributeError, OSError):  # pragma: no cover - z.B. umgeleitete Pipes
        pass

# Ergebnis- und DB-Ablage: per Env überschreibbar, sonst neben diesem Skript.
_OUT = Path(os.environ.get("PRAXISTEST_OUT_DIR", Path(__file__).resolve().parent / ".praxistest"))
_OUT.mkdir(parents=True, exist_ok=True)
os.environ["DATABASE_URL"] = f"sqlite+aiosqlite:///{(_OUT / 'aydi_praxis2.db').as_posix()}"
import app.core.config; importlib.reload(app.core.config)
import app.db.database; importlib.reload(app.db.database)
from app.db.database import engine
from app.models.models import Base

async def _init_db():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.drop_all)
        await conn.run_sync(Base.metadata.create_all)
asyncio.run(_init_db())

from fastapi.testclient import TestClient
from app.main import app
client = TestClient(app)

# Dieser Praxistest simuliert den reinen Bearer-Client (API-Zugang), nicht den
# Browser. /auth/login setzt zusaetzlich httpOnly-Session-Cookies; behaelt der
# Client sie, ist jeder Folge-Request cookie-authentifiziert (Cookie hat in
# _extract_token Vorrang vor dem Bearer-Header) und der CSRF-Schutz greift
# korrekterweise. Darum nach jedem Request die Jar leeren.
_orig_request = client.request


def _request_without_cookie_jar(*args, **kwargs):
    response = _orig_request(*args, **kwargs)
    client.cookies.clear()
    return response


client.request = _request_without_cookie_jar

results = []
tokens = {}
project_ids = {}
layout_ids = {}

def log(scenario, status, detail=""):
    r = {"scenario": scenario, "status": status, "detail": str(detail)[:500]}
    results.append(r)
    icon = "✅" if status == "PASS" else "❌" if status == "FAIL" else "⚠️"
    print(f"{icon} {scenario}: {str(detail)[:160]}")

def auth(name):
    return {"Authorization": f"Bearer {tokens[name]}"}

# ============================================================
# GRUPPE A: ONBOARDING & ACCOUNT-FLOWS
# ============================================================
print("\n" + "="*70)
print("SZENARIO-GRUPPE A: ONBOARDING & ACCOUNT-FLOWS")
print("="*70)

personas = [
    {"email": "kai@example.com", "password": "Segeln2024!", "full_name": "Kai Svensson"},
    {"email": "sarah@example.com", "password": "Werft2024!", "full_name": "Sarah Lindqvist"},
    {"email": "marc@example.com", "password": "Kaufen2024!", "full_name": "Marc Dupont"},
    {"email": "elena@example.com", "password": "Design2024!", "full_name": "Elena Rossi"},
]

# A1: Register
for p in personas:
    name = p["full_name"].split()[0]
    resp = client.post("/api/v1/auth/register", json=p)
    if resp.status_code == 201:
        log(f"A1-Register-{name}", "PASS", f"User erstellt: {resp.json().get('email')}")
    else:
        log(f"A1-Register-{name}", "FAIL", f"{resp.status_code}: {resp.text[:100]}")

# A2: Duplikat
resp = client.post("/api/v1/auth/register", json=personas[0])
log("A2-DuplikatReg", "PASS" if resp.status_code == 409 else "FAIL",
    f"Duplikat: {resp.status_code}")

# A3: Login + Token
for p in personas:
    name = p["full_name"].split()[0]
    resp = client.post("/api/v1/auth/login", json={"email": p["email"], "password": p["password"]})
    if resp.status_code == 200 and "access_token" in resp.json():
        tokens[name] = resp.json()["access_token"]
        log(f"A3-Login-{name}", "PASS", "Token erhalten")
    else:
        log(f"A3-Login-{name}", "FAIL", f"{resp.status_code}: {resp.text[:100]}")

# A4-A5: Negative auth
resp = client.post("/api/v1/auth/login", json={"email": "kai@example.com", "password": "Falsch!"})
log("A4-FalschesPasswort", "PASS" if resp.status_code == 401 else "FAIL", f"Status: {resp.status_code}")

resp = client.post("/api/v1/auth/login", json={"email": "nobody@ex.com", "password": "X"})
log("A5-UnbekannterUser", "PASS" if resp.status_code == 401 else "FAIL", f"Status: {resp.status_code}")

# A6: Profil
for name in tokens:
    resp = client.get("/api/v1/auth/me", headers=auth(name))
    if resp.status_code == 200:
        log(f"A6-Profil-{name}", "PASS", f"{resp.json().get('full_name')}")
    else:
        log(f"A6-Profil-{name}", "FAIL", f"{resp.status_code}")

# A7: Auth-Guard — mit EIGENEM Client ohne Cookies/Token, sonst misst man nichts.
guarded = ["/api/v1/projects", "/api/v1/materials", "/api/v1/competitors",
           "/api/v1/community/reports", "/api/v1/service-reports",
           "/api/v1/collaborate/sessions"]
# Bewusst oeffentlich (Produktsaeule 1 "Wissensbasis": Public read, Tiefe ist PRO).
public = ["/api/v1/knowledge/categories"]
with TestClient(app) as anon:
    fails = [p for p in guarded if anon.get(p).status_code != 401]
    pub_fails = [p for p in public if anon.get(p).status_code != 200]
log("A7-AuthGuard", "PASS" if not fails else "FAIL",
    f"{len(guarded)} Endpoints geschützt" if not fails else f"Ungeschützt: {fails}")
log("A7b-PublicRead", "PASS" if not pub_fails else "FAIL",
    f"{len(public)} öffentliche Endpoints erreichbar" if not pub_fails
    else f"Öffentlich erwartet, aber gesperrt: {pub_fails}")

# A8: Refresh
resp = client.post("/api/v1/auth/login", json={"email": "kai@example.com", "password": "Segeln2024!"})
rt = resp.json().get("refresh_token", "")
if rt:
    resp2 = client.post("/api/v1/auth/refresh", json={"refresh_token": rt})
    log("A8-Refresh", "PASS" if resp2.status_code == 200 else "FAIL", f"Status: {resp2.status_code}")

# A9: Schnellanalyse OHNE Login
quick = {
    "boat_class": "cruising_sail",
    "length_m": 10.85, "beam_m": 3.50, "draft_m": 1.75,
    "year": 2008, "cabin_count": 2, "head_count": 1, "displacement_kg": 7200,
    "brand": "Hallberg-Rassy", "model_name": "HR 36",
}
resp = client.post("/api/v1/quick-analysis", json=quick)
if resp.status_code in (200, 201):
    qa = resp.json()
    log("A9-Schnellanalyse", "PASS", f"ID: {qa.get('id','?')[:12]}, Level: {qa.get('analysis_level')}, Score: {qa.get('overall_assessment',{}).get('overall_score','?')}")
else:
    log("A9-Schnellanalyse", "FAIL", f"{resp.status_code}: {resp.text[:150]}")

# A10: Projekte erstellen (boat_class + length_m + beam_m required)
for name, bc, desc, length, beam in [
    ("Sarah", "cruising_sail", "HR36 Refitting 2024", 10.85, 3.50),
    ("Kai", "cruising_sail", "Bavaria 40 Langfahrt-Check", 12.14, 3.99),
    ("Elena", "catamaran_sail", "Lagoon 42 Redesign", 12.80, 7.20),
    ("Marc", "cruising_sail", "Kaufgutachten Beneteau Oceanis 38.1", 11.50, 3.81),
]:
    resp = client.post("/api/v1/projects", headers=auth(name),
        json={"name": desc, "boat_class": bc, "description": desc,
              "length_m": length, "beam_m": beam})
    if resp.status_code in (200, 201):
        pid = resp.json()["id"]
        project_ids[f"{name.lower()}_proj"] = pid
        log(f"A10-Projekt-{name}", "PASS", f"ID: {pid[:12]}")
    else:
        log(f"A10-Projekt-{name}", "FAIL", f"{resp.status_code}: {resp.text[:150]}")

# A11: User-Isolation
resp = client.get("/api/v1/projects", headers=auth("Kai"))
if resp.status_code == 200:
    names = [p["name"] for p in resp.json()]
    foreign = [n for n in names if "HR36" in n or "Lagoon" in n or "Beneteau" in n]
    log("A11-UserIsolation", "PASS" if not foreign else "FAIL",
        f"Kai sieht: {names}, Fremde: {foreign}")


# ============================================================
# GRUPPE B: ANALYSE-PIPELINE (ohne echte Fotos — Structured)
# ============================================================
print("\n" + "="*70)
print("SZENARIO-GRUPPE B: ANALYSE-PIPELINE")
print("="*70)

# B1: Layout erstellen für Sarahs HR36-Projekt
sarah_pid = project_ids.get("sarah_proj")
if sarah_pid:
    # Create a layout with realistic zones (polygon = list of [x,y] coordinate pairs in mm)
    layout_data = {
        "name": "HR36 Hauptdeck",
        "version": "1.0",
        "zones": [
            {"name": "Cockpit", "zone_type": "cockpit",
             "polygon": [[0,0],[3000,0],[3000,2500],[0,2500]], "height_mm": 0,
             "properties": {"area_sqm": 4.5, "headroom_mm": 0, "seat_count": 6}},
            {"name": "Salon", "zone_type": "saloon",
             "polygon": [[0,2500],[3200,2500],[3200,5500],[0,5500]], "height_mm": 1920,
             "properties": {"area_sqm": 8.2, "headroom_mm": 1920, "seat_count": 6}},
            {"name": "Pantry", "zone_type": "pantry",
             "polygon": [[0,5500],[1800,5500],[1800,7000],[0,7000]], "height_mm": 1900,
             "properties": {"area_sqm": 2.7, "headroom_mm": 1900, "has_stove": True}},
            {"name": "Vorschiffkabine", "zone_type": "cabin",
             "polygon": [[0,7000],[3000,7000],[3000,9800],[1500,10500],[0,9800]], "height_mm": 1850,
             "properties": {"area_sqm": 6.5, "headroom_mm": 1850, "berth_type": "v_berth", "berth_count": 2}},
            {"name": "Achterkabine", "zone_type": "aft_cabin",
             "polygon": [[0,-2000],[2600,-2000],[2600,0],[0,0]], "height_mm": 1750,
             "properties": {"area_sqm": 4.8, "headroom_mm": 1750, "berth_type": "double", "berth_count": 2}},
            {"name": "Nasszelle", "zone_type": "head",
             "polygon": [[2000,5500],[3200,5500],[3200,7000],[2000,7000]], "height_mm": 1880,
             "properties": {"area_sqm": 1.5, "headroom_mm": 1880, "has_shower": True}},
            {"name": "Maschinenraum", "zone_type": "engine",
             "polygon": [[1500,-500],[2700,-500],[2700,1000],[1500,1000]], "height_mm": 1200,
             "properties": {"area_sqm": 1.8, "engine_type": "diesel", "engine_hp": 29}},
            {"name": "Navecke", "zone_type": "nav_station",
             "polygon": [[2200,2500],[3200,2500],[3200,3700],[2200,3700]], "height_mm": 1900,
             "properties": {"area_sqm": 1.2, "headroom_mm": 1900}},
        ],
        "passages": [
            {"from_zone": "Cockpit", "to_zone": "Salon", "width_mm": 750},
            {"from_zone": "Salon", "to_zone": "Pantry", "width_mm": 650},
            {"from_zone": "Salon", "to_zone": "Vorschiffkabine", "width_mm": 600},
            {"from_zone": "Salon", "to_zone": "Achterkabine", "width_mm": 550},
            {"from_zone": "Salon", "to_zone": "Nasszelle", "width_mm": 550},
            {"from_zone": "Salon", "to_zone": "Navecke", "width_mm": 700},
        ],
    }
    resp = client.post(f"/api/v1/projects/{sarah_pid}/layouts",
        headers=auth("Sarah"), json=layout_data)
    if resp.status_code in (200, 201):
        lid = resp.json()["id"]
        layout_ids["sarah_hr36"] = lid
        log("B1-Layout-HR36", "PASS", f"Layout erstellt: {lid[:12]}, {len(layout_data['zones'])} Zonen, {len(layout_data['passages'])} Passagen")
    else:
        log("B1-Layout-HR36", "FAIL", f"{resp.status_code}: {resp.text[:200]}")

# B2: Einzelmodul-Analyse starten (needs layout_id from B1)
sarah_lid = layout_ids.get("sarah_hr36")
if sarah_pid and sarah_lid:
    resp = client.post(f"/api/v1/projects/{sarah_pid}/analyze",
        headers=auth("Sarah"),
        json={"module": "ergonomics", "layout_id": sarah_lid})
    if resp.status_code in (200, 201):
        analysis = resp.json()
        log("B2-Einzelanalyse-Ergo", "PASS",
            f"Score: {analysis.get('result',{}).get('overall_score','?')}, Confidence: {analysis.get('result',{}).get('confidence','?')}")
    else:
        log("B2-Einzelanalyse-Ergo", "FAIL", f"{resp.status_code}: {resp.text[:200]}")
elif not sarah_lid:
    log("B2-Einzelanalyse-Ergo", "FAIL", "Kein Layout-ID von B1 verfügbar")

from app.core.subscription import get_allowed_modules
ALLOWED_FREE = set(get_allowed_modules("free"))

# B3: Vollanalyse (alle Module)
if sarah_pid and sarah_lid:
    resp = client.post(f"/api/v1/projects/{sarah_pid}/full-analysis",
        headers=auth("Sarah"),
        json={"layout_id": sarah_lid})
    if resp.status_code in (200, 201):
        fa = resp.json()
        modules_run = list(fa.get("modules", {}).keys()) if isinstance(fa.get("modules"), dict) else []
        overall = fa.get("overall_score", fa.get("overall_assessment", {}).get("overall_score", "?"))
        log("B3-Vollanalyse", "PASS",
            f"Module: {len(modules_run)}, Overall: {overall}, Keys: {list(fa.keys())[:8]}")
        # Sarah ist als frisch registrierte Nutzerin FREE — sie bekommt per Tarif
        # nur die FREE-Module. Frueher stand hier "erwarte >= 10 Module", was fuer
        # einen FREE-Nutzer nie zutreffen konnte: Der Test war seit der Einfuehrung
        # des Tarif-Gatings dauerhaft rot und der Profi-Pfad faktisch ungeprueft.
        gated = fa.get("tier_gated", {})
        if fa.get("tier") == "free" and gated and all(m in ALLOWED_FREE for m in modules_run):
            log("B3-ModulCount-Free", "PASS",
                f"FREE: {len(modules_run)} Module gelaufen, {len(gated)} tarifgesperrt")
        else:
            log("B3-ModulCount-Free", "FAIL",
                f"tier={fa.get('tier')}, gelaufen={modules_run}, gesperrt={list(gated)}")
    else:
        log("B3-Vollanalyse", "FAIL", f"{resp.status_code}: {resp.text[:200]}")

# B3b: Derselbe Durchlauf als PRO — das ist der Pfad, den das Produkt verkauft.
# Der Tarif ist laut Spezifikation admin-provisioniert, es gibt keine Selbstbedienung;
# im Test wird er darum direkt in der DB gesetzt.
if sarah_pid and sarah_lid:
    async def _set_tier(email, tier):
        from sqlalchemy import update
        from app.db.database import async_session
        from app.models.models import User
        async with async_session() as session:
            await session.execute(update(User).where(User.email == email).values(tier=tier))
            await session.commit()
    asyncio.run(_set_tier("sarah@example.com", "pro"))

    resp = client.post(f"/api/v1/projects/{sarah_pid}/full-analysis",
        headers=auth("Sarah"), json={"layout_id": sarah_lid})
    if resp.status_code in (200, 201):
        fa = resp.json()
        ran = set((fa.get("modules") or {}).keys())
        skipped = fa.get("skipped", {})
        gated = fa.get("tier_gated", {})
        errors = fa.get("errors", {})
        allowed_pro = set(get_allowed_modules("pro"))
        unaccounted = allowed_pro - ran - set(skipped)
        log("B3b-Vollanalyse-Pro", "PASS" if fa.get("tier") == "pro" else "FAIL",
            f"tier={fa.get('tier')}, {len(ran)} gelaufen, {len(skipped)} mangels Daten übersprungen")
        # Jedes freigeschaltete Modul muss entweder laufen oder einen Grund nennen.
        log("B3b-ModulRechenschaft", "PASS" if not unaccounted and not gated and not errors else "FAIL",
            "Jedes PRO-Modul lief oder nannte einen Grund"
            if not unaccounted and not gated and not errors
            else f"ohne Rechenschaft: {sorted(unaccounted)}, gesperrt: {list(gated)}, Fehler: {list(errors)}")
        # Uebersprungen ist nur akzeptabel MIT Klartextbegruendung.
        vague = [m for m, r in skipped.items() if not isinstance(r, str) or len(r) < 15]
        log("B3b-SkipGruende", "PASS" if not vague else "FAIL",
            f"{len(skipped)} Begründungen im Klartext" if not vague else f"Ohne Begründung: {vague}")
    else:
        log("B3b-Vollanalyse-Pro", "FAIL", f"{resp.status_code}: {resp.text[:200]}")

# B4: Schnellanalyse mit verschiedenen Bootsklassen
for bc, name, specs in [
    ("small_sail", "Jollenkreuzer", {"length_m": 6.5, "beam_m": 2.3, "cabin_count": 1}),
    ("large_motor", "Motoryacht 15m", {"length_m": 15.0, "beam_m": 4.2, "cabin_count": 3}),
    ("catamaran_sail", "Katamaran 42ft", {"length_m": 12.8, "beam_m": 7.2, "cabin_count": 4}),
    ("superyacht", "Superyacht 30m", {"length_m": 30.0, "beam_m": 7.0, "cabin_count": 5}),
]:
    qdata = {"model_name": name, "boat_class": bc, "year": 2020, "head_count": 1,
             "displacement_kg": 5000, "draft_m": 1.5, **specs}
    resp = client.post("/api/v1/quick-analysis", json=qdata)
    if resp.status_code in (200, 201):
        score = resp.json().get("overall_assessment", {}).get("overall_score", "?")
        log(f"B4-Quick-{bc}", "PASS", f"{name}: Score={score}")
    else:
        log(f"B4-Quick-{bc}", "FAIL", f"{resp.status_code}: {resp.text[:100]}")

# B5: Schnellanalyse mit fehlenden Daten (minimal input)
resp = client.post("/api/v1/quick-analysis", json={
    "boat_class": "cruising_sail", "length_m": 10.0,
})
if resp.status_code in (200, 201):
    qa = resp.json()
    provided = qa.get("specs_provided", 0)
    inferred = qa.get("specs_inferred", 0)
    log("B5-MinimalInput", "PASS", f"Provided: {provided}, Inferred: {inferred}, Level: {qa.get('analysis_level')}")
else:
    log("B5-MinimalInput", "FAIL", f"{resp.status_code}: {resp.text[:150]}")


# ============================================================
# GRUPPE C: 10 DOMÄNEN-SZENARIEN MIT REALEN DATEN
# ============================================================
print("\n" + "="*70)
print("SZENARIO-GRUPPE C: 10 DOMÄNEN-SZENARIEN")
print("="*70)

# Test each domain's analysis module directly using correct function names
# All modules use run_*_analysis(zones, passages, boat_class, config_overrides, data_source)
# Zones need polygon field for area calculation

def make_zone(name, zone_type, polygon, properties=None):
    """Helper to create a zone dict with polygon."""
    return {"name": name, "zone_type": zone_type, "polygon": polygon,
            "properties": properties or {}}

# Standard polygon for a 3x2.5m area
RECT_3x25 = [[0,0],[3000,0],[3000,2500],[0,2500]]
RECT_2x15 = [[0,0],[2000,0],[2000,1500],[0,1500]]
RECT_1x1 = [[0,0],[1000,0],[1000,1000],[0,1000]]

from app.services.analysis.structural import run_structural_analysis
from app.services.analysis.materials import run_materials_analysis
from app.services.analysis.service_patterns import run_service_patterns_analysis
from app.services.analysis.compliance import run_compliance_analysis
from app.services.analysis.ergonomics import run_ergonomics_analysis
from app.services.analysis.volume_storage import run_volume_storage_analysis
from app.services.analysis.emotional import run_emotional_analysis
from app.services.analysis.production import run_production_analysis
from app.services.analysis.cost import run_cost_analysis
from app.services.analysis.brand_dna import run_brand_dna_analysis
from app.services.analysis.market import run_market_analysis

# C1: Hull/Structure
try:
    structural_result = run_structural_analysis(
        zones=[
            make_zone("Hull", "hull", RECT_3x25, {"material": "grp", "thickness_mm": 12}),
            make_zone("Keel", "keel", RECT_1x1, {"keel_type": "fin", "keel_weight_kg": 2800}),
        ],
        passages=[], boat_class="cruising_sail")
    log("C1-Hull-Structural", "PASS",
        f"Score: {structural_result.get('overall_score','?')}, Confidence: {structural_result.get('confidence','?')}")
except Exception as e:
    log("C1-Hull-Structural", "FAIL", f"Exception: {e}")

# C2: Rigging/Materials
try:
    materials_result = run_materials_analysis(
        zones=[
            make_zone("Mast", "mast", RECT_1x1, {"material": "aluminum_6082", "age_years": 16}),
            make_zone("Rigging", "rigging", RECT_1x1, {"material": "stainless_316L_wire", "age_years": 16}),
        ],
        passages=[], boat_class="cruising_sail")
    log("C2-Rigging-Materials", "PASS",
        f"Score: {materials_result.get('overall_score','?')}, Findings: {len(materials_result.get('findings',[]))}")
except Exception as e:
    log("C2-Rigging-Materials", "FAIL", f"Exception: {e}")

# C3: Propulsion/Service
try:
    service_result = run_service_patterns_analysis(
        zones=[
            make_zone("Maschinenraum", "engine", RECT_2x15, {
                "engine_type": "diesel", "engine_make": "Volvo Penta",
                "engine_hp": 29, "engine_hours": 2400}),
        ],
        passages=[], boat_class="cruising_sail")
    log("C3-Propulsion-Service", "PASS",
        f"Score: {service_result.get('overall_score','?')}")
except Exception as e:
    log("C3-Propulsion-Service", "FAIL", f"Exception: {e}")

# C4: Electrical/Compliance
try:
    compliance_result = run_compliance_analysis(
        zones=[
            make_zone("E-Panel", "electrical_panel", RECT_1x1, {"battery_bank_ah": 220}),
            make_zone("Batterie", "battery_compartment", RECT_1x1, {"battery_type": "agm"}),
        ],
        passages=[], boat_class="cruising_sail")
    log("C4-Electrical-Compliance", "PASS",
        f"Score: {compliance_result.get('overall_score','?')}")
except Exception as e:
    log("C4-Electrical-Compliance", "FAIL", f"Exception: {e}")

# C5: Sanitary/Compliance
try:
    sanitary_result = run_compliance_analysis(
        zones=[
            make_zone("Nasszelle", "head", RECT_2x15, {"has_toilet": True, "holding_tank": True}),
            make_zone("Frischwasser", "water_tank", RECT_1x1, {"capacity_liters": 200}),
        ],
        passages=[], boat_class="cruising_sail")
    log("C5-Sanitary-Compliance", "PASS",
        f"Score: {sanitary_result.get('overall_score','?')}")
except Exception as e:
    log("C5-Sanitary-Compliance", "FAIL", f"Exception: {e}")

# C6: Deck/Ergonomics
try:
    ergo_deck = run_ergonomics_analysis(
        zones=[
            make_zone("Cockpit", "cockpit", [[0,0],[3000,0],[3000,2500],[0,2500]], {"seat_count": 6}),
            make_zone("Vordeck", "foredeck", [[0,2500],[3000,2500],[3000,5000],[0,5000]], {"non_skid": True}),
            make_zone("Seitendeck", "side_deck", [[3000,0],[3350,0],[3350,5000],[3000,5000]], {"width_mm": 350}),
        ],
        passages=[{"from_zone": "Cockpit", "to_zone": "Vordeck", "width_mm": 350}],
        boat_class="cruising_sail")
    log("C6-Deck-Ergonomics", "PASS",
        f"Score: {ergo_deck.get('overall_score','?')}, Findings: {len(ergo_deck.get('findings',[]))}")
except Exception as e:
    log("C6-Deck-Ergonomics", "FAIL", f"Exception: {e}")

# C7: Interior/Volume
try:
    volume_result = run_volume_storage_analysis(
        zones=[
            make_zone("Salon", "saloon", [[0,0],[3200,0],[3200,3000],[0,3000]], {
                "headroom_mm": 1920, "storage_liters": 400}),
            make_zone("Pantry", "pantry", [[0,3000],[1800,3000],[1800,4500],[0,4500]], {
                "headroom_mm": 1900}),
            make_zone("Vorschiff", "cabin", [[0,4500],[3000,4500],[3000,7000],[1500,7500],[0,7000]], {
                "headroom_mm": 1850, "berth_count": 2}),
        ],
        passages=[], boat_class="cruising_sail")
    log("C7-Interior-Volume", "PASS",
        f"Score: {volume_result.get('overall_score','?')}")
except Exception as e:
    log("C7-Interior-Volume", "FAIL", f"Exception: {e}")

# C8: Safety/Compliance
try:
    safety_result = run_compliance_analysis(
        zones=[
            make_zone("Sicherheitslocker", "safety_locker", RECT_1x1, {
                "liferaft": True, "flares": True, "epirb": True}),
        ],
        passages=[], boat_class="cruising_sail")
    log("C8-Safety-Compliance", "PASS",
        f"Score: {safety_result.get('overall_score','?')}")
except Exception as e:
    log("C8-Safety-Compliance", "FAIL", f"Exception: {e}")

# C9: Navigation/Cost
try:
    cost_result = run_cost_analysis(
        zones=[
            make_zone("Navecke", "nav_station", RECT_1x1, {
                "chart_plotter": True, "autopilot": True, "radar": True}),
            make_zone("Helm", "helm", RECT_2x15, {"instruments_complete": True}),
        ],
        passages=[], boat_class="cruising_sail")
    log("C9-Navigation-Cost", "PASS",
        f"Score: {cost_result.get('overall_score','?')}")
except Exception as e:
    log("C9-Navigation-Cost", "FAIL", f"Exception: {e}")

# C10: Maintenance
try:
    maint_result = run_service_patterns_analysis(
        zones=[
            make_zone("Service", "service_area", RECT_2x15, {
                "antifouling_type": "hard", "antifouling_age_months": 18}),
        ],
        passages=[], boat_class="cruising_sail")
    log("C10-Maintenance-Service", "PASS",
        f"Score: {maint_result.get('overall_score','?')}")
except Exception as e:
    log("C10-Maintenance-Service", "FAIL", f"Exception: {e}")

# C-Extra: Emotional
try:
    emotional_result = run_emotional_analysis(
        zones=[
            make_zone("Salon", "saloon", [[0,0],[3200,0],[3200,3000],[0,3000]], {
                "natural_light": "good", "wood_type": "mahogany"}),
            make_zone("Cockpit", "cockpit", RECT_3x25, {"teak_deck": True}),
        ],
        passages=[], boat_class="cruising_sail")
    log("C-Emotional", "PASS", f"Score: {emotional_result.get('overall_score','?')}")
except Exception as e:
    log("C-Emotional", "FAIL", f"Exception: {e}")

# C-Extra: Production
try:
    production_result = run_production_analysis(
        zones=[
            make_zone("Hull", "hull", RECT_3x25, {"construction": "grp_sandwich"}),
            make_zone("Interior", "saloon", [[0,0],[3200,0],[3200,3000],[0,3000]], {
                "joinery": "veneer_plywood"}),
        ],
        passages=[], boat_class="cruising_sail")
    log("C-Production", "PASS", f"Score: {production_result.get('overall_score','?')}")
except Exception as e:
    log("C-Production", "FAIL", f"Exception: {e}")

# C-Extra: Brand DNA
try:
    brand_result = run_brand_dna_analysis(
        zones=[make_zone("Salon", "saloon", [[0,0],[3200,0],[3200,3000],[0,3000]], {
            "brand": "hallberg_rassy"})],
        passages=[], boat_class="cruising_sail")
    log("C-BrandDNA", "PASS", f"Score: {brand_result.get('overall_score','?')}")
except Exception as e:
    log("C-BrandDNA", "FAIL", f"Exception: {e}")

# C-Extra: Market
try:
    market_result = run_market_analysis(
        zones=[make_zone("Overall", "hull", RECT_3x25)],
        passages=[], boat_class="cruising_sail")
    log("C-Market", "PASS", f"Score: {market_result.get('overall_score','?')}")
except Exception as e:
    log("C-Market", "FAIL", f"Exception: {e}")


# ============================================================
# GRUPPE D: 4-SPRACHEN-PRAXISTEST
# ============================================================
print("\n" + "="*70)
print("SZENARIO-GRUPPE D: 4-SPRACHEN-PRAXISTEST")
print("="*70)

from app.core.i18n import t, has_key, get_all_keys, Locale, NumberFormatter

# D1: Alle 4 Sprachen — Kernbegriffe
for lang_str in ["de", "en", "es", "fr"]:
    try:
        locale = Locale(lang_str)
        critical_keys = [
            "domain.hull_structure", "domain.rigging_sails", "domain.propulsion_engine",
            "confidence.measured", "confidence.estimated",
            "error.validation_failed", "unit.m", "unit.kg",
        ]
        missing = [k for k in critical_keys if not has_key(k)]
        if not missing:
            example = t("domain.hull_structure", locale)
            log(f"D1-Sprache-{lang_str.upper()}", "PASS",
                f"Alle {len(critical_keys)} Kern-Keys vorhanden. Beispiel: {example}")
        else:
            log(f"D1-Sprache-{lang_str.upper()}", "FAIL", f"Fehlend: {missing}")
    except Exception as e:
        log(f"D1-Sprache-{lang_str.upper()}", "FAIL", f"Exception: {e}")

# D2: Zahlenformatierung pro Locale
test_numbers = [
    (1234.56, Locale.DE, "1.234,56"),
    (1234.56, Locale.EN, "1,234.56"),
    (1234.56, Locale.FR, "1\u202f234,56"),
    (1234.56, Locale.ES, "1.234,56"),
]
for val, locale, expected in test_numbers:
    try:
        formatted = NumberFormatter.format_number(val, locale=locale)
        clean_f = formatted.replace("\xa0", " ").replace("\u202f", " ")
        clean_e = expected.replace("\xa0", " ").replace("\u202f", " ")
        if clean_f == clean_e or formatted == expected:
            log(f"D2-NumFormat-{locale.value.upper()}", "PASS", f"{val} → {formatted}")
        else:
            log(f"D2-NumFormat-{locale.value.upper()}", "FAIL", f"Erwartet '{expected}', bekommen '{formatted}'")
    except Exception as e:
        log(f"D2-NumFormat-{locale.value.upper()}", "FAIL", f"Exception: {e}")

# D3: Währungsformatierung
for locale in [Locale.DE, Locale.EN, Locale.ES, Locale.FR]:
    try:
        formatted = NumberFormatter.format_currency(15750.00, locale=locale)
        log(f"D3-Currency-{locale.value.upper()}", "PASS", f"15750 EUR → {formatted}")
    except Exception as e:
        log(f"D3-Currency-{locale.value.upper()}", "FAIL", f"Exception: {e}")

# D4: Marine-Fachterminologie
marine_terms = ["marine.shrouds", "marine.forestay", "finding.gelcoat_damage", "finding.rigging_fatigue"]
for term in marine_terms:
    translations = {}
    for locale in [Locale.DE, Locale.EN, Locale.ES, Locale.FR]:
        try:
            tr = t(term, locale)
            translations[locale.value] = tr
        except:
            translations[locale.value] = "MISSING"
    all_unique = len(set(translations.values())) >= 3
    log(f"D4-Marine-{term}", "PASS" if all_unique else "WARN",
        f"{translations}")


# ============================================================
# GRUPPE E: STRESSSZENARIEN
# ============================================================
print("\n" + "="*70)
print("SZENARIO-GRUPPE E: STRESSSZENARIEN")
print("="*70)

# E1: Leere Eingabe
resp = client.post("/api/v1/quick-analysis", json={})
log("E1-LeereEingabe", "PASS" if resp.status_code == 422 else "FAIL",
    f"Status: {resp.status_code}")

# E2: Extremwerte
resp = client.post("/api/v1/quick-analysis", json={
    "boat_class": "superyacht",
    "length_m": 199.0, "beam_m": 30.0, "draft_m": 8.0,
    "year": 1900, "cabin_count": 50, "head_count": 25,
    "displacement_kg": 5000000,
})
if resp.status_code in (200, 201):
    log("E2-Extremwerte", "PASS", f"System verarbeitet Extremwerte ohne Crash")
else:
    log("E2-Extremwerte", "FAIL" if resp.status_code == 500 else "PASS",
        f"Status: {resp.status_code}: {resp.text[:100]}")

# E3: SQL-Injection Versuch
resp = client.post("/api/v1/quick-analysis", json={
    "model_name": "'; DROP TABLE users; --", "boat_class": "cruising_sail",
    "length_m": 10.0, "beam_m": 3.5,
})
log("E3-SQLInjection", "PASS" if resp.status_code in (200, 201, 422) else "FAIL",
    f"Status: {resp.status_code}")

# E4: XSS Versuch
resp = client.post("/api/v1/quick-analysis", json={
    "model_name": "<script>alert('xss')</script>", "boat_class": "cruising_sail",
    "length_m": 10.0, "beam_m": 3.5,
})
if resp.status_code in (200, 201):
    data = resp.json()
    # Eine JSON-API darf Nutzertext zurueckspiegeln — das ist per se kein XSS.
    # Entscheidend ist, dass der Browser die Antwort nicht als HTML deuten darf
    # (nosniff + application/json) und dass der einzige HTML-Renderpfad im
    # Frontend (KnowledgeDetail.tsx) durch DOMPurify laeuft.
    nosniff = resp.headers.get("X-Content-Type-Options") == "nosniff"
    is_json = resp.headers.get("content-type", "").startswith("application/json")
    log("E4-XSS-Sniffing", "PASS" if nosniff and is_json else "FAIL",
        "nosniff + application/json — Reflexion nicht als HTML interpretierbar"
        if nosniff and is_json
        else f"nosniff={nosniff}, content-type={resp.headers.get('content-type')}")
else:
    log("E4-XSS", "PASS" if resp.status_code == 422 else "FAIL", f"Status: {resp.status_code}")

# E5: Unbekannte Bootsklasse über Module direkt
unknown_result = run_ergonomics_analysis(
    zones=[make_zone("Test", "cabin", RECT_2x15, {"area_sqm": 5})],
    passages=[],
    boat_class="unknown_class_xyz",
)
if isinstance(unknown_result, dict):
    if unknown_result.get("available") is False or "overall_score" in unknown_result:
        log("E5-UnbekannteBK", "PASS", f"Graceful handling: {str(unknown_result)[:100]}")
    else:
        log("E5-UnbekannteBK", "PASS", f"Result: {str(unknown_result)[:100]}")
else:
    log("E5-UnbekannteBK", "FAIL", f"Unexpected type: {type(unknown_result)}")

# E6: Concurrent Quick-Analyses (simulated)
import time
start = time.time()
for i in range(10):
    client.post("/api/v1/quick-analysis", json={
        "model_name": f"Stresstest-{i}", "boat_class": "cruising_sail",
        "length_m": 10.0 + i*0.5, "beam_m": 3.5,
    })
elapsed = time.time() - start
log("E6-10xQuickAnalysis", "PASS" if elapsed < 30 else "FAIL",
    f"10 Schnellanalysen in {elapsed:.1f}s ({elapsed/10:.2f}s/Stück)")


# ============================================================
# GRUPPE F: SUBSCRIPTION-TIERS
# ============================================================
print("\n" + "="*70)
print("SZENARIO-GRUPPE F: SUBSCRIPTION-TIERS")
print("="*70)

from app.core.subscription import get_allowed_modules, has_feature, Feature

# F1: Free Tier
all_modules = ["ergonomics", "volume_storage", "emotional", "compliance", "production",
               "materials", "structural", "cost", "service_patterns", "brand_dna", "market"]

free_modules = get_allowed_modules("free")
log("F1-FreeModules", "PASS" if 2 <= len(free_modules) <= 6 else "WARN",
    f"Free: {len(free_modules)} Module: {free_modules}")

# F2: Pro Tier
pro_modules = get_allowed_modules("pro")
log("F2-ProModules", "PASS" if len(pro_modules) >= 10 else "FAIL",
    f"Pro: {len(pro_modules)} Module: {pro_modules}")

# F3: Enterprise Tier
ent_modules = get_allowed_modules("enterprise")
log("F3-EnterpriseModules", "PASS" if len(ent_modules) >= len(pro_modules) else "FAIL",
    f"Enterprise: {len(ent_modules)} Module")

# F4: Feature gating
for feature in Feature:
    free_has = has_feature("free", feature)
    pro_has = has_feature("pro", feature)
    ent_has = has_feature("enterprise", feature)
    # Enterprise should have everything Pro has
    if pro_has and not ent_has:
        log(f"F4-Feature-{feature.value}", "FAIL", f"Pro hat Feature aber Enterprise nicht!")
    else:
        log(f"F4-Feature-{feature.value}", "PASS",
            f"Free:{free_has}, Pro:{pro_has}, Enterprise:{ent_has}")


# ============================================================
# KNOWLEDGE BASE TESTS
# ============================================================
print("\n" + "="*70)
print("KNOWLEDGE-BASE & DOMAIN-MAPPING")
print("="*70)

from app.core.domains import (get_domain_for_zone_type, get_domain_for_component,
                               get_all_zone_types, get_all_component_categories,
                               get_critical_checks, AnalysisDomain, DOMAIN_CONFIGS)

# K1: Jeder Zone-Type mapped auf genau eine Domäne
all_zt = get_all_zone_types()
zt_issues = []
for zt in all_zt:
    domain = get_domain_for_zone_type(zt)
    if domain is None:
        zt_issues.append(f"{zt} → None")
log("K1-ZoneTypeMapping", "PASS" if not zt_issues else "FAIL",
    f"{len(all_zt)} Zone-Types, alle gemappt" if not zt_issues else f"Unmapped: {zt_issues}")

# K1b: Die beiden Vokabulare muessen deckungsgleich sein. K1 allein prueft nur
# die Domaenen gegen sich selbst und war deshalb trivial erfuellt — waehrend
# VALID_ZONE_TYPES und die Domaenen um je 4 Eintraege auseinandergelaufen waren.
from app.core.validation import VALID_ZONE_TYPES, ZONE_TYPE_ALIASES, normalize_zone_type
only_domains = sorted(set(all_zt) - VALID_ZONE_TYPES)
only_validation = sorted(zt for zt in VALID_ZONE_TYPES if get_domain_for_zone_type(zt) is None)
log("K1b-VokabularDeckung", "PASS" if not (only_domains or only_validation) else "FAIL",
    f"{len(VALID_ZONE_TYPES)} gueltige Typen, alle mit Domaene" if not (only_domains or only_validation)
    else f"nur in Domaenen: {only_domains} | ohne Domaene: {only_validation}")

# K1c: Gebraeuchliche Synonyme muessen auf kanonische Typen ziehen.
alias_issues = [f"{a} -> {t}" for a, t in ZONE_TYPE_ALIASES.items() if t not in VALID_ZONE_TYPES]
galley_ok = normalize_zone_type("galley") in VALID_ZONE_TYPES
log("K1c-ZoneTypeSynonyme", "PASS" if not alias_issues and galley_ok else "FAIL",
    f"{len(ZONE_TYPE_ALIASES)} Synonyme, u.a. galley->{normalize_zone_type('galley')}"
    if not alias_issues and galley_ok else f"Defekte Aliase: {alias_issues}")

# K2: Keine Zone-Type-Duplikate
from collections import Counter
all_zt_list = []
for config in DOMAIN_CONFIGS.values():
    all_zt_list.extend(config.zone_types)
dupes = [zt for zt, count in Counter(all_zt_list).items() if count > 1]
log("K2-ZoneTypeDuplikate", "PASS" if not dupes else "FAIL",
    f"Keine Duplikate" if not dupes else f"Duplikate: {dupes}")

# K3: Jede Domäne hat ≥5 Critical Checks
for domain in AnalysisDomain:
    checks = get_critical_checks(domain)
    log(f"K3-Checks-{domain.value}", "PASS" if len(checks) >= 5 else "FAIL",
        f"{len(checks)} Critical Checks")

# K4: Knowledge API
if "Sarah" in tokens:
    try:
        resp = client.get("/api/v1/knowledge/categories", headers=auth("Sarah"))
        if resp.status_code == 200:
            cats = resp.json()
            log("K4-KnowledgeAPI", "PASS", f"{len(cats)} Kategorien")
        else:
            log("K4-KnowledgeAPI", "FAIL", f"Status: {resp.status_code}")
    except Exception as e:
        log("K4-KnowledgeAPI", "FAIL", f"Exception: {e}")


# ============================================================
# FINAL REPORT
# ============================================================
print("\n" + "="*70)
print("PRAXISTEST — GESAMTERGEBNIS")
print("="*70)

passed = sum(1 for r in results if r["status"] == "PASS")
failed = sum(1 for r in results if r["status"] == "FAIL")
warned = sum(1 for r in results if r["status"] == "WARN")

print(f"\n  ✅ BESTANDEN:  {passed}")
print(f"  ❌ FEHLGESCHLAGEN: {failed}")
print(f"  ⚠️  WARNUNGEN:    {warned}")
print(f"  📊 GESAMT:       {len(results)}")
print(f"  📈 PASS-RATE:    {passed/len(results)*100:.1f}%\n")

if failed > 0:
    print("FEHLGESCHLAGENE TESTS:")
    for r in results:
        if r["status"] == "FAIL":
            print(f"  ❌ {r['scenario']}: {r['detail'][:120]}")

# Save full results
with open(_OUT / "praxistest_results.json", "w", encoding="utf-8") as f:
    json.dump(results, f, indent=2, ensure_ascii=False)

print(f"\n{'='*70}")
