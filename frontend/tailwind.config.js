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
      },
      backgroundImage: {
        'gradient-premium': 'linear-gradient(135deg, #0b1220 0%, #0d2730 50%, #0b1220 100%)',
        'gradient-card': 'linear-gradient(180deg, rgba(21,61,74,0.08) 0%, rgba(11,18,32,0.4) 100%)',
      },
      animation: {
        'fade-in': 'fadeIn 0.6s ease-out',
        'slide-up': 'slideUp 0.5s ease-out',
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
      },
    },
  },
  plugins: [],
}
