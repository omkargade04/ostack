---
name: mode
description: Omkar's workflow router. Picks the playbook for the task and copies its steps into the todo list. Playbooks are ticket (customer ticket triage, RCA, fix), feature, optimize (optimization or feasibility), review-pr, and execute (run an approved implementation plan in a fresh Sonnet session). Use at the start of any of these tasks, for example when the user pastes a Linear ticket, a failed workflow URL, or a PR link, asks whether something is feasible, or runs /ostack:mode <playbook>.
---

# Mode

## Pick and load

1. Take the playbook from the argument: `ticket`, `feature`, `optimize`, `review-pr`, or `execute`. With no argument, pick it from the task and say which one you picked in one line. If no playbook fits (a migration, a multi-part change, a long unattended run), read `~/Desktop/Work/ostack/skills/figure-it-out/SKILL.md` and follow it instead.
2. Read `~/Desktop/Work/ostack/skills/mode/playbooks/<playbook>.md`.
3. Copy every step into the todo list. If a step does not apply, keep it in the list as `skip: <reason>`.
4. Do the steps in order. The current prompt overrides the playbook.

## Rules for every playbook

- Gates from CLAUDE.md:
  - Grill gate before large work.
  - Code only after an explicit go.
  - Outbound posts are drafts unless my current message says post, send, or comment on.
- Models: the main session plans and judges. Every subagent runs on Sonnet. Do not pass a model override.
- Memory: write findings, decisions, and evidence to the effort dir as you go. The effort dir is `~/Desktop/Work/Obsidian-Work/Claude Code Sessions/<TICKET-ID or Topic> - <Short Title>/`, with `_INDEX.md` at its root.
- Every claim carries a label: measured, inferred, or guess.
- Every conclusion names what would prove it wrong.
- Every fix names what it does not fix.
- A playbook step that names an ostack skill (`tdd`, `blast-radius`, `architect`, `benchmark-checklist`, `show-me-your-work`, `how`, `why`) means: read `~/Desktop/Work/ostack/skills/<name>/SKILL.md` and follow it. These skills cannot be chained with the Skill tool.

## Subagent brief

Start every subagent prompt from this template. Fill each field or write `none`.

```
GOAL: <one sentence>
SCOPE: <files, repos, tenants it may touch>
CONTEXT: <facts it needs, with paths to docs and evidence>
ACCEPTANCE: <what done looks like>
VERIFY: <the command or check that proves it>
FORBIDDEN: <what it must not touch or do>
REPORT: <the shape of the answer you want back>
STANDING: Operate fully autonomously — never ask or wait for the user; just execute.
```
