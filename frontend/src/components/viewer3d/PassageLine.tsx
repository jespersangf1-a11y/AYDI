import { useMemo } from 'react'
import * as THREE from 'three'
import { Line } from '@react-three/drei'
import type { ZoneData, PassageData } from '../../types'

interface PassageLineProps {
  passage: PassageData
  zones: ZoneData[]
  zOffset: number
  heightMm: number
}

const MM_TO_UNITS = 0.001

/** Minimum passage width thresholds for color coding (mm) */
const WIDTH_COMFORTABLE = 750
const WIDTH_NARROW = 600

function centroid(polygon: number[][]): [number, number] {
  const n = polygon.length
  if (n === 0) return [0, 0]
  const x = polygon.reduce((s, p) => s + p[0], 0) / n
  const y = polygon.reduce((s, p) => s + p[1], 0) / n
  return [x, y]
}

function getPassageColor(widthMm: number): string {
  if (widthMm >= WIDTH_COMFORTABLE) return '#22c55e'  // green
  if (widthMm >= WIDTH_NARROW) return '#eab308'        // yellow
  return '#ef4444'                                      // red
}

export default function PassageLine({
  passage,
  zones,
  zOffset,
  heightMm,
}: PassageLineProps) {
  const points = useMemo(() => {
    const fromZone = zones.find((z) => z.name === passage.from_zone)
    const toZone = zones.find((z) => z.name === passage.to_zone)
    if (!fromZone || !toZone) return null

    const [fx, fy] = centroid(fromZone.polygon)
    const [tx, ty] = centroid(toZone.polygon)
    const yPos = zOffset * MM_TO_UNITS + heightMm * MM_TO_UNITS * 0.5

    return [
      new THREE.Vector3(fx * MM_TO_UNITS, yPos, fy * MM_TO_UNITS),
      new THREE.Vector3(tx * MM_TO_UNITS, yPos, ty * MM_TO_UNITS),
    ]
  }, [passage, zones, zOffset, heightMm])

  if (!points) return null

  const color = getPassageColor(passage.width_mm)
  const lineWidth = Math.max(1, Math.min(3, passage.width_mm / 300))

  return (
    <Line
      points={points}
      color={color}
      lineWidth={lineWidth}
      transparent
      opacity={passage.is_primary ? 0.8 : 0.4}
      dashed={!passage.is_primary}
      dashSize={0.1}
      gapSize={0.05}
    />
  )
}
