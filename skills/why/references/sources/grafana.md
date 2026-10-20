# Grafana logs (runtime reality)

Written for ostack, in the shape of pstack's Datadog source guide (MIT). Use it only when the target code looks defensive: retry, timeout, rate limit, guard, feature flag, OOM handling.

## What this source contains

The runtime record of what happened in production, as opposed to what was planned:

- Service ERROR and WARN logs per tenant.
- Kubernetes events: pod restarts, OOMKills, evictions.
- Workflow logs for Temporal runs.
- Memory and CPU metrics through the `grafana-metrics` skill.

## How to search it

Read `~/.claude/skills/grafana-logs/SKILL.md` and use its query method. For metrics, read `~/.claude/skills/grafana-metrics/SKILL.md`.

1. **Find the owning service** and the tenants where the target code runs.
2. **Time-bound every query.** Use a window around the target's merge date, for example 30 days before and after. Unbounded queries time out.
3. **Search for the error string** that the defensive code handles, or the exception class, or the activity name.
4. **Correlate in time.** Did the error spike before the merge and stop after it? Which release fixed it?
5. **Aggregate, do not dump.** Count by day or by tenant. Quote a few representative lines verbatim.

## What good evidence looks like here

- An error pattern that the defensive code prevents, timestamped in the window before the change, and gone after it.
- An OOMKill or eviction pattern before a memory guard landed.
- A timeout pattern on the exact activity that later got a retry or a longer timeout.

## Common pitfalls

- **Correlation is not causation.** Other changes may have landed in the same window. Check neighboring PRs.
- **Retention cliffs.** If the window predates log retention, that is a gap, not a null result. Say so.
- **Logged is not caused.** A log line shows that someone cared to log it, not that the code exists because of it.
- **Tenant names.** Do not copy customer or tenant names into anything outside the effort dir.

## What to return

For each relevant finding: the query, the time window, the service and tenant, a compact numeric summary (counts per day, first and last seen), a few verbatim log lines, and the time correlation with the target's merge date.
