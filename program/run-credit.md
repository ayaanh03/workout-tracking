# Assessment run credit and test resets

Apply [normal progression gates](run-progression.md), [assessment prescriptions](assessments.md), and [return restrictions](run-return.md). Persist each run separately in [running state](../state/running.json).

## Assessment counters and carried award


- **W5 and selected early assessment:** at week end clear counts/comfortable credit, tested or not. Retain last successful normal dose, latest normal classification, recovery flags and pending dose validation.
- **W10:** pause counts/comfortable credit and advancement until the next normal build exposure. Representative test, Option C, illness or qualifying gap clears instead. No separate carried award is created.
- **At an assessment week's start**, save at most one pending 5 s/mi award per run only from its still-valid, unused comfortable pair. Record both source sessions, source pace/minutes/format and assessment week. Never reconstruct eligibility by filtering out intervening sessions. Pending awards cannot speed up assessment work.
- **May survive:** W5 Option B or an early assessment cancelled *before testing starts* and completed under B, with prescribed work and reported recovery acceptable. Only planned reduction and its scheduled streak reset are waived. Consecutive eligible light weeks may preserve the same award until the first normal opportunity; they never create another award.
- **Cancel permanently for:** miss/no-count; skipped or unexpectedly shortened work; poor recovery; illness; Option C; return interruption/restriction; incompatible normal pace/minutes/format change; or recovery still unreported when planning the next corresponding run. Any test attempt cancels **both** awards, including stopped/compromised tests. Later recovery cannot revive them.
- **Use or expire at first otherwise-normal opportunity:** all progression gates must pass, source pace/minutes still apply, and complete planned week must fit 15 miles. Apply once, hold minutes, mark used **before** target/reset update. The permitted W6 equal-minute Friday format change is allowed. That workout can earn hit/miss 1. If unusable then, cancel; do not bank it.

## Tests

Any attempt cancels both pending awards. A **representative 5K** recalculates both targets using [endurance.md](endurance.md), clears both runs' counts/comfortable credit, and replaces queued pace changes; never add another earned 5-second step. A compromised result leaves pace unchanged; other reset/recovery rules still apply.

First normal exposure at reset pace: no more than last successful normal minutes, or calibration if none; stricter limits win. Test results do not validate interval dose or clear an unfinished return. The Friday 3 × 8 → 4 × 6 change stays at calendar W6; if only 21 minutes succeeded, use 21. This reset differs from the pre-block 21:30 initialization.
