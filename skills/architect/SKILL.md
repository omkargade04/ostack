---
name: architect
description: "Sketch types, signatures, and module structure before code, from two distinct Opus sketches plus one Sonnet sketch, then stop for a go. Use for /architect, 'architect this', 'design this', or a contract change or cross-module change where jumping to code would lock in the wrong shape."
disable-model-invocation: true
---

# Architect

Adapted from pstack `architect` (MIT). Sketch types, function signatures, class shapes, and module boundaries with `NotImplementedError` bodies and pseudocode. Compare several sketches, pick one, and stop. Code starts only after the user's go.

## When it runs

- On demand, at any time.
- In the feature playbook, between SCOPE and PLAN, only for a contract change or a change across modules or repos (the CLAUDE.md "large" list). The chosen sketch feeds the PLAN.

## Start

Open a todo list with one entry per phase: Ground, Sketch, Stop, Implement, Scrap.

## Phase A: Ground the problem

Build a real mental model of every system that the new code touches. Run `how` over the relevant subsystems (`~/Desktop/Work/ostack/skills/how/SKILL.md`). Naming a file is not grounding. If the design redefines ownership or layering, also run `why` on the existing shape (`~/Desktop/Work/ostack/skills/why/SKILL.md`), so that the rationale becomes a constraint, not a guess.

Skip Phase A only when the work is greenfield with no surrounding system.

## Phase B: Sketch

Design it at least twice. Whole-shape alternatives, not point fixes inside one shape.

1. In this session (Opus), write two structurally distinct candidates. Follow `references/runner-prompt.md` for each.
2. In parallel, spawn one `Agent` (`subagent_type: "general-purpose"`, Sonnet) with `references/runner-prompt.md`, the task, and the Phase A grounding. It writes a third candidate into its own scratch directory. It does not see your two.
3. Screen every candidate against `references/design-red-flags.md`. Assume the next contributor is an agent that sees only the files it opened, copies the nearest example, and takes the shortest path that compiles. Prefer the design where a change that looks right from one file is right for the whole repo.
4. Compare viable candidates on interface depth. Prefer the design that hides more complexity behind a smaller, simpler public surface.
5. Pick a base. Graft what is better from the others. Record which candidate won, what came from each of the others, and what was rejected and why. That record fills the rationale's "Synthesis decision" section.

## Phase C: Stop

Always stop here. Show the chosen sketch and the rationale (`references/rationale-template.md`), and wait for the user's go. Write both to the effort dir (`SKETCH - <topic>.md`). If the user pushes back on the shape, treat that as Phase A evidence: re-ground and redo Phase B.

## Phase D: Implement against the sketch (after the go)

Replace `NotImplementedError` bodies with code and pseudocode with logic. The sketch is the contract. A deviation is a signal to surface, not friction to absorb. If a function needs a parameter that the sketch did not expect, ask whether the sketch was wrong, the requirement was missed, or the implementation overreaches.

## Phase E: Scrap when the architecture is wrong

If implementation keeps producing friction that the sketch cannot absorb, throw the sketch out. Do not bolt fixes onto a wrong design.

The signal is a pattern, not one instance:

- The same shape of workaround appears across unrelated code.
- Several unrelated edge cases each need a special-case branch.
- Types need escape hatches (`Any`, casts, optional fields that are always set) to type-check.
- The "we need a lock" reflex when the sketch said that the state was not shared.
- Callers must know the abstraction's internal rules to use it.
- Two or more independent Phase D deviations of the same shape.

When you scrap:

1. Run `how` over what was built.
2. Redesign as if the new constraints had been day-one assumptions.
3. Subtract before you add. The new sketch is smaller than the old one before it grows.
4. Return to Phase B.

## Outputs

The caller's usage is written first, and the type sketch is derived from it. One file with new types and signatures for small changes. A module map plus type definitions for larger work. The rationale ships beside it, shaped per `references/rationale-template.md`.
