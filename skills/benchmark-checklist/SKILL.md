---
name: benchmark-checklist
description: "Vet a performance number (limiter, tuning, limits, errors, repeatability, relevance, and whether the work happened) before you report or act on it. Use when you run a benchmark, compare connector runs, or report a speedup or regression. The optimize playbook runs it on the baseline and on every number after."
disable-model-invocation: true
---

# Benchmark checklist

Adapted from pstack `benchmark-checklist` (MIT). Use it when you produce a performance number: a PR's before and after, a regression claim, a run-time comparison between connector runs, or a library or config choice. Answer each question with evidence from a run, not a guess about the code.

For a quick ballpark that the user asked for, one run is enough. Still check questions 4 and 7, and say that it is one run. A choice between options is never a ballpark.

## Where connector numbers come from

- Run time per activity: Temporal workflow history for the exact run (`temporal`, `worker-temporal-walk`, `rca-temporal-logs`).
- Worker memory, CPU, and disk: `grafana-metrics`, `worker-cluster-snapshot`.
- Data volume: record counts in the run's output files (`connector-run-artifacts`). Check line counts and the last line of each file, so a truncated file does not pass as a small one.
- Baselines: earlier numbers in the Obsidian effort docs. Probe the heaviest tenants, because customers notice regressions there first.

## Before you run anything

- Write down the claim that you expect to make, in the words you would ship ("extract is 30% faster at p50 on the heaviest tenant"). The questions test that sentence.
- Read the measurement script or query. Note what it times, counts, and ignores.
- On a Mac, check load with `uptime` and cores with `sysctl -n hw.ncpu`. If the machine is busy, find out what runs. If you cannot stop it, interleave the sides so both see the same noise, and say so.

## The questions

1. **Why not double?** Name the limiter. Profile in a run that you do not report, because profilers slow the work. Use CPU per process (`top`, `ps`), a runtime profiler (`py-spy`), and I/O wait, then map the hot spot to source. For a connector run, the limiter is often one activity, a source API rate limit, or the publish step. If a change did not move the number, the limiter explains why.
2. **Was it tuned?** Run every side the way production runs it: production flags and env, batch sizes, connection pools, caches as warm or cold as production sees them, and the same versions and data. If one side runs on defaults, you compared configurations, not implementations. Tune it and measure again before you pick a winner.
3. **Did it break limits?** Do the arithmetic. Compare bytes per second with disk and network bandwidth, and the time saved with the time that the changed piece took. Removing a piece that takes 10% of the run can make the run at most about 11% faster. A result past a limit measured something else: a cache, a no-op, or a bug.
4. **Did it error?** Count failures, retries, and non-success responses. Check that outputs are correct, not just present. Decode response bodies. Never judge success from a status code or a body size. Rejections are often fast. Timeouts and retries are slow.
5. **Does it reproduce?** Run each side at least 5 times, alternating (A, B, A, B), so warmup and drift favor neither. Report the median and range. A gap smaller than the run-to-run variation is no measurable difference.
6. **Does it matter?** Next to any micro result, measure the end-to-end workflow run time that the customer waits on, with realistic data sizes. Report the micro result as a share of the whole.
7. **Did it even happen?** Confirm that the work ran inside the timed region: the API call reached the source, the rows were written, the records were published. Generators that nobody iterates, skipped activities, and cached results produce numbers for work that never happened.

## Report

- Lead with the verdict: faster, slower, no measurable difference, or inconclusive.
- Give the number with its unit, peak or steady, the denominator, the run count, the range, and the limiter. For example: "extract activity p50 41 min to 33 min, median of 5 runs per side, range 32 to 35 min after, bound by the source API page size".
- Call the verdict inconclusive when you claim a difference but cannot name the limiter, when a side ran untuned, or when you could not check questions 4 and 7. Name the gap.
- A PR body gets one primary number. Put the runs, range, and limiter evidence in the effort dir.
