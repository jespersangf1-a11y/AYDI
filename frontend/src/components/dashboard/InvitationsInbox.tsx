import { useCallback, useEffect, useState } from 'react'
import { Check, Loader2, Mail, X } from 'lucide-react'
import { acceptInvitation, declineInvitation, getMyInvitations } from '../../services/api'
import type { Invitation } from '../../types'

interface InvitationsInboxProps {
  /** Called after an invite is accepted so the parent can refresh its lists. */
  onChanged?: () => void
}

const ROLE_LABELS: Record<string, string> = {
  owner: 'Eigentümer',
  admin: 'Administrator',
  editor: 'Bearbeiten',
  viewer: 'Nur Lesen',
  member: 'Mitglied',
}

/**
 * Pillar 4, stage 2: the recipient's pending invitations. Rendered as a banner
 * on the projects dashboard; hides itself when there is nothing pending.
 */
export default function InvitationsInbox({ onChanged }: InvitationsInboxProps) {
  const [invitations, setInvitations] = useState<Invitation[]>([])
  const [loading, setLoading] = useState(true)
  const [busyId, setBusyId] = useState<string | null>(null)
  const [error, setError] = useState<string | null>(null)

  const reload = useCallback(async () => {
    setLoading(true)
    try {
      setInvitations(await getMyInvitations())
    } catch {
      // Silent: a failed inbox load must not block the dashboard.
      setInvitations([])
    } finally {
      setLoading(false)
    }
  }, [])

  useEffect(() => {
    reload()
  }, [reload])

  const handleAccept = async (inv: Invitation) => {
    setBusyId(inv.id)
    setError(null)
    try {
      await acceptInvitation(inv.id)
      setInvitations((prev) => prev.filter((i) => i.id !== inv.id))
      onChanged?.()
    } catch (e) {
      setError(e instanceof Error ? e.message : 'Annehmen fehlgeschlagen')
    } finally {
      setBusyId(null)
    }
  }

  const handleDecline = async (inv: Invitation) => {
    setBusyId(inv.id)
    setError(null)
    try {
      await declineInvitation(inv.id)
      setInvitations((prev) => prev.filter((i) => i.id !== inv.id))
    } catch (e) {
      setError(e instanceof Error ? e.message : 'Ablehnen fehlgeschlagen')
    } finally {
      setBusyId(null)
    }
  }

  if (loading || invitations.length === 0) return null

  return (
    <div className="card-premium px-6 py-5 mb-8 border-ocean-300 bg-ocean-50/40">
      <p className="label-premium mb-3 flex items-center gap-2">
        <Mail className="w-4 h-4 text-ocean-600" />
        Einladungen ({invitations.length})
      </p>
      {error && (
        <div className="border-l-4 border-amber-400 bg-amber-50 rounded-r px-3 py-2 text-xs text-amber-900 mb-3">
          {error}
        </div>
      )}
      <ul className="space-y-2">
        {invitations.map((inv) => (
          <li
            key={inv.id}
            className="flex items-center justify-between gap-3 rounded-lg border border-sand-200 bg-white px-4 py-3 text-sm"
          >
            <div className="min-w-0">
              <p className="text-navy-900">
                {inv.scope === 'org' ? 'Organisation' : 'Projekt'}:{' '}
                <span className="font-medium">{inv.target_name ?? '—'}</span>
              </p>
              <p className="text-xs text-navy-600">
                Rolle: {ROLE_LABELS[inv.role] ?? inv.role}
                {inv.invited_by_email ? ` · von ${inv.invited_by_email}` : ''}
              </p>
            </div>
            <div className="flex items-center gap-2 flex-shrink-0">
              <button
                onClick={() => handleAccept(inv)}
                disabled={busyId !== null}
                className="flex items-center gap-1.5 bg-ocean-700 hover:bg-ocean-600 disabled:opacity-50 text-navy-900 px-3 py-1.5 rounded-lg text-xs font-medium transition-all"
              >
                {busyId === inv.id ? <Loader2 className="w-3.5 h-3.5 animate-spin" /> : <Check className="w-3.5 h-3.5" />}
                Annehmen
              </button>
              <button
                onClick={() => handleDecline(inv)}
                disabled={busyId !== null}
                aria-label="Einladung ablehnen"
                className="flex items-center gap-1.5 border border-sand-300 hover:bg-sand-100 disabled:opacity-50 text-navy-700 px-3 py-1.5 rounded-lg text-xs font-medium transition-all"
              >
                <X className="w-3.5 h-3.5" />
                Ablehnen
              </button>
            </div>
          </li>
        ))}
      </ul>
    </div>
  )
}
