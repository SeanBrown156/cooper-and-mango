# Tutorial Room prop placement in Godot

> `input/` and `reference/` are source-only folders marked with `.gdignore`, so Godot does not import them. Copy selected game-ready art into `wip/` (or the eventual `approved/` area) before assigning it to a scene.

The playable room is `scenes/rooms/tutorial_room.tscn`. Its shell is instanced from
`scenes/rooms/tutorial_room_base.tscn` and should normally remain untouched while
placing furniture.

## Scene structure

```text
TutorialRoom
├── Base
│   ├── Floor                 16px TileMapLayer
│   ├── Walls                 16px TileMapLayer
│   ├── RoomBounds            shell collision
│   └── PropAnchors           named editor guides
├── YSort                     depth-sorted gameplay layer
│   ├── PlacedProps           put furniture here
│   ├── Mango
│   ├── SpiderPlant
│   └── RoomExit
└── UI                        fixed to the camera
```

## Position a prop

1. Open `scenes/rooms/tutorial_room.tscn` in Godot.
2. Expand `Base > PropAnchors`. Each `Marker2D` is named for its intended object.
3. Select the marker and read its **Position** in the Inspector. Its editor
   description records expected canvas size, pivot, and facing.
4. Drag the prop PNG from the FileSystem dock into `YSort > PlacedProps`. Godot will
   create a `Sprite2D`.
5. Set the new sprite's Position to the matching marker Position. Do not scale it.
6. For a bottom-centred prop, leave **Centered** on and adjust the source image so
   its intended floor contact is the sprite bottom. If the PNG contains padding,
   use **Offset Y** to put the contact point exactly on the marker.
7. For a top-left flat overlay such as the rug, turn **Centered** off and copy the
   marker position directly.
8. Save and run the scene. Walk Mango both in front of and behind the prop to check
   sorting.

## Grid snapping

Use the 2D toolbar's grid snap with:

- grid step: `16 × 16`;
- primary line every: `1`;
- rotation snap: off for room props;
- scale snap: off;
- sprite scale: always `1, 1`.

Hold `Shift` only when deliberately making a sub-cell adjustment. Large furniture
normally lands on whole cells; small visual offsets should be integers, never
fractions.

## Sorting

Freestanding props belong under `YSort/PlacedProps`. The bottom of the sprite should
represent its floor contact. This allows Mango to draw behind it when north of the
contact and in front when south of it.

Flat floor overlays such as rugs should use a negative `z_index` (for example `-1`)
so they always remain below Mango. Overhead objects such as the paper pendant should
use a separate positive `z_index` rather than ordinary Y sorting.

Wall decoration does not need Y sorting. Put it under `PlacedProps`, assign a stable
negative or low `z_index`, and keep its contact/pivot convention from the environment
specification.

## Add collision

For furniture Mango cannot walk through:

1. Right-click the prop and add a `StaticBody2D` child.
2. Add a `CollisionShape2D` beneath the body.
3. Choose a `RectangleShape2D` for the first pass.
4. Cover only the object's floor footprint—not its full visible height.
5. Leave at least one 16px cell around the central route and the east-door route.

The room shell already supplies north, south, west, and split east-wall collision.
The east-wall gap covers cells `y=16..19` for the exit.

## Gemini composition anchors

The important first-pass coordinates are:

| Prop | Position/pivot |
|---|---:|
| bed/futon | `(200, 208)` bottom-centre |
| rug | `(224, 128)` top-left |
| table | `(424, 176)` bottom-centre |
| pendant | `(424, 144)` centre |
| cat tree | `(480, 112)` bottom-centre |
| clothes rack | `(64, 288)` bottom-centre |
| carved chest | `(232, 384)` bottom-centre |
| exit door | `(496, 320)` bottom-centre |
| purple hoodie | `(360, 320)` bottom-centre |

These are a faithful starting translation of the Gemini layout, not immutable final
art direction. Move a prop in whole 16px steps first; use small integer offsets only
after testing the room at native 1× scale.
