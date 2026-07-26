"""
Tests for pillar 2 (Kaufberatung): buyer_insights service + public endpoint.

Service tests are pure (no DB); the HTTP test exercises the public
/quick-analysis/buyer-insights endpoint via TestClient.
"""

from fastapi.testclient import TestClient

from app.main import app
from app.services.knowledge.buyer_insights import (
    get_buyer_insights,
    parse_year_window,
)

client = TestClient(app)


# ---------------------------------------------------------------------------
# Year-window parsing
# ---------------------------------------------------------------------------


def test_parse_year_windows():
    assert parse_year_window("2000_2012") == (2000, 2012)
    assert parse_year_window("pre_2008") == (None, 2007)
    assert parse_year_window("post_2015") == (2015, None)
    assert parse_year_window("1980s_1990s") == (1980, 1999)
    assert parse_year_window("unbekannt") is None
    assert parse_year_window(None) is None


# ---------------------------------------------------------------------------
# Manufacturer section
# ---------------------------------------------------------------------------


def test_bavaria_2006_keel_issue_applies():
    result = get_buyer_insights(
        brand="Bavaria", model_name="37 Cruiser", year=2006,
        boat_class="cruising_sail", current_year=2026,
    )
    assert result["available"] is True
    mfr = result["manufacturer"]
    assert mfr["found"] is True
    assert mfr["display_name"] == "Bavaria Yachtbau"
    assert mfr["confidence"] == "documented"

    keel = next(p for p in mfr["known_problems"] if "keel" in p["issue"])
    # 2006 lies inside the documented 2000-2012 window
    assert keel["applies_to_year"] is True
    assert keel["severity_de"] == "schwerwiegend"
    assert keel["repair_cost_eur"] == 12000
    # Applicable problems sort first
    assert mfr["known_problems"][0]["applies_to_year"] is True
    assert mfr["survey_recommendation"]


def test_bavaria_2020_keel_window_not_applicable():
    result = get_buyer_insights(
        brand="bavaria", model_name=None, year=2020,
        boat_class="cruising_sail", current_year=2026,
    )
    keel = next(
        p for p in result["manufacturer"]["known_problems"] if "keel" in p["issue"]
    )
    assert keel["applies_to_year"] is False


def test_no_year_means_undecided_not_false():
    result = get_buyer_insights(
        brand="Bavaria", model_name="37", year=None,
        boat_class="cruising_sail", current_year=2026,
    )
    assert result["available"] is True
    for problem in result["manufacturer"]["known_problems"]:
        assert problem["applies_to_year"] is None
    assert result["age_expectations"] is None  # no year -> no age claims


def test_dehler_positive_track_record_not_a_problem_card():
    # Dehler's known_problems is "virtually_none_documented_..." — a POSITIVE
    # track record. It must never be rendered as a weakness entry.
    result = get_buyer_insights(
        brand="Dehler", model_name=None, year=2010,
        boat_class="cruising_sail", current_year=2026,
    )
    mfr = result["manufacturer"]
    assert mfr["known_problems"] == []
    assert mfr["track_record_note_de"]
    assert "Keine dokumentierten Typ-Schwachstellen" in mfr["track_record_note_de"]
    assert "unauffällige Werft-Bilanz" in result["summary_de"]


def test_alternative_problem_keys_are_read():
    # 18/23 entries store problems under variant keys — reading only
    # `known_problems` produced a false clean bill for e.g. Jeanneau
    # (known_problems_minimal) and Hallberg-Rassy (known_problems_documented).
    for brand in ("Jeanneau", "Hallberg-Rassy", "Dufour"):
        result = get_buyer_insights(
            brand=brand, model_name=None, year=2005,
            boat_class="cruising_sail", current_year=2026,
        )
        problems = result["manufacturer"]["known_problems"]
        assert problems, f"{brand}: documented problems must not be suppressed"


def test_hallberg_rassy_decade_window_parsed():
    # The 1980s_1990s decade format only occurs in the hallberg_rassy entry —
    # previously dead code because that entry's problem key was never read.
    result = get_buyer_insights(
        brand="Hallberg-Rassy", model_name=None, year=1985,
        boat_class="cruising_sail", current_year=2026,
    )
    windows = [
        p["model_years"] for p in result["manufacturer"]["known_problems"]
        if p["model_years"]
    ]
    assert any("–" in w for w in windows), windows
    assert any(p["applies_to_year"] is True
               for p in result["manufacturer"]["known_problems"])


def test_unknown_brand_honest_not_found():
    result = get_buyer_insights(
        brand="Nichtexistente Werft XY", model_name=None, year=2015,
        boat_class="cruising_sail", current_year=2026,
    )
    assert result["available"] is True
    assert result["manufacturer"]["found"] is False
    assert "keine Entwarnung" in result["manufacturer"]["note"]
    # Age expectations still work without manufacturer data
    assert result["age_expectations"] is not None


def test_brand_containment_matching():
    # "Swan" must resolve to nautor_swan; "Hallberg-Rassy" to hallberg_rassy
    for query in ("Swan", "Hallberg-Rassy", "hallberg rassy"):
        result = get_buyer_insights(
            brand=query, model_name=None, year=None,
            boat_class="cruising_sail", current_year=2026,
        )
        assert result["manufacturer"]["found"] is True, query


# ---------------------------------------------------------------------------
# Age expectations
# ---------------------------------------------------------------------------


def test_age_expectations_old_boat():
    result = get_buyer_insights(
        brand=None, model_name=None, year=1996,  # 30 years old
        boat_class="cruising_sail", current_year=2026,
    )
    age = result["age_expectations"]
    assert age["age_years"] == 30
    assert age["confidence"] == "estimated"
    assert age["items"], "a 30-year-old boat must have components to check"
    components = [item["component"] for item in age["items"]]
    # WIRE standing rigging (mast-loss risk; lifespan_range_temperate variant
    # key) must be flagged — previously dropped by the strict key filter.
    assert "standing_rigging_wire" in components
    # Saildrive diaphragm + cast-iron exhaust elbow resolve via string keys
    assert "saildrive_diaphragm" in components
    assert "exhaust_elbow_cast_iron" in components
    # Rod rigging is rare outside racing builds — excluded from generic reports
    assert "standing_rigging_rod" not in components
    # Every item carries a German component name and honest confidence
    for item in age["items"]:
        assert item["component_de"]
        assert item["confidence"] == "estimated"


def test_consumables_are_info_not_major():
    # Anodes/impeller follow the SERVICE interval, not the build year — a
    # 10-year-old boat must not open its report with "major: Anoden
    # überschritten"; they appear as info items at the END of the list.
    result = get_buyer_insights(
        brand=None, model_name=None, year=2016,
        boat_class="cruising_sail", current_year=2026,
    )
    items = result["age_expectations"]["items"]
    consumables = [i for i in items if i["component"] in ("anodes_zinc", "impeller")]
    for item in consumables:
        assert item["severity"] == "info"
        assert "Austauschhistorie" in item["status_de"]
    if consumables:
        first_consumable_idx = min(
            items.index(i) for i in consumables
        )
        majors = [i for i in items if i["severity"] == "major"]
        if majors:
            assert items.index(majors[0]) < first_consumable_idx


def test_hanseat_does_not_match_hanse():
    # Token matching: the real German shipyard "Hanseat" must NOT inherit
    # Hanse's documented QC problems (substring matching did exactly that).
    result = get_buyer_insights(
        brand="Hanseat", model_name=None, year=2000,
        boat_class="cruising_sail", current_year=2026,
    )
    assert result["manufacturer"]["found"] is False
    # Prefix inputs must not match either
    for query in ("Sun", "Con", "Prince"):
        r = get_buyer_insights(
            brand=query, model_name=None, year=None,
            boat_class="cruising_sail", current_year=2026,
        )
        assert r["manufacturer"]["found"] is False, query


def test_german_display_formats():
    result = get_buyer_insights(
        brand="Bavaria", model_name=None, year=2006,
        boat_class="cruising_sail", current_year=2026,
    )
    keel = next(
        p for p in result["manufacturer"]["known_problems"] if "keel" in p["issue"]
    )
    assert keel["model_years"] == "2000–2012"
    assert keel["affected_percentage"] == "15–20 %"


def test_age_expectations_motor_boat_excludes_rigging():
    result = get_buyer_insights(
        brand=None, model_name=None, year=1996,
        boat_class="large_motor", current_year=2026,
    )
    components = [i["component"] for i in result["age_expectations"]["items"]]
    assert not any("rigging" in c or "saildrive" in c for c in components)


def test_new_boat_few_or_no_age_items():
    result = get_buyer_insights(
        brand=None, model_name=None, year=2025,
        boat_class="cruising_sail", current_year=2026,
    )
    assert result["age_expectations"]["age_years"] == 1
    assert result["age_expectations"]["items"] == []


def test_no_identity_unavailable():
    result = get_buyer_insights(
        brand=None, model_name=None, year=None,
        boat_class="cruising_sail", current_year=2026,
    )
    assert result["available"] is False
    assert result["reason"]


# ---------------------------------------------------------------------------
# Community section (patterns injected by caller)
# ---------------------------------------------------------------------------


def test_community_patterns_rendered():
    patterns = [
        {
            "description": "Bilgenpumpe fällt nach 5 Jahren aus",
            "zone_type": "bilge",
            "severity_mode": "major",
            "report_count": 7,
            "typical_onset_years": 5.0,
            "relevance": 1.0,
            "match_reason": "exact_model",
            "is_positive": False,
        }
    ]
    result = get_buyer_insights(
        brand="Bavaria", model_name="37", year=2006,
        boat_class="cruising_sail",
        community_patterns=patterns, current_year=2026,
    )
    community = result["community"]
    assert community["available"] is True
    assert community["patterns"][0]["report_count"] == 7
    assert community["patterns"][0]["confidence"] == "documented"
    assert "Community-Muster" in result["summary_de"]


def test_community_empty_is_honest():
    result = get_buyer_insights(
        brand="Bavaria", model_name=None, year=2006,
        boat_class="cruising_sail",
        community_patterns=[], current_year=2026,
    )
    assert result["community"]["available"] is False


# ---------------------------------------------------------------------------
# Public HTTP endpoint
# ---------------------------------------------------------------------------


def test_endpoint_public_bavaria():
    res = client.get(
        "/api/v1/quick-analysis/buyer-insights",
        params={"brand": "Bavaria", "year": 2006, "boat_class": "cruising_sail"},
    )
    assert res.status_code == 200, res.text
    data = res.json()
    assert data["available"] is True
    assert data["manufacturer"]["found"] is True
    assert data["disclaimer_de"]
    assert data["summary_de"]


def test_endpoint_requires_some_identity():
    res = client.get("/api/v1/quick-analysis/buyer-insights")
    assert res.status_code == 422


def test_endpoint_not_swallowed_by_uuid_route():
    # The literal path must not be captured by /quick-analysis/{analysis_id}
    res = client.get(
        "/api/v1/quick-analysis/buyer-insights", params={"brand": "Hanse"}
    )
    assert res.status_code == 200, res.text
