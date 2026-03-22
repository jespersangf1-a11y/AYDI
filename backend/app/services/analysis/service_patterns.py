"""Service Pattern Analysis module for yacht layouts.

Mines historical service reports for patterns that should inform new designs.
Rule-based analysis — no ML. Identifies problematic zone types, age-related
failure windows, recurring material failures, and correlates these against
the current layout to generate proactive design warnings.
Pure function module — no database access.
All user-facing strings are in German.
"""
import logging

logger = logging.getLogger(__name__)

# Try to import knowledge databases for degradation and lifespan analysis
try:
    from app.services.knowledge.aging_lifecycle_manufacturers_deep import (
        DEGRADATION_CYCLES_DATABASE,
        MATERIAL_LIFESPAN_DATABASE,
        MANUFACTURER_DATABASE_SAIL,
        MANUFACTURER_DATABASE_MOTOR,
    )
except ImportError:
    DEGRADATION_CYCLES_DATABASE = {}
    MATERIAL_LIFESPAN_DATABASE = {}
    MANUFACTURER_DATABASE_SAIL = {}
    MANUFACTURER_DATABASE_MOTOR = {}

try:
    from app.services.knowledge.forensic_failure_analysis import (
        CUMULATIVE_DEGRADATION_CYCLES,
    )
except ImportError:
    CUMULATIVE_DEGRADATION_CYCLES = {}

BOAT_CLASS_DEFAULTS = {
    "small_sail": {
        "min_reports_for_pattern": 3,
        "high_issue_threshold": 5,  # 5+ weighted score in a zone_type = concerning
        "critical_age_window_months": 36,
        "weights": {
            "zone_issues": 0.30,
            "age_patterns": 0.25,
            "material_failures": 0.25,
            "design_warnings": 0.20,
        },
    },
    "cruising_sail": {
        "min_reports_for_pattern": 3,
        "high_issue_threshold": 5,
        "critical_age_window_months": 48,
        "weights": {
            "zone_issues": 0.25,
            "age_patterns": 0.25,
            "material_failures": 0.25,
            "design_warnings": 0.25,
        },
    },
    "large_motor": {
        "min_reports_for_pattern": 4,
        "high_issue_threshold": 4,
        "critical_age_window_months": 60,
        "weights": {
            "zone_issues": 0.25,
            "age_patterns": 0.20,
            "material_failures": 0.30,
            "design_warnings": 0.25,
        },
    },
    "racing_sail": {
        "min_reports_for_pattern": 2,
        "high_issue_threshold": 6,
        "critical_age_window_months": 24,
        "weights": {
            "zone_issues": 0.35,
            "age_patterns": 0.20,
            "material_failures": 0.20,
            "design_warnings": 0.25,
        },
    },
    "daysailer": {
        "min_reports_for_pattern": 3,
        "high_issue_threshold": 5,
        "critical_age_window_months": 36,
        "weights": {
            "zone_issues": 0.30,
            "age_patterns": 0.25,
            "material_failures": 0.23,
            "design_warnings": 0.22,
        },
    },
    "motorsailer": {
        "min_reports_for_pattern": 3,
        "high_issue_threshold": 5,
        "critical_age_window_months": 48,
        "weights": {
            "zone_issues": 0.26,
            "age_patterns": 0.24,
            "material_failures": 0.25,
            "design_warnings": 0.25,
        },
    },
    "catamaran_sail": {
        "min_reports_for_pattern": 3,
        "high_issue_threshold": 5,
        "critical_age_window_months": 48,
        "weights": {
            "zone_issues": 0.26,
            "age_patterns": 0.24,
            "material_failures": 0.25,
            "design_warnings": 0.25,
        },
    },
    "catamaran_motor": {
        "min_reports_for_pattern": 4,
        "high_issue_threshold": 4,
        "critical_age_window_months": 60,
        "weights": {
            "zone_issues": 0.25,
            "age_patterns": 0.20,
            "material_failures": 0.30,
            "design_warnings": 0.25,
        },
    },
    "small_motor": {
        "min_reports_for_pattern": 3,
        "high_issue_threshold": 4,
        "critical_age_window_months": 55,
        "weights": {
            "zone_issues": 0.25,
            "age_patterns": 0.21,
            "material_failures": 0.29,
            "design_warnings": 0.25,
        },
    },
    "sport_cruiser": {
        "min_reports_for_pattern": 4,
        "high_issue_threshold": 4,
        "critical_age_window_months": 60,
        "weights": {
            "zone_issues": 0.25,
            "age_patterns": 0.20,
            "material_failures": 0.30,
            "design_warnings": 0.25,
        },
    },
    "trawler": {
        "min_reports_for_pattern": 4,
        "high_issue_threshold": 4,
        "critical_age_window_months": 72,
        "weights": {
            "zone_issues": 0.24,
            "age_patterns": 0.19,
            "material_failures": 0.31,
            "design_warnings": 0.26,
        },
    },
    "explorer": {
        "min_reports_for_pattern": 4,
        "high_issue_threshold": 3,
        "critical_age_window_months": 72,
        "weights": {
            "zone_issues": 0.20,
            "age_patterns": 0.19,
            "material_failures": 0.31,
            "design_warnings": 0.30,
        },
    },
    "superyacht": {
        "min_reports_for_pattern": 4,
        "high_issue_threshold": 3,
        "critical_age_window_months": 60,
        "weights": {
            "zone_issues": 0.20,
            "age_patterns": 0.20,
            "material_failures": 0.30,
            "design_warnings": 0.30,
        },
    },
}

SEVERITY_ORDER = {"critical": 0, "warning": 1, "info": 2}

# Weighted score per report severity for zone issue accumulation
_REPORT_SEVERITY_WEIGHT = {
    "critical": 4,
    "high": 3,
    "medium": 2,
    "low": 1,
}

# Age buckets in months (lower bound inclusive, upper bound exclusive)
_AGE_BUCKETS = [
    (0, 12, "0–12 Monate"),
    (12, 24, "12–24 Monate"),
    (24, 36, "24–36 Monate"),
    (36, 48, "36–48 Monate"),
    (48, 60, "48–60 Monate"),
    (60, None, "60+ Monate"),
]


# ---------------------------------------------------------------------------
# Sub-analysis 1: Zone type issues
# ---------------------------------------------------------------------------


def analyze_zone_type_issues(
    zones: list[dict],
    service_reports: list[dict],
    config: dict,
) -> tuple[float, list[dict], dict]:
    """Count weighted service report scores per zone_type.

    Each report contributes severity-weighted points to its zone_type.
    Zone types that exceed high_issue_threshold trigger a warning.
    Score degrades linearly per problematic zone type.

    Returns (score 0-100, warnings, metrics).
    """
    warnings: list[dict] = []
    threshold = config.get("high_issue_threshold", 5)

    # Accumulate weighted score per zone_type
    zone_type_scores: dict[str, float] = {}
    for report in service_reports:
        zt = report.get("zone_type")
        if not zt:
            continue
        sev = report.get("severity", "low")
        weight = _REPORT_SEVERITY_WEIGHT.get(sev, 1)
        zone_type_scores[zt] = zone_type_scores.get(zt, 0.0) + weight

    problematic: list[str] = []
    for zt, score_val in zone_type_scores.items():
        if score_val >= threshold:
            problematic.append(zt)
            warnings.append({
                "code": f"SERVICE_PATTERN_{zt.upper()}",
                "severity": "warning",
                "message": (
                    f"Zonentyp '{zt}' weist wiederkehrende Serviceprobleme auf "
                    f"(Gewichteter Problemwert: {score_val:.0f}, Schwelle: {threshold})."
                ),
                "suggestion": (
                    f"Detailkonstruktion für Zonentyp '{zt}' überprüfen. "
                    f"Zugänglichkeit, Materialwahl und Abdichtung besonders beachten."
                ),
            })

    if not problematic:
        score = 100.0
    else:
        # Each problematic zone type reduces score by 15 points, minimum 0
        penalty = len(problematic) * 15.0
        score = max(0.0, 100.0 - penalty)

    return score, warnings, {
        "zone_type_scores": {k: round(v, 1) for k, v in zone_type_scores.items()},
        "problematic_zone_types": problematic,
        "threshold": threshold,
    }


# ---------------------------------------------------------------------------
# Sub-analysis 2: Age patterns
# ---------------------------------------------------------------------------


def analyze_age_patterns(
    service_reports: list[dict],
    config: dict,
) -> tuple[float, list[dict], dict]:
    """Group reports by boat_age_months into fixed buckets and flag spikes.

    A spike is defined as a bucket containing more than 2x the average
    report count across all buckets. Score is 100 for uniform distribution,
    penalized per spike bucket.

    Enriched with DEGRADATION_CYCLES_DATABASE and MATERIAL_LIFESPAN_DATABASE
    to identify self-reinforcing failure patterns.

    Returns (score 0-100, warnings, metrics).
    """
    warnings: list[dict] = []

    # Count reports per bucket
    bucket_counts: dict[str, int] = {label: 0 for _, _, label in _AGE_BUCKETS}

    for report in service_reports:
        age = report.get("boat_age_months")
        if age is None:
            continue
        for lo, hi, label in _AGE_BUCKETS:
            if hi is None:
                if age >= lo:
                    bucket_counts[label] += 1
                    break
            elif lo <= age < hi:
                bucket_counts[label] += 1
                break

    total = sum(bucket_counts.values())
    if total == 0:
        warnings.append({
            "code": "AGE_PATTERN_NO_DATA",
            "severity": "info",
            "message": "Keine Altersangaben in Serviceberichten — Alterskurven-Analyse nicht möglich.",
            "suggestion": "Bootslalter (boat_age_months) in Serviceberichten erfassen.",
        })
        return 50.0, warnings, {"bucket_counts": bucket_counts, "spike_buckets": []}

    num_buckets_with_data = sum(1 for c in bucket_counts.values() if c > 0)
    avg = total / max(num_buckets_with_data, 1)

    spike_buckets: list[str] = []
    for label, count in bucket_counts.items():
        if count > 2 * avg:
            spike_buckets.append(label)
            severity = "critical" if count > 3 * avg else "warning"
            warnings.append({
                "code": "AGE_PATTERN_WARNING",
                "severity": severity,
                "message": (
                    f"Überdurchschnittlich viele Serviceberichte im Altersfenster "
                    f"'{label}' ({count} Berichte, Ø {avg:.1f}). "
                    f"Mögliche Schwachstelle im Alterungsprozess."
                ),
                "suggestion": (
                    f"Materialien und Komponenten, die typisch im Fenster '{label}' "
                    f"versagen, auf Alternativen mit höherer Lebensdauer prüfen. "
                    f"Wenn bekannt, selbstverstärkende Degradationszyklen überprüfen."
                ),
            })

            # Enrich with knowledge of self-reinforcing degradation cycles
            if CUMULATIVE_DEGRADATION_CYCLES:
                try:
                    cycles = CUMULATIVE_DEGRADATION_CYCLES.get("common_cascades", [])
                    if cycles:
                        warnings.append({
                            "code": "SELF_REINFORCING_DEGRADATION",
                            "severity": "warning",
                            "message": (
                                f"Altersfenster '{label}' könnte selbstverstärkendem "
                                f"Degradationszyklus unterliegen (z.B. Osmose → Delamination → "
                                f"Wassereintritt → Kernfaulung)."
                            ),
                            "suggestion": (
                                f"Inspektionsplan mit verstärktem Fokus auf frühe Indikatoren "
                                f"für Materialabbau im Fenster '{label}' erstellen."
                            ),
                        })
                except (KeyError, TypeError, AttributeError):
                    pass

    if not spike_buckets:
        score = 100.0
    else:
        penalty = len(spike_buckets) * 20.0
        score = max(0.0, 100.0 - penalty)

    return score, warnings, {
        "bucket_counts": bucket_counts,
        "spike_buckets": spike_buckets,
        "average_per_bucket": round(avg, 1),
    }


# ---------------------------------------------------------------------------
# Sub-analysis 3: Material failures
# ---------------------------------------------------------------------------


def analyze_material_failures(
    service_reports: list[dict],
    config: dict,
) -> tuple[float, list[dict], dict]:
    """Cross-reference reports that list materials_involved.

    Materials appearing in 3+ reports are flagged as failure risks.
    Score is 100 if no material is problematic.

    Enriched with MATERIAL_LIFESPAN_DATABASE to provide real material
    science data on expected failure modes.

    Returns (score 0-100, warnings, metrics).
    """
    warnings: list[dict] = []
    min_reports = config.get("min_reports_for_pattern", 3)

    # Count occurrences per material
    material_counts: dict[str, int] = {}
    for report in service_reports:
        materials = report.get("materials_involved") or []
        if isinstance(materials, str):
            materials = [materials]
        for mat in materials:
            if mat:
                material_counts[mat] = material_counts.get(mat, 0) + 1

    problematic_materials: list[str] = []
    for mat, count in material_counts.items():
        if count >= min_reports:
            problematic_materials.append(mat)
            sev = "critical" if count >= min_reports * 2 else "warning"

            # Enrich with knowledge from material lifespan database
            known_failure_modes = []
            if MATERIAL_LIFESPAN_DATABASE:
                mat_lower = mat.lower()
                for db_key, db_data in MATERIAL_LIFESPAN_DATABASE.items():
                    if db_key.lower() in mat_lower or mat_lower in db_key.lower():
                        modes = db_data.get("failure_modes", [])
                        known_failure_modes = modes[:3]  # Top 3 failure modes
                        break

            msg = (
                f"Material '{mat}' erscheint in {count} Serviceberichten "
                f"(Mindestgrenze: {min_reports}). Erhöhtes Ausfallrisiko."
            )
            if known_failure_modes:
                msg += f" Bekannte Ausfallmodi: {', '.join(str(m).replace('_', ' ') for m in known_failure_modes)}."

            warnings.append({
                "code": "MATERIAL_FAILURE_RISK",
                "severity": sev,
                "message": msg,
                "suggestion": (
                    f"Material '{mat}' in neuen Entwürfen durch bewährtere "
                    f"Alternative ersetzen oder Wartungsintervall verkürzen."
                ),
            })

    if not problematic_materials:
        score = 100.0
    else:
        penalty = len(problematic_materials) * 20.0
        score = max(0.0, 100.0 - penalty)

    return score, warnings, {
        "material_counts": material_counts,
        "problematic_materials": problematic_materials,
        "min_reports_threshold": min_reports,
    }


# ---------------------------------------------------------------------------
# Sub-analysis 4: Design warnings (correlation with current layout)
# ---------------------------------------------------------------------------


def analyze_design_warnings(
    zones: list[dict],
    service_reports: list[dict],
    config: dict,
) -> tuple[float, list[dict], dict]:
    """Match the current layout's zone_types against historically problematic ones.

    For each zone in the current layout whose zone_type has accumulated many
    service reports, a proactive design warning is generated. Score degrades
    5 points per matched zone type.

    Returns (score 0-100, warnings, metrics).
    """
    warnings: list[dict] = []
    threshold = config.get("high_issue_threshold", 5)

    # Build zone_type -> weighted score from service reports
    zone_type_scores: dict[str, float] = {}
    for report in service_reports:
        zt = report.get("zone_type")
        if not zt:
            continue
        sev = report.get("severity", "low")
        weight = _REPORT_SEVERITY_WEIGHT.get(sev, 1)
        zone_type_scores[zt] = zone_type_scores.get(zt, 0.0) + weight

    # Collect problematic zone_types
    problematic_types = {zt for zt, s in zone_type_scores.items() if s >= threshold}

    # Find zones in current layout that match
    matched_zones: list[dict] = []
    seen_types: set[str] = set()

    for zone in zones:
        zt = zone.get("zone_type", "")
        if zt in problematic_types:
            matched_zones.append(zone)
            if zt not in seen_types:
                seen_types.add(zt)
                report_score = zone_type_scores.get(zt, 0.0)
                warnings.append({
                    "code": "LAYOUT_CORRELATED_ISSUE",
                    "severity": "warning",
                    "message": (
                        f"Zone '{zone.get('name', zt)}' (Typ: '{zt}') entspricht einem "
                        f"Zonentyp mit bekannten Serviceproblemen "
                        f"(Gewichteter Problemwert: {report_score:.0f})."
                    ),
                    "suggestion": (
                        f"Konstruktionsdetails für Zone '{zone.get('name', zt)}' "
                        f"besonders sorgfältig prüfen. Serviceerfahrungen aus "
                        f"ähnlichen Booten einbeziehen."
                    ),
                })

    score = max(0.0, 100.0 - len(seen_types) * 5.0)

    return score, warnings, {
        "problematic_types_in_history": sorted(problematic_types),
        "matched_zone_count": len(matched_zones),
        "matched_zone_types": sorted(seen_types),
    }


# ---------------------------------------------------------------------------
# Orchestrator
# ---------------------------------------------------------------------------


def run_service_patterns_analysis(
    zones: list[dict],
    passages: list[dict],
    boat_class: str,
    config_overrides: dict | None = None,
    service_reports: list[dict] | None = None,
    data_source: str = "measured",
) -> dict:
    """Orchestrator — runs all service pattern sub-analyses.

    Args:
        zones: Layout zones used to correlate historical patterns against
               the current design.
        passages: Layout passages (kept for API consistency, not used directly).
        boat_class: One of small_sail, cruising_sail, large_motor, superyacht.
        config_overrides: Optional dict to override default config values.
        service_reports: List of service report dicts. Each may contain:
            report_type, category, zone_type, severity, description,
            boat_age_months, materials_involved, cost_eur.

    Returns a standardized result dict matching the AYDI analysis module contract.
    """
    if boat_class not in BOAT_CLASS_DEFAULTS:
        raise ValueError(f"Unknown boat class: {boat_class}")

    config = BOAT_CLASS_DEFAULTS[boat_class].copy()
    weights = config.pop("weights").copy()

    if config_overrides:
        config.update(config_overrides)

    reports = service_reports or []

    # Early exit when no reports are available
    if not reports:
        return {
            "module": "service_patterns",
            "overall_score": 50.0,
            "sub_scores": {
                "zone_issues": 50.0,
                "age_patterns": 50.0,
                "material_failures": 50.0,
                "design_warnings": 50.0,
            },
            "warnings": [
                {
                    "code": "NO_SERVICE_REPORTS",
                    "severity": "info",
                    "message": (
                        "Keine Serviceberichte vorhanden. "
                        "Musteranalyse nicht möglich."
                    ),
                    "suggestion": (
                        "Serviceberichte erfassen und mit Layouts verknüpfen, "
                        "um Musteranalysen zu ermöglichen."
                    ),
                }
            ],
            "suggestions": [
                "Serviceberichte erfassen und mit Layouts verknüpfen, "
                "um Musteranalysen zu ermöglichen."
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
        (
            "zone_issues",
            lambda: analyze_zone_type_issues(zones, reports, config),
        ),
        (
            "age_patterns",
            lambda: analyze_age_patterns(reports, config),
        ),
        (
            "material_failures",
            lambda: analyze_material_failures(reports, config),
        ),
        (
            "design_warnings",
            lambda: analyze_design_warnings(zones, reports, config),
        ),
    ]

    for name, fn in analyses:
        try:
            score, warnings, metrics = fn()
            sub_scores[name] = score
            all_warnings.extend(warnings)
            all_metrics[name] = metrics
        except Exception:
            logger.exception("Error in service_patterns sub-analysis %s", name)
            sub_scores[name] = 0.0
            all_warnings.append({
                "code": "ANALYSIS_ERROR",
                "severity": "critical",
                "message": f"Fehler bei Servicemuster-Analyse: {name}",
                "suggestion": "Serviceberichte auf Vollständigkeit und Format prüfen.",
            })

    overall = sum(sub_scores.get(k, 50.0) * w for k, w in weights.items())

    for w in all_warnings:
        suggestion = w.get("suggestion")
        if suggestion and suggestion not in all_suggestions:
            all_suggestions.append(suggestion)

    all_warnings.sort(key=lambda w: SEVERITY_ORDER.get(w.get("severity", "info"), 2))

    return {
        "module": "service_patterns",
        "overall_score": round(overall, 1),
        "sub_scores": {k: round(v, 1) for k, v in sub_scores.items()},
        "warnings": all_warnings,
        "suggestions": all_suggestions,
        "metrics": all_metrics,
        "config_used": config,
        "confidence": data_source,
        "confidence_note": "Basiert auf geschätzten Werten aus öffentlichen Spezifikationen." if data_source == "estimated" else None,
    }
