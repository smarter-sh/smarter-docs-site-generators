# ADR-004: Docusaurus: a Plugin

## Status

Accepted

## Context

Docusaurus 3 plugins are functions that return an object of lifecycle methods. `injectHtmlTags()` adds tags to every page's `<head>` or `<body>`, server-rendered and client-side. Docusaurus is a single-page app after the first page, but its React root is a `<div>` inside `<body>`, so an element appended to `<body>` survives navigation.

## Decision

`@smarter.sh/docusaurus-plugin-smarter-chat` is a Docusaurus plugin, ES module, with TypeScript declarations, whose `injectHtmlTags()` returns the script tag (ADR-003) in `postBodyTags`. It validates its options in `validateOptions`, Docusaurus's own hook, so a misconfigured site fails `docusaurus build` with a clear message. It has no dependencies.

## Alternatives Considered

- **A theme component (swizzled `Root`)** that renders `<smarter-chat>`. The launcher lives outside React's tree; a component would be remounted by React and gain nothing.
- **`scripts` in `docusaurus.config.js`.** Works, but it has no validation, and its attribute names are the user's to get right.

## Consequences

- **Positive:**
  - One line in `plugins`, validated, typed.
- **Negative:**
  - Docusaurus's `validateOptions` api is its own; a Docusaurus 4 may change it.

## Related ADRs

- [ADR-003: The Same Options, and the Same Tag, Everywhere](003-same-options.md)
