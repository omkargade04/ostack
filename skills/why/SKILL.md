---
name: why
description: "Use for 'why does X work this way', 'why we picked Y', design rationale, regressions, postmortems, or the origin of a threshold. Sends investigators to git/gh, Linear, and Glean (docs and Slack), plus Grafana logs for defensive code, then writes a cited, confidence-tiered answer in the main session. Use how for runtime behavior."
disable-model-invocation: true
---

# Why

Adapted from pstack `why` (MIT). Investigate the motivation and intent behind code. The companion `how` skill (`~/Desktop/Work/ostack/skills/how/SKILL.md`) answers what the code does. `why` answers what forces led to its shape.

Investigators are `Agent` calls with `subagent_type: "general-purpose"`. They run on Sonnet (forced). Do not pass a model. They must not write files or change external state. The synthesis runs in this session, not in a subagent, so the judgment stays on the main model.

## Operating posture

Work as a careful, cautious, and precise investigator. Be honest about what you know and what you infer. Read `references/epistemics.md` before you synthesize, and follow it.

## Step 1. Understand the target and the question

The target is usually code, a pattern, a feature, or a named design decision. The question is usually a design rationale, a tradeoff, a motivating edge case, an external constraint, dead code, or a history sweep.

If the target is vague, make your best guess from the conversation (open files, recent edits, what was just discussed). State your interpretation in one line, then proceed.

## Step 2. Establish the code anchor

Before you spawn investigators, build the seed context inline:

- file paths and line ranges, key symbols
- `git blame -L <start>,<end> <file>` for last-touch commits
- `git log --follow -p -- <file>` for history through renames
- `git log --oneline -20 -- <file>` for recent commits with PR numbers
- `git log -1 --format=%B <commit>` to extract PR numbers and ticket IDs
- `gh pr view <number> --json title,body,author,createdAt,mergedAt,labels,closingIssuesReferences,comments,reviews` for each substantive PR

The anchor goes to every investigator.

## Step 3. Spawn the investigators

Spawn them in one message so they run in parallel. Each owns exactly one source. Each prompt is `references/investigator-prompt.md` filled in, plus its source guide from `references/sources/`, plus the anchor and the user's question.

| Investigator | Source guide | When |
|---|---|---|
| Source control (git, `gh`, code comments, tests) | `sources/code-archaeology.md` | Always |
| Linear tickets (claude.ai Linear connector) | `sources/linear.md` | Always |
| Glean (Confluence, Google Docs, Notion, Slack) | `sources/glean.md` | Always. Glean tools run only in a subagent. |
| Grafana logs (service logs, Kubernetes events, workflow logs) | `sources/grafana.md` | Only when the target looks defensive: retry, timeout, rate limit, guard, feature flag, OOM handling |

If the target looks defensive, also append `references/sources/incident-postmortem.md` to every investigator's prompt.

If a source is unavailable (for example the Linear connector fails to authenticate), do not guess. Record it as a gap in Sources Consulted. An error tracker and the analytics warehouse are not searched. List them as gaps when they could matter.

You may answer inline without investigators only for a single-commit target where the PR description already holds the complete answer. Say so explicitly.

## Step 4. Synthesize in this session

Follow `references/synthesizer-prompt.md` and `references/epistemics.md` yourself, with:

1. every investigator's findings, including null results and skipped sources
2. the code anchor
3. the user's original question

Spot-check one or two load-bearing citations before you present them.

## Output

The structure is the one in `references/synthesizer-prompt.md`: The Question, The Code in Question, What We Found, What We Can Reasonably Infer, Competing Hypotheses, What We Don't Know, Sources Consulted, Confidence Summary. Keep the confidence tiers intact. Sources Consulted has one line per source, including the ones that returned nothing or were skipped, with the reason.

If the `why` question comes before a change to this code, end with a Preserve / Change / Avoid / Risk set for planning the change.

Write findings to the effort dir when the question belongs to an effort.

## Failure modes to avoid

- **Recency bias.** The most recent commit is not the whole story. The current shape is often many earlier decisions. Trace back.
- **Code as its own evidence.** Code shows what it does, not why it exists.
- **The embedded hypothesis.** A guess in the user's question is a candidate, not a conclusion.
