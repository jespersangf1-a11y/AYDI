"""
HTTP tests for the public knowledge API (product pillar 1: lexicon).

These are the first TestClient-based route tests in the project. They verify:
- knowledge endpoints are publicly readable (no auth required),
- the corpus browse structure exposes all categories/documents,
- a full document can be read as a structured article,
- the manufacturer endpoint actually finds known manufacturers
  (regression for the found/profile wrapper-key bug),
- search returns corpus-document hits that the UI can open as articles.
"""

import pytest
from fastapi.testclient import TestClient

from app.main import app

client = TestClient(app)

BASE = "/api/v1/knowledge"


# ---------------------------------------------------------------------------
# Public access (no Authorization header anywhere in this file)
# ---------------------------------------------------------------------------


def test_legacy_categories_public():
    res = client.get(f"{BASE}/categories")
    assert res.status_code == 200, res.text
    data = res.json()
    assert data["total_categories"] >= 20
    assert len(data["categories"]) == data["total_categories"]


def test_search_public():
    res = client.get(f"{BASE}/search", params={"q": "osmose"})
    assert res.status_code == 200, res.text
    data = res.json()
    assert data["query"] == "osmose"
    assert isinstance(data["matches"], list)


# ---------------------------------------------------------------------------
# Corpus browsing
# ---------------------------------------------------------------------------


@pytest.fixture(scope="module")
def corpus():
    res = client.get(f"{BASE}/corpus/categories")
    assert res.status_code == 200, res.text
    return res.json()


def test_corpus_categories_structure(corpus):
    # 31 corpus categories, ~251 canonical documents
    assert corpus["total_categories"] >= 30
    assert corpus["total_documents"] >= 245
    assert len(corpus["categories"]) == corpus["total_categories"]

    doc_sum = sum(c["document_count"] for c in corpus["categories"])
    assert doc_sum == corpus["total_documents"]

    # Category 01 must resolve to its real German name from KNOWLEDGE_INDEX
    cat01 = next(c for c in corpus["categories"] if c["id"] == "01")
    assert cat01["name"] != "Kategorie 01"
    assert cat01["document_count"] >= 10

    # Every document summary carries a usable key and title
    for cat in corpus["categories"]:
        for doc in cat["documents"]:
            assert doc["key"]
            assert doc["title"]
            assert doc["line_count"] > 0


def test_corpus_document_read(corpus):
    # Read the first document of category 01 as a full article
    cat01 = next(c for c in corpus["categories"] if c["id"] == "01")
    key = cat01["documents"][0]["key"]

    res = client.get(f"{BASE}/corpus/documents/{key}")
    assert res.status_code == 200, res.text
    doc = res.json()

    assert doc["key"] == key
    assert doc["title"]
    assert doc["category"] == "01"
    assert doc["category_name"] != "Kategorie 01"
    assert doc["line_count"] > 100

    # Section hierarchy present with real content somewhere
    def has_text(section) -> bool:
        if section.get("text"):
            return True
        return any(has_text(s) for s in section.get("subsections", []))

    assert has_text(doc["sections"])


def test_corpus_document_not_found():
    res = client.get(f"{BASE}/corpus/documents/does_not_exist_xyz")
    assert res.status_code == 404


def test_corpus_keys_resolve(corpus):
    # Composite collision keys (category_subcategory_slug) must resolve too
    composite = [
        doc["key"]
        for cat in corpus["categories"]
        for doc in cat["documents"]
        if doc["key"].count("_") >= 2 and doc["key"][:2].isdigit()
    ]
    for key in composite[:2]:
        res = client.get(f"{BASE}/corpus/documents/{key}")
        assert res.status_code == 200, f"composite key {key} did not resolve"


# ---------------------------------------------------------------------------
# Manufacturer endpoint (regression: wrapper-key bug reported every real
# match as "not found")
# ---------------------------------------------------------------------------


def test_manufacturer_known_brand_found():
    res = client.get(f"{BASE}/manufacturer/bavaria")
    assert res.status_code == 200, res.text
    data = res.json()
    assert data["manufacturer"] is not None, (
        "Known manufacturer 'bavaria' must resolve to a profile "
        f"(got message: {data.get('message')})"
    )
    profile = data["manufacturer"]
    assert profile["manufacturer_name"]
    # The aging/lifecycle DB carries known problems for Bavaria
    assert profile["known_weaknesses"], "expected known_weaknesses from knowledge DB"


def test_manufacturer_unknown_brand():
    res = client.get(f"{BASE}/manufacturer/definitely-not-a-shipyard-xyz")
    assert res.status_code == 200
    assert res.json()["manufacturer"] is None


# ---------------------------------------------------------------------------
# Search integration with the corpus
# ---------------------------------------------------------------------------


def test_manufacturer_string_problems_not_char_split():
    # Dehler's known_problems is a single STRING in the knowledge DB — the
    # endpoint must not iterate it char-wise into one-letter "weaknesses".
    res = client.get(f"{BASE}/manufacturer/dehler")
    assert res.status_code == 200, res.text
    profile = res.json()["manufacturer"]
    if profile is not None and profile["known_weaknesses"]:
        assert all(len(w) > 1 for w in profile["known_weaknesses"]), (
            f"char-split weaknesses: {profile['known_weaknesses'][:6]}..."
        )


def test_frontmatter_titles_resolved(corpus):
    # ~100 corpus files start with YAML frontmatter instead of an H1 in line 0
    # (e.g. all of category 09) — their titles must not fall back to raw keys.
    cat09 = next((c for c in corpus["categories"] if c["id"] == "09"), None)
    assert cat09 is not None
    for doc in cat09["documents"]:
        assert doc["title"] != doc["key"], f"raw slug shown as title: {doc['key']}"
        assert "_" not in doc["title"] or " " in doc["title"], (
            f"slug-like title for {doc['key']}: {doc['title']}"
        )


def test_table_parser_preserves_empty_cells():
    # Empty middle cells must stay positional — filtering them shifted values
    # under the WRONG column headers (prices/torques in ~100 files).
    from app.services.knowledge.markdown_knowledge_loader import (
        _parse_markdown_table,
    )

    rows = _parse_markdown_table(
        [
            "| Produkt | Härte | Preis |",
            "|---------|-------|-------|",
            "| Sikaflex 291 |  | 15 €/Kartusche |",
        ]
    )
    assert rows[0]["Härte"] == ""
    assert rows[0]["Preis"] == "15 €/Kartusche"


def test_corpus_document_tables_have_explicit_columns(corpus):
    # Article tables are delivered as {columns, rows} so the UI cannot
    # reorder integer-like headers (JS object-key semantics).
    cat01 = next(c for c in corpus["categories"] if c["id"] == "01")
    key = cat01["documents"][0]["key"]
    doc = client.get(f"{BASE}/corpus/documents/{key}").json()

    def find_table(section):
        for t in section.get("tables", []):
            return t
        for sub in section.get("subsections", []):
            found = find_table(sub)
            if found:
                return found
        return None

    table = find_table(doc["sections"])
    assert table is not None, "expected at least one table in a 01-doc"
    assert isinstance(table["columns"], list) and table["columns"]
    assert all(len(row) == len(table["columns"]) for row in table["rows"])


def test_search_finds_corpus_documents():
    res = client.get(f"{BASE}/search", params={"q": "dichtungen"})
    assert res.status_code == 200, res.text
    matches = res.json()["matches"]
    doc_hits = [m for m in matches if m["database"] == "markdown_document"]
    assert doc_hits, "title search must surface corpus documents"

    # The hit's category field is the document key — it must open as article
    key = doc_hits[0]["category"]
    res2 = client.get(f"{BASE}/corpus/documents/{key}")
    assert res2.status_code == 200, f"search hit key '{key}' must resolve to a document"
