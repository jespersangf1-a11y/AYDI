import type {
  KnowledgeCategory,
  KnowledgeDetail,
  DegradationTimeline,
  ManufacturerKnowledge,
} from '../types'

const BASE = '/api/v1'

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
  const res = await fetch(`${BASE}/knowledge/categories`)
  if (!res.ok) throw new Error('Failed to fetch knowledge categories')
  return res.json()
}

/**
 * Get detailed knowledge for a specific category
 */
export async function getKnowledgeDetail(categoryId: string): Promise<KnowledgeDetail> {
  const res = await fetch(`${BASE}/knowledge/categories/${categoryId}`)
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
  const res = await fetch(`${BASE}/knowledge/materials${query}`)
  if (!res.ok) throw new Error('Failed to fetch material knowledge')
  return res.json()
}

/**
 * Get manufacturer-specific knowledge and known issues
 */
export async function getManufacturerKnowledge(name: string): Promise<ManufacturerKnowledge> {
  const res = await fetch(`${BASE}/knowledge/manufacturers/${encodeURIComponent(name)}`)
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
  const res = await fetch(`${BASE}/knowledge/degradation${query}`)
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

  const res = await fetch(`${BASE}/knowledge/search?${searchParams.toString()}`)
  if (!res.ok) throw new Error('Failed to search knowledge')
  return res.json()
}
