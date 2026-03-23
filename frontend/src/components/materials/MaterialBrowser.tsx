import { useEffect, useState } from 'react'
import { X } from 'lucide-react'
import { getMaterials } from '../../services/api'
import { MEDIA } from '../../config/media'
import HeroSection from '../layout/HeroSection'

interface Material {
  id: string
  name: string
  category: string
  subcategory?: string | null
  cost_eur_per_unit?: number | null
  unit?: string | null
  lifespan_years?: number | null
  maintenance_interval_months?: number | null
  properties?: Record<string, unknown> | null
  notes?: string | null
}


export default function MaterialBrowser() {
  const [materials, setMaterials] = useState<Material[]>([])
  const [filtered, setFiltered] = useState<Material[]>([])
  const [categories, setCategories] = useState<string[]>([])
  const [selectedCategory, setSelectedCategory] = useState<string>('')
  const [selectedMaterial, setSelectedMaterial] = useState<Material | null>(null)
  const [loading, setLoading] = useState(true)
  const [error, setError] = useState<string | null>(null)
  const [searchTerm, setSearchTerm] = useState<string>('')
  const [isMobileDetailOpen, setIsMobileDetailOpen] = useState(false)

  useEffect(() => {
    getMaterials()
      .then((data) => {
        const mats = data as Material[]
        setMaterials(mats)
        setFiltered(mats)
        const cats = Array.from(new Set(mats.map((m) => m.category))).sort()
        setCategories(cats)
      })
      .catch((e) => setError(e.message))
      .finally(() => setLoading(false))
  }, [])

  const handleCategoryChange = (cat: string) => {
    setSelectedCategory(cat)
    if (cat === '') {
      setFiltered(materials)
    } else {
      setFiltered(materials.filter((m) => m.category === cat))
    }
    setSelectedMaterial(null)
    setSearchTerm('')
  }

  const handleSearchChange = (term: string) => {
    setSearchTerm(term)
    const categoryFiltered =
      selectedCategory === ''
        ? materials
        : materials.filter((m) => m.category === selectedCategory)

    const searchFiltered = categoryFiltered.filter((m) =>
      m.name.toLowerCase().includes(term.toLowerCase()) ||
      m.category.toLowerCase().includes(term.toLowerCase()) ||
      (m.subcategory?.toLowerCase().includes(term.toLowerCase()) ?? false)
    )
    setFiltered(searchFiltered)
    setSelectedMaterial(null)
  }

  const handleSelectMaterial = (material: Material) => {
    setSelectedMaterial(material)
    setIsMobileDetailOpen(true)
  }

  const handleCloseDetail = () => {
    setSelectedMaterial(null)
    setIsMobileDetailOpen(false)
  }

  return (
      <div>
        <HeroSection
          backgroundImage={MEDIA.materials.teak_deck}
          title="Materialdatenbank"
          subtitle="Umfassende Sammlung maritimer Materialien mit Kostendaten, Lebensdauer und Wartungsintervallen"
          label="Material"
        />

        <div className="space-y-8 px-6 md:px-10 py-12">
          {/* Controls */}
          <div className="space-y-4 md:space-y-0 md:flex md:items-end md:justify-between gap-4 animate-fade-in-up">
            <div>
              <p className="label-premium mb-2">FILTER</p>
              <label className="text-xs font-medium text-navy-700">Kategorie:</label>
            </div>
            <div className="flex flex-col md:flex-row gap-3">
              <select
                value={selectedCategory}
                onChange={(e) => handleCategoryChange(e.target.value)}
                className="bg-sand-50/60 border border-sand-200 rounded-lg px-4 py-2.5 text-navy-900 text-sm focus:outline-none focus:border-ocean-500/60 transition-all duration-200 focus:ring-2 focus:ring-ocean-500/20"
              >
                <option value="">Alle Kategorien</option>
                {categories.map((c) => (
                  <option key={c} value={c}>
                    {c}
                  </option>
                ))}
              </select>
              <input
                type="text"
                placeholder="Nach Material suchen..."
                value={searchTerm}
                onChange={(e) => handleSearchChange(e.target.value)}
                className="bg-sand-50/60 border border-sand-200 rounded-lg px-4 py-2.5 text-navy-900 text-sm placeholder:text-navy-500 focus:outline-none focus:border-ocean-500/60 transition-all duration-200 focus:ring-2 focus:ring-ocean-500/20"
                aria-label="Materialen suchen"
              />
            </div>
          </div>

          {loading && (
            <div className="space-y-2">
              {Array.from({ length: 6 }).map((_, i) => (
                <div key={i} className="flex items-center gap-4 px-6 py-4">
                  <div className="skeleton w-1/4 h-4 rounded" />
                  <div className="skeleton w-1/5 h-4 rounded hidden sm:block" />
                  <div className="skeleton w-1/5 h-4 rounded hidden md:block" />
                  <div className="skeleton w-16 h-4 rounded ml-auto" />
                  <div className="skeleton w-12 h-4 rounded hidden sm:block" />
                  <div className="skeleton w-12 h-4 rounded hidden lg:block" />
                </div>
              ))}
            </div>
          )}

          {error && (
            <div className="card-premium bg-red-950/20 border-red-700/20 p-6 text-red-300 text-sm" role="alert">
              Fehler beim Laden: {error}
            </div>
          )}

          {!loading && !error && (
            <div className="flex flex-col lg:flex-row gap-8">
              {/* Table */}
              <div className="flex-1 overflow-hidden">
                {filtered.length === 0 ? (
                  <div className="card-premium px-8 md:px-10 py-12 text-center text-navy-600">
                    Keine Materialien gefunden
                  </div>
                ) : (
                  <div className="overflow-x-auto">
                    <table className="w-full text-sm">
                      <thead>
                        <tr className="border-b border-sand-200">
                          <th className="text-left px-4 md:px-6 py-4 label-premium font-semibold">Material</th>
                          <th className="hidden sm:table-cell text-left px-4 md:px-6 py-4 label-premium font-semibold">Kategorie</th>
                          <th className="hidden md:table-cell text-left px-4 md:px-6 py-4 label-premium font-semibold">Unterkategorie</th>
                          <th className="text-right px-4 md:px-6 py-4 label-premium font-semibold">Preis</th>
                          <th className="hidden sm:table-cell text-right px-4 md:px-6 py-4 label-premium font-semibold">Lebensdauer</th>
                          <th className="hidden lg:table-cell text-right px-4 md:px-6 py-4 label-premium font-semibold">Wartung</th>
                        </tr>
                      </thead>
                      <tbody>
                        {filtered.map((m) => (
                          <tr
                            key={m.id}
                            onClick={() => handleSelectMaterial(m)}
                            className={`hover:bg-[rgba(45,139,168,0.1)] hover:pl-2 transition-all duration-300 border-b border-navy-700/20 cursor-pointer even:bg-sand-50/50 focus-visible:outline-2 focus-visible:outline-ocean-400 focus-visible:outline-offset-[-2px] ${
                              selectedMaterial?.id === m.id
                                ? 'bg-ocean-700/15 border-ocean-600/40'
                                : ''
                            }`}
                            role="row"
                            tabIndex={0}
                            onKeyDown={(e) => {
                              if (e.key === 'Enter' || e.key === ' ') {
                                e.preventDefault()
                                handleSelectMaterial(m)
                              } else if (e.key === 'ArrowDown') {
                                e.preventDefault()
                                const next = (e.currentTarget as HTMLElement).nextElementSibling as HTMLElement | null
                                next?.focus()
                              } else if (e.key === 'ArrowUp') {
                                e.preventDefault()
                                const prev = (e.currentTarget as HTMLElement).previousElementSibling as HTMLElement | null
                                prev?.focus()
                              }
                            }}
                            aria-label={`Material: ${m.name}, Kategorie: ${m.category}`}
                          >
                            <td className="px-4 md:px-6 py-4 text-navy-900 font-medium text-sm">{m.name}</td>
                            <td className="hidden sm:table-cell px-4 md:px-6 py-4 text-navy-700 text-sm">{m.category}</td>
                            <td className="hidden md:table-cell px-4 md:px-6 py-4 text-navy-600 text-sm">{m.subcategory ?? ''}</td>
                            <td className="px-4 md:px-6 py-4 text-right font-mono text-navy-700 text-sm">
                              {m.cost_eur_per_unit != null
                                ? `${m.cost_eur_per_unit.toFixed(0)} € / ${m.unit ?? 'Stk.'}`
                                : '—'}
                            </td>
                            <td className="hidden sm:table-cell px-4 md:px-6 py-4 text-right font-mono text-navy-700 text-sm">
                              {m.lifespan_years != null ? `${m.lifespan_years} J.` : '—'}
                            </td>
                            <td className="hidden lg:table-cell px-4 md:px-6 py-4 text-right font-mono text-navy-700 text-sm">
                              {m.maintenance_interval_months != null
                                ? `${m.maintenance_interval_months} Mo.`
                                : '—'}
                            </td>
                          </tr>
                        ))}
                      </tbody>
                    </table>
                  </div>
                )}
              </div>

              {/* Detail panel — Desktop */}
              {selectedMaterial && (
                <div className="hidden lg:flex lg:w-80 lg:shrink-0 card-premium p-8 space-y-6 animate-slide-in-right max-h-96 overflow-y-auto">
                  <DetailPanel material={selectedMaterial} onClose={() => setSelectedMaterial(null)} />
                </div>
              )}
            </div>
          )}

          {/* Detail panel — Mobile Overlay */}
          {selectedMaterial && isMobileDetailOpen && (
            <div className="lg:hidden fixed inset-0 z-50 animate-backdrop-fade before:content-[''] before:absolute before:inset-0 before:bg-black/40 before:-z-10">
              <div className="absolute bottom-0 left-0 right-0 card-premium rounded-t-2xl p-6 space-y-6 max-h-[70vh] overflow-y-auto animate-slide-in-right">
                <div className="flex items-start justify-between mb-4">
                  <h3 className="font-serif text-lg font-medium text-navy-900">Details</h3>
                  <button
                    onClick={handleCloseDetail}
                    className="text-navy-600 hover:text-ocean-700 transition-colors duration-200"
                    aria-label="Detail-Panel schließen"
                  >
                    <X className="w-6 h-6" />
                  </button>
                </div>
                <DetailPanel material={selectedMaterial} onClose={handleCloseDetail} />
              </div>
            </div>
          )}
        </div>
      </div>
  )
}

function DetailPanel({ material, onClose }: { material: Material; onClose: () => void }) {
  return (
    <>
      <div className="hidden lg:block">
        <div className="flex items-start justify-between mb-4">
          <h3 className="font-serif text-lg font-medium text-navy-900">{material.name}</h3>
          <button
            onClick={onClose}
            className="text-navy-600 hover:text-ocean-700 transition-colors duration-200"
            aria-label="Panel schließen"
          >
            <X className="w-5 h-5" />
          </button>
        </div>
      </div>

      <div className="space-y-4 border-t border-navy-700/30 pt-6 lg:pt-0 lg:border-t-0">
        {material.category && (
          <div>
            <p className="label-premium mb-1">KATEGORIE</p>
            <p className="text-navy-900">{material.category}</p>
          </div>
        )}
        {material.subcategory && (
          <div>
            <p className="label-premium mb-1">UNTERKATEGORIE</p>
            <p className="text-navy-900">{material.subcategory}</p>
          </div>
        )}
        {material.cost_eur_per_unit != null && (
          <div>
            <p className="label-premium mb-1">PREIS</p>
            <p className="font-mono text-ocean-600">
              {material.cost_eur_per_unit.toFixed(2)} € / {material.unit ?? 'Stk.'}
            </p>
          </div>
        )}
        {material.lifespan_years != null && (
          <div>
            <p className="label-premium mb-1">LEBENSDAUER</p>
            <p className="font-mono text-navy-900">{material.lifespan_years} Jahre</p>
          </div>
        )}
        {material.maintenance_interval_months != null && (
          <div>
            <p className="label-premium mb-1">WARTUNGSINTERVALL</p>
            <p className="font-mono text-navy-900">{material.maintenance_interval_months} Monate</p>
          </div>
        )}
        {material.notes && (
          <div>
            <p className="label-premium mb-1">NOTIZEN</p>
            <p className="text-navy-700 text-sm leading-relaxed">{material.notes}</p>
          </div>
        )}
        {material.properties && Object.keys(material.properties).length > 0 && (
          <div>
            <p className="label-premium mb-2">EIGENSCHAFTEN</p>
            <div className="space-y-1.5 text-xs">
              {Object.entries(material.properties).map(([k, v]) => (
                <div key={k} className="flex justify-between">
                  <span className="text-navy-600">{k}</span>
                  <span className="font-mono text-navy-700">{String(v)}</span>
                </div>
              ))}
            </div>
          </div>
        )}
      </div>
    </>
  )
}
