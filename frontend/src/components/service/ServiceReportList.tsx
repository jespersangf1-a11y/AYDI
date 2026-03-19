import { useEffect, useState } from 'react'
import { AlertCircle, AlertTriangle, Info, CheckCircle } from 'lucide-react'
import { getServiceReports } from '../../services/api'
import type { ServiceReport, Severity } from '../../types'
import { BOAT_CLASS_LABELS } from '../../types'

const SEVERITY_CONFIG: Record<
  Severity,
  { label: string; bg: string; border: string; text: string; icon: typeof AlertCircle }
> = {
  critical: {
    label: 'Kritisch',
    bg: 'bg-red-900/30',
    border: 'border-red-800',
    text: 'text-red-300',
    icon: AlertCircle,
  },
  high: {
    label: 'Hoch',
    bg: 'bg-orange-900/30',
    border: 'border-orange-800',
    text: 'text-orange-300',
    icon: AlertTriangle,
  },
  medium: {
    label: 'Mittel',
    bg: 'bg-amber-900/30',
    border: 'border-amber-800',
    text: 'text-amber-300',
    icon: AlertTriangle,
  },
  low: {
    label: 'Niedrig',
    bg: 'bg-navy-800/50',
    border: 'border-navy-700',
    text: 'text-navy-300',
    icon: Info,
  },
}

const REPORT_TYPE_LABELS: Record<string, string> = {
  warranty: 'Garantie',
  maintenance: 'Wartung',
  refit: 'Umbau',
  complaint: 'Reklamation',
  feedback: 'Feedback',
}

function SeverityBadge({ severity }: { severity: Severity }) {
  const cfg = SEVERITY_CONFIG[severity]
  return (
    <span
      className={`inline-flex items-center gap-1 text-xs px-2 py-0.5 rounded-full border ${cfg.bg} ${cfg.border} ${cfg.text}`}
    >
      <cfg.icon className="w-3 h-3" />
      {cfg.label}
    </span>
  )
}

function ResolvedBadge() {
  return (
    <span className="inline-flex items-center gap-1 text-xs px-2 py-0.5 rounded-full border bg-emerald-900/30 border-emerald-800 text-emerald-300">
      <CheckCircle className="w-3 h-3" />
      Behoben
    </span>
  )
}

export default function ServiceReportList() {
  const [reports, setReports] = useState<ServiceReport[]>([])
  const [loading, setLoading] = useState(true)
  const [error, setError] = useState<string | null>(null)
  const [categoryFilter, setCategoryFilter] = useState('')
  const [severityFilter, setSeverityFilter] = useState('')
  const [categories, setCategories] = useState<string[]>([])

  const fetchReports = (cat?: string, sev?: string) => {
    setLoading(true)
    getServiceReports({ category: cat || undefined, severity: sev || undefined })
      .then((data) => {
        setReports(data)
        if (!cat && !sev) {
          const cats = Array.from(new Set(data.map((r) => r.category))).sort()
          setCategories(cats)
        }
      })
      .catch((e) => setError(e.message))
      .finally(() => setLoading(false))
  }

  useEffect(() => {
    fetchReports()
  }, [])

  const handleCategoryChange = (cat: string) => {
    setCategoryFilter(cat)
    fetchReports(cat, severityFilter)
  }

  const handleSeverityChange = (sev: string) => {
    setSeverityFilter(sev)
    fetchReports(categoryFilter, sev)
  }

  return (
    <div className="space-y-4">
      <div className="flex items-center justify-between">
        <h2 className="font-display text-2xl font-bold text-white">Serviceberichte</h2>
        <div className="flex items-center gap-3">
          <select
            value={categoryFilter}
            onChange={(e) => handleCategoryChange(e.target.value)}
            className="bg-navy-800 border border-navy-600 rounded-lg px-3 py-2 text-white text-sm focus:outline-none focus:border-ocean-500 transition-colors"
          >
            <option value="">Alle Kategorien</option>
            {categories.map((c) => (
              <option key={c} value={c}>
                {c}
              </option>
            ))}
          </select>
          <select
            value={severityFilter}
            onChange={(e) => handleSeverityChange(e.target.value)}
            className="bg-navy-800 border border-navy-600 rounded-lg px-3 py-2 text-white text-sm focus:outline-none focus:border-ocean-500 transition-colors"
          >
            <option value="">Alle Schweregrade</option>
            <option value="critical">Kritisch</option>
            <option value="high">Hoch</option>
            <option value="medium">Mittel</option>
            <option value="low">Niedrig</option>
          </select>
        </div>
      </div>

      {loading && <div className="text-navy-400">Lade Berichte...</div>}

      {error && (
        <div className="bg-red-900/50 border border-red-700 rounded-lg p-4 text-red-300 text-sm">
          Fehler: {error}
        </div>
      )}

      {!loading && !error && reports.length === 0 && (
        <div className="bg-navy-900 border border-navy-700 rounded-xl p-8 text-center text-navy-400">
          Keine Berichte gefunden
        </div>
      )}

      <div className="space-y-3">
        {reports.map((report) => {
          const cfg = SEVERITY_CONFIG[report.severity]
          return (
            <div
              key={report.id}
              className={`${cfg.bg} border ${cfg.border} rounded-xl p-4`}
            >
              <div className="flex items-start justify-between gap-4 mb-2">
                <div className="flex-1">
                  <p className="text-white font-medium text-sm leading-snug">
                    {report.description}
                  </p>
                </div>
                <div className="flex items-center gap-2 shrink-0">
                  <SeverityBadge severity={report.severity} />
                  {report.resolution && <ResolvedBadge />}
                </div>
              </div>

              <div className="flex flex-wrap gap-x-4 gap-y-1 text-xs text-navy-400">
                <span>
                  Typ:{' '}
                  <span className="text-navy-300">
                    {REPORT_TYPE_LABELS[report.report_type] ?? report.report_type}
                  </span>
                </span>
                {report.category && (
                  <span>
                    Kategorie: <span className="text-navy-300">{report.category}</span>
                  </span>
                )}
                {report.zone_type && (
                  <span>
                    Zone: <span className="text-navy-300">{report.zone_type}</span>
                  </span>
                )}
                {report.boat_class && (
                  <span>
                    Klasse:{' '}
                    <span className="text-navy-300">
                      {BOAT_CLASS_LABELS[report.boat_class]}
                    </span>
                  </span>
                )}
                {report.cost_eur != null && (
                  <span>
                    Kosten:{' '}
                    <span className="font-mono text-amber-300">
                      {report.cost_eur.toLocaleString('de-DE', {
                        style: 'currency',
                        currency: 'EUR',
                      })}
                    </span>
                  </span>
                )}
                {report.boat_age_months != null && (
                  <span>
                    Bootsalter:{' '}
                    <span className="font-mono text-navy-300">
                      {report.boat_age_months} Monate
                    </span>
                  </span>
                )}
              </div>

              {report.root_cause && (
                <p className="mt-2 text-xs text-navy-400">
                  <span className="text-navy-500">Ursache: </span>
                  {report.root_cause}
                </p>
              )}
            </div>
          )
        })}
      </div>
    </div>
  )
}
