import { ShieldAlert, Clock, Users, FileSearch, Info } from 'lucide-react'
import type { BuyerInsights, BuyerKnownProblem } from '../../types'

interface BuyerInsightsPanelProps {
  insights: BuyerInsights
}

const CONFIDENCE_BADGES: Record<string, { label: string; className: string }> = {
  documented: { label: 'Dokumentiert', className: 'bg-ocean-100 text-ocean-700 border-ocean-300' },
  estimated: { label: 'Geschätzt', className: 'bg-amber-100 text-amber-700 border-amber-300' },
}

function ConfidenceBadge({ confidence }: { confidence?: string }) {
  const badge = CONFIDENCE_BADGES[confidence ?? ''] ?? null
  if (!badge) return null
  return (
    <span className={`text-xs px-2.5 py-1 rounded-full border whitespace-nowrap ${badge.className}`}>
      {badge.label}
    </span>
  )
}

function AppliesBadge({ problem }: { problem: BuyerKnownProblem }) {
  if (problem.applies_to_year === true) {
    return (
      <span className="text-xs px-2 py-0.5 rounded-full bg-red-100 text-red-700 border border-red-300 whitespace-nowrap">
        Betrifft dieses Baujahr
      </span>
    )
  }
  if (problem.applies_to_year === false) {
    return (
      <span className="text-xs px-2 py-0.5 rounded-full bg-sand-100 text-navy-600 border border-sand-300 whitespace-nowrap">
        Anderes Baujahr-Fenster
      </span>
    )
  }
  return (
    <span className="text-xs px-2 py-0.5 rounded-full bg-amber-100 text-amber-700 border border-amber-300 whitespace-nowrap">
      Baujahr-Zuordnung offen
    </span>
  )
}

function formatEur(value: number): string {
  return `${value.toLocaleString('de-DE')} €`
}

function formatEurRange(range?: number[] | null): string | null {
  if (!range || range.length !== 2) return null
  return `${range[0].toLocaleString('de-DE')}–${range[1].toLocaleString('de-DE')} €`
}

function formatYears(value: number): string {
  return value.toLocaleString('de-DE')
}

/**
 * Pillar 2 (Kaufberatung): known type weaknesses, age expectations and
 * community patterns for the specific boat identity entered in Level 1.
 */
export default function BuyerInsightsPanel({ insights }: BuyerInsightsPanelProps) {
  if (!insights.available) return null

  const identity = insights.boat_identity
  const manufacturer = insights.manufacturer
  const age = insights.age_expectations
  const community = insights.community

  const identityLabel = [
    identity?.brand,
    identity?.model_name,
    identity?.year ? `(${identity.year})` : null,
  ]
    .filter(Boolean)
    .join(' ')

  return (
    <div className="bg-white border border-sand-200 rounded-xl p-6 md:p-8 shadow-sm animate-fade-in-up">
      {/* Header */}
      <div className="flex items-start justify-between gap-4 mb-2">
        <div>
          <p className="text-xs font-semibold tracking-wider-premium uppercase text-navy-600 mb-1">
            Kaufberatung
          </p>
          <h3 className="font-serif text-lg font-medium text-navy-900">{identityLabel}</h3>
        </div>
        <ShieldAlert className="w-6 h-6 text-ocean-600 flex-shrink-0" />
      </div>
      {insights.summary_de && (
        <p className="text-sm text-navy-700 leading-relaxed mb-6">{insights.summary_de}</p>
      )}

      <div className="space-y-6">
        {/* Known type weaknesses */}
        {manufacturer && (
          <section>
            <div className="flex items-center justify-between gap-3 mb-3">
              <h4 className="flex items-center gap-2 text-sm font-semibold text-navy-900">
                <FileSearch className="w-4 h-4 text-ocean-600" />
                Bekannte Typ-Schwachstellen
                {manufacturer.display_name ? ` — ${manufacturer.display_name}` : ''}
              </h4>
              {manufacturer.found && <ConfidenceBadge confidence={manufacturer.confidence} />}
            </div>

            {!manufacturer.found ? (
              <p className="text-xs text-navy-600 leading-relaxed">{manufacturer.note}</p>
            ) : (
              <>
                {manufacturer.era_note_de && (
                  <p className="text-xs text-navy-600 italic mb-3">
                    Bauqualität-Einordnung: {manufacturer.era_note_de}
                  </p>
                )}
                {manufacturer.track_record_note_de && (
                  <div className="mb-3 border-l-4 border-emerald-400 bg-emerald-50/60 rounded-r px-3 py-2">
                    <p className="text-xs text-emerald-900">
                      {manufacturer.track_record_note_de}
                    </p>
                  </div>
                )}
                {manufacturer.problems_note_de && (
                  <p className="text-xs text-navy-600 leading-relaxed mb-3">
                    {manufacturer.problems_note_de}
                  </p>
                )}
                <ul className="space-y-3">
                  {(manufacturer.known_problems ?? []).map((problem, i) => (
                    <li
                      key={i}
                      className={`rounded-lg border p-3 ${
                        problem.applies_to_year === true
                          ? 'border-red-200 bg-red-50/50'
                          : 'border-sand-200 bg-sand-50/50'
                      }`}
                    >
                      <div className="flex items-start justify-between gap-2 flex-wrap mb-1">
                        <span className="text-sm font-medium text-navy-900">{problem.issue}</span>
                        <div className="flex items-center gap-2 flex-wrap">
                          <span className="text-xs text-navy-600">
                            Schwere: {problem.severity_de}
                          </span>
                          <AppliesBadge problem={problem} />
                        </div>
                      </div>
                      {problem.model_years && (
                        <p className="text-xs text-navy-600 mb-1">
                          Betroffene Baujahre: {problem.model_years}
                        </p>
                      )}
                      {problem.description && (
                        <p className="text-xs text-navy-700 leading-relaxed mb-1">
                          {problem.description}
                        </p>
                      )}
                      {problem.detection && (
                        <p className="text-xs text-navy-700 leading-relaxed">
                          <span className="font-medium">Prüfen:</span> {problem.detection}
                        </p>
                      )}
                      {(problem.repair_cost_eur || problem.affected_percentage) && (
                        <p className="text-xs text-navy-600 mt-1">
                          {problem.repair_cost_eur
                            ? `Typische Reparaturkosten: ${formatEur(problem.repair_cost_eur)}`
                            : ''}
                          {problem.repair_cost_eur && problem.affected_percentage ? ' · ' : ''}
                          {problem.affected_percentage
                            ? `Betroffen: ${problem.affected_percentage}`
                            : ''}
                        </p>
                      )}
                    </li>
                  ))}
                </ul>
                {manufacturer.survey_recommendation && (
                  <div className="mt-3 border-l-4 border-ocean-400 bg-ocean-50/60 rounded-r px-3 py-2">
                    <p className="text-xs text-navy-800">
                      <span className="font-semibold">Survey-Empfehlung:</span>{' '}
                      {manufacturer.survey_recommendation}
                    </p>
                  </div>
                )}
                {manufacturer.common_repair_costs_eur &&
                  Object.keys(manufacturer.common_repair_costs_eur).length > 0 && (
                    <div className="mt-3">
                      <p className="text-xs font-medium text-navy-800 mb-1">
                        Typische Reparaturkosten dieser Werft:
                      </p>
                      <ul className="text-xs text-navy-600 space-y-0.5">
                        {Object.entries(manufacturer.common_repair_costs_eur).map(
                          ([repair, cost]) => (
                            <li key={repair}>
                              {repair}:{' '}
                              {Array.isArray(cost)
                                ? formatEurRange(cost)
                                : formatEur(cost as number)}
                            </li>
                          ),
                        )}
                      </ul>
                    </div>
                  )}
              </>
            )}
          </section>
        )}

        {/* Age expectations */}
        {age && (
          <section>
            <div className="flex items-center justify-between gap-3 mb-3">
              <h4 className="flex items-center gap-2 text-sm font-semibold text-navy-900">
                <Clock className="w-4 h-4 text-ocean-600" />
                Altersbedingt prüfwürdig ({age.age_years} Jahre)
              </h4>
              <ConfidenceBadge confidence={age.confidence} />
            </div>
            {age.items.length === 0 ? (
              <p className="text-xs text-navy-600">
                Keine Komponenten im typischen Austauschfenster für dieses Alter.
              </p>
            ) : (
              <ul className="space-y-2">
                {age.items.map((item, i) => (
                  <li key={i} className="flex items-start gap-2">
                    <span
                      className={`mt-1 w-2 h-2 rounded-full flex-shrink-0 ${
                        item.severity === 'major'
                          ? 'bg-red-500'
                          : item.severity === 'moderate'
                          ? 'bg-amber-500'
                          : 'bg-ocean-400'
                      }`}
                    />
                    <div className="min-w-0">
                      <p className="text-sm text-navy-900">
                        <span className="font-medium">{item.component_de}</span>
                        <span className="text-xs text-navy-600">
                          {' '}
                          (typ. {formatYears(item.lifespan_years[0])}–{formatYears(item.lifespan_years[1])} Jahre
                          {item.lifespan_basis_de ? `, ${item.lifespan_basis_de}` : ''})
                        </span>
                      </p>
                      <p className="text-xs text-navy-700">{item.status_de}</p>
                      {item.inspection_hint && (
                        <p className="text-xs text-navy-600">
                          <span className="font-medium">Prüfen:</span> {item.inspection_hint}
                        </p>
                      )}
                      {formatEurRange(item.replacement_cost_range_eur) && (
                        <p className="text-xs text-navy-600">
                          Typische Austauschkosten: {formatEurRange(item.replacement_cost_range_eur)}
                        </p>
                      )}
                    </div>
                  </li>
                ))}
              </ul>
            )}
            <p className="text-xs text-navy-500 italic mt-2">{age.note_de}</p>
          </section>
        )}

        {/* Community patterns */}
        {community && (
          <section>
            <div className="flex items-center justify-between gap-3 mb-3">
              <h4 className="flex items-center gap-2 text-sm font-semibold text-navy-900">
                <Users className="w-4 h-4 text-ocean-600" />
                Community-Erfahrungen
              </h4>
              {community.available && <ConfidenceBadge confidence={community.confidence} />}
            </div>
            {!community.available ? (
              <p className="text-xs text-navy-600">{community.note}</p>
            ) : (
              <ul className="space-y-2">
                {(community.patterns ?? []).map((pattern, i) => (
                  <li key={i} className="text-xs text-navy-700 leading-relaxed">
                    <span className="font-medium text-navy-900">
                      {pattern.is_positive ? '✓' : '⚠'} {pattern.description}
                    </span>
                    {' — '}
                    {pattern.report_count} Bericht{pattern.report_count === 1 ? '' : 'e'}
                    {pattern.typical_onset_years != null &&
                      `, typisch ab Jahr ${formatYears(pattern.typical_onset_years)}`}
                    {pattern.match_reason_de && ` (${pattern.match_reason_de})`}
                  </li>
                ))}
              </ul>
            )}
          </section>
        )}

        {/* Disclaimer */}
        {insights.disclaimer_de && (
          <div className="flex items-start gap-2 pt-4 border-t border-sand-200">
            <Info className="w-4 h-4 text-navy-500 flex-shrink-0 mt-0.5" />
            <p className="text-xs text-navy-600 leading-relaxed">{insights.disclaimer_de}</p>
          </div>
        )}
      </div>
    </div>
  )
}
