"""Knowledge base modules for yacht design analysis.

Provides comprehensive domain knowledge across all craftsmanship disciplines:
- Construction weak-point analysis (FMEA)
- Textile/sewing craftsmanship (thread, stitch, needle)
- Wood joinery and finishing
- Composite lamination and processing
- Coating and painting systems
- Fasteners and hardware mounting
- Custom fitting and adaptation
- Seals, gaskets and sealing technology
- Electrical and electronics systems
- Plumbing, sanitation and fluid systems
- Rigging, standing and running rigging
- Propulsion, engines and drive trains
- Hull forms and hydrodynamics
- Norms, standards and regulations
- Forensic failure analysis and degradation cycles
- Inspection methods and condition assessment
- Practical owner experience and manufacturer patterns
"""

from .construction_weakpoints import (
    ZONE_WEAKPOINTS,
    CONSTRUCTION_METHOD_RISKS,
    GALVANIC_CORROSION_TABLE,
    JOINT_FAILURE_MODES,
    WEAR_PATTERN_DATABASE,
    get_weakpoints_for_boat,
    get_joint_inspection_schedule,
    assess_galvanic_risk,
    get_construction_method_risks,
)

from .craftsmanship import (
    MARINE_THREADS,
    STITCH_PATTERNS,
    MATERIAL_STITCH_COMPATIBILITY,
    NEEDLE_TYPES,
    JOINING_TECHNIQUES,
    SEAM_QUALITY_ASSESSMENT,
    SURFACE_TREATMENTS,
    SAIL_FABRICS,
    MARINE_ZIPPERS,
    MARINE_SNAP_FASTENERS,
    KEDER_PIPING,
    MARINE_VELCRO,
    MARINE_FOAM_TYPES,
    assess_thread_for_application,
    assess_stitch_pattern,
    get_full_recommendation,
)

from .craftsmanship_wood import (
    WOOD_JOINTS,
    WOOD_FINISHING,
    WOOD_BENDING,
    WOOD_FITTING_TECHNIQUES,
    WOOD_TOOL_ASSESSMENT,
    WOOD_SPECIES_MARINE,
    STEAM_BENDING_PARAMS,
    WOOD_CNC_MARINE,
    assess_wood_joint,
)

from .craftsmanship_lamination import (
    LAMINATION_TECHNIQUES,
    FIBER_TYPES,
    RESIN_SYSTEMS,
    LAMINATE_SCHEDULES,
    SANDWICH_CORE_PROCESSING,
    REPAIR_TECHNIQUES,
    assess_laminate_quality,
)

from .craftsmanship_coating import (
    PAINT_SYSTEMS,
    SURFACE_PREPARATION,
    APPLICATION_METHODS,
    DEFECT_DIAGNOSIS,
    MEASUREMENT_METHODS,
    POLISHING_SYSTEMS,
    FOIL_WRAPPING,
    METAL_SURFACE_TREATMENTS,
    assess_coating_system,
)

from .craftsmanship_fasteners import (
    MARINE_FASTENERS,
    DECK_HARDWARE_MOUNTING,
    THROUGH_HULL_FITTINGS,
    RIGGING_HARDWARE,
    SEALANT_SELECTION_MATRIX,
    TORQUE_PATTERNS,
    THREAD_TYPES_MARINE,
    THREAD_LOCKING,
    WELDING_MARINE,
    assess_fastener_installation,
)

from .craftsmanship_custom import (
    CUSTOM_FIT_TECHNIQUES,
    INTERIOR_FITTING,
    ALIGNMENT_AND_FAIRNESS,
    GAP_AND_TOLERANCE_STANDARDS,
    CUSTOM_METALWORK,
    SYSTEMS_INTEGRATION,
    assess_custom_fit,
)

from .craftsmanship_seals import (
    SEAL_MATERIALS,
    SEAL_PROFILES,
    MEDIA_COMPATIBILITY,
    MEDIA_NAMES_DE,
    O_RING_SIZING,
    COMPRESSION_BEHAVIOR,
    SEALING_SURFACE_PREPARATION,
    SEAL_INSPECTION_CRITERIA,
    assess_seal_installation,
)

from .yacht_systems_electrical import (
    calculate_cable_size,
    assess_electrical_installation,
)

from .yacht_systems_plumbing import (
    assess_plumbing_installation,
)

from .yacht_systems_rigging import (
    assess_rigging_condition,
)

from .yacht_systems_propulsion import (
    DRIVE_TRAIN_TYPES,
    PROPELLER_TYPES,
    COOLING_SYSTEMS,
    EXHAUST_SYSTEMS,
    FUEL_CONSUMPTION_DATABASE,
    TRANSMISSION_TYPES,
    ENGINE_MAINTENANCE_SCHEDULE,
    PROPULSION_SELECTION_MATRIX,
    assess_propulsion_system,
)

from .hull_forms_hydrodynamics import (
    assess_hull_design,
    calculate_fn_at_speed,
    assess_stability_iso_category,
)

from .norms_standards import (
    assess_compliance,
    recommend_standards,
)

from .forensic_failure_analysis import (
    MATERIAL_INTERACTION_FAILURES,
    CUMULATIVE_DEGRADATION_CYCLES,
    HIDDEN_MOISTURE_PATHS,
    CHEMICAL_INCOMPATIBILITIES,
    OSMOSIS_KNOWLEDGE,
    LAMINATE_DEFECTS,
    GALVANIC_SERIES_MARINE,
    TEAK_DECK_KNOWLEDGE,
    assess_failure_risk,
)

from .inspection_knowledge import (
    assess_inspection_findings,
)

from .practical_experience import (
    MANUFACTURER_PATTERNS,
    REAL_FAILURE_CASES,
    PROCESSING_QUALITY_PRINCIPLES,
    SEACOCK_KNOWLEDGE,
    CORE_MATERIAL_KNOWLEDGE,
    assess_manufacturer_risk,
)
