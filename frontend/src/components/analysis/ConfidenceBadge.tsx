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

const CONFIDENCE_CONFIG: Record<string, { label: string; color: string; icon: typeof CheckCircle }> = {
  // Measured/calculated (green)
  measured: { label: 'Gemessen', color: 'green', icon: CheckCircle },
  calculated: { label: 'Berechnet', color: 'green', icon: CheckCircle },
  // Visual (blue/amber/red/gray)
  high: { label: 'Hohe Sicherheit', color: 'green', icon: CheckCircle },
  visual_high: { label: 'Visuell (hoch)', color: 'blue', icon: Eye },
  medium: { label: 'Mittlere Sicherheit', color: 'amber', icon: AlertCircle },
  visual_medium: { label: 'Visuell (mittel)', color: 'amber', icon: Eye },
  low: { label: 'Niedrige Sicherheit', color: 'red', icon: AlertTriangle },
  visual_low: { label: 'Visuell (niedrig)', color: 'red', icon: EyeOff },
  insufficient: { label: 'Nicht auswertbar', color: 'gray', icon: XCircle },
  visual_insufficient: { label: 'Nicht auswertbar', color: 'gray', icon: XCircle },
  // Other
  estimated: { label: 'Geschaetzt', color: 'gray', icon: HelpCircle },
  benchmark: { label: 'Benchmark', color: 'gray', icon: BarChart },
  documented: { label: 'Dokumentiert', color: 'blue', icon: FileText },
  discrepant: { label: 'Abweichung', color: 'orange', icon: AlertOctagon },
  'measured+visual': { label: 'Gemessen + Visuell', color: 'green', icon: CheckCircle },
  visual_only: { label: 'Nur visuell', color: 'amber', icon: Eye },
}

const COLOR_CLASSES: Record<string, { bg: string; text: string }> = {
  green: { bg: 'bg-emerald-900/30', text: 'text-emerald-300' },
  blue: { bg: 'bg-blue-900/30', text: 'text-blue-300' },
  amber: { bg: 'bg-amber-900/30', text: 'text-amber-300' },
  red: { bg: 'bg-red-900/30', text: 'text-red-300' },
  gray: { bg: 'bg-gray-800/50', text: 'text-gray-300' },
  orange: { bg: 'bg-amber-900/30', text: 'text-amber-300' },
}

export default function ConfidenceBadge({
  confidence,
  showLabel = true,
  size = 'md',
}: ConfidenceBadgeProps) {
  const cfg = CONFIDENCE_CONFIG[confidence] ?? {
    label: confidence,
    color: 'gray',
    icon: HelpCircle,
  }
  const colors = COLOR_CLASSES[cfg.color] ?? COLOR_CLASSES.gray
  const Icon = cfg.icon
  const iconSize = size === 'sm' ? 'w-3 h-3' : 'w-4 h-4'
  const textSize = size === 'sm' ? 'text-xs' : 'text-sm'
  const padding = size === 'sm' ? 'px-2 py-0.5' : 'px-3 py-1'

  return (
    <span
      className={`inline-flex items-center gap-1.5 rounded-full font-medium ${colors.bg} ${colors.text} ${textSize} ${padding}`}
    >
      <Icon className={iconSize} />
      {showLabel && cfg.label}
    </span>
  )
}
