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
  }

  return (
    <div>
      <HeroSection
        backgroundImage={MEDIA.materials.teak_deck}
        title="Materialdatenbank"
        subtitle="Umfassende Sammlung maritimer Materialien mit Kostendaten, Lebensdauer und Wartungsintervallen"
        label="Material"
      />

      <div className="space-y-8 px-10 py-12">
        {/* Controls */}
        <div className="flex items-center justify-between">
          <div>
            <p className="label-premium mb-2">FILTER</p>
            <label className="text-xs font-medium text-navy-300">Kategorie:</label>
          </div>
          <select
            value={selectedCategory}
            onChange={(e) => handleCategoryChange(e.target.value)}
            className="bg-navy-800/60 border border-navy-600/40 rounded-lg px-4 py-2.5 text-navy-100 text-sm focus:outline-none focus:border-ocean-500/60 transition-colors duration-200"
          >
            <option value="">Alle Kategorien</option>
            {categories.map((c) => (
              <option key={c} value={c}>
                {c}
              </option>
            ))}
          </select>
        </div>

        {loading && (
          <div className="text-center py-12 text-navy-400">
            Materialien werden geladen...
          </div>
        )}

        {error && (
          <div className="card-premium bg-red-950/20 border-red-700/20 p-6 text-red-300 text-sm">
            Fehler beim Laden: {error}
          </div>
        )}

        {!loading && !error && (
          <div className="flex gap-8">
            {/* Table */}
            <div className="flex-1 overflow-hidden">
              {filtered.length === 0 ? (
                <div className="card-premium px-10 py-12 text-center text-navy-400">
                  Keine Materialien in dieser Kategorie
                </div>
              ) : (
                <div className="overflow-x-auto">
                  <table className="w-full text-sm">
                    <thead>
                      <tr className="border-b border-navy-700/40">
                        <th className="text-left px-6 py-4 label-premium font-semibold">Material</th>
                        <th className="text-left px-6 py-4 label-premium font-semibold">Kategorie</th>
                        <th className="text-left px-6 py-4 label-premium font-semibold">Unterkategorie</th>
                        <th className="text-right px-6 py-4 label-premium font-semibold">Preis / Einheit</th>
                        <th className="text-right px-6 py-4 label-premium font-semibold">Lebensdauer</th>
                        <th className="text-right px-6 py-4 label-premium font-semibold">Wartung</th>
                      </tr>
                    </thead>
                    <tbody>
                      {filtered.map((m, idx) => (
                        <tr
                          key={m.id}
                          onClick={() => setSelectedMaterial(m)}
                          className={`border-b border-navy-700/20 cursor-pointer transition-colors duration-200 ${
                            idx % 2 === 0 ? 'bg-navy-900/20' : 'bg-transparent'
                          } ${
                            selectedMaterial?.id === m.id
                              ? 'bg-ocean-700/15'
                              : 'hover:bg-ocean-700/10'
                          }`}
                        >
                          <td className="px-6 py-4 text-white font-medium">{m.name}</td>
                          <td className="px-6 py-4 text-navy-300 text-sm">{m.category}</td>
                          <td className="px-6 py-4 text-navy-400 text-sm">{m.subcategory ?? ''}</td>
                          <td className="px-6 py-4 text-right font-mono text-navy-300 text-sm">
                            {m.cost_eur_per_unit != null
                              ? `${m.cost_eur_per_unit.toFixed(2)} € / ${m.unit ?? 'Stk.'}`
                              : ''}
                          </td>
                          <td className="px-6 py-4 text-right font-mono text-navy-300 text-sm">
                            {m.lifespan_years != null ? `${m.lifespan_years} J.` : ''}
                          </td>
                          <td className="px-6 py-4 text-right font-mono text-navy-300 text-sm">
                            {m.maintenance_interval_months != null
                              ? `${m.maintenance_interval_months} Mo.`
                              : ''}
                          </td>
                        </tr>
                      ))}
                    </tbody>
                  </table>
                </div>
              )}
            </div>

            {/* Detail panel */}
            {selectedMaterial && (
              <div className="w-80 shrink-0 card-premium p-8 space-y-6">
                <div className="flex items-start justify-between">
                  <div>
                    <h3 className="font-serif text-lg font-medium text-white">
                      {selectedMaterial.name}
                    </h3>
                  </div>
                  <button
                    onClick={() => setSelectedMaterial(null)}
                    className="text-navy-400 hover:text-ocean-300 transition-colors duration-200 ml-2"
                  >
                    <X className="w-5 h-5" />
                  </button>
                </div>

                <div className="space-y-4 border-t border-navy-700/30 pt-6">
                  {selectedMaterial.category && (
                    <div>
                      <p className="label-premium mb-1">KATEGORIE</p>
                      <p className="text-white">{selectedMaterial.category}</p>
                    </div>
                  )}
                  {selectedMaterial.subcategory && (
                    <div>
                      <p className="label-premium mb-1">UNTERKATEGORIE</p>
                      <p className="text-white">{selectedMaterial.subcategory}</p>
                    </div>
                  )}
                  {selectedMaterial.cost_eur_per_unit != null && (
                    <div>
                      <p className="label-premium mb-1">PREIS</p>
                      <p className="font-mono text-ocean-300">
                        {selectedMaterial.cost_eur_per_unit.toFixed(2)} € / {selectedMaterial.unit ?? 'Stk.'}
                      </p>
                    </div>
                  )}
                  {selectedMaterial.lifespan_years != null && (
                    <div>
                      <p className="label-premium mb-1">LEBENSDAUER</p>
                      <p className="font-mono text-white">{selectedMaterial.lifespan_years} Jahre</p>
                    </div>
                  )}
                  {selectedMaterial.maintenance_interval_months != null && (
                    <div>
                      <p className="label-premium mb-1">WARTUNGSINTERVALL</p>
                      <p className="font-mono text-white">{selectedMaterial.maintenance_interval_months} Monate</p>
                    </div>
                  )}
                  {selectedMaterial.notes && (
                    <div>
                      <p className="label-premium mb-1">NOTIZEN</p>
                      <p className="text-navy-300 text-sm leading-relaxed">
                        {selectedMaterial.notes}
                      </p>
                    </div>
                  )}
                  {selectedMaterial.properties &&
                    Object.keys(selectedMaterial.properties).length > 0 && (
                      <div>
                        <p className="label-premium mb-2">EIGENSCHAFTEN</p>
                        <div className="space-y-1.5 text-xs">
                          {Object.entries(selectedMaterial.properties).map(([k, v]) => (
                            <div key={k} className="flex justify-between">
                              <span className="text-navy-400">{k}</span>
                              <span className="font-mono text-navy-300">{String(v)}</span>
                            </div>
                          ))}
                        </div>
                      </div>
                    )}
                </div>
              </div>
            )}
          </div>
        )}
      </div>
    </div>
  )
}
