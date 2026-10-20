# Incident and postmortem context

Add this to every investigator when the target code looks defensive.

- **Linear:** tickets labeled `incident`, `sev-*`, `postmortem`, `reliability`, and WARE tickets around the dates the target code was added.
- **Glean:** postmortem docs, and Slack incident channels around the dates the target code was added.
- **Git:** commits like "fix for incident", "add defensive check", "revert" followed by "re-apply with ..." are strong signals.
- **Grafana:** the error pattern that the defensive code prevents, in the window before the merge.
