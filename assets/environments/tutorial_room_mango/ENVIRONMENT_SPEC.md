# Mango tutorial room — technical environment specification

Status: canonical generation specification; art remains WIP until human review and
Godot validation.

This document translates the room references into production constraints. The
machine-readable ledger and PixelLab request manifest is
[`environment_manifest.json`](environment_manifest.json).

## 1. Source authority

Use the sources in this order:

1. `input/gemini/tutorial_room-day.png` controls composition, placement, object priority,
   proportions, and the baseline colour relationships.
2. `input/gemini/tutorial_room-dawn.png`, `-dusk.png`, and `-night.png` control lighting
   variants only. They do not introduce different geometry.
3. The photographs in `reference/photos/` control real-object identity, materials, and
   distinctive details.
4. The Art Bible controls pixel discipline, palette, and scale.

If a photograph and a Gemini composite disagree, keep the Gemini layout and use the
photograph to make the object more specific. Photo-only furniture is optional room
dressing, not a required composition anchor.

## 1a. Manifest and Godot ownership

`environment_manifest.json` is the environment-local inventory and production
contract. It records references, asset IDs, generation inputs and provenance,
technical bounds, variants, review state, and generation order.

Godot `.tscn` and `.tres` resources remain authoritative for runtime composition:
placement, layering, sorting, collision, and scene behaviour. The manifest must
describe the assets Godot can compose, but it must not become a second hand-authored
scene graph.

## 2. Native room contract

| Property | Locked value |
|---|---:|
| Room artboard | **512×384 px** |
| Room grid | **32×24 cells** |
| Tile/cell size | **16×16 px** |
| Runtime camera | **480×270 logical px** |
| Camera behaviour | viewport into the room; never stretch the room to fit |
| Projection | **orthographic high top-down** |
| Floor-object camera | 90° plan view, top surfaces dominant |
| Pixel edges | hard; no antialiasing or soft alpha halos |
| Runtime scale | 1× native, enlarged only by integer presentation scaling |

The 512×384 artboard is deliberate: the dawn Gemini composite is already 512×384,
and this 32×24-cell room preserves the intended 4:3 composition. The 480×270 game
camera shows part of that room; it must not resize or distort the environment.

## 3. Orientation grammar

The room has one global compass:

- north is the window/headboard wall at the top of the artboard;
- east is the dining-table and exit-door side;
- south is the carved chest/foreground side;
- west is the flag, shelves, and clothes-rack side.

All freestanding floor objects use a high top-down plan view. Their local north must
match room north unless the ledger explicitly provides a cardinal variant. Invalid
results include isometric projection, oblique cabinets, horizon lines, eye-level or
side views, converging perspective, and a dominant visible front face.

A narrow 1–3 px near-side depth edge is permitted on beds, tables, rugs, chests, and
similar objects when it helps the silhouette read. It may not change the footprint
or turn the asset into a three-quarter view.

Vertical fixtures are the only exception. Windows, curtains, wall shelves, art,
flag, door leaf, and the tall cat-tree trunk may use a front-elevation overlay while
their collision and floor contact remain on the 16 px grid. These are tagged
`vertical_fixture` in the JSON ledger.

## 4. Gemini composition translation

The production room keeps the Gemini image's large, readable masses:

- north: a broad three-panel glazed window/door with sheer curtains and a restrained
  city silhouette outside;
- north-west/centre-left: the deep-blue bed/futon with carved timber rails, two pale
  pillows, a cream throw, and optional sleeping-Mango state;
- centre: cream geometric rug with tan and blue-grey repeated cells;
- east: square dark-wood dining/work table, four cane-backed chairs, and the round
  paper pendant centred above it;
- north-east: tall green cactus-like cat tree; it must read as a cat tree, not a
  literal cactus;
- west: Filipino flag/banner, small wall shelves/books/art, and a crowded clothes
  rack;
- south: carved wooden storage chest;
- south-east: exit door and purple hoodie/garment on the floor;
- small accents: potted foliage, pet bed, bowl, and wastebasket where navigation
  remains clear.

The photos add material truth: warm varied timber floorboards, off-white plaster,
deep cobalt upholstery, cane weave, dark carved wood, white paper lamp ribs, black
wire shelving, leafy palms, and the actual blue-white-red flag colours.

## 5. Tile-set specification

The reusable shell is a 16 px atlas family, not one full-room painting.

### Required terrain and shell vocabulary

| Family | Native piece | Required variants |
|---|---:|---|
| timber floor | 16×16 | clean A/B/C/D, dark-edge A/B, subtle seam |
| plaster wall | 16×16 | clean A/B, shadowed, light-wash |
| wall/floor boundary | 16×16 | N/E/S/W, four outer corners, four inner corners |
| baseboard/end cap | 16×16 | horizontal, vertical, four ends/corners |
| doorway threshold | 16×16 | centre, left jamb, right jamb |
| rug transition | 16×16 Wang family | floor↔rug edges, corners, inner corners, full rug |

The atlas target is 16 columns × 8 rows (**256×128 px**) with unused cells left
transparent. Cell assignments are recorded in the JSON ledger; final atlas packing
may move cells only if the Godot TileSet metadata moves with them.

Window, curtains, door states, and wall decoration are modular overlay sprites,
because they span cells and need different sorting/lighting behaviour.

### Draft placement grid

The generation ledger also records the first assembly pass in cell and pixel
coordinates. These anchors translate the Gemini composition without stretching it:

| Anchor | Cell rectangle `(x,y,w,h)` | Pixel rectangle |
|---|---:|---:|
| north window/curtain | `8,0,18,5` | `128,0,288,80` |
| bed/futon | `8,5,9,8` | `128,80,144,128` |
| geometric rug | `14,8,10,7` | `224,128,160,112` |
| dining table | `24,7,5,4` | `384,112,80,64` |
| cat tree | `28,1,4,6` | `448,16,64,96` |
| Filipino flag/banner | `0,7,4,6` | `0,112,64,96` |
| clothes rack | `1,14,6,4` | `16,224,96,64` |
| carved chest | `12,21,5,3` | `192,336,80,48` |
| exit door | `29,16,3,4` | `464,256,48,64` |
| purple hoodie | `21,18,3,2` | `336,288,48,32` |

These are composition anchors, not collision rectangles. Collision uses each sprite's
declared `grid_footprint_cells`. Keep the central cells around columns 17–22 and the
southern route to the east door readable and walkable during the first Godot pass.

## 6. Sprite scale and anchoring

Every ledger item declares:

- `canvas_px`: exact PixelLab request size;
- `visible_bounds_px`: maximum non-transparent content bounds;
- `grid_footprint_cells`: gameplay/collision footprint, not necessarily the whole
  drawing;
- `pivot`: Godot origin convention;
- `facing`: required local cardinal orientation;
- `projection_class`: `floor_plan`, `vertical_fixture`, or `flat_overlay`;
- `z_group`: intended sorting band.

Floor props use `bottom_center` pivots unless they are flat overlays. Rugs and light
grades use `top_left`. Wall fixtures use `bottom_center` at the wall/floor contact or
`top_left` when they form part of the shell.

The JSON ledger is definitive for individual dimensions. The principal anchors are:

| Asset | Canvas | Footprint | Facing |
|---|---:|---:|---|
| bed/futon | 144×128 | 8×7 cells | head north |
| geometric rug | 160×112 | 10×7 cells | pattern north-aligned |
| dining table | 80×64 | 4×3 cells | long grain east–west |
| cane chair | 32×32 each | 1×1 cell | N/E/S/W variants |
| cat tree | 64×96 | 3×3 cells | trunk on north/east wall |
| clothes rack | 96×64 | 5×2 cells | rail east–west |
| carved chest | 80×48 | 4×2 cells | lid grain east–west |
| window assembly | 288×80 | wall overlay | north wall |
| exit door | 48×64 per state | 2×1 cells | east wall |

Canvas padding is transparent and must never be interpreted as permission to enlarge
the object. The visible drawing must remain inside `visible_bounds_px`.

## 7. Palette and lighting

Day is the canonical asset palette. Generate one geometry/material set only.

- plaster: warm off-white/grey;
- floor and carved wood: Art Bible wood/earth ramp;
- bed: deep cobalt/navy with cream and one orange accent;
- rug: cream, tan, muted blue-grey;
- plants/cat tree: forest green ramp with warm fibre accents;
- outline: warm near-black `#181425`, used selectively;
- per prop: normally 4–8 colours; anchors may use up to 10.

Dawn, dusk, and night are non-destructive 512×384 lighting overlays or Godot colour
grades. Do not bake four differently drawn copies of every object. The night variant
adds a separate warm pendant pool; it does not recolour object source sprites.

## 8. Acceptance gates

An asset can move from generated input to WIP only when all of these pass:

1. exact canvas dimensions and transparent background;
2. visible pixels within the declared bounds;
3. 16 px footprint alignment and correct pivot;
4. required cardinal orientation and projection class;
5. recognisable at 1× next to the 24×16 Mango overworld sprite;
6. hard edges, no fractional pixels, blur, halo, or noisy isolated pixels;
7. palette close to the room subset;
8. collision footprint does not block the intended central route;
9. no text or illegible pseudo-writing on art, books, or flag details;
10. reviewed in the assembled 512×384 room, not only in isolation.

If orientation fails, reject the candidate even when its canvas size is correct. The
two previous top-down batches are retained as evidence of exactly that failure mode.

## 9. Production sequence

1. Generate and approve the shell atlas: timber floor, plaster, boundaries, and rug
   transition.
2. Generate the window/curtain and door overlay families.
3. Generate the P0 anchors in coherent batches: bed, rug, table/chairs, cat tree,
   chest, flag, clothes rack, pendant.
4. Assemble a greyscale/collision room and verify the camera route.
5. Add P1 identity props and the sleeping-Mango/opening-state sprites.
6. Add dawn/day/dusk/night grades and pendant glow.
7. Clean in Aseprite, test in Godot, and promote only approved output.
