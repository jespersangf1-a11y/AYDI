import type {
  AnalysisResult,
  DxfImportResponse,
  Layout,
  LayoutCreate,
  Project,
  ProjectCreate,
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
