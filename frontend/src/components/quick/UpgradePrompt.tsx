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
    <div className="bg-navy-900/40 border border-navy-700/40 rounded-xl p-6 backdrop-blur-sm">
      <div className="flex items-start gap-4">
        <div className="w-10 h-10 rounded-lg bg-navy-800/50 flex items-center justify-center shrink-0">
          <Layers className="w-5 h-5 text-ocean-500" />
        </div>
        <div className="flex-1">
          <h3 className="font-serif font-semibold text-white mb-2">
            Vollständige Analyse freischalten
          </h3>
          <p className="text-sm text-navy-400 mb-4 leading-relaxed">
            Mit CAD-Daten und Materialwahl können <span className="text-ocean-400 font-semibold">{moduleCount} zusätzliche Module</span> ausgewertet werden.
          </p>

          {upgradePrompt.additional_modules.length > 0 && (
            <div className="flex flex-wrap gap-2 mb-5">
              {upgradePrompt.additional_modules.map((mod) => (
                <span
                  key={mod}
                  className="px-3 py-1.5 rounded-full bg-navy-800/50 border border-navy-700/50 text-xs text-navy-300 font-medium"
                >
                  {ANALYSIS_MODULE_LABELS[mod as AnalysisModule] ?? mod}
                </span>
              ))}
            </div>
          )}

          <button
            onClick={onUpgrade}
            className="inline-flex items-center gap-2 px-6 py-2.5 rounded-lg bg-ocean-700 hover:bg-ocean-600 text-white text-sm font-semibold transition-colors duration-200"
          >
            Upgrade
            <ArrowRight className="w-4 h-4" />
          </button>
        </div>
      </div>
    </div>
  )
}
