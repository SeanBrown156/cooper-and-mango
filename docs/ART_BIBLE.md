# Art Bible

## Perspective and Dimensions

- Three-quarter top-down JRPG perspective (SNES/early-PlayStation JRPG energy — not a literal simulation of any existing game's assets)
- Overworld character frames: **48×48 pixels, locked** (decided 2026-08-11 over a larger 92×92 "Octopath/HD-2D" option — see rationale below)
- 8 directions per character (PixelLab's default; better than the originally-planned 4 for a top-down game, keep it)
- Environment tiles: 32×32 pixels
- Battle sprites: larger, 64×64 or 96×96, for expressive attacks/reactions/victory poses
- Portraits (dialogue/profile): a separate, higher-detail asset category — see Character Reference Process below. This is deliberately where pet-likeness detail lives, not the overworld sprite.

**Why 48×48 and not larger:** PixelLab's default output for the first Mango sprite came out at 92×92 (an unrequested default, not a deliberate choice). Weighed against the alternative of keeping that larger "Octopath-style" scale: 48×48 matches the SNES-chunky mood already set below and the reference-games table, stays forgiving of AI-generation imperfections and frame-to-frame drift, and keeps per-sprite production cost sane across the game's large planned cast (dozens of enemies/NPCs across 8 regions, built by two people plus AI assist — not a studio). The trade-off (less likeness detail directly in the overworld sprite) is deliberately absorbed by the separate portrait and battle-sprite channels instead. Any sprite already generated at 92×92 should be regenerated at 48×48 from the same approved reference — don't algorithmically downscale, pixel art doesn't survive that cleanly.

## Palette and Line

- Shared palette of roughly 16–24 colours across the whole game
- Dark brown or navy outlines, never pure black
- Minimal texture, no antialiasing, no soft edges
- Strong, readable animal silhouettes above all else

## Mood

Warm domestic fantasy — a distinctive internal description to reuse in prompts is:

> "Warm domestic fantasy, limited autumn palette, chunky pixel art, expressive animal silhouettes"

Avoid leaning only on "Final Fantasy style" as a prompt — it's too generic to hold a consistent identity across hundreds of assets.

## Animal Vision / Colour Note

Dogs and cats perceive colour weighted toward blue/yellow. This can inform world palettes (warm yellow, ochre, blue, violet-grey, muted earth tones), an optional "Animal Vision" overlay for clues/scent/hidden paths, and dialogue jokes (animals arguing over human colour names) — without forcing the whole screen into a restrictive simulation. Readability and art direction win over scientific accuracy.

## Character Reference Process

1. Photograph each pet: front, left profile, right profile, standing, sitting, one characteristic expression, close-ups of distinctive markings.
2. Identify which features must survive pixel reduction:
   - **Mango:** exact coat colours and facial markings, tail shape, judgemental eyes, a tiny mage mantle/charm/magical collar
   - **Cooper:** ear shape, coat and paw markings, open expressive face, a scarf/shield/harness resembling armour
3. Generate clean front/back/side concept turnarounds in PixelLab first.
4. Select one approved design per pet — treat it as the source of truth for every later pose.
5. Generate one neutral sprite before requesting all directions and animations.
6. Use Mango's approved sprite as a style reference when generating Cooper so both characters visibly belong to the same game.

## Sprite Cleanup

AI-generated sprites are starting material, not final assets. Correct manually in Aseprite: stray/semi-transparent pixels, markings that drift between frames, wobbly outlines, inconsistent eye positions, limbs that appear/disappear, off-palette colours, anything that weakens silhouette or likeness. At 48×48, a few pixels can change a whole face — this is closer to icon design than illustration.

## Animation Plan

| Animation | Frames | Detail |
|---|---:|---|
| Idle | 2–4 | Mango's tail flick; Cooper's breathing/ear movement |
| Walk | 3 per direction | 24 frames across eight directions |
| Attack | 4–6 | One strong, readable action |
| Hurt | 2–3 | Recoil and brief flash |
| Victory | 3–5 | A characterful celebration |
| Knockout | 1–2 | A static collapsed pose is sufficient |

Walk cycle loop: `step left → neutral → step right → neutral`.

## PixelLab → Aseprite → Godot Pipeline

1. Photograph pets across the required poses (see above).
2. Drop every raw photo into `assets/source/reference/<mango|cooper>/raw/` — no need to pre-sort or resize, see "Reference Photo Drop Zone" below.
3. Lock the art grammar before generating quantity: 48×48 overworld sprites, 32×32 tiles, eight movement directions, three walking frames per direction, one shared palette/outline colour, one fixed top-down perspective.
4. Generate turnarounds and one neutral sprite per pet in PixelLab.
5. Select and manually correct one canonical design per pet; save the chosen source photo into `assets/source/reference/<pet>/approved/` alongside the generated result, so the winning reference is easy to reuse later.
6. Use approved sprites as references for every later pose/animation — never regenerate characters from scratch.
7. Generate only the minimum needed for the current production stage (see `PRODUCTION_ROADMAP.md`) — the Tutorial Room slice needs idle, walk, interact, hurt, one battle pose.
8. Clean up in Aseprite (eyes, markings, paws, silhouette, transparency, palette drift).
9. Export PNG sprite sheets, import into Godot as `SpriteFrames` resources.
10. Test at integer scaling with nearest-neighbour filtering before producing the wider cast.

## Reference Photo Drop Zone

```
assets/source/reference/
├── mango/
│   ├── raw/        ← drop every Mango photo here, any resolution, unsorted
│   └── approved/   ← the specific photo(s) actually used as the PixelLab identity reference
└── cooper/
    ├── raw/        ← drop every Cooper photo here
    └── approved/   ← the specific photo(s) actually used as the PixelLab identity reference
```

**Why `raw/` isn't auto-ingested:** PixelLab's character-generation tool (`create_character`, mode `v3`) accepts exactly **one** reference image per call — either a base64 PNG (max 256×256) or an HTTPS URL — not a folder or batch. There's no "point PixelLab at a directory" option. So the practical workflow is:

1. Sean/Lillian drop as many raw photos as they want into `raw/` — front, both profiles, sitting, standing, a characteristic expression, close-ups of markings (see Character Reference Process above). No curation needed at drop time.
2. When generating, Claude Code or Codex picks (or is told) which single photo best matches the pose needed, resizes/crops it as required, and passes it to the PixelLab MCP tool directly from the local file.
3. Once a generation is approved, the winning source photo gets copied into `approved/` so it's easy to find and reuse as the reference for every subsequent pose/animation (per the "never regenerate from scratch" rule above).

This means: just keep dropping photos into `raw/` as you take them — no online editor, no manual pre-processing. Tell Claude/Codex when a fresh batch has landed and which pet/pose it covers, and generation can start from there.

**Note:** `assets/source/` is currently gitignored (see the open Git LFS question in the project setup) — reference photos live locally and are not yet pushed to GitHub. Worth revisiting once a real batch of photos lands.

## Current Status

PixelLab has been test-driven and is more demanding than expected — treat that as normal pipeline learning, not a signal the idea isn't working. Immediate next goal (Stage 1 prerequisite):

1. One approved glossy profile portrait of Mango
2. One approved glossy profile portrait of Cooper, same style
3. A simple character reference sheet for each
4. One neutral overworld sprite generated from each approved design
5. A documented, reproducible recipe (exact imports, prompt, model, dimensions, palette, settings) before attempting directions, walk cycles, or the wider cast

## Division of Labour

- **Sean:** monster/creature concepts, silhouettes, personality, final selection, hand-drawn details — his existing strength in drawing monsters/animals over humans is a real asset here, especially for the game's large cast of awakened-object enemies
- **Lillian:** pet likeness, humour, story reactions, taste and character approval
- **AI tools (PixelLab):** variations, clean turnarounds, palette experiments, pose exploration, production assistance
- **Aseprite:** consistency, animation, pixel cleanup, final authorship

## Turning Real Places into the World

Photograph real objects (sofa, food bowls, beds, hallway, houseplants, windows, toys, vacuum cleaner) and reinterpret them rather than generating a generic fantasy kingdom. Example naming convention:

| Real object | RPG version |
|---|---|
| Sofa | The Great Upholstered Range |
| Kitchen | Provisioning Hall |
| Cat tree | Tower of the Oracle |
| Dog bed | Guardian's Sanctuary |
| Vacuum cleaner | Mechanical Devourer |
| Robot vacuum | Wandering Iron Slime |
| Food bowl | Sacred Basin |
| Front door | Sealed Gate of Walkies |
