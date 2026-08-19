---
name: cm-pixellab-portraits
description: Create consistent Cooper & Mango portrait candidates from character art and real-pet references while preserving the 48×48 role contract.
---

# CM PixelLab Portraits

Use for bust/portrait art or portrait/character conversion, not overworld
movement sheets or battle animations.

- Portrait role size is **48×48**. Larger renders are provisional source for
  Aseprite cleanup. Preserve Mango/Cooper likeness, markings and expressions.
- Use `create_portrait_character` for conversion: `character_to_portrait` for
  a bust from a sprite, `portrait_to_character` for the reverse, preferably
  with `image_url` and `result_size=48`. This is asynchronous; poll with
  `get_portrait_character` and inspect crop, transparency, likeness and size.
- Use `create_image_pro` only for a genuinely new static portrait direction;
  label references and use a transparent background. It costs more than
  conversion and is not a replacement when an identity anchor exists.

Generation output starts in `input/`. Cleanup, palette enforcement, cropping
and expression iteration belong in the family's `wip/` complete package. A
portrait `.png`/`.aseprite` may be accompanied by `.tres` data or `.tscn` UI
when the game actually treats it as reusable. Only the complete reviewed
package moves to `approved/`. Record source, direction, size, job ID, prompt
and review outcome. Read `docs/art/ART_BIBLE.md` first.
