"""Simple file-based cache for visual analysis results.

Avoids re-analyzing the same image with the same parameters.
Results are stored as JSON files keyed by a hash of image content
and analysis parameters.
"""
import hashlib
import json
import logging
from pathlib import Path

logger = logging.getLogger(__name__)


class AnalysisCache:
    """File-based cache for visual analysis results."""

    def __init__(self, cache_dir: str = "backend/uploads/cache"):
        self.cache_dir = Path(cache_dir)
        try:
            self.cache_dir.mkdir(parents=True, exist_ok=True)
        except OSError:
            logger.warning("Could not create cache directory: %s", cache_dir)

    def get_cache_key(
        self,
        image_path: str,
        image_type: str,
        boat_class: str,
        analysis_depth: str,
    ) -> str:
        """Generate a deterministic cache key from image content and parameters.

        Args:
            image_path: Path to the image file.
            image_type: Type of image (e.g. 'interior_overview').
            boat_class: Yacht class (e.g. 'cruising_sail').
            analysis_depth: Analysis depth ('standard' or 'detailed').

        Returns:
            A hex digest string used as cache key.
        """
        hasher = hashlib.sha256()

        # Hash file content
        try:
            with open(image_path, "rb") as f:
                for chunk in iter(lambda: f.read(8192), b""):
                    hasher.update(chunk)
        except OSError:
            logger.warning("Could not read file for hashing: %s", image_path)
            hasher.update(image_path.encode("utf-8"))

        # Hash parameters
        hasher.update(image_type.encode("utf-8"))
        hasher.update(boat_class.encode("utf-8"))
        hasher.update(analysis_depth.encode("utf-8"))

        return hasher.hexdigest()

    def get(self, cache_key: str) -> dict | None:
        """Retrieve a cached analysis result.

        Args:
            cache_key: The cache key from get_cache_key().

        Returns:
            Cached result dict, or None if not found.
        """
        cache_path = self.cache_dir / f"{cache_key}.json"
        if not cache_path.exists():
            return None

        try:
            with open(cache_path, "r", encoding="utf-8") as f:
                result = json.load(f)
            logger.debug("Cache hit for key: %s", cache_key[:16])
            return result
        except (json.JSONDecodeError, OSError):
            logger.warning("Corrupt cache entry: %s", cache_key[:16])
            return None

    def set(self, cache_key: str, result: dict) -> None:
        """Store an analysis result in the cache.

        Args:
            cache_key: The cache key from get_cache_key().
            result: Analysis result dict to cache.
        """
        cache_path = self.cache_dir / f"{cache_key}.json"
        try:
            with open(cache_path, "w", encoding="utf-8") as f:
                json.dump(result, f, ensure_ascii=False, indent=2)
            logger.debug("Cached result for key: %s", cache_key[:16])
        except OSError:
            logger.warning("Could not write cache entry: %s", cache_key[:16])

    def invalidate(self, cache_key: str) -> bool:
        """Remove a cached entry.

        Returns:
            True if an entry was removed, False if it did not exist.
        """
        cache_path = self.cache_dir / f"{cache_key}.json"
        if cache_path.exists():
            try:
                cache_path.unlink()
                return True
            except OSError:
                logger.warning("Could not delete cache entry: %s", cache_key[:16])
        return False
