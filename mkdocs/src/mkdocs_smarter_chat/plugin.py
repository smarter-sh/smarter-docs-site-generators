"""
The MkDocs plugin ``smarter-chat``: adds the embed script's tag before each page's ``</body>``.

.. code-block:: yaml

    # mkdocs.yml
    plugins:
      - search
      - smarter-chat:
          chatbot: https://docs-bot.example.com/

See ``doc/adr/005-mkdocs.md``.
"""

from __future__ import annotations

from typing import Any

from mkdocs.config import base
from mkdocs.config import config_options as c
from mkdocs.config.defaults import MkDocsConfig
from mkdocs.exceptions import PluginError
from mkdocs.plugins import BasePlugin
from mkdocs.structure.pages import Page

from . import tag


class SmarterChatConfig(base.Config):
    """The plugin's options, in ``mkdocs.yml``. Only ``chatbot`` is required."""

    chatbot = c.Type(str, default="")
    api_key = c.Optional(c.Type(str))
    position = c.Optional(c.Choice(tag.POSITIONS))
    label = c.Optional(c.Type(str))
    color = c.Optional(c.Type(str))
    open = c.Type(bool, default=False)
    height = c.Optional(c.Type(str))
    width = c.Optional(c.Type(str))
    version = c.Optional(c.Type(str))
    src = c.Optional(c.Type(str))


class SmarterChatPlugin(BasePlugin[SmarterChatConfig]):
    """Adds the Smarter Chat launcher to every page."""

    def options(self) -> dict[str, Any]:
        """
        The plugin's options, as the embed script's tag reads them.

        :returns: The options, in snake_case.
        """
        return dict(self.config.items())

    def on_config(self, config: MkDocsConfig) -> MkDocsConfig:
        """
        Fail the build if an option is invalid.

        :param config: The site's configuration.
        :returns: The configuration, unchanged.
        :raises PluginError: If an option is invalid.
        """
        try:
            tag.validate(self.options())
        except tag.OptionError as error:
            raise PluginError(f"smarter-chat: {error}") from error
        return config

    def on_post_page(self, output: str, /, *, page: Page, config: MkDocsConfig) -> str:
        """
        Add the embed script's tag before the page's last ``</body>``.

        :param output: The page's html.
        :param page: The page.
        :param config: The site's configuration.
        :returns: The page's html, with the tag, or unchanged if it has no ``</body>``.
        """
        position = output.lower().rfind("</body>")
        if position < 0:
            return output
        return f"{output[:position]}{tag.script_tag(self.options())}\n{output[position:]}"
