# Core resolution (Exalted 3e)

**The roll.** Dice pool = Attribute + Ability (+ specialty +1, + stunt, + Charm dice). Roll d10s via `python3 scripts/ex_dice.py pool <N> [--diff D] [--stunt S]`.
- **Success** = each die ≥ 7. **Double 10s**: each 10 = 2 successes (on by default; some Charms lower the double threshold — `--double 8`).
- **Difficulty** 0–5 (trivial→legendary). Succeed if successes ≥ difficulty; **threshold** = successes − difficulty (extra successes matter for damage, crafting, influence).
- **Botch** = zero successes AND at least one 1 (dramatic failure). The script flags it.

**Static values** (no roll; used as difficulties against the character):
- **Defense** = higher of Evasion or Parry. **Evasion** = (Dexterity + Dodge + Speed bonus)/2 round up, − mobility penalty. **Parry** = (Dexterity + [Brawl/Melee] + weapon defense)/2 round up.
- **Resolve** (vs social influence) and **Guile** (vs reading you / deception) — see `04`.
- **Soak** (subtracts from withering raw damage) = Stamina + armor. **Hardness** (blocks weak decisive attacks) = from armor/Charms.

**Willpower:** 1–10 pool. Spend 1 WP to resist influence, to power some Charms, or to take a second "miscellaneous action" exception. Regain WP from fulfilling Intimacies, a full night's rest, or stunts. **Channel an Intimacy** for +Willpower-effect on related rolls (see `04`).

**Stunts:** reward vivid description. 1-/2-/3-die stunt = +1/+2/+3 dice; a 2+-die stunt also restores 1 mote (or 1 WP if no motes). Pass `--stunt N`.

**Essence & motes:** Personal + Peripheral mote pools fuel Charms; spent motes return over time (or by stunt/rest). Anima flares as Peripheral motes are spent (see `lunar/03_traits.md`).
