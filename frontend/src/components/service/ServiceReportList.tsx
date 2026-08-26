import { useCallback, useEffect, useMemo, useState } from 'react'
import {
  AlertCircle,
  AlertTriangle,
  Info,
  CheckCircle,
  ChevronDown,
  Plus,
  Save,
  Pencil,
  Trash2,
  X,
} from 'lucide-react'
import { listProjects } from '../../services/api'
import {
  CATEGORY_LABELS,
  CATEGORY_OPTIONS,
  REPORT_TYPE_LABELS,
  REPORT_TYPE_OPTIONS,
  SEVERITY_OPTIONS,
  ZONE_TYPE_GROUPS,
  ZONE_TYPE_LABELS,
  createServiceReport,
  deleteServiceReport,
  listServiceReports,
  updateServiceReport,
} from '../../services/service-api'
import type { ServiceReportCreatePayload, ServiceReportDto } from '../../services/service-api'
import type { BoatClass, Project, Severity } from '../../types'
import { BOAT_CLASS_LABELS } from '../../types'
import { MEDIA } from '../../config/media'
import HeroSection from '../layout/HeroSection'

const SEVERITY_CONFIG: Record<
  Severity,
  { label: string; borderColor: string; bgColor: string; text: string; icon: typeof AlertCircle }
> = {
  critical: {
    label: 'Kritisch',
    borderColor: 'border-l-red-500',
    bgColor: 'bg-red-50',
    text: 'text-red-700',
    icon: AlertCircle,
  },
  high: {
    label: 'Hoch',
    borderColor: 'border-l-orange-500',
    bgColor: 'bg-orange-50',
    text: 'text-orange-700',
    icon: AlertTriangle,
  },
  medium: {
    label: 'Mittel',
    borderColor: 'border-l-amber-500',
    bgColor: 'bg-amber-50',
    text: 'text-amber-700',
    icon: AlertTriangle,
  },
  low: {
    label: 'Niedrig',
    borderColor: 'border-l-navy-300',
    bgColor: 'bg-transparent',
    text: 'text-navy-600',
    icon: Info,
  },
}

const FIELD_CLASS =
  'w-full bg-sand-50/60 border border-sand-200 rounded-lg px-4 py-2.5 text-navy-900 text-sm placeholder:text-navy-500 focus:outline-none focus:border-ocean-500/60 focus:ring-2 focus:ring-ocean-500/20 transition-all duration-200'

function SeverityBadge({ severity }: { severity: Severity }) {
  const cfg = SEVERITY_CONFIG[severity]
  return (
    <span
      className={`inline-flex items-center gap-1 text-xs px-2.5 py-1.5 rounded-md border border-navy-600/30 ${cfg.text} transition-all duration-300`}
      aria-label={`Schweregrad: ${cfg.label}`}
    >
      <cfg.icon className="w-3 h-3" />
      {cfg.label}
    </span>
  )
}

function ResolvedBadge() {
  return (
    <span className="inline-flex items-center gap-1 text-xs px-2.5 py-1.5 rounded-md border border-emerald-500/30 text-emerald-700 bg-emerald-50">
      <CheckCircle className="w-3 h-3" />
      Behoben
    </span>
  )
}

// ─── Erfassungsformular (Pipeline C Schreib-Einstieg) ───

type Scope = 'project' | 'fleet'

interface FormState {
  report_type: string
  category: string
  severity: Severity
  zone_type: string
  description: string
  root_cause: string
  resolution: string
  cost_eur: string
  hours_labor: string
  boat_age_months: string
  materials_involved: string
  reported_by: string
  reported_at: string
  scope: Scope
  project_id: string
  boat_class: string
  model_name: string
}

const EMPTY_FORM: FormState = {
  report_type: 'repair',
  category: '',
  severity: 'medium',
  zone_type: '',
  description: '',
  root_cause: '',
  resolution: '',
  cost_eur: '',
  hours_labor: '',
  boat_age_months: '',
  materials_involved: '',
  reported_by: '',
  reported_at: '',
  scope: 'fleet',
  project_id: '',
  boat_class: '',
  model_name: '',
}

function formFromReport(report: ServiceReportDto): FormState {
  return {
    report_type: report.report_type,
    category: report.category,
    severity: report.severity,
    zone_type: report.zone_type ?? '',
    description: report.description,
    root_cause: report.root_cause ?? '',
    resolution: report.resolution ?? '',
    cost_eur: report.cost_eur != null ? String(report.cost_eur) : '',
    hours_labor: report.hours_labor != null ? String(report.hours_labor) : '',
    boat_age_months: report.boat_age_months != null ? String(report.boat_age_months) : '',
    materials_involved: (report.materials_involved ?? []).join(', '),
    reported_by: report.reported_by ?? '',
    reported_at: report.reported_at ?? '',
    scope: report.project_id ? 'project' : 'fleet',
    project_id: report.project_id ?? '',
    boat_class: report.boat_class ?? '',
    model_name: report.model_name ?? '',
  }
}

/** Leerer String → null; Komma als Dezimaltrenner wird akzeptiert. */
function parseNumber(value: string): number | null {
  const trimmed = value.trim()
  if (!trimmed) return null
  const parsed = Number(trimmed.replace(',', '.'))
  return Number.isFinite(parsed) ? parsed : null
}

function textOrNull(value: string): string | null {
  const trimmed = value.trim()
  return trimmed ? trimmed : null
}

function buildPayload(form: FormState): ServiceReportCreatePayload {
  const materials = form.materials_involved
    .split(',')
    .map((m) => m.trim())
    .filter(Boolean)

  return {
    report_type: form.report_type,
    category: form.category,
    description: form.description.trim(),
    severity: form.severity,
    zone_type: textOrNull(form.zone_type),
    root_cause: textOrNull(form.root_cause),
    resolution: textOrNull(form.resolution),
    cost_eur: parseNumber(form.cost_eur),
    hours_labor: parseNumber(form.hours_labor),
    boat_age_months: form.boat_age_months.trim()
      ? Math.round(Number(form.boat_age_months.trim()))
      : null,
    materials_involved: materials.length > 0 ? materials : null,
    reported_by: textOrNull(form.reported_by),
    reported_at: textOrNull(form.reported_at),
    // Zuordnung: entweder projektbezogen ODER klassenweit. Das Backend
    // (`_load_service_reports` in routes/layouts.py) lädt projektbezogene
    // Berichte über project_id und zusätzlich die eigenen Berichte OHNE
    // project_id, die zur Bootsklasse des Projekts passen.
    project_id: form.scope === 'project' ? textOrNull(form.project_id) : null,
    boat_class: (textOrNull(form.boat_class) as BoatClass | null) ?? null,
    model_name: textOrNull(form.model_name),
  }
}

/** Clientseitige Prüfung — spiegelt die Grenzen aus schemas/service.py. */
function validate(form: FormState): string | null {
  if (!form.category) return 'Bitte eine Systemdomäne (Kategorie) wählen.'
  if (!form.description.trim()) return 'Bitte den Vorfall beschreiben.'
  if (form.description.trim().length > 20000)
    return 'Die Beschreibung darf höchstens 20.000 Zeichen lang sein.'
  if (form.scope === 'project' && !form.project_id)
    return 'Bitte ein Projekt wählen — oder auf „Klassenweit“ umstellen.'
  if (form.scope === 'fleet' && !form.boat_class)
    return 'Ohne Bootsklasse fließt ein klassenweiter Bericht in keine Analyse ein. Bitte Bootsklasse wählen.'

  const cost = form.cost_eur.trim() ? parseNumber(form.cost_eur) : null
  if (form.cost_eur.trim() && (cost === null || cost < 0))
    return 'Kosten müssen eine Zahl ≥ 0 sein.'
  const hours = form.hours_labor.trim() ? parseNumber(form.hours_labor) : null
  if (form.hours_labor.trim() && (hours === null || hours < 0 || hours > 100000))
    return 'Arbeitsstunden müssen zwischen 0 und 100.000 liegen.'
  const age = form.boat_age_months.trim() ? parseNumber(form.boat_age_months) : null
  if (form.boat_age_months.trim() && (age === null || age < 0 || age > 1200))
    return 'Das Bootsalter muss zwischen 0 und 1200 Monaten liegen.'
  return null
}

interface ReportFormProps {
  form: FormState
  editing: boolean
  saving: boolean
  error: string | null
  projects: Project[]
  projectsError: string | null
  onChange: (patch: Partial<FormState>) => void
  onSubmit: () => void
  onCancel: () => void
}

function ReportForm({
  form,
  editing,
  saving,
  error,
  projects,
  projectsError,
  onChange,
  onSubmit,
  onCancel,
}: ReportFormProps) {
  const severityInfo = SEVERITY_OPTIONS.find((s) => s.value === form.severity)

  return (
    <form
      onSubmit={(e) => {
        e.preventDefault()
        onSubmit()
      }}
      className="card-premium p-6 sm:p-8 space-y-8 animate-fade-in-up"
    >
      <div>
        <h2 className="font-serif text-xl text-navy-900">
          {editing ? 'Servicebericht bearbeiten' : 'Neuer Servicebericht'}
        </h2>
        <p className="text-sm text-navy-600 mt-2 leading-relaxed">
          Ein Servicebericht dokumentiert einen konkreten Vorfall am Boot — Reparatur,
          Wartung, Inspektion oder Schaden. Diese Berichte sind die Textdatenquelle der
          Analyse: ohne sie bleibt das Modul „Servicemuster“ dauerhaft übersprungen.
        </p>
      </div>

      {/* Vorfall */}
      <div className="space-y-6">
        <p className="label-premium">Vorfall</p>

        <div className="grid grid-cols-1 sm:grid-cols-2 gap-6">
          <div>
            <label htmlFor="sr-type" className="label-premium block mb-2">
              Art des Berichts *
            </label>
            <select
              id="sr-type"
              value={form.report_type}
              onChange={(e) => onChange({ report_type: e.target.value })}
              className={FIELD_CLASS}
            >
              {REPORT_TYPE_OPTIONS.map((o) => (
                <option key={o.value} value={o.value}>
                  {o.label}
                </option>
              ))}
            </select>
          </div>

          <div>
            <label htmlFor="sr-category" className="label-premium block mb-2">
              Systemdomäne *
            </label>
            <select
              id="sr-category"
              value={form.category}
              onChange={(e) => onChange({ category: e.target.value })}
              required
              className={FIELD_CLASS}
            >
              <option value="">Bitte wählen …</option>
              {CATEGORY_OPTIONS.map((o) => (
                <option key={o.value} value={o.value}>
                  {o.label}
                </option>
              ))}
            </select>
          </div>
        </div>

        <div>
          <label htmlFor="sr-description" className="label-premium block mb-2">
            Beschreibung *
          </label>
          <textarea
            id="sr-description"
            value={form.description}
            onChange={(e) => onChange({ description: e.target.value })}
            rows={4}
            required
            maxLength={20000}
            placeholder="Was wurde festgestellt? z.B. „Ruderlager hat deutliches Spiel, Ruderblatt lässt sich 8 mm axial bewegen.“"
            className={`${FIELD_CLASS} resize-y`}
          />
          <p className="text-xs text-navy-600 mt-2">
            Die Analyse liest diesen Text mit: Schadensbegriffe wie „Osmose“, „Riss“ oder
            „durchgerostet“ heben den Schweregrad an, Verneinungen („keine Osmose“) nicht.
          </p>
        </div>

        <div className="grid grid-cols-1 sm:grid-cols-2 gap-6">
          <div>
            <label htmlFor="sr-severity" className="label-premium block mb-2">
              Schweregrad *
            </label>
            <select
              id="sr-severity"
              value={form.severity}
              onChange={(e) => onChange({ severity: e.target.value as Severity })}
              className={FIELD_CLASS}
            >
              {SEVERITY_OPTIONS.map((o) => (
                <option key={o.value} value={o.value}>
                  {o.label}
                </option>
              ))}
            </select>
            {severityInfo && (
              <div className="mt-2 rounded-lg border border-sand-200 bg-sand-50/60 px-4 py-3">
                <p className="text-xs text-navy-700 leading-relaxed">{severityInfo.hint}</p>
                <p className="text-xs text-navy-600 mt-1.5">
                  Gewicht in der Zonenbewertung:{' '}
                  <span className="font-mono text-navy-900">{severityInfo.weight}</span> von 4.
                  Der Schweregrad steuert messbar, welche Zonen als problematisch gemeldet
                  werden.
                </p>
              </div>
            )}
          </div>

          <div>
            <label htmlFor="sr-zone" className="label-premium block mb-2">
              Zone
            </label>
            <select
              id="sr-zone"
              value={form.zone_type}
              onChange={(e) => onChange({ zone_type: e.target.value })}
              className={FIELD_CLASS}
            >
              <option value="">Keine Zone zugeordnet</option>
              {ZONE_TYPE_GROUPS.map((g) => (
                <optgroup key={g.group} label={g.group}>
                  {g.options.map((o) => (
                    <option key={o.value} value={o.value}>
                      {o.label}
                    </option>
                  ))}
                </optgroup>
              ))}
            </select>
            <p className="text-xs text-navy-600 mt-2">
              Ohne Zone lässt sich der Befund keiner Stelle am Boot zuordnen und zählt nicht
              in die Zonenbewertung ein.
            </p>
          </div>
        </div>
      </div>

      {/* Ursache & Behebung */}
      <div className="space-y-6 pt-2 border-t border-sand-200">
        <p className="label-premium pt-6">Ursache & Behebung</p>

        <div className="grid grid-cols-1 sm:grid-cols-2 gap-6">
          <div>
            <label htmlFor="sr-root-cause" className="label-premium block mb-2">
              Ursache
            </label>
            <textarea
              id="sr-root-cause"
              value={form.root_cause}
              onChange={(e) => onChange({ root_cause: e.target.value })}
              rows={3}
              placeholder="z.B. Lagerbuchse verschlissen, Wartungsintervall überschritten"
              className={`${FIELD_CLASS} resize-y`}
            />
          </div>
          <div>
            <label htmlFor="sr-resolution" className="label-premium block mb-2">
              Behebung
            </label>
            <textarea
              id="sr-resolution"
              value={form.resolution}
              onChange={(e) => onChange({ resolution: e.target.value })}
              rows={3}
              placeholder="Leer lassen, solange der Vorfall offen ist"
              className={`${FIELD_CLASS} resize-y`}
            />
          </div>
        </div>

        <div className="grid grid-cols-1 sm:grid-cols-3 gap-6">
          <div>
            <label htmlFor="sr-cost" className="label-premium block mb-2">
              Kosten (EUR)
            </label>
            <input
              id="sr-cost"
              type="number"
              min={0}
              step="0.01"
              value={form.cost_eur}
              onChange={(e) => onChange({ cost_eur: e.target.value })}
              placeholder="z.B. 1250"
              className={FIELD_CLASS}
            />
          </div>
          <div>
            <label htmlFor="sr-hours" className="label-premium block mb-2">
              Arbeitsstunden
            </label>
            <input
              id="sr-hours"
              type="number"
              min={0}
              max={100000}
              step="0.5"
              value={form.hours_labor}
              onChange={(e) => onChange({ hours_labor: e.target.value })}
              placeholder="z.B. 6"
              className={FIELD_CLASS}
            />
          </div>
          <div>
            <label htmlFor="sr-age" className="label-premium block mb-2">
              Bootsalter (Monate)
            </label>
            <input
              id="sr-age"
              type="number"
              min={0}
              max={1200}
              step="1"
              value={form.boat_age_months}
              onChange={(e) => onChange({ boat_age_months: e.target.value })}
              placeholder="z.B. 84"
              className={FIELD_CLASS}
            />
          </div>
        </div>

        <div className="grid grid-cols-1 sm:grid-cols-3 gap-6">
          <div>
            <label htmlFor="sr-materials" className="label-premium block mb-2">
              Beteiligte Materialien
            </label>
            <input
              id="sr-materials"
              type="text"
              value={form.materials_involved}
              onChange={(e) => onChange({ materials_involved: e.target.value })}
              placeholder="Komma-getrennt, z.B. Teak, Edelstahl 316L"
              className={FIELD_CLASS}
            />
          </div>
          <div>
            <label htmlFor="sr-reported-by" className="label-premium block mb-2">
              Gemeldet von
            </label>
            <input
              id="sr-reported-by"
              type="text"
              value={form.reported_by}
              onChange={(e) => onChange({ reported_by: e.target.value })}
              placeholder="Werft, Eigner, Gutachter …"
              className={FIELD_CLASS}
            />
          </div>
          <div>
            <label htmlFor="sr-reported-at" className="label-premium block mb-2">
              Datum des Vorfalls
            </label>
            <input
              id="sr-reported-at"
              type="date"
              value={form.reported_at}
              onChange={(e) => onChange({ reported_at: e.target.value })}
              className={FIELD_CLASS}
            />
          </div>
        </div>
      </div>

      {/* Zuordnung */}
      <div className="space-y-6 pt-2 border-t border-sand-200">
        <div className="pt-6">
          <p className="label-premium">Zuordnung</p>
          <p className="text-xs text-navy-600 mt-2 leading-relaxed">
            Projektbezogene Berichte fließen in die Analyse genau dieses Projekts ein.
            Klassenweite Berichte ohne Projekt fließen in alle Ihre Projekte derselben
            Bootsklasse ein — so wird gesammelte Flottenerfahrung nutzbar.
          </p>
        </div>

        <div className="flex flex-col sm:flex-row gap-3">
          <button
            type="button"
            onClick={() => onChange({ scope: 'project' })}
            aria-pressed={form.scope === 'project'}
            className={`flex-1 text-left rounded-lg border px-4 py-3 transition-all duration-200 ${
              form.scope === 'project'
                ? 'border-ocean-500 bg-ocean-50 text-ocean-800'
                : 'border-sand-200 bg-sand-50/60 text-navy-700 hover:border-ocean-300'
            }`}
          >
            <span className="block text-sm font-medium">Projektbezogen</span>
            <span className="block text-xs mt-1 opacity-80">Vorfall an einem konkreten Entwurf</span>
          </button>
          <button
            type="button"
            onClick={() => onChange({ scope: 'fleet' })}
            aria-pressed={form.scope === 'fleet'}
            className={`flex-1 text-left rounded-lg border px-4 py-3 transition-all duration-200 ${
              form.scope === 'fleet'
                ? 'border-ocean-500 bg-ocean-50 text-ocean-800'
                : 'border-sand-200 bg-sand-50/60 text-navy-700 hover:border-ocean-300'
            }`}
          >
            <span className="block text-sm font-medium">Klassenweit</span>
            <span className="block text-xs mt-1 opacity-80">Erfahrung für eine ganze Bootsklasse</span>
          </button>
        </div>

        {form.scope === 'project' ? (
          <div>
            <label htmlFor="sr-project" className="label-premium block mb-2">
              Projekt *
            </label>
            <select
              id="sr-project"
              value={form.project_id}
              onChange={(e) => onChange({ project_id: e.target.value })}
              className={FIELD_CLASS}
              disabled={projects.length === 0}
            >
              <option value="">Bitte wählen …</option>
              {projects.map((p) => (
                <option key={p.id} value={p.id}>
                  {p.name} · {BOAT_CLASS_LABELS[p.boat_class]}
                </option>
              ))}
            </select>
            {projectsError && (
              <p className="text-xs text-amber-700 mt-2">
                Projekte konnten nicht geladen werden: {projectsError}
              </p>
            )}
            {!projectsError && projects.length === 0 && (
              <p className="text-xs text-navy-600 mt-2">
                Noch keine Projekte vorhanden — bitte „Klassenweit“ verwenden.
              </p>
            )}
          </div>
        ) : null}

        <div className="grid grid-cols-1 sm:grid-cols-2 gap-6">
          <div>
            <label htmlFor="sr-boat-class" className="label-premium block mb-2">
              Bootsklasse {form.scope === 'fleet' ? '*' : ''}
            </label>
            <select
              id="sr-boat-class"
              value={form.boat_class}
              onChange={(e) => onChange({ boat_class: e.target.value })}
              className={FIELD_CLASS}
            >
              <option value="">Keine Angabe</option>
              {Object.entries(BOAT_CLASS_LABELS).map(([value, label]) => (
                <option key={value} value={value}>
                  {label}
                </option>
              ))}
            </select>
          </div>
          <div>
            <label htmlFor="sr-model" className="label-premium block mb-2">
              Modell
            </label>
            <input
              id="sr-model"
              type="text"
              value={form.model_name}
              onChange={(e) => onChange({ model_name: e.target.value })}
              placeholder="z.B. Bavaria Cruiser 46"
              className={FIELD_CLASS}
            />
          </div>
        </div>
      </div>

      {error && (
        <div
          role="alert"
          className="rounded-lg border border-red-200 bg-red-50 px-4 py-3 text-sm text-red-700"
        >
          {error}
        </div>
      )}

      <div className="flex flex-col sm:flex-row gap-3 pt-2">
        <button
          type="submit"
          disabled={saving}
          className="flex items-center justify-center gap-2 bg-ocean-600 hover:bg-ocean-700 disabled:opacity-50 disabled:cursor-not-allowed text-white px-8 py-3 rounded-lg font-medium transition-colors duration-200"
        >
          {saving ? (
            <>
              <span className="inline-block w-4 h-4 rounded-full border-2 border-current border-t-transparent animate-spin" />
              Wird gespeichert …
            </>
          ) : (
            <>
              <Save className="w-4 h-4" />
              {editing ? 'Änderungen speichern' : 'Bericht anlegen'}
            </>
          )}
        </button>
        <button
          type="button"
          onClick={onCancel}
          disabled={saving}
          className="flex items-center justify-center gap-2 text-navy-700 hover:text-navy-900 px-8 py-3 rounded-lg transition-colors duration-200 font-medium"
        >
          <X className="w-4 h-4" />
          Abbrechen
        </button>
      </div>
    </form>
  )
}

export default function ServiceReportList() {
  const [reports, setReports] = useState<ServiceReportDto[]>([])
  const [loading, setLoading] = useState(true)
  const [error, setError] = useState<string | null>(null)
  const [categoryFilter, setCategoryFilter] = useState('')
  const [severityFilter, setSeverityFilter] = useState('')
  const [knownCategories, setKnownCategories] = useState<string[]>([])
  const [expandedReportId, setExpandedReportId] = useState<string | null>(null)

  const [formOpen, setFormOpen] = useState(false)
  const [editingId, setEditingId] = useState<string | null>(null)
  const [form, setForm] = useState<FormState>(EMPTY_FORM)
  const [saving, setSaving] = useState(false)
  const [formError, setFormError] = useState<string | null>(null)
  const [notice, setNotice] = useState<string | null>(null)

  const [confirmDeleteId, setConfirmDeleteId] = useState<string | null>(null)
  const [deletingId, setDeletingId] = useState<string | null>(null)

  const [projects, setProjects] = useState<Project[]>([])
  const [projectsError, setProjectsError] = useState<string | null>(null)

  const fetchReports = useCallback((cat?: string, sev?: string) => {
    setLoading(true)
    setError(null)
    listServiceReports({ category: cat || undefined, severity: sev || undefined })
      .then((data) => {
        setReports(data)
        setKnownCategories((prev) =>
          Array.from(new Set([...prev, ...data.map((r) => r.category)])).sort()
        )
      })
      .catch((e: unknown) => setError(e instanceof Error ? e.message : 'Unbekannter Fehler'))
      .finally(() => setLoading(false))
  }, [])

  useEffect(() => {
    fetchReports()
  }, [fetchReports])

  useEffect(() => {
    listProjects()
      .then(setProjects)
      .catch((e: unknown) =>
        setProjectsError(e instanceof Error ? e.message : 'Unbekannter Fehler')
      )
  }, [])

  const handleCategoryChange = (cat: string) => {
    setCategoryFilter(cat)
    fetchReports(cat, severityFilter)
  }

  const handleSeverityChange = (sev: string) => {
    setSeverityFilter(sev)
    fetchReports(categoryFilter, sev)
  }

  const categoryOptions = useMemo(() => {
    const extra = knownCategories
      .filter((c) => !(c in CATEGORY_LABELS))
      .map((c) => ({ value: c, label: c }))
    return [...CATEGORY_OPTIONS, ...extra]
  }, [knownCategories])

  const openCreateForm = () => {
    setEditingId(null)
    setForm(EMPTY_FORM)
    setFormError(null)
    setNotice(null)
    setFormOpen(true)
  }

  const openEditForm = (report: ServiceReportDto) => {
    setEditingId(report.id)
    setForm(formFromReport(report))
    setFormError(null)
    setNotice(null)
    setFormOpen(true)
  }

  const closeForm = () => {
    setFormOpen(false)
    setEditingId(null)
    setFormError(null)
  }

  const handleFormChange = (patch: Partial<FormState>) => {
    setForm((prev) => ({ ...prev, ...patch }))
  }

  const handleSubmit = async () => {
    const validationError = validate(form)
    if (validationError) {
      setFormError(validationError)
      return
    }
    setSaving(true)
    setFormError(null)
    try {
      const payload = buildPayload(form)
      if (editingId) {
        await updateServiceReport(editingId, payload)
        setNotice('Servicebericht aktualisiert.')
      } else {
        await createServiceReport(payload)
        setNotice('Servicebericht angelegt.')
      }
      closeForm()
      fetchReports(categoryFilter, severityFilter)
    } catch (e: unknown) {
      setFormError(e instanceof Error ? e.message : 'Speichern fehlgeschlagen')
    } finally {
      setSaving(false)
    }
  }

  const handleDelete = async (id: string) => {
    setDeletingId(id)
    setError(null)
    try {
      await deleteServiceReport(id)
      setConfirmDeleteId(null)
      setNotice('Servicebericht gelöscht.')
      if (editingId === id) closeForm()
      fetchReports(categoryFilter, severityFilter)
    } catch (e: unknown) {
      setError(e instanceof Error ? e.message : 'Löschen fehlgeschlagen')
    } finally {
      setDeletingId(null)
    }
  }

  return (
    <div>
      <HeroSection
        backgroundImage={MEDIA.structure.hull_drydock}
        title="Serviceberichte"
        subtitle="Berichte über Wartung, Garantie, Umbau und erkannte Probleme mit Schweregradkennzeichnung"
        label="Service"
      />

      <div className="space-y-8 px-4 sm:px-10 py-12">
        {/* Controls */}
        <div className="flex flex-col sm:flex-row items-start sm:items-end justify-between gap-4 sm:gap-6">
          <div className="flex flex-col sm:flex-row items-start sm:items-center gap-4 w-full sm:w-auto">
            <div className="w-full sm:w-auto">
              <p className="label-premium mb-2">KATEGORIE</p>
              <select
                value={categoryFilter}
                onChange={(e) => handleCategoryChange(e.target.value)}
                aria-label="Kategorie filtern"
                className="w-full sm:w-auto bg-sand-50/60 border border-sand-200 rounded-lg px-4 py-2.5 text-navy-900 text-sm focus:outline-none focus:border-ocean-500/60 focus:ring-2 focus:ring-ocean-500/20 transition-all duration-200"
              >
                <option value="">Alle Kategorien</option>
                {categoryOptions.map((c) => (
                  <option key={c.value} value={c.value}>
                    {c.label}
                  </option>
                ))}
              </select>
            </div>

            <div className="w-full sm:w-auto">
              <p className="label-premium mb-2">SCHWEREGRAD</p>
              <select
                value={severityFilter}
                onChange={(e) => handleSeverityChange(e.target.value)}
                aria-label="Schweregrad filtern"
                className="w-full sm:w-auto bg-sand-50/60 border border-sand-200 rounded-lg px-4 py-2.5 text-navy-900 text-sm focus:outline-none focus:border-ocean-500/60 focus:ring-2 focus:ring-ocean-500/20 transition-all duration-200"
              >
                <option value="">Alle Schweregrade</option>
                {SEVERITY_OPTIONS.map((o) => (
                  <option key={o.value} value={o.value}>
                    {o.label}
                  </option>
                ))}
              </select>
            </div>
          </div>

          {!formOpen && (
            <button
              type="button"
              onClick={openCreateForm}
              className="flex items-center gap-2 bg-ocean-600 hover:bg-ocean-700 text-white px-6 py-2.5 rounded-lg font-medium text-sm transition-colors duration-200"
            >
              <Plus className="w-4 h-4" />
              Neuer Bericht
            </button>
          )}
        </div>

        {notice && !formOpen && (
          <div
            role="status"
            className="rounded-lg border border-emerald-200 bg-emerald-50 px-4 py-3 text-sm text-emerald-700"
          >
            {notice}
          </div>
        )}

        {formOpen && (
          <ReportForm
            form={form}
            editing={editingId !== null}
            saving={saving}
            error={formError}
            projects={projects}
            projectsError={projectsError}
            onChange={handleFormChange}
            onSubmit={handleSubmit}
            onCancel={closeForm}
          />
        )}

        {loading && <div className="text-center py-12 text-navy-600">Berichte werden geladen...</div>}

        {error && (
          <div role="alert" className="card-premium bg-red-50 border-red-200 p-6 text-red-700 text-sm">
            Fehler: {error}
          </div>
        )}

        {!loading && !error && reports.length === 0 && (
          <div className="card-premium px-10 py-12 text-center">
            <p className="text-navy-900 font-medium">Noch keine Serviceberichte erfasst</p>
            <p className="text-navy-600 text-sm mt-2 max-w-xl mx-auto leading-relaxed">
              Solange keine Berichte vorliegen, überspringt die Analyse das Modul
              „Servicemuster“. Legen Sie den ersten Vorfall an — Reparatur, Wartung oder
              Inspektion.
            </p>
            {!formOpen && (
              <button
                type="button"
                onClick={openCreateForm}
                className="mt-6 inline-flex items-center gap-2 bg-ocean-600 hover:bg-ocean-700 text-white px-6 py-2.5 rounded-lg font-medium text-sm transition-colors duration-200"
              >
                <Plus className="w-4 h-4" />
                Ersten Bericht anlegen
              </button>
            )}
          </div>
        )}

        {!loading && !error && reports.length > 0 && (
          <div className="space-y-4">
            {reports.map((report, idx) => {
              const cfg = SEVERITY_CONFIG[report.severity]
              const isExpanded = expandedReportId === report.id
              return (
                <div
                  key={report.id}
                  style={{ animationDelay: `${idx * 60}ms` }}
                  className={`animate-fade-in-up border-l-4 ${cfg.borderColor} border border-sand-200 ${cfg.bgColor} rounded-lg transition-all duration-300 hover:shadow-lg hover:shadow-sand-200/50 group`}
                >
                  <button
                    type="button"
                    onClick={() => setExpandedReportId(isExpanded ? null : report.id)}
                    className="w-full text-left p-6"
                    aria-expanded={isExpanded}
                    aria-label={`${report.description} - ${cfg.label}`}
                  >
                    <div className="flex items-start justify-between gap-4 mb-3">
                      <div className="flex-1">
                        <p className="text-navy-900 font-medium text-sm leading-snug group-hover:text-ocean-700 transition-colors">
                          {report.description}
                        </p>
                      </div>
                      <div className="flex items-center gap-2 shrink-0">
                        <SeverityBadge severity={report.severity} />
                        {report.resolution && <ResolvedBadge />}
                        {(report.root_cause || report.resolution) && (
                          <ChevronDown
                            className={`w-4 h-4 text-navy-500 transition-transform duration-300 ${
                              isExpanded ? 'rotate-180' : ''
                            }`}
                          />
                        )}
                      </div>
                    </div>

                    {/* Metadata Grid - Stacked on mobile */}
                    <div className="grid grid-cols-1 sm:grid-cols-2 gap-3 text-xs text-navy-600 pt-3 border-t border-sand-200">
                      <div>
                        <span className="label-premium mr-1">TYP</span>
                        <span className="text-navy-700">
                          {REPORT_TYPE_LABELS[report.report_type] ?? report.report_type}
                        </span>
                      </div>
                      {report.category && (
                        <div>
                          <span className="label-premium mr-1">KATEGORIE</span>
                          <span className="text-navy-700">
                            {CATEGORY_LABELS[report.category] ?? report.category}
                          </span>
                        </div>
                      )}
                      {report.zone_type && (
                        <div>
                          <span className="label-premium mr-1">ZONE</span>
                          <span className="text-navy-700">
                            {ZONE_TYPE_LABELS[report.zone_type] ?? report.zone_type}
                          </span>
                        </div>
                      )}
                      {report.boat_class && (
                        <div>
                          <span className="label-premium mr-1">KLASSE</span>
                          <span className="text-navy-700">
                            {BOAT_CLASS_LABELS[report.boat_class]}
                          </span>
                        </div>
                      )}
                      {report.cost_eur != null && (
                        <div>
                          <span className="label-premium mr-1">KOSTEN</span>
                          <span className="font-mono text-amber-700">
                            {report.cost_eur.toLocaleString('de-DE', {
                              style: 'currency',
                              currency: 'EUR',
                            })}
                          </span>
                        </div>
                      )}
                      {report.boat_age_months != null && (
                        <div>
                          <span className="label-premium mr-1">BOOTSALTER</span>
                          <span className="font-mono text-navy-700">
                            {report.boat_age_months} Monate
                          </span>
                        </div>
                      )}
                    </div>

                    {/* Expandable Root Cause / Resolution */}
                    {isExpanded && (report.root_cause || report.resolution) && (
                      <div className="mt-4 pt-4 border-t border-sand-200 space-y-4 animate-slide-down">
                        {report.root_cause && (
                          <div className="flex items-start gap-2">
                            <AlertTriangle className="w-4 h-4 text-amber-400 flex-shrink-0 mt-0.5" />
                            <div className="flex-1">
                              <p className="label-premium mb-2">URSACHE</p>
                              <p className="text-xs text-navy-600 leading-relaxed">
                                {report.root_cause}
                              </p>
                            </div>
                          </div>
                        )}
                        {report.resolution && (
                          <div className="flex items-start gap-2">
                            <CheckCircle className="w-4 h-4 text-emerald-500 flex-shrink-0 mt-0.5" />
                            <div className="flex-1">
                              <p className="label-premium mb-2">BEHEBUNG</p>
                              <p className="text-xs text-navy-600 leading-relaxed">
                                {report.resolution}
                              </p>
                            </div>
                          </div>
                        )}
                      </div>
                    )}
                  </button>

                  {/* Aktionen */}
                  <div className="flex flex-wrap items-center gap-2 px-6 pb-4 -mt-1">
                    <button
                      type="button"
                      onClick={() => openEditForm(report)}
                      className="inline-flex items-center gap-1.5 text-xs text-navy-600 hover:text-ocean-700 px-3 py-1.5 rounded-md border border-sand-200 bg-white/60 transition-colors duration-200"
                    >
                      <Pencil className="w-3 h-3" />
                      Bearbeiten
                    </button>
                    {confirmDeleteId === report.id ? (
                      <>
                        <span className="text-xs text-red-700">Wirklich löschen?</span>
                        <button
                          type="button"
                          onClick={() => handleDelete(report.id)}
                          disabled={deletingId === report.id}
                          className="inline-flex items-center gap-1.5 text-xs text-white bg-red-600 hover:bg-red-700 disabled:opacity-50 px-3 py-1.5 rounded-md transition-colors duration-200"
                        >
                          <Trash2 className="w-3 h-3" />
                          {deletingId === report.id ? 'Wird gelöscht …' : 'Ja, löschen'}
                        </button>
                        <button
                          type="button"
                          onClick={() => setConfirmDeleteId(null)}
                          className="text-xs text-navy-600 hover:text-navy-900 px-3 py-1.5 rounded-md transition-colors duration-200"
                        >
                          Abbrechen
                        </button>
                      </>
                    ) : (
                      <button
                        type="button"
                        onClick={() => setConfirmDeleteId(report.id)}
                        className="inline-flex items-center gap-1.5 text-xs text-navy-600 hover:text-red-700 px-3 py-1.5 rounded-md border border-sand-200 bg-white/60 transition-colors duration-200"
                      >
                        <Trash2 className="w-3 h-3" />
                        Löschen
                      </button>
                    )}
                  </div>
                </div>
              )
            })}
          </div>
        )}
      </div>
    </div>
  )
}
