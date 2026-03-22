import { useState, useEffect } from 'react'
import { RotateCcw, CheckCircle, AlertTriangle, XCircle } from 'lucide-react'
import type { QuickAnalysisResponse, QuickModuleResult, AnalysisModule } from '../../types'
import { ANALYSIS_MODULE_LABELS } from '../../types'
import ScoreGauge from '../analysis/ScoreGauge'
import UpgradePrompt from './UpgradePrompt'

interface QuickResultsProps {
  result: QuickAnalysisResponse
  onNewAnalysis: () => void
}

const CONFIDENCE_LABELS: Record<string, string> = {
  measured: 'Gemessen',
  calculated: 'Berechnet',
  estimated: 'Geschätzt',
  benchmark: 'Benchmark',
}

const CONFIDENCE_STYLES: Record<string, string> = {
  measured: 'bg-emerald-100 text-emerald-700 border-emerald-300',
  calculated: 'bg-ocean-100 text-ocean-700 border-ocean-300',
  estimated: 'bg-amber-100 text-amber-700 border-amber-300',
  benchmark: 'bg-sand-100 text-navy-700 border-sand-300',
}

const SEVERITY_ICONS = {
  critical: XCircle,
  warning: AlertTriangle,
  info: CheckCircle,
}

const SEVERITY_COLORS = {
  critical: 'text-red-600',
  warning: 'text-amber-600',
  info: 'text-ocean-600',
}

function ModuleCard({ name, result, index = 0 }: { name: string; result: QuickModuleResult; index?: number }) {
  const label = ANALYSIS_MODULE_LABELS[name as AnalysisModule] ?? name
  const scoreColor =
    result.score != null
      ? result.score >= 80
        ? 'text-emerald-400'
        : result.score >= 60
        ? 'text-amber-400'
        : result.score >= 40
        ? 'text-orange-400'
        : 'text-red-400'
      : 'text-navy-500'

  if (!result.available) {
    return (
      <div
        className="bg-sand-50 border border-sand-200 rounded-xl p-5 opacity-70 shadow-sm animate-fade-in-up"
        style={{ animationDelay: `${index * 80}ms` }}
      >
        <div className="flex items-start justify-between mb-2">
          <span className="text-sm font-semibold text-navy-700">{label}</span>
          <span className="text-xs px-2.5 py-1 rounded-full bg-sand-100 border border-sand-300 text-navy-600">
            Level 2+
          </span>
        </div>
        {result.reason && <p className="text-xs text-navy-600 leading-relaxed">{result.reason}</p>}
      </div>
    )
  }

  return (
    <div
      className="card-premium bg-white border border-sand-200 rounded-xl p-5 shadow-sm animate-fade-in-up"
      style={{ animationDelay: `${index * 80}ms` }}
    >
      <div className="flex items-start justify-between mb-4">
        <span className="text-sm font-semibold text-navy-900">{label}</span>
        {result.score != null && (
          <span className={`font-mono font-bold text-lg ${scoreColor}`}>
            {Math.round(result.score)}
          </span>
        )}
      </div>

      {/* Score bar with smooth animation */}
      {result.score != null && (
        <div className="h-1.5 bg-sand-200 rounded-full overflow-hidden mb-4">
          <div
            className={`h-full rounded-full transition-all duration-1000 ease-out ${
              result.score >= 80
                ? 'bg-emerald-400'
                : result.score >= 60
                ? 'bg-amber-400'
                : result.score >= 40
                ? 'bg-orange-400'
                : 'bg-red-400'
            }`}
            style={{
              width: `${result.score}%`,
              animation: `count-up 1.2s ease-out ${index * 80}ms both`,
            }}
          />
        </div>
      )}

      {/* Key findings */}
      {result.key_findings && result.key_findings.length > 0 && (
        <ul className="space-y-2">
          {result.key_findings.slice(0, 3).map((f, i) => {
            const sev = f.severity as keyof typeof SEVERITY_ICONS
            const Icon = SEVERITY_ICONS[sev] ?? CheckCircle
            const color = SEVERITY_COLORS[sev] ?? 'text-navy-600'
            return (
              <li key={i} className="flex items-start gap-2">
                <Icon className={`w-3.5 h-3.5 mt-0.5 shrink-0 ${color}`} />
                <span className="text-xs text-navy-700 leading-relaxed">{f.finding}</span>
              </li>
            )
          })}
        </ul>
      )}

      {/* Confidence badge */}
      {result.confidence && (
        <div className="mt-4 pt-4 border-t border-sand-200">
          <span
            className={`text-xs px-2.5 py-1 rounded-full border ${
              CONFIDENCE_STYLES[result.confidence] ?? CONFIDENCE_STYLES.benchmark
            }`}
          >
            {CONFIDENCE_LABELS[result.confidence] ?? result.confidence}
          </span>
        </div>
      )}
    </div>
  )
}

export default function QuickResults({ result, onNewAnalysis }: QuickResultsProps) {
  const { overall_assessment, modules, upgrade_prompt, specs_provided, specs_inferred } = result
  const [displayedScore, setDisplayedScore] = useState(0)

  const availableModules = Object.entries(modules).filter(([, m]) => m.available)
  const unavailableModules = Object.entries(modules).filter(([, m]) => !m.available)

  // Animate score count-up
  useEffect(() => {
    let animationFrame: number
    const duration = 1200
    const startTime = Date.now()
    const targetScore = overall_assessment.score

    const animate = () => {
      const elapsed = Date.now() - startTime
      const progress = Math.min(elapsed / duration, 1)
      // Easing function for smooth animation
      const easeOutQuad = 1 - (1 - progress) * (1 - progress)
      const currentScore = Math.round(easeOutQuad * targetScore)
      setDisplayedScore(currentScore)

      if (progress < 1) {
        animationFrame = requestAnimationFrame(animate)
      }
    }

    animationFrame = requestAnimationFrame(animate)
    return () => cancelAnimationFrame(animationFrame)
  }, [overall_assessment.score])

  return (
    <>
      <div className="space-y-8">
        {/* Header */}
        <div className="flex flex-col md:flex-row md:items-start md:justify-between gap-4 animate-fade-in-up">
          <div>
            <p className="text-xs font-semibold tracking-wider-premium uppercase text-navy-600 mb-2">
              Analyseergebnisse
            </p>
            <p className="text-sm text-navy-700">
              <span className="font-mono text-ocean-600">{specs_provided}</span> bereitgestellte Angaben · <span className="font-mono text-navy-600">{specs_inferred}</span> geschätzte Werte
            </p>
          </div>
          <button
            onClick={onNewAnalysis}
            className="flex items-center gap-2 px-5 py-2.5 rounded-lg bg-sand-100 border border-sand-300 hover:bg-sand-200 text-navy-700 text-sm font-medium transition-all duration-200 hover:shadow-md active:scale-95"
            aria-label="Neue Analyse starten"
          >
            <RotateCcw className="w-4 h-4" />
            Neu
          </button>
        </div>

        {/* Overall score */}
        <div className="bg-white border border-sand-200 rounded-xl p-6 md:p-8 shadow-sm animate-fade-in-up" style={{ animationDelay: '100ms' }}>
          <div className="flex flex-col md:flex-row md:items-center gap-6 md:gap-8">
            <div className="flex-shrink-0">
              <ScoreGauge score={displayedScore} label="Gesamtbewertung" size={140} />
            </div>
            <div className="flex-1">
              <div className="flex items-center gap-2 mb-3">
                <span
                  className={`text-xs px-2.5 py-1 rounded-full border ${
                    CONFIDENCE_STYLES[overall_assessment.confidence] ?? CONFIDENCE_STYLES.benchmark
                  }`}
                >
                  {CONFIDENCE_LABELS[overall_assessment.confidence] ?? overall_assessment.confidence}
                </span>
              </div>
              <p className="text-navy-700 text-sm leading-relaxed">{overall_assessment.summary}</p>
            </div>
          </div>
        </div>

        {/* Available modules */}
        {availableModules.length > 0 && (
          <div className="animate-fade-in-up" style={{ animationDelay: '200ms' }}>
            <p className="text-xs font-semibold tracking-wider-premium uppercase text-navy-600 mb-4">
              Analysierte Module
            </p>
            <div className="grid gap-4 sm:grid-cols-2 lg:grid-cols-3">
              {availableModules.map(([name, mod], idx) => (
                <ModuleCard key={name} name={name} result={mod} index={idx} />
              ))}
            </div>
          </div>
        )}

        {/* Unavailable modules */}
        {unavailableModules.length > 0 && (
          <div className="animate-fade-in-up" style={{ animationDelay: '300ms' }}>
            <p className="text-xs font-semibold tracking-wider-premium uppercase text-navy-500 mb-4">
              Zusätzliche Module (Level 2+)
            </p>
            <div className="grid gap-4 sm:grid-cols-2 lg:grid-cols-3">
              {unavailableModules.map(([name, mod], idx) => (
                <ModuleCard key={name} name={name} result={mod} index={availableModules.length + idx} />
              ))}
            </div>
          </div>
        )}

        {/* Upgrade prompt */}
        <div className="animate-fade-in-up" style={{ animationDelay: '400ms' }}>
          <UpgradePrompt upgradePrompt={upgrade_prompt} />
        </div>
      </div>
    </>
  )
}
