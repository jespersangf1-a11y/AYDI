/** @type {import('tailwindcss').Config} */
export default {
  content: ['./index.html', './src/**/*.{ts,tsx}'],
  theme: {
    extend: {
      colors: {
        navy: {
          50: '#eef1f6',
          100: '#d4dae6',
          200: '#a9b5cd',
          300: '#7e90b4',
          400: '#536b9b',
          500: '#3a5282',
          600: '#2d4068',
          700: '#1e2d4a',
          800: '#131d32',
          900: '#0b1220',
          950: '#060a14',
        },
        ocean: {
          50: '#eff8fa',
          100: '#d5ecf2',
          200: '#a8d8e5',
          300: '#72bfd4',
          400: '#4ba7c3',
          500: '#2d8ba8',
          600: '#246f87',
          700: '#1c5567',
          800: '#153d4a',
          900: '#0d2730',
          950: '#081a20',
        },
        sand: {
          50: '#faf8f5',
          100: '#f0ece4',
          200: '#e0d7c8',
          300: '#c9bba3',
          400: '#b5a282',
          500: '#9e8a66',
          600: '#7d6d50',
          700: '#5e523d',
          800: '#3f372a',
          900: '#211d17',
          950: '#110f0c',
        },
      },
      fontFamily: {
        serif: ['Playfair Display', 'Georgia', 'serif'],
        sans: ['Inter', 'system-ui', 'sans-serif'],
        mono: ['JetBrains Mono', 'monospace'],
      },
      letterSpacing: {
        'wide-premium': '0.08em',
        'wider-premium': '0.15em',
      },
      fontSize: {
        'hero': ['3.5rem', { lineHeight: '1.1', letterSpacing: '-0.02em' }],
        'display': ['2.5rem', { lineHeight: '1.15', letterSpacing: '-0.015em' }],
        'title': ['1.75rem', { lineHeight: '1.25', letterSpacing: '-0.01em' }],
        'subtitle': ['1.25rem', { lineHeight: '1.35', letterSpacing: '-0.005em' }],
        'body-lg': ['1.0625rem', { lineHeight: '1.6' }],
      },
      backgroundImage: {
        'gradient-premium': 'linear-gradient(135deg, #faf8f5 0%, #f0ece4 50%, #faf8f5 100%)',
        'gradient-card': 'linear-gradient(180deg, rgba(212,218,230,0.4) 0%, rgba(250,248,245,0.8) 100%)',
      },
      animation: {
        'fade-in': 'fadeIn 0.6s ease-out',
        'slide-up': 'slideUp 0.5s ease-out',
        'fade-in-up': 'fade-in-up 0.5s ease-out both',
        'fade-in-scale': 'fade-in-scale 0.4s ease-out both',
        'slide-in-right': 'slide-in-right 0.5s ease-out both',
        'slide-in-left': 'slide-in-left 0.4s ease-out both',
        'shimmer': 'shimmer 1.5s ease-in-out infinite',
        'pulse-glow': 'pulse-glow 2s ease-in-out infinite',
        'draw-circle': 'draw-circle 1s ease-out both',
        'fill-bar': 'fill-bar 0.8s ease-out both',
        'slide-down': 'slide-down 0.3s ease-out both',
        'shake': 'shake 0.4s ease-out',
        'section-expand': 'section-expand 0.3s ease-out both',
        'section-collapse': 'section-collapse 0.2s ease-out both',
        'slide-out-right': 'slide-out-right 0.3s cubic-bezier(0.4, 0, 0.2, 1) both',
        'backdrop-fade': 'backdrop-fade 0.3s ease-out both',
        'count-up': 'count-up 0.6s ease-out both',
      },
      keyframes: {
        fadeIn: {
          '0%': { opacity: '0' },
          '100%': { opacity: '1' },
        },
        slideUp: {
          '0%': { opacity: '0', transform: 'translateY(12px)' },
          '100%': { opacity: '1', transform: 'translateY(0)' },
        },
        'fade-in-up': {
          'from': { opacity: '0', transform: 'translateY(16px)' },
          'to': { opacity: '1', transform: 'translateY(0)' },
        },
        'fade-in-scale': {
          'from': { opacity: '0', transform: 'scale(0.95)' },
          'to': { opacity: '1', transform: 'scale(1)' },
        },
        'slide-in-right': {
          'from': { opacity: '0', transform: 'translateX(24px)' },
          'to': { opacity: '1', transform: 'translateX(0)' },
        },
        'slide-in-left': {
          'from': { opacity: '0', transform: 'translateX(-24px)' },
          'to': { opacity: '1', transform: 'translateX(0)' },
        },
        'slide-down': {
          'from': { opacity: '0', transform: 'translateY(-8px)' },
          'to': { opacity: '1', transform: 'translateY(0)' },
        },
        'shake': {
          '0%, 100%': { transform: 'translateX(0)' },
          '25%': { transform: 'translateX(-4px)' },
          '50%': { transform: 'translateX(4px)' },
          '75%': { transform: 'translateX(-2px)' },
        },
        'section-expand': {
          'from': { 'grid-template-rows': '0fr', opacity: '0' },
          'to': { 'grid-template-rows': '1fr', opacity: '1' },
        },
        'section-collapse': {
          'from': { 'grid-template-rows': '1fr', opacity: '1' },
          'to': { 'grid-template-rows': '0fr', opacity: '0' },
        },
        'slide-out-right': {
          'from': { opacity: '1', transform: 'translateX(0)' },
          'to': { opacity: '0', transform: 'translateX(100%)' },
        },
        'backdrop-fade': {
          'from': { opacity: '0' },
          'to': { opacity: '1' },
        },
        'count-up': {
          'from': { opacity: '0' },
          'to': { opacity: '1' },
        },
        'shimmer': {
          '0%': { 'background-position': '-200% 0' },
          '100%': { 'background-position': '200% 0' },
        },
        'pulse-glow': {
          '0%, 100%': { 'box-shadow': '0 0 0 0 rgba(45, 139, 168, 0)' },
          '50%': { 'box-shadow': '0 0 20px 4px rgba(45, 139, 168, 0.15)' },
        },
        'draw-circle': {
          'from': { 'stroke-dashoffset': 'var(--circumference, 283)' },
        },
        'fill-bar': {
          'from': { 'width': '0%' },
        },
      },
      transitionDuration: {
        '400': '400ms',
        '600': '600ms',
        '800': '800ms',
      },
      backdropBlur: {
        'xs': '2px',
      },
      spacing: {
        'section': '4rem',
        'section-lg': '6rem',
      },
      borderRadius: {
        'card': '14px',
        'button': '10px',
        'badge': '8px',
      },
      transitionTimingFunction: {
        'premium': 'cubic-bezier(0.4, 0, 0.2, 1)',
        'bounce': 'cubic-bezier(0.34, 1.56, 0.64, 1)',
      },
      boxShadow: {
        'glow-ocean': '0 0 20px 0 rgba(45, 139, 168, 0.1)',
        'glow-ocean-lg': '0 0 40px 0 rgba(45, 139, 168, 0.12)',
        'inner-ocean': 'inset 0 1px 2px rgba(45, 139, 168, 0.08)',
        'card-hover': '0 8px 24px rgba(45, 139, 168, 0.12), 0 0 0 1px rgba(212, 218, 230, 0.6)',
        'card-rest': '0 1px 3px rgba(11, 18, 32, 0.04), 0 1px 2px rgba(11, 18, 32, 0.06)',
      },
    },
  },
  plugins: [],
}
