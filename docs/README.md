# Cooper & Mango documentation

This folder is organised by the part of the game-making process a document
serves. Use the most specific document below as the source of truth; do not
duplicate a decision in several bibles.

## How the project points together

```text
README.md       project landing page
    ↓
CLAUDE.md       agent startup rules
    ↓
docs/README.md  canonical documentation map
    ↓
specific source-of-truth document
```

The root README is for orienting a person to the project. `CLAUDE.md` is the
short operational context loaded for agents. This file is the complete map;
the documents below contain the actual decisions.

## Vision

- [Game Bible](vision/GAME_BIBLE.md) — premise, player fantasy, world, cast and story spine.
- [Inspiration](vision/INSPIRATION.md) — reference board and thematic/structural inspiration. This is reference material, not locked direction.

## Art

- [Art Bible](art/ART_BIBLE.md) — locked visual rules, dimensions, palette, pixel grammar and art acceptance criteria.
- [Art Production Pipeline](art/ART_PRODUCTION_PIPELINE.md) — how references, third-party assets, PixelLab output, Aseprite masters and Godot composition move through the lifecycle.
- [Asset Licenses](art/ASSET_LICENSES.md) — provenance and permissions for external assets.

Character-specific visual briefs live with their owning assets at
`assets/characters/<character>/CHARACTER_VISUAL_BRIEF.md` and are maintained
with `$cm-character-visual-brief`.

## Design and content

- [Combat Design](design/COMBAT_DESIGN.md) — battle identity and progression built around Instinct reactions, Zoom and Companionship.
- [Items, Abilities and Progression Catalogue](design/ITEMS_ABILITIES_PROGRESSION.md) — exploratory first draft of pet-themed character kits, items, equipment, statuses and progression; not a locked implementation roster.
- [Technical Game Design](design/TECHNICAL_GAME_DESIGN.md) — reusable runtime contracts for player movement, interaction, dialogue, encounters, states and scene responsibility.
- [Content Schema](design/CONTENT_SCHEMA.md) — structured content records, IDs, relationships and publishing shape.
- [Content Schema Plan](design/CONTENT_SCHEMA_PLAN.md) — exploratory schema map, JRPG content domains, authoring/runtime boundaries and open decisions.
- [Core Mechanics Library](design/MECHANICS_LIBRARY.md) — shared contracts for movement, interaction, battle actions, Zoom Meter, and traversal abilities.

## Production

- [Production Roadmap](production/PRODUCTION_ROADMAP.md) — stages, sequencing and scope.
- [Vertical Slice](production/VERTICAL_SLICE.md) — the current playable validation target and definition of done.
- [Project Management Convention](production/PROJECT_MANAGEMENT.md) — how GitHub Issues, Milestones, Labels and Assignees divide and allocate the work.
- [Tutorial Room Build Card](production/slices/TUTORIAL_ROOM_BUILD.md) — current executable work order and Godot acceptance checks for Mango's first playable postcard.

## Audio

- [Audio Bible](audio/AUDIO_BIBLE.md) — music, sound, pet recordings and audio production direction.

## Engineering and tools

- [MCP Guide](engineering/MCP.md) — MCP setup, capabilities, limits and governance.

## Ownership model

The project is small, so these are areas of ownership rather than separate
departments:

- Creative direction: Sean, with Lillian's taste and character approval.
- Character likeness and humour: Lillian and Sean.
- Art production: Aseprite/PixLab workflows, palette and asset promotion.
- Environment composition: Godot TileSets, Sprite2D regions, scenes and collisions.
- Design and narrative: Game Bible, systems, dialogue and content records.
- Engineering: Godot code, tools, integrations and runtime systems.
- Audio: music, ambience, sound effects and pet recordings.
- Production/QA: roadmap, vertical-slice validation, playtesting and release hygiene.

When a decision changes a locked rule, update the relevant source-of-truth
document and any affected implementation guidance in the same change.