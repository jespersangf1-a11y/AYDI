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

async function request<T>(url: string, options?: RequestInit): Promise<T> {
  const res = await fetch(url, {
    headers: { 'Content-Type': 'application/json', ...options?.headers },
    ...options,
  })
  if (!res.ok) {
    const error = await res.json().catch(() => ({ detail: res.statusText }))
    throw new Error(error.detail || res.statusText)
  }
  if (res.status === 204) return undefined as T
  return res.json()
}

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
  const res = await fetch(`${BASE}/projects/${projectId}/layouts/import-dxf`, {
    method: 'POST',
    body: form,
  })
  if (!res.ok) {
    const error = await res.json().catch(() => ({ detail: res.statusText }))
    throw new Error(error.detail || res.statusText)
  }
  return res.json()
}

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

// Quick Analysis
export async function runQuickAnalysis(specs: PublicSpecs): Promise<QuickAnalysisResponse> {
  return request<QuickAnalysisResponse>(`${BASE}/quick-analysis`, {
    method: 'POST',
    body: JSON.stringify(specs),
  })
}

export async function getQuickAnalysis(id: string): Promise<QuickAnalysisResponse> {
  return request<QuickAnalysisResponse>(`${BASE}/quick-analysis/${id}`)
}

// Service Reports
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

// Materials
export async function getMaterials(filters?: { category?: string }): Promise<unknown[]> {
  const params = new URLSearchParams()
  if (filters?.category) params.set('category', filters.category)
  const query = params.toString() ? `?${params.toString()}` : ''
  return request<unknown[]>(`${BASE}/materials${query}`)
}

// Cost summary
export async function getCostSummary(projectId: string, layoutId: string): Promise<CostSummary> {
  return request<CostSummary>(`${BASE}/projects/${projectId}/layouts/${layoutId}/costs/summary`)
}

// Layout versions
export async function getLayoutVersions(
  projectId: string,
  layoutId: string
): Promise<LayoutVersion[]> {
  return request<LayoutVersion[]>(
    `${BASE}/projects/${projectId}/layouts/${layoutId}/versions`
  )
}

export async function getLayoutDiff(
  projectId: string,
  layoutId: string,
  versionA: string,
  versionB: string
): Promise<LayoutDiff> {
  return request<LayoutDiff>(
    `${BASE}/projects/${projectId}/layouts/${layoutId}/diff?version_a=${versionA}&version_b=${versionB}`
  )
}

// Benchmarks
export async function getClassBenchmarks(boatClass: string): Promise<unknown> {
  return request<unknown>(`${BASE}/benchmarks/${boatClass}`)
}

// Auth
export async function login(
  email: string,
  password: string
): Promise<{ access_token: string; refresh_token: string }> {
  return request<{ access_token: string; refresh_token: string }>(`${BASE}/auth/login`, {
    method: 'POST',
    body: JSON.stringify({ email, password }),
  })
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

// Image upload + analysis
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
  const res = await fetch(`${BASE}/images/analyze`, {
    method: 'POST',
    body: form,
  })
  if (!res.ok) {
    const error = await res.json().catch(() => ({ detail: res.statusText }))
    throw new Error(error.detail || res.statusText)
  }
  return res.json()
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
  const res = await fetch(`${BASE}/projects/${projectId}/images`, {
    method: 'POST',
    body: form,
  })
  if (!res.ok) {
    const error = await res.json().catch(() => ({ detail: res.statusText }))
    throw new Error(error.detail || res.statusText)
  }
  return res.json()
}

export async function getProjectImages(projectId: string): Promise<ImageUploadData[]> {
  return request<ImageUploadData[]>(`${BASE}/projects/${projectId}/images`)
}

// Full Analysis (Orchestrator)
export async function runFullAnalysis(
  projectId: string,
  layoutId: string,
  configOverrides?: Record<string, unknown>,
): Promise<FullAnalysisResult> {
  return request<FullAnalysisResult>(`${BASE}/projects/${projectId}/full-analysis`, {
    method: 'POST',
    body: JSON.stringify({ layout_id: layoutId, module: 'all', config_overrides: configOverrides }),
  })
}
