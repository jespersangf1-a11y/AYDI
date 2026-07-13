> **⚠️ ARCHIV — HISTORISCHER PLANUNGSSTAND (nicht maßgeblich).**
> Dieses Dokument beschreibt einen früheren Planungs-/Design-Stand und trackt den aktuellen Code **nicht**.
> Bekannte Drift: 4 statt real **13 Bootsklassen** (`BoatClass`-Enum); abweichende Sub-Analysen/Gewichte; einzelne enthaltene Tests schlagen gegen den Ist-Code fehl.
> **Maßgeblich ist `CLAUDE.md`** (plus der Code). Nicht zum Ableiten von Enums, Return-Contracts oder Tests verwenden.

# Material & Quality Analysis Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Build Module 6 — a material & quality analysis module that evaluates material choices for durability, maintenance burden, known issues, compatibility, and weight impact. Includes the required data layer (Material DB, ZoneMaterial assignments, CRUD routes).

**Architecture:** Two layers: (1) Data layer — `Material` and `ZoneMaterial` ORM models with CRUD routes for managing a global material database and per-layout assignments. (2) Pure-function analysis module following the established AYDI pattern (BOAT_CLASS_DEFAULTS, 5 sub-analyses, orchestrator). The analysis function receives pre-loaded material data as dicts — no DB access inside. The route handler in `layouts.py` loads material data before calling the analysis function.

**Tech Stack:** Python 3.12, FastAPI, SQLAlchemy 2.0 (async), Pydantic v2, pytest

---

## File Structure

| File | Action | Responsibility |
|---|---|---|
| `backend/app/models/models.py` | MODIFY | Add `Material` and `ZoneMaterial` ORM models |
| `backend/app/schemas/materials.py` | CREATE | Pydantic schemas for materials CRUD |
| `backend/app/api/routes/materials.py` | CREATE | Materials CRUD + zone assignment routes |
| `backend/app/main.py` | MODIFY | Register materials router |
| `backend/app/services/analysis/materials.py` | CREATE | BOAT_CLASS_DEFAULTS, 5 sub-analyses, orchestrator |
| `backend/app/api/routes/layouts.py` | MODIFY | Add material data loader for analysis endpoint |
| `backend/tests/conftest.py` | MODIFY | Add `make_material()` and `make_zone_material()` helpers |
| `backend/tests/test_materials.py` | CREATE | ~25 tests for analysis module |

---

### Task 1: ORM Models (Material + ZoneMaterial)

**Files:**
- Modify: `backend/app/models/models.py`

- [ ] **Step 1: Add Material and ZoneMaterial models to models.py**

Add after the `Passage` class at the bottom of `models.py`:

```python
class Material(Base):
    __tablename__ = "materials"

    id: Mapped[uuid.UUID] = mapped_column(Uuid, primary_key=True, default=uuid.uuid4)
    name: Mapped[str] = mapped_column(String(255), nullable=False)
    category: Mapped[str] = mapped_column(String(50), nullable=False)
    subcategory: Mapped[str] = mapped_column(String(50), nullable=False)
    manufacturer: Mapped[str | None] = mapped_column(String(255), nullable=True)
    properties: Mapped[dict | None] = mapped_column(JSON, nullable=True)
    cost_per_unit: Mapped[float] = mapped_column(Float, nullable=False, default=0.0)
    cost_unit: Mapped[str] = mapped_column(String(20), nullable=False, default="sqm")
    lifespan_years: Mapped[float | None] = mapped_column(Float, nullable=True)
    maintenance_interval_months: Mapped[int | None] = mapped_column(Integer, nullable=True)
    maintenance_cost_factor: Mapped[float] = mapped_column(Float, nullable=False, default=0.0)
    known_issues: Mapped[list | None] = mapped_column(JSON, nullable=True)
    alternatives: Mapped[list | None] = mapped_column(JSON, nullable=True)
    created_at: Mapped[datetime] = mapped_column(DateTime, default=_utcnow)
    updated_at: Mapped[datetime] = mapped_column(DateTime, default=_utcnow, onupdate=_utcnow)


class ZoneMaterial(Base):
    __tablename__ = "zone_materials"

    id: Mapped[uuid.UUID] = mapped_column(Uuid, primary_key=True, default=uuid.uuid4)
    layout_id: Mapped[uuid.UUID] = mapped_column(ForeignKey("layouts.id", ondelete="CASCADE"), nullable=False)
    zone_name: Mapped[str] = mapped_column(String(100), nullable=False)
    surface_type: Mapped[str] = mapped_column(String(50), nullable=False)
    material_id: Mapped[uuid.UUID] = mapped_column(ForeignKey("materials.id", ondelete="CASCADE"), nullable=False)
    area_sqm: Mapped[float] = mapped_column(Float, nullable=False)
    notes: Mapped[str | None] = mapped_column(Text, nullable=True)
    created_at: Mapped[datetime] = mapped_column(DateTime, default=_utcnow)

    material: Mapped["Material"] = relationship()
    layout: Mapped["Layout"] = relationship(back_populates="zone_materials")
```

Also add a `zone_materials` relationship on the `Layout` model. In `models.py`, add inside the `Layout` class (after the `analysis_results` relationship):

```python
    zone_materials: Mapped[list["ZoneMaterial"]] = relationship(
        back_populates="layout", cascade="all, delete-orphan"
    )
```

- [ ] **Step 2: Verify app starts (tables auto-created)**

Run: `cd backend && PYTHONPATH=. python -c "from app.models.models import Material, ZoneMaterial; print('OK')"`
Expected: `OK`

- [ ] **Step 3: Generate Alembic migration**

Run: `cd backend && alembic revision --autogenerate -m "add materials and zone_materials tables"`
Expected: New migration file created in `backend/migrations/versions/`

- [ ] **Step 4: Commit**

```bash
git add backend/app/models/models.py backend/migrations/versions/
git commit -m "feat: add Material and ZoneMaterial ORM models"
```

---

### Task 2: Pydantic Schemas + conftest helpers

**Files:**
- Create: `backend/app/schemas/materials.py`
- Modify: `backend/tests/conftest.py`

- [ ] **Step 1: Create material schemas**

```python
# backend/app/schemas/materials.py
from datetime import datetime
from uuid import UUID

from pydantic import BaseModel, ConfigDict


class MaterialCreate(BaseModel):
    name: str
    category: str
    subcategory: str
    manufacturer: str | None = None
    properties: dict | None = None
    cost_per_unit: float = 0.0
    cost_unit: str = "sqm"
    lifespan_years: float | None = None
    maintenance_interval_months: int | None = None
    maintenance_cost_factor: float = 0.0
    known_issues: list[dict] | None = None
    alternatives: list[str] | None = None


class MaterialUpdate(BaseModel):
    name: str | None = None
    category: str | None = None
    subcategory: str | None = None
    manufacturer: str | None = None
    properties: dict | None = None
    cost_per_unit: float | None = None
    cost_unit: str | None = None
    lifespan_years: float | None = None
    maintenance_interval_months: int | None = None
    maintenance_cost_factor: float | None = None
    known_issues: list[dict] | None = None
    alternatives: list[str] | None = None


class MaterialResponse(BaseModel):
    id: UUID
    name: str
    category: str
    subcategory: str
    manufacturer: str | None
    properties: dict | None
    cost_per_unit: float
    cost_unit: str
    lifespan_years: float | None
    maintenance_interval_months: int | None
    maintenance_cost_factor: float
    known_issues: list[dict] | None
    alternatives: list[str] | None
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)


class ZoneMaterialCreate(BaseModel):
    zone_name: str
    surface_type: str
    material_id: UUID
    area_sqm: float
    notes: str | None = None


class ZoneMaterialResponse(BaseModel):
    id: UUID
    layout_id: UUID
    zone_name: str
    surface_type: str
    material_id: UUID
    area_sqm: float
    notes: str | None
    created_at: datetime

    model_config = ConfigDict(from_attributes=True)
```

- [ ] **Step 2: Add conftest helpers**

Append to `backend/tests/conftest.py`:

```python
def make_material(
    name: str = "Test Material",
    category: str = "interior",
    subcategory: str = "wood",
    cost_per_unit: float = 100.0,
    cost_unit: str = "sqm",
    lifespan_years: float = 20.0,
    maintenance_interval_months: int = 12,
    maintenance_cost_factor: float = 0.02,
    known_issues: list[dict] | None = None,
    properties: dict | None = None,
) -> dict:
    return {
        "name": name,
        "category": category,
        "subcategory": subcategory,
        "cost_per_unit": cost_per_unit,
        "cost_unit": cost_unit,
        "lifespan_years": lifespan_years,
        "maintenance_interval_months": maintenance_interval_months,
        "maintenance_cost_factor": maintenance_cost_factor,
        "known_issues": known_issues or [],
        "properties": properties or {},
    }


def make_zone_material(
    zone_name: str = "salon",
    surface_type: str = "floor",
    area_sqm: float = 10.0,
    material: dict | None = None,
) -> dict:
    if material is None:
        material = make_material()
    return {
        "zone_name": zone_name,
        "surface_type": surface_type,
        "area_sqm": area_sqm,
        "material": material,
    }
```

- [ ] **Step 3: Commit**

```bash
git add backend/app/schemas/materials.py backend/tests/conftest.py
git commit -m "feat: add material Pydantic schemas and conftest helpers"
```

---

### Task 3: Materials CRUD Routes + registration

**Files:**
- Create: `backend/app/api/routes/materials.py`
- Modify: `backend/app/main.py`

- [ ] **Step 1: Create materials CRUD route file**

```python
# backend/app/api/routes/materials.py
from uuid import UUID

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from app.db.database import get_db
from app.models.models import Layout, Material, ZoneMaterial
from app.schemas.materials import (
    MaterialCreate,
    MaterialResponse,
    MaterialUpdate,
    ZoneMaterialCreate,
    ZoneMaterialResponse,
)

router = APIRouter(tags=["materials"])


# --- Global material database ---


@router.get("/materials", response_model=list[MaterialResponse])
async def list_materials(
    category: str | None = None,
    subcategory: str | None = None,
    db: AsyncSession = Depends(get_db),
):
    query = select(Material).order_by(Material.name)
    if category:
        query = query.where(Material.category == category)
    if subcategory:
        query = query.where(Material.subcategory == subcategory)
    result = await db.execute(query)
    return result.scalars().all()


@router.post("/materials", response_model=MaterialResponse, status_code=201)
async def create_material(
    data: MaterialCreate,
    db: AsyncSession = Depends(get_db),
):
    material = Material(**data.model_dump())
    db.add(material)
    await db.commit()
    await db.refresh(material)
    return material


@router.get("/materials/{material_id}", response_model=MaterialResponse)
async def get_material(
    material_id: UUID,
    db: AsyncSession = Depends(get_db),
):
    result = await db.execute(select(Material).where(Material.id == material_id))
    material = result.scalar_one_or_none()
    if not material:
        raise HTTPException(status_code=404, detail="Material nicht gefunden")
    return material


@router.patch("/materials/{material_id}", response_model=MaterialResponse)
async def update_material(
    material_id: UUID,
    data: MaterialUpdate,
    db: AsyncSession = Depends(get_db),
):
    result = await db.execute(select(Material).where(Material.id == material_id))
    material = result.scalar_one_or_none()
    if not material:
        raise HTTPException(status_code=404, detail="Material nicht gefunden")

    for field, value in data.model_dump(exclude_unset=True).items():
        setattr(material, field, value)

    await db.commit()
    await db.refresh(material)
    return material


@router.delete("/materials/{material_id}", status_code=204)
async def delete_material(
    material_id: UUID,
    db: AsyncSession = Depends(get_db),
):
    result = await db.execute(select(Material).where(Material.id == material_id))
    material = result.scalar_one_or_none()
    if not material:
        raise HTTPException(status_code=404, detail="Material nicht gefunden")
    await db.delete(material)
    await db.commit()


# --- Zone material assignments (per layout) ---


@router.get(
    "/projects/{project_id}/layouts/{layout_id}/materials",
    response_model=list[ZoneMaterialResponse],
)
async def list_zone_materials(
    project_id: UUID,
    layout_id: UUID,
    db: AsyncSession = Depends(get_db),
):
    result = await db.execute(
        select(Layout).where(Layout.id == layout_id, Layout.project_id == project_id)
    )
    if not result.scalar_one_or_none():
        raise HTTPException(status_code=404, detail="Layout nicht gefunden")

    result = await db.execute(
        select(ZoneMaterial).where(ZoneMaterial.layout_id == layout_id)
    )
    return result.scalars().all()


@router.post(
    "/projects/{project_id}/layouts/{layout_id}/materials",
    response_model=ZoneMaterialResponse,
    status_code=201,
)
async def assign_zone_material(
    project_id: UUID,
    layout_id: UUID,
    data: ZoneMaterialCreate,
    db: AsyncSession = Depends(get_db),
):
    result = await db.execute(
        select(Layout).where(Layout.id == layout_id, Layout.project_id == project_id)
    )
    if not result.scalar_one_or_none():
        raise HTTPException(status_code=404, detail="Layout nicht gefunden")

    # Verify material exists
    result = await db.execute(
        select(Material).where(Material.id == data.material_id)
    )
    if not result.scalar_one_or_none():
        raise HTTPException(status_code=404, detail="Material nicht gefunden")

    zone_mat = ZoneMaterial(
        layout_id=layout_id,
        zone_name=data.zone_name,
        surface_type=data.surface_type,
        material_id=data.material_id,
        area_sqm=data.area_sqm,
        notes=data.notes,
    )
    db.add(zone_mat)
    await db.commit()
    await db.refresh(zone_mat)
    return zone_mat


@router.delete(
    "/projects/{project_id}/layouts/{layout_id}/materials/{zone_material_id}",
    status_code=204,
)
async def delete_zone_material(
    project_id: UUID,
    layout_id: UUID,
    zone_material_id: UUID,
    db: AsyncSession = Depends(get_db),
):
    result = await db.execute(
        select(ZoneMaterial).where(
            ZoneMaterial.id == zone_material_id,
            ZoneMaterial.layout_id == layout_id,
        )
    )
    zone_mat = result.scalar_one_or_none()
    if not zone_mat:
        raise HTTPException(status_code=404, detail="Materialzuweisung nicht gefunden")
    await db.delete(zone_mat)
    await db.commit()
```

- [ ] **Step 2: Register materials router in main.py**

In `backend/app/main.py`, add import:

```python
from app.api.routes import layouts, materials, projects
```

And add router registration:

```python
app.include_router(materials.router, prefix="/api/v1")
```

- [ ] **Step 3: Verify existing tests still pass**

Run: `cd backend && PYTHONPATH=. pytest tests/ -q`
Expected: 126 passed

- [ ] **Step 4: Commit**

```bash
git add backend/app/api/routes/materials.py backend/app/main.py
git commit -m "feat: add materials CRUD routes and register router"
```

---

### Task 4: analyze_material_durability + analyze_maintenance_burden

**Files:**
- Create: `backend/app/services/analysis/materials.py`
- Create: `backend/tests/test_materials.py`

- [ ] **Step 1: Write failing tests**

```python
"""Tests for material & quality analysis module."""
from tests.conftest import make_material, make_zone_material
from app.services.analysis.materials import (
    analyze_material_durability,
    analyze_maintenance_burden,
    BOAT_CLASS_DEFAULTS,
)


def _default_config(boat_class="cruising_sail"):
    config = BOAT_CLASS_DEFAULTS[boat_class].copy()
    config.pop("weights", None)
    return config


# ---------------------------------------------------------------------------
# analyze_material_durability
# ---------------------------------------------------------------------------


def test_durability_all_long_lived():
    """All materials outlast min lifespan -> score 100."""
    zone_mats = [
        make_zone_material("salon", "floor", 10.0, make_material(lifespan_years=25)),
        make_zone_material("cabin", "wall", 8.0, make_material(lifespan_years=30)),
    ]
    config = _default_config()  # min_lifespan_years = 20
    score, warnings, metrics = analyze_material_durability(zone_mats, config)
    assert score == 100.0
    assert metrics["compliant_count"] == 2


def test_durability_short_lived():
    """Material with lifespan below min -> warning, lower score."""
    zone_mats = [
        make_zone_material("salon", "floor", 10.0, make_material(lifespan_years=10)),
        make_zone_material("cabin", "wall", 8.0, make_material(lifespan_years=25)),
    ]
    config = _default_config()  # min_lifespan_years = 20
    score, warnings, metrics = analyze_material_durability(zone_mats, config)
    assert score < 100.0
    assert any(w["severity"] == "warning" for w in warnings)
    assert any(w["code"] == "MATERIAL_SHORT_LIFE" for w in warnings)
    assert metrics["compliant_count"] == 1


def test_durability_no_lifespan_data():
    """Material without lifespan_years -> info warning."""
    zone_mats = [
        make_zone_material("salon", "floor", 10.0, make_material(lifespan_years=None)),
    ]
    config = _default_config()
    score, warnings, metrics = analyze_material_durability(zone_mats, config)
    assert score == 50.0
    assert any(w["severity"] == "info" for w in warnings)


def test_durability_no_materials():
    """No material assignments -> score 50, info."""
    config = _default_config()
    score, warnings, metrics = analyze_material_durability([], config)
    assert score == 50.0
    assert any(w["severity"] == "info" for w in warnings)


# ---------------------------------------------------------------------------
# analyze_maintenance_burden
# ---------------------------------------------------------------------------


def test_maintenance_low():
    """Low maintenance cost -> score 100."""
    zone_mats = [
        make_zone_material("salon", "floor", 10.0,
            make_material(cost_per_unit=100.0, maintenance_cost_factor=0.01)),
    ]
    config = _default_config()  # max_annual_maintenance_pct = 0.025
    score, warnings, metrics = analyze_maintenance_burden(zone_mats, config)
    assert score >= 80.0
    assert metrics["annual_maintenance_eur"] > 0


def test_maintenance_high():
    """High maintenance cost -> warning, lower score."""
    zone_mats = [
        make_zone_material("salon", "floor", 50.0,
            make_material(cost_per_unit=200.0, maintenance_cost_factor=0.10)),
    ]
    config = _default_config()  # max_annual_maintenance_pct = 0.025
    score, warnings, metrics = analyze_maintenance_burden(zone_mats, config)
    assert score < 80.0
    assert any(w["code"] == "MAINTENANCE_HIGH" for w in warnings)


def test_maintenance_no_materials():
    """No materials -> score 50, info."""
    config = _default_config()
    score, warnings, metrics = analyze_maintenance_burden([], config)
    assert score == 50.0
    assert any(w["severity"] == "info" for w in warnings)
```

- [ ] **Step 2: Run tests to verify they fail**

Run: `cd backend && PYTHONPATH=. pytest tests/test_materials.py -v`
Expected: FAIL — module `materials` does not exist

- [ ] **Step 3: Create materials.py with BOAT_CLASS_DEFAULTS + first 2 sub-analyses**

```python
"""Material & quality analysis module for yacht layouts.

Evaluates material choices for durability, maintenance burden, known issues,
compatibility, and weight impact. Pure function module — no database access.
All user-facing strings are in German.
"""
import logging

logger = logging.getLogger(__name__)

BOAT_CLASS_DEFAULTS = {
    "small_sail": {
        "min_lifespan_years": 15,
        "max_annual_maintenance_pct": 0.03,
        "max_zone_weight_kg_sqm": 25.0,
        "weights": {
            "durability": 0.30,
            "maintenance": 0.25,
            "known_issues": 0.20,
            "compatibility": 0.15,
            "weight": 0.10,
        },
    },
    "cruising_sail": {
        "min_lifespan_years": 20,
        "max_annual_maintenance_pct": 0.025,
        "max_zone_weight_kg_sqm": 30.0,
        "weights": {
            "durability": 0.25,
            "maintenance": 0.25,
            "known_issues": 0.20,
            "compatibility": 0.15,
            "weight": 0.15,
        },
    },
    "large_motor": {
        "min_lifespan_years": 20,
        "max_annual_maintenance_pct": 0.02,
        "max_zone_weight_kg_sqm": 35.0,
        "weights": {
            "durability": 0.20,
            "maintenance": 0.25,
            "known_issues": 0.25,
            "compatibility": 0.15,
            "weight": 0.15,
        },
    },
    "superyacht": {
        "min_lifespan_years": 25,
        "max_annual_maintenance_pct": 0.015,
        "max_zone_weight_kg_sqm": 40.0,
        "weights": {
            "durability": 0.20,
            "maintenance": 0.20,
            "known_issues": 0.25,
            "compatibility": 0.20,
            "weight": 0.15,
        },
    },
}

SEVERITY_ORDER = {"critical": 0, "warning": 1, "info": 2}


# ---------------------------------------------------------------------------
# Sub-analysis: Material durability
# ---------------------------------------------------------------------------


def analyze_material_durability(
    zone_materials: list[dict],
    config: dict,
) -> tuple[float, list[dict], dict]:
    """Check if material lifespans meet minimum requirements.

    Each zone_material dict has keys: zone_name, surface_type, area_sqm, material.
    material dict has: lifespan_years, name, etc.

    Returns (score 0-100, warnings, metrics).
    """
    warnings: list[dict] = []

    if not zone_materials:
        warnings.append({
            "code": "MATERIAL_NO_ASSIGNMENTS",
            "severity": "info",
            "message": "Keine Materialzuweisungen für Haltbarkeitsanalyse vorhanden.",
            "suggestion": "Materialien den Zonen zuweisen.",
        })
        return 50.0, warnings, {"compliant_count": 0, "total_count": 0, "missing_data_count": 0}

    min_life = config.get("min_lifespan_years", 20)
    compliant = 0
    missing_data = 0

    for zm in zone_materials:
        mat = zm["material"]
        lifespan = mat.get("lifespan_years")

        if lifespan is None:
            missing_data += 1
            warnings.append({
                "code": "MATERIAL_NO_LIFESPAN",
                "severity": "info",
                "message": (
                    f"Material '{mat.get('name', '?')}' in Zone '{zm['zone_name']}' "
                    f"({zm['surface_type']}): keine Lebensdauer-Angabe."
                ),
                "suggestion": f"Lebensdauer für '{mat.get('name', '?')}' hinterlegen.",
            })
            continue

        if lifespan >= min_life:
            compliant += 1
        else:
            warnings.append({
                "code": "MATERIAL_SHORT_LIFE",
                "severity": "warning",
                "message": (
                    f"Material '{mat.get('name', '?')}' in Zone '{zm['zone_name']}' "
                    f"({zm['surface_type']}): Lebensdauer {lifespan:.0f} Jahre "
                    f"< Minimum {min_life} Jahre."
                ),
                "suggestion": (
                    f"Material mit Lebensdauer ≥ {min_life} Jahre wählen oder "
                    f"Wartungsplan erstellen."
                ),
            })

    evaluated = len(zone_materials) - missing_data
    if evaluated == 0:
        return 50.0, warnings, {
            "compliant_count": 0,
            "total_count": len(zone_materials),
            "missing_data_count": missing_data,
        }

    score = (compliant / evaluated) * 100.0

    return score, warnings, {
        "compliant_count": compliant,
        "total_count": len(zone_materials),
        "missing_data_count": missing_data,
    }


# ---------------------------------------------------------------------------
# Sub-analysis: Maintenance burden
# ---------------------------------------------------------------------------


def analyze_maintenance_burden(
    zone_materials: list[dict],
    config: dict,
) -> tuple[float, list[dict], dict]:
    """Estimate annual maintenance cost and compare to benchmark.

    Annual maintenance per assignment = area_sqm * cost_per_unit * maintenance_cost_factor.
    Total is compared against max_annual_maintenance_pct * total_material_cost.

    Returns (score 0-100, warnings, metrics).
    """
    warnings: list[dict] = []

    if not zone_materials:
        warnings.append({
            "code": "MAINTENANCE_NO_MATERIALS",
            "severity": "info",
            "message": "Keine Materialzuweisungen für Wartungskosten-Analyse vorhanden.",
            "suggestion": "Materialien den Zonen zuweisen.",
        })
        return 50.0, warnings, {
            "annual_maintenance_eur": 0.0,
            "total_material_cost_eur": 0.0,
            "maintenance_ratio": 0.0,
        }

    max_pct = config.get("max_annual_maintenance_pct", 0.025)

    total_material_cost = 0.0
    annual_maintenance = 0.0

    for zm in zone_materials:
        mat = zm["material"]
        area = zm.get("area_sqm", 0.0)
        cost = mat.get("cost_per_unit", 0.0)
        factor = mat.get("maintenance_cost_factor", 0.0)

        mat_cost = area * cost
        total_material_cost += mat_cost
        annual_maintenance += mat_cost * factor

    if total_material_cost <= 0:
        return 50.0, warnings, {
            "annual_maintenance_eur": 0.0,
            "total_material_cost_eur": 0.0,
            "maintenance_ratio": 0.0,
        }

    ratio = annual_maintenance / total_material_cost

    if ratio > max_pct:
        # Score degrades proportionally: at 2x benchmark → score 0
        overshoot = ratio / max_pct
        score = max(0.0, 100.0 * (2.0 - overshoot))
        warnings.append({
            "code": "MAINTENANCE_HIGH",
            "severity": "warning",
            "message": (
                f"Jährliche Wartungskosten ca. {annual_maintenance:.0f} EUR "
                f"({ratio:.1%} der Materialkosten) — Richtwert: {max_pct:.1%}."
            ),
            "suggestion": "Wartungsarme Materialien bevorzugen oder Wartungsplan budgetieren.",
        })
    else:
        score = 100.0

    return score, warnings, {
        "annual_maintenance_eur": round(annual_maintenance, 2),
        "total_material_cost_eur": round(total_material_cost, 2),
        "maintenance_ratio": round(ratio, 4),
    }
```

- [ ] **Step 4: Run tests to verify they pass**

Run: `cd backend && PYTHONPATH=. pytest tests/test_materials.py -v`
Expected: 7 PASS

- [ ] **Step 5: Commit**

```bash
git add backend/app/services/analysis/materials.py backend/tests/test_materials.py
git commit -m "feat: add material durability and maintenance sub-analyses"
```

---

### Task 5: analyze_known_issues + analyze_material_compatibility + analyze_material_weight

**Files:**
- Modify: `backend/app/services/analysis/materials.py`
- Modify: `backend/tests/test_materials.py`

- [ ] **Step 1: Write failing tests for all 3 sub-analyses**

Append to `test_materials.py`:

```python
from app.services.analysis.materials import (
    analyze_known_issues,
    analyze_material_compatibility,
    analyze_material_weight,
)


# ---------------------------------------------------------------------------
# analyze_known_issues
# ---------------------------------------------------------------------------


def test_known_issues_none():
    """Materials with no known issues -> score 100."""
    zone_mats = [
        make_zone_material("salon", "floor", 10.0, make_material(known_issues=[])),
    ]
    config = _default_config()
    score, warnings, metrics = analyze_known_issues(zone_mats, config)
    assert score == 100.0
    assert metrics["total_issues"] == 0


def test_known_issues_critical():
    """Material with critical known issue -> low score."""
    zone_mats = [
        make_zone_material("salon", "floor", 10.0, make_material(
            known_issues=[{"issue": "Delamination bei Feuchtigkeit", "severity": "critical"}],
        )),
    ]
    config = _default_config()
    score, warnings, metrics = analyze_known_issues(zone_mats, config)
    assert score < 70.0
    assert any(w["code"] == "KNOWN_ISSUE_CRITICAL" for w in warnings)


def test_known_issues_medium():
    """Material with medium known issue -> partial score reduction."""
    zone_mats = [
        make_zone_material("salon", "floor", 10.0, make_material(
            known_issues=[{"issue": "Verfärbung nach 5 Jahren", "severity": "medium"}],
        )),
    ]
    config = _default_config()
    score, warnings, metrics = analyze_known_issues(zone_mats, config)
    assert score < 100.0
    assert score >= 70.0
    assert any(w["code"] == "KNOWN_ISSUE_MEDIUM" for w in warnings)


def test_known_issues_no_materials():
    """No materials -> score 50, info."""
    config = _default_config()
    score, warnings, metrics = analyze_known_issues([], config)
    assert score == 50.0


# ---------------------------------------------------------------------------
# analyze_material_compatibility
# ---------------------------------------------------------------------------


def test_compatibility_ok():
    """Non-metal materials in same zone -> no issues."""
    zone_mats = [
        make_zone_material("salon", "floor", 10.0, make_material(subcategory="wood")),
        make_zone_material("salon", "wall", 8.0, make_material(subcategory="composite")),
    ]
    config = _default_config()
    score, warnings, metrics = analyze_material_compatibility(zone_mats, config)
    assert score == 100.0
    assert metrics["incompatibility_count"] == 0


def test_compatibility_galvanic():
    """Two different metals in same zone -> galvanic corrosion warning."""
    zone_mats = [
        make_zone_material("engine_room", "wall", 5.0, make_material(
            name="Alu-Platte", subcategory="metal",
            properties={"metal_type": "aluminum"},
        )),
        make_zone_material("engine_room", "ceiling", 5.0, make_material(
            name="Edelstahl-Verkleidung", subcategory="metal",
            properties={"metal_type": "stainless_steel"},
        )),
    ]
    config = _default_config()
    score, warnings, metrics = analyze_material_compatibility(zone_mats, config)
    assert score < 100.0
    assert any(w["code"] == "MATERIAL_INCOMPATIBLE" for w in warnings)
    assert metrics["incompatibility_count"] >= 1


def test_compatibility_no_materials():
    """No materials -> score 50, info."""
    config = _default_config()
    score, warnings, metrics = analyze_material_compatibility([], config)
    assert score == 50.0


# ---------------------------------------------------------------------------
# analyze_material_weight
# ---------------------------------------------------------------------------


def test_weight_normal():
    """Normal weight materials -> score 100."""
    zone_mats = [
        make_zone_material("salon", "floor", 10.0, make_material(
            properties={"density_kg_m3": 650, "thickness_mm": 20},
        )),
    ]
    config = _default_config()  # max_zone_weight_kg_sqm = 30.0
    # Weight = 650 * 0.020 = 13 kg/sqm < 30
    score, warnings, metrics = analyze_material_weight(zone_mats, config)
    assert score == 100.0


def test_weight_heavy():
    """Heavy materials -> warning, lower score."""
    zone_mats = [
        make_zone_material("salon", "floor", 10.0, make_material(
            name="Marmor", properties={"density_kg_m3": 2700, "thickness_mm": 30},
        )),
    ]
    config = _default_config()  # max_zone_weight_kg_sqm = 30.0
    # Weight = 2700 * 0.030 = 81 kg/sqm > 30
    score, warnings, metrics = analyze_material_weight(zone_mats, config)
    assert score < 100.0
    assert any(w["code"] == "MATERIAL_HEAVY" for w in warnings)


def test_weight_no_density():
    """Material without density data -> info, partial score."""
    zone_mats = [
        make_zone_material("salon", "floor", 10.0, make_material(properties={})),
    ]
    config = _default_config()
    score, warnings, metrics = analyze_material_weight(zone_mats, config)
    assert score == 50.0
    assert any(w["severity"] == "info" for w in warnings)


def test_weight_no_materials():
    """No materials -> score 50, info."""
    config = _default_config()
    score, warnings, metrics = analyze_material_weight([], config)
    assert score == 50.0
```

- [ ] **Step 2: Run tests to verify new tests fail**

Run: `cd backend && PYTHONPATH=. pytest tests/test_materials.py::test_known_issues_none -v`
Expected: FAIL — `analyze_known_issues` not defined

- [ ] **Step 3: Implement analyze_known_issues**

Add to `materials.py`:

```python
# ---------------------------------------------------------------------------
# Sub-analysis: Known issues
# ---------------------------------------------------------------------------

_ISSUE_SEVERITY_PENALTY = {
    "critical": 30,
    "high": 20,
    "medium": 10,
    "low": 5,
}


def analyze_known_issues(
    zone_materials: list[dict],
    config: dict,
) -> tuple[float, list[dict], dict]:
    """Cross-reference materials against their known issues database.

    Each material.known_issues is a list of {issue, severity, conditions, source}.
    Higher severity issues cause larger score penalties.

    Returns (score 0-100, warnings, metrics).
    """
    warnings: list[dict] = []

    if not zone_materials:
        warnings.append({
            "code": "ISSUES_NO_MATERIALS",
            "severity": "info",
            "message": "Keine Materialzuweisungen für Problemanalyse vorhanden.",
            "suggestion": "Materialien den Zonen zuweisen.",
        })
        return 50.0, warnings, {"total_issues": 0, "critical_issues": 0}

    total_penalty = 0.0
    total_issues = 0
    critical_issues = 0

    for zm in zone_materials:
        mat = zm["material"]
        issues = mat.get("known_issues") or []

        for issue in issues:
            severity = issue.get("severity", "low")
            penalty = _ISSUE_SEVERITY_PENALTY.get(severity, 5)
            total_penalty += penalty
            total_issues += 1

            if severity in ("critical", "high"):
                critical_issues += 1

            code = f"KNOWN_ISSUE_{severity.upper()}"
            warnings.append({
                "code": code,
                "severity": "critical" if severity == "critical" else "warning",
                "message": (
                    f"Material '{mat.get('name', '?')}' in Zone '{zm['zone_name']}': "
                    f"bekanntes Problem — {issue.get('issue', '?')} "
                    f"(Schwere: {severity})."
                ),
                "suggestion": (
                    f"Alternative zu '{mat.get('name', '?')}' prüfen oder "
                    f"Gegenmaßnahmen planen."
                ),
            })

    score = max(0.0, 100.0 - total_penalty)

    return score, warnings, {
        "total_issues": total_issues,
        "critical_issues": critical_issues,
    }
```

- [ ] **Step 4: Implement analyze_material_compatibility**

Add to `materials.py`:

```python
# ---------------------------------------------------------------------------
# Sub-analysis: Material compatibility
# ---------------------------------------------------------------------------


def analyze_material_compatibility(
    zone_materials: list[dict],
    config: dict,
) -> tuple[float, list[dict], dict]:
    """Check for incompatible material combinations within zones.

    Currently checks: dissimilar metals in the same zone (galvanic corrosion
    risk in marine environment).

    Returns (score 0-100, warnings, metrics).
    """
    warnings: list[dict] = []

    if not zone_materials:
        warnings.append({
            "code": "COMPAT_NO_MATERIALS",
            "severity": "info",
            "message": "Keine Materialzuweisungen für Kompatibilitätsanalyse vorhanden.",
            "suggestion": "Materialien den Zonen zuweisen.",
        })
        return 50.0, warnings, {"incompatibility_count": 0, "zones_checked": 0}

    # Group by zone_name
    by_zone: dict[str, list[dict]] = {}
    for zm in zone_materials:
        by_zone.setdefault(zm["zone_name"], []).append(zm)

    incompatibility_count = 0

    for zone_name, mats in by_zone.items():
        # Check dissimilar metals
        metals = [
            zm for zm in mats
            if zm["material"].get("subcategory") == "metal"
        ]
        if len(metals) >= 2:
            metal_types = set()
            for m in metals:
                mt = m["material"].get("properties", {}).get("metal_type", "unknown")
                metal_types.add(mt)

            if len(metal_types) > 1:
                incompatibility_count += 1
                types_str = ", ".join(sorted(metal_types))
                warnings.append({
                    "code": "MATERIAL_INCOMPATIBLE",
                    "severity": "warning",
                    "message": (
                        f"Zone '{zone_name}': unterschiedliche Metalle ({types_str}) — "
                        f"Risiko galvanischer Korrosion im Salzwasser."
                    ),
                    "suggestion": (
                        f"Gleiche Metallart verwenden oder galvanische Trennung "
                        f"in Zone '{zone_name}' vorsehen."
                    ),
                })

    score = max(0.0, 100.0 - incompatibility_count * 25.0)

    return score, warnings, {
        "incompatibility_count": incompatibility_count,
        "zones_checked": len(by_zone),
    }
```

- [ ] **Step 5: Implement analyze_material_weight**

Add to `materials.py`:

```python
# ---------------------------------------------------------------------------
# Sub-analysis: Material weight
# ---------------------------------------------------------------------------


def analyze_material_weight(
    zone_materials: list[dict],
    config: dict,
) -> tuple[float, list[dict], dict]:
    """Check if material choices add excessive weight per zone.

    Weight per assignment = density_kg_m3 * (thickness_mm / 1000) * area_sqm.
    Aggregated per zone, compared against max_zone_weight_kg_sqm.

    Returns (score 0-100, warnings, metrics).
    """
    warnings: list[dict] = []

    if not zone_materials:
        warnings.append({
            "code": "WEIGHT_NO_MATERIALS",
            "severity": "info",
            "message": "Keine Materialzuweisungen für Gewichtsanalyse vorhanden.",
            "suggestion": "Materialien den Zonen zuweisen.",
        })
        return 50.0, warnings, {"zone_weights_kg_sqm": {}, "heaviest_zone": None}

    max_weight = config.get("max_zone_weight_kg_sqm", 30.0)

    # Accumulate weight per zone (kg/sqm average)
    zone_weight: dict[str, float] = {}
    zone_area: dict[str, float] = {}
    missing_data = 0

    for zm in zone_materials:
        mat = zm["material"]
        props = mat.get("properties") or {}
        density = props.get("density_kg_m3")
        thickness = props.get("thickness_mm")
        area = zm.get("area_sqm", 0.0)

        if density is None or thickness is None:
            missing_data += 1
            continue

        weight_kg = density * (thickness / 1000.0) * area
        zone_name = zm["zone_name"]
        zone_weight[zone_name] = zone_weight.get(zone_name, 0.0) + weight_kg
        zone_area[zone_name] = zone_area.get(zone_name, 0.0) + area

    if not zone_weight:
        if missing_data > 0:
            warnings.append({
                "code": "WEIGHT_NO_DATA",
                "severity": "info",
                "message": (
                    f"{missing_data} Materialzuweisung(en) ohne Dichte-/Dicke-Angaben — "
                    f"Gewichtsanalyse nicht möglich."
                ),
                "suggestion": "Dichte (density_kg_m3) und Dicke (thickness_mm) in Materialeigenschaften ergänzen.",
            })
        return 50.0, warnings, {"zone_weights_kg_sqm": {}, "heaviest_zone": None}

    # Compute kg/sqm per zone
    zone_kg_sqm: dict[str, float] = {}
    for zn in zone_weight:
        if zone_area.get(zn, 0) > 0:
            zone_kg_sqm[zn] = zone_weight[zn] / zone_area[zn]

    heavy_zones = []
    for zn, kg_sqm in zone_kg_sqm.items():
        if kg_sqm > max_weight:
            heavy_zones.append(zn)
            warnings.append({
                "code": "MATERIAL_HEAVY",
                "severity": "warning",
                "message": (
                    f"Zone '{zn}': Materialgewicht {kg_sqm:.1f} kg/m² "
                    f"überschreitet Maximum {max_weight:.0f} kg/m²."
                ),
                "suggestion": f"Leichtere Materialien für Zone '{zn}' in Betracht ziehen.",
            })

    if not heavy_zones:
        score = 100.0
    else:
        score = max(0.0, 100.0 * (1.0 - len(heavy_zones) / len(zone_kg_sqm)))

    heaviest = max(zone_kg_sqm, key=zone_kg_sqm.get) if zone_kg_sqm else None

    return score, warnings, {
        "zone_weights_kg_sqm": {k: round(v, 1) for k, v in zone_kg_sqm.items()},
        "heaviest_zone": heaviest,
    }
```

- [ ] **Step 6: Run tests to verify they pass**

Run: `cd backend && PYTHONPATH=. pytest tests/test_materials.py -v`
Expected: 18 PASS (4 durability + 3 maintenance + 4 known_issues + 3 compatibility + 4 weight)

- [ ] **Step 7: Commit**

```bash
git add backend/app/services/analysis/materials.py backend/tests/test_materials.py
git commit -m "feat: add known issues, compatibility, and weight sub-analyses"
```

---

### Task 6: Orchestrator + integration tests + route handler extension

**Files:**
- Modify: `backend/app/services/analysis/materials.py`
- Modify: `backend/tests/test_materials.py`
- Modify: `backend/app/api/routes/layouts.py`

- [ ] **Step 1: Write failing integration tests**

Append to `test_materials.py`:

```python
from app.services.analysis.materials import run_materials_analysis, SEVERITY_ORDER


# ---------------------------------------------------------------------------
# Integration
# ---------------------------------------------------------------------------


def test_full_materials_analysis():
    """Complete material assignments -> valid result structure with all 5 sub-scores."""
    zone_mats = [
        make_zone_material("salon", "floor", 15.0, make_material(
            name="Teak", lifespan_years=25, cost_per_unit=250.0,
            maintenance_cost_factor=0.02, subcategory="wood",
            properties={"density_kg_m3": 650, "thickness_mm": 20},
        )),
        make_zone_material("cabin", "wall", 12.0, make_material(
            name="Marine-Sperrholz", lifespan_years=20, cost_per_unit=80.0,
            maintenance_cost_factor=0.01, subcategory="wood",
            properties={"density_kg_m3": 550, "thickness_mm": 15},
        )),
        make_zone_material("head", "floor", 3.0, make_material(
            name="Keramikfliese", lifespan_years=30, cost_per_unit=120.0,
            maintenance_cost_factor=0.005, subcategory="composite",
            properties={"density_kg_m3": 2200, "thickness_mm": 8},
        )),
    ]
    result = run_materials_analysis([], [], "cruising_sail", materials=zone_mats)
    assert result["module"] == "materials"
    assert 0 <= result["overall_score"] <= 100
    assert "durability" in result["sub_scores"]
    assert "maintenance" in result["sub_scores"]
    assert "known_issues" in result["sub_scores"]
    assert "compatibility" in result["sub_scores"]
    assert "weight" in result["sub_scores"]
    assert len(result["sub_scores"]) == 5


def test_materials_warnings_sorted():
    """Warnings should be sorted: critical -> warning -> info."""
    zone_mats = [
        make_zone_material("salon", "floor", 10.0, make_material(
            lifespan_years=5,
            known_issues=[{"issue": "Bruch", "severity": "critical"}],
        )),
    ]
    result = run_materials_analysis([], [], "cruising_sail", materials=zone_mats)
    severities = [w["severity"] for w in result["warnings"]]
    order = [SEVERITY_ORDER.get(s, 2) for s in severities]
    assert order == sorted(order)


def test_materials_boat_class_difference():
    """Different boat classes produce different scores."""
    zone_mats = [
        make_zone_material("salon", "floor", 10.0, make_material(
            lifespan_years=18, cost_per_unit=100.0,
            maintenance_cost_factor=0.025,
            properties={"density_kg_m3": 800, "thickness_mm": 25},
        )),
    ]
    result_small = run_materials_analysis([], [], "small_sail", materials=zone_mats)
    result_super = run_materials_analysis([], [], "superyacht", materials=zone_mats)
    # small_sail: min_lifespan=15 (compliant), superyacht: min_lifespan=25 (not compliant)
    assert result_small["overall_score"] != result_super["overall_score"]


def test_materials_config_overrides():
    """Config overrides are applied and stored in config_used."""
    zone_mats = [make_zone_material()]
    result = run_materials_analysis([], [], "cruising_sail", materials=zone_mats,
                                    config_overrides={"min_lifespan_years": 30})
    assert result["config_used"]["min_lifespan_years"] == 30


def test_materials_empty_input():
    """No material assignments -> degraded scores, no crash."""
    result = run_materials_analysis([], [], "cruising_sail", materials=[])
    assert 0 <= result["overall_score"] <= 100
    assert len(result["sub_scores"]) == 5
    assert len(result["warnings"]) > 0
```

- [ ] **Step 2: Run tests to verify they fail**

Run: `cd backend && PYTHONPATH=. pytest tests/test_materials.py::test_full_materials_analysis -v`
Expected: FAIL — `run_materials_analysis` not defined

- [ ] **Step 3: Implement orchestrator**

Add at the bottom of `materials.py`:

```python
# ---------------------------------------------------------------------------
# Orchestrator
# ---------------------------------------------------------------------------


def run_materials_analysis(
    zones: list[dict],
    passages: list[dict],
    boat_class: str,
    config_overrides: dict | None = None,
    materials: list[dict] | None = None,
) -> dict:
    """Orchestrator — runs all material & quality sub-analyses.

    Args:
        zones: Layout zones (unused by this module, kept for API consistency).
        passages: Layout passages (unused by this module, kept for API consistency).
        boat_class: One of small_sail, cruising_sail, large_motor, superyacht.
        config_overrides: Optional dict to override config values.
        materials: List of zone_material dicts with resolved material data.

    Returns a standardized result dict matching the AYDI analysis module contract.
    """
    if boat_class not in BOAT_CLASS_DEFAULTS:
        raise ValueError(f"Unknown boat class: {boat_class}")

    config = BOAT_CLASS_DEFAULTS[boat_class].copy()
    weights = config.pop("weights").copy()

    if config_overrides:
        config.update(config_overrides)

    zone_materials = materials or []

    sub_scores: dict[str, float] = {}
    all_warnings: list[dict] = []
    all_suggestions: list[str] = []
    all_metrics: dict[str, dict] = {}

    analyses = [
        ("durability", lambda: analyze_material_durability(zone_materials, config)),
        ("maintenance", lambda: analyze_maintenance_burden(zone_materials, config)),
        ("known_issues", lambda: analyze_known_issues(zone_materials, config)),
        ("compatibility", lambda: analyze_material_compatibility(zone_materials, config)),
        ("weight", lambda: analyze_material_weight(zone_materials, config)),
    ]

    for name, fn in analyses:
        try:
            score, warnings, metrics = fn()
            sub_scores[name] = score
            all_warnings.extend(warnings)
            all_metrics[name] = metrics
        except Exception:
            logger.exception("Error in materials sub-analysis %s", name)
            sub_scores[name] = 0.0
            all_warnings.append({
                "code": "ANALYSIS_ERROR",
                "severity": "critical",
                "message": f"Fehler bei Materialanalyse: {name}",
                "suggestion": "Materialzuweisungen überprüfen.",
            })

    overall = sum(sub_scores.get(k, 50.0) * w for k, w in weights.items())

    for w in all_warnings:
        suggestion = w.get("suggestion")
        if suggestion and suggestion not in all_suggestions:
            all_suggestions.append(suggestion)

    all_warnings.sort(key=lambda w: SEVERITY_ORDER.get(w.get("severity", "info"), 2))

    return {
        "module": "materials",
        "overall_score": round(overall, 1),
        "sub_scores": {k: round(v, 1) for k, v in sub_scores.items()},
        "warnings": all_warnings,
        "suggestions": all_suggestions,
        "metrics": all_metrics,
        "config_used": config,
    }
```

- [ ] **Step 4: Update layouts.py — add import, register module, add data loader**

In `backend/app/api/routes/layouts.py`:

Add imports at top (after production import):

```python
from sqlalchemy.orm import selectinload
from app.services.analysis.materials import run_materials_analysis
from app.models.models import ZoneMaterial
```

Add to `ANALYSIS_MODULES`:

```python
ANALYSIS_MODULES = {
    "ergonomics": run_ergonomics_analysis,
    "volume_storage": run_volume_storage_analysis,
    "emotional": run_emotional_analysis,
    "compliance": run_compliance_analysis,
    "production": run_production_analysis,
    "materials": run_materials_analysis,
}
```

Add a loader function before `run_analysis`:

```python
async def _load_materials_for_analysis(layout_id: UUID, db: AsyncSession) -> list[dict]:
    """Load zone_material assignments with eagerly-loaded material data."""
    result = await db.execute(
        select(ZoneMaterial)
        .where(ZoneMaterial.layout_id == layout_id)
        .options(selectinload(ZoneMaterial.material))
    )
    zone_mats = result.scalars().all()

    assembled = []
    for zm in zone_mats:
        material = zm.material
        if material:
            assembled.append({
                "zone_name": zm.zone_name,
                "surface_type": zm.surface_type,
                "area_sqm": zm.area_sqm,
                "material": {
                    "name": material.name,
                    "category": material.category,
                    "subcategory": material.subcategory,
                    "cost_per_unit": material.cost_per_unit,
                    "cost_unit": material.cost_unit,
                    "lifespan_years": material.lifespan_years,
                    "maintenance_interval_months": material.maintenance_interval_months,
                    "maintenance_cost_factor": material.maintenance_cost_factor,
                    "known_issues": material.known_issues or [],
                    "properties": material.properties or {},
                },
            })
    return assembled
```

In the `run_analysis` endpoint, update the analysis call section (between loading the layout and creating db_result):

```python
    # Load extra data for modules that need it
    extra_kwargs: dict = {}
    if data.module == "materials":
        extra_kwargs["materials"] = await _load_materials_for_analysis(data.layout_id, db)

    analysis_fn = ANALYSIS_MODULES[data.module]
    analysis_result = analysis_fn(
        zones, passages, project.boat_class,
        config_overrides=data.config_overrides,
        **extra_kwargs,
    )
```

- [ ] **Step 5: Run all tests to verify everything passes**

Run: `cd backend && PYTHONPATH=. pytest tests/ -v`
Expected: All tests pass (~149: 126 existing + 23 new material tests)

- [ ] **Step 6: Commit**

```bash
git add backend/app/services/analysis/materials.py backend/tests/test_materials.py backend/app/api/routes/layouts.py
git commit -m "feat: add materials analysis orchestrator and register module"
```

---

## Test Summary

| Sub-analysis | Tests | Coverage |
|---|---|---|
| material_durability | 4 | all compliant, short-lived, no data, no materials |
| maintenance_burden | 3 | low cost, high cost, no materials |
| known_issues | 4 | no issues, critical issue, medium issue, no materials |
| material_compatibility | 3 | compatible, galvanic corrosion, no materials |
| material_weight | 4 | normal, heavy, no density, no materials |
| integration | 5 | full layout, warnings sorted, boat class diff, overrides, empty |
| **Total** | **23** | |
