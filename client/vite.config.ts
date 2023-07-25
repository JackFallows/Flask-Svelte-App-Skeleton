import { resolve } from 'path';
import { defineConfig } from 'vite';
import { svelte } from '@sveltejs/vite-plugin-svelte';

// https://vitejs.dev/config/
export default defineConfig({
  plugins: [svelte()],
  build: {
    rollupOptions: {
      input: {
        index: resolve(__dirname, './src/main.ts'),
      },
    },
    sourcemap: true,
    minify: false,
    cssCodeSplit: false,
    copyPublicDir: false,
    outDir: './public/build',
    assetsDir: '.'
  },
});
