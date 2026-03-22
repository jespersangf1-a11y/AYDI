/**
 * AYDI Media Configuration
 * All background images and videos for the platform.
 * Using Unsplash for high-quality, freely licensed photography.
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

  // Video backgrounds (Pexels free stock — autoplay, muted, looped)
  video: {
    ocean_calm: 'https://videos.pexels.com/video-files/1918465/1918465-hd_1920_1080_24fps.mp4',
    sailing_aerial: 'https://videos.pexels.com/video-files/2491284/2491284-hd_1920_1080_24fps.mp4',
    ocean_waves: 'https://videos.pexels.com/video-files/1093662/1093662-hd_1920_1080_30fps.mp4',
    yacht_sunset: 'https://videos.pexels.com/video-files/857251/857251-hd_1920_1080_25fps.mp4',
  },

  // Structural Analysis / Hull
  structure: {
    hull_waterline: section('photo-1569263979104-865ab7cd8d13'),  // Yacht hull line
    hull_drydock: section('photo-1559134197-64a0a4c40502'),       // Boat in dry dock
  },

  // Materials
  materials: {
    teak_deck: section('photo-1558618666-fcd25c85f82e'),          // Teak wood grain
    marine_hardware: section('photo-1544551763-46a013bb70d5'),    // Marine hardware detail
  },

  // Electrical / Electronics
  electrical: {
    nav_instruments: section('photo-1559136555-9303baea8ebd'),    // Navigation instruments
    helm_night: section('photo-1544620347-c4fd4a3d5957'),         // Helm illuminated
  },

  // Interior / Layout
  interior: {
    salon: section('photo-1569263979104-865ab7cd8d13'),           // Yacht interior salon
    cabin: section('photo-1540946485063-a40da27545f8'),           // Yacht cabin
  },

  // Rigging / Sails
  rigging: {
    under_sail: section('photo-1534438327276-14e5300c3a48'),      // Sailing yacht dramatic
    winch_detail: section('photo-1535532901685-188aafe0c77d'),    // Rigging winch detail
  },

  // Propulsion
  propulsion: {
    engine_room: section('photo-1530103862676-de8c9debad1d'),     // Engine
    propeller: section('photo-1507003211169-0a1dd7228f2d'),       // Underwater propeller
  },

  // Quick Analysis / Overview
  overview: {
    blueprint: section('photo-1504711331183-9c7b2d1a5748'),       // Technical drawings
    marina_aerial: section('photo-1545579133-99bb5ab189bd'),      // Marina from above
  },
} as const

export type MediaCategory = keyof typeof MEDIA
