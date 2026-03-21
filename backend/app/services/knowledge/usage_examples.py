"""Usage examples for the Construction Weak-Points Knowledge Base.

Demonstrates practical applications of the FMEA database for yacht design analysis.
"""

from typing import Dict, List, Any
from .construction_weakpoints import (
    get_weakpoints_for_boat,
    get_construction_method_risks,
    assess_galvanic_risk,
    get_joint_inspection_schedule,
    ZONE_WEAKPOINTS,
    CONSTRUCTION_METHOD_RISKS,
    GALVANIC_CORROSION_TABLE,
)


def example_1_basic_weakpoint_analysis():
    """Example 1: Analyze weak-points for a specific boat design."""
    print("\n" + "=" * 70)
    print("EXAMPLE 1: Basic Weak-Point Analysis")
    print("=" * 70)

    # Scenario: Designing a 12m cruising sailboat with galley, engine, rigging
    boat_zones = [
        "hull_below_waterline",
        "hull_above_waterline",
        "deck",
        "cockpit",
        "keel",
        "rudder",
        "engine_room",
        "rigging",
    ]

    weakpoints = get_weakpoints_for_boat("cruising_sail", boat_zones)

    print(f"\nBoat Class: {weakpoints['boat_class']}")
    print(f"Design Zones: {len(weakpoints['zones_present'])}")
    print(f"\nRISK SUMMARY:")
    print(f"  Total critical areas identified: {weakpoints['summary']['total_critical_areas']}")
    print(f"  Critical severity items: {weakpoints['summary']['critical_severity_count']}")
    print(f"  Major severity items: {weakpoints['summary']['major_severity_count']}")
    print(f"  Water ingress vectors: {weakpoints['summary']['water_ingress_vectors_count']}")

    print(f"\nTOP 5 PRIORITY FOCUS AREAS:")
    for i, area in enumerate(weakpoints['summary']['priority_focus_areas'], 1):
        print(f"\n{i}. {area['zone'].upper()}")
        print(f"   Location: {area['location']}")
        print(f"   Failure Mode: {area['failure_mode']}")
        print(f"   Onset: ~{area['onset_years']} years")
        print(f"   Root Cause: {area['root_cause']}")


def example_2_material_compatibility():
    """Example 2: Check material compatibility in hull structure."""
    print("\n" + "=" * 70)
    print("EXAMPLE 2: Material Compatibility Analysis")
    print("=" * 70)

    # Scenario: Evaluating material selections for through-hull fittings
    material_pairs_to_check = [
        ("stainless_316", "aluminum_5083"),  # Hull material
        ("stainless_316", "bronze"),  # Through-hull fitting with strainer
        ("stainless_316", "zinc"),  # Sacrificial anode
        ("stainless_316", "carbon_fiber"),  # Deck reinforcement
    ]

    print("\nMaterial Compatibility Assessment:")
    print("-" * 70)

    for mat1, mat2 in material_pairs_to_check:
        risk = assess_galvanic_risk(mat1, mat2)
        if risk:
            risk_icon = "⚠️ HIGH" if risk["risk"] == "high" else "⚡ MEDIUM" if risk["risk"] == "medium" else "✓ LOW"
            print(f"\n{mat1.upper()} + {mat2.upper()}")
            print(f"  Risk Level: {risk_icon}")
            print(f"  Voltage Differential: {risk['voltage_diff_mv']}mV")
            print(f"  Notes: {risk['notes']}")


def example_3_construction_method_selection():
    """Example 3: Select construction method and assess quality risks."""
    print("\n" + "=" * 70)
    print("EXAMPLE 3: Construction Method Risk Assessment")
    print("=" * 70)

    # Scenario: Choosing between hand layup and vacuum infusion for hull
    methods_to_evaluate = ["hand_layup", "vacuum_infusion", "foam_sandwich"]

    for method in methods_to_evaluate:
        risks = get_construction_method_risks(method)

        print(f"\n{method.upper().replace('_', ' ')}")
        print("-" * 70)

        print("Environmental Requirements:")
        env = risks["environmental_requirements"]
        print(f"  Temperature: {env['temperature_min_celsius']}–{env['temperature_max_celsius']}°C")
        print(f"  Humidity: ≤{env['humidity_max_percent']}%")
        print(f"  Cure time: {env['cure_time_hours']} hours")
        if env.get('post_cure_temperature_celsius'):
            print(f"  Post-cure: {env['post_cure_temperature_celsius']}°C for {env['post_cure_time_hours']} hours")

        print("\nQuality Risks to Monitor:")
        for risk in risks["quality_risks"][:2]:  # Show top 2
            severity_icon = "🔴 CRITICAL" if risk["severity"] == "critical" else "🟠 MAJOR"
            print(f"  {severity_icon}: {risk['defect']}")
            print(f"    → Detection: {risk['detection']}")


def example_4_joint_design_verification():
    """Example 4: Verify joint design against failure modes."""
    print("\n" + "=" * 70)
    print("EXAMPLE 4: Joint Design Verification")
    print("=" * 70)

    # Scenario: Designing hull-deck joint for cruising sailboat
    joint_type = "hull_deck_joint"
    boat_class = "cruising_sail"

    schedule = get_joint_inspection_schedule(joint_type, boat_class)

    print(f"\nJoint Type: {joint_type.upper().replace('_', ' ')}")
    print(f"Boat Class: {boat_class.upper().replace('_', ' ')}")

    print(f"\nDocumented Failure Modes:")
    for mode in schedule["failure_modes"]:
        severity_icon = "🔴" if mode["severity"] == "critical" else "🟠"
        print(f"\n{severity_icon} {mode['mode']}")
        print(f"  Typical Onset: ~{mode['onset_years']} years")
        print(f"  Symptoms: {mode['symptoms']}")

    print(f"\nInspection Protocol:")
    print(f"{schedule['inspection_protocol']}")

    print(f"\nRecommended Materials & Construction:")
    print(f"{schedule['recommended_materials']}")


def example_5_water_intrusion_risk_assessment():
    """Example 5: Assess water intrusion vectors for critical zones."""
    print("\n" + "=" * 70)
    print("EXAMPLE 5: Water Intrusion Risk Assessment")
    print("=" * 70)

    # Get weakpoints for deck zone
    deck_weakpoints = get_weakpoints_for_boat("large_motor", ["deck"])

    print(f"\nWater Ingress Vectors for DECK Zone:")
    print("-" * 70)

    for vector in deck_weakpoints["water_ingress_vectors"]:
        print(f"\nEntry Point: {vector['entry_point']}")
        print(f"  Mechanism: {vector['mechanism']}")
        print(f"  Detection: {vector['detection_method']}")
        print(f"  Prevention: {vector['prevention']}")


def example_6_construction_schedule_impact():
    """Example 6: Analyze impact of construction method on timeline."""
    print("\n" + "=" * 70)
    print("EXAMPLE 6: Construction Timeline Analysis")
    print("=" * 70)

    methods = {
        "hand_layup": "Traditional method, lower cost, longer cure",
        "vacuum_infusion": "Modern, better quality, moderate timeline",
        "prepreg_autoclave": "Premium quality, fastest cure, highest cost",
    }

    print("\nCure Time Comparison:")
    print("-" * 70)

    for method_key, description in methods.items():
        risks = get_construction_method_risks(method_key)
        cure = risks["environmental_requirements"]["cure_time_hours"]
        post_cure = risks["environmental_requirements"].get("post_cure_time_hours", 0)
        total = cure + post_cure

        print(f"\n{method_key.upper().replace('_', ' ')}")
        print(f"  Initial cure: {cure} hours")
        print(f"  Post-cure: {post_cure} hours")
        print(f"  Total time: {total} hours ({total/24:.1f} days)")
        print(f"  Notes: {description}")


def example_7_galvanic_protection_design():
    """Example 7: Design galvanic protection strategy."""
    print("\n" + "=" * 70)
    print("EXAMPLE 7: Galvanic Protection Strategy")
    print("=" * 70)

    print("\nHigh-Risk Material Pairings and Mitigation:")
    print("-" * 70)

    risky_materials = [
        ("stainless_316", "aluminum_5083"),
        ("stainless_316", "carbon_fiber"),
        ("aluminum_5083", "bronze"),
    ]

    for mat1, mat2 in risky_materials:
        risk = assess_galvanic_risk(mat1, mat2)
        if risk and risk["risk"] == "high":
            print(f"\n⚠️  {mat1.upper()} + {mat2.upper()}")
            print(f"   Risk: {risk['risk'].upper()}")
            print(f"   Voltage: {risk['voltage_diff_mv']}mV")
            print(f"   MITIGATION:")
            print(f"   • Use bedding compound isolation")
            print(f"   • Install sacrificial anodes")
            print(f"   • Consider alternative material pairing")
            print(f"   • Implement impressed current protection")


def example_8_predictive_maintenance_schedule():
    """Example 8: Generate predictive maintenance schedule."""
    print("\n" + "=" * 70)
    print("EXAMPLE 8: Predictive Maintenance Schedule")
    print("=" * 70)

    # Get wear patterns for a cruising sailboat
    from .construction_weakpoints import WEAR_PATTERN_DATABASE

    cruising_wear_patterns = [
        wp for wp in WEAR_PATTERN_DATABASE
        if "cruising_sail" in wp["affected_boat_classes"] or "all" in wp["affected_boat_classes"]
    ]

    print(f"\nPredicted Component Lifespan (Cruising Sailboat):")
    print("-" * 70)

    # Sort by lifespan
    sorted_patterns = sorted(
        cruising_wear_patterns,
        key=lambda x: x["typical_lifespan_years"]
    )

    print("\nEARLY ATTENTION (3-5 years):")
    for pattern in sorted_patterns:
        if pattern["typical_lifespan_years"] <= 5:
            print(f"  • {pattern['component']} ({pattern['zone']})")
            print(f"    Typical life: {pattern['typical_lifespan_years']} years")
            print(f"    Watch for: {pattern['early_warning_signs']}")

    print("\nMIDTERM MAINTENANCE (6-8 years):")
    for pattern in sorted_patterns:
        if 5 < pattern["typical_lifespan_years"] <= 8:
            print(f"  • {pattern['component']} ({pattern['zone']})")
            print(f"    Typical life: {pattern['typical_lifespan_years']} years")


def run_all_examples():
    """Execute all usage examples."""
    examples = [
        example_1_basic_weakpoint_analysis,
        example_2_material_compatibility,
        example_3_construction_method_selection,
        example_4_joint_design_verification,
        example_5_water_intrusion_risk_assessment,
        example_6_construction_schedule_impact,
        example_7_galvanic_protection_design,
        example_8_predictive_maintenance_schedule,
    ]

    for example in examples:
        try:
            example()
        except Exception as e:
            print(f"\nError in {example.__name__}: {e}")

    print("\n" + "=" * 70)
    print("ALL EXAMPLES COMPLETED")
    print("=" * 70)


if __name__ == "__main__":
    run_all_examples()
