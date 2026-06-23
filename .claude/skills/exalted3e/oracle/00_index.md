# Oracle — Creation-native content for the mythic-gm engine

The `mythic-gm` engine is the **sole oracle**: yes/no Fate Questions, scene tests, Random Events,
Turning Points, and Chaos all run through it. These tables are the **Creation-native content** the
engine plays through — the companion's Meaning words and event/encounter tables, surfaced via
`bridge/generators/` (built to verified JSON by `scripts/build_bridge_generators.py`, rolled with
`mythic-gm/scripts/dice.py table`). `Turmoil` (Exalted) and `Chaos` (the engine) are the same 1–9
value in state.

- `01_meaning_tables.md` — Creation interpretation words → `bridge/generators/meaning_{action,theme,subject}.json`
- `02_event_tables.md` — Creation events/encounters → `bridge/generators/{faction_move, encounter_north,
  encounter_east, encounter_south, encounter_west, wyld_weirdness, omen}.json`

This markdown is the human-readable source of truth and design notes; the bridge JSON is its
machine-rollable form. See `bridge/generators/registry.md` for routing (which need → which table → mode).
