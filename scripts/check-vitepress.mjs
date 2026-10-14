/**
 * Checks the VitePress example's built pages for the embed script's tag, with test/expected-tag.json's "every option"
 * attributes, and the version of embed.json. `make test-vitepress` builds the example first. See
 * doc/adr/007-vitepress.md.
 */
import fs from "node:fs";
import path from "node:path";

const root = path.resolve(import.meta.dirname, "..");
const dist = path.join(root, "vitepress/example/docs/.vitepress/dist");
const expected = JSON.parse(fs.readFileSync(path.join(root, "test/expected-tag.json"), "utf-8")).cases.find(
  (testCase) => testCase.name === "every option",
).attributes;
const { version } = JSON.parse(fs.readFileSync(path.join(root, "embed.json"), "utf-8"));

/** The attributes of the page's embed script tags. */
function embedScripts(html) {
  return [...html.matchAll(/<script\b([^>]*)>/g)]
    .map(([, attributes]) =>
      Object.fromEntries(
        [...attributes.matchAll(/([\w-]+)(?:="([^"]*)")?/g)].map(([, name, value]) => [name, value ?? true]),
      ),
    )
    .filter((attributes) => String(attributes.src ?? "").endsWith("embed.js"))
    .map((attributes) => ({ ...attributes, async: "async" in attributes }));
}

let failures = 0;
for (const page of ["index.html", "guide.html"]) {
  const scripts = embedScripts(fs.readFileSync(path.join(dist, page), "utf-8"));
  const ok = scripts.length === 1 && JSON.stringify(scripts[0]) === JSON.stringify(expected);
  console.log(`${ok ? "ok:  " : "FAIL:"} ${page} ${ok ? "" : JSON.stringify(scripts)}`);
  if (!ok) failures++;
}
if (!expected.src.includes(`@${version}/`)) {
  console.log(`FAIL: the example's version is not embed.json's ${version}`);
  failures++;
}
process.exit(failures ? 1 : 0);
