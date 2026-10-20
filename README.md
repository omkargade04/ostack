# ostack

Local Claude Code plugin for Omkar's workflow. Local only: no remote, no marketplace repo.

Design and decisions: `~/Desktop/Work/Obsidian-Work/Claude Code Sessions/ostack - Personal Claude Code Plugin/`.

## Install (once)

```bash
claude plugin validate ~/Desktop/Work/ostack
claude plugin marketplace add ~/Desktop/Work/ostack
claude plugin install ostack@ostack
```

The marketplace is this directory. Claude Code 2.1.303 loads the plugin's skills from `skills/` here, not from the cache copy in `~/.claude/plugins/cache/ostack/ostack/<version>/` (the debug log shows the path). Skill and playbook edits apply in the next session. Agents probably load from here too, but the log does not show their path. After an agent or manifest edit, bump `version` in `.claude-plugin/plugin.json`, run `claude plugin update ostack@ostack`, and start a new session.

## Use

| Command | What it does |
|---|---|
| `/ostack:mode ticket <ID>` | Ticket triage, RCA, and fix. Triage method: `~/.claude/skills/verify-triage`. |
| `/ostack:mode feature <topic>` | Feasibility, approval, grill, scope, plan, doc review. No code. |
| `/ostack:mode optimize <topic>` | Same as feature, measurement first. |
| `/ostack:mode review-pr <PR or branch>` | Run in an Opus session. The session reviews with the repo standard, and the Thermos pair runs on Sonnet. Add "cross-review" for a blind Sonnet reviewer. |
| `/ostack:mode execute <effort>` | Run an approved plan. Start the session with `claude --model sonnet`. It ends with the commands for review-pr in an Opus session. |
| `/ostack:grill-me` | The upgraded grill: interview until every decision is settled, recorded in the effort dir. Bare `/grill-me` is the original user skill in `~/.claude/skills/grill-me`, kept as it is. |
| `/devils-advocate` | Argue against a decision. |
| `/figure-it-out` | Design a playbook when none fits. Grill and GO gates still apply. |
| `/architect` | Two Opus sketches plus one Sonnet sketch, pick one, stop for a go. |
| `/how` | How code works: Explore subagents, one explainer. |
| `/why` | Why code is shaped this way: git/gh, Linear, Glean investigators (Grafana for defensive code), synthesis in the main session. |
| `/blast-radius` | What a change breaks elsewhere, with the one safety fact proven by running code. |
| `/tdd` | Test-first under the unit-test HARD RULE. |
| `/benchmark-checklist` | Vet a performance number before you trust it. |
| `/show-me-your-work` | Decision log (`decisions.tsv` in the effort dir) plus a trail review. |
| `/unslop` | Cut AI tells from PRs, commits, docs, and drafts. |
| `/no-comments` | Delete comments with `ostack:comment-sicko`. On demand, needs a go. |
| `/correct` | Propose ways to make repeated mistakes impossible. Each change needs a yes. |
| `/create-verification-skill` | Generate `verify-<app>` on top of the shared verify core. |
| `/maintain-verification-skill` | Keep a `verify-<app>` feature map current. |

## Two names for every skill

Both `/<name>` and `/ostack:<name>` work for every skill. The bare name is a small wrapper in `~/.claude/skills/<name>/SKILL.md` that copies the menu fields and points at the repo skill. Exception: bare `/grill-me` is the original user skill, so the script leaves it alone.

Do not symlink a skill into `~/.claude/skills/`. Claude Code drops a plugin skill when its SKILL.md realpath equals a user skill's realpath, and `/ostack:<name>` disappears.

To add a skill or to change a description, run `python3 scripts/bare-skills.py`. The script rewrites only its own wrappers and old symlinks into this repo. It skips any other folder of the same name. Wrappers set `disable-model-invocation: true`, so the model sees each skill once, as `ostack:<name>`.

The registry daemon (`~/.registry`) syncs `~/.claude/skills` to the `omkar-gade` namespace in the internal marketplace. It then shows a third name, `/omkar-gade:<name>`, which is a snapshot from the last sync.

Skills that set `disable-model-invocation: true` cannot be chained with the Skill tool. Playbooks and other skills read them by path: `~/Desktop/Work/ostack/skills/<name>/SKILL.md`.

## Models

Main session: Opus. Every subagent: Sonnet (`CLAUDE_CODE_SUBAGENT_MODEL=sonnet`, forced, in `~/.claude/settings.json`). Feature code: a separate Sonnet session. Final code review: the main Opus session. FORCE ignores the `model:` line in agent files, so no agent can run on Opus.

## Gates

The gates live in `~/.claude/hooks/write-gate.sh` and `~/.claude/CLAUDE.md`, not in this plugin, so they still apply when ostack is off.

## Credits

Thermos skills and agents: cursor/plugins, MIT (LICENSE files kept in each skill folder).

pstack v0.15.26 by Lauren Tan, MIT: `tdd`, `blast-radius`, `no-comments`, `correct`, `unslop`, `figure-it-out`, `benchmark-checklist`, `create-verification-skill`, `maintain-verification-skill`, `show-me-your-work`, `architect`, `why`, `how`, and the `comment-sicko` agent, each adapted (LICENSE file in each skill folder). Some playbook ideas also come from pstack. The unmodified source is kept read-only at `~/.local/share/ostack/vendor/pstack-0.15.26/`.
