# Technical Game Design

> **Runtime-system source of truth for Cooper & Mango.**
>
> This document defines the small, reusable contracts that make scenes playable.
> It complements—not replaces—the Game Bible (creative direction), Art Bible
> (visual rules), Content Schema (data records), and Vertical Slice (milestone
> scope). Do not turn it into a speculative catalogue of future systems.

## Current implementation rule

Build a **playable postcard** at a time: one visible outcome that can be run,
tested and shown in a screenshot or short capture. A postcard may use
placeholders and room-scoped WIP art. It must not wait for the whole asset
library, combat system or full narrative to be complete.

The current postcard is defined by
[`../production/slices/TUTORIAL_ROOM_BUILD.md`](../production/slices/TUTORIAL_ROOM_BUILD.md).

## Runtime states

The game has an explicit top-level mode. Only one mode accepts player movement
at a time.

| Mode | Player movement | Primary owner |
|---|---|---|
| `exploration` | enabled | current room + player |
| `dialogue` | disabled | dialogue runner |
| `cutscene` | disabled | event runner |
| `transition` | disabled | scene/encounter transition |
| `battle` | disabled | battle scene |

Do not make individual room scripts guess whether movement should be enabled.
They request a state change; the active owner returns the game to
`exploration` when finished.

## Player contract

Each overworld leader is a reusable `CharacterBody2D` scene with:

- a stable actor ID: `actor_mango` or `actor_cooper`;
- 4-direction input through the project actions `move_left`,
  `move_right`, `move_up`, `move_down`;
- `idle` and `walk` animation states for each facing direction;
- an interaction origin/facing direction;
- collision through `CollisionShape2D`;
- a movement lock controlled by runtime state, dialogue, cutscenes and
  transitions.

Overworld art uses the locked **24×16 quadruped** frame. Foot placement and
collision are gameplay truth; a sprite's transparent bounds are not.

The selected protagonist remains the leader for the whole playthrough:

- `mango` → Mango leads exploration; Cooper joins battle party later.
- `cooper` → Cooper leads exploration; Mango joins battle party later.

Do not implement leader swapping.

## Interaction contract

Every inspectable object is a reusable scene with:

- `interaction_id` — stable, room-unique string such as
  `tutorial_room_purple_sweater`;
- `prompt_text` — normally `Inspect`;
- `Area2D` interaction range;
- optional visual highlight/prompt;
- one action on activation: start dialogue, set a flag, run an event, change
  scene, or begin an encounter.

The player may activate the highest-priority interactable within range using
the project's `interact` action. Interaction must be impossible through
solid furniture or from an implausible distance.

A room-specific controller may decide **what happens** after an interaction,
but the generic detection, prompt and activation behaviour belongs in the
shared interaction system.

## Data and flags

Narrative text, encounters and persistent consequences are data-driven:

- dialogue: `data/dialogue/`
- encounters: `data/encounters/`
- actors/enemies: their matching `data/` folders

Stable record IDs follow
[`CONTENT_SCHEMA.md`](CONTENT_SCHEMA.md). Room scripts may reference IDs but
must not embed display dialogue or battle statistics.

Use small, explicit world flags for one-time room events, for example:

- `tutorial_room_sweater_inspected`
- `tutorial_room_spider_plant_awakened`
- `tutorial_room_dust_bunny_defeated`

A flag is set only after the event successfully completes. A later save system
will persist these values; do not block early postcards on building saves.

## Dialogue contract

The dialogue runner receives a dialogue record ID and:

1. changes runtime mode to `dialogue`;
2. renders the specified text and speaker;
3. accepts advance input;
4. applies approved record consequences/flags;
5. emits completion;
6. restores `exploration` unless the caller begins another explicit mode.

The first implementation may be visually simple, but it must load text from a
real data record rather than from a scene script.

## Encounter contract

An encounter begins through a stable encounter ID:

1. interaction/event requests an encounter;
2. exploration locks;
3. transition begins;
4. battle scene receives the encounter ID;
5. result returns to the requesting world state;
6. success consequences set flags and restore exploration.

For the current tutorial postcard, a labelled transition or a minimal
placeholder battle scene is valid proof. Full battle UI, balancing and the
Zoom Meter are not required.

## Scene responsibility

- **Shared systems** own movement, interaction selection, dialogue mode and
  state transitions.
- **Room scenes** own layout, collisions, placement, room exits and which
  interactions exist.
- **Room controllers** sequence events using IDs and flags.
- **Data records** own player-facing content and gameplay values.
- **Godot composition resources** own atlas regions, SpriteFrames, TileSets
  and other asset assembly.

Keep a room controller thin. If two rooms need the same behaviour, promote it
to a shared system instead of copying it.

## Verification loop

Every implementation card ends with this loop:

1. run the target scene in Godot;
2. exercise the exact input or interaction;
3. inspect Godot errors and output;
4. capture a screenshot or short clip at the meaningful state;
5. compare against the card's acceptance checks;
6. iterate until it passes, then commit the proof reference in the issue/PR.

Godot MCP is the preferred local assembly and verification bridge: Godot must
be running with this project open and its MCP plugin enabled. See
[`../engineering/MCP.md`](../engineering/MCP.md).

## Explicit non-goals for the current slice

- generic ECS architecture;
- multiplayer/networking;
- a production save system;
- full combat, menus, equipment or Zoom Meter;
- mobile/Switch input or export;
- dynamically generated complete maps.

Add systems only when a playable postcard or approved production stage requires
them.
