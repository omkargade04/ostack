# Review a PR

Run this in an Opus session. This session is the primary reviewer. Subagents are forced to Sonnet, so they add a second model's view. If this session does not run on Opus, stop and tell me to start one with `claude`.

1. **Scope.** Find the PR number, branch, or diff. Collect the diff against the merge base (`git diff $(git merge-base main HEAD)`, so that uncommitted work is included), any untracked files from `git status --short`, and the full contents of the changed files.
2. **Standard.** Look for the repo's own review standard: `.claude/skills/*review*`, `.claude/agents/*review*`, `.claude/commands/*review*`, a CONTRIBUTING file, or a review checklist. If one exists, it is the primary rubric.
3. **Reviewers.** Launch the Thermos pair: read `~/Desktop/Work/ostack/skills/thermos/SKILL.md` and follow it. While it runs, review the diff in this session with the repo standard and the Review checklist in `~/Desktop/Work/ostack/agents/reviewer.md`. If the diff touches shared code (`application-sdk`, `atlan-publish-app`), also run `blast-radius` and prove its one safety fact.
4. **Cross-review.** If my message says "cross-review", also launch `ostack:reviewer` and tell it that it is the blind cross-reviewer. Give it only the diff and the file paths, never the other verdicts.
5. **Merge.** Dedupe the findings. Give more weight to findings that more than one reviewer raised. Settle disagreements yourself, against the code.
6. **Answer.** Is it safe to merge, and can it break the connector? List the findings with file:line, severity, and an evidence label.
7. **Comments.** Review comments are drafts unless my message says post or comment on.
