# Optimize

This playbook covers optimization and feasibility work. It runs in the main session on Opus and writes no code. The `execute` playbook writes the code later, in a new Sonnet session.

1. **Context.** Load the effort dir's `_INDEX.md`, or create the effort dir. Restate the request in three lines.
2. **Measure first.** Probe the heaviest tenants for real numbers: memory, disk, runtime, data volume, and Temporal activity durations. Compare them with the baselines in earlier Obsidian docs. For each number, state the unit, peak or steady, and the denominator. Vet the baseline with `benchmark-checklist`, and vet every number after it the same way.
3. **Feasibility.**
   - List the options cheapest first: config, algorithm, batching, caching, parallelism, architecture.
   - Score each option on runtime impact and data-loss risk. Customers notice runtime regressions.
   - Before you trust a benchmark, prove that it can tell a good change from a bad one.
   - Write `FEASIBILITY - <topic>.md` in the effort dir, with a recommendation.
4. **Feasibility review.** Dispatch `ostack:doc-reviewer`. Fix each REVISE finding.
5. **Approval.** Stop. Wait for my approval of the feasibility doc.
6. **Grill.** Run `ostack:grill-me`.
7. **Scope.** Write `SCOPE - <topic>.md` with the target numbers. Never lower a target to declare success.
8. **Implementation plan.** Write `PLAN - <topic>.md` with `superpowers:writing-plans` and the same overrides as the feature playbook, step 8. Add a benchmark step to each task that changes performance, vetted with `benchmark-checklist`.
9. **Plan review.** Dispatch `ostack:doc-reviewer`. Fix each finding until the verdict is PASS. Record the PASS in `_INDEX.md`.
10. **Hand off.** Offer `/handoff`. Give me the exact commands for the code session: `claude --model sonnet`, then `/ostack:mode execute <effort dir name>`.
