// Assemble each vNN/src.html into a renderable HyperFrames project (vNN/index.html + assets)
// usage: node build.mjs [v01 v02 ...]
import fs from "node:fs";
import path from "node:path";
import { execFileSync } from "node:child_process";

const ROOT = path.dirname(new URL(import.meta.url).pathname);
const V = path.join(ROOT, "_vendor");
const brand = fs.readFileSync(path.join(V, "brand.css"), "utf8");
const helpers = fs.readFileSync(path.join(V, "helpers.js"), "utf8");
const durCache = {};
const sfxDur = (name) =>
  (durCache[name] ??= Number(
    execFileSync("ffprobe", [
      "-v",
      "error",
      "-show_entries",
      "format=duration",
      "-of",
      "csv=p=0",
      path.join(V, "sfx", name + ".mp3"),
    ])
      .toString()
      .trim(),
  ));

function section(src, name) {
  const m = src.match(new RegExp(`<!--${name}-->([\\s\\S]*?)(?=<!--[a-z]+-->|$)`));
  return m ? m[1].trim() : "";
}

function build(dir) {
  const p = path.join(ROOT, dir);
  const src = fs.readFileSync(path.join(p, "src.html"), "utf8");
  const meta = JSON.parse(src.match(/<!--meta([\s\S]*?)-->/)[1]);
  const { w, h, dur, title } = meta;
  const css = section(src, "style");
  const body = section(src, "body");
  const script = section(src, "script");
  const mod = section(src, "module");
  const audio = (meta.sfx || [])
    .map(([name, t, vol = 0.7, len, ms = 0], i) => {
      const d = Math.min(len ?? sfxDur(name), sfxDur(name) - ms, dur - t).toFixed(3);
      return `<audio id="sfx${i}" class="clip" src="assets/sfx/${name}.mp3" data-start="${t}" data-duration="${d}"${ms ? ` data-media-start="${ms}"` : ""} data-track-index="${20 + (i % 6)}" data-volume="${vol}"></audio>`;
    })
    .join("\n");
  const vo = meta.vo
    ? `<audio id="vo" class="clip" src="assets/media/${meta.vo}" data-start="${meta.voStart ?? 0}" data-duration="${meta.voDur}" data-track-index="31" data-volume="1"></audio>`
    : "";
  const music = meta.music
    ? `<audio id="bgm" class="clip" src="assets/${meta.music}" data-start="0" data-duration="${dur}" data-track-index="30" data-volume="${meta.musicVol ?? 0.35}"></audio>`
    : "";
  const html = `<!doctype html>
<html lang="bn" data-theme="${process.env.THEME || meta.theme || "clean"}">
  <head>
    <meta charset="UTF-8" />
    <meta name="viewport" content="width=${w}, height=${h}" />
    <title>${title}</title>
    <script src="assets/lib/gsap.min.js"></script>
    <script type="importmap">{"imports":{"three":"./assets/lib/three.module.js","three/addons/":"./assets/lib/jsm/"}}</script>
    <style>
${brand}
html, body { width: ${w}px; height: ${h}px; }
${css}
    </style>
  </head>
  <body>
    <div id="root" data-composition-id="main" data-start="0" data-duration="${dur}" data-width="${w}" data-height="${h}">
${body}
${audio}
${music}
${vo}
    </div>
    <script>
${helpers}
var W = ${w}, H = ${h}, DUR = ${dur};
const tl = gsap.timeline({ paused: true });
${script}
window.__timelines["main"] = tl;
tl.seek(0);
    </script>
${mod ? `    <script type="module">\nimport { mount3D } from "./assets/sr3d.js";\n${mod}\n    </script>` : ""}
  </body>
</html>
`;
  fs.writeFileSync(path.join(p, "index.html"), html);
  const a = path.join(p, "assets");
  fs.mkdirSync(a, { recursive: true });
  for (const sub of ["lib", "fonts"])
    fs.cpSync(path.join(V, sub), path.join(a, sub), { recursive: true });
  fs.mkdirSync(path.join(a, "sfx"), { recursive: true });
  for (const [name] of meta.sfx || [])
    fs.copyFileSync(path.join(V, "sfx", name + ".mp3"), path.join(a, "sfx", name + ".mp3"));
  for (const f of ["sr3d.js", "dhaka.js", "logo-mark.png", "logo-mark-t.png", "logo-full.png"])
    fs.copyFileSync(path.join(V, f), path.join(a, f));
  fs.mkdirSync(path.join(a, "media"), { recursive: true });
  for (const f of [...(meta.media || []), ...(meta.vo ? [meta.vo] : [])])
    fs.copyFileSync(path.join(V, "media", f), path.join(a, "media", f));
  for (const [, set, name] of src.matchAll(/icons\/(logos|emoji|flat)\/([\w-]+)\.svg/g)) {
    fs.mkdirSync(path.join(a, "icons", set), { recursive: true });
    fs.copyFileSync(
      path.join(V, "icons", set, name + ".svg"),
      path.join(a, "icons", set, name + ".svg"),
    );
  }
  if (meta.music) fs.copyFileSync(path.join(V, meta.music), path.join(a, meta.music));
  if (!fs.existsSync(path.join(p, "hyperframes.json")))
    fs.writeFileSync(
      path.join(p, "hyperframes.json"),
      JSON.stringify(
        {
          paths: {
            blocks: "compositions",
            components: "compositions/components",
            assets: "assets",
          },
        },
        null,
        2,
      ),
    );
  console.log("built", dir, `${w}x${h}`, dur + "s");
}

const dirs = process.argv.slice(2).length
  ? process.argv.slice(2)
  : fs
      .readdirSync(ROOT)
      .filter((d) => /^v\d\d$/.test(d))
      .sort();
dirs.forEach(build);
