---
name: cm-openai-battle-sprite-sheet
description: Generate a consistent provisional pixel-art battle sprite sheet with explicit standing or seated two-legged poses, melee actions, and reactions from character references.
---

# CM OpenAI Battle Sprite Sheet

Use this for battle-only generation or for extracting/refining the battle
region of a character-wide master sheet.

1. Read `CHARACTER_VISUAL_BRIEF.md`, the character contract, art bible, all relevant references, and the
   existing master sheet if one exists.
2. Prefer the master sheet as the likeness source. Keep a consistent baseline,
   silhouette, scale, face, signature accessory, and prop language.
3. Require a substantial bipedal battle set when the character's battle design
   calls for it: standing on two legs, seated upright, guard, attack wind-up,
   attack follow-through, hit, stagger, victory, and exhausted poses. Do not
   let the model collapse every cell into a quadrupedal pet pose.
4. Include character-specific melee concepts where requested, such as biting,
   gnawing, a leash or tether used as a lasso, and toy-like sword or knuckle
   props. Keep props playful and readable, never realistic weapons.
5. Require hard-edged square pixel clusters, limited palette, no antialiasing,
   blur, photorealism, painterly gradients, text, labels, UI, or presentation
   board layout.
6. Save the provisional result under `assets/characters/<character>/battle/02_input/`.
   Never overwrite an existing candidate; use a versioned name.
7. Send selected static battle candidates through
   `$cm-prepare-role-resolution` for the governed **32×32** target before
   PixelLab refinement or animation. Do not normalize, recolour, or promote to
   WIP in this skill.

The output is a battle input sheet for later extraction and cleanup, not final
SpriteFrames.
