# Combat tracker
Live board is maintained by `scripts/ex_combat.py` (prints Initiative order, Health, onslaught, Crash). Start a fight with `ex_combat.py new`, add the Lunar with `join`, add foes with `join`/`add` (stat fast via `ex_npc.py stat <tier>`), then resolve with `withering`/`decisive`/`gambit` and `endturn` after each combatant. The board persists in `campaign_state.json`.
