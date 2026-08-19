---
name: cm-pixellab-props
description: Create Cooper & Mango top-down props, interactables, and animated object candidates with correct orientation, bounds, and scene/resource handoff.
---

# CM PixelLab Props

Use for furniture, doors, chests, plants, pickups, animated props and other
independently reusable objects. Static decorative tiles usually do not need a
scene.

- Props use a 2D orthographic top-down world, 16×16 grid and hard pixel edges.
  Describe footprint, floor contact, visible bounds, orientation and draw order;
  keep transparent backgrounds and no external cast shadows.
- Use `create_map_object` for a one-view top-down prop or style-matched/inpaint
  result. Basic mode needs width/height; style matching needs a base64 image and
  optional mask. Poll with `get_map_object`/`get_object` as supported.
- Use `create_1_direction_object` when its candidate-review workflow helps:
  inspect review candidates with `get_object`, then explicitly select/dismiss.
- Use `create_8_direction_object` only for genuinely rotatable non-humanoid
  props. Never use it for Mango, Cooper or any character; identity transfer is
  unreliable. Use `$cm-pixellab-characters` for characters.
- For motion, use `animate_object` for a PixelLab object or `animate_image` for
  a loose PNG. Choose 4 frames for simple idle and 8 for more involved motion;
  poll with `get_image`/`get_object`.

Raw downloads start in `input/`. Once cropped, cleaned or wired, keep the whole
working package in the owning family's `wip/` including `.aseprite`, `.png`,
metadata, resource `.tres` and behavior scene `.tscn`. Promote only after
Godot collision, interaction, sorting, animation and native-scale checks pass.
Record object/job IDs, references, canvas size, footprint and review outcome.
