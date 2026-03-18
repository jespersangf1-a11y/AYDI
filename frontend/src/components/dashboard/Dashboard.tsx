import { useEffect, useState } from 'react'
import { FolderOpen, Ship } from 'lucide-react'
import { listProjects } from '../../services/api'
import type { Project } from '../../types'
import { BOAT_CLASS_LABELS, STATUS_LABELS } from '../../types'

interface DashboardProps {
  onSelectProject: (id: string) => void
}

const STATUS_COLORS: Record<string, string> = {
  draft: 'bg-navy-700 text-navy-300',
  active: 'bg-ocean-900 text-ocean-300',
  review: 'bg-amber-900 text-amber-300',
  archived: 'bg-navy-800 text-navy-400',
}

export default function Dashboard({ onSelectProject }: DashboardProps) {
  const [projects, setProjects] = useState<Project[]>([])
  const [loading, setLoading] = useState(true)
  const [error, setError] = useState<string | null>(null)

  useEffect(() => {
    listProjects()
      .then(setProjects)
      .catch((e) => setError(e.message))
      .finally(() => setLoading(false))
  }, [])

  if (loading) {
    return <div className="text-navy-400">Lade Projekte...</div>
  }

  if (error) {
    return <div className="text-red-400">Fehler: {error}</div>
  }

  return (
    <div>
      <h2 className="font-heading text-2xl font-bold text-white mb-6">Projekte</h2>
      {projects.length === 0 ? (
        <div className="text-center py-12 text-navy-400">
          <FolderOpen className="w-12 h-12 mx-auto mb-4 opacity-50" />
          <p>Noch keine Projekte vorhanden</p>
        </div>
      ) : (
        <div className="grid gap-4 md:grid-cols-2 lg:grid-cols-3">
          {projects.map((project) => (
            <button
              key={project.id}
              onClick={() => onSelectProject(project.id)}
              className="text-left bg-navy-900 border border-navy-700 rounded-xl p-5 hover:border-ocean-500 transition-colors"
            >
              <div className="flex items-start justify-between mb-3">
                <Ship className="w-5 h-5 text-ocean-400" />
                <span
                  className={`text-xs px-2 py-0.5 rounded-full ${STATUS_COLORS[project.status] || ''}`}
                >
                  {STATUS_LABELS[project.status]}
                </span>
              </div>
              <h3 className="font-heading font-semibold text-white mb-1">{project.name}</h3>
              <p className="text-sm text-navy-400 mb-3">{project.description}</p>
              <div className="flex gap-4 text-xs text-navy-400">
                <span>{BOAT_CLASS_LABELS[project.boat_class]}</span>
                <span className="font-mono">{project.length_m}m × {project.beam_m}m</span>
              </div>
            </button>
          ))}
        </div>
      )}
    </div>
  )
}
