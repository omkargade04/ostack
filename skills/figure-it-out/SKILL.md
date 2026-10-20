---
name: figure-it-out
description: "Design an auditable playbook when no ostack playbook fits: a large migration, an ambitious multi-part change, or work Omkar reviews after stepping away. Scales rigor to the task, runs a hypothesis loop, and logs decisions. The grill and GO gates still apply. Use for /figure-it-out or 'figure it out'."
disable-model-invocation: true
---

# Figure it out

Adapted from pstack `figure-it-out` (MIT). When the task matches no ostack playbook (ticket, feature, optimize, review-pr, execute), design one. The deliverable before any code is the workflow itself: phases that scale rigor to the task, run the scientific method, and leave a decision trail that the user can audit after stepping away.

## Start

Open a todo list with the phases below.

## Phase A: Frame

Ground first, then commit. Do not start the run until you can state:

- The definition of done as a falsifiable predicate: the check that would prove the result right or wrong.
- The scope, quantified: rough units and effort, plus the blockers that grounding surfaced.
- The rigor level, biased high. One-way doors and a high blast radius get more. Reversible low-stakes steps get less. Rigor is gates and artifacts, not "try harder".

Then the gates (CLAUDE.md):

1. Present the framing and the tradeoffs.
2. Run `/ostack:grill-me` on the open preferences. Decisions go to `DECISION - <topic>.md` and `_INDEX.md` in the effort dir.
3. Stop for an explicit go before any code. Read-only fact-finding may continue without a go.

## Phase B: Design the workflow

Decompose into atomic, independently landable units. Put the riskiest unknown first. Build the scaffold and the verification before the features.

- Build the verification harness before the work, with the baseline captured from the pre-change state, so each check reads "old value vs new value".
- For a one-way-door design decision, run `/architect` (`~/Desktop/Work/ostack/skills/architect/SKILL.md`). Skip it for mechanical work whose shape is already concrete.
- Decide what fans out. Parallelize only across seams, and give each worker its own worktree or branch. Do not over-fan. Subagents run on Sonnet.
- Write the designed phase list into `PLAN - <topic>.md` in the effort dir, in the `superpowers:writing-plans` format with the ostack overrides (no commit step per task, handoff to `/ostack:mode execute`). That plan is what the user reviews.

Then, after the go, execute the design. Add its steps to the todo list between the Phase C and Phase D entries. Run each one under the Phase C loop, and log a row as each step lands.

## Phase C: Run the loop

Each unit is an experiment. State the hypothesis, make the smallest change, measure against the predicate on the real artifact, keep it if it advanced, revert it if it did not. Verify each unit before you start the next one.

- Verify by inspecting the artifact, never a self-report. When something passes too easily, suspect the observation method before the system.
- Pair delegated work with a judge. If a worker games the gate, reset and harden the contract. If the gate itself is wrong, fix the gate in its own change.
- A verdict is VERIFIED, NOT VERIFIED, or INCONCLUSIVE. Inconclusive is not a pass. Do not hide a negative.

## Phase D: Keep the audit trail

Log the run with `/show-me-your-work` (`~/Desktop/Work/ostack/skills/show-me-your-work/SKILL.md`). The log lives in the effort dir and is never committed.

## Phase E: Verify and hand back

Check the whole against the Phase A predicate on the real product, not just the harness. Propose a gate, lint, check, or script for any correction that repeated, through `/correct` (proposals need the user's yes).

**Reply:** the playbook you designed, the rigor level and why, the decision-trail path, what is verified against the predicate, and what is still open.
