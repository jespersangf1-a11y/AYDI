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
  const cfg = CONFIDENCE_CONFIG[confidence] ?? {
    label: confidence,
    color: 'gray',
    icon: HelpCircle,
  }
  const colors = COLOR_CLASSES[cfg.color] ?? COLOR_CLASSES.gray
  const Icon = cfg.icon
  const iconSize = size === 'sm' ? 'w-3 h-3' : 'w-3.5 h-3.5'
  const textSize = size === 'sm' ? 'text-xs' : 'text-xs'
  const padding = size === 'sm' ? 'px-2 py-1' : 'px-2.5 py-1'

  return (
    <span
      className={`inline-flex items-center gap-1.5 rounded-full font-medium border ${colors.bg} ${colors.text} ${textSize} ${padding} ${colors.border}`}
    >
      <Icon className={iconSize} />
      {showLabel && cfg.label}
    </span>
  )
}
