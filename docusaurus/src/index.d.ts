/** The plugin's options: the embed script's launcher options, and where to load it from. */
export interface SmarterChatOptions {
  /** The url of the deployed LLMClient, e.g. https://docs-bot.example.com/. Required. */
  chatbot: string;
  /** A Smarter api key, for LLMClients that require one. It is public in the pages. */
  apiKey?: string;
  /** The launcher's corner. Default: bottom-right. */
  position?: "bottom-right" | "bottom-left";
  /** The launcher's accessible name. Default: Chat. */
  label?: string;
  /** The launcher button's hex color. Default: #ff5733. */
  color?: string;
  /** Whether the launcher starts open. Default: false. */
  open?: boolean;
  /** The launcher panel's height, a css length. Default: 600px. */
  height?: string;
  /** The launcher panel's width, a css length. Default: 400px. */
  width?: string;
  /** The version of @smarter.sh/ui-chat to load from jsDelivr, or a range such as 0.9. */
  version?: string;
  /** The url or path of a self-hosted embed.js, with its embed/ directory beside it. */
  src?: string;
}

/** A Docusaurus html tag. */
export interface HtmlTag {
  tagName: string;
  attributes: Record<string, string | boolean>;
}

/** The plugin's lifecycle methods. */
export interface SmarterChatPlugin {
  name: string;
  injectHtmlTags(): { postBodyTags: HtmlTag[] };
}

/** The version of the embed script that this release is tested with. */
export declare const EMBED_VERSION: string;
/** The launcher's corners. */
export declare const POSITIONS: readonly ["bottom-right", "bottom-left"];
/** Checks the options, and throws an Error that names an invalid one. */
export declare function checkOptions(options?: Partial<SmarterChatOptions>): SmarterChatOptions;
/** The embed script tag's attributes. */
export declare function scriptAttributes(options: SmarterChatOptions): Record<string, string | boolean>;
/** The plugin. */
export default function pluginSmarterChat(context: unknown, options: SmarterChatOptions): SmarterChatPlugin;
/** Docusaurus's options validation hook. */
export declare function validateOptions(args: { options: SmarterChatOptions }): SmarterChatOptions;
