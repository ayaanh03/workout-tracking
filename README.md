# Workout tracking

Hybrid v11 begins **Monday, October 26, 2026**, through January 3, 2027. The agent generates workouts and records results; the static dashboard displays them. No backend or build.

Every workout answers three questions:

1. **Why this workout today?** Calendar slot, achieved stage, and evidence behind changes.
2. **Exactly what do I do?** Ordered exercises, effective sets/reps/load/RIR/rest, or endurance duration, pace, effort and recovery.
3. **Was the adaptation correct?** Previous comparable actuals → applicable rule → today's decision. Missing evidence stays pending.

Ask for today's workout; afterward report actual load/reps/RIR per set or interval paces/final RPE, plus relevant symptoms and next-day recovery. The dashboard's lift form formats a report to paste into chat; it does not save records itself.

| Start here | Purpose |
|---|---|
| [program.md](program.md) | Current prescription, split by decision and training day |
| [Tracker.md](Tracker.md) | Entry point to current state |
| [state/baseline.md](state/baseline.md) | Tiny carry-forward: dated loads, 5K result, unresolved injuries |
| [history/](history/) | This block's actuals, injury reports and decisions |
| [docs/workflow.md](docs/workflow.md) | Generate, log and verify adaptations |
| [docs/dashboard.md](docs/dashboard.md) | Cache format and Watch export |
| [archive/README.md](archive/README.md) | Old records and unabridged source; excluded from ordinary generation |

Monday Upper A · Tuesday intervals · Wednesday delts/arms + bike · Thursday Upper B · Friday intervals · Saturday delts/arms + bike · Sunday legs.

Matching lifts carry over their previous working weights as starting loads, adjusted for the new reps/RIR. New or unmatched equipment stays uninitialized. Each slot progresses independently. While the ab strain recovers, use the bodyweight-only ab substitutions in recovery state; the first hard run still requires current recovery confirmation.

`index.html` reads `latest-workout.json` and `week-ahead.json`. Host the root on GitHub Pages (Settings → Pages → intended branch). `tools/workoutgen.py` builds Watch workouts in `runs/`; its fixtures/tests remain available. License: [LICENSE](LICENSE).
