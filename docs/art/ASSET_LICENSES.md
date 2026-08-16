# Third-Party Asset Licenses

Tracks every non-bespoke asset used in the game — required hygiene before a commercial Steam release. Bespoke assets (Mango, Cooper, and any character based on a real pet/friend, generated via PixelLab from our own reference photos) don't need an entry here; this file is for things we didn't make ourselves.

Rule: an asset only gets added to `assets/` after its license is checked and recorded here — not after the fact.

## Environment Tiles

| Asset | Source | Author | License | Commercial use? | Attribution required? | Local path |
|---|---|---|---|---|---|---|
| Free CC0 Top Down Tileset Template Pixel Art | [itch.io](https://rgsdev.itch.io/free-cc0-top-down-tileset-template-pixel-art) | Raphael Gonçalves (RGS_Dev) | CC0 1.0 Universal | Yes, unrestricted | No | `assets/environments/tutorial_room/reference/rgsdev_cc0_topdown_template/` |
| Pixel Interior – Cozy 16x16 Living Room & Kitchen Top Down Tileset v1.1 | [itch.io](https://bitglow.itch.io/pixelinterior-livingroomkitchen) | Bitglow | Bitglow Asset License (bundled `license.txt`) | Yes; modification permitted | No; credit appreciated | `assets/environments/tutorial_room/approved/thirdparty/bitglow_pixelinterior_lrk_v1_1/` |
| DungeonTileset II | [itch.io](https://0x72.itch.io/dungeontileset-ii) | 0x72 | CC0 (confirmed on itch.io page text at download time: "You can use this tileset for whatever you like (CC-0)"). No license file is bundled in the pack itself — the folder only has a technical `README` (autotile/grid notes), not license terms. | Yes, unrestricted | No | `assets/environments/input/0x72_dungeon_tileset_ii/` |
| 16x16 Industrial Tileset | [itch.io](https://0x72.itch.io/16x16-industrial-tileset) | 0x72 | CC0, same creator/license pattern as DungeonTileset II, confirmed on-page at download time. No bundled license file. | Yes, unrestricted | No | `assets/environments/input/0x72_industrial_tileset/` |
| Super Retro World • Free Interior Pack | [itch.io](https://farm-animal.itch.io/interior-pack) | Gif | Custom license per itch.io page (no license file is bundled in the pack — only `STORE.html`/`DONATE.html` redirect pages were present, both content-free). Per the page: commercial and non-commercial use and modification permitted; redistributing the assets directly (even modified) is prohibited; NFT and AI-training use prohibited; credit requested but not required. **Not independently verified from a file in-pack — flagged below.** | Yes, per page (unverified in-pack) | No, requested | `assets/environments/input/superretroworld_interior_pack/` |
| Modern Exteriors | [itch.io](https://limezu.itch.io/modernexteriors) | LimeZu | Custom license, OCR'd from bundled `Modern_Exteriors_License.pdf` (scanned image, read via `pdftoppm`+`tesseract`): can edit and use the asset in any commercial or non-commercial project, including open-source (e.g. GitHub); can't resell or distribute the asset itself to others, and can't edit-and-resell (including NFT minting); credit required (link to https://limezu.itch.io/). | Yes, with credit | Yes, required | `assets/environments/wip/limezu_modern_exteriors/` |
| Modern Interiors (full/paid version) | [itch.io](https://limezu.itch.io/moderninteriors) | LimeZu | Custom "MODERN INTERIORS FULL VERSION LICENSE" per bundled `LICENSE.txt`: can edit and use the asset in any commercial or non-commercial project; can't resell or distribute the asset (edited or not) to others; credit required (limezu.itch.io). | **Yes**, with credit | Yes, required | `assets/environments/wip/limezu_modern_interiors_full/` |
| Serene Village | itch.io (URL unconfirmed — see note) | LimeZu | **No license file found anywhere in the pack** (checked for `.txt`/`.pdf`/`.md`/`README` — none present). Not verified. | **Unknown — do not use before verifying** | Unknown | `assets/environments/wip/limezu_serene_village/` |

**Note on this pack:** 16×16 tiles — matches our locked tile spec (16×16 world grid, revised 2026-08-12) natively, no upscale needed. Dungeon-template style (walls/floor/door/chest/decorative props, 5 colour variations) — used as prototyping/greybox primitives for the Empty House chapter, not final art. Swap for a purpose-made "cozy apartment" set later if the dungeon aesthetic doesn't read as domestic enough once tiled out.

**Note on the Bitglow pack:** 16×16 top-down interior art — matches the project's 16×16 environment grid natively. It provides floors, walls, doors, windows, stairs, cabinets, kitchen props, decorations, and living-room furniture, so it is the preferred coherent source for the Tutorial Room prototype. The custom license allows use and modification in commercial projects but forbids standalone redistribution, resale, inclusion in another asset/resource pack, or sharing outside the project team.

**Note on the 0x72 DungeonTileset II pack:** Native 16×16 tiles (plus a 16×32 "high" wall variant meant to be drawn on a layer above a 16×16 base, per the bundled README) — matches our grid directly for the 16×16 set. Covers a full dungeon kit: autotiled floors/walls, doors, chests, levers, fountains, plus a large roster of enemy/character sprite sheets (skeletons, zombies, orcs, wizards, etc.) in the `frames/` folder — far more content than we need for environment tiles alone, but harmless to keep since it's CC0. Commercially fine for Steam with no restriction, but the CC0 claim rests on the itch.io page text at download time rather than a bundled license file — worth a quick re-check of the live page before shipping, per our own "don't trust a title alone" rule.

**Note on the 0x72 Industrial Tileset pack:** Only `industrial.v1.png` is actually present — the v2 file referenced on the itch.io page did not save during download, so this pack is currently just the one 16×16-native tilesheet. Same CC0 pattern and creator as DungeonTileset II; same caveat that the claim is page-text-at-download-time rather than a bundled license file. Fine for Steam commercially once re-verified.

**Note on the Super Retro World interior pack:** Ships pre-baked at 16×16, 32×32, and 48×48 in `atlas_*.png`, plus RPG Maker (MV/MZ and VX Ace) and Unity-specific exports we don't need for a Godot project. No license file was actually bundled in the download — the license terms above come from the itch.io page description, not a file we can point to inside `assets/`. This is a materially weaker paper trail than every other pack in this table and should be re-confirmed against the live itch.io page (and ideally saved as a screenshot/PDF into the folder) before any asset from it ships in a commercial build.

**Note on the LimeZu Modern Exteriors pack:** Trimmed to just the 16×16 export (see Part 2 trim below) — native pixel dimensions match our grid exactly, no upscale needed. Broad exterior kit: terrain autotiles, buildings, fences, foliage, water, and a "Character Generator Addons" sheet for building custom NPC outfits. The OCR'd license permits commercial use and modification but prohibits redistributing the raw or lightly-edited asset files themselves (so no re-packaging into a separate downloadable tileset) and requires crediting LimeZu — that credit line needs to land in the in-game/store-page credits before Steam release. A `rpg_maker_mv_export/` subfolder (from a separate `Modern_Exteriors_RPG_Maker_MV_v42.3.zip` download) held the same content in RPG Maker MV's proprietary tile-strip format under the same license — removed in the Part 2 trim since this project is built in Godot, not RPG Maker.

**Note on the LimeZu Modern Interiors (full) pack:** Superseded the free tier on 2026-08-13 — the paid version is now the pack on disk, and its bundled `LICENSE.txt` confirms unrestricted commercial use with credit required. **The Steam-publish blocker tracked below (2026-08-12) is resolved**; this is the pack the Tutorial Room and future interior rooms should build from. Massive pack — 16×16-native, includes a "Room Builder" sheet (matched wall/floor/baseboard/carpet strips organised by colour family, plus door/window/stair pieces) and a `Theme_Sorter` folder of curated per-theme furniture/prop sheets (e.g. `2_LivingRoom_16x16.png`). Credit LimeZu (limezu.itch.io) in the in-game/store-page credits before Steam release — not yet built, flag when it becomes relevant.

**Note on the LimeZu Serene Village pack:** No license file, README, or any text file of any kind was found in this folder — just image exports across several engine-specific formats (RPG Maker MV/VX Ace/XP, Construct 3) plus loose animated GIFs/PNGs (campfire, door, water). The itch.io URL above (`limezu.itch.io/serenevillage`) is LimeZu's standard slug pattern but is **not confirmed from anything inside this folder** — there's no readme to cross-check it against. Per the project's own asset-licensing rule, this pack should be treated as unverified and **not used in `assets/` proper until someone visits the live itch.io page, confirms the URL and license terms, and ideally saves a copy of the license text into this folder.**

## UI

| Asset | Source | Author | License | Commercial use? | Attribution required? | Local path |
|---|---|---|---|---|---|---|
| UI Pack (2.0) | [itch.io](https://kenney-assets.itch.io/ui-pack) | Kenney (Assets) | CC0 1.0 Universal, per bundled `License.txt`: "free to use in personal, educational and commercial projects." | Yes, unrestricted | No; credit appreciated | `assets/ui/input/kenney_ui_pack/` |
| Fantasy UI Borders (1.0) | [itch.io](https://kenney-assets.itch.io/fantasy-ui-borders) | Kenney (Assets) | CC0 1.0 Universal, per bundled `License.txt`: "You can use this content for personal, educational, and commercial purposes." | Yes, unrestricted | No; credit appreciated | `assets/ui/input/kenney_fantasy_ui_borders/` |

**Note on the Kenney packs:** Both are vector-sourced UI kits (PNG + SVG exports, not native pixel-grid art like the environment tiles) — buttons, panels, borders, and icon sets for menus/HUD, plus a couple of UI click/tap sound effects and two bundled fonts (Kenney Future, Kenney Future Narrow) in the UI Pack. CC0 with no restrictions, so both are safe for a commercial Steam release outright; the fonts and sounds bundled inside `kenney_ui_pack/` carry the same CC0 terms per Kenney's blanket license text, but if either gets used, double-check the font's own embedded license metadata before relying on that assumption for anything beyond this project's internal use.

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
