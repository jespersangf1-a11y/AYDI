"""Regressionstests fuer die Robustheit des VisualAnalyzer.

Deckt die Audit-Befunde ab:
- B-9:  blockierender SDK-Aufruf unter asyncio.wait_for (Event-Loop blockiert,
        deklariertes Timeout wirkungslos)
- B-10: fehlender Schema-Guard nach dem JSON-Parsing (Liste/Skalar -> AttributeError)
- B-11: Score wird nicht auf 0-100 validiert, ``True`` wird zu 1.0
- B-14: ``overall_findings`` (Build-Quality-Prompt) werden bei der Aggregation
        verworfen
- B-3/B-15: Bilder werden ungeskaliert base64-kodiert an die Vision-API geschickt
"""
import asyncio
import base64
import io
import os
import tempfile
import time
from unittest.mock import MagicMock, patch

import pytest

from app.services.visual import analyzer as analyzer_module
from app.services.visual.analyzer import VisualAnalyzer

VALID_JSON = (
    '{"spatial_score": 78, "confidence": "hoch", "assessable": true, '
    '"findings": [{"observation": "Salon hell"}], "cannot_assess": []}'
)


def _stub_image(suffix=".jpg"):
    """Erzeuge eine eindeutige (nicht cachebare) Pseudo-Bilddatei."""
    with tempfile.NamedTemporaryFile(suffix=suffix, delete=False) as f:
        f.write(b"\xff\xd8\xff\xe0" + os.urandom(256))
        return f.name


def _mock_client(text=VALID_JSON, side_effect=None):
    response = MagicMock()
    response.content = [MagicMock(text=text)]
    client = MagicMock()
    if side_effect is not None:
        client.messages.create.side_effect = side_effect
    else:
        client.messages.create.return_value = response
    return client, response


# ===========================================================================
# B-10 — Schema-Guard nach dem JSON-Parsing
# ===========================================================================


class TestJsonSchemaGuard:
    def setup_method(self):
        self.analyzer = VisualAnalyzer()

    @pytest.mark.parametrize("raw", [
        '[{"spatial_score": 80}]',      # Liste statt Objekt
        '[1, 2, 3]',
        '42',                            # Skalar
        '78.5',
        '"nur ein String"',
        'true',
        'null',
    ])
    def test_non_object_json_is_rejected(self, raw):
        """Nur JSON-Objekte werden akzeptiert — sonst None."""
        assert self.analyzer._parse_json_response(raw) is None

    @pytest.mark.parametrize("raw", [
        '```json\n[{"spatial_score": 80}]\n```',
        '```\n[1, 2, 3]\n```',
        '```json\n"kein Objekt"\n```',
    ])
    def test_non_object_json_in_markdown_fence_is_rejected(self, raw):
        """Auch in Markdown-Fences gilt der Schema-Guard."""
        assert self.analyzer._parse_json_response(raw) is None

    def test_object_still_parses(self):
        """Gueltige Objekte gehen unveraendert durch (auch in Fences)."""
        assert self.analyzer._parse_json_response('{"a": 1}') == {"a": 1}
        assert self.analyzer._parse_json_response('```json\n{"a": 1}\n```') == {"a": 1}
        assert self.analyzer._parse_json_response('Text vorab {"a": 1} Text danach') == {"a": 1}

    def test_analyze_image_with_list_response_returns_error_not_crash(self):
        """Liefert das Modell eine Liste, kommt ein Fehlerergebnis — kein AttributeError."""
        analyzer = VisualAnalyzer()
        analyzer._client, _ = _mock_client(text='[{"spatial_score": 80}]')
        path = _stub_image()
        try:
            result = asyncio.run(
                analyzer.analyze_image(path, "interior_overview", "cruising_sail")
            )
        finally:
            os.unlink(path)

        assert result["score"] is None
        assert result["analysis"] is None
        assert result["confidence"]["level"] == "visual_insufficient"
        assert result["confidence"]["is_usable"] is False
        assert "nicht verarbeitet" in result["error"]


# ===========================================================================
# B-11 — Score-Validierung
# ===========================================================================


class TestScoreValidation:
    def setup_method(self):
        self.analyzer = VisualAnalyzer()

    @pytest.mark.parametrize("value", [True, False])
    def test_boolean_score_is_rejected(self, value):
        """``True`` darf nicht stillschweigend zu 1.0 werden."""
        assert self.analyzer._extract_score({"spatial_score": value}) is None

    @pytest.mark.parametrize("value", [5000, 100.1, -0.5, -20, 1e9])
    def test_out_of_range_score_is_rejected(self, value):
        """Werte ausserhalb 0-100 sind 'nicht beurteilbar', kein erfundener Score."""
        assert self.analyzer._extract_score({"overall_quality_score": value}) is None

    @pytest.mark.parametrize("value", [float("nan"), float("inf"), float("-inf")])
    def test_non_finite_score_is_rejected(self, value):
        assert self.analyzer._extract_score({"material_score": value}) is None

    @pytest.mark.parametrize("value,expected", [(0, 0.0), (100, 100.0), (78, 78.0), ("78.5", 78.5)])
    def test_valid_scores_pass(self, value, expected):
        assert self.analyzer._extract_score({"spatial_score": value}) == expected

    def test_invalid_first_key_falls_through_to_valid_key(self):
        """Ein unbrauchbarer Score blockiert einen gueltigen spaeteren nicht."""
        parsed = {"spatial_score": True, "overall_quality_score": 64}
        assert self.analyzer._extract_score(parsed) == 64.0

    def test_non_dict_input_returns_none(self):
        assert self.analyzer._extract_score([{"spatial_score": 80}]) is None


# ===========================================================================
# B-9 — Blockierender SDK-Aufruf / Timeout
# ===========================================================================


class TestApiCallDoesNotBlockEventLoop:
    def test_event_loop_stays_responsive_during_sdk_call(self):
        """Der blockierende SDK-Aufruf darf den Event-Loop nicht anhalten."""
        analyzer = VisualAnalyzer()
        response = MagicMock()
        response.content = [MagicMock(text=VALID_JSON)]

        def blocking_create(*args, **kwargs):
            time.sleep(0.8)   # blockierender SDK-Aufruf
            return response

        analyzer._client, _ = _mock_client(side_effect=blocking_create)
        path = _stub_image()

        async def main():
            gaps = []

            async def heartbeat():
                last = time.monotonic()
                try:
                    while True:
                        await asyncio.sleep(0.02)
                        now = time.monotonic()
                        gaps.append(now - last)
                        last = now
                except asyncio.CancelledError:
                    pass

            hb = asyncio.create_task(heartbeat())
            await asyncio.sleep(0.2)      # Heartbeat sicher anlaufen lassen
            gaps.clear()
            result = await analyzer.analyze_image(
                path, "interior_overview", "cruising_sail"
            )
            await asyncio.sleep(0.05)     # letzten Tick nachholen lassen
            hb.cancel()
            await asyncio.gather(hb, return_exceptions=True)
            return max(gaps), result

        try:
            worst_gap, result = asyncio.run(main())
        finally:
            os.unlink(path)

        # Ohne to_thread wuerde der Loop ~0.8s stillstehen.
        assert worst_gap < 0.3, f"Event-Loop {worst_gap:.2f}s blockiert"
        assert result["score"] == 78.0

    def test_timeout_bounds_the_wait(self):
        """Das deklarierte Timeout begrenzt die Wartezeit tatsaechlich."""
        analyzer = VisualAnalyzer()
        analyzer.API_TIMEOUT_S = 0.1
        response = MagicMock()
        response.content = [MagicMock(text=VALID_JSON)]

        def slow_create(*args, **kwargs):
            time.sleep(1.5)   # deutlich laenger als das Timeout
            return response

        analyzer._client, _ = _mock_client(side_effect=slow_create)
        path = _stub_image()

        real_retry = analyzer_module.retry_async

        async def fast_retry(func, *args, **kwargs):
            # Backoff verkuerzen, damit der Test schnell bleibt; das Timeout
            # bleibt unveraendert — es ist der Pruefgegenstand.
            kwargs["base_delay"] = 0.01
            kwargs["max_delay"] = 0.01
            return await real_retry(func, *args, **kwargs)

        async def main():
            started = time.monotonic()
            result = await analyzer.analyze_image(
                path, "interior_overview", "cruising_sail"
            )
            return time.monotonic() - started, result

        try:
            with patch.object(analyzer_module, "retry_async", fast_retry):
                elapsed, result = asyncio.run(main())
        finally:
            os.unlink(path)

        # 4 Versuche x 0.1s Timeout — ohne wirksames Timeout waeren es >=6s.
        assert elapsed < 2.0, f"Timeout wirkungslos: {elapsed:.2f}s gewartet"
        assert result["score"] is None
        assert "fehlgeschlagen" in result["error"]


# ===========================================================================
# B-14 — overall_findings in der Aggregation
# ===========================================================================


class TestBatchCollectsOverallFindings:
    def _batch_with(self, analysis):
        analyzer = VisualAnalyzer()

        async def mock_analyze(image_path, image_type, boat_class, **kwargs):
            return {
                "image_path": image_path,
                "score": 70.0,
                "confidence": {
                    "level": "visual_high",
                    "is_usable": True,
                    "assessment_certainty": 0.9,
                },
                "analysis": analysis,
            }

        with patch.object(analyzer, "analyze_image", side_effect=mock_analyze):
            return asyncio.run(
                analyzer.analyze_batch(
                    [{"path": "/i1.jpg", "image_type": "build_quality"}], "cruising_sail"
                )
            )

    def test_overall_findings_reach_the_user(self):
        """Befunde des Build-Quality-Prompts duerfen nicht verworfen werden."""
        batch = self._batch_with({
            "overall_quality_score": 70,
            "overall_findings": [
                {"observation": "Fugen ungleichmaessig", "category": "joinery"}
            ],
        })
        observations = [f["observation"] for f in batch["findings"]]
        assert "Fugen ungleichmaessig" in observations

    def test_both_finding_keys_are_merged_and_deduplicated(self):
        batch = self._batch_with({
            "findings": [{"observation": "Salon hell"}, {"observation": "Doppelt"}],
            "overall_findings": [{"observation": "Doppelt"}, {"observation": "Spaltmass 4mm"}],
        })
        observations = [f["observation"] for f in batch["findings"]]
        assert observations.count("Doppelt") == 1
        assert set(observations) == {"Salon hell", "Doppelt", "Spaltmass 4mm"}

    def test_non_dict_analysis_is_skipped(self):
        batch = self._batch_with(None)
        assert batch["findings"] == []


# ===========================================================================
# B-3 / B-15 — Bildskalierung vor der base64-Kodierung
# ===========================================================================


def _noise_jpeg(width, height, path, quality=95):
    from PIL import Image
    img = Image.effect_noise((width, height), 64).convert("RGB")
    img.save(path, "JPEG", quality=quality)
    return path


class TestImageDownscaling:
    def setup_method(self):
        self.analyzer = VisualAnalyzer()

    def test_large_image_is_downscaled_before_encoding(self):
        """Ein grosses Foto wird vor dem Kodieren verkleinert."""
        from PIL import Image

        with tempfile.TemporaryDirectory() as d:
            path = os.path.join(d, "big.jpg")
            _noise_jpeg(2400, 1800, path)
            raw_size = os.path.getsize(path)

            data, media_type = self.analyzer._load_image_base64(path)

            decoded = base64.b64decode(data)
            with Image.open(io.BytesIO(decoded)) as img:
                assert max(img.size) == analyzer_module.MAX_IMAGE_EDGE_PX
            assert len(decoded) < raw_size / 2
            assert media_type == "image/jpeg"

    def test_small_image_is_passed_through_unchanged(self):
        """Kleine Bilder werden nicht unnoetig neu kodiert."""
        with tempfile.TemporaryDirectory() as d:
            path = os.path.join(d, "small.jpg")
            _noise_jpeg(400, 300, path)
            original = open(path, "rb").read()

            data, media_type = self.analyzer._load_image_base64(path)

            assert base64.b64decode(data) == original
            assert media_type == "image/jpeg"

    def test_oversized_bytes_are_recompressed(self):
        """Auch masshaltige, aber sehr grosse Dateien werden komprimiert."""
        with tempfile.TemporaryDirectory() as d:
            path = os.path.join(d, "heavy.png")
            from PIL import Image
            Image.effect_noise((1000, 1000), 64).convert("RGB").save(path, "PNG")
            raw_size = os.path.getsize(path)

            with patch.object(analyzer_module, "MAX_IMAGE_BYTES", raw_size - 1):
                data, media_type = self.analyzer._load_image_base64(path)

            assert len(base64.b64decode(data)) < raw_size
            assert media_type == "image/jpeg"

    def test_transparency_is_preserved_as_png(self):
        """Bilder mit Alphakanal bleiben PNG (kein schwarzer JPEG-Hintergrund)."""
        from PIL import Image

        with tempfile.TemporaryDirectory() as d:
            path = os.path.join(d, "alpha.png")
            Image.new("RGBA", (2000, 1200), (10, 20, 30, 128)).save(path, "PNG")

            data, media_type = self.analyzer._load_image_base64(path)

            assert media_type == "image/png"
            with Image.open(io.BytesIO(base64.b64decode(data))) as img:
                assert img.mode == "RGBA"
                assert max(img.size) == analyzer_module.MAX_IMAGE_EDGE_PX

    def test_unreadable_file_falls_back_to_raw_bytes(self):
        """Defekte Dateien lassen die Analyse nicht scheitern."""
        with tempfile.TemporaryDirectory() as d:
            path = os.path.join(d, "junk.jpg")
            payload = b"\xff\xd8\xff\xe0" + b"\x00" * 50
            with open(path, "wb") as f:
                f.write(payload)

            data, media_type = self.analyzer._load_image_base64(path)

            assert base64.b64decode(data) == payload
            assert media_type == "image/jpeg"

    def test_prepare_without_pillow_returns_original(self):
        """Ohne Pillow wird unveraendert (aber funktionsfaehig) gesendet."""
        import builtins

        real_import = builtins.__import__

        def no_pillow(name, *args, **kwargs):
            if name.startswith("PIL"):
                raise ImportError("no pillow")
            return real_import(name, *args, **kwargs)

        payload = b"x" * 100
        with patch.object(builtins, "__import__", no_pillow):
            data, media_type = self.analyzer._prepare_image_bytes(payload, "image/jpeg")

        assert data == payload
        assert media_type == "image/jpeg"
