"""Der DXF-Import darf keine Durchgangsbreite erfinden.

``_detect_shared_edges`` misst den Abstand der naechstgelegenen ECKPUNKTE zweier
Zonenpolygone — ein Nachbarschaftstest, keine Tuerbreite. Daraus wurde frueher
``width_mm = max(tolerance, min_dist)`` gebildet. Bei aneinandergrenzenden Zonen
ist der Abstand praktisch 0, es kamen also immer exakt 100 mm heraus. Die
Ergonomie meldete daraufhin fuer JEDEN importierten Durchgang "kritisch schmal
(100mm)" — mit dem Konfidenzsiegel ``measured``, also als Messwert ausgegeben.

Richtig ist: Nachbarschaft melden, Breite als unbekannt kennzeichnen, und in der
Ergonomie als nicht beurteilbar behandeln.
"""

import io

import ezdxf
import pytest

from app.services.analysis.ergonomics import (
    analyze_passage_widths,
    run_ergonomics_analysis,
)
from app.services.dxf.parser import _detect_shared_edges, parse_dxf


def _dxf_with_adjacent_zones(layers=("CABIN", "SALON", "HEAD", "COCKPIT")) -> bytes:
    doc = ezdxf.new()
    msp = doc.modelspace()
    for i, layer in enumerate(layers):
        y = i * 1000
        msp.add_lwpolyline(
            [(0, y), (3000, y), (3000, y + 1000), (0, y + 1000)],
            dxfattribs={"layer": layer},
        )
    buffer = io.BytesIO()
    text = io.TextIOWrapper(buffer, encoding="utf-8")
    doc.write(text)
    text.flush()
    return buffer.getvalue()


class TestKeineErfundeneBreite:
    def test_import_reports_unknown_width(self):
        result = parse_dxf(_dxf_with_adjacent_zones())
        assert result["passages"], "Angrenzende Zonen muessen als Durchgang erkannt werden"
        for passage in result["passages"]:
            assert passage["width_mm"] is None, (
                f"Breite {passage['width_mm']} wurde erfunden — aus Zonenpolygonen "
                f"ist sie nicht ableitbar."
            )
            assert passage["width_source"] == "unknown"

    def test_no_passage_is_reported_as_exactly_100mm(self):
        """Genau dieser Wert war das Artefakt der alten Formel."""
        result = parse_dxf(_dxf_with_adjacent_zones())
        assert all(p["width_mm"] != 100.0 for p in result["passages"])

    def test_distant_zones_are_not_connected(self):
        zones = [
            {"name": "a", "polygon": [[0, 0], [1000, 0], [1000, 1000], [0, 1000]]},
            {"name": "b", "polygon": [[50000, 0], [51000, 0], [51000, 1000], [50000, 1000]]},
        ]
        assert _detect_shared_edges(zones) == []

    def test_adjacent_zones_are_connected(self):
        zones = [
            {"name": "a", "polygon": [[0, 0], [1000, 0], [1000, 1000], [0, 1000]]},
            {"name": "b", "polygon": [[0, 1000], [1000, 1000], [1000, 2000], [0, 2000]]},
        ]
        passages = _detect_shared_edges(zones)
        assert len(passages) == 1
        assert passages[0]["width_mm"] is None


class TestNichtFiniteKoordinaten:
    def test_nan_coordinates_do_not_raise(self):
        zones = [
            {"name": "a", "polygon": [[0, 0], [float("nan"), 0], [1000, 1000], [0, 1000]]},
            {"name": "b", "polygon": [[0, 1000], [1000, 1000], [1000, 2000], [0, 2000]]},
        ]
        _detect_shared_edges(zones)  # darf nicht werfen

    def test_huge_coordinates_do_not_overflow(self):
        """Sehr grosse Koordinaten loesten frueher einen OverflowError (HTTP 500) aus."""
        zones = [
            {"name": "a", "polygon": [[0, 0], [1e308, 0], [1e308, 1e308], [0, 1e308]]},
            {"name": "b", "polygon": [[0, 0], [1000, 0], [1000, 1000], [0, 1000]]},
        ]
        _detect_shared_edges(zones)  # darf nicht werfen

    def test_zone_without_usable_polygon_is_skipped(self):
        zones = [
            {"name": "a", "polygon": []},
            {"name": "b", "polygon": [[0, 0], [1000, 0], [1000, 1000], [0, 1000]]},
        ]
        assert _detect_shared_edges(zones) == []


class TestErgonomieBehandeltUnbekannteBreite:
    CONFIG = {"min_passage_width_mm": 650, "critical_passage_width_mm": 500}

    def test_unknown_width_is_not_a_critical_finding(self):
        passages = [{"from_zone": "a", "to_zone": "b", "width_mm": None}]
        score, warnings, metrics = analyze_passage_widths(passages, self.CONFIG)
        assert metrics["unknown_width_passages"] == 1
        assert metrics["critical_passages"] == 0
        assert not any(w["severity"] == "critical" for w in warnings)

    def test_unknown_width_is_flagged_as_not_assessable(self):
        passages = [{"from_zone": "a", "to_zone": "b", "width_mm": None}]
        _, warnings, _ = analyze_passage_widths(passages, self.CONFIG)
        assert any("nicht beurteilbar" in w["message"] for w in warnings)

    def test_known_widths_are_still_judged(self):
        passages = [{"from_zone": "a", "to_zone": "b", "width_mm": 300.0}]
        _, warnings, metrics = analyze_passage_widths(passages, self.CONFIG)
        assert metrics["critical_passages"] == 1

    def test_unknown_widths_do_not_dilute_a_real_finding(self):
        """Nur bewertbare Durchgaenge gehen in die Note ein."""
        only_narrow = analyze_passage_widths(
            [{"from_zone": "a", "to_zone": "b", "width_mm": 300.0}], self.CONFIG
        )[0]
        with_unknowns = analyze_passage_widths(
            [
                {"from_zone": "a", "to_zone": "b", "width_mm": 300.0},
                {"from_zone": "c", "to_zone": "d", "width_mm": None},
                {"from_zone": "e", "to_zone": "f", "width_mm": None},
            ],
            self.CONFIG,
        )[0]
        assert only_narrow == pytest.approx(with_unknowns)

    def test_full_dxf_to_ergonomics_path_is_clean(self):
        parsed = parse_dxf(_dxf_with_adjacent_zones())
        result = run_ergonomics_analysis(
            zones=parsed["zones"], passages=parsed["passages"], boat_class="cruising_sail"
        )
        assert result["degraded_subanalyses"] == [], (
            "Eine unbekannte Breite darf keine Teilanalyse zum Absturz bringen"
        )
        narrow = [w for w in result["warnings"] if "schmal" in w.get("message", "")]
        assert not narrow, f"Erfundene Schmal-Befunde aus dem Import: {narrow}"
