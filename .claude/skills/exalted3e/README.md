# exalted3e — Solo Exalted 3rd Edition Storyteller (skill)

A standalone solo Game-Master skill for **Exalted 3rd Edition**: play one **Lunar Exalt** in Creation with full tactical combat, social influence, sorcery, crafting, shapeshifting, a living faction world, and a built-in oracle + generator suite. Honest dice, rolled in the shell, never fudged.

**Start:** load the skill and say *"be my Storyteller for Exalted"* / *"let's play a Lunar."* Claude reads `SKILL.md` and runs Session Zero → the Turn.

**Standalone, mythic-optional.** Runs with no other skill. If `mythic-gm` is also loaded, the yes/no oracle, scene tests, and random events defer to mythic (shared `Turmoil ≡ Chaos`); everything else stays here.

## Layout
- `SKILL.md` — router: the Creed, the Turn, the oracle seam, the loading guide.
- `rules/` — distilled, LLM-facing mechanics (resolution, combat, social, sorcery, crafting, xp, charms-engine, domain/projects).
- `scripts/` — all dice & bookkeeping: `ex_dice ex_combat ex_social ex_npc ex_faction oracle projects state`.
- `charms/` — the Lunar PC catalog (642 charms across 9 Attributes) + 11 Martial-Arts styles (89 indexed) + antagonist Charm pools for 6 other Exalt types & spirits.
- `lunar/` — chargen, shapeshifting/Heart's Blood, castes/anima/Limit.
- `setting/` — Creation as AI-GM cards (Surface vs Truth secrets, clocks, hooks, handles, links, vault cites).
- `statblocks/` — index of ~200 ready foes (pull stats from the cited vault).
- `generators/` — ruins, courts, communities, challenges, cults, adventures, foes.
- `oracle/` — built-in yes/no + Creation event/meaning tables.
- `vault/` — the 16 converted rulebooks (authoritative full text; cited by everything).

## Credits
Exalted © Onyx Path Publishing (rules text lives in `vault/`, cited, not reproduced in the reference layer). The referee generators (faction turn, ruin, court, community, cult, challenge, adventure, foe assembly) are **design-inspired by Sine Nomine's _Godbound_** (Kevin Crawford), reimplemented with original Creation content. For personal play.
