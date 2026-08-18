# Agent startup guide

Start with [`docs/README.md`](docs/README.md) for the documentation map and
source-of-truth rules. Read the specific document relevant to the task before
changing code, content, or assets.

This is a full-scope, data-driven 2D RPG starring the real pets Mango and
Cooper. Build it deliberately in stages; the current build target and exit
criteria live in [`docs/production/PRODUCTION_ROADMAP.md`](docs/production/PRODUCTION_ROADMAP.md)
and [`docs/production/VERTICAL_SLICE.md`](docs/production/VERTICAL_SLICE.md).

For gameplay behaviour, follow the reusable runtime contracts in
[`docs/design/TECHNICAL_GAME_DESIGN.md`](docs/design/TECHNICAL_GAME_DESIGN.md).
For the active room, follow its build card before expanding scope:
[`docs/production/slices/TUTORIAL_ROOM_BUILD.md`](docs/production/slices/TUTORIAL_ROOM_BUILD.md).

## Non-negotiable rules

- Keep content data-driven. Use stable string IDs from [`docs/design/CONTENT_SCHEMA.md`](docs/design/CONTENT_SCHEMA.md); do not hard-code dialogue, items, or statistics in UI/scene scripts.
- Preserve the approved visual direction in [`docs/art/ART_BIBLE.md`](docs/art/ART_BIBLE.md) and follow the production workflow in [`docs/art/ART_PRODUCTION_PIPELINE.md`](docs/art/ART_PRODUCTION_PIPELINE.md).
- AI output is provisional until Sean/Lillian approve it. Do not invent major character traits, story beats, or historical/cultural claims without approval.
- Do not copy copyrighted assets or named visual identities.
- Run the project after meaningful changes and validate references between content records.
- Do not open the next production stage until the current stage's exit criteria are playable in the running game.
- The chosen overworld leader remains locked for the playthrough; every main route must be completable by either leader alone. See [`docs/vision/GAME_BIBLE.md`](docs/vision/GAME_BIBLE.md).

## Asset and composition rules

The asset lifecycle is `reference → input → wip → approved`, with Godot
composition resources in a sibling `composite/` folder. The detailed rules,
including family-vs-room placement, third-party provenance, and promotion,
live in the Art Production Pipeline.

- `reference/`: look-only references; never load or edit directly.
- `input/`: unreviewed downloaded or generated material; do not use in the running game.
- `wip/`: actively curated material. During active room composition, Godot may reference that room's WIP textures.
- `approved/`: human-approved, Godot-authoritative content.
- `composite/`: TileSets, SpriteFrames, scenes/resources, and other Godot-side assembly.
- Keep static sheets intact where possible. Use Godot TileSet atlases for grid-native tiles and Sprite2D regions/scenes for coherent multi-cell furniture. Use separate assets for animated, interactive, or independently reusable props.

Raw `input/` remains excluded from Godot. A room-specific WIP exception is
allowed only while that room is being composed; promote accepted content to
`approved/` and update its `composite/` resources once the room is accepted.

## Where to look

- Story, world, and cast: [`docs/vision/GAME_BIBLE.md`](docs/vision/GAME_BIBLE.md)
- Visual rules and asset workflow: [`docs/art/`](docs/art/)
- Runtime contracts: [`docs/design/TECHNICAL_GAME_DESIGN.md`](docs/design/TECHNICAL_GAME_DESIGN.md)
- Design and data: [`docs/design/`](docs/design/)
- Build stages and active room work: [`docs/production/`](docs/production/)
- Audio: [`docs/audio/AUDIO_BIBLE.md`](docs/audio/AUDIO_BIBLE.md)
- MCP/tooling: [`docs/engineering/MCP.md`](docs/engineering/MCP.md)
- Runtime content: `data/`
- Godot project: `scenes/`, `scripts/`, `project.godot`

For documentation ownership and update rules, see
[`docs/engineering/OWNERSHIP_AND_CHANGE_CONTROL.md`](docs/engineering/OWNERSHIP_AND_CHANGE_CONTROL.md).
