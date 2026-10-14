# Smarter Chat for documentation sites

> Add a [Smarter](https://smarter.sh) chatbot to every page of a documentation site, with one setting in Docusaurus,
> MkDocs (and Material), Sphinx or VitePress.

[![Build](https://github.com/smarter-sh/smarter-docs-site-generators/actions/workflows/build.yml/badge.svg?branch=main)](https://github.com/smarter-sh/smarter-docs-site-generators/actions/workflows/build.yml)
[![Test](https://github.com/smarter-sh/smarter-docs-site-generators/actions/workflows/test.yml/badge.svg?branch=main)](https://github.com/smarter-sh/smarter-docs-site-generators/actions/workflows/test.yml)
[![Docusaurus coverage](https://img.shields.io/codecov/c/github/smarter-sh/smarter-docs-site-generators/main?flag=docusaurus&label=Docusaurus%20coverage&logo=codecov)](https://app.codecov.io/gh/smarter-sh/smarter-docs-site-generators?flags%5B0%5D=docusaurus)
[![MkDocs coverage](https://img.shields.io/codecov/c/github/smarter-sh/smarter-docs-site-generators/main?flag=mkdocs&label=MkDocs%20coverage&logo=codecov)](https://app.codecov.io/gh/smarter-sh/smarter-docs-site-generators?flags%5B0%5D=mkdocs)
[![Sphinx coverage](https://img.shields.io/codecov/c/github/smarter-sh/smarter-docs-site-generators/main?flag=sphinx&label=Sphinx%20coverage&logo=codecov)](https://app.codecov.io/gh/smarter-sh/smarter-docs-site-generators?flags%5B0%5D=sphinx)
[![License: AGPL v3](https://img.shields.io/badge/license-AGPL--3.0--or--later-blue)](LICENSE.txt)

Each package adds the chat launcher of [`@smarter.sh/ui-chat`](https://github.com/smarter-sh/smarter-chat)'s embed
script, a chat button that opens the chat, to every page of the built site. The chatbot is an LLMClient that you build
and deploy on a Smarter platform, for example with your docs in a vectorstore.

| Generator           | Install                                                  | Configure                                                                      |
| ------------------- | -------------------------------------------------------- | ------------------------------------------------------------------------------ |
| Docusaurus          | `npm install @smarter.sh/docusaurus-plugin-smarter-chat` | [docusaurus/](docusaurus/README.md): `plugins` in `docusaurus.config.js`       |
| MkDocs (+ Material) | `pip install mkdocs-smarter-chat`                        | [mkdocs/](mkdocs/README.md): `plugins` in `mkdocs.yml`                         |
| Sphinx              | `pip install sphinx-smarter-chat`                        | [sphinx/](sphinx/README.md): `extensions` in `conf.py`                         |
| VitePress           | nothing                                                  | [vitepress/](vitepress/README.md): one `head` entry in `.vitepress/config.mts` |

Every one writes the same tag, with the same options, and fails the build if the chatbot's url is missing or invalid.
Other generators (Hugo, Jekyll, Astro) need only that tag in their base template; see the
[guide](https://docs.smarter.sh/en/latest/smarter-framework/smarter-docs-sites.html).

## Development

```console
make init     # venv/ with both Python packages, npm, pre-commit
make test     # every package: Vitest, pytest with real MkDocs and Sphinx builds, a real VitePress build
make embed-version V=0.9.1
```

The repository is developed with [Agent Skills](skills/README.md) for AI coding agents; start with
[CLAUDE.md](CLAUDE.md). The design is in the [architecture decisions](doc/adr/000-intro.md). See
[CONTRIBUTING.md](.github/CONTRIBUTING.md).

## License

[AGPL-3.0-or-later](LICENSE.txt), as Smarter is.
