# ADR-005: MkDocs: a Plugin

## Status

Accepted

## Context

MkDocs plugins are Python classes, registered with the `mkdocs.plugins` entry point, configured in `mkdocs.yml`, whose events include `on_post_page(output, page, config)`, which receives each page's final html. MkDocs Material is a theme, so a plugin works with it and with MkDocs' other themes. Material's "instant navigation" replaces the page's content without a reload, and keeps elements that aren't its own.

## Decision

`mkdocs-smarter-chat` is an MkDocs plugin, `plugins: [smarter-chat: {chatbot: ...}]`, with typed `config_options`, that inserts the script tag (ADR-003) before each page's `</body>` in `on_post_page`. It validates the chatbot in `on_config`, so a misconfigured site fails `mkdocs build`. Its only dependency is MkDocs.

## Alternatives Considered

- **`extra_javascript` in `mkdocs.yml`.** It can't set `data-` attributes, and it would need an inline script for the options.
- **A Material theme override (`main.html`).** Theme-specific, and replaces the user's own overrides.

## Consequences

- **Positive:**
  - Works with every MkDocs theme, including Material with instant navigation.
- **Negative:**
  - Pages that a theme renders without `</body>` get no launcher (none of the common themes do).

## Related ADRs

- [ADR-003: The Same Options, and the Same Tag, Everywhere](003-same-options.md)
