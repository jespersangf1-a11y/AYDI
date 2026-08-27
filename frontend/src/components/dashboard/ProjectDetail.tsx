import { useEffect, useState, useMemo, useRef, lazy, Suspense } from 'react'
import { useNavigate, useParams } from 'react-router-dom'
import {
  Anchor,
  ArrowLeft,
  Camera,
  Ship,
  Wrench,
  Zap,
  Clock,
  Layers,
  Calendar,
  Euro,
  GitCompare,
  BarChart3,
  ImageIcon,
  ChevronRight,
  Loader2,
  Box,
  Map,
  Package,
  RotateCcw,
  Save,
  Share2,
  Eye,
  TrendingUp,
  Radio,
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
  createLayoutVersion,
  updateLayout,
  getMyOrganizations,
  setProjectOrg,
} from '../../services/api'
import HeroSection from '../layout/HeroSection'
import { MEDIA } from '../../config/media'
import type {
  Project,
  Layout,
  AnalysisResult,
  AnalysisUnavailable,
  LayoutVersion,
  LayoutDiff,
  FullAnalysisResult,
  AnalysisModule,
  ImageUploadData,
  Organization,
} from '../../types'
import { istNichtBeurteilbar } from '../../types'
import {
  BOAT_CLASS_LABELS,
  STATUS_LABELS,
  ANALYSIS_MODULE_LABELS,
  IMAGE_TYPE_LABELS,
} from '../../types'
import ScoreGauge from '../analysis/ScoreGauge'
import SubScoreBars from '../analysis/SubScoreBars'
import ZoneMaterialsPanel from '../materials/ZoneMaterialsPanel'
import StructuralItemsPanel from '../structural/StructuralItemsPanel'
import LayoutEditor from '../editor/LayoutEditor'
import ShareDialog from './ShareDialog'
import CollabPanel from '../collab/CollabPanel'
import { useCollaboration } from '../../hooks/useCollaboration'
import WarningList from '../analysis/WarningList'
import LayoutViewer from '../analysis/LayoutViewer'
import FullAnalysisView from '../analysis/FullAnalysisView'
import ModuleSelector from '../analysis/ModuleSelector'
import CostOverview from '../costs/CostOverview'
import ImageUpload from '../images/ImageUpload'
import ServiceReportList from '../service/ServiceReportList'
import DiffViewer from '../compare/DiffViewer'
// ConfidenceBadge is used by FullAnalysisView internally

// Lazy-load 3D viewer to avoid large bundle on initial load
const DeckViewer3D = lazy(() => import('../viewer3d/DeckViewer3D'))

interface ProjectDetailProps {
  projectId: string
  onBack: () => void
}

import {
  type TabType,
  type ViewerMode,
  isTabType,
  collectWarnings,
  latestByModule,
  moduleScoreClass,
  moduleBorderClass,
  moduleBgClass,
} from './projectDetail/helpers'

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
  // Ein Modul, das mangels Daten nicht urteilen konnte. Bewusst getrennt von
  // `error`: das ist kein Fehlschlag, sondern eine Auskunft.
  const [nichtBeurteilbar, setNichtBeurteilbar] = useState<AnalysisUnavailable | null>(null)

  // ─── Version state ───
  const [versions, setVersions] = useState<LayoutVersion[]>([])
  const [versionsLoaded, setVersionsLoaded] = useState(false)
  const [versionsLoading, setVersionsLoading] = useState(false)
  const [selectedVersionA, setSelectedVersionA] = useState<string | null>(null)
  const [selectedVersionB, setSelectedVersionB] = useState<string | null>(null)
  const [diff, setDiff] = useState<LayoutDiff | null>(null)
  const [diffLoading, setDiffLoading] = useState(false)
  const [savingVersion, setSavingVersion] = useState(false)
  const [restoringVersionId, setRestoringVersionId] = useState<string | null>(null)

  // ─── Score comparison (refit loop: before/after) ───
  const [compareRunA, setCompareRunA] = useState<string | null>(null)
  const [compareRunB, setCompareRunB] = useState<string | null>(null)

  // ─── Material assignments changed since last materials analysis ───
  // Lifted here so the hint survives tab switches; reset on successful run.
  const [materialsChanged, setMaterialsChanged] = useState(false)
  const [structuralChanged, setStructuralChanged] = useState(false)

  // ─── Sharing dialog (pillar 4, stage 1) ───
  const [shareDialogOpen, setShareDialogOpen] = useState(false)

  // ─── Organization attachment (pillar 4, stage 2) ───
  const [myOrgs, setMyOrgs] = useState<Organization[]>([])
  const [orgSaving, setOrgSaving] = useState(false)

  // ─── Live collaboration (pillar 4, stage 2) ───
  const [collabActive, setCollabActive] = useState(false)
  const collab = useCollaboration(
    collabActive ? selectedLayout?.id ?? null : null,
    collabActive
  )

  // ─── Zone editor (pillar 3: graphical layout editing) ───
  const [editingLayout, setEditingLayout] = useState(false)
  const [savingLayoutEdit, setSavingLayoutEdit] = useState(false)
  // Ref (not state): read inside navigation guards without re-renders
  const editorDirtyRef = useRef(false)

  const confirmLeaveEditor = (): boolean => {
    if (!editingLayout || !editorDirtyRef.current) return true
    const ok = window.confirm(
      'Ungespeicherte Layout-Änderungen gehen verloren — trotzdem fortfahren?',
    )
    if (ok) {
      editorDirtyRef.current = false
      setEditingLayout(false)
    }
    return ok
  }

  // ─── Images state ───
  const [images, setImages] = useState<ImageUploadData[]>([])

  // ─── Snapshot indicator ───
  const [snapshotLabel, setSnapshotLabel] = useState<string | null>(null)

  // ─── UI state ───
  // Tab state derives from the URL — supports deep links. The route is the
  // splat "/projects/:id/*" (react-router v6 has no optional params), so the
  // tab segment lives under params['*'], NOT params.tab — reading only
  // params.tab left activeTab permanently on 'overview' and made every other
  // tab unreachable in the browser.
  const params = useParams<{ tab?: string; '*': string }>()
  const tabFromUrl = params.tab ?? params['*']?.split('/')[0]
  const navigate = useNavigate()
  const activeTab: TabType = isTabType(tabFromUrl) ? tabFromUrl : 'overview'
  const setActiveTab = (next: TabType) => {
    // Leaving the layouts tab unmounts the zone editor — guard unsaved work
    if (!confirmLeaveEditor()) return
    navigate(`/projects/${projectId}/${next}`, { replace: false })
  }
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
    setCompareRunA(null)
    setCompareRunB(null)
    setMaterialsChanged(false)
    setStructuralChanged(false)
    setEditingLayout(false)
  }, [selectedLayout?.id])

  // ─── Save zone-editor changes (PATCH — previous state auto-versioned) ───
  const handleSaveLayoutEdit = async (
    zones: Layout['zones'],
    passages: Layout['passages'],
    changeSummary: string,
    zoneRenames: Record<string, string>,
  ) => {
    if (!selectedLayout) return
    setSavingLayoutEdit(true)
    setError(null)
    try {
      const updated = await updateLayout(projectId, selectedLayout.id, {
        zones,
        passages,
        change_summary: changeSummary || 'Layout im Editor bearbeitet',
        // Server cascades renames to material/structural/cost references
        ...(Object.keys(zoneRenames).length > 0 ? { zone_renames: zoneRenames } : {}),
      })
      editorDirtyRef.current = false
      setSelectedLayout(updated)
      setLayouts((prev) => prev.map((l) => (l.id === updated.id ? updated : l)))
      setEditingLayout(false)
      setSnapshotLabel(null)
      // Geometry changed: derived results are stale
      setFullAnalysisResult(null)
      setDiff(null)
      setSelectedVersionA(null)
      setSelectedVersionB(null)
      setCompareRunA(null)
      setCompareRunB(null)
      setMaterialsChanged(true)
      setStructuralChanged(true)
      if (versionsLoaded) {
        const v = await getLayoutVersions(projectId, updated.id)
        setVersions(v)
      }
    } catch (e) {
      setError(e instanceof Error ? e.message : 'Layout konnte nicht gespeichert werden')
    } finally {
      setSavingLayoutEdit(false)
    }
  }

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

  // ─── Viewer gating (pillar 4, stage 1) ───
  // Shared members with role 'viewer' get a read-only UI. The backend
  // enforces this server-side (403) — this only prevents dead-end clicks.
  // No access_role (legacy responses) counts as editable: worst case the
  // server rejects, we never over-lock the owner's own project.
  const canEdit =
    !project?.access_role ||
    project.access_role === 'owner' ||
    project.access_role === 'editor'
  const READ_ONLY_HINT = 'Nur-Lesen-Zugriff — Änderungen sind für Betrachter deaktiviert'

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
        // Always set (also to null): without this, navigating to a project
        // with zero layouts kept the PREVIOUS project's layout selected and
        // fired requests with a foreign layout_id.
        setSelectedLayout(lays[0] ?? null)
        setSelectedAnalysis(anals[0] ?? null)
      })
      .catch((e) => setError(e.message))
      .finally(() => setLoading(false))
  }, [projectId])

  // Load the owner's organizations so they can attach/detach the project.
  useEffect(() => {
    if (project?.access_role === 'owner') {
      getMyOrganizations().then(setMyOrgs).catch(() => setMyOrgs([]))
    }
  }, [project?.access_role])

  const handleSetOrg = async (orgId: string | null) => {
    if (!project) return
    setOrgSaving(true)
    setError(null)
    try {
      const updated = await setProjectOrg(project.id, orgId)
      setProject((prev) => (prev ? { ...prev, org_id: updated.org_id, access_role: updated.access_role } : prev))
    } catch (e) {
      setError(e instanceof Error ? e.message : 'Organisationszuordnung fehlgeschlagen')
    } finally {
      setOrgSaving(false)
    }
  }

  // ─── Run single module analysis ───
  const handleRunAnalysis = async (module: string) => {
    if (!selectedLayout) return
    // Concurrency guard: a second parallel run would end the shared spinner
    // early and duplicate history rows
    if (analyzing || fullAnalyzing) return
    setAnalyzing(true)
    setAnalyzingModule(module)
    setError(null)
    setNichtBeurteilbar(null)
    try {
      const result = await runAnalysis(projectId, selectedLayout.id, module)
      // Ohne Datengrundlage gibt es keinen Wert, der in die Liste gehoerte —
      // er wuerde in den Gesamtwert des Projekts einfliessen und dort eine
      // Bewertung vortaeuschen, die nie stattgefunden hat.
      if (istNichtBeurteilbar(result)) {
        setNichtBeurteilbar(result)
        return
      }
      setAnalyses((prev) => [result, ...prev])
      setSelectedAnalysis(result)
      setSelectedModuleForDetail(module)
      if (module === 'materials') setMaterialsChanged(false)
      if (module === 'structural') setStructuralChanged(false)
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
    if (analyzing || fullAnalyzing) return
    setFullAnalyzing(true)
    setError(null)
    try {
      const result = await runFullAnalysis(projectId, selectedLayout.id)
      setFullAnalysisResult(result)
      // Refresh analyses list
      const refreshed = await listAnalyses(projectId)
      setAnalyses(refreshed)
      if (refreshed.length > 0) setSelectedAnalysis(refreshed[0])
      // Full analysis covers materials + structural — clear the pending
      // "Änderungen noch nicht analysiert" hints (only for modules that ran)
      if (result.modules?.materials) setMaterialsChanged(false)
      if (result.modules?.structural) setStructuralChanged(false)
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

  // ─── Preview a version (viewer only — analyses always use the DB state) ───
  const handlePreviewVersion = (version: LayoutVersion) => {
    if (!selectedLayout) return
    if (version.zones_snapshot && version.passages_snapshot) {
      setSelectedLayout({
        ...selectedLayout,
        zones: version.zones_snapshot,
        passages: version.passages_snapshot,
      })
      setSnapshotLabel(`Vorschau v${version.version_number} — nicht der Analyse-Stand`)
    }
  }

  // ─── Really restore a version (PATCH — server snapshots current state first) ───
  const handleRestoreVersion = async (version: LayoutVersion) => {
    if (!selectedLayout) return
    // A version without geometry snapshots cannot be restored — patching
    // zones=[] would silently EMPTY the layout instead.
    if (!version.zones_snapshot || !version.passages_snapshot) {
      setError('Diese Version enthält keinen Geometrie-Snapshot und kann nicht wiederhergestellt werden.')
      return
    }
    setRestoringVersionId(version.id)
    setError(null)
    try {
      const meta = version.layout_meta_snapshot
      const updated = await updateLayout(projectId, selectedLayout.id, {
        zones: version.zones_snapshot,
        passages: version.passages_snapshot,
        // Restore analysis-relevant meta too (deck height affects scores)
        ...(meta?.deck_height_mm != null ? { deck_height_mm: meta.deck_height_mm } : {}),
        change_summary: `Wiederhergestellt von Version ${version.version_number}`,
      })
      setSelectedLayout(updated)
      setLayouts((prev) => prev.map((l) => (l.id === updated.id ? updated : l)))
      setSnapshotLabel(null)
      // The restored geometry invalidates everything derived from the old
      // state — leaving these standing would present stale scores as current.
      setFullAnalysisResult(null)
      setDiff(null)
      setSelectedVersionA(null)
      setSelectedVersionB(null)
      setCompareRunA(null)
      setCompareRunB(null)
      const v = await getLayoutVersions(projectId, updated.id)
      setVersions(v)
      setVersionsLoaded(true)
    } catch (e) {
      setError(e instanceof Error ? e.message : 'Version konnte nicht wiederhergestellt werden')
    } finally {
      setRestoringVersionId(null)
    }
  }

  // ─── Exit a version preview (back to the real DB state) ───
  const handleExitPreview = () => {
    if (!selectedLayout) return
    const original = layouts.find((l) => l.id === selectedLayout.id)
    if (original) setSelectedLayout(original)
    setSnapshotLabel(null)
  }

  // ─── Save current layout state as a named version ───
  const handleSaveVersion = async () => {
    if (!selectedLayout) return
    setSavingVersion(true)
    setError(null)
    try {
      await createLayoutVersion(projectId, selectedLayout.id, {
        zones_snapshot: selectedLayout.zones,
        passages_snapshot: selectedLayout.passages,
        change_summary: 'Manuell gesicherte Version',
      })
      await handleLoadVersions()
    } catch (e) {
      setError(e instanceof Error ? e.message : 'Version konnte nicht gesichert werden')
    } finally {
      setSavingVersion(false)
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
    {
      // Pipeline B (Bildanalyse): ohne diesen Einstieg war der Bild-Upload im
      // Projektkontext nur über die freie Schnellanalyse erreichbar.
      id: 'images',
      label: 'Bilder',
      icon: <Camera className="w-4 h-4" />,
      badge: images.length > 0 ? images.length : undefined,
    },
    { id: 'materials', label: 'Materialien', icon: <Package className="w-4 h-4" /> },
    { id: 'structural', label: 'Struktur', icon: <Anchor className="w-4 h-4" /> },
    { id: 'costs', label: 'Kosten', icon: <Euro className="w-4 h-4" /> },
    {
      // Pipeline C (Textanalyse): Datengrundlage für das Modul service_patterns.
      id: 'service',
      label: 'Serviceberichte',
      icon: <Wrench className="w-4 h-4" />,
    },
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

        {nichtBeurteilbar && (
          <div className="card-premium bg-navy-900/20 border-navy-700/40 p-4 text-navy-300 text-sm mb-8">
            <div className="flex items-start justify-between gap-4">
              <div>
                <p className="font-medium text-navy-200 mb-1">
                  Nicht beurteilbar
                </p>
                <p>{nichtBeurteilbar.reason}</p>
                {nichtBeurteilbar.suggestions.length > 0 && (
                  <ul className="mt-2 list-disc list-inside text-navy-400">
                    {nichtBeurteilbar.suggestions.map((vorschlag) => (
                      <li key={vorschlag}>{vorschlag}</li>
                    ))}
                  </ul>
                )}
              </div>
              <button
                onClick={() => setNichtBeurteilbar(null)}
                className="text-navy-400 hover:text-navy-300 text-xs font-medium shrink-0"
              >
                Schließen
              </button>
            </div>
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
            {/* Org attachment (pillar 4, stage 2): owner may assign the
                project to one of their organizations, or keep it private. */}
            {project.access_role === 'owner' && myOrgs.length > 0 && (
              <div className="flex items-center gap-2">
                <span className="label-premium">Organisation</span>
                <select
                  value={project.org_id ?? ''}
                  onChange={(e) => handleSetOrg(e.target.value || null)}
                  disabled={orgSaving}
                  aria-label="Projekt einer Organisation zuordnen"
                  className="rounded-lg border border-sand-300 bg-white px-2.5 py-1.5 text-xs text-navy-800 focus:border-ocean-500 focus:outline-none disabled:opacity-50"
                >
                  <option value="">Privat</option>
                  {myOrgs.map((o) => (
                    <option key={o.id} value={o.id}>{o.name}</option>
                  ))}
                </select>
              </div>
            )}
            {/* Sharing (pillar 4, stage 1): owner shares; members see a badge */}
            {project.access_role === 'owner' ? (
              <button
                onClick={() => setShareDialogOpen(true)}
                className="flex items-center gap-2 bg-sand-100 border border-sand-300 hover:bg-sand-200 text-navy-700 px-4 py-2 rounded-lg text-xs font-medium transition-all"
              >
                <Share2 className="w-3.5 h-3.5" />
                Teilen
              </button>
            ) : project.access_role ? (
              <span className="text-xs px-2.5 py-1 rounded-full border bg-ocean-100 text-ocean-700 border-ocean-300 whitespace-nowrap">
                Geteilt · {project.access_role === 'editor' ? 'Bearbeiten' : 'Nur Lesen'}
              </span>
            ) : null}
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
                      disabled={fullAnalyzing || !selectedLayout || !canEdit}
                      title={!canEdit ? READ_ONLY_HINT : undefined}
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
                        // Switching layouts unmounts the editor — guard dirty state
                        if (!confirmLeaveEditor()) return
                        setSelectedLayout(layout)
                        // Re-selecting the SAME card must also end a preview
                        // (the reset effect only fires on id CHANGE)
                        setSnapshotLabel(null)
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
                    <button
                      onClick={handleExitPreview}
                      className="ml-1 underline hover:text-amber-100 transition-colors"
                      aria-label="Vorschau beenden"
                    >
                      beenden
                    </button>
                  </span>
                )}
                <button
                  onClick={() => setEditingLayout(true)}
                  disabled={editingLayout || snapshotLabel !== null || !canEdit}
                  title={
                    !canEdit
                      ? READ_ONLY_HINT
                      : snapshotLabel
                        ? 'Vorschau aktiv — erst beenden, dann bearbeiten'
                        : 'Zonen grafisch bearbeiten (Vorzustand wird versioniert)'
                  }
                  className="flex items-center gap-1.5 px-3 py-1.5 rounded-lg text-xs font-medium transition-all bg-ocean-700 hover:bg-ocean-600 disabled:opacity-50 text-navy-900 mr-2"
                >
                  Bearbeiten
                </button>
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

            {/* Zone editor (replaces the viewers while active) */}
            {selectedLayout && editingLayout && (
              <LayoutEditor
                key={selectedLayout.id}
                zones={selectedLayout.zones}
                passages={selectedLayout.passages}
                saving={savingLayoutEdit}
                onSave={handleSaveLayoutEdit}
                onCancel={() => {
                  editorDirtyRef.current = false
                  setEditingLayout(false)
                }}
                onDirtyChange={(dirty) => {
                  editorDirtyRef.current = dirty
                }}
              />
            )}

            {/* Live-Session join / status (pillar 4, stage 2) */}
            {selectedLayout && !editingLayout && (
              <div className="flex items-center gap-3">
                {!collabActive ? (
                  <button
                    onClick={() => setCollabActive(true)}
                    className="flex items-center gap-1.5 px-3 py-1.5 rounded-lg text-xs font-medium transition-all bg-sand-100 border border-sand-300 hover:bg-sand-200 text-navy-700"
                    title="Andere Teammitglieder live in diesem Layout sehen (Präsenz, Cursor, Kommentare)"
                  >
                    <Radio className="w-3.5 h-3.5" />
                    Live-Session beitreten
                  </button>
                ) : (
                  <span className="flex items-center gap-1.5 text-xs text-emerald-700">
                    <Radio className="w-3.5 h-3.5" />
                    Live-Session aktiv
                  </span>
                )}
              </div>
            )}

            {/* Live-Session panel */}
            {selectedLayout && !editingLayout && collabActive && (
              <CollabPanel
                status={collab.status}
                statusDetail={collab.statusDetail}
                participants={collab.participants}
                comments={collab.comments}
                activity={collab.activity}
                onSendComment={collab.sendComment}
                onEndSession={() => setCollabActive(false)}
              />
            )}

            {/* Layout Viewer */}
            {selectedLayout && !editingLayout && viewerMode === '2d' && (
              <div className="card-premium p-0 overflow-hidden">
                <LayoutViewer
                  zones={selectedLayout.zones}
                  passages={selectedLayout.passages}
                  remoteCursors={collabActive ? Object.values(collab.cursors) : undefined}
                  remoteSelections={collabActive ? collab.selections : undefined}
                  onCursorMove={collabActive ? collab.sendCursor : undefined}
                  onZoneSelect={collabActive ? collab.sendZoneSelect : undefined}
                />
              </div>
            )}

            {selectedLayout && !editingLayout && viewerMode === '3d' && (
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
                    disabled={fullAnalyzing || !selectedLayout || !canEdit}
                    title={!canEdit ? READ_ONLY_HINT : undefined}
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

            {/* Module Selector — all 11 modules; hidden for read-only members
                (running an analysis writes history rows → editor required) */}
            {selectedLayout && canEdit && (
              <ModuleSelector
                onSelect={(mod) => handleRunAnalysis(mod)}
                selectedModule={(analyzingModule as AnalysisModule) ?? undefined}
                availableModules={undefined}
              />
            )}
            {selectedLayout && !canEdit && (
              <div className="card-premium px-6 py-4 text-sm text-navy-600">
                {READ_ONLY_HINT}. Vorhandene Analyseergebnisse können Sie unten einsehen.
              </div>
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

                {/* Before/after score comparison (refit loop).
                    Runs are filtered to the SELECTED layout — analyses are
                    project-wide, and comparing runs of two different layouts
                    would present an apples/oranges delta as the effect of a
                    refit change. Runs older than the layout's last change are
                    marked as outdated. */}
                {analyses.filter((a) => a.layout_id === selectedLayout?.id).length >= 2 && (
                  <div className="card-premium px-6 py-5 mb-4">
                    <h3 className="font-sans font-semibold text-navy-900 mb-3 flex items-center gap-2 text-sm">
                      <TrendingUp className="w-4 h-4 text-ocean-500" />
                      Vorher/Nachher-Vergleich
                    </h3>
                    <div className="grid grid-cols-1 sm:grid-cols-2 gap-4 mb-2">
                      <div>
                        <label className="label-premium mb-2 block">Lauf A (vorher)</label>
                        <select
                          value={compareRunA ?? ''}
                          onChange={(e) => {
                            setCompareRunA(e.target.value || null)
                            setCompareRunB(null)
                          }}
                          className="w-full rounded-lg border border-sand-200 bg-white px-3 py-2 text-sm text-navy-900 focus:border-ocean-500 focus:outline-none"
                        >
                          <option value="">Wählen...</option>
                          {analyses
                            .filter((a) => a.layout_id === selectedLayout?.id)
                            .map((a) => (
                              <option key={a.id} value={a.id}>
                                {ANALYSIS_MODULE_LABELS[a.module as AnalysisModule] ?? a.module} —{' '}
                                {new Date(a.created_at).toLocaleString('de-DE', {
                                  day: '2-digit', month: '2-digit', hour: '2-digit', minute: '2-digit',
                                })}{' '}
                                ({Math.round(a.overall_score)})
                                {selectedLayout &&
                                new Date(a.created_at) < new Date(selectedLayout.updated_at)
                                  ? ' · veraltet (Layout seitdem geändert)'
                                  : ''}
                              </option>
                            ))}
                        </select>
                      </div>
                      <div>
                        <label className="label-premium mb-2 block">Lauf B (nachher)</label>
                        <select
                          value={compareRunB ?? ''}
                          onChange={(e) => setCompareRunB(e.target.value || null)}
                          disabled={!compareRunA}
                          className="w-full rounded-lg border border-sand-200 bg-white px-3 py-2 text-sm text-navy-900 focus:border-ocean-500 focus:outline-none disabled:opacity-50"
                        >
                          <option value="">Wählen...</option>
                          {analyses
                            .filter((a) => {
                              const runA = analyses.find((x) => x.id === compareRunA)
                              return (
                                runA &&
                                a.module === runA.module &&
                                a.layout_id === runA.layout_id &&
                                a.id !== runA.id
                              )
                            })
                            .map((a) => (
                              <option key={a.id} value={a.id}>
                                {new Date(a.created_at).toLocaleString('de-DE', {
                                  day: '2-digit', month: '2-digit', hour: '2-digit', minute: '2-digit',
                                })}{' '}
                                ({Math.round(a.overall_score)})
                                {selectedLayout &&
                                new Date(a.created_at) < new Date(selectedLayout.updated_at)
                                  ? ' · veraltet (Layout seitdem geändert)'
                                  : ''}
                              </option>
                            ))}
                        </select>
                      </div>
                    </div>
                    {(() => {
                      const runA = analyses.find((a) => a.id === compareRunA)
                      const runB = analyses.find((a) => a.id === compareRunB)
                      if (!runA || !runB) {
                        return (
                          <p className="text-xs text-navy-500">
                            Zwei Läufe desselben Moduls wählen, um die Wirkung einer
                            Änderung zu sehen.
                          </p>
                        )
                      }
                      const delta = runB.overall_score - runA.overall_score
                      const subKeys = Array.from(
                        new Set([
                          ...Object.keys(runA.sub_scores ?? {}),
                          ...Object.keys(runB.sub_scores ?? {}),
                        ]),
                      )
                      const deltaClass =
                        delta > 0 ? 'text-emerald-600' : delta < 0 ? 'text-red-600' : 'text-navy-600'
                      return (
                        <div className="mt-2 border-t border-sand-200 pt-3">
                          <p className="text-sm text-navy-900 mb-2">
                            Gesamt:{' '}
                            <span className="font-mono">{Math.round(runA.overall_score)}</span>
                            {' → '}
                            <span className="font-mono">{Math.round(runB.overall_score)}</span>{' '}
                            <span className={`font-mono font-semibold ${deltaClass}`}>
                              ({delta > 0 ? '+' : ''}
                              {delta.toFixed(1)})
                            </span>
                          </p>
                          {subKeys.length > 0 && (
                            <ul className="grid grid-cols-1 sm:grid-cols-2 gap-x-6 gap-y-1">
                              {subKeys.map((key) => {
                                const a = Number(runA.sub_scores?.[key] ?? NaN)
                                const b = Number(runB.sub_scores?.[key] ?? NaN)
                                if (isNaN(a) || isNaN(b)) return null
                                const d = b - a
                                const cls =
                                  d > 0 ? 'text-emerald-600' : d < 0 ? 'text-red-600' : 'text-navy-500'
                                return (
                                  <li key={key} className="text-xs text-navy-700 flex justify-between gap-2">
                                    <span className="truncate">{key.replace(/_/g, ' ')}</span>
                                    <span className={`font-mono ${cls}`}>
                                      {Math.round(a)}→{Math.round(b)} ({d > 0 ? '+' : ''}
                                      {d.toFixed(1)})
                                    </span>
                                  </li>
                                )
                              })}
                            </ul>
                          )}
                        </div>
                      )
                    })()}
                  </div>
                )}

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
            TAB: IMAGES — Pipeline B (Bildanalyse) im Projektkontext
        ═══════════════════════════════════════════════════════════════ */}
        {activeTab === 'images' && (
          <div className="space-y-8 animate-fade-in-up">
            <div className="card-premium px-8 py-6">
              <div className="flex items-start gap-4">
                <Camera className="w-6 h-6 text-ocean-500 shrink-0 mt-0.5" />
                <div>
                  <h2 className="font-serif text-xl text-navy-900 mb-1">
                    Bilder & visuelle Analyse
                  </h2>
                  <p className="text-navy-700 text-sm max-w-2xl">
                    Fotos und Renderings speisen Pipeline B. Sie fließen als visueller
                    Anteil in die Score-Fusion ein — besonders stark in Emotion,
                    Materialien und Markenidentität. Jeder Befund erhält eine eigene
                    Konfidenz; unsichere Befunde sind standardmäßig ausgeblendet.
                  </p>
                </div>
              </div>
            </div>

            {canEdit ? (
              <ImageUpload
                boatClass={project.boat_class}
                projectId={projectId}
                onUploadComplete={(img) => setImages((prev) => [img, ...prev])}
              />
            ) : (
              <div className="card-premium px-8 py-12 text-center">
                <Camera className="w-12 h-12 mx-auto mb-4 text-navy-600" />
                <p className="text-navy-600">{READ_ONLY_HINT}</p>
                <p className="text-navy-500 text-xs mt-2">
                  Bereits hochgeladene Bilder können Sie unten einsehen.
                </p>
              </div>
            )}

            {/* Bereits hinterlegte Projektbilder (GET /projects/{id}/images) */}
            <div className="card-premium px-8 py-6">
              <h3 className="font-serif text-lg text-navy-900 mb-4">
                Hinterlegte Projektbilder
                {images.length > 0 && (
                  <span className="ml-2 font-mono text-sm text-navy-600">
                    ({images.length})
                  </span>
                )}
              </h3>
              {images.length === 0 ? (
                <div className="py-8 text-center">
                  <ImageIcon className="w-10 h-10 mx-auto mb-3 text-navy-600" />
                  <p className="text-navy-600 text-sm">
                    Für dieses Projekt sind noch keine Bilder hinterlegt.
                  </p>
                  <p className="text-navy-500 text-xs mt-2">
                    Ohne Bilder bleibt die visuelle Analyse (Pipeline B)
                    „nicht beurteilbar“ — die Module bewerten dann rein strukturell.
                  </p>
                </div>
              ) : (
                <ul className="divide-y divide-sand-200">
                  {images.map((img) => (
                    <li
                      key={img.id}
                      className="py-3 flex flex-wrap items-center justify-between gap-3"
                    >
                      <div className="min-w-0">
                        <p className="text-navy-900 text-sm font-medium truncate">
                          {IMAGE_TYPE_LABELS[img.image_type] ?? img.image_type}
                          {img.zone_name && (
                            <span className="text-navy-600 font-normal"> · {img.zone_name}</span>
                          )}
                        </p>
                        <p className="text-navy-600 text-xs font-mono mt-0.5">
                          {new Date(img.uploaded_at).toLocaleDateString('de-DE')} ·{' '}
                          {Math.round(img.file_size_bytes / 1024)} KB
                        </p>
                      </div>
                      <span
                        className={`text-xs px-2.5 py-1 rounded-full border whitespace-nowrap ${
                          img.ai_analysis
                            ? 'bg-ocean-100 text-ocean-700 border-ocean-300'
                            : 'bg-sand-100 text-navy-600 border-sand-300'
                        }`}
                      >
                        {img.ai_analysis ? 'Visuell analysiert' : 'Noch nicht analysiert'}
                      </span>
                    </li>
                  ))}
                </ul>
              )}
            </div>
          </div>
        )}

        {/* ═══════════════════════════════════════════════════════════════
            TAB: MATERIALS — Materialzuweisungen (Refit: Optik/Material)
        ═══════════════════════════════════════════════════════════════ */}
        {activeTab === 'materials' && (
          <div className="space-y-8 animate-fade-in-up">
            {selectedLayout ? (
              <ZoneMaterialsPanel
                key={selectedLayout.id}
                projectId={projectId}
                layoutId={selectedLayout.id}
                zones={selectedLayout.zones}
                deckHeightMm={selectedLayout.deck_height_mm}
                onRunMaterialsAnalysis={() => handleRunAnalysis('materials')}
                analysisRunning={analyzing && analyzingModule === 'materials'}
                busy={analyzing || fullAnalyzing}
                changedSinceAnalysis={materialsChanged}
                onChangedSinceAnalysis={setMaterialsChanged}
                readOnly={!canEdit}
              />
            ) : (
              <div className="card-premium px-8 py-12 text-center">
                <Package className="w-12 h-12 mx-auto mb-4 text-navy-600" />
                <p className="text-navy-600">Kein Layout ausgewählt</p>
              </div>
            )}
          </div>
        )}

        {/* ═══════════════════════════════════════════════════════════════
            TAB: STRUCTURAL — gemessene Gewichte/Positionen (Trimm/CG)
        ═══════════════════════════════════════════════════════════════ */}
        {activeTab === 'structural' && (
          <div className="space-y-8 animate-fade-in-up">
            {selectedLayout ? (
              <StructuralItemsPanel
                key={selectedLayout.id}
                projectId={projectId}
                layoutId={selectedLayout.id}
                zones={selectedLayout.zones}
                onRunStructuralAnalysis={() => handleRunAnalysis('structural')}
                analysisRunning={analyzing && analyzingModule === 'structural'}
                busy={analyzing || fullAnalyzing}
                changedSinceAnalysis={structuralChanged}
                onChangedSinceAnalysis={setStructuralChanged}
                readOnly={!canEdit}
              />
            ) : (
              <div className="card-premium px-8 py-12 text-center">
                <Anchor className="w-12 h-12 mx-auto mb-4 text-navy-600" />
                <p className="text-navy-600">Kein Layout ausgewählt</p>
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
            TAB: SERVICE — Pipeline C (Serviceberichte / Textanalyse)
        ═══════════════════════════════════════════════════════════════ */}
        {activeTab === 'service' && (
          <div className="space-y-8 animate-fade-in-up">
            <div className="card-premium px-8 py-6">
              <div className="flex items-start gap-4">
                <Wrench className="w-6 h-6 text-ocean-500 shrink-0 mt-0.5" />
                <div>
                  <h2 className="font-serif text-xl text-navy-900 mb-1">
                    Serviceberichte (Pipeline C)
                  </h2>
                  <p className="text-navy-700 text-sm max-w-2xl">
                    Wartungs-, Garantie-, Umbau- und Reklamationsberichte sind die
                    Datengrundlage des Moduls „Service-Muster“. Ohne erfasste Berichte
                    meldet das Modul dauerhaft „nicht beurteilbar“ und wird bei der
                    Vollanalyse übersprungen.
                  </p>
                </div>
              </div>
            </div>

            <ServiceReportList />
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
                <p className="text-navy-600 mb-4">Noch keine Versionen vorhanden</p>
                <button
                  onClick={handleSaveVersion}
                  disabled={savingVersion || snapshotLabel !== null || !canEdit}
                  title={!canEdit ? READ_ONLY_HINT : undefined}
                  className="inline-flex items-center gap-2 bg-ocean-700 hover:bg-ocean-600 disabled:opacity-50 text-navy-900 px-5 py-2.5 rounded-lg text-sm font-medium transition-all duration-200"
                >
                  {savingVersion ? (
                    <Loader2 className="w-4 h-4 animate-spin" />
                  ) : (
                    <Save className="w-4 h-4" />
                  )}
                  Aktuellen Stand als Version sichern
                </button>
              </div>
            )}

            {selectedLayout && versionsLoaded && versions.length > 0 && (
              <>
                {/* Save current state as version */}
                <div className="flex justify-end">
                  <button
                    onClick={handleSaveVersion}
                    disabled={savingVersion || snapshotLabel !== null || !canEdit}
                    title={
                      !canEdit
                        ? READ_ONLY_HINT
                        : snapshotLabel
                          ? 'Vorschau aktiv — erst zurücksetzen oder wiederherstellen'
                          : 'Aktuellen Layout-Stand als Version sichern'
                    }
                    className="inline-flex items-center gap-2 bg-ocean-700 hover:bg-ocean-600 disabled:opacity-50 text-navy-900 px-5 py-2.5 rounded-lg text-sm font-medium transition-all duration-200"
                  >
                    {savingVersion ? (
                      <Loader2 className="w-4 h-4 animate-spin" />
                    ) : (
                      <Save className="w-4 h-4" />
                    )}
                    Version sichern
                  </button>
                </div>

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
                            <div className="flex items-center gap-3 opacity-0 group-hover:opacity-100 group-focus-within:opacity-100 focus-within:opacity-100 transition-opacity">
                              <button
                                onClick={() => handlePreviewVersion(version)}
                                disabled={!version.zones_snapshot || !version.passages_snapshot}
                                className="flex items-center gap-1.5 text-xs text-navy-600 hover:text-ocean-500 transition-colors disabled:opacity-50 focus-visible:outline focus-visible:outline-2 focus-visible:outline-ocean-500"
                                title="Im Viewer ansehen (ändert nichts)"
                              >
                                <Eye className="w-3.5 h-3.5" />
                                Ansehen
                              </button>
                              <button
                                onClick={() => handleRestoreVersion(version)}
                                disabled={
                                  restoringVersionId !== null ||
                                  !version.zones_snapshot ||
                                  !version.passages_snapshot ||
                                  !canEdit
                                }
                                className="flex items-center gap-1.5 text-xs text-ocean-600 hover:text-ocean-500 transition-colors disabled:opacity-50 focus-visible:outline focus-visible:outline-2 focus-visible:outline-ocean-500"
                                title={
                                  !canEdit
                                    ? READ_ONLY_HINT
                                    : !version.zones_snapshot || !version.passages_snapshot
                                      ? 'Kein Geometrie-Snapshot — nicht wiederherstellbar'
                                      : 'Diesen Stand wirklich wiederherstellen (aktueller Stand wird als Version gesichert)'
                                }
                              >
                                {restoringVersionId === version.id ? (
                                  <Loader2 className="w-3.5 h-3.5 animate-spin" />
                                ) : (
                                  <RotateCcw className="w-3.5 h-3.5" />
                                )}
                                Wiederherstellen
                              </button>
                            </div>
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

      {/* Share dialog (owner only) */}
      {shareDialogOpen && (
        <ShareDialog
          projectId={projectId}
          projectName={project.name}
          onClose={() => setShareDialogOpen(false)}
        />
      )}
    </div>
  )
}
