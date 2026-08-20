# Generation prompt

- Provider: OpenAI
- Model: `gpt-image-2`
- Mode: `edit`
- Size: `1536x1024`
- Quality: `high`
- Background: `opaque`
- Metadata: [mango_master_reference_pixel_sheet_v1.png.json](mango_master_reference_pixel_sheet_v1.png.json)

## Prompt

Use case: stylized-concept
Asset type: one provisional pixel-art character master sprite sheet for a game
Primary request: Create ONE giant clean master sprite sheet on one canvas. Do not create separate sheets or a presentation board. Divide the canvas into three clearly separated unlabelled regions using generous blank spacing: PORTRAIT, BATTLE, and OVERWORLD. Each region must contain a regular grid of many complete candidate sprites, all derived from the same Mango character design so likeness, palette, stripe placement and proportions remain consistent across the entire canvas. Leave enough blank space around every cell for deterministic later slicing. Do not render labels, captions, numbers, borders, text or UI; a separate script will add review numbers.

PORTRAIT region: consistent head-and-shoulders portraits with identical framing and scale. Include hoodie-down default portraits and a smaller set of hoodie-up variants. Include neutral, sleepy, unimpressed, worried, shocked, sad, embarrassed, angry, frustrated, determined, defiant, brave, relieved, proud, smug, curious, playful and gentle expressions.

BATTLE region: mostly bipedal standing or seated-upright sprites on two legs, not quadrupedal pet poses. Include neutral guard, crouched guard, bite/gnaw attack, leash-as-lasso attack, toy-wand attack, wind-up, follow-through, hit, stagger, exhausted, victory, shocked and determined/defiant poses. Purple hoodie down is the default; include a few hood-up variants. Keep props playful and readable, especially the toy-like wand/teaser, leash and toy weapons.

OVERWORLD region: small low-top-down orthographic quadrupedal sprites with a consistent footprint and baseline. Include north/back, south/front, east/right and west/left, with idle, contact, passing, opposite-contact and bob phases. Include both hoodie-down and hood-up outfit states, with hoodie-down as the default. Keep the hood-up state clearly distinct because the character interacts with the hoodie in the game.

Character invariants: Mango is an orange tabby cat, fluffy and chubby but cute rather than babyish, with half-open grumpy/aloof eyes, correct orange tiger stripes on forehead and cheeks, triangular ears, expressive demure face, and a purple hoodie. The hood should not cover the head in the default portrait or battle designs. Preserve identical identity across every cell. The character should feel judgemental, blasé and mildly arrogant, but warm underneath; expressions can show bravery and defiance.

Style: crisp 16-bit pixel art, hard square pixel clusters, limited coherent palette, clean crisp edges, transparent or flat neutral background, no antialiasing, blur, painterly gradients, photorealism, soft shading or decorative layout.
Avoid: generic cats, wrong stripe pattern, hood covering every cell, inconsistent face scale, quadrupedal-only battle poses, bipedal battle poses in the overworld region, scenery, isometric projection, perspective staging, random costumes, realistic weapons, text, labels, numbers, UI and presentation-board decoration.
