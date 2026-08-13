# Art Bible

> **Canonical visual source of truth for Cooper & Mango.**
>
> **Decision update — 2026-08-12 (revised):** this document supersedes the 2026-08-11 experiment (48×48 overworld characters, 32×32 environment tiles) and the initial 2026-08-12 pass (24×24 overworld, 40×40 portraits). The final locked visual formula is: **16×16 world grid, 24×16 quadruped overworld heroes, 32×32 theatrical battle heroes, 48×48 expressive portraits (with a 64×64 tier reserved for major story-beat close-ups), four-direction movement, a limited shared palette, and chunky GBA/SNES-inspired UI — modern tooling underneath, old-school discipline on top.**

## 1. North Star

**Cooper & Mango is a bright, poppy, late-SNES-inspired 2D RPG with warm domestic fantasy, chunky readable silhouettes, expressive animals, and deliberately limited pixel detail.**

The goal is **not** to reproduce SNES hardware limitations literally or copy any existing game's assets. The goal is to use the visual grammar of games such as Final Fantasy VI — tiny symbolic overworld characters, theatrical battle staging, richer portraits and monsters, economical animation, hard pixel edges, strong silhouettes — while building the game with modern tooling in Godot.

A useful shorthand for prompts and reviews:

> **“Bright warm domestic fantasy, late-SNES JRPG proportions, chunky pixel clusters, expressive animal silhouettes, joyful colour, crisp hard edges.”**

Avoid using only “Final Fantasy style” as a prompt. It is too broad and encourages inconsistent or derivative output.

UI direction follows the same principle: **chunky GBA/SNES-inspired UI** — thick borders, blocky text-box frames, high-contrast readable menus — built with modern Godot tooling underneath, not literal hardware constraints. Modern tooling underneath, old-school discipline on top.

---

## 2. Locked Technical Art Specification

### Core dimensions

| Asset | Locked frame / grid | Typical subject occupancy | Notes |
|---|---:|---:|---|
| Logical game presentation | **320×180** | — | Modern 16:9 canvas with deliberately low-resolution composition |
| Environment tile | **16×16** | — | Canonical world-building grid |
| Overworld hero (quadruped) | **24×16** | ~20–22 px wide, ~12–14 px tall | Tiny symbolic representation; silhouette first; on-all-fours proportions |
| Battle player character | **32×32** | ~24–30 px tall | Redrawn for combat; not an enlarged overworld sprite |
| Small battle enemy | **32×32** | variable | Only where deliberately tiny |
| Regular battle enemy | **48×48** | variable | Standard enemy target |
| Large enemy / mini-boss | **64×64** | variable | May overflow visual mass within battle layout |
| Major boss | **64×64 to ~128×96** | variable | Set-piece art may break regular sprite scale |
| Dialogue portrait | **48×48** | ~42–46 px | Separate drawing; primary likeness/expression layer; bipedal pose |
| Major story-beat portrait | **64×64** | ~56–62 px | Reserved for major story beats (e.g. Charlie's farewell, the final confrontation) where the face carries the scene, not required by default |
| Common prop | **16×16 / 16×32 / 32×32** | variable | Align to the environment grid wherever sensible |

### Historical reference, not a production constraint

The classic SNES presentation was commonly built around a roughly **256×224** visible canvas and an 8×8 hardware tile vocabulary. Final Fantasy VI used extremely small playable character art — roughly the visual territory of a ~16×24 character — and reused compact character sprites very economically.

We are deliberately giving Mango and Cooper a little more room because animal silhouettes need ears, tails, fluff, posture and signature props to remain readable. **24×16 is our SNES-plus compromise.**

### Important hierarchy rule

The same character is **redrawn at different levels of abstraction — and different body postures:**

- **24×16 overworld:** icon of the character, on all fours (quadruped)
- **32×32 battle:** pose and action readability, upright/bipedal
- **48×48 portrait:** likeness, fluff, face, emotion, costume detail, upright/bipedal

Do **not** create one large drawing and algorithmically scale it down into all three roles. They are separate drawings of the same design.

---

## 3. Mango at Each Scale

### Overworld Mango — 24×16 (quadruped)

This is an icon of Mango, not a miniature illustration. Mango moves on all fours here — a real cat's proportions, not the upright hoodie-mage pose used for battle/portrait.

Must survive reduction:

- orange-cat silhouette, on all fours
- oversized readable ears
- purple hoodie draped over the back like a cape, not worn like a person
- fluffy cheek or chest suggestion
- tail silhouette
- black cat-teaser wand / fishing-rod-like toy silhouette where the pose allows
- judgemental / blasé attitude communicated mainly through posture

Facial detail may be only a handful of pixels. Eyes may literally be one pixel each. If the silhouette does not read at native 1× scale, adding more detail is the wrong fix.

### Battle Mango — 32×32 (bipedal)

Redraw rather than enlarge. Upright/bipedal — the mage pose, not the overworld's on-all-fours stance.

Direction:

- upright / bipedal
- chubby and fluffy
- 3/4 combat stance
- one paw clearly gripping the wand
- stronger tail gesture
- enough face to sell confidence / mild arrogance / warmth
- robe/hoodie movement can animate by only one or two pixels

### Portrait Mango — 48×48 (bipedal)

This is the likeness layer. Upright/bipedal, same posture family as the battle sprite.

Use the extra resolution for:

- cheek and chest fluff
- judgemental eyes
- tiny smug or blasé mouth
- ear interior
- exact markings
- hood folds
- whisker suggestion
- wand handle / prop detail if composition permits

Portraits are **not** enlarged battle sprites.

The same scale hierarchy applies to Cooper and every major character.

---

## 4. Perspective and World Grammar

- Three-quarter top-down JRPG perspective
- Environment grid: **16×16**
- Characters visually align to the tile grid but are not required to fill a tile
- Production movement set: **4 cardinal directions**
- Diagonal character frames are optional future polish, not required for the core game
- Large scenery can be composed from multiple tiles; do not force every object into a single 16×16 square
- Doors, beds, sofas, cat trees, kitchen objects and other recognisable household forms should retain their real-world identity even after fantasy reinterpretation

The world should feel like **real domestic spaces becoming enormous mythical geography from the animals’ point of view**, not a generic medieval fantasy tileset.

---

## 5. Pixel Discipline

These are hard rules for production assets.

### Hard edges only

- no anti-aliasing
- no blurred edges
- no soft transparency halos
- no fake “pixel art” produced by shrinking a high-resolution painted image
- no fractional sprite scaling in-game

Every visible pixel should feel intentional.

### Pixel clusters over pixel noise

Prefer coherent blocks and shapes over scattered single-pixel texture.

Good pixel art reads as clusters first, details second. Generated art with isolated sparkle/noise pixels everywhere must be cleaned before approval.

### Silhouette before detail

At 1× native resolution, a player should be able to distinguish:

- Mango from Cooper
- party members from NPCs
- characters from background props
- major enemies from scenery

If readability depends on zooming in, the sprite is not done.

### Integer scale only

When shown larger, pixel art should scale by clean integer multiples wherever possible:

- 1×
- 2×
- 3×
- 4×
- 6×
- 8×

Avoid arbitrary 1.25× / 1.5× / 2.3× transforms on production sprites.

---

## 6. Colour Direction

### Mood

**Bright and poppy, but controlled.**

Not washed-out “retro brown.” Not maximum-saturation mobile-game candy. The target is joyful, warm colour with deliberate contrast and rich hue-shifted shadows.

### Palette hierarchy

Use a shared **master palette of roughly 48–64 colours** for the whole game.

Individual assets should use much smaller subsets:

- major character: usually **8–12 colours including outline/shadow ramps**
- minor NPC: often 6–10
- simple prop: often 4–8
- environment tile: only as many as the tile needs

The master palette creates world coherence; the per-asset limitation creates readable pixel art.

### The two-pole system

The world runs on a deliberate dichotomy, not one uniform mood: a bright, warm **Hero/World pole** (Mother/EarthBound/OMORI-adjacent) for everyday exploration and party members, and a dark, high-contrast **Threat/Boss pole** (Blasphemous-adjacent) reserved for awakened-object monsters, bosses, and fear beats. Every region leans somewhere on this axis rather than picking one absolutely — see `GAME_BIBLE.md`'s "A Single Day" for how that lean tracks the story's literal dawn-to-night timeline. Both poles are built from one shared master palette so the game still reads as one coherent world, not two different art styles.

### Master palette — hex reference

Every ramp below draws from the same ~20-colour core; individual assets still pull only the 8-12 colours they actually need per the palette hierarchy above.

| Ramp | Highlight | Midtone | Shadow | Deep shadow |
|---|---|---|---|---|
| Mango orange (fur) | `#FFCF7A` | `#F0913E` | `#C85A2E` | `#7A3524` |
| Purple hoodie | `#E8C9E8` | `#7C4FD6` | `#4A2D73` | `#241B4A` |
| Neutral/accent | `#FFFFFF` cream-white | `#F3ECD1` pale fur | `#E28FA0` pink accent | `#181425` outline (warm near-black, never pure black) |
| Cooper black/grey (coat) | `#8A857A` | `#55504A` | `#2E2A26` | `#171412` |
| Cooper cream (muzzle/paws/chest) | `#FBF6EC` | `#E0D6C4` | `#BFB29A` | `#8A7C63` |
| Cooper green (collar) | `#9FCDB0` | `#4E9873` | `#2E5F49` | `#1A3A2C` |
| Rocky chestnut (fur, linked to Mango's orange) | `#F0C9A0` | `#C17F4A` | `#8C4A2E` | `#7A3524` (shared with Mango's deepest shadow — deliberate kinship) |
| Rocky white (body) | `#FBF3E8` | `#E2CCB9` | `#C9AF98` | `#A0937E` |
| Threat/Boss pole | `#584A3A` faded gold-brown | `#3E2731` desaturated mid | `#181425` near-black | `#0F0015` deepest void |
| Threat accent (sparing use only) | `#C9A227` dread gold | — | `#8C1F28` blood-red (higher-intensity alt) | — |
| Water / The Park | `#8FD9D6` | `#2F8A8F` | `#1C5559` | `#193C3E` |
| Autumn / Eastern Cavoodle Forest | `#FFE1A3` | `#E08A3C` | `#A85A28` | `#5C3018` |
| Rust / The Industrial Zone | `#E8B796` | `#B86F50` | `#733E39` | `#3E2731` |
| Metal / The Industrial Zone | `#C0CBDC` | `#8A8A82` | `#55554E` | `#2E2E28` |
| Wood / earth (general domestic) | `#C28569` | `#8A5F3A` | `#733E39` | `#181425` |
| Forest green (verdant foliage) | `#C6E88F` | `#63C74D` | `#3E8948` | `#265C42` |
| Bright water / sky (lush blue accent) | `#2CE8F5` | `#0099DB` | `#124E89` | `#262B44` |

**2026-08-13 addition:** two new environment ramps — Forest green and Bright water/sky — added to push the master palette toward ~60 colours, per direction to bring more verdant green and lusher, brighter blue into the world (the existing Water/The Park ramp is teal-leaning; this new ramp gives a genuinely saturated sky/water blue for contrast). Midtone/Shadow/Deep-shadow on both are exact Endesga-32 matches (`#63C74D`/`#3E8948`/`#265C42` and `#0099DB`/`#124E89`/`#262B44`), keeping them compatible with the CC0 tileset the same way the other utility ramps are; each Highlight is bespoke since Endesga-32 has no light-enough match in either hue family. Forest green is for general foliage/tree/bush environment art — distinct from the Autumn/Eastern Cavoodle Forest ramp, which stays orange-toned for that specific region's sun/community theme.

### Single accent colours (not full ramps)

Three gaps identified when pushing the master palette to the full 64-colour ceiling — each is a standalone accent rather than a 4-tier ramp, because each fills a specific missing role rather than needing its own highlight/shadow family:

| Accent | Hex | Purpose |
|---|---|---|
| UI danger / critical-HP red | `#E43B44` | Semantic UI red (low-HP flash, danger prompts). Distinct from Threat accent's blood-red, which is a *monster/boss* colour, not a UI state colour — using the same hex for both would blur "this enemy is scary" and "you are about to die." |
| Reward / treasure gold | `#FEE761` | Positive UI gold (loot, currency, level-up flashes). Distinct from Threat accent's dread-gold (`#C9A227`), which is deliberately desaturated/ominous — this one needs to read as unambiguously good news. |
| Dust / Empty House domestic magic | `#C9BFE0` | The Empty House was the one region in the Elemental Regions table with no colour identity of its own (everything else had a ramp: water, metal, autumn, industrial rust). A soft dust-lilac gives the game's first region — and Mecha Mi-chan's awakening — its own quiet magical-dust palette note, distinct from the plain Wood/earth domestic ramp. |

`#E43B44` and `#FEE761` are both exact Endesga-32 matches. `#C9BFE0` is bespoke — it's evoking a specific in-fiction "magic dust" feeling rather than a neutral utility colour, so it gets the same treatment as the character ramps (left unforced).

This brings the master palette to its full **64-colour ceiling.**

As of 2026-08-12, the neutral/utility ramps (Neutral/accent, Threat/Boss pole, Water/The Park, Rust/Industrial Zone, Metal/Industrial Zone, Wood/earth) have had every swatch with a genuinely close Endesga-32 match realigned to that exact Endesga-32 hex, for palette compatibility with the CC0 `rgsdev_cc0_topdown_template` tileset. Swatches with no close Endesga-32 counterpart (wrong hue family or too great a distance) were deliberately left bespoke rather than forced. Mango orange, Purple hoodie, Cooper black/grey, Cooper cream, Cooper green, Rocky chestnut, Rocky white, and Threat accent remain fully bespoke/photo-grounded and were not touched.

The Autumn/Cavoodle ramp deliberately echoes Mango's own orange ramp — a nice quiet resonance between the protagonist's colour story and the "sun/orange" region theme, not a coincidence to fix.

Cooper's and Rocky's ramps above are sampled from real reference photos in `assets/characters/cooper/reference/` and `assets/characters/rocky/reference/` — not invented. Rocky's deepest shadow deliberately shares Mango's exact hex, a quiet visual "kinship" between the game's two orange-family characters, while Cooper's black/white/grey-plus-green reads as the cool contrast to both.

### Time-of-day light grading

Since the whole story takes place across one day (`GAME_BIBLE.md`, "A Single Day"), use these as scene-level colour-grade/overlay tints layered on top of the ramps above — they shift mood without requiring separate art per time of day.

| Time of day | Tint | Use |
|---|---|---|
| Dawn | `#3A4A6B` cool blue-grey | Tutorial Room, Empty House opening |
| Morning | `#FFF2C9` warm pale gold | Empty House resolving, The Park |
| Midday | `#FEF9E8` neutral bright | The Industrial Zone |
| Golden hour | `#FFB35C` warm amber | The Helipad/Airport, Cavoodle Forest arrival |
| Dusk | `#7A4A6B` purple-pink twilight | Cavoodle Forest's haunted turn, meeting Charlie |
| Night | `#1A1F3A` deep blue-black | Road Home, boss rush, Centre of Absence |

### Hue-shift shadows

Do not shade by simply moving the same hue toward black.

Prefer:

- orange → red-orange → warm brown / burgundy
- purple → blue-purple → indigo
- yellow-green → green → blue-green

Shadows should contain colour.

### Character/background separation

> **Characters should generally be warmer, brighter and/or more contrast-rich than the environment immediately behind them.**

> **Interactive objects can sit roughly one chroma/contrast step above passive scenery.**

This is a readability system, not an excuse to make everything saturated.

### Outline colour

Prefer warm near-black, dark brown, indigo or navy depending on the local palette. Avoid defaulting every asset to absolute RGB black unless a specific visual effect needs it.

---

## 7. Animal Vision / Colour Note

Dogs and cats perceive colour differently from humans, with much stronger blue/yellow discrimination than red/green discrimination.

Use this as a **thematic ingredient**, not a restrictive simulation:

- occasional blue/yellow-biased regions or magic effects
- an optional animal-vision / clue mechanic
- jokes about human colour names
- visual storytelling around what animals notice

Readability and the core bright-poppy art direction win over scientific literalism.

---

## 8. Character Reference Process

1. Photograph each pet: front, left profile, right profile, standing, sitting, one characteristic expression, close-ups of distinctive markings.
2. Identify the features that must survive reduction.
3. Develop the **portrait / character design first**, because likeness is easiest to judge at 48×48 or in concept art.
4. Lock one approved design per pet.
5. Redraw that design deliberately into the 32×32 battle and 24×16 overworld grammars.
6. Use the approved design as the reference for later poses and animations.
7. Use Mango and Cooper’s approved art as style anchors for the wider cast.

### Mango identity notes

- orange cat
- young/cute proportions, but not babyish
- fluffy / chubby
- judgemental, blasé, mildly arrogant expression
- still warm and friendly
- purple **hoodie**, not a grand wizard robe
- orange ears visibly emerge from the hood
- wand is a **black cat-teaser rod / fishing-rod-like toy with a simple bird/feather flutterer**, not a conventional fantasy staff
- exact eye colour and fur markings must be checked against real photos

### Cooper identity notes

- Cavoodle — black/white/grey coat with a warm, "ruddy" (never cold-grey) undertone throughout
- shaggy, grizzled muzzle and beard; warm cream/tan eyebrow markings, chest, and paw "socks" against the black body
- preserve real ear shape, coat, paw markings and open expressive face
- anxiety-to-courage personality should be readable in posture and animation
- signature item: a **green collar in a Japanese Shiba-style**, worn always — his equivalent of Mango's hoodie; not a scarf/harness substitute, this is his defining accessory

### Rocky identity notes

- Cavalier King Charles Spaniel — ruddy chestnut/copper patches (ears, back, tail base) on a clean white body, freckled white-and-brown muzzle, long silky ears
- deliberately colour-linked to Mango's orange family rather than treated as an unrelated hue — same warm "kin" story, redder/richer than Mango's more yellow-leaning orange
- immense, uncontrollable power should read in posture even at rest — never a small or dainty silhouette despite the breed's real-life daintiness

---

## 9. Mango’s Current Visual Reference Direction

Exploratory Gemini sprite sheets exist locally under:

`assets/characters/mango/reference/sprites/superseded/mango-sprite-sheet-gemini-raw-v{1,2,3}.png`

**v3 remains the strongest style/personality reference**, but it is not production truth.

Keep from v3:

- younger/cuter Mango proportions
- crisp bright palette
- purple hoodie direction
- grumpy / judgemental close-up expression
- strong profile/battle poses

Correct / replace:

- wand should use the black cat-teaser / feather-toy direction
- likeness details must come from real Mango photos
- all assets must be redrawn to the locked production dimensions in this document
- generated palettes must be conformed to the project palette
- generated pixel noise must be cleaned manually

Do not algorithmically downscale old 48×48 or ~92×92 experiments and call them final overworld sprites. Use them as reference and **redraw/regenerate at 24×16, on all fours**.

---

## 10. Animation Standards

Do not overanimate. Late-SNES character comes from strong poses and economical changes.

### Overworld — 24×16

Minimum production set:

| Animation | Frames | Notes |
|---|---:|---|
| Idle | 2 | Tiny breathing / tail / ear shift |
| Walk | 4 per cardinal direction | Clear contact/neutral rhythm |
| Interact | 2–3 | Contextual action |
| Surprise | 2 | Strong silhouette change |
| Hurt | 2 | Recoil |
| Sleep | 2–3 | Minimal loop |
| Wand / special interact | 3–4 | Only where needed |

### Battle — 32×32

| Animation | Frames | Notes |
|---|---:|---|
| Idle | 2–3 | One-pixel robe/tail/breath movement can be enough |
| Attack | 4–6 | Readable anticipation → strike → recovery |
| Cast | 4–6 | Strong pose plus effects handled separately where possible |
| Hurt | 2 | Fast recoil |
| Defend | 2 | Clear silhouette change |
| Victory | 3–5 | Personality first |
| KO | 1–2 | Static collapsed pose is fine |

Animation should not introduce markings, limbs or costume details that disappear between frames.

---

## 11. Tool Stack

### Reference / ideation

- real pet photos
- photos of the home and real objects
- manga / JRPG screenshots used for analysis of visual grammar, not copying
- Sean’s sketches / Procreate concepts when useful

### PixelLab — generation and exploration

Use PixelLab for:

- early character exploration
- pose variations
- turnaround starters
- animation starters
- environment concepts
- production assistance once a canonical design exists

**PixelLab output is provisional.** It does not become production art merely because it looks good.

### Aseprite — canonical production editor

**Aseprite is the source of truth for final pixel art.**

Use it to:

- clean generated art
- enforce dimensions
- enforce palettes
- repair silhouettes
- correct eye / marking drift
- animate
- tag frames
- export final PNG sprite sheets

Canonical editable files should be `.aseprite` wherever practical.

### Pixelorama — optional/open-source alternative

Pixelorama is a capable fallback/secondary editor. Do not create two competing source-of-truth workflows. Unless there is a specific reason otherwise, production masters live in Aseprite.

### itch.io — commodity asset library

Use licensed external assets for things whose uniqueness does not define the game:

- generic grass / stone / water
- basic props
- particles
- UI icons
- common spell effects
- simple environment pieces

Before use:

1. check the individual licence
2. log it in `docs/ASSET_LICENSES.md`
3. resize/redraw only in a pixel-safe way
4. recolour into the project palette where required
5. make sure the asset matches the 16×16 world grammar

Do **not** outsource the identity-defining layer: Mango, Cooper, major cast, signature monsters, major story props and important locations.

### Godot — game/runtime

Godot is the production runtime and level-building environment.

Pixel-art rules in-engine:

- nearest-neighbour texture filtering
- whole-pixel placement wherever possible
- integer scaling
- no texture smoothing
- no arbitrary sprite scaling
- preserve the 16×16 environment grid

**Target logical presentation: 320×180.**

The repository currently contains an earlier 480×270 viewport experiment in `project.godot`; treat **320×180 as the art-direction target** when the viewport is next standardised. Do not generate art against the assumption that 480×270 is the locked visual scale.

### GitHub — source control and documentation

- `docs/ART_BIBLE.md` is the canonical visual specification
- raw/reference material belongs under each family's `assets/<family>/reference/` locally unless/until storage policy changes
- game-ready exports belong under `assets/`
- changes to locked dimensions/palette rules must update this document in the same change

---

## 12. Canonical Asset Pipeline

```text
REAL REFERENCES / SKETCHES / VISUAL RESEARCH
                    ↓
             PIXELLAB / IDEATION
                    ↓
             ASEPRITE MASTER
       (redraw, cleanup, palette,
        animation, pixel discipline)
                    ↓
               PNG EXPORT
                    ↓
                  GODOT
                    ↓
             PLAY AT NATIVE SCALE
                    ↓
           APPROVE OR RETURN UPSTREAM
```

Practical flow:

1. Gather real reference photos.
2. Establish / confirm canonical character design.
3. Generate or sketch a starting asset at the **correct target size** where possible.
4. Bring it into Aseprite.
5. Enforce the shared palette and per-asset colour budget.
6. Remove stray pixels, semi-transparent pixels and generated noise.
7. Fix silhouette and likeness.
8. Animate economically.
9. Export PNG sprite sheets.
10. Import into Godot.
11. Test at native 1× and integer-scaled presentation.
12. Reject anything that only looks good when zoomed in.

---

## 13. Recommended Repository Art Structure

```text
art/
  references/
  palette/
    cooper-mango-master-palette.aseprite
    cooper-mango-master-palette.png
  characters/
    mango/
      source/
        mango.aseprite
      exports/
        mango_world.png
        mango_battle.png
        mango_portrait.png
    cooper/
      source/
      exports/
  enemies/
  tilesets/
  ui/
  effects/

assets/
  characters/
  enemies/
  tilesets/
  ui/
  effects/
```

The exact folder migration can happen incrementally. The important rule is conceptual: **editable source art and game-ready exports are different things.**

Current local reference drop zone remains (one `reference/` folder per character, under that character's own family folder):

```text
assets/characters/
├── mango/
│   └── reference/
│       ├── photos/
│       ├── sketches/
│       ├── sprites/
│       └── approved/
├── cooper/
│   └── reference/
│       ├── photos/
│       └── approved/
└── rocky/
    └── reference/
        └── photos/
```

---

## 14. AI / Asset Acceptance Checklist

Before an AI-generated or third-party asset is accepted, ask:

### Dimensions
- Is it built for the correct locked frame/grid?
- If it came from an older 48×48/92×92 experiment, has it been deliberately redrawn rather than blindly downscaled?

### Silhouette
- Does it read at native 1×?
- Can Mango and Cooper be distinguished instantly?
- Are ears, tail, hood, wand/harness and posture doing useful work?

### Palette
- Does it use a small subset of the master palette?
- Are there unnecessary near-duplicate colours?
- Are shadows hue-shifted rather than simply grey/black?

### Pixel quality
- Any anti-aliasing?
- Any semi-transparent fringe pixels?
- Any isolated generated noise?
- Any inconsistent outline thickness?

### Character continuity
- Do markings drift?
- Do eye positions change randomly?
- Do limbs/accessories disappear between frames?
- Does the expression still fit the character?

### World fit
- Is the character more readable than the scenery behind it?
- Does the asset match the bright, warm, poppy domestic-fantasy direction?
- Does it feel like the same game as the approved Mango and Cooper masters?

If it fails these checks, it is a **draft**, not production art.

---

## 15. Turning Real Places into the World

Photograph real objects and reinterpret them rather than generating a generic fantasy kingdom.

| Real object | RPG interpretation |
|---|---|
| Sofa | The Great Upholstered Range |
| Kitchen | Provisioning Hall |
| Cat tree | Tower of the Oracle |
| Dog bed | Guardian's Sanctuary |
| Vacuum cleaner | Mechanical Devourer |
| Robot vacuum | Wandering Iron Slime / Mi-chan boss form |
| Food bowl | Sacred Basin |
| Front door | Sealed Gate of Walkies |

The joke works best when the fantasy version is still recognisably the ordinary thing the pets know.

---

## 16. Division of Labour

- **Sean:** visual direction, monster/creature concepts, silhouettes, personality, final selection, hand-drawn intervention
- **Lillian:** pet likeness, humour, reactions, taste and character approval
- **AI tools / PixelLab:** variations, pose exploration, turnarounds, production assistance
- **Aseprite:** consistency, animation, palette enforcement, pixel cleanup, final authorship
- **Godot:** composition, timing, camera, effects, gameplay readability

---

## 17. Immediate Art Milestone

Before scaling production to the wider cast, produce and approve:

1. **Mango 48×48 portrait**
2. **Cooper 48×48 portrait** in the same visual language
3. **Mango 24×16 neutral overworld sprite (quadruped)**
4. **Cooper 24×16 neutral overworld sprite (quadruped)**
5. **Mango 32×32 battle sprite**
6. **Cooper 32×32 battle sprite**
7. one small **16×16 environment test tileset** using the shared palette
8. one Godot test screen showing all of the above at native scale and integer scaling
9. a first committed **48–64 colour master palette**
10. a reproducible note for each approved asset: reference used, tool/model, prompt/settings, target dimensions, cleanup decisions

Do not generate the entire cast before these samples look like one coherent game.

---

# One-Sentence Rule

> **Cooper & Mango uses a bright, warm late-SNES visual grammar: 16×16 world tiles, 24×16 symbolic quadruped overworld characters, 32×32 expressive bipedal battle characters, 48×48 likeness-rich bipedal portraits (64×64 for major story-beat close-ups), four-direction movement, compact per-asset palettes drawn from a shared ~48–64 colour master palette, hard pixel clusters with no antialiasing, chunky GBA/SNES-inspired UI, and Godot presentation designed around a 320×180 low-resolution canvas with nearest-neighbour integer scaling. Modern tooling underneath, old-school discipline on top.**
