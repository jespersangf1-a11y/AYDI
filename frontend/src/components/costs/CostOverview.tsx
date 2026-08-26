import { useCallback, useEffect, useMemo, useState } from 'react'
import { Euro, Loader2, Plus, RefreshCw, Trash2 } from 'lucide-react'
import { getCostSummary } from '../../services/api'
import { createCostItem, deleteCostItem, listCostItems } from '../../services/cost-api'
import { parseLocaleNumber } from '../../utils/number'
import type { CostItem, CostSummary, ZoneData } from '../../types'

interface CostOverviewProps {
  projectId: string
  layoutId: string
  /** Optional: zone names for the zone picker (falls back to free text). */
  zones?: ZoneData[]
  /** Viewer gating (pillar 4): the backend answers 403 regardless — this only
      prevents dead-end clicks for read-only members. */
  readOnly?: boolean
}

function formatCurrency(value: number, digits = 2): string {
  return value.toLocaleString('de-DE', {
    style: 'currency',
    currency: 'EUR',
    minimumFractionDigits: digits,
    maximumFractionDigits: digits,
  })
}

function formatAmountInput(value: number): string {
  return value.toLocaleString('de-DE', {
    minimumFractionDigits: 2,
    maximumFractionDigits: 2,
  })
}

function formatQuantity(value: number): string {
  return value.toLocaleString('de-DE', { maximumFractionDigits: 3 })
}

// --- Domain vocabulary (mirrors backend/app/services/analysis/cost.py) ---

const CATEGORIES: { value: string; label: string; hint: string }[] = [
  {
    value: 'material',
    label: 'Material',
    hint: 'Fließt in die Materialkosten-Teilanalyse (Konzentration je Position).',
  },
  {
    value: 'labor',
    label: 'Arbeitszeit',
    hint: 'Wird gegen die geschätzten Fertigungsstunden gerechnet.',
  },
  { value: 'equipment', label: 'Ausrüstung / Technik', hint: '' },
  { value: 'overhead', label: 'Gemeinkosten', hint: '' },
  { value: 'other', label: 'Sonstiges', hint: '' },
]

const CATEGORY_LABELS: Record<string, string> = Object.fromEntries(
  CATEGORIES.map((c) => [c.value, c.label]),
)

const UNITS: { value: string; label: string }[] = [
  { value: 'piece', label: 'Stück' },
  { value: 'sqm', label: 'm²' },
  { value: 'm', label: 'lfd. Meter' },
  { value: 'kg', label: 'kg' },
  { value: 'liter', label: 'Liter' },
  { value: 'hour', label: 'Stunde' },
  { value: 'lot', label: 'Pauschal' },
]

const UNIT_LABELS: Record<string, string> = Object.fromEntries(
  UNITS.map((u) => [u.value, u.label]),
)

/**
 * Data quality per position. The backend weights these in `analyze_cost_risk`:
 * quote/contract = 1.0, budget = 0.6, estimate = 0.0. Above a 60 % estimate
 * share the analysis raises COST_UNCERTAINTY_HIGH.
 */
const SOURCES: {
  value: string
  label: string
  weight: number
  hint: string
  badgeClass: string
}[] = [
  {
    value: 'quote',
    label: 'Verbindliches Angebot',
    weight: 1.0,
    hint: 'Schriftliches Angebot eines Lieferanten — höchste Datengüte.',
    badgeClass: 'bg-emerald-50 text-emerald-700 border-emerald-200',
  },
  {
    value: 'contract',
    label: 'Vertrag / Auftrag',
    weight: 1.0,
    hint: 'Beauftragt oder vertraglich fixiert — höchste Datengüte.',
    badgeClass: 'bg-emerald-50 text-emerald-700 border-emerald-200',
  },
  {
    value: 'budget',
    label: 'Budgetansatz',
    weight: 0.6,
    hint: 'Interner Budgetwert aus Erfahrung — mittlere Datengüte.',
    badgeClass: 'bg-amber-50 text-amber-700 border-amber-200',
  },
  {
    value: 'estimate',
    label: 'Schätzung',
    weight: 0.0,
    hint: 'Grobe Schätzung — geht als Kalkulationsrisiko in die Analyse ein.',
    badgeClass: 'bg-sand-50 text-navy-600 border-sand-200',
  },
]

const SOURCE_BY_VALUE: Record<string, (typeof SOURCES)[number]> = Object.fromEntries(
  SOURCES.map((s) => [s.value, s]),
)

const CATEGORY_COLORS = [
  'bg-ocean-500',
  'bg-emerald-500',
  'bg-amber-500',
  'bg-purple-500',
  'bg-red-500',
  'bg-pink-500',
  'bg-cyan-500',
  'bg-indigo-500',
]

const INPUT_CLASS =
  'w-full rounded-lg border border-sand-200 bg-white px-3 py-2 text-sm text-navy-900 focus:border-ocean-500 focus:outline-none'

function BreakdownBar({
  label,
  value,
  total,
  colorClass,
}: {
  label: string
  value: number
  total: number
  colorClass: string
}) {
  const pct = total > 0 ? (value / total) * 100 : 0
  return (
    <div>
      <div className="flex justify-between items-center mb-2">
        <span className="label-premium">{label}</span>
        <div className="text-right">
          <span className="font-mono text-sm font-semibold text-navy-900">
            {formatCurrency(value)}
          </span>
          <span className="text-navy-500 text-xs ml-2">({pct.toFixed(1)} %)</span>
        </div>
      </div>
      <div className="h-1.5 bg-sand-50/60 rounded-full overflow-hidden">
        <div
          className={`h-full rounded-full transition-all duration-300 ${colorClass}`}
          style={{ width: `${pct}%` }}
        />
      </div>
    </div>
  )
}

function SourceBadge({ source }: { source: string }) {
  const meta = SOURCE_BY_VALUE[source]
  return (
    <span
      title={meta ? meta.hint : 'Unbekannte Quelle — wird wie eine Schätzung gewertet.'}
      className={`inline-flex items-center rounded border px-1.5 py-0.5 text-[11px] font-medium ${
        meta ? meta.badgeClass : 'bg-sand-50 text-navy-600 border-sand-200'
      }`}
    >
      {meta ? meta.label : source}
    </span>
  )
}

/**
 * Pillar 3/4: manual capture of cost items. Without this form the cost module
 * reported "Keine Kostenpositionen vorhanden" for every real user — the API
 * existed, the UI did not.
 */
export default function CostOverview({
  projectId,
  layoutId,
  zones,
  readOnly = false,
}: CostOverviewProps) {
  const [summary, setSummary] = useState<CostSummary | null>(null)
  const [items, setItems] = useState<CostItem[]>([])
  const [loading, setLoading] = useState(true)
  const [error, setError] = useState<string | null>(null)
  const [formError, setFormError] = useState<string | null>(null)
  const [saving, setSaving] = useState(false)
  const [deletingId, setDeletingId] = useState<string | null>(null)
  const [activeTab, setActiveTab] = useState<'category' | 'zone'>('category')

  // --- Form state ---
  const [category, setCategory] = useState('material')
  const [subcategory, setSubcategory] = useState('')
  const [description, setDescription] = useState('')
  const [quantity, setQuantity] = useState('1')
  const [unit, setUnit] = useState('piece')
  const [unitCost, setUnitCost] = useState('')
  const [totalCost, setTotalCost] = useState('')
  const [totalTouched, setTotalTouched] = useState(false)
  const [zoneName, setZoneName] = useState('')
  const [source, setSource] = useState('estimate')
  const [notes, setNotes] = useState('')

  const reload = useCallback(async () => {
    setLoading(true)
    setError(null)
    try {
      const [summaryData, itemData] = await Promise.all([
        getCostSummary(projectId, layoutId),
        listCostItems(projectId, layoutId),
      ])
      setSummary(summaryData)
      setItems(itemData)
    } catch (e) {
      setError(e instanceof Error ? e.message : 'Kostendaten konnten nicht geladen werden')
    } finally {
      setLoading(false)
    }
  }, [projectId, layoutId])

  useEffect(() => {
    reload()
  }, [reload])

  const parsedQuantity = parseLocaleNumber(quantity)
  const parsedUnitCost = parseLocaleNumber(unitCost)
  const parsedTotal = parseLocaleNumber(totalCost)
  const computedTotal =
    parsedQuantity != null && parsedUnitCost != null ? parsedQuantity * parsedUnitCost : null

  // Pre-compute total = quantity x unit cost so the value is not typed twice.
  // Stops as soon as the user corrects the total by hand (Pauschale, Rabatt).
  useEffect(() => {
    if (totalTouched) return
    if (computedTotal == null) {
      setTotalCost('')
      return
    }
    setTotalCost(formatAmountInput(computedTotal))
  }, [computedTotal, totalTouched])

  const totalDiffers =
    totalTouched &&
    computedTotal != null &&
    parsedTotal != null &&
    Math.abs(parsedTotal - computedTotal) > 0.005

  const resetForm = () => {
    setSubcategory('')
    setDescription('')
    setQuantity('1')
    setUnitCost('')
    setTotalCost('')
    setTotalTouched(false)
    setZoneName('')
    setNotes('')
  }

  const handleSubmit = async (e: React.FormEvent) => {
    e.preventDefault()
    setFormError(null)

    if (parsedQuantity == null || parsedQuantity < 0) {
      setFormError(`Menge '${quantity}' ist keine gültige Zahl größer oder gleich 0 (z.B. 2 oder 2,5).`)
      return
    }
    if (parsedUnitCost == null || parsedUnitCost < 0) {
      setFormError(`Einzelpreis '${unitCost}' ist keine gültige Zahl größer oder gleich 0 (z.B. 1.250,00).`)
      return
    }
    if (parsedTotal == null || parsedTotal < 0) {
      setFormError(`Gesamtpreis '${totalCost}' ist keine gültige Zahl größer oder gleich 0 (z.B. 1.250,00).`)
      return
    }

    setSaving(true)
    try {
      await createCostItem(projectId, layoutId, {
        category,
        subcategory: subcategory.trim() || null,
        description: description.trim() || null,
        quantity: parsedQuantity,
        unit,
        unit_cost_eur: parsedUnitCost,
        total_cost_eur: parsedTotal,
        zone_name: zoneName.trim() || null,
        source,
        notes: notes.trim() || null,
      })
      resetForm()
      await reload()
    } catch (err) {
      setFormError(
        err instanceof Error ? err.message : 'Kostenposition konnte nicht gespeichert werden',
      )
    } finally {
      setSaving(false)
    }
  }

  const handleDelete = async (item: CostItem) => {
    const label =
      item.description || item.subcategory || CATEGORY_LABELS[item.category] || item.category
    if (!window.confirm(`Kostenposition '${label}' wirklich löschen?`)) return
    setDeletingId(item.id)
    setFormError(null)
    try {
      await deleteCostItem(projectId, layoutId, item.id)
      await reload()
    } catch (err) {
      setFormError(err instanceof Error ? err.message : 'Löschen fehlgeschlagen')
    } finally {
      setDeletingId(null)
    }
  }

  // Client-side mirror of `analyze_cost_risk` so the user sees WHY the
  // confidence of the cost result ends up where it does.
  const dataQuality = useMemo(() => {
    const total = items.reduce((sum, i) => sum + i.total_cost_eur, 0)
    if (total <= 0) return null
    let reliable = 0
    let estimate = 0
    for (const i of items) {
      const weight = SOURCE_BY_VALUE[i.source]?.weight ?? 0
      reliable += i.total_cost_eur * weight
      if (weight === 0) estimate += i.total_cost_eur
    }
    return {
      quoteShare: reliable / total,
      estimateShare: estimate / total,
    }
  }, [items])

  const zoneOptions = useMemo(
    () => Array.from(new Set((zones ?? []).map((z) => z.name).filter(Boolean))),
    [zones],
  )

  const categoryHint = CATEGORIES.find((c) => c.value === category)?.hint ?? ''
  const sourceHint = SOURCE_BY_VALUE[source]?.hint ?? ''

  if (loading) {
    return (
      <div className="flex items-center gap-2 text-navy-600 text-xs font-sans font-semibold uppercase tracking-wider-premium">
        <Loader2 className="w-4 h-4 animate-spin" />
        Lade Kostendaten
      </div>
    )
  }

  if (error) {
    return (
      <div className="space-y-4">
        <div className="card-premium border-red-500/30 bg-red-500/5 p-4 text-sm text-red-600">
          Fehler beim Laden: {error}
        </div>
        <button
          onClick={reload}
          className="flex items-center gap-2 bg-ocean-700 hover:bg-ocean-600 text-navy-900 px-4 py-2 rounded-lg text-xs font-medium transition-all duration-200"
        >
          <RefreshCw className="w-3.5 h-3.5" />
          Erneut versuchen
        </button>
      </div>
    )
  }

  const totalCostSum = summary?.total_cost ?? 0
  const itemCount = summary?.item_count ?? items.length
  const categoryEntries = Object.entries(summary?.breakdown_by_category ?? {}).sort(
    ([, a], [, b]) => b - a,
  )
  const zoneEntries = Object.entries(summary?.breakdown_by_zone ?? {}).sort(([, a], [, b]) => b - a)

  return (
    <div className="space-y-6">
      {/* Total cost hero */}
      <div className="card-premium p-6 text-center">
        <p className="label-premium mb-3">Erfasste Gesamtkosten</p>
        <p className="font-mono text-4xl font-bold text-navy-900 mb-2">
          {formatCurrency(totalCostSum, 0)}
        </p>
        <p className="text-xs text-navy-500">
          {itemCount === 1 ? '1 Kostenposition' : `${itemCount} Kostenpositionen`}
        </p>
        {dataQuality && (
          <div className="mt-5 max-w-md mx-auto text-left">
            <div className="flex justify-between items-center mb-2">
              <span className="label-premium">Datengüte</span>
              <span className="text-xs text-navy-500">
                {(dataQuality.quoteShare * 100).toFixed(0)} % belegt ·{' '}
                {(dataQuality.estimateShare * 100).toFixed(0)} % geschätzt
              </span>
            </div>
            <div className="h-1.5 bg-sand-50/60 rounded-full overflow-hidden">
              <div
                className="h-full rounded-full bg-emerald-500 transition-all duration-300"
                style={{ width: `${dataQuality.quoteShare * 100}%` }}
              />
            </div>
            {dataQuality.estimateShare > 0.6 && (
              <p className="text-xs text-amber-600 mt-2">
                Über 60 % der Kosten beruhen auf Schätzungen — die Kostenanalyse
                weist dafür ein erhöhtes Kalkulationsrisiko aus. Verbindliche
                Angebote für die größten Positionen senken es.
              </p>
            )}
          </div>
        )}
      </div>

      {formError && (
        <div className="card-premium bg-amber-950/20 border-amber-700/20 p-4 text-sm text-amber-700">
          {formError}
        </div>
      )}

      {readOnly && (
        <div className="card-premium px-6 py-4 text-sm text-navy-600">
          Nur-Lesen-Zugriff — Kostenpositionen können Sie einsehen, aber nicht ändern.
        </div>
      )}

      {/* Capture form */}
      {!readOnly && (
        <form onSubmit={handleSubmit} className="card-premium px-6 py-5">
          <h3 className="font-sans font-semibold text-navy-900 mb-1 flex items-center gap-2">
            <Euro className="w-4 h-4 text-ocean-500" />
            Kostenposition erfassen
          </h3>
          <p className="text-xs text-navy-600 mb-4">
            Erfasste Positionen sind die Grundlage der Kostenanalyse — ohne sie
            bleibt das Modul ohne Ergebnis. Die Quellenangabe bestimmt, wie
            belastbar das Ergebnis ausgewiesen wird.
          </p>

          <div className="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-3 gap-4 mb-4">
            <div>
              <label htmlFor="cost-category" className="label-premium mb-2 block">
                Kategorie
              </label>
              <select
                id="cost-category"
                value={category}
                onChange={(e) => setCategory(e.target.value)}
                className={INPUT_CLASS}
              >
                {CATEGORIES.map((c) => (
                  <option key={c.value} value={c.value}>
                    {c.label}
                  </option>
                ))}
              </select>
              {categoryHint && <p className="text-xs text-navy-500 mt-1">{categoryHint}</p>}
            </div>

            <div>
              <label htmlFor="cost-subcategory" className="label-premium mb-2 block">
                Unterkategorie (optional)
              </label>
              <input
                id="cost-subcategory"
                type="text"
                value={subcategory}
                onChange={(e) => setSubcategory(e.target.value)}
                maxLength={100}
                placeholder="z.B. Teakdeck"
                className={INPUT_CLASS}
              />
            </div>

            <div>
              <label htmlFor="cost-zone" className="label-premium mb-2 block">
                Zone (optional)
              </label>
              <input
                id="cost-zone"
                type="text"
                value={zoneName}
                onChange={(e) => setZoneName(e.target.value)}
                maxLength={100}
                list={zoneOptions.length > 0 ? 'cost-zone-options' : undefined}
                placeholder={zoneOptions.length > 0 ? 'Zone wählen oder eintippen' : 'z.B. Salon'}
                className={INPUT_CLASS}
              />
              {zoneOptions.length > 0 && (
                <datalist id="cost-zone-options">
                  {zoneOptions.map((z) => (
                    <option key={z} value={z} />
                  ))}
                </datalist>
              )}
              <p className="text-xs text-navy-500 mt-1">
                Ermöglicht die Aufschlüsselung nach Zone.
              </p>
            </div>

            <div className="sm:col-span-2 lg:col-span-3">
              <label htmlFor="cost-description" className="label-premium mb-2 block">
                Bezeichnung (optional)
              </label>
              <input
                id="cost-description"
                type="text"
                value={description}
                onChange={(e) => setDescription(e.target.value)}
                maxLength={1000}
                placeholder="z.B. Teakdeck Cockpit, 12 mm, verlegt"
                className={INPUT_CLASS}
              />
            </div>

            <div>
              <label htmlFor="cost-quantity" className="label-premium mb-2 block">
                Menge
              </label>
              <input
                id="cost-quantity"
                type="text"
                inputMode="decimal"
                value={quantity}
                onChange={(e) => setQuantity(e.target.value)}
                placeholder="z.B. 12,5"
                className={INPUT_CLASS}
              />
            </div>

            <div>
              <label htmlFor="cost-unit" className="label-premium mb-2 block">
                Einheit
              </label>
              <select
                id="cost-unit"
                value={unit}
                onChange={(e) => setUnit(e.target.value)}
                className={INPUT_CLASS}
              >
                {UNITS.map((u) => (
                  <option key={u.value} value={u.value}>
                    {u.label}
                  </option>
                ))}
              </select>
            </div>

            <div>
              <label htmlFor="cost-unit-price" className="label-premium mb-2 block">
                Einzelpreis (€)
              </label>
              <input
                id="cost-unit-price"
                type="text"
                inputMode="decimal"
                value={unitCost}
                onChange={(e) => setUnitCost(e.target.value)}
                placeholder="z.B. 320,00"
                className={INPUT_CLASS}
              />
            </div>

            <div className="sm:col-span-2">
              <label htmlFor="cost-total" className="label-premium mb-2 block">
                Gesamtpreis (€)
              </label>
              <input
                id="cost-total"
                type="text"
                inputMode="decimal"
                value={totalCost}
                onChange={(e) => {
                  setTotalTouched(true)
                  setTotalCost(e.target.value)
                }}
                placeholder="wird berechnet"
                className={INPUT_CLASS}
              />
              <div className="flex flex-wrap items-center gap-3 mt-1">
                <p className="text-xs text-navy-500">
                  {totalTouched
                    ? 'Manuell gesetzt (z.B. Pauschale oder Rabatt).'
                    : 'Berechnet aus Menge × Einzelpreis — überschreibbar.'}
                </p>
                {totalTouched && (
                  <button
                    type="button"
                    onClick={() => setTotalTouched(false)}
                    className="text-xs text-ocean-600 underline hover:text-ocean-500"
                  >
                    Neu berechnen
                  </button>
                )}
              </div>
              {totalDiffers && computedTotal != null && (
                <p className="text-xs text-amber-600 mt-1">
                  Weicht von Menge × Einzelpreis ({formatCurrency(computedTotal)}) ab — wird
                  so übernommen.
                </p>
              )}
            </div>

            <div>
              <label htmlFor="cost-source" className="label-premium mb-2 block">
                Quelle / Datengüte
              </label>
              <select
                id="cost-source"
                value={source}
                onChange={(e) => setSource(e.target.value)}
                className={INPUT_CLASS}
              >
                {SOURCES.map((s) => (
                  <option key={s.value} value={s.value}>
                    {s.label}
                  </option>
                ))}
              </select>
              {sourceHint && <p className="text-xs text-navy-500 mt-1">{sourceHint}</p>}
            </div>

            <div className="sm:col-span-2 lg:col-span-3">
              <label htmlFor="cost-notes" className="label-premium mb-2 block">
                Notiz (optional)
              </label>
              <textarea
                id="cost-notes"
                value={notes}
                onChange={(e) => setNotes(e.target.value)}
                maxLength={2000}
                rows={2}
                placeholder="z.B. Angebot Nr. 2026-114, gültig bis 30.09."
                className={INPUT_CLASS}
              />
            </div>
          </div>

          <div className="flex flex-wrap items-center gap-3">
            <button
              type="submit"
              disabled={saving || unitCost.trim() === '' || totalCost.trim() === ''}
              className="flex items-center gap-2 bg-ocean-700 hover:bg-ocean-600 disabled:opacity-50 disabled:cursor-not-allowed text-navy-900 px-5 py-2.5 rounded-lg text-sm font-medium transition-all duration-200"
            >
              {saving ? <Loader2 className="w-4 h-4 animate-spin" /> : <Plus className="w-4 h-4" />}
              Erfassen
            </button>
            <span className="text-xs text-navy-500">
              Neue Positionen wirken sich erst auf das Modulergebnis aus, wenn die
              Kostenanalyse erneut ausgeführt wird.
            </span>
          </div>
        </form>
      )}

      {/* Breakdown */}
      {itemCount > 0 && (
        <>
          <div className="flex gap-1 card-premium p-1">
            {(['category', 'zone'] as const).map((t) => (
              <button
                key={t}
                onClick={() => setActiveTab(t)}
                className={`flex-1 py-2 rounded-lg text-xs font-sans font-semibold uppercase tracking-wider-premium transition-all duration-200 ${
                  activeTab === t
                    ? 'bg-ocean-700 text-navy-900'
                    : 'text-navy-600 hover:text-navy-900'
                }`}
              >
                {t === 'category' ? 'Nach Kategorie' : 'Nach Zone'}
              </button>
            ))}
          </div>

          {activeTab === 'category' && (
            <div className="card-premium p-6 space-y-4">
              <h3 className="font-sans font-semibold text-navy-900">
                Aufschlüsselung nach Kategorie
              </h3>
              {categoryEntries.length === 0 ? (
                <p className="text-navy-600 text-xs">Keine Kategoriedaten verfügbar</p>
              ) : (
                <div className="space-y-4">
                  {categoryEntries.map(([cat, val], i) => (
                    <BreakdownBar
                      key={cat}
                      label={CATEGORY_LABELS[cat] ?? cat}
                      value={val}
                      total={totalCostSum}
                      colorClass={CATEGORY_COLORS[i % CATEGORY_COLORS.length]}
                    />
                  ))}
                </div>
              )}
            </div>
          )}

          {activeTab === 'zone' && (
            <div className="card-premium p-6 space-y-4">
              <h3 className="font-sans font-semibold text-navy-900">Aufschlüsselung nach Zone</h3>
              {zoneEntries.length === 0 ? (
                <p className="text-navy-600 text-xs">
                  Keine Zonendaten verfügbar — Positionen ohne Zonenangabe erscheinen hier nicht.
                </p>
              ) : (
                <div className="space-y-4">
                  {zoneEntries.map(([zone, val], i) => (
                    <BreakdownBar
                      key={zone}
                      label={zone}
                      value={val}
                      total={totalCostSum}
                      colorClass={CATEGORY_COLORS[i % CATEGORY_COLORS.length]}
                    />
                  ))}
                </div>
              )}
            </div>
          )}
        </>
      )}

      {/* Item list */}
      <div>
        <p className="label-premium mb-4">Kostenpositionen ({items.length})</p>
        {items.length === 0 ? (
          <div className="card-premium px-8 py-10 text-center space-y-2">
            <p className="text-navy-600 text-sm font-medium">
              Noch keine Kostenpositionen erfasst
            </p>
            <p className="text-navy-500 text-xs max-w-md mx-auto">
              {readOnly
                ? 'Ohne erfasste Positionen bleibt die Kostenanalyse ohne Ergebnis.'
                : 'Erfassen Sie Material-, Arbeits- und Ausrüstungskosten über das Formular oben — erst dann liefert die Kostenanalyse ein Ergebnis statt der Meldung „Keine Kostenpositionen vorhanden“.'}
            </p>
          </div>
        ) : (
          <ul className="space-y-2">
            {items.map((item) => (
              <li
                key={item.id}
                className="card-premium px-5 py-3 flex items-start justify-between gap-3 text-sm"
              >
                <div className="min-w-0">
                  <div className="flex flex-wrap items-center gap-2">
                    <span className="text-navy-900 font-medium">
                      {item.description ||
                        item.subcategory ||
                        CATEGORY_LABELS[item.category] ||
                        item.category}
                    </span>
                    <SourceBadge source={item.source} />
                  </div>
                  <p className="text-xs text-navy-600 mt-0.5">
                    {CATEGORY_LABELS[item.category] ?? item.category}
                    {item.subcategory ? ` · ${item.subcategory}` : ''}
                    {item.zone_name ? ` · ${item.zone_name}` : ''}
                    {' · '}
                    {formatQuantity(item.quantity)} {UNIT_LABELS[item.unit] ?? item.unit} ×{' '}
                    {formatCurrency(item.unit_cost_eur)}
                  </p>
                  {item.notes && (
                    <p className="text-xs text-navy-500 mt-0.5 truncate">{item.notes}</p>
                  )}
                </div>
                <div className="flex items-center gap-3 flex-shrink-0">
                  <span className="font-mono text-sm font-semibold text-navy-900">
                    {formatCurrency(item.total_cost_eur)}
                  </span>
                  {!readOnly && (
                    <button
                      onClick={() => handleDelete(item)}
                      disabled={deletingId !== null}
                      aria-label="Kostenposition löschen"
                      className="p-1.5 rounded text-navy-500 hover:text-red-600 hover:bg-red-50 transition-colors disabled:opacity-50"
                    >
                      {deletingId === item.id ? (
                        <Loader2 className="w-4 h-4 animate-spin" />
                      ) : (
                        <Trash2 className="w-4 h-4" />
                      )}
                    </button>
                  )}
                </div>
              </li>
            ))}
          </ul>
        )}
      </div>
    </div>
  )
}
