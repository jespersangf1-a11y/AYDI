"""Generate structured analysis reports for yacht designs."""
from datetime import datetime, timezone
from typing import Optional


def generate_report(
    project: dict,
    layout: dict,
    analysis_results: list[dict],
    report_type: str = "full",  # "full", "summary", "executive"
) -> dict:
    """
    Generate a structured report from analysis results.

    Returns a dict that represents the report structure,
    ready for PDF rendering or JSON export.
    """
    # Module labels in German
    MODULE_LABELS = {
        "ergonomics": "Ergonomie",
        "volume_storage": "Volumen & Stauraum",
        "emotional": "Emotionales Design",
        "compliance": "Normenprüfung",
        "production": "Produktionsfreundlichkeit",
        "materials": "Material & Qualität",
        "structural": "Strukturanalyse",
        "cost": "Kostenschätzung",
        "service_patterns": "Servicemuster",
        "brand_dna": "Marken-DNA",
        "market": "Markt & Wettbewerb",
    }

    BOAT_CLASS_LABELS = {
        "small_sail": "Kleine Segelyacht",
        "cruising_sail": "Fahrtensegler",
        "large_motor": "Große Motoryacht",
        "superyacht": "Superyacht",
    }

    # Sort results by module order
    module_order = list(MODULE_LABELS.keys())
    sorted_results = sorted(
        analysis_results,
        key=lambda r: module_order.index(r["module"]) if r["module"] in module_order else 99,
    )

    # Calculate overall score (average of all module scores)
    scores = [r["overall_score"] for r in sorted_results if r.get("overall_score") is not None]
    overall_score = round(sum(scores) / len(scores), 1) if scores else 0.0

    # Build sections
    sections = []
    all_warnings = []
    all_suggestions = []

    for result in sorted_results:
        module = result["module"]
        label = MODULE_LABELS.get(module, module)

        # Collect warnings
        warnings = result.get("warnings", [])
        for w in warnings:
            w_copy = dict(w)
            w_copy["module"] = label
            all_warnings.append(w_copy)

        # Collect suggestions
        for s in result.get("suggestions", []):
            if s not in all_suggestions:
                all_suggestions.append(s)

        section = {
            "title": label,
            "module": module,
            "score": result.get("overall_score", 0),
            "score_label": _score_label(result.get("overall_score", 0)),
            "sub_scores": result.get("sub_scores", {}),
            "warnings_count": len(warnings),
            "critical_count": sum(1 for w in warnings if w.get("severity") == "critical"),
            "warning_count": sum(1 for w in warnings if w.get("severity") == "warning"),
            "info_count": sum(1 for w in warnings if w.get("severity") == "info"),
            "key_metrics": _extract_key_metrics(result.get("metrics", {})),
        }

        if report_type == "full":
            section["warnings"] = warnings
            section["metrics"] = result.get("metrics", {})
            section["config_used"] = result.get("config_used", {})

        sections.append(section)

    # Sort all warnings by severity
    severity_order = {"critical": 0, "warning": 1, "info": 2}
    all_warnings.sort(key=lambda w: severity_order.get(w.get("severity", "info"), 3))

    # Build header
    header = {
        "title": f"AYDI Analysebericht — {project.get('name', 'Unbenannt')}",
        "subtitle": f"{layout.get('name', '')} ({layout.get('version', '')})",
        "boat_class": BOAT_CLASS_LABELS.get(project.get("boat_class", ""), project.get("boat_class", "")),
        "length_m": project.get("length_m"),
        "beam_m": project.get("beam_m"),
        "generated_at": datetime.now(timezone.utc).isoformat(),
        "report_type": report_type,
    }

    # Executive summary
    executive_summary = {
        "overall_score": overall_score,
        "overall_label": _score_label(overall_score),
        "modules_analyzed": len(sorted_results),
        "total_warnings": len(all_warnings),
        "critical_warnings": sum(1 for w in all_warnings if w.get("severity") == "critical"),
        "top_strengths": _find_strengths(sorted_results),
        "top_weaknesses": _find_weaknesses(sorted_results),
        "recommendation": _generate_recommendation(overall_score, all_warnings),
    }

    report = {
        "header": header,
        "executive_summary": executive_summary,
        "sections": sections,
        "all_warnings": all_warnings[:20] if report_type == "summary" else all_warnings,
        "suggestions": all_suggestions[:10] if report_type == "summary" else all_suggestions,
        "metadata": {
            "generator": "AYDI Report Generator v1.0",
            "format_version": "1.0",
        },
    }

    return report


def _score_label(score: float) -> str:
    """Return a German quality label for a 0-100 score."""
    if score >= 80:
        return "Sehr gut"
    elif score >= 65:
        return "Gut"
    elif score >= 50:
        return "Befriedigend"
    elif score >= 35:
        return "Ausreichend"
    else:
        return "Mangelhaft"


def _extract_key_metrics(metrics: dict, max_items: int = 5) -> list[dict]:
    """Extract the most important metrics for display."""
    items = []
    for key, value in list(metrics.items())[:max_items]:
        if isinstance(value, (int, float)):
            items.append({"key": key, "value": round(value, 2) if isinstance(value, float) else value})
        elif isinstance(value, str):
            items.append({"key": key, "value": value})
    return items


def _find_strengths(results: list[dict], top_n: int = 3) -> list[str]:
    """Find modules with highest scores."""
    MODULE_LABELS = {
        "ergonomics": "Ergonomie",
        "volume_storage": "Raumnutzung",
        "emotional": "Raumwirkung",
        "compliance": "Normenkonformität",
        "production": "Produktionsfreundlichkeit",
        "materials": "Materialqualität",
        "structural": "Strukturintegrität",
        "cost": "Kosteneffizienz",
        "service_patterns": "Servicemuster",
        "brand_dna": "Marken-DNA",
        "market": "Marktpositionierung",
    }
    sorted_by_score = sorted(results, key=lambda r: r.get("overall_score", 0), reverse=True)
    strengths = []
    for r in sorted_by_score[:top_n]:
        if r.get("overall_score", 0) >= 70:
            label = MODULE_LABELS.get(r["module"], r["module"])
            strengths.append(f"{label} ({r['overall_score']:.0f}/100)")
    return strengths


def _find_weaknesses(results: list[dict], top_n: int = 3) -> list[str]:
    """Find modules with lowest scores."""
    MODULE_LABELS = {
        "ergonomics": "Ergonomie",
        "volume_storage": "Raumnutzung",
        "emotional": "Raumwirkung",
        "compliance": "Normenkonformität",
        "production": "Produktionsfreundlichkeit",
        "materials": "Materialqualität",
        "structural": "Strukturintegrität",
        "cost": "Kosteneffizienz",
        "service_patterns": "Servicemuster",
        "brand_dna": "Marken-DNA",
        "market": "Marktpositionierung",
    }
    sorted_by_score = sorted(results, key=lambda r: r.get("overall_score", 0))
    weaknesses = []
    for r in sorted_by_score[:top_n]:
        if r.get("overall_score", 0) < 65:
            label = MODULE_LABELS.get(r["module"], r["module"])
            weaknesses.append(f"{label} ({r['overall_score']:.0f}/100)")
    return weaknesses


def _generate_recommendation(overall_score: float, warnings: list[dict]) -> str:
    """Generate an overall German-language recommendation."""
    critical_count = sum(1 for w in warnings if w.get("severity") == "critical")

    if critical_count > 0:
        return (
            f"{critical_count} kritische Befunde erfordern sofortige Aufmerksamkeit. "
            "Prüfen Sie die markierten Bereiche vor der Weiterentwicklung."
        )
    elif overall_score >= 80:
        return (
            "Der Entwurf zeigt insgesamt ein hohes Qualitätsniveau. "
            "Kleinere Optimierungen sind in den Detailbereichen möglich."
        )
    elif overall_score >= 60:
        return (
            "Der Entwurf ist grundsätzlich solide, weist aber Optimierungspotenzial in mehreren Bereichen auf. "
            "Empfehlung: Schwächste Module gezielt überarbeiten."
        )
    else:
        return (
            "Der Entwurf weist signifikante Verbesserungsmöglichkeiten auf. "
            "Empfehlung: Grundlegende Überarbeitung der schwächsten Bereiche vor Weiterentwicklung."
        )
