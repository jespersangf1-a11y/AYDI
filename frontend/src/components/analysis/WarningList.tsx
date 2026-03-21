import { AlertTriangle, AlertCircle, Info } from 'lucide-react'
import type { WarningData } from '../../types'

interface WarningListProps {
  warnings: WarningData[]
}

const SEVERITY_CONFIG = {
  critical: { icon: AlertCircle, bg: 'bg-navy-900/30', leftBorder: 'border-l-2 border-l-red-400', text: 'text-red-300', label: 'Kritisch' },
  warning: { icon: AlertTriangle, bg: 'bg-navy-900/30', leftBorder: 'border-l-2 border-l-amber-400', text: 'text-amber-300', label: 'Warnung' },
  info: { icon: Info, bg: 'bg-navy-900/30', leftBorder: 'border-l-2 border-l-ocean-400', text: 'text-ocean-300', label: 'Info' },
}

export default function WarningList({ warnings }: WarningListProps) {
  if (warnings.length === 0) {
    return <p className="text-navy-400 text-xs font-sans font-semibold uppercase tracking-wider-premium">Keine Warnungen</p>
  }

  return (
    <div className="space-y-3">
      {warnings.map((w, i) => {
        const config = SEVERITY_CONFIG[w.severity] || SEVERITY_CONFIG.info
        const Icon = config.icon
        return (
          <div key={i} className={`${config.bg} border border-navy-700/40 ${config.leftBorder} rounded-lg p-4 backdrop-blur-sm`}>
            <div className="flex items-start gap-3">
              <Icon className={`w-4 h-4 mt-0.5 flex-shrink-0 ${config.text}`} />
              <div className="flex-1 min-w-0">
                <p className={`text-sm font-medium ${config.text}`}>{w.message}</p>
                <p className="text-xs text-navy-400 mt-1.5">{w.suggestion}</p>
              </div>
            </div>
          </div>
        )
      })}
    </div>
  )
}
