# Cooper & Mango

A full-scope 2D RPG starring our real pets, Mango (cat) and Cooper (dog). Their humans vanish one night; the animals gain speech and magical powers, household technology awakens as monsters, and the truth — a new baby — isn't revealed until the end. It's a story about love, grief, courage, and a family changing rather than disappearing.

Full premise, world, and cast: [`docs/vision/GAME_BIBLE.md`](docs/vision/GAME_BIBLE.md).

## Status

Pre-vertical-slice. See [`docs/production/PRODUCTION_ROADMAP.md`](docs/production/PRODUCTION_ROADMAP.md) for the staged build order (Room → House → Neighbourhood → Open World) and [`docs/production/VERTICAL_SLICE.md`](docs/production/VERTICAL_SLICE.md) for the current first milestone.

## How this gets built

Every stage follows the same practice: **toy → vertical slice → game.** AI accelerates first drafts and production friction (concept art, sprite variations, dialogue drafts, music sketches, boilerplate code); Sean and Lillian retain authorship over premise, characters, humour, emotional beats, and final art/audio direction. This is a method for building deliberately at scale, not a way to keep the game small.

Platform target: **PC via Steam**, keyboard + controller. Mobile/Switch are open future export targets, not near-term commitments.

## Tool stack

### Creative direction and reference

- **FigJam** — inspiration, mood boards, visual references, game examples, palette exploration and art-direction discussions
- **Procreate** — loose sketches, character ideas, poses, environment concepts and visual problem-solving
- **Real photos** — likeness and physical reference for Mango, Cooper, the home, furniture and distinctive objects
- **Gemini / ChatGPT** — rapid concept exploration, composition ideas, critique and comparison

### Pixel-art production

- **PixelLab** — reference-driven pixel-art generation, environment kits, tilesets, props, character candidates, variants and animation candidates
- **Pixquare** — iPad and Apple Pencil drawing, cleanup, repainting and animation; supports Aseprite round-tripping
- **Aseprite** — desktop production master for precise pixel cleanup, palette control, animation timing, sprite sheets and editable masters

### Game production and project memory

- **Godot 4** — engine, scene composition and runtime validation
- **GitHub** — source of truth for code, content, assets and documentation
- **Claude Code / Codex** — GDScript, content schema, tests and repetitive asset integration
- **Ableton** — music composition and audio production
- **Supabase** — optional future content-authoring layer once the schema is proven (see `docs/design/CONTENT_SCHEMA.md`)

The detailed workflow and asset lifecycle are documented in [`docs/art/ART_PRODUCTION_PIPELINE.md`](docs/art/ART_PRODUCTION_PIPELINE.md) and [`_studio/README.md`](_studio/README.md).

## Documentation

Start with [`docs/README.md`](docs/README.md), the canonical documentation map. It points to the source-of-truth document for each area and explains who owns each kind of decision.
