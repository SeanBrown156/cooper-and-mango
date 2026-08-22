# Combat Stat Model

Reference design for issue #15. This document defines the shared combat
vocabulary for actors, enemies, abilities and items. It is a design reference,
not a data record and not a replacement for the content-record shape in
[`CONTENT_SCHEMA.md`](CONTENT_SCHEMA.md).

## Design goals

- Keep the visible model small enough to read at a glance in a fast,
  personality-first RPG.
- Give Mango, Cooper and recruited allies distinct combat identities without
  requiring a large spreadsheet of hidden attributes.
- Let abilities and items create temporary decisions rather than permanently
  rewriting an actor's identity.
- Make encounter tuning predictable: a region's threat should be expressible
  in a few numbers and checked against the party's expected level.

## Stat vocabulary

Every combatant has the following permanent base stats. Actors and enemies use
the same vocabulary; an enemy simply has no progression outside the encounter
where it appears.

| Stat | Meaning | Primary uses |
|---|---|---|
| `max_hp` | Maximum vitality | Damage survival and healing cap |
| `power` | Physical and magical force | Damage and restorative effect strength |
| `guard` | Ability to withstand force | Reduces incoming damage |
| `speed` | Battle tempo | Turn order and escape priority |
| `focus` | Control, precision and composure | Accuracy, status resistance and status application |
| `zoom_max` | Capacity of the shared zoom meter | Signature-move threshold |

`hp` and current `zoom` are runtime state, not base stats. `level` is a
progression input and is not itself a combat stat. Species, elemental affinity,
resistances, weaknesses and traversal abilities are tags or capabilities, not
additional numeric stats.

### Derived combat values

Use integer values in content records and round down after each formula unless
the formula says otherwise.

```text
effective_stat = max(0, base_stat + flat_modifiers) × (1 + sum(percent_modifiers))
damage = max(1, floor(ability_power × effective_power / max(1, target_effective_guard)))
healing = max(1, floor(ability_power × effective_power / 10))
```

`ability_power` is the move's own coefficient or fixed value. A move that does
not deal damage or heal does not need an `ability_power` value. Percent
modifiers are additive with one another and applied once; they do not compound
in application order.

Damage types, if introduced, should be expressed as ability/item tags and
resistance multipliers rather than new actor stats. A neutral hit has a `1.0`
multiplier; a weakness uses `1.5`; a resistance uses `0.5`; immunity uses `0`.
Apply the affinity multiplier after the base damage formula and round down,
with a minimum of `1` only for non-immune damage.

## Actor and enemy profiles

The stat line is the combat identity. A profile should normally have one clear
strength, one usable secondary strength and one exploitable weakness.

| Profile | High stat | Low stat | Intended job |
|---|---|---|---|
| Mango | `power`, `focus` | `guard` | Precise damage and reliable status play |
| Cooper | `guard`, `max_hp` | `speed` | Durable protector and steady support |
| Rocky | `power`, `max_hp` | `focus` | Volatile burst damage; control is unreliable |
| Milo | `speed`, `focus` | `max_hp` | Fast utility and setup |
| Charlie | `focus`, support scaling | `power` | Protection, recovery and memory effects |
| Common enemy | One encounter-relevant stat | One readable weakness | Simple regional obstacle |
| Boss | Two complementary stats | A discoverable counterplay | A multi-phase story challenge |

These are role targets, not extra rules or fixed numbers. Individual records
choose the actual values and abilities. Do not add a new stat to solve a single
enemy or move; prefer a modifier, tag, status or ability effect.

## Level and progression scaling

### Actors

Actor records provide level-1 base stats. At level `L`, progression uses a
single growth rate per stat:

```text
level_stat = floor(base_stat × (1 + growth_rate × (L - 1)))
```

Use these default growth bands unless a character's design explicitly calls for
an exception:

| Growth band | Per-level rate | Suitable stats |
|---|---:|---|
| Low | 0.05 | A deliberate weakness or secondary stat |
| Standard | 0.08 | Most stats |
| High | 0.11 | Signature strengths |
| Exceptional | 0.14 | A rare identity-defining strength |

`zoom_max` does not grow automatically. It increases only through deliberate
story or progression rewards, normally by `+1` at a time, so the automatic
signature-move rhythm stays legible. Rocky's permanently full meter is an
explicit character rule, not a different zoom stat.

### Enemies

Enemy records define a level-1 template plus a threat tier. When an enemy is
placed at level `L`, use the same linear formula, but with threat-tier growth
bands:

| Threat tier | HP / Guard | Power / Speed / Focus | Use |
|---|---:|---:|---|
| Minor | 0.10 | 0.08 | Common regional enemy |
| Standard | 0.12 | 0.10 | Durable or specialised enemy |
| Elite | 0.15 | 0.12 | Optional challenge or miniboss |
| Boss | Encounter-authored | Encounter-authored | Phase and story tuning |

Enemy level comes from the encounter, not from the enemy's identity. The
encounter should normally set enemy level to the party's expected level for the
region. A deliberate surprise may use `party_level + 1`, but a whole encounter
should not exceed `party_level + 2` without a visible warning or optional
challenge framing.

For a boss, use the same stat vocabulary and show its counterplay through
behaviour, animation or narrative clues. Boss phases may change effective stats
or grant effects, but should not silently replace the boss's base record.

### Tuning guardrails

These are playtest targets, not guarantees:

- A standard enemy should survive roughly 2–4 basic actor turns when attacked
  by its intended counter.
- A standard enemy should threaten roughly 3–5 unmitigated hits before defeating
  an actor at full health.
- A restorative item should repair a meaningful portion of an actor's health,
  but not make damage irrelevant; start at 25–35% of `max_hp` for a common
  single-target restore.
- A temporary stat buff should be felt for its duration without becoming the
  only correct action; start at `+2` flat or `+15%`, then playtest.

If a fight misses these targets, adjust the encounter level, enemy template or
ability coefficient before introducing a new stat.

## Modifiers and precedence

Abilities and items modify a combatant through explicit effects. They never
mutate the permanent base stat in the record.

Supported modifier forms:

| Form | Example | Duration |
|---|---|---|
| Flat stat | `power +2` | Instant or timed |
| Percent stat | `guard +15%` | Timed or encounter |
| Current resource | `hp +18`, `zoom +2` | Instant |
| Cap change | `max_hp +10%` | Timed or encounter |
| Rule effect | Protect an ally, cleanse, taunt, delay | Effect-defined |

Resolve effects in this order:

1. Start from level-scaled base stats.
2. Add active flat modifiers.
3. Apply the sum of active percent modifiers.
4. Apply ability power, target affinity and other move-specific rules.
5. Clamp resources and stats to their legal bounds.

Positive and negative modifiers use the same arithmetic. A stat cannot fall
below `0`; `max_hp` cannot fall below `1`; current `hp` is clamped to the new
maximum. No single temporary effect may reduce a stat below `25%` of its
level-scaled base value unless the effect is a specifically authored boss or
status rule.

When multiple effects modify the same stat, each effect remains separately
named and timed for display and removal. Flat modifiers add together. Percent
modifiers add together. Identical named effects refresh their duration rather
than stacking unless the ability explicitly says `stackable` and supplies a
maximum stack count.

## Ability modifiers

An ability record should state its user, target, cost, power/effect, and any
modifier duration. The content schema's `effects` array is the canonical place
for these changes.

Recommended effect vocabulary:

```text
damage            target, ability_power, affinity/tag
heal              target, ability_power or fixed_amount
modify_stat       target, stat, amount, mode(flat|percent), turns
modify_resource   target, resource(hp|zoom), amount
apply_status      target, status_id, turns, chance
cleanse_status    target, status_id or category
protect           target, damage_share, turns
taunt             target, turns
```

Examples of intended design language:

- Mango's `skill_judgemental_stare` can apply `focus -2` to one enemy for
  several turns, matching the existing schema example without adding a new
  stat.
- Cooper's protection ability should use `protect` or a timed `guard` modifier,
  so the defensive identity is visible in the effect and removable at combat
  end.
- Rocky's burst ability can use high `ability_power` plus a temporary negative
  `focus` modifier, making recklessness a trade-off rather than a hidden
  accuracy formula.
- A Zoom Meter signature move may consume or reset `zoom`; its power should be
  authored on the ability and not inferred from a permanent stat increase.

Traversal abilities remain exploration capabilities. They may have combat
versions, but a combat version must be an explicit ability record rather than
implicitly granting a stat bonus.

## Item modifiers

Items are consumable or equipable content records and use the same effect
vocabulary as abilities. Species affinity controls who may use an item; it does
not change the stat model.

| Item role | Default effect shape | Guardrail |
|---|---|---|
| Food / kibble | `heal` fixed amount or percentage of `max_hp` | Single target; no free stat buff |
| Treat | Small `heal` plus a short morale/stat effect | Keep the buff weaker than a dedicated ability |
| Water | Restore a small amount of `zoom` or cleanse a heat/status effect | Do not also fully heal by default |
| Toy | Restore `zoom`, or grant a short speed/focus effect | Stronger in setup than in raw damage |
| Equipment / signature item | Persistent flat or percent modifier | One clear identity; removable and inspectable |
| Key item | No combat effect unless explicitly authored | Preserve narrative purpose |

Item effects should be concrete and inspectable: “restores 20 HP” or “guard
`+15%` for 2 turns,” not “makes Cooper tougher.” Equipment applies before the
combat round begins and is removed or replaced through the equipment system;
consumables resolve immediately and do not permanently alter base stats.

## Encounter balancing handoff

An encounter should specify the expected party level, enemy IDs and levels,
formation/targeting rules, and any authored modifiers. Balance in this order:

1. Pick the region's expected party level and enemy threat tier.
2. Pick enemy roles and weaknesses that teach the encounter's intended answer.
3. Check time-to-defeat and threat against the tuning guardrails above.
4. Add or adjust abilities/items only when the encounter needs a new decision,
   not to compensate for an uncalibrated stat line.

The resulting records should retain stable IDs, `content_status`, and explicit
relationships described by `CONTENT_SCHEMA.md`. This document does not create
or approve any actor, enemy, ability, item or encounter record.

## Open tuning decisions

The following can remain data-level choices during the first vertical slice:

- exact level cap and level-up cadence;
- whether damage affinity is elemental, thematic, or both;
- the final status catalogue and resistance rules;
- whether equipment slots are available before Stage 2.

Those decisions must use the vocabulary and precedence rules above if they are
introduced; they should not create parallel stat systems.
