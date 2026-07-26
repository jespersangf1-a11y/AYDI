# backend/app/services/knowledge/buyer_insights.py
"""
Buyer insights — product pillar 2 (Kaufberatung).

Combines three existing knowledge assets into one boat-specific answer to
"what are the known / expected problems of THIS boat?":

  1. Manufacturer weak-spot database (MANUFACTURER_DATABASE_SAIL/MOTOR/CUSTOM)
     with model-year windows, repair costs and survey recommendations
     -> confidence "documented" (curated knowledge base).
  2. Age-based component expectations (MATERIAL_LIFESPAN_DATABASE):
     build year -> current age -> components at/over typical lifespan
     -> confidence "estimated" (statistical lifespans, not findings on the
     actual boat).
  3. Community patterns (matched AND relevance-filtered by the caller via
     app.services.community.engine.find_relevant_patterns — only identity
     matches, no zone-level fallback of foreign manufacturers)
     -> confidence "documented" with report counts.

Pure functions, no DB access — the route layer loads community patterns and
passes them in. Reliability rules apply: nothing is fabricated; when a source
has no data the section says so instead of guessing; a positive track record
is rendered as a positive note, never as a problem card.
"""

from __future__ import annotations

import re
from typing import Any, Optional

from app.services.knowledge.aging_lifecycle_manufacturers_deep import (
    MANUFACTURER_DATABASE_SAIL,
    MANUFACTURER_DATABASE_MOTOR,
    MANUFACTURER_DATABASE_CUSTOM,
    MATERIAL_LIFESPAN_DATABASE,
)

SAIL_CLASSES = {
    "small_sail", "cruising_sail", "racing_sail", "daysailer",
    "motorsailer", "catamaran_sail",
}

# Components that only exist on sailing boats
_SAIL_ONLY_COMPONENTS = {
    "standing_rigging_wire", "standing_rigging_rod", "saildrive_diaphragm",
}

# Excluded from generic reports: rod rigging is rare outside racing/custom
# builds — flagging it for every production sailboat would be misleading.
_EXCLUDED_COMPONENTS = {"standing_rigging_rod"}

_SEVERITY_DE = {
    "critical": "kritisch",
    "critical_specific": "kritisch (modellspezifisch)",
    "major": "schwerwiegend",
    "moderate": "mittel",
    "moderate_preventable": "mittel (vermeidbar)",
    "manageable_with_care": "beherrschbar bei Pflege",
    "low_to_moderate": "gering bis mittel",
    "low": "gering",
    "minor": "gering",
}

_MATCH_REASON_DE = {
    "exact_model": "gleiches Modell",
    "manufacturer": "gleiche Werft",
    "construction_method": "gleiche Bauweise",
    "material": "gleiches Material",
    "zone_category": "bauartähnlich (andere Werft möglich)",
}

# The knowledge base stores problem lists / strings under several keys
_PROBLEM_LIST_KEYS = (
    "known_problems",
    "known_problems_documented",
    "known_problems_minimal",
)
_PROBLEM_STRING_KEYS = ("known_problems", "known_issue", "known_issues_consequence")

# String values that document the ABSENCE of problems (positive track record)
_NO_PROBLEM_MARKERS = ("virtually_none", "none_documented", "impeccable")

# Generic company-name tokens ignored during brand matching
_BRAND_STOPWORDS = {"", "yacht", "yachts", "yachtbau", "boats", "gmbh", "ag", "marine"}


def _humanize(value: Any) -> str:
    """Turn snake_case knowledge-base strings into readable text."""
    if value is None:
        return ""
    return str(value).replace("_", " ").strip()


def _severity_de(severity: Any) -> str:
    return _SEVERITY_DE.get(str(severity or "").lower(), _humanize(severity) or "unbekannt")


def parse_year_window(window: Any) -> Optional[tuple[Optional[int], Optional[int]]]:
    """Parse model_years strings like '2000_2012', 'pre_2008', 'post_2015',
    '1980s_1990s'. Returns (low, high) with None for open ends, or None when
    the format is unknown."""
    if not window:
        return None
    text = str(window).strip().lower()
    match = re.fullmatch(r"(\d{4})_(\d{4})", text)
    if match:
        return int(match.group(1)), int(match.group(2))
    match = re.fullmatch(r"pre_(\d{4})", text)
    if match:
        return None, int(match.group(1)) - 1
    match = re.fullmatch(r"post_(\d{4})", text)
    if match:
        return int(match.group(1)), None
    match = re.fullmatch(r"(\d{4})s_(\d{4})s", text)
    if match:
        return int(match.group(1)), int(match.group(2)) + 9
    return None


def format_year_window_de(window: Any) -> Optional[str]:
    """German display form: '2000–2012', 'vor 2008', 'ab 2015'."""
    parsed = parse_year_window(window)
    if parsed is None:
        return _humanize(window) or None
    low, high = parsed
    if low is None and high is not None:
        return f"vor {high + 1}"
    if high is None and low is not None:
        return f"ab {low}"
    return f"{low}–{high}"


def _format_percentage_de(value: Any) -> Optional[str]:
    """'15_20%' -> '15–20 %'."""
    if not value:
        return None
    match = re.fullmatch(r"(\d+)_(\d+)\s*%", str(value).strip())
    if match:
        return f"{match.group(1)}–{match.group(2)} %"
    return _humanize(value) or None


def _year_applies(year: Optional[int], window: Any) -> Optional[bool]:
    """True/False when decidable, None when year or window is missing/unparseable."""
    if year is None:
        return None
    parsed = parse_year_window(window)
    if parsed is None:
        return None
    low, high = parsed
    if low is not None and year < low:
        return False
    if high is not None and year > high:
        return False
    return True


def _brand_tokens(value: str) -> set[str]:
    tokens = set(re.split(r"[\s\-_/]+", value.strip().lower()))
    return tokens - _BRAND_STOPWORDS


def _lookup_manufacturer(brand: str) -> tuple[Optional[str], Optional[dict]]:
    """Find a manufacturer entry via token-subset matching on word boundaries.

    "Hallberg-Rassy" == hallberg_rassy; "Swan" ⊆ nautor_swan;
    "Bavaria Yachts GmbH" ⊇ bavaria. Substring containment is deliberately
    NOT used: it mis-assigned real brands (Hanseat -> hanse, Sun -> sunseeker)
    and would attribute documented facts of shipyard A to shipyard B.
    """
    if len(brand.strip()) < 3:
        return None, None
    query_tokens = _brand_tokens(brand)
    if not query_tokens:
        return None, None
    for database in (
        MANUFACTURER_DATABASE_SAIL,
        MANUFACTURER_DATABASE_MOTOR,
        MANUFACTURER_DATABASE_CUSTOM,
    ):
        for key, entry in database.items():
            key_tokens = _brand_tokens(key)
            if not key_tokens:
                continue
            if key_tokens <= query_tokens or query_tokens <= key_tokens:
                return key, entry
    return None, None


def _collect_known_problems(entry: dict) -> tuple[list[dict], Optional[str]]:
    """Normalize the KB's problem-key zoo into (problem_dicts, track_record_note).

    Only 5/23 entries use `known_problems` as a dict list; others use
    `known_problems_minimal`/`_documented`, singular string keys, or a
    positive "virtually none" string. Reading only one key silently
    suppressed documented weaknesses (false clean bill) — the exact failure
    the reliability rules forbid.
    """
    problems: list[dict] = []
    track_note: Optional[str] = None

    for key in _PROBLEM_LIST_KEYS:
        value = entry.get(key)
        if isinstance(value, list):
            problems.extend(p for p in value if isinstance(p, dict))

    for key in _PROBLEM_STRING_KEYS:
        value = entry.get(key)
        if isinstance(value, str) and value.strip():
            lowered = value.lower()
            if any(marker in lowered for marker in _NO_PROBLEM_MARKERS):
                track_note = (
                    "Keine dokumentierten Typ-Schwachstellen — die Wissensbasis "
                    f"vermerkt: „{_humanize(value)}“."
                )
            else:
                problems.append({"issue": value, "severity": "moderate"})

    return problems, track_note


def _era_note(entry: dict, year: Optional[int]) -> Optional[str]:
    """Pick the build_quality_assessment note matching the build year."""
    assessment = entry.get("build_quality_assessment")
    if not isinstance(assessment, dict):
        return None
    if year is not None:
        for era_key, note in assessment.items():
            if _year_applies(year, era_key):
                era_label = format_year_window_de(era_key) or _humanize(era_key)
                return f"{era_label}: {_humanize(note)}"
    general = assessment.get("general") or assessment.get("current_reputation")
    if general:
        return _humanize(general)
    return None


def _manufacturer_section(
    brand: str, model_name: Optional[str], year: Optional[int]
) -> dict:
    key, entry = _lookup_manufacturer(brand)
    if entry is None:
        return {
            "found": False,
            "note": (
                f"Für die Werft '{brand}' liegen keine kuratierten "
                "Schwachstellen-Daten vor. Das ist keine Entwarnung — "
                "es bedeutet nur: nicht dokumentiert."
            ),
        }

    raw_problems, track_note = _collect_known_problems(entry)

    problems: list[dict] = []
    for problem in raw_problems:
        # Window lives under 'model_years' OR 'period' depending on the entry
        window = problem.get("model_years") or problem.get("period")
        applies = _year_applies(year, window)
        problems.append(
            {
                "issue": _humanize(problem.get("issue")),
                "severity": problem.get("severity", ""),
                "severity_de": _severity_de(problem.get("severity")),
                "model_years": format_year_window_de(window),
                "applies_to_year": applies,
                "applies_note_de": (
                    "Baujahr liegt im betroffenen Fenster"
                    if applies is True
                    else "Baujahr liegt außerhalb des betroffenen Fensters"
                    if applies is False
                    else "Baujahr-Zuordnung nicht möglich"
                    + ("" if year is not None else " (kein Baujahr angegeben)")
                ),
                "description": _humanize(problem.get("description")) or None,
                "detection": _humanize(problem.get("detection")) or None,
                "repair_cost_eur": problem.get("repair_cost_eur"),
                "affected_percentage": _format_percentage_de(
                    problem.get("affected_percentage")
                ),
                "confidence": "documented",
            }
        )

    # Applicable problems first, then undecided, then non-applicable
    problems.sort(
        key=lambda p: {True: 0, None: 1, False: 2}[p["applies_to_year"]]
    )

    problems_note = None
    if not problems and not track_note:
        problems_note = (
            "Die Wissensbasis enthält für diese Werft keine strukturierte "
            "Problemliste — siehe Bauqualitäts-Einordnung. Keine Entwarnung."
        )

    repairs = entry.get("common_repairs_cost_range")
    repair_costs = None
    if isinstance(repairs, dict):
        repair_costs = {
            _humanize(name): list(cost) if isinstance(cost, (tuple, list)) else cost
            for name, cost in repairs.items()
        }

    return {
        "found": True,
        "key": key,
        "display_name": entry.get("key_de") or brand,
        "country": entry.get("country"),
        "model_name": model_name,
        "known_problems": problems,
        "track_record_note_de": track_note,
        "problems_note_de": problems_note,
        "era_note_de": _era_note(entry, year),
        "survey_recommendation": _humanize(entry.get("survey_recommendation")) or None,
        "owner_forum_consensus": _humanize(entry.get("owner_forum_consensus")) or None,
        "common_repair_costs_eur": repair_costs,
        "confidence": "documented",
    }


# Preference order for lifespan resolution. Range tuples first; the string
# fallbacks prefer ACTUAL field data over manufacturer claims.
_LIFESPAN_RANGE_KEYS = (
    "lifespan_range",
    "lifespan_range_temperate",  # standing_rigging_wire (conservative default)
    "lifespan_range_quality",    # sanitation_hoses (quality hose assumption)
)
_LIFESPAN_STRING_KEYS = (
    "typical_lifespan_years",
    "typical_lifespan_years_actual",
    "typical_lifespan_years_volvo_spec",
    "typical_lifespan_years_claimed",
)
_LIFESPAN_BASIS_DE = {
    "lifespan_range_temperate": "gemäßigtes Klima",
    "lifespan_range_quality": "Qualitätsausführung",
    "typical_lifespan_years_actual": "Praxiswerte",
    "typical_lifespan_years_volvo_spec": "Hersteller-Vorgabe",
    "typical_lifespan_years_claimed": "Herstellerangabe",
}


def _resolve_lifespan_range(data: dict) -> tuple[Optional[tuple[float, float]], Optional[str]]:
    """Resolve a (low, high) lifespan from the KB's key variants.

    Reading only `lifespan_range` (old behaviour) silently dropped exactly
    the most critical components: wire standing rigging (mast loss risk),
    saildrive diaphragm, cast-iron exhaust elbows, sanitation hoses.
    """
    for key in _LIFESPAN_RANGE_KEYS:
        value = data.get(key)
        if (
            isinstance(value, (tuple, list))
            and len(value) == 2
            and all(isinstance(v, (int, float)) for v in value)
        ):
            return (float(value[0]), float(value[1])), key
    for key in _LIFESPAN_STRING_KEYS:
        value = data.get(key)
        if isinstance(value, str):
            match = re.fullmatch(
                r"(\d+(?:\.\d+)?)\s*-\s*(\d+(?:\.\d+)?)\+?", value.strip()
            )
            if match:
                return (float(match.group(1)), float(match.group(2))), key
    return None, None


def _age_expectations(age_years: int, boat_class: str) -> list[dict]:
    """Components whose typical lifespan the boat's age approaches/exceeds.

    Derived from MATERIAL_LIFESPAN_DATABASE — statistical expectations
    ("estimated"), NOT findings on the actual boat. Consumables (typical
    lifespan <= 5y, e.g. anodes/impeller) are routine maintenance items whose
    age follows the SERVICE interval, not the build year — they are listed as
    "info: Austauschhistorie erfragen", never as major findings.
    """
    is_sail = boat_class in SAIL_CLASSES
    items: list[dict] = []
    for component_key, data in MATERIAL_LIFESPAN_DATABASE.items():
        if component_key in _EXCLUDED_COMPONENTS:
            continue
        if not is_sail and component_key in _SAIL_ONLY_COMPONENTS:
            continue
        lifespan, basis_key = _resolve_lifespan_range(data)
        if lifespan is None:
            continue  # e.g. balsa_core (wet/dry duality — not age-driven)
        low, high = lifespan

        is_consumable = high <= 5
        if is_consumable:
            if age_years < high:
                continue
            status = (
                "Routine-Wartungsposten (regelmäßiger Austausch) — "
                "Austauschhistorie beim Verkäufer erfragen"
            )
            severity = "info"
        elif age_years >= high:
            status = "Typische Lebensdauer überschritten — prüfen, Austausch einplanen"
            severity = "major"
        elif age_years >= low:
            status = "Im typischen Austauschfenster — Zustand gezielt prüfen"
            severity = "moderate"
        elif low <= 30 and age_years >= 0.7 * low:
            # Early warning only for components in refit-relevant ranges;
            # flagging a 50-80y hull at year 35 would be alarmist.
            status = "Nähert sich dem Ende der typischen Lebensdauer"
            severity = "info"
        else:
            continue

        inspection = data.get("inspection_protocol")
        inspection_hint = None
        if isinstance(inspection, dict) and inspection:
            first_key = next(iter(inspection))
            inspection_hint = _humanize(inspection[first_key])

        cost_range = data.get("replacement_cost_range")
        items.append(
            {
                "component": component_key,
                "component_de": data.get("key_de") or _humanize(component_key),
                "status_de": status,
                "severity": severity,
                "lifespan_years": [low, high],
                "lifespan_basis_de": _LIFESPAN_BASIS_DE.get(basis_key),
                "inspection_hint": inspection_hint,
                "replacement_cost_range_eur": (
                    list(cost_range) if isinstance(cost_range, (tuple, list)) else None
                ),
                "confidence": "estimated",
            }
        )

    severity_order = {"major": 0, "moderate": 1, "info": 2}
    items.sort(key=lambda item: severity_order.get(item["severity"], 3))
    return items


def _community_section(community_patterns: Optional[list[dict]]) -> dict:
    if not community_patterns:
        return {
            "available": False,
            "note": "Keine Community-Berichte zu vergleichbaren Booten vorhanden.",
        }
    patterns = []
    for pattern in community_patterns[:10]:
        description = pattern.get("description") or _humanize(
            pattern.get("category") or pattern.get("issue_category")
        )
        if not description:
            continue  # a warning line without any content helps nobody
        match_reason = pattern.get("match_reason")
        patterns.append(
            {
                "description": description,
                "zone_type": pattern.get("zone_type"),
                "severity": pattern.get("severity_mode") or pattern.get("severity"),
                "report_count": pattern.get("report_count", 0),
                "typical_onset_years": pattern.get("typical_onset_years"),
                "relevance": pattern.get("relevance"),
                "match_reason": match_reason,
                "match_reason_de": _MATCH_REASON_DE.get(
                    match_reason, _humanize(match_reason) or None
                ),
                "is_positive": bool(pattern.get("is_positive", False)),
                "confidence": "documented",
            }
        )
    if not patterns:
        return {
            "available": False,
            "note": "Keine Community-Berichte zu vergleichbaren Booten vorhanden.",
        }
    return {"available": True, "patterns": patterns, "confidence": "documented"}


def get_buyer_insights(
    brand: Optional[str],
    model_name: Optional[str],
    year: Optional[int],
    boat_class: str = "cruising_sail",
    community_patterns: Optional[list[dict]] = None,
    current_year: Optional[int] = None,
) -> dict:
    """Compose the boat-specific buyer report from all knowledge sources.

    Args:
        community_patterns: pre-matched AND relevance-filtered pattern dicts
            (route layer keeps only identity-level matches); None/[] renders
            an honest empty section.
        current_year: injected by the caller (keeps this function pure and
            deterministic for tests).
    """
    if not brand and year is None and not model_name:
        return {
            "available": False,
            "reason": (
                "Keine Boots-Identität angegeben — Marke, Modell oder Baujahr "
                "werden für die Kaufberatung benötigt."
            ),
        }

    age_years: Optional[int] = None
    if year is not None and current_year is not None and current_year >= year:
        age_years = current_year - year

    manufacturer = _manufacturer_section(brand, model_name, year) if brand else {
        "found": False,
        "note": "Keine Werft angegeben.",
    }

    age_section = None
    if age_years is not None:
        age_section = {
            "age_years": age_years,
            "items": _age_expectations(age_years, boat_class),
            "confidence": "estimated",
            "note_de": (
                "Statistische Lebensdauer-Erwartungen für ein Boot dieses "
                "Alters — kein Befund am konkreten Boot."
            ),
        }

    community = _community_section(community_patterns)

    # German one-line summary
    parts: list[str] = []
    if manufacturer.get("found"):
        applicable = [
            p for p in manufacturer["known_problems"] if p["applies_to_year"] is True
        ]
        if applicable:
            parts.append(
                f"{len(applicable)} dokumentierte Typ-Schwachstelle(n) betreffen "
                "dieses Baujahr"
            )
        elif manufacturer.get("track_record_note_de"):
            parts.append("dokumentiert unauffällige Werft-Bilanz")
        elif manufacturer["known_problems"]:
            parts.append(
                f"{len(manufacturer['known_problems'])} dokumentierte "
                "Typ-Schwachstelle(n) (Baujahr-Zuordnung siehe Detail)"
            )
        else:
            parts.append("Werft-Einordnung vorhanden, keine strukturierte Problemliste")
    if age_section and age_section["items"]:
        parts.append(
            f"{len(age_section['items'])} Komponente(n) altersbedingt prüfwürdig"
        )
    if community.get("available"):
        parts.append(f"{len(community['patterns'])} Community-Muster")
    identity = " ".join(
        str(x) for x in (brand, model_name, f"({year})" if year else None) if x
    )
    summary = (
        f"Kaufprüfung {identity}: " + "; ".join(parts) + "."
        if parts
        else f"Kaufprüfung {identity}: keine dokumentierten Auffälligkeiten in der "
        "Wissensbasis — das ist keine Entwarnung, nur fehlende Dokumentation."
    )

    return {
        "available": True,
        "boat_identity": {
            "brand": brand,
            "model_name": model_name,
            "year": year,
            "age_years": age_years,
            "boat_class": boat_class,
        },
        "manufacturer": manufacturer,
        "age_expectations": age_section,
        "community": community,
        "summary_de": summary,
        "disclaimer_de": (
            "Diese Kaufberatung basiert auf dokumentiertem Typ-Wissen und "
            "statistischen Lebensdauern. Sie ersetzt keine Besichtigung und "
            "kein Gutachten (Survey) am konkreten Boot. Detailtexte stammen "
            "teilweise unübersetzt aus der internationalen Wissensbasis (EN)."
        ),
    }
