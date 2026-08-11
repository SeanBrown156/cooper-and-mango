# Art Bible

> **Canonical visual source of truth for Cooper & Mango.**
>
> **Decision update — 2026-08-12:** this document supersedes the 2026-08-11 experiment that used 48×48 overworld characters and 32×32 environment tiles. The locked direction is now a tighter late-SNES / FFVI-inspired visual grammar: **24×24 overworld characters, 32×32 battle characters, 48×48 portraits, 16×16 environment tiles, and a 320×180 target logical presentation.**

## 1. North Star

**Cooper & Mango is a bright, poppy, late-SNES-inspired 2D RPG with warm domestic fantasy, chunky readable silhouettes, expressive animals, and deliberately limited pixel detail.**

The goal is **not** to reproduce SNES hardware limitations literally or copy any existing game's assets. The goal is to use the visual grammar of games such as Final Fantasy VI — tiny symbolic overworld characters, theatrical battle staging, richer portraits and monsters, economical animation, hard pixel edges, strong silhouettes — while building the game with modern tooling in Godot.

A useful shorthand for prompts and reviews:

> **“Bright warm domestic fantasy, late-SNES JRPG proportions, chunky pixel clusters, expressive animal silhouettes, joyful colour, crisp hard edges.”**

Avoid using only “Final Fantasy style” as a prompt. It is too broad and encourages inconsistent or derivative output.

---

## 2. Locked Technical Art Specification

### Core dimensions

| Asset | Locked frame / grid | Typical subject occupancy | Notes |
|---|---:|---:|---|
| Logical game presentation | **320×180** | — | Modern 16:9 canvas with deliberately low-resolution composition |
| Environment tile | **16×16** | — | Canonical world-building grid |
| Overworld player / NPC | **24×24** | ~18–22 px tall | Tiny symbolic representation; silhouette first |
| Battle player character | **32×32** | ~24–30 px tall | Redrawn for combat; not an enlarged overworld sprite |
| Small battle enemy | **32×32** | variable | Only where deliberately tiny |
| Regular battle enemy | **48×48** | variable | Standard enemy target |
| Large enemy / mini-boss | **64×64** | variable | May overflow visual mass within battle layout |
| Major boss | **64×64 to ~128×96** | variable | Set-piece art may break regular sprite scale |
| Dialogue portrait | **48×48** | ~42–46 px | Separate drawing; primary likeness/expression layer |
| Optional major/menu portrait | **64×64** | ~56–62 px | For special UI or important scenes, not required by default |
| Common prop | **16×16 / 16×32 / 32×32** | variable | Align to the environment grid wherever sensible |

### Historical reference, not a production constraint

The classic SNES presentation was commonly built around a roughly **256×224** visible canvas and an 8×8 hardware tile vocabulary. Final Fantasy VI used extremely small playable character art — roughly the visual territory of a ~16×24 character — and reused compact character sprites very economically.

We are deliberately giving Mango and Cooper a little more room because animal silhouettes need ears, tails, fluff, posture and signature props to remain readable. **24×24 is our SNES-plus compromise.**

### Important hierarchy rule

The same character is **redrawn at different levels of abstraction**:

- **24×24 overworld:** icon of the character
- **32×32 battle:** pose and action readability
- **48×48 portrait:** likeness, fluff, face, emotion, costume detail

Do **not** create one large drawing and algorithmically scale it down into all three roles. They are separate drawings of the same design.

---

## 3. Mango at Each Scale

### Overworld Mango — 24×24

This is an icon of Mango, not a miniature illustration.

Must survive reduction:

- orange-cat silhouette
- oversized readable ears
- purple hoodie / hood shape
- fluffy cheek or chest suggestion
- tail silhouette
- black cat-teaser wand / fishing-rod-like toy silhouette where the pose allows
- judgemental / blasé attitude communicated mainly through posture

Facial detail may be only a handful of pixels. Eyes may literally be one pixel each. If the silhouette does not read at native 1× scale, adding more detail is the wrong fix.

### Battle Mango — 32×32

Redraw rather than enlarge.

Direction:

- slightly more upright / bipedal
- chubby and fluffy
- 3/4 combat stance
- one paw clearly gripping the wand
- stronger tail gesture
- enough face to sell confidence / mild arrogance / warmth
- robe/hoodie movement can animate by only one or two pixels

### Portrait Mango — 48×48

This is the likeness layer.

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

### Mango palette principle

A typical Mango asset might use:

**Orange ramp**
- yellow-orange highlight
- Mango orange midtone
- red-orange shadow
- warm brown / burgundy deep shadow

**Purple hoodie ramp**
- pink-lavender highlight
- rich purple midtone
- blue-purple shadow
- indigo deep shadow

**Accents**
- cream / pale fur
- warm near-black or deep navy-brown outline
- restrained pink for nose/ear detail

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
5. Redraw that design deliberately into the 32×32 battle and 24×24 overworld grammars.
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

- preserve real ear shape, coat, paw markings and open expressive face
- anxiety-to-courage personality should be readable in posture and animation
- any armour-like accessory should still feel derived from a real pet object: scarf, harness, tag, etc.

---

## 9. Mango’s Current Visual Reference Direction

Exploratory Gemini sprite sheets exist locally under:

`assets/source/reference/mango/raw/mango-sprite-sheet-gemini-raw-v{1,2,3}.png`

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

Do not algorithmically downscale old 48×48 or ~92×92 experiments and call them final overworld sprites. Use them as reference and **redraw/regenerate at 24×24**.

---

## 10. Animation Standards

Do not overanimate. Late-SNES character comes from strong poses and economical changes.

### Overworld — 24×24

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
- raw/reference material belongs under `assets/source/` locally unless/until storage policy changes
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

Current local reference drop zone remains:

```text
assets/source/reference/
├── mango/
│   ├── raw/
│   └── approved/
└── cooper/
    ├── raw/
    └── approved/
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
3. **Mango 24×24 neutral overworld sprite**
4. **Cooper 24×24 neutral overworld sprite**
5. **Mango 32×32 battle sprite**
6. **Cooper 32×32 battle sprite**
7. one small **16×16 environment test tileset** using the shared palette
8. one Godot test screen showing all of the above at native scale and integer scaling
9. a first committed **48–64 colour master palette**
10. a reproducible note for each approved asset: reference used, tool/model, prompt/settings, target dimensions, cleanup decisions

Do not generate the entire cast before these samples look like one coherent game.

---

# One-Sentence Rule

> **Cooper & Mango uses a bright, warm late-SNES visual grammar: 16×16 world tiles, 24×24 symbolic overworld characters, 32×32 expressive battle characters, 48×48 likeness-rich portraits, compact per-asset palettes drawn from a shared ~48–64 colour master palette, hard pixel clusters with no antialiasing, and Godot presentation designed around a 320×180 low-resolution canvas with nearest-neighbour integer scaling.**
