---
name: create-verification-skill
description: "Generate an app-specific verification skill (verify-<app>) that drives an Atlan connector app the way a user does and proves behavior on an allowlisted tenant, on top of the shared ostack verify core. Use for /create-verification-skill, 'make a verify skill for this app', or when an app has no scripted way to prove behavior."
disable-model-invocation: true
---

# Create a verification skill

Adapted from pstack `create-verification-skill` (MIT). Every serious app needs a scripted way to drive the real app and prove behavior: launch or trigger it, exercise a feature the way a user would, and capture evidence. This skill generates that as `~/Desktop/Work/ostack/skills/verify-<app>/`, tailored to one app. Write it for the next agent, not for a human. An agent reads it cold, mid-task, with no memory of the app.

## The shared core

Every generated skill calls the shared core at `~/Desktop/Work/ostack/skills/verify/` for the Atlan safety rules and scripts: the tenant allowlist gate, the undo ledger, evidence redaction, the idle signal (the Temporal parent workflow is closed, never "the AE run finished"), and the verdict tied to the head SHA. The generated skill names the core's steps. It does not copy them. If the core does not exist yet, stop and say so: build the core first.

## 1. Interview the repo, not the user

Answer these from the codebase, the Obsidian effort docs, and earlier e2e runs. Ask the user only what you cannot observe:

- **Surface:** what does a user touch? For a connector app: the workflow run started from the Atlan UI or API, the assets and lineage that appear in Atlas, tags, and reverse sync to the source.
- **Run:** how does a run start on a dev tenant? The app's documented command, the workflow config, credentials through `~/.claude/scripts/load-token <tenant>`, never a literal secret.
- **Drive:** how can an agent exercise it? Existing e2e harnesses first, then the tenant API (`tenant-api`), the Temporal workflow history, and the source system's API.
- **Observe:** what evidence can be captured? Temporal history, run artifacts in object storage (`connector-run-artifacts`), Atlas search results, Grafana logs, output file line counts and last lines.
- **Isolate:** can two runs share a tenant or a source workspace safely? If not, say so in the generated skill. Refusing to double-drive a shared instance beats corrupting it.

If the app does not build or start as-is, fix that first or report it precisely. A skill written against a broken base teaches wrong steps.

## 2. Generate the skill

Write `~/Desktop/Work/ostack/skills/verify-<app>/SKILL.md` with YAML frontmatter (`name: verify-<app>`, `disable-model-invocation: true`, and a `description` that names the app, the surface, and when to use it) and these sections, each grounded in what the interview found. No placeholders left.

- **Gate:** the shared core's allowlist check for the target tenant. Writes only on allowlisted tenants.
- **Launch:** the exact command or API call that starts a run, and how to tell that the run is usable: the Temporal parent workflow is running and the first activity started. Include teardown.
- **Doctor:** one read-only check: right app version or image on the tenant, credentials valid, no other verify run in flight.
- **Drive:** the recipe with real commands and API calls from this repo, not examples. Prefer stable handles: qualified names, GUIDs read back from the API, workflow IDs.
- **Evidence:** what to capture and where (`~/.local/share/ostack/runs/<run-id>/`, redacted by the core). Proof standards: exercise the real user path, not test-only endpoints. Capture the action and the resulting state. Verify side effects (assets written to Atlas, tags set on the source) alongside the run status. Never judge from an HTTP status or a body size alone: decode the body.
- **Cleanup:** replay the core's undo ledger. Remove only what this run created. Never remove the evidence.
- **Helpers:** any script that the skill ships is executable, and its invocation is in the skill body.

## 3. Seed the feature map

Create `verify-<app>/features/README.md` plus one file per user-facing feature (start with the top 3 to 5). Follow the shape in `references/feature-map-example/`: a README index and one file per feature, with four H2s: `Sub-features`, `How to get to it (user POV)`, `Driving it with <harness>`, and `Gotchas`. If the seed data lacks a precondition that a journey needs, the journey reports a failure and the reason goes in that feature's `Gotchas`. Never weaken a journey to make it pass.

## 4. Prove the generated skill

Run its instructions end to end once on an allowlisted tenant: gate, launch, doctor, drive ONE mapped feature, capture evidence, clean up. After cleanup, confirm that the evidence still exists. A generated skill that was never run is a draft, not a deliverable. If you proved it on a stand-in (a local stack in place of a tenant), list every step the stand-in did that the real target will not. Those steps stay unverified.

The live run needs the user's go in the same message, and the tenant on the allowlist.

## 5. Keep it honest

Point the user at `/maintain-verification-skill` for keeping the map current as the app changes.
