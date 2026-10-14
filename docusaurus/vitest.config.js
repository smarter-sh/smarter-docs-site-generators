import { defineConfig } from "vitest/config";

export default defineConfig({
  test: {
    include: ["test/**/*.test.js"],
    coverage: { include: ["src/**/*.js"], thresholds: { lines: 95, branches: 95, functions: 95 } },
  },
});
