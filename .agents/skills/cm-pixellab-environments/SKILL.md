---
name: cm-pixellab-environments
description: Create Cooper & Mango orthographic top-down environment tilesets, room assets, and map-object candidates with PixelLab and the 16px room contract.
---

# CM PixelLab Environments

Use for rooms, terrain, wall/floor atlases, Wang tilesets and environment
extensions. Use `$cm-pixellab-props` for a standalone object with a
silhouette.

Tilesets are room-agnostic packages under `assets/tilesets/<tileset_name>/`,
not bespoke per-room folders — a room references tileset IDs from its
`environment_manifest.json` rather than owning its own tile lifecycle. Raw
licensed pack downloads live in `assets/tilesets/shared/02_input/<pack_name>/`.

## Contract

- Rooms are 2D orthographic high top-down: no isometric, oblique, perspective,
  horizon or vanishing-point language. Native tile size is **16×16** with hard
  pixel edges. Tutorial Room is 512×384 (32×24 cells), camera 480×270.
- Default guidance is selective outline, flat shading, low detail, transparent
  object backgrounds, and no antialiasing/blur/glow. Use approved/WIP style
  references and explicit orientation/footprints.
- Use black or near-black outlines for foreground interactables. Use faded,
  lower-contrast outlines for passive/background scenery so it recedes.
- Use `create_topdown_tileset` for connected terrain; provide lower/upper
  descriptions and poll with `get_topdown_tileset`. Chain
  `lower_base_tile_id` for compatible terrain families.
- Use `create_map_object` for a standalone room object or style-matched
  inpaint. It returns a transparent cutout, not a room composition; include
  negative constraints in the description because there is no separate field.
- Never use isometric tools for Cooper & Mango rooms. The Tutorial Room
  manifest `assets/environments/tutorial_room_mango/environment_manifest.json`
  is mandatory for that room.

Raw results/licensed source stay in `02_input/`; remapped atlases, masters and
candidate TileSets stay together in the tileset package's own `03_wip/`. An
approved tileset package may contain atlas `.png`/`.aseprite` and TileSet
`.tres`. Room-level composition (which tilesets/items go where, the assembled
`.tscn`) lives in the owning `assets/environments/<room_name>/` package, not
here. Validate seams, walkability, collisions, camera readability, palette and
character contrast in Godot before approval. Record job IDs and prompts.
