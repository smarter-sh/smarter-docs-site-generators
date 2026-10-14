---
name: smarter-docs-sites-development
description: Start here for any change to the smarter-docs-site-generators repository - the Docusaurus plugin (@smarter.sh/docusaurus-plugin-smarter-chat), the MkDocs plugin (mkdocs-smarter-chat), the Sphinx extension (sphinx-smarter-chat) and the VitePress recipe that add @smarter.sh/ui-chat's chat launcher to documentation sites. Gives the rules, each package's architecture and generator hook, the shared options and expected tag, embed.json, how to add an option to every package, and an index of the narrower skills.
---

# Smarter Chat for documentation sites: Development

Every package writes one tag, the embed script's, with the launcher's options as
`data-` attributes (`doc/adr/003-same-options.md`):

```html
<script
  src="https://cdn.jsdelivr.net/npm/@smarter.sh/ui-chat@0.9.0/dist/embed.js"
  data-chatbot="https://docs-bot.example.com/"
  data-position="bottom-right"
  async
></script>
```

## Non-negotiable rules

1. **Never execute git write commands, and never publish.**
2. **`make test` after every change**: every package, not only the one you
   changed, because they share `test/expected-tag.json` and `embed.json`.
3. **Escape every attribute**: `html.escape(value, quote=True)` in Python;
   Docusaurus escapes `attributes` itself; VitePress too.
4. **Fail the build on a missing or invalid chatbot**, with a message that
   names the option, in the generator's own way.

## The packages

| Package    | Entry point                                  | Generator hook                                                        |
| ---------- | -------------------------------------------- | --------------------------------------------------------------------- |
| Docusaurus | `docusaurus/src/index.js` (`index.d.ts`)     | `injectHtmlTags()` → `postBodyTags`; `validateOptions`                |
| MkDocs     | `mkdocs/src/mkdocs_smarter_chat/plugin.py`   | `on_config` (validate), `on_post_page` (insert before `</body>`)      |
| Sphinx     | `sphinx/src/sphinx_smarter_chat/__init__.py` | `config-inited` (validate), `builder-inited` → `app.add_js_file(...)` |
| VitePress  | `vitepress/README.md`, `vitepress/example/`  | `head: [['script', {...}]]` in `.vitepress/config.mts`                |

The options, in each ecosystem's naming: `chatbot` (required), `apiKey`/`api_key`,
`position`, `label`, `color`, `open`, `height`, `width`, `version`, `src`.
Sphinx prefixes them `smarter_chat_`. Only options that are set are written.

## Adding an option

1. Check `../smarter-chat/src/embed/options.ts` for it, and the version.
2. Add it to every package (Docusaurus types and validation, MkDocs
   `config_options`, Sphinx `add_config_value`), and to the VitePress recipe.
3. Add it to `test/expected-tag.json`'s options and attributes; every package's
   tests then check it.
4. Every package's README, and
   `../smarter/docs/source/smarter-framework/smarter-docs-sites.rst`.

## Related skills

| Skill                        | Use it when                                        |
| ---------------------------- | -------------------------------------------------- |
| `smarter-docs-sites-testing` | Writing or running any package's tests             |
| `smarter-code-quality`       | Before finishing                                   |
| `smarter-git-commits`        | Asked to write a commit message                    |
| `monthly-maintenance`        | Bumping the embed script, generators, dependencies |
