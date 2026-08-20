---
name: cm-python-simple-pixel-animation
description: Create simple deterministic integer-pixel loops from approved or canonical PNG anchors for breathing, bobbing, blinking, tail flicks, ear movement, and small prop motion.
---

# CM Python Simple Pixel Animation

Use procedural pixel motion after a selected static anchor has passed
`$cm-prepare-role-resolution`, when the action is simple enough that a model
would introduce unnecessary identity drift. This is complementary to PixelLab,
not a replacement for complex locomotion.

Run:

```sh
python3 tools/shared/python_pixel_animation.py anchor.png output/ \
  --mode breathe --frames 4
```

Supported modes are `breathe`, `bob`, and `sway`. The script uses integer-pixel
offsets, transparent compositing, and no interpolation. Review the loop at
native 1× scale, then keep it in WIP until the loop, dimensions, baseline and
scene behavior are reviewed. Promote only the complete tested package.
