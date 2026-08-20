# Mango Character Visual Brief

## Authority and open questions

- Story and personality canon: [`docs/vision/GAME_BIBLE.md`](../../../docs/vision/GAME_BIBLE.md).
- Global visual rules: [`docs/art/ART_BIBLE.md`](../../../docs/art/ART_BIBLE.md).
- Production workflow: [`docs/art/ART_PRODUCTION_PIPELINE.md`](../../../docs/art/ART_PRODUCTION_PIPELINE.md).
- This brief translates canon into art-facing constraints; it does not replace the Game Bible.
- A future shared character data layer may own dialogue/personality and visual generation together. Until that decision is made, keep narrative canon in the Game Bible and art-facing interpretation here.

## Identity and likeness

- Orange cat.
- Young/cute proportions without becoming babyish.
- Fluffy and chubby.
- Check exact eye colour and fur markings against real reference photos.

## Personality and behaviour cues

- Aloof, judgemental, blasé and mildly arrogant.
- Still warm and friendly underneath the guarded exterior.
- The survival-to-love arc should inform expression, posture and animation; the Game Bible remains the narrative authority.

## Art direction

- Purple hoodie, not a grand wizard robe.
- Orange ears visibly emerge from the hood.
- Readable silhouette and strong personality at native scale.

## Role-specific visual grammar

- Overworld: 20×16, quadruped/on all fours, hoodie draped over the back, silhouette first.
- Battle: 32×32, upright/bipedal mage pose, chubby and fluffy, 3/4 combat stance.
- Portrait: 40×40, expressive upright likeness with face, fluff, markings and hoodie detail.

## Signature items and props

- Black cat-teaser rod/fishing-rod-like toy with a simple bird or feather flutterer.
- It is a toy-like wand, not a conventional fantasy staff.

## Animation invariants

- Preserve orange fur, ears, hoodie, tail and wand identity across frames.
- Keep the judgemental/blasé attitude readable during action.
- Do not turn the overworld quadruped grammar into the battle/portrait bipedal grammar.

## Reference map

- Real likeness references: the reference folders under `assets/characters/mango/`.
- Exploratory Gemini sheets are superseded style references, not production truth.

## Approved anchors

No approved anchor is recorded yet.

## Production notes

Use `$cm-character-visual-brief` before new reference synthesis or a major
character visual change. Route selected assets through the master-sheet,
resolution, refinement, animation and normalization skills in the Pipeline.
