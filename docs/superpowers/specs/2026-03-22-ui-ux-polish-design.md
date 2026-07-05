> **⚠️ ARCHIV — HISTORISCHER PLANUNGSSTAND (nicht maßgeblich).**
> Dieses Dokument beschreibt einen früheren Planungs-/Design-Stand und trackt den aktuellen Code **nicht**.
> Bekannte Drift: 4 statt real **13 Bootsklassen** (`BoatClass`-Enum); abweichende Sub-Analysen/Gewichte; einzelne enthaltene Tests schlagen gegen den Ist-Code fehl.
> **Maßgeblich ist `CLAUDE.md`** (plus der Code). Nicht zum Ableiten von Enums, Return-Contracts oder Tests verwenden.

# AYDI UI/UX Polish — Design Specification

**Date:** 2026-03-22
**Approach:** Component-First Polish (evolutionary, not revolutionary)
**Scope:** All screens, all dimensions (typography, color, spacing, motion, components, accessibility)

---

## Context

AYDI frontend is a Scandinavian maritime-themed yacht design analysis platform built with React 18 + TypeScript + Tailwind CSS. The current design is already high-quality with Navy/Ocean/Sand color palette, Playfair Display + Inter typography, and extensive animations. This spec defines targeted polish to elevate consistency, accessibility, and refinement.

**Note:** CLAUDE.md lists DM Sans + Plus Jakarta Sans as target fonts, but the actual tailwind.config.js uses Playfair Display + Inter. This spec works with the implemented fonts. Font alignment with CLAUDE.md is a separate decision.

**Key constraints:**
- German UI text, English code
- Preserve existing Scandinavian maritime aesthetic
- Primarily visual polish. Exceptions: Phase 4.1 (IntersectionObserver scroll reveal) and Phase 5.5 (keyboard navigation) add minimal behavioral code required for polish and accessibility respectively.
- All changes must propagate through design tokens where possible

---

## Phase 1: Foundation (Tailwind Tokens)

### 1.1 Color Corrections

**Problem:** Multiple components use hardcoded `rgba(0, 176, 240, ...)` (bright cyan) instead of the Ocean design tokens `rgba(45, 139, 168, ...)`. Found in 6 files: Dashboard.tsx, QuickResults.tsx, MaterialBrowser.tsx, SpecForm.tsx, QuickAnalysis.tsx, ImageUpload.tsx (hover shadows/borders).

**Fix:** Replace all `rgba(0, 176, 240, ...)` with Ocean-token equivalents across all 6 components.

### 1.2 Typography Scale

**Current:** 3 custom sizes (hero: 3.5rem, display: 2.5rem, title: 1.75rem), then a gap to Tailwind's text-base (1rem).

**Add to tailwind.config.js:**
```
'subtitle': ['1.25rem', { lineHeight: '1.35', letterSpacing: '-0.005em' }],
'body-lg': ['1.0625rem', { lineHeight: '1.6' }],
```

### 1.3 Shadow System

**Current:** 4 custom shadows, all ocean-tinted. No neutral resting shadow for cards.

**Add:**
```
'card-rest': '0 1px 3px rgba(11, 18, 32, 0.04), 0 1px 2px rgba(11, 18, 32, 0.06)',
```

Note: `card-hover` already exists in the config. `card-rest` is the new neutral resting shadow. Together with the existing `card-hover`, this completes the card shadow system.

### 1.4 Spacing Tokens

**Add:**
```
spacing: {
  'section': '4rem',
  'section-lg': '6rem',
}
```

### 1.5 Border Radius Tokens

**Add:**
```
borderRadius: {
  'card': '14px',
  'button': '10px',
  'badge': '8px',
}
```

### 1.6 Transition Easings

**Add:**
```
transitionTimingFunction: {
  'premium': 'cubic-bezier(0.4, 0, 0.2, 1)',
  'bounce': 'cubic-bezier(0.34, 1.56, 0.64, 1)',
}
```

### 1.7 Score Colors (globals.css)

**Note:** The `.score-*` classes exist in globals.css but are currently unused by any component. Score colors are applied via inline Tailwind classes in components like ScoreGauge.tsx, SubScoreBars.tsx, and FusedScoreCard.tsx. The fix must update both the globals.css definitions AND the inline color logic in those components.

**Replace hardcoded hex values in globals.css:**
```css
.score-excellent { @apply text-emerald-600; }   /* was #4ade80 — WCAG fail */
.score-acceptable { @apply text-amber-600; }     /* was #fbbf24 — WCAG fail */
.score-poor { @apply text-orange-600; }           /* was #f97316 — borderline */
.score-critical { @apply text-red-600; }          /* was #ef4444 — OK but align */
```

Remove `.score-good` — merge with `.score-excellent` (two greens unnecessary).

**Additionally:** Update score color logic in ScoreGauge.tsx, SubScoreBars.tsx, and FusedScoreCard.tsx to use these classes or equivalent WCAG-compliant Tailwind classes (emerald-600, amber-600, orange-600, red-600).

**SVG gradient stops (ScoreGauge.tsx):** SVG `<stop>` elements cannot use Tailwind classes — they require raw hex values. Map to the updated WCAG palette:
- Excellent: `#059669` (emerald-600) / `#34d399` (emerald-400 for gradient end)
- Acceptable: `#d97706` (amber-600) / `#fbbf24` (amber-400 for gradient end)
- Poor: `#ea580c` (orange-600) / `#fb923c` (orange-400 for gradient end)
- Critical: `#dc2626` (red-600) / `#f87171` (red-400 for gradient end)

---

## Phase 2: Component Polish

### 2.1 Centralize Animations

**Problem:** 15+ components define inline `<style>` blocks with their own @keyframes. Duplicated and inconsistent. Full inventory:

| Component | Inline @keyframes |
|-----------|-------------------|
| Dashboard.tsx | projectCardSlideIn, emptyStateFloat, statusPulse, iconBounce |
| QuickResults.tsx | fadeInUp, countUp, moduleSlideIn, moduleHoverLift, skeletonPulse |
| QuickAnalysis.tsx | slideInRight, slideInLeft, stepPulse, cardStaggered, checkmarkScale |
| SpecForm.tsx | sectionExpand, sectionCollapse, shake, focusGlow, errorSlideIn |
| MaterialBrowser.tsx | tableRowHover, panelSlideIn, panelSlideOut, mobileOverlayFadeIn, filterTransition |
| ImageUpload.tsx | dragBorderPulse, previewScaleIn, progressFill, uploadPulse |
| FullAnalysisView.tsx | slideIn, fadeIn |
| ConfidenceBadge.tsx | fadeInScale |
| WarningList.tsx | slideIn, slideDown |
| SubScoreBars.tsx | slideIn |
| ScoreGauge.tsx | fadeIn |
| HeroCarousel.tsx | fadeInUp |
| HeroSection.tsx | fadeInUp |
| ProjectDetail.tsx | fadeInUp, slideInLeft, slideUnderline |
| ServiceReportList.tsx | fadeInUp, slideDown, borderGlow |
| KnowledgeDetail.tsx | slideInRight, slideOutRight, backdropFade, fadeInUp |
| KnowledgePage.tsx | fadeInUp, slideDown, ocnglow, pulse-glow |

**Fix:**
- Move ALL @keyframes to globals.css
- Remove all inline `<style>` template strings from components
- Components use only Tailwind classes or globals.css utility classes

**Canonical animation set (globals.css) — 8 base + 6 specialized:**

| Class | Animation | Duration | Easing | Replaces |
|-------|-----------|----------|--------|----------|
| `.animate-fade-in` | opacity 0→1 | 400ms | ease-out | fadeIn (multiple) |
| `.animate-fade-in-up` | opacity + translateY(16px→0) | 500ms | ease-out | fadeInUp (7 components) |
| `.animate-fade-in-scale` | opacity + scale(0.95→1) | 400ms | ease-out | fadeInScale, previewScaleIn, checkmarkScale |
| `.animate-slide-in-right` | opacity + translateX(24px→0) | 400ms | ease-premium | slideInRight, panelSlideIn |
| `.animate-slide-in-left` | opacity + translateX(-24px→0) | 400ms | ease-premium | slideInLeft |
| `.animate-slide-down` | opacity + translateY(-8px→0) | 300ms | ease-out | slideDown (multiple) |
| `.animate-draw-circle` | stroke-dashoffset | 1000ms | ease-out | (ScoreGauge) |
| `.animate-fill-bar` | width 0→target | 800ms | ease-out | progressFill |
| `.animate-shimmer` | background-position sweep | 1500ms | ease-in-out infinite | shimmer, skeletonPulse |
| `.animate-shake` | translateX wiggle | 400ms | ease-out | shake (SpecForm) |
| `.animate-section-expand` | grid-rows 0fr→1fr + opacity | 300ms | ease-out | sectionExpand |
| `.animate-section-collapse` | grid-rows 1fr→0fr + opacity | 200ms | ease-out | sectionCollapse |
| `.animate-slide-out-right` | opacity + translateX(0→100%) | 300ms | ease-premium | slideOutRight, panelSlideOut |
| `.animate-backdrop-fade` | opacity 0→1 on overlay | 300ms | ease-out | backdropFade, mobileOverlayFadeIn |
| `.animate-count-up` | opacity 0→1 (score numbers) | 600ms | ease-out | countUp |

**Implementation notes for new animations:**
- All 6 new animations (shake, section-expand, section-collapse, slide-out-right, backdrop-fade, count-up) require BOTH `@keyframes` in globals.css AND `animation` entries in tailwind.config.js.
- `section-expand`/`section-collapse`: Use `grid-template-rows: 0fr → 1fr` technique (not `height: auto` which cannot be animated). Wrap content in `<div style="overflow: hidden"><div style="min-height: 0">...</div></div>`.
- `ease-premium` is a new easing (Phase 1.6) — must be added to tailwind.config.js before these animations can reference it.

**Remove (infinite animations on static elements):** `iconBounce`, `statusPulse`, `emptyStateFloat`, `moduleHoverLift` — replace with one-shot or static alternatives.

**Remove (redundant, covered by canonical set):** `projectCardSlideIn`, `moduleSlideIn`, `cardStaggered`, `tableRowHover`, `filterTransition`, `errorSlideIn`, `focusGlow`, `borderGlow`, `ocnglow`, `slideUnderline`, `uploadPulse`, `dragBorderPulse`, `countUp` — these are all variants of the 14 canonical animations above.

**Keep:** `pulse-glow` only for active loading states (not static elements).

### 2.2 Card Hover System

**Note:** `.card-premium` already exists in globals.css (lines 108-114) with `rounded-xl shadow-sm` and hover `shadow-md`. This is a **redefinition** — replace the existing class, do not add a second one. The current Dashboard hover lift of `-12px` is intentionally reduced to `-6px` for a more refined feel.

**Replace existing `.card-premium` in globals.css:**
```css
.card-premium {
  @apply bg-white border border-sand-200 shadow-card-rest;
  border-radius: theme('borderRadius.card');
  transition: all 300ms theme('transitionTimingFunction.premium');
}
.card-premium:hover {
  @apply border-navy-100 shadow-card-hover;
  transform: translateY(-6px);
}
```

Variants:
- `.card-premium--compact`: hover translateY(-4px)
- `.card-premium--featured`: hover translateY(-8px)

### 2.3 Button System

**Add to globals.css:**
```css
.btn-primary {
  @apply bg-ocean-600 text-white font-sans font-medium px-5 py-2.5;
  border-radius: theme('borderRadius.button');
  transition: all 200ms theme('transitionTimingFunction.premium');
}
.btn-primary:hover { @apply bg-ocean-700; }
.btn-primary:active { transform: scale(0.97); @apply shadow-inner-ocean; }

.btn-secondary {
  @apply bg-white border border-sand-200 text-navy-700 font-sans font-medium px-5 py-2.5;
  border-radius: theme('borderRadius.button');
  transition: all 200ms theme('transitionTimingFunction.premium');
}
.btn-secondary:hover { @apply border-ocean-300 text-ocean-700; }

.btn-ghost {
  @apply text-navy-600 font-sans font-medium px-3 py-2;
  border-radius: theme('borderRadius.button');
  transition: all 200ms theme('transitionTimingFunction.premium');
}
.btn-ghost:hover { @apply text-ocean-600 bg-sand-100; }
```

### 2.4 Badge System

**Add to globals.css:**
```css
.badge {
  @apply inline-flex items-center gap-1.5 px-2.5 py-1 text-xs font-medium;
  border-radius: theme('borderRadius.badge');
}
.badge-ocean { @apply bg-ocean-50 text-ocean-700 border border-ocean-200; }
.badge-emerald { @apply bg-emerald-50 text-emerald-700 border border-emerald-200; }
.badge-amber { @apply bg-amber-50 text-amber-700 border border-amber-200; }
.badge-red { @apply bg-red-50 text-red-700 border border-red-200; }
.badge-sand { @apply bg-sand-100 text-navy-600 border border-sand-200; }
```

### 2.5 Input Consistency

**Standardize focus states everywhere:**
```css
input:focus, select:focus, textarea:focus {
  @apply ring-2 ring-ocean-300 border-ocean-400 outline-none;
}
```

### 2.6 Section Headers

**Standardize hierarchy:**
- Page title: `font-serif text-title font-medium text-navy-900`
- Section title: `font-serif text-subtitle font-medium text-navy-800`
- Card title: `font-serif text-base font-medium text-navy-900`
- Label: `.label-premium` (existing, enforce usage everywhere)

### 2.7 Empty & Loading States

**Add `.empty-state` to globals.css:**
```css
.empty-state {
  @apply flex flex-col items-center justify-center py-16 text-center;
}
.empty-state-icon { @apply w-12 h-12 text-sand-300 mb-4; }
.empty-state-title { @apply font-serif text-lg font-medium text-navy-700 mb-2; }
.empty-state-text { @apply text-sm text-navy-500 max-w-sm; }
```

**Skeleton loading:** Apply existing `.skeleton` class to Dashboard cards, Material table rows, and Analysis module cards during loading.

---

## Phase 3: Screen-Specific Refinements

### 3.1 AppShell / Navigation

- Logo "AYDI" letter-spacing: increase to `tracking-[0.12em]`
- Mobile bottom-nav: add dot indicator under active tab icon
- Breadcrumbs: chevron separator `text-sand-300`, active item `font-medium`
- Sidebar collapse button: increase touch target to min 44x44px

### 3.2 Hero / Carousel

- Dynamic overlay strength: video slides opacity 0.7, photo slides 0.5
- Domain label: crossfade transition instead of hard switch
- CTA button: add `backdrop-blur-sm` + `border border-white/20` for glassmorphism effect

### 3.3 Quick Analysis

- Step indicator line: gradient fill (sand-200 → ocean-500 → emerald-500) based on progress
- Dimensions section: subtle `bg-ocean-50/50` background to visually prioritize
- Results: Overall score card spans 2 columns on desktop, module cards in 3-col grid below

### 3.4 Dashboard

- Project cards: show mini progress ring when analysis exists
- Archived projects: `opacity-75` + subtle grayscale filter
- Consistent card class usage (`.card-premium`)

### 3.5 MaterialBrowser

- Zebra-striping: every other row `bg-sand-50/50`
- Detail panel open: light `bg-navy-950/10` overlay on table

### 3.6 Knowledge / Service Reports

- Standardize on `.card-premium` class
- Consistent header structure matching Dashboard cards

---

## Phase 4: Motion Refinement

### 4.1 Scroll-Triggered Animations

Add `IntersectionObserver`-based reveal for content sections. Elements start with `opacity: 0; transform: translateY(16px)` and animate in when 20% visible.

### 4.2 Page Transitions

Content fade-out (150ms) → fade-in (300ms) on view switch. No layout shift.

### 4.3 Tab/Filter Transitions

When switching filters (MaterialBrowser categories, Dashboard status): content fades out (150ms) then fades in (300ms).

### 4.4 Nav Hover

Sidebar nav icons: `scale(1.1)` on hover, 200ms transition.

### 4.5 Score Animations

- ScoreGauge: keep existing draw-circle (1000ms)
- Score numbers: animated count-up with `font-mono tabular-nums`
- Score bars: keep existing fill-bar (800ms)

---

## Phase 5: Accessibility (WCAG 2.1 AA)

### 5.1 Color Contrast Fixes

**Note:** `text-navy-300` and `text-sand-400` are not currently used in any component. These entries are preventive guidance — if these colors appear during implementation, use the corrected alternatives. The score color issues ARE real (defined in globals.css, applied via inline logic in components).

| Element | Current | Fix | Result |
|---------|---------|-----|--------|
| `text-navy-300` on white (preventive) | 3.4:1 FAIL | → use `text-navy-400` instead | 4.7:1 PASS |
| `text-sand-400` as label (preventive) | 2.6:1 FAIL | → use `text-sand-600` instead | 5.3:1 PASS |
| `.score-excellent` (#4ade80) | ~2.0:1 FAIL | → badge: `bg-emerald-50 text-emerald-700` | Verify exact ratio during implementation |
| `.score-good` (#86efac) | ~1.7:1 FAIL | → merge with excellent | N/A |
| `.score-acceptable` (#fbbf24) | ~1.8:1 FAIL | → badge: `bg-amber-50 text-amber-700` | Verify exact ratio during implementation |
| `.score-poor` (#f97316) | ~3.0:1 FAIL | → badge: `bg-orange-50 text-orange-700` | Verify exact ratio during implementation |

**Implementation note:** Exact contrast ratios should be verified with a contrast checker tool during implementation for each specific color pairing.

### 5.2 Score Display Redesign

Replace colored text on white with colored background badges:
```
excellent (80+):  bg-emerald-50 text-emerald-700 border-emerald-200
good (60-79):     bg-amber-50 text-amber-700 border-amber-200
poor (40-59):     bg-orange-50 text-orange-700 border-orange-200
critical (<40):   bg-red-50 text-red-700 border-red-200
```

### 5.3 Focus States

- `*:focus-visible` border-radius: change from `4px` to `inherit`
- Clickable cards: add `focus-visible:ring-2 focus-visible:ring-ocean-300`
- Sidebar nav items: add `focus-visible:bg-ocean-50`

### 5.4 Touch Targets (WCAG 2.5.8)

- Sidebar collapse button: min 44x44px
- Mobile bottom-nav tabs: min 48x48px with `gap-1`
- SpecForm stepper buttons (+/-): min 36x36px

### 5.5 Keyboard Navigation

- Dashboard project cards: `tabIndex={0}` + Enter/Space handler
- Material table rows: `role="row"` + `tabIndex={0}` + arrow key navigation

### 5.6 Screen Reader

- ScoreGauge: `aria-label={`Gesamtbewertung: ${score} von 100`}`
- ConfidenceBadge: `aria-label` on every badge
- All icon-only buttons: `aria-label` attribute

### 5.7 Reduced Motion

**Add to globals.css:**
```css
@media (prefers-reduced-motion: reduce) {
  *, *::before, *::after {
    animation-duration: 0.01ms !important;
    animation-iteration-count: 1 !important;
    transition-duration: 0.01ms !important;
  }
  /* Exception: height transitions for accordions (SpecForm sections) need non-zero duration */
  .section-expand-transition {
    transition-duration: 1ms !important;
  }
}
```

**Note:** The blanket `!important` override is intentionally aggressive for accessibility. The `.section-expand-transition` exception preserves accordion usability where instant height changes would be disorienting.

---

## Files Affected

### Modified (Foundation — Phase 1):
- `frontend/tailwind.config.js` — new tokens (typography, shadows, spacing, radii, easings)
- `frontend/src/styles/globals.css` — centralized animations, component classes, a11y, reduced-motion

### Modified (Inline styles removal + color fixes — Phase 1.1 & 2.1):
- `frontend/src/components/dashboard/Dashboard.tsx` — remove inline @keyframes (4), fix hardcoded cyan
- `frontend/src/components/dashboard/ProjectDetail.tsx` — remove inline @keyframes (3)
- `frontend/src/components/quick/QuickAnalysis.tsx` — remove inline @keyframes (5), fix hardcoded cyan
- `frontend/src/components/quick/QuickResults.tsx` — remove inline @keyframes (5), fix hardcoded cyan
- `frontend/src/components/quick/SpecForm.tsx` — remove inline @keyframes (5), fix hardcoded cyan
- `frontend/src/components/materials/MaterialBrowser.tsx` — remove inline @keyframes (5), fix hardcoded cyan
- `frontend/src/components/images/ImageUpload.tsx` — remove inline @keyframes (4), fix hardcoded cyan
- `frontend/src/components/analysis/FullAnalysisView.tsx` — remove inline @keyframes (2)
- `frontend/src/components/analysis/ConfidenceBadge.tsx` — remove inline @keyframes (1), badge classes, aria-label
- `frontend/src/components/analysis/WarningList.tsx` — remove inline @keyframes (2), card consistency
- `frontend/src/components/analysis/SubScoreBars.tsx` — remove inline @keyframes (1), score color tokens
- `frontend/src/components/analysis/ScoreGauge.tsx` — remove inline @keyframes (1), aria-label
- `frontend/src/components/layout/HeroCarousel.tsx` — remove inline @keyframes (1), domain label crossfade
- `frontend/src/components/layout/HeroSection.tsx` — remove inline @keyframes (1), overlay, CTA
- `frontend/src/components/service/ServiceReportList.tsx` — remove inline @keyframes (3), card consistency
- `frontend/src/components/knowledge/KnowledgeDetail.tsx` — remove inline @keyframes (4), card consistency
- `frontend/src/pages/KnowledgePage.tsx` — remove inline @keyframes (4), card consistency

### Modified (Screen polish + a11y — Phases 3-5):
- `frontend/src/components/layout/AppShell.tsx` — nav polish, touch targets, keyboard nav
- `frontend/src/components/images/FusedScoreCard.tsx` — score color tokens
- `frontend/src/components/images/VisualResults.tsx` — card consistency

### Verify for consistency (may need minor updates):
- `frontend/src/components/quick/UpgradePrompt.tsx` — card/badge consistency check
- `frontend/src/components/costs/CostOverview.tsx` — card consistency check
- `frontend/src/components/compare/DiffViewer.tsx` — card class alignment only; its emerald/amber colors are intentional diff semantics (added/changed), NOT score colors — do not change
- `frontend/src/components/dashboard/ProjectCreate.tsx` — inline styles check

### Not Modified:
- `frontend/src/components/viewer3d/*` — 3D viewer untouched
- `frontend/src/services/*` — no API changes
- `frontend/src/types/*` — no type changes
- Backend — completely untouched

---

## Success Criteria

1. Zero hardcoded `rgba(0, 176, 240, ...)` values — all use Ocean tokens
2. Zero inline `<style>` blocks — all animations in globals.css
3. All text passes WCAG 2.1 AA contrast (4.5:1 normal, 3:1 large)
4. All interactive elements have focus-visible states
5. All touch targets >= 44px on mobile
6. `prefers-reduced-motion` respected
7. Consistent card, button, badge, and label styling across all screens
8. No visual regressions — app looks better, not different
