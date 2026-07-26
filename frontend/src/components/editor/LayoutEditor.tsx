import { useEffect, useMemo, useRef, useState } from 'react'
import { Check, Loader2, Plus, Trash2, X } from 'lucide-react'
import type { PassageData, ZoneData } from '../../types'

interface LayoutEditorProps {
  zones: ZoneData[]
  passages: PassageData[]
  saving: boolean
  onSave: (
    zones: ZoneData[],
    passages: PassageData[],
    changeSummary: string,
    zoneRenames: Record<string, string>,
  ) => void
  onCancel: () => void
  onDirtyChange?: (dirty: boolean) => void
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

const ZONE_TYPE_OPTIONS: { value: string; label: string }[] = [
  { value: 'cabin', label: 'Kabine' },
  { value: 'salon', label: 'Salon' },
  { value: 'pantry', label: 'Pantry' },
  { value: 'head', label: 'Nasszelle' },
  { value: 'engine', label: 'Motorraum' },
  { value: 'storage', label: 'Stauraum' },
  { value: 'cockpit', label: 'Cockpit' },
  { value: 'helm', label: 'Steuerstand' },
  { value: 'foredeck', label: 'Vordeck' },
  { value: 'flybridge', label: 'Flybridge' },
  { value: 'crew_quarters', label: 'Crew-Bereich' },
]

const GRID_MM = 50

/**
 * Passages reference zones BY NAME in the data model. During an edit
 * session names are volatile (typed character by character), so we resolve
 * them to zone INDICES on mount and only map back to names on save —
 * per-keystroke name matching corrupted foreign passages on transient
 * name collisions.
 */
interface EditorPassage {
  data: PassageData
  fromIdx: number // -1 = unresolved (keeps its original names on save)
  toIdx: number
}

type DragState =
  | { kind: 'vertex'; zoneIdx: number; vertexIdx: number }
  | {
      kind: 'body'
      zoneIdx: number
      startX: number
      startY: number
      origPolygon: number[][]
    }

function snap(value: number): number {
  return Math.round(value / GRID_MM) * GRID_MM
}

function centroid(polygon: number[][]): [number, number] {
  const n = polygon.length
  if (n === 0) return [0, 0]
  return [
    polygon.reduce((s, p) => s + p[0], 0) / n,
    polygon.reduce((s, p) => s + p[1], 0) / n,
  ]
}

function clonePolygon(polygon: number[][]): number[][] {
  return polygon.map((p) => [p[0], p[1]])
}

/**
 * Pillar 3 MVP zone editor: drag vertices, move zones, insert/remove points,
 * rename (passages + server-side zone_name references follow), delete, add
 * rectangular zones. Saving goes through PATCH /layouts — the backend
 * auto-snapshots the previous state, so every edit stays reversible.
 */
export default function LayoutEditor({
  zones: initialZones,
  passages: initialPassages,
  saving,
  onSave,
  onCancel,
  onDirtyChange,
}: LayoutEditorProps) {
  const [zones, setZones] = useState<ZoneData[]>(() =>
    initialZones.map((z) => ({ ...z, polygon: clonePolygon(z.polygon) })),
  )
  // Original name per zone entry (null = zone added in this session).
  // Drives the zone_renames cascade so materials/structural/cost references
  // follow a rename instead of being orphaned.
  const [originalNames, setOriginalNames] = useState<(string | null)[]>(() =>
    initialZones.map((z) => z.name),
  )
  const [passages, setPassages] = useState<EditorPassage[]>(() =>
    initialPassages.map((p) => ({
      data: { ...p },
      fromIdx: initialZones.findIndex((z) => z.name === p.from_zone),
      toIdx: initialZones.findIndex((z) => z.name === p.to_zone),
    })),
  )
  const [selectedIdx, setSelectedIdx] = useState<number | null>(null)
  const [drag, setDrag] = useState<DragState | null>(null)
  const [changeSummary, setChangeSummary] = useState('')
  const [error, setError] = useState<string | null>(null)
  const [dirty, setDirty] = useState(false)
  const svgRef = useRef<SVGSVGElement>(null)

  const markDirty = () => {
    setDirty(true)
    onDirtyChange?.(true)
  }

  // Unsaved changes must not vanish silently on window close/reload
  useEffect(() => {
    if (!dirty) return
    const handler = (e: BeforeUnloadEvent) => {
      e.preventDefault()
    }
    window.addEventListener('beforeunload', handler)
    return () => window.removeEventListener('beforeunload', handler)
  }, [dirty])

  useEffect(() => () => onDirtyChange?.(false), [onDirtyChange])

  // Frozen view frame (initial bounds + generous margin) so dragging a zone
  // outward does not make the whole canvas jump under the cursor.
  const viewBox = useMemo(() => {
    const points = initialZones.flatMap((z) => z.polygon)
    if (points.length === 0) return '-1000 -1000 12000 6000'
    const minX = Math.min(...points.map((p) => p[0]))
    const maxX = Math.max(...points.map((p) => p[0]))
    const minY = Math.min(...points.map((p) => p[1]))
    const maxY = Math.max(...points.map((p) => p[1]))
    const pad = Math.max(1000, (maxX - minX) * 0.15)
    return `${minX - pad} ${minY - pad} ${maxX - minX + pad * 2} ${maxY - minY + pad * 2}`
    // eslint-disable-next-line react-hooks/exhaustive-deps
  }, [])

  const vertexRadius = useMemo(() => {
    const parts = viewBox.split(' ').map(Number)
    return Math.max(60, parts[2] / 90)
  }, [viewBox])

  const toSvgPoint = (e: React.PointerEvent): [number, number] | null => {
    const svg = svgRef.current
    if (!svg) return null
    const ctm = svg.getScreenCTM()
    if (!ctm) return null
    const point = new DOMPoint(e.clientX, e.clientY).matrixTransform(ctm.inverse())
    return [point.x, point.y]
  }

  const capturePointer = (e: React.PointerEvent) => {
    // Capture on the SVG: move/up keep arriving even when the cursor leaves
    // the element — without this, drags died at the canvas edge.
    try {
      svgRef.current?.setPointerCapture(e.pointerId)
    } catch {
      /* capture is progressive enhancement */
    }
  }

  const updateZonePolygon = (zoneIdx: number, polygon: number[][]) => {
    setZones((prev) =>
      prev.map((z, i) => (i === zoneIdx ? { ...z, polygon } : z)),
    )
    markDirty()
  }

  // ── Pointer interaction ──
  const handleVertexDown = (e: React.PointerEvent, zoneIdx: number, vertexIdx: number) => {
    e.stopPropagation()
    if (e.altKey) {
      const polygon = zones[zoneIdx].polygon
      if (polygon.length <= 3) {
        setError('Ein Polygon braucht mindestens 3 Punkte.')
        return
      }
      updateZonePolygon(
        zoneIdx,
        polygon.filter((_, i) => i !== vertexIdx),
      )
      return
    }
    capturePointer(e)
    setSelectedIdx(zoneIdx)
    setDrag({ kind: 'vertex', zoneIdx, vertexIdx })
  }

  const handleMidpointDown = (e: React.PointerEvent, zoneIdx: number, edgeIdx: number) => {
    e.stopPropagation()
    capturePointer(e)
    const polygon = zones[zoneIdx].polygon
    const a = polygon[edgeIdx]
    const b = polygon[(edgeIdx + 1) % polygon.length]
    const mid: number[] = [snap((a[0] + b[0]) / 2), snap((a[1] + b[1]) / 2)]
    const next = clonePolygon(polygon)
    next.splice(edgeIdx + 1, 0, mid)
    updateZonePolygon(zoneIdx, next)
    setSelectedIdx(zoneIdx)
    setDrag({ kind: 'vertex', zoneIdx, vertexIdx: edgeIdx + 1 })
  }

  const handleZoneDown = (e: React.PointerEvent, zoneIdx: number) => {
    const svgPoint = toSvgPoint(e)
    if (!svgPoint) return
    capturePointer(e)
    setSelectedIdx(zoneIdx)
    setDrag({
      kind: 'body',
      zoneIdx,
      startX: svgPoint[0],
      startY: svgPoint[1],
      origPolygon: clonePolygon(zones[zoneIdx].polygon),
    })
  }

  const handlePointerMove = (e: React.PointerEvent) => {
    if (!drag) return
    // A mouse with no button pressed means we missed the up event
    // (e.g. pointercancel) — never let the zone "stick" to the cursor.
    if (e.pointerType === 'mouse' && e.buttons === 0) {
      setDrag(null)
      return
    }
    const svgPoint = toSvgPoint(e)
    if (!svgPoint) return
    if (drag.kind === 'vertex') {
      const polygon = clonePolygon(zones[drag.zoneIdx].polygon)
      polygon[drag.vertexIdx] = [snap(svgPoint[0]), snap(svgPoint[1])]
      updateZonePolygon(drag.zoneIdx, polygon)
    } else {
      const dx = snap(svgPoint[0] - drag.startX)
      const dy = snap(svgPoint[1] - drag.startY)
      updateZonePolygon(
        drag.zoneIdx,
        drag.origPolygon.map((p) => [p[0] + dx, p[1] + dy]),
      )
    }
  }

  const handlePointerUp = () => setDrag(null)

  // ── Zone operations ──
  const handleRename = (newName: string) => {
    if (selectedIdx == null) return
    setZones((prev) =>
      prev.map((z, i) => (i === selectedIdx ? { ...z, name: newName } : z)),
    )
    markDirty()
    // Passages track zones by index — nothing else to rewrite here.
  }

  const handleTypeChange = (zoneType: string) => {
    if (selectedIdx == null) return
    setZones((prev) =>
      prev.map((z, i) => (i === selectedIdx ? { ...z, zone_type: zoneType } : z)),
    )
    markDirty()
  }

  const handleDeleteZone = () => {
    if (selectedIdx == null) return
    const zone = zones[selectedIdx]
    const affected = passages.filter(
      (p) => p.fromIdx === selectedIdx || p.toIdx === selectedIdx,
    ).length
    const hadOriginalName = originalNames[selectedIdx] != null
    const parts = [`Zone '${zone.name}' löschen?`]
    if (affected > 0) parts.push(`${affected} Durchgang/Durchgänge werden mit entfernt.`)
    if (hadOriginalName)
      parts.push(
        'Material-/Struktur-/Kostenzuweisungen dieser Zone verlieren ihre Referenz.',
      )
    if (!window.confirm(parts.join(' '))) return
    setZones((prev) => prev.filter((_, i) => i !== selectedIdx))
    setOriginalNames((prev) => prev.filter((_, i) => i !== selectedIdx))
    setPassages((prev) =>
      prev
        .filter((p) => p.fromIdx !== selectedIdx && p.toIdx !== selectedIdx)
        .map((p) => ({
          ...p,
          fromIdx: p.fromIdx > selectedIdx ? p.fromIdx - 1 : p.fromIdx,
          toIdx: p.toIdx > selectedIdx ? p.toIdx - 1 : p.toIdx,
        })),
    )
    setSelectedIdx(null)
    setDrag(null)
    markDirty()
  }

  const handleAddZone = () => {
    const parts = viewBox.split(' ').map(Number)
    const cx = snap(parts[0] + parts[2] / 2)
    const cy = snap(parts[1] + parts[3] / 2)
    const half = 1000
    let n = zones.length + 1
    let name = `Neue Zone ${n}`
    const names = new Set(zones.map((z) => z.name))
    while (names.has(name)) {
      n += 1
      name = `Neue Zone ${n}`
    }
    setZones((prev) => [
      ...prev,
      {
        name,
        zone_type: 'cabin',
        polygon: [
          [cx - half, cy - half],
          [cx + half, cy - half],
          [cx + half, cy + half],
          [cx - half, cy + half],
        ],
        is_crew_area: false,
        is_guest_area: false,
      },
    ])
    setOriginalNames((prev) => [...prev, null])
    setSelectedIdx(zones.length)
    markDirty()
  }

  const handleCancel = () => {
    if (dirty && !window.confirm('Ungespeicherte Änderungen verwerfen?')) return
    onDirtyChange?.(false)
    onCancel()
  }

  const handleSave = () => {
    const names = zones.map((z) => z.name.trim())
    if (names.some((n) => n === '')) {
      setError('Jede Zone braucht einen Namen.')
      return
    }
    if (new Set(names).size !== names.length) {
      setError('Zonennamen müssen eindeutig sein (Durchgänge referenzieren Namen).')
      return
    }
    if (zones.length === 0) {
      setError('Mindestens eine Zone behalten — ein leeres Layout ist nicht analysierbar.')
      return
    }
    if (zones.some((z) => z.polygon.length < 3)) {
      setError('Jedes Polygon braucht mindestens 3 Punkte.')
      return
    }
    setError(null)

    // Map index-based passages back to (now final) names
    const finalPassages: PassageData[] = passages.map((p) => ({
      ...p.data,
      from_zone: p.fromIdx >= 0 ? zones[p.fromIdx].name : p.data.from_zone,
      to_zone: p.toIdx >= 0 ? zones[p.toIdx].name : p.data.to_zone,
    }))

    // Renames for the server-side reference cascade
    const zoneRenames: Record<string, string> = {}
    zones.forEach((zone, i) => {
      const original = originalNames[i]
      if (original && original !== zone.name) zoneRenames[original] = zone.name
    })

    const deletedOriginals = initialZones
      .map((z) => z.name)
      .filter(
        (name) =>
          !originalNames.includes(name),
      )
    if (deletedOriginals.length > 0) {
      const proceed = window.confirm(
        `Gelöschte Zone(n): ${deletedOriginals.join(', ')}. ` +
          'Deren Material-/Struktur-/Kostenzuweisungen verlieren ihre Referenz. Speichern?',
      )
      if (!proceed) return
    }

    onDirtyChange?.(false)
    onSave(zones, finalPassages, changeSummary.trim(), zoneRenames)
  }

  const selected = selectedIdx != null ? zones[selectedIdx] : null

  return (
    <div className="space-y-4">
      {/* Toolbar */}
      <div className="card-premium px-6 py-4 flex flex-wrap items-center gap-4">
        <button
          onClick={handleAddZone}
          className="flex items-center gap-2 bg-sand-100 border border-sand-300 hover:bg-sand-200 text-navy-700 px-4 py-2 rounded-lg text-xs font-medium transition-all"
        >
          <Plus className="w-3.5 h-3.5" />
          Zone hinzufügen
        </button>

        {selected && (
          <>
            <div className="flex items-center gap-2">
              <label htmlFor="ed-name" className="label-premium">Name</label>
              <input
                id="ed-name"
                type="text"
                value={selected.name}
                maxLength={100}
                onChange={(e) => handleRename(e.target.value)}
                className="w-40 rounded-lg border border-sand-200 bg-white px-3 py-1.5 text-sm text-navy-900 focus:border-ocean-500 focus:outline-none"
              />
            </div>
            <div className="flex items-center gap-2">
              <label htmlFor="ed-type" className="label-premium">Typ</label>
              <select
                id="ed-type"
                value={selected.zone_type}
                onChange={(e) => handleTypeChange(e.target.value)}
                className="rounded-lg border border-sand-200 bg-white px-3 py-1.5 text-sm text-navy-900 focus:border-ocean-500 focus:outline-none"
              >
                {ZONE_TYPE_OPTIONS.map((option) => (
                  <option key={option.value} value={option.value}>
                    {option.label}
                  </option>
                ))}
                {!ZONE_TYPE_OPTIONS.some((o) => o.value === selected.zone_type) && (
                  <option value={selected.zone_type}>{selected.zone_type}</option>
                )}
              </select>
            </div>
            <button
              onClick={handleDeleteZone}
              className="flex items-center gap-1.5 text-xs text-red-600 hover:text-red-500 transition-colors"
            >
              <Trash2 className="w-3.5 h-3.5" />
              Zone löschen
            </button>
          </>
        )}

        <span className="text-xs text-navy-500 ml-auto">
          Eckpunkt ziehen · Fläche ziehen = verschieben · kleines Quadrat = Punkt
          einfügen · Alt+Klick = Punkt löschen · Raster {GRID_MM} mm
        </span>
      </div>

      {error && (
        <div className="card-premium bg-amber-950/20 border-amber-700/20 p-3 text-amber-300 text-sm">
          {error}
        </div>
      )}

      {/* Canvas */}
      <div className="card-premium p-2 overflow-hidden">
        <svg
          ref={svgRef}
          viewBox={viewBox}
          className="w-full h-auto touch-none"
          style={{ maxHeight: '540px', cursor: drag ? 'grabbing' : 'default' }}
          onPointerMove={handlePointerMove}
          onPointerUp={handlePointerUp}
          onPointerCancel={handlePointerUp}
        >
          {zones.map((zone, zoneIdx) => {
            const points = zone.polygon.map((p) => p.join(',')).join(' ')
            const color = ZONE_COLORS[zone.zone_type] || '#6b7280'
            const [cx, cy] = centroid(zone.polygon)
            const isSelected = selectedIdx === zoneIdx
            return (
              <g key={zoneIdx}>
                <polygon
                  points={points}
                  fill={color}
                  fillOpacity={isSelected ? 0.35 : 0.15}
                  stroke={color}
                  strokeWidth={isSelected ? vertexRadius / 3 : vertexRadius / 6}
                  onPointerDown={(e) => handleZoneDown(e, zoneIdx)}
                  style={{ cursor: 'move' }}
                />
                <text
                  x={cx}
                  y={cy}
                  textAnchor="middle"
                  dominantBaseline="middle"
                  fill="#1e293b"
                  fontSize={vertexRadius * 2.2}
                  className="pointer-events-none select-none font-sans"
                >
                  {zone.name}
                </text>

                {isSelected &&
                  zone.polygon.map((p, edgeIdx) => {
                    const next = zone.polygon[(edgeIdx + 1) % zone.polygon.length]
                    const mx = (p[0] + next[0]) / 2
                    const my = (p[1] + next[1]) / 2
                    return (
                      <rect
                        key={`m${edgeIdx}`}
                        x={mx - vertexRadius * 0.6}
                        y={my - vertexRadius * 0.6}
                        width={vertexRadius * 1.2}
                        height={vertexRadius * 1.2}
                        fill="white"
                        stroke={color}
                        strokeWidth={vertexRadius / 6}
                        onPointerDown={(e) => handleMidpointDown(e, zoneIdx, edgeIdx)}
                        style={{ cursor: 'copy' }}
                      />
                    )
                  })}

                {isSelected &&
                  zone.polygon.map((p, vertexIdx) => (
                    <circle
                      key={`v${vertexIdx}`}
                      cx={p[0]}
                      cy={p[1]}
                      r={vertexRadius}
                      fill={color}
                      stroke="white"
                      strokeWidth={vertexRadius / 4}
                      onPointerDown={(e) => handleVertexDown(e, zoneIdx, vertexIdx)}
                      style={{ cursor: 'grab' }}
                    />
                  ))}
              </g>
            )
          })}

          {/* Passages (read-only in the editor, tracked by zone index) */}
          {passages.map((p, i) => {
            const from = p.fromIdx >= 0 ? zones[p.fromIdx] : undefined
            const to = p.toIdx >= 0 ? zones[p.toIdx] : undefined
            if (!from || !to) return null
            const [x1, y1] = centroid(from.polygon)
            const [x2, y2] = centroid(to.polygon)
            return (
              <line
                key={`p${i}`}
                x1={x1}
                y1={y1}
                x2={x2}
                y2={y2}
                stroke="#4a6fa8"
                strokeWidth={vertexRadius / 4}
                strokeDasharray={p.data.is_primary ? 'none' : '8,4'}
                opacity="0.35"
                className="pointer-events-none"
              />
            )
          })}
        </svg>
      </div>

      {/* Footer: summary + save/cancel */}
      <div className="card-premium px-6 py-4 flex flex-wrap items-center gap-3">
        <input
          type="text"
          value={changeSummary}
          onChange={(e) => setChangeSummary(e.target.value)}
          placeholder="Änderungsbeschreibung (für die Versionshistorie)"
          maxLength={500}
          className="flex-1 min-w-[220px] rounded-lg border border-sand-200 bg-white px-3 py-2 text-sm text-navy-900 focus:border-ocean-500 focus:outline-none"
        />
        <button
          onClick={handleSave}
          disabled={saving || !dirty}
          title={dirty ? undefined : 'Keine Änderungen'}
          className="flex items-center gap-2 bg-ocean-700 hover:bg-ocean-600 disabled:opacity-50 text-navy-900 px-5 py-2.5 rounded-lg text-sm font-medium transition-all"
        >
          {saving ? <Loader2 className="w-4 h-4 animate-spin" /> : <Check className="w-4 h-4" />}
          Speichern (Vorzustand wird versioniert)
        </button>
        <button
          onClick={handleCancel}
          disabled={saving}
          className="flex items-center gap-2 bg-sand-100 border border-sand-300 hover:bg-sand-200 disabled:opacity-50 text-navy-700 px-5 py-2.5 rounded-lg text-sm font-medium transition-all"
        >
          <X className="w-4 h-4" />
          Verwerfen
        </button>
      </div>
    </div>
  )
}
