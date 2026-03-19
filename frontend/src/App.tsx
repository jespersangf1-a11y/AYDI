import { useState } from 'react'
import AppShell from './components/layout/AppShell'
import Dashboard from './components/dashboard/Dashboard'
import ProjectDetail from './components/dashboard/ProjectDetail'
import ProjectCreate from './components/dashboard/ProjectCreate'
import QuickAnalysis from './components/quick/QuickAnalysis'
import MaterialBrowser from './components/materials/MaterialBrowser'
import ServiceReportList from './components/service/ServiceReportList'
import ImageUpload from './components/images/ImageUpload'

type View =
  | 'quick-analysis'
  | 'dashboard'
  | 'project-detail'
  | 'project-create'
  | 'materials'
  | 'service-reports'
  | 'image-analysis'

export default function App() {
  const [view, setView] = useState<View>('quick-analysis')
  const [selectedProjectId, setSelectedProjectId] = useState<string | null>(null)

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
      {view === 'quick-analysis' && <QuickAnalysis />}
      {view === 'dashboard' && <Dashboard onSelectProject={handleSelectProject} />}
      {view === 'project-detail' && selectedProjectId && (
        <ProjectDetail projectId={selectedProjectId} onBack={() => setView('dashboard')} />
      )}
      {view === 'project-create' && (
        <ProjectCreate onCreated={handleProjectCreated} onCancel={() => setView('dashboard')} />
      )}
      {view === 'materials' && <MaterialBrowser />}
      {view === 'service-reports' && <ServiceReportList />}
      {view === 'image-analysis' && <ImageUpload boatClass="cruising_sail" />}
    </AppShell>
  )
}
