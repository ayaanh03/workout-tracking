# Dashboard and workout files

`index.html` displays prepared JSON. The assistant applies the program rules and writes state, logs and caches together; the page does not calculate progression. Keep chat and dashboard aligned: **why this day, exact effective workout, adaptation check**. Omit technique, evidence essays and routine lifting warmup/cooldown text.

## Daily cache

`latest-workout.json` uses plain text strings, never embedded Markdown/HTML:

| Field | Shape / meaning |
|---|---|
| `generatedAt` | Actual generation timestamp with `America/New_York` offset, including DST |
| `week`, `day`, `date`, `phase`, `sessionName` | Strings; date is athlete-local ISO; `Pre-block` before October 26, then W1–W10 |
| `why` | String array: session/stage selection and relevant gates; concise |
| `intro` | String array: current constraints, normally empty or one line |
| `lift` | `null` or `{table, lastWeek?}` |
| `lift.table` | Rows `{exercise, setsReps, load, rir, rest}`; all strings. Optional `slotId` for identity |
| `lift.lastWeek` | Optional `{label, table}` with dated same-slot actual rows `{exercise, load, reps, rir}` |
| `cardio` | `null` or `{workout, warmup, cooldown, flags?, targets?, workoutFile}` |
| `cardio.targets` | Optional `{pace, rpe}` strings; no mandatory HR/cadence/power targets |
| `adaptation` | Rows `{exercise, previous, decision, reason}`: dated actual evidence, hold/increase/reduce/omit/calibrate decision, and applicable rule |
| `currentLoads` | Rows `{exercise, load, lastVerified, note}`, optional `slotId`; one per independent active slot |

Use `setsReps: "2×8–12"` with an integer set-count prefix. Include only effective work, preserve separate incline top-set/back-off rows, and show unknown loads as `Calibrate`. Omitted abs are absent from the workout table; their restriction remains in state and the adaptation check. A literal zero RIR is `"0"`. Historical references do not become comparable new-block actuals; omit `lastWeek` until relevant actuals exist. If no work is prescribed, both modalities are `null`, with the reason shown.

The adaptation check must expose uncertainty: `previous: "First exposure; no comparable actuals"` and `decision: "Calibrate"` are valid. Do not label a prescription correctly adapted when the required performance or recovery evidence remains unknown. Include the affected date/slot, actual reps/RIR or pace/effort/recovery, and the gate that passed, failed or remains pending.

Wednesday/Saturday cardio says bike **after lifting**; `workoutFile` is null. Runs retain exact warmup, work, between-rep recovery, cooldown and RPE cap. Lift cues/warmup/cooldown and cardio cues are not rendered.

## Week cache

`week-ahead.json`: `{generatedAt, week, phase, summary, days}`. `days` has exactly seven consecutive Monday–Sunday rows `{date, day, session, note, status}`. Both caches describe the same current week and state snapshot; timestamps match when written together.

Statuses: `done` only for reported completion; `today` for unresolved current-day work; `upcoming` for future work; `skipped`, `rest` or `unreported` for supported past outcomes. Before the start, keep the transition week and Sunday October 25 rest. Logging never silently replaces today with tomorrow's preview. A calendar rollover does not advance stages or clear recovery gates.

## Lift logging

Drafts stay in the browser by date. Load fields are prefilled only for initialized loads; reps/RIR remain blank with targets as placeholders. **Confirm exact targets** is the athlete's explicit confirmation of the numeric targets completed; it fills only exact numeric values, never rep ranges or compound RIR. Review all pasted values as actuals. Missing values stay `n/r`, unknown load becomes `?`, and `Calibrate` never becomes a logged weight.

A warning marks drafts from a different prescription. Preserve entered actuals before resetting; compare the dump with the dated effective prescription. Copy/share only prepares text for chat, never writes the repo.

## Apple Watch export

For actual outdoor-run briefs use `tools/workoutgen.py` (its docstring defines syntax). Write `runs/{date}.txt`, build its `.workout`, decode-check it, then set `cardio.workoutFile` to that relative path. Bike, rest and treadmill-only work use null. Unsupported exports must not leave a download link.

- Match every goal to the brief; choose a concrete allowed cooldown duration and include it in planned mileage.
- Encode recoveries **between** reps only: N−1 work/recovery pairs, then final work.
- Work alerts may use current target ±5 s/mi; initially Tuesday 6:45–6:55 and Friday 7:20–7:30/mi. Effort caps still govern.
- Easy running is conversational, without mandatory legacy pace alerts. Recoveries have no pace alert. Add no HR/cadence/power targets, strides or sub-minute work.
- A test is a 5 km work segment; never force the aspirational goal pace as an alert.

Validate JSON types, dates, slot separation, effective sets, pace/RPE, complete-week mileage and file links before writing caches. After encoder edits run `python3 tools/test_workoutgen.py`; ordinary content changes need JSON/link/render checks, not new tests.
