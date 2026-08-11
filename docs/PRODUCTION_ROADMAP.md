# Production Roadmap

This translates the full vision in `GAME_BIBLE.md` into deliberate build stages. The "toy → vertical slice → game" practice (see `AI-Assisted Game Development` source note) is the *method* used at every stage — it is not a cap on the final scope. Each stage below has to be proven working before the next stage's scope is opened up, so growth is intentional rather than accidental.

## Stage 0 — Toy (pre-slice)

Prove the smallest possible thing: a character that can move and interact with one object, using placeholder art and the real data schema.

**Exit criteria:** Mango moves on a greybox map and can inspect one object. No battle, no Cooper, no polish.

## Stage 1 — Room (the Vertical Slice)

See `VERTICAL_SLICE.md` for full detail. One room (the apartment living room), Mango and Cooper both playable, one battle, one ending beat.

**Exit criteria:**
1. Mango walks across the apartment
2. Mango inspects the empty food bowl
3. Mango and Cooper exchange dialogue
4. Mango and Cooper fight and beat the Vacuum Cleaner using complementary abilities
5. One closing emotional beat plays

This is the proof that "moving Mango already feels recognisably like Mango" — the decisive early milestone, not merely a generic cat moving.

## Stage 2 — House

Expand from one room to the full **Empty House** chapter: the rest of the apartment, the full set of domestic enemies (Dust Bunnies, Crumb Slimes, Static Sprites, Vinegar Wisps, the Mop Serpent, Hairdryer Wyvern, Washing Machine Mimic, the Doorbell), and the complete first Mi-chan boss encounter (not just a placeholder fight).

**Exit criteria:** the apartment's sealed exit opens; Mi-chan retreats rather than being destroyed, setting up its return; leader-switching field abilities (climb/squeeze/sense for Mango, swim/pull/track/dig for Cooper) are implemented and used to solve at least one traversal puzzle.

## Stage 3 — Neighbourhood

Move outside the house. Build **The Drowned Park** (sprinkler mini-game) and **The Iron Estate** (Rocky's recruitment and berserker behaviour system). Introduce the Zoom Meter as a real mechanic, not a placeholder.

**Exit criteria:** three playable party members (Mango, Cooper, Rocky) with distinct combat identities; one environmental puzzle region (Drowned Park) fully playable; Rocky's probabilistic action system implemented and balanced enough to feel characterful rather than random.

## Stage 4 — Open World

Build out the remaining regions: **The Eastern Cavoodle Kingdom** (Milo, King Jeff), **The Tower of Wind / hot-air-balloon boss** (unlocks the airship and free world navigation), **The Road Home** (the loop back, changed), the **homecoming boss rush**, and the **Centre of Absence** final confrontation and ending.

**Exit criteria:** the full story spine from `GAME_BIBLE.md` is playable start to finish, with Charlie's arc and farewell implemented with the intended sincerity, and the ending (the humans' return, the baby, the broken vacuum) in place.

## Beyond Stage 4

Platform packaging for Steam (see below), further polish passes, and only then evaluation of mobile/Switch ports. Optional Supabase content-authoring layer (see `CONTENT_SCHEMA.md` and the source note's "Revised Technical Direction" section) can be adopted once the schema has survived real production use — not before.

## Platform

**Target #1: PC via Steam.** Godot 4 exports to Steam most directly; design input and UI for keyboard + controller from Stage 1 onward. Mobile and Nintendo Switch are explicitly deferred — Switch requires a Nintendo developer account/license that isn't worth pursuing before the game is proven. Revisit platform breadth after Stage 4.

## Working Rule

Do not open the next stage's scope (new regions, new systems, new party members) until the current stage's exit criteria are actually true in the running game — not "mostly done," not "designed," actually playable.
