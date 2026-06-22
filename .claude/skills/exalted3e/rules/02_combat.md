# Tactical combat — the Initiative war (Exalted 3e)

The showpiece. Combat is a duel of **Initiative**: withering attacks steal it, decisive attacks spend it as damage. Run the whole fight through `scripts/ex_combat.py` (it tracks the board and shows every die).

## Sequence
1. **Join Battle:** `ex_combat.py join <name> --wa <Wits+Awareness> [--pc] --evasion E --parry P --soak S --hardness H --hl N --str-wdmg B`. Initiative = successes + 3. (NPCs from a statblock: `add <name> --init 3 …`.)
2. **Turn order** by Initiative, high to low. One **combat action** per round (attack, etc.) + movement + reflexives. A **flurry** does two actions at −3 dice each and lowers Defense.
3. After each combatant acts: `ex_combat.py endturn <name>` (clears their **onslaught** penalty; handles the 3-turn Crash reset).

## Withering (build Initiative) — `withering <atk> <def> --acc <pool> --base <Str+wpnDmg> [--ovw <min>]`
Accuracy pool vs the defender's **Defense** (reduced by accumulated onslaught). On hit: raw = base + threshold; minus soak (min = Overwhelming) = damage dice (double 10s); attacker **+1 Initiative for the hit** plus the damage successes, defender loses that much. Each attack adds **−1 onslaught** to the target's Defense until its next turn.

## Decisive (spend Initiative as damage) — `decisive <atk> <def> --acc <pool>`
Accuracy (no weapon bonus) vs Defense. On hit: damage dice = **attacker's current Initiative** (NO double 10s); if ≤ target **Hardness**, no damage; successes = Health Track damage. **Initiative resets to base 3** after any connecting decisive. **Miss** = lose 2 Initiative (if at 1–10) or 3 (if 11+). So strike when your Initiative is high and the foe is low/Crashed.

## Crash, Break, Reset, Shift
- **Crash:** Initiative ≤ 0 — can't make decisive attacks, Hardness 0, vulnerable. Crashing a foe grants the attacker **+5 Initiative Break** (auto-applied by the script).
- **Reset:** survive 3 turns Crashed → Initiative resets to 3.
- **Shift:** a Crashed character who Crashes their crasher resets to base + a fresh Join Battle and refreshes their turn (narrate; adjust with `add`/manual).

## Other actions
Full Defense (+2 Defense, −1 Initiative); Aim (+3 next attack); Disengage (−2 Init, opposed); Withdraw (−10 Init/round, leave the field); Rise from Prone; Ready Weapon. **Range bands:** close/short/medium/long; melee at close; move one band/round. **Cover/surprise:** unaware target loses Defense; ambush opens with a free decisive.

## Gambits — `gambit <atk> <def> --acc <pool> --diff <D>`
A decisive-style maneuver (disarm, knockdown, grapple, etc.): to-hit vs Defense, then Initiative roll vs the gambit difficulty; lose (difficulty + 1) Initiative regardless. Use for anything the basic rules don't cover.

**NPCs act to win:** spend their motes and Charms (from `charms/antagonist_pools/`), build Initiative, focus the wounded, exploit onslaught, flee/parley when outmatched. See `generators/foes.md` for per-foe Tactics tables.
