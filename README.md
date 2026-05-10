# 🏃 Workout Tracking Dashboard

A personal training dashboard built as a single-page app served via **GitHub Pages** — no backend, no build step, just one `index.html` file and a GitHub PAT.

---

## 🎯 The Program — Sub-20 5K Training

This app is built around a structured **Sub-20 5K training plan** that combines running and hypertrophy lifting across a ~25-week program.

### 📅 Weekly Schedule

| Day | Session |
|-----|---------|
| **Sunday** | 😴 Rest + Prehab |
| **Monday** | 🏃 Easy Run + Strides (Z1, ≤143 bpm) |
| **Tuesday** | 🔥 Threshold Run + Hypertrophy A (~40 min lift) |
| **Wednesday** | 🏃 Easy Run (Z1) |
| **Thursday** | 🏃 Easy Run or Full Rest |
| **Friday** | ⚡ VO2max / Quality Session |
| **Saturday** | 💪 Long Run (Z1) + Hypertrophy B (~40 min lift) |

### 🏋️ Hypertrophy Sessions

Two lifting circuits focused on injury resilience and race-day strength:

- **Hypertrophy A (Tuesday PM)** — Incline press, lateral raises, rear-delt flyes, triceps pushdown, preacher curl, planks
- **Hypertrophy B (Saturday PM)** — Lat pulldown, chest-supported row, cable lateral raise, preacher curl, triceps pushdown, hanging knee raise, seated calf raise, soleus wall-sit

### 🫀 Heart Rate Zones (locked off max 191 bpm)

| Zone | Purpose | Range |
|------|---------|-------|
| Z1 | Easy / recovery | ≤143 bpm |
| Z2 | Threshold | 162–168 bpm |
| Z3 | VO2max | 176–183 bpm |

### 🚦 Phase Gates

The program progresses through phases — **Reset → Base → Build → Sharpen → Taper**. Phase B (Running Reintroduction) requires 7 consecutive symptom-free days, negative SI provocation tests, and a PT sign-off before unlocking higher-intensity running.

---

## 🛠️ How the App Works

**Live flow:**
1. 🔑 Log in with a GitHub PAT (stored in `localStorage`) — validates against the GitHub API to fetch your username and avatar
2. 📖 App reads `program.md` (training plan) and `Tracker.md` (your workout log)
3. ✨ AI generates today's workout brief using your actual loads and recent notes from the Tracker
4. 📝 Log your session set-by-set or via natural language → AI formats it into Markdown
5. ✅ Confirm screen shows exactly what will be appended → one-click commit to `Tracker.md` via the GitHub Contents API

**No server. No database. Your data lives in this repo.**

---

## 🤖 AI Features

- **Daily workout brief** — pulls from both `program.md` and `Tracker.md` so the AI knows your current loads, injuries, and carry-forwards. Cached in `brief-cache.json` for cross-device access.
- **Natural language logging** — describe your session in plain text; AI formats it into a structured Markdown table
- **AI Consult** — chat with your coach about any training decision; commit the decisions directly to `Tracker.md`
- **Supports Gemini 2.5 Flash** (free tier, 1,500 req/day) and **Claude Haiku** — keys injected at deploy time via GitHub Actions secrets, never committed

---

## 📁 File Map

| File | Purpose |
|------|---------|
| `index.html` | Entire app — single file, all JS/CSS inline |
| `program.md` | Sub-20 5K training program (source of truth) |
| `Tracker.md` | Workout log — appended by the app, read by AI |
| `brief-cache.json` | Daily AI brief cache for cross-device sync |
| `.github/workflows/deploy.yml` | Deploys to GitHub Pages; bakes API keys into `config.js` |

---

## 🚀 Setup

1. Fork this repo
2. Go to **Settings → Pages** and set source to **GitHub Actions**
3. Add secrets under **Settings → Secrets → Actions**:
   - `GEMINI_API_KEY` — from [Google AI Studio](https://aistudio.google.com/app/apikey)
   - `ANTHROPIC_API_KEY` — from [Anthropic Console](https://console.anthropic.com/settings/apikeys)
4. Push any change to trigger a deploy
5. Open the Pages URL, enter your GitHub PAT (needs `repo` scope), and start logging
