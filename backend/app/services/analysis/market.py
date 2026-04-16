"""Market & Competitor Analysis module for yacht layouts.

Compares a planned model against competitors in the same segment,
evaluating metric positioning, competitive strengths/weaknesses,
price fit, uniqueness, and market gaps. Pure function module — no
database access. All user-facing strings are in German.
"""
import logging
import math

logger = logging.getLogger(__name__)

BOAT_CLASS_DEFAULTS = {
    "small_sail": {
        "min_competitors": 5,
        "length_tolerance_pct": 0.15,
        "benchmark_metrics": [
            "cockpit_area_sqm",
            "cabin_count",
            "head_count",
            "storage_volume_l",
            "deck_height_mm",
        ],
        "weights": {
            "metric_comparison": 0.30,
            "competitive_position": 0.25,
            "price_positioning": 0.15,
            "uniqueness": 0.15,
            "gaps": 0.15,
        },
    },
    "cruising_sail": {
        "min_competitors": 5,
        "length_tolerance_pct": 0.15,
        "benchmark_metrics": [
            "cockpit_area_sqm",
            "salon_area_sqm",
            "cabin_count",
            "head_count",
            "berth_count",
            "storage_volume_l",
            "deck_height_mm",
        ],
        "weights": {
            "metric_comparison": 0.30,
            "competitive_position": 0.25,
            "price_positioning": 0.15,
            "uniqueness": 0.15,
            "gaps": 0.15,
        },
    },
    "large_motor": {
        "min_competitors": 5,
        "length_tolerance_pct": 0.15,
        "benchmark_metrics": [
            "cockpit_area_sqm",
            "salon_area_sqm",
            "cabin_count",
            "head_count",
            "flybridge_area_sqm",
            "deck_height_mm",
        ],
        "weights": {
            "metric_comparison": 0.25,
            "competitive_position": 0.25,
            "price_positioning": 0.20,
            "uniqueness": 0.15,
            "gaps": 0.15,
        },
    },
    "racing_sail": {
        "min_competitors": 5,
        "length_tolerance_pct": 0.12,
        "benchmark_metrics": [
            "cockpit_area_sqm",
            "cabin_count",
            "displacement_kg",
            "deck_height_mm",
        ],
        "weights": {
            "metric_comparison": 0.35,
            "competitive_position": 0.25,
            "price_positioning": 0.12,
            "uniqueness": 0.15,
            "gaps": 0.13,
        },
    },
    "daysailer": {
        "min_competitors": 5,
        "length_tolerance_pct": 0.14,
        "benchmark_metrics": [
            "cockpit_area_sqm",
            "cabin_count",
            "head_count",
            "deck_height_mm",
        ],
        "weights": {
            "metric_comparison": 0.32,
            "competitive_position": 0.25,
            "price_positioning": 0.14,
            "uniqueness": 0.15,
            "gaps": 0.14,
        },
    },
    "motorsailer": {
        "min_competitors": 5,
        "length_tolerance_pct": 0.15,
        "benchmark_metrics": [
            "cockpit_area_sqm",
            "salon_area_sqm",
            "cabin_count",
            "head_count",
            "deck_height_mm",
        ],
        "weights": {
            "metric_comparison": 0.30,
            "competitive_position": 0.25,
            "price_positioning": 0.16,
            "uniqueness": 0.15,
            "gaps": 0.14,
        },
    },
    "catamaran_sail": {
        "min_competitors": 4,
        "length_tolerance_pct": 0.16,
        "benchmark_metrics": [
            "cockpit_area_sqm",
            "salon_area_sqm",
            "cabin_count",
            "head_count",
            "deck_height_mm",
        ],
        "weights": {
            "metric_comparison": 0.30,
            "competitive_position": 0.25,
            "price_positioning": 0.15,
            "uniqueness": 0.16,
            "gaps": 0.14,
        },
    },
    "catamaran_motor": {
        "min_competitors": 5,
        "length_tolerance_pct": 0.15,
        "benchmark_metrics": [
            "cockpit_area_sqm",
            "salon_area_sqm",
            "cabin_count",
            "head_count",
            "flybridge_area_sqm",
            "deck_height_mm",
        ],
        "weights": {
            "metric_comparison": 0.25,
            "competitive_position": 0.25,
            "price_positioning": 0.20,
            "uniqueness": 0.15,
            "gaps": 0.15,
        },
    },
    "small_motor": {
        "min_competitors": 5,
        "length_tolerance_pct": 0.14,
        "benchmark_metrics": [
            "cockpit_area_sqm",
            "salon_area_sqm",
            "cabin_count",
            "head_count",
            "deck_height_mm",
        ],
        "weights": {
            "metric_comparison": 0.28,
            "competitive_position": 0.25,
            "price_positioning": 0.18,
            "uniqueness": 0.15,
            "gaps": 0.14,
        },
    },
    "sport_cruiser": {
        "min_competitors": 5,
        "length_tolerance_pct": 0.15,
        "benchmark_metrics": [
            "cockpit_area_sqm",
            "salon_area_sqm",
            "cabin_count",
            "head_count",
            "flybridge_area_sqm",
            "deck_height_mm",
        ],
        "weights": {
            "metric_comparison": 0.24,
            "competitive_position": 0.26,
            "price_positioning": 0.20,
            "uniqueness": 0.15,
            "gaps": 0.15,
        },
    },
    "trawler": {
        "min_competitors": 4,
        "length_tolerance_pct": 0.16,
        "benchmark_metrics": [
            "cockpit_area_sqm",
            "salon_area_sqm",
            "cabin_count",
            "head_count",
            "fuel_capacity_l",
            "deck_height_mm",
        ],
        "weights": {
            "metric_comparison": 0.24,
            "competitive_position": 0.24,
            "price_positioning": 0.22,
            "uniqueness": 0.15,
            "gaps": 0.15,
        },
    },
    "explorer": {
        "min_competitors": 3,
        "length_tolerance_pct": 0.18,
        "benchmark_metrics": [
            "salon_area_sqm",
            "cabin_count",
            "head_count",
            "fuel_capacity_l",
            "water_capacity_l",
            "deck_height_mm",
        ],
        "weights": {
            "metric_comparison": 0.22,
            "competitive_position": 0.24,
            "price_positioning": 0.24,
            "uniqueness": 0.15,
            "gaps": 0.15,
        },
    },
    "superyacht": {
        "min_competitors": 3,
        "length_tolerance_pct": 0.20,
        "benchmark_metrics": [
            "salon_area_sqm",
            "cabin_count",
            "head_count",
            "crew_quarters_count",
            "deck_height_mm",
        ],
        "weights": {
            "metric_comparison": 0.20,
            "competitive_position": 0.25,
            "price_positioning": 0.25,
            "uniqueness": 0.15,
            "gaps": 0.15,
        },
    },
}

SEVERITY_ORDER = {"critical": 0, "warning": 1, "info": 2}


# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------


def _calculate_zone_area(polygon: list[list[float]]) -> float:
    """Compute polygon area in square metres using the Shoelace formula.

    Polygon vertices are expected in millimetres; result is returned in sqm.
    """
    n = len(polygon)
    if n < 3:
        return 0.0
    area_mm2 = 0.0
    for i in range(n):
        x1, y1 = polygon[i]
        x2, y2 = polygon[(i + 1) % n]
        area_mm2 += x1 * y2 - x2 * y1
    area_mm2 = abs(area_mm2) / 2.0
    return area_mm2 / 1_000_000.0  # mm² → m²


def _extract_layout_metrics(
    zones: list[dict],
    passages: list[dict],
    boat_length_m: float | None,
) -> dict:
    """Extract key spatial metrics from a layout's zones and passages.

    Returns a dict with numeric values for each benchmark metric:
      cockpit_area_sqm, salon_area_sqm, cabin_count, head_count,
      berth_count, storage_volume_l, deck_height_mm, flybridge_area_sqm,
      crew_quarters_count, boat_length_m.
    """
    cockpit_area = 0.0
    salon_area = 0.0
    flybridge_area = 0.0
    cabin_count = 0
    head_count = 0
    berth_count = 0
    crew_quarters_count = 0
    storage_volume_l = 0.0
    deck_heights: list[float] = []

    for zone in zones:
        zone_type = zone.get("zone_type", "")
        polygon = zone.get("polygon", [])
        area = _calculate_zone_area(polygon)
        height_mm = zone.get("height_mm") or 0.0
        props = zone.get("properties") or {}

        if zone_type == "cockpit":
            cockpit_area += area
        elif zone_type == "salon":
            salon_area += area
        elif zone_type == "flybridge":
            flybridge_area += area
        elif zone_type == "cabin":
            cabin_count += 1
            berths = props.get("berth_count") or props.get("berths") or 1
            berth_count += int(berths)
        elif zone_type == "head":
            head_count += 1
        elif zone_type == "crew_quarters":
            crew_quarters_count += 1
        elif zone_type == "storage":
            # Estimate volume: area (sqm) * accessible height fraction (50% of height)
            if height_mm > 0:
                storage_volume_l += area * (height_mm * 0.5 / 1000.0) * 1000.0
            else:
                storage_volume_l += area * 0.5 * 1000.0  # assume 0.5 m accessible

        if height_mm > 0:
            deck_heights.append(height_mm)

    avg_deck_height = (sum(deck_heights) / len(deck_heights)) if deck_heights else 0.0

    return {
        "cockpit_area_sqm": round(cockpit_area, 2),
        "salon_area_sqm": round(salon_area, 2),
        "cabin_count": cabin_count,
        "head_count": head_count,
        "berth_count": berth_count,
        "storage_volume_l": round(storage_volume_l, 1),
        "deck_height_mm": round(avg_deck_height, 1),
        "flybridge_area_sqm": round(flybridge_area, 2),
        "crew_quarters_count": crew_quarters_count,
        "boat_length_m": boat_length_m or 0.0,
    }


def _competitor_stats(competitors: list[dict], metric: str) -> tuple[float, float, float] | None:
    """Return (avg, min, max) for a metric across all competitors.

    Skips competitors that don't have the metric. Returns None if no data.
    """
    values = []
    for c in competitors:
        km = c.get("key_metrics") or {}
        v = km.get(metric)
        if v is not None:
            values.append(float(v))
    if not values:
        return None
    return sum(values) / len(values), min(values), max(values)


# ---------------------------------------------------------------------------
# Sub-analysis 1: Metric comparison
# ---------------------------------------------------------------------------


def analyze_metric_comparison(
    layout_metrics: dict,
    competitors: list[dict],
    config: dict,
) -> tuple[float, list[dict], dict]:
    """Compare layout metrics against competitor averages.

    Per benchmark metric: compute competitor avg/min/max and layout deviation.
    Score starts at 100; -10 per metric deviating >20% from competitor average.
    Warnings issued for below-average (MARKET_BELOW_AVERAGE) and
    above-average (MARKET_ABOVE_AVERAGE) metrics.

    Returns (score 0-100, warnings, metrics).
    """
    warnings: list[dict] = []
    benchmark_metrics = config.get("benchmark_metrics", [])
    metric_details: dict[str, dict] = {}
    deviating_count = 0

    for metric in benchmark_metrics:
        layout_val = layout_metrics.get(metric)
        stats = _competitor_stats(competitors, metric)

        if stats is None or layout_val is None:
            metric_details[metric] = {"layout_value": layout_val, "status": "no_data"}
            continue

        avg, comp_min, comp_max = stats
        if avg == 0:
            metric_details[metric] = {
                "layout_value": layout_val,
                "competitor_avg": avg,
                "competitor_min": comp_min,
                "competitor_max": comp_max,
                "deviation_pct": 0.0,
                "status": "ok",
            }
            continue

        deviation_pct = (layout_val - avg) / avg  # signed

        status = "ok"
        if abs(deviation_pct) > 0.20:
            deviating_count += 1
            if deviation_pct < -0.20:
                status = "below_average"
                code = f"MARKET_BELOW_AVERAGE_{metric.upper()}"
                metric_label = metric.replace("_", " ")
                warnings.append({
                    "code": code,
                    "severity": "warning",
                    "message": (
                        f"{metric_label.capitalize()} liegt {abs(deviation_pct):.0%} "
                        f"unter dem Segmentdurchschnitt "
                        f"({layout_val:.1f} vs. Ø {avg:.1f})."
                    ),
                    "suggestion": (
                        f"{metric_label.capitalize()} {abs(deviation_pct):.0%} "
                        f"unter Segmentdurchschnitt — Vergrößerung/Erhöhung prüfen."
                    ),
                    "location": metric,
                    "value": layout_val,
                    "threshold": avg,
                })
            else:
                status = "above_average"
                code = f"MARKET_ABOVE_AVERAGE_{metric.upper()}"
                metric_label = metric.replace("_", " ")
                warnings.append({
                    "code": code,
                    "severity": "info",
                    "message": (
                        f"{metric_label.capitalize()} liegt {deviation_pct:.0%} "
                        f"über dem Segmentdurchschnitt "
                        f"({layout_val:.1f} vs. Ø {avg:.1f})."
                    ),
                    "suggestion": (
                        f"{metric_label.capitalize()} deutlich über Durchschnitt — "
                        f"Gewichts- und Kostenauswirkungen prüfen."
                    ),
                    "location": metric,
                    "value": layout_val,
                    "threshold": avg,
                })

        metric_details[metric] = {
            "layout_value": layout_val,
            "competitor_avg": round(avg, 2),
            "competitor_min": round(comp_min, 2),
            "competitor_max": round(comp_max, 2),
            "deviation_pct": round(deviation_pct, 4),
            "status": status,
        }

    score = max(0.0, 100.0 - deviating_count * 10.0)

    return score, warnings, {
        "metrics_compared": len(benchmark_metrics),
        "deviating_count": deviating_count,
        "metric_details": metric_details,
    }


# ---------------------------------------------------------------------------
# Sub-analysis 2: Competitive position
# ---------------------------------------------------------------------------


def analyze_competitive_position(
    layout_metrics: dict,
    competitors: list[dict],
    config: dict,
) -> tuple[float, list[dict], dict]:
    """Identify competitive strengths (>110% of avg) and weaknesses (<90% of avg).

    Score = 50 + 10 * strengths_count - 10 * weaknesses_count, clamped 0-100.

    Returns (score 0-100, warnings, metrics).
    """
    warnings: list[dict] = []
    benchmark_metrics = config.get("benchmark_metrics", [])
    strengths: list[str] = []
    weaknesses: list[str] = []

    for metric in benchmark_metrics:
        layout_val = layout_metrics.get(metric)
        stats = _competitor_stats(competitors, metric)

        if stats is None or layout_val is None:
            continue

        avg, _, _ = stats
        if avg == 0:
            continue

        ratio = layout_val / avg
        if ratio > 1.10:
            strengths.append(metric)
        elif ratio < 0.90:
            weaknesses.append(metric)

    for metric in weaknesses:
        metric_label = metric.replace("_", " ").capitalize()
        warnings.append({
            "code": f"COMPETITIVE_WEAKNESS_{metric.upper()}",
            "severity": "warning",
            "message": (
                f"Wettbewerbsschwäche: {metric_label} liegt unter 90% "
                f"des Segmentdurchschnitts."
            ),
            "suggestion": (
                f"{metric_label} verbessern um wettbewerbsfähig zu bleiben."
            ),
            "location": metric,
        })

    for metric in strengths:
        metric_label = metric.replace("_", " ").capitalize()
        warnings.append({
            "code": f"COMPETITIVE_STRENGTH_{metric.upper()}",
            "severity": "info",
            "message": (
                f"Wettbewerbsstärke: {metric_label} liegt über 110% "
                f"des Segmentdurchschnitts."
            ),
            "suggestion": (
                f"{metric_label} als Verkaufsargument hervorheben."
            ),
            "location": metric,
        })

    score = 50.0 + 10.0 * len(strengths) - 10.0 * len(weaknesses)
    score = max(0.0, min(100.0, score))

    return score, warnings, {
        "strengths": strengths,
        "weaknesses": weaknesses,
        "strength_count": len(strengths),
        "weakness_count": len(weaknesses),
    }


# ---------------------------------------------------------------------------
# Sub-analysis 3: Price positioning
# ---------------------------------------------------------------------------


def analyze_price_positioning(
    layout_metrics: dict,
    competitors: list[dict],
    estimated_cost: float | None,
    config: dict,
) -> tuple[float, list[dict], dict]:
    """Compare estimated build cost to competitor price ranges.

    Score 100 if within ±15% of competitor median price, degrades outside that.
    If no estimated_cost provided, returns score 50 + info warning.

    Returns (score 0-100, warnings, metrics).
    """
    warnings: list[dict] = []

    if estimated_cost is None:
        warnings.append({
            "code": "PRICE_NO_DATA",
            "severity": "info",
            "message": "Kein Zielpreis angegeben — Preispositionierung nicht bewertet.",
            "suggestion": "Geschätzten Verkaufspreis für Wettbewerbsvergleich angeben.",
        })
        return 50.0, warnings, {"estimated_cost": None, "competitor_median_price": None}

    # Collect competitor mid-prices from price_range_eur
    competitor_prices: list[float] = []
    for c in competitors:
        pr = c.get("price_range_eur")
        if pr and isinstance(pr, dict):
            lo = pr.get("min")
            hi = pr.get("max")
            if lo is not None and hi is not None:
                competitor_prices.append((float(lo) + float(hi)) / 2.0)
            elif lo is not None:
                competitor_prices.append(float(lo))
            elif hi is not None:
                competitor_prices.append(float(hi))

    if not competitor_prices:
        warnings.append({
            "code": "PRICE_NO_COMPETITOR_DATA",
            "severity": "info",
            "message": "Keine Wettbewerbspreisdaten verfügbar — Preisvergleich nicht möglich.",
            "suggestion": "Marktpreisdaten für Wettbewerber erfassen.",
        })
        return 50.0, warnings, {"estimated_cost": estimated_cost, "competitor_median_price": None}

    sorted_prices = sorted(competitor_prices)
    n = len(sorted_prices)
    if n % 2 == 1:
        median_price = sorted_prices[n // 2]
    else:
        median_price = (sorted_prices[n // 2 - 1] + sorted_prices[n // 2]) / 2.0

    deviation = (estimated_cost - median_price) / median_price  # signed

    if abs(deviation) <= 0.15:
        score = 100.0
    elif deviation > 0.15:
        # Too expensive
        overshoot = (deviation - 0.15) / 0.85  # 0 at 15%, 1 at 100% over
        score = max(0.0, 100.0 - overshoot * 100.0)
        warnings.append({
            "code": "PRICE_OUTLIER_HIGH",
            "severity": "warning",
            "message": (
                f"Zielpreis {estimated_cost:,.0f} EUR liegt {deviation:.0%} "
                f"über dem Segmentmedian ({median_price:,.0f} EUR)."
            ),
            "suggestion": (
                "Kosteneinsparungen prüfen oder Premium-Positionierung "
                "mit zusätzlichen Features begründen."
            ),
            "value": estimated_cost,
            "threshold": median_price,
        })
    else:
        # Too cheap
        undershoot = (-deviation - 0.15) / 0.85
        score = max(0.0, 100.0 - undershoot * 100.0)
        warnings.append({
            "code": "PRICE_OUTLIER_LOW",
            "severity": "warning",
            "message": (
                f"Zielpreis {estimated_cost:,.0f} EUR liegt {abs(deviation):.0%} "
                f"unter dem Segmentmedian ({median_price:,.0f} EUR)."
            ),
            "suggestion": (
                "Preisunterschreitung analysieren — Margendruck oder "
                "Positionierung als Einstiegsmodell prüfen."
            ),
            "value": estimated_cost,
            "threshold": median_price,
        })

    return score, warnings, {
        "estimated_cost": estimated_cost,
        "competitor_median_price": round(median_price, 2),
        "deviation_pct": round(deviation, 4),
    }


# ---------------------------------------------------------------------------
# Sub-analysis 4: Layout uniqueness
# ---------------------------------------------------------------------------


def analyze_layout_uniqueness(
    layout_metrics: dict,
    competitors: list[dict],
    config: dict,
) -> tuple[float, list[dict], dict]:
    """Assess how many benchmark metrics differ >20% from competitor average.

    Sweet spot: 30-70% of metrics unique. Score peaks at 50% unique (score 100),
    degrades toward 0% (too similar) and 100% (too unusual).
    Warning: LAYOUT_TOO_SIMILAR (<20% unique), LAYOUT_TOO_UNUSUAL (>80% unique).

    Returns (score 0-100, warnings, metrics).
    """
    warnings: list[dict] = []
    benchmark_metrics = config.get("benchmark_metrics", [])

    comparable = 0
    unique_count = 0
    unique_metrics: list[str] = []

    for metric in benchmark_metrics:
        layout_val = layout_metrics.get(metric)
        stats = _competitor_stats(competitors, metric)

        if stats is None or layout_val is None:
            continue

        avg, _, _ = stats
        if avg == 0:
            continue

        comparable += 1
        deviation_pct = abs(layout_val - avg) / avg
        if deviation_pct > 0.20:
            unique_count += 1
            unique_metrics.append(metric)

    if comparable == 0:
        warnings.append({
            "code": "UNIQUENESS_NO_DATA",
            "severity": "info",
            "message": "Keine vergleichbaren Metriken für Einzigartigkeitsanalyse vorhanden.",
            "suggestion": "Benchmark-Metriken im Layout und bei Wettbewerbern erfassen.",
        })
        return 50.0, warnings, {
            "unique_ratio": 0.0,
            "unique_count": 0,
            "comparable_count": 0,
            "unique_metrics": [],
        }

    unique_ratio = unique_count / comparable

    # Score: triangle function peaking at 0.50 unique ratio
    if unique_ratio <= 0.50:
        score = unique_ratio / 0.50 * 100.0
    else:
        score = (1.0 - unique_ratio) / 0.50 * 100.0

    score = max(0.0, min(100.0, score))

    if unique_ratio < 0.20:
        warnings.append({
            "code": "LAYOUT_TOO_SIMILAR",
            "severity": "warning",
            "message": (
                f"Layout ist dem Wettbewerb sehr ähnlich: nur {unique_ratio:.0%} "
                f"der Metriken weichen >20% vom Durchschnitt ab."
            ),
            "suggestion": (
                "Differenzierungsmerkmale entwickeln um sich vom Wettbewerb abzuheben."
            ),
        })
    elif unique_ratio > 0.80:
        warnings.append({
            "code": "LAYOUT_TOO_UNUSUAL",
            "severity": "warning",
            "message": (
                f"Layout weicht stark vom Marktsegment ab: {unique_ratio:.0%} "
                f"der Metriken unterscheiden sich >20% vom Durchschnitt."
            ),
            "suggestion": (
                "Starke Abweichungen auf Markttauglichkeit prüfen — "
                "Käufererwartungen im Segment beachten."
            ),
        })

    return score, warnings, {
        "unique_ratio": round(unique_ratio, 4),
        "unique_count": unique_count,
        "comparable_count": comparable,
        "unique_metrics": unique_metrics,
    }


# ---------------------------------------------------------------------------
# Sub-analysis 5: Market gaps
# ---------------------------------------------------------------------------


def analyze_market_gaps(
    layout_metrics: dict,
    competitors: list[dict],
    config: dict,
) -> tuple[float, list[dict], dict]:
    """Identify metrics where layout exceeds or undercuts all competitors.

    Each gap (layout > competitor max or layout < competitor min on a benchmark
    metric) adds +20 to a base score of 60, capped at 100.
    Gap descriptions are included in metrics.

    Returns (score 0-100, warnings, metrics).
    """
    warnings: list[dict] = []
    benchmark_metrics = config.get("benchmark_metrics", [])
    gaps: list[dict] = []

    for metric in benchmark_metrics:
        layout_val = layout_metrics.get(metric)
        stats = _competitor_stats(competitors, metric)

        if stats is None or layout_val is None:
            continue

        avg, comp_min, comp_max = stats

        if layout_val > comp_max:
            metric_label = metric.replace("_", " ").capitalize()
            gap_desc = (
                f"{metric_label}: Layout ({layout_val:.1f}) übertrifft "
                f"alle Wettbewerber (max. {comp_max:.1f})."
            )
            gaps.append({
                "metric": metric,
                "direction": "above_all",
                "layout_value": layout_val,
                "competitor_max": comp_max,
                "description": gap_desc,
            })
            warnings.append({
                "code": f"MARKET_GAP_ABOVE_{metric.upper()}",
                "severity": "info",
                "message": gap_desc,
                "suggestion": (
                    f"{metric_label} als Alleinstellungsmerkmal im Marketing nutzen."
                ),
                "location": metric,
            })
        elif layout_val < comp_min:
            metric_label = metric.replace("_", " ").capitalize()
            gap_desc = (
                f"{metric_label}: Layout ({layout_val:.1f}) liegt unter "
                f"allen Wettbewerbern (min. {comp_min:.1f})."
            )
            gaps.append({
                "metric": metric,
                "direction": "below_all",
                "layout_value": layout_val,
                "competitor_min": comp_min,
                "description": gap_desc,
            })
            warnings.append({
                "code": f"MARKET_GAP_BELOW_{metric.upper()}",
                "severity": "warning",
                "message": gap_desc,
                "suggestion": (
                    f"{metric_label} liegt unter allen Wettbewerbern — "
                    f"Marktfähigkeit prüfen oder Nischenpositioning klar definieren."
                ),
                "location": metric,
            })

    score = min(100.0, 60.0 + len(gaps) * 20.0)

    return score, warnings, {
        "gap_count": len(gaps),
        "gaps": gaps,
    }


# ---------------------------------------------------------------------------
# Orchestrator
# ---------------------------------------------------------------------------


def run_market_analysis(
    zones: list[dict],
    passages: list[dict],
    boat_class: str,
    config_overrides: dict | None = None,
    competitors: list[dict] | None = None,
    boat_length_m: float | None = None,
    estimated_cost: float | None = None,
    data_source: str = "measured",
) -> dict:
    """Orchestrator — runs all market & competitor sub-analyses.

    Args:
        zones: Layout zones (used to extract spatial metrics).
        passages: Layout passages (kept for API consistency).
        boat_class: One of small_sail, cruising_sail, large_motor, superyacht.
        config_overrides: Optional dict to override config values.
        competitors: List of competitor dicts, each with:
            - key_metrics (dict): numeric metric values keyed by metric name
            - length_m (float): overall length in metres
            - price_range_eur (dict): {"min": float, "max": float}
        boat_length_m: Length of the layout's boat in metres.
        estimated_cost: Estimated build/sale cost in EUR (optional).

    Returns a standardized result dict matching the AYDI analysis module contract.
    """
    if boat_class not in BOAT_CLASS_DEFAULTS:
        return {"available": False, "reason": f"Unbekannte Bootsklasse: {boat_class}"}

    config = BOAT_CLASS_DEFAULTS[boat_class].copy()
    weights = config.pop("weights").copy()

    if config_overrides:
        config.update(config_overrides)

    min_competitors = config.get("min_competitors", 5)
    competitor_list = competitors or []

    # Insufficient competitor data — degrade gracefully
    if len(competitor_list) < min_competitors:
        return {
            "module": "market",
            "overall_score": 50.0,
            "sub_scores": {k: 50.0 for k in weights},
            "warnings": [
                {
                    "code": "MARKET_INSUFFICIENT_COMPETITORS",
                    "severity": "info",
                    "message": (
                        f"Nicht genügend Wettbewerbsdaten. "
                        f"Mindestens {min_competitors} Modelle erforderlich "
                        f"(vorhanden: {len(competitor_list)})."
                    ),
                    "suggestion": (
                        f"Mindestens {min_competitors} Wettbewerbsmodelle "
                        f"in der Datenbank erfassen um eine Marktanalyse durchzuführen."
                    ),
                }
            ],
            "suggestions": [
                f"Mindestens {min_competitors} Wettbewerbsmodelle "
                f"in der Datenbank erfassen um eine Marktanalyse durchzuführen."
            ],
            "metrics": {},
            "config_used": config,
            "confidence": data_source,
            "confidence_note": "Basiert auf geschätzten Werten aus öffentlichen Spezifikationen." if data_source == "estimated" else None,
        }

    layout_metrics = _extract_layout_metrics(zones, passages, boat_length_m)

    sub_scores: dict[str, float] = {}
    all_warnings: list[dict] = []
    all_suggestions: list[str] = []
    all_metrics: dict[str, object] = {}

    analyses: list[tuple[str, object]] = [
        (
            "metric_comparison",
            lambda: analyze_metric_comparison(layout_metrics, competitor_list, config),
        ),
        (
            "competitive_position",
            lambda: analyze_competitive_position(layout_metrics, competitor_list, config),
        ),
        (
            "price_positioning",
            lambda: analyze_price_positioning(
                layout_metrics, competitor_list, estimated_cost, config
            ),
        ),
        (
            "uniqueness",
            lambda: analyze_layout_uniqueness(layout_metrics, competitor_list, config),
        ),
        (
            "gaps",
            lambda: analyze_market_gaps(layout_metrics, competitor_list, config),
        ),
    ]

    for name, fn in analyses:
        try:
            score, warnings, metrics = fn()
            sub_scores[name] = score
            all_warnings.extend(warnings)
            all_metrics[name] = metrics
        except Exception:
            logger.exception("Error in market sub-analysis %s", name)
            sub_scores[name] = 0.0
            all_warnings.append({
                "code": "ANALYSIS_ERROR",
                "severity": "critical",
                "message": f"Fehler bei Marktanalyse: {name}",
                "suggestion": "Eingabedaten und Wettbewerbsmodelle überprüfen.",
            })

    overall = sum(sub_scores.get(k, 50.0) * w for k, w in weights.items())

    for w in all_warnings:
        suggestion = w.get("suggestion")
        if suggestion and suggestion not in all_suggestions:
            all_suggestions.append(suggestion)

    all_warnings.sort(key=lambda w: SEVERITY_ORDER.get(w.get("severity", "info"), 2))

    all_metrics["layout_metrics"] = layout_metrics

    return {
        "module": "market",
        "overall_score": round(overall, 1),
        "sub_scores": {k: round(v, 1) for k, v in sub_scores.items()},
        "warnings": all_warnings,
        "suggestions": all_suggestions,
        "metrics": all_metrics,
        "config_used": config,
        "confidence": data_source,
        "confidence_note": "Basiert auf geschätzten Werten aus öffentlichen Spezifikationen." if data_source == "estimated" else None,
    }
