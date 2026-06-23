# Generator Index — Creation   (hooks: generate:*, meaning)

A routing index, **not** a blanket override. Each row: *need · when it's called · table(s) · mode*.
**mode** = `replace` (use the companion table), `conjunction` (companion layered on the Mythic/AC
core), `default` (fall through to Mythic/AC). Anything not listed → Mythic/AC default.

All tables are `list_d100`/`list_d10` JSON in this folder, built by
`exalted3e/scripts/build_bridge_generators.py` and rolled with:
`python3 .claude/skills/mythic-gm/scripts/dice.py table <abs path to the json>`.

| need | when called | table(s) | mode |
|------|-------------|----------|------|
| Creation flavor word | a Meaning pull / Random-Event detail in Creation | `meaning_action`, `meaning_theme`, `meaning_subject` | **conjunction** — use the Creation words for setting-true texture; combine with the engine's Mythic Meaning when a broader nudge helps |
| generic inspiration | Discover Meaning, no specific need | Mythic Elements (`oracle.py elements`) | **default** |
| new NPC (traits) | any new Character invoked | AC Character Crafter (`oracle.py character`) **+** `meaning_subject` / `court_role` for a Creation role | **conjunction** |
| new NPC (stats) | a Character needs mechanics | `ex_npc.py stat <mortal\|elite\|hero\|young-exalt\|exalt\|legendary>` (statblocks in `statblocks/`) | **replace** |
| a place: ruin / First Age site | PC enters a manse, tomb, shadowland, demon-prison, old place | **Ruins set** (see recipe) | **replace** |
| a place: settlement | the Lunar arrives at a village / town | **Communities set** (see recipe) | **replace** |
| a power-group / court | a satrap court, House seat, Lunar council, Guild caravan, god-court | **Courts set** (see recipe) | **replace** |
| a faction / cult | a new faith-as-faction or org | **Cults set** (see recipe) + `setting/04_factions.md` + `ex_faction.py` | **replace** |
| a wilderness encounter | travel in the wilds | `encounter_north` / `encounter_east` / `encounter_south` / `encounter_west` | **replace** |
| an obstacle (make it a scene) | "the PC wants X" should not just succeed | `challenge_goal_type` → that goal's complication table | **replace** |
| a session hook | starting a session / needing a reason to act | **Adventures set** (see recipe) | **replace** |
| an antagonist's flavor | statting a rival Exalt, behemoth, spirit | **Foes set** (see recipe), paired with `ex_npc.py` | **replace** |
| a faction's action (world-tick) | a faction acts at bookkeeping | `faction_move` (pair with `ex_faction.py turn`) | **replace** |
| an omen / Wyld weirdness | a supernatural tell; a Wyld zone | `omen` · `wyld_weirdness` | **replace** |

## Multi-step recipes (roll the set in order; skip what's dull)
- **Ruins:** `ruin_purpose` → `ruin_hazard` → `ruin_inhabitants` (+ sub-rolls `ruin_why_here`,
  `ruin_goal`, `ruin_leadership`, `ruin_defenses`, `ruin_internal_problem`, `ruin_recent_event`,
  `ruin_external_stance`) → for each of ~6 rooms: `ruin_room_purpose`, `ruin_room_valuables`,
  `ruin_room_mood`, `ruin_room_ingress`, `ruin_room_peril`, `ruin_room_feature`, `ruin_room_info`
  → `ruin_reward`. (Full prose: `generators/ruins.md`.)
- **Courts:** `court_structure` → `court_mood` → 3+ actors (each: `court_role` + `court_power_source`
  + `court_agenda`) → `court_stakes` → 2–3 `court_minor_actor` → if attacked: `court_defenses`;
  if destroyed: `court_consequences`. *Signature move: an **orphaned power source** is a ready hook.*
- **Communities:** `community_nature` → `community_leadership` → `community_feature` →
  `community_problem` (the cry for a god = the hook) → `community_tell` → `community_stance`.
- **Cults:** `cult_patron` → `cult_severity` → `cult_feature` → `cult_problem` (1–2) → `cult_growth`
  → `cult_subtype` (its faction Goal archetype).
- **Adventures:** `adventure_situation` + `adventure_draw` + `adventure_threat` + a Challenge
  (`challenge_goal_type` → complication). *Shortcut: pull a live faction `Problem:` as the hook.*
- **Foes:** `foe_attack_pattern` + `foe_defense` + `foe_mobility` + `foe_impairing`, then write the
  per-foe **Tactics** block (Opener / Standard turn / Signature / When crashed / When hurt / Never
  forgets — `generators/foes.md`) and assemble numbers with `ex_npc.py`.

The markdown in `exalted3e/generators/` and `exalted3e/oracle/` is the human-readable source of
truth and the full design notes (House style, cross-refs, worked examples); this folder is its
verified, machine-rollable form. **Problems are hooks** — a rolled Problem can be promoted straight
onto a faction's `Problems:` line, and clearing it visibly moves the board.
