# ADR-007: VitePress: a Recipe, Not a Package

## Status

Accepted

## Context

VitePress has no plugin system for pages. Its configuration's `head` is a list of tags, `['script', {attributes}]`, added to every page, which is exactly the one tag the chat needs. Its app root is a `<div>` in `<body>`, so the launcher survives its client-side navigation.

## Decision

VitePress gets a **recipe**, not a package: the `head` entry, documented in `vitepress/README.md` and on docs.smarter.sh, and a working example site, `vitepress/example/`, whose build CI checks for the same tag as the other packages (ADR-003).

## Alternatives Considered

- **A package with a `smarterChat(options)` helper** that returns the `head` entry. It would add validation, at the cost of a dependency for five lines of configuration. If VitePress users ask for one, it is a small addition to this repository.

## Consequences

- **Positive:**
  - Nothing to install or update but the version in the url.
- **Negative:**
  - No validation of the options at build time.

## Related ADRs

- [ADR-003: The Same Options, and the Same Tag, Everywhere](003-same-options.md)
- [ADR-009: Testing](009-testing.md)
