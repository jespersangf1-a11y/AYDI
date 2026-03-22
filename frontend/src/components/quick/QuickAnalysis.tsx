import { useState } from 'react'
import type { BoatClass, PublicSpecs, QuickAnalysisResponse } from '../../types'
import { BOAT_CLASS_LABELS } from '../../types'
import { runQuickAnalysis } from '../../services/api'
import { MEDIA } from '../../config/media'
import HeroCarousel from '../layout/HeroCarousel'
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
      : step === 'results'
      ? MEDIA.hero.aerial_yacht
      : MEDIA.hero.ocean_horizon

  // Video background for the initial boat class selection step
  const heroVideo = step === 'select-class' ? MEDIA.video.ocean_calm : undefined

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
      {/* Hero header — Carousel on start, static on other steps */}
      {step === 'select-class' ? (
        <HeroCarousel
          title={heroTitle}
          subtitle={heroSubtitle}
          label="Yacht Design Intelligence"
          imageDuration={6000}
          videoDuration={10000}
          fadeDuration={1500}
          showDomainLabel={true}
        />
      ) : (
        <div className="hero-section min-h-[240px] md:min-h-[300px] flex items-end overflow-hidden">
          {heroVideo ? (
            <video
              autoPlay
              loop
              muted
              playsInline
              className="absolute inset-0 w-full h-full object-cover transition-opacity duration-700"
              key={heroVideo}
            >
              <source src={heroVideo} type="video/mp4" />
            </video>
          ) : (
            <div
              className="absolute inset-0 w-full h-full bg-cover bg-center transition-all duration-500"
              style={{ backgroundImage: `url(${heroImage})` }}
            />
          )}
          <div className="absolute inset-0 bg-gradient-to-t from-navy-950/85 via-navy-950/55 to-navy-950/35" />
          <div className="relative w-full px-6 md:px-10 pb-8 pt-20 z-10">
            <p className="label-premium mb-2 opacity-90" style={{ color: 'rgba(255,255,255,0.9)' }}>Schnelle Analyse</p>
            <h1 className="font-serif text-3xl md:text-display font-medium text-white">
              {heroTitle}
            </h1>
            <p className="font-sans text-sm text-white mt-2 max-w-xl leading-relaxed">
              {heroSubtitle}
            </p>
          </div>
        </div>
      )}

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
                      ? 'bg-ocean-500 text-navy-900 ring-2 ring-ocean-300/50 animate-pulse-glow'
                      : isDone
                      ? 'bg-emerald-500 text-navy-900 ring-1 ring-emerald-300/30'
                      : 'bg-sand-200 text-navy-600'
                  }`}
                >
                  {isDone ? (
                    <span className="animate-fade-in-scale">✓</span>
                  ) : (
                    idx + 1
                  )}
                </div>
                <span
                  className={`text-xs md:text-[13px] font-sans font-medium transition-all duration-300 whitespace-nowrap ${
                    isActive ? 'text-navy-900 font-semibold' : isDone ? 'text-navy-700' : 'text-navy-600'
                  }`}
                >
                  {s.label}
                </span>
                {idx < steps.length - 1 && (
                  <div
                    className={`hidden md:block w-12 h-px mx-2 transition-all duration-500 ${
                      isDone ? 'bg-emerald-600/60' : isActive ? 'bg-ocean-500/50' : 'bg-sand-50'
                    }`}
                  />
                )}
              </div>
            )
          })}
        </div>

        {/* Step: Select boat class */}
        {step === 'select-class' && (
          <div className={`grid gap-4 sm:grid-cols-2 ${isMovingForward ? 'animate-slide-in-right' : 'animate-slide-in-left'}`}>
            {(Object.keys(BOAT_CLASS_LABELS) as BoatClass[]).map((bc, idx) => (
              <button
                key={bc}
                onClick={() => handleSelectClass(bc)}
                className={`text-left card-premium p-6 group overflow-hidden animate-fade-in-up stagger-${idx + 1}`}
                aria-label={`${BOAT_CLASS_LABELS[bc]}: ${BOAT_CLASS_DESCRIPTIONS[bc] || ''}`}
              >
                <h3 className="font-serif text-lg font-medium text-navy-900 mb-1.5 group-hover:text-ocean-600 transition-colors duration-200">
                  {BOAT_CLASS_LABELS[bc]}
                </h3>
                <p className="text-[13px] text-navy-600 leading-relaxed">
                  {BOAT_CLASS_DESCRIPTIONS[bc] || ''}
                </p>
              </button>
            ))}
          </div>
        )}

        {/* Step: Enter specs */}
        {step === 'enter-specs' && selectedClass && (
          <div className={isMovingForward ? 'animate-slide-in-right' : 'animate-slide-in-left'}>
            {error && (
              <div
                className="bg-red-950/40 border-l-4 border-red-500 rounded-r-lg px-5 py-3 text-red-300 text-sm mb-8 animate-slide-in-right"
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
          <div className={isMovingForward ? 'animate-slide-in-right' : 'animate-slide-in-left'}>
            <QuickResults result={result} onNewAnalysis={handleNewAnalysis} />
          </div>
        )}
      </div>
    </div>
  )
}
