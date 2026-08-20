---
name: cm-openai-animation-sheet
description: Generate action or pose spritesheets from one canonical anchor with OpenAI Image; use for idle, attack, hurt, crouch, death, and other non-locomotion actions where a single image call can fill a padded frame grid.
---

# CM OpenAI Animation Sheet

Use one selected, resolution-prepared anchor plus one padded, labelled
frame-grid canvas. Do not call the
image model independently for every frame because identity and proportions will
drift.

## Workflow

1. Read the owning package contract and select the canonical anchor directly.
2. Validate the anchor before generation: confirm its role dimensions, visible
   bounds, transparency, pivot, baseline, palette direction, and identity
   markings. The anchor is the identity reference, not merely an arbitrary
   first frame.
3. Create a larger transparent working canvas with one cell per intended frame.
   Place the actual target-size pixel anchor into one cell and leave the other
   cells blank. Do not enlarge the anchor independently. If the API needs a
   larger working image, scale the complete blank grid with nearest-neighbour
   after placement so every cell and pixel keeps the same proportions. Use:

   ```sh
   python3 tools/shared/animation_canvas.py anchor.png animation_canvas.png \
     --columns 4 --rows 1 --cell-width 20 --cell-height 16 --scale 8
   ```

   The scaled canvas is only a generation template. The game target remains the
   manifest’s exact frame size, such as 20×16 or 32×32.
4. Edit the template with `tools/openai/image_generate.py --image animation_canvas.png`;
   describe the action as ordered beats and state the unchanged identity
   invariants.
5. Save the complete raw sheet and metadata in `input/`.
6. Extract the intended cells, then run `$cm-normalize-animation-frames`.
7. Validate body baseline, pivot, body scale, effect bounds, frame count,
   palette, and loop continuity.
8. Compare the candidate in Godot against PixelLab, procedural, and video
   variants before placing it in WIP. Only a human-reviewed, tested package
   moves from WIP to approved.

The model may still shift cell boundaries, add extra frames, or drift from the
anchor. Treat the returned sheet as raw material: crop by the intended grid,
reject unusable cells, and normalize every accepted frame.

Best uses are crouch, attack, hurt, death, idle, and other pose-led actions.
Use `$cm-openai-video-to-sprite` for walk/run cycles where limb timing and
locomotion continuity are the dominant problem.
