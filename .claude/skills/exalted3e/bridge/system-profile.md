# System Profile — Exalted 3rd Edition (Lunar solo)   (hook: resolve)

The ruleset is the **`exalted3e` skill**. This profile tells the `mythic-gm` engine how Exalted
resolves things and where to route each call. The engine owns only the oracle, scene tests, Random
Events, Turning Points, and Chaos/pacing; **everything mechanical resolves here, through
`exalted3e/scripts/` and `exalted3e/rules/`.** Don't re-derive Exalted's rules in this file — route.

- **Dice convention:** d10 dice pool. Roll a number of d10s = Attribute + Ability (+ bonuses); each
  die ≥ **7** is a success (10s = one success; some effects double 10s).
  **Express every roll through** `python3 .claude/skills/exalted3e/scripts/ex_dice.py pool <N> [--diff D] [--stunt S] [--double X]`.
  Generic / table dice: `ex_dice.py roll <NdM[+/-K]>`.
- **Core resolution:** count successes vs a **difficulty**; meet/exceed = success; extra = threshold
  successes. Botch = 0 successes with a 1 showing. → `rules/01_core_resolution.md`.
- **Degrees of success?** Yes (threshold successes + botches). A Mythic *rule-mode* Fate Question's
  Exceptional Yes/No therefore has a home — but in practice Exalted resolves these directly; fall back
  to a rule-mode Fate Question (`dice.py fate <odds> <CF> --mode rule`) only when **no** Exalted rule
  applies.
- **Stats / skills:** 9 Attributes (Str/Dex/Sta · Cha/Man/App · Per/Int/Wits) + Abilities (dots).
  Tracked resources: Essence, motes (Personal/Peripheral), Willpower, Limit (/10), anima, Initiative, Health.
- **Defenses / health:** Evasion, Parry, Resolve, Guile, Soak, Hardness; Health track
  -0/-1/-1/-2/-2/-4/Incap. Static values per `rules/01`.
- **Combat:** the **Initiative system** (Join Battle → withering attacks build Initiative → decisive
  attacks spend it → Initiative Crash). Owned by `ex_combat.py`
  (`new|join|add|withering|decisive|gambit|endturn|status`) and `rules/02`–`03`. **Defeat is real:**
  death, capture, crippling, Limit Break, a lost Heart's-Blood form.
- **Social influence:** Intimacies, Resolve/Guile, instill/persuade/read-intentions →
  `ex_social.py influence …` and `rules/04`.
- **Charms / Essence:** Charms cost real motes/Willpower. Adjudicate via `rules/08_charms_engine.md`;
  pull text from `charms/` (PC, by Attribute) or `charms/antagonist_pools/` (foes).
- **NPC stat units (for the engine's on-the-fly NPC Statistics):** Exalted statblocks by **tier** —
  `ex_npc.py stat <mortal|elite|hero|young-exalt|exalt|legendary>`; ready foes in `statblocks/`.
  (When the engine reads `npc_statistics`: Yes = the tier value; ExcYes ≈ +25%; No ≈ −25%; ExcNo ≈ −50%.)
- **Subsystems:** Sorcery & workings → `rules/05`; Crafting & projects → `rules/06`, `rules/09`
  (`scripts/projects.py`); Advancement / XP → `rules/07`.

## Routing default
- **Exalted resolves:** every task roll, all combat, social influence, sorcery, crafting, Charms, NPC
  stats, the faction world, and the generators — always via `exalted3e/scripts/` + `rules/`.
- **The engine resolves:** yes/no world questions (Fate Questions), scene tests, Random Events,
  Turning Points, and the Chaos Factor / pacing (Threads, Characters, Adventure Crafter).
- **Precedence when sources disagree:** this profile + `exalted3e/rules/` > Exalted `vault/` text >
  training knowledge. When all are silent, a Fate Question decides and the answer is written to
  `campaign-state.md` / `setting-canon.md` so it stays consistent.

## House rules / notes
- _(record any table rulings here as they come up, so play stays consistent)_
