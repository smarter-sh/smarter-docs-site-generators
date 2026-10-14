"""
Sets the embed script's version in embed.json, and copies it into every package: ``make embed-version V=0.9.1``.

See doc/adr/008-cdn.md. Every package's tests check that its copy is embed.json's.
"""

import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

COPIES = {
    "docusaurus/src/index.js": (r'export const EMBED_VERSION = "[^"]+";', 'export const EMBED_VERSION = "{v}";'),
    "mkdocs/src/mkdocs_smarter_chat/__init__.py": (r'EMBED_VERSION = "[^"]+"', 'EMBED_VERSION = "{v}"'),
    "sphinx/src/sphinx_smarter_chat/tag.py": (r'EMBED_VERSION = "[^"]+"', 'EMBED_VERSION = "{v}"'),
    "vitepress/example/docs/.vitepress/config.mts": (r"@smarter\.sh/ui-chat@[^/]+/", "@smarter.sh/ui-chat@{v}/"),
    "vitepress/README.md": (r"@smarter\.sh/ui-chat@\d[^/]*/", "@smarter.sh/ui-chat@{v}/"),
}


def main(version: str) -> None:
    """Write the version into embed.json, test/expected-tag.json and every package."""
    if not re.fullmatch(r"\d+\.\d+\.\d+(-[\w.]+)?", version):
        sys.exit("usage: make embed-version V=<exact version, e.g. 0.9.1>")
    embed = ROOT / "embed.json"
    data = json.loads(embed.read_text())
    old = data["version"]
    data["version"] = version
    embed.write_text(json.dumps(data, indent=2) + "\n")
    expected = ROOT / "test" / "expected-tag.json"
    expected.write_text(expected.read_text().replace(f"@smarter.sh/ui-chat@{old}/", f"@smarter.sh/ui-chat@{version}/"))
    for path, (pattern, replacement) in COPIES.items():
        file = ROOT / path
        file.write_text(re.sub(pattern, replacement.format(v=version), file.read_text()))
    print(f"The embed script is @smarter.sh/ui-chat@{version}, in embed.json and every package.")


if __name__ == "__main__":
    main(sys.argv[1] if len(sys.argv) > 1 else "")
