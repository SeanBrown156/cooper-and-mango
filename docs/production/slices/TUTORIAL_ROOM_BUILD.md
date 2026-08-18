# Tutorial Room Build Card — Postcard 0: Mango Walks

> **Current executable work order.**
>
> This is deliberately smaller than the Stage 1 Vertical Slice. It proves the
> first visible loop before title choice, the opening branch, Cooper's room,
> dialogue architecture, or battle are treated as blockers.

## Outcome

Mango can walk convincingly around the existing Tutorial Room using the real
approved 24×16 overworld animation. He collides with room furniture and walls,
faces the correct direction, and visibly switches between idle and walking.
The room feels like a coherent domestic game space at native presentation
scale.

**This card is complete when a person can run it without assistance and say:
“that is Mango walking around his room.”**

## Scope

### In

- current `scenes/rooms/tutorial_room.tscn`;
- Mango as a real reusable player scene, replacing a non-animated placeholder
  only where necessary;
- 4-direction movement from the existing input actions;
- idle/walk animation and correct facing;
- collision with room boundaries, bookcase, sofa and kitchen counter;
- a camera/presentation check at the locked 480×270 logical viewport;
- a screenshot or short capture showing Mango moving in the composed room.

### Out

- protagonist choice;
- Cooper’s alternate starting room;
- dialogue UI or real dialogue records;
- purple-sweater interaction;
- Dust Bunny battle;
- spider-plant awakening event;
- party formation;
- any new environment pack or major room-art revision.

Those are subsequent postcards. Do not expand this card because a later scene
will need them.

## Current anchors

| Concern | Existing authority |
|---|---|
| Room scene | `scenes/rooms/tutorial_room.tscn` |
| Room event sequence | `scripts/systems/tutorial_room_controller.gd` |
| Mango scene | `scenes/characters/mango_placeholder.tscn` (replace/rename only when the real player scene is ready) |
| Art dimensions | `../art/ART_BIBLE.md` |
| Asset workflow | `../art/ART_PRODUCTION_PIPELINE.md` |
| Runtime contracts | `../design/TECHNICAL_GAME_DESIGN.md` |
| Final Stage 1 scope | `VERTICAL_SLICE.md` |

## Asset minimum

Only prepare what the postcard needs:

- one approved Mango overworld sheet;
- 24×16 frame size;
- four directions;
- idle and walk animations;
- a common feet baseline;
- no blur, nearest-neighbour import;
- signature orange silhouette, purple hoodie draped over the back, ears and
  tail readable at native size.

Use the existing approved Tutorial Room art unchanged unless a simple
alignment/collision correction is necessary. New assets enter the normal
`input → wip → approved` lifecycle; active room composition may reference
room WIP art while it is being tested.

## Implementation checklist

- [ ] Confirm the approved Mango overworld sheet has the required frames and
  frame order.
- [ ] Wire SpriteFrames/AnimatedSprite2D (or the project's equivalent) to
  Mango's reusable player scene.
- [ ] Map input to velocity and direction using `move_left`,
  `move_right`, `move_up`, `move_down`.
- [ ] Start the matching walk animation only while velocity is non-zero;
  otherwise use matching idle.
- [ ] Place collision at Mango's feet/body, not across transparent sprite area.
- [ ] Verify collisions against walls, bookcase, sofa and kitchen counter.
- [ ] Ensure movement is pixel-clean—no texture smoothing or fractional visual
  jitter.
- [ ] Run the scene, test all four directions and collect proof.
- [ ] Record any unresolved asset issue as a separate issue; do not silently
  broaden this card.

## Acceptance checks

| Check | Pass condition |
|---|---|
| Startup | Tutorial Room runs from a clean Godot launch with no errors. |
| Identity | Mango is recognisable: orange quadruped silhouette, purple hoodie, ears and tail. |
| Direction | Mango faces left, right, up and down correctly. |
| Animation | Walking visibly animates; stopping returns to idle. |
| Collision | Mango cannot pass through any four room boundaries, bookcase, sofa or counter. |
| Readability | At 480×270, Mango separates clearly from floor and furniture. |
| Pixel treatment | Crisp nearest-neighbour pixels; no blurred scaling or shaky sub-pixel movement. |
| Proof | A screenshot/short capture demonstrates movement and an intentional furniture collision. |

## Verification script

1. Open the Godot project and run `tutorial_room.tscn`.
2. Walk Mango left into the sofa, then upward into the bookcase.
3. Walk to the kitchen counter and test its collision edge.
4. Walk in all four directions in open floor space, observing each animation.
5. Stop in a visually clear central location and capture the room.
6. Read the Godot output/errors; fix only defects relevant to this card.
7. Repeat until all acceptance checks pass.

## Next postcards — not part of this card

1. Purple sweater: interaction prompt → one data-driven inspect line.
2. Purple sweater: event → Dust Bunny encounter placeholder.
3. Spider Plant: data-driven awakening dialogue/event.
4. Cooper: matching movement postcard in the alternate opening path.
5. Connect both paths to the Stage 1 Vertical Slice sequence.
