# CLAUDE.md — Workout Tracking via Claude Code

This repo is a two-file training system driven by Claude Code chats. No app, no UI.

- `program.md` — the prescribed 27-week Sub-20 5K + hypertrophy program (v4.4 re-anchor; race = W27 Sat Oct 24). Source of truth for what's *prescribed*.
- `Tracker.md` — the running log: status, current working loads, carry-forwards, lifting/cardio logs. Source of truth for what's *been executed* and current state.
- `latest-workout.json` — machine-readable cache of today's brief. Rendered by `index.html` (GitHub Pages) for at-the-gym viewing.
- `week-ahead.json` — machine-readable cache of the current program week (7-day glance). Also rendered by `index.html`.

Each day has two interactions:

1. **Morning** — user asks for today's workout. You read both md files, output the brief in chat, AND write `latest-workout.json` + (when needed) `week-ahead.json`, then commit + push so the dash reflects the new brief.
2. **Post-session** — user dumps what they did. You append a structured entry to `Tracker.md`, update load/carry-forward tables, regenerate the affected JSON caches, commit, and push.

The conversation IS the interface for input; the dash is the read-only output surface at the gym. Be terse. Tables over prose. Numbers over adjectives. No emoji, no encouragement, no "let me know how it goes".

> **TIME ZONE — always operate in US Eastern (America/New_York, EST/EDT).** The athlete trains on Eastern time. The system-context date may be UTC and can be a calendar day *ahead* in the evening (e.g. UTC shows Friday while it is still Thursday night ET). **Before resolving today's date or day-of-week, convert the system timestamp to America/New_York and use that.** When in doubt, derive ET explicitly (e.g. `TZ="America/New_York" date "+%Y-%m-%d %A"`) rather than trusting the raw system date. Every `{YYYY-MM-DD}`, `{Day}`, commit-message date, and JSON `date`/`generatedAt` field uses ET. `generatedAt` carries the ET offset (`-04:00` EDT / `-05:00` EST).

---

## Morning brief

Triggers: "what's today", "today's workout", "workout of the day", "give me the workout", or any variant.

### Steps

1. Resolve **today's date and day-of-week** in **US Eastern time** (America/New_York) — convert the system-context timestamp to ET first; do not trust a raw UTC date, which can read one day ahead in the evening.
2. Read `program.md` and `Tracker.md` **in full** (not partial — context matters).
3. Determine **week number and phase** from `Tracker.md ## Status` + most-recent log entries cross-referenced against `program.md §1`.
4. Look up today's session via `program.md §2` (weekly template) + the phase-specific section (`§4.B` Reset / `§4.C` Base / `§4.D` Build / `§4.E` Sharpen / `§2.C` Taper for cardio; `§3.A`/`§3.B` for lifts).
5. Pull **loads from `Tracker.md ## Current Working Loads`**, never from program.md projections.
6. Apply any **carry-forwards** from `Tracker.md ## Adjustments / Carry-forwards` that touch today (bump-eligible loads, ordering rules, exercise subs, paused additions, etc.).
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
1a. **Ask about what's worth logging but missing.** Before writing anything, scan the dump for gaps in the metrics that matter and ask them back in **one batched message** (don't interrogate set-by-set across turns). Worth asking when absent:
   - Per working set: **RPE / RIR** — especially on bump-eligible lifts.
   - Lifts: actual load/reps where a set is ambiguous; **tennis-elbow status** (any symptoms on preacher/pushdown — tracks the §10.A 4-wk clock, Adj #72).
   - Runs: **avg/split pace, avg & max HR, cadence, surface** (treadmill/road/track).
   - **SI / sciatica status** (AM / pre / during / post) when a flare or prehab is in play.
   - Anything a carry-forward says to **test today** (the "clean" condition).
   Skip questions the dump already answers, and don't block on truly soft context (a missing accessory cue). If the user still doesn't have a number after asking, log it as "not recorded" — never guess.
2. **Append a new entry** under `## Lifting Log` and/or `## Cardio Log`:
   - Header: `### W{wk} {Day} {YYYY-MM-DD} — {Session Name}`
   - Lift table columns (match existing): `|Exercise|Sets|Notes|`
   - Cardio table: append a row under the existing `## Cardio Log` table (don't make a new sub-table for one session).
   - End the entry with a `> AI: {one paragraph}` summary — what bumped, what held, what carried forward, anything off-protocol. Match the prose style and density of existing summaries (read the last 2–3 to calibrate).
3. **Update `## Current Working Loads`** for any load that bumped, held, or changed status. Update the "Last verified" column to today and rewrite the Note column with what just happened.
4. **Update `## Adjustments / Carry-forwards`**:
   - Add new numbered entries for anything that carries into the next session.
   - When a new entry resolves an existing one, cite it ("Adj #3 hold-until-clean **satisfied**" style — match existing wording).
   - Don't renumber or delete old entries; the list is append-only and entries become historical context.
5. **Update `## Weekly Summary`** — mark today's day in the current week's row (`✓ {Session} {date}`). Add a new row if it's a new week.
6. **Update `## SI / Sciatica Log`** if SI status was reported (AM / pre / during / post / notes).
7. **Update `## Incline BB Progression`** Actual column if today was an Incline BB session.
8. **Regenerate `latest-workout.json` and `week-ahead.json`:**
   - In `latest-workout.json`: refresh `currentLoads` to match Tracker.md after your updates.
   - In `week-ahead.json`: flip today's `status` from `today` to `done`, update its `note` with what actually happened (e.g. "Logged — lat 130→135 clean RIR 3 ×4"), and bump tomorrow's status to `today`. Update `summary` if a major carry-forward flipped (a bump landed, a hold satisfied, a new flare, etc.).
9. **Commit & push:**
   - Branch: keep working on whatever branch the session started on (typically `claude/rebuild-workout-dashboard-403SR` or whatever is current).
   - Commit message format, matching existing history: `Log W{wk} {Day} {Session} — {YYYY-MM-DD}` (e.g. `Log W5 Sat Hyp B — 2026-05-23`). The JSON updates go in the same commit as the Tracker.md update.
   - `git push -u origin <branch>`.

### What NOT to do

- **Don't reformat unrelated sections** of `Tracker.md`. Append/update only what today's session warrants.
- **Don't create the entry** without the data — ask for the loggable metrics in step 1a (RPE/RIR, pace/HR/cadence, soleus hold, SI status, any "clean" test) in one batched message first. Don't interrogate over accessory cues or other soft context.
- **Don't summarize on the user's behalf.** The `> AI:` line should reflect what actually happened, not a coaching pep talk.
- **Don't open a PR** unless the user explicitly asks.

---

## Determining today's session (quick reference)

Cross-reference against `program.md §2`:

| Day | Default session |
|---|---|
| Sun | Off / SI prehab (Tyler twists, reverse Tyler, McGill Big 3) |
| Mon | Z1 easy run + strides (hill strides Phase B+) |
| Tue | Threshold (run or row) — run only |
| Wed | **Hyp A** lift (no run; upper-dominant + soleus wall-sit) |
| Thu | Z1 easy run (revert to rest on yellow/red days per §11.C) |
| Fri | VO2max / Quality (T session in Base; intervals in Build) |
| Sat | Long run AM + **Hyp B** PM (≥6h gap; push to Sun if hard) |

Phase determines the cardio prescription:

- Reset W1–W4 → `§4.B`
- Base W5–W14 → `§4.C` (v4.4 re-anchor, Adj #71)
- Build W15–W20 → `§4.D`
- Sharpen W21–W24 → `§4.E`
- Taper W25–W27 → `§2.C` (race = W27 Sat Oct 24)

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
