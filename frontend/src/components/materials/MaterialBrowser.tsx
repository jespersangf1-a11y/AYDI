import { useEffect, useState } from 'react'
import { X } from 'lucide-react'
import { getMaterials } from '../../services/api'

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

  if (loading) {
    return <div className="text-navy-400">Lade Materialien...</div>
  }

  if (error) {
    return (
      <div className="bg-red-900/50 border border-red-700 rounded-lg p-4 text-red-300 text-sm">
        Fehler beim Laden: {error}
      </div>
    )
  }

  return (
    <div className="space-y-4">
      <div className="flex items-center justify-between">
        <h2 className="font-display text-2xl font-bold text-white">Materialdatenbank</h2>
        <div className="flex items-center gap-3">
          <label className="text-sm text-navy-400">Kategorie:</label>
          <select
            value={selectedCategory}
            onChange={(e) => handleCategoryChange(e.target.value)}
            className="bg-navy-800 border border-navy-600 rounded-lg px-3 py-2 text-white text-sm focus:outline-none focus:border-ocean-500 transition-colors"
          >
            <option value="">Alle Kategorien</option>
            {categories.map((c) => (
              <option key={c} value={c}>
                {c}
              </option>
            ))}
          </select>
        </div>
      </div>

      <div className="flex gap-4">
        {/* Table */}
        <div className="flex-1 bg-navy-900 border border-navy-700 rounded-xl overflow-hidden">
          {filtered.length === 0 ? (
            <div className="p-8 text-center text-navy-400">
              Keine Materialien in dieser Kategorie
            </div>
          ) : (
            <table className="w-full text-sm">
              <thead>
                <tr className="border-b border-navy-700">
                  <th className="text-left px-4 py-3 text-navy-400 font-medium">Name</th>
                  <th className="text-left px-4 py-3 text-navy-400 font-medium">Kategorie</th>
                  <th className="text-left px-4 py-3 text-navy-400 font-medium">Unterkategorie</th>
                  <th className="text-right px-4 py-3 text-navy-400 font-medium">Preis / Einheit</th>
                  <th className="text-right px-4 py-3 text-navy-400 font-medium">Lebensdauer</th>
                  <th className="text-right px-4 py-3 text-navy-400 font-medium">Wartung</th>
                </tr>
              </thead>
              <tbody>
                {filtered.map((m) => (
                  <tr
                    key={m.id}
                    onClick={() => setSelectedMaterial(m)}
                    className={`border-b border-navy-800 cursor-pointer transition-colors ${
                      selectedMaterial?.id === m.id
                        ? 'bg-ocean-900/30'
                        : 'hover:bg-navy-800'
                    }`}
                  >
                    <td className="px-4 py-3 text-white font-medium">{m.name}</td>
                    <td className="px-4 py-3 text-navy-300">{m.category}</td>
                    <td className="px-4 py-3 text-navy-400">{m.subcategory ?? '—'}</td>
                    <td className="px-4 py-3 text-right font-mono text-navy-300">
                      {m.cost_eur_per_unit != null
                        ? `${m.cost_eur_per_unit.toFixed(2)} € / ${m.unit ?? 'Stk.'}`
                        : '—'}
                    </td>
                    <td className="px-4 py-3 text-right font-mono text-navy-300">
                      {m.lifespan_years != null ? `${m.lifespan_years} Jahre` : '—'}
                    </td>
                    <td className="px-4 py-3 text-right font-mono text-navy-300">
                      {m.maintenance_interval_months != null
                        ? `${m.maintenance_interval_months} Mo.`
                        : '—'}
                    </td>
                  </tr>
                ))}
              </tbody>
            </table>
          )}
        </div>

        {/* Detail panel */}
        {selectedMaterial && (
          <div className="w-72 shrink-0 bg-navy-900 border border-navy-700 rounded-xl p-5">
            <div className="flex items-start justify-between mb-4">
              <h3 className="font-display font-semibold text-white">{selectedMaterial.name}</h3>
              <button
                onClick={() => setSelectedMaterial(null)}
                className="text-navy-400 hover:text-white transition-colors"
              >
                <X className="w-4 h-4" />
              </button>
            </div>

            <div className="space-y-3 text-sm">
              <div>
                <span className="text-navy-500">Kategorie</span>
                <p className="text-white mt-0.5">{selectedMaterial.category}</p>
              </div>
              {selectedMaterial.subcategory && (
                <div>
                  <span className="text-navy-500">Unterkategorie</span>
                  <p className="text-white mt-0.5">{selectedMaterial.subcategory}</p>
                </div>
              )}
              {selectedMaterial.cost_eur_per_unit != null && (
                <div>
                  <span className="text-navy-500">Preis</span>
                  <p className="font-mono text-ocean-300 mt-0.5">
                    {selectedMaterial.cost_eur_per_unit.toFixed(2)} € / {selectedMaterial.unit ?? 'Stk.'}
                  </p>
                </div>
              )}
              {selectedMaterial.lifespan_years != null && (
                <div>
                  <span className="text-navy-500">Lebensdauer</span>
                  <p className="font-mono text-white mt-0.5">{selectedMaterial.lifespan_years} Jahre</p>
                </div>
              )}
              {selectedMaterial.maintenance_interval_months != null && (
                <div>
                  <span className="text-navy-500">Wartungsintervall</span>
                  <p className="font-mono text-white mt-0.5">
                    {selectedMaterial.maintenance_interval_months} Monate
                  </p>
                </div>
              )}
              {selectedMaterial.notes && (
                <div>
                  <span className="text-navy-500">Notizen</span>
                  <p className="text-navy-300 mt-0.5 text-xs leading-relaxed">
                    {selectedMaterial.notes}
                  </p>
                </div>
              )}
              {selectedMaterial.properties &&
                Object.keys(selectedMaterial.properties).length > 0 && (
                  <div>
                    <span className="text-navy-500 block mb-1">Eigenschaften</span>
                    <div className="space-y-1">
                      {Object.entries(selectedMaterial.properties).map(([k, v]) => (
                        <div key={k} className="flex justify-between">
                          <span className="text-navy-400 text-xs">{k}</span>
                          <span className="font-mono text-xs text-white">{String(v)}</span>
                        </div>
                      ))}
                    </div>
                  </div>
                )}
            </div>
          </div>
        )}
      </div>
    </div>
  )
}
