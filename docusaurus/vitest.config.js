import { defineConfig } from "vitest/config";

export default defineConfig({
  test: {
    include: ["test/**/*.test.js"],
    coverage: {
      include: ["src/**/*.js"],
      // lcov: coverage/lcov.info, which CI uploads to Codecov.
      reporter: ["text", "lcov"],
      thresholds: { lines: 95, branches: 95, functions: 95 },
    },
  },
});
