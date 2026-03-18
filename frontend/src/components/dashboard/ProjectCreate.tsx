import { useState } from 'react'
import { Save, X } from 'lucide-react'
import { createProject, createLayout, importDxf } from '../../services/api'
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
          const data = JSON.parse(text) as { zones: ZoneData[]; passages: PassageData[] }
          await createLayout(project.id, {
            name: 'Importiert aus JSON',
            zones: data.zones,
            passages: data.passages,
          })
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
    <div className="max-w-2xl">
      <h2 className="font-heading text-2xl font-bold text-white mb-6">Neues Projekt</h2>

      <form onSubmit={handleSubmit} className="space-y-5">
        <div>
          <label className="block text-sm font-medium text-navy-300 mb-1">Name *</label>
          <input
            type="text"
            value={name}
            onChange={(e) => setName(e.target.value)}
            required
            className="w-full bg-navy-900 border border-navy-700 rounded-lg px-4 py-2 text-white focus:border-ocean-500 focus:outline-none"
            placeholder="z.B. Meridian 40 Cruiser"
          />
        </div>

        <div>
          <label className="block text-sm font-medium text-navy-300 mb-1">Beschreibung</label>
          <textarea
            value={description}
            onChange={(e) => setDescription(e.target.value)}
            rows={3}
            className="w-full bg-navy-900 border border-navy-700 rounded-lg px-4 py-2 text-white focus:border-ocean-500 focus:outline-none resize-none"
          />
        </div>

        <div>
          <label className="block text-sm font-medium text-navy-300 mb-1">Bootsklasse *</label>
          <select
            value={boatClass}
            onChange={(e) => setBoatClass(e.target.value as BoatClass)}
            className="w-full bg-navy-900 border border-navy-700 rounded-lg px-4 py-2 text-white focus:border-ocean-500 focus:outline-none"
          >
            {Object.entries(BOAT_CLASS_LABELS).map(([value, label]) => (
              <option key={value} value={value}>{label}</option>
            ))}
          </select>
        </div>

        <div className="grid grid-cols-2 gap-4">
          <div>
            <label className="block text-sm font-medium text-navy-300 mb-1">Länge (m) *</label>
            <input
              type="number"
              step="0.1"
              min="1"
              value={lengthM}
              onChange={(e) => setLengthM(e.target.value)}
              required
              className="w-full bg-navy-900 border border-navy-700 rounded-lg px-4 py-2 text-white focus:border-ocean-500 focus:outline-none"
            />
          </div>
          <div>
            <label className="block text-sm font-medium text-navy-300 mb-1">Breite (m) *</label>
            <input
              type="number"
              step="0.1"
              min="1"
              value={beamM}
              onChange={(e) => setBeamM(e.target.value)}
              required
              className="w-full bg-navy-900 border border-navy-700 rounded-lg px-4 py-2 text-white focus:border-ocean-500 focus:outline-none"
            />
          </div>
        </div>

        <div>
          <label className="block text-sm font-medium text-navy-300 mb-1">Layout-Datei (optional)</label>
          <input
            type="file"
            accept=".json,.dxf"
            onChange={(e) => setLayoutFile(e.target.files?.[0] || null)}
            className="w-full bg-navy-900 border border-navy-700 rounded-lg px-4 py-2 text-white file:mr-4 file:py-1 file:px-3 file:rounded file:border-0 file:bg-ocean-600 file:text-white file:text-sm file:cursor-pointer"
          />
          <p className="text-xs text-navy-500 mt-1">JSON oder DXF-Datei mit Zonendaten</p>
        </div>

        {error && (
          <div className="bg-red-900/50 border border-red-700 rounded-lg p-3 text-red-300 text-sm">
            {error}
          </div>
        )}

        <div className="flex gap-3 pt-2">
          <button
            type="submit"
            disabled={submitting}
            className="flex items-center gap-2 bg-ocean-600 hover:bg-ocean-700 text-white px-5 py-2 rounded-lg font-medium transition-colors disabled:opacity-50"
          >
            <Save className="w-4 h-4" />
            {submitting ? 'Erstelle...' : 'Projekt erstellen'}
          </button>
          <button
            type="button"
            onClick={onCancel}
            className="flex items-center gap-2 text-navy-400 hover:text-white px-5 py-2 rounded-lg transition-colors"
          >
            <X className="w-4 h-4" />
            Abbrechen
          </button>
        </div>
      </form>
    </div>
  )
}
