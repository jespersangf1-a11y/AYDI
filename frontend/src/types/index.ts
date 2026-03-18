export type BoatClass = 'small_sail' | 'cruising_sail' | 'large_motor' | 'superyacht'
export type ProjectStatus = 'draft' | 'active' | 'review' | 'archived'

export interface ZoneData {
  name: string
  zone_type: string
  polygon: number[][]
  is_crew_area: boolean
  is_guest_area: boolean
  visibility_angle: number | null
}

export interface PassageData {
  from_zone: string
  to_zone: string
  width_mm: number
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
  severity: 'critical' | 'warning' | 'info'
  message: string
  suggestion: string
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

export const BOAT_CLASS_LABELS: Record<BoatClass, string> = {
  small_sail: 'Kleine Segelyacht',
  cruising_sail: 'Fahrtensegler',
  large_motor: 'Große Motoryacht',
  superyacht: 'Superyacht',
}

export const STATUS_LABELS: Record<ProjectStatus, string> = {
  draft: 'Entwurf',
  active: 'Aktiv',
  review: 'Review',
  archived: 'Archiviert',
}
