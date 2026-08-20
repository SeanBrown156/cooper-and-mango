# Art Bible

> Canonical visual source of truth for Cooper & Mango.

This document defines what the game should look like. It does not define the
provider APIs, repository mechanics or the production sequence; those belong in
the [Art Production Pipeline](ART_PRODUCTION_PIPELINE.md) and
[`docs/engineering/MCP.md`](../engineering/MCP.md).

## 1. North Star

Cooper & Mango is a bright, poppy, late-SNES-inspired 2D RPG with warm
domestic fantasy, chunky readable silhouettes, expressive animals and
deliberately limited pixel detail.

Useful shorthand for prompts and reviews:

> Bright warm domestic fantasy, late-SNES JRPG proportions, chunky pixel
> clusters, expressive animal silhouettes, joyful colour, crisp hard edges.

Use references such as Final Fantasy VI to discuss visual grammar, not to copy
assets or named visual identities. UI follows the same principle: chunky
GBA/SNES-inspired frames, blocky text and high-contrast readability built with
modern Godot tooling.

## 2. Locked technical contract

| Asset | Native size | Contract |
|---|---:|---|
| Logical presentation | **480×270** | Current Godot logical canvas; integer presentation scaling |
| Environment tile | **16×16** | World-building and TileMap grid |
| Overworld hero | **20×16** | Quadruped, four cardinal directions, symbolic silhouette |
| Battle player character | **32×32** | Upright/bipedal theatrical combat presentation |
| Small battle enemy | **32×32** | Only for deliberately small enemies |
| Regular battle enemy | **48×48** | Standard enemy target |
| Large enemy / mini-boss | **64×64** | May carry more visual mass within battle layout |
| Major boss | **64×64 to ~128×96** | Set-piece exception where required |
| Dialogue portrait | **40×40** | Expressive upright/bipedal likeness |
| Major story portrait | **64×64** | Reserved for major close-up story beats |
| Common prop | **16×16 / 16×32 / 32×32** | Align to the environment grid where sensible |

Presentation size is not asset size. The 480×270 camera can reveal a partial
16×16 row at an edge; that is normal framing, not a reason to change the tile
grid. Characters are redrawn for their roles; do not algorithmically scale one
large drawing into overworld, battle and portrait assets.

## 3. Role grammar

### Overworld

- 20×16, quadruped/on all fours.
- Four directions: north, south, east and west.
- Silhouette, feet contact, tail and signature accessory matter more than face detail.
- The character must read at native 1× scale.

### Battle

- 32×32, upright/bipedal unless a specific action requires otherwise.
- Use strong theatrical poses and readable anticipation/impact/recovery.
- Signature props and attacks must remain legible without overwhelming the body.
- Battle art is a redraw, not an enlarged overworld sprite.

### Portrait

- 40×40, upright/bipedal likeness and expression layer.
- Prioritize face, markings, ears, muzzle/fluff, costume and emotional clarity.
- Portraits are separate drawings, not enlarged battle sprites.

### Character briefs

Character-specific identity and user-guided visual direction live in:

- `assets/characters/mango/CHARACTER_VISUAL_BRIEF.md`
- `assets/characters/cooper/CHARACTER_VISUAL_BRIEF.md`
- `assets/characters/rocky/CHARACTER_VISUAL_BRIEF.md`

Use `$cm-character-visual-brief` to create or update those files. Narrative
canon remains in `docs/vision/GAME_BIBLE.md`; briefs translate it into
art-facing constraints and record current direction/open questions.

## 4. Environment and world grammar

- Use a high top-down orthographic or near-orthographic view.
- Floor-facing surfaces dominate; furniture must read in plan view.
- Narrow depth edges are allowed only for readability.
- Wall-mounted/tall fixtures may use a front-elevation layer where necessary.
- The world grid is 16×16, but large scenery may occupy multiple cells.
- The world is real domestic space perceived as enormous mythical geography by animals.
- Preserve the identity of recognisable sofas, beds, bowls, cat trees, doors and appliances.

## 5. Pixel discipline

- No antialiasing, blur, soft halos or fractional scaling.
- Use hard edges and coherent pixel clusters.
- Avoid isolated generated noise and unnecessary dithering.
- Use nearest-neighbour filtering and integer presentation scale.
- Prioritize silhouette before texture or facial detail.
- At native scale, characters must separate clearly from props and scenery.

## 6. Outline and contrast grammar

Foreground readability is a gameplay rule.

- Characters and interactables use black or near-black readable outlines.
- Non-interactable background scenery uses faded, lower-contrast outlines that
  recede into the local palette.
- Do not give background objects the same outline contrast as a player,
  enemy, pickup, door or usable prop.
- Outline colour may use the palette's warm near-black rather than literal
  `#000000`, but it must read visually as black at native scale.
- Characters and important interactive objects should generally be warmer,
  brighter and/or more contrast-rich than the scenery immediately behind them.

## 7. Consolidated palette

The project master palette contains 64 colours in
`assets/palette/cooper_mango_master_palette.gpl`. Individual assets use small
subsets, usually 8–12 colours for a major character and fewer for simple props.

| Family | Highlight | Midtone | Shadow | Deep shadow / accent | Notes |
|---|---|---|---|---|---|
| Mango orange | `#FFCF7A` | `#F0913E` | `#C85A2E` | `#7A3524` | Warm fur ramp |
| Purple hoodie | `#E8C9E8` | `#7C4FD6` | `#4A2D73` | `#241B4A` | Mango costume |
| Neutral | `#FFFFFF` | `#F3ECD1` | `#E28FA0` | `#181425` | Cream, pink accent, outline near-black |
| Cooper black-grey | `#8A857A` | `#55504A` | `#2E2A26` | `#171412` | Warm, never cold-grey |
| Cooper cream | `#FBF6EC` | `#E0D6C4` | `#BFB29A` | `#8A7C63` | Muzzle, chest and paws |
| Cooper green | `#9FCDB0` | `#4E9873` | `#2E5F49` | `#1A3A2C` | Collar/accessory green |
| Rocky chestnut | `#F0C9A0` | `#C17F4A` | `#8C4A2E` | — | Shares kinship with Mango orange |
| Rocky white | `#FBF3E8` | `#E2CCB9` | `#C9AF98` | `#A0937E` | White coat ramp |
| Threat/boss | `#584A3A` | `#3E2731` | — | `#0F0015` | Dark high-contrast threat pole |
| Threat accent | `#C9A227` | — | `#8C1F28` | — | Dread gold and blood red |
| Water / Park | `#8FD9D6` | `#2F8A8F` | `#1C5559` | `#193C3E` | Teal water ramp |
| Autumn / Cavoodle Forest | `#FFE1A3` | `#E08A3C` | `#A85A28` | `#5C3018` | Warm regional identity |
| Rust / Industrial | `#E8B796` | `#B86F50` | `#733E39` | `#3E2731` | Industrial rust |
| Metal / Industrial | `#C0CBDC` | `#8A8A82` | `#55554E` | `#2E2E28` | Industrial metal |
| Wood / earth | `#C28569` | `#8A5F3A` | `#733E39` | `#181425` | General domestic material |
| Forest green | `#C6E88F` | `#63C74D` | `#3E8948` | `#265C42` | Verdant foliage |
| Bright water / sky | `#2CE8F5` | `#0099DB` | `#124E89` | `#262B44` | Saturated blue accent |
| UI danger | — | `#E43B44` | — | — | Critical HP/danger state |
| Reward gold | — | `#FEE761` | — | — | Loot/currency/level-up |
| Empty House dust | — | `#C9BFE0` | — | — | Domestic magic accent |

Use hue-shifted shadows rather than moving a colour directly toward black.
The master palette supports two poles: bright warm Hero/World and dark
high-contrast Threat/Boss. Both remain part of the same world palette.

## 8. Animation standards

Animation should be economical and identity-preserving.

- Overworld: 2-frame idle, 4-frame walk per direction, plus only the states
  needed by gameplay.
- Battle: 2–3 idle, 4–6 attack/cast, 2 hurt, 2 defend, 3–5 victory and 1–2 KO
  are useful defaults, not mandatory quotas.
- Preserve head/feet relationship, baseline, pivot, markings, accessories and
  body grammar across frames.
- A smooth animation that changes the character's design is a failed animation.

## 9. Visual acceptance checklist

Before approval, confirm:

- correct role dimensions and posture;
- native 1× silhouette readability;
- character/background contrast and outline class;
- limited palette with no accidental colours;
- no antialiasing, halos or generated pixel noise;
- stable markings, eyes, limbs, accessories and proportions;
- correct perspective and feet/pivot alignment;
- frame-to-frame identity consistency;
- successful Godot composition and runtime test.

## 10. Related authority

- Character identity: `assets/characters/<character>/CHARACTER_VISUAL_BRIEF.md`.
- Narrative canon: [`docs/vision/GAME_BIBLE.md`](../vision/GAME_BIBLE.md).
- Production sequence and skill handoffs: [`ART_PRODUCTION_PIPELINE.md`](ART_PRODUCTION_PIPELINE.md).
- MCP/tool capabilities: [`docs/engineering/MCP.md`](../engineering/MCP.md).
