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
  const heights = {
    sm: 'min-h-[180px]',
    md: 'min-h-[260px]',
    lg: 'min-h-[360px]',
  }

  return (
    <div className={`hero-section ${heights[size]} flex items-end`}>
      {/* Background media */}
      {backgroundVideo ? (
        <video
          autoPlay
          loop
          muted
          playsInline
          className="absolute inset-0 w-full h-full object-cover"
        >
          <source src={backgroundVideo} type="video/mp4" />
        </video>
      ) : backgroundImage ? (
        <div
          className="absolute inset-0 w-full h-full bg-cover bg-center"
          style={{ backgroundImage: `url(${backgroundImage})` }}
        />
      ) : (
        <div className="absolute inset-0 w-full h-full bg-gradient-premium" />
      )}

      {/* Content */}
      <div className="w-full px-10 pb-8 pt-16">
        {label && (
          <p className="label-premium mb-3">{label}</p>
        )}
        <h1 className="font-serif text-display font-medium text-white mb-1">
          {title}
        </h1>
        {subtitle && (
          <p className="font-sans text-[15px] text-navy-300 max-w-2xl leading-relaxed mt-2">
            {subtitle}
          </p>
        )}
        {children && <div className="mt-6">{children}</div>}
      </div>
    </div>
  )
}
