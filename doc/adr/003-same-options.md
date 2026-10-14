# ADR-003: The Same Options, and the Same Tag, Everywhere

## Status

Accepted

## Context

The embed script reads the launcher's options from its script tag's `data-` attributes. Each generator names configuration in its own style: camelCase in JavaScript, snake_case in YAML and Python.

## Decision

- Every package accepts the same options, named in its ecosystem's style: `chatbot` (required), `apiKey` / `api_key`, `position`, `label`, `color`, `open`, `height`, `width`, plus `version` and `src` (ADR-008).
- Every package writes **the same tag**, one `<script src="…/embed.js" data-chatbot="…" … async></script>`, with html-escaped attributes, and only the options that are set. Its tests compare it with the same expected tag.
- A package validates what it can at build time (a chatbot url must be `http(s)`; a position must be one of two), and fails the build with a clear message when the chatbot is missing or invalid, rather than shipping a site without its chat.

## Alternatives Considered

- **`window.SmarterChatConfig` in an inline script.** One more script, which a site's Content Security Policy must allow. The tag's attributes need nothing more.

## Consequences

- **Positive:**
  - The same result on every generator, and one shape of tag to test.

## Related ADRs

- [ADR-008: The Embed Script Is Loaded from jsDelivr, at a Pinned Version](008-cdn.md)
- [ADR-009: Testing](009-testing.md)
