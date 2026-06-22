# System Profile — Exalted 3rd Edition (Lunar solo)

> This is the pre-built bridge that satisfies `mythic-gm`'s adaptation layer
> (`references/adapting/compatibility-spec.md`). It tells the Mythic engine that the
> **entire ruleset is owned by the `exalted3e` skill** — Mythic supplies only the oracle,
> scene tests, random events, and Chaos/pacing. You do **not** need to re-derive Exalted's
> rules here; just route to the skill. Full rules live in `exalted3e/rules/`.

- **Dice convention:** d10 dice pool. Roll a number of d10s = Attribute + Ability (+bonuses);
  each die ≥ **7** is a success (10s normally count as one success; some effects double 10s).
  **Express every roll through** `exalted3e/scripts/ex_dice.py pool <N> [--diff D] [--stunt S] [--double X]`.
  Generic table dice: `ex_dice.py roll <NdM[+/-K]>`.
- **Core resolution:** count successes vs a **difficulty**; meet/exceed = success, extra successes
  = threshold successes. Botch = 0 successes with a 1 showing. Detail: `exalted3e/rules/01_core_resolution.md`.
- **Degrees of success?** Yes (threshold successes + botches). So a Mythic *rule-mode* Fate Question's
  Exceptional Yes/No has a home — but in practice Exalted resolves these directly; only fall back to a
  rule-mode Fate Question when no Exalted rule applies.
- **Stats / skills:** 9 Attributes (Str/Dex/Sta · Cha/Man/App · Per/Int/Wits) + Abilities (dots).
  Tracked resources: Essence, motes (Personal/Peripheral), Willpower, Limit (/10), anima, Initiative, Health.
- **Defenses / health:** Evasion, Parry, Resolve, Guile, Soak, Hardness; Health track
  -0/-1/-1/-2/-2/-4/Incap. Static values per `rules/01`.
- **Combat:** the **Initiative system** (Join Battle → withering attacks build Initiative → decisive
  attacks spend it → Initiative Crash). Owned by `exalted3e/scripts/ex_combat.py`
  (`new|join|add|withering|decisive|gambit|endturn|status`) and `rules/02`–`03`. **Defeat is real:**
  death, capture, crippling, Limit Break, a lost Heart's-Blood form.
- **Social influence:** Intimacies, Resolve/Guile, instill/persuade/read-intentions →
  `exalted3e/scripts/ex_social.py influence …` and `rules/04`.
- **NPC stat units:** Exalted statblocks by tier — `exalted3e/scripts/ex_npc.py stat <mortal|elite|hero|young-exalt|exalt|legendary>`; ready foes in `exalted3e/statblocks/`.
- **Charms / Essence:** Charms cost real motes/Willpower. Adjudicate via `rules/08_charms_engine.md`;
  pull text from `exalted3e/charms/` (PC) or `charms/antagonist_pools/` (foes).
- **Subsystems:** Sorcery & workings → `rules/05`; Crafting & projects → `rules/06`, `rules/09`
  (`scripts/projects.py`); Advancement/XP → `rules/07`.

## Routing default (THE SEAM)
- **`exalted3e` resolves:** every task roll, all combat, social influence, sorcery, crafting,
  Charms, NPC stats, the faction world, and the generators. Always via `exalted3e/scripts/`.
- **`mythic-gm` resolves ONLY:** yes/no world questions (Fate Questions), scene tests, random
  events, and the Chaos Factor / pacing (Threads, Characters, Adventure Crafter).
- **Precedence when sources disagree:** this profile + `exalted3e/rules/` > Exalted `vault/` text >
  training knowledge. When all are silent, a Mythic **Fate Question** decides and the result is
  written to canon/state.

## House rules / notes
- _(record any table rulings here as they come up, so play stays consistent)_
