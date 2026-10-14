/**
 * @smarter.sh/docusaurus-plugin-smarter-chat: adds the chat launcher of @smarter.sh/ui-chat's embed script to every
 * page of a Docusaurus site, with one tag before `</body>`. See ../doc/adr/004-docusaurus.md.
 *
 * ```js
 * // docusaurus.config.js
 * plugins: [["@smarter.sh/docusaurus-plugin-smarter-chat", { chatbot: "https://docs-bot.example.com/" }]],
 * ```
 */

/** The version of the embed script that this release is tested with. Copied from ../embed.json. */
export const EMBED_VERSION = "0.9.0";

/** The launcher's corners. */
export const POSITIONS = ["bottom-right", "bottom-left"];

const HTTP_URL = /^https?:\/\/[^\s"'<>`]+$/i;
const HEX_COLOR = /^#([0-9a-f]{3}|[0-9a-f]{6})$/i;
const CSS_LENGTH = /^\d{1,5}(\.\d{1,3})?(px|em|rem|vh|vw|svh|dvh|%)$/;
const VERSION = /^\d+(\.\d+){0,2}(-[0-9A-Za-z.]+)?$/;
const SCRIPT_SRC = /^(https?:\/\/|\/)[^\s"'<>`]*$/i;

/** The options that become data- attributes, by option name. */
const DATA_ATTRIBUTES = {
  chatbot: "data-chatbot",
  apiKey: "data-api-key",
  position: "data-position",
  label: "data-label",
  color: "data-color",
  open: "data-open",
  height: "data-height",
  width: "data-width",
};

/**
 * Checks the plugin's options, and fails the build with a message that names the option.
 *
 * @param {Partial<import("./index.js").SmarterChatOptions>} [options] The options from docusaurus.config.js.
 * @returns {import("./index.js").SmarterChatOptions} The options.
 * @throws {Error} If an option is invalid.
 */
export function checkOptions(options = {}) {
  /** @param {string} message */
  const fail = (message) => {
    throw new Error(`docusaurus-plugin-smarter-chat: ${message}`);
  };
  if (typeof options.chatbot !== "string" || !HTTP_URL.test(options.chatbot)) {
    fail(`"chatbot" must be the http(s) url of a deployed LLMClient, not ${JSON.stringify(options.chatbot)}.`);
  }
  if (options.position !== undefined && !POSITIONS.includes(options.position)) {
    fail(`"position" must be one of ${POSITIONS.join(", ")}.`);
  }
  if (options.color !== undefined && !HEX_COLOR.test(options.color)) fail(`"color" must be a hex color, e.g. #ff5733.`);
  for (const name of /** @type {const} */ (["height", "width"])) {
    if (options[name] !== undefined && !CSS_LENGTH.test(options[name]))
      fail(`"${name}" must be a css length, e.g. 600px.`);
  }
  if (options.version !== undefined && !VERSION.test(options.version)) fail(`"version" must be a version, e.g. 0.9.0.`);
  if (options.src !== undefined && !SCRIPT_SRC.test(options.src)) fail(`"src" must be an http(s) url or a path.`);
  if (options.open !== undefined && typeof options.open !== "boolean") fail(`"open" must be true or false.`);
  return /** @type {import("./index.js").SmarterChatOptions} */ (options);
}

/**
 * The embed script tag's attributes: its src, the options that are set, as data- attributes, and async.
 *
 * @param {import("./index.js").SmarterChatOptions} options The options.
 * @returns {Record<string, string | boolean>} The attributes, which Docusaurus escapes.
 */
export function scriptAttributes(options) {
  const version = options.version ?? EMBED_VERSION;
  /** @type {Record<string, string | boolean>} */
  const attributes = {
    src: options.src ?? `https://cdn.jsdelivr.net/npm/@smarter.sh/ui-chat@${version}/dist/embed.js`,
  };
  for (const [name, attribute] of Object.entries(DATA_ATTRIBUTES)) {
    const value = /** @type {Record<string, unknown>} */ (/** @type {unknown} */ (options))[name];
    if (value === undefined || value === null || value === "" || value === false) continue;
    attributes[attribute] = String(value);
  }
  attributes.async = true;
  return attributes;
}

/**
 * The plugin.
 *
 * @param {unknown} _context Docusaurus's context, which the plugin doesn't need.
 * @param {import("./index.js").SmarterChatOptions} options The options from docusaurus.config.js.
 * @returns {import("./index.js").SmarterChatPlugin} The plugin.
 */
export default function pluginSmarterChat(_context, options) {
  return {
    name: "docusaurus-plugin-smarter-chat",
    injectHtmlTags() {
      return { postBodyTags: [{ tagName: "script", attributes: scriptAttributes(options) }] };
    },
  };
}

/**
 * Docusaurus's options validation hook, which runs before the build.
 *
 * @param {{ options: import("./index.js").SmarterChatOptions }} args Docusaurus's arguments.
 * @returns {import("./index.js").SmarterChatOptions} The options.
 */
export function validateOptions({ options }) {
  return checkOptions(options);
}
