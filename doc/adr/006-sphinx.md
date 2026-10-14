# ADR-006: Sphinx: an Extension

## Status

Accepted

## Context

Sphinx extensions are Python modules with a `setup(app)` function, enabled in `conf.py`'s `extensions`. `app.add_js_file(url, loading_method="async", **attributes)` adds a script tag to every html page, with any attributes, and works with every html theme (Read the Docs', Furo, PyData, Book, Alabaster).

## Decision

`sphinx-smarter-chat` is a Sphinx extension, `extensions = ["sphinx_smarter_chat"]`, with config values `smarter_chat_chatbot`, `smarter_chat_api_key`, `smarter_chat_position`, ... It validates them in `config-inited`, and, on `builder-inited`, adds the embed script with its `data-` attributes (ADR-003) for html builders only. It declares itself parallel read and write safe. Its only dependency is Sphinx.

## Consequences

- **Positive:**
  - Works with every html theme, and with Read the Docs' builds, without template overrides.
- **Negative:**
  - Sphinx puts the tag in `<head>`, not before `</body>`; the embed script waits for the body, so the result is the same.

## Related ADRs

- [ADR-003: The Same Options, and the Same Tag, Everywhere](003-same-options.md)
