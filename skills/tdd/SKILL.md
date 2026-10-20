---
name: tdd
description: "Test-first for every bug fix and feature, under Omkar's unit-test HARD RULE: name the bug the test catches, prove red then green by breaking the logic, and fall back to an env-gated integration test when a unit test cannot cover it. Use for /tdd, and from ostack:coder and the execute playbook."
disable-model-invocation: true
---

# TDD

Adapted from pstack `tdd` (MIT). Test-first is the default for every bug fix and feature, not an opt-in.

Before you write, change, or plan any test, read the HARD RULE file: `/Users/omkar.gade/.claude/projects/-Users-omkar-gade-Desktop-Work-atlan-databricks-app/memory/feedback-quality-unit-tests-only.md`. It decides which tests are worth writing.

## Workflow

1. **Understand the bug or behavior.** Identify the intended behavior, current behavior, affected path, and smallest observable reproduction.
2. **Name the bug the test catches.** Write it in the test's docstring. If you cannot name a real bug (a decision, a guard, a data-loss path), do not write the test. No tests for defaults, constructors, log lines, message strings, or mock-call counts.
3. **Choose the narrowest executable check.** Prefer the closest unit, component, or regression test already used for that codepath. Follow the repo's existing test pattern, and say so when that pattern is weak.
4. **Write the failing test first.** Encode intended behavior, not the current implementation.
5. **Run it before the fix.** Confirm it fails for the intended reason. If it passes, or fails for an unrelated reason, fix the test or the reproduction before you touch the implementation.
6. **Fix.** Make the smallest production change that satisfies the intended behavior and keeps nearby contracts.
7. **Rerun.** The new test passes. Run the sibling tests and compare failures with the base branch.
8. **Prove red/green for each new test.** Break the logic on purpose, watch the test fail, restore the logic.

## When a unit test cannot cover it

A real API, multi-workspace auth, or a live tenant cannot be faked well. Write an env-gated integration test (for example under `tests/integration/`) that skips cleanly when its env vars are missing. If even that is impractical, use the closest executable check: a targeted script, a log assertion, or a replay of a recorded input with a diff of the output (record counts and last-line integrity included).

Prefer no new test over a bad test. A bad test mostly tests mocks, encodes implementation details, depends on timing or global state, or would be deleted right after it proves the fix.

## Guardrails

- Never change an existing test to match a wrong implementation. If an existing test must change, stop and report it.
- Do not weaken existing assertions.
- Keep the regression test focused on the bug. No broad fixture churn.
- If the bug is flaky, make the test deterministic and say which signal it locks down.
- Plan task IDs never go into test names, docstrings, or commits.

## Report

- The failing-before test, the command, and the failure line.
- The passing-after run and the sibling-test result against the base branch.
- The red/green proof: what you broke, and that the test failed.
- If no failing-before test was possible, why, and which check you used instead.
