---
name: show-me-your-work
description: "Keep a reviewable decision trail for long-running or unattended work: decisions.tsv in the effort dir, one row per decision (what, why, evidence, result), audited against the transcript and reviewed by a Sonnet subagent at the end. Use for /show-me-your-work, /figure-it-out runs, the execute playbook, or work Omkar reviews after stepping away."
disable-model-invocation: true
---

# Show me your work

Adapted from pstack `show-me-your-work` (MIT). Keep one canonical log.

## Where it lives

`decisions.tsv` beside `_INDEX.md` in the effort dir (`~/Desktop/Work/Obsidian-Work/Claude Code Sessions/<effort>/`). `/resume` finds it there. Never commit it, and never copy it into a repo or a PR.

## The format

One TSV file, one row per decision. Cells stay single-line. Evidence is a pointer, not prose.

Copy `references/decision-log-template.tsv` (the header row) to start a clean log. Columns:

- **ts.** ISO8601 timestamp.
- **phase.** The phase or workstream.
- **decision.** What was chosen or done, one line.
- **why.** The reason in plain words.
- **evidence.** A pointer that proves it: commit SHA, PR number, `file:line`, a Temporal run ID, or an artifact path. Never a paragraph. No customer or tenant names, no secrets.
- **result.** The outcome or predicate state: `tests green`, `reverted`, `VERIFIED`, `INCONCLUSIVE`, `open`.

An example:

```
ts	phase	decision	why	evidence	result
2026-05-24T09:02:00Z	frame	counted the work first, about 40 files and roughly 6 hours	wanted the size before a long run	commit 3a9f1c2	found 3 blockers to settle first
2026-05-24T09:40:00Z	harness	saved the current-state output before changing anything	so old and new output can be diffed	baseline/current-state.jsonl	saved 12,400 records
2026-05-24T11:15:00Z	diff	moved the dedupe into the shared reader	one owner for the rule	commit 7c21e0a	output diff empty, tests pass
2026-05-24T12:30:00Z	diff	threw out a subagent's change because its output file was truncated	checked the file, not its summary	worktree reset	reverted, tightened the brief
```

## Logging a row

Write each row the way you would tell a teammate what you did. Plain words, concrete actions (the `unslop` rules apply).

Use the helper:

```bash
~/Desktop/Work/ostack/skills/show-me-your-work/scripts/log.sh <logfile> <phase> <decision> <why> <evidence> <result>
```

It stamps `ts`, writes the header on first use, strips stray tabs and newlines, and prefixes any cell that starts with `=`, `+`, `-`, or `@` with a single quote.

Log decision points and checkpoints, not every action: a fork chosen, a unit completed with its verification result, a pivot or revert with its trigger, a blocker found, a gate fixed. For loop runs, one row per iteration.

A run is one agent conversation, including its later turns. A pickup after `/resume`, a replacement agent, or a new session starts a new run. When a run adds to a log that already has rows, its first row has phase `start`. Its evidence names this run (the session ID). Before you add rows in a later turn, read the last rows to see whether another run wrote since. Use phase `start` for nothing else.

## Rules

- Append-only. A wrong call gets a new row that supersedes it. Never edit or delete history.
- Prefer evidence from committed scripts and real artifacts over hand-made one-offs.

## Audit the log against the transcript

At the end of the run, before you hand back, check that the log told the truth. Read only this session's transcript: `~/.claude/projects/<project-slug>/<session-id>.jsonl`. Never glob across other sessions. They hold unrelated private chats.

- Every row in this run's stretch maps to a real decision or action.
- Each row's evidence resolves and shows what the row claims.
- A fork, pivot, or abandoned approach that shaped the work but is not logged is a gap. Add it.

Correct the log, not the story. Never edit or remove a row. When a row is wrong, add a row that supersedes it with what happened.

## Review of the trail

Before you hand back, spawn one `Agent` (`subagent_type: "general-purpose"`, Sonnet, read-only by instruction). It reads the trail and this session's transcript, then flags what the user must look at. Not a redo of the work.

- Decisions logged with weak or absent evidence.
- Verification steps skipped or claimed without proof in the transcript.
- Choices that look risky in hindsight: premature, scope creep, a symptom patched instead of the cause.
- Gaps that the user would miss on a quick skim.

The reviewer is a second model, not a second model family: every subagent runs on Claude Sonnet. In a Sonnet session (the execute playbook) it is the same model as the writer. The later Opus review-pr pass covers that.

Every reply for a run that produced a trail ends with an "Attention" section. Its first line is `reviewed by <model>`. Then list each flag with the row or moment it points to. "No flags" is a valid value.

## Reading the trail

Read top to bottom, follow the evidence pointers, spot-check. In a terminal: `column -s$'\t' -t decisions.tsv`.

## Composing this skill

Other skills route their audit trail here. Reference this file by path and let it own the format. Do not restate the columns.
