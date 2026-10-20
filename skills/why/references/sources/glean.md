# Glean (docs and Slack)

Written for ostack, in the shape of pstack's Notion and Slack source guides (MIT).

## What this source contains

Glean indexes the company's internal content. For a "why" question the useful parts are:

- Long-form docs: Confluence pages, Google Docs, Notion pages. PRDs, design docs, RFCs, ADRs, postmortems, runbooks.
- Slack messages and threads: real-time discussion that never reached a doc. Incident channels.
- Linear and GitHub content is also indexed, but the Linear and source-control investigators own those. Do not chase them here.

## How to search it

Use the Glean MCP tools (`mcp__claude_ai_Glean__search`, `mcp__claude_ai_Glean__read_document`, or the `mcp__glean_default__*` equivalents). This investigator is a subagent, so Glean is allowed here.

1. **Short keyword queries.** The feature name, key symbols or class names, error strings, the ticket ID, the PR number. Glean is keyword-matched: no full sentences, no OR/AND.
2. **Bound by time** when you know when the code shipped (`after:` and `before:` filters around the merge date).
3. **Bound by author** with `from:` or `owner:` for the PR author.
4. **Read the whole document** with `read_document` for every candidate. Rationale is often mid-document or in a comment. For Slack results, the snippet often carries the content even when the full thread does not load. Record which one you used.
5. **Follow links inside the docs only.** Record a cross-source link (a Linear ticket, a PR) under Additional Leads.

## What good evidence looks like here

- A design doc with a "Motivation", "Alternatives considered", or "Rejected approaches" section that matches the target.
- A postmortem that names the target code as the fix for an incident.
- A Slack thread where the author states the reason before or near the merge date.
- Meeting notes that record "we decided X because Y" near the PR date.

## Common pitfalls

- **Outdated docs.** A spec may describe a plan that changed. Cross-check with the PR. Flag the drift.
- **Jokes as decisions.** "lol just do the thing" is not a decision. Look for considered discussion.
- **Context collapse.** A single Slack message reads differently without its thread. Try to load the thread.
- **Access gaps.** Results are permission-filtered. An empty result can mean no access. Record it as a gap, never as "no discussion happened".
- **Auth failure.** If Glean is not authenticated, stop and report the gap. Do not make up findings.

## What to return

For each relevant item: title or channel, URL, author, date, the verbatim quote with its location, whether the doc was final or a draft, and its relevance in one sentence.
