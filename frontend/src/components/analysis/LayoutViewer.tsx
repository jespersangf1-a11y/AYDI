import { useState } from 'react'
import type { ZoneData, PassageData } from '../../types'

interface LayoutViewerProps {
  zones: ZoneData[]
  passages: PassageData[]
}

const ZONE_COLORS: Record<string, string> = {
  cabin: '#6366f1',
  pantry: '#f59e0b',
  helm: '#10b981',
  engine: '#ef4444',
  storage: '#8b5cf6',
  cockpit: '#06b6d4',
  salon: '#3b82f6',
  head: '#ec4899',
}

function centroid(polygon: number[][]): [number, number] {
  const n = polygon.length
  if (n === 0) return [0, 0]
  const x = polygon.reduce((s, p) => s + p[0], 0) / n
  const y = polygon.reduce((s, p) => s + p[1], 0) / n
  return [x, y]
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

export default function LayoutViewer({ zones, passages }: LayoutViewerProps) {
  const [hoveredZone, setHoveredZone] = useState<string | null>(null)

  if (zones.length === 0) {
    return <div className="text-navy-400 text-sm">Kein Layout vorhanden</div>
  }

  // Calculate bounding box
  const allPoints = zones.flatMap((z) => z.polygon)
  const minX = Math.min(...allPoints.map((p) => p[0]))
  const maxX = Math.max(...allPoints.map((p) => p[0]))
  const minY = Math.min(...allPoints.map((p) => p[1]))
  const maxY = Math.max(...allPoints.map((p) => p[1]))
  const padding = 200
  const viewBox = `${minX - padding} ${minY - padding} ${maxX - minX + padding * 2} ${maxY - minY + padding * 2}`

  // Build centroid map for passages
  const centroidMap = new Map<string, [number, number]>()
  zones.forEach((z) => centroidMap.set(z.name, centroid(z.polygon)))

  return (
    <div className="relative bg-navy-900 rounded-xl border border-navy-700 p-4">
      <svg viewBox={viewBox} className="w-full h-auto" style={{ maxHeight: '500px' }}>
        {/* Zones */}
        {zones.map((zone) => {
          const points = zone.polygon.map((p) => p.join(',')).join(' ')
          const color = ZONE_COLORS[zone.zone_type] || '#6b7280'
          const [cx, cy] = centroid(zone.polygon)
          const isHovered = hoveredZone === zone.name
          return (
            <g key={zone.name}>
              <polygon
                points={points}
                fill={color}
                fillOpacity={isHovered ? 0.4 : 0.2}
                stroke={color}
                strokeWidth={isHovered ? 3 : 1.5}
                onMouseEnter={() => setHoveredZone(zone.name)}
                onMouseLeave={() => setHoveredZone(null)}
                className="cursor-pointer transition-all"
              />
              <text
                x={cx}
                y={cy}
                textAnchor="middle"
                dominantBaseline="middle"
                fill="white"
                fontSize={Math.max(100, (maxX - minX) / 30)}
                className="pointer-events-none select-none"
              >
                {zone.name}
              </text>
            </g>
          )
        })}

        {/* Passages */}
        {passages.map((p, i) => {
          const from = centroidMap.get(p.from_zone)
          const to = centroidMap.get(p.to_zone)
          if (!from || !to) return null
          return (
            <line
              key={i}
              x1={from[0]}
              y1={from[1]}
              x2={to[0]}
              y2={to[1]}
              stroke="#94a3b8"
              strokeWidth={Math.max(2, p.width_mm / 100)}
              strokeDasharray={p.is_primary ? 'none' : '10,5'}
              opacity={0.5}
            />
          )
        })}
      </svg>

      {/* Tooltip */}
      {hoveredZone && (() => {
        const zone = zones.find((z) => z.name === hoveredZone)
        if (!zone) return null
        const area = polygonArea(zone.polygon)
        return (
          <div className="absolute top-4 right-4 bg-navy-800 border border-navy-600 rounded-lg p-3 text-sm">
            <p className="font-medium text-white">{zone.name}</p>
            <p className="text-navy-400">Typ: {zone.zone_type}</p>
            <p className="text-navy-400 font-mono">Fläche: {area.toFixed(1)}m²</p>
          </div>
        )
      })()}
    </div>
  )
}
