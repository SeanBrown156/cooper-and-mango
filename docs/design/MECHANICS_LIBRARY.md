# Core Mechanics Library

This document is the shared reference for reusable gameplay mechanics. It
defines the contracts that systems and content records can depend on; it does
not contain Stage 1 content records, balance values, scene wiring, or Godot
implementation code.

The library is intentionally separate from the content catalogue described in
[`CONTENT_SCHEMA.md`](CONTENT_SCHEMA.md). A mechanic says *how a system
behaves*. A content record says *which actor, item, ability, enemy, or room
uses it*.

## Status and authority

- **Scope:** full-game design reference, staged for implementation by the
  [`PRODUCTION_ROADMAP.md`](../production/PRODUCTION_ROADMAP.md).
- **Current implementation target:** Stage 1 only needs movement and
  interaction. Battle actions, the Zoom Meter, and traversal abilities remain
  reference material until their roadmap stages open.
- **Canonical character decisions:** the chosen overworld leader is locked for
  the playthrough, and traversal access follows that choice. See the
  [Protagonist Choice section](../vision/GAME_BIBLE.md#protagonist-choice-redblue-opening)
  in the Game Bible.
- **Design maturity:** mechanic names and contracts are stable enough for
  system planning; timings, formulas, costs, status lists, and final action
  rosters require later tuning and approval.

## Library conventions

Mechanic IDs are stable identifiers for systems and future data references.
They use the `mechanic_<snake_case_name>` form and should not be renamed after
implementation begins. The examples below are schemas, not records to place
in `data/`.

Every mechanic definition should be expressible in this shape:

```yaml
id: mechanic_<stable_name>
category: movement | interaction | battle_action | zoom_meter | traversal
phase: stage_0 | stage_1 | stage_2 | stage_3 | stage_4
purpose: <player-facing job>
inputs: []
outputs: []
rules: []
content_hooks: []
open_questions: []
```

`phase` is the earliest planned implementation stage, not a promise that the
mechanic is part of the current Stage 1 dataset.

## 1. Movement

Movement is continuous-feeling, grid-aware overworld navigation. The player
controls the selected leader in four directions and is stopped by room
collision. Direction also determines the leader's facing and the directional
presentation of its overworld animation.

| ID | Contract | Content hooks |
| --- | --- | --- |
| `mechanic_overworld_move` | Read directional input, resolve collision, update position, and preserve the last valid facing direction. | Walk speed, acceleration feel, animation set, controller bindings |
| `mechanic_collision_resolution` | Solid furniture, walls, and boundaries prevent overlap; movement along an unblocked axis may continue when the other axis is blocked. | Collision shapes, room bounds, one-way or special surfaces |
| `mechanic_facing` | The leader has one of `north`, `south`, `east`, or `west`; the last meaningful input remains the facing when movement stops. | Directional sprites, inspect direction, interaction probe |
| `mechanic_leader_lock` | Exactly one chosen character is the exploration leader for a playthrough. The second pet remains a battle party member and is not swappable as the leader. | Protagonist choice, party order, save state |
| `mechanic_room_transition` | A valid exit changes the current room/region and places the leader at a declared destination point. | Exit condition, destination region, spawn point, transition presentation |

Movement should not decide whether an object is meaningful or whether a route
is story-critical. Those are interaction and traversal concerns respectively.

### Movement event shape

```yaml
event: overworld_move_resolved
actor_id: actor_<leader>
from: { x: <number>, y: <number> }
to: { x: <number>, y: <number> }
facing: north | south | east | west
blocked_axes: []
```

## 2. Interaction

Interaction is an intentional player action against the nearest eligible
object, character, trigger, or exit. It is distinct from collision: walking
into a thing does not automatically inspect or activate it.

| ID | Contract | Content hooks |
| --- | --- | --- |
| `mechanic_interact` | An interaction input checks the leader's facing/probe and resolves at most one eligible target using deterministic priority. | Prompt text, range, priority, facing requirement |
| `mechanic_inspect` | An inspectable target presents flavour, clue, or state text without requiring a battle or inventory change. | Dialogue node, one-shot/repeatable policy, target state |
| `mechanic_trigger` | A target or region condition starts a scripted event, dialogue, battle, or state change once its prerequisites pass. | Prerequisites, consequences, replay policy |
| `mechanic_dialogue` | A conversation presents ordered lines and optional choices, then emits consequences for the owning content record. | Speaker, line order, choices, flags |
| `mechanic_exit` | An interacted or entered exit validates its condition and invokes room transition. | Lock condition, destination, spawn point |
| `mechanic_state_flag` | Persistent world facts are set and read by interaction, dialogue, traversal, and quest logic. | Stable flag ID, save scope, setter, readers |

### Interaction resolution order

When multiple targets overlap the probe, resolve in this order:

1. an explicitly facing, enabled target;
2. the nearest target within the interaction range;
3. the target's declared priority;
4. stable scene/content order as a final deterministic tie-break.

If no target qualifies, the input has no gameplay effect and should not create
an accidental trigger. Prompts are presentation and must not be treated as the
authority for eligibility.

## 3. Battle actions

Battle actions are turn-based commands resolved by the battle controller. The
library defines action categories and resolution order without defining the
Stage 1 ability roster or balance numbers.

| ID | Contract | Content hooks |
| --- | --- | --- |
| `mechanic_battle_start` | Convert an encounter into a battle state with ordered party/enemy combatants and a fresh round. | Encounter record, formation, opening effects |
| `mechanic_action_select` | Offer legal actions for the active combatant and accept one player/AI choice. | Ability ownership, item access, target rules, disabled states |
| `mechanic_action_order` | Build a deterministic turn order from combatant timing rules, with a stable tie-break. | Speed, priority, forced order, Rocky's future behaviour |
| `mechanic_action_resolve` | Validate an action, select/validate targets, apply effects, and emit result events. | Costs, power, hit rules, statuses, animations, sound |
| `mechanic_basic_action` | A low-complexity action available without a special ability record, such as a normal attack or defend. | Actor identity, damage/effect profile |
| `mechanic_ability_action` | Resolve a referenced ability record through the common action pipeline. | `abilities` record, resource cost, effects, target shape |
| `mechanic_item_action` | Consume or apply an eligible item through the same turn-resolution pipeline. | `items` record, species affinity, quantity |
| `mechanic_battle_status` | Apply, tick, stack/replace, and expire temporary combat conditions. | Status record, duration, immunity, display |
| `mechanic_battle_end` | Resolve victory, defeat, escape, rewards, and return to the overworld or a follow-up event. | Encounter rewards, consequences, next state |

### Action resolution contract

```yaml
action:
  actor_id: actor_<id>
  action_id: skill_<id> | item_<id> | basic_<id>
  targets: [actor_<id> | enemy_<id>]
  source: player | ai | automatic
result:
  accepted: true | false
  effects: []
  resource_changes: []
  events: []
```

The common pipeline is: select → validate → order → resolve → apply effects →
emit presentation/events → advance status timers → check battle end. An
invalid action must not consume its item, resource, or turn.

## 4. Zoom Meter

The Zoom Meter is a shared limit-break system built around real pet zoomies.
It fills from damage and excitement; at its threshold, the character
automatically unleashes its signature move. The player does not choose the
signature move. Rocky is permanently maxed, as established in the Game Bible.

| ID | Contract | Content hooks |
| --- | --- | --- |
| `mechanic_zoom_meter` | Track a meter for each eligible battle character, clamped between empty and maximum. | Meter capacity, UI presentation, persistence scope |
| `mechanic_zoom_gain` | Award meter from approved battle events such as taking damage or causing excitement. | Gain source, amount/formula, caps, modifiers |
| `mechanic_zoom_threshold` | Detect the transition to full and mark the signature action ready. | Threshold, ready cue, overflow policy |
| `mechanic_zoom_auto_action` | At the next legal resolution point, automatically resolve the character's signature move without player selection. | Signature ability ID, target policy, interruption rules |
| `mechanic_zoom_reset` | Clear or reduce the meter according to the chosen post-action rule. | Reset amount, defeat handling, battle transition |
| `mechanic_zoom_permanent_ready` | Keep a designated character permanently ready/full rather than charging normally. | Actor exception, signature action, repeat policy |

### Zoom state machine

```text
empty/charging --qualifying event--> charging
charging --meter reaches max--> ready
ready --next legal action point--> auto-resolve signature move
auto-resolve --resolution complete--> reset or ready (tuning decision)
```

Meter gain should be emitted by battle events, not hard-coded into individual
abilities. A signature action still uses the normal action validation and
effect pipeline; only selection is automatic.

## 5. Traversal abilities

Traversal abilities are overworld capabilities that change which optional
routes, shortcuts, puzzles, and secrets the locked leader can access. They are
not battle skills and should not be encoded as ordinary battle ability costs.

The Game Bible defines the current capability sets:

| Leader | Traversal abilities | Typical affordance |
| --- | --- | --- |
| Cooper | swim, pull, track scent, dig | Cross water, move/pull obstacles, follow scent trails, open dig sites |
| Mango | climb, squeeze through gaps, balance, sense hidden things | Reach heights, enter narrow spaces, cross precarious surfaces, reveal hidden things |

| ID | Contract | Content hooks |
| --- | --- | --- |
| `mechanic_traversal_check` | Ask whether the locked leader has the capability required by a traversal gate. | Required ability ID, leader ID, gate state |
| `mechanic_traversal_gate` | Keep an optional route, shortcut, puzzle interaction, or secret inaccessible until its check passes. | Gate type, feedback, destination, reward |
| `mechanic_traversal_use` | Resolve the world interaction associated with an owned capability and emit its state change. | Target type, animation, resulting flag/open path |
| `mechanic_scent_tracking` | Present or reveal a route clue that Cooper can follow when a scent trail is available. | Trail source, visibility, destination |
| `mechanic_hidden_sense` | Reveal otherwise hidden things when Mango uses the sense capability. | Reveal target, duration, persistence |
| `mechanic_traversal_persistence` | Preserve unlocked traversal state and world consequences in the save state. | Flag IDs, one-shot/repeatable policy |

### Traversal rules

- The leader choice is permanent for a playthrough; the other pet's traversal
  set is not temporarily available because that pet is in the battle party.
- Every main route must be completable by either leader alone. Leader-specific
  gates are optional or bonus content unless a future design decision says
  otherwise for a named story beat.
- A failed traversal check should explain the missing affordance in
  player-facing language and leave the world unchanged.
- A successful traversal use may set a persistent state flag, but the flag is
  owned by the target content record, not by the generic mechanic.

## Cross-system event vocabulary

These event names are the intended seams between systems. Payloads may grow,
but event meaning should remain stable.

| Event | Emitted by | Consumed by |
| --- | --- | --- |
| `overworld_move_resolved` | Movement | Animation, camera, interaction probe |
| `interaction_resolved` | Interaction | Dialogue, trigger, traversal, UI |
| `battle_action_resolved` | Battle action | Status, rewards, Zoom Meter, presentation |
| `battle_damage_received` | Effect resolution | Zoom Meter, defeat checks, presentation |
| `battle_excitement_awarded` | Battle/effect resolution | Zoom Meter |
| `zoom_signature_ready` | Zoom Meter | Battle action resolver, UI |
| `traversal_used` | Traversal | World state, quest/dialogue, presentation |
| `state_flag_changed` | World/content owner | Save system, gates, dialogue, quests |

## Data boundary and exclusions

This library deliberately does **not** add:

- files under `data/` or any Stage 1 actor/item/ability/enemy/encounter/dialogue
  records;
- numeric balance such as walk speed, meter capacity, damage, costs, or
  probability tables;
- Godot scenes, scripts, input-map changes, UI, animations, or save code;
- a final list of battle moves for Mango, Cooper, or any other character;
- new story beats or traversal destinations beyond the decisions already in
  the Game Bible.

When implementation begins, each system should consume this document's
mechanic contract and the existing [content schema](CONTENT_SCHEMA.md), then
add only the smallest approved content records required by the active roadmap
stage.

## Related authority

- [Game Bible](../vision/GAME_BIBLE.md) — player fantasy, protagonist choice,
  traversal sets, and Zoom Meter intent.
- [Content Schema](CONTENT_SCHEMA.md) — record IDs, content tables, and
  publishing lifecycle.
- [Production Roadmap](../production/PRODUCTION_ROADMAP.md) — staged delivery
  order and exit criteria.
- [Vertical Slice](../production/VERTICAL_SLICE.md) — current Stage 1 scope and
  explicit Zoom Meter exclusion.
