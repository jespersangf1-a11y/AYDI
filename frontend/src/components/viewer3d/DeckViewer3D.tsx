import { useState, useMemo, useCallback, useRef } from 'react'
import { Canvas } from '@react-three/fiber'
import { OrbitControls, Grid, Html } from '@react-three/drei'
import type { OrbitControls as OrbitControlsImpl } from 'three-stdlib'
import * as THREE from 'three'
import type { ZoneData, PassageData, WarningData } from '../../types'
import ZoneMesh from './ZoneMesh'
import PassageLine from './PassageLine'
import ViewerControls from './ViewerControls'
import ViewerInfoPanel from './ViewerInfoPanel'

interface DeckInput {
  deck_number: number
  name: string
  z_offset_mm: number
  height_mm: number
  zones: ZoneData[]
}

interface DeckViewer3DProps {
  zones: ZoneData[]
  passages: PassageData[]
  decks?: DeckInput[]
  warnings?: WarningData[]
  selectedZone?: string | null
  onZoneSelect?: (zoneName: string) => void
  deckSpacing?: number
}

const MM_TO_UNITS = 0.001
const DEFAULT_DECK_HEIGHT_MM = 2000
const DEFAULT_DECK_SPACING_MM = 500
const EXPLODE_EXTRA_MM = 1500

type CameraPreset = 'top' | 'side' | 'front' | 'perspective'

/** Compute the bounding box center of all zone polygons (in Three.js units). */
function computeSceneCenter(allZones: ZoneData[]): THREE.Vector3 {
  const pts = allZones.flatMap((z) => (Array.isArray(z.polygon) ? z.polygon : []))
  if (pts.length === 0) return new THREE.Vector3(0, 0, 0)
  const minX = Math.min(...pts.map((p) => p[0]))
  const maxX = Math.max(...pts.map((p) => p[0]))
  const minY = Math.min(...pts.map((p) => p[1]))
  const maxY = Math.max(...pts.map((p) => p[1]))
  return new THREE.Vector3(
    ((minX + maxX) / 2) * MM_TO_UNITS,
    0,
    ((minY + maxY) / 2) * MM_TO_UNITS
  )
}

/** Compute camera distance based on scene extent. */
function computeCameraDistance(allZones: ZoneData[]): number {
  const pts = allZones.flatMap((z) => (Array.isArray(z.polygon) ? z.polygon : []))
  if (pts.length === 0) return 15
  const minX = Math.min(...pts.map((p) => p[0]))
  const maxX = Math.max(...pts.map((p) => p[0]))
  const minY = Math.min(...pts.map((p) => p[1]))
  const maxY = Math.max(...pts.map((p) => p[1]))
  const dx = (maxX - minX) * MM_TO_UNITS
  const dy = (maxY - minY) * MM_TO_UNITS
  return Math.max(dx, dy) * 1.2
}

export default function DeckViewer3D({
  zones,
  passages,
  decks,
  warnings = [],
  selectedZone: controlledSelected,
  onZoneSelect,
  deckSpacing = DEFAULT_DECK_SPACING_MM,
}: DeckViewer3DProps) {
  const [internalSelected, setInternalSelected] = useState<string | null>(null)
  const [exploded, setExploded] = useState(false)
  const [wireframe, setWireframe] = useState(false)
  const [showLabels, setShowLabels] = useState(false)
  const [showWarnings, setShowWarnings] = useState(true)
  const controlsRef = useRef<OrbitControlsImpl>(null)

  const selectedZoneName = controlledSelected ?? internalSelected

  // Normalise input: single-deck mode or multi-deck mode
  const normalizedDecks: DeckInput[] = useMemo(() => {
    if (decks && decks.length > 0) return decks
    // Single-deck mode: put all zones on deck 0
    return [
      {
        deck_number: 0,
        name: 'Hauptdeck',
        z_offset_mm: 0,
        height_mm: DEFAULT_DECK_HEIGHT_MM,
        zones,
      },
    ]
  }, [decks, zones])

  // All zones flattened (for bounding box, etc.)
  const allZones = useMemo(
    () => normalizedDecks.flatMap((d) => d.zones),
    [normalizedDecks]
  )

  // Deck visibility state
  const [deckVisibility, setDeckVisibility] = useState<Record<number, boolean>>(
    () => {
      const vis: Record<number, boolean> = {}
      normalizedDecks.forEach((d) => {
        vis[d.deck_number] = true
      })
      return vis
    }
  )

  // Scene geometry helpers
  const sceneCenter = useMemo(() => computeSceneCenter(allZones), [allZones])
  const cameraDist = useMemo(() => computeCameraDistance(allZones), [allZones])

  // Warning lookup by zone name
  const warningsByZone = useMemo(() => {
    const map = new Map<string, WarningData[]>()
    for (const w of warnings) {
      if (!w.location) continue
      const loc = w.location.toLowerCase()
      for (const zone of allZones) {
        if (loc.includes(zone.name.toLowerCase())) {
          const existing = map.get(zone.name) ?? []
          existing.push(w)
          map.set(zone.name, existing)
        }
      }
    }
    return map
  }, [warnings, allZones])

  // Worst severity for a zone
  const worstSeverity = useCallback(
    (zoneName: string): 'critical' | 'warning' | 'info' | undefined => {
      const zw = warningsByZone.get(zoneName)
      if (!zw || zw.length === 0) return undefined
      if (zw.some((w) => w.severity === 'critical')) return 'critical'
      if (zw.some((w) => w.severity === 'warning')) return 'warning'
      return 'info'
    },
    [warningsByZone]
  )

  // Zone selection handler
  const handleZoneSelect = useCallback(
    (name: string) => {
      const newVal = name === selectedZoneName ? null : name
      setInternalSelected(newVal)
      if (onZoneSelect && newVal) {
        onZoneSelect(newVal)
      }
    },
    [selectedZoneName, onZoneSelect]
  )

  // Camera preset handler
  const handleCameraPreset = useCallback(
    (preset: CameraPreset) => {
      const controls = controlsRef.current
      if (!controls) return

      const target = sceneCenter.clone()
      target.y = cameraDist * 0.15 // slightly above ground for better framing
      controls.target.copy(target)

      const d = cameraDist
      switch (preset) {
        case 'top':
          controls.object.position.set(target.x, target.y + d, target.z)
          break
        case 'side':
          controls.object.position.set(target.x + d, target.y + d * 0.3, target.z)
          break
        case 'front':
          controls.object.position.set(target.x, target.y + d * 0.3, target.z + d)
          break
        case 'perspective':
          controls.object.position.set(
            target.x + d * 0.6,
            target.y + d * 0.5,
            target.z + d * 0.6
          )
          break
      }
      controls.update()
    },
    [sceneCenter, cameraDist]
  )

  // Toggle deck visibility
  const handleToggleDeck = useCallback((deckNumber: number) => {
    setDeckVisibility((prev) => ({
      ...prev,
      [deckNumber]: !prev[deckNumber],
    }))
  }, [])

  // Build deck visibility list for controls
  const deckVisList = useMemo(
    () =>
      normalizedDecks.map((d) => ({
        deckNumber: d.deck_number,
        name: d.name,
        visible: deckVisibility[d.deck_number] ?? true,
      })),
    [normalizedDecks, deckVisibility]
  )

  // Selected zone object
  const selectedZoneObj = useMemo(
    () => allZones.find((z) => z.name === selectedZoneName) ?? null,
    [allZones, selectedZoneName]
  )

  // Warnings for selected zone
  const selectedZoneWarnings = useMemo(
    () =>
      selectedZoneName ? warningsByZone.get(selectedZoneName) ?? [] : [],
    [selectedZoneName, warningsByZone]
  )

  // Grid size based on scene
  const gridSize = Math.ceil(cameraDist * 1.5)

  return (
    <div className="relative w-full h-full min-h-[400px] bg-sand-50 rounded-xl border border-sand-200 overflow-hidden">
      {/* Toolbar overlay */}
      <ViewerControls
        exploded={exploded}
        wireframe={wireframe}
        showLabels={showLabels}
        showWarnings={showWarnings}
        deckVisibility={deckVisList}
        onToggleExploded={() => setExploded((v) => !v)}
        onToggleWireframe={() => setWireframe((v) => !v)}
        onToggleLabels={() => setShowLabels((v) => !v)}
        onToggleWarnings={() => setShowWarnings((v) => !v)}
        onToggleDeck={handleToggleDeck}
        onCameraPreset={handleCameraPreset}
      />

      {/* Info panel */}
      <ViewerInfoPanel
        zone={selectedZoneObj}
        warnings={selectedZoneWarnings}
        onClose={() => {
          setInternalSelected(null)
        }}
      />

      {/* 3D Canvas */}
      <Canvas
        camera={{
          position: [
            sceneCenter.x + cameraDist * 0.6,
            sceneCenter.y + cameraDist * 0.5,
            sceneCenter.z + cameraDist * 0.6,
          ],
          fov: 50,
          near: 0.1,
          far: cameraDist * 10,
        }}
        style={{ width: '100%', height: '100%' }}
        onPointerMissed={() => {
          setInternalSelected(null)
        }}
      >
        {/* Lighting */}
        <ambientLight intensity={0.5} />
        <directionalLight
          position={[cameraDist * 0.5, cameraDist, cameraDist * 0.3]}
          intensity={0.8}
          castShadow={false}
        />
        <directionalLight
          position={[-cameraDist * 0.3, cameraDist * 0.5, -cameraDist * 0.2]}
          intensity={0.3}
        />

        {/* Sky-colored background */}
        <color attach="background" args={['#0d1423']} />

        {/* Grid floor */}
        <Grid
          args={[gridSize, gridSize]}
          cellSize={1}
          sectionSize={5}
          cellColor="#273c69"
          sectionColor="#34508c"
          fadeDistance={cameraDist * 2}
          fadeStrength={1}
          position={[sceneCenter.x, -0.01, sceneCenter.z]}
        />

        {/* Render decks */}
        {normalizedDecks.map((deck) => {
          const isVisible = deckVisibility[deck.deck_number] ?? true
          if (!isVisible) return null

          const explodeOffset = exploded
            ? deck.deck_number * (deckSpacing + EXPLODE_EXTRA_MM)
            : 0
          const effectiveZOffset = deck.z_offset_mm + explodeOffset

          return (
            <group key={deck.deck_number}>
              {/* Zone meshes */}
              {deck.zones.map((zone) => {
                const hasW =
                  showWarnings && warningsByZone.has(zone.name)
                return (
                  <ZoneMesh
                    key={`${deck.deck_number}-${zone.name}`}
                    zone={zone}
                    heightMm={zone.height_mm ?? deck.height_mm}
                    zOffset={effectiveZOffset}
                    selected={zone.name === selectedZoneName}
                    hasWarning={hasW}
                    warningSeverity={worstSeverity(zone.name)}
                    wireframe={wireframe}
                    showLabels={showLabels}
                    onSelect={handleZoneSelect}
                  />
                )
              })}

              {/* Passage lines */}
              {passages.map((p, i) => (
                <PassageLine
                  key={`passage-${deck.deck_number}-${i}`}
                  passage={p}
                  zones={deck.zones}
                  zOffset={effectiveZOffset}
                  heightMm={deck.height_mm}
                />
              ))}

              {/* Deck label */}
              {normalizedDecks.length > 1 && (
                <DeckLabel
                  name={deck.name}
                  zOffset={effectiveZOffset}
                  heightMm={deck.height_mm}
                  xPosition={sceneCenter.x - cameraDist * 0.45}
                  zPosition={sceneCenter.z}
                />
              )}
            </group>
          )
        })}

        {/* Orbit controls */}
        <OrbitControls
          ref={controlsRef}
          target={sceneCenter}
          enableDamping
          dampingFactor={0.1}
          minDistance={cameraDist * 0.2}
          maxDistance={cameraDist * 3}
        />
      </Canvas>
    </div>
  )
}

/** Floating deck label beside each deck */
function DeckLabel({
  name,
  zOffset,
  heightMm,
  xPosition,
  zPosition,
}: {
  name: string
  zOffset: number
  heightMm: number
  xPosition: number
  zPosition: number
}) {
  const yPos = zOffset * MM_TO_UNITS + (heightMm * MM_TO_UNITS) / 2
  return (
    <Html
      position={[xPosition, yPos, zPosition]}
      center
      distanceFactor={12}
      zIndexRange={[5, 0]}
    >
      <div className="bg-white border border-sand-200 rounded px-2 py-0.5 text-xs text-ocean-600 font-heading font-medium whitespace-nowrap pointer-events-none select-none shadow-sm">
        {name}
      </div>
    </Html>
  )
}
