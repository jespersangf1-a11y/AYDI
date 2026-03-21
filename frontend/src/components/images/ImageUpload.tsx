import { useState, useRef, useCallback, useEffect } from 'react'
import { Upload, X, Loader2, ImageIcon } from 'lucide-react'
import type { BoatClass, ImageType, ImageAnalysisResult, ImageUploadData } from '../../types'
import { IMAGE_TYPE_LABELS } from '../../types'
import { uploadAndAnalyzeImage, uploadProjectImage } from '../../services/api'
import VisualResults from './VisualResults'
import { MEDIA } from '../../config/media'
import HeroSection from '../layout/HeroSection'

interface ImageUploadProps {
  boatClass: BoatClass
  projectId?: string
  onAnalysisComplete?: (result: ImageAnalysisResult) => void
  onUploadComplete?: (image: ImageUploadData) => void
}

const MAX_FILE_SIZE = 20 * 1024 * 1024 // 20 MB
const ACCEPTED_TYPES = ['image/jpeg', 'image/png', 'image/webp', 'image/heic']

export default function ImageUpload({
  boatClass,
  projectId,
  onAnalysisComplete,
  onUploadComplete,
}: ImageUploadProps) {
  const [file, setFile] = useState<File | null>(null)
  const [preview, setPreview] = useState<string | null>(null)
  const [imageType, setImageType] = useState<ImageType>('interior_overview')
  const [zoneType, setZoneType] = useState('')
  const [uploading, setUploading] = useState(false)
  const [error, setError] = useState<string | null>(null)
  const [result, setResult] = useState<ImageAnalysisResult | null>(null)
  const [dragOver, setDragOver] = useState(false)
  const inputRef = useRef<HTMLInputElement>(null)

  const handleFile = useCallback((f: File) => {
    setError(null)
    setResult(null)

    if (!ACCEPTED_TYPES.includes(f.type) && !f.name.toLowerCase().endsWith('.heic')) {
      setError('Ungültiges Dateiformat. Erlaubt: JPG, PNG, WebP, HEIC.')
      return
    }
    if (f.size > MAX_FILE_SIZE) {
      setError('Datei zu groß. Maximal 20 MB erlaubt.')
      return
    }

    setFile(f)
    const url = URL.createObjectURL(f)
    setPreview(url)
  }, [])

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
    setError(null)

    try {
      if (projectId) {
        const img = await uploadProjectImage(
          projectId,
          file,
          imageType,
          zoneType || undefined,
        )
        onUploadComplete?.(img)
      }

      const analysisResult = await uploadAndAnalyzeImage(
        file,
        imageType,
        boatClass,
        zoneType || undefined,
      )
      setResult(analysisResult)
      onAnalysisComplete?.(analysisResult)
    } catch (err) {
      setError(err instanceof Error ? err.message : 'Upload fehlgeschlagen.')
    } finally {
      setUploading(false)
    }
  }

  return (
    <div>
      <HeroSection
        backgroundImage={MEDIA.hero.deck_detail}
        title="Bildanalyse"
        subtitle="Laden Sie Bilder von Yacht-Abschnitten hoch fr detaillierte visuelle Analyse und Zustandsbewertung"
        label="Bilder"
      />

      <div className="space-y-8 px-10 py-12">
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
            className={`flex flex-col items-center justify-center gap-6 rounded-xl border-2 border-dashed px-12 py-16 cursor-pointer transition-all duration-200 ${
              dragOver
                ? 'border-ocean-400 bg-ocean-400/10'
                : 'border-navy-600/50 bg-navy-900/20 hover:border-navy-500 hover:bg-navy-900/30'
            }`}
          >
            <div className="rounded-full bg-navy-800/40 p-4 border border-navy-600/30">
              <Upload className="w-8 h-8 text-ocean-400" />
            </div>
            <div className="text-center">
              <p className="text-sm font-medium text-navy-100 font-serif">
                Bild hierher ziehen oder klicken
              </p>
              <p className="mt-2 text-xs text-navy-400">
                JPG, PNG, WebP, HEIC — max. 20 MB
              </p>
            </div>
            <input
              ref={inputRef}
              type="file"
              accept=".jpg,.jpeg,.png,.webp,.heic"
              onChange={handleInputChange}
              className="hidden"
            />
          </div>
        )}

        {/* Preview + Controls */}
        {file && !result && (
          <div className="card-premium p-8 space-y-6">
            <div className="flex items-start gap-6">
              {/* Preview Image */}
              <div className="relative w-56 h-40 rounded-lg overflow-hidden bg-navy-800/60 border border-navy-700/30 flex-shrink-0">
                {preview ? (
                  <img
                    src={preview}
                    alt="Vorschau"
                    className="w-full h-full object-cover"
                  />
                ) : (
                  <div className="flex items-center justify-center h-full">
                    <ImageIcon className="w-10 h-10 text-navy-600" />
                  </div>
                )}
                <button
                  onClick={clearFile}
                  className="absolute top-2 right-2 p-1.5 rounded-full bg-navy-950/80 border border-navy-600 text-navy-300 hover:text-ocean-300 hover:border-ocean-500 transition-colors duration-200"
                >
                  <X className="w-4 h-4" />
                </button>
              </div>

              {/* File info + options */}
              <div className="flex-1 space-y-6">
                <div className="border-b border-navy-700/30 pb-4">
                  <p className="label-premium mb-1">DATEI</p>
                  <p className="text-white font-medium text-sm">{file.name}</p>
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
                    className="w-full rounded-lg border border-navy-600/40 bg-navy-800/60 px-4 py-2.5 text-sm text-navy-100 focus:border-ocean-500/60 focus:outline-none transition-colors duration-200"
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

                {/* Zone Type (optional) */}
                <div>
                  <label className="label-premium mb-2 block">Zonentyp (Optional)</label>
                  <input
                    type="text"
                    value={zoneType}
                    onChange={(e) => setZoneType(e.target.value)}
                    placeholder="z.B. salon, cabin, pantry"
                    className="w-full rounded-lg border border-navy-600/40 bg-navy-800/60 px-4 py-2.5 text-sm text-navy-100 placeholder:text-navy-600 focus:border-ocean-500/60 focus:outline-none transition-colors duration-200"
                  />
                </div>
              </div>
            </div>

            {/* Upload Button */}
            <div className="pt-4 border-t border-navy-700/30">
              <button
                onClick={handleUpload}
                disabled={uploading}
                className="w-full flex items-center justify-center gap-2 rounded-lg bg-ocean-700 hover:bg-ocean-600 px-6 py-3 text-sm font-medium text-white disabled:opacity-50 disabled:cursor-not-allowed transition-colors duration-200"
              >
                {uploading ? (
                  <>
                    <Loader2 className="w-4 h-4 animate-spin" />
                    Wird analysiert...
                  </>
                ) : (
                  <>
                    <Upload className="w-4 h-4" />
                    Hochladen & Analysieren
                  </>
                )}
              </button>
            </div>
          </div>
        )}

        {/* Error */}
        {error && (
          <div className="rounded-lg border border-red-500/20 bg-red-950/20 px-6 py-4 text-sm text-red-300">
            {error}
          </div>
        )}

        {/* Results */}
        {result && (
          <div className="space-y-6">
            <div className="flex items-center justify-between">
              <div>
                <h3 className="font-serif text-lg font-medium text-white">
                  Analyseergebnisse
                </h3>
                <p className="text-xs text-navy-500 mt-1">Detaillierte Bewertung des hochgeladenen Bildes</p>
              </div>
              <button
                onClick={clearFile}
                className="text-sm text-ocean-400 hover:text-ocean-300 transition-colors duration-200"
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
