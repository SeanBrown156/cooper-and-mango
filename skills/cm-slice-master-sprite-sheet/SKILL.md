---
name: cm-slice-master-sprite-sheet
description: Slice a character-wide master pixel-art sprite-sheet canvas into preserved portrait, battle, and overworld input-region sheets without altering the master.
---

# CM Slice Master Sprite Sheet

Use this immediately after `$cm-openai-character-reference-input` generates a
master canvas, or when a manually selected master already exists.

1. Keep the master PNG and its sidecar metadata untouched in the character's
   general `shared/02_input/` folder.
2. Inspect the master at native size and determine the exact crop rectangle for
   each region, then create the numbered review copy with
   `tools/shared/label_sprite_sheet_review.py` if it does not already exist.
3. Ask for explicit IDs from the review copy. Do not write every cell by
   default. Use `tools/shared/extract_selected_sprite_cells.py` with the review
   JSON map and the selected IDs to write only accepted candidates into:
   `assets/characters/<character>/<role>/02_input/`.
4. Use `tools/shared/slice_master_sprite_sheet.py` only when a whole role-region
   sheet is also useful for context or later manual extraction.
5. Use versioned names tied to the master version and never overwrite an earlier
   candidate. Update the character-local manifest with selected IDs, crop boxes,
   source master, slice paths, dimensions, and review state.
6. Treat extracted cells as provisional input. Do not resize, normalize,
   recolour, animate, or promote to WIP here; those are later role-specific
   steps.

The master remains the canonical consistency source. The three slices are
derived working inputs for the portrait, battle, and overworld skills.
