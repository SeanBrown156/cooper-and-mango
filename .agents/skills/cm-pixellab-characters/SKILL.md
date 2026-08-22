---
name: cm-pixellab-characters
description: Create or extend Cooper & Mango playable-character, NPC, and battle sprite candidates with PixelLab while preserving orthogonal directions, role sizes, likeness references, and the asset lifecycle.
---

# CM PixelLab Characters

Use for a new or revised character sprite after the user has selected numbered
cells from a master review sheet. Do not send an entire unreviewed sheet or all
cells to PixelLab.

## Cooper & Mango contract

- The game is a 2D orthographic top-down RPG. Overworld characters walk only
  north, south, east and west. Never request eight-direction movement or
  diagonals for an overworld actor.
- Role frames are overworld **16×20 north/south and 20×16 east/west**, battle **32×32**, and portrait **40×40**.
  Larger PixelLab canvases are provisional input for Aseprite cropping/redraw.
- Prepare the selected source at the role's declared target size before this
  handoff where PixelLab accepts it. Use high reference influence so PixelLab
  refines the selected likeness rather than inventing a replacement.
- Mango and Cooper are real-pet likenesses. Use the relevant photos and any
  approved canonical sprite as references; describe markings and silhouette.
- Overworld is quadruped/low top-down. Battle art is an upright/bipedal
  presentation at 32×32; do not force the battle pose into the overworld view.

## Tool selection

1. Use `mcp__pixellab__create_character` for a character turnaround. Set
   `n_directions=4`, `view="low top-down"`, and `body_type="quadruped"` with
   the appropriate animal template. Standard mode is the economical first pass.
2. For battle candidates, prefer `create_image_pro` for a static pose with a
   labelled canonical reference, or use v3 only when its eight-direction
   limitation is acceptable for that battle asset.
3. Poll with `get_character` or `get_image`; never claim completion from a
   queued ID. Inspect every direction/candidate.

## Handoff

Put selected source cells and PixelLab raw outputs in the owning family's
`input/`/`02_input/` staging area. Once cleanup, cropping,
palette work or Godot wiring begins, keep the complete package in `wip/`:
`.aseprite`, `.png`, metadata, `.tres`, and `.tscn` where they exist. Only
human-reviewed, tested packages move to `approved/`; PixelLab never promotes
itself. Record master cell ID, source path, job ID, reference influence, prompt,
references, size and direction contract.

Read `docs/vision/GAME_BIBLE.md`, the owning
`assets/characters/<character>/CHARACTER_VISUAL_BRIEF.md`,
`docs/art/ART_BIBLE.md`, `docs/art/ART_PRODUCTION_PIPELINE.md`, and the owning
family's specification before generating. Stop if the request changes
role dimensions, adds diagonal overworld directions, or discards likeness.
