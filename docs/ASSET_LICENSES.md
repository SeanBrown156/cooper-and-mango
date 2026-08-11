# Third-Party Asset Licenses

Tracks every non-bespoke asset used in the game — required hygiene before a commercial Steam release. Bespoke assets (Mango, Cooper, and any character based on a real pet/friend, generated via PixelLab from our own reference photos) don't need an entry here; this file is for things we didn't make ourselves.

Rule: an asset only gets added to `assets/` after its license is checked and recorded here — not after the fact.

## Environment Tiles

| Asset | Source | Author | License | Commercial use? | Attribution required? | Local path |
|---|---|---|---|---|---|---|
| Free CC0 Top Down Tileset Template Pixel Art | [itch.io](https://rgsdev.itch.io/free-cc0-top-down-tileset-template-pixel-art) | Raphael Gonçalves (RGS_Dev) | CC0 1.0 Universal | Yes, unrestricted | No | `assets/environments/thirdparty/rgsdev_cc0_topdown_template/` |
| Pixel Interior – Cozy 16x16 Living Room & Kitchen Top Down Tileset v1.1 | [itch.io](https://bitglow.itch.io/pixelinterior-livingroomkitchen) | Bitglow | Bitglow Asset License (bundled `license.txt`) | Yes; modification permitted | No; credit appreciated | `assets/environments/thirdparty/bitglow_pixelinterior_lrk_v1_1/` |

**Note on this pack:** 16×16 tiles (our locked tile spec is 32×32 — needs 2× nearest-neighbour upscale on import, not a redraw). Dungeon-template style (walls/floor/door/chest/decorative props, 5 colour variations) — used as prototyping/greybox primitives for the Empty House chapter, not final art. Swap for a purpose-made "cozy apartment" set later if the dungeon aesthetic doesn't read as domestic enough once tiled out.

**Note on the Bitglow pack:** 16×16 top-down interior art (use at 2× nearest-neighbour scale against the project's 32×32 environment grid). It provides floors, walls, doors, windows, stairs, cabinets, kitchen props, decorations, and living-room furniture, so it is the preferred coherent source for the Tutorial Room prototype. The custom license allows use and modification in commercial projects but forbids standalone redistribution, resale, inclusion in another asset/resource pack, or sharing outside the project team.

## Audio

_None yet._

## Fonts

_None yet._

## Adding a new entry

Before adding any third-party asset:
1. Read the actual license text on the source page — don't trust a title or tag alone ("free" ≠ CC0; some require attribution or restrict commercial use)
2. Confirm it's usable in a commercial, Steam-distributed game
3. Add a row here with the source URL, author, exact license, and where it lives in `assets/`
4. If attribution is required, also add it to the in-game credits (not yet built — flag when it becomes relevant)
