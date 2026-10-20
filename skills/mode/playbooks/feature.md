# Feature

This playbook runs in the main session on Opus and writes no code. The `execute` playbook writes the code later, in a new Sonnet session.

1. **Context.** Load the effort dir's `_INDEX.md`, or create the effort dir. Restate the request in three lines.
2. **Feasibility.** Answer four questions: can it be done, within which limits, at what cost, and with which risks.
   - Probe live APIs on a dev tenant or test workspace to confirm limits. Probes stay read-only unless the tenant is allowlisted.
   - Name the data shape first.
   - Give 2 or 3 options with a recommendation.
   - Write `FEASIBILITY - <topic>.md` in the effort dir.
3. **Feasibility review.** Dispatch `ostack:doc-reviewer` on the doc. Fix each REVISE finding.
4. **Approval.** Stop. Wait for my approval of the feasibility doc.
5. **Grill.** Run `ostack:grill-me`. Decisions go to `DECISION - <topic>.md` and `_INDEX.md`.
6. **Scope.** Write `SCOPE - <topic>.md`: goal, non-goals, the decisions (link each one to its grill row), risks, and how we will know that it worked.
7. **Sketch.** If the change is a contract change or crosses modules or repos (the CLAUDE.md "large" list), run `architect`. It stops after the sketch. The chosen sketch feeds the plan. Otherwise write `skip: no contract or cross-module change`.
8. **Implementation plan.** Write `PLAN - <topic>.md` in the effort dir with the `superpowers:writing-plans` skill, with these overrides:
   - Save it to the effort dir, not `docs/superpowers/plans/`.
   - No commit step in any task. Commits happen only when I ask.
   - The execution handoff is `/ostack:mode execute`, not `subagent-driven-development` or `executing-plans`.
   - Each task's test steps follow `tdd` and the unit-test HARD RULE.
   - The header also names the repo, the base branch, the new branch, the done check, the rollback, and the blast radius.
   A fresh Sonnet session with no other context must be able to run it. Plan task IDs stay in the plan. They never go into code, comments, test names, or commits.
9. **Plan review.** Dispatch `ostack:doc-reviewer`. Fix each finding until the verdict is PASS. Record the PASS in `_INDEX.md`.
10. **Hand off.** Offer `/handoff`. Give me the exact commands for the code session: `claude --model sonnet`, then `/ostack:mode execute <effort dir name>`.
