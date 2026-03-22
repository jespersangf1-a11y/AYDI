import { AlertTriangle } from 'lucide-react'
import type { FusedScore } from '../../types'
import ConfidenceBadge from '../analysis/ConfidenceBadge'

interface FusedScoreCardProps {
  moduleName: string
  moduleLabel: string
  fusedScore: FusedScore
}

function scoreColor(score: number): string {
  if (score >= 80) return 'text-emerald-400'
  if (score >= 60) return 'text-amber-400'
  if (score >= 40) return 'text-orange-400'
  return 'text-red-400'
}

function scoreBgColor(score: number): string {
  if (score >= 80) return 'bg-emerald-400/10 border-emerald-400/20'
  if (score >= 60) return 'bg-amber-400/10 border-amber-400/20'
  if (score >= 40) return 'bg-orange-400/10 border-orange-400/20'
  return 'bg-red-400/10 border-red-400/20'
}

export default function FusedScoreCard({
  moduleName,
  moduleLabel,
  fusedScore,
}: FusedScoreCardProps) {
  const hasFused = fusedScore.fused_score !== null
  const mainScore = fusedScore.fused_score ?? 0

  return (
    <div className="card-premium p-6 space-y-5">
      {/* Header */}
      <div className="flex items-center justify-between border-b border-navy-700/30 pb-4">
        <div>
          <h3 className="font-serif text-base font-medium text-navy-900">
            {moduleLabel}
          </h3>
          <p className="text-xs text-navy-500 mt-1">{moduleName}</p>
        </div>
        {fusedScore.visual_confidence && (
          <ConfidenceBadge confidence={fusedScore.visual_confidence} size="sm" />
        )}
      </div>

      {/* Main fused score */}
      {hasFused && (
        <div
          className={`flex items-center justify-center rounded-lg border px-6 py-6 transition-all duration-200 ${scoreBgColor(mainScore)}`}
        >
          <span className={`font-mono text-5xl font-bold ${scoreColor(mainScore)}`}>
            {Math.round(mainScore)}
          </span>
          <span className="ml-2 text-sm text-navy-600">/100</span>
        </div>
      )}

      {/* Sub-scores: structured vs visual */}
      <div className="grid grid-cols-2 gap-4">
        {fusedScore.structured_score !== null && (
          <div className="rounded-lg border border-navy-700/30 bg-navy-900/20 p-4 text-center transition-colors duration-200 hover:bg-white">
            <p className="label-premium mb-2">Strukturiert</p>
            <p
              className={`font-mono text-2xl font-bold ${scoreColor(fusedScore.structured_score)}`}
            >
              {Math.round(fusedScore.structured_score)}
            </p>
            <p className="text-[10px] text-navy-500 mt-2 border-t border-navy-700/20 pt-2">
              Gewicht: {Math.round(fusedScore.fusion_weights.structured * 100)}%
            </p>
          </div>
        )}
        {fusedScore.visual_score !== null && (
          <div className="rounded-lg border border-navy-700/30 bg-navy-900/20 p-4 text-center transition-colors duration-200 hover:bg-white">
            <p className="label-premium mb-2">Visuell</p>
            <p
              className={`font-mono text-2xl font-bold ${scoreColor(fusedScore.visual_score)}`}
            >
              {Math.round(fusedScore.visual_score)}
            </p>
            <p className="text-[10px] text-navy-500 mt-2 border-t border-navy-700/20 pt-2">
              Gewicht: {Math.round(fusedScore.fusion_weights.visual * 100)}%
            </p>
          </div>
        )}
      </div>

      {/* Disagreement warning */}
      {fusedScore.disagreement && (
        <div className="flex items-start gap-3 rounded-lg border border-amber-500/20 bg-amber-950/15 px-4 py-3">
          <AlertTriangle className="w-4 h-4 text-amber-400 flex-shrink-0 mt-0.5" />
          <div className="text-xs text-amber-300">
            <p className="font-medium">{fusedScore.disagreement.message}</p>
            <p className="mt-1.5 text-amber-400/90 font-mono text-[11px]">
              Strukturiert: {Math.round(fusedScore.disagreement.structured_score)} | Visuell: {Math.round(fusedScore.disagreement.visual_score)}
            </p>
          </div>
        </div>
      )}

      {/* Data source badges */}
      {fusedScore.data_sources.length > 0 && (
        <div className="flex items-center gap-2 flex-wrap pt-2 border-t border-navy-700/20">
          <span className="text-xs text-navy-500">Quellen:</span>
          {fusedScore.data_sources.map((source) => (
            <span
              key={source}
              className="inline-block rounded-md border border-navy-600/20 bg-sand-50/40 px-2.5 py-1 text-[10px] font-medium text-navy-600"
            >
              {source}
            </span>
          ))}
        </div>
      )}
    </div>
  )
}
