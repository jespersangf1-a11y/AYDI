import type {
  AnalysisResult,
  CostSummary,
  DxfImportResponse,
  FullAnalysisResult,
  ImageAnalysisResult,
  ImageUploadData,
  Invitation,
  Layout,
  LayoutCreate,
  LayoutDiff,
  LayoutVersion,
  Organization,
  OrgMemberEntry,
  OrgRole,
  PassageData,
  Project,
  ProjectMemberEntry,
  ProjectCreate,
  PublicSpecs,
  QuickAnalysisResponse,
  ServiceReport,
  StructuralItemCreatePayload,
  StructuralItemData,
  ZoneData,
  ZoneMaterialAssignment,
  ZoneMaterialCreatePayload,
} from '../types'

const BASE = '/api/v1'

// ─── Auth Token Management ───
let _authToken: string | null = null

export function setAuthToken(token: string | null) {
  _authToken = token
  if (token) {
    try { localStorage.setItem('aydi_token', token) } catch { /* SSR/incognito */ }
  } else {
    try { localStorage.removeItem('aydi_token') } catch { /* SSR/incognito */ }
  }
}

export function getAuthToken(): string | null {
  if (_authToken) return _authToken
  try {
    const stored = localStorage.getItem('aydi_token')
    if (stored) _authToken = stored
    return stored
  } catch {
    return null
  }
}

export function clearAuthToken() {
  _authToken = null
  try { localStorage.removeItem('aydi_token') } catch { /* SSR/incognito */ }
}

// ─── CSRF token helper ───
// Set as a non-httpOnly cookie by /auth/login. We read it from
// document.cookie and echo it as X-CSRF-Token on mutating requests.
function readCsrfToken(): string | null {
  if (typeof document === 'undefined') return null
  const match = document.cookie.match(/(?:^|;\s*)aydi_csrf=([^;]+)/)
  return match ? decodeURIComponent(match[1]) : null
}

// ─── HTTP Error Messages (German) ───
const HTTP_ERROR_MESSAGES: Record<number, string> = {
  400: 'Ungültige Anfrage',
  401: 'Authentifizierung erforderlich',
  403: 'Zugriff verweigert',
  404: 'Ressource nicht gefunden',
  409: 'Konflikt mit existierenden Daten',
  413: 'Datei zu groß',
  422: 'Ungültige Daten',
  429: 'Zu viele Anfragen. Bitte später versuchen.',
  500: 'Serverfehler',
  502: 'Schlechtes Gateway',
  503: 'Service nicht verfügbar',
  504: 'Gateway-Timeout',
}

// ─── Core Request Function ───
async function request<T>(url: string, options?: RequestInit): Promise<T> {
  const token = getAuthToken()
  const headers: Record<string, string> = {
    'Content-Type': 'application/json',
  }
  if (token) {
    headers['Authorization'] = `Bearer ${token}`
  }
  // Add CSRF token for mutating requests (cookie-auth path)
  const method = (options?.method || 'GET').toUpperCase()
  if (!['GET', 'HEAD', 'OPTIONS'].includes(method)) {
    const csrf = readCsrfToken()
    if (csrf) headers['X-CSRF-Token'] = csrf
  }
  // Merge caller headers (allows overriding Content-Type for FormData)
  if (options?.headers) {
    const callerHeaders = options.headers as Record<string, string>
    Object.assign(headers, callerHeaders)
  }

  const res = await fetch(url, {
    ...options,
    headers,
    credentials: 'include',  // send cookies for cross-origin requests
  })

  if (!res.ok) {
    const error = await res.json().catch(() => ({ detail: undefined }))
    // Pydantic 422s deliver detail as an ARRAY of error objects — stringifying
    // that produced "[object Object]" banners instead of readable messages.
    const detail = error.detail
    const detailText = Array.isArray(detail)
      ? detail
          .map((d: { msg?: string; loc?: unknown[] }) =>
            d?.msg
              ? `${Array.isArray(d.loc) ? d.loc.slice(1).join('.') + ': ' : ''}${d.msg}`
              : JSON.stringify(d)
          )
          .join(' · ')
      : typeof detail === 'string'
      ? detail
      : undefined
    const userMessage = detailText || HTTP_ERROR_MESSAGES[res.status] || 'Ein Fehler ist aufgetreten'
    const err = new Error(userMessage) as Error & { status: number }
    err.status = res.status
    throw err
  }

  if (res.status === 204) return undefined as T
  return res.json()
}

// Helper for FormData requests that need auth but NOT Content-Type header
async function requestFormData<T>(url: string, form: FormData, method = 'POST'): Promise<T> {
  const token = getAuthToken()
  const headers: Record<string, string> = {}
  if (token) {
    headers['Authorization'] = `Bearer ${token}`
  }
  if (!['GET', 'HEAD', 'OPTIONS'].includes(method.toUpperCase())) {
    const csrf = readCsrfToken()
    if (csrf) headers['X-CSRF-Token'] = csrf
  }
  // Do NOT set Content-Type — browser sets it with boundary for FormData
  const res = await fetch(url, {
    method,
    headers,
    body: form,
    credentials: 'include',
  })
  if (!res.ok) {
    const error = await res.json().catch(() => ({ detail: res.statusText }))
    const userMessage = error.detail || HTTP_ERROR_MESSAGES[res.status] || res.statusText
    const err = new Error(userMessage) as Error & { status: number }
    err.status = res.status
    throw err
  }
  return res.json()
}

// ─── Projects ───
export async function listProjects(status?: string): Promise<Project[]> {
  const params = status ? `?status=${status}` : ''
  return request<Project[]>(`${BASE}/projects${params}`)
}

export async function getProject(id: string): Promise<Project> {
  return request<Project>(`${BASE}/projects/${id}`)
}

export async function createProject(data: ProjectCreate): Promise<Project> {
  return request<Project>(`${BASE}/projects/`, {
    method: 'POST',
    body: JSON.stringify(data),
  })
}

export async function updateProject(id: string, data: Partial<ProjectCreate>): Promise<Project> {
  return request<Project>(`${BASE}/projects/${id}`, {
    method: 'PATCH',
    body: JSON.stringify(data),
  })
}

export async function deleteProject(id: string): Promise<void> {
  return request<void>(`${BASE}/projects/${id}`, { method: 'DELETE' })
}

// ─── Layouts ───
export async function listLayouts(projectId: string): Promise<Layout[]> {
  return request<Layout[]>(`${BASE}/projects/${projectId}/layouts`)
}

export async function getLayout(projectId: string, layoutId: string): Promise<Layout> {
  return request<Layout>(`${BASE}/projects/${projectId}/layouts/${layoutId}`)
}

export async function createLayout(projectId: string, data: LayoutCreate): Promise<Layout> {
  return request<Layout>(`${BASE}/projects/${projectId}/layouts`, {
    method: 'POST',
    body: JSON.stringify(data),
  })
}

export async function importDxf(
  projectId: string,
  file: File,
  name: string,
  version: string = 'v1.0'
): Promise<DxfImportResponse> {
  const form = new FormData()
  form.append('file', file)
  form.append('name', name)
  form.append('version', version)
  return requestFormData<DxfImportResponse>(
    `${BASE}/projects/${projectId}/layouts/import-dxf`,
    form
  )
}

// ─── Analysis ───
export async function runAnalysis(
  projectId: string,
  layoutId: string,
  module: string
): Promise<AnalysisResult> {
  return request<AnalysisResult>(`${BASE}/projects/${projectId}/analyze`, {
    method: 'POST',
    body: JSON.stringify({ layout_id: layoutId, module }),
  })
}

export async function listAnalyses(projectId: string, module?: string): Promise<AnalysisResult[]> {
  const params = module ? `?module=${module}` : ''
  return request<AnalysisResult[]>(`${BASE}/projects/${projectId}/analyses${params}`)
}

// ─── Quick Analysis (Level 1 — no auth required) ───
export async function runQuickAnalysis(specs: PublicSpecs): Promise<QuickAnalysisResponse> {
  return request<QuickAnalysisResponse>(`${BASE}/quick-analysis`, {
    method: 'POST',
    body: JSON.stringify(specs),
  })
}

export async function getQuickAnalysis(id: string): Promise<QuickAnalysisResponse> {
  return request<QuickAnalysisResponse>(`${BASE}/quick-analysis/${id}`)
}

// ─── Service Reports ───
export async function getServiceReports(filters?: {
  category?: string
  severity?: string
}): Promise<ServiceReport[]> {
  const params = new URLSearchParams()
  if (filters?.category) params.set('category', filters.category)
  if (filters?.severity) params.set('severity', filters.severity)
  const query = params.toString() ? `?${params.toString()}` : ''
  return request<ServiceReport[]>(`${BASE}/service-reports${query}`)
}

// ─── Materials ───
export async function getMaterials(filters?: {
  category?: string
  limit?: number
}): Promise<Record<string, unknown>[]> {
  const params = new URLSearchParams()
  if (filters?.category) params.set('category', filters.category)
  // Backend default is 100 — a grown catalog would silently truncate and
  // existing assignments would render as "Unbekanntes Material".
  params.set('limit', String(filters?.limit ?? 500))
  return request<Record<string, unknown>[]>(`${BASE}/materials?${params.toString()}`)
}

// ─── Project sharing (pillar 4, stage 1) ───
export async function getProjectMembers(projectId: string): Promise<ProjectMemberEntry[]> {
  return request<ProjectMemberEntry[]>(`${BASE}/projects/${projectId}/members`)
}

export async function addProjectMember(
  projectId: string,
  email: string,
  role: 'viewer' | 'editor'
): Promise<ProjectMemberEntry> {
  return request<ProjectMemberEntry>(`${BASE}/projects/${projectId}/members`, {
    method: 'POST',
    body: JSON.stringify({ email, role }),
  })
}

export async function updateProjectMemberRole(
  projectId: string,
  userId: string,
  role: 'viewer' | 'editor'
): Promise<ProjectMemberEntry> {
  return request<ProjectMemberEntry>(`${BASE}/projects/${projectId}/members/${userId}`, {
    method: 'PATCH',
    body: JSON.stringify({ role }),
  })
}

export async function removeProjectMember(
  projectId: string,
  userId: string
): Promise<void> {
  await request<void>(`${BASE}/projects/${projectId}/members/${userId}`, {
    method: 'DELETE',
  })
}

// ─── Invitations (pillar 4, stage 2) ───
export async function getProjectInvitations(projectId: string): Promise<Invitation[]> {
  return request<Invitation[]>(`${BASE}/projects/${projectId}/invitations`)
}

export async function createProjectInvitation(
  projectId: string,
  email: string,
  role: 'viewer' | 'editor'
): Promise<Invitation> {
  return request<Invitation>(`${BASE}/projects/${projectId}/invitations`, {
    method: 'POST',
    body: JSON.stringify({ email, role }),
  })
}

export async function revokeProjectInvitation(
  projectId: string,
  invitationId: string
): Promise<void> {
  await request<void>(`${BASE}/projects/${projectId}/invitations/${invitationId}`, {
    method: 'DELETE',
  })
}

export async function getMyInvitations(): Promise<Invitation[]> {
  return request<Invitation[]>(`${BASE}/invitations/mine`)
}

export async function acceptInvitation(invitationId: string): Promise<Invitation> {
  return request<Invitation>(`${BASE}/invitations/${invitationId}/accept`, { method: 'POST' })
}

export async function declineInvitation(invitationId: string): Promise<void> {
  await request<void>(`${BASE}/invitations/${invitationId}/decline`, { method: 'POST' })
}

export async function setProjectOrg(
  projectId: string,
  orgId: string | null
): Promise<Project> {
  return request<Project>(`${BASE}/projects/${projectId}/org`, {
    method: 'PATCH',
    body: JSON.stringify({ org_id: orgId }),
  })
}

// ─── Organizations (pillar 4, stage 2) ───
export async function getMyOrganizations(): Promise<Organization[]> {
  return request<Organization[]>(`${BASE}/orgs`)
}

export async function createOrganization(name: string): Promise<Organization> {
  return request<Organization>(`${BASE}/orgs`, {
    method: 'POST',
    body: JSON.stringify({ name }),
  })
}

export async function getOrganization(orgId: string): Promise<Organization> {
  return request<Organization>(`${BASE}/orgs/${orgId}`)
}

export async function updateOrganization(orgId: string, name: string): Promise<Organization> {
  return request<Organization>(`${BASE}/orgs/${orgId}`, {
    method: 'PATCH',
    body: JSON.stringify({ name }),
  })
}

export async function deleteOrganization(orgId: string): Promise<void> {
  await request<void>(`${BASE}/orgs/${orgId}`, { method: 'DELETE' })
}

export async function getOrgMembers(orgId: string): Promise<OrgMemberEntry[]> {
  return request<OrgMemberEntry[]>(`${BASE}/orgs/${orgId}/members`)
}

export async function updateOrgMemberRole(
  orgId: string,
  userId: string,
  orgRole: OrgRole
): Promise<OrgMemberEntry> {
  return request<OrgMemberEntry>(`${BASE}/orgs/${orgId}/members/${userId}`, {
    method: 'PATCH',
    body: JSON.stringify({ org_role: orgRole }),
  })
}

export async function removeOrgMember(orgId: string, userId: string): Promise<void> {
  await request<void>(`${BASE}/orgs/${orgId}/members/${userId}`, { method: 'DELETE' })
}

export async function getOrgProjects(orgId: string): Promise<Project[]> {
  return request<Project[]>(`${BASE}/orgs/${orgId}/projects`)
}

export async function getOrgInvitations(orgId: string): Promise<Invitation[]> {
  return request<Invitation[]>(`${BASE}/orgs/${orgId}/invitations`)
}

export async function createOrgInvitation(
  orgId: string,
  email: string,
  role: 'member' | 'admin'
): Promise<Invitation> {
  return request<Invitation>(`${BASE}/orgs/${orgId}/invitations`, {
    method: 'POST',
    body: JSON.stringify({ email, role }),
  })
}

export async function revokeOrgInvitation(orgId: string, invitationId: string): Promise<void> {
  await request<void>(`${BASE}/orgs/${orgId}/invitations/${invitationId}`, { method: 'DELETE' })
}

// ─── Structural items (measured weights/positions → trim/CG analysis) ───
export async function getStructuralItems(
  projectId: string,
  layoutId: string
): Promise<StructuralItemData[]> {
  return request<StructuralItemData[]>(
    `${BASE}/projects/${projectId}/layouts/${layoutId}/structural`
  )
}

export async function createStructuralItem(
  projectId: string,
  layoutId: string,
  payload: StructuralItemCreatePayload
): Promise<StructuralItemData> {
  return request<StructuralItemData>(
    `${BASE}/projects/${projectId}/layouts/${layoutId}/structural`,
    { method: 'POST', body: JSON.stringify(payload) }
  )
}

export async function updateStructuralItem(
  projectId: string,
  layoutId: string,
  itemId: string,
  payload: Partial<StructuralItemCreatePayload>
): Promise<StructuralItemData> {
  return request<StructuralItemData>(
    `${BASE}/projects/${projectId}/layouts/${layoutId}/structural/${itemId}`,
    { method: 'PATCH', body: JSON.stringify(payload) }
  )
}

export async function deleteStructuralItem(
  projectId: string,
  layoutId: string,
  itemId: string
): Promise<void> {
  await request<void>(
    `${BASE}/projects/${projectId}/layouts/${layoutId}/structural/${itemId}`,
    { method: 'DELETE' }
  )
}

// ─── Zone material assignments (refit: swap materials per zone) ───
export async function getZoneMaterials(
  projectId: string,
  layoutId: string
): Promise<ZoneMaterialAssignment[]> {
  return request<ZoneMaterialAssignment[]>(
    `${BASE}/projects/${projectId}/layouts/${layoutId}/materials`
  )
}

export async function assignZoneMaterial(
  projectId: string,
  layoutId: string,
  payload: ZoneMaterialCreatePayload
): Promise<ZoneMaterialAssignment> {
  return request<ZoneMaterialAssignment>(
    `${BASE}/projects/${projectId}/layouts/${layoutId}/materials`,
    { method: 'POST', body: JSON.stringify(payload) }
  )
}

export async function deleteZoneMaterial(
  projectId: string,
  layoutId: string,
  zoneMaterialId: string
): Promise<void> {
  await request<void>(
    `${BASE}/projects/${projectId}/layouts/${layoutId}/materials/${zoneMaterialId}`,
    { method: 'DELETE' }
  )
}

// ─── Cost Summary ───
export async function getCostSummary(projectId: string, layoutId: string): Promise<CostSummary> {
  return request<CostSummary>(`${BASE}/projects/${projectId}/layouts/${layoutId}/costs/summary`)
}

// ─── Layout Versions ───
export async function getLayoutVersions(
  projectId: string,
  layoutId: string
): Promise<LayoutVersion[]> {
  return request<LayoutVersion[]>(
    `${BASE}/projects/${projectId}/layouts/${layoutId}/versions`
  )
}

// FIX: Backend expects query params named `a` and `b`, not `version_a`/`version_b`
export async function getLayoutDiff(
  projectId: string,
  layoutId: string,
  versionA: string,
  versionB: string
): Promise<LayoutDiff> {
  return request<LayoutDiff>(
    `${BASE}/projects/${projectId}/layouts/${layoutId}/diff?a=${versionA}&b=${versionB}`
  )
}

/** Save the current layout state as a named version (refit loop). */
export async function createLayoutVersion(
  projectId: string,
  layoutId: string,
  payload: {
    zones_snapshot: ZoneData[]
    passages_snapshot: PassageData[]
    change_summary?: string | null
  }
): Promise<LayoutVersion> {
  return request<LayoutVersion>(
    `${BASE}/projects/${projectId}/layouts/${layoutId}/versions`,
    { method: 'POST', body: JSON.stringify(payload) }
  )
}

/**
 * Partially update a layout. The backend auto-snapshots the previous state
 * as a version before applying — edits are never destructive.
 */
export async function updateLayout(
  projectId: string,
  layoutId: string,
  payload: {
    name?: string
    version?: string
    zones?: ZoneData[]
    passages?: PassageData[]
    deck_height_mm?: number
    change_summary?: string
    /** {oldName: newName} — server cascades to material/structural/cost refs */
    zone_renames?: Record<string, string>
  }
): Promise<Layout> {
  return request<Layout>(`${BASE}/projects/${projectId}/layouts/${layoutId}`, {
    method: 'PATCH',
    body: JSON.stringify(payload),
  })
}

// ─── Benchmarks ───
export async function getClassBenchmarks(boatClass: string): Promise<unknown> {
  return request<unknown>(`${BASE}/benchmarks/${boatClass}`)
}

// ─── Auth ───
export async function login(
  email: string,
  password: string
): Promise<{ access_token: string; refresh_token: string }> {
  const result = await request<{ access_token: string; refresh_token: string }>(`${BASE}/auth/login`, {
    method: 'POST',
    body: JSON.stringify({ email, password }),
  })
  // Auto-store token on successful login
  setAuthToken(result.access_token)
  return result
}

export async function register(
  email: string,
  password: string,
  fullName: string
): Promise<unknown> {
  return request<unknown>(`${BASE}/auth/register`, {
    method: 'POST',
    body: JSON.stringify({ email, password, full_name: fullName }),
  })
}

export async function logout(): Promise<void> {
  try {
    await request<void>(`${BASE}/auth/logout`, { method: 'POST' })
  } finally {
    clearAuthToken()
  }
}

// ─── Image Upload + Analysis ───
export async function uploadAndAnalyzeImage(
  file: File,
  imageType: string,
  boatClass: string,
  zoneType?: string,
): Promise<ImageAnalysisResult> {
  const form = new FormData()
  form.append('file', file)
  form.append('image_type', imageType)
  form.append('boat_class', boatClass)
  if (zoneType) form.append('zone_type', zoneType)
  return requestFormData<ImageAnalysisResult>(`${BASE}/images/analyze`, form)
}

export async function uploadProjectImage(
  projectId: string,
  file: File,
  imageType: string,
  zoneName?: string,
): Promise<ImageUploadData> {
  const form = new FormData()
  form.append('file', file)
  form.append('image_type', imageType)
  if (zoneName) form.append('zone_name', zoneName)
  return requestFormData<ImageUploadData>(`${BASE}/projects/${projectId}/images`, form)
}

export async function getProjectImages(projectId: string): Promise<ImageUploadData[]> {
  return request<ImageUploadData[]>(`${BASE}/projects/${projectId}/images`)
}

// ─── Full Analysis (Orchestrator) ───
// FIX: Backend FullAnalysisRequest schema does NOT include `module` field
export async function runFullAnalysis(
  projectId: string,
  layoutId: string,
  configOverrides?: Record<string, unknown>,
): Promise<FullAnalysisResult> {
  return request<FullAnalysisResult>(`${BASE}/projects/${projectId}/full-analysis`, {
    method: 'POST',
    body: JSON.stringify({ layout_id: layoutId, config_overrides: configOverrides }),
  })
}
