# Content Schema

The game is data-driven from the start. Claude Code should add content through these shared record shapes rather than burying items, enemies, and abilities inside bespoke scenes/scripts.

## ID Convention

Every content record gets a permanent, stable, machine-readable ID: `<type>_<snake_case_name>`, e.g. `item_cat_kibble`, `skill_judgemental_stare`, `enemy_mi_chan`, `region_empty_house`. IDs are never renamed once referenced elsewhere — if a record is wrong, add a new ID and retire the old one rather than mutating meaning under a stable name.

## Core Tables

- `actors` — playable characters and major NPCs (Mango, Cooper, Rocky, Milo, Charlie, King Jeff)
- `abilities` — skills/moves, including Zoom Meter signature moves
- `items` — food, treats, equipment, key items
- `enemies` — awakened-object monsters and bosses
- `encounters` — enemy groupings and battle setups
- `dialogue` — conversation nodes and choices
- `quests` — objectives and their steps
- `statuses` — status effects (confusion, protection, etc.)
- `regions` — the elemental regions and their metadata (see [`../vision/GAME_BIBLE.md`](../vision/GAME_BIBLE.md))

Each table has a matching folder under `data/` (`data/actors/`, `data/abilities/`, etc.) holding one file per record or one file per small group of related records — decide the split when the first real records are added; don't pre-optimize file layout before there's real content to organize.

## Example Record — Ability

```json
{
  "id": "skill_judgemental_stare",
  "name": "Judgemental Stare",
  "user_id": "actor_mango",
  "target": "one_enemy",
  "cost": 4,
  "effects": [
    {
      "type": "modify_stat",
      "stat": "attack",
      "amount": -3,
      "turns": 3
    }
  ],
  "animation_id": "mango_stare",
  "description": "The enemy begins to question every decision it has made."
}
```

## Required Fields (all record types)

- `id` — stable, permanent
- `name` — display name
- `description` — flavour text; can reference the real pet behaviour or story inspiration behind the record
- `content_status` — see Publishing Lifecycle below
- type-specific gameplay fields (stats, effects, targets, costs, drop tables, dialogue prerequisites/consequences, quest-step ordering, asset references, etc.)

## Publishing Lifecycle

Every record moves through: `idea` → `draft` → `review` → `approved` → `exported` → `retired`. Only `approved` (or later) records are included in a build. This applies whether records live purely as local JSON/Godot resources (current state) or later move into Supabase as an authoring layer (see below).

## Relationships to Track

- which abilities belong to each actor
- which items are usable by cats, dogs, or everyone (species affinities)
- which enemies appear in which region
- dialogue prerequisites and consequences
- quest-step ordering
- item drop tables
- sprite and audio asset paths
- balancing values (power, cost, probability, status duration)

## Supabase — Deferred, Not Rejected

The source note recommends Supabase as an eventual **editable master catalogue**, with Godot always running from an exported, versioned local snapshot — never depending on Supabase at runtime. This is explicitly a **Phase Three** step (per the note's phased rollout: tiny local dataset → first room validation → Supabase authoring catalogue → content production at scale). Do not begin the Supabase integration until the local schema has survived real use building Stage 1–2 content. When it does happen:

- Godot reads only local exported JSON/resources at runtime — no network dependency, no accounts required to play, no save-file breakage from a live database edit
- Exports are versioned snapshots (`content-0.1.0`, schema version, source commit, checksum/manifest) committed to GitHub alongside the build
- Snapshots must be deterministic — same approved state in, same files out

## Authored Data and Runtime Code

Content records describe authored meaning; Godot code interprets those records.
Scripts should not be generated separately for every conversation or object
interaction, and JSON should not become an arbitrary programming language.

The boundary is:

- **Authored data** defines dialogue lines, choices, stable IDs, conditions,
  consequences, encounter composition, asset references, and presentation
  metadata.
- **Runtime code** loads and indexes records, checks conditions, renders UI,
  applies consequences, manages save state, and emits gameplay events.
- **Runtime state** records what happened in the current playthrough. It must
  remain separate from the reusable authored definition.

This supports a classic JRPG-style workflow: designers author reusable content
records while a small set of engine systems provides the verbs that make those
records playable. New bespoke scripts should be added only when a genuinely new
runtime capability is required.

### Dialogue, interactions, and consequences

Dialogue belongs in `data/dialogue/`, alongside actors, abilities, items, and
encounters. A scene interaction should reference a dialogue or event ID rather
than contain its conversation text in GDScript.

The intended flow is:

```text
player presses interact
  -> interaction_resolved
  -> start dialogue/event by stable ID
  -> evaluate prerequisites and show dialogue nodes
  -> apply authored consequences
  -> emit state/event changes
  -> return control to the player
```

For example, the spider-plant interaction may start
`dialogue_plant_awakening`; when it completes, a consequence sets
`flag_plant_awakened`, unlocks the door, and returns control to the player.
The same consequence vocabulary should be reusable by dialogue, items, quests,
encounters, and traversal gates.

An interaction record or scene configuration should be small and declarative:

```json
{
  "id": "interaction_spider_plant",
  "trigger_type": "interact",
  "dialogue_id": "dialogue_plant_awakening",
  "prerequisites": [],
  "replay_policy": "once",
  "consequences": [
    { "type": "set_flag", "flag": "flag_plant_awakened" },
    { "type": "unlock", "target_id": "exit_tutorial_room" }
  ]
}
```

The engine systems implied by this boundary are intentionally small:

1. `ContentRepository` loads approved local records and indexes them by ID.
2. `WorldState` reads and writes persistent flags and other save-scoped state.
3. `DialogueRunner` walks nodes, evaluates conditions, handles choices, and
   hands consequences to the effect system.
4. `ConsequenceRunner` applies controlled verbs such as `set_flag`, `unlock`,
   `add_party_member`, `start_battle`, and `give_item`.
5. Interactable components provide the trigger and presentation hook but do not
   own the story text or duplicate progression logic.

The current linear dialogue records are a valid Stage 1 starting point. The
runtime should prove one complete path first — interaction → dialogue → flag or
party consequence → world response — before adding a general-purpose cutscene
language or a remote authoring database.

## Immediate Next Step

Populate the smallest possible real dataset needed for the Stage 1 vertical slice (see [`../production/PRODUCTION_ROADMAP.md`](../production/PRODUCTION_ROADMAP.md)): Mango, Cooper, one item (cat kibble), one ability each, one enemy (Dust Bunny or the Vacuum Cleaner), one encounter, and one short dialogue sequence. Then prove one data-driven interaction end to end: an interactable starts a dialogue, the dialogue applies a consequence, and the room responds to the resulting world-state change.
