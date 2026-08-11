# Mango and Cooper

A full-scope 2D RPG starring our real pets, Mango (cat) and Cooper (dog). Their humans vanish one night; the animals gain speech and magical powers, household technology awakens as monsters, and the truth — a new baby — isn't revealed until the end. It's a story about love, grief, courage, and a family changing rather than disappearing.

Full premise, world, and cast: [`docs/GAME_BIBLE.md`](docs/GAME_BIBLE.md).

## Status

Pre-vertical-slice. See [`docs/PRODUCTION_ROADMAP.md`](docs/PRODUCTION_ROADMAP.md) for the staged build order (Room → House → Neighbourhood → Open World) and [`docs/VERTICAL_SLICE.md`](docs/VERTICAL_SLICE.md) for the current first milestone.

## How this gets built

Every stage follows the same practice: **toy → vertical slice → game.** AI accelerates first drafts and production friction (concept art, sprite variations, dialogue drafts, music sketches, boilerplate code); Sean and Lillian retain authorship over premise, characters, humour, emotional beats, and final art/audio direction. This is a method for building deliberately at scale, not a way to keep the game small.

Platform target: **PC via Steam**, keyboard + controller. Mobile/Switch are open future export targets, not near-term commitments.

## Tool stack

- **Godot 4** — engine
- **PixelLab** — reference-driven pixel art (MCP-connected in both Claude Code and Codex)
- **Aseprite** — sprite cleanup, palette control, animation timing
- **Ableton** — music composition, alongside AI-assisted drafting and possible composer collaborators
- **Claude Code / Codex** — GDScript, content schema, tests, repetitive asset integration
- **GitHub** — source of truth for code, content, and docs
- **Supabase** — optional future content-authoring layer once the schema is proven (see `docs/CONTENT_SCHEMA.md`)

## Docs

- [`docs/GAME_BIBLE.md`](docs/GAME_BIBLE.md) — full story, world, cast
- [`docs/PRODUCTION_ROADMAP.md`](docs/PRODUCTION_ROADMAP.md) — staged build order
- [`docs/VERTICAL_SLICE.md`](docs/VERTICAL_SLICE.md) — current milestone
- [`docs/ART_BIBLE.md`](docs/ART_BIBLE.md) — visual direction and asset pipeline
- [`docs/AUDIO_BIBLE.md`](docs/AUDIO_BIBLE.md) — music/audio direction and pipeline
- [`docs/CONTENT_SCHEMA.md`](docs/CONTENT_SCHEMA.md) — data model and ID conventions
