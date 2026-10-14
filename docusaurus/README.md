# @smarter.sh/docusaurus-plugin-smarter-chat

A [Docusaurus](https://docusaurus.io) 3 plugin that adds a [Smarter](https://smarter.sh) chatbot to every page of a
documentation site: a chat button in a corner of the page, which opens the chat. The chat is the embed script of
[`@smarter.sh/ui-chat`](https://github.com/smarter-sh/smarter-chat); its look comes from the chatbot's manifest.

```console
npm install @smarter.sh/docusaurus-plugin-smarter-chat
```

```js
// docusaurus.config.js
export default {
  plugins: [["@smarter.sh/docusaurus-plugin-smarter-chat", { chatbot: "https://docs-bot.example.com/" }]],
};
```

The chatbot is a deployed LLMClient, whose manifest must allow the site's origin in
`spec.config.prompt.allowedOrigins`.

| Option            | Default          | Description                                                                |
| ----------------- | ---------------- | -------------------------------------------------------------------------- |
| `chatbot`         | (required)       | The deployed LLMClient's url.                                              |
| `apiKey`          |                  | Only for an LLMClient that requires one. It is public in the pages.        |
| `position`        | `bottom-right`   | `bottom-right` or `bottom-left`.                                           |
| `label`           | `Chat`           | The button's accessible name.                                              |
| `color`           | `#ff5733`        | The button's hex color.                                                    |
| `open`            | `false`          | Start open.                                                                |
| `height`, `width` | `600px`, `400px` | The panel's size, css lengths.                                             |
| `version`         | this release's   | The version of `@smarter.sh/ui-chat` to load from jsDelivr, or a range.    |
| `src`             |                  | The url or path of a self-hosted `embed.js` (with its `embed/` beside it). |

An invalid option fails `docusaurus build`, with a message that names it. See the
[guide](https://docs.smarter.sh/en/latest/smarter-framework/smarter-docs-sites.html). License: AGPL-3.0-or-later.
