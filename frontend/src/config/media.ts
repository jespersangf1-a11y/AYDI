/**
 * AYDI Media Configuration
 * All background images and videos for the platform.
 * Using Unsplash for high-quality, freely licensed photography.
 * Using Pexels for royalty-free video backgrounds.
 */

const UNSPLASH_BASE = 'https://images.unsplash.com'

// Quality presets
const hero = (id: string) => `${UNSPLASH_BASE}/${id}?auto=format&fit=crop&w=1920&q=80`
const section = (id: string) => `${UNSPLASH_BASE}/${id}?auto=format&fit=crop&w=1200&q=80`

export const MEDIA = {
  // General / Hero backgrounds
  hero: {
    aerial_yacht: hero('photo-1567899378494-47b22a2ae96a'),      // Aerial yacht on blue water
    ocean_horizon: hero('photo-1505142468610-359e7d316be0'),      // Ocean horizon calm
    deck_detail: hero('photo-1540946485063-a40da27545f8'),        // Yacht deck teak
    sailing_wide: hero('photo-1534438327276-14e5300c3a48'),       // Wide sailing shot
  },

  // Video backgrounds (locally served from public/videos/ — downloaded via download-videos.ps1)
  video: {
    ocean_calm: '/videos/ocean-calm.mp4',
    sailing_aerial: '/videos/sailing-aerial.mp4',
    ocean_waves: '/videos/ocean-waves.mp4',
    yacht_sunset: '/videos/yacht-sunset.mp4',
    yacht_sailing: '/videos/yacht-sailing.mp4',
    boat_sea: '/videos/boat-sea.mp4',
    sailing_ocean: '/videos/sailing-ocean.mp4',
  },

  // ===================================================================
  // BEREICHSSPEZIFISCHE MEDIEN (2 Bilder + 1 Video pro Bereich)
  // ===================================================================

  // Rumpf / Struktur (Hull / Structure)
  structure: {
    hull_waterline: hero('photo-1569263979104-865ab7cd8d13'),     // Yacht hull line
    hull_drydock: hero('photo-1559134197-64a0a4c40502'),          // Boat in dry dock
    // Video: ocean_calm (Unterwasser/Rumpf-nah)
  },

  // Materialien (Materials)
  materials: {
    teak_deck: hero('photo-1558618666-fcd25c85f82e'),             // Teak wood grain
    marine_hardware: hero('photo-1544551763-46a013bb70d5'),       // Marine hardware detail
    // Video: boat_sea
  },

  // Elektrik / Elektronik (Electrical)
  electrical: {
    nav_instruments: hero('photo-1559136555-9303baea8ebd'),       // Navigation instruments
    helm_night: hero('photo-1544620347-c4fd4a3d5957'),            // Helm illuminated
    // Video: yacht_sunset
  },

  // Interieur (Interior)
  interior: {
    salon: hero('photo-1605281317010-fe5ffe798166'),              // Luxury yacht interior
    cabin: hero('photo-1540946485063-a40da27545f8'),              // Yacht cabin/deck
    // Video: yacht_sailing
  },

  // Rigg / Segel (Rigging / Sails)
  rigging: {
    under_sail: hero('photo-1534438327276-14e5300c3a48'),         // Sailing yacht dramatic
    winch_detail: hero('photo-1535532901685-188aafe0c77d'),       // Rigging winch detail
    // Video: sailing_aerial
  },

  // Antrieb (Propulsion)
  propulsion: {
    engine_room: hero('photo-1530103862676-de8c9debad1d'),        // Engine
    propeller: hero('photo-1507003211169-0a1dd7228f2d'),          // Underwater propeller
    // Video: ocean_waves
  },

  // Quick Analysis / Overview
  overview: {
    blueprint: section('photo-1504711331183-9c7b2d1a5748'),       // Technical drawings
    marina_aerial: hero('photo-1545579133-99bb5ab189bd'),         // Marina from above
  },

  // ===================================================================
  // ÜBERGREIFENDE ATMOSPHÄRE-BILDER (3-5 Premium-Shots)
  // ===================================================================
  atmosphere: {
    yacht_aerial_turquoise: hero('photo-1567899378494-47b22a2ae96a'),  // Aerial yacht turquoise water
    sunset_sailing: hero('photo-1505142468610-359e7d316be0'),          // Ocean horizon golden hour
    marina_panorama: hero('photo-1545579133-99bb5ab189bd'),            // Marina panorama from above
    deck_lifestyle: hero('photo-1540946485063-a40da27545f8'),          // On-deck lifestyle
    ocean_dramatic: hero('photo-1534438327276-14e5300c3a48'),          // Dramatic sailing wide shot
  },
} as const

export type MediaCategory = keyof typeof MEDIA

// =====================================================================
// HERO CAROUSEL — Endlos-Slideshow für die Startseite
// Alle Bereiche durchmixt: 2 Bilder + 1 Video pro Bereich + Übergreifende
// =====================================================================

export interface CarouselSlide {
  type: 'image' | 'video'
  src: string
  domain: string        // Bereich-Label für optionale Einblendung
  domainDe: string      // Deutscher Bereich-Name
}

/**
 * Kuratierte Medien-Reihenfolge für die Startseite.
 * Die Reihenfolge mixt Bereiche und Medientypen für maximale Abwechslung.
 * Jeder Bereich hat 2 Bilder + 1 Video, dazwischen Atmosphäre-Bilder.
 */
export const HERO_CAROUSEL_SLIDES: CarouselSlide[] = [
  // -- Start: Atmosphäre --
  { type: 'image', src: MEDIA.atmosphere.yacht_aerial_turquoise, domain: 'overview', domainDe: 'Yacht Design Intelligence' },

  // -- Rigg / Segel --
  { type: 'image', src: MEDIA.rigging.under_sail, domain: 'rigging', domainDe: 'Rigg & Segel' },
  { type: 'video', src: MEDIA.video.sailing_aerial, domain: 'rigging', domainDe: 'Rigg & Segel' },
  { type: 'image', src: MEDIA.rigging.winch_detail, domain: 'rigging', domainDe: 'Rigg & Segel' },

  // -- Atmosphäre --
  { type: 'image', src: MEDIA.atmosphere.sunset_sailing, domain: 'atmosphere', domainDe: 'Maritime Exzellenz' },

  // -- Rumpf / Struktur --
  { type: 'image', src: MEDIA.structure.hull_waterline, domain: 'structure', domainDe: 'Rumpf & Struktur' },
  { type: 'video', src: MEDIA.video.ocean_calm, domain: 'structure', domainDe: 'Rumpf & Struktur' },
  { type: 'image', src: MEDIA.structure.hull_drydock, domain: 'structure', domainDe: 'Rumpf & Struktur' },

  // -- Atmosphäre --
  { type: 'image', src: MEDIA.atmosphere.marina_panorama, domain: 'atmosphere', domainDe: 'Hafen & Werft' },

  // -- Interieur --
  { type: 'image', src: MEDIA.interior.salon, domain: 'interior', domainDe: 'Interieur' },
  { type: 'video', src: MEDIA.video.yacht_sailing, domain: 'interior', domainDe: 'Interieur' },
  { type: 'image', src: MEDIA.interior.cabin, domain: 'interior', domainDe: 'Interieur' },

  // -- Materialien --
  { type: 'image', src: MEDIA.materials.teak_deck, domain: 'materials', domainDe: 'Materialien' },
  { type: 'video', src: MEDIA.video.boat_sea, domain: 'materials', domainDe: 'Materialien' },
  { type: 'image', src: MEDIA.materials.marine_hardware, domain: 'materials', domainDe: 'Materialien' },

  // -- Atmosphäre --
  { type: 'image', src: MEDIA.atmosphere.deck_lifestyle, domain: 'atmosphere', domainDe: 'An Bord' },

  // -- Elektrik --
  { type: 'image', src: MEDIA.electrical.nav_instruments, domain: 'electrical', domainDe: 'Elektrik & Elektronik' },
  { type: 'video', src: MEDIA.video.yacht_sunset, domain: 'electrical', domainDe: 'Elektrik & Elektronik' },
  { type: 'image', src: MEDIA.electrical.helm_night, domain: 'electrical', domainDe: 'Elektrik & Elektronik' },

  // -- Antrieb --
  { type: 'image', src: MEDIA.propulsion.engine_room, domain: 'propulsion', domainDe: 'Antrieb' },
  { type: 'video', src: MEDIA.video.ocean_waves, domain: 'propulsion', domainDe: 'Antrieb' },
  { type: 'image', src: MEDIA.propulsion.propeller, domain: 'propulsion', domainDe: 'Antrieb' },

  // -- Atmosphäre (Ende → Loop zurück zum Anfang) --
  { type: 'image', src: MEDIA.atmosphere.ocean_dramatic, domain: 'atmosphere', domainDe: 'Maritime Exzellenz' },
  { type: 'video', src: MEDIA.video.sailing_ocean, domain: 'atmosphere', domainDe: 'Auf See' },
]
