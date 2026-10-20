# Ticket: triage, RCA, fix

The triage method is `~/.claude/skills/verify-triage/SKILL.md`. Read it and follow its phases. Do not restate its routing table or evidence tiers here. It stays the single source for how to triage.

1. **Intake.** Fetch the ticket, its comments, any linked RCA doc, and any linked Slack thread. Give a TLDR and a one-line class: workflow failure, or data or lineage missing or wrong. Open or create the effort dir and its `_INDEX.md`.
2. **Anchors** (verify-triage §1). Pin the customer's own words (Zendesk vs Linear), the incident window with why-now, and the incident SHA from the failing pod's `build_id`.
3. **Triage** (verify-triage §2–§6.5).
   - If an RCA was handed down, build the claim ledger and check each claim against a higher evidence tier.
   - If there is no RCA, or it is wrong, run the RCA in the lane that verify-triage names for its shape.
   - If a lane's skill is missing on disk, say which rung was missing and mark the affected claims UNVERIFIED. Known gap (checked 2026-10-20): `debug-connector-run-failure` is not on disk. `dry-analysis-argo` exists only in the org plugin cache.
4. **Depth.** Apply `root-cause-depth-check` and `workaround-vs-fix`. Name the layer that owns the fix. If the fix touches shared code (`application-sdk`, `atlan-publish-app`), run `blast-radius` on the proposed change.
5. **Report.** Write TLDR · Issue · Root cause · Evidence · Fix or Next steps to the effort dir. Label the evidence. Name what would prove the root cause wrong. Draft the ticket comment with `/draft-comment`. Do not post it.
6. **Short grill.** If the fix crosses a function boundary or the fix layer is unclear, ask 3 to 5 questions with `ostack:grill-me` rules. Write `skip: local fix` otherwise.
7. **GO gate.** Stop here until I give an explicit go.
8. **Fix.** Dispatch `ostack:coder` with the subagent brief.
   - Layer ladder: `application-sdk`, then `atlan-publish-app`, then the connector app. Fix the layer whose own code is wrong.
   - New worktree from the latest main, on a branch named after the ticket.
   - The regression test comes first, and it must fail for the RCA's reason. The coder follows `tdd`.
9. **Review.** Review in this Opus session, because `ostack:coder` wrote the code. Use the repo's own review standard, for example `/app-review` or `connector-review` in `atlan-databricks-app`. With no repo standard, run the `review-pr` playbook.
10. **Verify.** If the fix changes runtime behavior, prove it on an allowlisted tenant: red without the fix, green with it. If `~/Desktop/Work/ostack/skills/verify` does not exist yet, write `skip: verify skill not built` and say so in the report.
11. **Ship.** Open a PR only when my message asks for it. The ticket comment stays a draft until I say post.
