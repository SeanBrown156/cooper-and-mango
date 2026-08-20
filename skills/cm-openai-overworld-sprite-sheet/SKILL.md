---
name: cm-openai-overworld-sprite-sheet
description: Generate a consistent provisional pixel-art four-direction overworld sheet with intermediate movement phases from character references.
---

# CM OpenAI Overworld Sprite Sheet

Use this for overworld-only generation or for extracting/refining the
overworld region of a character-wide master sheet.

1. Read `CHARACTER_VISUAL_BRIEF.md`, the character contract, art bible, all relevant references, and the
   existing master sheet if one exists.
2. Prefer the master sheet as the likeness source. Preserve a consistent
   footprint, baseline, tail, ears, markings, and signature accessory.
3. Require a strict directional grid: north/back, south/front, east/right,
   and west/left, with multiple phases per direction such as contact, passing,
   opposite contact, and idle/bob.
4. Keep the character a readable low top-down orthographic overworld figure;
   avoid battle staging, perspective, isometric projection, horizon lines, and
   unrelated scenery.
5. Require hard-edged square pixel clusters, limited palette, no antialiasing,
   blur, photorealism, painterly gradients, text, labels, UI, or presentation
   board layout.
6. Save the provisional result under `assets/characters/<character>/overworld/02_input/`.
   Never overwrite an existing candidate; use a versioned name.
7. Send selected static overworld candidates through
   `$cm-prepare-role-resolution` for the governed **20×16** target before
   PixelLab refinement. If a provider cannot preserve that target, route to
   manual redraw or the OpenAI path; do not silently substitute another size.
   Do not normalize, recolour, or promote to WIP here.

The output is an overworld input sheet for later extraction and cleanup, not
final SpriteFrames.
