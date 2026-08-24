# MCP setup, capabilities and governance

This document combines the project MCP setup notes with the capabilities and
operating rules for the PixelLab, SpriteCook, Aseprite and Godot AI
integrations.

## Setup

Project-owned MCP definitions live in `.mcp.json` for Claude Code and
`.codex/config.toml` for Codex. Keep credentials out of both files.

Export the PixelLab token before starting a client:

```sh
export PIXELLAB_API_TOKEN="..."
```

PixelLab is remote. Claude Code connects over HTTP; Codex uses the
`mcp-remote` bridge because its local MCP transport is stdio.

Godot AI is local-only and requires the Godot editor running with this project
open and the `godot_ai` plugin enabled. Its local server uses HTTP port 8000
and WebSocket port 9500.

Aseprite MCP is launched with `npx` and requires Aseprite installed locally.
The current executable is configured as:

```text
/Applications/Aseprite.app/Contents/MacOS/aseprite
```

SpriteCook is the hosted game-art generation MCP. Claude Code and Codex use
client-specific endpoints and authenticate through SpriteCook OAuth on first
protected use; no API key is stored in this repository.

Restart Claude Code or Codex after changing MCP configuration or environment
variables. Codex must trust the workspace before loading `.codex/config.toml`.

## PixelLab

Repo-specific PixelLab workflows are split by production need under
`.agents/skills/cm-pixellab-*`. Use the narrowest matching skill: characters,
animation, portraits, environments, or props. These skills encode the
Cooper & Mango constraints that are easy to lose in a generic prompt, such as
four-direction overworld movement, directional 16×20 north/south and 20×16
east/west bounds, plus 32×32 battle and 48×48 portrait role bounds, orthographic
16×16 environments, and complete WIP/Approved handoff packages.

PixelLab is the generative asset and variation system. It can create or edit:

- four- and eight-direction characters, including quadrupeds;
- character states, portraits, animations, talking GIFs and vocal animations;
- freeform pixel-art images, props, map objects, UI assets and fonts;
- top-down Wang/autotile tilesets and connected terrain transitions;
- roads and paths, building kits, sidescroller tilesets and isometric tiles;
- maps and map-object placements.

It can also edit whole images, inpaint masked regions, animate loose sprites,
attach portraits, inspect jobs, check balance and download results.

PixelLab operations are asynchronous and may consume subscription generations.
Delete operations are destructive. Generated output is a production candidate:
for a well-briefed room kit, tileset or non-identity prop it may move directly
into WIP, then to approved after Godot validation. Aseprite cleanup is used
when needed, not required by default.

### Tutorial Room PixelLab hard constraints

For `tutorial_room_mango`, discovery resolves the owning
`assets/environments/tutorial_room_mango/environment_manifest.json`; use that
local manifest before every generation request. Future environments follow the
same direct-package convention. Do not create or consult a root-level manifest
copy. The default is native 16×16-grid sizing, transparent
background, and strict orthographic high top-down view. Oblique, isometric,
side-view, perspective, and visible-front-face outputs are invalid unless the
request explicitly overrides the room contract. PixelLab canvas size is not
the same as visible asset bounds: when the API requires a 32px minimum canvas,
keep transparent padding and fit the actual content to the specified bounds.

### Environment manifest boundary

An environment-local manifest is the generation and asset ledger: references,
provider jobs, asset IDs, technical bounds, variants, prompts, provenance,
review state, and generation order. Tooling discovers these manifests from
`assets/environments/*/environment_manifest.json` and validates their package
identity; it must not assemble a second hand-authored report.

Godot remains authoritative for runtime composition: `.tscn` and `.tres`
resources own node structure, atlas/region placement, draw order and sorting,
collision, interaction, navigation, camera wiring, and scene behaviour. A
manifest may describe intended bounds or placement inputs, but changing it does
not change a Godot scene. Validate the assembled result in Godot before
promotion.

## SpriteCook

SpriteCook and PixelLab overlap substantially and can both be used for most
game-art generation tasks. SpriteCook is especially useful when the job
benefits from a consistent family of assets, an existing local image as a
reference, or an engine-ready export:

- cohesive prop, UI and texture sets that share a visual style;
- editing or importing an existing sprite, including background cleanup;
- animating an approved still into explicit loops such as idle, walk, run or
  attack;
- reusable presets, asset IDs and manifests that keep related generations
  connected;
- Godot-ready character animation and top-down/platformer terrain exports,
  including `SpriteFrames` and configured `TileSet` resources where supported.

These are tendencies rather than strict boundaries: choose whichever tool
produces the better result for the particular prompt, reference and art
direction. Neither tool replaces Aseprite as the pixel-level cleanup, palette
and approval tool. SpriteCook output remains provisional until it passes the
same human review and Godot validation as every other generated asset.

## Aseprite

Aseprite is the pixel-art production master. Its MCP can inspect sprites,
frames, layers, tags, palettes and selections; export frames, tags, layers,
sprite sheets and metadata; recolour explicit palette mappings; normalise
animation timing; crop transparent borders; remove or merge layers; and run
Lua templates or raw Lua scripts.

Lua is optional automation, not part of the normal asset workflow. Use the
Aseprite Slice tool for manually curated named regions, then export slice
metadata when exact bounds are needed by Godot or future asset extraction.

## Godot

Godot AI is the local assembly and verification system. It can edit and
inspect scenes, nodes, scripts, shaders, resources, TileMaps, animations,
AnimationTrees, physics, navigation, particles, audio, themes, cameras,
input actions, project settings and export settings.

It can also search references, inspect errors and logs, run scenes, simulate
input, capture and compare screenshots, run tests, inspect performance, export
the project and deploy to Android.

Godot is the composition workbench for room development. Most static assets
should remain on their original sheets:

- use a 16×16 TileSet atlas for floors, walls and grid-native tiles;
- use Sprite2D regions or scenes for coherent multi-cell furniture;
- use separate PNG/.aseprite assets only for animated, interactive or
  independently reusable props;
- keep collision and interaction logic in Godot scenes.

## Governance

The authority order is:

1. real photos and likeness references for real animals;
2. [`../art/ART_BIBLE.md`](../art/ART_BIBLE.md) for dimensions, perspective, palette and style;
3. approved game-ready assets plus recorded source/recipe for production truth;
4. [`../art/ART_PRODUCTION_PIPELINE.md`](../art/ART_PRODUCTION_PIPELINE.md) for lifecycle and handoff;
5. MCP schemas and server limits for technical capability;
6. human review for promotion to approved content.

The normal asset flow is:

```text
input → relevant-sheet selection → palette remap → wip
→ Aseprite named slices + metadata where needed
→ Godot atlas/region composition → runtime screenshot/test
→ approved complete asset package (art + resources + scenes)
```

Aseprite cleanup/slices/metadata are inserted only where they add value:
identity art, animation repair, palette/silhouette correction, or a reusable
object whose exact bounds need curation.

Raw generated and third-party candidates stay in `input/`. Palette-remapped
room materials and active composition live in `wip/`. During active room work,
Godot may reference WIP textures. Promotion happens only after the room is
accepted. Authoritative accepted assets live in `approved/`, while Godot
resources and scenes live alongside the art in the owning family's WIP or
Approved package. A `.tres` is a saved Godot Resource; a `.tscn` is an assembled
Scene. There is no separate `composite/` lifecycle stage.

For a reusable or complex object, curated Aseprite slice metadata is the
coordinate authority. For a simple 16×16 interactable or directly generated
meta-tile, Godot's explicit region and interaction/collision definitions are
sufficient. AI should consume the established bounds rather than estimate
them from screenshots.
