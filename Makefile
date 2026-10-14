# ---------------------------------------------------------
# Smarter Chat for documentation sites. See README.md and
# CLAUDE.md. One directory per generator; the Python
# packages share venv/.
# ---------------------------------------------------------
SHELL := /bin/bash
PYTHON ?= python3
VENV := venv/bin
# The developer's shell may export NODE_ENV=production, which makes npm skip devDependencies.
NPM_INSTALL := npm install --include=dev --no-audit --no-fund

.PHONY: all init test test-docusaurus test-mkdocs test-sphinx test-vitepress lint embed-version build publish clean help

all: help

init:
	$(PYTHON) -m venv venv
	$(VENV)/pip install --upgrade pip
	$(VENV)/pip install -e mkdocs -e sphinx -r requirements-dev.txt
	$(NPM_INSTALL)
	cd docusaurus && $(NPM_INSTALL)
	cd vitepress/example && $(NPM_INSTALL)
	$(VENV)/pre-commit install

test: test-docusaurus test-mkdocs test-sphinx test-vitepress

test-docusaurus:
	cd docusaurus && npx vitest run --coverage && npm run typecheck

test-mkdocs:
	$(VENV)/python -m pytest mkdocs/tests --cov=mkdocs_smarter_chat --cov-report=term-missing --cov-report=xml:coverage/mkdocs.xml --cov-fail-under=95

test-sphinx:
	$(VENV)/python -m pytest sphinx/tests --cov=sphinx_smarter_chat --cov-report=term-missing --cov-report=xml:coverage/sphinx.xml --cov-fail-under=95

test-vitepress:
	cd vitepress/example && npm run build
	node scripts/check-vitepress.mjs

lint:
	$(VENV)/pre-commit run --all-files

# make embed-version V=0.9.1
embed-version:
	$(VENV)/python scripts/embed_version.py $(V)

# build/: the npm tarball, and the Python sdists and wheels. `make publish` uploads them (the user's step).
build:
	rm -rf build && mkdir -p build
	cd docusaurus && npm pack --pack-destination ../build
	$(VENV)/python -m build --outdir build mkdocs
	$(VENV)/python -m build --outdir build sphinx

publish: build
	cd docusaurus && npm publish --access public
	$(VENV)/python -m twine upload build/*.whl build/*.tar.gz

clean:
	rm -rf venv node_modules docusaurus/node_modules vitepress/example/node_modules vitepress/example/docs/.vitepress/dist vitepress/example/docs/.vitepress/cache build coverage .coverage docusaurus/coverage

help:
	@echo '===================================================================='
	@echo 'Smarter Chat for documentation sites'
	@echo '===================================================================='
	@echo 'init            - venv/ (Python packages, test deps), npm, pre-commit'
	@echo 'test            - every package: Docusaurus, MkDocs, Sphinx, VitePress'
	@echo 'test-<name>     - one of them'
	@echo 'lint            - the pre-commit hooks, on every file'
	@echo 'embed-version   - make embed-version V=0.9.1'
	@echo 'build           - build/: npm tarball, Python sdists and wheels'
	@echo 'publish         - build, then upload to npm and PyPI (the maintainer, by hand)'
