# Source guides

The why skill spawns one investigator per source. Each reads one guide below.

| Source | Guide | Tools |
|---|---|---|
| Source control history | [`code-archaeology.md`](./sources/code-archaeology.md) | git, `gh` |
| Linear tickets | [`linear.md`](./sources/linear.md) | claude.ai Linear connector |
| Docs and Slack | [`glean.md`](./sources/glean.md) | Glean MCP (subagent only) |
| Runtime logs (defensive code only) | [`grafana.md`](./sources/grafana.md) | `grafana-logs`, `grafana-metrics` skills |

Cross-cutting:

- [`incident-postmortem.md`](./sources/incident-postmortem.md). Add it to every investigator when the target code looks defensive (retry, timeout, rate limit, guard, feature flag, OOM handling).

Not searched: an error tracker and the analytics warehouse. List them as gaps in Sources Consulted when they could matter.
