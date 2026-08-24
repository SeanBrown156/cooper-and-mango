---
name: cm-openai-environment-sprite
description: Generate a provisional OpenAI GPT Image 2 orthographic pixel-art environment sprite from an environment reference folder; use for turning photos, sketches, mood boards, or existing art into a close reference point before building the real tileset and Godot scene.
---

# CM OpenAI Environment Sprite

Use this skill to translate the references belonging to one environment into an
actual pixel-art environment input. The output should be a usable pixel-art
build target, not a beautiful concept illustration, mood board, or presentation
sheet. It is still not a final tileset, atlas, scene, or collision map.

## Workflow

1. Identify `assets/environments/<environment_id>/` and read its local
   `environment_manifest.json` when present. Inspect all relevant references,
   especially the room's own `01_reference/`, plus any tileset/item packages
   already referenced by the manifest and clearly labelled source material.
   Do not use unrelated references from another environment.
2. Extract the environment’s non-negotiable facts: spatial layout, room
   boundaries, materials, architecture, important objects, lighting direction,
   colour relationships, and the project’s camera contract. For Cooper & Mango,
   default to 2D orthographic high top-down, 16×16 tile logic, no perspective,
   no isometric projection, no oblique camera, and no horizon.
3. Use `tools/openai/image_generate.py` with `--model gpt-image-2` and the
   selected reference images. Ask for the closest possible restrained pixel-art
   approximation of the environment as an actual game-art input: discrete
   square pixel clusters, hard pixel edges, limited palette, black outlines for
   foreground interactables, faded outlines for passive background scenery, flat
   controlled shading, clear walkable space, and a composition
   that can later be decomposed into tiles, props, and layers. Require a solid
   opaque pure-white background and explicitly prohibit transparency,
   checkerboards, black or coloured backgrounds, and gradients. Explicitly
   reject smooth illustration, painterly detail, photographic texture, blur,
   antialiasing, and decorative concept-art framing.
4. Generate a coherent pixel-art composition at a working resolution that
   preserves a visible 16×16 tile rhythm. Do not ask GPT Image 2 to solve the
   final atlas cells in this pass, but do require the result to read as pixel
   art at native inspection scale. If the source references include real
   photographs, preserve their meaningful layout and material cues while
   translating them into the game’s visual language rather than copying photo
   noise.
5. Save the raw image and sidecar metadata under the room's own
   `assets/environments/<environment_id>/wip/`, using a versioned name and
   never overwriting an existing study. This is whole-room composition
   ideation, not a tileset or item candidate — those get extracted afterward
   into their own `assets/tilesets/<name>/` or `assets/props/<name>/` package.
6. Inspect the study against the source references and environment manifest.
   Check camera, layout, visual hierarchy, tile-readability, and whether the
   result gives the team a useful build target. Record disagreements and
   uncertainties instead of silently “fixing” them.
7. Do not generate a Godot scene, tileset resource, collision map, final atlas,
   WIP package, or approved asset here. Hand the selected study to the
   PixelLab environment/props skills, manual tileset construction, or Godot
   composition workflow.

## Output contract

The result is one or more versioned pixel-art environment input candidates in
the room's `wip/`. Record model, prompt, source references, output path,
camera assumptions, tile rhythm, and review state in the environment-local
manifest.
