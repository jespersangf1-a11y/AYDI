import { useCallback, useEffect, useMemo, useState } from 'react'
import { Anchor, Loader2, Plus, Trash2, Zap } from 'lucide-react'
import {
  createStructuralItem,
  deleteStructuralItem,
  getStructuralItems,
  updateStructuralItem,
} from '../../services/api'
import { parseLocaleNumber } from '../../utils/number'
import type { StructuralItemData, ZoneData } from '../../types'

interface StructuralItemsPanelProps {
  projectId: string
  layoutId: string
  zones: ZoneData[]
  onRunStructuralAnalysis: () => void
  /** True while the structural module itself is running (spinner) */
  analysisRunning: boolean
  /** True while ANY analysis is running (disables the run button) */
  busy: boolean
  changedSinceAnalysis: boolean
  onChangedSinceAnalysis: (changed: boolean) => void
  /** Viewer gating (pillar 4): hide mutations for read-only members.
      Backend enforces 403 regardless — this prevents dead-end clicks. */
  readOnly?: boolean
}

const ITEM_TYPES: { value: string; label: string }[] = [
  { value: 'engine', label: 'Motor' },
  { value: 'ballast', label: 'Ballast' },
  { value: 'fuel_tank', label: 'Kraftstofftank' },
  { value: 'water_tank', label: 'Wassertank' },
  { value: 'battery', label: 'Batteriebank' },
  { value: 'anchor_chain', label: 'Anker & Kette' },
  { value: 'rigging', label: 'Rigg' },
  { value: 'other', label: 'Sonstiges' },
]

const ITEM_LABELS: Record<string, string> = Object.fromEntries(
  ITEM_TYPES.map((t) => [t.value, t.label]),
)

function boatExtents(zones: ZoneData[]): { minX: number; maxX: number } | null {
  const xs = zones.flatMap((z) => z.polygon?.map((p) => p[0]) ?? [])
  if (xs.length === 0) return null
  return { minX: Math.min(...xs), maxX: Math.max(...xs) }
}

/**
 * Pillar 3: measured weights/positions. These feed the structural analysis
 * (CG, loading conditions, trim) as point masses — previously they were
 * collected via the API but silently ignored by the analysis, and had no UI.
 */
export default function StructuralItemsPanel({
  projectId,
  layoutId,
  zones,
  onRunStructuralAnalysis,
  analysisRunning,
  busy,
  changedSinceAnalysis,
  onChangedSinceAnalysis,
  readOnly = false,
}: StructuralItemsPanelProps) {
  const [items, setItems] = useState<StructuralItemData[]>([])
  const [loading, setLoading] = useState(true)
  const [error, setError] = useState<string | null>(null)
  const [saving, setSaving] = useState(false)
  const [deletingId, setDeletingId] = useState<string | null>(null)

  // Form state
  const [name, setName] = useState('')
  const [itemType, setItemType] = useState('engine')
  const [weightKg, setWeightKg] = useState('')
  const [posX, setPosX] = useState('')
  const [posY, setPosY] = useState('')

  const extents = useMemo(() => boatExtents(zones), [zones])

  const reload = useCallback(async () => {
    setLoading(true)
    setError(null)
    try {
      setItems(await getStructuralItems(projectId, layoutId))
    } catch (e) {
      setError(
        e instanceof Error ? e.message : 'Strukturelemente konnten nicht geladen werden',
      )
    } finally {
      setLoading(false)
    }
  }, [projectId, layoutId])

  useEffect(() => {
    reload()
  }, [reload])

  const handleAdd = async (e: React.FormEvent) => {
    e.preventDefault()
    const weight = weightKg.trim() === '' ? null : parseLocaleNumber(weightKg)
    const x = posX.trim() === '' ? null : parseLocaleNumber(posX)
    const y = posY.trim() === '' ? null : parseLocaleNumber(posY)
    if (weightKg.trim() !== '' && weight == null) {
      setError(`Gewicht '${weightKg}' ist keine gültige Zahl (z.B. 2000 oder 2.000).`)
      return
    }
    if ((posX.trim() !== '' && x == null) || (posY.trim() !== '' && y == null)) {
      setError('Position ist keine gültige Zahl (mm, z.B. 9.500).')
      return
    }
    if (!name.trim() || weight == null || weight <= 0) {
      setError('Name und ein Gewicht > 0 kg angeben.')
      return
    }
    setSaving(true)
    setError(null)
    try {
      const created = await createStructuralItem(projectId, layoutId, {
        name: name.trim(),
        item_type: itemType,
        weight_kg: weight,
        position_x_mm: x,
        position_y_mm: y,
      })
      setItems((prev) => [...prev, created])
      onChangedSinceAnalysis(true)
      setName('')
      setWeightKg('')
      setPosX('')
      setPosY('')
    } catch (e) {
      setError(e instanceof Error ? e.message : 'Anlegen fehlgeschlagen')
    } finally {
      setSaving(false)
    }
  }

  const handleDelete = async (item: StructuralItemData) => {
    if (!window.confirm(`Strukturelement '${item.name}' wirklich löschen?`)) return
    setDeletingId(item.id)
    setError(null)
    try {
      await deleteStructuralItem(projectId, layoutId, item.id)
      setItems((prev) => prev.filter((i) => i.id !== item.id))
      onChangedSinceAnalysis(true)
    } catch (e) {
      setError(e instanceof Error ? e.message : 'Löschen fehlgeschlagen')
    } finally {
      setDeletingId(null)
    }
  }

  // Inline position editing (PATCH): items without X are useless to the
  // analysis — forcing delete-and-retype would risk fresh input errors.
  const [editingId, setEditingId] = useState<string | null>(null)
  const [editX, setEditX] = useState('')
  const [editY, setEditY] = useState('')
  const [savingPosition, setSavingPosition] = useState(false)

  const handleSavePosition = async (item: StructuralItemData) => {
    const x = parseLocaleNumber(editX)
    if (x == null) {
      setError(`Position '${editX}' ist keine gültige Zahl (mm).`)
      return
    }
    const y = editY.trim() === '' ? null : parseLocaleNumber(editY)
    if (editY.trim() !== '' && y == null) {
      setError(`Position '${editY}' ist keine gültige Zahl (mm).`)
      return
    }
    setSavingPosition(true)
    setError(null)
    try {
      const updated = await updateStructuralItem(projectId, layoutId, item.id, {
        position_x_mm: x,
        ...(y != null ? { position_y_mm: y } : {}),
      })
      setItems((prev) => prev.map((i) => (i.id === item.id ? updated : i)))
      onChangedSinceAnalysis(true)
      setEditingId(null)
      setEditX('')
      setEditY('')
    } catch (e) {
      setError(e instanceof Error ? e.message : 'Position konnte nicht gespeichert werden')
    } finally {
      setSavingPosition(false)
    }
  }

  const totalWeight = useMemo(
    () => items.reduce((sum, item) => sum + (item.weight_kg || 0), 0),
    [items],
  )
  const withoutPosition = useMemo(
    () => items.filter((i) => i.position_x_mm == null).length,
    [items],
  )

  if (loading) {
    return (
      <div className="flex items-center gap-2 text-navy-600 text-sm py-8">
        <Loader2 className="w-4 h-4 animate-spin" />
        Lade Strukturelemente...
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
          Nur-Lesen-Zugriff — Strukturelemente können Sie einsehen, aber
          nicht ändern.
        </div>
      )}

      {/* Add form (hidden for read-only members) */}
      {!readOnly && (
      <form onSubmit={handleAdd} className="card-premium px-6 py-5">
        <h3 className="font-sans font-semibold text-navy-900 mb-1 flex items-center gap-2">
          <Anchor className="w-4 h-4 text-ocean-500" />
          Strukturelement erfassen
        </h3>
        <p className="text-xs text-navy-600 mb-4">
          Gemessene Gewichte und Positionen fließen als Punktmassen in
          Schwerpunkt-, Beladungs- und Trimmanalyse ein.
          {extents &&
            ` Längsposition X von ${extents.minX.toLocaleString('de-DE')} bis ${extents.maxX.toLocaleString('de-DE')} mm (Elemente außerhalb sind zulässig, z.B. Motor achtern).`}
        </p>
        <div className="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-5 gap-4 mb-4">
          <div>
            <label htmlFor="si-name" className="label-premium mb-2 block">Name</label>
            <input
              id="si-name"
              type="text"
              value={name}
              onChange={(e) => setName(e.target.value)}
              placeholder="z.B. Volvo D2-50"
              className="w-full rounded-lg border border-sand-200 bg-white px-3 py-2 text-sm text-navy-900 focus:border-ocean-500 focus:outline-none"
            />
          </div>
          <div>
            <label htmlFor="si-type" className="label-premium mb-2 block">Typ</label>
            <select
              id="si-type"
              value={itemType}
              onChange={(e) => setItemType(e.target.value)}
              className="w-full rounded-lg border border-sand-200 bg-white px-3 py-2 text-sm text-navy-900 focus:border-ocean-500 focus:outline-none"
            >
              {ITEM_TYPES.map((type) => (
                <option key={type.value} value={type.value}>
                  {type.label}
                </option>
              ))}
            </select>
            {(itemType === 'fuel_tank' || itemType === 'water_tank') && (
              <p className="text-xs text-navy-500 mt-1">
                Gewicht bei vollem Tank — Beladungszustände skalieren die Füllung
              </p>
            )}
          </div>
          <div>
            <label htmlFor="si-weight" className="label-premium mb-2 block">Gewicht (kg)</label>
            <input
              id="si-weight"
              type="text"
              inputMode="decimal"
              value={weightKg}
              onChange={(e) => setWeightKg(e.target.value)}
              placeholder="z.B. 240"
              className="w-full rounded-lg border border-sand-200 bg-white px-3 py-2 text-sm text-navy-900 focus:border-ocean-500 focus:outline-none"
            />
          </div>
          <div>
            <label htmlFor="si-x" className="label-premium mb-2 block">Position X (mm)</label>
            <input
              id="si-x"
              type="text"
              inputMode="decimal"
              value={posX}
              onChange={(e) => setPosX(e.target.value)}
              placeholder="längs, ab Referenz"
              className="w-full rounded-lg border border-sand-200 bg-white px-3 py-2 text-sm text-navy-900 focus:border-ocean-500 focus:outline-none"
            />
          </div>
          <div>
            <label htmlFor="si-y" className="label-premium mb-2 block">Position Y (mm)</label>
            <input
              id="si-y"
              type="text"
              inputMode="decimal"
              value={posY}
              onChange={(e) => setPosY(e.target.value)}
              placeholder="quer, optional"
              className="w-full rounded-lg border border-sand-200 bg-white px-3 py-2 text-sm text-navy-900 focus:border-ocean-500 focus:outline-none"
            />
          </div>
        </div>
        <div className="flex items-center gap-3">
          <button
            type="submit"
            disabled={saving || !name.trim() || !weightKg.trim()}
            className="flex items-center gap-2 bg-ocean-700 hover:bg-ocean-600 disabled:opacity-50 disabled:cursor-not-allowed text-navy-900 px-5 py-2.5 rounded-lg text-sm font-medium transition-all duration-200"
          >
            {saving ? <Loader2 className="w-4 h-4 animate-spin" /> : <Plus className="w-4 h-4" />}
            Erfassen
          </button>
          {posX.trim() === '' && (
            <span className="text-xs text-amber-600">
              Ohne X-Position geht das Element NICHT in die Analyse ein
            </span>
          )}
        </div>
      </form>
      )}

      {/* Item list */}
      <div>
        <div className="flex items-center justify-between mb-4 flex-wrap gap-3">
          <p className="label-premium">
            Elemente ({items.length}
            {totalWeight > 0 ? ` · ${totalWeight.toLocaleString('de-DE')} kg` : ''})
          </p>
          <div className="flex items-center gap-3">
            {changedSinceAnalysis && (
              <span className="text-xs text-amber-600">
                Änderungen noch nicht analysiert
              </span>
            )}
            <button
              onClick={onRunStructuralAnalysis}
              disabled={busy || items.length === 0 || readOnly}
              title={
                readOnly
                  ? 'Nur-Lesen-Zugriff — Analysen sind für Betrachter deaktiviert'
                  : items.length === 0
                  ? 'Erst Strukturelemente erfassen'
                  : busy && !analysisRunning
                  ? 'Eine andere Analyse läuft gerade'
                  : 'Strukturanalyse mit den gemessenen Elementen ausführen'
              }
              className="flex items-center gap-2 bg-ocean-700 hover:bg-ocean-600 disabled:opacity-50 text-navy-900 px-4 py-2 rounded-lg text-xs font-medium transition-all duration-200"
            >
              {analysisRunning ? (
                <Loader2 className="w-3.5 h-3.5 animate-spin" />
              ) : (
                <Zap className="w-3.5 h-3.5" />
              )}
              Strukturanalyse ausführen
            </button>
          </div>
        </div>

        {withoutPosition > 0 && (
          <div className="mb-3 border-l-4 border-amber-400 bg-amber-50 rounded-r px-4 py-2 text-xs text-amber-900">
            {withoutPosition} Element(e) ohne X-Position werden von der Analyse
            übersprungen — Position über „Position nachtragen" ergänzen.
          </div>
        )}

        {items.length === 0 ? (
          <div className="card-premium px-8 py-10 text-center text-navy-600 text-sm">
            Noch keine Strukturelemente erfasst. Gemessene Gewichte (Motor,
            Ballast, Tanks, Batterien) machen Schwerpunkt- und Trimmanalyse
            deutlich belastbarer als die Flächenheuristik allein.
          </div>
        ) : (
          <ul className="space-y-2">
            {items.map((item) => (
              <li
                key={item.id}
                className="card-premium px-5 py-3 flex items-center justify-between gap-3 text-sm"
              >
                <div className="min-w-0">
                  <span className="text-navy-900 font-medium">{item.name}</span>
                  <span className="text-xs text-navy-600">
                    {' '}
                    · {ITEM_LABELS[item.item_type] ?? item.item_type}
                    {' '}· {item.weight_kg.toLocaleString('de-DE')} kg
                    {item.position_x_mm != null
                      ? ` · X ${item.position_x_mm.toLocaleString('de-DE')} mm`
                      : ' · ohne Position'}
                    {item.position_y_mm != null
                      ? ` · Y ${item.position_y_mm.toLocaleString('de-DE')} mm`
                      : ''}
                  </span>
                  {item.position_x_mm == null && editingId !== item.id && !readOnly && (
                    <button
                      onClick={() => {
                        setEditingId(item.id)
                        setEditX('')
                        setEditY('')
                      }}
                      className="ml-2 text-xs text-ocean-600 underline hover:text-ocean-500"
                    >
                      Position nachtragen
                    </button>
                  )}
                  {editingId === item.id && (
                    <span className="ml-2 inline-flex items-center gap-2">
                      <input
                        type="text"
                        inputMode="decimal"
                        value={editX}
                        onChange={(e) => setEditX(e.target.value)}
                        placeholder="X (mm)"
                        aria-label={`X-Position für ${item.name}`}
                        className="w-24 rounded border border-sand-200 bg-white px-2 py-1 text-xs text-navy-900 focus:border-ocean-500 focus:outline-none"
                      />
                      <input
                        type="text"
                        inputMode="decimal"
                        value={editY}
                        onChange={(e) => setEditY(e.target.value)}
                        placeholder="Y (mm, opt.)"
                        aria-label={`Y-Position für ${item.name}`}
                        className="w-24 rounded border border-sand-200 bg-white px-2 py-1 text-xs text-navy-900 focus:border-ocean-500 focus:outline-none"
                      />
                      <button
                        onClick={() => handleSavePosition(item)}
                        disabled={savingPosition || editX.trim() === ''}
                        className="text-xs bg-ocean-700 hover:bg-ocean-600 disabled:opacity-50 text-navy-900 px-2 py-1 rounded"
                      >
                        {savingPosition ? '…' : 'Speichern'}
                      </button>
                      <button
                        onClick={() => setEditingId(null)}
                        className="text-xs text-navy-500 underline"
                      >
                        Abbrechen
                      </button>
                    </span>
                  )}
                </div>
                {!readOnly && (
                  <button
                    onClick={() => handleDelete(item)}
                    disabled={deletingId !== null}
                    aria-label={`${item.name} löschen`}
                    className="flex-shrink-0 p-1.5 rounded text-navy-500 hover:text-red-600 hover:bg-red-50 transition-colors disabled:opacity-50"
                  >
                    {deletingId === item.id ? (
                      <Loader2 className="w-4 h-4 animate-spin" />
                    ) : (
                      <Trash2 className="w-4 h-4" />
                    )}
                  </button>
                )}
              </li>
            ))}
          </ul>
        )}
      </div>
    </div>
  )
}
