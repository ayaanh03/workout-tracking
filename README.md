# Workout Tracking

Two markdown files + a tiny read-only dash, all driven by Claude Code chats. No backend, no build.

- **`program.md`** — the prescribed 25-week Sub-20 5K + hypertrophy program. The plan.
- **`Tracker.md`** — what's actually been done: status, current working loads, carry-forwards, lifting/cardio logs. The record.
- **`index.html`** — a static, mobile-friendly view of today's brief + the week ahead. Renders `latest-workout.json` and `week-ahead.json`, both written by Claude.

`CLAUDE.md` tells Claude how to behave in this repo.

---

## How it works

**Morning:** ask for the workout.

> "what's today"

Claude reads `program.md` + `Tracker.md`, figures out the week / phase / day, applies current working loads and any carry-forward flags, and outputs a tight brief: intro line, lift table (sets × reps × load × RIR × rest × cue), warmup, cooldown. Cardio gets its own block — flags, workout, targets, cues.

**Post-session:** dump what you did.

> "Hyp A done. Incline 135×5/5/5 RIR 3/2/2. Lat raise 25×12 across RIR 3. Preacher 50×10 across RIR 4/3/2. Pushdown 50×12 across RIR 4/3/2…"

Claude appends a structured entry to `Tracker.md`, updates Current Working Loads, adds/resolves entries in Adjustments/Carry-forwards, marks the Weekly Summary, logs SI status if reported, then commits and pushes. The next morning's brief reads the new state.

That's the whole loop. Each session feeds context into the next.

---

## The program at a glance

25-week Sub-20 5K plan + 2×/wk hypertrophy. Phases: **Reset → Base → Build → Sharpen → Taper**, race day Sat Oct 24, 2026.

| Day | Session |
|---|---|
| Sun | Off / SI prehab |
| Mon | Z1 easy run + strides |
| Tue | Threshold + Hyp A (≥6h gap) |
| Wed | Z1 easy run |
| Thu | Z1 easy or rest |
| Fri | Quality (T or VO2max) |
| Sat | Long run + Hyp B (≥6h gap) |

Full prescription in `program.md`. Current execution state in `Tracker.md`.

---

## File map

| File | Purpose |
|---|---|
| `program.md` | 25-week plan (prescription, source of truth) |
| `Tracker.md` | Execution log: status, current loads, carry-forwards, lifting/cardio logs |
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
