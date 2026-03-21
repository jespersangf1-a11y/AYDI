import { Anchor, BarChart3, Plus, Zap, Wrench, Package, Camera, ChevronRight } from 'lucide-react'

interface AppShellProps {
  currentView: string
  onNavigate: (view: string) => void
  children: React.ReactNode
  breadcrumbs?: Array<{ label: string; onClick?: () => void }>
}

export default function AppShell({ currentView, onNavigate, children, breadcrumbs }: AppShellProps) {
  const navItems = [
    { id: 'quick-analysis', label: 'Schnellanalyse', icon: Zap },
    { id: 'dashboard', label: 'Projekte', icon: BarChart3 },
    { id: 'project-create', label: 'Neues Projekt', icon: Plus },
    { id: 'materials', label: 'Materialien', icon: Package },
    { id: 'service-reports', label: 'Serviceberichte', icon: Wrench },
    { id: 'image-analysis', label: 'Bildanalyse', icon: Camera },
  ]

  return (
    <div className="flex h-screen">
      {/* Sidebar */}
      <aside className="w-64 bg-navy-900 border-r border-navy-700 flex flex-col">
        <div className="p-6 border-b border-navy-700">
          <div className="flex items-center gap-3">
            <Anchor className="w-8 h-8 text-ocean-400" />
            <div>
              <h1 className="font-heading text-lg font-bold text-white">AYDI</h1>
              <p className="text-xs text-navy-400">Yacht Design Intelligence</p>
            </div>
          </div>
        </div>
        <nav className="flex-1 p-4 space-y-1">
          {navItems.map((item) => {
            const Icon = item.icon
            const active = currentView === item.id
            return (
              <button
                key={item.id}
                onClick={() => onNavigate(item.id)}
                aria-label={item.label}
                aria-current={active ? 'page' : undefined}
                className={`w-full flex items-center gap-3 px-3 py-2 rounded-lg text-sm transition-colors ${
                  active
                    ? 'bg-ocean-600 text-white'
                    : 'text-navy-300 hover:bg-navy-800 hover:text-white'
                }`}
              >
                <Icon className="w-4 h-4" />
                {item.label}
              </button>
            )
          })}
        </nav>
      </aside>

      {/* Main Content */}
      <main className="flex-1 overflow-auto bg-navy-950 flex flex-col">
        {/* Breadcrumb Navigation */}
        {breadcrumbs && breadcrumbs.length > 0 && (
          <div className="bg-navy-900 border-b border-navy-700 px-8 py-3 flex items-center gap-2">
            <button
              onClick={() => onNavigate('dashboard')}
              className="text-sm text-ocean-400 hover:text-ocean-300 transition-colors"
            >
              Dashboard
            </button>
            {breadcrumbs.map((crumb, index) => (
              <div key={index} className="flex items-center gap-2">
                <ChevronRight className="w-4 h-4 text-navy-500" />
                {crumb.onClick ? (
                  <button
                    onClick={crumb.onClick}
                    className="text-sm text-ocean-400 hover:text-ocean-300 transition-colors"
                  >
                    {crumb.label}
                  </button>
                ) : (
                  <span className="text-sm text-navy-300">{crumb.label}</span>
                )}
              </div>
            ))}
          </div>
        )}
        <div className="flex-1 overflow-auto p-8">{children}</div>
      </main>
    </div>
  )
}
