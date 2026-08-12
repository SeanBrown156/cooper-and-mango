# Audio Bible

## Direction

Same mood as the visual art direction: warm domestic fantasy, SNES/early-PlayStation JRPG energy, without copying any existing game's identifiable themes. Music should carry the same emotional range as the story — cosy and funny in the domestic chapters, genuinely tender and sad around Charlie's arc and The Absence, triumphant without irony at the ending.

## Tool Stack

- **Ableton** — primary composition tool (Sean's existing skill)
- **AI-assisted drafting** — for sketches, motif ideas, and quickly trying directions before committing studio time
- **Composer friends** — potential collaborators for specific themes or the score as a whole; treat as an open resource, not a plan dependency
- **Audacity** — recording/editing raw pet sound sources

No single approach is locked in — this is intentionally a hybrid pipeline. Whichever method produces a theme, the same review bar applies: does it sound like *this* game and *these* characters, not a generic JRPG soundtrack.

## Planned Themes

Start per-character, expand per-region as regions get built (see `PRODUCTION_ROADMAP.md` — don't score regions that don't exist yet):

- **Mango's theme** — reflects the survival→love arc; could start guarded/minor and resolve warmer
- **Cooper's theme** — reflects anxiety→courage; earnest, a little unsteady, building to something steadier
- **Regional themes** — one per elemental region once that region enters production (Empty House, Drowned Park, Iron Estate, Eastern Cavoodle Kingdom, Tower of Wind, High Overworld, Road Home, Centre of Absence)
- **Charlie's motif** — a quiet, plain, wise theme; should recur (not literally repeat) as a mechanical presence after his farewell — a learned ability's cue, a protective moment, a memory
- **The Absence** — the most tonally distinct piece in the game; assembled dread built from fragments of earlier themes, mirroring how the boss itself is assembled from fragments of the journey

## Pet Sound Recording

Per the source note's "Handmade Emotional Core": record real barks, meows, purring, paws on the floor, collar jingles, food-bowl noises. Process these into battle effects, UI cues, and ability sound design rather than using generic SFX libraries wherever a real sound can do the job.

## Folder and Versioning Convention

```
assets/audio/
├── music/
│   └── <theme-name>/
│       ├── source/        (Ableton project files, stems — gitignored via assets/reference pattern if large; confirm LFS decision first)
│       └── exports/       (final mixed/mastered exports, e.g. mango_theme_v1.ogg)
└── sfx/
    └── <category>/        (e.g. battle/, ui/, pet-sounds/)
```

- Export files use a stable name + version suffix (`cooper_theme_v2.ogg`) so Godot references don't break when a track is revised — bump the version rather than overwriting silently.
- Raw Ableton projects and unprocessed pet-sound recordings live under `assets/reference/` per the same provenance rule as visual reference material (see `ART_BIBLE.md` and the open Git LFS question in the project plan).
- Only finished, mixed exports go under `assets/audio/*/exports/` and get referenced by the game.

## Open Questions

- Which themes get composer-friend involvement vs. staying in-house — decide per-theme as they come up, not in advance.
- Whether region themes need a shared musical "family" motif (a game-wide leitmotif) that regional themes vary — worth deciding once at least two regional themes exist to compare.
