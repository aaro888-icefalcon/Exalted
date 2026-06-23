# exalted3e — Exalted 3rd Edition companion (skill)

The Exalted **companion** to the `mythic-gm` engine: play one **Lunar Exalt** in Creation with full tactical combat, social influence, sorcery, crafting, shapeshifting, a living faction world, and a generator suite. The engine supplies the oracle, scene tests, Random Events, and pacing; everything Exalted lives here. Honest dice, rolled in the shell, never fudged.

**Start:** load **both** skills (`mythic-gm` + `exalted3e`) and say *"be my Storyteller for Exalted"* / *"let's play a Lunar."* Claude reads each `SKILL.md`, loads the companion `bridge/`, and runs Session Zero → the Turn.

**Companion architecture.** This skill fills the engine's hooks through its **`bridge/`** (`bridge.md` manifest): `system-profile.md` (resolution), `interpretation.md` (the GM agenda/lens), `chaos-tendency.md`, `theme-weights.md`, `subsystems.md`, `seeds.md`, `setting-canon.md`, and `generators/` (verified JSON). The engine owns the oracle/scene/Chaos layer; `Turmoil ≡ Chaos` is one shared value. See `docs/INTEGRATION.md`.

## Layout
- `SKILL.md` — router: the Creed, the Turn, the bridge seam, the loading guide.
- `bridge/` — the declarative hooks the engine reads (manifest, system-profile, interpretation, generators, …).
- `rules/` — distilled, LLM-facing mechanics (resolution, combat, social, sorcery, crafting, xp, charms-engine, domain/projects).
- `scripts/` — all Exalted dice & bookkeeping: `ex_dice ex_combat ex_social ex_npc ex_faction projects state` + `build_bridge_generators.py` (builds the bridge JSON tables).
- `charms/` — the Lunar PC catalog (642 charms across 9 Attributes) + 11 Martial-Arts styles (89 indexed) + antagonist Charm pools for 6 other Exalt types & spirits.
- `lunar/` — chargen, shapeshifting/Heart's Blood, castes/anima/Limit.
- `setting/` — Creation as AI-GM cards (Surface vs Truth secrets, clocks, hooks, handles, links, vault cites).
- `statblocks/` — index of ~200 ready foes (pull stats from the cited vault).
- `generators/` — ruins, courts, communities, challenges, cults, adventures, foes (markdown source → `bridge/generators/*.json`).
- `oracle/` — Creation event/meaning tables (source for `bridge/generators/`); the engine rolls the oracle.
- `vault/` — the 16 converted rulebooks (authoritative full text; cited by everything).

## Credits
Exalted © Onyx Path Publishing (rules text lives in `vault/`, cited, not reproduced in the reference layer). The referee generators (faction turn, ruin, court, community, cult, challenge, adventure, foe assembly) are **design-inspired by Sine Nomine's _Godbound_** (Kevin Crawford), reimplemented with original Creation content. For personal play.
