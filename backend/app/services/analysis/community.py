"""Community Intelligence analysis module.

Scores community-reported patterns (forum experiences, owner feedback)
for a specific boat. Pure function, no DB access.
"""
from collections import Counter


BOAT_CLASS_DEFAULTS = {
    "small_sail": {
        "max_patterns": 15,
        "min_confidence": 0.4,
        "severity_weights": {"critical": 25, "major": 15, "minor": 5, "cosmetic": 2},
    },
    "cruising_sail": {
        "max_patterns": 20,
        "min_confidence": 0.3,
        "severity_weights": {"critical": 25, "major": 15, "minor": 5, "cosmetic": 2},
    },
    "large_motor": {
        "max_patterns": 20,
        "min_confidence": 0.3,
        "severity_weights": {"critical": 25, "major": 15, "minor": 5, "cosmetic": 2},
    },
    "superyacht": {
        "max_patterns": 25,
        "min_confidence": 0.2,
        "severity_weights": {"critical": 25, "major": 15, "minor": 5, "cosmetic": 2},
    },
}

ZONE_LABELS = {
    "hull": "den Rumpfbereich",
    "deck": "das Deck",
    "cockpit": "das Cockpit",
    "galley": "die Pantry",
    "head": "den Nassbereich",
    "cabin": "die Kabine",
    "engine_room": "den Motorraum",
    "bilge": "die Bilge",
    "rigging": "das Rigg",
    "salon": "den Salon",
    "helm": "den Steuerstand",
}


def run_community_analysis(
    zones: list[dict],
    passages: list[dict],
    boat_class: str = "cruising_sail",
    config_overrides: dict | None = None,
    *,
    community_patterns: list[dict] | None = None,
) -> dict:
    if not community_patterns:
        return {"available": False, "reason": "Keine Community-Daten verfügbar."}

    defaults = BOAT_CLASS_DEFAULTS.get(boat_class, BOAT_CLASS_DEFAULTS["cruising_sail"]).copy()
    if config_overrides:
        defaults.update(config_overrides)
    config = defaults

    max_patterns = config["max_patterns"]
    min_confidence = config["min_confidence"]
    severity_weights = config["severity_weights"]

    negative = [p for p in community_patterns if not p.get("is_positive", False)]
    positive = [p for p in community_patterns if p.get("is_positive", False)]

    # Known issues score
    known_issues_score = 100.0
    for p in negative:
        weight = severity_weights.get(p.get("severity", "minor"), 5)
        relevance = p.get("relevance", 0.5)
        confidence = p.get("confidence", 0.5)
        known_issues_score -= weight * relevance * confidence
    known_issues_score = max(0.0, known_issues_score)

    # Positive reputation score
    positive_reputation_score = 50.0
    for p in positive:
        relevance = p.get("relevance", 0.5)
        confidence = p.get("confidence", 0.5)
        positive_reputation_score += 10 * relevance * confidence
    positive_reputation_score = min(100.0, positive_reputation_score)

    # Data coverage score
    total_count = len(community_patterns)
    data_coverage_score = min(100.0, total_count / max_patterns * 100)

    # Overall score
    overall_score = (
        known_issues_score * 0.50
        + positive_reputation_score * 0.30
        + data_coverage_score * 0.20
    )

    # Warnings
    warnings = []
    warning_patterns = []
    for p in negative:
        if p.get("severity") not in ("critical", "major"):
            continue
        if p.get("confidence", 0) < min_confidence:
            continue
        warnings.append({
            "code": "COMMUNITY_KNOWN_ISSUE",
            "severity": "critical" if p["severity"] == "critical" else "warning",
            "zone": p.get("zone_type"),
            "message": f"COMMUNITY: {p['description']} ({p.get('report_count', 0)} Berichte)",
            "source": "community",
            "confidence": "documented",
        })
        warning_patterns.append(p)

    # Suggestions
    suggestions = []
    for p in warning_patterns:
        zone_label = ZONE_LABELS.get(p.get("zone_type", ""), p.get("zone_type", "diesen Bereich"))
        onset = p.get("typical_onset_years")
        onset_text = f" (typisch nach {onset:.0f} Jahren)" if onset else ""
        suggestions.append({
            "code": "COMMUNITY_CHECK_RECOMMENDATION",
            "zone": p.get("zone_type"),
            "message": f"Prüfen Sie {zone_label} besonders sorgfältig — bekanntes Problem bei vergleichbaren Booten{onset_text}.",
            "priority": "high" if p["severity"] == "critical" else "medium",
            "source": "community",
        })

    # Metrics
    categories = [p.get("category", "unknown") for p in community_patterns]
    category_counts = Counter(categories)
    most_common = category_counts.most_common(1)[0][0] if category_counts else None
    onset_values = [p["typical_onset_years"] for p in negative if p.get("typical_onset_years") is not None]
    earliest_onset = min(onset_values) if onset_values else None

    return {
        "module": "community",
        "available": True,
        "overall_score": round(overall_score, 1),
        "sub_scores": {
            "known_issues": {
                "score": round(known_issues_score, 1),
                "label": "Bekannte Probleme",
                "details": [{"description": p["description"], "severity": p.get("severity"),
                             "relevance": p.get("relevance"), "report_count": p.get("report_count")} for p in negative],
            },
            "positive_reputation": {
                "score": round(positive_reputation_score, 1),
                "label": "Positive Erfahrungen",
                "details": [{"description": p["description"], "relevance": p.get("relevance"),
                             "report_count": p.get("report_count")} for p in positive],
            },
            "data_coverage": {
                "score": round(data_coverage_score, 1),
                "label": "Datenabdeckung",
                "details": {"total_patterns": total_count, "max_patterns": max_patterns},
            },
        },
        "warnings": warnings,
        "suggestions": suggestions,
        "metrics": {
            "total_patterns_found": total_count,
            "negative_patterns": len(negative),
            "positive_patterns": len(positive),
            "most_common_category": most_common,
            "earliest_typical_onset_years": earliest_onset,
        },
        "config_used": config,
        "confidence": "documented",
    }
