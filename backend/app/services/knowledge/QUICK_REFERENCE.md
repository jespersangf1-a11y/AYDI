# Construction Weak-Points Knowledge Base - Quick Reference

## Import Statement
```python
from backend.app.services.knowledge import (
    get_weakpoints_for_boat,
    get_joint_inspection_schedule,
    assess_galvanic_risk,
    get_construction_method_risks,
    ZONE_WEAKPOINTS,
    CONSTRUCTION_METHOD_RISKS,
    GALVANIC_CORROSION_TABLE,
    JOINT_FAILURE_MODES,
    WEAR_PATTERN_DATABASE,
)
```

## Common Tasks

### 1. Get Risk Assessment for a Boat Design
```python
weakpoints = get_weakpoints_for_boat(
    boat_class="cruising_sail",
    zones=["hull_below_waterline", "deck", "rigging"]
)

# Access results:
print(weakpoints['summary']['total_critical_areas'])
print(weakpoints['summary']['critical_severity_count'])

# Get top priority areas:
for area in weakpoints['summary']['priority_focus_areas']:
    print(f"{area['location']}: {area['failure_mode']}")
```

### 2. Check Material Compatibility
```python
risk = assess_galvanic_risk("stainless_316", "aluminum_5083")

if risk:
    print(f"Risk: {risk['risk']}")          # high/medium/low/none
    print(f"Voltage: {risk['voltage_diff_mv']}mV")
    print(f"Notes: {risk['notes']}")
```

### 3. Review Construction Method Risks
```python
method = get_construction_method_risks("vacuum_infusion")

# Check environmental requirements
env = method['environmental_requirements']
print(f"Temperature: {env['temperature_min_celsius']}-{env['temperature_max_celsius']}°C")
print(f"Humidity: ≤{env['humidity_max_percent']}%")
print(f"Cure time: {env['cure_time_hours']}h")

# Review quality risks
for risk in method['quality_risks']:
    print(f"{risk['defect']}: {risk['severity']}")

# Common mistakes to avoid
for mistake in method['common_mistakes']:
    print(f"- {mistake}")
```

### 4. Get Joint Inspection Schedule
```python
schedule = get_joint_inspection_schedule("hull_deck_joint", "cruising_sail")

print(schedule['inspection_protocol'])
print(schedule['recommended_materials'])

for mode in schedule['failure_modes']:
    print(f"{mode['mode']} (Onset: ~{mode['onset_years']} years)")
```

### 5. Find Weak-Points in Specific Zone
```python
hull_weakpoints = ZONE_WEAKPOINTS["hull_below_waterline"]

for critical_area in hull_weakpoints["critical_areas"]:
    print(f"{critical_area['location']}: {critical_area['failure_mode']}")

for vector in hull_weakpoints["water_ingress_vectors"]:
    print(f"Water entry: {vector['entry_point']}")
```

## Boat Classes
| Class | Usage |
|-------|-------|
| `small_sail` | Racing dinghies, day sailors (under 8m) |
| `cruising_sail` | Offshore cruising sailboats (8-20m) |
| `racing_sail` | High-performance racing designs |
| `daysailer` | Coastal day boats (5-12m) |
| `motorsailer` | Hybrid sail-power designs |
| `large_motor` | Power yachts, trawlers (>15m) |

## Zone Names
```
hull_below_waterline    deck                 mast_step
hull_above_waterline    cabin_top            chainplates
keel                    cockpit              windows
rudder                  flybridge            hatches
through_hulls           transom              propeller_shaft
stern_tube              anchor_locker        bow_thruster
engine_room             fuel_system          electrical_system
rigging                 stanchions           pulpit
```

## Severity Levels
- **critical** - Immediate risk to safety or structural integrity
- **major** - Significant risk requiring preventive maintenance
- **minor** - Cosmetic or low-impact issues

## Construction Methods
```
hand_layup              - Manual fiber/resin application
vacuum_infusion         - Bagged lamination with pump
prepreg_autoclave       - Pre-impregnated fiber in autoclave
resin_transfer_molding  - Closed-mold injection
spray_layup             - Simultaneous fiber/resin spray
aluminum_welded         - Marine aluminum construction
steel_welded            - Steel hull fabrication
strip_plank_epoxy       - Wooden plank epoxy bonding
cold_molded             - Epoxy-bonded wood layers
foam_sandwich           - Composite core construction
```

## Material Pairing Risk Quick Reference

| Material Pair | Risk | Notes |
|---|---|---|
| SS316 + Al5083 | HIGH | Avoid direct contact |
| SS316 + Bronze | MEDIUM | Use isolators |
| SS316 + Carbon | HIGH | Rapid SS attack |
| Al5083 + Bronze | HIGH | Use isolators |
| SS316 + Zinc | HIGH | Design for replacement |
| SS316 + Titanium | NONE | Fully compatible |

## Joint Types
```
hull_deck_joint         - Primary water barrier
keel_hull_joint         - Structural appendage bond
through_hull_fitting    - Sea water penetrations
window_frame            - Glazing and seals
hatch_seal              - Access cover integrity
chainplate_bulkhead     - Rigging attachment points
mast_step_beam          - Mast support structure
rudder_bearing          - Steering pivot point
propshaft_seal          - Engine propulsion seal
fuel_tank_mount         - Fuel system isolation
battery_mount           - Electrical power mounting
```

## Common Failure Onset Times

| Component | Years | Symptoms |
|---|---|---|
| Battery terminals | 3 | Green corrosion deposits |
| Through-hull seals | 4 | Water weeping |
| Hatch gaskets | 5-7 | Loses seal tightness |
| Sealant caulk | 5-6 | Cracks appear |
| Stanchion bases | 6 | Base loosens |
| Rudder bearing | 7-8 | Hard to turn |
| Osmotic blistering | 5-8 | Blisters below WL |
| Hull-deck joint | 8 | Visible separation |

## Data Structure Quick Look

### Critical Area
```python
{
    "location": "Keel Root Fillet",
    "failure_mode": "Delamination under load",
    "severity": "critical",
    "onset_years": 8,
    "symptoms": "Cracking at root, hollow sound...",
    "root_cause": "Insufficient fillet radius...",
    "affected_boat_classes": ["racing_sail", "small_sail"]
}
```

### Water Ingress Vector
```python
{
    "entry_point": "Hull-deck joint exterior",
    "mechanism": "Capillary action under caulk",
    "detection_method": "Water spray test, tracer dye",
    "prevention": "Proper slope design, quality caulking"
}
```

### Material Pairing
```python
{
    "risk": "high",
    "voltage_diff_mv": 950,
    "notes": "One of worst pairs, avoid direct contact"
}
```

### Wear Pattern
```python
{
    "zone": "hull_below_waterline",
    "component": "Through-hull fitting seal",
    "wear_type": "corrosion",
    "typical_lifespan_years": 4,
    "early_warning_signs": "White corrosion deposits...",
    "affected_boat_classes": ["all"]
}
```

## Severity Color Coding (for UI)
- 🔴 **CRITICAL** - Red - Immediate action required
- 🟠 **MAJOR** - Orange - Preventive maintenance needed
- 🟡 **MINOR** - Yellow - Monitor, cosmetic issue

## Risk Levels (Material Pairing)
- ⚠️ **HIGH** - Voltage diff > 500mV, avoid contact
- ⚡ **MEDIUM** - Voltage diff 100-500mV, use isolation
- ✓ **LOW** - Voltage diff < 100mV, usually OK
- ✓✓ **NONE** - Fully compatible

## Quick Diagnosis Guide

### Water Entering Cabin
1. Check ZONE_WEAKPOINTS["hull_deck_joint"]["water_ingress_vectors"]
2. Check hatches, windows, through-hulls
3. Use get_weakpoints_for_boat() with relevant zones
4. Review prevention strategies

### Corrosion Issue
1. Use assess_galvanic_risk() to check material pair
2. Review GALVANIC_CORROSION_TABLE for notes
3. Check WEAR_PATTERN_DATABASE for degradation timeline
4. Plan protection/replacement schedule

### Construction Quality Concern
1. Use get_construction_method_risks() for method used
2. Review quality_risks list
3. Check inspection_points for verification
4. Check common_mistakes to avoid

### Joint Failure Risk
1. Use get_joint_inspection_schedule() for joint type
2. Review documented failure_modes
3. Follow inspection_protocol
4. Use recommended_materials for repairs

## Database Size
- **Total Entries**: 182+
- **Total Zones**: 24
- **Total Construction Methods**: 10
- **Total Material Pairs**: 26
- **Total Joint Types**: 11
- **Total Wear Patterns**: 20+

## File Locations
```
/backend/app/services/knowledge/
├── construction_weakpoints.py     ← Main database
├── __init__.py                    ← Imports
├── usage_examples.py              ← 8 examples
├── README_WEAKPOINTS.md           ← Full docs
└── QUICK_REFERENCE.md             ← This file
```

## Example Workflow

```python
# 1. Get design risks
weakpoints = get_weakpoints_for_boat("cruising_sail", ["deck"])

# 2. Check material selections
for critical_area in weakpoints["critical_areas"]:
    if "aluminum" in critical_area["root_cause"].lower():
        risk = assess_galvanic_risk("stainless_316", "aluminum_5083")
        print(f"Material risk: {risk['risk']}")

# 3. Verify construction method
method_risks = get_construction_method_risks("vacuum_infusion")
print(f"Cure time: {method_risks['environmental_requirements']['cure_time_hours']}h")

# 4. Plan inspection schedule
schedule = get_joint_inspection_schedule("hull_deck_joint", "cruising_sail")
print(f"Inspection: {schedule['inspection_protocol']}")

# 5. Monitor for early warnings
for wear in weakpoints.get("wear_patterns", []):
    if wear["typical_lifespan_years"] < 5:
        print(f"MONITOR: {wear['component']} - {wear['early_warning_signs']}")
```

## Troubleshooting

**Question**: "How do I know which zones my design has?"
**Answer**: List zones you've defined in your layout and call `get_weakpoints_for_boat()` with that list.

**Question**: "What materials are safe to use together?"
**Answer**: Use `assess_galvanic_risk()` for each pair. High-risk pairs need isolation with sealant compound.

**Question**: "How long does construction take?"
**Answer**: Review `environmental_requirements` under `get_construction_method_risks()` for cure times.

**Question**: "What should I inspect and when?"
**Answer**: Use `get_joint_inspection_schedule()` for each joint type - it includes inspection protocol.

**Question**: "What are the most critical areas?"
**Answer**: Call `get_weakpoints_for_boat()` and check `priority_focus_areas` in summary.

---

**Version**: 1.0
**Updated**: 2026-03-20
**Status**: Production Ready
