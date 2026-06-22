# Foes — Antagonist Flavor Menus + Tactics Tables

Quick prompt tables that **pair with `scripts/ex_npc.py`.** The script assembles the numbers (Essence + mote pool, Join Battle + Evasion/Parry/soak/Hardness, Health levels, attack/Initiative profile, Resolve/Guile). These menus answer *"what makes this foe interesting?"* — the signature Charms and the per-foe **Tactics table** so you never forget a power mid-fight. Roll with `scripts/ex_dice.py roll NdM`. Read every effect as a **Feature** (what it does to the PC) with an implied **Problem** (its tell / its counter).

Cost grammar matches Exalted stat blocks: `Xm` motes, `Yi` Initiative, `1wp` Willpower, `Reflexive/Supplemental/Simple`, decisive/withering, gambit difficulty.

## Attack-Pattern Menu (`roll 1d10`)
Pick the foe's signature offense.
| d10 | Pattern | Effect sketch |
|---|---|---|
| 1 | Onslaught flurry | multiple withering attacks to strip the PC's Initiative fast |
| 2 | Crippling decisive | one big decisive aimed to land a wound penalty / Crippling effect |
| 3 | Opening ambush | surprise decisive from concealment before Join Battle settles |
| 4 | Gambit specialist | leans on gambits — disarm, knockdown, grapple (set difficulty) |
| 5 | Reach / zone control | denies approach; punishes movement into its range |
| 6 | Poison / lingering | low up-front damage, a debuff that ticks each turn (`Xm`, Essence-fueled) |
| 7 | Battle-group / swarm | attacks as a unit; Magnitude soaks losses; drowns in numbers |
| 8 | Essence blast | ranged Charm attack ignoring some soak/Hardness (`Xm`) |
| 9 | Counter-puncher | weak offense, devastating on the riposte (see Defensive 2) |
| 10 | Escalator | grows stronger as the fight drags / as it takes damage |

## Defensive-Ability Menu (`roll 1d10`)
| d10 | Defense | Effect sketch |
|---|---|---|
| 1 | Perfect dodge/parry (1/round) | spends motes to no-sell one attack outright |
| 2 | Counterattack on miss/parry | a reflexive withering/decisive when the PC fails to land |
| 3 | High Hardness | shrugs decisive damage below a threshold (armor/Charm) |
| 4 | Damage cap / immunity | a damage type (fire, cold, poison, lethal) is halved or ignored |
| 5 | Regeneration | heals health levels each turn unless a condition is met |
| 6 | Soak-stacking ward | reflexive soak boost when struck (`Xm`) |
| 7 | Hostage / meatshield | redirects harm onto a captive or minion |
| 8 | Discorporation | becomes immaterial / mist to escape harm (spirit, raksha) |
| 9 | Reset on crash | when Initiative-crashed, reflexively repositions and resets |
| 10 | Untouchable while X | invulnerable until a vulnerability is exposed (a seal, a name, daylight) |

## Mobility Menu (`roll 1d8`)
1 flight · 2 burrowing (strikes from below) · 3 teleport/blink (Essence) · 4 wall-/ceiling-crawl · 5 aquatic (drags foes under) · 6 supernatural Speed Bonus (always acts first to reposition) · 7 phasing through matter (immaterial passage) · 8 mounted / on a warbeast.

## Impairing-Power Menu (`roll 1d10`)
The "save-or-suck" the foe can hang a fight on.
| d10 | Power | Effect sketch |
|---|---|---|
| 1 | Fear aura | onslaught to Resolve; failed = Initiative loss / can't approach |
| 2 | Paralysis / stasis | a gambit or Charm that roots the PC in place |
| 3 | Mind-control gambit | a social attack mid-combat: turn an ally, force a step back |
| 4 | Mutation / curse touch | lasting penalty until cleansed (cross-ref `challenges.md` undo-magic) |
| 5 | Mote-drain / anima-douse | strips the PC's motes or suppresses Charms |
| 6 | Blinding / sense-deny | fog, darkness, illusion: attack penalties |
| 7 | Confusion / Wyld-warp | the battlefield itself shifts (raksha, Wyld zone) |
| 8 | Disarm / sunder | removes the PC's weapon or breaks gear |
| 9 | Sticky / grapple-lock | holds the PC fast, dragging Initiative down each turn |
| 10 | Despair / Intimacy-strike | a social nuke that erodes a motivating Intimacy |

## Per-Foe Tactics Table (the ≈6-line block)
Write one for every named foe so the script's numbers come alive. Fill these six lines (pull from the menus above):
1. **Opener** — first action turn 1 (ambush decisive? Join Battle then flurry? buff up?).
2. **Standard turn** — its bread-and-butter attack pattern while healthy.
3. **Signature power** — when/why it fires its impairing power or best Charm (and the cost).
4. **When crashed (Initiative 0 or fewer)** — does it flee, reset, go defensive, or escalate?
5. **When hurt (e.g., at –2 health levels)** — break point: flee, surrender, call reinforcements, or berserk?
6. **Never forgets** — the one thing the GM must not overlook (a reflexive counter, a hostage, a regen condition, a perfect defense it always saves for the killing blow).

### Worked example — *Tomb-Automaton, Rusted Sentinel* (assemble stats via `scripts/ex_npc.py`)
1. **Opener:** holds the doorway (Reach/zone control); does not pursue — guards the vault.
2. **Standard turn:** heavy withering swings to crash intruders, then a decisive to a downed foe.
3. **Signature:** `6m` reflexive soak-ward when first struck (Defensive 6); fights at high Hardness.
4. **When crashed:** never flees — resets stance in the doorway, keeps blocking the only ingress.
5. **When hurt (–2):** no morale; fights to Incapacitation. The *Problem*: it stops if given the First Age command-phrase (a hook the PC can find in the ruin).
6. **Never forgets:** it ignores anyone bearing the builder's sigil — a non-combat solution exists.
