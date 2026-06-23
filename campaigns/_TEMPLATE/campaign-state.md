# Campaign State — <campaign name>

> **The single source of truth.** Overwrite this at the end of **every** scene. If a change
> happened in the fiction but isn't written here, it didn't happen. Live mechanical scratch for
> in-progress fights/seasons lives alongside in `campaign_state.json` (maintained by the
> `exalted3e` scripts) — this file is the *narrative* truth.
>
> **Architecture:** the `mythic-gm` engine is the oracle/scene/Chaos/pacing layer; the `exalted3e`
> companion (its `bridge/`) supplies the ruleset, Creation, and generators. This one file carries
> both the Mythic apparatus and the Exalted play tracks.

## Frame
- **Adventure Source mode:** Pure Mythic | Adventure Crafter | Prepared Adventure
- **System / resolution:** Exalted 3rd Edition → companion `exalted3e/bridge/system-profile.md`
- **Setting / canon:** Creation (Age of Sorrows) → `exalted3e/bridge/setting-canon.md` + this campaign's `setting-canon.md`
- **GM lens / agenda:** `exalted3e/bridge/interpretation.md` (Creation-as-Threat primary; Creation-as-Cost secondary)
- **Genre & stakes vocabulary:** <e.g. mythic-tragic — meaningful cost, not a death rate>
- **Resolution:** Fate Chart (default) | Fate Check   ·   **Chaos flavor:** standard (`bridge/chaos-tendency.md`)
- **Discipline:** HARDCORE (no softening; Peril Points OFF unless the player opts in)

## Turmoil ≡ Chaos Factor: 5
_(One shared 1–9 value — Exalted's Turmoil and Mythic's Chaos are the same number. −1 if the PC was
mostly in control of the last scene; +1 if it was chaotic. Adjust via
`mythic-gm/scripts/state.py chaos <+1|-1> <CF>`. Floor per `bridge/chaos-tendency.md`.)_

## CURRENT ADVENTURE: <title>
_Each adventure has its own Threads & Characters Lists and its own Theme priority (rolled from
`bridge/theme-weights.md`). A new adventure begins when the current main Thread(s) reach a
Conclusion (Threads List empties of active goals) — then roll new Themes, start fresh Lists, carry
over only what stays relevant, archive the rest._
- **Adventure status:** active | concluding | concluded
- **Theme priority (this adventure):** 1.Tension 2.Personal 3.Social 4.Action 5.Mystery  _(rolled per bridge weights)_

## The Lunar (PC)
See `character-sheet.md`. Quick line: <name>, <caste>, Essence <n> · motes <p/P> · WP <n/n> ·
Limit <n/10> · anima <level> · Join Battle <n> · Defense <n> (Parry/Evasion) · Resolve <n> · Guile <n> ·
Soak <n> · Health <track>. Mask/disguise: <…>. Spirit shape: <…>.

## Intimacies
- **Defining:** … · **Major:** … · **Minor / Ties:** + … / − … · **Limit trigger:** …

## Threads List (this adventure; open goals & hooks; weighted, max 3 each)
_(Many are seeded from faction **Problems** below — Problems are hooks.)_
1.

## Characters List (this adventure; NPCs & forces; weighted, max 3 each; the PC is NOT listed)
1.

## Adventure Features List (Prepared-Adventure mode only — set-pieces/hazards/locations)
1.

## Campaign roster (persists across adventures: recurring NPCs, long arcs)
-

## Faction board (summary; full mechanical state via `exalted3e/scripts/ex_faction.py status`)
- <Faction> — Mag _, Goal _, Features…, Problems… (= hooks onto the Threads List)

## Clocks (offscreen factions / threats / projects / exposure ticking toward a payoff)
- none

## Overlays (optional)
- **Keyed Scenes:** _(Trigger → Event; Count)_ none
- **Thread Progress Track:** _(Focus Thread, Track 10/15/20, points, flashpoint flag)_ none
- **Peril Points:** OFF _(player-invoked only; never used by the Storyteller)_

## Adventure Crafter state (Adventure-Crafter mode)
- Active Turning Point: —   ·   Theme priority: Tension, Personal, Social, Action, Mystery

## Known canon revealed in play (only facts the PC has earned; card Truths stay hidden until triggered)
- …

## Scene
- **Last scene recap (2–3 sentences):** <the campaign opens here>
- **Adversity counter (consecutive scenes with no real cost/risk):** 0
- **Self-audit drift counter (consecutive soft scenes):** 0

## Archive pointer
- Resolved Threads / dead Characters / spent clocks → `archive.md`
