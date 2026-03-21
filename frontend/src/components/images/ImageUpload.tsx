import { useState, useRef, useCallback, useEffect } from 'react'
import { Upload, X, Loader2, ImageIcon } from 'lucide-react'
import type { BoatClass, ImageType, ImageAnalysisResult, ImageUploadData } from '../../types'
import { IMAGE_TYPE_LABELS } from '../../types'
import { uploadAndAnalyzeImage, uploadProjectImage } from '../../services/api'
import VisualResults from './VisualResults'

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
    <div className="space-y-6">
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
          className={`flex flex-col items-center justify-center gap-4 rounded-xl border-2 border-dashed p-12 cursor-pointer transition-colors ${
            dragOver
              ? 'border-ocean-400 bg-ocean-400/10'
              : 'border-navy-600 bg-navy-900/50 hover:border-navy-500 hover:bg-navy-900'
          }`}
        >
          <Upload className="w-10 h-10 text-navy-400" />
          <div className="text-center">
            <p className="text-sm font-medium text-navy-200">
              Bild hierher ziehen oder klicken zum Durchsuchen
            </p>
            <p className="mt-1 text-xs text-navy-500">
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
        <div className="rounded-xl border border-navy-700 bg-navy-900 p-6 space-y-5">
          <div className="flex items-start gap-5">
            {/* Preview Image */}
            <div className="relative w-48 h-36 rounded-lg overflow-hidden bg-navy-800 flex-shrink-0">
              {preview ? (
                <img
                  src={preview}
                  alt="Vorschau"
                  className="w-full h-full object-cover"
                />
              ) : (
                <div className="flex items-center justify-center h-full">
                  <ImageIcon className="w-8 h-8 text-navy-600" />
                </div>
              )}
              <button
                onClick={clearFile}
                className="absolute top-1 right-1 p-1 rounded-full bg-navy-900/80 text-navy-300 hover:text-white transition-colors"
              >
                <X className="w-4 h-4" />
              </button>
            </div>

            {/* File info + options */}
            <div className="flex-1 space-y-4">
              <div>
                <p className="text-sm font-medium text-navy-200">{file.name}</p>
                <p className="text-xs text-navy-500">
                  {(file.size / 1024 / 1024).toFixed(1)} MB
                </p>
              </div>

              {/* Image Type Selector */}
              <div>
                <label className="block text-xs font-medium text-navy-400 mb-1">
                  Bildtyp
                </label>
                <select
                  value={imageType}
                  onChange={(e) => setImageType(e.target.value as ImageType)}
                  className="w-full rounded-lg border border-navy-600 bg-navy-800 px-3 py-2 text-sm text-navy-200 focus:border-ocean-500 focus:outline-none"
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
                <label className="block text-xs font-medium text-navy-400 mb-1">
                  Zonentyp (optional)
                </label>
                <input
                  type="text"
                  value={zoneType}
                  onChange={(e) => setZoneType(e.target.value)}
                  placeholder="z.B. salon, cabin, pantry"
                  className="w-full rounded-lg border border-navy-600 bg-navy-800 px-3 py-2 text-sm text-navy-200 placeholder:text-navy-600 focus:border-ocean-500 focus:outline-none"
                />
              </div>
            </div>
          </div>

          {/* Upload Button */}
          <button
            onClick={handleUpload}
            disabled={uploading}
            className="w-full flex items-center justify-center gap-2 rounded-lg bg-ocean-600 px-4 py-2.5 text-sm font-medium text-white hover:bg-ocean-500 disabled:opacity-50 disabled:cursor-not-allowed transition-colors"
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
      )}

      {/* Error */}
      {error && (
        <div className="rounded-lg border border-red-500/30 bg-red-500/10 px-4 py-3 text-sm text-red-400">
          {error}
        </div>
      )}

      {/* Results */}
      {result && (
        <div className="space-y-4">
          <div className="flex items-center justify-between">
            <h3 className="font-heading text-lg font-semibold text-white">
              Analyseergebnisse
            </h3>
            <button
              onClick={clearFile}
              className="text-sm text-ocean-400 hover:text-ocean-300 transition-colors"
            >
              Neues Bild analysieren
            </button>
          </div>
          <VisualResults result={result} />
        </div>
      )}
    </div>
  )
}
