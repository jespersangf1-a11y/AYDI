import { useState } from 'react'
import { Save, X, Upload } from 'lucide-react'
import { createProject, createLayout, importDxf } from '../../services/api'
import HeroSection from '../layout/HeroSection'
import { MEDIA } from '../../config/media'
import type { BoatClass, ZoneData, PassageData } from '../../types'
import { BOAT_CLASS_LABELS } from '../../types'

interface ProjectCreateProps {
  onCreated: (id: string) => void
  onCancel: () => void
}

export default function ProjectCreate({ onCreated, onCancel }: ProjectCreateProps) {
  const [name, setName] = useState('')
  const [description, setDescription] = useState('')
  const [boatClass, setBoatClass] = useState<BoatClass>('cruising_sail')
  const [lengthM, setLengthM] = useState('')
  const [beamM, setBeamM] = useState('')
  const [layoutFile, setLayoutFile] = useState<File | null>(null)
  const [submitting, setSubmitting] = useState(false)
  const [error, setError] = useState<string | null>(null)

  const handleSubmit = async (e: React.FormEvent) => {
    e.preventDefault()
    setError(null)
    setSubmitting(true)

    try {
      const project = await createProject({
        name,
        description: description || undefined,
        boat_class: boatClass,
        length_m: parseFloat(lengthM),
        beam_m: parseFloat(beamM),
      })

      if (layoutFile) {
        if (layoutFile.name.toLowerCase().endsWith('.dxf')) {
          const dxfResult = await importDxf(project.id, layoutFile, 'Importiert aus DXF')
          await createLayout(project.id, {
            name: 'Importiert aus DXF',
            zones: dxfResult.zones,
            passages: dxfResult.passages,
          })
        } else {
          const text = await layoutFile.text()
          try {
            const data = JSON.parse(text) as { zones: ZoneData[]; passages: PassageData[] }
            await createLayout(project.id, {
              name: 'Importiert aus JSON',
              zones: data.zones,
              passages: data.passages,
            })
          } catch (parseError) {
            throw new Error('JSON-Datei ist ungültig. Bitte überprüfen Sie das Format.')
          }
        }
      }

      onCreated(project.id)
    } catch (e) {
      setError(e instanceof Error ? e.message : 'Unbekannter Fehler')
    } finally {
      setSubmitting(false)
    }
  }

  return (
    <div>
      <HeroSection
        backgroundImage={MEDIA.hero.deck_detail}
        title="Neues Projekt"
        label="Yacht Design erstellen"
      />

      <div className="px-10 py-12">
        <div className="max-w-2xl">
          <form onSubmit={handleSubmit} className="space-y-8">
            {/* Project Name */}
            <div>
              <label className="label-premium block mb-3">Projektname *</label>
              <input
                type="text"
                value={name}
                onChange={(e) => setName(e.target.value)}
                required
                className="w-full card-premium px-6 py-4 text-navy-900 placeholder:text-navy-600 focus:border-ocean-400 focus:outline-none transition-colors duration-200"
                placeholder="z.B. Meridian 40 Cruiser"
              />
            </div>

            {/* Description */}
            <div>
              <label className="label-premium block mb-3">Beschreibung</label>
              <textarea
                value={description}
                onChange={(e) => setDescription(e.target.value)}
                rows={4}
                className="w-full card-premium px-6 py-4 text-navy-900 placeholder:text-navy-500 focus:bg-navy-900/70 focus:border-ocean-500 focus:outline-none resize-none transition-colors duration-200"
                placeholder="Beschreiben Sie die Hauptmerkmale und den Zweck dieses Entwurfs"
              />
            </div>

            {/* Boat Class */}
            <div>
              <label className="label-premium block mb-3">Bootsklasse *</label>
              <select
                value={boatClass}
                onChange={(e) => setBoatClass(e.target.value as BoatClass)}
                className="w-full card-premium px-6 py-4 text-navy-900 focus:border-ocean-400 focus:outline-none transition-colors duration-200 appearance-none bg-right"
                style={{
                  backgroundImage: `url("data:image/svg+xml;charset=UTF-8,%3csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 24 24' fill='none' stroke='%234ba7c3' stroke-width='2' stroke-linecap='round' stroke-linejoin='round'%3e%3cpolyline points='6 9 12 15 18 9'%3e%3c/polyline%3e%3c/svg%3e")`,
                  backgroundRepeat: 'no-repeat',
                  backgroundPosition: 'right 1rem center',
                  backgroundSize: '20px',
                  paddingRight: '2.5rem'
                }}
              >
                {Object.entries(BOAT_CLASS_LABELS).map(([value, label]) => (
                  <option key={value} value={value}>{label}</option>
                ))}
              </select>
            </div>

            {/* Dimensions */}
            <div className="grid grid-cols-2 gap-6">
              <div>
                <label className="label-premium block mb-3">Länge (m) *</label>
                <input
                  type="number"
                  step="0.1"
                  min="1"
                  value={lengthM}
                  onChange={(e) => setLengthM(e.target.value)}
                  required
                  className="w-full card-premium px-6 py-4 text-navy-900 placeholder:text-navy-600 focus:border-ocean-400 focus:outline-none transition-colors duration-200"
                  placeholder="z.B. 12.5"
                />
              </div>
              <div>
                <label className="label-premium block mb-3">Breite (m) *</label>
                <input
                  type="number"
                  step="0.1"
                  min="1"
                  value={beamM}
                  onChange={(e) => setBeamM(e.target.value)}
                  required
                  className="w-full card-premium px-6 py-4 text-navy-900 placeholder:text-navy-600 focus:border-ocean-400 focus:outline-none transition-colors duration-200"
                  placeholder="z.B. 4.2"
                />
              </div>
            </div>

            {/* File Upload */}
            <div>
              <label className="label-premium block mb-3">Layout-Datei (optional)</label>
              <div className="relative">
                <input
                  type="file"
                  accept=".json,.dxf"
                  onChange={(e) => setLayoutFile(e.target.files?.[0] || null)}
                  id="layout-file"
                  className="hidden"
                />
                <label
                  htmlFor="layout-file"
                  className="card-premium px-6 py-8 block text-center cursor-pointer hover:shadow-md hover:border-sand-300 transition-all duration-200 group"
                >
                  <div className="flex flex-col items-center">
                    <Upload className="w-8 h-8 text-ocean-600 mb-3 group-hover:text-ocean-700 transition-colors duration-200" />
                    {layoutFile ? (
                      <div>
                        <p className="text-navy-900 font-medium">{layoutFile.name}</p>
                        <p className="text-navy-600 text-sm mt-1">
                          {(layoutFile.size / 1024).toFixed(1)} KB
                        </p>
                      </div>
                    ) : (
                      <div>
                        <p className="text-navy-900 font-medium">Datei auswählen</p>
                        <p className="text-navy-600 text-sm mt-1">JSON oder DXF-Format</p>
                      </div>
                    )}
                  </div>
                </label>
              </div>
              <p className="text-navy-600 text-xs mt-3">
                Unterstützte Formate: JSON oder DXF mit Zonendaten
              </p>
            </div>

            {/* Error Message */}
            {error && (
              <div className="card-premium bg-red-50 border-red-300 px-6 py-4 text-red-700 text-sm">
                {error}
              </div>
            )}

            {/* Actions */}
            <div className="flex gap-4 pt-4">
              <button
                type="submit"
                disabled={submitting}
                className="flex items-center gap-2 bg-ocean-600 hover:bg-ocean-700 disabled:opacity-50 disabled:cursor-not-allowed text-white px-8 py-4 rounded-lg font-serif font-medium transition-colors duration-200"
              >
                {submitting ? (
                  <>
                    <span className="inline-block w-4 h-4 rounded-full border-2 border-current border-t-transparent animate-spin" />
                    Erstelle Projekt...
                  </>
                ) : (
                  <>
                    <Save className="w-4 h-4" />
                    Projekt erstellen
                  </>
                )}
              </button>
              <button
                type="button"
                onClick={onCancel}
                className="flex items-center gap-2 text-navy-700 hover:text-navy-900 px-8 py-4 rounded-lg transition-colors duration-200 font-medium"
              >
                <X className="w-4 h-4" />
                Abbrechen
              </button>
            </div>
          </form>
        </div>
      </div>
    </div>
  )
}
