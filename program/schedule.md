# Schedule — Hybrid v11

Block `hybrid-2026-10-26`; program `hybrid-2026-10-26-v11` (11.0). Activated October 25, 2026; regular calendar anchor October 26; end January 3, 2027; `America/New_York`.

| Day | Prescription |
|---|---|
| Monday | [Upper A](monday.md) |
| Tuesday | [Intervals](endurance.md) |
| Wednesday | [Delts and arms A](wednesday.md), then easy bike |
| Thursday | [Upper B](thursday.md) |
| Friday | [Longer intervals](endurance.md) |
| Saturday | [Delts and arms B](saturday.md), then easy bike |
| Sunday | [Legs, abs, calves](sunday.md) |

Apply dated `schedule_overrides` in [block state](../state/block.json) before selecting from this weekday table. A one-time swap changes session dates, preserving the original lift slots and independent run/cycling tracks; it does not change the regular template. Automatic next-workout generation follows this effective schedule.

**November 6–7 swap (#475):** Saturday's delts/arms B + bike moves to Friday November 6; Friday's longer intervals move to Saturday November 7. The normal schedule resumes with Sunday legs on November 8.

W1–W3 are calendar Ramp; W4–W9 Build; W10 Reduce. The **achieved lifting stage**, current reports and restrictions determine the actual dose. Calendar rollover never advances a stage. At the athlete's request, **October 25 is the opening stage-A Sunday leg session** (#433); October 24 remains pre-block. Monday October 26 stays Upper A, W1 remains October 26–November 1, and later single/test/end dates are unchanged. Record the opening exposure separately: it does not complete the following Sunday's session or a manageable week. No automatic next-block prescription after January 3.

## Selection order

1. Current symptoms, persistent local restrictions and global recovery.
2. Saved return limits and assessment overrides.
3. Achieved lifting stage and calendar ceilings.
4. Valid earned progression. Resolve a pending carried run-pace adjustment before ordinary progression.

The lowest applicable limit wins. Use [Tracker](../Tracker.md) to locate the current `state/` records; immutable starting values never reset earned state. Every changed prescription needs its source actual(s), applicable rule and resulting hold/increase/reduction recorded.

## Constraints that affect selection

- Priority: hypertrophy (side delts, arms, back, abs, calves; conservative legs), then incline strength toward a completed 225 lb single, then running toward 18:00 for 5K.
- Runs normally Tuesday/Friday, subject to explicit dated overrides; never share a day with lifting/cycling. Bikes follow the Wednesday/Saturday lifting sessions, including when those sessions are moved.
- No standalone easy runs, strides, or planned running work bouts shorter than one minute. 5K is the longest race; whole sessions may exceed 5 km. Running ceiling: 15 miles/week.
- No hard run the day after direct leg/calf lifting; no direct triceps the day before incline. If a compatible rearrangement is unavailable, skip missed work. Never make it up.
- Incline first Monday/Thursday; otherwise use the listed exercise order. At most one direct triceps exercise per lifting day. Working-set rest is at least two minutes; supersets are unnecessary.
- Preserve selected lifts and each slot's equipment/load conventions. An alternative requires a documented symptom/equipment decision, not an inferred program revision.
