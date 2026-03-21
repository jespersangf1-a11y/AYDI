# Construction Weak-Points Knowledge Base

## Overview

The Construction Weak-Points Knowledge Base is a comprehensive FMEA (Failure Mode and Effects Analysis) database for yacht design. It provides detailed information about potential construction defects, failure modes, and preventive measures organized by structural zone, construction method, and material pairings.

## Database Contents

### 1. ZONE_WEAKPOINTS (24 zones, 61+ critical areas)

Organized by structural zone type with four categories per zone:

- **critical_areas**: Specific weak points with:
  - Location description (German)
  - Failure mode description
  - Severity level (critical/major/minor)
  - Typical onset time in years
  - Observable symptoms
  - Root cause analysis
  - Affected boat classes

- **water_ingress_vectors**: Potential water entry paths:
  - Entry point identification
  - Mechanism of ingress
  - Detection methods
  - Prevention strategies

- **chafing_zones**: Friction/abrasion areas:
  - Location and surfaces
  - Material pairs at risk
  - Prevention recommendations

Covered zones:
- Hull below/above waterline
- Deck systems
- Cabin top
- Cockpit area
- Keel, rudder, mast step
- Chainplates, windows, hatches
- Through-hulls, propeller shaft
- Stern tube, bow thruster
- Flybridge, transom
- Anchor locker, engine room
- Fuel and electrical systems
- Rigging, stanchions, pulpit

### 2. CONSTRUCTION_METHOD_RISKS (10 methods, 200+ quality risks)

Detailed risk profiles for each construction method:

- **hand_layup**: Manual fiber placement with resin
- **vacuum_infusion**: Bagged lamination with vacuum pump
- **prepreg_autoclave**: Pre-impregnated fiber with autoclave
- **resin_transfer_molding**: Closed-mold injection process
- **spray_layup**: Simultaneous fiber/resin spraying
- **aluminum_welded**: Marine aluminum construction
- **steel_welded**: Steel hull fabrication
- **strip_plank_epoxy**: Wooden plank construction
- **cold_molded**: Epoxy-bonded wood layers
- **foam_sandwich**: Composite core construction

For each method:
- Quality risks (defect, cause, detection, severity)
- Environmental requirements (temperature, humidity, cure time)
- Common installation mistakes
- Inspection points for quality control

### 3. GALVANIC_CORROSION_TABLE (26 material pairs)

Comprehensive galvanic compatibility matrix:

Material pairs include:
- Stainless steel (304, 316)
- Aluminum alloys (5083, 6082)
- Bronze, brass, copper
- Carbon fiber composites
- Zinc, mild steel, titanium
- Monel, lead

For each pairing:
- Risk level (high/medium/low/none)
- Voltage differential in mV
- Application notes and mitigation strategies

### 4. JOINT_FAILURE_MODES (11 joint types)

Detailed failure analysis for critical joints:

- Hull-deck joint
- Keel-hull bond
- Through-hull fittings
- Window frames
- Hatch seals
- Chainplate-bulkhead connections
- Mast step beam interfaces
- Rudder bearings
- Propeller shaft seals
- Fuel tank mounts
- Battery mounts

For each joint:
- Documented failure modes (with severity and onset time)
- Inspection protocols and frequency
- Recommended materials and construction methods

### 5. WEAR_PATTERN_DATABASE (20+ patterns)

Historical wear patterns organized by:
- Structural zone
- Component name
- Wear type (abrasion, fatigue, corrosion, UV, chemical)
- Typical lifespan in years
- Early warning signs
- Affected boat classes

## Usage Examples

### Basic Weak-Point Query

```python
from backend.app.services.knowledge import get_weakpoints_for_boat

# Get all weak-points relevant to a cruising sailboat
boat_weakpoints = get_weakpoints_for_boat(
    boat_class="cruising_sail",
    zones=["hull_below_waterline", "deck", "rigging"]
)

# Access results
print(f"Total critical areas: {boat_weakpoints['summary']['total_critical_areas']}")
print(f"Critical severity items: {boat_weakpoints['summary']['critical_severity_count']}")

# Get priority focus areas
for area in boat_weakpoints['summary']['priority_focus_areas']:
    print(f"CRITICAL: {area['location']} - {area['failure_mode']}")
```

### Material Compatibility Check

```python
from backend.app.services.knowledge import assess_galvanic_risk

# Check compatibility between two materials
risk = assess_galvanic_risk("stainless_316", "aluminum_5083")
if risk['risk'] == 'high':
    print(f"WARNING: {risk['notes']}")
    print(f"Voltage differential: {risk['voltage_diff_mv']}mV")
```

### Construction Method Risk Assessment

```python
from backend.app.services.knowledge import get_construction_method_risks

# Get risks for a specific construction method
hand_layup_risks = get_construction_method_risks("hand_layup")

print("Environmental Requirements:")
for key, value in hand_layup_risks['environmental_requirements'].items():
    print(f"  {key}: {value}")

print("\nCommon Mistakes to Avoid:")
for mistake in hand_layup_risks['common_mistakes']:
    print(f"  - {mistake}")
```

### Joint Inspection Schedule

```python
from backend.app.services.knowledge import get_joint_inspection_schedule

# Get inspection protocol for hull-deck joint
schedule = get_joint_inspection_schedule("hull_deck_joint", "cruising_sail")

print("Inspection Protocol:")
print(schedule['inspection_protocol'])
print("\nRecommended Materials:")
print(schedule['recommended_materials'])
```

## Data Structure Examples

### Critical Area Object
```python
{
    "location": "Keel Root Fillet",
    "failure_mode": "Delamination under load",
    "severity": "critical",
    "onset_years": 8,
    "symptoms": "Cracking at root, hollow sound when tapped, visible gap",
    "root_cause": "Insufficient fillet radius, impact loads, resin starvation",
    "affected_boat_classes": ["racing_sail", "small_sail", "daysailer"],
    "zone": "hull_below_waterline"
}
```

### Construction Method Risk Object
```python
{
    "defect": "Resin starvation",
    "cause": "Insufficient resin application, high fiber volume fraction",
    "detection": "Dry spots visible, high void content on cross-section",
    "severity": "critical"
}
```

### Galvanic Corrosion Entry
```python
{
    "risk": "high",
    "voltage_diff_mv": 950,
    "notes": "One of worst pairs, avoid direct contact"
}
```

## Helper Functions

### get_weakpoints_for_boat(boat_class, zones)
Filters weak-points by boat class and present zones.
- Returns summary statistics and priority focus areas

### get_joint_inspection_schedule(joint_type, boat_class)
Provides inspection protocols and material recommendations for specific joints.

### assess_galvanic_risk(material_1, material_2)
Assesses corrosion risk between material pairs.

### get_construction_method_risks(method)
Returns quality risks and environmental requirements for construction methods.

## Integration Points

This module is designed to integrate with:

1. **Structural Analysis** (`backend.app.services.analysis.structural`):
   - Cross-reference weak-points with structural load paths
   - Identify critical areas under high stress

2. **Materials Analysis** (`backend.app.services.analysis.materials`):
   - Check material compatibility
   - Assess durability against known failure modes

3. **Compliance Checking** (`backend.app.services.analysis.compliance`):
   - Ensure construction methods meet maritime standards
   - Verify inspection schedules meet regulatory requirements

4. **Production Analysis** (`backend.app.services.analysis.production`):
   - Guide manufacturing process specifications
   - Set quality control inspection points

## Database Statistics

- **Total zones**: 24
- **Total critical areas**: 61+
- **Total water ingress vectors**: 21+
- **Total chafing zones**: 10+
- **Total construction methods**: 10
- **Total material pairings**: 26
- **Total joint types**: 11
- **Total wear patterns**: 20+
- **Combined FMEA entries**: 200+

## Quality Assurance Notes

The database includes:
- Real marine engineering knowledge
- Typical failure onset times
- Specific symptom descriptions for field diagnosis
- Prevention and mitigation strategies
- Boat-class-specific risk profiles
- Material compatibility matrices
- Construction method specifications
- Inspection protocols and frequencies

## Language

- **User-facing descriptions**: German (all zone locations, component names, symptoms)
- **Technical notes**: English
- **Code comments**: English
- **Function docstrings**: English

## Future Extensions

Potential additions:
- Climate/salinity-specific modifications
- Budget-based remediation recommendations
- Historical failure statistics by manufacturer
- Expert interview notes on prevention methods
- Video/image references for diagnostic training
- Automated alert thresholds for boat monitoring systems
