import { useState, useEffect, useRef } from 'react'
import { Search, ChevronDown, Package, AlertTriangle, Zap, BookOpen, TrendingUp, Droplets } from 'lucide-react'
import HeroSection from '../components/layout/HeroSection'
import KnowledgeArticle from '../components/knowledge/KnowledgeArticle'
import {
  getKnowledgeCategories,
  getKnowledgeDocument,
  searchKnowledge,
} from '../services/knowledge-api'
import type { KnowledgeCategory, KnowledgeDocument, KnowledgeSearchResult } from '../types'
import { MEDIA } from '../config/media'


export default function KnowledgePage() {
  const [categories, setCategories] = useState<KnowledgeCategory[]>([])
  const [expandedCategoryId, setExpandedCategoryId] = useState<string | null>(null)
  const [searchQuery, setSearchQuery] = useState('')
  const [searchResults, setSearchResults] = useState<KnowledgeSearchResult[]>([])
  const [isSearching, setIsSearching] = useState(false)
  const [selectedDocument, setSelectedDocument] = useState<KnowledgeDocument | null>(null)
  const [docLoadingKey, setDocLoadingKey] = useState<string | null>(null)
  const [docError, setDocError] = useState<string | null>(null)
  const [searchError, setSearchError] = useState<string | null>(null)
  const [loading, setLoading] = useState(true)
  const [error, setError] = useState<string | null>(null)
  const [showSearchResults, setShowSearchResults] = useState(false)

  // Load corpus categories
  useEffect(() => {
    getKnowledgeCategories()
      .then((data) => {
        setCategories(data)
        setError(null)
      })
      .catch((e) => {
        setError(
          e instanceof Error
            ? e.message
            : 'Wissensdatenbank konnte nicht geladen werden',
        )
        setCategories([])
      })
      .finally(() => setLoading(false))
  }, [])

  // Handle search with debounce. The sequence counter guards against BOTH
  // stale debounce timers (query shortened below 2 chars while a timer was
  // pending) and out-of-order fetch responses (older response arriving after
  // a newer one).
  const searchTimeoutRef = useRef<ReturnType<typeof setTimeout> | null>(null)
  const searchSeqRef = useRef(0)

  const handleSearch = (query: string) => {
    setSearchQuery(query)
    const seq = ++searchSeqRef.current

    if (searchTimeoutRef.current) {
      clearTimeout(searchTimeoutRef.current)
      searchTimeoutRef.current = null
    }

    if (query.trim().length < 2) {
      setShowSearchResults(false)
      setSearchResults([])
      setSearchError(null)
      setIsSearching(false)
      return
    }

    setIsSearching(true)
    searchTimeoutRef.current = setTimeout(async () => {
      try {
        const results = await searchKnowledge(query)
        if (seq !== searchSeqRef.current) return // stale response — discard
        setSearchResults(results)
        setSearchError(null)
        setShowSearchResults(true)
      } catch (e) {
        if (seq !== searchSeqRef.current) return
        console.error('Search error:', e)
        setSearchResults([])
        setSearchError('Suche fehlgeschlagen — bitte versuchen Sie es erneut.')
        setShowSearchResults(true)
      } finally {
        if (seq === searchSeqRef.current) setIsSearching(false)
      }
    }, 300)
  }

  const handleCategoryClick = (categoryId: string) => {
    setExpandedCategoryId(expandedCategoryId === categoryId ? null : categoryId)
  }

  const handleOpenDocument = async (key: string) => {
    setDocLoadingKey(key)
    setDocError(null)
    try {
      const doc = await getKnowledgeDocument(key)
      setSelectedDocument(doc)
    } catch (e) {
      console.error('Failed to fetch document:', e)
      setDocError('Artikel konnte nicht geladen werden — bitte versuchen Sie es erneut.')
    } finally {
      setDocLoadingKey(null)
    }
  }

  const getCategoryIcon = (categoryName: string) => {
    const name = categoryName.toLowerCase()
    if (name.includes('elektr')) return <Zap className="w-6 h-6" />
    if (name.includes('sicherheit')) return <AlertTriangle className="w-6 h-6" />
    if (name.includes('norm') || name.includes('standard') || name.includes('konstruktion'))
      return <BookOpen className="w-6 h-6" />
    if (name.includes('schl') || name.includes('wasser') || name.includes('sanit'))
      return <Droplets className="w-6 h-6" />
    if (name.includes('beschichtung') || name.includes('pflege') || name.includes('wartung'))
      return <TrendingUp className="w-6 h-6" />
    return <Package className="w-6 h-6" />
  }

  const getDatabaseLabel = (database: string) => {
    switch (database) {
      case 'markdown_document':
        return 'Fachartikel'
      case 'markdown_faq':
        return 'FAQ'
      case 'markdown_glossary':
        return 'Glossar'
      case 'markdown_fehlerbilder':
        return 'Fehlerbild'
      case 'markdown_erfahrungsberichte':
        return 'Erfahrungsbericht'
      default:
        return 'Wissensbasis'
    }
  }

  const displayedCategories = showSearchResults ? [] : categories

  return (
    <div>
      <HeroSection
        backgroundVideo={MEDIA.video.ocean_waves}
        backgroundImage={MEDIA.overview.blueprint}
        title="Wissensdatenbank"
        subtitle="Umfassendes Nachschlagewerk für Yachtdesign, Materialwissenschaft und maritime Standards – sorgfältig kuratiert wie ein klassisches Nachschlagewerk"
        label="Wissen"
      />

      <div className="space-y-8 px-4 sm:px-10 py-12">
        {/* Search Bar */}
        <div className="max-w-3xl mx-auto">
          <div className="relative group">
            <Search className="absolute left-4 top-1/2 transform -translate-y-1/2 w-5 h-5 text-navy-600 group-focus-within:text-ocean-600 transition-colors duration-200" />
            <input
              type="text"
              placeholder="Suchen Sie in der Wissensdatenbank..."
              value={searchQuery}
              onChange={(e) => handleSearch(e.target.value)}
              aria-label="Wissensdatenbank durchsuchen"
              className="w-full pl-12 pr-12 py-3 bg-white border border-sand-200 rounded-lg text-navy-900 placeholder-navy-500 focus:outline-none focus:border-ocean-500 focus:ring-2 focus:ring-ocean-500/20 transition-all duration-200"
            />
            {isSearching && (
              <div className="absolute right-4 top-1/2 transform -translate-y-1/2">
                <div className="animate-spin">
                  <div className="w-5 h-5 border-2 border-ocean-400/30 border-t-ocean-400 rounded-full" />
                </div>
              </div>
            )}
          </div>
          {showSearchResults && searchError && !isSearching && (
            <div className="mt-4 card-premium bg-amber-950/20 border-amber-700/20 p-4 text-amber-300 text-sm">
              {searchError}
            </div>
          )}
          {showSearchResults && !searchError && searchResults.length === 0 && !isSearching && searchQuery.length > 1 && (
            <div className="text-center mt-8 py-12 animate-fade-in-up">
              <BookOpen className="w-12 h-12 text-navy-600 mx-auto mb-4" />
              <p className="text-navy-700 text-sm">Keine Ergebnisse für "{searchQuery}"</p>
              <p className="text-navy-600 text-xs mt-2">Versuchen Sie andere Suchbegriffe</p>
            </div>
          )}
          {docError && (
            <div className="mt-4 card-premium bg-amber-950/20 border-amber-700/20 p-4 text-amber-300 text-sm">
              {docError}
            </div>
          )}
        </div>

        {loading && (
          <div className="text-center py-12 text-navy-700">
            <div className="animate-spin inline-block">
              <div className="w-8 h-8 border-2 border-ocean-400/30 border-t-ocean-400 rounded-full" />
            </div>
            <p className="mt-3">Wissensdatenbank wird geladen...</p>
          </div>
        )}

        {error && (
          <div className="card-premium bg-amber-950/20 border-amber-700/20 p-6 text-amber-300 text-sm max-w-3xl mx-auto">
            <p className="font-medium mb-1">Wissensdatenbank nicht erreichbar</p>
            <p>{error}</p>
            <p className="mt-2 text-xs">
              Bitte stellen Sie sicher, dass das Backend läuft, und laden Sie die Seite neu.
            </p>
          </div>
        )}

        {!loading && !error && !showSearchResults && displayedCategories.length === 0 && (
          <div className="card-premium px-10 py-12 text-center text-navy-700">
            Keine Kategorien verfügbar
          </div>
        )}

        {/* Search Results */}
        {showSearchResults && searchResults.length > 0 && (
          <div className="animate-fade-in-up">
            <p className="label-premium mb-6">
              SUCHERGEBNISSE ({searchResults.length})
            </p>
            <div className="grid grid-cols-1 md:grid-cols-2 gap-4">
              {searchResults.map((result, idx) => {
                const clickable = Boolean(result.sourceKey)
                const inner = (
                  <>
                    <div className="flex items-start gap-3 mb-3">
                      <span className="text-ocean-600 transition-all duration-200">
                        <BookOpen className="w-6 h-6" />
                      </span>
                      <div className="flex-1 min-w-0">
                        <p className="text-xs font-medium text-navy-700 uppercase tracking-wide">
                          {getDatabaseLabel(result.database)}
                        </p>
                        <h3 className="font-serif font-medium text-navy-900 mt-1">
                          {result.title}
                        </h3>
                      </div>
                    </div>
                    <p className="text-sm text-navy-700 line-clamp-3">{result.excerpt}</p>
                    {clickable && (
                      <p className="mt-3 text-xs text-ocean-600 font-medium">
                        {docLoadingKey === result.sourceKey
                          ? 'Artikel wird geladen...'
                          : 'Quellartikel öffnen →'}
                      </p>
                    )}
                  </>
                )
                return clickable ? (
                  <button
                    key={result.id}
                    onClick={() => handleOpenDocument(result.sourceKey as string)}
                    style={{ animationDelay: `${idx * 60}ms` }}
                    className="animate-fade-in-up card-premium p-6 text-left hover:bg-sand-50 hover:shadow-lg hover:shadow-ocean-500/10 transition-all duration-200"
                    aria-label={`${result.title} öffnen`}
                  >
                    {inner}
                  </button>
                ) : (
                  <div
                    key={result.id}
                    style={{ animationDelay: `${idx * 60}ms` }}
                    className="animate-fade-in-up card-premium p-6 text-left"
                  >
                    {inner}
                  </div>
                )
              })}
            </div>
          </div>
        )}

        {/* Categories Grid */}
        {!showSearchResults && (
          <div className="space-y-4">
            {displayedCategories.map((category, catIdx) => (
              <div key={category.id} className="space-y-2">
                {/* Category Card */}
                <button
                  onClick={() => handleCategoryClick(category.id)}
                  style={{ animationDelay: `${catIdx * 40}ms` }}
                  className="animate-fade-in-up w-full card-premium p-6 text-left hover:bg-sand-50 transition-all duration-200 group"
                  aria-expanded={expandedCategoryId === category.id}
                  aria-label={category.name}
                >
                  <div className="flex items-start justify-between">
                    <div className="flex items-start gap-4 flex-1">
                      <div className="flex-shrink-0 text-ocean-600 mt-1 group-hover:scale-110 group-hover:text-ocean-600 transition-all duration-200">
                        {getCategoryIcon(category.name)}
                      </div>
                      <div className="flex-1 min-w-0">
                        <div className="flex items-center gap-3 mb-2 flex-wrap">
                          <span className="font-mono text-xs text-navy-500">{category.id}</span>
                          <h3 className="font-serif text-subtitle font-medium text-navy-800 group-hover:text-ocean-600 transition-colors">
                            {category.name}
                          </h3>
                        </div>
                        <p className="text-sm text-navy-700 line-clamp-2 mb-3">{category.description}</p>
                        <div className="flex items-center gap-4 text-xs text-navy-600">
                          <span className="font-mono">
                            {category.subcategory_count} {category.subcategory_count === 1 ? 'Artikel' : 'Artikel'}
                          </span>
                        </div>
                      </div>
                    </div>
                    <ChevronDown
                      className={`w-5 h-5 text-navy-600 flex-shrink-0 group-hover:text-ocean-600 transition-all duration-300 ${
                        expandedCategoryId === category.id ? 'rotate-180' : ''
                      }`}
                    />
                  </div>
                </button>

                {/* Expanded document list */}
                {expandedCategoryId === category.id && (
                  <div className="pl-0 sm:pl-6 space-y-2 animate-slide-down">
                    {category.subcategories && category.subcategories.length > 0 ? (
                      category.subcategories.map((sub, subIdx) => (
                        <button
                          key={sub.id}
                          onClick={() => handleOpenDocument(sub.id)}
                          style={{ animationDelay: `${subIdx * 40}ms` }}
                          className="animate-fade-in-up w-full card-premium p-4 text-left hover:bg-sand-50 hover:translate-x-1 transition-all duration-200 border-l-2 border-ocean-500/40 hover:border-ocean-500 group"
                          aria-label={`Öffne ${sub.name}`}
                        >
                          <h4 className="font-medium text-navy-900 mb-1 group-hover:text-ocean-600 transition-colors">
                            {docLoadingKey === sub.id ? `${sub.name} — wird geladen...` : sub.name}
                          </h4>
                          {sub.description && (
                            <p className="text-sm text-navy-700 line-clamp-1">{sub.description}</p>
                          )}
                        </button>
                      ))
                    ) : (
                      <div className="card-premium p-4 text-navy-700 text-sm">
                        Keine Artikel verfügbar
                      </div>
                    )}
                  </div>
                )}
              </div>
            ))}
          </div>
        )}

        {/* Info Box */}
        {!loading && !error && !showSearchResults && categories.length > 0 && (
          <div className="mt-12 card-premium bg-ocean-50/40 border-ocean-200 p-6">
            <div className="flex gap-4">
              <BookOpen className="w-6 h-6 text-ocean-600 flex-shrink-0 mt-1" />
              <div>
                <h3 className="font-serif text-base font-medium text-navy-900 mb-2">Über diese Wissensdatenbank</h3>
                <p className="text-sm text-navy-700 leading-relaxed">
                  Diese Wissensdatenbank ist Ihr digitales Nachschlagewerk für alle Aspekte des Yachtdesigns —
                  {' '}{categories.reduce((sum, c) => sum + c.subcategory_count, 0)} Fachartikel in {categories.length} Kategorien:
                  Materialkunde, Dichtungen, Beschichtungen, Bordsysteme, Sicherheit, Konstruktion und mehr.
                  Jeder Artikel nennt seine Quellenlage; unsichere Angaben sind als solche gekennzeichnet.
                </p>
              </div>
            </div>
          </div>
        )}
      </div>

      {/* Article Modal */}
      {selectedDocument && (
        <KnowledgeArticle doc={selectedDocument} onClose={() => setSelectedDocument(null)} />
      )}
    </div>
  )
}
