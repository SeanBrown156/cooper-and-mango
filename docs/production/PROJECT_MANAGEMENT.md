# Project Management Convention

Cooper & Mango uses GitHub Projects, Milestones, Issues and Labels at
different levels of the game-making hierarchy. The aim is to make progress
visible, motivating and easy to navigate.

## The hierarchy

```text
Project   →  major game area
Milestone →  small, rewarding playable capability
Issue     →  concrete task needed to reach the milestone
Label     →  cross-cutting description of the work
```

## Projects are the large areas

Projects should represent durable parts of the game that will contain many
milestones over time. Examples include:

- Mango's Tutorial Room
- Cooper's Tutorial Room
- The House
- Title Screen
- Items, Stats & Battle Mechanics
- Tooling

An issue should normally have one primary project. Project items move through
the board workflow, usually `Todo → In Progress → Done`.

Do not create a new project for every feature or small task. Projects are the
large containers that remain useful throughout development.

## Milestones are small victories

A milestone should be a visible, testable capability that feels rewarding to
complete. It should be possible to finish one milestone in a short focused
work period and demonstrate it in the running game.

Good examples:

- Mango can walk
- Mango can inspect an object
- Mango can trigger the plant awakening
- Mango can leave the room
- Mango meets Cooper
- First playable battle

Milestones are deliberately smaller than chapters, vertical slices or full
projects. A large chapter can contain many milestones. This makes progress
feel like unlocking abilities in the game itself.

## Issues are the work items

Issues should describe one concrete task or a small coherent bundle of tasks.
Several issues can contribute to one milestone. For example, `Mango can walk`
may include sprite cleanup, Godot export, SpriteFrames setup, movement code,
grounding checks and playtesting.

Keep the milestone's acceptance criteria focused on the player-visible
capability, while the issues contain the implementation steps.

## Labels describe dimensions

Labels are reusable tags, not hierarchy. Use them to describe the kind of
work or its current concern, for example:

- `art`
- `godot`
- `tooling`
- `design`
- `writing`
- `audio`
- `bug`
- `enhancement`
- `blocked`

An issue can have several labels. For example, a Mango sprite handoff may be
labelled `art`, `godot` and `enhancement` while belonging to the Mango's
Tutorial Room project and the `Mango can walk` milestone.

## Practical example

```text
Project:   01_Mango's Tutorial Room
Milestone: Mango can walk
Issue:     Export the four walk cycles into Godot SpriteFrames
Labels:    art, godot, enhancement
Status:    Todo
```

## The gamification rule

When choosing the next milestone, prefer the smallest capability that can be
made playable and demonstrated. Finish it, run it, and record the result
before opening a larger milestone. The project should accumulate visible
unlocks rather than only moving toward distant chapter-level goals.

