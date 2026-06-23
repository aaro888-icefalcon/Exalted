# Exalted — a solo tabletop table for Claude

A self-contained repository for playing **Exalted 3rd Edition solo** (one player, one Lunar
Exalt in Creation) with Claude as your Storyteller. It pairs a shared **engine** with an Exalted
**companion**:

- **[`mythic-gm`](.claude/skills/mythic-gm/)** — the **engine**: the *Mythic Game Master Emulator
  2e* + *The Adventure Crafter*. Content-free and shared; owns the yes/no oracle, scene tests,
  Random Events, Turning Points, and pacing, so the game surprises even the Storyteller.
- **[`exalted3e`](.claude/skills/exalted3e/)** — the **companion**: the full Exalted 3e ruleset,
  the setting of Creation, Charms, generators, and the converted rulebooks. Owns all the crunch,
  and fills the engine's hooks through its declarative [`bridge/`](.claude/skills/exalted3e/bridge/).

Together they give you an honest, GM-less game: every die is rolled in real scripts and never
fudged, the world acts to win, and consequences are real.

## How to play
1. Open this repo in Claude Code (CLI, web, or an IDE). `CLAUDE.md` loads automatically and
   tells Claude how to run the table.
2. Say: **"Be my Storyteller — let's play Exalted."**
3. Claude runs Session Zero (builds your Lunar, seeds Creation), then plays the Turn loop:
   it frames a scene, asks **"What do you do?"**, and resolves what you declare with rolled dice.
4. To stop, just stop. To resume later, say **"continue my campaign."**

Your game is saved as a folder under [`campaigns/`](campaigns/). Because this environment is
ephemeral, **commit and push your campaign folder to keep it between sessions.**

## How it's organized
```
CLAUDE.md            ← the control panel: how Claude runs a game (auto-loaded)
docs/INTEGRATION.md  ← how the companion bridges to the engine
.claude/skills/
  mythic-gm/         ← the ENGINE: Mythic GME 2e + Adventure Crafter (content-free, shared)
  exalted3e/         ← the COMPANION: Exalted 3e ruleset + setting + charms + generators + vault
    bridge/          ← the declarative hooks the engine reads (manifest + system-profile + generators…)
campaigns/
  _TEMPLATE/         ← copy this to start a new game
  <your campaign>/   ← your saves (commit them!)
```

## Requirements
`python3` (all randomness runs through the skills' scripts). No other dependencies.

## Credits & content
Exalted © Onyx Path Publishing. Mythic GME 2e and The Adventure Crafter © Tana Pigeon /
Word Mill Games. The bundled rulebook text and oracle tables are included **for personal
play**. The referee generators are design-inspired by Sine Nomine's *Godbound* (Kevin
Crawford), reimplemented with original Creation content. See each skill's `README.md` for details.
