import { useEffect, useState } from 'react'
import { ArrowLeft, Play, Ship, Zap, Clock, Layers } from 'lucide-react'
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
    return <div className="text-navy-400">Lade...</div>
  }

  if (error && !project) {
    return <div className="text-red-400">Fehler: {error}</div>
  }

  if (!project) {
    return <div className="text-navy-400">Lade...</div>
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

      <div className="px-10 py-8">
        {/* Back Button */}
        <button
          onClick={onBack}
          className="flex items-center gap-2 text-navy-400 hover:text-ocean-300 transition-colors duration-200 mb-8"
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
              <p className="text-white font-serif text-lg">
                {STATUS_LABELS[project.status]}
              </p>
            </div>
          </div>
          {project.description && (
            <p className="text-navy-300 text-sm max-w-md text-right">
              {project.description}
            </p>
          )}
        </div>

        {/* Tab Navigation */}
        <div className="border-b border-navy-700/40 mb-8 flex gap-8">
          {tabs.map((tab) => (
            <button
              key={tab.id}
              onClick={() => setActiveTab(tab.id)}
              className={`flex items-center gap-2 pb-4 font-medium text-sm transition-colors duration-200 ${
                activeTab === tab.id
                  ? 'text-ocean-300 border-b-2 border-ocean-500'
                  : 'text-navy-400 hover:text-navy-300'
              }`}
            >
              {tab.icon}
              {tab.label}
            </button>
          ))}
        </div>

        {/* Tab Content */}
        {activeTab === 'layouts' && (
          <div className="space-y-8">
            {/* Layout Selector */}
            {layouts.length > 0 && (
              <div>
                <p className="label-premium mb-4">Verfügbare Layouts</p>
                <div className="grid gap-4 md:grid-cols-2">
                  {layouts.map((layout) => (
                    <button
                      key={layout.id}
                      onClick={() => setSelectedLayout(layout)}
                      className={`card-premium px-6 py-5 text-left transition-all duration-200 ${
                        selectedLayout?.id === layout.id
                          ? 'bg-ocean-900/40 border-ocean-600/60'
                          : 'hover:bg-navy-900/60 hover:border-navy-600/40'
                      }`}
                    >
                      <div className="font-serif text-lg font-medium text-white mb-1">
                        {layout.name}
                      </div>
                      <div className="text-xs text-navy-400">
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
                <p className="text-navy-400">Noch kein Layout vorhanden</p>
              </div>
            )}
          </div>
        )}

        {activeTab === 'analysis' && (
          <div className="space-y-8">
            {/* Full Analysis */}
            {selectedLayout && (
              <div className="card-premium px-8 py-6 bg-gradient-to-br from-ocean-900/40 to-navy-900/40 border-ocean-600/40">
                <div className="flex items-center justify-between">
                  <div>
                    <p className="label-premium mb-2">Umfassende Analyse</p>
                    <p className="text-white font-serif text-lg">
                      Alle Module analysieren
                    </p>
                  </div>
                  <button
                    onClick={handleRunFullAnalysis}
                    disabled={fullAnalyzing || !selectedLayout}
                    className="flex items-center gap-2 bg-ocean-700 hover:bg-ocean-600 disabled:opacity-50 disabled:cursor-not-allowed text-white px-6 py-3 rounded-lg font-medium transition-colors duration-200"
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
                  {['ergonomics', 'volume_storage'].map((module) => (
                    <button
                      key={module}
                      onClick={() => handleRunAnalysis(module)}
                      disabled={analyzing}
                      className="card-premium px-6 py-4 flex items-center justify-between hover:bg-navy-900/60 hover:border-navy-600/40 disabled:opacity-50 transition-all duration-200"
                    >
                      <span className="text-white font-medium">
                        {MODULE_LABELS[module]}
                      </span>
                      <Play className="w-4 h-4 text-ocean-500" />
                    </button>
                  ))}
                </div>
              </div>
            )}

            {/* Analysis Results */}
            {selectedAnalysis && (
              <div className="space-y-8">
                <div>
                  <p className="label-premium mb-4">Analyseergebnisse</p>
                  <p className="text-white font-serif text-lg mb-6">
                    {MODULE_LABELS[selectedAnalysis.module] || selectedAnalysis.module}
                  </p>
                  <div className="card-premium px-8 py-8 flex items-center justify-center">
                    <ScoreGauge
                      score={selectedAnalysis.overall_score}
                      label="Gesamtbewertung"
                    />
                  </div>
                </div>

                <div className="card-premium px-8 py-6">
                  <p className="label-premium mb-4">Teilbewertungen</p>
                  <SubScoreBars subScores={selectedAnalysis.sub_scores} />
                </div>

                {selectedAnalysis.warnings.length > 0 && (
                  <div className="card-premium px-8 py-6">
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
              <div>
                <p className="label-premium mb-4">Analysehistorie</p>
                <div className="space-y-2">
                  {analyses.map((a) => (
                    <button
                      key={a.id}
                      onClick={() => setSelectedAnalysis(a)}
                      className={`card-premium px-6 py-4 text-left flex items-center justify-between transition-all duration-200 ${
                        selectedAnalysis?.id === a.id
                          ? 'bg-ocean-900/40 border-ocean-600/60'
                          : 'hover:bg-navy-900/60 hover:border-navy-600/40'
                      }`}
                    >
                      <span className="text-white font-medium">
                        {MODULE_LABELS[a.module] || a.module}
                      </span>
                      <span className="text-ocean-300 font-mono text-sm font-semibold">
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
          <div>
            <p className="label-premium mb-4">Versionshistorie</p>
            {versions.length > 0 ? (
              <div className="space-y-3">
                {versions.map((version) => (
                  <button
                    key={version.id}
                    onClick={() => handleSelectVersion(version)}
                    className="card-premium px-6 py-5 text-left hover:bg-navy-900/60 hover:border-navy-600/40 transition-all duration-200 group"
                  >
                    <div className="flex items-start justify-between">
                      <div>
                        <div className="font-mono text-ocean-300 font-semibold mb-1">
                          Version {version.version_number}
                        </div>
                        <div className="text-sm text-navy-400">
                          {new Date(version.created_at).toLocaleString('de-DE')}
                        </div>
                        {version.change_summary && (
                          <div className="text-sm text-navy-300 mt-2">
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
                className="card-premium px-8 py-6 text-center hover:bg-navy-900/60 hover:border-navy-600/40 transition-all duration-200 w-full"
              >
                <p className="text-navy-400">Versionshistorie laden</p>
              </button>
            )}
          </div>
        )}
      </div>
    </div>
  )
}
