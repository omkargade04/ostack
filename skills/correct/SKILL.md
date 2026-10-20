---
name: correct
description: "Find the mistakes agents keep repeating and propose a way to make each one impossible: architecture first, then types, then a lint whose error names the fix, then a test, docs last. Proposals only; each change needs Omkar's yes. Use for /correct, or after the user corrects the same mistake twice."
disable-model-invocation: true
---

# Correct

Adapted from pstack `correct` (MIT). The user keeps correcting agents for the same mistakes. Propose changes so the next agent cannot make them.

Assume every contributor is an agent that sees only the files it opened, copies the nearest example, and takes the shortest path that compiles. A change that looks right from one file must be right for the whole repo.

## Gate

This skill proposes. It does not apply.

- Each new rule, lint, hook, CI check, or CLAUDE.md line needs the user's explicit yes before you write it. Show the exact text or diff first.
- Hooks, CI workflows, and Claude settings are control-plane files (org baseline §3). Confirm each one separately.
- No commits unless the user's message asks for one.

## Find the mistake classes

Read recent commits, reverts, review comments, the user's corrections in this session, the memory files, and CLAUDE.md. Group the mistakes into classes. A class counts once it has happened twice. Cite each occurrence (commit, file:line, or the user's words).

## Pick the highest level that works

1. **Architecture.** One owner per piece of state, one supported way per task. Hide internals so the wrong import fails. Replace hand-synced lists with one source. Delete old ways and dead code that an agent would copy.
2. **Types.** Make the bad state impossible to write. If bad code still compiles, propose a lint or CI check whose error names the file, type, or function to use instead. If the pattern is already common, fail only when a change adds more.
3. **Test.** Fix or delete any test that still passes when its behavior breaks, or that fails when only internals change.
4. **Docs or agent rules last**, only for judgment calls. Nothing fails when an agent skips them.

## Prove

For each proposed check, show that it fails on a real past mistake. Run the same command locally that CI would run. An exception goes on the offending line with a reason and an expiry date.

## Rule table

Personal rules go in a rule table in `~/.claude/CLAUDE.md` (rule, enforcer, status). A repo's own CLAUDE.md changes only through a PR that the user asks for. If a rule already exists and nothing enforces it, that is a repeat: propose the enforcement in the same change. Drop a rule once its mistake cannot happen.

**Reply:** each class with its evidence, the level you picked, why a higher level did not work, and the exact change you propose. Then wait for a yes.
