# Knowledge Browser Component

A premium maritime knowledge reference system for the AYDI yacht analysis platform, designed as a digital equivalent to Nigel Calder's Boatowner's Mechanical and Electrical Manual.

## Components

### KnowledgeDetail.tsx
Modal panel displaying detailed knowledge about a selected category or subcategory.

**Features:**
- Rich formatted content display with HTML rendering
- Material properties in clean table format
- Degradation timelines with visual condition percentage bars
- Manufacturer-specific known issues with severity badges
- Cost impact estimates
- Compliance standards and certifications
- Implementation notes with technical guidance
- Responsive modal with backdrop blur

**Props:**
- `data: KnowledgeDetail` - The knowledge item to display
- `onClose: () => void` - Callback when user closes the panel

**Design Elements:**
- Color-coded severity badges (critical: red, warning: amber, info: blue)
- Trending indicator for degradation data
- Icon-based visual hierarchy
- Premium maritime color scheme (navy, ocean, gold)

## Usage

### Basic Implementation
```tsx
import { useState } from 'react'
import KnowledgePage from './pages/KnowledgePage'

export default function App() {
  return <KnowledgePage />
}
```

### API Integration
The knowledge system uses dedicated API endpoints:

```typescript
import {
  getKnowledgeCategories(),      // Fetch all categories
  getKnowledgeDetail(categoryId), // Get detailed knowledge
  getMaterialKnowledge(params),   // Material-specific data
  getManufacturerKnowledge(name), // Manufacturer profiles
  getDegradationKnowledge(params), // Degradation timelines
  searchKnowledge(query)          // Full-text search
} from './services/knowledge-api'
```

## Data Types

### KnowledgeCategory
```typescript
interface KnowledgeCategory {
  id: string
  name: string
  description: string
  icon?: string
  subcategory_count: number
  subcategories: KnowledgeSubcategory[]
  implementation_status: 'complete' | 'partial' | 'planned'
  documentation_ready: boolean
}
```

### KnowledgeDetail
```typescript
interface KnowledgeDetail {
  id: string
  category_id: string
  category_name: string
  subcategory_id?: string
  subcategory_name?: string
  title: string
  description: string
  content_html?: string
  content_markdown?: string
  material_properties?: MaterialProperty[]
  related_issues?: ManufacturerIssue[]
  degradation_data?: DegradationTimeline
  implementation_notes?: string
  cost_impact?: { low: number; high: number }
  compliance_standards?: string[]
  created_at: string
  updated_at: string
}
```

### MaterialProperty
```typescript
interface MaterialProperty {
  name: string
  value: string | number
  unit?: string
  typical_range?: { min: number; max: number }
  notes?: string
}
```

### DegradationTimeline
```typescript
interface DegradationTimeline {
  material: string
  environment: 'tropical' | 'temperate' | 'polar' | 'saltwater_exposed' | 'fresh_water'
  datapoints: DegradationData[] // timepoint_years, condition_percentage, etc.
  expected_lifespan_years: number
  mitigation_strategies: string[]
  maintenance_plan: string[]
  replacement_triggers: string[]
}
```

## Feature Breakdown

### 1. Knowledge Categories Grid
- Displays all 21 knowledge categories
- Each card shows:
  - Category name with serif font (Playfair Display)
  - Descriptive text
  - Implementation status badge (Complete/Partial/Planned)
  - Subcategory count
  - Documentation readiness indicator

### 2. Expandable Subcategories
- Click category to expand and reveal subcategories
- Smooth animation transition
- Left border accent on subcategory items
- Hover states for interactive feedback

### 3. Search Functionality
- Real-time search across knowledge base
- Minimum 2 characters to trigger search
- Results displayed in grid format
- Quick preview with category context
- Graceful fallback when no results found

### 4. Detail Panel Modal
- Full-screen overlay with backdrop blur
- Premium gradient backgrounds
- Organized content sections:
  - Overview with rich description
  - Material properties table
  - Degradation timeline visualization
  - Known issues with severity indicators
  - Cost impact estimates
  - Compliance standards
  - Implementation notes
- Close button (X) and footer action button
- Smooth animations

### 5. Design System Integration
- **Colors:**
  - Navy (#0F1729) - primary background
  - Ocean (#1B6B8F) - accent/highlights
  - Cream/White - text
  - Gold (#B8860B) - premium accents

- **Typography:**
  - Playfair Display (serif) - headings, premium text
  - Inter (sans-serif) - body, UI labels
  - Premium tracking and letter-spacing

- **Components:**
  - `card-premium` - elevated card style with border
  - `label-premium` - uppercase labels with tracking
  - Hero section with background image
  - Responsive grid layouts

## Backend API Endpoints

Expected endpoints:

```
GET /api/v1/knowledge/categories
  -> Returns: KnowledgeCategory[]

GET /api/v1/knowledge/categories/{id}
  -> Returns: KnowledgeDetail

GET /api/v1/knowledge/materials?category=X&material=Y&use_case=Z
  -> Returns: KnowledgeDetail[]

GET /api/v1/knowledge/manufacturers/{name}
  -> Returns: ManufacturerKnowledge

GET /api/v1/knowledge/degradation?material=X&environment=Y&timeframe=Z
  -> Returns: DegradationTimeline[]

GET /api/v1/knowledge/search?q=query&limit=20&offset=0
  -> Returns: KnowledgeDetail[]
```

## Styling & Responsive Design

- **Mobile:** Single column layout with full-width cards
- **Tablet:** Optimized spacing and readable font sizes
- **Desktop:** Multi-column grids (2-3 columns)
- **Modal:** Centered with max-width constraint, scrollable content

## Accessibility

- Proper heading hierarchy (H1 -> H4)
- ARIA labels on interactive elements
- Keyboard-navigable search and controls
- Color-coded content includes text labels (not just color)
- High contrast text on backgrounds
- Semantic HTML structure

## Mock Data

The component includes mock data for demonstration when the backend API is unavailable. Mock data includes:

1. **Materialwissenschaft** (Materials Science) - 8 subcategories
2. **Degradationszeitleisten** (Degradation Timelines) - 6 subcategories
3. **Bekannte Herstellungsprobleme** (Known Manufacturing Issues) - 12 subcategories
4. **Maritime Standards & Zertifizierungen** (Marine Standards) - 5 subcategories
5. **Best Practices & Wartung** (Best Practices & Maintenance) - 7 subcategories
6. **Umweltauswirkungen** (Environmental Impact) - 4 subcategories

## Performance Considerations

- Lazy loading of category details on demand
- Search debouncing recommended for large datasets
- Virtual scrolling for long lists (future optimization)
- Image optimization through media configuration
- Efficient CSS transitions and animations

## Future Enhancements

- Bookmarking/favoriting knowledge items
- Printing/PDF export of knowledge details
- Version history and change tracking
- Comments/annotations system
- Related knowledge cross-linking
- Citation/reference management
- Manufacturer comparison tool
- Interactive degradation calculators

## German UI Text

All UI text is in German to match the Scandinavian maritime aesthetic of the AYDI platform:

- "Wissensdatenbank" - Knowledge Database
- "Wissen" - Knowledge (nav label)
- "Übersicht" - Overview
- "Materialeigenschaften" - Material Properties
- "Degradationszeitleiste" - Degradation Timeline
- "Bekannte Probleme" - Known Issues
- "Kostenfolgen" - Cost Impact
- "Geltende Normen" - Applicable Standards

---

**Design Philosophy:** Premium maritime reference tool inspired by Nigel Calder's authoritative boating manuals. Clean, professional, trustworthy – like consulting a master shipwright's decades of accumulated knowledge.
