# Campaign State — <campaign name>

> **The single source of truth.** Both skills read this every turn and overwrite it at
> scene end. If a change happened in the fiction but isn't written here, it didn't happen.
> Mechanical scratch for live fights/seasons lives alongside in `campaign_state.json`
> (maintained by the `exalted3e` scripts) — this file is the *narrative* truth.
>
> This is the **merged** state file: it carries the Exalted play tracks **and** the
> Mythic apparatus so one document serves both skills. See `docs/INTEGRATION.md`.

## Frame
- **System:** Exalted 3rd Edition — owned by the `exalted3e` skill → `system-profile.md`
- **Oracle / pacing engine:** `mythic-gm` (Fate Chart, scene tests, random events, Chaos)
- **Adventure Source mode:** Pure Mythic | Adventure Crafter | Prepared Adventure
- **Setting / canon:** Creation (Age of Sorrows) → `setting-canon.md`
- **Genre & stakes vocabulary:** mythic heroic / wuxia-tragic — meaningful cost, not a death rate
  (see `exalted3e/assets/discipline/adversity-calibration.md`)
- **Resolution:** Fate Chart (default) | Fate Check · **Chaos flavor:** normal | mid | low | no
- **Discipline:** HARDCORE (no softening; Peril Points OFF unless the player opts in)

## Turmoil ≡ Chaos Factor: 5
_(One shared 1–9 value. −1 if the PC was mostly in control of the last scene; +1 if it was
chaotic. Mythic calls it Chaos, Exalted calls it Turmoil — same number. Adjust via
`mythic-gm/scripts/state.py chaos <+1|-1> <CF>`.)_

## The Lunar (PC)
See `character-sheet.md`. Quick line: <name>, <caste>, Essence <n> · motes <p/P> · WP <n/n> ·
Limit <n/10> · anima <level> · Initiative <n> · Health <0/-1/-2/-4/Incap>.

## Intimacies
- **Defining:** …
- **Major:** …
- **Minor / Ties:** + … / − …

## Threads List (open goals & hooks; weighted, max 3 entries each)
_(Mythic Threads. Many are seeded from faction **Problems** below.)_
1.

## Characters List (NPCs & forces in play; weighted, max 3 each; the PC is NOT listed)
1.

## Adventure Features List (Prepared-Adventure mode only — set-pieces/hazards/locations)
1.

## Faction board (summary; full mechanical state via `exalted3e/scripts/ex_faction.py status`)
- <Faction> — Mag _, Goal _, Features…, Problems… (= hooks onto the Threads List)

## Clocks (offscreen factions / threats / projects ticking toward a payoff)
- none

## Overlays (Mythic; optional)
- **Keyed Scenes:** _(Trigger → Event; Count)_ none
- **Thread Progress Track:** _(Focus Thread, Track 10/15/20, points, flashpoint flag)_ none
- **Peril Points:** OFF _(player-invoked only; never used by the Storyteller)_

## Adventure Crafter state (Adventure-Crafter mode only)
- Active Turning Point: —   ·   Theme priority: Action, Tension, Mystery, Social, Personal

## Known canon revealed in play
_(Only facts the PC has actually earned. Card **Truths** stay hidden until their trigger fires.)_
- …

## Scene
- **Last beat / recap (2–3 sentences):** <the campaign opens here>
- **Adversity counter (consecutive scenes with no real cost/risk):** 0
- **Self-audit drift counter (consecutive soft scenes):** 0

## Archive pointer
- Resolved Threads / dead Characters / spent clocks → `archive.md`
