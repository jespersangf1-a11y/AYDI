import { useCallback, useEffect, useRef, useState } from 'react'
import { getAuthToken } from '../services/api'

/**
 * Pillar 4, stage 2: frontend client for the collaboration WebSocket
 * (backend/app/api/routes/collaborate.py). The protocol is broadcast-only —
 * nothing is persisted server-side. The UI must say so (reliability rule:
 * never imply durability that does not exist).
 *
 * Scope decisions (stage 2, deliberate):
 * - presence, live cursors (mm coordinates), zone selection highlights and
 *   ephemeral comments are supported;
 * - zone_edit frames are NOT applied to local state — remote geometry
 *   mutation without conflict resolution would silently corrupt the local
 *   editing session. Incoming zone_edit is surfaced as an activity note only.
 */

export type CollabStatus = 'idle' | 'connecting' | 'connected' | 'denied' | 'reconnecting'

export interface CollabUser {
  user_id: string
  name: string
  role: string // owner | editor | viewer
  joined_at?: string
}

export interface CollabCursor {
  user: CollabUser
  x: number // mm, layout coordinate system
  y: number // mm
  updatedAt: number
}

export interface CollabComment {
  id: string
  user: CollabUser
  text: string
  timestamp: string
}

export interface CollabActivity {
  id: string
  text: string
  timestamp: string
}

interface CollaborationState {
  status: CollabStatus
  /** Close/deny reason (German, from server close frame or error message) */
  statusDetail: string | null
  participants: CollabUser[]
  cursors: Record<string, CollabCursor>
  /** zone name -> users that currently have it selected */
  selections: Record<string, CollabUser[]>
  comments: CollabComment[]
  activity: CollabActivity[]
}

const INITIAL: CollaborationState = {
  status: 'idle',
  statusDetail: null,
  participants: [],
  cursors: {},
  selections: {},
  comments: [],
  activity: [],
}

const MAX_COMMENTS = 100
const MAX_ACTIVITY = 30
const CURSOR_THROTTLE_MS = 60
const CURSOR_STALE_MS = 8000
/** 4001 = not authenticated, 4003 = no access / tier — do not retry those. */
const NO_RETRY_CODES = new Set([4001, 4003])
/** Cap reconnects so a persistent abnormal close (1006) can't hammer forever
    — e.g. if a denial ever arrives as 1006 instead of a custom code. */
const MAX_RECONNECTS = 6

let nextLocalId = 0
function localId(): string {
  nextLocalId += 1
  return `c${nextLocalId}-${Date.now()}`
}

export function useCollaboration(layoutId: string | null, enabled: boolean) {
  const [state, setState] = useState<CollaborationState>(INITIAL)
  const wsRef = useRef<WebSocket | null>(null)
  const retryRef = useRef(0)
  const retryTimerRef = useRef<number | null>(null)
  const lastCursorSentRef = useRef(0)
  const closedByUsRef = useRef(false)

  const connect = useCallback((lid: string) => {
    const token = getAuthToken()
    const proto = window.location.protocol === 'https:' ? 'wss' : 'ws'
    // Cookie auth works on the upgrade request too; the token query param is
    // the explicit fallback for localStorage-token sessions.
    const url =
      `${proto}://${window.location.host}/api/v1/ws/collaborate/${lid}` +
      (token ? `?token=${encodeURIComponent(token)}` : '')

    setState((prev) => ({
      ...prev,
      status: retryRef.current > 0 ? 'reconnecting' : 'connecting',
      statusDetail: null,
    }))

    const ws = new WebSocket(url)
    wsRef.current = ws

    ws.onopen = () => {
      retryRef.current = 0
      setState((prev) => ({ ...prev, status: 'connected', statusDetail: null }))
    }

    ws.onmessage = (event) => {
      let msg: Record<string, unknown>
      try {
        msg = JSON.parse(event.data as string)
      } catch {
        return
      }
      const type = msg.type as string
      const user = msg.user as CollabUser | undefined
      const timestamp = (msg.timestamp as string) ?? new Date().toISOString()

      setState((prev) => {
        switch (type) {
          case 'participants':
            return { ...prev, participants: (msg.participants as CollabUser[]) ?? [] }
          case 'user_joined': {
            if (!user) return prev
            const others = prev.participants.filter((p) => p.user_id !== user.user_id)
            return {
              ...prev,
              participants: [...others, user],
              activity: pushActivity(prev.activity, `${user.name} ist beigetreten`, timestamp),
            }
          }
          case 'user_left': {
            if (!user) return prev
            const cursors = { ...prev.cursors }
            delete cursors[user.user_id]
            return {
              ...prev,
              participants: prev.participants.filter((p) => p.user_id !== user.user_id),
              cursors,
              selections: removeUserFromSelections(prev.selections, user.user_id),
              activity: pushActivity(prev.activity, `${user.name} hat die Sitzung verlassen`, timestamp),
            }
          }
          case 'cursor_move': {
            if (!user) return prev
            const pos = (msg.position as { x?: number; y?: number }) ?? {}
            if (typeof pos.x !== 'number' || typeof pos.y !== 'number') return prev
            return {
              ...prev,
              cursors: {
                ...prev.cursors,
                [user.user_id]: { user, x: pos.x, y: pos.y, updatedAt: Date.now() },
              },
            }
          }
          case 'zone_select': {
            if (!user) return prev
            const zoneName = msg.zone_name as string | null
            const cleared = removeUserFromSelections(prev.selections, user.user_id)
            if (!zoneName) return { ...prev, selections: cleared }
            return {
              ...prev,
              selections: {
                ...cleared,
                [zoneName]: [...(cleared[zoneName] ?? []), user],
              },
            }
          }
          case 'comment': {
            if (!user) return prev
            const text = (msg.text as string) ?? ''
            if (!text.trim()) return prev
            return {
              ...prev,
              comments: [
                ...prev.comments.slice(-(MAX_COMMENTS - 1)),
                { id: localId(), user, text, timestamp },
              ],
            }
          }
          case 'zone_edit': {
            // Deliberately NOT applied to local geometry (no conflict
            // resolution) — surfaced as activity so the change is not silent.
            if (!user) return prev
            const zoneName = (msg.zone_name as string) ?? '?'
            return {
              ...prev,
              activity: pushActivity(
                prev.activity,
                `${user.name} bearbeitet Zone „${zoneName}" — Ansicht ggf. neu laden`,
                timestamp,
              ),
            }
          }
          case 'error': {
            return {
              ...prev,
              statusDetail: (msg.message as string) ?? 'Unbekannter Fehler',
            }
          }
          default:
            return prev
        }
      })
    }

    ws.onclose = (event) => {
      if (wsRef.current !== ws) return
      wsRef.current = null
      if (closedByUsRef.current) {
        setState(() => ({ ...INITIAL, status: 'idle' }))
        return
      }
      if (NO_RETRY_CODES.has(event.code)) {
        setState((prev) => ({
          ...prev,
          status: 'denied',
          statusDetail: event.reason || 'Zugriff verweigert',
          participants: [],
          cursors: {},
        }))
        return
      }
      // Give up after too many abnormal closes instead of hammering forever.
      if (retryRef.current >= MAX_RECONNECTS) {
        setState((prev) => ({
          ...prev,
          status: 'denied',
          statusDetail: 'Verbindung nicht möglich — bitte später erneut versuchen.',
          participants: [],
          cursors: {},
        }))
        return
      }
      // Transient close: retry with capped exponential backoff
      const delay = Math.min(10000, 1000 * 2 ** retryRef.current)
      retryRef.current += 1
      setState((prev) => ({
        ...prev,
        status: 'reconnecting',
        statusDetail: 'Verbindung unterbrochen — versuche erneut...',
        participants: [],
        cursors: {},
      }))
      retryTimerRef.current = window.setTimeout(() => connect(lid), delay)
    }

    ws.onerror = () => {
      // onclose follows and handles retry/state
    }
  }, [])

  useEffect(() => {
    if (!enabled || !layoutId) {
      return
    }
    closedByUsRef.current = false
    retryRef.current = 0
    connect(layoutId)
    return () => {
      closedByUsRef.current = true
      if (retryTimerRef.current !== null) {
        window.clearTimeout(retryTimerRef.current)
        retryTimerRef.current = null
      }
      wsRef.current?.close()
      wsRef.current = null
      setState(() => ({ ...INITIAL }))
    }
  }, [enabled, layoutId, connect])

  // Prune cursors that stopped moving (their owner may just be idle — the
  // presence list, not the cursor, is the source of truth for who is here).
  useEffect(() => {
    if (state.status !== 'connected') return
    const timer = window.setInterval(() => {
      setState((prev) => {
        const now = Date.now()
        const fresh = Object.fromEntries(
          Object.entries(prev.cursors).filter(([, c]) => now - c.updatedAt < CURSOR_STALE_MS),
        )
        return Object.keys(fresh).length === Object.keys(prev.cursors).length
          ? prev
          : { ...prev, cursors: fresh }
      })
    }, 2000)
    return () => window.clearInterval(timer)
  }, [state.status])

  const send = useCallback((payload: Record<string, unknown>) => {
    const ws = wsRef.current
    if (ws && ws.readyState === WebSocket.OPEN) {
      ws.send(JSON.stringify(payload))
    }
  }, [])

  const sendCursor = useCallback(
    (x: number, y: number) => {
      const now = Date.now()
      if (now - lastCursorSentRef.current < CURSOR_THROTTLE_MS) return
      lastCursorSentRef.current = now
      send({ type: 'cursor_move', position: { x, y } })
    },
    [send],
  )

  const sendZoneSelect = useCallback(
    (zoneName: string | null) => send({ type: 'zone_select', zone_name: zoneName }),
    [send],
  )

  const sendComment = useCallback(
    (text: string) => {
      const trimmed = text.trim()
      if (!trimmed) return
      send({ type: 'comment', text: trimmed })
      // The server excludes the sender from the broadcast — append locally.
      setState((prev) => ({
        ...prev,
        comments: [
          ...prev.comments.slice(-(MAX_COMMENTS - 1)),
          {
            id: localId(),
            user: { user_id: 'self', name: 'Sie', role: 'self' },
            text: trimmed,
            timestamp: new Date().toISOString(),
          },
        ],
      }))
    },
    [send],
  )

  return { ...state, sendCursor, sendZoneSelect, sendComment }
}

function pushActivity(
  activity: CollabActivity[],
  text: string,
  timestamp: string,
): CollabActivity[] {
  return [...activity.slice(-(MAX_ACTIVITY - 1)), { id: localId(), text, timestamp }]
}

function removeUserFromSelections(
  selections: Record<string, CollabUser[]>,
  userId: string,
): Record<string, CollabUser[]> {
  const result: Record<string, CollabUser[]> = {}
  for (const [zone, users] of Object.entries(selections)) {
    const remaining = users.filter((u) => u.user_id !== userId)
    if (remaining.length > 0) result[zone] = remaining
  }
  return result
}
