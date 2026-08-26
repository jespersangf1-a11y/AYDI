import { useState, useRef, useCallback, useEffect } from 'react'
import { Upload, X, Loader2, ImageIcon, Lock, Info } from 'lucide-react'
import type { BoatClass, ImageType, ImageUploadData } from '../../types'
import { IMAGE_TYPE_LABELS } from '../../types'
import { uploadAndAnalyzeImage, uploadProjectImage } from '../../services/api'
import { normalizeVisualAnalysis } from '../../services/visual-result'
import type { VisualAnalysisView } from '../../services/visual-result'
import VisualResults from './VisualResults'
import { MEDIA } from '../../config/media'
import HeroSection from '../layout/HeroSection'

/**
 * Zwei Betriebsarten, beide gegen das Backend geprüft:
 *
 *  - Standalone (kein `projectId`): `POST /api/v1/images/analyze`
 *    (Formfelder file, image_type, boat_class, zone_type) — reine
 *    Analyse-Route, deshalb PRO-Pflicht (403) VOR dem Upload.
 *  - Projektkontext (`projectId`): `POST /api/v1/projects/{project_id}/images`
 *    (Formfelder file, image_type, zone_name) — die Bootsklasse kommt vom
 *    Projekt, deshalb wird hier KEINE `boatClass` benötigt. FREE darf
 *    hochladen; die Analyse unterbleibt sichtbar (weiches Tarif-Gate).
 */
type ImageUploadProps = {
  onAnalysisComplete?: (result: VisualAnalysisView) => void
  onUploadComplete?: (image: ImageUploadData) => void
  /** Hero-Kopf ausblenden, wenn die Komponente in einem Tab eingebettet ist. */
  showHero?: boolean
} & (
  | { projectId: string; boatClass?: BoatClass }
  | { projectId?: undefined; boatClass: BoatClass }
)

const MAX_FILE_SIZE = 20 * 1024 * 1024 // 20 MB

// Deckungsgleich mit dem Backend (images.py: ALLOWED_EXTENSIONS bzw.
// _PIL_FORMAT_TO_EXT) — HEIC ist dort bewusst NICHT erlaubt und würde mit
// HTTP 400 abgewiesen.
const ACCEPTED_TYPES = ['image/jpeg', 'image/png', 'image/webp']
const ACCEPTED_EXTENSIONS = ['.jpg', '.jpeg', '.png', '.webp']
const ACCEPT_ATTRIBUTE = ACCEPTED_EXTENSIONS.join(',')

const FORMAT_ERROR =
  'Ungültiges Dateiformat. Erlaubt sind JPG, PNG und WebP — die Datei braucht auch die passende Dateiendung.'

// HEIC/HEIF ist das Standardformat der iPhone-Kamera und damit der
// wahrscheinlichste Upload überhaupt. Deshalb wird es hier vorher und
// erklärend abgelehnt statt erst vom Backend mit einem nackten 400.
const HEIC_ERROR =
  'HEIC/HEIF wird nicht unterstützt (Standardformat der iPhone-Kamera). ' +
  'Lösung am iPhone: Einstellungen → Kamera → Formate → „Maximale Kompatibilität“ — ' +
  'dann fotografiert das iPhone in JPG. Alternativ das vorhandene Bild vor dem ' +
  'Hochladen in JPG oder PNG umwandeln (Fotos-App → Teilen → „In JPEG konvertieren“).'

function isHeic(file: File): boolean {
  const name = file.name.toLowerCase()
  return (
    file.type === 'image/heic' ||
    file.type === 'image/heif' ||
    name.endsWith('.heic') ||
    name.endsWith('.heif')
  )
}

/** Status der Antwort: `err.status` wird von services/api.ts gesetzt. */
function statusOf(err: unknown): number {
  if (typeof err === 'object' && err !== null && 'status' in err) {
    const value = (err as { status: unknown }).status
    return typeof value === 'number' ? value : 0
  }
  return 0
}

export default function ImageUpload(props: ImageUploadProps) {
  const { boatClass, projectId, onAnalysisComplete, onUploadComplete } = props
  const showHero = props.showHero ?? projectId === undefined

  const [file, setFile] = useState<File | null>(null)
  const [preview, setPreview] = useState<string | null>(null)
  const [imageType, setImageType] = useState<ImageType>('interior_overview')
  const [zoneType, setZoneType] = useState('')
  const [uploading, setUploading] = useState(false)
  const [uploadProgress, setUploadProgress] = useState(0)
  const [error, setError] = useState<string | null>(null)
  const [tierNotice, setTierNotice] = useState<string | null>(null)
  const [notice, setNotice] = useState<string | null>(null)
  const [result, setResult] = useState<VisualAnalysisView | null>(null)
  const [dragOver, setDragOver] = useState(false)
  const inputRef = useRef<HTMLInputElement>(null)

  const resetMessages = useCallback(() => {
    setError(null)
    setTierNotice(null)
    setNotice(null)
  }, [])

  const handleFile = useCallback(
    (f: File) => {
      resetMessages()
      setResult(null)
      setUploadProgress(0)

      if (isHeic(f)) {
        setError(HEIC_ERROR)
        return
      }

      const name = f.name.toLowerCase()
      const extensionOk = ACCEPTED_EXTENSIONS.some((ext) => name.endsWith(ext))
      // Das Backend prüft zuerst die Dateiendung (_extract_extension) und
      // danach den Inhalt (_validate_image_bytes) — beides wird hier gespiegelt.
      if (!extensionOk || (f.type !== '' && !ACCEPTED_TYPES.includes(f.type))) {
        setError(FORMAT_ERROR)
        return
      }
      if (f.size > MAX_FILE_SIZE) {
        setError('Datei zu groß. Maximal 20 MB erlaubt.')
        return
      }

      setFile(f)
      const url = URL.createObjectURL(f)
      setPreview(url)
    },
    [resetMessages],
  )

  const handleDrop = useCallback(
    (e: React.DragEvent) => {
      e.preventDefault()
      setDragOver(false)
      const dropped = e.dataTransfer.files[0]
      if (dropped) handleFile(dropped)
    },
    [handleFile],
  )

  const handleDragOver = useCallback((e: React.DragEvent) => {
    e.preventDefault()
    setDragOver(true)
  }, [])

  const handleDragLeave = useCallback(() => {
    setDragOver(false)
  }, [])

  const handleInputChange = useCallback(
    (e: React.ChangeEvent<HTMLInputElement>) => {
      const selected = e.target.files?.[0]
      if (selected) handleFile(selected)
    },
    [handleFile],
  )

  const clearFile = useCallback(() => {
    setFile(null)
    if (preview) URL.revokeObjectURL(preview)
    setPreview(null)
    setResult(null)
    setError(null)
    setTierNotice(null)
    setNotice(null)
    if (inputRef.current) inputRef.current.value = ''
  }, [preview])

  // Cleanup blob URLs on unmount and when component receives new preview
  useEffect(() => {
    return () => {
      if (preview) URL.revokeObjectURL(preview)
    }
  }, [preview])

  const handleUpload = async () => {
    if (!file) return
    setUploading(true)
    resetMessages()
    setUploadProgress(0)

    let progressInterval: ReturnType<typeof setInterval> | null = null
    try {
      // Simulate progress
      progressInterval = setInterval(() => {
        setUploadProgress((prev) => Math.min(prev + Math.random() * 30, 90))
      }, 200)

      // Genau EIN Upload pro Klick. Vorher wurde im Projektkontext zusätzlich
      // die Standalone-Route aufgerufen — das speicherte dasselbe Bild zweimal
      // und löste eine zweite (kostenpflichtige) Vision-Analyse aus.
      let raw: unknown
      if (projectId) {
        const img = await uploadProjectImage(projectId, file, imageType, zoneType || undefined)
        onUploadComplete?.(img)
        raw = img
      } else if (boatClass) {
        raw = await uploadAndAnalyzeImage(file, imageType, boatClass, zoneType || undefined)
      } else {
        throw new Error('Ohne Projektbezug wird eine Bootsklasse benötigt.')
      }

      setUploadProgress(100)

      const normalized = normalizeVisualAnalysis(raw)
      if (normalized.result) {
        setResult(normalized.result)
        onAnalysisComplete?.(normalized.result)
      } else if (normalized.tierGated) {
        setTierNotice(normalized.unavailableReason)
      } else {
        setNotice(normalized.unavailableReason)
      }
    } catch (err) {
      const message = err instanceof Error ? err.message : 'Upload fehlgeschlagen.'
      const status = statusOf(err)
      if (status === 401) {
        setError(
          'Bitte melden Sie sich an — die Bildanalyse steht nur angemeldeten Nutzern zur Verfügung.',
        )
      } else if (status === 403 && !projectId) {
        // /images/analyze sperrt Nicht-PRO-Konten hart (VISUAL_TIER_MESSAGE).
        setTierNotice(message)
      } else {
        setError(message)
      }
    } finally {
      if (progressInterval) clearInterval(progressInterval)
      setUploading(false)
      setTimeout(() => setUploadProgress(0), 1000)
    }
  }

  return (
    <div>
      {showHero && (
        <HeroSection
          backgroundVideo={MEDIA.video.yacht_sunset}
          backgroundImage={MEDIA.hero.deck_detail}
          title="Bildanalyse"
          subtitle="Laden Sie Bilder von Yacht-Abschnitten hoch für detaillierte visuelle Analyse und Zustandsbewertung"
          label="Bilder"
        />
      )}

      <div className={`space-y-8 ${showHero ? 'px-6 md:px-10 py-12' : 'py-2'}`}>
        {/* Drop Zone */}
        {!file && (
          <div
            onDrop={handleDrop}
            onDragOver={handleDragOver}
            onDragLeave={handleDragLeave}
            onClick={() => inputRef.current?.click()}
            role="button"
            tabIndex={0}
            onKeyDown={(e) => {
              if (e.key === 'Enter' || e.key === ' ') {
                e.preventDefault()
                inputRef.current?.click()
              }
            }}
            aria-label="Datei-Upload-Bereich. Bild hierher ziehen oder klicken zum Durchsuchen"
            className={`flex flex-col items-center justify-center gap-6 rounded-xl border-2 border-dashed px-8 md:px-12 py-16 cursor-pointer transition-all duration-300 ${
              dragOver
                ? 'animate-pulse-glow border-[rgba(45,139,168,0.6)] bg-[rgba(45,139,168,0.08)]'
                : 'border-ocean-300/60 bg-ocean-50 hover:border-ocean-400/80 hover:bg-ocean-100/50'
            }`}
          >
            <div className="rounded-full bg-ocean-100 p-4 border border-ocean-300 group-hover:border-ocean-500 transition-colors duration-300">
              <Upload className="w-8 h-8 text-ocean-600" />
            </div>
            <div className="text-center">
              <p className="text-sm font-medium text-navy-900 font-serif">
                Bild hierher ziehen oder klicken
              </p>
              <p className="mt-2 text-xs text-navy-600">JPG, PNG, WebP — max. 20 MB</p>
              <p className="mt-1 text-xs text-navy-500">
                HEIC/HEIF (iPhone-Standard) wird nicht unterstützt — bitte als JPG aufnehmen
                oder umwandeln.
              </p>
            </div>
            <input
              ref={inputRef}
              type="file"
              accept={ACCEPT_ATTRIBUTE}
              onChange={handleInputChange}
              className="hidden"
              aria-label="Bilddatei hochladen"
            />
          </div>
        )}

        {/* Preview + Controls */}
        {file && !result && (
          <div className="card-premium p-6 md:p-8 space-y-6 animate-fade-in-scale">
            <div className="flex flex-col md:flex-row gap-6">
              {/* Preview Image */}
              <div className="relative w-full md:w-56 h-48 md:h-40 rounded-lg overflow-hidden bg-sand-100 border border-sand-300 flex-shrink-0">
                {preview ? (
                  <img
                    src={preview}
                    alt="Bildvorschau"
                    className="w-full h-full object-cover animate-fade-in-scale"
                  />
                ) : (
                  <div className="flex items-center justify-center h-full">
                    <ImageIcon className="w-10 h-10 text-navy-600" />
                  </div>
                )}
                <button
                  onClick={clearFile}
                  className="absolute top-2 right-2 p-1.5 rounded-full bg-navy-900/80 border border-navy-700 text-navy-900 hover:text-ocean-700 hover:border-ocean-500 transition-all duration-200 hover:scale-110"
                  aria-label="Bild entfernen"
                >
                  <X className="w-4 h-4" />
                </button>
              </div>

              {/* File info + options */}
              <div className="flex-1 space-y-6">
                <div className="border-b border-sand-200 pb-4">
                  <p className="label-premium mb-1">DATEI</p>
                  <p className="text-navy-900 font-medium text-sm">{file.name}</p>
                  <p className="text-xs text-navy-500 mt-1">
                    {(file.size / 1024 / 1024).toFixed(1)} MB
                  </p>
                </div>

                {/* Image Type Selector */}
                <div>
                  <label className="label-premium mb-2 block">Bildtyp</label>
                  <select
                    value={imageType}
                    onChange={(e) => setImageType(e.target.value as ImageType)}
                    className="w-full rounded-lg border border-sand-200 bg-sand-50/60 px-4 py-2.5 text-sm text-navy-900 focus:border-ocean-500/60 focus:outline-none transition-all duration-200 focus:ring-2 focus:ring-ocean-500/20"
                  >
                    {(Object.entries(IMAGE_TYPE_LABELS) as [ImageType, string][]).map(
                      ([value, label]) => (
                        <option key={value} value={value}>
                          {label}
                        </option>
                      ),
                    )}
                  </select>
                </div>

                {/* Zone (optional) */}
                <div>
                  <label className="label-premium mb-2 block">Zone (Optional)</label>
                  <input
                    type="text"
                    value={zoneType}
                    onChange={(e) => setZoneType(e.target.value)}
                    placeholder="z.B. salon, cabin, pantry"
                    className="w-full rounded-lg border border-sand-200 bg-sand-50/60 px-4 py-2.5 text-sm text-navy-900 placeholder:text-navy-600 focus:border-ocean-500/60 focus:outline-none transition-all duration-200 focus:ring-2 focus:ring-ocean-500/20"
                  />
                </div>
              </div>
            </div>

            {/* Upload Button with Progress */}
            <div className="pt-4 border-t border-navy-700/30 space-y-3">
              {uploading && uploadProgress > 0 && (
                <div className="space-y-2">
                  <div className="flex items-center justify-between text-xs">
                    <span className="text-navy-600">Upload-Fortschritt</span>
                    <span className="text-ocean-600 font-medium">
                      {Math.round(uploadProgress)}%
                    </span>
                  </div>
                  <div className="h-2 bg-sand-100 rounded-full overflow-hidden">
                    <div
                      className="h-full bg-gradient-to-r from-ocean-500 to-ocean-400 rounded-full animate-fill-bar transition-all duration-300"
                      style={{
                        width: `${uploadProgress}%`,
                      }}
                    />
                  </div>
                </div>
              )}
              <button
                onClick={handleUpload}
                disabled={uploading}
                className={`w-full flex items-center justify-center gap-2 rounded-lg bg-ocean-600 hover:bg-ocean-700 px-6 py-3 text-sm font-medium text-white transition-all duration-200 disabled:opacity-50 disabled:cursor-not-allowed active:scale-95 ${
                  uploading ? 'animate-pulse-glow' : ''
                }`}
              >
                {uploading ? (
                  <>
                    <Loader2 className="w-4 h-4 animate-spin" />
                    {projectId ? 'Wird hochgeladen...' : 'Wird analysiert...'}
                  </>
                ) : (
                  <>
                    <Upload className="w-4 h-4" />
                    {projectId ? 'Zum Projekt hochladen' : 'Hochladen & Analysieren'}
                  </>
                )}
              </button>
            </div>
          </div>
        )}

        {/* Tarif-Hinweis: PRO-Feature VISUAL_ANALYSIS */}
        {tierNotice && (
          <div
            className="rounded-xl border border-amber-500/30 bg-amber-500/10 px-6 py-5 flex items-start gap-3 animate-fade-in-scale"
            role="status"
          >
            <Lock className="w-5 h-5 text-amber-600 flex-shrink-0 mt-0.5" />
            <div className="space-y-1">
              <p className="text-sm font-medium text-navy-900">
                KI-Bildanalyse ist im PRO-Tarif enthalten
              </p>
              <p className="text-xs text-navy-600">{tierNotice}</p>
              {projectId && (
                <p className="text-xs text-navy-500">
                  Das Bild wurde am Projekt gespeichert und kann später erneut ausgewertet
                  werden.
                </p>
              )}
            </div>
          </div>
        )}

        {/* Analyse nicht gelaufen (kein Tarif-Grund) */}
        {notice && (
          <div
            className="rounded-xl border border-sand-300 bg-sand-50 px-6 py-5 flex items-start gap-3 animate-fade-in-scale"
            role="status"
          >
            <Info className="w-5 h-5 text-navy-600 flex-shrink-0 mt-0.5" />
            <div className="space-y-1">
              <p className="text-sm font-medium text-navy-900">
                Keine visuelle Analyse verfügbar
              </p>
              <p className="text-xs text-navy-600">{notice}</p>
            </div>
          </div>
        )}

        {/* Error */}
        {error && (
          <div
            className="rounded-lg border border-red-500/30 bg-red-500/10 px-6 py-4 text-sm text-navy-900 animate-fade-in-scale"
            role="alert"
          >
            {error}
          </div>
        )}

        {/* Results */}
        {result && (
          <div className="space-y-6 animate-fade-in-scale">
            <div className="flex flex-col md:flex-row md:items-center md:justify-between gap-4">
              <div>
                <h3 className="font-serif text-lg font-medium text-navy-900">
                  Analyseergebnisse
                </h3>
                <p className="text-xs text-navy-500 mt-1">
                  Detaillierte Bewertung des hochgeladenen Bildes
                </p>
              </div>
              <button
                onClick={clearFile}
                className="text-sm text-ocean-600 hover:text-ocean-700 transition-colors duration-200"
              >
                Neues Bild analysieren
              </button>
            </div>
            <VisualResults result={result} />
          </div>
        )}
      </div>
    </div>
  )
}
