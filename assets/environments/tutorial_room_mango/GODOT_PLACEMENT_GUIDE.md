# Tutorial Mango environment assembly

The Tutorial Mango room currently has no authored Godot scene or generated
TileSet resource. It is intentionally reset while the environment package
structure is being decided.

## Environment structure

Environments are larger compositions than character families, so do not make
a lifecycle folder for every tree, chair, or 16×16 tile. Treat the room or
biome as the meaningful environment family, then group its material by role:

```text
tutorial_room_mango/
├── general/
│   ├── 01_reference/     room photos, layout references
│   └── 02_input/         raw/licensed packs and broad generations
├── tiles/                coherent atlas/terrain families
├── props/                grouped furniture, plants, fixtures, objects
├── wip/                  room-level experiments and future Godot assembly
└── approved/             canonical room-level package
```

`general/` is shared room context. `tiles/` and `props/` are asset-group
boundaries, not extra lifecycle stages. When a group becomes a real production
family, give that group the same numbered workflow used by the characters:

```text
tiles/home_interior/
├── 01_reference/
├── 02_input/
├── 03_wip/       atlas + TileSet .tres while iterating
└── 04_approved/  canonical atlas + TileSet .tres
```

Use one tileset folder for a coherent atlas family, not one folder per tile.
Use grouped prop folders or batches unless a prop needs independent reuse,
behavior, animation, collision, or its own approval decision. A static tree or
chair can remain part of a grouped prop sheet.

Room scenes are a later composition layer. Create one only when the room
assembly is ready, and keep it with the room's WIP/Approved package. Do not
create prop scenes merely because a PNG exists.
