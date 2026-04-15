import { useState, useEffect, useRef, useId } from 'react'

interface ScoreGaugeProps {
  score: number
  label: string
  size?: 'sm' | 'md' | 'lg' | number
}

const SIZE_MAP: Record<'sm' | 'md' | 'lg', number> = {
  sm: 80,
  md: 120,
  lg: 160,
}

export default function ScoreGauge({ score, label, size = 'md' }: ScoreGaugeProps) {
  const uniqueId = useId()
  const sizeValue = typeof size === 'string' ? SIZE_MAP[size] : size
  const [animatedScore, setAnimatedScore] = useState(0)
  const [hasAnimated, setHasAnimated] = useState(false)
  const animationRef = useRef<ReturnType<typeof setInterval> | null>(null)
  const [offset, setOffset] = useState<number | null>(null)

  const radius = (sizeValue - 12) / 2
  const circumference = 2 * Math.PI * radius
  const targetOffset = circumference - (score / 100) * circumference

  const color =
    score >= 80 ? 'text-emerald-600' : score >= 60 ? 'text-amber-600' : score >= 40 ? 'text-orange-600' : 'text-red-600'

  // Color gradient stops
  const strokeStartColor =
    score >= 80 ? '#059669' : score >= 60 ? '#d97706' : score >= 40 ? '#ea580c' : '#dc2626'
  const strokeEndColor =
    score >= 80 ? '#34d399' : score >= 60 ? '#fbbf24' : score >= 40 ? '#fb923c' : '#f87171'

  // Animate number count-up on mount
  useEffect(() => {
    if (hasAnimated) return

    const duration = 1000 // 1 second
    const startTime = Date.now()

    const animate = () => {
      const elapsed = Date.now() - startTime
      const progress = Math.min(elapsed / duration, 1)
      setAnimatedScore(Math.floor(score * progress))

      if (progress < 1) {
        animationRef.current = setTimeout(animate, 16) // ~60fps
      } else {
        setAnimatedScore(score)
        setHasAnimated(true)
      }
    }

    animationRef.current = setTimeout(animate, 16)

    return () => {
      if (animationRef.current) {
        clearTimeout(animationRef.current)
      }
    }
  }, [score, hasAnimated])

  // Animate circle draw on mount
  useEffect(() => {
    if (!hasAnimated) {
      setOffset(circumference)
    } else {
      setOffset(targetOffset)
    }
  }, [hasAnimated, circumference, targetOffset])

  return (
    <div className="flex flex-col items-center" aria-label={`Gesamtbewertung: ${score} von 100`}>
      <div className="relative" style={{ width: sizeValue, height: sizeValue }}>
        <svg
          className="transform -rotate-90"
          width={sizeValue}
          height={sizeValue}
          role="img"
          aria-label={`${label}: ${Math.round(score)} von 100 Punkten`}
        >
          <defs>
            <linearGradient id={`gradient-${uniqueId}`} x1="0%" y1="0%" x2="100%" y2="100%">
              <stop offset="0%" stopColor={strokeStartColor} />
              <stop offset="100%" stopColor={strokeEndColor} />
            </linearGradient>
            <filter id={`glow-${uniqueId}`} x="-50%" y="-50%" width="200%" height="200%">
              <feGaussianBlur stdDeviation="2" result="coloredBlur" />
              <feMerge>
                <feMergeNode in="coloredBlur" />
                <feMergeNode in="SourceGraphic" />
              </feMerge>
            </filter>
          </defs>

          {/* Glow effect background circle */}
          <circle
            cx={sizeValue / 2}
            cy={sizeValue / 2}
            r={radius}
            fill="none"
            stroke={strokeStartColor}
            strokeWidth={3}
            strokeDasharray={circumference}
            strokeDashoffset={offset ?? circumference}
            strokeLinecap="round"
            opacity="0.2"
            filter={`url(#glow-${uniqueId})`}
            style={{
              transition: `stroke-dashoffset 1s ease-out`,
            }}
          />

          {/* Background circle */}
          <circle
            cx={sizeValue / 2}
            cy={sizeValue / 2}
            r={radius}
            fill="none"
            stroke="currentColor"
            strokeWidth={3}
            className="text-navy-700/60"
          />

          {/* Gradient animated circle */}
          <circle
            cx={sizeValue / 2}
            cy={sizeValue / 2}
            r={radius}
            fill="none"
            stroke={`url(#gradient-${uniqueId})`}
            strokeWidth={3}
            strokeDasharray={circumference}
            strokeDashoffset={offset ?? circumference}
            strokeLinecap="round"
            style={{
              transition: `stroke-dashoffset 1s ease-out`,
            }}
          />
        </svg>

        {/* Score number display */}
        <div className="absolute inset-0 flex flex-col items-center justify-center">
          <span
            className={`font-mono tabular-nums font-bold ${color} ${!hasAnimated ? 'animate-fade-in-scale stagger-2' : ''}`}
            style={{
              fontSize: sizeValue * 0.25,
            }}
          >
            {animatedScore}
          </span>
          <span
            className={`text-navy-600 ${!hasAnimated ? 'animate-fade-in-scale stagger-4' : ''}`}
            style={{
              fontSize: sizeValue * 0.08,
            }}
          >
            / 100
          </span>
        </div>
      </div>

      <span className="mt-3 text-xs font-sans font-semibold uppercase tracking-wider-premium text-navy-700">
        {label}
      </span>

    </div>
  )
}
