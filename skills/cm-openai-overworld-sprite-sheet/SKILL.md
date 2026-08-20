---
name: cm-openai-overworld-sprite-sheet
description: Generate a consistent provisional pixel-art four-direction overworld sheet with intermediate movement phases from character references; use only when the user explicitly requests an overworld-only sheet.
---

# CM OpenAI Overworld Sprite Sheet

Use this only when the user explicitly requests an overworld-only sheet or
explicitly invokes this skill. It is not the default for a generic sprite-sheet
request; generic requests use `$cm-openai-master-sprite-sheet` to generate one
master canvas first.

1. Read `CHARACTER_VISUAL_BRIEF.md`, the character contract, art bible, all relevant references, and the
   existing master sheet if one exists.
2. Prefer the master sheet as the likeness source. Preserve a consistent
   footprint, baseline, tail, ears, markings, and signature accessory.
3. For animal characters, require a strict quadruped/all-fours overworld
   grammar by default. The character must walk and idle on four legs; do not
   use bipedal battle stances or upright poses unless the user explicitly
   provides an exception for that character/species.
4. Require a strict directional grid: north/back, south/front, east/right,
   and west/left, with multiple phases per direction such as contact, passing,
   opposite contact, and idle/bob. Preserve a consistent ground contact,
   quadruped footprint, tail, ears, markings, and explicitly requested outfit
   states in every cell. For Mango, the required outfit groups are hoodie-up,
   hoodie-down, and no hoodie worn at all.
5. Keep the character a readable low top-down orthographic overworld figure;
   avoid battle staging, perspective, isometric projection, horizon lines, and
   unrelated scenery.
6. Require hard-edged square pixel clusters, limited palette, no antialiasing,
   blur, photorealism, painterly gradients, text, labels, UI, or presentation
   board layout. Require a solid opaque pure-white background; never use
   transparency, checkerboards, black backgrounds, coloured backgrounds, or
   background scenery.
7. Save the provisional result under `assets/characters/<character>/overworld/02_input/`.
   Never overwrite an existing candidate; use a versioned name.
8. Send selected static overworld candidates through
   `$cm-prepare-role-resolution` for the governed directional targets (**16×20
   north/south, 20×16 east/west**) before
   PixelLab refinement. If a provider cannot preserve that target, route to
   manual redraw or the OpenAI path; do not silently substitute another size.
   Do not normalize, recolour, or promote to WIP here.

The output is an overworld input sheet for later extraction and cleanup, not
final SpriteFrames.
