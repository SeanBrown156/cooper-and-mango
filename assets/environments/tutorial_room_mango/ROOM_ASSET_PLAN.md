# Mango tutorial room — build plan

Status: specification and generation ledger complete; new generation not yet run.

The detailed source analysis, orientation rules, pixel dimensions, and acceptance
criteria now live in [`ENVIRONMENT_SPEC.md`](ENVIRONMENT_SPEC.md). The complete
machine-readable tile and sprite ledger is
[`../../../tools/pixellab_tutorial_room_spec.json`](../../../tools/pixellab_tutorial_room_spec.json).

## Locked decisions

- Gemini controls the room composition; photographs control object identity and
  materials.
- The room is 512×384 px: 32×24 cells on the 16×16 world grid.
- The 480×270 camera views the room without stretching it.
- Environments use orthographic high top-down projection.
- Day is the canonical material pass. Dawn, dusk, and night are lighting layers,
  not separately redrawn rooms.
- Floor furniture that reads as oblique, isometric, side-on, or three-quarter is a
  failed result regardless of canvas size.

## Generation order

1. Shell building kit and timber-floor↔rug transition tiles.
2. Window/curtain and exit-door architecture overlays.
3. P0 composition anchors: bed, rug, table, four chair directions, pendant, cat
   tree, carved chest, Filipino flag/banner, and clothes rack.
4. P1 identity dressing: wall shelves/art, plants, pet corner, purple hoodie, and
   sleeping Mango.
5. Dawn/day/dusk/night lighting implementation.
6. Aseprite cleanup, Godot collision/sorting test, and human approval.

## Completion gates

- [x] Reference and Gemini source hierarchy locked.
- [x] Projection and cardinal orientation locked.
- [x] Room, tile, atlas, canvas, bounds, and footprint dimensions recorded.
- [x] Tile-set ledger created.
- [x] Sprite ledger created.
- [x] PixelLab request descriptions and batch order created.
- [ ] New shell batch generated and reviewed.
- [ ] New P0 anchor batch generated and reviewed.
- [ ] Room assembled at native size in Godot.
- [ ] Collision, sorting, camera, and four light states verified.
- [ ] Approved art promoted out of WIP.

Historical PixelLab attempts and their IDs remain in
[`PIXELLAB_JOBS.md`](PIXELLAB_JOBS.md). They are evidence, not inputs to the new
manifest; their orientation failures must not be reintroduced.
