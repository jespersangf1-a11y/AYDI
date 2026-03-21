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
        "max_annualized_cost_per_sqm": 50,
        "weights": {
            "durability": 0.25,
            "maintenance": 0.21,
            "known_issues": 0.17,
            "compatibility": 0.13,
            "weight": 0.09,
            "lifecycle_cost": 0.08,
            "uv_exposure": 0.04,
            "moisture_risk": 0.03,
        },
    },
    "cruising_sail": {
        "min_lifespan_years": 20,
        "max_annual_maintenance_pct": 0.025,
        "max_zone_weight_kg_sqm": 30.0,
        "max_annualized_cost_per_sqm": 75,
        "weights": {
            "durability": 0.21,
            "maintenance": 0.21,
            "known_issues": 0.17,
            "compatibility": 0.13,
            "weight": 0.13,
            "lifecycle_cost": 0.08,
            "uv_exposure": 0.04,
            "moisture_risk": 0.03,
        },
    },
    "large_motor": {
        "min_lifespan_years": 20,
        "max_annual_maintenance_pct": 0.02,
        "max_zone_weight_kg_sqm": 35.0,
        "max_annualized_cost_per_sqm": 100,
        "weights": {
            "durability": 0.17,
            "maintenance": 0.21,
            "known_issues": 0.21,
            "compatibility": 0.13,
            "weight": 0.13,
            "lifecycle_cost": 0.08,
            "uv_exposure": 0.04,
            "moisture_risk": 0.03,
        },
    },
    "racing_sail": {
        "min_lifespan_years": 12,
        "max_annual_maintenance_pct": 0.04,
        "max_zone_weight_kg_sqm": 20.0,
        "max_annualized_cost_per_sqm": 35,
        "weights": {
            "durability": 0.20,
            "maintenance": 0.20,
            "known_issues": 0.15,
            "compatibility": 0.10,
            "weight": 0.20,
            "lifecycle_cost": 0.08,
            "uv_exposure": 0.04,
            "moisture_risk": 0.03,
        },
    },
    "daysailer": {
        "min_lifespan_years": 14,
        "max_annual_maintenance_pct": 0.035,
        "max_zone_weight_kg_sqm": 24.0,
        "max_annualized_cost_per_sqm": 45,
        "weights": {
            "durability": 0.2449,
            "maintenance": 0.2143,
            "known_issues": 0.1633,
            "compatibility": 0.1224,
            "weight": 0.1020,
            "lifecycle_cost": 0.0816,
            "uv_exposure": 0.0408,
            "moisture_risk": 0.0307,
        },
    },
    "motorsailer": {
        "min_lifespan_years": 18,
        "max_annual_maintenance_pct": 0.027,
        "max_zone_weight_kg_sqm": 32.0,
        "max_annualized_cost_per_sqm": 80,
        "weights": {
            "durability": 0.21,
            "maintenance": 0.21,
            "known_issues": 0.17,
            "compatibility": 0.13,
            "weight": 0.12,
            "lifecycle_cost": 0.08,
            "uv_exposure": 0.04,
            "moisture_risk": 0.03,
        },
    },
    "catamaran_sail": {
        "min_lifespan_years": 18,
        "max_annual_maintenance_pct": 0.028,
        "max_zone_weight_kg_sqm": 28.0,
        "max_annualized_cost_per_sqm": 70,
        "weights": {
            "durability": 0.21,
            "maintenance": 0.21,
            "known_issues": 0.17,
            "compatibility": 0.13,
            "weight": 0.12,
            "lifecycle_cost": 0.08,
            "uv_exposure": 0.04,
            "moisture_risk": 0.03,
        },
    },
    "catamaran_motor": {
        "min_lifespan_years": 20,
        "max_annual_maintenance_pct": 0.022,
        "max_zone_weight_kg_sqm": 33.0,
        "max_annualized_cost_per_sqm": 95,
        "weights": {
            "durability": 0.19,
            "maintenance": 0.20,
            "known_issues": 0.20,
            "compatibility": 0.13,
            "weight": 0.12,
            "lifecycle_cost": 0.08,
            "uv_exposure": 0.04,
            "moisture_risk": 0.03,
        },
    },
    "small_motor": {
        "min_lifespan_years": 18,
        "max_annual_maintenance_pct": 0.025,
        "max_zone_weight_kg_sqm": 32.0,
        "max_annualized_cost_per_sqm": 85,
        "weights": {
            "durability": 0.19,
            "maintenance": 0.21,
            "known_issues": 0.20,
            "compatibility": 0.13,
            "weight": 0.12,
            "lifecycle_cost": 0.08,
            "uv_exposure": 0.04,
            "moisture_risk": 0.03,
        },
    },
    "sport_cruiser": {
        "min_lifespan_years": 20,
        "max_annual_maintenance_pct": 0.020,
        "max_zone_weight_kg_sqm": 35.0,
        "max_annualized_cost_per_sqm": 110,
        "weights": {
            "durability": 0.18,
            "maintenance": 0.20,
            "known_issues": 0.21,
            "compatibility": 0.14,
            "weight": 0.13,
            "lifecycle_cost": 0.08,
            "uv_exposure": 0.04,
            "moisture_risk": 0.03,
        },
    },
    "trawler": {
        "min_lifespan_years": 22,
        "max_annual_maintenance_pct": 0.019,
        "max_zone_weight_kg_sqm": 36.0,
        "max_annualized_cost_per_sqm": 120,
        "weights": {
            "durability": 0.18,
            "maintenance": 0.19,
            "known_issues": 0.21,
            "compatibility": 0.14,
            "weight": 0.13,
            "lifecycle_cost": 0.08,
            "uv_exposure": 0.04,
            "moisture_risk": 0.03,
        },
    },
    "explorer": {
        "min_lifespan_years": 25,
        "max_annual_maintenance_pct": 0.017,
        "max_zone_weight_kg_sqm": 38.0,
        "max_annualized_cost_per_sqm": 135,
        "weights": {
            "durability": 0.17,
            "maintenance": 0.18,
            "known_issues": 0.21,
            "compatibility": 0.16,
            "weight": 0.13,
            "lifecycle_cost": 0.08,
            "uv_exposure": 0.04,
            "moisture_risk": 0.03,
        },
    },
    "superyacht": {
        "min_lifespan_years": 25,
        "max_annual_maintenance_pct": 0.015,
        "max_zone_weight_kg_sqm": 40.0,
        "max_annualized_cost_per_sqm": 150,
        "weights": {
            "durability": 0.17,
            "maintenance": 0.17,
            "known_issues": 0.21,
            "compatibility": 0.17,
            "weight": 0.13,
            "lifecycle_cost": 0.08,
            "uv_exposure": 0.04,
            "moisture_risk": 0.03,
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


# ---------------------------------------------------------------------------
# Sub-analysis: Known issues
# ---------------------------------------------------------------------------

_ISSUE_SEVERITY_PENALTY = {
    "critical": 35,
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


# ---------------------------------------------------------------------------
# Sub-analysis: Lifecycle cost
# ---------------------------------------------------------------------------


def analyze_lifecycle_cost(
    zone_materials: list[dict],
    config: dict,
) -> tuple[float, list[dict], dict]:
    """Estimate 20-year total cost of ownership per material.

    Considers purchase cost, annual maintenance, and replacement cycles.

    Returns (score 0-100, warnings, metrics).
    """
    warnings: list[dict] = []

    if not zone_materials:
        warnings.append({
            "severity": "info",
            "message": "Keine Materialzuweisungen für Lebenszykluskosten-Analyse vorhanden.",
            "suggestion": "Materialien den Zonen zuweisen.",
        })
        return 50.0, warnings, {
            "total_lifecycle_cost_eur": 0.0,
            "annualized_cost_eur": 0.0,
            "total_area_sqm": 0.0,
        }

    max_annualized = config.get("max_annualized_cost_per_sqm", 50)
    lifecycle_costs: list[float] = []
    total_area = 0.0

    for zm in zone_materials:
        mat = zm["material"]
        area = zm.get("area_sqm", 0.0)
        cost_per_unit = mat.get("cost_per_unit", 0.0)
        maintenance_factor = mat.get("maintenance_cost_factor", 0.0)
        lifespan = mat.get("lifespan_years", 20)

        purchase = area * cost_per_unit
        annual_maintenance = purchase * maintenance_factor
        replacements = max(0, (20 // lifespan) - 1) if lifespan and lifespan > 0 else 0
        replacement_cost = replacements * purchase * 0.8
        lifecycle_total = purchase + (annual_maintenance * 20) + replacement_cost

        lifecycle_costs.append(lifecycle_total)
        total_area += area

    total_lifecycle = sum(lifecycle_costs)
    annualized = total_lifecycle / 20.0

    # Check for outliers: any single material > 3× average
    if lifecycle_costs:
        avg_cost = total_lifecycle / len(lifecycle_costs)
        for i, zm in enumerate(zone_materials):
            if avg_cost > 0 and lifecycle_costs[i] > 3.0 * avg_cost:
                mat = zm["material"]
                warnings.append({
                    "severity": "warning",
                    "message": (
                        f"Material '{mat.get('name', '?')}' in Zone '{zm['zone_name']}': "
                        f"Lebenszykluskosten ({lifecycle_costs[i]:.0f} EUR) überschreiten "
                        f"das 3-fache des Durchschnitts ({avg_cost:.0f} EUR)."
                    ),
                    "suggestion": (
                        f"Günstigere Alternative zu '{mat.get('name', '?')}' prüfen oder "
                        f"Material mit längerer Lebensdauer wählen."
                    ),
                })

    # Score based on annualized cost per sqm
    if total_area > 0:
        annualized_per_sqm = annualized / total_area
        if annualized_per_sqm <= max_annualized:
            score = 100.0
        else:
            score = max(0.0, (max_annualized / annualized_per_sqm) * 100.0)
    else:
        score = 50.0

    return score, warnings, {
        "total_lifecycle_cost_eur": round(total_lifecycle, 2),
        "annualized_cost_eur": round(annualized, 2),
        "total_area_sqm": round(total_area, 2),
    }


# ---------------------------------------------------------------------------
# Sub-analysis: UV exposure risk
# ---------------------------------------------------------------------------

_HIGH_UV_ZONE_TYPES = {"cockpit", "flybridge", "foredeck", "swim_platform"}


def analyze_uv_exposure(
    zone_materials: list[dict],
    config: dict,
) -> tuple[float, list[dict], dict]:
    """Flag materials in high-UV zones without UV resistance.

    Returns (score 0-100, warnings, metrics).
    """
    warnings: list[dict] = []

    if not zone_materials:
        warnings.append({
            "severity": "info",
            "message": "Keine Materialzuweisungen für UV-Analyse vorhanden.",
            "suggestion": "Materialien den Zonen zuweisen.",
        })
        return 50.0, warnings, {"uv_zones_checked": 0, "non_uv_resistant_count": 0}

    non_uv_resistant_count = 0
    uv_zones_checked = 0

    for zm in zone_materials:
        zone_type = zm.get("zone_type")
        if zone_type is None:
            continue

        if zone_type not in _HIGH_UV_ZONE_TYPES:
            continue

        uv_zones_checked += 1
        mat = zm["material"]
        mat_props = mat.get("properties") or {}
        uv_resistant = mat_props.get("uv_resistant", True)

        if not uv_resistant:
            non_uv_resistant_count += 1
            warnings.append({
                "severity": "warning",
                "message": (
                    f"Material '{mat.get('name', '?')}' in Zone '{zm['zone_name']}' "
                    f"(Typ: {zone_type}): nicht UV-beständig in sonnenexponiertem Bereich."
                ),
                "suggestion": (
                    f"UV-beständiges Material für Zone '{zm['zone_name']}' wählen oder "
                    f"UV-Schutzbehandlung vorsehen."
                ),
            })

    score = max(0.0, min(100.0, 100.0 - non_uv_resistant_count * 20))

    return score, warnings, {
        "uv_zones_checked": uv_zones_checked,
        "non_uv_resistant_count": non_uv_resistant_count,
    }


# ---------------------------------------------------------------------------
# Sub-analysis: Moisture risk
# ---------------------------------------------------------------------------

_HIGH_MOISTURE_ZONE_TYPES = {"head", "pantry", "engine", "storage"}
_WOOD_SUBCATEGORIES = {"wood", "plywood", "veneer"}


def analyze_moisture_risk(
    zone_materials: list[dict],
    config: dict,
) -> tuple[float, list[dict], dict]:
    """Flag wood-based materials in high-moisture zones without moisture sealing.

    Returns (score 0-100, warnings, metrics).
    """
    warnings: list[dict] = []

    if not zone_materials:
        warnings.append({
            "severity": "info",
            "message": "Keine Materialzuweisungen für Feuchtigkeitsrisiko-Analyse vorhanden.",
            "suggestion": "Materialien den Zonen zuweisen.",
        })
        return 50.0, warnings, {"moisture_zones_checked": 0, "unsealed_count": 0}

    unsealed_count = 0
    moisture_zones_checked = 0

    for zm in zone_materials:
        zone_type = zm.get("zone_type")
        if zone_type is None:
            continue

        if zone_type not in _HIGH_MOISTURE_ZONE_TYPES:
            continue

        mat = zm["material"]
        subcategory = mat.get("subcategory")
        if subcategory not in _WOOD_SUBCATEGORIES:
            continue

        moisture_zones_checked += 1
        mat_props = mat.get("properties") or {}
        moisture_sealed = mat_props.get("moisture_sealed", False)

        if not moisture_sealed:
            unsealed_count += 1
            warnings.append({
                "severity": "warning",
                "message": (
                    f"Material '{mat.get('name', '?')}' ({subcategory}) in Zone "
                    f"'{zm['zone_name']}' (Typ: {zone_type}): Holzwerkstoff ohne "
                    f"Feuchtigkeitsversiegelung in feuchtem Bereich."
                ),
                "suggestion": (
                    f"Feuchtigkeitsversiegelung für '{mat.get('name', '?')}' in Zone "
                    f"'{zm['zone_name']}' vorsehen oder feuchtigkeitsresistentes Material wählen."
                ),
            })

    score = max(0.0, min(100.0, 100.0 - unsealed_count * 15))

    return score, warnings, {
        "moisture_zones_checked": moisture_zones_checked,
        "unsealed_count": unsealed_count,
    }


# ---------------------------------------------------------------------------
# Orchestrator
# ---------------------------------------------------------------------------


def run_materials_analysis(
    zones: list[dict],
    passages: list[dict],
    boat_class: str,
    config_overrides: dict | None = None,
    materials: list[dict] | None = None,
    data_source: str = "measured",
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
        ("lifecycle_cost", lambda: analyze_lifecycle_cost(zone_materials, config)),
        ("uv_exposure", lambda: analyze_uv_exposure(zone_materials, config)),
        ("moisture_risk", lambda: analyze_moisture_risk(zone_materials, config)),
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
        "confidence": data_source,
        "confidence_note": "Basiert auf geschätzten Werten aus öffentlichen Spezifikationen." if data_source == "estimated" else None,
    }
