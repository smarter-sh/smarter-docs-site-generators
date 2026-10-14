---
name: smarter-docs-sites-testing
description: Use when writing or running smarter-docs-site-generators' tests - Vitest unit tests of the Docusaurus plugin's hooks, pytest unit tests and real mkdocs builds (default theme and Material), real Sphinx builds in a temporary directory, the VitePress example's real build, the shared test/expected-tag.json and embed.json checks, and coverage.
---

# Smarter Chat for documentation sites: Testing

`make test` runs all four; `make test-<generator>` one. `make init` creates
`venv/` with both Python packages installed in editable mode, MkDocs, Material,
Sphinx and pytest.

## The shared contract

`test/expected-tag.json` has one set of options (in camelCase) and the
attributes that every package must write for them, and `embed.json` the
embed script's version. Each package's tests load both: change them, and every
package must follow.

## Per package

- **Docusaurus** (`docusaurus/test/*.test.js`, Vitest): call the plugin with
  options, check `injectHtmlTags().postBodyTags`; call `validateOptions` with a
  fake `validate` that runs the plugin's schema, as Docusaurus does.
- **MkDocs** (`mkdocs/tests/`, pytest): unit tests of `on_config` and
  `on_post_page`; a real `mkdocs build` of `tests/site/` into `tmp_path`, with
  the default theme and with Material, parsed with `html.parser`.
- **Sphinx** (`sphinx/tests/`, pytest): a real build of `tests/roots/basic` with
  `sphinx.application.Sphinx` into `tmp_path`, html and text builders, and the
  configuration errors.
- **VitePress** (`make test-vitepress`): installs `vitepress/example/`, runs
  `vitepress build`, and `scripts/check-vitepress.mjs` checks the built pages'
  tags against `test/expected-tag.json`.

The Python tests parse html with `html.parser` (`tests/htmltags.py`); the
VitePress check, which has no dependencies, reads only the attributes of
`<script>` tags. Never contact a Smarter platform: the chatbot is
`https://docs-bot.example.com/`.
