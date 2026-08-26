/**
 * Shared helpers for ProjectDetail and its tab-views.
 *
 * Extracted from ProjectDetail.tsx as part of the production-readiness
 * refactor. Score-class helpers, analysis-collation utilities, and tab
 * types live here so the main container stays focused on data fetching
 * and routing concerns.
 */
import type { AnalysisResult, WarningData } from '../../../types'

export type TabType =
  | 'overview'
  | 'layouts'
  | 'analysis'
  | 'images'
  | 'materials'
  | 'structural'
  | 'costs'
  | 'service'
  | 'history'
export type ViewerMode = '2d' | '3d'

export const ALL_TABS: readonly TabType[] = [
  'overview',
  'layouts',
  'analysis',
  'images',
  'materials',
  'structural',
  'costs',
  'service',
  'history',
] as const

export function isTabType(value: string | undefined): value is TabType {
  return !!value && (ALL_TABS as readonly string[]).includes(value)
}

/** Flatten warnings across all analyses for one project. */
export function collectWarnings(analyses: AnalysisResult[]): WarningData[] {
  return analyses.flatMap((a) => a.warnings ?? [])
}

/** Group analyses by module, keeping only the most-recent per module. */
export function latestByModule(
  analyses: AnalysisResult[],
): Record<string, AnalysisResult> {
  const map: Record<string, AnalysisResult> = {}
  for (const a of analyses) {
    if (
      !map[a.module] ||
      new Date(a.created_at) > new Date(map[a.module].created_at)
    ) {
      map[a.module] = a
    }
  }
  return map
}

/** Tailwind text-color class by score bucket. */
export function moduleScoreClass(score: number): string {
  if (score >= 80) return 'text-emerald-600'
  if (score >= 60) return 'text-amber-600'
  if (score >= 40) return 'text-orange-600'
  return 'text-red-600'
}

/** Tailwind border-color class by score bucket. */
export function moduleBorderClass(score: number): string {
  if (score >= 80) return 'border-emerald-500/30'
  if (score >= 60) return 'border-amber-500/30'
  if (score >= 40) return 'border-orange-500/30'
  return 'border-red-500/30'
}

/** Tailwind background-color class by score bucket. */
export function moduleBgClass(score: number): string {
  if (score >= 80) return 'bg-emerald-500/5'
  if (score >= 60) return 'bg-amber-500/5'
  if (score >= 40) return 'bg-orange-500/5'
  return 'bg-red-500/5'
}
