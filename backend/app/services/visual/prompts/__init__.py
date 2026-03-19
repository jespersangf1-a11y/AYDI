"""Prompt registry for visual analysis.

Maps image types to appropriate prompt generator functions.
Each prompt function returns a German-language prompt string
that instructs the AI to return structured JSON.
"""
from app.services.visual.prompts.spatial import get_spatial_analysis_prompt
from app.services.visual.prompts.quality import get_build_quality_prompt
from app.services.visual.prompts.materials import get_material_assessment_prompt
from app.services.visual.prompts.emotional import get_emotional_impact_prompt
from app.services.visual.prompts.exterior import get_exterior_assessment_prompt
from app.services.visual.prompts.helm import get_helm_ergonomics_prompt

PROMPT_REGISTRY: dict[str, callable] = {
    "interior_overview": get_spatial_analysis_prompt,
    "interior_detail": get_build_quality_prompt,
    "exterior_overview": get_exterior_assessment_prompt,
    "exterior_detail": get_build_quality_prompt,
    "material_sample": get_material_assessment_prompt,
    "rendering": get_emotional_impact_prompt,
    "cockpit": get_spatial_analysis_prompt,
    "helm_station": get_helm_ergonomics_prompt,
    "floorplan_photo": get_spatial_analysis_prompt,
}


def get_prompt(
    image_type: str,
    boat_class: str,
    zone_type: str | None = None,
    context: dict | None = None,
) -> str:
    """Get the appropriate prompt for an image type and boat class.

    Args:
        image_type: One of the keys in PROMPT_REGISTRY.
        boat_class: Yacht class (e.g. 'cruising_sail').
        zone_type: Optional zone type for focused analysis.
        context: Optional additional context (length_m, beam_m, etc.).

    Returns:
        German-language prompt string requesting structured JSON output.
    """
    prompt_fn = PROMPT_REGISTRY.get(image_type, get_spatial_analysis_prompt)
    return prompt_fn(boat_class, zone_type, context)
