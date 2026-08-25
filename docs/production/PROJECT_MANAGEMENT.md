# Project Management Convention

Cooper & Mango tracks work with GitHub Issues, Milestones, Labels and
Assignees. GitHub Projects (v2) are **not** part of this workflow — see
[Why not Projects](#why-not-projects) below.

## The hierarchy

```text
Milestone →  the build stage from PRODUCTION_ROADMAP.md
Issue     →  concrete task — this is where completion happiness lives
Type      →  discipline doing the work (a label)
Kind      →  nature of the work item (a label)
Assignee  →  who is doing it — Sean or Lillian
```

## Milestones are the build stages

A Milestone corresponds directly to a stage in
[`PRODUCTION_ROADMAP.md`](PRODUCTION_ROADMAP.md):

- `Stage 0 — Toy`
- `Stage 1 — Mango's Room`
- `Stage 1 — Cooper's Room`
- `Stage 2 — House`
- `Stage 3 — Neighbourhood`
- `Stage 4 — Open World`

Stage 1 is split into two milestones — Mango's and Cooper's — because
[`VERTICAL_SLICE.md`](VERTICAL_SLICE.md) requires both starting choices to be
independently playable, and issues (art, greybox, sprite work) genuinely
belong to one path or the other. Everything else stays one milestone per
stage. Issues that are cross-cutting systems or infrastructure (core
mechanics, tooling, pipeline docs, licensing) and aren't bound to a single
stage are left unmilestoned rather than forced into one.

Milestones are deliberately not the "small win" tier any more — a stage can
run for weeks and contain dozens of issues. That's fine: **issue completion
is now where the frequent, motivating win lives**, not milestone completion.
Closing a milestone marks reaching the stage's exit criteria from
`PRODUCTION_ROADMAP.md`, playable in the running game.

## Issues are the work items, and the reward unit

Issues describe one concrete task or a small coherent bundle of tasks.
Closing an issue is the small, frequent bit of completion happiness — it
should represent a real shipped deliverable (a sprite imported, a bug fixed,
a system wired up), not a rubber-stamp checkbox.

## Type: discipline

`type:*` labels describe which discipline the work belongs to, matching the
Ownership Model in [`docs/README.md`](../README.md):

- `type:art`
- `type:audio`
- `type:design`
- `type:engineering`
- `type:writing`
- `type:production`

## Kind: nature of the work

`kind:*` labels describe what the item actually is, independent of
discipline:

- `kind:asset`
- `kind:documentation`
- `kind:bug`
- `kind:feature`
- `kind:polish`
- `kind:blocked`

A sprite export is `type:art` + `kind:asset`. A movement bug is
`type:engineering` + `kind:bug`. A licensing task is `type:production` +
`kind:feature`.

## Assignee: allocating work between Sean and Lillian

Use GitHub's native Assignee field — this is the actual allocation
mechanism, not a label. As a rough default: art/audio/writing work goes to
Lillian, engineering/tooling/production work goes to Sean, but reassign
freely when either of you picks something up.

## Practical example

```text
Milestone: Stage 1 — Mango's Room
Issue:     Export the four walk cycles into Godot SpriteFrames
Type:      type:art
Kind:      kind:asset
Assignee:  lillianlixinwang-dev
```

```text
Milestone: (none — cross-cutting)
Issue:     Fix PixelLab MCP auth token refresh
Type:      type:engineering
Kind:      kind:bug
Assignee:  SeanBrown156
```

## Getting a project-like view without Projects

A saved issue search/filter (for example `milestone:"Stage 2 — House"` or
`label:"type:engineering" label:"kind:bug"`) is a live, always-current board.
Because it's just filtering repo-native issues, any repo collaborator sees
it automatically — unlike Projects (see below).

## Why not Projects

GitHub Projects (v2) owned by a personal user account (as opposed to an
organisation) have their own separate access list, distinct from repo
collaborator access. A collaborator with `write` access to this repo is not
automatically granted access to a Project owned by the repo owner's personal
account — the Project has to be made public or the collaborator invited to
it individually, on top of their repo access. This is why the six Projects
previously used for this repo (`00_Tooling`, `00_Title Screen`, `01_Mango's
Tutorial Room`, `01_Cooper's Tutorial Room`, `02_The House`, `00_Items,
Stats & Battle Mechanics`) were not visible to Lillian despite her having
write access to the repo itself. Those boards were also mixing two
different concerns — some were places (a room) and some were cross-cutting
systems (tooling, battle mechanics) — which `type:*`/`kind:*` now resolves
without needing a separate container object.

The six boards have been left in place, unused, rather than deleted. If a
visual kanban is wanted later, a Project grouped by Milestone is the
suggested approach — but only once its visibility is fixed (made public, or
Lillian explicitly added as a project collaborator).
