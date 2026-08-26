"""Die teuersten Routen muessen im striktesten Rate-Limit-Eimer landen.

Die Zuordnung lief ueber reine Praefixe und traf damit genau die Routen NICHT,
fuer die sie gedacht war:

* ``/api/v1/projects/{id}/images`` — loest eine kostenpflichtige Claude-Vision-
  Analyse aus — beginnt mit ``/api/v1/projects`` und fiel in den 120/min-Eimer
  statt in den 10/min-Eimer fuer Bilder.
* ``/api/v1/import-cad`` stand in der Konfiguration, existiert aber als Route
  gar nicht. Die echten CAD-Pfade (``/projects/{id}/import/step|iges``,
  ``/projects/{id}/layouts/import-dxf``) lagen ebenfalls bei 120/min — der
  CAD-Eimer war vollstaendig wirkungslos.

Zusaetzlich abgesichert: die CSRF-Ausnahme fuer die oeffentliche Schnellanalyse
galt per Praefix auch fuer deren authentifizierte Unterrouten.
"""

import pytest

from app.core.middleware import CSRFMiddleware, RateLimitMiddleware


@pytest.fixture(scope="module")
def limiter() -> RateLimitMiddleware:
    return RateLimitMiddleware.__new__(RateLimitMiddleware)


class TestTeuerstRoutenZuerst:
    @pytest.mark.parametrize(
        "path",
        [
            "/api/v1/images/analyze",
            "/api/v1/images/analyze-batch",
            "/api/v1/projects/abc-123/images",
            "/api/v1/quick-analysis/abc-123/images",
        ],
    )
    def test_image_routes_use_the_image_bucket(self, limiter, path):
        assert limiter._match_route(path) == "images"
        assert limiter._limit_for("images")[0] == 10

    @pytest.mark.parametrize(
        "path",
        [
            "/api/v1/projects/abc-123/import/step",
            "/api/v1/projects/abc-123/import/iges",
            "/api/v1/projects/abc-123/layouts/import-dxf",
        ],
    )
    def test_cad_routes_use_the_cad_bucket(self, limiter, path):
        assert limiter._match_route(path) == "cad_import"
        assert limiter._limit_for("cad_import")[0] == 10

    def test_image_routes_are_stricter_than_their_parent(self):
        """Der Kern des Fehlers: Die Unterroute fiel in den Eimer des Elternpfads."""
        limiter = RateLimitMiddleware.__new__(RateLimitMiddleware)
        child = limiter._limit_for(limiter._match_route("/api/v1/projects/x/images"))[0]
        parent = limiter._limit_for(limiter._match_route("/api/v1/projects"))[0]
        assert child < parent, (
            f"Bild-Upload ({child}/min) darf nicht so grosszuegig sein wie "
            f"der Projektpfad ({parent}/min)"
        )


class TestUebrigeEimer:
    @pytest.mark.parametrize(
        "path,expected",
        [
            ("/api/v1/auth/login", "auth"),
            ("/api/v1/quick-analysis", "quick_analysis"),
            ("/api/v1/knowledge/categories", "knowledge"),
            ("/api/v1/projects", "projects"),
            ("/api/v1/layouts", "layouts"),
            ("/api/v1/materials", "default"),
        ],
    )
    def test_bucket_assignment(self, limiter, path, expected):
        assert limiter._match_route(path) == expected

    def test_every_rule_name_is_unique(self):
        names = [name for name, _pattern, _limit in RateLimitMiddleware.RULES]
        assert len(names) == len(set(names))

    def test_every_rule_has_a_positive_limit(self):
        for name, _pattern, (max_requests, window) in RateLimitMiddleware.RULES:
            assert max_requests > 0, name
            assert window > 0, name

    def test_unknown_route_falls_back_to_default(self, limiter):
        assert limiter._match_route("/api/v1/etwas-neues") == "default"
        assert limiter._limit_for("default") == RateLimitMiddleware.DEFAULT_LIMIT


class TestCsrfAusnahme:
    def test_public_quick_analysis_entry_is_exempt(self):
        assert "/api/v1/quick-analysis" in CSRFMiddleware.EXEMPT_PATHS

    def test_quick_analysis_subroutes_are_not_exempt(self):
        """Die Bild-Unterroute ist authentifiziert und gehoert unter CSRF-Schutz."""
        subroute = "/api/v1/quick-analysis/abc-123/images"
        assert subroute not in CSRFMiddleware.EXEMPT_PATHS
        assert not any(
            subroute.startswith(prefix) for prefix in CSRFMiddleware.EXEMPT_PATH_PREFIXES
        ), "Ein Praefix nimmt die Unterroute wieder aus"

    def test_exempt_prefixes_only_cover_unauthenticated_entry_points(self):
        """Ausgenommen darf nur sein, wo es noch keine Sitzung zu schuetzen gibt."""
        for prefix in CSRFMiddleware.EXEMPT_PATH_PREFIXES:
            assert prefix.startswith(("/api/v1/auth/", "/health", "/docs", "/openapi")), (
                f"Unerwartete CSRF-Ausnahme: {prefix}"
            )


def test_reset_clears_counters():
    RateLimitMiddleware._requests["1.2.3.4"]["images"].append(123.0)
    RateLimitMiddleware.reset()
    assert not RateLimitMiddleware._requests
