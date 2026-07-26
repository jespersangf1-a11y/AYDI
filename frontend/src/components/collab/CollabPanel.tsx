import { useState } from 'react'
import { Loader2, MessageSquare, Radio, Send, Users, WifiOff } from 'lucide-react'
import type {
  CollabActivity,
  CollabComment,
  CollabStatus,
  CollabUser,
} from '../../hooks/useCollaboration'

interface CollabPanelProps {
  status: CollabStatus
  statusDetail: string | null
  participants: CollabUser[]
  comments: CollabComment[]
  activity: CollabActivity[]
  onSendComment: (text: string) => void
  onEndSession: () => void
}

const ROLE_LABELS: Record<string, string> = {
  owner: 'Eigentümer',
  editor: 'Bearbeiten',
  viewer: 'Nur Lesen',
}

function initials(name: string): string {
  const at = name.indexOf('@')
  const base = at > 0 ? name.slice(0, at) : name
  return base.slice(0, 2).toUpperCase()
}

/**
 * Pillar 4, stage 2: live-session side panel. Everything here is ephemeral —
 * the backend broadcasts but does not persist, and the panel says so
 * explicitly (never imply durability that does not exist).
 */
export default function CollabPanel({
  status,
  statusDetail,
  participants,
  comments,
  activity,
  onSendComment,
  onEndSession,
}: CollabPanelProps) {
  const [draft, setDraft] = useState('')

  const submit = (e: React.FormEvent) => {
    e.preventDefault()
    if (!draft.trim()) return
    onSendComment(draft)
    setDraft('')
  }

  return (
    <div className="card-premium px-6 py-5 space-y-4">
      <div className="flex items-center justify-between gap-3 flex-wrap">
        <h3 className="font-sans font-semibold text-navy-900 flex items-center gap-2 text-sm">
          {status === 'connected' ? (
            <Radio className="w-4 h-4 text-emerald-500" />
          ) : status === 'denied' ? (
            <WifiOff className="w-4 h-4 text-red-500" />
          ) : (
            <Loader2 className="w-4 h-4 animate-spin text-ocean-500" />
          )}
          Live-Sitzung
          {status === 'connected' && (
            <span className="text-xs font-normal text-emerald-600">verbunden</span>
          )}
          {status === 'reconnecting' && (
            <span className="text-xs font-normal text-amber-600">Verbindung wird wiederhergestellt...</span>
          )}
          {status === 'connecting' && (
            <span className="text-xs font-normal text-navy-500">verbinde...</span>
          )}
        </h3>
        <button
          onClick={onEndSession}
          className="text-xs text-navy-600 underline hover:text-navy-900 transition-colors"
        >
          Sitzung beenden
        </button>
      </div>

      {status === 'denied' && (
        <div className="border-l-4 border-red-400 bg-red-50 rounded-r px-3 py-2 text-xs text-red-900">
          {statusDetail ?? 'Zugriff verweigert'}
        </div>
      )}
      {status !== 'denied' && statusDetail && (
        <div className="border-l-4 border-amber-400 bg-amber-50 rounded-r px-3 py-2 text-xs text-amber-900">
          {statusDetail}
        </div>
      )}

      {status === 'connected' && (
        <>
          {/* Presence */}
          <div>
            <p className="label-premium mb-2 flex items-center gap-2">
              <Users className="w-3.5 h-3.5" />
              Teilnehmer ({participants.length})
            </p>
            {participants.length === 0 ? (
              <p className="text-xs text-navy-500">
                Noch niemand sonst in der Sitzung — Teilnehmer erscheinen hier,
                sobald sie beitreten.
              </p>
            ) : (
              <ul className="flex flex-wrap gap-2">
                {participants.map((p) => (
                  <li
                    key={p.user_id}
                    className="flex items-center gap-2 rounded-full border border-sand-200 pl-1 pr-3 py-1"
                    title={p.name}
                  >
                    <span className="w-6 h-6 rounded-full bg-ocean-700 text-navy-900 text-[10px] font-semibold flex items-center justify-center">
                      {initials(p.name)}
                    </span>
                    <span className="text-xs text-navy-900 max-w-[140px] truncate">{p.name}</span>
                    <span className="text-[10px] text-navy-500">
                      {ROLE_LABELS[p.role] ?? p.role}
                    </span>
                  </li>
                ))}
              </ul>
            )}
          </div>

          {/* Activity */}
          {activity.length > 0 && (
            <div>
              <p className="label-premium mb-2">Aktivität</p>
              <ul className="space-y-1 max-h-24 overflow-y-auto">
                {[...activity].reverse().map((a) => (
                  <li key={a.id} className="text-xs text-navy-600">
                    {a.text}
                  </li>
                ))}
              </ul>
            </div>
          )}

          {/* Comments (ephemeral!) */}
          <div>
            <p className="label-premium mb-2 flex items-center gap-2">
              <MessageSquare className="w-3.5 h-3.5" />
              Kommentare
            </p>
            <p className="text-[11px] text-amber-700 mb-2">
              Kommentare sind Teil der Live-Sitzung und werden{' '}
              <strong>nicht gespeichert</strong> — sie verschwinden beim Beenden.
            </p>
            <ul className="space-y-2 max-h-48 overflow-y-auto mb-3">
              {comments.length === 0 ? (
                <li className="text-xs text-navy-500">Noch keine Kommentare.</li>
              ) : (
                comments.map((c) => (
                  <li key={c.id} className="text-xs">
                    <span className="font-semibold text-navy-900">
                      {c.user.user_id === 'self' ? 'Sie' : c.user.name}
                    </span>{' '}
                    <span className="text-navy-500">
                      {new Date(c.timestamp).toLocaleTimeString('de-DE', {
                        hour: '2-digit',
                        minute: '2-digit',
                      })}
                    </span>
                    <p className="text-navy-700 break-words">{c.text}</p>
                  </li>
                ))
              )}
            </ul>
            <form onSubmit={submit} className="flex gap-2">
              <input
                type="text"
                value={draft}
                onChange={(e) => setDraft(e.target.value)}
                maxLength={500}
                placeholder="Kommentar an alle Teilnehmer..."
                className="flex-1 rounded-lg border border-sand-200 bg-white px-3 py-2 text-xs text-navy-900 focus:border-ocean-500 focus:outline-none"
              />
              <button
                type="submit"
                disabled={!draft.trim()}
                aria-label="Kommentar senden"
                className="flex items-center gap-1.5 bg-ocean-700 hover:bg-ocean-600 disabled:opacity-50 text-navy-900 px-3 py-2 rounded-lg text-xs font-medium transition-all"
              >
                <Send className="w-3.5 h-3.5" />
              </button>
            </form>
          </div>
        </>
      )}
    </div>
  )
}
