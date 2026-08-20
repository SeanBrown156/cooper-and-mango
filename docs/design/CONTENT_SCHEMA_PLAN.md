# Content Schema Plan

Planning document for the long-term content model and authoring workflow for
Mango and Cooper. This is a design exploration, not an approved schema and not
a runtime implementation specification.

The purpose of this document is to make the whole problem visible before the
project commits to a larger catalogue of actors, abilities, items, enemies,
encounters, dialogue, quests, regions, and assets.

The current small Stage 1 dataset is a useful proof that stable IDs and
cross-record references can work. It is not evidence that every final field
has been decided. The source-of-truth documents remain:

- [`CONTENT_SCHEMA.md`](CONTENT_SCHEMA.md) for the current record convention
  and publishing lifecycle.
- [`COMBAT_STAT_MODEL.md`](COMBAT_STAT_MODEL.md) for the current combat stat
  vocabulary, formulas, effect guidance, and tuning guardrails.
- [`MECHANICS_LIBRARY.md`](MECHANICS_LIBRARY.md) for system contracts such as
  battle actions, dialogue, state flags, Zoom Meter, and traversal.
- [`../vision/GAME_BIBLE.md`](../vision/GAME_BIBLE.md) for character, story,
  protagonist-choice, traversal, and world decisions.

Nothing in this plan should silently override those documents. Where they do
not yet agree, the disagreement is an open design decision.

## 1. The mental model

The game should have three different kinds of data:

```text
AUTHORED CONTENT
  What the designers write: Mango, Dust Bunny, Brave Bark, dialogue,
  regions, quests, effects, rewards, asset references.

RUNTIME DEFINITIONS
  Validated, loaded, typed versions of authored content that the Godot game
  can query by stable ID.

PLAYTHROUGH STATE
  What happened for this player: current HP, level, inventory quantities,
  equipped items, story flags, quest progress, opened routes, defeated bosses.
```

These layers must not collapse into one giant record. An authored actor should
not contain Mango's current HP. An item definition should not contain the
player's current quantity. A dialogue definition should not itself be the save
file's record of whether the player has seen it.

The intended pipeline is:

```text
Human authoring UI / repository files
        ↓
Schema validation and reference validation
        ↓
Deterministic content package
        ↓
Godot runtime definitions
        ↓
Systems: battle, dialogue, inventory, quests, regions, presentation
        ↓
Save state records only player/world changes
```

The future Builder Console should make this pipeline understandable and
pleasant, but it should not become a second hidden database with a different
model from the JSON consumed by Godot.

## 2. Design principles

### Stable identity over display names

Every authored record needs a permanent ID such as `actor_mango`,
`skill_brave_bark`, or `enemy_dust_bunny`. Names, descriptions, balance values,
and presentation assets can change. The ID should not change after references
exist.

If a record's meaning changes substantially, create a new ID and retire the old
one. Do not make `enemy_dust_bunny` silently become a Vacuum Cleaner because
the old ID is already part of encounter, save, dialogue, or analytics data.

### References are explicit

Records should refer to other records by ID, not by display name, filename
guessing, or copied nested definitions. The authoring UI should provide
searchable pickers and previews so a human can understand the reference.

### Definitions are reusable; instances carry exceptions

An enemy definition describes the reusable Dust Bunny template. An encounter
describes where and how many Dust Bunnies appear, at what level, in what
formation, with what reward or opening rule. A battle instance is runtime state
for the specific fight currently happening.

The same separation applies to:

- Actor definition versus party member state.
- Item definition versus inventory stack.
- Ability definition versus selected action.
- Dialogue definition versus whether a conversation was completed.
- Region definition versus the player's opened gates and defeated encounters.

### Small shared vocabularies beat bespoke mechanics

Abilities, items, scripted consequences, and eventually quest rewards should
reuse a small effect/action vocabulary. A new effect type should be added only
when an existing effect, tag, status, or rule cannot express the intended
design clearly.

### Authoring should be human-readable, runtime should be convenient

The authored JSON may retain descriptive names, explicit arrays, and useful
metadata. The runtime loader may build indexes such as `actors_by_id` and
typed Godot objects. Runtime optimization should not make the authored source
opaque.

### Content should be staged

The schema can describe the whole game, but implementation and validation
should proceed by roadmap stage. A field is not necessarily implemented just
because the schema can represent it. Stage 1 should prove the smallest useful
slice; Stage 2 can add the next systems without forcing every future table into
the first loader.

## 3. Content map

The content catalogue is larger than the six records currently in `data/`.
This is the proposed mind-map of the major domains.

```text
Game content
├── Characters
│   ├── Actors / party members
│   ├── NPCs
│   ├── Enemies
│   └── Boss phases / variants
├── Combat
│   ├── Abilities
│   ├── Items
│   ├── Statuses
│   ├── Effects
│   ├── Targeting rules
│   ├── Encounters / formations
│   └── Rewards / drops
├── Story and progression
│   ├── Dialogue graphs
│   ├── Choices
│   ├── Quests and steps
│   ├── State flags
│   ├── Party recruitment
│   ├── Unlocks and gates
│   └── Endings / story outcomes
├── World
│   ├── Regions
│   ├── Rooms / maps
│   ├── Exits and spawn points
│   ├── Interactables
│   ├── Traversal gates
│   ├── Encounter zones
│   └── One-shot / repeatable triggers
├── Presentation
│   ├── Sprites and animations
│   ├── Portraits and expressions
│   ├── VFX and battle presentation
│   ├── Music and sound effects
│   ├── UI labels and icons
│   └── Localization text
└── Production metadata
    ├── Content status
    ├── Tags and ownership
    ├── Source / inspiration notes
    ├── Balance notes
    ├── Review history
    └── Compatibility / deprecation information
```

The Builder Console should make this graph visible. A human should be able to
open Mango and see abilities, traversal capabilities, assets, dialogue
appearances, recruitment conditions, and encounters in which Mango is used.

## 4. Shared record envelope

Every content record should probably share a small envelope. Exact field names
are still open, but the concepts are important:

```json
{
  "id": "actor_mango",
  "record_type": "actor",
  "schema_version": 1,
  "content_status": "draft",
  "name": "Mango",
  "description": "...",
  "tags": ["playable", "cat"],
  "authoring": {
    "notes": "...",
    "source": "real_pet",
    "review_notes": []
  }
}
```

Questions to settle:

- Is `record_type` redundant because the folder already identifies the type?
- Are authoring notes shipped, or stripped during export?
- Do we need `created_at`, `updated_at`, and `updated_by`, or is Git history
  enough for the initial project?
- Is `schema_version` per record, per table, or only in the exported manifest?
- Should display text use direct strings initially and move to localization
  keys later?
- Which metadata is creative content and which is production-only metadata?

The lifecycle remains conceptually useful:

```text
idea → draft → review → approved → exported → retired
```

The exporter should include only records allowed by the build policy. A
development build may include drafts with a warning; a release build should
normally include approved/exported records only.

## 5. Proposed content domains

### Actors and party members

An actor is a reusable character identity. A party member is an actor plus
playthrough state and possibly a progression profile.

Potential authored fields:

- stable ID, display name, description, species, role, character tags;
- base combat stats and growth profile;
- starting level and starting abilities;
- ability learnset and unlock conditions;
- signature/Zoom ability;
- traversal capabilities;
- equipment slots or restrictions;
- recruitment and party-availability rules;
- battle AI defaults when the actor is not directly controlled;
- overworld, battle, portrait, expression, animation, and audio assets.

Potential runtime/save fields:

- current level and experience;
- current HP, resources, statuses, and Zoom;
- learned abilities;
- equipment;
- temporary modifiers;
- recruitment/party status;
- current position only if the character is a world actor.

Important blind spot: the same actor may appear as a playable party member,
dialogue speaker, overworld follower, battle combatant, and story NPC. The
schema should avoid duplicating identity in each system.

### Stats and progression

The current combat authority uses `max_hp`, `power`, `guard`, `speed`, `focus`,
and `zoom_max`. Those names should remain centralized rather than redefined in
each record type.

Progression may eventually include:

- level cap;
- experience curve;
- per-stat growth;
- ability learning by level, quest, item, or story flag;
- stat rewards or permanent upgrades;
- equipment-derived stats;
- temporary battle modifiers;
- difficulty or encounter scaling.

The schema must distinguish base values, growth values, derived values, and
runtime values. Otherwise balance editing and save data will become confused.

### Abilities and actions

An ability should describe the action's identity and resolution inputs:

- user restrictions or ownership model;
- battle/overworld/traversal context;
- resource cost and cost type;
- target shape and target validation;
- power, accuracy, priority, and tags;
- one or more ordered effects;
- status or affinity interactions;
- animation, VFX, sound, camera, and UI presentation;
- unlock or availability conditions.

Open model decision: should `user_id` live on the ability, or should ownership
be a relationship/learnset record? A relationship model is more reusable if an
ability can later be shared, inherited, taught, or granted temporarily.

The ordinary attack, defend, flee, and item actions also need a home. They may
be built-in mechanics rather than content records, but the action pipeline
should treat them consistently with authored abilities.

### Items and equipment

An item definition should not contain the player's quantity. Potential fields:

- item category: consumable, equipment, key item, quest item, currency;
- usable contexts: battle, field, menu, shop, gift;
- species, actor, or role affinity;
- stack limit and consumption rule;
- buy/sell value if shops exist;
- effects and target policy;
- equipment slot and stat modifiers;
- acquisition and removal rules;
- icon, inventory sprite, use animation, and sound.

Blind spots to decide early:

- Are items ever lost, traded, sold, or permanently consumed?
- Can key items have effects, or are they purely progression references?
- Is equipment a separate domain from items, or a subtype with shared fields?
- Are shops, prices, and inventories content records or runtime economy state?

### Enemies and bosses

An enemy is a reusable template. A boss may need a base enemy record plus
phase/variant records rather than one huge special-case object.

Potential fields:

- base stats and threat tier;
- AI profile and legal actions;
- abilities and weighted action selection;
- resistances, weaknesses, immunities, and status rules;
- battle role and tags;
- level scaling policy;
- rewards, drops, stealable items, and guaranteed rewards;
- defeat consequences;
- sprite, animation, portrait, VFX, audio, and battle presentation;
- boss phases, thresholds, scripted transitions, and recovery rules.

An important separation is enemy identity versus encounter tuning. The same
enemy can appear at different levels, counts, positions, or scripted phases.

### Encounters and battle setup

An encounter should answer “what battle starts here?” without copying the
enemy definitions.

Potential fields:

- encounter ID, region, location, and narrative purpose;
- expected party level and difficulty tags;
- ordered party or allowed party rules;
- enemy members, counts, levels, variants, and formation slots;
- opening effects or scripted dialogue;
- escape policy and defeat policy;
- battle background, music, and presentation;
- rewards, drops, flags, quest consequences, and follow-up events;
- repeat policy: one-shot, random, rematchable, or story-triggered.

Blind spot: random encounters and authored story encounters may share a battle
definition but have different selection rules. It may be better to keep
`encounter` separate from `encounter_trigger` or `encounter_table`.

### Effects, statuses, and targeting

Effects are likely the most important shared primitive in the whole model.
They should be ordered, inspectable, testable, and reusable across abilities,
items, dialogue consequences, quests, and rewards where semantics overlap.

Candidate effect families:

```text
damage
heal
modify_stat
modify_resource
apply_status
remove_status
protect
taunt / redirect
change_turn_order
add_party_member
remove_party_member
give_item
remove_item
give_experience
set_flag
clear_flag
start_quest
complete_quest_step
unlock_region_or_gate
start_dialogue
start_encounter
```

Every effect needs a defined target, validation behavior, failure behavior,
duration, stacking rule, and presentation hook where relevant.

Statuses deserve their own records if they have shared behavior:

- display name and icon;
- duration and tick timing;
- stack/refresh/replace rules;
- stat modifiers or triggered effects;
- immunities and resistances;
- cure/cleanse categories;
- battle and overworld scope;
- presentation and accessibility text.

Targeting should use a controlled vocabulary such as `self`, `one_ally`,
`all_allies`, `one_enemy`, `all_enemies`, `party`, `field`, or an explicit
selection rule. Targeting is not just UI; it is part of action validation.

### Dialogue and narrative graphs

The current linear dialogue is a useful start. A production dialogue record
will likely need:

- entry node and explicit node IDs;
- speaker actor ID;
- text or localization key;
- portrait/expression/audio references;
- next node or choice list;
- conditions/prerequisites;
- consequences/effects;
- one-shot, repeatable, or branch replay policy;
- interruption and return behavior;
- links to quests, encounters, flags, and party changes.

Dialogue should be a graph, not only an ordered list. A node-level condition
should be able to hide a choice without corrupting the graph. A consequence
should be applied exactly once when the design says it is one-shot, even if the
player reopens the conversation later.

Potential blind spot: localization. If text is stored directly in records now,
the schema should leave room for later text keys, speaker names, rich text,
line timing, and voice/audio without making the dialogue loader obsolete.

### Quests, flags, and progression

Progression is the glue between dialogue, combat, inventory, and world state.
Likely domains include:

- quests and ordered steps;
- objectives and counters;
- state flags and flag categories;
- prerequisites and consequences;
- party recruitment;
- item rewards and experience rewards;
- region and traversal unlocks;
- encounter completion;
- story chapter and milestone state;
- optional content and replay policy.

Flags should have stable IDs and explicit save scope. A flag might be:

- global story state;
- region state;
- room state;
- actor relationship state;
- one-time presentation state;
- battle or encounter completion state.

Blind spot: counters are not the same as booleans. “Collected three feathers”
needs a numeric or set-based state model, while “Cooper joined the party” is a
boolean/event state. The save model should support both deliberately.

### Regions, rooms, triggers, and traversal

The content schema should eventually connect data-driven records to Godot
scenes without trying to replace every scene property.

Potential content references:

- region and chapter;
- room/map ID;
- entrance and exit IDs;
- spawn points;
- interaction targets;
- encounter zones;
- dialogue or battle triggers;
- traversal requirements;
- one-shot/repeatable behavior;
- associated assets and music.

Scene geometry, collision shapes, tilemaps, and camera composition can remain
Godot scene data. The content layer should describe the game meaning of a
thing: “this is the locked route to the balcony,” not every pixel of its
collision shape.

## 6. Asset model

Assets should be first-class references, not arbitrary strings scattered across
records.

An asset record or manifest entry may contain:

```json
{
  "id": "portrait_mango_default",
  "kind": "portrait",
  "path": "assets/characters/mango/portraits/mango-default.png",
  "status": "approved",
  "dimensions": { "width": 256, "height": 256 },
  "source_record_id": "actor_mango"
}
```

The asset system should distinguish:

- source files and working files;
- approved game-facing assets;
- generated previews and contact sheets;
- animations and their frame sources;
- audio files and loop metadata;
- assets used by content records versus assets used only by scenes.

The Builder Console should provide an asset browser, thumbnails, missing-file
warnings, dimensions, provenance, and a way to attach an approved asset to a
record. Uploading or copying an asset should not silently create an untracked
file outside Git.

Potential future hosted asset storage is a separate decision. The first
canonical asset location should remain the repository because the game build
needs a reproducible local snapshot.

## 7. Versioning and export

There are at least four different versions to consider:

1. **Record ID** — permanent identity; should not change.
2. **Record revision** — content edits to one record.
3. **Schema version** — meaning/shape of fields and effects.
4. **Content snapshot version** — the complete approved set shipped in a build.

An export manifest could eventually contain:

```json
{
  "content_version": "content-0.1.0",
  "schema_version": 1,
  "source_commit": "<git commit>",
  "records": 0,
  "checksum": "<deterministic checksum>",
  "generated_at": null
}
```

If reproducibility matters, timestamps should not affect the checksum or should
be omitted from deterministic output. Export ordering, numeric formatting, and
file naming should be deterministic.

Migration policy needs to answer:

- Can old save files load against newer content?
- What happens when a referenced content ID is retired?
- Are migrations applied to authored data, exported data, save data, or all
  three?
- Can an old game build continue to use an old content snapshot?
- Does balance editing require a new content version even when the schema is
  unchanged?

## 8. Validation model

Validation should have several layers instead of one enormous checker.

### Structural validation

- Valid JSON.
- Correct record type and required fields.
- Correct scalar and array types.
- Allowed enum values.
- Numeric bounds.
- Stable ID format and filename alignment.

### Referential validation

- Every referenced actor, ability, item, enemy, status, quest, region, flag,
  node, and asset exists.
- Retired records are not referenced by approved content.
- Dialogue `next_id` and choice targets resolve.
- Effect-specific references resolve.

### Semantic validation

- An actor-owned ability points back to a valid owner or relationship.
- Encounter parties and enemies are legal.
- An item effect is compatible with its item type.
- A battle ability does not require an unavailable resource type.
- A traversal gate uses a traversal capability.
- A one-shot dialogue consequence has a replay policy.

### Build validation

- Only allowed lifecycle states enter the build.
- All required assets exist and are importable.
- The export is deterministic.
- No duplicate IDs exist across the catalogue.
- The manifest checksum matches generated files.

### Design warnings

Warnings should not necessarily block a draft, but should be visible:

- Ability has no readable counterplay.
- Enemy has no weakness or role tag.
- Encounter is above expected party level.
- Item restores an unusually large portion of max HP.
- Dialogue node is unreachable.
- Actor has no battle or overworld presentation asset.
- Record is approved but has unresolved authoring notes.

## 9. Builder Console shape

The Builder Console should be a human interface over this model, not a hidden
replacement for it.

Useful first-class views:

- Catalogue browser by record type and lifecycle status.
- Record editor with type-specific forms.
- Reference picker with search, filtering, and previews.
- Relationship graph for incoming and outgoing references.
- Effect builder with target/stat/status controls.
- Dialogue graph editor and play-through preview.
- Encounter formation and reward preview.
- Asset browser with thumbnails and missing-reference checks.
- Validation panel with errors, warnings, and source locations.
- Generated JSON preview and Git diff.
- History/revision view using Git commits.

The first implementation should be local-first and file-backed. A hosted
Vercel version could later be a read-only viewer or create Git branches and
pull requests, but hosted persistence should not be required before the forms
and schema have proved useful.

The console should not start as a generic arbitrary JSON form builder. Shared
schema primitives can be reusable, but actors, dialogue, encounters, effects,
and assets deserve deliberate interfaces because their relationships are the
hard part humans need help understanding.

## 10. JRPG blind-spot checklist

These are common areas that are easy to forget when starting with only actors,
abilities, items, enemies, encounters, and dialogue.

### Combat

- Basic attack, defend, flee, and disabled/dead states.
- Turn order and action priority.
- Accuracy, evasion, criticals, and guaranteed-hit rules.
- Elemental or thematic affinities.
- Status duration, ticking, stacking, cleansing, and immunity.
- Damage floors, healing caps, and defeat behavior.
- Multi-target selection and random-target actions.
- Battle transitions, victory, defeat, escape, and retry.
- Boss phases and scripted interruptions.
- AI behavior and weighted action choice.
- Battle UI labels, icons, animations, sounds, and feedback.

### Progression

- Experience, levels, level caps, and growth curves.
- Learning abilities and forgetting/replacing abilities.
- Equipment, slots, upgrades, and restrictions.
- Inventory stacks, currencies, shops, and selling.
- Party order, formation, recruitment, and temporary members.
- Rewards that are items, flags, abilities, experience, or new routes.

### Narrative

- Branches, conditions, choices, and hidden choices.
- One-shot versus repeatable dialogue.
- Localization and text keys.
- Portraits, expressions, voice/audio, and timing.
- Quest steps, counters, and failure/abandonment.
- Story flags with different scopes.
- Post-battle and post-dialogue consequences.
- Save compatibility when story records change.

### World

- Regions, rooms, exits, spawn points, and map ownership.
- Interaction targets and prompt text.
- Traversal gates and leader-specific optional content.
- Random encounter tables versus authored encounters.
- One-shot triggers and resettable world state.
- Shops, chests, pickups, destructibles, and inspectable props.
- Music zones, ambience, battle backgrounds, and presentation transitions.

### Production and tooling

- Draft/review/approval ownership.
- Balance notes and playtest results.
- Asset provenance and licensing.
- Deprecation and migration of IDs.
- Duplicate or unreachable content.
- Search, tags, and backlinks.
- Content snapshots associated with builds.
- A way to see what is implemented versus merely authored.

## 11. Open decisions for the schema mind-map

These are the questions worth deciding before broad content production:

1. What is the canonical authored source: individual JSON records, a structured
   workbook imported to JSON, or JSON edited through the Builder Console?
2. Is the Builder Console a local file editor first, or does it write GitHub
   branches and pull requests from its first hosted version?
3. Are abilities reusable shared records with ownership relationships, or are
   they always owned by one actor?
4. Are equipment and consumable items one domain with subtypes, or separate
   domains sharing effects?
5. Which mechanics are content records and which remain code-defined built-ins?
6. What is the complete canonical stat vocabulary for this game?
7. Which resources exist besides HP and Zoom?
8. Are elemental affinities part of the game, and if so are they elemental,
   emotional, household, regional, or a combination?
9. What is the status catalogue and how do statuses stack or expire?
10. How are ability learning, traversal capabilities, and story unlocks
    represented without conflating them?
11. What is the minimum quest and state-flag model needed for the first chapter?
12. How are random encounter tables represented separately from battle setups?
13. How are boss phases authored without creating bespoke one-off code for every
    boss?
14. How will text localization work if the game expands beyond one language?
15. What is the asset ID/path/manifest rule for sprites, portraits, animation,
    VFX, music, and sound?
16. What does `approved` mean, and who is allowed to approve it?
17. Which validation errors block export, and which are warnings?
18. What must remain compatible with old save files?
19. What belongs in Git history versus explicit record revision metadata?
20. What does a content snapshot contain, and how is it tied to a game build?

## 12. Recommended order of work

Do not attempt to solve the whole catalogue at once.

### Decision pass

- Draw the domain mind-map.
- Mark each node as definition, relationship, runtime state, or presentation.
- Lock the stat/effect/status vocabulary needed by the first combat slice.
- Decide the authored source and Builder Console boundary.
- Decide the asset reference model.
- Decide the minimum flags/quests/dialogue conditions needed by Stage 1–2.

### Schema pass

- Turn approved decisions into formal record shapes.
- Add shared envelopes and schema versioning.
- Add effect and reference rules.
- Define the export manifest.
- Keep unresolved future fields explicitly optional or out of the schema.

### Tooling pass

- Build a local catalogue viewer.
- Add structural and referential validation.
- Add one deliberate editor for actors and abilities.
- Add dialogue and encounter previews.
- Add asset browsing and missing-file checks.
- Save valid JSON and show a Git diff.

### Runtime pass

- Build a Godot content loader and ID index.
- Load the Stage 1 records through the real systems.
- Keep player state separate from content definitions.
- Add snapshot/version checks to builds.

### Expansion pass

- Add quests, flags, regions, statuses, equipment, shops, bosses, and
  localization only when the next playable slice requires them.

The success criterion is not “we have fields for every possible JRPG system.”
It is “a human can author a small piece of content, understand every
relationship, validate it, preview it, and use the same approved data in the
game without bespoke duplication.”

