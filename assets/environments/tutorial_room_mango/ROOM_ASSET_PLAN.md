# Mango tutorial room — asset audit and build plan

Status: audit complete; room-specific build not yet approved as final art.

## Reference audit

The reference images in `reference/` identify the real objects and materials.
The `input/tutorial_room-*.png` Gemini composites remain the intended blended
living-room/bedroom layout; they are not being replaced by a literal photo
reconstruction. Use the photos to make each composite object specific and
recognisable, while preserving the composite's designed placement and mood.

### Fixed room composition

- Back/left wall: a wide glass door or window covered by sheer white curtains,
  with a folding canvas chair and a leafy potted plant in front of it.
- Left wall: a wall-mounted TV on a long wooden media console, large speakers,
  a low drawer unit, a desk with monitor/laptop, and a black office chair.
- Left/upper wall: a freestanding clothes rack crowded with dark and coloured
  jackets, black wire bookshelves, and small floating book shelves.
- Upper/right wall: framed art and prints, including Buddhist/Japanese artwork,
  calligraphy, an illustrated landscape, and a large blue-white-red Filipino
  flag/banner.
- Centre-left: a deep-blue futon-style sofa/bed with white cushions, a cream
  throw, and a bright orange cushion.
- Centre: a cream rug with a repeated blue-grey and tan geometric grid.
- Centre/right: a square dining/work table with four cane-backed chairs and a
  black stone-look kitchen bench at the edge of the room.
- Centre/right foreground: a small wooden side table, a round wooden-lidded
  wastebasket, a pet bed, and a small metal pet bowl.
- Right wall: a tall green cat tree with multiple sisal platforms and beds;
  this is not a cactus.
- Right/entry wall: a carved wooden storage chest, shoe storage, a white door,
  wall hooks with tote bags and lanyards, and a small shelf for keys and books.
- Planting and details: a hanging trailing plant, potted palms/foliage, framed
  photos, books, headphones, desk lamp, and small ornaments.
- Floor: warm vertical wood planks with a restrained darker edge/shadow band.

### Lighting variants

The layout and material colours should remain stable across time-of-day variants.
Only the following should vary:

- outside/curtain colour and value;
- window glow and cast light from the glass door/window;
- overall room tint and shadow intensity;
- Noguchi-style paper pendant-lamp glow, which is strongest at night;
- small highlights on the floor, rug, bed, and furniture.

Day is the baseline palette. Dawn shifts toward soft pink/lilac. Dusk shifts
toward orange/ochre. Night uses a cool blue room with a warm pool of light at
the table.

## Existing source inventory

### PixelLab generation contract

All room props are native 16×16-grid assets. The target dimensions below are
the visible content bounds, not padded generation canvases. PixelLab requests
must use strict orthographic high top-down output by default: no oblique,
isometric, side, or visible front-face presentation unless a specific asset
explicitly calls for it.

PixelLab has a 32px minimum canvas for map objects, so a small prop may use a
32×32 transparent canvas but its visible art must remain within its specified
16px-grid footprint. See `tools/pixellab_tutorial_room_spec.json` for the
machine-readable contract and canonical bounds.

Canonical visible bounds include 32×32 small props, 64×32 chests, 64×48 desks
and tables, 80×48 TV consoles, 112×64 futons, 144×96 rugs, and 64×96 cat trees.

Reusable or adaptable material already exists under:

- `input/limezu_modern_interiors_full/1_Interiors/16x16/`: floor, wall, and
  room-builder tile candidates;
- `wip/items/single/`: plants, bed variants, table, rug, mirror, shelving,
  drawers, lights, and related furniture;
- `wip/items/`: sliced cabinets, decorations, and living-room atlases;
- `input/bitglow_pixelinterior_lrk_v1_1/`: walls/floors, kitchen, cabinets,
  decorations, doors/windows/stairs;
- `input/limezu_modern_interiors_full/`: additional interior and character
  references;
- `composite/tutorial_room_wip_tileset.tres`: the current WIP Godot tileset.
- `wip/pixellab/`: first-pass PixelLab exports for the room shell, geometric
  rug transition, and recognisable furniture/prop candidates. These remain WIP
  until they are reviewed against the blended composites and sliced to the
  project grid.

These are source/WIP assets, not automatically final room art. Licensing and
palette provenance must stay attached to any asset promoted to `approved/`.

## Asset backlog

### P0 — room shell and walkable space

- [ ] 16×16 floor tile family: clean plank, subtle variation, edge/shadow,
  and damaged/occluded variants only if needed.
- [ ] Wall/floor transition tiles with the semi-3D front-facing wall edge.
- [ ] Outer corners, inner corners, doorway opening, and wall end caps.
- [ ] Glazed door/window assembly: frame, panes, sheer curtain, and outside-light layer.
- [ ] Door assembly: closed, open, frame, handle/hinges, and collision footprint.
- [ ] Room boundary and shadow overlays that do not make walkable cells unclear.
- [ ] Tile collision/navigation metadata for floor, furniture, wall, sofa, table,
  chest, rack, cat tree, and door.

### P0 — recognisable room anchors

- [ ] Deep-blue futon sofa/bed with cushions and throw.
- [ ] Cream geometric rug with blue-grey/tan grid.
- [ ] Dining/work table with top, front edge, and Noguchi-style pendant lamp.
- [ ] Four cane chair variants or one chair with rotations/placement variants.
- [ ] Carved wooden storage chest and shoe storage.
- [ ] Door and the room-exit interaction marker.

### P1 — identity and storytelling props

- [ ] Framed Buddhist/Japanese art, calligraphy, illustrated landscape, and
  Filipino flag/banner.
- [ ] TV/media console, speakers, desk, monitor/laptop, and office chair.
- [ ] Wall shelves, wire bookshelves, books, headphones, and small ornaments.
- [ ] Clothes rack with a readable set of dark and coloured garments.
- [ ] Hanging trailing plant, potted foliage, and the tall cat tree.
- [ ] Pet bed, metal bowl, round-lidded wastebasket, tote bags, and lanyards.
- [ ] Optional fridge, cabinet, drawer unit, and small interactive props.

### P1 — atmosphere and animation

- [ ] Four lighting grade overlays or palette variants: dawn/day/dusk/night.
- [ ] Window/curtain glow layers for day and night; restrained outside light at night.
- [ ] Pendant lamp glow (Noguchi style lamp) and optional low-frequency flicker.
- [ ] Curtain/window highlight animation if it reads at game scale.
- [ ] Optional subtle plant sway and lamp/light animation.

### P2 — implementation support

- [ ] Final atlas exports at the project tile scale with nearest-neighbour import.
- [ ] Godot `TileSetAtlasSource` regions and terrain/peering rules.
- [ ] Occlusion/sorting conventions for bed, table, chairs, chest, and props.
- [ ] Interaction hotspots for door, bed, lamp, mirror, chest, and selected props.
- [ ] A small room test scene proving walkability, collision, sorting, and all
  four lighting variants.

## Recommended build order

1. Lock the 16×16 grid, room footprint, walkable cells, and wall height.
2. Build the floor/wall/window/door shell and verify the semi-3D silhouette.
3. Place sofa, rug, table, chairs, chest, cat tree, and door as the composition anchors.
4. Add the left-wall props, plants, clothing rack, and floor garment.
5. Add lighting variants and animated details.
6. Promote only verified, licensed, palette-consistent assets into `approved/`.

## Mango placement contract

Mango should use a centered 20×16 logical sprite footprint for overworld
movement. The visible character can occupy less than the full footprint, but no
direction may exceed it. The four directional sprites should share the same
baseline and centre line so rotation does not make Mango pop vertically or
sideways when changing direction.
