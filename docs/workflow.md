# Generate, log and verify

## Read only relevant inputs

Start with `program.md`, `state/block.json` and `state/recovery.json`. Lifting needs today's table, ramp/return, lift progression and `state/lifting.json`. Running/cycling needs endurance/run progression and `state/running.json`. Read assessment/adjustment rules when a test, plateau, decline, return or fatigue flag applies. Use `state/baseline.md` for initial calibration. Search specific comparable sessions in current logs; do not load old history routinely.

## Generate the workout

1. Resolve the requested date in America/New_York. Derive week from October 26, 2026; earlier dates are Pre-block. After January 3, review before prescribing another block. Calendar rollover changes date fields, not stage or recovery clearance.
2. Use one state snapshot for both caches. Reconcile newer actual reports first. Apply symptoms/local restrictions and global recovery → saved return/assessment limits → achieved stage/calendar ceiling → valid progression. Lowest limit wins. Resolve carried pace credit at its first eligible opportunity before new progression.
3. Calculate effective sets/dose after omissions, cuts, trials and reductions. Entry stage A with M6/T7/L1 omitted gives Mon/Wed/Thu/Sat/Sun **9/7/10/6/9 = 41**. Stage advancement does not restore them. October 25 remains rest; first leg session is November 1.
4. Give only effective work: slot, ordered exercise, sets, reps, load, RIR, rest; or exact endurance work/recovery/pace/effort. Matching lifts inherit previous working weights as authorized by the athlete. For `carried_unvalidated` loads, read the dated source and adjust to today's reps/RIR before prescribing; explain material changes. A carried 160 lb incline baseline is not evidence for 6–8 reps at that weight. Derive back-offs from today's effective top-set load and select Thursday's load independently. New/unmatched lifts require calibration to the rep/RIR target. Never invent completed weights.
5. Explain why this date/stage selects the workout. For each material hold/increase/reduction/omission show **dated same-slot actual → rule → decision**. Distinguish first exposure, historical non-comparable references and pending evidence. Unchanged rows may share one explanation.
6. Audit the adaptation: matching source date/setup, all required sets/effort, qualification count, recovery, stage/return/test eligibility, preserved local limits and no cancelled credit reused. If evidence is missing, say `pending`; do not certify it correct. Fix a mismatch before writing and record the correction.
7. Write current-date daily and seven-day current-week caches using [dashboard.md](dashboard.md). Build Watch files only for actually prescribed outdoor runs. Label requested future previews with their real date; logging never silently advances today.

## Record actuals and decisions

- Lift: load/reps/RIR per set and slot. Run: each rep's average pace, final RPE, reported distance and next-day recovery. Bike: minutes/effort. Symptoms: reported observations only. Ask once for decision-critical missing values; otherwise `n/r` in prose or null in JSON. HR/cadence and technique narration are not required.
- Append dated `Hybrid v11 Wn` actuals to the relevant history stream. Store the effective prescription alongside actuals or reference its durable dated ledger entry; an overwritten cache must not erase what was prescribed. Record every heavy single exposure.
- Append numbered carried decisions to `history/adjustments.md`: source actuals, rule file/heading, previous → next dose/load, and pending gates. A hold cites the unmet gate. IDs increase after #429.
- Update relevant slot/run state and current-week outcomes. Completion can coexist with pending classification. Dashboard ranges/placeholders are not actual values; exact athlete-confirmed completions are acceptable.
- Follow run rules for missing recovery: unresolved ordinary evidence becomes no-count at the next corresponding run and clears dependent credit, without inventing poor recovery. Missing manageable/return/observation answers hold only dependent decisions. Silence cannot clear injury or diagnose fatigue.
- At calendar week close, append outcomes, effective doses and manageable/recovery evidence to `history/weekly-summary.md`; retain unresolved gates. Do not mark unreported sessions done.
- Regenerate affected caches from reconciled state. Parse JSON; verify dates, links, all effective sets/doses and adaptation evidence; persist state/logs/caches together. Verify publishing before claiming it succeeded.

## Compact state

`state/lifting.json` has all 33 named slots. Overlay each stored slot on `slot_defaults`, an explicit common empty record. Missing overrides inherit defaults; **never reset populated fields**. Prescription sets/reps/RIR/rest derive from day tables and active gates. Null load is uninitialized, including bodyweight/assisted slots until their convention is established.

At first exposure, store load/units, equipment/setup and per-hand/per-arm/assistance convention. `last_actual` points to a dated log. Maintain comparable first-set anchors, qualification/exposure counts, trial/cut state, decline cases and handled windows when relevant. Ab omissions remain in recovery state. Never borrow another slot's credit.

Carried loads use `load_status: carried_unvalidated` and a `load_source` key in `carryover_sources`. They are known prior working weights, not new-block actuals. Preserve source dates and ambiguous apparatus notation. Once an actual establishes the effective load in that slot, record it and change status to `established`; stage/progression gates still apply. Do not reset established loads from the carry-over map on later reads.

Before return work, save pre-interruption reference, reason, initial/active limits and pending validation. Before fatigue reduction, save response dates, observation doses/evidence and effective normal-dose snapshot. Temporary work never erases return limits; repeated reduction never halves an already reduced prescription. Carried run awards retain source IDs/pace/minutes/format, assessment week, status and dated use/cancellation. Empty fields do not authorize reconstructing cancelled credit.

Adoption is once per stable block ID. Program version edits preserve actuals and migrate changed fields, never re-bootstrap. Result key `baseline-5k-reported-2026-10-24` is logged once. Future completed blocks may be archived verbatim with a small carry-forward.
