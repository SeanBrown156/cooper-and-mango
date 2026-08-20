# Generation prompt

- Provider: OpenAI
- Model: `gpt-image-2`
- Mode: `edit`
- Size: `1536x1024`
- Quality: `high`
- Background: `opaque`
- Metadata: [mango_overworld_reference_pixel_sheet_v1.png.json](mango_overworld_reference_pixel_sheet_v1.png.json)

## Prompt

Use case: stylized-concept
Asset type: provisional pixel-art quadruped overworld sprite master sheet
Primary request: Create one clean overworld-only master sprite sheet on one canvas. Do not create separate images or a presentation board. Use an evenly spaced grid with many complete candidate sprites. Include north/back, south/front, east/right and west/left directions, with idle, contact, passing, opposite-contact and bob phases for each direction. Include three clearly separated outfit groups: hoodie-up, hoodie-down, and no hoodie worn whatsoever. Hoodie-down is the normal default; hoodie-up and no-hoodie are intentional gameplay variants because Mango interacts with the hoodie. Leave generous blank spacing around every cell for later manual selection and slicing. Do not render labels, captions, numbers, borders, text or UI; a separate script adds review numbers.

Critical overworld grammar: Mango must be a quadruped animal on all fours in every cell, with four-leg locomotion and a consistent ground contact baseline. Never use bipedal, upright, standing-on-two-legs or battle poses. Keep the body low and readable in low top-down orthographic view. Show front/south, back/north, right/east and left/west views, not only rear views.

Character identity: use the supplied clean Mango master sheet as the primary likeness reference. Mango is an orange tabby cat, fluffy and chubby but cute rather than babyish, with correct orange tiger stripes, triangular ears, tail, half-open grumpy/aloof eyes where visible, and a purple hoodie. In hoodie-down cells the hoodie is draped around the neck/back without covering the head. In hoodie-up cells the purple hood covers the head while the ears visibly emerge. In no-hoodie cells there must be no purple hoodie garment at all: show the orange tabby fur and body unobstructed. Preserve identical face, stripe placement, silhouette, palette, proportions, tail and outfit logic across all cells.

Style: crisp 16-bit pixel art, hard square pixel clusters, limited coherent palette, solid opaque pure-white background, clean crisp edges, no antialiasing, blur, painterly gradients, photorealism, soft shading or scenery.
Avoid: bipedal or upright poses, battle staging, generic cats, changed proportions, inconsistent stripes, hood covering every cell, purple fabric appearing in the no-hoodie group, transparent/checkerboard/black/coloured backgrounds, isometric projection, perspective, horizon lines, scenery, decorative layout, labels, numbers and text.
