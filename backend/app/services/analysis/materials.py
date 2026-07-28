"""Material & quality analysis module for yacht layouts.

Evaluates material choices for durability, maintenance burden, known issues,
compatibility, and weight impact. Pure function module — no database access.
All user-facing strings are in German.
"""
import logging
from app.services.analysis.scoring import weighted_overall, hinweis_teilanalysen

logger = logging.getLogger(__name__)

# Try to import knowledge databases for enriched analysis
try:
    from app.services.knowledge.hull_construction_deep import (
        RESIN_DATABASE,
        FIBER_DATABASE,
        CORE_MATERIALS_DATABASE,
    )
except ImportError:
    RESIN_DATABASE = {}
    FIBER_DATABASE = {}
    CORE_MATERIALS_DATABASE = {}

try:
    from app.services.knowledge.aging_lifecycle_manufacturers_deep import (
        MATERIAL_LIFESPAN_DATABASE,
    )
except ImportError:
    MATERIAL_LIFESPAN_DATABASE = {}

try:
    from app.services.knowledge.keel_rudder_underwater_deep import (
        ANTIFOULING_DATABASE,
    )
except ImportError:
    ANTIFOULING_DATABASE = {}

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
) -> tuple[float | None, list[dict], dict]:
    """Estimate annual maintenance cost and compare to benchmark.

    Annual maintenance per assignment = area_sqm * cost_per_unit * maintenance_cost_factor.
    Total is compared against max_annual_maintenance_pct * total_material_cost.

    Returns (score 0-100 oder None, warnings, metrics). ``None`` bedeutet
    "nicht beurteilbar" — es lag keine verwertbare Kostenangabe vor.
    """
    warnings: list[dict] = []

    if not zone_materials:
        warnings.append({
            "code": "MAINTENANCE_NO_MATERIALS",
            "severity": "info",
            "message": "Keine Materialzuweisungen für Wartungskosten-Analyse vorhanden.",
            "suggestion": "Materialien den Zonen zuweisen.",
            "location": "layout.materials",
        })
        # Ohne Materialzuweisung gibt es keine Wartungskosten zu pruefen. Die
        # bisherige 50.0 war eine Zahl ohne Messung und ging voll gewichtet in
        # die Modulnote ein.
        return None, warnings, {
            "annual_maintenance_eur": None,
            "total_material_cost_eur": None,
            "maintenance_ratio": None,
        }

    max_pct = config.get("max_annual_maintenance_pct", 0.025)

    total_material_cost = 0.0
    annual_maintenance = 0.0
    # Zuweisungen ohne Kosten- oder Wartungsfaktor werden gezaehlt, nicht
    # stillschweigend mit 0.0 gerechnet: ein fehlender Wartungsfaktor haette
    # als "verursacht keine Wartungskosten" gezaehlt und das Verhaeltnis
    # guenstiger aussehen lassen, als es gemessen ist.
    ohne_kostenangabe: list[str] = []
    ohne_wartungsfaktor: list[str] = []
    bewertete_zuweisungen = 0

    for zm in zone_materials:
        mat = zm["material"]
        area = zm.get("area_sqm") or 0.0
        cost = mat.get("cost_per_unit")
        factor = mat.get("maintenance_cost_factor")
        bezeichnung = f"{mat.get('name', '?')} ({zm.get('zone_name', '?')})"

        if cost is None:
            ohne_kostenangabe.append(bezeichnung)
            continue
        if factor is None:
            ohne_wartungsfaktor.append(bezeichnung)
            continue

        mat_cost = area * cost
        total_material_cost += mat_cost
        annual_maintenance += mat_cost * factor
        bewertete_zuweisungen += 1

    if ohne_kostenangabe or ohne_wartungsfaktor:
        fehlend = ohne_kostenangabe + ohne_wartungsfaktor
        warnings.append({
            "code": "MAINTENANCE_DATA_INCOMPLETE",
            "severity": "info",
            "message": (
                "Für folgende Materialzuweisungen fehlt eine Kosten- oder "
                "Wartungsfaktor-Angabe; sie sind in der Wartungskosten-Analyse "
                f"nicht enthalten: {', '.join(fehlend)}."
            ),
            "suggestion": (
                "Preis je Einheit und Wartungsfaktor im Materialstamm "
                "nachtragen, damit die Wartungslast vollständig gerechnet wird."
            ),
            "location": "layout.materials",
        })

    if bewertete_zuweisungen == 0:
        warnings.append({
            "code": "MAINTENANCE_NOT_ASSESSABLE",
            "severity": "info",
            "message": (
                "Wartungskosten nicht beurteilbar: keine der Materialzuweisungen "
                "trägt Kosten- und Wartungsfaktor-Angaben."
            ),
            "suggestion": "Materialstammdaten um Preis und Wartungsfaktor ergänzen.",
            "location": "layout.materials",
        })
        return None, warnings, {
            "annual_maintenance_eur": None,
            "total_material_cost_eur": None,
            "maintenance_ratio": None,
        }

    if total_material_cost <= 0:
        # Kostensumme null trotz vorhandener Angaben: entweder alle Flaechen 0
        # oder alle Preise 0. Ein Verhaeltnis ist daraus nicht bildbar.
        warnings.append({
            "code": "MAINTENANCE_NOT_ASSESSABLE",
            "severity": "info",
            "message": (
                "Wartungskosten nicht beurteilbar: die Materialkosten des Layouts "
                "summieren sich auf 0 EUR (fehlende Flächen- oder Preisangaben)."
            ),
            "suggestion": "Flächen je Zuweisung und Preis je Einheit prüfen.",
            "location": "layout.materials",
        })
        return None, warnings, {
            "annual_maintenance_eur": None,
            "total_material_cost_eur": None,
            "maintenance_ratio": None,
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

    Also enriches with knowledge from RESIN_DATABASE, FIBER_DATABASE,
    CORE_MATERIALS_DATABASE for known marine material failure modes.

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

        # Enrich with knowledge database if available
        mat_name = mat.get("name", "").lower()
        mat_category = mat.get("category", "").lower()
        mat_subcat = mat.get("subcategory", "").lower()

        # Check resin knowledge for GFK/FRP materials
        if "gfk" in mat_category or "fiberglass" in mat_name or "polyester" in mat_name:
            if "orthophthalic" in mat_name.lower() and RESIN_DATABASE:
                ortho = RESIN_DATABASE.get("orthophthalic_polyester", {})
                if ortho.get("osmosis_mechanism"):
                    total_penalty += 15
                    total_issues += 1
                    critical_issues += 1
                    warnings.append({
                        "code": "KNOWLEDGE_OSMOSIS_RISK",
                        "severity": "critical",
                        "message": (
                            f"Material '{mat.get('name', '?')}' in Zone '{zm['zone_name']}': "
                            f"Orthophthalsäure-Polyester hat erhöhtes Osmose-Risiko "
                            f"(Beginn typisch 10-15 Jahre bei Dauergewässerung)."
                        ),
                        "suggestion": (
                            f"Isophthalsäure-Polyester oder Vinylester-Laminat "
                            f"in Feuchtzonen für Zone '{zm['zone_name']}' bevorzugen."
                        ),
                    })
            elif "vinylester" in mat_name.lower() and RESIN_DATABASE:
                vinyl = RESIN_DATABASE.get("vinylester", {})
                if vinyl.get("barrier_vs_full_hull"):
                    # Vinylester is good - no penalty, but add info if relevant
                    pass

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
                # ``or {}``: ein Material ohne gepflegte Eigenschaften traegt
                # properties = None, nicht ein fehlendes Feld.
                mt = (m["material"].get("properties") or {}).get("metal_type", "unknown")
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
) -> tuple[float | None, list[dict], dict]:
    """Estimate 20-year total cost of ownership per material.

    Considers purchase cost, annual maintenance, and replacement cycles.
    Uses MATERIAL_LIFESPAN_DATABASE to validate and enrich lifespan estimates.

    Returns (score 0-100, warnings, metrics).
    """
    warnings: list[dict] = []

    if not zone_materials:
        warnings.append({
            "severity": "info",
            "message": "Keine Materialzuweisungen für Lebenszykluskosten-Analyse vorhanden.",
            "suggestion": "Materialien den Zonen zuweisen.",
        })
        # Ohne Materialzuweisung gibt es keine Lebenszykluskosten zu rechnen.
        return None, warnings, {
            "total_lifecycle_cost_eur": None,
            "annualized_cost_eur": None,
            "total_area_sqm": None,
        }

    max_annualized = config.get("max_annualized_cost_per_sqm", 50)
    lifecycle_costs: list[float] = []
    bewertete_zuweisungen: list[dict] = []
    # Fehlende Stammdaten werden gesammelt statt durch guenstige Vorgabewerte
    # ersetzt: cost_per_unit=0.0 machte ein Material kostenlos,
    # maintenance_cost_factor=0.0 wartungsfrei und lifespan_years=20 traf genau
    # das 20-Jahres-Fenster, sodass rechnerisch nie ein Ersatz anfiel. Alle drei
    # Vorgaben waren jeweils das guenstigste denkbare Ergebnis.
    ohne_stammdaten: list[str] = []
    total_area = 0.0

    for zm in zone_materials:
        mat = zm["material"]
        area = zm.get("area_sqm") or 0.0
        cost_per_unit = mat.get("cost_per_unit")
        maintenance_factor = mat.get("maintenance_cost_factor")
        lifespan = mat.get("lifespan_years")

        # Try to enrich lifespan from knowledge database
        mat_name = (mat.get("name") or "").lower()
        if MATERIAL_LIFESPAN_DATABASE:
            for mat_key, mat_data in MATERIAL_LIFESPAN_DATABASE.items():
                if mat_key.lower() in mat_name or mat_name in mat_key.lower():
                    # Use knowledge database lifespan if available
                    known_lifespan = mat_data.get("typical_lifespan_years")
                    if known_lifespan:
                        # Parse if it's a string like "50+"
                        try:
                            if isinstance(known_lifespan, str):
                                lifespan = int(known_lifespan.rstrip("+"))
                            else:
                                lifespan = known_lifespan
                        except (ValueError, TypeError):
                            pass
                    break

        bezeichnung = f"{mat.get('name', '?')} ({zm.get('zone_name', '?')})"
        if cost_per_unit is None or maintenance_factor is None or lifespan is None:
            ohne_stammdaten.append(bezeichnung)
            continue

        purchase = area * cost_per_unit
        annual_maintenance = purchase * maintenance_factor
        replacements = max(0, (20 // lifespan) - 1) if lifespan > 0 else 0
        replacement_cost = replacements * purchase * 0.8
        lifecycle_total = purchase + (annual_maintenance * 20) + replacement_cost

        lifecycle_costs.append(lifecycle_total)
        bewertete_zuweisungen.append(zm)
        total_area += area

    if ohne_stammdaten:
        warnings.append({
            "code": "LIFECYCLE_DATA_INCOMPLETE",
            "severity": "info",
            "message": (
                "Für folgende Materialzuweisungen fehlen Preis, Wartungsfaktor "
                "oder Lebensdauer; sie sind in der Lebenszykluskosten-Rechnung "
                f"nicht enthalten: {', '.join(ohne_stammdaten)}."
            ),
            "suggestion": (
                "Preis je Einheit, Wartungsfaktor und Lebensdauer im "
                "Materialstamm nachtragen."
            ),
            "location": "layout.materials",
        })

    if not lifecycle_costs:
        warnings.append({
            "code": "LIFECYCLE_NOT_ASSESSABLE",
            "severity": "info",
            "message": (
                "Lebenszykluskosten nicht beurteilbar: keine der "
                "Materialzuweisungen trägt vollständige Kostenstammdaten."
            ),
            "suggestion": "Materialstammdaten vervollständigen.",
            "location": "layout.materials",
        })
        return None, warnings, {
            "total_lifecycle_cost_eur": None,
            "annualized_cost_eur": None,
            "total_area_sqm": None,
        }

    total_lifecycle = sum(lifecycle_costs)
    annualized = total_lifecycle / 20.0

    # Check for outliers: any single material > 3× average
    if lifecycle_costs:
        avg_cost = total_lifecycle / len(lifecycle_costs)
        for i, zm in enumerate(bewertete_zuweisungen):
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
        # Ohne Flaechenangabe laesst sich kein Kostenwert je Quadratmeter
        # bilden. Die bisherige 50.0 war eine Zahl ohne Bezugsgroesse.
        warnings.append({
            "code": "LIFECYCLE_NOT_ASSESSABLE",
            "severity": "info",
            "message": (
                "Lebenszykluskosten nicht beurteilbar: für die bewerteten "
                "Materialzuweisungen ist keine Fläche hinterlegt."
            ),
            "suggestion": "Fläche (area_sqm) je Materialzuweisung erfassen.",
            "location": "layout.materials",
        })
        score = None

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
) -> tuple[float | None, list[dict], dict]:
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
        return None, warnings, {"uv_zones_checked": 0, "non_uv_resistant_count": 0}

    non_uv_resistant_count = 0
    uv_zones_checked = 0
    ohne_uv_angabe: list[str] = []
    uv_zonen_gefunden = 0

    for zm in zone_materials:
        zone_type = zm.get("zone_type")
        if zone_type is None:
            continue

        if zone_type not in _HIGH_UV_ZONE_TYPES:
            continue

        uv_zonen_gefunden += 1

        mat = zm["material"]
        mat_props = mat.get("properties") or {}
        # Fruehere Fassung: mat_props.get("uv_resistant", True). Ein Material ohne
        # Angabe galt damit als UV-bestaendig — die guenstigste Annahme, und keine
        # Messung. Fehlt die Angabe, wird das Material nicht mitgezaehlt und der
        # Anwender darauf hingewiesen.
        uv_resistant = mat_props.get("uv_resistant")
        if uv_resistant is None:
            ohne_uv_angabe.append(f"{mat.get('name', '?')} ({zm['zone_name']})")
            continue

        uv_zones_checked += 1

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

    if ohne_uv_angabe:
        warnings.append({
            "code": "UV_RESISTANCE_UNKNOWN",
            "severity": "info",
            "message": (
                "UV-Beständigkeit nicht angegeben für: "
                + ", ".join(ohne_uv_angabe)
                + ". Diese Materialien gehen nicht in die Bewertung ein."
            ),
            "suggestion": (
                "Eigenschaft uv_resistant beim Material hinterlegen."
            ),
            "location": "materials",
        })

    if uv_zonen_gefunden == 0:
        warnings.append({
            "code": "UV_NOT_ASSESSABLE",
            "severity": "info",
            "message": (
                "Keine sonnenexponierten Zonen mit Materialzuweisung gefunden — "
                "die UV-Belastung konnte nicht bewertet werden."
            ),
            "suggestion": (
                "Materialien den Decksbereichen (cockpit, foredeck, side_deck, "
                "flybridge, swim_platform) zuweisen."
            ),
            "location": "materials",
        })
        return None, warnings, {"uv_zones_checked": 0, "non_uv_resistant_count": 0}

    if uv_zones_checked == 0:
        # Zonen vorhanden, aber zu keinem Material eine UV-Angabe.
        return None, warnings, {"uv_zones_checked": 0, "non_uv_resistant_count": 0}

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
) -> tuple[float | None, list[dict], dict]:
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
        return None, warnings, {"moisture_zones_checked": 0, "unsealed_count": 0}

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

    if moisture_zones_checked == 0:
        warnings.append({
            "code": "MOISTURE_NOT_ASSESSABLE",
            "severity": "info",
            "message": (
                "Keine Holzwerkstoffe in feuchtebelasteten Zonen (Nasszelle, "
                "Pantry, Maschinenraum, Stauraum) gefunden — das Feuchterisiko "
                "konnte nicht bewertet werden."
            ),
            "suggestion": (
                "Materialzuweisungen für diese Zonen erfassen, sofern vorhanden."
            ),
            "location": "materials",
        })
        return None, warnings, {"moisture_zones_checked": 0, "unsealed_count": 0}

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
        return {"available": False, "reason": f"Unbekannte Bootsklasse: {boat_class}"}

    config = BOAT_CLASS_DEFAULTS[boat_class].copy()
    weights = config.pop("weights").copy()

    if config_overrides:
        config.update(config_overrides)

    zone_materials = materials or []

    # Anders als die uebrigen Module hatte dieses gar keinen Zweig fuer den Fall
    # ohne Daten: jede der acht Teilanalysen gab einzeln 50.0 zurueck, woraus
    # sich ein Gesamtwert von genau 50.0 ergab. Der sah nach einem Ergebnis aus
    # und war doch nur die Abwesenheit von Materialzuweisungen.
    if not zone_materials:
        return {
            "module": "materials",
            "available": False,
            "reason": (
                "Keine Materialzuweisungen vorhanden — Haltbarkeit, Wartungsaufwand "
                "und Lebenszykluskosten setzen zugewiesene Materialien voraus."
            ),
            "suggestions": [
                "Den Zonen Materialien zuweisen, um die Materialanalyse zu aktivieren."
            ],
        }

    sub_scores: dict[str, float | None] = {}
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

    # Teilanalysen ohne Datengrundlage geben None zurueck und bleiben aus der
    # Rechnung heraus; ihr Gewicht verteilt sich auf die geprueften. Frueher
    # ging hier ein Vorgabewert ein — bei fehlenden Eintraegen 0.0 bzw. 50.0 —
    # und erzeugte eine Note fuer etwas, das nie geprueft wurde.
    overall, _nicht_bewertet = weighted_overall(sub_scores, weights)
    if overall is None:
        return {
            "module": "materials",
            "available": False,
            "reason": "Keine der Teilanalysen konnte mangels Datengrundlage durchgeführt werden.",
            "suggestions": [
                "Layout- und Stammdaten vervollständigen, um eine Bewertung zu ermöglichen."
            ],
        }

    for w in all_warnings:
        suggestion = w.get("suggestion")
        if suggestion and suggestion not in all_suggestions:
            all_suggestions.append(suggestion)

    all_warnings.sort(key=lambda w: SEVERITY_ORDER.get(w.get("severity", "info"), 2))

    return {
        "module": "materials",
        "overall_score": round(overall, 1),
        # Eine Teilanalyse ohne Datengrundlage traegt None — sie wird als
        # solche weitergereicht statt auf eine Zahl gerundet zu werden.
        "sub_scores": {
            k: (round(v, 1) if v is not None else None)
            for k, v in sub_scores.items()
        },
        "warnings": all_warnings,
        "suggestions": all_suggestions,
        "metrics": all_metrics,
        "config_used": config,
        "confidence": data_source,
        "confidence_note": "Basiert auf geschätzten Werten aus öffentlichen Spezifikationen." if data_source == "estimated" else None,
        "coverage_note": hinweis_teilanalysen(_nicht_bewertet),
        "unassessed_sub_analyses": _nicht_bewertet,
    }
