import { useEffect, useState } from 'react'
import { AlertCircle, AlertTriangle, Info, CheckCircle } from 'lucide-react'
import { getServiceReports } from '../../services/api'
import type { ServiceReport, Severity } from '../../types'
import { BOAT_CLASS_LABELS } from '../../types'
import { MEDIA } from '../../config/media'
import HeroSection from '../layout/HeroSection'

const SEVERITY_CONFIG: Record<
  Severity,
  { label: string; borderColor: string; bgColor: string; text: string; icon: typeof AlertCircle }
> = {
  critical: {
    label: 'Kritisch',
    borderColor: 'border-l-red-500',
    bgColor: 'bg-red-950/10',
    text: 'text-red-300',
    icon: AlertCircle,
  },
  high: {
    label: 'Hoch',
    borderColor: 'border-l-orange-500',
    bgColor: 'bg-orange-950/10',
    text: 'text-orange-300',
    icon: AlertTriangle,
  },
  medium: {
    label: 'Mittel',
    borderColor: 'border-l-amber-500',
    bgColor: 'bg-amber-950/10',
    text: 'text-amber-300',
    icon: AlertTriangle,
  },
  low: {
    label: 'Niedrig',
    borderColor: 'border-l-navy-600',
    bgColor: 'bg-transparent',
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
      className={`inline-flex items-center gap-1 text-xs px-2.5 py-1.5 rounded-md border border-navy-600/30 ${cfg.text}`}
    >
      <cfg.icon className="w-3 h-3" />
      {cfg.label}
    </span>
  )
}

function ResolvedBadge() {
  return (
    <span className="inline-flex items-center gap-1 text-xs px-2.5 py-1.5 rounded-md border border-emerald-500/30 text-emerald-300">
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
    <div>
      <HeroSection
        backgroundImage={MEDIA.structure.hull_drydock}
        title="Serviceberichte"
        subtitle="Berichte ber Wartung, Garantie, Umbau und erkannte Probleme mit Schweregradkennzeichnung"
        label="Service"
      />

      <div className="space-y-8 px-10 py-12">
        {/* Controls */}
        <div className="flex items-center justify-between gap-6">
          <div className="flex items-center gap-4">
            <div>
              <p className="label-premium mb-2">KATEGORIE</p>
              <select
                value={categoryFilter}
                onChange={(e) => handleCategoryChange(e.target.value)}
                className="bg-navy-800/60 border border-navy-600/40 rounded-lg px-4 py-2.5 text-navy-100 text-sm focus:outline-none focus:border-ocean-500/60 transition-colors duration-200"
              >
                <option value="">Alle Kategorien</option>
                {categories.map((c) => (
                  <option key={c} value={c}>
                    {c}
                  </option>
                ))}
              </select>
            </div>

            <div>
              <p className="label-premium mb-2">SCHWEREGARD</p>
              <select
                value={severityFilter}
                onChange={(e) => handleSeverityChange(e.target.value)}
                className="bg-navy-800/60 border border-navy-600/40 rounded-lg px-4 py-2.5 text-navy-100 text-sm focus:outline-none focus:border-ocean-500/60 transition-colors duration-200"
              >
                <option value="">Alle Schweregrade</option>
                <option value="critical">Kritisch</option>
                <option value="high">Hoch</option>
                <option value="medium">Mittel</option>
                <option value="low">Niedrig</option>
              </select>
            </div>
          </div>
        </div>

        {loading && (
          <div className="text-center py-12 text-navy-400">
            Berichte werden geladen...
          </div>
        )}

        {error && (
          <div className="card-premium bg-red-950/20 border-red-700/20 p-6 text-red-300 text-sm">
            Fehler: {error}
          </div>
        )}

        {!loading && !error && reports.length === 0 && (
          <div className="card-premium px-10 py-12 text-center text-navy-400">
            Keine Berichte gefunden
          </div>
        )}

        {!loading && !error && reports.length > 0 && (
          <div className="space-y-4">
            {reports.map((report) => {
              const cfg = SEVERITY_CONFIG[report.severity]
              return (
                <div
                  key={report.id}
                  className={`border-l-4 ${cfg.borderColor} border-r border-b border-navy-700/30 ${cfg.bgColor} rounded-lg p-6 transition-colors duration-200 hover:bg-navy-900/20`}
                >
                  <div className="flex items-start justify-between gap-4 mb-3">
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

                  <div className="grid grid-cols-2 gap-x-6 gap-y-2 text-xs text-navy-400 pt-3 border-t border-navy-700/20">
                    <span>
                      <span className="label-premium mr-1">TYP</span>
                      <span className="text-navy-300">
                        {REPORT_TYPE_LABELS[report.report_type] ?? report.report_type}
                      </span>
                    </span>
                    {report.category && (
                      <span>
                        <span className="label-premium mr-1">KATEGORIE</span>
                        <span className="text-navy-300">{report.category}</span>
                      </span>
                    )}
                    {report.zone_type && (
                      <span>
                        <span className="label-premium mr-1">ZONE</span>
                        <span className="text-navy-300">{report.zone_type}</span>
                      </span>
                    )}
                    {report.boat_class && (
                      <span>
                        <span className="label-premium mr-1">KLASSE</span>
                        <span className="text-navy-300">
                          {BOAT_CLASS_LABELS[report.boat_class]}
                        </span>
                      </span>
                    )}
                    {report.cost_eur != null && (
                      <span>
                        <span className="label-premium mr-1">KOSTEN</span>
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
                        <span className="label-premium mr-1">BOOTSALTER</span>
                        <span className="font-mono text-navy-300">
                          {report.boat_age_months} Monate
                        </span>
                      </span>
                    )}
                  </div>

                  {report.root_cause && (
                    <p className="mt-3 pt-3 border-t border-navy-700/20 text-xs text-navy-300">
                      <span className="label-premium">URSACHE</span> {report.root_cause}
                    </p>
                  )}
                </div>
              )
            })}
          </div>
        )}
      </div>
    </div>
  )
}
