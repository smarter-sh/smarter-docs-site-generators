# ADR-011: Code Quality

## Status

Accepted

Follows the platform's pre-commit standard, and the Python SDK's [ADR-014](https://github.com/smarter-sh/smarter-python/blob/main/doc/adr/014-code-quality.md).

## Decision

- **Python:** black, isort, flake8 and pyupgrade, as the platform and the Python SDK use them, with reST docstrings.
- **JavaScript:** Prettier and ESLint, with JSDoc on exports, and TypeScript declarations checked by `tsc`.
- **Everything:** codespell, the generic pre-commit hooks, and commitlint.

## Consequences

- **Positive:**
  - Each package looks like the rest of Smarter's code in its language.
