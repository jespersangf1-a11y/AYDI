import { useState, useEffect, useCallback } from 'react'
import { getAuthToken, clearAuthToken } from './services/api'
import AppShell from './components/layout/AppShell'
import Dashboard from './components/dashboard/Dashboard'
import ProjectDetail from './components/dashboard/ProjectDetail'
import ProjectCreate from './components/dashboard/ProjectCreate'
import QuickAnalysis from './components/quick/QuickAnalysis'
import MaterialBrowser from './components/materials/MaterialBrowser'
import ServiceReportList from './components/service/ServiceReportList'
import ImageUpload from './components/images/ImageUpload'
import KnowledgePage from './pages/KnowledgePage'
import AuthPage from './components/auth/AuthPage'
import ErrorBoundary from './components/layout/ErrorBoundary'

type View =
  | 'quick-analysis'
  | 'dashboard'
  | 'project-detail'
  | 'project-create'
  | 'materials'
  | 'service-reports'
  | 'image-analysis'
  | 'knowledge'

// Views that require authentication (Level 2)
const AUTH_REQUIRED_VIEWS: View[] = [
  'dashboard',
  'project-detail',
  'project-create',
  'service-reports',
]

export default function App() {
  const [view, setView] = useState<View>(() => getAuthToken() ? 'dashboard' : 'quick-analysis')
  const [displayView, setDisplayView] = useState<View>(view)
  const [transitioning, setTransitioning] = useState(false)
  const [selectedProjectId, setSelectedProjectId] = useState<string | null>(null)
  const [authToken, setAuthTokenState] = useState<string | null>(() => getAuthToken())
  const [showAuth, setShowAuth] = useState(false)
  const [pendingView, setPendingView] = useState<View | null>(null)

  useEffect(() => {
    if (view !== displayView) {
      setTransitioning(true)
      const timer = setTimeout(() => {
        setDisplayView(view)
        setTransitioning(false)
      }, 150)
      return () => clearTimeout(timer)
    }
  }, [view, displayView])

  const handleSelectProject = (id: string) => {
    setSelectedProjectId(id)
    setView('project-detail')
  }

  const handleNavigate = useCallback((target: string) => {
    const validViews: View[] = [
      'quick-analysis',
      'dashboard',
      'project-detail',
      'project-create',
      'materials',
      'service-reports',
      'image-analysis',
      'knowledge',
    ]
    if (!validViews.includes(target as View)) return

    const targetView = target as View
    // Check if view requires auth
    if (AUTH_REQUIRED_VIEWS.includes(targetView) && !authToken) {
      setPendingView(targetView)
      setShowAuth(true)
      return
    }
    setView(targetView)
  }, [authToken])

  const handleProjectCreated = (id: string) => {
    setSelectedProjectId(id)
    setView('project-detail')
  }

  const handleAuthenticated = (token: string) => {
    // api.ts login() already stores the token — just sync React state
    setAuthTokenState(token)
    setShowAuth(false)
    if (pendingView) {
      setView(pendingView)
      setPendingView(null)
    } else {
      setView('dashboard')
    }
  }

  const handleSkipAuth = () => {
    setShowAuth(false)
    setPendingView(null)
    setView('quick-analysis')
  }

  // Show auth page when needed
  if (showAuth) {
    return <AuthPage onAuthenticated={handleAuthenticated} onSkip={handleSkipAuth} />
  }

  return (
    <AppShell
      currentView={view}
      onNavigate={handleNavigate}
      isAuthenticated={!!authToken}
      onLogin={() => setShowAuth(true)}
      onLogout={() => { clearAuthToken(); setAuthTokenState(null); setView('quick-analysis') }}
    >
      <ErrorBoundary fallbackTitle="Anzeigefehler">
        <div className={`transition-opacity ${transitioning ? 'opacity-0 duration-150' : 'opacity-100 duration-300'}`}>
          {displayView === 'quick-analysis' && <QuickAnalysis />}
          {displayView === 'dashboard' && <Dashboard onSelectProject={handleSelectProject} />}
          {displayView === 'project-detail' && selectedProjectId && (
            <ProjectDetail projectId={selectedProjectId} onBack={() => setView('dashboard')} />
          )}
          {displayView === 'project-create' && (
            <ProjectCreate onCreated={handleProjectCreated} onCancel={() => setView('dashboard')} />
          )}
          {displayView === 'materials' && <MaterialBrowser />}
          {displayView === 'service-reports' && <ServiceReportList />}
          {displayView === 'image-analysis' && <ImageUpload boatClass="cruising_sail" />}
          {displayView === 'knowledge' && <KnowledgePage />}
        </div>
      </ErrorBoundary>
    </AppShell>
  )
}
