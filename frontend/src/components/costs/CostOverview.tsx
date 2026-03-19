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
      <div className="flex justify-between text-sm mb-1">
        <span className="text-navy-300">{label}</span>
        <div className="text-right">
          <span className="font-mono text-white">{formatCurrency(value)}</span>
          <span className="text-navy-500 text-xs ml-2">({pct.toFixed(1)} %)</span>
        </div>
      </div>
      <div className="h-2 bg-navy-800 rounded-full overflow-hidden">
        <div
          className={`h-full rounded-full transition-all duration-700 ${colorClass}`}
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
    return <div className="text-navy-400">Lade Kostendaten...</div>
  }

  if (error) {
    return (
      <div className="bg-red-900/50 border border-red-700 rounded-lg p-4 text-red-300 text-sm">
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
      <div className="bg-navy-900 border border-navy-700 rounded-xl p-6 text-center">
        <p className="text-sm text-navy-400 mb-2">Geschätzte Gesamtkosten</p>
        <p className="font-mono text-4xl font-bold text-white mb-1">
          {formatCurrency(summary.total_cost)}
        </p>
        <p className="text-xs text-navy-500">
          {summary.item_count} Kostenpositionen
        </p>
      </div>

      {/* Tabs */}
      <div className="flex gap-1 bg-navy-900 border border-navy-700 rounded-xl p-1">
        {(['category', 'zone'] as const).map((t) => (
          <button
            key={t}
            onClick={() => setActiveTab(t)}
            className={`flex-1 py-2 rounded-lg text-sm font-medium transition-colors ${
              activeTab === t ? 'bg-ocean-700 text-white' : 'text-navy-400 hover:text-white'
            }`}
          >
            {t === 'category' ? 'Nach Kategorie' : 'Nach Zone'}
          </button>
        ))}
      </div>

      {/* Category breakdown */}
      {activeTab === 'category' && (
        <div className="bg-navy-900 border border-navy-700 rounded-xl p-5 space-y-4">
          <h3 className="font-display font-semibold text-white">Aufschlüsselung nach Kategorie</h3>
          {categoryEntries.length === 0 ? (
            <p className="text-navy-400 text-sm">Keine Kategoriedaten verfügbar</p>
          ) : (
            <div className="space-y-3">
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
        <div className="bg-navy-900 border border-navy-700 rounded-xl p-5 space-y-4">
          <h3 className="font-display font-semibold text-white">Aufschlüsselung nach Zone</h3>
          {zoneEntries.length === 0 ? (
            <p className="text-navy-400 text-sm">Keine Zonendaten verfügbar</p>
          ) : (
            <div className="space-y-3">
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
