import { useState } from 'react'
import { ChevronDown, ChevronRight } from 'lucide-react'
import type { BoatClass, PublicSpecs } from '../../types'

interface SpecFormProps {
  boatClass: BoatClass
  loading: boolean
  onSubmit: (specs: PublicSpecs) => void
  onBack: () => void
}

interface SectionProps {
  title: string
  hint?: string
  defaultOpen?: boolean
  children: React.ReactNode
}

function Section({ title, hint, defaultOpen = false, children }: SectionProps) {
  const [open, setOpen] = useState(defaultOpen)
  return (
    <div className="bg-navy-900/40 border border-navy-700/40 rounded-xl overflow-hidden backdrop-blur-sm transition-colors duration-200 hover:bg-navy-900/50">
      <button
        type="button"
        onClick={() => setOpen((v) => !v)}
        className="w-full flex items-center justify-between px-6 py-4 transition-colors duration-200"
      >
        <div className="flex items-center gap-3">
          {open ? (
            <ChevronDown className="w-4 h-4 text-ocean-500" />
          ) : (
            <ChevronRight className="w-4 h-4 text-navy-500" />
          )}
          <span className="font-serif font-semibold text-white">{title}</span>
          {hint && <span className="text-xs text-navy-500 ml-2">{hint}</span>}
        </div>
      </button>
      {open && <div className="px-6 pb-6 grid gap-4 sm:grid-cols-2 border-t border-navy-700/40">{children}</div>}
    </div>
  )
}

interface FieldProps {
  label: string
  name: string
  type?: 'number' | 'text'
  unit?: string
  placeholder?: string
  value: string
  onChange: (name: string, value: string) => void
  required?: boolean
  min?: number
  step?: number
  error?: string
  validator?: (value: string, otherFields?: Record<string, string>) => string | null
}

function Field({ label, name, type = 'number', unit, placeholder, value, onChange, required, min, step, error }: FieldProps) {
  return (
    <div>
      <label className="block text-xs font-semibold tracking-wider-premium uppercase text-navy-400 mb-2">
        {label}
        {required && <span className="text-ocean-400 ml-1.5">erforderlich</span>}
        {unit && <span className="text-navy-500 ml-1.5">({unit})</span>}
      </label>
      <input
        type={type}
        name={name}
        value={value}
        placeholder={placeholder}
        required={required}
        min={min}
        step={step}
        onChange={(e) => onChange(name, e.target.value)}
        className={`w-full bg-navy-800/50 border rounded-lg px-4 py-2.5 text-white text-sm placeholder-navy-500 focus:outline-none transition-colors duration-200 font-mono ${
          error ? 'border-red-600/60 focus:border-red-500' : 'border-navy-600/40 focus:border-ocean-600'
        }`}
      />
      {error && <p className="text-red-400 text-xs mt-1.5">{error}</p>}
    </div>
  )
}

export default function SpecForm({ boatClass, loading, onSubmit, onBack }: SpecFormProps) {
  const [fields, setFields] = useState<Record<string, string>>({
    length_m: '',
    beam_m: '',
    draft_m: '',
    displacement_kg: '',
    cabin_count: '',
    berth_count: '',
    head_count: '',
    cockpit_area_sqm: '',
    salon_area_sqm: '',
    pantry_type: '',
    helm_position: '',
    has_flybridge: '',
    has_crew_quarters: '',
    engine_hp: '',
    engine_count: '',
    fuel_capacity_l: '',
    water_capacity_l: '',
    sail_area_sqm: '',
    max_speed_kn: '',
    price_eur: '',
    year: '',
    brand: '',
    model_name: '',
    deck_height_mm: '',
    storage_volume_l: '',
  })

  const [errors, setErrors] = useState<Record<string, string>>({})

  const validateFields = () => {
    const newErrors: Record<string, string> = {}

    // Validate length_m
    if (fields.length_m) {
      const len = parseFloat(fields.length_m)
      if (len < 2 || len > 100) {
        newErrors.length_m = 'Länge muss zwischen 2 und 100 m liegen'
      }
    }

    // Validate beam_m
    if (fields.beam_m && fields.length_m) {
      const beam = parseFloat(fields.beam_m)
      const length = parseFloat(fields.length_m)
      if (beam >= length) {
        newErrors.beam_m = 'Breite muss kleiner als Länge sein'
      }
    }

    setErrors(newErrors)
    return Object.keys(newErrors).length === 0
  }

  const handleChange = (name: string, value: string) => {
    setFields((prev) => ({ ...prev, [name]: value }))
    // Clear error for this field when user starts typing
    if (errors[name]) {
      setErrors((prev) => {
        const newErrors = { ...prev }
        delete newErrors[name]
        return newErrors
      })
    }
  }

  const handleSubmit = (e: React.FormEvent) => {
    e.preventDefault()
    if (!validateFields()) {
      return
    }
    const num = (k: string) => (fields[k] !== '' ? parseFloat(fields[k]) : null)
    const int = (k: string) => (fields[k] !== '' ? parseInt(fields[k], 10) : null)
    const bool = (k: string): boolean | null => {
      if (fields[k] === 'true') return true
      if (fields[k] === 'false') return false
      return null
    }
    const specs: PublicSpecs = {
      boat_class: boatClass,
      length_m: parseFloat(fields.length_m),
      beam_m: num('beam_m'),
      draft_m: num('draft_m'),
      displacement_kg: num('displacement_kg'),
      cabin_count: int('cabin_count'),
      berth_count: int('berth_count'),
      head_count: int('head_count'),
      cockpit_area_sqm: num('cockpit_area_sqm'),
      salon_area_sqm: num('salon_area_sqm'),
      pantry_type: fields.pantry_type || null,
      helm_position: fields.helm_position || null,
      has_flybridge: bool('has_flybridge'),
      has_crew_quarters: bool('has_crew_quarters'),
      engine_hp: num('engine_hp'),
      engine_count: int('engine_count'),
      fuel_capacity_l: num('fuel_capacity_l'),
      water_capacity_l: num('water_capacity_l'),
      sail_area_sqm: num('sail_area_sqm'),
      max_speed_kn: num('max_speed_kn'),
      price_eur: num('price_eur'),
      year: int('year'),
      brand: fields.brand || null,
      model_name: fields.model_name || null,
      deck_height_mm: num('deck_height_mm'),
      storage_volume_l: num('storage_volume_l'),
    }
    onSubmit(specs)
  }

  const isSailboat = boatClass === 'small_sail' || boatClass === 'cruising_sail'

  return (
    <form onSubmit={handleSubmit} className="space-y-5">
      {/* Abmessungen — always open, length required */}
      <Section title="Abmessungen" defaultOpen hint="Erforderlich">
        <Field
          label="Länge über alles"
          name="length_m"
          unit="m"
          placeholder="z.B. 12.5"
          value={fields.length_m}
          onChange={handleChange}
          required
          min={3}
          step={0.1}
          error={errors.length_m}
        />
        <Field
          label="Breite (Bmax)"
          name="beam_m"
          unit="m"
          placeholder="z.B. 4.2"
          value={fields.beam_m}
          onChange={handleChange}
          step={0.1}
          error={errors.beam_m}
        />
        <Field
          label="Tiefgang"
          name="draft_m"
          unit="m"
          placeholder="z.B. 1.8"
          value={fields.draft_m}
          onChange={handleChange}
          step={0.01}
        />
        <Field
          label="Verdrängung"
          name="displacement_kg"
          unit="kg"
          placeholder="z.B. 8500"
          value={fields.displacement_kg}
          onChange={handleChange}
        />
        <Field
          label="Stehhöhe Innen"
          name="deck_height_mm"
          unit="mm"
          placeholder="z.B. 1950"
          value={fields.deck_height_mm}
          onChange={handleChange}
        />
      </Section>

      {/* Layout */}
      <Section title="Layout & Raumaufteilung">
        <Field
          label="Anzahl Kabinen"
          name="cabin_count"
          placeholder="z.B. 3"
          value={fields.cabin_count}
          onChange={handleChange}
        />
        <Field
          label="Anzahl Schlafplätze"
          name="berth_count"
          placeholder="z.B. 6"
          value={fields.berth_count}
          onChange={handleChange}
        />
        <Field
          label="Anzahl Nasszellen"
          name="head_count"
          placeholder="z.B. 2"
          value={fields.head_count}
          onChange={handleChange}
        />
        <Field
          label="Cockpit-Fläche"
          name="cockpit_area_sqm"
          unit="m²"
          placeholder="z.B. 6.5"
          value={fields.cockpit_area_sqm}
          onChange={handleChange}
          step={0.1}
        />
        <Field
          label="Salon-Fläche"
          name="salon_area_sqm"
          unit="m²"
          placeholder="z.B. 12.0"
          value={fields.salon_area_sqm}
          onChange={handleChange}
          step={0.1}
        />
        <Field
          label="Stauraumvolumen"
          name="storage_volume_l"
          unit="Liter"
          placeholder="z.B. 800"
          value={fields.storage_volume_l}
          onChange={handleChange}
        />
        <div>
          <label className="block text-xs font-semibold tracking-wider-premium uppercase text-navy-400 mb-2">Steuerstand-Position</label>
          <select
            value={fields.helm_position}
            onChange={(e) => handleChange('helm_position', e.target.value)}
            className="w-full bg-navy-800/50 border border-navy-600/40 rounded-lg px-4 py-2.5 text-white text-sm focus:outline-none focus:border-ocean-600 transition-colors duration-200"
          >
            <option value="">Nicht angegeben</option>
            <option value="cockpit">Cockpit</option>
            <option value="flybridge">Flybridge</option>
            <option value="wheelhouse">Wheelhouse</option>
          </select>
        </div>
        <div>
          <label className="block text-xs font-semibold tracking-wider-premium uppercase text-navy-400 mb-2">Flybridge vorhanden</label>
          <select
            value={fields.has_flybridge}
            onChange={(e) => handleChange('has_flybridge', e.target.value)}
            className="w-full bg-navy-800/50 border border-navy-600/40 rounded-lg px-4 py-2.5 text-white text-sm focus:outline-none focus:border-ocean-600 transition-colors duration-200"
          >
            <option value="">Nicht angegeben</option>
            <option value="true">Ja</option>
            <option value="false">Nein</option>
          </select>
        </div>
        {(boatClass === 'large_motor' || boatClass === 'superyacht') && (
          <div>
            <label className="block text-xs font-semibold tracking-wider-premium uppercase text-navy-400 mb-2">Crew-Quarters vorhanden</label>
            <select
              value={fields.has_crew_quarters}
              onChange={(e) => handleChange('has_crew_quarters', e.target.value)}
              className="w-full bg-navy-800/50 border border-navy-600/40 rounded-lg px-4 py-2.5 text-white text-sm focus:outline-none focus:border-ocean-600 transition-colors duration-200"
            >
              <option value="">Nicht angegeben</option>
              <option value="true">Ja</option>
              <option value="false">Nein</option>
            </select>
          </div>
        )}
      </Section>

      {/* Antrieb */}
      <Section title="Antrieb & Kapazitäten">
        <Field
          label="Motorleistung"
          name="engine_hp"
          unit="PS"
          placeholder="z.B. 150"
          value={fields.engine_hp}
          onChange={handleChange}
        />
        <Field
          label="Anzahl Motoren"
          name="engine_count"
          placeholder="z.B. 2"
          value={fields.engine_count}
          onChange={handleChange}
        />
        <Field
          label="Tankvolumen"
          name="fuel_capacity_l"
          unit="Liter"
          placeholder="z.B. 400"
          value={fields.fuel_capacity_l}
          onChange={handleChange}
        />
        <Field
          label="Frischwasservolumen"
          name="water_capacity_l"
          unit="Liter"
          placeholder="z.B. 300"
          value={fields.water_capacity_l}
          onChange={handleChange}
        />
        <Field
          label="Höchstgeschwindigkeit"
          name="max_speed_kn"
          unit="kn"
          placeholder="z.B. 28"
          value={fields.max_speed_kn}
          onChange={handleChange}
          step={0.5}
        />
        {isSailboat && (
          <Field
            label="Segelfläche"
            name="sail_area_sqm"
            unit="m²"
            placeholder="z.B. 95"
            value={fields.sail_area_sqm}
            onChange={handleChange}
            step={0.5}
          />
        )}
      </Section>

      {/* Kommerziell */}
      <Section title="Kommerziell & Identifikation">
        <Field
          label="Marke / Werft"
          name="brand"
          type="text"
          placeholder="z.B. Hallberg-Rassy"
          value={fields.brand}
          onChange={handleChange}
        />
        <Field
          label="Modellname"
          name="model_name"
          type="text"
          placeholder="z.B. HR 48"
          value={fields.model_name}
          onChange={handleChange}
        />
        <Field
          label="Baujahr"
          name="year"
          placeholder="z.B. 2024"
          value={fields.year}
          onChange={handleChange}
          min={1960}
        />
        <Field
          label="Listenpreis"
          name="price_eur"
          unit="EUR"
          placeholder="z.B. 450000"
          value={fields.price_eur}
          onChange={handleChange}
        />
      </Section>

      <div className="bg-navy-900/40 border border-navy-700/40 rounded-xl px-6 py-4 text-sm text-navy-400 backdrop-blur-sm">
        Mehr Details führen zu besseren Ergebnissen. Felder ohne Angaben werden anhand der Bootsklasse geschätzt.
      </div>

      <div className="flex gap-3 pt-4">
        <button
          type="button"
          onClick={onBack}
          className="px-6 py-2.5 rounded-lg bg-navy-800/50 border border-navy-700/50 text-navy-300 hover:bg-navy-800 text-sm font-medium transition-colors duration-200 backdrop-blur-sm"
        >
          Zurück
        </button>
        <button
          type="submit"
          disabled={loading || fields.length_m === '' || Object.keys(errors).length > 0}
          className="flex-1 px-6 py-2.5 rounded-lg bg-ocean-700 hover:bg-ocean-600 text-white font-semibold text-sm transition-colors duration-200 disabled:opacity-50 disabled:cursor-not-allowed"
        >
          {loading ? 'Analysiere...' : 'Analysieren'}
        </button>
      </div>
    </form>
  )
}
