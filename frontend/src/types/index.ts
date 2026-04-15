export type BoatClass =
  | 'small_sail'
  | 'cruising_sail'
  | 'racing_sail'
  | 'daysailer'
  | 'motorsailer'
  | 'catamaran_sail'
  | 'catamaran_motor'
  | 'small_motor'
  | 'large_motor'
  | 'sport_cruiser'
  | 'trawler'
  | 'explorer'
  | 'superyacht'
export type ProjectStatus = 'draft' | 'active' | 'review' | 'archived'

export interface ZoneData {
  name: string
  zone_type: string
  polygon: number[][]
  height_mm?: number | null
  is_crew_area: boolean
  is_guest_area: boolean
  visibility_angle?: number | null
  properties?: Record<string, unknown> | null
}

export interface PassageData {
  from_zone: string
  to_zone: string
  width_mm: number
  length_mm?: number | null
  points?: number[][] | null
  is_primary: boolean
}

export interface Project {
  id: string
  name: string
  description: string | null
  boat_class: BoatClass
  length_m: number
  beam_m: number
  status: ProjectStatus
  created_at: string
  updated_at: string
}

export interface ProjectCreate {
  name: string
  description?: string
  boat_class: BoatClass
  length_m: number
  beam_m: number
}

export interface Layout {
  id: string
  project_id: string
  name: string
  version: string
  file_path: string | null
  file_type: string | null
  zones: ZoneData[]
  passages: PassageData[]
  deck_height_mm: number
  created_at: string
  updated_at: string
}

export interface LayoutCreate {
  name: string
  version?: string
  zones: ZoneData[]
  passages: PassageData[]
  deck_height_mm?: number
}

export interface WarningData {
  code?: string | null
  severity: 'critical' | 'warning' | 'info'
  message: string
  location?: string | null
  value?: number | null
  threshold?: number | null
  suggestion: string
  norm?: string | null
}

export interface AnalysisResult {
  id: string
  project_id: string
  layout_id: string
  module: string
  overall_score: number
  sub_scores: Record<string, number>
  warnings: WarningData[]
  suggestions: string[]
  metrics: Record<string, unknown>
  config_used: Record<string, unknown>
  created_at: string
}

export interface DxfImportResponse {
  zones: ZoneData[]
  passages: PassageData[]
  warnings: string[]
}

// --- Deck (multi-deck 3D viewer) ---
export interface Deck {
  id: string
  layout_id: string
  deck_number: number
  name: string
  z_offset_mm: number
  height_mm: number
  is_open: boolean
  zones: ZoneData[]
  created_at: string
}

// --- Quick Analysis (Level 1) ---
export type ConfidenceLevel = 'measured' | 'calculated' | 'estimated' | 'benchmark'

export interface PublicSpecs {
  boat_class: BoatClass
  length_m: number
  beam_m?: number | null
  draft_m?: number | null
  displacement_kg?: number | null
  cabin_count?: number | null
  berth_count?: number | null
  head_count?: number | null
  cockpit_area_sqm?: number | null
  salon_area_sqm?: number | null
  pantry_type?: string | null
  helm_position?: string | null
  has_flybridge?: boolean | null
  has_crew_quarters?: boolean | null
  engine_hp?: number | null
  engine_count?: number | null
  fuel_capacity_l?: number | null
  water_capacity_l?: number | null
  sail_area_sqm?: number | null
  max_speed_kn?: number | null
  price_eur?: number | null
  year?: number | null
  brand?: string | null
  model_name?: string | null
  deck_height_mm?: number | null
  storage_volume_l?: number | null
}

export interface QuickModuleResult {
  available: boolean
  score?: number | null
  confidence?: ConfidenceLevel | null
  key_findings?: Array<{ finding: string; severity: string }> | null
  competitors_compared?: number | null
  strengths?: string[] | null
  weaknesses?: string[] | null
  reason?: string | null
}

export interface QuickAnalysisResponse {
  id: string
  analysis_level: string
  confidence: ConfidenceLevel
  specs_provided: number
  specs_inferred: number
  overall_assessment: {
    score: number
    confidence: ConfidenceLevel
    summary: string
  }
  modules: Record<string, QuickModuleResult>
  upgrade_prompt: {
    message: string
    additional_modules: string[]
  }
  specs_used: PublicSpecs
  created_at: string
}

// --- Service Reports ---
export type ReportType = 'warranty' | 'maintenance' | 'refit' | 'complaint' | 'feedback'
export type Severity = 'low' | 'medium' | 'high' | 'critical'

export interface ServiceReport {
  id: string
  project_id: string | null
  boat_class: BoatClass | null
  model_name: string | null
  report_type: ReportType
  category: string
  zone_type: string | null
  description: string
  severity: Severity
  root_cause: string | null
  resolution: string | null
  cost_eur: number | null
  hours_labor: number | null
  boat_age_months: number | null
  materials_involved: string[] | null
  images: string[] | null
  reported_by: string | null
  reported_at: string | null
  created_at: string
  metadata_extra: Record<string, unknown> | null
}

export interface ServiceReportCreate {
  report_type: ReportType
  category: string
  description: string
  severity?: Severity
  zone_type?: string | null
  root_cause?: string | null
  resolution?: string | null
  cost_eur?: number | null
  hours_labor?: number | null
  boat_age_months?: number | null
  materials_involved?: string[] | null
  reported_by?: string | null
  reported_at?: string | null
  project_id?: string | null
  boat_class?: BoatClass | null
  model_name?: string | null
  metadata_extra?: Record<string, unknown> | null
}

// --- Cost Items ---
export interface CostItem {
  id: string
  layout_id: string
  category: string
  subcategory: string | null
  description: string | null
  quantity: number
  unit: string
  unit_cost_eur: number
  total_cost_eur: number
  zone_name: string | null
  source: string
  notes: string | null
  created_at: string
}

export interface CostItemCreate {
  category: string
  subcategory?: string | null
  description?: string | null
  quantity?: number
  unit?: string
  unit_cost_eur: number
  total_cost_eur: number
  zone_name?: string | null
  source?: string
  notes?: string | null
}

export interface CostSummary {
  total_cost: number
  breakdown_by_category: Record<string, number>
  breakdown_by_zone: Record<string, number>
  item_count: number
}

// --- Structural Items ---
export interface StructuralItem {
  id: string
  layout_id: string
  name: string
  item_type: string
  zone_name: string | null
  weight_kg: number
  position_x_mm: number | null
  position_y_mm: number | null
  position_z_mm: number | null
  dimensions: Record<string, number> | null
  properties: Record<string, unknown> | null
  created_at: string
}

export interface StructuralItemCreate {
  name: string
  item_type: string
  weight_kg: number
  zone_name?: string | null
  position_x_mm?: number | null
  position_y_mm?: number | null
  position_z_mm?: number | null
  dimensions?: Record<string, number> | null
  properties?: Record<string, unknown> | null
}

// --- Competitors ---
export interface CompetitorModel {
  id: string
  brand: string
  model_name: string
  boat_class: BoatClass
  length_m: number | null
  beam_m: number | null
  year: number | null
  price_range_eur: { min: number; max: number } | null
  key_metrics: Record<string, number> | null
  source: string | null
  source_url: string | null
  images: string[] | null
  notes: string | null
  created_at: string
}

export interface CompetitorCreate {
  brand: string
  model_name: string
  boat_class: BoatClass
  length_m?: number | null
  beam_m?: number | null
  year?: number | null
  price_range_eur?: { min: number; max: number } | null
  key_metrics?: Record<string, number> | null
  source?: string | null
  source_url?: string | null
  notes?: string | null
}

// --- Brand References ---
export interface BrandReference {
  id: string
  shipyard_id: string | null
  model_name: string
  model_year: number | null
  boat_class: BoatClass
  layout_id: string | null
  features: Record<string, unknown> | null
  images: string[] | null
  notes: string | null
  created_at: string
}

export interface BrandReferenceCreate {
  model_name: string
  boat_class: BoatClass
  shipyard_id?: string | null
  model_year?: number | null
  layout_id?: string | null
  features?: Record<string, unknown> | null
  notes?: string | null
}

// --- Layout Versions ---
export interface LayoutVersion {
  id: string
  layout_id: string
  version_number: number
  parent_version_id: string | null
  zones_snapshot: ZoneData[] | null
  passages_snapshot: PassageData[] | null
  change_summary: string | null
  changed_by: string | null
  created_at: string
  tags: string[] | null
}

export interface LayoutVersionCreate {
  zones_snapshot: ZoneData[]
  passages_snapshot: PassageData[]
  change_summary?: string | null
  changed_by?: string | null
  tags?: string[] | null
}

// --- Layout Diff ---
export interface LayoutDiff {
  zones: {
    added: Array<{ name: string; zone: ZoneData }>
    removed: Array<{ name: string; zone: ZoneData }>
    modified: Array<{ name: string; changes: Array<{ field: string; old: unknown; new: unknown }> }>
    unchanged: string[]
  }
  passages: {
    added: Array<{ from_zone: string; to_zone: string; passage: PassageData }>
    removed: Array<{ from_zone: string; to_zone: string; passage: PassageData }>
    modified: Array<{ from_zone: string; to_zone: string; changes: Array<{ field: string; old: unknown; new: unknown }> }>
  }
  summary: {
    zones_added: number
    zones_removed: number
    zones_modified: number
    zones_unchanged: number
    passages_added: number
    passages_removed: number
    passages_modified: number
    total_area_change_sqm: number
    has_changes: boolean
  }
}

// --- Analysis Module Names ---
export type AnalysisModule =
  | 'ergonomics'
  | 'volume_storage'
  | 'emotional'
  | 'compliance'
  | 'production'
  | 'materials'
  | 'structural'
  | 'cost'
  | 'service_patterns'
  | 'brand_dna'
  | 'market'

export const ANALYSIS_MODULE_LABELS: Record<AnalysisModule, string> = {
  ergonomics: 'Ergonomie',
  volume_storage: 'Volumen & Stauraum',
  emotional: 'Emotionales Design',
  compliance: 'Normenprüfung',
  production: 'Produktionsfreundlichkeit',
  materials: 'Material & Qualität',
  structural: 'Strukturanalyse',
  cost: 'Kostenschätzung',
  service_patterns: 'Servicemuster',
  brand_dna: 'Marken-DNA',
  market: 'Markt & Wettbewerb',
}

// --- Image Upload & Visual Analysis ---
export type ImageType =
  | 'interior_overview'
  | 'interior_detail'
  | 'exterior_overview'
  | 'exterior_detail'
  | 'material_sample'
  | 'rendering'
  | 'floorplan_photo'
  | 'cockpit'
  | 'helm_station'

export const IMAGE_TYPE_LABELS: Record<ImageType, string> = {
  interior_overview: 'Innenraum Übersicht',
  interior_detail: 'Innenraum Detail',
  exterior_overview: 'Außenansicht',
  exterior_detail: 'Außendetail',
  material_sample: 'Materialprobe',
  rendering: 'Rendering',
  floorplan_photo: 'Grundriss-Foto',
  cockpit: 'Cockpit',
  helm_station: 'Steuerstand',
}

export type VisualConfidence = 'high' | 'medium' | 'low' | 'insufficient'

export interface VisualFinding {
  category: string
  observation: string
  assessment: string
  confidence: string
  location_in_image?: string | null
  detail?: string | null
  severity?: string | null
  suggestion?: string | null
}

export interface ImageUploadData {
  id: string
  project_id: string | null
  quick_analysis_id: string | null
  file_path: string
  file_type: string
  file_size_bytes: number
  image_type: ImageType
  zone_name: string | null
  deck_number: number | null
  tags: string[] | null
  ai_analysis: Record<string, unknown> | null
  ai_analysis_version: string | null
  uploaded_at: string
  metadata_extra: Record<string, unknown> | null
}

export interface ImageAnalysisResult {
  image_id: string
  scores: Record<string, number>
  findings: VisualFinding[]
  positive_aspects: string[]
  concerns: string[]
  cannot_assess: string[]
  recommendations: string[]
  confidence: VisualConfidence
  confidence_factors: string[]
  image_quality_sufficient: boolean
}

export interface FusedScore {
  fused_score: number | null
  confidence: string
  data_sources: string[]
  structured_score: number | null
  visual_score: number | null
  fusion_weights: { structured: number; visual: number }
  visual_confidence: VisualConfidence | null
  disagreement: { message: string; structured_score: number; visual_score: number } | null
}

export const BOAT_CLASS_LABELS: Record<BoatClass, string> = {
  small_sail: 'Kleine Segelyacht',
  cruising_sail: 'Fahrtensegler',
  racing_sail: 'Regattayacht',
  daysailer: 'Daysailer',
  motorsailer: 'Motorsailer',
  catamaran_sail: 'Segel-Katamaran',
  catamaran_motor: 'Motor-Katamaran',
  small_motor: 'Kleine Motoryacht',
  large_motor: 'Große Motoryacht',
  sport_cruiser: 'Sport Cruiser',
  trawler: 'Trawler',
  explorer: 'Explorer',
  superyacht: 'Superyacht',
}

export const STATUS_LABELS: Record<ProjectStatus, string> = {
  draft: 'Entwurf',
  active: 'Aktiv',
  review: 'Review',
  archived: 'Archiviert',
}

// --- Full Analysis (Orchestrator) ---
export interface FullAnalysisResult {
  modules: Record<string, AnalysisResult>
  skipped: Record<string, string>
  errors: Record<string, string | { error: string; type: string }>
  overall_score: number | null
  overall_confidence: string
  module_count: number
  skipped_count: number
  error_count: number
  executed_at: string
}

// --- Updated Confidence Levels ---
export type DetailedConfidence =
  | 'measured'
  | 'calculated'
  | 'visual_high'
  | 'visual_medium'
  | 'visual_low'
  | 'visual_insufficient'
  | 'estimated'
  | 'benchmark'
  | 'documented'
  | 'discrepant'
  | 'insufficient'

export const CONFIDENCE_LABELS: Record<DetailedConfidence, string> = {
  measured: 'Gemessen',
  calculated: 'Berechnet',
  visual_high: 'Visuell (hoch)',
  visual_medium: 'Visuell (mittel)',
  visual_low: 'Visuell (niedrig)',
  visual_insufficient: 'Nicht auswertbar',
  estimated: 'Geschätzt',
  benchmark: 'Benchmark',
  documented: 'Dokumentiert',
  discrepant: 'Abweichung',
  insufficient: 'Unzureichend',
}

export const CONFIDENCE_COLORS: Record<DetailedConfidence, string> = {
  measured: 'green',
  calculated: 'green',
  visual_high: 'blue',
  visual_medium: 'amber',
  visual_low: 'red',
  visual_insufficient: 'gray',
  estimated: 'gray',
  benchmark: 'gray',
  documented: 'blue',
  discrepant: 'orange',
  insufficient: 'gray',
}

// --- Zone-level fused score ---
export interface ZoneFusedScore {
  zone_name: string
  score: number | null
  confidence: string
  sources: string[]
  structured_component: number | null
  visual_component: number | null
  discrepancy_note: string | null
}

// --- Knowledge Base ---
export interface KnowledgeSubcategory {
  id: string
  name: string
  description: string | null
  icon?: string | null
}

export interface KnowledgeCategory {
  id: string
  name: string
  description: string
  icon?: string | null
  subcategory_count: number
  subcategories: KnowledgeSubcategory[]
  implementation_status: 'complete' | 'partial' | 'planned'
  documentation_ready: boolean
}

export interface MaterialProperty {
  name: string
  value: string | number
  unit?: string | null
  typical_range?: { min: number; max: number } | null
  notes?: string | null
}

export interface ManufacturerIssue {
  title: string
  description: string
  severity: 'info' | 'warning' | 'critical'
  affected_models: string[]
  resolution?: string | null
  workaround?: string | null
}

export interface ManufacturerKnowledge {
  id: string
  name: string
  specialty: string
  yacht_types: string[]
  known_strengths: string[]
  known_weaknesses: string[]
  common_issues: ManufacturerIssue[]
  notable_materials: string[]
  quality_certifications: string[]
  cost_positioning: 'budget' | 'mid-range' | 'premium' | 'ultra-premium'
}

export interface DegradationData {
  timepoint_years: number
  condition_percentage: number
  primary_failure_mode?: string | null
  secondary_failures?: string[] | null
  maintenance_required?: string | null
}

export interface DegradationTimeline {
  material: string
  environment: 'tropical' | 'temperate' | 'polar' | 'saltwater_exposed' | 'fresh_water'
  datapoints: DegradationData[]
  expected_lifespan_years: number
  mitigation_strategies: string[]
  maintenance_plan: string[]
  replacement_triggers: string[]
}

export interface KnowledgeDetail {
  id: string
  category_id: string
  category_name: string
  subcategory_id?: string | null
  subcategory_name?: string | null
  title: string
  description: string
  content_html?: string | null
  content_markdown?: string | null
  material_properties?: MaterialProperty[] | null
  related_issues?: ManufacturerIssue[] | null
  degradation_data?: DegradationTimeline | null
  implementation_notes?: string | null
  cost_impact?: { low: number; high: number } | null
  compliance_standards?: string[] | null
  created_at: string
  updated_at: string
}
