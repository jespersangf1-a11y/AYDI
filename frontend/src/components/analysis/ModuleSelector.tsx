import type { AnalysisModule } from '../../types'
import { ANALYSIS_MODULE_LABELS } from '../../types'

interface ModuleSelectorProps {
  onSelect: (module: AnalysisModule) => void
  selectedModule?: AnalysisModule | null
  availableModules?: AnalysisModule[]
}

// Modules that can be run without additional data
const ALWAYS_AVAILABLE: AnalysisModule[] = ['ergonomics', 'volume_storage']

// Modules that require extra inputs
const REQUIRES_EXTRA: Partial<Record<AnalysisModule, string>> = {
  materials: 'Materialdaten benötigt',
  cost: 'Kostendaten benötigt',
  compliance: 'Normversion erforderlich',
  brand_dna: 'Mind. 3 Referenzmodelle benötigt',
  market: 'Wettbewerbsdaten benötigt',
}

const MODULE_DESCRIPTIONS: Partial<Record<AnalysisModule, string>> = {
  ergonomics: 'Durchgangsbreiten, Wegeführung, Erreichbarkeit',
  volume_storage: 'Stauraumverteilung, Möblierungsgrad, Volumennutzung',
  emotional: 'Proportionen, Licht, Sichtachsen, visuelle Ruhe',
  compliance: 'ISO-Normen, CE-Kategorie, Fluchtwege',
  production: 'Montagesequenz, Formkomplexität, Servicezugang',
  materials: 'Materialqualität, Kosten, Lebensdauer',
  structural: 'Schwerpunkt, Lastverteilung, Strukturbereiche',
  cost: 'Kostenschätzung nach Zonen und Kategorien',
  service_patterns: 'Wartungshäufigkeiten, Problemzonen',
  brand_dna: 'Geometrischer Vergleich mit Werft-Referenzmodellen',
  market: 'Kennzahlenvergleich mit Wettbewerbern',
}

export default function ModuleSelector({
  onSelect,
  selectedModule,
  availableModules,
}: ModuleSelectorProps) {
  const allModules = Object.keys(ANALYSIS_MODULE_LABELS) as AnalysisModule[]

  const isAvailable = (mod: AnalysisModule): boolean => {
    if (availableModules) return availableModules.includes(mod)
    return ALWAYS_AVAILABLE.includes(mod) || !REQUIRES_EXTRA[mod]
  }

  const getDisabledReason = (mod: AnalysisModule): string | undefined => {
    if (availableModules && !availableModules.includes(mod)) return 'Nicht verfügbar'
    return REQUIRES_EXTRA[mod]
  }

  return (
    <div>
      <h3 className="font-display font-semibold text-white mb-4">Analysemodul wählen</h3>
      <div className="grid gap-3 sm:grid-cols-2 lg:grid-cols-3">
        {allModules.map((mod) => {
          const available = isAvailable(mod)
          const disabledReason = getDisabledReason(mod)
          const isSelected = selectedModule === mod
          return (
            <button
              key={mod}
              disabled={!available}
              onClick={() => available && onSelect(mod)}
              className={`text-left rounded-xl p-4 border transition-all ${
                isSelected
                  ? 'bg-ocean-900/50 border-ocean-600 text-white'
                  : available
                  ? 'bg-navy-900 border-navy-700 hover:border-ocean-600 hover:bg-navy-800 text-white'
                  : 'bg-navy-900/50 border-navy-800 text-navy-600 cursor-not-allowed'
              }`}
            >
              <div className="flex items-start justify-between mb-1">
                <span
                  className={`text-sm font-semibold ${
                    isSelected ? 'text-ocean-200' : available ? 'text-white' : 'text-navy-500'
                  }`}
                >
                  {ANALYSIS_MODULE_LABELS[mod]}
                </span>
                {isSelected && (
                  <span className="text-xs px-1.5 py-0.5 rounded bg-ocean-700 text-ocean-200">
                    Aktiv
                  </span>
                )}
                {!available && disabledReason && (
                  <span className="text-xs text-navy-600 text-right leading-tight ml-2">
                    {disabledReason}
                  </span>
                )}
              </div>
              {MODULE_DESCRIPTIONS[mod] && (
                <p
                  className={`text-xs leading-relaxed ${
                    available ? 'text-navy-400' : 'text-navy-700'
                  }`}
                >
                  {MODULE_DESCRIPTIONS[mod]}
                </p>
              )}
            </button>
          )
        })}
      </div>
    </div>
  )
}
