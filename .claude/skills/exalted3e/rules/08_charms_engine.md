# Charms Engine — How to Read & Adjudicate ANY Charm

This file lets you run a Charm pulled from the catalog/vault even if you've never seen it. Read the stat line, apply the keywords, resolve by type. *(Core Rulebook › Chapter Six: Charms; Presentation Format)*

---

## The Stat Line *(Core Rulebook › Presentation Format)*

**Cost** — must pay in full to activate. Shorthand *(Core Rulebook › Charm Costs)*:

| Code | Means | Code | Means |
|---|---|---|---|
| `#m` | motes | `#a` | anima levels |
| `#wp` | Willpower | `#i` | Initiative |
| `#hl`/`#lhl`/`#ahl` | bashing / lethal / aggravated health levels | `#xp`/`#sxp`/`#gxp`/`#wxp` | experience (general / silver / gold / white craft) |

- Can't spend **Initiative below 0**; in **Initiative Crash** you can't pay any `#i` cost (unless the Charm says so).
- `1m per die` (Excellencies) = pay per die added.

**Mins** — `Ability X, Essence Y`: must have both to **learn** it (e.g. "Melee 3, Essence 3").

**Type** — when/how it fires (see next section).

**Keywords** — special rules (glossary below).

**Duration** — how long it lasts (see Duration section).

**Prerequisite Charms** — must already know all listed. For "any N Charms," **Excellencies never count**, and a named prereq's own prereqs don't count toward the "any N."

---

## Type — the timing rule *(Core Rulebook › Presentation Format — Type)*

- **Simple** — *is* a combat action; only on your turn; **not** flurryable → **one Simple Charm per round**. Usually creates an action with its governing Ability.
- **Supplemental** — enhances one action (attack/craft/social roll) using that Ability. Use as many per round as you have valid actions, **but never the same Charm twice on one action**.
- **Reflexive** — creates a reflexive action or boosts a non-dice thing (a Parry, holding breath). Usable anytime it makes sense; **can't stack the same enhancing Charm**. Reflexive defensive Charms only boost static values from their own Ability.
- **Permanent** — always-on, usually free (e.g. Ox-Body Technique adds health levels).

---

## Keyword Glossary *(Core Rulebook › Presentation Format — Keywords)*

| Keyword | Effect |
|---|---|
| **Uniform** | Same function for **both** withering & decisive attacks/defenses. |
| **Dual** | Two functions — one withering, one decisive. |
| **Withering-only** | Works only with/against a **withering** attack. |
| **Decisive-only** | Works only with/against a **decisive** attack. |
| **Perilous** | **Cannot be used in Initiative Crash.** (Crash = Initiative ≤ 0.) |
| **Aggravated** | Damage it deals **can't be healed or hastened by magic**. |
| **Mute** | Its cost **won't raise the anima** unless the user wants it to. |
| **Psyche** | Unnatural mental influence/control — the magic that can override "unacceptable influence." |
| **Salient** | Cost wants silver/gold/white craft XP for major/superior/legendary projects. |
| **Stackable** | Its effects **do** stack (the exception to the no-stack rule). |
| **Written-only** | Only enhances/creates **written** social influence. |
| **Clash** | Can't be used with/against a **Counterattack** Charm. |
| **Counterattack** | Can't be used in reaction to a **Counterattack** or **Clash** Charm. |
| **Bridge** | Buyable via alternate prereqs from another Ability (see Core for discount math). |
| **Pilot** | User must be captain/helmsman of the vessel. |

---

## Duration *(Core Rulebook › Presentation Format — Duration)*

- **Instant** — acts then ends (effects can still persist: a dead foe stays dead).
- **one tick / one turn / one round** — until that tick / your next turn / end of this round.
- **Scene / Indefinite** — lasts the scene, or until released / a stated trigger.
- **Commitment:** any non-Permanent Charm lasting **longer than Instant requires its motes be committed** (tied up until released). A Solar may reflexively end one of his own Charms early (unless its text forbids).
- *(Sorcerous motes are never committed — see `05_sorcery_and_workings.md`.)*

---

## Excellencies — the universal dial *(Core Rulebook › Excellencies)*

Solars auto-get an Excellency for each Caste/Favored Ability with ≥1 dot, and each Ability with ≥1 Charm (free; no slot).

- **Add dice to a roll:** **1 mote per die**, up to **(Attribute + Ability)** dice. Supplemental, Instant.
- **Raise a static value** (Defense, Resolve, etc.): **2 motes per +1**, up to **half (Attribute + Ability that builds it)**. Reflexive, Instant.

---

## Charm Limitations & Stacking *(Core Rulebook › Using Charms and Charm Limitations)*

- **Declare all Charms and pay costs BEFORE any dice are rolled. Attacker declares before defender.**
- **Dice cap (the absolute rule):** magic can add at most **(Attribute + Ability)** dice to a roll. A **success** added by a Charm counts as **2 dice**. Specialties don't count toward this cap. Applies to all magic stacked on the roll (Solar, MA, sorcery, Evocations, allies' Charms).
- **Static value cap:** magic can raise a static value by at most **half (Attribute + Ability)** (round down). Each +1 = 2 dice for the cap.
- These caps are absolute unless a Charm **explicitly** says otherwise.
- **No "combos" needed:** Exalts may use any number of Charms per round, subject to type rules and cost — there is no separate combo system or combo cost in 3e.

**Order of operations** *(Core Rulebook › Order of Operations)*: reroll/remove-number Charms resolve **first**; a Charm that *preys on* a number (e.g. 1s) sees the result only **after** all rerolls. Any Charm acting on another action's result waits until all that action's modifiers are in place.

---

## Anima Effects *(Core Rulebook › The Anima Banner)*

Spending **5+ Peripheral motes in one instant** raises the anima **one level per 5 Peripheral motes**. **Personal** motes and smaller spends don't stir it. **Mute** Charms don't add to it.

| Level | Effect (Solar) |
|---|---|
| **Dim** | Invisible; hides Exalted nature. Default when not spending. |
| **Glowing** | Caste mark shows; **−3 to stealth/disguise**. |
| **Burning** | Mark subsumed in radiance; **stealth impossible**. |
| **Bonfire/Iconic** | Iconic display; lights area to short range; visible for miles. |

Some Charms require a specific anima level; some can mute/diminish/extinguish the display.

---

## Adjudicating an UNFAMILIAR Charm — checklist

1. **Can they pay?** Full cost, incl. `#i` not below 0, no Perilous/`#i` in Crash. Pay & declare *before* dice.
2. **Type** → may they act now? (Simple = their turn, one/round; Supplemental needs a valid action; Reflexive anytime sensible; Permanent already on.)
3. **Keywords** → withering/decisive gate, Aggravated, Psyche, Clash/Counterattack, anima from non-Mute spend.
4. **Apply the effect**, then enforce the **dice cap (Att+Abi)** / **static cap (half Att+Abi)**; success-adds count double.
5. **Duration** → commit motes if longer than Instant; note when it ends.
6. **Stacking?** Same Charm never twice on one action; same enhancing Reflexive/Supplemental doesn't stack (unless **Stackable**).
7. **Anima:** add levels if ≥5 Peripheral motes spent at once.
8. **Solar-feel sanity check** *(Core Rulebook › Designing Charms — Theme/Limits)*: no teleport, no time travel, no resurrection, no non-human transformation via Solar Charms. If a vault Charm seems to break a cap or limit, the **Charm's explicit text wins** over the general rule; otherwise enforce the cap.

> **Worked example.** Vault Charm: *Cost 3m; Type Supplemental; Keywords Decisive-only; Mins Melee 4, Essence 2; Duration Instant.* Adjudicate: pay 3m & declare before the attack roll → legal only on a **decisive** attack → it enhances one Melee action → any dice it grants still cap at (Dex + Melee). 3 Peripheral motes < 5, so **no anima rise**. Instant → nothing to commit.
