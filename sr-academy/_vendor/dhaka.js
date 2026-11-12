// Dhaka 2050: one procedural 3D city, camera shots and lighting driven by HyperFrames time (hf-seek).
import * as THREE from "three";
import { EffectComposer } from "three/addons/postprocessing/EffectComposer.js";
import { RenderPass } from "three/addons/postprocessing/RenderPass.js";
import { UnrealBloomPass } from "three/addons/postprocessing/UnrealBloomPass.js";
import { OutputPass } from "three/addons/postprocessing/OutputPass.js";
import { RoundedBoxGeometry } from "three/addons/geometries/RoundedBoxGeometry.js";

let LAST_T = 0;
window.addEventListener("hf-seek", (e) => (LAST_T = e.detail.time));

const clamp = (v, a = 0, b = 1) => Math.min(b, Math.max(a, v));
const ease = (x) => {
  x = clamp(x);
  return x < 0.5 ? 4 * x * x * x : 1 - Math.pow(-2 * x + 2, 3) / 2;
};
const out = (x) => 1 - Math.pow(1 - clamp(x), 3);
const lerp = (a, b, k) => a + (b - a) * k;
const V = (x, y, z) => new THREE.Vector3(x, y, z);
function rng(seed) {
  let a = seed >>> 0;
  return () => {
    a = (a + 0x6d2b79f5) >>> 0;
    let t = a;
    t = Math.imul(t ^ (t >>> 15), t | 1);
    t ^= t + Math.imul(t ^ (t >>> 7), t | 61);
    return ((t ^ (t >>> 14)) >>> 0) / 4294967296;
  };
}

// ---------- procedural textures ----------
function canvasTex(w, h, draw, repeat) {
  const c = document.createElement("canvas");
  c.width = w;
  c.height = h;
  draw(c.getContext("2d"), w, h);
  const t = new THREE.CanvasTexture(c);
  t.colorSpace = THREE.SRGBColorSpace;
  t.anisotropy = 4;
  if (repeat) {
    t.wrapS = t.wrapT = THREE.RepeatWrapping;
    t.repeat.set(repeat[0], repeat[1]);
  }
  return t;
}
function windowsTex(seed, lit) {
  const R = rng(seed);
  return canvasTex(128, 256, (g, w, h) => {
    g.fillStyle = lit ? "#000" : "#3a4150";
    g.fillRect(0, 0, w, h);
    for (let y = 6; y < h - 6; y += 16)
      for (let x = 6; x < w - 6; x += 14) {
        const on = R() > 0.35;
        if (lit) g.fillStyle = on ? (R() > 0.5 ? "#ffd59a" : "#9fdcff") : "#000";
        else g.fillStyle = R() > 0.5 ? "#8fb3d9" : "#5d7593";
        g.fillRect(x, y, 9, 10);
      }
  });
}
function nakshiTex() {
  return canvasTex(
    256,
    512,
    (g, w, h) => {
      g.fillStyle = "#000";
      g.fillRect(0, 0, w, h);
      g.lineWidth = 4;
      const cols = ["#ff8a1f", "#ff3d6e", "#ffd23f"];
      for (let y = 0; y < h; y += 64)
        for (let x = 0; x < w; x += 64) {
          const cx = x + 32,
            cy = y + 32,
            k = ((x + y) / 64) % 3;
          g.strokeStyle = cols[k];
          g.beginPath();
          g.moveTo(cx, cy - 26);
          g.lineTo(cx + 26, cy);
          g.lineTo(cx, cy + 26);
          g.lineTo(cx - 26, cy);
          g.closePath();
          g.stroke();
          g.beginPath();
          for (let i = 0; i < 8; i++) {
            const a = (i / 8) * Math.PI * 2;
            g.moveTo(cx, cy);
            g.lineTo(cx + Math.cos(a) * 12, cy + Math.sin(a) * 12);
          }
          g.stroke();
          g.fillStyle = cols[(k + 1) % 3];
          g.beginPath();
          g.arc(cx, cy, 4, 0, Math.PI * 2);
          g.fill();
        }
      g.strokeStyle = "#ffd23f";
      g.lineWidth = 6;
      for (let y = 0; y < h; y += 128) {
        g.beginPath();
        g.moveTo(0, y);
        g.lineTo(w, y);
        g.stroke();
      }
    },
    [3, 10],
  );
}
function rickshawArtTex() {
  return canvasTex(256, 256, (g, w, h) => {
    const bg = g.createLinearGradient(0, 0, 0, h);
    bg.addColorStop(0, "#ff2e63");
    bg.addColorStop(0.5, "#ffb400");
    bg.addColorStop(1, "#08d9d6");
    g.fillStyle = bg;
    g.fillRect(0, 0, w, h);
    const R = rng(9);
    for (let i = 0; i < 26; i++) {
      const x = R() * w,
        y = R() * h,
        r = 8 + R() * 22;
      for (let p = 0; p < 6; p++) {
        const a = (p / 6) * Math.PI * 2;
        g.fillStyle = ["#fff", "#2b2d42", "#ff006e", "#3a86ff"][p % 4];
        g.beginPath();
        g.ellipse(
          x + Math.cos(a) * r * 0.6,
          y + Math.sin(a) * r * 0.6,
          r * 0.45,
          r * 0.25,
          a,
          0,
          Math.PI * 2,
        );
        g.fill();
      }
      g.fillStyle = "#ffd60a";
      g.beginPath();
      g.arc(x, y, r * 0.25, 0, Math.PI * 2);
      g.fill();
    }
    g.strokeStyle = "#fff";
    g.lineWidth = 10;
    g.strokeRect(6, 6, w - 12, h - 12);
  });
}
function signTex(text, color) {
  return canvasTex(512, 160, (g, w, h) => {
    g.fillStyle = "rgba(0,0,0,0.0)";
    g.clearRect(0, 0, w, h);
    g.font = '700 92px "Hind Siliguri"';
    g.textAlign = "center";
    g.textBaseline = "middle";
    g.shadowColor = color;
    g.shadowBlur = 30;
    g.fillStyle = color;
    g.fillText(text, w / 2, h / 2 + 6);
    g.shadowBlur = 0;
    g.fillStyle = "#fff";
    g.globalAlpha = 0.85;
    g.fillText(text, w / 2, h / 2 + 6);
  });
}
function skyTex(top, mid, bot) {
  return canvasTex(8, 512, (g, w, h) => {
    const gr = g.createLinearGradient(0, 0, 0, h);
    gr.addColorStop(0, top);
    gr.addColorStop(0.55, mid);
    gr.addColorStop(1, bot);
    g.fillStyle = gr;
    g.fillRect(0, 0, w, h);
  });
}
function cloudTex() {
  return canvasTex(256, 256, (g) => {
    const R = rng(4);
    for (let i = 0; i < 40; i++) {
      const x = 40 + R() * 176,
        y = 70 + R() * 116,
        r = 20 + R() * 50;
      const gr = g.createRadialGradient(x, y, 0, x, y, r);
      gr.addColorStop(0, "rgba(255,255,255,0.35)");
      gr.addColorStop(1, "rgba(255,255,255,0)");
      g.fillStyle = gr;
      g.beginPath();
      g.arc(x, y, r, 0, Math.PI * 2);
      g.fill();
    }
  });
}

// ---------- scene presets (lighting per shot) ----------
const LOOKS = {
  sunrise: {
    sky: ["#2b4a8b", "#f7a35c", "#ffd7a0"],
    fog: 0xf0b37e,
    near: 60,
    far: 420,
    sun: [0xffc58a, 2.4, V(-80, 40, -60)],
    hemi: 0.7,
    win: 0.25,
    neon: 0.6,
    exp: 1.0,
  },
  night: {
    sky: ["#05040f", "#1a0b3a", "#3b1050"],
    fog: 0x1a0b2e,
    near: 30,
    far: 260,
    sun: [0x6f7cff, 0.5, V(40, 80, 40)],
    hemi: 0.25,
    win: 0.75,
    neon: 3.0,
    exp: 1.0,
  },
  morning: {
    sky: ["#4f8fe0", "#a8d4ff", "#e8f4ff"],
    fog: 0xcfe6ff,
    near: 80,
    far: 520,
    sun: [0xfff3df, 2.6, V(60, 90, 30)],
    hemi: 0.9,
    win: 0.1,
    neon: 0.2,
    exp: 1.0,
  },
  sunset: {
    sky: ["#241a5c", "#e8615a", "#ffb36b"],
    fog: 0xd27a63,
    near: 80,
    far: 600,
    sun: [0xff8a50, 2.2, V(-100, 30, -40)],
    hemi: 0.55,
    win: 0.7,
    neon: 1.8,
    exp: 1.0,
  },
  golden: {
    sky: ["#5fa8e8", "#ffe0a3", "#fff2d0"],
    fog: 0xf5ddb0,
    near: 70,
    far: 500,
    sun: [0xffd9a0, 2.8, V(-70, 60, 50)],
    hemi: 0.9,
    win: 0.05,
    neon: 0.2,
    exp: 1.0,
  },
  evening: {
    sky: ["#0d1640", "#3a3f8f", "#e07a5f"],
    fog: 0x3b3a6b,
    near: 40,
    far: 330,
    sun: [0xffa26b, 1.0, V(-90, 25, 60)],
    hemi: 0.4,
    win: 0.65,
    neon: 2.2,
    exp: 1.0,
  },
  dawn: {
    sky: ["#1b2a6b", "#ff9a8b", "#ffe1b8"],
    fog: 0xf2b4a0,
    near: 120,
    far: 700,
    sun: [0xffc9a0, 2.0, V(-60, 30, -80)],
    hemi: 0.75,
    win: 0.4,
    neon: 0.8,
    exp: 1.0,
  },
};

// shots: [start, end, look, cameraFn(t, k) -> {pos, look}]
export async function mountDhaka({ canvas, w, h, shots }) {
  await document.fonts.load('700 92px "Hind Siliguri"');
  const el = document.getElementById(canvas);
  const renderer = new THREE.WebGLRenderer({
    canvas: el,
    antialias: true,
    preserveDrawingBuffer: true,
  });
  renderer.setPixelRatio(1);
  renderer.setSize(w, h, false);
  renderer.toneMapping = THREE.ACESFilmicToneMapping;
  renderer.shadowMap.enabled = false;
  const scene = new THREE.Scene();
  scene.fog = new THREE.Fog(0xffffff, 60, 400);
  const camera = new THREE.PerspectiveCamera(55, w / h, 0.3, 1500);
  const sun = new THREE.DirectionalLight(0xffffff, 2);
  scene.add(sun);
  const hemi = new THREE.HemisphereLight(0xbfd8ff, 0x2a2018, 0.7);
  scene.add(hemi);
  const skies = Object.fromEntries(Object.entries(LOOKS).map(([k, L]) => [k, skyTex(...L.sky)]));

  // ground + roads + river
  const ground = new THREE.Mesh(
    new THREE.PlaneGeometry(1200, 1200),
    new THREE.MeshStandardMaterial({ color: 0x2c2f36, roughness: 0.9 }),
  );
  ground.rotation.x = -Math.PI / 2;
  scene.add(ground);
  const river = new THREE.Mesh(
    new THREE.PlaneGeometry(1200, 34),
    new THREE.MeshStandardMaterial({
      color: 0x1b3d5c,
      metalness: 0.9,
      roughness: 0.08,
      emissive: 0x0a1a33,
      emissiveIntensity: 0.5,
    }),
  );
  river.rotation.x = -Math.PI / 2;
  river.position.set(0, 0.05, -150);
  scene.add(river);
  const laneMat = new THREE.MeshBasicMaterial({ color: 0x9fdcff });
  for (let i = -12; i <= 12; i++) {
    const a = new THREE.Mesh(new THREE.PlaneGeometry(0.3, 260), laneMat);
    a.rotation.x = -Math.PI / 2;
    a.position.set(i * 12 + 6, 0.06, 0);
    scene.add(a);
    const b = new THREE.Mesh(new THREE.PlaneGeometry(300, 0.3), laneMat);
    b.rotation.x = -Math.PI / 2;
    b.position.set(0, 0.06, i * 12 + 6);
    if (i * 12 + 6 > -130) scene.add(b);
  }

  // buildings: 3 height classes with window textures (day map + night emissive)
  const R = rng(2050);
  const classes = [
    { hmin: 8, hmax: 22, rep: 2, list: [] },
    { hmin: 22, hmax: 45, rep: 4, list: [] },
    { hmin: 45, hmax: 90, rep: 8, list: [] },
  ];
  const roofs = [];
  for (let i = -12; i <= 12; i++)
    for (let j = -12; j <= 8; j++) {
      const x = i * 12,
        z = j * 12;
      if (Math.abs(z + 150) < 30 || z < -130) continue;
      if (Math.abs(x) < 8 && z > 6 && z < 84) continue; // robot plaza + camera corridor
      const d = Math.hypot(x, z + 10);
      const tall = d < 50 ? 0.85 : d < 100 ? 0.5 : 0.25;
      const r = R();
      const cls = r < tall * 0.45 ? 2 : r < tall ? 1 : 0;
      const C = classes[cls];
      const hh = C.hmin + R() * (C.hmax - C.hmin);
      let s = 7 + R() * 2.5;
      if ((i === 0 || i === 1) && z > -75 && z < 75) s = 6; // wider neon street at x=6
      C.list.push([x, z, s, hh]);
      roofs.push([x, z, s, hh]);
    }
  const winMats = [];
  classes.forEach((C, ci) => {
    const day = windowsTex(10 + ci, false),
      night = windowsTex(20 + ci, true);
    day.wrapS = day.wrapT = night.wrapS = night.wrapT = THREE.RepeatWrapping;
    day.repeat.set(1, C.rep);
    night.repeat.set(1, C.rep);
    const mat = new THREE.MeshStandardMaterial({
      map: day,
      emissiveMap: night,
      emissive: 0xffffff,
      emissiveIntensity: 0.3,
      roughness: 0.6,
      metalness: 0.2,
    });
    winMats.push(mat);
    const im = new THREE.InstancedMesh(new THREE.BoxGeometry(1, 1, 1), mat, C.list.length);
    const m = new THREE.Matrix4(),
      col = new THREE.Color();
    C.list.forEach(([x, z, s, hh], k) => {
      m.compose(V(x, hh / 2, z), new THREE.Quaternion(), V(s, hh, s));
      im.setMatrixAt(k, m);
      col.setHSL(0.58 + R() * 0.1, 0.1 + R() * 0.15, 0.55 + R() * 0.3);
      im.setColorAt(k, col);
    });
    scene.add(im);
  });

  // super towers with nakshi kantha facades
  const nk = nakshiTex();
  const towerMat = new THREE.MeshStandardMaterial({
    color: 0x1a1d29,
    metalness: 0.8,
    roughness: 0.25,
    emissiveMap: nk,
    emissive: 0xffffff,
    emissiveIntensity: 1,
  });
  const towers = [];
  [
    [0, -10, 260, 9],
    [-30, -30, 200, 8],
    [28, -34, 220, 8],
    [-14, 22, 170, 7],
    [40, 8, 180, 7],
    [-46, 4, 150, 6],
  ].forEach(([x, z, hh, r]) => {
    const g = new THREE.Group();
    const body = new THREE.Mesh(new THREE.CylinderGeometry(r * 0.55, r, hh, 6, 1), towerMat);
    body.position.y = hh / 2;
    g.add(body);
    const crown = new THREE.Mesh(
      new THREE.ConeGeometry(r * 0.55, hh * 0.12, 6),
      new THREE.MeshStandardMaterial({
        color: 0xffd23f,
        emissive: 0xff8a1f,
        emissiveIntensity: 1.2,
        metalness: 0.6,
        roughness: 0.3,
      }),
    );
    crown.position.y = hh + hh * 0.06;
    g.add(crown);
    const ring = new THREE.Mesh(
      new THREE.TorusGeometry(r * 1.05, 0.25, 8, 48),
      new THREE.MeshBasicMaterial({ color: 0x00e5ff }),
    );
    ring.rotation.x = Math.PI / 2;
    ring.position.y = hh * 0.62;
    g.add(ring);
    g.position.set(x, 0, z);
    scene.add(g);
    towers.push(g);
  });
  // sky bridges
  const bridgeMat = new THREE.MeshStandardMaterial({
    color: 0xdfe8ff,
    metalness: 0.7,
    roughness: 0.2,
    emissive: 0x00bcd4,
    emissiveIntensity: 0.3,
  });
  [
    [[0, -10], [-30, -30], 120],
    [[0, -10], [28, -34], 140],
    [[0, -10], [-14, 22], 110],
  ].forEach(([a, b, y]) => {
    const A = V(a[0], y, a[1]),
      B = V(b[0], y, b[1]),
      L = A.distanceTo(B);
    const br = new THREE.Mesh(new THREE.BoxGeometry(L, 2, 3), bridgeMat);
    br.position.copy(A).add(B).multiplyScalar(0.5);
    br.lookAt(B);
    br.rotateY(Math.PI / 2);
    scene.add(br);
  });

  // clouds layer (for tower shot)
  const cloudMat = new THREE.MeshBasicMaterial({
    map: cloudTex(),
    transparent: true,
    depthWrite: false,
    opacity: 0.8,
  });
  const clouds = new THREE.Group();
  const RC = rng(77);
  for (let i = 0; i < 40; i++) {
    const c = new THREE.Mesh(new THREE.PlaneGeometry(90, 90), cloudMat);
    c.rotation.x = -Math.PI / 2;
    c.position.set((RC() - 0.5) * 500, 150 + RC() * 25, (RC() - 0.5) * 500);
    clouds.add(c);
  }
  scene.add(clouds);

  // neon district: strips + Bengali signs on buildings around the street x=6 (z 40..-60)
  const neon = new THREE.Group();
  const neonCols = [0xff2bd6, 0x00e5ff, 0xff8a1f, 0x7c4dff, 0x39ff88];
  const neonMats = neonCols.map((c) => new THREE.MeshBasicMaterial({ color: c }));
  const RN = rng(5);
  for (let k = 0; k < 140; k++) {
    const side = RN() > 0.5 ? 1 : -1;
    const z = 60 - RN() * 130;
    const y = 3 + RN() * 30;
    const strip = new THREE.Mesh(
      new THREE.BoxGeometry(0.25, 0.25 + RN() * 5, 1 + RN() * 6),
      neonMats[k % neonMats.length],
    );
    strip.position.set(6 + side * 2.92, y, z);
    neon.add(strip);
  }
  const SIGNS = [
    ["ঢাকা ২০৫০", "#ff2bd6"],
    ["পুরান ঢাকা", "#00e5ff"],
    ["বুড়িগঙ্গা", "#ffb02e"],
    ["নিউ মার্কেট", "#7cff6b"],
    ["চা • কফি", "#ff8a1f"],
    ["রিকশা স্ট্যান্ড", "#b388ff"],
    ["সদরঘাট", "#00e5ff"],
    ["মেট্রো ⇢", "#ff2bd6"],
  ];
  SIGNS.forEach(([t, c], i) => {
    const m = new THREE.Mesh(
      new THREE.PlaneGeometry(9, 2.8),
      new THREE.MeshBasicMaterial({
        map: signTex(t, c),
        transparent: true,
        depthWrite: false,
        side: THREE.DoubleSide,
      }),
    );
    const side = i % 2 ? 1 : -1;
    m.position.set(6 + side * 2.85, 8 + (i % 3) * 7, 40 - i * 13);
    m.rotation.y = side > 0 ? -Math.PI / 2 : Math.PI / 2;
    neon.add(m);
  });
  // lantern boats on the river
  const RB = rng(6);
  for (let i = 0; i < 40; i++) {
    const b = new THREE.Mesh(new THREE.BoxGeometry(3, 0.6, 1.2), neonMats[i % neonMats.length]);
    b.position.set((RB() - 0.5) * 300, 0.4, -150 + (RB() - 0.5) * 26);
    b.userData.v = 0.5 + RB();
    b.userData.x0 = b.position.x;
    neon.add(b);
  }
  scene.add(neon);

  // rickshaw factory
  const artTex = rickshawArtTex();
  function rickshaw(scale = 1) {
    const g = new THREE.Group();
    const red = new THREE.MeshStandardMaterial({
      color: 0xd7263d,
      metalness: 0.5,
      roughness: 0.35,
    });
    const art = new THREE.MeshStandardMaterial({
      map: artTex,
      emissiveMap: artTex,
      emissive: 0xffffff,
      emissiveIntensity: 0.35,
      roughness: 0.5,
    });
    const chrome = new THREE.MeshStandardMaterial({
      color: 0xe8eef7,
      metalness: 1,
      roughness: 0.15,
    });
    const seat = new THREE.Mesh(new RoundedBoxGeometry(2.2, 1.1, 1.6, 3, 0.2), red);
    seat.position.set(0, 1.2, 0);
    g.add(seat);
    const back = new THREE.Mesh(new THREE.BoxGeometry(2.3, 1.6, 0.12), art);
    back.position.set(0, 1.5, -0.85);
    g.add(back);
    const hood = new THREE.Mesh(
      new THREE.CylinderGeometry(1.25, 1.25, 1.8, 20, 1, true, 0, Math.PI),
      art,
    );
    hood.rotation.z = Math.PI / 2;
    hood.rotation.y = Math.PI / 2;
    hood.position.set(0, 2.2, -0.1);
    g.add(hood);
    const frame = new THREE.Mesh(new THREE.BoxGeometry(0.15, 0.15, 3.4), chrome);
    frame.position.set(0, 0.7, 1.0);
    g.add(frame);
    const driverBody = new THREE.Mesh(
      new THREE.CapsuleGeometry(0.35, 0.8, 4, 8),
      new THREE.MeshStandardMaterial({ color: 0x2f6fd6, roughness: 0.6 }),
    );
    driverBody.position.set(0, 1.6, 2.3);
    g.add(driverBody);
    const head = new THREE.Mesh(
      new THREE.SphereGeometry(0.28, 16, 16),
      new THREE.MeshStandardMaterial({ color: 0x8d5a3b, roughness: 0.6 }),
    );
    head.position.set(0, 2.35, 2.3);
    g.add(head);
    const wingMat = new THREE.MeshBasicMaterial({
      color: 0x66f2ff,
      transparent: true,
      opacity: 0.55,
      side: THREE.DoubleSide,
      blending: THREE.AdditiveBlending,
      depthWrite: false,
    });
    const wings = [-1, 1].map((s) => {
      const wg = new THREE.Mesh(new THREE.PlaneGeometry(3.2, 1.1), wingMat);
      wg.position.set(s * 2.4, 1.2, 0.2);
      wg.rotation.x = -Math.PI / 2;
      g.add(wg);
      return wg;
    });
    const glow = new THREE.Mesh(
      new THREE.CircleGeometry(0.9, 24),
      new THREE.MeshBasicMaterial({
        color: 0xffa630,
        transparent: true,
        opacity: 0.9,
        blending: THREE.AdditiveBlending,
        depthWrite: false,
      }),
    );
    glow.rotation.x = Math.PI / 2;
    glow.position.set(0, 0.45, 0);
    g.add(glow);
    g.userData.wings = wings;
    g.scale.setScalar(scale);
    return g;
  }
  const hero = rickshaw(1);
  scene.add(hero);
  const fleet = [];
  const RF = rng(12);
  for (let i = 0; i < 26; i++) {
    const r = rickshaw(0.9 + RF() * 0.3);
    r.userData.lane = [
      (RF() - 0.5) * 200,
      95 + RF() * 45,
      (RF() - 0.5) * 200,
      6 + RF() * 8,
      RF() * 100,
    ];
    scene.add(r);
    fleet.push(r);
  }

  // metro: elevated track along x at z=60, y=18 + train of 5 cars + glass station
  const metro = new THREE.Group();
  const trackMat = new THREE.MeshStandardMaterial({
    color: 0xd9dee8,
    metalness: 0.4,
    roughness: 0.4,
  });
  const track = new THREE.Mesh(new THREE.BoxGeometry(700, 1.2, 4), trackMat);
  track.position.set(0, 17.4, 60);
  metro.add(track);
  for (let x = -330; x <= 330; x += 22) {
    const p = new THREE.Mesh(new THREE.CylinderGeometry(0.9, 1.1, 17, 10), trackMat);
    p.position.set(x, 8.5, 60);
    metro.add(p);
  }
  const glowLine = new THREE.Mesh(
    new THREE.BoxGeometry(700, 0.15, 0.2),
    new THREE.MeshBasicMaterial({ color: 0x39ff88 }),
  );
  glowLine.position.set(0, 18.05, 62);
  metro.add(glowLine);
  const station = new THREE.Mesh(
    new THREE.BoxGeometry(46, 7, 12),
    new THREE.MeshPhysicalMaterial({
      color: 0xbfe6ff,
      transparent: true,
      opacity: 0.22,
      roughness: 0.05,
      metalness: 0.1,
    }),
  );
  station.position.set(0, 21, 60);
  metro.add(station);
  const platform = new THREE.Mesh(new THREE.BoxGeometry(46, 0.6, 5), trackMat);
  platform.position.set(0, 17.6, 66);
  metro.add(platform);
  const gates = [];
  for (let i = 0; i < 6; i++) {
    const gt = new THREE.Mesh(
      new THREE.TorusGeometry(1.0, 0.1, 8, 32),
      new THREE.MeshBasicMaterial({ color: 0x00e5ff }),
    );
    gt.position.set(-12 + i * 5, 19.2, 65.5);
    metro.add(gt);
    gates.push(gt);
  }
  const train = new THREE.Group();
  const carMat = new THREE.MeshStandardMaterial({
    color: 0xf4f7fb,
    metalness: 0.5,
    roughness: 0.2,
  });
  const winMat = new THREE.MeshStandardMaterial({
    color: 0x0b1a2b,
    emissive: 0x7fd8ff,
    emissiveIntensity: 0.6,
    metalness: 0.6,
    roughness: 0.1,
  });
  const stripeMat = new THREE.MeshBasicMaterial({ color: 0x00c853 });
  for (let i = 0; i < 5; i++) {
    const c = new THREE.Mesh(new RoundedBoxGeometry(15, 3.6, 3.4, 4, 1.2), carMat);
    c.position.set(-i * 15.6, 0, 0);
    train.add(c);
    const wn = new THREE.Mesh(new THREE.BoxGeometry(12, 1.1, 3.45), winMat);
    wn.position.set(-i * 15.6, 0.5, 0);
    train.add(wn);
    const st = new THREE.Mesh(new THREE.BoxGeometry(14.6, 0.25, 3.5), stripeMat);
    st.position.set(-i * 15.6, -0.6, 0);
    train.add(st);
  }
  const nose = new THREE.Mesh(new THREE.SphereGeometry(1.75, 20, 16, 0, Math.PI), carMat);
  nose.rotation.y = Math.PI / 2;
  nose.scale.set(1, 1, 2.2);
  nose.position.set(7.4, 0, 0);
  train.add(nose);
  train.position.set(-200, 19.9, 60);
  metro.add(train);
  scene.add(metro);

  // rooftop gardens + solar panels (instanced), in a region around the garden shot
  const garden = new THREE.Group();
  const gRoofs = roofs.filter(([x, z, , hh]) => Math.hypot(x - 60, z - 40) < 110 && hh < 46);
  const treeN = gRoofs.length * 5;
  const crowns = new THREE.InstancedMesh(
    new THREE.IcosahedronGeometry(1, 1),
    new THREE.MeshStandardMaterial({ color: 0x3fae49, roughness: 0.8 }),
    treeN,
  );
  const lawn = new THREE.InstancedMesh(
    new THREE.BoxGeometry(1, 0.3, 1),
    new THREE.MeshStandardMaterial({ color: 0x6cc24a, roughness: 0.9 }),
    gRoofs.length,
  );
  const solar = new THREE.InstancedMesh(
    new THREE.BoxGeometry(2.4, 0.12, 1.4),
    new THREE.MeshStandardMaterial({ color: 0x1b3a8a, metalness: 0.8, roughness: 0.2 }),
    gRoofs.length,
  );
  const flowers = new THREE.InstancedMesh(
    new THREE.SphereGeometry(0.35, 8, 8),
    new THREE.MeshStandardMaterial({ color: 0xff4fa3, emissive: 0x551133, emissiveIntensity: 0.3 }),
    gRoofs.length * 3,
  );
  const RG = rng(31),
    mm = new THREE.Matrix4(),
    cc = new THREE.Color();
  let ti = 0,
    fi = 0;
  gRoofs.forEach(([x, z, s, hh], k) => {
    mm.compose(V(x, hh + 0.15, z), new THREE.Quaternion(), V(s * 0.95, 1, s * 0.95));
    lawn.setMatrixAt(k, mm);
    mm.compose(
      V(x + s * 0.25, hh + 0.5, z - s * 0.3),
      new THREE.Quaternion().setFromEuler(new THREE.Euler(-0.4, 0, 0)),
      V(1, 1, 1),
    );
    solar.setMatrixAt(k, mm);
    for (let q = 0; q < 5; q++) {
      const sc = 0.8 + RG() * 1.3;
      mm.compose(
        V(x + (RG() - 0.5) * s * 0.8, hh + 0.3 + sc, z + (RG() - 0.5) * s * 0.8),
        new THREE.Quaternion(),
        V(sc, sc * 1.1, sc),
      );
      crowns.setMatrixAt(ti, mm);
      cc.setHSL(0.27 + RG() * 0.08, 0.55, 0.32 + RG() * 0.15);
      crowns.setColorAt(ti++, cc);
    }
    for (let q = 0; q < 3; q++) {
      mm.compose(
        V(x + (RG() - 0.5) * s * 0.8, hh + 0.6, z + (RG() - 0.5) * s * 0.8),
        new THREE.Quaternion(),
        V(1, 1, 1),
      );
      flowers.setMatrixAt(fi, mm);
      cc.setHSL([0.95, 0.12, 0.83][q], 0.8, 0.6);
      flowers.setColorAt(fi++, cc);
    }
  });
  garden.add(crowns, lawn, solar, flowers);
  scene.add(garden);
  // birds
  const birds = new THREE.InstancedMesh(
    new THREE.ConeGeometry(0.35, 1.2, 3),
    new THREE.MeshBasicMaterial({ color: 0x1b1b1b }),
    60,
  );
  scene.add(birds);

  // robot plaza at (0, 24): platform, robot cop, cars, drones
  const plaza = new THREE.Group();
  plaza.position.set(0, 0, 24);
  const disc = new THREE.Mesh(
    new THREE.CylinderGeometry(3.2, 3.6, 1.2, 40),
    new THREE.MeshStandardMaterial({ color: 0xe8ecf4, metalness: 0.4, roughness: 0.3 }),
  );
  disc.position.y = 0.6;
  plaza.add(disc);
  const discRing = new THREE.Mesh(
    new THREE.TorusGeometry(3.3, 0.12, 8, 64),
    new THREE.MeshBasicMaterial({ color: 0x00e5ff }),
  );
  discRing.rotation.x = Math.PI / 2;
  discRing.position.y = 1.25;
  plaza.add(discRing);
  const white = new THREE.MeshStandardMaterial({
    color: 0xf2f5fa,
    metalness: 0.3,
    roughness: 0.25,
  });
  const blue = new THREE.MeshStandardMaterial({ color: 0x1e4fd8, metalness: 0.4, roughness: 0.3 });
  const robot = new THREE.Group();
  robot.position.y = 1.2;
  const torso = new THREE.Mesh(new RoundedBoxGeometry(1.6, 2.1, 0.9, 4, 0.3), blue);
  torso.position.y = 2.9;
  robot.add(torso);
  const belt = new THREE.Mesh(
    new THREE.BoxGeometry(1.65, 0.25, 0.95),
    new THREE.MeshBasicMaterial({ color: 0xffd23f }),
  );
  belt.position.y = 2.0;
  robot.add(belt);
  [-0.45, 0.45].forEach((x) => {
    const lg = new THREE.Mesh(new THREE.CapsuleGeometry(0.28, 1.4, 4, 8), white);
    lg.position.set(x, 1.0, 0);
    robot.add(lg);
  });
  const headG = new THREE.Group();
  headG.position.y = 4.45;
  robot.add(headG);
  const headM = new THREE.Mesh(new RoundedBoxGeometry(1.1, 0.95, 0.95, 4, 0.3), white);
  headG.add(headM);
  const visor = new THREE.Mesh(
    new RoundedBoxGeometry(0.9, 0.32, 0.1, 3, 0.1),
    new THREE.MeshBasicMaterial({ color: 0x00e5ff }),
  );
  visor.position.set(0, 0.05, 0.48);
  headG.add(visor);
  const cap = new THREE.Mesh(new THREE.CylinderGeometry(0.62, 0.62, 0.22, 24), blue);
  cap.position.y = 0.55;
  headG.add(cap);
  const capBill = new THREE.Mesh(new THREE.BoxGeometry(0.9, 0.06, 0.4), blue);
  capBill.position.set(0, 0.47, 0.55);
  headG.add(capBill);
  function arm(side) {
    const a = new THREE.Group();
    a.position.set(side * 1.0, 3.7, 0);
    const up = new THREE.Mesh(new THREE.CapsuleGeometry(0.22, 1.2, 4, 8), white);
    up.position.y = -0.7;
    a.add(up);
    const lamp = new THREE.Mesh(
      new THREE.SphereGeometry(0.25, 12, 12),
      new THREE.MeshBasicMaterial({ color: side > 0 ? 0x39ff88 : 0xff3355 }),
    );
    lamp.position.y = -1.5;
    a.add(lamp);
    robot.add(a);
    return [a, lamp];
  }
  const [armL] = arm(-1),
    [armR] = arm(1);
  plaza.add(robot);
  const carCols = [0xffffff, 0xe63946, 0x1d3557, 0xf1c40f, 0x2a9d8f, 0x8e44ad];
  const cars = [];
  for (let i = 0; i < 28; i++) {
    const c = new THREE.Mesh(
      new RoundedBoxGeometry(2.0, 1.1, 4.0, 3, 0.45),
      new THREE.MeshStandardMaterial({
        color: carCols[i % carCols.length],
        metalness: 0.6,
        roughness: 0.25,
      }),
    );
    const tail = new THREE.Mesh(
      new THREE.BoxGeometry(1.6, 0.15, 0.05),
      new THREE.MeshBasicMaterial({ color: 0xff2244 }),
    );
    tail.position.set(0, 0.1, -2.02);
    c.add(tail);
    const head = new THREE.Mesh(
      new THREE.BoxGeometry(1.6, 0.15, 0.05),
      new THREE.MeshBasicMaterial({ color: 0xe0f7ff }),
    );
    head.position.set(0, 0.1, 2.02);
    c.add(head);
    c.userData = { dir: i % 2, lane: (i % 4 < 2 ? -1 : 1) * 2.2, off: (i * 9.7) % 120 };
    plaza.add(c);
    cars.push(c);
  }
  const drones = [];
  for (let i = 0; i < 18; i++) {
    const d = new THREE.Group();
    const bodyD = new THREE.Mesh(
      new RoundedBoxGeometry(0.9, 0.25, 0.9, 2, 0.1),
      new THREE.MeshStandardMaterial({ color: 0x222831, metalness: 0.6, roughness: 0.3 }),
    );
    d.add(bodyD);
    [
      [-0.6, -0.6],
      [0.6, -0.6],
      [-0.6, 0.6],
      [0.6, 0.6],
    ].forEach(([x, z]) => {
      const r = new THREE.Mesh(
        new THREE.TorusGeometry(0.28, 0.04, 6, 16),
        new THREE.MeshBasicMaterial({ color: 0x00e5ff }),
      );
      r.rotation.x = Math.PI / 2;
      r.position.set(x, 0.1, z);
      d.add(r);
    });
    const box = new THREE.Mesh(
      new THREE.BoxGeometry(0.6, 0.5, 0.6),
      new THREE.MeshStandardMaterial({ color: 0xc8a165, roughness: 0.8 }),
    );
    box.position.y = -0.45;
    d.add(box);
    d.userData = { lane: i % 3, off: (i * 13.3) % 100 };
    plaza.add(d);
    drones.push(d);
  }
  scene.add(plaza);

  // composer
  const composer = new EffectComposer(renderer);
  composer.setPixelRatio(1);
  composer.setSize(w, h);
  composer.addPass(new RenderPass(scene, camera));
  const bloom = new UnrealBloomPass(new THREE.Vector2(w / 2, h / 2), 0.7, 0.5, 0.8);
  composer.addPass(bloom);
  composer.addPass(new OutputPass());

  const tmpLook = new THREE.Vector3();
  function applyLook(L) {
    scene.background = skies[L];
    const P = LOOKS[L];
    scene.fog.color.set(P.fog);
    scene.fog.near = P.near;
    scene.fog.far = P.far;
    sun.color.set(P.sun[0]);
    sun.intensity = P.sun[1];
    sun.position.copy(P.sun[2]);
    hemi.intensity = P.hemi;
    winMats.forEach((m) => (m.emissiveIntensity = P.win));
    neon.visible = P.neon > 0.5;
    bloom.strength = 0.2 + P.neon * 0.12;
    renderer.toneMappingExposure = P.exp;
  }

  function renderAt(T) {
    const shot = shots.find((s) => T >= s.start && T < s.end) || shots[shots.length - 1];
    const t = T - shot.start,
      k = clamp(t / (shot.end - shot.start));
    applyLook(shot.look);
    // world animation (global time keeps continuity)
    fleet.forEach((r, i) => {
      const [x0, y0, z0, sp, ph] = r.userData.lane;
      const u = ((T * sp + ph) % 260) - 130;
      const dir = i % 2 ? 1 : -1;
      r.position.set(
        x0 + u * dir,
        y0 + Math.sin(T * 0.8 + i) * 0.8,
        z0 + Math.sin(T * 0.2 + i) * 6,
      );
      r.rotation.y = dir > 0 ? Math.PI / 2 : -Math.PI / 2;
      r.userData.wings.forEach(
        (wg, s) => (wg.rotation.z = Math.sin(T * 9 + i) * 0.25 * (s ? 1 : -1)),
      );
      r.visible = shot.fleet !== false;
    });
    hero.visible = !!shot.hero;
    if (shot.hero) {
      hero.position.set(
        lerp(-40, 40, k) + shot.hero[0],
        shot.hero[1] + Math.sin(T * 1.2) * 0.6,
        shot.hero[2],
      );
      hero.rotation.set(Math.sin(T * 0.9) * 0.05, Math.PI / 2, Math.sin(T * 1.1) * 0.06);
      hero.userData.wings.forEach(
        (wg, s) => (wg.rotation.z = Math.sin(T * 10) * 0.3 * (s ? 1 : -1)),
      );
    }
    neon.children.forEach((c) => {
      if (c.userData.v) c.position.x = ((c.userData.x0 + 150 + T * c.userData.v * 3) % 300) - 150;
    });
    // metro: train drives through station during metro shot
    const mt = shot.id === "metro" ? t : 0;
    train.position.x = shot.id === "metro" ? lerp(-120, 260, ease(clamp((mt - 0.6) / 7.2))) : 200;
    gates.forEach((g, i) => g.scale.setScalar(1 + 0.15 * Math.sin(T * 6 + i)));
    garden.visible = ["garden", "dream", "end"].includes(shot.id);
    // birds
    const bm = new THREE.Matrix4();
    for (let i = 0; i < 60; i++) {
      const a = T * 0.35 + i * 0.105,
        rr = 18 + (i % 7) * 2;
      const p = V(
        60 + Math.cos(a) * rr,
        52 + Math.sin(T * 2 + i) * 1.5 + (i % 5),
        40 + Math.sin(a) * rr,
      );
      const flap = Math.sin(T * 14 + i) * 0.6;
      bm.compose(
        p,
        new THREE.Quaternion().setFromEuler(new THREE.Euler(Math.PI / 2, -a, flap)),
        V(1, 1, 1),
      );
      birds.setMatrixAt(i, bm);
    }
    birds.instanceMatrix.needsUpdate = true;
    birds.visible = shot.id === "garden" || shot.id === "dream";
    // robot plaza
    plaza.visible = shot.plaza !== false;
    const phase = Math.floor(T / 2.4) % 2;
    armL.rotation.z = phase ? -1.4 : -0.25 + Math.sin(T * 3) * 0.08;
    armR.rotation.z = phase ? 0.25 : 1.4 + Math.sin(T * 3) * 0.08;
    headG.rotation.y =
      shot.id === "robot"
        ? lerp(0, 0, 0) +
          (k > 0.82 ? lerp(-0.6, 0, out((k - 0.82) / 0.12)) : -0.6 + Math.sin(T * 0.7) * 0.25)
        : 0;
    headG.rotation.x = shot.id === "robot" && k > 0.9 ? Math.sin((k - 0.9) * 31) * 0.12 : 0;
    robot.rotation.y = shot.id === "robot" ? lerp(0.9, 0.0, out(k * 1.2)) : 0;
    cars.forEach((c) => {
      const { dir, lane, off } = c.userData;
      const go = dir === phase ? 1 : 0;
      const u = ((off + T * 9 * (0.35 + go * 0.65)) % 120) - 60;
      if (dir === 0) {
        c.position.set(lane, 0.6, u);
        c.rotation.y = lane > 0 ? Math.PI : 0;
        if (lane > 0) c.position.z = -u;
      } else {
        c.position.set(u, 0.6, lane);
        c.rotation.y = lane > 0 ? -Math.PI / 2 : Math.PI / 2;
        if (lane > 0) c.position.x = -u;
      }
      if (Math.abs(c.position.x) < 4.5 && Math.abs(c.position.z) < 4.5) c.position.y = -5; // keep the robot's disc clear
    });
    drones.forEach((d) => {
      const { lane, off } = d.userData;
      const u = ((off + T * 7) % 100) - 50;
      d.position.set(lane === 1 ? u : (lane - 1) * 6, 14 + lane * 3, lane === 1 ? -6 : u);
      d.rotation.y = T * 0.5;
    });
    clouds.visible = shot.id === "towers" || shot.id === "dream" || shot.id === "end";
    towers.forEach((tw, i) => (tw.children[2].rotation.z = T * (0.3 + i * 0.05)));
    // camera
    const cam = shot.cam(t, k);
    camera.position.copy(cam.pos);
    tmpLook.copy(cam.look);
    camera.lookAt(tmpLook);
    camera.fov = cam.fov || 55;
    camera.updateProjectionMatrix();
    composer.render();
  }

  window.addEventListener("hf-seek", (e) => renderAt(e.detail.time));
  renderAt(window.__hfThreeTime ?? LAST_T);
  return { renderAt, V, lerp, ease, out };
}

export { V, lerp, ease, out, clamp };
