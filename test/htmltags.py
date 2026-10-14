"""Finds the embed script's tags in html, with the standard library's parser."""

from html.parser import HTMLParser


class ScriptFinder(HTMLParser):
    """Collects the attributes of the script tags whose src is an embed.js."""

    def __init__(self) -> None:
        super().__init__()
        self.scripts: list[dict] = []
        self.elements: list[str] = []

    def handle_starttag(self, tag, attrs):
        self.elements.append(tag)
        attributes = {name: (True if value is None else value) for name, value in attrs}
        if tag == "script" and str(attributes.get("src", "")).endswith("embed.js"):
            self.scripts.append(attributes)


def embed_scripts(html: str) -> list[dict]:
    """The attributes of the html's embed script tags, with async normalized to True."""
    finder = ScriptFinder()
    finder.feed(html)
    for script in finder.scripts:
        if "async" in script:
            script["async"] = True
    return finder.scripts


def elements(html: str) -> list[str]:
    """The html's elements' names, in order."""
    finder = ScriptFinder()
    finder.feed(html)
    return finder.elements
