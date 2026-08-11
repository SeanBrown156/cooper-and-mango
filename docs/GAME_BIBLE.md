# Game Bible — Mango and Cooper

## Premise

A small 2D *Final Fantasy*-style role-playing game starring our real pets, Mango (cat) and Cooper (dog). Their humans vanish suddenly one night; the animals gain speech and magical powers, household technology awakens as monsters, and the pair sets out to find out what happened. The truth — a baby was born — is withheld from the player until the ending. The emotional question driving the whole game:

> Have our humans left us forever — and if they have, can we still find the courage to continue?

## Player Fantasy

You are a small animal in a suddenly vast, transformed version of your own home and city, discovering that you are braver and more capable than you knew — without stopping being who you already are.

## Emotional Idea

The family did not disappear. It changed and became larger. Love, grief, and courage are not solved by certainty; they are practiced.

## Core Loop

Explore a region as a two-character party (switching overworld leader for complementary field abilities) → encounter transformed domestic/environmental enemies → recruit animal allies with distinct combat identities → confront a personal-fear boss → return home through a looping world structure where earlier places have changed.

## Main Characters

- **Mango** — aloof, magically powerful ex-street cat. Arc: survival → love. Learns that opening up emotionally is not weakness.
- **Cooper** — earnest, anxious dog. Arc: anxiety → courage. Learns that courage means acting while still afraid.
- **Rocky** — berserker dog ally (a friend's dog). Immense, uncontrollable power; teaches that bravery isn't the same as recklessness.
- **Milo** — Cooper's best friend/lover; temporary guest companion for the Eastern Cavoodle Kingdom chapter.
- **Charlie** — Yuichi's elderly cat; the old sage who joins the final journey and passes away during it. His death is a sincere, central emotional beat, not a shock twist.
- **Yuichi** — Charlie's human; present only through memory/environmental storytelling, not as a playable character.
- **King Jeff, the Chad Cavoodle** — ruler of the satirical Eastern Cavoodle Kingdom; comic but can carry real themes of status and belonging.
- **Sean and Lillian** — the missing/returning humans; affectionate, unreliable quest-givers whose absence drives the plot and whose return resolves it.

## World Rules

- The moment the humans vanish, animals gain speech and awaken personal magical powers.
- Household technology and objects awaken as monsters (vacuum cleaners, phones, hot-air balloons, sprinklers, etc.).
- The world is real Melbourne homes/parks/suburbs/industrial areas, reinterpreted through animal perception as elemental fantasy regions.
- Dogs and cats perceive colour differently (blue/yellow-weighted); this can inform palettes, puzzles, and dialogue without becoming a literal simulation.
- The overworld forms a large loop: the journey out and the journey home cross the same places, which have visibly changed.

## Elemental Regions

| Region | Element / theme | Major feature |
|---|---|---|
| The Empty House | dust / domestic magic | Mi-chan and awakened appliances |
| The Drowned Park | water | sprinkler puzzle and aquatic enemies |
| The Iron Estate | metal / machinery | Rocky and industrial monsters |
| The Eastern Cavoodle Kingdom | sun / orange / community | orange cavoodle NPC civilisation, King Jeff |
| The Tower of Wind | air | Cooper's hot-air-balloon trial |
| The High Overworld | sky | balloon-airship navigation |
| The Road Home | remixed elements | return journey and boss rush |
| The Centre of Absence | void / memory | chimeric final boss |

## Story Spine

1. **The Empty House** — Mango and Cooper wake to an empty apartment; explore; fight domestic enemies (Dust Bunnies, Crumb Slimes, the Mop Serpent, etc.); first boss **Mi-chan** (the robot vacuum), defeated but not destroyed — it retreats and returns stronger later.
2. **Beyond the house** — party expands with allies (Rocky in the Iron Estate, Milo in the Cavoodle Kingdom); world grows from house → neighbourhood → wider regions.
3. **The Hot-Air Balloon** — major personal boss built around Cooper's specific fear; victory turns the balloon into the game's airship, unlocking free exploration and backtracking.
4. **The Road Home** — the loop bends back; earlier areas are revisited, changed, and made passable by new abilities/allies.
5. **Homecoming boss rush** — evolved rematches of earlier fears and bosses, ending in Mecha Mi-chan's final form.
6. **The Absence** — final boss, a chimera assembled from the journey's fears (Mi-chan parts, TV faces, balloons, storms, cages, empty bowls, distorted human silhouettes). Not defeated by denying the fear was real — defeated by acknowledging love, memory, and the allies gathered along the way.
7. **The humans return** — magic fades, speech disappears, and the owners come home carrying a newborn baby: the real reason for their absence. Mango and Cooper become guardians/older siblings rather than being replaced. The destroyed vacuum cleaner (Mi-chan) is the game's ambiguous final wink — did any of it really happen?

## Charlie's Arc

Charlie is based on a real, elderly cat nearing the end of his life. In the game he is the old sage who joins the final journey, sees through Mango's guarded exterior, recognises Cooper's courage before Cooper does, and passes away during the story — a quiet, loving farewell rather than a shock beat. His memory stays mechanically present afterward (a learned ability, protective light, remembered line, or musical motif). This is the emotional key that lets Mango and Cooper understand: courage does not prevent loss, it lets you love fully anyway.

## Key Systems (see CONTENT_SCHEMA.md for data shape)

- **Field ability leader-switching** — Mango climbs/squeezes/senses hidden things; Cooper swims/pulls/tracks scent/digs. Exploration is lightly ability-gated.
- **Zoom Meter** — shared limit-break system built on real pet zoomies. Meter fills on damage/excitement; at max, the character automatically unleashes a signature move the player doesn't choose. Rocky is permanently maxed.
- **Animal-needs items** — kibble, treats, water, toys as HP/MP-equivalent restoratives, with species affinities and the running joke that cat kibble is surprisingly effective on dogs.
- **Toileting mechanics** — scent-marking as save points/fast travel, territory claiming, and similar reinterpretations rather than literal bodily-needs meters.

## Scope Boundary (for now)

This is a full-scope game, staged deliberately — see `PRODUCTION_ROADMAP.md` for how the above story spine gets built incrementally starting from one room. This document is the destination, not a build order.
