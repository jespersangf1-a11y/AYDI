import { getAuthToken } from './api'
import type { CostItem, CostItemCreate } from '../types'

/**
 * Cost item CRUD against the real backend routes
 * (backend/app/api/routes/costs.py — router prefix "/projects/{project_id}"):
 *
 *   GET    /api/v1/projects/{p}/layouts/{l}/costs            → CostItemResponse[]
 *   POST   /api/v1/projects/{p}/layouts/{l}/costs            → 201 CostItemResponse
 *   PATCH  /api/v1/projects/{p}/layouts/{l}/costs/{id}       → CostItemResponse
 *   DELETE /api/v1/projects/{p}/layouts/{l}/costs/{id}       → 204
 *
 * The summary endpoint (.../costs/summary) already lives in `api.ts`
 * (`getCostSummary`) and is not duplicated here.
 *
 * Own module (pattern: knowledge-api.ts) because `api.ts` is owned elsewhere.
 * Auth/CSRF mirrors `api.ts`: bearer token from the shared token store plus
 * the non-httpOnly `aydi_csrf` cookie echoed on mutating requests.
 */

const BASE = '/api/v1'

const HTTP_ERROR_MESSAGES: Record<number, string> = {
  400: 'Ungültige Anfrage',
  401: 'Authentifizierung erforderlich',
  403: 'Zugriff verweigert',
  404: 'Ressource nicht gefunden',
  422: 'Ungültige Daten',
  429: 'Zu viele Anfragen. Bitte später versuchen.',
  500: 'Serverfehler',
  503: 'Service nicht verfügbar',
}

function readCsrfToken(): string | null {
  if (typeof document === 'undefined') return null
  const match = document.cookie.match(/(?:^|;\s*)aydi_csrf=([^;]+)/)
  return match ? decodeURIComponent(match[1]) : null
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
    const detail = (body as { detail?: unknown }).detail
    // Pydantic 422 delivers `detail` as an array of error objects.
    const detailText = Array.isArray(detail)
      ? detail
          .map((d: { msg?: string; loc?: unknown[] }) =>
            d?.msg
              ? `${Array.isArray(d.loc) ? d.loc.slice(1).join('.') + ': ' : ''}${d.msg}`
              : JSON.stringify(d),
          )
          .join(' · ')
      : typeof detail === 'string'
      ? detail
      : undefined
    const err = new Error(
      detailText || HTTP_ERROR_MESSAGES[res.status] || 'Ein Fehler ist aufgetreten',
    ) as Error & { status: number }
    err.status = res.status
    throw err
  }

  if (res.status === 204) return undefined as T
  return res.json() as Promise<T>
}

/** All cost items of a layout, optionally filtered by category. */
export async function listCostItems(
  projectId: string,
  layoutId: string,
  category?: string,
): Promise<CostItem[]> {
  const query = category ? `?category=${encodeURIComponent(category)}` : ''
  return request<CostItem[]>(
    `${BASE}/projects/${projectId}/layouts/${layoutId}/costs${query}`,
  )
}

/**
 * Create a cost item. Required by CostItemCreate: category, unit_cost_eur,
 * total_cost_eur (all `ge=0`); quantity defaults to 1, unit to "piece",
 * source to "estimate" server-side.
 */
export async function createCostItem(
  projectId: string,
  layoutId: string,
  data: CostItemCreate,
): Promise<CostItem> {
  return request<CostItem>(
    `${BASE}/projects/${projectId}/layouts/${layoutId}/costs`,
    { method: 'POST', body: JSON.stringify(data) },
  )
}

/** Partially update a cost item (CostItemUpdate — every field optional). */
export async function updateCostItem(
  projectId: string,
  layoutId: string,
  costItemId: string,
  data: Partial<CostItemCreate>,
): Promise<CostItem> {
  return request<CostItem>(
    `${BASE}/projects/${projectId}/layouts/${layoutId}/costs/${costItemId}`,
    { method: 'PATCH', body: JSON.stringify(data) },
  )
}

/** Delete a cost item (backend answers 204). */
export async function deleteCostItem(
  projectId: string,
  layoutId: string,
  costItemId: string,
): Promise<void> {
  await request<void>(
    `${BASE}/projects/${projectId}/layouts/${layoutId}/costs/${costItemId}`,
    { method: 'DELETE' },
  )
}
