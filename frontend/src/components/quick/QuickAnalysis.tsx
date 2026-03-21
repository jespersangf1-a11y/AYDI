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

export default function QuickAnalysis() {
  const [step, setStep] = useState<Step>('select-class')
  const [selectedClass, setSelectedClass] = useState<BoatClass | null>(null)
  const [result, setResult] = useState<QuickAnalysisResponse | null>(null)
  const [loading, setLoading] = useState(false)
  const [error, setError] = useState<string | null>(null)

  const handleSelectClass = (bc: BoatClass) => {
    setSelectedClass(bc)
    setStep('enter-specs')
  }

  const handleSubmitSpecs = async (specs: PublicSpecs) => {
    setLoading(true)
    setError(null)
    try {
      const res = await runQuickAnalysis(specs)
      setResult(res)
      setStep('results')
    } catch (e) {
      setError(e instanceof Error ? e.message : 'Analysefehler')
    } finally {
      setLoading(false)
    }
  }

  const handleNewAnalysis = () => {
    setStep('select-class')
    setSelectedClass(null)
    setResult(null)
    setError(null)
  }

  // Step labels for progress indicator
  const steps: { key: Step; label: string }[] = [
    { key: 'select-class', label: 'Bootsklasse' },
    { key: 'enter-specs', label: 'Spezifikationen' },
    { key: 'results', label: 'Ergebnis' },
  ]
  const stepIndex = steps.findIndex((s) => s.key === step)

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
      ? 'Erste Bewertung ohne CAD-Daten — waehlen Sie die Bootsklasse.'
      : step === 'enter-specs'
      ? 'Geben Sie die bekannten Spezifikationen ein.'
      : 'Vollstaendige Bewertung Ihres Entwurfs.'

  return (
    <div>
      {/* Hero header with background image */}
      <div className="hero-section min-h-[240px] flex items-end">
        <div
          className="absolute inset-0 w-full h-full bg-cover bg-center"
          style={{ backgroundImage: `url(${heroImage})` }}
        />
        <div className="w-full px-10 pb-8 pt-20">
          <p className="label-premium mb-2">Schnelle Analyse</p>
          <h1 className="font-serif text-display font-medium text-white">
            {heroTitle}
          </h1>
          <p className="font-sans text-sm text-navy-300 mt-2 max-w-xl">
            {heroSubtitle}
          </p>
        </div>
      </div>

      {/* Content */}
      <div className="max-w-5xl mx-auto px-10 py-10">
        {/* Step indicator */}
        <div className="flex items-center gap-4 mb-10">
          {steps.map((s, idx) => {
            const isActive = s.key === step
            const isDone = idx < stepIndex
            return (
              <div key={s.key} className="flex items-center gap-3">
                <div
                  className={`w-7 h-7 rounded-full flex items-center justify-center text-[11px] font-mono font-semibold transition-colors duration-200 ${
                    isActive
                      ? 'bg-ocean-700/80 text-white ring-1 ring-ocean-500/30'
                      : isDone
                      ? 'bg-navy-700 text-emerald-400'
                      : 'bg-navy-800/60 text-navy-500'
                  }`}
                >
                  {isDone ? '\u2713' : idx + 1}
                </div>
                <span
                  className={`text-[13px] font-sans font-medium transition-colors duration-200 ${
                    isActive ? 'text-white' : isDone ? 'text-navy-300' : 'text-navy-500'
                  }`}
                >
                  {s.label}
                </span>
                {idx < steps.length - 1 && (
                  <div className={`w-16 h-px mx-1 ${isDone ? 'bg-navy-600' : 'bg-navy-800'}`} />
                )}
              </div>
            )
          })}
        </div>

        {/* Step: Select boat class */}
        {step === 'select-class' && (
          <div className="grid gap-4 sm:grid-cols-2 animate-fade-in">
            {(Object.keys(BOAT_CLASS_LABELS) as BoatClass[]).map((bc) => (
              <button
                key={bc}
                onClick={() => handleSelectClass(bc)}
                className="text-left card-premium p-6 hover:border-ocean-700/40 transition-all duration-200 group"
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
          <div className="animate-fade-in">
            {error && (
              <div className="bg-red-950/40 border-l-2 border-red-500 rounded-r-lg px-5 py-3 text-red-300 text-sm mb-8">
                {error}
              </div>
            )}
            <SpecForm
              boatClass={selectedClass}
              loading={loading}
              onSubmit={handleSubmitSpecs}
              onBack={() => setStep('select-class')}
            />
          </div>
        )}

        {/* Step: Results */}
        {step === 'results' && result && (
          <div className="animate-fade-in">
            <QuickResults result={result} onNewAnalysis={handleNewAnalysis} />
          </div>
        )}
      </div>
    </div>
  )
}
