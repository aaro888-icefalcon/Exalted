# Campaign State — The Tide Beneath the Dragon

> The single source of truth. Both skills read this every turn and overwrite it at scene end.
> Narrative truth here; live mechanical scratch (fights/seasons) in `campaign_state.json`.

## Frame
- **System:** Exalted 3rd Edition — owned by the `exalted3e` skill → `system-profile.md`
- **Oracle / pacing engine:** `mythic-gm` (Fate Chart, scene tests, random events, Chaos)
- **Adventure Source mode:** **Adventure Crafter** (Turning Points + themes braid the Threads)
- **Setting / canon:** Creation (Age of Sorrows) → `setting-canon.md`. **Home turf: Prasad** (SW, Dreaming Sea).
- **Genre & stakes:** mythic-tragic intrigue under a theocratic-military state — maximal honest consequence is
  **exposure, ruin, the Wyld Hunt**. `adversity-calibration.md`.
- **Resolution:** Fate Chart · **Chaos flavor:** normal · **Discipline:** HARDCORE (Peril Points OFF)

## Turmoil ≡ Chaos Factor: 5
_(One shared 1–9 value. −1 if the PC was mostly in control of the last scene; +1 if chaotic.
Adjust via `mythic-gm/scripts/state.py chaos <+1|-1> <CF>`.)_

## The Lunar (PC)
See `character-sheet.md`. Quick line: **Ophris ("Shake")**, No Moon, Essence 1 · motes 16/16 P, 38/38 Periph
· WP 5/5 · Limit 0/10 · anima Dim · Join Battle 7 · Defense 5 (Parry 5/Evasion 3) · Resolve 3 · Guile 2 ·
Soak 4 · Health 10 levels (-0/-1×2/-2×4/-4×2/Incap), all undamaged. Mask: Wood Aspect of House Ophris.
Spirit shape: Sky-Titan⊗Otter (Legendary; titan transform via Towering Beast Form). Tell: leaves in his hair.

## Intimacies
- **Defining (Tie +):** My family — Akhil (brother), Bhaskar & Sudha (parents).
- **Major (Principle):** "The job is the job." · "I look out for my crew." · "I will make something of myself."
  · "No one can determine my secret." · "It's best to be honest." ⚡(opposed by his life → lies feed Limit)
- **Major (Tie +):** House Ophris · Tanisa Ring-Eater (teacher/sister/mate/pawn?)
- **Minor:** (Principle) "I like the Pure Way — my tradition." ⚡ · (Tie +) my friends (dynast circle)
- **Major (Tie −):** Burano Ravan (House Burano rival) · Mahru, the Drowned God (slew his soldiers)
- **Limit trigger:** his counsel/help is refused or ignored → roll 3 Limit dice.

## Threads List (open goals & hooks; weighted)
1. **Keep the moon hidden** — sustain the Wood-Aspect lie under the Pure Way's scrutiny. *(3)*
2. **Tanisa's design** — steer Prasad against the Realm/Lookshy as her agent, while Leopard schemes to burn it. *(2)*
3. **Family & House Ophris** — protect the kin who share the secret's risk. *(2)*
4. **The Burano rivalry** — outshine Burano Ravan / "make something of myself." Ravan just drew first blood in court. *(2)*
5. **Mahru's reckoning** — the drowned god who took your soldiers; now a Pure Way-marked "rebel god." *(2)*
6. **The sanctified expedition** — ACCEPTED. Ophris will lead a rite-bound expedition to subjugate/destroy Mahru,
   under **Akatha** Prelate Anuhya's direct oversight; marches once the rites are prepared. His chance to "make
   something of myself" — chained to an Akatha god-hunter's lamp held to the secret, with his fake element expected
   to manifest on the water. *(3, active)*

## Characters List (NPCs & forces in play; the PC is NOT listed)
1. **Akhil** — younger brother; knows the secret; closest tie. Present in the Vashri court as Ophris's aide. *(3)*
2. **Bhaskar & Sudha** — parents, heads of House Ophris; hid him. *(2)*
3. **Tanisa Ring-Eater** — shahan-ya, master schemer; runs Ophris as an asset (Mount Namas). *(2)*
4. **Burano Ravan** — rival of House Burano. Exposed Ophris's false blame-shift in open court. *(2)*
5. **Prelate Anuhya** — **Clan Akatha** (Exceptional-Yes), and senior: a god-clan prelate-monk schooled in the martial
   rites that bring rebel gods to heel. White-robed, austere, serene. Now bound to Ophris as overseer of the sanctified
   expedition; will "spend the road together" teaching him the rites — and expects his Wood element to "show plainly"
   on the marches. **THE DANGER — the worst possible chaperone for a hidden Lunar.** *(3)*
6. **Prefect Sesrina of the Cinquefoil Banner** — Prince of the Earth (DB, Ess 3), frontier prefect at Vashri Crossing.
   Icy, by-the-book Air-aspect. Holds Major Principle *"discipline & doctrine win the frontier."* **Resolve 4**, Guile ~3;
   combat (if ever): Evasion/Parry 6, soak 10, Hardness 6, HL 8, Join Battle 6. Accepted Ophris's doctrine frame (barely). *(2)*
7. **Mahru, the Drowned God of the border marches** — wronged frontier god, vengeful; now named in court as a "rebel god"
   marked for subjugation. *(2)*
8. **Seven Obsidian Leopard** — Tanisa's necromancer-partner; wants Prasad destroyed. *(1, offstage)*

## Adventure Features List (Prepared-Adventure mode only) — n/a

## Faction board (live state via `ex_faction.py status`; EX_STATE → this folder's json)
- **Prasad / the Pure Way** (Mag 4) — expand & purge Anathema/heresy; Problem: border wars on many fronts.
- **House Ophris** (Mag 2) — rise among Prasad's houses; Problem: a hidden Anathema in its own blood.
- **House Burano** (Mag 2) — outshine House Ophris; Problem: rivalry with House Ophris.
- **Clan Akatha** (Mag ~3, not yet in json) — God-Blooded priest-clan; keeps the spirit courts, weds & murders gods;
   Pure Way's hand on divine affairs. Now personally engaged via Prelate Anuhya. *(add to json on next faction turn.)*
- **The Silver Pact** (Mag 3) — tear down DB tyranny, shelter Lunars; Tanisa's hand reaches into Prasad.
- **The Guild** (Mag 3) — profit from the Dreaming Sea trade.
- **Ysyr** (Mag 3) — extend the sorcerer-princes against Prasad.

## Clocks (offscreen, ticking)
- **Prasad's Advance [3/6]** — the empire pushes its frontier & Pure Way outward (canon).
- **Pure Way scrutiny of House Ophris's "new Wood Aspect" [1/?]** — TICKED: Ophris invited Prelate Anuhya's
  counsel in open court; she answered by fixing her attention on him personally and proposing to keep him "under her eye."

## Overlays (Mythic; optional)
- **Keyed Scenes:** none · **Thread Progress Track:** none · **Peril Points:** OFF (player-invoked only).

## Adventure Crafter state
- Active Turning Point: — (first scene untested) · Theme priority: Action, Tension, Mystery, Social, Personal.

## Known canon revealed in play (only what the PC has earned)
- Ophris is a No Moon Lunar hiding as a Wood Aspect of House Ophris; his parents & Akhil know.
- Prasad is a fanatically-Immaculate ("Pure Way") expansionist Dragon-Blooded empire on the Dreaming Sea that burns
  Anathema; Houses Ophris and Burano are among its conqueror-houses. *(Public Prasadi knowledge.)*
- His shahan-ya **Tanisa Ring-Eater** placed him inside Prasad to steer it against the Realm. *(Her deeper aims & the
  Leopard schism: only partly earned — treat as potential until confirmed in play.)*
- **Earned in Scene 1:** the failed reconnaissance of the Silt Marches was House Ophris's OWN charge, not Burano's —
  Ophris's blame-shift was false and Ravan proved it publicly. The Pure Way (via Prelate Anuhya) has formally named
  **Mahru a "rebel god"** to be subjugated by sanctified expedition. Anuhya's attention is now personally on Ophris.
- **Prasad has three Dragon-Blooded clans** — Ophris, Burano, and **Akatha** (the God-Blooded priest-clan that manages
  and punishes gods). **Prelate Anuhya is a senior Akatha** god-hunter; Ophris will lead Mahru's subjugation under her.

## Scene
- **SCENE 1 — "Two Houses, One Frontier"** · Vashri Crossing war-court · Turmoil/Chaos 5 · ONGOING (untested first scene).
- **Last beat / recap:** A contentious joint court over the costly Silt Marches skirmish (11 Ophris dead to the god Mahru,
  after the legion fired his shrine). Burano Ravan opened by mocking Ophris's competence and brushing at "the Dragons'
  favor." Ophris answered with a factual account — true on the doctrine (a major god on its own demesne is a known
  hazard) but he wrongly pinned the recon failure on Burano. **Rolls:** his instill landed on Prefect Sesrina by a hair
  (4 vs Resolve 4) → she concedes the doctrine point. But ground-truth (rolled): the recon was Ophris's OWN charge, and
  **Ravan exposed the false blame** in open court. Ophris deferred to **Prelate Anuhya** for "the best approach" — she
  declined to shelter him (Fate: NO) and instead declared Mahru a *rebel god* to be subjugated by sanctified expedition,
  **led by Ophris under her personal oversight** ("unless you have some reason you should not"), her gaze on his leaves.
- **Exchange 2:** Ophris paid pious homage and ACCEPTED the charge (smart, low-suspicion; defused the needle, locked the
  expedition). Fate Q resolved Anuhya as **Clan Akatha — Exceptional Yes**: a senior god-clan prelate-monk, a god-hunter.
  She's now his expedition overseer ("we'll spend the road together") and pointedly expects his Wood element to "show
  plainly." Court is breaking; Ravan denied his kill but the false-blame stain holds; Akhil at his side.
- **Open decision (cliff):** the court disperses around Ophris — a last move before the scene closes (Akhil? Ravan?
  Anuhya? withdraw to prepare?).
- **Adversity counter:** 1 (pressed: standing bruised, scrutiny clock ticked, now leashed to an Akatha god-hunter) · **Self-audit drift:** 0
- **NOTE:** Turmoil/Chaos tick deferred to scene END. Leaning **+1 → 6** (scene moved against his core interest: he's
  bound to the most dangerous overseer possible). Confirm at close.

## Archive pointer
- Resolved Threads / dead Characters / spent clocks → `archive.md`
