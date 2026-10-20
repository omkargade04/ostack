---
name: grill-me
description: Interview the user about a plan or design until every decision is settled, one question at a time, each with a recommended answer. Use before any feature, optimization, project, or large change (the Grill gate in CLAUDE.md), after a feasibility doc is approved, or when the user says "grill me".
---

# Grill me

Interview me about every part of this plan until we reach a shared understanding. Walk down each branch of the design tree. Settle the dependencies between decisions one by one.

Code writes are locked while a grill runs. The write-gate hook re-locks them when a message starts a grill. Docs in the Obsidian vault and the scratchpad stay writable.

## Step 0: restate

Restate the request in three lines: the goal, what is out of scope, and how we will know that it worked. If I correct it, restate it again.

## Each question

1. Sort the question first.
   - Fact: code, a tenant, a log, or a doc can answer it. Find the answer yourself with a read, a grep, or a read-only probe. Do not ask me.
   - Preference or product call: ask me.
2. Ask one question at a time. Use AskUserQuestion when the options are clear. Put your recommended answer first, with a one-line reason.
3. Show the facts that shape the question. Label each one: measured, inferred, or guess.

## Record

After each answer, write the decision as a row in the effort dir's `DECISION - <topic>.md` and one row in `_INDEX.md`: number, date, decision, answer. If a later answer changes an earlier one, mark the earlier row `superseded`.

## When I am away

If I do not answer, write the open questions to the DECISION doc with your recommended defaults, mark them `awaiting-human`, and stop. Never code on defaults.

## Done

The grill ends when every branch has an answer. Then show all decisions in one table and name the next doc to write: the scope doc, then the implementation plan.

"Agreed", "ok", and "yes" accept a decision only. Code needs an explicit go.
