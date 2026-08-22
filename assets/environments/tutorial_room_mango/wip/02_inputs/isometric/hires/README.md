# PixelLab WIP exports

These exports are generated candidates for the blended Gemini living-room /
bedroom composition. They are not approved production art and are not wired
into the runtime scene yet.

The first batch in this folder is superseded for room use: it was generated on
oversized 128px canvases and reads as oblique/three-quarter furniture. Future
room generations must follow
`assets/environments/tutorial_room_mango/environment_manifest.json`, which now
contains the complete tile and sprite ledger: exact canvas, visible bounds,
footprint, pivot, cardinal facing, projection class, prompt, and batch order.

- `floor_to_geometric_rug_tileset.png`: 16-tile, 16px connected terrain sheet.
- `timber_plaster_building_kit.zip`: PixelLab building-kit package; extracted
  16px pieces are in `building_kit/`.
- The 16 named 128px PNGs are transparent object candidates for the room
  anchors and identity props described in `ROOM_ASSET_PLAN.md`.

Before wiring these into Godot, review them at native size, crop or slice them
to the project’s 16px grid, check palette and silhouette against the Gemini
composites and reference photos, then add collision/sorting metadata.

The corresponding PixelLab IDs and generation provenance are in
`../../../../PIXELLAB_JOBS.md`.
