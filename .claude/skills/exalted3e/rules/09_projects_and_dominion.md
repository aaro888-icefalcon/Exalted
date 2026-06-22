# Domain play — changing Creation & the faction board

The solo Lunar's late game: turning a Heart's-Blood-won tribe into a confederation, a ruin into a manse-seat, a satrapy into a rebellion.

## Changing Creation (a Project) — `python3 scripts/projects.py cost --scope <s> --mag <m> [--opp N]`
Cost = **Scope** (hamlet 1 · town/city 2 · region 4 · nation/Great House 8 · a Direction/the Realm 16) × **Magnitude** (plausible ×1 · improbable ×2 · impossible ×4) + **Opposition** (wards, rival Exalts, gods — sum). Pay from Resources, Backgrounds, downtime intervals, and faction **Reach**. **Impossible** goals require **Mighty Deeds** — i.e. adventures — to buy the cost down. **Permanent** if backed by lasting investment (a built institution, a sworn faction); **reverts** if held only by personal attention. A finished Project becomes a new faction **Feature** (and a backlash **Problem**).

## The faction board — `python3 scripts/ex_faction.py`
Every power is a stat block: `Magnitude 1–5 (die d6→d20) · Cohesion · Trouble (Σ Problems; ≥ die-max → collapse) · Features · Problems · Interest · Reach · Goal`. The starting board lives in `setting/04_factions.md`.
- `add <name> --mag M --goal <tyrant|conqueror|survivor|schemer|theocrat|predator> [--feature ..] [--problem ..]`
- `turn` — run a season: each faction acts in random order (Consolidate / Strike), dice shown; surfaced **Problems become Threads/hooks**.
- `strike <A> <B>` — opposed Contest; loser gains a Problem.

**The PC edits the board with no dice:** kill a House's star Dragon-Blood → its Feature drops; resolve a famine → delete that Problem; found a cult (`generators/cults.md`) → +Feature and a backlash Problem. Clearing Problems is visible progress — that's the agency loop.
