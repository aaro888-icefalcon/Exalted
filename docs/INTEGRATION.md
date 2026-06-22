# INTEGRATION — how `exalted3e` and `mythic-gm` run as one table

Both skills are standalone, but each was built to interlock with the other:
- `exalted3e/SKILL.md`: *"If `mythic-gm` is also loaded, defer the yes/no oracle, scene tests,
  and random events to it … `Turmoil` and `Chaos` are the same 1–9 value in state."*
- `mythic-gm/SKILL.md`: *"Layers on any RPG ruleset … via the adaptation guide."*

This repo wires that seam once, so you never have to re-derive it mid-game. Read this file
once at the start of a session; afterward `CLAUDE.md` is enough.

---

## 1. Division of labor (who owns what)

| Question in play | Resolve with | Why |
|---|---|---|
| Does my attack hit? Damage? Initiative? | `exalted3e` (`ex_combat.py`, `rules/02–03`) | Exalted owns combat |
| Skill/feat/task roll | `exalted3e` (`ex_dice.py pool`, `rules/01`) | Exalted owns resolution |
| Social influence, Intimacies | `exalted3e` (`ex_social.py`, `rules/04`) | Exalted owns social |
| Sorcery / crafting / Charms / projects | `exalted3e` (`rules/05,06,08,09`) | Exalted owns subsystems |
| Stat a foe; the faction world turns | `exalted3e` (`ex_npc.py`, `ex_faction.py`) | Exalted owns the world's crunch |
| **Yes/no about the world** (is the gate guarded?) | `mythic-gm` (`dice.py fate`) | Mythic's Fate Chart is the oracle |
| **Should a new scene change/interrupt?** | `mythic-gm` (`dice.py scene`) | Mythic owns scene tests |
| **A random event / twist** | `mythic-gm` (`oracle.py event-focus`) | Mythic owns events |
| **Pacing: Chaos, Threads, Adventure Crafter** | `mythic-gm` (`state.py`, `adventure_crafter.py`) | Mythic owns pacing |

**Rule of thumb:** if it's an *Exalted mechanic*, `exalted3e` resolves it. If it's the
*oracle, a scene test, a random event, or pacing*, `mythic-gm` resolves it. Nothing else
crosses the seam. (`exalted3e` also ships its own `oracle.py` for solo use **without** Mythic —
when Mythic is loaded, prefer Mythic's richer Fate Chart and use the Exalted `oracle/` *tables*
only as Creation-native flavor.)

## 2. The shared dial: Turmoil ≡ Chaos
One number, stored once in `campaign-state.md` as **"Turmoil ≡ Chaos Factor."** Start at 5.
At scene end: PC mostly in control → −1; scene was chaotic → +1 (clamp 1–9). Adjust with
`mythic-gm/scripts/state.py chaos <+1|-1> <CF>`. Both skills read the same value — Exalted's
oracle/scene calls and Mythic's Fate Chart all key off it.

## 3. One state file (the merge)
Each skill alone wants its own `campaign-state.md`. We use **one merged file**
(`campaigns/_TEMPLATE/campaign-state.md`) that carries:
- the **Exalted** tracks — the Lunar quick-line, Intimacies, faction board, known canon,
  Adversity counter;
- the **Mythic** apparatus — Chaos, Threads List, Characters List, Adventure Features,
  Overlays, Adventure Crafter state, self-audit drift counter;
- a shared **Frame** and **Scene** block.

That single file is the narrative source of truth, overwritten every scene. Use it instead of
either skill's bundled `assets/templates/campaign-state.md`.

**Narrative vs mechanical state.** `campaign-state.md` is *narrative* truth. Live mechanical
scratch — an in-progress fight's Initiative board, the faction season ledger — lives in
`campaign_state.json` next to it, written by the `exalted3e` scripts (`ex_combat.py`,
`ex_faction.py`, `state.py show`). They don't conflict: the JSON is the calculator's tape,
the markdown is the record. After a fight/season resolves, fold the outcome into the markdown.

## 4. The ruleset bridge: `system-profile.md`
Mythic's adaptation layer (`mythic-gm/references/adapting/compatibility-spec.md`) reads a
`system-profile.md` to know how the RPG resolves tasks. We **pre-fill** it
(`campaigns/_TEMPLATE/system-profile.md`) to say: *the ruleset is the `exalted3e` skill —
route all mechanics there; Mythic supplies only oracle/scene/event/pacing.* So the Session
Zero "adapt a ruleset" step is already done.

## 5. The canon bridge: `setting-canon.md`
Mythic treats `setting-canon.md` as world ground-truth. We point it at Creation as carried by
`exalted3e/setting/` (cards with Surface vs Truth, hooks, clocks, vault cites). Consult those
cards before inventing; reveal a card's **Truth** only when its in-fiction trigger fires.

## 6. The oracle-flavor bridge
When Mythic fires a random event or a Meaning pull, flavor it with Creation-native content
from `exalted3e/oracle/01_meaning_tables.md` and `02_event_tables.md` (and the generators in
`exalted3e/generators/`) so twists read as Exalted, not generic.

## 7. Precedence when sources disagree
`campaigns/<name>/system-profile.md` + `exalted3e/rules/` > `exalted3e/vault/` text >
training knowledge. When **all** are silent, a Mythic **Fate Question** decides, and you
record the answer to `campaign-state.md` / `setting-canon.md` so it stays consistent.

---

## Combined Session Zero (do this once per campaign)
1. **Confirm hardcore play** — honest dice, real consequences, Charms cost real resources,
   defeat/Limit Break are real.
2. **Create the campaign folder:** `cp -r campaigns/_TEMPLATE "campaigns/<name>"`.
3. **Build the Lunar** — walk `exalted3e/lunar/01_chargen.md` (caste, spirit shape,
   attributes/abilities, merits, Charms from `charms/lunar_*`, Intimacies, Limit); pull
   shapeshifting/traits from `lunar/02–03`. Write `character-sheet.md`.
4. **Seed Creation** — start from `exalted3e/setting/00_index.md`; default home turf = the
   North + Lunar Dominions. Stand up the starting faction board
   (`setting/04_factions.md` → `ex_faction.py add`); note it in `setting-canon.md`.
5. **Set the dials** — Turmoil ≡ Chaos = 5; empty Threads/Characters lists; pick the
   **Adventure Source mode** (Pure Mythic / Adventure Crafter / Prepared Adventure) and the
   genre/stakes vocabulary.
6. **First scene (untested)** — frame it, describe what the PC perceives, seed 1–2 Threads
   from backstory and the faction board, then **"What do you do?"** and STOP.
7. Write all of it into `campaign-state.md`.

## The combined Turn (every scene)
See `CLAUDE.md` → "The Turn." In short: **frame → (Mythic) scene test → prompt & STOP →
resolve via the owning skill → (Mythic) random event on trigger → (Exalted) advance the
faction world on a season → bookkeep `campaign-state.md`, adjust Turmoil ≡ Chaos, run the
self-audit + Adversity gate → repeat.**

## Quick command reference (from repo root)
```
# Exalted mechanics
python3 .claude/skills/exalted3e/scripts/ex_dice.py   pool <N> [--diff D] [--stunt S]
python3 .claude/skills/exalted3e/scripts/ex_combat.py new|join|add|withering|decisive|gambit|endturn|status
python3 .claude/skills/exalted3e/scripts/ex_social.py influence <pool> --resolve R [--intimacy N]
python3 .claude/skills/exalted3e/scripts/ex_npc.py    stat <mortal|elite|hero|young-exalt|exalt|legendary>
python3 .claude/skills/exalted3e/scripts/ex_faction.py add|turn|strike|status
python3 .claude/skills/exalted3e/scripts/projects.py  cost --scope S --mag M [--opp N]
python3 .claude/skills/exalted3e/scripts/state.py     show

# Mythic oracle & pacing
python3 .claude/skills/mythic-gm/scripts/dice.py      fate <odds> <CF> | scene <CF> --mode <pure|crafter|prepared> | roll <NdM>
python3 .claude/skills/mythic-gm/scripts/oracle.py    event-focus | pair actions | meaning <t>
python3 .claude/skills/mythic-gm/scripts/adventure_crafter.py turning-point --plotlines N --characters M
python3 .claude/skills/mythic-gm/scripts/state.py     chaos <+1|-1> <CF>
```
Odds: `certain, nearly-certain, very-likely, likely, 50/50, unlikely, very-unlikely, nearly-impossible, impossible`.
