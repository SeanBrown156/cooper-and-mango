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
5. Stop after producing the numbered review copy and JSON map. The user owns
   selection and manual slicing: never extract or write role-specific cells
   unless the user explicitly supplies selected IDs in the current instruction.
   When explicit IDs are supplied, use
   `tools/shared/extract_selected_sprite_cells.py` with the review JSON map and
   the selected IDs to write only accepted candidates into:
   `assets/characters/<character>/<role>/02_input/`.
6. Use `tools/shared/slice_master_sprite_sheet.py` only when a whole role-region
   sheet is also useful for context or later manual extraction.
7. Use versioned names tied to the master version and never overwrite an earlier
   candidate. Update the character-local manifest with selected IDs, crop boxes,
   source master, slice paths, dimensions, and review state.
8. Treat extracted cells as provisional input. Do not resize, normalize,
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
