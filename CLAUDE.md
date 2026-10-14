# CLAUDE.md

Guidance for Claude Code (and other coding agents) working in this repository.

smarter-docs-site-generators is **Smarter Chat for documentation sites**: one
package per static site generator, each of which adds the chat launcher of
[`@smarter.sh/ui-chat`](https://github.com/smarter-sh/smarter-chat)'s embed
script (`../smarter-chat`) to every page of a built site:

| Directory     | Package                                                 | Ecosystem |
| ------------- | ------------------------------------------------------- | --------- |
| `docusaurus/` | `@smarter.sh/docusaurus-plugin-smarter-chat`            | npm       |
| `mkdocs/`     | `mkdocs-smarter-chat` (plugin `smarter-chat`)           | PyPI      |
| `sphinx/`     | `sphinx-smarter-chat` (extension `sphinx_smarter_chat`) | PyPI      |
| `vitepress/`  | a `head` recipe and an example site (no package)        | -         |

The chatbot is an LLMClient on a Smarter platform
([smarter-sh/smarter](https://github.com/smarter-sh/smarter), `../smarter`).

Detailed know-how lives in the Agent Skills under `skills/` (symlinked to
`.claude/skills`). **Load `smarter-docs-sites-development` first for any
change.**

## Hard rules

1. **Never run git write commands**, here, in `../smarter` or in
   `../smarter-chat`. "Write a git commit" means print the command as text.
   See `smarter-git-commits`.
2. **Never publish** (`npm publish`, `twine upload`, `make publish`): that is
   the user's step.
3. **Run the tests yourself** after any change (`make test`, every package).
   Report failures honestly.
4. **The same options and the same tag everywhere**
   (`doc/adr/003-same-options.md`): a change to one package's options is a
   change to all of them, and to `test/expected-tag.json`.
5. **The embed version is in `embed.json`**, copied into each package by
   `make embed-version`. Never edit a package's copy by hand.
6. **The pre-commit hooks are the lint standard.** See `smarter-code-quality`.
7. **Coverage:** at least 95% of each package.
8. **This repository is public.** No api keys, tokens or customer data.

## Common commands

```bash
make init                    # venv/ with the Python packages and their test deps, npm, pre-commit
make test                    # every package: Docusaurus (Vitest), MkDocs and Sphinx (pytest), VitePress (a real build)
make test-docusaurus | test-mkdocs | test-sphinx | test-vitepress
make embed-version V=0.9.1   # embed.json and every package's copy
make build                   # build/: the npm tarball and the Python sdists and wheels
git diff --name-only | xargs venv/bin/pre-commit run --files
```

User documentation lives in the platform's repository:
`../smarter/docs/source/smarter-framework/smarter-docs-sites.rst`.

## Definition of done

- The change follows the ADRs in `doc/adr/`, in every package that it concerns.
- `make test` passes, and you ran it.
- Pre-commit hooks pass on the changed files.
- The packages' READMEs and docs.smarter.sh describe user-facing changes.
- Your summary says what changed, what you verified, and what you skipped.
