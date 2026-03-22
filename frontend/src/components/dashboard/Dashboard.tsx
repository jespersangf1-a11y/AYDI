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

// Animations for dashboard
const dashboardAnimationStyles = `
  @keyframes projectCardSlideIn {
    from {
      opacity: 0;
      transform: translateY(24px);
    }
    to {
      opacity: 1;
      transform: translateY(0);
    }
  }

  @keyframes emptyStateFloat {
    0%, 100% { transform: translateY(0px); }
    50% { transform: translateY(-8px); }
  }

  @keyframes statusPulse {
    0%, 100% { opacity: 1; }
    50% { opacity: 0.7; }
  }

  @keyframes iconBounce {
    0%, 100% { transform: scale(1); }
    50% { transform: scale(1.1); }
  }

  .animate-project-in {
    animation: projectCardSlideIn 0.5s cubic-bezier(0.34, 1.56, 0.64, 1);
  }

  .animate-empty-float {
    animation: emptyStateFloat 3s ease-in-out infinite;
  }

  .animate-status-pulse {
    animation: statusPulse 2s ease-in-out infinite;
  }

  .animate-icon-bounce {
    animation: iconBounce 2s ease-in-out infinite;
  }

  .card-hover-lift {
    transition: all 0.4s cubic-bezier(0.34, 1.56, 0.64, 1);
  }

  .card-hover-lift:hover {
    transform: translateY(-12px);
    box-shadow: 0 32px 64px rgba(0, 176, 240, 0.2);
    border-color: rgba(0, 176, 240, 0.4);
  }
`

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
      <div className="text-center py-12">
        <div className="animate-spin rounded-full h-12 w-12 border-b-2 border-ocean-500 mx-auto mb-4" />
        <p className="text-navy-400">Projekte werden geladen...</p>
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
      <style>{dashboardAnimationStyles}</style>
      <div>
        <HeroSection
          backgroundImage={MEDIA.hero.sailing_wide}
          title="Projekte"
          label="Yacht Design Verwaltung"
        />

        <div className="px-6 md:px-10 py-12">
          {projects.length === 0 ? (
            <div className="text-center py-16">
              <div className="animate-empty-float mb-4">
                <FolderOpen className="w-16 h-16 mx-auto text-navy-600" />
              </div>
              <p className="text-navy-400 text-lg font-serif">Noch keine Projekte vorhanden</p>
              <p className="text-navy-500 text-sm mt-2">Erstellen Sie Ihr erstes Yacht-Design-Projekt</p>
            </div>
          ) : (
            <div className="grid gap-6 sm:grid-cols-2 lg:grid-cols-3">
              {projects.map((project, idx) => (
                <button
                  key={project.id}
                  onClick={() => onSelectProject(project.id)}
                  className="card-hover-lift card-premium group text-left px-8 py-6 animate-project-in"
                  style={{ animationDelay: `${idx * 100}ms` }}
                  aria-label={`Projekt ${project.name}, Status: ${STATUS_LABELS[project.status]}`}
                >
                  <div className="flex items-start justify-between mb-4">
                    <Ship className="w-6 h-6 text-ocean-500 transition-colors duration-300 group-hover:text-ocean-300 group-hover:animate-icon-bounce" />
                    <span
                      className={`text-xs px-3 py-1.5 rounded-md font-semibold uppercase tracking-wider-premium transition-all duration-300 ${
                        project.status === 'active' ? 'animate-status-pulse' : ''
                      } ${STATUS_COLORS[project.status] || ''}`}
                    >
                      {STATUS_LABELS[project.status]}
                    </span>
                  </div>

                  <h3 className="font-serif text-title font-medium text-white mb-2 group-hover:text-ocean-200 transition-colors duration-300">
                    {project.name}
                  </h3>

                  {project.description && (
                    <p className="text-sm text-navy-300 mb-4 leading-relaxed line-clamp-2">
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
    </>
  )
}
