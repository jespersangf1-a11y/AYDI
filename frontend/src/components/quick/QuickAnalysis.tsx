import { useState } from 'react'
import type { BoatClass, PublicSpecs, QuickAnalysisResponse } from '../../types'
import { BOAT_CLASS_LABELS } from '../../types'
import { runQuickAnalysis } from '../../services/api'
import SpecForm from './SpecForm'
import QuickResults from './QuickResults'

type Step = 'select-class' | 'enter-specs' | 'results'

const BOAT_CLASS_DESCRIPTIONS: Record<BoatClass, string> = {
  small_sail: '8 – 12 m · Kompakt, effizient, segeloptimiert',
  cruising_sail: '12 – 18 m · Blauwasser, Komfort + Funktion',
  large_motor: '18 – 30 m · Luxus, Crew-Trennung, mehrere Decks',
  superyacht: '30 m+ · Architektonisches Design, volle Privatheit',
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

  return (
    <div className="max-w-4xl mx-auto">
      {/* Step indicator */}
      <div className="flex items-center gap-2 mb-8">
        {(['select-class', 'enter-specs', 'results'] as Step[]).map((s, idx) => {
          const labels = ['Bootsklasse', 'Spezifikationen', 'Ergebnis']
          const stepIndex = ['select-class', 'enter-specs', 'results'].indexOf(step)
          const isActive = s === step
          const isDone = idx < stepIndex
          return (
            <div key={s} className="flex items-center gap-2">
              <div
                className={`w-7 h-7 rounded-full flex items-center justify-center text-xs font-mono font-bold transition-colors ${
                  isActive
                    ? 'bg-ocean-600 text-white'
                    : isDone
                    ? 'bg-emerald-600 text-white'
                    : 'bg-navy-800 text-navy-400'
                }`}
              >
                {isDone ? '✓' : idx + 1}
              </div>
              <span
                className={`text-sm ${isActive ? 'text-white' : isDone ? 'text-emerald-400' : 'text-navy-500'}`}
              >
                {labels[idx]}
              </span>
              {idx < 2 && <div className="w-8 h-px bg-navy-700 mx-1" />}
            </div>
          )
        })}
      </div>

      {/* Step: Select boat class */}
      {step === 'select-class' && (
        <div>
          <h2 className="font-display text-2xl font-bold text-white mb-2">
            Schnellanalyse starten
          </h2>
          <p className="text-navy-400 mb-8">
            Wählen Sie die Bootsklasse, um eine Erstbewertung ohne CAD-Daten zu erhalten.
          </p>
          <div className="grid gap-4 sm:grid-cols-2">
            {(Object.keys(BOAT_CLASS_LABELS) as BoatClass[]).map((bc) => (
              <button
                key={bc}
                onClick={() => handleSelectClass(bc)}
                className="text-left bg-navy-900 border border-navy-700 rounded-xl p-6 hover:border-ocean-500 hover:bg-navy-800 transition-all group"
              >
                <h3 className="font-display font-semibold text-white text-lg mb-1 group-hover:text-ocean-300 transition-colors">
                  {BOAT_CLASS_LABELS[bc]}
                </h3>
                <p className="text-sm text-navy-400">{BOAT_CLASS_DESCRIPTIONS[bc]}</p>
              </button>
            ))}
          </div>
        </div>
      )}

      {/* Step: Enter specs */}
      {step === 'enter-specs' && selectedClass && (
        <div>
          <h2 className="font-display text-2xl font-bold text-white mb-2">
            {BOAT_CLASS_LABELS[selectedClass]}
          </h2>
          <p className="text-navy-400 mb-6">
            Geben Sie die bekannten Spezifikationen ein. Mehr Details ergeben eine bessere Analyse.
          </p>
          {error && (
            <div className="bg-red-900/50 border border-red-700 rounded-lg p-3 text-red-300 text-sm mb-4">
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
        <QuickResults result={result} onNewAnalysis={handleNewAnalysis} />
      )}
    </div>
  )
}
