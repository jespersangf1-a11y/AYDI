import { useCallback, useEffect, useMemo, useState } from 'react'
import { Loader2, Package, Plus, Trash2, Zap } from 'lucide-react'
import {
  assignZoneMaterial,
  deleteZoneMaterial,
  getMaterials,
  getZoneMaterials,
} from '../../services/api'
import { parseLocaleNumber } from '../../utils/number'
import type {
  MaterialSummary,
  ZoneData,
  ZoneMaterialAssignment,
} from '../../types'

interface ZoneMaterialsPanelProps {
  projectId: string
  layoutId: string
  zones: ZoneData[]
  deckHeightMm: number
  /** Run the materials analysis module (wired to ProjectDetail's handler) */
  onRunMaterialsAnalysis: () => void
  /** True while the materials module itself is running (spinner) */
  analysisRunning: boolean
  /** True while ANY analysis is running (disables the run button) */
  busy: boolean
  /** Lifted state: survives tab switches, reset on successful analysis */
  changedSinceAnalysis: boolean
  onChangedSinceAnalysis: (changed: boolean) => void
  /** Viewer gating (pillar 4): hide mutations for read-only members.
      Backend enforces 403 regardless — this prevents dead-end clicks. */
  readOnly?: boolean
}

const SURFACE_TYPES: { value: string; label: string }[] = [
  { value: 'floor', label: 'Boden' },
  { value: 'wall', label: 'Wand' },
  { value: 'ceiling', label: 'Decke' },
  { value: 'countertop', label: 'Arbeitsfläche' },
  { value: 'upholstery', label: 'Polster' },
  { value: 'deck', label: 'Deck' },
]

const SURFACE_LABELS: Record<string, string> = Object.fromEntries(
  SURFACE_TYPES.map((s) => [s.value, s.label]),
)

/** Shoelace area of a zone polygon, mm² → m². */
function polygonAreaSqm(polygon: number[][]): number {
  if (!polygon || polygon.length < 3) return 0
  let sum = 0
  for (let i = 0; i < polygon.length; i++) {
    const [x1, y1] = polygon[i]
    const [x2, y2] = polygon[(i + 1) % polygon.length]
    sum += x1 * y2 - x2 * y1
  }
  return Math.abs(sum) / 2 / 1_000_000
}

/** Polygon perimeter, mm → m. */
function polygonPerimeterM(polygon: number[][]): number {
  if (!polygon || polygon.length < 2) return 0
  let sum = 0
  for (let i = 0; i < polygon.length; i++) {
    const [x1, y1] = polygon[i]
    const [x2, y2] = polygon[(i + 1) % polygon.length]
    sum += Math.hypot(x2 - x1, y2 - y1)
  }
  return sum / 1000
}

/**
 * Surface-aware area estimate. The floor polygon area is WRONG for walls
 * (a 12 m² salon has ~27 m² of wall) — presenting it as "geometry-based"
 * would violate "estimates are never presented as facts".
 */
function estimateAreaSqm(
  zone: ZoneData | undefined,
  surfaceType: string,
  deckHeightMm: number,
): number | null {
  if (!zone) return null
  if (surfaceType === 'floor' || surfaceType === 'ceiling') {
    const area = polygonAreaSqm(zone.polygon)
    return area > 0 ? area : null
  }
  if (surfaceType === 'wall') {
    const height = (zone.height_mm ?? deckHeightMm) / 1000
    const perimeter = polygonPerimeterM(zone.polygon)
    const area = perimeter * height
    return area > 0 ? area : null
  }
  // upholstery/countertop/deck: no defensible geometric estimate
  return null
}

function formatEur(value: number): string {
  return `${value.toLocaleString('de-DE', { maximumFractionDigits: 2 })} €`
}

/**
 * Pillar 3 (owner refit): assign/swap materials per zone. The backend CRUD
 * existed but had no UI — material customization was API-only.
 */
export default function ZoneMaterialsPanel({
  projectId,
  layoutId,
  zones,
  deckHeightMm,
  onRunMaterialsAnalysis,
  analysisRunning,
  busy,
  changedSinceAnalysis,
  onChangedSinceAnalysis,
  readOnly = false,
}: ZoneMaterialsPanelProps) {
  const [assignments, setAssignments] = useState<ZoneMaterialAssignment[]>([])
  const [materials, setMaterials] = useState<MaterialSummary[]>([])
  const [loading, setLoading] = useState(true)
  const [error, setError] = useState<string | null>(null)
  const [saving, setSaving] = useState(false)
  const [deletingId, setDeletingId] = useState<string | null>(null)

  // Form state
  const [zoneName, setZoneName] = useState('')
  const [surfaceType, setSurfaceType] = useState('floor')
  const [materialId, setMaterialId] = useState('')
  const [areaSqm, setAreaSqm] = useState('')
  const [areaTouched, setAreaTouched] = useState(false)

  const materialById = useMemo(
    () => new Map(materials.map((m) => [m.id, m])),
    [materials],
  )

  const materialsByCategory = useMemo(() => {
    const grouped = new Map<string, MaterialSummary[]>()
    for (const material of materials) {
      const list = grouped.get(material.category) ?? []
      list.push(material)
      grouped.set(material.category, list)
    }
    return Array.from(grouped.entries()).sort(([a], [b]) => a.localeCompare(b))
  }, [materials])

  const reload = useCallback(async () => {
    setLoading(true)
    setError(null)
    try {
      const [assigned, mats] = await Promise.all([
        getZoneMaterials(projectId, layoutId),
        getMaterials(),
      ])
      setAssignments(assigned)
      setMaterials(mats as unknown as MaterialSummary[])
    } catch (e) {
      setError(
        e instanceof Error ? e.message : 'Materialdaten konnten nicht geladen werden',
      )
    } finally {
      setLoading(false)
    }
  }, [projectId, layoutId])

  useEffect(() => {
    reload()
  }, [reload])

  // Surface-aware area prefill unless the user typed a value
  useEffect(() => {
    if (areaTouched) return
    const zone = zones.find((z) => z.name === zoneName)
    const area = estimateAreaSqm(zone, surfaceType, deckHeightMm)
    setAreaSqm(area != null ? area.toFixed(1) : '')
  }, [zoneName, surfaceType, zones, deckHeightMm, areaTouched])

  const existingForZoneSurface = useMemo(
    () =>
      assignments.find(
        (a) => a.zone_name === zoneName && a.surface_type === surfaceType,
      ),
    [assignments, zoneName, surfaceType],
  )

  const handleAssign = async (e: React.FormEvent) => {
    e.preventDefault()
    const area = parseLocaleNumber(areaSqm)
    if (areaSqm.trim() !== '' && area == null) {
      setError(`Fläche '${areaSqm}' ist keine gültige Zahl (z.B. 12,5).`)
      return
    }
    if (!zoneName || !materialId || area == null || area <= 0) {
      setError('Zone, Material und eine Fläche > 0 m² angeben.')
      return
    }
    setSaving(true)
    setError(null)
    try {
      // Swap semantics: one material per (zone, surface) — the analysis sums
      // per assignment, so a leftover old material would double-count the
      // same physical surface. Replace the existing assignment.
      if (existingForZoneSurface) {
        await deleteZoneMaterial(projectId, layoutId, existingForZoneSurface.id)
        setAssignments((prev) =>
          prev.filter((a) => a.id !== existingForZoneSurface.id),
        )
      }
      const created = await assignZoneMaterial(projectId, layoutId, {
        zone_name: zoneName,
        surface_type: surfaceType,
        material_id: materialId,
        area_sqm: area,
      })
      setAssignments((prev) => [...prev, created])
      onChangedSinceAnalysis(true)
      setMaterialId('')
      setAreaTouched(false)
    } catch (e) {
      setError(e instanceof Error ? e.message : 'Zuweisung fehlgeschlagen')
    } finally {
      setSaving(false)
    }
  }

  const handleDelete = async (assignment: ZoneMaterialAssignment) => {
    setDeletingId(assignment.id)
    setError(null)
    try {
      await deleteZoneMaterial(projectId, layoutId, assignment.id)
      setAssignments((prev) => prev.filter((a) => a.id !== assignment.id))
      onChangedSinceAnalysis(true)
    } catch (e) {
      setError(e instanceof Error ? e.message : 'Löschen fehlgeschlagen')
    } finally {
      setDeletingId(null)
    }
  }

  const assignmentsByZone = useMemo(() => {
    const grouped = new Map<string, ZoneMaterialAssignment[]>()
    for (const assignment of assignments) {
      const list = grouped.get(assignment.zone_name) ?? []
      list.push(assignment)
      grouped.set(assignment.zone_name, list)
    }
    return grouped
  }, [assignments])

  if (loading) {
    return (
      <div className="flex items-center gap-2 text-navy-600 text-sm py-8">
        <Loader2 className="w-4 h-4 animate-spin" />
        Lade Materialzuweisungen...
      </div>
    )
  }

  return (
    <div className="space-y-6">
      {error && (
        <div className="card-premium bg-amber-950/20 border-amber-700/20 p-4 text-amber-300 text-sm">
          {error}
        </div>
      )}

      {readOnly && (
        <div className="card-premium px-6 py-4 text-sm text-navy-600">
          Nur-Lesen-Zugriff — Materialzuweisungen können Sie einsehen, aber
          nicht ändern.
        </div>
      )}

      {/* Assign form (hidden for read-only members) */}
      {!readOnly && (
      <form onSubmit={handleAssign} className="card-premium px-6 py-5">
        <h3 className="font-sans font-semibold text-navy-900 mb-4 flex items-center gap-2">
          <Package className="w-4 h-4 text-ocean-500" />
          Material zuweisen
        </h3>
        <div className="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-4 gap-4 mb-4">
          <div>
            <label htmlFor="zm-zone" className="label-premium mb-2 block">Zone</label>
            <select
              id="zm-zone"
              value={zoneName}
              onChange={(e) => {
                setZoneName(e.target.value)
                setAreaTouched(false)
              }}
              className="w-full rounded-lg border border-sand-200 bg-white px-3 py-2 text-sm text-navy-900 focus:border-ocean-500 focus:outline-none"
            >
              <option value="">Wählen...</option>
              {zones.map((zone) => (
                <option key={zone.name} value={zone.name}>
                  {zone.name}
                </option>
              ))}
            </select>
          </div>
          <div>
            <label htmlFor="zm-surface" className="label-premium mb-2 block">Oberfläche</label>
            <select
              id="zm-surface"
              value={surfaceType}
              onChange={(e) => setSurfaceType(e.target.value)}
              className="w-full rounded-lg border border-sand-200 bg-white px-3 py-2 text-sm text-navy-900 focus:border-ocean-500 focus:outline-none"
            >
              {SURFACE_TYPES.map((surface) => (
                <option key={surface.value} value={surface.value}>
                  {surface.label}
                </option>
              ))}
            </select>
          </div>
          <div>
            <label htmlFor="zm-material" className="label-premium mb-2 block">Material</label>
            <select
              id="zm-material"
              value={materialId}
              onChange={(e) => setMaterialId(e.target.value)}
              className="w-full rounded-lg border border-sand-200 bg-white px-3 py-2 text-sm text-navy-900 focus:border-ocean-500 focus:outline-none"
            >
              <option value="">Wählen...</option>
              {materialsByCategory.map(([category, items]) => (
                <optgroup key={category} label={category}>
                  {items.map((material) => (
                    <option key={material.id} value={material.id}>
                      {material.name}
                      {material.cost_per_unit
                        ? ` (${formatEur(material.cost_per_unit)}/${material.cost_unit})`
                        : ''}
                    </option>
                  ))}
                </optgroup>
              ))}
            </select>
          </div>
          <div>
            <label htmlFor="zm-area" className="label-premium mb-2 block">Fläche (m²)</label>
            <input
              id="zm-area"
              type="text"
              inputMode="decimal"
              value={areaSqm}
              onChange={(e) => {
                setAreaSqm(e.target.value)
                setAreaTouched(true)
              }}
              placeholder="z.B. 12,5"
              className="w-full rounded-lg border border-sand-200 bg-white px-3 py-2 text-sm text-navy-900 focus:border-ocean-500 focus:outline-none"
            />
            {!areaTouched && zoneName && areaSqm && (
              <p className="text-xs text-navy-500 mt-1">aus Zonengeometrie geschätzt</p>
            )}
          </div>
        </div>
        <div className="flex items-center gap-3">
          <button
            type="submit"
            disabled={saving || !zoneName || !materialId}
            className="flex items-center gap-2 bg-ocean-700 hover:bg-ocean-600 disabled:opacity-50 disabled:cursor-not-allowed text-navy-900 px-5 py-2.5 rounded-lg text-sm font-medium transition-all duration-200"
          >
            {saving ? <Loader2 className="w-4 h-4 animate-spin" /> : <Plus className="w-4 h-4" />}
            {existingForZoneSurface ? 'Ersetzen' : 'Zuweisen'}
          </button>
          {existingForZoneSurface && (
            <span className="text-xs text-amber-600">
              Ersetzt die bestehende Zuweisung für {zoneName}/
              {SURFACE_LABELS[surfaceType] ?? surfaceType}
            </span>
          )}
        </div>
      </form>
      )}

      {/* Current assignments */}
      <div>
        <div className="flex items-center justify-between mb-4">
          <p className="label-premium">
            Zuweisungen ({assignments.length})
          </p>
          <div className="flex items-center gap-3">
            {changedSinceAnalysis && (
              <span className="text-xs text-amber-600">
                Änderungen noch nicht analysiert
              </span>
            )}
            <button
              onClick={onRunMaterialsAnalysis}
              disabled={busy || assignments.length === 0 || readOnly}
              title={
                readOnly
                  ? 'Nur-Lesen-Zugriff — Analysen sind für Betrachter deaktiviert'
                  : assignments.length === 0
                  ? 'Erst Materialien zuweisen'
                  : busy && !analysisRunning
                  ? 'Eine andere Analyse läuft gerade'
                  : 'Materialanalyse mit den aktuellen Zuweisungen ausführen'
              }
              className="flex items-center gap-2 bg-ocean-700 hover:bg-ocean-600 disabled:opacity-50 text-navy-900 px-4 py-2 rounded-lg text-xs font-medium transition-all duration-200"
            >
              {analysisRunning ? (
                <Loader2 className="w-3.5 h-3.5 animate-spin" />
              ) : (
                <Zap className="w-3.5 h-3.5" />
              )}
              Materialanalyse ausführen
            </button>
          </div>
        </div>

        {assignments.length === 0 ? (
          <div className="card-premium px-8 py-10 text-center text-navy-600 text-sm">
            Noch keine Materialien zugewiesen. Weisen Sie oben ein Material zu —
            die Materialanalyse bewertet dann Lebensdauer, Kosten und Risiken
            Ihrer Auswahl.
          </div>
        ) : (
          <div className="space-y-4">
            {Array.from(assignmentsByZone.entries()).map(([zone, zoneAssignments]) => (
              <div key={zone} className="card-premium px-6 py-4">
                <p className="font-medium text-navy-900 text-sm mb-3">{zone}</p>
                <ul className="space-y-2">
                  {zoneAssignments.map((assignment) => {
                    const material = materialById.get(assignment.material_id)
                    return (
                      <li
                        key={assignment.id}
                        className="flex items-center justify-between gap-3 text-sm"
                      >
                        <div className="min-w-0">
                          <span className="text-navy-900">
                            {material?.name ?? 'Unbekanntes Material'}
                          </span>
                          <span className="text-xs text-navy-600">
                            {' '}
                            · {SURFACE_LABELS[assignment.surface_type] ?? assignment.surface_type}
                            {' '}· {assignment.area_sqm.toLocaleString('de-DE')} m²
                            {material?.lifespan_years
                              ? ` · typ. ${material.lifespan_years} J. Lebensdauer`
                              : ''}
                          </span>
                        </div>
                        {!readOnly && (
                          <button
                            onClick={() => handleDelete(assignment)}
                            disabled={deletingId !== null}
                            aria-label={`Zuweisung ${material?.name ?? ''} entfernen`}
                            className="flex-shrink-0 p-1.5 rounded text-navy-500 hover:text-red-600 hover:bg-red-50 transition-colors disabled:opacity-50"
                          >
                            {deletingId === assignment.id ? (
                              <Loader2 className="w-4 h-4 animate-spin" />
                            ) : (
                              <Trash2 className="w-4 h-4" />
                            )}
                          </button>
                        )}
                      </li>
                    )
                  })}
                </ul>
              </div>
            ))}
          </div>
        )}
      </div>
    </div>
  )
}
