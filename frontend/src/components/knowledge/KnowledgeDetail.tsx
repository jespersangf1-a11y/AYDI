import { AlertTriangle, AlertCircle, Info, CheckCircle, TrendingDown, Wrench, X } from 'lucide-react'
import type { KnowledgeDetail, ManufacturerIssue } from '../../types'

interface KnowledgeDetailProps {
  data: KnowledgeDetail
  onClose: () => void
}

export default function KnowledgeDetailPanel({ data, onClose }: KnowledgeDetailProps) {
  const getSeverityIcon = (severity: string) => {
    switch (severity) {
      case 'critical':
        return <AlertTriangle className="w-5 h-5 text-red-400" />
      case 'warning':
        return <AlertCircle className="w-5 h-5 text-amber-400" />
      case 'info':
        return <Info className="w-5 h-5 text-blue-400" />
      default:
        return <Info className="w-5 h-5 text-navy-400" />
    }
  }

  const getSeverityColor = (severity: string) => {
    switch (severity) {
      case 'critical':
        return 'bg-red-950/30 border-red-700/30'
      case 'warning':
        return 'bg-amber-950/30 border-amber-700/30'
      case 'info':
        return 'bg-blue-950/30 border-blue-700/30'
      default:
        return 'bg-navy-900/30 border-navy-700/30'
    }
  }

  return (
    <div className="fixed inset-0 z-50 flex items-center justify-center bg-black/50 backdrop-blur-sm">
      <div className="w-full max-w-2xl mx-4 max-h-[90vh] bg-navy-900/95 border border-navy-700/50 rounded-xl shadow-2xl overflow-hidden flex flex-col">
        {/* Header */}
        <div className="flex items-start justify-between p-8 border-b border-navy-700/30">
          <div className="flex-1 pr-4">
            <p className="label-premium mb-2">
              {data.category_name}
              {data.subcategory_name && ` / ${data.subcategory_name}`}
            </p>
            <h2 className="font-serif text-2xl font-medium text-white">{data.title}</h2>
          </div>
          <button
            onClick={onClose}
            className="text-navy-400 hover:text-ocean-300 transition-colors duration-200 flex-shrink-0"
            aria-label="Schließen"
          >
            <X className="w-6 h-6" />
          </button>
        </div>

        {/* Content */}
        <div className="flex-1 overflow-y-auto px-8 py-6 space-y-8">
          {/* Description */}
          <div>
            <h3 className="label-premium mb-3">ÜBERSICHT</h3>
            <p className="text-navy-200 leading-relaxed">{data.description}</p>
          </div>

          {/* HTML Content */}
          {data.content_html && (
            <div className="prose prose-invert max-w-none">
              <div
                className="text-navy-200 space-y-4"
                dangerouslySetInnerHTML={{ __html: data.content_html }}
              />
            </div>
          )}

          {/* Material Properties */}
          {data.material_properties && data.material_properties.length > 0 && (
            <div>
              <h3 className="label-premium mb-4">MATERIALEIGENSCHAFTEN</h3>
              <div className="overflow-x-auto">
                <table className="w-full text-sm">
                  <thead>
                    <tr className="border-b border-navy-700/40">
                      <th className="text-left px-4 py-3 label-premium font-semibold">Eigenschaft</th>
                      <th className="text-left px-4 py-3 label-premium font-semibold">Wert</th>
                      <th className="text-left px-4 py-3 label-premium font-semibold">Einheit</th>
                      <th className="text-left px-4 py-3 label-premium font-semibold">Typischer Bereich</th>
                    </tr>
                  </thead>
                  <tbody>
                    {data.material_properties.map((prop, idx) => (
                      <tr
                        key={idx}
                        className={`border-b border-navy-700/20 ${
                          idx % 2 === 0 ? 'bg-navy-900/20' : 'bg-transparent'
                        }`}
                      >
                        <td className="px-4 py-3 text-white font-medium">{prop.name}</td>
                        <td className="px-4 py-3 font-mono text-ocean-300">
                          {typeof prop.value === 'number' ? prop.value.toFixed(2) : prop.value}
                        </td>
                        <td className="px-4 py-3 text-navy-400 text-sm">{prop.unit ?? ''}</td>
                        <td className="px-4 py-3 text-navy-400 text-sm">
                          {prop.typical_range
                            ? `${prop.typical_range.min.toFixed(2)} - ${prop.typical_range.max.toFixed(2)}`
                            : '—'}
                        </td>
                      </tr>
                    ))}
                  </tbody>
                </table>
              </div>
            </div>
          )}

          {/* Degradation Timeline */}
          {data.degradation_data && (
            <div>
              <div className="flex items-center gap-2 mb-4">
                <TrendingDown className="w-5 h-5 text-amber-400" />
                <h3 className="label-premium">DEGRADATIONSZEITLEISTE</h3>
              </div>
              <div className="space-y-4">
                <div className="card-premium p-4">
                  <p className="text-sm text-navy-300 mb-2">
                    <span className="font-medium text-white">Material:</span> {data.degradation_data.material}
                  </p>
                  <p className="text-sm text-navy-300 mb-2">
                    <span className="font-medium text-white">Umgebung:</span> {data.degradation_data.environment}
                  </p>
                  <p className="text-sm text-navy-300">
                    <span className="font-medium text-white">Erwartete Lebensdauer:</span>{' '}
                    {data.degradation_data.expected_lifespan_years} Jahre
                  </p>
                </div>

                {/* Timeline visualization */}
                <div className="space-y-2">
                  {data.degradation_data.datapoints.map((point, idx) => (
                    <div key={idx} className="flex items-center gap-4">
                      <div className="w-16 text-sm font-mono text-navy-400">
                        Jahr {point.timepoint_years}
                      </div>
                      <div className="flex-1 bg-navy-800/40 rounded-full h-2 overflow-hidden">
                        <div
                          className="h-full bg-gradient-to-r from-green-600 via-amber-500 to-red-600"
                          style={{ width: `${point.condition_percentage}%` }}
                        />
                      </div>
                      <div className="w-16 text-right text-sm font-mono text-ocean-300">
                        {point.condition_percentage}%
                      </div>
                    </div>
                  ))}
                </div>

                {/* Maintenance plan */}
                {data.degradation_data.maintenance_plan && (
                  <div className="mt-4">
                    <p className="label-premium mb-2">WARTUNGSPLAN</p>
                    <ul className="space-y-1.5">
                      {data.degradation_data.maintenance_plan.map((item, idx) => (
                        <li key={idx} className="flex items-start gap-2 text-sm text-navy-200">
                          <CheckCircle className="w-4 h-4 text-green-500 mt-0.5 flex-shrink-0" />
                          <span>{item}</span>
                        </li>
                      ))}
                    </ul>
                  </div>
                )}
              </div>
            </div>
          )}

          {/* Known Issues */}
          {data.related_issues && data.related_issues.length > 0 && (
            <div>
              <div className="flex items-center gap-2 mb-4">
                <AlertTriangle className="w-5 h-5 text-red-400" />
                <h3 className="label-premium">BEKANNTE PROBLEME</h3>
              </div>
              <div className="space-y-3">
                {data.related_issues.map((issue, idx) => (
                  <div key={idx} className={`card-premium border p-4 ${getSeverityColor(issue.severity)}`}>
                    <div className="flex items-start gap-3 mb-2">
                      {getSeverityIcon(issue.severity)}
                      <h4 className="font-medium text-white flex-1">{issue.title}</h4>
                    </div>
                    <p className="text-sm text-navy-200 mb-2">{issue.description}</p>
                    {issue.affected_models && issue.affected_models.length > 0 && (
                      <p className="text-xs text-navy-400 mb-2">
                        <span className="font-medium">Betroffene Modelle:</span> {issue.affected_models.join(', ')}
                      </p>
                    )}
                    {issue.resolution && (
                      <div className="text-xs text-navy-300 bg-navy-900/40 rounded p-2 mb-2">
                        <p className="font-medium text-green-400 mb-1">Lösung:</p>
                        <p>{issue.resolution}</p>
                      </div>
                    )}
                    {issue.workaround && (
                      <div className="text-xs text-navy-300 bg-navy-900/40 rounded p-2">
                        <p className="font-medium text-amber-400 mb-1">Workaround:</p>
                        <p>{issue.workaround}</p>
                      </div>
                    )}
                  </div>
                ))}
              </div>
            </div>
          )}

          {/* Cost Impact */}
          {data.cost_impact && (
            <div>
              <h3 className="label-premium mb-3">KOSTENFOLGEN</h3>
              <div className="card-premium p-4">
                <p className="text-sm text-navy-300">
                  Geschätzter Kostenbereich: <span className="font-mono text-ocean-300 font-medium">
                    {data.cost_impact.low.toFixed(0)} € - {data.cost_impact.high.toFixed(0)} €
                  </span>
                </p>
              </div>
            </div>
          )}

          {/* Compliance Standards */}
          {data.compliance_standards && data.compliance_standards.length > 0 && (
            <div>
              <h3 className="label-premium mb-3">GELTENDE NORMEN</h3>
              <div className="flex flex-wrap gap-2">
                {data.compliance_standards.map((standard, idx) => (
                  <div
                    key={idx}
                    className="px-3 py-1.5 bg-blue-950/30 border border-blue-700/30 rounded-full text-xs text-blue-300 font-medium"
                  >
                    {standard}
                  </div>
                ))}
              </div>
            </div>
          )}

          {/* Implementation Notes */}
          {data.implementation_notes && (
            <div>
              <div className="flex items-center gap-2 mb-3">
                <Wrench className="w-5 h-5 text-ocean-400" />
                <h3 className="label-premium">IMPLEMENTIERUNGSHINWEISE</h3>
              </div>
              <div className="card-premium p-4 bg-ocean-950/20 border-ocean-700/30">
                <p className="text-navy-200 text-sm leading-relaxed">{data.implementation_notes}</p>
              </div>
            </div>
          )}
        </div>

        {/* Footer */}
        <div className="px-8 py-4 border-t border-navy-700/30 bg-navy-900/20 flex items-center justify-between">
          <p className="text-xs text-navy-500">
            Aktualisiert am {new Date(data.updated_at).toLocaleDateString('de-DE')}
          </p>
          <button
            onClick={onClose}
            className="px-4 py-2 bg-ocean-900/40 hover:bg-ocean-900/60 border border-ocean-700/40 rounded-lg text-sm font-medium text-ocean-300 transition-colors duration-200"
          >
            Schließen
          </button>
        </div>
      </div>
    </div>
  )
}
