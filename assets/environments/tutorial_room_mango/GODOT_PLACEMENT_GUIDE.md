# Tutorial Mango environment assembly

The Tutorial Mango room currently has no authored Godot scene or generated
TileSet resource.

## Environment structure

An environment package is a composite of reusable tileset and item packages,
not an owner of bespoke per-room art. Tiles and props live once each in a
flat, room-agnostic library and are referenced by ID from the room's manifest:

```text
assets/
  tilesets/
    shared/02_input/<pack_name>/     # raw tile-oriented pack downloads
    <tileset_name>/01_reference/ 02_input/ 03_wip/ 04_approved/
  props/
    shared/02_input/<pack_name>/     # raw item/furniture-oriented pack downloads
    <item_name>/01_reference/ 02_input/ 03_wip/ 04_approved/
  environments/
    tutorial_room_mango/
      environment_manifest.json      # which tileset/item IDs compose this room, plus placement
      01_reference/                  # room-specific photos, layout references
      wip/                           # room-level composition experiments, colour/lighting studies
      approved/                      # canonical assembled .tscn + room-level .tres
```

A tileset or item is built once under `assets/tilesets/<name>/` or
`assets/props/<name>/` using the normal
`01_reference → 02_input → 03_wip → 04_approved` lifecycle. Plants, lighting
fixtures, seating and similar dressing are expected to recur across rooms —
build the package once and reference it from every room manifest that places
it, rather than duplicating a copy into this room's own folder.

Use one tileset folder for a coherent atlas family, not one folder per tile.
Use one item folder per genuinely reusable object; a static decorative sheet
that will never be placed independently can stay a single grouped candidate
sheet inside its own item folder until it is worth splitting.

Room scenes are a later composition layer. Create one only when the room
assembly is ready, referencing the approved (or actively-tested WIP) tileset
and item packages, and keep it with this room's `approved/` package. Do not
create a prop scene merely because a PNG exists.
