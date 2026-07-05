import { useState } from 'react'
import {
  CheckCircle,
  AlertTriangle,
  Lightbulb,
  ChevronDown,
  ChevronRight,
  Eye,
  EyeOff,
} from 'lucide-react'
import type { ImageAnalysisResult, VisualFinding } from '../../types'
import ConfidenceBadge from '../analysis/ConfidenceBadge'

interface VisualResultsProps {
  result: ImageAnalysisResult
  showLowConfidence?: boolean
}

const ASSESSMENT_STYLES: Record<string, { bg: string; text: string; label: string }> = {
  gut: { bg: 'bg-emerald-500/10', text: 'text-emerald-400', label: 'Gut' },
  akzeptabel: { bg: 'bg-ocean-500/10', text: 'text-ocean-600', label: 'Akzeptabel' },
  mangelhaft: { bg: 'bg-amber-500/10', text: 'text-amber-400', label: 'Mangelhaft' },
  kritisch: { bg: 'bg-red-500/10', text: 'text-red-400', label: 'Kritisch' },
}

function AssessmentBadge({ assessment }: { assessment: string }) {
  const key = assessment.toLowerCase()
  const style = ASSESSMENT_STYLES[key] ?? {
    bg: 'bg-navy-700',
    text: 'text-navy-700',
    label: assessment,
  }
  return (
    <span
      className={`inline-block rounded px-2 py-0.5 text-xs font-medium ${style.bg} ${style.text}`}
    >
      {style.label}
    </span>
  )
}

// Per-finding confidence is the raw AI self-assessment, which the Vision prompts
// emit in German (hoch/mittel/niedrig) or, for materials, sicher/wahrscheinlich/vermutet.
// Match all low-confidence spellings (plus the canonical/English fallbacks) so that
// low-confidence findings are correctly hidden by default, per the confidence framework.
const LOW_CONFIDENCE_TOKENS = new Set([
  'niedrig', 'sehr niedrig', 'vermutet', 'low', 'very low', 'visual_low',
])

function isLowConfidence(confidence: string | null | undefined): boolean {
  return !!confidence && LOW_CONFIDENCE_TOKENS.has(confidence.trim().toLowerCase())
}

function groupFindings(findings: VisualFinding[]): Record<string, VisualFinding[]> {
  const groups: Record<string, VisualFinding[]> = {}
  for (const f of findings) {
    const cat = f.category || 'Allgemein'
    if (!groups[cat]) groups[cat] = []
    groups[cat].push(f)
  }
  return groups
}

function ScoreBar({ label, score }: { label: string; score: number }) {
  const color =
    score >= 80 ? 'bg-emerald-400' : score >= 60 ? 'bg-amber-400' : score >= 40 ? 'bg-orange-400' : 'bg-red-400'

  return (
    <div className="space-y-1">
      <div className="flex items-center justify-between text-xs">
        <span className="text-navy-700">{label}</span>
        <span className="font-mono text-navy-600">{Math.round(score)}</span>
      </div>
      <div className="h-2 rounded-full bg-sand-50">
        <div
          className={`h-full rounded-full transition-all duration-700 ${color}`}
          style={{ width: `${Math.min(score, 100)}%` }}
        />
      </div>
    </div>
  )
}

export default function VisualResults({
  result,
  showLowConfidence: initialShowLow = false,
}: VisualResultsProps) {
  const [showLow, setShowLow] = useState(initialShowLow)
  const [cannotAssessOpen, setCannotAssessOpen] = useState(false)

  const visibleFindings = showLow
    ? result.findings
    : result.findings.filter((f) => !isLowConfidence(f.confidence))

  const grouped = groupFindings(visibleFindings)
  const hasLowConfidence = result.findings.some((f) => isLowConfidence(f.confidence))

  return (
    <div className="space-y-6">
      {/* Header: confidence + quality */}
      <div className="flex items-center gap-3 flex-wrap">
        <ConfidenceBadge confidence={result.confidence} />
        {!result.image_quality_sufficient && (
          <span className="inline-flex items-center gap-1 rounded-md border border-red-500/30 bg-red-950/20 px-3 py-1.5 text-xs font-medium text-red-300">
            <AlertTriangle className="w-3 h-3" />
            Bildqualität unzureichend
          </span>
        )}
      </div>

      {/* Scores */}
      {Object.keys(result.scores).length > 0 && (
        <div className="card-premium p-6 space-y-4">
          <h4 className="text-sm font-serif font-semibold text-navy-900">
            Bewertungen
          </h4>
          <div className="space-y-3">
            {Object.entries(result.scores).map(([key, value]) => (
              <ScoreBar key={key} label={key} score={value} />
            ))}
          </div>
        </div>
      )}

      {/* Findings grouped by category */}
      {Object.keys(grouped).length > 0 && (
        <div className="card-premium p-6 space-y-5">
          <div className="flex items-center justify-between border-b border-navy-700/30 pb-4">
            <h4 className="text-sm font-serif font-semibold text-navy-900">
              Befunde
            </h4>
            {hasLowConfidence && (
              <button
                onClick={() => setShowLow(!showLow)}
                className="flex items-center gap-1.5 text-xs text-navy-600 hover:text-ocean-700 transition-colors duration-200"
              >
                {showLow ? (
                  <EyeOff className="w-3.5 h-3.5" />
                ) : (
                  <Eye className="w-3.5 h-3.5" />
                )}
                {showLow ? 'Unsichere ausblenden' : 'Unsichere anzeigen'}
              </button>
            )}
          </div>

          {Object.entries(grouped).map(([category, findings]) => (
            <div key={category} className="space-y-3">
              <h5 className="label-premium font-semibold">
                {category}
              </h5>
              {findings.map((finding, i) => (
                <div
                  key={`${category}-${i}`}
                  className="border-l-2 border-sand-200 bg-navy-900/20 rounded-lg px-4 py-3 space-y-2.5 transition-colors duration-200 hover:bg-navy-900/30"
                >
                  <div className="flex items-start justify-between gap-2">
                    <p className="text-sm text-navy-900">{finding.observation}</p>
                    <AssessmentBadge assessment={finding.assessment} />
                  </div>
                  {finding.location_in_image && (
                    <p className="text-xs text-navy-500">
                      Position: {finding.location_in_image}
                    </p>
                  )}
                  {finding.detail && (
                    <p className="text-xs text-navy-600">{finding.detail}</p>
                  )}
                  {finding.suggestion && (
                    <div className="flex items-start gap-2 text-xs text-ocean-600">
                      <Lightbulb className="w-3 h-3 mt-0.5 flex-shrink-0" />
                      <span>{finding.suggestion}</span>
                    </div>
                  )}
                  {isLowConfidence(finding.confidence) && (
                    <span className="inline-block rounded text-[10px] text-navy-500 border border-navy-600/30 px-2 py-1">
                      Niedrige Sicherheit
                    </span>
                  )}
                </div>
              ))}
            </div>
          ))}
        </div>
      )}

      {/* Positive aspects */}
      {result.positive_aspects.length > 0 && (
        <div className="rounded-xl border border-emerald-500/20 bg-emerald-950/10 p-6 space-y-4">
          <h4 className="flex items-center gap-2 text-sm font-serif font-semibold text-emerald-400">
            <CheckCircle className="w-4 h-4" />
            Positive Aspekte
          </h4>
          <ul className="space-y-2">
            {result.positive_aspects.map((item, i) => (
              <li key={i} className="flex items-start gap-3 text-sm text-emerald-300">
                <span className="mt-1.5 h-2 w-2 rounded-full bg-emerald-400 flex-shrink-0" />
                {item}
              </li>
            ))}
          </ul>
        </div>
      )}

      {/* Concerns */}
      {result.concerns.length > 0 && (
        <div className="rounded-xl border border-amber-500/20 bg-amber-950/10 p-6 space-y-4">
          <h4 className="flex items-center gap-2 text-sm font-serif font-semibold text-amber-400">
            <AlertTriangle className="w-4 h-4" />
            Bedenken
          </h4>
          <ul className="space-y-2">
            {result.concerns.map((item, i) => (
              <li key={i} className="flex items-start gap-3 text-sm text-amber-300">
                <span className="mt-1.5 h-2 w-2 rounded-full bg-amber-400 flex-shrink-0" />
                {item}
              </li>
            ))}
          </ul>
        </div>
      )}

      {/* Recommendations */}
      {result.recommendations.length > 0 && (
        <div className="card-premium p-6 space-y-4">
          <h4 className="flex items-center gap-2 text-sm font-serif font-semibold text-ocean-600">
            <Lightbulb className="w-4 h-4" />
            Empfehlungen
          </h4>
          <ul className="space-y-2">
            {result.recommendations.map((item, i) => (
              <li key={i} className="flex items-start gap-3 text-sm text-navy-600">
                <span className="mt-1.5 h-2 w-2 rounded-full bg-ocean-400 flex-shrink-0" />
                {item}
              </li>
            ))}
          </ul>
        </div>
      )}

      {/* Cannot assess (collapsed) */}
      {result.cannot_assess.length > 0 && (
        <div className="card-premium p-5">
          <button
            onClick={() => setCannotAssessOpen(!cannotAssessOpen)}
            className="flex items-center gap-2 text-sm font-medium text-navy-700 hover:text-navy-900 transition-colors duration-200 w-full"
          >
            {cannotAssessOpen ? (
              <ChevronDown className="w-4 h-4" />
            ) : (
              <ChevronRight className="w-4 h-4" />
            )}
            Nicht beurteilbar ({result.cannot_assess.length})
          </button>
          {cannotAssessOpen && (
            <ul className="mt-4 space-y-1.5 border-t border-navy-700/30 pt-4">
              {result.cannot_assess.map((item, i) => (
                <li key={i} className="flex items-start gap-2 text-sm text-navy-500">
                  <span className="mt-1.5 h-1.5 w-1.5 rounded-full bg-navy-600 flex-shrink-0" />
                  {item}
                </li>
              ))}
            </ul>
          )}
        </div>
      )}
    </div>
  )
}
