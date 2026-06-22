# Setting Layer — Index & Spine

The deduplicated AI-GM "card" layer for solo-Lunar Exalted 3e. Every entity is compressed to a **card** the GM can run a scene off (Header · Tone · Surface vs. Truth+triggers · Clocks · Hooks · Handles · Links · Vault) per the *Setting Card Template*. Prose stays in `vault/`; each card cites its source as `Book › Heading`.

**How to use in play:** orient with the geography spine below → jump to the file → read Header+Tone+Surface, narrate, pull a Hook → resolve via Handles (`../statblocks/00_index.md` for foes, `dice.py`/`ex_*` for rolls) → never narrate **Truth** until its trigger fires → at scene end tick **Clocks** and follow **Links**. The PC is a **Lunar**; default kin = the **Silver Pact**; default enemy = the **Realm** + its **Wyld Hunt**.

---

## The Spine — cosmology & geography at a glance

**Creation** = a flat world on the chaos-sea of the **Wyld**, anchored by five **Elemental Poles**. Reality is firmest at the center, thinnest at the rim.

```
                          THE WYLD  (chaos; Lunar refuge)
        ┌───────────────────────────────────────────────────┐
        │   NORTH — Pole of Air (ice, Lunar home turf)       │
        │  WEST          BLESSED ISLE          EAST          │
        │  Pole of      Pole of Earth         Pole of Wood   │
        │  Water    (Imperial Mtn; the Realm)  (free cities) │
        │   SOUTH — Pole of Fire (deserts, glass cities)     │
        └───────────────────────────────────────────────────┘
   beyond/beside Creation:  YU-SHAN (Heaven)  ·  the UNDERWORLD (the dead)  ·  MALFEAS (Hell)
```

- **Blessed Isle** (center, Pole of Earth): seat of the **Realm** (the Dragon-Blooded empire) → `directions/blessed_isle.md`.
- **The Threshold** (everything beyond the Inland Sea), four Directions:
  - **North** — Pole of Air; ice & iron; the Bull of the North, Whitewall, the Haslanti, Icewalkers; **Lunar home turf** → `directions/north.md`.
  - **East** — Pole of Wood; the Scavenger Lands, Nexus, Lookshy → `directions/east.md`.
  - **South** — Pole of Fire; Chiaroscuro, the Varang, An-Teng, the Lintha → `directions/south.md`.
  - **West** — Pole of Water; Wavecrest, the Azurite Empire, the Tya → `directions/west.md`.
- **Lunar Dominions** (the Pact's strongholds, spread across all Directions) → `directions/lunar_dominions.md`.
- **The Otherworlds** → `03_otherworlds.md`: the **Wyld** (raw chaos; a Lunar's refuge), the **Underworld** (land of the dead; reached via shadowlands), **Yu-Shan** (the bureaucratic Heaven), **Malfeas** (the demon-city prison of the Yozis).
- **The era:** the **Age of Sorrows / Time of Tumult** — the Scarlet Empress vanished ~5 yrs ago (RY 768); the Realm fractures, the Wyld Hunt is at its weakest, the Solars have returned. The window the Lunar campaign exploits. Full concept layer → `01_cosmology.md`.

---

## Directory (files in this layer)

| File | Contents |
|---|---|
| `00_index.md` | this spine + gazetteer + directory |
| `01_cosmology.md` | Creation, Essence, the Exalted types, Luna/Lunars, the Great Curse, fate, the spirit world, the Age of Sorrows, the Usurpation |
| `03_otherworlds.md` | the Wyld · Fair Folk · the Underworld · ghosts · shadowlands · Thorns · Yu-Shan · Malfeas · behemoths |
| `04_factions.md` | the faction board: Silver Pact · Realm · Great Houses · Immaculate Order · Lookshy · Guild · Deathlords · Fair Folk · Bureau of Destiny · Malfeas — w/ Magnitude/Cohesion/Trouble/Features/Problems/Interest/Reach/Goal + Tracks |
| `05_named_npcs.md` | NPC cards/pointers: Lunar elders (Shahan-yas) · the Bull's Circle · the Realm (Empress, Mnemon, V'neef, Regent) · Deathlords · Sidereal leaders |
| `06_bestiary_lore.md` | lore cards (spirits · demons · the dead · Fair Folk · behemoths · animals), each → `../statblocks/00_index.md` |
| `directions/blessed_isle.md` | the Realm's heart: the Isle, Imperial City, Imperial Mountain, satrapies |
| `directions/north.md` | **PRIORITIZED** — Lunar home turf: Whitewall, Bull's empire, Plenilune, Saltspire League, Icewalkers, Haslanti, Fortitude, Clovina, Ascension/Notch, Gethamane |
| `directions/east.md` | Nexus, Hundred Kingdoms, Halta, Linowan, Wolf's Paw, Champoor (+Lookshy/Sijan/Great Forks pointers) |
| `directions/south.md` | Chiaroscuro, Ember, Varang, An-Teng, the Lintha (+Gem/Harborhead/Dajaz pointers) |
| `directions/west.md` | Wavecrest, the Azurite Empire, the Tya (+Skullstone/Wu-Jian pointers) |
| `directions/lunar_dominions.md` | **PRIORITIZED** — Iscomay, Mahalanka, Ma-Ha-Suchi's Lair, Sunken Luthe, the Caul, Skandhar-Bhal, Touman, Bronze Tide, Eskari (+dominion pointers) |
| `../statblocks/00_index.md` | tagged index of ~257 ready-to-run statblocks (AotR · HDNP · Core Ch8 · Lunars Ch9) |

---

## Gazetteer — one line per card

### Concepts (`01_cosmology.md`)
- **Creation** — flat world on the Wyld, five Elemental Poles; firm at center, thin at rim.
- **Essence** — the fuel of all magic; mortals can't wield it, the Exalted shape it into Charms & sorcery.
- **The Exalted** — god-chosen champions; Solar/Lunar/Sidereal (Celestial) > Dragon-Blooded (Terrestrial) + Abyssal/Liminal/Exigent.
- **Luna & the Lunar Exalted** — the PC's kind: shapeshifting apex-predator heroes, 3 moon-phase castes, rage-fueled.
- **The Great Curse** — the flaw in every Exalt; for Lunars, Limit → a forced Limit Break.
- **Fate & the Loom** — destiny woven in Yu-Shan, read/rewritten by Sidereals.
- **The Spirit World** — gods (portfolio overseers), elementals (material spirits), demons (enslaved Yozi-souls); all crave worship.
- **The Age of Sorrows** — RY 768; Empress gone 5 yrs; Realm fracturing, Wyld Hunt weakest, Solars returned.
- **The Usurpation** — the Sidereals had the Dragon-Blooded murder the Solars; the wound behind the Lunars' rage.

### Otherworlds (`03_otherworlds.md`)
- **The Wyld** — raw chaos beyond the rim; mutates/dissolves the unprepared; a Lunar's refuge.
- **The Fair Folk (raksha)** — soulless chaos-beings who eat souls/dreams, wear gossamer masks, bound by their bargains.
- **The Underworld** — sunless mirror-world of the dead; salt repels, blood lures.
- **Ghosts & the Restless Dead** — lingering souls; hungry ghosts burn in sunlight.
- **Shadowlands** — seams where Creation & the Underworld overlap; cross by night → the dead's world.
- **Thorns** — fallen city, capital of the Deathlord Mask of Winters atop the behemoth Juggernaut; eyes the River Province.
- **Yu-Shan (Heaven)** — continent-sized city of gods & bureaucracy; the Loom of Fate; divine slums.
- **Malfeas (Hell)** — the brass demon-city under a green sun; prison of the Yozis; source of summonable demons.
- **Behemoths** — fortress-sized discarded prototypes of life; redirect, don't fight.

### Factions (`04_factions.md`) — Track starts in ( )
- **The Silver Pact** (+1) — the only Lunar society; cub-rescue + favor economy; tear down the Realm.
- **The Realm** (−3) — the wounded Dragon-Blooded empire; succession war looming; the prime enemy.
- **The Great Houses** (−2) — ten rival Dynastic houses carving up the Realm for the throne.
- **The Immaculate Order** (−3) — the state faith + Wyld Hunt; brands Solars/Lunars Anathema; secretly Sidereal-run.
- **Lookshy** (−2) — Shogunate-heir military power in the East; hoards First Age weapons.
- **The Guild** (0) — the amoral merchant leviathan; trades with anyone, including a Lunar.
- **The Deathlords** (−2) — undead Solar-ghost kings out to end all existence; ride the Abyssals.
- **The Fair Folk** (−1) — chaos courts that feed on souls; raid or bargain.
- **The Bureau of Destiny** (−2 Bronze / 0 Gold) — the hidden Sidereals; Bronze props the Realm, Gold backs the Solars.
- **Malfeas / demon-cults** (0/−2) — the imprisoned Yozis + their summonable demons + Creation's demon-cults.

### Named NPCs (`05_named_npcs.md`)
- **Lunar elders:** Ma-Ha-Suchi (unified-Realm dreamer) · Raksi (cannibal sorcerer-queen) · Leviathan (grieving sea-god) · Sha'a Oka (open-war Black Lion) · Lilith (wandering legend) · + Liseli, Rukhsara, Tayan, Amatha, Ül & more.
- **The Bull's Circle:** the Bull of the North (dying Solar warlord) · Samea, Raneth, Crimson Antler.
- **The Realm:** the Scarlet Empress (absent keystone) · Regent Tepet Fokuf · Mnemon · V'neef · Cathak Cainan.
- **Deathlords:** Mask of Winters · the Lover Clad in the Raiment of Tears · the Silver Prince.
- **Bureau of Destiny:** Chejop Kejak (Bronze leader) · the Mouth of Peace.

### Places — North (`directions/north.md`, PRIORITIZED)
- **Whitewall** — Syndic-ruled refuge behind blessed walls; the Nightwalkers' Treaty; low by day, lethal by night.
- **The Bull of the North's Empire** — a dying Solar warlord's wounded conquest of Malice Bay.
- **Plenilune** — the empire's salt-rich, seething capital.
- **The Saltspire League** — the four salt-cities + revolting holdings around Malice Bay.
- **The Icewalkers** — three totem-beast nomad nations; ripe for a Lunar living-god patron.
- **The Haslanti League** — rising airship-tech oligarchy; the Grandmothers (spies).
- **Fortitude** — subterranean prison-city of warring gangs; the Buried God.
- **Clovina** — Mnemon tin satrapy with a buried ancestor-cult rebellion.
- **Ascension & Notch** — timeless warm monastery over a lawless freezing mine-pit.
- **Gethamane** — the underground city + the deep Underways.
- *(pointers: Tusk, Pneuma, Grieve, Karasch/Medo, Glass-Pine Wood.)*

### Places — East (`directions/east.md`)
- **Nexus** — the greatest trade city; lawless; the Council + the masked Emissary; Guild hub.
- **The Hundred Kingdoms** — dozens of weak, warring petty states; a Lunar-protectorate sandbox.
- **Halta** — treetop nation paying a soul-tithe to the Fair Folk of the forest floor.
- **The Linowan** — autumn-haired raider nation of spirit-masked masters; at war with Halta.
- **Wolf's Paw** — talking wolves rule a half-ruined city; humans serve.
- **Champoor** — the Nighted City, run from the shadows by a Court of secret-keeping gods.
- *(pointers: Lookshy, Great Forks, Sijan, Thorns, Ixcoatli.)*

### Places — South (`directions/south.md`)
- **Chiaroscuro** — glass metropolis of the Delzahn; Sesus satrapy; salt-warded shadowlands.
- **Ember** — five-tiered fire-city of the Nywera; twin-queen seers; secret Shogunate automatons.
- **The Varang City-States** — astrology-caste confederacy (the system is a sham); Realm satrapy.
- **An-Teng** — the Realm's pleasure-garden satrapy, seething toward rebellion; demon cult below.
- **The Lintha** — demon-blooded pirates of floating Bluehaven; the cult of Dukantha.
- *(pointers: Gem, Harborhead, Dajaz, Lathe, Ysyr, Prasad.)*

### Places — West (`directions/west.md`)
- **The Wavecrest Archipelago** — Realm breadbasket; volcano-gods fed by human sacrifice; a powderkeg.
- **The Azurite Empire** — sea-lord republic (DB barred from office); turtle-ships; the Kraken's Pool.
- **The Tya** — stateless free sailor-folk in communal lodges; bound patron-spirits (compeers).
- *(pointers: Skullstone, Wu-Jian, Abalone, Denzik, Makelo/Randan.)*

### Places — Blessed Isle (`directions/blessed_isle.md`)
- **The Blessed Isle** — the Realm's heart; the densest, deadliest ground for an Anathema.
- **The Imperial City** — the capital around the Imperial Manse; the Legion of Silence; power vacuum.
- **The Imperial Mountain** — the Pole of Earth; sacred, extreme, First Age wonders.
- *(satrapy pointers: Greyfalls, Chiaroscuro, Varang, An-Teng, Clovina, Wavecrest, Prasad; Lookshy = faction.)*

### Lunar Dominions (`directions/lunar_dominions.md`, PRIORITIZED)
- **Iscomay, the Empire of the Bear** — a janissary empire (True Voice) mobilizing for war on the Realm.
- **Mahalanka** — Raksi's sorcerous apefolk empire even the Realm avoids.
- **The Nameless Lair of Ma-Ha-Suchi** — a beastfolk bastion in the SE jungle; the Three Mothers.
- **Sunken Luthe** — Leviathan's drowned city; the Pact's Western war-HQ.
- **The Caul** — a living sibling-continent; the open-war front; the five Shrine Cities.
- **Skandhar-Bhal** — hidden valley theocracy guarding the Moon-That-Fell.
- **The Touman Clans** — conqueror-nomads settling Carnelian; Wake the hero-aunt.
- **The Bronze Tide** — a refugee war-fleet (Lukha) fleeing a soul-eating fae empire.
- **The Eskari** — savanna clans secretly militarized by the trickster Smiling Zamisha.
- *(pointers: Shadow Fang Vanguard, Black Winter Boneyard, Shattersea Bastion, Mount Namas, the Green Rose, Lake Nyandi, Fulgurite Spire, Star Jasmine Pavilion, Eye of the Killing Storm, Luz Liura.)*

---

## Coverage notes & gaps
- **Breadth over depth by design:** every major entity gets a tight card; minor locales are pointers under each Direction (cite the vault for full text).
- **North & Lunar dominions are deepest** (the solo-Lunar priority).
- **Statblocks** (~257) are indexed in `../statblocks/00_index.md`; heavier antagonist supplements (Abyssals, Dragon-Blooded, Sidereals, Exigents, Alchemicals) are in the vault but out of scope for that index — mine directly if needed.
- **Known gaps / thin spots:** Gethamane (brief in the vault — expand via the Underways); the Far East (Ixcoatli), Dreaming Sea (Ysyr, Volivat), and Northeast (Fray, the Gathering Suns) are pointer-only; Skullstone and Lookshy have faction/pointer coverage but no full place card (detailed in supplements not in scope). The **Tamuz** elder named in some lists does not appear in *Fangs at the Gate* (omitted).
