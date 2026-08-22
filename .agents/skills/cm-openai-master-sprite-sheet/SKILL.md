---
name: cm-openai-master-sprite-sheet
description: Generate the default character-wide OpenAI GPT Image 2 master sprite-sheet canvas from references, containing portrait, battle, and overworld sections for later extraction; use for normal or generic sprite-sheet generation unless a role-specific sheet is explicitly requested.
---

# CM OpenAI Master Sprite Sheet

This is the default character sprite-sheet workflow. For a normal or generic
sprite-sheet request, use the OpenAI API to generate one character-wide master
canvas containing portrait, battle, and overworld sections together. Do not
generate separate overworld, portrait, or battle sheets in the generic case.
Those role-specific skills are opt-in and may be used only when the user
explicitly names or requests that role.

The master is provisional input, not final sprite production. It keeps
likeness and accessory decisions consistent before selected cells are sliced
into role-specific inputs.

## Workflow

1. Read `docs/vision/GAME_BIBLE.md`, the owning
   `CHARACTER_VISUAL_BRIEF.md`, `docs/art/ART_BIBLE.md`, the character package,
   all role-specific `01_reference/` folders, and any general references. Include unusual
   identity-defining props or toys as explicit image references.
2. Build one reference set from the whole character package. The generic output
   must be one master sheet, not independent portrait, battle, and overworld
   calls.
3. Use `tools/openai/image_generate.py` with `--model gpt-image-2`, passing the
   complete reference set. Ask for one large master canvas with a solid opaque
   pure-white background and three clearly separated but unlabelled regions:
   portrait expressions, battle poses, and overworld directions/movement.
   Explicitly prohibit transparency, checkerboards, black or coloured
   backgrounds, gradients, and background scenery.
4. For battle sections, preserve the requested body language. If the character
   is intended to stand or sit on two legs, require that explicitly in the
   battle region rather than allowing a purely quadrupedal interpretation.
5. Require visible pixel art: hard square clusters, limited palette, crisp
   edges, opaque pure-white background, no transparency, checkerboard, black or
   coloured background, antialiasing, blur, photorealism, painterly gradients,
   UI, text, or decorative presentation layout.
6. Save each clean master canvas as a new version in the character's general
   `shared/02_input/` folder. Record all source references, layout, model,
   prompt, and review state in the local manifest.
7. Immediately create a separate deterministic numbered review copy with
   `tools/shared/label_sprite_sheet_review.py`. Use role-prefixed IDs such as
   `P01`, `B04`, and `O12`. Never ask the image model to render the numbers.
8. Ask the user to select IDs from the review copy. Invoke
   `$cm-slice-master-sprite-sheet` with the master, review map, and selected
   IDs. It must extract only those cells into the relevant role `02_input/`
   folders; keep the master and review copy for provenance.
9. Do not normalize, recolour, animate, or promote assets here.

## Output contract

One giant provisional pixel-art master sheet containing all three role regions,
plus sidecar metadata and a manifest entry. The master is the consistency source
for later role-specific extraction.
