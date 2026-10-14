// semantic-release versions the repository, and every package with the same version (doc/adr/010-ci-cd.md), from the
// conventional commit messages, with the same rules and release notes as Smarter's other repositories. It runs on each
// push to main, and to alpha and beta, whose releases are prereleases (.github/workflows/pushMain.yml). Publishing to
// npm and PyPI is done by hand, with `make publish`.
const setVersion = [
  "npm version --no-git-tag-version --allow-same-version ${nextRelease.version}",
  "(cd docusaurus && npm version --no-git-tag-version --allow-same-version ${nextRelease.version})",
  'sed -i -E \'s/^version = "[^"]+"/version = "${nextRelease.version}"/\' mkdocs/pyproject.toml sphinx/pyproject.toml',
  'sed -i -E \'s/^__version__ = "[^"]+"/__version__ = "${nextRelease.version}"/\' mkdocs/src/mkdocs_smarter_chat/__init__.py sphinx/src/sphinx_smarter_chat/__init__.py',
].join(" && ");

export default {
  branches: ["main", { name: "beta", prerelease: true }, { name: "alpha", prerelease: true }],
  plugins: [
    [
      "@semantic-release/commit-analyzer",
      {
        preset: "conventionalcommits",
        releaseRules: [
          { type: "docs", release: false },
          { type: "test", release: false },
          { type: "style", release: false },
          { type: "refactor", release: false },
        ],
        parserOpts: { noteKeywords: ["BREAKING CHANGE", "BREAKING CHANGES"] },
      },
    ],
    [
      "@semantic-release/release-notes-generator",
      {
        preset: "conventionalcommits",
        presetConfig: {
          types: [
            { type: "feat", section: "Features", hidden: false },
            { type: "fix", section: "Bug Fixes", hidden: false },
            { type: "refactor", section: "Refactoring", hidden: false },
            { type: "perf", section: "Performance", hidden: false },
          ],
        },
      },
    ],
    [
      "@semantic-release/changelog",
      {
        changelogFile: "CHANGELOG.md",
        changelogTitle: `# Change Log\n\nAll notable changes to this project will be documented in this file.\n\nThe format is based on [Keep a Changelog](http://keepachangelog.com/) and this project adheres to [Semantic Versioning](http://semver.org/).\n\n`,
      },
    ],
    ["@semantic-release/exec", { prepareCmd: setVersion }],
    "@semantic-release/github",
    [
      "@semantic-release/git",
      {
        assets: [
          "CHANGELOG.md",
          "package.json",
          "package-lock.json",
          "docusaurus/package.json",
          "docusaurus/package-lock.json",
          "mkdocs/pyproject.toml",
          "sphinx/pyproject.toml",
          "mkdocs/src/mkdocs_smarter_chat/__init__.py",
          "sphinx/src/sphinx_smarter_chat/__init__.py",
        ],
        message: "chore(release): ${nextRelease.version} [skip ci]\n\n${nextRelease.notes}",
      },
    ],
  ],
};
