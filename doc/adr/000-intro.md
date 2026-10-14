# ADR Introduction

Architectural Design Records (ADRs) are short documents that capture a single architectural or design decision, its context, and its consequences. Less is more: keep them brief.

These are the ADRs of Smarter Chat for documentation sites: plugins for Docusaurus, MkDocs (and MkDocs Material) and Sphinx, and a recipe for VitePress, that add a Smarter chatbot to a documentation site. They follow the Smarter platform's own [ADRs](https://github.com/smarter-sh/smarter/tree/main/docs/source/adr) and those of the [Python SDK](https://github.com/smarter-sh/smarter-python/tree/main/doc/adr), from which this repository's layout is copied, and its siblings for [WordPress](https://github.com/smarter-sh/smarter-wordpress/tree/main/doc/adr), [Drupal](https://github.com/smarter-sh/smarter-drupal/tree/main/doc/adr), [Shopify](https://github.com/smarter-sh/smarter-shopify/tree/main/doc/adr) and [Google Tag Manager](https://github.com/smarter-sh/smarter-gtm-template/tree/main/doc/adr).

See: [Michael Nygard's ADRs](https://cognitect.com/blog/2011/11/15/documenting-architecture-decisions.html)

## Guidelines for writing ADRs

- **One decision per ADR.**
- **Be concise.** Focus on clarity and brevity.
- **State the context:** the forces that led to the decision.
- **List the alternatives**, and why they weren't chosen.
- **Explain the decision**, and **describe its consequences**, positive and negative.
- **Use simple language**, for future contributors without today's context.
- **Use the same format** as the others, and **reference related ADRs**.

## Index

- [ADR-001: Scope](001-scope.md)
- [ADR-002: One Repository, One Package per Generator](002-monorepo.md)
- [ADR-003: The Same Options, and the Same Tag, Everywhere](003-same-options.md)
- [ADR-004: Docusaurus: a Plugin](004-docusaurus.md)
- [ADR-005: MkDocs: a Plugin](005-mkdocs.md)
- [ADR-006: Sphinx: an Extension](006-sphinx.md)
- [ADR-007: VitePress: a Recipe, Not a Package](007-vitepress.md)
- [ADR-008: The Embed Script Is Loaded from jsDelivr, at a Pinned Version](008-cdn.md)
- [ADR-009: Testing](009-testing.md)
- [ADR-010: CI/CD, Versioning and Publishing](010-ci-cd.md)
- [ADR-011: Code Quality](011-code-quality.md)
- [ADR-012: Licensing and Documentation](012-licensing-and-docs.md)
