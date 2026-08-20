# Cooper & Mango Art Production Pipeline

> Operational source of truth for turning references, generated candidates,
> hand edits and premade assets into complete Godot-ready art packages.

The [Art Bible](ART_BIBLE.md) defines visual direction. Character identity
lives in each character's `CHARACTER_VISUAL_BRIEF.md`. This document defines
the production sequence, skill handoffs, lifecycle, review gates and Godot
handoff. Technical MCP setup belongs in [`docs/engineering/MCP.md`](../engineering/MCP.md).

## 1. Core lifecycle

The conceptual lifecycle is:

```text
reference → input → wip → approved
```

Where numbered folders exist, they normally map to:

```text
01_reference → 02_input → 03_wip → 04_approved
```

`shared/` is an organizational layer for cross-role material; it is not an
additional lifecycle stage. Raw inputs are not runtime content. WIP is the
complete actively curated package. Approved is the complete human-reviewed,
Godot-tested package.

Every package includes the relevant art and, where applicable, `.aseprite`,
metadata, `.tres` resources and `.tscn` scenes. Do not promote a PNG without
the resources and scenes required to use it correctly.

Typical character package shape:

```text
assets/characters/<character>/
  CHARACTER_VISUAL_BRIEF.md
  shared/01_reference/
  shared/02_input/
  <role>/01_reference/
  <role>/02_input/
  <role>/03_wip/
  <role>/04_approved/
```

`<role>` is normally `overworld`, `battle` or `portrait`. Not every character
has every role yet, and existing packages may still use an unnumbered folder;
the lifecycle meaning remains the same.

## 2. Authority and intake

Before work begins, read:

1. `docs/vision/GAME_BIBLE.md` for narrative and personality canon;
2. `docs/art/ART_BIBLE.md` for global visual constraints;
3. `assets/characters/<character>/CHARACTER_VISUAL_BRIEF.md` for identity;
4. the owning environment or character manifest;
5. the relevant references, current anchors and previous review state.

Use real photos for likeness and physical truth. Use visual references for
direction, not copying. Use generated material as provisional input until a
human reviews it.

When user direction changes a character's identity, expression, prop or pose,
record it through `$cm-character-visual-brief`. Keep current direction distinct
from canonical Game Bible facts and record unresolved conflicts as open
questions.

## 3. Skill-driven character workflow

This is the default character path. Skills are narrow operations with explicit
handoffs, not one monolithic asset skill.

| Stage | Skill/pathway | Input | Output |
|---|---|---|---|
| Identity | `$cm-character-visual-brief` | Game Bible, references, user direction | `CHARACTER_VISUAL_BRIEF.md` |
| Master synthesis (default for generic sprite-sheet requests) | `$cm-openai-master-sprite-sheet` or equivalent Gemini path | Complete reference set and brief | Clean master sheet plus metadata |
| Review labeling | Internal deterministic label tool | Clean master | Separate numbered review copy and cell map |
| Selection | `$cm-slice-master-sprite-sheet` | Clean master plus review IDs | Selected clean cells in role `02_input/` |
| Resolution gate | `$cm-prepare-role-resolution` | Selected cell | Transparent governed-size candidate |
| Static refinement | `$cm-pixellab-characters`, `$cm-pixellab-portraits`, explicitly requested OpenAI role skill, Aseprite or manual redraw | Prepared selected candidate | Refined static WIP candidate |
| Animation | `$cm-pixellab-animation`, `$cm-openai-animation-sheet`, `$cm-openai-video-to-sprite`, `$cm-higgsfield-autosprite`, `$cm-python-simple-pixel-animation` or Aseprite | Selected prepared anchor | Candidate frames/sheet |
| Frame validation | `$cm-normalize-animation-frames` | Candidate animation | Consistent frames, baseline, pivot and bounds |
| Palette cleanup | `$cm-aseprite-recolour` | WIP art only | Palette-conforming WIP art |
| Runtime validation | Godot | Complete WIP package | Scene/resource/runtime review |
| Promotion | Human approval | Reviewed, tested package | `04_approved/` package |

The numbered review copy is never source art. Cell coordinates come from its
map, but extraction always crops the original clean master. Do not process or
send unselected cells downstream.

## 4. Governed role contracts

| Role | Native size | Pose grammar | Required gate |
|---|---:|---|---|
| Overworld | 20×16 | Quadruped, north/south/east/west | Transparent target-size preparation and four-direction landmark review |
| Battle | 32×32 | Upright/bipedal, with deliberate action poses | Transparent target-size preparation and baseline/pivot review |
| Portrait | 40×40 | Upright/bipedal, expression/likeness first | Transparent target-size preparation and crop/likeness review |

The resolution gate removes white/black or near-uniform backgrounds from
selected candidates, preserves aspect ratio, uses nearest-neighbour fitting and
flags native-scale review. It must not stretch the character to fill the
canvas. If the pose cannot survive the target ratio, regenerate or redraw it.

## 5. Master-sheet workflow

Use `$cm-openai-master-sprite-sheet` as the default for a normal or generic
character sprite-sheet request. It uses the OpenAI API to generate one master
sheet when multiple roles or expressions must share one character model, with
the logical regions explicit: portrait, battle and overworld. Generate a
separate overworld, portrait, or battle sheet only when that role-specific
workflow is explicitly requested.

The production sequence is:

1. Generate and preserve one clean master.
2. Create a separate deterministic numbered review copy.
3. Have the user select IDs such as `P03`, `B07` and `O12`.
4. Extract those IDs from the clean master into role input folders.
5. Keep the master, review map, selected-cell metadata and provider provenance
   together in the shared manifest.
6. Prepare only selected cells at governed role resolution.

Whole-region crops are optional context. They do not replace cell selection.

## 6. Choosing complementary pathways

Provider choice depends on the problem; no provider is a permanent fallback or
automatic next step.

| Problem | Useful path | Gate that still applies |
|---|---|---|
| Cross-role consistency and ideation | OpenAI Image or Gemini master | Number, review and extract selected cells |
| Static role refinement | PixelLab, OpenAI Image, Aseprite/manual | Governed resolution and high-reference review |
| Walk/run or complex motion | PixelLab, OpenAI video or Higgs AutoSprite | Extract, normalize, inspect loop and landmarks |
| Simple breathing/bob/sway | Python integer-pixel animation or Aseprite | Preserve anchor, dimensions and baseline |
| Palette and cluster cleanup | Aseprite/Pixquare | Operate only in WIP; preserve source provenance |
| Environment ideation | OpenAI environment study, Gemini, PixelLab | Treat as input reference; validate grid, perspective and seams |

OpenAI, PixelLab, Higgs and Gemini outputs remain provisional. Generated video
is source material; runtime uses extracted PNG frames or Godot SpriteFrames, not
the provider video itself.

## 7. Environment and prop workflow

Environment production uses the same lifecycle but a different composition
logic:

1. Read the environment-local manifest and references.
2. Use `$cm-openai-environment-sprite` or Gemini for provisional
   pixel-art ideation when a reference transformation is useful.
3. Use licensed packs from input only with provenance recorded.
4. Use PixelLab or Aseprite to restyle, extend, crop or manually curate.
5. Preserve original compatible sheets where possible; use 16×16 TileSet
   atlases for grid-native tiles.
6. Use Sprite2D regions or scenes for coherent multi-cell furniture and props.
7. Keep collision, interaction and sorting in Godot resources/scenes.
8. Compose the room in WIP and test camera, walkability, seams, scale,
   contrast, lighting and character readability.
9. Promote the complete accepted room package together.

Tutorial Room defaults are strict orthographic high top-down, 16×16 grid and
480×270 camera. Its environment manifest is mandatory for room-specific
PixelLab work. Do not treat a generated complete tileset as production-ready.

## 8. Canonicalization and recolour

Distinguish:

- **Recolour:** replace selected colours.
- **Palette remap:** map the asset into the master palette.
- **Restyle:** change clusters, outlines, shading and detail to obey the Art Bible.
- **Redraw:** reconstruct the role asset when scaling or generation cannot preserve identity.

Use `$cm-aseprite-recolour` only on material already in `wip/`. Never recolour
directly in reference, input or approved. Preserve the original and record the
palette, source and output in the manifest.

## 9. Godot validation and promotion

Godot is the composition workbench and reality check, not merely the last
import step. Validate:

- native 1× readability;
- black foreground versus faded background outline class;
- character/background contrast;
- feet, pivot and baseline placement;
- tile seams and atlas connectivity;
- collisions, sorting and interaction;
- animation weight and loop continuity;
- UI coexistence and camera framing;
- palette harmony and visual family consistency.

Promotion requires a complete package: accepted art, editable source where
appropriate, metadata, manifests, Godot resources/scenes and a successful
running-game review. An isolated good-looking PNG is not approved production art.

## 10. Manifest and provenance requirements

For generated or transformed material, record:

- character/environment and role;
- source references and brief version/state;
- provider/model/tool;
- prompt or generation description;
- job ID where applicable;
- master version and selected cell IDs;
- input/output paths;
- dimensions and normalization state;
- palette/recolour state;
- review status and approval decision;
- known failures or open questions.

Historical outputs may remain for provenance, but active manifests must point to
current paths and current role contracts.

## 11. Related authority

- Visual direction: [`ART_BIBLE.md`](ART_BIBLE.md).
- Character identity: `assets/characters/<character>/CHARACTER_VISUAL_BRIEF.md`.
- Narrative canon: [`docs/vision/GAME_BIBLE.md`](../vision/GAME_BIBLE.md).
- MCP/tool setup: [`docs/engineering/MCP.md`](../engineering/MCP.md).
