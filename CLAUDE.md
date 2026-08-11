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
- Preserve the approved art direction (`docs/ART_BIBLE.md`) and audio direction (`docs/AUDIO_BIBLE.md`)
- Preserve the emotional premise — especially Charlie's arc, which should stay sincere rather than played for shock or cheap sentiment
- Do not open the next production stage's scope before the current stage's exit criteria are actually true in the running game
- The overworld leader is locked to the title-screen choice for the whole playthrough (`docs/GAME_BIBLE.md`'s Protagonist Choice) — every region needs a route fully completable by *either* leader alone; don't gate main-path progress behind the other pet's ability

## Where things live

- `docs/GAME_BIBLE.md` — the full story/world/cast (the destination)
- `docs/PRODUCTION_ROADMAP.md` — staged build order (the path)
- `docs/VERTICAL_SLICE.md` — current first-milestone detail
- `docs/ART_BIBLE.md` / `docs/AUDIO_BIBLE.md` — visual/audio direction and pipelines
- `docs/CONTENT_SCHEMA.md` — data shape and ID conventions
- `data/` — actual content records
- `assets/` — game-ready art/audio (raw source material lives in `assets/source/`, gitignored for now)
- `scenes/`, `scripts/` — Godot project
