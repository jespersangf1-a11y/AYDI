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

// Animations for results
const resultsAnimationStyles = `
  @keyframes fadeInUp {
    from {
      opacity: 0;
      transform: translateY(20px);
    }
    to {
      opacity: 1;
      transform: translateY(0);
    }
  }

  @keyframes countUp {
    from {
      opacity: 0;
    }
    to {
      opacity: 1;
    }
  }

  @keyframes moduleSlideIn {
    from {
      opacity: 0;
      transform: translateY(16px);
    }
    to {
      opacity: 1;
      transform: translateY(0);
    }
  }

  @keyframes moduleHoverLift {
    0% { transform: translateY(0); }
    100% { transform: translateY(-8px); }
  }

  @keyframes skeletonPulse {
    0%, 100% { opacity: 0.6; }
    50% { opacity: 1; }
  }

  .animate-fade-in-up {
    animation: fadeInUp 0.6s ease-out;
  }

  .animate-module-in {
    animation: moduleSlideIn 0.5s ease-out;
  }

  .module-card-hover {
    transition: all 0.4s cubic-bezier(0.34, 1.56, 0.64, 1);
  }

  .module-card-hover:hover {
    transform: translateY(-8px);
    box-shadow: 0 24px 48px rgba(0, 176, 240, 0.2);
    border-color: rgba(0, 176, 240, 0.4);
  }

  .skeleton-loading {
    animation: skeletonPulse 2s ease-in-out infinite;
  }
`

const CONFIDENCE_LABELS: Record<string, string> = {
  measured: 'Gemessen',
  calculated: 'Berechnet',
  estimated: 'Geschätzt',
  benchmark: 'Benchmark',
}

const CONFIDENCE_STYLES: Record<string, string> = {
  measured: 'bg-emerald-900/50 text-emerald-300 border-emerald-700',
  calculated: 'bg-ocean-900/50 text-ocean-300 border-ocean-700',
  estimated: 'bg-amber-900/50 text-amber-300 border-amber-700',
  benchmark: 'bg-navy-800 text-navy-300 border-navy-600',
}

const SEVERITY_ICONS = {
  critical: XCircle,
  warning: AlertTriangle,
  info: CheckCircle,
}

const SEVERITY_COLORS = {
  critical: 'text-red-400',
  warning: 'text-amber-400',
  info: 'text-ocean-400',
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
        className="bg-navy-900/40 border border-navy-700/40 rounded-xl p-5 opacity-60 backdrop-blur-sm animate-module-in"
        style={{ animationDelay: `${index * 80}ms` }}
      >
        <div className="flex items-start justify-between mb-2">
          <span className="text-sm font-semibold text-navy-400">{label}</span>
          <span className="text-xs px-2.5 py-1 rounded-full bg-navy-800/50 border border-navy-700/50 text-navy-500">
            Level 2+
          </span>
        </div>
        {result.reason && <p className="text-xs text-navy-600 leading-relaxed">{result.reason}</p>}
      </div>
    )
  }

  return (
    <div
      className="module-card-hover bg-navy-900/40 border border-navy-700/40 rounded-xl p-5 backdrop-blur-sm animate-module-in"
      style={{ animationDelay: `${index * 80}ms` }}
    >
      <div className="flex items-start justify-between mb-4">
        <span className="text-sm font-semibold text-white">{label}</span>
        {result.score != null && (
          <span className={`font-mono font-bold text-lg ${scoreColor}`}>
            {Math.round(result.score)}
          </span>
        )}
      </div>

      {/* Score bar with smooth animation */}
      {result.score != null && (
        <div className="h-1.5 bg-navy-800/50 rounded-full overflow-hidden mb-4">
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
              animation: `countUp 1.2s ease-out ${index * 80}ms both`,
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
            const color = SEVERITY_COLORS[sev] ?? 'text-navy-400'
            return (
              <li key={i} className="flex items-start gap-2">
                <Icon className={`w-3.5 h-3.5 mt-0.5 shrink-0 ${color}`} />
                <span className="text-xs text-navy-300 leading-relaxed">{f.finding}</span>
              </li>
            )
          })}
        </ul>
      )}

      {/* Confidence badge */}
      {result.confidence && (
        <div className="mt-4 pt-4 border-t border-navy-700/40">
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
      <style>{resultsAnimationStyles}</style>
      <div className="space-y-8">
        {/* Header */}
        <div className="flex flex-col md:flex-row md:items-start md:justify-between gap-4 animate-fade-in-up">
          <div>
            <p className="text-xs font-semibold tracking-wider-premium uppercase text-navy-400 mb-2">
              Analyseergebnisse
            </p>
            <p className="text-sm text-navy-400">
              <span className="font-mono text-ocean-300">{specs_provided}</span> bereitgestellte Angaben · <span className="font-mono text-navy-300">{specs_inferred}</span> geschätzte Werte
            </p>
          </div>
          <button
            onClick={onNewAnalysis}
            className="flex items-center gap-2 px-5 py-2.5 rounded-lg bg-navy-800/50 border border-navy-700/50 hover:bg-navy-800/70 text-navy-300 text-sm font-medium transition-all duration-200 backdrop-blur-sm hover:shadow-lg active:scale-95"
            aria-label="Neue Analyse starten"
          >
            <RotateCcw className="w-4 h-4" />
            Neu
          </button>
        </div>

        {/* Overall score */}
        <div className="bg-navy-900/40 border border-navy-700/40 rounded-xl p-6 md:p-8 backdrop-blur-sm animate-fade-in-up" style={{ animationDelay: '100ms' }}>
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
              <p className="text-navy-300 text-sm leading-relaxed">{overall_assessment.summary}</p>
            </div>
          </div>
        </div>

        {/* Available modules */}
        {availableModules.length > 0 && (
          <div className="animate-fade-in-up" style={{ animationDelay: '200ms' }}>
            <p className="text-xs font-semibold tracking-wider-premium uppercase text-navy-400 mb-4">
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
