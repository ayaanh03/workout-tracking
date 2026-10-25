# Current training state

Block `hybrid-2026-10-26`, program v11.0: **activated October 25, 2026**, ending January 3, 2027. The opening Sunday leg session precedes the unchanged W1 calendar, October 26–November 1. Calendar dates never advance achieved stage automatically.

| Record | Read for |
|---|---|
| [block.json](state/block.json) | Adoption, calendar, stage, manageable-week evidence, assessment choices, current-week outcomes |
| [lifting.json](state/lifting.json) | 33 independent loads, comparable actuals, qualification, dose changes, forearms, return limits |
| [running.json](state/running.json) | Independent Tue/Fri targets, actuals, recovery/counters, return paths, carried adjustments, cycling |
| [recovery.json](state/recovery.json) | Symptoms, omissions, pending gates, fatigue/observation and reduced-dose state |
| [baseline.md](state/baseline.md) | Tiny handoff: dated evidence and authorized working-weight carry-over |

JSON records are the mutable source of truth; this index is not a duplicate tracker. Null means unknown/not established, never clean, completed or zero-load. Day tables in [program.md](program.md) plus state determine the effective prescription.

Actuals: [lifting](history/lifting-log.md), [cardio](history/cardio-log.md), [injury/recovery](history/injury-log.md), [completed weeks](history/weekly-summary.md). Adaptations cite dated actuals and a rule in the [decision ledger](history/adjustments.md). [Old records](archive/README.md) are archived.
