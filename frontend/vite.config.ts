import { defineConfig } from 'vite'
import react from '@vitejs/plugin-react'

export default defineConfig({
  plugins: [react()],
  server: {
    port: 5173,
    proxy: {
      '/api': {
        target: 'http://localhost:8000',
        changeOrigin: true,
        ws: true, // real-time collaboration (WS /api/v1/ws/collaborate/...)
      },
      '/health': {
        target: 'http://localhost:8000',
        changeOrigin: true,
      },
    },
  },
})
