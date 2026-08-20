---
name: cm-openai-video-to-sprite
description: Generate or process a reference-guided motion clip and convert it into normalized Cooper & Mango spritesheets; use for walk, run, locomotion, and complex action timing.
---

# CM OpenAI Video to Sprite

Treat video as a motion source, never as runtime art.

## Workflow

1. Read the owning `CHARACTER_VISUAL_BRIEF.md` and package contract, then select a user-approved, normalized
   static anchor directly. This is a complementary path after PixelLab or when
   PixelLab cannot produce the required motion/size; it is not a reason to
   animate every generated cell.
2. Prepare a reference image matching the provider’s video resolution.
3. Describe one action, direction, camera lock, timing beats, and identity
   invariants. Request a solid opaque pure-white background throughout the
   clip; prohibit transparency, checkerboards, black or coloured backgrounds,
   and background scenery. For walks/runs, explicitly request alternating limb
   contact and a loopable return to the starting pose.
4. Create/poll/download with `tools/openai/video_generate.py`.
5. Extract frames using `tools/shared/video_extract_frames.py`.
6. Run `$cm-normalize-animation-frames` to choose, deduplicate, crop, place, and
   export fixed-size frames.
7. Validate at native 1× and in Godot; retain the MP4 as source evidence and
   the PNG/SpriteFrames as the WIP candidate. Only promote after review and
   testing.

Sora 2 is the current adapter, isolated behind this pathway because its Videos
API has an announced September 24, 2026 shutdown. Replace the adapter without
changing the extraction or normalization workflow.
