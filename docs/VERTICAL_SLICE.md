# Vertical Slice — Stage 1: The Room

This is the first proof of concept, not the ceiling of the game. See `PRODUCTION_ROADMAP.md` for what comes after it and `GAME_BIBLE.md` for the full story this slice is a fragment of.

## Scope

One room: the apartment living room.

## The Slice

1. Mango can walk across the apartment (four-direction movement, working collision with furniture).
2. Mango can inspect the empty food bowl (one meaningful interactive object).
3. Cooper enters and exchanges dialogue with Mango.
4. The player can switch the active leader between Mango and Cooper.
5. Mango can climb or cross something Cooper cannot; Cooper can move, dig, or scent-track something Mango cannot (at least one instance each — proves the field-ability-gating concept, does not need to be a full puzzle yet).
6. A Dust Bunny (or the Vacuum Cleaner directly, if the first encounter is simplified for the slice) triggers a turn-based battle.
7. Mango and Cooper win using character-specific abilities.
8. A small objective unlocks the door, and one short closing beat completes the scene.

## What This Validates

Pet photography → PixelLab generation → manual Aseprite cleanup → Godot import → character movement → dialogue → field abilities → structured content data → battle transition → Claude Code working safely inside the project structure.

## Definition of Done

- All 8 steps above are playable in the running Godot project, not just designed.
- Mango and Cooper's sprites and movement feel recognisably like the real animals, not generic RPG cat/dog placeholders.
- The battle uses real `data/` content records (see `CONTENT_SCHEMA.md`), not hardcoded values in a scene script.
- The scene is playable start to finish without manual intervention (no "the door doesn't actually open yet").

## Explicitly Out of Scope for This Slice

- Any region beyond the single room
- Rocky, Milo, Charlie, King Jeff
- The Zoom Meter (can be stubbed/skipped)
- Music beyond a placeholder or silence — full audio direction lives in `AUDIO_BIBLE.md` and is not a slice blocker
- Steam packaging or any export target
