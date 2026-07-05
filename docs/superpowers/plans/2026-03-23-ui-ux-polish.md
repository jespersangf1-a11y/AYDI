> **⚠️ ARCHIV — HISTORISCHER PLANUNGSSTAND (nicht maßgeblich).**
> Dieses Dokument beschreibt einen früheren Planungs-/Design-Stand und trackt den aktuellen Code **nicht**.
> Bekannte Drift: 4 statt real **13 Bootsklassen** (`BoatClass`-Enum); abweichende Sub-Analysen/Gewichte; einzelne enthaltene Tests schlagen gegen den Ist-Code fehl.
> **Maßgeblich ist `CLAUDE.md`** (plus der Code). Nicht zum Ableiten von Enums, Return-Contracts oder Tests verwenden.

# AYDI UI/UX Polish Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Evolutionary UI/UX polish across all AYDI frontend screens — tokens, components, motion, accessibility.

**Architecture:** Component-First approach. Update design tokens in tailwind.config.js first, then centralize animations in globals.css, then polish individual screens. Changes propagate through tokens so edits to foundation files automatically improve all screens.

**Tech Stack:** React 18, TypeScript, Tailwind CSS 3.4, Vite 6

**Spec:** `docs/superpowers/specs/2026-03-22-ui-ux-polish-design.md`

---

## File Structure

### Foundation (modified):
- `frontend/tailwind.config.js` — add typography, shadow, spacing, radius, easing tokens
- `frontend/src/styles/globals.css` — centralized animations, component classes, a11y

### Components (modified — inline styles removed):
- `frontend/src/components/dashboard/Dashboard.tsx` (180 lines, inline styles L21-73)
- `frontend/src/components/dashboard/ProjectDetail.tsx` (465 lines, inline styles L14-57)
- `frontend/src/components/quick/QuickAnalysis.tsx` (330 lines, inline styles L20-101)
- `frontend/src/components/quick/QuickResults.tsx` (315 lines, inline styles L14-77)
- `frontend/src/components/quick/SpecForm.tsx` (647 lines, inline styles L20-100)
- `frontend/src/components/materials/MaterialBrowser.tsx` (404 lines, inline styles L21-114)
- `frontend/src/components/images/ImageUpload.tsx` (390 lines, inline styles L21-70)
- `frontend/src/components/analysis/FullAnalysisView.tsx` (349 lines, inline styles L321-345)
- `frontend/src/components/analysis/ConfidenceBadge.tsx` (118 lines, inline styles L99-114)
- `frontend/src/components/analysis/WarningList.tsx` (113 lines, inline styles L76-109)
- `frontend/src/components/analysis/SubScoreBars.tsx` (115 lines, inline styles L100-111)
- `frontend/src/components/analysis/ScoreGauge.tsx` (185 lines, inline styles L170-181)
- `frontend/src/components/layout/HeroCarousel.tsx` (236 lines, inline styles L227-232)
- `frontend/src/components/layout/HeroSection.tsx` (141 lines, inline styles L126-137)
- `frontend/src/components/service/ServiceReportList.tsx` (328 lines, inline styles L10-55)
- `frontend/src/components/knowledge/KnowledgeDetail.tsx` (360 lines, inline styles L5-82)
- `frontend/src/pages/KnowledgePage.tsx` (519 lines, inline styles L14-72)

### Screen polish (modified):
- `frontend/src/components/layout/AppShell.tsx` (192 lines, no inline styles)
- `frontend/src/components/images/FusedScoreCard.tsx` (120 lines)
- `frontend/src/components/images/VisualResults.tsx`

### Verify only:
- `frontend/src/components/quick/UpgradePrompt.tsx`
- `frontend/src/components/costs/CostOverview.tsx`
- `frontend/src/components/compare/DiffViewer.tsx` (diff colors are intentional — don't change)
- `frontend/src/components/dashboard/ProjectCreate.tsx`

---

## Task 1: Tailwind Token Foundation

**Files:**
- Modify: `frontend/tailwind.config.js`

- [ ] **Step 1: Add typography scale tokens**

In `tailwind.config.js`, inside `theme.extend.fontSize`, add after the `title` entry:

```js
'subtitle': ['1.25rem', { lineHeight: '1.35', letterSpacing: '-0.005em' }],
'body-lg': ['1.0625rem', { lineHeight: '1.6' }],
```

- [ ] **Step 2: Add shadow token**

In `theme.extend.boxShadow`, add:

```js
'card-rest': '0 1px 3px rgba(11, 18, 32, 0.04), 0 1px 2px rgba(11, 18, 32, 0.06)',
```

- [ ] **Step 3: Add spacing tokens**

Add new `spacing` key inside `theme.extend`:

```js
spacing: {
  'section': '4rem',
  'section-lg': '6rem',
},
```

- [ ] **Step 4: Add border radius tokens**

Add new `borderRadius` key inside `theme.extend`:

```js
borderRadius: {
  'card': '14px',
  'button': '10px',
  'badge': '8px',
},
```

- [ ] **Step 5: Add transition easing tokens**

Add new `transitionTimingFunction` key inside `theme.extend`:

```js
transitionTimingFunction: {
  'premium': 'cubic-bezier(0.4, 0, 0.2, 1)',
  'bounce': 'cubic-bezier(0.34, 1.56, 0.64, 1)',
},
```

- [ ] **Step 6: Add new animation entries to tailwind.config.js**

**Note on duplication:** All @keyframes are defined ONLY in tailwind.config.js. The globals.css file will contain only the `.animate-*` utility classes that reference them. Existing @keyframes already in globals.css (fade-in-up, fade-in-scale, etc.) should be REMOVED from globals.css in Task 2 since they are also defined in tailwind.config.js. Tailwind generates the keyframes from the config automatically.

In `theme.extend.animation`, add:

```js
'slide-down': 'slide-down 0.3s ease-out both',
'shake': 'shake 0.4s ease-out',
'section-expand': 'section-expand 0.3s ease-out both',
'section-collapse': 'section-collapse 0.2s ease-out both',
'slide-out-right': 'slide-out-right 0.3s cubic-bezier(0.4, 0, 0.2, 1) both',
'backdrop-fade': 'backdrop-fade 0.3s ease-out both',
'count-up': 'count-up 0.6s ease-out both',
```

In `theme.extend.keyframes`, add:

```js
'slide-down': {
  'from': { opacity: '0', transform: 'translateY(-8px)' },
  'to': { opacity: '1', transform: 'translateY(0)' },
},
'shake': {
  '0%, 100%': { transform: 'translateX(0)' },
  '25%': { transform: 'translateX(-4px)' },
  '50%': { transform: 'translateX(4px)' },
  '75%': { transform: 'translateX(-2px)' },
},
'section-expand': {
  'from': { 'grid-template-rows': '0fr', opacity: '0' },
  'to': { 'grid-template-rows': '1fr', opacity: '1' },
},
'section-collapse': {
  'from': { 'grid-template-rows': '1fr', opacity: '1' },
  'to': { 'grid-template-rows': '0fr', opacity: '0' },
},
'slide-out-right': {
  'from': { opacity: '1', transform: 'translateX(0)' },
  'to': { opacity: '0', transform: 'translateX(100%)' },
},
'backdrop-fade': {
  'from': { opacity: '0' },
  'to': { opacity: '1' },
},
'count-up': {
  'from': { opacity: '0' },
  'to': { opacity: '1' },
},
```

- [ ] **Step 7: Verify build**

Run: `cd frontend && npx vite build 2>&1 | tail -5`
Expected: Build succeeds with no errors.

- [ ] **Step 8: Commit**

```bash
git add frontend/tailwind.config.js
git commit -m "feat(ui): add design token foundation — typography, shadows, spacing, radii, easings, animations"
```

---

## Task 2: Centralized Animations & Component Classes in globals.css

**Files:**
- Modify: `frontend/src/styles/globals.css`

- [ ] **Step 1: Clean up duplicate @keyframes and add new ones**

First, REMOVE the existing @keyframes blocks from globals.css (lines 6-51) that are already defined in tailwind.config.js: `fade-in-up`, `fade-in-scale`, `slide-in-right`, `slide-in-left`, `count-up`, `shimmer`, `pulse-glow`, `draw-circle`, `fill-bar`. Tailwind generates these from the config. Only keep @keyframes that are NOT in the config.

Then add these NEW @keyframes that are not in tailwind.config.js (for the utility classes below):

```css
/* Slide down for dropdowns/accordions */
@keyframes slide-down {
  from { opacity: 0; transform: translateY(-8px); }
  to { opacity: 1; transform: translateY(0); }
}

/* Form validation shake */
@keyframes shake {
  0%, 100% { transform: translateX(0); }
  25% { transform: translateX(-4px); }
  50% { transform: translateX(4px); }
  75% { transform: translateX(-2px); }
}

/* Accordion expand using grid technique */
@keyframes section-expand {
  from { grid-template-rows: 0fr; opacity: 0; }
  to { grid-template-rows: 1fr; opacity: 1; }
}

@keyframes section-collapse {
  from { grid-template-rows: 1fr; opacity: 1; }
  to { grid-template-rows: 0fr; opacity: 0; }
}

/* Panel dismiss */
@keyframes slide-out-right {
  from { opacity: 1; transform: translateX(0); }
  to { opacity: 0; transform: translateX(100%); }
}

/* Overlay fade */
@keyframes backdrop-fade {
  from { opacity: 0; }
  to { opacity: 1; }
}

/* Score number reveal */
@keyframes count-up {
  from { opacity: 0; }
  to { opacity: 1; }
}
```

- [ ] **Step 2: Add animation utility classes**

After the existing `.animate-fill-bar` class, add:

```css
.animate-slide-down { animation: slide-down 0.3s ease-out both; }
.animate-shake { animation: shake 0.4s ease-out; }
.animate-section-expand { animation: section-expand 0.3s ease-out both; }
.animate-section-collapse { animation: section-collapse 0.2s ease-out both; }
.animate-slide-out-right { animation: slide-out-right 0.3s cubic-bezier(0.4, 0, 0.2, 1) both; }
.animate-backdrop-fade { animation: backdrop-fade 0.3s ease-out both; }
.animate-count-up { animation: count-up 0.6s ease-out both; }
```

- [ ] **Step 3: Update score color classes**

Replace the existing `.score-*` block (lines 122-126) with:

```css
/* Score colors — WCAG AA compliant */
.score-excellent { @apply text-emerald-600; }
.score-acceptable { @apply text-amber-600; }
.score-poor { @apply text-orange-600; }
.score-critical { @apply text-red-600; }
```

- [ ] **Step 4: Replace .card-premium class**

Replace the existing `.card-premium` block (lines 108-114) with:

```css
/* Card system */
.card-premium {
  @apply bg-white border border-sand-200;
  box-shadow: theme('boxShadow.card-rest');
  border-radius: theme('borderRadius.card');
  transition: all 300ms theme('transitionTimingFunction.premium');
}
.card-premium:hover {
  @apply border-navy-100;
  box-shadow: theme('boxShadow.card-hover');
  transform: translateY(-6px);
}
.card-premium--compact:hover { transform: translateY(-4px); }
.card-premium--featured:hover { transform: translateY(-8px); }
```

- [ ] **Step 5: Add button system**

After `.card-premium`, add:

```css
/* Button system */
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

- [ ] **Step 6: Add badge system**

```css
/* Badge system */
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

- [ ] **Step 7: Add input focus, empty state, and label consistency**

```css
/* Consistent input focus */
input:focus, select:focus, textarea:focus {
  @apply ring-2 ring-ocean-300 border-ocean-400 outline-none;
}

/* Empty state */
.empty-state {
  @apply flex flex-col items-center justify-center py-16 text-center;
}
.empty-state-icon { @apply w-12 h-12 text-sand-300 mb-4; }
.empty-state-title { @apply font-serif text-lg font-medium text-navy-700 mb-2; }
.empty-state-text { @apply text-sm text-navy-500 max-w-sm; }
```

- [ ] **Step 8: Add accessibility — focus-visible fix + reduced motion**

Update the existing `*:focus-visible` rule (line 79) — change `border-radius: 4px` to `border-radius: inherit`:

```css
*:focus-visible {
  outline: 2px solid rgba(45, 139, 168, 0.7);
  outline-offset: 2px;
  border-radius: inherit;
}
```

Add at the end of the file (after `@layer components`):

```css
/* Reduced motion preference */
@media (prefers-reduced-motion: reduce) {
  *, *::before, *::after {
    animation-duration: 0.01ms !important;
    animation-iteration-count: 1 !important;
    transition-duration: 0.01ms !important;
  }
  .section-expand-transition {
    transition-duration: 1ms !important;
  }
}
```

- [ ] **Step 9: Verify build**

Run: `cd frontend && npx vite build 2>&1 | tail -5`
Expected: Build succeeds.

- [ ] **Step 10: Commit**

```bash
git add frontend/src/styles/globals.css
git commit -m "feat(ui): centralize animations, add component classes, score colors, a11y"
```

---

## Task 3: Remove Inline Styles — Batch 1 (Dashboard, QuickResults, QuickAnalysis)

**Files:**
- Modify: `frontend/src/components/dashboard/Dashboard.tsx` (inline styles L21-73)
- Modify: `frontend/src/components/quick/QuickResults.tsx` (inline styles L14-77)
- Modify: `frontend/src/components/quick/QuickAnalysis.tsx` (inline styles L20-101)

For each file:

- [ ] **Step 1: Dashboard.tsx — remove inline styles and fix cyan colors**

1. Delete the `const dashboardAnimationStyles` template string (lines 21-73)
2. Delete the `<style>{dashboardAnimationStyles}</style>` JSX element
3. Replace all `rgba(0, 176, 240, 0.2)` with `rgba(45, 139, 168, 0.2)`
4. Replace all `rgba(0, 176, 240, 0.4)` with `rgba(45, 139, 168, 0.4)`
5. Replace CSS class references:
   - `animate-project-in` → `animate-fade-in-up`
   - `animate-empty-float` → remove (static icon, no infinite animation)
   - `animate-status-pulse` → remove (static badge)
   - `animate-icon-bounce` → remove (static icon)
   - `card-hover-lift` → `card-premium`

- [ ] **Step 2: QuickResults.tsx — remove inline styles and fix cyan colors**

1. Delete `const resultsAnimationStyles` (lines 14-77)
2. Delete the `<style>{resultsAnimationStyles}</style>` JSX element
3. Replace `rgba(0, 176, 240, ...)` with `rgba(45, 139, 168, ...)` (2 occurrences)
4. Replace CSS class references:
   - `animate-fade-in-up` → already exists in globals.css (keep)
   - `animate-module-in` → `animate-fade-in-up`
   - `module-card-hover` → `card-premium`
   - `skeleton-loading` → `skeleton`

- [ ] **Step 3: QuickAnalysis.tsx — remove inline styles and fix cyan colors**

1. Delete `const stepAnimationStyles` (lines 20-101)
2. Delete the `<style>{stepAnimationStyles}</style>` JSX element
3. Replace all `rgba(0, 176, 240, ...)` with `rgba(45, 139, 168, ...)` (5 occurrences)
4. Replace CSS class references:
   - Inline slide animations → `animate-slide-in-right` / `animate-slide-in-left`
   - `stepPulse` animation → `animate-pulse-glow` (already in globals)
   - `cardStaggered` → `animate-fade-in-up` with stagger classes
   - `checkmarkScale` → `animate-fade-in-scale`

- [ ] **Step 4: Verify build**

Run: `cd frontend && npx vite build 2>&1 | tail -5`

- [ ] **Step 5: Commit**

```bash
git add frontend/src/components/dashboard/Dashboard.tsx frontend/src/components/quick/QuickResults.tsx frontend/src/components/quick/QuickAnalysis.tsx
git commit -m "refactor(ui): remove inline styles from Dashboard, QuickResults, QuickAnalysis — use global animations"
```

---

## Task 4: Remove Inline Styles — Batch 2 (SpecForm, MaterialBrowser, ImageUpload)

**Files:**
- Modify: `frontend/src/components/quick/SpecForm.tsx` (inline styles L20-100)
- Modify: `frontend/src/components/materials/MaterialBrowser.tsx` (inline styles L21-114)
- Modify: `frontend/src/components/images/ImageUpload.tsx` (inline styles L21-70)

- [ ] **Step 1: SpecForm.tsx — remove inline styles and fix cyan colors**

1. Delete `const sectionAnimationStyles` (lines 20-100)
2. Delete the `<style>{sectionAnimationStyles}</style>` JSX element
3. Replace `rgba(0, 176, 240, ...)` with `rgba(45, 139, 168, ...)` (3 occurrences)
4. Replace CSS class references:
   - Section expand/collapse → use `animate-section-expand` / `animate-section-collapse` classes
   - `shake` → `animate-shake`
   - `focusGlow` → handled by globals.css input focus rule
   - `errorSlideIn` → `animate-slide-down`
   - Wrap collapsible content in grid container for section-expand technique: `<div style={{display:'grid'}}><div style={{overflow:'hidden',minHeight:0}}>...</div></div>`

- [ ] **Step 2: MaterialBrowser.tsx — remove inline styles and fix cyan colors**

1. Delete `const materialBrowserAnimationStyles` (lines 21-114)
2. Delete the `<style>{materialBrowserAnimationStyles}</style>` JSX element
3. Replace `rgba(0, 176, 240, ...)` with `rgba(45, 139, 168, ...)` (2 occurrences)
4. Replace CSS class references:
   - `table-row-hover` → use Tailwind `hover:bg-ocean-50/10 transition-colors duration-300`
   - Panel slide in → `animate-slide-in-right`
   - Panel slide out → `animate-slide-out-right`
   - `mobileOverlayFadeIn` → `animate-backdrop-fade`
   - `filterTransition` → `animate-fade-in-up`

- [ ] **Step 3: ImageUpload.tsx — remove inline styles and fix cyan colors**

1. Delete `const imageUploadAnimationStyles` (lines 21-70)
2. Delete the `<style>{imageUploadAnimationStyles}</style>` JSX element
3. Replace `rgba(0, 176, 240, ...)` with `rgba(45, 139, 168, ...)` (4 occurrences)
4. Replace CSS class references:
   - `dragBorderPulse` → `animate-pulse-glow` (already in globals)
   - `previewScaleIn` → `animate-fade-in-scale`
   - `progressFill` → `animate-fill-bar`
   - `uploadPulse` → `animate-pulse-glow`

- [ ] **Step 4: Verify build**

Run: `cd frontend && npx vite build 2>&1 | tail -5`

- [ ] **Step 5: Commit**

```bash
git add frontend/src/components/quick/SpecForm.tsx frontend/src/components/materials/MaterialBrowser.tsx frontend/src/components/images/ImageUpload.tsx
git commit -m "refactor(ui): remove inline styles from SpecForm, MaterialBrowser, ImageUpload"
```

---

## Task 5: Remove Inline Styles — Batch 3 (Analysis components)

**Files:**
- Modify: `frontend/src/components/analysis/FullAnalysisView.tsx` (inline styles L321-345)
- Modify: `frontend/src/components/analysis/ConfidenceBadge.tsx` (inline styles L99-114)
- Modify: `frontend/src/components/analysis/WarningList.tsx` (inline styles L76-109)
- Modify: `frontend/src/components/analysis/SubScoreBars.tsx` (inline styles L100-111)
- Modify: `frontend/src/components/analysis/ScoreGauge.tsx` (inline styles L170-181)

- [ ] **Step 1: FullAnalysisView.tsx**

1. Delete inline `<style>` block (lines 321-345)
2. Replace class references: `slideIn` → `animate-slide-in-right`, `fadeIn` → `animate-fade-in`

- [ ] **Step 2: ConfidenceBadge.tsx**

1. Delete inline `<style>` block (lines 99-114)
2. Replace: `fadeInScale` → `animate-fade-in-scale`
3. Add `aria-label` attribute to each badge with descriptive text

- [ ] **Step 3: WarningList.tsx**

1. Delete inline `<style>` block (lines 76-109)
2. Replace: `slideIn` → `animate-slide-in-right`, `slideDown` → `animate-slide-down`

- [ ] **Step 4: SubScoreBars.tsx**

1. Delete inline `<style>` block (lines 100-111)
2. Replace: `slideIn` → `animate-slide-in-right`
3. Update score color logic: replace any `text-emerald-400` → `text-emerald-600`, `text-amber-400` → `text-amber-600`, `text-orange-400` → `text-orange-600`

- [ ] **Step 5: ScoreGauge.tsx**

1. Delete inline `<style>` block (lines 170-181)
2. Replace: `fadeIn` → `animate-fade-in`
3. Add `aria-label={`Gesamtbewertung: ${score} von 100`}` to the root SVG/container
4. Update SVG gradient stop hex values:
   - Excellent: `#059669` / `#34d399`
   - Acceptable: `#d97706` / `#fbbf24`
   - Poor: `#ea580c` / `#fb923c`
   - Critical: `#dc2626` / `#f87171`

- [ ] **Step 6: Verify build**

Run: `cd frontend && npx vite build 2>&1 | tail -5`

- [ ] **Step 7: Commit**

```bash
git add frontend/src/components/analysis/
git commit -m "refactor(ui): remove inline styles from analysis components, fix score colors, add aria-labels"
```

---

## Task 6: Remove Inline Styles — Batch 4 (Layout, Service, Knowledge)

**Files:**
- Modify: `frontend/src/components/layout/HeroCarousel.tsx` (inline styles L227-232)
- Modify: `frontend/src/components/layout/HeroSection.tsx` (inline styles L126-137)
- Modify: `frontend/src/components/dashboard/ProjectDetail.tsx` (inline styles L14-57)
- Modify: `frontend/src/components/service/ServiceReportList.tsx` (inline styles L10-55)
- Modify: `frontend/src/components/knowledge/KnowledgeDetail.tsx` (inline styles L5-82)
- Modify: `frontend/src/pages/KnowledgePage.tsx` (inline styles L14-72)

- [ ] **Step 1: HeroCarousel.tsx**

1. Delete inline `<style>` block (lines 227-232)
2. Replace: `fadeInUp` → `animate-fade-in-up`
3. Add crossfade transition for domain label: wrap label in element with `transition-opacity duration-500`
4. **Dynamic overlay strength**: Add conditional overlay opacity based on slide type. If current slide is a video, overlay opacity = 0.7; if photo, overlay opacity = 0.5. Pass this as a style prop or conditional class to the overlay div (e.g., `className={isVideo ? 'bg-navy-950/70' : 'bg-navy-950/50'}`)

- [ ] **Step 2: HeroSection.tsx**

1. Delete inline `<style>` block (lines 126-137)
2. Replace: `fadeInUp` → `animate-fade-in-up`
3. Add glassmorphism to CTA button: `backdrop-blur-sm border border-white/20`

- [ ] **Step 3: ProjectDetail.tsx**

1. Delete `const ANIMATIONS` (lines 14-57)
2. Delete `<style>{ANIMATIONS}</style>` JSX element
3. Replace: `fadeInUp` → `animate-fade-in-up`, `slideInLeft` → `animate-slide-in-left`, `slideUnderline` → remove or use CSS transition

- [ ] **Step 4: ServiceReportList.tsx**

1. Delete `const ANIMATIONS` (lines 10-55)
2. Delete `<style>{ANIMATIONS}</style>` JSX element
3. Replace: `fadeInUp` → `animate-fade-in-up`, `slideDown` → `animate-slide-down`, `borderGlow` → `animate-pulse-glow` or remove

- [ ] **Step 5: KnowledgeDetail.tsx**

1. Delete `const ANIMATIONS` (lines 5-82)
2. Delete `<style>{ANIMATIONS}</style>` JSX element
3. Replace `rgba(6, 182, 212, 0.05)` with `rgba(45, 139, 168, 0.05)` (line 80)
4. Replace: `slideInRight` → `animate-slide-in-right`, `slideOutRight` → `animate-slide-out-right`, `backdropFade` → `animate-backdrop-fade`, `fadeInUp` → `animate-fade-in-up`

- [ ] **Step 6: KnowledgePage.tsx**

1. Delete `const ANIMATIONS` (lines 14-72)
2. Delete `<style>{ANIMATIONS}</style>` JSX element
3. Replace `rgba(6, 182, 212, ...)` with `rgba(45, 139, 168, ...)` (2 occurrences)
4. Replace: `fadeInUp` → `animate-fade-in-up`, `slideDown` → `animate-slide-down`, `ocnglow` → remove, `pulse-glow` → `animate-pulse-glow`

- [ ] **Step 7: Verify build**

Run: `cd frontend && npx vite build 2>&1 | tail -5`

- [ ] **Step 8: Commit**

```bash
git add frontend/src/components/layout/ frontend/src/components/dashboard/ProjectDetail.tsx frontend/src/components/service/ frontend/src/components/knowledge/ frontend/src/pages/
git commit -m "refactor(ui): remove inline styles from layout, service, knowledge components"
```

---

## Task 7: Screen Polish — AppShell Navigation

**Files:**
- Modify: `frontend/src/components/layout/AppShell.tsx`

- [ ] **Step 1: Polish sidebar**

1. Logo "AYDI": change `tracking-wide-premium` to `tracking-[0.12em]`
2. Sidebar collapse button: increase touch target — add `min-w-[44px] min-h-[44px]` and center the icon
3. Nav items: add `focus-visible:bg-ocean-50 focus-visible:ring-0 focus-visible:outline-none`
4. Nav icon hover: add `group` to nav item, icon gets `group-hover:scale-110 transition-transform duration-200`

- [ ] **Step 2: Polish mobile bottom-nav**

1. Active tab: add a small dot indicator: `<div className="w-1 h-1 rounded-full bg-ocean-500 mt-0.5" />`
2. Tab touch targets: ensure min 48×48px with `min-w-[48px] min-h-[48px]`
3. Add `gap-1` between tabs

- [ ] **Step 3: Polish breadcrumbs**

1. Chevron separator: `text-sand-300`
2. Active breadcrumb item: `font-medium`

- [ ] **Step 4: Verify build**

Run: `cd frontend && npx vite build 2>&1 | tail -5`

- [ ] **Step 5: Commit**

```bash
git add frontend/src/components/layout/AppShell.tsx
git commit -m "feat(ui): polish AppShell — nav hover, touch targets, mobile dot indicator, breadcrumbs"
```

---

## Task 8: Screen Polish — Quick Analysis Flow

**Files:**
- Modify: `frontend/src/components/quick/QuickAnalysis.tsx`
- Modify: `frontend/src/components/quick/QuickResults.tsx`
- Modify: `frontend/src/components/quick/SpecForm.tsx`

- [ ] **Step 1: Step indicator gradient**

In QuickAnalysis.tsx, update the step indicator progress line to use a gradient:
- Completed segments: `bg-gradient-to-r from-ocean-500 to-emerald-500`
- Current segment: `bg-ocean-500`
- Upcoming: `bg-sand-200`

- [ ] **Step 2: SpecForm dimensions section highlight + stepper touch targets**

1. Add subtle `bg-ocean-50/50` background and `border-l-2 border-ocean-300` to the Dimensions section to visually prioritize it.
2. **Touch targets**: Find the +/- stepper buttons in SpecForm.tsx and ensure they have `min-w-[36px] min-h-[36px]` for accessible touch targets.

- [ ] **Step 3: Results layout — score card span-2 + font-mono scores**

1. In QuickResults.tsx, make the overall score card `col-span-2` on desktop (`md:col-span-2`), with module cards in a 3-column grid below.
2. Add `font-mono tabular-nums` to all score number elements in QuickResults.tsx for proper numerical alignment.

- [ ] **Step 4: FusedScoreCard + ScoreGauge font-mono scores**

1. In `frontend/src/components/images/FusedScoreCard.tsx`, update score color logic to use WCAG-compliant colors (emerald-600, amber-600, orange-600, red-600).
2. In ScoreGauge.tsx, ensure score numbers use `font-mono tabular-nums`.

- [ ] **Step 5: Verify build**

Run: `cd frontend && npx vite build 2>&1 | tail -5`

- [ ] **Step 6: Commit**

```bash
git add frontend/src/components/quick/ frontend/src/components/images/FusedScoreCard.tsx
git commit -m "feat(ui): polish Quick Analysis — step gradient, dimensions highlight, results layout, score colors"
```

---

## Task 9: Screen Polish — Dashboard & Remaining Screens

**Files:**
- Modify: `frontend/src/components/dashboard/Dashboard.tsx`
- Modify: `frontend/src/components/materials/MaterialBrowser.tsx`
- Modify: `frontend/src/components/service/ServiceReportList.tsx`
- Modify: `frontend/src/pages/KnowledgePage.tsx`
- Modify: `frontend/src/components/images/VisualResults.tsx`

- [ ] **Step 1: Dashboard — archived projects + mini progress ring**

1. Add `opacity-75 grayscale-[30%]` to project cards with `status === 'archived'`.
2. **Mini progress ring**: When a project has analysis data (score available), render a small (24×24px) SVG circle showing the overall score as a filled arc, using the same color scale as ScoreGauge (emerald/amber/orange/red). Place it in the top-right corner of the project card.

- [ ] **Step 2: Dashboard — keyboard navigation**

Add `tabIndex={0}` and `onKeyDown` handler (Enter/Space triggers `onSelectProject`) to each project card. Add `focus-visible:ring-2 focus-visible:ring-ocean-300` class.

- [ ] **Step 3: MaterialBrowser — zebra striping + keyboard navigation**

1. Add `even:bg-sand-50/50` to table rows. When detail panel is open, add `bg-navy-950/10` overlay div over the table area.
2. **Keyboard navigation**: Add `role="row"` and `tabIndex={0}` to each table row. Add `onKeyDown` handler: Enter/Space opens detail panel, ArrowDown/ArrowUp moves focus to next/previous row.

- [ ] **Step 4: ServiceReportList & KnowledgePage — card consistency + section headers**

1. Replace any inline card styling with `.card-premium` class.
2. **Section header hierarchy audit**: Update headers to match the standardized hierarchy:
   - Page titles: `font-serif text-title font-medium text-navy-900`
   - Section titles: `font-serif text-subtitle font-medium text-navy-800`
   - Card titles: `font-serif text-base font-medium text-navy-900`
   - Labels: `.label-premium` class

- [ ] **Step 5: VisualResults — card consistency**

Apply `.card-premium` class to result cards.

- [ ] **Step 6: Skeleton loading states**

1. In Dashboard.tsx, add skeleton cards (3-6 `.skeleton` divs matching card dimensions) during `loading` state.
2. In MaterialBrowser.tsx, add skeleton table rows (5-8 `.skeleton` bars) during loading.
3. In QuickResults.tsx, add skeleton module cards during loading (if applicable).

- [ ] **Step 7: Icon-only button aria-labels sweep**

Audit and add `aria-label` to all icon-only buttons:
- AppShell.tsx: sidebar collapse toggle, mobile nav icons
- MaterialBrowser.tsx: filter/close buttons
- Any other icon-only buttons found during audit

- [ ] **Step 8: Verify build**

Run: `cd frontend && npx vite build 2>&1 | tail -5`

- [ ] **Step 9: Commit**

```bash
git add frontend/src/components/dashboard/Dashboard.tsx frontend/src/components/materials/MaterialBrowser.tsx frontend/src/components/service/ frontend/src/pages/KnowledgePage.tsx frontend/src/components/images/VisualResults.tsx frontend/src/components/layout/AppShell.tsx
git commit -m "feat(ui): polish Dashboard, MaterialBrowser, Service, Knowledge — cards, a11y, skeleton, keyboard nav"
```

---

## Task 10: Motion Refinement — Scroll Reveal, Page Transitions, Filter Transitions

**Files:**
- Create: `frontend/src/hooks/useScrollReveal.ts`
- Modify: `frontend/src/App.tsx`
- Modify: `frontend/src/components/layout/AppShell.tsx`
- Modify: `frontend/src/components/materials/MaterialBrowser.tsx`
- Modify: `frontend/src/components/dashboard/Dashboard.tsx`

- [ ] **Step 1: Create useScrollReveal hook**

Create `frontend/src/hooks/useScrollReveal.ts`:

```ts
import { useEffect, useRef } from 'react'

export function useScrollReveal<T extends HTMLElement>(threshold = 0.2) {
  const ref = useRef<T>(null)

  useEffect(() => {
    const el = ref.current
    if (!el) return

    el.style.opacity = '0'
    el.style.transform = 'translateY(16px)'
    el.style.transition = 'opacity 0.5s ease-out, transform 0.5s ease-out'

    const observer = new IntersectionObserver(
      ([entry]) => {
        if (entry.isIntersecting) {
          el.style.opacity = '1'
          el.style.transform = 'translateY(0)'
          observer.unobserve(el)
        }
      },
      { threshold }
    )

    observer.observe(el)
    return () => observer.disconnect()
  }, [threshold])

  return ref
}
```

- [ ] **Step 2: Apply scroll reveal to content sections**

Import `useScrollReveal` in key pages and apply to major content sections:
- QuickResults.tsx: module cards grid
- Dashboard.tsx: project cards grid
- KnowledgePage.tsx: knowledge sections
- MaterialBrowser.tsx: table container

Usage: `const sectionRef = useScrollReveal<HTMLDivElement>()` then `<div ref={sectionRef}>...</div>`

- [ ] **Step 3: Page transitions in App.tsx**

In App.tsx, wrap the view-switching logic with a fade transition. When `currentView` changes:
1. Set a `transitioning` state to true
2. Apply `opacity-0 transition-opacity duration-150` to content
3. After 150ms, update the view and apply `opacity-100 transition-opacity duration-300`

```tsx
const [transitioning, setTransitioning] = useState(false)
const [displayView, setDisplayView] = useState(currentView)

useEffect(() => {
  if (currentView !== displayView) {
    setTransitioning(true)
    const timer = setTimeout(() => {
      setDisplayView(currentView)
      setTransitioning(false)
    }, 150)
    return () => clearTimeout(timer)
  }
}, [currentView])
```

Wrap content: `<div className={`transition-opacity ${transitioning ? 'opacity-0 duration-150' : 'opacity-100 duration-300'}`}>`

- [ ] **Step 4: Tab/filter transitions**

In MaterialBrowser.tsx and Dashboard.tsx, when filter/status changes:
1. Set `filterTransitioning` state
2. Fade content out (150ms opacity-0), update filter, fade in (300ms opacity-100)

Same pattern as page transitions but scoped to the content area below the filters.

- [ ] **Step 5: Verify build**

Run: `cd frontend && npx vite build 2>&1 | tail -5`

- [ ] **Step 6: Commit**

```bash
git add frontend/src/hooks/useScrollReveal.ts frontend/src/App.tsx frontend/src/components/layout/AppShell.tsx frontend/src/components/materials/MaterialBrowser.tsx frontend/src/components/dashboard/Dashboard.tsx
git commit -m "feat(ui): add scroll reveal, page transitions, filter transitions"
```

---

## Task 11: Verify & Consistency Check

**Files:**
- Check: `frontend/src/components/quick/UpgradePrompt.tsx`
- Check: `frontend/src/components/costs/CostOverview.tsx`
- Check: `frontend/src/components/compare/DiffViewer.tsx`
- Check: `frontend/src/components/dashboard/ProjectCreate.tsx`

- [ ] **Step 1: Check UpgradePrompt.tsx**

Read file. If it has inline card/badge styling, replace with `.card-premium` / `.badge-*` classes. If it uses cyan colors, fix to ocean tokens.

- [ ] **Step 2: Check CostOverview.tsx**

Read file. Apply `.card-premium` if applicable. Fix any inconsistent styling.

- [ ] **Step 3: Check DiffViewer.tsx**

Read file. Only apply `.card-premium` for outer container if applicable. Do NOT change emerald/amber colors — they are intentional diff semantics.

- [ ] **Step 4: Check ProjectCreate.tsx**

Read file. Remove any inline `<style>` blocks. Apply consistent classes.

- [ ] **Step 5: Final grep verification**

Run: `grep -r "rgba(0, 176, 240" frontend/src/` — expected: zero results
Run: `grep -r "rgba(6, 182, 212" frontend/src/` — expected: zero results
Run: `grep -rn "const.*AnimationStyles\|const.*ANIMATIONS\|const.*Styles = \`" frontend/src/components/ frontend/src/pages/` — expected: zero results (no inline style blocks)

- [ ] **Step 6: Full build + visual sanity check**

Run: `cd frontend && npx vite build 2>&1 | tail -5`
Run: `cd frontend && npx vite preview` — manually check key screens

- [ ] **Step 7: Commit (explicit file paths only)**

```bash
git add frontend/src/components/quick/UpgradePrompt.tsx frontend/src/components/costs/CostOverview.tsx frontend/src/components/compare/DiffViewer.tsx frontend/src/components/dashboard/ProjectCreate.tsx
git commit -m "fix(ui): consistency pass — verify remaining components, zero inline styles"
```

---

## Summary

| Task | Phase | Files | Focus |
|------|-------|-------|-------|
| 1 | Foundation | tailwind.config.js | Tokens (typography, shadows, spacing, radii, easings, animations) |
| 2 | Foundation | globals.css | Centralized animations, component classes, a11y |
| 3 | Inline removal | Dashboard, QuickResults, QuickAnalysis | Batch 1 — remove inline styles + fix cyan |
| 4 | Inline removal | SpecForm, MaterialBrowser, ImageUpload | Batch 2 — remove inline styles + fix cyan |
| 5 | Inline removal | Analysis components (5 files) | Batch 3 — score colors + aria-labels |
| 6 | Inline removal | Layout, Service, Knowledge (6 files) | Batch 4 — hero overlay, crossfade |
| 7 | Screen polish | AppShell | Navigation, touch targets, mobile nav |
| 8 | Screen polish | Quick Analysis flow (3 files) | Steps, results, stepper touch targets, font-mono |
| 9 | Screen polish | Dashboard, Material, Service, Knowledge | Cards, keyboard nav, skeleton, section headers, aria-labels |
| 10 | Motion | useScrollReveal hook, App.tsx, screens | Scroll reveal, page transitions, filter transitions |
| 11 | Verify | 4 files + grep checks | Final consistency check |
