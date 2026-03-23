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
  draft: 'bg-sand-200 text-navy-700 border border-sand-300',
  active: 'bg-ocean-100 text-ocean-700 border border-ocean-300',
  review: 'bg-amber-100 text-amber-700 border border-amber-300',
  archived: 'bg-gray-100 text-gray-700 border border-gray-300',
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
    return (
      <div className="px-6 md:px-10 py-12">
        <div className="grid gap-6 sm:grid-cols-2 lg:grid-cols-3">
          {Array.from({ length: 6 }).map((_, i) => (
            <div key={i} className="card-premium px-8 py-6 space-y-4">
              <div className="flex items-start justify-between">
                <div className="skeleton w-6 h-6 rounded" />
                <div className="skeleton w-16 h-6 rounded-md" />
              </div>
              <div className="skeleton w-3/4 h-5 rounded" />
              <div className="skeleton w-full h-4 rounded" />
              <div className="border-t border-sand-200 pt-4 space-y-3">
                <div className="flex justify-between">
                  <div className="skeleton w-20 h-3 rounded" />
                  <div className="skeleton w-24 h-3 rounded" />
                </div>
                <div className="flex justify-between">
                  <div className="skeleton w-20 h-3 rounded" />
                  <div className="skeleton w-24 h-3 rounded" />
                </div>
              </div>
            </div>
          ))}
        </div>
      </div>
    )
  }

  if (error) {
    return (
      <div className="max-w-2xl mx-auto px-10 py-12">
        <div className="bg-red-950/20 border border-red-700/40 rounded-xl p-6 text-red-300">
          Fehler beim Laden der Projekte: {error}
        </div>
      </div>
    )
  }

  return (
    <>
      <div>
        <HeroSection
          backgroundVideo={MEDIA.video.sailing_aerial}
          backgroundImage={MEDIA.hero.sailing_wide}
          title="Projekte"
          label="Yacht Design Verwaltung"
        />

        <div className="px-6 md:px-10 py-12">
          {projects.length === 0 ? (
            <div className="text-center py-16">
              <div className="mb-4">
                <FolderOpen className="w-16 h-16 mx-auto text-navy-600" />
              </div>
              <p className="text-navy-700 text-lg font-serif">Noch keine Projekte vorhanden</p>
              <p className="text-navy-600 text-sm mt-2">Erstellen Sie Ihr erstes Yacht-Design-Projekt</p>
            </div>
          ) : (
            <div className="grid gap-6 sm:grid-cols-2 lg:grid-cols-3">
              {projects.map((project, idx) => (
                <button
                  key={project.id}
                  onClick={() => onSelectProject(project.id)}
                  className={`card-premium group text-left px-8 py-6 animate-fade-in-up focus-visible:ring-2 focus-visible:ring-ocean-300 ${
                    project.status === 'archived' ? 'opacity-75 grayscale-[30%]' : ''
                  }`}
                  style={{ animationDelay: `${idx * 100}ms` }}
                  aria-label={`Projekt ${project.name}, Status: ${STATUS_LABELS[project.status]}`}
                >
                  <div className="flex items-start justify-between mb-4">
                    <Ship className="w-6 h-6 text-ocean-600 transition-colors duration-300 group-hover:text-ocean-700" />
                    <span
                      className={`text-xs px-3 py-1.5 rounded-md font-semibold uppercase tracking-wider-premium transition-all duration-300 ${STATUS_COLORS[project.status] || ''}`}
                    >
                      {STATUS_LABELS[project.status]}
                    </span>
                  </div>

                  <h3 className="font-serif text-title font-medium text-navy-900 mb-2 group-hover:text-ocean-700 transition-colors duration-300">
                    {project.name}
                  </h3>

                  {project.description && (
                    <p className="text-sm text-navy-700 mb-4 leading-relaxed line-clamp-2">
                      {project.description}
                    </p>
                  )}

                  <div className="border-t border-sand-200 pt-4 space-y-3">
                    <div className="flex items-center justify-between text-xs">
                      <span className="label-premium">Bootsklasse</span>
                      <span className="text-ocean-600 font-medium">
                        {BOAT_CLASS_LABELS[project.boat_class]}
                      </span>
                    </div>
                    <div className="flex items-center justify-between text-xs">
                      <span className="label-premium">Abmessungen</span>
                      <span className="text-ocean-600 font-medium font-mono">
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
    </>
  )
}
