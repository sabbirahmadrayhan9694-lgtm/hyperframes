// Sabbir Rayhan Academy — deterministic Three.js scene kit (seek-driven via hf-seek)
import * as THREE from "three";
import { EffectComposer } from "three/addons/postprocessing/EffectComposer.js";
import { RenderPass } from "three/addons/postprocessing/RenderPass.js";
import { UnrealBloomPass } from "three/addons/postprocessing/UnrealBloomPass.js";
import { OutputPass } from "three/addons/postprocessing/OutputPass.js";
import { RoomEnvironment } from "three/addons/environments/RoomEnvironment.js";
import { RoundedBoxGeometry } from "three/addons/geometries/RoundedBoxGeometry.js";
import { TextGeometry } from "three/addons/geometries/TextGeometry.js";
import { FontLoader } from "three/addons/loaders/FontLoader.js";

const G = 0x5cff2e,
  G2 = 0x2bd40f,
  LIME = 0xc6ff3d,
  BG = 0x020a04;

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
const clamp = (v, a = 0, b = 1) => Math.min(b, Math.max(a, v));
const ease = (x) => {
  x = clamp(x);
  return x < 0.5 ? 4 * x * x * x : 1 - Math.pow(-2 * x + 2, 3) / 2;
};
const out = (x) => 1 - Math.pow(1 - clamp(x), 3);
const back = (x) => {
  x = clamp(x);
  const c1 = 1.70158,
    c3 = c1 + 1;
  return 1 + c3 * Math.pow(x - 1, 3) + c1 * Math.pow(x - 1, 2);
};

const M = {
  neon: (c = G, i = 2.2) =>
    new THREE.MeshStandardMaterial({ color: c, emissive: c, emissiveIntensity: i, roughness: 0.4 }),
  dark: () =>
    new THREE.MeshPhysicalMaterial({
      color: 0x0c1f12,
      metalness: 0.7,
      roughness: 0.22,
      clearcoat: 1,
      clearcoatRoughness: 0.15,
    }),
  green: () =>
    new THREE.MeshPhysicalMaterial({
      color: 0x3fd61a,
      metalness: 0.35,
      roughness: 0.25,
      clearcoat: 1,
      emissive: 0x0f3a05,
      emissiveIntensity: 0.6,
    }),
  white: () =>
    new THREE.MeshPhysicalMaterial({
      color: 0xf2f5f3,
      metalness: 0.1,
      roughness: 0.28,
      clearcoat: 0.8,
    }),
  chrome: () => new THREE.MeshStandardMaterial({ color: 0xd9e6dc, metalness: 1, roughness: 0.18 }),
  wire: (c = G, o = 0.55) =>
    new THREE.MeshBasicMaterial({ color: c, wireframe: true, transparent: true, opacity: o }),
};

function stars(scene, n = 900, r = 40, seed = 7) {
  const R = rng(seed),
    pos = new Float32Array(n * 3);
  for (let i = 0; i < n; i++) {
    pos[i * 3] = (R() - 0.5) * r * 2;
    pos[i * 3 + 1] = (R() - 0.5) * r;
    pos[i * 3 + 2] = -R() * r - 4;
  }
  const g = new THREE.BufferGeometry();
  g.setAttribute("position", new THREE.BufferAttribute(pos, 3));
  const p = new THREE.Points(
    g,
    new THREE.PointsMaterial({ color: 0x8dff6a, size: 0.06, transparent: true, opacity: 0.7 }),
  );
  scene.add(p);
  return p;
}

let fontPromise = null;
function loadFont(url) {
  if (!fontPromise) fontPromise = new Promise((res) => new FontLoader().load(url, res));
  return fontPromise;
}
function text3d(font, str, size = 1, depth = 0.35, mat = M.white()) {
  const g = new TextGeometry(str, {
    font,
    size,
    depth,
    curveSegments: 6,
    bevelEnabled: true,
    bevelThickness: 0.04,
    bevelSize: 0.025,
    bevelSegments: 3,
  });
  g.center();
  return new THREE.Mesh(g, mat);
}
function gearShape(teeth = 12, r = 1, h = 0.18, inner = 0.35) {
  const s = new THREE.Shape(),
    n = teeth * 4;
  for (let i = 0; i <= n; i++) {
    const a = (i / n) * Math.PI * 2,
      rr = i % 4 < 2 ? r + h : r;
    if (i === 0) s.moveTo(Math.cos(a) * rr, Math.sin(a) * rr);
    else s.lineTo(Math.cos(a) * rr, Math.sin(a) * rr);
  }
  const hole = new THREE.Path();
  hole.absarc(0, 0, inner, 0, Math.PI * 2, true);
  s.holes.push(hole);
  return s;
}

// ---------- scene kinds: (ctx) => update(t) ----------
const KINDS = {
  // 1 neural brain sphere
  neural({ scene, camera }) {
    const grp = new THREE.Group();
    scene.add(grp);
    const ico = new THREE.Mesh(new THREE.IcosahedronGeometry(2.2, 2), M.wire(G, 0.35));
    grp.add(ico);
    const core = new THREE.Mesh(new THREE.IcosahedronGeometry(1.1, 5), M.green());
    grp.add(core);
    const R = rng(3),
      nodes = [];
    const pts = ico.geometry.attributes.position;
    for (let i = 0; i < pts.count; i += 3) {
      const n = new THREE.Mesh(
        new THREE.SphereGeometry(0.055, 12, 12),
        M.neon(R() > 0.7 ? LIME : G, 3),
      );
      n.position.fromBufferAttribute(pts, i);
      grp.add(n);
      nodes.push([n, R() * 6]);
    }
    const ring = new THREE.Mesh(new THREE.TorusGeometry(3.2, 0.015, 8, 160), M.neon(G, 2));
    ring.rotation.x = 1.2;
    grp.add(ring);
    const ring2 = ring.clone();
    ring2.rotation.set(0.4, 0.9, 0);
    ring2.scale.setScalar(1.15);
    grp.add(ring2);
    return (t, p) => {
      const s = back(t / 1.2);
      grp.scale.setScalar(0.001 + s);
      grp.rotation.y = t * 0.45;
      grp.rotation.x = Math.sin(t * 0.5) * 0.2;
      core.scale.setScalar(1 + 0.06 * Math.sin(t * 3));
      nodes.forEach(([n, o]) => n.scale.setScalar(0.7 + 0.6 * Math.max(0, Math.sin(t * 2.4 + o))));
      ring.rotation.z = t * 0.6;
      ring2.rotation.z = -t * 0.4;
      camera.position.z = 8.5 - p * 1.6;
    };
  },
  // 2 chat bubbles
  chat({ scene, camera }) {
    const grp = new THREE.Group();
    scene.add(grp);
    const mk = (w, h, mat, x, y, z) => {
      const m = new THREE.Mesh(new RoundedBoxGeometry(w, h, 0.35, 6, 0.3), mat);
      m.position.set(x, y, z);
      grp.add(m);
      const dots = [];
      for (let i = 0; i < 3; i++) {
        const d = new THREE.Mesh(
          new THREE.SphereGeometry(0.12, 16, 16),
          M.neon(mat === M._g ? 0xffffff : G, 2.5),
        );
        d.position.set(x - 0.4 + i * 0.4, y, z + 0.22);
        grp.add(d);
        dots.push(d);
      }
      return [m, dots];
    };
    M._g = M.green();
    const b = [
      mk(2.8, 1.3, M._g, -1.4, 0.9, 0),
      mk(3.2, 1.4, M.white(), 1.4, -0.8, -0.6),
      mk(2.2, 1.1, M._g, -0.6, -2.4, 0.4),
    ];
    return (t, p) => {
      b.forEach(([m, dots], i) => {
        const k = back((t - i * 0.45) / 0.8);
        const s = 0.001 + k;
        m.scale.setScalar(s);
        dots.forEach((d, j) => {
          d.scale.setScalar(s * (0.7 + 0.4 * Math.max(0, Math.sin(t * 6 - j * 0.9))));
        });
        m.position.y += Math.sin(t * 1.4 + i) * 0.002;
      });
      grp.rotation.y = Math.sin(t * 0.5) * 0.35;
      grp.rotation.x = -0.1;
      camera.position.z = 9 - p * 1.2;
    };
  },
  // 3 torus knot "prompt engine"
  knot({ scene, camera }) {
    const k = new THREE.Mesh(new THREE.TorusKnotGeometry(1.6, 0.42, 300, 40, 2, 3), M.green());
    scene.add(k);
    const w = new THREE.Mesh(
      new THREE.TorusKnotGeometry(1.6, 0.48, 120, 12, 2, 3),
      M.wire(LIME, 0.25),
    );
    scene.add(w);
    const halo = new THREE.Mesh(new THREE.TorusGeometry(3.4, 0.02, 8, 200), M.neon(G, 2.5));
    scene.add(halo);
    return (t, p) => {
      const s = back(t / 1.1);
      k.scale.setScalar(0.001 + s);
      w.scale.setScalar(0.001 + s);
      k.rotation.set(t * 0.4, t * 0.7, 0);
      w.rotation.copy(k.rotation);
      halo.rotation.set(Math.PI / 2 + Math.sin(t) * 0.2, 0, t * 0.5);
      halo.scale.setScalar(0.001 + out(t / 1.6));
      camera.position.z = 9 - p * 1.5;
    };
  },
  // 4 interlocking gears
  gears({ scene, camera }) {
    const ex = {
      depth: 0.4,
      bevelEnabled: true,
      bevelThickness: 0.05,
      bevelSize: 0.04,
      bevelSegments: 2,
      curveSegments: 6,
    };
    const g1 = new THREE.Mesh(
      new THREE.ExtrudeGeometry(gearShape(14, 1.5, 0.28, 0.45), ex),
      M.green(),
    );
    const g2 = new THREE.Mesh(
      new THREE.ExtrudeGeometry(gearShape(10, 1.05, 0.28, 0.35), ex),
      M.white(),
    );
    const g3 = new THREE.Mesh(
      new THREE.ExtrudeGeometry(gearShape(8, 0.82, 0.26, 0.28), ex),
      M.chrome(),
    );
    g1.position.set(-1.4, 0.2, 0);
    g2.position.set(1.32, 0.95, 0);
    g3.position.set(1.05, -1.75, 0.0);
    const grp = new THREE.Group();
    grp.add(g1, g2, g3);
    scene.add(grp);
    return (t, p) => {
      const s = back(t / 1);
      grp.scale.setScalar(0.001 + s);
      g1.rotation.z = t * 0.8;
      g2.rotation.z = -t * 0.8 * (14 / 10) + 0.16;
      g3.rotation.z = -t * 0.8 * (14 / 8) + 0.2;
      grp.rotation.y = -0.5 + Math.sin(t * 0.5) * 0.25;
      grp.rotation.x = -0.25;
      camera.position.z = 9 - p * 1.4;
    };
  },
  // 5 cube wave field
  cubes({ scene, camera }) {
    const N = 14,
      geo = new RoundedBoxGeometry(0.42, 0.42, 0.42, 2, 0.06),
      list = [];
    const mats = [M.dark(), M.green(), M.neon(G, 1.6)];
    for (let i = 0; i < N; i++)
      for (let j = 0; j < N; j++) {
        const d = Math.hypot(i - N / 2, j - N / 2),
          m = new THREE.Mesh(geo, d < 2.2 ? mats[2] : d < 4.5 ? mats[1] : mats[0]);
        m.position.set((i - N / 2) * 0.5, 0, (j - N / 2) * 0.5);
        scene.add(m);
        list.push([m, d]);
      }
    camera.position.set(0, 6, 7.5);
    camera.lookAt(0, 0, 0);
    return (t, p) => {
      list.forEach(([m, d]) => {
        m.position.y =
          Math.sin(d * 0.8 - t * 3) * 0.45 * out(t / 1.5) - (1 - out((t - d * 0.06) / 0.8)) * 4;
      });
      camera.position.set(Math.sin(t * 0.3) * 3, 6 - p * 1.5, 7.5 - p);
      camera.lookAt(0, 0, 0);
    };
  },
  // 6 3D bar chart rising
  bars({ scene, camera }) {
    const vals = [0.35, 0.5, 0.42, 0.68, 0.8, 1.0],
      bars = [];
    vals.forEach((v, i) => {
      const m = new THREE.Mesh(
        new RoundedBoxGeometry(0.7, 4, 0.7, 3, 0.08),
        i === vals.length - 1 ? M.neon(G, 1.8) : M.green(),
      );
      m.position.set((i - 2.5) * 1.05, 0, 0);
      scene.add(m);
      bars.push([m, v]);
    });
    const base = new THREE.Mesh(new RoundedBoxGeometry(7.4, 0.12, 2, 2, 0.05), M.dark());
    base.position.y = -2.05;
    scene.add(base);
    const arrowPts = vals.map(
      (v, i) => new THREE.Vector3((i - 2.5) * 1.05, -2 + v * 4 + 0.45, 0.5),
    );
    const curve = new THREE.CatmullRomCurve3(arrowPts);
    const tube = new THREE.Mesh(new THREE.TubeGeometry(curve, 120, 0.05, 8), M.neon(LIME, 3));
    scene.add(tube);
    camera.position.set(2.5, 1.2, 8.5);
    return (t, p) => {
      bars.forEach(([m, v], i) => {
        const k = ease((t - 0.15 * i) / 1.0);
        m.scale.y = 0.001 + v * k;
        m.position.y = -2 + 2 * v * k;
      });
      const tk = clamp((t - 1.1) / 1.2);
      tube.geometry.setDrawRange(0, Math.floor((tk * tube.geometry.index.count) / 3) * 3);
      camera.position.x = 2.5 - p * 3.5;
      camera.lookAt(0, 0, 0);
    };
  },
  // 7 robot head (AI agent)
  robot({ scene, camera }) {
    const grp = new THREE.Group();
    scene.add(grp);
    const head = new THREE.Mesh(new RoundedBoxGeometry(3, 2.4, 2.2, 6, 0.55), M.white());
    grp.add(head);
    const visor = new THREE.Mesh(new RoundedBoxGeometry(2.5, 1.05, 0.3, 4, 0.25), M.dark());
    visor.position.set(0, 0.1, 1.05);
    grp.add(visor);
    const eyes = [-0.55, 0.55].map((x) => {
      const e = new THREE.Mesh(new RoundedBoxGeometry(0.5, 0.26, 0.1, 3, 0.1), M.neon(G, 4));
      e.position.set(x, 0.12, 1.22);
      grp.add(e);
      return e;
    });
    const ant = new THREE.Mesh(new THREE.CylinderGeometry(0.05, 0.05, 0.8), M.chrome());
    ant.position.y = 1.6;
    grp.add(ant);
    const bulb = new THREE.Mesh(new THREE.SphereGeometry(0.17, 20, 20), M.neon(LIME, 4));
    bulb.position.y = 2.05;
    grp.add(bulb);
    [-1.62, 1.62].forEach((x) => {
      const e = new THREE.Mesh(new THREE.CylinderGeometry(0.38, 0.38, 0.25, 32), M.green());
      e.rotation.z = Math.PI / 2;
      e.position.x = x;
      grp.add(e);
      return e;
    });
    const orb = new THREE.Mesh(new THREE.TorusGeometry(2.6, 0.02, 8, 160), M.neon(G, 2));
    orb.rotation.x = 1.3;
    grp.add(orb);
    return (t, p) => {
      grp.scale.setScalar(0.001 + back(t / 1.1));
      grp.rotation.y = Math.sin(t * 0.8) * 0.45;
      grp.rotation.x = Math.sin(t * 0.6) * 0.08;
      grp.position.y = Math.sin(t * 1.3) * 0.12;
      const blink = t % 2.6 > 2.45 ? 0.15 : 1;
      eyes.forEach((e) => (e.scale.y = blink));
      bulb.material.emissiveIntensity = 2 + 2 * Math.max(0, Math.sin(t * 5));
      orb.rotation.z = t;
      camera.position.z = 9 - p * 1.3;
    };
  },
  // 8 pipeline with flowing packets
  pipeline({ scene, camera }) {
    const pts = [
      [-5, -1.5, 0],
      [-2.5, 1, -1],
      [0, -0.5, 0.5],
      [2.5, 1.2, -0.5],
      [5, -0.8, 0],
    ].map((a) => new THREE.Vector3(...a));
    const curve = new THREE.CatmullRomCurve3(pts);
    const tube = new THREE.Mesh(
      new THREE.TubeGeometry(curve, 200, 0.12, 12),
      new THREE.MeshPhysicalMaterial({
        color: 0x0f2a14,
        metalness: 0.4,
        roughness: 0.2,
        transparent: true,
        opacity: 0.55,
      }),
    );
    scene.add(tube);
    const stations = pts.map((v, i) => {
      const m = new THREE.Mesh(
        new RoundedBoxGeometry(0.9, 0.9, 0.9, 4, 0.18),
        i % 2 ? M.white() : M.green(),
      );
      m.position.copy(v);
      scene.add(m);
      return m;
    });
    const packets = Array.from({ length: 16 }, (_, i) => {
      const m = new THREE.Mesh(
        new THREE.SphereGeometry(0.1, 16, 16),
        M.neon(i % 3 ? G : LIME, 3.5),
      );
      scene.add(m);
      return [m, i / 16];
    });
    camera.position.set(0, 0.8, 9);
    return (t, p) => {
      stations.forEach((s, i) => {
        s.scale.setScalar(0.001 + back((t - i * 0.2) / 0.7));
        s.rotation.set(t * 0.5 + i, t * 0.7, 0);
      });
      packets.forEach(([m, o]) => {
        const u = (o + t * 0.12) % 1;
        m.position.copy(curve.getPointAt(u));
        m.visible = t > 0.9;
      });
      camera.position.x = -1 + p * 2;
      camera.lookAt(0, 0, 0);
    };
  },
  // 9 & 19 extruded logo text
  logo({ scene, camera, font }) {
    const grp = new THREE.Group();
    scene.add(grp);
    const s = text3d(font, "S", 2.4, 0.6, M.white()),
      r = text3d(font, "R", 2.4, 0.6, M.white());
    s.position.x = -1.05;
    r.position.x = 1.15;
    grp.add(s, r);
    const leaf = new THREE.Shape();
    leaf.moveTo(0, -1.4);
    leaf.bezierCurveTo(1.1, -0.6, 1.0, 0.8, 0.2, 1.6);
    leaf.bezierCurveTo(0.0, 0.5, -0.6, -0.4, 0, -1.4);
    const lf = new THREE.Mesh(
      new THREE.ExtrudeGeometry(leaf, {
        depth: 0.3,
        bevelEnabled: true,
        bevelSize: 0.04,
        bevelThickness: 0.04,
      }),
      M.neon(G, 1.2),
    );
    lf.position.set(0.05, -0.1, 0.5);
    lf.rotation.z = -0.35;
    grp.add(lf);
    const ring = new THREE.Mesh(new THREE.TorusGeometry(3.3, 0.03, 8, 200), M.neon(G, 2.5));
    grp.add(ring);
    const play = new THREE.Mesh(new RoundedBoxGeometry(0.7, 0.7, 0.3, 3, 0.15), M.neon(G2, 1.6));
    play.position.set(2.7, -1.1, 0.2);
    grp.add(play);
    return (t, p) => {
      const k = out(t / 1.4);
      s.position.set(-1.05 - (1 - k) * 6, 0, -(1 - k) * 6);
      r.position.set(1.15 + (1 - k) * 6, 0, -(1 - k) * 6);
      lf.scale.setScalar(0.001 + back((t - 0.9) / 0.7));
      play.scale.setScalar(0.001 + back((t - 1.3) / 0.6));
      ring.scale.setScalar(0.001 + out((t - 0.6) / 1.2));
      ring.rotation.set(Math.PI / 2 - 0.25, 0, t * 0.6);
      grp.rotation.y = (1 - k) * 0.9 + Math.sin(t * 0.6) * 0.18;
      grp.rotation.x = Math.sin(t * 0.4) * 0.05;
      camera.position.z = 10 - p * 1.6;
    };
  },
  // 10 helix timeline
  helix({ scene, camera }) {
    const grp = new THREE.Group();
    scene.add(grp);
    const items = [];
    for (let i = 0; i < 60; i++) {
      const a = i * 0.42,
        y = (i - 30) * 0.16;
      [0, Math.PI].forEach((o, k) => {
        const m = new THREE.Mesh(
          new THREE.SphereGeometry(0.13, 16, 16),
          k ? M.white() : M.neon(G, 2),
        );
        m.position.set(Math.cos(a + o) * 1.4, y, Math.sin(a + o) * 1.4);
        grp.add(m);
        items.push([m, i]);
      });
      if (i % 3 === 0) {
        const b = new THREE.Mesh(new THREE.CylinderGeometry(0.03, 0.03, 2.8), M.green());
        b.position.y = y;
        b.rotation.set(0, -a, Math.PI / 2);
        grp.add(b);
        items.push([b, i]);
      }
    }
    grp.rotation.z = 0.5;
    return (t, p) => {
      items.forEach(([m, i]) => m.scale.setScalar(0.001 + out((t * 40 - i) / 6)));
      grp.rotation.y = t * 0.6;
      camera.position.z = 9 - p * 1.5;
    };
  },
  // 11 chaos -> order cubes
  order({ scene, camera }) {
    const R = rng(11),
      list = [];
    for (let i = 0; i < 64; i++) {
      const m = new THREE.Mesh(
        new RoundedBoxGeometry(0.5, 0.5, 0.5, 2, 0.08),
        i % 5 ? M.green() : M.white(),
      );
      const gx = (i % 8) - 3.5,
        gy = Math.floor(i / 8) - 3.5;
      const chaos = new THREE.Vector3((R() - 0.5) * 9, (R() - 0.5) * 6, (R() - 0.5) * 5);
      const rot = new THREE.Euler(R() * 6, R() * 6, R() * 6);
      scene.add(m);
      list.push([m, chaos, new THREE.Vector3(gx * 0.62, gy * 0.62, 0), rot, R()]);
    }
    return (t, p) => {
      list.forEach(([m, c, g, r, o]) => {
        const k = ease((t - 1.2 - o * 0.6) / 1.2);
        m.position.lerpVectors(c, g, k);
        m.position.y += (1 - k) * Math.sin(t * 2 + o * 6) * 0.3;
        m.rotation.set(r.x * (1 - k) + t * (1 - k), r.y * (1 - k), r.z * (1 - k));
      });
      camera.position.set(Math.sin(t * 0.4) * 1.5, 0, 9.5 - p);
      camera.lookAt(0, 0, 0);
    };
  },
  // 12 countdown numerals
  countdown({ scene, camera, font }) {
    const nums = ["3", "2", "1"].map((n) => {
      const m = text3d(font, n, 3.2, 0.8, M.green());
      scene.add(m);
      return m;
    });
    const ring = new THREE.Mesh(
      new THREE.TorusGeometry(2.8, 0.06, 12, 200, Math.PI * 2),
      M.neon(G, 2.5),
    );
    scene.add(ring);
    return (t) => {
      const seg = 1.0;
      nums.forEach((m, i) => {
        const lt = t - i * seg,
          k = clamp(lt / seg);
        m.visible = lt >= 0 && lt < seg;
        m.scale.setScalar(0.4 + back(k * 2.2) * 0.8 - Math.max(0, k - 0.75) * 2);
        m.rotation.y = (1 - out(k * 2)) * 1.4;
        m.position.z = k * 1.2;
      });
      ring.rotation.z = -t * 2;
      ring.scale.setScalar(1 + 0.08 * Math.sin(t * 6.28));
      camera.position.z = 9;
    };
  },
  // 13 floating tool cards orbiting
  cards({ scene, camera }) {
    const grp = new THREE.Group();
    scene.add(grp);
    const cs = [];
    for (let i = 0; i < 5; i++) {
      const c = new THREE.Mesh(
        new RoundedBoxGeometry(1.8, 2.4, 0.12, 4, 0.12),
        i % 2 ? M.white() : M.green(),
      );
      const ic = new THREE.Mesh(
        new THREE.TorusGeometry(0.35, 0.09, 12, 40),
        M.neon(i % 2 ? G2 : 0xffffff, 1.8),
      );
      ic.position.set(0, 0.35, 0.12);
      c.add(ic);
      for (let l = 0; l < 2; l++) {
        const ln = new THREE.Mesh(
          new RoundedBoxGeometry(1.1 - l * 0.3, 0.12, 0.05, 2, 0.03),
          M.dark(),
        );
        ln.position.set(0, -0.45 - l * 0.28, 0.08);
        c.add(ln);
      }
      grp.add(c);
      cs.push(c);
    }
    camera.position.set(0, 1.2, 9);
    return (t, p) => {
      cs.forEach((c, i) => {
        const a = (i / cs.length) * Math.PI * 2 + t * 0.5,
          r = 3.4 * out((t - i * 0.12) / 1);
        c.position.set(Math.sin(a) * r, Math.sin(t * 1.2 + i) * 0.25, Math.cos(a) * r);
        c.rotation.y = a;
        c.scale.setScalar(0.001 + out((t - i * 0.12) / 0.8));
      });
      camera.lookAt(0, 0, 0);
      camera.position.y = 1.2 - p * 0.6;
    };
  },
  // 14 keyboard keycaps
  keys({ scene, camera }) {
    const grp = new THREE.Group();
    scene.add(grp);
    const caps = [];
    for (let r = 0; r < 4; r++)
      for (let c = 0; c < 10; c++) {
        const hot = (r === 1 && c === 4) || (r === 2 && c === 6) || (r === 3 && c === 2);
        const m = new THREE.Mesh(
          new RoundedBoxGeometry(0.82, 0.38, 0.82, 3, 0.12),
          hot ? M.green() : M.dark(),
        );
        m.position.set((c - 4.5) * 0.95 + r * 0.2, 0, (r - 1.5) * 0.95);
        grp.add(m);
        caps.push([m, r * 10 + c, hot]);
      }
    const plate = new THREE.Mesh(new RoundedBoxGeometry(10.6, 0.3, 4.4, 3, 0.15), M.chrome());
    plate.position.y = -0.32;
    grp.add(plate);
    camera.position.set(0, 5.5, 6.5);
    camera.lookAt(0, 0, 0);
    return (t, p) => {
      const R = rng(Math.floor(t * 9) + 1);
      caps.forEach(([m, i, hot]) => {
        const press = R() > 0.9 || (hot && Math.sin(t * 6 + i) > 0.6);
        m.position.y = press ? -0.14 : 0;
        if (hot) m.material = press ? M._n || (M._n = M.neon(G, 3)) : M._gg || (M._gg = M.green());
      });
      grp.rotation.y = -0.25 + p * 0.5;
      grp.scale.setScalar(0.001 + out(t / 0.9));
    };
  },
  // 15 graduation cap
  grad({ scene, camera }) {
    const grp = new THREE.Group();
    scene.add(grp);
    const board = new THREE.Mesh(new RoundedBoxGeometry(3.6, 0.16, 3.6, 3, 0.05), M.dark());
    board.rotation.y = Math.PI / 4;
    grp.add(board);
    const capb = new THREE.Mesh(new THREE.CylinderGeometry(1.2, 1.35, 1, 48, 1, true), M.dark());
    capb.position.y = -0.55;
    grp.add(capb);
    const button = new THREE.Mesh(new THREE.SphereGeometry(0.16, 20, 20), M.neon(G, 3));
    button.position.y = 0.14;
    grp.add(button);
    const tassel = new THREE.Mesh(new THREE.CylinderGeometry(0.035, 0.035, 1.6), M.neon(G, 2.5));
    tassel.position.set(1.8, -0.6, 0);
    grp.add(tassel);
    const tend = new THREE.Mesh(new THREE.ConeGeometry(0.16, 0.5, 16), M.neon(LIME, 3));
    tend.position.set(1.8, -1.5, 0);
    grp.add(tend);
    const parts = [];
    const R = rng(15);
    for (let i = 0; i < 40; i++) {
      const m = new THREE.Mesh(
        new THREE.OctahedronGeometry(0.08),
        M.neon(R() > 0.5 ? G : 0xffffff, 2),
      );
      scene.add(m);
      parts.push([m, R() * 6.28, 2 + R() * 2.5, R() * 3 - 1.5]);
    }
    return (t, p) => {
      grp.position.y = -3 * (1 - out(t / 1.2)) + Math.sin(t * 1.5) * 0.1;
      grp.rotation.set(0.35, t * 0.5, 0);
      parts.forEach(([m, a, r, y]) => {
        m.position.set(
          Math.cos(a + t * 0.7) * r,
          y + Math.sin(t + a) * 0.3,
          Math.sin(a + t * 0.7) * r,
        );
        m.rotation.set(t, t, 0);
        m.scale.setScalar(out((t - 0.8) / 0.8) + 0.001);
      });
      camera.position.z = 9 - p * 1.2;
      camera.position.y = 0.6;
    };
  },
  // 16 glitch shards
  shards({ scene, camera }) {
    const R = rng(16),
      list = [];
    for (let i = 0; i < 70; i++) {
      const m = new THREE.Mesh(
        new THREE.TetrahedronGeometry(0.2 + R() * 0.5),
        R() > 0.6 ? M.neon(G, 2) : R() > 0.5 ? M.white() : M.dark(),
      );
      const dir = new THREE.Vector3(R() - 0.5, R() - 0.5, R() - 0.5).normalize();
      scene.add(m);
      list.push([m, dir, 0.6 + R() * 1.2, R() * 6]);
    }
    const core = new THREE.Mesh(new THREE.IcosahedronGeometry(1.2, 0), M.green());
    scene.add(core);
    return (t) => {
      const burst = out((t - 1.2) / 1.4);
      list.forEach(([m, d, sp, o]) => {
        m.position.copy(d).multiplyScalar(1.3 + burst * sp * 4.5);
        m.rotation.set(t * sp + o, t * 0.7, o);
      });
      core.scale.setScalar(t < 1.2 ? 0.5 + out(t / 1.2) * 0.8 : 1.3 - burst * 1.29);
      core.rotation.set(t, t * 1.3, 0);
      camera.position.set(Math.sin(t * 13) * 0.04 * (t > 1.1 && t < 1.5 ? 1 : 0), 0, 9);
    };
  },
  // 17 smartphone with incoming messages
  phone({ scene, camera }) {
    const grp = new THREE.Group();
    scene.add(grp);
    const body = new THREE.Mesh(new RoundedBoxGeometry(2.4, 4.8, 0.28, 6, 0.32), M.dark());
    grp.add(body);
    const screen = new THREE.Mesh(
      new RoundedBoxGeometry(2.15, 4.5, 0.05, 4, 0.22),
      new THREE.MeshStandardMaterial({ color: 0x041207, emissive: 0x06200b, emissiveIntensity: 1 }),
    );
    screen.position.z = 0.15;
    grp.add(screen);
    const msgs = [];
    for (let i = 0; i < 5; i++) {
      const right = i % 2 === 1,
        m = new THREE.Mesh(
          new RoundedBoxGeometry(1.35, 0.5, 0.06, 3, 0.2),
          right ? M.neon(G, 1.4) : M.white(),
        );
      m.position.set(right ? 0.3 : -0.3, 1.6 - i * 0.72, 0.2);
      grp.add(m);
      msgs.push(m);
    }
    return (t, p) => {
      grp.rotation.y = -0.45 + Math.sin(t * 0.6) * 0.25 + (1 - out(t / 1)) * 1.2;
      grp.rotation.x = -0.08;
      grp.position.y = Math.sin(t * 1.2) * 0.08;
      msgs.forEach((m, i) => m.scale.setScalar(0.001 + back((t - 0.8 - i * 0.55) / 0.45)));
      camera.position.z = 8.5 - p;
    };
  },
  // 18 gift box opening
  gift({ scene, camera }) {
    const grp = new THREE.Group();
    scene.add(grp);
    const box = new THREE.Mesh(new RoundedBoxGeometry(2.4, 2, 2.4, 4, 0.1), M.green());
    grp.add(box);
    const lid = new THREE.Mesh(new RoundedBoxGeometry(2.6, 0.45, 2.6, 4, 0.1), M.green());
    grp.add(lid);
    const rib1 = new THREE.Mesh(new THREE.BoxGeometry(0.35, 2.05, 2.45), M.white());
    grp.add(rib1);
    const rib2 = new THREE.Mesh(new THREE.BoxGeometry(2.45, 2.05, 0.35), M.white());
    grp.add(rib2);
    const lidr = new THREE.Mesh(new THREE.BoxGeometry(0.36, 0.5, 2.65), M.white());
    lid.add(lidr);
    const beam = new THREE.Mesh(
      new THREE.CylinderGeometry(0.2, 1.1, 5, 32, 1, true),
      new THREE.MeshBasicMaterial({
        color: G,
        transparent: true,
        opacity: 0.35,
        side: THREE.DoubleSide,
      }),
    );
    beam.position.y = 3.4;
    grp.add(beam);
    const R = rng(18),
      conf = [];
    for (let i = 0; i < 50; i++) {
      const m = new THREE.Mesh(
        new THREE.BoxGeometry(0.12, 0.12, 0.02),
        M.neon(R() > 0.5 ? G : 0xffffff, 2),
      );
      grp.add(m);
      conf.push([m, (R() - 0.5) * 4, 3 + R() * 4, (R() - 0.5) * 4]);
    }
    grp.position.y = -1;
    return (t, p) => {
      const open = out((t - 1.2) / 0.6);
      lid.position.set(open * 1.2, 1.2 + open * 2.2, 0);
      lid.rotation.z = -open * 0.8;
      beam.scale.set(0.001 + open, 0.001 + open, 0.001 + open);
      beam.material.opacity = 0.35 * open;
      conf.forEach(([m, vx, vy, vz]) => {
        const lt = Math.max(0, t - 1.25);
        m.visible = t > 1.25;
        m.position.set(vx * lt, 1 + vy * lt - 2.2 * lt * lt, vz * lt);
        m.rotation.set(lt * 6, lt * 4, 0);
      });
      grp.rotation.y = t * 0.5;
      grp.scale.setScalar(0.001 + 0.62 * back(t / 0.8));
      if (t < 1.2) grp.rotation.z = Math.sin(t * 30) * 0.03 * clamp(t - 0.6);
      else grp.rotation.z = 0;
      camera.position.set(0, 1.5, 9 - p);
      camera.lookAt(0, 0.5, 0);
    };
  },
  // 20 particle wave field
  wave({ scene, camera }) {
    const W = 90,
      H = 50,
      n = W * H,
      pos = new Float32Array(n * 3);
    const g = new THREE.BufferGeometry();
    g.setAttribute("position", new THREE.BufferAttribute(pos, 3));
    const pts = new THREE.Points(
      g,
      new THREE.PointsMaterial({ color: G, size: 0.07, transparent: true, opacity: 0.95 }),
    );
    scene.add(pts);
    const orb = new THREE.Mesh(new THREE.SphereGeometry(0.9, 48, 48), M.green());
    orb.position.y = 1.6;
    scene.add(orb);
    camera.position.set(0, 3.2, 9);
    camera.lookAt(0, 0, 0);
    return (t, p) => {
      for (let i = 0; i < W; i++)
        for (let j = 0; j < H; j++) {
          const k = (i * H + j) * 3,
            x = (i - W / 2) * 0.2,
            z = (j - H / 2) * 0.2,
            d = Math.hypot(x, z);
          pos[k] = x;
          pos[k + 1] = Math.sin(d * 1.3 - t * 3.2) * 0.4 * Math.exp(-d * 0.08) * out(t / 1.2) - 0.8;
          pos[k + 2] = z;
        }
      g.attributes.position.needsUpdate = true;
      orb.scale.setScalar(0.001 + back((t - 0.4) / 0.8) * (1 + 0.08 * Math.sin(t * 6.4)));
      camera.position.set(Math.sin(t * 0.35) * 2.5, 3.2 - p, 9 - p * 1.5);
      camera.lookAt(0, 0.3, 0);
    };
  },
};

export async function mount3D({ canvas, w, h, start = 0, kind, opts = {}, bloom = 1.0, fov = 38 }) {
  const el = typeof canvas === "string" ? document.getElementById(canvas) : canvas;
  const renderer = new THREE.WebGLRenderer({
    canvas: el,
    antialias: true,
    preserveDrawingBuffer: true,
  });
  renderer.setPixelRatio(1);
  renderer.setSize(w, h, false);
  renderer.toneMapping = THREE.ACESFilmicToneMapping;
  renderer.toneMappingExposure = 0.8;
  const scene = new THREE.Scene();
  scene.background = new THREE.Color(BG);
  scene.fog = new THREE.Fog(BG, 14, 40);
  const pm = new THREE.PMREMGenerator(renderer);
  scene.environment = pm.fromScene(new RoomEnvironment(), 0.04).texture;
  scene.environmentIntensity = 0.45;
  const camera = new THREE.PerspectiveCamera(fov, w / h, 0.1, 200);
  camera.position.set(0, 0, 9);
  if (h > w) camera.position.z *= 1.0;
  const key = new THREE.DirectionalLight(0xffffff, 1.4);
  key.position.set(4, 6, 8);
  scene.add(key);
  const rim = new THREE.PointLight(G, 30, 30);
  rim.position.set(-5, 2, -3);
  scene.add(rim);
  const fill = new THREE.PointLight(LIME, 10, 25);
  fill.position.set(5, -3, 4);
  scene.add(fill);
  scene.add(new THREE.HemisphereLight(0xcfffc0, 0x020a04, 0.25));
  stars(scene, 700, 40, 5);
  const font = opts.font ? await loadFont(opts.font) : null;
  const update = KINDS[kind]({ scene, camera, opts, font, THREE });
  const composer = new EffectComposer(renderer);
  composer.setPixelRatio(1);
  composer.setSize(w, h);
  composer.addPass(new RenderPass(scene, camera));
  composer.addPass(new UnrealBloomPass(new THREE.Vector2(w / 2, h / 2), 0.55 * bloom, 0.45, 0.72));
  composer.addPass(new OutputPass());
  const dur = opts.dur || 6;
  const portrait = h > w;
  const renderAt = (time) => {
    if (time < start - 0.05 || time > start + dur + 0.05) return;
    const t = Math.max(0, time - start);
    update(t, clamp(t / dur));
    if (portrait) {
      camera.zoom = opts.zoom || 0.62;
      camera.updateProjectionMatrix();
    }
    composer.render();
  };
  window.addEventListener("hf-seek", (e) => renderAt(e.detail.time));
  update(0, 0);
  composer.render();
  renderAt(window.__hfThreeTime || 0);
  return renderAt;
}
