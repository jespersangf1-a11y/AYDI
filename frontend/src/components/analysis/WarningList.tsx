import { useState } from 'react'
import { AlertTriangle, AlertCircle, Info, ChevronDown } from 'lucide-react'
import type { WarningData } from '../../types'

interface WarningListProps {
  warnings: WarningData[]
}

const SEVERITY_CONFIG = {
  critical: { icon: AlertTriangle, bg: 'bg-navy-900/30', leftBorder: 'border-l-2 border-l-red-400', text: 'text-red-300', label: 'Kritisch' },
  warning: { icon: AlertCircle, bg: 'bg-navy-900/30', leftBorder: 'border-l-2 border-l-amber-400', text: 'text-amber-300', label: 'Warnung' },
  info: { icon: Info, bg: 'bg-navy-900/30', leftBorder: 'border-l-2 border-l-ocean-400', text: 'text-ocean-600', label: 'Info' },
}

interface WarningCardProps {
  warning: WarningData
  index: number
}

function WarningCard({ warning, index }: WarningCardProps) {
  const [isExpanded, setIsExpanded] = useState(false)
  const config = SEVERITY_CONFIG[warning.severity] || SEVERITY_CONFIG.info
  const Icon = config.icon

  return (
    <div
      className={`${config.bg} border border-sand-200 ${config.leftBorder} rounded-lg backdrop-blur-sm transition-all duration-200 hover:shadow-lg hover:shadow-navy-900/20 hover:-translate-y-0.5 overflow-hidden animate-slide-in-right stagger-${Math.min(index + 1, 8)}`}
    >
      <button
        onClick={() => setIsExpanded(!isExpanded)}
        className="w-full p-4 text-left"
      >
        <div className="flex items-start gap-3">
          <Icon className={`w-4 h-4 mt-0.5 flex-shrink-0 ${config.text}`} />
          <div className="flex-1 min-w-0">
            <p className={`text-sm font-medium ${config.text}`}>{warning.message}</p>
            {!isExpanded && (
              <p className="text-xs text-navy-600 mt-1.5 line-clamp-1">{warning.suggestion}</p>
            )}
          </div>
          <ChevronDown
            className={`w-4 h-4 mt-0.5 flex-shrink-0 text-navy-500 transition-transform duration-200 ${
              isExpanded ? 'transform rotate-180' : ''
            }`}
          />
        </div>
      </button>

      {isExpanded && (
        <div className="px-4 pb-4 border-t border-navy-700/20 animate-slide-down">
          <p className="text-xs text-navy-700 leading-relaxed">{warning.suggestion}</p>
        </div>
      )}
    </div>
  )
}

export default function WarningList({ warnings }: WarningListProps) {
  if (warnings.length === 0) {
    return (
      <p className="text-navy-600 text-xs font-sans font-semibold uppercase tracking-wider-premium">
        Keine Warnungen
      </p>
    )
  }

  return (
    <div className="space-y-3">
      {warnings.map((w, i) => (
        <WarningCard key={i} warning={w} index={i} />
      ))}

    </div>
  )
}
