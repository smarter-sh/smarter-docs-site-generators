---
name: smarter-code-quality
description: Use before finishing any change to smarter-docs-site-generators, to lint and format it - black, isort, flake8 and pyupgrade for the Python packages, Prettier, ESLint and tsc for the JavaScript, codespell, the generic pre-commit hooks and commitlint, run from venv/ under zsh.
---

# Smarter Chat for documentation sites: Code Quality

`.pre-commit-config.yaml` is the standard. Never bypass a hook.

| Language   | Tools                                   | Configuration                          |
| ---------- | --------------------------------------- | -------------------------------------- |
| Python     | black, isort, flake8, pyupgrade         | `pyproject.toml`, `.flake8`            |
| JavaScript | Prettier, ESLint, `tsc` on `index.d.ts` | `.prettierrc.json`, `eslint.config.js` |
| everything | codespell, generic hooks, commitlint    | `codespell.txt`                        |

```console
make lint
git diff --name-only | xargs venv/bin/pre-commit run --files
```

Use `xargs`: under zsh, `--files $FILES` is one argument. Python docstrings are
reST (`:param:`, `:returns:`, `:raises:`), as in the platform and the Python SDK.
