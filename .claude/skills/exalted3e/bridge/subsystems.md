# World Subsystems — Creation   (hook: world-tick; fired by `tick.py <bridge> <scene#>` at bookkeeping)

The living world keeps turning whether or not the Lunar acts. At each scene's bookkeeping,
`tick.py` reports which of these are due; the engine then rolls their named tables honestly and
records the result to `campaign-state.md`. (Roll a table with
`python3 .claude/skills/mythic-gm/scripts/dice.py table <abs path to the json>`.)

| subsystem | cadence | advance by |
|-----------|---------|-----------|
| Offscreen clocks | every scene | tick each armed clock toward its payoff; surface only what the PC perceives. At full → the threat lands (the Wyld Hunt arrives, the famine breaks, the rite completes). |
| Faction world turn | every 5 scenes | `python3 .claude/skills/exalted3e/scripts/ex_faction.py turn` — each faction acts (roll `generators/faction_move.json`) and Moves Toward/Away a Thread; a faction's `Problem:` is a live hook (Threads List). |
| Exposure / scrutiny clocks | on trigger: a flagrant act or a slipped tell | +1 when the Lunar uses a tell-breaking miracle, slips, or is studied; at full → the secret breaks / the Hunt is called. (Reward earned caution: no tick when the PC plays it clean.) |
| Projects & dominion | on trigger: a build/social-project interval elapses | advance the Project per `rules/09_projects_and_dominion.md` (`scripts/projects.py`); a finished Project edits the faction board (a new Feature, a cleared Problem). |
| Intimacy & Limit pressure | on trigger: an Intimacy is pressed or a Limit trigger fires | roll/track Limit per `lunar/03_traits.md`; at 10 → the Great Curse erupts. |

Default (anything not listed): the engine advances offscreen clocks only.
