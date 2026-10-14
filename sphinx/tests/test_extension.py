"""Tests of the Sphinx extension, with real Sphinx builds of tests/roots/basic in a temporary directory."""

import shutil
from pathlib import Path

import pytest

from htmltags import embed_scripts
from sphinx.application import Sphinx
from sphinx.errors import ConfigError
from sphinx_smarter_chat import EMBED_VERSION, tag

ROOT = Path(__file__).parent / "roots" / "basic"


def build(tmp_path: Path, builder: str = "html", **options) -> Path:
    """A real Sphinx build, with the extension's options as smarter_chat_<option> overrides."""
    source = tmp_path / "source"
    shutil.copytree(ROOT, source)
    out = tmp_path / "out"
    overrides = {f"smarter_chat_{name}": value for name, value in options.items()}
    app = Sphinx(
        str(source),
        str(source),
        str(out),
        str(tmp_path / "doctrees"),
        builder,
        confoverrides=overrides,
        status=None,
        warning=None,
        freshenv=True,
    )
    app.build()
    return out


def test_the_embed_version_is_embed_json(embed):
    assert EMBED_VERSION == embed["version"]


def test_writes_the_expected_tags_on_every_page(tmp_path, expected):
    for index, case in enumerate(expected["cases"]):
        out = build(tmp_path / str(index), **case["options"])
        for page in ("index.html", "guide.html"):
            assert embed_scripts((out / page).read_text()) == [case["attributes"]], (case["name"], page)


def test_invalid_options_fail_the_build(tmp_path, expected):
    for index, case in enumerate(expected["invalid"]):
        options = dict(case["options"])
        options.setdefault("chatbot", "")
        with pytest.raises(ConfigError, match=r"^sphinx_smarter_chat: smarter_chat_"):
            build(tmp_path / str(index), **options)


def test_the_tag_is_escaped(tmp_path):
    out = build(tmp_path, label='"><script>alert(1)</script>')
    html = (out / "index.html").read_text()
    assert "&#34;&gt;&lt;script&gt;" in html or "&quot;&gt;&lt;script&gt;" in html
    assert "<script>alert(1)" not in html


def test_non_html_builders_have_no_script(tmp_path):
    out = build(tmp_path, builder="text")
    assert "embed.js" not in (out / "index.txt").read_text()


def test_the_extension_is_parallel_safe():
    from sphinx_smarter_chat import setup

    class App:
        def __init__(self):
            self.values = {}
            self.events = []

        def add_config_value(self, name, default, rebuild):
            self.values[name] = (default, rebuild)

        def connect(self, event, callback):
            self.events.append(event)

    app = App()
    metadata = setup(app)
    assert metadata["parallel_read_safe"] and metadata["parallel_write_safe"]
    assert "smarter_chat_chatbot" in app.values and app.values["smarter_chat_open"] == (False, "html")
    assert app.events == ["config-inited", "builder-inited"]


def test_tag_attributes_leave_out_unset_options():
    assert list(tag.attributes({"chatbot": "https://docs-bot.example.com/", "open": False, "label": ""})) == [
        "src",
        "data-chatbot",
        "async",
    ]


def test_script_tag_is_the_same_tag_as_the_other_packages(expected):
    for case in expected["cases"]:
        assert embed_scripts(tag.script_tag(case["options"])) == [case["attributes"]], case["name"]


def test_tag_is_the_same_module_as_mkdocs_smarter_chats():
    """The two packages' tag.py must stay the same, but for where they get the embed version (doc/adr/002-monorepo.md)."""
    ours = Path(tag.__file__).read_text().splitlines()
    theirs = (Path(__file__).parents[2] / "mkdocs" / "src" / "mkdocs_smarter_chat" / "tag.py").read_text().splitlines()
    differences = [
        line
        for line in set(ours) ^ set(theirs)
        if "EMBED_VERSION" not in line and "dependency" not in line and "Copied from embed.json" not in line
    ]
    assert differences == []
