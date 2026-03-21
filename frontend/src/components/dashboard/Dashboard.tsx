import { useEffect, useState } from 'react'
import { FolderOpen, Ship } from 'lucide-react'
import { listProjects } from '../../services/api'
import HeroSection from '../layout/HeroSection'
import { MEDIA } from '../../config/media'
import type { Project } from '../../types'
import { BOAT_CLASS_LABELS, STATUS_LABELS } from '../../types'

interface DashboardProps {
  onSelectProject: (id: string) => void
}

const STATUS_COLORS: Record<string, string> = {
  draft: 'bg-navy-700/60 text-navy-200 border border-navy-600/40',
  active: 'bg-ocean-900/60 text-ocean-200 border border-ocean-600/40',
  review: 'bg-amber-900/60 text-amber-200 border border-amber-600/40',
  archived: 'bg-navy-800/60 text-navy-300 border border-navy-700/40',
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
      <HeroSection
        backgroundImage={MEDIA.hero.sailing_wide}
        title="Projekte"
        label="Yacht Design Verwaltung"
      />

      <div className="px-10 py-12">
        {projects.length === 0 ? (
          <div className="text-center py-16">
            <FolderOpen className="w-16 h-16 mx-auto mb-4 text-navy-600" />
            <p className="text-navy-400 text-lg">Noch keine Projekte vorhanden</p>
            <p className="text-navy-500 text-sm mt-2">Erstellen Sie Ihr erstes Yacht-Design-Projekt</p>
          </div>
        ) : (
          <div className="grid gap-6 md:grid-cols-2 lg:grid-cols-3">
            {projects.map((project) => (
              <button
                key={project.id}
                onClick={() => onSelectProject(project.id)}
                className="card-premium group text-left px-8 py-6 transition-all duration-200 hover:bg-navy-900/80 hover:border-ocean-600/60"
              >
                <div className="flex items-start justify-between mb-4">
                  <Ship className="w-6 h-6 text-ocean-500 transition-colors duration-200 group-hover:text-ocean-400" />
                  <span
                    className={`text-xs px-3 py-1.5 rounded-md font-semibold uppercase tracking-wider-premium transition-colors duration-200 ${STATUS_COLORS[project.status] || ''}`}
                  >
                    {STATUS_LABELS[project.status]}
                  </span>
                </div>

                <h3 className="font-serif text-title font-medium text-white mb-2 group-hover:text-ocean-200 transition-colors duration-200">
                  {project.name}
                </h3>

                {project.description && (
                  <p className="text-sm text-navy-300 mb-4 leading-relaxed">
                    {project.description}
                  </p>
                )}

                <div className="border-t border-navy-700/40 pt-4 space-y-3">
                  <div className="flex items-center justify-between text-xs">
                    <span className="label-premium">Bootsklasse</span>
                    <span className="text-ocean-300 font-medium">
                      {BOAT_CLASS_LABELS[project.boat_class]}
                    </span>
                  </div>
                  <div className="flex items-center justify-between text-xs">
                    <span className="label-premium">Abmessungen</span>
                    <span className="text-ocean-300 font-medium font-mono">
                      {project.length_m}m × {project.beam_m}m
                    </span>
                  </div>
                </div>
              </button>
            ))}
          </div>
        )}
      </div>
    </div>
  )
}
