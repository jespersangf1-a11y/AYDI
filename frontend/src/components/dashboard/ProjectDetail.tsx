import { useEffect, useState } from 'react'
import { ArrowLeft, Play, Ship, Zap, Clock } from 'lucide-react'
import { getProject, listLayouts, listAnalyses, runAnalysis, runFullAnalysis, getLayoutVersions } from '../../services/api'
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
  const [showVersions, setShowVersions] = useState(false)

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
      setShowVersions(true)
    } catch (e) {
      setError(e instanceof Error ? e.message : 'Versionsverlauf konnte nicht geladen werden')
    }
  }

  const handleSelectVersion = (_version: LayoutVersion) => {
    // In a real implementation, this would load the layout data from the version
    setShowVersions(false)
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

  return (
    <div>
      {/* Header */}
      <div className="flex items-center gap-4 mb-6">
        <button onClick={onBack} className="text-navy-400 hover:text-white transition-colors">
          <ArrowLeft className="w-5 h-5" />
        </button>
        <div>
          <h2 className="font-heading text-2xl font-bold text-white flex items-center gap-2">
            <Ship className="w-6 h-6 text-ocean-400" />
            {project.name}
          </h2>
          <p className="text-sm text-navy-400">
            {BOAT_CLASS_LABELS[project.boat_class]} · {project.length_m}m × {project.beam_m}m ·{' '}
            {STATUS_LABELS[project.status]}
          </p>
        </div>
      </div>

      {error && (
        <div className="bg-red-900/50 border border-red-700 rounded-lg p-3 text-red-300 text-sm mb-4">
          {error}
        </div>
      )}

      <div className="grid grid-cols-1 lg:grid-cols-3 gap-6">
        {/* Left: Layout + Viewer */}
        <div className="lg:col-span-2 space-y-4">
          {/* Layout Selector */}
          {layouts.length > 0 && (
            <div className="bg-navy-900 border border-navy-700 rounded-xl p-4">
              <h3 className="font-heading font-semibold text-white mb-3">Layouts</h3>
              <div className="flex gap-2 flex-wrap">
                {layouts.map((layout) => (
                  <button
                    key={layout.id}
                    onClick={() => setSelectedLayout(layout)}
                    className={`px-3 py-1.5 rounded-lg text-sm transition-colors ${
                      selectedLayout?.id === layout.id
                        ? 'bg-ocean-600 text-white'
                        : 'bg-navy-800 text-navy-300 hover:bg-navy-700'
                    }`}
                  >
                    {layout.name} ({layout.version})
                  </button>
                ))}
              </div>
            </div>
          )}

          {/* Layout Viewer */}
          {selectedLayout && (
            <LayoutViewer zones={selectedLayout.zones} passages={selectedLayout.passages} />
          )}

          {layouts.length === 0 && (
            <div className="bg-navy-900 border border-navy-700 rounded-xl p-8 text-center text-navy-400">
              Noch kein Layout vorhanden
            </div>
          )}
        </div>

        {/* Right: Analysis */}
        <div className="space-y-4">
          {/* Full Analysis */}
          {selectedLayout && (
            <div className="bg-gradient-to-br from-ocean-900 to-navy-900 border border-ocean-700 rounded-xl p-4">
              <h3 className="font-heading font-semibold text-white mb-3 flex items-center gap-2">
                <Zap className="w-4 h-4 text-ocean-400" />
                Vollanalyse
              </h3>
              <button
                onClick={handleRunFullAnalysis}
                disabled={fullAnalyzing || !selectedLayout}
                className="w-full flex items-center justify-center bg-ocean-600 hover:bg-ocean-500 text-white px-4 py-3 rounded-lg text-sm font-semibold transition-colors disabled:opacity-50 disabled:cursor-not-allowed"
              >
                {fullAnalyzing ? (
                  <>
                    <span className="inline-block animate-spin mr-2">⏳</span>
                    Vollanalyse läuft...
                  </>
                ) : (
                  <>
                    <Zap className="w-4 h-4 mr-2" />
                    Vollanalyse starten
                  </>
                )}
              </button>
            </div>
          )}

          {/* Analysis Trigger */}
          {selectedLayout && (
            <div className="bg-navy-900 border border-navy-700 rounded-xl p-4">
              <h3 className="font-heading font-semibold text-white mb-3">Modulanalyse</h3>
              <div className="space-y-2">
                {['ergonomics', 'volume_storage'].map((module) => (
                  <button
                    key={module}
                    onClick={() => handleRunAnalysis(module)}
                    disabled={analyzing}
                    className="w-full flex items-center justify-between bg-navy-800 hover:bg-navy-700 text-white px-4 py-2 rounded-lg text-sm transition-colors disabled:opacity-50"
                  >
                    <span>{MODULE_LABELS[module]}</span>
                    <Play className="w-4 h-4" />
                  </button>
                ))}
              </div>
            </div>
          )}

          {/* Analysis Results */}
          {selectedAnalysis && (
            <>
              <div className="bg-navy-900 border border-navy-700 rounded-xl p-4 flex flex-col items-center">
                <h3 className="font-heading font-semibold text-white mb-4">
                  {MODULE_LABELS[selectedAnalysis.module] || selectedAnalysis.module}
                </h3>
                <ScoreGauge score={selectedAnalysis.overall_score} label="Gesamtbewertung" />
              </div>

              <div className="bg-navy-900 border border-navy-700 rounded-xl p-4">
                <h3 className="font-heading font-semibold text-white mb-3">Teilbewertungen</h3>
                <SubScoreBars subScores={selectedAnalysis.sub_scores} />
              </div>

              <div className="bg-navy-900 border border-navy-700 rounded-xl p-4">
                <h3 className="font-heading font-semibold text-white mb-3">
                  Warnungen ({selectedAnalysis.warnings.length})
                </h3>
                <WarningList warnings={selectedAnalysis.warnings} />
              </div>
            </>
          )}

          {/* Version History */}
          {selectedLayout && (
            <div className="bg-navy-900 border border-navy-700 rounded-xl p-4">
              <button
                onClick={handleLoadVersions}
                className="w-full flex items-center justify-between px-0 py-0 text-white font-heading font-semibold mb-3 hover:text-ocean-300 transition-colors"
              >
                <span className="flex items-center gap-2">
                  <Clock className="w-4 h-4" />
                  Versionshistorie
                </span>
                <span className="text-xs text-navy-400">{versions.length}</span>
              </button>
              {showVersions && versions.length > 0 ? (
                <div className="space-y-2">
                  {versions.map((version) => (
                    <button
                      key={version.id}
                      onClick={() => handleSelectVersion(version)}
                      className="w-full text-left px-3 py-2 rounded-lg text-sm bg-navy-800 hover:bg-navy-700 transition-colors"
                    >
                      <div className="font-mono text-ocean-300 text-xs font-semibold">v{version.version_number}</div>
                      <div className="text-navy-400 text-xs mt-0.5">
                        Erstellt am: {new Date(version.created_at).toLocaleString('de-DE')}
                      </div>
                      {version.change_summary && (
                        <div className="text-navy-500 text-xs mt-1 truncate">{version.change_summary}</div>
                      )}
                    </button>
                  ))}
                </div>
              ) : (
                showVersions && (
                  <div className="text-center text-navy-500 text-xs py-4">
                    Keine Versionshistorie verfügbar
                  </div>
                )
              )}
            </div>
          )}

          {/* Previous Analyses */}
          {analyses.length > 1 && (
            <div className="bg-navy-900 border border-navy-700 rounded-xl p-4">
              <h3 className="font-heading font-semibold text-white mb-3">Analysehistorie</h3>
              <div className="space-y-1">
                {analyses.map((a) => (
                  <button
                    key={a.id}
                    onClick={() => setSelectedAnalysis(a)}
                    className={`w-full text-left px-3 py-2 rounded-lg text-sm transition-colors ${
                      selectedAnalysis?.id === a.id
                        ? 'bg-ocean-900 text-ocean-300'
                        : 'text-navy-400 hover:bg-navy-800'
                    }`}
                  >
                    <span>{MODULE_LABELS[a.module] || a.module}</span>
                    <span className="float-right font-mono">{Math.round(a.overall_score)}/100</span>
                  </button>
                ))}
              </div>
            </div>
          )}
        </div>
      </div>
    </div>
  )
}
