#!/usr/bin/env python3
"""ex_npc.py — quick antagonist statting by tier, in Exalted 3e units.
Prints a ready block (paste into ex_combat add) + a Tactics reminder.
  stat <tier> [--name N]   tiers: mortal | elite | hero | young-exalt | exalt | legendary
Fill Charms from charms/antagonist_pools/<type>.md as appropriate.
"""
import sys
TIERS={
 "mortal":   dict(ess=0,motes=0,wa=2,eva=2,par=2,soak=2,hard=0,hl=7,acc=6,base=7,charms=0),
 "elite":    dict(ess=1,motes=0,wa=3,eva=3,par=3,soak=5,hard=0,hl=7,acc=9,base=10,charms=0),
 "hero":     dict(ess=2,motes=10,wa=4,eva=4,par=4,soak=7,hard=2,hl=7,acc=11,base=11,charms=2),
 "young-exalt":dict(ess=2,motes=13,wa=5,eva=5,par=5,soak=8,hard=4,hl=8,acc=12,base=11,charms=4),
 "exalt":    dict(ess=3,motes=16,wa=6,eva=6,par=6,soak=10,hard=6,hl=8,acc=14,base=13,charms=6),
 "legendary":dict(ess=5,motes=40,wa=7,eva=7,par=7,soak=12,hard=8,hl=9,acc=16,base=15,charms=10),
}
TACT=["open with a surprise/ambush decisive if the PC is unaware",
      "build Initiative with withering until 12+, then a decisive",
      "if Crashed, disengage/retreat to survive to reset to base (3 turns)",
      "spend the signature social or mobility Charm before melee",
      "focus the wounded; use onslaught by attacking after an ally",
      "flee or parley if reduced below half HL and outmatched"]
def main():
    a=sys.argv[1:]
    if not a or a[0]!="stat": print(__doc__); return
    t=a[1]; 
    if t not in TIERS: sys.exit(f"tiers: {', '.join(TIERS)}")
    s=TIERS[t]; name=a[a.index("--name")+1] if "--name" in a else t
    print(f"# {name}  (tier: {t})")
    print(f"Essence {s['ess']} · motes {s['motes']} · Join Battle pool {s['wa']}")
    print(f"Evasion {s['eva']} · Parry {s['par']} · soak {s['soak']} · Hardness {s['hard']} · HL {s['hl']}")
    print(f"Accuracy ~{s['acc']} · withering base (Str+wpn) ~{s['base']} · Charm slots: {s['charms']}")
    print(f"add → python3 scripts/ex_combat.py add {name} --init 3 --evasion {s['eva']} --parry {s['par']} "
          f"--soak {s['soak']} --hardness {s['hard']} --hl {s['hl']} --str-wdmg {s['base']}")
    print("Tactics:"); [print(f"  {i+1}. {x}") for i,x in enumerate(TACT)]
if __name__=="__main__": main()
