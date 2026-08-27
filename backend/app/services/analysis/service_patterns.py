"""Service Pattern Analysis module for yacht layouts.

Mines historical service reports for patterns that should inform new designs.
Rule-based analysis — no ML. Identifies problematic zone types, age-related
failure windows, recurring material failures, and correlates these against
the current layout to generate proactive design warnings.
Pure function module — no database access.
All user-facing strings are in German.
"""
import logging
from app.services.analysis.scoring import weighted_overall, hinweis_teilanalysen


logger = logging.getLogger(__name__)


def _knowledge_lookup_hint(source: str) -> str:
    """Handlungsvorschlag fuer Wissensbefunde ohne hinterlegte Massnahme.

    Der Korpus fuehrt nicht zu jedem Fehlerbild eine Massnahme. Statt die
    Warnung ohne Vorschlag auszuliefern (Konventionsbruch) oder einen Rat zu
    erfinden (Belegbruch), verweist sie auf den Quellartikel.
    """
    label = (source or "").strip().replace("_", " ")
    if not label:
        return "Zugehörigen Wissensartikel im Lexikon nachschlagen — im Korpus ist für dieses Fehlerbild keine Maßnahme hinterlegt."
    return (
        f"Im Wissensartikel „{label[:80]}\" nachschlagen — für dieses Fehlerbild "
        f"ist im Korpus keine Maßnahme hinterlegt."
    )


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

# Import central knowledge retrieval for markdown knowledge integration
try:
    from app.services.knowledge.knowledge_retrieval import (
        get_knowledge_for_service_patterns as _get_md_service_knowledge,
        MARKDOWN_LOADER_AVAILABLE as _MD_AVAILABLE,
    )
except ImportError:
    _MD_AVAILABLE = False

    def _get_md_service_knowledge(*a, **kw):
        return {}

BOAT_CLASS_DEFAULTS = {
    "small_sail": {
        "min_reports_for_pattern": 3,
        "high_issue_threshold": 5,  # 5+ weighted score in a zone_type = concerning
        "critical_age_window_months": 36,
        "weights": {
            "zone_issues": 0.222,
            "age_patterns": 0.185,
            "material_failures": 0.185,
            "design_warnings": 0.148,
            "severity_burden": 0.26,
        },
    },
    "cruising_sail": {
        "min_reports_for_pattern": 3,
        "high_issue_threshold": 5,
        "critical_age_window_months": 48,
        "weights": {
            "zone_issues": 0.185,
            "age_patterns": 0.185,
            "material_failures": 0.185,
            "design_warnings": 0.185,
            "severity_burden": 0.26,
        },
    },
    "large_motor": {
        "min_reports_for_pattern": 4,
        "high_issue_threshold": 4,
        "critical_age_window_months": 60,
        "weights": {
            "zone_issues": 0.185,
            "age_patterns": 0.148,
            "material_failures": 0.222,
            "design_warnings": 0.185,
            "severity_burden": 0.26,
        },
    },
    "racing_sail": {
        "min_reports_for_pattern": 2,
        "high_issue_threshold": 6,
        "critical_age_window_months": 24,
        "weights": {
            "zone_issues": 0.259,
            "age_patterns": 0.148,
            "material_failures": 0.148,
            "design_warnings": 0.185,
            "severity_burden": 0.26,
        },
    },
    "daysailer": {
        "min_reports_for_pattern": 3,
        "high_issue_threshold": 5,
        "critical_age_window_months": 36,
        "weights": {
            "zone_issues": 0.222,
            "age_patterns": 0.185,
            "material_failures": 0.1702,
            "design_warnings": 0.1628,
            "severity_burden": 0.26,
        },
    },
    "motorsailer": {
        "min_reports_for_pattern": 3,
        "high_issue_threshold": 5,
        "critical_age_window_months": 48,
        "weights": {
            "zone_issues": 0.1924,
            "age_patterns": 0.1776,
            "material_failures": 0.185,
            "design_warnings": 0.185,
            "severity_burden": 0.26,
        },
    },
    "catamaran_sail": {
        "min_reports_for_pattern": 3,
        "high_issue_threshold": 5,
        "critical_age_window_months": 48,
        "weights": {
            "zone_issues": 0.1924,
            "age_patterns": 0.1776,
            "material_failures": 0.185,
            "design_warnings": 0.185,
            "severity_burden": 0.26,
        },
    },
    "catamaran_motor": {
        "min_reports_for_pattern": 4,
        "high_issue_threshold": 4,
        "critical_age_window_months": 60,
        "weights": {
            "zone_issues": 0.185,
            "age_patterns": 0.148,
            "material_failures": 0.222,
            "design_warnings": 0.185,
            "severity_burden": 0.26,
        },
    },
    "small_motor": {
        "min_reports_for_pattern": 3,
        "high_issue_threshold": 4,
        "critical_age_window_months": 55,
        "weights": {
            "zone_issues": 0.185,
            "age_patterns": 0.1554,
            "material_failures": 0.2146,
            "design_warnings": 0.185,
            "severity_burden": 0.26,
        },
    },
    "sport_cruiser": {
        "min_reports_for_pattern": 4,
        "high_issue_threshold": 4,
        "critical_age_window_months": 60,
        "weights": {
            "zone_issues": 0.185,
            "age_patterns": 0.148,
            "material_failures": 0.222,
            "design_warnings": 0.185,
            "severity_burden": 0.26,
        },
    },
    "trawler": {
        "min_reports_for_pattern": 4,
        "high_issue_threshold": 4,
        "critical_age_window_months": 72,
        "weights": {
            "zone_issues": 0.1776,
            "age_patterns": 0.1406,
            "material_failures": 0.2294,
            "design_warnings": 0.1924,
            "severity_burden": 0.26,
        },
    },
    "explorer": {
        "min_reports_for_pattern": 4,
        "high_issue_threshold": 3,
        "critical_age_window_months": 72,
        "weights": {
            "zone_issues": 0.148,
            "age_patterns": 0.1406,
            "material_failures": 0.2294,
            "design_warnings": 0.222,
            "severity_burden": 0.26,
        },
    },
    "superyacht": {
        "min_reports_for_pattern": 4,
        "high_issue_threshold": 3,
        "critical_age_window_months": 60,
        "weights": {
            "zone_issues": 0.148,
            "age_patterns": 0.148,
            "material_failures": 0.222,
            "design_warnings": 0.222,
            "severity_burden": 0.26,
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
# Free-text severity extraction (L-5) — Pipeline C previously ignored the
# description field entirely, so identical structured reports with wildly
# different text scored the same. Derive an implied severity from damage
# keywords, with negation handling so "keine Osmose" does not escalate.
# ---------------------------------------------------------------------------
_TEXT_SEVERITY_KEYWORDS: dict[str, tuple[str, ...]] = {
    "critical": (
        "totalschaden", "kernschaden", "delaminiert", "wassereinbruch",
        "nicht seetüchtig", "nicht mehr seetüchtig", "durchgerostet",
        "gebrochen", "abgerissen", "gerissen", "wasser im kiel",
    ),
    "high": (
        "osmose", "korrosion", "undicht", "morsch", "durchfeuchtet",
        "leck", "defekt", "verschlissen", "ausgeschlagen", "faul", "riss",
    ),
    "medium": (
        "spiel", "verschleiß", "abnutzung", "gebrauchsspuren", "oberflächlich",
    ),
}
_SEVERITY_RANK = {"low": 0, "medium": 1, "high": 2, "critical": 3}
_NEGATIONS = ("kein", "keine", "keinerlei", "ohne", "nicht", "frei von")


def _derive_text_severity(description: str | None) -> str | None:
    """Highest severity implied by non-negated damage keywords in the text.

    Scans critical→high→medium; a keyword occurrence preceded (within ~25 chars)
    by a negation ("keine Osmose", "ohne Befund") is ignored. Returns None when
    no damage is described.
    """
    if not description:
        return None
    text = description.lower()
    for sev in ("critical", "high", "medium"):
        for kw in _TEXT_SEVERITY_KEYWORDS[sev]:
            idx = text.find(kw)
            while idx != -1:
                prefix = text[max(0, idx - 25):idx]
                if not any(neg in prefix for neg in _NEGATIONS):
                    return sev
                idx = text.find(kw, idx + 1)
    return None


def _apply_text_severity(reports: list[dict]) -> tuple[list[dict], list[dict]]:
    """Lift each report's effective severity to at least what its text implies.

    Returns (effective_reports, underreport_warnings). A report whose free text
    describes worse damage than its recorded severity is both escalated (so the
    text affects the score) and flagged (L-5, and partially the L-4b
    under-reporting/contradiction case).
    """
    effective: list[dict] = []
    underreports: list[dict] = []
    for r in reports:
        text_sev = _derive_text_severity(r.get("description"))
        struct_sev = r.get("severity", "low")
        if text_sev and _SEVERITY_RANK.get(text_sev, 0) > _SEVERITY_RANK.get(struct_sev, 0):
            underreports.append({
                "code": "SERVICE_TEXT_UNDERREPORT",
                "severity": "warning",
                "message": (
                    f"Freitext (Zone '{r.get('zone_type', '?')}') deutet auf "
                    f"Schweregrad '{text_sev}' hin, erfasst war '{struct_sev}'."
                ),
                "suggestion": "Schweregrad des Serviceberichts an die Beschreibung anpassen.",
            })
            r = {**r, "severity": text_sev}
        effective.append(r)
    return effective, underreports


# ---------------------------------------------------------------------------
# Sub-analysis 1: Zone type issues
# ---------------------------------------------------------------------------


def analyze_zone_type_issues(
    zones: list[dict],
    service_reports: list[dict],
    config: dict,
) -> tuple[float | None, list[dict], dict]:
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
    # Berichte ohne Zonenzuordnung sind fuer diese Auswertung unsichtbar. Wurden
    # sie alle uebersprungen, blieb die Sammlung leer, es gab nichts
    # Auffaelliges — und die Pruefung meldete 100.0 fuer eine Flotte, deren
    # Serviceberichte gar nicht zugeordnet werden konnten.
    berichte_mit_zone = 0
    for report in service_reports:
        zt = report.get("zone_type")
        if not zt:
            continue
        berichte_mit_zone += 1
        # A documented clean inspection is a POSITIVE signal, not a defect
        # (L-12). Don't let a routine "no findings" check raise a zone's problem
        # score. Only inspections that actually flagged something (elevated
        # severity or a cost) still count.
        if report.get("report_type") == "inspection" and \
                report.get("severity", "low") in ("low", "none") and \
                not report.get("cost_eur"):
            continue
        sev = report.get("severity", "low")
        weight = _REPORT_SEVERITY_WEIGHT.get(sev, 1)
        zone_type_scores[zt] = zone_type_scores.get(zt, 0.0) + weight

    if berichte_mit_zone == 0:
        return None, [{
            "code": "SERVICE_ZONE_ISSUES_NOT_ASSESSABLE",
            "severity": "info",
            "message": (
                f"Zonenbezogene Servicemuster nicht beurteilbar: keiner der "
                f"{len(service_reports)} Serviceberichte nennt einen Zonentyp."
            ),
            "suggestion": "Serviceberichte beim Erfassen einem Zonentyp zuordnen.",
            "location": "service_reports.zone_type",
        }], {
            "zone_type_scores": {},
            "problematic_zone_types": [],
            "threshold": threshold,
            "reports_with_zone": 0,
        }

    # L-10 (see analyze_material_failures): above ~30 reports a zone should also
    # stand out from the average zone, so uniform noise doesn't flag everything.
    #
    # Dieser relative Filter darf aber nur greifen, wenn es überhaupt mehrere
    # Zonentypen zum Vergleichen gibt. Sonst kehrt er sich um: Bei EINEM
    # betroffenen Zonentyp ist der Mittelwert genau dessen Wert, `1.5 * mean`
    # liegt also immer darüber und der Befund wird ausgerechnet dann unterdrückt,
    # wenn die Evidenz am eindeutigsten ist. Gemessen: 60 Totalschäden in einer
    # Zone wurden mit 93,8 besser bewertet als 20 (90,0), weil ab 31 Berichten
    # alle Befunde verschwanden. Ab drei Zonentypen ist ein Mittelwert
    # aussagekräftig — darunter zählt allein die absolute Schwelle.
    mean_zone_score = (
        sum(zone_type_scores.values()) / len(zone_type_scores)
    ) if zone_type_scores else 0.0
    relative_gate = (
        1.5 * mean_zone_score
        if len(service_reports) > 30 and len(zone_type_scores) >= 3
        else 0.0
    )

    problematic: list[str] = []
    for zt, score_val in zone_type_scores.items():
        if score_val >= threshold and score_val >= relative_gate:
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
        "reports_with_zone": berichte_mit_zone,
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

    # Average over ALL buckets, not only the filled ones (L-7). Dividing by the
    # filled-bucket count made a spike mathematically impossible when reports
    # clustered in one or two windows: with a single filled bucket the average
    # equalled the count, so "count > 2×avg" could never fire — exactly the
    # clearest serial-defect case (all failures at one age) scored a perfect 100.
    avg = total / len(_AGE_BUCKETS)

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
) -> tuple[float | None, list[dict], dict]:
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
    # Ohne Materialangabe im Bericht gibt es nichts zu zaehlen. Nannten alle
    # Berichte kein Material, blieb die Zaehlung leer und die Pruefung meldete
    # 100.0 — eine Unbedenklichkeitsbescheinigung fuer saemtliche Materialien,
    # ueber die nichts bekannt war.
    berichte_mit_material = 0
    for report in service_reports:
        materials = report.get("materials_involved") or []
        if isinstance(materials, str):
            materials = [materials]
        gezaehlt = False
        for mat in materials:
            if mat:
                material_counts[mat] = material_counts.get(mat, 0) + 1
                gezaehlt = True
        if gezaehlt:
            berichte_mit_material += 1

    if berichte_mit_material == 0:
        return None, [{
            "code": "SERVICE_MATERIAL_NOT_ASSESSABLE",
            "severity": "info",
            "message": (
                f"Materialbezogene Ausfallmuster nicht beurteilbar: keiner der "
                f"{len(service_reports)} Serviceberichte nennt ein beteiligtes Material."
            ),
            "suggestion": "Beteiligte Materialien im Servicebericht erfassen (materials_involved).",
            "location": "service_reports.materials_involved",
        }], {
            "material_counts": {},
            "problematic_materials": [],
            "min_reports_threshold": min_reports,
            "reports_with_material": 0,
        }

    # L-10: a fixed absolute count flags every material once the dataset is
    # large (e.g. 100 reports → each material trivially clears 3). Above ~30
    # reports also require the material to stand out from the average material;
    # small realistic datasets keep the sensitive absolute floor unchanged.
    mean_count = (sum(material_counts.values()) / len(material_counts)) if material_counts else 0.0
    relative_gate = 1.5 * mean_count if len(service_reports) > 30 else 0.0

    problematic_materials: list[str] = []
    for mat, count in material_counts.items():
        if count >= min_reports and count >= relative_gate:
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
        "reports_with_material": berichte_mit_material,
    }


# ---------------------------------------------------------------------------
# Sub-analysis 4: Design warnings (correlation with current layout)
# ---------------------------------------------------------------------------


def analyze_design_warnings(
    zones: list[dict],
    service_reports: list[dict],
    config: dict,
) -> tuple[float | None, list[dict], dict]:
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
    berichte_mit_zone = 0
    for report in service_reports:
        zt = report.get("zone_type")
        if not zt:
            continue
        berichte_mit_zone += 1
        sev = report.get("severity", "low")
        weight = _REPORT_SEVERITY_WEIGHT.get(sev, 1)
        zone_type_scores[zt] = zone_type_scores.get(zt, 0.0) + weight

    if berichte_mit_zone == 0:
        # Ohne zugeordnete Berichte gibt es keinen Abgleich mit dem Layout. Die
        # frueheren 100.0 bescheinigten dem Entwurf, keinem bekannten
        # Problemmuster zu entsprechen — es war nur kein Muster bekannt.
        return None, [{
            "code": "SERVICE_DESIGN_WARNINGS_NOT_ASSESSABLE",
            "severity": "info",
            "message": (
                "Abgleich des Layouts mit Servicemustern nicht möglich: kein "
                "Servicebericht ist einem Zonentyp zugeordnet."
            ),
            "suggestion": "Serviceberichte beim Erfassen einem Zonentyp zuordnen.",
            "location": "service_reports.zone_type",
        }], {
            "problematic_types_in_history": [],
            "matched_zone_count": None,
            "matched_zone_types": [],
        }

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



def analyze_severity_burden(
    service_reports: list[dict],
    config: dict,
) -> tuple[float, list[dict], dict]:
    """Bewertet die tatsaechliche Schadenslast, nicht nur deren Musterhaftigkeit.

    Warum es diese Teilanalyse gibt: Die vier urspruenglichen Teilanalysen sind
    reine MUSTER-Detektoren — sie fragen "sticht eine Zone / ein Alter / ein
    Material heraus?". Keine davon bewertet, WIE SCHLIMM das Gemeldete ist.
    Gemessen (vorher): ein einzelner Totalschaden mit ``severity: critical`` und
    zehn davon ergaben exakt dieselbe Note wie zehn kosmetische ``low``-Berichte
    (95,0 bzw. 90,0). Da der Modulwert in die Gesamtnote eingeht, hob ein
    gemeldeter Schaden die Gesamtbewertung sogar an, statt sie zu senken.

    Fuer Marc (Kaeufer) und Kai (Eigner) ist genau das die Kernfrage: Nicht
    "haeufen sich Meldungen an einer Stelle?", sondern "wie schwer ist das, was
    dieses Boot hinter sich hat?".

    Bewertungslogik: Jeder Bericht traegt sein Schweregewicht bei
    (kritisch 4 ... niedrig 1); dokumentierte, unauffaellige Inspektionen zaehlen
    nicht als Last. Die Summe wird gegen eine klassenabhaengige Toleranz
    normiert. Ein einzelner kritischer Befund kostet damit spuerbar Punkte, viele
    schwere Befunde fuehren in den unteren Bereich.

    Returns (score 0-100, warnings, metrics).
    """
    warnings: list[dict] = []

    burden = 0.0
    counted = 0
    by_severity: dict[str, int] = {}
    for report in service_reports:
        severity = report.get("severity", "low")
        # Eine saubere Inspektion ohne Befund und ohne Kosten ist ein POSITIVES
        # Signal — dieselbe Ausnahme wie in analyze_zone_type_issues.
        if (
            report.get("report_type") == "inspection"
            and severity in ("low", "none")
            and not report.get("cost_eur")
        ):
            continue
        weight = _REPORT_SEVERITY_WEIGHT.get(severity, 1)
        burden += weight
        counted += 1
        by_severity[severity] = by_severity.get(severity, 0) + 1

    if counted == 0:
        return 100.0, warnings, {
            "burden_points": 0.0,
            "counted_reports": 0,
            "by_severity": {},
            "note": "Nur unauffaellige Inspektionen dokumentiert.",
        }

    # Toleranz: ab wie vielen Schwerepunkten gilt die Historie als deutlich
    # belastet. Bewusst klassenabhaengig — eine Charteryacht sammelt naturgemaess
    # mehr Eintraege als ein privat gefahrener Daysailer.
    # Kalibrierung: Ein einzelner als "critical" gemeldeter Befund wiegt 4 Punkte.
    # Bei einer Toleranz von 12 landet er damit bei 66,7 — deutlich sichtbar, aber
    # nicht vernichtend; drei kritische Befunde (oder vier schwere) erreichen 0.
    # Mit dem urspruenglichen Wert 24 kam ein kritischer Strukturschaden auf 83,3,
    # was fuer einen Kaeufer ein irrefuehrend gutes Zeugnis gewesen waere.
    tolerance = float(config.get("severity_burden_tolerance", 12))
    score = max(0.0, 100.0 - (burden / tolerance) * 100.0)

    critical_count = by_severity.get("critical", 0)
    high_count = by_severity.get("high", 0)

    if critical_count:
        warnings.append({
            "code": "SERVICE_SEVERITY_CRITICAL",
            "severity": "critical",
            "message": (
                f"{critical_count} als kritisch eingestufte(r) Servicebefund(e) in der "
                f"Historie (Schwerelast gesamt: {burden:.0f} Punkte)."
            ),
            "suggestion": (
                "Befunde vor einem Kauf oder einer groesseren Investition durch eine "
                "Sachverstaendige oder einen Sachverstaendigen pruefen lassen und die "
                "Behebung belegen lassen."
            ),
        })
    elif high_count >= 3:
        warnings.append({
            "code": "SERVICE_SEVERITY_HIGH",
            "severity": "warning",
            "message": (
                f"{high_count} Servicebefunde mit hoher Schwere "
                f"(Schwerelast gesamt: {burden:.0f} Punkte)."
            ),
            "suggestion": (
                "Haeufung schwerer Befunde auf eine gemeinsame Ursache pruefen "
                "(Nutzungsprofil, Revier, Wartungsintervalle)."
            ),
        })

    return score, warnings, {
        "burden_points": round(burden, 1),
        "counted_reports": counted,
        "by_severity": by_severity,
        "tolerance": tolerance,
    }


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
        return {"available": False, "reason": f"Unbekannte Bootsklasse: {boat_class}"}

    config = BOAT_CLASS_DEFAULTS[boat_class].copy()
    weights = config.pop("weights").copy()

    if config_overrides:
        config.update(config_overrides)

    reports = service_reports or []

    # Dieses Modul wertet ausschliesslich Erfahrung aus der Flotte aus. Ohne
    # Serviceberichte hat es keine Grundlage. Frueher gab es hier 50.0 zurueck —
    # ein Wert, der wie ein Befund aussah, aber keiner war.
    if not reports:
        return {
            "module": "service_patterns",
            "available": False,
            "reason": (
                "Keine Serviceberichte vorhanden — ohne Betriebserfahrung "
                "lassen sich keine wiederkehrenden Muster erkennen."
            ),
            "suggestions": [
                "Serviceberichte erfassen und mit Layouts verknüpfen, "
                "um Musteranalysen zu ermöglichen."
            ],
        }

    # L-5: read the free-text description — lift effective severity from it so
    # the analysis reflects what the text says, not only the structured fields.
    reports, text_underreports = _apply_text_severity(reports)

    sub_scores: dict[str, float | None] = {}
    all_warnings: list[dict] = list(text_underreports)
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
        (
            "severity_burden",
            lambda: analyze_severity_burden(reports, config),
        ),
    ]

    _failed_subs: set[str] = set()

    for name, fn in analyses:
        try:
            score, warnings, metrics = fn()
            sub_scores[name] = score
            all_warnings.extend(warnings)
            all_metrics[name] = metrics
        except Exception:
            logger.exception("Error in service_patterns sub-analysis %s", name)
            # Kein Messwert. None statt 0.0: weighted_overall nimmt die
            # Teilanalyse damit aus Zaehler UND Nenner, statt einen internen
            # Fehler als schlechte Note am Boot auszugeben.
            sub_scores[name] = None
            _failed_subs.add(name)
            all_warnings.append({
                "code": "ANALYSIS_ERROR",
                "severity": "critical",
                "message": f"Fehler bei Servicemuster-Analyse: {name}",
                "suggestion": "Serviceberichte auf Vollständigkeit und Format prüfen.",
            })

    # Teilanalysen ohne Datengrundlage geben None zurueck und bleiben aus der
    # Rechnung heraus; ihr Gewicht verteilt sich auf die geprueften. Frueher
    # ging hier ein Vorgabewert ein — bei fehlenden Eintraegen 0.0 bzw. 50.0 —
    # und erzeugte eine Note fuer etwas, das nie geprueft wurde.
    overall, _nicht_bewertet = weighted_overall(sub_scores, weights)
    if overall is None:
        return {
            "module": "service_patterns",
            "available": False,
            "reason": "Keine der Teilanalysen konnte mangels Datengrundlage durchgeführt werden.",
            "degraded_subanalyses": sorted(_failed_subs),
            "warnings": all_warnings,
            "suggestions": [
                "Layout- und Stammdaten vervollständigen, um eine Bewertung zu ermöglichen."
            ],
        }

    for w in all_warnings:
        suggestion = w.get("suggestion")
        if suggestion and suggestion not in all_suggestions:
            all_suggestions.append(suggestion)

    all_warnings.sort(key=lambda w: SEVERITY_ORDER.get(w.get("severity", "info"), 2))

    # =========================================================================
    # MARKDOWN KNOWLEDGE ENRICHMENT — Fallstudien, Erfahrungsberichte
    # =========================================================================

    knowledge_enrichment = {}
    if _MD_AVAILABLE:
        try:
            md_service = _get_md_service_knowledge(
                hull_material="grp",
                hull_construction=None,
            )

            # Add real fallstudien from markdown knowledge
            md_fallstudien = md_service.get("markdown_fallstudien", [])
            knowledge_enrichment["markdown_fallstudien"] = md_fallstudien[:15]

            # Add erfahrungsberichte
            md_erfahrungen = md_service.get("markdown_erfahrungsberichte", [])
            knowledge_enrichment["markdown_erfahrungsberichte"] = md_erfahrungen[:15]

            # Add markdown fehlerbilder as design warnings
            for fm in md_service.get("common_failure_modes", []):
                if isinstance(fm, dict) and fm.get("title"):
                    all_warnings.append({
                        "code": "MD_SERVICE_FEHLERBILD",
                        "severity": "info",
                        "message": (
                            f"[Wissensdatenbank: {fm.get('source', '')}] "
                            f"{fm.get('title', '')}: {fm.get('symptom', '')[:120]}"
                        ),
                        # Siehe materials.py: Verweis statt erfundener Maßnahme.
                        "suggestion": (
                            fm.get("massnahme", "")[:150]
                            if fm.get("massnahme")
                            else _knowledge_lookup_hint(fm.get("source", ""))
                        ),
                        "source": "markdown",
                    })
        except Exception:
            logger.exception("Error enriching service_patterns with markdown knowledge")


    return {
        "module": "service_patterns",
        "degraded_subanalyses": sorted(_failed_subs),
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
        # Pipeline C: results derive from documented service reports, so the
        # canonical provenance is "documented" (not "measured"/"estimated").
        "confidence": "documented",
        "confidence_note": "Aus dokumentierten Serviceberichten abgeleitet.",
        "knowledge_enrichment": knowledge_enrichment if knowledge_enrichment else None,
        "coverage_note": hinweis_teilanalysen(_nicht_bewertet),
        "unassessed_sub_analyses": _nicht_bewertet,
    }
