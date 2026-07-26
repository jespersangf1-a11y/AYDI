import { useCallback, useEffect, useState } from 'react'
import { Loader2, MailPlus, Trash2, Users, X } from 'lucide-react'
import {
  createProjectInvitation,
  getProjectInvitations,
  getProjectMembers,
  removeProjectMember,
  revokeProjectInvitation,
  updateProjectMemberRole,
} from '../../services/api'
import type { Invitation, ProjectMemberEntry } from '../../types'

interface ShareDialogProps {
  projectId: string
  projectName: string
  onClose: () => void
}

const ROLE_LABELS: Record<string, string> = {
  owner: 'Eigentümer',
  editor: 'Bearbeiten',
  viewer: 'Nur Lesen',
}

/**
 * Pillar 4: share a project. Stage 2 uses the INVITATION flow (no direct add):
 * an invite reveals nothing about whether the email has an account and takes
 * effect only when the recipient accepts it under "Einladungen". Owner-only —
 * the button is only rendered for access_role === 'owner', server-enforced.
 */
export default function ShareDialog({ projectId, projectName, onClose }: ShareDialogProps) {
  const [members, setMembers] = useState<ProjectMemberEntry[]>([])
  const [invitations, setInvitations] = useState<Invitation[]>([])
  const [loading, setLoading] = useState(true)
  const [error, setError] = useState<string | null>(null)
  const [notice, setNotice] = useState<string | null>(null)
  const [email, setEmail] = useState('')
  const [role, setRole] = useState<'viewer' | 'editor'>('viewer')
  const [inviting, setInviting] = useState(false)
  const [removingId, setRemovingId] = useState<string | null>(null)
  const [revokingId, setRevokingId] = useState<string | null>(null)
  const [changingRoleId, setChangingRoleId] = useState<string | null>(null)

  const reload = useCallback(async () => {
    setLoading(true)
    setError(null)
    try {
      const [mem, inv] = await Promise.all([
        getProjectMembers(projectId),
        getProjectInvitations(projectId),
      ])
      setMembers(mem)
      setInvitations(inv)
    } catch (e) {
      setError(e instanceof Error ? e.message : 'Daten konnten nicht geladen werden')
    } finally {
      setLoading(false)
    }
  }, [projectId])

  useEffect(() => {
    reload()
  }, [reload])

  useEffect(() => {
    const onKey = (e: KeyboardEvent) => {
      if (e.key === 'Escape') onClose()
    }
    window.document.addEventListener('keydown', onKey)
    return () => window.document.removeEventListener('keydown', onKey)
  }, [onClose])

  const handleInvite = async (e: React.FormEvent) => {
    e.preventDefault()
    if (!email.trim()) return
    setInviting(true)
    setError(null)
    setNotice(null)
    try {
      const created = await createProjectInvitation(projectId, email.trim(), role)
      setInvitations((prev) => [created, ...prev])
      setNotice(
        `Einladung für ${created.email} erstellt. Es wird keine E-Mail ` +
          'versendet — sie erscheint nach Anmeldung/Registrierung unter „Einladungen".'
      )
      setEmail('')
    } catch (err) {
      setError(err instanceof Error ? err.message : 'Einladung fehlgeschlagen')
    } finally {
      setInviting(false)
    }
  }

  const handleRoleChange = async (
    member: ProjectMemberEntry,
    newRole: 'viewer' | 'editor'
  ) => {
    if (newRole === member.role) return
    setChangingRoleId(member.user_id)
    setError(null)
    try {
      const updated = await updateProjectMemberRole(projectId, member.user_id, newRole)
      setMembers((prev) =>
        prev.map((m) => (m.user_id === member.user_id ? updated : m))
      )
    } catch (err) {
      setError(err instanceof Error ? err.message : 'Rollenänderung fehlgeschlagen')
    } finally {
      setChangingRoleId(null)
    }
  }

  const handleRemove = async (member: ProjectMemberEntry) => {
    if (!window.confirm(`Zugriff von ${member.email} entfernen?`)) return
    setRemovingId(member.user_id)
    setError(null)
    try {
      await removeProjectMember(projectId, member.user_id)
      setMembers((prev) => prev.filter((m) => m.user_id !== member.user_id))
    } catch (err) {
      setError(err instanceof Error ? err.message : 'Entfernen fehlgeschlagen')
    } finally {
      setRemovingId(null)
    }
  }

  const handleRevoke = async (inv: Invitation) => {
    setRevokingId(inv.id)
    setError(null)
    try {
      await revokeProjectInvitation(projectId, inv.id)
      setInvitations((prev) => prev.filter((i) => i.id !== inv.id))
    } catch (err) {
      setError(err instanceof Error ? err.message : 'Zurückziehen fehlgeschlagen')
    } finally {
      setRevokingId(null)
    }
  }

  return (
    <div
      className="fixed inset-0 z-50 bg-navy-950/70 backdrop-blur-sm flex items-start justify-center overflow-y-auto"
      role="dialog"
      aria-modal="true"
      aria-label={`Projekt '${projectName}' teilen`}
      onMouseDown={(e) => {
        if (e.target === e.currentTarget) onClose()
      }}
    >
      <div className="w-full max-w-lg mx-4 my-16 bg-white rounded-xl shadow-2xl">
        {/* Header */}
        <div className="flex items-start justify-between gap-4 px-6 py-5 border-b border-sand-200">
          <div>
            <p className="text-xs font-medium text-ocean-600 uppercase tracking-wide mb-1">
              Projekt teilen
            </p>
            <h2 className="font-serif text-lg font-medium text-navy-900">{projectName}</h2>
          </div>
          <button
            onClick={onClose}
            aria-label="Dialog schließen"
            className="p-2 rounded-lg text-navy-600 hover:text-navy-900 hover:bg-sand-100 transition-colors"
          >
            <X className="w-5 h-5" />
          </button>
        </div>

        <div className="px-6 py-5 space-y-5">
          {error && (
            <div className="border-l-4 border-amber-400 bg-amber-50 rounded-r px-3 py-2 text-xs text-amber-900">
              {error}
            </div>
          )}
          {notice && (
            <div className="border-l-4 border-ocean-400 bg-ocean-50 rounded-r px-3 py-2 text-xs text-ocean-900">
              {notice}
            </div>
          )}

          {/* Invite by email */}
          <form onSubmit={handleInvite} className="flex flex-wrap items-end gap-3">
            <div className="flex-1 min-w-[180px]">
              <label htmlFor="share-email" className="label-premium mb-2 block">
                Per E-Mail einladen
              </label>
              <input
                id="share-email"
                type="email"
                value={email}
                onChange={(e) => setEmail(e.target.value)}
                placeholder="name@werft.de"
                className="w-full rounded-lg border border-sand-200 bg-white px-3 py-2 text-sm text-navy-900 focus:border-ocean-500 focus:outline-none"
              />
            </div>
            <div>
              <label htmlFor="share-role" className="label-premium mb-2 block">Rolle</label>
              <select
                id="share-role"
                value={role}
                onChange={(e) => setRole(e.target.value as 'viewer' | 'editor')}
                className="rounded-lg border border-sand-200 bg-white px-3 py-2 text-sm text-navy-900 focus:border-ocean-500 focus:outline-none"
              >
                <option value="viewer">Nur Lesen</option>
                <option value="editor">Bearbeiten</option>
              </select>
            </div>
            <button
              type="submit"
              disabled={inviting || !email.trim()}
              className="flex items-center gap-2 bg-ocean-700 hover:bg-ocean-600 disabled:opacity-50 text-navy-900 px-4 py-2 rounded-lg text-sm font-medium transition-all"
            >
              {inviting ? <Loader2 className="w-4 h-4 animate-spin" /> : <MailPlus className="w-4 h-4" />}
              Einladen
            </button>
          </form>

          {loading ? (
            <div className="flex items-center gap-2 text-navy-600 text-sm py-4">
              <Loader2 className="w-4 h-4 animate-spin" />
              Lade...
            </div>
          ) : (
            <>
              {/* Members */}
              <div>
                <p className="label-premium mb-3 flex items-center gap-2">
                  <Users className="w-3.5 h-3.5" />
                  Zugriff ({members.length})
                </p>
                <ul className="space-y-2">
                  {members.map((member) => (
                    <li
                      key={member.user_id}
                      className="flex items-center justify-between gap-3 rounded-lg border border-sand-200 px-4 py-2.5 text-sm"
                    >
                      <div className="min-w-0">
                        <p className="text-navy-900 truncate">{member.full_name}</p>
                        <p className="text-xs text-navy-600 truncate">{member.email}</p>
                      </div>
                      <div className="flex items-center gap-3 flex-shrink-0">
                        {member.role === 'owner' ? (
                          <span className="text-xs px-2.5 py-1 rounded-full border bg-ocean-100 text-ocean-700 border-ocean-300">
                            {ROLE_LABELS.owner}
                          </span>
                        ) : (
                          <select
                            value={member.role}
                            onChange={(e) =>
                              handleRoleChange(member, e.target.value as 'viewer' | 'editor')
                            }
                            disabled={changingRoleId !== null}
                            aria-label={`Rolle von ${member.email} ändern`}
                            className={`text-xs px-2 py-1 rounded-lg border bg-white focus:border-ocean-500 focus:outline-none disabled:opacity-50 ${
                              member.role === 'editor'
                                ? 'text-emerald-700 border-emerald-300'
                                : 'text-navy-700 border-sand-300'
                            }`}
                          >
                            <option value="viewer">Nur Lesen</option>
                            <option value="editor">Bearbeiten</option>
                          </select>
                        )}
                        {member.role !== 'owner' && (
                          <button
                            onClick={() => handleRemove(member)}
                            disabled={removingId !== null}
                            aria-label={`Zugriff von ${member.email} entfernen`}
                            className="p-1.5 rounded text-navy-500 hover:text-red-600 hover:bg-red-50 transition-colors disabled:opacity-50"
                          >
                            {removingId === member.user_id ? (
                              <Loader2 className="w-4 h-4 animate-spin" />
                            ) : (
                              <Trash2 className="w-4 h-4" />
                            )}
                          </button>
                        )}
                      </div>
                    </li>
                  ))}
                </ul>
              </div>

              {/* Pending invitations */}
              {invitations.length > 0 && (
                <div>
                  <p className="label-premium mb-3">Ausstehende Einladungen ({invitations.length})</p>
                  <ul className="space-y-2">
                    {invitations.map((inv) => (
                      <li
                        key={inv.id}
                        className="flex items-center justify-between gap-3 rounded-lg border border-dashed border-sand-300 px-4 py-2.5 text-sm"
                      >
                        <div className="min-w-0">
                          <p className="text-navy-800 truncate">{inv.email}</p>
                          <p className="text-xs text-navy-500">
                            {ROLE_LABELS[inv.role] ?? inv.role} · ausstehend
                          </p>
                        </div>
                        <button
                          onClick={() => handleRevoke(inv)}
                          disabled={revokingId !== null}
                          aria-label={`Einladung für ${inv.email} zurückziehen`}
                          className="p-1.5 rounded text-navy-500 hover:text-red-600 hover:bg-red-50 transition-colors disabled:opacity-50"
                        >
                          {revokingId === inv.id ? (
                            <Loader2 className="w-4 h-4 animate-spin" />
                          ) : (
                            <Trash2 className="w-4 h-4" />
                          )}
                        </button>
                      </li>
                    ))}
                  </ul>
                </div>
              )}
            </>
          )}

          <p className="text-xs text-navy-500">
            „Nur Lesen" kann Projekt und Analysen ansehen; „Bearbeiten" kann
            Projektdaten, Layouts, Materialien und Analysen ändern. Löschen und
            Teilen bleiben dem Eigentümer vorbehalten. Es wird keine E-Mail
            versendet — Eingeladene sehen die Einladung nach der Anmeldung unter
            „Einladungen". Geteilte Nutzer können der Live-Kollaboration
            beitreten (erfordert PRO-Tarif; „Nur Lesen" dort ohne Schreibrechte).
          </p>
        </div>
      </div>
    </div>
  )
}
