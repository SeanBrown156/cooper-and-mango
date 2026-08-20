---
name: cm-openai-anchor-frame
description: Create one canonical static Cooper & Mango character, prop, or environment sprite with OpenAI Image; use when later pose, animation, PixelLab, or Aseprite work needs one stable visual reference.
---

# CM OpenAI Anchor Frame

This skill creates exactly one strong static reference image. It does not create
an animation, spritesheet, inventory, or Godot scene. Its output is the visual
anchor that other skills can reference.

## Workflow

1. Read the owning package contract, available references and, for characters,
   `CHARACTER_VISUAL_BRIEF.md` directly.
2. Assemble labelled inspiration, likeness, composition, palette, and approved
   references. Do not treat generic generated art as canon.
3. Prompt one clear static pose with transparent background where supported,
   restrained pixel clusters, and explicit target use.
4. Generate at a controllable working resolution using
   `tools/openai/image_generate.py`.
5. For a character role, pass the selected result through
   `$cm-prepare-role-resolution` rather than inventing a one-off resize. The
   governed targets are overworld 20×16, battle 32×32, and portrait 40×40.
   Validate the target size and palette, and save raw/prepared outputs in the
   package `input/`/`02_input/` area.
6. Record the anchor prompt, references, model, dimensions, and review state in
   the local manifest.

The anchor becomes a reference candidate for PixelLab, Image edits, video
motion, procedural animation, and manual cleanup. It is not approved until
reviewed at native 1× scale and in Godot.
