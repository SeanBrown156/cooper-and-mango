---
name: cm-pixellab-characters
description: Create or extend Cooper & Mango playable-character, NPC, and battle sprite candidates with PixelLab while preserving orthogonal directions, role sizes, likeness references, and the asset lifecycle.
---

# CM PixelLab Characters

Use for a new or revised character sprite, not animation-only, portrait-only,
environment, or prop requests.

## Cooper & Mango contract

- The game is a 2D orthographic top-down RPG. Overworld characters walk only
  north, south, east and west. Never request eight-direction movement or
  diagonals for an overworld actor.
- Role frames are overworld **24×16**, battle **32×32**, and portrait **48×48**.
  Larger PixelLab canvases are provisional input for Aseprite cropping/redraw.
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

Put raw outputs in the owning family's `input/`. Once cleanup, cropping,
palette work or Godot wiring begins, keep the complete package in `wip/`:
`.aseprite`, `.png`, metadata, `.tres`, and `.tscn` where they exist. Only
human-reviewed, tested packages move to `approved/`; PixelLab never promotes
itself. Record job ID, prompt, references, size and direction contract.

Read `docs/art/ART_BIBLE.md`, `docs/art/ART_PRODUCTION_PIPELINE.md`, and the
owning family's specification before generating. Stop if the request changes
role dimensions, adds diagonal overworld directions, or discards likeness.
