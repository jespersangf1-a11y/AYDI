import { useEffect, useState, useMemo, lazy, Suspense } from 'react'
import {
  ArrowLeft,
  Ship,
  Zap,
  Clock,
  Layers,
  Calendar,
  Euro,
  GitCompare,
  BarChart3,
  ChevronRight,
  Loader2,
  Box,
  Map,
  RotateCcw,
} from 'lucide-react'
import {
  getProject,
  listLayouts,
  listAnalyses,
  runAnalysis,
  runFullAnalysis,
  getLayoutVersions,
  getLayoutDiff,
  getProjectImages,
} from '../../services/api'
import HeroSection from '../layout/HeroSection'
import { MEDIA } from '../../config/media'
import type {
  Project,
  Layout,
  AnalysisResult,
  LayoutVersion,
  LayoutDiff,
  FullAnalysisResult,
  AnalysisModule,
  ImageUploadData,
  WarningData,
} from '../../types'
import {
  BOAT_CLASS_LABELS,
  STATUS_LABELS,
  ANALYSIS_MODULE_LABELS,
} from '../../types'
import ScoreGauge from '../analysis/ScoreGauge'
import SubScoreBars from '../analysis/SubScoreBars'
import WarningList from '../analysis/WarningList'
import LayoutViewer from '../analysis/LayoutViewer'
import FullAnalysisView from '../analysis/FullAnalysisView'
import ModuleSelector from '../analysis/ModuleSelector'
import CostOverview from '../costs/CostOverview'
import DiffViewer from '../compare/DiffViewer'
// ConfidenceBadge is used by FullAnalysisView internally

// Lazy-load 3D viewer to avoid large bundle on initial load
const DeckViewer3D = lazy(() => import('../viewer3d/DeckViewer3D'))

interface ProjectDetailProps {
  projectId: string
  onBack: () => void
}

type TabType = 'overview' | 'layouts' | 'analysis' | 'costs' | 'history'
type ViewerMode = '2d' | '3d'

// ─── Helper: collect all warnings from all analyses ───
function collectWarnings(analyses: AnalysisResult[]): WarningData[] {
  return analyses.flatMap((a) => a.warnings ?? [])
}

// ─── Helper: group analyses by module (latest first) ───
function latestByModule(analyses: AnalysisResult[]): Record<string, AnalysisResult> {
  const map: Record<string, AnalysisResult> = {}
  for (const a of analyses) {
    if (!map[a.module] || new Date(a.created_at) > new Date(map[a.module].created_at)) {
      map[a.module] = a
    }
  }
  return map
}

// ─── Module icon colors by score ───
function moduleScoreClass(score: number): string {
  if (score >= 80) return 'text-emerald-600'
  if (score >= 60) return 'text-amber-600'
  if (score >= 40) return 'text-orange-600'
  return 'text-red-600'
}

function moduleBorderClass(score: number): string {
  if (score >= 80) return 'border-emerald-500/30'
  if (score >= 60) return 'border-amber-500/30'
  if (score >= 40) return 'border-orange-500/30'
  return 'border-red-500/30'
}

function moduleBgClass(score: number): string {
  if (score >= 80) return 'bg-emerald-500/5'
  if (score >= 60) return 'bg-amber-500/5'
  if (score >= 40) return 'bg-orange-500/5'
  return 'bg-red-500/5'
}

export default function ProjectDetail({ projectId, onBack }: ProjectDetailProps) {
  // ─── Core state ───
  const [project, setProject] = useState<Project | null>(null)
  const [layouts, setLayouts] = useState<Layout[]>([])
  const [analyses, setAnalyses] = useState<AnalysisResult[]>([])
  const [selectedLayout, setSelectedLayout] = useState<Layout | null>(null)
  const [selectedAnalysis, setSelectedAnalysis] = useState<AnalysisResult | null>(null)
  const [loading, setLoading] = useState(true)
  const [error, setError] = useState<string | null>(null)

  // ─── Analysis state ───
  const [analyzing, setAnalyzing] = useState(false)
  const [analyzingModule, setAnalyzingModule] = useState<string | null>(null)
  const [fullAnalyzing, setFullAnalyzing] = useState(false)
  const [fullAnalysisResult, setFullAnalysisResult] = useState<FullAnalysisResult | null>(null)
  const [, setSelectedModuleForDetail] = useState<string | null>(null)

  // ─── Version state ───
  const [versions, setVersions] = useState<LayoutVersion[]>([])
  const [versionsLoaded, setVersionsLoaded] = useState(false)
  const [versionsLoading, setVersionsLoading] = useState(false)
  const [selectedVersionA, setSelectedVersionA] = useState<string | null>(null)
  const [selectedVersionB, setSelectedVersionB] = useState<string | null>(null)
  const [diff, setDiff] = useState<LayoutDiff | null>(null)
  const [diffLoading, setDiffLoading] = useState(false)

  // ─── Images state ───
  const [images, setImages] = useState<ImageUploadData[]>([])

  // ─── Snapshot indicator ───
  const [snapshotLabel, setSnapshotLabel] = useState<string | null>(null)

  // ─── UI state ───
  const [activeTab, setActiveTab] = useState<TabType>('overview')
  const [viewerMode, setViewerMode] = useState<ViewerMode>('2d')

  // ─── Reset dependent state when selectedLayout changes ───
  useEffect(() => {
    // Clear analysis/version/diff state that belongs to the previous layout
    setFullAnalysisResult(null)
    setVersions([])
    setVersionsLoaded(false)
    setSelectedVersionA(null)
    setSelectedVersionB(null)
    setDiff(null)
    setSnapshotLabel(null)
  }, [selectedLayout?.id])

  // ─── Derived data ───
  const latestModuleResults = useMemo(() => latestByModule(analyses), [analyses])
  const allWarnings = useMemo(() => collectWarnings(analyses), [analyses])
  const analyzedModules = useMemo(
    () => Object.keys(latestModuleResults) as AnalysisModule[],
    [latestModuleResults]
  )

  // ─── Overall score from latest analyses ───
  const overallScore = useMemo(() => {
    const scores = Object.values(latestModuleResults).map((a) => a.overall_score)
    if (scores.length === 0) return null
    return scores.reduce((sum, s) => sum + s, 0) / scores.length
  }, [latestModuleResults])

  // ─── Initial data load ───
  useEffect(() => {
    setLoading(true)
    Promise.allSettled([
      getProject(projectId),
      listLayouts(projectId),
      listAnalyses(projectId),
      getProjectImages(projectId),
    ])
      .then((results) => {
        const proj = results[0].status === 'fulfilled' ? results[0].value : null
        const lays = results[1].status === 'fulfilled' ? results[1].value : []
        const anals = results[2].status === 'fulfilled' ? results[2].value : []
        const imgs = results[3].status === 'fulfilled' ? results[3].value : []

        if (proj) setProject(proj)
        else setError('Projekt konnte nicht geladen werden')

        setLayouts(lays)
        setAnalyses(anals)
        setImages(imgs)
        if (lays.length > 0) setSelectedLayout(lays[0])
        if (anals.length > 0) setSelectedAnalysis(anals[0])
      })
      .catch((e) => setError(e.message))
      .finally(() => setLoading(false))
  }, [projectId])

  // ─── Run single module analysis ───
  const handleRunAnalysis = async (module: string) => {
    if (!selectedLayout) return
    setAnalyzing(true)
    setAnalyzingModule(module)
    setError(null)
    try {
      const result = await runAnalysis(projectId, selectedLayout.id, module)
      setAnalyses((prev) => [result, ...prev])
      setSelectedAnalysis(result)
      setSelectedModuleForDetail(module)
    } catch (e) {
      setError(e instanceof Error ? e.message : 'Analysefehler')
    } finally {
      setAnalyzing(false)
      setAnalyzingModule(null)
    }
  }

  // ─── Run full orchestrated analysis ───
  const handleRunFullAnalysis = async () => {
    if (!selectedLayout) return
    setFullAnalyzing(true)
    setError(null)
    try {
      const result = await runFullAnalysis(projectId, selectedLayout.id)
      setFullAnalysisResult(result)
      // Refresh analyses list
      const refreshed = await listAnalyses(projectId)
      setAnalyses(refreshed)
      if (refreshed.length > 0) setSelectedAnalysis(refreshed[0])
    } catch (e) {
      setError(e instanceof Error ? e.message : 'Vollanalyse fehlgeschlagen')
    } finally {
      setFullAnalyzing(false)
    }
  }

  // ─── Load version history ───
  const handleLoadVersions = async () => {
    if (!selectedLayout) return
    setVersionsLoading(true)
    try {
      const v = await getLayoutVersions(projectId, selectedLayout.id)
      setVersions(v)
      setVersionsLoaded(true)
    } catch (e) {
      setError(e instanceof Error ? e.message : 'Versionsverlauf konnte nicht geladen werden')
    } finally {
      setVersionsLoading(false)
    }
  }

  // ─── Load diff between two versions ───
  const handleLoadDiff = async () => {
    if (!selectedLayout || !selectedVersionA || !selectedVersionB) return
    setDiffLoading(true)
    try {
      const d = await getLayoutDiff(projectId, selectedLayout.id, selectedVersionA, selectedVersionB)
      setDiff(d)
    } catch (e) {
      setError(e instanceof Error ? e.message : 'Diff konnte nicht geladen werden')
    } finally {
      setDiffLoading(false)
    }
  }

  // ─── Restore version ───
  const handleSelectVersion = (version: LayoutVersion) => {
    if (!selectedLayout) return
    // Apply version snapshot to current viewer
    if (version.zones_snapshot && version.passages_snapshot) {
      setSelectedLayout({
        ...selectedLayout,
        zones: version.zones_snapshot,
        passages: version.passages_snapshot,
      })
      setSnapshotLabel(`Snapshot v${version.version_number}`)
    }
  }

  // ─── Loading / Error states ───
  if (loading) {
    return (
      <div className="flex items-center justify-center min-h-[400px]">
        <div className="flex items-center gap-3 text-navy-600">
          <Loader2 className="w-5 h-5 animate-spin" />
          <span className="text-sm font-medium">Lade Projektdaten...</span>
        </div>
      </div>
    )
  }

  if (error && !project) {
    return (
      <div className="flex items-center justify-center min-h-[400px]">
        <div className="card-premium bg-red-900/20 border-red-700/40 p-6 text-red-300 text-sm max-w-md text-center">
          <p className="font-medium mb-2">Fehler beim Laden</p>
          <p>{error}</p>
        </div>
      </div>
    )
  }

  if (!project) return null

  // ─── Tab definitions ───
  const tabs: { id: TabType; label: string; icon: React.ReactNode; badge?: number }[] = [
    { id: 'overview', label: 'Übersicht', icon: <BarChart3 className="w-4 h-4" /> },
    { id: 'layouts', label: 'Layouts', icon: <Layers className="w-4 h-4" /> },
    {
      id: 'analysis',
      label: 'Analyse',
      icon: <Zap className="w-4 h-4" />,
      badge: Object.keys(latestModuleResults).length,
    },
    { id: 'costs', label: 'Kosten', icon: <Euro className="w-4 h-4" /> },
    {
      id: 'history',
      label: 'Versionen',
      icon: <Clock className="w-4 h-4" />,
      badge: versions.length > 0 ? versions.length : undefined,
    },
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
          <div className="card-premium bg-red-900/20 border-red-700/40 p-4 text-red-300 text-sm mb-8 flex items-center justify-between">
            <span>{error}</span>
            <button
              onClick={() => setError(null)}
              className="text-red-400 hover:text-red-300 text-xs font-medium"
            >
              Schließen
            </button>
          </div>
        )}

        {/* Project Meta Card */}
        <div className="card-premium px-8 py-6 mb-10 flex flex-col sm:flex-row items-start sm:items-center justify-between gap-4">
          <div className="flex items-center gap-4">
            <Ship className="w-8 h-8 text-ocean-500" />
            <div>
              <p className="label-premium mb-1">Projektstatus</p>
              <p className="text-navy-900 font-serif text-lg">
                {STATUS_LABELS[project.status]}
              </p>
            </div>
          </div>
          <div className="flex items-center gap-6">
            {overallScore !== null && (
              <div className="text-center">
                <p className="label-premium mb-1">Gesamtscore</p>
                <p className={`font-mono text-2xl font-bold ${moduleScoreClass(overallScore)}`}>
                  {Math.round(overallScore)}
                </p>
              </div>
            )}
            <div className="text-center">
              <p className="label-premium mb-1">Module</p>
              <p className="font-mono text-lg font-semibold text-navy-900">
                {analyzedModules.length}/{Object.keys(ANALYSIS_MODULE_LABELS).length}
              </p>
            </div>
            <div className="text-center">
              <p className="label-premium mb-1">Bilder</p>
              <p className="font-mono text-lg font-semibold text-navy-900">
                {images.length}
              </p>
            </div>
          </div>
          {project.description && (
            <p className="text-navy-700 text-sm max-w-md sm:text-right">
              {project.description}
            </p>
          )}
        </div>

        {/* ─── Tab Navigation ─── */}
        <div className="border-b border-sand-200 mb-8 flex gap-2 sm:gap-6 overflow-x-auto scrollbar-hide">
          {tabs.map((tab) => (
            <button
              key={tab.id}
              onClick={() => {
                setActiveTab(tab.id)
                if (tab.id === 'history' && !versionsLoaded && selectedLayout) {
                  handleLoadVersions()
                }
              }}
              className={`flex items-center gap-2 pb-4 font-medium text-sm transition-colors duration-200 relative whitespace-nowrap ${
                activeTab === tab.id
                  ? 'text-ocean-600'
                  : 'text-navy-600 hover:text-navy-700'
              }`}
              aria-selected={activeTab === tab.id}
            >
              {tab.icon}
              {tab.label}
              {tab.badge !== undefined && tab.badge > 0 && (
                <span className="inline-flex items-center justify-center w-5 h-5 rounded-full bg-ocean-700/60 text-ocean-200 text-[10px] font-bold">
                  {tab.badge}
                </span>
              )}
              {activeTab === tab.id && (
                <div className="absolute bottom-0 left-0 right-0 h-0.5 bg-gradient-to-r from-ocean-500 to-ocean-400" />
              )}
            </button>
          ))}
        </div>

        {/* ═══════════════════════════════════════════════════════════════
            TAB: OVERVIEW — Projektübersicht mit allen Modul-Scores
        ═══════════════════════════════════════════════════════════════ */}
        {activeTab === 'overview' && (
          <div className="space-y-8 animate-fade-in-up">
            {/* Overall Score + Full Analysis Button */}
            {selectedLayout && (
              <div className="card-premium px-8 py-8 bg-gradient-to-br from-ocean-900/30 to-navy-900/30 border-ocean-600/30">
                <div className="flex flex-col lg:flex-row items-center gap-8">
                  {overallScore !== null ? (
                    <ScoreGauge score={overallScore} label="Gesamtbewertung" size="lg" />
                  ) : (
                    <div className="flex flex-col items-center">
                      <div className="flex items-center justify-center w-[160px] h-[160px] rounded-full border-2 border-dashed border-navy-700/40">
                        <span className="text-navy-600 text-sm text-center px-4">
                          Noch keine Analyse
                        </span>
                      </div>
                    </div>
                  )}
                  <div className="flex-1 text-center lg:text-left">
                    <h2 className="font-serif text-2xl text-navy-900 mb-3">
                      {analyzedModules.length > 0
                        ? `${analyzedModules.length} von ${Object.keys(ANALYSIS_MODULE_LABELS).length} Modulen analysiert`
                        : 'Bereit für die Analyse'}
                    </h2>
                    <p className="text-navy-700 text-sm mb-6 max-w-lg">
                      {analyzedModules.length > 0
                        ? 'Starten Sie eine Vollanalyse, um alle Module gleichzeitig zu bewerten und ein umfassendes Ergebnis zu erhalten.'
                        : 'Wählen Sie ein Layout und starten Sie die Vollanalyse, um Ihr Yachtdesign umfassend bewerten zu lassen.'}
                    </p>
                    <button
                      onClick={handleRunFullAnalysis}
                      disabled={fullAnalyzing || !selectedLayout}
                      className="inline-flex items-center gap-2 bg-ocean-700 hover:bg-ocean-600 disabled:opacity-50 disabled:cursor-not-allowed text-navy-900 px-8 py-3.5 rounded-lg font-medium transition-all duration-200 hover:shadow-lg hover:shadow-ocean-700/30"
                    >
                      {fullAnalyzing ? (
                        <>
                          <Loader2 className="w-4 h-4 animate-spin" />
                          Vollanalyse läuft...
                        </>
                      ) : (
                        <>
                          <Zap className="w-4 h-4" />
                          Vollanalyse starten
                        </>
                      )}
                    </button>
                  </div>
                </div>
              </div>
            )}

            {/* Full Analysis Results (if available) */}
            {fullAnalysisResult && (
              <FullAnalysisView
                result={fullAnalysisResult}
                onModuleClick={(mod) => {
                  setSelectedModuleForDetail(mod)
                  setSelectedAnalysis(latestModuleResults[mod] ?? null)
                  setActiveTab('analysis')
                }}
              />
            )}

            {/* Module Score Grid (from individual analyses, shown when no full analysis) */}
            {!fullAnalysisResult && analyzedModules.length > 0 && (
              <div className="space-y-4">
                <h3 className="label-premium">Analyseergebnisse nach Modul</h3>
                <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-4">
                  {Object.entries(latestModuleResults).map(([mod, result], idx) => (
                    <button
                      key={mod}
                      onClick={() => {
                        setSelectedModuleForDetail(mod)
                        setSelectedAnalysis(result)
                        setActiveTab('analysis')
                      }}
                      style={{ animationDelay: `${idx * 80}ms` }}
                      className={`animate-fade-in-up card-premium p-5 text-left group transition-all duration-300 hover:shadow-lg hover:-translate-y-0.5 ${moduleBorderClass(result.overall_score)} ${moduleBgClass(result.overall_score)}`}
                    >
                      <div className="flex items-start justify-between mb-2">
                        <span className="text-sm font-sans font-semibold text-navy-900 group-hover:text-ocean-700 transition-colors">
                          {ANALYSIS_MODULE_LABELS[mod as AnalysisModule] ?? mod}
                        </span>
                        <span className={`font-mono text-2xl font-bold ${moduleScoreClass(result.overall_score)}`}>
                          {Math.round(result.overall_score)}
                        </span>
                      </div>
                      {result.warnings.length > 0 && (
                        <p className="text-xs text-navy-600">
                          {result.warnings.length} Hinweis{result.warnings.length !== 1 ? 'e' : ''}
                          {result.warnings.filter((w) => w.severity === 'critical').length > 0 && (
                            <span className="text-red-400 ml-1">
                              ({result.warnings.filter((w) => w.severity === 'critical').length} kritisch)
                            </span>
                          )}
                        </p>
                      )}
                      <div className="mt-3 flex items-center gap-2 text-xs text-ocean-600 opacity-0 group-hover:opacity-100 transition-opacity">
                        <ChevronRight className="w-3 h-3" />
                        Details anzeigen
                      </div>
                    </button>
                  ))}
                </div>
              </div>
            )}

            {/* Warning Summary */}
            {allWarnings.length > 0 && (
              <div className="card-premium px-8 py-6">
                <p className="label-premium mb-4">
                  Alle Warnungen ({allWarnings.length})
                </p>
                <WarningList warnings={allWarnings.slice(0, 10)} />
                {allWarnings.length > 10 && (
                  <p className="text-xs text-navy-500 mt-4 text-center">
                    +{allWarnings.length - 10} weitere Warnungen im Analyse-Tab
                  </p>
                )}
              </div>
            )}
          </div>
        )}

        {/* ═══════════════════════════════════════════════════════════════
            TAB: LAYOUTS — Layout-Auswahl + 2D/3D-Viewer
        ═══════════════════════════════════════════════════════════════ */}
        {activeTab === 'layouts' && (
          <div className="space-y-8 animate-fade-in-up">
            {/* Layout Selector */}
            {layouts.length > 0 && (
              <div>
                <p className="label-premium mb-4">Verfügbare Layouts</p>
                <div className="grid gap-4 md:grid-cols-2 lg:grid-cols-3">
                  {layouts.map((layout, idx) => (
                    <button
                      key={layout.id}
                      onClick={() => {
                        setSelectedLayout(layout)
                        setVersionsLoaded(false)
                        setVersions([])
                      }}
                      style={{ animationDelay: `${idx * 100}ms` }}
                      className={`animate-fade-in-up card-premium px-6 py-5 text-left transition-all duration-300 hover:shadow-lg hover:shadow-ocean-500/10 group ${
                        selectedLayout?.id === layout.id
                          ? 'bg-ocean-900/40 border-ocean-600/60'
                          : 'hover:bg-navy-900/60 hover:border-sand-200'
                      }`}
                    >
                      <div className="font-serif text-lg font-medium text-navy-900 mb-1 group-hover:text-ocean-700 transition-colors">
                        {layout.name}
                      </div>
                      <div className="text-xs text-navy-600 flex items-center gap-3">
                        <span>Version {layout.version}</span>
                        <span>{layout.zones.length} Zonen</span>
                        <span>{layout.passages.length} Durchgänge</span>
                      </div>
                    </button>
                  ))}
                </div>
              </div>
            )}

            {/* Viewer Mode Toggle */}
            {selectedLayout && (
              <div className="flex items-center gap-2">
                {snapshotLabel && (
                  <span className="flex items-center gap-1.5 text-xs bg-amber-900/20 border border-amber-600/30 text-amber-300 px-3 py-1.5 rounded-full font-medium mr-2">
                    <RotateCcw className="w-3 h-3" />
                    {snapshotLabel}
                  </span>
                )}
                <span className="label-premium mr-2">Ansicht</span>
                <button
                  onClick={() => setViewerMode('2d')}
                  className={`flex items-center gap-1.5 px-3 py-1.5 rounded-lg text-xs font-medium transition-all ${
                    viewerMode === '2d'
                      ? 'bg-ocean-700 text-navy-900'
                      : 'text-navy-600 hover:text-navy-700 border border-sand-200'
                  }`}
                >
                  <Map className="w-3.5 h-3.5" />
                  2D
                </button>
                <button
                  onClick={() => setViewerMode('3d')}
                  className={`flex items-center gap-1.5 px-3 py-1.5 rounded-lg text-xs font-medium transition-all ${
                    viewerMode === '3d'
                      ? 'bg-ocean-700 text-navy-900'
                      : 'text-navy-600 hover:text-navy-700 border border-sand-200'
                  }`}
                >
                  <Box className="w-3.5 h-3.5" />
                  3D
                </button>
              </div>
            )}

            {/* Layout Viewer */}
            {selectedLayout && viewerMode === '2d' && (
              <div className="card-premium p-0 overflow-hidden">
                <LayoutViewer zones={selectedLayout.zones} passages={selectedLayout.passages} />
              </div>
            )}

            {selectedLayout && viewerMode === '3d' && (
              <div className="card-premium p-0 overflow-hidden" style={{ height: '600px' }}>
                <Suspense
                  fallback={
                    <div className="flex items-center justify-center h-full text-navy-600">
                      <Loader2 className="w-5 h-5 animate-spin mr-2" />
                      3D-Viewer wird geladen...
                    </div>
                  }
                >
                  <DeckViewer3D
                    zones={selectedLayout.zones}
                    passages={selectedLayout.passages}
                    warnings={allWarnings}
                  />
                </Suspense>
              </div>
            )}

            {layouts.length === 0 && (
              <div className="card-premium px-8 py-12 text-center">
                <Layers className="w-12 h-12 mx-auto mb-4 text-navy-600" />
                <p className="text-navy-600">Noch kein Layout vorhanden</p>
                <p className="text-navy-500 text-xs mt-2">
                  Importieren Sie eine DXF-Datei oder erstellen Sie ein Layout manuell.
                </p>
              </div>
            )}
          </div>
        )}

        {/* ═══════════════════════════════════════════════════════════════
            TAB: ANALYSIS — Einzelmodul-Analyse + Detailansicht
        ═══════════════════════════════════════════════════════════════ */}
        {activeTab === 'analysis' && (
          <div className="space-y-8 animate-fade-in-up">
            {/* Full Analysis Banner */}
            {selectedLayout && (
              <div className="card-premium px-8 py-6 bg-gradient-to-br from-ocean-900/40 to-navy-900/40 border-ocean-600/40">
                <div className="flex flex-col sm:flex-row items-start sm:items-center justify-between gap-4">
                  <div>
                    <p className="label-premium mb-2">Umfassende Analyse</p>
                    <p className="text-navy-900 font-serif text-lg">
                      Alle Module gleichzeitig analysieren
                    </p>
                  </div>
                  <button
                    onClick={handleRunFullAnalysis}
                    disabled={fullAnalyzing || !selectedLayout}
                    className="flex items-center gap-2 bg-ocean-700 hover:bg-ocean-600 disabled:opacity-50 disabled:cursor-not-allowed text-navy-900 px-6 py-3 rounded-lg font-medium transition-all duration-200 hover:shadow-lg hover:shadow-ocean-700/30"
                  >
                    {fullAnalyzing ? (
                      <>
                        <Loader2 className="w-4 h-4 animate-spin" />
                        Läuft...
                      </>
                    ) : (
                      <>
                        <Zap className="w-4 h-4" />
                        Vollanalyse starten
                      </>
                    )}
                  </button>
                </div>
              </div>
            )}

            {/* Full Analysis Results */}
            {fullAnalysisResult && (
              <FullAnalysisView
                result={fullAnalysisResult}
                onModuleClick={(mod) => {
                  setSelectedModuleForDetail(mod)
                  setSelectedAnalysis(latestModuleResults[mod] ?? null)
                }}
              />
            )}

            {/* Module Selector — all 11 modules */}
            {selectedLayout && (
              <ModuleSelector
                onSelect={(mod) => handleRunAnalysis(mod)}
                selectedModule={(analyzingModule as AnalysisModule) ?? undefined}
                availableModules={undefined}
              />
            )}

            {/* Running indicator */}
            {analyzing && analyzingModule && (
              <div className="card-premium px-6 py-4 flex items-center gap-3 border-ocean-600/40 bg-ocean-900/20">
                <Loader2 className="w-4 h-4 animate-spin text-ocean-500" />
                <span className="text-sm text-navy-900">
                  {ANALYSIS_MODULE_LABELS[analyzingModule as AnalysisModule] ?? analyzingModule} wird analysiert...
                </span>
              </div>
            )}

            {/* Selected Module Detail */}
            {selectedAnalysis && (
              <div className="space-y-6">
                <div className="flex items-center justify-between">
                  <h3 className="font-serif text-xl text-navy-900">
                    {ANALYSIS_MODULE_LABELS[selectedAnalysis.module as AnalysisModule] ?? selectedAnalysis.module}
                  </h3>
                  <span className="text-xs text-navy-500">
                    {new Date(selectedAnalysis.created_at).toLocaleString('de-DE')}
                  </span>
                </div>

                <div className="grid grid-cols-1 lg:grid-cols-3 gap-6">
                  {/* Score Gauge */}
                  <div className="card-premium px-8 py-8 flex items-center justify-center">
                    <ScoreGauge
                      score={selectedAnalysis.overall_score}
                      label="Modulbewertung"
                    />
                  </div>

                  {/* Sub-Scores */}
                  <div className="lg:col-span-2 card-premium px-8 py-6">
                    <p className="label-premium mb-4">Teilbewertungen</p>
                    <SubScoreBars subScores={selectedAnalysis.sub_scores} />
                  </div>
                </div>

                {/* Warnings */}
                {selectedAnalysis.warnings.length > 0 && (
                  <div className="card-premium px-8 py-6">
                    <p className="label-premium mb-4">
                      Warnungen ({selectedAnalysis.warnings.length})
                    </p>
                    <WarningList warnings={selectedAnalysis.warnings} />
                  </div>
                )}

                {/* Suggestions */}
                {selectedAnalysis.suggestions.length > 0 && (
                  <div className="card-premium px-8 py-6">
                    <p className="label-premium mb-4">Verbesserungsvorschläge</p>
                    <div className="space-y-2">
                      {selectedAnalysis.suggestions.map((s, i) => (
                        <div key={i} className="flex items-start gap-3 text-sm text-navy-700">
                          <ChevronRight className="w-4 h-4 text-ocean-500 flex-shrink-0 mt-0.5" />
                          <span>{s}</span>
                        </div>
                      ))}
                    </div>
                  </div>
                )}
              </div>
            )}

            {/* Analysis History */}
            {analyses.length > 0 && (
              <div>
                <p className="label-premium mb-4">Analysehistorie</p>
                <div className="space-y-2 max-h-96 overflow-y-auto scrollbar-hide">
                  {analyses.map((a) => (
                    <button
                      key={a.id}
                      onClick={() => {
                        setSelectedAnalysis(a)
                        setSelectedModuleForDetail(a.module)
                      }}
                      className={`w-full card-premium px-6 py-4 text-left flex items-center justify-between transition-all duration-200 hover:shadow-lg hover:shadow-ocean-500/10 group ${
                        selectedAnalysis?.id === a.id
                          ? 'bg-ocean-900/40 border-ocean-600/60'
                          : 'hover:bg-navy-900/60 hover:border-sand-200'
                      }`}
                    >
                      <div className="flex items-center gap-3">
                        <span className="text-navy-900 font-medium group-hover:text-ocean-700 transition-colors text-sm">
                          {ANALYSIS_MODULE_LABELS[a.module as AnalysisModule] ?? a.module}
                        </span>
                        <span className="text-xs text-navy-500">
                          {new Date(a.created_at).toLocaleString('de-DE', {
                            day: '2-digit',
                            month: '2-digit',
                            hour: '2-digit',
                            minute: '2-digit',
                          })}
                        </span>
                      </div>
                      <span className={`font-mono text-sm font-semibold ${moduleScoreClass(a.overall_score)}`}>
                        {Math.round(a.overall_score)}/100
                      </span>
                    </button>
                  ))}
                </div>
              </div>
            )}
          </div>
        )}

        {/* ═══════════════════════════════════════════════════════════════
            TAB: COSTS — Kostenübersicht
        ═══════════════════════════════════════════════════════════════ */}
        {activeTab === 'costs' && (
          <div className="space-y-8 animate-fade-in-up">
            {selectedLayout ? (
              <CostOverview projectId={projectId} layoutId={selectedLayout.id} />
            ) : (
              <div className="card-premium px-8 py-12 text-center">
                <Euro className="w-12 h-12 mx-auto mb-4 text-navy-600" />
                <p className="text-navy-600">Kein Layout ausgewählt</p>
                <p className="text-navy-500 text-xs mt-2">
                  Wählen Sie ein Layout im Layout-Tab, um die Kostenanalyse zu sehen.
                </p>
              </div>
            )}
          </div>
        )}

        {/* ═══════════════════════════════════════════════════════════════
            TAB: HISTORY — Versionshistorie + Diff-Viewer
        ═══════════════════════════════════════════════════════════════ */}
        {activeTab === 'history' && (
          <div className="space-y-8 animate-fade-in-up">
            {!selectedLayout && (
              <div className="card-premium px-8 py-12 text-center">
                <Clock className="w-12 h-12 mx-auto mb-4 text-navy-600" />
                <p className="text-navy-600">Kein Layout ausgewählt</p>
              </div>
            )}

            {selectedLayout && versionsLoading && (
              <div className="flex items-center gap-2 text-navy-600 text-sm">
                <Loader2 className="w-4 h-4 animate-spin" />
                Lade Versionshistorie...
              </div>
            )}

            {selectedLayout && versionsLoaded && versions.length === 0 && (
              <div className="card-premium px-8 py-12 text-center">
                <Clock className="w-12 h-12 mx-auto mb-4 text-navy-600" />
                <p className="text-navy-600">Noch keine Versionen vorhanden</p>
              </div>
            )}

            {selectedLayout && versionsLoaded && versions.length > 0 && (
              <>
                {/* Version comparison selector */}
                <div className="card-premium px-6 py-5">
                  <h3 className="font-sans font-semibold text-navy-900 mb-4 flex items-center gap-2">
                    <GitCompare className="w-4 h-4 text-ocean-500" />
                    Versionen vergleichen
                  </h3>
                  <div className="grid grid-cols-1 sm:grid-cols-2 gap-4 mb-4">
                    <div>
                      <label className="label-premium mb-2 block">Version A</label>
                      <select
                        value={selectedVersionA ?? ''}
                        onChange={(e) => setSelectedVersionA(e.target.value || null)}
                        className="w-full rounded-lg border border-sand-200 bg-white px-3 py-2 text-sm text-navy-900 focus:border-ocean-500 focus:outline-none"
                      >
                        <option value="">Wählen...</option>
                        {versions.map((v) => (
                          <option key={v.id} value={v.id}>
                            Version {v.version_number} — {new Date(v.created_at).toLocaleDateString('de-DE')}
                          </option>
                        ))}
                      </select>
                    </div>
                    <div>
                      <label className="label-premium mb-2 block">Version B</label>
                      <select
                        value={selectedVersionB ?? ''}
                        onChange={(e) => setSelectedVersionB(e.target.value || null)}
                        className="w-full rounded-lg border border-sand-200 bg-white px-3 py-2 text-sm text-navy-900 focus:border-ocean-500 focus:outline-none"
                      >
                        <option value="">Wählen...</option>
                        {versions.map((v) => (
                          <option key={v.id} value={v.id}>
                            Version {v.version_number} — {new Date(v.created_at).toLocaleDateString('de-DE')}
                          </option>
                        ))}
                      </select>
                    </div>
                  </div>
                  <button
                    onClick={handleLoadDiff}
                    disabled={!selectedVersionA || !selectedVersionB || selectedVersionA === selectedVersionB || diffLoading}
                    className="flex items-center gap-2 bg-ocean-700 hover:bg-ocean-600 disabled:opacity-50 disabled:cursor-not-allowed text-navy-900 px-5 py-2.5 rounded-lg text-sm font-medium transition-all duration-200"
                  >
                    {diffLoading ? (
                      <>
                        <Loader2 className="w-4 h-4 animate-spin" />
                        Vergleiche...
                      </>
                    ) : (
                      <>
                        <GitCompare className="w-4 h-4" />
                        Vergleichen
                      </>
                    )}
                  </button>
                </div>

                {/* Diff result */}
                {diff && <DiffViewer diff={diff} />}

                {/* Version timeline */}
                <div>
                  <p className="label-premium mb-4">Versionshistorie</p>
                  <div className="space-y-3 relative">
                    {/* Timeline line */}
                    <div className="absolute left-5 top-6 bottom-6 w-px bg-sand-200" />

                    {versions.map((version, idx) => (
                      <div
                        key={version.id}
                        style={{ animationDelay: `${idx * 80}ms` }}
                        className="animate-fade-in-up relative pl-12"
                      >
                        {/* Timeline dot */}
                        <div className="absolute left-3.5 top-5 w-3 h-3 rounded-full bg-ocean-500 border-2 border-white z-10" />

                        <div className="card-premium px-6 py-5 group hover:shadow-lg hover:shadow-ocean-500/10 transition-all duration-200">
                          <div className="flex items-start justify-between">
                            <div>
                              <div className="font-mono text-ocean-600 font-semibold mb-1">
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
                              {version.changed_by && (
                                <div className="text-xs text-navy-500 mt-1">
                                  von {version.changed_by}
                                </div>
                              )}
                              {version.tags && version.tags.length > 0 && (
                                <div className="flex gap-1.5 mt-2">
                                  {version.tags.map((tag) => (
                                    <span
                                      key={tag}
                                      className="inline-block rounded-md border border-sand-200 bg-sand-50/40 px-2 py-0.5 text-[10px] font-medium text-navy-600"
                                    >
                                      {tag}
                                    </span>
                                  ))}
                                </div>
                              )}
                            </div>
                            <button
                              onClick={() => handleSelectVersion(version)}
                              className="flex items-center gap-1.5 text-xs text-ocean-600 hover:text-ocean-500 transition-colors opacity-0 group-hover:opacity-100"
                              title="Version wiederherstellen"
                            >
                              <RotateCcw className="w-3.5 h-3.5" />
                              Laden
                            </button>
                          </div>
                        </div>
                      </div>
                    ))}
                  </div>
                </div>
              </>
            )}
          </div>
        )}
      </div>
    </div>
  )
}
