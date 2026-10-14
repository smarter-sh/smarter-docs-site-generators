// ESLint for the JavaScript: the Docusaurus plugin, its tests, and the scripts. See skills/smarter-code-quality.
import js from "@eslint/js";
import globals from "globals";

export default [
  {
    ignores: ["**/node_modules/", "**/coverage/", "build/", "venv/", "vitepress/example/docs/.vitepress/{dist,cache}/"],
  },
  js.configs.recommended,
  { files: ["**/*.{js,mjs}"], languageOptions: { globals: globals.node } },
];
