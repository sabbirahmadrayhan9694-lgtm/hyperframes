# Sabbir Rayhan Academy video series

Twenty HyperFrames videos (12 at 16:9, 8 at 9:16) for Sabbir Rayhan Academy, built on one shared brand system.

## Layout

- `_vendor/brand.css`: brand colors, cards, pills, and `@font-face` rules for the local fonts
- `_vendor/helpers.js`: seek-safe helpers (`typeText`, `countUp`, `splitWords`, `BN` digits) and the inline icon set
- `_vendor/sr3d.js`: a deterministic Three.js scene kit, driven by `hf-seek`, with 20 scene kinds
- `_vendor/fonts`, `_vendor/sfx`: Hind Siliguri, Poppins, and the repo's sound effects
- `vNN/src.html`: one video's source (meta, style, body, script, and module sections)
- `build.mjs`: turns `vNN/src.html` into a renderable `vNN/index.html` and copies its assets

## Kept local (not committed)

- `_vendor/lib/`: gsap 3.14.2 and three 0.181.2 (the build copies `three.module.js`, `three.core.js`, the needed `examples/jsm` addons, and `helvetiker_bold.typeface.json`). Restore them with `npm pack gsap@3.14.2 three@0.181.2`.
- `_vendor/media/`, `_vendor/logo-*.png`: the user's personal photos, screenshots, voiceovers, and logo.

## Build and render

```bash
node sr-academy/build.mjs v01
cd sr-academy/v01
node ../../packages/cli/bin/hyperframes.mjs lint
node ../../packages/cli/bin/hyperframes.mjs render -o renders/v01.mp4 --quality delivery
```
