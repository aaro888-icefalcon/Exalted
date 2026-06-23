# Bridge manifest — Exalted 3rd Edition (Lunar solo)

This companion supplies the **Exalted 3e ruleset** (d10 dice pools, the Initiative combat
system, social influence, sorcery, crafting, Charms, shapeshifting), the **setting of
Creation** (the Age of Sorrows, its factions and gods), and a full **generator + Creation-oracle
suite** — all of it pointing back into the `exalted3e` skill's `rules/`, `setting/`, `charms/`,
`vault/`, and `scripts/`. The `mythic-gm` engine remains the sole oracle/scene/Chaos/Random-Event/
Turning-Point layer; this bridge only fills the engine's content hooks.

Generators are built to verified JSON by `exalted3e/scripts/build_bridge_generators.py`
(the companion build step) and rolled through the engine's `dice.py table` / validated by
`bridge.py validate`.

```json
{
  "companion": "Exalted 3rd Edition (Lunar solo)",
  "engine": "mythic-gm>=2",
  "overrides": ["resolve","meaning","chaos","themes","generate:character","generate:element","world-tick","seeds"],
  "files": {
    "system_profile": "system-profile.md",
    "interpretation": "interpretation.md",
    "chaos": "chaos-tendency.md",
    "themes": "theme-weights.md",
    "generators": "generators/registry.md",
    "subsystems": "subsystems.md",
    "seeds": "seeds.md",
    "canon": "setting-canon.md"
  }
}
```
