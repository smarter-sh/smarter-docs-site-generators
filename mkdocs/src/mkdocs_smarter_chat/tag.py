"""
The embed script's tag: its attributes, validated, and its html.

Every Smarter Chat package for documentation sites writes the same tag for the same options
(``doc/adr/003-same-options.md``). This module has no MkDocs dependency.
"""

from __future__ import annotations

import html
import re
from collections.abc import Mapping
from typing import Union

from . import EMBED_VERSION

POSITIONS = ("bottom-right", "bottom-left")
"""The launcher's corners."""

HTTP_URL = re.compile(r"^https?://[^\s\"'<>`]+$", re.IGNORECASE)
HEX_COLOR = re.compile(r"^#([0-9a-f]{3}|[0-9a-f]{6})$", re.IGNORECASE)
CSS_LENGTH = re.compile(r"^\d{1,5}(\.\d{1,3})?(px|em|rem|vh|vw|svh|dvh|%)$")
VERSION = re.compile(r"^\d+(\.\d+){0,2}(-[0-9A-Za-z.]+)?$")
SCRIPT_SRC = re.compile(r"^(https?://|/)[^\s\"'<>`]*$", re.IGNORECASE)

DATA_ATTRIBUTES = {
    "chatbot": "data-chatbot",
    "api_key": "data-api-key",
    "position": "data-position",
    "label": "data-label",
    "color": "data-color",
    "open": "data-open",
    "height": "data-height",
    "width": "data-width",
}
"""The options that become data- attributes, by option name."""

OptionValue = Union[str, bool, None]


class OptionError(ValueError):
    """
    An invalid option.

    :param name: The option's name, e.g. ``chatbot``.
    :param message: What it must be, e.g. ``must be a hex color``.
    """

    def __init__(self, name: str, message: str) -> None:
        super().__init__(f'"{name}" {message}')
        self.name = name
        self.message = message


def validate(options: Mapping[str, OptionValue]) -> None:
    """
    Check the options.

    :param options: The options, in snake_case.
    :raises OptionError: If an option is invalid.
    """
    chatbot = options.get("chatbot")
    if not isinstance(chatbot, str) or not HTTP_URL.match(chatbot):
        raise OptionError("chatbot", f"must be the http(s) url of a deployed LLMClient, not {chatbot!r}.")
    position = options.get("position")
    if position is not None and position not in POSITIONS:
        raise OptionError("position", f"must be one of {', '.join(POSITIONS)}.")
    checks = (
        ("color", HEX_COLOR, "a hex color, e.g. #ff5733"),
        ("height", CSS_LENGTH, "a css length, e.g. 600px"),
        ("width", CSS_LENGTH, "a css length, e.g. 400px"),
        ("version", VERSION, "a version, e.g. 0.9.0"),
        ("src", SCRIPT_SRC, "an http(s) url or a path"),
    )
    for name, pattern, description in checks:
        value = options.get(name)
        if value is not None and (not isinstance(value, str) or not pattern.match(value)):
            raise OptionError(name, f"must be {description}.")


def attributes(options: Mapping[str, OptionValue]) -> dict[str, str | bool]:
    """
    The embed script tag's attributes: its src, the options that are set, as data- attributes, and async.

    :param options: The options, in snake_case, validated.
    :returns: The attributes, not yet escaped. ``async`` is ``True``.
    """
    version = options.get("version") or EMBED_VERSION
    src = options.get("src") or f"https://cdn.jsdelivr.net/npm/@smarter.sh/ui-chat@{version}/dist/embed.js"
    result: dict[str, str | bool] = {"src": str(src)}
    for name, attribute in DATA_ATTRIBUTES.items():
        value: OptionValue | None = options.get(name)
        if value is None or value == "" or value is False:
            continue
        result[attribute] = "true" if value is True else str(value)
    result["async"] = True
    return result


def script_tag(options: Mapping[str, OptionValue]) -> str:
    """
    The embed script's tag, with its attributes escaped.

    :param options: The options, in snake_case, validated.
    :returns: ``<script src="..." data-chatbot="..." async></script>``
    """
    parts = []
    for name, value in attributes(options).items():
        parts.append(name if value is True else f'{name}="{html.escape(str(value), quote=True)}"')
    return f"<script {' '.join(parts)}></script>"
