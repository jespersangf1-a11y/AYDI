import { useCallback, useEffect, useState } from 'react'
import {
  Building2,
  Crown,
  Loader2,
  MailPlus,
  Plus,
  Ship,
  Trash2,
  Users,
} from 'lucide-react'
import {
  createOrganization,
  createOrgInvitation,
  deleteOrganization,
  getMyOrganizations,
  getOrgInvitations,
  getOrgMembers,
  getOrgProjects,
  removeOrgMember,
  revokeOrgInvitation,
  updateOrgMemberRole,
} from '../../services/api'
import type { Invitation, Organization, OrgMemberEntry, OrgRole, Project } from '../../types'

const ORG_ROLE_LABELS: Record<string, string> = {
  owner: 'Eigentümer',
  admin: 'Administrator',
  member: 'Mitglied',
}

const TIER_LABELS: Record<string, string> = {
  free: 'FREE',
  pro: 'PRO',
  enterprise: 'ENTERPRISE',
}

export default function OrganizationsPage() {
  const [orgs, setOrgs] = useState<Organization[]>([])
  const [loading, setLoading] = useState(true)
  const [error, setError] = useState<string | null>(null)
  const [selectedId, setSelectedId] = useState<string | null>(null)
  const [creating, setCreating] = useState(false)
  const [newName, setNewName] = useState('')

  const loadOrgs = useCallback(async () => {
    setError(null)
    try {
      const list = await getMyOrganizations()
      setOrgs(list)
      setSelectedId((prev) => prev ?? (list[0]?.id ?? null))
    } catch (e) {
      setError(e instanceof Error ? e.message : 'Organisationen konnten nicht geladen werden')
    } finally {
      setLoading(false)
    }
  }, [])

  useEffect(() => {
    loadOrgs()
  }, [loadOrgs])

  const handleCreate = async (e: React.FormEvent) => {
    e.preventDefault()
    if (!newName.trim()) return
    setCreating(true)
    setError(null)
    try {
      const org = await createOrganization(newName.trim())
      setNewName('')
      await loadOrgs()
      setSelectedId(org.id)
    } catch (err) {
      setError(err instanceof Error ? err.message : 'Anlegen fehlgeschlagen')
    } finally {
      setCreating(false)
    }
  }

  const selected = orgs.find((o) => o.id === selectedId) ?? null

  if (loading) {
    return (
      <div className="px-6 md:px-10 py-12 flex items-center gap-2 text-navy-600">
        <Loader2 className="w-5 h-5 animate-spin" /> Lade Organisationen...
      </div>
    )
  }

  return (
    <div className="px-6 md:px-10 py-12 max-w-6xl mx-auto">
      <div className="flex items-center gap-3 mb-8">
        <Building2 className="w-7 h-7 text-ocean-600" />
        <h1 className="font-serif text-2xl text-navy-900">Organisationen</h1>
      </div>

      {error && (
        <div className="border-l-4 border-amber-400 bg-amber-50 rounded-r px-4 py-2 text-sm text-amber-900 mb-6">
          {error}
        </div>
      )}

      <div className="grid grid-cols-1 lg:grid-cols-[280px_1fr] gap-8">
        {/* Org list + create */}
        <div className="space-y-4">
          <form onSubmit={handleCreate} className="card-premium px-4 py-4 space-y-3">
            <label htmlFor="org-name" className="label-premium block">Neue Organisation</label>
            <input
              id="org-name"
              value={newName}
              onChange={(e) => setNewName(e.target.value)}
              placeholder="z.B. Werft Nord GmbH"
              className="w-full rounded-lg border border-sand-200 bg-white px-3 py-2 text-sm text-navy-900 focus:border-ocean-500 focus:outline-none"
            />
            <button
              type="submit"
              disabled={creating || !newName.trim()}
              className="w-full flex items-center justify-center gap-2 bg-ocean-700 hover:bg-ocean-600 disabled:opacity-50 text-navy-900 px-4 py-2 rounded-lg text-sm font-medium transition-all"
            >
              {creating ? <Loader2 className="w-4 h-4 animate-spin" /> : <Plus className="w-4 h-4" />}
              Anlegen
            </button>
          </form>

          <ul className="space-y-2">
            {orgs.map((org) => (
              <li key={org.id}>
                <button
                  onClick={() => setSelectedId(org.id)}
                  className={`w-full text-left rounded-lg border px-4 py-3 transition-all ${
                    org.id === selectedId
                      ? 'border-ocean-400 bg-ocean-50'
                      : 'border-sand-200 hover:bg-sand-50'
                  }`}
                >
                  <p className="text-navy-900 font-medium text-sm truncate">{org.name}</p>
                  <p className="text-xs text-navy-500 flex items-center gap-2 mt-0.5">
                    <span>{ORG_ROLE_LABELS[org.org_role ?? ''] ?? org.org_role}</span>
                    <span className="px-1.5 py-0.5 rounded bg-sand-100 text-navy-600">
                      {TIER_LABELS[org.tier] ?? org.tier}
                    </span>
                  </p>
                </button>
              </li>
            ))}
            {orgs.length === 0 && (
              <li className="text-sm text-navy-500 px-1">
                Noch keine Organisation. Legen Sie eine an, um ein Werft-Team
                und geteilte Projekte zu verwalten.
              </li>
            )}
          </ul>
        </div>

        {/* Detail */}
        {selected ? (
          <OrgDetail key={selected.id} org={selected} onChanged={loadOrgs} />
        ) : (
          <div className="card-premium px-8 py-12 text-center text-navy-600">
            Wählen Sie links eine Organisation.
          </div>
        )}
      </div>
    </div>
  )
}

function OrgDetail({ org, onChanged }: { org: Organization; onChanged: () => void }) {
  const [members, setMembers] = useState<OrgMemberEntry[]>([])
  const [invitations, setInvitations] = useState<Invitation[]>([])
  const [projects, setProjects] = useState<Project[]>([])
  const [fleetLocked, setFleetLocked] = useState(false)
  const [loading, setLoading] = useState(true)
  const [error, setError] = useState<string | null>(null)
  const [notice, setNotice] = useState<string | null>(null)
  const [email, setEmail] = useState('')
  const [inviteRole, setInviteRole] = useState<'member' | 'admin'>('member')
  const [inviting, setInviting] = useState(false)
  const [busyUserId, setBusyUserId] = useState<string | null>(null)

  const canManage = org.org_role === 'owner' || org.org_role === 'admin'
  const isOwner = org.org_role === 'owner'

  const reload = useCallback(async () => {
    setLoading(true)
    setError(null)
    try {
      const [mem, projRes] = await Promise.all([
        getOrgMembers(org.id),
        getOrgProjects(org.id).catch((e) => {
          // 403 → fleet view needs ENTERPRISE; treat as locked, not an error.
          if (e instanceof Error && /ENTERPRISE/i.test(e.message)) {
            setFleetLocked(true)
            return [] as Project[]
          }
          throw e
        }),
      ])
      setMembers(mem)
      setProjects(projRes)
      if (canManage) {
        setInvitations(await getOrgInvitations(org.id))
      }
    } catch (e) {
      setError(e instanceof Error ? e.message : 'Daten konnten nicht geladen werden')
    } finally {
      setLoading(false)
    }
  }, [org.id, canManage])

  useEffect(() => {
    reload()
  }, [reload])

  const handleInvite = async (e: React.FormEvent) => {
    e.preventDefault()
    if (!email.trim()) return
    setInviting(true)
    setError(null)
    setNotice(null)
    try {
      const inv = await createOrgInvitation(org.id, email.trim(), inviteRole)
      setInvitations((prev) => [inv, ...prev])
      setNotice(
        `Einladung für ${inv.email} erstellt — sie erscheint nach Anmeldung ` +
          'unter „Einladungen" (es wird keine E-Mail versendet).'
      )
      setEmail('')
    } catch (err) {
      setError(err instanceof Error ? err.message : 'Einladung fehlgeschlagen')
    } finally {
      setInviting(false)
    }
  }

  const handleRoleChange = async (member: OrgMemberEntry, role: OrgRole) => {
    if (role === member.org_role) return
    setBusyUserId(member.user_id)
    setError(null)
    try {
      const updated = await updateOrgMemberRole(org.id, member.user_id, role)
      setMembers((prev) => prev.map((m) => (m.user_id === member.user_id ? updated : m)))
      onChanged()
    } catch (err) {
      setError(err instanceof Error ? err.message : 'Rollenänderung fehlgeschlagen')
    } finally {
      setBusyUserId(null)
    }
  }

  const handleRemove = async (member: OrgMemberEntry) => {
    if (!window.confirm(`${member.email} aus der Organisation entfernen?`)) return
    setBusyUserId(member.user_id)
    setError(null)
    try {
      await removeOrgMember(org.id, member.user_id)
      setMembers((prev) => prev.filter((m) => m.user_id !== member.user_id))
    } catch (err) {
      setError(err instanceof Error ? err.message : 'Entfernen fehlgeschlagen')
    } finally {
      setBusyUserId(null)
    }
  }

  const handleDeleteOrg = async () => {
    if (!window.confirm(
      'Organisation wirklich löschen? Projekte bleiben bei ihren Erstellern ' +
        'erhalten (werden wieder privat).'
    )) return
    try {
      await deleteOrganization(org.id)
      onChanged()
    } catch (err) {
      setError(err instanceof Error ? err.message : 'Löschen fehlgeschlagen')
    }
  }

  if (loading) {
    return (
      <div className="card-premium px-8 py-12 flex items-center gap-2 text-navy-600">
        <Loader2 className="w-5 h-5 animate-spin" /> Lade...
      </div>
    )
  }

  return (
    <div className="space-y-6">
      <div className="card-premium px-6 py-5 flex items-center justify-between gap-4 flex-wrap">
        <div>
          <h2 className="font-serif text-xl text-navy-900">{org.name}</h2>
          <p className="text-xs text-navy-500 mt-1">
            Tarif {TIER_LABELS[org.tier] ?? org.tier} · Ihre Rolle{' '}
            {ORG_ROLE_LABELS[org.org_role ?? ''] ?? org.org_role}
          </p>
          {org.tier === 'free' && (
            <p className="text-xs text-navy-500 mt-1 max-w-md">
              Der Tarif wird manuell von AYDI verwaltet — es gibt derzeit keine
              Selbstverwaltung oder Abrechnung. ENTERPRISE schaltet die
              Flottenübersicht und Team-Features für alle Mitglieder frei.
            </p>
          )}
        </div>
        {isOwner && (
          <button
            onClick={handleDeleteOrg}
            className="flex items-center gap-1.5 text-xs text-red-600 border border-red-200 hover:bg-red-50 px-3 py-1.5 rounded-lg transition-all"
          >
            <Trash2 className="w-3.5 h-3.5" />
            Organisation löschen
          </button>
        )}
      </div>

      {error && (
        <div className="border-l-4 border-amber-400 bg-amber-50 rounded-r px-4 py-2 text-sm text-amber-900">
          {error}
        </div>
      )}
      {notice && (
        <div className="border-l-4 border-ocean-400 bg-ocean-50 rounded-r px-4 py-2 text-sm text-ocean-900">
          {notice}
        </div>
      )}

      {/* Invite */}
      {canManage && (
        <form onSubmit={handleInvite} className="card-premium px-6 py-5 flex flex-wrap items-end gap-3">
          <div className="flex-1 min-w-[180px]">
            <label htmlFor="org-invite-email" className="label-premium mb-2 block">
              Mitglied einladen
            </label>
            <input
              id="org-invite-email"
              type="email"
              value={email}
              onChange={(e) => setEmail(e.target.value)}
              placeholder="name@werft.de"
              className="w-full rounded-lg border border-sand-200 bg-white px-3 py-2 text-sm text-navy-900 focus:border-ocean-500 focus:outline-none"
            />
          </div>
          <div>
            <label htmlFor="org-invite-role" className="label-premium mb-2 block">Rolle</label>
            <select
              id="org-invite-role"
              value={inviteRole}
              onChange={(e) => setInviteRole(e.target.value as 'member' | 'admin')}
              className="rounded-lg border border-sand-200 bg-white px-3 py-2 text-sm text-navy-900 focus:border-ocean-500 focus:outline-none"
            >
              <option value="member">Mitglied</option>
              {/* Only owners may invite admins — the server enforces it too. */}
              <option value="admin" disabled={!isOwner}>Administrator</option>
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
      )}

      {/* Members */}
      <div className="card-premium px-6 py-5">
        <p className="label-premium mb-3 flex items-center gap-2">
          <Users className="w-3.5 h-3.5" />
          Mitglieder ({members.length})
        </p>
        <ul className="space-y-2">
          {members.map((member) => (
            <li
              key={member.user_id}
              className="flex items-center justify-between gap-3 rounded-lg border border-sand-200 px-4 py-2.5 text-sm"
            >
              <div className="min-w-0 flex items-center gap-2">
                {member.org_role === 'owner' && <Crown className="w-3.5 h-3.5 text-amber-500" />}
                <div className="min-w-0">
                  <p className="text-navy-900 truncate">{member.full_name}</p>
                  <p className="text-xs text-navy-600 truncate">{member.email}</p>
                </div>
              </div>
              <div className="flex items-center gap-3 flex-shrink-0">
                {isOwner ? (
                  <select
                    value={member.org_role}
                    onChange={(e) => handleRoleChange(member, e.target.value as OrgRole)}
                    disabled={busyUserId !== null}
                    aria-label={`Rolle von ${member.email}`}
                    className="text-xs px-2 py-1 rounded-lg border border-sand-300 bg-white focus:border-ocean-500 focus:outline-none disabled:opacity-50"
                  >
                    <option value="member">Mitglied</option>
                    <option value="admin">Administrator</option>
                    <option value="owner">Eigentümer</option>
                  </select>
                ) : (
                  <span className="text-xs px-2.5 py-1 rounded-full border bg-sand-100 text-navy-700 border-sand-300">
                    {ORG_ROLE_LABELS[member.org_role] ?? member.org_role}
                  </span>
                )}
                {canManage && (
                  <button
                    onClick={() => handleRemove(member)}
                    disabled={busyUserId !== null}
                    aria-label={`${member.email} entfernen`}
                    className="p-1.5 rounded text-navy-500 hover:text-red-600 hover:bg-red-50 transition-colors disabled:opacity-50"
                  >
                    {busyUserId === member.user_id ? (
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

      {/* Pending org invitations */}
      {canManage && invitations.length > 0 && (
        <div className="card-premium px-6 py-5">
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
                    {ORG_ROLE_LABELS[inv.role] ?? inv.role} · ausstehend
                  </p>
                </div>
                <button
                  onClick={async () => {
                    await revokeOrgInvitation(org.id, inv.id)
                    setInvitations((prev) => prev.filter((i) => i.id !== inv.id))
                  }}
                  aria-label={`Einladung für ${inv.email} zurückziehen`}
                  className="p-1.5 rounded text-navy-500 hover:text-red-600 hover:bg-red-50 transition-colors"
                >
                  <Trash2 className="w-4 h-4" />
                </button>
              </li>
            ))}
          </ul>
        </div>
      )}

      {/* Fleet view */}
      <div className="card-premium px-6 py-5">
        <p className="label-premium mb-3 flex items-center gap-2">
          <Ship className="w-3.5 h-3.5" />
          Flotte ({projects.length})
        </p>
        {fleetLocked ? (
          <p className="text-sm text-navy-600">
            Die Flottenübersicht ist ein ENTERPRISE-Feature. Sobald der Tarif
            der Organisation auf ENTERPRISE gehoben wird, erscheinen hier alle
            Projekte der Organisation.
          </p>
        ) : projects.length === 0 ? (
          <p className="text-sm text-navy-600">
            Noch keine Projekte in dieser Organisation. Projekte werden im
            Projekt-Detail über „Organisation" zugeordnet.
          </p>
        ) : (
          <ul className="grid grid-cols-1 sm:grid-cols-2 gap-3">
            {projects.map((p) => (
              <li key={p.id} className="rounded-lg border border-sand-200 px-4 py-3">
                <p className="text-navy-900 text-sm font-medium truncate">{p.name}</p>
                <p className="text-xs text-navy-500">
                  {p.length_m}m × {p.beam_m}m
                </p>
              </li>
            ))}
          </ul>
        )}
      </div>
    </div>
  )
}
