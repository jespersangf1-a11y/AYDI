interface ScoreGaugeProps {
  score: number
  label: string
  size?: number
}

export default function ScoreGauge({ score, label, size = 160 }: ScoreGaugeProps) {
  const radius = (size - 12) / 2
  const circumference = 2 * Math.PI * radius
  const offset = circumference - (score / 100) * circumference

  const color =
    score >= 80 ? 'text-emerald-400' : score >= 60 ? 'text-amber-400' : score >= 40 ? 'text-orange-400' : 'text-red-400'
  const strokeColor =
    score >= 80 ? '#4ade80' : score >= 60 ? '#fbbf24' : score >= 40 ? '#fb923c' : '#f87171'

  return (
    <div className="flex flex-col items-center">
      <div className="relative" style={{ width: size, height: size }}>
        <svg
          className="transform -rotate-90"
          width={size}
          height={size}
          role="img"
          aria-label={`${label}: ${Math.round(score)} von 100 Punkten`}
        >
          <circle
            cx={size / 2}
            cy={size / 2}
            r={radius}
            fill="none"
            stroke="currentColor"
            strokeWidth={3}
            className="text-navy-700/60"
          />
          <circle
            cx={size / 2}
            cy={size / 2}
            r={radius}
            fill="none"
            stroke={strokeColor}
            strokeWidth={3}
            strokeDasharray={circumference}
            strokeDashoffset={offset}
            strokeLinecap="round"
            className="transition-all duration-500"
          />
        </svg>
        <div className="absolute inset-0 flex flex-col items-center justify-center">
          <span className={`font-mono text-3xl font-bold ${color}`}>{Math.round(score)}</span>
          <span className="text-xs text-navy-400">/ 100</span>
        </div>
      </div>
      <span className="mt-3 text-xs font-sans font-semibold uppercase tracking-wider-premium text-navy-300">{label}</span>
    </div>
  )
}
