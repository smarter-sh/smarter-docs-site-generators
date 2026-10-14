# ADR-002: One Repository, One Package per Generator

## Status

Accepted

## Context

The four integrations do the same thing, with the same options (ADR-003), in two languages. Their users install one of them, from that generator's ecosystem.

## Decision

One repository, one directory per generator, each a complete package of its own ecosystem with its own tests: `docusaurus/` (npm), `mkdocs/` (PyPI), `sphinx/` (PyPI), `vitepress/` (an example site, ADR-007). The repository's root holds what they share: ADRs, skills, CI, release tooling, and `embed.json`, the one place that names the embed script's version (ADR-008). Each package is released with the same version (ADR-010).

## Alternatives Considered

- **A repository per generator.** Four copies of the same tooling, and changes to the shared options made four times.
- **A shared core library** used by every package. A Python and a JavaScript package can't share code, and each package's logic is a few dozen lines.

## Consequences

- **Positive:**
  - A change to the options is one pull request, tested in every generator.
- **Negative:**
  - A release of one package releases them all, with the same version.

## Related ADRs

- [ADR-008: The Embed Script Is Loaded from jsDelivr, at a Pinned Version](008-cdn.md)
- [ADR-010: CI/CD, Versioning and Publishing](010-ci-cd.md)
