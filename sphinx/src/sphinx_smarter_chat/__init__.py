"""
sphinx-smarter-chat: a Sphinx extension that adds a Smarter chatbot to every page of a documentation site.

.. code-block:: python

    # conf.py
    extensions = ["sphinx_smarter_chat"]
    smarter_chat_chatbot = "https://docs-bot.example.com/"

Every option of the embed script's launcher is a config value, prefixed ``smarter_chat_``: ``chatbot`` (required),
``api_key``, ``position``, ``label``, ``color``, ``open``, ``height``, ``width``, ``version`` and ``src``. See
``doc/adr/006-sphinx.md``.
"""

from __future__ import annotations

from typing import Any

from sphinx.application import Sphinx
from sphinx.config import Config
from sphinx.errors import ConfigError

from . import tag
from .tag import EMBED_VERSION

__version__ = "0.1.0-alpha.1"
__all__ = ["EMBED_VERSION", "setup"]

OPTIONS: dict[str, Any] = {
    "chatbot": "",
    "api_key": None,
    "position": None,
    "label": None,
    "color": None,
    "open": False,
    "height": None,
    "width": None,
    "version": None,
    "src": None,
}
"""The options, and their defaults. Each is the config value ``smarter_chat_<option>``."""


def options(config: Config) -> dict[str, Any]:
    """
    The options, from the project's configuration.

    :param config: The Sphinx configuration.
    :returns: The options, in snake_case, without the prefix.
    """
    return {name: getattr(config, f"smarter_chat_{name}") for name in OPTIONS}


def check_config(app: Sphinx, config: Config) -> None:
    """
    Fail the build if an option is invalid. Connected to ``config-inited``.

    :param app: The Sphinx application.
    :param config: The Sphinx configuration.
    :raises ConfigError: If an option is invalid.
    """
    try:
        tag.validate(options(config))
    except tag.OptionError as error:
        raise ConfigError(f"sphinx_smarter_chat: smarter_chat_{error.name} {error.message}") from error


def add_script(app: Sphinx) -> None:
    """
    Add the embed script to every page, for html builders. Connected to ``builder-inited``.

    :param app: The Sphinx application.
    """
    if app.builder.format != "html":
        return
    attributes = tag.attributes(options(app.config))
    src = str(attributes.pop("src"))
    attributes.pop("async")
    app.add_js_file(src, loading_method="async", **attributes)


def setup(app: Sphinx) -> dict[str, Any]:
    """
    Register the extension's config values and events.

    :param app: The Sphinx application.
    :returns: The extension's metadata.
    """
    for name, default in OPTIONS.items():
        app.add_config_value(f"smarter_chat_{name}", default, "html")
    app.connect("config-inited", check_config)
    app.connect("builder-inited", add_script)
    return {"version": __version__, "parallel_read_safe": True, "parallel_write_safe": True}
