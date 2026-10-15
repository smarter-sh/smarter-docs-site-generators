# mkdocs-smarter-chat

[![Build](https://github.com/smarter-sh/smarter-docs-site-generators/actions/workflows/build.yml/badge.svg?branch=main)](https://github.com/smarter-sh/smarter-docs-site-generators/actions/workflows/build.yml)
[![Test](https://github.com/smarter-sh/smarter-docs-site-generators/actions/workflows/test.yml/badge.svg?branch=main)](https://github.com/smarter-sh/smarter-docs-site-generators/actions/workflows/test.yml)
[![MkDocs coverage](https://img.shields.io/codecov/c/github/smarter-sh/smarter-docs-site-generators/main?flag=mkdocs&label=coverage&logo=codecov)](https://app.codecov.io/gh/smarter-sh/smarter-docs-site-generators?flags%5B0%5D=mkdocs)

An [MkDocs](https://www.mkdocs.org) plugin that adds a [Smarter](https://smarter.sh) chatbot to every page of a
documentation site, with any theme, including [Material for MkDocs](https://squidfunk.github.io/mkdocs-material/): a
chat button in a corner of the page, which opens the chat. The chat is the embed script of
[`@smarter.sh/ui-chat`](https://github.com/smarter-sh/smarter-chat); its look comes from the chatbot's manifest.

```console
pip install mkdocs-smarter-chat
```

```yaml
# mkdocs.yml
plugins:
  - search
  - smarter-chat:
      chatbot: https://docs-bot.example.com/
```

The chatbot is a deployed LLMClient, whose manifest must allow the site's origin in
`spec.config.prompt.allowedOrigins`.

| Option            | Default          | Description                                                                |
| ----------------- | ---------------- | -------------------------------------------------------------------------- |
| `chatbot`         | (required)       | The deployed LLMClient's url.                                              |
| `api_key`         |                  | Only for an LLMClient that requires one. It is public in the pages.        |
| `position`        | `bottom-right`   | `bottom-right` or `bottom-left`.                                           |
| `label`           | `Chat`           | The button's accessible name.                                              |
| `color`           | `#ff5733`        | The button's hex color.                                                    |
| `open`            | `false`          | Start open.                                                                |
| `height`, `width` | `600px`, `400px` | The panel's size, css lengths.                                             |
| `version`         | this release's   | The version of `@smarter.sh/ui-chat` to load from jsDelivr, or a range.    |
| `src`             |                  | The url or path of a self-hosted `embed.js` (with its `embed/` beside it). |

An invalid option fails `mkdocs build`. With Material's instant navigation, the launcher stays on the page, and the
conversation follows the reader. See the
[guide](https://docs.smarter.sh/en/latest/smarter-framework/smarter-docs-sites.html). License: AGPL-3.0-or-later.
