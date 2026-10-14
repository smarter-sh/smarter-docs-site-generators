# ADR-012: Licensing and Documentation

## Status

Accepted

## Decision

- **License:** AGPL-3.0-or-later, as Smarter is. The packages don't contain the embed script; they write its tag.
- **Documentation:** each package's `README.md` is its registry page (npm, PyPI): install, configure, options. docs.smarter.sh has the page `smarter-framework/smarter-docs-sites.rst`, in the platform's repository, listed in Smarter APIs and SDKs, covering all four generators, the LLMClient's `allowedOrigins`, and the tag for other generators (Hugo, Jekyll). Prose is evergreen.

## Consequences

- **Positive:**
  - Each registry page stands alone; docs.smarter.sh compares them.
- **Negative:**
  - AGPL may give some documentation teams pause for a build-time plugin; the plugins' output is a script tag, not AGPL code in their site.
