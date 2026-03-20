"""Community Knowledge Engine — relevance-based pattern matching.

Pure function version for testability. The DB-backed async version
wraps this with SQLAlchemy queries.
"""


def find_relevant_patterns(
    all_patterns: list[dict],
    hull_material: str | None = None,
    hull_construction: str | None = None,
    manufacturer: str | None = None,
    model: str | None = None,
    max_results: int = 20,
    include_positive: bool = False,
) -> list[dict]:
    """5-level relevance search against a list of pattern dicts.

    Args:
        all_patterns: All available patterns (from DB or test data).
        hull_material: Boat's hull material (BoatDNA value).
        hull_construction: Boat's hull construction method.
        manufacturer: Boat manufacturer name.
        model: Boat model name.
        max_results: Maximum patterns to return.
        include_positive: If True, include positive patterns in results.

    Returns:
        List of pattern dicts augmented with relevance, match_reason, pattern_id.
        Sorted by relevance × confidence descending.
    """
    candidates = all_patterns
    if not include_positive:
        candidates = [p for p in candidates if not p.get("is_positive", False)]

    matches: dict[int, dict] = {}

    for idx, pattern in enumerate(candidates):
        pattern_id = pattern.get("id", idx)
        p_mfr = pattern.get("manufacturer")
        p_model = pattern.get("boat_model")
        p_materials = pattern.get("materials_involved") or []
        p_constructions = pattern.get("construction_methods_involved") or []

        best_relevance = 0.0
        best_reason = None

        # Level 1: Exact model match
        if (manufacturer and model and p_mfr
                and p_mfr.lower() == manufacturer.lower()
                and p_model and p_model.lower() == model.lower()):
            best_relevance = 1.0
            best_reason = "exact_model"

        # Level 2: Manufacturer-wide (pattern has no model)
        if (manufacturer and p_mfr
                and p_mfr.lower() == manufacturer.lower()
                and p_model is None
                and best_relevance < 0.8):
            best_relevance = 0.8
            best_reason = "manufacturer"

        # Level 3: Construction method match (cross-manufacturer patterns)
        if (hull_material and hull_construction
                and p_mfr is None
                and hull_material in p_materials
                and hull_construction in p_constructions
                and best_relevance < 0.6):
            best_relevance = 0.6
            best_reason = "construction_method"

        # Level 4: Material-specific (cross-manufacturer, material only)
        if (hull_material
                and p_mfr is None
                and hull_material in p_materials
                and best_relevance < 0.4):
            best_relevance = 0.4
            best_reason = "material"

        # Level 5: Zone + Category fallback (any pattern)
        if (pattern.get("zone_type") and pattern.get("issue_category")
                and best_relevance < 0.3):
            best_relevance = 0.3
            best_reason = "zone_category"

        if best_relevance > 0 and best_reason:
            if pattern_id not in matches or matches[pattern_id]["relevance"] < best_relevance:
                matches[pattern_id] = {
                    "pattern_id": pattern_id,
                    "relevance": best_relevance,
                    "category": pattern.get("issue_category", "unknown"),
                    "zone_type": pattern.get("zone_type"),
                    "description": pattern.get("description", ""),
                    "report_count": pattern.get("report_count", 0),
                    "severity": pattern.get("severity_mode", "minor"),
                    "typical_onset_years": pattern.get("typical_onset_years"),
                    "materials_involved": pattern.get("materials_involved") or [],
                    "confidence": pattern.get("confidence", 0.5),
                    "match_reason": best_reason,
                    "is_positive": pattern.get("is_positive", False),
                }

    sorted_matches = sorted(
        matches.values(),
        key=lambda m: m["relevance"] * m["confidence"],
        reverse=True,
    )

    return sorted_matches[:max_results]
