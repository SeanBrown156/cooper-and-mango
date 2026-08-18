# MCP setup, capabilities and governance

This document combines the project MCP setup notes with the capabilities and
operating rules for the PixelLab, Aseprite and Godot MCP servers.

## Setup

Project-owned MCP definitions live in `.mcp.json` for Claude Code and
`.codex/config.toml` for Codex. Keep credentials out of both files.

Export the PixelLab token before starting a client:

```sh
export PIXELLAB_API_TOKEN="..."
```

PixelLab is remote. Claude Code connects over HTTP; Codex uses the
`mcp-remote` bridge because its local MCP transport is stdio.

Godot MCP is local-only and requires the Godot editor running with this
project open and the plugin enabled. The editor bridge listens on port 6505.

Aseprite MCP is launched with `npx` and requires Aseprite installed locally.
The current executable is configured as:

```text
/Applications/Aseprite.app/Contents/MacOS/aseprite
```

Restart Claude Code or Codex after changing MCP configuration or environment
variables. Codex must trust the workspace before loading `.codex/config.toml`.

## PixelLab

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

Godot MCP is the local assembly and verification system. It can edit and
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
3. approved `.aseprite` files for production truth;
4. [`../art/ART_PRODUCTION_PIPELINE.md`](../art/ART_PRODUCTION_PIPELINE.md) for lifecycle and handoff;
5. MCP schemas and server limits for technical capability;
6. human review for promotion to approved content.

The normal asset flow is:

```text
reference packet → PixelLab generation or selected licensed asset → wip
→ Godot atlas/region composition → runtime screenshot/test
→ approved assets + composite resources

Aseprite cleanup/slices/metadata are inserted only where they add value:
identity art, animation repair, palette/silhouette correction, or a reusable
object whose exact bounds need curation.
```

Raw generated and third-party candidates stay in `input/`. Palette-remapped
room materials and active composition live in `wip/`. During active room work,
Godot may reference WIP textures. Promotion happens only after the room is
accepted. Authoritative accepted assets live in `approved/`, while Godot
composition resources live in the family's `composite/` folder.

For a reusable or complex object, curated Aseprite slice metadata is the
coordinate authority. For a simple 16×16 interactable or directly generated
meta-tile, Godot's explicit region and interaction/collision definitions are
sufficient. AI should consume the established bounds rather than estimate
them from screenshots.
