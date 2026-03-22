import { useState } from 'react'
import { Plus, Minus, Edit2 } from 'lucide-react'
import type { LayoutDiff } from '../../types'

interface DiffViewerProps {
  diff: LayoutDiff
}

type Tab = 'zones' | 'passages'

export default function DiffViewer({ diff }: DiffViewerProps) {
  const [tab, setTab] = useState<Tab>('zones')
  const { summary } = diff

  if (!summary.has_changes) {
    return (
      <div className="card-premium p-8 text-center">
        <p className="text-navy-600 text-sm">Keine Unterschiede zwischen den Versionen gefunden.</p>
      </div>
    )
  }

  return (
    <div className="space-y-6">
      {/* Summary bar */}
      <div className="card-premium p-5">
        <h3 className="font-sans font-semibold text-navy-900 mb-4">Zusammenfassung</h3>
        <div className="flex flex-wrap gap-2.5">
          {summary.zones_added > 0 && (
            <span className="flex items-center gap-1.5 text-xs text-emerald-300 bg-emerald-900/20 border border-emerald-700/40 px-3 py-1.5 rounded-full font-medium">
              <Plus className="w-3 h-3" />
              {summary.zones_added} Zone{summary.zones_added !== 1 ? 'n' : ''} hinzugefügt
            </span>
          )}
          {summary.zones_removed > 0 && (
            <span className="flex items-center gap-1.5 text-xs text-red-300 bg-red-900/20 border border-red-700/40 px-3 py-1.5 rounded-full font-medium">
              <Minus className="w-3 h-3" />
              {summary.zones_removed} Zone{summary.zones_removed !== 1 ? 'n' : ''} entfernt
            </span>
          )}
          {summary.zones_modified > 0 && (
            <span className="flex items-center gap-1.5 text-xs text-amber-300 bg-amber-900/20 border border-amber-700/40 px-3 py-1.5 rounded-full font-medium">
              <Edit2 className="w-3 h-3" />
              {summary.zones_modified} Zone{summary.zones_modified !== 1 ? 'n' : ''} geändert
            </span>
          )}
          {summary.passages_added > 0 && (
            <span className="flex items-center gap-1.5 text-xs text-emerald-300 bg-emerald-900/20 border border-emerald-700/40 px-3 py-1.5 rounded-full font-medium">
              <Plus className="w-3 h-3" />
              {summary.passages_added} Durchgang{summary.passages_added !== 1 ? 'e' : ''}{' '}
              hinzugefügt
            </span>
          )}
          {summary.passages_removed > 0 && (
            <span className="flex items-center gap-1.5 text-xs text-red-300 bg-red-900/20 border border-red-700/40 px-3 py-1.5 rounded-full font-medium">
              <Minus className="w-3 h-3" />
              {summary.passages_removed} Durchgang{summary.passages_removed !== 1 ? 'e' : ''}{' '}
              entfernt
            </span>
          )}
          {summary.passages_modified > 0 && (
            <span className="flex items-center gap-1.5 text-xs text-amber-300 bg-amber-900/20 border border-amber-700/40 px-3 py-1.5 rounded-full font-medium">
              <Edit2 className="w-3 h-3" />
              {summary.passages_modified} Durchgang{summary.passages_modified !== 1 ? 'e' : ''}{' '}
              geändert
            </span>
          )}
          {summary.total_area_change_sqm !== 0 && (
            <span
              className={`text-xs px-3 py-1.5 rounded-full border font-mono font-medium ${
                summary.total_area_change_sqm > 0
                  ? 'text-emerald-300 bg-emerald-900/20 border-emerald-700/40'
                  : 'text-red-300 bg-red-900/20 border-red-700/40'
              }`}
            >
              {summary.total_area_change_sqm > 0 ? '+' : ''}
              {summary.total_area_change_sqm.toFixed(1)} m² Gesamtfläche
            </span>
          )}
        </div>
      </div>

      {/* Tabs */}
      <div className="flex gap-1 card-premium p-1">
        {(['zones', 'passages'] as Tab[]).map((t) => (
          <button
            key={t}
            onClick={() => setTab(t)}
            className={`flex-1 py-2 rounded-lg text-xs font-sans font-semibold uppercase tracking-wider-premium transition-all duration-200 ${
              tab === t ? 'bg-ocean-700 text-navy-900' : 'text-navy-600 hover:text-navy-600'
            }`}
          >
            {t === 'zones' ? 'Zonen' : 'Durchgänge'}
          </button>
        ))}
      </div>

      {/* Zones diff */}
      {tab === 'zones' && (
        <div className="space-y-4">
          {diff.zones.added.map((item, i) => (
            <div
              key={`added-${i}`}
              className="card-premium border-emerald-600/30 bg-emerald-900/10 p-4"
            >
              <div className="flex items-center gap-2 mb-2">
                <Plus className="w-4 h-4 text-emerald-400 flex-shrink-0" />
                <span className="font-sans font-semibold text-emerald-300">{item.name}</span>
                <span className="text-xs text-emerald-700 uppercase font-medium">hinzugefügt</span>
              </div>
              <p className="text-xs text-navy-600 ml-6">
                Typ: {item.zone.zone_type} · Höhe: {item.zone.height_mm ?? '—'} mm
              </p>
            </div>
          ))}

          {diff.zones.removed.map((item, i) => (
            <div
              key={`removed-${i}`}
              className="card-premium border-red-600/30 bg-red-900/10 p-4"
            >
              <div className="flex items-center gap-2 mb-2">
                <Minus className="w-4 h-4 text-red-400 flex-shrink-0" />
                <span className="font-sans font-semibold text-red-300">{item.name}</span>
                <span className="text-xs text-red-700 uppercase font-medium">entfernt</span>
              </div>
              <p className="text-xs text-navy-600 ml-6">Typ: {item.zone.zone_type}</p>
            </div>
          ))}

          {diff.zones.modified.map((item, i) => (
            <div
              key={`modified-${i}`}
              className="card-premium border-amber-600/30 bg-amber-900/10 p-4"
            >
              <div className="flex items-center gap-2 mb-2">
                <Edit2 className="w-4 h-4 text-amber-400 flex-shrink-0" />
                <span className="font-sans font-semibold text-amber-300">{item.name}</span>
                <span className="text-xs text-amber-700 uppercase font-medium">geändert</span>
              </div>
              <div className="ml-6 space-y-1">
                {item.changes.map((change, j) => (
                  <div key={j} className="flex items-center gap-2 text-xs">
                    <span className="text-navy-600 w-32 shrink-0">{change.field}</span>
                    <span className="font-mono text-red-400 line-through">
                      {String(change.old)}
                    </span>
                    <span className="text-navy-600">→</span>
                    <span className="font-mono text-emerald-400">{String(change.new)}</span>
                  </div>
                ))}
              </div>
            </div>
          ))}

          {diff.zones.unchanged.length > 0 && (
            <div className="card-premium bg-navy-900/20 p-4">
              <p className="text-xs text-navy-500">
                {diff.zones.unchanged.length} unveränderte Zone
                {diff.zones.unchanged.length !== 1 ? 'n' : ''}:{' '}
                {diff.zones.unchanged.join(', ')}
              </p>
            </div>
          )}
        </div>
      )}

      {/* Passages diff */}
      {tab === 'passages' && (
        <div className="space-y-4">
          {diff.passages.added.map((item, i) => (
            <div
              key={`added-${i}`}
              className="card-premium border-emerald-600/30 bg-emerald-900/10 p-4"
            >
              <div className="flex items-center gap-2 mb-2">
                <Plus className="w-4 h-4 text-emerald-400 flex-shrink-0" />
                <span className="font-sans font-semibold text-emerald-300">
                  {item.from_zone} → {item.to_zone}
                </span>
                <span className="text-xs text-emerald-700 uppercase font-medium">hinzugefügt</span>
              </div>
              <p className="text-xs text-navy-600 ml-6 font-mono">
                Breite: {item.passage.width_mm} mm
              </p>
            </div>
          ))}

          {diff.passages.removed.map((item, i) => (
            <div
              key={`removed-${i}`}
              className="card-premium border-red-600/30 bg-red-900/10 p-4"
            >
              <div className="flex items-center gap-2 mb-2">
                <Minus className="w-4 h-4 text-red-400 flex-shrink-0" />
                <span className="font-sans font-semibold text-red-300">
                  {item.from_zone} → {item.to_zone}
                </span>
                <span className="text-xs text-red-700 uppercase font-medium">entfernt</span>
              </div>
              <p className="text-xs text-navy-600 ml-6 font-mono">
                Breite: {item.passage.width_mm} mm
              </p>
            </div>
          ))}

          {diff.passages.modified.map((item, i) => (
            <div
              key={`modified-${i}`}
              className="card-premium border-amber-600/30 bg-amber-900/10 p-4"
            >
              <div className="flex items-center gap-2 mb-2">
                <Edit2 className="w-4 h-4 text-amber-400 flex-shrink-0" />
                <span className="font-sans font-semibold text-amber-300">
                  {item.from_zone} → {item.to_zone}
                </span>
                <span className="text-xs text-amber-700 uppercase font-medium">geändert</span>
              </div>
              <div className="ml-6 space-y-1">
                {item.changes.map((change, j) => (
                  <div key={j} className="flex items-center gap-2 text-xs">
                    <span className="text-navy-600 w-32 shrink-0">{change.field}</span>
                    <span className="font-mono text-red-400 line-through">
                      {String(change.old)}
                    </span>
                    <span className="text-navy-600">→</span>
                    <span className="font-mono text-emerald-400">{String(change.new)}</span>
                  </div>
                ))}
              </div>
            </div>
          ))}

          {diff.passages.added.length === 0 &&
            diff.passages.removed.length === 0 &&
            diff.passages.modified.length === 0 && (
              <div className="card-premium bg-navy-900/20 p-4 text-center">
                <p className="text-xs text-navy-500">Keine Änderungen an Durchgängen</p>
              </div>
            )}
        </div>
      )}
    </div>
  )
}
