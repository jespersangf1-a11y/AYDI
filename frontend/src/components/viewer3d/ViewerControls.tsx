import {
  Eye,
  EyeOff,
  Box,
  Grid3X3,
  Tag,
  AlertTriangle,
  RotateCcw,
  ArrowUp,
  ArrowRight,
  ArrowDown,
  Maximize2,
} from 'lucide-react'

interface DeckVisibility {
  deckNumber: number
  name: string
  visible: boolean
}

interface ViewerControlsProps {
  exploded: boolean
  wireframe: boolean
  showLabels: boolean
  showWarnings: boolean
  deckVisibility: DeckVisibility[]
  onToggleExploded: () => void
  onToggleWireframe: () => void
  onToggleLabels: () => void
  onToggleWarnings: () => void
  onToggleDeck: (deckNumber: number) => void
  onCameraPreset: (preset: 'top' | 'side' | 'front' | 'perspective') => void
}

export default function ViewerControls({
  exploded,
  wireframe,
  showLabels,
  showWarnings,
  deckVisibility,
  onToggleExploded,
  onToggleWireframe,
  onToggleLabels,
  onToggleWarnings,
  onToggleDeck,
  onCameraPreset,
}: ViewerControlsProps) {
  return (
    <div className="absolute top-3 left-3 z-10 flex flex-col gap-2">
      {/* Camera presets */}
      <div className="bg-sand-50/90 backdrop-blur-sm border border-navy-600 rounded-lg p-1.5 flex gap-1">
        <ControlButton
          title="Draufsicht"
          onClick={() => onCameraPreset('top')}
          icon={<ArrowDown className="w-4 h-4" />}
        />
        <ControlButton
          title="Seitenansicht"
          onClick={() => onCameraPreset('side')}
          icon={<ArrowRight className="w-4 h-4" />}
        />
        <ControlButton
          title="Frontansicht"
          onClick={() => onCameraPreset('front')}
          icon={<ArrowUp className="w-4 h-4" />}
        />
        <ControlButton
          title="Perspektive (Reset)"
          onClick={() => onCameraPreset('perspective')}
          icon={<RotateCcw className="w-4 h-4" />}
        />
      </div>

      {/* Toggle controls */}
      <div className="bg-sand-50/90 backdrop-blur-sm border border-navy-600 rounded-lg p-1.5 flex flex-col gap-1">
        <ToggleButton
          title="Explosionsansicht"
          active={exploded}
          onClick={onToggleExploded}
          icon={<Maximize2 className="w-4 h-4" />}
          label="Explosionsansicht"
        />
        <ToggleButton
          title="Drahtgitter"
          active={wireframe}
          onClick={onToggleWireframe}
          icon={<Grid3X3 className="w-4 h-4" />}
          label="Drahtgitter"
        />
        <ToggleButton
          title="Beschriftungen"
          active={showLabels}
          onClick={onToggleLabels}
          icon={<Tag className="w-4 h-4" />}
          label="Beschriftungen"
        />
        <ToggleButton
          title="Warnungen"
          active={showWarnings}
          onClick={onToggleWarnings}
          icon={<AlertTriangle className="w-4 h-4" />}
          label="Warnungen"
        />
      </div>

      {/* Deck visibility */}
      {deckVisibility.length > 1 && (
        <div className="bg-sand-50/90 backdrop-blur-sm border border-navy-600 rounded-lg p-2">
          <p className="text-navy-700 text-xs font-medium mb-1.5 font-heading">
            Decks
          </p>
          {deckVisibility.map((deck) => (
            <label
              key={deck.deckNumber}
              className="flex items-center gap-2 text-xs text-navy-900 cursor-pointer py-0.5 hover:text-ocean-700"
            >
              <button
                onClick={() => onToggleDeck(deck.deckNumber)}
                className="flex-shrink-0"
                title={deck.visible ? 'Deck ausblenden' : 'Deck einblenden'}
              >
                {deck.visible ? (
                  <Eye className="w-3.5 h-3.5 text-ocean-600" />
                ) : (
                  <EyeOff className="w-3.5 h-3.5 text-navy-500" />
                )}
              </button>
              <span className={deck.visible ? '' : 'text-navy-500'}>
                {deck.name}
              </span>
            </label>
          ))}
        </div>
      )}
    </div>
  )
}

function ControlButton({
  title,
  onClick,
  icon,
}: {
  title: string
  onClick: () => void
  icon: React.ReactNode
}) {
  return (
    <button
      onClick={onClick}
      title={title}
      className="p-1.5 rounded text-navy-700 hover:text-navy-900 hover:bg-navy-700 transition-colors"
    >
      {icon}
    </button>
  )
}

function ToggleButton({
  title,
  active,
  onClick,
  icon,
  label,
}: {
  title: string
  active: boolean
  onClick: () => void
  icon: React.ReactNode
  label: string
}) {
  return (
    <button
      onClick={onClick}
      title={title}
      className={`flex items-center gap-2 px-2 py-1 rounded text-xs transition-colors ${
        active
          ? 'bg-ocean-600/30 text-ocean-600'
          : 'text-navy-700 hover:text-navy-900 hover:bg-navy-700'
      }`}
    >
      {active ? icon : <Box className="w-4 h-4" />}
      <span>{label}</span>
    </button>
  )
}
