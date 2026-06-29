# Workout Tracking

Four markdown files + a tiny read-only dash, all driven by Claude Code chats. No backend, no build.

- **`program.md`** — lean, **current** prescription only: the 25-week Sub-20 5K + hypertrophy program as it stands today. The plan.
- **`program-history.md`** — chronological rationale for *why* the prescription changed (template revisions, mileage reshapes). `program.md` points here instead of carrying the prose inline.
- **`Tracker.md`** — lean, **current** state only: status, current working loads, active flags, shoe rotation, latest Incline BB row, latest Weekly Summary row. The record of what's true right now.
- **`Tracker-history.md`** — everything historical: the full Adjustments/Carry-forwards ledger, full Lifting Log, full Cardio Log, full SI/Sciatica Log, full Weekly Summary table. `Tracker.md` cites an Adj # or week; the detail lives here.
- **`index.html`** — a static, mobile-friendly view of today's brief + the week ahead. Renders `latest-workout.json` and `week-ahead.json`, both written by Claude.

`CLAUDE.md` tells Claude how to behave in this repo.

---

## How it works

**Morning:** ask for the workout.

> "what's today"

Claude reads the two **lean** files — `program.md` + `Tracker.md` — figures out the week / phase / day, applies current working loads and any active flags, and outputs a tight brief: intro line, lift table (sets × reps × load × RIR × rest × cue), warmup, cooldown. Cardio gets its own block — flags, workout, targets, cues. The history files aren't needed to generate a brief.

**Post-session:** dump what you did.

> "Hyp A done. Incline 135×5/5/5 RIR 3/2/2. Lat raise 25×12 across RIR 3. Preacher 50×10 across RIR 4/3/2. Pushdown 50×12 across RIR 4/3/2…"

Claude appends a structured entry to `Tracker-history.md` (Lifting/Cardio Log, Adjustments, SI Log, Weekly Summary), then syncs `Tracker.md`'s current-state sections (Current Working Loads, Active Flags, latest Incline BB row, latest Weekly Summary row) to match, then commits and pushes. The next morning's brief reads the new lean state.

That's the whole loop. Each session feeds context into the next; the history files keep that context lossless without bloating the files Claude has to read every morning.

---

## The program at a glance

25-week Sub-20 5K plan + 2×/wk hypertrophy. Phases: **Reset → Base → Build → Sharpen → Taper**, race day Sat Oct 24, 2026.

| Day | Session |
|---|---|
| Sun | Off / SI prehab |
| Mon | Z1 easy run + strides (hill strides Phase B+) |
| Tue | Hyp A lift (no run; upper-dominant) |
| Wed | Threshold (run or row) |
| Thu | Off — permanent, mobility / walk + SI prehab |
| Fri | Quality (T or VO2max) |
| Sat | Long run + Hyp B (≥6h gap) |

Full current prescription in `program.md`; why it changed in `program-history.md`. Current execution state in `Tracker.md`; full session history in `Tracker-history.md`.

---

## File map

| File | Purpose |
|---|---|
| `program.md` | Lean, current 25-week plan (prescription, source of truth for what's prescribed now) |
| `program-history.md` | Chronological rationale for past prescription changes |
| `Tracker.md` | Lean, current state: status, current loads, active flags, shoe rotation, latest forecast/summary rows |
| `Tracker-history.md` | Full Adjustments ledger, full lifting/cardio/SI logs, full Weekly Summary history |
| `index.html` | Read-only dash — fetches the two JSON caches and renders them |
| `latest-workout.json` | Cached daily brief (written by Claude each morning) |
| `week-ahead.json` | Cached 7-day glance for the current program week (written by Claude) |
| `CLAUDE.md` | Behavior instructions for Claude Code |
| `README.md` | This file |
| `LICENSE` | MIT |

---

## Dash setup (one-time)

The dash is just `index.html` + the two JSON files in this repo. To put it on the web:

1. Repo **Settings → Pages**
2. Source: **Deploy from a branch**
3. Branch: `main` (or whichever branch you merge to) / `/(root)`
4. Save → wait a minute → open the Pages URL

No secrets, no workflow, no build. Every morning Claude writes the fresh JSON, commits it, and the dash picks it up on the next load.
