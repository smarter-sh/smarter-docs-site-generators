"""Tests of the MkDocs plugin, its tag, and real mkdocs builds."""

import shutil
import subprocess
import sys
from pathlib import Path

import pytest

from htmltags import elements, embed_scripts
from mkdocs.config.defaults import MkDocsConfig
from mkdocs.exceptions import PluginError
from mkdocs_smarter_chat import EMBED_VERSION, tag
from mkdocs_smarter_chat.plugin import SmarterChatPlugin

SITE = Path(__file__).parent / "site"


def plugin(options: dict) -> SmarterChatPlugin:
    """A configured plugin, as mkdocs creates it."""
    instance = SmarterChatPlugin()
    errors, _ = instance.load_config(options)
    assert errors == []
    return instance


def test_the_embed_version_is_embed_json(embed):
    assert EMBED_VERSION == embed["version"]


def test_writes_the_expected_tags(expected):
    for case in expected["cases"]:
        page = "<html><body><p>docs</p></body></html>"
        output = plugin(case["options"]).on_post_page(page, page=None, config=None)
        assert embed_scripts(output) == [case["attributes"]], case["name"]
        # the tag is before </body>, and adds no element but the script.
        assert elements(output) == ["html", "body", "p", "script"], case["name"]


def test_invalid_options_fail_the_build(expected):
    for case in expected["invalid"]:
        options = case["options"]
        if options.get("position") not in (None, *tag.POSITIONS):
            # mkdocs' own Choice option rejects it, before the plugin.
            errors, _ = SmarterChatPlugin().load_config(options)
            assert errors, case["name"]
            continue
        with pytest.raises(PluginError, match=r'^smarter-chat: "'):
            plugin(options).on_config(MkDocsConfig())


def test_the_tag_is_escaped():
    html = tag.script_tag({"chatbot": "https://docs-bot.example.com/", "label": '"><script>alert(1)</script>'})
    assert 'data-label="&quot;&gt;&lt;script&gt;alert(1)&lt;/script&gt;"' in html
    assert html.count("<script") == 1


def test_a_page_without_a_body_is_unchanged():
    assert (
        plugin({"chatbot": "https://docs-bot.example.com/"}).on_post_page("<p>x</p>", page=None, config=None)
        == "<p>x</p>"
    )


def test_validate_checks_types():
    with pytest.raises(ValueError, match='"color"'):
        tag.validate({"chatbot": "https://docs-bot.example.com/", "color": 123})


def build(tmp_path: Path, theme: str | None = None) -> Path:
    """A real mkdocs build of tests/site, with a theme, into tmp_path."""
    site = tmp_path / "site"
    shutil.copytree(SITE, site)
    if theme:
        config = site / "mkdocs.yml"
        config.write_text(config.read_text() + f"theme:\n  name: {theme}\n")
    subprocess.run([sys.executable, "-m", "mkdocs", "build", "--strict", "-q"], cwd=site, check=True)
    return site / "site"


@pytest.mark.parametrize("theme", [None, "material"])
def test_a_real_build_has_the_tag_on_every_page(tmp_path, theme):
    if theme == "material":
        pytest.importorskip("material")
    output = build(tmp_path, theme)
    for page in ("index.html", "guide/index.html"):
        scripts = embed_scripts((output / page).read_text())
        assert scripts == [
            {
                "src": f"https://cdn.jsdelivr.net/npm/@smarter.sh/ui-chat@{EMBED_VERSION}/dist/embed.js",
                "data-chatbot": "https://docs-bot.example.com/",
                "data-position": "bottom-left",
                "async": True,
            }
        ], page


def test_a_real_build_fails_without_a_chatbot(tmp_path):
    site = tmp_path / "site"
    shutil.copytree(SITE, site)
    (site / "mkdocs.yml").write_text("site_name: Smoke\nplugins:\n  - smarter-chat\n")
    result = subprocess.run([sys.executable, "-m", "mkdocs", "build", "-q"], cwd=site, capture_output=True, text=True)
    assert result.returncode != 0
    assert '"chatbot" must be' in result.stderr


def test_validate_rejects_an_unknown_position():
    with pytest.raises(tag.OptionError) as error:
        tag.validate({"chatbot": "https://docs-bot.example.com/", "position": "top"})
    assert error.value.name == "position"


def test_valid_options_pass_on_config():
    config = MkDocsConfig()
    assert plugin({"chatbot": "https://docs-bot.example.com/"}).on_config(config) is config
