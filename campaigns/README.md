# Campaigns

Each saved game is one folder here. A campaign folder **is** the save file — it persists
the whole game so you can stop and resume across sessions. Because this environment is
ephemeral, **commit and push a campaign folder to keep it.**

## Start a new campaign
Copy the template and rename it, then play:

```
cp -r campaigns/_TEMPLATE "campaigns/<your-campaign-name>"
```

Then tell Claude: **"Be my Storyteller — let's play Exalted."** Claude runs Session Zero
(builds your Lunar, seeds Creation and the faction board) and writes everything into your
campaign folder.

## What's in a campaign folder
The shared ruleset & Creation baseline live in the companion bridge
(`exalted3e/bridge/system-profile.md`, `setting-canon.md`); a campaign folder holds the **live
play state**:

| File | Role | Owner |
|---|---|---|
| `campaign-state.md` | the single source of truth, overwritten every scene | engine + companion |
| `setting-canon.md`  | this game's local truths (layers on `bridge/setting-canon.md`) | companion |
| `seeds.md`          | the 30–40 seed deck, refreshed each bookkeeping | engine + companion |
| `character-sheet.md`| the Lunar PC | `exalted3e` |
| `archive.md`        | resolved threads / dead NPCs / session log | engine + companion |
| `campaign_state.json` | live mechanical scratch (fights, faction seasons) — auto-created | `exalted3e` scripts |

## Resume a campaign
Tell Claude **"continue my campaign"** (name it if you have several). Claude reads that
folder's `campaign-state.md`, recaps the last beat, and resumes the Turn.

> `_TEMPLATE/` is scaffolding — never play in it directly.
