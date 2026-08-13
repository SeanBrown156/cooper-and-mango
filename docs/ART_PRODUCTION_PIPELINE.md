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

### Where experimentation lives

`.scratch/` (repo root, gitignored) is the sandbox for the "draft" and "multiply" steps of the core loop — trial crops, candidate palette remaps, composite mockups, side-by-side comparisons, anything produced while figuring out whether an approach works. Nothing in `.scratch/` is canon and nothing in it should be referenced by a `res://` path in a scene or `.tres` file. If a candidate is worth keeping but isn't finished, it graduates to `src/` (below), not straight to `assets/`; if it's actually done, it exports straight to `assets/`. Either way the scratch copy can then be deleted — it was never meant to be permanent.

### Where the "not final, but getting there" stuff lives

`src/` is the polishing tier — **versioned** (unlike `.scratch/`), holding the editable `.aseprite` masters you iterate on over time but that Godot never loads directly (`res://` paths always point into `assets/`). This is where a WIP asset belongs once it's past "is this a good idea" and into "I'm touching up this specific piece": redrawing a chipped sprite edge, adjusting a palette-remapped tile by hand, refining a pose. Layout mirrors `assets/` — e.g. `src/environments/tutorial_room/sofa.aseprite` is the editable master for `assets/environments/rooms/tutorial_room/sofa.png`. Workflow: open the `.aseprite` file, edit, re-export over the matching PNG in `assets/`, reimport in Godot. `src/palette/` (the master palette source) follows the same pattern.

So the full map: reference/raw material lives in `raw/`, third-party source lives in `assets/thirdparty/`, disposable experiments live in `.scratch/`, WIP editable masters live in `src/`, and only exported, approved, tested output lives in `assets/` proper.

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
