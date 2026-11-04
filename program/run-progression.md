# Run progression

Read with [endurance](endurance.md), [assessments](assessments.md) and [credit/reset rules](run-credit.md). Keep Tuesday and Friday independent in [running state](../state/running.json): normal target/dose, latest actuals/classification, hit/miss counts, pace-step evidence, last successful normal dose, recovery/return and carried award. Temporary work never overwrites normal dose.

**Athlete directive, November 3, 2026 (#467):** adjust pace promptly when completed work shows the target is too slow; use smaller, evidence-based steps as headroom disappears. This replaces the W1/W2 speed lock, W3/W6 pace eligibility waits and automatic minutes-first priority. These step sizes are programming choices, not physiological thresholds.

| Run | Calibration fallback | Normal levels, minutes: format |
|---|---|---|
| Tuesday | 8: 2 × 4 | 12: 3 × 4 → 16: 4 × 4 |
| Friday | 12: 2 × 6 | 18: 3 × 6 → 21: 3 × 7 → 24: 3 × 8 / 4 × 6 → 28: 4 × 7 → 32: 4 × 8 |

Friday's 24-minute formats are one level: 3 × 8 before W5, 4 × 6 from W6. One level below either is 21 minutes. Calendar rows cap **work minutes**, not pace. They never force a volume increase.

## Classification

Classify only after actual next-day recovery is reported. Full normal work in comparable conditions is required; temporary cuts, return work and assessment workouts earn no progression. A recovery forecast is not an observation.

| Result | Conditions / action |
|---|---|
| Hit | Every rep at target or faster, allowing up to 5 s/mi slow (`actual seconds/mile ≤ target + 5`); no extra interval rest, final RPE within cap, normal next-day recovery. No fast-side cutoff. Clears misses. |
| Miss | Otherwise recovered/comparable, but a rep >5 s/mi slow, extra rest, or effort exceeds cap. Deliberate slowing of an unsuitable target also counts. Clears hits/comfortable credit and unused pace steps. |
| No-count | Uncertain measurement, materially changed conditions, poor recovery, shortened/skipped work. Clear counts/comfortable credit and unused pace steps; hold progression. Poor recovery invokes [run recovery](run-return.md). |

Apply exclusions before pace. Missing recovery stays pending; at the next corresponding run, unresolved recovery becomes no-count without inventing poor recovery. Faster reps count under #450 but do not offset a slow rep, excessive effort, extra rest or missing work. Watch pace alerts guide pacing; fast-side alerts do not disqualify credit. Preserve actual paces and the original prescribed target separately.

A required streak clear also cancels unused pace evidence/awards, except an explicitly saved surviving [assessment award](run-credit.md). A pause cannot revive cancelled credit.

A **comfortable hit** has final RPE ≤6 Tuesday / ≤5 Friday (two points below cap). Retain the comfortable tag/pair for history: a pair is two latest consecutive comfortable hits at the same prescribed target, minutes, format and recovery duration. It is no longer a prerequisite for prompt pace adjustment. Ordinary pairs likewise compare prescriptions, not identical actual splits. A miss/no-count or changed prescription breaks the pair; a non-comfortable hit breaks only the comfortable pair.

## Eligibility before increasing

Symptoms/recovery → fatigue/assessment/return → complete-week mileage → performance-based progression. Effort caps remain **Tuesday 8, Friday 7**; never force extra effort to earn progression. Normal recovery and acceptable running/lifting tolerance are required. During the ramp, review the latest completed week's manageability; pending evidence is not clearance. Investigate persistent priority-lift decline before attributing it to running or increasing its load.

A **local upper-body hold or repeated lifting stage alone does not block running**. Record why the stage is held: global fatigue, poor recovery, running-relevant joint/tendon symptoms or persistent lower-body decline can block increases; a biceps maintenance hold by itself cannot. Existing injury/return restrictions still apply. Assessment weeks allow no progression. The full planned week must fit 15 running miles, including all easy sections.

## Choose the next normal prescription

Evaluate the latest eligible normal session at its **original prescribed target**. Use the first applicable pace route below; never add routes together. A valid carried award is handled first under [run credit](run-credit.md). No minimum calendar week is required.

| Evidence after recovery | Next pace, with work minutes held |
|---|---|
| **All work reps ≥5 s/mi faster** | Let `headroom = prescribed seconds/mile − slowest work-rep seconds/mile`. Step = `min(15, 5 × floor(headroom / 5))` s/mi faster. One qualifying session is enough. All ≥10 faster gives a 10–15 second step; 5–9 faster gives 5. |
| **Target met with clearly spare effort** | One comfortable hit (final RPE ≤cap−2) earns 5 s/mi faster, even without running faster than prescribed. |
| **Near current limit, little demonstrated headroom** | Two consecutive eligible hits at unchanged target/minutes/format/recovery earn 5 s/mi faster. With only one and no other route, hold pace. |

The measured-pace route uses the **slowest** rep, never the fastest or average, and cannot set a target faster than every rep demonstrated. Its 15-second cap applies per next exposure; do not apply the same source repeatedly. The effort/pair routes are small prospective progressions and need not have been run already. Pace offsets accepted by a historical tracking exception remain hits, but unmeasured corrections cannot establish faster-pace headroom.

If no pace step is due, one normal hit with final RPE **≤cap−1** may add **one work-minute level** within the next week's ceiling, at unchanged pace. Otherwise hold the dose and reassess. Never skip levels or add work to compensate for a miss. Faster pace takes priority whenever its route qualifies; **never increase pace and minutes together**. The scheduled Friday equal-minute format change is allowed.

Examples: Tuesday target 6:50, actuals 6:28/6:37/6:31 → slowest 6:37, headroom 13 → **3×4 at 6:40** once recovery/other gates pass. Friday target 7:25, actuals 7:27/7:13/7:16, final RPE 7 and hit 1 → no faster target yet. Keep each run's evidence separate.

## Stalls, resets and use once

- One eligible miss: hold/review; slow immediately if the target is clearly unsuitable or exceeds the effort cap. At unchanged prescription, **two consecutive eligible misses → 10 s/mi slower**. Poor recovery follows [run return](run-return.md), not the miss shortcut.
- If the first attempt at higher minutes misses, return to last successful normal minutes at the same pace (calibration if none). Clear counts before returning; do not assume the established pace needs slowing.
- Before first exposure to changed normal pace/minutes/format, record the chosen step and source session(s) as used, then clear counts/comfortable credit. Count that changed exposure normally if eligible; do not reset its result again afterward. A pending candidate does not itself update the current normal target or clear counts.
- A newer miss/no-count cancels unused steps. Never search past a newer result, reuse a consumed source, or resurrect cancelled credit. Multiple eligible routes yield **one step**, never stacked awards.
- A reset or assessment can leave the latest full normal classification available for dose review but cannot recreate consumed pace evidence. Only an explicitly saved eligible [carried award](run-credit.md) can bridge the W5/early-assessment reset. W10 instead pauses still-valid unused evidence under the existing credit rules, without creating a separate carried award; tests or other clearing events cancel it. Tests replace queued pace changes.

Persist each decision's original target, complete actual paces, slowest rep/headroom, effort/recovery, route, proposed step, remaining gates and application status. Record the effective prescription and source consumption when it is generated. The dashboard displays prepared decisions; it is not an automatic progression engine.
