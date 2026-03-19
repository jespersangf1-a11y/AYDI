import { AlertTriangle, AlertCircle, Info, X } from 'lucide-react'
import type { ZoneData, WarningData } from '../../types'
import { ZONE_TYPE_LABELS, ZONE_COLORS, DEFAULT_ZONE_COLOR } from './zoneColors'

interface ViewerInfoPanelProps {
  zone: ZoneData | null
  warnings: WarningData[]
  onClose: () => void
}

function polygonArea(polygon: number[][]): number {
  const n = polygon.length
  let area = 0
  for (let i = 0; i < n; i++) {
    const j = (i + 1) % n
    area += polygon[i][0] * polygon[j][1]
    area -= polygon[j][0] * polygon[i][1]
  }
  return Math.abs(area) / 2 / 1_000_000
}

function SeverityIcon({ severity }: { severity: string }) {
  if (severity === 'critical')
    return <AlertCircle className="w-4 h-4 text-red-400 flex-shrink-0" />
  if (severity === 'warning')
    return <AlertTriangle className="w-4 h-4 text-amber-400 flex-shrink-0" />
  return <Info className="w-4 h-4 text-ocean-400 flex-shrink-0" />
}

export default function ViewerInfoPanel({
  zone,
  warnings,
  onClose,
}: ViewerInfoPanelProps) {
  if (!zone) return null

  const typeLabel = ZONE_TYPE_LABELS[zone.zone_type] ?? zone.zone_type
  const area = polygonArea(zone.polygon)
  const color = ZONE_COLORS[zone.zone_type] ?? DEFAULT_ZONE_COLOR

  // Filter warnings relevant to this zone
  const zoneWarnings = warnings.filter((w) => {
    const loc = w.location?.toLowerCase() ?? ''
    const name = zone.name.toLowerCase()
    return loc.includes(name)
  })

  return (
    <div className="absolute top-3 right-3 z-10 w-64 bg-navy-800/95 backdrop-blur-sm border border-navy-600 rounded-lg overflow-hidden">
      {/* Header */}
      <div className="flex items-center justify-between p-3 border-b border-navy-700">
        <div className="flex items-center gap-2">
          <div
            className="w-3 h-3 rounded-sm"
            style={{ backgroundColor: color }}
          />
          <h3 className="text-sm font-heading font-semibold text-white">
            {zone.name}
          </h3>
        </div>
        <button
          onClick={onClose}
          className="text-navy-400 hover:text-white transition-colors"
          title="Schlie\u00dfen"
        >
          <X className="w-4 h-4" />
        </button>
      </div>

      {/* Details */}
      <div className="p-3 space-y-2 text-xs">
        <DetailRow label="Typ" value={typeLabel} />
        <DetailRow label="Fl\u00e4che" value={`${area.toFixed(1)} m\u00b2`} mono />
        {zone.height_mm != null && (
          <DetailRow
            label="H\u00f6he"
            value={`${zone.height_mm.toFixed(0)} mm`}
            mono
          />
        )}
        <DetailRow
          label="Bereich"
          value={
            zone.is_crew_area
              ? 'Crew'
              : zone.is_guest_area
                ? 'Gast'
                : 'Allgemein'
          }
        />
      </div>

      {/* Warnings */}
      {zoneWarnings.length > 0 && (
        <div className="border-t border-navy-700 p-3">
          <p className="text-xs font-heading font-medium text-navy-300 mb-2">
            Warnungen ({zoneWarnings.length})
          </p>
          <div className="space-y-2">
            {zoneWarnings.map((w, i) => (
              <div
                key={i}
                className="flex gap-2 text-xs"
              >
                <SeverityIcon severity={w.severity} />
                <div>
                  <p className="text-white">{w.message}</p>
                  {w.suggestion && (
                    <p className="text-navy-400 mt-0.5">{w.suggestion}</p>
                  )}
                </div>
              </div>
            ))}
          </div>
        </div>
      )}
    </div>
  )
}

function DetailRow({
  label,
  value,
  mono,
}: {
  label: string
  value: string
  mono?: boolean
}) {
  return (
    <div className="flex justify-between">
      <span className="text-navy-400">{label}</span>
      <span className={`text-white ${mono ? 'font-mono' : ''}`}>{value}</span>
    </div>
  )
}
