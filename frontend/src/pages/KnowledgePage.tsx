import { useState, useEffect, useRef } from 'react'
import { Search, ChevronDown, Package, AlertTriangle, Zap, BookOpen, TrendingUp, Eye } from 'lucide-react'
import HeroSection from '../components/layout/HeroSection'
import KnowledgeDetailPanel from '../components/knowledge/KnowledgeDetail'
import {
  getKnowledgeCategories,
  getKnowledgeDetail,
  searchKnowledge,
} from '../services/knowledge-api'
import type { KnowledgeCategory, KnowledgeDetail } from '../types'
import { MEDIA } from '../config/media'


export default function KnowledgePage() {
  const [categories, setCategories] = useState<KnowledgeCategory[]>([])
  const [expandedCategoryId, setExpandedCategoryId] = useState<string | null>(null)
  const [searchQuery, setSearchQuery] = useState('')
  const [searchResults, setSearchResults] = useState<KnowledgeDetail[]>([])
  const [isSearching, setIsSearching] = useState(false)
  const [selectedDetail, setSelectedDetail] = useState<KnowledgeDetail | null>(null)
  const [loading, setLoading] = useState(true)
  const [error, setError] = useState<string | null>(null)
  const [showSearchResults, setShowSearchResults] = useState(false)

  // Load categories
  useEffect(() => {
    getKnowledgeCategories()
      .then((data) => {
        setCategories(data)
        setError(null)
      })
      .catch((e) => {
        setError(e.message)
        // Mock data for demo
        setCategories(getMockCategories())
      })
      .finally(() => setLoading(false))
  }, [])

  // Handle search with debounce
  const searchTimeoutRef = useRef<ReturnType<typeof setTimeout> | null>(null)

  const handleSearch = async (query: string) => {
    setSearchQuery(query)
    if (query.trim().length < 2) {
      setShowSearchResults(false)
      setSearchResults([])
      return
    }

    if (searchTimeoutRef.current) {
      clearTimeout(searchTimeoutRef.current)
    }

    setIsSearching(true)
    searchTimeoutRef.current = setTimeout(async () => {
      try {
        const results = await searchKnowledge({ query, limit: 20 })
        setSearchResults(results)
        setShowSearchResults(true)
      } catch (e) {
        console.error('Search error:', e)
        setShowSearchResults(false)
      } finally {
        setIsSearching(false)
      }
    }, 300)
  }

  const handleCategoryClick = async (categoryId: string) => {
    if (expandedCategoryId === categoryId) {
      setExpandedCategoryId(null)
    } else {
      setExpandedCategoryId(categoryId)
    }
  }

  const handleViewDetail = async (categoryId: string) => {
    try {
      const detail = await getKnowledgeDetail(categoryId)
      setSelectedDetail(detail)
    } catch (e) {
      console.error('Failed to fetch detail:', e)
    }
  }

  const getCategoryIcon = (categoryName: string) => {
    const name = categoryName.toLowerCase()
    if (name.includes('material')) return <Package className="w-6 h-6" />
    if (name.includes('degradation')) return <TrendingUp className="w-6 h-6" />
    if (name.includes('issue') || name.includes('problem'))
      return <AlertTriangle className="w-6 h-6" />
    if (name.includes('electrical') || name.includes('power'))
      return <Zap className="w-6 h-6" />
    if (name.includes('standard') || name.includes('norm'))
      return <BookOpen className="w-6 h-6" />
    return <Eye className="w-6 h-6" />
  }

  const getStatusColor = (status: string) => {
    switch (status) {
      case 'complete':
        return 'bg-green-950/30 border-green-700/30'
      case 'partial':
        return 'bg-amber-950/30 border-amber-700/30'
      case 'planned':
        return 'bg-blue-950/30 border-blue-700/30'
      default:
        return 'bg-navy-900/30 border-navy-700/30'
    }
  }

  const getStatusLabel = (status: string) => {
    switch (status) {
      case 'complete':
        return 'Vollständig'
      case 'partial':
        return 'Teilweise'
      case 'planned':
        return 'Geplant'
      default:
        return status
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
          {showSearchResults && searchResults.length === 0 && !isSearching && searchQuery.length > 1 && (
            <div className="text-center mt-8 py-12 animate-fade-in-up">
              <Eye className="w-12 h-12 text-navy-600 mx-auto mb-4" />
              <p className="text-navy-700 text-sm">Keine Ergebnisse für "{searchQuery}"</p>
              <p className="text-navy-600 text-xs mt-2">Versuchen Sie andere Suchbegriffe</p>
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
          <div className="card-premium bg-amber-950/20 border-amber-700/20 p-6 text-amber-300 text-sm">
            <p className="font-medium mb-1">Hinweis:</p>
            <p>{error}</p>
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
              {searchResults.map((result, idx) => (
                <button
                  key={result.id}
                  onClick={() => setSelectedDetail(result)}
                  style={{ animationDelay: `${idx * 80}ms` }}
                  className="animate-fade-in-up card-premium p-6 text-left hover:bg-sand-50 hover:shadow-lg hover:shadow-ocean-500/10 transition-all duration-200 group"
                  aria-label={`${result.title} öffnen`}
                >
                  <div className="flex items-start gap-3 mb-3">
                    <span className="text-ocean-600 group-hover:scale-110 group-hover:text-ocean-600 transition-all duration-200">
                      {getCategoryIcon(result.category_name)}
                    </span>
                    <div className="flex-1">
                      <p className="text-xs font-medium text-navy-700 uppercase tracking-wide">
                        {result.category_name}
                      </p>
                      <h3 className="font-serif font-medium text-navy-900 mt-1 group-hover:text-ocean-600 transition-colors">
                        {result.title}
                      </h3>
                    </div>
                  </div>
                  <p className="text-sm text-navy-700 line-clamp-2">{result.description}</p>
                </button>
              ))}
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
                  style={{ animationDelay: `${catIdx * 80}ms` }}
                  className="animate-fade-in-up w-full card-premium p-6 text-left hover:bg-sand-50 transition-all duration-200 group"
                  aria-expanded={expandedCategoryId === category.id}
                  aria-label={`${category.name} - ${expandedCategoryId === category.id ? 'Eingeklappt' : 'Ausgeklappt'}`}
                >
                  <div className="flex items-start justify-between">
                    <div className="flex items-start gap-4 flex-1">
                      <div className="flex-shrink-0 text-ocean-600 mt-1 group-hover:scale-110 group-hover:text-ocean-600 transition-all duration-200">
                        {getCategoryIcon(category.name)}
                      </div>
                      <div className="flex-1 min-w-0">
                        <div className="flex items-center gap-3 mb-2 flex-wrap">
                          <h3 className="font-serif text-lg font-medium text-navy-900 group-hover:text-ocean-600 transition-colors">
                            {category.name}
                          </h3>
                          <span
                            className={`px-2.5 py-1 rounded-full text-xs font-medium whitespace-nowrap border transition-all duration-200 ${
                              category.implementation_status === 'planned' && expandedCategoryId === category.id
                                ? 'animate-pulse-glow'
                                : ''
                            } ${getStatusColor(category.implementation_status)}`}
                          >
                            {getStatusLabel(category.implementation_status)}
                          </span>
                        </div>
                        <p className="text-sm text-navy-700 line-clamp-2 mb-3">{category.description}</p>
                        <div className="flex items-center gap-4 text-xs text-navy-600">
                          <span className="font-mono">
                            {category.subcategory_count} {category.subcategory_count === 1 ? 'Unterkategorie' : 'Unterkategorien'}
                          </span>
                          {category.documentation_ready && (
                            <span className="flex items-center gap-1 text-green-600">
                              ✓ Dokumentiert
                            </span>
                          )}
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

                {/* Expanded Subcategories */}
                {expandedCategoryId === category.id && (
                  <div className="pl-0 sm:pl-6 space-y-2 animate-slide-down">
                    {category.subcategories && category.subcategories.length > 0 ? (
                      category.subcategories.map((sub, subIdx) => (
                        <button
                          key={sub.id}
                          onClick={() => handleViewDetail(sub.id)}
                          style={{ animationDelay: `${subIdx * 60}ms` }}
                          className="animate-fade-in-up w-full card-premium p-4 text-left hover:bg-sand-50 hover:translate-x-1 transition-all duration-200 border-l-2 border-ocean-500/40 hover:border-ocean-500 group"
                          aria-label={`Öffne ${sub.name}`}
                        >
                          <h4 className="font-medium text-navy-900 mb-1 group-hover:text-ocean-600 transition-colors">
                            {sub.name}
                          </h4>
                          {sub.description && (
                            <p className="text-sm text-navy-700 line-clamp-1">{sub.description}</p>
                          )}
                        </button>
                      ))
                    ) : (
                      <div className="card-premium p-4 text-navy-700 text-sm">
                        Keine Unterkategorien verfügbar
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
                <h3 className="font-medium text-navy-900 mb-2">Über diese Wissensdatenbank</h3>
                <p className="text-sm text-navy-700 leading-relaxed">
                  Diese Wissensdatenbank ist Ihr digitales Nachschlagewerk für alle Aspekte des Yachtdesigns.
                  Ähnlich wie Nigel Calders klassisches Bootsbesitzer-Nachschlagewerk bietet es autorisierte,
                  vertrauenswürdige Informationen über Materialwissenschaft, Degradation, maritime Standards und bewährte Praktiken.
                  Alle Inhalte wurden von Fachleuten kuratiert und mit aktuellen Erkenntnissen aktualisiert.
                </p>
              </div>
            </div>
          </div>
        )}
      </div>

      {/* Detail Panel Modal */}
      {selectedDetail && (
        <KnowledgeDetailPanel data={selectedDetail} onClose={() => setSelectedDetail(null)} />
      )}
    </div>
  )
}

// Mock data for demo when API is not available
function getMockCategories(): KnowledgeCategory[] {
  return [
    {
      id: 'materials-overview',
      name: 'Materialwissenschaft',
      description: 'Umfassender Überblick über maritime Materialien, ihre Eigenschaften und optimale Anwendung',
      subcategory_count: 8,
      implementation_status: 'complete',
      documentation_ready: true,
      subcategories: [
        {
          id: 'teak-wood',
          name: 'Teakholz und tropische Hölzer',
          description: 'Eigenschaften, Behandlung und Langzeitverhalten',
        },
        {
          id: 'composite-materials',
          name: 'Verbundwerkstoffe',
          description: 'GFK, Kohlefaser und fortgeschrittene Materialen',
        },
      ],
    },
    {
      id: 'degradation-timelines',
      name: 'Degradationszeitleisten',
      description: 'Zeitbasierte Vorhersagen des Materialverhaltens in verschiedenen maritimen Umgebungen',
      subcategory_count: 6,
      implementation_status: 'complete',
      documentation_ready: true,
      subcategories: [
        {
          id: 'saltwater-exposure',
          name: 'Salzwassergefährdung',
          description: 'Korrosion und Abbau in Meeresumgebungen',
        },
        {
          id: 'tropical-climate',
          name: 'Tropische Bedingungen',
          description: 'UV-Strahlung und hohe Luftfeuchtigkeit',
        },
      ],
    },
    {
      id: 'known-issues',
      name: 'Bekannte Herstellungsprobleme',
      description: 'Dokumentierte Probleme und deren Lösungen nach Hersteller und Modell',
      subcategory_count: 12,
      implementation_status: 'partial',
      documentation_ready: true,
      subcategories: [
        {
          id: 'hallberg-rassy',
          name: 'Hallberg-Rassy Yachten',
          description: 'Qualitäts-Standards und bekannte Stärken',
        },
        {
          id: 'x-yachts',
          name: 'X-Yachts',
          description: 'Design-Philosophie und typische Details',
        },
      ],
    },
    {
      id: 'marine-standards',
      name: 'Maritime Standards & Zertifizierungen',
      description: 'Geltende Normen, Klassifikationen und Compliance-Anforderungen',
      subcategory_count: 5,
      implementation_status: 'complete',
      documentation_ready: true,
      subcategories: [
        {
          id: 'iso-standards',
          name: 'ISO-Normen für Yachtbau',
          description: 'Internationale Sicherheits- und Qualitätsstandards',
        },
        {
          id: 'ce-marking',
          name: 'CE-Kennzeichnung',
          description: 'Europäische Konformitätsanforderungen',
        },
      ],
    },
    {
      id: 'best-practices',
      name: 'Best Practices & Wartung',
      description: 'Bewährte Verfahren für Wartung, Reparatur und Erhaltung',
      subcategory_count: 7,
      implementation_status: 'complete',
      documentation_ready: true,
      subcategories: [
        {
          id: 'preventive-maintenance',
          name: 'Vorbeugende Wartung',
          description: 'Zeitpläne und Verfahren',
        },
        {
          id: 'restoration',
          name: 'Restaurierung',
          description: 'Verfahren zur Wiederherstellung klassischer Materialien',
        },
      ],
    },
    {
      id: 'environmental-impact',
      name: 'Umweltauswirkungen',
      description: 'Nachhaltigkeit, Umweltbelastung und ökologische Überlegungen',
      subcategory_count: 4,
      implementation_status: 'partial',
      documentation_ready: false,
      subcategories: [
        {
          id: 'sustainable-materials',
          name: 'Nachhaltige Materialien',
          description: 'Umweltfreundliche Alternativen',
        },
      ],
    },
  ]
}
