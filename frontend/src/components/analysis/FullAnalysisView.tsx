import { AlertTriangle, CheckCircle, Clock, Info, Lock, SkipForward, XCircle } from 'lucide-react'
import { useState, useEffect, useRef } from 'react'
import type { FullAnalysisResult, AnalysisModule, AnalysisResult } from '../../types'
import { ANALYSIS_MODULE_LABELS } from '../../types'
import ConfidenceBadge from './ConfidenceBadge'
import ScoreGauge from './ScoreGauge'

// ---------------------------------------------------------------------------
// Local types
//
// Der Orchestrator (`run_full_analysis`, backend/app/services/analysis/
// orchestrator.py) liefert mehr Felder zurück, als `FullAnalysisResult` in
// src/types/index.ts beschreibt: `tier_gated`, `tier_gated_count`, `tier` und
// (nur wenn vorhanden) `validation_warnings`. Ebenso trägt jedes Modulergebnis
// `degraded_subanalyses` — die Liste abgestürzter Teilanalysen. Die zentralen
// Typen gehören einer anderen Datei; deshalb werden die fehlenden Felder hier
// lokal ergänzt, statt sie global zu ändern.
// ---------------------------------------------------------------------------

interface OrchestratorExtras {
  tier_gated?: Record<string, string>
  tier_gated_count?: number
  validation_warnings?: string[]
  tier?: string
}

/** Modulergebnis inkl. der vom Modul gemeldeten ausgefallenen Teilanalysen. */
type ModuleAnalysisResult = AnalysisResult & {
  degraded_subanalyses?: string[]
}

/** Tarif-Anzeigenamen (Backend: SubscriptionTier in app/core/subscription.py). */
const TIER_LABELS: Record<string, string> = {
  free: 'FREE',
  pro: 'PRO',
  enterprise: 'ENTERPRISE',
}

/**
 * Mindest-Tarif je Modul — Spiegel von MODULE_FEATURE_MAP/_TIER_FEATURES
 * (backend/app/core/subscription.py). FREE enthält ergonomics, volume_storage,
 * emotional und market; alle übrigen Module ab PRO.
 */
const MODULE_REQUIRED_TIER: Record<string, string> = {
  compliance: 'pro',
  production: 'pro',
  materials: 'pro',
  structural: 'pro',
  cost: 'pro',
  service_patterns: 'pro',
  brand_dna: 'pro',
  community: 'pro',
}

/** Was der Nutzer tun kann, damit ein mangels Daten übersprungenes Modul läuft. */
const SKIP_ACTIONS: Record<string, string> = {
  materials: 'Materialien den Zonen zuweisen.',
  cost: 'Kostenpositionen zum Layout erfassen.',
  structural: 'Zonen dem Layout zuweisen.',
  service_patterns: 'Serviceberichte zum Projekt hinterlegen.',
  brand_dna: 'Frühere Modelle der Werft als Referenz hinterlegen.',
  market: 'Vergleichbare Wettbewerbsmodelle in der Datenbank erfassen.',
  ergonomics: 'Zonen und Durchgänge im Layout vervollständigen.',
  volume_storage: 'Zonen und Stauräume im Layout vervollständigen.',
  emotional: 'Zonen mit Maßen und Fenstern vervollständigen.',
  production: 'Zonen und Bauteile im Layout vervollständigen.',
  compliance: 'Zonen, Durchgänge und CE-Kategorie vervollständigen.',
}

/** Deutsche Namen der Teilanalysen (Backend: `analyses`-Listen je Modul). */
const SUB_ANALYSIS_LABELS: Record<string, string> = {
  // ergonomics
  passage_width: 'Durchgangsbreiten',
  path_efficiency: 'Wegeeffizienz',
  crew_guest_separation: 'Crew-/Gasttrennung',
  accessibility: 'Erreichbarkeit',
  helm_ergonomics: 'Steuerstand-Ergonomie',
  heel_impact: 'Krängungseinfluss',
  morning_circulation: 'Morgenzirkulation',
  access_complexity: 'Zugangsaufwand',
  headroom: 'Stehhöhe',
  // volume_storage
  utilization: 'Raumausnutzung',
  storage_ratio: 'Stauraumanteil',
  storage_distribution: 'Stauraumverteilung',
  storage_accessibility: 'Stauraum-Erreichbarkeit',
  furniture_ratio: 'Möbelanteil',
  // emotional
  room_proportion: 'Raumproportion',
  light_distribution: 'Lichtverteilung',
  sightline: 'Sichtachsen',
  sightline_rays: 'Sichtachsen (Raytracing)',
  visual_calm: 'Visuelle Ruhe',
  ceiling_perception: 'Deckenwirkung',
  inside_outside_flow: 'Innen-Außen-Bezug',
  // compliance
  ce_category: 'CE-Kategorie',
  escape_routes: 'Fluchtwege',
  escape_hatch: 'Notausstieg',
  fire_safety: 'Brandschutz',
  railing: 'Relingshöhen',
  stability: 'Stabilität',
  ventilation: 'Belüftung',
  cockpit_drain: 'Cockpit-Lenzung',
  companionway_sill: 'Niedergangsschwelle',
  electrical_access: 'Elektrik-Zugang',
  weights: 'Gewichte',
  // production
  assembly_sequence: 'Montagereihenfolge',
  form_complexity: 'Formkomplexität',
  service_access: 'Wartungszugang',
  standardization: 'Standardisierung',
  cable_routing: 'Kabelführung',
  mold_complexity: 'Formenbau-Komplexität',
  flat_panel_ratio: 'Flachpaneel-Anteil',
  // materials
  durability: 'Haltbarkeit',
  maintenance: 'Wartungsaufwand',
  known_issues: 'Bekannte Schwachstellen',
  compatibility: 'Materialverträglichkeit',
  weight: 'Gewicht',
  lifecycle_cost: 'Lebenszykluskosten',
  uv_exposure: 'UV-Belastung',
  moisture_risk: 'Feuchterisiko',
  // structural
  fore_aft: 'Längsbalance',
  lateral: 'Querbalance',
  heavy_placement: 'Schwergewichtsplatzierung',
  load_concentration: 'Lastkonzentration',
  loading_conditions: 'Beladungszustände',
  trim: 'Trimm',
  // cost
  material_costs: 'Materialkosten',
  labor_estimate: 'Arbeitszeitschätzung',
  cost_per_meter: 'Kosten je Meter',
  distribution: 'Kostenverteilung',
  risk: 'Kostenrisiko',
  parametric_estimate: 'Parametrische Schätzung',
  // service_patterns
  zone_issues: 'Zonenbezogene Mängel',
  age_patterns: 'Altersmuster',
  material_failures: 'Materialausfälle',
  design_warnings: 'Konstruktionshinweise',
  severity_burden: 'Schwerelast der Mängel',
  // brand_dna
  topology: 'Layout-Topologie',
  proportions: 'Proportionen',
  materials: 'Materialpalette',
  spatial: 'Räumliche Signatur',
  style: 'Stilkontinuität',
  // market
  metric_comparison: 'Kennzahlvergleich',
  competitive_position: 'Wettbewerbsposition',
  price_positioning: 'Preispositionierung',
  uniqueness: 'Alleinstellung',
  gaps: 'Marktlücken',
}

function scoreColor(score: number): string {
  if (score >= 80) return 'text-emerald-600'
  if (score >= 60) return 'text-amber-600'
  if (score >= 40) return 'text-orange-600'
  return 'text-red-600'
}

function scoreBorderColor(score: number): string {
  if (score >= 80) return 'border-emerald-500/30'
  if (score >= 60) return 'border-amber-500/30'
  if (score >= 40) return 'border-orange-500/30'
  return 'border-red-500/30'
}

function scoreBgColor(score: number): string {
  if (score >= 80) return 'bg-emerald-500/10'
  if (score >= 60) return 'bg-amber-500/10'
  if (score >= 40) return 'bg-orange-500/10'
  return 'bg-red-500/10'
}

function getModuleLabel(module: string): string {
  return ANALYSIS_MODULE_LABELS[module as AnalysisModule] ?? module
}

function getSubAnalysisLabel(name: string): string {
  return SUB_ANALYSIS_LABELS[name] ?? name.replace(/_/g, ' ')
}

function getTierLabel(tier: string | undefined): string {
  if (!tier) return '—'
  return TIER_LABELS[tier.toLowerCase()] ?? tier.toUpperCase()
}

function getRequiredTierLabel(module: string): string {
  return getTierLabel(MODULE_REQUIRED_TIER[module] ?? 'pro')
}

/**
 * Konkreter nächster Schritt für ein übersprungenes Modul. Der Grund kommt vom
 * Backend im Klartext; die Handlungsempfehlung wird daraus bzw. aus dem Modul
 * abgeleitet.
 */
function getSkipAction(module: string, reason: string): string | null {
  if (/Bootsklasse/i.test(reason)) {
    return 'Bootsklasse im Projekt prüfen und auf einen unterstützten Wert setzen.'
  }
  if (/Teilanalysen fehlgeschlagen/i.test(reason)) {
    return 'Eingabedaten prüfen — kein Teilergebnis war verwertbar.'
  }
  return SKIP_ACTIONS[module] ?? null
}

function getErrorMessage(value: unknown): string {
  if (typeof value === 'string') return value
  if (value && typeof value === 'object') {
    const detail = (value as Record<string, unknown>).error
    if (typeof detail === 'string') return detail
  }
  return 'Unbekannter Fehler'
}

function formatTimestamp(iso: string): string {
  try {
    const d = new Date(iso)
    return d.toLocaleString('de-DE', {
      day: '2-digit',
      month: '2-digit',
      year: 'numeric',
      hour: '2-digit',
      minute: '2-digit',
    })
  } catch {
    return iso
  }
}

interface FullAnalysisViewProps {
  result: FullAnalysisResult
  onModuleClick?: (module: string) => void
  isLoading?: boolean
}

// Loading skeleton component
function SkeletonLoader() {
  return (
    <div className="space-y-8">
      {/* Header skeleton */}
      <div className="card-premium p-6 animate-pulse">
        <div className="flex items-center justify-between gap-6">
          <div className="flex items-center gap-6">
            <div className="w-[140px] h-[140px] rounded-full bg-navy-700/30"></div>
            <div className="space-y-3">
              <div className="h-6 w-24 bg-navy-700/30 rounded"></div>
              <div className="h-4 w-32 bg-navy-700/30 rounded"></div>
            </div>
          </div>
          <div className="flex items-center gap-5">
            <div className="h-4 w-40 bg-navy-700/30 rounded"></div>
            <div className="h-4 w-40 bg-navy-700/30 rounded"></div>
          </div>
        </div>
      </div>

      {/* Cards grid skeleton */}
      <div className="space-y-4">
        <div className="h-4 w-24 bg-navy-700/30 rounded animate-pulse"></div>
        <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-5">
          {[...Array(6)].map((_, i) => (
            <div key={i} className="card-premium p-4 animate-pulse">
              <div className="h-6 w-20 bg-navy-700/30 rounded mb-3"></div>
              <div className="h-4 w-32 bg-navy-700/30 rounded mb-3"></div>
              <div className="h-4 w-28 bg-navy-700/30 rounded"></div>
            </div>
          ))}
        </div>
      </div>
    </div>
  )
}

// Module card with scroll-triggered animation
function ModuleCardWithAnimation({
  moduleName,
  analysisResult,
  onModuleClick,
  index,
}: {
  moduleName: string
  analysisResult: ModuleAnalysisResult
  onModuleClick?: (module: string) => void
  index: number
}) {
  const [hasAnimated, setHasAnimated] = useState(false)
  const cardRef = useRef<HTMLButtonElement>(null)

  useEffect(() => {
    const observer = new IntersectionObserver(
      ([entry]) => {
        if (entry.isIntersecting) {
          setHasAnimated(true)
          observer.unobserve(entry.target)
        }
      },
      { threshold: 0.1 }
    )

    if (cardRef.current) {
      observer.observe(cardRef.current)
    }

    return () => {
      if (cardRef.current) {
        observer.unobserve(cardRef.current)
      }
    }
  }, [])

  const score = analysisResult.overall_score
  const confidence =
    (analysisResult.config_used?.confidence as string) ??
    (analysisResult.config_used?.validation_level as string) ??
    'calculated'
  const warningCount = analysisResult.warnings?.length ?? 0
  const criticalCount =
    analysisResult.warnings?.filter((w) => w.severity === 'critical').length ?? 0
  const degraded = analysisResult.degraded_subanalyses ?? []

  return (
    <button
      ref={cardRef}
      onClick={() => onModuleClick?.(moduleName)}
      className={`card-premium p-4 text-left transition-all duration-300 group cursor-pointer ${scoreBorderColor(score)} ${scoreBgColor(score)} ${
        hasAnimated
          ? 'opacity-100 translate-y-0 shadow-lg shadow-navy-500/20'
          : 'opacity-0 translate-y-4 shadow-none'
      } hover:shadow-ocean-500/30 hover:shadow-lg hover:-translate-y-1`}
      style={{
        transitionDelay: `${index * 100}ms`,
      }}
    >
      <div className="flex items-start justify-between mb-3">
        <h4 className="text-sm font-sans font-semibold text-navy-900">
          {getModuleLabel(moduleName)}
        </h4>
        <span className={`font-mono text-2xl font-bold ${scoreColor(score)}`}>
          {hasAnimated ? Math.round(score) : '...'}
        </span>
      </div>
      <div className="flex flex-wrap items-center gap-2 mb-3">
        <ConfidenceBadge confidence={confidence} size="sm" />
        {degraded.length > 0 && (
          <span className="badge badge-amber">
            <AlertTriangle className="w-3 h-3" />
            Teilweise berechnet
          </span>
        )}
      </div>
      {degraded.length > 0 && (
        <div className="mb-3 rounded-md border border-amber-200 bg-amber-50 px-2.5 py-2">
          <p className="text-xs text-amber-700 leading-relaxed">
            {degraded.length === 1 ? 'Eine Teilanalyse ist' : `${degraded.length} Teilanalysen sind`}{' '}
            ausgefallen — die Note beruht nur auf den übrigen Teilanalysen:
          </p>
          <p className="mt-1 text-xs font-medium text-amber-700">
            {degraded.map(getSubAnalysisLabel).join(', ')}
          </p>
        </div>
      )}
      {warningCount > 0 && (
        <div className="flex items-center gap-2 text-xs text-navy-600">
          <AlertTriangle className="w-3 h-3 flex-shrink-0" />
          <span>
            {warningCount} Hinweis{warningCount !== 1 ? 'e' : ''}
            {criticalCount > 0 && (
              <span className="text-red-400">
                {' '}({criticalCount} kritisch)
              </span>
            )}
          </span>
        </div>
      )}
    </button>
  )
}

export default function FullAnalysisView({
  result,
  onModuleClick,
  isLoading = false,
}: FullAnalysisViewProps) {
  if (isLoading) {
    return <SkeletonLoader />
  }

  const extras = result as FullAnalysisResult & OrchestratorExtras

  const moduleEntries = Object.entries(result.modules ?? {}) as [string, ModuleAnalysisResult][]
  const skippedEntries = Object.entries(result.skipped ?? {})
  const errorEntries = Object.entries(result.errors ?? {})
  const tierGatedEntries = Object.entries(extras.tier_gated ?? {})
  const validationWarnings = extras.validation_warnings ?? []
  const degradedModules = moduleEntries.filter(
    ([, m]) => (m.degraded_subanalyses?.length ?? 0) > 0
  )
  const currentTier = extras.tier

  return (
    <div className="space-y-8">
      {/* Header with overall score */}
      <div className="card-premium p-6 animate-fade-in">
        <div className="flex flex-col lg:flex-row items-start lg:items-center justify-between gap-6">
          <div className="flex flex-col sm:flex-row items-start sm:items-center gap-6">
            {result.overall_score !== null ? (
              <ScoreGauge score={result.overall_score} label="Gesamtbewertung" size="md" />
            ) : (
              <div className="flex flex-col items-center">
                <div className="flex items-center justify-center w-[120px] h-[120px] rounded-full border-2 border-navy-700/60">
                  <span className="font-mono text-2xl text-navy-600">--</span>
                </div>
                <span className="mt-3 text-xs font-sans font-semibold uppercase tracking-wider-premium text-navy-700">
                  Gesamtbewertung
                </span>
              </div>
            )}
            <div className="space-y-3">
              <ConfidenceBadge confidence={result.overall_confidence} />
              <div className="flex items-center gap-2 text-xs text-navy-600">
                <Clock className="w-3.5 h-3.5" />
                <span>{formatTimestamp(result.executed_at)}</span>
              </div>
              {currentTier && (
                <div className="flex items-center gap-2 text-xs text-navy-600">
                  <Lock className="w-3.5 h-3.5" />
                  <span>Tarif {getTierLabel(currentTier)}</span>
                </div>
              )}
            </div>
          </div>

          {/* Summary stats */}
          <div className="flex flex-wrap items-center gap-3 sm:gap-5 text-xs w-full lg:w-auto">
            <div className="flex items-center gap-2 text-navy-700">
              <CheckCircle className="w-4 h-4 text-emerald-400 flex-shrink-0" />
              <span>{result.module_count} Module analysiert</span>
            </div>
            {degradedModules.length > 0 && (
              <div className="flex items-center gap-2 text-amber-700">
                <AlertTriangle className="w-4 h-4 flex-shrink-0" />
                <span>{degradedModules.length} teilweise berechnet</span>
              </div>
            )}
            {tierGatedEntries.length > 0 && (
              <div className="flex items-center gap-2 text-ocean-700">
                <Lock className="w-4 h-4 flex-shrink-0" />
                <span>{tierGatedEntries.length} tarifgesperrt</span>
              </div>
            )}
            {result.skipped_count > 0 && (
              <div className="flex items-center gap-2 text-navy-600">
                <SkipForward className="w-4 h-4 text-navy-500 flex-shrink-0" />
                <span>{result.skipped_count} übersprungen</span>
              </div>
            )}
            {result.error_count > 0 && (
              <div className="flex items-center gap-2 text-red-400">
                <XCircle className="w-4 h-4 flex-shrink-0" />
                <span>{result.error_count} Fehler</span>
              </div>
            )}
          </div>
        </div>
      </div>

      {/* Validation warnings (Plausibilität der Eingabedaten) */}
      {validationWarnings.length > 0 && (
        <div className="card-premium border-amber-200 bg-amber-50 p-5 animate-fade-in">
          <div className="flex items-start gap-3">
            <Info className="w-5 h-5 text-amber-600 flex-shrink-0 mt-0.5" />
            <div className="flex-1">
              <h3 className="text-sm font-sans font-semibold text-amber-800 mb-1">
                Hinweise zu den Eingabedaten
              </h3>
              <p className="text-xs text-amber-700 mb-3 leading-relaxed">
                Die Analyse wurde trotzdem gerechnet. Die Ergebnisse sind nur so
                belastbar wie die zugrunde liegenden Daten.
              </p>
              <ul className="space-y-1.5">
                {validationWarnings.map((warning, i) => (
                  <li key={i} className="text-xs text-amber-700 leading-relaxed">
                    • {warning}
                  </li>
                ))}
              </ul>
            </div>
          </div>
        </div>
      )}

      {/* Module cards grid */}
      {moduleEntries.length > 0 && (
        <div className="space-y-4">
          <h3 className="label-premium animate-fade-in">Analyseergebnisse</h3>
          <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-5">
            {moduleEntries.map(([moduleName, analysisResult], index) => (
              <ModuleCardWithAnimation
                key={moduleName}
                moduleName={moduleName}
                analysisResult={analysisResult}
                onModuleClick={onModuleClick}
                index={index}
              />
            ))}
          </div>
        </div>
      )}

      {/* Divider */}
      {(tierGatedEntries.length > 0 || skippedEntries.length > 0 || errorEntries.length > 0) &&
        moduleEntries.length > 0 && (
          <div className="border-t border-navy-700/30"></div>
        )}

      {/* Tier-gated modules — kein Fehler, sondern Tarifinformation */}
      {tierGatedEntries.length > 0 && (
        <div className="space-y-4 animate-fade-in">
          <div className="space-y-1">
            <h3 className="label-premium text-ocean-700">Im Tarif nicht enthalten</h3>
            <p className="text-xs text-navy-600 leading-relaxed">
              {tierGatedEntries.length === 1
                ? 'Ein Modul wurde'
                : `${tierGatedEntries.length} Module wurden`}{' '}
              mit Ihrem Tarif {getTierLabel(currentTier)} nicht gerechnet. Die
              Gesamtbewertung beruht deshalb nur auf den freigeschalteten Modulen.
            </p>
          </div>
          <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-5">
            {tierGatedEntries.map(([moduleName], index) => (
              <div
                key={moduleName}
                className="card-premium border-ocean-200 bg-ocean-50 p-4 transition-all duration-300 hover:shadow-lg hover:shadow-ocean-500/20 hover:-translate-y-0.5 animate-slide-in-right"
                style={{ animationDelay: `${Math.min(index, 7) * 80}ms` }}
              >
                <div className="flex items-center gap-2 mb-2">
                  <Lock className="w-4 h-4 text-ocean-600 flex-shrink-0" />
                  <h4 className="text-sm font-sans font-semibold text-navy-900">
                    {getModuleLabel(moduleName)}
                  </h4>
                </div>
                <p className="text-xs text-navy-600 leading-relaxed">
                  Verfügbar ab Tarif{' '}
                  <span className="font-semibold text-ocean-700">
                    {getRequiredTierLabel(moduleName)}
                  </span>
                  .
                </p>
                <span className="badge badge-ocean mt-2.5">
                  Ab {getRequiredTierLabel(moduleName)}
                </span>
              </div>
            ))}
          </div>
          <p className="text-xs text-navy-500 leading-relaxed">
            Tarife werden von AYDI manuell verwaltet — für eine Freischaltung
            wenden Sie sich an Ihren Ansprechpartner.
          </p>
        </div>
      )}

      {/* Divider */}
      {skippedEntries.length > 0 &&
        (tierGatedEntries.length > 0 || moduleEntries.length > 0) && (
          <div className="border-t border-navy-700/30"></div>
        )}

      {/* Skipped modules — mangels Daten nicht berechenbar */}
      {skippedEntries.length > 0 && (
        <div className="space-y-4 animate-fade-in">
          <div className="space-y-1">
            <h3 className="label-premium">Mangels Daten übersprungen</h3>
            <p className="text-xs text-navy-600 leading-relaxed">
              Diese Module konnten kein belastbares Ergebnis liefern. Sie sind
              nicht gesperrt — es fehlen Eingabedaten.
            </p>
          </div>
          <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-5">
            {skippedEntries.map(([moduleName, reason], index) => {
              const action = getSkipAction(moduleName, String(reason))
              return (
                <div
                  key={moduleName}
                  className="card-premium p-4 transition-all duration-300 hover:shadow-lg hover:shadow-navy-500/20 hover:-translate-y-0.5 animate-slide-in-right"
                  style={{ animationDelay: `${Math.min(index, 7) * 80}ms` }}
                >
                  <div className="flex items-center gap-2 mb-2">
                    <SkipForward className="w-4 h-4 text-navy-500 flex-shrink-0" />
                    <h4 className="text-sm font-sans font-semibold text-navy-600">
                      {getModuleLabel(moduleName)}
                    </h4>
                  </div>
                  <p className="text-xs text-navy-500 leading-relaxed">{reason}</p>
                  {action && (
                    <p className="mt-2.5 text-xs text-ocean-700 leading-relaxed">
                      Nächster Schritt: {action}
                    </p>
                  )}
                </div>
              )
            })}
          </div>
        </div>
      )}

      {/* Divider */}
      {errorEntries.length > 0 &&
        (skippedEntries.length > 0 || tierGatedEntries.length > 0 || moduleEntries.length > 0) && (
          <div className="border-t border-navy-700/30"></div>
        )}

      {/* Error modules */}
      {errorEntries.length > 0 && (
        <div className="space-y-4 animate-fade-in">
          <div className="space-y-1">
            <h3 className="label-premium text-red-400">Fehlgeschlagene Module</h3>
            <p className="text-xs text-navy-600 leading-relaxed">
              Diese Module sind bei der Berechnung abgestürzt. Das Ergebnis ist
              unvollständig — Analyse nach Behebung erneut starten.
            </p>
          </div>
          <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-5">
            {errorEntries.map(([moduleName, errorMsg], index) => (
              <div
                key={moduleName}
                className="card-premium border-red-500/30 bg-red-500/5 p-4 transition-all duration-300 hover:shadow-lg hover:shadow-red-500/20 hover:-translate-y-0.5 animate-slide-in-right"
                style={{ animationDelay: `${Math.min(index, 7) * 80}ms` }}
              >
                <div className="flex items-center gap-2 mb-2">
                  <XCircle className="w-4 h-4 text-red-400 flex-shrink-0" />
                  <h4 className="text-sm font-sans font-semibold text-red-300">
                    {getModuleLabel(moduleName)}
                  </h4>
                </div>
                <p className="text-xs text-red-400">{getErrorMessage(errorMsg)}</p>
              </div>
            ))}
          </div>
        </div>
      )}

    </div>
  )
}
