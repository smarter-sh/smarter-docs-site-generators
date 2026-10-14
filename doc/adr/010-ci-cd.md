# ADR-010: CI/CD, Versioning and Publishing

## Status

Accepted

## Context

Three packages are published to two registries, and their users expect semantic versions.

## Decision

- GitHub Actions: `test.yml` runs each package's tests (Python 3.10 to 3.14 for MkDocs and Sphinx; Node.js 22 and 24 for Docusaurus and VitePress) and the shared checks, for every push and pull request. `pushMain.yml` runs semantic-release on `main`, `beta` and `alpha`.
- One version for the repository and all its packages, set by semantic-release from conventional commits, written into `docusaurus/package.json`, `mkdocs/pyproject.toml` and `sphinx/pyproject.toml`. Updating the embed script to a new minor version is a `feat`; to a patch, a `fix`.
- Publishing is by hand, after a release: `make publish` builds and uploads the npm package and both Python packages.

## Consequences

- **Positive:**
  - One release note for one change, whichever package it touches.
- **Negative:**
  - A release of one package is a release of all three; an unchanged package gets a new version.

## Related ADRs

- [ADR-002: One Repository, One Package per Generator](002-monorepo.md)
