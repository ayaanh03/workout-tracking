---
schema_version: 1
block_id: hybrid-2026-10-26
program_id: hybrid-2026-10-26-v11
program_version: "11.0"
based_on_program_version: "10.0"
repository: ayaanh03/workout-tracking
canonical_path: program.md
prepared_on: "2026-10-24"
timezone: America/New_York
block_start_date: "2026-10-26"
block_end_date: "2027-01-03"
block_weeks: 10
baseline_5k:
  distance_m: 5000
  elapsed_seconds: 1290
  display_time: "21:30"
  status: athlete_reported_final_result
  reported_on: "2026-10-24"
  performed_on: null
  scheduled_event_date_context: "2026-10-24"
  course_conditions: null
  race_rpe: null
  next_day_recovery: pending
initial_targets:
  tuesday_pace_seconds_per_mile: 410
  friday_pace_seconds_per_mile: 445
  tuesday_final_rep_rpe_cap: 8
  friday_final_rep_rpe_cap: 7
  easy_guide_seconds_per_mile: [510, 570]
  running_miles_per_week_ceiling: 15
goals:
  five_k_seconds: 1080
  incline_barbell_single_lb: 225
bootstrap_once:
  lifting_stage: A
  last_tolerated_stage: null
  tuesday_normal_work_minutes: 12
  friday_normal_work_minutes: 18
  successful_normal_run_levels: null
  progression_counts: 0
  comfortable_pairs: []
  pending_carried_adjustments: []
  first_in_block_test_week: 5
  first_in_block_test_attempted: false
  direct_ab_review_slots: [M6, T7, L1]
---

# Hybrid Training Program v11.0

**One authoritative agent input for `ayaanh03/workout-tracking`.** The complete prescription, progression rules, starting performance, adoption instructions, and dashboard contract are in this file. No companion change document or previous program is required.

**Prepared:** October 24, 2026. **Planned block:** October 26, 2026–January 3, 2027, America/New_York.

**Confirmed input:** the athlete reports a final **21:30 5K**. This is a reported result, not an independently verified timing record. The report is dated October 24; the actual event date, splits, conditions, RPE, warmup/cooldown, and recovery are not supplied. The repository had an October 24 race scheduled; retain that as context without fabricating missing actuals. Exact 21:30 is not “sub-21:30.”

**Current authority:** the exercise tables are the baseline; adoption restrictions, symptoms, recovery, ramp, return, assessment, and recorded adjustment rules determine the effective workout. This file replaces the legacy 25/27-week race prescription and conflicting training defaults in `CLAUDE.md`, `README.md`, `Tracker.md`, and older program documents. Keep the repository's ordinary file-handling, append-only history, and publishing workflow. The current athlete's explicit instructions and newer actual reports take precedence.

**Changes from the v10 source:** use the reported 21:30 baseline; recompute both run targets and mileage illustrations; provide an explicit new-block bootstrap and the real repository's cache/Watch contract; carry forward unresolved current restrictions. The selected lifts, baseline sets, progression rules, and ten-week calendar remain the approved v10 structure. Earlier exercise alternatives were discussion options and have not been adopted.

The YAML front matter is a machine-readable index and immutable starting snapshot. It is not a second live tracker: after adoption, current loads, targets, stages, and flags come from this program's rules plus the persisted state in `Tracker.md`. Never reset live state from the bootstrap on every read. If a constant or instruction appears inconsistent, resolve the inconsistency before generating the affected workout; do not choose a convenient value silently.

## 0. Agent entry point and adoption

### What this file powers

The current `index.html` renders **`latest-workout.json` and `week-ahead.json`**. It does not parse this Markdown, decide progression, or write training records. The agent reads this file and `Tracker.md`, applies the rules, logs reports, and generates the two caches using section 11. Existing history and Watch export files remain derived records; they are not extra program inputs the athlete must maintain.

### Adopt once, preserve history

At the first interaction using this program, check `Tracker.md` for the matching program ID, `adoption_status: complete`, and all required state fields. Reuse the initialized state only when all three checks pass. Otherwise start or resume adoption before selecting a workout. Set `adoption_status: in_progress` and retain step-completion markers. Resume partial adoption by filling missing state only; never reset actual new-block work, repeat a history migration, or duplicate a baseline result just because the procedure was interrupted:

The stable `block_id` is `hybrid-2026-10-26`, separate from the versioned program ID. A future version change within this same block requires a state-preserving migration; it does not authorize a fresh bootstrap or erase actuals/earned state. The first-adoption steps below apply only to state that has not already been established.

1. Preserve the previous block's current status, loads and dated actuals in the existing append-only history/ledger workflow. Do not delete history, rename old weeks, or reuse their progression credit. Keep adjustment IDs globally monotonic.
2. Record the athlete-reported 5K as 5,000 m in 1,290 seconds, reported October 24, with unreported fields `n/r` or `null`. Preserve the old prescribed race details as plans, never as completed actuals. Use a stable result key, `baseline-5k-reported-2026-10-24`, to avoid logging the same report twice. The report is enough to initialize pace; no additional test is required to start.
3. Store this program ID/version and the start date. W1 means **October 26–November 1** in this block, not legacy W28. Qualify new history headings with the program ID or “Hybrid v11 Wn” so two blocks' W1 records cannot collide.
4. Initialize lifting at **stage A**, with no completed new-block stage. Prior lifting experience does not skip this program's ramp. Initialize the 33 exercise slots independently; no borrowed qualification streaks, plateau windows, decline anchors, extra-set trials, or queued load bumps. Preserve actual unresolved restrictions separately.
5. Initialize Tuesday at **3 × 4 minutes, 6:50/mi**, and Friday at **3 × 6 minutes, 7:25/mi**, with zero hit/miss counts, no comfortable pair, no carried award, and no successfully completed new-block normal level yet. The pre-block result supplies initial pace evidence; it is **not** section 6 rule 6's in-block reset. Thus absence of a new-block successful level does not by itself reduce the initial W1 prescription. Use lower calibration/return doses when actual readiness or another rule requires them.
6. The baseline race does not consume the first optional W3/W4/W5 assessment. Initialize that choice at W5, unused. Keep W10 as the other optional opportunity. Do not infer an illness/gap return, poor recovery, or a global-fatigue flag merely because a new block begins.
7. Resolve the carried restrictions below, then generate the current brief and week cache from the same state snapshot. Check whether any newer repository report changes this adoption snapshot before carrying it forward. Set `adoption_status: complete` only after all required state is initialized and the matching caches validate; commit the reconciled state/history/caches together. Presence of a program ID alone is never an adoption-completion marker.

### Transition dates and readiness

- **Before October 26:** this block has not begun. The old race result can be logged, but do not prescribe a new-block Saturday lift or Sunday leg workout on October 24/25.
- **Sunday October 25:** retain the existing post-race rest day. It is not W1 Legs.
- **Monday October 26:** planned W1 Upper A, stage A, subject to actual recovery and local restrictions.
- **Tuesday October 27 / Friday October 30:** the first planned interval sessions. Their paces are initial targets, not an obligation to force the effort caps.
- **Sunday November 1:** the first planned leg session.
- Ask once at the next relevant interaction for decision-critical current/post-race recovery and the unresolved ab status. Until reported, store recovery as pending; do not declare the race well tolerated. Unknown recovery blocks progression and any clearance dependent on it. For the first post-race hard run, confirm current recovery before issuing a hard-work prescription; defer it if that necessary readiness check remains unanswered. Other appropriate training need not stop. Do not fabricate normal recovery or automatically diagnose fatigue.

### Restrictions that survive adoption

The repository snapshot reviewed October 24 contains these current items:

| Item | Evidence in the current tracker | Adoption action |
|---|---|---|
| Left lower-ab strain | Last reported improving but unresolved; old direct-ab work limited to bodyweight decline crunches until resolution | Keep baseline M6/T7/L1 in this file, but temporarily **omit all three** pending a documented symptom-informed review. The new cable-crunch and hanging-raise setups have not been established as tolerated. Do not silently substitute decline crunches or infer clearance from finishing a 5K. |
| Left Achilles history | Reactive-tendon flag; last explicitly clean post-calf response dated October 12 | Preserve the dated history and ask for current status when decision-critical. The old cycle's calf taper expires with that cycle. Use calibrated new-movement loading and the current symptom rules; do not copy the old seated-calf load into leg-press calf raises or label the tendon resolved. |
| Other historical watches | No current new report establishing a revived restriction | Do not reactivate retired elbow/patellar watches solely because old history mentions them. Apply the current symptom rule if new symptoms are reported. Forearm work remains ordinary gradual exposure. |

The temporary ab omissions are recorded local restrictions, not a new exercise selection or a failed adherence week. With all three still omitted, stage-A effective totals are **Mon 9, Wed 7, Thu 10, Sat 6, Sun 9 = 41 sets**; the unchanged unrestricted baseline is 47. No catch-up work. Recalculate later-stage/reduced totals from the actual slot vector. A week can satisfy the manageable gate with the documented omissions if the prescribed appropriate work and actual recovery meet the criteria. Restoration needs an explicit review and the section 8 local-restoration process; stage advancement alone does not restore an omitted slot.

### Historical loads: references, not prescriptions

Read the current tracker for the freshest actuals. The legacy incline, pulldown, chest-supported row, dumbbell laterals, unilateral preacher, and rope pushdown records may inform initial calibration **only when equipment, load notation, range, and setup match**. Reverse-pec-deck references require confirming the old rear-delt fly used that machine. M1a, M1b, and T1 get separate loads; all four lateral slots get separate records.

Retire the old training max, Hyp A/Hyp B gates, “bump next” credit, and old I/T/R/M pace bands. Recalibrate to this program's stage-specific reps/RIR. Do not transfer seated-calf stack numbers to a leg-press calf raise, decline-crunch loads to cable crunches, or an old taper single into a new M1a progression anchor. New movements start `load: uninitialized`; do not invent starting weights. Historical sessions can appear as dated references, explicitly marked non-comparable, but cannot become a first exposure in this block.

### Conflicting legacy defaults explicitly replaced

- Use section 2's five-lift/two-run schedule; Thursday and Sunday are no longer automatic rest days. There are no standalone easy runs or strides in this block.
- Use section 3's rests and warmups: at least two minutes between working sets. Do not import the old 60–90-second isolation rest default or fixed warmup loads.
- Use the current pace and RPE caps; do not request or manufacture HR/cadence targets. Historical heart rate/power may remain recorded observations.
- A queued bump passes all current stage, recovery, return, assessment and symptom gates before use.
- Replace “no-news-is-clean” and automatic status filling with section 8's pending-observation rules. Ask one compact prompt for decision-critical missing information; missing values remain unknown.
- Logging a session does not advance today's calendar date. Rebuild the actual current-day cache; a requested tomorrow preview must identify its future date explicitly.
- Use the 33 new slot IDs and section 11's cache contract. Legacy section numbers and Hyp A/Hyp B labels do not select this block's prescriptions.

## How to use this program

1. Start with the achieved ramp stage in section 4; the full tables in section 3 are not the W1 prescription.
2. Apply symptom, recovery, return, and assessment overrides before ordinary progression.
3. Use separate records for each lifting slot and each run day. Progression is earned from comparable work.
4. Treat a plateau as a review trigger. Declining performance never directly qualifies for more sets.
5. If a session is missed, skip it. There is no catch-up work.

### Athlete card (summary; the numbered sections govern)

**Week:** Mon Upper A · Tue run · Wed delts/arms + easy bike · Thu Upper B · Fri run · Sat delts/arms + easy bike · Sun legs.

**Log:**

- **Every lifting set:** load, clean reps and RIR.
- **Every run:** each rep's average pace and the final rep's RPE. The next morning, record whether recovery was normal or poor.
- **Every ride:** minutes and effort.
- **End of each ramp, return or observation week:** was it manageable? That means technique stable, soreness settling, no worsening joint or tendon symptoms, and later priority sessions fine.

**Always:**

- Missed work is skipped, never doubled.
- Pain that changes technique or gait: stop or modify that movement now.
- Only the nine marked final sets may use `0–1 RIR`, and only in eligible normal stage D. All other sets follow their listed RIR targets.
- Run at an even pace. Stop at the RPE cap rather than forcing the target.
- Report unusual fatigue that carries into later sessions.
- Review run targets weekly. From W3, two qualifying comfortable workouts can earn a small pace increase while work minutes stay unchanged; an all-out test is optional.

The logging workflow applies the program rules and writes the next prescription. The repository dashboard displays that prepared brief. Missing recovery or manageable-week answers remain pending; they are never inferred from silence.

## 1. Goals, inputs, and constraints

### Priority order

1. **Hypertrophy:** side delts, biceps, triceps and overall arms, back, abs, then calves. Legs get conservative work to regain lost size. Incline pressing is the chest work.
2. **Strength:** a technically consistent 225 lb incline barbell single.
3. **Running:** progress toward an 18:00 5K without compromising goals 1–2, and within the running-volume limit.

These are starting allocations to evaluate. They are not proven personal optima. No deadline or probability is attached to either performance goal.

Going from the reported 21:30 to 18:00 means 3:30 less race time and about 19.4% higher average race speed (16.3% less race time). VDOT, if logged, is a race-performance score rather than measured VO2max. [R9]

### Reported performance and provisional planning inputs

The 5K result is athlete-reported. The bodyweight and incline estimate remain provisional planning inputs, not newly measured values:

- **5K result: 21:30**, athlete-reported October 24, 2026: **4:18/km; approximately 6:55/mi**. Use it as the initial performance baseline. The actual event date, conditions, splits, race RPE, and post-race recovery are unreported; do not infer them from the old race prescription.
- bodyweight 157 lb
- incline estimated 1RM ≈185 lb, from a rep set

Week 1 starts Monday, October 26, 2026. If the start moves, shift the whole calendar and keep the weekday order. Use `America/New_York`.

The 185 lb estimate does not set mandatory working weights. Calibrate loads from the prescribed reps and RIR. Record one bench angle and keep it fixed; use 30° if the original angle is unknown.

### Preserved preferences

- **Schedule**

  - Five lifting days, with runs on their own Tuesday and Friday.
  - No run shares a day with lifting or cycling. Cycling only follows the Wednesday and Saturday lifts.
  - Seven training days is the framework. A needed day off is allowed, and missed work is not debt.
- **Running**

  - No strides, and no planned running work bout shorter than one minute.
  - No standalone easy runs. Easy running only appears in warmups, recoveries and cooldowns.
  - Running stays at or under **15 miles per week**. This is a ceiling, not a target.
  - **Distance rule (confirmed by the athlete, October 21, 2026):** 5K is the longest race distance. A whole session may total more than 5 km.
- **Lifting**

  - DB lateral raises only.
  - Keep the unilateral machine preacher curl, rope cable hammer curl, leg-press calf raises, barbell incline on both pressing days, seated cable rows, and back extensions instead of RDLs.
  - Keep cable reverse and wrist curls as standard gradual-exposure accessories. They remain subject to the symptom and recovery rules.
  - At most one direct triceps exercise on any lifting day.
  - At least two minutes between working sets. No supersets are required.

## 2. Weekly schedule

| Day | Session | Main purpose |
|---|---|---|
| Monday | Upper A | Heavy incline, priority upper-body work, direct triceps |
| Tuesday | Running intervals | Controlled work near current 5K pace |
| Wednesday | Delts and arms A, then easy cycling | Priority muscles at restrained effort before Thursday |
| Thursday | Upper B | Incline volume, arms, back, abs |
| Friday | Longer running intervals | Sustained work near threshold pace |
| Saturday | Delts and arms B, then easy cycling | Priority muscles; forearm build-up |
| Sunday | Legs, abs, calves | Regain leg size with a conservative allocation |

Rules for rescheduling:

- No hard run the day after direct calf or leg lifting.
- No direct triceps work the day before an incline session.
- If a safe rearrangement isn't possible, skip the missed session and resume the schedule.

These are fatigue-management defaults for this program, not universal biological laws.

Exercise order:

- Incline stays first on Monday and Thursday.
- Otherwise follow priority order, and interleave obvious local demands where practical.
- Shared stabilizers don't create a literal ban on adjacent exercises.
- Curls before pulls is accepted: it costs some elbow-flexor fatigue in exchange for prioritizing arms. Straps handle grip, not that fatigue.

### Planned phases

| Phase | Weeks | Dates |
|---|---|---|
| Ramp | W1–W3 | Oct 26 – Nov 15, 2026 |
| Build | W4–W9 | Nov 16 – Dec 27, 2026; default first optional 5K Fri Nov 27, or deliberately move it to W3/W4 under section 7 |
| Reduce | W10 | Dec 28, 2026 – Jan 3, 2027; optional 5K test Fri Jan 1 |

These are calendar labels. The achieved stage and any active recovery/return restriction determine the actual prescription.

## 3. Lifting sessions

**Read the ramp in section 4 before using these tables.** Table RIR targets apply from ramp stage D, planned for W4. An earlier achieved stage, or a reduced week, overrides them even if the calendar is further ahead.

- **RIR:** the additional clean reps you could still do with the same range of motion. It is an estimate.
- **"last 0–1":** the final set of that exercise ends with 0–1 clean reps left. A failed repetition is not required. Stop if technique changes or symptoms worsen. This applies only in normal stage D, never in reduced/return work or while a fatigue response is active. A local rollback suspends it in the affected slot until explicitly reviewed.
- No exercise uses forced reps or partials after failure.

Technique:

- Use a stable range of motion and setup.
- M5 is a conventional bilateral lat pulldown. T8 is a straight-arm cable pulldown and may also use both arms together; it does not require one-arm execution. WE2 remains unilateral as prescribed.
- **Calf raises:**

  - controlled reps
  - a comfortable bottom stretch
  - secure foot placement and safety stops
  - knees straight without forcefully locking them
  - a suitable calf machine if the leg press can't provide secure positioning
- **Back extensions:** hinge at the hips with a controlled torso.

### Monday: Upper A

| ID | Exercise | Full-volume sets × reps | Normal RIR | Rest |
|---|---|---|---|---|
| M1a | Incline barbell bench, top set | 1 × 4–6; **W4 and W9: heavy single (section 5)** | 2; single 1–2 | 3–4 min |
| M1b | Incline barbell bench, back-offs | 2 × 6–8 | 2–3 | 3–4 min |
| M2 | Incline DB curl | 2 × 8–12 | 1–2; last 0–1 | 2 min |
| M3 | DB lateral raise | 4 × 12–20 | 1–2; last 0–1 | 2 min |
| M4 | Overhead cable triceps extension | 3 × 10–15 | About 2; last 0–1 | 2 min |
| M5 | Lat pulldown | 2 × 8–12 | About 2 | 2–3 min |
| M6 | Cable crunch | 3 × 10–15 | 1–2 | 2 min |
| M7 | Chest-supported row | 2 × 8–12 | About 2 | 2–3 min |

**Full-volume total: 19 working sets.** Straps may be used on the pulls.

### Wednesday: Delts and arms A

| ID | Exercise | Full-volume sets × reps | Normal RIR | Rest |
|---|---|---|---|---|
| WE1 | DB lateral raise | 4 × 12–20 | 2–3 | 2 min |
| WE2 | Unilateral machine preacher curl | 2 × 8–12 per arm | 2–3 | 2 min |
| WE3 | Reverse pec deck | 2 × 12–20 | 1–2 | 2 min |
| WE4 | Rope cable hammer curl | 2 × 10–15 | 2–3 | 2 min |
| WE5 | Leg-press calf raise | 4 × 10–15 | 1–2 | 2 min |

**Full-volume total: 14 working sets, then the bike.**

- Wednesday lateral and curl effort is deliberately restrained, and there are no "last 0–1" sets, because Thursday repeats those areas.
- Rear delts separate the two curl exercises.
- The weaker arm sets the preacher load, and the stronger arm matches its clean reps.

### Thursday: Upper B

| ID | Exercise | Full-volume sets × reps | Normal RIR | Rest |
|---|---|---|---|---|
| T1 | Incline barbell bench | 3 × 6–8 | 2–3 | 3 min |
| T2 | Cable curl | 2 × 10–15 | 1–2; last 0–1 | 2 min |
| T3 | DB lateral raise | 4 × 12–20 | 1–2; last 0–1 | 2 min |
| T4 | Pull-up | 2 × 6–12 | About 2 | 2–3 min |
| T5 | Cable pushdown | 3 × 10–15 | About 2; last 0–1 | 2 min |
| T6 | Seated cable row | 2 × 8–12 | About 2 | 2–3 min |
| T7 | Cable crunch | 3 × 10–15 | 1–2 | 2 min |
| T8 | Straight-arm cable pulldown | 2 × 10–15 | 1–2 | 2 min |

**Full-volume total: 21 working sets.**

- Calibrate T1 independently from M1a and M1b. Dated old-block loads are references only, subject to section 0.
- Use pull-up assistance if needed to stay in range at the intended RIR. Add load only when the progression rule is met.

### Saturday: Delts and arms B

| ID | Exercise | Full-volume sets × reps | Normal RIR | Rest |
|---|---|---|---|---|
| S1 | DB lateral raise | 4 × 12–20 | 1–2; last 0–1 | 2 min |
| S2 | Incline DB curl | 2 × 8–12 | 1–2; last 0–1 | 2 min |
| S3 | Overhead cable triceps extension | 3 × 10–15 | About 2; last 0–1 | 2 min |
| S4 | Reverse pec deck | 2 × 12–20 | 1–2 | 2 min |
| S5 | Cable reverse curl | 1 × 15–20; from W6 if eligible, 2 × 15–20 | 1 set: 3–4; 2 sets: 2–3 | 2 min |
| S6 | Cable wrist curl | 1 × 15–20; from W6 if eligible, 2 × 15–20 | 1 set: 3–4; 2 sets: 2–3 | 2 min |

**Full-volume total: 11 core sets, plus 2 or 4 forearm sets, then the bike.** There is no Saturday calf work.

**Forearm rules:**

- These are standard accessories, subject to the same modification/stop rules as other work.
- Stage A and reduced weeks: none.
- Stage B onward: one set each at 3–4 RIR.
- At the first normal stage-D week on or after W6, with no active fatigue or return restriction, ask once: *Did elbow symptoms worsen after starting this work?* If no, use two sets each at 2–3 RIR. If yes or uncertain, retain one each for this block and review the aggravating work. Do not force either exercise through worsening symptoms.
- Do not take these sets to failure. Load/repetition progression follows section 5, with two qualifying exposures per slot.
- This is a chosen exposure progression, not a diagnosed rehabilitation protocol or proof that more sets improve elbow health. Loads and reps can progress even when sets stay fixed.

### Sunday: Legs, abs, and calves

| ID | Exercise | Full-volume sets × reps | Normal RIR | Rest |
|---|---|---|---|---|
| L1 | Hanging leg raise | 3 × 8–15 | 1–2 | 2 min |
| L2 | Leg-press calf raise | 4 × 10–15 | 1–2 | 2 min |
| L3 | Hack squat | 3 × 6–10 | About 2 | 2–3 min |
| L4 | Seated leg curl | 3 × 8–12 | About 2 | 2 min |
| L5 | Leg extension | 3 × 10–15 | 1–2 | 2 min |
| L6 | Loaded 45-degree back extension | 2 × 8–12 | About 2 | 2 min |

**Full-volume total: 18 working sets.**

- Curl the pelvis up on leg raises; an uncontrolled swing is not a rep.
- Use a captain's chair if hanging grip or elbows are limiting.

### Warmups

- **General:** about five minutes of comfortable cycling or rowing if helpful.
- **First loaded movement:** progressive practice sets.
- **Incline:** empty bar, a light set, a moderate set, then an optional short set near working load, without fatigue.
- **Heavy single (W4/W9):** bar × 10, then approximately 50% × 5, 70% × 3 and 85% × 1 of the planned single. Round to practical loads, avoid duplicate steps, and keep these preparatory sets easy.
- **Hack squat:** its own progressive warmup, even though abs and calves come first.
- **Curls and triceps:** one light rehearsal set for the first curl or triceps movement as needed.

Warmups do not count toward working-set totals.

## 4. Ramp, set accounting, reduced work, and return

### Achieved stages

| Baseline exercise allocation | Stage A, planned W1 | Stage B, planned W2 | Stage C/D |
|---|---:|---:|---:|
| 2 sets | 1 | 2 | 2 |
| 3 sets | 2 | 2 | 3 |
| 4 sets | 2 | 3 | 4 |

**Incline exception:** stage A uses M1a one set, M1b one set, and T1 two sets. Stage B onward uses M1a one, M1b two, and T1 three. Forearms follow their separate rule in section 3.

| Stage | Effort on core work | Advancement |
|---|---|---|
| A | About 3 RIR; calibrate loads | Complete a manageable week before B |
| B | About 2–3 RIR | Complete a manageable week before C |
| C | Full baseline sets, still about 2–3 RIR | Complete a manageable week before D |
| D | Session-table RIR, including eligible final 0–1 sets | Use normal progression while recovery remains acceptable |

A manageable week has stable technique, settling ordinary soreness, no worsening joint/tendon symptoms, and acceptable subsequent priority sessions. Otherwise repeat the stage or use the recovery rules if needed. The calendar never permits skipping C. During A–C, keep loads stable once effort is appropriate; adding sets already progresses the dose.

Single weeks do not move if D is delayed: skip the W4 single if not in normal D then. Apply the same eligibility check in W9. Never add a missed single later to catch up.

### Baseline weekly totals

| Day | A / planned W1 | B / planned W2 | C / planned W3 | D / planned W4–W5 | D / planned W6–W9 | Reduced from full baseline |
|---|---:|---:|---:|---:|---:|---:|
| Monday | 11 | 16 | 19 | 19 | 19 | 9 |
| Wednesday | 7 | 12 | 14 | 14 | 14 | 7 |
| Thursday | 12 | 18 | 21 | 21 | 21 | 10 |
| Saturday core | 6 | 9 | 11 | 11 | 11 | 5 |
| Saturday forearms | 0 | 2 | 2 | 2 | 4 if eligible; otherwise 2 | 0 |
| Sunday | 11 | 13 | 18 | 18 | 18 | 7 |
| **Total** | **47** | **70** | **85** | **85** | **87 if eligible; otherwise 85** | **38** |

These totals assume the unmodified baseline and the stated stage. They are not fixed targets after a cut, an approved addition, an omission, or an interruption. Warmups are excluded. Two unilateral sets per arm count as two sets for the trained muscle.

### Full baseline allocations

| Area | Direct or movement-specific weekly sets |
|---|---:|
| Side delts | 16 |
| Supinated curls | 8 |
| Hammer curls | 2 |
| Direct triceps | 9, plus pressing contribution |
| Back | 10, plus 4 separate rear-delt sets |
| Abs | 9 |
| Calves | 8 |
| Incline pressing | 6; one is a single in eligible W4/W9 |
| Quads | 6 |
| Hamstring/hip-extension movements | 5 |
| Forearms | 2 initially; 4 when eligible |

There are nine eligible final 0–1 slots before rollbacks or omissions. A set addition makes the new final set the only 0–1 set in that slot; it does not leave two final sets near failure. The listed direct/movement counts sum to 83 core sets, plus forearms. Indirect muscle contributions should not be counted again as additional working sets. Six incline sets are not six identical stimuli, particularly during single weeks.

### How recorded changes affect sets

For each slot, begin with the achieved-stage allocation in this file. In normal stage D, include any deliberately approved set addition. Apply persistent local limits last: an omitted slot stays omitted, and a set ceiling cannot be undone by a ramp increase or a volume trial. Such a ceiling stays until explicitly reviewed.

During return stages A–C, suspend extra-set trials and use the original stage allocation, capped by any persistent local restriction. Reintroducing a suspended trial after return requires a fresh review; it is not automatic.

### First-test week and W5

If recovered, continue the achieved lifting stage in W5. Only endurance is routinely reduced then. A first 5K in W3, W4, or W5 additionally omits that week's Wednesday calves. After an early test attempt, W5 uses Option B when recovered, with its usual achieved-stage calves; it does not include another test. If recovery is needed, use Option C instead.

| Achieved stage in the first-test week or W5, before other changes | No test | With test and Wednesday calves omitted |
|---|---:|---:|
| A | 47 | 45 |
| B | 70 | 67 |
| C or D, one forearm set each | 85 | 81 |

The planned Wednesday calf omission is an assessment override, not a persistent local cut or an incomplete stage week. It does not by itself block stage advancement; the completed prescription and actual post-test recovery must still satisfy the manageable-week criteria. If an early test is cancelled after calves were omitted, do not restore that work later. Calculate actual sets after all omissions and recorded changes.

An early test does not move or automatically cancel the W4 incline single. Its normal-stage-D and recovery eligibility rules still apply; if D is delayed, skip that single as already prescribed.

### Reduced lifting: W10 or an Option C period

First apply any new local rollback and any saved return-stage limit. An active global fatigue response also cancels unresolved added-set trials. Then take a snapshot of the **current effective normal prescription**: baseline plus adopted additions and any still-active approved trial, with existing local cuts applied. A pending return at A–C uses that stage's baseline allocation with local limits, not an old stage-D dose. A scheduled W10 reduction alone does not cancel a trial; the next-block review decides its future. Apply the following once:

- If a slot is omitted, it remains at zero.
- For other core slots, use `max(1, floor(current normal sets / 2))`.
- **Incline exceptions replace the halving rule:** use `min(current normal sets, 1)` for M1a and M1b, and `min(current normal sets, 2)` for T1. An omitted slot stays at zero.
- Forearms: zero.
- Use about 4 RIR, lowering weight as needed. No final 0–1 sets and no heavy single.
- A test additionally omits Wednesday calves.

Examples: five normal sets become two; six become three. From the unmodified full baseline, the result is **38 sets**, or **36** with Wednesday calves omitted. From unmodified stage A or B, it is **32 sets**, or **31** with that omission. Recalculate after persistent changes.

A repeated reduced period uses the same appropriate normal-dose reference; do not repeatedly halve the already reduced week. If a restriction becomes tighter, apply it immediately. Overlapping scheduled and fatigue reductions use one reduced prescription, not two stacked reductions.

### Return to ordinary work

- **After a planned W10 reduction without illness/fatigue:** the next block begins from the last tolerated stage, adjusted at review. This file does not prescribe a new block automatically.
- **After Option C for fatigue:** use the observation week in section 8. It controls the return and progression freeze; any stricter illness/gap limit still applies.
- **After illness or time away:** once ordinary training is appropriate again, count days from the pre-interruption last completed lifting session to the first attempted return. Use the first matching row. The reason for the break remains illness-related even after symptoms resolve.

  | Situation | Initial return stage |
  |---|---|
  | More than 28 days without lifting, for any reason | A |
  | Break unrelated to illness, 14 days or fewer | No special return week; resume the established stage, subject to existing restrictions |
  | Brief, fully resolved mild illness lasting no more than seven days, with seven days or fewer without lifting | C, or the last tolerated stage if lower |
  | Any other illness-related break of 28 days or fewer, or a non-illness break of 15–28 days | B, or A if B was never tolerated |

  If there is no established tolerated stage, start at A. These rows do not authorize training during ongoing illness or despite materially reduced capacity.

- **Preserve the return limit:** before recording the first return attempt, including reduced or Option C lifting, save the pre-interruption last-lift date, last tolerated stage, reason, and initial return stage. Keep the resulting return-stage limit active. Temporary sessions update actual dates but cannot erase it or recalculate it upward. A later interruption can require a stricter limit.
- **After a completed return week:** advance at most one stage from the stage actually completed, and only after an explicitly manageable week. A reduced week does not satisfy that gate. An appropriate completed observation week can satisfy it, with advancement waiting for fatigue clearance. After each authorized advance, update the active return-stage limit to the next stage; preserve the initial stage as history. Clear the lifting return restriction when entry to D is authorized, retaining all local and global restrictions. Continue this sequence to D; do not jump to an older pre-break stage. Review suspended trials before reintroduction.
- **Falling tolerance** without illness or a gap uses section 8's local or global response according to the pattern.
- Return work has no 0–1 sets or singles and earns no loading, stall, or running pace credit. Endurance follows section 6's own return levels.

These day thresholds and stage assignments are coaching defaults. Symptoms or materially reduced capacity can require less work or further time off. A missing manageable-week answer holds the current return stage under section 8.

## 5. Loading and progression

### Rules that apply to every lift

Actual technique, reps and RIR govern loading. A forecast never overrides them.

Each **exercise slot** keeps its own working load and progression record. For example, M3, WE1, T3 and S1 are four separate lateral-raise records.

1. Keep the same load while building reps within the range.
2. Increase by the smallest available increment once **all prescribed sets** reach the top of the range with stable technique and the full set count. Each set must be at its intended RIR or with more in reserve. A "last 0–1" set qualifies at 0–1 RIR or more in reserve.
3. Stop at the rep ceiling even if the load feels easy; that can qualify. Don't add unplanned reps or sets.
4. DB lateral raises and cable forearm curls need two qualifying exposures in the same slot before a load increase. Other lifts need one.
5. If the available increment makes the bottom of the rep range impossible at the intended RIR, use a smaller increment if one exists. Otherwise keep the old load and review the implement or rep range. Don't bounce between weights.
6. Reduce weight mid-session if needed and record it. A session that needed a load drop doesn't qualify the original load.

Ramp, reduced, return, changed-equipment, and temporarily shortened sessions do not count toward progression streaks or plateaus. An active fatigue response freezes discretionary progression. Reset progression streaks after a load, set-count, or effort-target change. Keep a saved prechange first-set reference for a trial when its first-set conditions remain comparable; section 8 defines that comparison. A load or first-set RIR change requires a new anchor. A planned recovery-to-observation return is allowed despite the progression freeze.

### Monday incline

**Top set M1a**

- 4–6 clean reps at about 2 RIR.
- Once six reps meet that standard, add 2.5 lb next Monday (5 lb if 2.5 isn't available).
- After an increase, calibrate rather than forcing four reps at excessive effort.

**Heavy single (W4 and W9, normal stage D only)**

- Replaces the M1a top set that day.
- **Eligibility:** no active fatigue/return restriction, no relevant worsening symptoms, and an appropriate recent comparable M1a estimate. Otherwise do the usual top set at the applicable effort, or modify/omit it under the symptom rule.
- **Planned load:** recent comparable M1a e1RM ÷ 1.1, rounded down to 5 lb, as an initial guide. Warmup response and clean execution govern; lower the plan when needed.
- **Execution:** one single at RIR 1–2, with clean technique and no grinding.
- If it was clearly RIR 3 or more, do one more single 5 lb heavier and stop there. The first single then counts as a warmup.
- **Record:** log every heavy exposure. The last single is the counted working set; an easier preparatory single still happened and must remain visible in the log. Do not treat the one-set table entry as proof that there was only one heavy exposure.
- **Effect on other records:** the single doesn't change the 4–6 top-set record. The next Monday resumes the top set as before.
- **Skip** the W9 single if the W4 single aggravated a joint and the issue has not been assessed/resolved. Current symptoms and the eligibility rules always take precedence.

**Back-offs M1b**

- 2 × 6–8 at 2–3 RIR, with their own record. 5–10% below the top set is a first estimate; actual effort governs.
- Both sets reaching eight clean reps qualifies for the smallest increase.
- The back-off load doesn't rise automatically when the top set rises. Back-offs are unchanged on single days.

### Thursday incline

**T1**

- 3 × 6–8 at 2–3 RIR.
- Increase after all currently prescribed sets reach eight with the required reserve, using 2.5 lb total steps where possible.
- No compulsory starting load, no automatic weekly increase, and no automatic fourth set; the stall response is in section 8.

### Estimating strength

Track the Monday top set and the singles with one formula:

`e1RM = load × [1 + (completed reps + estimated RIR) / 30]`

- Use the unrounded value in calculations and display whole pounds.
- Compare like with like: reps, RIR, angle, equipment and technique.
- A single supplies heavy-load practice and a separate performance observation. A subjective 1–2 RIR single is not proven to estimate 1RM more accurately than the rep-set method used here.
- Do not remove or retain singles based on a 2% match with the estimate used to choose their load. That comparison is partly circular and smaller than plausible RIR-estimation error.
- The result is a trend estimate, not a verified maximum. An estimated 225 lb is not a completed 225 lb single.
- No maximal single is required in this block. A later strength-assessment phase can be planned when useful.

## 6. Endurance sessions and progression

### Starting pace targets

| Use | Provisional pace | Effort cap |
|---|---|---|
| Tuesday work | **6:50/mi (≈4:15/km)** | Final rep RPE ≤8/10 |
| Friday work | **7:25/mi (≈4:37/km)** | Final rep RPE ≤7/10 |
| Warmup, recovery, cooldown | 8:30–9:30/mi as a guide | Comfortable conversation; slower is allowed |

- **Updating targets:** from a representative 5K at average pace `P` (seconds per mile), Tuesday is `P − 5` and Friday is `P + 30`, rounded to the nearest 5 s/mi. Use unrounded `P`; define rounding as `5 × floor(value / 5 + 0.5)` for these positive values. For 21:30, `P = 1290 × 1.609344 / 5 = 415.210752`; the resulting targets are exactly 410 and 445 s/mi. Normal pace-hit bands are 6:45–6:55/mi Tuesday and 7:20–7:30/mi Friday, subject to every other hit criterion.
- **Initial setup versus later test:** section 0 initializes this pre-block result and the W1 doses. Section 6 rule 6 governs subsequent in-block recalibration; it does not retroactively replace the initial setup.
- **Calibration:** check both targets through actual response. If a target is clearly inappropriate, slow it during the session; collecting a failed workout is not the objective.
- These are provisional coaching targets derived from the athlete-reported 21:30 result. Friday is intended as controlled sustained work, not a measured lactate-threshold prescription. The progression increments below are this program's heuristics, not a validated fitness model or a literal implementation of a named training system.
- **RPE** is a guardrail on the pace prescription, not a replacement for tracking pace.
- No heart-rate or cadence targets.

### Every normal run

- **Warmup:** ten minutes of easy running. Extend it by up to five minutes if needed, and count that distance in the weekly total.
- **Work intervals:** at an even pace. No finishing sprint.
- **Recoveries:** only **between** reps: three minutes on Tuesday, two on Friday, as comfortable jogging or walking. Choose one repeatable approach. Extra rest disqualifies the session from pace progression.
- **Cooldown:** five to ten minutes of easy jogging or walking.
- **Route:** use a reasonably flat route or a consistent treadmill setup.

  - On a treadmill, 1% grade is the default; record any other fixed setting and compare like with like.
  - No grade guarantees exact outdoor equivalence.

### Ten-week endurance schedule

Interval times are work only. Each week's table dose is that week's ceiling; the run rules can hold it lower. An earned faster pace can defer a duration increase, so reaching the listed minutes on that date is not required.

| Week | Tuesday | Friday | Wed bike | Sat bike | Running miles* |
|---|---|---|---:|---:|---|
| W1 | 3 × 4 min | 3 × 6 min | 20 min | 20 min | 8.4–10.1 |
| W2 | 3 × 4 min | 3 × 6 min | 20 min | 20 min | 8.4–10.1 |
| W3† | 4 × 4 min | 3 × 7 min | 20 min | 20 min | 9.7–11.4 |
| W4† | 4 × 4 min | 3 × 8 min | 25 min | 25 min | 10.1–11.8 |
| W5 | 2 × 4 min if recovered | A: first 5K if unused · B: 2 × 6 min · C: none | 15 min | 15 min | A 7.8–9.3 · B 6.5–8.1 |
| W6 | 4 × 4 min | 4 × 6 min | 25 min | 25 min | 10.3–12.0 |
| W7 | 4 × 4 min | 4 × 7 min | 30 min | 30 min | 10.9–12.6 |
| W8 | 4 × 4 min | 4 × 8 min | 35 min | 35 min | 11.4–13.1 |
| W9 | 4 × 4 min | 4 × 8 min | 40 min | 40 min | 11.4–13.1 |
| W10 | 2 × 4 min if recovered | A: 5K test · B: 2 × 6 min · C: none | 15 min | 15 min | A 7.8–9.3 · B 6.5–8.1 |

† W3/W4 show the ordinary build ceilings. If selected for the earlier first test, replace that week's endurance with section 7's assessment prescription: Tuesday 2 × 4, Friday 5K, and bikes at most 15 minutes each. Its illustrative mileage is then 7.8–9.3, not the ordinary row's range. After an early attempt, W5 uses B or C; no repeat first test.

\*Mileage assumptions:

- ten-minute warmups and 5–10-minute cooldowns, with those illustrated segments jogged at 8:30–9:30/mi
- every recovery jogged at 8:30–9:30/mi
- work at the 21:30-based starting targets (6:50/mi Tuesday; 7:25/mi Friday) and the full table ceilings; a test counts as exactly 5 km
- these are planning illustrations, not forecasts of mileage after earned pace changes, delayed progression, or recovery modifications

Walking recoveries reduce running mileage. Fifteen-minute warmups add about 1.05–1.18 miles in a two-run week; at the illustrative W8/W9 ceiling, the resulting range is about 12.4–14.3 miles. Recalculate the complete week whenever pace, work, warmup, or other running time changes; faster work at fixed minutes adds distance.

W6's 4 × 6 keeps W4's 24 Friday work minutes, broken into shorter reps after a possible pace reset. The two are not physiologically identical. There is no requirement to reach 32 minutes if the earlier dose isn't well tolerated.

### Cycling

- Cycle after the Wednesday and Saturday lifts at about **RPE 3/10**, with an acceptable range of 2–4. Full-sentence conversation should be possible.
- Use comfortable resistance, not a high-resistance leg workout.
- The listed minutes are ceilings, not required increases.
- Advance only when the previous dose leaves the following lifting and running acceptable. Otherwise hold at the last well-tolerated duration.
- An active global fatigue flag freezes duration increases. Option C allows at most 15 comfortable minutes per ride; section 8 controls the subsequent observation and return.
- Cycling is low impact, but it still requires recovery.

### Run rules

Keep separate Tuesday and Friday records: the **normal prescription**, current target pace, last successfully completed normal level, consecutive hits or misses, comfortable-hit tags/pair credit, any separate pending carried adjustment, recovery-report status, and any active return path. The normal prescription is the workout you are building from; a temporary cut does not replace it. Start with Tuesday 3 × 4 and Friday 3 × 6 unless calibration or a return rule calls for less.

| Run | Lower calibration level | Normal work-minute levels |
|---|---|---|
| Tuesday | 8 min: 2 × 4 | 12 min: 3 × 4 → 16 min: 4 × 4 |
| Friday | 12 min: 2 × 6 | 18 min: 3 × 6 → 21 min: 3 × 7 → 24 min: 3 × 8 or 4 × 6 → 28 min: 4 × 7 → 32 min: 4 × 8 |

Friday's two 24-minute formats are alternatives at the same level. Use 3 × 8 before W5 and 4 × 6 from W6. Returning one level below either means 21 minutes, not switching between them.

**Order of decisions:** symptoms and recovery overrides first; assessment-week and return prescriptions next; then the weekly and mileage ceilings; then ordinary progression. The lowest applicable limit wins. A ceiling is never a requirement to complete the work. The calibration levels are fallback workouts, not minimums to force through symptoms. Every instruction to clear or pause a run's progression records includes both ordinary hit/miss counts and comfortable-pair credit unless a more specific rule says otherwise. A clearing event also cancels any pending carried adjustment, except the scheduled assessment reset expressly waived in rule 5. A planned pause preserves only otherwise-valid records; it cannot reverse a cancellation.

1. **Classify eligible normal sessions after checking next-day recovery.** Only full normal prescriptions in reasonably comparable conditions earn progression credit. Temporary fatigue cuts, mileage cuts, return workouts, and assessment-week workouts do not.

   - **Hit:** every rep within ±5 s/mi of target, no extra rest, final-rep RPE within its cap, and normal next-day recovery.
   - **Miss:** while otherwise recovered and in comparable conditions, a rep is more than 5 s/mi slow, extra rest is needed, or the target requires exceeding the RPE cap. Deliberately slowing a clearly inappropriate target is also a miss; do not force the pace to protect the record.
   - **No-count:** uncertain measurement, substantially different conditions or treadmill setup, reps more than 5 s/mi fast at acceptable effort, poor recovery, or a shortened/skipped session. Hold progression and clear ordinary counts and comfortable-pair credit. Poor recovery also invokes rule 7. Apply these exclusions before deciding whether the pace numbers look like a hit. Assessment weeks have the specific counter treatment in rule 5 and section 7.

   **Comfortable hit:** an ordinary eligible hit whose final-rep RPE is **≤6 on Tuesday or ≤5 on Friday**. All other hit requirements still apply, including reported normal next-day recovery. Record whether each hit was comfortable. A **comfortable pair** means the two latest consecutive hits were both comfortable at the same target pace, work minutes, and interval format. It follows the ordinary hit streak's reset and pause rules; a miss, no-count, prescription reset, or non-comfortable hit breaks the comfortable sequence. These thresholds are coaching heuristics for trying a small pace adjustment, not a measured fitness test. The existing RPE caps of 8 and 7 remain ceilings, not targets to chase.

2. **Missed sessions, illness, and returning.** Never make up missed work. Apply gaps separately to each run type, using time since its last completed interval workout; a planned assessment substitution or reduction, including a deliberately selected W3/W4 assessment, does not itself trigger an additional return reduction. On every return, previous paces are provisional: start no faster than the previous target and slow as necessary to respect the effort cap. A representative new 5K can recalibrate pace when ready; a test is not required to return. Record the return reason and intended normal level before temporary work begins; retain that path until validated. A later temporary session or test does not erase it merely by updating the last-completed date.

   - After an isolated missed session with a gap of **14 days or less**, and no illness or fatigue problem, repeat the previous normal prescription before increasing it. Clear the interrupted streak. This first full session validates the normal dose; it earns no progression credit. Resume counting on subsequent normal workouts only after controlled effort and reported normal next-day recovery. If the prescribed work cannot be completed within the effort cap, or next-day recovery is reported poor, follow the reduced return path in the next bullet. Slowing a provisional pace alone does not fail dose validation; record and use the slower target if it is the appropriate recalibration. Uncertain conditions or missing recovery leave validation pending: repeat the appropriate prescription without progression. One isolated scheduling miss does not by itself block the narrow Option A exception in section 7.
   - After **Option C, illness, or a 15–28-day gap**, clear ordinary counts and comfortable-pair credit. Once recovered, start one work-minute level below the last successful normal level, bounded by the calibration level and this week's ceiling. If no normal level has yet succeeded, use the calibration workout.
   - After **more than 28 days**, restart at the calibration level.
   - When no global fatigue flag is active, a return workout with normal effort and next-day recovery permits restoring at most one level on the next corresponding run. These workouts earn no pace or progression hits; a global fatigue flag can require holding the return dose through its observation week. For a short return, restore only toward the previous normal level; after more than 28 days, rebuild to the original starting level (12 Tuesday/18 Friday). Normal counting resumes on subsequent full workouts only after that intended normal level has been validated with normal recovery and any global fatigue flag has cleared. If a return workout is not tolerated, hold lower or omit it; do not automatically restore work. Rule 7 governs the recovery-to-observation transition while the global flag is active.

3. **Choose one progression for the next normal session.** Recovery, return, assessment, and mileage restrictions take precedence. A repeated lifting ramp stage blocks both pace and work-minute increases. A faster-pace decision also requires acceptable priority lifting, no current recovery problem or worsening symptoms, and resolution of any missing report needed for that decision.

   **Acceptable priority lifting** means no open persistent-decline case in a slot assigned to a priority muscle or incline, using section 8's documented closure rule; during ramp or return weeks it also requires an explicit manageable answer for the latest completed week. An isolated rep dip does not by itself establish persistent decline. Current recovery, symptom, and technique concerns still take precedence over an earlier manageable answer.

   - **Comfortable-pair exception, from W3:** after a comfortable pair, or when applying rule 5's valid carried adjustment, use a target **5 s/mi faster** for the next normal exposure and keep work minutes unchanged. This takes priority over a due work-minute increase; defer that increase. W1–W2 hits can establish the pair for W3. The existing equal-minute Friday format change remains allowed.
   - **Otherwise, work minutes first:** following an ordinary hit, move up at most one work-minute level when the next normal build week's ceiling permits. If it does not, repeat the level and apply rule 4 when eligible. Never skip levels to catch up. An assessment week pauses ordinary progression; it does not move the calendar's other prescribed reductions. After an assessment without a representative test, retain the latest full normal session's actual classification for the next duration decision: only a hit permits an increase. Do not look past a more recent miss or no-count to reuse an older hit. Clearing streaks does not change that recorded result; existing recovery and return restrictions still take precedence. A representative test instead invokes rule 6's first-session hold. Only section 7's deliberate first-test rescheduling changes its week.
   - If the first attempt at increased work minutes misses, return to the last successful normal level at the same target pace. If none exists, use the calibration level. Clear progression counts before that return; a failed volume increase is not automatically evidence that the established pace must change.
   - An initial miss at the unchanged starting prescription, or a miss after a **pace-only** change, follows rule 4. Its first eligible miss is miss 1. Immediate effort/recovery overrides still apply.
   - Never increase work minutes and target speed together. Changing Friday between its two 24-minute formats is not a work-minute increase.

4. **Pace and counter timing.** Keep Tuesday and Friday records separate. At an unchanged target pace, work level, and format, two consecutive eligible misses call for **10 s/mi slower**. A hit clears misses; a miss clears hits and comfortable-pair credit.

   From W6, two consecutive ordinary eligible hits can still permit **5 s/mi faster** when no work-minute increase takes priority. A comfortable pair uses rule 3's earlier exception instead. These and a carried adjustment are alternative grounds for one five-second step; never stack them or add a pace increase to a work-minute increase.

   Clear both ordinary counts and comfortable-pair credit **before the first exposure** to a changed normal target pace, work level, or interval format. Then record that workout's result normally if eligible: its first miss is miss 1, and its first hit is hit 1, marked comfortable when applicable. Do not reset again just because the prescription was new. Temporary and assessment prescriptions follow their specific reset/pause rules and earn no progression credit. A clearly unsuitable target may be slowed immediately; the two-miss rule is not an instruction to repeat excessive effort.

5. **Build and assessment weeks.** W1–W2 permit work-minute increases within the table but no pace increases. From W3, the comfortable-pair exception is available; the ordinary two-hit pace route begins in W6. Slower targets remain allowed throughout.

   W5, W10, and any earlier assessment override earn no progression credit; their prescriptions override queued ordinary pace or work-minute increases. **End W5:** clear ordinary counts and comfortable-pair credit, whether or not a test happened. The narrowly defined carried adjustment below is separate from those cleared streaks.

   **One carried adjustment across recovered no-test work:** when an assessment week begins, save at most one pending five-second-per-mile adjustment per run type only if its comfortable pair is still valid and unused at that point. Record the source sessions, source pace/work minutes/format, and assessment week. Preserve it through **W5 Option B**, or an early assessment **cancelled before the test starts and completed under Option B**, only when the prescribed assessment work and reported recovery remain acceptable. The pending record may provisionally await the test decision; it cannot authorize faster assessment work. Do not recreate a pair by filtering historical logs for older full normal sessions.

   **Cancellation:** only the planned assessment reduction and its scheduled streak reset are waived. Any other event that clears comfortable credit cancels the pending adjustment permanently. This includes an intervening miss/no-count, a skipped or unexpectedly shortened run, poor recovery, illness, Option C, a return interruption/restriction, or an incompatible change to the normal pace, work minutes, or format. A missing recovery report still unresolved when planning the next corresponding run also cancels it. A test attempt cancels both runs' pending adjustments even if stopped or compromised; a representative result supplies the replacement targets under rule 6. Later recovery or a cleared restriction does not revive cancelled credit.

   **Application and expiry:** resolve the pending adjustment at the first otherwise-normal workout opportunity after the eligible assessment reduction. Apply it once only if rule 3's gates pass, the source normal pace and work minutes still apply, and the complete proposed week fits the mileage ceiling. Hold work minutes; Friday's expressly permitted equal-minute W6 format change may accompany it. Mark it used before applying the new target and rule 4's reset; the completed workout can then earn hit 1 or miss 1 normally. If the adjustment cannot be used at that first normal opportunity, cancel it and follow the remaining applicable prescription rules. Do not bank it for a later week. Consecutive eligible planned light weeks may postpone that first normal opportunity while preserving the same single pending record; they never create a second award. New credit thereafter must come from newly qualifying sessions.

   **W10:** pause existing ordinary counts and comfortable-pair credit and defer ordinary advancement until the next normal build session; a representative test, Option C, illness, or a qualifying gap overrides the pause and clears them. W10 does not create a separate carried award. An earlier assessment override follows section 7's end-of-assessment reset and the carried-adjustment exception above. Assessment reductions do not erase the last successful normal work level.

6. **Test recalibration.** Any test attempt cancels both runs' pending carried adjustments. A representative 5K sets Tuesday to `P − 5` and Friday to `P + 30`, rounded to the nearest 5 s/mi, and clears both runs' ordinary counts and comfortable-pair credit. This replaces queued ordinary pace adjustments; do not add an earned five-second step on top of the test-derived targets. It does not validate the previous interval work-minute dose or erase pending interval-dose validation. A clearly compromised result does not change the targets; other recovery/reset rules still apply. On the first normal workout at a reset target, use no more than the last successful normal work minutes, or the calibration workout if no normal level has succeeded. From calendar W6, Friday may change 3 × 8 to 4 × 6 at that same 24-minute level; an earlier test does not move the format change. If the ramp was delayed and only 21 minutes succeeded, start W6 at 21 minutes. Apply any stricter return, fatigue, or mileage limit first.

7. **Symptoms, fatigue, and temporary reductions.** Shorten or skip immediately for pain that changes gait, worsening joint/tendon symptoms, illness, or unusual fatigue. Do not wait for a second miss. Two successive attempts at the same prescription followed by reported poor next-day recovery also trigger a one-level temporary reduction for that run, even if both met the pace target; clear its counts. A well-recovered attempt at that prescription breaks this pattern. If the calibration dose is already poorly tolerated, omit hard work and review the cause rather than forcing a minimum.

   **Global fatigue:** the section 8 trigger starts **seven days of Option C**, followed by reassessment. When recovery supports returning, complete an observation week at the appropriate doses prescribed by section 8 and the return rules. The global flag remains active throughout that week: no pace, work-minute, cycling, or discretionary lifting increases, and no singles or tests. The expressly prescribed recovery-to-observation transition is allowed; it is not ordinary progression. Clear the flag only after the relevant lifting, running, and cycling sessions have actually been completed with acceptable recovery and performance. An empty calendar week does not supply that evidence. If recovery or performance remains poor, continue the recovery response and reassess rather than clearing the flag automatically. After clearance, make only **one substantive progression or restoration at a time**, within the current limits, as section 8 specifies.

   **Isolated run-recovery reduction:** when the problem is confined to one run, freeze that run's progression and require two well-recovered exposures at its reduced prescription before restoring toward its previous normal dose. If a global flag is active, the global response takes precedence; these exposures cannot authorize an otherwise prohibited increase. Record any temporary prescription separately from the normal one; it may fall between the listed levels. Neither temporary work nor restoration earns normal progression credit. Validate the intended normal dose with acceptable effort and next-day recovery before counting subsequent full normal workouts. Persistent symptoms take precedence over every restoration timetable.

8. **Mileage and other temporary ceilings.** Recalculate the upper end of the planned running-mileage range after any pace, work, or warmup change. Compare unrounded calculated distance with 15 miles; a rounded display below 15 does not establish compliance. If it exceeds 15 miles, remove Friday's last work rep and recalculate until it fits. If further trimming would go below the 12-minute Friday calibration level, use that workout; if even that cannot fit, omit the Friday run. Recheck the complete week and shorten or omit Tuesday too if needed to keep the total within 15 miles. A mileage-trimmed session earns no progression credit and does not redefine the normal prescription. Restore only when the complete planned week fits the ceiling and recovery permits; no catch-up or added easy miles. In a test week, keep the test at 5 km and reduce the other run or choose Option B instead of adding/truncating a test.

Without the comfortable-pair exception, Friday mainly progresses work minutes and its first ordinary two-hit pace increase may fall in the next block. The exception can instead advance its pace from W3 while deferring duration. These progression and return thresholds are practical coaching defaults, not a validated physiological algorithm or a literal implementation of Daniels' VDOT-update schedule.

## 7. Assessment weeks and the calendar

| Week | Dates if starting October 26 |
|---|---|
| W1 | Oct 26–Nov 1, 2026 |
| W2 | Nov 2–8 |
| W3 | Nov 9–15 |
| W4 | Nov 16–22 |
| W5 | Nov 23–29 |
| W6 | Nov 30–Dec 6 |
| W7 | Dec 7–13 |
| W8 | Dec 14–20 |
| W9 | Dec 21–27 |
| W10 | Dec 28, 2026–Jan 3, 2027 |

**Holiday collisions:**

- Thu Nov 26, Thanksgiving (W5 Upper B)
- Thu Dec 24 and Fri Dec 25 (W9 Upper B and the Friday run)
- Thu Dec 31 and Fri Jan 1 (W10 Upper B and the optional test)

If the gym is closed, skip that lift; missed work isn't debt. A run can go outdoors, or move under the section 2 rules.

The tests are options, not compulsory holiday appointments. A test can move to another separate run day within its selected assessment week, or a race can replace it once that week is explicitly rearranged under section 2. Changing the first assessment week follows the selection rule below. Never add a third hard run, and never pair a test with a lift or a ride.

### Optional earlier first 5K

The default test opportunities remain **W5 and W10**. After reviewing repeated comparable workouts and their recovery reports, the athlete may deliberately move the first 5K to **W3 (Friday November 13) or W4 (Friday November 20)** if the starting result appears unrepresentative or the prescribed paces substantially mismatched. An earlier test adds a lighter endurance week because W5 stays light; selecting W4 can therefore mean consecutive light endurance weeks. This is optional reassessment, not an automatic response to one easy session or a requirement to prove fitness. Normal Option A eligibility still applies.

Record the selected first-test week, whether its test has been attempted, and any assessment override already applied. Choose an early week **before that week's Tuesday workout** so the adjustments below apply prospectively. Moving the first test does not move the calendar, the lifting ramp, W5's lighter endurance week, or the W10 opportunity.

**In the selected early week:**

| Component | Prescription |
|---|---|
| Tuesday | 2 × 4 minutes at the current target, with normal warmup/recoveries/cooldown; stricter recovery limits still apply. |
| Friday | Option A's 5K and its warmup/cooldown, replacing Friday intervals. |
| Wednesday and Saturday bikes | At most 15 easy minutes each. |
| Lifting | Current achieved-stage prescription, with Wednesday calves omitted; retain all local limits. The test alone does not impose a lifting reduction. |

There is no added run, no third hard session, and no catch-up interval work. Recalculate mileage from the actual targets. These temporary endurance doses do not replace the saved normal prescriptions or last successful normal work-minute levels.

**What happens to W5:** after an early test attempt, W5 remains a lighter endurance week using **Option B** when recovered: Tuesday 2 × 4, Friday 2 × 6, and both bikes at most 15 minutes. Its lifting follows the achieved stage, with Wednesday calves included unless another restriction omits them. Use Option C if recovery is needed. W5 is not another test opportunity after the first test has already been attempted; W10 remains the second optional opportunity.

**Attempted versus cancelled:** once an early 5K starts, record the first opportunity as attempted even if the run is stopped or the result is compromised. There is no automatic replacement test at W5. If cancelled before starting, the unused first opportunity may explicitly revert to W5; record that decision. Retain the early week's already-applied reductions, with Option B Friday intervals if recovered or Option C if not. Do not retroactively restore omitted work. At most one first-test attempt plus the W10 attempt is scheduled within this block.

**Counters and pace:** the entire selected early assessment week earns no ordinary hit, miss, or comfortable-session credit, and no ordinary pace/dose increase is applied during it. Any test attempt cancels both runs' pending carried adjustments. A representative test immediately recalibrates both targets under rule 6 and clears ordinary hit/miss counts and comfortable-pair credit. At the end of the early assessment week, clear those streaks whether the test was representative, compromised, or cancelled; a compromised result does not change the targets. If the test was cancelled before starting and the week meets rule 5's recovered Option B conditions, only its separate, still-valid pending adjustment may survive that scheduled reset. Calendar W5 remains a separate no-credit lighter week and follows the same narrowly defined exception; W10 retains its pause/reset rules. Recovery flags, pending validation, and the saved successful normal dose are not cleared by these assessment resets.

**After the early week:** use the unchanged calendar ceilings and readiness rules. On the first normal run at a test-reset pace, hold work minutes at no more than the last successful normal level, even if the table allows more; use calibration if none exists. The test does not validate an outstanding interval-dose return requirement. Friday's 24-minute format remains **3 × 8 before W5 and 4 × 6 from W6**; moving the test does not move this format change.

A planned early assessment substitution, like the planned W5/W10 reduction, is neither a missed workout nor by itself a reason for a return penalty. Genuine illness, skipped work, unusual fatigue, poor recovery, or an existing return restriction still invokes its normal rule. An assessment week cannot supply the normal-dose observation required to clear a global fatigue flag.

### Option A: test

Choose this only when interested in testing, normally recovered, and free of worsening symptoms. A fatigue response or illness/gap return restriction defers the test, apart from the isolated scheduling-miss exception below.

- **Eligibility:** an available assessment opportunity, no active fatigue response or return restriction. The sole exception is one isolated scheduling miss with a gap of 14 days or less, confirmed normal current recovery, no worsening symptoms, and no other return or fatigue restriction. The test replaces the scheduled intervals; it never catches up missed work. Outstanding interval-dose validation remains required under run rule 2.
- **Lifting:**

  - First-test week, W3/W4/W5: the achieved-stage prescription minus Wednesday calves. Normally 81 sets at on-time C/D with one forearm set each; if the ramp is delayed or the prescription modified, calculate the actual total using section 4.
  - W10: the current reduced prescription minus Wednesday calves. Normally 36 from the unmodified full baseline; calculate after changes.
- **Tuesday:** 2 × 4 at the current target.
- **Friday:** ten minutes easy, a best evenly paced 5K, then five to ten minutes easy. The test **replaces** the Friday intervals; it is not an extra workout.
- **Bike:** at most 15 easy minutes after each of the Wednesday and Saturday lifts.
- **Afterwards:** apply run rule 6. VDOT may be logged as a race-performance score, not a measured VO2max. [R9]

### Option B: no test, recovered

- **Lifting:** W5 at the achieved stage, normally 85 sets; W10 reduced, normally 38 from the full baseline. If an early assessment is cancelled, continue its achieved-stage prescription with already-applied omissions retained. These parenthetical totals change with the achieved stage and recorded adjustments.
- **Runs:**

  - Tuesday 2 × 4 and Friday 2 × 6, both at the current targets with controlled effort.
  - No progression credit. Pace targets stay as they are unless a safety/effort adjustment requires slowing.
- **Bike:** at most 15 easy minutes after each of the Wednesday and Saturday lifts.

### Option C: recovery needed

Use this in any week when unusual fatigue or worsening symptoms are the reason to back off.

- Reduced lifting using section 4's current-dose calculation; 38 sets only when reduced from the unmodified full baseline.
- Omit hard runs and defer any test.
- Up to 15 minutes of easy cycling on each normal cycling day, after the lift and only if comfortable. Rest is fine; this is a ceiling.
- Use section 8's persistent fatigue flag and recovery-to-observation process. Section 4 supplies lifting allocations and section 6 controls the running return. No catch-up work.

## 8. Reviews, fatigue, and adjustments

Record:

- **Lifting:** each slot's load, clean repetitions and estimated RIR.
- **Runs:** each rep's pace, the final-rep RPE, and next-morning recovery after each run (normal or poor).
- **Cycling:** duration and effort.
- **Weekly:** review each run type's pace, work minutes, interval format, final-rep RPE, and reported recovery. Record hold, slower, faster at unchanged minutes, or the next work-minute level; apply the precedence in section 6. This is a review, not an added workout. At the end of each ramp, return or observation week, also record whether the week was manageable by section 4's four criteria.

Brief notes about unusual fatigue or aggravating movements are sufficient. No separate symptom dashboard is required.

### Missing or pending observations

Use actual reports for recovery and manageable-week decisions. Ask for the run response at the next morning brief or regular interaction, and the weekly answer at the next review, using one compact prompt. Silence means **not reported**, never normal, manageable, or poor. Record actual loads, reps, and RIR; never fill missing actuals from the prescription.

- A session can be logged as completed while its progression classification remains pending. Missing evidence blocks only the progression, restoration, stage advance, or clearance that depends on it. Repeat the current appropriate prescription when otherwise ready.
- If an ordinary run still lacks its recovery report when planning the next corresponding run, make the earlier result no-count and clear its ordinary hit/miss counts and comfortable-pair credit. Unknown recovery does not add a poor-recovery strike. Do not use a stale answer later to manufacture a missed progression opportunity.
- Return validation and observation remain pending until relevant work and recovery have been observed. Missing data does not establish either success or failure. Repeat the appropriate prescription rather than restoring an unvalidated dose.
- A missing manageable-week answer holds the achieved stage. A later completed and explicitly manageable week can permit advancement without recovering the older answer. Calendar rollover alone does not advance a stage.
- During global recovery or observation, unknown evidence holds the current phase and restrictions. It does not itself trigger another seven-day Option C period or clear the flag. Confirmed continuing recovery problems follow the reassessment rule below.

Corrections update records and future decisions; they do not rewrite completed prescriptions or create catch-up work.

**Body measures:** use a seven-day average of morning bodyweight. Every four to five weeks, optionally compare arms, chest, calves, waist, and consistent front/back photos under similar conditions without a pump. Read repeated trends alongside performance; flat circumference alone does not establish a hypertrophy plateau. There is no requirement for neck work or the earlier thigh/forearm circumference targets.

The thresholds below are coaching defaults for consistent decisions, not validated diagnostic cutoffs. Symptoms, deteriorating technique, or clearly inadequate recovery can justify reducing work immediately; do not wait for a counter.

### Distinguish a plateau from declining performance

- **Comparable lifting exposure:** the same slot, load, setup, range of motion, rest, and intended first-set RIR. For a normal plateau/progression comparison, also match the full prescribed set count and effort targets. Ramp, reduced, return, illness-affected, heavy-single, changed-equipment, and temporarily shortened sessions do not establish a normal plateau. A rep drop after a load increase is not automatically a decline.
- **First-set comparison during a trial:** a change to later sets does not erase a comparable first-set reference. That reference can detect deterioration even while the new full prescription is being evaluated.
- **Progress:** more clean repetitions across the same prescribed sets at comparable effort, or a successful load increase. Improvements in later sets count even if the first set is unchanged.
- **Plateau:** three comparable normal exposures with no progress, with performance otherwise stable. A downward trend is not a plateau and never earns additional sets.
- **Reference for a new trial:** before adding a set, changing effort, or changing a potentially interfering dose, save the affected slot's most recent comparable normal first-set performance. Keep that reference fixed while evaluating the change; do not lower it after a bad session. If no adequate reference exists, use the first normal exposure at the current load and first-set RIR as the anchor, then collect comparable exposures before drawing a causal conclusion. For example, the first stage-D exposure supplies the anchor when its first-set RIR differs from stage C. A load or first-set RIR change requires a new comparable anchor; it does not retrospectively establish deterioration.
- **Persistent decline:** the first set is at least two clean reps below that reference on two consecutive comparable exposures, or falls cumulatively by at least two reps across three comparable exposures. Thus both `10 -> 8 -> 8` and `10 -> 9 -> 8` trigger review. Neither pattern triggers a set addition. Compare RIR and execution before treating a rep difference as real deterioration.

### Local responses

Use the first applicable response for the affected movement. Keep unrelated training stable unless a global fatigue flag applies.

| Finding | Default action from the next unperformed relevant session |
|---|---|
| Pain worsens or technique changes to protect a joint | Stop, reduce, or modify the aggravating movement; do not force the programmed load. Persistent or worsening symptoms warrant assessment. |
| Persistent decline in a slot carrying added sets or a `0–1 RIR` last set | **If added sets are present, remove one added weekly set, newest first. Otherwise, return the last set to `1–2 RIR`.** Apply one response per new qualifying observation window. This rollback does not prove the cause. |
| Thursday cable curls still decline persistently, with no added set or `0–1 RIR` target left in that slot | Remove one Wednesday preacher-curl set, **once per block**. If that cut has already been used, hold progression and flag review. Do not also cut lateral raises unless their performance warrants it. |
| Thursday lateral raises still decline persistently, with no added set or `0–1 RIR` target left in that slot | Remove one Wednesday lateral-raise set, **once per block**. If that cut has already been used, hold progression and flag review. Do not also cut curls unless their performance warrants it. |
| Sunday leg performance declines persistently | If one plausible lower-body training-dose increase in the last four weeks is identifiable, undo that one change. If several are plausible or none is identifiable, hold progression and flag review of lifting, running, cycling and recovery to select the response. Do not undo every increase automatically or declare the Saturday bike responsible by default. |
| Stable plateau or a load increment too large for the rep range | Hold the prescription and flag review. Use smaller increments when available. Otherwise review the implement or rep range; do not automatically add sets or alternate repeatedly between two unsuitable loads. |

Log a rollback or local set cut and mark the triggering observations as handled. It remains in place until a documented review changes it; a timer does not restore it. Do not compensate by adding the removed work elsewhere.

Before another ordinary decline-based reduction, collect **at least two new comparable exposures** and reapply the persistent-decline test to that new observation window. Keep the fixed first-set anchor wherever conditions remain comparable; do not lower it after a cut or reuse handled observations to trigger another cut. Hold other discretionary changes to that muscle during this observation. Worsening symptoms or clear further deterioration can justify earlier action, and a global fatigue response need not wait. Applying a local response alone does not resolve a decline for the global-fatigue test.

**Closing a persistent-decline case:** record each qualifying case as open until a documented review of follow-up lifting performance and recovery resolves it. Use the new comparable observations gathered after the response, with the existing fixed reference wherever conditions remain comparable. The review must record the evidence, current prescription, recovery/symptom status, and why the observed decline is judged resolved. If follow-up evidence is insufficient or the problem continues, leave the case open, hold the progression that depends on closure, and flag review. A rollback, handled observation window, progression-counter reset, changed reference, or manageable-week answer alone does not close it. A retained local set or effort restriction may coexist with a resolved decline and stays in place until separately reviewed. Closing one case does not clear a global fatigue flag; that requires the full observation process below. Likewise, global-flag clearance alone does not silently close individual cases: record their status at that review.

### Global fatigue: one persistent flag

Set **global fatigue active** when currently unresolved persistent declines affect at least three core lifting slots across at least two lifting days, or when the athlete reports widespread unusual fatigue that continues into subsequent sessions and compromises normal training. This indicates a recovery problem to address; it does not identify lifting, running, or cycling as the sole cause.

While the flag is active:

- Freeze discretionary load increases, harder RIR targets, ramp-stage increases, forearm-dose increases, running pace/dose increases, bike-duration increases, and added-set trials. Downward adjustments remain allowed. The expressly prescribed recovery-to-observation return below is allowed; it is not a new progression trial.
- Defer heavy singles and 5K tests. Suspend `0–1 RIR` last sets during recovery and observation; use the easier stage-specific RIR, or `1–2 RIR` for those last sets if otherwise at stage D.
- Cancel unresolved added-set trials before calculating the reduced prescription. Previously adopted additions remain part of the normal-dose snapshot unless implicated and removed by a local rollback. Neither cancelled trials nor harder last-set targets return automatically.
- Clear progression counters and cancel pending carried run-pace adjustments on entering Option C, then keep progression inactive. Reduced recovery sessions alone do not establish recovery; clearance requires the observation week below.
- Apply changes only to sessions not yet performed. Do not rewrite completed workouts or add catch-up work.

**Default response:** begin the existing Option C prescription at the next unperformed session and continue it for a full seven days: reduced lifting, no hard runs or testing, and comfortable easy cycling only if appropriate. This reduces the combined workload without assuming which modality caused the problem. Undo any recent discretionary increase implicated by the local rules above.

**Reassess after those seven days:**

1. If unusual fatigue, worsening symptoms, or poor day-to-day function are reported or observed to remain, continue Option C for another seven days, review the cause, then reassess again. If the needed report is missing, hold the current phase pending that evidence; do not automatically start a new seven-day clock. Do not clear the flag or resume hard work merely because a week elapsed.
2. If recovery is acceptable, start a full seven-day **observation week** at the lower of the last clearly tolerated lifting stage and the saved illness/gap return-stage limit from section 4, with local rollbacks retained. If no return limit applies, use the last clearly tolerated stage. Running starts at section 6's return level, and cycling stays at or below its last clearly tolerated duration and the calendar ceiling. If no clearly tolerated lifting dose can be identified, use stage B only if previously tolerated and currently appropriate; otherwise start at A. The symptom rule can reduce further. No previous run success means the calibration workout. Planned assessment caps, including W5/W10 and any selected earlier assessment, still apply and do not qualify as the normal-dose observation week; an active fatigue flag also defers testing. After those scheduled caps end, the transition to the specified observation doses remains expressly allowed while the flag is active. Running observation uses the applicable return level; any remaining restoration occurs after clearance.
3. The flag remains active throughout observation: no increases, heavy singles, or testing. Downward adjustments remain available.
4. Clear the flag only after a complete observation week at the appropriate doses has been performed with acceptable performance and recovery, symptoms are not worsening, and priority sessions show no continuing decline. Seven elapsed days, skipped work, or the absence of comparable declines alone is insufficient; continue observation when the needed sessions have not been observed.
5. On clearance, reset progression counters and use the doses actually tolerated as the starting point. Introduce only one substantive progression or restoration at a time, checking its response before the next. Any unfinished running-return restriction remains in force. Removed sets, near-failure work, and an old calendar dose do not restore automatically; a persistent local cut still requires its documented review.

### Additional sets require a deliberate trial

The tracker's deterministic response to a stable plateau is **hold and flag review**. It does not add volume by itself.

A documented revision may trial **one additional weekly set** when all of the following hold:

- The pattern is a stable plateau, not a decline, and no global fatigue flag is active.
- Technique, RIR estimation, adherence, recovery, and food intake have been reviewed; a large load increment is not the unresolved obstacle.
- There is a clear target and affected slot, with a saved prechange reference.
- There is no unresolved local rollback or cut for that muscle, and no concurrent discretionary increase that would obscure the result.

Use at most one added-set trial at a time, at least two weeks between additions, and no more than two additional weekly sets for one muscle within this ten-week block. A trial may target one of the priority muscles or incline pressing. For incline, add at most one weekly set, at T1 only (four total there); do not add a top set or single. A calf trial goes to Sunday L2. Rear-delt and leg allocations remain fixed in this block. Forearms retain their separate conditional schedule. A successful trial must be explicitly adopted or removed before another begins.

During the trial, hold other discretionary changes stable and evaluate at least two comparable exposures. Retain the added set only if it is tolerated and the observed response supports continuing it. Two exposures assess tolerance and short-term performance; they cannot demonstrate additional muscle growth. Remove the set if performance declines, symptoms worsen, or recovery deteriorates. Update the prescription and set totals whenever a trial is adopted or reversed. More sets are not the default interpretation of an unchanging logbook.

### Missed sessions and re-entry

Missed work is skipped, not doubled. Use actual capacity on return rather than a calendar forecast. The global-fatigue process controls timing and clearance while its flag is active; the lower illness/gap return limits still apply. After illness or a substantial gap without an active fatigue flag, use the program's defined re-entry stage and calibrate; the calendar does not establish readiness.

## 9. Food and recovery assumptions

**Weight gain:**

- Keep the slow-gain target of about **0.4 lb/week**, judged as a trend over several weeks.
- Review if the four-week trend leaves roughly +0.2 to +0.6 lb/week, or if waist gain clearly outpaces useful training progress.
- A single weigh-in never triggers a calorie change.
- Weight gain can affect running; no fixed seconds-per-pound penalty is assumed.

**Protein:**

- About **1.6–2.2 g/kg/day**, which is **≈114–157 g/day at 157 lb (71.2 kg)**.
- The upper end is a practical buffer, not a requirement. [R8]

Eat enough total food and carbohydrate, and get enough hydration and sleep, to complete the work. Don't add supplements to compensate for an unrecoverable schedule.

## 10. Evidence and implementation notes

The exact set counts, RIR distribution, pace offsets, ramp, fatigue thresholds, and ten-week arrangement are **coaching choices**. Studies inform their direction; none has tested this combination in this athlete. Agreement between reviewers establishes agreement, not individual optimality.

### What the evidence supports—and its limits

- **Volume:** the aggregate relationship shows diminishing returns, with considerable uncertainty about the best dose for one person. It does not justify automatic calendar increases. [R1] Barsuhn et al. found no clear hypertrophy advantage from 30–60% set increases in an eight-week comparison with substantial attrition (29 of 55 enrolled completed). Enes et al. found strength benefits from progressive sets; the hypertrophy differences were uncertain. Neither demonstrates that extra sets never help. [R16, R17]
- **Proximity to failure:** meta-regressions associate closer estimated RIR with more hypertrophy, but do not establish the exact optimum or this nine-slot allocation. [R11] Refalo et al. found similar quadriceps growth with failure and perceived 1–2 RIR, with more acute fatigue at failure. A later small unilateral preacher-curl study found broadly similar adaptations with failure and 1–3 RIR, with uncertain differences. These findings leave room for a monitored near-failure trial, without making it necessary. [R2, R23]

  A 10-week trial with 31 completers compared constant 1 RIR with repeated progressions from 4 to 1 RIR. Between-group growth and strength differences were not significant; varying effort lowered average session RPE. RIR-3 error improved within the varying group, but changes in error did not differ significantly between groups. Both received failure familiarization and feedback. This does not show that near-failure training never improves estimation, or validate these nine isolation slots. [R25]

- **RIR accuracy:** Halperin et al. reported an average underprediction of about one repetition, with substantial heterogeneity. Accuracy was poorer in sets permitting more than 12 repetitions **to failure**; this does not mean 12 repetitions remaining, and the group average is not this athlete's personal bias. The result supports checking RIR judgments, not automatically correcting every set by one rep. [R12]
- **Loading and strength estimation:** RIR-based loading offers a workable approach without a tested maximum. [R3] Higher-load prescriptions ranked well for strength in a network meta-analysis; this does not establish that two singles improve this block. [R13] Reynolds et al. tested actual multiple-RM performances on flat barbell bench press and plate-loaded leg press. It did not validate this incline RIR-adjusted formula or prove a subjective-RIR single is more accurate than a rep set. [R14]
- **Exercise choice:** a direct comparison supports dumbbell lateral raises as a reasonable choice, consistent with the athlete's preference; it does not prove every lateral-raise variant equivalent in all settings. [R4]
- **Recovery weeks:** Coleman et al. studied an entire week without resistance training, not this reduced-volume prescription. Its outcomes cannot settle whether W5 should use normal or reduced lifting for this athlete. This program makes W5 conditional on recovery. [R15]
- **Short layoffs:** an author conference abstract reports retained lean mass and leg-press strength after two weeks without training in 20 trained men; this is a small cessation study with limited detail. [R24] A meta-analysis links longer cessation with larger muscular-performance losses. [R26] Duration therefore informs the return decision, but neither source validates an illness return or the specific 7/14/28-day thresholds and A/B/C assignments. The manageable-week gate and symptom rule still apply.
- **Running around leg work:** muscle-damage studies support taking recovery and repeated-exposure effects seriously. They do not establish a precise individual recovery window; the day-order restrictions here are conservative scheduling choices. [R18]
- **Intervals and concurrent training:** interval studies used different populations, protocols, and additional training. Their percentage improvements are not forecasts for this two-run program. [R5, R6] Concurrent-training results support combining modalities in principle; they do not establish tolerance for these exact sessions or guarantee the performance goals. [R7]
- **Adaptive endurance training:** a randomized study of recreational runners compared a predetermined program with adjustments based on recovery and training-status measures. The individualized group improved 10 km performance more. Its adjustments concerned volume and interval frequency, and participants trained more often than this two-run hybrid schedule. It supports responding to training and recovery together; it does not validate this program's five-second pace steps or earlier-test timing. [R27]
- **Interpreting a test:** a small reliability study in six trained male runners found roughly 1.5% within-runner variation across repeated 5 km trials. That scale is about 19 seconds at 21:30. It is not this athlete's personal error bound or a minimum meaningful improvement; route, conditions, pacing, effort, and repeated training evidence still matter. [R28]
- **Run progression:** two hits, the ±5 s/mi completion band, pace changes of 5 or 10 s/mi, comfortable-hit cutoffs of RPE 6/5, W3 eligibility, return-gap thresholds, and work-minute levels are transparent coaching heuristics. Neither the adaptive-training trial nor the reliability study establishes an optimal test frequency for this athlete. Weekly review and a deliberately selected W3/W4 test are practical options; frequent all-out tests are not required to adjust pace. Test results and actual training response remain the calibration inputs.

### References

Reference numbers retained from the review history make comparison easier. R19–R22 are intentionally unused: the secondary Daniels quotation, an old per-set coefficient, Pages-plan generalizations, and a third-party VDOT calculation are not needed for this prescription.

- **R1:** Pelland et al. The resistance training dose response, Sports Medicine 2026;56(2):481–505. [Primary paper](https://link.springer.com/article/10.1007/s40279-025-02344-w).
- **R2:** Refalo et al. Similar muscle hypertrophy following eight weeks of training to failure or with repetitions in reserve, 2024. [PubMed](https://pubmed.ncbi.nlm.nih.gov/38393985/).
- **R3:** Helms et al. RPE vs. percentage 1RM loading, 2018. [Primary paper](https://www.frontiersin.org/journals/physiology/articles/10.3389/fphys.2018.00247/full).
- **R4:** Larsen et al. Dumbbell versus cable lateral raises, 2025. [Primary paper](https://www.frontiersin.org/journals/physiology/articles/10.3389/fphys.2025.1611468/full).
- **R5:** Seiler et al. Adaptations to aerobic interval training, 2013. [PubMed](https://pubmed.ncbi.nlm.nih.gov/21812820/).
- **R6:** Esfarjani and Laursen. Manipulating high-intensity interval training, 2007. [PubMed](https://pubmed.ncbi.nlm.nih.gov/16876479/).
- **R7:** Schumann et al. Compatibility of concurrent aerobic and strength training, 2022. [Primary paper](https://link.springer.com/article/10.1007/s40279-021-01587-7).
- **R8:** Morton et al. Protein supplementation and resistance-training adaptations, 2018. [Full paper](https://pmc.ncbi.nlm.nih.gov/articles/PMC5867436/).
- **R9:** V.O2. [Official VDOT FAQ](https://support.vdoto2.com/v-o2-faq/).
- **R10:** GitHub. [About repositories and visibility](https://docs.github.com/en/repositories/creating-and-managing-repositories/about-repositories).
- **R11:** Robinson et al. Estimated proximity to failure, strength gain and hypertrophy: a series of meta-regressions, 2024. [Primary paper](https://link.springer.com/article/10.1007/s40279-024-02069-2).
- **R12:** Halperin et al. Accuracy in predicting repetitions to task failure in resistance exercise, 2022. [Primary paper](https://link.springer.com/article/10.1007/s40279-021-01559-x).
- **R13:** Currier et al. Resistance training prescription for muscle strength and hypertrophy: a Bayesian network meta-analysis, 2023. [Full paper](https://pmc.ncbi.nlm.nih.gov/articles/PMC10579494/).
- **R14:** Reynolds, Gordon and Robergs. Prediction of 1RM from multiple-RM testing, 2006. [Primary PDF](https://www.unm.edu/~rrobergs/478RMStrengthPrediction.pdf).
- **R15:** Coleman et al. Gaining more from doing less? A one-week deload during resistance training, 2024. [Full paper](https://pmc.ncbi.nlm.nih.gov/articles/PMC10809978/).
- **R16:** Barsuhn et al. Training volume increases or maintenance based on previous volume, 2025. [DOI](https://doi.org/10.1152/japplphysiol.00476.2024) · [Institutional abstract](https://openrepository.aut.ac.nz/items/87b4d27e-50d0-4dd4-b652-1cf456281ded).
- **R17:** Enes et al. Effects of different weekly set progressions on muscular adaptations in trained males, 2024. [PubMed](https://pubmed.ncbi.nlm.nih.gov/37796222/).
- **R18:** Assumpção et al. Exercise-induced muscle damage and running economy in humans, 2013. [Full paper](https://pmc.ncbi.nlm.nih.gov/articles/PMC3575608/).
- **R23:** Vasconcelos et al. Elbow flexor adaptations to failure versus repetitions-in-reserve training: a unilateral within-participant study in resistance-trained adults, Muscles 2026;5(3):61. [Full paper](https://pmc.ncbi.nlm.nih.gov/articles/PMC13609929/) · [DOI](https://doi.org/10.3390/muscles5030061).
- **R24:** Hwang et al. Effects of a two-week detraining period followed by retraining on resistance-trained men, 2016 conference abstract. [Primary author abstract](https://digitalcommons.wku.edu/ijesab/vol2/iss8/82/). This accessible abstract supports the limited cessation finding; the previously linked dissertation was not available for full-text verification in the v6 review.
- **R25:** Martikainen et al. Influence of varying proximity-to-failure on muscular adaptations and repetitions-in-reserve estimation accuracy in resistance-trained individuals, Journal of Science in Sport and Exercise 2025. [Primary paper](https://link.springer.com/article/10.1007/s42978-025-00338-8).
- **R26:** Bosquet et al. Effect of training cessation on muscular performance: a meta-analysis, Scand J Med Sci Sports 2013;23(3). [Primary publication](https://onlinelibrary.wiley.com/doi/10.1111/sms.12047).

- **R27:** Nuuttila et al. Individualized endurance training based on recovery and training status in recreational runners, Med Sci Sports Exerc 2022;54(10):1690–1701. [PubMed](https://pubmed.ncbi.nlm.nih.gov/35975912/) · [Full paper](https://pmc.ncbi.nlm.nih.gov/articles/PMC9473708/) · [Author-shared paper](https://www.researchgate.net/publication/362719958_Individualized_Endurance_Training_Based_on_Recovery_and_Training_Status_in_Recreational_Runners).
- **R28:** Fisher et al. Intra-subject variability of 5 km time trial performance completed by competitive trained runners, J Hum Kinet 2017;57:139–146. [Institutional primary record](https://ueaeprints.uea.ac.uk/id/eprint/90082/) · [DOI](https://doi.org/10.1515/hukin-2017-0055).

## 11. Repository and dashboard contract

### Authority and persisted state

This is the complete current prescription. `Tracker.md` supplies current state and actual reports, not a competing old program. The agent applies the decision rules; `index.html` displays the prepared result. Updating `program.md` alone does not rewrite the caches or implement a decision engine. On adoption and every later relevant interaction, the agent must reconcile state and regenerate the affected caches through the normal repository workflow.

Apply, in order: current symptoms/local restrictions and global recovery; saved return and assessment overrides; achieved stage and current ceilings; valid ordinary progression. The lowest applicable limit wins. Resolve a pending carried pace adjustment at the first otherwise-normal opportunity under section 6 rule 5 before ordinary progression. Never reconstruct cancelled credit from old logs, combine pace awards, or add one to a test-derived reset.

Keep these records in the existing current-state file, with detailed dated actuals/decisions in the existing history streams. Structured JSON or YAML state may be embedded in `Tracker.md`; it does not require another program file.

| State group | Required fields/meaning |
|---|---|
| Block | Stable block ID, program ID/version, adoption status and completed-step markers, activation status (scheduled/active/completed), start/end dates, timezone, calendar week, phase, achieved lifting stage, latest explicitly manageable completed week; calendar and stage are separate. |
| Baseline/results | Stable result ID, report date, actual event date if known, distance, elapsed time, provenance, conditions/RPE/recovery if actually reported. Do not relabel a report as independently verified. |
| Lifting slots | All 33 IDs below; current load/units/equipment/setup or uninitialized, sets/reps/RIR/rest, qualification count, last same-slot actual and date, comparable first-set anchors, persistent cuts/omissions and reason, trial/extra-set status, handled decline windows, new-exposure count, open/resolved decline case with review evidence/date, used cross-day cuts. |
| Return | Historical pre-interruption last-lift date and last tolerated stage, interruption reason, initial return stage, current active return-stage limit, pending validation and dates; temporary attempts never overwrite the historical reference. |
| Forearms | Current exposure stage, one/two-set eligibility, dated elbow-response answer, and any restriction. A null answer does not qualify two sets. |
| Runs, independently Tue/Fri | Normal pace, work minutes and interval format; separate temporary prescription; last successful normal level; latest actual classification; hit/miss counts; comfortable-hit tags/pair credit; next-day recovery status; poor-recovery pattern; last completed date; saved return path/normal-dose validation. |
| Carried adjustment, each run | Source sessions, source pace/minutes/format, assessment week, status pending/used/cancelled, and dated use/cancellation reason. Null means none. Never regenerate from filtered history. |
| Assessments | Selected first in-block test week, attempt status, applied overrides, cancellation/reversion decision, result provenance and representativeness. Pre-block baseline is separate. |
| Recovery | Local restrictions, global-fatigue flag if actually triggered, seven-day response dates, observation phase/doses, per-modality completed evidence, pending gates, effective normal set vector, and reduced snapshot. |
| Completion | Dated done/skipped/rest/unreported outcomes, actual per-set/rep values, bike minutes/effort, and shoes/distance only when reported. |

**Slot IDs:** `M1a, M1b, M2, M3, M4, M5, M6, M7; WE1, WE2, WE3, WE4, WE5; T1, T2, T3, T4, T5, T6, T7, T8; S1, S2, S3, S4, S5, S6; L1, L2, L3, L4, L5, L6`.

Keep Current Working Loads an exercise-slot table. State flags and run counters are not fictitious exercises. Render separate “Incline BB — top set” and “Incline BB — back-offs” rows so M1a and M1b cannot be merged by the lift-log form. Distinguish repeated exercises by slot/day in the current-load table. Store actual machine/handle and per-arm conventions; equal stack numbers across equipment do not imply equal loading.

### Unknown evidence and logging

- Actual numbers come from the athlete's report, never from targets, a cached brief, or an old prescription. A completed session can still have pending progression classification.
- Missing run recovery stays pending. At the next corresponding run, an unresolved ordinary-session report becomes no-count and clears ordinary/comfortable credit and pending carried credit, without inventing a poor-recovery strike. Missing assessment recovery follows section 6 rule 5.
- Missing manageable/return/observation answers hold only the advancement/restoration/clearance that requires them. A later completed, explicitly manageable week can release a stage hold without inventing the older answer. Unknown evidence alone does not start another seven-day recovery response.
- The dashboard's **Fill targets** button is a convenience, not evidence. Validate pasted actuals as actual numeric reps and estimated RIR for each set. A range such as `8–12`, compound `2 / last 0–1`, or unchanged placeholder is not a measured actual; request the needed value once or log `n/r` and withhold dependent credit. Explicit athlete confirmation of exact completed values is acceptable.
- The lift-log form saves a draft by date in the browser. A same-day prescription change may leave an old draft visible. Preserve any entered actuals before using its existing Reset button, and compare pasted dumps with the dated effective prescription. Never overwrite real actuals with targets to make the form match.
- Preserve current symptom restrictions until reviewed. The default “unchanged context” may preserve an existing restriction; it cannot invent a normal response, clear it, or authorize advancement.

### Daily cache: exact existing renderer shape

All displayed scalar values are **plain strings**; arrays/objects/null remain their declared types. Use `"0"` for zero RIR, not numeric `0` (the renderer uses truthy fallback). Do not embed Markdown or HTML in values. Extra JSON properties are not displayed unless the renderer is changed.

`latest-workout.json` requires `generatedAt`, `week`, `day`, `date`, `phase`, `sessionName`, `intro`, `lift`, `cardio`, and `currentLoads`:

- `generatedAt`: real generation timestamp with the New York offset; `date`: the brief's athlete-local ISO date. DST is determined by `America/New_York`, not a fixed offset.
- `week`: `W1` through `W10`, or `Pre-block` before the start. `phase` identifies Hybrid v11 and the actual ramp/normal/recovery/return state.
- `intro`: string array; normally zero or one concise decision-critical line.
- `lift`: `null` when absent. Otherwise an object with `table` array, `lastWeek` object, `warmup` string, and `cooldown` string. Never use `{}` for an absent lift.
- `lift.table` rows: `exercise`, `setsReps`, `load`, `rir`, `rest`, `cue`, all strings. Begin `setsReps` with the effective integer set count and `×`, e.g. `2×8–12`; the log form reads that prefix. Omitted exercises do not appear as prescribed work rows. Keep separate top-set/back-off rows. Show unknown loads as `Calibrate` and never turn that word into a logged load.
- `lift.lastWeek`: `label` string and `table` array of `exercise`, `load`, `reps`, `rir` strings. Give actual dates in the label/rows. For new slots, say `First exposure` and use `n/r`; the fixed “Last week” heading is not evidence of recency or comparability.
- `cardio`: `null` when absent. Otherwise `flags` string array, `workout` string, `targets` object or null, `warmup` string, `cooldown` string, `cues` string array, and `workoutFile` relative path or null. Put RPE caps in workout/cues; the renderer has no RPE grid field. For optional targets use `{ "pace": "...", "hr": "", "cadence": "" }`; omit/null the grid when unused. Never require HR/cadence values.
- Wednesday/Saturday can contain both lift and cycling; the cardio block clearly says bike **after lifting**, and its Watch file is null. Running never shares a day with lifting/cycling.
- `currentLoads`: array of `exercise`, `load`, `lastVerified`, `note` strings, matching the active slot table in Tracker at that snapshot. Do not put obsolete legacy progression instructions back into these notes.

This is a **synthetic shape fixture**, not an actual completed workout or today's cache. It intentionally includes one lift row to show field types:

```json
{
  "generatedAt": "2026-10-26T07:00:00-04:00",
  "week": "W1",
  "day": "Mon",
  "date": "2026-10-26",
  "phase": "Hybrid v11 — Ramp A",
  "sessionName": "Upper A — schema example only",
  "intro": ["Example only; production briefs contain every effective exercise."],
  "lift": {
    "table": [
      {"exercise": "Incline BB — top set", "setsReps": "1×4–6", "load": "Calibrate", "rir": "3", "rest": "3–4 min", "cue": "Stable angle and range; no forced reps."}
    ],
    "lastWeek": {
      "label": "First exposure in this slot and block",
      "table": [{"exercise": "Incline BB — top set", "load": "n/r", "reps": "n/r", "rir": "n/r"}]
    },
    "warmup": "Progressive incline practice sets without fatigue.",
    "cooldown": "No required cooldown."
  },
  "cardio": null,
  "currentLoads": [{"exercise": "M1a — Incline BB top set", "load": "Calibrate", "lastVerified": "First exposure", "note": "Historical loads are calibration references only."}]
}
```

For a rest/recovery day with no prescribed modalities, use `lift: null`, `cardio: null`; retain the correct date, phase, explanation and current loads. Show only today's **effective** workout, not a second executable normal workout alongside its recovery override.

### Week cache and calendar

`week-ahead.json` has `generatedAt`, `week`, `phase`, `summary` strings and a `days` array. Each row contains `date`, `day`, `session`, `note`, `status` strings. Keep exactly seven consecutive Monday–Sunday rows. `generatedAt` matches the daily cache when generated together. The two caches must refer to the same block/current calendar week and state snapshot.

- Use `done` only for reported completion; `today` for unresolved current-date work; `upcoming` for future dates.
- For past dates use explicit `skipped`, `rest`, or `unreported` as supported by the actual report. The renderer displays those neutral classes; add a short note. Missing logs are not proof of completion or rest.
- Sunday is Legs in this block. Wednesday/Saturday include the post-lift bike when appropriate. Current restrictions and recovery can change the effective sessions.
- Before October 26, display the current transition week with `Pre-block`; do not mislabel next Monday's W1 preview as today's week. October 25 remains post-race rest.
- Calendar rollover does not advance the achieved lifting stage, clear fatigue, validate recovery, or consume an assessment. Close prior weeks at the calendar boundary while retaining unresolved evidence.
- Generate a future preview only when requested, label its actual future date, and do not silently replace a current-day cache with tomorrow's workout after logging today.

### Apple Watch export using the existing helper

The repository already supplies `tools/workoutgen.py`; use it when generating an actual outdoor-run brief. No new encoder is required. Read its supported syntax, generate the text spec, build and decode-check it. Put the actual file under `runs/{date}.workout` and set `cardio.workoutFile` only after a successful build. Bike, rest, and treadmill-only sessions use null.

1. Work, warmup and cooldown goals match the selected effective brief exactly. Select a concrete allowed cooldown duration for the export; never convert a range into a silently invented actual. Count its prescribed running distance in the plan.
2. Recoveries occur **between** reps only: encode `N−1` work/recovery pairs followed by one final work rep, or another supported structure producing the same sequence. Never put recovery after the last rep just because it is easier to repeat.
3. Work-step pace alerts may use the target ±5 s/mi band: initially Tuesday `6:45–6:55/mi`, Friday `7:20–7:30/mi`. Recompute after a target change. These display alerts do not remove the effort cap or dictate the actual post-session hit classification.
4. Do not import the old I/T/R/M or easy bands into this block. Easy running is conversational and may be slower than 8:30–9:30; omit an easy-pace alert when it would suggest a mandatory faster effort. Recovery steps have no pace alert. No HR/cadence/power targets, strides, or sub-minute work bouts are added.
5. RPE remains visible in the brief because the file has no RPE alert. Do not replace it with heart rate. A test is a 5 km work segment; never insert the aspirational 18:00 goal pace as a mandatory test alert.
6. If the encoder does not support a requested feature, omit that unsupported alert/file as appropriate and state the limitation; do not invent an encoding or broken download link.

### Validation before writing derived state/caches

- Confirm program ID, athlete-local date/week and active stage; apply gates before generating rows.
- Validate all 33 slot identities; preserve 23 unique selected exercises and the nine specifically eligible final 0–1 slots. The full baseline is 83 core sets plus 2/4 forearm sets. Recompute effective counts after omissions, stage, cuts, trials or reduction; never force a baseline total.
- Validate the pace formula with unrounded inputs, the selected interval format, RPE caps, recovery count, and the **unrounded** complete-week mileage ceiling.
- Parse JSON; verify field types, non-null lift structure, separate incline rows, seven week rows, real dates/statuses and consistent timestamps. A `0`-RIR display uses the string `"0"`.
- Check “Last week” dates and comparable slots. Missing actuals stay missing; no inherited new-block qualification credit.
- Before overwriting generated caches, confirm the state snapshot still matches the actual reports being logged. Update state/history/caches together through the repository's normal logging workflow. A stale open browser tab does not authorize overwriting a newer report.
- Do not claim that editing this file has executed a workout, completed migration, or regenerated a live cache. The agent must actually perform and verify those actions when it adopts/logs the program.

### Verification scope

This source preserves the v10 training decision rules and exercise tables while updating the reported baseline and repository handoff. Arithmetic, slot/set invariants, front-matter constants, example JSON and the visible renderer contract can be checked statically. Those checks do not establish personal optimality, validate every future state transition in an executable engine, or confirm live dashboard regeneration. Actual training response and the explicit review gates govern changes.
