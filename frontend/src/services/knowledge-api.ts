import type {
  KnowledgeCategory,
  KnowledgeDocument,
  KnowledgeSearchResult,
  CorpusDocumentSummary,
} from '../types'

const BASE = '/api/v1'

interface CorpusCategoryDto {
  id: string
  name: string
  document_count: number
  documents: CorpusDocumentSummary[]
}

interface CorpusCategoriesResponseDto {
  total_categories: number
  total_documents: number
  categories: CorpusCategoryDto[]
}

interface SearchMatchDto {
  category: string
  database: string
  entry_name: string
  excerpt: string
  relevance_score: number
}

interface SearchResponseDto {
  query: string
  results_count: number
  matches: SearchMatchDto[]
}

/**
 * Get all corpus categories (01-31) with their documents,
 * mapped onto the category grid shape used by KnowledgePage.
 */
export async function getKnowledgeCategories(): Promise<KnowledgeCategory[]> {
  const res = await fetch(`${BASE}/knowledge/corpus/categories`)
  if (!res.ok) throw new Error('Wissensdatenbank konnte nicht geladen werden')
  const data: CorpusCategoriesResponseDto = await res.json()
  return data.categories.map((c) => ({
    id: c.id,
    name: c.name,
    description: `${c.document_count} ${c.document_count === 1 ? 'Fachartikel' : 'Fachartikel'} aus dem Recherche-Korpus`,
    subcategory_count: c.document_count,
    implementation_status: 'complete' as const,
    documentation_ready: true,
    subcategories: c.documents.map((d) => ({
      id: d.key,
      name: d.title,
      description: `${d.line_count.toLocaleString('de-DE')} Zeilen · ${d.table_count} Tabellen · ${d.fehlerbilder_count} Fehlerbilder · ${d.faq_count} FAQ`,
    })),
  }))
}

/**
 * Read one full research document (lexicon article view).
 */
export async function getKnowledgeDocument(key: string): Promise<KnowledgeDocument> {
  const res = await fetch(`${BASE}/knowledge/corpus/documents/${encodeURIComponent(key)}`)
  if (!res.ok) throw new Error(`Artikel konnte nicht geladen werden: ${key}`)
  return res.json()
}

/**
 * Search across the knowledge base. Results stemming from the corpus carry
 * a sourceKey that can be opened as a full article.
 */
export async function searchKnowledge(query: string): Promise<KnowledgeSearchResult[]> {
  const res = await fetch(`${BASE}/knowledge/search?q=${encodeURIComponent(query)}`)
  if (!res.ok) throw new Error('Suche fehlgeschlagen')
  const data: SearchResponseDto = await res.json()
  return (data.matches ?? []).map((m, idx) => ({
    id: `${m.database}-${idx}`,
    title: m.entry_name,
    excerpt: m.excerpt,
    database: m.database,
    // Markdown-based hits carry the source document key in `category`
    sourceKey: m.database.startsWith('markdown') && m.category ? m.category : null,
  }))
}
