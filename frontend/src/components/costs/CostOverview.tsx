import { useEffect, useState } from 'react'
import { getCostSummary } from '../../services/api'
import type { CostSummary } from '../../types'

interface CostOverviewProps {
  projectId: string
  layoutId: string
}

function formatCurrency(value: number): string {
  return value.toLocaleString('de-DE', { style: 'currency', currency: 'EUR', maximumFractionDigits: 0 })
}

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
          <span className="font-mono text-sm font-semibold text-navy-900">{formatCurrency(value)}</span>
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

export default function CostOverview({ projectId, layoutId }: CostOverviewProps) {
  const [summary, setSummary] = useState<CostSummary | null>(null)
  const [loading, setLoading] = useState(true)
  const [error, setError] = useState<string | null>(null)
  const [isEmpty, setIsEmpty] = useState(false)
  const [activeTab, setActiveTab] = useState<'category' | 'zone'>('category')

  useEffect(() => {
    setLoading(true)
    setError(null)
    setIsEmpty(false)
    getCostSummary(projectId, layoutId)
      .then(setSummary)
      .catch((e: Error & { status?: number }) => {
        if (e.status === 404) {
          setIsEmpty(true)
        } else {
          setError(e.message)
        }
      })
      .finally(() => setLoading(false))
  }, [projectId, layoutId])

  if (loading) {
    return (
      <div className="flex items-center gap-2 text-navy-600 text-xs font-sans font-semibold uppercase tracking-wider-premium">
        <div className="w-1.5 h-1.5 rounded-full bg-navy-400 animate-pulse"></div>
        Lade Kostendaten
      </div>
    )
  }

  if (error) {
    return (
      <div className="card-premium border-red-500/30 bg-red-500/5 p-4 text-red-300 text-xs">
        Fehler beim Laden: {error}
      </div>
    )
  }

  if (isEmpty || !summary) {
    return (
      <div className="card-premium p-8 text-center space-y-3">
        <div className="w-12 h-12 rounded-full bg-navy-800/30 flex items-center justify-center mx-auto">
          <span className="text-2xl">💰</span>
        </div>
        <p className="text-navy-600 text-sm font-medium">Noch keine Kostendaten vorhanden</p>
        <p className="text-navy-500 text-xs max-w-sm mx-auto">
          Kostendaten werden nach einer Vollanalyse oder manueller Kosteneingabe hier angezeigt.
        </p>
      </div>
    )
  }

  const categoryEntries = Object.entries(summary.breakdown_by_category).sort(
    ([, a], [, b]) => b - a
  )
  const zoneEntries = Object.entries(summary.breakdown_by_zone).sort(([, a], [, b]) => b - a)

  return (
    <div className="space-y-6">
      {/* Total cost hero */}
      <div className="card-premium p-6 text-center">
        <p className="label-premium mb-3">Geschätzte Gesamtkosten</p>
        <p className="font-mono text-4xl font-bold text-navy-900 mb-2">
          {formatCurrency(summary.total_cost)}
        </p>
        <p className="text-xs text-navy-500">
          {summary.item_count} Kostenpositionen
        </p>
      </div>

      {/* Tabs */}
      <div className="flex gap-1 card-premium p-1">
        {(['category', 'zone'] as const).map((t) => (
          <button
            key={t}
            onClick={() => setActiveTab(t)}
            className={`flex-1 py-2 rounded-lg text-xs font-sans font-semibold uppercase tracking-wider-premium transition-all duration-200 ${
              activeTab === t ? 'bg-ocean-700 text-navy-900' : 'text-navy-600 hover:text-navy-600'
            }`}
          >
            {t === 'category' ? 'Nach Kategorie' : 'Nach Zone'}
          </button>
        ))}
      </div>

      {/* Category breakdown */}
      {activeTab === 'category' && (
        <div className="card-premium p-6 space-y-4">
          <h3 className="font-sans font-semibold text-navy-900">Aufschlüsselung nach Kategorie</h3>
          {categoryEntries.length === 0 ? (
            <p className="text-navy-600 text-xs">Keine Kategoriedaten verfügbar</p>
          ) : (
            <div className="space-y-4">
              {categoryEntries.map(([cat, val], i) => (
                <BreakdownBar
                  key={cat}
                  label={cat}
                  value={val}
                  total={summary.total_cost}
                  colorClass={CATEGORY_COLORS[i % CATEGORY_COLORS.length]}
                />
              ))}
            </div>
          )}
        </div>
      )}

      {/* Zone breakdown */}
      {activeTab === 'zone' && (
        <div className="card-premium p-6 space-y-4">
          <h3 className="font-sans font-semibold text-navy-900">Aufschlüsselung nach Zone</h3>
          {zoneEntries.length === 0 ? (
            <p className="text-navy-600 text-xs">Keine Zonendaten verfügbar</p>
          ) : (
            <div className="space-y-4">
              {zoneEntries.map(([zone, val], i) => (
                <BreakdownBar
                  key={zone}
                  label={zone}
                  value={val}
                  total={summary.total_cost}
                  colorClass={CATEGORY_COLORS[i % CATEGORY_COLORS.length]}
                />
              ))}
            </div>
          )}
        </div>
      )}
    </div>
  )
}
