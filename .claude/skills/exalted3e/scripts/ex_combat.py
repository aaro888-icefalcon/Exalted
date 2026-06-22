#!/usr/bin/env python3
"""ex_combat.py — Exalted 3e tactical combat engine (RAW). Honest dice, shown.
State persists in campaign_state.json (set EX_STATE to override). Commands:
  new                                   start/clear a combat
  join  <name> --wa N [--pc] [stats]    Join Battle (Wits+Awareness)+3 → Initiative
  add   <name> --init I [stats]         add a combatant with explicit Initiative
       stats: --evasion E --parry P --soak S --hardness H --hl N --str-wdmg B
  withering <atk> <def> --acc N --base B [--ovw O]     withering attack
  decisive  <atk> <def> --acc N                        decisive attack (dmg = atk Initiative)
  gambit    <atk> <def> --acc N --diff D               gambit (special maneuver)
  endturn <name>                        clears their onslaught; handles 3-turn crash reset
  status                                show the board
Rules: success=die>=7; attack & withering-damage double 10s; DECISIVE damage does NOT.
Defense used = max(Evasion,Parry) - onslaught. Crash at Initiative<=0 → +5 Initiative Break to crasher.
Decisive: dmg pool = attacker Initiative; if pool<=Hardness no HL dmg; Initiative resets to 3 on any connect.
"""
import json, os, random, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import state as ST

def roll(n, double=10, target=7, decisive=False):
    n = max(0, int(n)); dice = sorted((random.randint(1,10) for _ in range(n)), reverse=True)
    if decisive:  # no double 10s
        succ = sum(1 for v in dice if v >= target)
    else:
        succ = sum(1 + (1 if v >= double else 0) for v in dice if v >= target)
    return succ, dice

TRACK = [0,-1,-1,-2,-2,-4]  # wound penalty per filled box (then Incapacitated)
def wound_pen(c):
    f = c.get("dmg",0)
    return TRACK[min(f, len(TRACK)-1)] if f>0 else 0

def get(s,name):
    c = s["combat"]["combatants"].get(name)
    if not c: sys.exit(f"no combatant '{name}' (status to list)")
    return c

def show(s):
    cb = s["combat"]
    print(f"⚔  COMBAT round {cb['round']}")
    order = sorted(cb["combatants"].items(), key=lambda kv:-kv[1]["init"])
    for n,c in order:
        tag = "PC" if c.get("pc") else "  "
        st = "DEFEATED" if c.get("defeated") else ("CRASH" if c["init"]<=0 else "")
        print(f"  [{tag}] {n:16} Init {c['init']:>3}  HL {c.get('dmg',0)}/{c.get('hl',7)}"
              f"  Def {max(c.get('evasion',0),c.get('parry',0))}-ons{c.get('onslaught',0)}"
              f"  soak {c.get('soak',0)} hard {c.get('hardness',0)}  {st}")

def add_combatant(s, name, init, a):
    def o(f,dv,cast=float):
        v=a[a.index(f)+1] if f in a else dv; return cast(v)
    s["combat"]["combatants"][name] = {
        "init":int(init), "base":3, "pc":("--pc" in a),
        "evasion":int(o("--evasion",2)), "parry":int(o("--parry",2)),
        "soak":int(o("--soak",2)), "hardness":int(o("--hardness",0)),
        "hl":int(o("--hl",7)), "dmg":0, "str_wdmg":int(o("--str-wdmg",o("--base",7))),
        "onslaught":0, "crash_turns":0, "defeated":False}

def defense(c): return max(c.get("evasion",0), c.get("parry",0)) - c.get("onslaught",0)

def crash_check(s, atk, dfn, before):
    c = get(s,dfn)
    if before>0 and c["init"]<=0:
        get(s,atk)["init"] += 5; c["crash_turns"]=0
        print(f"   💥 {dfn} CRASHED! {atk} gains +5 Initiative Break.")

def main():
    a = sys.argv[1:]
    if not a or a[0] in ("-h","--help"): print(__doc__); return
    s = ST.load(); cmd = a[0]
    def opt(f,dv,cast=str): return cast(a[a.index(f)+1]) if f in a else dv
    if cmd == "new":
        s["combat"]={"round":1,"combatants":{}}; ST.save(s); print("⚔ new combat (round 1)")
    elif cmd == "join":
        wa=opt("--wa",0,int); succ,dice=roll(wa); init=succ+3
        add_combatant(s,a[1],init,a); ST.save(s)
        print(f"🎲 {a[1]} Join Battle (Wits+Aware {wa}d10)={dice} → {succ} succ, Initiative {init}")
    elif cmd == "add":
        add_combatant(s,a[1],opt("--init",3,int),a); ST.save(s); print(f"added {a[1]}")
    elif cmd == "withering":
        atk,dfn=a[1],a[2]; ca,cd=get(s,atk),get(s,dfn)
        acc=opt("--acc",0,int)+ (0 if ca.get("dmg",0)==0 else wound_pen(ca))
        base=opt("--base",ca.get("str_wdmg",7),int); ovw=opt("--ovw",1,int)
        succ,dice=roll(acc); df=defense(cd)
        print(f"🎲 {atk} WITHERING vs {dfn}: acc {acc}d10={dice} → {succ} vs Def {df}")
        cd["onslaught"]=cd.get("onslaught",0)+1
        if succ<df: print(f"   MISS (onslaught on {dfn} now -{cd['onslaught']})"); ST.save(s); show(s); return
        thr=succ-df; raw=base+thr; pool=max(raw-cd.get("soak",0),ovw)
        idmg,ddice=roll(pool)
        before=cd["init"]
        ca["init"]+=idmg+1; cd["init"]-=idmg
        print(f"   HIT thr {thr}; raw {raw} - soak {cd.get('soak',0)} = {pool}d10={ddice} → {idmg} Init dmg")
        print(f"   {atk} Init +{idmg+1} → {ca['init']}; {dfn} Init -{idmg} → {cd['init']}")
        crash_check(s,atk,dfn,before); ST.save(s); show(s)
    elif cmd == "decisive":
        atk,dfn=a[1],a[2]; ca,cd=get(s,atk),get(s,dfn)
        if ca["init"]<=0: print(f"   {atk} is Crashed — cannot make decisive attacks."); return
        acc=opt("--acc",0,int)+(0 if ca.get("dmg",0)==0 else wound_pen(ca))
        succ,dice=roll(acc); df=defense(cd)
        print(f"🎲 {atk} DECISIVE vs {dfn}: acc {acc}d10={dice} → {succ} vs Def {df}")
        cd["onslaught"]=cd.get("onslaught",0)+1
        if succ<df:
            loss=2 if ca["init"]<=10 else 3; ca["init"]-=loss
            print(f"   MISS — {atk} loses {loss} Initiative → {ca['init']}"); ST.save(s); show(s); return
        pool=ca["init"]; hard=0 if cd["init"]<=0 else cd.get("hardness",0)
        if pool<=hard:
            print(f"   HIT but dmg pool {pool} ≤ Hardness {hard}: no damage."); ca["init"]=ca["base"]
        else:
            hd,hdice=roll(pool,decisive=True)
            cd["dmg"]=cd.get("dmg",0)+hd
            print(f"   HIT! decisive dmg {pool}d10 (no double10){hdice} → {hd} HL to {dfn} ({cd['dmg']}/{cd['hl']})")
            ca["init"]=ca["base"]
            if cd["dmg"]>=cd["hl"]: cd["defeated"]=True; print(f"   ☠ {dfn} DEFEATED!")
        print(f"   {atk} Initiative resets to base {ca['base']}.")
        ST.save(s); show(s)
    elif cmd == "gambit":
        atk,dfn=a[1],a[2]; ca,cd=get(s,atk),get(s,dfn); diff=opt("--diff",3,int)
        acc=opt("--acc",0,int); succ,dice=roll(acc); df=defense(cd)
        print(f"🎲 {atk} GAMBIT(diff {diff}) vs {dfn}: acc {acc}d10={dice} → {succ} vs Def {df}")
        if succ<df:
            loss=2 if ca["init"]<=10 else 3; ca["init"]-=loss; print(f"   MISS — lose {loss} Init")
        else:
            gp=ca["init"]; gs,gd=roll(gp,decisive=True)
            ok = gs>=diff
            ca["init"]-=(diff+1)
            print(f"   to-hit ok; gambit roll {gp}d10={gd} → {gs} vs diff {diff}: {'SUCCESS' if ok else 'fail'}; lose {diff+1} Init → {ca['init']}")
        ST.save(s); show(s)
    elif cmd == "endturn":
        c=get(s,a[1])
        if c["init"]<=0:
            c["crash_turns"]=c.get("crash_turns",0)+1
            if c["crash_turns"]>=3: c["init"]=3; c["crash_turns"]=0; print(f"   {a[1]} resets to base Initiative 3 (3 turns in Crash).")
        else: c["crash_turns"]=0
        c["onslaught"]=0; ST.save(s); print(f"{a[1]} turn ended (onslaught cleared).")
    elif cmd == "status": show(s)
    else: sys.exit("unknown cmd; see --help")
if __name__ == "__main__": main()
