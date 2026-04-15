import type {
  AnalysisResult,
  CostSummary,
  DxfImportResponse,
  FullAnalysisResult,
  ImageAnalysisResult,
  ImageUploadData,
  Layout,
  LayoutCreate,
  LayoutDiff,
  LayoutVersion,
  Project,
  ProjectCreate,
  PublicSpecs,
  QuickAnalysisResponse,
  ServiceReport,
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
  // Merge caller headers (allows overriding Content-Type for FormData)
  if (options?.headers) {
    const callerHeaders = options.headers as Record<string, string>
    Object.assign(headers, callerHeaders)
  }

  const res = await fetch(url, {
    ...options,
    headers,
  })

  if (!res.ok) {
    const error = await res.json().catch(() => ({ detail: undefined }))
    const userMessage = error.detail || HTTP_ERROR_MESSAGES[res.status] || 'Ein Fehler ist aufgetreten'
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
  // Do NOT set Content-Type — browser sets it with boundary for FormData
  const res = await fetch(url, {
    method,
    headers,
    body: form,
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
export async function getMaterials(filters?: { category?: string }): Promise<Record<string, unknown>[]> {
  const params = new URLSearchParams()
  if (filters?.category) params.set('category', filters.category)
  const query = params.toString() ? `?${params.toString()}` : ''
  return request<Record<string, unknown>[]>(`${BASE}/materials${query}`)
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
