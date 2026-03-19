"""Cost estimation analysis module for yacht layouts.

Estimates production cost, identifies cost drivers, evaluates cost distribution,
and quantifies cost risk from uncertain estimates. Pure function module — no database
access. All user-facing strings are in German.
"""
import logging

logger = logging.getLogger(__name__)

BOAT_CLASS_DEFAULTS = {
    "small_sail": {
        "benchmark_cost_per_meter": 20000,  # €/m
        "labor_rate_eur_hour": 55,
        "boat_length_m": 0,
        "ideal_distribution": {
            "material": 0.40,
            "labor": 0.35,
            "equipment": 0.15,
            "overhead": 0.10,
        },
        "parametric_model": {
            "base_cost_per_m": 18000,
            "hull_pct": 0.25,
            "deck_rigging_pct": 0.15,
            "interior_pct": 0.35,
            "systems_pct": 0.15,
            "design_pct": 0.10,
        },
        "weights": {
            "material_costs": 0.23,
            "labor_estimate": 0.18,
            "cost_per_meter": 0.18,
            "distribution": 0.13,
            "risk": 0.18,
            "parametric_estimate": 0.10,
        },
    },
    "cruising_sail": {
        "benchmark_cost_per_meter": 32000,
        "labor_rate_eur_hour": 60,
        "boat_length_m": 0,
        "ideal_distribution": {
            "material": 0.38,
            "labor": 0.35,
            "equipment": 0.17,
            "overhead": 0.10,
        },
        "parametric_model": {
            "base_cost_per_m": 32000,
            "hull_pct": 0.22,
            "deck_rigging_pct": 0.13,
            "interior_pct": 0.38,
            "systems_pct": 0.17,
            "design_pct": 0.10,
        },
        "weights": {
            "material_costs": 0.23,
            "labor_estimate": 0.18,
            "cost_per_meter": 0.18,
            "distribution": 0.13,
            "risk": 0.18,
            "parametric_estimate": 0.10,
        },
    },
    "large_motor": {
        "benchmark_cost_per_meter": 65000,
        "labor_rate_eur_hour": 65,
        "boat_length_m": 0,
        "ideal_distribution": {
            "material": 0.35,
            "labor": 0.30,
            "equipment": 0.20,
            "overhead": 0.15,
        },
        "parametric_model": {
            "base_cost_per_m": 65000,
            "hull_pct": 0.18,
            "deck_rigging_pct": 0.10,
            "interior_pct": 0.40,
            "systems_pct": 0.22,
            "design_pct": 0.10,
        },
        "weights": {
            "material_costs": 0.18,
            "labor_estimate": 0.18,
            "cost_per_meter": 0.23,
            "distribution": 0.13,
            "risk": 0.18,
            "parametric_estimate": 0.10,
        },
    },
    "superyacht": {
        "benchmark_cost_per_meter": 120000,
        "labor_rate_eur_hour": 75,
        "boat_length_m": 0,
        "ideal_distribution": {
            "material": 0.30,
            "labor": 0.30,
            "equipment": 0.25,
            "overhead": 0.15,
        },
        "parametric_model": {
            "base_cost_per_m": 120000,
            "hull_pct": 0.15,
            "deck_rigging_pct": 0.08,
            "interior_pct": 0.42,
            "systems_pct": 0.25,
            "design_pct": 0.10,
        },
        "weights": {
            "material_costs": 0.18,
            "labor_estimate": 0.14,
            "cost_per_meter": 0.22,
            "distribution": 0.18,
            "risk": 0.18,
            "parametric_estimate": 0.10,
        },
    },
}

SEVERITY_ORDER = {"critical": 0, "warning": 1, "info": 2}

# Base labor hours per zone type
_LABOR_HOURS_BY_ZONE_TYPE: dict[str, float] = {
    "engine": 80.0,
    "cabin": 60.0,
    "salon": 50.0,
    "pantry": 40.0,
    "head": 30.0,
    "storage": 15.0,
}
_LABOR_HOURS_DEFAULT = 25.0


# ---------------------------------------------------------------------------
# Helper: compute zone area from polygon (shoelace formula)
# ---------------------------------------------------------------------------


def _polygon_area_sqm(polygon: list[list[float]]) -> float:
    """Return area in square meters from a polygon in mm coordinates."""
    if len(polygon) < 3:
        return 0.0
    n = len(polygon)
    area_mm2 = 0.0
    for i in range(n):
        x1, y1 = polygon[i]
        x2, y2 = polygon[(i + 1) % n]
        area_mm2 += x1 * y2 - x2 * y1
    return abs(area_mm2) / 2.0 / 1_000_000.0  # mm² → m²


# ---------------------------------------------------------------------------
# Sub-analysis 1: Material costs
# ---------------------------------------------------------------------------


def analyze_material_costs(
    cost_items: list[dict],
    config: dict,
) -> tuple[float, list[dict], dict]:
    """Evaluate material cost items.

    Checks that no single material item dominates total cost (>15%).
    Score degrades proportionally above the concentration threshold.

    Args:
        cost_items: List of cost item dicts. Each has keys: category,
            subcategory (optional), quantity, unit, unit_cost_eur,
            total_cost_eur, zone_name (optional), source.
        config: Active analysis config dict.

    Returns:
        Tuple of (score 0-100, list of warning dicts, metrics dict).
    """
    warnings: list[dict] = []

    material_items = [ci for ci in cost_items if ci.get("category") == "material"]

    if not material_items:
        warnings.append({
            "code": "MATERIAL_COST_NO_ITEMS",
            "severity": "info",
            "message": "Keine Materialkostenpositionen vorhanden.",
            "suggestion": "Materialkosten erfassen, um eine aussagekräftige Analyse zu erhalten.",
        })
        return 50.0, warnings, {"total_material_eur": 0.0, "item_count": 0, "concentrated_items": 0}

    total_material = sum(ci.get("total_cost_eur", 0.0) for ci in material_items)

    if total_material <= 0.0:
        warnings.append({
            "code": "MATERIAL_COST_ZERO",
            "severity": "info",
            "message": "Gesamte Materialkosten sind null — Positionen prüfen.",
            "suggestion": "Kosten pro Position (total_cost_eur) korrekt erfassen.",
        })
        return 50.0, warnings, {"total_material_eur": 0.0, "item_count": len(material_items), "concentrated_items": 0}

    concentration_threshold = 0.15
    concentrated_items = 0
    penalty = 0.0

    for ci in material_items:
        item_cost = ci.get("total_cost_eur", 0.0)
        share = item_cost / total_material
        if share > concentration_threshold:
            concentrated_items += 1
            overshoot = share - concentration_threshold
            # Each concentrated item subtracts up to 30 points (at 100% share)
            penalty += overshoot / (1.0 - concentration_threshold) * 30.0
            zone_label = ci.get("zone_name") or ci.get("subcategory") or "?"
            warnings.append({
                "code": "MATERIAL_COST_HIGH",
                "severity": "warning",
                "message": (
                    f"Materialposition '{ci.get('subcategory', zone_label)}' "
                    f"macht {share:.0%} der Gesamtmaterialkosten aus "
                    f"(Richtwert: max. {concentration_threshold:.0%})."
                ),
                "suggestion": (
                    "Kostentreiber prüfen: Alternativmaterialien oder "
                    "Lieferantenvergleich für diese Position durchführen."
                ),
            })

    score = max(0.0, 100.0 - penalty)

    return score, warnings, {
        "total_material_eur": round(total_material, 2),
        "item_count": len(material_items),
        "concentrated_items": concentrated_items,
    }


# ---------------------------------------------------------------------------
# Sub-analysis 2: Labor estimate
# ---------------------------------------------------------------------------


def analyze_labor_estimate(
    zones: list[dict],
    cost_items: list[dict],
    config: dict,
) -> tuple[float, list[dict], dict]:
    """Estimate labor hours from zone types and compare against cost item labor entries.

    Estimated hours are derived from base hours per zone_type. If labor cost items
    are present, the implied hours (total_labor_eur / labor_rate) are compared against
    the estimate. Zones with unusually high complexity are flagged.

    Args:
        zones: Layout zone dicts.
        cost_items: All cost items.
        config: Active config dict.

    Returns:
        Tuple of (score 0-100, warnings, metrics dict).
    """
    warnings: list[dict] = []

    if not zones:
        warnings.append({
            "code": "LABOR_NO_ZONES",
            "severity": "info",
            "message": "Keine Zonen für Arbeitsstunden-Schätzung vorhanden.",
            "suggestion": "Zonen definieren, um Arbeitsaufwand schätzen zu können.",
        })
        return 50.0, warnings, {"estimated_hours": 0.0, "labor_cost_eur": 0.0, "implied_hours": 0.0}

    labor_rate = config.get("labor_rate_eur_hour", 60.0)

    # Estimate hours per zone
    estimated_hours = 0.0
    for zone in zones:
        zone_type = zone.get("zone_type", "other")
        base_hours = _LABOR_HOURS_BY_ZONE_TYPE.get(zone_type, _LABOR_HOURS_DEFAULT)

        # Scale by zone area (relative to a 10 m² baseline)
        polygon = zone.get("polygon")
        if polygon:
            area = _polygon_area_sqm(polygon)
            scale = max(0.5, min(3.0, area / 10.0))
        else:
            scale = 1.0

        zone_hours = base_hours * scale
        estimated_hours += zone_hours

        # Flag labor-intensive individual zones (engine room, complex areas)
        if zone_type == "engine" and zone_hours > 120.0:
            warnings.append({
                "code": "LABOR_INTENSIVE_ZONE",
                "severity": "warning",
                "message": (
                    f"Zone '{zone.get('name', zone_type)}' (Maschinenraum): "
                    f"geschätzter Aufwand {zone_hours:.0f} h — sehr arbeitsintensiv."
                ),
                "suggestion": (
                    "Zugänglichkeit des Maschinenraums verbessern und "
                    "Installationsreihenfolge frühzeitig festlegen."
                ),
            })

    # Implied hours from labor cost items
    labor_items = [ci for ci in cost_items if ci.get("category") == "labor"]
    total_labor_eur = sum(ci.get("total_cost_eur", 0.0) for ci in labor_items)
    implied_hours = total_labor_eur / labor_rate if labor_rate > 0 else 0.0

    # Score: compare implied vs estimated hours (tolerance ±40%)
    if implied_hours > 0 and estimated_hours > 0:
        ratio = implied_hours / estimated_hours
        if 0.6 <= ratio <= 1.4:
            score = 100.0
        elif ratio < 0.6:
            # Significantly fewer hours than estimated → possible underestimate
            deviation = (0.6 - ratio) / 0.6
            score = max(40.0, 100.0 - deviation * 100.0)
            warnings.append({
                "code": "LABOR_UNDERESTIMATE",
                "severity": "warning",
                "message": (
                    f"Kalkulierte Arbeitsstunden ({implied_hours:.0f} h) liegen "
                    f"{(1 - ratio):.0%} unter der Schätzung ({estimated_hours:.0f} h)."
                ),
                "suggestion": (
                    "Arbeitsstunden-Kalkulation überprüfen — mögliche Unterkalkulation."
                ),
            })
        else:
            # More hours than estimated → possible overestimate or complex design
            deviation = (ratio - 1.4) / 1.4
            score = max(40.0, 100.0 - deviation * 60.0)
            warnings.append({
                "code": "LABOR_OVERESTIMATE",
                "severity": "info",
                "message": (
                    f"Kalkulierte Arbeitsstunden ({implied_hours:.0f} h) liegen "
                    f"{(ratio - 1):.0%} über der Schätzung ({estimated_hours:.0f} h)."
                ),
                "suggestion": (
                    "Ursache prüfen: Komplexes Design oder konservative Kalkulation."
                ),
            })
    elif estimated_hours > 0:
        # No labor cost items provided — use estimate as baseline, neutral score
        score = 75.0
    else:
        score = 50.0

    return score, warnings, {
        "estimated_hours": round(estimated_hours, 1),
        "labor_cost_eur": round(total_labor_eur, 2),
        "implied_hours": round(implied_hours, 1),
    }


# ---------------------------------------------------------------------------
# Sub-analysis 3: Cost per meter
# ---------------------------------------------------------------------------


def analyze_cost_per_meter(
    cost_items: list[dict],
    boat_length_m: float,
    config: dict,
) -> tuple[float, list[dict], dict]:
    """Compare total cost per meter LOA against class benchmark.

    Score: 100 if within ±20% of benchmark, linearly degrades outside.
    At ±100% deviation the score reaches 0.

    Args:
        cost_items: All cost items.
        boat_length_m: Length overall in meters.
        config: Active config dict.

    Returns:
        Tuple of (score 0-100, warnings, metrics dict).
    """
    warnings: list[dict] = []

    if not cost_items:
        warnings.append({
            "code": "CPM_NO_COST_ITEMS",
            "severity": "info",
            "message": "Keine Kostenpositionen für Kosten-pro-Meter-Analyse vorhanden.",
            "suggestion": "Kostenpositionen erfassen, um Benchmark-Vergleich zu ermöglichen.",
        })
        return 50.0, warnings, {"total_cost_eur": 0.0, "cost_per_meter": 0.0, "benchmark": 0.0}

    if not boat_length_m or boat_length_m <= 0:
        warnings.append({
            "code": "CPM_NO_LENGTH",
            "severity": "info",
            "message": "Bootslänge fehlt — Kosten-pro-Meter-Analyse nicht möglich.",
            "suggestion": "Bootslänge im Projekt hinterlegen.",
        })
        return 50.0, warnings, {"total_cost_eur": 0.0, "cost_per_meter": 0.0, "benchmark": 0.0}

    total_cost = sum(ci.get("total_cost_eur", 0.0) for ci in cost_items)
    cost_per_meter = total_cost / boat_length_m
    benchmark = config.get("benchmark_cost_per_meter", 32000.0)

    deviation = (cost_per_meter - benchmark) / benchmark  # positive = above

    tolerance = 0.20  # ±20% is score 100
    max_deviation = 1.0  # ±100% is score 0

    abs_dev = abs(deviation)
    if abs_dev <= tolerance:
        score = 100.0
    elif abs_dev >= max_deviation:
        score = 0.0
    else:
        score = 100.0 * (1.0 - (abs_dev - tolerance) / (max_deviation - tolerance))

    if deviation > tolerance:
        warnings.append({
            "code": "COST_ABOVE_BENCHMARK",
            "severity": "warning",
            "message": (
                f"Kosten pro Meter {cost_per_meter:,.0f} €/m liegen "
                f"{deviation:.0%} über dem Klassenrichtwert ({benchmark:,.0f} €/m)."
            ),
            "suggestion": (
                "Kostentreiber identifizieren: Materialspezifikationen, "
                "Ausrüstungsauswahl und Arbeitsstunden prüfen."
            ),
        })
    elif deviation < -tolerance:
        warnings.append({
            "code": "COST_BELOW_BENCHMARK",
            "severity": "info",
            "message": (
                f"Kosten pro Meter {cost_per_meter:,.0f} €/m liegen "
                f"{abs(deviation):.0%} unter dem Klassenrichtwert ({benchmark:,.0f} €/m)."
            ),
            "suggestion": (
                "Prüfen ob Qualitätsstandards und Ausrüstungsumfang vollständig "
                "abgedeckt sind."
            ),
        })

    return score, warnings, {
        "total_cost_eur": round(total_cost, 2),
        "cost_per_meter": round(cost_per_meter, 2),
        "benchmark": benchmark,
        "deviation_pct": round(deviation * 100, 1),
    }


# ---------------------------------------------------------------------------
# Sub-analysis 4: Cost distribution
# ---------------------------------------------------------------------------


def analyze_cost_distribution(
    cost_items: list[dict],
    config: dict,
) -> tuple[float, list[dict], dict]:
    """Check if cost categories are balanced against the ideal distribution.

    Score: 100 - sum of absolute percentage deviations (capped at 0).
    Flags any category that accounts for >50% of total cost.

    Args:
        cost_items: All cost items.
        config: Active config dict (contains ideal_distribution).

    Returns:
        Tuple of (score 0-100, warnings, metrics dict).
    """
    warnings: list[dict] = []

    if not cost_items:
        warnings.append({
            "code": "DIST_NO_COST_ITEMS",
            "severity": "info",
            "message": "Keine Kostenpositionen für Verteilungsanalyse vorhanden.",
            "suggestion": "Kostenpositionen aller Kategorien erfassen.",
        })
        return 50.0, warnings, {"actual_distribution": {}, "ideal_distribution": {}}

    total_cost = sum(ci.get("total_cost_eur", 0.0) for ci in cost_items)

    if total_cost <= 0.0:
        return 50.0, warnings, {"actual_distribution": {}, "ideal_distribution": {}}

    # Aggregate by category
    category_totals: dict[str, float] = {}
    for ci in cost_items:
        cat = ci.get("category", "other")
        category_totals[cat] = category_totals.get(cat, 0.0) + ci.get("total_cost_eur", 0.0)

    actual_distribution = {
        cat: round(amount / total_cost, 4)
        for cat, amount in category_totals.items()
    }

    ideal = config.get("ideal_distribution", {})
    total_deviation = 0.0

    for cat, ideal_share in ideal.items():
        actual_share = actual_distribution.get(cat, 0.0)
        dev = abs(actual_share - ideal_share)
        total_deviation += dev

    score = max(0.0, 100.0 - total_deviation * 100.0)

    # Flag concentrated categories
    concentration_threshold = 0.50
    for cat, share in actual_distribution.items():
        if share > concentration_threshold:
            warnings.append({
                "code": "COST_CONCENTRATION",
                "severity": "warning",
                "message": (
                    f"Kostenkategorie '{cat}' macht {share:.0%} der Gesamtkosten aus "
                    f"(Richtwert: max. {concentration_threshold:.0%})."
                ),
                "suggestion": (
                    f"Kostenstruktur ausbalancieren: Anteil '{cat}' durch "
                    "alternative Lösungen oder Verhandlungen reduzieren."
                ),
            })

    return score, warnings, {
        "actual_distribution": actual_distribution,
        "ideal_distribution": ideal,
        "total_deviation": round(total_deviation, 4),
    }


# ---------------------------------------------------------------------------
# Sub-analysis 5: Cost risk
# ---------------------------------------------------------------------------


def analyze_cost_risk(
    cost_items: list[dict],
    config: dict,
) -> tuple[float, list[dict], dict]:
    """Quantify cost uncertainty by source quality.

    Sources ranked: "quote" (firm offer) > "contract" > "budget" > "estimate" (rough).
    Score: 100 if all items are quotes/contracts, degrades with estimate share.
    Warning when >60% of total cost is based on estimates.

    Args:
        cost_items: All cost items.
        config: Active config dict.

    Returns:
        Tuple of (score 0-100, warnings, metrics dict).
    """
    warnings: list[dict] = []

    if not cost_items:
        warnings.append({
            "code": "RISK_NO_COST_ITEMS",
            "severity": "info",
            "message": "Keine Kostenpositionen für Risikoanalyse vorhanden.",
            "suggestion": "Kostenpositionen mit Quellenangabe erfassen.",
        })
        return 50.0, warnings, {
            "quote_share": 0.0,
            "estimate_share": 0.0,
            "total_cost_eur": 0.0,
        }

    total_cost = sum(ci.get("total_cost_eur", 0.0) for ci in cost_items)

    if total_cost <= 0.0:
        return 50.0, warnings, {
            "quote_share": 0.0,
            "estimate_share": 0.0,
            "total_cost_eur": 0.0,
        }

    # Source quality weights (higher = more reliable)
    _SOURCE_QUALITY: dict[str, float] = {
        "quote": 1.0,
        "contract": 1.0,
        "budget": 0.6,
        "estimate": 0.0,
    }

    reliable_cost = 0.0
    estimate_cost = 0.0

    for ci in cost_items:
        source = ci.get("source", "estimate")
        item_cost = ci.get("total_cost_eur", 0.0)
        quality = _SOURCE_QUALITY.get(source, 0.0)
        reliable_cost += item_cost * quality
        if quality == 0.0:
            estimate_cost += item_cost

    quote_share = reliable_cost / total_cost
    estimate_share = estimate_cost / total_cost

    # Score: linear from 0 (all estimates) to 100 (all quotes)
    score = quote_share * 100.0

    estimate_threshold = 0.60
    if estimate_share > estimate_threshold:
        warnings.append({
            "code": "COST_UNCERTAINTY_HIGH",
            "severity": "warning",
            "message": (
                f"{estimate_share:.0%} der Gesamtkosten basieren auf Schätzwerten "
                f"(Richtwert: max. {estimate_threshold:.0%})."
            ),
            "suggestion": (
                "Verbindliche Angebote für die größten Kostenpositionen einholen, "
                "um Kalkulations-Risiko zu reduzieren."
            ),
        })

    return score, warnings, {
        "quote_share": round(quote_share, 4),
        "estimate_share": round(estimate_share, 4),
        "total_cost_eur": round(total_cost, 2),
    }


# ---------------------------------------------------------------------------
# Sub-analysis 6: Parametric estimate
# ---------------------------------------------------------------------------


def analyze_parametric_estimate(
    zones: list[dict],
    config: dict,
) -> tuple[float, list[dict], dict]:
    """Parametric cost model based on LOA and zone count.

    Computes estimated total cost from boat length and a per-class cost model,
    adjusted by a zone complexity factor.

    Returns (score 0-100, warnings, metrics).
    """
    warnings: list[dict] = []
    boat_length_m = config.get("boat_length_m", 0)
    parametric_model = config.get("parametric_model", {})

    if not boat_length_m or boat_length_m <= 0:
        warnings.append({
            "code": "PARAMETRIC_NO_LENGTH",
            "severity": "info",
            "message": "Bootslänge nicht angegeben — parametrische Schätzung eingeschränkt.",
            "suggestion": "Bootslänge im Projekt hinterlegen für vollständige parametrische Analyse.",
        })
        return 50.0, warnings, {"boat_length_m": 0, "estimated_total_eur": 0.0}

    base_cost_per_m = parametric_model.get("base_cost_per_m", 32000)
    estimated_total = base_cost_per_m * boat_length_m

    # Category breakdown
    category_breakdown = {}
    for key in ("hull_pct", "deck_rigging_pct", "interior_pct", "systems_pct", "design_pct"):
        pct = parametric_model.get(key, 0.0)
        label = key.replace("_pct", "")
        category_breakdown[label] = round(estimated_total * pct, 2)

    # Zone complexity factor
    zone_count = len(zones) if zones else 0
    if zone_count > 0:
        complexity_factor = (zone_count / 6.0) ** 0.3
    else:
        complexity_factor = 1.0

    adjusted_total = estimated_total * complexity_factor

    # Score is always 100 — parametric estimates are informational
    score = 100.0

    return score, warnings, {
        "boat_length_m": boat_length_m,
        "base_cost_per_m": base_cost_per_m,
        "estimated_total_eur": round(estimated_total, 2),
        "complexity_factor": round(complexity_factor, 4),
        "adjusted_total_eur": round(adjusted_total, 2),
        "category_breakdown": category_breakdown,
    }


# ---------------------------------------------------------------------------
# Orchestrator
# ---------------------------------------------------------------------------


def run_cost_analysis(
    zones: list[dict],
    passages: list[dict],
    boat_class: str,
    config_overrides: dict | None = None,
    cost_items: list[dict] | None = None,
    boat_length_m: float = 0.0,
    data_source: str = "measured",
) -> dict:
    """Orchestrator — runs all cost estimation sub-analyses.

    Args:
        zones: Layout zones (used for labor estimation).
        passages: Layout passages (unused, kept for API consistency).
        boat_class: One of small_sail, cruising_sail, large_motor, superyacht.
        config_overrides: Optional dict to override config values.
        cost_items: List of cost item dicts. Each item has keys:
            category (material|labor|equipment|overhead),
            subcategory (optional string),
            quantity (float),
            unit (string, e.g. "piece", "sqm", "hour"),
            unit_cost_eur (float),
            total_cost_eur (float),
            zone_name (optional string),
            source ("quote"|"contract"|"budget"|"estimate").
        boat_length_m: Length overall in meters (needed for cost-per-meter).

    Returns:
        Standardized result dict matching the AYDI analysis module contract.
    """
    if boat_class not in BOAT_CLASS_DEFAULTS:
        raise ValueError(f"Unknown boat class: {boat_class}")

    config = BOAT_CLASS_DEFAULTS[boat_class].copy()
    weights = config.pop("weights").copy()

    if config_overrides:
        config.update(config_overrides)

    # Make boat_length_m available in config for parametric estimate
    config["boat_length_m"] = boat_length_m

    items = cost_items or []

    # Early exit when no cost data at all
    if not items:
        return {
            "module": "cost",
            "overall_score": 50.0,
            "sub_scores": {k: 50.0 for k in weights},
            "warnings": [{
                "code": "COST_NO_DATA",
                "severity": "info",
                "message": "Keine Kostenpositionen vorhanden — Analyse nicht möglich.",
                "suggestion": "Kostenpositionen erfassen, um eine vollständige Kostenkalkulation zu erhalten.",
            }],
            "suggestions": [
                "Kostenpositionen erfassen, um eine vollständige Kostenkalkulation zu erhalten."
            ],
            "metrics": {},
            "config_used": config,
            "confidence": data_source,
            "confidence_note": "Basiert auf geschätzten Werten aus öffentlichen Spezifikationen." if data_source == "estimated" else None,
        }

    sub_scores: dict[str, float] = {}
    all_warnings: list[dict] = []
    all_suggestions: list[str] = []
    all_metrics: dict[str, dict] = {}

    analyses = [
        ("material_costs", lambda: analyze_material_costs(items, config)),
        ("labor_estimate", lambda: analyze_labor_estimate(zones, items, config)),
        ("cost_per_meter", lambda: analyze_cost_per_meter(items, boat_length_m, config)),
        ("distribution", lambda: analyze_cost_distribution(items, config)),
        ("risk", lambda: analyze_cost_risk(items, config)),
        ("parametric_estimate", lambda: analyze_parametric_estimate(zones, config)),
    ]

    for name, fn in analyses:
        try:
            score, warnings, metrics = fn()
            sub_scores[name] = score
            all_warnings.extend(warnings)
            all_metrics[name] = metrics
        except Exception:
            logger.exception("Error in cost sub-analysis %s", name)
            sub_scores[name] = 0.0
            all_warnings.append({
                "code": "ANALYSIS_ERROR",
                "severity": "critical",
                "message": f"Fehler bei Kostenanalyse: {name}",
                "suggestion": "Kostenpositionen und Konfiguration überprüfen.",
            })

    overall = sum(sub_scores.get(k, 50.0) * w for k, w in weights.items())

    for w in all_warnings:
        suggestion = w.get("suggestion")
        if suggestion and suggestion not in all_suggestions:
            all_suggestions.append(suggestion)

    all_warnings.sort(key=lambda w: SEVERITY_ORDER.get(w.get("severity", "info"), 2))

    return {
        "module": "cost",
        "overall_score": round(overall, 1),
        "sub_scores": {k: round(v, 1) for k, v in sub_scores.items()},
        "warnings": all_warnings,
        "suggestions": all_suggestions,
        "metrics": all_metrics,
        "config_used": config,
        "confidence": data_source,
        "confidence_note": "Basiert auf geschätzten Werten aus öffentlichen Spezifikationen." if data_source == "estimated" else None,
    }
