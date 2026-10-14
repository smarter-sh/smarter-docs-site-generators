"""Fixtures of the MkDocs plugin's tests: the shared expected tags, and embed.json."""

import json
from pathlib import Path

import pytest

ROOT = Path(__file__).resolve().parents[2]


def snake_case(name: str) -> str:
    """The snake_case name of a camelCase option, e.g. apiKey to api_key."""
    return "".join(f"_{letter.lower()}" if letter.isupper() else letter for letter in name)


@pytest.fixture(scope="session")
def expected() -> dict:
    """test/expected-tag.json, with the options in snake_case."""
    data = json.loads((ROOT / "test" / "expected-tag.json").read_text())
    for case in data["cases"] + data["invalid"]:
        case["options"] = {snake_case(name): value for name, value in case["options"].items()}
    return data


@pytest.fixture(scope="session")
def embed() -> dict:
    """embed.json."""
    return json.loads((ROOT / "embed.json").read_text())
