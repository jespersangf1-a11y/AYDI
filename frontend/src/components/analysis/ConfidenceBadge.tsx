import { useState, useEffect } from 'react'
import {
  CheckCircle,
  AlertCircle,
  AlertTriangle,
  XCircle,
  Eye,
  EyeOff,
  HelpCircle,
  BarChart,
  FileText,
  AlertOctagon,
} from 'lucide-react'

interface ConfidenceBadgeProps {
  confidence: string
  showLabel?: boolean
  size?: 'sm' | 'md'
}

const CONFIDENCE_CONFIG: Record<string, { label: string; color: string; icon: typeof CheckCircle; tooltip: string }> = {
  // Measured/calculated (green)
  measured: { label: 'Gemessen', color: 'green', icon: CheckCircle, tooltip: 'Wert wurde direkt gemessen.' },
  calculated: { label: 'Berechnet', color: 'green', icon: CheckCircle, tooltip: 'Wert wurde aus Messdaten berechnet.' },
  // Visual (blue/amber/red/gray)
  high: { label: 'Hohe Sicherheit', color: 'green', icon: CheckCircle, tooltip: 'Hohe Zuverlässigkeit der Analyse.' },
  visual_high: { label: 'Visuell (hoch)', color: 'blue', icon: Eye, tooltip: 'Visuelle Bewertung mit hoher Zuverlässigkeit.' },
  medium: { label: 'Mittlere Sicherheit', color: 'amber', icon: AlertCircle, tooltip: 'Mittlere Zuverlässigkeit der Analyse.' },
  visual_medium: { label: 'Visuell (mittel)', color: 'amber', icon: Eye, tooltip: 'Visuelle Bewertung mit mittlerer Zuverlässigkeit.' },
  low: { label: 'Niedrige Sicherheit', color: 'red', icon: AlertTriangle, tooltip: 'Niedrige Zuverlässigkeit der Analyse.' },
  visual_low: { label: 'Visuell (niedrig)', color: 'red', icon: EyeOff, tooltip: 'Visuelle Bewertung mit niedriger Zuverlässigkeit.' },
  insufficient: { label: 'Nicht auswertbar', color: 'gray', icon: XCircle, tooltip: 'Nicht genug Daten für eine zuverlässige Analyse.' },
  visual_insufficient: { label: 'Nicht auswertbar', color: 'gray', icon: XCircle, tooltip: 'Nicht genug visuellen Daten verfügbar.' },
  // Other
  estimated: { label: 'Geschaetzt', color: 'gray', icon: HelpCircle, tooltip: 'Wert wurde geschaetzt.' },
  benchmark: { label: 'Benchmark', color: 'gray', icon: BarChart, tooltip: 'Wert basiert auf Benchmark-Daten.' },
  documented: { label: 'Dokumentiert', color: 'blue', icon: FileText, tooltip: 'Wert aus Dokumentation.' },
  discrepant: { label: 'Abweichung', color: 'orange', icon: AlertOctagon, tooltip: 'Widerspruch in den Daten erkannt.' },
  'measured+visual': { label: 'Gemessen + Visuell', color: 'green', icon: CheckCircle, tooltip: 'Kombiniert Messung und visuelle Analyse.' },
  visual_only: { label: 'Nur visuell', color: 'amber', icon: Eye, tooltip: 'Ausschliesslich visuelle Bewertung.' },
}

const COLOR_CLASSES: Record<string, { bg: string; text: string; border: string }> = {
  green: { bg: 'bg-emerald-900/20', text: 'text-emerald-300', border: 'border-emerald-700/40' },
  blue: { bg: 'bg-ocean-900/20', text: 'text-ocean-300', border: 'border-ocean-700/40' },
  amber: { bg: 'bg-amber-900/20', text: 'text-amber-300', border: 'border-amber-700/40' },
  red: { bg: 'bg-red-900/20', text: 'text-red-300', border: 'border-red-700/40' },
  gray: { bg: 'bg-navy-800/40', text: 'text-navy-300', border: 'border-navy-700/40' },
  orange: { bg: 'bg-orange-900/20', text: 'text-orange-300', border: 'border-orange-700/40' },
}

export default function ConfidenceBadge({
  confidence,
  showLabel = true,
  size = 'md',
}: ConfidenceBadgeProps) {
  const [showTooltip, setShowTooltip] = useState(false)
  const [hasAnimated, setHasAnimated] = useState(false)

  useEffect(() => {
    setHasAnimated(true)
  }, [])

  const cfg = CONFIDENCE_CONFIG[confidence] ?? {
    label: confidence,
    color: 'gray',
    icon: HelpCircle,
    tooltip: 'Vertrauensniveau für diese Analyse.',
  }

  const colors = COLOR_CLASSES[cfg.color] ?? COLOR_CLASSES.gray
  const Icon = cfg.icon
  const iconSize = size === 'sm' ? 'w-3 h-3' : 'w-3.5 h-3.5'
  const textSize = size === 'sm' ? 'text-xs' : 'text-xs'
  const padding = size === 'sm' ? 'px-2 py-1' : 'px-2.5 py-1'

  // Pulse animation for low confidence
  const isPulsing = confidence.includes('low')

  return (
    <div className="relative inline-block">
      <span
        className={`inline-flex items-center gap-1.5 rounded-full font-medium border ${colors.bg} ${colors.text} ${textSize} ${padding} ${colors.border} transition-all duration-300 ${
          isPulsing && hasAnimated ? 'animate-pulse' : ''
        } ${hasAnimated ? 'animate-fadeInScale' : 'opacity-0'}`}
        onMouseEnter={() => setShowTooltip(true)}
        onMouseLeave={() => setShowTooltip(false)}
      >
        <Icon className={iconSize} />
        {showLabel && cfg.label}
      </span>

      {showTooltip && (
        <div className="absolute bottom-full left-1/2 transform -translate-x-1/2 mb-2 px-2.5 py-1.5 bg-navy-900 text-navy-100 text-xs rounded whitespace-nowrap z-20 border border-navy-700 shadow-lg animate-fadeInScale">
          {cfg.tooltip}
        </div>
      )}

      <style>{`
        @keyframes fadeInScale {
          from {
            opacity: 0;
            transform: scale(0.95);
          }
          to {
            opacity: 1;
            transform: scale(1);
          }
        }

        .animate-fadeInScale {
          animation: fadeInScale 0.3s ease-out;
        }
      `}</style>
    </div>
  )
}
