import { useState, useRef, useEffect } from 'react'

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

interface BarItemProps {
  label: string
  value: number
  index: number
}

function BarItem({ label, value, index }: BarItemProps) {
  const [showTooltip, setShowTooltip] = useState(false)
  const [truncated, setTruncated] = useState(false)
  const labelRef = useRef<HTMLSpanElement>(null)

  useEffect(() => {
    if (labelRef.current) {
      setTruncated(labelRef.current.scrollWidth > labelRef.current.clientWidth)
    }
  }, [label])

  const gradientColor =
    value >= 80
      ? 'from-emerald-500 to-emerald-400'
      : value >= 60
        ? 'from-amber-500 to-amber-400'
        : value >= 40
          ? 'from-orange-500 to-orange-400'
          : 'from-red-500 to-red-400'

  return (
    <div>
      <div className="flex justify-between items-center mb-2">
        <div className="relative flex-1 mr-2">
          <span
            ref={labelRef}
            className="label-premium block truncate"
            title={truncated ? label : undefined}
          >
            {label}
          </span>
          {truncated && showTooltip && (
            <div className="absolute bottom-full left-0 mb-2 px-2 py-1 bg-white text-navy-800 text-xs rounded whitespace-nowrap z-10 border border-sand-200 shadow-md">
              {label}
            </div>
          )}
        </div>
        <div className="relative">
          <span className="font-mono text-sm font-semibold text-navy-900">{Math.round(value)}</span>
          {showTooltip && (
            <div className="absolute bottom-full right-0 mb-2 px-2.5 py-1 bg-white text-navy-800 text-xs rounded border border-sand-200 shadow-md whitespace-nowrap">
              {Math.round(value)} / 100
            </div>
          )}
        </div>
      </div>

      <div
        className="h-1.5 bg-sand-200 rounded-full overflow-hidden cursor-help transition-all duration-200 hover:h-2"
        onMouseEnter={() => setShowTooltip(true)}
        onMouseLeave={() => setShowTooltip(false)}
      >
        <div
          className={`h-full rounded-full bg-gradient-to-r ${gradientColor}`}
          style={{
            width: `${value}%`,
            animation: `slideIn 0.8s ease-out ${index * 80}ms both`,
          }}
        />
      </div>
    </div>
  )
}

export default function SubScoreBars({ subScores }: SubScoreBarsProps) {
  return (
    <div className="space-y-5">
      {Object.entries(subScores).map(([key, value], index) => (
        <BarItem
          key={key}
          label={SUB_SCORE_LABELS[key] || key}
          value={value}
          index={index}
        />
      ))}

      <style>{`
        @keyframes slideIn {
          from {
            width: 0;
            opacity: 0;
          }
          to {
            width: var(--target-width);
            opacity: 1;
          }
        }
      `}</style>
    </div>
  )
}
