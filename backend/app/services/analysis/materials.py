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
        # Score degrades proportionally: at 2x benchmark -> score 0
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
