/**
 * Service reports (Pipeline C) — standalone API module.
 *
 * `services/api.ts` is owned elsewhere; this module follows the same pattern as
 * `knowledge-api.ts` and only reuses the shared auth-token accessor so there is
 * a single source of truth for the bearer token.
 *
 * Backend: `app/api/routes/service_reports.py`
 *   GET    /api/v1/service-reports              (list, own reports only)
 *   POST   /api/v1/service-reports              (201)
 *   GET    /api/v1/service-reports/{id}
 *   PATCH  /api/v1/service-reports/{id}
 *   DELETE /api/v1/service-reports/{id}         (204)
 * Schema: `app/schemas/service.py::ServiceReportCreate / ServiceReportUpdate`
 */
import { getAuthToken } from './api'
import type { BoatClass, Severity } from '../types'

const BASE = '/api/v1'

// ─── DTOs (mirror app/schemas/service.py exactly) ───

/** Response shape of `ServiceReportResponse`. */
export interface ServiceReportDto {
  id: string
  report_type: string
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
  reported_by: string | null
  reported_at: string | null
  project_id: string | null
  boat_class: BoatClass | null
  model_name: string | null
  metadata_extra: Record<string, unknown> | null
  created_at: string
}

/** Request shape of `ServiceReportCreate`. Required: report_type, category, description. */
export interface ServiceReportCreatePayload {
  report_type: string
  category: string
  description: string
  severity?: string
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
}

/** Request shape of `ServiceReportUpdate` — every field optional (PATCH). */
export type ServiceReportUpdatePayload = Partial<ServiceReportCreatePayload>

// ─── HTTP plumbing ───

const HTTP_ERROR_MESSAGES: Record<number, string> = {
  400: 'Ungültige Anfrage',
  401: 'Anmeldung erforderlich',
  403: 'Zugriff verweigert',
  404: 'Servicebericht nicht gefunden',
  422: 'Ungültige Daten',
  429: 'Zu viele Anfragen. Bitte später versuchen.',
  500: 'Serverfehler',
  503: 'Service nicht verfügbar',
}

/** CSRF token cookie set by /auth/login (cookie-auth transport). */
function readCsrfToken(): string | null {
  if (typeof document === 'undefined') return null
  const match = document.cookie.match(/(?:^|;\s*)aydi_csrf=([^;]+)/)
  return match ? decodeURIComponent(match[1]) : null
}

interface ValidationDetail {
  msg?: string
  loc?: unknown[]
}

/** Pydantic 422 delivers `detail` as an array — render it readably, not "[object Object]". */
function formatDetail(detail: unknown): string | undefined {
  if (Array.isArray(detail)) {
    return detail
      .map((d: ValidationDetail) =>
        d?.msg
          ? `${Array.isArray(d.loc) ? d.loc.slice(1).join('.') + ': ' : ''}${d.msg}`
          : JSON.stringify(d)
      )
      .join(' · ')
  }
  if (typeof detail === 'string') return detail
  return undefined
}

async function request<T>(url: string, options?: RequestInit): Promise<T> {
  const headers: Record<string, string> = { 'Content-Type': 'application/json' }
  const token = getAuthToken()
  if (token) headers['Authorization'] = `Bearer ${token}`

  const method = (options?.method || 'GET').toUpperCase()
  if (!['GET', 'HEAD', 'OPTIONS'].includes(method)) {
    const csrf = readCsrfToken()
    if (csrf) headers['X-CSRF-Token'] = csrf
  }

  const res = await fetch(url, { ...options, headers, credentials: 'include' })

  if (!res.ok) {
    const body = await res.json().catch(() => ({ detail: undefined }))
    const message =
      formatDetail((body as { detail?: unknown }).detail) ||
      HTTP_ERROR_MESSAGES[res.status] ||
      'Ein Fehler ist aufgetreten'
    const err = new Error(message) as Error & { status: number }
    err.status = res.status
    throw err
  }

  if (res.status === 204) return undefined as T
  return res.json()
}

// ─── Endpoints ───

export async function listServiceReports(filters?: {
  category?: string
  severity?: string
  boat_class?: string
  report_type?: string
  limit?: number
  offset?: number
}): Promise<ServiceReportDto[]> {
  const params = new URLSearchParams()
  if (filters?.category) params.set('category', filters.category)
  if (filters?.severity) params.set('severity', filters.severity)
  if (filters?.boat_class) params.set('boat_class', filters.boat_class)
  if (filters?.report_type) params.set('report_type', filters.report_type)
  if (filters?.limit != null) params.set('limit', String(filters.limit))
  if (filters?.offset != null) params.set('offset', String(filters.offset))
  const query = params.toString() ? `?${params.toString()}` : ''
  return request<ServiceReportDto[]>(`${BASE}/service-reports${query}`)
}

export async function createServiceReport(
  payload: ServiceReportCreatePayload
): Promise<ServiceReportDto> {
  return request<ServiceReportDto>(`${BASE}/service-reports`, {
    method: 'POST',
    body: JSON.stringify(payload),
  })
}

export async function updateServiceReport(
  id: string,
  payload: ServiceReportUpdatePayload
): Promise<ServiceReportDto> {
  return request<ServiceReportDto>(`${BASE}/service-reports/${id}`, {
    method: 'PATCH',
    body: JSON.stringify(payload),
  })
}

export async function deleteServiceReport(id: string): Promise<void> {
  return request<void>(`${BASE}/service-reports/${id}`, { method: 'DELETE' })
}

// ─── Closed value sets — must match the backend exactly ───

/**
 * `_REPORT_TYPES` in app/schemas/service.py. Anything outside this set is
 * rejected with 422, so the UI offers a select, never free text.
 */
export const REPORT_TYPE_OPTIONS: { value: string; label: string }[] = [
  { value: 'repair', label: 'Reparatur' },
  { value: 'maintenance', label: 'Wartung' },
  { value: 'inspection', label: 'Inspektion' },
  { value: 'service', label: 'Service' },
  { value: 'warranty', label: 'Garantiefall' },
  { value: 'refit', label: 'Umbau / Refit' },
  { value: 'complaint', label: 'Reklamation' },
  { value: 'incident', label: 'Vorfall / Schaden' },
  { value: 'feedback', label: 'Rückmeldung' },
]

export const REPORT_TYPE_LABELS: Record<string, string> = Object.fromEntries(
  REPORT_TYPE_OPTIONS.map((o) => [o.value, o.label])
)

/**
 * The 10 Systemdomänen from app/core/domains.py (`AnalysisDomain`).
 * Labels taken from the DE column of app/core/i18n.py (`domain.*`).
 */
export const CATEGORY_OPTIONS: { value: string; label: string }[] = [
  { value: 'hull_structure', label: 'Rumpf & Struktur' },
  { value: 'rigging_sails', label: 'Rigg & Segel' },
  { value: 'propulsion_engine', label: 'Antrieb & Motor' },
  { value: 'electrical_electronics', label: 'Elektrik & Elektronik' },
  { value: 'sanitary_water', label: 'Sanitär & Wasser' },
  { value: 'deck_fittings', label: 'Deck & Beschläge' },
  { value: 'interior', label: 'Innenausbau' },
  { value: 'safety', label: 'Sicherheit' },
  { value: 'navigation', label: 'Navigation' },
  { value: 'maintenance_service', label: 'Wartung & Service' },
]

export const CATEGORY_LABELS: Record<string, string> = Object.fromEntries(
  CATEGORY_OPTIONS.map((o) => [o.value, o.label])
)

/**
 * `VALID_ZONE_TYPES` from app/core/validation.py, grouped as in the source.
 * The zone type is what `service_patterns` accumulates its weighted issue
 * score on — a report without zone_type never lands on a zone.
 */
export const ZONE_TYPE_GROUPS: { group: string; options: { value: string; label: string }[] }[] = [
  {
    group: 'Innenausbau',
    options: [
      { value: 'cabin', label: 'Kabine' },
      { value: 'saloon', label: 'Salon' },
      { value: 'pantry', label: 'Pantry / Kombüse' },
      { value: 'head', label: 'Nasszelle / WC' },
      { value: 'shower', label: 'Dusche' },
      { value: 'storage', label: 'Stauraum' },
      { value: 'forepeak', label: 'Vorschiff / Vorpiek' },
      { value: 'aft_cabin', label: 'Achterkabine' },
      { value: 'quarter_berth', label: 'Hundekoje' },
      { value: 'workshop', label: 'Werkstatt' },
    ],
  },
  {
    group: 'Deck & Cockpit',
    options: [
      { value: 'cockpit', label: 'Cockpit' },
      { value: 'foredeck', label: 'Vordeck' },
      { value: 'side_deck', label: 'Seitendeck' },
      { value: 'flybridge', label: 'Flybridge' },
      { value: 'swim_platform', label: 'Badeplattform' },
      { value: 'deck_hardware', label: 'Deckbeschläge' },
    ],
  },
  {
    group: 'Antrieb & Systeme',
    options: [
      { value: 'engine', label: 'Motor' },
      { value: 'engine_room', label: 'Maschinenraum' },
      { value: 'fuel_tank', label: 'Kraftstofftank' },
      { value: 'shaft_tunnel', label: 'Wellentunnel' },
      { value: 'water_tank', label: 'Wassertank' },
      { value: 'holding_tank', label: 'Fäkalientank' },
    ],
  },
  {
    group: 'Elektrik & Navigation',
    options: [
      { value: 'electrical_panel', label: 'Schalttafel' },
      { value: 'battery_compartment', label: 'Batteriefach' },
      { value: 'charger_area', label: 'Ladegerätebereich' },
      { value: 'nav_station', label: 'Kartentisch / Navigation' },
      { value: 'helm', label: 'Steuerstand' },
      { value: 'flybridge_helm', label: 'Flybridge-Steuerstand' },
    ],
  },
  {
    group: 'Struktur',
    options: [
      { value: 'hull', label: 'Rumpf' },
      { value: 'keel', label: 'Kiel' },
      { value: 'rudder', label: 'Ruder' },
      { value: 'bulkhead', label: 'Schott' },
      { value: 'frame', label: 'Spant' },
      { value: 'transom', label: 'Spiegel / Heck' },
      { value: 'void', label: 'Hohlraum' },
    ],
  },
  {
    group: 'Rigg & Segel',
    options: [
      { value: 'mast', label: 'Mast' },
      { value: 'rigging', label: 'Rigg / Stehendes Gut' },
      { value: 'sail_storage', label: 'Segelstau' },
    ],
  },
  {
    group: 'Sicherheit',
    options: [
      { value: 'safety_locker', label: 'Sicherheitsstau' },
      { value: 'liferaft_storage', label: 'Rettungsinselstau' },
      { value: 'fire_station', label: 'Feuerlöschstation' },
    ],
  },
  {
    group: 'Wartung & Sonstiges',
    options: [
      { value: 'service_area', label: 'Servicebereich' },
      { value: 'maintenance_hatch', label: 'Wartungsluke' },
      { value: 'boatyard', label: 'Werft / Winterlager' },
      { value: 'technical', label: 'Technikraum' },
      { value: 'crew_area', label: 'Crewbereich' },
      { value: 'guest_area', label: 'Gästebereich' },
    ],
  },
]

export const ZONE_TYPE_LABELS: Record<string, string> = Object.fromEntries(
  ZONE_TYPE_GROUPS.flatMap((g) => g.options.map((o) => [o.value, o.label]))
)

/**
 * Severity is not decorative: `_REPORT_SEVERITY_WEIGHT` in
 * app/services/analysis/service_patterns.py turns it into the weighted score
 * per Zonentyp (critical 4 · high 3 · medium 2 · low 1). Zones above the
 * threshold are reported as problematic. The form therefore explains each
 * level instead of offering four bare words.
 */
export const SEVERITY_OPTIONS: {
  value: Severity
  label: string
  weight: number
  hint: string
}[] = [
  {
    value: 'critical',
    label: 'Kritisch',
    weight: 4,
    hint: 'Seetüchtigkeit oder Sicherheit betroffen — Boot bis zur Behebung nicht einsatzfähig.',
  },
  {
    value: 'high',
    label: 'Hoch',
    weight: 3,
    hint: 'Erheblicher Mangel, Nutzung eingeschränkt oder Folgeschaden absehbar.',
  },
  {
    value: 'medium',
    label: 'Mittel',
    weight: 2,
    hint: 'Behebbarer Mangel ohne Sicherheitsrisiko — planbare Instandsetzung.',
  },
  {
    value: 'low',
    label: 'Niedrig',
    weight: 1,
    hint: 'Bagatelle, Verschleiß im Rahmen oder reine Routinearbeit.',
  },
]

export const SEVERITY_LABELS: Record<Severity, string> = {
  critical: 'Kritisch',
  high: 'Hoch',
  medium: 'Mittel',
  low: 'Niedrig',
}
