import { useEffect, useState } from 'react'
import { AlertCircle, AlertTriangle, Info, CheckCircle, ChevronDown } from 'lucide-react'
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
    bgColor: 'bg-red-50',
    text: 'text-red-700',
    icon: AlertCircle,
  },
  high: {
    label: 'Hoch',
    borderColor: 'border-l-orange-500',
    bgColor: 'bg-orange-50',
    text: 'text-orange-700',
    icon: AlertTriangle,
  },
  medium: {
    label: 'Mittel',
    borderColor: 'border-l-amber-500',
    bgColor: 'bg-amber-50',
    text: 'text-amber-700',
    icon: AlertTriangle,
  },
  low: {
    label: 'Niedrig',
    borderColor: 'border-l-navy-300',
    bgColor: 'bg-transparent',
    text: 'text-navy-600',
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
      className={`inline-flex items-center gap-1 text-xs px-2.5 py-1.5 rounded-md border border-navy-600/30 ${cfg.text} transition-all duration-300 hover:scale-105`}
      aria-label={`Schweregrad: ${cfg.label}`}
    >
      <cfg.icon className="w-3 h-3" />
      {cfg.label}
    </span>
  )
}

function ResolvedBadge() {
  return (
    <span className="inline-flex items-center gap-1 text-xs px-2.5 py-1.5 rounded-md border border-emerald-500/30 text-emerald-700 bg-emerald-50">
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
  const [expandedReportId, setExpandedReportId] = useState<string | null>(null)

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
        subtitle="Berichte über Wartung, Garantie, Umbau und erkannte Probleme mit Schweregradkennzeichnung"
        label="Service"
      />

      <div className="space-y-8 px-4 sm:px-10 py-12">
        {/* Controls */}
        <div className="flex flex-col sm:flex-row items-start sm:items-center justify-between gap-4 sm:gap-6">
          <div className="flex flex-col sm:flex-row items-start sm:items-center gap-4 w-full sm:w-auto">
            <div className="w-full sm:w-auto">
              <p className="label-premium mb-2">KATEGORIE</p>
              <select
                value={categoryFilter}
                onChange={(e) => handleCategoryChange(e.target.value)}
                aria-label="Kategorie filtern"
                className="w-full sm:w-auto bg-sand-50/60 border border-sand-200 rounded-lg px-4 py-2.5 text-navy-900 text-sm focus:outline-none focus:border-ocean-500/60 focus:ring-2 focus:ring-ocean-500/20 transition-all duration-200"
              >
                <option value="">Alle Kategorien</option>
                {categories.map((c) => (
                  <option key={c} value={c}>
                    {c}
                  </option>
                ))}
              </select>
            </div>

            <div className="w-full sm:w-auto">
              <p className="label-premium mb-2">SCHWEREGRAD</p>
              <select
                value={severityFilter}
                onChange={(e) => handleSeverityChange(e.target.value)}
                aria-label="Schweregrad filtern"
                className="w-full sm:w-auto bg-sand-50/60 border border-sand-200 rounded-lg px-4 py-2.5 text-navy-900 text-sm focus:outline-none focus:border-ocean-500/60 focus:ring-2 focus:ring-ocean-500/20 transition-all duration-200"
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
          <div className="text-center py-12 text-navy-600">
            Berichte werden geladen...
          </div>
        )}

        {error && (
          <div className="card-premium bg-red-50 border-red-200 p-6 text-red-700 text-sm">
            Fehler: {error}
          </div>
        )}

        {!loading && !error && reports.length === 0 && (
          <div className="card-premium px-10 py-12 text-center text-navy-600">
            Keine Berichte gefunden
          </div>
        )}

        {!loading && !error && reports.length > 0 && (
          <div className="space-y-4">
            {reports.map((report, idx) => {
              const cfg = SEVERITY_CONFIG[report.severity]
              const isExpanded = expandedReportId === report.id
              return (
                <button
                  key={report.id}
                  onClick={() => setExpandedReportId(isExpanded ? null : report.id)}
                  style={{ animationDelay: `${idx * 60}ms` }}
                  className={`animate-fade-in-up w-full text-left border-l-4 ${cfg.borderColor} border border-sand-200 ${cfg.bgColor} rounded-lg p-6 transition-all duration-300 hover:shadow-lg hover:shadow-sand-200/50 group`}
                  aria-expanded={isExpanded}
                  aria-label={`${report.description} - ${cfg.label}`}
                >
                  <div className="flex items-start justify-between gap-4 mb-3">
                    <div className="flex-1">
                      <p className="text-navy-900 font-medium text-sm leading-snug group-hover:text-ocean-700 transition-colors">
                        {report.description}
                      </p>
                    </div>
                    <div className="flex items-center gap-2 shrink-0">
                      <SeverityBadge severity={report.severity} />
                      {report.resolution && <ResolvedBadge />}
                      {report.root_cause && (
                        <ChevronDown
                          className={`w-4 h-4 text-navy-500 transition-transform duration-300 ${
                            isExpanded ? 'rotate-180' : ''
                          }`}
                        />
                      )}
                    </div>
                  </div>

                  {/* Metadata Grid - Stacked on mobile */}
                  <div className="grid grid-cols-1 sm:grid-cols-2 gap-3 text-xs text-navy-600 pt-3 border-t border-sand-200">
                    <div>
                      <span className="label-premium mr-1">TYP</span>
                      <span className="text-navy-700">
                        {REPORT_TYPE_LABELS[report.report_type] ?? report.report_type}
                      </span>
                    </div>
                    {report.category && (
                      <div>
                        <span className="label-premium mr-1">KATEGORIE</span>
                        <span className="text-navy-700">{report.category}</span>
                      </div>
                    )}
                    {report.zone_type && (
                      <div>
                        <span className="label-premium mr-1">ZONE</span>
                        <span className="text-navy-700">{report.zone_type}</span>
                      </div>
                    )}
                    {report.boat_class && (
                      <div>
                        <span className="label-premium mr-1">KLASSE</span>
                        <span className="text-navy-700">
                          {BOAT_CLASS_LABELS[report.boat_class]}
                        </span>
                      </div>
                    )}
                    {report.cost_eur != null && (
                      <div>
                        <span className="label-premium mr-1">KOSTEN</span>
                        <span className="font-mono text-amber-700">
                          {report.cost_eur.toLocaleString('de-DE', {
                            style: 'currency',
                            currency: 'EUR',
                          })}
                        </span>
                      </div>
                    )}
                    {report.boat_age_months != null && (
                      <div>
                        <span className="label-premium mr-1">BOOTSALTER</span>
                        <span className="font-mono text-navy-700">
                          {report.boat_age_months} Monate
                        </span>
                      </div>
                    )}
                  </div>

                  {/* Expandable Root Cause */}
                  {report.root_cause && isExpanded && (
                    <div className="mt-4 pt-4 border-t border-sand-200 animate-slide-down">
                      <div className="flex items-start gap-2">
                        <AlertTriangle className="w-4 h-4 text-amber-400 flex-shrink-0 mt-0.5" />
                        <div className="flex-1">
                          <p className="label-premium mb-2">URSACHE</p>
                          <p className="text-xs text-navy-600 leading-relaxed">{report.root_cause}</p>
                        </div>
                      </div>
                    </div>
                  )}
                </button>
              )
            })}
          </div>
        )}
      </div>
    </div>
  )
}
