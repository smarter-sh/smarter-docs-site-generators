# sphinx-smarter-chat

A [Sphinx](https://www.sphinx-doc.org) extension that adds a [Smarter](https://smarter.sh) chatbot to every page of a
documentation site, with any html theme (Read the Docs', Furo, PyData, Book, Alabaster): a chat button in a corner of
the page, which opens the chat. The chat is the embed script of
[`@smarter.sh/ui-chat`](https://github.com/smarter-sh/smarter-chat); its look comes from the chatbot's manifest.

```console
pip install sphinx-smarter-chat
```

```python
# conf.py
extensions = ["sphinx_smarter_chat"]
smarter_chat_chatbot = "https://docs-bot.example.com/"
```

On Read the Docs, add `sphinx-smarter-chat` to the docs' requirements file. The chatbot is a deployed LLMClient, whose
manifest must allow the site's origin (e.g. `https://<project>.readthedocs.io`) in `spec.config.prompt.allowedOrigins`.

| Config value                                | Default          | Description                                               |
| ------------------------------------------- | ---------------- | --------------------------------------------------------- |
| `smarter_chat_chatbot`                      | (required)       | The deployed LLMClient's url.                             |
| `smarter_chat_api_key`                      |                  | Only for an LLMClient that requires one. Public.          |
| `smarter_chat_position`                     | `bottom-right`   | `bottom-right` or `bottom-left`.                          |
| `smarter_chat_label`                        | `Chat`           | The button's accessible name.                             |
| `smarter_chat_color`                        | `#ff5733`        | The button's hex color.                                   |
| `smarter_chat_open`                         | `False`          | Start open.                                               |
| `smarter_chat_height`, `smarter_chat_width` | `600px`, `400px` | The panel's size, css lengths.                            |
| `smarter_chat_version`                      | this release's   | The version of `@smarter.sh/ui-chat` to load, or a range. |
| `smarter_chat_src`                          |                  | The url or path of a self-hosted `embed.js`.              |

An invalid value fails the build. Non-html builders (latex, epub's text, man) are unaffected. See the
[guide](https://docs.smarter.sh/en/latest/smarter-framework/smarter-docs-sites.html). License: AGPL-3.0-or-later.
