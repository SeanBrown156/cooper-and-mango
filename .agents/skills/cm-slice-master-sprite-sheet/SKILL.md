---
name: cm-slice-master-sprite-sheet
description: Slice a character-wide master pixel-art sprite-sheet canvas into preserved portrait, battle, and overworld input-region sheets without altering the master.
---

# CM Slice Master Sprite Sheet

Use this immediately after `$cm-openai-master-sprite-sheet` generates a
master canvas, or when a manually selected master already exists.

1. Keep the master PNG and its sidecar metadata untouched in the character's
   general `shared/02_input/` folder.
2. Inspect the master at native size before defining any cells. Determine each
   candidate sprite's actual content bounds, including tails, ears, weapons,
   clothing, effects, shadows, and other intentional parts of the sprite.
   Equal-width/equal-height grid boxes are forbidden for an AI-generated sheet
   unless visual inspection confirms that every candidate is fully contained by
   its box and separated from its neighbours.
3. Validate every candidate crop. If a sprite touches a proposed boundary,
   crosses into a neighbouring candidate, is only partly visible, or cannot be
   separated confidently from an adjacent effect or sprite, stop and repair the
   cell map before numbering. Do not create a review map from guessed geometry.
4. Create the numbered review copy with
   `tools/shared/label_sprite_sheet_review.py` only after the verified crop map
   exists. The JSON map must contain the exact extraction `box` for each label;
   the numbered PNG is only a visual index and is never an extraction source.
   Note that this script always divides a region into an *equal* grid — it
   does not itself detect or correct content bleeding across a cell boundary.
5. Before extracting, run
   `tools/shared/preview_sprite_cells.py --master <master> --review-map
   <review.json> --select <IDs> --out <preview.png>` and actually look at the
   output (e.g. with the Read tool). It tiles each candidate cell with a
   margin of surrounding context and outlines the candidate box in red, so a
   sprite bleeding into a neighbour is visibly still bleeding past the line,
   while a cleanly bounded cell shows a gap of background between the box
   edge and the next sprite. Pixel-difference heuristics (background-vs-
   content, colour continuity across the seam) were tried and do not work
   reliably on this project's dithered/noisy AI-generated art — both a clean
   fill-the-frame sprite and an actual neighbour-bleed read the same way to
   that kind of check. Only a visual look, via this tool, is reliable; do not
   skip it and do not extract a cell that has not been previewed this way. If
   a cell shows bleed, its box needs tightening (or the sheet needs a
   verified, non-uniform crop map per step 3) before it is re-numbered and
   re-previewed — do not extract a flagged cell as-is.
6. Stop after producing the numbered review copy and JSON map. The user owns
   selection and manual slicing: never extract or write role-specific cells
   unless the user explicitly supplies selected IDs in the current instruction.
   When explicit IDs are supplied, preview them (step 5), then use
   `tools/shared/extract_selected_sprite_cells.py` with the review JSON map and
   the selected IDs to write only accepted candidates into:
   `assets/characters/<character>/<role>/02_input/`.
7. Use `tools/shared/slice_master_sprite_sheet.py` only when a whole role-region
   sheet is also useful for context or later manual extraction.
8. Use versioned names tied to the master version and never overwrite an earlier
   candidate. Update the character-local manifest with selected IDs, crop boxes,
   source master, slice paths, dimensions, and review state.
9. Treat extracted cells as provisional input. Do not resize, normalize,
   recolour, animate, or promote to WIP here; those are later role-specific
   steps.

The master remains the canonical consistency source. Extracted cells are
derived working inputs for the portrait, battle, and overworld skills. If the
sheet cannot support trustworthy verified bounds, leave the master and review
artifacts untouched and report the geometry problem instead of slicing.

## Canonical destinations

The canonical staging folder is always `02_input` (singular):

| Selected role | Destination |
| --- | --- |
| Portrait | `assets/characters/<character>/portrait/02_input/` |
| Battle | `assets/characters/<character>/battle/02_input/` |
| Overworld | `assets/characters/<character>/overworld/02_input/` |

Do not create new outputs in legacy `02_inputs/`, `02_portrait/`, or other
role-specific naming variants. Existing legacy folders may be preserved for
history, but they are not valid destinations for new slices.

Sidecar JSON produced by `extract_selected_sprite_cells.py` (and every other
generation/slicing script) lands in a `meta/` subfolder next to the image, not
beside it directly — see `docs/art/ART_PRODUCTION_PIPELINE.md` §10.1. Do not
write `.json` sidecars directly into `02_input/`.

## Overworld direction subfolders

Overworld cells are directional; a flat `02_input/` listing mixes north, south,
and side-facing frames together. When extracting overworld cells, pass
`--subfolder north`, `--subfolder south`, or `--subfolder west` to
`extract_selected_sprite_cells.py` so output lands in
`overworld/02_input/{north,south,west}/`. There is no `east/` output — east is
produced at runtime by horizontally mirroring the west frames, since the art
only ever renders one side-facing direction.

When numbering a *new* master sheet's overworld region with
`label_sprite_sheet_review.py`, name the region argument with a direction
suffix (e.g. `overworld-north:x0,y0,x1,y1:columns:rows`) rather than a bare
`overworld:...`. The script derives the cell-label prefix from each
hyphen-separated word (`overworld-north` → `ON`, `overworld-south` → `OS`,
`overworld-west` → `OW`, `overworld-east` → `OE`), so cells come out numbered
`ON01`, `OS01`, `OW01`, etc. instead of an undifferentiated `O01`–`O16` run.
This only applies to sheets numbered after this convention was adopted —
existing review maps keep their original flat `O01`–`O16` labels; map those to
directions manually by inspecting the sheet (as was done for Cooper's v2/v3/v4
masters) rather than renumbering an already-approved review map.
