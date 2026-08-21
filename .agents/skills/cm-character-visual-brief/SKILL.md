---
name: cm-character-visual-brief
description: Create or update a character visual brief from project canon, references, existing assets, and current user direction.
---

# CM Character Visual Brief

Maintain `assets/characters/<character>/CHARACTER_VISUAL_BRIEF.md` as the
character's living art-facing identity document.

The brief is not a replacement for `docs/vision/GAME_BIBLE.md`. The Game Bible
remains the authority for story canon, relationships and personality. The
brief translates that canon into production-relevant visual guidance and
records current user direction without silently promoting it to canon.

## Workflow

1. Read `GAME_BIBLE.md`, `ART_BIBLE.md`, the character's references, manifests,
   WIP/approved assets and the user's current instructions.
2. Create or update the character-root `CHARACTER_VISUAL_BRIEF.md`. Do not
   create role-specific copies.
3. Separate information into:
   - **Canonical:** confirmed Game Bible, approved assets and explicit decisions;
   - **Current direction:** user-provided guidance for current/upcoming work;
   - **Open question:** unresolved interpretation requiring confirmation;
   - **Superseded:** retained history that must not guide new generation.
4. Preserve user intent and wording when recording current direction. Do not
   invent biography, relationships, powers, markings or personality changes.
   If direction conflicts with canon, record the conflict as an open question
   and ask before changing canonical sections.
5. Convert the brief into generation constraints: likeness, markings,
   silhouette, role posture, signature props, expression cues, animation
   invariants, prohibited drift, references and approved anchors.
6. Cross-reference the Game Bible instead of copying large narrative passages.
   Record that a future structured/global character system may become the
   shared authority for dialogue, personality and art generation; do not
   migrate to it without a later project decision.
7. Update manifests or prompt metadata only when a confirmed brief change
   affects a generation constraint, and record the change source.

## Required brief headings

Every brief should contain these headings, even when a section says `Unknown`
or `Not yet decided`:

- Authority and open questions
- Identity and likeness
- Personality and behaviour cues
- Art direction
- Role-specific visual grammar
- Signature items and props
- Animation invariants
- Reference map
- Approved anchors
- Production notes

## Boundaries

Do not use this skill to generate sprites, decide global palette/dimensions/
perspective, rewrite the Game Bible without explicit direction, promote assets,
or replace role-specific generation and normalization skills.
