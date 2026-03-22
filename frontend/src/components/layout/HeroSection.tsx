import { useState, useEffect } from 'react'

interface HeroSectionProps {
  backgroundImage?: string
  backgroundVideo?: string
  title: string
  subtitle?: string
  label?: string
  children?: React.ReactNode
  size?: 'sm' | 'md' | 'lg'
}

export default function HeroSection({
  backgroundImage,
  backgroundVideo,
  title,
  subtitle,
  label,
  children,
  size = 'md',
}: HeroSectionProps) {
  const [scrollY, setScrollY] = useState(0)
  const [isMobile, setIsMobile] = useState(window.innerWidth < 768)

  useEffect(() => {
    const handleResize = () => {
      setIsMobile(window.innerWidth < 768)
    }
    window.addEventListener('resize', handleResize)
    return () => window.removeEventListener('resize', handleResize)
  }, [])

  useEffect(() => {
    const handleScroll = () => {
      setScrollY(window.scrollY)
    }
    window.addEventListener('scroll', handleScroll)
    return () => window.removeEventListener('scroll', handleScroll)
  }, [])

  const heights = {
    sm: isMobile ? 'min-h-[180px] md:min-h-[240px]' : 'min-h-[240px]',
    md: isMobile ? 'min-h-[240px] md:min-h-[320px]' : 'min-h-[320px]',
    lg: isMobile ? 'min-h-[280px] md:min-h-[380px]' : 'min-h-[380px]',
  }

  // Subtle parallax effect (max 30px movement)
  const parallaxOffset = Math.min(scrollY * 0.5, 30)

  return (
    <div className={`hero-section ${heights[size]} flex items-end relative overflow-hidden`}>
      {/* Background media with parallax */}
      {backgroundVideo ? (
        <video
          autoPlay
          loop
          muted
          playsInline
          className="absolute inset-0 w-full h-full object-cover"
          style={{
            transform: `translateY(${parallaxOffset}px)`,
          }}
        >
          <source src={backgroundVideo} type="video/mp4" />
        </video>
      ) : backgroundImage ? (
        <div
          className="absolute inset-0 w-full h-full bg-cover bg-center"
          style={{
            backgroundImage: `url(${backgroundImage})`,
            transform: `translateY(${parallaxOffset}px)`,
          }}
        />
      ) : (
        <div className="absolute inset-0 w-full h-full bg-gradient-premium" />
      )}

      {/* Gradient overlay - improved with radial gradient for depth */}
      <div className="absolute inset-0 bg-gradient-premium" />
      <div className="absolute inset-0 bg-radial-gradient opacity-40"
        style={{
          background: 'radial-gradient(circle at 50% 100%, rgba(6, 182, 212, 0.15) 0%, transparent 70%)',
        }}
      />

      {/* Content */}
      <div className="w-full px-6 md:px-10 pb-8 pt-16 relative z-10">
        {label && (
          <p className="label-premium mb-3 animate-fade-in" style={{ animationDelay: '0ms' }}>
            {label}
          </p>
        )}
        <h1
          className="font-serif text-display font-medium text-white mb-1 opacity-0 animate-fade-in"
          style={{
            animation: 'fadeInUp 600ms ease-out forwards',
            animationDelay: '100ms',
          }}
        >
          {title}
        </h1>
        {subtitle && (
          <p
            className="font-sans text-[15px] text-navy-300 max-w-2xl leading-relaxed mt-2 opacity-0 animate-fade-in"
            style={{
              animation: 'fadeInUp 600ms ease-out forwards',
              animationDelay: '200ms',
            }}
          >
            {subtitle}
          </p>
        )}
        {children && (
          <div
            className="mt-6 opacity-0 animate-fade-in"
            style={{
              animation: 'fadeInUp 600ms ease-out forwards',
              animationDelay: '300ms',
            }}
          >
            {children}
          </div>
        )}
      </div>

      <style>{`
        @keyframes fadeInUp {
          from {
            opacity: 0;
            transform: translateY(12px);
          }
          to {
            opacity: 1;
            transform: translateY(0);
          }
        }
      `}</style>
    </div>
  )
}
