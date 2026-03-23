import { useEffect, useState } from 'react'
import { ArrowLeft, Play, Ship, Zap, Clock, Layers, Calendar } from 'lucide-react'
import { getProject, listLayouts, listAnalyses, runAnalysis, runFullAnalysis, getLayoutVersions } from '../../services/api'
import HeroSection from '../layout/HeroSection'
import { MEDIA } from '../../config/media'
import type { Project, Layout, AnalysisResult, LayoutVersion } from '../../types'
import { BOAT_CLASS_LABELS, STATUS_LABELS } from '../../types'
import ScoreGauge from '../analysis/ScoreGauge'
import SubScoreBars from '../analysis/SubScoreBars'
import WarningList from '../analysis/WarningList'
import LayoutViewer from '../analysis/LayoutViewer'


interface ProjectDetailProps {
  projectId: string
  onBack: () => void
}

type TabType = 'overview' | 'layouts' | 'analysis' | 'history'

const MODULE_LABELS: Record<string, string> = {
  ergonomics: 'Ergonomie',
  volume_storage: 'Volumen/Stauraum',
}

export default function ProjectDetail({ projectId, onBack }: ProjectDetailProps) {
  const [project, setProject] = useState<Project | null>(null)
  const [layouts, setLayouts] = useState<Layout[]>([])
  const [analyses, setAnalyses] = useState<AnalysisResult[]>([])
  const [selectedLayout, setSelectedLayout] = useState<Layout | null>(null)
  const [selectedAnalysis, setSelectedAnalysis] = useState<AnalysisResult | null>(null)
  const [analyzing, setAnalyzing] = useState(false)
  const [fullAnalyzing, setFullAnalyzing] = useState(false)
  const [loading, setLoading] = useState(true)
  const [error, setError] = useState<string | null>(null)
  const [versions, setVersions] = useState<LayoutVersion[]>([])
  const [activeTab, setActiveTab] = useState<TabType>('layouts')

  useEffect(() => {
    setLoading(true)
    Promise.allSettled([
      getProject(projectId),
      listLayouts(projectId),
      listAnalyses(projectId),
    ])
      .then((results) => {
        const project = results[0].status === 'fulfilled' ? results[0].value : null
        const layouts = results[1].status === 'fulfilled' ? results[1].value : []
        const analyses = results[2].status === 'fulfilled' ? results[2].value : []

        if (project) setProject(project)
        else setError('Projekt konnte nicht geladen werden')

        setLayouts(layouts)
        setAnalyses(analyses)
        if (layouts.length > 0) setSelectedLayout(layouts[0])
        if (analyses.length > 0) setSelectedAnalysis(analyses[0])
      })
      .catch((e) => setError(e.message))
      .finally(() => setLoading(false))
  }, [projectId])

  const handleRunAnalysis = async (module: string) => {
    if (!selectedLayout) return
    setAnalyzing(true)
    setError(null)
    try {
      const result = await runAnalysis(projectId, selectedLayout.id, module)
      setAnalyses((prev) => [result, ...prev])
      setSelectedAnalysis(result)
    } catch (e) {
      setError(e instanceof Error ? e.message : 'Analysefehler')
    } finally {
      setAnalyzing(false)
    }
  }

  const handleRunFullAnalysis = async () => {
    if (!selectedLayout) return
    setFullAnalyzing(true)
    setError(null)
    try {
      await runFullAnalysis(projectId, selectedLayout.id)
      // Refresh analyses
      const refreshedAnalyses = await listAnalyses(projectId)
      setAnalyses(refreshedAnalyses)
      if (refreshedAnalyses.length > 0) {
        setSelectedAnalysis(refreshedAnalyses[0])
      }
    } catch (e) {
      setError(e instanceof Error ? e.message : 'Vollanalyse fehlgeschlagen')
    } finally {
      setFullAnalyzing(false)
    }
  }

  const handleLoadVersions = async () => {
    if (!selectedLayout) return
    try {
      const v = await getLayoutVersions(projectId, selectedLayout.id)
      setVersions(v)
      setActiveTab('history')
    } catch (e) {
      setError(e instanceof Error ? e.message : 'Versionsverlauf konnte nicht geladen werden')
    }
  }

  const handleSelectVersion = (_version: LayoutVersion) => {
    // In a real implementation, this would load the layout data from the version
  }

  if (loading) {
    return <div className="text-navy-600">Lade...</div>
  }

  if (error && !project) {
    return <div className="text-red-400">Fehler: {error}</div>
  }

  if (!project) {
    return <div className="text-navy-600">Lade...</div>
  }

  const tabs: { id: TabType; label: string; icon: React.ReactNode }[] = [
    { id: 'layouts', label: 'Layouts', icon: <Layers className="w-4 h-4" /> },
    { id: 'analysis', label: 'Analyse', icon: <Zap className="w-4 h-4" /> },
    { id: 'history', label: 'Versionshistorie', icon: <Clock className="w-4 h-4" /> },
  ]

  return (
    <div>
      <HeroSection
        backgroundImage={MEDIA.hero.deck_detail}
        title={project.name}
        subtitle={`${BOAT_CLASS_LABELS[project.boat_class]} · ${project.length_m}m × ${project.beam_m}m`}
        label="Projektdetails"
      />

      <div className="px-4 sm:px-10 py-8">
        {/* Back Button */}
        <button
          onClick={onBack}
          className="flex items-center gap-2 text-navy-600 hover:text-ocean-700 transition-colors duration-200 mb-8"
        >
          <ArrowLeft className="w-5 h-5" />
          <span className="text-sm font-medium">Zurück</span>
        </button>

        {error && (
          <div className="card-premium bg-red-900/20 border-red-700/40 p-4 text-red-300 text-sm mb-8">
            {error}
          </div>
        )}

        {/* Project Meta */}
        <div className="card-premium px-8 py-6 mb-10 flex items-center justify-between">
          <div className="flex items-center gap-4">
            <Ship className="w-8 h-8 text-ocean-500" />
            <div>
              <p className="label-premium mb-1">Projektstatus</p>
              <p className="text-navy-900 font-serif text-lg">
                {STATUS_LABELS[project.status]}
              </p>
            </div>
          </div>
          {project.description && (
            <p className="text-navy-700 text-sm max-w-md text-right">
              {project.description}
            </p>
          )}
        </div>

        {/* Tab Navigation with Sliding Indicator */}
        <div className="border-b border-sand-200 mb-8 flex gap-4 sm:gap-8 overflow-x-auto scrollbar-hide">
          <div className="relative flex gap-4 sm:gap-8 min-w-full">
            {tabs.map((tab) => (
              <button
                key={tab.id}
                onClick={() => setActiveTab(tab.id)}
                className={`flex items-center gap-2 pb-4 font-medium text-sm transition-colors duration-200 relative whitespace-nowrap ${
                  activeTab === tab.id
                    ? 'text-ocean-600'
                    : 'text-navy-600 hover:text-navy-700'
                }`}
                aria-selected={activeTab === tab.id}
                aria-label={tab.label}
              >
                {tab.icon}
                {tab.label}
                {activeTab === tab.id && (
                  <div className="absolute bottom-0 left-0 right-0 h-0.5 bg-gradient-to-r from-ocean-500 to-ocean-400 transition-all duration-300" />
                )}
              </button>
            ))}
          </div>
        </div>

        {/* Tab Content with Smooth Transitions */}
        {activeTab === 'layouts' && (
          <div className="space-y-8 animate-fade-in-up">
            {/* Layout Selector */}
            {layouts.length > 0 && (
              <div>
                <p className="label-premium mb-4">Verfügbare Layouts</p>
                <div className="grid gap-4 md:grid-cols-2">
                  {layouts.map((layout, idx) => (
                    <button
                      key={layout.id}
                      onClick={() => setSelectedLayout(layout)}
                      style={{ animationDelay: `${idx * 100}ms` }}
                      className={`animate-fade-in-up card-premium px-6 py-5 text-left transition-all duration-300 hover:shadow-lg hover:shadow-ocean-500/10 group ${
                        selectedLayout?.id === layout.id
                          ? 'bg-ocean-900/40 border-ocean-600/60'
                          : 'hover:bg-navy-900/60 hover:border-sand-200'
                      }`}
                      aria-selected={selectedLayout?.id === layout.id}
                      aria-label={`Layout ${layout.name}`}
                    >
                      <div className="font-serif text-lg font-medium text-navy-900 mb-1 group-hover:text-ocean-700 transition-colors">
                        {layout.name}
                      </div>
                      <div className="text-xs text-navy-600">
                        Version {layout.version}
                      </div>
                    </button>
                  ))}
                </div>
              </div>
            )}

            {/* Layout Viewer */}
            {selectedLayout && (
              <div className="card-premium p-0 overflow-hidden">
                <LayoutViewer zones={selectedLayout.zones} passages={selectedLayout.passages} />
              </div>
            )}

            {layouts.length === 0 && (
              <div className="card-premium px-8 py-12 text-center">
                <Layers className="w-12 h-12 mx-auto mb-4 text-navy-600" />
                <p className="text-navy-600">Noch kein Layout vorhanden</p>
              </div>
            )}
          </div>
        )}

        {activeTab === 'analysis' && (
          <div className="space-y-8 animate-fade-in-up">
            {/* Full Analysis */}
            {selectedLayout && (
              <div className="card-premium px-8 py-6 bg-gradient-to-br from-ocean-900/40 to-navy-900/40 border-ocean-600/40 hover:shadow-lg hover:shadow-ocean-500/10 transition-all duration-300">
                <div className="flex flex-col sm:flex-row items-start sm:items-center justify-between gap-4">
                  <div>
                    <p className="label-premium mb-2">Umfassende Analyse</p>
                    <p className="text-navy-900 font-serif text-lg">
                      Alle Module analysieren
                    </p>
                  </div>
                  <button
                    onClick={handleRunFullAnalysis}
                    disabled={fullAnalyzing || !selectedLayout}
                    className="flex items-center gap-2 bg-ocean-700 hover:bg-ocean-600 disabled:opacity-50 disabled:cursor-not-allowed text-navy-900 px-6 py-3 rounded-lg font-medium transition-all duration-200 hover:shadow-lg hover:shadow-ocean-700/30"
                    aria-label="Vollständige Analyse starten"
                  >
                    {fullAnalyzing ? (
                      <>
                        <span className="inline-block w-4 h-4 rounded-full border-2 border-current border-t-transparent animate-spin" />
                        Läuft...
                      </>
                    ) : (
                      <>
                        <Zap className="w-4 h-4" />
                        Starten
                      </>
                    )}
                  </button>
                </div>
              </div>
            )}

            {/* Module Analysis */}
            {selectedLayout && (
              <div>
                <p className="label-premium mb-4">Modul-Analyse</p>
                <div className="grid gap-3">
                  {['ergonomics', 'volume_storage'].map((module, idx) => (
                    <button
                      key={module}
                      onClick={() => handleRunAnalysis(module)}
                      disabled={analyzing}
                      style={{ animationDelay: `${idx * 100}ms` }}
                      className="animate-fade-in-up card-premium px-6 py-4 flex items-center justify-between hover:bg-navy-900/60 hover:border-sand-200 hover:shadow-lg hover:shadow-ocean-500/10 disabled:opacity-50 transition-all duration-200 group"
                      aria-label={`${MODULE_LABELS[module]} analysieren`}
                    >
                      <span className="text-navy-900 font-medium group-hover:text-ocean-700 transition-colors">
                        {MODULE_LABELS[module]}
                      </span>
                      <Play className="w-4 h-4 text-ocean-500 group-hover:scale-110 transition-transform" />
                    </button>
                  ))}
                </div>
              </div>
            )}

            {/* Analysis Results */}
            {selectedAnalysis && (
              <div className="space-y-8">
                <div className="animate-fade-in-up">
                  <p className="label-premium mb-4">Analyseergebnisse</p>
                  <p className="text-navy-900 font-serif text-lg mb-6">
                    {MODULE_LABELS[selectedAnalysis.module] || selectedAnalysis.module}
                  </p>
                  <div className="card-premium px-8 py-8 flex items-center justify-center hover:shadow-lg hover:shadow-ocean-500/10 transition-all duration-300">
                    <ScoreGauge
                      score={selectedAnalysis.overall_score}
                      label="Gesamtbewertung"
                    />
                  </div>
                </div>

                <div className="animate-fade-in-up card-premium px-8 py-6 hover:shadow-lg hover:shadow-ocean-500/10 transition-all duration-300" style={{ animationDelay: '100ms' }}>
                  <p className="label-premium mb-4">Teilbewertungen</p>
                  <SubScoreBars subScores={selectedAnalysis.sub_scores} />
                </div>

                {selectedAnalysis.warnings.length > 0 && (
                  <div className="animate-fade-in-up card-premium px-8 py-6 hover:shadow-lg hover:shadow-orange-500/10 transition-all duration-300" style={{ animationDelay: '200ms' }}>
                    <p className="label-premium mb-4">
                      Warnungen ({selectedAnalysis.warnings.length})
                    </p>
                    <WarningList warnings={selectedAnalysis.warnings} />
                  </div>
                )}
              </div>
            )}

            {/* Analysis History */}
            {analyses.length > 1 && (
              <div className="animate-fade-in-up">
                <p className="label-premium mb-4">Analysehistorie</p>
                <div className="space-y-2">
                  {analyses.map((a, idx) => (
                    <button
                      key={a.id}
                      onClick={() => setSelectedAnalysis(a)}
                      style={{ animationDelay: `${idx * 80}ms` }}
                      className={`animate-fade-in-up card-premium px-6 py-4 text-left flex items-center justify-between transition-all duration-200 hover:shadow-lg hover:shadow-ocean-500/10 group ${
                        selectedAnalysis?.id === a.id
                          ? 'bg-ocean-900/40 border-ocean-600/60'
                          : 'hover:bg-navy-900/60 hover:border-sand-200'
                      }`}
                      aria-selected={selectedAnalysis?.id === a.id}
                      aria-label={`${MODULE_LABELS[a.module] || a.module} - ${Math.round(a.overall_score)} von 100`}
                    >
                      <span className="text-navy-900 font-medium group-hover:text-ocean-700 transition-colors">
                        {MODULE_LABELS[a.module] || a.module}
                      </span>
                      <span className="text-ocean-600 font-mono text-sm font-semibold">
                        {Math.round(a.overall_score)}/100
                      </span>
                    </button>
                  ))}
                </div>
              </div>
            )}
          </div>
        )}

        {activeTab === 'history' && (
          <div className="animate-fade-in-up">
            <p className="label-premium mb-4">Versionshistorie</p>
            {versions.length > 0 ? (
              <div className="space-y-3">
                {versions.map((version, idx) => (
                  <button
                    key={version.id}
                    onClick={() => handleSelectVersion(version)}
                    style={{ animationDelay: `${idx * 80}ms` }}
                    className="animate-fade-in-up card-premium px-6 py-5 text-left hover:bg-navy-900/60 hover:border-sand-200 hover:shadow-lg hover:shadow-ocean-500/10 transition-all duration-200 group relative"
                    aria-label={`Version ${version.version_number}`}
                  >
                    {/* Timeline indicator */}
                    <div className="absolute left-0 top-1/2 w-3 h-3 -translate-x-5 -translate-y-1/2 rounded-full bg-ocean-500 border-2 border-navy-900 group-hover:scale-125 transition-transform" />

                    <div className="flex items-start justify-between">
                      <div>
                        <div className="font-mono text-ocean-600 font-semibold mb-1 group-hover:text-ocean-200 transition-colors">
                          Version {version.version_number}
                        </div>
                        <div className="flex items-center gap-2 text-sm text-navy-600">
                          <Calendar className="w-3 h-3" />
                          {new Date(version.created_at).toLocaleString('de-DE')}
                        </div>
                        {version.change_summary && (
                          <div className="text-sm text-navy-700 mt-2">
                            {version.change_summary}
                          </div>
                        )}
                      </div>
                    </div>
                  </button>
                ))}
              </div>
            ) : (
              <button
                onClick={handleLoadVersions}
                className="card-premium px-8 py-6 text-center hover:bg-navy-900/60 hover:border-sand-200 hover:shadow-lg hover:shadow-ocean-500/10 transition-all duration-200 w-full"
                aria-label="Versionshistorie laden"
              >
                <p className="text-navy-600">Versionshistorie laden</p>
              </button>
            )}
          </div>
        )}
      </div>
    </div>
  )
}
