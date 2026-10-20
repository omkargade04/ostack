---
name: no-comments
description: "Spawn ostack:comment-sicko on a diff or files, apply the accepted comment deletions, and offer encodings for claimed constraints. On demand only; it edits code, so the user's message must carry a go. Use for /no-comments."
disable-model-invocation: true
---

# No comments

Adapted from pstack `no-comments` (MIT). Spawn `ostack:comment-sicko`. Act on its accepted findings.

It deletes comments, so it is a code write. Run it only when the user's current message carries a go (CLAUDE.md "When to write code").

## Scope

Use the files or diff that the user names. Otherwise use the current diff against the base branch, default `main`, including the working tree.

## Keep-list (the user's rule)

- Docstrings, only where the contract or the reason is not obvious.
- License and legal headers.
- Behavior forced by an external dependency, platform, vendor, or protocol that we cannot reshape.
- Python suppressions (`# noqa`, `# type: ignore`, `# pragma: no cover`) only when the rule is wrong, pedantic, or style-only for that line. If the rule catches real bugs, the suppression dies and the symbol gets `MUST KILL`.
- Issue or ticket links that explain a constraint the code cannot express.

Everything else dies. The `ponytail:` comment convention does not apply. A ceiling note goes in the function docstring.

## Steps

1. Spawn the agent with `subagent_type: "ostack:comment-sicko"`. Pass the scope and the keep-list. Do not restate its rules.
2. Inspect its report and diff. Reject application-code edits, scope escapes, deletions of keep-list items, misstated `MUST KILL` reasons, and flags that treat kept intentional code as guilty. A keep survives only with proof that it is about something we cannot change. Before you accept a thin `IMPORTANT` or `do not remove` kill or keep, run `how` or `why` on its symbol (`~/Desktop/Work/ostack/skills/how/SKILL.md`, `~/Desktop/Work/ostack/skills/why/SKILL.md`). If a kill is ambiguous, do not restore. If a keep is refuted or still ambiguous, delete it. Revert and rerun one rejected report with the failure named. If a second report is also rejected, report it open and stop.
3. Fix trivial accepted flags directly: delete a dead path, drop a parameter, or use the real API. If a fix needs a new shape, run `/architect` once for the accepted set and stop at the sketch.
4. Implement the smallest root-cause fix in scope. Remove every named workaround. If the root cause is out of scope, land the smallest in-scope fix and report the rest open. Never bolt on symptom guards.
5. A constraint comment (`do not remove`, `talk to X before changing`) about our own code: offer the cheapest in-scope type, runtime check, test, or lint that encodes it, and wait for the user's yes. If approved, encode it, then delete the comment. Otherwise delete it and report the constraint open.
6. Run the sibling tests. Report the deletion count, restored comments, reruns, any architect sketch, fixes, encoding offers, unenforced constraints, and other open work.

No commit unless the user's message asks for one.
