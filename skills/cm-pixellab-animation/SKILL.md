---
name: cm-pixellab-animation
description: Create and validate Cooper & Mango character idle and walk animations in PixelLab using four orthogonal directions, fixed role bounds, and complete WIP packages.
---

# CM PixelLab Animation

Use for motion on an existing, user-selected and resolution-prepared character
identity. Read the owning `CHARACTER_VISUAL_BRIEF.md` first. Use
`$cm-pixellab-characters` when the character itself does
not exist. Do not animate every cell from a master sheet.

## Contract and workflow

- Overworld animation is strictly `north`, `south`, `east`, `west`; no
  diagonals or eight-direction movement. Preserve role bounds: overworld
  16×20 for north/south and 20×16 for east/west, battle 32×32, portrait 40×40. Frames share baseline, pivot and
  visible bounds; PixelLab must not invent markings or limbs per frame.
- Inspect the character with `get_character` and identify the character ID and
  available templates.
- Confirm the selected static anchor, target dimensions, baseline, and pivot
  before spending a PixelLab animation generation.
- Prefer `animate_character(mode="template", template_animation_id=...)` for
  standard idle/walk/run templates. Use `mode="v3"` for custom actions or a
  small reroll, passing explicit four directions, frame count 4/8/16, and a
  concise motion description.
- Use pro only after template/v3 fail. Call once without `confirm_cost=true`,
  then confirm deliberately; it is expensive and has fixed frame behavior.
- Poll `get_character` until complete and inspect every direction for identity,
  baseline, foot contact and loop continuity. Delete and retry poor output.

## Handoff

Save raw results in `input/`; once editing starts, keep the complete current
package in the family's `wip/`: source `.aseprite`, exported sheet(s),
metadata, `SpriteFrames` `.tres`, and actor `.tscn` where applicable. Promote
the whole tested package to `approved/`, never just the PNG. Record job ID,
character ID, animation/template, directions, frame count, size and review.

If PixelLab cannot accept the declared target size or cannot preserve the
selected reference, route the candidate to the OpenAI video/image animation
workflow or the simple Python pixel-animation workflow. Do not alter the role
contract silently.

Read the owning family spec and Art Bible before spending generations.
