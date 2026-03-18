import { AlertTriangle, AlertCircle, Info } from 'lucide-react'
import type { WarningData } from '../../types'

interface WarningListProps {
  warnings: WarningData[]
}

const SEVERITY_CONFIG = {
  critical: { icon: AlertCircle, bg: 'bg-red-900/30', border: 'border-red-800', text: 'text-red-300', label: 'Kritisch' },
  warning: { icon: AlertTriangle, bg: 'bg-amber-900/30', border: 'border-amber-800', text: 'text-amber-300', label: 'Warnung' },
  info: { icon: Info, bg: 'bg-ocean-900/30', border: 'border-ocean-800', text: 'text-ocean-300', label: 'Info' },
}

export default function WarningList({ warnings }: WarningListProps) {
  if (warnings.length === 0) {
    return <p className="text-navy-400 text-sm">Keine Warnungen</p>
  }

  return (
    <div className="space-y-2">
      {warnings.map((w, i) => {
        const config = SEVERITY_CONFIG[w.severity] || SEVERITY_CONFIG.info
        const Icon = config.icon
        return (
          <div key={i} className={`${config.bg} border ${config.border} rounded-lg p-3`}>
            <div className="flex items-start gap-2">
              <Icon className={`w-4 h-4 mt-0.5 ${config.text}`} />
              <div className="flex-1">
                <p className={`text-sm ${config.text}`}>{w.message}</p>
                <p className="text-xs text-navy-400 mt-1">{w.suggestion}</p>
              </div>
            </div>
          </div>
        )
      })}
    </div>
  )
}
