import io
import ezdxf
from app.services.dxf.parser import parse_dxf, DEFAULT_LAYER_MAP


def _make_test_dxf(layers_and_polys):
    doc = ezdxf.new("R2010")
    msp = doc.modelspace()
    for layer_name, polylines in layers_and_polys.items():
        doc.layers.add(layer_name)
        for points in polylines:
            msp.add_lwpolyline(points, dxfattribs={"layer": layer_name}, close=True)
    stream = io.StringIO()
    doc.write(stream)
    return stream.getvalue().encode("utf-8")


def test_parse_basic_zones():
    content = _make_test_dxf({
        "CABIN": [[(0, 0), (2000, 0), (2000, 2000), (0, 2000)]],
        "SALON": [[(2000, 0), (5000, 0), (5000, 3000), (2000, 3000)]],
    })
    result = parse_dxf(content)
    assert len(result["zones"]) == 2
    types = {z["zone_type"] for z in result["zones"]}
    assert "cabin" in types
    assert "salon" in types


def test_parse_layer_mapping():
    content = _make_test_dxf({
        "WC": [[(0, 0), (1000, 0), (1000, 1000), (0, 1000)]],
        "GALLEY": [[(1000, 0), (3000, 0), (3000, 2000), (1000, 2000)]],
    })
    result = parse_dxf(content)
    types = {z["zone_type"] for z in result["zones"]}
    assert "head" in types
    assert "pantry" in types


def test_parse_custom_layer_map():
    content = _make_test_dxf({
        "MY_ROOM": [[(0, 0), (2000, 0), (2000, 2000), (0, 2000)]],
    })
    result = parse_dxf(content, layer_map={"MY_ROOM": "cabin"})
    assert len(result["zones"]) == 1
    assert result["zones"][0]["zone_type"] == "cabin"


def test_parse_unknown_layer_skipped():
    content = _make_test_dxf({
        "RANDOM_LAYER": [[(0, 0), (1000, 0), (1000, 1000), (0, 1000)]],
        "CABIN": [[(0, 0), (2000, 0), (2000, 2000), (0, 2000)]],
    })
    result = parse_dxf(content)
    assert len(result["zones"]) == 1


def test_parse_coordinates_in_mm():
    content = _make_test_dxf({
        "CABIN": [[(0, 0), (3000, 0), (3000, 2500), (0, 2500)]],
    })
    result = parse_dxf(content)
    polygon = result["zones"][0]["polygon"]
    assert polygon[1][0] == 3000.0


def test_parse_passage_layer():
    doc = ezdxf.new("R2010")
    msp = doc.modelspace()
    doc.layers.add("CABIN")
    doc.layers.add("SALON")
    doc.layers.add("PASSAGE")
    msp.add_lwpolyline([(0, 0), (2000, 0), (2000, 2000), (0, 2000)], dxfattribs={"layer": "CABIN"}, close=True)
    msp.add_lwpolyline([(2000, 0), (5000, 0), (5000, 2000), (2000, 2000)], dxfattribs={"layer": "SALON"}, close=True)
    msp.add_line((2000, 0), (2000, 2000), dxfattribs={"layer": "PASSAGE"})
    stream = io.StringIO()
    doc.write(stream)
    content = stream.getvalue().encode("utf-8")
    result = parse_dxf(content)
    assert len(result["zones"]) == 2


def test_parse_invalid_dxf():
    try:
        parse_dxf(b"not a valid dxf file")
        assert False, "Should have raised ValueError"
    except ValueError as e:
        assert "DXF" in str(e) or "ungültig" in str(e).lower()


def test_parse_empty_dxf():
    content = _make_test_dxf({})
    try:
        parse_dxf(content)
        assert False, "Should have raised ValueError"
    except ValueError:
        pass
