import type {
  KnowledgeCategory,
  KnowledgeDetail,
  DegradationTimeline,
  ManufacturerKnowledge,
} from '../types'

const BASE = '/api/v1'

import { getAuthToken } from './api'

/** fetch() wrapper that attaches the auth token — knowledge endpoints require login. */
function authFetch(url: string): Promise<Response> {
  const token = getAuthToken()
  const headers: Record<string, string> = {}
  if (token) headers['Authorization'] = `Bearer ${token}`
  return fetch(url, { headers })
}

interface MaterialKnowledgeParams {
  category?: string
  material?: string
  use_case?: string
}

interface DegradationKnowledgeParams {
  material?: string
  environment?: string
  timeframe?: string
}

interface SearchParams {
  query: string
  limit?: number
  offset?: number
}

/**
 * Get all knowledge categories
 */
export async function getKnowledgeCategories(): Promise<KnowledgeCategory[]> {
  const res = await authFetch(`${BASE}/knowledge/categories`)
  if (!res.ok) throw new Error('Failed to fetch knowledge categories')
  const data = await res.json()
  // Backend liefert {total_categories, categories: [{category_id, title, status, ...}]}
  // — auf das Frontend-Schema (KnowledgeCategory) abbilden.
  const raw = Array.isArray(data) ? data : (data.categories ?? [])
  return raw.map((c: any): KnowledgeCategory => ({
    id: c.id ?? c.category_id,
    name: c.name ?? c.title,
    description: c.description ?? '',
    icon: c.icon ?? null,
    subcategory_count: c.subcategory_count ?? c.entry_count ?? 0,
    subcategories: c.subcategories ?? [],
    implementation_status:
      c.implementation_status ?? (c.status === 'implemented' ? 'complete' : 'planned'),
    documentation_ready: c.documentation_ready ?? c.status === 'implemented',
  }))
}

/**
 * Get detailed knowledge for a specific category
 */
export async function getKnowledgeDetail(categoryId: string): Promise<KnowledgeDetail> {
  const res = await authFetch(`${BASE}/knowledge/categories/${categoryId}`)
  if (!res.ok) throw new Error(`Failed to fetch knowledge for category: ${categoryId}`)
  return res.json()
}

/**
 * Get material-specific knowledge
 */
export async function getMaterialKnowledge(
  params: MaterialKnowledgeParams,
): Promise<KnowledgeDetail[]> {
  const searchParams = new URLSearchParams()
  if (params.category) searchParams.set('category', params.category)
  if (params.material) searchParams.set('material', params.material)
  if (params.use_case) searchParams.set('use_case', params.use_case)

  const query = searchParams.toString() ? `?${searchParams.toString()}` : ''
  const res = await authFetch(`${BASE}/knowledge/materials${query}`)
  if (!res.ok) throw new Error('Failed to fetch material knowledge')
  return res.json()
}

/**
 * Get manufacturer-specific knowledge and known issues
 */
export async function getManufacturerKnowledge(name: string): Promise<ManufacturerKnowledge> {
  const res = await authFetch(`${BASE}/knowledge/manufacturers/${encodeURIComponent(name)}`)
  if (!res.ok) throw new Error(`Failed to fetch manufacturer knowledge: ${name}`)
  return res.json()
}

/**
 * Get degradation timelines and environmental impact
 */
export async function getDegradationKnowledge(
  params: DegradationKnowledgeParams,
): Promise<DegradationTimeline[]> {
  const searchParams = new URLSearchParams()
  if (params.material) searchParams.set('material', params.material)
  if (params.environment) searchParams.set('environment', params.environment)
  if (params.timeframe) searchParams.set('timeframe', params.timeframe)

  const query = searchParams.toString() ? `?${searchParams.toString()}` : ''
  const res = await authFetch(`${BASE}/knowledge/degradation${query}`)
  if (!res.ok) throw new Error('Failed to fetch degradation knowledge')
  return res.json()
}

/**
 * Search across all knowledge base
 */
export async function searchKnowledge(params: SearchParams): Promise<KnowledgeDetail[]> {
  const searchParams = new URLSearchParams()
  searchParams.set('q', params.query)
  if (params.limit) searchParams.set('limit', params.limit.toString())
  if (params.offset) searchParams.set('offset', params.offset.toString())

  const res = await authFetch(`${BASE}/knowledge/search?${searchParams.toString()}`)
  if (!res.ok) throw new Error('Failed to search knowledge')
  return res.json()
}
