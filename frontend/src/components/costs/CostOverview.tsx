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
          <span className="font-mono text-sm font-semibold text-white">{formatCurrency(value)}</span>
          <span className="text-navy-500 text-xs ml-2">({pct.toFixed(1)} %)</span>
        </div>
      </div>
      <div className="h-1.5 bg-navy-800/60 rounded-full overflow-hidden">
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
  const [activeTab, setActiveTab] = useState<'category' | 'zone'>('category')

  useEffect(() => {
    setLoading(true)
    getCostSummary(projectId, layoutId)
      .then(setSummary)
      .catch((e) => setError(e.message))
      .finally(() => setLoading(false))
  }, [projectId, layoutId])

  if (loading) {
    return (
      <div className="flex items-center gap-2 text-navy-400 text-xs font-sans font-semibold uppercase tracking-wider-premium">
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

  if (!summary) return null

  const categoryEntries = Object.entries(summary.breakdown_by_category).sort(
    ([, a], [, b]) => b - a
  )
  const zoneEntries = Object.entries(summary.breakdown_by_zone).sort(([, a], [, b]) => b - a)

  return (
    <div className="space-y-6">
      {/* Total cost hero */}
      <div className="card-premium p-6 text-center">
        <p className="label-premium mb-3">Geschätzte Gesamtkosten</p>
        <p className="font-mono text-4xl font-bold text-white mb-2">
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
              activeTab === t ? 'bg-ocean-700 text-white' : 'text-navy-400 hover:text-navy-200'
            }`}
          >
            {t === 'category' ? 'Nach Kategorie' : 'Nach Zone'}
          </button>
        ))}
      </div>

      {/* Category breakdown */}
      {activeTab === 'category' && (
        <div className="card-premium p-6 space-y-4">
          <h3 className="font-sans font-semibold text-white">Aufschlüsselung nach Kategorie</h3>
          {categoryEntries.length === 0 ? (
            <p className="text-navy-400 text-xs">Keine Kategoriedaten verfügbar</p>
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
          <h3 className="font-sans font-semibold text-white">Aufschlüsselung nach Zone</h3>
          {zoneEntries.length === 0 ? (
            <p className="text-navy-400 text-xs">Keine Zonendaten verfügbar</p>
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
