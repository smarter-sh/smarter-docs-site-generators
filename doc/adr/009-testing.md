# ADR-009: Testing

## Status

Accepted

Follows the Python SDK's [ADR-009: Testing](https://github.com/smarter-sh/smarter-python/blob/main/doc/adr/009-testing.md).

## Context

Each package is a few dozen lines, but it runs inside a generator whose apis change. The tag it writes must be the same everywhere (ADR-003).

## Decision

- **Docusaurus:** Vitest unit tests of the plugin's `injectHtmlTags()` and `validateOptions()`, called as Docusaurus calls them. The plugin validates its options itself, without Docusaurus's Joi, so it has no dependencies. Docusaurus itself is not installed: it is large, and the plugin uses only those two hooks.
- **MkDocs:** pytest, with unit tests of the plugin, and a real `mkdocs build` of a two-page site, with the default theme and with Material, whose html is parsed.
- **Sphinx:** pytest, with a real Sphinx build of a small project in a temporary directory, with the html builder and a non-html builder, whose html is parsed.
- **VitePress:** a real `vitepress build` of `vitepress/example/` in CI, whose html is checked.
- **Shared:** every package's tests compare its tag with `test/expected-tag.json`, one expected set of attributes for one set of options, and check that the package's embed version is `embed.json`'s.
- Coverage of the Python and JavaScript packages: at least 95%.

## Consequences

- **Positive:**
  - Real builds for the generators that are cheap to install, and one expected tag for all.
- **Negative:**
  - Docusaurus is tested through its hooks, not a real build.

## Related ADRs

- [ADR-003: The Same Options, and the Same Tag, Everywhere](003-same-options.md)
