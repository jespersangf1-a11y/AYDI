"""Batch aggregation of community reports into patterns.

Pure function version: takes list of report dicts, returns list of pattern dicts.
The DB-backed wrapper (used by API endpoint) calls this function.
"""
from collections import Counter, defaultdict
from dataclasses import dataclass
from statistics import median


MIN_REPORTS_FOR_PATTERN = 3
MIN_RELIABILITY = 0.3


@dataclass
class AggregationResult:
    patterns_created: int
    reports_processed: int
    reports_skipped: int
    groups_below_threshold: int


def aggregate_reports_to_patterns(reports: list[dict]) -> list[dict]:
    """Aggregate community reports into patterns.

    Args:
        reports: List of report dicts (from DB or test factories).

    Returns:
        List of pattern dicts ready for DB insertion or direct use.
    """
    # Filter low-reliability reports
    valid_reports = [r for r in reports if r.get("reliability", 0) >= MIN_RELIABILITY]

    patterns = []

    # --- Negative patterns ---
    # Explode issues into individual tuples
    issue_entries = []
    for idx, report in enumerate(valid_reports):
        for issue in report.get("issues", []):
            issue_entries.append({
                "report_idx": idx,
                "report": report,
                "category": issue.get("category", "unknown"),
                "zone_type": issue.get("zone_type"),
                "description": issue.get("description", ""),
                "severity": issue.get("severity", "minor"),
                "boat_age_months": issue.get("boat_age_months"),
            })

    # Pass 1: Model-level grouping
    model_groups = defaultdict(list)
    for entry in issue_entries:
        mfr = entry["report"].get("boat_manufacturer")
        model = entry["report"].get("boat_model")
        if mfr and model:
            key = (mfr, model, entry["category"], entry["zone_type"])
            model_groups[key].append(entry)

    for (mfr, model, category, zone_type), entries in model_groups.items():
        if len(entries) < MIN_REPORTS_FOR_PATTERN:
            continue
        patterns.append(_build_pattern(entries, mfr, model, category, zone_type))

    # Pass 2: Manufacturer-level grouping
    mfr_groups = defaultdict(list)
    for entry in issue_entries:
        mfr = entry["report"].get("boat_manufacturer")
        if mfr:
            key = (mfr, entry["category"], entry["zone_type"])
            mfr_groups[key].append(entry)

    for (mfr, category, zone_type), entries in mfr_groups.items():
        if len(entries) < MIN_REPORTS_FOR_PATTERN:
            continue
        # Skip if already covered by a model-level pattern
        existing = [p for p in patterns
                    if p["manufacturer"] == mfr and p["issue_category"] == category
                    and p["zone_type"] == zone_type and p["boat_model"] is not None]
        if existing:
            continue
        patterns.append(_build_pattern(entries, mfr, None, category, zone_type))

    # Pass 3: Construction-level grouping (cross-manufacturer)
    construction_groups = defaultdict(list)
    for entry in issue_entries:
        hull_mat = entry["report"].get("hull_material")
        hull_con = entry["report"].get("hull_construction")
        if hull_mat:
            key = (hull_mat, hull_con, entry["category"], entry["zone_type"])
            construction_groups[key].append(entry)

    for (hull_mat, hull_con, category, zone_type), entries in construction_groups.items():
        if len(entries) < MIN_REPORTS_FOR_PATTERN:
            continue
        # Only create if reports come from >=2 different manufacturers
        manufacturers = set(e["report"].get("boat_manufacturer") for e in entries)
        if len(manufacturers) < 2:
            continue
        p = _build_pattern(entries, None, None, category, zone_type)
        p["materials_involved"] = [hull_mat] if hull_mat else []
        p["construction_methods_involved"] = [hull_con] if hull_con else []
        patterns.append(p)

    # --- Positive patterns ---
    positive_entries = []
    for idx, report in enumerate(valid_reports):
        for pos in report.get("positives", []):
            positive_entries.append({
                "report_idx": idx,
                "report": report,
                "category": pos.get("category", "unknown"),
                "zone_type": pos.get("zone_type"),
                "description": pos.get("description", ""),
                "severity": "positive",
                "boat_age_months": None,
            })

    # Group positives by (manufacturer, model, category, zone_type)
    pos_groups = defaultdict(list)
    for entry in positive_entries:
        mfr = entry["report"].get("boat_manufacturer")
        model = entry["report"].get("boat_model")
        key = (mfr, model, entry["category"], entry["zone_type"])
        pos_groups[key].append(entry)

    for (mfr, model, category, zone_type), entries in pos_groups.items():
        if len(entries) < MIN_REPORTS_FOR_PATTERN:
            continue
        p = _build_pattern(entries, mfr, model, category, zone_type)
        p["is_positive"] = True
        p["severity_mode"] = "positive"
        patterns.append(p)

    return patterns


def _build_pattern(
    entries: list[dict],
    manufacturer: str | None,
    model: str | None,
    category: str,
    zone_type: str | None,
) -> dict:
    """Build a pattern dict from a group of issue entries."""
    report_count = len(entries)

    # Severity mode
    severities = [e["severity"] for e in entries]
    severity_mode = Counter(severities).most_common(1)[0][0]

    # Description mode
    descriptions = [e["description"] for e in entries]
    description = Counter(descriptions).most_common(1)[0][0]

    # Onset median
    age_values = [e["boat_age_months"] for e in entries if e.get("boat_age_months") is not None]
    typical_onset_years = round(median(age_values) / 12, 1) if len(age_values) >= 3 else None

    # Confidence
    reliabilities = [e["report"].get("reliability", 0.5) for e in entries]
    mean_reliability = sum(reliabilities) / len(reliabilities) if reliabilities else 0.5
    confidence = round(min(1.0, report_count / 10) * mean_reliability, 2)

    # Materials and construction from reports
    materials = list(set(
        e["report"].get("hull_material") for e in entries
        if e["report"].get("hull_material")
    ))
    constructions = list(set(
        e["report"].get("hull_construction") for e in entries
        if e["report"].get("hull_construction")
    ))

    # Source report indices (placeholder -- real DB version would use IDs)
    report_indices = list(set(e["report_idx"] for e in entries))

    return {
        "manufacturer": manufacturer,
        "boat_model": model,
        "issue_category": category,
        "zone_type": zone_type,
        "description": description,
        "report_count": report_count,
        "severity_mode": severity_mode,
        "typical_onset_years": typical_onset_years,
        "materials_involved": materials or None,
        "construction_methods_involved": constructions or None,
        "confidence": confidence,
        "source_report_ids": report_indices,
        "is_positive": False,
    }
