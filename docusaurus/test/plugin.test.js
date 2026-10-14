import fs from "node:fs";
import path from "node:path";
import { describe, expect, it } from "vitest";

import pluginSmarterChat, { EMBED_VERSION, checkOptions, scriptAttributes, validateOptions } from "../src/index.js";

const ROOT = path.resolve(import.meta.dirname, "../..");
const expected = JSON.parse(fs.readFileSync(path.join(ROOT, "test/expected-tag.json"), "utf-8"));
const embed = JSON.parse(fs.readFileSync(path.join(ROOT, "embed.json"), "utf-8"));

describe("the Docusaurus plugin", () => {
  it.each(expected.cases.map((testCase) => [testCase.name, testCase]))(
    "writes the expected tag: %s",
    (_name, testCase) => {
      const plugin = pluginSmarterChat({}, validateOptions({ options: testCase.options }));
      expect(plugin.name).toBe("docusaurus-plugin-smarter-chat");
      expect(plugin.injectHtmlTags()).toEqual({
        postBodyTags: [{ tagName: "script", attributes: testCase.attributes }],
      });
    },
  );

  it.each(expected.invalid.map((testCase) => [testCase.name, testCase]))("fails the build: %s", (_name, testCase) => {
    expect(() => validateOptions({ options: testCase.options })).toThrow(/^docusaurus-plugin-smarter-chat: "/);
  });

  it("checks every typed option", () => {
    const chatbot = "https://docs-bot.example.com/";
    expect(() => checkOptions()).toThrow(/"chatbot"/);
    expect(() => checkOptions({ chatbot, height: "tall" })).toThrow(/"height"/);
    expect(() => checkOptions({ chatbot, width: "1px;x" })).toThrow(/"width"/);
    expect(() => checkOptions({ chatbot, open: "yes" })).toThrow(/"open"/);
    expect(checkOptions({ chatbot, open: false })).toEqual({ chatbot, open: false });
  });

  it("leaves out options that are empty, false or null", () => {
    const attributes = scriptAttributes({
      chatbot: "https://docs-bot.example.com/",
      apiKey: "",
      open: false,
      label: null,
    });
    expect(Object.keys(attributes)).toEqual(["src", "data-chatbot", "async"]);
  });

  it("loads the embed version of embed.json", () => {
    expect(EMBED_VERSION).toBe(embed.version);
  });
});
