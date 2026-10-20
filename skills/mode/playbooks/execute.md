# Execute an approved plan

Run this in a new session started with `claude --model sonnet`. The input is the effort dir name.

1. **Load.** Read the effort dir's `_INDEX.md` and `PLAN - <topic>.md`.
2. **Check approval.** `_INDEX.md` must show a doc-reviewer PASS on the plan and my approval. If either is missing, stop and say what is missing.
3. **Restate.** Restate the plan in five lines: repo, branch, tasks, verify steps, and done check.
4. **Set up.** Make a new worktree from the latest base branch, on the branch that the plan names.
5. **Per task.** Follow `tdd`. Log each finished task, pivot, and revert with `show-me-your-work` to `decisions.tsv` in the effort dir.
   1. Write the task's test first. Run it and confirm that it fails for the right reason.
   2. Write the code.
   3. Run the task's tests and the sibling tests.
   4. Tick the task in the plan's checklist, with the test name and its result.
6. **Code rules.** Follow CLAUDE.md Code quality, `/ponytail:ponytail`, and the unit-test HARD RULE file. Plan task IDs never go into code, comments, test names, or commits.
7. **Deviation.** If the plan is wrong, stop that task. Write the deviation to the effort dir and ask me. Do not redesign silently.
8. **Verify.** Run the plan's verify steps. Use the verify skill on an allowlisted tenant when the plan asks for it. If `~/Desktop/Work/ostack/skills/verify` does not exist yet, say that this step was skipped.
9. **Report.** Report what changed, the test evidence, what would prove it wrong, and what it does not fix. Write the result to the effort dir.
10. **Hand off the review.** Do not review the diff in this session. Give me the exact commands for the review: `cd <worktree>`, `claude`, then `/ostack:mode review-pr <branch>`. If the review finds blockers, fix them in this session, then run the review again. Commit, push, or open a PR only when my message asks for it.
