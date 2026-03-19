import { ArrowRight, Layers } from 'lucide-react'
import { ANALYSIS_MODULE_LABELS } from '../../types'
import type { AnalysisModule } from '../../types'

interface UpgradePromptProps {
  upgradePrompt: {
    message: string
    additional_modules: string[]
  }
  onUpgrade?: () => void
}

export default function UpgradePrompt({ upgradePrompt, onUpgrade }: UpgradePromptProps) {
  const moduleCount = upgradePrompt.additional_modules.length

  return (
    <div className="bg-gradient-to-br from-ocean-900/40 to-navy-900 border border-ocean-700/50 rounded-xl p-6">
      <div className="flex items-start gap-4">
        <div className="w-10 h-10 rounded-lg bg-ocean-800/60 flex items-center justify-center shrink-0">
          <Layers className="w-5 h-5 text-ocean-300" />
        </div>
        <div className="flex-1">
          <h3 className="font-display font-semibold text-white mb-1">
            Vollanalyse freischalten
          </h3>
          <p className="text-sm text-navy-300 mb-4">
            Mit CAD-Daten und Materialwahl können{' '}
            <span className="text-ocean-300 font-semibold">{moduleCount} weitere Module</span>{' '}
            ausgewertet werden.
          </p>

          {upgradePrompt.additional_modules.length > 0 && (
            <div className="flex flex-wrap gap-2 mb-5">
              {upgradePrompt.additional_modules.map((mod) => (
                <span
                  key={mod}
                  className="px-2.5 py-1 rounded-full bg-navy-800 border border-navy-600 text-xs text-navy-300"
                >
                  {ANALYSIS_MODULE_LABELS[mod as AnalysisModule] ?? mod}
                </span>
              ))}
            </div>
          )}

          <button
            onClick={onUpgrade}
            className="inline-flex items-center gap-2 px-5 py-2.5 rounded-lg bg-ocean-600 hover:bg-ocean-500 text-white text-sm font-semibold transition-colors"
          >
            Vollanalyse starten
            <ArrowRight className="w-4 h-4" />
          </button>
        </div>
      </div>
    </div>
  )
}
