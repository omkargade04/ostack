---
name: thermos
description: "Launch both thermo-nuclear review subagents in parallel, then synthesize their findings. Use for thermos, double thermo review, or combined bug/security and code-quality branch audits."
disable-model-invocation: true
---

# Thermos

Run the two thermo review passes as async background subagents in parallel, then synthesize their results.

## Workflow

1. Determine the review scope from the user request, PR, current branch, or relevant changed files.
2. Gather the diff and any file/context excerpts needed for reviewers to evaluate the change without guessing.
3. Check the repo for its own review standard: `.claude/skills/*review*`, `.claude/agents/*review*`, `.claude/commands/*review*`, a CONTRIBUTING or review checklist, or documented review conventions. If one exists, pass it to each subagent as the primary rubric, with the thermo rubric layered on top.
4. Launch both subagents in the same message (two parallel Agent calls):
   - `subagent_type: "ostack:thermo-nuclear-review-subagent"` for bugs, breakages, security, devex regressions, feature-flag leaks, and other branch-audit risks.
   - `subagent_type: "ostack:thermo-nuclear-code-quality-review-subagent"` for maintainability, structure, file-size growth, spaghetti, abstractions, and codebase-health risks.
5. Pass each subagent the same scoped diff/file context and ask it to return prioritized findings with file references and evidence.
6. After both finish, synthesize the results with findings first, deduplicated across reviewers. Weight overlapping findings more heavily, resolve disagreements with your own judgment, and keep summaries brief.

If individual background summaries are already visible to the user, do not restate them wholesale. Surface the unified verdict, the highest-signal findings, and any remaining uncertainty.
