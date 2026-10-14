---
name: monthly-maintenance
description: Use when asked to do smarter-docs-site-generators' monthly maintenance, or part of it - bump embed.json to the latest @smarter.sh/ui-chat and pick up its new options in every package, update the generators (Docusaurus, MkDocs, Material, Sphinx, VitePress) and dev dependencies, retest every package, and write a "fix" or "feat" git commit.
---

# Monthly Maintenance

1. **The embed script.** Compare `embed.json` with
   `npm view @smarter.sh/ui-chat version`; read `../smarter-chat/CHANGELOG.md`
   between them. `make embed-version V=<version>`; add new options to every
   package (see "Adding an option" in `smarter-docs-sites-development`).
   Minor: `feat`; patch: `fix`.
2. **Generators.** Check the latest Docusaurus (its plugin api, `injectHtmlTags`,
   `validateOptions`), MkDocs, Material, Sphinx and VitePress releases; widen
   the version ranges in the packages' metadata when the tests pass.
3. **Dependencies.** `npm update` in `docusaurus/` and `vitepress/example/`,
   `venv/bin/pip install -U -e ...`, `pre-commit autoupdate`.
4. **Test.** `make lint test`.
5. **Commit.** Load `smarter-git-commits`. Publishing is the user's step.
