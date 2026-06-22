# Advanced & large-scale combat

**Battle groups (mass combat).** A unit is one combatant with: **Size** (0–5, adds to attack/Defense/soak and a Might-like edge), **Drill** (Poor/Average/Elite — discipline), **Might** (0–3, supernatural). Size adds bonus dice to the group's attacks and to its Defense; damage chips away Size (Magnitude). A heroic character can fight a group; routing happens on a failed morale check. Stat a group as a normal combatant in `ex_combat.py` with inflated soak/HL and note its Size.

**Morale / rout:** when a group takes heavy losses or its leader falls, roll morale; failure = it breaks. NPCs and groups act to win and rout honestly.

**Naval & mounted.** Resolve as combat with the vehicle/mount's traits; relevant Ability (Sail / Ride) gates maneuvers; ramming, boarding, and trampling are gambits or withering attacks with large base damage.

**Environmental hazards** (drowning, falling, fire, cold, poison, disease): set a difficulty or a per-round damage; resolve with `ex_dice.py pool` (Stamina+Resistance to resist) and apply Initiative or Health damage per the fiction. Poisons have damage/duration/penalty; diseases use interval rolls.

Keep the discipline: hazards and groups are real threats with pre-committed stakes; the dice decide.
