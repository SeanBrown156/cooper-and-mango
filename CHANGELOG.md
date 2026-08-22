# Changelog

## Unreleased

- Locked high top-down environment perspective, replacing the conflicting
  three-quarter rule in the Art Bible.
- Added the 512×384 Mango Tutorial Room technical specification and a complete
  PixelLab tile/sprite generation ledger with explicit orientation and scale.
- Made PixelLab the primary environment-production engine: well-briefed generated tilesets, room kits and non-identity props can move directly through WIP into Godot and be approved after runtime validation, without mandatory manual cleanup.
- Added the interaction visual grammar: crisp dark near-black outlines for characters/key interactables, softer outlines for passive scenery, and a 16×16 default footprint for small inspectable props.

- Added `docs/design/TECHNICAL_GAME_DESIGN.md`, defining reusable runtime contracts for player movement, interaction, dialogue, encounters, explicit game modes and scene responsibilities.
- Added `docs/production/slices/TUTORIAL_ROOM_BUILD.md`, a narrow executable build card for the first Mango movement postcard in the Tutorial Room.
- Linked technical design and active build-card guidance from the documentation index and agent startup guide.
- Reorganised project documentation by function under `docs/`.
- Consolidated MCP setup, capabilities, and governance into `docs/engineering/MCP.md`.
- Established `README.md` as the project landing page, `CLAUDE.md` as the agent startup guide, and `docs/README.md` as the canonical documentation index.
- Documented ownership and documentation change control in `docs/engineering/OWNERSHIP_AND_CHANGE_CONTROL.md`.
- Documented the overlapping roles of PixelLab, SpriteCook and Aseprite in the
  asset-production workflow.
- Consolidated AI-assisted generation guidance into the Art Production Pipeline;
  removed the redundant standalone AI Asset Lab document.
- Added character-root visual briefs and the `cm-character-visual-brief` skill;
  clarified Art Bible, Pipeline and Game Bible ownership boundaries.
