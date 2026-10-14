# ADR-001: Scope

## Status

Accepted

## Context

Documentation sites are where a product's users ask questions, and a Smarter LLMClient with the docs in a vectorstore can answer them. Most documentation sites are built by a static site generator: Docusaurus, MkDocs (often with the Material theme), Sphinx (with Read the Docs' theme or Furo) and VitePress are among the most used. Each has its own way to add a script to every page.

## Decision

This repository makes the chat launcher of `@smarter.sh/ui-chat`'s embed script one configuration entry in each of those four generators:

| Generator           | Deliverable                                                         | Configured in           |
| ------------------- | ------------------------------------------------------------------- | ----------------------- |
| Docusaurus          | npm package `@smarter.sh/docusaurus-plugin-smarter-chat`            | `docusaurus.config.js`  |
| MkDocs (+ Material) | PyPI package `mkdocs-smarter-chat`, plugin `smarter-chat`           | `mkdocs.yml`            |
| Sphinx              | PyPI package `sphinx-smarter-chat`, extension `sphinx_smarter_chat` | `conf.py`               |
| VitePress           | a documented `head` entry, and a tested example (ADR-007)           | `.vitepress/config.mts` |

Each adds the launcher to every page of the built site. The chat itself is the embed script; nothing here renders a chat.

## Alternatives Considered

- **Docs pages only**, telling users to add the script tag to each generator's template. Every generator can do it, but each needs a template override (Sphinx, MkDocs) or a custom component (Docusaurus), which a plugin replaces with one setting.
- **More generators** (Hugo, Jekyll, Astro Starlight, GitBook). Hugo and Jekyll take the tag in a partial; docs.smarter.sh shows it. Others can be added the same way when users ask.

## Consequences

- **Positive:**
  - Documentation teams add the chat without touching templates.
- **Negative:**
  - Four ecosystems, two languages, three registries to maintain (ADR-002, ADR-010).

## Related ADRs

- [ADR-002: One Repository, One Package per Generator](002-monorepo.md)
- [ADR-003: The Same Options, and the Same Tag, Everywhere](003-same-options.md)
