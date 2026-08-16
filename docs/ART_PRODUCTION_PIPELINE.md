# Cooper & Mango Art Production Pipeline

> Project-specific workflow for turning references, sketches, AI drafts and premade assets into consistent, game-ready pixel art.
>
> This document complements `docs/ART_BIBLE.md`. The Art Bible defines **what the game should look like**; this file defines **how we produce and scale the art without losing that look**.

## Core loop

The art pipeline is **iterative, not linear**:

> Ideate → draft → canonicalise → multiply → clean → test in Godot → feed the improved result back into the loop.

AI is not a single upstream step. PixelLab can appear both at the beginning and later in production once a strong canonical asset exists.

---

## 1. Ideation and reference layer

Use this layer to decide what an asset should feel like before worrying about production-perfect pixels.

### Procreate

Use for:
- loose sketches;
- creature and character design;
- poses;
- environment ideas;
- monster concepts;
- rough animation thumbnails;
- visual problem solving with Apple Pencil.

### FigJam

Use as the main **visual reference board** for Cooper & Mango.

Store and organise:
- reference games;
- manga and illustration references;
- UI examples;
- palette references;
- sprite comparisons;
- screenshots;
- environmental inspiration;
- visual notes and callouts.

FigJam is the quick, digestible art-direction surface for Sean and for Claude when reasoning about references.

### Gemini / ChatGPT

Use for:
- rapid visual ideation;
- concept exploration;
- composition ideas;
- style experiments;
- critique and comparison;
- testing different visual directions quickly.

Gemini-generated sprite sheets are **approximations**, not production truth. They are useful for silhouette, colour planning, costume ideas, pose direction and mood, but they often drift from exact pixel dimensions, palette constraints and sprite consistency.

### Real photos

Real photos remain the likeness and physical-reference truth for:
- Mango;
- Cooper;
- real household objects;
- rooms and furniture;
- locations;
- textures and distinctive props.

---

## 2. PixelLab has two jobs

PixelLab is unusual because it belongs in both **ideation** and **production multiplication**.

### Early-stage PixelLab

Use it to:
- draft pixel-art concepts closer to the correct medium and dimensions than generic image generation;
- test silhouettes;
- produce early character/prop/environment candidates;
- work inside the project palette where possible;
- explore pixel-specific versions of ideas from Procreate, Gemini, photos or FigJam.

These outputs may still need substantial cleanup, redraws or simplification.

### Late-stage PixelLab

Once a canonical asset exists, use PixelLab to multiply it:
- south-facing character → north/east/west candidates;
- idle → pose variants;
- canonical frame → animation candidates;
- approved prop → related variants;
- approved tile → additional tile variations;
- approved environment style → compatible extensions;
- inpainting / local corrections where useful.

A common Cooper & Mango loop is:

1. PixelLab drafts an initial candidate.
2. Aseprite or Pixquare cleans, redraws or substantially improves it.
3. That improved asset becomes the canonical reference.
4. PixelLab uses the canonical reference to produce directions, poses, animations or variants.
5. Aseprite/Pixquare correct drift.
6. The corrected result becomes a stronger input for the next PixelLab pass.
7. Repeat until the full asset family is coherent.

Do **not** treat PixelLab as either “only concept art” or “one-click final art.” Its value increases as the project accumulates canonical references and constraints.

---

## 3. Canonical production tools

### Aseprite — desktop production master

Use Aseprite for:
- canonical `.aseprite` files;
- palette control;
- precise pixel cleanup;
- full redraws;
- animation and cels;
- onion skinning;
- frame timing and animation tags;
- sprite-sheet export;
- indexed-palette work;
- batch or CLI export where useful.

### Pixquare — iPad / Apple Pencil production companion

Use Pixquare for:
- direct pixel drawing with Apple Pencil;
- silhouettes;
- cleanup and repainting;
- animation work;
- palette-driven editing;
- mobile/couch/train/bed production sessions;
- `.aseprite` round-tripping.

Aseprite and Pixquare are not competing sources of truth. They are desktop and Pencil interfaces onto the same pixel-art production discipline.

---

## 4. What counts as truth

Different sources have different authority:

- **Real photos** = likeness / physical truth.
- **FigJam references** = visual-direction truth.
- **Gemini / generic AI concepts** = approximation and ideation.
- **Locked project palette** = colour truth.
- **`docs/ART_BIBLE.md`** = style and technical truth.
- **Approved canonical `.aseprite` / Pixquare source** = production truth.

A clean AI image is not automatically canon. A hand-drawn image is not automatically canon either. Canon is the approved master asset that downstream generation and implementation reference.

---

## 5. Character production method

For major characters such as Mango and Cooper:

1. Gather photos, sketches and FigJam references.
2. Explore with Procreate, Gemini and/or PixelLab.
3. Produce one strong canonical key view in Aseprite/Pixquare.
4. Make sure it obeys the Art Bible and locked palette.
5. Use that view as the reference for PixelLab multiplication.
6. Generate the required directions/poses/animation candidates.
7. Review the entire set together.
8. Correct silhouette, anatomy, costume, markings, palette drift, tail/ear thickness, feet placement and perspective.
9. Promote the corrected set as the new canonical family.
10. Test it in Godot early.

For four-direction movement, get the **south/front-facing sprite genuinely right first**, then use it as the strongest reference for north/east/west generation.

Animation consistency matters more than smoothness. A beautiful animation where the character changes design frame-to-frame is a failed animation.

---

## 6. Canonical asset packets

Each important character or asset family should gradually accumulate a small reference packet containing:

- canonical master file;
- approved palette subset;
- approved key view;
- battle reference where relevant;
- portrait reference where relevant;
- likeness / marking notes;
- costume or prop notes;
- animation invariants;
- PixelLab generation recipe/settings where reproducibility matters.

Claude and PixelLab should increasingly work from these packets rather than vague prose memory.

---

# Environment, tiles and props

Environment production should be **less precious than hero-character production** while still obeying the same palette and pixel grammar.

The goal is not to hand-author every generic chair, grass tile, rock and bowl from scratch.

## 7. Three asset tiers

### Tier A — identity assets

Give these the full bespoke treatment:
- Mango;
- Cooper;
- party members;
- major bosses;
- signature awakened-object enemies;
- iconic locations;
- narratively important props.

These may involve heavy hand-drawing, PixelLab iteration, bespoke AI generation and multiple cleanup passes.

### Tier B — distinctive world assets

These matter because they make the world feel like **Cooper & Mango**, but they can begin from references or existing art:
- the real sofa;
- cat tree;
- food bowls;
- Cooper's bed;
- household furniture;
- Mi-chan / the robot vacuum;
- recognisable architecture and regional objects.

Typical flow:

> Photo / sketch / reference → PixelLab or premade base → palette remap → Aseprite/Pixquare restyle → approve → PixelLab extend if useful → Godot test.

### Tier C — commodity environment assets

Do not waste bespoke production time where the player only needs a convincing world:
- grass;
- dirt;
- generic floors;
- plain walls;
- rocks;
- fences;
- pots;
- crates;
- barrels;
- bushes;
- common tables/chairs;
- generic decorative objects.

For these, licensed premade 16px-friendly asset packs are encouraged.

---

## 8. Premade-asset pipeline

For commodity tiles and props:

1. Find a good **licensed** base asset or coherent tileset family.
2. Record the licence/source in `docs/ASSET_LICENSES.md`.
3. Preserve the useful structure and silhouette.
4. Remap its colours into the locked Cooper & Mango palette.
5. Check whether the original pixel grammar fits our Art Bible.
6. Restyle outlines, shading, clusters or detail density where needed.
7. Promote the cleaned result as an approved environment reference.
8. Use PixelLab to extend that approved family with compatible variations where useful.
9. Clean the generated extensions in Aseprite/Pixquare.
10. Test the family in Godot against the actual characters and UI.

This is not merely “change the hue.” Distinguish:

- **Recolour** — swap one colour for another.
- **Palette remap** — map the entire asset into our master palette.
- **Restyle** — alter clusters, outlines, shading and detail so the asset obeys our game’s pixel grammar.

Palette remapping is the baseline. Restyle only as much as necessary.

---

## 9. PixelLab as environment extender

Once one environment family is canonical, PixelLab can accelerate variation rather than invent everything from nothing.

Examples:
- approved grass tiles → flower/weed/worn variants;
- approved wall family → cracked/damaged/decorated variants;
- approved pot → multiple compatible pot variants;
- approved floor → scuffed/stained/aged versions;
- approved furniture → regional or story-specific variations;
- approved tiles → additional compatible environmental details.

Preferred loop:

> good base structure → palette remap → clean canonical example → PixelLab extension → cleanup → palette check → Godot.

For tile assets, connectivity and seam behaviour matter more than whether a single tile looks beautiful in isolation.

---

## 10. Avoid environment Frankenstein

Do not accumulate ten unrelated asset packs simply because each contains one useful item.

Even with a shared palette, different packs may have incompatible:
- outline weight;
- dithering;
- cluster size;
- light direction;
- perspective;
- shading depth;
- detail density.

Prefer **one dominant base family** for a region or environment, then extend and remix it.

---

## 11. Environment base kits

Each major region should eventually have a small canonical environment kit containing:

- tile grid rules;
- approved palette subset;
- light direction;
- outline treatment;
- floor examples;
- wall examples;
- foliage/terrain examples where relevant;
- common prop examples;
- approved base tileset;
- PixelLab extension references/settings where useful.

This is the environment equivalent of a canonical character packet.

---

## 12. Godot is the reality check

Art is not complete until it works in the running game.

Test early for:
- native-scale readability;
- character/background contrast;
- tile seams;
- collisions and feet anchors;
- visual scale;
- animation weight;
- palette harmony;
- UI coexistence;
- whether bespoke and remixed assets genuinely feel like one game.

A sprite or tile that looks great alone but fails in the room is not finished.

---

## 13. Asset hygiene

Keep separate locations for:
- reference material;
- raw AI generations;
- third-party source assets;
- working source files;
- canonical masters;
- exported game-ready assets.

Avoid `final-final-v7.png` chaos. One obvious canonical master per asset family should always exist.

Use predictable naming and keep raw AI generations out of game-ready asset folders.

### The lifecycle, end to end

Every asset family (`assets/characters/mango/`, `assets/environments/tutorial_room/`, etc.) moves content through the same four stages, plus a same-level `composite/` for Godot wiring: **`reference/` → `input/` → `wip/` → `approved/`**, `composite/`. Not called "final" deliberately — an approved asset can still be superseded by a new approved version later; the word just isn't allowed to imply permanence it doesn't have.

### Where reference material lives

Each family's `reference/` folder (e.g. `assets/characters/mango/reference/`, `assets/characters/cooper/reference/`, `assets/characters/rocky/reference/`) holds photos, other games' images, and other look-only reference points — **not usable as something to work on directly**: real reference photos and sketches of Mango, Cooper, and Rocky, never edited directly or loaded by Godot. Excluded from Godot's editor scan via an empty `.gdignore`, and untracked in git except for the folder structure itself (`.gdignore`/`.gitkeep`) — actual reference files stay local until a storage/LFS policy is decided. Subdivided by *source* (`photos/`, `sketches/`, `locked/` — locked design-direction stills), not by which sprite scale-tier it might inform — a photo isn't yet committed to becoming overworld, battle, or portrait art. Deliberately called `locked/`, not `approved/` — that word means something different one level up (the family's own Godot-loaded lifecycle tier), and reusing it here for a different concept was exactly the kind of same-word-different-meaning collision this whole model exists to kill.

### Where input material lives

Each family's `input/` folder (e.g. `assets/environments/input/`, `assets/ui/input/`) holds **actual game sprites/art that ARE usable as a starting point**, just not reviewed or cleaned up yet: off-the-shelf vendor/found asset packs meant to be cut, remixed, or composited into final art (most third-party packs land here once downloaded but before being drawn from), *and* initial AI generations ready for cleanup — a raw PixelLab batch, a raw Gemini or ChatGPT sprite-sheet export, anything freshly generated that hasn't been reviewed or started on yet, regardless of which tool produced it. Same treatment as `reference/`: excluded from Godot's editor scan via `.gdignore`, untracked in git except folder structure. The distinction from `reference/` is deliberate — `reference/` is look-only, never becomes the art directly, while `input/` is meant to be composited into it or cleaned up into it. The distinction from `wip/` is also deliberate — the moment a human actually starts hand-cleaning or redrawing something from `input/`, it moves to `wip/`; `input/` is "available," `wip/` is "someone's actively touching this right now." A pack that's been fully composited into a finished asset and is now kept only for provenance graduates back to `reference/` instead (e.g. `assets/environments/tutorial_room/reference/rgsdev_cc0_topdown_template/`, whose content is already baked into the finished Tutorial Room tileset).

### Where experimentation lives

Each asset family's `wip/` folder (e.g. `assets/environments/tutorial_room/wip/`, tracked in git) is the sandbox for the "draft" and "multiply" steps of the core loop — trial crops, candidate palette remaps, composite mockups, side-by-side comparisons, editable `.aseprite` masters — anything a human is actively mid-edit on right now, having already been picked out of `input/`. Nothing in a `wip/` folder is canon and nothing in it should be referenced by a `res://` path in a scene or `.tres` file. Godot's editor skips scanning/importing `wip/` folders entirely (empty `.gdignore` file in each one). Split into type subfolders (`overworld/`, `battle/`, `portrait/`, etc.) only when a family genuinely has more than one type in flight simultaneously — not a hard requirement, unlike `approved/` below. Workflow: open the `.aseprite` file, edit, re-export over the matching PNG in the family's `approved/` folder, reimport in Godot. `assets/palette/` (the master palette source and its exported `.png`) is an exception to the whole lifecycle — it's a production resource used directly by Godot with no meaningful draft state, so it lives at the top level of its family with no `wip/`/`reference/`/`input/`/`approved/` subfolder.

### Where approved (Godot-loaded) content lives

Each family's `approved/` folder is the current authoritative version, promoted from `wip/` once locked in — e.g. `assets/characters/mango/approved/overworld/`, `assets/environments/tutorial_room/approved/`. Unlike `wip/`, the type split is **always** present here, even when a family only has one type today — this is the tier Godot actually loads, so it must never be ambiguous which content is which type. For characters that means `overworld/`, `battle/`, `portrait/` (the Art Bible's scale hierarchy); for other families it means whatever that family's content actually is (e.g. a room's props/tileset).

So the full map: per-family personal reference material lives in `assets/<family>/reference/`, third-party source or fresh unreviewed output not yet being drawn from lives in `assets/<family>/input/` (or `assets/<family>/<subarea>/reference/` for archived-but-provenance-relevant source that's already been used), actively-hand-edited masters live in `assets/<family>/.../wip/`, and only exported, approved, tested output lives in `assets/<family>/.../approved/`. Third-party source that's actually wired into a scene lives *inside* that specific room/instance's `approved/thirdparty/` (e.g. `assets/environments/tutorial_room/approved/thirdparty/bitglow_pixelinterior_lrk_v1_1/`) — not a family-level bucket, since being wired in means it's tied to one specific scene, same as any other approved content; `thirdparty/` there is just a sub-label for license-provenance clarity, not a separate lifecycle tier.

For families broad enough to contain multiple distinct instances (`environments/` can hold many rooms/regions; `characters/` currently can't, since each character folder already *is* the specific instance), there are two levels this lifecycle attaches at: family-level `reference/`/`input/`/`wip/` for material not yet tied to any particular instance, and that instance's own full `reference/`/`input/`/`wip/`/`approved/`/`composite/` set once it is. A downloaded tileset pack nobody's assigned to a room yet sits at `assets/environments/input/`; the moment it's actually drawn from for a specific room, it moves down into that room's own `input/`/`wip/`, and once wired into that room's shipped scene, into that room's `approved/`.

### Where the Godot-side assembly of an approved asset lives

`reference/`/`input/`/`wip/`/`approved/` are a pure content library — raw PNGs, audio, and similar files only. None of them hold the Godot resources that assemble that content into something the engine actually uses as a unit: a `TileSet` built from a tilesheet PNG, a `SpriteFrames` built from an animation sheet, a `Theme` built from UI panels. Those composition resources live in that family's own `composite/` folder instead (e.g. `assets/environments/tutorial_room/composite/tutorial_room_tileset.tres`) — not a separate top-level tree, and not called `resources/`, since Godot's own engine vocabulary already overloads "Resource" for nearly everything, including plain textures. So once a PNG has been exported into `approved/`, the next step for anything that needs Godot-side assembly (not every asset does — a plain sprite `Texture2D` is referenced directly) is to build or update the matching `.tres` under that family's `composite/`, then wire scenes to that `.tres`, not directly to the raw asset.

---

## 14. Acceptance criteria

An approved asset should be:
- on-palette;
- readable at native scale;
- consistent with the Art Bible;
- consistent with its canonical family;
- free of accidental/noisy pixels;
- correctly aligned and exported;
- appropriately licensed/provenanced;
- tested in Godot.

For generated directions or animations, also check:
- head/body dimensions;
- costume and markings;
- tail/ear thickness;
- prop size;
- perspective;
- palette drift;
- frame-to-frame identity consistency.

---

## 15. Tool roles for Cooper & Mango

### Ideate / reference
- Procreate
- FigJam
- Gemini / ChatGPT
- photos
- game / manga / UI references

### Draft and multiply
- PixelLab
- Gemini for looser concept exploration

### Canonicalise, redraw and clean
- Aseprite
- Pixquare

### Implement and test
- Godot

### Orchestrate and remember
- Claude Code
- GitHub

## Guiding rule

> **Handcraft the things players remember. Industrialise the things they merely need to believe are there.**

Use AI to multiply clear intent rather than replace art direction. As Cooper & Mango accumulates canonical characters, palette rules, environment kits and approved asset families, the AI-assisted parts of the pipeline should become faster and more reliable rather than more random.

---

## 16. Locked presentation and environment-tile practice

### Keep these three concerns separate

| Concern | Locked decision | What it changes |
|---|---|---|
| Logical presentation | **480×270** | Camera composition and how much of a room is visible |
| World grid / TileMap cell | **16×16** | Placement, collision, reusable environment vocabulary |
| Character asset tiers | **24×16 overworld; 32×32 battle; 48×48 portrait** | The deliberate amount of detail in each character role |

Do not raise the tile grid or character frames merely because PixelLab can generate on a larger canvas. Screen resolution is not sprite resolution. The 480×270 presentation gives useful camera space and a clean 4× 1080p scale; it does not make the art more complex.

### Tilesets are atlas sheets, not a pile of manually chopped PNGs

Keep a compatible tileset as one source PNG. In Aseprite, turn on a **16×16 grid**; in Godot, create a TileSet Atlas source from the approved sheet, set the atlas tile size to **16×16**, define the usable cells and their collision/navigation metadata, then paint the room with a TileMap. The resulting TileSet resource belongs in the room's composite folder.

Individual exported PNGs are only needed when an asset is genuinely standalone (for example, a Sprite2D prop, an animated object, or a hand-managed reusable component). Aseprite slices can batch-export such regions where useful, but manual chopping is not the default workflow.

A 32×32 or 48×32 piece of furniture is a **meta-tile** occupying several 16×16 world cells, not a reason to change the grid. Do not algorithmically downscale a good 32×32 object to 16×16 just to make it one cell.

### PixelLab's role in environment work

Use PixelLab to generate:
- a small, coherent top-down terrain family or transition set;
- style-matched individual props and variants;
- environmental extensions from an approved room screenshot or kit;
- multiplication passes after an approved art/palette anchor exists.

Do not treat a giant generated “complete apartment tileset” as production-ready. It must still be checked for repeated-edge seams, compatible palette use, grid alignment, recognisable domestic forms, collision meaning and reuse value.

For a generated environment request, name the production constraints: three-quarter top-down RPG view, hard edges, transparent background where appropriate, **16×16 tile grid**, master-palette subset, and whether the output is a single prop, a 2×2 meta-tile, or a terrain/transition set. A generated result enters input; it moves to wip the moment human cleanup starts; only the tested export belongs in approved.

### PixelLab's role in characters

Ask PixelLab for the intended **role frame**, not a vague large character image:
- overworld: **24×16**, quadruped, transparent background;
- battle: **32×32**, upright/bipedal;
- portrait: **48×48**, upright/bipedal;
- animation: explicit frame size, direction count and shared baseline.

If PixelLab is more reliable at a larger generation canvas, treat that output as a draft/reference and deliberately redraw/crop it into the locked production frame in Aseprite or Pixquare. Never resize a detailed large sprite down and call it a finished 24×16 overworld asset.

The loop remains: **reference and approved anchors → PixelLab candidate/multiplication → Aseprite/Pixquare canonicalisation → Godot validation → new approved anchor**.

