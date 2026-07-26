import { useRef, useState } from 'react'
import type { ZoneData, PassageData } from '../../types'
import type { CollabCursor, CollabUser } from '../../hooks/useCollaboration'

interface LayoutViewerProps {
  zones: ZoneData[]
  passages: PassageData[]
  /** Live collaboration (pillar 4, stage 2) — all optional, viewer stays
      fully functional without a session. */
  remoteCursors?: CollabCursor[]
  remoteSelections?: Record<string, CollabUser[]>
  onCursorMove?: (xMm: number, yMm: number) => void
  onZoneSelect?: (zoneName: string | null) => void
}

/** Stable per-user cursor color from the user id. */
const CURSOR_COLORS = ['#0ea5e9', '#f59e0b', '#10b981', '#ec4899', '#8b5cf6', '#ef4444']
function cursorColor(userId: string): string {
  let hash = 0
  for (let i = 0; i < userId.length; i++) hash = (hash * 31 + userId.charCodeAt(i)) | 0
  return CURSOR_COLORS[Math.abs(hash) % CURSOR_COLORS.length]
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

export default function LayoutViewer({
  zones,
  passages,
  remoteCursors,
  remoteSelections,
  onCursorMove,
  onZoneSelect,
}: LayoutViewerProps) {
  const [hoveredZone, setHoveredZone] = useState<string | null>(null)
  const [selectedZone, setSelectedZone] = useState<string | null>(null)
  const svgRef = useRef<SVGSVGElement | null>(null)

  /** Client coords → layout mm coords via the SVG's transform matrix. */
  const toLayoutCoords = (clientX: number, clientY: number): [number, number] | null => {
    const svg = svgRef.current
    if (!svg) return null
    const ctm = svg.getScreenCTM()
    if (!ctm) return null
    const point = new DOMPoint(clientX, clientY).matrixTransform(ctm.inverse())
    return [point.x, point.y]
  }

  if (zones.length === 0) {
    return <div className="text-navy-600 text-sm">Kein Layout vorhanden</div>
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
    <div className="relative card-premium p-6 overflow-hidden">
      <svg
        ref={svgRef}
        viewBox={viewBox}
        className="w-full h-auto"
        style={{ maxHeight: '500px' }}
        onPointerMove={
          onCursorMove
            ? (e) => {
                const pt = toLayoutCoords(e.clientX, e.clientY)
                if (pt) onCursorMove(pt[0], pt[1])
              }
            : undefined
        }
      >
        {/* Zones */}
        {zones.map((zone) => {
          const points = zone.polygon.map((p) => p.join(',')).join(' ')
          const color = ZONE_COLORS[zone.zone_type] || '#6b7280'
          const [cx, cy] = centroid(zone.polygon)
          const isHovered = hoveredZone === zone.name
          const remoteUsers = remoteSelections?.[zone.name] ?? []
          const isRemoteSelected = remoteUsers.length > 0
          const isLocalSelected = onZoneSelect != null && selectedZone === zone.name
          return (
            <g key={zone.name}>
              <polygon
                points={points}
                fill={color}
                fillOpacity={isHovered || isLocalSelected ? 0.3 : 0.15}
                stroke={isRemoteSelected ? cursorColor(remoteUsers[0].user_id) : color}
                strokeWidth={isHovered || isLocalSelected || isRemoteSelected ? 2.5 : 1}
                strokeDasharray={isRemoteSelected ? '60,30' : undefined}
                onMouseEnter={() => setHoveredZone(zone.name)}
                onMouseLeave={() => setHoveredZone(null)}
                onClick={
                  onZoneSelect
                    ? () => {
                        const next = selectedZone === zone.name ? null : zone.name
                        setSelectedZone(next)
                        onZoneSelect(next)
                      }
                    : undefined
                }
                className="cursor-pointer transition-all duration-200"
              />
              <text
                x={cx}
                y={cy}
                textAnchor="middle"
                dominantBaseline="middle"
                fill="white"
                fontSize={Math.max(100, (maxX - minX) / 30)}
                opacity="0.8"
                className="pointer-events-none select-none font-sans"
              >
                {zone.name}
              </text>
              {isRemoteSelected && (
                <text
                  x={cx}
                  y={cy + Math.max(140, (maxX - minX) / 22)}
                  textAnchor="middle"
                  fill={cursorColor(remoteUsers[0].user_id)}
                  fontSize={Math.max(80, (maxX - minX) / 40)}
                  className="pointer-events-none select-none font-sans"
                >
                  {remoteUsers.map((u) => u.name).join(', ')}
                </text>
              )}
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
              stroke="#4a6fa8"
              strokeWidth={Math.max(1.5, p.width_mm / 120)}
              strokeDasharray={p.is_primary ? 'none' : '8,4'}
              opacity="0.4"
              className="transition-all duration-200"
            />
          )
        })}

        {/* Remote cursors (live collaboration) */}
        {remoteCursors?.map((cursor) => {
          const color = cursorColor(cursor.user.user_id)
          const r = Math.max(60, (maxX - minX) / 60)
          return (
            <g key={cursor.user.user_id} className="pointer-events-none">
              <circle cx={cursor.x} cy={cursor.y} r={r} fill={color} fillOpacity={0.85} />
              <circle cx={cursor.x} cy={cursor.y} r={r * 1.8} fill="none" stroke={color} strokeWidth={r / 4} strokeOpacity={0.4} />
              <text
                x={cursor.x + r * 2.2}
                y={cursor.y + r * 0.6}
                fill={color}
                fontSize={Math.max(90, (maxX - minX) / 36)}
                className="select-none font-sans"
              >
                {cursor.user.name}
              </text>
            </g>
          )
        })}
      </svg>

      {/* Tooltip */}
      {hoveredZone && (() => {
        const zone = zones.find((z) => z.name === hoveredZone)
        if (!zone) return null
        const area = polygonArea(zone.polygon)
        return (
          <div className="absolute top-6 right-6 card-premium p-4 text-sm backdrop-blur-md">
            <p className="font-sans font-semibold text-navy-900">{zone.name}</p>
            <p className="text-navy-600 text-xs mt-1">Typ: {zone.zone_type}</p>
            <p className="text-navy-600 font-mono text-xs mt-1">Fläche: {area.toFixed(1)}m²</p>
          </div>
        )
      })()}
    </div>
  )
}
