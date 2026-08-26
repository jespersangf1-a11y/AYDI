/**
 * Normalisierung der Antworten aus Pipeline B (visuelle Analyse).
 *
 * Warum das nötig ist — gegen das echte Backend geprüft
 * (`backend/app/api/routes/images.py`):
 *
 *  - `POST /api/v1/images/analyze` UND `POST /api/v1/projects/{id}/images`
 *    sind BEIDE auf `response_model=ImageUploadResponse` gesetzt. Es kommt
 *    also NICHT das flache `ImageAnalysisResponse` zurück, sondern der
 *    Upload-Datensatz — das Analyseergebnis steckt im Feld `ai_analysis`.
 *  - `ai_analysis` wird von `app/services/visual/analyzer.py` gebaut:
 *      { analysis: {...} | null, confidence: { level, is_usable, factors },
 *        score: number | null, error?: string }
 *  - Tarif-Gate (FREE, Feature VISUAL_ANALYSIS):
 *      `ai_analysis = { available: false, reason: "..." }`
 *    (`_tier_skipped_analysis`) — das Bild ist gespeichert, die Analyse
 *    unterblieb bewusst.
 *
 * Die Prompt-Ausgaben unterscheiden sich je Bildtyp (`findings` vs.
 * `overall_findings`, `rating` vs. `assessment`, `concerns` mal als
 * String-Liste, mal als Objektliste), deshalb wird hier bewusst tolerant
 * gelesen statt auf eine einzige Form zu vertrauen.
 */
import type { ImageAnalysisResult, VisualFinding } from '../types'

/**
 * Wie `ImageAnalysisResult`, aber mit den kanonischen Konfidenz-Codes
 * (`visual_high` … `visual_insufficient`), die der ConfidenceGatekeeper
 * liefert und die `ConfidenceBadge` kennt.
 */
export interface VisualAnalysisView extends Omit<ImageAnalysisResult, 'confidence'> {
  confidence: string
}

export interface NormalizedVisualAnalysis {
  /** Auswertbares Ergebnis — `null`, wenn keine Analyse gelaufen ist. */
  result: VisualAnalysisView | null
  /** Deutsche Begründung, warum kein Ergebnis vorliegt. */
  unavailableReason: string | null
  /** true, wenn die Analyse am PRO-Tarif-Gate hängt (nicht an einem Fehler). */
  tierGated: boolean
}

/** Score-Schlüssel der Prompts (analyzer.py: SCORE_KEYS). */
const SCORE_KEYS = [
  'spatial_score',
  'overall_quality_score',
  'material_score',
  'emotional_score',
  'exterior_score',
  'helm_score',
] as const

/** Befund-Schlüssel der Prompts (analyzer.py: FINDING_KEYS). */
const FINDING_KEYS = ['findings', 'overall_findings'] as const

const NO_ANALYSIS_REASON =
  'Für dieses Bild liegt keine visuelle Auswertung vor. Das Bild wurde gespeichert, aber nicht bewertet.'

const TIER_REASON_FALLBACK =
  'Die KI-Bildanalyse ist im PRO-Tarif enthalten. Das Bild wurde gespeichert, für die visuelle Auswertung ist ein Upgrade erforderlich.'

/** Deutsche Selbsteinschätzung der Prompts -> kanonischer Konfidenz-Code. */
const CONFIDENCE_ALIASES: Record<string, string> = {
  hoch: 'visual_high',
  mittel: 'visual_medium',
  niedrig: 'visual_low',
  sicher: 'visual_high',
  wahrscheinlich: 'visual_medium',
  vermutet: 'visual_low',
  high: 'visual_high',
  medium: 'visual_medium',
  low: 'visual_low',
  insufficient: 'visual_insufficient',
}

type Dict = Record<string, unknown>

function isDict(value: unknown): value is Dict {
  return typeof value === 'object' && value !== null && !Array.isArray(value)
}

function str(value: unknown): string | null {
  return typeof value === 'string' && value.trim().length > 0 ? value.trim() : null
}

function num(value: unknown): number | null {
  return typeof value === 'number' && Number.isFinite(value) ? value : null
}

/**
 * Listeneinträge können Strings ODER Objekte sein — der Build-Quality-Prompt
 * liefert `concerns` z.B. als {area, issue, severity, suggestion}.
 */
function toText(value: unknown): string | null {
  if (typeof value === 'string') return str(value)
  if (!isDict(value)) return null
  const head = str(value.area) ?? str(value.aspect) ?? str(value.category)
  const body =
    str(value.issue) ?? str(value.observation) ?? str(value.description) ?? str(value.text)
  const core = head && body ? `${head}: ${body}` : body ?? head
  if (!core) return null
  const suggestion = str(value.suggestion)
  return suggestion ? `${core} — ${suggestion}` : core
}

function toTextList(value: unknown): string[] {
  if (!Array.isArray(value)) return []
  return value.map(toText).filter((entry): entry is string => entry !== null)
}

function toFinding(value: unknown): VisualFinding | null {
  if (!isDict(value)) {
    const text = str(value)
    return text
      ? { category: 'Allgemein', observation: text, assessment: '', confidence: '' }
      : null
  }
  const observation =
    str(value.observation) ?? str(value.issue) ?? str(value.description) ?? str(value.text)
  if (!observation) return null
  return {
    category: str(value.category) ?? str(value.aspect) ?? str(value.area) ?? 'Allgemein',
    observation,
    // spatial/emotional-Prompts nennen es `rating`, quality-Prompt `assessment`.
    assessment: str(value.assessment) ?? str(value.rating) ?? '',
    confidence: str(value.confidence) ?? '',
    location_in_image: str(value.location_in_image),
    detail: str(value.detail) ?? str(value.notes),
    severity: str(value.severity),
    suggestion: str(value.suggestion),
  }
}

function collectFindings(analysis: Dict): VisualFinding[] {
  const findings: VisualFinding[] = []
  for (const key of FINDING_KEYS) {
    const raw = analysis[key]
    if (!Array.isArray(raw)) continue
    for (const entry of raw) {
      const finding = toFinding(entry)
      if (finding) findings.push(finding)
    }
  }
  return findings
}

function collectScores(analysis: Dict, envelope: Dict): Record<string, number> {
  const scores: Record<string, number> = {}
  for (const key of SCORE_KEYS) {
    const value = num(analysis[key])
    if (value !== null) scores[key] = value
  }
  if (Object.keys(scores).length === 0) {
    // `score` ist der vom Analyzer extrahierte Einzelwert (_extract_score).
    const overall = num(envelope.score)
    if (overall !== null) scores.overall = overall
  }
  return scores
}

function normalizeConfidenceCode(value: unknown): string | null {
  const raw = str(value)
  if (!raw) return null
  const key = raw.toLowerCase()
  if (key.startsWith('visual_')) return key
  return CONFIDENCE_ALIASES[key] ?? null
}

function buildView(imageId: string, envelope: Dict, analysis: Dict): VisualAnalysisView {
  const confidence = isDict(envelope.confidence) ? envelope.confidence : {}
  const level =
    normalizeConfidenceCode(confidence.level) ??
    normalizeConfidenceCode(analysis.confidence_overall) ??
    normalizeConfidenceCode(analysis.confidence) ??
    // Im Zweifel untertreiben statt überzeichnen (Reliability-Regel 1).
    'visual_low'

  return {
    image_id: imageId,
    scores: collectScores(analysis, envelope),
    findings: collectFindings(analysis),
    positive_aspects: toTextList(analysis.positive_aspects),
    concerns: toTextList(analysis.concerns),
    recommendations: toTextList(analysis.recommendations),
    cannot_assess: toTextList(analysis.cannot_assess),
    confidence: level,
    confidence_factors: toTextList(confidence.factors),
    image_quality_sufficient:
      confidence.is_usable !== false && analysis.image_quality_sufficient !== false,
  }
}

/** Bereits flaches `ImageAnalysisResponse` (falls die Route je umgestellt wird). */
function fromFlatResponse(raw: Dict): VisualAnalysisView {
  const findings = Array.isArray(raw.findings)
    ? raw.findings.map(toFinding).filter((f): f is VisualFinding => f !== null)
    : []
  const scores: Record<string, number> = {}
  if (isDict(raw.scores)) {
    for (const [key, value] of Object.entries(raw.scores)) {
      const parsed = num(value)
      if (parsed !== null) scores[key] = parsed
    }
  }
  return {
    image_id: str(raw.image_id) ?? str(raw.id) ?? '',
    scores,
    findings,
    positive_aspects: toTextList(raw.positive_aspects),
    concerns: toTextList(raw.concerns),
    recommendations: toTextList(raw.recommendations),
    cannot_assess: toTextList(raw.cannot_assess),
    confidence: normalizeConfidenceCode(raw.confidence) ?? 'visual_low',
    confidence_factors: toTextList(raw.confidence_factors),
    image_quality_sufficient: raw.image_quality_sufficient !== false,
  }
}

/**
 * Verwandelt die Rohantwort einer Upload-/Analyse-Route in ein anzeigbares
 * Ergebnis — oder in eine verständliche Begründung, warum keines vorliegt.
 */
export function normalizeVisualAnalysis(raw: unknown): NormalizedVisualAnalysis {
  if (!isDict(raw)) {
    return { result: null, unavailableReason: NO_ANALYSIS_REASON, tierGated: false }
  }

  // Defensiv: flache Analyse-Antwort direkt übernehmen.
  if (Array.isArray(raw.findings) || isDict(raw.scores)) {
    return { result: fromFlatResponse(raw), unavailableReason: null, tierGated: false }
  }

  const envelope = isDict(raw.ai_analysis) ? raw.ai_analysis : null
  if (!envelope) {
    return { result: null, unavailableReason: NO_ANALYSIS_REASON, tierGated: false }
  }

  // Tarif-Skip: Bild gespeichert, Analyse bewusst nicht gelaufen.
  if (envelope.available === false) {
    return {
      result: null,
      unavailableReason: str(envelope.reason) ?? TIER_REASON_FALLBACK,
      tierGated: true,
    }
  }

  const analysis = isDict(envelope.analysis) ? envelope.analysis : null
  if (!analysis) {
    // analyzer.py: _unavailable_result / _error_result tragen `error`.
    return {
      result: null,
      unavailableReason: str(envelope.error) ?? NO_ANALYSIS_REASON,
      tierGated: false,
    }
  }

  return {
    result: buildView(str(raw.id) ?? '', envelope, analysis),
    unavailableReason: null,
    tierGated: false,
  }
}
