import { useCallback, useEffect, useState } from 'react'
import {
  BrowserRouter,
  Navigate,
  Route,
  Routes,
  useLocation,
  useNavigate,
  useParams,
} from 'react-router-dom'

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
import OrganizationsPage from './components/organizations/OrganizationsPage'
import AuthPage from './components/auth/AuthPage'
import ErrorBoundary from './components/layout/ErrorBoundary'

const VIEW_ROUTES: Record<string, string> = {
  'quick-analysis': '/',
  dashboard: '/projects',
  'project-create': '/projects/new',
  'project-detail': '/projects',
  materials: '/materials',
  'service-reports': '/service-reports',
  'image-analysis': '/image-analysis',
  knowledge: '/knowledge',
  organizations: '/organizations',
}

const AUTH_REQUIRED_VIEWS = new Set<string>([
  'dashboard',
  'project-detail',
  'project-create',
  'service-reports',
  'organizations',
])

function pathToViewId(pathname: string): string {
  if (pathname.startsWith('/projects/new')) return 'project-create'
  if (pathname.startsWith('/projects/')) return 'project-detail'
  if (pathname.startsWith('/projects')) return 'dashboard'
  if (pathname.startsWith('/materials')) return 'materials'
  if (pathname.startsWith('/service-reports')) return 'service-reports'
  if (pathname.startsWith('/image-analysis')) return 'image-analysis'
  if (pathname.startsWith('/knowledge')) return 'knowledge'
  if (pathname.startsWith('/organizations')) return 'organizations'
  return 'quick-analysis'
}

interface ProtectedRouteProps {
  authToken: string | null
  children: React.ReactNode
}

function ProtectedRoute({ authToken, children }: ProtectedRouteProps) {
  const location = useLocation()
  if (!authToken) {
    return (
      <Navigate
        to="/login"
        replace
        state={{ from: location.pathname + location.search }}
      />
    )
  }
  return <>{children}</>
}

function ProjectDetailRoute() {
  const { id } = useParams<{ id: string }>()
  const navigate = useNavigate()
  if (!id) return <Navigate to="/projects" replace />
  return <ProjectDetail projectId={id} onBack={() => navigate('/projects')} />
}

function ProjectCreateRoute() {
  const navigate = useNavigate()
  return (
    <ProjectCreate
      onCreated={(id) => navigate(`/projects/${id}`)}
      onCancel={() => navigate('/projects')}
    />
  )
}

function DashboardRoute() {
  const navigate = useNavigate()
  return <Dashboard onSelectProject={(id) => navigate(`/projects/${id}`)} />
}

function ShellRoutes() {
  const location = useLocation()
  const navigate = useNavigate()
  const [authToken, setAuthTokenState] = useState<string | null>(() => getAuthToken())
  const [displayKey, setDisplayKey] = useState<string>(location.pathname)
  const [transitioning, setTransitioning] = useState<boolean>(false)

  useEffect(() => {
    if (location.pathname !== displayKey) {
      setTransitioning(true)
      const timer = setTimeout(() => {
        setDisplayKey(location.pathname)
        setTransitioning(false)
      }, 150)
      return () => clearTimeout(timer)
    }
  }, [location.pathname, displayKey])

  const currentView = pathToViewId(location.pathname)

  const handleNavigate = useCallback(
    (target: string) => {
      const path = VIEW_ROUTES[target]
      if (!path) return
      if (AUTH_REQUIRED_VIEWS.has(target) && !authToken) {
        navigate('/login', { state: { from: path } })
        return
      }
      navigate(path)
    },
    [authToken, navigate],
  )

  const handleAuthenticated = useCallback(
    (token: string) => {
      setAuthTokenState(token)
      const from = (location.state as { from?: string } | null)?.from
      navigate(from && from !== '/login' ? from : '/projects', { replace: true })
    },
    [navigate, location.state],
  )

  const handleSkipAuth = useCallback(() => {
    navigate('/', { replace: true })
  }, [navigate])

  if (location.pathname === '/login') {
    return <AuthPage onAuthenticated={handleAuthenticated} onSkip={handleSkipAuth} />
  }

  return (
    <AppShell
      currentView={currentView}
      onNavigate={handleNavigate}
      isAuthenticated={!!authToken}
      onLogin={() => navigate('/login')}
      onLogout={() => {
        clearAuthToken()
        setAuthTokenState(null)
        navigate('/', { replace: true })
      }}
    >
      <ErrorBoundary fallbackTitle="Anzeigefehler">
        <div
          className={`transition-opacity ${
            transitioning ? 'opacity-0 duration-150' : 'opacity-100 duration-300'
          }`}
        >
          <Routes>
            <Route path="/" element={<QuickAnalysis />} />
            <Route
              path="/projects"
              element={
                <ProtectedRoute authToken={authToken}>
                  <DashboardRoute />
                </ProtectedRoute>
              }
            />
            <Route
              path="/projects/new"
              element={
                <ProtectedRoute authToken={authToken}>
                  <ProjectCreateRoute />
                </ProtectedRoute>
              }
            />
            <Route
              path="/projects/:id/*"
              element={
                <ProtectedRoute authToken={authToken}>
                  <ProjectDetailRoute />
                </ProtectedRoute>
              }
            />
            <Route
              path="/organizations"
              element={
                <ProtectedRoute authToken={authToken}>
                  <OrganizationsPage />
                </ProtectedRoute>
              }
            />
            <Route path="/materials" element={<MaterialBrowser />} />
            <Route
              path="/service-reports"
              element={
                <ProtectedRoute authToken={authToken}>
                  <ServiceReportList />
                </ProtectedRoute>
              }
            />
            <Route path="/image-analysis" element={<ImageUpload boatClass="cruising_sail" />} />
            <Route path="/knowledge" element={<KnowledgePage />} />
            <Route path="*" element={<Navigate to="/" replace />} />
          </Routes>
        </div>
      </ErrorBoundary>
    </AppShell>
  )
}

export default function App() {
  return (
    <BrowserRouter>
      <ShellRoutes />
    </BrowserRouter>
  )
}
