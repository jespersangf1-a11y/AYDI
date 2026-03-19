import { AlertTriangle, CheckCircle, Clock, SkipForward, XCircle } from 'lucide-react'
import type { FullAnalysisResult, AnalysisModule } from '../../types'
import { ANALYSIS_MODULE_LABELS } from '../../types'
import ConfidenceBadge from './ConfidenceBadge'
import ScoreGauge from './ScoreGauge'

interface FullAnalysisViewProps {
  result: FullAnalysisResult
  onModuleClick?: (module: string) => void
}

function scoreColor(score: number): string {
  if (score >= 80) return 'text-emerald-400'
  if (score >= 60) return 'text-amber-400'
  if (score >= 40) return 'text-orange-400'
  return 'text-red-400'
}

function scoreBorderColor(score: number): string {
  if (score >= 80) return 'border-emerald-500/30'
  if (score >= 60) return 'border-amber-500/30'
  if (score >= 40) return 'border-orange-500/30'
  return 'border-red-500/30'
}

function scoreBgColor(score: number): string {
  if (score >= 80) return 'bg-emerald-500/10'
  if (score >= 60) return 'bg-amber-500/10'
  if (score >= 40) return 'bg-orange-500/10'
  return 'bg-red-500/10'
}

function getModuleLabel(module: string): string {
  return ANALYSIS_MODULE_LABELS[module as AnalysisModule] ?? module
}

function formatTimestamp(iso: string): string {
  try {
    const d = new Date(iso)
    return d.toLocaleString('de-DE', {
      day: '2-digit',
      month: '2-digit',
      year: 'numeric',
      hour: '2-digit',
      minute: '2-digit',
    })
  } catch {
    return iso
  }
}

export default function FullAnalysisView({ result, onModuleClick }: FullAnalysisViewProps) {
  const moduleEntries = Object.entries(result.modules)
  const skippedEntries = Object.entries(result.skipped)
  const errorEntries = Object.entries(result.errors)

  return (
    <div className="space-y-6">
      {/* Header with overall score */}
      <div className="rounded-xl bg-navy-800 border border-navy-700 p-6">
        <div className="flex items-center justify-between">
          <div className="flex items-center gap-6">
            {result.overall_score !== null ? (
              <ScoreGauge score={result.overall_score} label="Gesamtbewertung" size={140} />
            ) : (
              <div className="flex flex-col items-center">
                <div className="flex items-center justify-center w-[140px] h-[140px] rounded-full border-4 border-navy-700">
                  <span className="font-mono text-2xl text-navy-400">--</span>
                </div>
                <span className="mt-2 text-sm font-medium text-navy-300">Gesamtbewertung</span>
              </div>
            )}
            <div className="space-y-2">
              <ConfidenceBadge confidence={result.overall_confidence} />
              <div className="flex items-center gap-1.5 text-sm text-navy-400">
                <Clock className="w-4 h-4" />
                <span>{formatTimestamp(result.executed_at)}</span>
              </div>
            </div>
          </div>
          {/* Summary stats */}
          <div className="flex items-center gap-4 text-sm">
            <div className="flex items-center gap-1.5 text-navy-300">
              <CheckCircle className="w-4 h-4 text-emerald-400" />
              <span>{result.module_count} Module analysiert</span>
            </div>
            {result.skipped_count > 0 && (
              <div className="flex items-center gap-1.5 text-navy-400">
                <SkipForward className="w-4 h-4 text-gray-400" />
                <span>{result.skipped_count} uebersprungen</span>
              </div>
            )}
            {result.error_count > 0 && (
              <div className="flex items-center gap-1.5 text-red-400">
                <XCircle className="w-4 h-4" />
                <span>{result.error_count} Fehler</span>
              </div>
            )}
          </div>
        </div>
      </div>

      {/* Module cards grid */}
      {moduleEntries.length > 0 && (
        <div>
          <h3 className="text-sm font-semibold text-navy-300 uppercase tracking-wider mb-3">
            Analyseergebnisse
          </h3>
          <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-4">
            {moduleEntries.map(([moduleName, analysisResult]) => {
              const score = analysisResult.overall_score
              const confidence =
                (analysisResult.config_used?.confidence as string) ??
                (analysisResult.config_used?.validation_level as string) ??
                'calculated'
              const warningCount = analysisResult.warnings?.length ?? 0
              const criticalCount =
                analysisResult.warnings?.filter((w) => w.severity === 'critical').length ?? 0

              return (
                <button
                  key={moduleName}
                  onClick={() => onModuleClick?.(moduleName)}
                  className={`rounded-lg border p-4 text-left transition-colors hover:bg-navy-700/50 ${scoreBorderColor(score)} ${scoreBgColor(score)}`}
                >
                  <div className="flex items-start justify-between mb-3">
                    <h4 className="text-sm font-semibold text-navy-100">
                      {getModuleLabel(moduleName)}
                    </h4>
                    <span className={`font-mono text-2xl font-bold ${scoreColor(score)}`}>
                      {Math.round(score)}
                    </span>
                  </div>
                  <div className="flex items-center gap-2 mb-2">
                    <ConfidenceBadge confidence={confidence} size="sm" />
                  </div>
                  {warningCount > 0 && (
                    <div className="flex items-center gap-2 text-xs text-navy-400">
                      <AlertTriangle className="w-3 h-3" />
                      <span>
                        {warningCount} Hinweis{warningCount !== 1 ? 'e' : ''}
                        {criticalCount > 0 && (
                          <span className="text-red-400">
                            {' '}({criticalCount} kritisch)
                          </span>
                        )}
                      </span>
                    </div>
                  )}
                </button>
              )
            })}
          </div>
        </div>
      )}

      {/* Skipped modules */}
      {skippedEntries.length > 0 && (
        <div>
          <h3 className="text-sm font-semibold text-navy-400 uppercase tracking-wider mb-3">
            Uebersprungene Module
          </h3>
          <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-4">
            {skippedEntries.map(([moduleName, reason]) => (
              <div
                key={moduleName}
                className="rounded-lg border border-navy-700 bg-navy-800/50 p-4"
              >
                <div className="flex items-center gap-2 mb-2">
                  <SkipForward className="w-4 h-4 text-gray-500" />
                  <h4 className="text-sm font-semibold text-navy-400">
                    {getModuleLabel(moduleName)}
                  </h4>
                </div>
                <p className="text-xs text-navy-500">{reason}</p>
              </div>
            ))}
          </div>
        </div>
      )}

      {/* Error modules */}
      {errorEntries.length > 0 && (
        <div>
          <h3 className="text-sm font-semibold text-red-400 uppercase tracking-wider mb-3">
            Fehlgeschlagene Module
          </h3>
          <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-4">
            {errorEntries.map(([moduleName, errorMsg]) => (
              <div
                key={moduleName}
                className="rounded-lg border border-red-500/30 bg-red-500/10 p-4"
              >
                <div className="flex items-center gap-2 mb-2">
                  <XCircle className="w-4 h-4 text-red-400" />
                  <h4 className="text-sm font-semibold text-red-300">
                    {getModuleLabel(moduleName)}
                  </h4>
                </div>
                <p className="text-xs text-red-400">{errorMsg}</p>
              </div>
            ))}
          </div>
        </div>
      )}
    </div>
  )
}
