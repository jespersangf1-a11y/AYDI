"""Haelt CLAUDE.md an den Code gefesselt.

CLAUDE.md ist die Arbeitsgrundlage jedes neuen Durchlaufs. Eine falsche Zahl
oder ein falscher Modulschluessel darin kostet mehr als ein Bug: der naechste
Durchlauf baut auf der Falschaussage auf. Diese Tests schlagen fehl, sobald
Spezifikation und Code auseinanderlaufen — in beide Richtungen.

Geprueft werden nur Aussagen, die sich objektiv am Code messen lassen.
"""

from __future__ import annotations

import glob
import re
from pathlib import Path

import pytest

BACKEND = Path(__file__).resolve().parent.parent
REPO = BACKEND.parent
CLAUDE_MD = REPO / "CLAUDE.md"
KNOWLEDGE_DIR = BACKEND / "app" / "services" / "knowledge"

# Suffixe, die der Loader bewusst ueberspringt (Zwischen-/Sicherungskopien).
BACKUP_SUFFIXES = ("_clean.md", "_backup.md", "_old.md", "_tmp.md")


@pytest.fixture(scope="module")
def spec() -> str:
    return CLAUDE_MD.read_text(encoding="utf-8")


# ---------------------------------------------------------------------------
# Korpusgroesse (SPEC-3 / COV-3 / D-9)
# ---------------------------------------------------------------------------


def _numbered_knowledge_files() -> list[Path]:
    return sorted(
        f for f in KNOWLEDGE_DIR.glob("*.md") if re.match(r"^\d{2}_\d{2}_", f.name)
    )


def test_corpus_numbers_in_spec_match_disk(spec: str) -> None:
    numbered = _numbered_knowledge_files()
    loaded = [f for f in numbered if not f.name.endswith(BACKUP_SUFFIXES)]
    categories = {f.name[:2] for f in numbered}

    assert len(numbered) == 261, "Korpus hat sich geaendert — CLAUDE.md mitziehen"
    assert len(loaded) == 260
    assert len(categories) == 32

    assert "**261**" in spec, "CLAUDE.md nennt nicht 261 Dateien auf der Platte"
    assert "**260**" in spec, "CLAUDE.md nennt nicht 260 geladene Dateien"
    assert "**32**" in spec, "CLAUDE.md nennt nicht 32 Kategorien"
    # Die alten, falschen Zahlen duerfen nicht zurueckkehren.
    assert "252 numbered" not in spec
    assert "**252**" not in spec
    assert "(252/31)" not in spec


def test_only_the_clean_copy_is_skipped_and_spec_names_it(spec: str) -> None:
    numbered = _numbered_knowledge_files()
    skipped = [f.name for f in numbered if f.name.endswith(BACKUP_SUFFIXES)]
    assert skipped == ["24_05_pumpen_sanitaer_clean.md"]
    assert "24_05_pumpen_sanitaer_clean.md" in spec, (
        "CLAUDE.md muss benennen, welche Datei bewusst uebersprungen wird"
    )


# ---------------------------------------------------------------------------
# score_fusion ist NICHT verdrahtet (SPEC-1 / SPEC-2 / SPEC-8)
# ---------------------------------------------------------------------------


def test_score_fusion_has_no_caller_in_app_and_spec_says_so(spec: str) -> None:
    callers = [
        p
        for p in glob.glob(str(BACKEND / "app" / "**" / "*.py"), recursive=True)
        if "score_fusion" in Path(p).read_text(encoding="utf-8")
    ]
    assert callers == [], (
        "score_fusion.py wird jetzt aufgerufen — CLAUDE.md darf es dann nicht "
        f"mehr als NICHT VERDRAHTET fuehren. Aufrufer: {callers}"
    )
    assert "NICHT VERDRAHTET" in spec


def test_fusion_weight_keys_match_spec_table(spec: str) -> None:
    from app.services.analysis.score_fusion import (
        DEFAULT_WEIGHTS,
        DISAGREEMENT_THRESHOLD,
        FUSION_WEIGHTS,
    )

    assert len(FUSION_WEIGHTS) == 12
    assert "volume_storage" in FUSION_WEIGHTS
    assert "volume" not in FUSION_WEIGHTS
    assert "community" in FUSION_WEIGHTS
    assert DEFAULT_WEIGHTS == (0.50, 0.50)
    assert DISAGREEMENT_THRESHOLD == 25.0

    # Jede Zeile der Tabelle in CLAUDE.md muss einen echten Schluessel treffen.
    table = re.findall(r"^\| (\w+) \| (\d\.\d\d) \| (\d\.\d\d) \|$", spec, re.M)
    assert table, "Score-Fusion-Tabelle in CLAUDE.md nicht gefunden"
    for module, sw, vw in table:
        assert module in FUSION_WEIGHTS, f"CLAUDE.md nennt unbekanntes Modul {module!r}"
        assert FUSION_WEIGHTS[module] == (float(sw), float(vw)), module
    assert {m for m, _, _ in table} == set(FUSION_WEIGHTS), (
        "Score-Fusion-Tabelle in CLAUDE.md ist unvollstaendig"
    )


def test_fusion_confidence_codes_are_not_emitted_by_backend(spec: str) -> None:
    """measured+visual / visual_only / discrepant kommen aus keinem Backend-Wert."""
    pattern = re.compile(r'"(measured\+visual|visual_only|discrepant)"')
    offenders: list[str] = []
    for p in glob.glob(str(BACKEND / "app" / "**" / "*.py"), recursive=True):
        for line in Path(p).read_text(encoding="utf-8").splitlines():
            if pattern.search(line) and not line.strip().startswith("#"):
                offenders.append(f"{Path(p).name}: {line.strip()}")
    assert offenders == [], (
        "Das Backend emittiert jetzt Fusions-Confidence-Codes — CLAUDE.md "
        f"aktualisieren. Treffer: {offenders}"
    )


# ---------------------------------------------------------------------------
# Orchestrator (SPEC-6 / SPEC-7)
# ---------------------------------------------------------------------------


def test_orchestrator_tiers_in_spec_match_code(spec: str) -> None:
    from app.services.analysis.orchestrator import ALL_MODULE_NAMES, EXECUTION_TIERS

    assert len(ALL_MODULE_NAMES) == 12, "Modulanzahl geaendert — CLAUDE.md mitziehen"
    assert EXECUTION_TIERS[0] == [
        "ergonomics",
        "volume_storage",
        "emotional",
        "compliance",
        "community",
    ]
    assert EXECUTION_TIERS[1] == ["production", "materials", "structural"]

    for tier_no, modules in enumerate(EXECUTION_TIERS, start=1):
        line = re.search(rf"^Tier {tier_no} \([^)]+\): (.+)$", spec, re.M)
        assert line, f"Tier {tier_no} fehlt im Orchestrator-Block von CLAUDE.md"
        # Erklaerenden Klammerzusatz ("(needs cost)") abschneiden.
        body = re.sub(r"\s*\(.*$", "", line.group(1))
        listed = {m.strip() for m in body.split(",") if m.strip()}
        assert listed == set(modules), (
            f"Tier {tier_no}: CLAUDE.md nennt {sorted(listed)}, Code {sorted(modules)}"
        )


def test_orchestrator_runs_no_visual_analysis_and_no_fusion() -> None:
    src = (BACKEND / "app" / "services" / "analysis" / "orchestrator.py").read_text(
        encoding="utf-8"
    )
    assert "visual" not in src
    assert "fusion" not in src


# ---------------------------------------------------------------------------
# Modulschluessel volume_storage (SPEC-2 / SPEC-6)
# ---------------------------------------------------------------------------


def test_spec_never_uses_the_nonexistent_module_key_volume() -> None:
    """Der Schluessel heisst ueberall volume_storage; 'volume' gibt es nicht."""
    from app.core.subscription import MODULE_FEATURE_MAP
    from app.services.analysis.orchestrator import ALL_MODULE_NAMES
    from app.services.analysis.score_fusion import FUSION_WEIGHTS

    for mapping in (MODULE_FEATURE_MAP, FUSION_WEIGHTS):
        assert "volume" not in mapping
        assert "volume_storage" in mapping
    assert "volume" not in ALL_MODULE_NAMES
    assert "volume_storage" in ALL_MODULE_NAMES


# ---------------------------------------------------------------------------
# Professional Module Enhancements (SPEC-5 / SPEC-9 / SPEC-10 / SPEC-13)
# ---------------------------------------------------------------------------


def test_configured_heel_angles_match_spec(spec: str) -> None:
    from app.services.analysis.ergonomics import BOAT_CLASS_DEFAULTS

    angles = sorted({c["heel_angle_deg"] for c in BOAT_CLASS_DEFAULTS.values()})
    assert angles == [0, 12, 15, 20, 25]
    assert "**0°, 12°, 15°, 20°, 25°**" in spec
    assert "Standard angles: 0°, 15°, 25°" not in spec


def test_cockpit_drain_is_a_flow_not_a_volume(spec: str) -> None:
    from app.services.analysis.compliance import DEFAULT_COCKPIT_DRAIN_TIME_S

    assert DEFAULT_COCKPIT_DRAIN_TIME_S == 300
    assert "drain_capacity = cockpit_volume × 2 (seconds)" not in spec, (
        "Die dimensionsfalsche Formel darf nicht als Ist-Zustand dastehen"
    )
    assert "required_drain_capacity_lps = cockpit_volume_liters / drain_time_s" in spec


def test_volume_module_has_no_deadspace_or_range_analysis(spec: str) -> None:
    src = (BACKEND / "app" / "services" / "analysis" / "volume_storage.py").read_text(
        encoding="utf-8"
    ).lower()
    assert "deadspace" not in src and "dead_space" not in src
    assert "geplant, nicht implementiert" in spec


def test_sightline_raytracing_description_matches_code(spec: str) -> None:
    src = (BACKEND / "app" / "services" / "analysis" / "emotional.py").read_text(
        encoding="utf-8"
    )
    assert "num_rays = 72" in src
    assert "_polygon_centroid(polygon)" in src
    assert "window=1.0, passage=0.5, wall=0.0" not in spec, (
        "Beschreibt ein Verfahren, das emotional.py nicht implementiert"
    )
    assert "72 Strahlen" in spec


# ---------------------------------------------------------------------------
# Zugriffs-Resolver (SPEC-14)
# ---------------------------------------------------------------------------


def test_access_resolver_delegation_count_matches_spec(spec: str) -> None:
    routes = sorted(
        Path(p) for p in glob.glob(str(BACKEND / "app" / "api" / "routes" / "*.py"))
        if not p.endswith("__init__.py")
    )
    delegating = sorted(
        p.stem for p in routes if "get_accessible_project" in p.read_text(encoding="utf-8")
    )
    assert len(routes) == 19
    assert delegating == [
        "costs",
        "images",
        "import_cad",
        "layouts",
        "materials",
        "organizations",
        "projects",
        "reports",
        "service_reports",
        "structural_items",
        "versions",
    ]
    assert "**11 der 19 Routenmodule**" in spec
    assert "All 9 route files delegate to it" not in spec


# ---------------------------------------------------------------------------
# Tech Stack (SPEC-11 / SPEC-12)
# ---------------------------------------------------------------------------


def test_scipy_is_neither_declared_nor_imported(spec: str) -> None:
    requirements = (BACKEND / "requirements.txt").read_text(encoding="utf-8").lower()
    assert "scipy" not in requirements
    importers = [
        p
        for p in glob.glob(str(BACKEND / "app" / "**" / "*.py"), recursive=True)
        if re.search(r"^\s*(import scipy|from scipy)", Path(p).read_text(encoding="utf-8"), re.M)
    ]
    assert importers == []
    assert "**Kein SciPy.**" in spec


def test_frontend_fonts_in_spec_match_tailwind_config(spec: str) -> None:
    config = (REPO / "frontend" / "tailwind.config.js").read_text(encoding="utf-8")
    index_html = (REPO / "frontend" / "index.html").read_text(encoding="utf-8")
    for font in ("Playfair Display", "Inter", "JetBrains Mono"):
        assert font in config, font
        assert font in spec, f"CLAUDE.md nennt {font} nicht"
    assert "Playfair+Display" in index_html
    for ghost in ("DM Sans", "Plus Jakarta Sans"):
        assert ghost not in config
        assert ghost not in index_html
        assert f"- {ghost}" not in spec


# ---------------------------------------------------------------------------
# Neu eingearbeitete Mechanismen
# ---------------------------------------------------------------------------


def test_subscore_helper_is_wired_into_eleven_modules(spec: str) -> None:
    from app.services.analysis.subscore import aggregate_subscores

    users = sorted(
        Path(p).stem
        for p in glob.glob(str(BACKEND / "app" / "services" / "analysis" / "*.py"))
        if "from app.services.analysis.subscore" in Path(p).read_text(encoding="utf-8")
    )
    assert len(users) == 11
    assert "community" not in users
    assert "degraded_subanalyses" in spec

    # Verhalten, das CLAUDE.md zusichert: Ausfaelle fliegen aus Zaehler UND Nenner.
    assert aggregate_subscores({"a": 80.0, "b": 0.0}, {"a": 0.5, "b": 0.5}, failed=["b"]) == 80.0
    assert aggregate_subscores({}, {"a": 1.0}, failed=["a"]) is None


def test_zone_type_aliases_and_domain_coverage(spec: str) -> None:
    from app.core.domains import DOMAIN_CONFIGS, get_domain_for_zone_type
    from app.core.validation import (
        VALID_ZONE_TYPES,
        ZONE_TYPE_ALIASES,
        normalize_zone_type,
    )

    domain_types: set[str] = set()
    for cfg in DOMAIN_CONFIGS.values():
        domain_types |= set(cfg.zone_types)
    assert domain_types == set(VALID_ZONE_TYPES)
    assert len(VALID_ZONE_TYPES) == 47
    assert all(get_domain_for_zone_type(z) for z in VALID_ZONE_TYPES)

    assert len(ZONE_TYPE_ALIASES) == 37
    assert all(target in VALID_ZONE_TYPES for target in ZONE_TYPE_ALIASES.values())
    assert normalize_zone_type("Galley") == "pantry"
    assert normalize_zone_type("salon") == "saloon"
    assert normalize_zone_type(" Unbekannt ") == "unbekannt"  # unveraendert, nur normiert

    assert "ZONE_TYPE_ALIASES" in spec and "normalize_zone_type" in spec


def test_security_headers_middleware_documented(spec: str) -> None:
    from app.core.middleware import SecurityHeadersMiddleware

    assert set(SecurityHeadersMiddleware.STATIC_HEADERS) == {
        "X-Content-Type-Options",
        "X-Frame-Options",
        "Referrer-Policy",
        "Content-Security-Policy",
        "Cross-Origin-Resource-Policy",
    }
    assert SecurityHeadersMiddleware.STATIC_HEADERS["X-Content-Type-Options"] == "nosniff"
    middleware_src = (BACKEND / "app" / "core" / "middleware.py").read_text(encoding="utf-8")
    assert "app.add_middleware(SecurityHeadersMiddleware)" in middleware_src
    assert "SecurityHeadersMiddleware" in spec


def test_render_yaml_arms_the_production_boot_guard(spec: str) -> None:
    render = (REPO / "render.yaml").read_text(encoding="utf-8")
    assert re.search(r"key:\s*ENVIRONMENT\s*\n\s*value:\s*\"production\"", render)
    assert re.search(r"key:\s*COOKIE_SECURE\s*\n\s*value:\s*\"true\"", render)
    assert re.search(r"key:\s*SECRET_KEY\s*\n\s*sync:\s*false", render)
    assert "ENVIRONMENT=production" in spec


# ---------------------------------------------------------------------------
# Setup-Abschnitt (SPEC-15)
# ---------------------------------------------------------------------------


def test_documented_env_vars_exist_on_settings(spec: str) -> None:
    from app.core.config import Settings

    # Erste Tabellenspalte einsammeln; Zeilen fassen teils mehrere Vars
    # zusammen ("`LOG_LEVEL` / `LOG_JSON`").
    documented: set[str] = set()
    for row in re.findall(r"^\|((?:\s*`[A-Z][A-Z0-9_]+`\s*/?)+)\|", spec, re.M):
        documented |= set(re.findall(r"`([A-Z][A-Z0-9_]+)`", row))

    known = set(Settings.model_fields)
    assert documented, "Env-Var-Tabelle in CLAUDE.md nicht gefunden"
    assert documented <= known, f"CLAUDE.md dokumentiert unbekannte Env-Vars: {documented - known}"
    for required in ("ENVIRONMENT", "DATABASE_URL", "SECRET_KEY", "COOKIE_SECURE"):
        assert required in documented, f"{required} fehlt in der Env-Tabelle"


def test_setup_section_names_the_real_commands(spec: str) -> None:
    assert (KNOWLEDGE_DIR.parent.parent.parent / "praxistest_full.py").exists()
    assert (BACKEND / "praxistest_runner.py").exists()
    assert (BACKEND / "alembic.ini").exists()
    assert (BACKEND / "requirements.txt").exists()
    assert len(list((BACKEND / "migrations" / "versions").glob("0*.py"))) == 7

    for command in (
        "pip install -r requirements.txt",
        "PYTHONPATH=. alembic upgrade head",
        "PYTHONPATH=. uvicorn app.main:app --reload",
        "PYTHONPATH=. python -m pytest tests/ -q",
        "PYTHONPATH=. python praxistest_full.py",
        "npm install",
        "npm run dev",
    ):
        assert command in spec, f"Setup-Kommando fehlt in CLAUDE.md: {command}"
