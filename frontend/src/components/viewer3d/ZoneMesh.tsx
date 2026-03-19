import { useMemo, useState, useRef } from 'react'
import * as THREE from 'three'
import { Html } from '@react-three/drei'
import type { ThreeEvent } from '@react-three/fiber'
import type { ZoneData } from '../../types'
import { ZONE_COLORS, ZONE_TYPE_LABELS, DEFAULT_ZONE_COLOR } from './zoneColors'

interface ZoneMeshProps {
  zone: ZoneData
  heightMm: number
  zOffset: number
  selected: boolean
  hasWarning: boolean
  warningSeverity?: 'critical' | 'warning' | 'info'
  wireframe: boolean
  showLabels: boolean
  onSelect: (zoneName: string) => void
}

/** Scale factor: convert mm to Three.js units (meters) */
const MM_TO_UNITS = 0.001

function polygonArea(polygon: number[][]): number {
  const n = polygon.length
  let area = 0
  for (let i = 0; i < n; i++) {
    const j = (i + 1) % n
    area += polygon[i][0] * polygon[j][1]
    area -= polygon[j][0] * polygon[i][1]
  }
  return Math.abs(area) / 2 / 1_000_000
}

export default function ZoneMesh({
  zone,
  heightMm,
  zOffset,
  selected,
  hasWarning,
  warningSeverity,
  wireframe,
  showLabels,
  onSelect,
}: ZoneMeshProps) {
  const [hovered, setHovered] = useState(false)
  const meshRef = useRef<THREE.Mesh>(null)

  const color = ZONE_COLORS[zone.zone_type] ?? DEFAULT_ZONE_COLOR

  const warningOutlineColor = useMemo(() => {
    if (!hasWarning) return null
    if (warningSeverity === 'critical') return '#ef4444'
    if (warningSeverity === 'warning') return '#f59e0b'
    return '#3b82f6'
  }, [hasWarning, warningSeverity])

  // Build the extruded geometry from the 2D polygon
  const geometry = useMemo(() => {
    if (zone.polygon.length < 3) return null

    const shape = new THREE.Shape()
    // Polygon is in mm — convert to units
    const pts = zone.polygon.map(
      (p) => new THREE.Vector2(p[0] * MM_TO_UNITS, p[1] * MM_TO_UNITS)
    )

    shape.moveTo(pts[0].x, pts[0].y)
    for (let i = 1; i < pts.length; i++) {
      shape.lineTo(pts[i].x, pts[i].y)
    }
    shape.closePath()

    const extrudeSettings: THREE.ExtrudeGeometryOptions = {
      depth: heightMm * MM_TO_UNITS,
      bevelEnabled: false,
    }

    const geo = new THREE.ExtrudeGeometry(shape, extrudeSettings)
    // Rotate so extrusion goes along Y (up), not Z
    geo.rotateX(-Math.PI / 2)
    return geo
  }, [zone.polygon, heightMm])

  // Compute centroid for label placement
  const centroid = useMemo(() => {
    const n = zone.polygon.length
    if (n === 0) return new THREE.Vector3(0, 0, 0)
    const cx = zone.polygon.reduce((s, p) => s + p[0], 0) / n
    const cy = zone.polygon.reduce((s, p) => s + p[1], 0) / n
    return new THREE.Vector3(
      cx * MM_TO_UNITS,
      zOffset * MM_TO_UNITS + heightMm * MM_TO_UNITS * 0.5,
      cy * MM_TO_UNITS
    )
  }, [zone.polygon, heightMm, zOffset])

  // Warning outline geometry (slightly larger wireframe)
  const outlineGeometry = useMemo(() => {
    if (!hasWarning || zone.polygon.length < 3) return null

    const shape = new THREE.Shape()
    const pts = zone.polygon.map(
      (p) => new THREE.Vector2(p[0] * MM_TO_UNITS, p[1] * MM_TO_UNITS)
    )

    shape.moveTo(pts[0].x, pts[0].y)
    for (let i = 1; i < pts.length; i++) {
      shape.lineTo(pts[i].x, pts[i].y)
    }
    shape.closePath()

    const extrudeSettings: THREE.ExtrudeGeometryOptions = {
      depth: heightMm * MM_TO_UNITS + 0.005,
      bevelEnabled: false,
    }

    const geo = new THREE.ExtrudeGeometry(shape, extrudeSettings)
    geo.rotateX(-Math.PI / 2)
    return geo
  }, [zone.polygon, heightMm, hasWarning])

  if (!geometry) return null

  const handleClick = (e: ThreeEvent<MouseEvent>) => {
    e.stopPropagation()
    onSelect(zone.name)
  }

  const handlePointerOver = (e: ThreeEvent<PointerEvent>) => {
    e.stopPropagation()
    setHovered(true)
    document.body.style.cursor = 'pointer'
  }

  const handlePointerOut = () => {
    setHovered(false)
    document.body.style.cursor = 'auto'
  }

  const opacity = selected ? 0.85 : hovered ? 0.7 : 0.55
  const area = polygonArea(zone.polygon)
  const typeLabel = ZONE_TYPE_LABELS[zone.zone_type] ?? zone.zone_type

  return (
    <group position={[0, zOffset * MM_TO_UNITS, 0]}>
      {/* Main zone mesh */}
      <mesh
        ref={meshRef}
        geometry={geometry}
        onClick={handleClick}
        onPointerOver={handlePointerOver}
        onPointerOut={handlePointerOut}
      >
        <meshStandardMaterial
          color={color}
          transparent
          opacity={opacity}
          wireframe={wireframe}
          side={THREE.DoubleSide}
        />
      </mesh>

      {/* Warning outline */}
      {hasWarning && outlineGeometry && warningOutlineColor && (
        <mesh geometry={outlineGeometry} position={[0, -0.002, 0]}>
          <meshBasicMaterial
            color={warningOutlineColor}
            wireframe
            transparent
            opacity={0.8}
          />
        </mesh>
      )}

      {/* Selection outline */}
      {selected && (
        <mesh geometry={geometry}>
          <meshBasicMaterial
            color="#ffffff"
            wireframe
            transparent
            opacity={0.6}
          />
        </mesh>
      )}

      {/* Hover label */}
      {(hovered || showLabels) && (
        <Html position={centroid} center distanceFactor={15} zIndexRange={[10, 0]}>
          <div
            className="bg-navy-800 border border-navy-600 rounded px-2 py-1 text-xs whitespace-nowrap pointer-events-none select-none"
            style={{ color: 'white' }}
          >
            <span className="font-medium">{zone.name}</span>
            {hovered && (
              <>
                <br />
                <span className="text-navy-300">{typeLabel}</span>
                <br />
                <span className="font-mono text-navy-300">
                  {area.toFixed(1)} m&sup2;
                </span>
              </>
            )}
          </div>
        </Html>
      )}
    </group>
  )
}
