// Render YouTube/Facebook thumbnails (HTML -> PNG/JPG) in the reference style.
// usage: node thumbs/render.mjs   (writes thumbs/out/*.jpg)
import fs from "node:fs";
import path from "node:path";
import { createRequire } from "node:module";

const require = createRequire(import.meta.url);
const { chromium } = require("playwright");
const ROOT = path.dirname(new URL(import.meta.url).pathname);
const V = path.resolve(ROOT, "../_vendor");
const u = (p) => "file://" + path.join(V, p);

const FEATURES = [
  ["logos/facebook", "ফেসবুক", "কাজ"],
  ["logos/youtube-icon", "ইউটিউব", "কাজ"],
  ["emoji/memo", "কনটেন্ট", "তৈরি"],
  ["emoji/chart-increasing", "ব্যবসার", "সহায়তা"],
  ["emoji/robot", "আরও", "অনেক কিছু"],
];

const css = `
@font-face { font-family: Anek; font-weight: 800; src: url(${u("fonts/anek-bangla-bengali-800-normal.woff2")}); }
@font-face { font-family: Anek; font-weight: 800; src: url(${u("fonts/anek-bangla-latin-800-normal.woff2")}); unicode-range: U+0000-00FF; }
@font-face { font-family: Baloo; font-weight: 800; src: url(${u("fonts/baloo-da-2-bengali-800-normal.woff2")}); }
@font-face { font-family: Poppins; font-weight: 900; src: url(${u("fonts/poppins-latin-900-normal.woff2")}); }
@font-face { font-family: Poppins; font-weight: 800; src: url(${u("fonts/poppins-latin-800-normal.woff2")}); }
* { margin: 0; padding: 0; box-sizing: border-box; }
body { width: var(--W); height: var(--H); overflow: hidden; font-family: Anek, Poppins, sans-serif; }
.stage { position: relative; width: 100%; height: 100%; overflow: hidden; background: #0b3fd1; }
.bgimg { position: absolute; inset: -40px; background-size: cover; background-position: center; filter: blur(14px) saturate(1.2); opacity: .55; }
.tint { position: absolute; inset: 0; background: radial-gradient(70% 90% at 30% 40%, rgba(120,190,255,.55) 0%, rgba(20,80,230,.75) 55%, rgba(8,30,140,.95) 100%); }
.rays { position: absolute; inset: 0; background: repeating-conic-gradient(from 0deg at 28% 45%, rgba(255,255,255,.07) 0deg 6deg, transparent 6deg 18deg); }
.person { position: absolute; bottom: 0; filter: drop-shadow(0 20px 40px rgba(0,0,30,.45)); }
.soft { -webkit-mask-image: linear-gradient(to right, #000 82%, transparent 100%), linear-gradient(to bottom, #000 80%, transparent 100%); -webkit-mask-composite: source-in; mask-composite: intersect; }
.brush { position: absolute; display: flex; align-items: center; justify-content: center; filter: drop-shadow(0 10px 18px rgba(0,0,0,.35)); }
.brush .bg { position: absolute; inset: 0; transform: skewX(-8deg); border-radius: 18px 60px 22px 70px; filter: url(#rough); }
.brush .tx { position: relative; color: #111; font-weight: 800; white-space: nowrap; letter-spacing: -0.01em; }
.yellow .bg { background: linear-gradient(180deg, #fff35a, #ffd400); }
.white .bg { background: linear-gradient(180deg, #ffffff, #f1f4ff); }
.tag { position: absolute; display: flex; align-items: center; justify-content: center; filter: drop-shadow(0 18px 30px rgba(80,0,0,.45)); }
.tag .shape { position: absolute; inset: 0; background: linear-gradient(180deg, #ff3b30, #c40d0d); clip-path: polygon(7% 0, 100% 0, 100% 100%, 7% 100%, 0 50%); border-radius: 26px; }
.tag .stitch { position: absolute; inset: 14px 14px 14px 9%; border: 3px dashed rgba(255,255,255,.55); border-radius: 18px; }
.tag .hole { position: absolute; left: 3.6%; top: 50%; width: 26px; height: 26px; margin-top: -13px; border-radius: 50%; background: #9fe7ff; box-shadow: inset 0 2px 4px rgba(0,0,0,.4); }
.gold { font-family: Anek; font-weight: 800; color: #ffe14d; background: linear-gradient(180deg, #fff9b0 0%, #ffd400 45%, #ff9f00 100%); -webkit-background-clip: text; background-clip: text; -webkit-text-fill-color: transparent; filter: drop-shadow(3px 0 0 #5a1a00) drop-shadow(-3px 0 0 #5a1a00) drop-shadow(0 3px 0 #5a1a00) drop-shadow(0 -3px 0 #5a1a00) drop-shadow(0 9px 0 #7a2200) drop-shadow(0 14px 18px rgba(0,0,0,.4)); line-height: 1; }
.wt { color: #fff; text-shadow: 2px 2px 0 #7a0000, -2px 2px 0 #7a0000, 2px -2px 0 #7a0000, -2px -2px 0 #7a0000, 0 6px 0 #7a0000, 0 10px 16px rgba(0,0,0,.35); line-height: 1; }
.red { color: #e3121a; }
.blue { color: #1238d6; }
.feat { position: absolute; display: flex; border-radius: 24px; background: linear-gradient(180deg, #121a33, #050913); border: 3px solid #ffb703; box-shadow: 0 16px 40px rgba(0,0,0,.45); }
.feat .f { flex: 1; display: flex; flex-direction: column; align-items: center; justify-content: center; color: #fff; text-align: center; line-height: 1.08; border-left: 2px solid #ffb703; }
.feat .f:first-child { border-left: none; }
.feat img { display: block; filter: drop-shadow(0 4px 8px rgba(0,0,0,.4)); }
.musecard { position: absolute; border-radius: 26px; background: linear-gradient(180deg, #fff35a, #ffcc00); border: 5px solid #ff2d2d; box-shadow: 0 16px 36px rgba(0,0,0,.4); display: flex; flex-direction: column; align-items: center; justify-content: center; }
.musecard .a { font-weight: 800; color: #111; white-space: nowrap; }
.musecard .b { font-family: Poppins; font-weight: 900; font-style: italic; color: #1238d6; line-height: 1; letter-spacing: -0.02em; }
.musecard .ul { height: 8px; border-radius: 4px; background: #ff2d2d; transform: rotate(-2deg); }
.metab { position: absolute; display: flex; flex-direction: column; align-items: center; padding: 14px 22px; border-radius: 22px; background: rgba(255,255,255,.92); box-shadow: 0 10px 26px rgba(0,0,0,.25); font-family: Poppins; font-weight: 800; color: #1c2b4a; }
.spark { position: absolute; width: 90px; height: 14px; border-radius: 7px; background: #ffd400; box-shadow: 0 4px 8px rgba(0,0,0,.25); }
`;
const svgFilter = `<svg width="0" height="0" style="position:absolute"><filter id="rough"><feTurbulence type="fractalNoise" baseFrequency="0.035" numOctaves="2" seed="7"/><feDisplacementMap in="SourceGraphic" scale="14"/></filter></svg>`;
const feat = (sz, fs) =>
  FEATURES.map(([ic, a, b]) => `<div class="f"><img src="${u("icons/" + ic + ".svg")}" style="width:${sz}px;height:${sz}px;margin-bottom:8px" /><div style="font-size:${fs}px;font-weight:800">${a}</div><div style="font-size:${fs}px;font-weight:800">${b}</div></div>`).join("");

function landscape(s) {
  return `<div class="stage">
  <div class="bgimg" style="background-image:url(${u("media/" + s.bg)})"></div><div class="tint"></div><div class="rays"></div>
  <div class="metab" style="left:46px;top:40px"><img src="${u("icons/logos/meta-icon.svg")}" style="width:150px" /><div style="font-size:40px;margin-top:-4px">Meta</div></div>
  <img class="person ${s.soft ? "soft" : ""}" src="${u("media/" + s.person)}" style="${s.personStyle}" />
  <div class="brush yellow" style="left:${s.x}px;top:36px;width:${s.w}px;height:150px"><div class="bg"></div><div class="tx" style="font-size:${s.h1size || 92}px">${s.h1}</div></div>
  <div class="spark" style="left:${s.x - 40}px;top:120px;transform:rotate(-35deg)"></div>
  <div class="tag" style="left:${s.x + 10}px;top:200px;width:${s.w - 20}px;height:330px">
    <div class="shape"></div><div class="stitch"></div><div class="hole"></div>
    <div style="position:relative;display:flex;align-items:center;gap:16px;margin-left:40px">
      <div style="display:flex;flex-direction:column;align-items:center"><div class="wt" style="font-size:72px;margin-bottom:6px">মাত্র</div><div class="gold" style="font-size:225px">২৪৯</div></div>
      <div class="wt" style="font-size:96px;margin-top:110px">টাকায়</div>
    </div>
  </div>
  <div class="brush white" style="left:${s.x + 30}px;top:560px;width:${s.w - 60}px;height:250px"><div class="bg"></div>
    <div class="tx" style="display:flex;flex-direction:column;align-items:center;line-height:1.05">
      <div style="font-size:78px">সাথে পাবেন</div>
      <div style="display:flex;align-items:baseline;gap:18px"><span class="red" style="font-family:Poppins;font-weight:900;font-size:150px;line-height:.9">1</span><span class="blue" style="font-size:118px">বিলিয়ন</span><span class="blue" style="font-family:Poppins;font-weight:800;font-size:84px">token</span></div>
    </div></div>
  <div class="spark" style="left:${s.x + s.w - 30}px;top:600px;transform:rotate(40deg)"></div>
  <div class="feat" style="left:${s.x - 10}px;top:850px;width:${s.w + 20}px;height:200px">${feat(78, 32)}</div>
  <div class="musecard" style="left:40px;top:760px;width:640px;height:270px;transform:rotate(-2deg)">
    <div class="a" style="font-size:56px">Meta-এর AI এজেন্ট</div><div class="b" style="font-size:150px">Muse</div><div class="ul" style="width:420px"></div>
  </div>
</div>`;
}

function portrait(s) {
  return `<div class="stage">
  <div class="bgimg" style="background-image:url(${u("media/" + s.bg)})"></div><div class="tint"></div><div class="rays"></div>
  <div class="brush yellow" style="left:60px;top:150px;width:960px;height:170px"><div class="bg"></div><div class="tx" style="font-size:88px">${s.h1}</div></div>
  <div style="position:absolute;left:0;right:0;top:340px;text-align:center"><span class="gold" style="font-size:180px">${s.h2}</span></div>
  <img class="person ${s.soft ? "soft" : ""}" src="${u("media/" + s.person)}" style="${s.personStyle}" />
  <div class="metab" style="right:40px;top:560px"><img src="${u("icons/logos/meta-icon.svg")}" style="width:130px" /><div style="font-size:34px;margin-top:-4px">Meta</div></div>
  <div class="tag" style="left:70px;top:1080px;width:940px;height:300px">
    <div class="shape"></div><div class="stitch"></div><div class="hole"></div>
    <div style="position:relative;display:flex;align-items:center;gap:22px;margin-left:40px">
      <div style="display:flex;flex-direction:column;align-items:center"><div class="wt" style="font-size:70px;margin-bottom:6px">মাত্র</div><div class="gold" style="font-size:215px">২৪৯</div></div>
      <div class="wt" style="font-size:96px;margin-top:100px">টাকায়</div>
    </div>
  </div>
  <div class="brush white" style="left:90px;top:1410px;width:900px;height:220px"><div class="bg"></div>
    <div class="tx" style="display:flex;flex-direction:column;align-items:center;line-height:1.05">
      <div style="font-size:66px">সাথে পাবেন</div>
      <div style="display:flex;align-items:baseline;gap:16px"><span class="red" style="font-family:Poppins;font-weight:900;font-size:130px;line-height:.9">1</span><span class="blue" style="font-size:104px">বিলিয়ন</span><span class="blue" style="font-family:Poppins;font-weight:800;font-size:74px">token</span></div>
    </div></div>
  <div class="feat" style="left:50px;top:1670px;width:980px;height:190px">${feat(70, 30)}</div>
</div>`;
}

const SPECS = [
  {
    id: "v01-thumb", W: 1920, H: 1080, kind: landscape, bg: "sabbir-muse-thumb.png", person: "cut-sabbir-muse-c.png",
    personStyle: "left:-250px;height:900px;bottom:0", x: 1060, w: 820, h1: "নিজে আর কাজ করতে হবে না!", h1size: 62,
  },
  {
    id: "v02-cover", W: 1080, H: 1920, kind: portrait, bg: "sabbir-muse-thumb.png", person: "cut-sabbir-pointing-c.png",
    soft: true, personStyle: "left:90px;height:640px;top:470px;bottom:auto", h1: "২৪ ঘণ্টা কাজ করবে", h2: "AI কর্মী",
  },
  {
    id: "v02-thumb", W: 1920, H: 1080, kind: landscape, bg: "thumb-ref-pointing.png", person: "cut-sabbir-pointing-c.png",
    soft: true, personStyle: "left:20px;height:960px;bottom:auto;top:110px", x: 1060, w: 820, h1: "২৪ ঘণ্টার AI কর্মী!", h1size: 84,
  },
];

const out = path.join(ROOT, "out");
fs.mkdirSync(out, { recursive: true });
const browser = await chromium.launch();
const only = process.argv.slice(2);
for (const s of SPECS) {
  if (only.length && !only.includes(s.id)) continue;
  const page = await browser.newPage({ viewport: { width: s.W, height: s.H } });
  const html = `<!doctype html><html><head><meta charset="utf-8"><style>:root{--W:${s.W}px;--H:${s.H}px}${css}</style></head><body>${svgFilter}${s.kind(s)}</body></html>`;
  const f = path.join(out, s.id + ".html");
  fs.writeFileSync(f, html);
  await page.goto("file://" + f);
  await page.evaluate(() => document.fonts.ready);
  await page.waitForTimeout(400);
  await page.screenshot({ path: path.join(out, s.id + ".png") });
  await page.close();
  console.log("wrote", s.id);
}
await browser.close();
