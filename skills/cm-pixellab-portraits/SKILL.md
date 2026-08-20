---
name: cm-pixellab-portraits
description: Create consistent Cooper & Mango portrait candidates from character art and real-pet references while preserving the 40×40 role contract.
---

# CM PixelLab Portraits

Use for a user-selected portrait cell after master review and role-resolution
preparation. Read the owning `CHARACTER_VISUAL_BRIEF.md` first; do not use this
for an unreviewed sheet, overworld movement, or battle animation.

- Portrait role size is **40×40**. Use `$cm-prepare-role-resolution` before
  PixelLab when the selected source is larger. Preserve Mango/Cooper likeness,
  markings and expressions with high reference influence.
- Use `create_portrait_character` for conversion: `character_to_portrait` for
  a bust from a sprite, `portrait_to_character` for the reverse, preferably
  with `image_url` and `result_size=40`. This is asynchronous; poll with
  `get_portrait_character` and inspect crop, transparency, likeness and size.
- Use `create_image_pro` only for a genuinely new static portrait direction;
  label references and use a transparent background. It costs more than
  conversion and is not a replacement when an identity anchor exists.

Generation output starts in `input/`/`02_input/`. Cleanup, palette enforcement, cropping
and expression iteration belong in the family's `wip/` complete package. A
portrait `.png`/`.aseprite` may be accompanied by `.tres` data or `.tscn` UI
when the game actually treats it as reusable. Only the complete reviewed
package moves to `approved/`. Record source, direction, size, job ID, prompt
and review outcome. Read `docs/art/ART_BIBLE.md` first.
