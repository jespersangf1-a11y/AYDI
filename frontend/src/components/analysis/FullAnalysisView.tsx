import { AlertTriangle, CheckCircle, Clock, SkipForward, XCircle } from 'lucide-react'
import { useState, useEffect, useRef } from 'react'
import type { FullAnalysisResult, AnalysisModule } from '../../types'
import { ANALYSIS_MODULE_LABELS } from '../../types'
import ConfidenceBadge from './ConfidenceBadge'
import ScoreGauge from './ScoreGauge'

interface FullAnalysisViewProps {
  result: FullAnalysisResult
  onModuleClick?: (module: string) => void
  isLoading?: boolean
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

// Loading skeleton component
function SkeletonLoader() {
  return (
    <div className="space-y-8">
      {/* Header skeleton */}
      <div className="card-premium p-6 animate-pulse">
        <div className="flex items-center justify-between gap-6">
          <div className="flex items-center gap-6">
            <div className="w-[140px] h-[140px] rounded-full bg-navy-700/30"></div>
            <div className="space-y-3">
              <div className="h-6 w-24 bg-navy-700/30 rounded"></div>
              <div className="h-4 w-32 bg-navy-700/30 rounded"></div>
            </div>
          </div>
          <div className="flex items-center gap-5">
            <div className="h-4 w-40 bg-navy-700/30 rounded"></div>
            <div className="h-4 w-40 bg-navy-700/30 rounded"></div>
          </div>
        </div>
      </div>

      {/* Cards grid skeleton */}
      <div className="space-y-4">
        <div className="h-4 w-24 bg-navy-700/30 rounded animate-pulse"></div>
        <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-5">
          {[...Array(6)].map((_, i) => (
            <div key={i} className="card-premium p-4 animate-pulse">
              <div className="h-6 w-20 bg-navy-700/30 rounded mb-3"></div>
              <div className="h-4 w-32 bg-navy-700/30 rounded mb-3"></div>
              <div className="h-4 w-28 bg-navy-700/30 rounded"></div>
            </div>
          ))}
        </div>
      </div>
    </div>
  )
}

// Module card with scroll-triggered animation
function ModuleCardWithAnimation({
  moduleName,
  analysisResult,
  onModuleClick,
  index,
}: {
  moduleName: string
  analysisResult: any
  onModuleClick?: (module: string) => void
  index: number
}) {
  const [hasAnimated, setHasAnimated] = useState(false)
  const cardRef = useRef<HTMLButtonElement>(null)

  useEffect(() => {
    const observer = new IntersectionObserver(
      ([entry]) => {
        if (entry.isIntersecting) {
          setHasAnimated(true)
          observer.unobserve(entry.target)
        }
      },
      { threshold: 0.1 }
    )

    if (cardRef.current) {
      observer.observe(cardRef.current)
    }

    return () => {
      if (cardRef.current) {
        observer.unobserve(cardRef.current)
      }
    }
  }, [])

  const score = analysisResult.overall_score
  const confidence =
    (analysisResult.config_used?.confidence as string) ??
    (analysisResult.config_used?.validation_level as string) ??
    'calculated'
  const warningCount = analysisResult.warnings?.length ?? 0
  const criticalCount =
    analysisResult.warnings?.filter((w: any) => w.severity === 'critical').length ?? 0

  return (
    <button
      ref={cardRef}
      onClick={() => onModuleClick?.(moduleName)}
      className={`card-premium p-4 text-left transition-all duration-300 group cursor-pointer ${scoreBorderColor(score)} ${scoreBgColor(score)} ${
        hasAnimated
          ? 'opacity-100 translate-y-0 shadow-lg shadow-navy-500/20'
          : 'opacity-0 translate-y-4 shadow-none'
      } hover:shadow-ocean-500/30 hover:shadow-lg hover:-translate-y-1`}
      style={{
        transitionDelay: `${index * 100}ms`,
      }}
    >
      <div className="flex items-start justify-between mb-3">
        <h4 className="text-sm font-sans font-semibold text-navy-900">
          {getModuleLabel(moduleName)}
        </h4>
        <span className={`font-mono text-2xl font-bold ${scoreColor(score)}`}>
          {hasAnimated ? Math.round(score) : '...'}
        </span>
      </div>
      <div className="flex items-center gap-2 mb-3">
        <ConfidenceBadge confidence={confidence} size="sm" />
      </div>
      {warningCount > 0 && (
        <div className="flex items-center gap-2 text-xs text-navy-600">
          <AlertTriangle className="w-3 h-3 flex-shrink-0" />
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
}

export default function FullAnalysisView({
  result,
  onModuleClick,
  isLoading = false,
}: FullAnalysisViewProps) {
  if (isLoading) {
    return <SkeletonLoader />
  }

  const moduleEntries = Object.entries(result.modules)
  const skippedEntries = Object.entries(result.skipped)
  const errorEntries = Object.entries(result.errors)

  return (
    <div className="space-y-8">
      {/* Header with overall score */}
      <div className="card-premium p-6 animate-fadeIn">
        <div className="flex flex-col lg:flex-row items-start lg:items-center justify-between gap-6">
          <div className="flex flex-col sm:flex-row items-start sm:items-center gap-6">
            {result.overall_score !== null ? (
              <ScoreGauge score={result.overall_score} label="Gesamtbewertung" size="md" />
            ) : (
              <div className="flex flex-col items-center">
                <div className="flex items-center justify-center w-[120px] h-[120px] rounded-full border-2 border-navy-700/60">
                  <span className="font-mono text-2xl text-navy-600">--</span>
                </div>
                <span className="mt-3 text-xs font-sans font-semibold uppercase tracking-wider-premium text-navy-700">
                  Gesamtbewertung
                </span>
              </div>
            )}
            <div className="space-y-3">
              <ConfidenceBadge confidence={result.overall_confidence} />
              <div className="flex items-center gap-2 text-xs text-navy-600">
                <Clock className="w-3.5 h-3.5" />
                <span>{formatTimestamp(result.executed_at)}</span>
              </div>
            </div>
          </div>

          {/* Summary stats */}
          <div className="flex flex-wrap items-center gap-3 sm:gap-5 text-xs w-full lg:w-auto">
            <div className="flex items-center gap-2 text-navy-700">
              <CheckCircle className="w-4 h-4 text-emerald-400 flex-shrink-0" />
              <span>{result.module_count} Module analysiert</span>
            </div>
            {result.skipped_count > 0 && (
              <div className="flex items-center gap-2 text-navy-600">
                <SkipForward className="w-4 h-4 text-navy-500 flex-shrink-0" />
                <span>{result.skipped_count} uebersprungen</span>
              </div>
            )}
            {result.error_count > 0 && (
              <div className="flex items-center gap-2 text-red-400">
                <XCircle className="w-4 h-4 flex-shrink-0" />
                <span>{result.error_count} Fehler</span>
              </div>
            )}
          </div>
        </div>
      </div>

      {/* Module cards grid */}
      {moduleEntries.length > 0 && (
        <div className="space-y-4">
          <h3 className="label-premium animate-fadeIn">Analyseergebnisse</h3>
          <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-5">
            {moduleEntries.map(([moduleName, analysisResult], index) => (
              <ModuleCardWithAnimation
                key={moduleName}
                moduleName={moduleName}
                analysisResult={analysisResult}
                onModuleClick={onModuleClick}
                index={index}
              />
            ))}
          </div>
        </div>
      )}

      {/* Divider */}
      {(skippedEntries.length > 0 || errorEntries.length > 0) && moduleEntries.length > 0 && (
        <div className="border-t border-navy-700/30"></div>
      )}

      {/* Skipped modules */}
      {skippedEntries.length > 0 && (
        <div className="space-y-4 animate-fadeIn">
          <h3 className="label-premium">Uebersprungene Module</h3>
          <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-5">
            {skippedEntries.map(([moduleName, reason], index) => (
              <div
                key={moduleName}
                className="card-premium p-4 transition-all duration-300 hover:shadow-lg hover:shadow-navy-500/20 hover:-translate-y-0.5"
                style={{
                  animation: `slideIn 0.4s ease-out ${index * 50}ms both`,
                }}
              >
                <div className="flex items-center gap-2 mb-2">
                  <SkipForward className="w-4 h-4 text-navy-500 flex-shrink-0" />
                  <h4 className="text-sm font-sans font-semibold text-navy-600">
                    {getModuleLabel(moduleName)}
                  </h4>
                </div>
                <p className="text-xs text-navy-500">{reason}</p>
              </div>
            ))}
          </div>
        </div>
      )}

      {/* Divider */}
      {errorEntries.length > 0 && (skippedEntries.length > 0 || moduleEntries.length > 0) && (
        <div className="border-t border-navy-700/30"></div>
      )}

      {/* Error modules */}
      {errorEntries.length > 0 && (
        <div className="space-y-4 animate-fadeIn">
          <h3 className="label-premium text-red-400">Fehlgeschlagene Module</h3>
          <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-5">
            {errorEntries.map(([moduleName, errorMsg], index) => (
              <div
                key={moduleName}
                className="card-premium border-red-500/30 bg-red-500/5 p-4 transition-all duration-300 hover:shadow-lg hover:shadow-red-500/20 hover:-translate-y-0.5"
                style={{
                  animation: `slideIn 0.4s ease-out ${index * 50}ms both`,
                }}
              >
                <div className="flex items-center gap-2 mb-2">
                  <XCircle className="w-4 h-4 text-red-400 flex-shrink-0" />
                  <h4 className="text-sm font-sans font-semibold text-red-300">
                    {getModuleLabel(moduleName)}
                  </h4>
                </div>
                <p className="text-xs text-red-400">{errorMsg}</p>
              </div>
            ))}
          </div>
        </div>
      )}

      <style>{`
        @keyframes slideIn {
          from {
            opacity: 0;
            transform: translateY(10px);
          }
          to {
            opacity: 1;
            transform: translateY(0);
          }
        }

        @keyframes fadeIn {
          from {
            opacity: 0;
          }
          to {
            opacity: 1;
          }
        }

        .animate-fadeIn {
          animation: fadeIn 0.5s ease-out;
        }
      `}</style>
    </div>
  )
}
