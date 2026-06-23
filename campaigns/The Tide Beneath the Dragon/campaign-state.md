# Campaign State — The Tide Beneath the Dragon

> The single source of truth. Overwrite it at scene end. Narrative truth here; live mechanical
> scratch (fights/seasons) in `campaign_state.json`.
> **Architecture:** the `mythic-gm` engine is the oracle/scene/Chaos/pacing layer; the `exalted3e`
> companion (its `bridge/`) supplies the ruleset, Creation, and the generators.

## Frame
- **Adventure Source mode:** **Adventure Crafter** (Turning Points + themes braid the Threads)
- **System / resolution:** Exalted 3rd Edition → `exalted3e/bridge/system-profile.md`
- **Setting / canon:** Creation (Age of Sorrows) → `exalted3e/bridge/setting-canon.md` + this folder's `setting-canon.md`. **Home turf: Prasad** (SW, Dreaming Sea).
- **GM lens / agenda:** `exalted3e/bridge/interpretation.md` — Creation-as-Threat (primary) / Creation-as-Cost (secondary)
- **Genre & stakes:** mythic-tragic intrigue under a theocratic-military state — maximal honest consequence is
  **exposure, ruin, the Wyld Hunt**. (`exalted3e/assets/discipline/adversity-calibration.md`)
- **Resolution:** Fate Chart · **Chaos flavor:** standard · **Discipline:** HARDCORE (Peril Points OFF)

## Turmoil ≡ Chaos Factor: 4
_(was 5; Scene 3 closed PC-firmly-in-control → −1. One shared 1–9 value. −1 if the PC was mostly in control of the last scene; +1 if chaotic.
Adjust via `mythic-gm/scripts/state.py chaos <+1|-1> <CF>`.)_

## CURRENT ADVENTURE: The Silt Marches Subjugation
- **Adventure status:** active (Session 1 closed; resume at Scene 4 — "Eyes on the Road")
- **Theme priority (this adventure):** Action, Tension, Mystery, Social, Personal _(rolled at the adventure's start; held for its duration; new adventures roll from `exalted3e/bridge/theme-weights.md`)_

## ⏸ SESSION 1 — CLOSED ("The Night of Mahru") · resume pointer
> **Status: SAVED. Session 1 complete; advancement processed.** Pick up at **Scene 4 — "Eyes on the Road,"** grey dawn at
> Vashri Crossing, Turmoil/Chaos **4**. (On resume: restate the Creed, recap the 2–3 beats below, then "What do you do?")
> **Recap:** A hidden Lunar (Ophris, posing as a Wood Aspect of House Ophris in Pure-Way Prasad) was bound by senior
> **Akatha** god-hunter **Prelate Anuhya** to subjugate the rebel river-god **Mahru**. He bested Burano Ravan twice (court
> + a command-split raid), then — when Mahru flooded the camp to break the binding rites — saved his crew, witch-warded
> the flood, traced the god to the **drowned heart of his burned shrine**, and at the south reed-channel forced an
> **ultimatum** that made the grieving god kneel and take the Pure Way collar (penance: the 11 dead freed). Triumph, with
> a price: a bitter bound god, a betrayed emissary, and **Anuhya's scrutiny riveted on him (3/?)**. Dawn: the column
> marches south for the marches' other gods; reinforcements (incl. **Burano**) arrive; a **hidden watcher's eyes** settle
> on Ophris (new plotline).
> **Advancement banked:** **+5 xp · +4 Lunar xp** (unspent — see `character-sheet.md` Experience ledger & spend menu).
> **On next rest:** motes & WP refresh to full before the march.

## The Lunar (PC)
See `character-sheet.md`. Quick line: **Ophris ("Shake")**, No Moon, Essence 1 · motes 16/16 P, **25/38 Periph (refresh on rest)**
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
5. **Mahru's reckoning** — the drowned god who took your soldiers; a Pure Way-marked "rebel god" — now ATTACKING the
   camp to pre-empt his own subjugation. *(3)*
9. **The leak — who fed the marsh the plan?** (Turning Point 1: Secret Information Leaked). Mahru's host hit the exact
   soft seam of the disposition Ophris spoke in the writ-tent (Ravan + clerks present). Unknown. *(2, mystery)*
10. **THE WATCHER — someone is studying Ophris** (NEW PLOTLINE, Turning Point 2: The Observer). At dawn Ophris's
   ambush-instinct flags a hidden, patient, *knowing* observer who has watched him do impossible things (warding a god,
   bargaining a deity) and is now **marching south with the column.** Ophris has only deniable unease — **identity &
   purpose UNEARNED** (the leak-spy? a Burano agent in the new contingent? an Akatha watcher of Anuhya's? a Silver Pact
   scout / Tanisa's? the emissary?). The campaign's new driving tension — eyes on the hidden Lunar. *(3, new)*
6. **The sanctified expedition** — ACCEPTED. Ophris will lead a rite-bound expedition to subjugate/destroy Mahru,
   under **Akatha** Prelate Anuhya's direct oversight; marches once the rites are prepared. His chance to "make
   something of myself" — chained to an Akatha god-hunter's lamp held to the secret, with his fake element expected
   to manifest on the water. *(3, active)*
7. **The Burano rivalry / Ravan's grudge** — Ravan's legal raid to split the command was **DEFEATED**: Ophris ignored
   the bait, presented a clean operational plan (Int+War, 4 succ), and Sesrina struck the split — *"That is a commander."*
   **Sole command affirmed**, court competence-stain partly mended, Ravan bested twice in one night and withdrawn with a
   face-saving nicety + a deepening grudge. The rivalry is now personal and patient. *(2)*

## Characters List (NPCs & forces in play; the PC is NOT listed)
1. **Akhil** — younger brother; **genuine Fire Aspect** Dragon-Blood of House Ophris (canonized in play); knows the
   secret; closest tie. Hot, blunt, fiercely protective; his real Exaltation is part of what makes Ophris's cover hold.
   Present as Ophris's aide. Stance after the court: the Akatha leash terrifies him; wants the 11 dead given rites; uneasy
   about the unknown stranger; offered to set the watch on them or brace them himself. *(3)*
2. **Bhaskar & Sudha** — parents, heads of House Ophris; hid him. *(2)*
3. **Tanisa Ring-Eater** — shahan-ya, master schemer; runs Ophris as an asset (Mount Namas). *(2)*
4. **Burano Ravan** — rival of House Burano. Exposed Ophris's false blame-shift in open court. *(2)*
5. **Prelate Anuhya** — **senior Clan Akatha** god-hunter prelate-monk. **Appearance (seen up close):** small, spare,
   age-indeterminate (DB-slow; silt-grey cropped hair, fine-creased eyes); white Pure Way robes; the **triple sigil**
   (plum-blossom / banner / closed eye = Akatha spirit-blood, Pure Way authority, the watching office); a rope of dark
   jade **screaming-face prayer-beads** wound on her right hand (her god-strangling tool); flat lightless brown eyes,
   a scent of altar-smoke & plum-blossom — **God-Blooded uncanniness**; the economy of a body that has bent gods barehanded.
   **Stillness like deep water / a drawn bow.** Now openly suspicious of "Captain Ophris" (scrutiny 3) — didn't buy his
   *"just lucky"* but had nothing to seize; **banked it, patient and permanent**, and means to keep him at her elbow the
   whole expedition: *"We'll have such time to talk, you and I."* **THE DANGER — worst possible chaperone for a Lunar.** *(3)*
6. **Prefect Sesrina of the Cinquefoil Banner** — Prince of the Earth (DB, Ess 3), frontier prefect at Vashri Crossing.
   Icy, by-the-book Air-aspect; Major Principle *"discipline & doctrine win the frontier"*; Resolve 4. Twice impressed by
   Ophris; confirmed the campaign continues (Mahru was "the gate, not the war"). **STEPS DOWN (AC −1 → weight 1):** she
   **holds Vashri Crossing** while the column marches south — recedes from the traveling story. *(1)*
7. **Mahru, the Drowned God of the border marches** — **SUBJUGATED** (ultimatum, 6 succ vs Resolve 5): knelt, gave penance
   (freed the 11 dead), took the Pure Way collar under Akatha — a bitter bound vassal. **DOWNGRADE (AC −2 → weight 1):**
   recedes to a quiet, latent thread in his channel (the hateful caged god — a lever for a future reckoning). *(1)*
8. **Mahru's ruined emissary** (the waterline stranger) — a drowned god-blood / shrine-priest of Mahru. Was **well-disposed**
   and twice offered Ophris its hope; Ophris used the second offer to fit the god's collar. **Goodwill CURDLED to contempt**
   — *"You always think the collar is the mercy"* — and withdrew into the deep. Now likely a bitter, dangerous loose end. *(2)*
9. **Seven Obsidian Leopard** — Tanisa's necromancer-partner; wants Prasad destroyed. *(1, offstage)*

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
- **Pure Way scrutiny of House Ophris's "new Wood Aspect" [3/?]** — TICKED HARD: across one night Ophris warded a god,
  traced its anchor, and *bargained a rebel god into the fold* — brilliance no field-surgeon should have. Anuhya's last
  words: *"Who wards like a temple adept and bargains gods like an Akatha karta… Captain Ophris, who ARE you?"* Her
  attention is now **riveted and openly probing** (appetite, edging toward suspicion). Veil still held — barely.
- **Mahru's attention on Ophris [latent]** — the god turned his awareness on the warder; whether his Essence-sight ever
  perceived the Lunar truth through the disguise stays **UNEARNED, ominous** — and now Mahru is a bound vassal who may know.
- **NIGHT OF MAHRU — RESOLVED:** the assault ended by **oath, not force** — Ophris's ultimatum made the god submit;
  Anuhya sealed a Pure Way **submission-binding**. Camp held, flood gone, the 11 dead floated back **freed** (penance,
  owed their rites). The shrine-heart in the south reed-channel was **never broken** — it stays Mahru's last home, now
  the seat of a bound vassal (**a latent lever** for any future Mahru reckoning). The emissary fled, contemptuous.

## Overlays (Mythic; optional)
- **Keyed Scenes:** none · **Thread Progress Track:** none · **Peril Points:** OFF (player-invoked only).

## Adventure Crafter state
- **TP1 — "The Marsh Doesn't Wait"** (Scene 3, INTERRUPT). Plotline: the sanctified expedition (Advancement). PPs: MASS
  BATTLE + SECRET INFORMATION LEAKED. → resolved: Mahru's assault, then his subjugation by ultimatum.
- **TP2 — "Eyes on the Road"** (Scene 4, INTERRUPT, test 1d10=2). **NEW PLOTLINE** (1d25=12). PPs: **THE OBSERVER**
  (Mys49) + **REINFORCEMENTS** (Soc63) + **CHARACTER DOWNGRADE** (Meta 58 → Mahru 3→1) + **CHARACTER STEPS DOWN**
  (Meta 52 → Sesrina 2→1); 1× None. Reading: as the relief column (legion + Akatha rite-cadre + a **Burano** contingent)
  arrives for the deeper march and Mahru/Sesrina recede, a hidden **observer** is now studying Ophris on the road.
- Scenes played: 4. Theme priority: Action, Tension, Mystery, Social, Personal.

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
- **SCENE 4 — "Eyes on the Road"** · Vashri Crossing, grey dawn · Turmoil/Chaos 4 · **OPEN (Turning Point 2, NEW
  plotline).** Ophris ordered rites for the 11 freed dead (Akhil oversaw). Debrief w/ Sesrina: **the campaign CONTINUES**
  — Mahru was "the gate, not the war"; the column marches south at first light (Anuhya's rite-cadre along) to bring the
  Silt Marches' other drowned/burning gods to heel & open the road. Ophris's command confirmed/expanded; star high.
  **INTERRUPT:** dawn relief column arrives (legion + Akatha rite-cadre + a **House Burano** contingent — Ravan's reach
  on the campaign), and **Ophris's ambush-instinct flags a hidden OBSERVER** — patient, knowing eyes that watched him do
  the impossible by the channel and are now marching with him. **Deniable unease only; the watcher's identity UNEARNED.**
  - **Open decision:** what Ophris does — hunt the watcher / meet the reinforcements & the Burano contingent / prep the
    march / a word with Anuhya or Akhil / rest. Init n/a (out of combat). Periph 25/38 · WP 5 · Limit 0 · anima Dim · veil holding.
- **SCENE 3 — "The Marsh Doesn't Wait"** · Vashri Crossing, night camp · **CLOSED** (Turning Point 1).
  Ophris was visiting his grieving crew when **Mahru's host stormed the camp's marsh-ward edge** — drowned dead, marsh-
  beasts, reed-painted marsh-folk, the water itself — pre-empting the rites. The assault hits the **soft seam of the
  plan Ophris spoke an hour ago** (→ the plan leaked). **Exchange 1 resolved:** Ophris ordered the **fall-back**
  (Cha+War+stunt, **5 succ/thr 2**) → crew pulled out of the seam in order, wounded saved (Akhil enforcing); **the flood
  took the 11 unburied dead.** He strode forward to find/kill the leading spirit — **Fate: Exceptional No, there is none:
  Mahru is the bodiless flood, unduelable.** His hunt (Per+Aware+spec, **5 succ/thr 2**) revealed the surge's true axis:
  **it drives past the camp at the Akatha rite-pavilion**, to break the rites before they seal. Anima still **Dim** (no
  flare; mask = Essential Mirror Nature, doesn't burn). **Disguise ruling:** Essential Mirror Nature + Shifting Penumbra
  Stance let his anima flare as a Wood Aspect's & use ordinary Charms safely; **flagrant Lunar miracles (the Sky-Titan)
  would blow it**, and a god's Essence-sight may pierce the mask if he closes with Mahru.
- **Exchange 2 (Scene 3 / COMBAT JOINED):** Ophris called for Anuhya. **Fate: she CANNOT break Mahru alone** (rites
  unsealed). Her god-hunter directive: *"You don't fight a flood — you find its FOOT."* **Mahru has a material SEAT/anchor
  in this water (a shrine-heart, idol, or a drowned vessel he's poured his name into); break it and she can cage the
  rest — but the pavilion/her circle must be kept clear.** New objective: **find & break Mahru's anchor** (location
  UNKNOWN — a hunt; the emissary/south reed-channel/the taken dead may relate). **Horror:** the drowned spearhead
  includes Ophris's own freshly-taken dead in Prasadi harness.
- **Exchange 3 (Scene 3 / COMBAT round 1):** Ophris withered the drowned battle group (Violet Bier reaper daiklave;
  Dex5+MA5+Acc5+spec+stunt = 18d → 6 succ/thr3; raw15−soak5 → 6 Init dmg). **Crashed them** (+5 Break) → **Ophris
  Initiative 18**, unhurt; drowned at **−2, Crashed** (god-driven, no rout). Their counter-claw **missed** (Parry 6 held).
  Grim: the front rank were his own taken dead in Prasadi harness (cut down a soldier he'd once stitched). **Anima still
  DIM — no motes/Charms spent; mask intact.** Reaper daiklave finalized: **Acc +5, Dmg +10L withering, Def +0, Ovw 3.**
- **Exchange 4 (Scene 3 / COMBAT round 2):** Ophris coiled (Agile Beast Defense 1m) and **Coiled Serpent Strikes** (3m)
  decisive counter — gorgeous to-hit (13d → 12 succ, five 10s) but the decisive **damage rolled poorly (18d → 3 succ)**:
  the god-knit drowned barely thinned (**HL 3/10, still up, Crashed**). **Ophris Initiative reset 3.** Lesson landed hard:
  you can't win by fighting the water. **Honest cost:** the flood poured PAST during the fight → **Anuhya's circle is at
  its LAST candle**, the rites about to fail. Motes: 4 peripheral spent (**Periph 30/38**), anima Dim, mask intact, unhurt.
- **Weapon corrected (player, going-forward):** moonsilver Violet Bier daiklave = **MEDIUM** artifact: **Acc +3, Dmg +11L,
  Def +1, Ovw 4** (the +1 Def is why Parry is 6 with it drawn). Decisive to-hit uses no weapon bonus (engine rule).
- **COMBAT board (scratch /tmp/tide_combat.json):** **Ophris Init 3 / HL 10 full**; **drowned Init −2, HL 3/10, Crashed**
  (bottomless — Mahru replenishes). Onslaught wearing Ophris's guard when swarmed.
- **Exchange 5 (Scene 3):** Ophris pivoted off the blade to **improvised flood-warding rites** (Int 5 + Occult 3 + Int
  Excellency 5m + 1-stunt = 15d → **5 succ vs diff 5, thr 0**). The wards HOLD the flood's leading edge at the sand-line;
  **Anuhya's circle survives, time bought** — but bare success = **no anchor lead gained**, and the **wards are eroding.**
  Two consequences: (a) **Mahru's attention turned toward Ophris** (the god "looked at" the warder — Essence-sight
  exposure risk, unresolved); (b) **Anuhya saw a "Wood Aspect" ward a god expertly** → scrutiny clock → 2, her interest
  sharpened. Motes **Periph 25/38**; anima flickers green (reads as Wood, reinforces cover); Init 3; unhurt; WP5; Limit0.
- **COMBAT:** the wards cut the drowned off from the flood's push; the immediate melee eases (drowned group HL 3/10 still
  about, but the surge is held at the line). Scene is pivoting from fight → the anchor hunt.
- **Exchange 6 (Scene 3):** Ophris traced the god's Essence (Per 5 + Occult 3 + hot-trail 2 = 10d → **6 succ/thr3**).
  **ANCHOR FOUND:** the drowned shrine-heart in the **south reed-channel** (= the emissary's parley spot). Felt the god's
  **grief**. Veil held (strong roll → not read back). No motes spent.
- **Exchange 7–8 (Scene 3 / CLIMAX & RESOLUTION at the south reed-channel):** at the drowned heart, the emissary still
  tried to talk (Fate: Yes) and laid out Mahru's terms (be LEFT, not caged). Anuhya pressed for the hammer. **Ophris
  threaded a THIRD path — an ultimatum:** kneel, pay penance for the dead, take Pure Way instruction under Anuhya, **or
  die** (threaten/persuade, **6 succ vs Resolve 5**). **Mahru chose survival → SUBJUGATED:** the flood receded, the 11
  dead floated back freed (penance), the god took the collar as a bound Prasadi vassal. **Outcome for Ophris — a
  masterstroke:** camp saved, rebel god brought into the fold (Akatha's ideal), his dead avenged & returned, **cover &
  standing hugely bolstered** ("make something of myself" ↑). **Costs:** a bitter bound vassal-god; the emissary's
  goodwill curdled to contempt; **Anuhya's scrutiny → 3, now openly probing — *"Captain Ophris, who ARE you?"*** Veil held.
- **SCENE 3 RESOLVING (Turning Point 1 essentially complete — the sanctified expedition's crisis ended early & on Ophris's
  terms, at the camp, no marches-campaign needed).** Aftermath beat open: the kneeling god, the freed dead, the vanished
  emissary, Akhil, and **Anuhya's point-blank question hanging in the air.** PENDING bookkeep: **Chaos −1 → 4** (PC firmly
  in control). Combat ended (flood gone) — clear board. Motes Periph 25/38 · WP 5 · Limit 0 · anima Dim · veil intact.
- **SCENE 1 — "Two Houses, One Frontier"** · Vashri Crossing war-court · CLOSED. Outcome: Ophris landed his doctrine
  point on Prefect Sesrina (4 vs Resolve 4) but his false Burano-blame was exposed by Ravan (ground-truth: the recon was
  Ophris's OWN charge). He then deferred to **Prelate Anuhya**, who declined to shelter him, named Mahru a *rebel god*,
  and bound Ophris to lead the sanctified subjugation **under her oversight**. Ophris paid pious homage and ACCEPTED
  (low-suspicion; locked the expedition). Anuhya revealed as **senior Clan Akatha** (Exceptional Yes) — a god-hunter,
  the worst chaperone for a hidden Lunar; she expects his "Wood element to show plainly" on the marches.
  Close: **PC not in control → Chaos +1 → Turmoil/Chaos 6.**
- **SCENE 2 — "What Walks Out of the Water"** · Vashri Crossing camp, dusk · **CLOSED** (opened ALTERED, scene test
  1d10=1). Delivered: first contact with Mahru's emissary (parley window banked) + defeat of Burano's command-split.
  Close: PC in control → **Chaos −1 → 5.** Net for Ophris: **sole command secured, a secret door to the god open,
  competence-stain easing** — at the cost of an Akatha leash still looming and a god that has now seen his face.
- **Last beat / recap:** Ophris steps out into the garrison-town (granary-turned-fort at the Silt Marches ford, Dreaming
  Sea SW). His domain: the field-infirmary. Across the yard: Akatha's white pavilion. His surviving cohort sits grieving;
  **11 wrapped dead** still await rites. Akhil at his shoulder. At the silt-line, a **travel-worn stranger** was expertly
  reading Mahru's water/silt and then met Ophris's eye as if waiting for him. Akhil hasn't seen them yet.
- **Exchange 1 (Scene 2):** Akhil's read (Fire Aspect): the Akatha leash is the knife, Ravan's framing will travel, the
  11 dead are owed rites; he doesn't recognize the stranger (Fate: No) and offered to watch/brace them.
- **Exchange 2 (Scene 2):** Ophris went down with open hands and greeted the stranger. Reveals (rolled): the figure is
  **Mahru's drowned, ruined emissary**, **well-disposed**, offering parley before the war — naming the impious
  shrine-burning, marking Ophris as different for coming hands-open. **Doubles → Random Event (Remote·Divide·Legal):**
  a runner brings word that **House Burano has moved at the writ-tent to SPLIT the expedition's command.**
- **Exchange 3 (Scene 2):** Ophris deferred the parley → recontact at the south reed-channel before the rites; emissary
  withdrew. **Exchange 4 (Scene 2, CLOSE):** at the writ-tent Ophris ignored Ravan, presented a clean operational plan
  (Int 5 + War 3 + Int Excellency 4m + 1-stunt = 14d → **4 succ vs diff 3**), invited Burano's input. Sesrina struck the
  split — *"That is a commander"* — **sole command affirmed**, competence-stain easing; Ravan withdrew bested with a
  banked grudge. **SCENE 2 CLOSED. PC in control → Chaos −1 → 5.**
- **Open / next-scene seeds (player's pick frames Scene 3 — will get a scene test):** (a) give the **11 dead their
  rites**; (b) take the **parley window** — south reed-channel, alone, before Akatha seals the rites (risky, off-book,
  a god who may sense what he is); (c) **expedition prep** / coordinate with Anuhya's rites (close Akatha scrutiny);
  (d) a beat with **Akhil**; (e) rest/recover motes.
- **Adversity counter:** 1 · **Self-audit drift:** 0

## Archive pointer
- Resolved Threads / dead Characters / spent clocks → `archive.md`
