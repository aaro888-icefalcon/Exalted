# INTEGRATION — how `mythic-gm` (engine) and `exalted3e` (companion) run as one table

The `mythic-gm` skill is the **engine** (Mythic GME 2e + Adventure Crafter): content-free, shared,
the sole oracle/scene/Chaos/Random-Event/Turning-Point layer. The `exalted3e` skill is the
**companion**: the Exalted ruleset + Creation + generators, exposed to the engine through a
declarative **`bridge/`** that fills the engine's hooks. This repo wires that contract once, so you
never re-derive it mid-game. Read this file once at the start of a session; afterward `CLAUDE.md` is
enough. (Background: `mythic-gm/COMPANION-SKILLS.md` and `mythic-gm/CONVERSION.md`.)

---

## 1. Division of labor (who owns what)

| Question in play | Resolve with | Why |
|---|---|---|
| Does my attack hit? Damage? Initiative? | companion (`ex_combat.py`, `rules/02–03`) | Exalted owns combat |
| Skill / feat / task roll | companion (`ex_dice.py pool`, `rules/01`) | Exalted owns resolution |
| Social influence, Intimacies | companion (`ex_social.py`, `rules/04`) | Exalted owns social |
| Sorcery / crafting / Charms / projects | companion (`rules/05,06,08,09`) | Exalted owns subsystems |
| Stat a foe; the faction world turns | companion (`ex_npc.py`, `ex_faction.py`) | Exalted owns the world's crunch |
| Generate a ruin / court / community / cult / hook / foe | companion (`bridge/generators/`, rolled by `dice.py table`) | Exalted owns the generators |
| **Yes/no about the world** (is the gate guarded?) | engine (`dice.py fate`) | Mythic's Fate Chart is the oracle |
| **Should a scene change / interrupt?** | engine (`dice.py scene`) | Mythic owns scene tests |
| **A Random Event / a Turning Point** | engine (`oracle.py event` · `adventure_crafter.py`) | Mythic + AC own events & plot |
| **Pacing: Chaos, Threads, the seed/list machinery** | engine (`state.py`, `oracle.py list`) | Mythic owns pacing |

**Rule of thumb:** if it's an *Exalted mechanic*, the companion resolves it. If it's the *oracle, a
scene test, a Random Event, a Turning Point, or pacing*, the engine resolves it. The engine reaches
into the companion only through the `bridge/` hooks — never re-implementing Exalted; the companion
never re-implements the oracle.

## 2. The bridge (the hooks the engine reads)
`exalted3e/bridge/bridge.md` is the manifest (a `json` block) declaring which hooks the companion
overrides and where its files are. Load/verify it with:
```
python3 .claude/skills/mythic-gm/scripts/bridge.py summary  .claude/skills/exalted3e/bridge
python3 .claude/skills/mythic-gm/scripts/bridge.py validate .claude/skills/exalted3e/bridge
```
The hooks and their files:
- **resolve** → `bridge/system-profile.md` (d10 pools, Initiative combat, social, Charms; routes to `exalted3e/scripts/*` + `rules/`).
- **meaning** → `bridge/interpretation.md` (the **agenda & principles**: Creation-as-Threat primary, Creation-as-Cost secondary; how NPCs/factions think and act).
- **chaos** → `bridge/chaos-tendency.md` (start 5, Turmoil ≡ Chaos, floors, standard flavor).
- **themes** → `bridge/theme-weights.md` (fixed Adventure Crafter weights for the setting).
- **world-tick** → `bridge/subsystems.md` (faction turn, clocks, projects, exposure — fired by `tick.py`).
- **seeds** → `bridge/seeds.md` (the 30–40 seed-deck sources & refresh).
- **generate:** → `bridge/generators/registry.md` + the verified `*.json` tables (built by `exalted3e/scripts/build_bridge_generators.py`).
- **canon** → `bridge/setting-canon.md` (Creation baseline; the campaign's own `setting-canon.md` layers on top).
Any hook a bridge doesn't fill defers to the engine default — a partial bridge still plays.

## 3. The shared dial: Turmoil ≡ Chaos
One number, stored once in `campaign-state.md` as **"Turmoil ≡ Chaos Factor."** Start at 5. At scene
end: PC mostly in control → −1; scene was chaotic → +1 (clamp 1–9; floors per
`bridge/chaos-tendency.md`). Adjust with `mythic-gm/scripts/state.py chaos <+1|-1> <CF>`. Both the
engine's Fate Chart/scene tests and the companion's world key off the same value.

## 4. One state file (the merge)
Each campaign keeps **one merged** `campaign-state.md` (from `campaigns/_TEMPLATE/`) carrying both the
Mythic apparatus (Chaos, Threads/Characters Lists, Adventure Crafter state, overlays, self-audit
counter) and the Exalted tracks (Lunar quick-line, Intimacies, faction board, anima/Limit, Adversity
counter). That single file is narrative truth, overwritten every scene. Live mechanical scratch (an
in-progress fight's Initiative board, a faction season ledger) lives in `campaign_state.json` beside
it, written by the `exalted3e` scripts. A `seeds.md` (the seed deck) sits alongside.

## 5. Generators & the oracle (sharing the engine for meaning/elements)
The companion's generators and Creation oracle tables are **verified JSON** in `bridge/generators/`,
built by `exalted3e/scripts/build_bridge_generators.py` and rolled through the engine's
`dice.py table`. The routing `registry.md` says, per need, which table to use and in what **mode**:
`replace` (use the Creation table — ruins, courts, communities, cults, encounters, foes), `conjunction`
(layer Creation Meaning words on Mythic's — `meaning_action/theme/subject`), or `default` (fall
through to Mythic Elements / the AC Character Crafter). So Exalted and the engine **share** the
meaning/elements layer rather than one wholly replacing the other.

## 6. Precedence when sources disagree
`bridge/system-profile.md` + `exalted3e/rules/` > Exalted `vault/` text > training knowledge. For the
world: the campaign's `setting-canon.md` + `bridge/setting-canon.md` + `exalted3e/setting/` cards >
recollection. When **all** are silent, a Fate Question decides, and you record the answer to
`campaign-state.md` / the campaign's `setting-canon.md` so it stays consistent. Reveal a card's
**Truth** only when its in-fiction trigger fires (player ≠ PC knowledge).

---

## Combined Session Zero (do this once per campaign)
1. **Confirm hardcore play** — honest dice, real consequences, Charms cost real resources,
   defeat/Limit Break are real; agree on the genre register and any safety lines.
2. **Create the campaign folder:** `cp -r campaigns/_TEMPLATE "campaigns/<name>"`.
3. **Build the Lunar** — walk `exalted3e/lunar/01_chargen.md` (caste, spirit shape,
   attributes/abilities, merits, Charms from `charms/lunar_*`, Intimacies, Limit); pull
   shapeshifting/traits from `lunar/02–03`. Write `character-sheet.md`.
4. **Seed Creation** — start from `exalted3e/setting/00_index.md`; pick home turf; stand up the
   starting faction board (`setting/04_factions.md` → `ex_faction.py add`); note it in the campaign's
   `setting-canon.md`.
5. **Set the dials** — Turmoil ≡ Chaos = 5; empty Threads/Characters lists; pick the **Adventure
   Source mode** (Pure Mythic / Adventure Crafter / Prepared Adventure); the adventure's Theme
   priority rolls from `bridge/theme-weights.md`; populate the seed deck (`seeds.md`).
6. **First scene (untested)** — frame it, describe what the PC perceives, seed 1–2 Threads from
   backstory and the faction board, then **"What do you do?"** and STOP.
7. Write all of it into `campaign-state.md`.

## The combined Turn (every scene)
See `CLAUDE.md` → "The Turn." In short: **frame → (engine) scene test → prompt & STOP → resolve via
the owning layer → (engine) Random Event on a doubles trigger → advance plot on a due Plotline →
(companion) world-tick the faction world & clocks → bookkeep `campaign-state.md`, adjust Turmoil ≡
Chaos, refresh the seed deck, run the self-audit + Adversity gate → repeat.**

## Quick command reference (from repo root)
```
# Exalted mechanics (companion)
python3 .claude/skills/exalted3e/scripts/ex_dice.py   pool <N> [--diff D] [--stunt S]
python3 .claude/skills/exalted3e/scripts/ex_combat.py new|join|add|withering|decisive|gambit|endturn|status
python3 .claude/skills/exalted3e/scripts/ex_social.py influence <pool> --resolve R [--intimacy N]
python3 .claude/skills/exalted3e/scripts/ex_npc.py    stat <mortal|elite|hero|young-exalt|exalt|legendary>
python3 .claude/skills/exalted3e/scripts/ex_faction.py add|turn|strike|status
python3 .claude/skills/exalted3e/scripts/projects.py  cost --scope S --mag M [--opp N]
python3 .claude/skills/exalted3e/scripts/build_bridge_generators.py     # rebuild bridge/generators/*.json

# Mythic engine — oracle, scene, events, pacing, bridge
python3 .claude/skills/mythic-gm/scripts/dice.py      fate <odds> <CF> | scene <CF> | table <path-to-bridge-json> | roll <NdM>
python3 .claude/skills/mythic-gm/scripts/oracle.py    event --threads N --characters M | event-focus | pair actions | character
python3 .claude/skills/mythic-gm/scripts/adventure_crafter.py turning-point --plotlines N --characters M
python3 .claude/skills/mythic-gm/scripts/state.py     chaos <+1|-1> <CF>
python3 .claude/skills/mythic-gm/scripts/tick.py      .claude/skills/exalted3e/bridge <scene#>
python3 .claude/skills/mythic-gm/scripts/bridge.py    summary|validate .claude/skills/exalted3e/bridge
```
Odds: `certain, nearly-certain, very-likely, likely, 50/50, unlikely, very-unlikely, nearly-impossible, impossible`.
