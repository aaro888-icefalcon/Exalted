# Generators — Router

LLM-facing prompt tables for solo Exalted 3e. Roll dice **only** via `scripts/ex_dice.py roll NdM` (honest, shown). Every entity is written as **Features** (what it can do) + **Problems** (named weaknesses — and Problems *are* your adventure hooks). Combinable, optional, throwaway: roll, keep what serves the scene, discard the rest.

| File | Generates | Reach for it when… |
|---|---|---|
| `ruins.md` | First Age site (purpose → hazard → inhabitants → 6 keyed rooms → reward) | PC enters a manse, tomb, shadowland, demon-prison, or any old place worth looting |
| `courts.md` | Power-group / intrigue web (structure → mood → actors w/ power sources → conflict) | PC walks into a satrap court, House seat, Lunar council, Guild caravan, or god-court |
| `communities.md` | Settlement (nature → leadership → Feature → the Problem that cries for a god) | A wandering Lunar arrives at a village/town and you need it alive in two rolls |
| `challenges.md` | Obstacle (goal-type × complication) | The PC says "I want X" and you need it to become a *scene*, not a yes |
| `cults.md` | Faith-as-faction (patron → holy-law severity → Features/Problems → growth) | A god-cult, totem-cult, Immaculate cell, or Exalt-worship congregation appears |
| `adventures.md` | Session hook (Situation + Draw + Threat + Challenge) | Starting a session and you need a reason to leave the inn |
| `foes.md` | Antagonist flavor menus + per-foe Tactics table | Statting a rival Exalt, behemoth, or spirit; pairs with `scripts/ex_npc.py` |

**Cross-refs.** Factions roll up via `setting/04_factions.md` (Magnitude/Cohesion/Trouble + Features/Problems). NPCs and stat blocks come from `scripts/ex_npc.py`. Projects/world-change use `rules/09_projects_and_dominion.md`. The Problem you roll here can be promoted straight into a faction's `Problems:` line — clearing it visibly moves the board.

**House style (applies to all files below).**
- **Problems = hooks.** No separate hook table; the weakness *is* the quest seed.
- **Complication, not first idea.** Roll the trouble *with* the entity; layer sub-rolls for texture.
- **Two-axis framing.** "How big" (Scope/tier/Magnitude) is decoupled from "how strange" (Magnitude/complication/special).
- **Nested dice.** d6 quick binary · d10/d12 menus · d20 big tables.
- **Name on arrival.** Roll blank sites/courts ahead; name them when the PC shows up; recycle the unused.
