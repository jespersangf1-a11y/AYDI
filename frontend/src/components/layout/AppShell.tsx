import { useState, useEffect } from 'react'
import {
  Anchor,
  BarChart3,
  Plus,
  Zap,
  Wrench,
  Package,
  Camera,
  ChevronRight,
  Menu,
  X,
  BookOpen,
} from 'lucide-react'

interface AppShellProps {
  currentView: string
  onNavigate: (view: string) => void
  children: React.ReactNode
  breadcrumbs?: Array<{ label: string; onClick?: () => void }>
}

export default function AppShell({ currentView, onNavigate, children, breadcrumbs }: AppShellProps) {
  const [sidebarCollapsed, setSidebarCollapsed] = useState(false)
  const [isMobile, setIsMobile] = useState(window.innerWidth < 768)

  // Handle window resize for mobile detection
  useEffect(() => {
    const handleResize = () => {
      setIsMobile(window.innerWidth < 768)
    }
    window.addEventListener('resize', handleResize)
    return () => window.removeEventListener('resize', handleResize)
  }, [])

  const navItems = [
    { id: 'quick-analysis', label: 'Schnellanalyse', icon: Zap },
    { id: 'dashboard', label: 'Projekte', icon: BarChart3 },
    { id: 'project-create', label: 'Neues Projekt', icon: Plus },
    { id: 'materials', label: 'Materialien', icon: Package },
    { id: 'knowledge', label: 'Wissen', icon: BookOpen },
    { id: 'service-reports', label: 'Serviceberichte', icon: Wrench },
    { id: 'image-analysis', label: 'Bildanalyse', icon: Camera },
  ]

  return (
    <div className="flex h-screen bg-slate-950">
      {/* Sidebar - Hidden on mobile */}
      {!isMobile && (
      <aside
        className={`${
          sidebarCollapsed ? 'w-[72px]' : 'w-64'
        } bg-navy-950/80 backdrop-blur-md border-r border-navy-800/30 flex flex-col transition-all duration-300`}
      >
        {/* Logo */}
        <div className="px-5 py-6 border-b border-navy-800/30">
          <div className="flex items-center gap-3">
            <div className="w-9 h-9 rounded-lg bg-ocean-800/40 flex items-center justify-center flex-shrink-0">
              <Anchor className="w-5 h-5 text-ocean-400" strokeWidth={1.5} />
            </div>
            {!sidebarCollapsed && (
              <div className="animate-fade-in transition-opacity duration-200">
                <h1 className="font-serif text-lg font-medium text-white tracking-wide-premium">
                  AYDI
                </h1>
                <p className="text-[10px] font-sans font-medium tracking-wider-premium uppercase text-navy-500">
                  Yacht Design Intelligence
                </p>
              </div>
            )}
          </div>
        </div>

        {/* Collapse toggle */}
        <button
          onClick={() => setSidebarCollapsed(!sidebarCollapsed)}
          className="mx-3 mt-4 mb-2 p-2 rounded-lg text-navy-500 hover:text-navy-300 hover:bg-navy-800/30 transition-colors self-end"
          aria-label={sidebarCollapsed ? 'Sidebar erweitern' : 'Sidebar minimieren'}
        >
          {sidebarCollapsed ? <Menu className="w-4 h-4" /> : <X className="w-4 h-4" />}
        </button>

        {/* Navigation */}
        <nav className="flex-1 px-3 space-y-0.5 overflow-y-auto">
          {navItems.map((item) => {
            const Icon = item.icon
            const active = currentView === item.id
            return (
              <button
                key={item.id}
                onClick={() => onNavigate(item.id)}
                aria-label={item.label}
                aria-current={active ? 'page' : undefined}
                title={sidebarCollapsed ? item.label : undefined}
                className={`w-full flex items-center gap-3 px-3 py-2.5 rounded-lg text-[13px] font-sans font-medium relative group transition-all duration-200 hover:scale-[1.02] ${
                  active
                    ? 'bg-ocean-900/30 text-ocean-300'
                    : 'text-navy-400 hover:text-ocean-400'
                }`}
              >
                {/* Active indicator - left border animation */}
                {active && (
                  <div className="absolute left-0 top-0 bottom-0 w-[3px] bg-ocean-400 rounded-r-sm" />
                )}
                <Icon className={`w-[18px] h-[18px] flex-shrink-0 transition-colors duration-200 ${
                  active ? 'text-ocean-400' : 'group-hover:text-ocean-400'
                }`} strokeWidth={1.5} />
                {!sidebarCollapsed && (
                  <span className="transition-all duration-200">{item.label}</span>
                )}
              </button>
            )
          })}
        </nav>

        {/* Version info at bottom */}
        {!sidebarCollapsed && (
          <div className="px-5 py-4 border-t border-navy-800/30 transition-opacity duration-200">
            <p className="text-[10px] font-sans text-navy-600 tracking-wide-premium">
              v0.9.0 Preview
            </p>
          </div>
        )}
      </aside>
      )}

      {/* Mobile Bottom Navigation Bar */}
      {isMobile && (
        <div className="fixed bottom-0 left-0 right-0 z-50">
          <nav className="bg-navy-950/90 backdrop-blur-lg border-t border-navy-800/30 flex justify-around items-end pb-safe">
            {navItems.map((item) => {
              const Icon = item.icon
              const active = currentView === item.id
              return (
                <button
                  key={item.id}
                  onClick={() => onNavigate(item.id)}
                  aria-label={item.label}
                  aria-current={active ? 'page' : undefined}
                  className={`flex flex-col items-center justify-center py-3 px-2 transition-all duration-200 ${
                    active ? 'text-ocean-400' : 'text-navy-400'
                  }`}
                >
                  <Icon className={`w-5 h-5 mb-1 transition-colors duration-200 ${
                    active ? 'text-ocean-400' : ''
                  }`} strokeWidth={1.5} />
                  <span className={`text-[10px] font-sans font-medium tracking-wide transition-colors duration-200 ${
                    active ? 'text-ocean-400' : 'text-navy-500'
                  }`}>
                    {item.label.split(' ')[0]}
                  </span>
                </button>
              )
            })}
          </nav>
        </div>
      )}

      {/* Main Content */}
      <main className={`flex-1 overflow-auto bg-slate-950 flex flex-col ${isMobile ? 'pb-24' : ''}`}>
        {/* Breadcrumb Navigation */}
        {breadcrumbs && breadcrumbs.length > 0 && (
          <div className="bg-navy-950/60 backdrop-blur-sm border-b border-navy-800/20 px-6 md:px-10 py-3 flex items-center gap-2 animate-fade-in">
            <button
              onClick={() => onNavigate('dashboard')}
              className="text-[13px] font-sans text-ocean-500 hover:text-ocean-400 transition-colors duration-200"
            >
              Dashboard
            </button>
            {breadcrumbs.map((crumb, index) => (
              <div key={index} className="flex items-center gap-2">
                <ChevronRight className="w-3.5 h-3.5 text-navy-600 flex-shrink-0" strokeWidth={1.5} />
                {crumb.onClick ? (
                  <button
                    onClick={crumb.onClick}
                    className="text-[13px] font-sans text-ocean-500 hover:text-ocean-400 transition-colors duration-200"
                  >
                    {crumb.label}
                  </button>
                ) : (
                  <span className="text-[13px] font-sans font-medium text-navy-300">{crumb.label}</span>
                )}
              </div>
            ))}
          </div>
        )}
        <div className="flex-1 overflow-auto">{children}</div>
      </main>
    </div>
  )
}
