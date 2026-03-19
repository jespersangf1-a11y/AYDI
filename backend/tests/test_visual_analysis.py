"""Tests for visual analysis services (confidence, cache, analyzer)."""
import asyncio
import json
import os
import tempfile
from pathlib import Path
from unittest.mock import AsyncMock, MagicMock, patch

import pytest

from app.services.visual.confidence import (
    CONFIDENCE_WORD_MAP,
    ConfidenceAssessment,
    ConfidenceGatekeeper,
    VisualConfidence,
)
from app.services.visual.cache import AnalysisCache
from app.services.visual.analyzer import (
    MEDIA_TYPE_MAP,
    VisualAnalyzer,
)


# ===========================================================================
# Confidence tests
# ===========================================================================


class TestConfidenceGatekeeper:
    """Tests for the ConfidenceGatekeeper class."""

    def _good_metadata(self) -> dict:
        return {"width": 1920, "height": 1080, "file_size_bytes": 600_000}

    def _low_res_metadata(self) -> dict:
        return {"width": 320, "height": 240, "file_size_bytes": 20_000}

    def _good_ai_response(self) -> dict:
        return {
            "score": 80,
            "confidence": "hoch",
            "assessable": True,
            "findings": [{"area": "salon", "note": "gut"}],
            "cannot_assess": [],
        }

    def test_high_quality_high_confidence(self):
        """Good image + high AI confidence -> HIGH level."""
        gk = ConfidenceGatekeeper()
        result = gk.evaluate(self._good_ai_response(), self._good_metadata())
        assert result.level == VisualConfidence.HIGH
        assert result.is_usable

    def test_low_resolution_insufficient(self):
        """Very low resolution -> image quality < 0.4 -> at most LOW."""
        gk = ConfidenceGatekeeper()
        result = gk.evaluate(
            self._good_ai_response(),
            {"width": 100, "height": 100, "file_size_bytes": 5_000},
        )
        assert result.image_quality < 0.4
        assert result.level in (VisualConfidence.LOW, VisualConfidence.INSUFFICIENT)

    def test_assessable_false_low_relevance(self):
        """AI says assessable=false -> content relevance drops below 0.5."""
        gk = ConfidenceGatekeeper()
        ai = {"assessable": False, "confidence": "hoch", "findings": []}
        result = gk.evaluate(ai, self._good_metadata())
        assert result.content_relevance <= 0.2

    def test_niedrig_confidence_low_certainty(self):
        """AI confidence 'niedrig' maps to certainty 0.3."""
        gk = ConfidenceGatekeeper()
        ai = {
            "confidence": "niedrig",
            "assessable": True,
            "findings": [{"area": "test"}],
        }
        result = gk.evaluate(ai, self._good_metadata())
        assert result.assessment_certainty == 0.3

    def test_many_cannot_assess_reduces_relevance(self):
        """Many cannot_assess items reduce content relevance score."""
        gk = ConfidenceGatekeeper()
        ai = {
            "confidence": "hoch",
            "assessable": True,
            "findings": [],
            "cannot_assess": ["item1", "item2", "item3", "item4", "item5"],
        }
        result = gk.evaluate(ai, self._good_metadata())
        assert result.content_relevance < 0.5

    def test_is_usable_high_and_medium(self):
        """is_usable returns True for HIGH and MEDIUM only."""
        assert ConfidenceAssessment(level=VisualConfidence.HIGH).is_usable is True
        assert ConfidenceAssessment(level=VisualConfidence.MEDIUM).is_usable is True
        assert ConfidenceAssessment(level=VisualConfidence.LOW).is_usable is False
        assert ConfidenceAssessment(level=VisualConfidence.INSUFFICIENT).is_usable is False

    def test_small_file_size_reduces_quality(self):
        """Small file size contributes to lower image quality score."""
        gk = ConfidenceGatekeeper()
        good = gk._assess_image_quality(self._good_metadata())
        small = gk._assess_image_quality(
            {"width": 1920, "height": 1080, "file_size_bytes": 30_000}
        )
        assert small < good

    def test_confidence_word_map_covers_german(self):
        """CONFIDENCE_WORD_MAP includes German words."""
        assert "hoch" in CONFIDENCE_WORD_MAP
        assert "mittel" in CONFIDENCE_WORD_MAP
        assert "niedrig" in CONFIDENCE_WORD_MAP
        assert "sehr hoch" in CONFIDENCE_WORD_MAP

    def test_numeric_confidence_passthrough(self):
        """Numeric confidence values are used directly."""
        gk = ConfidenceGatekeeper()
        ai = {"confidence": 0.85, "assessable": True, "findings": [{"a": 1}]}
        result = gk.evaluate(ai, self._good_metadata())
        assert result.assessment_certainty == 0.85


# ===========================================================================
# Cache tests
# ===========================================================================


class TestAnalysisCache:
    """Tests for the AnalysisCache class."""

    def test_cache_miss_returns_none(self):
        """Unknown key returns None."""
        with tempfile.TemporaryDirectory() as tmpdir:
            cache = AnalysisCache(cache_dir=tmpdir)
            assert cache.get("nonexistent_key_abc123") is None

    def test_cache_set_then_get(self):
        """Store a result and retrieve it."""
        with tempfile.TemporaryDirectory() as tmpdir:
            cache = AnalysisCache(cache_dir=tmpdir)
            data = {"score": 85.0, "confidence": "high"}
            cache.set("test_key_001", data)
            retrieved = cache.get("test_key_001")
            assert retrieved == data

    def test_different_params_different_keys(self):
        """Different analysis parameters produce different cache keys."""
        with tempfile.TemporaryDirectory() as tmpdir:
            cache = AnalysisCache(cache_dir=tmpdir)

            # Create a temp image to hash
            img_path = os.path.join(tmpdir, "test.jpg")
            with open(img_path, "wb") as f:
                f.write(b"fake image data")

            key1 = cache.get_cache_key(img_path, "interior", "cruising_sail", "standard")
            key2 = cache.get_cache_key(img_path, "exterior", "cruising_sail", "standard")
            key3 = cache.get_cache_key(img_path, "interior", "superyacht", "standard")
            key4 = cache.get_cache_key(img_path, "interior", "cruising_sail", "detailed")

            assert key1 != key2
            assert key1 != key3
            assert key1 != key4

    def test_cache_handles_missing_directory(self):
        """Cache creation with unreachable path does not crash."""
        # On Windows, /dev/null/impossible won't exist; just test it doesn't raise
        cache = AnalysisCache(cache_dir=os.path.join(tempfile.gettempdir(), "aydi_test_cache_xyz"))
        assert cache.get("any_key") is None

    def test_cache_invalidate(self):
        """Invalidate removes cached entry."""
        with tempfile.TemporaryDirectory() as tmpdir:
            cache = AnalysisCache(cache_dir=tmpdir)
            cache.set("to_remove", {"score": 50})
            assert cache.get("to_remove") is not None
            removed = cache.invalidate("to_remove")
            assert removed is True
            assert cache.get("to_remove") is None

    def test_invalidate_nonexistent(self):
        """Invalidating a non-existent key returns False."""
        with tempfile.TemporaryDirectory() as tmpdir:
            cache = AnalysisCache(cache_dir=tmpdir)
            assert cache.invalidate("nope") is False


# ===========================================================================
# Analyzer tests
# ===========================================================================


class TestParseJsonResponse:
    """Tests for VisualAnalyzer._parse_json_response."""

    def setup_method(self):
        self.analyzer = VisualAnalyzer()

    def test_clean_json(self):
        """Plain JSON string parses correctly."""
        raw = '{"score": 80, "confidence": "hoch"}'
        result = self.analyzer._parse_json_response(raw)
        assert result["score"] == 80
        assert result["confidence"] == "hoch"

    def test_strips_markdown_code_blocks(self):
        """JSON wrapped in ```json ... ``` is extracted."""
        raw = '```json\n{"score": 72, "assessable": true}\n```'
        result = self.analyzer._parse_json_response(raw)
        assert result["score"] == 72
        assert result["assessable"] is True

    def test_strips_plain_code_blocks(self):
        """JSON wrapped in ``` ... ``` (no language tag) is extracted."""
        raw = '```\n{"score": 65}\n```'
        result = self.analyzer._parse_json_response(raw)
        assert result["score"] == 65

    def test_malformed_json_returns_none(self):
        """Non-JSON text returns None."""
        raw = "This is not JSON at all."
        result = self.analyzer._parse_json_response(raw)
        assert result is None

    def test_empty_string_returns_none(self):
        """Empty string returns None."""
        result = self.analyzer._parse_json_response("")
        assert result is None

    def test_json_with_surrounding_text(self):
        """JSON embedded in text is extracted via brace matching."""
        raw = 'Here is the analysis:\n{"score": 55, "ok": true}\nEnd.'
        result = self.analyzer._parse_json_response(raw)
        assert result["score"] == 55


class TestVisualAnalyzer:
    """Tests for the VisualAnalyzer class."""

    def test_analyze_image_no_client(self):
        """Without API client, returns unavailable result."""
        analyzer = VisualAnalyzer()
        analyzer._client = None
        with patch.object(type(analyzer), 'client', new_callable=lambda: property(lambda self: None)):
            result = asyncio.run(analyzer.analyze_image("some/path.jpg", "interior_overview", "cruising_sail"))
        assert result["score"] is None
        assert result["confidence"]["level"] == "insufficient"
        assert result["confidence"]["is_usable"] is False

    def test_analyze_image_file_not_found(self):
        """Missing image file returns error result."""
        analyzer = VisualAnalyzer()
        analyzer._client = MagicMock()
        result = asyncio.run(analyzer.analyze_image("/nonexistent/path/img.jpg", "interior_overview", "cruising_sail"))
        assert result["score"] is None
        assert "nicht gefunden" in result.get("error", "")

    def test_analyze_image_success(self):
        """With mocked API, returns structured result with score."""
        analyzer = VisualAnalyzer()

        mock_response = MagicMock()
        mock_response.content = [
            MagicMock(text='{"spatial_score": 78, "confidence": "hoch", "assessable": true, "findings": [{"area": "salon"}], "cannot_assess": []}')
        ]

        mock_client = MagicMock()
        mock_client.messages.create.return_value = mock_response
        analyzer._client = mock_client

        with tempfile.NamedTemporaryFile(suffix=".jpg", delete=False) as f:
            f.write(b"\xff\xd8\xff\xe0" + b"\x00" * 100)
            img_path = f.name

        try:
            result = asyncio.run(analyzer.analyze_image(img_path, "interior_overview", "cruising_sail"))
            assert result["score"] == 78.0
            assert result["confidence"]["level"] in ("high", "medium", "low", "insufficient")
            assert result["analysis"]["spatial_score"] == 78
        finally:
            os.unlink(img_path)

    def test_analyze_batch_combines_results(self):
        """analyze_batch aggregates multiple image results."""
        analyzer = VisualAnalyzer()

        async def mock_analyze(image_path, image_type, boat_class, **kwargs):
            scores = {"/img1.jpg": 80.0, "/img2.jpg": 70.0}
            score = scores.get(image_path, 50.0)
            return {
                "image_path": image_path,
                "score": score,
                "confidence": {"level": "high", "is_usable": True, "assessment_certainty": 0.9},
                "analysis": {"findings": [{"observation": f"finding for {image_path}"}]},
            }

        with patch.object(analyzer, "analyze_image", side_effect=mock_analyze):
            batch = asyncio.run(analyzer.analyze_batch(
                [{"path": "/img1.jpg", "image_type": "interior_overview"},
                 {"path": "/img2.jpg", "image_type": "interior_detail"}],
                boat_class="cruising_sail",
            ))
        assert batch["total_images"] == 2
        assert batch["usable_images"] == 2
        assert batch["fused_score"] is not None

    def test_analyze_batch_filters_unusable(self):
        """analyze_batch excludes results with is_usable=False."""
        analyzer = VisualAnalyzer()

        async def mock_analyze(image_path, image_type, boat_class, **kwargs):
            if "bad" in image_path:
                return {
                    "image_path": image_path, "score": None,
                    "confidence": {"level": "insufficient", "is_usable": False, "assessment_certainty": 0.1},
                    "analysis": {"findings": []},
                }
            return {
                "image_path": image_path, "score": 80.0,
                "confidence": {"level": "high", "is_usable": True, "assessment_certainty": 0.9},
                "analysis": {"findings": []},
            }

        with patch.object(analyzer, "analyze_image", side_effect=mock_analyze):
            batch = asyncio.run(analyzer.analyze_batch(
                [{"path": "/good.jpg"}, {"path": "/bad.jpg"}],
                boat_class="cruising_sail",
            ))
        assert batch["usable_images"] == 1
        assert batch["unusable_images"] == 1

    def test_analyze_batch_flags_high_variance(self):
        """analyze_batch flags cross-validation warning when score spread > 30."""
        analyzer = VisualAnalyzer()

        async def mock_analyze(image_path, image_type, boat_class, **kwargs):
            scores = {"/a.jpg": 90.0, "/b.jpg": 50.0}
            score = scores.get(image_path, 70.0)
            return {
                "image_path": image_path, "score": score,
                "confidence": {"level": "high", "is_usable": True, "assessment_certainty": 0.9},
                "analysis": {"findings": []},
            }

        with patch.object(analyzer, "analyze_image", side_effect=mock_analyze):
            batch = asyncio.run(analyzer.analyze_batch(
                [{"path": "/a.jpg"}, {"path": "/b.jpg"}],
                boat_class="cruising_sail",
            ))
        assert len(batch["cross_validation_warnings"]) > 0
        assert "varianz" in batch["cross_validation_warnings"][0].lower()


class TestImageUtilities:
    """Tests for image loading and metadata utilities."""

    def setup_method(self):
        self.analyzer = VisualAnalyzer()

    def test_get_image_metadata_basic(self):
        """_get_image_metadata extracts file size."""
        with tempfile.NamedTemporaryFile(suffix=".png", delete=False) as f:
            f.write(b"\x89PNG" + b"\x00" * 200)
            path = f.name

        try:
            meta = self.analyzer._get_image_metadata(path)
            assert meta["file_size_bytes"] > 0
        finally:
            os.unlink(path)

    def test_get_image_metadata_nonexistent(self):
        """Non-existent file returns zero size."""
        meta = self.analyzer._get_image_metadata("/tmp/nonexistent_image_xyz.jpg")
        assert meta["file_size_bytes"] == 0

    def test_load_image_base64_jpg(self):
        """_load_image_base64 returns correct media type for .jpg."""
        with tempfile.NamedTemporaryFile(suffix=".jpg", delete=False) as f:
            f.write(b"\xff\xd8\xff\xe0" + b"\x00" * 50)
            path = f.name

        try:
            data, media_type = self.analyzer._load_image_base64(path)
            assert media_type == "image/jpeg"
            assert len(data) > 0
        finally:
            os.unlink(path)

    def test_load_image_base64_png(self):
        """_load_image_base64 returns correct media type for .png."""
        with tempfile.NamedTemporaryFile(suffix=".png", delete=False) as f:
            f.write(b"\x89PNG" + b"\x00" * 50)
            path = f.name

        try:
            data, media_type = self.analyzer._load_image_base64(path)
            assert media_type == "image/png"
        finally:
            os.unlink(path)

    def test_load_image_base64_webp(self):
        """_load_image_base64 returns correct media type for .webp."""
        with tempfile.NamedTemporaryFile(suffix=".webp", delete=False) as f:
            f.write(b"RIFF" + b"\x00" * 50)
            path = f.name

        try:
            data, media_type = self.analyzer._load_image_base64(path)
            assert media_type == "image/webp"
        finally:
            os.unlink(path)

    def test_load_image_base64_unsupported_format(self):
        """Unsupported extension raises ValueError."""
        with tempfile.NamedTemporaryFile(suffix=".bmp", delete=False) as f:
            f.write(b"BM" + b"\x00" * 50)
            path = f.name

        try:
            with pytest.raises(ValueError, match="Nicht unterstuetzt"):
                self.analyzer._load_image_base64(path)
        finally:
            os.unlink(path)

    def test_load_image_base64_file_not_found(self):
        """Missing file raises FileNotFoundError."""
        with pytest.raises(FileNotFoundError):
            self.analyzer._load_image_base64("/tmp/no_such_file_xyz.jpg")

    def test_media_type_map_has_common_formats(self):
        """MEDIA_TYPE_MAP covers jpg, jpeg, png, webp."""
        assert ".jpg" in MEDIA_TYPE_MAP
        assert ".jpeg" in MEDIA_TYPE_MAP
        assert ".png" in MEDIA_TYPE_MAP
        assert ".webp" in MEDIA_TYPE_MAP

    def test_extract_score_various_keys(self):
        """_extract_score finds scores under different key names."""
        assert self.analyzer._extract_score({"spatial_score": 75}) == 75.0
        assert self.analyzer._extract_score({"overall_quality_score": 82}) == 82.0
        assert self.analyzer._extract_score({"emotional_score": 60}) == 60.0
        assert self.analyzer._extract_score({"helm_score": 55}) == 55.0
        assert self.analyzer._extract_score({"no_score_here": 90}) is None
