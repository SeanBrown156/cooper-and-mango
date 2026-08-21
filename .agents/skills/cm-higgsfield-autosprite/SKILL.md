---
name: cm-higgsfield-autosprite
description: Generate a reference-guided provisional character spritesheet with Higgs Field AutoSprite; use for quick idle, walk, run, attack, jump, custom, or isometric motion experiments from a canonical anchor before normalization and Godot integration.
---

# CM Higgs Field AutoSprite

Use Higgs Field’s `autosprite` model as a complementary motion pathway. It is
especially useful when a stable character anchor exists and we want a fast
spritesheet experiment to compare with PixelLab, OpenAI Image, or video-derived
animation.

## Workflow

1. Read the owning character package and select the canonical anchor. Prefer an
   approved or deliberately chosen WIP anchor; do not use an arbitrary photo
   as the only generation reference.
2. Confirm the requested action and role contract. Choose one of `idle`,
   `walk`, `run`, `attack`, `jump`, `custom`, or an explicitly supported
   isometric preset. Do not use isometric presets for the orthographic
   overworld unless the user is intentionally exploring a different pathway.
3. Upload the local anchor through the Higgs Field media upload tool, or use a
   completed Higgs image job already available in the workspace. Keep the
   returned media ID and source path together.
4. Before spending credits, inspect the model/cost information. Submit
   `mcp__codex_apps__higgsfield_generate_image` with:
   `model="autosprite"`, one image reference, an explicit action kind, a
   conservative frame count, the requested working frame size, and
   `is_humanoid` set correctly. Use silent output unless sound is explicitly
   wanted for a motion study.
5. Wait for the job to complete. Preserve the job ID, raw result URL, atlas
   metadata, requested parameters, and any provider adjustments.
6. Save the raw sheet and metadata in the owning package’s `02_input/` area.
   Do not put the provider result directly into `03_wip/` or `04_approved/`.
7. Inspect the sheet at native scale. Higgs may return a useful sheet while
   still changing frame count, cell boundaries, body scale, palette, or
   transparency. Extract intended frames and run
   `$cm-normalize-animation-frames` before any Godot integration.
8. Compare the normalized result against the anchor and other complementary
   pathways. Record the outcome in the local package manifest; never claim the
   provider’s “game-ready” label as project approval.

## Guardrails

- AutoSprite is a motion and sheet generator, not a likeness authority.
- Do not create a Higgs reusable reference element until the anchor is stable;
  if one is created, record its ID and source image in the local manifest.
- Do not silently choose between free/unlimited allowance and credits when the
  Higgs tool asks for that choice.
- Preserve the raw output. Normalization, palette work, recolouring, and
  promotion are separate decisions.
