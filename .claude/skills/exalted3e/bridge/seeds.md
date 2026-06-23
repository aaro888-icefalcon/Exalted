# Seed Sources — Creation   (hook: seeds)

The seed deck is the pool of concrete candidates the engine draws on for upcoming scenes,
Turning Points, and Random Events, so play stays Creation-native instead of generic.

- **deck size:** 35            # 30–40
- **refresh:** each bookkeeping (top up to size; drop spent seeds)
- **sources:**
  - **setting canon near the PC** — the live `setting/` cards (region, factions, named NPCs,
    bestiary) for wherever the Lunar currently stands; campaign-specific canon in the campaign's
    own `setting-canon.md`.
  - **live world state** — every faction `Problem:` on the board (Problems *are* hooks), armed
    clocks, revealed regions, standing Threads/Characters, pressed Intimacies, the rising Limit.
  - **random rolls for novelty** — draw on the companion generators:
    `community_problem`, `court_power_source` / `court_stakes`, `adventure_situation` /
    `adventure_draw` / `adventure_threat`, `encounter_<direction>`, `ruin_purpose`, `cult_problem`,
    and the Creation Meaning words (`meaning_action` / `meaning_theme` / `meaning_subject`).
- **consumed** when a seed is spent by a scene / Turning Point / Random Event (then refreshed).

The main AI populates the deck inline at bookkeeping; optionally offload the harvest to the
engine's **mythic-scout** agent (`mythic-gm/references/scout.md`).
