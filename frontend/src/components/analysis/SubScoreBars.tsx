import { useState, useRef, useEffect } from 'react'

// German labels for every module sub-score key. Keys are the canonical English
// identifiers emitted by the analysis modules (weights keys); the UI is German,
// so an untranslated key here shows a raw identifier to the user (M-5). Keep in
// sync when a module adds a sub-score.
const SUB_SCORE_LABELS: Record<string, string> = {
  // ergonomics
  passage_width: 'Durchgangsbreiten',
  path_efficiency: 'Wegeeffizienz',
  crew_guest_separation: 'Crew/Gast-Trennung',
  accessibility: 'Erreichbarkeit',
  helm_ergonomics: 'Steuerstand-Ergonomie',
  heel_impact: 'Krängungseinfluss',
  morning_circulation: 'Morgendliche Zirkulation',
  access_complexity: 'Zugangskomplexität',
  // volume
  storage_ratio: 'Stauraumanteil',
  storage_distribution: 'Stauraumverteilung',
  storage_accessibility: 'Stauraum-Erreichbarkeit',
  utilization: 'Raumnutzung',
  room_proportion: 'Raumproportionen',
  // emotional
  sightline: 'Sichtlinien',
  sightline_rays: 'Sichtlinien-Analyse',
  ceiling_perception: 'Deckenwahrnehmung',
  light_distribution: 'Lichtverteilung',
  inside_outside_flow: 'Innen-Außen-Fluss',
  visual_calm: 'Visuelle Ruhe',
  // compliance
  escape_routes: 'Fluchtwege',
  fire_safety: 'Brandschutz',
  stability: 'Stabilität',
  railing: 'Reling',
  electrical_access: 'Elektrik-Zugang',
  ce_category: 'CE-Kategorie',
  escape_hatch: 'Fluchtluke',
  cockpit_drain: 'Cockpit-Entwässerung',
  companionway_sill: 'Niedergangs-Süllhöhe',
  ventilation: 'Belüftung',
  // production
  mold_complexity: 'Formwerkzeug-Komplexität',
  flat_panel_ratio: 'Flachpaneel-Anteil',
  form_complexity: 'Formkomplexität',
  standardization: 'Standardisierung',
  assembly_sequence: 'Montagereihenfolge',
  service_access: 'Wartungszugang',
  cable_routing: 'Kabelführung',
  // materials
  durability: 'Haltbarkeit',
  maintenance: 'Wartungsaufwand',
  known_issues: 'Bekannte Schwachstellen',
  compatibility: 'Materialverträglichkeit',
  weight: 'Gewicht',
  lifecycle_cost: 'Lebenszykluskosten',
  uv_exposure: 'UV-Belastung',
  moisture_risk: 'Feuchtigkeitsrisiko',
  // structural
  loading_conditions: 'Beladungszustände',
  trim: 'Längsschwerpunkt',
  fore_aft: 'Längsbalance',
  lateral: 'Querbalance',
  load_concentration: 'Lastkonzentration',
  heavy_placement: 'Schwergewichts-Platzierung',
  // cost
  material_costs: 'Materialkosten',
  labor_estimate: 'Arbeitsaufwand',
  cost_per_meter: 'Kosten pro Meter',
  distribution: 'Kostenverteilung',
  risk: 'Kostenrisiko',
  parametric_estimate: 'Parametrische Schätzung',
  // brand_dna
  topology: 'Zonentopologie',
  proportions: 'Proportionen',
  materials: 'Materialpalette',
  spatial: 'Räumliche Signatur',
  style: 'Stilkontinuität',
  // market
  price_positioning: 'Preispositionierung',
  competitive_position: 'Wettbewerbsposition',
  uniqueness: 'Eigenständigkeit',
  metric_comparison: 'Kennzahlen-Vergleich',
  furniture_ratio: 'Möblierungsanteil',
  gaps: 'Spaltmaße',
  design_warnings: 'Konstruktionshinweise',
  // service_patterns
  zone_issues: 'Zonen-Probleme',
  age_patterns: 'Altersmuster',
  material_failures: 'Materialversagen',
}

interface SubScoreBarsProps {
  subScores: Record<string, number>
}

interface BarItemProps {
  label: string
  value: number
  index: number
}

function BarItem({ label, value, index }: BarItemProps) {
  const [showTooltip, setShowTooltip] = useState(false)
  const [truncated, setTruncated] = useState(false)
  const labelRef = useRef<HTMLSpanElement>(null)

  useEffect(() => {
    if (labelRef.current) {
      setTruncated(labelRef.current.scrollWidth > labelRef.current.clientWidth)
    }
  }, [label])

  const gradientColor =
    value >= 80
      ? 'from-emerald-500 to-emerald-400'
      : value >= 60
        ? 'from-amber-500 to-amber-400'
        : value >= 40
          ? 'from-orange-500 to-orange-400'
          : 'from-red-500 to-red-400'

  return (
    <div>
      <div className="flex justify-between items-center mb-2">
        <div className="relative flex-1 mr-2">
          <span
            ref={labelRef}
            className="label-premium block truncate"
            title={truncated ? label : undefined}
          >
            {label}
          </span>
          {truncated && showTooltip && (
            <div className="absolute bottom-full left-0 mb-2 px-2 py-1 bg-white text-navy-800 text-xs rounded whitespace-nowrap z-10 border border-sand-200 shadow-md">
              {label}
            </div>
          )}
        </div>
        <div className="relative">
          <span className="font-mono text-sm font-semibold text-navy-900">{Math.round(value)}</span>
          {showTooltip && (
            <div className="absolute bottom-full right-0 mb-2 px-2.5 py-1 bg-white text-navy-800 text-xs rounded border border-sand-200 shadow-md whitespace-nowrap">
              {Math.round(value)} / 100
            </div>
          )}
        </div>
      </div>

      <div
        className="h-1.5 bg-sand-200 rounded-full overflow-hidden cursor-help transition-all duration-200 hover:h-2"
        onMouseEnter={() => setShowTooltip(true)}
        onMouseLeave={() => setShowTooltip(false)}
      >
        <div
          className={`h-full rounded-full bg-gradient-to-r ${gradientColor} animate-fill-bar stagger-${Math.min(index + 1, 8)}`}
          style={{
            width: `${value}%`,
          }}
        />
      </div>
    </div>
  )
}

export default function SubScoreBars({ subScores }: SubScoreBarsProps) {
  return (
    <div className="space-y-5">
      {Object.entries(subScores).map(([key, value], index) => (
        <BarItem
          key={key}
          label={SUB_SCORE_LABELS[key] || key}
          value={value}
          index={index}
        />
      ))}

    </div>
  )
}
