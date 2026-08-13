# Project principles

This is a full-scope, data-driven 2D RPG built in deliberate stages (see `docs/PRODUCTION_ROADMAP.md`). It is personal — starring real pets, Mango and Cooper — but built to genuinely work as a game other people can play.

Priorities, in order:
1. A playable current-stage milestone (see `docs/PRODUCTION_ROADMAP.md` for which stage is active)
2. Simple, legible systems
3. Content stored separately from game logic
4. No premature abstractions
5. No feature without a testable player outcome

## Technical rules

- Use stable string IDs for all content (`docs/CONTENT_SCHEMA.md`)
- Never hard-code dialogue, items, or statistics in UI/scene scripts — read from `data/`
- Keep scenes small and composable
- Preserve pixel-art import settings (nearest-neighbour filtering, integer scaling)
- Run the project after meaningful changes
- Validate references between content records (an ability pointing at a missing actor ID is a bug, not a warning)
- Update `docs/` when schemas or scope change — the docs are meant to stay true, not become historical

## Creative rules

- AI output (art, music drafts, dialogue drafts) is provisional until Sean/Lillian approve it
- Do not invent major character traits, story beats, or historical/cultural claims without approval — especially for the Eastern Cavoodle Kingdom satire, which needs to stay playful and specific rather than mapping onto anything real
- Do not copy copyrighted assets or named visual identities
- Preserve the approved art direction (`docs/ART_BIBLE.md`) and use `docs/ART_PRODUCTION_PIPELINE.md` for the project-specific iterative AI/human asset-production workflow
- Preserve the emotional premise — especially Charlie's arc, which should stay sincere rather than played for shock or cheap sentiment
- Do not open the next production stage's scope before the current stage's exit criteria are actually true in the running game
- The overworld leader is locked to the title-screen choice for the whole playthrough (`docs/GAME_BIBLE.md`'s Protagonist Choice) — every region needs a route fully completable by *either* leader alone; don't gate main-path progress behind the other pet's ability

## Where things live

- `docs/GAME_BIBLE.md` — the full story/world/cast (the destination)
- `docs/PRODUCTION_ROADMAP.md` — staged build order (the path)
- `docs/VERTICAL_SLICE.md` — current first-milestone detail
- `docs/ART_BIBLE.md` — visual direction and technical art rules
- `docs/ART_PRODUCTION_PIPELINE.md` — project-specific character, tiles, props, AI multiplication, cleanup and Godot-validation workflow
- `docs/AUDIO_BIBLE.md` — audio direction and pipeline
- `docs/CONTENT_SCHEMA.md` — data shape and ID conventions
- `docs/INSPIRATION.md` — reference material for art direction, tone, and structure (visual reference board + thematic references)
- `data/` — actual content records
- `assets/` — a pure content library: raw PNGs/audio/etc. that Godot loads via `res://`, organized by *asset family* first (`characters/mango/`, `characters/cooper/`, `characters/rocky/`, `npcs/`, `environments/`, `ui/`, `audio/`, `enemies/`, `palette/`), with lifecycle stage as a subfolder. There is no top-level `portraits/` family — a portrait is one of a specific character's own scale-tiers (per the Art Bible: overworld/battle/portrait are the same character redrawn at different scales), so it lives nested under that character, e.g. `characters/mango/approved/portrait/`, never as its own top-level bucket. The lifecycle is `reference/` → `input/` → `wip/` → `approved/`, plus a same-level `composite/` for Godot wiring. **Two levels this can attach at:** for `characters/`, the family root *is* the specific instance (`characters/mango/` — one named character), so lifecycle folders sit directly under it. For `environments/`, the family (`environments/`) can contain multiple distinct rooms/regions, so there are two tiers: family-level `reference/`/`input/`/`wip/` hold material *not yet tied to any specific room* (e.g. a downloaded tileset pack nobody's assigned yet), while a specific room (`environments/tutorial_room/`) has its own full `reference/`/`input/`/`wip/`/`approved/`/`composite/` set for material that *is* tied to it. The moment something's actually wired into a specific scene, it's by definition tied to that specific room/instance, so it lives at that level, never floating at the family level — this is what "wired into a scene" always cashes out to concretely:
  - `reference/` — photos, other game images, other people's reference points — **not usable as something to work on directly**, never edited or loaded by Godot: real photos, sketches of Mango/Cooper/Rocky — untracked in git except folder structure (`.gdignore`/`.gitkeep`), excluded from the Godot editor's filesystem scan via an empty `.gdignore` in each `reference/` folder. Subdivided by *source* (`photos/`, `sketches/`, `locked/` — locked design-direction stills), not by target sprite type — a reference photo isn't yet committed to becoming one specific scale-tier. Deliberately called `locked/`, not `approved/` — that word is reserved for the family's own lifecycle tier below, and reusing it here for something different was exactly the kind of ambiguity this whole model exists to kill.
  - `input/` — actual game sprites/art that ARE usable as a starting point, just not reviewed or cleaned up yet: off-the-shelf vendor/found asset packs meant to be cut, remixed, or composited into final art (e.g. licensed third-party packs not yet wired into a scene), *and* initial AI generations ready for cleanup — a raw PixelLab batch, a raw Gemini or ChatGPT sprite-sheet export, anything freshly generated that nobody has reviewed or started cleaning up yet — same untracked/`.gdignore` treatment as `reference/`. Also subdivided by source, not target type.
  - `wip/` — actively being hand-worked on right now: a human is currently mid-edit (draft/mid-edit `.aseprite` files, disposable comparison renders, third-party packs genuinely mid-transformation) — tracked in git (this is the shared handoff point with Lillian) and also excluded from the Godot scan via `.gdignore`. Once something in `input/` gets picked and a human starts actively cleaning/redrawing it, it moves to `wip/`. Split into type subfolders (`overworld/`, `battle/`, `portrait/`, etc.) only when a family actually has more than one type in flight at once — not a hard requirement.
  - `approved/` — the current authoritative version, promoted from `wip/` once locked in: final, Godot-loaded content. Deliberately not called "final" — approved content can still be superseded by a new approved version later, it just isn't presumed permanent. **Always** split into type subfolders here, even if a family only has one type today (e.g. `approved/overworld/`) — unlike `wip/`, this split is not optional, since this is the tier Godot actually loads and it must be unambiguous which content is which type. For non-character families, "type" means whatever that family's content actually is (e.g. a room's approved props/tileset), not literally `overworld/battle/portrait`.
  - `composite/` — that family's Godot-specific composition resources (TileSets, SpriteFrames, Themes, and similar `.tres` files) that assemble its `approved/` content into game-usable resources; `reference/`/`input/`/`wip/`/`approved/` never contain `.tres`/`.tscn` composition logic, only raw content. Not called `resources/` since Godot's own engine vocabulary already overloads "Resource" for nearly everything, including plain textures. E.g. `assets/environments/tutorial_room/composite/tutorial_room_tileset.tres`.
  - `thirdparty/` — licensed external packs that ARE wired into a scene right now, nested *inside* that specific instance's `approved/` (e.g. `assets/environments/tutorial_room/approved/thirdparty/bitglow_pixelinterior_lrk_v1_1/`, since Bitglow is wired into the shipped Tutorial Room specifically) — never a top-level-of-family bucket, because anything actually wired in is by definition tied to one specific room/scene, same as any other approved content. It's kept sub-labeled `thirdparty/` only so licensing provenance (see `docs/ASSET_LICENSES.md`) stays obvious at a glance, not because it's a different lifecycle tier. Fully scanned/imported by Godot like the rest of `approved/`.
  - `assets/npcs/` — ambient/background wildlife that is neither named story cast (`characters/`) nor canonical monsters (`enemies/` — per the Game Bible, this game's enemies are transformed household objects/appliances, not animals)
  - `assets/_unsorted/` — a top-level holding pen for files of unknown origin/purpose, not sorted into any family
  - (restructured from the old `raw/`/`src/`/`assets/`/`.scratch/`/`assets/thirdparty/` split into this per-family model on 2026-08-13, then refined from reference/material/wip to reference/input/wip/approved+composite on 2026-08-14, then had the family-vs-specific-instance (e.g. room) two-tier rule clarified and the last floating family-level `thirdparty/` folded into its room's `approved/` on 2026-08-14, see GitHub issue #20)
- `scenes/`, `scripts/` — Godot project. Scenes are node trees — the concrete, placed instances (e.g. `tutorial_room.tscn`'s `TileMap` node *using* a `composite/` TileSet resource); scripts are the actual behavior, attached to nodes inside scenes. The chain is: raw pixels (`assets/<family>/approved/`) → structural meaning (`assets/<family>/composite/`) → placed as real objects (`scenes/`) → given behavior (`scripts/`).
