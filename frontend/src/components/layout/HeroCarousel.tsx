import { useState, useEffect, useRef, useCallback } from 'react'
// Video refs removed — videos auto-manage playback via autoPlay+loop
import { HERO_CAROUSEL_SLIDES, type CarouselSlide } from '../../config/media'

interface HeroCarouselProps {
  /** Wie lange jedes Bild angezeigt wird (ms). Default: 6000 */
  imageDuration?: number
  /** Wie lange jedes Video angezeigt wird (ms). Default: 10000 */
  videoDuration?: number
  /** Crossfade-Dauer (ms). Default: 1500 */
  fadeDuration?: number
  /** Titel auf dem Hero */
  title: string
  subtitle?: string
  label?: string
  children?: React.ReactNode
  /** Bereichslabel einblenden? Default: true */
  showDomainLabel?: boolean
}

export default function HeroCarousel({
  imageDuration = 6000,
  videoDuration = 10000,
  fadeDuration = 1500,
  title,
  subtitle,
  label,
  children,
  showDomainLabel = true,
}: HeroCarouselProps) {
  const slides = HERO_CAROUSEL_SLIDES
  const [currentIndex, setCurrentIndex] = useState(0)
  const [nextIndex, setNextIndex] = useState(1)
  const [isFading, setIsFading] = useState(false)
  const [scrollY, setScrollY] = useState(0)
  const [domainLabel, setDomainLabel] = useState(slides[0]?.domainDe || '')
  const [domainFading, setDomainFading] = useState(false)

  const timerRef = useRef<ReturnType<typeof setTimeout> | null>(null)

  // Parallax
  useEffect(() => {
    const handleScroll = () => setScrollY(window.scrollY)
    window.addEventListener('scroll', handleScroll, { passive: true })
    return () => window.removeEventListener('scroll', handleScroll)
  }, [])

  const parallaxOffset = Math.min(scrollY * 0.3, 40)

  // Advance to next slide
  const advanceSlide = useCallback(() => {
    const nextIdx = (currentIndex + 1) % slides.length
    const afterNext = (nextIdx + 1) % slides.length

    // Start domain label crossfade
    if (slides[nextIdx].domainDe !== domainLabel) {
      setDomainFading(true)
      setTimeout(() => {
        setDomainLabel(slides[nextIdx].domainDe)
        setDomainFading(false)
      }, 400)
    }

    // Start crossfade
    setNextIndex(nextIdx)
    setIsFading(true)

    // After fade completes, swap current to the new slide
    setTimeout(() => {
      setCurrentIndex(nextIdx)
      setNextIndex(afterNext)
      setIsFading(false)
    }, fadeDuration)
  }, [currentIndex, slides, fadeDuration, domainLabel])

  // Timer for auto-advance
  useEffect(() => {
    const currentSlide = slides[currentIndex]
    const duration = currentSlide?.type === 'video' ? videoDuration : imageDuration

    timerRef.current = setTimeout(() => {
      advanceSlide()
    }, duration)

    return () => {
      if (timerRef.current) clearTimeout(timerRef.current)
    }
  }, [currentIndex, isFading, advanceSlide, imageDuration, videoDuration, slides])

  // Preload next image
  useEffect(() => {
    const nextSlide = slides[nextIndex]
    if (nextSlide?.type === 'image') {
      const img = new Image()
      img.src = nextSlide.src
    }
  }, [nextIndex, slides])

  const renderSlide = (
    slide: CarouselSlide,
    isVisible: boolean,
  ) => {
    if (slide.type === 'video') {
      return (
        <video
          autoPlay
          loop
          muted
          playsInline
          className="absolute inset-0 w-full h-full object-cover"
          style={{
            transform: `translateY(${parallaxOffset}px) scale(1.05)`,
            opacity: isVisible ? 1 : 0,
            transition: `opacity ${fadeDuration}ms ease-in-out`,
          }}
          onError={(e) => {
            // Video not available — hide it and advance to next slide
            (e.currentTarget as HTMLVideoElement).style.display = 'none'
            advanceSlide()
          }}
        >
          <source src={slide.src} type="video/mp4" />
        </video>
      )
    }

    return (
      <div
        className="absolute inset-0 w-full h-full bg-cover bg-center"
        style={{
          backgroundImage: `url(${slide.src})`,
          transform: `translateY(${parallaxOffset}px) scale(1.05)`,
          opacity: isVisible ? 1 : 0,
          transition: `opacity ${fadeDuration}ms ease-in-out`,
        }}
      />
    )
  }

  const currentSlide = slides[currentIndex]
  const nextSlide = slides[nextIndex]

  return (
    <div className="hero-section min-h-[280px] md:min-h-[360px] lg:min-h-[420px] flex items-end relative overflow-hidden">

      {/* === Background Layer: Current Slide === */}
      {currentSlide && renderSlide(currentSlide, true)}

      {/* === Background Layer: Next Slide (fades in on top) === */}
      {nextSlide && renderSlide(nextSlide, isFading)}

      {/* === Gradient Overlays === */}
      <div className="absolute inset-0" style={{
        background: 'linear-gradient(180deg, rgba(6,10,20,0.3) 0%, rgba(6,10,20,0.6) 60%, rgba(6,10,20,0.85) 100%)',
      }} />
      <div className="absolute inset-0" style={{
        background: 'radial-gradient(ellipse at 50% 100%, rgba(45,139,168,0.12) 0%, transparent 60%)',
      }} />

      {/* === Content === */}
      <div className="w-full px-6 md:px-10 pb-8 pt-20 relative z-10">
        {/* Domain label */}
        {showDomainLabel && domainLabel && (
          <div
            className="mb-4 transition-all duration-400"
            style={{ opacity: domainFading ? 0 : 0.9, transform: domainFading ? 'translateY(-4px)' : 'translateY(0)' }}
          >
            <span className="inline-block px-3 py-1 text-[10px] font-sans uppercase tracking-[0.2em] text-white border border-white/40 rounded-full backdrop-blur-sm bg-white/15">
              {domainLabel}
            </span>
          </div>
        )}

        {/* Label */}
        {label && (
          <p className="label-premium mb-3" style={{ animation: 'fadeInUp 600ms ease-out forwards' }}>
            {label}
          </p>
        )}

        {/* Title */}
        <h1
          className="font-serif text-3xl md:text-display lg:text-hero font-medium text-white mb-1 opacity-0"
          style={{ animation: 'fadeInUp 600ms ease-out 100ms forwards' }}
        >
          {title}
        </h1>

        {/* Subtitle */}
        {subtitle && (
          <p
            className="font-sans text-[15px] text-white max-w-2xl leading-relaxed mt-2 opacity-0"
            style={{ animation: 'fadeInUp 600ms ease-out 200ms forwards' }}
          >
            {subtitle}
          </p>
        )}

        {/* Children */}
        {children && (
          <div
            className="mt-6 opacity-0"
            style={{ animation: 'fadeInUp 600ms ease-out 300ms forwards' }}
          >
            {children}
          </div>
        )}

        {/* === Slide Progress Indicator === */}
        <div className="flex items-center gap-1.5 mt-6">
          {slides.map((_, idx) => (
            <div
              key={idx}
              className="h-[2px] rounded-full transition-all duration-500"
              style={{
                width: idx === currentIndex ? '24px' : '6px',
                backgroundColor: idx === currentIndex
                  ? 'rgba(75, 167, 195, 0.8)'
                  : 'rgba(75, 167, 195, 0.2)',
              }}
            />
          ))}
        </div>
      </div>

      {/* Keyframes */}
      <style>{`
        @keyframes fadeInUp {
          from { opacity: 0; transform: translateY(12px); }
          to { opacity: 1; transform: translateY(0); }
        }
      `}</style>
    </div>
  )
}
