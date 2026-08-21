---
name: cm-normalize-animation-frames
description: Normalize generated PNG sheets or extracted video frames into fixed Cooper & Mango sprite frames with stable pivots, baselines, bounds, nearest-neighbour scaling, and validation.
---

# CM Normalize Animation Frames

Use after selected-cell extraction and role-resolution preparation, and again
after Image, video, PixelLab, or manual animation work before approval or Godot
integration.

## Workflow

1. Determine the role contract from the owning manifest: frame size, frame
   count, columns, baseline, pivot, body height, and palette.
2. Put only user-selected source PNGs or generated frames in a temporary or
   package `input/`/`02_input/` folder. Do not normalize an entire master sheet.
3. For character animations, identify each frame’s head and feet landmarks
   before normalization. The body landmarks define scale and contact; the full
   alpha bounds may include an attack weapon, tail, scarf, or other effect.
4. Run:

   ```sh
     python3 tools/shared/frames_normalize.py input_frames/ output_frames/ \
     --width 24 --height 16 --columns 4 --baseline 15 \
     --landmarks landmarks.json --target-body-height 13 --target-pivot-x 12
   ```

5. Inspect the exported frames and sheet at native 1× scale.
6. Run `tools/shared/asset_validate.py` for dimensions, visible pixels, transparency, and
   palette membership.
7. Record body bounds, effect bounds, pivot/baseline decisions, and any rejected
   frames in the manifest.

Normalization is the resolution gate before PixelLab refinement and animation.
Normalization must not scale each frame independently to its canvas. Keep the
head-to-feet body height and foot contact stable; allow an attack weapon, tail,
scarf, or other effect to extend outside the body bounds. Reject ambiguous
landmarks rather than silently guessing. For non-character props, a simpler
center/baseline placement is acceptable.
