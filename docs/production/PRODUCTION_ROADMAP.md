# Production Roadmap

This translates the full vision in [`../vision/GAME_BIBLE.md`](../vision/GAME_BIBLE.md) into deliberate build stages. The "toy → vertical slice → game" practice is the *method* used at every stage — it is not a cap on the final scope. Each stage below has to be proven working before the next stage's scope is opened up, so growth is intentional rather than accidental.

## Stage 0 — Toy (pre-slice)

Prove the smallest possible thing: a character that can move and interact with one object, using placeholder art and the real data schema.

**Exit criteria:** Mango moves on a greybox map and can inspect one object. No battle, no Cooper, no polish.

## Stage 1 — Room (the Vertical Slice)

See [`VERTICAL_SLICE.md`](VERTICAL_SLICE.md) for full detail. The Tutorial Room from [`../vision/GAME_BIBLE.md`](../vision/GAME_BIBLE.md)'s Story Spine: the player picks Mango or Cooper, plays a short solo intro, the spider-plant trigger kicks off the magical awakening, they leave the room, and meet the other pet — the party of two forms.

**Exit criteria:**
1. Protagonist choice screen (Mango or Cooper) works and actually changes the opening scene
2. The chosen character walks their starting room and interacts with at least one object
3. The spider-plant trigger event plays (the inciting hallucination/awakening beat)
4. The character leaves the room and meets the other pet
5. A short two-character dialogue beat plays and the party of two is formed

This is the proof that "moving Mango (or Cooper) already feels recognisably like them" — the decisive early milestone, not merely a generic cat or dog moving. The Mi-chan battle is deliberately **not** part of this stage — it's the climax of Stage 2.

## Stage 2 — House

Expand from the Tutorial Room into the full **Empty House** chapter: the rest of the apartment, the full set of domestic enemies (Dust Bunnies, Crumb Slimes, Static Sprites, Vinegar Wisps, the Mop Serpent, Hairdryer Wyvern, Washing Machine Mimic, the Doorbell), and the complete Mecha Mi-chan boss encounter (not just a placeholder fight).

**Exit criteria:** the apartment's sealed exit opens; Mecha Mi-chan is destroyed; the locked-leader traversal ability (climb/squeeze/sense for a Mango playthrough, swim/pull/track/dig for a Cooper playthrough) is implemented and used to solve at least one puzzle, tested for **both** starting choices.

## Stage 3 — Neighbourhood

Move outside the house, following the route from [`../vision/GAME_BIBLE.md`](../vision/GAME_BIBLE.md): **The Park** (sprinkler/water puzzle region) → **The Goose's tram** (connects Park to Industrial Zone) → **The Industrial Zone** (Rocky's recruitment and berserker behaviour system). Introduce the Zoom Meter as a real mechanic, not a placeholder.

**Exit criteria:** three playable party members (Mango, Cooper, Rocky) with distinct combat identities; the Park's environmental puzzle fully playable; the tram sequence (with the Goose) connects the two regions; Rocky's probabilistic action system implemented and balanced enough to feel characterful rather than random.

## Stage 4 — Open World

Continue the route: **The Helipad/Airport** (tower-climb dungeon → hot-air-balloon boss, unlocks the airship) → **The Eastern Cavoodle Forest** (King Jeff's Kingdom, Milo recruited) → **return to meet Charlie**, who instils the courage needed for the final stretch → **The Road Home** (the loop back, changed) → **homecoming boss rush** → **The Centre of Absence** final confrontation and ending.

**Exit criteria:** the full story spine from [`../vision/GAME_BIBLE.md`](../vision/GAME_BIBLE.md) is playable start to finish, with Charlie's arc and farewell implemented with the intended sincerity, and the ending (the humans' return, the baby, the broken vacuum) in place.

## Beyond Stage 4

Platform packaging for Steam (see below), further polish passes, and only then evaluation of mobile/Switch ports. Optional Supabase content-authoring layer (see [`../design/CONTENT_SCHEMA.md`](../design/CONTENT_SCHEMA.md)) can be adopted once the schema has survived real production use — not before.

## Platform

**Target #1: PC via Steam.** Godot 4 exports to Steam most directly; design input and UI for keyboard + controller from Stage 1 onward. Mobile and Nintendo Switch are explicitly deferred — Switch requires a Nintendo developer account/license that isn't worth pursuing before the game is proven. Revisit platform breadth after Stage 4.

## Working Rule

Do not open the next stage's scope (new regions, new systems, new party members) until the current stage's exit criteria are actually true in the running game — not "mostly done," not "designed," actually playable.
