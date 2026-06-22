#!/usr/bin/env python3
"""ex_faction.py — the faction turn engine (honest, shown). State in campaign_state.json.
  add <name> --mag M [--goal G] [--reach R] [--feature "x"] [--problem "y"]
  turn                  run a season: each faction acts in random order (Consolidate/Strike)
  strike <A> <B>        opposed Contest (A's die vs B's die); loser gains a Problem
  status
Magnitude die: 1→d6 2→d8 3→d10 4→d12 5→d20. Trouble = #Problems; collapse if Trouble ≥ die max.
"""
import os,random,sys
sys.path.insert(0,os.path.dirname(os.path.abspath(__file__))); import state as ST
DIE={1:6,2:8,3:10,4:12,5:20}
def die(m): return DIE.get(int(m),6)
def main():
    a=sys.argv[1:]
    if not a or a[0] in ("-h","--help"): print(__doc__); return
    s=ST.load(); F=s.setdefault("factions",{})
    def opt(f,dv,c=str): return c(a[a.index(f)+1]) if f in a else dv
    if a[0]=="add":
        F[a[1]]={"mag":opt("--mag",1,int),"reach":opt("--reach",0,int),"goal":opt("--goal","survivor"),
                 "features":[opt("--feature","")] if "--feature" in a else [],
                 "problems":[opt("--problem","")] if "--problem" in a else []}
        ST.save(s); print(f"added faction {a[1]}")
    elif a[0]=="status":
        for n,f in F.items():
            print(f"{n}: Mag {f['mag']}(d{die(f['mag'])}) Reach {f['reach']} Goal {f['goal']}")
            print(f"   Features: {', '.join(x for x in f['features'] if x) or '—'}")
            print(f"   Problems: {', '.join(x for x in f['problems'] if x) or '—'}  (Trouble {len([x for x in f['problems'] if x])})")
    elif a[0]=="turn":
        names=list(F); random.shuffle(names)
        print("🌑 FACTION TURN (season)")
        for n in names:
            f=F[n]; d=die(f["mag"]); r=random.randint(1,d); trouble=len([x for x in f["problems"] if x])
            if r>trouble:
                f["reach"]+=max(1,f["mag"]//2); print(f"  {n}: Consolidate d{d}={r} > Trouble {trouble} → +Reach (now {f['reach']})")
            else:
                f["problems"].append("setback from a failed gambit"); print(f"  {n}: Consolidate d{d}={r} ≤ Trouble {trouble} → a Problem worsens")
            if len([x for x in f['problems'] if x])>=d: print(f"   ⚠ {n} COLLAPSES (Trouble ≥ {d})")
        ST.save(s)
    elif a[0]=="strike":
        A,B=F[a[1]],F[a[2]]; da,db=die(A["mag"]),die(B["mag"]); ra,rb=random.randint(1,da),random.randint(1,db)
        print(f"⚔ STRIKE {a[1]}(d{da}={ra}) vs {a[2]}(d{db}={rb})")
        loser=a[2] if ra>=rb else a[1]; F[loser]["problems"].append(f"struck by {a[2] if loser==a[1] else a[1]}")
        print(f"   {loser} loses the Contest → gains a Problem"); ST.save(s)
    else: sys.exit("see --help")
if __name__=="__main__": main()
