# Decisions — Hybrid v11

## 2026-10-24 — adoption

429. Adopt `hybrid-2026-10-26-v11` for October 26. Archive prior records verbatim under `archive/pre-hybrid-2026-10-24/` (SHA-256 manifest); retain [baseline](../state/baseline.md). Initialize stage A, 33 independent uninitialized lift slots, Tuesday 3×4 min at 6:50/mi and Friday 3×6 min at 7:25/mi, no progression credit or completed new-block exposure. Keep M6/T7/L1 omitted pending ab review; stage-A effective sets Mon/Wed/Thu/Sat/Sun = 9/7/10/6/9 (41). Current Achilles status and post-race recovery remain unknown; confirm readiness before prescribing the first hard run. Correct the old October 12 Achilles label: #416 inferred clean by default, not an explicit recovery report. Baseline 5K report is logged once under its stable result ID. October 25 remains rest. Split and condense the approved prescription without changing its progression rules; all future decisions cite current module + dated actuals.

430. Athlete instruction, 2026-10-24: carry over previous working weights for the same lifts. This supersedes #429’s all-uninitialized loading policy. Carry 160 lb incline baselines to M1a/M1b/T1; 35 lb laterals to M3/WE1/T3, 40 lb to S1; pulldown 170 to M5; chest-supported row 80 to M7; unilateral preacher 75 to WE2; bilateral rope pushdown 50 to T5. Sources/dates/actuals are in `state/lifting.json` and the archived tracker. Slots remain independent, marked `carried_unvalidated`; no new-block actuals, anchors, exposure counts or qualification credit are created. Apply the new stage/reps/RIR before issuing the effective workout: incline 160×3 RIR 1 on October 13 and a taper single on October 21 do not establish 160 for the new targets. Derive M1b from the effective top-set load and select T1 independently. Rear-delt 145 remains a conditional reference because the reverse-pec-deck equipment match is unconfirmed. New calves/abs and other unmatched movements remain uninitialized; injury, readiness and stage gates are unchanged.

## 2026-10-24 — requested Monday preview

431. Generate and publish the requested **2026-10-26, Hybrid v11 W1 Monday Upper A** preview from stage A. This is prescribed work, not a completed session. Keep the live block scheduled/Pre-block, all actuals and progression unchanged. Apply the unresolved M6 omission: 11 baseline sets minus 2 crunch sets = **9**. Numeric loads below are starting estimates, adjusted to about 3 RIR; new exercises require first-exposure load selection. Rules: `program/monday.md`, `program/ramp-and-return.md` and `program/lift-progression.md`; sources: `state/lifting.json` carry-over records.

| Slot | Exercise | Sets × reps | Planned load | RIR | Rest |
|---|---|---|---|---|---|
| M1a | Incline BB — top set | 1×4–6 | 145 lb | 3 | 3 min |
| M1b | Incline BB — back-off | 1×6–8 | 135 lb | 3 | 3 min |
| M2 | Incline DB curl | 1×8–12 | Calibrate | 3 | 2 min |
| M3 | DB lateral raise | 2×12–20 | 35 lb | 3 | 2 min |
| M4 | Overhead cable triceps extension | 2×10–15 | Calibrate | 3 | 2 min |
| M5 | Lat pulldown | 1×8–12 | 165 lb | 3 | 3 min |
| M7 | Chest-supported row | 1×8–12 | 80 lb | 3 | 3 min |

Adaptation review: October 13 incline 160×3 at RIR 1 estimates about 181 lb e1RM; 145 is a provisional 4–6-rep load at RIR 3, with 135 back-off 6.9% lighter. October 17 pulldown first set 170×8 at RIR 2 supports reducing to 165 for the extra reserve; use the next lower available setting if 165 is unavailable. Retain lateral 35 (October 13, 3×12 at RIR 3) and row 80 (October 17 first set 10 at RIR 2), stopping within the ranges at RIR 3; roughly 9 row reps is an estimate, not an actual. New incline curl/overhead extension loads stay unknown. Keep all old equipment/load conventions. Ab omission persists; actual response and current recovery remain unverified. W1 week cache is explicitly a preview with all days upcoming; future run listings are conditional plans, not clearance of the pending first-hard-run readiness gate.

## 2026-10-24 — bodyweight ab work restored

432. Athlete reports the ab strain is recovering and explicitly requests ab work without weight. Replace #431’s ab omission in the unperformed Monday preview with **M6: bodyweight decline crunch, 2×10–15, RIR 3, rest 2 min**, positioned between pulldown and chest-supported row. The other seven rows from #431 are unchanged: Monday is now **11 working sets**. Apply the same temporary bodyweight substitute to T7/L1 while recovering; stage-A Mon/Wed/Thu/Sat/Sun totals become **11/7/12/6/11 = 47**. Keep normal program cable/hanging exercise identities intact; effective substitutions, 2-set ceiling, minimum 3 RIR and no-added-load constraint live in `state/recovery.json`. Reduced-work rules may reduce further. This is a symptom-informed prescription update, not full injury clearance or a completed workout. Follow-up response remains pending; no added load, extra sets or harder baseline ab movement until reviewed. Do not transfer substitute performance into baseline exercise progression. Rebuild both preview caches and publish under the existing dashboard authorization.

## 2026-10-25 — start on Sunday

433. Athlete requests starting today, reports all recovery metrics good, and explicitly confirms Sunday should be the first leg day. Activate the existing block on October 25 and generate **Sunday Legs, bodyweight abs and calves**, stage A. This supersedes the old October 25 rest instruction. Preserve the stable block/program IDs and the October 26 calendar anchor: Monday remains Upper A, W1 is October 26–November 1, and later assessment/single/end dates do not shift. Today is a separate opening exposure, not completion of the November 1 leg session and not a completed manageable week. No stage, actuals, qualification or progression counts advance merely from activation. General recovery gate satisfied; bodyweight ab substitution and Achilles history retained.

| Slot | Exercise | Sets × reps | Planned load | RIR | Rest |
|---|---|---|---|---|---|
| L1 | Decline crunch — bodyweight | 2×10–15 | BW | 3 | 2 min |
| L2 | Leg-press calf raise | 2×10–15 | Calibrate | 3 | 2 min |
| L3 | Hack squat | 2×6–10 | Calibrate | 3 | 3 min |
| L4 | Seated leg curl | 2×8–12 | Calibrate | 3 | 2 min |
| L5 | Leg extension | 2×10–15 | Calibrate | 3 | 2 min |
| L6 | 45-degree back extension | 1×8–12 | Calibrate | 3 | 2 min |

Total: **11 working sets**. All five other leg/calf slots are new setups with no supported starting weights; calibrate within the prescribed range at RIR 3, preserving actuals as unknown until reported. Do not transfer the old seated-calf stack. L1 uses the documented bodyweight decline-crunch override. No cardio today. The weekday schedule permits Monday Upper A and Tuesday intervals; actual leg/calf recovery can modify subsequent work. Publish today’s cache with a clearly dated seven-day forward window October 25–31. Monday’s complete unperformed prescription remains recorded in #431/#432; do not mark it completed or move it to today.

## 2026-10-25 — opening session logged

434. Record the athlete’s completed **Hybrid v11 Opening Sunday** against #433: L1 BW×15/15 at RIR 4/3; L2 365×10/10 at 3/3; L3 95×6/6 at 3/3; L4 85×8/8 at 3/3; L5 100×12/15 at 3/3; L6 25×12 at 3. All **11 sets** meet prescribed rep ranges and reserve targets. Detailed actuals and original prescription are in `history/lifting-log.md`.

Apply `program/ramp-and-return.md` (stage A–C: keep appropriate loads stable) and `program/lift-progression.md` (ramp earns no progression/plateau credit): initialize L2–L6 from Calibrate → **365/95/85/100/25 lb**, then hold. L6 reaching 12 does not earn an increase; L5 did not reach 15 on both sets, independently of the ramp exclusion. Record raw exposure counts only; ordinary qualification/comparison/anchor state remains empty. Use the same equipment and reported load notation; unspecified setup details stay unknown. WE5 and other slots receive no actuals or credit from this session.

Store L1’s decline-crunch actual separately from the uninitialized hanging-leg-raise baseline. Hold **BW, maximum 2×10–15, minimum RIR 3**, with the October 24 restrictions intact. `program/adjustments.md#missing-evidence`: completed performance is not symptom clearance. Lower-ab/Achilles response was not reported, follow-up requested once, next-day recovery pending. Hold dependent restoration/clearance; do not invent pain-free tolerance, adverse symptoms or a manageable week.

Mark October 25 opening completed; remain at A with no tolerated/manageable week established. Monday Upper A and W1 October 26–November 1 remain unchanged. Preserve #433’s actual prescription in today’s dashboard, add the exact reported results, show Sunday done and update the working-load list. Do not advance the dashboard to tomorrow or mark any future session complete.

435. Follow-up to #434, same date: asked how lower abs/Achilles felt during and after the opening session; athlete answers **“Both felt fine.”** Record both local responses as tolerated during/after this exposure, superseding the corresponding pending response fields. Continue the current permitted bodyweight ab dose and established L2 calf load, subject to later recovery. Keep the bodyweight-only instruction, 2-set ceiling and minimum 3 RIR; this report does not authorize weighted abs or baseline hanging/cable work. Retain Achilles history with the explicit current symptom-free exposure. Next-day recovery remains unknown, and no full manageable week, stage advancement or progression credit is established. Rule: `program/adjustments.md` (reported evidence and separate restoration review), `program/ramp-and-return.md` (manageable week).

## 2026-10-26 — Monday Upper A

436. Athlete reports **“Recovery metrics look good.”** Record next-day general recovery as good after the completed opening leg session; no numeric or new site-specific symptom report supplied. Keep October 25’s explicit tolerated ab/Achilles exposure and all active ab limits. Move the calendar to **W1 October 26–November 1**, with Stage A unchanged: one opening session does not establish a manageable week. Generate today’s **Monday Upper A**, not completed, prescription ID `hybrid-2026-10-26-mon-upper-a-436`.

| Slot | Effective exercise | Sets × reps | Planned load | RIR | Rest |
|---|---|---|---|---|---|
| M1a | Incline barbell bench — top set | 1×4–6 | 145 lb | 3 | 3 min |
| M1b | Incline barbell bench — back-off | 1×6–8 | 135 lb | 3 | 3 min |
| M2 | Incline DB curl | 1×8–12 | Calibrate | 3 | 2 min |
| M3 | DB lateral raise | 2×12–20 | 35 lb | 3 | 2 min |
| M4 | Overhead cable triceps extension | 2×10–15 | Calibrate | 3 | 2 min |
| M5 | Lat pulldown | 1×8–12 | 165 lb | 3 | 3 min |
| M6 | Decline crunch — bodyweight | 2×10–15 | BW | 3 | 2 min |
| M7 | Chest-supported row | 1×8–12 | 80 lb | 3 | 3 min |

**11 working sets; no cardio.** Retain the effective Monday loads from #431/#432 after reconciling Sunday’s actuals and today’s recovery. Source/rule review: `program/monday.md`, `program/ramp-and-return.md`, `program/lift-progression.md` and dated carry-over sources in `state/lifting.json`. October 13 incline 160×3 at RIR 1 estimates 181.3 lb e1RM: provisionally choose 145 for 4–6 at RIR 3 and 135 for 6–8, a 6.9% back-off. October 17 pulldown 170×8 at RIR 2 supports 165 for extra reserve; use the next lower setting if 165 is unavailable. Retain lateral 35 (October 13, 3×12 at RIR 3) and row 80 (October 17 first set 10 at RIR 2), stopping at RIR 3; approximately 9 row reps is an estimate, not a recorded actual. M2/M4 need independent calibration. Preserve existing apparatus and load conventions.

October 25 bodyweight decline crunch 15/15 at RIR 4/3 felt fine during/after; good general recovery today supports repeating the permitted dose in M6. Keep BW, two-set ceiling and minimum 3 RIR; no transfer of Sunday actuals or progression credit into M6, no weighted/baseline ab restoration. All numeric carry-over prescriptions remain provisional until performed; no new actuals, qualification, anchors or stage advancement created.

Publish current-day caches with Monday marked today and six upcoming W1 days, including a separate November 1 leg session. Preserve the October 25 actuals/opening completion and established lower-body loads. Future work remains subject to its current recovery review.
