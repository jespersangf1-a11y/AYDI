import { Component, type ReactNode } from 'react'
import { AlertTriangle, RotateCcw } from 'lucide-react'

interface ErrorBoundaryProps {
  children: ReactNode
  fallbackTitle?: string
}

interface ErrorBoundaryState {
  hasError: boolean
  error: Error | null
}

export default class ErrorBoundary extends Component<ErrorBoundaryProps, ErrorBoundaryState> {
  constructor(props: ErrorBoundaryProps) {
    super(props)
    this.state = { hasError: false, error: null }
  }

  static getDerivedStateFromError(error: Error): ErrorBoundaryState {
    return { hasError: true, error }
  }

  componentDidCatch(error: Error, errorInfo: React.ErrorInfo): void {
    console.error('[ErrorBoundary]', error, errorInfo)
  }

  handleReset = () => {
    this.setState({ hasError: false, error: null })
  }

  render() {
    if (this.state.hasError) {
      return (
        <div className="flex flex-col items-center justify-center min-h-[200px] p-8">
          <div className="card-premium border-red-500/30 bg-red-500/5 p-8 text-center max-w-md">
            <AlertTriangle className="w-10 h-10 text-red-400 mx-auto mb-4" />
            <h3 className="font-serif text-lg font-medium text-navy-900 mb-2">
              {this.props.fallbackTitle ?? 'Ein Fehler ist aufgetreten'}
            </h3>
            <p className="text-sm text-navy-600 mb-6">
              {this.state.error?.message ?? 'Die Komponente konnte nicht gerendert werden.'}
            </p>
            <button
              onClick={this.handleReset}
              className="inline-flex items-center gap-2 text-sm font-medium text-ocean-600 hover:text-ocean-500 transition-colors"
            >
              <RotateCcw className="w-4 h-4" />
              Erneut versuchen
            </button>
          </div>
        </div>
      )
    }

    return this.props.children
  }
}
