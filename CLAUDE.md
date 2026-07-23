# CLAUDE.md — Workout Tracking via Claude Code

This repo is a training system driven by Claude Code chats — two lean files (`program.md`, `Tracker.md`), per-stream history files under `history/`, and two JSON caches. No app, no UI.

- `program.md` — **lean, current prescription only.** The 25-week Sub-20 5K + hypertrophy program: macrocycle table, weekly template, phase-by-phase run progression, lift circuits, strength progression, rules (SI, tennis elbow, autoregulation), quick reference. Source of truth for what's *prescribed right now*. Historical rationale for why the prescription changed lives in `program-history.md`, cited via a one-line pointer at each revision point.
- `program-history.md` — **everything historical for the program side.** Chronological changelog of *why* the prescription changed (template revisions, mileage reshapes, etc.), newest at the bottom, ordered by date. `program.md` never holds this prose — it only holds short pointers into this file.
- `Tracker.md` — **lean, current-state only.** Status, Current Working Loads, Active Flags, Shoe Rotation, the latest Incline BB Progression row, the latest Weekly Summary row. Source of truth for what's *true right now*. This is the file the morning brief reads for loads/flags — it carries no session-by-session log detail.
- `history/` — **everything historical for the tracker side, one append-only file per stream; live files hold only the current phase (Build W13+):** `history/adjustments.md` (the numbered ledger, Adj #164+), `history/lifting-log.md`, `history/cardio-log.md`, `history/si-log.md`, `history/weekly-summary.md` (completed weeks), `history/incline-bb.md` (current meso, whole). Every live file's append point is **end of file**. Completed phases live verbatim in `history/archive/`. `Tracker.md` cites an Adj # or week; to resolve a cited Adj #N: `grep -rn '^N\. ' history/` — **never read a history file in full.**
- `Tracker-history.md` — **pointer stub only** (kept because hundreds of immutable old entries cite it by name; it maps old sections to their new homes). Never append here.
- `latest-workout.json` — machine-readable cache of today's brief. Rendered by `index.html` (GitHub Pages) for at-the-gym viewing.
- `week-ahead.json` — machine-readable cache of the current program week (7-day glance). Also rendered by `index.html`.

Each day has two interactions:

1. **Morning** — user asks for today's workout. You read the two **lean** files (`program.md` + `Tracker.md`) in full — the history files are not needed to generate a brief. Output the brief in chat, write `latest-workout.json` + (when needed) `week-ahead.json`, then commit + push so the dash reflects the new brief.
2. **Post-session** — user dumps what they did. You append the structured session entry to the matching **`history/` files** (lifting-log / cardio-log / si-log / adjustments), then update `Tracker.md`'s current-state sections (Current Working Loads, Active Flags, latest Incline BB row, current Weekly Summary row) to match, regenerate the affected JSON caches, commit, and push.

The conversation IS the interface for input; the dash is the read-only output surface at the gym. Be terse. Tables over prose. Numbers over adjectives. No emoji, no encouragement, no "let me know how it goes".

> **TIME ZONE — always operate in US Eastern (America/New_York, EST/EDT).** The athlete trains on Eastern time. The system-context date may be UTC and can be a calendar day *ahead* in the evening (e.g. UTC shows Friday while it is still Thursday night ET). **Before resolving today's date or day-of-week, convert the system timestamp to America/New_York and use that.** When in doubt, derive ET explicitly (e.g. `TZ="America/New_York" date "+%Y-%m-%d %A"`) rather than trusting the raw system date. Every `{YYYY-MM-DD}`, `{Day}`, commit-message date, and JSON `date`/`generatedAt` field uses ET. `generatedAt` carries the ET offset (`-04:00` EDT / `-05:00` EST).

---

## Morning brief

Triggers: "what's today", "today's workout", "workout of the day", "give me the workout", or any variant.

### Steps

1. Resolve **today's date and day-of-week** in **US Eastern time** (America/New_York) — convert the system-context timestamp to ET first; do not trust a raw UTC date, which can read one day ahead in the evening.
2. Read `program.md` and `Tracker.md` **in full** (the lean files — not partial, and the history files aren't needed for this).
3. Determine **week number and phase** from `Tracker.md ## Status`.
4. Look up today's session via `program.md §2` (weekly template) + the phase-specific section (`§4.B` Reset / `§4.C` Base / `§4.D` Build / `§4.E` Sharpen / `§2.C` Taper for cardio; `§3.A`/`§3.B` for lifts).
5. Pull **loads from `Tracker.md ## Current Working Loads`**, never from program.md projections.
6. Apply any **active flags** from `Tracker.md ## Active Flags` that touch today (bump-eligible loads, ordering rules, exercise subs, paused additions, etc.). If a cited Adj # needs fuller context, grep for it: `grep -rn '^{n}\. ' history/` (hits the live ledger or the archive — don't read either in full).
7. Output the brief in chat in the exact format below.
8. **Write `latest-workout.json`** matching the schema in the "JSON caches" section. Include the full current-loads table from Tracker.md so the dash has everything in one fetch.
9. **If `week-ahead.json` is stale** (different week than today, or any day's status is wrong relative to current state), regenerate it too.
10. **Commit & push** the JSON change(s) on the current branch. Commit message: `Cache brief — {YYYY-MM-DD}` (and `+ week-ahead` suffix if both updated). No PR.

### Output format (strict)

The brief is **three tables — Warmup, Work, Cooldown** — each readable row-by-row into the Apple Watch workout app. No multi-line intro, no Targets/Cues paragraphs, no per-exercise Cue column. The only non-table lines are an optional one-line flag at the top and an optional one-line **Notes** at the bottom — each kept *only* when a carry-forward materially changes today, otherwise omitted entirely. Detail/cues get discussed at logging anyway, so don't pre-load them here.

Each block uses **the modality's own columns**. Lift days are unchanged from before; cardio days carry pace/HR/cadence on *every* segment (warmup and cooldown included, not just the work set).

**Lift day** — Warmup/Cooldown use `Segment | Time/Sets | Target`; Work uses `Exercise | Sets×Reps | Load | RIR | Rest`:

```
**{Wk} {Day} {YYYY-MM-DD} — {Session name}**

{Optional ONE line — only if a carry-forward changes today (a bump landing, an ordering rule, a flare caveat). Cite Adj #. Omit otherwise.}

## Warmup

| Segment | Time/Sets | Target |
|---|---|---|
| ... | ... | ... |

## Work

| Exercise | Sets×Reps | Load | RIR | Rest |
|---|---|---|---|---|
| ... | ... | ... | ... | ... |

## Cooldown

| Segment | Time/Sets | Target |
|---|---|---|
| ... | ... | ... |

**Notes:** {one line, only if important — bump-eligibility test ("clean RIR 2 on set 3 → bump next"), ordering rule, flare flag. Cite Adj #. Omit if nothing material. Never restate a table.}
```

**Cardio day** — all three blocks use `Segment | Time/Dist | Pace | HR | Cadence`; fill pace/HR/cadence on the WU build and CD jog rows too:

```
**{Wk} {Day} {YYYY-MM-DD} — {Session name}**

{Optional ONE line — carry-forward flag. Cite Adj #. Omit otherwise.}

## Warmup

| Segment | Time/Dist | Pace | HR | Cadence |
|---|---|---|---|---|
| ... | ... | ... | ... | ... |

## Work

| Segment | Time/Dist | Pace | HR | Cadence |
|---|---|---|---|---|
| ... | ... | ... | ... | ... |

## Cooldown

| Segment | Time/Dist | Pace | HR | Cadence |
|---|---|---|---|---|
| ... | ... | ... | ... | ... |

**Notes:** {one line, only if important — surface/nasal-gate caveat, HR caveat, ordering. Cite Adj #. Omit if nothing material.}
```

**Combined Sat (lift + cardio):** split each block by modality — `### Warmup — Cardio` (cardio columns) + `### Warmup — Lift` (lift columns); two Work tables `### Work — Cardio` / `### Work — Lift`; same for Cooldown.

### Defaults to apply

- **Rest** if not stated in program.md:
  - Strength (Incline BB, 3×5–8): 2–3 min
  - Hypertrophy mid-rep (8–12, RIR 2): 90–120s
  - Accessories / iso (12–15, RIR 1–2): 60–90s
  - Soleus wall-sit between holds: 60s
- **Lift warmup** for the day's compound (currently Incline BB on Wed):
  - bar × 8, 95 × 5, 115 × 3, then working sets
- **General lift warmup:** 1–2 min dynamic (band pull-aparts, scap push-ups, hip openers — pick what fits the day).
- **Run cooldown:** 5–10 min easy + SI prehab on quality days.

### Carry-forward application rules

- A "→ bump next" entry in Current Working Loads that targets today's session **becomes** today's prescribed load — output the new load directly in the Load column and call out the bump in the top flag line.
- An "ordering" or "off-protocol" Adjustment that touches today (e.g. Adj #16 "restore run AM, lift PM ≥6h gap") → surface in the top flag line.
- A "hold-until-clean" Adjustment whose testing instance is today → put it in **Notes** and state what "clean" means here (e.g. "clean RIR 2 on set 3 → bump-eligible next").

---

## Logging the session

Triggers: user reports what they did — could be a structured dump, a paragraph, or fragmentary ("did Hyp A, 135×5 across, soleus 50s, tri pushdown bumped to 55").

### Steps

1. **Parse** exercise-by-exercise, set-by-set.
1a. **Default-fill context, prompt for numbers (Adj #188/#190, athlete directives 2026-07-19).** Log from the dump without interrogating over context — but do collect missing metrics:
   - **No-news-is-clean:** SI / tendon / pain status not mentioned logs as clean — including AM-read and pain-gated conditions. The athlete reports exceptions, not confirmations; an unmentioned gate reads as passed. Never ask about status.
   - **Fed** assumed unless stated. **Shoe / surface / WU / CD** assumed to match the last comparable session or the prescription. Never ask about these either.
   - **Missing numbers ARE prompted (Adj #190):** metrics absent from the dump that belong in the log — RPE/RIR on working sets (especially bump-eligible lifts), ambiguous loads/reps, pace/splits, HR, cadence, hold times — get **one compact message listing them all** before the entry is written. Whatever the athlete doesn't have logs as "n/r" — never invented.
   - Beyond that one numbers prompt, ask only for a **genuine blocker** — an ambiguity that changes a bump/hold/gate decision (e.g. "135×5 across" on a day 140 was prescribed).
2. **Append the session entry to the live history file(s)** — every live file's append point is **end of file** (not to the lean `Tracker.md` — that file holds no session-by-session detail):
   - Lift session → end of `history/lifting-log.md`. Header: `### W{wk} {Day} {YYYY-MM-DD} — {Session Name}`; table columns (match existing): `|Exercise|Sets|Notes|`.
   - Cardio session → append a row at the end of `history/cardio-log.md` (the log table is the last block in that file; don't make a new sub-table for one session).
   - End a lift entry with a `> AI: {one paragraph}` summary — what bumped, what held, what carried forward, anything off-protocol. Match the prose style and density of existing summaries (read the last 2–3 to calibrate).
3. **Append new numbered entries to the end of `history/adjustments.md`**:
   - Add entries for anything that carries into the next session.
   - When a new entry resolves an existing one, cite it ("Adj #3 hold-until-clean **satisfied**" style — match existing wording).
   - Don't renumber or delete old entries; the ledger is append-only and entries become historical context (completed phases rotate to `history/archive/`, never get pruned).
4. **Append a row to the end of `history/si-log.md`** if SI/tendon status was actually reported (AM / pre / during / post / notes) — no-news-is-clean days get no row (Adj #188).
5. **Update `history/incline-bb.md`** — fill today's actual in the forecast table if today was an Incline BB session.
6. **Mark today in `Tracker.md ## Weekly Summary`** (`✓ {Session} {date}` in the current week's row — this is the only place the in-progress week is tracked). **When a week closes** (its last session logs), append the completed row to the end of `history/weekly-summary.md` and start the new week's row in `Tracker.md`.
7. **Sync the lean `Tracker.md`** so it reflects the new current state — this is the only writing `Tracker.md` itself gets:
   - **`## Current Working Loads`**: update any load that bumped, held, or changed status. Update "Last verified" to today and rewrite the Note column with what just happened.
   - **`## Active Flags`**: add/remove/reword bullets so the list matches what's actually open after today (resolved flags drop off; new ones get added, citing the new Adj #).
   - **`## Status`**: update if the phase/week boundary or a locked value (HR, mileage ceiling, etc.) changed today.
   - **`## Incline BB Progression`**: overwrite the single latest row (mirroring `history/incline-bb.md`) — `Tracker.md` keeps only the current/latest row, never a growing history. (`## Weekly Summary` was already handled in step 6.)
8. **Regenerate `latest-workout.json` and `week-ahead.json`:**
   - In `latest-workout.json`: refresh `currentLoads` to match Tracker.md after your updates.
   - In `week-ahead.json`: flip today's `status` from `today` to `done`, update its `note` with what actually happened (e.g. "Logged — lat 130→135 clean RIR 3 ×4"), and bump tomorrow's status to `today`. Update `summary` if a major carry-forward flipped (a bump landed, a hold satisfied, a new flare, etc.).
9. **Commit & push:**
   - Branch: keep working on whatever branch the session started on (typically `claude/rebuild-workout-dashboard-403SR` or whatever is current).
   - Commit message format, matching existing history: `Log W{wk} {Day} {Session} — {YYYY-MM-DD}` (e.g. `Log W5 Sat Hyp B — 2026-05-23`). The `Tracker.md` + touched `history/` files + JSON updates go in the same commit.
   - `git push -u origin <branch>`.

### Changing the prescription (rare)

If a session's outcome warrants changing `program.md` itself (a permanent template change, a mileage reshape, a phase boundary move — not a routine load bump, which is a `Tracker.md` carry-forward, not a prescription change):

1. Edit `program.md` directly so it reflects the **new** prescription — it always describes what's current, never what used to be true.
2. Add a new dated entry to the bottom of `program-history.md` explaining what changed and why (cite the driving Adj # from `history/adjustments.md`).
3. Leave a short one-line pointer in `program.md` at the revision point (e.g. `*Template revision history ... in program-history.md.*`) rather than inline rationale prose.

### History files — rotation

- **At each phase boundary** (Build→Sharpen after the last W20 log; Sharpen→Taper after W24; post-race — renumbered per Adj #204), move the completed phase's content **verbatim** out of each live `history/` file into `history/archive/{stream}-W{a}-W{b}.md` (the ledger archives by number range: `adjustments-{first}-{last}.md`). Update the live file's header to state the new archived ranges, and record the rotation as a new Adj #. `history/incline-bb.md` rotates whole at meso boundaries, not phase boundaries.
- **Backstop:** if any live history file grows past **~40 KB** mid-phase, roll its oldest completed weeks into that phase's archive file early — same mechanics.
- **Moves are line-range cut/paste (sed/awk), byte-verbatim** — never retype, reformat, or summarize content while moving it. Verify with checksums/`cmp` before committing.

### What NOT to do

- **Don't reformat unrelated sections** of `Tracker.md` or the `history/` files. Append/update only what today's session warrants.
- **Don't let session-by-session detail accumulate in `Tracker.md`.** Full logs, the full Adjustments ledger, and full weekly history belong in `history/` only — `Tracker.md` stays lean.
- **Don't read any history file in full** — grep for the Adj #, date, or exercise you need; read only the matching lines plus a little context (the last 2–3 entries for style calibration are fine).
- **Don't append to `Tracker-history.md`** — it's a pointer stub only.
- **Don't interrogate over context.** Statuses and conditions default-fill per step 1a (assume-same-as-last, no-news-is-clean). Missing numbers get exactly one compact prompt (Adj #190); anything still unknown logs "n/r". No status questions, no soft-context questions, no set-by-set back-and-forth across turns.
- **Don't summarize on the user's behalf.** The `> AI:` line should reflect what actually happened, not a coaching pep talk.
- **Don't open a PR** unless the user explicitly asks.

---

## Determining today's session (quick reference)

Cross-reference against `program.md §2`:

| Day | Default session |
|---|---|
| Sun | Off / SI prehab (Tyler twists, reverse Tyler, McGill Big 3) |
| Mon | Z1 easy run + strides (hill strides Phase B+) |
| Tue | **Hyp A** lift (no run; upper-dominant) |
| Wed | Threshold (run or row) — run only (relocated from Tue, per §2.A 2026-06-16) |
| Thu | **Off** — mobility / walk, daily SI prehab (permanently off per §2.A 2026-06-16) |
| Fri | VO2max / Quality (T session in Base; intervals in Build) |
| Sat | Long run AM + **Hyp B** PM (≥6h gap; push to Sun if hard) |

Phase determines the cardio prescription:

- Reset W1–W4 → `§4.B`
- Base W5–W12 → `§4.C`
- Build W13–W20 → `§4.D`
- Sharpen W21–W24 → `§4.E`
- Taper W25–W27 → `§2.C`

Lift volume/prescription is in `§3.A` (Wed) and `§3.B` (Sat).

---

## JSON caches

Two files at the repo root, both consumed by `index.html` (which is served on GitHub Pages).

### `latest-workout.json`

One file, overwritten each morning. The dash renders sections only if present, so set `lift: null` on cardio-only days and `cardio: null` on lift-only days.

```json
{
  "generatedAt": "2026-05-20T07:30:00-04:00",
  "week": "W5",
  "day": "Wed",
  "date": "2026-05-20",
  "phase": "Base",
  "sessionName": "Z1 easy run 25 min",
  "intro": ["line 1", "line 2"],
  "lift": {
    "table": [
      { "exercise": "Incline BB", "setsReps": "3×5", "load": "135", "rir": "2", "rest": "2–3 min", "cue": "RPE 7; +5 lb next Tue if clean" }
    ],
    "warmup": "Incline BB: bar×8, 95×5, 115×3, then working. General: 1–2 min band pull-aparts.",
    "cooldown": "SI prehab — Tyler twists 3×15, reverse Tyler 3×15, McGill Big 3 5-3-1"
  },
  "cardio": {
    "flags": ["..."],
    "workout": "4×5 min @ T (1 min jog rec), 1% incline",
    "targets": { "pace": "7:55–8:10/mi", "hr": "...", "cadence": "175–182 spm" },
    "warmup": "1.0–1.5 mi easy build to T pace",
    "cooldown": "1.0 mi easy / Z1",
    "cues": ["...", "..."]
  },
  "currentLoads": [
    { "exercise": "Incline BB", "load": "135 working / TM 165", "lastVerified": "W5 Tue 5/19", "note": "..." }
  ]
}
```

Rules:
- Strings only — no markdown formatting in field values (the dash renders plain text).
- Keep the JSON as lean as the chat brief. `intro` holds at most the one top-flag line (`[]` if nothing material). `cues` and `flags` are `[]` unless a cue/flag is genuinely important — don't pad them. The dash renders these only when non-empty.
- `currentLoads` mirrors `Tracker.md ## Current Working Loads` row-for-row (Exercise, Load, Last verified, Note) at the time of generation.

### `week-ahead.json`

One file, regenerated when the week rolls over or when status changes (a session got logged, a flag got resolved).

```json
{
  "generatedAt": "2026-05-20T07:30:00-04:00",
  "week": "W5",
  "phase": "Base",
  "summary": "Base W5 — ~14 mpw, polarized 85% Z1. Sat is high-bump day...",
  "days": [
    { "date": "2026-05-18", "day": "Mon", "session": "Z1 easy 30 min", "note": "Logged — strides skipped", "status": "done" },
    { "date": "2026-05-20", "day": "Wed", "session": "Z1 easy 25 min", "note": "Recovery aerobic; nasal-gate (Adj #9)", "status": "today" },
    { "date": "2026-05-23", "day": "Sat", "session": "Long Z1 + Hyp B", "note": "Bumps: lat 130→135, calf +10–20...", "status": "upcoming" }
  ]
}
```

Rules:
- `days` covers the current program week, Mon → Sun (7 entries always — include Sun as "Off / SI prehab" even though it's a rest day).
- `status` is one of: `done`, `today`, `upcoming`.
- `note` is short (one line). For done days, summarize what actually happened. For upcoming days, surface flags / bumps / orderings.
- `summary` is one paragraph capturing the week's theme + the biggest flags.

---

## Style rules (apply everywhere)

- Cite **section numbers** when applying a prescription (`per §3.A`, `per §4.C W5 Tue`).
- Cite **Adj #** when applying a carry-forward.
- Numbers over adjectives. `RIR 2`, not "hard". `8:00/mi`, not "fast".
- No emoji. No exclamation marks. No "great session!" / "you got this".
- The brief is three tables — **Warmup, Work, Cooldown**. The only non-table lines are the optional top flag and optional **Notes**, one line each, kept only when a carry-forward materially changes today. No intro paragraph, no cues/targets bullets.
- Loads from `Current Working Loads`, never from `program.md` projection tables.
- The brief is for execution. Strip anything the user doesn't need at the gym — detail gets covered at logging.
