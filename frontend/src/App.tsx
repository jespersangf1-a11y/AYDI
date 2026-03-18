import { useState } from 'react'
import AppShell from './components/layout/AppShell'
import Dashboard from './components/dashboard/Dashboard'
import ProjectDetail from './components/dashboard/ProjectDetail'
import ProjectCreate from './components/dashboard/ProjectCreate'

type View = 'dashboard' | 'project-detail' | 'project-create'

export default function App() {
  const [view, setView] = useState<View>('dashboard')
  const [selectedProjectId, setSelectedProjectId] = useState<string | null>(null)

  const handleSelectProject = (id: string) => {
    setSelectedProjectId(id)
    setView('project-detail')
  }

  const handleNavigate = (target: string) => {
    if (target === 'dashboard' || target === 'project-detail' || target === 'project-create') {
      setView(target)
    }
  }

  const handleProjectCreated = (id: string) => {
    setSelectedProjectId(id)
    setView('project-detail')
  }

  return (
    <AppShell currentView={view} onNavigate={handleNavigate}>
      {view === 'dashboard' && <Dashboard onSelectProject={handleSelectProject} />}
      {view === 'project-detail' && selectedProjectId && (
        <ProjectDetail projectId={selectedProjectId} onBack={() => setView('dashboard')} />
      )}
      {view === 'project-create' && (
        <ProjectCreate onCreated={handleProjectCreated} onCancel={() => setView('dashboard')} />
      )}
    </AppShell>
  )
}
