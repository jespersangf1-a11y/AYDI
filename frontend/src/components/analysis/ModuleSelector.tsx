import type { AnalysisModule } from '../../types'
import { ANALYSIS_MODULE_LABELS } from '../../types'

interface ModuleSelectorProps {
  onSelect: (module: AnalysisModule) => void
  selectedModule?: AnalysisModule | null
  availableModules?: AnalysisModule[]
}

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
    // When availableModules is explicitly provided, respect it
    if (availableModules) return availableModules.includes(mod)
    // Otherwise ALL modules are available — the backend handles
    // graceful degradation when optional data is missing
    return true
  }

  const getDisabledReason = (mod: AnalysisModule): string | undefined => {
    if (availableModules && !availableModules.includes(mod)) return 'Nicht verfügbar'
    // Show hints for modules that benefit from extra data, but don't disable them
    if (REQUIRES_EXTRA[mod]) return undefined
    return undefined
  }

  return (
    <div className="space-y-5">
      <h3 className="font-serif text-title font-semibold text-navy-900">Analysemodul wählen</h3>
      <div className="grid gap-4 sm:grid-cols-2 lg:grid-cols-3">
        {allModules.map((mod) => {
          const available = isAvailable(mod)
          const disabledReason = getDisabledReason(mod)
          const isSelected = selectedModule === mod
          return (
            <button
              key={mod}
              disabled={!available}
              onClick={() => available && onSelect(mod)}
              className={`text-left rounded-xl p-4 border transition-all duration-200 ${
                isSelected
                  ? 'card-premium border-ocean-600/60 bg-ocean-900/30 text-navy-900'
                  : available
                  ? 'card-premium hover:border-ocean-600/40 hover:bg-sand-50/40 text-navy-900'
                  : 'card-premium border-navy-800/40 bg-navy-900/20 text-navy-600 cursor-not-allowed opacity-60'
              }`}
            >
              <div className="flex items-start justify-between mb-2">
                <span
                  className={`text-sm font-sans font-semibold ${
                    isSelected ? 'text-ocean-200' : available ? 'text-navy-900' : 'text-navy-500'
                  }`}
                >
                  {ANALYSIS_MODULE_LABELS[mod]}
                </span>
                {isSelected && (
                  <span className="text-xs px-2 py-1 rounded-full bg-ocean-700/60 text-ocean-200 font-medium">
                    Aktiv
                  </span>
                )}
                {!available && disabledReason && (
                  <span className="text-xs text-navy-500 text-right leading-tight ml-2">
                    {disabledReason}
                  </span>
                )}
              </div>
              {MODULE_DESCRIPTIONS[mod] && (
                <p
                  className={`text-xs leading-relaxed ${
                    available ? 'text-navy-600' : 'text-navy-700'
                  }`}
                >
                  {MODULE_DESCRIPTIONS[mod]}
                </p>
              )}
              {available && REQUIRES_EXTRA[mod] && !isSelected && (
                <p className="text-[10px] text-navy-500 mt-1.5 italic">
                  Hinweis: {REQUIRES_EXTRA[mod]}
                </p>
              )}
            </button>
          )
        })}
      </div>
    </div>
  )
}
