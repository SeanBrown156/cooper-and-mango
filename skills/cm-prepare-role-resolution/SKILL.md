---
name: cm-prepare-role-resolution
description: Prepare selected portrait, battle, or overworld sprite cells at the governed Cooper & Mango production resolution with nearest-neighbour scaling, preserved aspect ratio, and landmark review before PixelLab or animation.
---

# CM Prepare Role Resolution

This is the resolution gate between selected master cells and refinement.

## Governed targets

- Overworld: **20×16**, quadruped, four orthogonal directions.
- Battle: **32×32**, upright/bipedal presentation where required.
- Portrait: **40×40**, expressive portrait/bust.

## Workflow

1. Accept only a user-selected cell from the numbered master review. Never
   process an entire master sheet or unselected candidates.
2. Read the owning manifest and confirm the role target matches the contract.
3. Run `tools/shared/prepare_role_resolution.py` for the selected cell. It
   removes the edge-connected generated background, converts the candidate to
   transparency, then uses nearest-neighbour resampling and aspect-preserving
   containment. It must not stretch a character to fill a target canvas. Use
   `--keep-background` only when the source background is intentionally part of
   the asset.
4. Inspect the transparent target-size result at native 1×. Confirm head/face placement,
   feet or baseline, body height, pivot, silhouette, tail/ears, signature
   accessory, and any weapon/effect bounds.
5. If the source aspect ratio or pose cannot survive the target, stop for
   manual redraw or a role-specific OpenAI/PixelLab regeneration. Do not hide
   the problem with independent per-frame scaling. Check for leftover halos,
   shadows, or clipped fur around the transparent silhouette.
6. Put the prepared candidate in the role's `02_input/` staging folder. Send
   only this selected, prepared candidate to PixelLab with high reference
   influence where the provider supports it.
7. After refinement or animation, run `$cm-normalize-animation-frames` for
   frame-level baseline/pivot validation before WIP approval and Godot scenes.

This skill prepares a source candidate; it does not animate, recolour, promote,
or create Godot resources.
