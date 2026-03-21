const SUB_SCORE_LABELS: Record<string, string> = {
  passage_width: 'Durchgangsbreiten',
  path_efficiency: 'Wegeeffizienz',
  crew_guest_separation: 'Crew/Gast-Trennung',
  accessibility: 'Erreichbarkeit',
  helm_ergonomics: 'Steuerstand-Ergonomie',
  storage_ratio: 'Stauraumanteil',
  storage_distribution: 'Stauraumverteilung',
  storage_accessibility: 'Stauraum-Erreichbarkeit',
}

interface SubScoreBarsProps {
  subScores: Record<string, number>
}

export default function SubScoreBars({ subScores }: SubScoreBarsProps) {
  return (
    <div className="space-y-5">
      {Object.entries(subScores).map(([key, value]) => {
        const color =
          value >= 80 ? 'bg-emerald-400' : value >= 60 ? 'bg-amber-400' : value >= 40 ? 'bg-orange-400' : 'bg-red-400'
        return (
          <div key={key}>
            <div className="flex justify-between items-center mb-2">
              <span className="label-premium">{SUB_SCORE_LABELS[key] || key}</span>
              <span className="font-mono text-sm font-semibold text-white">{Math.round(value)}</span>
            </div>
            <div className="h-1.5 bg-navy-800/60 rounded-full overflow-hidden">
              <div
                className={`h-full rounded-full transition-all duration-300 ${color}`}
                style={{ width: `${value}%` }}
              />
            </div>
          </div>
        )
      })}
    </div>
  )
}
