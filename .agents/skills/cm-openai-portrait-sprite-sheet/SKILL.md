---
name: cm-openai-portrait-sprite-sheet
description: Generate a consistent provisional pixel-art portrait expression sheet from character references, using a master sheet as the preferred consistency source; use only when the user explicitly requests a portrait-only sheet.
---

# CM OpenAI Portrait Sprite Sheet

Use this only when the user explicitly requests a portrait-only sheet or
explicitly invokes this skill. It is not the default for a generic sprite-sheet
request; generic requests use `$cm-openai-master-sprite-sheet` to generate one
master canvas first.

1. Read `CHARACTER_VISUAL_BRIEF.md`, the character contract, art bible, all relevant references, and the
   existing master sheet if one exists.
2. Prefer editing or extracting from the master sheet so portrait likeness and
   accessories stay consistent with battle and overworld assets.
3. If a new generation is necessary, make one grid containing multiple
   expressions with identical framing and scale: neutral, gentle, worried,
   shocked, sad, determined, defiant, angry, relieved, proud, and brave.
4. Preserve all defining markings and props. Require hard-edged square pixel
   clusters, limited palette, no antialiasing, blur, photorealism, painterly
   gradients, text, labels, or decorative board layout. Require a solid opaque
   pure-white background; never use transparency, checkerboards, black
   backgrounds, or other background colours.
5. Save the provisional result under `assets/characters/<character>/portrait/02_input/`.
   Never overwrite an existing candidate; use a versioned name.
6. Send selected static portrait candidates through
   `$cm-prepare-role-resolution` for the governed **40×40** target before
   PixelLab refinement. Do not normalize, recolour, or promote to WIP here.

The output is a portrait input sheet for later cleanup, not final SpriteFrames.
