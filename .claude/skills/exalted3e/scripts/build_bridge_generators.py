#!/usr/bin/env python3
"""
build_bridge_generators.py — the COMPANION build step (CONVERSION.md step 3).

Emits verified, machine-rollable JSON tables into `exalted3e/bridge/generators/`
from the Exalted 3e generator + oracle content (the markdown in `exalted3e/generators/`
and `exalted3e/oracle/` is the human-readable source of truth; this script is the
single place that turns it into engine-schema tables).

Mirrors the pattern of the engine's `mythic-gm/scripts/build_data.py`. Every table is
encoded as `list_d100` (rolled 1d100) or `list_d10` (rolled 1d10) — the only two shapes
the engine's `dice.py table` rolls and `bridge.py validate` coverage-checks — with
contiguous ranges guaranteed by construction. Original d6/d8/d12/d20 menus are mapped
onto even d100 buckets; explicitly weighted d20 tables keep their weighting (x5).

Run:  python3 .claude/skills/exalted3e/scripts/build_bridge_generators.py
Then: python3 .claude/skills/mythic-gm/scripts/bridge.py validate .claude/skills/exalted3e/bridge
"""
import json, os, sys

HERE = os.path.dirname(os.path.abspath(__file__))
GEN = os.path.join(os.path.dirname(HERE), "bridge", "generators")
os.makedirs(GEN, exist_ok=True)
built, errors = [], []

# ---------------------------------------------------------------- encoders
def even_d100(options):
    """N uniform options -> contiguous d100 buckets summing to 100."""
    n = len(options); base, rem = divmod(100, n); entries = []; lo = 1
    for i, v in enumerate(options):
        size = base + (1 if i < rem else 0)
        entries.append({"min": lo, "max": lo + size - 1, "value": v}); lo += size
    return entries, "list_d100", "1d100"

def d10(options):
    """Exactly 10 options -> 1d10, one per face."""
    assert len(options) == 10, f"d10 needs 10 options, got {len(options)}"
    return [{"min": i + 1, "max": i + 1, "value": v} for i, v in enumerate(options)], "list_d10", "1d10"

def weighted20(ranges):
    """Explicitly weighted d20 ranges [(lo,hi,value)] -> x5 onto d100 (preserves weighting)."""
    return [{"min": (lo - 1) * 5 + 1, "max": hi * 5, "value": v} for (lo, hi, v) in ranges], "list_d100", "1d100"

def weighted_d100(ranges):
    """Explicit [(min,max,value)] already on d100 (for non-uniform low-die weightings)."""
    return [{"min": lo, "max": hi, "value": v} for (lo, hi, v) in ranges], "list_d100", "1d100"

def uniform(options):
    return d10(options) if len(options) == 10 else even_d100(options)

def T(name, title, packed, src, note=None):
    entries, ttype, dice = packed
    cov = sum(e["max"] - e["min"] + 1 for e in entries)
    need = 100 if ttype == "list_d100" else 10
    if cov != need:
        errors.append(f"{name}: coverage {cov}/{need}")
    obj = {"id": f"exalted.{name}", "title": title, "type": ttype, "dice": dice,
           "source": src, "entries": entries}
    if note: obj["note"] = note
    json.dump(obj, open(os.path.join(GEN, f"{name}.json"), "w", encoding="utf-8"),
              ensure_ascii=False, indent=1)
    built.append(name)

ORACLE = "exalted3e/oracle/"
G = "exalted3e/generators/"

# ============================================================ CREATION ORACLE
# Creation-flavored Meaning words (layer onto / replace Mythic Meaning in Creation).
T("meaning_action", "Creation Meaning — Action", uniform([
    "Betray", "Bestow", "Demand", "Pursue", "Conceal", "Threaten", "Bargain", "Reveal",
    "Hunt", "Bind", "Corrupt", "Liberate", "Usurp", "Mourn", "Ascend", "Sacrifice",
    "Awaken", "Ruin", "Guard", "Transform"]), ORACLE + "01_meaning_tables.md")
T("meaning_theme", "Creation Meaning — Theme", uniform([
    "fate", "blood", "jade", "ghosts", "ambition", "exile", "famine", "sorcery", "oaths",
    "empire", "the Wyld", "memory", "divinity", "plague", "rebellion", "hunger", "masks",
    "the dead", "gold", "ruin"]), ORACLE + "01_meaning_tables.md")
T("meaning_subject", "Creation Meaning — Subject", uniform([
    "a satrap", "a god", "a Dragon-Blood", "a Lunar elder", "a beastfolk", "the Guild",
    "a ghost", "a raksha", "a peasant", "a Wyld Hunt", "a demon", "an heirloom", "a manse",
    "a Deathlord's agent", "a spirit court", "an oathbreaker", "a rival", "a cult",
    "a behemoth", "the returned Solars"]), ORACLE + "01_meaning_tables.md")

# Faction move (pair with ex_faction.py) — the world-tick faction action.
T("faction_move", "Faction Move", d10([
    "raids a rival", "fortifies", "recruits / expands a Feature", "a Problem erupts publicly",
    "sues for alliance", "plants a spy (Interest)", "launches a Project", "internal feud",
    "hunts the PC", "a leader falls"]), ORACLE + "02_event_tables.md")

# Wilderness encounter by Direction (reroll/flavor by region card).
T("encounter_north", "Wilderness Encounter — North", uniform([
    "ice-walker raiders", "a frost-behemoth", "a Bull's-empire patrol", "a Wyld blizzard",
    "a hungry-ghost band", "stranded refugees", "a Lunar's beastfolk scouts",
    "a buried First Age cache"]), ORACLE + "02_event_tables.md")
T("encounter_east", "Wilderness Encounter — East", uniform([
    "spirit of a great tree", "Haltan beast-legion", "bandit lord", "a wandering god",
    "a raksha noble in disguise", "plague village", "a Solar tomb mouth",
    "Guild caravan"]), ORACLE + "02_event_tables.md")
T("encounter_south", "Wilderness Encounter — South", uniform([
    "fire dust smugglers", "a sand-behemoth", "Delzahn riders", "a djala cult",
    "a heat mirage-freehold", "salt-zombie swarm", "an oasis spirit's price",
    "a Realm satrap's tax-fleet"]), ORACLE + "02_event_tables.md")
T("encounter_west", "Wilderness Encounter — West", uniform([
    "Lintha pirates", "a sea-behemoth", "a storm-mother's wrath", "a drowned manse",
    "island Wyld zone", "a tya warband", "a god of a reef", "a ghost-ship"]),
    ORACLE + "02_event_tables.md")

T("wyld_weirdness", "Wyld Weirdness", uniform([
    "a road that wasn't there", "your reflection lies", "a freehold offers a bargain",
    "mutating rain", "a hobgoblin market", "a memory made flesh", "time slips a day",
    "a raksha duel of dreams"]), ORACLE + "02_event_tables.md")
T("omen", "Omen / Tell of the Supernatural", uniform([
    "animals flee a place", "a shrine bleeds", "the dead walk at dusk",
    "a child speaks prophecy", "jade hums near a wall",
    "anima-light seen on the horizon"]), ORACLE + "02_event_tables.md")

# ============================================================ RUINS
T("ruin_purpose", "Ruins — Original Purpose", uniform([
    "Solar manse-palace, anima-lit — command-phrase still half-works; hearthstone socket",
    "Shogunate war-fortress — jade armory, drilled automata-barracks",
    "First Age factory-cathedral (theurgic manufactory) — a production line that still runs on bound elementals",
    "Twilight's sorcerous workshop — half-finished working, ingredient stores, a spellbook",
    "Solar tomb / jade pleasure-dome — grave-goods, a sleeping artifact, an oathbound guardian",
    "Essence / weather engine — controls rain or wind for a satrapy, if reactivated",
    "Deliberative archive — First Age lore, maps to other ruins, a name long buried",
    "Daiklave armory — racks of artifact weapons, all keyed to dead bloodlines",
    "Lunar Wyld-redoubt — shapeshifting-cauldron, a tattoo-rite, beast-pens",
    "Ghost necropolis / mausoleum-city — a Well of soul-steel, a nephwrack's court",
    "Fae freehold half-pulled into Creation — a stolen treasure, a freehold-key, time runs wrong",
    "Sealed demon-prison — a bound Second Circle, a brass seal, forbidden pacts",
    "A neglected god's sanctum — the god still home (sleeping/mad), a relic of its portfolio",
    "Behemoth lair (occupied or vacated) — a hoard, a shed scale worth a fortune, eggs",
    "Realm-purged 'Anathema' sanctuary — a martyr's cache, Immaculate seals over a vault",
    "Drowned Western manse / coral-grown reef — pearls of Essence, a sea-god's tribute, air-pockets",
    "Threshold satrap's vault / counting-house — tribute-gold, ledgers (= blackmail), a Guild factor's cache",
    "Mountain observatory / star-shrine — a Sidereal astrology table, a prophecy, an orrery",
    "Hearthstone-quarry / geomantic node — raw demesne, uncut hearthstones, a feral elemental",
    "A ruin-in-a-ruin: two of the above, layered — roll twice; later builders dug into the older site"]),
    G + "ruins.md")
T("ruin_hazard", "Ruins — Hazard (why it's still full of loot)", weighted20([
    (1, 2, "Essence-radiation / leaking demesne — lingering causes mutation; motes drain or surge wildly"),
    (3, 3, "Wyld taint pooled in the lower halls — shapes shift, mutations, the map won't hold still"),
    (4, 5, "Awakened First Age automata still on patrol — obey dead orders; attack intruders lacking the sigil"),
    (6, 6, "Creeping shadowland necrosis — the dead walk; living Essence rots; a soul-gate yawns"),
    (7, 7, "A bound demon, seal failing — whispers bargains; one cracked sigil from freedom"),
    (8, 8, "Failing geomantic ward — floods, fire, or collapse cycles on a timer"),
    (9, 9, "Immaculate seals over the core — break them and the Wyld Hunt WILL hear of it"),
    (10, 10, "Resident behemoth (sleeping or hunting) — too big to fight; route around it or wake it"),
    (11, 11, "Temporal eddy (First Age stasis) — rooms frozen mid-disaster; time-debt on exit"),
    (12, 12, "Toxic alchemical miasma — poison gas, corroded floors, no open flame"),
    (13, 13, "Rival claimants already inside (see Inhabitants) — a tomb-robbing crew got here first"),
    (14, 14, "Structural ruin — every loud noise risks a cave-in; sound matters"),
    (15, 15, "Cursed grave-ward — takers sicken / are marked / are followed home"),
    (16, 16, "Hungry ghosts bound to the place — feed on the living's breath; placated only by rite"),
    (17, 17, "A weather-engine stuck 'on' — perpetual storm, blizzard, or killing heat inside"),
    (18, 18, "Feral elementals (the engine's old labor) — territorial, treat the PC as a thief"),
    (19, 19, "Drowned / flooded levels — the prize is underwater; tides, pressure, things below"),
    (20, 20, "The site itself is hostile (living manse) — doors close, halls rearrange, it wants to keep you")]),
    G + "ruins.md")
T("ruin_inhabitants", "Ruins — Who's Here", uniform([
    "a newly-Exalted youth + a green cult", "First Age war-automata (no master)",
    "a raksha court slumming in the ruin", "hungry ghosts under a nephwrack",
    "the resident god + sanctum-keepers", "a beastfolk warband",
    "a Wyld Hunt expedition (Dragon-Blooded + mortals)", "a Guild salvage crew with hired muscle",
    "a sorcerer with bound demons", "a Lunar/Solar rival + retinue",
    "refugees squatting, unaware what they sleep atop", "nobody living — only the Hazard"]),
    G + "ruins.md")
T("ruin_why_here", "Ruins — Inhabitants: Why Here", uniform([
    "trapped / can't leave", "came for the same prize you did", "guarding it for someone"]),
    G + "ruins.md")
T("ruin_goal", "Ruins — Inhabitants: Goal", uniform([
    "survive", "loot and go", "hold the site", "free / wake what's bound", "study it",
    "use it as a base for a wider scheme"]), G + "ruins.md")
T("ruin_leadership", "Ruins — Inhabitants: Leadership", uniform([
    "a tyrant", "a council that argues", "a charismatic believer", "a cold pragmatist",
    "leaderless / fractured", "secretly led by the Hazard itself"]), G + "ruins.md")
T("ruin_defenses", "Ruins — Inhabitants: Defenses", uniform([
    "numbers", "a chokepoint they hold", "a turned automaton / ward",
    "a hostage or relic they'll threaten", "an alarm to summon worse",
    "a Charm-user who hits above their weight"]), G + "ruins.md")
T("ruin_internal_problem", "Ruins — Inhabitants: Internal Problem (a hook)", uniform([
    "a traitor", "starving / short on Essence", "a feud splitting them", "a wounded leader",
    "a captive they mistreat", "a secret that ruins them if told"]), G + "ruins.md")
T("ruin_recent_event", "Ruins — Inhabitants: Recent Event", uniform([
    "a death", "a discovery", "a betrayal", "a failed ritual",
    "an arrival (yours, or another's)", "the Hazard worsened"]), G + "ruins.md")
T("ruin_external_stance", "Ruins — Inhabitants: Stance Toward the PC", uniform([
    "hostile on sight", "wary, will parley", "desperate for aid", "will trade",
    "try to use the PC", "indifferent until provoked"]), G + "ruins.md")
T("ruin_room_purpose", "Ruins — Keyed Room: Purpose", uniform([
    "threshold / gate", "great hall", "workshop / forge", "archive / vault", "shrine / tomb",
    "quarters", "the engine / core", "a wound (breach, sinkhole, Wyld-pool)"]), G + "ruins.md")
T("ruin_room_valuables", "Ruins — Keyed Room: Valuables", weighted_d100([
    (1, 50, "none visible"), (51, 67, "minor (coin, components)"),
    (68, 83, "a Feature (hearthstone, lore, a key)"),
    (84, 100, "the Reward (roll Reward), guarded")]),
    G + "ruins.md", note="Original 1d6: 1-3 none, 4 minor, 5 a Feature, 6 the Reward.")
T("ruin_room_mood", "Ruins — Keyed Room: Mood", uniform([
    "reverent", "ruined / sad", "tense", "wrong / uncanny", "serene (a trap)",
    "violent aftermath", "frozen mid-moment", "alive, watching"]), G + "ruins.md")
T("ruin_room_ingress", "Ruins — Keyed Room: Ingress Problem", uniform([
    "sealed door (puzzle / phrase)", "collapse blocks it", "flooded / gassed", "guarded",
    "warded (Essence cost to pass)", "only reachable via another room"]), G + "ruins.md")
T("ruin_room_peril", "Ruins — Keyed Room: Peril", uniform([
    "physical (trap, fall, fire)", "occupant (an inhabitant lairs here)",
    "magical (curse, hostile Charm-effect)", "the Hazard concentrated",
    "false floor over something worse", "none — let them breathe"]), G + "ruins.md")
T("ruin_room_feature", "Ruins — Keyed Room: Feature", uniform([
    "a working device", "a vantage / shortcut", "a clue to the Reward's lock",
    "a defensible spot", "raw Essence to harvest", "a captive / witness who knows things"]),
    G + "ruins.md")
T("ruin_room_info", "Ruins — Keyed Room: Useful Info", uniform([
    "a name", "a map", "the command-phrase", "who looted it before",
    "the Hazard's weakness", "a Problem of a faction outside (a hook out the door)"]),
    G + "ruins.md")
T("ruin_reward", "Ruins — Reward (Feature gained / Catch attached)", uniform([
    "An artifact weapon/armor (needs attunement) — keyed to a dead House that wants it back",
    "A hearthstone + its manse's location — the manse is occupied / cursed",
    "A manse command-phrase — someone else also learned it",
    "First Age lore / a map to the next ruin — the map is also a summons",
    "A sorcerous initiation or a working's notes — finishing it demands a Mighty Deed",
    "A bound spirit/elemental as ally — it serves the letter, not the spirit, of the pact",
    "Tribute-wealth (Resources for a Project) — its owner is alive and powerful",
    "A behemoth scale / rare crafting trove — the behemoth notices it's gone",
    "A prisoner freed who owes the PC — they're hunted, and now so is the PC",
    "Blackmail ledgers on a Dynast/Guild factor — holding them paints a target",
    "A geomantic node / demesne to claim — claiming it requires building (Project) + a guardian",
    "A secret (a Truth that reframes the campaign) — knowing it makes the PC a loose end to someone"]),
    G + "ruins.md")

# ============================================================ COURTS
T("court_structure", "Courts — Power Structure", uniform([
    "Autocratic — one Dragon-Blood / satrap / god rules; the rest petition",
    "Oligarchic — a handful of peers balance each other",
    "Bureaucratic — offices outlast officeholders; the ledger is king",
    "Factional — two-three blocs in open rivalry",
    "Theocratic — an Immaculate (or cult) hierarchy overrules the secular",
    "Anarchic / contested — the seat is empty or disputed; power is up for grabs"]), G + "courts.md")
T("court_mood", "Courts — Mood", uniform([
    "paranoid", "complacent", "grieving a recent death", "celebrating (a wedding, a victory)",
    "starving for coin", "braced for war", "festering with a buried scandal",
    "desperate for a savior", "smug and cruel", "fracturing openly",
    "in mourning for a vanished patron", "watching the PC the moment they enter"]), G + "courts.md")
T("court_role", "Courts — Actor Role", d10([
    "the seat-holder (satrap / matriarch / god)", "the heir / rival claimant", "the spymaster",
    "the treasurer / factor", "the priest / Immaculate", "the general / garrison-commander",
    "the favored advisor", "the outsider with leverage (Guild, foreign envoy)",
    "the indispensable functionary", "the power-behind-the-throne (hidden)"]), G + "courts.md")
T("court_power_source", "Courts — Power Source (and its orphan hook)", uniform([
    "Legitimacy (birth, mandate, an Imperial writ) — orphaned: a vacant claim everyone forges papers for",
    "The treasury — orphaned: unguarded gold; whoever takes it funds a coup",
    "Immaculate sanction — orphaned: a blessing withdrawn; heresy charges fly",
    "A bound god / elemental — orphaned: the binding lapses; the god is loose and owed",
    "The Realm garrison / legion detachment — orphaned: leaderless troops up for the highest bidder",
    "Guild credit / a trade monopoly — orphaned: a defaulted debt; the caravan reroutes",
    "A spy network — orphaned: masterless agents selling to anyone",
    "Blackmail (held on a Dynast) — orphaned: the file resurfaces with no owner",
    "An indispensable office (water, tribute, the courts) — orphaned: the seat empties; the function fails",
    "Popular love (a hero, a feeder of the poor) — orphaned: a leaderless mob looking for a champion",
    "A sorcerer's working / a relic — orphaned: an unattended power source anyone can claim",
    "Marriage alliance / hostages — orphaned: a broken match; both Houses feel the slight"]), G + "courts.md")
T("court_agenda", "Courts — Actor Agenda", uniform([
    "hold what they have", "take a rival's power source", "install / depose the seat-holder",
    "cover a crime", "court the PC as a tool", "burn it all down rather than lose"]), G + "courts.md")
T("court_stakes", "Courts — Central Conflict Stakes", uniform([
    "succession", "the treasury / tribute", "a marriage", "a heresy / Immaculate ruling",
    "a war (start it / stop it)", "control of a bound god or relic", "exposure of a scandal",
    "the PC themselves (both want to recruit or remove them)"]), G + "courts.md")
T("court_minor_actor", "Courts — Minor Actor (an entry point / door)", d10([
    "a slighted heir", "an indebted gambler", "a true believer",
    "a frightened servant who sees all", "a bitter veteran",
    "a Guild clerk with the real ledgers", "a discarded lover", "a captive / hostage",
    "a feral god of the household shrine", "a child who repeats secrets"]), G + "courts.md")
T("court_defenses", "Courts — Defenses (if the PC attacks)", uniform([
    "Dragon-Blooded house guard (combat)", "a bound god / elemental ward",
    "the garrison (a battle group)", "Immaculate retaliation (the Wyld Hunt hears)",
    "social: ruin the PC's name, not their body", "a poisoner / assassin on retainer",
    "they scatter and go to ground (no target)",
    "they have a hostage / leverage on someone the PC loves"]), G + "courts.md")
T("court_consequences", "Courts — Consequences if Destroyed", uniform([
    "a power vacuum a worse faction fills", "the orphaned power source becomes a free prize",
    "famine / chaos hits the dependent community", "a rival House moves in",
    "the bound god is freed and vengeful", "the PC inherits the seat — and its Problems",
    "a martyr is made; the cause grows",
    "nothing changes; the bureaucracy reabsorbs the wound"]), G + "courts.md")

# ============================================================ COMMUNITIES
T("community_nature", "Communities — Nature (Feature seed / likely tell)", d10([
    "Farming village (rice, grain) — full granaries, a harvest festival; tell: a shrine to a local field-god",
    "Herding camp / steppe clan — horses, warbeasts, mobility; tell: a totem-spirit, animal omens",
    "Mining town — jade, salt, or iron; a deep shaft; tell: something woke in the lowest tunnel",
    "River-port / trade-stop — a Guild factor, news, contraband; tell: a god of the ford takes tolls",
    "Wyld-edge frontier hamlet — hardy folk, strange crops; tell: mutations, doors onto elsewhere",
    "Refugee camp (war / famine fled) — desperate loyalty, hidden skills; tell: the dead of the old home still follow",
    "Fishing / coastal village — boats, pearls, a sea-shrine; tell: tribute owed to a thing in the water",
    "Logging / forest village (or tree-city) — timber, hunters, a sacred grove; tell: the forest's god is angry or absent",
    "Satrapy town under Realm tribute — a tax-house, a small garrison; tell: an Immaculate monk watches for Anathema",
    "Pilgrim / shrine town — a holy site, donations, a cult; tell: the patron god has gone silent"]),
    G + "communities.md")
T("community_leadership", "Communities — Leadership", uniform([
    "a council of elders", "a hereditary headman / matriarch",
    "a Realm-appointed reeve (resented)", "the local god speaks through a priest",
    "a Guild factor who really runs things", "a war-leader (recent threat)",
    "no one — leaderless, frightened", "a charismatic newcomer (savior or con)"]),
    G + "communities.md")
T("community_feature", "Communities — The Feature (worth protecting)", d10([
    "a hearthstone / demesne nearby", "a relic or shrine of real power",
    "a master craft (a smith, a weaver of note)", "a strategic pass / ford / harbor",
    "unusual loyalty / a militia that fights above its weight",
    "a secret heir or hidden Exalt among them", "a stockpile (grain, jade, medicine)",
    "a bound or friendly local god", "knowledge (a map, a rite, a name)",
    "simply that they're good people worth saving"]), G + "communities.md")
T("community_problem", "Communities — The Problem (the cry for a god; your hook)", uniform([
    "A monster / behemoth / strange-beast preys on them",
    "Bandits, a warlord, or a Realm tax-collector bleeds them dry",
    "Famine, blight, or a poisoned well",
    "A shadowland is spreading at the edge of the fields; the dead walk",
    "The local god has gone mad, silent, or greedy and demands too much",
    "A raksha / Fair Folk steals dreams, children, or names",
    "A feud or murder splits the village against itself",
    "The Wyld is creeping closer; crops and folk are changing",
    "A plague, or a curse laid by a slighted spirit",
    "An Immaculate monk has come hunting Anathema — and someone here qualifies",
    "A debt to the Guild / a Great House that will take people as payment",
    "A buried First Age thing under the town is waking (cross-ref Ruins)"]), G + "communities.md")
T("community_tell", "Communities — Supernatural Tell / Omen", uniform([
    "livestock born malformed", "a shrine over-laden or stripped bare",
    "ghost-lights / cold spots after dark", "the river / sky the wrong color",
    "a circle of dead grass, perfectly round", "charms and wards on every door",
    "a song or rite everyone knows but won't explain",
    "a stranger already here, watching (another Exalt? a spy?)"]), G + "communities.md")
T("community_stance", "Communities — Stance Toward a Revealed Exalt", uniform([
    "Awe — they kneel, offer the best they have; a god has come, they ask for miracles",
    "Desperate welcome — 'thank the heavens, DO something about the Problem'",
    "Immaculate fear — Anathema! they hide children, send word to the monk",
    "Wary bargaining — help is welcome, at a price, and watch your back",
    "Old loyalty — a grandmother's tale says their kind once protected here",
    "Greedy opportunism — how do WE profit from having a god in town?",
    "Hostile / armed — a prior Exalt wronged them; trust is gone",
    "Oblivious — they don't recognize what the PC is, yet"]), G + "communities.md")

# ============================================================ CHALLENGES
T("challenge_goal_type", "Challenges — Goal-type (match to the stated want)", d10([
    "build", "change-custom", "clear-ruin", "convince", "find", "kill", "rally",
    "resolve-conflict", "sneak/steal", "undo-magic"]), G + "challenges.md",
    note="Usually CHOSEN to match the PC's want, then roll that goal-type's complication table.")
_CH = {
 "build": ["the site is claimed / sacred", "the materials need a ruin-dive",
    "the only artisan is held hostage / indentured", "geomancy backfires without a rite",
    "a rival starts the same build faster", "the Guild owns the supply line",
    "a bound god demands tribute to allow it", "labor revolts mid-project",
    "the Realm taxes / forbids it", "it works — but draws a behemoth / elemental",
    "a hidden flaw will collapse it later", "finishing it requires a Mighty Deed (Projects)"],
 "change_custom": ["an Immaculate edict forbids it", "the elders' livelihood depends on the old way",
    "a god enforces the custom", "the change shames a powerful family",
    "it's load-bearing for a worse stability", "the young want it, the old will kill for tradition",
    "a martyr is needed first", "a rival Exalt champions the opposite", "it spreads too fast and warps",
    "it requires breaking an oath", "the Realm reads it as rebellion", "success creates a new, worse custom"],
 "clear_ruin": ["the Hazard reactivates", "someone got there first", "the 'monster' is a bound innocent",
    "clearing it frees something sealed", "a Wyld Hunt is en route", "the map is wrong",
    "the prize is cursed / keyed", "a patron wants it intact", "the path floods / collapses on a timer",
    "the inhabitants surrender — now they're dependents", "it's a trap baited by a rival",
    "the real ruin is below the ruin"],
 "convince": ["they have high Resolve; need an Intimacy lever first", "a rival whispers the opposite",
    "they demand a deed as proof", "they're under a Charm / oath",
    "telling the truth ruins someone the PC likes", "the audience is hostile (Immaculate crowd)",
    "the decider is a puppet; find the hidden hand", "a translation / cultural gap",
    "they want a bribe the PC can't afford", "success offends a third party",
    "they agree — then betray", "they'll only listen mid-crisis"],
 "find": ["it's hidden behind a riddle / cipher", "the only witness is dead / mad / ghost",
    "it's moving / being moved", "a rival hunts the same thing", "it's warded from scrying",
    "the trail runs through a court (Courts)", "it's in a shadowland / Wyld zone",
    "finding it alerts its guardian", "the 'it' is a decoy", "the source wants payment in secrets",
    "it's been split into pieces", "it finds the PC first"],
 "kill": ["it has a defensive Charm that no-sells the first blow", "it's protected by hostages / a crowd",
    "killing it frees something worse", "it accelerates when crashed (flees / grows)",
    "it's the wrong target (mistaken identity)", "it has a Wyld Hunt / faction backing",
    "it can only be killed by a specific means", "it's already dying — and warns of the real threat",
    "reinforcements on a clock", "it surrenders / begs", "its death triggers a curse on the killer",
    "it returns (ghost, regen, body-double)"],
 "rally": ["old feuds split the would-be allies", "they demand a champion's duel first",
    "a rival recruiter beat the PC there", "they're terrified of the Realm's reprisal",
    "a traitor in the ranks", "they need arms / food the PC must find", "a god must bless the muster",
    "they'll follow only after a visible miracle", "the leader is a coward / sellout",
    "numbers come, but green and unled", "success makes the PC a target faction",
    "they rally — for the wrong cause"],
 "resolve_conflict": ["both sides lie about the cause", "a third party profits from the strife",
    "the wronged party wants blood, not peace", "an old oath binds the fight",
    "a god / ghost feeds on the conflict", "the fair solution ruins a sympathetic figure",
    "the leaders are puppets", "peace requires a sacrifice", "the Realm wants it to continue",
    "a hidden grievance no one names", "settling it reignites a worse one",
    "only a marriage / hostage can seal it"],
 "sneak_steal": ["a bound god / elemental warden", "First Age wards trip on Essence use",
    "a witness who can't be silenced cleanly", "the prize is bait",
    "the layout shifts (Wyld / living-manse)", "a rival thief is inside already",
    "it's too heavy / large / alive to carry", "a Charm-user can sense intruders",
    "the route only opens on a schedule", "taking it triggers a curse / alarm-to-worse",
    "the owner is innocent / sympathetic", "success — but a clue points home to the PC"],
 "undo_magic": ["the caster must be found and faced", "unbinding frees what was bound",
    "it needs a rare reagent (a ruin-dive)", "the curse jumps to the breaker",
    "a counter-Charm is needed (sorcery / Essence)", "the ward is also load-bearing for a wall / dam",
    "a god owns the working and objects", "the victim resists being freed",
    "it's not magic — it's mundane (the diagnosis is the trap)", "partial undoing makes it worse",
    "the Immaculate Order wants the working studied, not destroyed",
    "undoing it reveals an uglier truth beneath"],
}
for k, opts in _CH.items():
    T(f"challenge_{k}", f"Challenges — Complication: {k.replace('_', '-')}", uniform(opts), G + "challenges.md")

# ============================================================ CULTS
T("cult_patron", "Cults — Patron (worshipped power)", d10([
    "A god of a place (river, mountain, ford, harvest) — local, transactional, jealous of tribute",
    "A god of a craft or trade — guild-like; bound to a profession",
    "An animal totem (steppe / forest clan) — shamanic; omens, beast-spirits, taboos",
    "The Immaculate Dragons (an Order cell) — doctrine, monks, Anathema-hunting",
    "An Exalt as living god (the PC, or a rival) — new, fervent, fragile; built on a person",
    "A dead hero / ancestor cult — graves, oaths, a ghost that may answer",
    "A demon (Yozi-touched, secret) — hidden, transgressive, hunted if found",
    "A Deathlord / the Neverborn (a death-cult) — shadowland-fed, nihilist, recruits the grieving",
    "A behemoth or Wyld-thing held as divine — terrible, propitiated, not loved",
    "A syncretic mix (roll twice; reconcile or schism) — tension built in"]), G + "cults.md")
T("cult_severity", "Cults — Holy-Law Severity (power gained / problem incurred)", uniform([
    "Loose / folk-faith — broad reach, easy growth; but shallow loyalty, scatters under pressure",
    "Customary — steady tithes, local trust; but complacent, co-opted by the powerful",
    "Devout — reliable miracles, a militia of believers; but intolerant, makes enemies",
    "Strict — fierce obedience, real supernatural aid; but schisms over doctrine, heretics breed",
    "Zealous — fanatic devotees, willing martyrs; but violent, the Realm/neighbors move against it",
    "Absolute / sacrificial — the patron answers directly; but demands blood, rots from within"]),
    G + "cults.md", note="Higher severity raises threat-Magnitude but lowers Cohesion.")
T("cult_feature", "Cults — Feature (what it can do)", uniform([
    "a real miracle on tap (heal, bless crops, ward)", "a militia of true believers",
    "a spy web of the pious (everyone confesses)", "a treasury of tithes / sacred relics",
    "the patron grants a Charm-like boon to clergy", "sanctuary network (safe houses across a region)",
    "legitimacy (the local lord needs their blessing)", "a holy site / demesne the patron empowers"]),
    G + "cults.md")
T("cult_problem", "Cults — Inherent Problem (the hook; take 1-2)", uniform([
    "a schism brewing over doctrine / succession",
    "the patron is waning, mad, or absent (miracles failing)",
    "a charismatic heretic splitting the flock",
    "the Realm / Immaculate Order marks it for suppression",
    "it demands a sacrifice the faithful are starting to question",
    "a rival cult contests the same patron / territory",
    "corrupt clergy embezzle tithes / abuse the flock",
    "the patron's true nature is a secret that would shatter it (a 'god' that's a demon, a hero that's a ghost)"]),
    G + "cults.md")
T("cult_growth", "Cults — How It Grows (and its counter)", uniform([
    "by miracle (a public wonder wins converts) — counter: expose the miracle",
    "by charity (feeds the poor; loyalty follows bread) — counter: starve the charity",
    "by the sword (convert or be cast out) — counter: break the war-band",
    "by patronage (a lord adopts it; top-down) — counter: turn the lord",
    "by infiltration (quiet, cell by cell, families first) — counter: out the cells",
    "by crisis (every disaster swells the ranks) — counter: solve the crises first"]), G + "cults.md")
T("cult_subtype", "Cults — Faction Subtype (Goal archetype for its faction turn)", uniform([
    "Theocrat — an Immaculate cell or established temple (consolidates, enforces doctrine)",
    "Predator — a death-cult or demon-cult (feeds on a region, recruits the desperate)",
    "Survivor — a folk-faith under Realm pressure (hides, hoards loyalty)",
    "Schemer — a secret / syncretic cult working through other factions",
    "Conqueror — a zealous expansionist faith (convert by sword)",
    "Tyrant — an Exalt-worship cult bound to one ruler's cult of personality"]),
    G + "cults.md", note="Usually CHOSEN to fit the cult, then drives its ex_faction.py turn.")

# ============================================================ ADVENTURES
T("adventure_situation", "Adventures — Situation (the state of play)", uniform([
    "a settlement under a Problem (Communities)", "a court mid-intrigue (Courts)",
    "a ruin newly opened (Ruins)", "a faction on the move (army, caravan, Wyld Hunt)",
    "a cult rising or schisming (Cults)", "a god / spirit out of balance",
    "a shadowland spreading", "a Wyld incursion / raksha raid",
    "a succession or a death of a power", "a Realm crackdown (tribute, Anathema-hunt)",
    "a natural disaster (flood, quake, blight)", "a rival Exalt's scheme bearing fruit"]),
    G + "adventures.md")
T("adventure_draw", "Adventures — Draw (why the PC engages)", uniform([
    "Reward: an artifact, a hearthstone, a demesne",
    "A person in danger the PC cares about (or could)",
    "A debt owed to the PC comes due", "A mystery / a Truth half-glimpsed",
    "Tribe / cult / charge the PC protects is threatened",
    "A rival the PC wants to thwart is involved",
    "A chance to grow a Project (build, rally, claim)",
    "Knowledge: a First Age secret, a lost name",
    "Reputation / a chance to be seen as a god", "An oath or Intimacy demands action",
    "A faction offers patronage for one job", "Simple justice: a wrong the PC can't walk past"]),
    G + "adventures.md")
T("adventure_threat", "Adventures — Threat (what pushes back)", uniform([
    "A rival Exalt (Dragon-Blood, Solar, Lunar, Abyssal)", "The Wyld Hunt closing in",
    "A behemoth / strange-beast (Foes)", "A bound or angry god / elemental",
    "A Deathlord's agent + the restless dead", "Raksha / Fair Folk and their unreality",
    "A Great House / the Realm garrison", "The Guild and its money and muscle",
    "A sorcerer with bound demons",
    "A failing First Age Hazard (radiation, stasis, miasma)",
    "A ticking clock (ritual, tribute deadline, spreading rot)",
    "The PC's own past / a secret that could surface"]), G + "adventures.md")

# ============================================================ FOES
T("foe_attack_pattern", "Foes — Attack-Pattern (signature offense)", d10([
    "Onslaught flurry — multiple withering attacks to strip the PC's Initiative fast",
    "Crippling decisive — one big decisive aimed to land a wound penalty / Crippling effect",
    "Opening ambush — surprise decisive from concealment before Join Battle settles",
    "Gambit specialist — leans on gambits: disarm, knockdown, grapple (set difficulty)",
    "Reach / zone control — denies approach; punishes movement into its range",
    "Poison / lingering — low up-front damage, a debuff that ticks each turn (Essence-fueled)",
    "Battle-group / swarm — attacks as a unit; Magnitude soaks losses; drowns in numbers",
    "Essence blast — ranged Charm attack ignoring some soak / Hardness",
    "Counter-puncher — weak offense, devastating on the riposte",
    "Escalator — grows stronger as the fight drags / as it takes damage"]), G + "foes.md")
T("foe_defense", "Foes — Defensive Ability", d10([
    "Perfect dodge/parry (1/round) — spends motes to no-sell one attack outright",
    "Counterattack on miss/parry — a reflexive withering/decisive when the PC fails to land",
    "High Hardness — shrugs decisive damage below a threshold (armor / Charm)",
    "Damage cap / immunity — a damage type (fire, cold, poison, lethal) is halved or ignored",
    "Regeneration — heals health levels each turn unless a condition is met",
    "Soak-stacking ward — reflexive soak boost when struck",
    "Hostage / meatshield — redirects harm onto a captive or minion",
    "Discorporation — becomes immaterial / mist to escape harm (spirit, raksha)",
    "Reset on crash — when Initiative-crashed, reflexively repositions and resets",
    "Untouchable while X — invulnerable until a vulnerability is exposed (a seal, a name, daylight)"]),
    G + "foes.md")
T("foe_mobility", "Foes — Mobility", uniform([
    "flight", "burrowing (strikes from below)", "teleport / blink (Essence)",
    "wall- / ceiling-crawl", "aquatic (drags foes under)",
    "supernatural Speed Bonus (always acts first to reposition)",
    "phasing through matter (immaterial passage)", "mounted / on a warbeast"]), G + "foes.md")
T("foe_impairing", "Foes — Impairing Power (the save-or-suck)", d10([
    "Fear aura — onslaught to Resolve; failed = Initiative loss / can't approach",
    "Paralysis / stasis — a gambit or Charm that roots the PC in place",
    "Mind-control gambit — a social attack mid-combat: turn an ally, force a step back",
    "Mutation / curse touch — lasting penalty until cleansed (Challenges: undo-magic)",
    "Mote-drain / anima-douse — strips the PC's motes or suppresses Charms",
    "Blinding / sense-deny — fog, darkness, illusion: attack penalties",
    "Confusion / Wyld-warp — the battlefield itself shifts (raksha, Wyld zone)",
    "Disarm / sunder — removes the PC's weapon or breaks gear",
    "Sticky / grapple-lock — holds the PC fast, dragging Initiative down each turn",
    "Despair / Intimacy-strike — a social nuke that erodes a motivating Intimacy"]), G + "foes.md")

# ---------------------------------------------------------------- report
print(f"BUILT {len(built)} companion tables in {GEN}")
if errors:
    print("\nERRORS:"); [print("  X", e) for e in errors]; sys.exit(1)
print("Coverage OK for every table (sums to 100 / 10).")
print("Verify with: python3 .claude/skills/mythic-gm/scripts/bridge.py validate .claude/skills/exalted3e/bridge")
