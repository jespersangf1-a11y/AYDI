"""
Tests for the Markdown Knowledge Loader.

Verifies that all 16 markdown knowledge files are parsed correctly
and integrated into the AYDI knowledge retrieval system.
"""

import pytest
import sys
import os

# Ensure backend is on the path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))

from app.services.knowledge.markdown_knowledge_loader import (
    _find_markdown_files,
    parse_knowledge_file,
    load_all_markdown_knowledge,
    get_markdown_knowledge,
    get_knowledge_by_slug,
    get_knowledge_by_category,
    get_all_manufacturers,
    get_all_erfahrungsberichte,
    get_all_fehlerbilder,
    get_all_fallstudien,
    get_all_faq,
    get_all_glossary,
    get_all_expert_references,
    search_markdown_knowledge,
    format_markdown_knowledge_for_prompt,
    get_markdown_knowledge_summary,
    get_relevant_slugs_for_context,
    SLUG_TO_RETRIEVAL_CONTEXT,
)


class TestMarkdownFileDiscovery:
    """Test that all markdown knowledge files are discovered."""

    def test_find_markdown_files(self):
        files = _find_markdown_files()
        assert len(files) >= 16, f"Expected at least 16 markdown files, found {len(files)}"

    def test_file_naming_pattern(self):
        files = _find_markdown_files()
        for f in files:
            assert f.name.endswith(".md"), f"File {f.name} is not a .md file"
            parts = f.stem.split("_", 2)
            assert len(parts) >= 3, f"File {f.name} doesn't match XX_YY_name pattern"
            assert parts[0].isdigit(), f"Category '{parts[0]}' is not numeric"
            assert parts[1].isdigit(), f"Subcategory '{parts[1]}' is not numeric"


class TestSingleFileParsing:
    """Test parsing of individual knowledge files."""

    def test_parse_kuehlwasserschlaeuche(self):
        files = _find_markdown_files()
        target = [f for f in files if "kuehlwasserschlaeuche" in f.name]
        assert len(target) == 1, "06_01_kuehlwasserschlaeuche.md not found"

        data = parse_knowledge_file(target[0])
        assert data["category"] == "06"
        assert data["subcategory"] == "01"
        assert data["slug"] == "kuehlwasserschlaeuche"
        assert data["line_count"] >= 3800
        assert len(data["tables"]) > 0
        assert len(data["faq"]) >= 5
        assert len(data["glossary"]) >= 20

    def test_parse_galvanische_spannungsreihe(self):
        files = _find_markdown_files()
        # Filter precisely: 05_10 (galvanische Spannungsreihe an Thru-Hulls),
        # not 22_10 (galvanische Korrosion Elektrik). Both legitimately exist.
        target = [f for f in files if f.name.startswith("05_10_")]
        assert len(target) == 1, f"expected exactly one 05_10_*.md, found {[f.name for f in target]}"

        data = parse_knowledge_file(target[0])
        assert data["category"] == "05"
        assert data["subcategory"] == "10"
        # Content-based assertions instead of brittle line-count thresholds:
        assert len(data["sections"]) >= 5
        assert len(data["fehlerbilder"]) >= 5

    def test_parse_has_required_fields(self):
        files = _find_markdown_files()
        for f in files:
            data = parse_knowledge_file(f)
            assert "file" in data
            assert "category" in data
            assert "subcategory" in data
            assert "slug" in data
            assert "title" in data
            assert "sections" in data
            assert "tables" in data
            assert "manufacturers" in data
            assert "erfahrungsberichte" in data
            assert "faq" in data
            assert "glossary" in data
            assert "fehlerbilder" in data
            assert "fallstudien" in data
            assert "line_count" in data


class TestFullLoad:
    """Test loading all markdown knowledge files."""

    def test_load_all(self):
        knowledge = load_all_markdown_knowledge()
        assert len(knowledge) >= 16

    def test_get_by_slug(self):
        data = get_knowledge_by_slug("kuehlwasserschlaeuche")
        assert data is not None
        assert data["title"] != ""

    def test_get_by_category(self):
        cat05 = get_knowledge_by_category("05")
        assert len(cat05) >= 6, f"Expected at least 6 files in category 05, got {len(cat05)}"

    def test_unknown_slug_returns_none(self):
        assert get_knowledge_by_slug("nonexistent_topic") is None


class TestAggregatedDatabases:
    """Test aggregated cross-file databases."""

    def test_all_manufacturers(self):
        mfrs = get_all_manufacturers()
        assert len(mfrs) >= 10, f"Expected at least 10 manufacturers, got {len(mfrs)}"

    def test_all_erfahrungsberichte(self):
        reports = get_all_erfahrungsberichte()
        assert len(reports) >= 20, f"Expected at least 20 reports, got {len(reports)}"

    def test_all_fehlerbilder(self):
        fb = get_all_fehlerbilder()
        assert len(fb) >= 10, f"Expected at least 10 fehlerbilder, got {len(fb)}"

    def test_all_fallstudien(self):
        studies = get_all_fallstudien()
        assert len(studies) >= 10, f"Expected at least 10 fallstudien, got {len(studies)}"

    def test_all_faq(self):
        faqs = get_all_faq()
        assert len(faqs) >= 30, f"Expected at least 30 FAQ entries, got {len(faqs)}"

    def test_all_glossary(self):
        glossary = get_all_glossary()
        assert len(glossary) >= 50, f"Expected at least 50 glossary entries, got {len(glossary)}"

    def test_all_expert_references(self):
        refs = get_all_expert_references()
        assert len(refs) >= 10, f"Expected at least 10 expert refs, got {len(refs)}"


class TestSearch:
    """Test search functionality."""

    def test_search_finds_results(self):
        results = search_markdown_knowledge("Korrosion")
        assert len(results) > 0, "Search for 'Korrosion' should find results"

    def test_search_finds_specific_topic(self):
        results = search_markdown_knowledge("EPDM")
        assert len(results) > 0, "Search for 'EPDM' should find results"

    def test_search_respects_max_results(self):
        results = search_markdown_knowledge("Schlauch", max_results=5)
        assert len(results) <= 5

    def test_search_no_results_for_nonsense(self):
        results = search_markdown_knowledge("xyznonexistent12345")
        assert len(results) == 0


class TestPromptFormatting:
    """Test prompt formatting for Claude Vision context."""

    def test_format_single_slug(self):
        output = format_markdown_knowledge_for_prompt(
            ["kuehlwasserschlaeuche"], max_lines=50
        )
        assert len(output) > 0
        assert "Kühlwasserschläuche" in output or "kuehlwasserschlaeuche" in output.lower()

    def test_format_respects_max_lines(self):
        output = format_markdown_knowledge_for_prompt(
            ["kuehlwasserschlaeuche", "galvanische_spannungsreihe_thru_hulls"],
            max_lines=20,
        )
        lines = output.split("\n")
        assert len(lines) <= 21  # max_lines + possible "gekürzt" line


class TestContextMapping:
    """Test the slug-to-context mapping."""

    def test_materials_context(self):
        slugs = get_relevant_slugs_for_context("materials")
        assert len(slugs) >= 5
        assert "galvanische_spannungsreihe_thru_hulls" in slugs

    def test_structural_context(self):
        slugs = get_relevant_slugs_for_context("structural")
        assert len(slugs) >= 3

    def test_service_patterns_context(self):
        slugs = get_relevant_slugs_for_context("service_patterns")
        assert "kuehlwasserschlaeuche" in slugs


class TestSummary:
    """Test summary statistics."""

    def test_summary_structure(self):
        summary = get_markdown_knowledge_summary()
        assert summary["total_files"] >= 16
        assert summary["total_lines"] >= 50000  # 16 files × 3800+ lines
        assert summary["total_tables"] >= 100
        assert "files" in summary
        assert len(summary["files"]) >= 16

    def test_summary_per_file(self):
        summary = get_markdown_knowledge_summary()
        for slug, info in summary["files"].items():
            assert "file" in info
            assert "title" in info
            assert "line_count" in info
            # Content-based minimum: a knowledge file must have some real
            # body (not a stub). Line-count thresholds are brittle because
            # research files legitimately vary from ~300 (concise topic
            # like 29_07_mann_ueber_bord) to ~4000 (deep system like
            # 18_02_yanmar_motoren).
            assert info["line_count"] >= 100, (
                f"File {info['file']} is a stub ({info['line_count']} lines)"
            )


if __name__ == "__main__":
    pytest.main([__file__, "-v"])
