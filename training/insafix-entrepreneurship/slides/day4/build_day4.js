const pptxgen = require("pptxgenjs");
const sharp = require("sharp");
const React = require("react");
const ReactDOMServer = require("react-dom/server");
const fa = require("react-icons/fa");

const OUT = process.argv[2] || "Day04_Allergy_Clean.pptx";
const ASSET = "/home/user/hyperframes/training/insafix-entrepreneurship";
const IMG = {
  product: ASSET + "/slides/day4/assets/allergy-clean.jpg",
  alinsaf: ASSET + "/assets/al-insaf-life-care-logo.jpg",
  insafix: ASSET + "/assets/insafix-academy-logo.jpg",
};
const FONT = "Nirmala UI";
const C = {
  dark: "12352A",
  green: "1F7A42",
  green2: "2E9E5B",
  greenTxt: "1F8A4C",
  lime: "A6D65A",
  light: "F6F7F0",
  light2: "EEF5EA",
  white: "FFFFFF",
  muted: "4A6358",
  border: "DCE6D6",
  orange: "F28C28",
  orangeTxt: "B85A0C",
  orangeSoft: "FFF1E0",
  orangeLine: "F6D2A8",
  brown: "5A3510",
  brownDark: "3A1E05",
  sand: "F6B26B",
  paleGreen: "D7F0C2",
  mutedDark: "9DB8AA",
};

// 1920x1080 design grid -> 13.333x7.5 in
const P = (px) => px / 144;
const F = (px) => px * 0.5;

async function svgPng(svg, w, h) {
  const buf = await sharp(Buffer.from(svg)).resize(w, h).png().toBuffer();
  return "image/png;base64," + buf.toString("base64");
}
async function iconPng(Comp, color) {
  const svg = ReactDOMServer.renderToStaticMarkup(
    React.createElement(Comp, { color: "#" + color, size: 256 }),
  );
  return svgPng(svg, 256, 256);
}

const WAVES = `<path d="M0 960 C 400 860, 780 1060, 1200 960 S 1720 830, 1920 890" fill="none" stroke="url(#w1)" stroke-width="5"/><path d="M0 1000 C 430 900, 800 1080, 1220 990 S 1730 870, 1920 930" fill="none" stroke="url(#w2)" stroke-width="3" opacity="0.9"/><path d="M0 1035 C 460 950, 830 1100, 1240 1025 S 1750 915, 1920 965" fill="none" stroke="url(#w1)" stroke-width="2" opacity="0.5"/>`;
const GRADS = `<linearGradient id="w1" x1="0" y1="0" x2="1" y2="0"><stop offset="0" stop-color="#FFD3A1" stop-opacity="0"/><stop offset="0.45" stop-color="#F28C28"/><stop offset="1" stop-color="#D9731A"/></linearGradient><linearGradient id="w2" x1="0" y1="0" x2="1" y2="0"><stop offset="0" stop-color="#8DC63F" stop-opacity="0"/><stop offset="0.5" stop-color="#8DC63F"/><stop offset="1" stop-color="#2E9E5B"/></linearGradient>`;
const SVG = {
  cover: `<svg xmlns="http://www.w3.org/2000/svg" width="1920" height="1080" viewBox="0 0 1920 1080"><defs><radialGradient id="g" cx="78%" cy="38%" r="60%"><stop offset="0" stop-color="#FFFFFF"/><stop offset="0.55" stop-color="#F6F7F0"/><stop offset="1" stop-color="#E7F0E1"/></radialGradient>${GRADS}</defs><rect width="1920" height="1080" fill="url(#g)"/><path d="M0 930 C 420 820, 760 1040, 1180 930 S 1700 800, 1920 860 L1920 1080 L0 1080 Z" fill="#DCEBD3" opacity="0.8"/>${WAVES}<circle cx="1580" cy="470" r="330" fill="none" stroke="#2E9E5B" stroke-opacity="0.18" stroke-width="2"/><circle cx="1580" cy="470" r="390" fill="none" stroke="#F28C28" stroke-opacity="0.2" stroke-width="2" stroke-dasharray="6 14"/></svg>`,
  soft: `<svg xmlns="http://www.w3.org/2000/svg" width="1920" height="1080" viewBox="0 0 1920 1080"><defs><radialGradient id="g" cx="50%" cy="40%" r="65%"><stop offset="0" stop-color="#FFFFFF"/><stop offset="0.6" stop-color="#F6F7F0"/><stop offset="1" stop-color="#E7F0E1"/></radialGradient>${GRADS}</defs><rect width="1920" height="1080" fill="url(#g)"/>${WAVES}</svg>`,
  light: (bg) =>
    `<svg xmlns="http://www.w3.org/2000/svg" width="1920" height="1080" viewBox="0 0 1920 1080"><rect width="1920" height="1080" fill="#${bg}"/><path d="M0 1050 C 480 1020, 960 1080, 1440 1045 S 1800 1030, 1920 1042" fill="none" stroke="#F28C28" stroke-width="3" opacity="0.6"/><path d="M0 1065 C 480 1035, 960 1095, 1440 1060 S 1800 1045, 1920 1057" fill="none" stroke="#8DC63F" stroke-width="2" opacity="0.6"/></svg>`,
  dark: `<svg xmlns="http://www.w3.org/2000/svg" width="1920" height="1080" viewBox="0 0 1920 1080"><defs><radialGradient id="g" cx="50%" cy="45%" r="70%"><stop offset="0" stop-color="#1F6B45"/><stop offset="0.6" stop-color="#12352A"/><stop offset="1" stop-color="#0C261D"/></radialGradient>${GRADS}</defs><rect width="1920" height="1080" fill="url(#g)"/><path d="M0 980 C 400 900, 780 1060, 1200 985 S 1720 880, 1920 920" fill="none" stroke="url(#w1)" stroke-width="4"/><path d="M0 1015 C 430 935, 800 1090, 1220 1015 S 1730 910, 1920 950" fill="none" stroke="url(#w2)" stroke-width="3" opacity="0.85"/></svg>`,
};

(async () => {
  const pres = new pptxgen();
  pres.layout = "LAYOUT_WIDE";
  pres.title = "চতুর্থ দিন — এলার্জি সমস্যা ও Allergy Clean";
  pres.author = "Al-Insaf Life Care";
  pres.theme = { headFontFace: FONT, bodyFontFace: FONT };

  const BG = {
    cover: await svgPng(SVG.cover, 1920, 1080),
    soft: await svgPng(SVG.soft, 1920, 1080),
    light: await svgPng(SVG.light(C.light), 1920, 1080),
    light2: await svgPng(SVG.light(C.light2), 1920, 1080),
    dark: await svgPng(SVG.dark, 1920, 1080),
  };
  const iconCache = {};
  const ico = async (name, color) => {
    const k = name + color;
    if (!iconCache[k]) iconCache[k] = await iconPng(fa[name], color);
    return iconCache[k];
  };

  // ---------- helpers (px in, design grid 1920x1080) ----------
  const T = (s, text, o) => {
    s.addText(text, {
      x: P(o.x),
      y: P(o.y),
      w: P(o.w),
      h: P(o.h),
      isTextBox: true,
      margin: 0,
      fontFace: FONT,
      fontSize: F(o.size || 28),
      color: o.color || C.dark,
      bold: !!o.bold,
      align: o.align || "left",
      valign: o.valign || "top",
      lineSpacingMultiple: o.ls || 1.15,
      charSpacing: o.cs,
      objectName: o.name,
      fit: "none",
    });
  };
  const R = (s, o) => {
    s.addShape(o.radius === 0 ? pres.shapes.RECTANGLE : pres.shapes.ROUNDED_RECTANGLE, {
      x: P(o.x),
      y: P(o.y),
      w: P(o.w),
      h: P(o.h),
      fill: { color: o.fill || C.white, transparency: o.transp || 0 },
      line: o.line
        ? { color: o.line, width: o.lw || 1, dashType: o.dash || "solid" }
        : { type: "none" },
      rectRadius:
        o.radius === 0 ? undefined : Math.min(0.5, P(o.radius || 24) / Math.min(P(o.w), P(o.h))),
      shadow: o.shadow
        ? { type: "outer", color: "12352A", opacity: 0.12, blur: 12, offset: 4, angle: 90 }
        : undefined,
      objectName: o.name,
    });
  };
  const O = (s, o) => {
    s.addShape(pres.shapes.OVAL, {
      x: P(o.x),
      y: P(o.y),
      w: P(o.d),
      h: P(o.d),
      fill: { color: o.fill },
      line: o.line ? { color: o.line, width: o.lw || 1 } : { type: "none" },
      objectName: o.name,
    });
  };
  const I = async (s, name, color, x, y, size, circleFill, pad) => {
    if (circleFill) O(s, { x, y, d: size, fill: circleFill });
    const p = pad == null ? size * 0.22 : pad;
    s.addImage({
      data: await ico(name, color),
      x: P(x + p),
      y: P(y + p),
      w: P(size - 2 * p),
      h: P(size - 2 * p),
    });
  };
  const ARROW = (s, x, y, w, h, color) => {
    s.addShape(pres.shapes.RIGHT_ARROW, {
      x: P(x),
      y: P(y),
      w: P(w),
      h: P(h),
      fill: { color: color || C.orange },
      line: { type: "none" },
    });
  };
  const bg = (s, k) => s.addImage({ data: BG[k], x: 0, y: 0, w: 13.333, h: 7.5 });
  const header = (s, eyebrow, a, b) => {
    T(s, eyebrow, {
      x: 128,
      y: 112,
      w: 1200,
      h: 36,
      size: 24,
      bold: true,
      color: C.orangeTxt,
      cs: 2,
    });
    T(
      s,
      [
        { text: a + " ", options: { color: C.dark } },
        { text: b, options: { color: C.greenTxt } },
      ],
      { x: 128, y: 156, w: 1664, h: 100, size: 72, bold: true, ls: 1.0 },
    );
  };
  const footer = (s, n, dark) => {
    if (!dark)
      T(s, "Al-Insaf Life Care · ইনসাফের সঙ্গে সেবার প্রতিশ্রুতি", {
        x: 128,
        y: 982,
        w: 1000,
        h: 36,
        size: 24,
        bold: true,
        color: C.muted,
      });
    T(s, n, {
      x: 1592,
      y: 982,
      w: 200,
      h: 36,
      size: 24,
      bold: true,
      color: dark ? C.mutedDark : C.green,
      align: "right",
    });
  };

  // ---------- 1 cover ----------
  let s = pres.addSlide();
  bg(s, "cover");
  R(s, { x: 128, y: 88, w: 290, h: 104, radius: 20, line: C.border, shadow: true });
  s.addImage({
    path: IMG.alinsaf,
    x: P(146),
    y: P(100),
    w: P(62),
    h: P(80),
    sizing: { type: "contain", w: P(62), h: P(80) },
  });
  T(
    s,
    [
      { text: "Al-Insaf", options: { breakLine: true } },
      { text: "Life Care", options: { color: "C2620A" } },
    ],
    { x: 222, y: 104, w: 180, h: 72, size: 26, bold: true, color: "0E3B2C", valign: "middle" },
  );
  s.addShape(pres.shapes.LINE, {
    x: P(436),
    y: P(140),
    w: P(36),
    h: 0,
    line: { color: C.orange, width: 2 },
  });
  R(s, { x: 490, y: 88, w: 300, h: 104, radius: 20, line: C.border, shadow: true });
  s.addImage({ path: IMG.insafix, x: P(504), y: P(100), w: P(80), h: P(80) });
  T(
    s,
    [
      { text: "Insafix", options: { breakLine: true } },
      { text: "Academy", options: { color: "1597B8" } },
    ],
    { x: 596, y: 104, w: 180, h: 72, size: 26, bold: true, color: "0E3B2C", valign: "middle" },
  );
  R(s, { x: 128, y: 330, w: 176, h: 56, radius: 28, fill: C.orange });
  T(s, "DAY 04", {
    x: 128,
    y: 330,
    w: 176,
    h: 56,
    size: 30,
    bold: true,
    color: C.brownDark,
    align: "center",
    valign: "middle",
    cs: 2,
  });
  T(s, "Allergy Problem & Allergy Clean", {
    x: 326,
    y: 336,
    w: 900,
    h: 44,
    size: 30,
    bold: true,
    color: C.muted,
    valign: "middle",
  });
  T(
    s,
    [
      { text: "এলার্জি সমস্যা ও", options: { breakLine: true } },
      { text: "এলার্জি ক্লিন", options: { color: C.greenTxt } },
    ],
    { x: 128, y: 420, w: 1180, h: 300, size: 104, bold: true, ls: 1.05 },
  );
  R(s, { x: 128, y: 800, w: 1120, h: 80, radius: 40, line: "CFE0C6", shadow: true });
  await I(s, "FaGraduationCap", C.green2, 158, 818, 44, null, 0);
  T(
    s,
    [
      { text: "Al Insaf Life Care", options: { bold: true, color: C.green } },
      { text: "  |  Entrepreneur Training Program", options: {} },
    ],
    { x: 220, y: 800, w: 1000, h: 80, size: 30, valign: "middle" },
  );
  O(s, { x: 1370, y: 260, d: 420, fill: C.white, line: C.green2, lw: 4.5 });
  T(s, "DAY", { x: 1370, y: 320, w: 420, h: 70, size: 56, bold: true, align: "center", cs: 6 });
  T(s, "০৪", {
    x: 1370,
    y: 380,
    w: 420,
    h: 200,
    size: 190,
    bold: true,
    color: C.greenTxt,
    align: "center",
    valign: "middle",
    ls: 1.0,
  });
  T(s, "Allergy Clean", {
    x: 1370,
    y: 580,
    w: 420,
    h: 44,
    size: 28,
    bold: true,
    color: C.orangeTxt,
    align: "center",
  });
  s.addNotes("আজকের বিষয়: এলার্জি সমস্যা ও এলার্জি ক্লিন।");

  // ---------- 2 what ----------
  s = pres.addSlide();
  bg(s, "light2");
  header(s, "WHAT IS ALLERGY", "এলার্জি কী?", "Allergy কী?");
  const what = [
    ["FaHeartbeat", "শরীরের অতিরিক্ত প্রতিক্রিয়া"],
    ["FaExclamationTriangle", "ধুলা, খাবার, আবহাওয়া ইত্যাদিতে সমস্যা"],
  ];
  for (let i = 0; i < 2; i++) {
    const x = 128 + i * 846;
    R(s, { x, y: 330, w: 818, h: 170, line: C.border });
    await I(s, what[i][0], C.white, x + 40, 375, 84, C.green2);
    T(s, what[i][1], {
      x: x + 150,
      y: 345,
      w: 640,
      h: 140,
      size: 36,
      bold: true,
      valign: "middle",
    });
  }
  R(s, { x: 128, y: 580, w: 1664, h: 300, radius: 28, fill: C.green });
  T(s, "“", { x: 176, y: 600, w: 120, h: 140, size: 140, bold: true, color: C.sand });
  T(s, "এলার্জি হলো শরীরের এমন একটি প্রতিক্রিয়া, যেখানে শরীর কিছু জিনিস সহ্য করতে পারে না।", {
    x: 310,
    y: 610,
    w: 1420,
    h: 240,
    size: 46,
    bold: true,
    color: C.white,
    valign: "middle",
    ls: 1.3,
  });
  footer(s, "০২ / ১৪");
  s.addNotes("এলার্জি হলো শরীরের এমন একটি প্রতিক্রিয়া, যেখানে শরীর কিছু জিনিস সহ্য করতে পারে না।");

  // ---------- 3 causes / 4 symptoms (5-card grid) ----------
  const grid5 = async (s, items, numbered) => {
    for (let i = 0; i < 5; i++) {
      const x = 128 + i * 337,
        y = 330,
        w = 316,
        last = i === 4;
      R(s, {
        x,
        y,
        w,
        h: 440,
        fill: last ? C.orangeSoft : C.white,
        line: last ? C.orange : C.border,
        lw: last ? 2 : 1,
      });
      if (numbered)
        T(s, items[i][0], {
          x,
          y: y + 40,
          w,
          h: 110,
          size: 96,
          bold: true,
          color: last ? C.orangeTxt : C.greenTxt,
          align: "center",
          valign: "middle",
        });
      else
        await I(
          s,
          items[i][0],
          last ? C.brownDark : C.white,
          x + 98,
          y + 40,
          120,
          last ? C.orange : C.green2,
        );
      T(s, items[i][1], {
        x: x + 16,
        y: y + 190,
        w: w - 32,
        h: 140,
        size: 34,
        bold: true,
        align: "center",
        valign: "middle",
      });
      T(s, items[i][2], {
        x: x + 16,
        y: y + 340,
        w: w - 32,
        h: 70,
        size: 26,
        color: last ? C.brown : C.muted,
        align: "center",
        valign: "middle",
      });
    }
  };
  s = pres.addSlide();
  bg(s, "light");
  header(s, "CAUSES OF ALLERGY", "এলার্জির", "কারণ");
  await grid5(s, [
    ["FaWind", "ধুলাবালি", "Dust & Pollution"],
    ["FaSnowflake", "ঠান্ডা আবহাওয়া", "Cold Weather"],
    ["FaUtensils", "খাবার", "Food Sensitivity"],
    ["FaFlask", "কেমিক্যাল", "Chemicals"],
    ["FaShieldAlt", "দুর্বল ইমিউন সিস্টেম", "Weak Immune System"],
  ]);
  footer(s, "০৩ / ১৪");
  s.addNotes("এলার্জির ৫টি কারণ: ধুলাবালি, ঠান্ডা আবহাওয়া, খাবার, কেমিক্যাল এবং দুর্বল ইমিউন সিস্টেম।");

  s = pres.addSlide();
  bg(s, "light2");
  header(s, "COMMON SYMPTOMS", "সাধারণ", "লক্ষণ");
  await grid5(
    s,
    [
      ["১", "চুলকানি", "Itching"],
      ["২", "হাঁচি", "Sneezing"],
      ["৩", "ত্বকে সমস্যা", "Skin Problems"],
      ["৪", "নাক দিয়ে পানি পড়া", "Runny Nose"],
      ["৫", "শ্বাসকষ্ট", "Breathing Difficulty"],
    ],
    true,
  );
  footer(s, "০৪ / ১৪");
  s.addNotes("এলার্জির ৫টি সাধারণ লক্ষণ: চুলকানি, হাঁচি, ত্বকে সমস্যা, নাক দিয়ে পানি পড়া এবং শ্বাসকষ্ট।");

  // ---------- 5 need ----------
  s = pres.addSlide();
  bg(s, "dark");
  T(s, "মানুষ চায়...", {
    x: 160,
    y: 250,
    w: 1600,
    h: 60,
    size: 38,
    bold: true,
    color: C.sand,
    align: "center",
  });
  T(s, "নিরাপদ সমাধান", {
    x: 160,
    y: 320,
    w: 1600,
    h: 180,
    size: 124,
    bold: true,
    color: C.white,
    align: "center",
    valign: "middle",
    ls: 1.0,
  });
  T(s, "Safe Solution", {
    x: 160,
    y: 510,
    w: 1600,
    h: 80,
    size: 60,
    bold: true,
    color: C.lime,
    align: "center",
    cs: 3,
  });
  s.addShape(pres.shapes.LINE, {
    x: P(880),
    y: P(620),
    w: P(160),
    h: 0,
    line: { color: C.orange, width: 3 },
  });
  T(s, "মানুষ এখন এমন সমাধান খুঁজছে যেটা দীর্ঘমেয়াদে উপকার দিতে পারে।", {
    x: 260,
    y: 660,
    w: 1400,
    h: 130,
    size: 40,
    color: "D7E8DD",
    align: "center",
    valign: "middle",
    ls: 1.3,
  });
  footer(s, "০৫ / ১৪", true);
  s.addNotes("মানুষ এখন এমন সমাধান খুঁজছে যেটা দীর্ঘমেয়াদে উপকার দিতে পারে।");

  // ---------- 6 product ----------
  s = pres.addSlide();
  bg(s, "light");
  R(s, { x: 128, y: 160, w: 660, h: 700, radius: 32, line: C.border, shadow: true });
  s.addImage({
    path: IMG.product,
    x: P(148),
    y: P(200),
    w: P(620),
    h: P(620),
    altText: "Allergy Clean পণ্যের ছবি",
  });
  T(s, "PRODUCT · পরিচিতি", {
    x: 860,
    y: 210,
    w: 900,
    h: 36,
    size: 24,
    bold: true,
    color: C.orangeTxt,
    cs: 2,
  });
  T(s, "Allergy Clean", {
    x: 860,
    y: 255,
    w: 932,
    h: 130,
    size: 100,
    bold: true,
    color: C.greenTxt,
    valign: "middle",
    ls: 1.0,
  });
  T(s, "একটি ন্যাচারাল সাপোর্ট প্রোডাক্ট", { x: 860, y: 395, w: 932, h: 60, size: 40, bold: true });
  R(s, { x: 860, y: 490, w: 932, h: 220, line: C.border });
  T(
    s,
    "Allergy Clean একটি ন্যাচারাল ভিত্তিক সাপোর্ট প্রোডাক্ট, যেটা এলার্জি সমস্যার জন্য সহায়ক হিসেবে ব্যবহার করা হয়।",
    { x: 900, y: 510, w: 852, h: 180, size: 32, color: C.muted, valign: "middle", ls: 1.4 },
  );
  const tags = [
    ["Natural", C.green2, C.white, 220],
    ["Safe", C.orange, C.brownDark, 170],
  ];
  let tx = 860;
  for (const [t, f, c, w] of tags) {
    R(s, { x: tx, y: 760, w, h: 70, radius: 35, fill: f });
    T(s, t, {
      x: tx,
      y: 760,
      w,
      h: 70,
      size: 32,
      bold: true,
      color: c,
      align: "center",
      valign: "middle",
    });
    tx += w + 20;
  }
  footer(s, "০৬ / ১৪");
  s.addNotes(
    "Allergy Clean একটি ন্যাচারাল ভিত্তিক সাপোর্ট প্রোডাক্ট, যেটা এলার্জি সমস্যার জন্য সহায়ক হিসেবে ব্যবহার করা হয়। Natural, Safe।",
  );

  // ---------- 7 works ----------
  s = pres.addSlide();
  bg(s, "light2");
  header(s, "NATURAL SUPPORT SYSTEM", "কীভাবে", "কাজ করে?");
  const works = [
    ["১", "প্রাকৃতিক উপাদান", "Natural Ingredients"],
    ["২", "শরীরকে সাপোর্ট", "Body Support"],
    ["৩", "ভেতর থেকে সহায়তা", "Inner Assistance"],
  ];
  for (let i = 0; i < 3; i++) {
    const x = 128 + i * 572,
      w = 480,
      last = i === 2;
    R(s, {
      x,
      y: 320,
      w,
      h: 360,
      radius: 28,
      fill: last ? C.green : C.white,
      line: last ? null : C.border,
    });
    R(s, { x: x + 190, y: 360, w: 100, h: 70, radius: 35, fill: last ? C.orange : C.green2 });
    T(s, works[i][0], {
      x: x + 190,
      y: 360,
      w: 100,
      h: 70,
      size: 42,
      bold: true,
      color: last ? C.brownDark : C.white,
      align: "center",
      valign: "middle",
    });
    T(s, works[i][1], {
      x: x + 20,
      y: 460,
      w: w - 40,
      h: 120,
      size: 40,
      bold: true,
      color: last ? C.white : C.dark,
      align: "center",
      valign: "middle",
    });
    T(s, works[i][2], {
      x: x + 20,
      y: 590,
      w: w - 40,
      h: 50,
      size: 28,
      color: last ? C.paleGreen : C.muted,
      align: "center",
    });
    if (i < 2) ARROW(s, x + w + 18, 480, 56, 40);
  }
  R(s, { x: 128, y: 760, w: 1664, h: 120, radius: 60, line: C.border });
  T(s, "প্রাকৃতিক উপাদানের মাধ্যমে শরীরকে ভেতর থেকে সাপোর্ট দেওয়ার ধারণার উপর এটি তৈরি করা হয়েছে।", {
    x: 168,
    y: 760,
    w: 1584,
    h: 120,
    size: 32,
    align: "center",
    valign: "middle",
  });
  footer(s, "০৭ / ১৪");
  s.addNotes("প্রাকৃতিক উপাদানের মাধ্যমে শরীরকে ভেতর থেকে সাপোর্ট দেওয়ার ধারণার উপর এটি তৈরি করা হয়েছে।");

  // ---------- 8 making / 10 income (4-step rows) ----------
  const row4 = async (s, items, opts) => {
    for (let i = 0; i < 4; i++) {
      const x = 128 + i * 432,
        w = 360,
        last = i === 3,
        y = 320;
      const fill = last ? (opts.lastDark ? C.green : C.orangeSoft) : C.white;
      R(s, {
        x,
        y,
        w,
        h: items[0].icon ? 430 : 380,
        fill,
        line: last ? (opts.lastDark ? null : C.orange) : C.border,
        lw: last ? 2 : 1,
      });
      let ty = y + 40;
      if (items[i].icon) {
        await I(
          s,
          items[i].icon,
          last ? C.green : C.white,
          x + 130,
          ty,
          100,
          last ? C.white : C.green2,
        );
        ty += 120;
      }
      T(s, items[i].num, {
        x,
        y: ty,
        w,
        h: 70,
        size: items[i].icon ? 36 : 64,
        bold: true,
        color: last
          ? opts.lastDark
            ? C.sand
            : C.orangeTxt
          : items[i].icon
            ? C.orangeTxt
            : C.greenTxt,
        align: "center",
        valign: "middle",
      });
      ty += 80;
      T(s, items[i].title, {
        x: x + 16,
        y: ty,
        w: w - 32,
        h: 100,
        size: 34,
        bold: true,
        color: last && opts.lastDark ? C.white : C.dark,
        align: "center",
        valign: "middle",
      });
      T(s, items[i].sub, {
        x: x + 16,
        y: ty + 105,
        w: w - 32,
        h: 44,
        size: 26,
        color: last ? (opts.lastDark ? C.paleGreen : C.brown) : C.muted,
        align: "center",
      });
      if (i < 3) ARROW(s, x + w + 14, 490, 44, 32);
    }
  };
  s = pres.addSlide();
  bg(s, "light");
  header(s, "PRODUCT MAKING", "প্রোডাক্ট", "তৈরি ধারণা");
  await row4(
    s,
    [
      { num: "01", title: "উপাদান নির্বাচন", sub: "Ingredient Selection" },
      { num: "02", title: "পরিষ্কার প্রক্রিয়া", sub: "Cleansing Process" },
      { num: "03", title: "সঠিক মিশ্রণ", sub: "Correct Mixing" },
      { num: "04", title: "নিরাপদ প্রস্তুতি", sub: "Safe Preparation" },
    ],
    {},
  );
  R(s, { x: 128, y: 770, w: 1664, h: 110, radius: 55, fill: C.green });
  T(s, "একটি প্রোডাক্ট তৈরির পেছনে পরিকল্পনা, উপাদান এবং সঠিক প্রক্রিয়া গুরুত্বপূর্ণ।", {
    x: 168,
    y: 770,
    w: 1584,
    h: 110,
    size: 32,
    color: C.white,
    align: "center",
    valign: "middle",
  });
  footer(s, "০৮ / ১৪");
  s.addNotes("একটি প্রোডাক্ট তৈরির পেছনে পরিকল্পনা, উপাদান এবং সঠিক প্রক্রিয়া গুরুত্বপূর্ণ।");

  // ---------- 9 opportunity ----------
  s = pres.addSlide();
  bg(s, "light2");
  R(s, { x: 170, y: 250, w: 620, h: 320, radius: 32, line: C.border, shadow: true });
  await I(s, "FaHeartbeat", C.white, 424, 290, 112, C.green2);
  T(s, "Health Solution", {
    x: 170,
    y: 430,
    w: 620,
    h: 100,
    size: 58,
    bold: true,
    color: C.green,
    align: "center",
    valign: "middle",
  });
  T(s, "+", {
    x: 800,
    y: 330,
    w: 120,
    h: 160,
    size: 130,
    bold: true,
    color: C.orange,
    align: "center",
    valign: "middle",
  });
  R(s, { x: 930, y: 250, w: 820, h: 320, radius: 32, fill: C.green, shadow: true });
  await I(s, "FaChartLine", C.green, 1284, 290, 112, C.white);
  T(s, "Business Opportunity", {
    x: 930,
    y: 430,
    w: 820,
    h: 100,
    size: 58,
    bold: true,
    color: C.white,
    align: "center",
    valign: "middle",
  });
  T(
    s,
    [
      { text: "যখন একটি প্রোডাক্ট মানুষের উপকারে আসে, তখন সেটি একটি " },
      { text: "Business Opportunity", options: { color: C.orangeTxt, bold: true } },
      { text: "-তেও পরিণত হয়।" },
    ],
    {
      x: 260,
      y: 650,
      w: 1400,
      h: 170,
      size: 42,
      bold: true,
      align: "center",
      valign: "middle",
      ls: 1.35,
    },
  );
  footer(s, "০৯ / ১৪");
  s.addNotes("যখন একটি প্রোডাক্ট মানুষের উপকারে আসে, তখন সেটি একটি Business Opportunity-তেও পরিণত হয়।");

  // ---------- 10 income ----------
  s = pres.addSlide();
  bg(s, "light");
  header(s, "INCOME OPPORTUNITY", "কিভাবে", "লাভবান হওয়া যায়?");
  await row4(
    s,
    [
      { icon: "FaShoppingBag", num: "১", title: "Product Selling", sub: "পণ্য বিক্রি করুন" },
      { icon: "FaHeadset", num: "২", title: "Customer Service", sub: "সেবা দিন" },
      { icon: "FaUsers", num: "৩", title: "Repeat Customer", sub: "নিয়মিত গ্রাহক" },
      { icon: "FaHandshake", num: "৪", title: "Trust Building", sub: "বিশ্বাস তৈরি" },
    ],
    { lastDark: true },
  );
  R(s, {
    x: 128,
    y: 790,
    w: 1664,
    h: 100,
    radius: 50,
    fill: C.orangeSoft,
    line: C.orangeLine,
    lw: 2,
  });
  T(s, "যখন মানুষ উপকার পায়, তখন বিশ্বাস তৈরি হয় এবং দীর্ঘমেয়াদী কাজের সুযোগ তৈরি হয়।", {
    x: 168,
    y: 790,
    w: 1584,
    h: 100,
    size: 32,
    color: C.brown,
    align: "center",
    valign: "middle",
  });
  footer(s, "১০ / ১৪");
  s.addNotes(
    "কিভাবে লাভবান হওয়া যায়: পণ্য বিক্রি করুন, সেবা দিন, নিয়মিত গ্রাহক তৈরি করুন, বিশ্বাস তৈরি করুন। যখন মানুষ উপকার পায়, তখন বিশ্বাস তৈরি হয় এবং দীর্ঘমেয়াদী কাজের সুযোগ তৈরি হয়।",
  );

  // ---------- 11 thinking ----------
  s = pres.addSlide();
  bg(s, "dark");
  T(s, "নতুন চিন্তা · New Thinking", {
    x: 160,
    y: 260,
    w: 1600,
    h: 60,
    size: 38,
    bold: true,
    color: C.sand,
    align: "center",
  });
  R(s, { x: 180, y: 380, w: 700, h: 130, radius: 26, fill: C.light });
  T(s, "মানুষের সমস্যা জানুন", {
    x: 180,
    y: 380,
    w: 700,
    h: 130,
    size: 56,
    bold: true,
    color: C.dark,
    align: "center",
    valign: "middle",
  });
  ARROW(s, 910, 425, 90, 44);
  R(s, { x: 1030, y: 380, w: 710, h: 130, radius: 26, fill: C.orange });
  T(s, "সমাধানের অংশ হোন", {
    x: 1030,
    y: 380,
    w: 710,
    h: 130,
    size: 56,
    bold: true,
    color: C.brownDark,
    align: "center",
    valign: "middle",
  });
  s.addShape(pres.shapes.LINE, {
    x: P(880),
    y: P(600),
    w: P(160),
    h: 0,
    line: { color: C.lime, width: 3 },
  });
  T(s, "“যে মানুষ সমস্যার সমাধান নিয়ে কাজ করে, সে সমাজে মূল্যবান হয়ে ওঠে।”", {
    x: 210,
    y: 640,
    w: 1500,
    h: 170,
    size: 48,
    bold: true,
    color: C.white,
    align: "center",
    valign: "middle",
    ls: 1.35,
  });
  footer(s, "১১ / ১৪", true);
  s.addNotes(
    "মানুষের সমস্যা জানুন, সমাধানের অংশ হোন। যে মানুষ সমস্যার সমাধান নিয়ে কাজ করে, সে সমাজে মূল্যবান হয়ে ওঠে।",
  );

  // ---------- 12 task ----------
  s = pres.addSlide();
  bg(s, "light2");
  header(s, "TODAY'S TASK", "আজকের", "Task");
  R(s, { x: 128, y: 300, w: 1664, h: 170, radius: 28, fill: C.green });
  await I(s, "FaSearch", C.green, 176, 340, 92, C.white);
  T(s, "আপনার আশেপাশে কতজন এলার্জির সমস্যায় ভুগছে?", {
    x: 310,
    y: 300,
    w: 1440,
    h: 170,
    size: 52,
    bold: true,
    color: C.white,
    valign: "middle",
  });
  T(
    s,
    "আজকে পর্যবেক্ষণ করুন: আপনার পরিবার, প্রতিবেশী, বন্ধুদের মধ্যে কতজন এলার্জিতে কষ্ট পাচ্ছেন। তাদের সংখ্যা গণনা করুন।",
    { x: 128, y: 510, w: 1664, h: 120, size: 34, color: C.muted, ls: 1.4 },
  );
  const cnt = ["পরিবার", "প্রতিবেশী", "বন্ধু"];
  for (let i = 0; i < 3; i++) {
    const x = 128 + i * 560;
    R(s, { x, y: 680, w: 480, h: 130, line: C.border });
    T(s, cnt[i], { x: x + 32, y: 680, w: 240, h: 130, size: 36, bold: true, valign: "middle" });
    R(s, {
      x: x + 300,
      y: 710,
      w: 150,
      h: 70,
      radius: 16,
      fill: C.white,
      line: C.sand,
      lw: 2.5,
      dash: "dash",
    });
    if (i < 2)
      T(s, "+", {
        x: x + 490,
        y: 680,
        w: 60,
        h: 130,
        size: 60,
        bold: true,
        color: C.orange,
        align: "center",
        valign: "middle",
      });
  }
  footer(s, "১২ / ১৪");
  s.addNotes(
    "আপনার আশেপাশে কতজন এলার্জির সমস্যায় ভুগছে? আজকে পর্যবেক্ষণ করুন, আপনার পরিবার, প্রতিবেশী, বন্ধুদের মধ্যে কতজন এলার্জিতে কষ্ট পাচ্ছেন। তাদের সংখ্যা গণনা করুন।",
  );

  // ---------- 13 next ----------
  s = pres.addSlide();
  bg(s, "soft");
  R(s, { x: 770, y: 220, w: 380, h: 60, radius: 30, fill: C.orange });
  T(s, "COMING NEXT", {
    x: 770,
    y: 220,
    w: 380,
    h: 60,
    size: 30,
    bold: true,
    color: C.brownDark,
    align: "center",
    valign: "middle",
    cs: 3,
  });
  T(s, "আগামীকাল আসছে...", {
    x: 160,
    y: 310,
    w: 1600,
    h: 140,
    size: 100,
    bold: true,
    align: "center",
    valign: "middle",
  });
  T(s, "আরও একটি Health Problem & Solution", {
    x: 160,
    y: 460,
    w: 1600,
    h: 80,
    size: 54,
    bold: true,
    color: C.greenTxt,
    align: "center",
  });
  T(s, "আগামীকালের ক্লাসে আমরা আরও একটি গুরুত্বপূর্ণ স্বাস্থ্য সমস্যা এবং তার সম্ভাব্য সমাধান নিয়ে আলোচনা করবো।", {
    x: 280,
    y: 560,
    w: 1360,
    h: 120,
    size: 36,
    color: C.muted,
    align: "center",
    valign: "middle",
    ls: 1.35,
  });
  R(s, { x: 540, y: 720, w: 840, h: 90, radius: 45, fill: C.green });
  await I(s, "FaCheckCircle", C.lime, 590, 742, 46, null, 0);
  T(s, "আগামীকালের ক্লাস মিস করবেন না!", {
    x: 650,
    y: 720,
    w: 700,
    h: 90,
    size: 36,
    bold: true,
    color: C.white,
    valign: "middle",
  });
  T(s, "১৩ / ১৪", {
    x: 1592,
    y: 982,
    w: 200,
    h: 36,
    size: 24,
    bold: true,
    color: C.green,
    align: "right",
  });
  s.addNotes(
    "আগামীকালের ক্লাসে আমরা আরও একটি গুরুত্বপূর্ণ স্বাস্থ্য সমস্যা এবং তার সম্ভাব্য সমাধান নিয়ে আলোচনা করবো। আগামীকালের ক্লাস মিস করবেন না!",
  );

  // ---------- 14 thanks ----------
  s = pres.addSlide();
  bg(s, "dark");
  T(s, "Thank You", {
    x: 160,
    y: 200,
    w: 1600,
    h: 160,
    size: 124,
    bold: true,
    color: C.white,
    align: "center",
    valign: "middle",
  });
  T(s, "ধন্যবাদ", {
    x: 160,
    y: 370,
    w: 1600,
    h: 110,
    size: 76,
    bold: true,
    color: C.lime,
    align: "center",
    valign: "middle",
  });
  s.addShape(pres.shapes.LINE, {
    x: P(880),
    y: P(510),
    w: P(160),
    h: 0,
    line: { color: C.orange, width: 3 },
  });
  T(s, "Al Insaf Life Care", {
    x: 160,
    y: 540,
    w: 1600,
    h: 64,
    size: 42,
    bold: true,
    color: C.white,
    align: "center",
  });
  T(s, "ইনসাফের সঙ্গে সেবার প্রতিশ্রুতি", {
    x: 160,
    y: 610,
    w: 1600,
    h: 60,
    size: 38,
    bold: true,
    color: C.sand,
    align: "center",
  });
  R(s, { x: 500, y: 710, w: 920, h: 86, radius: 43, fill: C.white, transp: 90, line: "2F5A47" });
  await I(s, "FaPhoneAlt", C.lime, 560, 733, 40, null, 0);
  T(s, "+880 1332-140494  |  01941474074", {
    x: 620,
    y: 710,
    w: 760,
    h: 86,
    size: 36,
    bold: true,
    color: C.white,
    valign: "middle",
  });
  T(s, "Day 4 | Allergy Problem & Allergy Clean", {
    x: 128,
    y: 982,
    w: 1000,
    h: 36,
    size: 24,
    bold: true,
    color: C.mutedDark,
  });
  footer(s, "১৪ / ১৪", true);
  s.addNotes("ধন্যবাদ। যোগাযোগ: +880 1332-140494, 01941474074।");

  await pres.writeFile({ fileName: OUT });
  console.log("wrote", OUT);
})().catch((e) => {
  console.error(e);
  process.exit(1);
});
