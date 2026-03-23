import { useState, useEffect } from 'react'
import AppShell from './components/layout/AppShell'
import Dashboard from './components/dashboard/Dashboard'
import ProjectDetail from './components/dashboard/ProjectDetail'
import ProjectCreate from './components/dashboard/ProjectCreate'
import QuickAnalysis from './components/quick/QuickAnalysis'
import MaterialBrowser from './components/materials/MaterialBrowser'
import ServiceReportList from './components/service/ServiceReportList'
import ImageUpload from './components/images/ImageUpload'
import KnowledgePage from './pages/KnowledgePage'

type View =
  | 'quick-analysis'
  | 'dashboard'
  | 'project-detail'
  | 'project-create'
  | 'materials'
  | 'service-reports'
  | 'image-analysis'
  | 'knowledge'

export default function App() {
  const [view, setView] = useState<View>('quick-analysis')
  const [displayView, setDisplayView] = useState<View>(view)
  const [transitioning, setTransitioning] = useState(false)
  const [selectedProjectId, setSelectedProjectId] = useState<string | null>(null)

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

  const handleNavigate = (target: string) => {
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
    if (validViews.includes(target as View)) {
      setView(target as View)
    }
  }

  const handleProjectCreated = (id: string) => {
    setSelectedProjectId(id)
    setView('project-detail')
  }

  return (
    <AppShell currentView={view} onNavigate={handleNavigate}>
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
    </AppShell>
  )
}
