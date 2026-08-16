# Vertical Slice — Stage 1: The Tutorial Room

This is the first proof of concept, not the ceiling of the game. See [`PRODUCTION_ROADMAP.md`](PRODUCTION_ROADMAP.md) for what comes after it and [`../vision/GAME_BIBLE.md`](../vision/GAME_BIBLE.md) for the full story (Story Spine, Protagonist Choice) this slice is a fragment of.

## Scope

The title-screen protagonist choice, plus one starting room (Mango's or Cooper's, depending on the choice) through to the party forming.

## The Slice

1. Title screen asks "Do you like cats or dogs?" — **Cats** starts as Mango (party order "Mango & Cooper"); **Dogs** starts as Cooper (party order "Cooper & Mango"). Both lead to the same underlying game — see [`../vision/GAME_BIBLE.md`](../vision/GAME_BIBLE.md)'s Protagonist Choice section.
2. The chosen character walks their starting room (four-direction movement, working collision with furniture) and inspects at least one meaningful object.
3. The spider-plant trigger event plays — the inciting hallucination/magical-awakening beat (speech, powers, the world beginning to shift).
4. The character leaves the room.
5. They meet the other pet for the first time; a short two-character dialogue beat plays.
6. The party of two is formed. The chosen character (Mango or Cooper) remains the overworld leader for the rest of the playthrough — the other pet joins as a full battle party member but is not switchable as exploration leader. See [`../vision/GAME_BIBLE.md`](../vision/GAME_BIBLE.md)'s Protagonist Choice section.

## What This Validates

Pet photography → PixelLab generation → manual Aseprite cleanup → Godot import → character movement → the protagonist-choice branch → dialogue → party formation → structured content data → Claude Code working safely inside the project structure.

## Definition of Done

- All 6 steps above are playable in the running Godot project for **both** starting choices (Cats and Dogs), not just designed.
- Mango and Cooper's sprites and movement feel recognisably like the real animals, not generic RPG cat/dog placeholders.
- Dialogue and any triggered content use real `data/` records (see [`../design/CONTENT_SCHEMA.md`](../design/CONTENT_SCHEMA.md)), not hardcoded values in a scene script.
- The scene is playable start to finish without manual intervention.

## Explicitly Out of Scope for This Slice

- The rest of the Empty House, and the Mi-chan battle — that's Stage 2's climax, not this one
- Any region beyond the Tutorial Room
- Rocky, Milo, Charlie, King Jeff, the Goose
- The Zoom Meter (can be stubbed/skipped)
- Music beyond a placeholder or silence — full audio direction lives in [`../audio/AUDIO_BIBLE.md`](../audio/AUDIO_BIBLE.md) and is not a slice blocker
- Steam packaging or any export target
