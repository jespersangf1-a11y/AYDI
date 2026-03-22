import { useState } from 'react'
import type { BoatClass, PublicSpecs, QuickAnalysisResponse } from '../../types'
import { BOAT_CLASS_LABELS } from '../../types'
import { runQuickAnalysis } from '../../services/api'
import { MEDIA } from '../../config/media'
import SpecForm from './SpecForm'
import QuickResults from './QuickResults'

type Step = 'select-class' | 'enter-specs' | 'results'

const BOAT_CLASS_DESCRIPTIONS: Record<string, string> = {
  small_sail: '8 – 12 m  ·  Kompakt, effizient, segeloptimiert',
  cruising_sail: '12 – 18 m  ·  Blauwasser, Komfort und Funktion',
  large_motor: '18 – 30 m  ·  Luxus, Crew-Trennung, mehrere Decks',
  superyacht: '30 m+  ·  Architektonisches Design, volle Privatheit',
}

// Animations for premium UX
const stepAnimationStyles = `
  @keyframes slideInRight {
    from {
      opacity: 0;
      transform: translateX(20px);
    }
    to {
      opacity: 1;
      transform: translateX(0);
    }
  }

  @keyframes slideInLeft {
    from {
      opacity: 0;
      transform: translateX(-20px);
    }
    to {
      opacity: 1;
      transform: translateX(0);
    }
  }

  @keyframes stepPulse {
    0% {
      box-shadow: 0 0 0 0 rgba(0, 176, 240, 0.4);
    }
    70% {
      box-shadow: 0 0 0 8px rgba(0, 176, 240, 0);
    }
    100% {
      box-shadow: 0 0 0 0 rgba(0, 176, 240, 0);
    }
  }

  @keyframes cardStaggered {
    from {
      opacity: 0;
      transform: translateY(16px);
    }
    to {
      opacity: 1;
      transform: translateY(0);
    }
  }

  @keyframes checkmarkScale {
    0% { transform: scale(0.5); }
    50% { transform: scale(1.2); }
    100% { transform: scale(1); }
  }

  .animate-step-pulse {
    animation: stepPulse 2s infinite;
  }

  .animate-slide-right {
    animation: slideInRight 0.5s ease-out;
  }

  .animate-slide-left {
    animation: slideInLeft 0.5s ease-out;
  }

  .animate-card-staggered {
    animation: cardStaggered 0.5s ease-out;
  }

  .animate-checkmark {
    animation: checkmarkScale 0.6s cubic-bezier(0.68, -0.55, 0.265, 1.55);
  }

  .card-hover-lift {
    transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1);
  }

  .card-hover-lift:hover {
    transform: translateY(-6px);
    box-shadow: 0 24px 48px rgba(0, 176, 240, 0.15);
    border-color: rgba(0, 176, 240, 0.4);
  }
`

export default function QuickAnalysis() {
  const [step, setStep] = useState<Step>('select-class')
  const [prevStep, setPrevStep] = useState<Step>('select-class')
  const [selectedClass, setSelectedClass] = useState<BoatClass | null>(null)
  const [result, setResult] = useState<QuickAnalysisResponse | null>(null)
  const [loading, setLoading] = useState(false)
  const [error, setError] = useState<string | null>(null)

  const handleSelectClass = (bc: BoatClass) => {
    setPrevStep(step)
    setSelectedClass(bc)
    setStep('enter-specs')
  }

  const handleSubmitSpecs = async (specs: PublicSpecs) => {
    setLoading(true)
    setError(null)
    try {
      const res = await runQuickAnalysis(specs)
      setResult(res)
      setPrevStep(step)
      setStep('results')
    } catch (e) {
      setError(e instanceof Error ? e.message : 'Analysefehler')
    } finally {
      setLoading(false)
    }
  }

  const handleNewAnalysis = () => {
    setPrevStep(step)
    setStep('select-class')
    setSelectedClass(null)
    setResult(null)
    setError(null)
  }

  const handleBack = () => {
    setPrevStep(step)
    setStep('select-class')
  }

  // Step labels for progress indicator
  const steps: { key: Step; label: string }[] = [
    { key: 'select-class', label: 'Bootsklasse' },
    { key: 'enter-specs', label: 'Spezifikationen' },
    { key: 'results', label: 'Ergebnis' },
  ]
  const stepIndex = steps.findIndex((s) => s.key === step)
  const isMovingForward = steps.findIndex((s) => s.key === step) > steps.findIndex((s) => s.key === prevStep)

  const heroImage =
    step === 'enter-specs'
      ? MEDIA.hero.deck_detail
      : MEDIA.hero.ocean_horizon

  const heroTitle =
    step === 'select-class'
      ? 'Schnellanalyse'
      : step === 'enter-specs' && selectedClass
      ? BOAT_CLASS_LABELS[selectedClass]
      : 'Analyseergebnis'

  const heroSubtitle =
    step === 'select-class'
      ? 'Erste Bewertung ohne CAD-Daten — wählen Sie die Bootsklasse.'
      : step === 'enter-specs'
      ? 'Geben Sie die bekannten Spezifikationen ein.'
      : 'Vollständige Bewertung Ihres Entwurfs.'

  return (
    <div>
      <style>{stepAnimationStyles}</style>

      {/* Hero header with background image */}
      <div className="hero-section min-h-[240px] md:min-h-[300px] flex items-end overflow-hidden">
        <div
          className="absolute inset-0 w-full h-full bg-cover bg-center transition-all duration-500"
          style={{ backgroundImage: `url(${heroImage})` }}
        />
        <div className="relative w-full px-6 md:px-10 pb-8 pt-20 z-10">
          <p className="label-premium mb-2 opacity-90">Schnelle Analyse</p>
          <h1 className="font-serif text-3xl md:text-display font-medium text-white">
            {heroTitle}
          </h1>
          <p className="font-sans text-sm text-navy-300 mt-2 max-w-xl leading-relaxed">
            {heroSubtitle}
          </p>
        </div>
      </div>

      {/* Content */}
      <div className="max-w-5xl mx-auto px-6 md:px-10 py-10 md:py-12">
        {/* Step indicator with animation */}
        <div className="flex flex-col md:flex-row md:items-center gap-4 md:gap-6 mb-10 md:mb-12 overflow-x-auto pb-2 md:pb-0">
          {steps.map((s, idx) => {
            const isActive = s.key === step
            const isDone = idx < stepIndex
            return (
              <div
                key={s.key}
                className="flex items-center gap-2 md:gap-3 shrink-0 md:shrink"
                role="progressbar"
                aria-valuenow={idx + 1}
                aria-valuemin={1}
                aria-valuemax={steps.length}
                aria-label={`Schritt ${idx + 1} von ${steps.length}: ${s.label}`}
              >
                <div
                  className={`w-7 h-7 rounded-full flex items-center justify-center text-[11px] font-mono font-semibold transition-all duration-500 ${
                    isActive
                      ? 'bg-ocean-700/80 text-white ring-2 ring-ocean-500/50 animate-step-pulse'
                      : isDone
                      ? 'bg-emerald-600/60 text-emerald-300 ring-1 ring-emerald-500/30'
                      : 'bg-navy-800/60 text-navy-500'
                  }`}
                >
                  {isDone ? (
                    <span className="animate-checkmark">✓</span>
                  ) : (
                    idx + 1
                  )}
                </div>
                <span
                  className={`text-xs md:text-[13px] font-sans font-medium transition-all duration-300 whitespace-nowrap ${
                    isActive ? 'text-white font-semibold' : isDone ? 'text-navy-300' : 'text-navy-500'
                  }`}
                >
                  {s.label}
                </span>
                {idx < steps.length - 1 && (
                  <div
                    className={`hidden md:block w-12 h-px mx-2 transition-all duration-500 ${
                      isDone ? 'bg-emerald-600/60' : isActive ? 'bg-ocean-500/50' : 'bg-navy-800'
                    }`}
                  />
                )}
              </div>
            )
          })}
        </div>

        {/* Step: Select boat class */}
        {step === 'select-class' && (
          <div className={`grid gap-4 sm:grid-cols-2 ${isMovingForward ? 'animate-slide-right' : 'animate-slide-left'}`}>
            {(Object.keys(BOAT_CLASS_LABELS) as BoatClass[]).map((bc, idx) => (
              <button
                key={bc}
                onClick={() => handleSelectClass(bc)}
                className="card-hover-lift text-left card-premium p-6 group overflow-hidden"
                style={{
                  animation: `cardStaggered 0.5s ease-out ${idx * 100}ms both`,
                }}
                aria-label={`${BOAT_CLASS_LABELS[bc]}: ${BOAT_CLASS_DESCRIPTIONS[bc] || ''}`}
              >
                <h3 className="font-serif text-lg font-medium text-white mb-1.5 group-hover:text-ocean-300 transition-colors duration-200">
                  {BOAT_CLASS_LABELS[bc]}
                </h3>
                <p className="text-[13px] text-navy-400 leading-relaxed">
                  {BOAT_CLASS_DESCRIPTIONS[bc] || ''}
                </p>
              </button>
            ))}
          </div>
        )}

        {/* Step: Enter specs */}
        {step === 'enter-specs' && selectedClass && (
          <div className={isMovingForward ? 'animate-slide-right' : 'animate-slide-left'}>
            {error && (
              <div
                className="bg-red-950/40 border-l-4 border-red-500 rounded-r-lg px-5 py-3 text-red-300 text-sm mb-8 animate-slide-right"
                role="alert"
              >
                {error}
              </div>
            )}
            <SpecForm
              boatClass={selectedClass}
              loading={loading}
              onSubmit={handleSubmitSpecs}
              onBack={handleBack}
            />
          </div>
        )}

        {/* Step: Results */}
        {step === 'results' && result && (
          <div className={isMovingForward ? 'animate-slide-right' : 'animate-slide-left'}>
            <QuickResults result={result} onNewAnalysis={handleNewAnalysis} />
          </div>
        )}
      </div>
    </div>
  )
}
