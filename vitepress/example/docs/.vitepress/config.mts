import { defineConfig } from "vitepress";

// The Smarter Chat launcher on every page: the embed script's tag, with the launcher's options as data- attributes.
// See ../../../README.md. The options here are test/expected-tag.json's "every option" case, which
// scripts/check-vitepress.mjs checks in the built pages.
export default defineConfig({
  title: "Smoke",
  head: [
    [
      "script",
      {
        src: "https://cdn.jsdelivr.net/npm/@smarter.sh/ui-chat@0.9.0/dist/embed.js",
        "data-chatbot": "https://docs-bot.example.com/",
        "data-api-key": "key-1",
        "data-position": "bottom-left",
        "data-label": "Ask the docs",
        "data-color": "#123456",
        "data-open": "true",
        "data-height": "70vh",
        "data-width": "420px",
        async: "",
      },
    ],
  ],
});
