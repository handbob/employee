import { defineConfig } from '@playwright/test'

export default defineConfig({
  webServer: {
    command: 'npm run dev'
  },
  testDir: './tests/e2e'
});
