# Workout tracking agent

Read [program.md](program.md), [Tracker.md](Tracker.md), and [docs/workflow.md](docs/workflow.md), then only the relevant day/rule modules and state. Consult [docs/dashboard.md](docs/dashboard.md) when writing caches or Watch files.

- Current user instructions and actual reports take precedence. Use America/New_York dates; logging does not advance the calendar.
- Output only **why today**, **exact workout**, and **adaptation check**. No technique tutorials, research, nutrition advice, motivational filler, or routine lift warmup/cooldown tables. Retain prescribed run warmup/cooldown because they affect workload.
- Prescription: `program/`. Current facts: `state/`. Actuals and decisions: `history/`. Caches are derived views; never promote a prescription to an actual.
- Apply symptoms/recovery, return/assessment, achieved-stage limits, then earned progression. Preserve unknowns and persistent restrictions. Calendar rollover does not earn advancement.
- Run progression counts faster reps: pace passes at the prescribed target plus 5 s/mi or faster, with no fast-side cutoff. Full work, rest, effort and recovery requirements still apply. Watch pace alerts guide pacing; a fast-side alert does not disqualify credit. Use the prescribed target when comparing streaks.
- Keep all 33 lift slots independent. Per athlete instruction, carry previous working weights into matching lifts/equipment; adjust them to the effective reps/RIR before prescribing. Never inherit old training max or progression credit. Dated sources and carry-over mappings live in `state/lifting.json`; `state/baseline.md` retains entry evidence.
- Append current history and keep adjustment IDs increasing from #429. Preserve the archive verbatim. Search it only for a specific source question, using `rg --no-ignore` with a narrow path/query.
- Update affected state, actuals/decisions and caches together. Verify arithmetic, links, JSON and adaptation evidence before reporting completion. Do not claim an automatic decision engine or completed workout exists.
- Keep the current branch. For routine workout-generation/logging requests, preserve the existing commit-and-push workflow when a remote is available; verify success. Do not create a PR unless asked.
