import { useState } from 'react'
import { Anchor, Mail, Lock, User, ArrowRight, Loader2, AlertCircle } from 'lucide-react'
import { login, register } from '../../services/api'

interface AuthPageProps {
  onAuthenticated: (token: string) => void
  onSkip: () => void
}

type AuthMode = 'login' | 'register'

export default function AuthPage({ onAuthenticated, onSkip }: AuthPageProps) {
  const [mode, setMode] = useState<AuthMode>('login')
  const [email, setEmail] = useState('')
  const [password, setPassword] = useState('')
  const [fullName, setFullName] = useState('')
  const [loading, setLoading] = useState(false)
  const [error, setError] = useState<string | null>(null)

  const handleSubmit = async (e: React.FormEvent) => {
    e.preventDefault()
    setLoading(true)
    setError(null)

    // Client-side validation
    if (!email.includes('@') || !email.includes('.')) {
      setError('Bitte geben Sie eine gültige E-Mail-Adresse ein.')
      setLoading(false)
      return
    }
    if (password.length < 8) {
      setError('Das Passwort muss mindestens 8 Zeichen lang sein.')
      setLoading(false)
      return
    }
    if (mode === 'register' && fullName.trim().length < 2) {
      setError('Bitte geben Sie Ihren vollständigen Namen ein.')
      setLoading(false)
      return
    }

    try {
      if (mode === 'login') {
        const result = await login(email, password)
        onAuthenticated(result.access_token)
      } else {
        await register(email, password, fullName)
        // Auto-login after registration
        const result = await login(email, password)
        onAuthenticated(result.access_token)
      }
    } catch (e) {
      setError(e instanceof Error ? e.message : 'Ein Fehler ist aufgetreten')
    } finally {
      setLoading(false)
    }
  }

  return (
    <div className="min-h-screen bg-sand-50 flex flex-col items-center justify-center px-4">
      {/* Background pattern */}
      <div className="absolute inset-0 overflow-hidden pointer-events-none">
        <div className="absolute top-0 right-0 w-[600px] h-[600px] bg-ocean-100/30 rounded-full blur-3xl -translate-y-1/2 translate-x-1/4" />
        <div className="absolute bottom-0 left-0 w-[400px] h-[400px] bg-ocean-100/20 rounded-full blur-3xl translate-y-1/3 -translate-x-1/4" />
      </div>

      <div className="relative w-full max-w-md">
        {/* Logo */}
        <div className="text-center mb-10">
          <div className="inline-flex items-center justify-center w-16 h-16 rounded-2xl bg-white border border-sand-200 shadow-lg shadow-ocean-100/30 mb-6">
            <Anchor className="w-8 h-8 text-ocean-600" strokeWidth={1.5} />
          </div>
          <h1 className="font-serif text-3xl font-medium text-navy-900 tracking-[0.12em] mb-2">
            AYDI
          </h1>
          <p className="text-sm text-navy-600">
            AI Yacht Design Intelligence
          </p>
        </div>

        {/* Auth Card */}
        <div className="bg-white rounded-2xl border border-sand-200 shadow-xl shadow-navy-100/10 p-8">
          {/* Mode Toggle */}
          <div className="flex gap-1 bg-sand-100 rounded-lg p-1 mb-8">
            <button
              onClick={() => { setMode('login'); setError(null) }}
              className={`flex-1 py-2.5 rounded-lg text-sm font-medium transition-all duration-200 ${
                mode === 'login'
                  ? 'bg-white text-navy-900 shadow-sm'
                  : 'text-navy-600 hover:text-navy-700'
              }`}
            >
              Anmelden
            </button>
            <button
              onClick={() => { setMode('register'); setError(null) }}
              className={`flex-1 py-2.5 rounded-lg text-sm font-medium transition-all duration-200 ${
                mode === 'register'
                  ? 'bg-white text-navy-900 shadow-sm'
                  : 'text-navy-600 hover:text-navy-700'
              }`}
            >
              Registrieren
            </button>
          </div>

          {/* Error message */}
          {error && (
            <div className="flex items-start gap-2 rounded-lg bg-red-50 border border-red-200 px-4 py-3 mb-6">
              <AlertCircle className="w-4 h-4 text-red-500 flex-shrink-0 mt-0.5" />
              <p className="text-sm text-red-700">{error}</p>
            </div>
          )}

          {/* Form */}
          <form onSubmit={handleSubmit} className="space-y-5">
            {mode === 'register' && (
              <div>
                <label className="block text-xs font-sans font-semibold uppercase tracking-wider text-navy-600 mb-2">
                  Vollständiger Name
                </label>
                <div className="relative">
                  <User className="absolute left-3.5 top-1/2 -translate-y-1/2 w-4 h-4 text-navy-500" />
                  <input
                    type="text"
                    value={fullName}
                    onChange={(e) => setFullName(e.target.value)}
                    placeholder="Max Mustermann"
                    required
                    className="w-full pl-10 pr-4 py-3 rounded-lg border border-sand-200 bg-sand-50/50 text-navy-900 text-sm placeholder:text-navy-500 focus:border-ocean-500 focus:ring-1 focus:ring-ocean-500/30 focus:outline-none transition-all"
                  />
                </div>
              </div>
            )}

            <div>
              <label className="block text-xs font-sans font-semibold uppercase tracking-wider text-navy-600 mb-2">
                E-Mail-Adresse
              </label>
              <div className="relative">
                <Mail className="absolute left-3.5 top-1/2 -translate-y-1/2 w-4 h-4 text-navy-500" />
                <input
                  type="email"
                  value={email}
                  onChange={(e) => setEmail(e.target.value)}
                  placeholder="name@werft.de"
                  required
                  className="w-full pl-10 pr-4 py-3 rounded-lg border border-sand-200 bg-sand-50/50 text-navy-900 text-sm placeholder:text-navy-500 focus:border-ocean-500 focus:ring-1 focus:ring-ocean-500/30 focus:outline-none transition-all"
                />
              </div>
            </div>

            <div>
              <label className="block text-xs font-sans font-semibold uppercase tracking-wider text-navy-600 mb-2">
                Passwort
              </label>
              <div className="relative">
                <Lock className="absolute left-3.5 top-1/2 -translate-y-1/2 w-4 h-4 text-navy-500" />
                <input
                  type="password"
                  value={password}
                  onChange={(e) => setPassword(e.target.value)}
                  placeholder="Mindestens 8 Zeichen"
                  required
                  minLength={8}
                  className="w-full pl-10 pr-4 py-3 rounded-lg border border-sand-200 bg-sand-50/50 text-navy-900 text-sm placeholder:text-navy-500 focus:border-ocean-500 focus:ring-1 focus:ring-ocean-500/30 focus:outline-none transition-all"
                />
              </div>
            </div>

            <button
              type="submit"
              disabled={loading}
              className="w-full flex items-center justify-center gap-2 bg-ocean-600 hover:bg-ocean-500 disabled:opacity-50 disabled:cursor-not-allowed text-white py-3.5 rounded-lg font-medium transition-all duration-200 hover:shadow-lg hover:shadow-ocean-600/30"
            >
              {loading ? (
                <>
                  <Loader2 className="w-4 h-4 animate-spin" />
                  {mode === 'login' ? 'Anmeldung...' : 'Registrierung...'}
                </>
              ) : (
                <>
                  {mode === 'login' ? 'Anmelden' : 'Konto erstellen'}
                  <ArrowRight className="w-4 h-4" />
                </>
              )}
            </button>
          </form>
        </div>

        {/* Skip to Quick Analysis */}
        <div className="text-center mt-6">
          <button
            onClick={onSkip}
            className="text-sm text-navy-600 hover:text-ocean-600 transition-colors font-medium"
          >
            Ohne Anmeldung zur Schnellanalyse
          </button>
          <p className="text-xs text-navy-500 mt-2">
            Level 1: Sofort-Analyse ohne Login verfügbar
          </p>
        </div>
      </div>
    </div>
  )
}
