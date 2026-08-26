"""Bindeglied zwischen Pipeline B (Bildanalyse) und der Score-Fusion.

Warum es dieses Modul braucht: ``score_fusion.py`` war vollstaendig implementiert
und getestet, hatte aber **keinen einzigen Aufrufer**. Fotos beeinflussten damit
keinen einzigen Score — die in CLAUDE.md dokumentierten Fusionsgewichte steuerten
nichts. Zwei Dinge fehlten dazwischen:

1. **Andere Schluesselung.** Die Fusion erwartet Ergebnisse je *Analysemodul*
   (``ergonomics``, ``materials`` …), der Analyzer liefert sie je *Bild* mit
   einem ``image_type`` (``interior_overview``, ``helm_station`` …).
2. **Anderes Konfidenzformat.** Die Fusion erwartet ``confidence`` als String
   (``"visual_medium"``), der Analyzer liefert ein Dict
   (``{"level": "visual_medium", "is_usable": True, …}``). ``CONFIDENCE_DISCOUNT``
   haette darauf mit ``TypeError: unhashable type: 'dict'`` abgebrochen — die
   Fusion war also nicht nur unverdrahtet, sie waere beim Anschliessen
   abgestuerzt.

Die Zuordnung Bild → Modul leitet sich aus dem **Prompt** ab, nicht aus dem
Etikett des Bildtyps: Massgeblich ist, wonach das Bild tatsaechlich befragt wird.
"""

from __future__ import annotations

import logging

logger = logging.getLogger(__name__)


# Bildtyp -> Analysemodule, zu denen dieses Bild etwas aussagt.
#
# Abgeleitet aus PROMPT_REGISTRY (app/services/visual/prompts/__init__.py):
# Ein Raumbild wird nach Raumwirkung und Nutzbarkeit befragt, ein Detailfoto nach
# Verarbeitungsqualitaet, eine Materialprobe nach Material. Ein Bildtyp ohne
# Eintrag traegt bewusst zu KEINEM Modul bei — lieber keine Aussage als eine
# hergeleitete.
IMAGE_TYPE_TO_MODULES: dict[str, tuple[str, ...]] = {
    # Raumanalyse-Prompt: Proportionen, Wege, Stauraum
    "interior_overview": ("ergonomics", "volume_storage", "emotional"),
    "cockpit": ("ergonomics", "emotional"),
    "floorplan_photo": ("ergonomics", "volume_storage"),
    # Verarbeitungsqualitaets-Prompt: Spaltmasse, Fugen, Oberflaechen
    "interior_detail": ("production", "materials"),
    "exterior_detail": ("production", "materials"),
    # Materialprompt
    "material_sample": ("materials",),
    # Emotionsprompt
    "rendering": ("emotional",),
    # Aussenansicht: Formensprache und Wirkung
    "exterior_overview": ("brand_dna", "emotional"),
    # Steuerstand-Ergonomie
    "helm_station": ("ergonomics",),
}


def _confidence_level(visual_result: dict) -> str | None:
    """Den Konfidenz-String aus dem Analyzer-Ergebnis holen.

    Der Analyzer verschachtelt ihn unter ``confidence.level``; aeltere bzw.
    direkt gebaute Ergebnisse fuehren ihn flach als String. Beides wird
    akzeptiert, alles andere gilt als unbrauchbar.
    """
    confidence = visual_result.get("confidence")
    if isinstance(confidence, str):
        return confidence
    if isinstance(confidence, dict):
        level = confidence.get("level")
        return level if isinstance(level, str) else None
    return None


def _is_usable(visual_result: dict) -> bool:
    """Nur belastbare Bildbefunde duerfen in eine Note einfliessen.

    Der Konfidenz-Waechter setzt ``is_usable`` auf False, wenn das Bild zu
    schlecht, das Motiv unpassend oder das Modell selbst unsicher ist. Solche
    Ergebnisse fliessen NICHT in die Fusion — sonst wuerde genau die Unsicherheit
    zur Zahl, die der Waechter gerade festgestellt hat.
    """
    confidence = visual_result.get("confidence")
    if isinstance(confidence, dict) and confidence.get("is_usable") is False:
        return False
    if _confidence_level(visual_result) == "visual_insufficient":
        return False
    if visual_result.get("error"):
        return False
    score = visual_result.get("score")
    return isinstance(score, (int, float)) and not isinstance(score, bool)


def visual_results_to_module_scores(
    visual_analyses: list[dict] | None,
) -> dict[str, dict]:
    """Bildanalysen zu modulweisen Visual-Scores verdichten.

    Args:
        visual_analyses: Liste von Analyzer-Ergebnissen. Jedes braucht
            ``image_type``, ``score`` und ``confidence``.

    Returns:
        ``{modul: {"score": float, "confidence": str, "image_count": int}}`` —
        genau das Format, das ``score_fusion.fuse_all_modules`` erwartet.
        Module ohne verwertbares Bild fehlen im Ergebnis.
    """
    if not visual_analyses:
        return {}

    # Rangfolge fuer die zusammengefasste Konfidenz: die SCHLECHTESTE der
    # beteiligten Bilder bestimmt sie. Zwei mittelmaessige Fotos ergeben keine
    # hohe Sicherheit.
    order = ["visual_high", "visual_medium", "visual_low", "visual_insufficient"]

    buckets: dict[str, list[tuple[float, str]]] = {}
    for result in visual_analyses:
        if not isinstance(result, dict):
            continue
        image_type = result.get("image_type")
        modules = IMAGE_TYPE_TO_MODULES.get(image_type or "")
        if not modules:
            if image_type:
                logger.debug("Bildtyp %r ist keinem Modul zugeordnet", image_type)
            continue
        if not _is_usable(result):
            continue
        level = _confidence_level(result) or "visual_low"
        score = float(result["score"])
        for module in modules:
            buckets.setdefault(module, []).append((score, level))

    fused: dict[str, dict] = {}
    for module, entries in buckets.items():
        scores = [s for s, _ in entries]
        levels = [lvl for _, lvl in entries]
        worst = max(levels, key=lambda lvl: order.index(lvl) if lvl in order else len(order))
        fused[module] = {
            "score": round(sum(scores) / len(scores), 1),
            "confidence": worst,
            "image_count": len(entries),
        }
    return fused
