# Smarter Chat for VitePress

Add a [Smarter](https://smarter.sh) chatbot to every page of a VitePress site: one `head` entry in
`.vitepress/config.mts`. There is no package to install (see
[ADR-007](../doc/adr/007-vitepress.md)).

```ts
import { defineConfig } from "vitepress";

export default defineConfig({
  head: [
    [
      "script",
      {
        src: "https://cdn.jsdelivr.net/npm/@smarter.sh/ui-chat@0.9.0/dist/embed.js",
        "data-chatbot": "https://docs-bot.example.com/",
        async: "",
      },
    ],
  ],
});
```

That adds a chat button to the bottom right corner of every page; it survives VitePress's client-side navigation, and
the conversation follows the reader from page to page. The chatbot is a deployed LLMClient, whose manifest must allow
the site's origin in `spec.config.prompt.allowedOrigins`.

| Attribute                   | Example                         | Description                                      |
| --------------------------- | ------------------------------- | ------------------------------------------------ |
| `data-chatbot`              | `https://docs-bot.example.com/` | The deployed LLMClient's url. Required.          |
| `data-api-key`              | `key-1`                         | Only for an LLMClient that requires one. Public. |
| `data-position`             | `bottom-left`                   | `bottom-right` (default) or `bottom-left`.       |
| `data-label`                | `Ask the docs`                  | The button's accessible name.                    |
| `data-color`                | `#123456`                       | The button's color.                              |
| `data-open`                 | `true`                          | Start open.                                      |
| `data-height`, `data-width` | `70vh`, `420px`                 | The panel's size.                                |

[`example/`](example/) is a working site with every option, which this repository's tests build.
