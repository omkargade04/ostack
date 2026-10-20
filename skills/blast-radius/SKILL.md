---
name: blast-radius
description: "Find what a change could break somewhere else before it ships, beyond the diff, and prove the one fact it is safe because of by running real code. Use for 'blast radius of X', 'what could this break', a small diff you do not trust, or any change to shared code (application-sdk, atlan-publish-app)."
disable-model-invocation: true
---

# Blast radius

Adapted from pstack `blast-radius` (MIT). Find what a change breaks somewhere else, before it ships.

Companion to `how` and `why`. `how` tells you what the code does. `why` tells you why it is shaped that way. Blast radius tells you what it breaks somewhere else. Read them by path when a step needs them: `~/Desktop/Work/ostack/skills/how/SKILL.md`, `~/Desktop/Work/ostack/skills/why/SKILL.md`.

Listing the callers is not the job. Grep finds those in a second. The job is the breakage that grep does not show.

## Do not trust your own writeup

A blast-radius writeup that sounds right is worthless. It reads as convincing whether or not it is true. Find the one or two facts that the whole thing depends on and prove them by running code.

### How sure are you

For each fact that the change's safety depends on, get it as far down this list as is cheap, and say where it stopped.

1. You said so. Worthless on its own.
2. You pointed at the line. A real `file:line`, or the library's own source at the pinned version.
3. You showed that the bad case cannot happen. You walked the failure step by step and it does not reach.
4. You ran it. A script or test that calls the real code and fails loud if you are wrong.
5. You reproduced it in a real run on an allowlisted tenant.

Step 4 is usually one small script in the scratchpad that imports the same library the app ships and calls the exact function you worry about.

## Steps

1. **Read the change.** The diff, the symbols it adds, changes, and deletes, and what it now does differently, including the part the diff does not spell out. Pull the PR and commits as `why` step 2 does.
2. **Find the one fact it is safe because of.** Most changes that look risky are safe because of one fact, like "this call only drops cache entries that are already dead". Find that fact. If it holds, most risky cases clear at once.
3. **Look where grep stops.** Read the source of the library you call at its pinned version. Work out when things run. Follow what a symbol search misses. In Atlan connector code, check these first:
   - Atlas typedef and attribute key names. Never infer a key's meaning from its name: `connectorName` and `sourceTagConnectorName` are different keys.
   - The current-state file format, and every reader of it (the publish diff, the miners, the lineage readers).
   - Publish, diff, and delete behavior. A changed diff can delete assets in Atlas.
   - Temporal workflow and activity signatures, and payloads in flight during a deploy.
   - Feature flags and tenant config that change the path at run time.
   - Typedefs and the shapes that the frontend or other apps read from Atlas.
   - Code three hops downstream: `application-sdk` changes reach every connector app.
4. **Be honest about each risk.** Give it a real chance of happening and a real cost. Keep the risks you confirmed. List the ones you checked and cleared separately. Cite a real `file:line`. A search that finds nothing is still an answer. Never make up a caller or an API.
5. **Prove the one fact.** Write a script or test that runs the real code, run it, and paste what happened.

## What to hand back

- **What it does.** What changed, including the part that is not obvious.
- **The one fact it is safe because of.** State it, say which step you got it to, and show the proof. If you could not prove it, write unproven.
- **Risks.** Each names how it breaks, the `file:line`, how likely and how bad, and how to check. Paste the proof for the ones that matter.
- **Cleared.** What you checked and why it is fine.
- **Before you merge.** The cheapest test or repro that catches the real bug, including the script you wrote.

Write it through `unslop`. Cite real code. Strip customer and tenant names before it goes anywhere outside the effort dir.

**Reply:** the writeup above, with the one safety fact either proven or marked unproven.
