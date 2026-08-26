"""Regressionstests fuer den Konfidenz-Waechter der visuellen Analyse.

Deckt die Audit-Befunde B-1 (Key-Mismatch confidence_overall), B-2
(assessable=false schlaegt nicht durch), B-5 (Unbekanntes wird hochgestuft)
und B-13 (Bildguete aus Metadaten wird als gemessen ausgegeben) ab.
"""
import pytest

from app.services.visual.confidence import (
    CONFIDENCE_KEY_ALIASES,
    ConfidenceAssessment,
    ConfidenceGatekeeper,
    VisualConfidence,
)


GOOD_METADATA = {"width": 1920, "height": 1080, "file_size_bytes": 600_000}


@pytest.fixture
def gk() -> ConfidenceGatekeeper:
    return ConfidenceGatekeeper()


# ---------------------------------------------------------------------------
# B-1: Selbsteinschaetzung des Build-Quality-Prompts wird gelesen
# ---------------------------------------------------------------------------


def _build_quality_response(confidence: str) -> dict:
    """Antwortform von prompts/quality.py (interior_detail / exterior_detail)."""
    return {
        "assessable": True,
        "overall_quality_score": 72.0,
        "overall_findings": [{"category": "joinery", "assessment": "neutral"}],
        "cannot_assess": [],
        "confidence_overall": confidence,
        "confidence_reasoning": "Beleuchtung erlaubt nur grobe Beurteilung",
    }


def test_build_quality_confidence_overall_is_read(gk):
    """B-1: 'confidence_overall' zaehlt genauso wie 'confidence'."""
    result = gk.evaluate(_build_quality_response("niedrig"), GOOD_METADATA)
    assert result.assessment_certainty == 0.3


def test_build_quality_low_confidence_is_not_usable(gk):
    """B-1: 'niedrig' des Modells darf nicht als belastbares Ergebnis erscheinen."""
    result = gk.evaluate(_build_quality_response("niedrig"), GOOD_METADATA)
    assert result.is_usable is False
    assert result.level in (VisualConfidence.LOW, VisualConfidence.INSUFFICIENT)


def test_build_quality_high_confidence_still_usable(gk):
    """B-1: Der Fix darf gute Build-Quality-Ergebnisse nicht abwuergen."""
    result = gk.evaluate(_build_quality_response("hoch"), GOOD_METADATA)
    assert result.assessment_certainty == 0.9
    assert result.is_usable is True


def test_build_quality_overall_findings_count_as_findings(gk):
    """B-1: Die Befundliste des Quality-Prompts heisst 'overall_findings'."""
    with_findings = gk._assess_content_relevance(_build_quality_response("hoch"))
    without = dict(_build_quality_response("hoch"))
    without["overall_findings"] = []
    assert with_findings > gk._assess_content_relevance(without)


def test_all_prompt_confidence_keys_are_registered():
    """Beide real vorkommenden Top-Level-Keys stehen in der Alias-Liste."""
    assert "confidence" in CONFIDENCE_KEY_ALIASES
    assert "confidence_overall" in CONFIDENCE_KEY_ALIASES


def test_lowest_stated_confidence_wins(gk):
    """Mehrere Konfidenzangaben: konservativ zaehlt die niedrigste."""
    ai = {"assessable": True, "confidence": "hoch", "confidence_overall": "niedrig"}
    assert gk._resolve_stated_certainty(ai) == 0.3


# ---------------------------------------------------------------------------
# B-2: assessable=false ist ein hartes Veto
# ---------------------------------------------------------------------------


def test_assessable_false_forces_insufficient(gk):
    """B-2: Explizites 'nicht beurteilbar' schlaegt jede Rechnung."""
    ai = {
        "assessable": False,
        "confidence": "hoch",
        "spatial_score": 88,
        "findings": [{"aspect": "salon", "observation": "gut"}],
        "cannot_assess": [],
    }
    result = gk.evaluate(ai, GOOD_METADATA)
    assert result.level == VisualConfidence.INSUFFICIENT
    assert result.is_usable is False
    assert result.model_assessable is False


def test_assessable_false_property_vetoes_is_usable():
    """B-2: Auch eine direkt gebaute Bewertung ist mit dem Veto unbrauchbar."""
    assert ConfidenceAssessment(
        level=VisualConfidence.HIGH, model_assessable=False
    ).is_usable is False
    assert ConfidenceAssessment(
        level=VisualConfidence.HIGH, model_assessable=True
    ).is_usable is True


@pytest.mark.parametrize("value", [False, 0, "false", "nein", "NEIN", "nicht beurteilbar", None])
def test_assessable_negative_variants(gk, value):
    """B-2: Auch String-/Zahlvarianten des Modells greifen."""
    assert gk._resolve_assessable({"assessable": value}) is False


@pytest.mark.parametrize("value", [True, 1, "true", "ja"])
def test_assessable_positive_variants(gk, value):
    assert gk._resolve_assessable({"assessable": value}) is True


def test_assessable_unknown_string_is_conservative(gk):
    """Unverstaendliche Angabe -> konservativ 'nicht beurteilbar'."""
    assert gk._resolve_assessable({"assessable": "vielleicht"}) is False


def test_assessable_missing_is_none(gk):
    """Fehlt das Feld, gibt es kein Veto — aber auch keine Bestaetigung."""
    assert gk._resolve_assessable({"confidence": "hoch"}) is None


# ---------------------------------------------------------------------------
# B-5: Unbekanntes wird nach unten bewertet
# ---------------------------------------------------------------------------


def test_unknown_confidence_word_is_downgraded(gk):
    """B-5: Unbekannter Begriff darf nicht auf 0.6 hochgestuft werden."""
    ai = {
        "assessable": True,
        "spatial_score": 80,
        "confidence": "voellig unklar",
        "findings": [{"aspect": "a"}],
    }
    result = gk.evaluate(ai, GOOD_METADATA)
    assert result.assessment_certainty == gk.UNKNOWN_CERTAINTY
    assert result.assessment_certainty < gk.MIN_ASSESSMENT_CERTAINTY
    assert result.is_usable is False


def test_missing_confidence_with_score_is_downgraded(gk):
    """B-5: Vorhandene Scores sind kein Ersatz fuer eine Selbsteinschaetzung."""
    ai = {"assessable": True, "overall_quality_score": 91, "findings": [{"a": 1}]}
    result = gk.evaluate(ai, GOOD_METADATA)
    assert result.assessment_certainty == gk.UNKNOWN_CERTAINTY
    assert result.is_usable is False


def test_bool_confidence_is_not_certainty_one(gk):
    """B-5: 'confidence': true ist keine Sicherheitsangabe."""
    ai = {"assessable": True, "confidence": True, "findings": [{"a": 1}]}
    result = gk.evaluate(ai, GOOD_METADATA)
    assert result.assessment_certainty == gk.UNKNOWN_CERTAINTY
    assert result.is_usable is False


def test_percent_confidence_is_scaled_not_clamped(gk):
    """B-5: 90 ist eine Prozentangabe, kein 1.0."""
    ai = {"assessable": True, "confidence": 90, "findings": [{"a": 1}]}
    assert gk.evaluate(ai, GOOD_METADATA).assessment_certainty == 0.9


def test_out_of_range_confidence_is_unknown(gk):
    """Unsinnige Zahlen gelten als keine Angabe."""
    assert gk._resolve_stated_certainty({"confidence": -3}) is None
    assert gk._resolve_stated_certainty({"confidence": 4000}) is None


def test_material_word_scale_is_understood(gk):
    """Der Materialprompt benutzt sicher/wahrscheinlich/vermutet."""
    assert gk._resolve_stated_certainty({"confidence": "vermutet"}) == 0.3
    assert gk._resolve_stated_certainty({"confidence": "sicher"}) == 0.9


def test_empty_response_is_insufficient(gk):
    """Leere Antwort: nichts bekannt -> nichts belastbar."""
    result = gk.evaluate({}, GOOD_METADATA)
    assert result.is_usable is False


# ---------------------------------------------------------------------------
# B-13: Bildguete ohne Schaerfe-/Belichtungspruefung ist gedeckelt
# ---------------------------------------------------------------------------


def test_metadata_only_quality_is_capped(gk):
    """B-13: Ein 4K-Foto bei Nacht bekommt keine 1.0 aus Metadaten."""
    score, measured = gk._assess_image_quality_detail(
        {"width": 3840, "height": 2160, "file_size_bytes": 3_000_000}
    )
    assert measured is False
    assert score == pytest.approx(gk.METADATA_ONLY_QUALITY_CAP)
    assert score < 1.0


def test_metadata_only_is_flagged_in_assessment(gk):
    """B-13: Die Einschraenkung ist im Ergebnis sichtbar."""
    result = gk.evaluate(
        {"assessable": True, "confidence": "hoch", "findings": [{"a": 1}]},
        GOOD_METADATA,
    )
    assert result.image_quality_measured is False
    assert any("Metadaten" in f for f in result.factors)


def test_perceptual_metrics_lower_the_score(gk):
    """B-13: Werden Schaerfe/Helligkeit geliefert, zaehlt der schlechtere Befund."""
    blurry, measured = gk._assess_image_quality_detail(
        {
            "width": 3840,
            "height": 2160,
            "file_size_bytes": 3_000_000,
            "sharpness": 0.05,
            "brightness": 0.5,
        }
    )
    assert measured is True
    assert blurry == pytest.approx(0.05)


def test_dark_image_is_penalised(gk):
    """B-13: Eine Nachtaufnahme faellt unter die Mindestbildqualitaet."""
    score, measured = gk._assess_image_quality_detail(
        {
            "width": 3840,
            "height": 2160,
            "file_size_bytes": 3_000_000,
            "sharpness": 1.0,
            "brightness": 0.05,
        }
    )
    assert measured is True
    assert score < gk.MIN_IMAGE_QUALITY


def test_invalid_perceptual_metrics_are_ignored(gk):
    """Unbrauchbare Metriken fallen auf die gedeckelte Metadaten-Bewertung zurueck."""
    score, measured = gk._assess_image_quality_detail(
        {
            "width": 3840,
            "height": 2160,
            "file_size_bytes": 3_000_000,
            "sharpness": "scharf",
            "brightness": 7,
        }
    )
    assert measured is False
    assert score == pytest.approx(gk.METADATA_ONLY_QUALITY_CAP)
