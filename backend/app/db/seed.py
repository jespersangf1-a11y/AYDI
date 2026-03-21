"""Seed script with example yacht projects.

Run with: PYTHONPATH=. python -m app.db.seed
"""
import asyncio
import logging

from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from app.db.database import async_session, engine
from app.models.models import Base, Layout, Project, Material, CompetitorModel

logger = logging.getLogger(__name__)


SEED_PROJECTS = [
    {
        "name": "Meridian 40 Cruiser",
        "description": "12m Fahrtensegler mit optimiertem Innenraumlayout für Langfahrt",
        "boat_class": "cruising_sail",
        "length_m": 12.2,
        "beam_m": 3.8,
        "status": "active",
    },
    {
        "name": "Nordic 28 Weekender",
        "description": "Kompakte Segelyacht für Wochenendtörns",
        "boat_class": "small_sail",
        "length_m": 8.5,
        "beam_m": 2.8,
        "status": "draft",
    },
    {
        "name": "Avalon 65 Flybridge",
        "description": "Große Motoryacht mit Flybridge und Crewbereich",
        "boat_class": "large_motor",
        "length_m": 19.8,
        "beam_m": 5.2,
        "status": "draft",
    },
]

MERIDIAN_ZONES = [
    {"name": "cockpit", "zone_type": "cockpit",
     "polygon": [[0, 0], [3800, 0], [3800, 2500], [0, 2500]],
     "height_mm": 2200,
     "is_crew_area": False, "is_guest_area": True, "visibility_angle": None,
     "properties": {"has_railing": True, "material_count": 3}},
    {"name": "salon", "zone_type": "salon",
     "polygon": [[0, 2500], [3800, 2500], [3800, 5500], [0, 5500]],
     "height_mm": 1950,
     "is_crew_area": False, "is_guest_area": True, "visibility_angle": None,
     "properties": {"window_area_pct": 0.30, "material_count": 5, "furniture_area_pct": 0.45}},
    {"name": "pantry", "zone_type": "pantry",
     "polygon": [[0, 5500], [1800, 5500], [1800, 7500], [0, 7500]],
     "height_mm": 1950,
     "is_crew_area": False, "is_guest_area": True, "visibility_angle": None,
     "properties": {"window_area_pct": 0.12, "material_count": 4, "furniture_area_pct": 0.55}},
    {"name": "helm", "zone_type": "helm",
     "polygon": [[1800, 5500], [3800, 5500], [3800, 7500], [1800, 7500]],
     "height_mm": 1950,
     "is_crew_area": False, "is_guest_area": False, "visibility_angle": 230,
     "properties": {"material_count": 3}},
    {"name": "fwd_cabin", "zone_type": "cabin",
     "polygon": [[500, 7500], [3300, 7500], [3300, 10000], [500, 10000]],
     "height_mm": 1900,
     "is_crew_area": False, "is_guest_area": True, "visibility_angle": None,
     "properties": {"window_area_pct": 0.18, "material_count": 4, "furniture_area_pct": 0.50}},
    # Intentionally overlaps with cockpit — demonstrates suboptimal layout
    {"name": "aft_cabin", "zone_type": "cabin",
     "polygon": [[0, 0], [1800, 0], [1800, 2000], [0, 2000]],
     "height_mm": 1850,
     "is_crew_area": False, "is_guest_area": True, "visibility_angle": None,
     "properties": {"window_area_pct": 0.10, "material_count": 3, "furniture_area_pct": 0.48}},
    {"name": "head", "zone_type": "head",
     "polygon": [[3300, 7500], [3800, 7500], [3800, 9000], [3300, 9000]],
     "height_mm": 1900,
     "is_crew_area": False, "is_guest_area": True, "visibility_angle": None,
     "properties": {"window_area_pct": 0.05, "material_count": 3, "furniture_area_pct": 0.35}},
    {"name": "engine_room", "zone_type": "engine",
     "polygon": [[1800, 0], [3800, 0], [3800, 1500], [1800, 1500]],
     "height_mm": 1500,
     "is_crew_area": True, "is_guest_area": False, "visibility_angle": None,
     "properties": {"material_count": 2}},
    {"name": "storage_aft", "zone_type": "storage",
     "polygon": [[0, 2000], [1000, 2000], [1000, 2500], [0, 2500]],
     "height_mm": 1200,
     "is_crew_area": False, "is_guest_area": False, "visibility_angle": None,
     "properties": {"furniture_area_pct": 0.80}},
]

MERIDIAN_PASSAGES = [
    {"from_zone": "cockpit", "to_zone": "salon", "width_mm": 750, "is_primary": True},
    {"from_zone": "salon", "to_zone": "pantry", "width_mm": 700, "is_primary": True},
    {"from_zone": "salon", "to_zone": "helm", "width_mm": 700, "is_primary": True},
    {"from_zone": "helm", "to_zone": "fwd_cabin", "width_mm": 650, "is_primary": True},
    {"from_zone": "fwd_cabin", "to_zone": "head", "width_mm": 600, "is_primary": False},
    {"from_zone": "cockpit", "to_zone": "aft_cabin", "width_mm": 550, "is_primary": True},
    {"from_zone": "cockpit", "to_zone": "engine_room", "width_mm": 500, "is_primary": False},
    {"from_zone": "cockpit", "to_zone": "storage_aft", "width_mm": 650, "is_primary": False},
]

SEED_MATERIALS = [
    {
        "name": "Teak Burma Grade A",
        "category": "wood",
        "subcategory": "tropical_hardwood",
        "manufacturer": "Various",
        "cost_per_unit": 45.0,
        "cost_unit": "sqm",
        "lifespan_years": 20,
        "maintenance_interval_months": 12,
        "maintenance_cost_factor": 0.05,
        "properties": {"density_kg_m3": 650, "hardness_janka": 1155, "color": "golden_brown", "uv_resistance": "high", "water_resistance": "high", "installation_methods": [{"method": "Fastened with stainless steel screws", "difficulty": "medium", "tools_required": ["cordless drill", "screwdriver bits", "clamps", "measuring tape"], "typical_errors": ["Cross-threading screws in dense wood", "Over-tightening causing splitting", "Misalignment of grain pattern"]}, {"method": "Glued with two-part epoxy adhesive", "difficulty": "medium", "tools_required": ["epoxy resin", "mixing cup", "brush", "clamps", "plastic sheeting"], "typical_errors": ["Uneven glue application", "Too much clamp pressure crushing wood", "Insufficient cure time before use"]}, {"method": "Caulked seams with marine sealant", "difficulty": "high", "tools_required": ["caulking gun", "caulk", "putty knife", "masking tape"], "typical_errors": ["Sealant not fully penetrating seams", "Caulk applied too thick or thin", "Poor surface preparation"]}], "failure_modes": [{"mode": "Surface checking and radial cracking", "onset_years": 3, "severity": "medium", "symptoms": "Small radial cracks visible in grain direction, typically on exposed surfaces", "prevention": "Regular oiling every 6 months, maintain consistent moisture levels, avoid rapid drying", "zone_risk": ["deck", "cockpit", "rails"]}, {"mode": "Rot initiation at fastener heads", "onset_years": 8, "severity": "high", "symptoms": "Dark staining around screw heads, soft wood when probed, potential water weeping", "prevention": "Use only stainless steel fasteners, seal screw holes, inspect every 12 months", "zone_risk": ["deck", "cockpit", "cabin_interior"]}, {"mode": "UV degradation and bleaching", "onset_years": 2, "severity": "low", "symptoms": "Honey color fades to gray or whitish tones, loss of luster", "prevention": "Apply UV-protective teak oil every 6 months, use protective covers when not in use", "zone_risk": ["deck", "cockpit", "exposed_rails"]}, {"mode": "Dimensional movement and shrinkage", "onset_years": 1, "severity": "medium", "symptoms": "Gaps opening between planks, fasteners loosening, caulking separation", "prevention": "Pre-seal all surfaces, use flexible sealants in seams, allow for wood movement in design", "zone_risk": ["deck", "cabin_interior"]}, {"mode": "Fungal staining (blue-black spots)", "onset_years": 0.5, "severity": "medium", "symptoms": "Dark spots or streaks appearing beneath varnish or in unfinished areas", "prevention": "Ensure good ventilation, maintain low humidity below 60%, treat with fungicide if detected", "zone_risk": ["cabin_interior", "head", "enclosed_areas"]}, {"mode": "Accelerated decay in protected crevices", "onset_years": 5, "severity": "high", "symptoms": "Soft, spongy wood in corners where moisture accumulates, potential structural weakness", "prevention": "Eliminate moisture traps, improve drainage, use stainless hardware with gaskets", "zone_risk": ["deck_seams", "cabin_joinery", "rail_mounts"]}], "water_ingress": {"risk_level": "medium", "mechanisms": ["Through cracks and checking", "At fastener penetrations", "Through open grain if unsealed", "At joint interfaces"], "prevention": "Seal all surfaces with teak oil or varnish, maintain intact finish, use stainless hardware with bedding compound", "inspection_interval_months": 6}, "wear_patterns": [{"location": "deck surface", "cause": "Foot traffic, weathering, UV degradation", "prevention": "Regular oiling, non-slip treatments where needed, frequent cleaning", "inspection_interval_months": 3}, {"location": "rail caps", "cause": "Hand wear, salt spray, sun exposure", "prevention": "Coat with protective varnish, maintain oiling schedule", "inspection_interval_months": 6}, {"location": "seam junctions", "cause": "Moisture penetration, fastener corrosion, wood movement", "prevention": "Re-caulk seams as needed, inspect fasteners annually", "inspection_interval_months": 12}], "environmental_limits": {"max_temp_c": 60, "min_temp_c": -5, "uv_resistance_hours": 2000, "salt_spray_resistance": "high", "humidity_tolerance": "40-70%"}, "galvanic_compatibility": {"compatible_with": ["stainless steel 316L", "bronze", "titanium", "coated fasteners"], "incompatible_with": ["mild steel", "galvanized steel without isolation", "aluminum without isolation", "copper directly"], "notes": "Always isolate different metals with gaskets and bedding compound. Do not use iron-based fasteners."}, "recommended_zones": ["deck", "cabin_interior", "cockpit", "rails", "trim", "rubbing_strakes"]},
        "known_issues": ["Can be expensive", "Requires regular oiling", "Splinter risk if not sealed"],
        "alternatives": ["Teak Plantation", "Iroko", "Accoya"],
    },
    {
        "name": "Teak Plantation",
        "category": "wood",
        "subcategory": "tropical_hardwood",
        "manufacturer": "Various",
        "cost_per_unit": 28.0,
        "cost_unit": "sqm",
        "lifespan_years": 15,
        "maintenance_interval_months": 12,
        "maintenance_cost_factor": 0.06,
        "properties": {"density_kg_m3": 580, "hardness_janka": 1000, "color": "lighter_brown", "uv_resistance": "medium_high", "water_resistance": "high", "grain": "less_consistent", "installation_methods": [{"method": "Fastened with stainless steel screws", "difficulty": "medium", "tools_required": ["cordless drill", "screwdriver bits", "clamps"], "typical_errors": ["Variable density causing fastener issues", "Grain tear-out in softer areas"]}, {"method": "Glued and fastened combination", "difficulty": "medium", "tools_required": ["epoxy", "clamps", "stainless screws"], "typical_errors": ["Adhesive squeeze-out staining wood", "Over-clamping softer material"]}], "failure_modes": [{"mode": "Inconsistent density causing fastener pull-through", "onset_years": 2, "severity": "medium", "symptoms": "Screws loosening, surface indentation around fasteners, potential fastener withdrawal", "prevention": "Pre-drill with pilot holes, use larger diameter fasteners, inspect and tighten every 12 months", "zone_risk": ["deck", "cabin_joinery"]}, {"mode": "Grain tear-out during cutting and machining", "onset_years": "immediate", "severity": "low", "symptoms": "Rough edges, fuzzy grain, cosmetic degradation", "prevention": "Use sharp tools, cut with grain direction, seal edges immediately after cutting", "zone_risk": ["any"]}, {"mode": "Color variation and fading", "onset_years": 1, "severity": "low", "symptoms": "Uneven color development, blotchy appearance, accelerated gray-ing compared to Burma grade", "prevention": "Apply stain if consistent color required, more frequent oiling schedule", "zone_risk": ["deck", "visible_surfaces"]}, {"mode": "Rot initiation in softer sections", "onset_years": 6, "severity": "high", "symptoms": "Soft spots in wood, dark staining, advanced decay in low-density areas", "prevention": "More frequent oiling (every 3-4 months), maintain ventilation, drain moisture promptly", "zone_risk": ["cabin_interior", "areas_under_stress"]}, {"mode": "Moisture absorption in exposed end grain", "onset_years": 0.5, "severity": "medium", "symptoms": "End grain darkening, moisture stains, swelling at edges", "prevention": "Seal all cut edges immediately, use end-grain sealer, avoid leaving cut surfaces exposed", "zone_risk": ["deck_edges", "planking_ends"]}, {"mode": "Accelerated degradation in low-ventilation areas", "onset_years": 3, "severity": "high", "symptoms": "Faster rot development than expected, fungal growth, musty odors", "prevention": "Ensure excellent ventilation in cabins, maintain humidity below 60%, inspect frequently", "zone_risk": ["cabin_interior", "lockers", "enclosed_spaces"]}], "water_ingress": {"risk_level": "medium-high", "mechanisms": ["Through end grain", "At fastener holes", "Through softer wood sections", "Capillary action"], "prevention": "Seal end grain and all cut surfaces, use epoxy around fasteners, maintain protective finish every 4 months", "inspection_interval_months": 3}, "wear_patterns": [{"location": "high-traffic deck areas", "cause": "Foot traffic on softer sections, accelerated wear", "prevention": "Apply non-slip coating, maintain finish regularly, consider wearing surface protection", "inspection_interval_months": 3}, {"location": "fastener areas", "cause": "Fastener loosening due to variable wood density", "prevention": "Use larger diameter fasteners, check tightness every 6 months", "inspection_interval_months": 6}], "environmental_limits": {"max_temp_c": 55, "min_temp_c": -2, "uv_resistance_hours": 1500, "salt_spray_resistance": "medium-high", "humidity_tolerance": "35-65%"}, "galvanic_compatibility": {"compatible_with": ["stainless steel 316L", "bronze", "titanium"], "incompatible_with": ["mild steel", "uncoated aluminum", "copper"]}, "recommended_zones": ["cabin_interior", "deck", "cockpit", "trim"]},
        "known_issues": ["Less dense than Burma teak", "Color more variable", "Requires more frequent oiling"],
        "alternatives": ["Teak Burma Grade A", "Accoya", "Iroko"],
    },
    {
        "name": "Iroko (African Teak)",
        "category": "wood",
        "subcategory": "tropical_hardwood",
        "manufacturer": "Various",
        "cost_per_unit": 32.0,
        "cost_unit": "sqm",
        "lifespan_years": 18,
        "maintenance_interval_months": 12,
        "maintenance_cost_factor": 0.06,
        "properties": {"density_kg_m3": 620, "hardness_janka": 1050, "color": "golden_yellow", "uv_resistance": "high", "water_resistance": "very_high", "teak_alternative": True, "installation_methods": [{"method": "Fastened with stainless steel screws and dowels", "difficulty": "high", "tools_required": ["high-speed drill", "carbide bits", "dowel jig", "safety equipment for silica dust"], "typical_errors": ["Rapid tool dulling", "Insufficient dust collection causing respiratory issues", "Bit breakage"]}, {"method": "Hand planed and fitted with epoxy", "difficulty": "high", "tools_required": ["sharp hand planes", "epoxy adhesive", "dust masks", "respiratory protection"], "typical_errors": ["Tool dulling, hand/respiratory irritation", "Over-sanding dust inhalation"]}], "failure_modes": [{"mode": "Respiratory irritation and allergic reaction to dust", "onset_years": "immediate", "severity": "medium", "symptoms": "Coughing, nasal irritation, allergic dermatitis, respiratory sensitivity over time", "prevention": "Use NIOSH N95 masks minimum, provide respiratory protection for workers, wet-sand when possible", "zone_risk": ["installation_areas"]}, {"mode": "Excessive tool wear from silica content", "onset_years": "immediate", "severity": "medium", "symptoms": "Rapid dulling of cutting tools, increased cutting resistance, poor surface finish", "prevention": "Use carbide tools, accept increased tool costs, maintain sharp tools", "zone_risk": ["construction"]}, {"mode": "Chemical sensitivity and toxic response", "onset_years": "variable", "severity": "high", "symptoms": "Skin irritation, eye redness, severe allergic reactions in sensitive individuals, systemic reactions", "prevention": "Screen for sensitization, provide proper PPE, maintain good ventilation, limit exposure", "zone_risk": ["installation_areas", "confined_spaces"]}, {"mode": "Dimensional instability during cure", "onset_years": 1, "severity": "medium", "symptoms": "Larger movement than teak, gap opening, fastener stress", "prevention": "Use larger sealant joints, plan for greater movement, monitor first season", "zone_risk": ["deck", "seams"]}, {"mode": "Checking and radial cracking (more pronounced than teak)", "onset_years": 2, "severity": "medium", "symptoms": "More pronounced and deeper cracks than equivalent teak", "prevention": "Seal early and frequently, control humidity and temperature swings", "zone_risk": ["deck", "exposed_surfaces"]}, {"mode": "Lower overall rot resistance than Burma teak", "onset_years": 7, "severity": "high", "symptoms": "Decay visible before pure teak would show problems", "prevention": "More frequent oiling, superior drainage design, good ventilation", "zone_risk": ["high_moisture_areas", "cabin_interior"]}], "water_ingress": {"risk_level": "medium", "mechanisms": ["Through checking", "At fasteners", "End grain absorption", "Joint interfaces"], "prevention": "Seal all surfaces regularly, use excellent drainage, epoxy-seal fastener holes", "inspection_interval_months": 4}, "wear_patterns": [{"location": "fastener holes", "cause": "Silica causes abrasion, fastener corrosion", "prevention": "Use epoxy bedding around fasteners, stainless hardware only", "inspection_interval_months": 6}, {"location": "tool contact areas", "cause": "Silica dust abrasion on contact surfaces", "prevention": "Smooth all surfaces, seal to prevent dust penetration", "inspection_interval_months": 12}], "environmental_limits": {"max_temp_c": 65, "min_temp_c": 0, "uv_resistance_hours": 2200, "salt_spray_resistance": "very high", "humidity_tolerance": "40-75%"}, "galvanic_compatibility": {"compatible_with": ["stainless steel 316L", "bronze", "titanium"], "incompatible_with": ["mild steel", "uncoated aluminum"], "notes": "Isolate all metals. Silica content accelerates corrosion in some metals."}, "recommended_zones": ["deck", "exposed_railings", "high_durability_areas"]},
        "known_issues": ["Contains silica; dulls tools quickly", "Wood dust can irritate skin", "May contain toxic compounds"],
        "alternatives": ["Teak Burma Grade A", "Teak Plantation", "Accoya"],
    },
    {
        "name": "Accoya (Modified Wood)",
        "category": "wood",
        "subcategory": "tropical_hardwood",
        "manufacturer": "Accsys",
        "cost_per_unit": 52.0,
        "cost_unit": "sqm",
        "lifespan_years": 50,
        "maintenance_interval_months": 24,
        "maintenance_cost_factor": 0.03,
        "properties": {"density_kg_m3": 640, "hardness_janka": 1200, "color": "warm_brown", "uv_resistance": "very_high", "water_resistance": "very_high", "acetylated": True, "dimensional_stability": "excellent", "installation_methods": [{"method": "Fastened with specialty stainless fasteners", "difficulty": "medium", "tools_required": ["cordless drill", "carbide-tipped bits", "pilot hole jig"], "typical_errors": ["Using standard fasteners (harder wood strips them)", "Over-drilling"]}, {"method": "Glued with epoxy adhesive", "difficulty": "medium", "tools_required": ["two-part epoxy", "mixing container", "brush", "clamps"], "typical_errors": ["Slow cure due to acetylation", "Uneven glue application"]}, {"method": "Mechanical fastening with roves and burrs", "difficulty": "medium", "tools_required": ["specialized fastening tools", "stainless hardware"], "typical_errors": ["Over-tightening against harder material", "Material splitting"]}], "failure_modes": [{"mode": "Dimensional stability excellent - minimal failure mode", "onset_years": 50, "severity": "very_low", "symptoms": "Minimal swelling/shrinking, joints remain tight", "prevention": "Standard maintenance; superior performance expected", "zone_risk": ["none"]}, {"mode": "Fastener stress concentration", "onset_years": 10, "severity": "low", "symptoms": "Fasteners may loosen due to harder wood; gaps do not develop as readily", "prevention": "Use larger diameter fasteners, check periodically", "zone_risk": ["fastened_areas"]}, {"mode": "Potential brittleness after 20+ years", "onset_years": 20, "severity": "medium", "symptoms": "Increased impact damage susceptibility, potential checking in thin sections", "prevention": "Maintain finish, avoid extreme temperature swings", "zone_risk": ["edges", "thin_sections"]}, {"mode": "Limited repair/replacement options", "onset_years": "varies", "severity": "low", "symptoms": "Accoya may no longer be available when repair needed", "prevention": "Document material specifications, plan for potential sourcing challenges", "zone_risk": ["any"]}, {"mode": "Color deepening over 10-15 years", "onset_years": 10, "severity": "low", "symptoms": "Warm brown color gradually darkens, may develop amber tones", "prevention": "Accept natural aging, apply UV-protective finishes if consistent color desired", "zone_risk": ["deck", "exposed_surfaces"]}, {"mode": "Surface checking in extreme conditions", "onset_years": 25, "severity": "low", "symptoms": "Fine surface cracks in high-sun exposure areas, much less severe than standard wood", "prevention": "Maintain finish, regular inspection", "zone_risk": ["south_facing_deck"]}], "water_ingress": {"risk_level": "low", "mechanisms": ["Through unsealed fastener holes", "At damaged finish areas"], "prevention": "Maintain intact finish, use bedding compound around fasteners, periodic resealing", "inspection_interval_months": 12}, "wear_patterns": [{"location": "surface areas", "cause": "Foot traffic, weather, lower wear rate than standard teak", "prevention": "Non-slip coating, regular finish maintenance", "inspection_interval_months": 6}], "environmental_limits": {"max_temp_c": 70, "min_temp_c": -10, "uv_resistance_hours": 3000, "salt_spray_resistance": "excellent", "humidity_tolerance": "25-85%"}, "galvanic_compatibility": {"compatible_with": ["stainless steel 316L", "bronze", "titanium", "epoxy-coated fasteners"], "incompatible_with": ["uncoated mild steel", "bare aluminum"], "notes": "Acetylation may alter galvanic behavior slightly; always isolate dissimilar metals."}, "recommended_zones": ["deck", "cabin_interior", "cockpit", "exposed_rails", "high_durability_zones", "long_life_applications"]},
        "known_issues": ["Premium cost", "Harder to find suppliers", "Requires specialty fasteners"],
        "alternatives": ["Teak Burma Grade A", "Iroko", "Teak Plantation"],
    },
    {
        "name": "Marine Sperrholz BS 1088",
        "category": "wood",
        "subcategory": "marine_plywood",
        "manufacturer": "Various",
        "cost_per_unit": 25.0,
        "cost_unit": "sqm",
        "lifespan_years": 15,
        "maintenance_interval_months": 18,
        "maintenance_cost_factor": 0.04,
        "properties": {"thickness_mm": [6, 9, 12, 18], "water_resistance": "very_high", "density_kg_m3": 580, "birch_veneer": True, "phenolic_glue": True, "installation_methods": [{"method": "Fastened with stainless steel screws", "difficulty": "easy", "tools_required": ["cordless drill", "screwdriver bits", "pilot hole bit"], "typical_errors": ["Screw over-tightening crushing core", "Inadequate edge sealing", "Fastener corrosion"]}, {"method": "Epoxy glued to substrate", "difficulty": "medium", "tools_required": ["epoxy resin", "brush", "clamps", "plastic sheeting for cleanup"], "typical_errors": ["Inadequate surface preparation", "Voids in adhesive layer", "Insufficient cure time"]}, {"method": "Sealed with penetrating epoxy", "difficulty": "medium", "tools_required": ["thin-film epoxy", "roller", "brush", "vacuum bag optional"], "typical_errors": ["Uneven penetration", "Missed edge areas", "Application too thick limiting penetration"]}], "failure_modes": [{"mode": "Delamination at surface plies", "onset_years": 3, "severity": "high", "symptoms": "Separation of veneer layers, bubbling, visible edge delamination", "prevention": "Seal all edges with epoxy, maintain waterproof finish, avoid fastener over-tightening", "zone_risk": ["any_area_with_poor_sealing"]}, {"mode": "Core rot from water ingress through fastener holes", "onset_years": 2, "severity": "high", "symptoms": "Soft spots, structural weakness, potential collapse under load", "prevention": "Seal every fastener hole with epoxy, use large washers, maintain surface finish", "zone_risk": ["high_fastener_density_areas"]}, {"mode": "Edge swelling and splintering", "onset_years": 0.5, "severity": "medium", "symptoms": "Exposed edges swell, splinter, fuzzy appearance", "prevention": "Seal edges immediately after cutting, use edge banding, protect during storage", "zone_risk": ["cut_edges", "panel_joints"]}, {"mode": "Glue-line failure allowing water penetration", "onset_years": 5, "severity": "high", "symptoms": "Plies separating, internal rot progression, structural failure", "prevention": "Use marine-grade epoxy adhesives only, ensure full contact during cure", "zone_risk": ["glued_joints", "interior_plies"]}, {"mode": "Fastener corrosion with water ingress", "onset_years": 1, "severity": "medium", "symptoms": "Staining around fasteners, potential structural weakness", "prevention": "Use only 316L stainless steel, apply epoxy bedding, maintain intact finish", "zone_risk": ["fastened_areas"]}, {"mode": "Uneven surface preparation preventing proper sealing", "onset_years": 1, "severity": "high", "symptoms": "Blotchy water absorption, uneven finish, failed waterproofing", "prevention": "Sand thoroughly before sealing, apply sanding sealer, ensure even surface", "zone_risk": ["any_area_with_poor_prep"]}], "water_ingress": {"risk_level": "high", "mechanisms": ["Through fastener holes", "At edge grain", "Through delamination", "Glue-line failure"], "prevention": "Seal all edges with epoxy, seal every fastener hole, maintain intact surface finish every 6 months", "inspection_interval_months": 3}, "wear_patterns": [{"location": "cut edges", "cause": "Water absorption, fiber exposure, swelling", "prevention": "Apply edge banding or epoxy seal immediately after cutting", "inspection_interval_months": 6}, {"location": "fastener areas", "cause": "Water entry through fastener holes, corrosion", "prevention": "Seal with epoxy, use large washers, maintain finish", "inspection_interval_months": 6}, {"location": "surface areas", "cause": "Traffic wear, UV degradation, moisture absorption", "prevention": "Apply protective topcoat, reseal annually", "inspection_interval_months": 6}], "environmental_limits": {"max_temp_c": 50, "min_temp_c": -5, "uv_resistance_hours": 1000, "salt_spray_resistance": "medium", "humidity_tolerance": "not_suitable_for_continuous_high_humidity"}, "galvanic_compatibility": {"compatible_with": ["stainless steel 316L", "bronze", "epoxy-coated fasteners"], "incompatible_with": ["mild steel fasteners", "uncoated aluminum", "copper"]}, "recommended_zones": ["cabin_interior_bulkheads", "sole_backing", "locker_linings", "non_critical_structural"]},
        "known_issues": ["Requires proper sealing", "Can delaminate if not protected", "Edge sealing is critical"],
        "alternatives": ["Mahagoni Sperrholz", "Zedernholz", "Accoya"],
    },
    {
        "name": "Mahagoni (Honduras Mahogany)",
        "category": "wood",
        "subcategory": "tropical_hardwood",
        "manufacturer": "Various",
        "cost_per_unit": 38.0,
        "cost_unit": "sqm",
        "lifespan_years": 18,
        "maintenance_interval_months": 12,
        "maintenance_cost_factor": 0.05,
        "properties": {"density_kg_m3": 580, "hardness_janka": 900, "color": "reddish_brown", "uv_resistance": "high", "water_resistance": "high", "traditional_boatbuilding": True, "installation_methods": [{"method": "Traditional fastening with screws and dowels", "difficulty": "medium", "tools_required": ["drill", "screwdriver bits", "dowel jig", "clamps"], "typical_errors": ["Splitting along grain", "Fastener pull-through in weak sections", "Tear-out"]}, {"method": "Mortise and tenon joinery with epoxy", "difficulty": "high", "tools_required": ["chisels", "mortise tools", "epoxy", "hand tools", "traditional equipment"], "typical_errors": ["Tight tolerances difficult due to quality variation", "Epoxy migration affecting stain"]}, {"method": "Surface veneering over plywood core", "difficulty": "medium", "tools_required": ["veneer hammer", "epoxy", "cauls", "veneer saw"], "typical_errors": ["Veneers bubbling", "Uneven glue application", "Grain pattern misalignment"]}], "failure_modes": [{"mode": "Quality variation within lumber", "onset_years": "immediate", "severity": "medium", "symptoms": "Varying density, color inconsistency, different working properties in same board", "prevention": "Source from reputable suppliers, accept some variation, plan for adjustment during installation", "zone_risk": ["any"]}, {"mode": "Periodic shortage and supply fluctuation", "onset_years": "variable", "severity": "medium", "symptoms": "Difficulty sourcing matching material for repairs, cost spikes", "prevention": "Purchase extra stock for repairs, establish supplier relationships, document specs", "zone_risk": ["any"]}, {"mode": "Pest damage (marine borers in tropical waters)", "onset_years": 1, "severity": "very_high", "symptoms": "Tiny exit holes, wood turning to powder, severe structural damage", "prevention": "Avoid in areas below waterline in tropical waters, use copperized finishes, maintain bottom paint", "zone_risk": ["hull_planking", "underwater_structures"]}, {"mode": "Fungal staining and rot initiation", "onset_years": 2, "severity": "high", "symptoms": "Black or dark green streaks, soft spots, musty odor", "prevention": "Maintain ventilation, keep humidity below 60%, treat with fungicide if detected", "zone_risk": ["cabin_interior", "enclosed_areas"]}, {"mode": "Dimensional movement and joint separation", "onset_years": 1, "severity": "medium", "symptoms": "Gaps opening in joinery, fasteners loosening, caulk separation", "prevention": "Pre-seal surfaces, use flexible sealants, allow for wood movement in design", "zone_risk": ["joinery", "seams"]}, {"mode": "Finish failure under salt spray", "onset_years": 2, "severity": "medium", "symptoms": "Varnish peeling, wood exposed to salt, accelerated degradation", "prevention": "Maintain finish diligently, use spar varnish, recoat every 12-18 months", "zone_risk": ["exterior_surfaces", "exposed_areas"]}], "water_ingress": {"risk_level": "medium", "mechanisms": ["Through varnish failure", "At fasteners", "Through exposed end grain", "At joint interfaces"], "prevention": "Maintain varnish finish, seal fastener holes, seal end grain, use epoxy at joints", "inspection_interval_months": 6}, "wear_patterns": [{"location": "high-traffic areas", "cause": "Foot traffic, surface wear, finish degradation", "prevention": "Apply durable topcoat, refinish as needed", "inspection_interval_months": 6}, {"location": "joint lines", "cause": "Dimensional movement, fastener stress", "prevention": "Re-caulk regularly, maintain flexible sealants", "inspection_interval_months": 12}], "environmental_limits": {"max_temp_c": 55, "min_temp_c": 5, "uv_resistance_hours": 1800, "salt_spray_resistance": "good", "humidity_tolerance": "45-65%"}, "galvanic_compatibility": {"compatible_with": ["stainless steel 316L", "bronze", "titanium"], "incompatible_with": ["mild steel without coating", "bare aluminum"], "notes": "Sourcing restrictions in some regions (CITES). Verify legal availability before specifying."}, "recommended_zones": ["cabin_interior_joinery", "trim_and_moldings", "decorative_elements", "high_visibility_areas"]},
        "known_issues": ["CITES restricted in some regions", "Cost fluctuates with supply", "Quality varies significantly"],
        "alternatives": ["Teak Burma Grade A", "Iroko", "Accoya"],
    },
    {
        "name": "Zedernholz (Western Red Cedar)",
        "category": "wood",
        "subcategory": "softwood",
        "manufacturer": "Various",
        "cost_per_unit": 18.0,
        "cost_unit": "sqm",
        "lifespan_years": 12,
        "maintenance_interval_months": 12,
        "maintenance_cost_factor": 0.07,
        "properties": {"density_kg_m3": 380, "hardness_janka": 350, "color": "reddish_brown", "uv_resistance": "medium", "water_resistance": "good", "lightweight": True, "natural_oils": True, "installation_methods": [{"method": "Fastened with stainless steel screws or copper rivets", "difficulty": "easy", "tools_required": ["cordless drill", "screwdriver bits", "rivet gun optional"], "typical_errors": ["Over-tightening fasteners in soft wood", "Fastener pull-through", "Surface crushing"]}, {"method": "Glued with epoxy or traditional casein glue", "difficulty": "medium", "tools_required": ["adhesive", "clamps", "brush"], "typical_errors": ["Over-clamping crushing soft wood", "Adhesive starvation in joints"]}, {"method": "Traditional clinker or carvel planking", "difficulty": "high", "tools_required": ["hand tools", "traditional shipwright skills"], "typical_errors": ["Inconsistent seam width", "Poor caulking", "Fastener placement errors"]}], "failure_modes": [{"mode": "Fastener pull-through due to soft wood", "onset_years": 0.5, "severity": "medium", "symptoms": "Screws sinking into wood, surface indentation, fastener backs visible", "prevention": "Use large diameter fasteners with large washers, use copper rivets for structural areas", "zone_risk": ["any_fastened_area"]}, {"mode": "Impact damage and denting", "onset_years": "immediate", "severity": "low", "symptoms": "Dings and dents from impacts, cosmetic damage", "prevention": "Protective rail padding, bumpers, careful handling", "zone_risk": ["rubbing_strakes", "impact_zones"]}, {"mode": "Rapid rot initiation in high-moisture areas", "onset_years": 1, "severity": "very_high", "symptoms": "Soft spots, structural weakness, rapid progression", "prevention": "Excellent drainage and ventilation critical, seal all surfaces, maintain low humidity", "zone_risk": ["cabin_interior", "areas_with_condensation", "enclosed_bilges"]}, {"mode": "Insect and marine borer attack", "onset_years": 1, "severity": "high", "symptoms": "Holes, tunnels, sawdust, structural damage", "prevention": "Use borate preservatives, maintain sound finish, avoid immersion in tropical waters", "zone_risk": ["underwater_areas", "warm_climates"]}, {"mode": "Dimensional movement in unstable environment", "onset_years": 0.5, "severity": "medium", "symptoms": "Large gaps developing in seams, fasteners loosening, caulk failures", "prevention": "Carefully seal surfaces, control cabin humidity, allow for larger wood movement than hardwoods", "zone_risk": ["any_area", "especially_seams"]}, {"mode": "Fungal decay in protected crevices", "onset_years": 2, "severity": "high", "symptoms": "Hidden rot in corners, potential structural failure, musty odors", "prevention": "Design to eliminate water traps, ensure ventilation, inspect regularly", "zone_risk": ["joinery", "corner_areas", "enclosed_spaces"]}], "water_ingress": {"risk_level": "high", "mechanisms": ["Through open grain", "At fasteners", "End grain absorption", "Capillary action"], "prevention": "Seal all surfaces thoroughly, maintain protective finish every 6 months, ensure good drainage", "inspection_interval_months": 3}, "wear_patterns": [{"location": "surface areas", "cause": "Foot traffic, weather exposure, UV damage, rapid fiber breakdown", "prevention": "Non-slip coating, frequent refinishing, protective covers", "inspection_interval_months": 3}, {"location": "fastener areas", "cause": "Soft wood, fastener loosening and pull-through", "prevention": "Use larger fasteners with washers, check every 6 months", "inspection_interval_months": 6}], "environmental_limits": {"max_temp_c": 45, "min_temp_c": -10, "uv_resistance_hours": 800, "salt_spray_resistance": "medium", "humidity_tolerance": "40-60%_critical"}, "galvanic_compatibility": {"compatible_with": ["stainless steel 316L", "bronze", "copper", "titanium", "coated fasteners"], "incompatible_with": ["mild steel without protection", "uncoated aluminum"], "notes": "Cedar naturally resists some corrosion, but always isolate dissimilar metals."}, "recommended_zones": ["cabin_interior", "non_structural_trim", "traditional_construction", "aesthetics_priority"]},
        "known_issues": ["Soft wood; susceptible to impact damage", "Requires more frequent maintenance", "Lower hardness rating"],
        "alternatives": ["Teak Plantation", "Accoya", "Marine Sperrholz"],
    },
    {
        "name": "Bamboo Marine (Engineered)",
        "category": "wood",
        "subcategory": "eco_friendly",
        "manufacturer": "Various",
        "cost_per_unit": 24.0,
        "cost_unit": "sqm",
        "lifespan_years": 14,
        "maintenance_interval_months": 12,
        "maintenance_cost_factor": 0.06,
        "properties": {"density_kg_m3": 640, "hardness_janka": 1180, "color": "light_tan", "uv_resistance": "medium", "water_resistance": "high", "sustainable": True, "fast_renewable": True, "installation_methods": [{"method": "Fastened with stainless steel hardware", "difficulty": "medium", "tools_required": ["cordless drill", "carbide bits", "stainless fasteners"], "typical_errors": ["Splitting along grain direction", "Fastener over-tightening"]}, {"method": "Glued with epoxy adhesive", "difficulty": "medium", "tools_required": ["two-part epoxy", "clamps", "brush"], "typical_errors": ["Uneven glue line", "Moisture affecting cure"]}, {"method": "Click-lock or tongue-and-groove systems", "difficulty": "easy", "tools_required": ["installation kit", "spacers", "mallet"], "typical_errors": ["Tight fitting causing buckling", "Humidity changes during installation"]}], "failure_modes": [{"mode": "Rapid UV degradation despite treatment", "onset_years": 1, "severity": "high", "symptoms": "Rapid graying, loss of color, accelerated failure of finish", "prevention": "Frequent recoating (every 3-4 months), UV-protective topcoat essential, protective covers", "zone_risk": ["deck", "exposed_surfaces", "cabin_exterior"]}, {"mode": "Moisture absorption and swelling", "onset_years": 0.5, "severity": "high", "symptoms": "Visible swelling, cupping, warping, seams separating", "prevention": "Seal all surfaces with waterproof coating, maintain humidity 40-60%, quick drainage", "zone_risk": ["high_moisture_areas", "deck", "cabin_interior"]}, {"mode": "Fungal growth despite treatment", "onset_years": 1, "severity": "medium", "symptoms": "Black mold, mildew, surface discoloration", "prevention": "Maintain excellent ventilation, keep humidity below 60%, anti-microbial topcoats", "zone_risk": ["interior_areas", "high_humidity_zones"]}, {"mode": "Delamination of engineered plies", "onset_years": 2, "severity": "high", "symptoms": "Layers separating, bubbling, surface peeling", "prevention": "Source from reputable manufacturers, maintain sealed finish, avoid standing water", "zone_risk": ["any_area"]}, {"mode": "Inconsistent supply and quality variation", "onset_years": "variable", "severity": "medium", "symptoms": "Difficulty sourcing matching material, quality inconsistency batch to batch", "prevention": "Purchase from established suppliers, order extra stock, document specifications", "zone_risk": ["any"]}, {"mode": "Long-term performance unknown", "onset_years": 5, "severity": "medium", "symptoms": "Unknown aging characteristics beyond 5-10 years, unexpected failures possible", "prevention": "Plan for possible replacement, maintain careful inspection schedule, document performance", "zone_risk": ["any_area"]}], "water_ingress": {"risk_level": "high", "mechanisms": ["Through bamboo fiber structure", "At fasteners", "Through delamination", "Capillary action"], "prevention": "Continuous protective coating, seal every fastener, maintain intact finish every 3 months", "inspection_interval_months": 2}, "wear_patterns": [{"location": "surface areas", "cause": "UV degradation, foot traffic, moisture absorption", "prevention": "Frequent recoating, non-slip treatment, protective covers in long-term storage", "inspection_interval_months": 3}, {"location": "joints and seams", "cause": "Moisture absorption causing swelling, fastener stress", "prevention": "Re-seal joints quarterly, maintain waterproof coating", "inspection_interval_months": 3}], "environmental_limits": {"max_temp_c": 50, "min_temp_c": 0, "uv_resistance_hours": 1000, "salt_spray_resistance": "medium", "humidity_tolerance": "40-60%_critical"}, "galvanic_compatibility": {"compatible_with": ["stainless steel 316L", "bronze", "titanium"], "incompatible_with": ["mild steel without coating", "bare aluminum"]}, "recommended_zones": ["cabin_interior_protected", "non_critical_areas", "environmental_consideration_important", "not_recommended_exterior"]},
        "known_issues": ["UV degradation can be rapid", "Supply chain variability", "Limited long-term marine data"],
        "alternatives": ["Teak Plantation", "Zedernholz", "Marine Sperrholz"],
    },
    {
        "name": "GFK/FRP Polyester Handlaminat",
        "category": "composite",
        "subcategory": "glass_fibre_reinforced",
        "manufacturer": "Various",
        "cost_per_unit": 12.0,
        "cost_unit": "sqm",
        "lifespan_years": 30,
        "maintenance_interval_months": 24,
        "maintenance_cost_factor": 0.03,
        "properties": {"density_kg_m3": 1800, "tensile_strength_mpa": 50, "water_absorption_pct": 1.5, "uv_resistance": "medium", "fiber_content_pct": 30, "installation_methods": [{"method": "Fastened with self-tapping stainless steel screws", "difficulty": "easy", "tools_required": ["cordless drill", "screw bits", "countersink drill bit"], "typical_errors": ["Over-tightening crushing composite", "Fastener pull-through", "Moisture intrusion"]}, {"method": "Glued with epoxy or polyester adhesive", "difficulty": "medium", "tools_required": ["adhesive", "application equipment", "clamps", "surface preparation tools"], "typical_errors": ["Inadequate surface preparation", "Adhesive starvation in joints", "Voids in bond line"]}, {"method": "Welded with heat-gun and filament", "difficulty": "high", "tools_required": ["heat gun", "welding rod (ABS or PVC)", "tools", "respiratory protection"], "typical_errors": ["Weak welds", "Heat damage to surrounding material", "Toxic fume exposure"]}], "failure_modes": [{"mode": "Osmotic blistering in gelcoat", "onset_years": 5, "severity": "high", "symptoms": "Visible blisters in gelcoat surface, water weeping from blisters, potential structural damage below", "prevention": "Use vinylester or epoxy matrix, maintain intact barrier coat, inspect annually", "zone_risk": ["hull_below_waterline", "immersed_areas"]}, {"mode": "Print-through and fiber show", "onset_years": 5, "severity": "medium", "symptoms": "Weave pattern visible through topcoat, aesthetic degradation, enhanced UV damage potential", "prevention": "Higher quality resin, thicker gelcoat, UV-protective topcoat, regular maintenance", "zone_risk": ["visible_surfaces"]}, {"mode": "Fiber-matrix separation (delamination)", "onset_years": 8, "severity": "high", "symptoms": "Hollow sound when tapped, visible separation, potential structural weakness", "prevention": "High quality resin and fabric, proper vacuum bagging, maintain waterproof finish", "zone_risk": ["structural_areas", "high_stress_zones"]}, {"mode": "Resin degradation under UV", "onset_years": 3, "severity": "medium", "symptoms": "Yellowing, chalking, loss of gloss, water absorption increase", "prevention": "UV-protective gelcoat, regular topcoat maintenance, protective covers", "zone_risk": ["exposed_surfaces"]}, {"mode": "Osmosis with inadequate barrier", "onset_years": 3, "severity": "very_high", "symptoms": "Progressive blistering and structural degradation, accelerated moisture ingress", "prevention": "Use epoxy or vinylester base, maintain paint barrier, inspect every 6 months", "zone_risk": ["underwater_areas"]}, {"mode": "Stress cracking at fastener holes", "onset_years": 2, "severity": "medium", "symptoms": "Radial cracks around fasteners, water entry pathway", "prevention": "Drill larger holes, use large stainless washers with gasket, apply sealant around fasteners", "zone_risk": ["fastener_areas"]}], "water_ingress": {"risk_level": "high", "mechanisms": ["Through osmotic blistering", "Around fasteners", "Through cracks", "At joints"], "prevention": "Quality resin system (avoid polyester for submerged), excellent barrier coat maintenance, frequent inspection", "inspection_interval_months": 6}, "wear_patterns": [{"location": "surface gelcoat", "cause": "UV degradation, foot traffic, salt spray", "prevention": "Regular washing, topcoat maintenance, protective covers", "inspection_interval_months": 6}, {"location": "fastener holes", "cause": "Stress concentration, water ingress, micro-cracking", "prevention": "Large washers, sealant bedding, inspect annually", "inspection_interval_months": 12}], "environmental_limits": {"max_temp_c": 60, "min_temp_c": -5, "uv_resistance_hours": 1500, "salt_spray_resistance": "poor", "humidity_tolerance": "not_suitable_below_waterline"}, "galvanic_compatibility": {"compatible_with": ["stainless steel 316L", "bronze", "titanium"], "incompatible_with": ["aluminum", "mild steel without protective coating"], "notes": "Ensure electrical isolation between metals to prevent galvanic corrosion in conductive matrix."}, "recommended_zones": ["cabin_interior_bulkheads", "deck_surfaces_above_waterline", "non_critical_cosmetic_areas"]},
        "known_issues": ["Can suffer from osmosis", "Print-through visible after 5-10 years", "Fiber-matrix separation possible"],
        "alternatives": ["GFK Vinylester", "GFK Vakuuminfusion", "Epoxy-GFK"],
    },
    {
        "name": "GFK Vinylester",
        "category": "composite",
        "subcategory": "glass_fibre_reinforced",
        "manufacturer": "Various",
        "cost_per_unit": 16.0,
        "cost_unit": "sqm",
        "lifespan_years": 35,
        "maintenance_interval_months": 24,
        "maintenance_cost_factor": 0.02,
        "properties": {"density_kg_m3": 1900, "tensile_strength_mpa": 70, "water_absorption_pct": 0.3, "uv_resistance": "high", "fiber_content_pct": 35, "osmosis_resistant": True, "installation_methods": [{"method": "Fastened with stainless steel screws and washers", "difficulty": "easy", "tools_required": ["drill", "screw bits", "quality washers"], "typical_errors": ["Fastener pull-through", "Over-tightening"]}, {"method": "Glued with epoxy adhesive (vinylester compatible)", "difficulty": "medium", "tools_required": ["epoxy", "clamps", "surface prep tools"], "typical_errors": ["Inadequate surface preparation", "Moisture on bonding surface"]}, {"method": "Thermal bonding in manufacturing", "difficulty": "high", "tools_required": ["heat source", "controlled temperature equipment"], "typical_errors": ["Thermal cycling stress", "Matrix degradation"]}], "failure_modes": [{"mode": "Superior osmosis resistance (major advantage)", "onset_years": 30, "severity": "very_low", "symptoms": "Minimal blistering compared to polyester, excellent long-term underwater performance", "prevention": "Standard maintenance; superior material property", "zone_risk": ["none"]}, {"mode": "Potential brittleness in cold environments", "onset_years": "immediate", "severity": "low", "symptoms": "Increased impact sensitivity in cold climates, potential cracking", "prevention": "Avoid high-impact zones in cold waters, design for flexibility", "zone_risk": ["northern_climates"]}, {"mode": "Fiber stress from resin shrinkage", "onset_years": 1, "severity": "low", "symptoms": "Micro-cracks, stress whitening, potential for accelerated failure", "prevention": "Proper manufacturing, controlled cure, design for stress relief", "zone_risk": ["any_area"]}, {"mode": "Cost premium impact on lifecycle planning", "onset_years": "planning_phase", "severity": "low", "symptoms": "Higher initial material cost, affects project budget", "prevention": "Justify premium with longevity, factor into lifecycle cost analysis", "zone_risk": ["any"]}, {"mode": "Matrix vulnerability at defects", "onset_years": 2, "severity": "medium", "symptoms": "Accelerated failure at voids or defects, water entry pathway", "prevention": "High-quality manufacturing, vacuum-assisted resin transfer molding, inspection", "zone_risk": ["manufacturing_defects"]}, {"mode": "UV degradation despite superior base resin", "onset_years": 5, "severity": "medium", "symptoms": "Gelcoat yellowing, surface chalking, degradation if not protected", "prevention": "UV-protective topcoat essential, regular maintenance", "zone_risk": ["exposed_surfaces"]}], "water_ingress": {"risk_level": "low", "mechanisms": ["Around fasteners", "Through cracks", "At joints"], "prevention": "Maintain topcoat, use quality fastener bedding, regular inspection", "inspection_interval_months": 12}, "wear_patterns": [{"location": "surface areas", "cause": "UV degradation, foot traffic, weather", "prevention": "Topcoat maintenance, protective covers", "inspection_interval_months": 6}], "environmental_limits": {"max_temp_c": 65, "min_temp_c": -10, "uv_resistance_hours": 2000, "salt_spray_resistance": "high", "humidity_tolerance": "excellent"}, "galvanic_compatibility": {"compatible_with": ["stainless steel 316L", "bronze", "titanium"], "incompatible_with": ["bare aluminum", "mild steel without coating"]}, "recommended_zones": ["hull_structure", "deck", "underwater_areas", "long_life_critical_areas"]},
        "known_issues": ["Higher cost than polyester", "Requires higher cure temperature", "VOC emissions during cure"],
        "alternatives": ["GFK Polyester Handlaminat", "GFK Vakuuminfusion", "Carbon-Infusion"],
    },
    {
        "name": "GFK Vakuuminfusion",
        "category": "composite",
        "subcategory": "glass_fibre_reinforced",
        "manufacturer": "Various",
        "cost_per_unit": 18.0,
        "cost_unit": "sqm",
        "lifespan_years": 35,
        "maintenance_interval_months": 24,
        "maintenance_cost_factor": 0.02,
        "properties": {"density_kg_m3": 1750, "tensile_strength_mpa": 80, "water_absorption_pct": 0.4, "uv_resistance": "high", "fiber_content_pct": 45, "void_content_pct": 2, "superior_strength": True, "installation_methods": [{"method": "Fastened with counter-sunk stainless steel fasteners", "difficulty": "easy", "tools_required": ["drill", "counter-sink bit", "stainless fasteners with washers"], "typical_errors": ["Fastener pull-through in high-void areas", "Over-tightening"]}, {"method": "Epoxy adhesive bonding", "difficulty": "medium", "tools_required": ["structural adhesive", "clamps", "vacuum bag optional"], "typical_errors": ["Inadequate surface prep", "Voids affecting bond quality"]}, {"method": "Welding (thermoplastic reinforced composites)", "difficulty": "high", "tools_required": ["heat source", "welding equipment", "specialized tools"], "typical_errors": ["Thermal damage", "Weak welds at high void content areas"]}], "failure_modes": [{"mode": "Superior strength and void content", "onset_years": 40, "severity": "very_low", "symptoms": "Excellent long-term structural performance, minimal void-related failures", "prevention": "Standard inspection; superior manufacturing provides advantages", "zone_risk": ["none"]}, {"mode": "Potential brittleness in extreme conditions", "onset_years": 20, "severity": "low", "symptoms": "Impact sensitivity in high-load conditions, potential catastrophic failure", "prevention": "Design for impact tolerance, protective covers in extreme conditions", "zone_risk": ["high_load_areas"]}, {"mode": "Fiber alignment stress", "onset_years": 1, "severity": "low", "symptoms": "Stress concentration at fiber boundaries, potential micro-cracking", "prevention": "Proper fiber orientation design, controlled manufacturing", "zone_risk": ["load_paths"]}, {"mode": "Void-related stress points", "onset_years": 5, "severity": "medium", "symptoms": "Accelerated failure at remaining voids (despite low void content), water ingress", "prevention": "Inspect for voids after manufacturing, seal any identified voids", "zone_risk": ["high_stress_areas"]}, {"mode": "Resin matrix degradation under extended UV", "onset_years": 5, "severity": "low", "symptoms": "Surface degradation, UV penetration causing internal damage", "prevention": "Protect with quality topcoat, regular maintenance", "zone_risk": ["exposed_surfaces"]}, {"mode": "Delamination at stress concentrations", "onset_years": 10, "severity": "medium", "symptoms": "Fiber-matrix separation at fastener holes or load concentrations", "prevention": "Large fastener washers, inspect high-stress areas annually", "zone_risk": ["fastener_areas", "load_paths"]}], "water_ingress": {"risk_level": "very_low", "mechanisms": ["Minimal voids mean fewer pathways", "Around fasteners", "Through cracks"], "prevention": "Excellent baseline properties; standard seal around fasteners sufficient", "inspection_interval_months": 12}, "wear_patterns": [{"location": "surface areas", "cause": "UV, traffic, salt spray", "prevention": "Topcoat maintenance, annual inspection", "inspection_interval_months": 12}], "environmental_limits": {"max_temp_c": 70, "min_temp_c": -15, "uv_resistance_hours": 2500, "salt_spray_resistance": "excellent", "humidity_tolerance": "excellent"}, "galvanic_compatibility": {"compatible_with": ["stainless steel 316L", "bronze", "titanium"], "incompatible_with": ["bare aluminum", "mild steel"]}, "recommended_zones": ["primary_structure", "hull", "high_load_areas", "long_life_applications", "critical_components"]},
        "known_issues": ["Complex process; operator-dependent results", "Equipment investment required", "Longer production time"],
        "alternatives": ["GFK Vinylester", "Carbon-Infusion", "GFK Polyester Handlaminat"],
    },
    {
        "name": "Carbon-Prepreg (Racing/Superyacht)",
        "category": "composite",
        "subcategory": "carbon_fibre",
        "manufacturer": "Various",
        "cost_per_unit": 85.0,
        "cost_unit": "sqm",
        "lifespan_years": 40,
        "maintenance_interval_months": 36,
        "maintenance_cost_factor": 0.01,
        "properties": {"density_kg_m3": 1600, "tensile_strength_mpa": 600, "modulus_gpa": 230, "fiber_content_pct": 60, "void_content_pct": 1, "lightweight": True, "highest_performance": True, "installation_methods": [{"method": "Autoclave curing with specialized layup", "difficulty": "very_high", "tools_required": ["autoclave", "vacuum bags", "specialized tools", "skilled technicians"], "typical_errors": ["Temperature/pressure control errors", "Delamination from improper vacuum", "Fiber waviness"]}, {"method": "Oven cure with controlled environment", "difficulty": "very_high", "tools_required": ["precision oven", "vacuum equipment", "specialized molds"], "typical_errors": ["Volatile off-gassing", "Cure profile errors", "Thermal stress"]}, {"method": "Fastened with titanium or specialty hardware", "difficulty": "high", "tools_required": ["drills with carbide bits", "titanium fasteners", "protective washers"], "typical_errors": ["Delamination around fasteners", "Over-tightening causing matrix damage"]}], "failure_modes": [{"mode": "Impact damage leading to delamination", "onset_years": 1, "severity": "very_high", "symptoms": "Invisible matrix cracking from impacts, sudden structural failure", "prevention": "Avoid impacts, protective bumpers, impact detection inspection, kevlar reinforcement in impact zones", "zone_risk": ["collision_zones", "fender_areas"]}, {"mode": "Galvanic corrosion with steel hardware", "onset_years": 1, "severity": "high", "symptoms": "Fiber/matrix degradation around fasteners, potential structural weakness", "prevention": "Use only titanium or specialty fasteners, isolate all metals with gaskets", "zone_risk": ["fastener_areas"]}, {"mode": "Moisture ingress in matrix cracks", "onset_years": 2, "severity": "high", "symptoms": "Progressive structural degradation, potential resin swelling and softening", "prevention": "Maintain perfect surface finish, inspect annually for damage, seal any cracks immediately", "zone_risk": ["any_crack_area"]}, {"mode": "Cure cycle sensitivity and variability", "onset_years": 1, "severity": "high", "symptoms": "Variability in properties between batches, potential structural weakness in weaker batches", "prevention": "Strict quality control, batch testing, certified manufacturers only", "zone_risk": ["any_area"]}, {"mode": "Brittle failure in cold temperatures", "onset_years": "immediate", "severity": "high", "symptoms": "Increased impact sensitivity in cold, potential catastrophic failure", "prevention": "Avoid racing/pushing limits in cold weather, kevlar reinforcement", "zone_risk": ["northern_climates"]}, {"mode": "UV degradation of exposed fibers", "onset_years": 2, "severity": "medium", "symptoms": "Fiber discoloration, potential strength loss, matrix degradation", "prevention": "Protective covering, UV-protective topcoat, avoid long-term exposure without cover", "zone_risk": ["exposed_surfaces"]}], "water_ingress": {"risk_level": "very_high_if_damaged", "mechanisms": ["Through impact cracks", "Capillary action at interfaces", "Delamination pathways"], "prevention": "Maintain perfect finish, inspect for ANY damage, repair immediately, protective covers during storage", "inspection_interval_months": 1}, "wear_patterns": [{"location": "fastener areas", "cause": "Galvanic action, stress concentration, matrix cracking", "prevention": "Titanium hardware only, large washers, inspect every inspection cycle", "inspection_interval_months": 1}, {"location": "edges and impact zones", "cause": "Impact damage, fiber exposure, moisture ingress", "prevention": "Protective bumpers, edge sealing, careful handling", "inspection_interval_months": 2}], "environmental_limits": {"max_temp_c": 80, "min_temp_c": -10, "uv_resistance_hours": 800, "salt_spray_resistance": "poor", "humidity_tolerance": "very_sensitive"}, "galvanic_compatibility": {"compatible_with": ["titanium", "specialty stainless (limited)", "epoxy-isolated hardware"], "incompatible_with": ["aluminum", "steel", "standard stainless without isolation"], "notes": "Use ONLY titanium fasteners. Any galvanic couple will cause rapid degradation."}, "recommended_zones": ["racing_applications", "superyacht_structures", "weight_critical_areas", "high_performance_racing"]},
        "known_issues": ["Extremely expensive", "Requires autoclave or oven", "Skilled labor intensive", "Galvanic corrosion risk"],
        "alternatives": ["Carbon-Infusion", "GFK Vakuuminfusion", "Aramid/Kevlar"],
    },
    {
        "name": "Carbon-Infusion",
        "category": "composite",
        "subcategory": "carbon_fibre",
        "manufacturer": "Various",
        "cost_per_unit": 55.0,
        "cost_unit": "sqm",
        "lifespan_years": 38,
        "maintenance_interval_months": 36,
        "maintenance_cost_factor": 0.01,
        "properties": {"density_kg_m3": 1580, "tensile_strength_mpa": 520, "modulus_gpa": 200, "fiber_content_pct": 50, "void_content_pct": 3, "lightweight": True, "semi_custom": True, "installation_methods": [{"method": "Vacuum infusion with specialized equipment", "difficulty": "high", "tools_required": ["vacuum pump", "infusion tubes", "molds", "specialized training"], "typical_errors": ["Resin starvation", "Air entrapment", "Uneven fiber saturation"]}, {"method": "Fastened with large stainless washers", "difficulty": "medium", "tools_required": ["drill", "carbide bits", "large stainless washers"], "typical_errors": ["Washer pull-through", "Micro-delamination at fastener"]}, {"method": "Bonded with structural adhesive", "difficulty": "high", "tools_required": ["structural epoxy", "vacuum bagging", "clamps"], "typical_errors": ["Void formation", "Inadequate bonding pressure"]}], "failure_modes": [{"mode": "Brittleness and impact sensitivity", "onset_years": "immediate", "severity": "very_high", "symptoms": "Catastrophic failure from minor impacts, no warning before failure", "prevention": "Avoid impact zones, use aramid/kevlar reinforcement in vulnerable areas, protective covers", "zone_risk": ["collision_areas", "fender_locations"]}, {"mode": "Micro-cracking from impact or vibration", "onset_years": 1, "severity": "high", "symptoms": "Invisible internal cracking, eventual water ingress and structural failure", "prevention": "Minimize vibration, avoid impacts, protective impact zones with hybrid reinforcement", "zone_risk": ["high_vibration_areas", "impact_zones"]}, {"mode": "Galvanic corrosion with inappropriate metals", "onset_years": 0.5, "severity": "very_high", "symptoms": "Rapid fiber degradation at fastener areas, structural weakness", "prevention": "Stainless steel 316L ONLY, titanium preferred, isolation gaskets mandatory", "zone_risk": ["fastener_areas"]}, {"mode": "Matrix resin degradation from moisture", "onset_years": 2, "severity": "high", "symptoms": "Resin softening, loss of structural properties, catastrophic failure potential", "prevention": "Maintain pristine finish, inspect for ANY damage, seal immediately", "zone_risk": ["immersed_areas"]}, {"mode": "Fiber waviness from infusion process", "onset_years": 1, "severity": "high", "symptoms": "Reduced strength in load paths, stress concentration", "prevention": "Quality control on manufacturing, batch testing", "zone_risk": ["load-bearing_areas"]}, {"mode": "Void content affecting strength", "onset_years": 1, "severity": "medium", "symptoms": "Lower than expected properties, accelerated failure at void locations", "prevention": "Proper vacuum infusion technique, quality control, testing", "zone_risk": ["any_area"]}], "water_ingress": {"risk_level": "very_high_if_damaged", "mechanisms": ["Through micro-cracks", "Matrix saturation and swelling", "Capillary action"], "prevention": "Pristine finish mandatory, any damage means immediate repair, protective storage covers", "inspection_interval_months": 2}, "wear_patterns": [{"location": "fastener areas", "cause": "Galvanic corrosion, micro-cracking, stress concentration", "prevention": "Large stainless washers, periodic inspection, rapid damage repair", "inspection_interval_months": 3}, {"location": "edges and corners", "cause": "Impact damage, fiber exposure, rapid water ingress", "prevention": "Protective bumpers, edge sealing, impact avoidance", "inspection_interval_months": 3}], "environmental_limits": {"max_temp_c": 75, "min_temp_c": -5, "uv_resistance_hours": 600, "salt_spray_resistance": "very_poor", "humidity_tolerance": "very_poor"}, "galvanic_compatibility": {"compatible_with": ["stainless steel 316L", "titanium"], "incompatible_with": ["all other metals without isolation"], "notes": "Use ONLY stainless 316L or titanium. Isolate with gaskets. Carbon fiber is highly galvanic."}, "recommended_zones": ["protected_structures", "race_boats", "weight-critical_non_impact_areas"]},
        "known_issues": ["Brittle; impact-prone", "Galvanic corrosion with metals", "Repair challenging"],
        "alternatives": ["Carbon-Prepreg", "Aramid/Kevlar", "GFK Vakuuminfusion"],
    },
    {
        "name": "Aramid/Kevlar (Impact Zones)",
        "category": "composite",
        "subcategory": "aramid_fibre",
        "manufacturer": "DuPont",
        "cost_per_unit": 48.0,
        "cost_unit": "sqm",
        "lifespan_years": 35,
        "maintenance_interval_months": 24,
        "maintenance_cost_factor": 0.02,
        "properties": {"density_kg_m3": 1450, "tensile_strength_mpa": 480, "modulus_gpa": 125, "impact_resistance": "excellent", "fiber_content_pct": 45, "lightweight": True, "energy_absorption": True, "installation_methods": [{"method": "Woven into laminate with glass or carbon", "difficulty": "high", "tools_required": ["manufacturing equipment", "specialized training"], "typical_errors": ["Improper fiber weaving", "Uneven saturation"]}, {"method": "Fastened with stainless steel hardware", "difficulty": "medium", "tools_required": ["drill", "bits", "stainless fasteners with washers"], "typical_errors": ["Over-tightening crushing aramid", "Fastener pull-through"]}, {"method": "Bonded with structural adhesive", "difficulty": "medium", "tools_required": ["epoxy adhesive", "clamps", "surface prep tools"], "typical_errors": ["Inadequate surface preparation", "Air bubbles in adhesive"]}], "failure_modes": [{"mode": "UV degradation and fiber weakening", "onset_years": 1, "severity": "very_high", "symptoms": "Rapid loss of impact resistance, color fading to white, potential structural failure", "prevention": "UV-protective topcoat ESSENTIAL, cover when not in use, recoat every 6 months", "zone_risk": ["any_exposed_area"]}, {"mode": "Moisture absorption affecting properties", "onset_years": 0.5, "severity": "high", "symptoms": "Swelling, matrix softening, loss of impact resistance", "prevention": "Maintain waterproof finish, inspect for damage, control humidity", "zone_risk": ["high_moisture_areas"]}, {"mode": "Limited supplier availability", "onset_years": "immediate", "severity": "medium", "symptoms": "Difficulty sourcing for repairs, availability gaps", "prevention": "Establish supplier relationships, plan ahead for repairs", "zone_risk": ["any"]}, {"mode": "Hygroscopic behavior", "onset_years": 0.5, "severity": "high", "symptoms": "Water absorption into fibers, dimensional changes, property loss", "prevention": "Waterproof topcoat mandatory, seal all edges, maintain below 70% humidity", "zone_risk": ["high_humidity_environments"]}, {"mode": "Impact damage progression", "onset_years": 1, "severity": "high", "symptoms": "After impact, accelerated water ingress and degradation", "prevention": "Immediate repair after any impact, protect with covers", "zone_risk": ["impact_zones"]}, {"mode": "Fiber debonding from matrix", "onset_years": 3, "severity": "high", "symptoms": "Fibers separating from resin, potential delamination", "prevention": "Maintain finish integrity, inspect for early signs, seal any exposed fibers", "zone_risk": ["edges", "damaged_areas"]}], "water_ingress": {"risk_level": "high", "mechanisms": ["Through UV-degraded areas", "Fiber capillary action", "At defects"], "prevention": "Superior UV protection, frequent recoating, perfect damage control", "inspection_interval_months": 3}, "wear_patterns": [{"location": "UV-exposed surfaces", "cause": "Rapid UV fiber degradation, fiber whitening", "prevention": "Topcoat every 6 months, protective covers, minimize storage exposure", "inspection_interval_months": 3}, {"location": "fastener areas", "cause": "Galvanic action, micro-cracking from fastener stress", "prevention": "Large washers, stainless only, inspect regularly", "inspection_interval_months": 6}], "environmental_limits": {"max_temp_c": 60, "min_temp_c": -5, "uv_resistance_hours": 500, "salt_spray_resistance": "poor", "humidity_tolerance": "poor"}, "galvanic_compatibility": {"compatible_with": ["stainless steel 316L", "titanium"], "incompatible_with": ["most other metals without isolation"], "notes": "Isolate all metals. Aramid fiber initiates corrosion in incompatible metals."}, "recommended_zones": ["impact_zones", "fender_areas", "rubbing_strakes", "collision_protection_areas"]},
        "known_issues": ["UV degradation; requires UV-resistant topcoat", "Moisture sensitive", "Higher cost"],
        "alternatives": ["Carbon-Infusion", "Aramid-Glass hybrid", "GFK Vakuuminfusion"],
    },
    {
        "name": "Glasfaser-Epoxid (Glass-Epoxy Premium)",
        "category": "composite",
        "subcategory": "glass_fibre_reinforced",
        "manufacturer": "Various",
        "cost_per_unit": 22.0,
        "cost_unit": "sqm",
        "lifespan_years": 37,
        "maintenance_interval_months": 24,
        "maintenance_cost_factor": 0.02,
        "properties": {"density_kg_m3": 1850, "tensile_strength_mpa": 90, "water_absorption_pct": 0.1, "uv_resistance": "very_high", "fiber_content_pct": 40, "epoxy_matrix": True, "superior_adhesion": True, "installation_methods": [{"method": "Fastened with stainless steel screws", "difficulty": "easy", "tools_required": ["drill", "screw bits", "washers"], "typical_errors": ["Fastener pull-through", "Over-tightening"]}, {"method": "Epoxy bonded to substrate", "difficulty": "medium", "tools_required": ["epoxy adhesive", "surface prep tools", "clamps"], "typical_errors": ["Moisture on bonding surface", "Inadequate curing"]}, {"method": "Laminated with epoxy resin", "difficulty": "high", "tools_required": ["epoxy resin", "vacuum bag", "molds", "controlled cure"], "typical_errors": ["Exothermic reaction runaway", "Void formation"]}], "failure_modes": [{"mode": "Exothermic reaction during cure (well-controlled)", "onset_years": "manufacturing", "severity": "medium", "symptoms": "Uneven cure, potential matrix degradation in thick sections", "prevention": "Proper cure schedule, controlled temperature, careful epoxy system selection", "zone_risk": ["manufacturing_phase"]}, {"mode": "Superior water resistance (major advantage)", "onset_years": 40, "severity": "very_low", "symptoms": "Minimal water absorption, excellent long-term properties", "prevention": "Standard maintenance sufficient", "zone_risk": ["none"]}, {"mode": "Potential brittleness in cold", "onset_years": "immediate", "severity": "low", "symptoms": "Increased impact sensitivity in cold temperatures", "prevention": "Avoid extreme impacts in cold, design for flexibility", "zone_risk": ["northern_climates"]}, {"mode": "UV-induced epoxy yellowing", "onset_years": 3, "severity": "low", "symptoms": "Yellowing of matrix, potential strength loss", "prevention": "UV-protective topcoat, protective covers", "zone_risk": ["exposed_surfaces"]}, {"mode": "Adhesive layer stress in bonded repairs", "onset_years": 5, "severity": "medium", "symptoms": "Repair failure under stress, adhesive line opening", "prevention": "Quality epoxy systems, proper surface prep, monitor repairs", "zone_risk": ["repair_areas"]}, {"mode": "Higher cost than polyester", "onset_years": "planning", "severity": "low", "symptoms": "Budget constraints may limit use", "prevention": "Justify with longevity, lifecycle cost analysis", "zone_risk": ["any"]}], "water_ingress": {"risk_level": "low", "mechanisms": ["Minimal water absorption inherent to material", "Around fasteners", "At joints"], "prevention": "Maintain finish, standard fastener sealing", "inspection_interval_months": 12}, "wear_patterns": [{"location": "surface areas", "cause": "UV exposure, traffic, environmental weathering", "prevention": "Protective topcoat, regular maintenance", "inspection_interval_months": 12}], "environmental_limits": {"max_temp_c": 80, "min_temp_c": -15, "uv_resistance_hours": 2500, "salt_spray_resistance": "excellent", "humidity_tolerance": "excellent"}, "galvanic_compatibility": {"compatible_with": ["stainless steel 316L", "bronze", "titanium"], "incompatible_with": ["bare aluminum", "mild steel without coating"]}, "recommended_zones": ["marine_applications", "underwater_structures", "long_life_critical", "naval_vessels", "premium_vessels"]},
        "known_issues": ["Higher cost than polyester", "Requires controlled cure", "Exothermic reaction risk"],
        "alternatives": ["GFK Vinylester", "GFK Vakuuminfusion", "Carbon-Infusion"],
    },
    {
        "name": "Basaltfaser (Basalt Fibre Eco)",
        "category": "composite",
        "subcategory": "natural_fibre",
        "manufacturer": "Various",
        "cost_per_unit": 20.0,
        "cost_unit": "sqm",
        "lifespan_years": 32,
        "maintenance_interval_months": 24,
        "maintenance_cost_factor": 0.03,
        "properties": {"density_kg_m3": 1900, "tensile_strength_mpa": 85, "water_absorption_pct": 0.5, "uv_resistance": "high", "fiber_content_pct": 40, "eco_friendly": True, "volcanic_origin": True, "installation_methods": [{"method": "Fastened with stainless steel hardware", "difficulty": "easy", "tools_required": ["drill", "fasteners", "washers"], "typical_errors": ["Fastener pull-through", "Inadequate washers"]}, {"method": "Glued with epoxy adhesive", "difficulty": "medium", "tools_required": ["epoxy", "clamps", "surface prep"], "typical_errors": ["Insufficient cure time", "Uneven bond line"]}, {"method": "Laminated in manufacturing", "difficulty": "high", "tools_required": ["resin system", "molds", "vacuum equipment"], "typical_errors": ["Uneven fiber saturation", "Air entrapment"]}], "failure_modes": [{"mode": "Limited long-term performance data", "onset_years": 5, "severity": "high", "symptoms": "Unknown aging characteristics, unexpected failures possible", "prevention": "Careful monitoring, plan for possible replacement, establish inspection schedule", "zone_risk": ["any"]}, {"mode": "Supply chain limitations", "onset_years": "variable", "severity": "medium", "symptoms": "Difficulty sourcing, availability gaps, quality inconsistency", "prevention": "Establish supplier relationships, stock extra material for repairs", "zone_risk": ["any"]}, {"mode": "Fiber orientation variability", "onset_years": 1, "severity": "medium", "symptoms": "Variable properties depending on fiber alignment", "prevention": "Specify fiber orientation, quality control during manufacturing", "zone_risk": ["any"]}, {"mode": "Cost premium for eco-credentials", "onset_years": "planning", "severity": "low", "symptoms": "Higher cost than conventional alternatives", "prevention": "Justify environmental benefits in project", "zone_risk": ["any"]}, {"mode": "Potential moisture absorption", "onset_years": 2, "severity": "medium", "symptoms": "Slight water absorption, potential property loss", "prevention": "Seal surfaces, maintain waterproof coating", "zone_risk": ["high_moisture_areas"]}, {"mode": "Volcanic fiber reactivity", "onset_years": 5, "severity": "low", "symptoms": "Potential alkali-silica reaction in certain environments", "prevention": "Select appropriate resin systems, avoid reactive environments", "zone_risk": ["fresh_water_immersion"]}], "water_ingress": {"risk_level": "medium", "mechanisms": ["Through unsealed areas", "At fasteners", "Capillary action"], "prevention": "Maintain finish integrity, seal fastener areas, regular inspection", "inspection_interval_months": 6}, "wear_patterns": [{"location": "surface areas", "cause": "Traffic, weather, UV exposure", "prevention": "Protective topcoat, regular maintenance", "inspection_interval_months": 6}], "environmental_limits": {"max_temp_c": 65, "min_temp_c": -10, "uv_resistance_hours": 1800, "salt_spray_resistance": "good", "humidity_tolerance": "good"}, "galvanic_compatibility": {"compatible_with": ["stainless steel 316L", "bronze", "titanium"], "incompatible_with": ["bare aluminum", "mild steel"]}, "recommended_zones": ["eco_conscious_projects", "non_critical_structures", "interior_applications", "where_cost_justified"]},
        "known_issues": ["Limited supplier base", "Long-term data still developing", "Cost premium vs GFK"],
        "alternatives": ["GFK Polyester Handlaminat", "GFK Vinylester", "Natural fiber composites"],
    },
    {
        "name": "Edelstahl 316L",
        "category": "metal",
        "subcategory": "stainless_steel",
        "manufacturer": "Various",
        "cost_per_unit": 18.0,
        "cost_unit": "kg",
        "lifespan_years": 25,
        "maintenance_interval_months": 6,
        "maintenance_cost_factor": 0.02,
        "properties": {"density_kg_m3": 8000, "tensile_strength_mpa": 485, "corrosion_resistance": "excellent", "magnetic": False, "molybdenum_content": True, "lower_carbon": True, "installation_methods": [{"method": "WIG/TIG-Schweißen", "difficulty": "high", "tools_required": ["WIG-Schweißgerät", "Schutzgas", "Schweißdraht", "Schleifmaschine"], "typical_errors": ["Porosität durch fehlenden Gasschutz", "Verzug durch zu hohe Hitze", "Unvollständige Durchschweißung"]}, {"method": "Verschraubt mit Isolierung", "difficulty": "medium", "tools_required": ["Edelstahlschrauben", "Isolierscheiben", "Drehmomentschlüssel"], "typical_errors": ["Galvanische Korrosion ohne Isolierung", "Zu hohes Drehmoment"]}, {"method": "Genietet mit Moneldorn", "difficulty": "medium", "tools_required": ["Nietenzange", "Monelnieten", "Bohrer"], "typical_errors": ["Falsches Nietenmaterial", "Bohrung zu groß"]}], "failure_modes": [{"mode": "Spaltkorrosion", "onset_years": 3, "severity": "high", "symptoms": "Rostflecken in Spalten, unter Dichtungen, an Überlappungen", "prevention": "Spalte eliminieren oder versiegeln, 316L verwenden", "zone_risk": ["deck", "rigging", "hull_fittings"]}, {"mode": "Galvanische Korrosion", "onset_years": 2, "severity": "critical", "symptoms": "Beschleunigter Materialabbau am unedleren Metall", "prevention": "Gleichartige Metalle, Isolierung, Opferanoden", "zone_risk": ["hull_below_waterline", "through_hulls", "propeller"]}, {"mode": "Spannungsrisskorrosion", "onset_years": 5, "severity": "critical", "symptoms": "Haarrisse unter Belastung, plötzliches Versagen", "prevention": "Spannungsarm glühen, richtige Legierung wählen", "zone_risk": ["rigging", "chainplates", "keel_bolts"]}, {"mode": "Ermüdungsbruch", "onset_years": 10, "severity": "critical", "symptoms": "Rissbildung an Schweißnähten und Biegungen", "prevention": "Fachgerechte Schweißung, Radien an Ecken, regelmäßige Inspektion", "zone_risk": ["rigging", "stanchions", "pulpit"]}, {"mode": "Lochfraß (Pitting)", "onset_years": 4, "severity": "medium", "symptoms": "Kleine tiefe Löcher in der Oberfläche", "prevention": "316L statt 304, Oberfläche passivieren", "zone_risk": ["deck", "hull_fittings", "through_hulls"]}], "water_ingress": {"risk_level": "low", "mechanisms": ["Durchrostung bei unlegiertem Stahl", "Lochfraß bei Edelstahl 304", "Korrosion an Schweißnähten"], "prevention": "Richtige Legierung (316L für Salzwasser), Schweißnähte beizen und passivieren", "inspection_interval_months": 12}, "wear_patterns": [{"location": "Winschen und Umlenkrollen", "cause": "Schoten und Fallen unter Last", "prevention": "Regelmäßig schmieren, Selbstwendewinschen warten", "inspection_interval_months": 6}, {"location": "Klampen und Poller", "cause": "Festmacherleinen unter Zug", "prevention": "Klampen mit genügend Radius, Leinenführung prüfen", "inspection_interval_months": 12}, {"location": "Relingstützen", "cause": "Seitliche Belastung, Fender", "prevention": "Fußplatten regelmäßig auf Risse prüfen", "inspection_interval_months": 12}], "environmental_limits": {"max_temp_c": 300, "min_temp_c": -60, "uv_resistance_hours": 50000, "salt_spray_resistance": "high_316L_medium_304", "humidity_tolerance": "bis 100%"}, "galvanic_compatibility": {"compatible_with": ["edelstahl_316", "titan", "monel"], "incompatible_with": ["aluminium", "zink_nahe_edelstahl", "kupfer_nahe_aluminium"], "notes": "Galvanische Reihe beachten — Potentialdifferenz unter 0.25V halten"}, "recommended_zones": ["rigging", "deck_hardware", "stanchions", "hull_fittings", "through_hulls", "keel_bolts"]},
        "known_issues": ["Crevice corrosion possible in harsh salt water", "Galvanic corrosion with other metals", "Galling risk"],
        "alternatives": ["Edelstahl 304", "Titan Grade 2", "Bronze"],
    },
    {
        "name": "Edelstahl 304",
        "category": "metal",
        "subcategory": "stainless_steel",
        "manufacturer": "Various",
        "cost_per_unit": 13.0,
        "cost_unit": "kg",
        "lifespan_years": 15,
        "maintenance_interval_months": 6,
        "maintenance_cost_factor": 0.03,
        "properties": {"density_kg_m3": 8000, "tensile_strength_mpa": 505, "corrosion_resistance": "good", "magnetic": False, "lower_molybdenum": True, "cheaper": True, "installation_methods": [{"method": "WIG/TIG-Schweißen", "difficulty": "high", "tools_required": ["WIG-Schweißgerät", "Schutzgas", "Schweißdraht", "Schleifmaschine"], "typical_errors": ["Porosität durch fehlenden Gasschutz", "Verzug durch zu hohe Hitze", "Unvollständige Durchschweißung"]}, {"method": "Verschraubt mit Isolierung", "difficulty": "medium", "tools_required": ["Edelstahlschrauben", "Isolierscheiben", "Drehmomentschlüssel"], "typical_errors": ["Galvanische Korrosion ohne Isolierung", "Zu hohes Drehmoment"]}, {"method": "Genietet mit Moneldorn", "difficulty": "medium", "tools_required": ["Nietenzange", "Monelnieten", "Bohrer"], "typical_errors": ["Falsches Nietenmaterial", "Bohrung zu groß"]}], "failure_modes": [{"mode": "Spaltkorrosion", "onset_years": 3, "severity": "high", "symptoms": "Rostflecken in Spalten, unter Dichtungen, an Überlappungen", "prevention": "Spalte eliminieren oder versiegeln, 316L verwenden", "zone_risk": ["deck", "rigging", "hull_fittings"]}, {"mode": "Galvanische Korrosion", "onset_years": 2, "severity": "critical", "symptoms": "Beschleunigter Materialabbau am unedleren Metall", "prevention": "Gleichartige Metalle, Isolierung, Opferanoden", "zone_risk": ["hull_below_waterline", "through_hulls", "propeller"]}, {"mode": "Spannungsrisskorrosion", "onset_years": 5, "severity": "critical", "symptoms": "Haarrisse unter Belastung, plötzliches Versagen", "prevention": "Spannungsarm glühen, richtige Legierung wählen", "zone_risk": ["rigging", "chainplates", "keel_bolts"]}, {"mode": "Ermüdungsbruch", "onset_years": 10, "severity": "critical", "symptoms": "Rissbildung an Schweißnähten und Biegungen", "prevention": "Fachgerechte Schweißung, Radien an Ecken, regelmäßige Inspektion", "zone_risk": ["rigging", "stanchions", "pulpit"]}, {"mode": "Lochfraß (Pitting)", "onset_years": 4, "severity": "medium", "symptoms": "Kleine tiefe Löcher in der Oberfläche", "prevention": "316L statt 304, Oberfläche passivieren", "zone_risk": ["deck", "hull_fittings", "through_hulls"]}], "water_ingress": {"risk_level": "low", "mechanisms": ["Durchrostung bei unlegiertem Stahl", "Lochfraß bei Edelstahl 304", "Korrosion an Schweißnähten"], "prevention": "Richtige Legierung (316L für Salzwasser), Schweißnähte beizen und passivieren", "inspection_interval_months": 12}, "wear_patterns": [{"location": "Winschen und Umlenkrollen", "cause": "Schoten und Fallen unter Last", "prevention": "Regelmäßig schmieren, Selbstwendewinschen warten", "inspection_interval_months": 6}, {"location": "Klampen und Poller", "cause": "Festmacherleinen unter Zug", "prevention": "Klampen mit genügend Radius, Leinenführung prüfen", "inspection_interval_months": 12}, {"location": "Relingstützen", "cause": "Seitliche Belastung, Fender", "prevention": "Fußplatten regelmäßig auf Risse prüfen", "inspection_interval_months": 12}], "environmental_limits": {"max_temp_c": 300, "min_temp_c": -60, "uv_resistance_hours": 50000, "salt_spray_resistance": "high_316L_medium_304", "humidity_tolerance": "bis 100%"}, "galvanic_compatibility": {"compatible_with": ["edelstahl_316", "titan", "monel"], "incompatible_with": ["aluminium", "zink_nahe_edelstahl", "kupfer_nahe_aluminium"], "notes": "Galvanische Reihe beachten — Potentialdifferenz unter 0.25V halten"}, "recommended_zones": ["rigging", "deck_hardware", "stanchions", "hull_fittings", "through_hulls", "keel_bolts"]},
        "known_issues": ["NOT suitable for saltwater immersion", "Pitting corrosion in high-chloride environments", "Limited lifespan offshore"],
        "alternatives": ["Edelstahl 316L", "Titan Grade 2", "Bronze"],
    },
    {
        "name": "Aluminium 5083",
        "category": "metal",
        "subcategory": "aluminium_alloy",
        "manufacturer": "Various",
        "cost_per_unit": 8.5,
        "cost_unit": "kg",
        "lifespan_years": 20,
        "maintenance_interval_months": 12,
        "maintenance_cost_factor": 0.02,
        "properties": {"density_kg_m3": 2650, "tensile_strength_mpa": 215, "corrosion_resistance": "excellent", "weldable": True, "magnesium_content": True, "marine_grade": True, "installation_methods": [{"method": "WIG/TIG-Schweißen", "difficulty": "high", "tools_required": ["WIG-Schweißgerät", "Schutzgas", "Schweißdraht", "Schleifmaschine"], "typical_errors": ["Porosität durch fehlenden Gasschutz", "Verzug durch zu hohe Hitze", "Unvollständige Durchschweißung"]}, {"method": "Verschraubt mit Isolierung", "difficulty": "medium", "tools_required": ["Edelstahlschrauben", "Isolierscheiben", "Drehmomentschlüssel"], "typical_errors": ["Galvanische Korrosion ohne Isolierung", "Zu hohes Drehmoment"]}, {"method": "Genietet mit Moneldorn", "difficulty": "medium", "tools_required": ["Nietenzange", "Monelnieten", "Bohrer"], "typical_errors": ["Falsches Nietenmaterial", "Bohrung zu groß"]}], "failure_modes": [{"mode": "Spaltkorrosion", "onset_years": 3, "severity": "high", "symptoms": "Rostflecken in Spalten, unter Dichtungen, an Überlappungen", "prevention": "Spalte eliminieren oder versiegeln, 316L verwenden", "zone_risk": ["deck", "rigging", "hull_fittings"]}, {"mode": "Galvanische Korrosion", "onset_years": 2, "severity": "critical", "symptoms": "Beschleunigter Materialabbau am unedleren Metall", "prevention": "Gleichartige Metalle, Isolierung, Opferanoden", "zone_risk": ["hull_below_waterline", "through_hulls", "propeller"]}, {"mode": "Spannungsrisskorrosion", "onset_years": 5, "severity": "critical", "symptoms": "Haarrisse unter Belastung, plötzliches Versagen", "prevention": "Spannungsarm glühen, richtige Legierung wählen", "zone_risk": ["rigging", "chainplates", "keel_bolts"]}, {"mode": "Ermüdungsbruch", "onset_years": 10, "severity": "critical", "symptoms": "Rissbildung an Schweißnähten und Biegungen", "prevention": "Fachgerechte Schweißung, Radien an Ecken, regelmäßige Inspektion", "zone_risk": ["rigging", "stanchions", "pulpit"]}, {"mode": "Lochfraß (Pitting)", "onset_years": 4, "severity": "medium", "symptoms": "Kleine tiefe Löcher in der Oberfläche", "prevention": "316L statt 304, Oberfläche passivieren", "zone_risk": ["deck", "hull_fittings", "through_hulls"]}], "water_ingress": {"risk_level": "low", "mechanisms": ["Durchrostung bei unlegiertem Stahl", "Lochfraß bei Edelstahl 304", "Korrosion an Schweißnähten"], "prevention": "Richtige Legierung (316L für Salzwasser), Schweißnähte beizen und passivieren", "inspection_interval_months": 12}, "wear_patterns": [{"location": "Winschen und Umlenkrollen", "cause": "Schoten und Fallen unter Last", "prevention": "Regelmäßig schmieren, Selbstwendewinschen warten", "inspection_interval_months": 6}, {"location": "Klampen und Poller", "cause": "Festmacherleinen unter Zug", "prevention": "Klampen mit genügend Radius, Leinenführung prüfen", "inspection_interval_months": 12}, {"location": "Relingstützen", "cause": "Seitliche Belastung, Fender", "prevention": "Fußplatten regelmäßig auf Risse prüfen", "inspection_interval_months": 12}], "environmental_limits": {"max_temp_c": 300, "min_temp_c": -60, "uv_resistance_hours": 50000, "salt_spray_resistance": "high_316L_medium_304", "humidity_tolerance": "bis 100%"}, "galvanic_compatibility": {"compatible_with": ["edelstahl_316", "titan", "monel"], "incompatible_with": ["aluminium", "zink_nahe_edelstahl", "kupfer_nahe_aluminium"], "notes": "Galvanische Reihe beachten — Potentialdifferenz unter 0.25V halten"}, "recommended_zones": ["rigging", "deck_hardware", "stanchions", "hull_fittings", "through_hulls", "keel_bolts"]},
        "known_issues": ["Galvanic corrosion with other metals; requires isolation", "Requires anodizing for durability", "Difficult to repair"],
        "alternatives": ["Aluminium 6082-T6", "Edelstahl 316L", "Titan Grade 2"],
    },
    {
        "name": "Aluminium 6082-T6",
        "category": "metal",
        "subcategory": "aluminium_alloy",
        "manufacturer": "Various",
        "cost_per_unit": 9.5,
        "cost_unit": "kg",
        "lifespan_years": 18,
        "maintenance_interval_months": 12,
        "maintenance_cost_factor": 0.02,
        "properties": {"density_kg_m3": 2700, "tensile_strength_mpa": 310, "corrosion_resistance": "good", "strength": "high", "heat_treated": True, "structural_applications": True, "installation_methods": [{"method": "WIG/TIG-Schweißen", "difficulty": "high", "tools_required": ["WIG-Schweißgerät", "Schutzgas", "Schweißdraht", "Schleifmaschine"], "typical_errors": ["Porosität durch fehlenden Gasschutz", "Verzug durch zu hohe Hitze", "Unvollständige Durchschweißung"]}, {"method": "Verschraubt mit Isolierung", "difficulty": "medium", "tools_required": ["Edelstahlschrauben", "Isolierscheiben", "Drehmomentschlüssel"], "typical_errors": ["Galvanische Korrosion ohne Isolierung", "Zu hohes Drehmoment"]}, {"method": "Genietet mit Moneldorn", "difficulty": "medium", "tools_required": ["Nietenzange", "Monelnieten", "Bohrer"], "typical_errors": ["Falsches Nietenmaterial", "Bohrung zu groß"]}], "failure_modes": [{"mode": "Spaltkorrosion", "onset_years": 3, "severity": "high", "symptoms": "Rostflecken in Spalten, unter Dichtungen, an Überlappungen", "prevention": "Spalte eliminieren oder versiegeln, 316L verwenden", "zone_risk": ["deck", "rigging", "hull_fittings"]}, {"mode": "Galvanische Korrosion", "onset_years": 2, "severity": "critical", "symptoms": "Beschleunigter Materialabbau am unedleren Metall", "prevention": "Gleichartige Metalle, Isolierung, Opferanoden", "zone_risk": ["hull_below_waterline", "through_hulls", "propeller"]}, {"mode": "Spannungsrisskorrosion", "onset_years": 5, "severity": "critical", "symptoms": "Haarrisse unter Belastung, plötzliches Versagen", "prevention": "Spannungsarm glühen, richtige Legierung wählen", "zone_risk": ["rigging", "chainplates", "keel_bolts"]}, {"mode": "Ermüdungsbruch", "onset_years": 10, "severity": "critical", "symptoms": "Rissbildung an Schweißnähten und Biegungen", "prevention": "Fachgerechte Schweißung, Radien an Ecken, regelmäßige Inspektion", "zone_risk": ["rigging", "stanchions", "pulpit"]}, {"mode": "Lochfraß (Pitting)", "onset_years": 4, "severity": "medium", "symptoms": "Kleine tiefe Löcher in der Oberfläche", "prevention": "316L statt 304, Oberfläche passivieren", "zone_risk": ["deck", "hull_fittings", "through_hulls"]}], "water_ingress": {"risk_level": "low", "mechanisms": ["Durchrostung bei unlegiertem Stahl", "Lochfraß bei Edelstahl 304", "Korrosion an Schweißnähten"], "prevention": "Richtige Legierung (316L für Salzwasser), Schweißnähte beizen und passivieren", "inspection_interval_months": 12}, "wear_patterns": [{"location": "Winschen und Umlenkrollen", "cause": "Schoten und Fallen unter Last", "prevention": "Regelmäßig schmieren, Selbstwendewinschen warten", "inspection_interval_months": 6}, {"location": "Klampen und Poller", "cause": "Festmacherleinen unter Zug", "prevention": "Klampen mit genügend Radius, Leinenführung prüfen", "inspection_interval_months": 12}, {"location": "Relingstützen", "cause": "Seitliche Belastung, Fender", "prevention": "Fußplatten regelmäßig auf Risse prüfen", "inspection_interval_months": 12}], "environmental_limits": {"max_temp_c": 300, "min_temp_c": -60, "uv_resistance_hours": 50000, "salt_spray_resistance": "high_316L_medium_304", "humidity_tolerance": "bis 100%"}, "galvanic_compatibility": {"compatible_with": ["edelstahl_316", "titan", "monel"], "incompatible_with": ["aluminium", "zink_nahe_edelstahl", "kupfer_nahe_aluminium"], "notes": "Galvanische Reihe beachten — Potentialdifferenz unter 0.25V halten"}, "recommended_zones": ["rigging", "deck_hardware", "stanchions", "hull_fittings", "through_hulls", "keel_bolts"]},
        "known_issues": ["Heat-treat sensitive; risk of losing properties", "Galvanic corrosion risk", "Requires protective coatings"],
        "alternatives": ["Aluminium 5083", "Edelstahl 316L", "Titan Grade 2"],
    },
    {
        "name": "Bronze (Cu-Sn Alloy)",
        "category": "metal",
        "subcategory": "copper_alloy",
        "manufacturer": "Various",
        "cost_per_unit": 22.0,
        "cost_unit": "kg",
        "lifespan_years": 30,
        "maintenance_interval_months": 12,
        "maintenance_cost_factor": 0.03,
        "properties": {"density_kg_m3": 8700, "tensile_strength_mpa": 350, "corrosion_resistance": "excellent", "self_healing_patina": True, "traditional": True, "through_hull_fittings": True, "installation_methods": [{"method": "WIG/TIG-Schweißen", "difficulty": "high", "tools_required": ["WIG-Schweißgerät", "Schutzgas", "Schweißdraht", "Schleifmaschine"], "typical_errors": ["Porosität durch fehlenden Gasschutz", "Verzug durch zu hohe Hitze", "Unvollständige Durchschweißung"]}, {"method": "Verschraubt mit Isolierung", "difficulty": "medium", "tools_required": ["Edelstahlschrauben", "Isolierscheiben", "Drehmomentschlüssel"], "typical_errors": ["Galvanische Korrosion ohne Isolierung", "Zu hohes Drehmoment"]}, {"method": "Genietet mit Moneldorn", "difficulty": "medium", "tools_required": ["Nietenzange", "Monelnieten", "Bohrer"], "typical_errors": ["Falsches Nietenmaterial", "Bohrung zu groß"]}], "failure_modes": [{"mode": "Spaltkorrosion", "onset_years": 3, "severity": "high", "symptoms": "Rostflecken in Spalten, unter Dichtungen, an Überlappungen", "prevention": "Spalte eliminieren oder versiegeln, 316L verwenden", "zone_risk": ["deck", "rigging", "hull_fittings"]}, {"mode": "Galvanische Korrosion", "onset_years": 2, "severity": "critical", "symptoms": "Beschleunigter Materialabbau am unedleren Metall", "prevention": "Gleichartige Metalle, Isolierung, Opferanoden", "zone_risk": ["hull_below_waterline", "through_hulls", "propeller"]}, {"mode": "Spannungsrisskorrosion", "onset_years": 5, "severity": "critical", "symptoms": "Haarrisse unter Belastung, plötzliches Versagen", "prevention": "Spannungsarm glühen, richtige Legierung wählen", "zone_risk": ["rigging", "chainplates", "keel_bolts"]}, {"mode": "Ermüdungsbruch", "onset_years": 10, "severity": "critical", "symptoms": "Rissbildung an Schweißnähten und Biegungen", "prevention": "Fachgerechte Schweißung, Radien an Ecken, regelmäßige Inspektion", "zone_risk": ["rigging", "stanchions", "pulpit"]}, {"mode": "Lochfraß (Pitting)", "onset_years": 4, "severity": "medium", "symptoms": "Kleine tiefe Löcher in der Oberfläche", "prevention": "316L statt 304, Oberfläche passivieren", "zone_risk": ["deck", "hull_fittings", "through_hulls"]}], "water_ingress": {"risk_level": "low", "mechanisms": ["Durchrostung bei unlegiertem Stahl", "Lochfraß bei Edelstahl 304", "Korrosion an Schweißnähten"], "prevention": "Richtige Legierung (316L für Salzwasser), Schweißnähte beizen und passivieren", "inspection_interval_months": 12}, "wear_patterns": [{"location": "Winschen und Umlenkrollen", "cause": "Schoten und Fallen unter Last", "prevention": "Regelmäßig schmieren, Selbstwendewinschen warten", "inspection_interval_months": 6}, {"location": "Klampen und Poller", "cause": "Festmacherleinen unter Zug", "prevention": "Klampen mit genügend Radius, Leinenführung prüfen", "inspection_interval_months": 12}, {"location": "Relingstützen", "cause": "Seitliche Belastung, Fender", "prevention": "Fußplatten regelmäßig auf Risse prüfen", "inspection_interval_months": 12}], "environmental_limits": {"max_temp_c": 300, "min_temp_c": -60, "uv_resistance_hours": 50000, "salt_spray_resistance": "high_316L_medium_304", "humidity_tolerance": "bis 100%"}, "galvanic_compatibility": {"compatible_with": ["edelstahl_316", "titan", "monel"], "incompatible_with": ["aluminium", "zink_nahe_edelstahl", "kupfer_nahe_aluminium"], "notes": "Galvanische Reihe beachten — Potentialdifferenz unter 0.25V halten"}, "recommended_zones": ["rigging", "deck_hardware", "stanchions", "hull_fittings", "through_hulls", "keel_bolts"]},
        "known_issues": ["Dezincification risk in some alloys", "Expensive", "Heavy compared to stainless"],
        "alternatives": ["Edelstahl 316L", "Tin-bronze", "Nitronic 60"],
    },
    {
        "name": "Titan Grade 2",
        "category": "metal",
        "subcategory": "titanium",
        "manufacturer": "Various",
        "cost_per_unit": 45.0,
        "cost_unit": "kg",
        "lifespan_years": 50,
        "maintenance_interval_months": 24,
        "maintenance_cost_factor": 0.01,
        "properties": {"density_kg_m3": 4510, "tensile_strength_mpa": 345, "corrosion_resistance": "exceptional", "lightweight": True, "biocompatible": True, "premium_hardware": True, "installation_methods": [{"method": "WIG/TIG-Schweißen", "difficulty": "high", "tools_required": ["WIG-Schweißgerät", "Schutzgas", "Schweißdraht", "Schleifmaschine"], "typical_errors": ["Porosität durch fehlenden Gasschutz", "Verzug durch zu hohe Hitze", "Unvollständige Durchschweißung"]}, {"method": "Verschraubt mit Isolierung", "difficulty": "medium", "tools_required": ["Edelstahlschrauben", "Isolierscheiben", "Drehmomentschlüssel"], "typical_errors": ["Galvanische Korrosion ohne Isolierung", "Zu hohes Drehmoment"]}, {"method": "Genietet mit Moneldorn", "difficulty": "medium", "tools_required": ["Nietenzange", "Monelnieten", "Bohrer"], "typical_errors": ["Falsches Nietenmaterial", "Bohrung zu groß"]}], "failure_modes": [{"mode": "Spaltkorrosion", "onset_years": 3, "severity": "high", "symptoms": "Rostflecken in Spalten, unter Dichtungen, an Überlappungen", "prevention": "Spalte eliminieren oder versiegeln, 316L verwenden", "zone_risk": ["deck", "rigging", "hull_fittings"]}, {"mode": "Galvanische Korrosion", "onset_years": 2, "severity": "critical", "symptoms": "Beschleunigter Materialabbau am unedleren Metall", "prevention": "Gleichartige Metalle, Isolierung, Opferanoden", "zone_risk": ["hull_below_waterline", "through_hulls", "propeller"]}, {"mode": "Spannungsrisskorrosion", "onset_years": 5, "severity": "critical", "symptoms": "Haarrisse unter Belastung, plötzliches Versagen", "prevention": "Spannungsarm glühen, richtige Legierung wählen", "zone_risk": ["rigging", "chainplates", "keel_bolts"]}, {"mode": "Ermüdungsbruch", "onset_years": 10, "severity": "critical", "symptoms": "Rissbildung an Schweißnähten und Biegungen", "prevention": "Fachgerechte Schweißung, Radien an Ecken, regelmäßige Inspektion", "zone_risk": ["rigging", "stanchions", "pulpit"]}, {"mode": "Lochfraß (Pitting)", "onset_years": 4, "severity": "medium", "symptoms": "Kleine tiefe Löcher in der Oberfläche", "prevention": "316L statt 304, Oberfläche passivieren", "zone_risk": ["deck", "hull_fittings", "through_hulls"]}], "water_ingress": {"risk_level": "low", "mechanisms": ["Durchrostung bei unlegiertem Stahl", "Lochfraß bei Edelstahl 304", "Korrosion an Schweißnähten"], "prevention": "Richtige Legierung (316L für Salzwasser), Schweißnähte beizen und passivieren", "inspection_interval_months": 12}, "wear_patterns": [{"location": "Winschen und Umlenkrollen", "cause": "Schoten und Fallen unter Last", "prevention": "Regelmäßig schmieren, Selbstwendewinschen warten", "inspection_interval_months": 6}, {"location": "Klampen und Poller", "cause": "Festmacherleinen unter Zug", "prevention": "Klampen mit genügend Radius, Leinenführung prüfen", "inspection_interval_months": 12}, {"location": "Relingstützen", "cause": "Seitliche Belastung, Fender", "prevention": "Fußplatten regelmäßig auf Risse prüfen", "inspection_interval_months": 12}], "environmental_limits": {"max_temp_c": 300, "min_temp_c": -60, "uv_resistance_hours": 50000, "salt_spray_resistance": "high_316L_medium_304", "humidity_tolerance": "bis 100%"}, "galvanic_compatibility": {"compatible_with": ["edelstahl_316", "titan", "monel"], "incompatible_with": ["aluminium", "zink_nahe_edelstahl", "kupfer_nahe_aluminium"], "notes": "Galvanische Reihe beachten — Potentialdifferenz unter 0.25V halten"}, "recommended_zones": ["rigging", "deck_hardware", "stanchions", "hull_fittings", "through_hulls", "keel_bolts"]},
        "known_issues": ["Extreme cost", "Difficult to machine", "Limited supplier base", "Overkill for most applications"],
        "alternatives": ["Edelstahl 316L", "Bronze", "Nitronic 60"],
    },
    {
        "name": "Divinycell H80 (PVC-Schaum)",
        "category": "core",
        "subcategory": "closed_cell_foam",
        "manufacturer": "DIAB",
        "cost_per_unit": 8.0,
        "cost_unit": "sqm",
        "lifespan_years": 20,
        "maintenance_interval_months": 12,
        "maintenance_cost_factor": 0.01,
        "properties": {"density_kg_m3": 80, "water_absorption_pct": 0.5, "thermal_insulation": "good", "fire_rating": "IMO", "compression_strength_kpa": 450, "shear_strength_kpa": 350, "installation_methods": [{"method": "Einlaminiert im Sandwichverfahren", "difficulty": "high", "tools_required": ["Kernmaterial", "Harz", "Glasfaser", "Vakuumanlage"], "typical_errors": ["Lufteinschlüsse zwischen Kern und Laminat", "Kernmaterial verschoben", "Ungleichmäßige Harzverteilung"]}, {"method": "Verklebt mit Strukturkleber", "difficulty": "medium", "tools_required": ["Thixotropierter Kleber", "Spachtel", "Klemmen"], "typical_errors": ["Zu dünne Klebeschicht", "Kern nicht entfettet"]}], "failure_modes": [{"mode": "Wasseraufnahme im Kern", "onset_years": 5, "severity": "critical", "symptoms": "Gewichtszunahme, weiche Stellen beim Klopfen, Blasen im Laminat", "prevention": "Schnittkanten versiegeln, Bohrungen abdichten, Drainage vorsehen", "zone_risk": ["deck", "cabin_top", "hull_sandwich"]}, {"mode": "Schubversagen zwischen Kern und Laminat", "onset_years": 10, "severity": "critical", "symptoms": "Deckoberfläche gibt nach, Laminat löst sich vom Kern", "prevention": "Ausreichende Harzschicht, Kerbschnitte im Kern für Harzbrücken", "zone_risk": ["deck", "hull"]}, {"mode": "Kernfäulnis bei Balsaholz", "onset_years": 6, "severity": "critical", "symptoms": "Weiche Bereiche, Verfärbung, moderner Geruch beim Öffnen", "prevention": "PVC- oder PET-Schaum statt Balsa in Feuchtzonen", "zone_risk": ["deck", "transom", "rudder"]}, {"mode": "Druckversagen unter Punktlasten", "onset_years": 0, "severity": "high", "symptoms": "Eindrücke in Deckoberfläche, Deformation", "prevention": "Lokale Verstärkungen unter Beschlägen, höhere Kerndichte wählen", "zone_risk": ["deck_hardware", "mast_step"]}], "water_ingress": {"risk_level": "high", "mechanisms": ["Kapillarwirkung an Schnittkanten", "Bohrungen für Beschläge", "Mikrorisse im Laminat", "Osmose durch Außenhaut"], "prevention": "Alle Bohrungen überdimensioniert bohren, mit Epoxy füllen, dann auf Maß nachbohren", "inspection_interval_months": 12}, "wear_patterns": [{"location": "Unter Decksbeschlägen", "cause": "Punktlasten und Vibration", "prevention": "Verdicktes Laminat oder Aluminium-Lastverteilplatten", "inspection_interval_months": 12}], "environmental_limits": {"max_temp_c": 65, "min_temp_c": -40, "uv_resistance_hours": 0, "salt_spray_resistance": "depends_on_outer_laminate", "humidity_tolerance": "Kern muss vollständig eingekapselt sein"}, "galvanic_compatibility": {"compatible_with": ["alle_nichtmetallischen"], "incompatible_with": [], "notes": "Kernmaterialien sind nicht leitfähig, aber Wasseraufnahme kann Elektrolyt bilden"}, "recommended_zones": ["deck_sandwich", "hull_sandwich", "cabin_top", "structural_bulkheads"]},
        "known_issues": ["Can degrade from prolonged UV exposure", "Moisture can enter through damage", "Limited repair options"],
        "alternatives": ["Balsa-Kern", "SAN-Schaum", "PET-Schaum"],
    },
    {
        "name": "Balsa-Kern (Balsa Core)",
        "category": "core",
        "subcategory": "wood_core",
        "manufacturer": "Various",
        "cost_per_unit": 6.5,
        "cost_unit": "sqm",
        "lifespan_years": 18,
        "maintenance_interval_months": 18,
        "maintenance_cost_factor": 0.03,
        "properties": {"density_kg_m3": 140, "water_absorption_pct": 3.0, "thermal_insulation": "excellent", "compression_strength_kpa": 550, "lightweight": True, "natural": True, "installation_methods": [{"method": "Einlaminiert im Sandwichverfahren", "difficulty": "high", "tools_required": ["Kernmaterial", "Harz", "Glasfaser", "Vakuumanlage"], "typical_errors": ["Lufteinschlüsse zwischen Kern und Laminat", "Kernmaterial verschoben", "Ungleichmäßige Harzverteilung"]}, {"method": "Verklebt mit Strukturkleber", "difficulty": "medium", "tools_required": ["Thixotropierter Kleber", "Spachtel", "Klemmen"], "typical_errors": ["Zu dünne Klebeschicht", "Kern nicht entfettet"]}], "failure_modes": [{"mode": "Wasseraufnahme im Kern", "onset_years": 5, "severity": "critical", "symptoms": "Gewichtszunahme, weiche Stellen beim Klopfen, Blasen im Laminat", "prevention": "Schnittkanten versiegeln, Bohrungen abdichten, Drainage vorsehen", "zone_risk": ["deck", "cabin_top", "hull_sandwich"]}, {"mode": "Schubversagen zwischen Kern und Laminat", "onset_years": 10, "severity": "critical", "symptoms": "Deckoberfläche gibt nach, Laminat löst sich vom Kern", "prevention": "Ausreichende Harzschicht, Kerbschnitte im Kern für Harzbrücken", "zone_risk": ["deck", "hull"]}, {"mode": "Kernfäulnis bei Balsaholz", "onset_years": 6, "severity": "critical", "symptoms": "Weiche Bereiche, Verfärbung, moderner Geruch beim Öffnen", "prevention": "PVC- oder PET-Schaum statt Balsa in Feuchtzonen", "zone_risk": ["deck", "transom", "rudder"]}, {"mode": "Druckversagen unter Punktlasten", "onset_years": 0, "severity": "high", "symptoms": "Eindrücke in Deckoberfläche, Deformation", "prevention": "Lokale Verstärkungen unter Beschlägen, höhere Kerndichte wählen", "zone_risk": ["deck_hardware", "mast_step"]}], "water_ingress": {"risk_level": "high", "mechanisms": ["Kapillarwirkung an Schnittkanten", "Bohrungen für Beschläge", "Mikrorisse im Laminat", "Osmose durch Außenhaut"], "prevention": "Alle Bohrungen überdimensioniert bohren, mit Epoxy füllen, dann auf Maß nachbohren", "inspection_interval_months": 12}, "wear_patterns": [{"location": "Unter Decksbeschlägen", "cause": "Punktlasten und Vibration", "prevention": "Verdicktes Laminat oder Aluminium-Lastverteilplatten", "inspection_interval_months": 12}], "environmental_limits": {"max_temp_c": 65, "min_temp_c": -40, "uv_resistance_hours": 0, "salt_spray_resistance": "depends_on_outer_laminate", "humidity_tolerance": "Kern muss vollständig eingekapselt sein"}, "galvanic_compatibility": {"compatible_with": ["alle_nichtmetallischen"], "incompatible_with": [], "notes": "Kernmaterialien sind nicht leitfähig, aber Wasseraufnahme kann Elektrolyt bilden"}, "recommended_zones": ["deck_sandwich", "hull_sandwich", "cabin_top", "structural_bulkheads"]},
        "known_issues": ["Water absorption if not sealed", "Susceptible to rot if damaged", "Can compress under load"],
        "alternatives": ["Divinycell H80", "SAN-Schaum", "PET-Schaum"],
    },
    {
        "name": "SAN-Schaum (Corecell)",
        "category": "core",
        "subcategory": "closed_cell_foam",
        "manufacturer": "Corecell",
        "cost_per_unit": 11.0,
        "cost_unit": "sqm",
        "lifespan_years": 22,
        "maintenance_interval_months": 18,
        "maintenance_cost_factor": 0.02,
        "properties": {"density_kg_m3": 110, "water_absorption_pct": 0.3, "compression_strength_kpa": 650, "shear_strength_kpa": 520, "tougher_than_pvc": True, "higher_stiffness": True, "installation_methods": [{"method": "Einlaminiert im Sandwichverfahren", "difficulty": "high", "tools_required": ["Kernmaterial", "Harz", "Glasfaser", "Vakuumanlage"], "typical_errors": ["Lufteinschlüsse zwischen Kern und Laminat", "Kernmaterial verschoben", "Ungleichmäßige Harzverteilung"]}, {"method": "Verklebt mit Strukturkleber", "difficulty": "medium", "tools_required": ["Thixotropierter Kleber", "Spachtel", "Klemmen"], "typical_errors": ["Zu dünne Klebeschicht", "Kern nicht entfettet"]}], "failure_modes": [{"mode": "Wasseraufnahme im Kern", "onset_years": 5, "severity": "critical", "symptoms": "Gewichtszunahme, weiche Stellen beim Klopfen, Blasen im Laminat", "prevention": "Schnittkanten versiegeln, Bohrungen abdichten, Drainage vorsehen", "zone_risk": ["deck", "cabin_top", "hull_sandwich"]}, {"mode": "Schubversagen zwischen Kern und Laminat", "onset_years": 10, "severity": "critical", "symptoms": "Deckoberfläche gibt nach, Laminat löst sich vom Kern", "prevention": "Ausreichende Harzschicht, Kerbschnitte im Kern für Harzbrücken", "zone_risk": ["deck", "hull"]}, {"mode": "Kernfäulnis bei Balsaholz", "onset_years": 6, "severity": "critical", "symptoms": "Weiche Bereiche, Verfärbung, moderner Geruch beim Öffnen", "prevention": "PVC- oder PET-Schaum statt Balsa in Feuchtzonen", "zone_risk": ["deck", "transom", "rudder"]}, {"mode": "Druckversagen unter Punktlasten", "onset_years": 0, "severity": "high", "symptoms": "Eindrücke in Deckoberfläche, Deformation", "prevention": "Lokale Verstärkungen unter Beschlägen, höhere Kerndichte wählen", "zone_risk": ["deck_hardware", "mast_step"]}], "water_ingress": {"risk_level": "high", "mechanisms": ["Kapillarwirkung an Schnittkanten", "Bohrungen für Beschläge", "Mikrorisse im Laminat", "Osmose durch Außenhaut"], "prevention": "Alle Bohrungen überdimensioniert bohren, mit Epoxy füllen, dann auf Maß nachbohren", "inspection_interval_months": 12}, "wear_patterns": [{"location": "Unter Decksbeschlägen", "cause": "Punktlasten und Vibration", "prevention": "Verdicktes Laminat oder Aluminium-Lastverteilplatten", "inspection_interval_months": 12}], "environmental_limits": {"max_temp_c": 65, "min_temp_c": -40, "uv_resistance_hours": 0, "salt_spray_resistance": "depends_on_outer_laminate", "humidity_tolerance": "Kern muss vollständig eingekapselt sein"}, "galvanic_compatibility": {"compatible_with": ["alle_nichtmetallischen"], "incompatible_with": [], "notes": "Kernmaterialien sind nicht leitfähig, aber Wasseraufnahme kann Elektrolyt bilden"}, "recommended_zones": ["deck_sandwich", "hull_sandwich", "cabin_top", "structural_bulkheads"]},
        "known_issues": ["Higher cost than PVC", "Still vulnerable to UV", "Requires proper surface protection"],
        "alternatives": ["Divinycell H80", "Honeycomb-Kern", "PET-Schaum"],
    },
    {
        "name": "Honeycomb-Kern (Nomex Honeycomb)",
        "category": "core",
        "subcategory": "honeycomb_core",
        "manufacturer": "Hexcel",
        "cost_per_unit": 16.0,
        "cost_unit": "sqm",
        "lifespan_years": 25,
        "maintenance_interval_months": 24,
        "maintenance_cost_factor": 0.01,
        "properties": {"density_kg_m3": 50, "compression_strength_kpa": 450, "lightweight": True, "fire_rating": "excellent", "stiffness_to_weight": "exceptional", "aluminum_cell": True, "installation_methods": [{"method": "Einlaminiert im Sandwichverfahren", "difficulty": "high", "tools_required": ["Kernmaterial", "Harz", "Glasfaser", "Vakuumanlage"], "typical_errors": ["Lufteinschlüsse zwischen Kern und Laminat", "Kernmaterial verschoben", "Ungleichmäßige Harzverteilung"]}, {"method": "Verklebt mit Strukturkleber", "difficulty": "medium", "tools_required": ["Thixotropierter Kleber", "Spachtel", "Klemmen"], "typical_errors": ["Zu dünne Klebeschicht", "Kern nicht entfettet"]}], "failure_modes": [{"mode": "Wasseraufnahme im Kern", "onset_years": 5, "severity": "critical", "symptoms": "Gewichtszunahme, weiche Stellen beim Klopfen, Blasen im Laminat", "prevention": "Schnittkanten versiegeln, Bohrungen abdichten, Drainage vorsehen", "zone_risk": ["deck", "cabin_top", "hull_sandwich"]}, {"mode": "Schubversagen zwischen Kern und Laminat", "onset_years": 10, "severity": "critical", "symptoms": "Deckoberfläche gibt nach, Laminat löst sich vom Kern", "prevention": "Ausreichende Harzschicht, Kerbschnitte im Kern für Harzbrücken", "zone_risk": ["deck", "hull"]}, {"mode": "Kernfäulnis bei Balsaholz", "onset_years": 6, "severity": "critical", "symptoms": "Weiche Bereiche, Verfärbung, moderner Geruch beim Öffnen", "prevention": "PVC- oder PET-Schaum statt Balsa in Feuchtzonen", "zone_risk": ["deck", "transom", "rudder"]}, {"mode": "Druckversagen unter Punktlasten", "onset_years": 0, "severity": "high", "symptoms": "Eindrücke in Deckoberfläche, Deformation", "prevention": "Lokale Verstärkungen unter Beschlägen, höhere Kerndichte wählen", "zone_risk": ["deck_hardware", "mast_step"]}], "water_ingress": {"risk_level": "high", "mechanisms": ["Kapillarwirkung an Schnittkanten", "Bohrungen für Beschläge", "Mikrorisse im Laminat", "Osmose durch Außenhaut"], "prevention": "Alle Bohrungen überdimensioniert bohren, mit Epoxy füllen, dann auf Maß nachbohren", "inspection_interval_months": 12}, "wear_patterns": [{"location": "Unter Decksbeschlägen", "cause": "Punktlasten und Vibration", "prevention": "Verdicktes Laminat oder Aluminium-Lastverteilplatten", "inspection_interval_months": 12}], "environmental_limits": {"max_temp_c": 65, "min_temp_c": -40, "uv_resistance_hours": 0, "salt_spray_resistance": "depends_on_outer_laminate", "humidity_tolerance": "Kern muss vollständig eingekapselt sein"}, "galvanic_compatibility": {"compatible_with": ["alle_nichtmetallischen"], "incompatible_with": [], "notes": "Kernmaterialien sind nicht leitfähig, aber Wasseraufnahme kann Elektrolyt bilden"}, "recommended_zones": ["deck_sandwich", "hull_sandwich", "cabin_top", "structural_bulkheads"]},
        "known_issues": ["Expensive", "Difficult to repair", "Moisture ingress risk at cell walls"],
        "alternatives": ["SAN-Schaum", "Divinycell H80", "Carbon honeycomb"],
    },
    {
        "name": "PET-Schaum (Recyclable Polyester)",
        "category": "core",
        "subcategory": "closed_cell_foam",
        "manufacturer": "Various",
        "cost_per_unit": 9.5,
        "cost_unit": "sqm",
        "lifespan_years": 20,
        "maintenance_interval_months": 18,
        "maintenance_cost_factor": 0.02,
        "properties": {"density_kg_m3": 100, "water_absorption_pct": 0.4, "compression_strength_kpa": 520, "recyclable": True, "good_strength_to_weight": True, "sustainable": True, "installation_methods": [{"method": "Einlaminiert im Sandwichverfahren", "difficulty": "high", "tools_required": ["Kernmaterial", "Harz", "Glasfaser", "Vakuumanlage"], "typical_errors": ["Lufteinschlüsse zwischen Kern und Laminat", "Kernmaterial verschoben", "Ungleichmäßige Harzverteilung"]}, {"method": "Verklebt mit Strukturkleber", "difficulty": "medium", "tools_required": ["Thixotropierter Kleber", "Spachtel", "Klemmen"], "typical_errors": ["Zu dünne Klebeschicht", "Kern nicht entfettet"]}], "failure_modes": [{"mode": "Wasseraufnahme im Kern", "onset_years": 5, "severity": "critical", "symptoms": "Gewichtszunahme, weiche Stellen beim Klopfen, Blasen im Laminat", "prevention": "Schnittkanten versiegeln, Bohrungen abdichten, Drainage vorsehen", "zone_risk": ["deck", "cabin_top", "hull_sandwich"]}, {"mode": "Schubversagen zwischen Kern und Laminat", "onset_years": 10, "severity": "critical", "symptoms": "Deckoberfläche gibt nach, Laminat löst sich vom Kern", "prevention": "Ausreichende Harzschicht, Kerbschnitte im Kern für Harzbrücken", "zone_risk": ["deck", "hull"]}, {"mode": "Kernfäulnis bei Balsaholz", "onset_years": 6, "severity": "critical", "symptoms": "Weiche Bereiche, Verfärbung, moderner Geruch beim Öffnen", "prevention": "PVC- oder PET-Schaum statt Balsa in Feuchtzonen", "zone_risk": ["deck", "transom", "rudder"]}, {"mode": "Druckversagen unter Punktlasten", "onset_years": 0, "severity": "high", "symptoms": "Eindrücke in Deckoberfläche, Deformation", "prevention": "Lokale Verstärkungen unter Beschlägen, höhere Kerndichte wählen", "zone_risk": ["deck_hardware", "mast_step"]}], "water_ingress": {"risk_level": "high", "mechanisms": ["Kapillarwirkung an Schnittkanten", "Bohrungen für Beschläge", "Mikrorisse im Laminat", "Osmose durch Außenhaut"], "prevention": "Alle Bohrungen überdimensioniert bohren, mit Epoxy füllen, dann auf Maß nachbohren", "inspection_interval_months": 12}, "wear_patterns": [{"location": "Unter Decksbeschlägen", "cause": "Punktlasten und Vibration", "prevention": "Verdicktes Laminat oder Aluminium-Lastverteilplatten", "inspection_interval_months": 12}], "environmental_limits": {"max_temp_c": 65, "min_temp_c": -40, "uv_resistance_hours": 0, "salt_spray_resistance": "depends_on_outer_laminate", "humidity_tolerance": "Kern muss vollständig eingekapselt sein"}, "galvanic_compatibility": {"compatible_with": ["alle_nichtmetallischen"], "incompatible_with": [], "notes": "Kernmaterialien sind nicht leitfähig, aber Wasseraufnahme kann Elektrolyt bilden"}, "recommended_zones": ["deck_sandwich", "hull_sandwich", "cabin_top", "structural_bulkheads"]},
        "known_issues": ["Limited temperature resistance vs PVC", "UV degradation possible", "Fewer suppliers than PVC"],
        "alternatives": ["Divinycell H80", "SAN-Schaum", "Balsa-Kern"],
    },
    {
        "name": "Marine Leder (Marine Leather)",
        "category": "textile",
        "subcategory": "upholstery",
        "manufacturer": "Various",
        "cost_per_unit": 35.0,
        "cost_unit": "sqm",
        "lifespan_years": 8,
        "maintenance_interval_months": 6,
        "maintenance_cost_factor": 0.08,
        "properties": {"durability_rating": "high", "salt_water_resistant": True, "uv_resistant": True, "breathable": True, "luxury_feel": True, "installation_methods": [{"method": "Geklebt mit Kontaktkleber", "difficulty": "medium", "tools_required": ["Kontaktkleber", "Andruckrolle", "Cuttermesser"], "typical_errors": ["Blasen durch zu schnelles Andrücken", "Kleber auf Sichtfläche"]}, {"method": "Getackert und Polsterpins", "difficulty": "low", "tools_required": ["Tackerpistole", "Klammern", "Polsterpins"], "typical_errors": ["Faltenbildung", "Klammern sichtbar"]}], "failure_modes": [{"mode": "UV-Zerfall", "onset_years": 3, "severity": "medium", "symptoms": "Verblassen, Fasern brüchig, Reißfestigkeit sinkt", "prevention": "UV-stabilisierte Stoffe, Sonnenschutz", "zone_risk": ["cockpit", "flybridge", "bimini"]}, {"mode": "Schimmelbefall", "onset_years": 1, "severity": "medium", "symptoms": "Schwarze Flecken, muffiger Geruch", "prevention": "Antimikrobielle Behandlung, gute Belüftung", "zone_risk": ["cabin_interior", "berths", "head"]}, {"mode": "Nähtefail unter Belastung", "onset_years": 5, "severity": "medium", "symptoms": "Nähte lösen sich, Stoff reißt an Nähten", "prevention": "Doppelnähte, verstärkte Kanten", "zone_risk": ["sails", "bimini", "cockpit_cushions"]}], "water_ingress": {"risk_level": "none", "mechanisms": [], "prevention": "N/A — Textilien sind keine Strukturmaterialien", "inspection_interval_months": 6}, "wear_patterns": [{"location": "Cockpit-Polster", "cause": "Reibung, UV, Salzwasser", "prevention": "Abnehmbare Bezüge, regelmäßige Reinigung", "inspection_interval_months": 6}, {"location": "Bimini/Sprayhoodflächen", "cause": "Windlast, UV, Regen", "prevention": "Spannungsfrei montiert, UV-Schutz", "inspection_interval_months": 12}], "environmental_limits": {"max_temp_c": 80, "min_temp_c": -20, "uv_resistance_hours": 3000, "salt_spray_resistance": "varies", "humidity_tolerance": "70% max empfohlen"}, "galvanic_compatibility": {"compatible_with": ["alle"], "incompatible_with": [], "notes": "Nicht relevant für Textilien"}, "recommended_zones": ["cabin_interior", "cockpit", "flybridge", "bimini"], "sewing_specifications": {'recommended_thread': 'nylon_bonded (innen) / polyester_v92 (außen)', 'thread_tex': '150 (innen) / 300 (außen)', 'needle_type': 'cutting_triangle (Dreikant-Schneidnadel)', 'needle_size': '#16-#20', 'stitch_type': 'Geradstich 301 (Maschine) / Sattlerstich (Hand-Premium)', 'stitch_length_mm': 3, 'stitches_per_cm': 3.3, 'seam_type': 'Flachnaht mit Kantenbug, Doppelnaht bei Belastung', 'thread_tension': 'medium_low — zu hoch perforiert Leder', 'assessment_notes': 'Dreikantige Schneidnadel Pflicht — runde Nadel reißt Leder. Stichbild muss gleichmäßig sein, jeder fehlgeschlagene Stich hinterlässt permanentes Loch. Farblich passender Faden empfohlen. Sattlerstich bei Reparatur oder Premium — jeder Stich von beiden Seiten, Naht hält auch wenn ein Faden reißt.', 'common_defects': ['Lochfraß durch zu große Nadel', 'Naht reißt Leder bei zu enger Stichlänge', 'Faden schneidet in weiches Leder — Spannung zu hoch']}},
        "known_issues": ["Requires regular cleaning", "Can fade with UV exposure", "Expensive maintenance"],
        "alternatives": ["Marine Vinyl", "Silvertex", "Alcantara Marine"],
    },
    {
        "name": "Marine Vinyl (Sunbrella Equivalent)",
        "category": "textile",
        "subcategory": "upholstery",
        "manufacturer": "Various",
        "cost_per_unit": 22.0,
        "cost_unit": "sqm",
        "lifespan_years": 10,
        "maintenance_interval_months": 12,
        "maintenance_cost_factor": 0.04,
        "properties": {"durability_rating": "very_high", "salt_water_resistant": True, "uv_resistant": True, "stain_resistant": True, "easy_clean": True, "installation_methods": [{"method": "Geklebt mit Kontaktkleber", "difficulty": "medium", "tools_required": ["Kontaktkleber", "Andruckrolle", "Cuttermesser"], "typical_errors": ["Blasen durch zu schnelles Andrücken", "Kleber auf Sichtfläche"]}, {"method": "Getackert und Polsterpins", "difficulty": "low", "tools_required": ["Tackerpistole", "Klammern", "Polsterpins"], "typical_errors": ["Faltenbildung", "Klammern sichtbar"]}], "failure_modes": [{"mode": "UV-Zerfall", "onset_years": 3, "severity": "medium", "symptoms": "Verblassen, Fasern brüchig, Reißfestigkeit sinkt", "prevention": "UV-stabilisierte Stoffe, Sonnenschutz", "zone_risk": ["cockpit", "flybridge", "bimini"]}, {"mode": "Schimmelbefall", "onset_years": 1, "severity": "medium", "symptoms": "Schwarze Flecken, muffiger Geruch", "prevention": "Antimikrobielle Behandlung, gute Belüftung", "zone_risk": ["cabin_interior", "berths", "head"]}, {"mode": "Nähtefail unter Belastung", "onset_years": 5, "severity": "medium", "symptoms": "Nähte lösen sich, Stoff reißt an Nähten", "prevention": "Doppelnähte, verstärkte Kanten", "zone_risk": ["sails", "bimini", "cockpit_cushions"]}], "water_ingress": {"risk_level": "none", "mechanisms": [], "prevention": "N/A — Textilien sind keine Strukturmaterialien", "inspection_interval_months": 6}, "wear_patterns": [{"location": "Cockpit-Polster", "cause": "Reibung, UV, Salzwasser", "prevention": "Abnehmbare Bezüge, regelmäßige Reinigung", "inspection_interval_months": 6}, {"location": "Bimini/Sprayhoodflächen", "cause": "Windlast, UV, Regen", "prevention": "Spannungsfrei montiert, UV-Schutz", "inspection_interval_months": 12}], "environmental_limits": {"max_temp_c": 80, "min_temp_c": -20, "uv_resistance_hours": 3000, "salt_spray_resistance": "varies", "humidity_tolerance": "70% max empfohlen"}, "galvanic_compatibility": {"compatible_with": ["alle"], "incompatible_with": [], "notes": "Nicht relevant für Textilien"}, "recommended_zones": ["cabin_interior", "cockpit", "flybridge", "bimini"], "sewing_specifications": {'recommended_thread': 'polyester_v92', 'thread_tex': 300, 'needle_type': 'wedge_point (Keilspitze)', 'needle_size': '#16-#20', 'stitch_type': 'Geradstich 301 / Doppelsteppstich 301x2', 'stitch_length_mm': 3.5, 'stitches_per_cm': 2.8, 'seam_type': 'Überwendnaht oder Flachnaht', 'thread_tension': 'medium', 'assessment_notes': 'Keilspitznadel MUSS verwendet werden — Schneidnadel perforiert PVC-Beschichtung und Wasser dringt ein. Zu enge Stiche = Perforation = Wassereintritt! Min. 3mm Stichlänge. Doppelnaht bei Cockpit-Polstern.', 'common_defects': ['PVC-Beschichtung perforiert bei falscher Nadel', 'Nahtlöcher als Wassereintrittspunkte', 'Vinyl klebt an Nähfuß — Teflonfuß verwenden']}},
        "known_issues": ["Can look plastic-like", "Less breathable than leather", "May crack in cold climate"],
        "alternatives": ["Marine Leder", "Silvertex", "Outdoorstoff Sunbrella"],
    },
    {
        "name": "Alcantara Marine (Synthetic Suede)",
        "category": "textile",
        "subcategory": "upholstery",
        "manufacturer": "Alcantara",
        "cost_per_unit": 48.0,
        "cost_unit": "sqm",
        "lifespan_years": 7,
        "maintenance_interval_months": 3,
        "maintenance_cost_factor": 0.12,
        "properties": {"feel": "luxurious_soft", "water_resistance": "moderate", "uv_resistance": "medium", "breathable": True, "premium": True, "installation_methods": [{"method": "Geklebt mit Kontaktkleber", "difficulty": "medium", "tools_required": ["Kontaktkleber", "Andruckrolle", "Cuttermesser"], "typical_errors": ["Blasen durch zu schnelles Andrücken", "Kleber auf Sichtfläche"]}, {"method": "Getackert und Polsterpins", "difficulty": "low", "tools_required": ["Tackerpistole", "Klammern", "Polsterpins"], "typical_errors": ["Faltenbildung", "Klammern sichtbar"]}], "failure_modes": [{"mode": "UV-Zerfall", "onset_years": 3, "severity": "medium", "symptoms": "Verblassen, Fasern brüchig, Reißfestigkeit sinkt", "prevention": "UV-stabilisierte Stoffe, Sonnenschutz", "zone_risk": ["cockpit", "flybridge", "bimini"]}, {"mode": "Schimmelbefall", "onset_years": 1, "severity": "medium", "symptoms": "Schwarze Flecken, muffiger Geruch", "prevention": "Antimikrobielle Behandlung, gute Belüftung", "zone_risk": ["cabin_interior", "berths", "head"]}, {"mode": "Nähtefail unter Belastung", "onset_years": 5, "severity": "medium", "symptoms": "Nähte lösen sich, Stoff reißt an Nähten", "prevention": "Doppelnähte, verstärkte Kanten", "zone_risk": ["sails", "bimini", "cockpit_cushions"]}], "water_ingress": {"risk_level": "none", "mechanisms": [], "prevention": "N/A — Textilien sind keine Strukturmaterialien", "inspection_interval_months": 6}, "wear_patterns": [{"location": "Cockpit-Polster", "cause": "Reibung, UV, Salzwasser", "prevention": "Abnehmbare Bezüge, regelmäßige Reinigung", "inspection_interval_months": 6}, {"location": "Bimini/Sprayhoodflächen", "cause": "Windlast, UV, Regen", "prevention": "Spannungsfrei montiert, UV-Schutz", "inspection_interval_months": 12}], "environmental_limits": {"max_temp_c": 80, "min_temp_c": -20, "uv_resistance_hours": 3000, "salt_spray_resistance": "varies", "humidity_tolerance": "70% max empfohlen"}, "galvanic_compatibility": {"compatible_with": ["alle"], "incompatible_with": [], "notes": "Nicht relevant für Textilien"}, "recommended_zones": ["cabin_interior", "cockpit", "flybridge", "bimini"], "sewing_specifications": {'recommended_thread': 'nylon_bonded', 'thread_tex': 150, 'needle_type': 'ball_point (Kugelspitze)', 'needle_size': '#12-#16', 'stitch_type': 'Geradstich 301 / Blindstich 103', 'stitch_length_mm': 2.5, 'stitches_per_cm': 4, 'seam_type': 'Flachnaht, Blindsaum für unsichtbare Kanten', 'thread_tension': 'low', 'assessment_notes': 'Alcantara ist extrem empfindlich — NUR Kugelspitznadel! Jede Nadelmarkierung bleibt auf Mikrofaser-Velours permanent sichtbar. Farblich exakt passender Faden ist Pflicht, da Stiche auf dem samtigen Flor sofort ins Auge fallen. Niedrige Spannung!', 'common_defects': ['Permanent sichtbare Nadelspuren bei falscher Nadel', 'Flor wird flachgedrückt unter Nähfuß', 'Farbabweichung zwischen Stoff und Faden sofort sichtbar']}},
        "known_issues": ["Requires frequent brushing", "Water stains easily", "High maintenance cost", "Fades with UV"],
        "alternatives": ["Marine Leder", "Silvertex", "Marine Vinyl"],
    },
    {
        "name": "Silvertex (Antimicrobial)",
        "category": "textile",
        "subcategory": "upholstery",
        "manufacturer": "Glen Raven",
        "cost_per_unit": 28.0,
        "cost_unit": "sqm",
        "lifespan_years": 11,
        "maintenance_interval_months": 12,
        "maintenance_cost_factor": 0.03,
        "properties": {"antimicrobial": True, "uv_resistant": True, "stain_resistant": True, "mildew_resistant": True, "solution_dyed": True, "installation_methods": [{"method": "Geklebt mit Kontaktkleber", "difficulty": "medium", "tools_required": ["Kontaktkleber", "Andruckrolle", "Cuttermesser"], "typical_errors": ["Blasen durch zu schnelles Andrücken", "Kleber auf Sichtfläche"]}, {"method": "Getackert und Polsterpins", "difficulty": "low", "tools_required": ["Tackerpistole", "Klammern", "Polsterpins"], "typical_errors": ["Faltenbildung", "Klammern sichtbar"]}], "failure_modes": [{"mode": "UV-Zerfall", "onset_years": 3, "severity": "medium", "symptoms": "Verblassen, Fasern brüchig, Reißfestigkeit sinkt", "prevention": "UV-stabilisierte Stoffe, Sonnenschutz", "zone_risk": ["cockpit", "flybridge", "bimini"]}, {"mode": "Schimmelbefall", "onset_years": 1, "severity": "medium", "symptoms": "Schwarze Flecken, muffiger Geruch", "prevention": "Antimikrobielle Behandlung, gute Belüftung", "zone_risk": ["cabin_interior", "berths", "head"]}, {"mode": "Nähtefail unter Belastung", "onset_years": 5, "severity": "medium", "symptoms": "Nähte lösen sich, Stoff reißt an Nähten", "prevention": "Doppelnähte, verstärkte Kanten", "zone_risk": ["sails", "bimini", "cockpit_cushions"]}], "water_ingress": {"risk_level": "none", "mechanisms": [], "prevention": "N/A — Textilien sind keine Strukturmaterialien", "inspection_interval_months": 6}, "wear_patterns": [{"location": "Cockpit-Polster", "cause": "Reibung, UV, Salzwasser", "prevention": "Abnehmbare Bezüge, regelmäßige Reinigung", "inspection_interval_months": 6}, {"location": "Bimini/Sprayhoodflächen", "cause": "Windlast, UV, Regen", "prevention": "Spannungsfrei montiert, UV-Schutz", "inspection_interval_months": 12}], "environmental_limits": {"max_temp_c": 80, "min_temp_c": -20, "uv_resistance_hours": 3000, "salt_spray_resistance": "varies", "humidity_tolerance": "70% max empfohlen"}, "galvanic_compatibility": {"compatible_with": ["alle"], "incompatible_with": [], "notes": "Nicht relevant für Textilien"}, "recommended_zones": ["cabin_interior", "cockpit", "flybridge", "bimini"], "sewing_specifications": {'recommended_thread': 'polyester_v92', 'thread_tex': 300, 'needle_type': 'wedge_point (Keilspitze)', 'needle_size': '#16-#18', 'stitch_type': 'Geradstich 301', 'stitch_length_mm': 3.5, 'stitches_per_cm': 2.8, 'seam_type': 'Standard-Flachnaht', 'thread_tension': 'medium', 'assessment_notes': 'Silvertex hat antimikrobielle Beschichtung — nicht beschädigen! Keilspitze schont Beschichtung. Lösung-gefärbt, daher farblich sehr stabil. Einfach zu verarbeiten.', 'common_defects': ['Antimikrobielle Beschichtung beschädigt durch Schneidnadel', 'Heißkleber beschädigt Oberfläche — nur Nähte verwenden']}},
        "known_issues": ["Still requires regular cleaning", "Antimicrobial effects degrade over time", "Higher cost"],
        "alternatives": ["Marine Vinyl", "Marine Leder", "Sunbrella fabric"],
    },
    {
        "name": "Outdoorstoff Sunbrella (Cushion Fabric)",
        "category": "textile",
        "subcategory": "canvas",
        "manufacturer": "Glen Raven",
        "cost_per_unit": 18.0,
        "cost_unit": "sqm",
        "lifespan_years": 9,
        "maintenance_interval_months": 12,
        "maintenance_cost_factor": 0.03,
        "properties": {"uv_resistance": "very_high", "water_resistant": True, "breathable": True, "color_retention": "excellent", "100pct_solution_dyed": True, "installation_methods": [{"method": "Geklebt mit Kontaktkleber", "difficulty": "medium", "tools_required": ["Kontaktkleber", "Andruckrolle", "Cuttermesser"], "typical_errors": ["Blasen durch zu schnelles Andrücken", "Kleber auf Sichtfläche"]}, {"method": "Getackert und Polsterpins", "difficulty": "low", "tools_required": ["Tackerpistole", "Klammern", "Polsterpins"], "typical_errors": ["Faltenbildung", "Klammern sichtbar"]}], "failure_modes": [{"mode": "UV-Zerfall", "onset_years": 3, "severity": "medium", "symptoms": "Verblassen, Fasern brüchig, Reißfestigkeit sinkt", "prevention": "UV-stabilisierte Stoffe, Sonnenschutz", "zone_risk": ["cockpit", "flybridge", "bimini"]}, {"mode": "Schimmelbefall", "onset_years": 1, "severity": "medium", "symptoms": "Schwarze Flecken, muffiger Geruch", "prevention": "Antimikrobielle Behandlung, gute Belüftung", "zone_risk": ["cabin_interior", "berths", "head"]}, {"mode": "Nähtefail unter Belastung", "onset_years": 5, "severity": "medium", "symptoms": "Nähte lösen sich, Stoff reißt an Nähten", "prevention": "Doppelnähte, verstärkte Kanten", "zone_risk": ["sails", "bimini", "cockpit_cushions"]}], "water_ingress": {"risk_level": "none", "mechanisms": [], "prevention": "N/A — Textilien sind keine Strukturmaterialien", "inspection_interval_months": 6}, "wear_patterns": [{"location": "Cockpit-Polster", "cause": "Reibung, UV, Salzwasser", "prevention": "Abnehmbare Bezüge, regelmäßige Reinigung", "inspection_interval_months": 6}, {"location": "Bimini/Sprayhoodflächen", "cause": "Windlast, UV, Regen", "prevention": "Spannungsfrei montiert, UV-Schutz", "inspection_interval_months": 12}], "environmental_limits": {"max_temp_c": 80, "min_temp_c": -20, "uv_resistance_hours": 3000, "salt_spray_resistance": "varies", "humidity_tolerance": "70% max empfohlen"}, "galvanic_compatibility": {"compatible_with": ["alle"], "incompatible_with": [], "notes": "Nicht relevant für Textilien"}, "recommended_zones": ["cabin_interior", "cockpit", "flybridge", "bimini"], "sewing_specifications": {'recommended_thread': 'polyester_v92 / polyester_v138 bei Hochlast', 'thread_tex': '300 (Standard) / 400 (Hochlast)', 'needle_type': 'cutting_point (Schneidspitze)', 'needle_size': '#16-#20', 'stitch_type': 'Doppelsteppstich 301x2 / Kappnaht bei exponierten Nähten', 'stitch_length_mm': 4, 'stitches_per_cm': 2.5, 'seam_type': 'Kappnaht an exponierten Stellen, Doppelnaht an Polstern', 'thread_tension': 'medium', 'assessment_notes': 'Sunbrella ist dankbares Material — lösung-gefärbt, UV-stabil, verzeiht Verarbeitungsfehler gut. Kappnaht an allen Stellen die Regen ausgesetzt sind (Bimini, Sprayhood). PTFE-Garn ist overkill — UV-beschichtetes Polyester reicht aus und ist günstiger.', 'common_defects': ['Kappnaht nicht wasserdicht wenn schlampig gefaltet', 'Doppelnaht ohne Nahtdichtband bei Regen undicht', 'Zu feines Garn für schweres Canvas — V-138 verwenden']}},
        "known_issues": ["Can still develop mildew in humid climates", "Not stain-proof", "Fading possible after 10+ years"],
        "alternatives": ["Marine Vinyl", "Silvertex", "Marine Leder"],
    },
    {
        "name": "Teppich Marine Grade (Marine Carpet)",
        "category": "textile",
        "subcategory": "flooring",
        "manufacturer": "Various",
        "cost_per_unit": 20.0,
        "cost_unit": "sqm",
        "lifespan_years": 6,
        "maintenance_interval_months": 6,
        "maintenance_cost_factor": 0.05,
        "properties": {"mildew_resistant": True, "water_resistant_backing": True, "non_slip": True, "comfortable": True, "acoustic_damping": True, "installation_methods": [{"method": "Geklebt mit Kontaktkleber", "difficulty": "medium", "tools_required": ["Kontaktkleber", "Andruckrolle", "Cuttermesser"], "typical_errors": ["Blasen durch zu schnelles Andrücken", "Kleber auf Sichtfläche"]}, {"method": "Getackert und Polsterpins", "difficulty": "low", "tools_required": ["Tackerpistole", "Klammern", "Polsterpins"], "typical_errors": ["Faltenbildung", "Klammern sichtbar"]}], "failure_modes": [{"mode": "UV-Zerfall", "onset_years": 3, "severity": "medium", "symptoms": "Verblassen, Fasern brüchig, Reißfestigkeit sinkt", "prevention": "UV-stabilisierte Stoffe, Sonnenschutz", "zone_risk": ["cockpit", "flybridge", "bimini"]}, {"mode": "Schimmelbefall", "onset_years": 1, "severity": "medium", "symptoms": "Schwarze Flecken, muffiger Geruch", "prevention": "Antimikrobielle Behandlung, gute Belüftung", "zone_risk": ["cabin_interior", "berths", "head"]}, {"mode": "Nähtefail unter Belastung", "onset_years": 5, "severity": "medium", "symptoms": "Nähte lösen sich, Stoff reißt an Nähten", "prevention": "Doppelnähte, verstärkte Kanten", "zone_risk": ["sails", "bimini", "cockpit_cushions"]}], "water_ingress": {"risk_level": "none", "mechanisms": [], "prevention": "N/A — Textilien sind keine Strukturmaterialien", "inspection_interval_months": 6}, "wear_patterns": [{"location": "Cockpit-Polster", "cause": "Reibung, UV, Salzwasser", "prevention": "Abnehmbare Bezüge, regelmäßige Reinigung", "inspection_interval_months": 6}, {"location": "Bimini/Sprayhoodflächen", "cause": "Windlast, UV, Regen", "prevention": "Spannungsfrei montiert, UV-Schutz", "inspection_interval_months": 12}], "environmental_limits": {"max_temp_c": 80, "min_temp_c": -20, "uv_resistance_hours": 3000, "salt_spray_resistance": "varies", "humidity_tolerance": "70% max empfohlen"}, "galvanic_compatibility": {"compatible_with": ["alle"], "incompatible_with": [], "notes": "Nicht relevant für Textilien"}, "recommended_zones": ["cabin_interior", "cockpit", "flybridge", "bimini"], "sewing_specifications": {'recommended_thread': 'polyester_v138', 'thread_tex': 400, 'needle_type': 'ball_point (Kugelspitze)', 'needle_size': '#18-#22', 'stitch_type': 'Overlockstich 504 (Kante) / Zickzack 304', 'stitch_length_mm': 5, 'stitches_per_cm': 2, 'seam_type': 'Overlock-Kantenversäuberung, ggf. Kederbandumfassung', 'thread_tension': 'medium', 'assessment_notes': 'Kugelspitze MUSS verwendet werden um Faserschlaufen nicht zu zerschneiden. Overlock an allen Schnittkanten ist Pflicht — sonst franst Marine-Teppich innerhalb von Monaten aus. Rückseite oft gummiert — Nadel muss durch Gummierung kommen.', 'common_defects': ['Faserschlaufen zerschnitten durch Schneidnadel', 'Kanten fransen aus ohne Overlock', 'Gummierung verstopft Nadel — regelmäßig reinigen']}},
        "known_issues": ["Absorbs moisture; mildew risk", "Stains easily", "Requires frequent vacuuming and cleaning"],
        "alternatives": ["Non-skid paint", "Vinyl flooring", "Teak decking"],
    },
    {
        "name": "Antifouling Kupfer (Copper-based)",
        "category": "coating",
        "subcategory": "antifouling",
        "manufacturer": "Various",
        "cost_per_unit": 28.0,
        "cost_unit": "liter",
        "lifespan_years": 3,
        "maintenance_interval_months": 36,
        "maintenance_cost_factor": 0.15,
        "properties": {"copper_content_pct": 25, "biocide": True, "traditional": True, "proven_effective": True, "water_based": False, "installation_methods": [{"method": "Spritzlackierung (HVLP)", "difficulty": "high", "tools_required": ["HVLP-Pistole", "Kompressor", "Atemschutz", "Schleifpapier"], "typical_errors": ["Nasenbildung", "Orange-Peel-Effekt", "Staubeinschlüsse"]}, {"method": "Rollerauftrag", "difficulty": "medium", "tools_required": ["Schaumstoffrolle", "Farbwanne", "Abklebeband"], "typical_errors": ["Rollenmarkierung", "Ungleichmäßige Schichtdicke"]}, {"method": "Pinselauftrag", "difficulty": "low", "tools_required": ["Pinsel", "Verdünner", "Abklebeband"], "typical_errors": ["Pinselstriche sichtbar", "Tropfnasen"]}], "failure_modes": [{"mode": "Blasenbildung/Blasenablösung", "onset_years": 2, "severity": "medium", "symptoms": "Blasen im Lack, Ablösung vom Untergrund", "prevention": "Untergrund sauber, trocken, entfettet; richtige Grundierung", "zone_risk": ["hull", "deck", "cabin_top"]}, {"mode": "Kreidung durch UV", "onset_years": 3, "severity": "low", "symptoms": "Oberfläche wird stumpf und pudrig", "prevention": "UV-stabile Lacksysteme, regelmäßig polieren", "zone_risk": ["hull_above_waterline", "deck", "cabin_top"]}, {"mode": "Antifouling-Erschöpfung", "onset_years": 1, "severity": "medium", "symptoms": "Bewuchs trotz Antifouling, Rumpfgeschwindigkeit sinkt", "prevention": "Jährlicher Neuanstrich, richtige Produktwahl für Revier", "zone_risk": ["hull_below_waterline"]}], "water_ingress": {"risk_level": "low", "mechanisms": ["Beschädigung der Schutzschicht durch Grundberührung", "Osmose bei mangelhaftem Barrier-Coat"], "prevention": "Schichtdicke messen, Barrier-Coat auf Epoxid-Basis", "inspection_interval_months": 12}, "wear_patterns": [{"location": "Wasserlinie", "cause": "Wellen, Schmutz, Reibung", "prevention": "Verstärkter Anstrich an der Wasserlinie", "inspection_interval_months": 6}, {"location": "Bugbereich", "cause": "Seeschlag, Spritzwasser", "prevention": "Zusätzliche Schutzschicht", "inspection_interval_months": 12}], "environmental_limits": {"max_temp_c": 80, "min_temp_c": -20, "uv_resistance_hours": 10000, "salt_spray_resistance": "high", "humidity_tolerance": "100% nach Aushärtung"}, "galvanic_compatibility": {"compatible_with": ["alle_bei_korrektem_system"], "incompatible_with": [], "notes": "Beschichtungen als Korrosionsschutz-Barriere nutzen"}, "recommended_zones": ["hull_below_waterline", "hull_above_waterline", "deck", "cabin_top", "engine_room"]},
        "known_issues": ["High copper content; environmental concerns", "Can damage aluminum hulls", "Staining possible"],
        "alternatives": ["Antifouling Silikon", "Ablative paint", "Copper-free alternatives"],
    },
    {
        "name": "Antifouling Silikon (Eco-friendly)",
        "category": "coating",
        "subcategory": "antifouling",
        "manufacturer": "Hempel",
        "cost_per_unit": 35.0,
        "cost_unit": "liter",
        "lifespan_years": 4,
        "maintenance_interval_months": 48,
        "maintenance_cost_factor": 0.12,
        "properties": {"silicone_based": True, "eco_friendly": True, "non_toxic_biocide": True, "self_polishing": True, "environmentally_approved": True, "installation_methods": [{"method": "Spritzlackierung (HVLP)", "difficulty": "high", "tools_required": ["HVLP-Pistole", "Kompressor", "Atemschutz", "Schleifpapier"], "typical_errors": ["Nasenbildung", "Orange-Peel-Effekt", "Staubeinschlüsse"]}, {"method": "Rollerauftrag", "difficulty": "medium", "tools_required": ["Schaumstoffrolle", "Farbwanne", "Abklebeband"], "typical_errors": ["Rollenmarkierung", "Ungleichmäßige Schichtdicke"]}, {"method": "Pinselauftrag", "difficulty": "low", "tools_required": ["Pinsel", "Verdünner", "Abklebeband"], "typical_errors": ["Pinselstriche sichtbar", "Tropfnasen"]}], "failure_modes": [{"mode": "Blasenbildung/Blasenablösung", "onset_years": 2, "severity": "medium", "symptoms": "Blasen im Lack, Ablösung vom Untergrund", "prevention": "Untergrund sauber, trocken, entfettet; richtige Grundierung", "zone_risk": ["hull", "deck", "cabin_top"]}, {"mode": "Kreidung durch UV", "onset_years": 3, "severity": "low", "symptoms": "Oberfläche wird stumpf und pudrig", "prevention": "UV-stabile Lacksysteme, regelmäßig polieren", "zone_risk": ["hull_above_waterline", "deck", "cabin_top"]}, {"mode": "Antifouling-Erschöpfung", "onset_years": 1, "severity": "medium", "symptoms": "Bewuchs trotz Antifouling, Rumpfgeschwindigkeit sinkt", "prevention": "Jährlicher Neuanstrich, richtige Produktwahl für Revier", "zone_risk": ["hull_below_waterline"]}], "water_ingress": {"risk_level": "low", "mechanisms": ["Beschädigung der Schutzschicht durch Grundberührung", "Osmose bei mangelhaftem Barrier-Coat"], "prevention": "Schichtdicke messen, Barrier-Coat auf Epoxid-Basis", "inspection_interval_months": 12}, "wear_patterns": [{"location": "Wasserlinie", "cause": "Wellen, Schmutz, Reibung", "prevention": "Verstärkter Anstrich an der Wasserlinie", "inspection_interval_months": 6}, {"location": "Bugbereich", "cause": "Seeschlag, Spritzwasser", "prevention": "Zusätzliche Schutzschicht", "inspection_interval_months": 12}], "environmental_limits": {"max_temp_c": 80, "min_temp_c": -20, "uv_resistance_hours": 10000, "salt_spray_resistance": "high", "humidity_tolerance": "100% nach Aushärtung"}, "galvanic_compatibility": {"compatible_with": ["alle_bei_korrektem_system"], "incompatible_with": [], "notes": "Beschichtungen als Korrosionsschutz-Barriere nutzen"}, "recommended_zones": ["hull_below_waterline", "hull_above_waterline", "deck", "cabin_top", "engine_room"]},
        "known_issues": ["Higher cost than copper", "Still under environmental scrutiny", "Variable effectiveness reports"],
        "alternatives": ["Antifouling Kupfer", "Ablative antifouling", "Copper-free paint"],
    },
    {
        "name": "Gelcoat ISO NPG (Standard)",
        "category": "coating",
        "subcategory": "gelcoat",
        "manufacturer": "Various",
        "cost_per_unit": 12.0,
        "cost_unit": "kg",
        "lifespan_years": 5,
        "maintenance_interval_months": 12,
        "maintenance_cost_factor": 0.08,
        "properties": {"polyester_based": True, "uv_stable": True, "color_retention": "good", "glossy_finish": True, "self_healing": False, "installation_methods": [{"method": "Spritzlackierung (HVLP)", "difficulty": "high", "tools_required": ["HVLP-Pistole", "Kompressor", "Atemschutz", "Schleifpapier"], "typical_errors": ["Nasenbildung", "Orange-Peel-Effekt", "Staubeinschlüsse"]}, {"method": "Rollerauftrag", "difficulty": "medium", "tools_required": ["Schaumstoffrolle", "Farbwanne", "Abklebeband"], "typical_errors": ["Rollenmarkierung", "Ungleichmäßige Schichtdicke"]}, {"method": "Pinselauftrag", "difficulty": "low", "tools_required": ["Pinsel", "Verdünner", "Abklebeband"], "typical_errors": ["Pinselstriche sichtbar", "Tropfnasen"]}], "failure_modes": [{"mode": "Blasenbildung/Blasenablösung", "onset_years": 2, "severity": "medium", "symptoms": "Blasen im Lack, Ablösung vom Untergrund", "prevention": "Untergrund sauber, trocken, entfettet; richtige Grundierung", "zone_risk": ["hull", "deck", "cabin_top"]}, {"mode": "Kreidung durch UV", "onset_years": 3, "severity": "low", "symptoms": "Oberfläche wird stumpf und pudrig", "prevention": "UV-stabile Lacksysteme, regelmäßig polieren", "zone_risk": ["hull_above_waterline", "deck", "cabin_top"]}, {"mode": "Antifouling-Erschöpfung", "onset_years": 1, "severity": "medium", "symptoms": "Bewuchs trotz Antifouling, Rumpfgeschwindigkeit sinkt", "prevention": "Jährlicher Neuanstrich, richtige Produktwahl für Revier", "zone_risk": ["hull_below_waterline"]}], "water_ingress": {"risk_level": "low", "mechanisms": ["Beschädigung der Schutzschicht durch Grundberührung", "Osmose bei mangelhaftem Barrier-Coat"], "prevention": "Schichtdicke messen, Barrier-Coat auf Epoxid-Basis", "inspection_interval_months": 12}, "wear_patterns": [{"location": "Wasserlinie", "cause": "Wellen, Schmutz, Reibung", "prevention": "Verstärkter Anstrich an der Wasserlinie", "inspection_interval_months": 6}, {"location": "Bugbereich", "cause": "Seeschlag, Spritzwasser", "prevention": "Zusätzliche Schutzschicht", "inspection_interval_months": 12}], "environmental_limits": {"max_temp_c": 80, "min_temp_c": -20, "uv_resistance_hours": 10000, "salt_spray_resistance": "high", "humidity_tolerance": "100% nach Aushärtung"}, "galvanic_compatibility": {"compatible_with": ["alle_bei_korrektem_system"], "incompatible_with": [], "notes": "Beschichtungen als Korrosionsschutz-Barriere nutzen"}, "recommended_zones": ["hull_below_waterline", "hull_above_waterline", "deck", "cabin_top", "engine_room"]},
        "known_issues": ["UV degradation over time", "Can crack and chip", "Osmosis risk if not sealed"],
        "alternatives": ["Epoxy-Primer", "Polyurethane topcoat", "Vinyl ester gelcoat"],
    },
    {
        "name": "Awlgrip Polyurethan (Premium Paint)",
        "category": "coating",
        "subcategory": "topcoat",
        "manufacturer": "Interlux",
        "cost_per_unit": 55.0,
        "cost_unit": "liter",
        "lifespan_years": 8,
        "maintenance_interval_months": 24,
        "maintenance_cost_factor": 0.06,
        "properties": {"polyurethane": True, "high_gloss": True, "uv_resistant": True, "color_retention": "excellent", "premium_finish": True, "installation_methods": [{"method": "Spritzlackierung (HVLP)", "difficulty": "high", "tools_required": ["HVLP-Pistole", "Kompressor", "Atemschutz", "Schleifpapier"], "typical_errors": ["Nasenbildung", "Orange-Peel-Effekt", "Staubeinschlüsse"]}, {"method": "Rollerauftrag", "difficulty": "medium", "tools_required": ["Schaumstoffrolle", "Farbwanne", "Abklebeband"], "typical_errors": ["Rollenmarkierung", "Ungleichmäßige Schichtdicke"]}, {"method": "Pinselauftrag", "difficulty": "low", "tools_required": ["Pinsel", "Verdünner", "Abklebeband"], "typical_errors": ["Pinselstriche sichtbar", "Tropfnasen"]}], "failure_modes": [{"mode": "Blasenbildung/Blasenablösung", "onset_years": 2, "severity": "medium", "symptoms": "Blasen im Lack, Ablösung vom Untergrund", "prevention": "Untergrund sauber, trocken, entfettet; richtige Grundierung", "zone_risk": ["hull", "deck", "cabin_top"]}, {"mode": "Kreidung durch UV", "onset_years": 3, "severity": "low", "symptoms": "Oberfläche wird stumpf und pudrig", "prevention": "UV-stabile Lacksysteme, regelmäßig polieren", "zone_risk": ["hull_above_waterline", "deck", "cabin_top"]}, {"mode": "Antifouling-Erschöpfung", "onset_years": 1, "severity": "medium", "symptoms": "Bewuchs trotz Antifouling, Rumpfgeschwindigkeit sinkt", "prevention": "Jährlicher Neuanstrich, richtige Produktwahl für Revier", "zone_risk": ["hull_below_waterline"]}], "water_ingress": {"risk_level": "low", "mechanisms": ["Beschädigung der Schutzschicht durch Grundberührung", "Osmose bei mangelhaftem Barrier-Coat"], "prevention": "Schichtdicke messen, Barrier-Coat auf Epoxid-Basis", "inspection_interval_months": 12}, "wear_patterns": [{"location": "Wasserlinie", "cause": "Wellen, Schmutz, Reibung", "prevention": "Verstärkter Anstrich an der Wasserlinie", "inspection_interval_months": 6}, {"location": "Bugbereich", "cause": "Seeschlag, Spritzwasser", "prevention": "Zusätzliche Schutzschicht", "inspection_interval_months": 12}], "environmental_limits": {"max_temp_c": 80, "min_temp_c": -20, "uv_resistance_hours": 10000, "salt_spray_resistance": "high", "humidity_tolerance": "100% nach Aushärtung"}, "galvanic_compatibility": {"compatible_with": ["alle_bei_korrektem_system"], "incompatible_with": [], "notes": "Beschichtungen als Korrosionsschutz-Barriere nutzen"}, "recommended_zones": ["hull_below_waterline", "hull_above_waterline", "deck", "cabin_top", "engine_room"]},
        "known_issues": ["High cost", "Requires multi-coat application", "Complex surface prep needed"],
        "alternatives": ["Epoxy-Primer", "Polyester topcoat", "2-part polyurethane"],
    },
    {
        "name": "Epoxy-Primer (Underwater Protection)",
        "category": "coating",
        "subcategory": "primer",
        "manufacturer": "Various",
        "cost_per_unit": 18.0,
        "cost_unit": "liter",
        "lifespan_years": 6,
        "maintenance_interval_months": 36,
        "maintenance_cost_factor": 0.04,
        "properties": {"epoxy_based": True, "water_resistant": True, "excellent_adhesion": True, "corrosion_inhibiting": True, "two_part": True, "installation_methods": [{"method": "Spritzlackierung (HVLP)", "difficulty": "high", "tools_required": ["HVLP-Pistole", "Kompressor", "Atemschutz", "Schleifpapier"], "typical_errors": ["Nasenbildung", "Orange-Peel-Effekt", "Staubeinschlüsse"]}, {"method": "Rollerauftrag", "difficulty": "medium", "tools_required": ["Schaumstoffrolle", "Farbwanne", "Abklebeband"], "typical_errors": ["Rollenmarkierung", "Ungleichmäßige Schichtdicke"]}, {"method": "Pinselauftrag", "difficulty": "low", "tools_required": ["Pinsel", "Verdünner", "Abklebeband"], "typical_errors": ["Pinselstriche sichtbar", "Tropfnasen"]}], "failure_modes": [{"mode": "Blasenbildung/Blasenablösung", "onset_years": 2, "severity": "medium", "symptoms": "Blasen im Lack, Ablösung vom Untergrund", "prevention": "Untergrund sauber, trocken, entfettet; richtige Grundierung", "zone_risk": ["hull", "deck", "cabin_top"]}, {"mode": "Kreidung durch UV", "onset_years": 3, "severity": "low", "symptoms": "Oberfläche wird stumpf und pudrig", "prevention": "UV-stabile Lacksysteme, regelmäßig polieren", "zone_risk": ["hull_above_waterline", "deck", "cabin_top"]}, {"mode": "Antifouling-Erschöpfung", "onset_years": 1, "severity": "medium", "symptoms": "Bewuchs trotz Antifouling, Rumpfgeschwindigkeit sinkt", "prevention": "Jährlicher Neuanstrich, richtige Produktwahl für Revier", "zone_risk": ["hull_below_waterline"]}], "water_ingress": {"risk_level": "low", "mechanisms": ["Beschädigung der Schutzschicht durch Grundberührung", "Osmose bei mangelhaftem Barrier-Coat"], "prevention": "Schichtdicke messen, Barrier-Coat auf Epoxid-Basis", "inspection_interval_months": 12}, "wear_patterns": [{"location": "Wasserlinie", "cause": "Wellen, Schmutz, Reibung", "prevention": "Verstärkter Anstrich an der Wasserlinie", "inspection_interval_months": 6}, {"location": "Bugbereich", "cause": "Seeschlag, Spritzwasser", "prevention": "Zusätzliche Schutzschicht", "inspection_interval_months": 12}], "environmental_limits": {"max_temp_c": 80, "min_temp_c": -20, "uv_resistance_hours": 10000, "salt_spray_resistance": "high", "humidity_tolerance": "100% nach Aushärtung"}, "galvanic_compatibility": {"compatible_with": ["alle_bei_korrektem_system"], "incompatible_with": [], "notes": "Beschichtungen als Korrosionsschutz-Barriere nutzen"}, "recommended_zones": ["hull_below_waterline", "hull_above_waterline", "deck", "cabin_top", "engine_room"]},
        "known_issues": ["Pot life limited once mixed", "Requires controlled application temp", "Sensitive to surface moisture"],
        "alternatives": ["Polyester primer", "Zinc-rich primer", "Wash primer"],
    },
    {
        "name": "Teak-Öl (Teak Oil Maintenance)",
        "category": "coating",
        "subcategory": "wood_treatment",
        "manufacturer": "Various",
        "cost_per_unit": 32.0,
        "cost_unit": "liter",
        "lifespan_years": 2,
        "maintenance_interval_months": 6,
        "maintenance_cost_factor": 0.1,
        "properties": {"penetrating_oil": True, "natural_ingredient": True, "uv_protection": "medium", "water_repellent": True, "enhances_grain": True, "installation_methods": [{"method": "Spritzlackierung (HVLP)", "difficulty": "high", "tools_required": ["HVLP-Pistole", "Kompressor", "Atemschutz", "Schleifpapier"], "typical_errors": ["Nasenbildung", "Orange-Peel-Effekt", "Staubeinschlüsse"]}, {"method": "Rollerauftrag", "difficulty": "medium", "tools_required": ["Schaumstoffrolle", "Farbwanne", "Abklebeband"], "typical_errors": ["Rollenmarkierung", "Ungleichmäßige Schichtdicke"]}, {"method": "Pinselauftrag", "difficulty": "low", "tools_required": ["Pinsel", "Verdünner", "Abklebeband"], "typical_errors": ["Pinselstriche sichtbar", "Tropfnasen"]}], "failure_modes": [{"mode": "Blasenbildung/Blasenablösung", "onset_years": 2, "severity": "medium", "symptoms": "Blasen im Lack, Ablösung vom Untergrund", "prevention": "Untergrund sauber, trocken, entfettet; richtige Grundierung", "zone_risk": ["hull", "deck", "cabin_top"]}, {"mode": "Kreidung durch UV", "onset_years": 3, "severity": "low", "symptoms": "Oberfläche wird stumpf und pudrig", "prevention": "UV-stabile Lacksysteme, regelmäßig polieren", "zone_risk": ["hull_above_waterline", "deck", "cabin_top"]}, {"mode": "Antifouling-Erschöpfung", "onset_years": 1, "severity": "medium", "symptoms": "Bewuchs trotz Antifouling, Rumpfgeschwindigkeit sinkt", "prevention": "Jährlicher Neuanstrich, richtige Produktwahl für Revier", "zone_risk": ["hull_below_waterline"]}], "water_ingress": {"risk_level": "low", "mechanisms": ["Beschädigung der Schutzschicht durch Grundberührung", "Osmose bei mangelhaftem Barrier-Coat"], "prevention": "Schichtdicke messen, Barrier-Coat auf Epoxid-Basis", "inspection_interval_months": 12}, "wear_patterns": [{"location": "Wasserlinie", "cause": "Wellen, Schmutz, Reibung", "prevention": "Verstärkter Anstrich an der Wasserlinie", "inspection_interval_months": 6}, {"location": "Bugbereich", "cause": "Seeschlag, Spritzwasser", "prevention": "Zusätzliche Schutzschicht", "inspection_interval_months": 12}], "environmental_limits": {"max_temp_c": 80, "min_temp_c": -20, "uv_resistance_hours": 10000, "salt_spray_resistance": "high", "humidity_tolerance": "100% nach Aushärtung"}, "galvanic_compatibility": {"compatible_with": ["alle_bei_korrektem_system"], "incompatible_with": [], "notes": "Beschichtungen als Korrosionsschutz-Barriere nutzen"}, "recommended_zones": ["hull_below_waterline", "hull_above_waterline", "deck", "cabin_top", "engine_room"]},
        "known_issues": ["Requires frequent reapplication", "Can build up and turn dark", "Flammable product"],
        "alternatives": ["Teak sealer", "Hardwax oil", "UV-protective sealant"],
    },
    {
        "name": "Sikaflex 291i (Polyurethane Sealant)",
        "category": "sealant",
        "subcategory": "polyurethane",
        "manufacturer": "Sika",
        "cost_per_unit": 14.0,
        "cost_unit": "piece",
        "lifespan_years": 15,
        "maintenance_interval_months": 36,
        "maintenance_cost_factor": 0.02,
        "properties": {"polyurethane": True, "marine_grade": True, "uv_resistant": True, "flexible": True, "one_part": True, "installation_methods": [{"method": "Kartusche mit Druckluft", "difficulty": "medium", "tools_required": ["Druckluft-Kartuschenpistole", "Düsen", "Spachtel", "Abklebeband"], "typical_errors": ["Zu dicke Raupe", "Abklebeband zu spät entfernt", "Oberfläche nicht grundiert"]}, {"method": "Handdosierung", "difficulty": "low", "tools_required": ["Handkartusche", "Spachtel"], "typical_errors": ["Ungleichmäßiger Auftrag", "Luftblasen in Fuge"]}], "failure_modes": [{"mode": "Adhäsionsversagen", "onset_years": 5, "severity": "high", "symptoms": "Dichtmasse löst sich vom Untergrund, Wasser dringt ein", "prevention": "Primer verwenden, Untergrund anschleifen und entfetten", "zone_risk": ["deck", "windows", "hatches", "through_hulls"]}, {"mode": "Kohäsionsversagen", "onset_years": 8, "severity": "medium", "symptoms": "Riss in der Dichtmasse selbst", "prevention": "Richtige Fugengeometrie (2:1 Breite:Tiefe), nicht zu dünn auftragen", "zone_risk": ["deck", "windows"]}, {"mode": "UV-Alterung", "onset_years": 5, "severity": "medium", "symptoms": "Verhärtung, Rissbildung, Verfärbung", "prevention": "UV-stabile Dichtmasse, oder überstreichen", "zone_risk": ["deck", "cockpit"]}], "water_ingress": {"risk_level": "high", "mechanisms": ["Adhäsionsversagen an Befestigungen", "Alterungsbedingte Rissbildung", "Falsche Produktwahl"], "prevention": "Richtige Dichtmasse für Anwendung wählen (z.B. Sikaflex 291i für unter Wasser, 296 für Scheiben)", "inspection_interval_months": 12}, "wear_patterns": [{"location": "Decksdurchführungen", "cause": "Mechanische Belastung, Temperaturwechsel", "prevention": "Regelmäßige Sichtkontrolle", "inspection_interval_months": 12}], "environmental_limits": {"max_temp_c": 90, "min_temp_c": -40, "uv_resistance_hours": 5000, "salt_spray_resistance": "high", "humidity_tolerance": "100%"}, "galvanic_compatibility": {"compatible_with": ["alle"], "incompatible_with": [], "notes": "Dichtmassen können als galvanische Isolierung dienen"}, "recommended_zones": ["deck_hardware", "windows", "hatches", "through_hulls", "hull_deck_joint"]},
        "known_issues": ["Can stain if not cleaned quickly", "Adhesion failures possible", "Difficult to remove after cure"],
        "alternatives": ["3M 5200", "Terostat MS", "Polyurethane adhesive"],
    },
    {
        "name": "3M 5200 (Permanent Adhesive-Sealant)",
        "category": "sealant",
        "subcategory": "polyurethane",
        "manufacturer": "3M",
        "cost_per_unit": 16.0,
        "cost_unit": "piece",
        "lifespan_years": 20,
        "maintenance_interval_months": 48,
        "maintenance_cost_factor": 0.01,
        "properties": {"polyurethane": True, "marine_grade": True, "permanent_set": True, "gap_filling": True, "excellent_adhesion": True, "installation_methods": [{"method": "Kartusche mit Druckluft", "difficulty": "medium", "tools_required": ["Druckluft-Kartuschenpistole", "Düsen", "Spachtel", "Abklebeband"], "typical_errors": ["Zu dicke Raupe", "Abklebeband zu spät entfernt", "Oberfläche nicht grundiert"]}, {"method": "Handdosierung", "difficulty": "low", "tools_required": ["Handkartusche", "Spachtel"], "typical_errors": ["Ungleichmäßiger Auftrag", "Luftblasen in Fuge"]}], "failure_modes": [{"mode": "Adhäsionsversagen", "onset_years": 5, "severity": "high", "symptoms": "Dichtmasse löst sich vom Untergrund, Wasser dringt ein", "prevention": "Primer verwenden, Untergrund anschleifen und entfetten", "zone_risk": ["deck", "windows", "hatches", "through_hulls"]}, {"mode": "Kohäsionsversagen", "onset_years": 8, "severity": "medium", "symptoms": "Riss in der Dichtmasse selbst", "prevention": "Richtige Fugengeometrie (2:1 Breite:Tiefe), nicht zu dünn auftragen", "zone_risk": ["deck", "windows"]}, {"mode": "UV-Alterung", "onset_years": 5, "severity": "medium", "symptoms": "Verhärtung, Rissbildung, Verfärbung", "prevention": "UV-stabile Dichtmasse, oder überstreichen", "zone_risk": ["deck", "cockpit"]}], "water_ingress": {"risk_level": "high", "mechanisms": ["Adhäsionsversagen an Befestigungen", "Alterungsbedingte Rissbildung", "Falsche Produktwahl"], "prevention": "Richtige Dichtmasse für Anwendung wählen (z.B. Sikaflex 291i für unter Wasser, 296 für Scheiben)", "inspection_interval_months": 12}, "wear_patterns": [{"location": "Decksdurchführungen", "cause": "Mechanische Belastung, Temperaturwechsel", "prevention": "Regelmäßige Sichtkontrolle", "inspection_interval_months": 12}], "environmental_limits": {"max_temp_c": 90, "min_temp_c": -40, "uv_resistance_hours": 5000, "salt_spray_resistance": "high", "humidity_tolerance": "100%"}, "galvanic_compatibility": {"compatible_with": ["alle"], "incompatible_with": [], "notes": "Dichtmassen können als galvanische Isolierung dienen"}, "recommended_zones": ["deck_hardware", "windows", "hatches", "through_hulls", "hull_deck_joint"]},
        "known_issues": ["Very difficult to remove", "Can stain surfaces", "Requires careful application"],
        "alternatives": ["Sikaflex 291i", "Terostat MS", "Polysulfide sealant"],
    },
    {
        "name": "Terostat MS (MS-Polymer Hybrid)",
        "category": "sealant",
        "subcategory": "ms_polymer",
        "manufacturer": "Henkel",
        "cost_per_unit": 12.0,
        "cost_unit": "piece",
        "lifespan_years": 12,
        "maintenance_interval_months": 36,
        "maintenance_cost_factor": 0.02,
        "properties": {"ms_polymer": True, "low_odor": True, "easy_cleanup": True, "fast_cure": True, "paintable": True, "installation_methods": [{"method": "Kartusche mit Druckluft", "difficulty": "medium", "tools_required": ["Druckluft-Kartuschenpistole", "Düsen", "Spachtel", "Abklebeband"], "typical_errors": ["Zu dicke Raupe", "Abklebeband zu spät entfernt", "Oberfläche nicht grundiert"]}, {"method": "Handdosierung", "difficulty": "low", "tools_required": ["Handkartusche", "Spachtel"], "typical_errors": ["Ungleichmäßiger Auftrag", "Luftblasen in Fuge"]}], "failure_modes": [{"mode": "Adhäsionsversagen", "onset_years": 5, "severity": "high", "symptoms": "Dichtmasse löst sich vom Untergrund, Wasser dringt ein", "prevention": "Primer verwenden, Untergrund anschleifen und entfetten", "zone_risk": ["deck", "windows", "hatches", "through_hulls"]}, {"mode": "Kohäsionsversagen", "onset_years": 8, "severity": "medium", "symptoms": "Riss in der Dichtmasse selbst", "prevention": "Richtige Fugengeometrie (2:1 Breite:Tiefe), nicht zu dünn auftragen", "zone_risk": ["deck", "windows"]}, {"mode": "UV-Alterung", "onset_years": 5, "severity": "medium", "symptoms": "Verhärtung, Rissbildung, Verfärbung", "prevention": "UV-stabile Dichtmasse, oder überstreichen", "zone_risk": ["deck", "cockpit"]}], "water_ingress": {"risk_level": "high", "mechanisms": ["Adhäsionsversagen an Befestigungen", "Alterungsbedingte Rissbildung", "Falsche Produktwahl"], "prevention": "Richtige Dichtmasse für Anwendung wählen (z.B. Sikaflex 291i für unter Wasser, 296 für Scheiben)", "inspection_interval_months": 12}, "wear_patterns": [{"location": "Decksdurchführungen", "cause": "Mechanische Belastung, Temperaturwechsel", "prevention": "Regelmäßige Sichtkontrolle", "inspection_interval_months": 12}], "environmental_limits": {"max_temp_c": 90, "min_temp_c": -40, "uv_resistance_hours": 5000, "salt_spray_resistance": "high", "humidity_tolerance": "100%"}, "galvanic_compatibility": {"compatible_with": ["alle"], "incompatible_with": [], "notes": "Dichtmassen können als galvanische Isolierung dienen"}, "recommended_zones": ["deck_hardware", "windows", "hatches", "through_hulls", "hull_deck_joint"]},
        "known_issues": ["Lower strength than pure polyurethane", "Limited UV resistance", "Shorter lifespan"],
        "alternatives": ["Sikaflex 291i", "3M 5200", "Polyurethane sealant"],
    },
    {
        "name": "Caulking Compound (Deck Seams)",
        "category": "sealant",
        "subcategory": "flexible_caulk",
        "manufacturer": "Various",
        "cost_per_unit": 9.0,
        "cost_unit": "piece",
        "lifespan_years": 8,
        "maintenance_interval_months": 24,
        "maintenance_cost_factor": 0.04,
        "properties": {"silicone_based": True, "paintable": True, "flexible": True, "uv_stable": True, "water_resistant": True, "installation_methods": [{"method": "Kartusche mit Druckluft", "difficulty": "medium", "tools_required": ["Druckluft-Kartuschenpistole", "Düsen", "Spachtel", "Abklebeband"], "typical_errors": ["Zu dicke Raupe", "Abklebeband zu spät entfernt", "Oberfläche nicht grundiert"]}, {"method": "Handdosierung", "difficulty": "low", "tools_required": ["Handkartusche", "Spachtel"], "typical_errors": ["Ungleichmäßiger Auftrag", "Luftblasen in Fuge"]}], "failure_modes": [{"mode": "Adhäsionsversagen", "onset_years": 5, "severity": "high", "symptoms": "Dichtmasse löst sich vom Untergrund, Wasser dringt ein", "prevention": "Primer verwenden, Untergrund anschleifen und entfetten", "zone_risk": ["deck", "windows", "hatches", "through_hulls"]}, {"mode": "Kohäsionsversagen", "onset_years": 8, "severity": "medium", "symptoms": "Riss in der Dichtmasse selbst", "prevention": "Richtige Fugengeometrie (2:1 Breite:Tiefe), nicht zu dünn auftragen", "zone_risk": ["deck", "windows"]}, {"mode": "UV-Alterung", "onset_years": 5, "severity": "medium", "symptoms": "Verhärtung, Rissbildung, Verfärbung", "prevention": "UV-stabile Dichtmasse, oder überstreichen", "zone_risk": ["deck", "cockpit"]}], "water_ingress": {"risk_level": "high", "mechanisms": ["Adhäsionsversagen an Befestigungen", "Alterungsbedingte Rissbildung", "Falsche Produktwahl"], "prevention": "Richtige Dichtmasse für Anwendung wählen (z.B. Sikaflex 291i für unter Wasser, 296 für Scheiben)", "inspection_interval_months": 12}, "wear_patterns": [{"location": "Decksdurchführungen", "cause": "Mechanische Belastung, Temperaturwechsel", "prevention": "Regelmäßige Sichtkontrolle", "inspection_interval_months": 12}], "environmental_limits": {"max_temp_c": 90, "min_temp_c": -40, "uv_resistance_hours": 5000, "salt_spray_resistance": "high", "humidity_tolerance": "100%"}, "galvanic_compatibility": {"compatible_with": ["alle"], "incompatible_with": [], "notes": "Dichtmassen können als galvanische Isolierung dienen"}, "recommended_zones": ["deck_hardware", "windows", "hatches", "through_hulls", "hull_deck_joint"]},
        "known_issues": ["Requires regular inspection", "Can shrink over time", "May need recaulking every 3-5 years"],
        "alternatives": ["Sikaflex 291i", "Polyurethane caulk", "Butyl caulk"],
    },
    {
        "name": "Sicherheitsglas gehärtet (Tempered Safety Glass)",
        "category": "glass",
        "subcategory": "window_glass",
        "manufacturer": "Various",
        "cost_per_unit": 85.0,
        "cost_unit": "sqm",
        "lifespan_years": 30,
        "maintenance_interval_months": 12,
        "maintenance_cost_factor": 0.01,
        "properties": {"tempered": True, "safety_rated": True, "thermal_expansion_resistant": True, "impact_resistant": True, "standard_thickness_mm": [5, 6, 8], "installation_methods": [{"method": "Eingeklebt mit PU-Kleber", "difficulty": "high", "tools_required": ["PU-Kleber", "Distanzstücke", "Saugnapfheber"], "typical_errors": ["Scheibe verkantet", "Klebenaht zu dünn", "Primer vergessen"]}, {"method": "Mechanisch gerahmt", "difficulty": "medium", "tools_required": ["Rahmen", "Schrauben", "EPDM-Dichtung"], "typical_errors": ["Dichtung falsch dimensioniert", "Schrauben zu fest"]}], "failure_modes": [{"mode": "Klebenaht-Versagen", "onset_years": 10, "severity": "high", "symptoms": "Scheibe löst sich, Wasser dringt ein", "prevention": "Richtige Klebstoffauswahl, UV-Schutz der Klebenaht", "zone_risk": ["windows", "windscreen"]}, {"mode": "Spannungsriss durch Temperaturschock", "onset_years": 0, "severity": "high", "symptoms": "Spontane Rissbildung bei schneller Temperaturänderung", "prevention": "ESG-Glas verwenden, keine Punktbelastung", "zone_risk": ["windows", "skylights"]}, {"mode": "Kratzer und Trübung", "onset_years": 5, "severity": "low", "symptoms": "Sichteinschränkung, Mikrokratzer", "prevention": "Weiche Reinigungsmittel, keine Scheibenwischer auf Salzwasser", "zone_risk": ["windscreen", "windows"]}], "water_ingress": {"risk_level": "high", "mechanisms": ["Klebenaht-Alterung", "Rahmendichtung schrumpft", "Scheibenrahmen korrodiert"], "prevention": "Regelmäßige Inspektion der Klebenaht, Dichtungstausch alle 10 Jahre", "inspection_interval_months": 12}, "wear_patterns": [{"location": "Windschutzscheibe", "cause": "Salzwasser, Scheibenwischer, UV", "prevention": "Weiche Wischerblätter, Süßwasserspülung", "inspection_interval_months": 6}], "environmental_limits": {"max_temp_c": 250, "min_temp_c": -60, "uv_resistance_hours": 100000, "salt_spray_resistance": "high", "humidity_tolerance": "100%"}, "galvanic_compatibility": {"compatible_with": ["alle"], "incompatible_with": [], "notes": "Glas ist nicht leitfähig"}, "recommended_zones": ["windows", "windscreen", "skylights", "portlights"]},
        "known_issues": ["Shatters into small pieces when broken", "Cannot be cut after tempering", "More expensive"],
        "alternatives": ["Verbund-Sicherheitsglas", "Polycarbonat", "Acrylglas"],
    },
    {
        "name": "Verbund-Sicherheitsglas (Laminated Safety Glass)",
        "category": "glass",
        "subcategory": "window_glass",
        "manufacturer": "Various",
        "cost_per_unit": 95.0,
        "cost_unit": "sqm",
        "lifespan_years": 32,
        "maintenance_interval_months": 12,
        "maintenance_cost_factor": 0.01,
        "properties": {"laminated": True, "safety_rated": True, "uv_protective_interlayer": True, "impact_resistant": True, "coastal_grade": True, "installation_methods": [{"method": "Eingeklebt mit PU-Kleber", "difficulty": "high", "tools_required": ["PU-Kleber", "Distanzstücke", "Saugnapfheber"], "typical_errors": ["Scheibe verkantet", "Klebenaht zu dünn", "Primer vergessen"]}, {"method": "Mechanisch gerahmt", "difficulty": "medium", "tools_required": ["Rahmen", "Schrauben", "EPDM-Dichtung"], "typical_errors": ["Dichtung falsch dimensioniert", "Schrauben zu fest"]}], "failure_modes": [{"mode": "Klebenaht-Versagen", "onset_years": 10, "severity": "high", "symptoms": "Scheibe löst sich, Wasser dringt ein", "prevention": "Richtige Klebstoffauswahl, UV-Schutz der Klebenaht", "zone_risk": ["windows", "windscreen"]}, {"mode": "Spannungsriss durch Temperaturschock", "onset_years": 0, "severity": "high", "symptoms": "Spontane Rissbildung bei schneller Temperaturänderung", "prevention": "ESG-Glas verwenden, keine Punktbelastung", "zone_risk": ["windows", "skylights"]}, {"mode": "Kratzer und Trübung", "onset_years": 5, "severity": "low", "symptoms": "Sichteinschränkung, Mikrokratzer", "prevention": "Weiche Reinigungsmittel, keine Scheibenwischer auf Salzwasser", "zone_risk": ["windscreen", "windows"]}], "water_ingress": {"risk_level": "high", "mechanisms": ["Klebenaht-Alterung", "Rahmendichtung schrumpft", "Scheibenrahmen korrodiert"], "prevention": "Regelmäßige Inspektion der Klebenaht, Dichtungstausch alle 10 Jahre", "inspection_interval_months": 12}, "wear_patterns": [{"location": "Windschutzscheibe", "cause": "Salzwasser, Scheibenwischer, UV", "prevention": "Weiche Wischerblätter, Süßwasserspülung", "inspection_interval_months": 6}], "environmental_limits": {"max_temp_c": 250, "min_temp_c": -60, "uv_resistance_hours": 100000, "salt_spray_resistance": "high", "humidity_tolerance": "100%"}, "galvanic_compatibility": {"compatible_with": ["alle"], "incompatible_with": [], "notes": "Glas ist nicht leitfähig"}, "recommended_zones": ["windows", "windscreen", "skylights", "portlights"]},
        "known_issues": ["Heavy; requires stronger frames", "More expensive than tempered", "Interlayer can yellow over time"],
        "alternatives": ["Sicherheitsglas gehärtet", "Polycarbonat", "Acrylglas"],
    },
    {
        "name": "Polycarbonat (Lightweight)",
        "category": "glass",
        "subcategory": "plastic_glazing",
        "manufacturer": "Various",
        "cost_per_unit": 45.0,
        "cost_unit": "sqm",
        "lifespan_years": 15,
        "maintenance_interval_months": 12,
        "maintenance_cost_factor": 0.02,
        "properties": {"polycarbonate": True, "lightweight": True, "impact_resistant": True, "uv_resistant": True, "easy_installation": True, "installation_methods": [{"method": "Eingeklebt mit PU-Kleber", "difficulty": "high", "tools_required": ["PU-Kleber", "Distanzstücke", "Saugnapfheber"], "typical_errors": ["Scheibe verkantet", "Klebenaht zu dünn", "Primer vergessen"]}, {"method": "Mechanisch gerahmt", "difficulty": "medium", "tools_required": ["Rahmen", "Schrauben", "EPDM-Dichtung"], "typical_errors": ["Dichtung falsch dimensioniert", "Schrauben zu fest"]}], "failure_modes": [{"mode": "Klebenaht-Versagen", "onset_years": 10, "severity": "high", "symptoms": "Scheibe löst sich, Wasser dringt ein", "prevention": "Richtige Klebstoffauswahl, UV-Schutz der Klebenaht", "zone_risk": ["windows", "windscreen"]}, {"mode": "Spannungsriss durch Temperaturschock", "onset_years": 0, "severity": "high", "symptoms": "Spontane Rissbildung bei schneller Temperaturänderung", "prevention": "ESG-Glas verwenden, keine Punktbelastung", "zone_risk": ["windows", "skylights"]}, {"mode": "Kratzer und Trübung", "onset_years": 5, "severity": "low", "symptoms": "Sichteinschränkung, Mikrokratzer", "prevention": "Weiche Reinigungsmittel, keine Scheibenwischer auf Salzwasser", "zone_risk": ["windscreen", "windows"]}], "water_ingress": {"risk_level": "high", "mechanisms": ["Klebenaht-Alterung", "Rahmendichtung schrumpft", "Scheibenrahmen korrodiert"], "prevention": "Regelmäßige Inspektion der Klebenaht, Dichtungstausch alle 10 Jahre", "inspection_interval_months": 12}, "wear_patterns": [{"location": "Windschutzscheibe", "cause": "Salzwasser, Scheibenwischer, UV", "prevention": "Weiche Wischerblätter, Süßwasserspülung", "inspection_interval_months": 6}], "environmental_limits": {"max_temp_c": 250, "min_temp_c": -60, "uv_resistance_hours": 100000, "salt_spray_resistance": "high", "humidity_tolerance": "100%"}, "galvanic_compatibility": {"compatible_with": ["alle"], "incompatible_with": [], "notes": "Glas ist nicht leitfähig"}, "recommended_zones": ["windows", "windscreen", "skylights", "portlights"]},
        "known_issues": ["Scratches easily; requires protective film", "Yellows with UV exposure", "Shorter lifespan vs glass"],
        "alternatives": ["Acrylglas", "Verbund-Sicherheitsglas", "Acrylic"],
    },
    {
        "name": "Acrylglas (Acrylic Plastic)",
        "category": "glass",
        "subcategory": "plastic_glazing",
        "manufacturer": "Various",
        "cost_per_unit": 38.0,
        "cost_unit": "sqm",
        "lifespan_years": 12,
        "maintenance_interval_months": 12,
        "maintenance_cost_factor": 0.03,
        "properties": {"acrylic": True, "lightweight": True, "optically_clear": True, "easy_fabrication": True, "hatch_compatible": True, "installation_methods": [{"method": "Eingeklebt mit PU-Kleber", "difficulty": "high", "tools_required": ["PU-Kleber", "Distanzstücke", "Saugnapfheber"], "typical_errors": ["Scheibe verkantet", "Klebenaht zu dünn", "Primer vergessen"]}, {"method": "Mechanisch gerahmt", "difficulty": "medium", "tools_required": ["Rahmen", "Schrauben", "EPDM-Dichtung"], "typical_errors": ["Dichtung falsch dimensioniert", "Schrauben zu fest"]}], "failure_modes": [{"mode": "Klebenaht-Versagen", "onset_years": 10, "severity": "high", "symptoms": "Scheibe löst sich, Wasser dringt ein", "prevention": "Richtige Klebstoffauswahl, UV-Schutz der Klebenaht", "zone_risk": ["windows", "windscreen"]}, {"mode": "Spannungsriss durch Temperaturschock", "onset_years": 0, "severity": "high", "symptoms": "Spontane Rissbildung bei schneller Temperaturänderung", "prevention": "ESG-Glas verwenden, keine Punktbelastung", "zone_risk": ["windows", "skylights"]}, {"mode": "Kratzer und Trübung", "onset_years": 5, "severity": "low", "symptoms": "Sichteinschränkung, Mikrokratzer", "prevention": "Weiche Reinigungsmittel, keine Scheibenwischer auf Salzwasser", "zone_risk": ["windscreen", "windows"]}], "water_ingress": {"risk_level": "high", "mechanisms": ["Klebenaht-Alterung", "Rahmendichtung schrumpft", "Scheibenrahmen korrodiert"], "prevention": "Regelmäßige Inspektion der Klebenaht, Dichtungstausch alle 10 Jahre", "inspection_interval_months": 12}, "wear_patterns": [{"location": "Windschutzscheibe", "cause": "Salzwasser, Scheibenwischer, UV", "prevention": "Weiche Wischerblätter, Süßwasserspülung", "inspection_interval_months": 6}], "environmental_limits": {"max_temp_c": 250, "min_temp_c": -60, "uv_resistance_hours": 100000, "salt_spray_resistance": "high", "humidity_tolerance": "100%"}, "galvanic_compatibility": {"compatible_with": ["alle"], "incompatible_with": [], "notes": "Glas ist nicht leitfähig"}, "recommended_zones": ["windows", "windscreen", "skylights", "portlights"]},
        "known_issues": ["Brittle; cracks easily under stress", "Scratches and clouds quickly", "Limited UV resistance"],
        "alternatives": ["Polycarbonat", "Verbund-Sicherheitsglas", "Polycarbonate sheets"],
    },
    {
        "name": "Armaflex (Closed-Cell Foam Insulation)",
        "category": "insulation",
        "subcategory": "foam_insulation",
        "manufacturer": "Armacell",
        "cost_per_unit": 22.0,
        "cost_unit": "sqm",
        "lifespan_years": 25,
        "maintenance_interval_months": 24,
        "maintenance_cost_factor": 0.01,
        "properties": {"closed_cell_foam": True, "thermal_conductivity_w_mk": 0.035, "fire_rated": True, "moisture_barrier": True, "flexible": True, "installation_methods": [{"method": "Verklebt mit Kontaktkleber", "difficulty": "low", "tools_required": ["Kontaktkleber", "Rolle", "Cuttermesser"], "typical_errors": ["Stöße nicht verklebt", "Dampfsperre vergessen"]}, {"method": "Mechanisch befestigt", "difficulty": "low", "tools_required": ["Tackerpistole", "Klebeband"], "typical_errors": ["Wärmebrücken an Befestigungen"]}], "failure_modes": [{"mode": "Feuchtigkeitsaufnahme", "onset_years": 3, "severity": "high", "symptoms": "Isolierung nass, Schimmelgeruch, Dämmwirkung verloren", "prevention": "Dampfsperre, geschlossenzellige Isolierung wählen", "zone_risk": ["hull_interior", "engine_room", "cabin"]}, {"mode": "Ablösung durch Vibration", "onset_years": 5, "severity": "low", "symptoms": "Isolierung fällt herunter", "prevention": "Zusätzliche mechanische Befestigung", "zone_risk": ["engine_room", "hull_interior"]}], "water_ingress": {"risk_level": "none", "mechanisms": [], "prevention": "N/A — Isolierung ist kein Strukturmaterial", "inspection_interval_months": 24}, "wear_patterns": [{"location": "Maschinenraum", "cause": "Vibration, Hitze, Öldämpfe", "prevention": "Ölbeständige Isolierung, mechanische Sicherung", "inspection_interval_months": 12}], "environmental_limits": {"max_temp_c": 120, "min_temp_c": -50, "uv_resistance_hours": 0, "salt_spray_resistance": "not_applicable", "humidity_tolerance": "geschlossene Zellen: 100%, offene Zellen: <70%"}, "galvanic_compatibility": {"compatible_with": ["alle"], "incompatible_with": [], "notes": "Nicht relevant"}, "recommended_zones": ["engine_room", "hull_interior", "cabin", "refrigeration"]},
        "known_issues": ["Can degrade under UV", "Moisture absorption if damaged", "Off-gassing possible"],
        "alternatives": ["Steinwolle Marine", "Thinsulate Marine", "PU spray foam"],
    },
    {
        "name": "Steinwolle Marine (Stone Wool - Fire-rated)",
        "category": "insulation",
        "subcategory": "mineral_wool",
        "manufacturer": "Various",
        "cost_per_unit": 18.0,
        "cost_unit": "sqm",
        "lifespan_years": 30,
        "maintenance_interval_months": 36,
        "maintenance_cost_factor": 0.01,
        "properties": {"stone_wool": True, "fire_rating": "A1", "thermal_conductivity_w_mk": 0.04, "breathable": True, "mold_resistant": True, "installation_methods": [{"method": "Verklebt mit Kontaktkleber", "difficulty": "low", "tools_required": ["Kontaktkleber", "Rolle", "Cuttermesser"], "typical_errors": ["Stöße nicht verklebt", "Dampfsperre vergessen"]}, {"method": "Mechanisch befestigt", "difficulty": "low", "tools_required": ["Tackerpistole", "Klebeband"], "typical_errors": ["Wärmebrücken an Befestigungen"]}], "failure_modes": [{"mode": "Feuchtigkeitsaufnahme", "onset_years": 3, "severity": "high", "symptoms": "Isolierung nass, Schimmelgeruch, Dämmwirkung verloren", "prevention": "Dampfsperre, geschlossenzellige Isolierung wählen", "zone_risk": ["hull_interior", "engine_room", "cabin"]}, {"mode": "Ablösung durch Vibration", "onset_years": 5, "severity": "low", "symptoms": "Isolierung fällt herunter", "prevention": "Zusätzliche mechanische Befestigung", "zone_risk": ["engine_room", "hull_interior"]}], "water_ingress": {"risk_level": "none", "mechanisms": [], "prevention": "N/A — Isolierung ist kein Strukturmaterial", "inspection_interval_months": 24}, "wear_patterns": [{"location": "Maschinenraum", "cause": "Vibration, Hitze, Öldämpfe", "prevention": "Ölbeständige Isolierung, mechanische Sicherung", "inspection_interval_months": 12}], "environmental_limits": {"max_temp_c": 120, "min_temp_c": -50, "uv_resistance_hours": 0, "salt_spray_resistance": "not_applicable", "humidity_tolerance": "geschlossene Zellen: 100%, offene Zellen: <70%"}, "galvanic_compatibility": {"compatible_with": ["alle"], "incompatible_with": [], "notes": "Nicht relevant"}, "recommended_zones": ["engine_room", "hull_interior", "cabin", "refrigeration"]},
        "known_issues": ["Irritating dust during installation", "Can settle over time", "Moisture issues if not sealed"],
        "alternatives": ["Armaflex", "Thinsulate Marine", "Polyurethane foam"],
    },
    {
        "name": "Thinsulate Marine (Acoustic & Thermal)",
        "category": "insulation",
        "subcategory": "synthetic_fiber",
        "manufacturer": "3M",
        "cost_per_unit": 25.0,
        "cost_unit": "sqm",
        "lifespan_years": 20,
        "maintenance_interval_months": 24,
        "maintenance_cost_factor": 0.01,
        "properties": {"microfiber": True, "thermal_conductivity_w_mk": 0.032, "acoustic_damping": True, "water_resistant": True, "lightweight": True, "installation_methods": [{"method": "Verklebt mit Kontaktkleber", "difficulty": "low", "tools_required": ["Kontaktkleber", "Rolle", "Cuttermesser"], "typical_errors": ["Stöße nicht verklebt", "Dampfsperre vergessen"]}, {"method": "Mechanisch befestigt", "difficulty": "low", "tools_required": ["Tackerpistole", "Klebeband"], "typical_errors": ["Wärmebrücken an Befestigungen"]}], "failure_modes": [{"mode": "Feuchtigkeitsaufnahme", "onset_years": 3, "severity": "high", "symptoms": "Isolierung nass, Schimmelgeruch, Dämmwirkung verloren", "prevention": "Dampfsperre, geschlossenzellige Isolierung wählen", "zone_risk": ["hull_interior", "engine_room", "cabin"]}, {"mode": "Ablösung durch Vibration", "onset_years": 5, "severity": "low", "symptoms": "Isolierung fällt herunter", "prevention": "Zusätzliche mechanische Befestigung", "zone_risk": ["engine_room", "hull_interior"]}], "water_ingress": {"risk_level": "none", "mechanisms": [], "prevention": "N/A — Isolierung ist kein Strukturmaterial", "inspection_interval_months": 24}, "wear_patterns": [{"location": "Maschinenraum", "cause": "Vibration, Hitze, Öldämpfe", "prevention": "Ölbeständige Isolierung, mechanische Sicherung", "inspection_interval_months": 12}], "environmental_limits": {"max_temp_c": 120, "min_temp_c": -50, "uv_resistance_hours": 0, "salt_spray_resistance": "not_applicable", "humidity_tolerance": "geschlossene Zellen: 100%, offene Zellen: <70%"}, "galvanic_compatibility": {"compatible_with": ["alle"], "incompatible_with": [], "notes": "Nicht relevant"}, "recommended_zones": ["engine_room", "hull_interior", "cabin", "refrigeration"]},
        "known_issues": ["Moisture can penetrate fibers", "Settling possible", "Specialty product; limited availability"],
        "alternatives": ["Armaflex", "Steinwolle Marine", "Polyurethane foam"],
    },
    {
        "name": "Spray-Schaum PU (Spray Polyurethane)",
        "category": "insulation",
        "subcategory": "spray_foam",
        "manufacturer": "Various",
        "cost_per_unit": 0.85,
        "cost_unit": "liter",
        "lifespan_years": 22,
        "maintenance_interval_months": 36,
        "maintenance_cost_factor": 0.01,
        "properties": {"polyurethane_foam": True, "thermal_conductivity_w_mk": 0.025, "custom_fit": True, "excellent_adhesion": True, "air_sealing": True, "installation_methods": [{"method": "Verklebt mit Kontaktkleber", "difficulty": "low", "tools_required": ["Kontaktkleber", "Rolle", "Cuttermesser"], "typical_errors": ["Stöße nicht verklebt", "Dampfsperre vergessen"]}, {"method": "Mechanisch befestigt", "difficulty": "low", "tools_required": ["Tackerpistole", "Klebeband"], "typical_errors": ["Wärmebrücken an Befestigungen"]}], "failure_modes": [{"mode": "Feuchtigkeitsaufnahme", "onset_years": 3, "severity": "high", "symptoms": "Isolierung nass, Schimmelgeruch, Dämmwirkung verloren", "prevention": "Dampfsperre, geschlossenzellige Isolierung wählen", "zone_risk": ["hull_interior", "engine_room", "cabin"]}, {"mode": "Ablösung durch Vibration", "onset_years": 5, "severity": "low", "symptoms": "Isolierung fällt herunter", "prevention": "Zusätzliche mechanische Befestigung", "zone_risk": ["engine_room", "hull_interior"]}], "water_ingress": {"risk_level": "none", "mechanisms": [], "prevention": "N/A — Isolierung ist kein Strukturmaterial", "inspection_interval_months": 24}, "wear_patterns": [{"location": "Maschinenraum", "cause": "Vibration, Hitze, Öldämpfe", "prevention": "Ölbeständige Isolierung, mechanische Sicherung", "inspection_interval_months": 12}], "environmental_limits": {"max_temp_c": 120, "min_temp_c": -50, "uv_resistance_hours": 0, "salt_spray_resistance": "not_applicable", "humidity_tolerance": "geschlossene Zellen: 100%, offene Zellen: <70%"}, "galvanic_compatibility": {"compatible_with": ["alle"], "incompatible_with": [], "notes": "Nicht relevant"}, "recommended_zones": ["engine_room", "hull_interior", "cabin", "refrigeration"]},
        "known_issues": ["VOC emissions; ventilation critical", "Over-expansion risk", "Difficult to remove once cured"],
        "alternatives": ["Armaflex", "Steinwolle Marine", "Pre-formed foam"],
    },
    {
        "name": "Marinekabel verzinnt (Marine Tinned Copper Wire)",
        "category": "electrical",
        "subcategory": "wiring",
        "manufacturer": "Various",
        "cost_per_unit": 12.5,
        "cost_unit": "meter",
        "lifespan_years": 20,
        "maintenance_interval_months": 24,
        "maintenance_cost_factor": 0.02,
        "properties": {"tinned_copper": True, "corrosion_resistant": True, "flexible": True, "insulated": True, "uv_resistant_jacket": True, "installation_methods": [{"method": "Verlegt in Kabelkanal", "difficulty": "medium", "tools_required": ["Kabelkanal", "Kabelbinder", "Crimpzange", "Schrumpfschlauch"], "typical_errors": ["Kabel zu eng verlegt", "Scharfe Kanten an Kabeldurchführungen", "Fehlende Zugentlastung"]}, {"method": "Direktverdrahtung mit Crimpverbindung", "difficulty": "medium", "tools_required": ["Crimpzange", "Verzinnte Kabelschuhe", "Schrumpfschlauch", "Multimeter"], "typical_errors": ["Kalte Crimpung", "Falscher Kabelschuh", "Kein Korrosionsschutz"]}], "failure_modes": [{"mode": "Korrosion an Verbindungen", "onset_years": 3, "severity": "high", "symptoms": "Grüne Ablagerungen, Spannungsabfall, Funkenbildung", "prevention": "Verzinnte Kabelschuhe, Wärme-Schrumpfschlauch mit Kleber", "zone_risk": ["engine_room", "bilge", "deck"]}, {"mode": "Kabelbruch durch Vibration", "onset_years": 5, "severity": "medium", "symptoms": "Intermittierende Ausfälle, Kabel bricht an Befestigung", "prevention": "Vibrationsdämpfer, Schlaufe an Durchführungen", "zone_risk": ["engine_room", "mast"]}, {"mode": "Kurzschluss durch Scheuern", "onset_years": 7, "severity": "critical", "symptoms": "Sicherung löst aus, Brandgeruch, Rauch", "prevention": "Kabelschutz an Durchführungen, scharfe Kanten entgraten", "zone_risk": ["engine_room", "bilge", "mast"]}], "water_ingress": {"risk_level": "medium", "mechanisms": ["Korrosion an Steckverbindungen", "Wasser in Kabelkanal", "Undichte Mastfuß-Durchführung"], "prevention": "Wasserdichte Stecker, Kabelkanal mit Gefälle verlegen, Mastfuß abdichten", "inspection_interval_months": 12}, "wear_patterns": [{"location": "Mastdurchführung", "cause": "Vibration, Bewegung des Mastes", "prevention": "Flexible Schlaufe, Kabelschutz", "inspection_interval_months": 12}, {"location": "Motorraum", "cause": "Hitze, Vibration, Öl", "prevention": "Hitzebeständige Kabel, Kabelbinder aus Metall", "inspection_interval_months": 6}], "environmental_limits": {"max_temp_c": 105, "min_temp_c": -40, "uv_resistance_hours": 2000, "salt_spray_resistance": "high_bei_verzinnung", "humidity_tolerance": "100% bei richtiger Isolierung"}, "galvanic_compatibility": {"compatible_with": ["verzinntes_kupfer", "edelstahl_klemmen"], "incompatible_with": ["aluminium_klemmen_auf_kupfer"], "notes": "Nur verzinnte Kabelschuhe und Klemmen im Marineeinsatz"}, "recommended_zones": ["engine_room", "navigation", "deck_lighting", "bilge", "mast"]},
        "known_issues": ["Salt water corrosion at connections", "Proper sealing of terminals critical", "Cost premium vs bare copper"],
        "alternatives": ["Bare copper (not marine)", "Nickel-plated copper", "Stainless-clad copper"],
    },
    {
        "name": "Edelstahl-Kabelkanal (Stainless Cable Tray)",
        "category": "electrical",
        "subcategory": "cable_management",
        "manufacturer": "Various",
        "cost_per_unit": 24.0,
        "cost_unit": "meter",
        "lifespan_years": 25,
        "maintenance_interval_months": 12,
        "maintenance_cost_factor": 0.01,
        "properties": {"stainless_steel_316l": True, "corrosion_resistant": True, "organized_routing": True, "accessible": True, "marine_grade": True, "installation_methods": [{"method": "Verlegt in Kabelkanal", "difficulty": "medium", "tools_required": ["Kabelkanal", "Kabelbinder", "Crimpzange", "Schrumpfschlauch"], "typical_errors": ["Kabel zu eng verlegt", "Scharfe Kanten an Kabeldurchführungen", "Fehlende Zugentlastung"]}, {"method": "Direktverdrahtung mit Crimpverbindung", "difficulty": "medium", "tools_required": ["Crimpzange", "Verzinnte Kabelschuhe", "Schrumpfschlauch", "Multimeter"], "typical_errors": ["Kalte Crimpung", "Falscher Kabelschuh", "Kein Korrosionsschutz"]}], "failure_modes": [{"mode": "Korrosion an Verbindungen", "onset_years": 3, "severity": "high", "symptoms": "Grüne Ablagerungen, Spannungsabfall, Funkenbildung", "prevention": "Verzinnte Kabelschuhe, Wärme-Schrumpfschlauch mit Kleber", "zone_risk": ["engine_room", "bilge", "deck"]}, {"mode": "Kabelbruch durch Vibration", "onset_years": 5, "severity": "medium", "symptoms": "Intermittierende Ausfälle, Kabel bricht an Befestigung", "prevention": "Vibrationsdämpfer, Schlaufe an Durchführungen", "zone_risk": ["engine_room", "mast"]}, {"mode": "Kurzschluss durch Scheuern", "onset_years": 7, "severity": "critical", "symptoms": "Sicherung löst aus, Brandgeruch, Rauch", "prevention": "Kabelschutz an Durchführungen, scharfe Kanten entgraten", "zone_risk": ["engine_room", "bilge", "mast"]}], "water_ingress": {"risk_level": "medium", "mechanisms": ["Korrosion an Steckverbindungen", "Wasser in Kabelkanal", "Undichte Mastfuß-Durchführung"], "prevention": "Wasserdichte Stecker, Kabelkanal mit Gefälle verlegen, Mastfuß abdichten", "inspection_interval_months": 12}, "wear_patterns": [{"location": "Mastdurchführung", "cause": "Vibration, Bewegung des Mastes", "prevention": "Flexible Schlaufe, Kabelschutz", "inspection_interval_months": 12}, {"location": "Motorraum", "cause": "Hitze, Vibration, Öl", "prevention": "Hitzebeständige Kabel, Kabelbinder aus Metall", "inspection_interval_months": 6}], "environmental_limits": {"max_temp_c": 105, "min_temp_c": -40, "uv_resistance_hours": 2000, "salt_spray_resistance": "high_bei_verzinnung", "humidity_tolerance": "100% bei richtiger Isolierung"}, "galvanic_compatibility": {"compatible_with": ["verzinntes_kupfer", "edelstahl_klemmen"], "incompatible_with": ["aluminium_klemmen_auf_kupfer"], "notes": "Nur verzinnte Kabelschuhe und Klemmen im Marineeinsatz"}, "recommended_zones": ["engine_room", "navigation", "deck_lighting", "bilge", "mast"]},
        "known_issues": ["Crevice corrosion possible", "Requires proper ventilation", "Higher cost than plastic"],
        "alternatives": ["Plastic conduit", "Aluminum tray", "Flexible hose"],
    },
    {
        "name": "LED-Marine-Beleuchtung (LED Marine Lighting)",
        "category": "electrical",
        "subcategory": "lighting",
        "manufacturer": "Various",
        "cost_per_unit": 35.0,
        "cost_unit": "piece",
        "lifespan_years": 12,
        "maintenance_interval_months": 24,
        "maintenance_cost_factor": 0.02,
        "properties": {"led": True, "low_power_consumption": True, "long_lifespan": True, "salt_spray_resistant": True, "dimmable": True, "installation_methods": [{"method": "Verlegt in Kabelkanal", "difficulty": "medium", "tools_required": ["Kabelkanal", "Kabelbinder", "Crimpzange", "Schrumpfschlauch"], "typical_errors": ["Kabel zu eng verlegt", "Scharfe Kanten an Kabeldurchführungen", "Fehlende Zugentlastung"]}, {"method": "Direktverdrahtung mit Crimpverbindung", "difficulty": "medium", "tools_required": ["Crimpzange", "Verzinnte Kabelschuhe", "Schrumpfschlauch", "Multimeter"], "typical_errors": ["Kalte Crimpung", "Falscher Kabelschuh", "Kein Korrosionsschutz"]}], "failure_modes": [{"mode": "Korrosion an Verbindungen", "onset_years": 3, "severity": "high", "symptoms": "Grüne Ablagerungen, Spannungsabfall, Funkenbildung", "prevention": "Verzinnte Kabelschuhe, Wärme-Schrumpfschlauch mit Kleber", "zone_risk": ["engine_room", "bilge", "deck"]}, {"mode": "Kabelbruch durch Vibration", "onset_years": 5, "severity": "medium", "symptoms": "Intermittierende Ausfälle, Kabel bricht an Befestigung", "prevention": "Vibrationsdämpfer, Schlaufe an Durchführungen", "zone_risk": ["engine_room", "mast"]}, {"mode": "Kurzschluss durch Scheuern", "onset_years": 7, "severity": "critical", "symptoms": "Sicherung löst aus, Brandgeruch, Rauch", "prevention": "Kabelschutz an Durchführungen, scharfe Kanten entgraten", "zone_risk": ["engine_room", "bilge", "mast"]}], "water_ingress": {"risk_level": "medium", "mechanisms": ["Korrosion an Steckverbindungen", "Wasser in Kabelkanal", "Undichte Mastfuß-Durchführung"], "prevention": "Wasserdichte Stecker, Kabelkanal mit Gefälle verlegen, Mastfuß abdichten", "inspection_interval_months": 12}, "wear_patterns": [{"location": "Mastdurchführung", "cause": "Vibration, Bewegung des Mastes", "prevention": "Flexible Schlaufe, Kabelschutz", "inspection_interval_months": 12}, {"location": "Motorraum", "cause": "Hitze, Vibration, Öl", "prevention": "Hitzebeständige Kabel, Kabelbinder aus Metall", "inspection_interval_months": 6}], "environmental_limits": {"max_temp_c": 105, "min_temp_c": -40, "uv_resistance_hours": 2000, "salt_spray_resistance": "high_bei_verzinnung", "humidity_tolerance": "100% bei richtiger Isolierung"}, "galvanic_compatibility": {"compatible_with": ["verzinntes_kupfer", "edelstahl_klemmen"], "incompatible_with": ["aluminium_klemmen_auf_kupfer"], "notes": "Nur verzinnte Kabelschuhe und Klemmen im Marineeinsatz"}, "recommended_zones": ["engine_room", "navigation", "deck_lighting", "bilge", "mast"]},
        "known_issues": ["Corrosion of fixtures possible", "Light quality variable by manufacturer", "Heat dissipation required"],
        "alternatives": ["Halogen marine lights", "Incandescent (obsolete)", "Fluorescent marine"],
    },
]

SEED_COMPETITORS = [
    # ===== small_sail (4 models, 6-9m) =====
    {
        "brand": "J Boats",
        "model_name": "J/70",
        "boat_class": "small_sail",
        "length_m": 6.93,
        "beam_m": 2.25,
        "year": 2023,
        "price_range_eur": {"min": 40000, "max": 50000},
        "key_metrics": {
            "cabin_count": 1,
            "berth_count": 4,
            "displacement_kg": 2200,
        },
        "source": "brochure",
        "notes": "One-design racer and daysailer, popular in international fleets",
    },
    {
        "brand": "Beneteau",
        "model_name": "First 24",
        "boat_class": "small_sail",
        "length_m": 7.27,
        "beam_m": 2.50,
        "year": 2023,
        "price_range_eur": {"min": 50000, "max": 60000},
        "key_metrics": {
            "cabin_count": 1,
            "berth_count": 4,
            "displacement_kg": 2500,
        },
        "source": "brochure",
        "notes": "Entry-level cruiser-racer, easy to handle",
    },
    {
        "brand": "Dehler",
        "model_name": "29",
        "boat_class": "small_sail",
        "length_m": 8.84,
        "beam_m": 2.99,
        "year": 2023,
        "price_range_eur": {"min": 110000, "max": 130000},
        "key_metrics": {
            "cabin_count": 1,
            "berth_count": 5,
            "displacement_kg": 3500,
        },
        "source": "brochure",
        "notes": "German construction, performance cruiser",
    },
    {
        "brand": "Bavaria",
        "model_name": "Easy 9.7",
        "boat_class": "small_sail",
        "length_m": 9.45,
        "beam_m": 3.28,
        "year": 2023,
        "price_range_eur": {"min": 120000, "max": 140000},
        "key_metrics": {
            "cabin_count": 1,
            "berth_count": 5,
            "displacement_kg": 3800,
        },
        "source": "brochure",
        "notes": "Easy-to-sail design with modern interior",
    },

    # ===== cruising_sail (keep existing 7, add 3 more, 12-16m) =====
    {
        "brand": "Bavaria",
        "model_name": "C42",
        "boat_class": "cruising_sail",
        "length_m": 12.35,
        "beam_m": 3.99,
        "year": 2023,
        "price_range_eur": {"min": 270000, "max": 300000},
        "key_metrics": {
            "cabin_count": 2,
            "berth_count": 6,
            "displacement_kg": 7800,
        },
        "source": "brochure",
    },
    {
        "brand": "Hanse",
        "model_name": "418",
        "boat_class": "cruising_sail",
        "length_m": 12.40,
        "beam_m": 4.17,
        "year": 2023,
        "price_range_eur": {"min": 255000, "max": 280000},
        "key_metrics": {
            "cabin_count": 2,
            "berth_count": 6,
            "displacement_kg": 8200,
        },
        "source": "brochure",
    },
    {
        "brand": "Jeanneau",
        "model_name": "Sun Odyssey 440",
        "boat_class": "cruising_sail",
        "length_m": 13.39,
        "beam_m": 4.29,
        "year": 2023,
        "price_range_eur": {"min": 280000, "max": 320000},
        "key_metrics": {
            "cabin_count": 2,
            "berth_count": 7,
            "displacement_kg": 9500,
        },
        "source": "brochure",
    },
    {
        "brand": "Beneteau",
        "model_name": "Oceanis 40.1",
        "boat_class": "cruising_sail",
        "length_m": 12.87,
        "beam_m": 4.18,
        "year": 2023,
        "price_range_eur": {"min": 230000, "max": 270000},
        "key_metrics": {
            "cabin_count": 2,
            "berth_count": 6,
            "displacement_kg": 8500,
        },
        "source": "brochure",
    },
    {
        "brand": "Dehler",
        "model_name": "42",
        "boat_class": "cruising_sail",
        "length_m": 12.88,
        "beam_m": 4.18,
        "year": 2023,
        "price_range_eur": {"min": 300000, "max": 350000},
        "key_metrics": {
            "cabin_count": 2,
            "berth_count": 6,
            "displacement_kg": 8700,
        },
        "source": "brochure",
    },
    {
        "brand": "Hallberg-Rassy",
        "model_name": "40",
        "boat_class": "cruising_sail",
        "length_m": 12.10,
        "beam_m": 3.95,
        "year": 2023,
        "price_range_eur": {"min": 320000, "max": 380000},
        "key_metrics": {
            "cabin_count": 2,
            "berth_count": 6,
            "displacement_kg": 8900,
        },
        "source": "brochure",
    },
    {
        "brand": "Garcia",
        "model_name": "Exploration 45",
        "boat_class": "cruising_sail",
        "length_m": 13.65,
        "beam_m": 4.45,
        "year": 2023,
        "price_range_eur": {"min": 350000, "max": 420000},
        "key_metrics": {
            "cabin_count": 3,
            "berth_count": 8,
            "displacement_kg": 10200,
        },
        "source": "brochure",
    },
    # 3 new cruising_sail
    {
        "brand": "X-Yachts",
        "model_name": "X4.3",
        "boat_class": "cruising_sail",
        "length_m": 13.09,
        "beam_m": 4.13,
        "year": 2023,
        "price_range_eur": {"min": 320000, "max": 380000},
        "key_metrics": {
            "cabin_count": 2,
            "berth_count": 6,
            "displacement_kg": 8800,
        },
        "source": "brochure",
        "notes": "Danish construction, excellent seaworthiness",
    },
    {
        "brand": "Najad",
        "model_name": "395",
        "boat_class": "cruising_sail",
        "length_m": 12.22,
        "beam_m": 3.82,
        "year": 2023,
        "price_range_eur": {"min": 350000, "max": 420000},
        "key_metrics": {
            "cabin_count": 2,
            "berth_count": 6,
            "displacement_kg": 8400,
        },
        "source": "brochure",
        "notes": "Swedish quality, high end interior",
    },
    {
        "brand": "Contest",
        "model_name": "42CS",
        "boat_class": "cruising_sail",
        "length_m": 12.85,
        "beam_m": 4.08,
        "year": 2023,
        "price_range_eur": {"min": 380000, "max": 460000},
        "key_metrics": {
            "cabin_count": 2,
            "berth_count": 7,
            "displacement_kg": 9100,
        },
        "source": "brochure",
        "notes": "Dutch constructor, excellent safety features",
    },

    # ===== racing_sail (4 models, 10-15m) =====
    {
        "brand": "J Boats",
        "model_name": "J/111",
        "boat_class": "racing_sail",
        "length_m": 11.10,
        "beam_m": 3.39,
        "year": 2023,
        "price_range_eur": {"min": 230000, "max": 270000},
        "key_metrics": {
            "cabin_count": 1,
            "berth_count": 5,
            "displacement_kg": 4200,
        },
        "source": "brochure",
        "notes": "One-design racer, competitive fleet racing",
    },
    {
        "brand": "Pogo",
        "model_name": "36",
        "boat_class": "racing_sail",
        "length_m": 10.87,
        "beam_m": 3.56,
        "year": 2023,
        "price_range_eur": {"min": 180000, "max": 220000},
        "key_metrics": {
            "cabin_count": 1,
            "berth_count": 5,
            "displacement_kg": 3900,
        },
        "source": "brochure",
        "notes": "French design, fast and fun racer",
    },
    {
        "brand": "ClubSwan",
        "model_name": "36",
        "boat_class": "racing_sail",
        "length_m": 11.31,
        "beam_m": 3.25,
        "year": 2023,
        "price_range_eur": {"min": 260000, "max": 300000},
        "key_metrics": {
            "cabin_count": 1,
            "berth_count": 5,
            "displacement_kg": 4500,
        },
        "source": "brochure",
        "notes": "Maxi yacht club racing, premium design",
    },
    {
        "brand": "Beneteau",
        "model_name": "Figaro 3",
        "boat_class": "racing_sail",
        "length_m": 10.04,
        "beam_m": 3.40,
        "year": 2023,
        "price_range_eur": {"min": 170000, "max": 210000},
        "key_metrics": {
            "cabin_count": 1,
            "berth_count": 4,
            "displacement_kg": 3600,
        },
        "source": "brochure",
        "notes": "Professional solo racing class",
    },

    # ===== daysailer (3 models) =====
    {
        "brand": "Saffier",
        "model_name": "SE 33",
        "boat_class": "daysailer",
        "length_m": 10.10,
        "beam_m": 3.20,
        "year": 2023,
        "price_range_eur": {"min": 250000, "max": 310000},
        "key_metrics": {
            "cabin_count": 1,
            "berth_count": 5,
            "displacement_kg": 4000,
        },
        "source": "brochure",
        "notes": "Dutch daysailer, perfect for weekends",
    },
    {
        "brand": "Eagle",
        "model_name": "44",
        "boat_class": "daysailer",
        "length_m": 13.50,
        "beam_m": 3.50,
        "year": 2023,
        "price_range_eur": {"min": 420000, "max": 480000},
        "key_metrics": {
            "cabin_count": 1,
            "berth_count": 6,
            "displacement_kg": 5800,
        },
        "source": "brochure",
        "notes": "Fast daysailer with large cockpit",
    },
    {
        "brand": "Spirit",
        "model_name": "46",
        "boat_class": "daysailer",
        "length_m": 14.10,
        "beam_m": 3.30,
        "year": 2023,
        "price_range_eur": {"min": 800000, "max": 900000},
        "key_metrics": {
            "cabin_count": 1,
            "berth_count": 6,
            "displacement_kg": 6200,
        },
        "source": "brochure",
        "notes": "Large modern daysailer, open cockpit",
    },

    # ===== motorsailer (3 models) =====
    {
        "brand": "Nauticat",
        "model_name": "42",
        "boat_class": "motorsailer",
        "length_m": 12.80,
        "beam_m": 3.90,
        "year": 2023,
        "price_range_eur": {"min": 320000, "max": 380000},
        "key_metrics": {
            "cabin_count": 2,
            "berth_count": 6,
            "displacement_kg": 8500,
        },
        "source": "brochure",
        "notes": "Finnish expedition motorsailer",
    },
    {
        "brand": "Fisher",
        "model_name": "37",
        "boat_class": "motorsailer",
        "length_m": 11.25,
        "beam_m": 3.55,
        "year": 2023,
        "price_range_eur": {"min": 180000, "max": 220000},
        "key_metrics": {
            "cabin_count": 1,
            "berth_count": 5,
            "displacement_kg": 6500,
        },
        "source": "brochure",
        "notes": "British motorsailer, practical design",
    },
    {
        "brand": "Malo",
        "model_name": "46",
        "boat_class": "motorsailer",
        "length_m": 14.00,
        "beam_m": 4.23,
        "year": 2023,
        "price_range_eur": {"min": 500000, "max": 600000},
        "key_metrics": {
            "cabin_count": 2,
            "berth_count": 7,
            "displacement_kg": 10000,
        },
        "source": "brochure",
        "notes": "Finnish expedition motorsailer, high quality",
    },

    # ===== catamaran_sail (4 models) =====
    {
        "brand": "Lagoon",
        "model_name": "42",
        "boat_class": "catamaran_sail",
        "length_m": 12.80,
        "beam_m": 7.70,
        "year": 2023,
        "price_range_eur": {"min": 340000, "max": 420000},
        "key_metrics": {
            "cabin_count": 2,
            "berth_count": 8,
            "displacement_kg": 13000,
        },
        "source": "brochure",
        "notes": "Popular cruising catamaran",
    },
    {
        "brand": "Fountaine Pajot",
        "model_name": "Elba 45",
        "boat_class": "catamaran_sail",
        "length_m": 13.41,
        "beam_m": 7.67,
        "year": 2023,
        "price_range_eur": {"min": 440000, "max": 520000},
        "key_metrics": {
            "cabin_count": 3,
            "berth_count": 8,
            "displacement_kg": 14500,
        },
        "source": "brochure",
        "notes": "French luxury catamaran",
    },
    {
        "brand": "Leopard",
        "model_name": "45",
        "boat_class": "catamaran_sail",
        "length_m": 13.72,
        "beam_m": 7.74,
        "year": 2023,
        "price_range_eur": {"min": 380000, "max": 460000},
        "key_metrics": {
            "cabin_count": 3,
            "berth_count": 8,
            "displacement_kg": 14200,
        },
        "source": "brochure",
        "notes": "South African design",
    },
    {
        "brand": "Catana",
        "model_name": "53",
        "boat_class": "catamaran_sail",
        "length_m": 15.84,
        "beam_m": 8.20,
        "year": 2023,
        "price_range_eur": {"min": 800000, "max": 900000},
        "key_metrics": {
            "cabin_count": 3,
            "berth_count": 10,
            "displacement_kg": 18000,
        },
        "source": "brochure",
        "notes": "Large luxury catamaran",
    },

    # ===== catamaran_motor (3 models) =====
    {
        "brand": "Leopard",
        "model_name": "43 Powercat",
        "boat_class": "catamaran_motor",
        "length_m": 13.14,
        "beam_m": 7.50,
        "year": 2023,
        "price_range_eur": {"min": 480000, "max": 560000},
        "key_metrics": {
            "cabin_count": 2,
            "berth_count": 8,
            "displacement_kg": 13500,
        },
        "source": "brochure",
        "notes": "Power catamaran variant",
    },
    {
        "brand": "Fountaine Pajot",
        "model_name": "MY 44",
        "boat_class": "catamaran_motor",
        "length_m": 13.30,
        "beam_m": 7.22,
        "year": 2023,
        "price_range_eur": {"min": 540000, "max": 620000},
        "key_metrics": {
            "cabin_count": 2,
            "berth_count": 8,
            "displacement_kg": 14000,
        },
        "source": "brochure",
        "notes": "French motor catamaran",
    },
    {
        "brand": "Aquila",
        "model_name": "44",
        "boat_class": "catamaran_motor",
        "length_m": 13.40,
        "beam_m": 7.34,
        "year": 2023,
        "price_range_eur": {"min": 500000, "max": 600000},
        "key_metrics": {
            "cabin_count": 2,
            "berth_count": 8,
            "displacement_kg": 13800,
        },
        "source": "brochure",
        "notes": "Australian motor catamaran",
    },

    # ===== small_motor (3 models, 6-10m) =====
    {
        "brand": "Axopar",
        "model_name": "37",
        "boat_class": "small_motor",
        "length_m": 11.00,
        "beam_m": 3.15,
        "year": 2023,
        "price_range_eur": {"min": 250000, "max": 310000},
        "key_metrics": {
            "cabin_count": 1,
            "berth_count": 5,
            "displacement_kg": 5200,
        },
        "source": "brochure",
        "notes": "Finnish speedboat, hard top cabin",
    },
    {
        "brand": "Nimbus",
        "model_name": "C9",
        "boat_class": "small_motor",
        "length_m": 9.22,
        "beam_m": 3.02,
        "year": 2023,
        "price_range_eur": {"min": 200000, "max": 240000},
        "key_metrics": {
            "cabin_count": 1,
            "berth_count": 4,
            "displacement_kg": 3800,
        },
        "source": "brochure",
        "notes": "Swedish design, modern styling",
    },
    {
        "brand": "Boston Whaler",
        "model_name": "280",
        "boat_class": "small_motor",
        "length_m": 8.60,
        "beam_m": 2.74,
        "year": 2023,
        "price_range_eur": {"min": 160000, "max": 200000},
        "key_metrics": {
            "cabin_count": 0,
            "berth_count": 4,
            "displacement_kg": 2900,
        },
        "source": "brochure",
        "notes": "American classic, center console",
    },

    # ===== large_motor (4 models, 12-24m) =====
    {
        "brand": "Princess",
        "model_name": "V55",
        "boat_class": "large_motor",
        "length_m": 17.00,
        "beam_m": 4.57,
        "year": 2023,
        "price_range_eur": {"min": 1100000, "max": 1300000},
        "key_metrics": {
            "cabin_count": 2,
            "berth_count": 6,
            "displacement_kg": 22000,
        },
        "source": "brochure",
        "notes": "British motor yacht, luxury interior",
    },
    {
        "brand": "Fairline",
        "model_name": "Squadron 53",
        "boat_class": "large_motor",
        "length_m": 16.30,
        "beam_m": 4.50,
        "year": 2023,
        "price_range_eur": {"min": 900000, "max": 1100000},
        "key_metrics": {
            "cabin_count": 2,
            "berth_count": 6,
            "displacement_kg": 20000,
        },
        "source": "brochure",
        "notes": "British trawler-style yacht",
    },
    {
        "brand": "Sunseeker",
        "model_name": "Manhattan 55",
        "boat_class": "large_motor",
        "length_m": 17.46,
        "beam_m": 4.64,
        "year": 2023,
        "price_range_eur": {"min": 1200000, "max": 1400000},
        "key_metrics": {
            "cabin_count": 2,
            "berth_count": 6,
            "displacement_kg": 23000,
        },
        "source": "brochure",
        "notes": "British power yacht, sporty design",
    },
    {
        "brand": "Azimut",
        "model_name": "60 Fly",
        "boat_class": "large_motor",
        "length_m": 18.70,
        "beam_m": 4.97,
        "year": 2023,
        "price_range_eur": {"min": 1400000, "max": 1600000},
        "key_metrics": {
            "cabin_count": 3,
            "berth_count": 7,
            "displacement_kg": 25000,
        },
        "source": "brochure",
        "notes": "Italian luxury yacht, flybridge",
    },

    # ===== sport_cruiser (3 models) =====
    {
        "brand": "Fjord",
        "model_name": "44",
        "boat_class": "sport_cruiser",
        "length_m": 13.74,
        "beam_m": 4.28,
        "year": 2023,
        "price_range_eur": {"min": 600000, "max": 700000},
        "key_metrics": {
            "cabin_count": 2,
            "berth_count": 6,
            "displacement_kg": 10500,
        },
        "source": "brochure",
        "notes": "Norwegian sport cruiser",
    },
    {
        "brand": "De Antonio",
        "model_name": "D46",
        "boat_class": "sport_cruiser",
        "length_m": 14.00,
        "beam_m": 4.20,
        "year": 2023,
        "price_range_eur": {"min": 500000, "max": 600000},
        "key_metrics": {
            "cabin_count": 2,
            "berth_count": 6,
            "displacement_kg": 10200,
        },
        "source": "brochure",
        "notes": "Spanish open boat design",
    },
    {
        "brand": "Wellcraft",
        "model_name": "355",
        "boat_class": "sport_cruiser",
        "length_m": 10.77,
        "beam_m": 3.35,
        "year": 2023,
        "price_range_eur": {"min": 320000, "max": 380000},
        "key_metrics": {
            "cabin_count": 1,
            "berth_count": 5,
            "displacement_kg": 4800,
        },
        "source": "brochure",
        "notes": "American open cruiser",
    },

    # ===== trawler (3 models) =====
    {
        "brand": "Nordhavn",
        "model_name": "41",
        "boat_class": "trawler",
        "length_m": 12.54,
        "beam_m": 4.42,
        "year": 2023,
        "price_range_eur": {"min": 600000, "max": 700000},
        "key_metrics": {
            "cabin_count": 2,
            "berth_count": 6,
            "displacement_kg": 9800,
        },
        "source": "brochure",
        "notes": "American ocean trawler",
    },
    {
        "brand": "Beneteau",
        "model_name": "Swift Trawler 41",
        "boat_class": "trawler",
        "length_m": 12.35,
        "beam_m": 4.15,
        "year": 2023,
        "price_range_eur": {"min": 380000, "max": 460000},
        "key_metrics": {
            "cabin_count": 2,
            "berth_count": 6,
            "displacement_kg": 9200,
        },
        "source": "brochure",
        "notes": "French trawler, fuel efficient",
    },
    {
        "brand": "Fleming",
        "model_name": "55",
        "boat_class": "trawler",
        "length_m": 16.76,
        "beam_m": 4.88,
        "year": 2023,
        "price_range_eur": {"min": 1700000, "max": 1900000},
        "key_metrics": {
            "cabin_count": 3,
            "berth_count": 7,
            "displacement_kg": 18000,
        },
        "source": "brochure",
        "notes": "Taiwanese expedition trawler",
    },

    # ===== explorer (3 models) =====
    {
        "brand": "Arksen",
        "model_name": "85",
        "boat_class": "explorer",
        "length_m": 25.50,
        "beam_m": 7.20,
        "year": 2023,
        "price_range_eur": {"min": 4500000, "max": 5500000},
        "key_metrics": {
            "cabin_count": 3,
            "berth_count": 8,
            "displacement_kg": 45000,
        },
        "source": "brochure",
        "notes": "Expedition explorer with ice class",
    },
    {
        "brand": "Bering",
        "model_name": "65",
        "boat_class": "explorer",
        "length_m": 19.50,
        "beam_m": 5.50,
        "year": 2023,
        "price_range_eur": {"min": 2300000, "max": 2700000},
        "key_metrics": {
            "cabin_count": 3,
            "berth_count": 8,
            "displacement_kg": 24000,
        },
        "source": "brochure",
        "notes": "German expedition trawler",
    },
    {
        "brand": "Garcia",
        "model_name": "Exploration 52",
        "boat_class": "explorer",
        "length_m": 15.90,
        "beam_m": 4.75,
        "year": 2023,
        "price_range_eur": {"min": 900000, "max": 1100000},
        "key_metrics": {
            "cabin_count": 2,
            "berth_count": 6,
            "displacement_kg": 12500,
        },
        "source": "brochure",
        "notes": "Expedition sailing yacht",
    },

    # ===== superyacht (3 models, 24m+) =====
    {
        "brand": "Benetti",
        "model_name": "Oasis 40m",
        "boat_class": "superyacht",
        "length_m": 40.00,
        "beam_m": 8.50,
        "year": 2023,
        "price_range_eur": {"min": 16000000, "max": 20000000},
        "key_metrics": {
            "cabin_count": 4,
            "berth_count": 10,
            "displacement_kg": 500000,
        },
        "source": "brochure",
        "notes": "Italian superyacht builder, custom",
    },
    {
        "brand": "Sanlorenzo",
        "model_name": "SL106",
        "boat_class": "superyacht",
        "length_m": 32.50,
        "beam_m": 7.10,
        "year": 2023,
        "price_range_eur": {"min": 11000000, "max": 13000000},
        "key_metrics": {
            "cabin_count": 3,
            "berth_count": 8,
            "displacement_kg": 320000,
        },
        "source": "brochure",
        "notes": "Italian custom superyacht",
    },
    {
        "brand": "Ferretti",
        "model_name": "1000",
        "boat_class": "superyacht",
        "length_m": 30.30,
        "beam_m": 7.00,
        "year": 2023,
        "price_range_eur": {"min": 9000000, "max": 11000000},
        "key_metrics": {
            "cabin_count": 3,
            "berth_count": 8,
            "displacement_kg": 280000,
        },
        "source": "brochure",
        "notes": "Italian luxury motor yacht",
    },
]


async def seed():
    # Create tables first
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)

    async with async_session() as session:
        result = await session.execute(select(Project))
        if result.scalars().first():
            print("Seed data already exists, skipping.")
            return

        # Seed materials
        for mat_data in SEED_MATERIALS:
            material = Material(**mat_data)
            session.add(material)

        # Seed competitors
        for comp_data in SEED_COMPETITORS:
            competitor = CompetitorModel(**comp_data)
            session.add(competitor)

        projects = []
        for data in SEED_PROJECTS:
            project = Project(**data)
            session.add(project)
            projects.append(project)

        await session.flush()

        meridian = projects[0]
        layout = Layout(
            project_id=meridian.id,
            name="Hauptdeck v1.0",
            version="v1.0",
            file_type="json",
            zones=MERIDIAN_ZONES,
            passages=MERIDIAN_PASSAGES,
            deck_height_mm=1950,
        )
        session.add(layout)

        await session.commit()
        print(f"Seeded {len(SEED_MATERIALS)} materials, {len(SEED_COMPETITORS)} competitors, {len(projects)} projects and 1 layout.")

        await seed_community_data(session)


async def seed_community_data(db):
    """Seed realistic community reports and run aggregation."""
    from app.models.models import CommunityReport, CommunityPattern
    from app.services.community.aggregator import aggregate_reports_to_patterns

    # Check if data already exists
    result = await db.execute(select(CommunityReport).limit(1))
    if result.scalar_one_or_none():
        logger.info("Community data already seeded")
        return

    reports_data = [
        # Bavaria 38 — Osmose (5 reports)
        *[{
            "source_forum": forum,
            "boat_manufacturer": "Bavaria",
            "boat_model": "38 Cruiser",
            "boat_year": 2015 + i,
            "hull_material": "grp_solid",
            "hull_construction": "hand_layup",
            "propulsion": "sail",
            "issues": [{
                "category": "material_degradation",
                "zone_type": "hull",
                "description": "Osmoseblasen am Unterwasserschiff",
                "severity": "major",
                "boat_age_months": 60 + i * 12,
            }],
            "positives": [],
            "reliability": 0.8 + i * 0.02,
        } for i, forum in enumerate([
            "boote-forum.de", "segeln-forum.de", "cruisersforum.com",
            "boote-forum.de", "sailboatowners.com",
        ])],

        # Bavaria 38 — Hull/deck fastener loosening (4 reports)
        *[{
            "source_forum": forum,
            "boat_manufacturer": "Bavaria",
            "boat_model": "38 Cruiser",
            "boat_year": 2014 + i,
            "hull_material": "grp_solid",
            "hull_construction": "hand_layup",
            "propulsion": "sail",
            "issues": [{
                "category": "structural",
                "zone_type": "deck",
                "description": "Rumpf/Deck-Verschraubung lockert nach 5-8 Jahren",
                "severity": "major",
                "boat_age_months": 60 + i * 6,
            }],
            "positives": [],
            "reliability": 0.75 + i * 0.05,
        } for i, forum in enumerate([
            "boote-forum.de", "segeln-forum.de", "cruisersforum.com", "boote-forum.de",
        ])],

        # Hanse 415 — Railing loosening (3 reports)
        *[{
            "source_forum": forum,
            "boat_manufacturer": "Hanse",
            "boat_model": "415",
            "boat_year": 2017,
            "hull_material": "grp_solid",
            "hull_construction": "hand_layup",
            "propulsion": "sail",
            "issues": [{
                "category": "hardware",
                "zone_type": "deck",
                "description": "Relingstützen lockern sich nach 3-5 Jahren",
                "severity": "minor",
                "boat_age_months": 36 + i * 12,
            }],
            "positives": [],
            "reliability": 0.7,
        } for i, forum in enumerate([
            "segeln-forum.de", "boote-forum.de", "myhanse.com",
        ])],

        # Hanse 415 — Galley countertop (3 reports)
        *[{
            "source_forum": forum,
            "boat_manufacturer": "Hanse",
            "boat_model": "415",
            "boat_year": 2018,
            "hull_material": "grp_solid",
            "hull_construction": "hand_layup",
            "propulsion": "sail",
            "issues": [{
                "category": "material_degradation",
                "zone_type": "galley",
                "description": "Arbeitsplatten splittern an Kanten",
                "severity": "cosmetic",
                "boat_age_months": 12 + i * 6,
            }],
            "positives": [],
            "reliability": 0.65,
        } for i, forum in enumerate([
            "myhanse.com", "boote-forum.de", "segeln-forum.de",
        ])],

        # Hallberg-Rassy 40 — Positive: keel (3 reports)
        *[{
            "source_forum": forum,
            "boat_manufacturer": "Hallberg-Rassy",
            "boat_model": "40",
            "boat_year": 2016,
            "hull_material": "grp_solid",
            "hull_construction": "hand_layup",
            "propulsion": "sail",
            "issues": [],
            "positives": [{
                "category": "structural",
                "zone_type": "hull",
                "description": "Kielstruktur direkt laminiert — von Gutachtern besser bewertet als modular",
            }],
            "reliability": 0.9,
        } for forum in [
            "segeln-forum.de", "cruisersforum.com", "ybw.com",
        ]],

        # Cross-manufacturer GRP hand_layup — Print-through (4 reports from 3+ mfrs)
        *[{
            "source_forum": "boote-forum.de",
            "boat_manufacturer": mfr,
            "boat_model": None,
            "boat_year": 2016,
            "hull_material": "grp_solid",
            "hull_construction": "hand_layup",
            "propulsion": "sail",
            "issues": [{
                "category": "cosmetic",
                "zone_type": "hull",
                "description": "Print-through der Gewebestruktur sichtbar",
                "severity": "cosmetic",
                "boat_age_months": 36 + i * 12,
            }],
            "positives": [],
            "reliability": 0.7,
        } for i, mfr in enumerate([
            "Bavaria", "Hanse", "Jeanneau", "Dufour",
        ])],

        # Jeanneau Sun Odyssey — Chainplate cracks (3 reports)
        *[{
            "source_forum": forum,
            "boat_manufacturer": "Jeanneau",
            "boat_model": "Sun Odyssey 410",
            "boat_year": 2012 + i,
            "hull_material": "grp_solid",
            "hull_construction": "hand_layup",
            "propulsion": "sail",
            "issues": [{
                "category": "structural",
                "zone_type": "rigging",
                "description": "Haarrisse an Wantenplatten nach 8-12 Jahren",
                "severity": "critical",
                "boat_age_months": 96 + i * 12,
            }],
            "positives": [],
            "reliability": 0.85,
        } for i, forum in enumerate([
            "cruisersforum.com", "segeln-forum.de", "sailboatowners.com",
        ])],

        # Bavaria general — Positive: price/value (3 reports)
        *[{
            "source_forum": forum,
            "boat_manufacturer": "Bavaria",
            "boat_model": None,
            "boat_year": None,
            "hull_material": "grp_solid",
            "hull_construction": "hand_layup",
            "propulsion": "sail",
            "issues": [],
            "positives": [{
                "category": "design_flaw",
                "zone_type": "cabin",
                "description": "Gutes Preis-Leistungs-Verhältnis für Innenraum und Ausstattung",
            }],
            "reliability": 0.7,
        } for forum in [
            "boote-forum.de", "segeln-forum.de", "boote-forum.de",
        ]],

        # Bavaria 38 Cruiser — Deck/mast step issues (6 additional reports)
        *[{
            "source_forum": forum,
            "boat_manufacturer": "Bavaria",
            "boat_model": "38 Cruiser",
            "boat_year": 2013 + i,
            "hull_material": "grp_solid",
            "hull_construction": "hand_layup",
            "propulsion": "sail",
            "issues": [{
                "category": "structural",
                "zone_type": "deck",
                "description": "Mastschritt zeigt Risse bei schwerem Wind und Seegang",
                "severity": "major",
                "boat_age_months": 84 + i * 12,
            }],
            "positives": [],
            "reliability": 0.72 + i * 0.03,
        } for i, forum in enumerate([
            "segeln-forum.de", "boote-forum.de", "cruisersforum.com",
            "sailboatowners.com", "segeln-forum.de", "boote-forum.de",
        ])],

        # Bavaria C42 — Rudder bearing issues (4 reports)
        *[{
            "source_forum": forum,
            "boat_manufacturer": "Bavaria",
            "boat_model": "C42",
            "boat_year": 2014 + i,
            "hull_material": "grp_solid",
            "hull_construction": "hand_layup",
            "propulsion": "sail",
            "issues": [{
                "category": "hardware",
                "zone_type": "hull",
                "description": "Ruderlagerung verschleißt nach 8-10 Jahren, Spiel wird immer größer",
                "severity": "major",
                "boat_age_months": 96 + i * 12,
            }],
            "positives": [],
            "reliability": 0.7 + i * 0.04,
        } for i, forum in enumerate([
            "boote-forum.de", "segeln-forum.de", "cruisersforum.com", "ybw.com",
        ])],

        # Bavaria C42 — Keel bolt corrosion (2 reports)
        *[{
            "source_forum": forum,
            "boat_manufacturer": "Bavaria",
            "boat_model": "C42",
            "boat_year": 2013 + i,
            "hull_material": "grp_solid",
            "hull_construction": "hand_layup",
            "propulsion": "sail",
            "issues": [{
                "category": "material_degradation",
                "zone_type": "hull",
                "description": "Kielbefestigungsschrauben rosten trotz Inspektionen nach 8-10 Jahren",
                "severity": "critical",
                "boat_age_months": 120 + i * 6,
            }],
            "positives": [],
            "reliability": 0.65 + i * 0.05,
        } for i, forum in enumerate([
            "segeln-forum.de", "boote-forum.de",
        ])],

        # Hanse 415 — Chainplate delamination (3 reports)
        *[{
            "source_forum": forum,
            "boat_manufacturer": "Hanse",
            "boat_model": "415",
            "boat_year": 2015 + i,
            "hull_material": "grp_solid",
            "hull_construction": "hand_layup",
            "propulsion": "sail",
            "issues": [{
                "category": "material_degradation",
                "zone_type": "rigging",
                "description": "Wantenplatte delaminialisiert nach 5-6 Jahren unter Belastung",
                "severity": "major",
                "boat_age_months": 60 + i * 12,
            }],
            "positives": [],
            "reliability": 0.68 + i * 0.04,
        } for i, forum in enumerate([
            "segeln-forum.de", "myhanse.com", "boote-forum.de",
        ])],

        # Hanse 415 — Window leaks (3 reports)
        *[{
            "source_forum": forum,
            "boat_manufacturer": "Hanse",
            "boat_model": "415",
            "boat_year": 2016 + i,
            "hull_material": "grp_solid",
            "hull_construction": "hand_layup",
            "propulsion": "sail",
            "issues": [{
                "category": "hardware",
                "zone_type": "cabin",
                "description": "Fensterrahmen zeigen undichte Stellen nach 3-4 Jahren",
                "severity": "minor",
                "boat_age_months": 48 + i * 12,
            }],
            "positives": [],
            "reliability": 0.72 + i * 0.03,
        } for i, forum in enumerate([
            "myhanse.com", "segeln-forum.de", "cruisersforum.com",
        ])],

        # Hanse 460 — Steering cable wear (3 reports)
        *[{
            "source_forum": forum,
            "boat_manufacturer": "Hanse",
            "boat_model": "460",
            "boat_year": 2014 + i,
            "hull_material": "grp_solid",
            "hull_construction": "hand_layup",
            "propulsion": "sail",
            "issues": [{
                "category": "hardware",
                "zone_type": "deck",
                "description": "Steuerkabel zeigen Verschleiß an den Rollen nach 7-9 Jahren",
                "severity": "major",
                "boat_age_months": 84 + i * 12,
            }],
            "positives": [],
            "reliability": 0.7 + i * 0.03,
        } for i, forum in enumerate([
            "boote-forum.de", "segeln-forum.de", "myhanse.com",
        ])],

        # Hanse 460 — Engine access issues (2 reports)
        *[{
            "source_forum": forum,
            "boat_manufacturer": "Hanse",
            "boat_model": "460",
            "boat_year": 2015 + i,
            "hull_material": "grp_solid",
            "hull_construction": "hand_layup",
            "propulsion": "sail",
            "issues": [{
                "category": "design_flaw",
                "zone_type": "engine",
                "description": "Motorraum mit schlechtem Zugang für Wartung und Reparaturen",
                "severity": "minor",
                "boat_age_months": 48 + i * 6,
            }],
            "positives": [],
            "reliability": 0.75 + i * 0.02,
        } for i, forum in enumerate([
            "segeln-forum.de", "myhanse.com",
        ])],

        # Jeanneau Sun Odyssey 410 — Forestay fitting issues (3 reports)
        *[({
            "source_forum": forum,
            "boat_manufacturer": "Jeanneau",
            "boat_model": "Sun Odyssey 410",
            "boat_year": 2013 + i,
            "hull_material": "grp_solid",
            "hull_construction": "hand_layup",
            "propulsion": "sail",
            "issues": [{
                "category": "hardware",
                "zone_type": "rigging",
                "description": "Vorstagarmaturen zeigen Ermüdungsrisse nach 8+ Jahren",
                "severity": "critical",
                "boat_age_months": 96 + i * 12,
            }],
            "positives": [],
            "reliability": 0.73 + i * 0.04,
        }) for i, forum in enumerate([
            "cruisersforum.com", "sailinganarchy.com", "segeln-forum.de",
        ])],

        # Jeanneau Sun Odyssey 410 — Hull-deck joint issues (2 reports)
        *[({
            "source_forum": forum,
            "boat_manufacturer": "Jeanneau",
            "boat_model": "Sun Odyssey 410",
            "boat_year": 2012 + i,
            "hull_material": "grp_solid",
            "hull_construction": "hand_layup",
            "propulsion": "sail",
            "issues": [{
                "category": "structural",
                "zone_type": "deck",
                "description": "Rumpf-Deck-Verbindung zeigt Undichtigkeiten und Wassereinbruch",
                "severity": "major",
                "boat_age_months": 108 + i * 12,
            }],
            "positives": [],
            "reliability": 0.68 + i * 0.05,
        }) for i, forum in enumerate([
            "segeln-forum.de", "cruisersforum.com",
        ])],

        # Jeanneau Sun Odyssey 440 — Standing rigging (3 reports)
        *[({
            "source_forum": forum,
            "boat_manufacturer": "Jeanneau",
            "boat_model": "Sun Odyssey 440",
            "boat_year": 2014 + i,
            "hull_material": "grp_solid",
            "hull_construction": "hand_layup",
            "propulsion": "sail",
            "issues": [{
                "category": "hardware",
                "zone_type": "rigging",
                "description": "Stehendes Gut zeigt vorzeitigen Verschleiß an den Terminals",
                "severity": "major",
                "boat_age_months": 72 + i * 12,
            }],
            "positives": [],
            "reliability": 0.71 + i * 0.04,
        }) for i, forum in enumerate([
            "cruisersforum.com", "segeln-forum.de", "sailboatowners.com",
        ])],

        # Jeanneau Sun Odyssey 440 — Anchor locker drainage (2 reports)
        *[({
            "source_forum": forum,
            "boat_manufacturer": "Jeanneau",
            "boat_model": "Sun Odyssey 440",
            "boat_year": 2015 + i,
            "hull_material": "grp_solid",
            "hull_construction": "hand_layup",
            "propulsion": "sail",
            "issues": [{
                "category": "design_flaw",
                "zone_type": "deck",
                "description": "Ankerkastenentwässerung unzureichend, Wasser sammelt sich",
                "severity": "minor",
                "boat_age_months": 48 + i * 6,
            }],
            "positives": [],
            "reliability": 0.76 + i * 0.02,
        }) for i, forum in enumerate([
            "segeln-forum.de", "cruisersforum.com",
        ])],

        # Hallberg-Rassy 40 — Windlass motor issues (2 reports)
        *[({
            "source_forum": forum,
            "boat_manufacturer": "Hallberg-Rassy",
            "boat_model": "40",
            "boat_year": 2012 + i,
            "hull_material": "grp_solid",
            "hull_construction": "hand_layup",
            "propulsion": "sail",
            "issues": [{
                "category": "hardware",
                "zone_type": "deck",
                "description": "Ankerwinde-Motor zeigt Überhitzung unter Belastung",
                "severity": "major",
                "boat_age_months": 84 + i * 12,
            }],
            "positives": [],
            "reliability": 0.74 + i * 0.03,
        }) for i, forum in enumerate([
            "ybw.com", "segeln-forum.de",
        ])],

        # Hallberg-Rassy 40 — Diesel tank corrosion (2 reports)
        *[({
            "source_forum": forum,
            "boat_manufacturer": "Hallberg-Rassy",
            "boat_model": "40",
            "boat_year": 2011 + i,
            "hull_material": "grp_solid",
            "hull_construction": "hand_layup",
            "propulsion": "sail",
            "issues": [{
                "category": "material_degradation",
                "zone_type": "engine",
                "description": "Dieseltank zeigt Korrosion von innen nach 10+ Jahren",
                "severity": "major",
                "boat_age_months": 120 + i * 12,
            }],
            "positives": [],
            "reliability": 0.68 + i * 0.04,
        }) for i, forum in enumerate([
            "cruisersforum.com", "ybw.com",
        ])],

        # Dehler 42 — Autopilot bracket issues (3 reports)
        *[({
            "source_forum": forum,
            "boat_manufacturer": "Dehler",
            "boat_model": "42",
            "boat_year": 2014 + i,
            "hull_material": "grp_solid",
            "hull_construction": "hand_layup",
            "propulsion": "sail",
            "issues": [{
                "category": "hardware",
                "zone_type": "deck",
                "description": "Segelkompass-Halterung zeigt Risse unter Seegang",
                "severity": "minor",
                "boat_age_months": 60 + i * 12,
            }],
            "positives": [],
            "reliability": 0.73 + i * 0.03,
        }) for i, forum in enumerate([
            "boote-forum.de", "segeln-forum.de", "cruisersforum.com",
        ])],

        # Dehler 42 — Genoa track issues (2 reports)
        *[({
            "source_forum": forum,
            "boat_manufacturer": "Dehler",
            "boat_model": "42",
            "boat_year": 2015 + i,
            "hull_material": "grp_solid",
            "hull_construction": "hand_layup",
            "propulsion": "sail",
            "issues": [{
                "category": "hardware",
                "zone_type": "deck",
                "description": "Genoa-Schiene zeigt Verschleiß und Verbiegung nach 5-6 Jahren",
                "severity": "minor",
                "boat_age_months": 60 + i * 12,
            }],
            "positives": [],
            "reliability": 0.74 + i * 0.02,
        }) for i, forum in enumerate([
            "segeln-forum.de", "boote-forum.de",
        ])],

        # Dehler 38 — Keel bolt tension (2 reports)
        *[({
            "source_forum": forum,
            "boat_manufacturer": "Dehler",
            "boat_model": "38",
            "boat_year": 2013 + i,
            "hull_material": "grp_solid",
            "hull_construction": "hand_layup",
            "propulsion": "sail",
            "issues": [{
                "category": "structural",
                "zone_type": "hull",
                "description": "Kielschrauben lockern sich periodisch, regelmäßige Überprüfung erforderlich",
                "severity": "major",
                "boat_age_months": 72 + i * 12,
            }],
            "positives": [],
            "reliability": 0.69 + i * 0.04,
        }) for i, forum in enumerate([
            "boote-forum.de", "segeln-forum.de",
        ])],

        # Dehler 38 — Mast step corrosion (1 report)
        *[({
            "source_forum": "segeln-forum.de",
            "boat_manufacturer": "Dehler",
            "boat_model": "38",
            "boat_year": 2012,
            "hull_material": "grp_solid",
            "hull_construction": "hand_layup",
            "propulsion": "sail",
            "issues": [{
                "category": "material_degradation",
                "zone_type": "deck",
                "description": "Mastschritt-Befestigung korrodiert unter UV-Einfluss und Salzwasser",
                "severity": "minor",
                "boat_age_months": 96,
            }],
            "positives": [],
            "reliability": 0.72,
        })],

        # X-Yachts X4.3 — Hull blister (3 reports)
        *[({
            "source_forum": forum,
            "boat_manufacturer": "X-Yachts",
            "boat_model": "X4.3",
            "boat_year": 2015 + i,
            "hull_material": "grp_solid",
            "hull_construction": "hand_layup",
            "propulsion": "sail",
            "issues": [{
                "category": "material_degradation",
                "zone_type": "hull",
                "description": "Osmoeblasen zeigen sich nach 5 Jahren bei kühleren Gewässern",
                "severity": "major",
                "boat_age_months": 60 + i * 12,
            }],
            "positives": [],
            "reliability": 0.70 + i * 0.03,
        }) for i, forum in enumerate([
            "cruisersforum.com", "ybw.com", "sailboatowners.com",
        ])],

        # X-Yachts X4.3 — Teak delamination (2 reports)
        *[({
            "source_forum": forum,
            "boat_manufacturer": "X-Yachts",
            "boat_model": "X4.3",
            "boat_year": 2014 + i,
            "hull_material": "grp_solid",
            "hull_construction": "hand_layup",
            "propulsion": "sail",
            "issues": [{
                "category": "material_degradation",
                "zone_type": "deck",
                "description": "Teakeinbau delaminialisiert an den Kanten nach 4-5 Jahren",
                "severity": "cosmetic",
                "boat_age_months": 48 + i * 12,
            }],
            "positives": [],
            "reliability": 0.75 + i * 0.02,
        }) for i, forum in enumerate([
            "boote-forum.de", "segeln-forum.de",
        ])],

        # X-Yachts X-40 — Rudder shaft issues (2 reports)
        *[({
            "source_forum": forum,
            "boat_manufacturer": "X-Yachts",
            "boat_model": "X-40",
            "boat_year": 2012 + i,
            "hull_material": "grp_solid",
            "hull_construction": "hand_layup",
            "propulsion": "sail",
            "issues": [{
                "category": "hardware",
                "zone_type": "hull",
                "description": "Ruderwelle zeigt minimales Spiel nach 8-10 Jahren, aber wird größer",
                "severity": "major",
                "boat_age_months": 96 + i * 12,
            }],
            "positives": [],
            "reliability": 0.71 + i * 0.04,
        }) for i, forum in enumerate([
            "ybw.com", "cruisersforum.com",
        ])],

        # X-Yachts X-40 — Chainplate issues (1 report)
        *[({
            "source_forum": "segeln-forum.de",
            "boat_manufacturer": "X-Yachts",
            "boat_model": "X-40",
            "boat_year": 2011,
            "hull_material": "grp_solid",
            "hull_construction": "hand_layup",
            "propulsion": "sail",
            "issues": [{
                "category": "structural",
                "zone_type": "rigging",
                "description": "Wantenplatten unter Seegang instabil, benötigen regelmäßige Verstärkung",
                "severity": "major",
                "boat_age_months": 120,
            }],
            "positives": [],
            "reliability": 0.68,
        })],

        # Beneteau Oceanis 40.1 — Bulkhead delamination (3 reports)
        *[({
            "source_forum": forum,
            "boat_manufacturer": "Beneteau",
            "boat_model": "Oceanis 40.1",
            "boat_year": 2015 + i,
            "hull_material": "grp_solid",
            "hull_construction": "hand_layup",
            "propulsion": "sail",
            "issues": [{
                "category": "material_degradation",
                "zone_type": "cabin",
                "description": "Schotten zeigen Verformung und Delamination nach 4-5 Jahren",
                "severity": "major",
                "boat_age_months": 48 + i * 12,
            }],
            "positives": [],
            "reliability": 0.68 + i * 0.04,
        }) for i, forum in enumerate([
            "cruisersforum.com", "segeln-forum.de", "sailboatowners.com",
        ])],

        # Beneteau Oceanis 40.1 — Window seal failures (3 reports)
        *[({
            "source_forum": forum,
            "boat_manufacturer": "Beneteau",
            "boat_model": "Oceanis 40.1",
            "boat_year": 2016 + i,
            "hull_material": "grp_solid",
            "hull_construction": "hand_layup",
            "propulsion": "sail",
            "issues": [{
                "category": "hardware",
                "zone_type": "cabin",
                "description": "Fensterrahmen zeigen Kondenswasser und undichte Stellen nach 3 Jahren",
                "severity": "minor",
                "boat_age_months": 36 + i * 12,
            }],
            "positives": [],
            "reliability": 0.71 + i * 0.03,
        }) for i, forum in enumerate([
            "segeln-forum.de", "cruisersforum.com", "sailboatowners.com",
        ])],

        # Beneteau First 40 — Keel issues (2 reports)
        *[({
            "source_forum": forum,
            "boat_manufacturer": "Beneteau",
            "boat_model": "First 40",
            "boat_year": 2013 + i,
            "hull_material": "grp_solid",
            "hull_construction": "hand_layup",
            "propulsion": "sail",
            "issues": [{
                "category": "structural",
                "zone_type": "hull",
                "description": "Kielbefestigung zeigt Verschleiß und erfordert Verstärkung",
                "severity": "critical",
                "boat_age_months": 84 + i * 12,
            }],
            "positives": [],
            "reliability": 0.65 + i * 0.05,
        }) for i, forum in enumerate([
            "cruisersforum.com", "ybw.com",
        ])],

        # Beneteau First 40 — Structural issues (1 report)
        *[({
            "source_forum": "sailboatowners.com",
            "boat_manufacturer": "Beneteau",
            "boat_model": "First 40",
            "boat_year": 2012,
            "hull_material": "grp_solid",
            "hull_construction": "hand_layup",
            "propulsion": "sail",
            "issues": [{
                "category": "structural",
                "zone_type": "hull",
                "description": "Rumpf-Struktur zeigt Verschleißerscheinungen unter extremer Belastung",
                "severity": "major",
                "boat_age_months": 108,
            }],
            "positives": [],
            "reliability": 0.66,
        })],

        # MOTORBOOT SECTION

        # Sunseeker Manhattan 55 — Engine room ventilation (3 reports)
        *[({
            "source_forum": forum,
            "boat_manufacturer": "Sunseeker",
            "boat_model": "Manhattan 55",
            "boat_year": 2015 + i,
            "hull_material": "grp_solid",
            "hull_construction": "hand_layup",
            "propulsion": "motor",
            "issues": [{
                "category": "design_flaw",
                "zone_type": "engine",
                "description": "Motorraum-Belüftung unzureichend, führt zu Überhitzung bei Dauerfahrt",
                "severity": "major",
                "boat_age_months": 48 + i * 12,
            }],
            "positives": [],
            "reliability": 0.67 + i * 0.04,
        }) for i, forum in enumerate([
            "thehulltruth.com", "boote-forum.de", "cruisersforum.com",
        ])],

        # Sunseeker Manhattan 55 — Gelcoat crazing (2 reports)
        *[({
            "source_forum": forum,
            "boat_manufacturer": "Sunseeker",
            "boat_model": "Manhattan 55",
            "boat_year": 2014 + i,
            "hull_material": "grp_solid",
            "hull_construction": "hand_layup",
            "propulsion": "motor",
            "issues": [{
                "category": "cosmetic",
                "zone_type": "hull",
                "description": "Gelcoat zeigt Kratzer-Netzwerk nach 5-6 Jahren unter UV",
                "severity": "cosmetic",
                "boat_age_months": 60 + i * 12,
            }],
            "positives": [],
            "reliability": 0.72 + i * 0.02,
        }) for i, forum in enumerate([
            "boote-forum.de", "thehulltruth.com",
        ])],

        # Sunseeker Manhattan 55 — Positive: luxury fit (1 report)
        *[({
            "source_forum": "boote-forum.de",
            "boat_manufacturer": "Sunseeker",
            "boat_model": "Manhattan 55",
            "boat_year": 2016,
            "hull_material": "grp_solid",
            "hull_construction": "hand_layup",
            "propulsion": "motor",
            "issues": [],
            "positives": [{
                "category": "design_flaw",
                "zone_type": "cabin",
                "description": "Sehr hochwertige Innenausstattung und Materialien trotz hohem Preis",
            }],
            "reliability": 0.78,
        })],

        # Sunseeker Predator 50 — Outdrive corrosion (2 reports)
        *[({
            "source_forum": forum,
            "boat_manufacturer": "Sunseeker",
            "boat_model": "Predator 50",
            "boat_year": 2013 + i,
            "hull_material": "grp_solid",
            "hull_construction": "hand_layup",
            "propulsion": "motor",
            "issues": [{
                "category": "material_degradation",
                "zone_type": "propulsion",
                "description": "Außenbordanlage zeigt Korrosion trotz Zinkanoden nach 6-7 Jahren",
                "severity": "major",
                "boat_age_months": 84 + i * 12,
            }],
            "positives": [],
            "reliability": 0.65 + i * 0.05,
        }) for i, forum in enumerate([
            "thehulltruth.com", "cruisersforum.com",
        ])],

        # Sunseeker Predator 50 — Electrical issues (2 reports)
        *[({
            "source_forum": forum,
            "boat_manufacturer": "Sunseeker",
            "boat_model": "Predator 50",
            "boat_year": 2014 + i,
            "hull_material": "grp_solid",
            "hull_construction": "hand_layup",
            "propulsion": "motor",
            "issues": [{
                "category": "hardware",
                "zone_type": "electrical",
                "description": "Elektrische Systeme zeigen Ausfälle in Salzwasserumgebung nach 5 Jahren",
                "severity": "major",
                "boat_age_months": 60 + i * 12,
            }],
            "positives": [],
            "reliability": 0.68 + i * 0.03,
        }) for i, forum in enumerate([
            "boote-forum.de", "thehulltruth.com",
        ])],

        # Princess V55 — Window seal failures (3 reports)
        *[({
            "source_forum": forum,
            "boat_manufacturer": "Princess",
            "boat_model": "V55",
            "boat_year": 2015 + i,
            "hull_material": "grp_solid",
            "hull_construction": "hand_layup",
            "propulsion": "motor",
            "issues": [{
                "category": "hardware",
                "zone_type": "cabin",
                "description": "Fensterrahmen zeigen Kondenswasser und Undichtigkeiten nach 3-4 Jahren",
                "severity": "minor",
                "boat_age_months": 36 + i * 12,
            }],
            "positives": [],
            "reliability": 0.71 + i * 0.03,
        }) for i, forum in enumerate([
            "cruisersforum.com", "boote-forum.de", "thehulltruth.com",
        ])],

        # Princess V55 — Generator noise (2 reports)
        *[({
            "source_forum": forum,
            "boat_manufacturer": "Princess",
            "boat_model": "V55",
            "boat_year": 2014 + i,
            "hull_material": "grp_solid",
            "hull_construction": "hand_layup",
            "propulsion": "motor",
            "issues": [{
                "category": "hardware",
                "zone_type": "engine",
                "description": "Generator-Lautstärke überschreitet Spezifikation unter Last",
                "severity": "minor",
                "boat_age_months": 48 + i * 12,
            }],
            "positives": [],
            "reliability": 0.73 + i * 0.02,
        }) for i, forum in enumerate([
            "boote-forum.de", "cruisersforum.com",
        ])],

        # Princess F50 — Hydraulic system issues (2 reports)
        *[({
            "source_forum": forum,
            "boat_manufacturer": "Princess",
            "boat_model": "F50",
            "boat_year": 2013 + i,
            "hull_material": "grp_solid",
            "hull_construction": "hand_layup",
            "propulsion": "motor",
            "issues": [{
                "category": "hardware",
                "zone_type": "propulsion",
                "description": "Hydraulische Systeme zeigen Druckverlust und Leckagen",
                "severity": "major",
                "boat_age_months": 72 + i * 12,
            }],
            "positives": [],
            "reliability": 0.66 + i * 0.04,
        }) for i, forum in enumerate([
            "thehulltruth.com", "cruisersforum.com",
        ])],

        # Princess F50 — Bow thruster issues (1 report)
        *[({
            "source_forum": "boote-forum.de",
            "boat_manufacturer": "Princess",
            "boat_model": "F50",
            "boat_year": 2012,
            "hull_material": "grp_solid",
            "hull_construction": "hand_layup",
            "propulsion": "motor",
            "issues": [{
                "category": "hardware",
                "zone_type": "propulsion",
                "description": "Bugstrahlanlage zeigt reduzierte Leistung nach 7-8 Jahren",
                "severity": "minor",
                "boat_age_months": 84,
            }],
            "positives": [],
            "reliability": 0.72,
        })],

        # Fairline Squadron 53 — Teak deck lifting (3 reports)
        *[({
            "source_forum": forum,
            "boat_manufacturer": "Fairline",
            "boat_model": "Squadron 53",
            "boat_year": 2014 + i,
            "hull_material": "grp_solid",
            "hull_construction": "hand_layup",
            "propulsion": "motor",
            "issues": [{
                "category": "material_degradation",
                "zone_type": "deck",
                "description": "Teakdeck hebt sich in Bereichen nach 4-5 Jahren, Wasser eindringt",
                "severity": "major",
                "boat_age_months": 48 + i * 12,
            }],
            "positives": [],
            "reliability": 0.68 + i * 0.04,
        }) for i, forum in enumerate([
            "boote-forum.de", "thehulltruth.com", "cruisersforum.com",
        ])],

        # Fairline Squadron 53 — Engine mount issues (1 report)
        *[({
            "source_forum": "thehulltruth.com",
            "boat_manufacturer": "Fairline",
            "boat_model": "Squadron 53",
            "boat_year": 2013,
            "hull_material": "grp_solid",
            "hull_construction": "hand_layup",
            "propulsion": "motor",
            "issues": [{
                "category": "hardware",
                "zone_type": "engine",
                "description": "Motorbefestigung zeigt Vibration und Verschleiß nach 6 Jahren",
                "severity": "major",
                "boat_age_months": 72,
            }],
            "positives": [],
            "reliability": 0.70,
        })],

        # Axopar 37 — T-top cracking (2 reports)
        *[({
            "source_forum": forum,
            "boat_manufacturer": "Axopar",
            "boat_model": "37",
            "boat_year": 2015 + i,
            "hull_material": "grp_solid",
            "hull_construction": "hand_layup",
            "propulsion": "motor",
            "issues": [{
                "category": "structural",
                "zone_type": "deck",
                "description": "T-Dach zeigt Risse an den Schweißstellen unter Windbelastung",
                "severity": "major",
                "boat_age_months": 36 + i * 12,
            }],
            "positives": [],
            "reliability": 0.69 + i * 0.04,
        }) for i, forum in enumerate([
            "boote-forum.de", "thehulltruth.com",
        ])],

        # Axopar 37 — Fuel tank access (1 report)
        *[({
            "source_forum": "boote-forum.de",
            "boat_manufacturer": "Axopar",
            "boat_model": "37",
            "boat_year": 2014,
            "hull_material": "grp_solid",
            "hull_construction": "hand_layup",
            "propulsion": "motor",
            "issues": [{
                "category": "design_flaw",
                "zone_type": "fuel",
                "description": "Zugang zum Kraftstofftank ist begrenzt für Wartung und Reinigung",
                "severity": "minor",
                "boat_age_months": 48,
            }],
            "positives": [],
            "reliability": 0.74,
        })],

        # Axopar 37 — Hull stress marks (1 report)
        *[({
            "source_forum": "thehulltruth.com",
            "boat_manufacturer": "Axopar",
            "boat_model": "37",
            "boat_year": 2013,
            "hull_material": "grp_solid",
            "hull_construction": "hand_layup",
            "propulsion": "motor",
            "issues": [{
                "category": "cosmetic",
                "zone_type": "hull",
                "description": "Sichtbare Spannungslinien auf dem Rumpf bei älteren Booten",
                "severity": "cosmetic",
                "boat_age_months": 60,
            }],
            "positives": [],
            "reliability": 0.72,
        })],

        # KATAMARANE SECTION

        # Lagoon 42 — Bridgedeck slamming (3 reports)
        *[({
            "source_forum": forum,
            "boat_manufacturer": "Lagoon",
            "boat_model": "42",
            "boat_year": 2014 + i,
            "hull_material": "grp_solid",
            "hull_construction": "hand_layup",
            "propulsion": "sail",
            "issues": [{
                "category": "structural",
                "zone_type": "deck",
                "description": "Zentrale Plattform zeigt Schäden durch Schlag auf dem Wasser bei Seegang",
                "severity": "major",
                "boat_age_months": 60 + i * 12,
            }],
            "positives": [],
            "reliability": 0.70 + i * 0.03,
        }) for i, forum in enumerate([
            "catamaranforum.com", "segeln-forum.de", "cruisersforum.com",
        ])],

        # Lagoon 42 — Dagger board issues (2 reports)
        *[({
            "source_forum": forum,
            "boat_manufacturer": "Lagoon",
            "boat_model": "42",
            "boat_year": 2015 + i,
            "hull_material": "grp_solid",
            "hull_construction": "hand_layup",
            "propulsion": "sail",
            "issues": [{
                "category": "hardware",
                "zone_type": "hull",
                "description": "Schwertkasten-Abdichtung undicht, Wasser in Rumpf eindringend",
                "severity": "major",
                "boat_age_months": 48 + i * 12,
            }],
            "positives": [],
            "reliability": 0.68 + i * 0.04,
        }) for i, forum in enumerate([
            "catamaranforum.com", "cruisersforum.com",
        ])],

        # Lagoon 42 — Positive: spacious cabin (1 report)
        *[({
            "source_forum": "catamaranforum.com",
            "boat_manufacturer": "Lagoon",
            "boat_model": "42",
            "boat_year": 2016,
            "hull_material": "grp_solid",
            "hull_construction": "hand_layup",
            "propulsion": "sail",
            "issues": [],
            "positives": [{
                "category": "design_flaw",
                "zone_type": "cabin",
                "description": "Großzügige Kabinen und Wohnbereiche im Vergleich zu Einrumpfbooten",
            }],
            "reliability": 0.82,
        })],

        # Lagoon 400 — Engine nacelle leaks (2 reports)
        *[({
            "source_forum": forum,
            "boat_manufacturer": "Lagoon",
            "boat_model": "400",
            "boat_year": 2013 + i,
            "hull_material": "grp_solid",
            "hull_construction": "hand_layup",
            "propulsion": "motor",
            "issues": [{
                "category": "hardware",
                "zone_type": "engine",
                "description": "Motor-Gondel zeigt Undichtigkeiten nach 7-8 Jahren",
                "severity": "major",
                "boat_age_months": 84 + i * 12,
            }],
            "positives": [],
            "reliability": 0.66 + i * 0.04,
        }) for i, forum in enumerate([
            "catamaranforum.com", "cruisersforum.com",
        ])],

        # Lagoon 400 — Trampoline wear (2 reports)
        *[({
            "source_forum": forum,
            "boat_manufacturer": "Lagoon",
            "boat_model": "400",
            "boat_year": 2014 + i,
            "hull_material": "grp_solid",
            "hull_construction": "hand_layup",
            "propulsion": "motor",
            "issues": [{
                "category": "material_degradation",
                "zone_type": "deck",
                "description": "Netz zwischen den Rümpfen zeigt UV-Schäden und Risse nach 5-6 Jahren",
                "severity": "minor",
                "boat_age_months": 60 + i * 12,
            }],
            "positives": [],
            "reliability": 0.73 + i * 0.02,
        }) for i, forum in enumerate([
            "catamaranforum.com", "boote-forum.de",
        ])],

        # Fountaine Pajot Elba 45 — Rudder play (2 reports)
        *[({
            "source_forum": forum,
            "boat_manufacturer": "Fountaine Pajot",
            "boat_model": "Elba 45",
            "boat_year": 2013 + i,
            "hull_material": "grp_solid",
            "hull_construction": "hand_layup",
            "propulsion": "sail",
            "issues": [{
                "category": "hardware",
                "zone_type": "hull",
                "description": "Ruderanlage zeigt erhöhtes Spiel und instabile Querruderbewegungen",
                "severity": "major",
                "boat_age_months": 72 + i * 12,
            }],
            "positives": [],
            "reliability": 0.68 + i * 0.04,
        }) for i, forum in enumerate([
            "catamaranforum.com", "cruisersforum.com",
        ])],

        # Fountaine Pajot Elba 45 — AC drain issues (2 reports)
        *[({
            "source_forum": forum,
            "boat_manufacturer": "Fountaine Pajot",
            "boat_model": "Elba 45",
            "boat_year": 2014 + i,
            "hull_material": "grp_solid",
            "hull_construction": "hand_layup",
            "propulsion": "sail",
            "issues": [{
                "category": "design_flaw",
                "zone_type": "cabin",
                "description": "Klimaanlage-Entwässerung unzureichend, Wasser im Schiff sammelt sich",
                "severity": "minor",
                "boat_age_months": 48 + i * 12,
            }],
            "positives": [],
            "reliability": 0.74 + i * 0.02,
        }) for i, forum in enumerate([
            "catamaranforum.com", "segeln-forum.de",
        ])],

        # TRAWLER/EXPLORER SECTION

        # Nordhavn 41 — Stabilizer issues (2 reports)
        *[({
            "source_forum": forum,
            "boat_manufacturer": "Nordhavn",
            "boat_model": "41",
            "boat_year": 2012 + i,
            "hull_material": "grp_solid",
            "hull_construction": "hand_layup",
            "propulsion": "motor",
            "issues": [{
                "category": "hardware",
                "zone_type": "propulsion",
                "description": "Stabilisierungssystem zeigt Fehlfunktionen und reduzierte Effektivität",
                "severity": "major",
                "boat_age_months": 84 + i * 12,
            }],
            "positives": [],
            "reliability": 0.67 + i * 0.04,
        }) for i, forum in enumerate([
            "trawlerforum.com", "cruisersforum.com",
        ])],

        # Nordhavn 41 — Fuel polishing system (2 reports)
        *[({
            "source_forum": forum,
            "boat_manufacturer": "Nordhavn",
            "boat_model": "41",
            "boat_year": 2011 + i,
            "hull_material": "grp_solid",
            "hull_construction": "hand_layup",
            "propulsion": "motor",
            "issues": [{
                "category": "hardware",
                "zone_type": "fuel",
                "description": "Kraftstoff-Filteranlage verstopft regelmäßig, erfordert häufige Wartung",
                "severity": "major",
                "boat_age_months": 96 + i * 12,
            }],
            "positives": [],
            "reliability": 0.65 + i * 0.05,
        }) for i, forum in enumerate([
            "trawlerforum.com", "cruisersforum.com",
        ])],

        # Nordhavn 41 — Positive: seaworthiness (1 report)
        *[({
            "source_forum": "trawlerforum.com",
            "boat_manufacturer": "Nordhavn",
            "boat_model": "41",
            "boat_year": 2013,
            "hull_material": "grp_solid",
            "hull_construction": "hand_layup",
            "propulsion": "motor",
            "issues": [],
            "positives": [{
                "category": "structural",
                "zone_type": "hull",
                "description": "Exzellente Seefahrtsfähigkeit und solide Konstruktion für Langstrecken",
            }],
            "reliability": 0.85,
        })],

        # Nordhavn 41 — Positive: diesel efficiency (1 report)
        *[({
            "source_forum": "cruisersforum.com",
            "boat_manufacturer": "Nordhavn",
            "boat_model": "41",
            "boat_year": 2012,
            "hull_material": "grp_solid",
            "hull_construction": "hand_layup",
            "propulsion": "motor",
            "issues": [],
            "positives": [{
                "category": "hardware",
                "zone_type": "engine",
                "description": "Dieselmotor zeigt hervorragende Effizienz und Zuverlässigkeit bei Langstrecken",
            }],
            "reliability": 0.84,
        })],

        # =====================================================================
        # MASSIVE EXPANSION: Water Ingress Failures (20 reports)
        # =====================================================================

        # Bavaria 42 — Chainplate delamination and water ingress (4 reports)
        *[({
            "source_forum": forum,
            "boat_manufacturer": "Bavaria",
            "boat_model": "42 Cruiser",
            "boat_year": 2013 + i,
            "hull_material": "grp_solid",
            "hull_construction": "hand_layup",
            "propulsion": "sail",
            "issues": [{
                "category": "material_degradation",
                "zone_type": "rigging",
                "description": "Wantenplatte-Befestigung zeigt Delamination um Bolzenlöcher, Wassereinbruch in Struktur",
                "severity": "critical",
                "boat_age_months": 84 + i * 12,
            }],
            "positives": [],
            "reliability": 0.62 + i * 0.03,
        }) for i, forum in enumerate([
            "boote-forum.de", "segeln-forum.de", "cruisersforum.com", "sailboatowners.com",
        ])],

        # Jeanneau Sun Odyssey 450 — Window frame seal failures (3 reports)
        *[({
            "source_forum": forum,
            "boat_manufacturer": "Jeanneau",
            "boat_model": "Sun Odyssey 450",
            "boat_year": 2012 + i,
            "hull_material": "grp_solid",
            "hull_construction": "hand_layup",
            "propulsion": "sail",
            "issues": [{
                "category": "hardware",
                "zone_type": "cabin",
                "description": "Fensterrahmen-Dichtungen ermüden nach 6-8 Jahren, Wasser läuft in Innenraum",
                "severity": "major",
                "boat_age_months": 84 + i * 12,
            }],
            "positives": [],
            "reliability": 0.71 + i * 0.02,
        }) for i, forum in enumerate([
            "cruisersforum.com", "segeln-forum.de", "sailboatowners.com",
        ])],

        # Beneteau First 44 — Through-hull fitting corrosion (3 reports)
        *[({
            "source_forum": forum,
            "boat_manufacturer": "Beneteau",
            "boat_model": "First 44",
            "boat_year": 2014 + i,
            "hull_material": "grp_solid",
            "hull_construction": "hand_layup",
            "propulsion": "sail",
            "issues": [{
                "category": "material_degradation",
                "zone_type": "hull",
                "description": "Durchgangsventile korrodieren trotz Edelstahl-Anspruch, Wasser leckt in Bilge",
                "severity": "major",
                "boat_age_months": 72 + i * 12,
            }],
            "positives": [],
            "reliability": 0.64 + i * 0.04,
        }) for i, forum in enumerate([
            "boote-forum.de", "segeln-forum.de", "cruisersforum.com",
        ])],

        # Hanse 455 — Deck-hull joint water ingress (3 reports)
        *[({
            "source_forum": forum,
            "boat_manufacturer": "Hanse",
            "boat_model": "455",
            "boat_year": 2015 + i,
            "hull_material": "grp_solid",
            "hull_construction": "hand_layup",
            "propulsion": "sail",
            "issues": [{
                "category": "structural",
                "zone_type": "deck",
                "description": "Rumpf-Deck-Naht zeigt Risse, massive Wassereintritt bei Seegang ab 5 Jahren",
                "severity": "critical",
                "boat_age_months": 60 + i * 12,
            }],
            "positives": [],
            "reliability": 0.58 + i * 0.05,
        }) for i, forum in enumerate([
            "myhanse.com", "boote-forum.de", "cruisersforum.com",
        ])],

        # Hallberg-Rassy 50 — Hatch seal degradation (2 reports)
        *[({
            "source_forum": forum,
            "boat_manufacturer": "Hallberg-Rassy",
            "boat_model": "50",
            "boat_year": 2011 + i,
            "hull_material": "grp_solid",
            "hull_construction": "hand_layup",
            "propulsion": "sail",
            "issues": [{
                "category": "material_degradation",
                "zone_type": "deck",
                "description": "Luke-Dichtung porös nach 10+ Jahren, bei Regen läuft Wasser in Kajüte",
                "severity": "minor",
                "boat_age_months": 120 + i * 12,
            }],
            "positives": [],
            "reliability": 0.73 + i * 0.02,
        }) for i, forum in enumerate([
            "ybw.com", "cruisersforum.com",
        ])],

        # Najad 385 — Rudder bearing water ingress (2 reports)
        *[({
            "source_forum": forum,
            "boat_manufacturer": "Najad",
            "boat_model": "385",
            "boat_year": 2013 + i,
            "hull_material": "grp_solid",
            "hull_construction": "hand_layup",
            "propulsion": "sail",
            "issues": [{
                "category": "hardware",
                "zone_type": "hull",
                "description": "Ruderschaft-Lager undicht, Seewasser dringt in Ruderschacht ein",
                "severity": "major",
                "boat_age_months": 84 + i * 12,
            }],
            "positives": [],
            "reliability": 0.67 + i * 0.03,
        }) for i, forum in enumerate([
            "cruisersforum.com", "segeln-forum.de",
        ])],

        # Lagoon 450 — Keel bolt seal failure (2 reports)
        *[({
            "source_forum": forum,
            "boat_manufacturer": "Lagoon",
            "boat_model": "450",
            "boat_year": 2014 + i,
            "hull_material": "grp_solid",
            "hull_construction": "hand_layup",
            "propulsion": "sail",
            "issues": [{
                "category": "material_degradation",
                "zone_type": "hull",
                "description": "Kielbefestigung-Dichtung versagt, Salzwasser sickert in Rumpfhohlraum",
                "severity": "critical",
                "boat_age_months": 60 + i * 12,
            }],
            "positives": [],
            "reliability": 0.61 + i * 0.04,
        }) for i, forum in enumerate([
            "catamaranforum.com", "cruisersforum.com",
        ])],

        # Sunseeker 60 — Mast step drainage failure (1 report)
        *[({
            "source_forum": "yachtforum.com",
            "boat_manufacturer": "Sunseeker",
            "boat_model": "60 Predator",
            "boat_year": 2012,
            "hull_material": "grp_solid",
            "hull_construction": "hand_layup",
            "propulsion": "motor",
            "issues": [{
                "category": "design_flaw",
                "zone_type": "deck",
                "description": "Mastschritt-Entwässerung unzureichend gestaltet, Wasser sammelt sich unter Mast",
                "severity": "minor",
                "boat_age_months": 108,
            }],
            "positives": [],
            "reliability": 0.74,
        })],

        # =====================================================================
        # Chafing/Wear Damage Reports (20 reports)
        # =====================================================================

        # Bavaria 38 — Genoa sheets on shrouds (3 reports)
        *[({
            "source_forum": forum,
            "boat_manufacturer": "Bavaria",
            "boat_model": "38 Cruiser",
            "boat_year": 2016 + i,
            "hull_material": "grp_solid",
            "hull_construction": "hand_layup",
            "propulsion": "sail",
            "issues": [{
                "category": "material_degradation",
                "zone_type": "rigging",
                "description": "Genua-Schoten schleifen an Wanten, Faden-Verschleiß nach 3-4 Jahren Fahrt",
                "severity": "minor",
                "boat_age_months": 48 + i * 12,
            }],
            "positives": [],
            "reliability": 0.78 + i * 0.02,
        }) for i, forum in enumerate([
            "boote-forum.de", "segeln-forum.de", "sailboatowners.com",
        ])],

        # Hanse 430 — Anchor chain on bow roller (3 reports)
        *[({
            "source_forum": forum,
            "boat_manufacturer": "Hanse",
            "boat_model": "430",
            "boat_year": 2015 + i,
            "hull_material": "grp_solid",
            "hull_construction": "hand_layup",
            "propulsion": "sail",
            "issues": [{
                "category": "material_degradation",
                "zone_type": "deck",
                "description": "Ankerkette schleift unregelmäßig über Rolle, oberflächliches Abschleifen nach 5+ Jahren",
                "severity": "cosmetic",
                "boat_age_months": 60 + i * 12,
            }],
            "positives": [],
            "reliability": 0.82 + i * 0.01,
        }) for i, forum in enumerate([
            "myhanse.com", "boote-forum.de", "segeln-forum.de",
        ])],

        # Jeanneau 45 — Dock lines on fairleads (2 reports)
        *[({
            "source_forum": forum,
            "boat_manufacturer": "Jeanneau",
            "boat_model": "45 DS",
            "boat_year": 2014 + i,
            "hull_material": "grp_solid",
            "hull_construction": "hand_layup",
            "propulsion": "sail",
            "issues": [{
                "category": "material_degradation",
                "zone_type": "deck",
                "description": "Anlegetrossen schleifen an Führungsösen, Faserausfransung nach 2-3 Jahren Liegeplatz",
                "severity": "minor",
                "boat_age_months": 36 + i * 12,
            }],
            "positives": [],
            "reliability": 0.80 + i * 0.02,
        }) for i, forum in enumerate([
            "cruisersforum.com", "segeln-forum.de",
        ])],

        # Beneteau 40 — Halyards on mast sheaves (2 reports)
        *[({
            "source_forum": forum,
            "boat_manufacturer": "Beneteau",
            "boat_model": "40 CR",
            "boat_year": 2013 + i,
            "hull_material": "grp_solid",
            "hull_construction": "hand_layup",
            "propulsion": "sail",
            "issues": [{
                "category": "material_degradation",
                "zone_type": "rigging",
                "description": "Großsegel- und Fock-Niederholer schleifen an Mastscheiben, Verschleiß nach 4-5 Jahren",
                "severity": "minor",
                "boat_age_months": 60 + i * 12,
            }],
            "positives": [],
            "reliability": 0.77 + i * 0.03,
        }) for i, forum in enumerate([
            "boote-forum.de", "cruisersforum.com",
        ])],

        # Hallberg-Rassy 42 — Fender lines on toe rails (2 reports)
        *[({
            "source_forum": forum,
            "boat_manufacturer": "Hallberg-Rassy",
            "boat_model": "42",
            "boat_year": 2012 + i,
            "hull_material": "grp_solid",
            "hull_construction": "hand_layup",
            "propulsion": "sail",
            "issues": [{
                "category": "material_degradation",
                "zone_type": "deck",
                "description": "Fender-Leinen schleifen an Schanzkleiderleisten, oberflächlicher Verschleiß nach 6+ Jahren",
                "severity": "cosmetic",
                "boat_age_months": 84 + i * 12,
            }],
            "positives": [],
            "reliability": 0.81 + i * 0.01,
        }) for i, forum in enumerate([
            "ybw.com", "segeln-forum.de",
        ])],

        # Dehler 41 — Boom vang on mast track (2 reports)
        *[({
            "source_forum": forum,
            "boat_manufacturer": "Dehler",
            "boat_model": "41",
            "boat_year": 2014 + i,
            "hull_material": "grp_solid",
            "hull_construction": "hand_layup",
            "propulsion": "sail",
            "issues": [{
                "category": "material_degradation",
                "zone_type": "deck",
                "description": "Großsegel-Niederholer-Leine schleift an Mastspur, Faserverschleiß nach 5 Jahren",
                "severity": "minor",
                "boat_age_months": 60 + i * 12,
            }],
            "positives": [],
            "reliability": 0.79 + i * 0.02,
        }) for i, forum in enumerate([
            "boote-forum.de", "segeln-forum.de",
        ])],

        # X-Yachts X45 — Propeller shaft bearing wear (2 reports)
        *[({
            "source_forum": forum,
            "boat_manufacturer": "X-Yachts",
            "boat_model": "X45",
            "boat_year": 2013 + i,
            "hull_material": "grp_solid",
            "hull_construction": "hand_layup",
            "propulsion": "sail",
            "issues": [{
                "category": "hardware",
                "zone_type": "propulsion",
                "description": "Propellerwelle-Lager zeigen zunehmendes Spiel nach 8-10 Jahren Betrieb",
                "severity": "major",
                "boat_age_months": 108 + i * 6,
            }],
            "positives": [],
            "reliability": 0.68 + i * 0.03,
        }) for i, forum in enumerate([
            "cruisersforum.com", "sailboatowners.com",
        ])],

        # Contest 45 — Standing rigging chafing (1 report)
        *[({
            "source_forum": "ybw.com",
            "boat_manufacturer": "Contest",
            "boat_model": "45",
            "boat_year": 2012,
            "hull_material": "grp_solid",
            "hull_construction": "hand_layup",
            "propulsion": "sail",
            "issues": [{
                "category": "material_degradation",
                "zone_type": "rigging",
                "description": "Stehende Wanten schleifen an Mastklemmen, oberflächliche Kratzer nach intensiver Segelnutzung",
                "severity": "cosmetic",
                "boat_age_months": 96,
            }],
            "positives": [],
            "reliability": 0.80,
        })],

        # =====================================================================
        # Material-Specific Degradation Reports (25 reports)
        # =====================================================================

        # Bavaria 38 — Gelcoat crazing and chalking (3 reports)
        *[({
            "source_forum": ['boote-forum.de', 'segeln-forum.de', 'cruisersforum.com', 'sailboatowners.com', 'ybw.com', 'thehulltruth.com', 'sailing-forum.de', 'motorbootforum.de', 'yachtforums.com', 'sailnet.com'][i % 10],
            "boat_manufacturer": "Bavaria",
            "boat_model": "38 Cruiser",
            "boat_year": 2015,
            "hull_material": "grp_solid",
            "hull_construction": "hand_layup",
            "propulsion": "sail",
            "issues": [{
                "category": "cosmetic",
                "zone_type": "hull",
                "description": "Gelcoat zeigt Rissbildung (Crazing) und Kreideausblühung nach 5-6 Jahren UV-Exposition",
                "severity": "cosmetic",
                "boat_age_months": 72 + i * 12,
            }],
            "positives": [],
            "reliability": 0.75 + i * 0.01,
        }) for i in range(3)],

        # Hanse 455 — Teak deck caulking failure (3 reports)
        *[({
            "source_forum": forum,
            "boat_manufacturer": "Hanse",
            "boat_model": "455",
            "boat_year": 2014,
            "hull_material": "grp_solid",
            "hull_construction": "hand_layup",
            "propulsion": "sail",
            "issues": [{
                "category": "material_degradation",
                "zone_type": "deck",
                "description": "Teakholz-Fugenkitt wird porig und brüchig nach 4-5 Jahren, Wasser dringt ein",
                "severity": "major",
                "boat_age_months": 60 + i * 12,
            }],
            "positives": [],
            "reliability": 0.68 + i * 0.03,
        }) for i, forum in enumerate([
            "boote-forum.de", "segeln-forum.de", "myhanse.com",
        ])],

        # Jeanneau 45 — Stainless steel crevice corrosion (3 reports)
        *[({
            "source_forum": forum,
            "boat_manufacturer": "Jeanneau",
            "boat_model": "45 DS",
            "boat_year": 2013 + i,
            "hull_material": "grp_solid",
            "hull_construction": "hand_layup",
            "propulsion": "sail",
            "issues": [{
                "category": "material_degradation",
                "zone_type": "deck",
                "description": "Edelstahl-Beschläge zeigen Spaltkorrosion unter GFK-Kanten und in Gewindelöchern",
                "severity": "minor",
                "boat_age_months": 84 + i * 12,
            }],
            "positives": [],
            "reliability": 0.77 + i * 0.02,
        }) for i, forum in enumerate([
            "cruisersforum.com", "segeln-forum.de", "sailboatowners.com",
        ])],

        # Beneteau 42 — Aluminum corrosion in bilge areas (2 reports)
        *[({
            "source_forum": forum,
            "boat_manufacturer": "Beneteau",
            "boat_model": "42 CR",
            "boat_year": 2012 + i,
            "hull_material": "grp_solid",
            "hull_construction": "hand_layup",
            "propulsion": "sail",
            "issues": [{
                "category": "material_degradation",
                "zone_type": "engine",
                "description": "Aluminium-Rohre in Bilge korrodieren schnell trotz Beschichtung, Weiße Korrosionsprodukte",
                "severity": "major",
                "boat_age_months": 96 + i * 12,
            }],
            "positives": [],
            "reliability": 0.64 + i * 0.04,
        }) for i, forum in enumerate([
            "boote-forum.de", "cruisersforum.com",
        ])],

        # Hallberg-Rassy 50 — Core material waterlogging (2 reports)
        *[({
            "source_forum": forum,
            "boat_manufacturer": "Hallberg-Rassy",
            "boat_model": "50",
            "boat_year": 2011 + i,
            "hull_material": "grp_cored",
            "hull_construction": "hand_layup",
            "propulsion": "sail",
            "issues": [{
                "category": "material_degradation",
                "zone_type": "hull",
                "description": "Balsa-Kern zeigt Wasseraufnahme und Fäulnis nach Delaminationsverletzungen",
                "severity": "critical",
                "boat_age_months": 120 + i * 12,
            }],
            "positives": [],
            "reliability": 0.59 + i * 0.05,
        }) for i, forum in enumerate([
            "ybw.com", "cruisersforum.com",
        ])],

        # Najad 42 — Antifouling paint compatibility (2 reports)
        *[({
            "source_forum": forum,
            "boat_manufacturer": "Najad",
            "boat_model": "42",
            "boat_year": 2014 + i,
            "hull_material": "grp_solid",
            "hull_construction": "hand_layup",
            "propulsion": "sail",
            "issues": [{
                "category": "material_degradation",
                "zone_type": "hull",
                "description": "Antifouling-Anstrich zeigt Blätterung und Farbabstoßung bei Schichtwechsel-Systemen",
                "severity": "minor",
                "boat_age_months": 60 + i * 12,
            }],
            "positives": [],
            "reliability": 0.72 + i * 0.02,
        }) for i, forum in enumerate([
            "cruisersforum.com", "segeln-forum.de",
        ])],

        # Lagoon 500 — Sealant adhesion failure (2 reports)
        *[({
            "source_forum": forum,
            "boat_manufacturer": "Lagoon",
            "boat_model": "500",
            "boat_year": 2015 + i,
            "hull_material": "grp_solid",
            "hull_construction": "hand_layup",
            "propulsion": "motor",
            "issues": [{
                "category": "material_degradation",
                "zone_type": "deck",
                "description": "Polyurethan-Dichtmasse verliert Haftung an Deck-Beschlägen nach UV-Exposition",
                "severity": "minor",
                "boat_age_months": 48 + i * 12,
            }],
            "positives": [],
            "reliability": 0.74 + i * 0.02,
        }) for i, forum in enumerate([
            "catamaranforum.com", "cruisersforum.com",
        ])],

        # Fountaine Pajot 47 — Hull print-through degradation (2 reports)
        *[({
            "source_forum": forum,
            "boat_manufacturer": "Fountaine Pajot",
            "boat_model": "47",
            "boat_year": 2013 + i,
            "hull_material": "grp_solid",
            "hull_construction": "hand_layup",
            "propulsion": "sail",
            "issues": [{
                "category": "cosmetic",
                "zone_type": "hull",
                "description": "Gewebestruktur-Abzeichnung wird nach 7+ Jahren immer ausgeprägter, kann poliert nicht entfernt",
                "severity": "cosmetic",
                "boat_age_months": 84 + i * 12,
            }],
            "positives": [],
            "reliability": 0.76 + i * 0.01,
        }) for i, forum in enumerate([
            "catamaranforum.com", "segeln-forum.de",
        ])],

        # Sunseeker 72 — Teak degradation and rot (1 report)
        *[({
            "source_forum": "yachtforum.com",
            "boat_manufacturer": "Sunseeker",
            "boat_model": "72 Sport Yacht",
            "boat_year": 2011,
            "hull_material": "grp_solid",
            "hull_construction": "hand_layup",
            "propulsion": "motor",
            "issues": [{
                "category": "material_degradation",
                "zone_type": "deck",
                "description": "Teakeinlegearbeiten zeigen Verfärbung, Pilzbefall und oberflächliche Faulstellen",
                "severity": "minor",
                "boat_age_months": 132,
            }],
            "positives": [],
            "reliability": 0.69,
        })],

        # Princess 62 — Cabin sole delamination (1 report)
        *[({
            "source_forum": "yachtforum.com",
            "boat_manufacturer": "Princess",
            "boat_model": "62 Motor Yacht",
            "boat_year": 2012,
            "hull_material": "grp_cored",
            "hull_construction": "hand_layup",
            "propulsion": "motor",
            "issues": [{
                "category": "material_degradation",
                "zone_type": "cabin",
                "description": "Kabinen-Bodenbelag delaminiert an Kanten nach feuchtigkeitsbedingter Quellung",
                "severity": "minor",
                "boat_age_months": 120,
            }],
            "positives": [],
            "reliability": 0.71,
        })],

        # =====================================================================
        # Structural Failures (15 reports)
        # =====================================================================

        # Bavaria C45 — Bulkhead tabbing failure (3 reports)
        *[({
            "source_forum": forum,
            "boat_manufacturer": "Bavaria",
            "boat_model": "C45",
            "boat_year": 2013 + i,
            "hull_material": "grp_solid",
            "hull_construction": "hand_layup",
            "propulsion": "sail",
            "issues": [{
                "category": "structural",
                "zone_type": "cabin",
                "description": "Schott-Befestigung zeigt Faser-Abschälungen und Risse nach 7-9 Jahren Belastung",
                "severity": "major",
                "boat_age_months": 96 + i * 12,
            }],
            "positives": [],
            "reliability": 0.63 + i * 0.04,
        }) for i, forum in enumerate([
            "boote-forum.de", "segeln-forum.de", "cruisersforum.com",
        ])],

        # Hanse 505 — Floor timber delamination (2 reports)
        *[({
            "source_forum": forum,
            "boat_manufacturer": "Hanse",
            "boat_model": "505",
            "boat_year": 2014 + i,
            "hull_material": "grp_solid",
            "hull_construction": "hand_layup",
            "propulsion": "sail",
            "issues": [{
                "category": "structural",
                "zone_type": "hull",
                "description": "Fußleistenaufbau zeigt Delaminationen und Risse unter ungleichmäßiger Lastverteilung",
                "severity": "major",
                "boat_age_months": 84 + i * 12,
            }],
            "positives": [],
            "reliability": 0.62 + i * 0.05,
        }) for i, forum in enumerate([
            "myhanse.com", "boote-forum.de",
        ])],

        # Jeanneau 55 — Transom core rot (2 reports)
        *[({
            "source_forum": forum,
            "boat_manufacturer": "Jeanneau",
            "boat_model": "55 DS",
            "boat_year": 2012 + i,
            "hull_material": "grp_cored",
            "hull_construction": "hand_layup",
            "propulsion": "sail",
            "issues": [{
                "category": "structural",
                "zone_type": "hull",
                "description": "Heck-Kern zeigt Verwesung und Fäulnis durch eindringende Seewasser-Mikrorisse",
                "severity": "critical",
                "boat_age_months": 108 + i * 12,
            }],
            "positives": [],
            "reliability": 0.54 + i * 0.06,
        }) for i, forum in enumerate([
            "cruisersforum.com", "segeln-forum.de",
        ])],

        # Beneteau 50 — Rudder tube wear (2 reports)
        *[({
            "source_forum": forum,
            "boat_manufacturer": "Beneteau",
            "boat_model": "50 CR",
            "boat_year": 2013 + i,
            "hull_material": "grp_solid",
            "hull_construction": "hand_layup",
            "propulsion": "sail",
            "issues": [{
                "category": "hardware",
                "zone_type": "hull",
                "description": "Ruderrohr-Lagerung zeigt Verschleiß und erhöhtes Spiel nach 8+ Jahren",
                "severity": "major",
                "boat_age_months": 108 + i * 12,
            }],
            "positives": [],
            "reliability": 0.64 + i * 0.04,
        }) for i, forum in enumerate([
            "boote-forum.de", "cruisersforum.com",
        ])],

        # Hallberg-Rassy 60 — Engine mount softening (2 reports)
        *[({
            "source_forum": forum,
            "boat_manufacturer": "Hallberg-Rassy",
            "boat_model": "60",
            "boat_year": 2011 + i,
            "hull_material": "grp_solid",
            "hull_construction": "hand_layup",
            "propulsion": "motor",
            "issues": [{
                "category": "material_degradation",
                "zone_type": "engine",
                "description": "Motor-Elastomerlager weichen auf und verlieren Steifigkeit nach 10+ Jahren Betrieb",
                "severity": "major",
                "boat_age_months": 132 + i * 12,
            }],
            "positives": [],
            "reliability": 0.59 + i * 0.04,
        }) for i, forum in enumerate([
            "ybw.com", "cruisersforum.com",
        ])],

        # Najad 48 — Battery box acid damage (1 report)
        *[({
            "source_forum": "cruisersforum.com",
            "boat_manufacturer": "Najad",
            "boat_model": "48",
            "boat_year": 2013,
            "hull_material": "grp_solid",
            "hull_construction": "hand_layup",
            "propulsion": "sail",
            "issues": [{
                "category": "material_degradation",
                "zone_type": "engine",
                "description": "Batteriefach-Kunststoff zeigt Säurebrand und Sprödigkeit nach Überladungsschäden",
                "severity": "minor",
                "boat_age_months": 96,
            }],
            "positives": [],
            "reliability": 0.70,
        })],

        # Dehler 45 — Deck-cabin joint cracks (2 reports)
        *[({
            "source_forum": forum,
            "boat_manufacturer": "Dehler",
            "boat_model": "45",
            "boat_year": 2014 + i,
            "hull_material": "grp_solid",
            "hull_construction": "hand_layup",
            "propulsion": "sail",
            "issues": [{
                "category": "structural",
                "zone_type": "deck",
                "description": "Schnittstelle Deck-Aufbau zeigt Risse und Spannungsrisse nach 6-7 Jahren",
                "severity": "major",
                "boat_age_months": 84 + i * 12,
            }],
            "positives": [],
            "reliability": 0.65 + i * 0.04,
        }) for i, forum in enumerate([
            "boote-forum.de", "cruisersforum.com",
        ])],

        # =====================================================================
        # Additional Motor Yacht Reports (15 reports)
        # =====================================================================

        # Fairline Squadron 55 — Shaft seal leakage (2 reports)
        *[({
            "source_forum": forum,
            "boat_manufacturer": "Fairline",
            "boat_model": "Squadron 55",
            "boat_year": 2012 + i,
            "hull_material": "grp_solid",
            "hull_construction": "hand_layup",
            "propulsion": "motor",
            "issues": [{
                "category": "hardware",
                "zone_type": "propulsion",
                "description": "Wellendichtring leckt und erfordert regelmäßigen Austausch nach 8-10 Jahren",
                "severity": "major",
                "boat_age_months": 108 + i * 12,
            }],
            "positives": [],
            "reliability": 0.61 + i * 0.04,
        }) for i, forum in enumerate([
            "yachtforum.com", "cruisersforum.com",
        ])],

        # Azimut 45 — Generator diesel fuel system (2 reports)
        *[({
            "source_forum": forum,
            "boat_manufacturer": "Azimut",
            "boat_model": "45 Flybridge",
            "boat_year": 2013 + i,
            "hull_material": "grp_solid",
            "hull_construction": "hand_layup",
            "propulsion": "motor",
            "issues": [{
                "category": "hardware",
                "zone_type": "engine",
                "description": "Aggregat-Kraftstoffsystem zeigt Wasserkondensation und Rostbildung in Tank",
                "severity": "major",
                "boat_age_months": 96 + i * 12,
            }],
            "positives": [],
            "reliability": 0.62 + i * 0.03,
        }) for i, forum in enumerate([
            "yachtforum.com", "cruisersforum.com",
        ])],

        # Ferretti 55 — AC compressor coolant loss (2 reports)
        *[({
            "source_forum": forum,
            "boat_manufacturer": "Ferretti",
            "boat_model": "55",
            "boat_year": 2014 + i,
            "hull_material": "grp_solid",
            "hull_construction": "hand_layup",
            "propulsion": "motor",
            "issues": [{
                "category": "hardware",
                "zone_type": "cabin",
                "description": "Klimaanlage-Kompressor verliert Kühlmittel nach 5-6 Jahren, Vibrationen entstehen",
                "severity": "major",
                "boat_age_months": 72 + i * 12,
            }],
            "positives": [],
            "reliability": 0.63 + i * 0.04,
        }) for i, forum in enumerate([
            "yachtforum.com", "cruisersforum.com",
        ])],

        # Grand Banks 42 — Hull oil canning (2 reports)
        *[({
            "source_forum": forum,
            "boat_manufacturer": "Grand Banks",
            "boat_model": "42",
            "boat_year": 2013 + i,
            "hull_material": "grp_solid",
            "hull_construction": "hand_layup",
            "propulsion": "motor",
            "issues": [{
                "category": "cosmetic",
                "zone_type": "hull",
                "description": "Rumpf zeigt leichte Beulungen (Oil Canning) und Wellen unter Sonneneinstrahlung",
                "severity": "cosmetic",
                "boat_age_months": 96 + i * 12,
            }],
            "positives": [],
            "reliability": 0.78 + i * 0.01,
        }) for i, forum in enumerate([
            "trawlerforum.com", "cruisersforum.com",
        ])],

        # Nordic Tug 37 — Thru-hull zincs corrosion (2 reports)
        *[({
            "source_forum": forum,
            "boat_manufacturer": "Nordic Tug",
            "boat_model": "37",
            "boat_year": 2012 + i,
            "hull_material": "grp_solid",
            "hull_construction": "hand_layup",
            "propulsion": "motor",
            "issues": [{
                "category": "material_degradation",
                "zone_type": "hull",
                "description": "Zink-Opferanoden werden schnell verbraucht, Durchgangsventile zeigen Korrosion",
                "severity": "major",
                "boat_age_months": 108 + i * 12,
            }],
            "positives": [],
            "reliability": 0.64 + i * 0.04,
        }) for i, forum in enumerate([
            "trawlerforum.com", "cruisersforum.com",
        ])],

        # Princess 75 — Cabin sole cracking (1 report)
        *[({
            "source_forum": "yachtforum.com",
            "boat_manufacturer": "Princess",
            "boat_model": "75 Motor Yacht",
            "boat_year": 2011,
            "hull_material": "grp_cored",
            "hull_construction": "hand_layup",
            "propulsion": "motor",
            "issues": [{
                "category": "structural",
                "zone_type": "cabin",
                "description": "Kabinen-Bodenplatten zeigen Haarrisse an den Rändern nach Setzung des Untergrunds",
                "severity": "minor",
                "boat_age_months": 132,
            }],
            "positives": [],
            "reliability": 0.72,
        })],

        # Sunseeker Manhattan 64 — Helm chair material (1 report)
        *[({
            "source_forum": "yachtforum.com",
            "boat_manufacturer": "Sunseeker",
            "boat_model": "Manhattan 64",
            "boat_year": 2012,
            "hull_material": "grp_solid",
            "hull_construction": "hand_layup",
            "propulsion": "motor",
            "issues": [{
                "category": "material_degradation",
                "zone_type": "deck",
                "description": "Steuersitz-Bezugsstoff feuert schnell nach UV-Exposition und wird brüchig",
                "severity": "cosmetic",
                "boat_age_months": 108,
            }],
            "positives": [],
            "reliability": 0.74,
        })],

        # =====================================================================
        # Additional Sailing Reports - Advanced Technical Issues (5 reports)
        # =====================================================================

        # J Boats J/46 — Mast structural cracks (1 report)
        *[({
            "source_forum": "sailboatowners.com",
            "boat_manufacturer": "J Boats",
            "boat_model": "J/46",
            "boat_year": 2012,
            "hull_material": "grp_solid",
            "hull_construction": "hand_layup",
            "propulsion": "sail",
            "issues": [{
                "category": "structural",
                "zone_type": "rigging",
                "description": "Aluminium-Mast zeigt Mikrobrüche an Wantenauslegern nach extremen Windlasten",
                "severity": "critical",
                "boat_age_months": 132,
            }],
            "positives": [],
            "reliability": 0.68,
        })],

        # Contest 50 — Carbon boom delamination (1 report)
        *[({
            "source_forum": "ybw.com",
            "boat_manufacturer": "Contest",
            "boat_model": "50",
            "boat_year": 2013,
            "hull_material": "grp_solid",
            "hull_construction": "hand_layup",
            "propulsion": "sail",
            "issues": [{
                "category": "material_degradation",
                "zone_type": "deck",
                "description": "Kohlefaser-Großbaum zeigt Oberflächendelaminationen unter Belastung nach 7 Jahren",
                "severity": "major",
                "boat_age_months": 96,
            }],
            "positives": [],
            "reliability": 0.71,
        })],

        # Najad 46 — Cored decks wave pattern (1 report)
        *[({
            "source_forum": "cruisersforum.com",
            "boat_manufacturer": "Najad",
            "boat_model": "46",
            "boat_year": 2014,
            "hull_material": "grp_cored",
            "hull_construction": "hand_layup",
            "propulsion": "sail",
            "issues": [{
                "category": "cosmetic",
                "zone_type": "deck",
                "description": "Kern-Decks zeigen Wellenmuster und leichte Verformungen unter Sonnenbestrahlung",
                "severity": "cosmetic",
                "boat_age_months": 60,
            }],
            "positives": [],
            "reliability": 0.76,
        })],

        # X-Yachts X4.9 — Bow pulpit joint cracks (1 report)
        *[({
            "source_forum": "sailboatowners.com",
            "boat_manufacturer": "X-Yachts",
            "boat_model": "X4.9",
            "boat_year": 2015,
            "hull_material": "grp_solid",
            "hull_construction": "hand_layup",
            "propulsion": "sail",
            "issues": [{
                "category": "structural",
                "zone_type": "deck",
                "description": "Bug-Reling-Befestigung zeigt Risse unter Backstag-Belastung nach 5 Jahren intensiver Nutzung",
                "severity": "major",
                "boat_age_months": 60,
            }],
            "positives": [],
            "reliability": 0.70,
        })],

        # Lagoon 52 F — Catamaran beam cracking (1 report)
        *[({
            "source_forum": "catamaranforum.com",
            "boat_manufacturer": "Lagoon",
            "boat_model": "52 F",
            "boat_year": 2014,
            "hull_material": "grp_solid",
            "hull_construction": "hand_layup",
            "propulsion": "sail",
            "issues": [{
                "category": "structural",
                "zone_type": "deck",
                "description": "Verbindungsträger zwischen Rümpfen zeigt Risse unter asymmetrischer Belastung",
                "severity": "critical",
                "boat_age_months": 72,
            }],
            "positives": [],
            "reliability": 0.57,
        })],
    ]

    # Insert reports
    for rd in reports_data:
        report = CommunityReport(**rd)
        db.add(report)
    await db.flush()

    # Run aggregation
    all_reports = (await db.execute(select(CommunityReport))).scalars().all()
    report_dicts = [{
        "id": r.id,
        "boat_manufacturer": r.boat_manufacturer,
        "boat_model": r.boat_model,
        "hull_material": r.hull_material,
        "hull_construction": r.hull_construction,
        "propulsion": r.propulsion,
        "issues": r.issues or [],
        "positives": r.positives or [],
        "reliability": r.reliability,
    } for r in all_reports]

    pattern_dicts = aggregate_reports_to_patterns(report_dicts)
    for pd in pattern_dicts:
        pattern = CommunityPattern(
            manufacturer=pd["manufacturer"],
            boat_model=pd["boat_model"],
            issue_category=pd["issue_category"],
            zone_type=pd["zone_type"],
            description=pd["description"],
            report_count=pd["report_count"],
            severity_mode=pd["severity_mode"],
            typical_onset_years=pd["typical_onset_years"],
            materials_involved=pd["materials_involved"],
            construction_methods_involved=pd["construction_methods_involved"],
            confidence=pd["confidence"],
            source_report_ids=pd["source_report_ids"],
            is_positive=pd.get("is_positive", False),
        )
        db.add(pattern)

    await db.commit()
    logger.info(f"Seeded {len(reports_data)} community reports → {len(pattern_dicts)} patterns")


if __name__ == "__main__":
    asyncio.run(seed())
